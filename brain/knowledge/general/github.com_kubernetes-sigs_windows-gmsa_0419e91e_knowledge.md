---
id: github.com-kubernetes-sigs-windows-gmsa-0419e91e-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:20.821312
---

# KNOWLEDGE EXTRACT: github.com_kubernetes-sigs_windows-gmsa_0419e91e
> **Extracted on:** 2026-04-01 10:32:36
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520950/github.com_kubernetes-sigs_windows-gmsa_0419e91e

---

## File: `.gitignore`
```
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

#IDE files
.idea/
.vscode/
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing Guidelines

Welcome to Kubernetes. We are excited about the prospect of you joining our [community](https://github.com/kubernetes/community)! The Kubernetes community abides by the CNCF [code of conduct](../../../vault/archives/archive_legacy/AutoGPT/docs/content/code-of-conduct.md). Here is an excerpt:

_As contributors and maintainers of this project, and in the interest of fostering an open and welcoming community, we pledge to respect all people who contribute through reporting issues, posting feature requests, updating documentation, submitting pull requests or patches, and other activities._

## Getting Started

We have full documentation on how to get started contributing here:

<!---
If your repo has certain guidelines for contribution, put them here ahead of the general k8s resources
-->

- [Contributor License Agreement](https://git.k8s.io/community/CLA.md) Kubernetes projects require that you sign a Contributor License Agreement (CLA) before we can accept your pull requests
- [Kubernetes Contributor Guide](http://git.k8s.io/community/contributors/guide) - Main contributor documentation, or you can just jump directly to the [contributing section](http://git.k8s.io/community/contributors/guide#contributing)
- [Contributor Cheat Sheet](https://k8s.dev/cheatsheet) - Common resources for existing developers

## Generating Helm Charts and Index

When a chart needs to be updated, create the new version and the chart information. Run helm pack, then generate a new Helm chart index.yaml with the following command.

```Bash
helm repo index --url https://raw.githubusercontent.com/kubernetes-sigs/windows-gmsa/master/charts .
```
## Mentorship

- [Mentoring Initiatives](https://git.k8s.io/community/mentoring) - We have a diverse set of mentorship programs available that are always looking for volunteers!

<!---
Custom Information - if you're copying this template for the first time you can add custom content here, for example:

## Contact Information

- [Slack channel](https://kubernetes.slack.com/messages/kubernetes-users) - Replace `kubernetes-users` with your slack channel string, this will send users directly to your channel. 
- [Mailing list](URL)

-->
```

## File: `HEAD`
```
ref: refs/heads/master
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

## File: `OWNERS`
```
# See the OWNERS docs: https:/go.k8s.io/owners

approvers:
  - jsturtevant
  - marosset
  - zylxjtu

emeritus_approvers:
  - ddebroy
  - wk8
  - jayunit100

labels:
  - sig/windows
```

## File: `README.md`
```markdown
![Build Status](https://github.com/kubernetes-sigs/windows-gmsa/actions/workflows/build.yaml/badge.svg)

# Kubernetes Windows GMSA

External components to support [Windows' GMSA](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview) in Kubernetes.

## Community, discussion, contribution, and support

Learn how to engage with the Kubernetes community on the [community page](http://kubernetes.io/community/).

You can reach the maintainers of this project at:

- [Slack](http://slack.k8s.io/)
- [Mailing List](https://groups.google.com/forum/#!forum/kubernetes-dev)

### Code of conduct

Participation in the Kubernetes community is governed by the [Kubernetes Code of Conduct](../../../vault/archives/archive_legacy/AutoGPT/docs/content/code-of-conduct.md).

[owners]: https://git.k8s.io/community/contributors/guide/owners.md
[Creative Commons 4.0]: https://git.k8s.io/website/LICENSE
```

## File: `RELEASE.md`
```markdown
# Release Process

The Kubernetes Windows GMSA project is released on an as-needed basis. The process is as follows:

1. An issue is created proposing a new release with a changelog since the last release using the [Cut a release issue template](.github//ISSUE_TEMPLATE/new-release.md)
1. All [OWNERS](OWNERS) must LGTM this release issue
1. An OWNER runs `git tag -s $VERSION` from `master` branch and pushes the tag with `git push $VERSION`
1. An OWNER promotes the `gcr.io/k8s-staging-gmsa-webhook/k8s-gmsa-webhook` image built the tagged commit.
    1. Follow setup steps for `kpromo` from [here](https://github.com/kubernetes-sigs/promo-tools/blob/main/docs/promotion-pull-requests.md#preparing-environment) if needed
    1. Manually tag the desired container image in the [staging registry](https://console.cloud.google.com/gcr/images/k8s-staging-gmsa-webhook/GLOBAL) as `$VERSION`
    1. Run `kpromo pr` to open a pull request to have tagged container image promoted from staging to release registries

        ```bash
        kpromo pr --project gmsa-webhook --tag $VERSION --reviewers "@jayunit100 @jsturtevant @marosset" --fork {your github username}
        ```

    1. Review / merge image promotion PR
    1. Verify the image is available using `docker pull registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook:$VERSION`.  The image is pushed to the release repository via the post submit which can take an hour or two to trigger. View results at https://testgrid.k8s.io/sig-k8s-infra-k8sio#post-k8sio-image-promo

1. An OWNER creates a release with by
    1. Navigating to [releases](https://github.com/kubernetes-sigs/windows-gmsa/releases) and clicking on `Draft a new release`
    1. Selecting the tag for the current release version
    1. Setting the title of the release to the current release version
    1. Clicking `Auto-generate release notes` button (and editing what was generated as appropriate) 
    1. Adding instructions on how to deploy the current release **to the top of the releaes notes** with the following template:

        To deploy:

        ```bash
        K8S_GMSA_DEPLOY_DOWNLOAD_REV='$VERSION' \
            ./deploy-gmsa-webhook.sh --file ./gmsa-manifests \
            --image registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook:$VERSION
        ```

    1. Clicking on `Publish Release`
1. Update `image.tag` in `charts/gmsa/chart.yaml` to $VERSION and create new chart package:
    1. Run `helm package charts/gmsa`. Make sure the resulting tgz file is in the `charts/repo` folder.
    1. Run `helm repo index charts/repo/` to update the helm index
1. Update the **IMAGE_NAME** variable in `admission_webhook/deploy/deploy-gmsa-webhook.sh` to use the latest released image.
1. The release issue is closed
1. An announcement email is sent to `kubernetes-sig-windows@googlegroups.com` with the subject `[ANNOUNCE] Kubernetes SIG-Windows GMSA Webhook $VERSION is Released`
1. An announcement is posted in `#SIG-windows` in the Kubernetes slack.
```

## File: `SECURITY_CONTACTS`
```
# Defined below are the security contacts for this repo.
#
# They are the contact point for the Product Security Team to reach out
# to for triaging and handling of incoming issues.
#
# The below names agree to abide by the
# [Embargo Policy](https://github.com/kubernetes/sig-release/blob/master/security-release-process-documentation/security-release-process.md#embargo-policy)
# and will be removed and replaced if they violate that agreement.
#
# DO NOT REPORT SECURITY VULNERABILITIES DIRECTLY TO THESE NAMES, FOLLOW THE
# INSTRUCTIONS AT https://kubernetes.io/security/

ddebroy
michmike
PatrickLang
```

## File: `cloudbuild.yaml`
```yaml
# See https://cloud.google.com/cloud-build/docs/build-config

# this must be specified in seconds. If omitted, defaults to 600s (10 mins)
timeout: 1200s
# this prevents errors if you don't use both _GIT_TAG and _PULL_BASE_REF,
# or any new substitutions added in the future.
options:
  substitution_option: ALLOW_LOOSE
steps:
  - name:  'gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20230522-312425ae46'
    entrypoint: bash
    env:
    - DOCKER_CLI_EXPERIMENTAL=enabled
    - TAG=${_GIT_TAG}
    - PULL_BASE_REF=${_PULL_BASE_REF}
      # default cloudbuild has HOME=/builder/home and docker buildx is in /root/.docker/cli-plugins/docker-buildx
      # set the home to /root explicitly to if using docker buildx
    - HOME=/root
    args:
    - -c
    - |
      echo "Building / Pushing GMSA webhook container"
      gcloud auth configure-docker
      cd admission-webhook
      make release-staging
substitutions:
  # _GIT_TAG will be filled with a git-based tag for the image, of the form vYYYYMMDD-hash, and
  # can be used as a substitution
  _GIT_TAG: '12345'
  # _PULL_BASE_REF will contain the ref that was pushed to to trigger this build -
  # a branch like 'master' or 'release-0.2', or a tag like 'v0.2'.
  _PULL_BASE_REF: 'master'
```

## File: `code-of-conduct.md`
```markdown
# Kubernetes Community Code of Conduct

Please refer to our [Kubernetes Community Code of Conduct](https://git.k8s.io/community/code-of-conduct.md)
```

## File: `config`
```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/kubernetes-sigs/windows-gmsa
	fetch = +refs/heads/master:refs/remotes/origin/master
[branch "master"]
	remote = origin
	merge = refs/heads/master
```

## File: `description`
```
Unnamed repository; edit this file 'description' to name the repository.
```

## File: `packed-refs`
```
# pack-refs with: peeled fully-peeled sorted 
993de21c8f98a4def841b8de89aed688a95630d8 refs/remotes/origin/master
```

## File: `shallow`
```
993de21c8f98a4def841b8de89aed688a95630d8
```

## File: `admission-webhook/.dockerignore`
```
/dev/
/integration_tests/tmp/
```

## File: `admission-webhook/.gitignore`
```
/dev/
/integration_tests/tmp/
/testdata/
```

## File: `admission-webhook/Makefile`
```
.DEFAULT_GOAL := test
SHELL := /bin/bash

WEBHOOK_ROOT := $(CURDIR)

REGISTRY ?= registry.k8s.io/gmsa-webhook
STAGING_REGISTRY ?= gcr.io/k8s-staging-gmsa-webhook
IMAGE_NAME ?= k8s-gmsa-webhook
TAG ?=  $(shell git describe --tags --always `git rev-parse HEAD`)
WEBHOOK_IMG ?= $(REGISTRY)/$(IMAGE_NAME)

DEV_IMAGE_NAME = k8s-windows-gmsa-webhook-dev

CURL = $(shell which curl 2> /dev/null)
WGET = $(shell which wget 2> /dev/null)

ifeq ($(CURL)$(WGET),)
$(error "Neither curl nor wget available")
endif

UNAME = $(shell uname | tr A-Z a-z)
ifeq ($(UNAME),)
$(error "Unable to determine OS type")
endif

include make/*.mk

.PHONY: test
test: deps_install unit_tests integration_tests

# the UNIT_TEST_FLAGS env var can be set to eg run only specific tests, e.g:
# UNIT_TEST_FLAGS='-test.run TestHTTPWebhook' make unit_tests
.PHONY: unit_tests
unit_tests:
	go test -v -count=1 -cover $(UNIT_TEST_FLAGS)

.PHONY: integration_tests
integration_tests: image_build deploy_webhook run_integration_tests

.PHONY: integration_tests_chart
integration_tests_chart: image_build deploy_chart run_integration_tests

.PHONY: integration_tests_with_dev_image
integration_tests_with_dev_image: image_build_dev deploy_dev_webhook run_integration_tests

# the INTEGRATION_TEST_FLAGS env var can be set to eg run only specific tests, e.g.:
# INTEGRATION_TEST_FLAGS='-test.run TestHappyPathWithPodLevelCredSpec' make run_integration_tests
.PHONY: run_integration_tests
run_integration_tests:
	@ echo "### Starting integration tests with Kubernetes version: $(KUBERNETES_VERSION) ###"
	cd integration_tests && KUBECONFIG=$(KUBECONFIG) KUBECTL=$(KUBECTL) go test -count 1 -v $(INTEGRATION_TEST_FLAGS)

.PHONY: clean_integration_tests
clean_integration_tests:
	rm -rf integration_tests/tmp

.PHONY: clean
clean: cluster_clean clean_integration_tests deps_clean

.PHONY: release-staging 
release-staging: ## Builds and push webhook image to k8s-staging bucket
	REGISTRY=$(STAGING_REGISTRY) $(MAKE) image_build_and_push
```

## File: `admission-webhook/README.md`
```markdown
# Windows GMSA Webhook Admission controller

## Supported versions

This branch supports versions 1.23 and later. 

## How to deploy

Assuming that `kubectl` is in your path and that your cluster's kube admin config file is present at either the canonical location
(`~/.kube/config`) or at the path specified by the `KUBECONFIG` environment variable, simply run:
```bash
curl -sL https://raw.githubusercontent.com/kubernetes-sigs/windows-gmsa/master/admission-webhook/deploy/deploy-gmsa-webhook.sh | bash -s -- --file webhook-manifests.yml
```

Run with the `--dry-run` option to not change anything to your cluster just yet and simply review the change it would be doing.

Run with `--help` to see all the available options.

## Amazon EKS

According to the Amazon EKS certificate signing documentation, all clusters running Amazon EKS version 1.22 or newer supports the following signer beta.eks.amazonaws.com/app-serving for Kubernetes Certificate Signing Requests (CSR) which is compatible with the latest gMSA admission webhook installation. As a result, we need to replace kubernetes.io/kubelet-serving signer in the gMSA Webhook create-signed-cert.sh file with the following signer : beta.eks.amazonaws.com/app-serving
```

## File: `admission-webhook/cert_reloader.go`
```go
package main

import (
	"context"
	"crypto/tls"
	"sync"

	"github.com/fsnotify/fsnotify"
	"github.com/sirupsen/logrus"
)

type CertLoader interface {
	CertPath() string
	KeyPath() string
	LoadCertificate() (*tls.Certificate, error)
}

type CertReloader struct {
	sync.Mutex
	certPath    string
	keyPath     string
	certificate *tls.Certificate
}

func NewCertReloader(certPath, keyPath string) *CertReloader {
	return &CertReloader{
		certPath: certPath,
		keyPath:  keyPath,
	}
}

func (cr *CertReloader) CertPath() string {
	return cr.certPath
}

func (cr *CertReloader) KeyPath() string {
	return cr.keyPath
}

// LoadCertificate loads or reloads the certificate from disk.
func (cr *CertReloader) LoadCertificate() (*tls.Certificate, error) {
	cr.Lock()
	defer cr.Unlock()

	cert, err := tls.LoadX509KeyPair(cr.certPath, cr.keyPath)
	if err != nil {
		return nil, err
	}
	cr.certificate = &cert
	return cr.certificate, nil
}

// GetCertificateFunc returns a function that can be assigned to tls.Config.GetCertificate
func (cr *CertReloader) GetCertificateFunc() func(*tls.ClientHelloInfo) (*tls.Certificate, error) {
	return func(chi *tls.ClientHelloInfo) (*tls.Certificate, error) {
		return cr.certificate, nil
	}
}

func watchCertFiles(ctx context.Context, certLoader CertLoader) {
	logrus.Infof("Starting certificate watcher on path %v and %v", certLoader.CertPath(), certLoader.KeyPath())
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		logrus.Errorf("error creating watcher: %v", err)
	}

	go func() {
		defer watcher.Close()

		for {
			select {
			case event, ok := <-watcher.Events:
				if !ok {
					logrus.Errorf("watcher events returned !ok: %v", err)
					return
				}
				logrus.Infof("detected change in certificate file: %v", event.Name)
				_, err := certLoader.LoadCertificate()
				if err != nil {
					logrus.Errorf("error reloading certificate: %v", err)
				} else {
					logrus.Infof("successfully reloaded certificate")
				}
			case err, ok := <-watcher.Errors:
				if !ok {
					logrus.Errorf("watcher error returned !ok: %v", err)
					return
				}
				logrus.Errorf("watcher error: %v", err)
			case <-ctx.Done():
				logrus.Info("stopping certificate watcher")
				return
			}
		}
	}()

	err = watcher.Add(certLoader.CertPath())
	if err != nil {
		logrus.Fatalf("error watching certificate file: %v", err)
	}
	err = watcher.Add(certLoader.KeyPath())
	if err != nil {
		logrus.Fatalf("error watching key file: %v", err)
	}
}
```

## File: `admission-webhook/cert_reloader_test.go`
```go
package main

import (
	"context"
	"crypto/tls"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

// TestCertReloader tests the reloading functionality of the certificate.
func TestCertReloader(t *testing.T) {
	// Create temporary cert and key files
	tmpCertFile, err := os.CreateTemp("", "cert*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp cert file: %v", err)
	}
	defer os.Remove(tmpCertFile.Name()) // clean up

	tmpKeyFile, err := os.CreateTemp("", "key*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp key file: %v", err)
	}
	defer os.Remove(tmpKeyFile.Name()) // clean up

	// Write initial cert and key to temp files
	initialCertData, _ := os.ReadFile("testdata/cert.pem")
	if err := os.WriteFile(tmpCertFile.Name(), initialCertData, 0644); err != nil {
		t.Fatalf("Failed to write to temp cert file: %v", err)
	}

	initialKeyData, _ := os.ReadFile("testdata/key.pem")
	if err := os.WriteFile(tmpKeyFile.Name(), initialKeyData, 0644); err != nil {
		t.Fatalf("Failed to write to temp key file: %v", err)
	}

	// Setup CertReloader with temp files
	certReloader := NewCertReloader(tmpCertFile.Name(), tmpKeyFile.Name())
	_, err = certReloader.LoadCertificate()
	if err != nil {
		t.Fatalf("Failed to load initial certificate: %v", err)
	}

	// Mocking a certificate change by writing new data to the files
	newCertData, _ := os.ReadFile("testdata/cert.pem")
	if err := os.WriteFile(tmpCertFile.Name(), newCertData, 0644); err != nil {
		t.Fatalf("Failed to write new data to cert file: %v", err)
	}

	// Simulate reloading
	_, err = certReloader.LoadCertificate()
	if err != nil {
		t.Fatalf("Failed to reload certificate: %v", err)
	}
}

type mockCertLoader struct {
	certPath     string
	keyPath      string
	loadCertFunc func() (*tls.Certificate, error)
}

func (m *mockCertLoader) CertPath() string {
	return m.certPath
}

func (m *mockCertLoader) KeyPath() string {
	return m.keyPath
}

func (m *mockCertLoader) LoadCertificate() (*tls.Certificate, error) {
	return m.loadCertFunc()
}

func TestWatchingCertFiles(t *testing.T) {
	tmpCertFile, err := os.CreateTemp("", "cert*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp cert file: %v", err)
	}
	defer os.Remove(tmpCertFile.Name())

	tmpKeyFile, err := os.CreateTemp("", "key*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp key file: %v", err)
	}
	defer os.Remove(tmpKeyFile.Name())

	loadCertFuncChan := make(chan bool)
	done := make(chan bool)

	cl := &mockCertLoader{
		certPath: tmpCertFile.Name(),
		keyPath:  tmpKeyFile.Name(),
		loadCertFunc: func() (*tls.Certificate, error) {
			loadCertFuncChan <- true
			return &tls.Certificate{}, nil
		},
	}

	go func() {
		called := <-loadCertFuncChan
		assert.True(t, called)
		done <- true
	}()

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	watchCertFiles(ctx, cl)

	newCertData, _ := os.ReadFile("testdata/cert.pem")
	if err := os.WriteFile(tmpCertFile.Name(), newCertData, 0644); err != nil {
		t.Fatalf("Failed to write new data to cert file: %v", err)
	}

	<-done
}
```

## File: `admission-webhook/go.mod`
```
module github.com/kubernetes-sigs/windows-gmsa/admission-webhook

go 1.23.0

toolchain go1.23.7

require (
	github.com/fsnotify/fsnotify v1.8.0
	github.com/google/uuid v1.6.0
	github.com/mitchellh/go-homedir v1.1.0
	github.com/sirupsen/logrus v1.9.3
	github.com/stretchr/testify v1.9.0
	gotest.tools v2.2.0+incompatible
	k8s.io/api v0.32.2
	k8s.io/apimachinery v0.32.2
	k8s.io/apiserver v0.32.2
	k8s.io/client-go v0.32.2
)

require (
	github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc // indirect
	github.com/emicklei/go-restful/v3 v3.12.2 // indirect
	github.com/fxamacker/cbor/v2 v2.7.0 // indirect
	github.com/go-logr/logr v1.4.2 // indirect
	github.com/go-openapi/jsonpointer v0.21.0 // indirect
	github.com/go-openapi/jsonreference v0.21.0 // indirect
	github.com/go-openapi/swag v0.23.0 // indirect
	github.com/gogo/protobuf v1.3.2 // indirect
	github.com/golang/protobuf v1.5.4 // indirect
	github.com/google/gnostic-models v0.6.9 // indirect
	github.com/google/go-cmp v0.7.0 // indirect
	github.com/google/gofuzz v1.2.0 // indirect
	github.com/josharian/intern v1.0.0 // indirect
	github.com/json-iterator/go v1.1.12 // indirect
	github.com/mailru/easyjson v0.9.0 // indirect
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.2 // indirect
	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
	github.com/pkg/errors v0.9.1 // indirect
	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
	github.com/x448/float16 v0.8.4 // indirect
	golang.org/x/net v0.37.0 // indirect
	golang.org/x/oauth2 v0.28.0 // indirect
	golang.org/x/sys v0.31.0 // indirect
	golang.org/x/term v0.30.0 // indirect
	golang.org/x/text v0.23.0 // indirect
	golang.org/x/time v0.11.0 // indirect
	google.golang.org/protobuf v1.36.5 // indirect
	gopkg.in/evanphx/json-patch.v4 v4.12.0 // indirect
	gopkg.in/inf.v0 v0.9.1 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
	k8s.io/klog/v2 v2.130.1 // indirect
	k8s.io/kube-openapi v0.0.0-20250304201544-e5f78fe3ede9 // indirect
	k8s.io/utils v0.0.0-20241210054802-24370beab758 // indirect
	sigs.k8s.io/json v0.0.0-20241014173422-cfa47c3a1cc8 // indirect
	sigs.k8s.io/randfill v1.0.0 // indirect
	sigs.k8s.io/structured-merge-diff/v4 v4.6.0 // indirect
	sigs.k8s.io/yaml v1.4.0 // indirect
)

replace golang.org/x/text => golang.org/x/text v0.23.0

replace golang.org/x/term => golang.org/x/term v0.30.0

replace golang.org/x/time => golang.org/x/time v0.11.0

replace golang.org/x/sys => golang.org/x/sys v0.31.0

replace golang.org/x/net => golang.org/x/net v0.37.0
```

## File: `admission-webhook/go.sum`
```
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/emicklei/go-restful/v3 v3.12.2 h1:DhwDP0vY3k8ZzE0RunuJy8GhNpPL6zqLkDf9B/a0/xU=
github.com/emicklei/go-restful/v3 v3.12.2/go.mod h1:6n3XBCmQQb25CM2LCACGz8ukIrRry+4bhvbpWn3mrbc=
github.com/fsnotify/fsnotify v1.8.0 h1:dAwr6QBTBZIkG8roQaJjGof0pp0EeF+tNV7YBP3F/8M=
github.com/fsnotify/fsnotify v1.8.0/go.mod h1:8jBTzvmWwFyi3Pb8djgCCO5IBqzKJ/Jwo8TRcHyHii0=
github.com/fxamacker/cbor/v2 v2.7.0 h1:iM5WgngdRBanHcxugY4JySA0nk1wZorNOpTgCMedv5E=
github.com/fxamacker/cbor/v2 v2.7.0/go.mod h1:pxXPTn3joSm21Gbwsv0w9OSA2y1HFR9qXEeXQVeNoDQ=
github.com/go-logr/logr v1.4.2 h1:6pFjapn8bFcIbiKo3XT4j/BhANplGihG6tvd+8rYgrY=
github.com/go-logr/logr v1.4.2/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-openapi/jsonpointer v0.21.0 h1:YgdVicSA9vH5RiHs9TZW5oyafXZFc6+2Vc1rr/O9oNQ=
github.com/go-openapi/jsonpointer v0.21.0/go.mod h1:IUyH9l/+uyhIYQ/PXVA41Rexl+kOkAPDdXEYns6fzUY=
github.com/go-openapi/jsonreference v0.21.0 h1:Rs+Y7hSXT83Jacb7kFyjn4ijOuVGSvOdF2+tg1TRrwQ=
github.com/go-openapi/jsonreference v0.21.0/go.mod h1:LmZmgsrTkVg9LG4EaHeY8cBDslNPMo06cago5JNLkm4=
github.com/go-openapi/swag v0.23.0 h1:vsEVJDUo2hPJ2tu0/Xc+4noaxyEffXNIs3cOULZ+GrE=
github.com/go-openapi/swag v0.23.0/go.mod h1:esZ8ITTYEsH1V2trKHjAN8Ai7xHb8RV+YSZ577vPjgQ=
github.com/go-task/slim-sprig/v3 v3.0.0 h1:sUs3vkvUymDpBKi3qH1YSqBQk9+9D/8M2mN1vB6EwHI=
github.com/go-task/slim-sprig/v3 v3.0.0/go.mod h1:W848ghGpv3Qj3dhTPRyJypKRiqCdHZiAzKg9hl15HA8=
github.com/gogo/protobuf v1.3.2 h1:Ov1cvc58UF3b5XjBnZv7+opcTcQFZebYjWzi34vdm4Q=
github.com/gogo/protobuf v1.3.2/go.mod h1:P1XiOD3dCwIKUDQYPy72D8LYyHL2YPYrpS2s69NZV8Q=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/gnostic-models v0.6.9 h1:MU/8wDLif2qCXZmzncUQ/BOfxWfthHi63KqpoNbWqVw=
github.com/google/gnostic-models v0.6.9/go.mod h1:CiWsm0s6BSQd1hRn8/QmxqB6BesYcbSZxsz9b0KuDBw=
github.com/google/go-cmp v0.5.9/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/gofuzz v1.0.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/google/gofuzz v1.2.0 h1:xRy4A+RhZaiKjJ1bPfwQ8sedCA+YS2YcCHW6ec7JMi0=
github.com/google/gofuzz v1.2.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/google/pprof v0.0.0-20241029153458-d1b30febd7db h1:097atOisP2aRj7vFgYQBbFN4U4JNXUNYpxael3UzMyo=
github.com/google/pprof v0.0.0-20241029153458-d1b30febd7db/go.mod h1:vavhavw2zAxS5dIdcRluK6cSGGPlZynqzFM8NdvU144=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/josharian/intern v1.0.0 h1:vlS4z54oSdjm0bgjRigI+G1HpF+tI+9rE5LLzOg8HmY=
github.com/josharian/intern v1.0.0/go.mod h1:5DoeVV0s6jJacbCEi61lwdGj/aVlrQvzHFFd8Hwg//Y=
github.com/json-iterator/go v1.1.12 h1:PV8peI4a0ysnczrg+LtxykD8LfKY9ML6u2jnxaEnrnM=
github.com/json-iterator/go v1.1.12/go.mod h1:e30LSqwooZae/UwlEbR2852Gd8hjQvJoHmT4TnhNGBo=
github.com/kisielk/errcheck v1.5.0/go.mod h1:pFxgyoBC7bSaBwPgfKdkLd5X25qrDl4LWUI2bnpBCr8=
github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/mailru/easyjson v0.9.0 h1:PrnmzHw7262yW8sTBwxi1PdJA3Iw/EKBa8psRf7d9a4=
github.com/mailru/easyjson v0.9.0/go.mod h1:1+xMtQp2MRNVL/V1bOzuP3aP8VNwRW55fQUto+XFtTU=
github.com/mitchellh/go-homedir v1.1.0 h1:lukF9ziXFxDFPkA1vsr5zpc1XuPDn/wFntq5mG+4E0Y=
github.com/mitchellh/go-homedir v1.1.0/go.mod h1:SfyaCUpYCn1Vlf4IUYiD9fPX4A5wJrkLzIz1N1q0pr0=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd h1:TRLaZ9cD/w8PVh93nsPXa1VrQ6jlwL5oN8l14QlcNfg=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v1.0.2 h1:xBagoLtFs94CBntxluKeaWgTMpvLxC4ur3nMaC9Gz0M=
github.com/modern-go/reflect2 v1.0.2/go.mod h1:yWuevngMOJpCy52FWWMvUC8ws7m/LJsjYzDa0/r8luk=
github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq1c1nUAm88MOHcQC9l5mIlSMApZMrHA=
github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
github.com/onsi/ginkgo/v2 v2.21.0 h1:7rg/4f3rB88pb5obDgNZrNHrQ4e6WpjonchcpuBRnZM=
github.com/onsi/ginkgo/v2 v2.21.0/go.mod h1:7Du3c42kxCUegi0IImZ1wUQzMBVecgIHjR1C+NkhLQo=
github.com/onsi/gomega v1.35.1 h1:Cwbd75ZBPxFSuZ6T+rN/WCb/gOc6YgFBXLlZLhC7Ds4=
github.com/onsi/gomega v1.35.1/go.mod h1:PvZbdDc8J6XJEpDK4HCuRBm8a6Fzp9/DmhC9C7yFlog=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 h1:Jamvg5psRIccs7FGNTlIRMkT8wgtp5eCXdBlqhYGL6U=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.12.0 h1:exVL4IDcn6na9z1rAb56Vxr+CgyK3nn3O+epU5NdKM8=
github.com/rogpeppe/go-internal v1.12.0/go.mod h1:E+RYuTGaKKdloAfM02xzb0FW3Paa99yedzYV+kq4uf4=
github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ=
github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
github.com/x448/float16 v0.8.4 h1:qLwI1I70+NjRFUR3zs1JPUCgaCXSh3SW62uAKT1mSBM=
github.com/x448/float16 v0.8.4/go.mod h1:14CWIYCyZA/cWjXOioeEpHeN/83MdbZDRQHoFcYsOfg=
github.com/yuin/goldmark v1.1.27/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.2.1/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.36.0/go.mod h1:Y4J0ReaxCR1IMaabaSMugxJES1EpwhBHhv2bDHklZvc=
golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4/go.mod h1:jJ57K6gSWd91VN4djpZkiMVwK6gcyfeH4XE8wZrZaV4=
golang.org/x/mod v0.12.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.15.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/mod v0.17.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/net v0.37.0 h1:1zLorHbz+LYj7MQlSf1+2tPIIgibq2eL5xkrGk6f+2c=
golang.org/x/net v0.37.0/go.mod h1:ivrbrMbzFq5J41QOQh0siUuly180yBYtLp+CKbEaFx8=
golang.org/x/oauth2 v0.28.0 h1:CrgCKl8PPAVtLnU3c+EDw6x11699EWlsDeWNWKdIOkc=
golang.org/x/oauth2 v0.28.0/go.mod h1:onh5ek6nERTohokkhCD/y2cV4Do3fxFHFuAejCkRWT8=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220722155255-886fb9371eb4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.3.0/go.mod h1:FU7BRWz2tNW+3quACPkgCx/L+uEAv1htQ0V83Z9Rj+Y=
golang.org/x/sync v0.6.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.12.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sys v0.31.0 h1:ioabZlmFYtWhL+TRYpcnNlLwhyxaM9kWTDEmfnprqik=
golang.org/x/sys v0.31.0/go.mod h1:BJP2sWEmIv4KK5OTEluFJCKSidICx8ciO85XgH3Ak8k=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2/go.mod h1:TeRTkGYfJXctD9OcfyVLyj2J3IxLnKwHJR8f4D8a3YE=
golang.org/x/term v0.30.0 h1:PQ39fJZ+mfadBm0y5WlL4vlM7Sx1Hgf13sMIY2+QS9Y=
golang.org/x/term v0.30.0/go.mod h1:NYYFdzHoI5wRh/h5tDMdMqCqPJZEuNqVR5xJLd/n67g=
golang.org/x/text v0.23.0 h1:D71I7dUrlY+VX0gQShAThNGHFxZ13dGLBHQLVl1mJlY=
golang.org/x/text v0.23.0/go.mod h1:/BLNzu4aZCJ1+kcD0DNRotWKage4q2rGVAg4o22unh4=
golang.org/x/time v0.11.0 h1:/bpjEDfN9tkoN/ryeYHnv5hcMlc8ncjMcM4XBk5NWV0=
golang.org/x/time v0.11.0/go.mod h1:CDIdPxbZBQxdj6cxyCIdrNogrJKMJ7pr37NYpMcMDSg=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20200619180055-7c47624df98f/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20210106214847-113979e3529a/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.1.12/go.mod h1:hNGJHUnrk76NpqgfD5Aqm5Crs+Hm0VOH/i9J2+nxYbc=
golang.org/x/tools v0.13.0/go.mod h1:HvlwmtVNQAhOuCjW7xxvovg8wbNq7LwfXh/k7wXUl58=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d/go.mod h1:aiJjzUbINMkxbQROHiO6hDPo2LHcIPhhQsa9DLh0yGk=
golang.org/x/tools v0.26.0 h1:v/60pFQmzmT9ExmjDv2gGIfi3OqfKoEP6I5+umXlbnQ=
golang.org/x/tools v0.26.0/go.mod h1:TPVVj70c7JJ3WCazhD8OdXcZg/og+b9+tH/KxylGwH0=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/protobuf v1.36.5 h1:tPhr+woSbjfYvY6/GPufUoYizxw1cF/yFoxJ2fmpwlM=
google.golang.org/protobuf v1.36.5/go.mod h1:9fA7Ob0pmnwhb644+1+CVWFRbNajQ6iRojtC/QF5bRE=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/evanphx/json-patch.v4 v4.12.0 h1:n6jtcsulIzXPJaxegRbvFNNrZDjbij7ny3gmSPG+6V4=
gopkg.in/evanphx/json-patch.v4 v4.12.0/go.mod h1:p8EYWUEYMpynmqDbY58zCKCFZw8pRWMG4EsWvDvM72M=
gopkg.in/inf.v0 v0.9.1 h1:73M5CoZyi3ZLMOyDlQh031Cx6N9NDJ2Vvfl76EDAgDc=
gopkg.in/inf.v0 v0.9.1/go.mod h1:cWUDdTG/fYaXco+Dcufb5Vnc6Gp2YChqWtbxRZE0mXw=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gotest.tools v2.2.0+incompatible h1:VsBPFP1AI068pPrMxtb/S8Zkgf9xEmTLJjfM+P5UIEo=
gotest.tools v2.2.0+incompatible/go.mod h1:DsYFclhRJ6vuDpmuTbkuFWG+y2sxOXAzmJt81HFBacw=
k8s.io/api v0.32.2 h1:bZrMLEkgizC24G9eViHGOPbW+aRo9duEISRIJKfdJuw=
k8s.io/api v0.32.2/go.mod h1:hKlhk4x1sJyYnHENsrdCWw31FEmCijNGPJO5WzHiJ6Y=
k8s.io/apimachinery v0.32.2 h1:yoQBR9ZGkA6Rgmhbp/yuT9/g+4lxtsGYwW6dR6BDPLQ=
k8s.io/apimachinery v0.32.2/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
k8s.io/apiserver v0.32.2 h1:WzyxAu4mvLkQxwD9hGa4ZfExo3yZZaYzoYvvVDlM6vw=
k8s.io/apiserver v0.32.2/go.mod h1:PEwREHiHNU2oFdte7BjzA1ZyjWjuckORLIK/wLV5goM=
k8s.io/client-go v0.32.2 h1:4dYCD4Nz+9RApM2b/3BtVvBHw54QjMFUl1OLcJG5yOA=
k8s.io/client-go v0.32.2/go.mod h1:fpZ4oJXclZ3r2nDOv+Ux3XcJutfrwjKTCHz2H3sww94=
k8s.io/klog/v2 v2.130.1 h1:n9Xl7H1Xvksem4KFG4PYbdQCQxqc/tTUyrgXaOhHSzk=
k8s.io/klog/v2 v2.130.1/go.mod h1:3Jpz1GvMt720eyJH1ckRHK1EDfpxISzJ7I9OYgaDtPE=
k8s.io/kube-openapi v0.0.0-20250304201544-e5f78fe3ede9 h1:t0huyHnz6HsokckRxAF1bY0cqPFwzINKCL7yltEjZQc=
k8s.io/kube-openapi v0.0.0-20250304201544-e5f78fe3ede9/go.mod h1:5jIi+8yX4RIb8wk3XwBo5Pq2ccx4FP10ohkbSKCZoK8=
k8s.io/utils v0.0.0-20241210054802-24370beab758 h1:sdbE21q2nlQtFh65saZY+rRM6x6aJJI8IUa1AmH/qa0=
k8s.io/utils v0.0.0-20241210054802-24370beab758/go.mod h1:OLgZIPagt7ERELqWJFomSt595RzquPNLL48iOWgYOg0=
sigs.k8s.io/json v0.0.0-20241014173422-cfa47c3a1cc8 h1:gBQPwqORJ8d8/YNZWEjoZs7npUVDpVXUUOFfW6CgAqE=
sigs.k8s.io/json v0.0.0-20241014173422-cfa47c3a1cc8/go.mod h1:mdzfpAEoE6DHQEN0uh9ZbOCuHbLK5wOm7dK4ctXE9Tg=
sigs.k8s.io/randfill v0.0.0-20250304075658-069ef1bbf016/go.mod h1:XeLlZ/jmk4i1HRopwe7/aU3H5n1zNUcX6TM94b3QxOY=
sigs.k8s.io/randfill v1.0.0 h1:JfjMILfT8A6RbawdsK2JXGBR5AQVfd+9TbzrlneTyrU=
sigs.k8s.io/randfill v1.0.0/go.mod h1:XeLlZ/jmk4i1HRopwe7/aU3H5n1zNUcX6TM94b3QxOY=
sigs.k8s.io/structured-merge-diff/v4 v4.6.0 h1:IUA9nvMmnKWcj5jl84xn+T5MnlZKThmUW1TdblaLVAc=
sigs.k8s.io/structured-merge-diff/v4 v4.6.0/go.mod h1:dDy58f92j70zLsuZVuUX5Wp9vtxXpaZnkPGWeqDfCps=
sigs.k8s.io/yaml v1.4.0 h1:Mk1wCc2gy/F0THH0TAp1QYyJNzRm2KCLy3o5ASXVI5E=
sigs.k8s.io/yaml v1.4.0/go.mod h1:Ejl7/uTz7PSA4eKMyQCUTnhZYNmLIl+5c2lQPGR2BPY=
```

## File: `admission-webhook/kube_client.go`
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"

	authorizationv1 "k8s.io/api/authorization/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime/schema"
	"k8s.io/apiserver/pkg/authentication/serviceaccount"
	"k8s.io/client-go/dynamic"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
)

const (
	// these 3 constants are the coordinates of the Custom Resource Definition
	crdAPIGroup     = "windows.k8s.io"
	crdAPIVersion   = "v1"
	crdResourceName = "gmsacredentialspecs"

	// crdContentsField is the single field that's expected to be defined in a GMSA CRD,
	// and to contain the contents of the cred spec itself
	crdContentsField = "credspec"

	// notFound is used in `isNotFoundError` below
	notFound = "not found"
)

// kubeClient centralizes all the operations we need when talking to k8s
type kubeClient struct {
	coreClient    kubernetes.Interface
	dynamicClient dynamic.Interface
}

func newKubeClient(config *rest.Config) (*kubeClient, error) {
	coreClient, err := kubernetes.NewForConfig(config)
	if err != nil {
		return nil, err
	}

	dynamicClient, err := dynamic.NewForConfig(config)
	if err != nil {
		return nil, err
	}

	return &kubeClient{
		coreClient:    coreClient,
		dynamicClient: dynamicClient,
	}, nil
}

// isAuthorizedToReadConfigMap checks whether a given service account is authorized to `use` a given cred spec.
// If it denies the request, it also returns a string explaining why.
func (kc *kubeClient) isAuthorizedToUseCredSpec(ctx context.Context, serviceAccountName, namespace, credSpecName string) (bool, string) {
	serviceAccountUserInfo := serviceaccount.UserInfo(namespace, serviceAccountName, "")

	// needed to cast `authorizationv1.ExtraValue` to `[]string`
	var extra map[string]authorizationv1.ExtraValue
	for k, v := range serviceAccountUserInfo.GetExtra() {
		extra[k] = v
	}

	subjectAccessReview := authorizationv1.LocalSubjectAccessReview{
		ObjectMeta: metav1.ObjectMeta{
			Namespace: namespace,
		},
		Spec: authorizationv1.SubjectAccessReviewSpec{
			ResourceAttributes: &authorizationv1.ResourceAttributes{
				Namespace: namespace,
				Verb:      "use",
				Group:     crdAPIGroup,
				Version:   crdAPIVersion,
				Resource:  crdResourceName,
				Name:      credSpecName,
			},
			User:   serviceAccountUserInfo.GetName(),
			Groups: serviceAccountUserInfo.GetGroups(),
			UID:    serviceAccountUserInfo.GetUID(),
			Extra:  extra,
		},
	}

	response, err := kc.coreClient.AuthorizationV1().LocalSubjectAccessReviews(namespace).Create(ctx, &subjectAccessReview, metav1.CreateOptions{})
	if err != nil {
		return false, fmt.Sprintf("error when checking authz access: %v", err.Error())
	}
	return response.Status.Allowed && !response.Status.Denied, response.Status.Reason
}

// retrieveCredSpecContents fetches the actual contents of a cred spec.
// If it returns an error, it also returns the corresponding HTTP code.
func (kc *kubeClient) retrieveCredSpecContents(ctx context.Context, credSpecName string) (string, int, error) {
	resource := schema.GroupVersionResource{
		Group:    crdAPIGroup,
		Version:  crdAPIVersion,
		Resource: crdResourceName,
	}
	credSpec, err := kc.dynamicClient.Resource(resource).Get(ctx, credSpecName, metav1.GetOptions{})
	if err != nil {
		if isNotFoundError(err) {
			return "", http.StatusNotFound, fmt.Errorf("cred spec %s does not exist", credSpecName)
		}
		return "", http.StatusInternalServerError, fmt.Errorf("unable to retrieve the contents of cred spec %s: %v", credSpecName, err)
	}

	if contents, present := credSpec.Object[crdContentsField]; !present || contents == "" {
		return "", http.StatusExpectationFailed, fmt.Errorf("cred spec %s does not have a %s key", credSpecName, crdContentsField)
	}

	contentsBytes, err := json.Marshal(credSpec.Object[crdContentsField])
	if err != nil {
		return "", http.StatusInternalServerError, fmt.Errorf("unable to marshall cred spec %s into a JSON: %v", credSpecName, err)
	}

	return string(contentsBytes), http.StatusOK, nil
}

// isNotFoundError returns true if the error indicates "not found".  It parses
// the error string looking for known values, which is imperfect but works in
// practice; and there's not much better we can do right now with k8s' dynamic client API
func isNotFoundError(err error) bool {
	msg := err.Error()
	return msg[len(msg)-len(notFound):] == notFound
}
```

## File: `admission-webhook/main.go`
```go
package main

import (
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/sirupsen/logrus"
	"k8s.io/client-go/rest"
)

func main() {
	initLogrus()

	enableCertReload := flag.Bool("cert-reload", false, "enable certificate reload")
	v := flag.Bool("version", false, "show version")
	flag.Parse()

	if *v {
		fmt.Printf("windows-gmsa-webhook v%s\n", getVersion())
		os.Exit(0)
	}

	kubeClient, err := createKubeClient()
	if err != nil {
		panic(err)
	}

	randomHostname := env_bool("RANDOM_HOSTNAME")

	options := []WebhookOption{WithCertReload(*enableCertReload)}
	options = append(options, WithRandomHostname(randomHostname))

	webhook := newWebhookWithOptions(kubeClient, options...)

	tlsConfig := &tlsConfig{
		crtPath: env("TLS_CRT"),
		keyPath: env("TLS_KEY"),
	}

	port := env_int("HTTPS_PORT", 443)

	if err = webhook.start(port, tlsConfig, nil); err != nil {
		panic(err)
	}
}

var logLevels = map[string]logrus.Level{
	"panic": logrus.PanicLevel,
	"fatal": logrus.FatalLevel,
	"error": logrus.ErrorLevel,
	"warn":  logrus.WarnLevel,
	"info":  logrus.InfoLevel,
	"debug": logrus.DebugLevel,
	"trace": logrus.TraceLevel,
}

func initLogrus() {
	logrus.SetOutput(os.Stdout)

	logLevel := logrus.DebugLevel
	invalid := false

	rawLogLevel, present := os.LookupEnv("LOG_LEVEL")
	if present {
		if level, valid := logLevels[strings.ToLower(rawLogLevel)]; valid {
			logLevel = level
		} else {
			invalid = true
		}
	}

	logrus.SetLevel(logLevel)

	if invalid {
		keys := make([]string, len(logLevels))
		i := 0
		for key := range logLevels {
			keys[i] = key
			i++
		}
		logrus.Warningf("Unknown log level %s, valid log levels are: %v", rawLogLevel, strings.Join(keys, ", "))
	}
}

func createKubeClient() (*kubeClient, error) {
	config, err := rest.InClusterConfig()
	if err != nil {
		return nil, err
	}

	config.QPS = env_float("QPS", rest.DefaultQPS)
	config.Burst = env_int("BURST", rest.DefaultBurst)
	logrus.Infof("QPS: %f, Burst: %d", config.QPS, config.Burst)

	return newKubeClient(config)
}

func env_float(key string, defaultFloat float32) float32 {
	if v, found := os.LookupEnv(key); found {
		if i, err := strconv.ParseFloat(v, 32); err == nil {
			return float32(i)
		}
		logrus.Warningf("unable to parse environment variable %s with value %s; using default value %f", key, v, defaultFloat)
	}

	return defaultFloat
}

func env_bool(key string) bool {
	if v, found := os.LookupEnv(key); found {
		// Convert string to bool
		if boolValue, err := strconv.ParseBool(v); err == nil {
			return boolValue
		}
		// throw error if unable to parse
		panic(fmt.Errorf("unable to parse environment variable %s with value %s to bool", key, v))
	}

	// return bool default value: false
	return false
}

func env_int(key string, defaultInt int) int {
	if v, found := os.LookupEnv(key); found {
		if i, err := strconv.Atoi(v); err == nil {
			return i
		}
		logrus.Warningf("unable to parse environment variable %s with value %s; using default value %d", key, v, defaultInt)
	}

	return defaultInt
}

func env(key string) string {
	if value, found := os.LookupEnv(key); found {
		return value
	}
	panic(fmt.Errorf("%s env var not found", key))
}
```

## File: `admission-webhook/main_test.go`
```go
package main

import (
	"fmt"
	"os"
	"testing"
)

func Test_env_float(t *testing.T) {
	defaultFloat := float32(5.0)
	tests := []struct {
		name   string
		envkey string
		envval string
		want   float32
	}{
		{
			name:   "Environment variable set to valid float",
			envkey: "TEST_ENV_FLOAT",
			envval: "3.14",
			want:   3.14,
		},
		{
			name:   "Environment variable set to invalid float",
			envkey: "TEST_ENV_FLOAT",
			envval: "invalid",
			want:   float32(defaultFloat),
		},
		{
			name:   "Environment variable not set",
			envkey: "TEST_ENV_FLOAT",
			envval: "",
			want:   float32(defaultFloat),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if tt.envval != "" {
				os.Setenv(tt.envkey, tt.envval)
			} else {
				os.Unsetenv(tt.envkey)
			}
			if got := env_float(tt.envkey, defaultFloat); got != tt.want {
				t.Errorf("env_float() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_env_int(t *testing.T) {
	defaultInt := 5
	tests := []struct {
		name   string
		envkey string
		envval string
		want   int
	}{
		{
			name:   "Environment variable set to valid int",
			envkey: "TEST_ENV_INT",
			envval: "10",
			want:   10,
		},
		{
			name:   "Environment variable set to invalid int",
			envkey: "TEST_ENV_INT",
			envval: "invalid",
			want:   defaultInt,
		},
		{
			name:   "Environment variable not set",
			envkey: "TEST_ENV_INT",
			envval: "",
			want:   defaultInt,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if tt.envval != "" {
				os.Setenv(tt.envkey, tt.envval)
			} else {
				os.Unsetenv(tt.envkey)
			}
			if got := env_int(tt.envkey, defaultInt); got != tt.want {
				t.Errorf("env_int() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_env_bool(t *testing.T) {
	tests := []struct {
		name   string
		envkey string
		envval string
		want   bool
	}{
		{
			name:   "Environment variable set to true",
			envkey: "TEST_ENV_BOOL",
			envval: "true",
			want:   true,
		},
		{
			name:   "Environment variable set to false",
			envkey: "TEST_ENV_BOOL",
			envval: "false",
			want:   false,
		},
		{
			name:   "Environment variable not set",
			envkey: "TEST_ENV_BOOL",
			envval: "",
			want:   false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if tt.envval != "" {
				os.Setenv(tt.envkey, tt.envval)
			} else {
				os.Unsetenv(tt.envkey)
			}
			if got := env_bool(tt.envkey); got != tt.want {
				t.Errorf("env_bool() = %v, want %v", got, tt.want)
			}
		})
	}

	envkey := "TEST_ENV_BOOL"
	envVal := "invalid"
	// Test panic
	defer func() {
		if r := recover(); r == nil {
			t.Errorf("The code did not panic")
		} else {
			t.Logf("Recovered from panic: %v", r)
			if r.(error).Error() != fmt.Sprintf("unable to parse environment variable %s with value %s to bool", envkey, envVal) {
				t.Errorf("Unexpected panic message: %v", r)
			}
		}
	}()

	os.Setenv(envkey, envVal)
	env_bool("TEST_ENV_BOOL")
}

func TestMain(m *testing.M) {
	GenerateTestCertAndKey()
	code := m.Run() // run tests
	ClearTestdata()
	os.Exit(code)
}
```

## File: `admission-webhook/run-ci.sh`
```bash
#!/usr/bin/env bash

## Runs the right Travis tests depending on the environment variables.
## Must stay in syncs with the build matrix from .travis.yml

set -e

# giving a unique name allows running locally with https://github.com/nektos/act
export CLUSTER_NAME="windows-gmsa-$GITHUB_JOB"
export KUBECTL="$GITHUB_WORKSPACE/admission-webhook/dev/kubectl-$CLUSTER_NAME"
export KUBECONFIG="$GITHUB_WORKSPACE/admission-webhook/dev/kubeconfig-$CLUSTER_NAME"

export K8S_GMSA_CHART="$GITHUB_WORKSPACE/charts/gmsa"

main() {
    case "$T" in
        unit)
            make unit_tests ;;
        integration)
            run_integration_tests ;;
        dry_run_deploy)
            run_dry_run_deploy ;;
        *)
            echo "Unknown test option: $T" && exit 1 ;;
    esac
}

run_integration_tests() {
    if [ "$WITHOUT_ENVSUBST" ] && [ -x "$(command -v envsubst)" ] && [[ "$GITHUB_ACTIONS" == "true" ]]; then
        echo "Removing envsubst"
        sudo rm -f "$(command -v envsubst)"
    fi

    export DEPLOYMENT_NAME=windows-gmsa-dev
    export NAMESPACE=windows-gmsa-dev

    if [[ "$DEPLOY_METHOD" == 'download' ]]; then
        export K8S_GMSA_DEPLOY_METHOD='download'

        if [ "$GITHUB_HEAD_REF" ]; then
            # GITHUB_HEAD_REF is only set if it's a pull request
            export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="$GITHUB_REPOSITORY"
            export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$GITHUB_SHA"
            echo "Running pull request: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
        else
            # not a pull request
            export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="kubernetes-sigs/windows-gmsa"
            export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$(git rev-parse HEAD)"
            echo "Running: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
        fi
    elif [[ "$DEPLOY_METHOD" == 'chart' ]]; then
       export K8S_GMSA_DEPLOY_METHOD='chart'
       echo "deploy method: $K8S_GMSA_DEPLOY_METHOD"
       if [ "$GITHUB_HEAD_REF" ]; then
           # GITHUB_HEAD_REF is only set if it's a pull request
           # Similar logic goes here, but installs the chart using the repo.
           export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="$GITHUB_REPOSITORY"
           export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$GITHUB_SHA"
           echo "Running pull request: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
       else
           # not a pull request
           # Installs the chart using the local copy.
           export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="kubernetes-sigs/windows-gmsa"
           export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$(git rev-parse HEAD)"
           echo "Running: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
       fi
    fi

    
    if [ "$WITH_DEV_IMAGE" ]; then
        make integration_tests_with_dev_image

        # for good measure let's check that one can change and restart the webhook when using the dev image
        local BOGUS_VERSION='cannotbeavalidversion'

        local POD_NAME
        POD_NAME="$($KUBECTL -n "$NAMESPACE" get pod --selector=app=$DEPLOYMENT_NAME -o=jsonpath='{.items[0].metadata.name}')"
        $KUBECTL -n "$NAMESPACE" exec "$POD_NAME" -- go build -ldflags="-X main.version=$BOGUS_VERSION"
        $KUBECTL -n "$NAMESPACE" exec "$POD_NAME" -- service webhook restart

        local SERVICE_IP
        SERVICE_IP="$($KUBECTL -n $NAMESPACE get service $DEPLOYMENT_NAME -o=jsonpath='{.spec.clusterIP}')"

        local INFO_OUTPUT
        INFO_OUTPUT="$(docker exec "$CLUSTER_NAME-control-plane" curl -sk https://$SERVICE_IP/info)"

        if [[ "$INFO_OUTPUT" == *"$BOGUS_VERSION"* ]]; then
            echo -e "Output from /info does contain '$BOGUS_VERSION':\n$INFO_OUTPUT"
        else
            echo -e "Expected output from /info to contain '$BOGUS_VERSION', instead got:\n$INFO_OUTPUT"
            exit 1
        fi
    else
        if [[ "$DEPLOY_METHOD" == 'chart' ]]; then
            make integration_tests_chart
        else 
            make integration_tests
        fi
    fi
}

# performs a dry-run deploy and ensures no changes have been made to the cluster
run_dry_run_deploy() {
    make cluster_start

    wait_for_all_terminating_or_pending_k8s_resources || return $?

    local SNAPSHOT_DIR='k8s_snapshot'
    k8s_snapshot $SNAPSHOT_DIR/before

    KUBECTL=$KUBECTL ./deploy/deploy-gmsa-webhook.sh --file gmsa-webhook.yml --dry-run

    k8s_snapshot $SNAPSHOT_DIR/after

    diff $SNAPSHOT_DIR/{before,after}
}

# lists all API objects present on a k8s master node and saves them to the folder given as 1st argument
# that dir shouldn't exist prior to calling the function
k8s_snapshot() {
    local DIR="$1"
    [ "$DIR" ] && [ ! -d "$DIR" ] || return 1
    mkdir -p "$DIR"

    local RESOURCE OUTPUT
    for RESOURCE in $($KUBECTL api-resources -o name); do
        OUTPUT="$(list_k8s_resources "$RESOURCE")" || return $?
        echo "$OUTPUT" | sort > "$DIR/$RESOURCE"
    done
}

# lists all API objects of the given resource, with an optional JSON-path filter
list_k8s_resources() {
    local RESOURCE="$1"

    local FILTER
    if [ "$2" ]; then
        FILTER="?(@.$2)"
    else
        FILTER='*'
    fi

    local OUTPUT EXIT_STATUS=0

    # this output is guaranteed to be unique since namespaces can't contain spaces
    OUTPUT="$($KUBECTL get "$RESOURCE" --all-namespaces -o jsonpath="{range .items[$FILTER]}{@.metadata.namespace}{\" \"}{@.metadata.name}{\"\n\"}{end}" 2>&1)" \
        || EXIT_STATUS=$?

    if [[ "$OUTPUT" == *'deprecated'* ]]; then
        # component status is deprecated in 1.19 and fails https://github.com/kubernetes-sigs/kind/issues/1998
        return 0
    elif [[ $EXIT_STATUS == 0 ]]; then
        echo "$OUTPUT"
        return 0
    elif [[ "$OUTPUT" == *'(NotFound)'* ]] || [[ "$OUTPUT" == *'(MethodNotAllowed)'* ]]; then
        return 0
    else
        echo "Error when listing k8s resource $RESOURCE: $OUTPUT" 1>&2
        return $EXIT_STATUS
    fi
}

# waits for all API objects in "Terminating" or "Pending" state to go away,
# for up to 120 secs per resource type
wait_for_all_terminating_or_pending_k8s_resources() {
    local RESOURCE
    for RESOURCE in $($KUBECTL api-resources -o name); do
        wait_until_no_k8s_resources_in_state "$RESOURCE" 'Terminating' || return $?
        wait_until_no_k8s_resources_in_state "$RESOURCE" 'Pending' || return $?
    done
}

# waits up to 60 seconds for API objects of the given resource that are
# in the given state to go away, else errors out
wait_until_no_k8s_resources_in_state() {
    local RESOURCE="$1"
    local STATE="$2"

    local START="$(date -u +%s)" OUTPUT

    while [ "$(( $(date -u +%s) - $START ))" -le 60 ]; do
        OUTPUT="$(list_k8s_resources "$RESOURCE" 'status.phase=="'$STATE'"')" || return $?
        if [ "$OUTPUT" ]; then
            # there still are resources in the given state
            echo "still waiting on $RESOURCE $OUTPUT"
            sleep 1
            continue
        fi
        return 0
    done

    echo -e "Timed out waiting for all $STATE $RESOURCE to go away:\n$OUTPUT"
    return 1
}

main "$@"
```

## File: `admission-webhook/types.go`
```go
package main

import "context"

type tlsConfig struct {
	crtPath string
	keyPath string
}

type kubeClientInterface interface {
	isAuthorizedToUseCredSpec(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string)
	retrieveCredSpecContents(ctx context.Context, credSpecName string) (contents string, httpCode int, err error)
}
```

## File: `admission-webhook/utils_test.go`
```go
package main

import (
	"context"
	crand "crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"crypto/x509/pkix"
	"encoding/pem"
	"math/big"
	"math/rand"
	"os"
	"time"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

const dummyCredSpecName = "dummy-cred-spec-name"

const dummyCredSpecContents = `{"We don't need no": ["education", "thought control", "dark sarcasm in the classroom"], "All in all you're just another": {"brick": "in", "the": "wall"}}`
const dummyServiceAccoutName = "dummy-service-account-name"
const dummyNamespace = "dummy-namespace"
const dummyPodName = "dummy-pod-name"
const dummyContainerName = "dummy-container-name"

type dummyKubeClient struct {
	isAuthorizedToUseCredSpecFunc func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string)
	retrieveCredSpecContentsFunc  func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error)
}

func (dkc *dummyKubeClient) isAuthorizedToUseCredSpec(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
	if dkc.isAuthorizedToUseCredSpecFunc != nil {
		return dkc.isAuthorizedToUseCredSpecFunc(ctx, serviceAccountName, namespace, credSpecName)
	}
	authorized = true
	return
}

func (dkc *dummyKubeClient) retrieveCredSpecContents(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
	if dkc.retrieveCredSpecContentsFunc != nil {
		return dkc.retrieveCredSpecContentsFunc(ctx, credSpecName)
	}
	contents = dummyCredSpecContents
	return
}

func buildWindowsOptions(credSpecName, credSpecContents string) *corev1.WindowsSecurityContextOptions {
	winOptions := &corev1.WindowsSecurityContextOptions{}
	setWindowsOptions(winOptions, credSpecName, credSpecContents)
	return winOptions
}

func setWindowsOptions(winOptions *corev1.WindowsSecurityContextOptions, credSpecName, credSpecContents string) {
	if credSpecName != "" {
		winOptions.GMSACredentialSpecName = &credSpecName
	}
	if credSpecContents != "" {
		winOptions.GMSACredentialSpec = &credSpecContents
	}
}

// buildPod builds a pod for unit tests.
// `podWindowsOptions` should be either a full `*corev1.WindowsSecurityContextOptions` or a string, in which
// case a `*corev1.WindowsSecurityContextOptions` is built using that string as the name of the cred spec to use.
// Same goes for the values of `containerNamesAndWindowsOptions`.
func buildPod(serviceAccountName string, podWindowsOptions *corev1.WindowsSecurityContextOptions, containerNamesAndWindowsOptions map[string]*corev1.WindowsSecurityContextOptions) *corev1.Pod {
	return buildPodWithHostName(serviceAccountName, nil, podWindowsOptions, containerNamesAndWindowsOptions)
}

// buildPod builds a pod for unit tests.
// `podWindowsOptions` should be either a full `*corev1.WindowsSecurityContextOptions` or a string, in which
// case a `*corev1.WindowsSecurityContextOptions` is built using that string as the name of the cred spec to use.
// Same goes for the values of `containerNamesAndWindowsOptions`.
func buildPodWithHostName(serviceAccountName string, hostname *string, podWindowsOptions *corev1.WindowsSecurityContextOptions, containerNamesAndWindowsOptions map[string]*corev1.WindowsSecurityContextOptions) *corev1.Pod {
	containers := make([]corev1.Container, len(containerNamesAndWindowsOptions))
	i := 0
	for name, winOptions := range containerNamesAndWindowsOptions {
		containers[i] = corev1.Container{Name: name}
		if winOptions != nil {
			containers[i].SecurityContext = &corev1.SecurityContext{WindowsOptions: winOptions}
		}
		i++
	}

	shuffleContainers(containers)

	podSpec := corev1.PodSpec{
		ServiceAccountName: serviceAccountName,
		Containers:         containers,
	}

	if hostname != nil {
		podSpec.Hostname = *hostname
	}

	if podWindowsOptions != nil {
		podSpec.SecurityContext = &corev1.PodSecurityContext{WindowsOptions: podWindowsOptions}
	}

	return &corev1.Pod{
		ObjectMeta: metav1.ObjectMeta{Name: dummyPodName},
		Spec:       podSpec,
	}
}

func shuffleContainers(a []corev1.Container) {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	for i := len(a) - 1; i > 0; i-- {
		j := r.Int() % (i + 1)
		tmp := a[j]
		a[j] = a[i]
		a[i] = tmp
	}
}

func GenerateTestCertAndKey() {
	// Generate a 2048-bit RSA private key
	priv, err := rsa.GenerateKey(crand.Reader, 2048)
	if err != nil {
		panic(err)
	}

	// Create a certificate template
	certTemplate := &x509.Certificate{
		SerialNumber: big.NewInt(1),
		Subject: pkix.Name{
			Organization: []string{"test"},
		},
		NotBefore:             time.Now(),
		NotAfter:              time.Now().AddDate(1, 0, 0), // Valid for 1 year
		KeyUsage:              x509.KeyUsageKeyEncipherment | x509.KeyUsageDigitalSignature,
		ExtKeyUsage:           []x509.ExtKeyUsage{x509.ExtKeyUsageServerAuth},
		BasicConstraintsValid: true,
	}

	// Create the certificate
	certDER, err := x509.CreateCertificate(crand.Reader, certTemplate, certTemplate, &priv.PublicKey, priv)
	if err != nil {
		panic(err)
	}

	err = os.Mkdir("testdata", 0755)
	if err != nil {
		panic(err)
	}

	// Write the certificate to a PEM file
	certFile, err := os.Create("testdata/cert.pem")
	if err != nil {
		panic(err)
	}
	pem.Encode(certFile, &pem.Block{Type: "CERTIFICATE", Bytes: certDER})
	certFile.Close()

	// Write the private key to a PEM file
	keyFile, err := os.Create("testdata/key.pem")
	if err != nil {
		panic(err)
	}
	keyBytes := x509.MarshalPKCS1PrivateKey(priv)
	pem.Encode(keyFile, &pem.Block{Type: "RSA PRIVATE KEY", Bytes: keyBytes})
	keyFile.Close()
}

func ClearTestdata() {
	os.RemoveAll("testdata")
}
```

## File: `admission-webhook/version.go`
```go
package main

var version string

func getVersion() string {
	if version == "" {
		return "unknown"
	}

	return version
}
```

## File: `admission-webhook/webhook.go`
```go
package main

import (
	"context"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"reflect"
	"strconv"
	"strings"
	"time"

	"github.com/google/uuid"

	"github.com/sirupsen/logrus"
	admissionV1 "k8s.io/api/admission/v1"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime"
)

type webhookOperation string

type gmsaResourceKind string

const (
	contentTypeHeader = "Content-Type"
	jsonContentType   = "application/json"

	validate webhookOperation = "VALIDATE"
	mutate   webhookOperation = "MUTATE"

	podKind       gmsaResourceKind = "pod"
	containerKind gmsaResourceKind = "container"
)

type webhook struct {
	server *http.Server
	client kubeClientInterface
	config *WebhookConfig
}

type podAdmissionError struct {
	error
	code int
	pod  *corev1.Pod
}

type WebhookConfig struct {
	EnableCertReload     bool
	EnableRandomHostName bool
}

type WebhookOption func(*WebhookConfig)

func WithCertReload(enabled bool) WebhookOption {
	return func(cfg *WebhookConfig) {
		cfg.EnableCertReload = enabled
	}
}

func WithRandomHostname(enabled bool) WebhookOption {
	return func(cfg *WebhookConfig) {
		cfg.EnableRandomHostName = enabled
	}
}

func newWebhook(client kubeClientInterface) *webhook {
	return newWebhookWithOptions(client)
}

func newWebhookWithOptions(client kubeClientInterface, options ...WebhookOption) *webhook {
	config := &WebhookConfig{EnableCertReload: false, EnableRandomHostName: false}

	for _, option := range options {
		option(config)
	}

	return &webhook{
		client: client,
		config: config,
	}
}

// start is a blocking call.
// If passed a listeningChan, it will close it when it's started listening
func (webhook *webhook) start(port int, tlsConfig *tlsConfig, listeningChan chan interface{}) error {
	if webhook.server != nil {
		return fmt.Errorf("webhook already started")
	}

	webhook.server = &http.Server{
		Addr:    ":" + strconv.Itoa(port),
		Handler: webhook,
	}

	logrus.Infof("starting webhook server at port %v", port)
	listener, err := net.Listen("tcp", webhook.server.Addr)
	if err != nil {
		return err
	}
	defer listener.Close()
	keepAliveListener := tcpKeepAliveListener{listener.(*net.TCPListener)}

	if listeningChan != nil {
		close(listeningChan)
	}

	if tlsConfig == nil {
		err = webhook.server.Serve(keepAliveListener)
	} else {
		if webhook.config.EnableCertReload {
			logrus.Infof("Webhook certificate reload enabled")
			certReloader := NewCertReloader(tlsConfig.crtPath, tlsConfig.keyPath)
			_, err = certReloader.LoadCertificate()
			if err != nil {
				return err
			}

			go watchCertFiles(context.Background(), certReloader)

			webhook.server.TLSConfig = &tls.Config{
				GetCertificate: certReloader.GetCertificateFunc(),
			}

			err = webhook.server.ServeTLS(keepAliveListener, "", "")
		} else {
			err = webhook.server.ServeTLS(keepAliveListener, tlsConfig.crtPath, tlsConfig.keyPath)
		}
	}

	if err != nil {
		if err == http.ErrServerClosed {
			logrus.Infof("server closed")
		} else {
			return err
		}
	}

	return nil
}

// stop stops the HTTP server.
func (webhook *webhook) stop() error {
	if webhook.server == nil {
		return fmt.Errorf("webhook server not started yet")
	}
	return webhook.server.Shutdown(context.Background())
}

// ServeHTTP makes this object a http.Handler; its job is handling the HTTP routing: paths,
// methods and content-type headers.
// Since we only have a handful of endpoints, there's no need for a full-fledged router here.
func (webhook *webhook) ServeHTTP(responseWriter http.ResponseWriter, request *http.Request) {
	var operation webhookOperation

	switch request.URL.Path {
	case "/validate":
		operation = validate
	case "/mutate":
		operation = mutate
	case "/info":
		writeJSONBody(responseWriter, map[string]string{"version": getVersion()})
		return
	case "/health":
		responseWriter.WriteHeader(http.StatusNoContent)
		return
	default:
		abortHTTPRequest(responseWriter, http.StatusNotFound, "received %s request for unknown path %s", request.Method, request.URL.Path)
		return
	}

	// should be a POST request
	if strings.ToUpper(request.Method) != "POST" {
		abortHTTPRequest(responseWriter, http.StatusMethodNotAllowed, "expected POST HTTP request, got a %s %s request", request.Method, operation)
		return
	}
	// verify the content type is JSON
	if contentType := request.Header.Get(contentTypeHeader); contentType != jsonContentType {
		abortHTTPRequest(responseWriter, http.StatusUnsupportedMediaType, "expected JSON content-type header for %s request, got %q", operation, contentType)
		return
	}

	admissionResponse := webhook.httpRequestToAdmissionResponse(request, operation)
	responseAdmissionReview := admissionV1.AdmissionReview{
		TypeMeta: metav1.TypeMeta{
			Kind:       "AdmissionReview",
			APIVersion: "admission.k8s.io/v1",
		},
		Response: admissionResponse,
	}

	writeJSONBody(responseWriter, responseAdmissionReview)
}

// abortHTTPRequest is called for low-level HTTP errors (routing or writing the body)
func abortHTTPRequest(responseWriter http.ResponseWriter, httpCode int, logMsg string, logArs ...interface{}) {
	logrus.Infof(logMsg, logArs...)
	responseWriter.WriteHeader(httpCode)
}

// writeJsonBody writes a JSON object to an HTTP response.
func writeJSONBody(responseWriter http.ResponseWriter, jsonBody interface{}) {
	if responseBytes, err := json.Marshal(jsonBody); err == nil {
		logrus.Debugf("sending response: %s", responseBytes)

		responseWriter.Header().Set(contentTypeHeader, jsonContentType)
		if _, err = responseWriter.Write(responseBytes); err != nil {
			abortHTTPRequest(responseWriter, http.StatusInternalServerError, "error when writing response JSON %s: %v", responseBytes, err)
		}
	} else {
		abortHTTPRequest(responseWriter, http.StatusInternalServerError, "error when marshalling response %v: %v", jsonBody, err)
	}
}

// httpRequestToAdmissionResponse turns a raw HTTP request into an AdmissionResponse struct.
func (webhook *webhook) httpRequestToAdmissionResponse(request *http.Request, operation webhookOperation) *admissionV1.AdmissionResponse {
	// read the body
	if request.Body == nil {
		deniedAdmissionResponse(fmt.Errorf("no request body"), http.StatusBadRequest)
	}
	body, err := ioutil.ReadAll(request.Body)
	if err != nil {
		return deniedAdmissionResponse(fmt.Errorf("couldn't read request body: %v", err), http.StatusBadRequest)
	}
	defer request.Body.Close()

	logrus.Debugf("handling %s request: %s", operation, body)

	// unmarshall the request
	admissionReview := admissionV1.AdmissionReview{}
	if err = json.Unmarshal(body, &admissionReview); err != nil {
		return deniedAdmissionResponse(fmt.Errorf("unable to unmarshall JSON body as an admission review: %v", err), http.StatusBadRequest)
	}
	if admissionReview.Request == nil {
		return deniedAdmissionResponse(fmt.Errorf("no 'Request' field in JSON body"), http.StatusBadRequest)
	}

	admissionResponse, admissionError := webhook.validateOrMutate(request.Context(), admissionReview.Request, operation)
	if admissionError != nil {
		admissionResponse = deniedAdmissionResponse(admissionError)
	}

	// return the same UID
	admissionResponse.UID = admissionReview.Request.UID

	return admissionResponse
}

// validateOrMutate is where the non-HTTP-related work happens.
func (webhook *webhook) validateOrMutate(ctx context.Context, request *admissionV1.AdmissionRequest, operation webhookOperation) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	if request.Kind.Kind != "Pod" {
		return nil, &podAdmissionError{error: fmt.Errorf("expected a Pod object, got a %v", request.Kind.Kind), code: http.StatusBadRequest}
	}

	pod, err := unmarshallPod(request.Object)
	if err != nil {
		return nil, err
	}

	switch request.Operation {
	case admissionV1.Create:
		switch operation {
		case validate:
			return webhook.validateCreateRequest(ctx, pod, request.Namespace)
		case mutate:
			return webhook.mutateCreateRequest(ctx, pod)
		default:
			// shouldn't happen, but needed so that all paths in the function have a return value
			panic(fmt.Errorf("unexpected webhook operation: %v", operation))
		}

	case admissionV1.Update:
		if operation == validate {
			oldPod, err := unmarshallPod(request.OldObject)
			if err != nil {
				return nil, err
			}
			return validateUpdateRequest(pod, oldPod)
		}

		// we only do validation on updates, no mutation
		return &admissionV1.AdmissionResponse{Allowed: true}, nil
	default:
		return nil, &podAdmissionError{error: fmt.Errorf("unpexpected operation %s", request.Operation), pod: pod, code: http.StatusBadRequest}
	}
}

// unmarshallPod unmarshalls a pod object from its raw JSON representation.
func unmarshallPod(object runtime.RawExtension) (*corev1.Pod, *podAdmissionError) {
	pod := &corev1.Pod{}
	if err := json.Unmarshal(object.Raw, pod); err != nil {
		return nil, &podAdmissionError{error: fmt.Errorf("unable to unmarshall pod JSON object: %v", err), code: http.StatusBadRequest}
	}

	return pod, nil
}

// validateCreateRequest ensures that the GMSA contents set in the pod's spec
// match the corresponding GMSA names, and that the pod's service account
// is authorized to `use` the requested GMSA's.
func (webhook *webhook) validateCreateRequest(ctx context.Context, pod *corev1.Pod, namespace string) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	if err := iterateOverWindowsSecurityOptions(pod, func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, _ int) *podAdmissionError {
		if credSpecName := windowsOptions.GMSACredentialSpecName; credSpecName != nil {
			// let's check that the associated service account can read the relevant cred spec CRD
			if authorized, reason := webhook.client.isAuthorizedToUseCredSpec(ctx, pod.Spec.ServiceAccountName, namespace, *credSpecName); !authorized {
				msg := fmt.Sprintf("service account %q is not authorized to `use` GMSA cred spec %q", pod.Spec.ServiceAccountName, *credSpecName)
				if reason != "" {
					msg += fmt.Sprintf(", reason: %q", reason)
				}
				return &podAdmissionError{error: fmt.Errorf(msg), pod: pod, code: http.StatusForbidden}
			}

			// and the contents should match the ones contained in the GMSA resource with that name
			if credSpecContents := windowsOptions.GMSACredentialSpec; credSpecContents != nil {
				if expectedContents, code, retrieveErr := webhook.client.retrieveCredSpecContents(ctx, *credSpecName); retrieveErr != nil {
					return &podAdmissionError{error: retrieveErr, pod: pod, code: code}
				} else if specsEqual, compareErr := compareCredSpecContents(*credSpecContents, expectedContents); !specsEqual || compareErr != nil {
					msg := fmt.Sprintf("the GMSA cred spec contents for %s %q does not match the contents of GMSA resource %q", resourceKind, resourceName, *credSpecName)
					if compareErr != nil {
						msg += fmt.Sprintf(": %v", compareErr)
					}
					return &podAdmissionError{error: fmt.Errorf(msg), pod: pod, code: http.StatusUnprocessableEntity}
				}
			}
		} else if windowsOptions.GMSACredentialSpec != nil {
			// the GMSA's name is not set, but the contents are
			msg := fmt.Sprintf("%s %q has a GMSA cred spec set, but does not define the name of the corresponding resource", resourceKind, resourceName)
			return &podAdmissionError{error: fmt.Errorf(msg), pod: pod, code: http.StatusUnprocessableEntity}
		}

		return nil
	}); err != nil {
		return nil, err
	}

	return &admissionV1.AdmissionResponse{Allowed: true}, nil
}

// compareCredSpecContents returns true iff the two strings represent the same credential spec contents.
func compareCredSpecContents(fromResource, fromCRD string) (bool, error) {
	// this is actually what happens almost all the time, when users don't set the GMSA contents directly
	// but instead rely on the mutating webhook to do that for them; and in that case no need for a slow
	// JSON parsing and comparison
	if fromResource == fromCRD {
		return true, nil
	}

	var (
		jsonObjectFromResource map[string]interface{}
		jsonObjectFromCRD      map[string]interface{}
	)

	if err := json.Unmarshal([]byte(fromResource), &jsonObjectFromResource); err != nil {
		return false, fmt.Errorf("unable to parse %q as a JSON object: %v", fromResource, err)
	}
	if err := json.Unmarshal([]byte(fromCRD), &jsonObjectFromCRD); err != nil {
		return false, fmt.Errorf("unable to parse CRD %q as a JSON object: %v", fromCRD, err)
	}

	return reflect.DeepEqual(jsonObjectFromResource, jsonObjectFromCRD), nil
}

// mutateCreateRequest inlines the requested GMSA's into the pod's and containers' `WindowsSecurityOptions` structs.
func (webhook *webhook) mutateCreateRequest(ctx context.Context, pod *corev1.Pod) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	var patches []map[string]string
	hasGMSA := false

	if err := iterateOverWindowsSecurityOptions(pod, func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, containerIndex int) *podAdmissionError {
		if credSpecName := windowsOptions.GMSACredentialSpecName; credSpecName != nil {
			hasGMSA = true
			// if the user has pre-set the GMSA's contents, we won't override it - it'll be down
			// to the validation endpoint to make sure the contents actually are what they should
			if credSpecContents := windowsOptions.GMSACredentialSpec; credSpecContents == nil {
				contents, code, retrieveErr := webhook.client.retrieveCredSpecContents(ctx, *credSpecName)
				if retrieveErr != nil {
					return &podAdmissionError{error: retrieveErr, pod: pod, code: code}
				}

				partialPath := ""
				if resourceKind == containerKind {
					partialPath = fmt.Sprintf("/containers/%d", containerIndex)
				}

				// worth noting that this JSON patch is guaranteed to work since we know at this point
				// that the resource comprises a `windowsOptions` object, and and that it doesn't have a
				// "gmsaCredentialSpec" field
				patches = append(patches, map[string]string{
					"op":    "add",
					"path":  fmt.Sprintf("/spec%s/securityContext/windowsOptions/gmsaCredentialSpec", partialPath),
					"value": contents,
				})
			}
		}

		return nil
	}); err != nil {
		return nil, err
	}

	if hasGMSA && webhook.config.EnableRandomHostName {
		// Pods are GMSA related, Env enabled, patch the hostname only if it is empty
		hostName := pod.Spec.Hostname
		if hostName == "" {
			hostName = generateUUID()
			patches = append(patches, map[string]string{
				"op":    "add",
				"path":  "/spec/hostname",
				"value": hostName,
			})
		} else {
			// Will honor the hostname set in the spec, print out a message
			logrus.Warnf("hostname is set in spec and will be hornored instead of being randomized")
		}
	}

	admissionResponse := &admissionV1.AdmissionResponse{Allowed: true}
	if len(patches) != 0 {
		patchesBytes, err := json.Marshal(patches)
		if err != nil {
			return nil, &podAdmissionError{error: fmt.Errorf("unable to marshall patch JSON %v: %v", patches, err), pod: pod, code: http.StatusInternalServerError}
		}

		admissionResponse.Patch = patchesBytes
		patchType := admissionV1.PatchTypeJSONPatch
		admissionResponse.PatchType = &patchType
	}

	return admissionResponse, nil
}

// validateUpdateRequest ensures that there are no updates to any of the GMSA names or contents.
func validateUpdateRequest(pod, oldPod *corev1.Pod) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	var oldPodContainerOptions map[string]*corev1.WindowsSecurityContextOptions

	if err := iterateOverWindowsSecurityOptions(pod, func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, _ int) *podAdmissionError {
		var oldWindowsOptions *corev1.WindowsSecurityContextOptions
		if resourceKind == podKind {
			if oldPod.Spec.SecurityContext != nil {
				oldWindowsOptions = oldPod.Spec.SecurityContext.WindowsOptions
			}
		} else {
			// it's a container; look for the same container in the old pod,
			// lazily building the map of container names to security options if needed
			if oldPodContainerOptions == nil {
				oldPodContainerOptions = make(map[string]*corev1.WindowsSecurityContextOptions)
				iterateOverWindowsSecurityOptions(oldPod, func(winOpts *corev1.WindowsSecurityContextOptions, rsrcKind gmsaResourceKind, rsrcName string, _ int) *podAdmissionError {
					if rsrcKind == containerKind {
						oldPodContainerOptions[rsrcName] = winOpts
					}
					return nil
				})
			}

			oldWindowsOptions = oldPodContainerOptions[resourceName]
		}

		if oldWindowsOptions == nil {
			oldWindowsOptions = &corev1.WindowsSecurityContextOptions{}
		}

		var modifiedFieldNames []string
		if !equalStringPointers(windowsOptions.GMSACredentialSpecName, oldWindowsOptions.GMSACredentialSpecName) {
			modifiedFieldNames = append(modifiedFieldNames, "name")
		}
		if !equalStringPointers(windowsOptions.GMSACredentialSpec, oldWindowsOptions.GMSACredentialSpec) {
			modifiedFieldNames = append(modifiedFieldNames, "contents")
		}

		if len(modifiedFieldNames) != 0 {
			msg := fmt.Errorf("cannot update an existing pod's GMSA settings (GMSA %s modified on %s %q)", strings.Join(modifiedFieldNames, " and "), resourceKind, resourceName)
			return &podAdmissionError{error: msg, pod: pod, code: http.StatusForbidden}
		}

		return nil
	}); err != nil {
		return nil, err
	}

	return &admissionV1.AdmissionResponse{Allowed: true}, nil
}

func equalStringPointers(s1, s2 *string) bool {
	if s1 == nil {
		return s2 == nil
	}
	if s2 == nil {
		return false
	}
	return *s1 == *s2
}

// iterateOverWindowsSecurityOptions calls `f` on the pod's `.Spec.SecurityContext.WindowsOptions` field,
// as well as over each of its container's `.SecurityContext.WindowsOptions` field.
// `f` can assume it only gets called with non-nil `WindowsSecurityOptions` pointers; the other
// arguments give information on the resource owning that pointer - in particular, if that
// resource is a container, `containerIndex` is the index of the container in the spec's list (-1 for pods).
// If `f` returns an error, that breaks the loop, and the error is bubbled up.
func iterateOverWindowsSecurityOptions(pod *corev1.Pod, f func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, containerIndex int) *podAdmissionError) *podAdmissionError {
	if pod.Spec.SecurityContext != nil && pod.Spec.SecurityContext.WindowsOptions != nil {
		if err := f(pod.Spec.SecurityContext.WindowsOptions, podKind, pod.Name, -1); err != nil {
			return err
		}
	}

	for i, container := range pod.Spec.Containers {
		if container.SecurityContext != nil && container.SecurityContext.WindowsOptions != nil {
			if err := f(container.SecurityContext.WindowsOptions, containerKind, container.Name, i); err != nil {
				return err
			}
		}
	}

	return nil
}

// deniedAdmissionResponse is a helper function to create an AdmissionResponse
// with an embedded error.
func deniedAdmissionResponse(err error, httpCode ...int) *admissionV1.AdmissionResponse {
	var code int
	logMsg := "refusing to admit"

	if admissionError, ok := err.(*podAdmissionError); ok {
		code = admissionError.code
		if admissionError.pod != nil {
			logMsg += fmt.Sprintf(" pod %+v", admissionError.pod)
		}
	}

	if len(httpCode) > 0 {
		code = httpCode[0]
	}

	if code != 0 {
		logMsg += fmt.Sprintf(" with code %v", code)
	}

	logrus.Infof("%s: %v", logMsg, err)

	return &admissionV1.AdmissionResponse{
		Allowed: false,
		Result: &metav1.Status{
			Message: err.Error(),
			Code:    int32(code),
		},
	}
}

// stolen from https://github.com/golang/go/blob/go1.12/src/net/http/server.go#L3255-L3271
type tcpKeepAliveListener struct {
	*net.TCPListener
}

func (ln tcpKeepAliveListener) Accept() (net.Conn, error) {
	tc, err := ln.AcceptTCP()
	if err != nil {
		return nil, err
	}
	tc.SetKeepAlive(true)
	tc.SetKeepAlivePeriod(3 * time.Minute)
	return tc, nil
}

func generateUUID() string {
	// Generate a new UUID
	id := uuid.New()
	// Convert to string and get the first 15 characters in lower case
	shortUUID := strings.ToLower(id.String()[:15])
	return shortUUID
}
```

## File: `admission-webhook/webhook_http_test.go`
```go
package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	admissionV1 "k8s.io/api/admission/v1"
	authenticationv1 "k8s.io/api/authentication/v1"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/apimachinery/pkg/types"
)

// this is just a quick-and-dirty test to ensure the HTTP server works. E2e/integration tests explore
// this much further.
func TestHTTPWebhook(t *testing.T) {
	var requestUID types.UID = "283f4877-34d4-11e9-a9f1-06da3a0adce4"

	pod := buildPod(dummyServiceAccoutName, buildWindowsOptions(dummyCredSpecName, ""), map[string]*corev1.WindowsSecurityContextOptions{"container-name": nil})

	admissionRequest := &admissionV1.AdmissionReview{
		Request: &admissionV1.AdmissionRequest{
			UID: requestUID,
			Kind: metav1.GroupVersionKind{
				Version: "v1",
				Kind:    "Pod",
			},
			Resource: metav1.GroupVersionResource{
				Version:  "v1",
				Resource: "pods",
			},
			Namespace: dummyNamespace,
			Operation: admissionV1.Create,
			UserInfo: authenticationv1.UserInfo{
				Username: "system:serviceaccount:kube-system:replicaset-controller",
				UID:      "cb335ac0-34b4-11e9-9745-06da3a0adce4",
				Groups:   []string{"system:serviceaccounts", "system:serviceaccounts:kube-system"},
			},
			Object: runtime.RawExtension{
				Object: pod,
			},
		},
	}

	authorizedToUseCredSpec := true

	kubeClient := &dummyKubeClient{
		isAuthorizedToUseCredSpecFunc: func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
			assert.Equal(t, dummyServiceAccoutName, serviceAccountName)
			assert.Equal(t, dummyNamespace, namespace)
			assert.Equal(t, dummyCredSpecName, credSpecName)

			return authorizedToUseCredSpec, "bogus reason"
		},
		retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
			assert.Equal(t, dummyCredSpecName, credSpecName)

			contents = dummyCredSpecContents
			return
		},
	}

	t.Run("success path", func(t *testing.T) {
		port, tearDownHTTP := startHTTPServer(t, kubeClient)
		defer tearDownHTTP()

		httpCode, response := makeHTTPRequest(t, port, "POST", "mutate", admissionRequest)
		assert.Equal(t, http.StatusOK, httpCode)
		require.NotNil(t, response)
		require.NotNil(t, response.Response)

		assert.Equal(t, requestUID, response.Response.UID)
		assert.True(t, response.Response.Allowed)

		if assert.NotNil(t, response.Response.PatchType) {
			assert.Equal(t, admissionV1.PatchTypeJSONPatch, *response.Response.PatchType)
		}

		var patches []map[string]string
		if err := json.Unmarshal(response.Response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, 1, len(patches)) {
			expectedPatch := map[string]string{
				"op":    "add",
				"path":  "/spec/securityContext/windowsOptions/gmsaCredentialSpec",
				"value": dummyCredSpecContents,
			}
			assert.Equal(t, expectedPatch, patches[0])
		}
	})

	t.Run("failure", func(t *testing.T) {
		previousAuthorizedToUseCredSpec := authorizedToUseCredSpec
		authorizedToUseCredSpec = false
		defer func() { authorizedToUseCredSpec = previousAuthorizedToUseCredSpec }()

		port, tearDownHTTP := startHTTPServer(t, kubeClient)
		defer tearDownHTTP()

		httpCode, response := makeHTTPRequest(t, port, "POST", "validate", admissionRequest)
		assert.Equal(t, http.StatusOK, httpCode)
		require.NotNil(t, response)
		require.NotNil(t, response.Response)

		assert.Equal(t, requestUID, response.Response.UID)
		assert.False(t, response.Response.Allowed)

		require.NotNil(t, response.Response.Result)
		assert.Equal(t, int32(http.StatusForbidden), response.Response.Result.Code)
		expectedSubstr := fmt.Sprintf("service account %q is not authorized to `use` GMSA cred spec", dummyServiceAccoutName)
		assert.Contains(t, response.Response.Result.Message, expectedSubstr)
	})

	for _, path := range []string{"validate", "mutate"} {
		t.Run(fmt.Sprintf("wrong HTTP method for %s", path), func(t *testing.T) {
			port, tearDownHTTP := startHTTPServer(t, kubeClient)
			defer tearDownHTTP()

			httpCode, response := makeHTTPRequest(t, port, "PUT", path, admissionRequest)
			assert.Equal(t, http.StatusMethodNotAllowed, httpCode)
			assert.Nil(t, response)
		})

		t.Run(fmt.Sprintf("wrong content-type for %s", path), func(t *testing.T) {
			port, tearDownHTTP := startHTTPServer(t, kubeClient)
			defer tearDownHTTP()

			httpCode, response := makeHTTPRequest(t, port, "POST", path, admissionRequest, "content-type", "text/plain")
			assert.Equal(t, http.StatusUnsupportedMediaType, httpCode)
			assert.Nil(t, response)
		})

		t.Run(fmt.Sprintf("wrong object kind for %s", path), func(t *testing.T) {
			previousKind := admissionRequest.Request.Kind.Kind
			admissionRequest.Request.Kind.Kind = "Deployment"
			defer func() { admissionRequest.Request.Kind.Kind = previousKind }()

			port, tearDownHTTP := startHTTPServer(t, kubeClient)
			defer tearDownHTTP()

			httpCode, response := makeHTTPRequest(t, port, "POST", path, admissionRequest)
			assert.Equal(t, http.StatusOK, httpCode)
			require.NotNil(t, response)
			require.NotNil(t, response.Response)

			assert.Equal(t, requestUID, response.Response.UID)
			assert.False(t, response.Response.Allowed)

			require.NotNil(t, response.Response.Result)
			assert.Equal(t, int32(http.StatusBadRequest), response.Response.Result.Code)
			assert.Equal(t, "expected a Pod object, got a Deployment", response.Response.Result.Message)
		})
	}

	t.Run("wrong route", func(t *testing.T) {
		port, tearDownHTTP := startHTTPServer(t, kubeClient)
		defer tearDownHTTP()

		httpCode, response := makeHTTPRequest(t, port, "POST", "i_dont_exist", admissionRequest)
		assert.Equal(t, http.StatusNotFound, httpCode)
		assert.Nil(t, response)
	})
}

func TestStartHTTPWebhookWithCertReload(t *testing.T) {
	authorizedToUseCredSpec := true

	kubeClient := &dummyKubeClient{
		isAuthorizedToUseCredSpecFunc: func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
			assert.Equal(t, dummyServiceAccoutName, serviceAccountName)
			assert.Equal(t, dummyNamespace, namespace)
			assert.Equal(t, dummyCredSpecName, credSpecName)

			return authorizedToUseCredSpec, "bogus reason"
		},
		retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
			assert.Equal(t, dummyCredSpecName, credSpecName)

			contents = dummyCredSpecContents
			return
		},
	}

	webhook := newWebhookWithOptions(kubeClient, WithCertReload(true))
	port := getAvailablePort(t)
	tlsConfig := &tlsConfig{
		crtPath: "testdata/cert.pem",
		keyPath: "testdata/key.pem",
	}

	listeningChan := make(chan interface{})
	go func() {
		assert.Nil(t, webhook.start(port, tlsConfig, listeningChan))
	}()
	defer webhook.stop()

	select {
	case <-listeningChan:
		for {
			if webhook.server.TLSConfig != nil {
				break
			}
			time.Sleep(10 * time.Millisecond)
		}
		assert.NotNil(t, webhook.server.TLSConfig.GetCertificate)
	case <-time.After(5 * time.Second):
		t.Fatalf("Timed out waiting for HTTP server to start listening on %d", port)
	}
}

func startHTTPServer(t *testing.T, kubeClient *dummyKubeClient) (int, func()) {
	webhook := newWebhook(kubeClient)
	port := getAvailablePort(t)

	listeningChan := make(chan interface{})
	go func() {
		assert.Nil(t, webhook.start(port, nil, listeningChan))
	}()

	select {
	case <-listeningChan:
	case <-time.After(5 * time.Second):
		t.Fatalf("Timed out waiting for HTTP server to start listening on %d", port)
	}

	return port, func() {
		assert.Nil(t, webhook.stop())
	}
}

func makeHTTPRequest(t *testing.T, port int, method string, path string, admissionRequest *admissionV1.AdmissionReview, headers ...string) (httpCode int, admissionResponse *admissionV1.AdmissionReview) {
	require.Equal(t, 0, len(headers)%2, "header names and values should be provided in pairs")

	reqBody, err := json.Marshal(admissionRequest)
	require.Nil(t, err)

	url := fmt.Sprintf("http://localhost:%d/%s", port, path)
	req, err := http.NewRequest(method, url, bytes.NewBuffer(reqBody))
	require.Nil(t, err)

	i := 0
	for i < len(headers) {
		req.Header.Set(headers[i], headers[i+1])
		i += 2
	}
	if req.Header.Get("Content-Type") == "" {
		req.Header.Set("Content-Type", "application/json")
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	require.Nil(t, err)

	defer resp.Body.Close()
	respBody, err := ioutil.ReadAll(resp.Body)
	require.Nil(t, err)

	admissionResponse = &admissionV1.AdmissionReview{}
	if err := json.Unmarshal(respBody, admissionResponse); err != nil {
		admissionResponse = nil
	}

	return resp.StatusCode, admissionResponse
}

// getAvailablePort asks the kernel for an available port, that is ready to use.
func getAvailablePort(t *testing.T) int {
	addr, err := net.ResolveTCPAddr("tcp", "localhost:0")
	require.Nil(t, err)

	listen, err := net.ListenTCP("tcp", addr)
	require.Nil(t, err)

	defer listen.Close()
	return listen.Addr().(*net.TCPAddr).Port
}
```

## File: `admission-webhook/webhook_test.go`
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	admissionV1 "k8s.io/api/admission/v1"
	corev1 "k8s.io/api/core/v1"
)

func TestValidateCreateRequest(t *testing.T) {
	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with empty GMSA settings": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with no GMSA settings": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			webhook := newWebhook(nil)
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		})
	}

	kubeClientFactory := func() *dummyKubeClient {
		return &dummyKubeClient{
			retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					contents = dummyCredSpecContents
				} else {
					contents = credSpecName + "-contents"
				}
				return
			},
		}
	}

	winOptionsFactory := func(containerName string) *corev1.WindowsSecurityContextOptions {
		return buildWindowsOptions(containerName+"-cred-spec", containerName+"-cred-spec-contents")
	}

	runWebhookValidateOrMutateTests(t, winOptionsFactory, map[string]webhookValidateOrMutateTest{
		"with matching name & content, it passes": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		},

		"if the cred spec contents are not byte-to-byte equal to that of the one named, but still represent equivalent JSONs, it passes": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(
				optionsSelector(pod),
				dummyCredSpecName,
				`{"All in all you're just another":      {"the":"wall","brick":   "in"},"We don't need no":["education", "thought control","dark sarcasm in the classroom"]}`,
			)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		},

		"if the cred spec contents are not that of the one named, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(
				optionsSelector(pod),
				dummyCredSpecName,
				`{"We don't need no": ["money"], "All in all you're just another": {"brick": "in", "the": "wall"}}`,
			)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusUnprocessableEntity,
				"the GMSA cred spec contents for %s %q does not match the contents of GMSA resource %q",
				resourceKind, resourceName, dummyCredSpecName)
		},

		"if the cred spec contents are not byte-to-byte equal to that of the one named, and are not even a valid JSON object, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "i ain't no JSON object")

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusUnprocessableEntity,
				"the GMSA cred spec contents for %s %q does not match the contents of GMSA resource %q",
				resourceKind, resourceName, dummyCredSpecName)
		},

		"if the contents are set, but the name one isn't provided, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), "", dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)

			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusUnprocessableEntity,
				"%s %q has a GMSA cred spec set, but does not define the name of the corresponding resource",
				resourceKind, resourceName)
		},

		"if the service account is not authorized to use the cred-spec, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			dummyReason := "dummy reason"

			client := kubeClientFactory()
			client.isAuthorizedToUseCredSpecFunc = func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
				if credSpecName == dummyCredSpecName {
					assert.Equal(t, dummyServiceAccoutName, serviceAccountName)
					assert.Equal(t, dummyNamespace, namespace)

					return false, dummyReason
				}

				return true, ""
			}

			webhook := newWebhook(client)

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"service account %q is not authorized to `use` GMSA cred spec %q, reason: %q",
				dummyServiceAccoutName, dummyCredSpecName, dummyReason)
		},

		"if there is an error when retrieving the cred-spec's contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			dummyError := fmt.Errorf("dummy error")

			client := kubeClientFactory()
			previousRetrieveCredSpecContentsFunc := client.retrieveCredSpecContentsFunc
			client.retrieveCredSpecContentsFunc = func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					return "", http.StatusNotFound, dummyError
				}
				return previousRetrieveCredSpecContentsFunc(ctx, credSpecName)
			}

			webhook := newWebhook(client)

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)

			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusNotFound, dummyError.Error())
		},
	})
}

func TestMutateCreateRequest(t *testing.T) {
	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with empty GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with no GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			webhook := newWebhookWithOptions(nil, WithRandomHostname(false))
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)

			assert.Nil(t, response.Patch)

		})
	}

	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with random hostname env set and empty GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with random hostname env set and no GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			webhook := newWebhookWithOptions(nil, WithRandomHostname(true))
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)

			assert.Nil(t, response.Patch)

		})
	}

	testCaseName, winOptionsFactory1 := "with random hostname env set and dummy GMSA settings, it passes and set random hostname", func() *corev1.WindowsSecurityContextOptions {
		dummyCredSpecNameVar := dummyCredSpecName
		dummyCredSpecContentsVar := dummyCredSpecContents
		return &corev1.WindowsSecurityContextOptions{GMSACredentialSpecName: &dummyCredSpecNameVar, GMSACredentialSpec: &dummyCredSpecContentsVar}
	}
	t.Run(testCaseName, func(t *testing.T) {
		webhook := newWebhookWithOptions(nil, WithRandomHostname(true))
		pod := buildPod(dummyServiceAccoutName, winOptionsFactory1(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory1()})

		response, err := webhook.mutateCreateRequest(context.Background(), pod)
		assert.Nil(t, err)

		require.NotNil(t, response)
		assert.True(t, response.Allowed)

		var patches []map[string]string
		// one more because we're adding the hostname
		if err := json.Unmarshal(response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, 1, len(patches)) {
			foundHostname := false
			for _, patch := range patches {
				if value, hasValue := patch["value"]; assert.True(t, hasValue) {
					if patch["path"] == "/spec/hostname" {
						foundHostname = true
						assert.Equal(t, "add", patch["op"])
						assert.Equal(t, 15, len(value))
					}
				}
			}
			assert.True(t, foundHostname)
		}
	})

	testCaseName, winOptionsFactory1 = "with random hostname env set and dummy GMSA settings and hostname set in spec, it passes and do nothing", func() *corev1.WindowsSecurityContextOptions {
		dummyCredSpecNameVar := dummyCredSpecName
		dummyCredSpecContentsVar := dummyCredSpecContents
		return &corev1.WindowsSecurityContextOptions{GMSACredentialSpecName: &dummyCredSpecNameVar, GMSACredentialSpec: &dummyCredSpecContentsVar}
	}
	t.Run(testCaseName, func(t *testing.T) {
		webhook := newWebhookWithOptions(nil, WithRandomHostname(true))
		dummyPodNameVar := dummyPodName
		pod := buildPodWithHostName(dummyServiceAccoutName, &dummyPodNameVar, winOptionsFactory1(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory1()})

		response, err := webhook.mutateCreateRequest(context.Background(), pod)
		assert.Nil(t, err)

		require.NotNil(t, response)
		assert.True(t, response.Allowed)

		assert.Nil(t, response.Patch)
	})

	kubeClientFactory := func() *dummyKubeClient {
		return &dummyKubeClient{
			retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					contents = dummyCredSpecContents
				} else {
					contents = credSpecName + "-contents"
				}
				return
			},
		}
	}

	winOptionsFactory := func(containerName string) *corev1.WindowsSecurityContextOptions {
		return buildWindowsOptions(containerName+"-cred-spec", "")
	}

	runWebhookValidateOrMutateTests(t, winOptionsFactory, map[string]webhookValidateOrMutateTest{
		"with random hostname env and a GMSA cred spec name, it passes and inlines the cred-spec's contents and generate random hostname": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhookWithOptions(kubeClientFactory(), WithRandomHostname(true))

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "")

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)

			if assert.NotNil(t, response.PatchType) {
				assert.Equal(t, admissionV1.PatchTypeJSONPatch, *response.PatchType)
			}

			patchPath := func(kind gmsaResourceKind, name string) string {
				partialPath := ""

				if kind == containerKind {
					containerIndex := -1
					for i, container := range pod.Spec.Containers {
						if container.Name == name {
							containerIndex = i
							break
						}
					}
					if containerIndex == -1 {
						t.Fatalf("Did not find any container named %q", name)
					}

					partialPath = fmt.Sprintf("/containers/%d", containerIndex)
				}

				return fmt.Sprintf("/spec%s/securityContext/windowsOptions/gmsaCredentialSpec", partialPath)
			}

			// maps the contents to the expected patch for that container
			expectedPatches := make(map[string]map[string]string)
			for i := 0; i < len(pod.Spec.Containers)-1; i++ {
				credSpecContents := extraContainerName(i) + "-cred-spec-contents"
				expectedPatches[credSpecContents] = map[string]string{
					"op":    "add",
					"path":  patchPath(containerKind, extraContainerName(i)),
					"value": credSpecContents,
				}
			}
			// and the patch for this test's specific cred spec
			expectedPatches[dummyCredSpecContents] = map[string]string{
				"op":    "add",
				"path":  patchPath(resourceKind, resourceName),
				"value": dummyCredSpecContents,
			}

			var patches []map[string]string
			// len(pod.Spec.Containers)+1 because we're adding the hostname
			if err := json.Unmarshal(response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, len(pod.Spec.Containers)+1, len(patches)) {
				foundHostname := false
				for _, patch := range patches {
					if value, hasValue := patch["value"]; assert.True(t, hasValue) {
						if patch["path"] == "/spec/hostname" {
							foundHostname = true
							assert.Equal(t, "add", patch["op"])
							assert.Equal(t, 15, len(value))
						} else if expectedPatch, present := expectedPatches[value]; assert.True(t, present, "value %s not found in expected patches", value) {
							assert.Equal(t, expectedPatch, patch)
						}
					}
				}
				assert.True(t, foundHostname)
			}
		},

		// random hostname env not set in the following cases, and validated no hostname is set (implicitly)
		"it the cred spec's contents are already set, along with its name, it passes and doesn't overwrite the provided contents": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, `{"pre-set GMSA": "cred contents"}`)

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			// all the patches we receive should be for the extra containers
			expectedPatchesLen := len(pod.Spec.Containers) - 1

			if expectedPatchesLen == 0 {
				assert.Nil(t, response.PatchType)
				assert.Nil(t, response.Patch)
			} else {
				var patches []map[string]string
				if err := json.Unmarshal(response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, expectedPatchesLen, len(patches)) {
					for _, patch := range patches {
						if path, hasPath := patch["path"]; assert.True(t, hasPath) {
							assert.NotContains(t, path, dummyCredSpecName)
						}
					}
				}
			}
		},

		"if there is an error when retrieving the cred-spec's contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			dummyError := fmt.Errorf("dummy error")

			client := kubeClientFactory()
			previousRetrieveCredSpecContentsFunc := client.retrieveCredSpecContentsFunc
			client.retrieveCredSpecContentsFunc = func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					return "", http.StatusNotFound, dummyError
				}
				return previousRetrieveCredSpecContentsFunc(ctx, credSpecName)
			}

			webhook := newWebhook(client)

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "")

			response, err := webhook.mutateCreateRequest(context.Background(), pod)

			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusNotFound, dummyError.Error())
		},
	})
}

func TestValidateUpdateRequest(t *testing.T) {
	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with empty GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with no GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})
			oldPod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		})
	}

	winOptionsFactory := func(containerName string) *corev1.WindowsSecurityContextOptions {
		return buildWindowsOptions(containerName+"-cred-spec", containerName+"-cred-spec-contents")
	}

	runWebhookValidateOrMutateTests(t, winOptionsFactory, map[string]webhookValidateOrMutateTest{
		"if there was no changes to GMSA settings, it passes": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			oldPod := pod.DeepCopy()

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		},

		"if there was a change to a GMSA name, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			setWindowsOptions(optionsSelector(pod), "new-cred-spec-name", dummyCredSpecContents)

			oldPod := pod.DeepCopy()
			setWindowsOptions(optionsSelector(oldPod), dummyCredSpecName, "")

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"cannot update an existing pod's GMSA settings (GMSA name modified on %s %q)",
				resourceKind, resourceName)
		},

		"if there was a change to a GMSA contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "new-cred-spec-contents")

			oldPod := pod.DeepCopy()
			setWindowsOptions(optionsSelector(oldPod), "", dummyCredSpecContents)

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"cannot update an existing pod's GMSA settings (GMSA contents modified on %s %q)",
				resourceKind, resourceName)
		},

		"if there were changes to both GMSA name & contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			setWindowsOptions(optionsSelector(pod), "new-cred-spec-name", "new-cred-spec-contents")

			oldPod := pod.DeepCopy()
			setWindowsOptions(optionsSelector(oldPod), dummyCredSpecName, dummyCredSpecContents)

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"cannot update an existing pod's GMSA settings (GMSA name and contents modified on %s %q)",
				resourceKind, resourceName)
		},
	})
}

func TestDefaultWebhookConfig(t *testing.T) {
	expectedCertReload := false
	webhook := newWebhookWithOptions(nil, WithCertReload(expectedCertReload))
	assert.Equal(t, expectedCertReload, webhook.config.EnableCertReload)
}

func TestSetWebhookConfig(t *testing.T) {
	expectedCertReload := true
	expectedRandomHostname := true
	randomHostname := true
	webhook := newWebhookWithOptions(nil, WithCertReload(expectedCertReload), WithRandomHostname(randomHostname))
	assert.Equal(t, expectedCertReload, webhook.config.EnableCertReload)
	assert.Equal(t, expectedRandomHostname, webhook.config.EnableRandomHostName)
}

func TestEqualStringPointers(t *testing.T) {
	ptrToString := func(s *string) string {
		if s == nil {
			return "nil"
		}
		return " = " + *s
	}

	foo := "foo"
	bar := "bar"

	for _, testCase := range []struct {
		s1             *string
		s2             *string
		expectedResult bool
	}{
		{
			s1:             nil,
			s2:             nil,
			expectedResult: true,
		},
		{
			s1:             &foo,
			s2:             nil,
			expectedResult: false,
		},
		{
			s1:             &foo,
			s2:             &foo,
			expectedResult: true,
		},
		{
			s1:             &foo,
			s2:             &bar,
			expectedResult: false,
		},
	} {
		for _, ptrs := range [][]*string{
			{testCase.s1, testCase.s2},
			{testCase.s2, testCase.s1},
		} {
			s1 := ptrs[0]
			s2 := ptrs[1]

			testName := fmt.Sprintf("with s1 %s and s2 %s, should return %v",
				ptrToString(s1),
				ptrToString(s2),
				testCase.expectedResult)

			t.Run(testName, func(t *testing.T) {
				assert.Equal(t, testCase.expectedResult, equalStringPointers(s1, s2))
			})
		}
	}
}

/* Helpers below */

type containerWindowsOptionsFactory func(containerName string) *corev1.WindowsSecurityContextOptions

type winOptionsSelector func(pod *corev1.Pod) *corev1.WindowsSecurityContextOptions

// a webhookValidateOrMutateTest function should run a test on one of the webhook's validate or mutate
// functions, given a selector to extract the WindowsSecurityOptions struct it can play with from the pod.
// It should assume that the pod it receives has any number of extra containers with correct
// (in the sense of the test) windows security options generated by a relevant containerWindowsOptionsFactory.
type webhookValidateOrMutateTest func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string)

// runWebhookValidateOrMutateTests runs the given tests with 0 to 5 extra containers with correct windows
// security options as generated by winOptionsFactory.
func runWebhookValidateOrMutateTests(t *testing.T, winOptionsFactory containerWindowsOptionsFactory, tests map[string]webhookValidateOrMutateTest) {
	for extraContainersCount := 0; extraContainersCount <= 5; extraContainersCount++ {
		containerNamesAndWindowsOptions := make(map[string]*corev1.WindowsSecurityContextOptions)

		for i := 0; i < extraContainersCount; i++ {
			containerName := extraContainerName(i)
			containerNamesAndWindowsOptions[containerName] = winOptionsFactory(containerName)
		}

		testNameSuffix := ""
		if extraContainersCount > 0 {
			testNameSuffix = fmt.Sprintf(" and %d extra containers", extraContainersCount)
		}

		for _, resourceKind := range []gmsaResourceKind{podKind, containerKind} {
			for testName, testFunc := range tests {
				podWindowsOptions := &corev1.WindowsSecurityContextOptions{}
				containerNamesAndWindowsOptions[dummyContainerName] = &corev1.WindowsSecurityContextOptions{}
				pod := buildPod(dummyServiceAccoutName, podWindowsOptions, containerNamesAndWindowsOptions)

				var optionsSelector winOptionsSelector
				var resourceName string
				switch resourceKind {
				case podKind:
					optionsSelector = func(pod *corev1.Pod) *corev1.WindowsSecurityContextOptions {
						if pod != nil && pod.Spec.SecurityContext != nil {
							return pod.Spec.SecurityContext.WindowsOptions
						}
						return nil
					}

					resourceName = dummyPodName
				case containerKind:
					optionsSelector = func(pod *corev1.Pod) *corev1.WindowsSecurityContextOptions {
						if pod != nil {
							for _, container := range pod.Spec.Containers {
								if container.Name == dummyContainerName {
									if container.SecurityContext != nil {
										return container.SecurityContext.WindowsOptions
									}
									return nil
								}
							}
						}
						return nil
					}

					resourceName = dummyContainerName
				default:
					t.Fatalf("Unknown resource kind: %q", resourceKind)
				}

				t.Run(fmt.Sprintf("%s - with %s-level windows options%s", testName, resourceKind, testNameSuffix), func(t *testing.T) {
					testFunc(t, pod, optionsSelector, resourceKind, resourceName)
				})
			}
		}
	}
}

func extraContainerName(i int) string {
	return fmt.Sprintf("extra-container-%d", i)
}

func assertPodAdmissionErrorContains(t *testing.T, err *podAdmissionError, pod *corev1.Pod, httpCode int, msgFormat string, msgArgs ...interface{}) bool {
	if !assert.NotNil(t, err) {
		return false
	}

	result := assert.Equal(t, pod, err.pod)
	result = assert.Equal(t, httpCode, err.code) && result
	return assert.Contains(t, err.Error(), fmt.Sprintf(msgFormat, msgArgs...)) && result
}
```

## File: `admission-webhook/deploy/.helpers.sh`
```bash
## Meant to be sourced by other files in this repo

echo_stderr() {
    local COLOR
    local NO_COLOR='\033[0m'

    case "$1" in
        green)
            COLOR='\033[0;32m' ;;
        yellow)
            COLOR='\033[0;33m' ;;
        red)
            COLOR='\033[0;31m' ;;
        esac
    shift 1

    >&2 printf "${COLOR}$@\n${NO_COLOR}"
}

info() {
    echo_stderr 'green' "*** $@ ***"
}

warn() {
    echo_stderr 'yellow' "WARNING: $@"
}

fatal_error() {
    echo_stderr 'red' "FATAL ERROR: $@"
    exit 1
}

if [ ! -x "$KUBECTL" ]; then
    KUBECTL=$(command -v kubectl)

    if [ ! -x "$KUBECTL" ]; then
        fatal_error 'kubectl not found'
    fi
fi

echo_or_run() {
    local WITH_KUBECTL_DRY_RUN=false
    if [[ "$1" == '--with-kubectl-dry-run' ]]; then
        WITH_KUBECTL_DRY_RUN=true
        shift
    fi

    if $DRY_RUN; then
        echo "$@"
        if $WITH_KUBECTL_DRY_RUN; then
            eval "$@ --dry-run=client >&2"
        fi
    else
        eval "$@"
    fi
}

wait_for() {
    local FUN="$1"
    local ERROR_MSG="$2"
    local MAX_ATTEMPTS="$3"
    [ "$MAX_ATTEMPTS" ] || MAX_ATTEMPTS=30

    local OUTPUT
    for _ in $(seq "$MAX_ATTEMPTS"); do
        if OUTPUT=$($FUN); then
            echo "$OUTPUT"
            return
        fi
        sleep 1
    done

    local MSG="$ERROR_MSG, giving up after $MAX_ATTEMPTS attempts"
    if [ "$OUTPUT" ]; then
        MSG+=" - last attempt's output: $OUTPUT"
    fi
    fatal_error "$MSG"
}

SERVER_KEY="$CERTS_DIR/server-key.pem"
SERVER_CERT="$CERTS_DIR/server-cert.pem"

if [ "$K8S_WINDOWS_GMSA_DEPLOY_DEBUG" ]; then
    set -x
fi
```

## File: `admission-webhook/deploy/create-signed-cert.sh`
```bash
#!/usr/bin/env bash

## Generates cluster-valid SSL certs for the webhook service
## Inspired from
## https://raw.githubusercontent.com/istio/istio/release-0.7/install/kubernetes/webhook-create-signed-cert.sh
## whose license is also Apache 2.0

set -e

usage() {
    cat <<EOF
Generates certificate suitable for use with the GMSA webhook service.

This script uses k8s' CertificateSigningRequest API to a generate a
certificate signed by k8s CA suitable for use with the GMSA webhook
service. This requires permissions to create and approve CSR. See
https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster for
detailed explantion and additional instructions.

usage: $0 --service SERVICE_NAME --namespace NAMESPACE_NAME --certs-dir PATH/TO/CERTS/DIR [--dry-run] [--overwrite]

If --dry-run is set, the script echoes what command it would perform
to stdout without actually affecting the k8s cluster.
If the files this script generates already exist and --overwrite is
not set, it will not regenerate the files.
EOF
    exit 1
}

SERVICE=
NAMESPACE=
CERTS_DIR=
DRY_RUN=false
OVERWRITE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --service)
            SERVICE="$2" && shift 2 ;;
        --namespace)
            NAMESPACE="$2" && shift 2 ;;
        --certs-dir)
            CERTS_DIR="$2" && shift 2 ;;
        --dry-run)
            DRY_RUN=true && shift ;;
        --overwrite)
            OVERWRITE=true && shift ;;
        *)
            echo "Unknown option: $1"
            usage ;;
    esac
done

[ "$SERVICE" ] && [ "$NAMESPACE" ] && [ "$CERTS_DIR" ] || usage

if [ ! "$K8S_WINDOWS_GMSA_HELPER_SCRIPT" ]; then
    DEPLOY_DIR="$(dirname "$0")"
    K8S_WINDOWS_GMSA_HELPER_SCRIPT="$DEPLOY_DIR/.helpers.sh"
fi
. "$K8S_WINDOWS_GMSA_HELPER_SCRIPT"

if [ ! -x "$(command -v openssl)" ]; then
    fatal_error 'openssl not found'
fi

gen_file() {
    local FUN="$1"
    local FILE_PATH="$2"

    if [ -f "$FILE_PATH" ] && ! $OVERWRITE; then
        warn "$FILE_PATH already exists, not re-generating"
    else
        $FUN
    fi
}

gen_server_key() { openssl genrsa -out "$SERVER_KEY" 2048; }
gen_file gen_server_key "$SERVER_KEY"

CSR_CONF="$CERTS_DIR/csr.conf"
gen_csr_conf() {
    cat <<EOF >> "$CSR_CONF"
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = $SERVICE
DNS.2 = $SERVICE.$NAMESPACE
DNS.3 = $SERVICE.$NAMESPACE.svc
EOF
}
gen_file gen_csr_conf "$CSR_CONF"

SERVER_CSR="$CERTS_DIR/server.csr"
gen_server_scr() { openssl req -new -key "$SERVER_KEY" -subj "/O=system:nodes/CN=system:node:$SERVICE.$NAMESPACE.svc" -out "$SERVER_CSR" -config "$CSR_CONF"; }
gen_file gen_server_scr "$SERVER_CSR"

CSR_NAME="$SERVICE.$NAMESPACE"
# clean-up any previously created CSR for our service
if ! $DRY_RUN && $KUBECTL get csr "$CSR_NAME" &> /dev/null; then
    $KUBECTL delete csr "$CSR_NAME"
fi

# create server cert/key CSR and send to k8s API
CSR_CONTENTS=$(cat <<EOF
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: $CSR_NAME
spec:
  groups:
  - system:authenticated
  request: $(cat "$SERVER_CSR" | base64 -w 0)
  signerName: kubernetes.io/kubelet-serving
  usages:
  - digital signature
  - key encipherment
  - server auth
EOF
)
echo_or_run --with-kubectl-dry-run "$KUBECTL create -f - <<< '$CSR_CONTENTS'"

if ! $DRY_RUN; then
    verify_csr_created() { $KUBECTL get csr "$CSR_NAME" 2>&1 ; }
    wait_for verify_csr_created "CSR $CSR_NAME not properly created"
fi

# approve and fetch the signed certificate
echo_or_run "$KUBECTL certificate approve $CSR_NAME"

if ! $DRY_RUN; then
    verify_cert_signed() {
        local CERT_CONTENTS
        CERT_CONTENTS=$($KUBECTL get csr $CSR_NAME -o jsonpath='{.status.certificate}')
        echo "$CERT_CONTENTS"
        [[ "$CERT_CONTENTS" != "" ]]
    }
    SERVER_CERT_CONTENTS=$(wait_for verify_cert_signed "after approving CSR $CSR_NAME, the signed certificate did not appear on the resource")

    gen_server_cert() { echo "$SERVER_CERT_CONTENTS" | openssl base64 -d -A -out "$SERVER_CERT"; }
    gen_file gen_server_cert "$SERVER_CERT"
fi
```

## File: `admission-webhook/deploy/deploy-gmsa-webhook.sh`
```bash
#!/usr/bin/env bash

## Deploys the GMSA webhook

set -e

usage() {
    cat <<EOF
Deploys the GMSA webhook.

Should be run with a kube admin config file present at either the canonical location
(~/.kube/config) or at the path specified by the KUBECONFIG environment variable.

This script:
 * generates a SSL certificate signed by k8s, for mutual authentication
   between the API server and the webhook service
 * deploys a k8s service running the webhook
 * registers that service as a webhook admission controller

usage: $0 --file MANIFESTS_FILE [--name NAME] [--namespace NAMESPACE] [--image IMAGE_NAME] [--certs-dir CERTS_DIR] [--dry-run] [--overwrite] [--tolerate-master]

MANIFESTS_FILE is the path to the file the k8s manifests will be written to.
NAME defaults to 'gmsa-webhook' and is used in the names of most of the k8s resources created.
NAMESPACE is the namespace to deploy to; defaults to 'gmsa-webhook'.
IMAGE_NAME is the name of the Docker image containing the webhook; defaults to 'sigwindowstools/k8s-gmsa-webhook:latest'
CERTS_DIR defaults to 'gmsa-webhook-certs'

If --dry-run is set, the script echoes what command it would perform
without actually affecting the k8s cluster.
If the files this script generates already exist and --overwrite is
not set, it will not regenerate the files.
If --tolerate-master is set, the webhook will tolerate running on master nodes.
EOF
    exit 1
}

DEPLOY_DIR="$(dirname "$0")"
TMP_DIR_PREFIX='/tmp/gmsa-webhook-deploy-'

# it's possible to override these 2 to download from another repo/branch
[ "$K8S_GMSA_DEPLOY_DOWNLOAD_REPO" ] || K8S_GMSA_DEPLOY_DOWNLOAD_REPO='kubernetes-sigs/windows-gmsa'
[ "$K8S_GMSA_DEPLOY_DOWNLOAD_REV" ] || K8S_GMSA_DEPLOY_DOWNLOAD_REV='master'

ensure_helper_file_present() {
    local NAME="$1"
    local DIR="$DEPLOY_DIR"

    if [ ! -r "$DIR/$NAME" ]; then
        DIR=$(mktemp -d "${TMP_DIR_PREFIX}XXXXXXX")
        local URL="https://raw.githubusercontent.com/$K8S_GMSA_DEPLOY_DOWNLOAD_REPO/$K8S_GMSA_DEPLOY_DOWNLOAD_REV/admission-webhook/deploy/$NAME"

        if which curl &> /dev/null; then
            curl -sL "$URL" > "$DIR/$NAME"
        else
            wget -O "$DIR/$NAME" "$URL"
        fi
    fi

    realpath "$DIR/$NAME"
}

write_manifests_file() {
    local TEMPLATE_PATH="$1"
    local MANIFESTS_FILE="$2"

    if [ -x "$(command -v envsubst)" ] && [ ! "$WITHOUT_ENVSUBST" ]; then
        echo "using local envsubst"
        envsubst < "$TEMPLATE_PATH" > "$MANIFESTS_FILE"
    elif [ -x "$(command -v docker)" ]; then
        echo "using envsubst in docker"
        # due to a bug in --env-file convert varaibles we care about to -e parameters 
        # The sed commands get only the env names before =, clean any white space, add -e to them, then make it all one line
        # https://github.com/moby/moby/issues/12997#issuecomment-307665540
        ENVS=`env | grep -E 'NAME|NAMESPACE|TLS|RBAC|TOLERATIONS|IMAGE|CA' | sed -n '/^[^\t]/s/=.*//p' | sed '/^$/d' | sed 's/^/-e /g' | tr '\n' ' '`

        # envsubst is installed in the nginx images which we already maintain
        docker run --rm -v "$TEMPLATE_PATH:$TEMPLATE_PATH" $ENVS registry.k8s.io/e2e-test-images/nginx:1.15-1 sh -c "cat $TEMPLATE_PATH | envsubst" > $MANIFESTS_FILE
    else
        fatal_error "Unable to run envsubst"
    fi
}

main() {
    local MANIFESTS_FILE=
    local NAME='gmsa-webhook'
    local NAMESPACE='gmsa-webhook'
    local IMAGE_NAME='registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook:v0.13.0'
    local CERTS_DIR='gmsa-webhook-certs'
    local DRY_RUN=false
    local OVERWRITE=false
    local TOLERATE_MASTER=false

    # parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --file)
                MANIFESTS_FILE="$2" && shift 2 ;;
            --name)
                NAME="$2" && shift 2 ;;
            --namespace)
                NAMESPACE="$2" && shift 2 ;;
            --image)
                IMAGE_NAME="$2" && shift 2 ;;
            --certs-dir)
                CERTS_DIR="$2" && shift 2 ;;
            --dry-run)
                DRY_RUN=true && shift ;;
            --overwrite)
                OVERWRITE=true && shift ;;
            --tolerate-master)
                TOLERATE_MASTER=true && shift ;;
            *)
                echo "Unknown option: $1"
                usage ;;
        esac
    done

    [ "$MANIFESTS_FILE" ] || usage

    # download the helper scripts if needed
    local HELPERS_SCRIPT
    HELPER_SCRIPT=$(ensure_helper_file_present '.helpers.sh')
    . "$HELPER_SCRIPT"
    local CREATE_SIGNED_CERT_SCRIPT
    CREATE_SIGNED_CERT_SCRIPT=$(ensure_helper_file_present 'create-signed-cert.sh')

    if [ -d "$CERTS_DIR" ]; then
        $OVERWRITE || warn "Certs dir $CERTS_DIR already exists"
    else
        mkdir -p "$CERTS_DIR"
    fi

    # create the SSL cert and apply it to the cluster
    local CREATE_CERT_CMD="$BASH $CREATE_SIGNED_CERT_SCRIPT --service $NAME --namespace $NAMESPACE --certs-dir $CERTS_DIR"
    $DRY_RUN && CREATE_CERT_CMD+=" --dry-run" || true
    $OVERWRITE && CREATE_CERT_CMD+=" --overwrite" || true
    eval "K8S_WINDOWS_GMSA_HELPER_SCRIPT='$HELPER_SCRIPT' $CREATE_CERT_CMD"

    # create the CRD
    local CRD_MANIFEST_PATH=$(ensure_helper_file_present 'gmsa-crd.yml')
    local CRD_MANIFEST_CONTENTS=$(cat "$CRD_MANIFEST_PATH")
    if ! $DRY_RUN && $KUBECTL get crd gmsacredentialspecs.windows.k8s.io &> /dev/null; then
        $KUBECTL delete crd gmsacredentialspecs.windows.k8s.io
    fi
    echo_or_run --with-kubectl-dry-run "$KUBECTL create -f - <<< '$CRD_MANIFEST_CONTENTS'"

    # then render the template for the rest of the resources
    local TEMPLATE_PATH
    TEMPLATE_PATH=$(ensure_helper_file_present 'gmsa-webhook.yml.tpl')

    # the TLS certificate might not have been generated yet if it's a dry run
    local TLS_CERTIFICATE
    if [ -r "$SERVER_CERT" ]; then
        TLS_CERTIFICATE=$(cat "$SERVER_CERT" | base64 -w 0)
    elif $DRY_RUN; then
        TLS_CERTIFICATE='TBD'
    else
        fatal_error "Expected to find the server certificate at $SERVER_CERT"
    fi

    TOLERATIONS=''
    if $TOLERATE_MASTER; then
        TOLERATIONS='
      tolerations:
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule'
    fi

    if [ -f "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt" ]; then
        info 'using pod based authentication'
        BUNDLE=$(cat /var/run/secrets/kubernetes.io/serviceaccount/ca.crt | base64 | tr -d '\n')
    else
        info 'using config file authentication'
        BUNDLE=$($KUBECTL config view --raw --minify --flatten -o jsonpath='{.clusters[].cluster.certificate-authority-data}')
    fi

    if [[ -z "$BUNDLE" ]]; then
        fatal_error "Not able to determine CA bundle for depoloyment"
    fi

    TLS_PRIVATE_KEY=$(cat "$SERVER_KEY" | base64 -w 0) \
        TLS_CERTIFICATE="$TLS_CERTIFICATE" \
        CA_BUNDLE="$BUNDLE" \
        RBAC_ROLE_NAME="$NAMESPACE-$NAME-rbac-role" \
        NAME="$NAME" \
        NAMESPACE="$NAMESPACE" \
        IMAGE_NAME="$IMAGE_NAME" \
        TOLERATIONS="$TOLERATIONS" \
        write_manifests_file "$TEMPLATE_PATH" "$MANIFESTS_FILE"

    echo_or_run --with-kubectl-dry-run "$KUBECTL apply -f $MANIFESTS_FILE"

    if ! $DRY_RUN; then
        verify_webhook_ready() {
            local READY
            if READY="$($KUBECTL -n "$NAMESPACE" get pod --selector=app=$NAME -o=jsonpath='{.items[0].status.containerStatuses[0].ready}' 2> /dev/null)"; then
                [[ "$READY" == 'true' ]]
            else
                return 1
            fi
        }
        wait_for verify_webhook_ready 'webhook not ready'

        info 'Windows GMSA Admission Webhook successfully deployed!'
        info "You can remove it by running $KUBECTL delete -f $MANIFESTS_FILE"
    fi

    # cleanup
    rm -rf "$TMP_DIR_PREFIX"*
}

main "$@"
```

## File: `admission-webhook/deploy/gmsa-crd.yml`
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: gmsacredentialspecs.windows.k8s.io
  annotations:
    "api-approved.kubernetes.io": "https://github.com/kubernetes/enhancements/tree/master/keps/sig-windows/689-windows-gmsa"
spec:
  group: windows.k8s.io
  versions:
  - name: v1alpha1
    served: true
    storage: false
    deprecated: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          credspec:
            description: GMSA Credential Spec
            type: object
            properties:
              ActiveDirectoryConfig:
                type: object
                properties:
                  GroupManagedServiceAccounts:
                    type: array
                    items:
                      type: object
                      properties:
                        Name:
                          type: string
                        Scope:
                          type: string
                  HostAccountConfig:
                    type: object
                    properties:
                      PluginGUID:
                        type: string
                      PluginInput:
                        type: string
                      PortableCcgVersion:
                        type: string
              CmsPlugins:
                type: array
                items:
                  type: string
              DomainJoinConfig:
                type: object
                properties:
                  DnsName:
                    type: string
                  DnsTreeName:
                    type: string
                  Guid:
                    type: string
                  MachineAccountName:
                    type: string
                  NetBiosName:
                    type: string
                  Sid:
                    type: string
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          credspec:
            description: GMSA Credential Spec
            type: object
            properties:
              ActiveDirectoryConfig:
                type: object
                properties:
                  GroupManagedServiceAccounts:
                    type: array
                    items:
                      type: object
                      properties:
                        Name:
                          type: string
                        Scope:
                          type: string
                  HostAccountConfig:
                    type: object
                    properties:
                      PluginGUID:
                        type: string
                      PluginInput:
                        type: string
                      PortableCcgVersion:
                        type: string
              CmsPlugins:
                type: array
                items:
                  type: string
              DomainJoinConfig:
                type: object
                properties:
                  DnsName:
                    type: string
                  DnsTreeName:
                    type: string
                  Guid:
                    type: string
                  MachineAccountName:
                    type: string
                  NetBiosName:
                    type: string
                  Sid:
                    type: string
  conversion:
    strategy: None
  names:
    kind: GMSACredentialSpec
    plural: gmsacredentialspecs
  scope: Cluster
```

## File: `admission-webhook/deploy/gmsa-webhook.yml.tpl`
```
## Template to deploy the GMSA webhook
## TODO: make this a helmchart instead?

apiVersion: v1
kind: Namespace
metadata:
  name: ${NAMESPACE}
  labels:
    gmsa-webhook: disabled

---

apiVersion: v1
kind: Secret
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
data:
  tls_private_key: ${TLS_PRIVATE_KEY}
  tls_certificate: ${TLS_CERTIFICATE}

---

# the service account for the webhook
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}

---

# the RBAC role that the webhook needs to:
#  * read GMSA custom resources
#  * check authorizations to use GMSA cred specs
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ${RBAC_ROLE_NAME}
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["get"]
- apiGroups: ["authorization.k8s.io"]
  resources: ["localsubjectaccessreviews"]
  verbs: ["create"]

---

# bind that role to the webhook's service account
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ${NAMESPACE}-${NAME}-binding-to-${RBAC_ROLE_NAME}
  namespace: ${NAMESPACE}
subjects:
- kind: ServiceAccount
  name: ${NAME}
  namespace: ${NAMESPACE}
roleRef:
  kind: ClusterRole
  name: ${RBAC_ROLE_NAME}
  apiGroup: rbac.authorization.k8s.io

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ${NAME}
  template:
    metadata:
      labels:
        app: ${NAME}
    spec:
      serviceAccountName: ${NAME}
      nodeSelector:
        kubernetes.io/os: linux${TOLERATIONS}
      containers:
      - name: ${NAME}
        image: ${IMAGE_NAME}
        imagePullPolicy: IfNotPresent
        readinessProbe:
          httpGet:
            scheme: HTTPS
            path: /health
            port: 443
        ports:
        - containerPort: 443
        volumeMounts:
          - name: tls
            mountPath: "/tls"
            readOnly: true
        env:
          - name: TLS_KEY
            value: /tls/key
          - name: TLS_CRT
            value: /tls/crt
      volumes:
      - name: tls
        secret:
          secretName: ${NAME}
          items:
          - key: tls_private_key
            path: key
          - key: tls_certificate
            path: crt

---

apiVersion: v1
kind: Service
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
spec:
  ports:
  - port: 443
    targetPort: 443
  selector:
    app: ${NAME}

---

apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: ${NAME}
webhooks:
- name: admission-webhook.windows-gmsa.sigs.k8s.io
  clientConfig:
    service:
      name: ${NAME}
      namespace: ${NAMESPACE}
      path: "/validate"
    caBundle: ${CA_BUNDLE}
  rules:
  - operations: ["CREATE", "UPDATE"]
    apiGroups: [""]
    apiVersions: ["*"]
    resources: ["pods"]
  failurePolicy: Fail
  admissionReviewVersions: ["v1", "v1beta1"]
  sideEffects: None
  # don't run on ${NAMESPACE}
  namespaceSelector:
    matchExpressions:
      - key: gmsa-webhook
        operator: NotIn
        values: [disabled]

---

apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: ${NAME}
webhooks:
- name: admission-webhook.windows-gmsa.sigs.k8s.io
  clientConfig:
    service:
      name: ${NAME}
      namespace: ${NAMESPACE}
      path: "/mutate"
    caBundle: ${CA_BUNDLE}
  rules:
  - operations: ["CREATE"]
    apiGroups: [""]
    apiVersions: ["*"]
    resources: ["pods"]
  failurePolicy: Fail
  admissionReviewVersions: ["v1", "v1beta1"]
  sideEffects: None
  # don't run on ${NAMESPACE}
  namespaceSelector:
    matchExpressions:
    - key: gmsa-webhook
      operator: NotIn
      values: [disabled]
```

## File: `admission-webhook/dockerfiles/Dockerfile`
```
## Dockerfile for release, as lightweight as possible

ARG ARCH
ARG GO_VERSION
ARG GOARCH

FROM --platform=linux/amd64 golang:${GO_VERSION} AS builder

WORKDIR /go/src/sigs.k8s.io/windows-gmsa/admission-webhook

# copy go dependencies
COPY go.mod ./go.mod
COPY go.sum ./go.sum

# build
COPY *.go ./
ARG VERSION
RUN go mod vendor && go mod tidy
RUN CGO_ENABLED=0 GOOS=linux GOARCH=${GOARCH} go build -ldflags="-w -s -X main.version=${VERSION}"

###

FROM --platform=linux/${ARCH} scratch

WORKDIR /admission-webhook

ENV LOG_LEVEL=info

COPY --from=builder /go/src/sigs.k8s.io/windows-gmsa/admission-webhook/admission-webhook .

ENTRYPOINT ["/admission-webhook/admission-webhook"]
```

## File: `admission-webhook/dockerfiles/Dockerfile.dev`
```
## Dockerfile for dev
## Differs from the release Dockerfile in that it allows re-compiling and re-starting
## the webserver from within the container

ARG GO_VERSION
FROM golang:$GO_VERSION

# we use runit so that we can stop the service without killing the container, and consequently
# play around with it
RUN apt-get update && apt-get install --yes runit
RUN mkdir /etc/service/webhook \
    && /bin/bash -c "echo -e '"'#!/bin/bash\nexec /go/src/sigs.k8s.io/windows-gmsa/admission-webhook/admission-webhook 2>&1\n'"' > /etc/service/webhook/run" \
    && chmod +x /etc/service/webhook/run
RUN ln -s /usr/bin/sv /etc/init.d/webhook

WORKDIR /go/src/sigs.k8s.io/windows-gmsa/admission-webhook

# copy go dependencies
COPY /vendor ./vendor

# build
COPY *.go ./
ARG VERSION
RUN go build -ldflags="-X main.version=${VERSION}"

# copy the rest
COPY . .

# let runit work its magic
CMD ["runsvdir", "/etc/service"]
```

## File: `admission-webhook/integration_tests/integration_test.go`
```go
package integrationtests

import (
	"context"
	"encoding/json"
	"fmt"
	"html/template"
	"io/ioutil"
	"os"
	"path"
	"reflect"
	"strconv"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime/schema"
)

const (
	// this is the JSON representation of the cred spec from templates/credspec-0.yml
	expectedCredSpec0 = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524075714-3094792973"}}`
	// this is the JSON representation of the cred spec from templates/credspec-1.yml
	expectedCredSpec1 = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication1","Scope":"CONTOSO"},{"Name":"WebApplication1","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication1","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524175714-3194792973"}}`
	// this is the JSON representation of the cred spec from templates/credspec-2.yml
	expectedCredSpec2 = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication2","Scope":"CONTOSO"},{"Name":"WebApplication2","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication2","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524275714-3294792973"}}`
	// this is the JSON representation of the cred spec from templates/credspec-with-hostagentconfig.yml
	expectedCredSpecWithHostAgentConfig = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication2","Scope":"CONTOSO"},{"Name":"WebApplication2","Scope":"contoso.com"}],"HostAccountConfig":{"PluginGUID":"{GDMA0342-266A-4D1P-831J-20990E82944F}","PluginInput":"contoso.com:gmsaccg:\u003cpassword\u003e","PortableCcgVersion":"1"}},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication2","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524275714-3294792973"}}`

	tmpRoot      = "tmp"
	ymlExtension = ".yml"
)

var (
	v1alpha1Resource = schema.GroupVersionResource{
		Group:    "windows.k8s.io",
		Version:  "v1alpha1",
		Resource: "gmsacredentialspecs",
	}

	v1Resource = schema.GroupVersionResource{
		Group:    "windows.k8s.io",
		Version:  "v1",
		Resource: "gmsacredentialspecs",
	}
)

func TestHappyPathWithPodLevelCredSpec(t *testing.T) {
	testName := "happy-path-with-pod-level-cred-spec"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpec0, extractPodCredSpecContents(t, pod))
}

func TestHappyPathWithContainerLevelCredSpec(t *testing.T) {
	testName := "happy-path-with-container-cred-spec"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-container-level-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, "nginx"))
}

func TestHappyPathWithSeveralContainers(t *testing.T) {
	testName := "happy-path-with-several-containers"
	credSpecTemplates := []string{"credspec-0", "credspec-1", "credspec-2"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "several-containers-with-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, "nginx0"))
	assert.Equal(t, expectedCredSpec1, extractPodCredSpecContents(t, pod))
	assert.Equal(t, expectedCredSpec2, extractContainerCredSpecContents(t, pod, "nginx2"))
}

func TestHappyPathWithPreSetMatchingContents(t *testing.T) {
	testName := "happy-path-with-pre-set-matching-contents"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-pre-set-matching-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	actualCredSpecContents := extractPodCredSpecContents(t, pod)
	assert.NotEqual(t, expectedCredSpec0, actualCredSpecContents)

	var (
		expectedCredSpec map[string]interface{}
		actualCredSpec   map[string]interface{}
	)
	if assert.Nil(t, json.Unmarshal([]byte(expectedCredSpec0), &expectedCredSpec)) &&
		assert.Nil(t, json.Unmarshal([]byte(actualCredSpecContents), &actualCredSpec)) {
		assert.True(t, reflect.DeepEqual(expectedCredSpec, actualCredSpec))
	}
}

func TestServiceAccountDoesNotHavePermissionsToUseCredSpec(t *testing.T) {
	testName := "sa-does-not-have-permissions-to-use-cred-spec"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "simple-with-container-level-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		expectedSubstr := fmt.Sprintf("service account %q is not authorized to `use` GMSA cred spec %q", testConfig.ServiceAccountName, testConfig.CredSpecNames[0])
		assert.Contains(t, condition.Message, expectedSubstr)
	}
}

func TestCredSpecDoesNotExist(t *testing.T) {
	testName := "cred-spec-does-not-exist"
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-unknown-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, nil, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		assert.Contains(t, condition.Message, "cred spec i-sure-dont-exist does not exist")
	}
}

func TestCannotPreSetGMSAPodLevelContentsWithoutName(t *testing.T) {
	testName := "cannot-pre-set-gmsa-pod-level-contents-without-name"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-preset-gmsa-pod-level-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		assert.Contains(t, condition.Message, "has a GMSA cred spec set, but does not define the name of the corresponding resource")
	}
}

func TestCannotPreSetGMSAContainerLevelContentsWithoutName(t *testing.T) {
	testName := "cannot-pre-set-gmsa-container-level-contents-without-name"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-preset-gmsa-container-level-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		assert.Contains(t, condition.Message, "has a GMSA cred spec set, but does not define the name of the corresponding resource")
	}
}

func TestCannotPreSetUnmatchingGMSASettings(t *testing.T) {
	testName := "cannot-pre-set-unmatching-gmsa-settings"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-pre-set-unmatching-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		expectedSubstr := fmt.Sprintf("does not match the contents of GMSA resource %q", testConfig.CredSpecNames[0])
		assert.Contains(t, condition.Message, expectedSubstr)
	}
}

func TestCannotUpdateExistingPodLevelGMSASettings(t *testing.T) {
	testName := "cannot-update-gmsa-pod-level-settings"
	credSpecTemplates := []string{"credspec-0"}
	singlePodTemplate := "single-pod-with-gmsa"
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", singlePodTemplate}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	// let's check that the pod has come up correctly, and has the correct GMSA cred inlined
	pod, err := kubeClient(t).CoreV1().Pods(testConfig.Namespace).Get(context.Background(), testName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, expectedCredSpec0, extractPodCredSpecContents(t, pod))

	// now let's try to update the cred spec's content
	testConfig.CredSpecContent = expectedCredSpec1
	defer func() { testConfig.CredSpecContent = "" }()
	renderedTemplate := renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ := applyManifest(t, renderedTemplate)
	assert.False(t, success)

	// and same for its name
	testConfig.CredSpecNames[0] = "new-credspec"
	renderedTemplate = renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ = applyManifest(t, renderedTemplate)
	assert.False(t, success)
}

func TestCannotUpdateExistingContainerLevelGMSASettings(t *testing.T) {
	testName := "cannot-update-gmsa-container-level-settings"
	credSpecTemplates := []string{"credspec-0"}
	singlePodTemplate := "single-pod-with-container-level-gmsa"
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", singlePodTemplate}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	// let's check that the pod has come up correctly, and has the correct GMSA cred inlined
	pod, err := kubeClient(t).CoreV1().Pods(testConfig.Namespace).Get(context.Background(), testName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, testName))

	// now let's try to update the cred spec's content
	testConfig.CredSpecContent = expectedCredSpec1
	defer func() { testConfig.CredSpecContent = "" }()
	renderedTemplate := renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ := applyManifest(t, renderedTemplate)
	assert.False(t, success)

	// and same for its name
	testConfig.CredSpecNames[0] = "new-credspec"
	renderedTemplate = renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ = applyManifest(t, renderedTemplate)
	assert.False(t, success)
}

func TestHappyPathWithHostAgentConfigInCredSpec(t *testing.T) {
	testName := "happy-path-with-pod-level-cred-spec"
	credSpecTemplates := []string{"credspec-with-hostagentconfig"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpecWithHostAgentConfig, extractPodCredSpecContents(t, pod))
}

func TestPossibleToUpdatePodWithExistingGMSASettings(t *testing.T) {
	testName := "possible-to-update-pod-with-existing-gmsa-settings"
	credSpecTemplates := []string{"credspec-0", "credspec-1"}
	singlePodTemplate := "single-pod-with-gmsa"
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", singlePodTemplate}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	// let's check that the pod has come up correctly, and has the correct GMSA cred inlined
	pod, err := kubeClient(t).CoreV1().Pods(testConfig.Namespace).Get(context.Background(), testName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, expectedCredSpec0, extractPodCredSpecContents(t, pod))

	// now let's update this pod
	testConfig.Image = "nginx"
	defer func() { testConfig.Image = "" }()
	renderedTemplate := renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ := applyManifest(t, renderedTemplate)
	assert.True(t, success)
}

func TestDeployV1Alpha1CredSpecGetAllVersions(t *testing.T) {
	testName := "deploy-v1alpha1-credspec-get-all-versions"
	credSpecTemplates := []string{"credspec-0", "credspec-1"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, nil)
	defer tearDownFunc()

	// ensure CredSpec specified v1 CRD
	templatePath := renderTemplate(t, testConfig, "credspec-1")
	b, err := ioutil.ReadFile(templatePath)
	if err != nil {
		t.Fatal(err)
	}
	s := string(b)
	assert.Contains(t, s, "apiVersion: windows.k8s.io/v1alpha1\n")

	client := dynamicClient(t)
	resourceName := "deploy-v1alpha1-credspec-get-all-versions-cred-spec-1"
	v1alpha1CredSpec, err := client.Resource(v1alpha1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	v1CredSpec, err := client.Resource(v1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	assert.Equal(t, v1alpha1CredSpec.Object["credSpec"], v1CredSpec.Object["credSpec"])
}

func TestDeployV1CredSpecGetAllVersions(t *testing.T) {
	testName := "deploy-v1-credspec-get-all-versions"
	credSpecTemplates := []string{"credspec-0", "credspec-1"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, nil)
	defer tearDownFunc()

	// ensure CredSpec specified v1 CRD
	templatePath := renderTemplate(t, testConfig, "credspec-0")
	b, err := ioutil.ReadFile(templatePath)
	if err != nil {
		t.Fatal(err)
	}
	s := string(b)
	assert.Contains(t, s, "apiVersion: windows.k8s.io/v1\n")

	client := dynamicClient(t)
	resourceName := "deploy-v1-credspec-get-all-versions-cred-spec-0"
	v1alpha1CredSpec, err := client.Resource(v1alpha1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	v1CredSpec, err := client.Resource(v1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	assert.Equal(t, v1alpha1CredSpec.Object["credSpec"], v1CredSpec.Object["credSpec"])
}

func TestPossibleToUpdatePodWithNewCert(t *testing.T) {
	/** TODO:
	 * - add a separate test to verify that requests to the webhook always return during this process
	 */

	webHookNs := os.Getenv("NAMESPACE")
	webHookDeploymentName := os.Getenv("DEPLOYMENT_NAME")
	webhook, err := kubeClient(t).AppsV1().Deployments(webHookNs).Get(context.Background(), webHookDeploymentName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	rotationEnabled := false
	for arg := range webhook.Spec.Template.Spec.Containers[0].Args {
		if strings.Contains(webhook.Spec.Template.Spec.Containers[0].Args[arg], "--cert-reload=true") {
			rotationEnabled = true
		}
	}

	if !rotationEnabled {
		t.Skip("Skipping test as rotation is not enabled")
	}

	testName := "possible-to-update-pod-with-new-cert"
	credSpecTemplates := []string{"credspec-0"}

	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "single-pod-with-container-level-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, testName))

	deployMethod := os.Getenv("DEPLOY_METHOD")
	if deployMethod == "chart" {
		runCommandOrFail(t, "cmctl", "renew", webHookDeploymentName, "-n", webHookNs)

		var (
			timeout = 30 * time.Second
			start   = time.Now()
		)

		for {
			success, stdout, stderr := runKubectlCommand(t, "get", "certificaterequest", webHookNs+"-2", "--namespace", webHookNs, "-o", "jsonpath='{.status.conditions[?(@.type==\"Ready\")].status}'")
			if !success {
				fmt.Printf("Warning: command failed with %s, %s\n", stdout, stderr)
				continue
			}

			if stdout == "'True'" {
				break
			} else {
				fmt.Printf("Warning: status was %s", stdout)
			}

			if time.Since(start) >= timeout {
				t.Fatal("Timeout: Unable to get the certificate request status")
			}

			time.Sleep(1 * time.Second)
		}
	} else {
		/** TODO:
		     * - get a blessed certificate from the API server
			 *   (https://github.com/kubernetes-sigs/windows-gmsa/blob/141/admission-webhook/deploy/create-signed-cert.sh)
			 *   runCommandOrFail(t, fmt."create-signed-cert.sh --service $NAME --namespace $NAMESPACE --certs-dir $CERTS_DIR", testConfig.Namespace)
		     * - update existing secret in place and wait for the pod to get new secrets which can take time
			 *   (https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod) - similar to what you are doing here
		     * - kubectl exec into the running pod to see that the secret changed
			 *   (using utils like https://github.com/ycheng-kareo/windows-gmsa/blob/watch-reload-cert/admission-webhook/integration_tests/kube.go#L199)
		**/

		t.Skip("Non chart deployment method not supported for this test")
	}

	// it takes ~60 seconds for the webhook to pick up the new certificate
	// so this first run makes sure the old cert still works
	testName2 := testName + "after-rotation"
	testConfig2, tearDownFunc2 := integrationTestSetup(t, testName2, credSpecTemplates, templates)
	defer tearDownFunc2()

	pod2 := waitForPodToComeUp(t, testConfig2.Namespace, "app="+testName2)
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod2, testName2))

	// sleep a bit to ensure the the secret has been propagated to the pod
	time.Sleep(90 * time.Second)

	testName3 := testName + "after-rotation-propagated"
	testConfig3, tearDownFunc3 := integrationTestSetup(t, testName3, credSpecTemplates, templates)
	defer tearDownFunc3()

	pod3 := waitForPodToComeUp(t, testConfig3.Namespace, "app="+testName3)
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod3, testName3))
}

func TestPossibleHostnameRandomization(t *testing.T) {
	deployMethod := os.Getenv("DEPLOY_METHOD")
	if deployMethod != "chart" {
		t.Skip("Non chart deployment method not supported for this test")
	}

	webHookNs := os.Getenv("NAMESPACE")
	webHookDeploymentName := os.Getenv("DEPLOYMENT_NAME")
	webhook, err := kubeClient(t).AppsV1().Deployments(webHookNs).Get(context.Background(), webHookDeploymentName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	randomHostnameEnabled := false
	for _, envVar := range webhook.Spec.Template.Spec.Containers[0].Env {
		if strings.EqualFold(envVar.Name, "RANDOM_HOSTNAME") && strings.EqualFold(envVar.Value, "true") {
			randomHostnameEnabled = true
		}
	}

	if randomHostnameEnabled {
		testName1 := "happy-path-with-hostname-randomization"
		credSpecTemplates1 := []string{"credspec-0"}
		templates1 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

		testConfig1, tearDownFunc1 := integrationTestSetup(t, testName1, credSpecTemplates1, templates1)
		defer tearDownFunc1()

		pod := waitForPodToComeUp(t, testConfig1.Namespace, "app="+testName1)
		assert.NotEqual(t, testName1, pod.Spec.Hostname)
		assert.Equal(t, 15, len(pod.Spec.Hostname))

		testName2 := "hostnameset-no-hostname-randomization"
		credSpecTemplates2 := []string{"credspec-0"}
		templates2 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa-hostname"}

		testConfig2, tearDownFunc2 := integrationTestSetup(t, testName2, credSpecTemplates2, templates2)
		defer tearDownFunc2()

		pod = waitForPodToComeUp(t, testConfig2.Namespace, "app="+testName2)
		assert.Equal(t, testName2, pod.Spec.Hostname)

		testName3 := "nogmsa-hostname-randomization"
		credSpecTemplates3 := []string{"credspec-0"}
		templates3 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-without-gmsa"}

		testConfig3, tearDownFunc3 := integrationTestSetup(t, testName3, credSpecTemplates3, templates3)
		defer tearDownFunc3()
		pod = waitForPodToComeUp(t, testConfig3.Namespace, "app="+testName3)

		assert.Equal(t, "", pod.Spec.Hostname)
	} else {
		testName4 := "notenabled-hostname-randomization"
		credSpecTemplates4 := []string{"credspec-0"}
		templates4 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

		testConfig4, tearDownFunc4 := integrationTestSetup(t, testName4, credSpecTemplates4, templates4)
		defer tearDownFunc4()
		pod := waitForPodToComeUp(t, testConfig4.Namespace, "app="+testName4)

		assert.Equal(t, "", pod.Spec.Hostname)
	}
}

/* Helpers */

type testConfig struct {
	TestName           string
	Namespace          string
	TmpDir             string
	CredSpecNames      []string
	CredSpecContent    string
	ClusterRoleName    string
	ServiceAccountName string
	RoleBindingName    string
	Image              string
	ExtraSpecLines     []string
	Cert               string
	Key                string
}

// integrationTestSetup creates a new namespace to play in, and returns a function to
// tear it down afterwards.
// It also applies the given templates
func integrationTestSetup(t *testing.T, name string, credSpecTemplates, templates []string) (*testConfig, func()) {
	if _, err := os.Stat(tmpRoot); os.IsNotExist(err) {
		if err = os.Mkdir(tmpRoot, os.ModePerm); err != nil {
			t.Fatal(err)
		}
	}
	tmpDir, err := ioutil.TempDir(tmpRoot, name+"-")
	if err != nil {
		t.Fatal(err)
	}

	namespace := createNamespace(t, "")

	credSpecNames := make([]string, len(credSpecTemplates))
	for i := range credSpecTemplates {
		credSpecNames[i] = name + "-cred-spec-" + strconv.Itoa(i)
	}

	testConfig := &testConfig{
		TestName:  name,
		Namespace: namespace,
		TmpDir:    tmpDir,

		CredSpecNames:      credSpecNames,
		ClusterRoleName:    name + "-credspecs-users",
		ServiceAccountName: name + "-service-account",
		RoleBindingName:    name + "-use-credspecs",
	}

	if needMasterToleration(t) {
		testConfig.ExtraSpecLines = append(testConfig.ExtraSpecLines, masterToleration...)
	}

	templatePaths := make([]string, len(credSpecTemplates)+len(templates))
	for i, template := range append(credSpecTemplates, templates...) {
		templatePaths[i] = renderTemplate(t, testConfig, template)
		applyManifestOrFail(t, templatePaths[i])
	}

	tearDownFunc := func() {
		// helps speed us test when working locally against a throw-away cluster
		// deleting namespaces seems to be a rather heavy operation
		if _, present := os.LookupEnv("K8S_GMSA_ADMISSION_WEBHOOK_INTEGRATION_TEST_SKIP_CLEANUP"); present {
			return
		}

		for _, templatePath := range templatePaths {
			deleteManifest(t, templatePath)
		}

		deleteNamespace(t, namespace)
		if err := os.RemoveAll(tmpDir); err != nil {
			t.Fatal(err)
		}
	}

	return testConfig, tearDownFunc
}

var masterToleration = []string{
	"tolerations:",
	"- key: node-role.kubernetes.io/master",
	"  operator: Exists",
	"  effect: NoSchedule",
}

var allNodesHaveMasterTaint *bool

// needMasterToleration returns true iff all of the cluster's nodes have the master taint.
// Caches that in allNodesHaveMasterTaint.
// Not thread-safe.
func needMasterToleration(t *testing.T) bool {
	if allNodesHaveMasterTaint == nil {
		allMaster := true
		for _, node := range getNodes(t) {
			if !nodeHasMasterTaint(node) {
				allMaster = false
				break
			}
		}
		allNodesHaveMasterTaint = &allMaster
	}
	return *allNodesHaveMasterTaint
}

// renderTemplate renders a template, and returns its path.
func renderTemplate(t *testing.T, testConfig *testConfig, name string) string {
	if name[len(name)-len(ymlExtension):] != ymlExtension {
		name += ymlExtension
	}

	contents, err := ioutil.ReadFile(path.Join("templates", name))
	if err != nil {
		t.Fatal(err)
	}

	tplName := fmt.Sprintf("%s-%s", testConfig.Namespace, name)
	tpl, err := template.New(tplName).Parse(string(contents))
	if err != nil {
		t.Fatal(err)
	}

	renderedTemplate, err := os.Create(path.Join(testConfig.TmpDir, name))
	if err != nil {
		t.Fatal(err)
	}
	defer renderedTemplate.Close()

	if err = tpl.Execute(renderedTemplate, *testConfig); err != nil {
		t.Fatal(err)
	}

	return renderedTemplate.Name()
}

func extractPodCredSpecContents(t *testing.T, pod *corev1.Pod) string {
	if pod.Spec.SecurityContext == nil ||
		pod.Spec.SecurityContext.WindowsOptions == nil ||
		pod.Spec.SecurityContext.WindowsOptions.GMSACredentialSpec == nil {
		t.Fatalf("No pod cred spec")
	}
	return *pod.Spec.SecurityContext.WindowsOptions.GMSACredentialSpec
}

func extractContainerCredSpecContents(t *testing.T, pod *corev1.Pod, containerName string) string {
	for _, container := range pod.Spec.Containers {
		if container.Name == containerName {
			if container.SecurityContext == nil ||
				container.SecurityContext.WindowsOptions == nil ||
				container.SecurityContext.WindowsOptions.GMSACredentialSpec == nil {
				t.Fatalf("No cred spec for container %q", containerName)
			}
			return *container.SecurityContext.WindowsOptions.GMSACredentialSpec
		}
	}

	t.Fatalf("Did not find any container named %q", containerName)
	panic("won't happen, but required by the compiler")
}
```

## File: `admission-webhook/integration_tests/kube.go`
```go
package integrationtests

import (
	"context"
	"fmt"
	"os"
	"testing"

	"github.com/mitchellh/go-homedir"
	"github.com/stretchr/testify/require"
	"gotest.tools/poll"
	appsv1 "k8s.io/api/apps/v1"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/dynamic"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
	"k8s.io/client-go/tools/clientcmd"
)

func clientConfig(t *testing.T) *rest.Config {
	kubeConfigPath, err := homedir.Expand(kubeconfig())
	if err != nil {
		t.Fatal(err)
	}
	config, err := clientcmd.BuildConfigFromFlags("", kubeConfigPath)
	if err != nil {
		t.Fatal(err)
	}

	return config
}

func kubeClient(t *testing.T) kubernetes.Interface {
	config := clientConfig(t)
	client, err := kubernetes.NewForConfig(config)
	if err != nil {
		t.Fatal(err)
	}

	return client
}

func dynamicClient(t *testing.T) dynamic.Interface {
	config := clientConfig(t)
	client, err := dynamic.NewForConfig(config)
	if err != nil {
		t.Fatal(err)
	}

	return client
}

// getNodes returns the nodes present in the cluster.
func getNodes(t *testing.T) []corev1.Node {
	client := kubeClient(t)

	nodeList, err := client.CoreV1().Nodes().List(context.Background(), metav1.ListOptions{})
	require.Nil(t, err, "Unable to list nodes")
	return nodeList.Items
}

// nodeHasMasterTaint returns true iff node has the canonical master taint.
func nodeHasMasterTaint(node corev1.Node) bool {
	for _, taint := range node.Spec.Taints {
		if taint.Key == "node-role.kubernetes.io/master" && taint.Effect == "NoSchedule" {
			return true
		}
	}
	return false
}

// waitForPodToComeUp waits for a pod matching `selector` to come up in `namespace`, and returns it.
func waitForPodToComeUp(t *testing.T, namespace, selector string, pollOps ...poll.SettingOp) *corev1.Pod {
	fetcher := func(client kubernetes.Interface, listOptions metav1.ListOptions) ([]interface{}, error) {
		podList, err := client.CoreV1().Pods(namespace).List(context.Background(), listOptions)
		if err == nil {
			result := make([]interface{}, len(podList.Items))
			for i, item := range podList.Items {
				result[i] = item
			}
			return result, nil
		}
		return nil, err
	}

	rawPod := waitForKubeObject(t, fetcher, namespace, selector, "pod", pollOps...)
	pod := rawPod.(corev1.Pod)
	return &pod
}

// waitForReplicaSet waits for a replica set matching `selector` to come up in `namespace`, and returns it.
func waitForReplicaSet(t *testing.T, namespace, selector string, pollOps ...poll.SettingOp) *appsv1.ReplicaSet {
	fetcher := func(client kubernetes.Interface, listOptions metav1.ListOptions) ([]interface{}, error) {
		rsList, err := client.AppsV1().ReplicaSets(namespace).List(context.Background(), listOptions)
		if err == nil {
			result := make([]interface{}, len(rsList.Items))
			for i, item := range rsList.Items {
				result[i] = item
			}
			return result, nil
		}
		return nil, err
	}

	rawReplicaSet := waitForKubeObject(t, fetcher, namespace, selector, "replica set", pollOps...)
	replicaSet := rawReplicaSet.(appsv1.ReplicaSet)
	return &replicaSet
}

// waitForReplicaSetGen1 waits for a given replica set to have its `Status.ObservedGeneration` field grow to > 0
// Comes in handy to wait for k8s to reach a decision for a given replicaset
func waitForReplicaSetGen1(t *testing.T, namespace, selector string, pollOps ...poll.SettingOp) *appsv1.ReplicaSet {
	replicaSet := waitForReplicaSet(t, namespace, selector, pollOps...)
	var err error

	client := kubeClient(t)

	pollingFunc := func(_ poll.LogT) poll.Result {
		replicaSet, err = client.AppsV1().ReplicaSets(namespace).Get(context.Background(), replicaSet.Name, metav1.GetOptions{})
		if err != nil {
			return poll.Error(err)
		}

		if replicaSet.Status.ObservedGeneration == 0 {
			return poll.Continue("replicaset %s is still at generation 0", replicaSet.Name)
		}
		return poll.Success()
	}

	poll.WaitOn(t, pollingFunc, pollOps...)

	return replicaSet
}

// waitForKubeObject waits for fetcher to return a list of one object matching `selector` in `namespace`, and returns it.
func waitForKubeObject(t *testing.T, fetcher func(kubernetes.Interface, metav1.ListOptions) ([]interface{}, error), namespace, selector, displayableName string, pollOps ...poll.SettingOp) (object interface{}) {
	client := kubeClient(t)
	listOptions := metav1.ListOptions{LabelSelector: selector}

	pollingFunc := func(_ poll.LogT) poll.Result {
		list, err := fetcher(client, listOptions)

		if err != nil {
			return poll.Error(err)
		}

		switch len(list) {
		case 0:
			return poll.Continue("no %s matching %s in namespace %s", displayableName, selector, namespace)
		case 1:
			object = list[0]
			return poll.Success()
		default:
			err = fmt.Errorf("expected no more than 1 %s matching %s in namespace %s, got %v", displayableName, selector, namespace, len(list))
			return poll.Error(err)
		}
	}

	poll.WaitOn(t, pollingFunc, pollOps...)

	return
}

const testNamespacePrefix = "gmsa-webhook-test-"

// value from https://github.com/kubernetes/kubernetes/blob/5e58841cce77d4bc13713ad2b91fa0d961e69192/pkg/volume/util/attach_limit.go#L53-L54
// removed so we didn't need to import the entire kubernetes source which is technically not supported
const resourceNameLengthLimit = 63

// createNamespace creates a new namespace, and fails the test if it already exists.
// if passed an empty string, it picks a random name and returns it.
func createNamespace(t *testing.T, name string) string {
	if name == "" {
		name = testNamespacePrefix + randomHexString(t, resourceNameLengthLimit-len(testNamespacePrefix))
	}

	runKubectlCommandOrFail(t, "create", "namespace", name)

	return name
}

func deleteNamespace(t *testing.T, name string) {
	runKubectlCommandOrFail(t, "delete", "namespace", name)
}

func applyManifestOrFail(t *testing.T, path string) {
	runKubectlCommandOrFail(t, "apply", "-f", path)
}

func applyManifest(t *testing.T, path string) (success bool, stdout string, stderr string) {
	return runKubectlCommand(t, "apply", "-f", path)
}

func deleteManifest(t *testing.T, path string) {
	runKubectlCommandOrFail(t, "delete", "-f", path)
}

func runKubectlCommandOrFail(t *testing.T, args ...string) {
	runCommandOrFail(t, kubectl(), args...)
}

func runKubectlCommand(t *testing.T, args ...string) (success bool, stdout string, stderr string) {
	return runCommand(t, kubectl(), args...)
}

func kubectl() string {
	return fromEnv("KUBECTL", "kubectl")
}

func kubeconfig() string {
	return fromEnv("KUBECONFIG", "~/.kube/config")
}

func fromEnv(key, defaultValue string) (value string) {
	if fromEnv, present := os.LookupEnv(key); present && fromEnv != "" {
		value = fromEnv
	} else {
		value = defaultValue
	}
	return
}
```

## File: `admission-webhook/integration_tests/utils.go`
```go
package integrationtests

import (
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"os/exec"
	"testing"
)

func runCommandOrFail(t *testing.T, name string, args ...string) {
	success, stdout, stderr := runCommand(t, name, args...)
	if !success {
		t.Fatal(stdout, stderr)
	}
	fmt.Print(stdout)
}

func runCommand(t *testing.T, name string, args ...string) (success bool, stdout string, stderr string) {
	cmd := exec.Command(name, args...)
	stdoutReader, err := cmd.StdoutPipe()
	if err != nil {
		t.Fatal(err)
	}
	stderrReader, err := cmd.StderrPipe()
	if err != nil {
		t.Fatal(err)
	}

	success = true
	if err := cmd.Start(); err != nil {
		t.Fatal(err)
	}

	stdoutBytes, err := ioutil.ReadAll(stdoutReader)
	if err != nil {
		t.Fatal(err)
	}
	stderrBytes, err := ioutil.ReadAll(stderrReader)
	if err != nil {
		t.Fatal(err)
	}

	if err := cmd.Wait(); err != nil {
		if _, ok := err.(*exec.ExitError); ok {
			success = false
		} else {
			t.Fatal(err)
		}
	}

	return success, string(stdoutBytes), string(stderrBytes)
}

func randomHexString(t *testing.T, length int) string {
	b := length / 2
	randBytes := make([]byte, b)

	if n, err := rand.Reader.Read(randBytes); err != nil || n != b {
		if err == nil {
			err = fmt.Errorf("only got %v random bytes, expected %v", n, b)
		}
		t.Fatal(err)
	}

	return hex.EncodeToString(randBytes)
}
```

## File: `admission-webhook/integration_tests/templates/all-credspecs-users-rbac-role.yml`
```yaml
# an RBAC role to grant `use` access to all credspecs

kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .ClusterRoleName }}
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["use"]
```

## File: `admission-webhook/integration_tests/templates/credspec-0.yml`
```yaml
# a sample cred spec

apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 0 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication0
      Scope: CONTOSO
    - Name: WebApplication0
      Scope: contoso.com
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication0
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524075714-3094792973
```

## File: `admission-webhook/integration_tests/templates/credspec-1.yml`
```yaml
# a sample cred spec
# Note: The apiVersion of this GMSACredentialSpec was intentionally left at windows.k8s.io/v1alpha1
#   to provide validation for scenarios where users deploy v1alpha CRD objects to their cluster after
#   updating the CRD definition to use windows.k8s.io/v1 as the storage version.

apiVersion: windows.k8s.io/v1alpha1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 1 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication1
      Scope: CONTOSO
    - Name: WebApplication1
      Scope: contoso.com
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication1
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524175714-3194792973
```

## File: `admission-webhook/integration_tests/templates/credspec-2.yml`
```yaml
# a sample cred spec

apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 2 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication2
      Scope: CONTOSO
    - Name: WebApplication2
      Scope: contoso.com
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication2
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524275714-3294792973
```

## File: `admission-webhook/integration_tests/templates/credspec-with-hostagentconfig.yml`
```yaml
# a sample cred spec

apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 0 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication2
      Scope: CONTOSO
    - Name: WebApplication2
      Scope: contoso.com
    HostAccountConfig:
      PluginGUID: "{GDMA0342-266A-4D1P-831J-20990E82944F}"
      PluginInput: "contoso.com:gmsaccg:<password>"
      PortableCcgVersion: "1"
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication2
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524275714-3294792973
```

## File: `admission-webhook/integration_tests/templates/credspecs-users-rbac-role.yml`
```yaml
# an RBAC role to grant `use` access to some credspecs

kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .ClusterRoleName }}
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["use"]
  resourceNames:
{{- range $_, $csn := .CredSpecNames }}
    - {{ $csn }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/new-secret.yml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
data:
  tls_private_key: {{ .Key }}
  tls_certificate: {{ .Cert }}
```

## File: `admission-webhook/integration_tests/templates/sa-rbac-binding.yml`
```yaml
## an RBAC role binding for a service account

kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .RoleBindingName }}
  namespace: {{ .Namespace }}
subjects:
- kind: ServiceAccount
  name: {{ .ServiceAccountName }}
  namespace: {{ .Namespace }}
roleRef:
  kind: ClusterRole
  name: {{ .ClusterRoleName }}
  apiGroup: rbac.authorization.k8s.io
```

## File: `admission-webhook/integration_tests/templates/service-account.yml`
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ .ServiceAccountName }}
  namespace: {{ .Namespace }}
```

## File: `admission-webhook/integration_tests/templates/several-containers-with-gmsa.yml`
```yaml
## a simple deployment with several containers: 2 with their own GMSA, and 1 without it, plus a pod-level cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 1 }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx0
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
      - image: registry.k8s.io/pause
        name: nginx1
      - image: registry.k8s.io/pause
        name: nginx2
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: {{ index .CredSpecNames 2 }}
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-container-level-gmsa.yml`
```yaml
## a simple deployment with a container-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-gmsa-hostname.yml`
```yaml
## a simple deployment with a pod-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      hostname: {{ .TestName }}
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-gmsa.yml`
```yaml
## a simple deployment with a pod-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-pre-set-matching-contents.yml`
```yaml
## a simple deployment with a fully specified GMSA cred spec (ie both its name and contents)

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
          gmsaCredentialSpec: '{"CmsPlugins":["ActiveDirectory"],  "ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"DomainJoinConfig":{"Sid":"S-1-5-21-2126729477-2524075714-3094792973",  "DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO"}}'
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-pre-set-unmatching-contents.yml`
```yaml
## a simple deployment with a fully specified GMSA cred spec (ie both its name and contents);
## but where the specified contents don't match the name

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
          gmsaCredentialSpec: '{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication1","Scope":"CONTOSO"},{"Name":"WebApplication1","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication1","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524175714-3194792973"}}'
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-preset-gmsa-container-level-contents.yml`
```yaml
## a simple deployment with a container-level cred spec GMSA's *contents* already set (and not its name)

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
        securityContext:
          windowsOptions:
            gmsaCredentialSpec: '{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524075714-3094792973"}}'
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-preset-gmsa-pod-level-contents.yml`
```yaml
## a simple deployment with a pod-level cred spec GMSA's *contents* already set (and not its name)

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpec: '{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524075714-3094792973"}}'
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-with-unknown-gmsa.yml`
```yaml
## a simple deployment trying to use a pod-level GMSA cred spec that doesn't exist

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: i-sure-dont-exist
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/simple-without-gmsa.yml`
```yaml
## a simple deployment with a pod-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/single-pod-with-container-level-gmsa.yml`
```yaml
## this deploys a single pod with a container-level GMSA cred spec

apiVersion: v1
kind: Pod
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  serviceAccountName: {{ .ServiceAccountName }}
  containers:
  - name: {{ .TestName }}
    image: registry.k8s.io/pause
    securityContext:
      windowsOptions:
        gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
{{- if .CredSpecContent }}
        gmsaCredentialSpec: '{{ .CredSpecContent }}'
{{- end }}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
{{- range $line := .ExtraSpecLines }}
  {{ $line }}
{{- end }}
```

## File: `admission-webhook/integration_tests/templates/single-pod-with-gmsa.yml`
```yaml
## this deploys a single pod with a pod-level GMSA cred spec

apiVersion: v1
kind: Pod
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  serviceAccountName: {{ .ServiceAccountName }}
  securityContext:
    windowsOptions:
      gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
{{- if .CredSpecContent }}
      gmsaCredentialSpec: '{{ .CredSpecContent }}'
{{- end }}
  containers:
  - name: nginx
{{- if .Image }}
    image: {{ .Image }}
{{- else }}
    image: registry.k8s.io/pause
{{- end }}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
{{- range $line := .ExtraSpecLines }}
  {{ $line }}
{{- end }}
```

## File: `admission-webhook/make/deps.mk`
```
.PHONY: deps_install
deps_install:
	go mod vendor

.PHONY: deps_update
deps_update:
	go mod tidy

.PHONY: deps_clean
deps_clean:
	rm -rf ./vendor
```

## File: `admission-webhook/make/dev_cluster.mk`
```
# K8S version can be overriden
# see available versions at https://hub.docker.com/r/kindest/node/tags
KUBERNETES_VERSION ?= 1.29.0
# see https://github.com/kubernetes-sigs/kind/releases
KIND_VERSION = 0.22.0
# https://github.com/helm/helm/releases
HELM_VERSION ?= 3.14.3
# https://github.com/cert-manager/cert-manager/releases
CERT_MANAGER_VERSION ?= v1.14.4

CLUSTER_NAME ?= windows-gmsa-dev
DEPLOYMENT_NAME ?= windows-gmsa-dev
NAMESPACE ?= windows-gmsa-dev
NUM_NODES ?= 1

DEV_DIR = $(WEBHOOK_ROOT)/dev

CERTS_DIR = $(DEV_DIR)/certs_dir
MANIFESTS_FILE = $(DEV_DIR)/gmsa-webhook.yml

KIND = $(DEV_DIR)/kind-$(KIND_VERSION)
KIND_URL = https://github.com/kubernetes-sigs/kind/releases/download/v$(KIND_VERSION)/kind-$(UNAME)-amd64

KUBECTL = $(shell which kubectl 2> /dev/null)
KUBECTL_URL = https://dl.k8s.io/release/v$(KUBERNETES_VERSION)/bin/$(UNAME)/amd64/kubectl

ifeq ($(KUBECTL),)
KUBECTL = $(DEV_DIR)/kubectl-$(KUBERNETES_VERSION)
endif

KUBECONFIG?="$(HOME)/.kube/kind-config-$(CLUSTER_NAME)"

# starts a new kind cluster (see https://github.com/kubernetes-sigs/kind)
.PHONY: cluster_start
cluster_start: $(KIND) $(KUBECTL)
	./make/start_cluster.sh --name '$(CLUSTER_NAME)' --num-nodes $(NUM_NODES) --version $(KUBERNETES_VERSION) --kind-bin "$(KIND)"
	@ echo '### Kubectl version: ###'
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) version
	# coredns has a thing for creating API resources continually, which confuses the dry-run test
	# since it's not needed for anything here, there's no reason to keep it around
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) delete -n kube-system deployment.apps/coredns || true
	# kind removes the taint on master when NUM_NODES is 0 - but we do want to test that case too!
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) taint node $(CLUSTER_NAME)-control-plane 'node-role.kubernetes.io/master=true:NoSchedule' --overwrite
	#@ echo -e 'Cluster started, KUBECONFIG available at $(KUBECONFIG), eg\nexport KUBECONFIG=$(KUBECONFIG)'
	#@ $(MAKE) cluster_symlinks

# removes the kind cluster
.PHONY: cluster_clean
cluster_clean: $(KIND) clean_certs
	$(KIND) delete cluster --name '$(CLUSTER_NAME)'
	# also clean up any left over ci clusters from act
	$(KIND) delete cluster --name 'windows-gmsa-deploy-method-download'
	$(KIND) delete cluster --name 'windows-gmsa-dry-run-deploy'
	$(KIND) delete cluster --name 'windows-gmsa-integration'
	$(KIND) delete cluster --name 'windows-gmsa-tolerate-control-plane'

.PHONY: clean_certs
clean_certs:
	rm -rf $(CERTS_DIR)

# deploys the webhook to the kind cluster with the dev image
.PHONY: deploy_dev_webhook
deploy_dev_webhook:
	K8S_GMSA_IMAGE=$(DEV_IMAGE_NAME) $(MAKE) _deploy_webhook

# deploys the webhook to the kind cluster with the release image
.PHONY: deploy_webhook
deploy_webhook:
	K8S_GMSA_IMAGE=$(WEBHOOK_IMG):$(TAG) $(MAKE) _deploy_webhook

# removes the webhook from the kind cluster
.PHONY: remove_webhook
remove_webhook:
ifeq ($(wildcard $(MANIFESTS_FILE)),)
	@ echo "No manifests file found at $(MANIFESTS_FILE), nothing to remove"
else
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) delete -f $(MANIFESTS_FILE) || true
endif

# cluster_symlinks symlinks kubectl to dev/kubectl, and the kube config to dev/kubeconfig (used in ci)
.PHONY:
cluster_symlinks:
	ln -sfv $(KUBECTL) $(DEV_DIR)/kubectl-$(CLUSTER_NAME)
	ln -sfv $(KUBECONFIG) $(DEV_DIR)/kubeconfig-$(CLUSTER_NAME)

### "Private" targets below ###

# starts the kind cluster only if it's not already running
.PHONY: _start_cluster_if_not_running
_start_cluster_if_not_running: $(KUBECTL) $(KIND)
	$(MAKE) cluster_start

# deploys the webhook to the kind cluster
# if $K8S_GMSA_DEPLOY_METHOD is set to "download", then it will deploy by downloading
# the deploy script as documented in the README, using $K8S_GMSA_DEPLOY_DOWNLOAD_REPO and
# $K8S_GMSA_DEPLOY_DOWNLOAD_REV env variables to build the download URL. If REV is not set the current
# HEAD's SHA is used.
.PHONY: _deploy_webhook
_deploy_webhook: _copy_image remove_webhook
ifeq ($(K8S_GMSA_IMAGE),)
	@ echo "Cannot call target $@ without setting K8S_GMSA_IMAGE"
	exit 1
endif
	mkdir -p $(dir $(MANIFESTS_FILE))
ifeq ($(K8S_GMSA_DEPLOY_METHOD),download)
	@if [ ! "$$K8S_GMSA_DEPLOY_DOWNLOAD_REPO" ]; then K8S_GMSA_DEPLOY_DOWNLOAD_REPO="kubernetes-sigs/windows-gmsa"; fi \
      && if [ ! "$$K8S_GMSA_DEPLOY_DOWNLOAD_REV" ]; then K8S_GMSA_DEPLOY_DOWNLOAD_REV="$$(git rev-parse HEAD)"; fi \
      && CMD="curl -sL 'https://raw.githubusercontent.com/$$K8S_GMSA_DEPLOY_DOWNLOAD_REPO/$$K8S_GMSA_DEPLOY_DOWNLOAD_REV/admission-webhook/deploy/deploy-gmsa-webhook.sh' | K8S_GMSA_DEPLOY_DOWNLOAD_REPO='$$K8S_GMSA_DEPLOY_DOWNLOAD_REPO' K8S_GMSA_DEPLOY_DOWNLOAD_REV='$$K8S_GMSA_DEPLOY_DOWNLOAD_REV' KUBECONFIG=$(KUBECONFIG) KUBECTL=$(KUBECTL) bash -s -- --file '$(MANIFESTS_FILE)' --name '$(DEPLOYMENT_NAME)' --namespace '$(NAMESPACE)' --image '$(K8S_GMSA_IMAGE)' --certs-dir '$(CERTS_DIR)' $(EXTRA_GMSA_DEPLOY_ARGS)" \
      && echo "$$CMD" && eval "$$CMD"
else
	KUBECONFIG=$(KUBECONFIG) KUBECTL=$(KUBECTL) ./deploy/deploy-gmsa-webhook.sh --file "$(MANIFESTS_FILE)" --name "$(DEPLOYMENT_NAME)" --namespace "$(NAMESPACE)" --image "$(K8S_GMSA_IMAGE)" --certs-dir "$(CERTS_DIR)" $(EXTRA_GMSA_DEPLOY_ARGS)
endif

# copies the image to the kind cluster
.PHONY: _copy_image
_copy_image: _start_cluster_if_not_running
ifeq ($(K8S_GMSA_IMAGE),)
	@ echo "Cannot call target $@ without setting K8S_GMSA_IMAGE"
	exit 1
endif
	$(KIND) load docker-image $(K8S_GMSA_IMAGE) --name '$(CLUSTER_NAME)'

$(KIND):
	mkdir -vp "$$(dirname $(KIND))"
ifeq ($(WGET),)
	$(CURL) -L $(KIND_URL) > $(KIND)
else
	$(WGET) -O $(KIND) $(KIND_URL)
endif
	chmod +x $(KIND)

$(KUBECTL):
	mkdir -vp "$$(dirname $(KUBECTL))"
ifeq ($(WGET),)
	$(CURL) -L $(KUBECTL_URL) > $(KUBECTL)
else
	$(WGET) -O $(KUBECTL) $(KUBECTL_URL)
endif
	chmod +x $(KUBECTL)
```

## File: `admission-webhook/make/helm.mk`
```
HELM = $(shell which helm 2> /dev/null)
HELM_URL = https://get.helm.sh/helm-v$(HELM_VERSION)-$(UNAME)-amd64.tar.gz

ifeq ($(HELM),)
HELM = $(DEV_DIR)/HELM-$(HELM_VERSION)
endif

.PHONY: install-helm
install-helm:
	curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

.PHONY: install-cmctl
install-cmctl:
	go install github.com/cert-manager/cmctl/v2@latest

.PHONY: helm-chart
helm-chart:
	$(HELM) package ../charts/gmsa -d ../charts/repo/

.PHONY: helm-index
helm-index:
	$(HELM) repo index ../charts/repo

.PHONY: helm-lint
helm-lint:
	$(HELM) lint ../charts/gmsa

# deploys the chart to the kind cluster with the release image
.PHONY: deploy_chart
deploy_chart: install-helm
	K8S_GMSA_IMAGE=$(WEBHOOK_IMG) $(MAKE) _deploy_chart

# removes the chart from the kind cluster
.PHONY: remove_chart
remove_chart:
	KUBECONFIG=$(KUBECONFIG) $(HELM) uninstall $(DEPLOYMENT_NAME) --namespace $(NAMESPACE)

# deploys the webhook to the kind cluster using helm
# if $K8S_GMSA_DEPLOY_METHOD is set to "download", then it will deploy by downloading
# the deploy script as documented in the README, using $K8S_GMSA_DEPLOY_CHART_REPO and
# $K8S_GMSA_DEPLOY_CHART_VERSION env variables to build the download URL. If VERSION is
# not set then latest is used.
# the HELM_INSTALL_FLAGS_FLAGS env var can be set to eg run only specific tests, e.g.:
# HELM_INSTALL_FLAGS_FLAGS='--set certificates.certReload.enabled=true' make deploy_chart
.PHONY: _deploy_chart
_deploy_chart:  _copy_image _deploy_certmanager install-cmctl
ifeq ($(K8S_GMSA_CHART),)
	@ echo "Cannot call target $@ without setting K8S_GMSA_CHART"
	exit 1
endif
	@ echo "installing helm deployment $(DEPLOYMENT_NAME) with chart $(K8S_GMSA_CHART) and image $(K8S_GMSA_IMAGE):$(TAG)"
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) create namespace $(NAMESPACE)
	KUBECONFIG=$(KUBECONFIG) $(HELM) version
	KUBECONFIG=$(KUBECONFIG) $(HELM) install $(DEPLOYMENT_NAME) $(K8S_GMSA_CHART) --set image.repository=$(K8S_GMSA_IMAGE) --set image.tag=$(TAG) --namespace $(NAMESPACE) $(HELM_INSTALL_FLAGS_FLAGS)
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) wait -n $(NAMESPACE) pod -l app=$(DEPLOYMENT_NAME) --for=condition=Ready

.PHONY: _deploy_certmanager
_deploy_certmanager: remove_certmanager
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) create namespace cert-manager
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) apply -f https://github.com/cert-manager/cert-manager/releases/download/$(CERT_MANAGER_VERSION)/cert-manager.yaml
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) wait -n cert-manager pod -l app=cainjector --for=condition=Ready
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) wait -n cert-manager pod -l app=webhook --for=condition=Ready
	
.PHONY: remove_certmanager
remove_certmanager:
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) delete namespace cert-manager || true
```

## File: `admission-webhook/make/image.mk`
```
# must stay consistent with the go version defined in .travis.yml
GO_VERSION = 1.23
BUILD_ARGS = --build-arg GO_VERSION=$(GO_VERSION) --build-arg VERSION=$(TAG) 
DOCKER_BUILD = docker build . $(BUILD_ARGS)

AMD64_ARGS = --build-arg GOARCH=amd64 --build-arg ARCH=amd64 --platform=linux/amd64
ARM64_ARGS = --build-arg GOARCH=arm64 --build-arg ARCH=arm64 --platform=linux/arm64
BUILDX_BUILD = docker buildx build . $(BUILD_ARGS) --provenance=false --sbom=false


.PHONY: image_build_dev
image_build_dev:
	$(DOCKER_BUILD) -f dockerfiles/Dockerfile.dev -t $(DEV_IMAGE_NAME)

.PHONY: create_buildx_builder
create_buildx_builder:
	docker buildx create --name img-builder --platform linux/amd64 --use

.PHONY: remove_image_builder
remove_image_builder:
	docker buildx rm img-builder || true

# Builds an amd64 image and loads it into the local image store - used during integration tests
image_build: remove_image_builder create_buildx_builder image_build_int remove_image_builder

.PHONY: image_build_int
image_build_int:
	$(BUILDX_BUILD) --load $(AMD64_ARGS) -f dockerfiles/Dockerfile -t $(WEBHOOK_IMG):$(TAG) -t $(WEBHOOK_IMG):latest

# Builds and pushes a multi-arch image (amd64 and arm64) to a remote registry
image_build_and_push: remove_image_builder create_buildx_builder image_build_and_push_int remove_image_builder

.PHONY: image_build_and_push_int
image_build_and_push_int:
	$(BUILDX_BUILD) --push $(AMD64_ARGS) -f dockerfiles/Dockerfile -t $(WEBHOOK_IMG):$(TAG)-amd64 -t $(WEBHOOK_IMG):latest-amd64
	$(BUILDX_BUILD) --push $(ARM64_ARGS) -f dockerfiles/Dockerfile -t $(WEBHOOK_IMG):$(TAG)-arm64 -t $(WEBHOOK_IMG):latest-arm64
	docker manifest create --amend $(WEBHOOK_IMG):$(TAG) $(WEBHOOK_IMG):$(TAG)-amd64 $(WEBHOOK_IMG):$(TAG)-arm64
	docker manifest push --purge $(WEBHOOK_IMG):$(TAG)
	docker manifest create --amend $(WEBHOOK_IMG):latest $(WEBHOOK_IMG):latest-amd64 $(WEBHOOK_IMG):latest-arm64
	docker manifest push --purge $(WEBHOOK_IMG):latest
```

## File: `admission-webhook/make/start_cluster.sh`
```bash
#!/usr/bin/env bash

set -e

usage() {
    cat <<EOF
Light wrapper around kind that generates the right configuration file for kind, then starts the cluster.

usage: $0 --name NAME --num-nodes NUM_NODES --version VERSION [--kind-bin KIND_BIN]

NAME is the kind cluster name.
NUM_NODES is the number of worker nodes.
VERSION is the k8s version to use.
KIND_BIN is the path to the kind executable.
EOF
    exit 1
}

setkubeconfig() {
    mkdir -p ~/.kube
    $KIND_BIN get kubeconfig --name "$NAME" >  ~/.kube/kind-config-$NAME
}

main() {
    local NAME=
    local NUM_NODES=
    local VERSION=
    local KIND_BIN=kind

    # parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --name)
                NAME="$2" ;;
            --num-nodes)
                NUM_NODES="$2" ;;
            --version)
                VERSION="$2" ;;
            --kind-bin)
                KIND_BIN="$2" ;;
            *)
                echo "Unknown option: $1"
                usage ;;
        esac
        shift 2
    done

    [ "$NAME" ] && [ "$NUM_NODES" ] && [ "$VERSION" ] || usage

    if [[ "$(${KIND_BIN} get clusters)" == *"${NAME}"* ]]; then
  	  echo "Dev cluster already running. Skipping cluster creation"
      setkubeconfig
  	  exit 0
  	else
  	  echo "Starting new cluster";
  	fi

    local CONFIG_FILE
    CONFIG_FILE="$(mktemp /tmp/gmsa-webhook-kind-config.XXXXXXX)"

    # generate the config file
    cat <<EOF > "$CONFIG_FILE"
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
kubeadmConfigPatches:
- |
  apiVersion: kubeadm.k8s.io/v1beta2
  kind: ClusterConfiguration
  metadata:
    name: config
  apiServer:
    extraArgs:
      enable-admission-plugins: NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook
EOF
    cat <<EOF >> "$CONFIG_FILE"
nodes:
- role: control-plane
EOF
    for _ in $(seq "$NUM_NODES"); do
        echo -e '- role: worker' >> "$CONFIG_FILE"
    done

    # run kind
    local EXIT_STATUS=0
    $KIND_BIN create cluster --name "$NAME" --config "$CONFIG_FILE" --image "kindest/node:v$VERSION" --wait 240s || EXIT_STATUS=$?
    setkubeconfig

    # clean up the config file
    rm -f "$CONFIG_FILE"

    return $EXIT_STATUS
}

main "$@"
```

## File: `charts/README.md`
```markdown
# Install Windows GMSA with Helm 3

## Prerequisites

- [install Helm](https://helm.sh/docs/intro/quickstart/#install-helm)

### Tips

### install a specific version

```console
helm repo add windows-gmsa https://raw.githubusercontent.com/kubernetes-sigs/windows-gmsa/master/charts/repo
helm install windows-gmsa/gmsa --namespace kube-system --version v0.4.4
```

### search for all available chart versions

```console
helm search repo -l gmsa
```

## uninstall Windows GMSA

```console
helm uninstall gmsa -n kube-system
```

## latest chart configuration

The following table lists the configurable parameters of the latest GMSA chart and default values.

| Parameter                                          | Description                                                           | Default                                         |
| -------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------- |
| `certificates.certManager.enabled`                 | enable cert manager integration                                       | `true`                                          |
| `certificates.certManager.version`                 | version of cert manager                                               |                                                 |
| `certificates.caBundle`                            | cert-manager disabled, add self-signed ca.crt in base64 format        |                                                 |
| `certificates.secretName`                          | cert-manager disabled, upload certs data as k8s secretName            | `gmsa-server-cert`                              |
| `certificates.certReload.enabled`                  | enable cert reload on changes                                         | `false`                                         |
| `credential.enabled`                               | enable creation of GMSA Credential                                    | `true`                                          |
| `credential.domainJoinConfig.dnsName`              | DNS Domain Name                                                       |                                                 |
| `credential.domainJoinConfig.dnsTreeName`          | DNS Domain Name Root                                                  |                                                 |
| `credential.domainJoinConfig.guid`                 | GUID                                                                  |                                                 |
| `credential.domainJoinConfig.machineAccountName`   | username of the GMSA account                                          |                                                 |
| `credential.domainJoinConfig.netBiosName`          | NETBIOS Domain Name                                                   |                                                 |
| `credential.domainJoinConfig.sid`                  | SID                                                                   |                                                 |
| `credential.hostAccountConfig.pluginGUID`          | GUID of CCG Plugin                                                    |                                                 |
| `credential.hostAccountConfigg.portableCcgVersion` | Version of CCG Plugin                                                 | `1`                                             |
| `credential.hostAccountConfig.pluginInput`         | Input to CCG Plugin                                                   |                                                 |
| `image.repository`                                 | image repository                                                      | `registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook` |
| `image.tag`                                        | image tag                                                             | `v0.4.0`                                        |
| `image.imagePullPolicy`                            | image pull policy                                                     | `IfNotPresent`                                  |
| `global.systemDefaultRegistry`                     | container registry                                                    |                                                 |
| `tolerations`                                      | tolerations                                                           | []                                              |
| `setPodOs`                                         | Enables setting of `OS` field on Pod for supported K8s versions       | `true`                                          |
| `viewerRole`                                       | Enable aggregation of `gmsacredentialspecs` to the built-in view role | `false`                                         |

## troubleshooting

- Add `--wait -v=5 --debug` in `helm install` command to get detailed error
- Use `kubectl describe` to acquire more info
```

## File: `charts/gmsa/Chart.yaml`
```yaml
apiVersion: v2
appVersion: 0.13.0
description: Windows GMSA Configuration
keywords:
- Windows
- Windows GMSA
- GMSA
- Active Directory
name: gmsa
sources:
- https://github.com/kubernetes-sigs/windows-gmsa
type: application
version: 0.13.0
```

## File: `charts/gmsa/app-readme.md`
```markdown
# Windows GMSA Admission Webhook

This chart creates the GMSA CRD, Credential, and Admission Webhook. The official documentation and tutorials can be found [here](https://github.com/kubernetes-sigs/windows-gmsa).

## Prerequisites

- Active Directory that supports Group Managed Service Accounts
- A Group Managed Service Account
- Kubernetes v1.23+
```

## File: `charts/gmsa/values.yaml`
```yaml
certificates:
  certManager:
    # Enable cert manager integration. Cert manager should be already installed at the k8s cluster
    enabled: true
    version: "v1.16.2"
  # If cert-manager integration is disabled, add self-signed ca.crt in base64 format
  caBundle: ""
  # If cert-manager integration is disabled, upload certs data (ca.crt, tls.crt and tls.key) as k8s secretName in the namespace
  secretName: gmsa-server-cert
  certReload:
    # Enable cert reload when the certs change
    enabled: false

credential:
  enabled: false
  hostAccountConfig: {}
    # pluginGUID: "" # CCG Plugin GUID
    # portableCcgVersion: "1" # This needs to equal the current version of CCG which right now is '1'
    # pluginInput: "" # Format of this field is dependent upon specific CCG Plugin
  domainJoinConfig:
    dnsName: "" # DNS Domain Name
    dnsTreeName: "" # DNS Domain Name Root
    guid: "" # GUID of Domain
    machineAccountName: "" # Username of the GMSA account
    netBiosName: "" # NETBIOS Domain Name
    sid: "" # SID of Domain

containerPort: "443"

image:
  repository: registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook
  tag: v0.13.0
  imagePullPolicy: IfNotPresent

# If true, will add os fields to pod specs for K8s versions where feature is in beta (v1.24+)
setPodOs: true

global:
  systemDefaultRegistry: ""

affinity: {}
nodeSelector: {}
podDisruptionBudget:
  enabled: false
  # minAvailable: 1
  # maxUnavailable: 1

podSecurityContext: {}

# Enable aggregation of GMSA resources to the built-in view role
viewerRole: false

replicaCount: 2
securityContext: {}
tolerations: []
qps: 30.0
burst: 50
randomHostname: false
```

## File: `charts/gmsa/crds/crds.yaml`
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: gmsacredentialspecs.windows.k8s.io
  annotations:
    "api-approved.kubernetes.io": "https://github.com/kubernetes/enhancements/tree/master/keps/sig-windows/689-windows-gmsa"
spec:
  group: windows.k8s.io
  versions:
    - name: v1alpha1
      served: true
      storage: false
      deprecated: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            credspec:
              description: GMSA Credential Spec
              type: object
              properties:
                ActiveDirectoryConfig:
                  type: object
                  properties:
                    GroupManagedServiceAccounts:
                      type: array
                      items:
                        type: object
                        properties:
                          Name:
                            type: string
                          Scope:
                            type: string
                    HostAccountConfig:
                      type: object
                      properties:
                        PluginGUID:
                          type: string
                        PluginInput:
                          type: string
                        PortableCcgVersion:
                          type: string
                CmsPlugins:
                  type: array
                  items:
                    type: string
                DomainJoinConfig:
                  type: object
                  properties:
                    DnsName:
                      type: string
                    DnsTreeName:
                      type: string
                    Guid:
                      type: string
                    MachineAccountName:
                      type: string
                    NetBiosName:
                      type: string
                    Sid:
                      type: string
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            credspec:
              description: GMSA Credential Spec
              type: object
              properties:
                ActiveDirectoryConfig:
                  type: object
                  properties:
                    GroupManagedServiceAccounts:
                      type: array
                      items:
                        type: object
                        properties:
                          Name:
                            type: string
                          Scope:
                            type: string
                    HostAccountConfig:
                      type: object
                      properties:
                        PluginGUID:
                          type: string
                        PluginInput:
                          type: string
                        PortableCcgVersion:
                          type: string
                CmsPlugins:
                  type: array
                  items:
                    type: string
                DomainJoinConfig:
                  type: object
                  properties:
                    DnsName:
                      type: string
                    DnsTreeName:
                      type: string
                    Guid:
                      type: string
                    MachineAccountName:
                      type: string
                    NetBiosName:
                      type: string
                    Sid:
                      type: string
  conversion:
    strategy: None
  names:
    kind: GMSACredentialSpec
    plural: gmsacredentialspecs
  scope: Cluster

```

## File: `charts/gmsa/templates/_helpers.tpl`
```
{{- define "system_default_registry" -}}
{{- if .Values.global.systemDefaultRegistry -}}
{{- printf "%s/" .Values.global.systemDefaultRegistry -}}
{{- end -}}
{{- end -}}

{{/* Create chart name and version as used by the chart label. */}}
{{- define "gmsa.chartref" -}}
chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
{{- end }}

{{/* Determine apiVersion for cert-manager */}}
{{- define "cert-manager.apiversion" -}}
  {{- $certmanagerVer :=  split "." .Values.certificates.certManager.version -}}
  {{- if or (.Capabilities.APIVersions.Has "cert-manager.io/v1") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 1) (ge (int $certmanagerVer._1) 0)) }}
apiVersion: cert-manager.io/v1
  {{- else if or (.Capabilities.APIVersions.Has "cert-manager.io/v1beta1") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 0) (ge (int $certmanagerVer._1) 16)) }}
apiVersion: cert-manager.io/v1beta1
  {{- else if or (.Capabilities.APIVersions.Has "cert-manager.io/v1alpha2") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 0) (ge (int $certmanagerVer._1) 11)) }}
apiVersion: cert-manager.io/v1alpha2
  {{- else if or (.Capabilities.APIVersions.Has "certmanager.k8s.io/v1alpha1") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 0) (lt (int $certmanagerVer._1) 11)) }}
apiVersion: cert-manager.io/v1alpha1
  {{- else }}
apiVersion: cert-manager.io/v1
  {{- end }}
{{- end }}

{{- define "certificates.cabundle"}}
{{- if .Values.certificates.caBundle }}
{{- .Values.certificates.caBundle }}
{{- else if gt (len (lookup "rbac.authorization.k8s.io/v1" "ClusterRole" "" "")) 0 -}}
{{- $secret := (lookup "v1" "Secret" .Release.Namespace .Values.certificates.secretName) -}}
{{- if lt (len $secret) 1 -}}
{{- required (printf "CA Bundle secret '%s' in namespace '%s' must exist" .Values.certificates.secretName .Release.Namespace) "" -}}
{{- else -}}
{{- if not (hasKey $secret "data") -}}
{{- required (printf "CA Bundle secret '%s' in namespace '%s' is empty" .Values.certificates.secretName .Release.Namespace) "" -}}
{{- end -}}
{{- if or (not (hasKey $secret.data "ca.crt")) (not (hasKey $secret.data "tls.crt")) (not (hasKey $secret.data "tls.key")) -}}
{{- required (printf "CA Bundle secret '%s' in namespace '%s' must contain ca.crt, tls.key, and tls.cert; found the following keys in the secret: %s" .Values.certificates.secretName .Release.Namespace $secret.data) "" -}}
{{- end -}}
{{- end -}}
{{- get $secret.data "ca.crt" }}
{{- else -}}
INSERT_CERTIFICATE_FROM_SECRET
{{- end -}}
{{- end }}
```

## File: `charts/gmsa/templates/clusterrole.yaml`
```yaml
# the RBAC role that the webhook needs to:
#  * read GMSA custom resources
#  * check authorizations to use GMSA cred specs
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .Release.Name }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
rules:
  - apiGroups: ["windows.k8s.io"]
    resources: ["gmsacredentialspecs"]
    verbs: ["get", "use"]
  - apiGroups: ["authorization.k8s.io"]
    resources: ["localsubjectaccessreviews"]
    verbs: ["create"]
---
{{- if .Values.viewerRole }}
# allow visibility of gmsacredentialspecs through built-in "view" role
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .Release.Name }}-viewer-role
  labels:
    {{ include "gmsa.chartref" . }}
    rbac.authorization.k8s.io/aggregate-to-view: "true"
rules:
  - apiGroups: ["windows.k8s.io"]
    resources: ["gmsacredentialspecs"]
    verbs: ["get", "list", "watch"]
{{- end }}
```

## File: `charts/gmsa/templates/clusterrolebinding.yaml`
```yaml
# bind that role to the webhook's service account
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .Release.Name }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
subjects:
  - kind: ServiceAccount
    name: {{ .Release.Name }}
    namespace: {{ .Release.Namespace }}
roleRef:
  kind: ClusterRole
  name: {{ .Release.Name }}
  apiGroup: rbac.authorization.k8s.io
```

## File: `charts/gmsa/templates/credentialspec.yaml`
```yaml
{{- if .Values.credential.enabled -}}
apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ lower .Values.credential.domainJoinConfig.machineAccountName | replace "_" "-" }}  #This is an arbitrary name but it will be used as a reference
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
      - Name: {{ .Values.credential.domainJoinConfig.machineAccountName }} # Username of the GMSA account
        Scope: {{ .Values.credential.domainJoinConfig.netBiosName }} # NETBIOS Domain Name
      - Name: {{ .Values.credential.domainJoinConfig.machineAccountName }} # Username of the GMSA account
        Scope: {{ .Values.credential.domainJoinConfig.dnsName }} # DNS Domain Name
{{- if .Values.credential.hostAccountConfig }}
    HostAccountConfig:
      PortableCcgVersion: {{ required "credential.hostAccountConfig.portableCCGVersion must be provided if credential.hostAccountConfig is set" .Values.credential.hostAccountConfig.portableCcgVersion | quote }} # This needs to equal the current version of CCG which right now is '1'
      PluginGUID:   {{ printf "{%s}" (required "credential.hostAccountConfig.pluginGUID must be provided if credential.hostAccountConfig is set" .Values.credential.hostAccountConfig.pluginGUID) | quote }} # CCG Plugin GUID
      PluginInput: {{ required "credential.hostAccountConfig.pluginInput must be provided if credential.hostAccountConfig is set" .Values.credential.hostAccountConfig.pluginInput | quote }} # Format of this field is dependent upon specific CCG Plugin
{{- end }}
  CmsPlugins:
    - ActiveDirectory
  DomainJoinConfig:
    DnsName: {{ .Values.credential.domainJoinConfig.dnsName }} # DNS Domain Name
    DnsTreeName:  {{ .Values.credential.domainJoinConfig.dnsTreeName }} # DNS Domain Name Root
    Guid:  {{ .Values.credential.domainJoinConfig.guid }} # GUID of Domain
    MachineAccountName:  {{ .Values.credential.domainJoinConfig.machineAccountName }} # Username of the GMSA account
    NetBiosName:  {{ .Values.credential.domainJoinConfig.netBiosName }} # NETBIOS Domain Name
    Sid:  {{ .Values.credential.domainJoinConfig.sid }} # SID of Domain
{{- end -}}
```

## File: `charts/gmsa/templates/deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      {{- if .Values.podSecurityContext }}
      securityContext: {{ toYaml .Values.podSecurityContext | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ .Release.Name }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      nodeSelector:
        kubernetes.io/os: linux
      {{- with .Values.nodeSelector }}
        {{- toYaml . | nindent 8 }}
      {{- end }}
      containers:
        - name: {{ .Release.Name }}
          image: '{{ template "system_default_registry" . }}{{ .Values.image.repository }}:{{ .Values.image.tag }}'
          imagePullPolicy: {{ .Values.image.imagePullPolicy }}
          readinessProbe:
            httpGet:
              scheme: HTTPS
              path: /health
              port: {{ .Values.containerPort }}
          ports:
            - containerPort: {{ .Values.containerPort }}
          volumeMounts:
            - name: tls
              mountPath: "/tls"
              readOnly: true
          env:
            - name: TLS_KEY
              value: /tls/key
            - name: TLS_CRT
              value: /tls/crt
            - name: HTTPS_PORT
              value: "{{ .Values.containerPort }}"
            - name: BURST
              value: "{{ .Values.burst }}"
            - name: QPS
              value: "{{ .Values.qps }}"
            - name: RANDOM_HOSTNAME
              value: "{{ .Values.randomHostname }}"
          {{- if .Values.securityContext }}
          securityContext: {{ toYaml .Values.securityContext | nindent 12 }}
          {{- end }}
          args:
            - --cert-reload={{ .Values.certificates.certReload.enabled }}
      volumes:
        - name: tls
          secret:
            secretName: {{ .Values.certificates.secretName }}
            items:
              - key: tls.key
                path: key
              - key: tls.crt
                path: crt
      {{- if and (.Values.setPodOs) (ge .Capabilities.KubeVersion.Minor "24")}}
      os:
        name: linux
      {{- end -}}
```

## File: `charts/gmsa/templates/issuer.yaml`
```yaml
{{- if .Values.certificates.certManager.enabled -}}
{{ template "cert-manager.apiversion" . }}
kind: Certificate
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  dnsNames:
    - {{ .Release.Name }}.{{ .Release.Namespace }}.svc
    - {{ .Release.Name }}.{{ .Release.Namespace }}.svc.cluster.local
  issuerRef:
    kind: Issuer
    name: {{ .Release.Name }}
  secretName: {{ .Values.certificates.secretName }}
  {{- if .Values.certificates.certReload.enabled }}
  privateKey:
    rotationPolicy: Always
  {{- end }}
---
{{ template "cert-manager.apiversion" . }}
kind: Issuer
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  ca:
    secretName: {{ .Release.Name }}-root-ca
---
{{ template "cert-manager.apiversion" . }}
kind: ClusterIssuer
metadata:
  name: {{ .Release.Name }}-ca
spec:
  selfSigned: {}
---
{{ template "cert-manager.apiversion" . }}
kind: Certificate
metadata:
  name: {{ .Release.Name }}-ca
  namespace: {{ .Release.Namespace }}
spec:
  isCA: true
  commonName: {{ .Release.Name }}-ca
  secretName: {{ .Release.Name }}-root-ca
  issuerRef:
    name: {{ .Release.Name }}-ca
    kind: ClusterIssuer
    group: cert-manager.io
---
{{- end -}}
```

## File: `charts/gmsa/templates/mutatingwebhook.yaml`
```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: {{ .Release.Name }}
  {{- if .Values.certificates.certManager.enabled }}
  annotations:
    cert-manager.io/inject-ca-from: {{ .Release.Namespace }}/{{ .Release.Name }}-ca
  {{- end }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
webhooks:
  - name: admission-webhook.windows-gmsa.sigs.k8s.io
    clientConfig:
      service:
        name: {{ .Release.Name }}
        namespace: {{.Release.Namespace}}
        path: "/mutate"
      {{- if not (.Values.certificates.certManager.enabled) }}
      caBundle: {{ template "certificates.cabundle" . }}
      {{- end }}
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["*"]
        resources: ["pods"]
    failurePolicy: Fail
    admissionReviewVersions: ["v1", "v1beta1"]
    sideEffects: None
    # don't run on ${NAMESPACE}
    namespaceSelector:
      matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values: [{{ .Release.Namespace }}]
        - key: windows.k8s.io/disabled
          operator: NotIn
          values: ["true"]
```

## File: `charts/gmsa/templates/pdb.yaml`
```yaml
{{- if .Values.podDisruptionBudget.enabled }}
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels:  {{ include "gmsa.chartref" . | nindent 4 }}
spec:
{{- if .Values.podDisruptionBudget.minAvailable }}
  minAvailable: {{ .Values.podDisruptionBudget.minAvailable }}
{{- end }}
{{- if .Values.podDisruptionBudget.maxUnavailable }}
  maxUnavailable: {{ .Values.podDisruptionBudget.maxUnavailable }}
{{- end }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
{{- end }}
```

## File: `charts/gmsa/templates/service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  ports:
    - port: 443
      targetPort: {{ .Values.containerPort }}
  selector:
    app: {{ .Release.Name }}
```

## File: `charts/gmsa/templates/serviceaccount.yaml`
```yaml
# the service account for the webhook
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
```

## File: `charts/gmsa/templates/validatingwebhook.yaml`
```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: {{ .Release.Name }}
  {{- if .Values.certificates.certManager.enabled }}
  annotations:
    cert-manager.io/inject-ca-from: {{ .Release.Namespace }}/{{ .Release.Name }}-ca
  {{- end }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
webhooks:
  - name: admission-webhook.windows-gmsa.sigs.k8s.io
    clientConfig:
      service:
        name: {{ .Release.Name }}
        namespace: {{ .Release.Namespace }}
        path: "/validate"
      {{- if not (.Values.certificates.certManager.enabled) }}
      caBundle: {{ template "certificates.cabundle" . }}
      {{- end }}
    rules:
      - operations: ["CREATE", "UPDATE"]
        apiGroups: [""]
        apiVersions: ["*"]
        resources: ["pods"]
    failurePolicy: Fail
    admissionReviewVersions: ["v1", "v1beta1"]
    sideEffects: None
    # don't run on ${NAMESPACE}
    namespaceSelector:
      matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values: [{{ .Release.Namespace }}]
        - key: windows.k8s.io/disabled
          operator: NotIn
          values: ["true"]
```

## File: `charts/repo/index.yaml`
```yaml
apiVersion: v1
entries:
  gmsa:
  - apiVersion: v2
    appVersion: 0.13.0
    created: "2025-03-14T19:52:28.477888534Z"
    description: Windows GMSA Configuration
    digest: d129b67f17b0d634a86a3573b760b518006bce53f56d677db4009049a51323bc
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.13.0.tgz
    version: 0.13.0
  - apiVersion: v2
    appVersion: 0.12.1
    created: "2025-03-14T19:52:28.47506763Z"
    description: Windows GMSA Configuration
    digest: bfc10d609983b41154f10fdbf3e4aed7ecd8b0ea48a4595ae5482db408787003
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.12.1.tgz
    version: 0.12.1
  - apiVersion: v2
    appVersion: 0.12.0
    created: "2025-03-14T19:52:28.472641525Z"
    description: Windows GMSA Configuration
    digest: b941f044d359dd4dfe7f5f9820e7f1243d5c43189e30eb28c9ebb570fa271d0d
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.12.0.tgz
    version: 0.12.0
  - apiVersion: v2
    appVersion: 0.11.0
    created: "2025-03-14T19:52:28.470961223Z"
    description: Windows GMSA Configuration
    digest: 46ab09c040c6aa5c908d9bfa30974e7dfd49a79cb69a55299b25cfa19d32465a
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.11.0.tgz
    version: 0.11.0
  - apiVersion: v2
    appVersion: 0.10.0
    created: "2025-03-14T19:52:28.46934612Z"
    description: Windows GMSA Configuration
    digest: 0d05c3750b9178124329d75dde218633557df594a69d60498abc38b138b45b1b
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.10.0.tgz
    version: 0.10.0
  - apiVersion: v2
    appVersion: 0.9.0
    created: "2025-03-14T19:52:28.486489549Z"
    description: Windows GMSA Configuration
    digest: f1757c9d665f98c18f81cb17a7cc6665ef6fcb63defa147fd7bec26e7fee31a1
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.9.0.tgz
    version: 0.9.0
  - apiVersion: v2
    appVersion: 0.8.0
    created: "2025-03-14T19:52:28.485595048Z"
    description: Windows GMSA Configuration
    digest: ec5a66b684c6507239d9fb9e08b71e910f6b097118efb7a29ffb4fb34ec385f3
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.8.0.tgz
    version: 0.8.0
  - apiVersion: v2
    appVersion: 0.7.0
    created: "2025-03-14T19:52:28.485025547Z"
    description: Windows GMSA Configuration
    digest: 8ff367280c392b406da60eb249b695b54de9d85b26c600628b6ffac13c1c9df7
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.3.tgz
    version: 0.7.3
  - apiVersion: v2
    appVersion: 0.7.0
    created: "2025-03-14T19:52:28.484422046Z"
    description: Windows GMSA Configuration
    digest: 97fc3964eabebb3cbe9ac7caf8ae7476a2f9371e508b2381e610983c0ad29f45
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.2.tgz
    version: 0.7.2
  - apiVersion: v2
    appVersion: 0.6.1
    created: "2025-03-14T19:52:28.483777945Z"
    description: Windows GMSA Configuration
    digest: c13d93a6ff7ff7f3219acd3b85ea085d1294f6d10a63a9d51d5c86d01dc80cb2
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.1.tgz
    version: 0.7.1
  - apiVersion: v2
    appVersion: 0.6.0
    created: "2025-03-14T19:52:28.483186144Z"
    description: Windows GMSA Configuration
    digest: 9b5fc25c235bac92af9ab0d960de8641b3a638ec8904326f2640f468e113b4ec
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.0.tgz
    version: 0.7.0
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.482604743Z"
    description: Windows GMSA Configuration
    digest: b637cee6f623598cca5611c3854514875ce1363d915ad8cdd4dabd8d96483546
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.6.0.tgz
    version: 0.6.0
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.482076042Z"
    description: Windows GMSA Configuration
    digest: 19003bcc3f5af484afd5a9ad0c833a861420daf7e50964563ecaf92e4a1dc35c
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.5.0.tgz
    version: 0.5.0
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.481452541Z"
    description: Windows GMSA Configuration
    digest: 1f6b8bbfe6af4088f80d08d3065094ab1504054526bea6e4477459fb738f504b
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.4.tgz
    version: 0.4.4
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.480501239Z"
    description: Windows GMSA Configuration
    digest: 6ae2ac87141c8e3ac598611153635b0dd6619634ddc27b27b9c1a8717a511d8a
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.3.tgz
    version: 0.4.3
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.479809838Z"
    description: Windows GMSA Configuration
    digest: 399a4d03dfc08ac4cd811106ab55d525845ca715f0edbdcfcafcfa02cceaf108
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.2.tgz
    version: 0.4.2
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.479194037Z"
    description: Windows GMSA Configuration
    digest: 0709c8666554bf7b521c003d33f6198dafe03bf883161e132e929dac478bda45
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.1.tgz
    version: 0.4.1
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.478498636Z"
    description: Windows GMSA Configuration
    digest: 7f29d22ba85d90a18e5b9c4e1a7d9ba1149d5827a2ca37b9a6fe1966e3598767
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.0.tgz
    version: 0.4.0
generated: "2025-03-14T19:52:28.468434118Z"
```

## File: `hooks/applypatch-msg.sample`
```
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:
```

## File: `hooks/commit-msg.sample`
```
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}
```

## File: `hooks/fsmonitor-watchman.sample`
```
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}
```

## File: `hooks/post-update.sample`
```
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info
```

## File: `hooks/pre-applypatch.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:
```

## File: `hooks/pre-commit.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff-index --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --
```

## File: `hooks/pre-merge-commit.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:
```

## File: `hooks/pre-push.sample`
```
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0
```

## File: `hooks/pre-rebase.sample`
```
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END
```

## File: `hooks/pre-receive.sample`
```
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi
```

## File: `hooks/prepare-commit-msg.sample`
```
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi
```

## File: `hooks/push-to-checkout.sample`
```
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi
```

## File: `hooks/sendemail-validate.sample`
```
#!/bin/sh

# An example hook script to validate a patch (and/or patch series) before
# sending it via email.
#
# The hook should exit with non-zero status after issuing an appropriate
# message if it wants to prevent the email(s) from being sent.
#
# To enable this hook, rename this file to "sendemail-validate".
#
# By default, it will only check that the patch(es) can be applied on top of
# the default upstream branch without conflicts in a secondary worktree. After
# validation (successful or not) of the last patch of a series, the worktree
# will be deleted.
#
# The following config variables can be set to change the default remote and
# remote ref that are used to apply the patches against:
#
#   sendemail.validateRemote (default: origin)
#   sendemail.validateRemoteRef (default: HEAD)
#
# Replace the TODO placeholders with appropriate checks according to your
# needs.

validate_cover_letter () {
	file="$1"
	# TODO: Replace with appropriate checks (e.g. spell checking).
	true
}

validate_patch () {
	file="$1"
	# Ensure that the patch applies without conflicts.
	git am -3 "$file" || return
	# TODO: Replace with appropriate checks for this patch
	# (e.g. checkpatch.pl).
	true
}

validate_series () {
	# TODO: Replace with appropriate checks for the whole series
	# (e.g. quick build, coding style checks, etc.).
	true
}

# main -------------------------------------------------------------------------

if test "$GIT_SENDEMAIL_FILE_COUNTER" = 1
then
	remote=$(git config --default origin --get sendemail.validateRemote) &&
	ref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&
	worktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&
	git worktree add -fd --checkout "$worktree" "refs/remotes/$remote/$ref" &&
	git config --replace-all sendemail.validateWorktree "$worktree"
else
	worktree=$(git config --get sendemail.validateWorktree)
fi || {
	echo "sendemail-validate: error: failed to prepare worktree" >&2
	exit 1
}

unset GIT_DIR GIT_WORK_TREE
cd "$worktree" &&

if grep -q "^diff --git " "$1"
then
	validate_patch "$1"
else
	validate_cover_letter "$1"
fi &&

if test "$GIT_SENDEMAIL_FILE_COUNTER" = "$GIT_SENDEMAIL_FILE_TOTAL"
then
	git config --unset-all sendemail.validateWorktree &&
	trap 'git worktree remove -ff "$worktree"' EXIT &&
	validate_series
fi
```

## File: `hooks/update.sample`
```
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0
```

## File: `info/exclude`
```
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```

## File: `kubernetes-sigs-windows-gmsa-993de21/.gitignore`
```
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

#IDE files
.idea/
.vscode/
```

## File: `kubernetes-sigs-windows-gmsa-993de21/CONTRIBUTING.md`
```markdown
# Contributing Guidelines

Welcome to Kubernetes. We are excited about the prospect of you joining our [community](https://github.com/kubernetes/community)! The Kubernetes community abides by the CNCF [code of conduct](../../../vault/archives/archive_legacy/AutoGPT/docs/content/code-of-conduct.md). Here is an excerpt:

_As contributors and maintainers of this project, and in the interest of fostering an open and welcoming community, we pledge to respect all people who contribute through reporting issues, posting feature requests, updating documentation, submitting pull requests or patches, and other activities._

## Getting Started

We have full documentation on how to get started contributing here:

<!---
If your repo has certain guidelines for contribution, put them here ahead of the general k8s resources
-->

- [Contributor License Agreement](https://git.k8s.io/community/CLA.md) Kubernetes projects require that you sign a Contributor License Agreement (CLA) before we can accept your pull requests
- [Kubernetes Contributor Guide](http://git.k8s.io/community/contributors/guide) - Main contributor documentation, or you can just jump directly to the [contributing section](http://git.k8s.io/community/contributors/guide#contributing)
- [Contributor Cheat Sheet](https://k8s.dev/cheatsheet) - Common resources for existing developers

## Generating Helm Charts and Index

When a chart needs to be updated, create the new version and the chart information. Run helm pack, then generate a new Helm chart index.yaml with the following command.

```Bash
helm repo index --url https://raw.githubusercontent.com/kubernetes-sigs/windows-gmsa/master/charts .
```
## Mentorship

- [Mentoring Initiatives](https://git.k8s.io/community/mentoring) - We have a diverse set of mentorship programs available that are always looking for volunteers!

<!---
Custom Information - if you're copying this template for the first time you can add custom content here, for example:

## Contact Information

- [Slack channel](https://kubernetes.slack.com/messages/kubernetes-users) - Replace `kubernetes-users` with your slack channel string, this will send users directly to your channel. 
- [Mailing list](URL)

-->
```

## File: `kubernetes-sigs-windows-gmsa-993de21/LICENSE`
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

## File: `kubernetes-sigs-windows-gmsa-993de21/OWNERS`
```
# See the OWNERS docs: https:/go.k8s.io/owners

approvers:
  - jsturtevant
  - marosset
  - zylxjtu

emeritus_approvers:
  - ddebroy
  - wk8
  - jayunit100

labels:
  - sig/windows
```

## File: `kubernetes-sigs-windows-gmsa-993de21/README.md`
```markdown
![Build Status](https://github.com/kubernetes-sigs/windows-gmsa/actions/workflows/build.yaml/badge.svg)

# Kubernetes Windows GMSA

External components to support [Windows' GMSA](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview) in Kubernetes.

## Community, discussion, contribution, and support

Learn how to engage with the Kubernetes community on the [community page](http://kubernetes.io/community/).

You can reach the maintainers of this project at:

- [Slack](http://slack.k8s.io/)
- [Mailing List](https://groups.google.com/forum/#!forum/kubernetes-dev)

### Code of conduct

Participation in the Kubernetes community is governed by the [Kubernetes Code of Conduct](../../../vault/archives/archive_legacy/AutoGPT/docs/content/code-of-conduct.md).

[owners]: https://git.k8s.io/community/contributors/guide/owners.md
[Creative Commons 4.0]: https://git.k8s.io/website/LICENSE
```

## File: `kubernetes-sigs-windows-gmsa-993de21/RELEASE.md`
```markdown
# Release Process

The Kubernetes Windows GMSA project is released on an as-needed basis. The process is as follows:

1. An issue is created proposing a new release with a changelog since the last release using the [Cut a release issue template](.github//ISSUE_TEMPLATE/new-release.md)
1. All [OWNERS](OWNERS) must LGTM this release issue
1. An OWNER runs `git tag -s $VERSION` from `master` branch and pushes the tag with `git push $VERSION`
1. An OWNER promotes the `gcr.io/k8s-staging-gmsa-webhook/k8s-gmsa-webhook` image built the tagged commit.
    1. Follow setup steps for `kpromo` from [here](https://github.com/kubernetes-sigs/promo-tools/blob/main/docs/promotion-pull-requests.md#preparing-environment) if needed
    1. Manually tag the desired container image in the [staging registry](https://console.cloud.google.com/gcr/images/k8s-staging-gmsa-webhook/GLOBAL) as `$VERSION`
    1. Run `kpromo pr` to open a pull request to have tagged container image promoted from staging to release registries

        ```bash
        kpromo pr --project gmsa-webhook --tag $VERSION --reviewers "@jayunit100 @jsturtevant @marosset" --fork {your github username}
        ```

    1. Review / merge image promotion PR
    1. Verify the image is available using `docker pull registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook:$VERSION`.  The image is pushed to the release repository via the post submit which can take an hour or two to trigger. View results at https://testgrid.k8s.io/sig-k8s-infra-k8sio#post-k8sio-image-promo

1. An OWNER creates a release with by
    1. Navigating to [releases](https://github.com/kubernetes-sigs/windows-gmsa/releases) and clicking on `Draft a new release`
    1. Selecting the tag for the current release version
    1. Setting the title of the release to the current release version
    1. Clicking `Auto-generate release notes` button (and editing what was generated as appropriate) 
    1. Adding instructions on how to deploy the current release **to the top of the releaes notes** with the following template:

        To deploy:

        ```bash
        K8S_GMSA_DEPLOY_DOWNLOAD_REV='$VERSION' \
            ./deploy-gmsa-webhook.sh --file ./gmsa-manifests \
            --image registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook:$VERSION
        ```

    1. Clicking on `Publish Release`
1. Update `image.tag` in `charts/gmsa/chart.yaml` to $VERSION and create new chart package:
    1. Run `helm package charts/gmsa`. Make sure the resulting tgz file is in the `charts/repo` folder.
    1. Run `helm repo index charts/repo/` to update the helm index
1. Update the **IMAGE_NAME** variable in `admission_webhook/deploy/deploy-gmsa-webhook.sh` to use the latest released image.
1. The release issue is closed
1. An announcement email is sent to `kubernetes-sig-windows@googlegroups.com` with the subject `[ANNOUNCE] Kubernetes SIG-Windows GMSA Webhook $VERSION is Released`
1. An announcement is posted in `#SIG-windows` in the Kubernetes slack.
```

## File: `kubernetes-sigs-windows-gmsa-993de21/SECURITY_CONTACTS`
```
# Defined below are the security contacts for this repo.
#
# They are the contact point for the Product Security Team to reach out
# to for triaging and handling of incoming issues.
#
# The below names agree to abide by the
# [Embargo Policy](https://github.com/kubernetes/sig-release/blob/master/security-release-process-documentation/security-release-process.md#embargo-policy)
# and will be removed and replaced if they violate that agreement.
#
# DO NOT REPORT SECURITY VULNERABILITIES DIRECTLY TO THESE NAMES, FOLLOW THE
# INSTRUCTIONS AT https://kubernetes.io/security/

ddebroy
michmike
PatrickLang
```

## File: `kubernetes-sigs-windows-gmsa-993de21/cloudbuild.yaml`
```yaml
# See https://cloud.google.com/cloud-build/docs/build-config

# this must be specified in seconds. If omitted, defaults to 600s (10 mins)
timeout: 1200s
# this prevents errors if you don't use both _GIT_TAG and _PULL_BASE_REF,
# or any new substitutions added in the future.
options:
  substitution_option: ALLOW_LOOSE
steps:
  - name:  'gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20230522-312425ae46'
    entrypoint: bash
    env:
    - DOCKER_CLI_EXPERIMENTAL=enabled
    - TAG=${_GIT_TAG}
    - PULL_BASE_REF=${_PULL_BASE_REF}
      # default cloudbuild has HOME=/builder/home and docker buildx is in /root/.docker/cli-plugins/docker-buildx
      # set the home to /root explicitly to if using docker buildx
    - HOME=/root
    args:
    - -c
    - |
      echo "Building / Pushing GMSA webhook container"
      gcloud auth configure-docker
      cd admission-webhook
      make release-staging
substitutions:
  # _GIT_TAG will be filled with a git-based tag for the image, of the form vYYYYMMDD-hash, and
  # can be used as a substitution
  _GIT_TAG: '12345'
  # _PULL_BASE_REF will contain the ref that was pushed to to trigger this build -
  # a branch like 'master' or 'release-0.2', or a tag like 'v0.2'.
  _PULL_BASE_REF: 'master'
```

## File: `kubernetes-sigs-windows-gmsa-993de21/code-of-conduct.md`
```markdown
# Kubernetes Community Code of Conduct

Please refer to our [Kubernetes Community Code of Conduct](https://git.k8s.io/community/code-of-conduct.md)
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/.dockerignore`
```
/dev/
/integration_tests/tmp/
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/.gitignore`
```
/dev/
/integration_tests/tmp/
/testdata/
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/Makefile`
```
.DEFAULT_GOAL := test
SHELL := /bin/bash

WEBHOOK_ROOT := $(CURDIR)

REGISTRY ?= registry.k8s.io/gmsa-webhook
STAGING_REGISTRY ?= gcr.io/k8s-staging-gmsa-webhook
IMAGE_NAME ?= k8s-gmsa-webhook
TAG ?=  $(shell git describe --tags --always `git rev-parse HEAD`)
WEBHOOK_IMG ?= $(REGISTRY)/$(IMAGE_NAME)

DEV_IMAGE_NAME = k8s-windows-gmsa-webhook-dev

CURL = $(shell which curl 2> /dev/null)
WGET = $(shell which wget 2> /dev/null)

ifeq ($(CURL)$(WGET),)
$(error "Neither curl nor wget available")
endif

UNAME = $(shell uname | tr A-Z a-z)
ifeq ($(UNAME),)
$(error "Unable to determine OS type")
endif

include make/*.mk

.PHONY: test
test: deps_install unit_tests integration_tests

# the UNIT_TEST_FLAGS env var can be set to eg run only specific tests, e.g:
# UNIT_TEST_FLAGS='-test.run TestHTTPWebhook' make unit_tests
.PHONY: unit_tests
unit_tests:
	go test -v -count=1 -cover $(UNIT_TEST_FLAGS)

.PHONY: integration_tests
integration_tests: image_build deploy_webhook run_integration_tests

.PHONY: integration_tests_chart
integration_tests_chart: image_build deploy_chart run_integration_tests

.PHONY: integration_tests_with_dev_image
integration_tests_with_dev_image: image_build_dev deploy_dev_webhook run_integration_tests

# the INTEGRATION_TEST_FLAGS env var can be set to eg run only specific tests, e.g.:
# INTEGRATION_TEST_FLAGS='-test.run TestHappyPathWithPodLevelCredSpec' make run_integration_tests
.PHONY: run_integration_tests
run_integration_tests:
	@ echo "### Starting integration tests with Kubernetes version: $(KUBERNETES_VERSION) ###"
	cd integration_tests && KUBECONFIG=$(KUBECONFIG) KUBECTL=$(KUBECTL) go test -count 1 -v $(INTEGRATION_TEST_FLAGS)

.PHONY: clean_integration_tests
clean_integration_tests:
	rm -rf integration_tests/tmp

.PHONY: clean
clean: cluster_clean clean_integration_tests deps_clean

.PHONY: release-staging 
release-staging: ## Builds and push webhook image to k8s-staging bucket
	REGISTRY=$(STAGING_REGISTRY) $(MAKE) image_build_and_push
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/README.md`
```markdown
# Windows GMSA Webhook Admission controller

## Supported versions

This branch supports versions 1.23 and later. 

## How to deploy

Assuming that `kubectl` is in your path and that your cluster's kube admin config file is present at either the canonical location
(`~/.kube/config`) or at the path specified by the `KUBECONFIG` environment variable, simply run:
```bash
curl -sL https://raw.githubusercontent.com/kubernetes-sigs/windows-gmsa/master/admission-webhook/deploy/deploy-gmsa-webhook.sh | bash -s -- --file webhook-manifests.yml
```

Run with the `--dry-run` option to not change anything to your cluster just yet and simply review the change it would be doing.

Run with `--help` to see all the available options.

## Amazon EKS

According to the Amazon EKS certificate signing documentation, all clusters running Amazon EKS version 1.22 or newer supports the following signer beta.eks.amazonaws.com/app-serving for Kubernetes Certificate Signing Requests (CSR) which is compatible with the latest gMSA admission webhook installation. As a result, we need to replace kubernetes.io/kubelet-serving signer in the gMSA Webhook create-signed-cert.sh file with the following signer : beta.eks.amazonaws.com/app-serving
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/cert_reloader.go`
```go
package main

import (
	"context"
	"crypto/tls"
	"sync"

	"github.com/fsnotify/fsnotify"
	"github.com/sirupsen/logrus"
)

type CertLoader interface {
	CertPath() string
	KeyPath() string
	LoadCertificate() (*tls.Certificate, error)
}

type CertReloader struct {
	sync.Mutex
	certPath    string
	keyPath     string
	certificate *tls.Certificate
}

func NewCertReloader(certPath, keyPath string) *CertReloader {
	return &CertReloader{
		certPath: certPath,
		keyPath:  keyPath,
	}
}

func (cr *CertReloader) CertPath() string {
	return cr.certPath
}

func (cr *CertReloader) KeyPath() string {
	return cr.keyPath
}

// LoadCertificate loads or reloads the certificate from disk.
func (cr *CertReloader) LoadCertificate() (*tls.Certificate, error) {
	cr.Lock()
	defer cr.Unlock()

	cert, err := tls.LoadX509KeyPair(cr.certPath, cr.keyPath)
	if err != nil {
		return nil, err
	}
	cr.certificate = &cert
	return cr.certificate, nil
}

// GetCertificateFunc returns a function that can be assigned to tls.Config.GetCertificate
func (cr *CertReloader) GetCertificateFunc() func(*tls.ClientHelloInfo) (*tls.Certificate, error) {
	return func(chi *tls.ClientHelloInfo) (*tls.Certificate, error) {
		return cr.certificate, nil
	}
}

func watchCertFiles(ctx context.Context, certLoader CertLoader) {
	logrus.Infof("Starting certificate watcher on path %v and %v", certLoader.CertPath(), certLoader.KeyPath())
	watcher, err := fsnotify.NewWatcher()
	if err != nil {
		logrus.Errorf("error creating watcher: %v", err)
	}

	go func() {
		defer watcher.Close()

		for {
			select {
			case event, ok := <-watcher.Events:
				if !ok {
					logrus.Errorf("watcher events returned !ok: %v", err)
					return
				}
				logrus.Infof("detected change in certificate file: %v", event.Name)
				_, err := certLoader.LoadCertificate()
				if err != nil {
					logrus.Errorf("error reloading certificate: %v", err)
				} else {
					logrus.Infof("successfully reloaded certificate")
				}
			case err, ok := <-watcher.Errors:
				if !ok {
					logrus.Errorf("watcher error returned !ok: %v", err)
					return
				}
				logrus.Errorf("watcher error: %v", err)
			case <-ctx.Done():
				logrus.Info("stopping certificate watcher")
				return
			}
		}
	}()

	err = watcher.Add(certLoader.CertPath())
	if err != nil {
		logrus.Fatalf("error watching certificate file: %v", err)
	}
	err = watcher.Add(certLoader.KeyPath())
	if err != nil {
		logrus.Fatalf("error watching key file: %v", err)
	}
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/cert_reloader_test.go`
```go
package main

import (
	"context"
	"crypto/tls"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

// TestCertReloader tests the reloading functionality of the certificate.
func TestCertReloader(t *testing.T) {
	// Create temporary cert and key files
	tmpCertFile, err := os.CreateTemp("", "cert*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp cert file: %v", err)
	}
	defer os.Remove(tmpCertFile.Name()) // clean up

	tmpKeyFile, err := os.CreateTemp("", "key*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp key file: %v", err)
	}
	defer os.Remove(tmpKeyFile.Name()) // clean up

	// Write initial cert and key to temp files
	initialCertData, _ := os.ReadFile("testdata/cert.pem")
	if err := os.WriteFile(tmpCertFile.Name(), initialCertData, 0644); err != nil {
		t.Fatalf("Failed to write to temp cert file: %v", err)
	}

	initialKeyData, _ := os.ReadFile("testdata/key.pem")
	if err := os.WriteFile(tmpKeyFile.Name(), initialKeyData, 0644); err != nil {
		t.Fatalf("Failed to write to temp key file: %v", err)
	}

	// Setup CertReloader with temp files
	certReloader := NewCertReloader(tmpCertFile.Name(), tmpKeyFile.Name())
	_, err = certReloader.LoadCertificate()
	if err != nil {
		t.Fatalf("Failed to load initial certificate: %v", err)
	}

	// Mocking a certificate change by writing new data to the files
	newCertData, _ := os.ReadFile("testdata/cert.pem")
	if err := os.WriteFile(tmpCertFile.Name(), newCertData, 0644); err != nil {
		t.Fatalf("Failed to write new data to cert file: %v", err)
	}

	// Simulate reloading
	_, err = certReloader.LoadCertificate()
	if err != nil {
		t.Fatalf("Failed to reload certificate: %v", err)
	}
}

type mockCertLoader struct {
	certPath     string
	keyPath      string
	loadCertFunc func() (*tls.Certificate, error)
}

func (m *mockCertLoader) CertPath() string {
	return m.certPath
}

func (m *mockCertLoader) KeyPath() string {
	return m.keyPath
}

func (m *mockCertLoader) LoadCertificate() (*tls.Certificate, error) {
	return m.loadCertFunc()
}

func TestWatchingCertFiles(t *testing.T) {
	tmpCertFile, err := os.CreateTemp("", "cert*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp cert file: %v", err)
	}
	defer os.Remove(tmpCertFile.Name())

	tmpKeyFile, err := os.CreateTemp("", "key*.pem")
	if err != nil {
		t.Fatalf("Failed to create temp key file: %v", err)
	}
	defer os.Remove(tmpKeyFile.Name())

	loadCertFuncChan := make(chan bool)
	done := make(chan bool)

	cl := &mockCertLoader{
		certPath: tmpCertFile.Name(),
		keyPath:  tmpKeyFile.Name(),
		loadCertFunc: func() (*tls.Certificate, error) {
			loadCertFuncChan <- true
			return &tls.Certificate{}, nil
		},
	}

	go func() {
		called := <-loadCertFuncChan
		assert.True(t, called)
		done <- true
	}()

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	watchCertFiles(ctx, cl)

	newCertData, _ := os.ReadFile("testdata/cert.pem")
	if err := os.WriteFile(tmpCertFile.Name(), newCertData, 0644); err != nil {
		t.Fatalf("Failed to write new data to cert file: %v", err)
	}

	<-done
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/go.mod`
```
module github.com/kubernetes-sigs/windows-gmsa/admission-webhook

go 1.23.0

toolchain go1.23.7

require (
	github.com/fsnotify/fsnotify v1.8.0
	github.com/google/uuid v1.6.0
	github.com/mitchellh/go-homedir v1.1.0
	github.com/sirupsen/logrus v1.9.3
	github.com/stretchr/testify v1.9.0
	gotest.tools v2.2.0+incompatible
	k8s.io/api v0.32.2
	k8s.io/apimachinery v0.32.2
	k8s.io/apiserver v0.32.2
	k8s.io/client-go v0.32.2
)

require (
	github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc // indirect
	github.com/emicklei/go-restful/v3 v3.12.2 // indirect
	github.com/fxamacker/cbor/v2 v2.7.0 // indirect
	github.com/go-logr/logr v1.4.2 // indirect
	github.com/go-openapi/jsonpointer v0.21.0 // indirect
	github.com/go-openapi/jsonreference v0.21.0 // indirect
	github.com/go-openapi/swag v0.23.0 // indirect
	github.com/gogo/protobuf v1.3.2 // indirect
	github.com/golang/protobuf v1.5.4 // indirect
	github.com/google/gnostic-models v0.6.9 // indirect
	github.com/google/go-cmp v0.7.0 // indirect
	github.com/google/gofuzz v1.2.0 // indirect
	github.com/josharian/intern v1.0.0 // indirect
	github.com/json-iterator/go v1.1.12 // indirect
	github.com/mailru/easyjson v0.9.0 // indirect
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.2 // indirect
	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
	github.com/pkg/errors v0.9.1 // indirect
	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
	github.com/x448/float16 v0.8.4 // indirect
	golang.org/x/net v0.37.0 // indirect
	golang.org/x/oauth2 v0.28.0 // indirect
	golang.org/x/sys v0.31.0 // indirect
	golang.org/x/term v0.30.0 // indirect
	golang.org/x/text v0.23.0 // indirect
	golang.org/x/time v0.11.0 // indirect
	google.golang.org/protobuf v1.36.5 // indirect
	gopkg.in/evanphx/json-patch.v4 v4.12.0 // indirect
	gopkg.in/inf.v0 v0.9.1 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
	k8s.io/klog/v2 v2.130.1 // indirect
	k8s.io/kube-openapi v0.0.0-20250304201544-e5f78fe3ede9 // indirect
	k8s.io/utils v0.0.0-20241210054802-24370beab758 // indirect
	sigs.k8s.io/json v0.0.0-20241014173422-cfa47c3a1cc8 // indirect
	sigs.k8s.io/randfill v1.0.0 // indirect
	sigs.k8s.io/structured-merge-diff/v4 v4.6.0 // indirect
	sigs.k8s.io/yaml v1.4.0 // indirect
)

replace golang.org/x/text => golang.org/x/text v0.23.0

replace golang.org/x/term => golang.org/x/term v0.30.0

replace golang.org/x/time => golang.org/x/time v0.11.0

replace golang.org/x/sys => golang.org/x/sys v0.31.0

replace golang.org/x/net => golang.org/x/net v0.37.0
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/go.sum`
```
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/emicklei/go-restful/v3 v3.12.2 h1:DhwDP0vY3k8ZzE0RunuJy8GhNpPL6zqLkDf9B/a0/xU=
github.com/emicklei/go-restful/v3 v3.12.2/go.mod h1:6n3XBCmQQb25CM2LCACGz8ukIrRry+4bhvbpWn3mrbc=
github.com/fsnotify/fsnotify v1.8.0 h1:dAwr6QBTBZIkG8roQaJjGof0pp0EeF+tNV7YBP3F/8M=
github.com/fsnotify/fsnotify v1.8.0/go.mod h1:8jBTzvmWwFyi3Pb8djgCCO5IBqzKJ/Jwo8TRcHyHii0=
github.com/fxamacker/cbor/v2 v2.7.0 h1:iM5WgngdRBanHcxugY4JySA0nk1wZorNOpTgCMedv5E=
github.com/fxamacker/cbor/v2 v2.7.0/go.mod h1:pxXPTn3joSm21Gbwsv0w9OSA2y1HFR9qXEeXQVeNoDQ=
github.com/go-logr/logr v1.4.2 h1:6pFjapn8bFcIbiKo3XT4j/BhANplGihG6tvd+8rYgrY=
github.com/go-logr/logr v1.4.2/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-openapi/jsonpointer v0.21.0 h1:YgdVicSA9vH5RiHs9TZW5oyafXZFc6+2Vc1rr/O9oNQ=
github.com/go-openapi/jsonpointer v0.21.0/go.mod h1:IUyH9l/+uyhIYQ/PXVA41Rexl+kOkAPDdXEYns6fzUY=
github.com/go-openapi/jsonreference v0.21.0 h1:Rs+Y7hSXT83Jacb7kFyjn4ijOuVGSvOdF2+tg1TRrwQ=
github.com/go-openapi/jsonreference v0.21.0/go.mod h1:LmZmgsrTkVg9LG4EaHeY8cBDslNPMo06cago5JNLkm4=
github.com/go-openapi/swag v0.23.0 h1:vsEVJDUo2hPJ2tu0/Xc+4noaxyEffXNIs3cOULZ+GrE=
github.com/go-openapi/swag v0.23.0/go.mod h1:esZ8ITTYEsH1V2trKHjAN8Ai7xHb8RV+YSZ577vPjgQ=
github.com/go-task/slim-sprig/v3 v3.0.0 h1:sUs3vkvUymDpBKi3qH1YSqBQk9+9D/8M2mN1vB6EwHI=
github.com/go-task/slim-sprig/v3 v3.0.0/go.mod h1:W848ghGpv3Qj3dhTPRyJypKRiqCdHZiAzKg9hl15HA8=
github.com/gogo/protobuf v1.3.2 h1:Ov1cvc58UF3b5XjBnZv7+opcTcQFZebYjWzi34vdm4Q=
github.com/gogo/protobuf v1.3.2/go.mod h1:P1XiOD3dCwIKUDQYPy72D8LYyHL2YPYrpS2s69NZV8Q=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/gnostic-models v0.6.9 h1:MU/8wDLif2qCXZmzncUQ/BOfxWfthHi63KqpoNbWqVw=
github.com/google/gnostic-models v0.6.9/go.mod h1:CiWsm0s6BSQd1hRn8/QmxqB6BesYcbSZxsz9b0KuDBw=
github.com/google/go-cmp v0.5.9/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/gofuzz v1.0.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/google/gofuzz v1.2.0 h1:xRy4A+RhZaiKjJ1bPfwQ8sedCA+YS2YcCHW6ec7JMi0=
github.com/google/gofuzz v1.2.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/google/pprof v0.0.0-20241029153458-d1b30febd7db h1:097atOisP2aRj7vFgYQBbFN4U4JNXUNYpxael3UzMyo=
github.com/google/pprof v0.0.0-20241029153458-d1b30febd7db/go.mod h1:vavhavw2zAxS5dIdcRluK6cSGGPlZynqzFM8NdvU144=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/josharian/intern v1.0.0 h1:vlS4z54oSdjm0bgjRigI+G1HpF+tI+9rE5LLzOg8HmY=
github.com/josharian/intern v1.0.0/go.mod h1:5DoeVV0s6jJacbCEi61lwdGj/aVlrQvzHFFd8Hwg//Y=
github.com/json-iterator/go v1.1.12 h1:PV8peI4a0ysnczrg+LtxykD8LfKY9ML6u2jnxaEnrnM=
github.com/json-iterator/go v1.1.12/go.mod h1:e30LSqwooZae/UwlEbR2852Gd8hjQvJoHmT4TnhNGBo=
github.com/kisielk/errcheck v1.5.0/go.mod h1:pFxgyoBC7bSaBwPgfKdkLd5X25qrDl4LWUI2bnpBCr8=
github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/mailru/easyjson v0.9.0 h1:PrnmzHw7262yW8sTBwxi1PdJA3Iw/EKBa8psRf7d9a4=
github.com/mailru/easyjson v0.9.0/go.mod h1:1+xMtQp2MRNVL/V1bOzuP3aP8VNwRW55fQUto+XFtTU=
github.com/mitchellh/go-homedir v1.1.0 h1:lukF9ziXFxDFPkA1vsr5zpc1XuPDn/wFntq5mG+4E0Y=
github.com/mitchellh/go-homedir v1.1.0/go.mod h1:SfyaCUpYCn1Vlf4IUYiD9fPX4A5wJrkLzIz1N1q0pr0=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd h1:TRLaZ9cD/w8PVh93nsPXa1VrQ6jlwL5oN8l14QlcNfg=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v1.0.2 h1:xBagoLtFs94CBntxluKeaWgTMpvLxC4ur3nMaC9Gz0M=
github.com/modern-go/reflect2 v1.0.2/go.mod h1:yWuevngMOJpCy52FWWMvUC8ws7m/LJsjYzDa0/r8luk=
github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq1c1nUAm88MOHcQC9l5mIlSMApZMrHA=
github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
github.com/onsi/ginkgo/v2 v2.21.0 h1:7rg/4f3rB88pb5obDgNZrNHrQ4e6WpjonchcpuBRnZM=
github.com/onsi/ginkgo/v2 v2.21.0/go.mod h1:7Du3c42kxCUegi0IImZ1wUQzMBVecgIHjR1C+NkhLQo=
github.com/onsi/gomega v1.35.1 h1:Cwbd75ZBPxFSuZ6T+rN/WCb/gOc6YgFBXLlZLhC7Ds4=
github.com/onsi/gomega v1.35.1/go.mod h1:PvZbdDc8J6XJEpDK4HCuRBm8a6Fzp9/DmhC9C7yFlog=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 h1:Jamvg5psRIccs7FGNTlIRMkT8wgtp5eCXdBlqhYGL6U=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.12.0 h1:exVL4IDcn6na9z1rAb56Vxr+CgyK3nn3O+epU5NdKM8=
github.com/rogpeppe/go-internal v1.12.0/go.mod h1:E+RYuTGaKKdloAfM02xzb0FW3Paa99yedzYV+kq4uf4=
github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ=
github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
github.com/x448/float16 v0.8.4 h1:qLwI1I70+NjRFUR3zs1JPUCgaCXSh3SW62uAKT1mSBM=
github.com/x448/float16 v0.8.4/go.mod h1:14CWIYCyZA/cWjXOioeEpHeN/83MdbZDRQHoFcYsOfg=
github.com/yuin/goldmark v1.1.27/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.2.1/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.36.0/go.mod h1:Y4J0ReaxCR1IMaabaSMugxJES1EpwhBHhv2bDHklZvc=
golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4/go.mod h1:jJ57K6gSWd91VN4djpZkiMVwK6gcyfeH4XE8wZrZaV4=
golang.org/x/mod v0.12.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.15.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/mod v0.17.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/net v0.37.0 h1:1zLorHbz+LYj7MQlSf1+2tPIIgibq2eL5xkrGk6f+2c=
golang.org/x/net v0.37.0/go.mod h1:ivrbrMbzFq5J41QOQh0siUuly180yBYtLp+CKbEaFx8=
golang.org/x/oauth2 v0.28.0 h1:CrgCKl8PPAVtLnU3c+EDw6x11699EWlsDeWNWKdIOkc=
golang.org/x/oauth2 v0.28.0/go.mod h1:onh5ek6nERTohokkhCD/y2cV4Do3fxFHFuAejCkRWT8=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220722155255-886fb9371eb4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.3.0/go.mod h1:FU7BRWz2tNW+3quACPkgCx/L+uEAv1htQ0V83Z9Rj+Y=
golang.org/x/sync v0.6.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.12.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sys v0.31.0 h1:ioabZlmFYtWhL+TRYpcnNlLwhyxaM9kWTDEmfnprqik=
golang.org/x/sys v0.31.0/go.mod h1:BJP2sWEmIv4KK5OTEluFJCKSidICx8ciO85XgH3Ak8k=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2/go.mod h1:TeRTkGYfJXctD9OcfyVLyj2J3IxLnKwHJR8f4D8a3YE=
golang.org/x/term v0.30.0 h1:PQ39fJZ+mfadBm0y5WlL4vlM7Sx1Hgf13sMIY2+QS9Y=
golang.org/x/term v0.30.0/go.mod h1:NYYFdzHoI5wRh/h5tDMdMqCqPJZEuNqVR5xJLd/n67g=
golang.org/x/text v0.23.0 h1:D71I7dUrlY+VX0gQShAThNGHFxZ13dGLBHQLVl1mJlY=
golang.org/x/text v0.23.0/go.mod h1:/BLNzu4aZCJ1+kcD0DNRotWKage4q2rGVAg4o22unh4=
golang.org/x/time v0.11.0 h1:/bpjEDfN9tkoN/ryeYHnv5hcMlc8ncjMcM4XBk5NWV0=
golang.org/x/time v0.11.0/go.mod h1:CDIdPxbZBQxdj6cxyCIdrNogrJKMJ7pr37NYpMcMDSg=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20200619180055-7c47624df98f/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20210106214847-113979e3529a/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.1.12/go.mod h1:hNGJHUnrk76NpqgfD5Aqm5Crs+Hm0VOH/i9J2+nxYbc=
golang.org/x/tools v0.13.0/go.mod h1:HvlwmtVNQAhOuCjW7xxvovg8wbNq7LwfXh/k7wXUl58=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d/go.mod h1:aiJjzUbINMkxbQROHiO6hDPo2LHcIPhhQsa9DLh0yGk=
golang.org/x/tools v0.26.0 h1:v/60pFQmzmT9ExmjDv2gGIfi3OqfKoEP6I5+umXlbnQ=
golang.org/x/tools v0.26.0/go.mod h1:TPVVj70c7JJ3WCazhD8OdXcZg/og+b9+tH/KxylGwH0=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/protobuf v1.36.5 h1:tPhr+woSbjfYvY6/GPufUoYizxw1cF/yFoxJ2fmpwlM=
google.golang.org/protobuf v1.36.5/go.mod h1:9fA7Ob0pmnwhb644+1+CVWFRbNajQ6iRojtC/QF5bRE=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/evanphx/json-patch.v4 v4.12.0 h1:n6jtcsulIzXPJaxegRbvFNNrZDjbij7ny3gmSPG+6V4=
gopkg.in/evanphx/json-patch.v4 v4.12.0/go.mod h1:p8EYWUEYMpynmqDbY58zCKCFZw8pRWMG4EsWvDvM72M=
gopkg.in/inf.v0 v0.9.1 h1:73M5CoZyi3ZLMOyDlQh031Cx6N9NDJ2Vvfl76EDAgDc=
gopkg.in/inf.v0 v0.9.1/go.mod h1:cWUDdTG/fYaXco+Dcufb5Vnc6Gp2YChqWtbxRZE0mXw=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gotest.tools v2.2.0+incompatible h1:VsBPFP1AI068pPrMxtb/S8Zkgf9xEmTLJjfM+P5UIEo=
gotest.tools v2.2.0+incompatible/go.mod h1:DsYFclhRJ6vuDpmuTbkuFWG+y2sxOXAzmJt81HFBacw=
k8s.io/api v0.32.2 h1:bZrMLEkgizC24G9eViHGOPbW+aRo9duEISRIJKfdJuw=
k8s.io/api v0.32.2/go.mod h1:hKlhk4x1sJyYnHENsrdCWw31FEmCijNGPJO5WzHiJ6Y=
k8s.io/apimachinery v0.32.2 h1:yoQBR9ZGkA6Rgmhbp/yuT9/g+4lxtsGYwW6dR6BDPLQ=
k8s.io/apimachinery v0.32.2/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
k8s.io/apiserver v0.32.2 h1:WzyxAu4mvLkQxwD9hGa4ZfExo3yZZaYzoYvvVDlM6vw=
k8s.io/apiserver v0.32.2/go.mod h1:PEwREHiHNU2oFdte7BjzA1ZyjWjuckORLIK/wLV5goM=
k8s.io/client-go v0.32.2 h1:4dYCD4Nz+9RApM2b/3BtVvBHw54QjMFUl1OLcJG5yOA=
k8s.io/client-go v0.32.2/go.mod h1:fpZ4oJXclZ3r2nDOv+Ux3XcJutfrwjKTCHz2H3sww94=
k8s.io/klog/v2 v2.130.1 h1:n9Xl7H1Xvksem4KFG4PYbdQCQxqc/tTUyrgXaOhHSzk=
k8s.io/klog/v2 v2.130.1/go.mod h1:3Jpz1GvMt720eyJH1ckRHK1EDfpxISzJ7I9OYgaDtPE=
k8s.io/kube-openapi v0.0.0-20250304201544-e5f78fe3ede9 h1:t0huyHnz6HsokckRxAF1bY0cqPFwzINKCL7yltEjZQc=
k8s.io/kube-openapi v0.0.0-20250304201544-e5f78fe3ede9/go.mod h1:5jIi+8yX4RIb8wk3XwBo5Pq2ccx4FP10ohkbSKCZoK8=
k8s.io/utils v0.0.0-20241210054802-24370beab758 h1:sdbE21q2nlQtFh65saZY+rRM6x6aJJI8IUa1AmH/qa0=
k8s.io/utils v0.0.0-20241210054802-24370beab758/go.mod h1:OLgZIPagt7ERELqWJFomSt595RzquPNLL48iOWgYOg0=
sigs.k8s.io/json v0.0.0-20241014173422-cfa47c3a1cc8 h1:gBQPwqORJ8d8/YNZWEjoZs7npUVDpVXUUOFfW6CgAqE=
sigs.k8s.io/json v0.0.0-20241014173422-cfa47c3a1cc8/go.mod h1:mdzfpAEoE6DHQEN0uh9ZbOCuHbLK5wOm7dK4ctXE9Tg=
sigs.k8s.io/randfill v0.0.0-20250304075658-069ef1bbf016/go.mod h1:XeLlZ/jmk4i1HRopwe7/aU3H5n1zNUcX6TM94b3QxOY=
sigs.k8s.io/randfill v1.0.0 h1:JfjMILfT8A6RbawdsK2JXGBR5AQVfd+9TbzrlneTyrU=
sigs.k8s.io/randfill v1.0.0/go.mod h1:XeLlZ/jmk4i1HRopwe7/aU3H5n1zNUcX6TM94b3QxOY=
sigs.k8s.io/structured-merge-diff/v4 v4.6.0 h1:IUA9nvMmnKWcj5jl84xn+T5MnlZKThmUW1TdblaLVAc=
sigs.k8s.io/structured-merge-diff/v4 v4.6.0/go.mod h1:dDy58f92j70zLsuZVuUX5Wp9vtxXpaZnkPGWeqDfCps=
sigs.k8s.io/yaml v1.4.0 h1:Mk1wCc2gy/F0THH0TAp1QYyJNzRm2KCLy3o5ASXVI5E=
sigs.k8s.io/yaml v1.4.0/go.mod h1:Ejl7/uTz7PSA4eKMyQCUTnhZYNmLIl+5c2lQPGR2BPY=
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/kube_client.go`
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"

	authorizationv1 "k8s.io/api/authorization/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime/schema"
	"k8s.io/apiserver/pkg/authentication/serviceaccount"
	"k8s.io/client-go/dynamic"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
)

const (
	// these 3 constants are the coordinates of the Custom Resource Definition
	crdAPIGroup     = "windows.k8s.io"
	crdAPIVersion   = "v1"
	crdResourceName = "gmsacredentialspecs"

	// crdContentsField is the single field that's expected to be defined in a GMSA CRD,
	// and to contain the contents of the cred spec itself
	crdContentsField = "credspec"

	// notFound is used in `isNotFoundError` below
	notFound = "not found"
)

// kubeClient centralizes all the operations we need when talking to k8s
type kubeClient struct {
	coreClient    kubernetes.Interface
	dynamicClient dynamic.Interface
}

func newKubeClient(config *rest.Config) (*kubeClient, error) {
	coreClient, err := kubernetes.NewForConfig(config)
	if err != nil {
		return nil, err
	}

	dynamicClient, err := dynamic.NewForConfig(config)
	if err != nil {
		return nil, err
	}

	return &kubeClient{
		coreClient:    coreClient,
		dynamicClient: dynamicClient,
	}, nil
}

// isAuthorizedToReadConfigMap checks whether a given service account is authorized to `use` a given cred spec.
// If it denies the request, it also returns a string explaining why.
func (kc *kubeClient) isAuthorizedToUseCredSpec(ctx context.Context, serviceAccountName, namespace, credSpecName string) (bool, string) {
	serviceAccountUserInfo := serviceaccount.UserInfo(namespace, serviceAccountName, "")

	// needed to cast `authorizationv1.ExtraValue` to `[]string`
	var extra map[string]authorizationv1.ExtraValue
	for k, v := range serviceAccountUserInfo.GetExtra() {
		extra[k] = v
	}

	subjectAccessReview := authorizationv1.LocalSubjectAccessReview{
		ObjectMeta: metav1.ObjectMeta{
			Namespace: namespace,
		},
		Spec: authorizationv1.SubjectAccessReviewSpec{
			ResourceAttributes: &authorizationv1.ResourceAttributes{
				Namespace: namespace,
				Verb:      "use",
				Group:     crdAPIGroup,
				Version:   crdAPIVersion,
				Resource:  crdResourceName,
				Name:      credSpecName,
			},
			User:   serviceAccountUserInfo.GetName(),
			Groups: serviceAccountUserInfo.GetGroups(),
			UID:    serviceAccountUserInfo.GetUID(),
			Extra:  extra,
		},
	}

	response, err := kc.coreClient.AuthorizationV1().LocalSubjectAccessReviews(namespace).Create(ctx, &subjectAccessReview, metav1.CreateOptions{})
	if err != nil {
		return false, fmt.Sprintf("error when checking authz access: %v", err.Error())
	}
	return response.Status.Allowed && !response.Status.Denied, response.Status.Reason
}

// retrieveCredSpecContents fetches the actual contents of a cred spec.
// If it returns an error, it also returns the corresponding HTTP code.
func (kc *kubeClient) retrieveCredSpecContents(ctx context.Context, credSpecName string) (string, int, error) {
	resource := schema.GroupVersionResource{
		Group:    crdAPIGroup,
		Version:  crdAPIVersion,
		Resource: crdResourceName,
	}
	credSpec, err := kc.dynamicClient.Resource(resource).Get(ctx, credSpecName, metav1.GetOptions{})
	if err != nil {
		if isNotFoundError(err) {
			return "", http.StatusNotFound, fmt.Errorf("cred spec %s does not exist", credSpecName)
		}
		return "", http.StatusInternalServerError, fmt.Errorf("unable to retrieve the contents of cred spec %s: %v", credSpecName, err)
	}

	if contents, present := credSpec.Object[crdContentsField]; !present || contents == "" {
		return "", http.StatusExpectationFailed, fmt.Errorf("cred spec %s does not have a %s key", credSpecName, crdContentsField)
	}

	contentsBytes, err := json.Marshal(credSpec.Object[crdContentsField])
	if err != nil {
		return "", http.StatusInternalServerError, fmt.Errorf("unable to marshall cred spec %s into a JSON: %v", credSpecName, err)
	}

	return string(contentsBytes), http.StatusOK, nil
}

// isNotFoundError returns true if the error indicates "not found".  It parses
// the error string looking for known values, which is imperfect but works in
// practice; and there's not much better we can do right now with k8s' dynamic client API
func isNotFoundError(err error) bool {
	msg := err.Error()
	return msg[len(msg)-len(notFound):] == notFound
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/main.go`
```go
package main

import (
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/sirupsen/logrus"
	"k8s.io/client-go/rest"
)

func main() {
	initLogrus()

	enableCertReload := flag.Bool("cert-reload", false, "enable certificate reload")
	v := flag.Bool("version", false, "show version")
	flag.Parse()

	if *v {
		fmt.Printf("windows-gmsa-webhook v%s\n", getVersion())
		os.Exit(0)
	}

	kubeClient, err := createKubeClient()
	if err != nil {
		panic(err)
	}

	randomHostname := env_bool("RANDOM_HOSTNAME")

	options := []WebhookOption{WithCertReload(*enableCertReload)}
	options = append(options, WithRandomHostname(randomHostname))

	webhook := newWebhookWithOptions(kubeClient, options...)

	tlsConfig := &tlsConfig{
		crtPath: env("TLS_CRT"),
		keyPath: env("TLS_KEY"),
	}

	port := env_int("HTTPS_PORT", 443)

	if err = webhook.start(port, tlsConfig, nil); err != nil {
		panic(err)
	}
}

var logLevels = map[string]logrus.Level{
	"panic": logrus.PanicLevel,
	"fatal": logrus.FatalLevel,
	"error": logrus.ErrorLevel,
	"warn":  logrus.WarnLevel,
	"info":  logrus.InfoLevel,
	"debug": logrus.DebugLevel,
	"trace": logrus.TraceLevel,
}

func initLogrus() {
	logrus.SetOutput(os.Stdout)

	logLevel := logrus.DebugLevel
	invalid := false

	rawLogLevel, present := os.LookupEnv("LOG_LEVEL")
	if present {
		if level, valid := logLevels[strings.ToLower(rawLogLevel)]; valid {
			logLevel = level
		} else {
			invalid = true
		}
	}

	logrus.SetLevel(logLevel)

	if invalid {
		keys := make([]string, len(logLevels))
		i := 0
		for key := range logLevels {
			keys[i] = key
			i++
		}
		logrus.Warningf("Unknown log level %s, valid log levels are: %v", rawLogLevel, strings.Join(keys, ", "))
	}
}

func createKubeClient() (*kubeClient, error) {
	config, err := rest.InClusterConfig()
	if err != nil {
		return nil, err
	}

	config.QPS = env_float("QPS", rest.DefaultQPS)
	config.Burst = env_int("BURST", rest.DefaultBurst)
	logrus.Infof("QPS: %f, Burst: %d", config.QPS, config.Burst)

	return newKubeClient(config)
}

func env_float(key string, defaultFloat float32) float32 {
	if v, found := os.LookupEnv(key); found {
		if i, err := strconv.ParseFloat(v, 32); err == nil {
			return float32(i)
		}
		logrus.Warningf("unable to parse environment variable %s with value %s; using default value %f", key, v, defaultFloat)
	}

	return defaultFloat
}

func env_bool(key string) bool {
	if v, found := os.LookupEnv(key); found {
		// Convert string to bool
		if boolValue, err := strconv.ParseBool(v); err == nil {
			return boolValue
		}
		// throw error if unable to parse
		panic(fmt.Errorf("unable to parse environment variable %s with value %s to bool", key, v))
	}

	// return bool default value: false
	return false
}

func env_int(key string, defaultInt int) int {
	if v, found := os.LookupEnv(key); found {
		if i, err := strconv.Atoi(v); err == nil {
			return i
		}
		logrus.Warningf("unable to parse environment variable %s with value %s; using default value %d", key, v, defaultInt)
	}

	return defaultInt
}

func env(key string) string {
	if value, found := os.LookupEnv(key); found {
		return value
	}
	panic(fmt.Errorf("%s env var not found", key))
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/main_test.go`
```go
package main

import (
	"fmt"
	"os"
	"testing"
)

func Test_env_float(t *testing.T) {
	defaultFloat := float32(5.0)
	tests := []struct {
		name   string
		envkey string
		envval string
		want   float32
	}{
		{
			name:   "Environment variable set to valid float",
			envkey: "TEST_ENV_FLOAT",
			envval: "3.14",
			want:   3.14,
		},
		{
			name:   "Environment variable set to invalid float",
			envkey: "TEST_ENV_FLOAT",
			envval: "invalid",
			want:   float32(defaultFloat),
		},
		{
			name:   "Environment variable not set",
			envkey: "TEST_ENV_FLOAT",
			envval: "",
			want:   float32(defaultFloat),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if tt.envval != "" {
				os.Setenv(tt.envkey, tt.envval)
			} else {
				os.Unsetenv(tt.envkey)
			}
			if got := env_float(tt.envkey, defaultFloat); got != tt.want {
				t.Errorf("env_float() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_env_int(t *testing.T) {
	defaultInt := 5
	tests := []struct {
		name   string
		envkey string
		envval string
		want   int
	}{
		{
			name:   "Environment variable set to valid int",
			envkey: "TEST_ENV_INT",
			envval: "10",
			want:   10,
		},
		{
			name:   "Environment variable set to invalid int",
			envkey: "TEST_ENV_INT",
			envval: "invalid",
			want:   defaultInt,
		},
		{
			name:   "Environment variable not set",
			envkey: "TEST_ENV_INT",
			envval: "",
			want:   defaultInt,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if tt.envval != "" {
				os.Setenv(tt.envkey, tt.envval)
			} else {
				os.Unsetenv(tt.envkey)
			}
			if got := env_int(tt.envkey, defaultInt); got != tt.want {
				t.Errorf("env_int() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_env_bool(t *testing.T) {
	tests := []struct {
		name   string
		envkey string
		envval string
		want   bool
	}{
		{
			name:   "Environment variable set to true",
			envkey: "TEST_ENV_BOOL",
			envval: "true",
			want:   true,
		},
		{
			name:   "Environment variable set to false",
			envkey: "TEST_ENV_BOOL",
			envval: "false",
			want:   false,
		},
		{
			name:   "Environment variable not set",
			envkey: "TEST_ENV_BOOL",
			envval: "",
			want:   false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if tt.envval != "" {
				os.Setenv(tt.envkey, tt.envval)
			} else {
				os.Unsetenv(tt.envkey)
			}
			if got := env_bool(tt.envkey); got != tt.want {
				t.Errorf("env_bool() = %v, want %v", got, tt.want)
			}
		})
	}

	envkey := "TEST_ENV_BOOL"
	envVal := "invalid"
	// Test panic
	defer func() {
		if r := recover(); r == nil {
			t.Errorf("The code did not panic")
		} else {
			t.Logf("Recovered from panic: %v", r)
			if r.(error).Error() != fmt.Sprintf("unable to parse environment variable %s with value %s to bool", envkey, envVal) {
				t.Errorf("Unexpected panic message: %v", r)
			}
		}
	}()

	os.Setenv(envkey, envVal)
	env_bool("TEST_ENV_BOOL")
}

func TestMain(m *testing.M) {
	GenerateTestCertAndKey()
	code := m.Run() // run tests
	ClearTestdata()
	os.Exit(code)
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/run-ci.sh`
```bash
#!/usr/bin/env bash

## Runs the right Travis tests depending on the environment variables.
## Must stay in syncs with the build matrix from .travis.yml

set -e

# giving a unique name allows running locally with https://github.com/nektos/act
export CLUSTER_NAME="windows-gmsa-$GITHUB_JOB"
export KUBECTL="$GITHUB_WORKSPACE/admission-webhook/dev/kubectl-$CLUSTER_NAME"
export KUBECONFIG="$GITHUB_WORKSPACE/admission-webhook/dev/kubeconfig-$CLUSTER_NAME"

export K8S_GMSA_CHART="$GITHUB_WORKSPACE/charts/gmsa"

main() {
    case "$T" in
        unit)
            make unit_tests ;;
        integration)
            run_integration_tests ;;
        dry_run_deploy)
            run_dry_run_deploy ;;
        *)
            echo "Unknown test option: $T" && exit 1 ;;
    esac
}

run_integration_tests() {
    if [ "$WITHOUT_ENVSUBST" ] && [ -x "$(command -v envsubst)" ] && [[ "$GITHUB_ACTIONS" == "true" ]]; then
        echo "Removing envsubst"
        sudo rm -f "$(command -v envsubst)"
    fi

    export DEPLOYMENT_NAME=windows-gmsa-dev
    export NAMESPACE=windows-gmsa-dev

    if [[ "$DEPLOY_METHOD" == 'download' ]]; then
        export K8S_GMSA_DEPLOY_METHOD='download'

        if [ "$GITHUB_HEAD_REF" ]; then
            # GITHUB_HEAD_REF is only set if it's a pull request
            export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="$GITHUB_REPOSITORY"
            export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$GITHUB_SHA"
            echo "Running pull request: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
        else
            # not a pull request
            export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="kubernetes-sigs/windows-gmsa"
            export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$(git rev-parse HEAD)"
            echo "Running: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
        fi
    elif [[ "$DEPLOY_METHOD" == 'chart' ]]; then
       export K8S_GMSA_DEPLOY_METHOD='chart'
       echo "deploy method: $K8S_GMSA_DEPLOY_METHOD"
       if [ "$GITHUB_HEAD_REF" ]; then
           # GITHUB_HEAD_REF is only set if it's a pull request
           # Similar logic goes here, but installs the chart using the repo.
           export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="$GITHUB_REPOSITORY"
           export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$GITHUB_SHA"
           echo "Running pull request: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
       else
           # not a pull request
           # Installs the chart using the local copy.
           export K8S_GMSA_DEPLOY_DOWNLOAD_REPO="kubernetes-sigs/windows-gmsa"
           export K8S_GMSA_DEPLOY_DOWNLOAD_REV="$(git rev-parse HEAD)"
           echo "Running: $K8S_GMSA_DEPLOY_DOWNLOAD_REPO $K8S_GMSA_DEPLOY_DOWNLOAD_REV"
       fi
    fi

    
    if [ "$WITH_DEV_IMAGE" ]; then
        make integration_tests_with_dev_image

        # for good measure let's check that one can change and restart the webhook when using the dev image
        local BOGUS_VERSION='cannotbeavalidversion'

        local POD_NAME
        POD_NAME="$($KUBECTL -n "$NAMESPACE" get pod --selector=app=$DEPLOYMENT_NAME -o=jsonpath='{.items[0].metadata.name}')"
        $KUBECTL -n "$NAMESPACE" exec "$POD_NAME" -- go build -ldflags="-X main.version=$BOGUS_VERSION"
        $KUBECTL -n "$NAMESPACE" exec "$POD_NAME" -- service webhook restart

        local SERVICE_IP
        SERVICE_IP="$($KUBECTL -n $NAMESPACE get service $DEPLOYMENT_NAME -o=jsonpath='{.spec.clusterIP}')"

        local INFO_OUTPUT
        INFO_OUTPUT="$(docker exec "$CLUSTER_NAME-control-plane" curl -sk https://$SERVICE_IP/info)"

        if [[ "$INFO_OUTPUT" == *"$BOGUS_VERSION"* ]]; then
            echo -e "Output from /info does contain '$BOGUS_VERSION':\n$INFO_OUTPUT"
        else
            echo -e "Expected output from /info to contain '$BOGUS_VERSION', instead got:\n$INFO_OUTPUT"
            exit 1
        fi
    else
        if [[ "$DEPLOY_METHOD" == 'chart' ]]; then
            make integration_tests_chart
        else 
            make integration_tests
        fi
    fi
}

# performs a dry-run deploy and ensures no changes have been made to the cluster
run_dry_run_deploy() {
    make cluster_start

    wait_for_all_terminating_or_pending_k8s_resources || return $?

    local SNAPSHOT_DIR='k8s_snapshot'
    k8s_snapshot $SNAPSHOT_DIR/before

    KUBECTL=$KUBECTL ./deploy/deploy-gmsa-webhook.sh --file gmsa-webhook.yml --dry-run

    k8s_snapshot $SNAPSHOT_DIR/after

    diff $SNAPSHOT_DIR/{before,after}
}

# lists all API objects present on a k8s master node and saves them to the folder given as 1st argument
# that dir shouldn't exist prior to calling the function
k8s_snapshot() {
    local DIR="$1"
    [ "$DIR" ] && [ ! -d "$DIR" ] || return 1
    mkdir -p "$DIR"

    local RESOURCE OUTPUT
    for RESOURCE in $($KUBECTL api-resources -o name); do
        OUTPUT="$(list_k8s_resources "$RESOURCE")" || return $?
        echo "$OUTPUT" | sort > "$DIR/$RESOURCE"
    done
}

# lists all API objects of the given resource, with an optional JSON-path filter
list_k8s_resources() {
    local RESOURCE="$1"

    local FILTER
    if [ "$2" ]; then
        FILTER="?(@.$2)"
    else
        FILTER='*'
    fi

    local OUTPUT EXIT_STATUS=0

    # this output is guaranteed to be unique since namespaces can't contain spaces
    OUTPUT="$($KUBECTL get "$RESOURCE" --all-namespaces -o jsonpath="{range .items[$FILTER]}{@.metadata.namespace}{\" \"}{@.metadata.name}{\"\n\"}{end}" 2>&1)" \
        || EXIT_STATUS=$?

    if [[ "$OUTPUT" == *'deprecated'* ]]; then
        # component status is deprecated in 1.19 and fails https://github.com/kubernetes-sigs/kind/issues/1998
        return 0
    elif [[ $EXIT_STATUS == 0 ]]; then
        echo "$OUTPUT"
        return 0
    elif [[ "$OUTPUT" == *'(NotFound)'* ]] || [[ "$OUTPUT" == *'(MethodNotAllowed)'* ]]; then
        return 0
    else
        echo "Error when listing k8s resource $RESOURCE: $OUTPUT" 1>&2
        return $EXIT_STATUS
    fi
}

# waits for all API objects in "Terminating" or "Pending" state to go away,
# for up to 120 secs per resource type
wait_for_all_terminating_or_pending_k8s_resources() {
    local RESOURCE
    for RESOURCE in $($KUBECTL api-resources -o name); do
        wait_until_no_k8s_resources_in_state "$RESOURCE" 'Terminating' || return $?
        wait_until_no_k8s_resources_in_state "$RESOURCE" 'Pending' || return $?
    done
}

# waits up to 60 seconds for API objects of the given resource that are
# in the given state to go away, else errors out
wait_until_no_k8s_resources_in_state() {
    local RESOURCE="$1"
    local STATE="$2"

    local START="$(date -u +%s)" OUTPUT

    while [ "$(( $(date -u +%s) - $START ))" -le 60 ]; do
        OUTPUT="$(list_k8s_resources "$RESOURCE" 'status.phase=="'$STATE'"')" || return $?
        if [ "$OUTPUT" ]; then
            # there still are resources in the given state
            echo "still waiting on $RESOURCE $OUTPUT"
            sleep 1
            continue
        fi
        return 0
    done

    echo -e "Timed out waiting for all $STATE $RESOURCE to go away:\n$OUTPUT"
    return 1
}

main "$@"
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/types.go`
```go
package main

import "context"

type tlsConfig struct {
	crtPath string
	keyPath string
}

type kubeClientInterface interface {
	isAuthorizedToUseCredSpec(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string)
	retrieveCredSpecContents(ctx context.Context, credSpecName string) (contents string, httpCode int, err error)
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/utils_test.go`
```go
package main

import (
	"context"
	crand "crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"crypto/x509/pkix"
	"encoding/pem"
	"math/big"
	"math/rand"
	"os"
	"time"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

const dummyCredSpecName = "dummy-cred-spec-name"

const dummyCredSpecContents = `{"We don't need no": ["education", "thought control", "dark sarcasm in the classroom"], "All in all you're just another": {"brick": "in", "the": "wall"}}`
const dummyServiceAccoutName = "dummy-service-account-name"
const dummyNamespace = "dummy-namespace"
const dummyPodName = "dummy-pod-name"
const dummyContainerName = "dummy-container-name"

type dummyKubeClient struct {
	isAuthorizedToUseCredSpecFunc func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string)
	retrieveCredSpecContentsFunc  func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error)
}

func (dkc *dummyKubeClient) isAuthorizedToUseCredSpec(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
	if dkc.isAuthorizedToUseCredSpecFunc != nil {
		return dkc.isAuthorizedToUseCredSpecFunc(ctx, serviceAccountName, namespace, credSpecName)
	}
	authorized = true
	return
}

func (dkc *dummyKubeClient) retrieveCredSpecContents(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
	if dkc.retrieveCredSpecContentsFunc != nil {
		return dkc.retrieveCredSpecContentsFunc(ctx, credSpecName)
	}
	contents = dummyCredSpecContents
	return
}

func buildWindowsOptions(credSpecName, credSpecContents string) *corev1.WindowsSecurityContextOptions {
	winOptions := &corev1.WindowsSecurityContextOptions{}
	setWindowsOptions(winOptions, credSpecName, credSpecContents)
	return winOptions
}

func setWindowsOptions(winOptions *corev1.WindowsSecurityContextOptions, credSpecName, credSpecContents string) {
	if credSpecName != "" {
		winOptions.GMSACredentialSpecName = &credSpecName
	}
	if credSpecContents != "" {
		winOptions.GMSACredentialSpec = &credSpecContents
	}
}

// buildPod builds a pod for unit tests.
// `podWindowsOptions` should be either a full `*corev1.WindowsSecurityContextOptions` or a string, in which
// case a `*corev1.WindowsSecurityContextOptions` is built using that string as the name of the cred spec to use.
// Same goes for the values of `containerNamesAndWindowsOptions`.
func buildPod(serviceAccountName string, podWindowsOptions *corev1.WindowsSecurityContextOptions, containerNamesAndWindowsOptions map[string]*corev1.WindowsSecurityContextOptions) *corev1.Pod {
	return buildPodWithHostName(serviceAccountName, nil, podWindowsOptions, containerNamesAndWindowsOptions)
}

// buildPod builds a pod for unit tests.
// `podWindowsOptions` should be either a full `*corev1.WindowsSecurityContextOptions` or a string, in which
// case a `*corev1.WindowsSecurityContextOptions` is built using that string as the name of the cred spec to use.
// Same goes for the values of `containerNamesAndWindowsOptions`.
func buildPodWithHostName(serviceAccountName string, hostname *string, podWindowsOptions *corev1.WindowsSecurityContextOptions, containerNamesAndWindowsOptions map[string]*corev1.WindowsSecurityContextOptions) *corev1.Pod {
	containers := make([]corev1.Container, len(containerNamesAndWindowsOptions))
	i := 0
	for name, winOptions := range containerNamesAndWindowsOptions {
		containers[i] = corev1.Container{Name: name}
		if winOptions != nil {
			containers[i].SecurityContext = &corev1.SecurityContext{WindowsOptions: winOptions}
		}
		i++
	}

	shuffleContainers(containers)

	podSpec := corev1.PodSpec{
		ServiceAccountName: serviceAccountName,
		Containers:         containers,
	}

	if hostname != nil {
		podSpec.Hostname = *hostname
	}

	if podWindowsOptions != nil {
		podSpec.SecurityContext = &corev1.PodSecurityContext{WindowsOptions: podWindowsOptions}
	}

	return &corev1.Pod{
		ObjectMeta: metav1.ObjectMeta{Name: dummyPodName},
		Spec:       podSpec,
	}
}

func shuffleContainers(a []corev1.Container) {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	for i := len(a) - 1; i > 0; i-- {
		j := r.Int() % (i + 1)
		tmp := a[j]
		a[j] = a[i]
		a[i] = tmp
	}
}

func GenerateTestCertAndKey() {
	// Generate a 2048-bit RSA private key
	priv, err := rsa.GenerateKey(crand.Reader, 2048)
	if err != nil {
		panic(err)
	}

	// Create a certificate template
	certTemplate := &x509.Certificate{
		SerialNumber: big.NewInt(1),
		Subject: pkix.Name{
			Organization: []string{"test"},
		},
		NotBefore:             time.Now(),
		NotAfter:              time.Now().AddDate(1, 0, 0), // Valid for 1 year
		KeyUsage:              x509.KeyUsageKeyEncipherment | x509.KeyUsageDigitalSignature,
		ExtKeyUsage:           []x509.ExtKeyUsage{x509.ExtKeyUsageServerAuth},
		BasicConstraintsValid: true,
	}

	// Create the certificate
	certDER, err := x509.CreateCertificate(crand.Reader, certTemplate, certTemplate, &priv.PublicKey, priv)
	if err != nil {
		panic(err)
	}

	err = os.Mkdir("testdata", 0755)
	if err != nil {
		panic(err)
	}

	// Write the certificate to a PEM file
	certFile, err := os.Create("testdata/cert.pem")
	if err != nil {
		panic(err)
	}
	pem.Encode(certFile, &pem.Block{Type: "CERTIFICATE", Bytes: certDER})
	certFile.Close()

	// Write the private key to a PEM file
	keyFile, err := os.Create("testdata/key.pem")
	if err != nil {
		panic(err)
	}
	keyBytes := x509.MarshalPKCS1PrivateKey(priv)
	pem.Encode(keyFile, &pem.Block{Type: "RSA PRIVATE KEY", Bytes: keyBytes})
	keyFile.Close()
}

func ClearTestdata() {
	os.RemoveAll("testdata")
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/version.go`
```go
package main

var version string

func getVersion() string {
	if version == "" {
		return "unknown"
	}

	return version
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/webhook.go`
```go
package main

import (
	"context"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"reflect"
	"strconv"
	"strings"
	"time"

	"github.com/google/uuid"

	"github.com/sirupsen/logrus"
	admissionV1 "k8s.io/api/admission/v1"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime"
)

type webhookOperation string

type gmsaResourceKind string

const (
	contentTypeHeader = "Content-Type"
	jsonContentType   = "application/json"

	validate webhookOperation = "VALIDATE"
	mutate   webhookOperation = "MUTATE"

	podKind       gmsaResourceKind = "pod"
	containerKind gmsaResourceKind = "container"
)

type webhook struct {
	server *http.Server
	client kubeClientInterface
	config *WebhookConfig
}

type podAdmissionError struct {
	error
	code int
	pod  *corev1.Pod
}

type WebhookConfig struct {
	EnableCertReload     bool
	EnableRandomHostName bool
}

type WebhookOption func(*WebhookConfig)

func WithCertReload(enabled bool) WebhookOption {
	return func(cfg *WebhookConfig) {
		cfg.EnableCertReload = enabled
	}
}

func WithRandomHostname(enabled bool) WebhookOption {
	return func(cfg *WebhookConfig) {
		cfg.EnableRandomHostName = enabled
	}
}

func newWebhook(client kubeClientInterface) *webhook {
	return newWebhookWithOptions(client)
}

func newWebhookWithOptions(client kubeClientInterface, options ...WebhookOption) *webhook {
	config := &WebhookConfig{EnableCertReload: false, EnableRandomHostName: false}

	for _, option := range options {
		option(config)
	}

	return &webhook{
		client: client,
		config: config,
	}
}

// start is a blocking call.
// If passed a listeningChan, it will close it when it's started listening
func (webhook *webhook) start(port int, tlsConfig *tlsConfig, listeningChan chan interface{}) error {
	if webhook.server != nil {
		return fmt.Errorf("webhook already started")
	}

	webhook.server = &http.Server{
		Addr:    ":" + strconv.Itoa(port),
		Handler: webhook,
	}

	logrus.Infof("starting webhook server at port %v", port)
	listener, err := net.Listen("tcp", webhook.server.Addr)
	if err != nil {
		return err
	}
	defer listener.Close()
	keepAliveListener := tcpKeepAliveListener{listener.(*net.TCPListener)}

	if listeningChan != nil {
		close(listeningChan)
	}

	if tlsConfig == nil {
		err = webhook.server.Serve(keepAliveListener)
	} else {
		if webhook.config.EnableCertReload {
			logrus.Infof("Webhook certificate reload enabled")
			certReloader := NewCertReloader(tlsConfig.crtPath, tlsConfig.keyPath)
			_, err = certReloader.LoadCertificate()
			if err != nil {
				return err
			}

			go watchCertFiles(context.Background(), certReloader)

			webhook.server.TLSConfig = &tls.Config{
				GetCertificate: certReloader.GetCertificateFunc(),
			}

			err = webhook.server.ServeTLS(keepAliveListener, "", "")
		} else {
			err = webhook.server.ServeTLS(keepAliveListener, tlsConfig.crtPath, tlsConfig.keyPath)
		}
	}

	if err != nil {
		if err == http.ErrServerClosed {
			logrus.Infof("server closed")
		} else {
			return err
		}
	}

	return nil
}

// stop stops the HTTP server.
func (webhook *webhook) stop() error {
	if webhook.server == nil {
		return fmt.Errorf("webhook server not started yet")
	}
	return webhook.server.Shutdown(context.Background())
}

// ServeHTTP makes this object a http.Handler; its job is handling the HTTP routing: paths,
// methods and content-type headers.
// Since we only have a handful of endpoints, there's no need for a full-fledged router here.
func (webhook *webhook) ServeHTTP(responseWriter http.ResponseWriter, request *http.Request) {
	var operation webhookOperation

	switch request.URL.Path {
	case "/validate":
		operation = validate
	case "/mutate":
		operation = mutate
	case "/info":
		writeJSONBody(responseWriter, map[string]string{"version": getVersion()})
		return
	case "/health":
		responseWriter.WriteHeader(http.StatusNoContent)
		return
	default:
		abortHTTPRequest(responseWriter, http.StatusNotFound, "received %s request for unknown path %s", request.Method, request.URL.Path)
		return
	}

	// should be a POST request
	if strings.ToUpper(request.Method) != "POST" {
		abortHTTPRequest(responseWriter, http.StatusMethodNotAllowed, "expected POST HTTP request, got a %s %s request", request.Method, operation)
		return
	}
	// verify the content type is JSON
	if contentType := request.Header.Get(contentTypeHeader); contentType != jsonContentType {
		abortHTTPRequest(responseWriter, http.StatusUnsupportedMediaType, "expected JSON content-type header for %s request, got %q", operation, contentType)
		return
	}

	admissionResponse := webhook.httpRequestToAdmissionResponse(request, operation)
	responseAdmissionReview := admissionV1.AdmissionReview{
		TypeMeta: metav1.TypeMeta{
			Kind:       "AdmissionReview",
			APIVersion: "admission.k8s.io/v1",
		},
		Response: admissionResponse,
	}

	writeJSONBody(responseWriter, responseAdmissionReview)
}

// abortHTTPRequest is called for low-level HTTP errors (routing or writing the body)
func abortHTTPRequest(responseWriter http.ResponseWriter, httpCode int, logMsg string, logArs ...interface{}) {
	logrus.Infof(logMsg, logArs...)
	responseWriter.WriteHeader(httpCode)
}

// writeJsonBody writes a JSON object to an HTTP response.
func writeJSONBody(responseWriter http.ResponseWriter, jsonBody interface{}) {
	if responseBytes, err := json.Marshal(jsonBody); err == nil {
		logrus.Debugf("sending response: %s", responseBytes)

		responseWriter.Header().Set(contentTypeHeader, jsonContentType)
		if _, err = responseWriter.Write(responseBytes); err != nil {
			abortHTTPRequest(responseWriter, http.StatusInternalServerError, "error when writing response JSON %s: %v", responseBytes, err)
		}
	} else {
		abortHTTPRequest(responseWriter, http.StatusInternalServerError, "error when marshalling response %v: %v", jsonBody, err)
	}
}

// httpRequestToAdmissionResponse turns a raw HTTP request into an AdmissionResponse struct.
func (webhook *webhook) httpRequestToAdmissionResponse(request *http.Request, operation webhookOperation) *admissionV1.AdmissionResponse {
	// read the body
	if request.Body == nil {
		deniedAdmissionResponse(fmt.Errorf("no request body"), http.StatusBadRequest)
	}
	body, err := ioutil.ReadAll(request.Body)
	if err != nil {
		return deniedAdmissionResponse(fmt.Errorf("couldn't read request body: %v", err), http.StatusBadRequest)
	}
	defer request.Body.Close()

	logrus.Debugf("handling %s request: %s", operation, body)

	// unmarshall the request
	admissionReview := admissionV1.AdmissionReview{}
	if err = json.Unmarshal(body, &admissionReview); err != nil {
		return deniedAdmissionResponse(fmt.Errorf("unable to unmarshall JSON body as an admission review: %v", err), http.StatusBadRequest)
	}
	if admissionReview.Request == nil {
		return deniedAdmissionResponse(fmt.Errorf("no 'Request' field in JSON body"), http.StatusBadRequest)
	}

	admissionResponse, admissionError := webhook.validateOrMutate(request.Context(), admissionReview.Request, operation)
	if admissionError != nil {
		admissionResponse = deniedAdmissionResponse(admissionError)
	}

	// return the same UID
	admissionResponse.UID = admissionReview.Request.UID

	return admissionResponse
}

// validateOrMutate is where the non-HTTP-related work happens.
func (webhook *webhook) validateOrMutate(ctx context.Context, request *admissionV1.AdmissionRequest, operation webhookOperation) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	if request.Kind.Kind != "Pod" {
		return nil, &podAdmissionError{error: fmt.Errorf("expected a Pod object, got a %v", request.Kind.Kind), code: http.StatusBadRequest}
	}

	pod, err := unmarshallPod(request.Object)
	if err != nil {
		return nil, err
	}

	switch request.Operation {
	case admissionV1.Create:
		switch operation {
		case validate:
			return webhook.validateCreateRequest(ctx, pod, request.Namespace)
		case mutate:
			return webhook.mutateCreateRequest(ctx, pod)
		default:
			// shouldn't happen, but needed so that all paths in the function have a return value
			panic(fmt.Errorf("unexpected webhook operation: %v", operation))
		}

	case admissionV1.Update:
		if operation == validate {
			oldPod, err := unmarshallPod(request.OldObject)
			if err != nil {
				return nil, err
			}
			return validateUpdateRequest(pod, oldPod)
		}

		// we only do validation on updates, no mutation
		return &admissionV1.AdmissionResponse{Allowed: true}, nil
	default:
		return nil, &podAdmissionError{error: fmt.Errorf("unpexpected operation %s", request.Operation), pod: pod, code: http.StatusBadRequest}
	}
}

// unmarshallPod unmarshalls a pod object from its raw JSON representation.
func unmarshallPod(object runtime.RawExtension) (*corev1.Pod, *podAdmissionError) {
	pod := &corev1.Pod{}
	if err := json.Unmarshal(object.Raw, pod); err != nil {
		return nil, &podAdmissionError{error: fmt.Errorf("unable to unmarshall pod JSON object: %v", err), code: http.StatusBadRequest}
	}

	return pod, nil
}

// validateCreateRequest ensures that the GMSA contents set in the pod's spec
// match the corresponding GMSA names, and that the pod's service account
// is authorized to `use` the requested GMSA's.
func (webhook *webhook) validateCreateRequest(ctx context.Context, pod *corev1.Pod, namespace string) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	if err := iterateOverWindowsSecurityOptions(pod, func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, _ int) *podAdmissionError {
		if credSpecName := windowsOptions.GMSACredentialSpecName; credSpecName != nil {
			// let's check that the associated service account can read the relevant cred spec CRD
			if authorized, reason := webhook.client.isAuthorizedToUseCredSpec(ctx, pod.Spec.ServiceAccountName, namespace, *credSpecName); !authorized {
				msg := fmt.Sprintf("service account %q is not authorized to `use` GMSA cred spec %q", pod.Spec.ServiceAccountName, *credSpecName)
				if reason != "" {
					msg += fmt.Sprintf(", reason: %q", reason)
				}
				return &podAdmissionError{error: fmt.Errorf(msg), pod: pod, code: http.StatusForbidden}
			}

			// and the contents should match the ones contained in the GMSA resource with that name
			if credSpecContents := windowsOptions.GMSACredentialSpec; credSpecContents != nil {
				if expectedContents, code, retrieveErr := webhook.client.retrieveCredSpecContents(ctx, *credSpecName); retrieveErr != nil {
					return &podAdmissionError{error: retrieveErr, pod: pod, code: code}
				} else if specsEqual, compareErr := compareCredSpecContents(*credSpecContents, expectedContents); !specsEqual || compareErr != nil {
					msg := fmt.Sprintf("the GMSA cred spec contents for %s %q does not match the contents of GMSA resource %q", resourceKind, resourceName, *credSpecName)
					if compareErr != nil {
						msg += fmt.Sprintf(": %v", compareErr)
					}
					return &podAdmissionError{error: fmt.Errorf(msg), pod: pod, code: http.StatusUnprocessableEntity}
				}
			}
		} else if windowsOptions.GMSACredentialSpec != nil {
			// the GMSA's name is not set, but the contents are
			msg := fmt.Sprintf("%s %q has a GMSA cred spec set, but does not define the name of the corresponding resource", resourceKind, resourceName)
			return &podAdmissionError{error: fmt.Errorf(msg), pod: pod, code: http.StatusUnprocessableEntity}
		}

		return nil
	}); err != nil {
		return nil, err
	}

	return &admissionV1.AdmissionResponse{Allowed: true}, nil
}

// compareCredSpecContents returns true iff the two strings represent the same credential spec contents.
func compareCredSpecContents(fromResource, fromCRD string) (bool, error) {
	// this is actually what happens almost all the time, when users don't set the GMSA contents directly
	// but instead rely on the mutating webhook to do that for them; and in that case no need for a slow
	// JSON parsing and comparison
	if fromResource == fromCRD {
		return true, nil
	}

	var (
		jsonObjectFromResource map[string]interface{}
		jsonObjectFromCRD      map[string]interface{}
	)

	if err := json.Unmarshal([]byte(fromResource), &jsonObjectFromResource); err != nil {
		return false, fmt.Errorf("unable to parse %q as a JSON object: %v", fromResource, err)
	}
	if err := json.Unmarshal([]byte(fromCRD), &jsonObjectFromCRD); err != nil {
		return false, fmt.Errorf("unable to parse CRD %q as a JSON object: %v", fromCRD, err)
	}

	return reflect.DeepEqual(jsonObjectFromResource, jsonObjectFromCRD), nil
}

// mutateCreateRequest inlines the requested GMSA's into the pod's and containers' `WindowsSecurityOptions` structs.
func (webhook *webhook) mutateCreateRequest(ctx context.Context, pod *corev1.Pod) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	var patches []map[string]string
	hasGMSA := false

	if err := iterateOverWindowsSecurityOptions(pod, func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, containerIndex int) *podAdmissionError {
		if credSpecName := windowsOptions.GMSACredentialSpecName; credSpecName != nil {
			hasGMSA = true
			// if the user has pre-set the GMSA's contents, we won't override it - it'll be down
			// to the validation endpoint to make sure the contents actually are what they should
			if credSpecContents := windowsOptions.GMSACredentialSpec; credSpecContents == nil {
				contents, code, retrieveErr := webhook.client.retrieveCredSpecContents(ctx, *credSpecName)
				if retrieveErr != nil {
					return &podAdmissionError{error: retrieveErr, pod: pod, code: code}
				}

				partialPath := ""
				if resourceKind == containerKind {
					partialPath = fmt.Sprintf("/containers/%d", containerIndex)
				}

				// worth noting that this JSON patch is guaranteed to work since we know at this point
				// that the resource comprises a `windowsOptions` object, and and that it doesn't have a
				// "gmsaCredentialSpec" field
				patches = append(patches, map[string]string{
					"op":    "add",
					"path":  fmt.Sprintf("/spec%s/securityContext/windowsOptions/gmsaCredentialSpec", partialPath),
					"value": contents,
				})
			}
		}

		return nil
	}); err != nil {
		return nil, err
	}

	if hasGMSA && webhook.config.EnableRandomHostName {
		// Pods are GMSA related, Env enabled, patch the hostname only if it is empty
		hostName := pod.Spec.Hostname
		if hostName == "" {
			hostName = generateUUID()
			patches = append(patches, map[string]string{
				"op":    "add",
				"path":  "/spec/hostname",
				"value": hostName,
			})
		} else {
			// Will honor the hostname set in the spec, print out a message
			logrus.Warnf("hostname is set in spec and will be hornored instead of being randomized")
		}
	}

	admissionResponse := &admissionV1.AdmissionResponse{Allowed: true}
	if len(patches) != 0 {
		patchesBytes, err := json.Marshal(patches)
		if err != nil {
			return nil, &podAdmissionError{error: fmt.Errorf("unable to marshall patch JSON %v: %v", patches, err), pod: pod, code: http.StatusInternalServerError}
		}

		admissionResponse.Patch = patchesBytes
		patchType := admissionV1.PatchTypeJSONPatch
		admissionResponse.PatchType = &patchType
	}

	return admissionResponse, nil
}

// validateUpdateRequest ensures that there are no updates to any of the GMSA names or contents.
func validateUpdateRequest(pod, oldPod *corev1.Pod) (*admissionV1.AdmissionResponse, *podAdmissionError) {
	var oldPodContainerOptions map[string]*corev1.WindowsSecurityContextOptions

	if err := iterateOverWindowsSecurityOptions(pod, func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, _ int) *podAdmissionError {
		var oldWindowsOptions *corev1.WindowsSecurityContextOptions
		if resourceKind == podKind {
			if oldPod.Spec.SecurityContext != nil {
				oldWindowsOptions = oldPod.Spec.SecurityContext.WindowsOptions
			}
		} else {
			// it's a container; look for the same container in the old pod,
			// lazily building the map of container names to security options if needed
			if oldPodContainerOptions == nil {
				oldPodContainerOptions = make(map[string]*corev1.WindowsSecurityContextOptions)
				iterateOverWindowsSecurityOptions(oldPod, func(winOpts *corev1.WindowsSecurityContextOptions, rsrcKind gmsaResourceKind, rsrcName string, _ int) *podAdmissionError {
					if rsrcKind == containerKind {
						oldPodContainerOptions[rsrcName] = winOpts
					}
					return nil
				})
			}

			oldWindowsOptions = oldPodContainerOptions[resourceName]
		}

		if oldWindowsOptions == nil {
			oldWindowsOptions = &corev1.WindowsSecurityContextOptions{}
		}

		var modifiedFieldNames []string
		if !equalStringPointers(windowsOptions.GMSACredentialSpecName, oldWindowsOptions.GMSACredentialSpecName) {
			modifiedFieldNames = append(modifiedFieldNames, "name")
		}
		if !equalStringPointers(windowsOptions.GMSACredentialSpec, oldWindowsOptions.GMSACredentialSpec) {
			modifiedFieldNames = append(modifiedFieldNames, "contents")
		}

		if len(modifiedFieldNames) != 0 {
			msg := fmt.Errorf("cannot update an existing pod's GMSA settings (GMSA %s modified on %s %q)", strings.Join(modifiedFieldNames, " and "), resourceKind, resourceName)
			return &podAdmissionError{error: msg, pod: pod, code: http.StatusForbidden}
		}

		return nil
	}); err != nil {
		return nil, err
	}

	return &admissionV1.AdmissionResponse{Allowed: true}, nil
}

func equalStringPointers(s1, s2 *string) bool {
	if s1 == nil {
		return s2 == nil
	}
	if s2 == nil {
		return false
	}
	return *s1 == *s2
}

// iterateOverWindowsSecurityOptions calls `f` on the pod's `.Spec.SecurityContext.WindowsOptions` field,
// as well as over each of its container's `.SecurityContext.WindowsOptions` field.
// `f` can assume it only gets called with non-nil `WindowsSecurityOptions` pointers; the other
// arguments give information on the resource owning that pointer - in particular, if that
// resource is a container, `containerIndex` is the index of the container in the spec's list (-1 for pods).
// If `f` returns an error, that breaks the loop, and the error is bubbled up.
func iterateOverWindowsSecurityOptions(pod *corev1.Pod, f func(windowsOptions *corev1.WindowsSecurityContextOptions, resourceKind gmsaResourceKind, resourceName string, containerIndex int) *podAdmissionError) *podAdmissionError {
	if pod.Spec.SecurityContext != nil && pod.Spec.SecurityContext.WindowsOptions != nil {
		if err := f(pod.Spec.SecurityContext.WindowsOptions, podKind, pod.Name, -1); err != nil {
			return err
		}
	}

	for i, container := range pod.Spec.Containers {
		if container.SecurityContext != nil && container.SecurityContext.WindowsOptions != nil {
			if err := f(container.SecurityContext.WindowsOptions, containerKind, container.Name, i); err != nil {
				return err
			}
		}
	}

	return nil
}

// deniedAdmissionResponse is a helper function to create an AdmissionResponse
// with an embedded error.
func deniedAdmissionResponse(err error, httpCode ...int) *admissionV1.AdmissionResponse {
	var code int
	logMsg := "refusing to admit"

	if admissionError, ok := err.(*podAdmissionError); ok {
		code = admissionError.code
		if admissionError.pod != nil {
			logMsg += fmt.Sprintf(" pod %+v", admissionError.pod)
		}
	}

	if len(httpCode) > 0 {
		code = httpCode[0]
	}

	if code != 0 {
		logMsg += fmt.Sprintf(" with code %v", code)
	}

	logrus.Infof("%s: %v", logMsg, err)

	return &admissionV1.AdmissionResponse{
		Allowed: false,
		Result: &metav1.Status{
			Message: err.Error(),
			Code:    int32(code),
		},
	}
}

// stolen from https://github.com/golang/go/blob/go1.12/src/net/http/server.go#L3255-L3271
type tcpKeepAliveListener struct {
	*net.TCPListener
}

func (ln tcpKeepAliveListener) Accept() (net.Conn, error) {
	tc, err := ln.AcceptTCP()
	if err != nil {
		return nil, err
	}
	tc.SetKeepAlive(true)
	tc.SetKeepAlivePeriod(3 * time.Minute)
	return tc, nil
}

func generateUUID() string {
	// Generate a new UUID
	id := uuid.New()
	// Convert to string and get the first 15 characters in lower case
	shortUUID := strings.ToLower(id.String()[:15])
	return shortUUID
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/webhook_http_test.go`
```go
package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	admissionV1 "k8s.io/api/admission/v1"
	authenticationv1 "k8s.io/api/authentication/v1"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/apimachinery/pkg/types"
)

// this is just a quick-and-dirty test to ensure the HTTP server works. E2e/integration tests explore
// this much further.
func TestHTTPWebhook(t *testing.T) {
	var requestUID types.UID = "283f4877-34d4-11e9-a9f1-06da3a0adce4"

	pod := buildPod(dummyServiceAccoutName, buildWindowsOptions(dummyCredSpecName, ""), map[string]*corev1.WindowsSecurityContextOptions{"container-name": nil})

	admissionRequest := &admissionV1.AdmissionReview{
		Request: &admissionV1.AdmissionRequest{
			UID: requestUID,
			Kind: metav1.GroupVersionKind{
				Version: "v1",
				Kind:    "Pod",
			},
			Resource: metav1.GroupVersionResource{
				Version:  "v1",
				Resource: "pods",
			},
			Namespace: dummyNamespace,
			Operation: admissionV1.Create,
			UserInfo: authenticationv1.UserInfo{
				Username: "system:serviceaccount:kube-system:replicaset-controller",
				UID:      "cb335ac0-34b4-11e9-9745-06da3a0adce4",
				Groups:   []string{"system:serviceaccounts", "system:serviceaccounts:kube-system"},
			},
			Object: runtime.RawExtension{
				Object: pod,
			},
		},
	}

	authorizedToUseCredSpec := true

	kubeClient := &dummyKubeClient{
		isAuthorizedToUseCredSpecFunc: func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
			assert.Equal(t, dummyServiceAccoutName, serviceAccountName)
			assert.Equal(t, dummyNamespace, namespace)
			assert.Equal(t, dummyCredSpecName, credSpecName)

			return authorizedToUseCredSpec, "bogus reason"
		},
		retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
			assert.Equal(t, dummyCredSpecName, credSpecName)

			contents = dummyCredSpecContents
			return
		},
	}

	t.Run("success path", func(t *testing.T) {
		port, tearDownHTTP := startHTTPServer(t, kubeClient)
		defer tearDownHTTP()

		httpCode, response := makeHTTPRequest(t, port, "POST", "mutate", admissionRequest)
		assert.Equal(t, http.StatusOK, httpCode)
		require.NotNil(t, response)
		require.NotNil(t, response.Response)

		assert.Equal(t, requestUID, response.Response.UID)
		assert.True(t, response.Response.Allowed)

		if assert.NotNil(t, response.Response.PatchType) {
			assert.Equal(t, admissionV1.PatchTypeJSONPatch, *response.Response.PatchType)
		}

		var patches []map[string]string
		if err := json.Unmarshal(response.Response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, 1, len(patches)) {
			expectedPatch := map[string]string{
				"op":    "add",
				"path":  "/spec/securityContext/windowsOptions/gmsaCredentialSpec",
				"value": dummyCredSpecContents,
			}
			assert.Equal(t, expectedPatch, patches[0])
		}
	})

	t.Run("failure", func(t *testing.T) {
		previousAuthorizedToUseCredSpec := authorizedToUseCredSpec
		authorizedToUseCredSpec = false
		defer func() { authorizedToUseCredSpec = previousAuthorizedToUseCredSpec }()

		port, tearDownHTTP := startHTTPServer(t, kubeClient)
		defer tearDownHTTP()

		httpCode, response := makeHTTPRequest(t, port, "POST", "validate", admissionRequest)
		assert.Equal(t, http.StatusOK, httpCode)
		require.NotNil(t, response)
		require.NotNil(t, response.Response)

		assert.Equal(t, requestUID, response.Response.UID)
		assert.False(t, response.Response.Allowed)

		require.NotNil(t, response.Response.Result)
		assert.Equal(t, int32(http.StatusForbidden), response.Response.Result.Code)
		expectedSubstr := fmt.Sprintf("service account %q is not authorized to `use` GMSA cred spec", dummyServiceAccoutName)
		assert.Contains(t, response.Response.Result.Message, expectedSubstr)
	})

	for _, path := range []string{"validate", "mutate"} {
		t.Run(fmt.Sprintf("wrong HTTP method for %s", path), func(t *testing.T) {
			port, tearDownHTTP := startHTTPServer(t, kubeClient)
			defer tearDownHTTP()

			httpCode, response := makeHTTPRequest(t, port, "PUT", path, admissionRequest)
			assert.Equal(t, http.StatusMethodNotAllowed, httpCode)
			assert.Nil(t, response)
		})

		t.Run(fmt.Sprintf("wrong content-type for %s", path), func(t *testing.T) {
			port, tearDownHTTP := startHTTPServer(t, kubeClient)
			defer tearDownHTTP()

			httpCode, response := makeHTTPRequest(t, port, "POST", path, admissionRequest, "content-type", "text/plain")
			assert.Equal(t, http.StatusUnsupportedMediaType, httpCode)
			assert.Nil(t, response)
		})

		t.Run(fmt.Sprintf("wrong object kind for %s", path), func(t *testing.T) {
			previousKind := admissionRequest.Request.Kind.Kind
			admissionRequest.Request.Kind.Kind = "Deployment"
			defer func() { admissionRequest.Request.Kind.Kind = previousKind }()

			port, tearDownHTTP := startHTTPServer(t, kubeClient)
			defer tearDownHTTP()

			httpCode, response := makeHTTPRequest(t, port, "POST", path, admissionRequest)
			assert.Equal(t, http.StatusOK, httpCode)
			require.NotNil(t, response)
			require.NotNil(t, response.Response)

			assert.Equal(t, requestUID, response.Response.UID)
			assert.False(t, response.Response.Allowed)

			require.NotNil(t, response.Response.Result)
			assert.Equal(t, int32(http.StatusBadRequest), response.Response.Result.Code)
			assert.Equal(t, "expected a Pod object, got a Deployment", response.Response.Result.Message)
		})
	}

	t.Run("wrong route", func(t *testing.T) {
		port, tearDownHTTP := startHTTPServer(t, kubeClient)
		defer tearDownHTTP()

		httpCode, response := makeHTTPRequest(t, port, "POST", "i_dont_exist", admissionRequest)
		assert.Equal(t, http.StatusNotFound, httpCode)
		assert.Nil(t, response)
	})
}

func TestStartHTTPWebhookWithCertReload(t *testing.T) {
	authorizedToUseCredSpec := true

	kubeClient := &dummyKubeClient{
		isAuthorizedToUseCredSpecFunc: func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
			assert.Equal(t, dummyServiceAccoutName, serviceAccountName)
			assert.Equal(t, dummyNamespace, namespace)
			assert.Equal(t, dummyCredSpecName, credSpecName)

			return authorizedToUseCredSpec, "bogus reason"
		},
		retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
			assert.Equal(t, dummyCredSpecName, credSpecName)

			contents = dummyCredSpecContents
			return
		},
	}

	webhook := newWebhookWithOptions(kubeClient, WithCertReload(true))
	port := getAvailablePort(t)
	tlsConfig := &tlsConfig{
		crtPath: "testdata/cert.pem",
		keyPath: "testdata/key.pem",
	}

	listeningChan := make(chan interface{})
	go func() {
		assert.Nil(t, webhook.start(port, tlsConfig, listeningChan))
	}()
	defer webhook.stop()

	select {
	case <-listeningChan:
		for {
			if webhook.server.TLSConfig != nil {
				break
			}
			time.Sleep(10 * time.Millisecond)
		}
		assert.NotNil(t, webhook.server.TLSConfig.GetCertificate)
	case <-time.After(5 * time.Second):
		t.Fatalf("Timed out waiting for HTTP server to start listening on %d", port)
	}
}

func startHTTPServer(t *testing.T, kubeClient *dummyKubeClient) (int, func()) {
	webhook := newWebhook(kubeClient)
	port := getAvailablePort(t)

	listeningChan := make(chan interface{})
	go func() {
		assert.Nil(t, webhook.start(port, nil, listeningChan))
	}()

	select {
	case <-listeningChan:
	case <-time.After(5 * time.Second):
		t.Fatalf("Timed out waiting for HTTP server to start listening on %d", port)
	}

	return port, func() {
		assert.Nil(t, webhook.stop())
	}
}

func makeHTTPRequest(t *testing.T, port int, method string, path string, admissionRequest *admissionV1.AdmissionReview, headers ...string) (httpCode int, admissionResponse *admissionV1.AdmissionReview) {
	require.Equal(t, 0, len(headers)%2, "header names and values should be provided in pairs")

	reqBody, err := json.Marshal(admissionRequest)
	require.Nil(t, err)

	url := fmt.Sprintf("http://localhost:%d/%s", port, path)
	req, err := http.NewRequest(method, url, bytes.NewBuffer(reqBody))
	require.Nil(t, err)

	i := 0
	for i < len(headers) {
		req.Header.Set(headers[i], headers[i+1])
		i += 2
	}
	if req.Header.Get("Content-Type") == "" {
		req.Header.Set("Content-Type", "application/json")
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	require.Nil(t, err)

	defer resp.Body.Close()
	respBody, err := ioutil.ReadAll(resp.Body)
	require.Nil(t, err)

	admissionResponse = &admissionV1.AdmissionReview{}
	if err := json.Unmarshal(respBody, admissionResponse); err != nil {
		admissionResponse = nil
	}

	return resp.StatusCode, admissionResponse
}

// getAvailablePort asks the kernel for an available port, that is ready to use.
func getAvailablePort(t *testing.T) int {
	addr, err := net.ResolveTCPAddr("tcp", "localhost:0")
	require.Nil(t, err)

	listen, err := net.ListenTCP("tcp", addr)
	require.Nil(t, err)

	defer listen.Close()
	return listen.Addr().(*net.TCPAddr).Port
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/webhook_test.go`
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	admissionV1 "k8s.io/api/admission/v1"
	corev1 "k8s.io/api/core/v1"
)

func TestValidateCreateRequest(t *testing.T) {
	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with empty GMSA settings": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with no GMSA settings": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			webhook := newWebhook(nil)
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		})
	}

	kubeClientFactory := func() *dummyKubeClient {
		return &dummyKubeClient{
			retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					contents = dummyCredSpecContents
				} else {
					contents = credSpecName + "-contents"
				}
				return
			},
		}
	}

	winOptionsFactory := func(containerName string) *corev1.WindowsSecurityContextOptions {
		return buildWindowsOptions(containerName+"-cred-spec", containerName+"-cred-spec-contents")
	}

	runWebhookValidateOrMutateTests(t, winOptionsFactory, map[string]webhookValidateOrMutateTest{
		"with matching name & content, it passes": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		},

		"if the cred spec contents are not byte-to-byte equal to that of the one named, but still represent equivalent JSONs, it passes": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(
				optionsSelector(pod),
				dummyCredSpecName,
				`{"All in all you're just another":      {"the":"wall","brick":   "in"},"We don't need no":["education", "thought control","dark sarcasm in the classroom"]}`,
			)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		},

		"if the cred spec contents are not that of the one named, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(
				optionsSelector(pod),
				dummyCredSpecName,
				`{"We don't need no": ["money"], "All in all you're just another": {"brick": "in", "the": "wall"}}`,
			)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusUnprocessableEntity,
				"the GMSA cred spec contents for %s %q does not match the contents of GMSA resource %q",
				resourceKind, resourceName, dummyCredSpecName)
		},

		"if the cred spec contents are not byte-to-byte equal to that of the one named, and are not even a valid JSON object, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "i ain't no JSON object")

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusUnprocessableEntity,
				"the GMSA cred spec contents for %s %q does not match the contents of GMSA resource %q",
				resourceKind, resourceName, dummyCredSpecName)
		},

		"if the contents are set, but the name one isn't provided, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), "", dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)

			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusUnprocessableEntity,
				"%s %q has a GMSA cred spec set, but does not define the name of the corresponding resource",
				resourceKind, resourceName)
		},

		"if the service account is not authorized to use the cred-spec, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			dummyReason := "dummy reason"

			client := kubeClientFactory()
			client.isAuthorizedToUseCredSpecFunc = func(ctx context.Context, serviceAccountName, namespace, credSpecName string) (authorized bool, reason string) {
				if credSpecName == dummyCredSpecName {
					assert.Equal(t, dummyServiceAccoutName, serviceAccountName)
					assert.Equal(t, dummyNamespace, namespace)

					return false, dummyReason
				}

				return true, ""
			}

			webhook := newWebhook(client)

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"service account %q is not authorized to `use` GMSA cred spec %q, reason: %q",
				dummyServiceAccoutName, dummyCredSpecName, dummyReason)
		},

		"if there is an error when retrieving the cred-spec's contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			dummyError := fmt.Errorf("dummy error")

			client := kubeClientFactory()
			previousRetrieveCredSpecContentsFunc := client.retrieveCredSpecContentsFunc
			client.retrieveCredSpecContentsFunc = func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					return "", http.StatusNotFound, dummyError
				}
				return previousRetrieveCredSpecContentsFunc(ctx, credSpecName)
			}

			webhook := newWebhook(client)

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			response, err := webhook.validateCreateRequest(context.Background(), pod, dummyNamespace)

			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusNotFound, dummyError.Error())
		},
	})
}

func TestMutateCreateRequest(t *testing.T) {
	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with empty GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with no GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			webhook := newWebhookWithOptions(nil, WithRandomHostname(false))
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)

			assert.Nil(t, response.Patch)

		})
	}

	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with random hostname env set and empty GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with random hostname env set and no GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			webhook := newWebhookWithOptions(nil, WithRandomHostname(true))
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)

			assert.Nil(t, response.Patch)

		})
	}

	testCaseName, winOptionsFactory1 := "with random hostname env set and dummy GMSA settings, it passes and set random hostname", func() *corev1.WindowsSecurityContextOptions {
		dummyCredSpecNameVar := dummyCredSpecName
		dummyCredSpecContentsVar := dummyCredSpecContents
		return &corev1.WindowsSecurityContextOptions{GMSACredentialSpecName: &dummyCredSpecNameVar, GMSACredentialSpec: &dummyCredSpecContentsVar}
	}
	t.Run(testCaseName, func(t *testing.T) {
		webhook := newWebhookWithOptions(nil, WithRandomHostname(true))
		pod := buildPod(dummyServiceAccoutName, winOptionsFactory1(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory1()})

		response, err := webhook.mutateCreateRequest(context.Background(), pod)
		assert.Nil(t, err)

		require.NotNil(t, response)
		assert.True(t, response.Allowed)

		var patches []map[string]string
		// one more because we're adding the hostname
		if err := json.Unmarshal(response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, 1, len(patches)) {
			foundHostname := false
			for _, patch := range patches {
				if value, hasValue := patch["value"]; assert.True(t, hasValue) {
					if patch["path"] == "/spec/hostname" {
						foundHostname = true
						assert.Equal(t, "add", patch["op"])
						assert.Equal(t, 15, len(value))
					}
				}
			}
			assert.True(t, foundHostname)
		}
	})

	testCaseName, winOptionsFactory1 = "with random hostname env set and dummy GMSA settings and hostname set in spec, it passes and do nothing", func() *corev1.WindowsSecurityContextOptions {
		dummyCredSpecNameVar := dummyCredSpecName
		dummyCredSpecContentsVar := dummyCredSpecContents
		return &corev1.WindowsSecurityContextOptions{GMSACredentialSpecName: &dummyCredSpecNameVar, GMSACredentialSpec: &dummyCredSpecContentsVar}
	}
	t.Run(testCaseName, func(t *testing.T) {
		webhook := newWebhookWithOptions(nil, WithRandomHostname(true))
		dummyPodNameVar := dummyPodName
		pod := buildPodWithHostName(dummyServiceAccoutName, &dummyPodNameVar, winOptionsFactory1(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory1()})

		response, err := webhook.mutateCreateRequest(context.Background(), pod)
		assert.Nil(t, err)

		require.NotNil(t, response)
		assert.True(t, response.Allowed)

		assert.Nil(t, response.Patch)
	})

	kubeClientFactory := func() *dummyKubeClient {
		return &dummyKubeClient{
			retrieveCredSpecContentsFunc: func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					contents = dummyCredSpecContents
				} else {
					contents = credSpecName + "-contents"
				}
				return
			},
		}
	}

	winOptionsFactory := func(containerName string) *corev1.WindowsSecurityContextOptions {
		return buildWindowsOptions(containerName+"-cred-spec", "")
	}

	runWebhookValidateOrMutateTests(t, winOptionsFactory, map[string]webhookValidateOrMutateTest{
		"with random hostname env and a GMSA cred spec name, it passes and inlines the cred-spec's contents and generate random hostname": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			webhook := newWebhookWithOptions(kubeClientFactory(), WithRandomHostname(true))

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "")

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)

			if assert.NotNil(t, response.PatchType) {
				assert.Equal(t, admissionV1.PatchTypeJSONPatch, *response.PatchType)
			}

			patchPath := func(kind gmsaResourceKind, name string) string {
				partialPath := ""

				if kind == containerKind {
					containerIndex := -1
					for i, container := range pod.Spec.Containers {
						if container.Name == name {
							containerIndex = i
							break
						}
					}
					if containerIndex == -1 {
						t.Fatalf("Did not find any container named %q", name)
					}

					partialPath = fmt.Sprintf("/containers/%d", containerIndex)
				}

				return fmt.Sprintf("/spec%s/securityContext/windowsOptions/gmsaCredentialSpec", partialPath)
			}

			// maps the contents to the expected patch for that container
			expectedPatches := make(map[string]map[string]string)
			for i := 0; i < len(pod.Spec.Containers)-1; i++ {
				credSpecContents := extraContainerName(i) + "-cred-spec-contents"
				expectedPatches[credSpecContents] = map[string]string{
					"op":    "add",
					"path":  patchPath(containerKind, extraContainerName(i)),
					"value": credSpecContents,
				}
			}
			// and the patch for this test's specific cred spec
			expectedPatches[dummyCredSpecContents] = map[string]string{
				"op":    "add",
				"path":  patchPath(resourceKind, resourceName),
				"value": dummyCredSpecContents,
			}

			var patches []map[string]string
			// len(pod.Spec.Containers)+1 because we're adding the hostname
			if err := json.Unmarshal(response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, len(pod.Spec.Containers)+1, len(patches)) {
				foundHostname := false
				for _, patch := range patches {
					if value, hasValue := patch["value"]; assert.True(t, hasValue) {
						if patch["path"] == "/spec/hostname" {
							foundHostname = true
							assert.Equal(t, "add", patch["op"])
							assert.Equal(t, 15, len(value))
						} else if expectedPatch, present := expectedPatches[value]; assert.True(t, present, "value %s not found in expected patches", value) {
							assert.Equal(t, expectedPatch, patch)
						}
					}
				}
				assert.True(t, foundHostname)
			}
		},

		// random hostname env not set in the following cases, and validated no hostname is set (implicitly)
		"it the cred spec's contents are already set, along with its name, it passes and doesn't overwrite the provided contents": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			webhook := newWebhook(kubeClientFactory())

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, `{"pre-set GMSA": "cred contents"}`)

			response, err := webhook.mutateCreateRequest(context.Background(), pod)
			assert.Nil(t, err)

			// all the patches we receive should be for the extra containers
			expectedPatchesLen := len(pod.Spec.Containers) - 1

			if expectedPatchesLen == 0 {
				assert.Nil(t, response.PatchType)
				assert.Nil(t, response.Patch)
			} else {
				var patches []map[string]string
				if err := json.Unmarshal(response.Patch, &patches); assert.Nil(t, err) && assert.Equal(t, expectedPatchesLen, len(patches)) {
					for _, patch := range patches {
						if path, hasPath := patch["path"]; assert.True(t, hasPath) {
							assert.NotContains(t, path, dummyCredSpecName)
						}
					}
				}
			}
		},

		"if there is an error when retrieving the cred-spec's contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			dummyError := fmt.Errorf("dummy error")

			client := kubeClientFactory()
			previousRetrieveCredSpecContentsFunc := client.retrieveCredSpecContentsFunc
			client.retrieveCredSpecContentsFunc = func(ctx context.Context, credSpecName string) (contents string, httpCode int, err error) {
				if credSpecName == dummyCredSpecName {
					return "", http.StatusNotFound, dummyError
				}
				return previousRetrieveCredSpecContentsFunc(ctx, credSpecName)
			}

			webhook := newWebhook(client)

			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "")

			response, err := webhook.mutateCreateRequest(context.Background(), pod)

			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusNotFound, dummyError.Error())
		},
	})
}

func TestValidateUpdateRequest(t *testing.T) {
	for testCaseName, winOptionsFactory := range map[string]func() *corev1.WindowsSecurityContextOptions{
		"with empty GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return &corev1.WindowsSecurityContextOptions{}
		},
		"with no GMSA settings, it passes and does nothing": func() *corev1.WindowsSecurityContextOptions {
			return nil
		},
	} {
		t.Run(testCaseName, func(t *testing.T) {
			pod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})
			oldPod := buildPod(dummyServiceAccoutName, winOptionsFactory(), map[string]*corev1.WindowsSecurityContextOptions{dummyContainerName: winOptionsFactory()})

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		})
	}

	winOptionsFactory := func(containerName string) *corev1.WindowsSecurityContextOptions {
		return buildWindowsOptions(containerName+"-cred-spec", containerName+"-cred-spec-contents")
	}

	runWebhookValidateOrMutateTests(t, winOptionsFactory, map[string]webhookValidateOrMutateTest{
		"if there was no changes to GMSA settings, it passes": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, _ gmsaResourceKind, _ string) {
			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, dummyCredSpecContents)

			oldPod := pod.DeepCopy()

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, err)

			require.NotNil(t, response)
			assert.True(t, response.Allowed)
		},

		"if there was a change to a GMSA name, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			setWindowsOptions(optionsSelector(pod), "new-cred-spec-name", dummyCredSpecContents)

			oldPod := pod.DeepCopy()
			setWindowsOptions(optionsSelector(oldPod), dummyCredSpecName, "")

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"cannot update an existing pod's GMSA settings (GMSA name modified on %s %q)",
				resourceKind, resourceName)
		},

		"if there was a change to a GMSA contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			setWindowsOptions(optionsSelector(pod), dummyCredSpecName, "new-cred-spec-contents")

			oldPod := pod.DeepCopy()
			setWindowsOptions(optionsSelector(oldPod), "", dummyCredSpecContents)

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"cannot update an existing pod's GMSA settings (GMSA contents modified on %s %q)",
				resourceKind, resourceName)
		},

		"if there were changes to both GMSA name & contents, it fails": func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string) {
			setWindowsOptions(optionsSelector(pod), "new-cred-spec-name", "new-cred-spec-contents")

			oldPod := pod.DeepCopy()
			setWindowsOptions(optionsSelector(oldPod), dummyCredSpecName, dummyCredSpecContents)

			response, err := validateUpdateRequest(pod, oldPod)
			assert.Nil(t, response)

			assertPodAdmissionErrorContains(t, err, pod, http.StatusForbidden,
				"cannot update an existing pod's GMSA settings (GMSA name and contents modified on %s %q)",
				resourceKind, resourceName)
		},
	})
}

func TestDefaultWebhookConfig(t *testing.T) {
	expectedCertReload := false
	webhook := newWebhookWithOptions(nil, WithCertReload(expectedCertReload))
	assert.Equal(t, expectedCertReload, webhook.config.EnableCertReload)
}

func TestSetWebhookConfig(t *testing.T) {
	expectedCertReload := true
	expectedRandomHostname := true
	randomHostname := true
	webhook := newWebhookWithOptions(nil, WithCertReload(expectedCertReload), WithRandomHostname(randomHostname))
	assert.Equal(t, expectedCertReload, webhook.config.EnableCertReload)
	assert.Equal(t, expectedRandomHostname, webhook.config.EnableRandomHostName)
}

func TestEqualStringPointers(t *testing.T) {
	ptrToString := func(s *string) string {
		if s == nil {
			return "nil"
		}
		return " = " + *s
	}

	foo := "foo"
	bar := "bar"

	for _, testCase := range []struct {
		s1             *string
		s2             *string
		expectedResult bool
	}{
		{
			s1:             nil,
			s2:             nil,
			expectedResult: true,
		},
		{
			s1:             &foo,
			s2:             nil,
			expectedResult: false,
		},
		{
			s1:             &foo,
			s2:             &foo,
			expectedResult: true,
		},
		{
			s1:             &foo,
			s2:             &bar,
			expectedResult: false,
		},
	} {
		for _, ptrs := range [][]*string{
			{testCase.s1, testCase.s2},
			{testCase.s2, testCase.s1},
		} {
			s1 := ptrs[0]
			s2 := ptrs[1]

			testName := fmt.Sprintf("with s1 %s and s2 %s, should return %v",
				ptrToString(s1),
				ptrToString(s2),
				testCase.expectedResult)

			t.Run(testName, func(t *testing.T) {
				assert.Equal(t, testCase.expectedResult, equalStringPointers(s1, s2))
			})
		}
	}
}

/* Helpers below */

type containerWindowsOptionsFactory func(containerName string) *corev1.WindowsSecurityContextOptions

type winOptionsSelector func(pod *corev1.Pod) *corev1.WindowsSecurityContextOptions

// a webhookValidateOrMutateTest function should run a test on one of the webhook's validate or mutate
// functions, given a selector to extract the WindowsSecurityOptions struct it can play with from the pod.
// It should assume that the pod it receives has any number of extra containers with correct
// (in the sense of the test) windows security options generated by a relevant containerWindowsOptionsFactory.
type webhookValidateOrMutateTest func(t *testing.T, pod *corev1.Pod, optionsSelector winOptionsSelector, resourceKind gmsaResourceKind, resourceName string)

// runWebhookValidateOrMutateTests runs the given tests with 0 to 5 extra containers with correct windows
// security options as generated by winOptionsFactory.
func runWebhookValidateOrMutateTests(t *testing.T, winOptionsFactory containerWindowsOptionsFactory, tests map[string]webhookValidateOrMutateTest) {
	for extraContainersCount := 0; extraContainersCount <= 5; extraContainersCount++ {
		containerNamesAndWindowsOptions := make(map[string]*corev1.WindowsSecurityContextOptions)

		for i := 0; i < extraContainersCount; i++ {
			containerName := extraContainerName(i)
			containerNamesAndWindowsOptions[containerName] = winOptionsFactory(containerName)
		}

		testNameSuffix := ""
		if extraContainersCount > 0 {
			testNameSuffix = fmt.Sprintf(" and %d extra containers", extraContainersCount)
		}

		for _, resourceKind := range []gmsaResourceKind{podKind, containerKind} {
			for testName, testFunc := range tests {
				podWindowsOptions := &corev1.WindowsSecurityContextOptions{}
				containerNamesAndWindowsOptions[dummyContainerName] = &corev1.WindowsSecurityContextOptions{}
				pod := buildPod(dummyServiceAccoutName, podWindowsOptions, containerNamesAndWindowsOptions)

				var optionsSelector winOptionsSelector
				var resourceName string
				switch resourceKind {
				case podKind:
					optionsSelector = func(pod *corev1.Pod) *corev1.WindowsSecurityContextOptions {
						if pod != nil && pod.Spec.SecurityContext != nil {
							return pod.Spec.SecurityContext.WindowsOptions
						}
						return nil
					}

					resourceName = dummyPodName
				case containerKind:
					optionsSelector = func(pod *corev1.Pod) *corev1.WindowsSecurityContextOptions {
						if pod != nil {
							for _, container := range pod.Spec.Containers {
								if container.Name == dummyContainerName {
									if container.SecurityContext != nil {
										return container.SecurityContext.WindowsOptions
									}
									return nil
								}
							}
						}
						return nil
					}

					resourceName = dummyContainerName
				default:
					t.Fatalf("Unknown resource kind: %q", resourceKind)
				}

				t.Run(fmt.Sprintf("%s - with %s-level windows options%s", testName, resourceKind, testNameSuffix), func(t *testing.T) {
					testFunc(t, pod, optionsSelector, resourceKind, resourceName)
				})
			}
		}
	}
}

func extraContainerName(i int) string {
	return fmt.Sprintf("extra-container-%d", i)
}

func assertPodAdmissionErrorContains(t *testing.T, err *podAdmissionError, pod *corev1.Pod, httpCode int, msgFormat string, msgArgs ...interface{}) bool {
	if !assert.NotNil(t, err) {
		return false
	}

	result := assert.Equal(t, pod, err.pod)
	result = assert.Equal(t, httpCode, err.code) && result
	return assert.Contains(t, err.Error(), fmt.Sprintf(msgFormat, msgArgs...)) && result
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/deploy/.helpers.sh`
```bash
## Meant to be sourced by other files in this repo

echo_stderr() {
    local COLOR
    local NO_COLOR='\033[0m'

    case "$1" in
        green)
            COLOR='\033[0;32m' ;;
        yellow)
            COLOR='\033[0;33m' ;;
        red)
            COLOR='\033[0;31m' ;;
        esac
    shift 1

    >&2 printf "${COLOR}$@\n${NO_COLOR}"
}

info() {
    echo_stderr 'green' "*** $@ ***"
}

warn() {
    echo_stderr 'yellow' "WARNING: $@"
}

fatal_error() {
    echo_stderr 'red' "FATAL ERROR: $@"
    exit 1
}

if [ ! -x "$KUBECTL" ]; then
    KUBECTL=$(command -v kubectl)

    if [ ! -x "$KUBECTL" ]; then
        fatal_error 'kubectl not found'
    fi
fi

echo_or_run() {
    local WITH_KUBECTL_DRY_RUN=false
    if [[ "$1" == '--with-kubectl-dry-run' ]]; then
        WITH_KUBECTL_DRY_RUN=true
        shift
    fi

    if $DRY_RUN; then
        echo "$@"
        if $WITH_KUBECTL_DRY_RUN; then
            eval "$@ --dry-run=client >&2"
        fi
    else
        eval "$@"
    fi
}

wait_for() {
    local FUN="$1"
    local ERROR_MSG="$2"
    local MAX_ATTEMPTS="$3"
    [ "$MAX_ATTEMPTS" ] || MAX_ATTEMPTS=30

    local OUTPUT
    for _ in $(seq "$MAX_ATTEMPTS"); do
        if OUTPUT=$($FUN); then
            echo "$OUTPUT"
            return
        fi
        sleep 1
    done

    local MSG="$ERROR_MSG, giving up after $MAX_ATTEMPTS attempts"
    if [ "$OUTPUT" ]; then
        MSG+=" - last attempt's output: $OUTPUT"
    fi
    fatal_error "$MSG"
}

SERVER_KEY="$CERTS_DIR/server-key.pem"
SERVER_CERT="$CERTS_DIR/server-cert.pem"

if [ "$K8S_WINDOWS_GMSA_DEPLOY_DEBUG" ]; then
    set -x
fi
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/deploy/create-signed-cert.sh`
```bash
#!/usr/bin/env bash

## Generates cluster-valid SSL certs for the webhook service
## Inspired from
## https://raw.githubusercontent.com/istio/istio/release-0.7/install/kubernetes/webhook-create-signed-cert.sh
## whose license is also Apache 2.0

set -e

usage() {
    cat <<EOF
Generates certificate suitable for use with the GMSA webhook service.

This script uses k8s' CertificateSigningRequest API to a generate a
certificate signed by k8s CA suitable for use with the GMSA webhook
service. This requires permissions to create and approve CSR. See
https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster for
detailed explantion and additional instructions.

usage: $0 --service SERVICE_NAME --namespace NAMESPACE_NAME --certs-dir PATH/TO/CERTS/DIR [--dry-run] [--overwrite]

If --dry-run is set, the script echoes what command it would perform
to stdout without actually affecting the k8s cluster.
If the files this script generates already exist and --overwrite is
not set, it will not regenerate the files.
EOF
    exit 1
}

SERVICE=
NAMESPACE=
CERTS_DIR=
DRY_RUN=false
OVERWRITE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --service)
            SERVICE="$2" && shift 2 ;;
        --namespace)
            NAMESPACE="$2" && shift 2 ;;
        --certs-dir)
            CERTS_DIR="$2" && shift 2 ;;
        --dry-run)
            DRY_RUN=true && shift ;;
        --overwrite)
            OVERWRITE=true && shift ;;
        *)
            echo "Unknown option: $1"
            usage ;;
    esac
done

[ "$SERVICE" ] && [ "$NAMESPACE" ] && [ "$CERTS_DIR" ] || usage

if [ ! "$K8S_WINDOWS_GMSA_HELPER_SCRIPT" ]; then
    DEPLOY_DIR="$(dirname "$0")"
    K8S_WINDOWS_GMSA_HELPER_SCRIPT="$DEPLOY_DIR/.helpers.sh"
fi
. "$K8S_WINDOWS_GMSA_HELPER_SCRIPT"

if [ ! -x "$(command -v openssl)" ]; then
    fatal_error 'openssl not found'
fi

gen_file() {
    local FUN="$1"
    local FILE_PATH="$2"

    if [ -f "$FILE_PATH" ] && ! $OVERWRITE; then
        warn "$FILE_PATH already exists, not re-generating"
    else
        $FUN
    fi
}

gen_server_key() { openssl genrsa -out "$SERVER_KEY" 2048; }
gen_file gen_server_key "$SERVER_KEY"

CSR_CONF="$CERTS_DIR/csr.conf"
gen_csr_conf() {
    cat <<EOF >> "$CSR_CONF"
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = $SERVICE
DNS.2 = $SERVICE.$NAMESPACE
DNS.3 = $SERVICE.$NAMESPACE.svc
EOF
}
gen_file gen_csr_conf "$CSR_CONF"

SERVER_CSR="$CERTS_DIR/server.csr"
gen_server_scr() { openssl req -new -key "$SERVER_KEY" -subj "/O=system:nodes/CN=system:node:$SERVICE.$NAMESPACE.svc" -out "$SERVER_CSR" -config "$CSR_CONF"; }
gen_file gen_server_scr "$SERVER_CSR"

CSR_NAME="$SERVICE.$NAMESPACE"
# clean-up any previously created CSR for our service
if ! $DRY_RUN && $KUBECTL get csr "$CSR_NAME" &> /dev/null; then
    $KUBECTL delete csr "$CSR_NAME"
fi

# create server cert/key CSR and send to k8s API
CSR_CONTENTS=$(cat <<EOF
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: $CSR_NAME
spec:
  groups:
  - system:authenticated
  request: $(cat "$SERVER_CSR" | base64 -w 0)
  signerName: kubernetes.io/kubelet-serving
  usages:
  - digital signature
  - key encipherment
  - server auth
EOF
)
echo_or_run --with-kubectl-dry-run "$KUBECTL create -f - <<< '$CSR_CONTENTS'"

if ! $DRY_RUN; then
    verify_csr_created() { $KUBECTL get csr "$CSR_NAME" 2>&1 ; }
    wait_for verify_csr_created "CSR $CSR_NAME not properly created"
fi

# approve and fetch the signed certificate
echo_or_run "$KUBECTL certificate approve $CSR_NAME"

if ! $DRY_RUN; then
    verify_cert_signed() {
        local CERT_CONTENTS
        CERT_CONTENTS=$($KUBECTL get csr $CSR_NAME -o jsonpath='{.status.certificate}')
        echo "$CERT_CONTENTS"
        [[ "$CERT_CONTENTS" != "" ]]
    }
    SERVER_CERT_CONTENTS=$(wait_for verify_cert_signed "after approving CSR $CSR_NAME, the signed certificate did not appear on the resource")

    gen_server_cert() { echo "$SERVER_CERT_CONTENTS" | openssl base64 -d -A -out "$SERVER_CERT"; }
    gen_file gen_server_cert "$SERVER_CERT"
fi
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/deploy/deploy-gmsa-webhook.sh`
```bash
#!/usr/bin/env bash

## Deploys the GMSA webhook

set -e

usage() {
    cat <<EOF
Deploys the GMSA webhook.

Should be run with a kube admin config file present at either the canonical location
(~/.kube/config) or at the path specified by the KUBECONFIG environment variable.

This script:
 * generates a SSL certificate signed by k8s, for mutual authentication
   between the API server and the webhook service
 * deploys a k8s service running the webhook
 * registers that service as a webhook admission controller

usage: $0 --file MANIFESTS_FILE [--name NAME] [--namespace NAMESPACE] [--image IMAGE_NAME] [--certs-dir CERTS_DIR] [--dry-run] [--overwrite] [--tolerate-master]

MANIFESTS_FILE is the path to the file the k8s manifests will be written to.
NAME defaults to 'gmsa-webhook' and is used in the names of most of the k8s resources created.
NAMESPACE is the namespace to deploy to; defaults to 'gmsa-webhook'.
IMAGE_NAME is the name of the Docker image containing the webhook; defaults to 'sigwindowstools/k8s-gmsa-webhook:latest'
CERTS_DIR defaults to 'gmsa-webhook-certs'

If --dry-run is set, the script echoes what command it would perform
without actually affecting the k8s cluster.
If the files this script generates already exist and --overwrite is
not set, it will not regenerate the files.
If --tolerate-master is set, the webhook will tolerate running on master nodes.
EOF
    exit 1
}

DEPLOY_DIR="$(dirname "$0")"
TMP_DIR_PREFIX='/tmp/gmsa-webhook-deploy-'

# it's possible to override these 2 to download from another repo/branch
[ "$K8S_GMSA_DEPLOY_DOWNLOAD_REPO" ] || K8S_GMSA_DEPLOY_DOWNLOAD_REPO='kubernetes-sigs/windows-gmsa'
[ "$K8S_GMSA_DEPLOY_DOWNLOAD_REV" ] || K8S_GMSA_DEPLOY_DOWNLOAD_REV='master'

ensure_helper_file_present() {
    local NAME="$1"
    local DIR="$DEPLOY_DIR"

    if [ ! -r "$DIR/$NAME" ]; then
        DIR=$(mktemp -d "${TMP_DIR_PREFIX}XXXXXXX")
        local URL="https://raw.githubusercontent.com/$K8S_GMSA_DEPLOY_DOWNLOAD_REPO/$K8S_GMSA_DEPLOY_DOWNLOAD_REV/admission-webhook/deploy/$NAME"

        if which curl &> /dev/null; then
            curl -sL "$URL" > "$DIR/$NAME"
        else
            wget -O "$DIR/$NAME" "$URL"
        fi
    fi

    realpath "$DIR/$NAME"
}

write_manifests_file() {
    local TEMPLATE_PATH="$1"
    local MANIFESTS_FILE="$2"

    if [ -x "$(command -v envsubst)" ] && [ ! "$WITHOUT_ENVSUBST" ]; then
        echo "using local envsubst"
        envsubst < "$TEMPLATE_PATH" > "$MANIFESTS_FILE"
    elif [ -x "$(command -v docker)" ]; then
        echo "using envsubst in docker"
        # due to a bug in --env-file convert varaibles we care about to -e parameters 
        # The sed commands get only the env names before =, clean any white space, add -e to them, then make it all one line
        # https://github.com/moby/moby/issues/12997#issuecomment-307665540
        ENVS=`env | grep -E 'NAME|NAMESPACE|TLS|RBAC|TOLERATIONS|IMAGE|CA' | sed -n '/^[^\t]/s/=.*//p' | sed '/^$/d' | sed 's/^/-e /g' | tr '\n' ' '`

        # envsubst is installed in the nginx images which we already maintain
        docker run --rm -v "$TEMPLATE_PATH:$TEMPLATE_PATH" $ENVS registry.k8s.io/e2e-test-images/nginx:1.15-1 sh -c "cat $TEMPLATE_PATH | envsubst" > $MANIFESTS_FILE
    else
        fatal_error "Unable to run envsubst"
    fi
}

main() {
    local MANIFESTS_FILE=
    local NAME='gmsa-webhook'
    local NAMESPACE='gmsa-webhook'
    local IMAGE_NAME='registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook:v0.13.0'
    local CERTS_DIR='gmsa-webhook-certs'
    local DRY_RUN=false
    local OVERWRITE=false
    local TOLERATE_MASTER=false

    # parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --file)
                MANIFESTS_FILE="$2" && shift 2 ;;
            --name)
                NAME="$2" && shift 2 ;;
            --namespace)
                NAMESPACE="$2" && shift 2 ;;
            --image)
                IMAGE_NAME="$2" && shift 2 ;;
            --certs-dir)
                CERTS_DIR="$2" && shift 2 ;;
            --dry-run)
                DRY_RUN=true && shift ;;
            --overwrite)
                OVERWRITE=true && shift ;;
            --tolerate-master)
                TOLERATE_MASTER=true && shift ;;
            *)
                echo "Unknown option: $1"
                usage ;;
        esac
    done

    [ "$MANIFESTS_FILE" ] || usage

    # download the helper scripts if needed
    local HELPERS_SCRIPT
    HELPER_SCRIPT=$(ensure_helper_file_present '.helpers.sh')
    . "$HELPER_SCRIPT"
    local CREATE_SIGNED_CERT_SCRIPT
    CREATE_SIGNED_CERT_SCRIPT=$(ensure_helper_file_present 'create-signed-cert.sh')

    if [ -d "$CERTS_DIR" ]; then
        $OVERWRITE || warn "Certs dir $CERTS_DIR already exists"
    else
        mkdir -p "$CERTS_DIR"
    fi

    # create the SSL cert and apply it to the cluster
    local CREATE_CERT_CMD="$BASH $CREATE_SIGNED_CERT_SCRIPT --service $NAME --namespace $NAMESPACE --certs-dir $CERTS_DIR"
    $DRY_RUN && CREATE_CERT_CMD+=" --dry-run" || true
    $OVERWRITE && CREATE_CERT_CMD+=" --overwrite" || true
    eval "K8S_WINDOWS_GMSA_HELPER_SCRIPT='$HELPER_SCRIPT' $CREATE_CERT_CMD"

    # create the CRD
    local CRD_MANIFEST_PATH=$(ensure_helper_file_present 'gmsa-crd.yml')
    local CRD_MANIFEST_CONTENTS=$(cat "$CRD_MANIFEST_PATH")
    if ! $DRY_RUN && $KUBECTL get crd gmsacredentialspecs.windows.k8s.io &> /dev/null; then
        $KUBECTL delete crd gmsacredentialspecs.windows.k8s.io
    fi
    echo_or_run --with-kubectl-dry-run "$KUBECTL create -f - <<< '$CRD_MANIFEST_CONTENTS'"

    # then render the template for the rest of the resources
    local TEMPLATE_PATH
    TEMPLATE_PATH=$(ensure_helper_file_present 'gmsa-webhook.yml.tpl')

    # the TLS certificate might not have been generated yet if it's a dry run
    local TLS_CERTIFICATE
    if [ -r "$SERVER_CERT" ]; then
        TLS_CERTIFICATE=$(cat "$SERVER_CERT" | base64 -w 0)
    elif $DRY_RUN; then
        TLS_CERTIFICATE='TBD'
    else
        fatal_error "Expected to find the server certificate at $SERVER_CERT"
    fi

    TOLERATIONS=''
    if $TOLERATE_MASTER; then
        TOLERATIONS='
      tolerations:
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule'
    fi

    if [ -f "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt" ]; then
        info 'using pod based authentication'
        BUNDLE=$(cat /var/run/secrets/kubernetes.io/serviceaccount/ca.crt | base64 | tr -d '\n')
    else
        info 'using config file authentication'
        BUNDLE=$($KUBECTL config view --raw --minify --flatten -o jsonpath='{.clusters[].cluster.certificate-authority-data}')
    fi

    if [[ -z "$BUNDLE" ]]; then
        fatal_error "Not able to determine CA bundle for depoloyment"
    fi

    TLS_PRIVATE_KEY=$(cat "$SERVER_KEY" | base64 -w 0) \
        TLS_CERTIFICATE="$TLS_CERTIFICATE" \
        CA_BUNDLE="$BUNDLE" \
        RBAC_ROLE_NAME="$NAMESPACE-$NAME-rbac-role" \
        NAME="$NAME" \
        NAMESPACE="$NAMESPACE" \
        IMAGE_NAME="$IMAGE_NAME" \
        TOLERATIONS="$TOLERATIONS" \
        write_manifests_file "$TEMPLATE_PATH" "$MANIFESTS_FILE"

    echo_or_run --with-kubectl-dry-run "$KUBECTL apply -f $MANIFESTS_FILE"

    if ! $DRY_RUN; then
        verify_webhook_ready() {
            local READY
            if READY="$($KUBECTL -n "$NAMESPACE" get pod --selector=app=$NAME -o=jsonpath='{.items[0].status.containerStatuses[0].ready}' 2> /dev/null)"; then
                [[ "$READY" == 'true' ]]
            else
                return 1
            fi
        }
        wait_for verify_webhook_ready 'webhook not ready'

        info 'Windows GMSA Admission Webhook successfully deployed!'
        info "You can remove it by running $KUBECTL delete -f $MANIFESTS_FILE"
    fi

    # cleanup
    rm -rf "$TMP_DIR_PREFIX"*
}

main "$@"
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/deploy/gmsa-crd.yml`
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: gmsacredentialspecs.windows.k8s.io
  annotations:
    "api-approved.kubernetes.io": "https://github.com/kubernetes/enhancements/tree/master/keps/sig-windows/689-windows-gmsa"
spec:
  group: windows.k8s.io
  versions:
  - name: v1alpha1
    served: true
    storage: false
    deprecated: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          credspec:
            description: GMSA Credential Spec
            type: object
            properties:
              ActiveDirectoryConfig:
                type: object
                properties:
                  GroupManagedServiceAccounts:
                    type: array
                    items:
                      type: object
                      properties:
                        Name:
                          type: string
                        Scope:
                          type: string
                  HostAccountConfig:
                    type: object
                    properties:
                      PluginGUID:
                        type: string
                      PluginInput:
                        type: string
                      PortableCcgVersion:
                        type: string
              CmsPlugins:
                type: array
                items:
                  type: string
              DomainJoinConfig:
                type: object
                properties:
                  DnsName:
                    type: string
                  DnsTreeName:
                    type: string
                  Guid:
                    type: string
                  MachineAccountName:
                    type: string
                  NetBiosName:
                    type: string
                  Sid:
                    type: string
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          credspec:
            description: GMSA Credential Spec
            type: object
            properties:
              ActiveDirectoryConfig:
                type: object
                properties:
                  GroupManagedServiceAccounts:
                    type: array
                    items:
                      type: object
                      properties:
                        Name:
                          type: string
                        Scope:
                          type: string
                  HostAccountConfig:
                    type: object
                    properties:
                      PluginGUID:
                        type: string
                      PluginInput:
                        type: string
                      PortableCcgVersion:
                        type: string
              CmsPlugins:
                type: array
                items:
                  type: string
              DomainJoinConfig:
                type: object
                properties:
                  DnsName:
                    type: string
                  DnsTreeName:
                    type: string
                  Guid:
                    type: string
                  MachineAccountName:
                    type: string
                  NetBiosName:
                    type: string
                  Sid:
                    type: string
  conversion:
    strategy: None
  names:
    kind: GMSACredentialSpec
    plural: gmsacredentialspecs
  scope: Cluster
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/deploy/gmsa-webhook.yml.tpl`
```
## Template to deploy the GMSA webhook
## TODO: make this a helmchart instead?

apiVersion: v1
kind: Namespace
metadata:
  name: ${NAMESPACE}
  labels:
    gmsa-webhook: disabled

---

apiVersion: v1
kind: Secret
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
data:
  tls_private_key: ${TLS_PRIVATE_KEY}
  tls_certificate: ${TLS_CERTIFICATE}

---

# the service account for the webhook
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}

---

# the RBAC role that the webhook needs to:
#  * read GMSA custom resources
#  * check authorizations to use GMSA cred specs
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ${RBAC_ROLE_NAME}
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["get"]
- apiGroups: ["authorization.k8s.io"]
  resources: ["localsubjectaccessreviews"]
  verbs: ["create"]

---

# bind that role to the webhook's service account
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ${NAMESPACE}-${NAME}-binding-to-${RBAC_ROLE_NAME}
  namespace: ${NAMESPACE}
subjects:
- kind: ServiceAccount
  name: ${NAME}
  namespace: ${NAMESPACE}
roleRef:
  kind: ClusterRole
  name: ${RBAC_ROLE_NAME}
  apiGroup: rbac.authorization.k8s.io

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ${NAME}
  template:
    metadata:
      labels:
        app: ${NAME}
    spec:
      serviceAccountName: ${NAME}
      nodeSelector:
        kubernetes.io/os: linux${TOLERATIONS}
      containers:
      - name: ${NAME}
        image: ${IMAGE_NAME}
        imagePullPolicy: IfNotPresent
        readinessProbe:
          httpGet:
            scheme: HTTPS
            path: /health
            port: 443
        ports:
        - containerPort: 443
        volumeMounts:
          - name: tls
            mountPath: "/tls"
            readOnly: true
        env:
          - name: TLS_KEY
            value: /tls/key
          - name: TLS_CRT
            value: /tls/crt
      volumes:
      - name: tls
        secret:
          secretName: ${NAME}
          items:
          - key: tls_private_key
            path: key
          - key: tls_certificate
            path: crt

---

apiVersion: v1
kind: Service
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
spec:
  ports:
  - port: 443
    targetPort: 443
  selector:
    app: ${NAME}

---

apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: ${NAME}
webhooks:
- name: admission-webhook.windows-gmsa.sigs.k8s.io
  clientConfig:
    service:
      name: ${NAME}
      namespace: ${NAMESPACE}
      path: "/validate"
    caBundle: ${CA_BUNDLE}
  rules:
  - operations: ["CREATE", "UPDATE"]
    apiGroups: [""]
    apiVersions: ["*"]
    resources: ["pods"]
  failurePolicy: Fail
  admissionReviewVersions: ["v1", "v1beta1"]
  sideEffects: None
  # don't run on ${NAMESPACE}
  namespaceSelector:
    matchExpressions:
      - key: gmsa-webhook
        operator: NotIn
        values: [disabled]

---

apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: ${NAME}
webhooks:
- name: admission-webhook.windows-gmsa.sigs.k8s.io
  clientConfig:
    service:
      name: ${NAME}
      namespace: ${NAMESPACE}
      path: "/mutate"
    caBundle: ${CA_BUNDLE}
  rules:
  - operations: ["CREATE"]
    apiGroups: [""]
    apiVersions: ["*"]
    resources: ["pods"]
  failurePolicy: Fail
  admissionReviewVersions: ["v1", "v1beta1"]
  sideEffects: None
  # don't run on ${NAMESPACE}
  namespaceSelector:
    matchExpressions:
    - key: gmsa-webhook
      operator: NotIn
      values: [disabled]
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/dockerfiles/Dockerfile`
```
## Dockerfile for release, as lightweight as possible

ARG ARCH
ARG GO_VERSION
ARG GOARCH

FROM --platform=linux/amd64 golang:${GO_VERSION} AS builder

WORKDIR /go/src/sigs.k8s.io/windows-gmsa/admission-webhook

# copy go dependencies
COPY go.mod ./go.mod
COPY go.sum ./go.sum

# build
COPY *.go ./
ARG VERSION
RUN go mod vendor && go mod tidy
RUN CGO_ENABLED=0 GOOS=linux GOARCH=${GOARCH} go build -ldflags="-w -s -X main.version=${VERSION}"

###

FROM --platform=linux/${ARCH} scratch

WORKDIR /admission-webhook

ENV LOG_LEVEL=info

COPY --from=builder /go/src/sigs.k8s.io/windows-gmsa/admission-webhook/admission-webhook .

ENTRYPOINT ["/admission-webhook/admission-webhook"]
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/dockerfiles/Dockerfile.dev`
```
## Dockerfile for dev
## Differs from the release Dockerfile in that it allows re-compiling and re-starting
## the webserver from within the container

ARG GO_VERSION
FROM golang:$GO_VERSION

# we use runit so that we can stop the service without killing the container, and consequently
# play around with it
RUN apt-get update && apt-get install --yes runit
RUN mkdir /etc/service/webhook \
    && /bin/bash -c "echo -e '"'#!/bin/bash\nexec /go/src/sigs.k8s.io/windows-gmsa/admission-webhook/admission-webhook 2>&1\n'"' > /etc/service/webhook/run" \
    && chmod +x /etc/service/webhook/run
RUN ln -s /usr/bin/sv /etc/init.d/webhook

WORKDIR /go/src/sigs.k8s.io/windows-gmsa/admission-webhook

# copy go dependencies
COPY /vendor ./vendor

# build
COPY *.go ./
ARG VERSION
RUN go build -ldflags="-X main.version=${VERSION}"

# copy the rest
COPY . .

# let runit work its magic
CMD ["runsvdir", "/etc/service"]
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/integration_test.go`
```go
package integrationtests

import (
	"context"
	"encoding/json"
	"fmt"
	"html/template"
	"io/ioutil"
	"os"
	"path"
	"reflect"
	"strconv"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime/schema"
)

const (
	// this is the JSON representation of the cred spec from templates/credspec-0.yml
	expectedCredSpec0 = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524075714-3094792973"}}`
	// this is the JSON representation of the cred spec from templates/credspec-1.yml
	expectedCredSpec1 = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication1","Scope":"CONTOSO"},{"Name":"WebApplication1","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication1","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524175714-3194792973"}}`
	// this is the JSON representation of the cred spec from templates/credspec-2.yml
	expectedCredSpec2 = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication2","Scope":"CONTOSO"},{"Name":"WebApplication2","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication2","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524275714-3294792973"}}`
	// this is the JSON representation of the cred spec from templates/credspec-with-hostagentconfig.yml
	expectedCredSpecWithHostAgentConfig = `{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication2","Scope":"CONTOSO"},{"Name":"WebApplication2","Scope":"contoso.com"}],"HostAccountConfig":{"PluginGUID":"{GDMA0342-266A-4D1P-831J-20990E82944F}","PluginInput":"contoso.com:gmsaccg:\u003cpassword\u003e","PortableCcgVersion":"1"}},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication2","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524275714-3294792973"}}`

	tmpRoot      = "tmp"
	ymlExtension = ".yml"
)

var (
	v1alpha1Resource = schema.GroupVersionResource{
		Group:    "windows.k8s.io",
		Version:  "v1alpha1",
		Resource: "gmsacredentialspecs",
	}

	v1Resource = schema.GroupVersionResource{
		Group:    "windows.k8s.io",
		Version:  "v1",
		Resource: "gmsacredentialspecs",
	}
)

func TestHappyPathWithPodLevelCredSpec(t *testing.T) {
	testName := "happy-path-with-pod-level-cred-spec"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpec0, extractPodCredSpecContents(t, pod))
}

func TestHappyPathWithContainerLevelCredSpec(t *testing.T) {
	testName := "happy-path-with-container-cred-spec"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-container-level-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, "nginx"))
}

func TestHappyPathWithSeveralContainers(t *testing.T) {
	testName := "happy-path-with-several-containers"
	credSpecTemplates := []string{"credspec-0", "credspec-1", "credspec-2"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "several-containers-with-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, "nginx0"))
	assert.Equal(t, expectedCredSpec1, extractPodCredSpecContents(t, pod))
	assert.Equal(t, expectedCredSpec2, extractContainerCredSpecContents(t, pod, "nginx2"))
}

func TestHappyPathWithPreSetMatchingContents(t *testing.T) {
	testName := "happy-path-with-pre-set-matching-contents"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-pre-set-matching-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	actualCredSpecContents := extractPodCredSpecContents(t, pod)
	assert.NotEqual(t, expectedCredSpec0, actualCredSpecContents)

	var (
		expectedCredSpec map[string]interface{}
		actualCredSpec   map[string]interface{}
	)
	if assert.Nil(t, json.Unmarshal([]byte(expectedCredSpec0), &expectedCredSpec)) &&
		assert.Nil(t, json.Unmarshal([]byte(actualCredSpecContents), &actualCredSpec)) {
		assert.True(t, reflect.DeepEqual(expectedCredSpec, actualCredSpec))
	}
}

func TestServiceAccountDoesNotHavePermissionsToUseCredSpec(t *testing.T) {
	testName := "sa-does-not-have-permissions-to-use-cred-spec"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "simple-with-container-level-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		expectedSubstr := fmt.Sprintf("service account %q is not authorized to `use` GMSA cred spec %q", testConfig.ServiceAccountName, testConfig.CredSpecNames[0])
		assert.Contains(t, condition.Message, expectedSubstr)
	}
}

func TestCredSpecDoesNotExist(t *testing.T) {
	testName := "cred-spec-does-not-exist"
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-unknown-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, nil, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		assert.Contains(t, condition.Message, "cred spec i-sure-dont-exist does not exist")
	}
}

func TestCannotPreSetGMSAPodLevelContentsWithoutName(t *testing.T) {
	testName := "cannot-pre-set-gmsa-pod-level-contents-without-name"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-preset-gmsa-pod-level-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		assert.Contains(t, condition.Message, "has a GMSA cred spec set, but does not define the name of the corresponding resource")
	}
}

func TestCannotPreSetGMSAContainerLevelContentsWithoutName(t *testing.T) {
	testName := "cannot-pre-set-gmsa-container-level-contents-without-name"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-preset-gmsa-container-level-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		assert.Contains(t, condition.Message, "has a GMSA cred spec set, but does not define the name of the corresponding resource")
	}
}

func TestCannotPreSetUnmatchingGMSASettings(t *testing.T) {
	testName := "cannot-pre-set-unmatching-gmsa-settings"
	credSpecTemplates := []string{"credspec-0"}
	templates := []string{"all-credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-pre-set-unmatching-contents"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	replicaSet := waitForReplicaSetGen1(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, int32(0), replicaSet.Status.Replicas)
	if assert.Equal(t, 1, len(replicaSet.Status.Conditions)) {
		condition := replicaSet.Status.Conditions[0]

		assert.Equal(t, condition.Reason, "FailedCreate")

		expectedSubstr := fmt.Sprintf("does not match the contents of GMSA resource %q", testConfig.CredSpecNames[0])
		assert.Contains(t, condition.Message, expectedSubstr)
	}
}

func TestCannotUpdateExistingPodLevelGMSASettings(t *testing.T) {
	testName := "cannot-update-gmsa-pod-level-settings"
	credSpecTemplates := []string{"credspec-0"}
	singlePodTemplate := "single-pod-with-gmsa"
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", singlePodTemplate}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	// let's check that the pod has come up correctly, and has the correct GMSA cred inlined
	pod, err := kubeClient(t).CoreV1().Pods(testConfig.Namespace).Get(context.Background(), testName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, expectedCredSpec0, extractPodCredSpecContents(t, pod))

	// now let's try to update the cred spec's content
	testConfig.CredSpecContent = expectedCredSpec1
	defer func() { testConfig.CredSpecContent = "" }()
	renderedTemplate := renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ := applyManifest(t, renderedTemplate)
	assert.False(t, success)

	// and same for its name
	testConfig.CredSpecNames[0] = "new-credspec"
	renderedTemplate = renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ = applyManifest(t, renderedTemplate)
	assert.False(t, success)
}

func TestCannotUpdateExistingContainerLevelGMSASettings(t *testing.T) {
	testName := "cannot-update-gmsa-container-level-settings"
	credSpecTemplates := []string{"credspec-0"}
	singlePodTemplate := "single-pod-with-container-level-gmsa"
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", singlePodTemplate}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	// let's check that the pod has come up correctly, and has the correct GMSA cred inlined
	pod, err := kubeClient(t).CoreV1().Pods(testConfig.Namespace).Get(context.Background(), testName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, testName))

	// now let's try to update the cred spec's content
	testConfig.CredSpecContent = expectedCredSpec1
	defer func() { testConfig.CredSpecContent = "" }()
	renderedTemplate := renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ := applyManifest(t, renderedTemplate)
	assert.False(t, success)

	// and same for its name
	testConfig.CredSpecNames[0] = "new-credspec"
	renderedTemplate = renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ = applyManifest(t, renderedTemplate)
	assert.False(t, success)
}

func TestHappyPathWithHostAgentConfigInCredSpec(t *testing.T) {
	testName := "happy-path-with-pod-level-cred-spec"
	credSpecTemplates := []string{"credspec-with-hostagentconfig"}
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)

	assert.Equal(t, expectedCredSpecWithHostAgentConfig, extractPodCredSpecContents(t, pod))
}

func TestPossibleToUpdatePodWithExistingGMSASettings(t *testing.T) {
	testName := "possible-to-update-pod-with-existing-gmsa-settings"
	credSpecTemplates := []string{"credspec-0", "credspec-1"}
	singlePodTemplate := "single-pod-with-gmsa"
	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", singlePodTemplate}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	// let's check that the pod has come up correctly, and has the correct GMSA cred inlined
	pod, err := kubeClient(t).CoreV1().Pods(testConfig.Namespace).Get(context.Background(), testName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, expectedCredSpec0, extractPodCredSpecContents(t, pod))

	// now let's update this pod
	testConfig.Image = "nginx"
	defer func() { testConfig.Image = "" }()
	renderedTemplate := renderTemplate(t, testConfig, singlePodTemplate)
	success, _, _ := applyManifest(t, renderedTemplate)
	assert.True(t, success)
}

func TestDeployV1Alpha1CredSpecGetAllVersions(t *testing.T) {
	testName := "deploy-v1alpha1-credspec-get-all-versions"
	credSpecTemplates := []string{"credspec-0", "credspec-1"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, nil)
	defer tearDownFunc()

	// ensure CredSpec specified v1 CRD
	templatePath := renderTemplate(t, testConfig, "credspec-1")
	b, err := ioutil.ReadFile(templatePath)
	if err != nil {
		t.Fatal(err)
	}
	s := string(b)
	assert.Contains(t, s, "apiVersion: windows.k8s.io/v1alpha1\n")

	client := dynamicClient(t)
	resourceName := "deploy-v1alpha1-credspec-get-all-versions-cred-spec-1"
	v1alpha1CredSpec, err := client.Resource(v1alpha1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	v1CredSpec, err := client.Resource(v1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	assert.Equal(t, v1alpha1CredSpec.Object["credSpec"], v1CredSpec.Object["credSpec"])
}

func TestDeployV1CredSpecGetAllVersions(t *testing.T) {
	testName := "deploy-v1-credspec-get-all-versions"
	credSpecTemplates := []string{"credspec-0", "credspec-1"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, nil)
	defer tearDownFunc()

	// ensure CredSpec specified v1 CRD
	templatePath := renderTemplate(t, testConfig, "credspec-0")
	b, err := ioutil.ReadFile(templatePath)
	if err != nil {
		t.Fatal(err)
	}
	s := string(b)
	assert.Contains(t, s, "apiVersion: windows.k8s.io/v1\n")

	client := dynamicClient(t)
	resourceName := "deploy-v1-credspec-get-all-versions-cred-spec-0"
	v1alpha1CredSpec, err := client.Resource(v1alpha1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	v1CredSpec, err := client.Resource(v1Resource).Get(context.TODO(), resourceName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	assert.Equal(t, v1alpha1CredSpec.Object["credSpec"], v1CredSpec.Object["credSpec"])
}

func TestPossibleToUpdatePodWithNewCert(t *testing.T) {
	/** TODO:
	 * - add a separate test to verify that requests to the webhook always return during this process
	 */

	webHookNs := os.Getenv("NAMESPACE")
	webHookDeploymentName := os.Getenv("DEPLOYMENT_NAME")
	webhook, err := kubeClient(t).AppsV1().Deployments(webHookNs).Get(context.Background(), webHookDeploymentName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	rotationEnabled := false
	for arg := range webhook.Spec.Template.Spec.Containers[0].Args {
		if strings.Contains(webhook.Spec.Template.Spec.Containers[0].Args[arg], "--cert-reload=true") {
			rotationEnabled = true
		}
	}

	if !rotationEnabled {
		t.Skip("Skipping test as rotation is not enabled")
	}

	testName := "possible-to-update-pod-with-new-cert"
	credSpecTemplates := []string{"credspec-0"}

	templates := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "single-pod-with-container-level-gmsa"}

	testConfig, tearDownFunc := integrationTestSetup(t, testName, credSpecTemplates, templates)
	defer tearDownFunc()

	pod := waitForPodToComeUp(t, testConfig.Namespace, "app="+testName)
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod, testName))

	deployMethod := os.Getenv("DEPLOY_METHOD")
	if deployMethod == "chart" {
		runCommandOrFail(t, "cmctl", "renew", webHookDeploymentName, "-n", webHookNs)

		var (
			timeout = 30 * time.Second
			start   = time.Now()
		)

		for {
			success, stdout, stderr := runKubectlCommand(t, "get", "certificaterequest", webHookNs+"-2", "--namespace", webHookNs, "-o", "jsonpath='{.status.conditions[?(@.type==\"Ready\")].status}'")
			if !success {
				fmt.Printf("Warning: command failed with %s, %s\n", stdout, stderr)
				continue
			}

			if stdout == "'True'" {
				break
			} else {
				fmt.Printf("Warning: status was %s", stdout)
			}

			if time.Since(start) >= timeout {
				t.Fatal("Timeout: Unable to get the certificate request status")
			}

			time.Sleep(1 * time.Second)
		}
	} else {
		/** TODO:
		     * - get a blessed certificate from the API server
			 *   (https://github.com/kubernetes-sigs/windows-gmsa/blob/141/admission-webhook/deploy/create-signed-cert.sh)
			 *   runCommandOrFail(t, fmt."create-signed-cert.sh --service $NAME --namespace $NAMESPACE --certs-dir $CERTS_DIR", testConfig.Namespace)
		     * - update existing secret in place and wait for the pod to get new secrets which can take time
			 *   (https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod) - similar to what you are doing here
		     * - kubectl exec into the running pod to see that the secret changed
			 *   (using utils like https://github.com/ycheng-kareo/windows-gmsa/blob/watch-reload-cert/admission-webhook/integration_tests/kube.go#L199)
		**/

		t.Skip("Non chart deployment method not supported for this test")
	}

	// it takes ~60 seconds for the webhook to pick up the new certificate
	// so this first run makes sure the old cert still works
	testName2 := testName + "after-rotation"
	testConfig2, tearDownFunc2 := integrationTestSetup(t, testName2, credSpecTemplates, templates)
	defer tearDownFunc2()

	pod2 := waitForPodToComeUp(t, testConfig2.Namespace, "app="+testName2)
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod2, testName2))

	// sleep a bit to ensure the the secret has been propagated to the pod
	time.Sleep(90 * time.Second)

	testName3 := testName + "after-rotation-propagated"
	testConfig3, tearDownFunc3 := integrationTestSetup(t, testName3, credSpecTemplates, templates)
	defer tearDownFunc3()

	pod3 := waitForPodToComeUp(t, testConfig3.Namespace, "app="+testName3)
	assert.Equal(t, expectedCredSpec0, extractContainerCredSpecContents(t, pod3, testName3))
}

func TestPossibleHostnameRandomization(t *testing.T) {
	deployMethod := os.Getenv("DEPLOY_METHOD")
	if deployMethod != "chart" {
		t.Skip("Non chart deployment method not supported for this test")
	}

	webHookNs := os.Getenv("NAMESPACE")
	webHookDeploymentName := os.Getenv("DEPLOYMENT_NAME")
	webhook, err := kubeClient(t).AppsV1().Deployments(webHookNs).Get(context.Background(), webHookDeploymentName, metav1.GetOptions{})
	if err != nil {
		t.Fatal(err)
	}

	randomHostnameEnabled := false
	for _, envVar := range webhook.Spec.Template.Spec.Containers[0].Env {
		if strings.EqualFold(envVar.Name, "RANDOM_HOSTNAME") && strings.EqualFold(envVar.Value, "true") {
			randomHostnameEnabled = true
		}
	}

	if randomHostnameEnabled {
		testName1 := "happy-path-with-hostname-randomization"
		credSpecTemplates1 := []string{"credspec-0"}
		templates1 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

		testConfig1, tearDownFunc1 := integrationTestSetup(t, testName1, credSpecTemplates1, templates1)
		defer tearDownFunc1()

		pod := waitForPodToComeUp(t, testConfig1.Namespace, "app="+testName1)
		assert.NotEqual(t, testName1, pod.Spec.Hostname)
		assert.Equal(t, 15, len(pod.Spec.Hostname))

		testName2 := "hostnameset-no-hostname-randomization"
		credSpecTemplates2 := []string{"credspec-0"}
		templates2 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa-hostname"}

		testConfig2, tearDownFunc2 := integrationTestSetup(t, testName2, credSpecTemplates2, templates2)
		defer tearDownFunc2()

		pod = waitForPodToComeUp(t, testConfig2.Namespace, "app="+testName2)
		assert.Equal(t, testName2, pod.Spec.Hostname)

		testName3 := "nogmsa-hostname-randomization"
		credSpecTemplates3 := []string{"credspec-0"}
		templates3 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-without-gmsa"}

		testConfig3, tearDownFunc3 := integrationTestSetup(t, testName3, credSpecTemplates3, templates3)
		defer tearDownFunc3()
		pod = waitForPodToComeUp(t, testConfig3.Namespace, "app="+testName3)

		assert.Equal(t, "", pod.Spec.Hostname)
	} else {
		testName4 := "notenabled-hostname-randomization"
		credSpecTemplates4 := []string{"credspec-0"}
		templates4 := []string{"credspecs-users-rbac-role", "service-account", "sa-rbac-binding", "simple-with-gmsa"}

		testConfig4, tearDownFunc4 := integrationTestSetup(t, testName4, credSpecTemplates4, templates4)
		defer tearDownFunc4()
		pod := waitForPodToComeUp(t, testConfig4.Namespace, "app="+testName4)

		assert.Equal(t, "", pod.Spec.Hostname)
	}
}

/* Helpers */

type testConfig struct {
	TestName           string
	Namespace          string
	TmpDir             string
	CredSpecNames      []string
	CredSpecContent    string
	ClusterRoleName    string
	ServiceAccountName string
	RoleBindingName    string
	Image              string
	ExtraSpecLines     []string
	Cert               string
	Key                string
}

// integrationTestSetup creates a new namespace to play in, and returns a function to
// tear it down afterwards.
// It also applies the given templates
func integrationTestSetup(t *testing.T, name string, credSpecTemplates, templates []string) (*testConfig, func()) {
	if _, err := os.Stat(tmpRoot); os.IsNotExist(err) {
		if err = os.Mkdir(tmpRoot, os.ModePerm); err != nil {
			t.Fatal(err)
		}
	}
	tmpDir, err := ioutil.TempDir(tmpRoot, name+"-")
	if err != nil {
		t.Fatal(err)
	}

	namespace := createNamespace(t, "")

	credSpecNames := make([]string, len(credSpecTemplates))
	for i := range credSpecTemplates {
		credSpecNames[i] = name + "-cred-spec-" + strconv.Itoa(i)
	}

	testConfig := &testConfig{
		TestName:  name,
		Namespace: namespace,
		TmpDir:    tmpDir,

		CredSpecNames:      credSpecNames,
		ClusterRoleName:    name + "-credspecs-users",
		ServiceAccountName: name + "-service-account",
		RoleBindingName:    name + "-use-credspecs",
	}

	if needMasterToleration(t) {
		testConfig.ExtraSpecLines = append(testConfig.ExtraSpecLines, masterToleration...)
	}

	templatePaths := make([]string, len(credSpecTemplates)+len(templates))
	for i, template := range append(credSpecTemplates, templates...) {
		templatePaths[i] = renderTemplate(t, testConfig, template)
		applyManifestOrFail(t, templatePaths[i])
	}

	tearDownFunc := func() {
		// helps speed us test when working locally against a throw-away cluster
		// deleting namespaces seems to be a rather heavy operation
		if _, present := os.LookupEnv("K8S_GMSA_ADMISSION_WEBHOOK_INTEGRATION_TEST_SKIP_CLEANUP"); present {
			return
		}

		for _, templatePath := range templatePaths {
			deleteManifest(t, templatePath)
		}

		deleteNamespace(t, namespace)
		if err := os.RemoveAll(tmpDir); err != nil {
			t.Fatal(err)
		}
	}

	return testConfig, tearDownFunc
}

var masterToleration = []string{
	"tolerations:",
	"- key: node-role.kubernetes.io/master",
	"  operator: Exists",
	"  effect: NoSchedule",
}

var allNodesHaveMasterTaint *bool

// needMasterToleration returns true iff all of the cluster's nodes have the master taint.
// Caches that in allNodesHaveMasterTaint.
// Not thread-safe.
func needMasterToleration(t *testing.T) bool {
	if allNodesHaveMasterTaint == nil {
		allMaster := true
		for _, node := range getNodes(t) {
			if !nodeHasMasterTaint(node) {
				allMaster = false
				break
			}
		}
		allNodesHaveMasterTaint = &allMaster
	}
	return *allNodesHaveMasterTaint
}

// renderTemplate renders a template, and returns its path.
func renderTemplate(t *testing.T, testConfig *testConfig, name string) string {
	if name[len(name)-len(ymlExtension):] != ymlExtension {
		name += ymlExtension
	}

	contents, err := ioutil.ReadFile(path.Join("templates", name))
	if err != nil {
		t.Fatal(err)
	}

	tplName := fmt.Sprintf("%s-%s", testConfig.Namespace, name)
	tpl, err := template.New(tplName).Parse(string(contents))
	if err != nil {
		t.Fatal(err)
	}

	renderedTemplate, err := os.Create(path.Join(testConfig.TmpDir, name))
	if err != nil {
		t.Fatal(err)
	}
	defer renderedTemplate.Close()

	if err = tpl.Execute(renderedTemplate, *testConfig); err != nil {
		t.Fatal(err)
	}

	return renderedTemplate.Name()
}

func extractPodCredSpecContents(t *testing.T, pod *corev1.Pod) string {
	if pod.Spec.SecurityContext == nil ||
		pod.Spec.SecurityContext.WindowsOptions == nil ||
		pod.Spec.SecurityContext.WindowsOptions.GMSACredentialSpec == nil {
		t.Fatalf("No pod cred spec")
	}
	return *pod.Spec.SecurityContext.WindowsOptions.GMSACredentialSpec
}

func extractContainerCredSpecContents(t *testing.T, pod *corev1.Pod, containerName string) string {
	for _, container := range pod.Spec.Containers {
		if container.Name == containerName {
			if container.SecurityContext == nil ||
				container.SecurityContext.WindowsOptions == nil ||
				container.SecurityContext.WindowsOptions.GMSACredentialSpec == nil {
				t.Fatalf("No cred spec for container %q", containerName)
			}
			return *container.SecurityContext.WindowsOptions.GMSACredentialSpec
		}
	}

	t.Fatalf("Did not find any container named %q", containerName)
	panic("won't happen, but required by the compiler")
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/kube.go`
```go
package integrationtests

import (
	"context"
	"fmt"
	"os"
	"testing"

	"github.com/mitchellh/go-homedir"
	"github.com/stretchr/testify/require"
	"gotest.tools/poll"
	appsv1 "k8s.io/api/apps/v1"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/dynamic"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
	"k8s.io/client-go/tools/clientcmd"
)

func clientConfig(t *testing.T) *rest.Config {
	kubeConfigPath, err := homedir.Expand(kubeconfig())
	if err != nil {
		t.Fatal(err)
	}
	config, err := clientcmd.BuildConfigFromFlags("", kubeConfigPath)
	if err != nil {
		t.Fatal(err)
	}

	return config
}

func kubeClient(t *testing.T) kubernetes.Interface {
	config := clientConfig(t)
	client, err := kubernetes.NewForConfig(config)
	if err != nil {
		t.Fatal(err)
	}

	return client
}

func dynamicClient(t *testing.T) dynamic.Interface {
	config := clientConfig(t)
	client, err := dynamic.NewForConfig(config)
	if err != nil {
		t.Fatal(err)
	}

	return client
}

// getNodes returns the nodes present in the cluster.
func getNodes(t *testing.T) []corev1.Node {
	client := kubeClient(t)

	nodeList, err := client.CoreV1().Nodes().List(context.Background(), metav1.ListOptions{})
	require.Nil(t, err, "Unable to list nodes")
	return nodeList.Items
}

// nodeHasMasterTaint returns true iff node has the canonical master taint.
func nodeHasMasterTaint(node corev1.Node) bool {
	for _, taint := range node.Spec.Taints {
		if taint.Key == "node-role.kubernetes.io/master" && taint.Effect == "NoSchedule" {
			return true
		}
	}
	return false
}

// waitForPodToComeUp waits for a pod matching `selector` to come up in `namespace`, and returns it.
func waitForPodToComeUp(t *testing.T, namespace, selector string, pollOps ...poll.SettingOp) *corev1.Pod {
	fetcher := func(client kubernetes.Interface, listOptions metav1.ListOptions) ([]interface{}, error) {
		podList, err := client.CoreV1().Pods(namespace).List(context.Background(), listOptions)
		if err == nil {
			result := make([]interface{}, len(podList.Items))
			for i, item := range podList.Items {
				result[i] = item
			}
			return result, nil
		}
		return nil, err
	}

	rawPod := waitForKubeObject(t, fetcher, namespace, selector, "pod", pollOps...)
	pod := rawPod.(corev1.Pod)
	return &pod
}

// waitForReplicaSet waits for a replica set matching `selector` to come up in `namespace`, and returns it.
func waitForReplicaSet(t *testing.T, namespace, selector string, pollOps ...poll.SettingOp) *appsv1.ReplicaSet {
	fetcher := func(client kubernetes.Interface, listOptions metav1.ListOptions) ([]interface{}, error) {
		rsList, err := client.AppsV1().ReplicaSets(namespace).List(context.Background(), listOptions)
		if err == nil {
			result := make([]interface{}, len(rsList.Items))
			for i, item := range rsList.Items {
				result[i] = item
			}
			return result, nil
		}
		return nil, err
	}

	rawReplicaSet := waitForKubeObject(t, fetcher, namespace, selector, "replica set", pollOps...)
	replicaSet := rawReplicaSet.(appsv1.ReplicaSet)
	return &replicaSet
}

// waitForReplicaSetGen1 waits for a given replica set to have its `Status.ObservedGeneration` field grow to > 0
// Comes in handy to wait for k8s to reach a decision for a given replicaset
func waitForReplicaSetGen1(t *testing.T, namespace, selector string, pollOps ...poll.SettingOp) *appsv1.ReplicaSet {
	replicaSet := waitForReplicaSet(t, namespace, selector, pollOps...)
	var err error

	client := kubeClient(t)

	pollingFunc := func(_ poll.LogT) poll.Result {
		replicaSet, err = client.AppsV1().ReplicaSets(namespace).Get(context.Background(), replicaSet.Name, metav1.GetOptions{})
		if err != nil {
			return poll.Error(err)
		}

		if replicaSet.Status.ObservedGeneration == 0 {
			return poll.Continue("replicaset %s is still at generation 0", replicaSet.Name)
		}
		return poll.Success()
	}

	poll.WaitOn(t, pollingFunc, pollOps...)

	return replicaSet
}

// waitForKubeObject waits for fetcher to return a list of one object matching `selector` in `namespace`, and returns it.
func waitForKubeObject(t *testing.T, fetcher func(kubernetes.Interface, metav1.ListOptions) ([]interface{}, error), namespace, selector, displayableName string, pollOps ...poll.SettingOp) (object interface{}) {
	client := kubeClient(t)
	listOptions := metav1.ListOptions{LabelSelector: selector}

	pollingFunc := func(_ poll.LogT) poll.Result {
		list, err := fetcher(client, listOptions)

		if err != nil {
			return poll.Error(err)
		}

		switch len(list) {
		case 0:
			return poll.Continue("no %s matching %s in namespace %s", displayableName, selector, namespace)
		case 1:
			object = list[0]
			return poll.Success()
		default:
			err = fmt.Errorf("expected no more than 1 %s matching %s in namespace %s, got %v", displayableName, selector, namespace, len(list))
			return poll.Error(err)
		}
	}

	poll.WaitOn(t, pollingFunc, pollOps...)

	return
}

const testNamespacePrefix = "gmsa-webhook-test-"

// value from https://github.com/kubernetes/kubernetes/blob/5e58841cce77d4bc13713ad2b91fa0d961e69192/pkg/volume/util/attach_limit.go#L53-L54
// removed so we didn't need to import the entire kubernetes source which is technically not supported
const resourceNameLengthLimit = 63

// createNamespace creates a new namespace, and fails the test if it already exists.
// if passed an empty string, it picks a random name and returns it.
func createNamespace(t *testing.T, name string) string {
	if name == "" {
		name = testNamespacePrefix + randomHexString(t, resourceNameLengthLimit-len(testNamespacePrefix))
	}

	runKubectlCommandOrFail(t, "create", "namespace", name)

	return name
}

func deleteNamespace(t *testing.T, name string) {
	runKubectlCommandOrFail(t, "delete", "namespace", name)
}

func applyManifestOrFail(t *testing.T, path string) {
	runKubectlCommandOrFail(t, "apply", "-f", path)
}

func applyManifest(t *testing.T, path string) (success bool, stdout string, stderr string) {
	return runKubectlCommand(t, "apply", "-f", path)
}

func deleteManifest(t *testing.T, path string) {
	runKubectlCommandOrFail(t, "delete", "-f", path)
}

func runKubectlCommandOrFail(t *testing.T, args ...string) {
	runCommandOrFail(t, kubectl(), args...)
}

func runKubectlCommand(t *testing.T, args ...string) (success bool, stdout string, stderr string) {
	return runCommand(t, kubectl(), args...)
}

func kubectl() string {
	return fromEnv("KUBECTL", "kubectl")
}

func kubeconfig() string {
	return fromEnv("KUBECONFIG", "~/.kube/config")
}

func fromEnv(key, defaultValue string) (value string) {
	if fromEnv, present := os.LookupEnv(key); present && fromEnv != "" {
		value = fromEnv
	} else {
		value = defaultValue
	}
	return
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/utils.go`
```go
package integrationtests

import (
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"os/exec"
	"testing"
)

func runCommandOrFail(t *testing.T, name string, args ...string) {
	success, stdout, stderr := runCommand(t, name, args...)
	if !success {
		t.Fatal(stdout, stderr)
	}
	fmt.Print(stdout)
}

func runCommand(t *testing.T, name string, args ...string) (success bool, stdout string, stderr string) {
	cmd := exec.Command(name, args...)
	stdoutReader, err := cmd.StdoutPipe()
	if err != nil {
		t.Fatal(err)
	}
	stderrReader, err := cmd.StderrPipe()
	if err != nil {
		t.Fatal(err)
	}

	success = true
	if err := cmd.Start(); err != nil {
		t.Fatal(err)
	}

	stdoutBytes, err := ioutil.ReadAll(stdoutReader)
	if err != nil {
		t.Fatal(err)
	}
	stderrBytes, err := ioutil.ReadAll(stderrReader)
	if err != nil {
		t.Fatal(err)
	}

	if err := cmd.Wait(); err != nil {
		if _, ok := err.(*exec.ExitError); ok {
			success = false
		} else {
			t.Fatal(err)
		}
	}

	return success, string(stdoutBytes), string(stderrBytes)
}

func randomHexString(t *testing.T, length int) string {
	b := length / 2
	randBytes := make([]byte, b)

	if n, err := rand.Reader.Read(randBytes); err != nil || n != b {
		if err == nil {
			err = fmt.Errorf("only got %v random bytes, expected %v", n, b)
		}
		t.Fatal(err)
	}

	return hex.EncodeToString(randBytes)
}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/all-credspecs-users-rbac-role.yml`
```yaml
# an RBAC role to grant `use` access to all credspecs

kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .ClusterRoleName }}
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["use"]
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/credspec-0.yml`
```yaml
# a sample cred spec

apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 0 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication0
      Scope: CONTOSO
    - Name: WebApplication0
      Scope: contoso.com
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication0
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524075714-3094792973
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/credspec-1.yml`
```yaml
# a sample cred spec
# Note: The apiVersion of this GMSACredentialSpec was intentionally left at windows.k8s.io/v1alpha1
#   to provide validation for scenarios where users deploy v1alpha CRD objects to their cluster after
#   updating the CRD definition to use windows.k8s.io/v1 as the storage version.

apiVersion: windows.k8s.io/v1alpha1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 1 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication1
      Scope: CONTOSO
    - Name: WebApplication1
      Scope: contoso.com
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication1
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524175714-3194792973
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/credspec-2.yml`
```yaml
# a sample cred spec

apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 2 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication2
      Scope: CONTOSO
    - Name: WebApplication2
      Scope: contoso.com
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication2
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524275714-3294792973
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/credspec-with-hostagentconfig.yml`
```yaml
# a sample cred spec

apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ index .CredSpecNames 0 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApplication2
      Scope: CONTOSO
    - Name: WebApplication2
      Scope: contoso.com
    HostAccountConfig:
      PluginGUID: "{GDMA0342-266A-4D1P-831J-20990E82944F}"
      PluginInput: "contoso.com:gmsaccg:<password>"
      PortableCcgVersion: "1"
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com
    DnsTreeName: contoso.com
    Guid: 244818ae-87ca-4fcd-92ec-e79e5252348a
    MachineAccountName: WebApplication2
    NetBiosName: CONTOSO
    Sid: S-1-5-21-2126729477-2524275714-3294792973
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/credspecs-users-rbac-role.yml`
```yaml
# an RBAC role to grant `use` access to some credspecs

kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .ClusterRoleName }}
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["use"]
  resourceNames:
{{- range $_, $csn := .CredSpecNames }}
    - {{ $csn }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/new-secret.yml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
data:
  tls_private_key: {{ .Key }}
  tls_certificate: {{ .Cert }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/sa-rbac-binding.yml`
```yaml
## an RBAC role binding for a service account

kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .RoleBindingName }}
  namespace: {{ .Namespace }}
subjects:
- kind: ServiceAccount
  name: {{ .ServiceAccountName }}
  namespace: {{ .Namespace }}
roleRef:
  kind: ClusterRole
  name: {{ .ClusterRoleName }}
  apiGroup: rbac.authorization.k8s.io
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/service-account.yml`
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ .ServiceAccountName }}
  namespace: {{ .Namespace }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/several-containers-with-gmsa.yml`
```yaml
## a simple deployment with several containers: 2 with their own GMSA, and 1 without it, plus a pod-level cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 1 }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx0
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
      - image: registry.k8s.io/pause
        name: nginx1
      - image: registry.k8s.io/pause
        name: nginx2
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: {{ index .CredSpecNames 2 }}
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-container-level-gmsa.yml`
```yaml
## a simple deployment with a container-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-gmsa-hostname.yml`
```yaml
## a simple deployment with a pod-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      hostname: {{ .TestName }}
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-gmsa.yml`
```yaml
## a simple deployment with a pod-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-pre-set-matching-contents.yml`
```yaml
## a simple deployment with a fully specified GMSA cred spec (ie both its name and contents)

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
          gmsaCredentialSpec: '{"CmsPlugins":["ActiveDirectory"],  "ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"DomainJoinConfig":{"Sid":"S-1-5-21-2126729477-2524075714-3094792973",  "DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO"}}'
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-pre-set-unmatching-contents.yml`
```yaml
## a simple deployment with a fully specified GMSA cred spec (ie both its name and contents);
## but where the specified contents don't match the name

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
          gmsaCredentialSpec: '{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication1","Scope":"CONTOSO"},{"Name":"WebApplication1","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication1","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524175714-3194792973"}}'
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-preset-gmsa-container-level-contents.yml`
```yaml
## a simple deployment with a container-level cred spec GMSA's *contents* already set (and not its name)

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
        securityContext:
          windowsOptions:
            gmsaCredentialSpec: '{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524075714-3094792973"}}'
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-preset-gmsa-pod-level-contents.yml`
```yaml
## a simple deployment with a pod-level cred spec GMSA's *contents* already set (and not its name)

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpec: '{"ActiveDirectoryConfig":{"GroupManagedServiceAccounts":[{"Name":"WebApplication0","Scope":"CONTOSO"},{"Name":"WebApplication0","Scope":"contoso.com"}]},"CmsPlugins":["ActiveDirectory"],"DomainJoinConfig":{"DnsName":"contoso.com","DnsTreeName":"contoso.com","Guid":"244818ae-87ca-4fcd-92ec-e79e5252348a","MachineAccountName":"WebApplication0","NetBiosName":"CONTOSO","Sid":"S-1-5-21-2126729477-2524075714-3094792973"}}'
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-with-unknown-gmsa.yml`
```yaml
## a simple deployment trying to use a pod-level GMSA cred spec that doesn't exist

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: i-sure-dont-exist
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/simple-without-gmsa.yml`
```yaml
## a simple deployment with a pod-level GMSA cred spec

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .TestName }}
  template:
    metadata:
      labels:
        app: {{ .TestName }}
    spec:
      serviceAccountName: {{ .ServiceAccountName }}
      containers:
      - image: registry.k8s.io/pause
        name: nginx
{{- range $line := .ExtraSpecLines }}
      {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/single-pod-with-container-level-gmsa.yml`
```yaml
## this deploys a single pod with a container-level GMSA cred spec

apiVersion: v1
kind: Pod
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  serviceAccountName: {{ .ServiceAccountName }}
  containers:
  - name: {{ .TestName }}
    image: registry.k8s.io/pause
    securityContext:
      windowsOptions:
        gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
{{- if .CredSpecContent }}
        gmsaCredentialSpec: '{{ .CredSpecContent }}'
{{- end }}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
{{- range $line := .ExtraSpecLines }}
  {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/integration_tests/templates/single-pod-with-gmsa.yml`
```yaml
## this deploys a single pod with a pod-level GMSA cred spec

apiVersion: v1
kind: Pod
metadata:
  labels:
    app: {{ .TestName }}
  name: {{ .TestName }}
  namespace: {{ .Namespace }}
spec:
  serviceAccountName: {{ .ServiceAccountName }}
  securityContext:
    windowsOptions:
      gmsaCredentialSpecName: {{ index .CredSpecNames 0 }}
{{- if .CredSpecContent }}
      gmsaCredentialSpec: '{{ .CredSpecContent }}'
{{- end }}
  containers:
  - name: nginx
{{- if .Image }}
    image: {{ .Image }}
{{- else }}
    image: registry.k8s.io/pause
{{- end }}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
{{- range $line := .ExtraSpecLines }}
  {{ $line }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/make/deps.mk`
```
.PHONY: deps_install
deps_install:
	go mod vendor

.PHONY: deps_update
deps_update:
	go mod tidy

.PHONY: deps_clean
deps_clean:
	rm -rf ./vendor
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/make/dev_cluster.mk`
```
# K8S version can be overriden
# see available versions at https://hub.docker.com/r/kindest/node/tags
KUBERNETES_VERSION ?= 1.29.0
# see https://github.com/kubernetes-sigs/kind/releases
KIND_VERSION = 0.22.0
# https://github.com/helm/helm/releases
HELM_VERSION ?= 3.14.3
# https://github.com/cert-manager/cert-manager/releases
CERT_MANAGER_VERSION ?= v1.14.4

CLUSTER_NAME ?= windows-gmsa-dev
DEPLOYMENT_NAME ?= windows-gmsa-dev
NAMESPACE ?= windows-gmsa-dev
NUM_NODES ?= 1

DEV_DIR = $(WEBHOOK_ROOT)/dev

CERTS_DIR = $(DEV_DIR)/certs_dir
MANIFESTS_FILE = $(DEV_DIR)/gmsa-webhook.yml

KIND = $(DEV_DIR)/kind-$(KIND_VERSION)
KIND_URL = https://github.com/kubernetes-sigs/kind/releases/download/v$(KIND_VERSION)/kind-$(UNAME)-amd64

KUBECTL = $(shell which kubectl 2> /dev/null)
KUBECTL_URL = https://dl.k8s.io/release/v$(KUBERNETES_VERSION)/bin/$(UNAME)/amd64/kubectl

ifeq ($(KUBECTL),)
KUBECTL = $(DEV_DIR)/kubectl-$(KUBERNETES_VERSION)
endif

KUBECONFIG?="$(HOME)/.kube/kind-config-$(CLUSTER_NAME)"

# starts a new kind cluster (see https://github.com/kubernetes-sigs/kind)
.PHONY: cluster_start
cluster_start: $(KIND) $(KUBECTL)
	./make/start_cluster.sh --name '$(CLUSTER_NAME)' --num-nodes $(NUM_NODES) --version $(KUBERNETES_VERSION) --kind-bin "$(KIND)"
	@ echo '### Kubectl version: ###'
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) version
	# coredns has a thing for creating API resources continually, which confuses the dry-run test
	# since it's not needed for anything here, there's no reason to keep it around
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) delete -n kube-system deployment.apps/coredns || true
	# kind removes the taint on master when NUM_NODES is 0 - but we do want to test that case too!
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) taint node $(CLUSTER_NAME)-control-plane 'node-role.kubernetes.io/master=true:NoSchedule' --overwrite
	#@ echo -e 'Cluster started, KUBECONFIG available at $(KUBECONFIG), eg\nexport KUBECONFIG=$(KUBECONFIG)'
	#@ $(MAKE) cluster_symlinks

# removes the kind cluster
.PHONY: cluster_clean
cluster_clean: $(KIND) clean_certs
	$(KIND) delete cluster --name '$(CLUSTER_NAME)'
	# also clean up any left over ci clusters from act
	$(KIND) delete cluster --name 'windows-gmsa-deploy-method-download'
	$(KIND) delete cluster --name 'windows-gmsa-dry-run-deploy'
	$(KIND) delete cluster --name 'windows-gmsa-integration'
	$(KIND) delete cluster --name 'windows-gmsa-tolerate-control-plane'

.PHONY: clean_certs
clean_certs:
	rm -rf $(CERTS_DIR)

# deploys the webhook to the kind cluster with the dev image
.PHONY: deploy_dev_webhook
deploy_dev_webhook:
	K8S_GMSA_IMAGE=$(DEV_IMAGE_NAME) $(MAKE) _deploy_webhook

# deploys the webhook to the kind cluster with the release image
.PHONY: deploy_webhook
deploy_webhook:
	K8S_GMSA_IMAGE=$(WEBHOOK_IMG):$(TAG) $(MAKE) _deploy_webhook

# removes the webhook from the kind cluster
.PHONY: remove_webhook
remove_webhook:
ifeq ($(wildcard $(MANIFESTS_FILE)),)
	@ echo "No manifests file found at $(MANIFESTS_FILE), nothing to remove"
else
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) delete -f $(MANIFESTS_FILE) || true
endif

# cluster_symlinks symlinks kubectl to dev/kubectl, and the kube config to dev/kubeconfig (used in ci)
.PHONY:
cluster_symlinks:
	ln -sfv $(KUBECTL) $(DEV_DIR)/kubectl-$(CLUSTER_NAME)
	ln -sfv $(KUBECONFIG) $(DEV_DIR)/kubeconfig-$(CLUSTER_NAME)

### "Private" targets below ###

# starts the kind cluster only if it's not already running
.PHONY: _start_cluster_if_not_running
_start_cluster_if_not_running: $(KUBECTL) $(KIND)
	$(MAKE) cluster_start

# deploys the webhook to the kind cluster
# if $K8S_GMSA_DEPLOY_METHOD is set to "download", then it will deploy by downloading
# the deploy script as documented in the README, using $K8S_GMSA_DEPLOY_DOWNLOAD_REPO and
# $K8S_GMSA_DEPLOY_DOWNLOAD_REV env variables to build the download URL. If REV is not set the current
# HEAD's SHA is used.
.PHONY: _deploy_webhook
_deploy_webhook: _copy_image remove_webhook
ifeq ($(K8S_GMSA_IMAGE),)
	@ echo "Cannot call target $@ without setting K8S_GMSA_IMAGE"
	exit 1
endif
	mkdir -p $(dir $(MANIFESTS_FILE))
ifeq ($(K8S_GMSA_DEPLOY_METHOD),download)
	@if [ ! "$$K8S_GMSA_DEPLOY_DOWNLOAD_REPO" ]; then K8S_GMSA_DEPLOY_DOWNLOAD_REPO="kubernetes-sigs/windows-gmsa"; fi \
      && if [ ! "$$K8S_GMSA_DEPLOY_DOWNLOAD_REV" ]; then K8S_GMSA_DEPLOY_DOWNLOAD_REV="$$(git rev-parse HEAD)"; fi \
      && CMD="curl -sL 'https://raw.githubusercontent.com/$$K8S_GMSA_DEPLOY_DOWNLOAD_REPO/$$K8S_GMSA_DEPLOY_DOWNLOAD_REV/admission-webhook/deploy/deploy-gmsa-webhook.sh' | K8S_GMSA_DEPLOY_DOWNLOAD_REPO='$$K8S_GMSA_DEPLOY_DOWNLOAD_REPO' K8S_GMSA_DEPLOY_DOWNLOAD_REV='$$K8S_GMSA_DEPLOY_DOWNLOAD_REV' KUBECONFIG=$(KUBECONFIG) KUBECTL=$(KUBECTL) bash -s -- --file '$(MANIFESTS_FILE)' --name '$(DEPLOYMENT_NAME)' --namespace '$(NAMESPACE)' --image '$(K8S_GMSA_IMAGE)' --certs-dir '$(CERTS_DIR)' $(EXTRA_GMSA_DEPLOY_ARGS)" \
      && echo "$$CMD" && eval "$$CMD"
else
	KUBECONFIG=$(KUBECONFIG) KUBECTL=$(KUBECTL) ./deploy/deploy-gmsa-webhook.sh --file "$(MANIFESTS_FILE)" --name "$(DEPLOYMENT_NAME)" --namespace "$(NAMESPACE)" --image "$(K8S_GMSA_IMAGE)" --certs-dir "$(CERTS_DIR)" $(EXTRA_GMSA_DEPLOY_ARGS)
endif

# copies the image to the kind cluster
.PHONY: _copy_image
_copy_image: _start_cluster_if_not_running
ifeq ($(K8S_GMSA_IMAGE),)
	@ echo "Cannot call target $@ without setting K8S_GMSA_IMAGE"
	exit 1
endif
	$(KIND) load docker-image $(K8S_GMSA_IMAGE) --name '$(CLUSTER_NAME)'

$(KIND):
	mkdir -vp "$$(dirname $(KIND))"
ifeq ($(WGET),)
	$(CURL) -L $(KIND_URL) > $(KIND)
else
	$(WGET) -O $(KIND) $(KIND_URL)
endif
	chmod +x $(KIND)

$(KUBECTL):
	mkdir -vp "$$(dirname $(KUBECTL))"
ifeq ($(WGET),)
	$(CURL) -L $(KUBECTL_URL) > $(KUBECTL)
else
	$(WGET) -O $(KUBECTL) $(KUBECTL_URL)
endif
	chmod +x $(KUBECTL)
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/make/helm.mk`
```
HELM = $(shell which helm 2> /dev/null)
HELM_URL = https://get.helm.sh/helm-v$(HELM_VERSION)-$(UNAME)-amd64.tar.gz

ifeq ($(HELM),)
HELM = $(DEV_DIR)/HELM-$(HELM_VERSION)
endif

.PHONY: install-helm
install-helm:
	curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

.PHONY: install-cmctl
install-cmctl:
	go install github.com/cert-manager/cmctl/v2@latest

.PHONY: helm-chart
helm-chart:
	$(HELM) package ../charts/gmsa -d ../charts/repo/

.PHONY: helm-index
helm-index:
	$(HELM) repo index ../charts/repo

.PHONY: helm-lint
helm-lint:
	$(HELM) lint ../charts/gmsa

# deploys the chart to the kind cluster with the release image
.PHONY: deploy_chart
deploy_chart: install-helm
	K8S_GMSA_IMAGE=$(WEBHOOK_IMG) $(MAKE) _deploy_chart

# removes the chart from the kind cluster
.PHONY: remove_chart
remove_chart:
	KUBECONFIG=$(KUBECONFIG) $(HELM) uninstall $(DEPLOYMENT_NAME) --namespace $(NAMESPACE)

# deploys the webhook to the kind cluster using helm
# if $K8S_GMSA_DEPLOY_METHOD is set to "download", then it will deploy by downloading
# the deploy script as documented in the README, using $K8S_GMSA_DEPLOY_CHART_REPO and
# $K8S_GMSA_DEPLOY_CHART_VERSION env variables to build the download URL. If VERSION is
# not set then latest is used.
# the HELM_INSTALL_FLAGS_FLAGS env var can be set to eg run only specific tests, e.g.:
# HELM_INSTALL_FLAGS_FLAGS='--set certificates.certReload.enabled=true' make deploy_chart
.PHONY: _deploy_chart
_deploy_chart:  _copy_image _deploy_certmanager install-cmctl
ifeq ($(K8S_GMSA_CHART),)
	@ echo "Cannot call target $@ without setting K8S_GMSA_CHART"
	exit 1
endif
	@ echo "installing helm deployment $(DEPLOYMENT_NAME) with chart $(K8S_GMSA_CHART) and image $(K8S_GMSA_IMAGE):$(TAG)"
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) create namespace $(NAMESPACE)
	KUBECONFIG=$(KUBECONFIG) $(HELM) version
	KUBECONFIG=$(KUBECONFIG) $(HELM) install $(DEPLOYMENT_NAME) $(K8S_GMSA_CHART) --set image.repository=$(K8S_GMSA_IMAGE) --set image.tag=$(TAG) --namespace $(NAMESPACE) $(HELM_INSTALL_FLAGS_FLAGS)
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) wait -n $(NAMESPACE) pod -l app=$(DEPLOYMENT_NAME) --for=condition=Ready

.PHONY: _deploy_certmanager
_deploy_certmanager: remove_certmanager
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) create namespace cert-manager
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) apply -f https://github.com/cert-manager/cert-manager/releases/download/$(CERT_MANAGER_VERSION)/cert-manager.yaml
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) wait -n cert-manager pod -l app=cainjector --for=condition=Ready
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) wait -n cert-manager pod -l app=webhook --for=condition=Ready
	
.PHONY: remove_certmanager
remove_certmanager:
	KUBECONFIG=$(KUBECONFIG) $(KUBECTL) delete namespace cert-manager || true
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/make/image.mk`
```
# must stay consistent with the go version defined in .travis.yml
GO_VERSION = 1.23
BUILD_ARGS = --build-arg GO_VERSION=$(GO_VERSION) --build-arg VERSION=$(TAG) 
DOCKER_BUILD = docker build . $(BUILD_ARGS)

AMD64_ARGS = --build-arg GOARCH=amd64 --build-arg ARCH=amd64 --platform=linux/amd64
ARM64_ARGS = --build-arg GOARCH=arm64 --build-arg ARCH=arm64 --platform=linux/arm64
BUILDX_BUILD = docker buildx build . $(BUILD_ARGS) --provenance=false --sbom=false


.PHONY: image_build_dev
image_build_dev:
	$(DOCKER_BUILD) -f dockerfiles/Dockerfile.dev -t $(DEV_IMAGE_NAME)

.PHONY: create_buildx_builder
create_buildx_builder:
	docker buildx create --name img-builder --platform linux/amd64 --use

.PHONY: remove_image_builder
remove_image_builder:
	docker buildx rm img-builder || true

# Builds an amd64 image and loads it into the local image store - used during integration tests
image_build: remove_image_builder create_buildx_builder image_build_int remove_image_builder

.PHONY: image_build_int
image_build_int:
	$(BUILDX_BUILD) --load $(AMD64_ARGS) -f dockerfiles/Dockerfile -t $(WEBHOOK_IMG):$(TAG) -t $(WEBHOOK_IMG):latest

# Builds and pushes a multi-arch image (amd64 and arm64) to a remote registry
image_build_and_push: remove_image_builder create_buildx_builder image_build_and_push_int remove_image_builder

.PHONY: image_build_and_push_int
image_build_and_push_int:
	$(BUILDX_BUILD) --push $(AMD64_ARGS) -f dockerfiles/Dockerfile -t $(WEBHOOK_IMG):$(TAG)-amd64 -t $(WEBHOOK_IMG):latest-amd64
	$(BUILDX_BUILD) --push $(ARM64_ARGS) -f dockerfiles/Dockerfile -t $(WEBHOOK_IMG):$(TAG)-arm64 -t $(WEBHOOK_IMG):latest-arm64
	docker manifest create --amend $(WEBHOOK_IMG):$(TAG) $(WEBHOOK_IMG):$(TAG)-amd64 $(WEBHOOK_IMG):$(TAG)-arm64
	docker manifest push --purge $(WEBHOOK_IMG):$(TAG)
	docker manifest create --amend $(WEBHOOK_IMG):latest $(WEBHOOK_IMG):latest-amd64 $(WEBHOOK_IMG):latest-arm64
	docker manifest push --purge $(WEBHOOK_IMG):latest
```

## File: `kubernetes-sigs-windows-gmsa-993de21/admission-webhook/make/start_cluster.sh`
```bash
#!/usr/bin/env bash

set -e

usage() {
    cat <<EOF
Light wrapper around kind that generates the right configuration file for kind, then starts the cluster.

usage: $0 --name NAME --num-nodes NUM_NODES --version VERSION [--kind-bin KIND_BIN]

NAME is the kind cluster name.
NUM_NODES is the number of worker nodes.
VERSION is the k8s version to use.
KIND_BIN is the path to the kind executable.
EOF
    exit 1
}

setkubeconfig() {
    mkdir -p ~/.kube
    $KIND_BIN get kubeconfig --name "$NAME" >  ~/.kube/kind-config-$NAME
}

main() {
    local NAME=
    local NUM_NODES=
    local VERSION=
    local KIND_BIN=kind

    # parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --name)
                NAME="$2" ;;
            --num-nodes)
                NUM_NODES="$2" ;;
            --version)
                VERSION="$2" ;;
            --kind-bin)
                KIND_BIN="$2" ;;
            *)
                echo "Unknown option: $1"
                usage ;;
        esac
        shift 2
    done

    [ "$NAME" ] && [ "$NUM_NODES" ] && [ "$VERSION" ] || usage

    if [[ "$(${KIND_BIN} get clusters)" == *"${NAME}"* ]]; then
  	  echo "Dev cluster already running. Skipping cluster creation"
      setkubeconfig
  	  exit 0
  	else
  	  echo "Starting new cluster";
  	fi

    local CONFIG_FILE
    CONFIG_FILE="$(mktemp /tmp/gmsa-webhook-kind-config.XXXXXXX)"

    # generate the config file
    cat <<EOF > "$CONFIG_FILE"
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
kubeadmConfigPatches:
- |
  apiVersion: kubeadm.k8s.io/v1beta2
  kind: ClusterConfiguration
  metadata:
    name: config
  apiServer:
    extraArgs:
      enable-admission-plugins: NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook
EOF
    cat <<EOF >> "$CONFIG_FILE"
nodes:
- role: control-plane
EOF
    for _ in $(seq "$NUM_NODES"); do
        echo -e '- role: worker' >> "$CONFIG_FILE"
    done

    # run kind
    local EXIT_STATUS=0
    $KIND_BIN create cluster --name "$NAME" --config "$CONFIG_FILE" --image "kindest/node:v$VERSION" --wait 240s || EXIT_STATUS=$?
    setkubeconfig

    # clean up the config file
    rm -f "$CONFIG_FILE"

    return $EXIT_STATUS
}

main "$@"
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/README.md`
```markdown
# Install Windows GMSA with Helm 3

## Prerequisites

- [install Helm](https://helm.sh/docs/intro/quickstart/#install-helm)

### Tips

### install a specific version

```console
helm repo add windows-gmsa https://raw.githubusercontent.com/kubernetes-sigs/windows-gmsa/master/charts/repo
helm install windows-gmsa/gmsa --namespace kube-system --version v0.4.4
```

### search for all available chart versions

```console
helm search repo -l gmsa
```

## uninstall Windows GMSA

```console
helm uninstall gmsa -n kube-system
```

## latest chart configuration

The following table lists the configurable parameters of the latest GMSA chart and default values.

| Parameter                                          | Description                                                           | Default                                         |
| -------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------- |
| `certificates.certManager.enabled`                 | enable cert manager integration                                       | `true`                                          |
| `certificates.certManager.version`                 | version of cert manager                                               |                                                 |
| `certificates.caBundle`                            | cert-manager disabled, add self-signed ca.crt in base64 format        |                                                 |
| `certificates.secretName`                          | cert-manager disabled, upload certs data as k8s secretName            | `gmsa-server-cert`                              |
| `certificates.certReload.enabled`                  | enable cert reload on changes                                         | `false`                                         |
| `credential.enabled`                               | enable creation of GMSA Credential                                    | `true`                                          |
| `credential.domainJoinConfig.dnsName`              | DNS Domain Name                                                       |                                                 |
| `credential.domainJoinConfig.dnsTreeName`          | DNS Domain Name Root                                                  |                                                 |
| `credential.domainJoinConfig.guid`                 | GUID                                                                  |                                                 |
| `credential.domainJoinConfig.machineAccountName`   | username of the GMSA account                                          |                                                 |
| `credential.domainJoinConfig.netBiosName`          | NETBIOS Domain Name                                                   |                                                 |
| `credential.domainJoinConfig.sid`                  | SID                                                                   |                                                 |
| `credential.hostAccountConfig.pluginGUID`          | GUID of CCG Plugin                                                    |                                                 |
| `credential.hostAccountConfigg.portableCcgVersion` | Version of CCG Plugin                                                 | `1`                                             |
| `credential.hostAccountConfig.pluginInput`         | Input to CCG Plugin                                                   |                                                 |
| `image.repository`                                 | image repository                                                      | `registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook` |
| `image.tag`                                        | image tag                                                             | `v0.4.0`                                        |
| `image.imagePullPolicy`                            | image pull policy                                                     | `IfNotPresent`                                  |
| `global.systemDefaultRegistry`                     | container registry                                                    |                                                 |
| `tolerations`                                      | tolerations                                                           | []                                              |
| `setPodOs`                                         | Enables setting of `OS` field on Pod for supported K8s versions       | `true`                                          |
| `viewerRole`                                       | Enable aggregation of `gmsacredentialspecs` to the built-in view role | `false`                                         |

## troubleshooting

- Add `--wait -v=5 --debug` in `helm install` command to get detailed error
- Use `kubectl describe` to acquire more info
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/Chart.yaml`
```yaml
apiVersion: v2
appVersion: 0.13.0
description: Windows GMSA Configuration
keywords:
- Windows
- Windows GMSA
- GMSA
- Active Directory
name: gmsa
sources:
- https://github.com/kubernetes-sigs/windows-gmsa
type: application
version: 0.13.0
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/app-readme.md`
```markdown
# Windows GMSA Admission Webhook

This chart creates the GMSA CRD, Credential, and Admission Webhook. The official documentation and tutorials can be found [here](https://github.com/kubernetes-sigs/windows-gmsa).

## Prerequisites

- Active Directory that supports Group Managed Service Accounts
- A Group Managed Service Account
- Kubernetes v1.23+
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/values.yaml`
```yaml
certificates:
  certManager:
    # Enable cert manager integration. Cert manager should be already installed at the k8s cluster
    enabled: true
    version: "v1.16.2"
  # If cert-manager integration is disabled, add self-signed ca.crt in base64 format
  caBundle: ""
  # If cert-manager integration is disabled, upload certs data (ca.crt, tls.crt and tls.key) as k8s secretName in the namespace
  secretName: gmsa-server-cert
  certReload:
    # Enable cert reload when the certs change
    enabled: false

credential:
  enabled: false
  hostAccountConfig: {}
    # pluginGUID: "" # CCG Plugin GUID
    # portableCcgVersion: "1" # This needs to equal the current version of CCG which right now is '1'
    # pluginInput: "" # Format of this field is dependent upon specific CCG Plugin
  domainJoinConfig:
    dnsName: "" # DNS Domain Name
    dnsTreeName: "" # DNS Domain Name Root
    guid: "" # GUID of Domain
    machineAccountName: "" # Username of the GMSA account
    netBiosName: "" # NETBIOS Domain Name
    sid: "" # SID of Domain

containerPort: "443"

image:
  repository: registry.k8s.io/gmsa-webhook/k8s-gmsa-webhook
  tag: v0.13.0
  imagePullPolicy: IfNotPresent

# If true, will add os fields to pod specs for K8s versions where feature is in beta (v1.24+)
setPodOs: true

global:
  systemDefaultRegistry: ""

affinity: {}
nodeSelector: {}
podDisruptionBudget:
  enabled: false
  # minAvailable: 1
  # maxUnavailable: 1

podSecurityContext: {}

# Enable aggregation of GMSA resources to the built-in view role
viewerRole: false

replicaCount: 2
securityContext: {}
tolerations: []
qps: 30.0
burst: 50
randomHostname: false
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/crds/crds.yaml`
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: gmsacredentialspecs.windows.k8s.io
  annotations:
    "api-approved.kubernetes.io": "https://github.com/kubernetes/enhancements/tree/master/keps/sig-windows/689-windows-gmsa"
spec:
  group: windows.k8s.io
  versions:
    - name: v1alpha1
      served: true
      storage: false
      deprecated: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            credspec:
              description: GMSA Credential Spec
              type: object
              properties:
                ActiveDirectoryConfig:
                  type: object
                  properties:
                    GroupManagedServiceAccounts:
                      type: array
                      items:
                        type: object
                        properties:
                          Name:
                            type: string
                          Scope:
                            type: string
                    HostAccountConfig:
                      type: object
                      properties:
                        PluginGUID:
                          type: string
                        PluginInput:
                          type: string
                        PortableCcgVersion:
                          type: string
                CmsPlugins:
                  type: array
                  items:
                    type: string
                DomainJoinConfig:
                  type: object
                  properties:
                    DnsName:
                      type: string
                    DnsTreeName:
                      type: string
                    Guid:
                      type: string
                    MachineAccountName:
                      type: string
                    NetBiosName:
                      type: string
                    Sid:
                      type: string
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            credspec:
              description: GMSA Credential Spec
              type: object
              properties:
                ActiveDirectoryConfig:
                  type: object
                  properties:
                    GroupManagedServiceAccounts:
                      type: array
                      items:
                        type: object
                        properties:
                          Name:
                            type: string
                          Scope:
                            type: string
                    HostAccountConfig:
                      type: object
                      properties:
                        PluginGUID:
                          type: string
                        PluginInput:
                          type: string
                        PortableCcgVersion:
                          type: string
                CmsPlugins:
                  type: array
                  items:
                    type: string
                DomainJoinConfig:
                  type: object
                  properties:
                    DnsName:
                      type: string
                    DnsTreeName:
                      type: string
                    Guid:
                      type: string
                    MachineAccountName:
                      type: string
                    NetBiosName:
                      type: string
                    Sid:
                      type: string
  conversion:
    strategy: None
  names:
    kind: GMSACredentialSpec
    plural: gmsacredentialspecs
  scope: Cluster

```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/_helpers.tpl`
```
{{- define "system_default_registry" -}}
{{- if .Values.global.systemDefaultRegistry -}}
{{- printf "%s/" .Values.global.systemDefaultRegistry -}}
{{- end -}}
{{- end -}}

{{/* Create chart name and version as used by the chart label. */}}
{{- define "gmsa.chartref" -}}
chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
{{- end }}

{{/* Determine apiVersion for cert-manager */}}
{{- define "cert-manager.apiversion" -}}
  {{- $certmanagerVer :=  split "." .Values.certificates.certManager.version -}}
  {{- if or (.Capabilities.APIVersions.Has "cert-manager.io/v1") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 1) (ge (int $certmanagerVer._1) 0)) }}
apiVersion: cert-manager.io/v1
  {{- else if or (.Capabilities.APIVersions.Has "cert-manager.io/v1beta1") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 0) (ge (int $certmanagerVer._1) 16)) }}
apiVersion: cert-manager.io/v1beta1
  {{- else if or (.Capabilities.APIVersions.Has "cert-manager.io/v1alpha2") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 0) (ge (int $certmanagerVer._1) 11)) }}
apiVersion: cert-manager.io/v1alpha2
  {{- else if or (.Capabilities.APIVersions.Has "certmanager.k8s.io/v1alpha1") (and (gt (len $certmanagerVer._0) 0) (eq (int $certmanagerVer._0) 0) (lt (int $certmanagerVer._1) 11)) }}
apiVersion: cert-manager.io/v1alpha1
  {{- else }}
apiVersion: cert-manager.io/v1
  {{- end }}
{{- end }}

{{- define "certificates.cabundle"}}
{{- if .Values.certificates.caBundle }}
{{- .Values.certificates.caBundle }}
{{- else if gt (len (lookup "rbac.authorization.k8s.io/v1" "ClusterRole" "" "")) 0 -}}
{{- $secret := (lookup "v1" "Secret" .Release.Namespace .Values.certificates.secretName) -}}
{{- if lt (len $secret) 1 -}}
{{- required (printf "CA Bundle secret '%s' in namespace '%s' must exist" .Values.certificates.secretName .Release.Namespace) "" -}}
{{- else -}}
{{- if not (hasKey $secret "data") -}}
{{- required (printf "CA Bundle secret '%s' in namespace '%s' is empty" .Values.certificates.secretName .Release.Namespace) "" -}}
{{- end -}}
{{- if or (not (hasKey $secret.data "ca.crt")) (not (hasKey $secret.data "tls.crt")) (not (hasKey $secret.data "tls.key")) -}}
{{- required (printf "CA Bundle secret '%s' in namespace '%s' must contain ca.crt, tls.key, and tls.cert; found the following keys in the secret: %s" .Values.certificates.secretName .Release.Namespace $secret.data) "" -}}
{{- end -}}
{{- end -}}
{{- get $secret.data "ca.crt" }}
{{- else -}}
INSERT_CERTIFICATE_FROM_SECRET
{{- end -}}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/clusterrole.yaml`
```yaml
# the RBAC role that the webhook needs to:
#  * read GMSA custom resources
#  * check authorizations to use GMSA cred specs
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .Release.Name }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
rules:
  - apiGroups: ["windows.k8s.io"]
    resources: ["gmsacredentialspecs"]
    verbs: ["get", "use"]
  - apiGroups: ["authorization.k8s.io"]
    resources: ["localsubjectaccessreviews"]
    verbs: ["create"]
---
{{- if .Values.viewerRole }}
# allow visibility of gmsacredentialspecs through built-in "view" role
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .Release.Name }}-viewer-role
  labels:
    {{ include "gmsa.chartref" . }}
    rbac.authorization.k8s.io/aggregate-to-view: "true"
rules:
  - apiGroups: ["windows.k8s.io"]
    resources: ["gmsacredentialspecs"]
    verbs: ["get", "list", "watch"]
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/clusterrolebinding.yaml`
```yaml
# bind that role to the webhook's service account
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: {{ .Release.Name }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
subjects:
  - kind: ServiceAccount
    name: {{ .Release.Name }}
    namespace: {{ .Release.Namespace }}
roleRef:
  kind: ClusterRole
  name: {{ .Release.Name }}
  apiGroup: rbac.authorization.k8s.io
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/credentialspec.yaml`
```yaml
{{- if .Values.credential.enabled -}}
apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: {{ lower .Values.credential.domainJoinConfig.machineAccountName | replace "_" "-" }}  #This is an arbitrary name but it will be used as a reference
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
      - Name: {{ .Values.credential.domainJoinConfig.machineAccountName }} # Username of the GMSA account
        Scope: {{ .Values.credential.domainJoinConfig.netBiosName }} # NETBIOS Domain Name
      - Name: {{ .Values.credential.domainJoinConfig.machineAccountName }} # Username of the GMSA account
        Scope: {{ .Values.credential.domainJoinConfig.dnsName }} # DNS Domain Name
{{- if .Values.credential.hostAccountConfig }}
    HostAccountConfig:
      PortableCcgVersion: {{ required "credential.hostAccountConfig.portableCCGVersion must be provided if credential.hostAccountConfig is set" .Values.credential.hostAccountConfig.portableCcgVersion | quote }} # This needs to equal the current version of CCG which right now is '1'
      PluginGUID:   {{ printf "{%s}" (required "credential.hostAccountConfig.pluginGUID must be provided if credential.hostAccountConfig is set" .Values.credential.hostAccountConfig.pluginGUID) | quote }} # CCG Plugin GUID
      PluginInput: {{ required "credential.hostAccountConfig.pluginInput must be provided if credential.hostAccountConfig is set" .Values.credential.hostAccountConfig.pluginInput | quote }} # Format of this field is dependent upon specific CCG Plugin
{{- end }}
  CmsPlugins:
    - ActiveDirectory
  DomainJoinConfig:
    DnsName: {{ .Values.credential.domainJoinConfig.dnsName }} # DNS Domain Name
    DnsTreeName:  {{ .Values.credential.domainJoinConfig.dnsTreeName }} # DNS Domain Name Root
    Guid:  {{ .Values.credential.domainJoinConfig.guid }} # GUID of Domain
    MachineAccountName:  {{ .Values.credential.domainJoinConfig.machineAccountName }} # Username of the GMSA account
    NetBiosName:  {{ .Values.credential.domainJoinConfig.netBiosName }} # NETBIOS Domain Name
    Sid:  {{ .Values.credential.domainJoinConfig.sid }} # SID of Domain
{{- end -}}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      {{- if .Values.podSecurityContext }}
      securityContext: {{ toYaml .Values.podSecurityContext | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ .Release.Name }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      nodeSelector:
        kubernetes.io/os: linux
      {{- with .Values.nodeSelector }}
        {{- toYaml . | nindent 8 }}
      {{- end }}
      containers:
        - name: {{ .Release.Name }}
          image: '{{ template "system_default_registry" . }}{{ .Values.image.repository }}:{{ .Values.image.tag }}'
          imagePullPolicy: {{ .Values.image.imagePullPolicy }}
          readinessProbe:
            httpGet:
              scheme: HTTPS
              path: /health
              port: {{ .Values.containerPort }}
          ports:
            - containerPort: {{ .Values.containerPort }}
          volumeMounts:
            - name: tls
              mountPath: "/tls"
              readOnly: true
          env:
            - name: TLS_KEY
              value: /tls/key
            - name: TLS_CRT
              value: /tls/crt
            - name: HTTPS_PORT
              value: "{{ .Values.containerPort }}"
            - name: BURST
              value: "{{ .Values.burst }}"
            - name: QPS
              value: "{{ .Values.qps }}"
            - name: RANDOM_HOSTNAME
              value: "{{ .Values.randomHostname }}"
          {{- if .Values.securityContext }}
          securityContext: {{ toYaml .Values.securityContext | nindent 12 }}
          {{- end }}
          args:
            - --cert-reload={{ .Values.certificates.certReload.enabled }}
      volumes:
        - name: tls
          secret:
            secretName: {{ .Values.certificates.secretName }}
            items:
              - key: tls.key
                path: key
              - key: tls.crt
                path: crt
      {{- if and (.Values.setPodOs) (ge .Capabilities.KubeVersion.Minor "24")}}
      os:
        name: linux
      {{- end -}}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/issuer.yaml`
```yaml
{{- if .Values.certificates.certManager.enabled -}}
{{ template "cert-manager.apiversion" . }}
kind: Certificate
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  dnsNames:
    - {{ .Release.Name }}.{{ .Release.Namespace }}.svc
    - {{ .Release.Name }}.{{ .Release.Namespace }}.svc.cluster.local
  issuerRef:
    kind: Issuer
    name: {{ .Release.Name }}
  secretName: {{ .Values.certificates.secretName }}
  {{- if .Values.certificates.certReload.enabled }}
  privateKey:
    rotationPolicy: Always
  {{- end }}
---
{{ template "cert-manager.apiversion" . }}
kind: Issuer
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  ca:
    secretName: {{ .Release.Name }}-root-ca
---
{{ template "cert-manager.apiversion" . }}
kind: ClusterIssuer
metadata:
  name: {{ .Release.Name }}-ca
spec:
  selfSigned: {}
---
{{ template "cert-manager.apiversion" . }}
kind: Certificate
metadata:
  name: {{ .Release.Name }}-ca
  namespace: {{ .Release.Namespace }}
spec:
  isCA: true
  commonName: {{ .Release.Name }}-ca
  secretName: {{ .Release.Name }}-root-ca
  issuerRef:
    name: {{ .Release.Name }}-ca
    kind: ClusterIssuer
    group: cert-manager.io
---
{{- end -}}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/mutatingwebhook.yaml`
```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: {{ .Release.Name }}
  {{- if .Values.certificates.certManager.enabled }}
  annotations:
    cert-manager.io/inject-ca-from: {{ .Release.Namespace }}/{{ .Release.Name }}-ca
  {{- end }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
webhooks:
  - name: admission-webhook.windows-gmsa.sigs.k8s.io
    clientConfig:
      service:
        name: {{ .Release.Name }}
        namespace: {{.Release.Namespace}}
        path: "/mutate"
      {{- if not (.Values.certificates.certManager.enabled) }}
      caBundle: {{ template "certificates.cabundle" . }}
      {{- end }}
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["*"]
        resources: ["pods"]
    failurePolicy: Fail
    admissionReviewVersions: ["v1", "v1beta1"]
    sideEffects: None
    # don't run on ${NAMESPACE}
    namespaceSelector:
      matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values: [{{ .Release.Namespace }}]
        - key: windows.k8s.io/disabled
          operator: NotIn
          values: ["true"]
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/pdb.yaml`
```yaml
{{- if .Values.podDisruptionBudget.enabled }}
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels:  {{ include "gmsa.chartref" . | nindent 4 }}
spec:
{{- if .Values.podDisruptionBudget.minAvailable }}
  minAvailable: {{ .Values.podDisruptionBudget.minAvailable }}
{{- end }}
{{- if .Values.podDisruptionBudget.maxUnavailable }}
  maxUnavailable: {{ .Values.podDisruptionBudget.maxUnavailable }}
{{- end }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
{{- end }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
spec:
  ports:
    - port: 443
      targetPort: {{ .Values.containerPort }}
  selector:
    app: {{ .Release.Name }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/serviceaccount.yaml`
```yaml
# the service account for the webhook
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ .Release.Name }}
  namespace: {{ .Release.Namespace }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/gmsa/templates/validatingwebhook.yaml`
```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: {{ .Release.Name }}
  {{- if .Values.certificates.certManager.enabled }}
  annotations:
    cert-manager.io/inject-ca-from: {{ .Release.Namespace }}/{{ .Release.Name }}-ca
  {{- end }}
  labels: {{ include "gmsa.chartref" . | nindent 4 }}
webhooks:
  - name: admission-webhook.windows-gmsa.sigs.k8s.io
    clientConfig:
      service:
        name: {{ .Release.Name }}
        namespace: {{ .Release.Namespace }}
        path: "/validate"
      {{- if not (.Values.certificates.certManager.enabled) }}
      caBundle: {{ template "certificates.cabundle" . }}
      {{- end }}
    rules:
      - operations: ["CREATE", "UPDATE"]
        apiGroups: [""]
        apiVersions: ["*"]
        resources: ["pods"]
    failurePolicy: Fail
    admissionReviewVersions: ["v1", "v1beta1"]
    sideEffects: None
    # don't run on ${NAMESPACE}
    namespaceSelector:
      matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: NotIn
          values: [{{ .Release.Namespace }}]
        - key: windows.k8s.io/disabled
          operator: NotIn
          values: ["true"]
```

## File: `kubernetes-sigs-windows-gmsa-993de21/charts/repo/index.yaml`
```yaml
apiVersion: v1
entries:
  gmsa:
  - apiVersion: v2
    appVersion: 0.13.0
    created: "2025-03-14T19:52:28.477888534Z"
    description: Windows GMSA Configuration
    digest: d129b67f17b0d634a86a3573b760b518006bce53f56d677db4009049a51323bc
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.13.0.tgz
    version: 0.13.0
  - apiVersion: v2
    appVersion: 0.12.1
    created: "2025-03-14T19:52:28.47506763Z"
    description: Windows GMSA Configuration
    digest: bfc10d609983b41154f10fdbf3e4aed7ecd8b0ea48a4595ae5482db408787003
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.12.1.tgz
    version: 0.12.1
  - apiVersion: v2
    appVersion: 0.12.0
    created: "2025-03-14T19:52:28.472641525Z"
    description: Windows GMSA Configuration
    digest: b941f044d359dd4dfe7f5f9820e7f1243d5c43189e30eb28c9ebb570fa271d0d
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.12.0.tgz
    version: 0.12.0
  - apiVersion: v2
    appVersion: 0.11.0
    created: "2025-03-14T19:52:28.470961223Z"
    description: Windows GMSA Configuration
    digest: 46ab09c040c6aa5c908d9bfa30974e7dfd49a79cb69a55299b25cfa19d32465a
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.11.0.tgz
    version: 0.11.0
  - apiVersion: v2
    appVersion: 0.10.0
    created: "2025-03-14T19:52:28.46934612Z"
    description: Windows GMSA Configuration
    digest: 0d05c3750b9178124329d75dde218633557df594a69d60498abc38b138b45b1b
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.10.0.tgz
    version: 0.10.0
  - apiVersion: v2
    appVersion: 0.9.0
    created: "2025-03-14T19:52:28.486489549Z"
    description: Windows GMSA Configuration
    digest: f1757c9d665f98c18f81cb17a7cc6665ef6fcb63defa147fd7bec26e7fee31a1
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.9.0.tgz
    version: 0.9.0
  - apiVersion: v2
    appVersion: 0.8.0
    created: "2025-03-14T19:52:28.485595048Z"
    description: Windows GMSA Configuration
    digest: ec5a66b684c6507239d9fb9e08b71e910f6b097118efb7a29ffb4fb34ec385f3
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.8.0.tgz
    version: 0.8.0
  - apiVersion: v2
    appVersion: 0.7.0
    created: "2025-03-14T19:52:28.485025547Z"
    description: Windows GMSA Configuration
    digest: 8ff367280c392b406da60eb249b695b54de9d85b26c600628b6ffac13c1c9df7
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.3.tgz
    version: 0.7.3
  - apiVersion: v2
    appVersion: 0.7.0
    created: "2025-03-14T19:52:28.484422046Z"
    description: Windows GMSA Configuration
    digest: 97fc3964eabebb3cbe9ac7caf8ae7476a2f9371e508b2381e610983c0ad29f45
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.2.tgz
    version: 0.7.2
  - apiVersion: v2
    appVersion: 0.6.1
    created: "2025-03-14T19:52:28.483777945Z"
    description: Windows GMSA Configuration
    digest: c13d93a6ff7ff7f3219acd3b85ea085d1294f6d10a63a9d51d5c86d01dc80cb2
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.1.tgz
    version: 0.7.1
  - apiVersion: v2
    appVersion: 0.6.0
    created: "2025-03-14T19:52:28.483186144Z"
    description: Windows GMSA Configuration
    digest: 9b5fc25c235bac92af9ab0d960de8641b3a638ec8904326f2640f468e113b4ec
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.7.0.tgz
    version: 0.7.0
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.482604743Z"
    description: Windows GMSA Configuration
    digest: b637cee6f623598cca5611c3854514875ce1363d915ad8cdd4dabd8d96483546
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.6.0.tgz
    version: 0.6.0
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.482076042Z"
    description: Windows GMSA Configuration
    digest: 19003bcc3f5af484afd5a9ad0c833a861420daf7e50964563ecaf92e4a1dc35c
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.5.0.tgz
    version: 0.5.0
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.481452541Z"
    description: Windows GMSA Configuration
    digest: 1f6b8bbfe6af4088f80d08d3065094ab1504054526bea6e4477459fb738f504b
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.4.tgz
    version: 0.4.4
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.480501239Z"
    description: Windows GMSA Configuration
    digest: 6ae2ac87141c8e3ac598611153635b0dd6619634ddc27b27b9c1a8717a511d8a
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.3.tgz
    version: 0.4.3
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.479809838Z"
    description: Windows GMSA Configuration
    digest: 399a4d03dfc08ac4cd811106ab55d525845ca715f0edbdcfcafcfa02cceaf108
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.2.tgz
    version: 0.4.2
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.479194037Z"
    description: Windows GMSA Configuration
    digest: 0709c8666554bf7b521c003d33f6198dafe03bf883161e132e929dac478bda45
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.1.tgz
    version: 0.4.1
  - apiVersion: v2
    appVersion: 0.4.0
    created: "2025-03-14T19:52:28.478498636Z"
    description: Windows GMSA Configuration
    digest: 7f29d22ba85d90a18e5b9c4e1a7d9ba1149d5827a2ca37b9a6fe1966e3598767
    keywords:
    - Windows
    - Windows GMSA
    - GMSA
    - Active Directory
    name: gmsa
    sources:
    - https://github.com/kubernetes-sigs/windows-gmsa
    type: application
    urls:
    - gmsa-0.4.0.tgz
    version: 0.4.0
generated: "2025-03-14T19:52:28.468434118Z"
```

## File: `kubernetes-sigs-windows-gmsa-993de21/scripts/GenerateCredentialSpecResource.ps1`
```powershell
<#
.Synopsis
 Renders a GMSA kubernetes resource manifest.
#>
Param(
    [Parameter(Position = 0, Mandatory = $true)] [String] $AccountName,
    [Parameter(Position = 1, Mandatory = $true)] [String] $ResourceName,
    [Parameter(Position = 2, Mandatory = $false)] [String] $ManifestFile,
    [Parameter(Mandatory=$false)] $Domain,
    [Parameter(Mandatory=$false)] [string[]] $AdditionalAccounts = @()
)
# Logging for troubleshooting
Start-Transcript -Path "C:\gmsa\CredSpec.txt"
# exit on error
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSDefaultParameterValues['*:ErrorAction'] = 'Stop'

# generate the name of the output file if not specified
if (-not $ManifestFile -or $ManifestFile.Length -eq 0) {
    $ManifestFile = "gmsa-cred-spec-$ResourceName.yml"
}
# check the out file doesn't exist
if ([System.IO.File]::Exists($ManifestFile)) {
    throw "Output file $ManifestFile already exists, refusing to overwrite it"
}

# install the dependencies we need
if (-not (Get-WindowsFeature rsat-ad-powershell).Installed) {
    Add-WindowsFeature rsat-ad-powershell
}
if (-not (Get-Command ConvertTo-Yaml -errorAction SilentlyContinue)) {
    Install-Module powershell-yaml -Force
}

# download the canonical helper script
Invoke-WebRequest "https://raw.githubusercontent.com/Microsoft/Virtualization-Documentation/live/windows-server-container-tools/ServiceAccounts/CredentialSpec.psm1" -UseBasicParsing -OutFile $env:TEMP\cred.psm1
Import-Module $env:temp\cred.psm1

# generate a unique docker cred spec name
$dockerCredSpecName = "tmp-k8s-cred-spec" + -join ((48..57) + (97..122) | Get-Random -Count 64 | ForEach-Object {[char]$_})

# have the upstream function perform its magic
if (-not $Domain) {
    $Domain = Get-ADDomain
}
New-CredentialSpec -Name $dockerCredSpecName -AccountName $AccountName -Domain $Domain.DnsRoot -AdditionalAccounts $AdditionalAccounts

# parse the JSON file thus generated
$dockerCredSpecPath = (Get-CredentialSpec | Where-Object {$_.Name -like "$dockerCredSpecName*"}).Path
$credSpecContents = Get-Content $dockerCredSpecPath | ConvertFrom-Json
# and clean it up
Remove-Item $dockerCredSpecPath

# generate the k8s resource
$resource = [ordered]@{
    "apiVersion" = "windows.k8s.io/v1";
    "kind" = 'GMSACredentialSpec';
    "metadata" = @{
        "name" = $ResourceName
    };
    "credspec" = $credSpecContents
}

ConvertTo-Yaml $resource | Set-Content $ManifestFile

Write-Output "K8S manifest rendered at $ManifestFile"
```

## File: `logs/HEAD`
```
0000000000000000000000000000000000000000 993de21c8f98a4def841b8de89aed688a95630d8 MaiKhue <R9000P 2021@MaiKhue.(none)> 1775014351 +0700	clone: from https://github.com/kubernetes-sigs/windows-gmsa
```

## File: `logs/refs/heads/master`
```
0000000000000000000000000000000000000000 993de21c8f98a4def841b8de89aed688a95630d8 MaiKhue <R9000P 2021@MaiKhue.(none)> 1775014351 +0700	clone: from https://github.com/kubernetes-sigs/windows-gmsa
```

## File: `logs/refs/remotes/origin/HEAD`
```
0000000000000000000000000000000000000000 993de21c8f98a4def841b8de89aed688a95630d8 MaiKhue <R9000P 2021@MaiKhue.(none)> 1775014351 +0700	clone: from https://github.com/kubernetes-sigs/windows-gmsa
```

## File: `refs/heads/master`
```
993de21c8f98a4def841b8de89aed688a95630d8
```

## File: `refs/remotes/origin/HEAD`
```
ref: refs/remotes/origin/master
```

## File: `scripts/GenerateCredentialSpecResource.ps1`
```powershell
<#
.Synopsis
 Renders a GMSA kubernetes resource manifest.
#>
Param(
    [Parameter(Position = 0, Mandatory = $true)] [String] $AccountName,
    [Parameter(Position = 1, Mandatory = $true)] [String] $ResourceName,
    [Parameter(Position = 2, Mandatory = $false)] [String] $ManifestFile,
    [Parameter(Mandatory=$false)] $Domain,
    [Parameter(Mandatory=$false)] [string[]] $AdditionalAccounts = @()
)
# Logging for troubleshooting
Start-Transcript -Path "C:\gmsa\CredSpec.txt"
# exit on error
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSDefaultParameterValues['*:ErrorAction'] = 'Stop'

# generate the name of the output file if not specified
if (-not $ManifestFile -or $ManifestFile.Length -eq 0) {
    $ManifestFile = "gmsa-cred-spec-$ResourceName.yml"
}
# check the out file doesn't exist
if ([System.IO.File]::Exists($ManifestFile)) {
    throw "Output file $ManifestFile already exists, refusing to overwrite it"
}

# install the dependencies we need
if (-not (Get-WindowsFeature rsat-ad-powershell).Installed) {
    Add-WindowsFeature rsat-ad-powershell
}
if (-not (Get-Command ConvertTo-Yaml -errorAction SilentlyContinue)) {
    Install-Module powershell-yaml -Force
}

# download the canonical helper script
Invoke-WebRequest "https://raw.githubusercontent.com/Microsoft/Virtualization-Documentation/live/windows-server-container-tools/ServiceAccounts/CredentialSpec.psm1" -UseBasicParsing -OutFile $env:TEMP\cred.psm1
Import-Module $env:temp\cred.psm1

# generate a unique docker cred spec name
$dockerCredSpecName = "tmp-k8s-cred-spec" + -join ((48..57) + (97..122) | Get-Random -Count 64 | ForEach-Object {[char]$_})

# have the upstream function perform its magic
if (-not $Domain) {
    $Domain = Get-ADDomain
}
New-CredentialSpec -Name $dockerCredSpecName -AccountName $AccountName -Domain $Domain.DnsRoot -AdditionalAccounts $AdditionalAccounts

# parse the JSON file thus generated
$dockerCredSpecPath = (Get-CredentialSpec | Where-Object {$_.Name -like "$dockerCredSpecName*"}).Path
$credSpecContents = Get-Content $dockerCredSpecPath | ConvertFrom-Json
# and clean it up
Remove-Item $dockerCredSpecPath

# generate the k8s resource
$resource = [ordered]@{
    "apiVersion" = "windows.k8s.io/v1";
    "kind" = 'GMSACredentialSpec';
    "metadata" = @{
        "name" = $ResourceName
    };
    "credspec" = $credSpecContents
}

ConvertTo-Yaml $resource | Set-Content $ManifestFile

Write-Output "K8S manifest rendered at $ManifestFile"
```

