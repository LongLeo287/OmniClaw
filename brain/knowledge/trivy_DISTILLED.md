---
id: trivy
type: knowledge
owner: OA_Triage
---
# trivy
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
<img src="docs/imgs/logo.png" width="200">

[![GitHub Release][release-img]][release]
[![Test][test-img]][test]
[![Go Report Card][go-report-img]][go-report]
[![License: Apache-2.0][license-img]][license]
[![GitHub Downloads][github-downloads-img]][release]
![Docker Pulls][docker-pulls]

[📖 Documentation][docs]
</div>

Trivy ([pronunciation][pronunciation]) is a comprehensive and versatile security scanner.
Trivy has *scanners* that look for security issues, and *targets* where it can find those issues.

Targets (what Trivy can scan):

- Container Image
- Filesystem
- Git Repository (remote)
- Virtual Machine Image
- Kubernetes

Scanners (what Trivy can find there):

- OS packages and software dependencies in use (SBOM)
- Known vulnerabilities (CVEs)
- IaC issues and misconfigurations
- Sensitive information and secrets
- Software licenses

Trivy supports most popular programming languages, operating systems, and platforms. For a complete list, see the [Scanning Coverage] page.

To learn more, go to the [Trivy homepage][homepage] for feature highlights, or to the [Documentation site][docs] for detailed information.

## Quick Start

### Get Trivy

Trivy is available in most common distribution channels. The full list of installation options is available in the [Installation] page. Here are a few popular examples:

- `brew install trivy`
- `docker run aquasec/trivy`
- Download binary from <https://github.com/aquasecurity/trivy/releases/latest/>
- See [Installation] for more

Trivy is integrated with many popular platforms and applications. The complete list of integrations is available in the [Ecosystem] page. Here are a few popular examples:

- [GitHub Actions](https://github.com/aquasecurity/trivy-action)
- [Kubernetes operator](https://github.com/aquasecurity/trivy-operator)
- [VS Code plugin](https://github.com/aquasecurity/trivy-vscode-extension)
- See [Ecosystem] for more

### Canary builds
There are canary builds ([Docker Hub](https://hub.docker.com/r/aquasec/trivy/tags?page=1&name=canary), [GitHub](https://github.com/aquasecurity/trivy/pkgs/container/trivy/75776514?tag=canary), [ECR](https://gallery.ecr.aws/aquasecurity/trivy#canary) images and [binaries](https://github.com/aquasecurity/trivy/actions/workflows/canary.yaml)) generated with every push to the main branch.

Please be aware: canary builds might have critical bugs, so they are not recommended for use in production.

### General usage

```bash
trivy <target> [--scanners <scanner1,scanner2>] <subject>
```

Examples:

```bash
trivy image python:3.4-alpine
```

<details>
<summary>Result</summary>

https://user-images.githubusercontent.com/1161307/171013513-95f18734-233d-45d3-aaf5-d6aec687db0e.mov

</details>

```bash
trivy fs --scanners vuln,secret,misconfig myproject/
```

<details>
<summary>Result</summary>

https://user-images.githubusercontent.com/1161307/171013917-b1f37810-f434-465c-b01a-22de036bd9b3.mov

</details>

```bash
trivy k8s --report summary cluster
```

<details>
<summary>Result</summary>

![k8s summary](docs/imgs/trivy-k8s.png)

</details>

## FAQ

### How to pronounce the name "Trivy"?

`tri` is pronounced like **tri**gger, `vy` is pronounced like en**vy**.

## Want more? Check out Aqua

If you liked Trivy, you will love Aqua which builds on top of Trivy to provide even more enhanced capabilities for a complete security management offering.  
You can find a high level comparison table specific to Trivy users [here](https://trivy.dev/docs/latest/commercial/compare/).
In addition check out the <https://aquasec.com> website for more information about our products and services.
If you'd like to contact Aqua or request a demo, please use this form: <https://www.aquasec.com/demo>

## Community

Trivy is an [Aqua Security][aquasec] open source project.  
Learn about our open source work and portfolio [here][oss].  
Contact us about any matter by opening a GitHub Discussion [here][discussions]

Please ensure to abide by our [Code of Conduct][code-of-conduct] during all interactions.

[test]: https://github.com/aquasecurity/trivy/actions/workflows/test.yaml
[test-img]: https://github.com/aquasecurity/trivy/actions/workflows/test.yaml/badge.svg
[go-report]: https://goreportcard.com/report/github.com/aquasecurity/trivy
[go-report-img]: https://goreportcard.com/badge/github.com/aquasecurity/trivy
[release]: https://github.com/aquasecurity/trivy/releases
[release-img]: https://img.shields.io/github/release/aquasecurity/trivy.svg?logo=github
[github-downloads-img]: https://img.shields.io/github/downloads/aquasecurity/trivy/total?logo=github
[docker-pulls]: https://img.shields.io/docker/pulls/aquasec/trivy?logo=docker&label=docker%20pulls%20%2F%20trivy
[license]: https://github.com/aquasecurity/trivy/blob/main/LICENSE
[license-img]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[homepage]: https://trivy.dev
[docs]: https://trivy.dev/docs/latest/
[pronunciation]: #how-to-pronounce-the-name-trivy
[code-of-conduct]: https://github.com/aquasecurity/community/blob/main/CODE_OF_CONDUCT.md

[Installation]:https://trivy.dev/docs/latest/getting-started/installation/
[Ecosystem]: https://trivy.dev/docs/latest/ecosystem/
[Scanning Coverage]: https://trivy.dev/docs/latest/coverage/

[alpine]: https://ariadne.space/2021/06/08/the-vulnerability-remediation-lifecycle-of-alpine-containers/
[rego]: https://www.openpolicyagent.org/docs/latest/#rego
[sigstore]: https://www.sigstore.dev/

[aquasec]: https://aquasec.com
[oss]: https://www.aquasec.com/products/open-source-projects/
[discussions]: https://github.com/aquasecurity/trivy/discussions

```

### File: brand\readme.md
```md
This directory contains media assets, such as the Trivy logo.
Assets under this directory are provided under the Creative Commons - BY 4.0 License. For more details, see here: <https://creativecommons.org/licenses/by/4.0/>
```

### File: e2e\README.md
```md
# End-to-End (E2E) Tests

## Testing Philosophy

The E2E tests in this directory are designed to test Trivy's functionality in realistic environments with **external dependencies and network connectivity**. These tests complement unit tests and integration tests by focusing on scenarios that require real external resources.

### What E2E Tests Should Cover

E2E tests should focus on functionality that involves:
- **External network connections** (downloading container images, vulnerability databases)
- **External service dependencies** (Docker daemon, registry access, proxy servers)
- **Real-world scenarios** that cannot be easily mocked or simulated
- **Cross-component integration** involving external systems

### What E2E Tests Should NOT Cover

E2E tests should **avoid** detailed assertions and comprehensive validation:
- **Detailed JSON output validation** - this should be covered by integration tests
- **Comprehensive vulnerability detection** - this should be covered by unit tests
- **Complex result comparison** - basic functionality verification is sufficient
- **Edge cases and error conditions** - these should be covered by unit tests

### Testing Approach

- **Minimal assertions**: Focus on basic functionality rather than detailed output validation
- **External dependencies**: Use real registries, databases, and services where practical
- **Environment isolation**: Each test should use isolated cache and working directories
- **Golden files**: Use -update flag for maintainable output comparison
- **Conditional execution**: Tests should validate required dependencies during setup

### Dependencies

- **Docker**: Required for local image scanning tests
- **Internet access**: Required for downloading images and databases

### Test Execution

The E2E tests build and execute trivy in isolated temporary directories. When you run `mage test:e2e`, it automatically:
1. Builds trivy in a test-specific temporary directory (via `t.TempDir()`)
2. Adds the temporary directory to the PATH for test execution
3. Runs the E2E tests using the isolated binary

This approach ensures:
- No pollution of the global environment
- Each test run uses a freshly built binary
- Test isolation between different test runs
- Clean test environment without side effects

### Running Tests

```bash
# Run all E2E tests
mage test:e2e

# Run specific test
go test -v -tags=e2e ./e2e/ -run TestE2E/image_scan

# Update golden files when output changes
go test -v -tags=e2e ./e2e/ -update
```

### Adding New Tests

When adding new E2E tests:
1. Focus on external dependencies and real-world scenarios
2. Use minimal assertions - verify functionality, not detailed output
3. Use golden files with -update flag for output comparison
4. Validate required dependencies in test setup
5. Use fixed/pinned versions for reproducible results
6. Include clear test documentation explaining the scenario being tested
```

### File: integration\README.md
```md
# Integration Tests

This directory contains integration tests for Trivy. These tests verify Trivy's behavior by running actual commands and comparing the output against golden files.

## Running Tests

### Run integration tests
```bash
# Run standard integration tests (excludes VM, K8s, and module tests)
mage test:integration

# Run all types of integration tests separately
mage test:integration  # Standard integration tests
mage test:module       # Wasm module tests
mage test:vm           # VM integration tests
mage test:k8s          # Kubernetes integration tests
```

### Run specific test
```bash
GOEXPERIMENT=jsonv2 go test -tags=integration -run TestRepository ./integration -v
```

## Golden Files

Golden files store the expected output for integration tests. They are located in `integration/testdata/*.golden`.

### Updating Golden Files

When you make changes that affect test output, you need to update the golden files:

```bash
# Update golden files for standard integration tests
mage test:updateGolden

# Update golden files for Wasm module tests
mage test:updateModuleGolden

# Update golden files for VM integration tests
mage test:updateVMGolden

# Update specific golden files manually
GOEXPERIMENT=jsonv2 go test -tags=integration -run TestRepository ./integration -v -update
```

**Important**:
- Only tests that generate golden files as the canonical source support the `-update` flag
- Tests that reuse golden files from other tests will be **skipped** during updates
- Look for `override: nil` comment in test code to identify canonical source tests

### Golden File Management Strategy

#### 1. Canonical Source Tests (Can Update Golden Files)

These tests generate golden files and should have:
- `override: nil` comment in the code
- No `t.Skipf()` for the `-update` flag

Example:
```go
func TestRepository(t *testing.T) {
    // ...
    runTest(t, osArgs, tt.golden, format, runOptions{
        fakeUUID: "3ff14136-e09f-4df9-80ea-%012d",
        override: nil, // Do not use overrides - golden files are generated from this test as the canonical source
    })
}
```

#### 2. Consumer Tests (Cannot Update Golden Files)

These tests reuse golden files from canonical source tests and should have:
- `if *update { t.Skipf(...) }` at the beginning of the test function
- `override` functions to adjust for differences (e.g., different artifact names, paths)
- Simplified comment: `Golden files are shared with TestXXX.`

Example:
```go
// TestClientServer tests the client-server mode of Trivy.
//
// Golden files are shared with TestTar or TestRepository.
func TestClientServer(t *testing.T) {
    if *update {
        t.Skipf("Skipping TestClientServer when -update flag is set. Golden files should be updated via TestTar or TestRepository.")
    }

    // ...
    runTest(t, osArgs, tt.golden, types.FormatJSON, runOptions{
        override: overrideFuncs(overrideUID, func(_ *testing.T, want, _ *types.Report) {
            want.ArtifactName = "https://github.com/knqyf263/trivy-ci-test"
        }),
        fakeUUID: "3ff14136-e09f-4df9-80ea-%012d",
    })
}
```

### Why Only One Test Updates Each Golden File

**Critical constraint**: Each golden file must be updated by exactly one test function.

If multiple tests update the same golden file, they may introduce subtle differences in the output. This causes the golden file to change every time tests are run, depending on which test executed last. This makes the golden files unstable and defeats their purpose.

**Solution**: Designate one test as the "canonical source" for each golden file. Other tests that want to verify equivalent results share the golden file in read-only mode (with `t.Skipf()` during updates).

### When to Share Golden Files

Share golden files between tests when you want to verify that different commands, flags, or configurations produce equivalent results with the **same output format**:

**Good reasons to share:**
- Testing different input methods that produce the same JSON output (local path vs remote URL vs client-server mode)
- Testing different ways to specify the same configuration (environment variables vs CLI flags vs config files)
- Testing different image sources that produce the same scan results (tar archive vs Docker Engine vs registry)

**Use override functions to handle:**
- Different artifact names or paths
- Different metadata (e.g., image config, repo info)
- Different ReportIDs or UUIDs
- Minor formatting differences in paths (e.g., Windows vs Unix separators)

**Example**: TestTar generates golden files for image scanning, and these are reused by:
- TestDockerEngine (different image source: Docker Engine API)
- TestRegistry (different image source: container registry)
- TestClientServer (different execution mode: client-server)

All of these produce the same JSON format with the same vulnerability data, but with different artifact names and metadata.

### Validation

The test framework automatically validates that:
- Tests updating golden files (`*update == true`) cannot use override functions
- This prevents accidentally updating golden files with modified data

If you try to update a golden file with an override function, the test will fail with:
```
invalid test configuration: cannot use override functions when update=true
```

## Test Organization

### Test Files

Tests are organized by functionality:

- `standalone_tar_test.go` - Container image scanning from tar archives
- `repo_test.go` - Repository and filesystem scanning
- `sbom_test.go` - SBOM scanning and generation
- `client_server_test.go` - Client-server mode
- `docker_engine_test.go` - Docker Engine API integration
- `registry_test.go` - Container registry integration
- `config_test.go` - Configuration handling (CLI flags, env vars, config files)
- `vm_test.go` - Virtual machine image scanning
- `module_test.go` - Wasm module integration

### Test Data Directory Structure

```
integration/testdata/
├── *.golden              # Golden files (expected test outputs)
└── fixtures/             # Test input files
    ├── images/           # Container images (auto-downloaded)
    ├── vm-images/        # VM images (auto-downloaded)
    ├── repo/             # Repository and filesystem test data
    ├── sbom/             # SBOM test files
    └── ...
```

**Important**: `testdata/fixtures/images/` and `testdata/fixtures/vm-images/` are automatically downloaded by mage commands:
- `mage test:integration` downloads container images
- `mage test:vm` downloads VM images

If you run tests directly with `go test` without using mage commands, these fixtures will not be present and tests will fail. Use mage commands to ensure fixtures are properly set up.

## Troubleshooting

### Golden file shared between tests shows unexpected differences

1. Identify which test is the canonical source (has `override: nil`)
2. Update golden file from the canonical source test only
3. Adjust override functions in consumer tests to handle differences

### Cannot update golden files for a specific test

1. Check if the test has `if *update { t.Skipf(...) }` - this prevents updates
2. Find the canonical source test mentioned in the skip message
3. Update golden files from the canonical source test instead

## Best Practices

1. **One golden file, one updater**: Each golden file should be updated by exactly one test function
2. **Use `mage test:updateGolden`**: This automatically updates all golden files from canonical source tests
3. **Minimize golden file duplication**: Share golden files when testing equivalent functionality
4. **Keep override functions simple**: Complex overrides may indicate tests shouldn't share golden files
5. **Add `override: nil` comments**: Clearly mark canonical source tests in the code

```

### File: trivy\README.md
```md
<div align="center">
<img src="docs/imgs/logo.png" width="200">

[![GitHub Release][release-img]][release]
[![Test][test-img]][test]
[![Go Report Card][go-report-img]][go-report]
[![License: Apache-2.0][license-img]][license]
[![GitHub Downloads][github-downloads-img]][release]
![Docker Pulls][docker-pulls]

[📖 Documentation][docs]
</div>

Trivy ([pronunciation][pronunciation]) is a comprehensive and versatile security scanner.
Trivy has *scanners* that look for security issues, and *targets* where it can find those issues.

Targets (what Trivy can scan):

- Container Image
- Filesystem
- Git Repository (remote)
- Virtual Machine Image
- Kubernetes

Scanners (what Trivy can find there):

- OS packages and software dependencies in use (SBOM)
- Known vulnerabilities (CVEs)
- IaC issues and misconfigurations
- Sensitive information and secrets
- Software licenses

Trivy supports most popular programming languages, operating systems, and platforms. For a complete list, see the [Scanning Coverage] page.

To learn more, go to the [Trivy homepage][homepage] for feature highlights, or to the [Documentation site][docs] for detailed information.

## Quick Start

### Get Trivy

Trivy is available in most common distribution channels. The full list of installation options is available in the [Installation] page. Here are a few popular examples:

- `brew install trivy`
- `docker run aquasec/trivy`
- Download binary from <https://github.com/aquasecurity/trivy/releases/latest/>
- See [Installation] for more

Trivy is integrated with many popular platforms and applications. The complete list of integrations is available in the [Ecosystem] page. Here are a few popular examples:

- [GitHub Actions](https://github.com/aquasecurity/trivy-action)
- [Kubernetes operator](https://github.com/aquasecurity/trivy-operator)
- [VS Code plugin](https://github.com/aquasecurity/trivy-vscode-extension)
- See [Ecosystem] for more

### Canary builds
There are canary builds ([Docker Hub](https://hub.docker.com/r/aquasec/trivy/tags?page=1&name=canary), [GitHub](https://github.com/aquasecurity/trivy/pkgs/container/trivy/75776514?tag=canary), [ECR](https://gallery.ecr.aws/aquasecurity/trivy#canary) images and [binaries](https://github.com/aquasecurity/trivy/actions/workflows/canary.yaml)) generated with every push to the main branch.

Please be aware: canary builds might have critical bugs, so they are not recommended for use in production.

### General usage

```bash
trivy <target> [--scanners <scanner1,scanner2>] <subject>
```

Examples:

```bash
trivy image python:3.4-alpine
```

<details>
<summary>Result</summary>

https://user-images.githubusercontent.com/1161307/171013513-95f18734-233d-45d3-aaf5-d6aec687db0e.mov

</details>

```bash
trivy fs --scanners vuln,secret,misconfig myproject/
```

<details>
<summary>Result</summary>

https://user-images.githubusercontent.com/1161307/171013917-b1f37810-f434-465c-b01a-22de036bd9b3.mov

</details>

```bash
trivy k8s --report summary cluster
```

<details>
<summary>Result</summary>

![k8s summary](docs/imgs/trivy-k8s.png)

</details>

## FAQ

### How to pronounce the name "Trivy"?

`tri` is pronounced like **tri**gger, `vy` is pronounced like en**vy**.

## Want more? Check out Aqua

If you liked Trivy, you will love Aqua which builds on top of Trivy to provide even more enhanced capabilities for a complete security management offering.  
You can find a high level comparison table specific to Trivy users [here](https://trivy.dev/docs/latest/commercial/compare/).
In addition check out the <https://aquasec.com> website for more information about our products and services.
If you'd like to contact Aqua or request a demo, please use this form: <https://www.aquasec.com/demo>

## Community

Trivy is an [Aqua Security][aquasec] open source project.  
Learn about our open source work and portfolio [here][oss].  
Contact us about any matter by opening a GitHub Discussion [here][discussions]

Please ensure to abide by our [Code of Conduct][code-of-conduct] during all interactions.

[test]: https://github.com/aquasecurity/trivy/actions/workflows/test.yaml
[test-img]: https://github.com/aquasecurity/trivy/actions/workflows/test.yaml/badge.svg
[go-report]: https://goreportcard.com/report/github.com/aquasecurity/trivy
[go-report-img]: https://goreportcard.com/badge/github.com/aquasecurity/trivy
[release]: https://github.com/aquasecurity/trivy/releases
[release-img]: https://img.shields.io/github/release/aquasecurity/trivy.svg?logo=github
[github-downloads-img]: https://img.shields.io/github/downloads/aquasecurity/trivy/total?logo=github
[docker-pulls]: https://img.shields.io/docker/pulls/aquasec/trivy?logo=docker&label=docker%20pulls%20%2F%20trivy
[license]: https://github.com/aquasecurity/trivy/blob/main/LICENSE
[license-img]: https://img.shields.io/badge/License-Apache%202.0-blue.svg
[homepage]: https://trivy.dev
[docs]: https://trivy.dev/docs/latest/
[pronunciation]: #how-to-pronounce-the-name-trivy
[code-of-conduct]: https://github.com/aquasecurity/community/blob/main/CODE_OF_CONDUCT.md

[Installation]:https://trivy.dev/docs/latest/getting-started/installation/
[Ecosystem]: https://trivy.dev/docs/latest/ecosystem/
[Scanning Coverage]: https://trivy.dev/docs/latest/coverage/

[alpine]: https://ariadne.space/2021/06/08/the-vulnerability-remediation-lifecycle-of-alpine-containers/
[rego]: https://www.openpolicyagent.org/docs/latest/#rego
[sigstore]: https://www.sigstore.dev/

[aquasec]: https://aquasec.com
[oss]: https://www.aquasec.com/products/open-source-projects/
[discussions]: https://github.com/aquasecurity/trivy/discussions

```

### File: helm\trivy\README.md
```md
# Trivy Scanner

Trivy vulnerability scanner standalone installation.

## TL;DR;

```
$ helm install trivy . --namespace trivy --create-namespace
```

## Introduction

This chart bootstraps a Trivy deployment on a [Kubernetes](http://kubernetes.io) cluster using the
[Helm](https://helm.sh) package manager.

## Prerequisites

- Kubernetes 1.12+
- Helm 3+

## Installing from the Aqua Chart Repository

```
helm repo add aquasecurity https://aquasecurity.github.io/helm-charts/
helm repo update
helm search repo trivy
helm install my-trivy aquasecurity/trivy
```

## Installing the Chart

To install the chart with the release name `my-release`:

```
$ helm install my-release .
```

The command deploys Trivy on the Kubernetes cluster in the default configuration. The [Parameters](#parameters)
section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Parameters

The following table lists the configurable parameters of the Trivy chart and their default values.

|                 Parameter             |                                Description                              |    Default     |
|---------------------------------------|-------------------------------------------------------------------------|----------------|
| `image.registry`                      | Image registry                                                          | `docker.io`    |
| `image.repository`                    | Image name                                                              | `aquasec/trivy` |
| `image.tag`                           | Image tag                                                               | `{TAG_NAME}`   |
| `image.pullPolicy`                    | Image pull policy                                                       | `IfNotPresent` |
| `image.pullSecret`                    | The name of an imagePullSecret used to pull trivy image from e.g. Docker Hub or a private registry  | |
| `replicaCount`                        | Number of Trivy Pods to run                                   | `1`            |
| `trivy.debugMode`                     | The flag to enable or disable Trivy debug mode                          | `false` |
| `trivy.gitHubToken`                   | The GitHub access token to download Trivy DB. More info: https://trivy.dev/docs/latest/references/troubleshooting/#github-rate-limiting                          |      |
| `trivy.registryUsername`              | The username used to log in at dockerhub. More info: https://trivy.dev/docs/latest/advanced/private-registries/docker-hub/ |      |
| `trivy.registryPassword`              | The password used to log in at dockerhub. More info: https://trivy.dev/docs/latest/advanced/private-registries/docker-hub/ |      |
| `trivy.registryCredentialsExistingSecret` | Name of Secret containing dockerhub credentials. Alternative to the 2 parameters above, has precedence if set.                    |      |
| `trivy.serviceAccount.annotations`        | Additional annotations to add to the Kubernetes service account resource |     |
| `trivy.skipDBUpdate`                    | The flag to enable or disable Trivy DB downloads from GitHub            | `false`        |
| `trivy.dbRepository`                  | OCI repository to retrieve the trivy vulnerability database from        | `ghcr.io/aquasecurity/trivy-db`        |
| `trivy.cache.redis.enabled`           | Enable Redis as caching backend                                         | `false` |
| `trivy.cache.redis.url`               | Specify redis connection url, e.g. redis://redis.redis.svc:6379         | `` |
| `trivy.cache.redis.ttl`               | Specify redis TTL, e.g. 3600s or 24h                                    | `` |
| `trivy.cache.redis.tls`               | Enable Redis TLS with public certificates                               | `` |
| `trivy.serverToken`                   | The token to authenticate Trivy client with Trivy server                | `` |
| `trivy.existingSecret`                | existingSecret if an existing secret has been created outside the chart. Overrides gitHubToken, registryUsername, registryPassword, serverToken | `` |
| `trivy.podAnnotations`                | Annotations for pods created by statefulset                             | `{}` |
| `trivy.extraEnvVars`                  | extraEnvVars to be set on the container                                 | `{}` |
| `trivy.sslCertDir`                    | Can be used to override the system default locations for SSL certificate files directory, example: `/ssl/certs` | `` |
| `service.name`                        | If specified, the name used for the Trivy service                       |     |
| `service.type`                        | Kubernetes service type                                                 | `ClusterIP` |
| `service.port`                        | Kubernetes service port                                                 | `4954`      |
| `service.sessionAffinity`             | Kubernetes service session affinity                                     | `ClientIP`  |
| `httpProxy`                           | The URL of the HTTP proxy server                                        |     |
| `httpsProxy`                          | The URL of the HTTPS proxy server                                       |     |
| `noProxy`                             | The URLs that the proxy settings do not apply to                        |     |
| `nodeSelector`                        | Node labels for pod assignment                                              |     |
| `affinity`                            | Affinity settings for pod assignment                                              |     |
| `tolerations`                         | Tolerations for pod assignment                                              |     |
| `podAnnotations`                      | Annotations for pods created by statefulset                             | `{}` |

The above parameters map to the env variables defined in [trivy](https://trivy.dev/docs/latest/configuration/#configuration).

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.

```
$ helm install my-release . \
       --namespace my-namespace \
       --set "service.port=9090" \
       --set "trivy.vulnType=os\,library"
```

## Storage

This chart uses a PersistentVolumeClaim to reduce the number of database downloads between POD restarts or updates. The storageclass should have the reclaim policy `Retain`.

## Caching

You can specify a Redis server as cache backend. This Redis server has to be already present. You can use the [bitnami chart](https://bitnami.com/stack/redis/helm).
More Information about the caching backends can be found [here](https://trivy.dev/docs/latest/configuration/cache/#scan-cache-backend).

```

### File: trivy\brand\readme.md
```md
This directory contains media assets, such as the Trivy logo.
Assets under this directory are provided under the Creative Commons - BY 4.0 License. For more details, see here: <https://creativecommons.org/licenses/by/4.0/>
```

### File: trivy\e2e\README.md
```md
# End-to-End (E2E) Tests

## Testing Philosophy

The E2E tests in this directory are designed to test Trivy's functionality in realistic environments with **external dependencies and network connectivity**. These tests complement unit tests and integration tests by focusing on scenarios that require real external resources.

### What E2E Tests Should Cover

E2E tests should focus on functionality that involves:
- **External network connections** (downloading container images, vulnerability databases)
- **External service dependencies** (Docker daemon, registry access, proxy servers)
- **Real-world scenarios** that cannot be easily mocked or simulated
- **Cross-component integration** involving external systems

### What E2E Tests Should NOT Cover

E2E tests should **avoid** detailed assertions and comprehensive validation:
- **Detailed JSON output validation** - this should be covered by integration tests
- **Comprehensive vulnerability detection** - this should be covered by unit tests
- **Complex result comparison** - basic functionality verification is sufficient
- **Edge cases and error conditions** - these should be covered by unit tests

### Testing Approach

- **Minimal assertions**: Focus on basic functionality rather than detailed output validation
- **External dependencies**: Use real registries, databases, and services where practical
- **Environment isolation**: Each test should use isolated cache and working directories
- **Golden files**: Use -update flag for maintainable output comparison
- **Conditional execution**: Tests should validate required dependencies during setup

### Dependencies

- **Docker**: Required for local image scanning tests
- **Internet access**: Required for downloading images and databases

### Test Execution

The E2E tests build and execute trivy in isolated temporary directories. When you run `mage test:e2e`, it automatically:
1. Builds trivy in a test-specific temporary directory (via `t.TempDir()`)
2. Adds the temporary directory to the PATH for test execution
3. Runs the E2E tests using the isolated binary

This approach ensures:
- No pollution of the global environment
- Each test run uses a freshly built binary
- Test isolation between different test runs
- Clean test environment without side effects

### Running Tests

```bash
# Run all E2E tests
mage test:e2e

# Run specific test
go test -v -tags=e2e ./e2e/ -run TestE2E/image_scan

# Update golden files when output changes
go test -v -tags=e2e ./e2e/ -update
```

### Adding New Tests

When adding new E2E tests:
1. Focus on external dependencies and real-world scenarios
2. Use minimal assertions - verify functionality, not detailed output
3. Use golden files with -update flag for output comparison
4. Validate required dependencies in test setup
5. Use fixed/pinned versions for reproducible results
6. Include clear test documentation explaining the scenario being tested
```

### File: trivy\integration\README.md
```md
# Integration Tests

This directory contains integration tests for Trivy. These tests verify Trivy's behavior by running actual commands and comparing the output against golden files.

## Running Tests

### Run integration tests
```bash
# Run standard integration tests (excludes VM, K8s, and module tests)
mage test:integration

# Run all types of integration tests separately
mage test:integration  # Standard integration tests
mage test:module       # Wasm module tests
mage test:vm           # VM integration tests
mage test:k8s          # Kubernetes integration tests
```

### Run specific test
```bash
GOEXPERIMENT=jsonv2 go test -tags=integration -run TestRepository ./integration -v
```

## Golden Files

Golden files store the expected output for integration tests. They are located in `integration/testdata/*.golden`.

### Updating Golden Files

When you make changes that affect test output, you need to update the golden files:

```bash
# Update golden files for standard integration tests
mage test:updateGolden

# Update golden files for Wasm module tests
mage test:updateModuleGolden

# Update golden files for VM integration tests
mage test:updateVMGolden

# Update specific golden files manually
GOEXPERIMENT=jsonv2 go test -tags=integration -run TestRepository ./integration -v -update
```

**Important**:
- Only tests that generate golden files as the canonical source support the `-update` flag
- Tests that reuse golden files from other tests will be **skipped** during updates
- Look for `override: nil` comment in test code to identify canonical source tests

### Golden File Management Strategy

#### 1. Canonical Source Tests (Can Update Golden Files)

These tests generate golden files and should have:
- `override: nil` comment in the code
- No `t.Skipf()` for the `-update` flag

Example:
```go
func TestRepository(t *testing.T) {
    // ...
    runTest(t, osArgs, tt.golden, format, runOptions{
        fakeUUID: "3ff14136-e09f-4df9-80ea-%012d",
        override: nil, // Do not use overrides - golden files are generated from this test as the canonical source
    })
}
```

#### 2. Consumer Tests (Cannot Update Golden Files)

These tests reuse golden files from canonical source tests and should have:
- `if *update { t.Skipf(...) }` at the beginning of the test function
- `override` functions to adjust for differences (e.g., different artifact names, paths)
- Simplified comment: `Golden files are shared with TestXXX.`

Example:
```go
// TestClientServer tests the client-server mode of Trivy.
//
// Golden files are shared with TestTar or TestRepository.
func TestClientServer(t *testing.T) {
    if *update {
        t.Skipf("Skipping TestClientServer when -update flag is set. Golden files should be updated via TestTar or TestRepository.")
    }

    // ...
    runTest(t, osArgs, tt.golden, types.FormatJSON, runOptions{
        override: overrideFuncs(overrideUID, func(_ *testing.T, want, _ *types.Report) {
            want.ArtifactName = "https://github.com/knqyf263/trivy-ci-test"
        }),
        fakeUUID: "3ff14136-e09f-4df9-80ea-%012d",
    })
}
```

### Why Only One Test Updates Each Golden File

**Critical constraint**: Each golden file must be updated by exactly one test function.

If multiple tests update the same golden file, they may introduce subtle differences in the output. This causes the golden file to change every time tests are run, depending on which test executed last. This makes the golden files unstable and defeats their purpose.

**Solution**: Designate one test as the "canonical source" for each golden file. Other tests that want to verify equivalent results share the golden file in read-only mode (with `t.Skipf()` during updates).

### When to Share Golden Files

Share golden files between tests when you want to verify that different commands, flags, or configurations produce equivalent results with the **same output format**:

**Good reasons to share:**
- Testing different input methods that produce the same JSON output (local path vs remote URL vs client-server mode)
- Testing different ways to specify the same configuration (environment variables vs CLI flags vs config files)
- Testing different image sources that produce the same scan results (tar archive vs Docker Engine vs registry)

**Use override functions to handle:**
- Different artifact names or paths
- Different metadata (e.g., image config, repo info)
- Different ReportIDs or UUIDs
- Minor formatting differences in paths (e.g., Windows vs Unix separators)

**Example**: TestTar generates golden files for image scanning, and these are reused by:
- TestDockerEngine (different image source: Docker Engine API)
- TestRegistry (different image source: container registry)
- TestClientServer (different execution mode: client-server)

All of these produce the same JSON format with the same vulnerability data, but with different artifact names and metadata.

### Validation

The test framework automatically validates that:
- Tests updating golden files (`*update == true`) cannot use override functions
- This prevents accidentally updating golden files with modified data

If you try to update a golden file with an override function, the test will fail with:
```
invalid test configuration: cannot use override functions when update=true
```

## Test Organization

### Test Files

Tests are organized by functionality:

- `standalone_tar_test.go` - Container image scanning from tar archives
- `repo_test.go` - Repository and filesystem scanning
- `sbom_test.go` - SBOM scanning and generation
- `client_server_test.go` - Client-server mode
- `docker_engine_test.go` - Docker Engine API integration
- `registry_test.go` - Container registry integration
- `config_test.go` - Configuration handling (CLI flags, env vars, config files)
- `vm_test.go` - Virtual machine image scanning
- `module_test.go` - Wasm module integration

### Test Data Directory Structure

```
integration/testdata/
├── *.golden              # Golden files (expected test outputs)
└── fixtures/             # Test input files
    ├── images/           # Container images (auto-downloaded)
    ├── vm-images/        # VM images (auto-downloaded)
    ├── repo/             # Repository and filesystem test data
    ├── sbom/             # SBOM test files
    └── ...
```

**Important**: `testdata/fixtures/images/` and `testdata/fixtures/vm-images/` are automatically downloaded by mage commands:
- `mage test:integration` downloads container images
- `mage test:vm` downloads VM images

If you run tests directly with `go test` without using mage commands, these fixtures will not be present and tests will fail. Use mage commands to ensure fixtures are properly set up.

## Troubleshooting

### Golden file shared between tests shows unexpected differences

1. Identify which test is the canonical source (has `override: nil`)
2. Update golden file from the canonical source test only
3. Adjust override functions in consumer tests to handle differences

### Cannot update golden files for a specific test

1. Check if the test has `if *update { t.Skipf(...) }` - this prevents updates
2. Find the canonical source test mentioned in the skip message
3. Update golden files from the canonical source test instead

## Best Practices

1. **One golden file, one updater**: Each golden file should be updated by exactly one test function
2. **Use `mage test:updateGolden`**: This automatically updates all golden files from canonical source tests
3. **Minimize golden file duplication**: Share golden files when testing equivalent functionality
4. **Keep override functions simple**: Complex overrides may indicate tests shouldn't share golden files
5. **Add `override: nil` comments**: Clearly mark canonical source tests in the code

```

### File: trivy\helm\trivy\README.md
```md
# Trivy Scanner

Trivy vulnerability scanner standalone installation.

## TL;DR;

```
$ helm install trivy . --namespace trivy --create-namespace
```

## Introduction

This chart bootstraps a Trivy deployment on a [Kubernetes](http://kubernetes.io) cluster using the
[Helm](https://helm.sh) package manager.

## Prerequisites

- Kubernetes 1.12+
- Helm 3+

## Installing from the Aqua Chart Repository

```
helm repo add aquasecurity https://aquasecurity.github.io/helm-charts/
helm repo update
helm search repo trivy
helm install my-trivy aquasecurity/trivy
```

## Installing the Chart

To install the chart with the release name `my-release`:

```
$ helm install my-release .
```

The command deploys Trivy on the Kubernetes cluster in the default configuration. The [Parameters](#parameters)
section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Parameters

The following table lists the configurable parameters of the Trivy chart and their default values.

|                 Parameter             |                                Description                              |    Default     |
|---------------------------------------|-------------------------------------------------------------------------|----------------|
| `image.registry`                      | Image registry                                                          | `docker.io`    |
| `image.repository`                    | Image name                                                              | `aquasec/trivy` |
| `image.tag`                           | Image tag                                                               | `{TAG_NAME}`   |
| `image.pullPolicy`                    | Image pull policy                                                       | `IfNotPresent` |
| `image.pullSecret`                    | The name of an imagePullSecret used to pull trivy image from e.g. Docker Hub or a private registry  | |
| `replicaCount`                        | Number of Trivy Pods to run                                   | `1`            |
| `trivy.debugMode`                     | The flag to enable or disable Trivy debug mode                          | `false` |
| `trivy.gitHubToken`                   | The GitHub access token to download Trivy DB. More info: https://trivy.dev/docs/latest/references/troubleshooting/#github-rate-limiting                          |      |
| `trivy.registryUsername`              | The username used to log in at dockerhub. More info: https://trivy.dev/docs/latest/advanced/private-registries/docker-hub/ |      |
| `trivy.registryPassword`              | The password used to log in at dockerhub. More info: https://trivy.dev/docs/latest/advanced/private-registries/docker-hub/ |      |
| `trivy.registryCredentialsExistingSecret` | Name of Secret containing dockerhub credentials. Alternative to the 2 parameters above, has precedence if set.                    |      |
| `trivy.serviceAccount.annotations`        | Additional annotations to add to the Kubernetes service account resource |     |
| `trivy.skipDBUpdate`                    | The flag to enable or disable Trivy DB downloads from GitHub            | `false`        |
| `trivy.dbRepository`                  | OCI repository to retrieve the trivy vulnerability database from        | `ghcr.io/aquasecurity/trivy-db`        |
| `trivy.cache.redis.enabled`           | Enable Redis as caching backend                                         | `false` |
| `trivy.cache.redis.url`               | Specify redis connection url, e.g. redis://redis.redis.svc:6379         | `` |
| `trivy.cache.redis.ttl`               | Specify redis TTL, e.g. 3600s or 24h                                    | `` |
| `trivy.cache.redis.tls`               | Enable Redis TLS with public certificates                               | `` |
| `trivy.serverToken`                   | The token to authenticate Trivy client with Trivy server                | `` |
| `trivy.existingSecret`                | existingSecret if an existing secret has been created outside the chart. Overrides gitHubToken, registryUsername, registryPassword, serverToken | `` |
| `trivy.podAnnotations`                | Annotations for pods created by statefulset                             | `{}` |
| `trivy.extraEnvVars`                  | extraEnvVars to be set on the container                                 | `{}` |
| `trivy.sslCertDir`                    | Can be used to override the system default locations for SSL certificate files directory, example: `/ssl/certs` | `` |
| `service.name`                        | If specified, the name used for the Trivy service                       |     |
| `service.type`                        | Kubernetes service type                                                 | `ClusterIP` |
| `service.port`                        | Kubernetes service port                                                 | `4954`      |
| `service.sessionAffinity`             | Kubernetes service session affinity                                     | `ClientIP`  |
| `httpProxy`                           | The URL of the HTTP proxy server                                        |     |
| `httpsProxy`                          | The URL of the HTTPS proxy server                                       |     |
| `noProxy`                             | The URLs that the proxy settings do not apply to                        |     |
| `nodeSelector`                        | Node labels for pod assignment                                              |     |
| `affinity`                            | Affinity settings for pod assignment                                              |     |
| `tolerations`                         | Tolerations for pod assignment                                              |     |
| `podAnnotations`                      | Annotations for pods created by statefulset                             | `{}` |

The above parameters map to the env variables defined in [trivy](https://trivy.dev/docs/latest/configuration/#configuration).

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.

```
$ helm install my-release . \
       --namespace my-namespace \
       --set "service.port=9090" \
       --set "trivy.vulnType=os\,library"
```

## Storage

This chart uses a PersistentVolumeClaim to reduce the number of database downloads between POD restarts or updates. The storageclass should have the reclaim policy `Retain`.

## Caching

You can specify a Redis server as cache backend. This Redis server has to be already present. You can use the [bitnami chart](https://bitnami.com/stack/redis/helm).
More Information about the caching backends can be found [here](https://trivy.dev/docs/latest/configuration/cache/#scan-cache-backend).

```

### File: .golangci.yaml
```yaml
issues:
  max-issues-per-linter: 0
  max-same-issues: 0

linters:
  settings:
    depguard:
      rules:
        main:
          list-mode: lax
          deny:
            # Cannot use gomodguard, which examines go.mod, as "golang.org/x/exp/slices" is not a module and doesn't appear in go.mod.
            - pkg: "golang.org/x/exp/slices"
              desc: "Use 'slices' instead"
            - pkg: "golang.org/x/exp/maps"
              desc: "Use 'maps' or 'github.com/samber/lo' instead"
            - pkg: "io/ioutil"
              desc: "io/ioutil is deprecated. Use 'io' or 'os' instead"
    dupl:
      threshold: 100
    errcheck:
      check-type-assertions: true
      check-blank: true
    goconst:
      min-len: 3
      min-occurrences: 3
    gocritic:
      disabled-checks:
        - appendAssign
        - commentedOutCode
        - hugeParam
        - importShadow # FIXME
        - indexAlloc
        - rangeValCopy
        - regexpSimplify
        - sloppyReassign
        - unnamedResult
        - whyNoLint
      enabled-tags:
        - diagnostic
        - style
        - performance
        - experimental
        - opinionated
      settings:
        ruleguard:
          failOn: all
          rules: "${base-path}/misc/lint/rules.go"
    gocyclo:
      # Next highest complexity candidate: ApplyLayers in pkg/fanal/applier/docker.go (score: 28)
      min-complexity: 20
    gomodguard:
      blocked:
        modules:
          - github.com/hashicorp/go-version:
              recommendations:
                - github.com/aquasecurity/go-version
              reason: "`aquasecurity/go-version` is designed for our use-cases"
          - github.com/Masterminds/semver:
              recommendations:
                - github.com/aquasecurity/go-version
              reason: "`aquasecurity/go-version` is designed for our use-cases"
          - github.com/liamg/memoryfs:
              recommendations:
                - github.com/aquasecurity/trivy/pkg/mapfs
    gosec:
      excludes:
        - G101
        - G114
        - G115
        - G117 # Potential exposure of secrets in values marshaled by JSON/YAML/XML/TOML
        - G204
        - G304
        - G402
        - G703 # Path traversal via taint analysis
        - G704 # SSRF via taint analysis
        - G705 # XSS via taint analysis
    govet:
      disable:
        - shadow
    misspell:
      locale: US
      ignore-rules:
        - behaviour
        - licence
        - optimise
        - simmilar
    perfsprint:
      # Optimizes even if it requires an int or uint type cast.
      int-conversion: true
      # Optimizes into `err.Error()` even if it is only equivalent for non-nil errors.
      err-error: true
      # Optimizes `fmt.Errorf`.
      errorf: true
      # Optimizes `fmt.Sprintf` with only one argument.
      sprintf1: false
      # Optimizes into strings concatenation.
      strconcat: false
      # Optimizes string concatenation in a loop.
      concat-loop: false
    revive:
      max-open-files: 2048
      # https://github.com/mgechev/revive/blob/HEAD/RULES_DESCRIPTIONS.md
      rules:
        - name: bool-literal-in-expr
        - name: context-as-argument
          arguments:
            - allowTypesBefore: "*testing.T"
        - name: duplicated-imports
        - name: early-return
          arguments:
            - preserve-scope
        - name: if-return
        - name: increment-decrement
        - name: indent-error-flow
          arguments:
            - preserve-scope
        - name: range
        - name: range-val-address
        - name: superfluous-else
          arguments:
            - preserve-scope
        - name: time-equal
        - name: unnecessary-stmt
        - name: unused-parameter
        - name: use-any

    staticcheck:
      checks:
        - all
        - -QF1008 # Omit embedded fields from selector expression
        - -S1007  # Simplify regular expression by using raw string literal
        - -S1011  # Use a single append to concatenate two slices
        - -S1023  # Omit redundant control flow
        - -SA1019 # Using a deprecated function, variable, constant or field
        - -SA1024 # A string cutset contains duplicate characters
        - -SA4004 # The loop exits unconditionally after one iteration
        - -SA4023 # Impossible comparison of interface value with untyped nil
        - -SA4032 # Comparing runtime.GOOS or runtime.GOARCH against impossible value
        - -SA5011 # Possible nil pointer dereference
        - -ST1003 # Poorly chosen identifier
        - -ST1012 # Poorly chosen name for error variable

    testifylint:
      enable-all: true

  default: none

  enable:
    - bodyclose
    - depguard
    - goconst
    - gocritic
    - gocyclo
    - gomodguard
    - gosec
    - govet
    - ineffassign
    - misspell
    - perfsprint
    - revive
    - staticcheck
    - testifylint
    - unconvert
    - unused
    - usestdlibvars
    - usetesting
    - modernize

  exclusions:
    generated: lax
    paths:
      - "pkg/iac/scanners/terraform/parser/funcs" # copies of Terraform functions
    rules:
      - path: ".*_test.go$"
        linters:
          - goconst
          - gosec
          - unused
      - path: ".*_test.go$"
        linters:
          - govet
        text: "copylocks:"
      - path: ".*_test.go$"
        linters:
          - gocritic
        text: "commentFormatting:"
      - path: ".*_test.go$"
        linters:
          - gocritic
        text: "exitAfterDefer:"
      - path: ".*_test.go$"
        linters:
          - gocritic
        text: "importShadow:"
      - linters:
          - goconst
        text: "string `each` has 3 occurrences, make it a constant" # FIXME
    presets:
      - comments
      - common-false-positives
      - legacy
      - std-error-handling
    warn-unused: true

run:
  go: "1.25"
  timeout: 30m

formatters:
  enable:
    - gci
    - gofmt

  exclusions:
    generated: lax

  settings:
    gci:
      sections:
        - standard
        - default
        - prefix(github.com/aquasecurity/)
        - blank
        - dot
    gofmt:
      simplify: false

version: "2"

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
