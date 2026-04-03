---
id: github.com-docker-login-action-fa925cea-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.099303
---

# KNOWLEDGE EXTRACT: github.com_docker_login-action_fa925cea
> **Extracted on:** 2026-04-01 07:35:03
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519050/github.com_docker_login-action_fa925cea

---

## File: `.dockerignore`
```
/coverage

# Dependency directories
node_modules/
jspm_packages/

# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*
```

## File: `.editorconfig`
```
# This file is for unifying the coding style for different editors and IDEs.
# More information at http://editorconfig.org

root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false
```

## File: `.gitattributes`
```
/.yarn/releases/** binary
/.yarn/plugins/** binary
/dist/** linguist-generated=true
/lib/** linguist-generated=true
```

## File: `.gitignore`
```
# https://raw.githubusercontent.com/github/gitignore/main/Node.gitignore

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*
.pnpm-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage
*.lcov

# Dependency directories
node_modules/
jspm_packages/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Yarn Integrity file
.yarn-integrity

# dotenv environment variable files
.env
.env.development.local
.env.test.local
.env.production.local
.env.local

# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*
```

## File: `.prettierignore`
```
# Dependency directories
node_modules/
jspm_packages/

# yarn v2
.yarn/
```

## File: `.prettierrc.json`
```json
{
  "printWidth": 240,
  "tabWidth": 2,
  "useTabs": false,
  "semi": true,
  "singleQuote": true,
  "trailingComma": "none",
  "bracketSpacing": false,
  "arrowParens": "avoid"
}
```

## File: `.yarnrc.yml`
```yaml
# https://yarnpkg.com/configuration/yarnrc

compressionLevel: mixed
enableGlobalCache: false
enableHardenedMode: true

logFilters:
  - code: YN0013
    level: discard
  - code: YN0019
    level: discard
  - code: YN0076
    level: discard
  - code: YN0086
    level: discard

nodeLinker: node-modules
```

## File: `LICENSE`
```

                                 Apache License
                           Version 2.0, January 2004
                        https://www.apache.org/licenses/

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

   Copyright 2013-2018 Docker, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       https://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
[![GitHub release](https://img.shields.io/github/release/docker/login-action.svg?style=flat-square)](https://github.com/docker/login-action/releases/latest)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-docker--login-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/docker-login)
[![CI workflow](https://img.shields.io/github/actions/workflow/status/docker/login-action/ci.yml?branch=master&label=ci&logo=github&style=flat-square)](https://github.com/docker/login-action/actions?workflow=ci)
[![Test workflow](https://img.shields.io/github/actions/workflow/status/docker/login-action/test.yml?branch=master&label=test&logo=github&style=flat-square)](https://github.com/docker/login-action/actions?workflow=test)
[![Codecov](https://img.shields.io/codecov/c/github/docker/login-action?logo=codecov&style=flat-square)](https://codecov.io/gh/docker/login-action)

## About

GitHub Action to login against a Docker registry.

![Screenshot](.github/docker-login.png)

___

* [Usage](#usage)
  * [Docker Hub](#docker-hub)
  * [GitHub Container Registry](#github-container-registry)
  * [GitLab](#gitlab)
  * [Azure Container Registry (ACR)](#azure-container-registry-acr)
  * [Google Container Registry (GCR)](#google-container-registry-gcr)
  * [Google Artifact Registry (GAR)](#google-artifact-registry-gar)
  * [AWS Elastic Container Registry (ECR)](#aws-elastic-container-registry-ecr)
  * [AWS Public Elastic Container Registry (ECR)](#aws-public-elastic-container-registry-ecr)
  * [OCI Oracle Cloud Infrastructure Registry (OCIR)](#oci-oracle-cloud-infrastructure-registry-ocir)
  * [Quay.io](#quayio)
  * [DigitalOcean](#digitalocean-container-registry)
  * [Authenticate to multiple registries](#authenticate-to-multiple-registries)
  * [Set scopes for the authentication token](#set-scopes-for-the-authentication-token)
* [Customizing](#customizing)
  * [inputs](#inputs)
* [Contributing](#contributing)

## Usage

### Docker Hub

When authenticating to [Docker Hub](https://hub.docker.com) with GitHub Actions,
use a [personal access token](https://docs.docker.com/docker-hub/access-tokens/).
Don't use your account password.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
```

### GitHub Container Registry

To authenticate to the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry),
use the [`GITHUB_TOKEN`](https://docs.github.com/en/actions/reference/authentication-in-a-workflow)
secret.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to GitHub Container Registry
        uses: docker/login-action@v4
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
```

You may need to [manage write and read access of GitHub Actions](https://docs.github.com/en/packages/managing-github-packages-using-github-actions-workflows/publishing-and-installing-a-package-with-github-actions#upgrading-a-workflow-that-accesses-ghcrio)
for repositories in the container settings.

You can also use a [personal access token (PAT)](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
with the [appropriate scopes](https://docs.github.com/en/packages/getting-started-with-github-container-registry/migrating-to-github-container-registry-for-docker-images#authenticating-with-the-container-registry).

### GitLab

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to GitLab
        uses: docker/login-action@v4
        with:
          registry: registry.gitlab.com
          username: ${{ vars.GITLAB_USERNAME }}
          password: ${{ secrets.GITLAB_PASSWORD }}
```

If you have [Two-Factor Authentication](https://gitlab.com/help/user/profile/account/two_factor_authentication)
enabled, use a [Personal Access Token](https://gitlab.com/help/user/profile/personal_access_tokens)
instead of a password.

### Azure Container Registry (ACR)

[Create a service principal](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal#create-a-service-principal)
with access to your container registry through the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
and take note of the generated service principal's ID (also called _client ID_)
and password (also called _client secret_).

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to ACR
        uses: docker/login-action@v4
        with:
          registry: <registry-name>.azurecr.io
          username: ${{ vars.AZURE_CLIENT_ID }}
          password: ${{ secrets.AZURE_CLIENT_SECRET }}
```

> Replace `<registry-name>` with the name of your registry.

### Google Container Registry (GCR)

> [Google Artifact Registry](#google-artifact-registry-gar) is the evolution of
> Google Container Registry. As a fully-managed service with support for both
> container images and non-container artifacts. If you currently use Google
> Container Registry, use the information [on this page](https://cloud.google.com/artifact-registry/brain/knowledge/docs_legacy/transition/transition-from-gcr)
> to learn about transitioning to Google Artifact Registry. 

You can authenticate with workload identity federation or a service account.

#### Workload identity federation

Configure the workload identity federation for GitHub Actions in Google Cloud,
[see here](https://github.com/google-github-actions/auth#setting-up-workload-identity-federation).
Your service account must have permission to push to GCR. Use the
`google-github-actions/auth` action to authenticate using workload identity as
shown in the following example:

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
    -
      name: Authenticate to Google Cloud
      id: auth
      uses: google-github-actions/auth@v1
      with:
        token_format: access_token
        workload_identity_provider: <workload_identity_provider>
        service_account: <service_account>
    -
      name: Login to GCR
      uses: docker/login-action@v4
      with:
        registry: gcr.io
        username: oauth2accesstoken
        password: ${{ steps.auth.outputs.access_token }}
```

> Replace `<workload_identity_provider>` with configured workload identity
> provider. For steps to configure, [see here](https://github.com/google-github-actions/auth#setting-up-workload-identity-federation).

> Replace `<service_account>` with configured service account in workload
> identity provider which has access to push to GCR

#### Service account based authentication

Use a service account with permission to push to GCR and [configure access control](https://cloud.google.com/container-registry/brain/knowledge/docs_legacy/access-control).
Download the key for the service account as a JSON file. Save the contents of
the file [as a secret](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository)
named `GCR_JSON_KEY` in your GitHub repository. Set the username to `_json_key`.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to GCR
        uses: docker/login-action@v4
        with:
          registry: gcr.io
          username: _json_key
          password: ${{ secrets.GCR_JSON_KEY }}
```

### Google Artifact Registry (GAR)

You can authenticate with workload identity federation or a service account.

#### Workload identity federation

Your service account must have permission to push to GAR. Use the
`google-github-actions/auth` action to authenticate using workload identity as
shown in the following example:

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Authenticate to Google Cloud
        id: auth
        uses: google-github-actions/auth@v1
        with:
          token_format: access_token
          workload_identity_provider: <workload_identity_provider>
          service_account: <service_account>
      -
        name: Login to GAR
        uses: docker/login-action@v4
        with:
          registry: <location>-docker.pkg.dev
          username: oauth2accesstoken
          password: ${{ steps.auth.outputs.access_token }}
```

> Replace `<workload_identity_provider>` with configured workload identity
> provider

> Replace `<service_account>` with configured service account in workload
> identity provider which has access to push to GCR

> Replace `<location>` with the regional or multi-regional [location](https://cloud.google.com/artifact-registry/brain/knowledge/docs_legacy/repo-organize#locations)
> of the repository where the image is stored.

#### Service account based authentication

Use a service account with permission to push to GAR and [configure access control](https://cloud.google.com/artifact-registry/brain/knowledge/docs_legacy/access-control).
Download the key for the service account as a JSON file. Save the contents of
the file [as a secret](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository)
named `GAR_JSON_KEY` in your GitHub repository. Set the username to `_json_key`,
or `_json_key_base64` if you use a base64-encoded key.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to GAR
        uses: docker/login-action@v4
        with:
          registry: <location>-docker.pkg.dev
          username: _json_key
          password: ${{ secrets.GAR_JSON_KEY }}
```

> Replace `<location>` with the regional or multi-regional [location](https://cloud.google.com/artifact-registry/brain/knowledge/docs_legacy/repo-organize#locations)
> of the repository where the image is stored.

### AWS Elastic Container Registry (ECR)

Use an IAM user with the ability to [push to ECR with `AmazonEC2ContainerRegistryPowerUser` managed policy for example](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser).
Download the access keys and save them as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` [as secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository)
in your GitHub repo.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to ECR
        uses: docker/login-action@v4
        with:
          registry: <aws-account-number>.dkr.ecr.<region>.amazonaws.com
          username: ${{ vars.AWS_ACCESS_KEY_ID }}
          password: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

If you need to log in to Amazon ECR registries associated with other accounts,
you can use the `AWS_ACCOUNT_IDS` environment variable:

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to ECR
        uses: docker/login-action@v4
        with:
          registry: <aws-account-number>.dkr.ecr.<region>.amazonaws.com
          username: ${{ vars.AWS_ACCESS_KEY_ID }}
          password: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        env:
          AWS_ACCOUNT_IDS: 012345678910,023456789012
```

> Only available with [AWS CLI version 1](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login.html)

You can also use the [Configure AWS Credentials](https://github.com/aws-actions/configure-aws-credentials)
action in combination with this action:

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ vars.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: <region>
      -
        name: Login to ECR
        uses: docker/login-action@v4
        with:
          registry: <aws-account-number>.dkr.ecr.<region>.amazonaws.com
```

> Replace `<aws-account-number>` and `<region>` with their respective values.

### AWS Public Elastic Container Registry (ECR)

Use an IAM user with permission to push to ECR Public, for example using [managed policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerRegistryPowerUser).
Download the access keys and save them as `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` [secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository)
in your GitHub repository.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Public ECR
        uses: docker/login-action@v4
        with:
          registry: public.ecr.aws
          username: ${{ vars.AWS_ACCESS_KEY_ID }}
          password: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        env:
          AWS_REGION: <region>
```

> Replace `<region>` with its respective value (default `us-east-1`).

### OCI Oracle Cloud Infrastructure Registry (OCIR)

To push into OCIR in specific tenancy the [username](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/registry/index.html#LogintoOracleCloudInfrastructureRegistryfromtheDockerCLI)
must be placed in format `<tenancy>/<username>` (in case of federated tenancy use the format
`<tenancy-namespace>/oracleidentitycloudservice/<username>`).

For password [create an auth token](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/registry/index.html#GetanAuthToken).
Save username and token [as a secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository)
in your GitHub repo. 

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to OCIR
        uses: docker/login-action@v4
        with:
          registry: <region>.ocir.io
          username: ${{ vars.OCI_USERNAME }}
          password: ${{ secrets.OCI_TOKEN }}
```

> Replace `<region>` with their respective values from [availability regions](https://docs.cloud.oracle.com/iaas/Content/Registry/Concepts/registryprerequisites.htm#Availab)

### Quay.io

Use a [Robot account](https://docs.quay.io/glossary/robot-accounts.html) with
permission to push to a Quay.io repository.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Quay.io
        uses: docker/login-action@v4
        with:
          registry: quay.io
          username: ${{ vars.QUAY_USERNAME }}
          password: ${{ secrets.QUAY_ROBOT_TOKEN }}
```

### DigitalOcean Container Registry

Use your DigitalOcean registered email address and an API access token to authenticate.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to DigitalOcean Container Registry
        uses: docker/login-action@v4
        with:
          registry: registry.digitalocean.com
          username: ${{ vars.DIGITALOCEAN_USERNAME }}
          password: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}
```

### Authenticate to multiple registries

To authenticate against multiple registries, you can specify the login-action
step multiple times in your workflow:

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Login to GitHub Container Registry
        uses: docker/login-action@v4
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
```

You can also use the `registry-auth` input for raw authentication to
registries, defined as YAML objects. Each object have the same attributes as
current inputs (except `logout`):

> [!WARNING]
> We don't recommend using this method, it's better to use the action multiple
> times as shown above.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to registries
        uses: docker/login-action@v4
        with:
          registry-auth: |
            - username: ${{ vars.DOCKERHUB_USERNAME }}
              password: ${{ secrets.DOCKERHUB_TOKEN }}
            - registry: ghcr.io
              username: ${{ github.actor }}
              password: ${{ secrets.GITHUB_TOKEN }}
```

### Set scopes for the authentication token

The `scope` input allows limiting registry credentials to a specific repository
or namespace scope when building images with Buildx.

This is useful in GitHub Actions to avoid overriding the Docker Hub
authentication token embedded in GitHub-hosted runners, which is used for
pulling images without rate limits. By scoping credentials, you can
authenticate only where needed (typically for pushing), while keeping
unauthenticated pulls for base images.

When `scope` is set, credentials are written to the Buildx configuration
instead of the global Docker configuration. This means:
* Authentication applies only to the specified scope
* The default Docker Hub credentials remain available for pulls
* Credentials are used only by Buildx during the build

> [!IMPORTANT]
> Credentials written to the Buildx configuration are only accessible by Buildx.
> They are not available to `docker pull`, `docker push`, or any other Docker
> CLI commands outside Buildx.

> [!NOTE]
> This feature requires Buildx version 0.31.0 or later.

```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub (scoped)
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
          scope: 'myorg/myimage@push'
      -
        name: Build and push
        uses: docker/build-push-action@v6
        with:
          push: true
          tags: myorg/myimage:latest
```

In this example, base images are pulled using the embedded GitHub-hosted runner
credentials, while authenticated access is used only to push `myorg/myimage`.

## Customizing

### inputs

The following inputs can be used as `step.with` keys:

| Name            | Type   | Default     | Description                                                                   |
|-----------------|--------|-------------|-------------------------------------------------------------------------------|
| `registry`      | String | `docker.io` | Server address of Docker registry. If not set then will default to Docker Hub |
| `username`      | String |             | Username for authenticating to the Docker registry                            |
| `password`      | String |             | Password or personal access token for authenticating the Docker registry      |
| `scope`         | String |             | Scope for the authentication token                                            |
| `ecr`           | String | `auto`      | Specifies whether the given registry is ECR (`auto`, `true` or `false`)       |
| `logout`        | Bool   | `true`      | Log out from the Docker registry at the end of a job                          |
| `registry-auth` | YAML   |             | Raw authentication to registries, defined as YAML objects                     |

> [!NOTE]
> The `registry-auth` input cannot be used with other inputs except `logout`.

## Contributing

Want to contribute? Awesome! You can find information about contributing to
this project in the [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md)
```

## File: `action.yml`
```yaml
# https://help.github.com/en/articles/metadata-syntax-for-github-actions
name: 'Docker Login'
description: 'GitHub Action to login against a Docker registry'
author: 'docker'
branding:
  icon: 'anchor'
  color: 'blue'

inputs:
  registry:
    description: 'Server address of Docker registry. If not set then will default to Docker Hub'
    required: false
  username:
    description: 'Username used to log against the Docker registry'
    required: false
  password:
    description: 'Password or personal access token used to log against the Docker registry'
    required: false
  ecr:
    description: 'Specifies whether the given registry is ECR (auto, true or false)'
    required: false
  scope:
    description: 'Scope for the authentication token'
    required: false
  logout:
    description: 'Log out from the Docker registry at the end of a job'
    default: 'true'
    required: false
  registry-auth:
    description: 'Raw authentication to registries, defined as YAML objects'
    required: false

runs:
  using: 'node24'
  main: 'dist/index.js'
  post: 'dist/index.js'
```

## File: `codecov.yml`
```yaml
comment: false
github_checks:
  annotations: false
```

## File: `dev.Dockerfile`
```
# syntax=docker/dockerfile:1

ARG NODE_VERSION=24

FROM node:${NODE_VERSION}-alpine AS base
RUN apk add --no-cache cpio findutils git rsync
WORKDIR /src
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache <<EOT
  set -e
  corepack enable
  yarn --version
  yarn config set --home enableTelemetry 0
EOT

FROM base AS deps
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn install && mkdir /vendor && cp yarn.lock /vendor

FROM scratch AS vendor-update
COPY --from=deps /vendor /

FROM deps AS vendor-validate
RUN --mount=type=bind,target=.,rw <<EOT
  set -e
  git add -A
  cp -rf /vendor/* .
  if [ -n "$(git status --porcelain -- yarn.lock)" ]; then
    echo >&2 'ERROR: Vendor result differs. Please vendor your package with "docker buildx bake vendor"'
    git status --porcelain -- yarn.lock
    exit 1
  fi
EOT

FROM deps AS build
RUN --mount=target=/context \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules <<EOT
  set -e
  rsync -a /context/. .
  rm -rf dist
  yarn run build
  mkdir /out
  cp -r dist /out
EOT

FROM scratch AS build-update
COPY --from=build /out /

FROM build AS build-validate
RUN --mount=target=/context \
  --mount=target=.,type=tmpfs <<EOT
  set -e
  rsync -a /context/. .
  git add -A
  rm -rf dist
  cp -rf /out/* .
  if [ -n "$(git status --porcelain -- dist)" ]; then
    echo >&2 'ERROR: Build result differs. Please build first with "docker buildx bake build"'
    git status --porcelain -- dist
    exit 1
  fi
EOT

FROM deps AS format
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn run format && mkdir /out && find . -name '*.ts' -not -path './node_modules/*' -not -path './.yarn/*' | cpio -pdm /out

FROM scratch AS format-update
COPY --from=format /out /

FROM deps AS lint
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn run lint

FROM deps AS test
ENV RUNNER_TEMP=/tmp/github_runner
ENV RUNNER_TOOL_CACHE=/tmp/github_tool_cache
RUN --mount=type=bind,target=.,rw \
  --mount=type=cache,target=/src/.yarn/cache \
  --mount=type=cache,target=/src/node_modules \
  yarn run test --coverage --coverage.reportsDirectory=/tmp/coverage

FROM scratch AS test-coverage
COPY --from=test /tmp/coverage /
```

## File: `docker-bake.hcl`
```
target "_common" {
  args = {
    BUILDKIT_CONTEXT_KEEP_GIT_DIR = 1
  }
}

group "default" {
  targets = ["build"]
}

group "pre-checkin" {
  targets = ["vendor", "format", "build"]
}

group "validate" {
  targets = ["lint", "build-validate", "vendor-validate"]
}

target "build" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "build-update"
  output = ["."]
}

target "build-validate" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "build-validate"
  output = ["type=cacheonly"]
}

target "format" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "format-update"
  output = ["."]
}

target "lint" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "lint"
  output = ["type=cacheonly"]
}

target "vendor" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "vendor-update"
  output = ["."]
}

target "vendor-validate" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "vendor-validate"
  output = ["type=cacheonly"]
}

target "test" {
  inherits = ["_common"]
  dockerfile = "dev.Dockerfile"
  target = "test-coverage"
  output = ["./coverage"]
}
```

## File: `eslint.config.mjs`
```
import {defineConfig} from 'eslint/config';
import js from '@eslint/js';
import tseslint from '@typescript-eslint/eslint-plugin';
import vitest from '@vitest/eslint-plugin';
import globals from 'globals';
import eslintConfigPrettier from 'eslint-config-prettier/flat';
import eslintPluginPrettier from 'eslint-plugin-prettier';

export default defineConfig([
  {
    ignores: ['.yarn/**/*', 'coverage/**/*', 'dist/**/*']
  },
  js.configs.recommended,
  ...tseslint.configs['flat/recommended'],
  eslintConfigPrettier,
  {
    languageOptions: {
      globals: {
        ...globals.node
      }
    }
  },
  {
    files: ['__tests__/**'],
    ...vitest.configs.recommended,
    languageOptions: {
      globals: {
        ...globals.node,
        ...vitest.environments.env.globals
      }
    },
    rules: {
      ...vitest.configs.recommended.rules,
      'vitest/no-conditional-expect': 'error',
      'vitest/no-disabled-tests': 0
    }
  },
  {
    plugins: {
      prettier: eslintPluginPrettier
    },
    rules: {
      'prettier/prettier': 'error',
      '@typescript-eslint/no-require-imports': [
        'error',
        {
          allowAsImport: true
        }
      ]
    }
  }
]);
```

## File: `package.json`
```json
{
  "name": "docker-login",
  "description": "GitHub Action to login against a Docker registry",
  "type": "module",
  "main": "src/main.ts",
  "scripts": {
    "build": "ncc build --source-map --minify --license licenses.txt",
    "lint": "eslint --max-warnings=0 .",
    "format": "eslint --fix .",
    "test": "vitest run"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/docker/login-action.git"
  },
  "keywords": [
    "actions",
    "docker",
    "login"
  ],
  "author": "Docker Inc.",
  "license": "Apache-2.0",
  "packageManager": "yarn@4.9.2",
  "dependencies": {
    "@actions/core": "^3.0.0",
    "@aws-sdk/client-ecr": "^3.1000.0",
    "@aws-sdk/client-ecr-public": "^3.1000.0",
    "@docker/actions-toolkit": "^0.79.0",
    "http-proxy-agent": "^7.0.2",
    "https-proxy-agent": "^7.0.6",
    "js-yaml": "^4.1.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.3",
    "@types/js-yaml": "^4.0.9",
    "@types/node": "^24.11.0",
    "@typescript-eslint/eslint-plugin": "^8.56.1",
    "@typescript-eslint/parser": "^8.56.1",
    "@vercel/ncc": "^0.38.4",
    "@vitest/coverage-v8": "^4.0.18",
    "@vitest/eslint-plugin": "^1.6.9",
    "eslint": "^9.39.3",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-prettier": "^5.5.5",
    "globals": "^17.3.0",
    "prettier": "^3.8.1",
    "typescript": "^5.9.3",
    "vitest": "^4.0.18"
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "module": "nodenext",
    "moduleResolution": "nodenext",
    "esModuleInterop": true,
    "newLine": "lf",
    "outDir": "./lib",
    "rootDir": "./src",
    "forceConsistentCasingInFileNames": true,
    "noImplicitAny": false,
    "resolveJsonModule": true,
    "useUnknownInCatchVariables": false,
  },
  "include": [
    "src/**/*.ts"
  ]
}
```

## File: `vitest.config.ts`
```typescript
import {defineConfig} from 'vitest/config';

export default defineConfig({
  test: {
    clearMocks: true,
    environment: 'node',
    setupFiles: ['./__tests__/setup.unit.ts'],
    include: ['**/*.test.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['clover'],
      include: ['src/**/*.ts'],
      exclude: ['src/**/main.ts']
    }
  }
});
```

## File: `__tests__/aws.test.ts`
```typescript
import {beforeEach, describe, expect, test, vi} from 'vitest';
import {AuthorizationData} from '@aws-sdk/client-ecr';

import * as aws from '../src/aws.js';

describe('isECR', () => {
  test.each([
    ['registry.gitlab.com', false],
    ['gcr.io', false],
    ['012345678901.dkr.ecr.eu-west-3.amazonaws.com', true],
    ['876820548815.dkr.ecr.cn-north-1.amazonaws.com.cn', true],
    ['390948362332.dkr.ecr.cn-northwest-1.amazonaws.com.cn', true],
    ['012345678901.dkr-ecr.eu-north-1.on.aws', true],
    ['012345678901.dkr.ecr.eusc-de-east-1.amazonaws.eu', true],
    ['public.ecr.aws', true],
    ['ecr-public.aws.com', true]
  ])('given registry %p', async (registry, expected) => {
    expect(aws.isECR(registry)).toEqual(expected);
  });
});

describe('isPubECR', () => {
  test.each([
    ['registry.gitlab.com', false],
    ['gcr.io', false],
    ['012345678901.dkr.ecr.eu-west-3.amazonaws.com', false],
    ['876820548815.dkr.ecr.cn-north-1.amazonaws.com.cn', false],
    ['390948362332.dkr.ecr.cn-northwest-1.amazonaws.com.cn', false],
    ['012345678901.dkr-ecr.eu-north-1.on.aws', false],
    ['012345678901.dkr.ecr.eusc-de-east-1.amazonaws.eu', false],
    ['public.ecr.aws', true],
    ['ecr-public.aws.com', true]
  ])('given registry %p', async (registry, expected) => {
    expect(aws.isPubECR(registry)).toEqual(expected);
  });
});

describe('getRegion', () => {
  test.each([
    ['012345678901.dkr.ecr.eu-west-3.amazonaws.com', 'eu-west-3'],
    ['876820548815.dkr.ecr.cn-north-1.amazonaws.com.cn', 'cn-north-1'],
    ['390948362332.dkr.ecr.cn-northwest-1.amazonaws.com.cn', 'cn-northwest-1'],
    ['012345678901.dkr-ecr.eu-north-1.on.aws', 'eu-north-1'],
    ['012345678901.dkr.ecr.eusc-de-east-1.amazonaws.eu', 'eusc-de-east-1'],
    ['public.ecr.aws', 'us-east-1']
  ])('given registry %p', async (registry, expected) => {
    expect(aws.getRegion(registry)).toEqual(expected);
  });
});

describe('getAccountIDs', () => {
  test.each([
    ['012345678901.dkr.ecr.eu-west-3.amazonaws.com', undefined, ['012345678901']],
    ['012345678901.dkr.ecr.eu-west-3.amazonaws.com', '012345678910,023456789012', ['012345678901', '012345678910', '023456789012']],
    ['012345678901.dkr.ecr.eu-west-3.amazonaws.com', '012345678901,012345678910,023456789012', ['012345678901', '012345678910', '023456789012']],
    ['390948362332.dkr.ecr.cn-northwest-1.amazonaws.com.cn', '012345678910,023456789012', ['390948362332', '012345678910', '023456789012']],
    ['876820548815.dkr-ecr.eu-north-1.on.aws', '012345678910,023456789012', ['876820548815', '012345678910', '023456789012']],
    ['012345678901.dkr.ecr.eusc-de-east-1.amazonaws.eu', '012345678910,023456789012', ['012345678901', '012345678910', '023456789012']],
    ['public.ecr.aws', undefined, []]
  ])('given registry %p', async (registry, accountIDsEnv, expected) => {
    if (accountIDsEnv) {
      process.env.AWS_ACCOUNT_IDS = accountIDsEnv;
    }
    expect(aws.getAccountIDs(registry)).toEqual(expected);
  });
});

const mockEcrGetAuthToken = vi.fn();
const mockEcrPublicGetAuthToken = vi.fn();
vi.mock('@aws-sdk/client-ecr', () => {
  class ECR {
    getAuthorizationToken = mockEcrGetAuthToken;
  }
  return {
    ECR
  };
});
vi.mock('@aws-sdk/client-ecr-public', () => {
  class ECRPUBLIC {
    getAuthorizationToken = mockEcrPublicGetAuthToken;
  }
  return {
    ECRPUBLIC
  };
});

describe('getRegistriesData', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    delete process.env.AWS_ACCOUNT_IDS;
  });
  // prettier-ignore
  test.each([
    [
      '012345678901.dkr.ecr.aws-region-1.amazonaws.com',
      'dkr.ecr.aws-region-1.amazonaws.com', undefined,
      [
        {
          registry: '012345678901.dkr.ecr.aws-region-1.amazonaws.com',
          username: '012345678901',
          password: 'world'
        }
      ]
    ],
    [
      '012345678901.dkr.ecr.eu-west-3.amazonaws.com',
      'dkr.ecr.eu-west-3.amazonaws.com',
      '012345678910,023456789012',
      [
        {
          registry: '012345678901.dkr.ecr.eu-west-3.amazonaws.com',
          username: '012345678901',
          password: 'world'
        },
        {
          registry: '012345678910.dkr.ecr.eu-west-3.amazonaws.com',
          username: '012345678910',
          password: 'world'
        },
        {
          registry: '023456789012.dkr.ecr.eu-west-3.amazonaws.com',
          username: '023456789012',
          password: 'world'
        }
      ]
    ],
    [
      'public.ecr.aws',
      undefined,
      undefined,
      [
        {
          registry: 'public.ecr.aws',
          username: 'AWS',
          password: 'world'
        }
      ]
    ]
  ])('given registry %p', async (registry, fqdn, accountIDsEnv, expected: aws.RegistryData[]) => {
    if (accountIDsEnv) {
      process.env.AWS_ACCOUNT_IDS = accountIDsEnv;
    }
    const accountIDs = aws.getAccountIDs(registry);
    const authData: AuthorizationData[] = [];
    if (accountIDs.length == 0) {
      mockEcrPublicGetAuthToken.mockImplementation(() => {
        return Promise.resolve({
          authorizationData: {
            authorizationToken: Buffer.from(`AWS:world`).toString('base64'),
          }
        });
      });
    } else {
      aws.getAccountIDs(registry).forEach(accountID => {
        authData.push({
          authorizationToken: Buffer.from(`${accountID}:world`).toString('base64'),
          proxyEndpoint: `${accountID}.${fqdn}`
        });
      });
      mockEcrGetAuthToken.mockImplementation(() => {
        return Promise.resolve({
          authorizationData: authData
        });
      });
    }
    const regData = await aws.getRegistriesData(registry);
    expect(regData).toEqual(expected);
  });
});
```

## File: `__tests__/context.test.ts`
```typescript
import {afterEach, expect, test} from 'vitest';
import * as path from 'path';

import {Buildx} from '@docker/actions-toolkit/lib/buildx/buildx.js';

import {getAuthList, getInputs} from '../src/context.js';

afterEach(() => {
  for (const key of Object.keys(process.env)) {
    if (key.startsWith('INPUT_')) {
      delete process.env[key];
    }
  }
});

test('with password and username getInputs does not throw error', async () => {
  process.env['INPUT_USERNAME'] = 'dbowie';
  process.env['INPUT_PASSWORD'] = 'groundcontrol';
  process.env['INPUT_LOGOUT'] = 'true';
  expect(() => {
    getInputs();
  }).not.toThrow();
});

test('getAuthList uses the default Docker Hub registry when computing scoped config dir', async () => {
  process.env['INPUT_USERNAME'] = 'dbowie';
  process.env['INPUT_PASSWORD'] = 'groundcontrol';
  process.env['INPUT_SCOPE'] = 'myscope';
  process.env['INPUT_LOGOUT'] = 'false';
  const [auth] = getAuthList(getInputs());
  expect(auth).toMatchObject({
    registry: 'docker.io',
    configDir: path.join(Buildx.configDir, 'config', 'registry-1.docker.io', 'myscope')
  });
});
```

## File: `__tests__/docker.test.ts`
```typescript
import {expect, test, vi} from 'vitest';

import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';

import {loginStandard, logout} from '../src/docker.js';

test('loginStandard calls exec', async () => {
  const execSpy = vi.spyOn(Docker, 'getExecOutput').mockImplementation(async () => {
    return {
      exitCode: expect.any(Number),
      stdout: expect.any(Function),
      stderr: expect.any(Function)
    };
  });

  const username = 'dbowie';
  const password = 'groundcontrol';
  const registry = 'https://ghcr.io';

  await loginStandard(registry, username, password);

  expect(execSpy).toHaveBeenCalledTimes(1);
  const callfunc = execSpy.mock.calls[0];
  if (callfunc && callfunc[1]) {
    // we don't want to check env opt
    callfunc[1].env = undefined;
  }
  expect(execSpy).toHaveBeenCalledWith(['login', '--password-stdin', '--username', username, registry], {
    input: Buffer.from(password),
    silent: true,
    ignoreReturnCode: true
  });
});

test('logout calls exec', async () => {
  const execSpy = vi.spyOn(Docker, 'getExecOutput').mockImplementation(async () => {
    return {
      exitCode: expect.any(Number),
      stdout: expect.any(Function),
      stderr: expect.any(Function)
    };
  });

  const registry = 'https://ghcr.io';

  await logout(registry, '');

  expect(execSpy).toHaveBeenCalledTimes(1);
  const callfunc = execSpy.mock.calls[0];
  if (callfunc && callfunc[1]) {
    // we don't want to check env opt
    callfunc[1].env = undefined;
  }
  expect(execSpy).toHaveBeenCalledWith(['logout', registry], {
    ignoreReturnCode: true
  });
});
```

## File: `__tests__/setup.unit.ts`
```typescript
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'docker-login-action-'));

process.env = Object.assign({}, process.env, {
  TEMP: tmpDir,
  GITHUB_REPOSITORY: 'docker/login-action',
  RUNNER_TEMP: path.join(tmpDir, 'runner-temp'),
  RUNNER_TOOL_CACHE: path.join(tmpDir, 'runner-tool-cache')
});
```

## File: `src/aws.ts`
```typescript
import * as core from '@actions/core';
import {ECR} from '@aws-sdk/client-ecr';
import {ECRPUBLIC} from '@aws-sdk/client-ecr-public';
import {NodeHttpHandler} from '@smithy/node-http-handler';
import {HttpProxyAgent} from 'http-proxy-agent';
import {HttpsProxyAgent} from 'https-proxy-agent';

const ecrRegistryRegex = /^(([0-9]{12})\.(dkr\.ecr|dkr-ecr)\.(.+)\.(on\.aws|amazonaws\.(com(.cn)?|eu)))(\/([^:]+)(:.+)?)?$/;
const ecrPublicRegistryRegex = /public\.ecr\.aws|ecr-public\.aws\.com/;

export const isECR = (registry: string): boolean => {
  return ecrRegistryRegex.test(registry) || isPubECR(registry);
};

export const isPubECR = (registry: string): boolean => {
  return ecrPublicRegistryRegex.test(registry);
};

export const getRegion = (registry: string): string => {
  if (isPubECR(registry)) {
    return process.env.AWS_REGION || process.env.AWS_DEFAULT_REGION || 'us-east-1';
  }
  const matches = registry.match(ecrRegistryRegex);
  if (!matches) {
    return '';
  }
  return matches[4];
};

export const getAccountIDs = (registry: string): string[] => {
  if (isPubECR(registry)) {
    return [];
  }
  const matches = registry.match(ecrRegistryRegex);
  if (!matches) {
    return [];
  }
  const accountIDs: Array<string> = [matches[2]];
  if (process.env.AWS_ACCOUNT_IDS) {
    accountIDs.push(...process.env.AWS_ACCOUNT_IDS.split(','));
  }
  return accountIDs.filter((item, index) => accountIDs.indexOf(item) === index);
};

export interface RegistryData {
  registry: string;
  username: string;
  password: string;
}

export const getRegistriesData = async (registry: string, username?: string, password?: string): Promise<RegistryData[]> => {
  const region = getRegion(registry);
  const accountIDs = getAccountIDs(registry);

  const authTokenRequest = {};
  if (accountIDs.length > 0) {
    core.debug(`Requesting AWS ECR auth token for ${accountIDs.join(', ')}`);
    authTokenRequest['registryIds'] = accountIDs;
  }

  let httpProxyAgent;
  const httpProxy = process.env.http_proxy || process.env.HTTP_PROXY || '';
  if (httpProxy) {
    core.debug(`Using http proxy ${httpProxy}`);
    httpProxyAgent = new HttpProxyAgent(httpProxy);
  }

  let httpsProxyAgent;
  const httpsProxy = process.env.https_proxy || process.env.HTTPS_PROXY || '';
  if (httpsProxy) {
    core.debug(`Using https proxy ${httpsProxy}`);
    httpsProxyAgent = new HttpsProxyAgent(httpsProxy);
  }

  const credentials =
    username && password
      ? {
          accessKeyId: username,
          secretAccessKey: password
        }
      : undefined;

  if (isPubECR(registry)) {
    core.info(`AWS Public ECR detected with ${region} region`);
    const ecrPublic = new ECRPUBLIC({
      customUserAgent: 'docker-login-action',
      credentials,
      region: region,
      requestHandler: new NodeHttpHandler({
        httpAgent: httpProxyAgent,
        httpsAgent: httpsProxyAgent
      })
    });
    const authTokenResponse = await ecrPublic.getAuthorizationToken(authTokenRequest);
    if (!authTokenResponse.authorizationData || !authTokenResponse.authorizationData.authorizationToken) {
      throw new Error('Could not retrieve an authorization token from AWS Public ECR');
    }
    const authToken = Buffer.from(authTokenResponse.authorizationData.authorizationToken, 'base64').toString('utf-8');
    const creds = authToken.split(':', 2);
    core.setSecret(creds[0]); // redacted in workflow logs
    core.setSecret(creds[1]); // redacted in workflow logs
    return [
      {
        registry: 'public.ecr.aws',
        username: creds[0],
        password: creds[1]
      }
    ];
  } else {
    core.info(`AWS ECR detected with ${region} region`);
    const ecr = new ECR({
      customUserAgent: 'docker-login-action',
      credentials,
      region: region,
      requestHandler: new NodeHttpHandler({
        httpAgent: httpProxyAgent,
        httpsAgent: httpsProxyAgent
      })
    });
    const authTokenResponse = await ecr.getAuthorizationToken(authTokenRequest);
    if (!Array.isArray(authTokenResponse.authorizationData) || !authTokenResponse.authorizationData.length) {
      throw new Error('Could not retrieve an authorization token from AWS ECR');
    }
    const regDatas: RegistryData[] = [];
    for (const authData of authTokenResponse.authorizationData) {
      const authToken = Buffer.from(authData.authorizationToken || '', 'base64').toString('utf-8');
      const creds = authToken.split(':', 2);
      core.setSecret(creds[0]); // redacted in workflow logs
      core.setSecret(creds[1]); // redacted in workflow logs
      regDatas.push({
        registry: authData.proxyEndpoint || '',
        username: creds[0],
        password: creds[1]
      });
    }
    return regDatas;
  }
};
```

## File: `src/context.ts`
```typescript
import path from 'path';
import * as core from '@actions/core';
import * as yaml from 'js-yaml';

import {Buildx} from '@docker/actions-toolkit/lib/buildx/buildx.js';
import {Util} from '@docker/actions-toolkit/lib/util.js';

export interface Inputs {
  registry: string;
  username: string;
  password: string;
  scope: string;
  ecr: string;
  logout: boolean;
  registryAuth: string;
}

export interface Auth {
  registry: string;
  username: string;
  password: string;
  scope: string;
  ecr: string;
  configDir: string;
}

export function getInputs(): Inputs {
  return {
    registry: core.getInput('registry'),
    username: core.getInput('username'),
    password: core.getInput('password'),
    scope: core.getInput('scope'),
    ecr: core.getInput('ecr'),
    logout: core.getBooleanInput('logout'),
    registryAuth: core.getInput('registry-auth')
  };
}

export function getAuthList(inputs: Inputs): Array<Auth> {
  if (inputs.registryAuth && (inputs.registry || inputs.username || inputs.password || inputs.scope || inputs.ecr)) {
    throw new Error('Cannot use registry-auth with other inputs');
  }
  let auths: Array<Auth> = [];
  if (!inputs.registryAuth) {
    const registry = inputs.registry || 'docker.io';
    auths.push({
      registry,
      username: inputs.username,
      password: inputs.password,
      scope: inputs.scope,
      ecr: inputs.ecr || 'auto',
      configDir: scopeToConfigDir(registry, inputs.scope)
    });
  } else {
    auths = (yaml.load(inputs.registryAuth) as Array<Auth>).map(auth => {
      core.setSecret(auth.password); // redacted in workflow logs
      const registry = auth.registry || 'docker.io';
      return {
        registry,
        username: auth.username,
        password: auth.password,
        scope: auth.scope,
        ecr: auth.ecr || 'auto',
        configDir: scopeToConfigDir(registry, auth.scope)
      };
    });
  }
  if (auths.length == 0) {
    throw new Error('No registry to login');
  }
  return auths;
}

export function scopeToConfigDir(registry: string, scope?: string): string {
  if (scopeDisabled() || !scope || scope === '') {
    return '';
  }
  let configDir = path.join(Buildx.configDir, 'config', registry === 'docker.io' ? 'registry-1.docker.io' : registry);
  if (scope.startsWith('@')) {
    configDir += scope;
  } else {
    configDir = path.join(configDir, scope);
  }
  return configDir;
}

function scopeDisabled(): boolean {
  if (process.env.DOCKER_LOGIN_SCOPE_DISABLED) {
    return Util.parseBool(process.env.DOCKER_LOGIN_SCOPE_DISABLED);
  }
  return false;
}
```

## File: `src/docker.ts`
```typescript
import * as core from '@actions/core';

import {Docker} from '@docker/actions-toolkit/lib/docker/docker.js';

import * as aws from './aws.js';
import * as context from './context.js';

export async function login(auth: context.Auth): Promise<void> {
  if (/true/i.test(auth.ecr) || (auth.ecr == 'auto' && aws.isECR(auth.registry))) {
    await loginECR(auth.registry, auth.username, auth.password, auth.scope);
  } else {
    await loginStandard(auth.registry, auth.username, auth.password, auth.scope);
  }
}

export async function logout(registry: string, configDir: string): Promise<void> {
  let envs: {[key: string]: string} | undefined;
  if (configDir !== '') {
    envs = Object.assign({}, process.env, {
      DOCKER_CONFIG: configDir
    }) as {
      [key: string]: string;
    };
    core.info(`Alternative config dir: ${configDir}`);
  }
  await Docker.getExecOutput(['logout', registry], {
    ignoreReturnCode: true,
    env: envs
  }).then(res => {
    if (res.stderr.length > 0 && res.exitCode != 0) {
      core.warning(res.stderr.trim());
    }
  });
}

export async function loginStandard(registry: string, username: string, password: string, scope?: string): Promise<void> {
  if (!username && !password) {
    throw new Error('Username and password required');
  }
  if (!username) {
    throw new Error('Username required');
  }
  if (!password) {
    throw new Error('Password required');
  }
  await loginExec(registry, username, password, scope);
}

export async function loginECR(registry: string, username: string, password: string, scope?: string): Promise<void> {
  core.info(`Retrieving registries data through AWS SDK...`);
  const regDatas = await aws.getRegistriesData(registry, username, password);
  for (const regData of regDatas) {
    await loginExec(regData.registry, regData.username, regData.password, scope);
  }
}

async function loginExec(registry: string, username: string, password: string, scope?: string): Promise<void> {
  let envs: {[key: string]: string} | undefined;
  const configDir = context.scopeToConfigDir(registry, scope);
  if (configDir !== '') {
    envs = Object.assign({}, process.env, {
      DOCKER_CONFIG: configDir
    }) as {
      [key: string]: string;
    };
    core.info(`Logging into ${registry} (scope ${scope})...`);
  } else {
    core.info(`Logging into ${registry}...`);
  }
  await Docker.getExecOutput(['login', '--password-stdin', '--username', username, registry], {
    ignoreReturnCode: true,
    silent: true,
    input: Buffer.from(password),
    env: envs
  }).then(res => {
    if (res.stderr.length > 0 && res.exitCode != 0) {
      throw new Error(res.stderr.trim());
    }
    core.info('Login Succeeded!');
  });
}
```

## File: `src/main.ts`
```typescript
import * as core from '@actions/core';
import * as actionsToolkit from '@docker/actions-toolkit';

import * as context from './context.js';
import * as docker from './docker.js';
import * as stateHelper from './state-helper.js';

export async function main(): Promise<void> {
  const inputs: context.Inputs = context.getInputs();
  stateHelper.setLogout(inputs.logout);

  const auths = context.getAuthList(inputs);
  stateHelper.setRegistries(Array.from(new Map(auths.map(auth => [`${auth.registry}|${auth.configDir}`, {registry: auth.registry, configDir: auth.configDir} as stateHelper.RegistryState])).values()));

  if (auths.length === 1) {
    await docker.login(auths[0]);
    return;
  }

  for (const auth of auths) {
    await core.group(`Login to ${auth.registry}`, async () => {
      await docker.login(auth);
    });
  }
}

async function post(): Promise<void> {
  if (!stateHelper.logout) {
    return;
  }
  for (const registryState of stateHelper.registries) {
    await core.group(`Logout from ${registryState.registry}`, async () => {
      await docker.logout(registryState.registry, registryState.configDir);
    });
  }
}

actionsToolkit.run(main, post);
```

## File: `src/state-helper.ts`
```typescript
import * as core from '@actions/core';

export const registries = process.env['STATE_registries'] ? (JSON.parse(process.env['STATE_registries']) as Array<RegistryState>) : [];
export const logout = /true/i.test(process.env['STATE_logout'] || '');

export interface RegistryState {
  registry: string;
  configDir: string;
}

export function setRegistries(registries: Array<RegistryState>) {
  core.saveState('registries', JSON.stringify(registries));
}

export function setLogout(logout: boolean) {
  core.saveState('logout', logout);
}
```

