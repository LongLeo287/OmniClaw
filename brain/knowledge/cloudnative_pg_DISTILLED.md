---
id: cloudnative-pg
type: knowledge
owner: OA_Triage
---
# cloudnative-pg
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![CNCF Landscape](https://img.shields.io/badge/CNCF%20Landscape-5699C6)][cncf-landscape]
[![Latest Release](https://img.shields.io/github/v/release/cloudnative-pg/cloudnative-pg.svg)][latest-release]
[![GitHub License](https://img.shields.io/github/license/cloudnative-pg/cloudnative-pg)][license]
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9933/badge)][openssf]
[![OpenSSF Baseline](https://www.bestpractices.dev/projects/9933/baseline)][openssf]
[![OpenSSF Scorecard Badge][openssf-scorecard-badge]][openssf-socrecard-view]
[![Documentation][documentation-badge]][documentation]
[![Stack Overflow](https://img.shields.io/badge/stackoverflow-cloudnative--pg-blue?logo=stackoverflow&logoColor=%23F48024&link=https%3A%2F%2Fstackoverflow.com%2Fquestions%2Ftagged%2Fcloudnative-pg)][stackoverflow]
[![FOSSA Status][fossa-badge]][fossa]
[![CLOMonitor](https://img.shields.io/endpoint?url=https://clomonitor.io/api/projects/cncf/cloudnative-pg/badge)](https://clomonitor.io/projects/cncf/cloudnative-pg)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/cloudnative-pg)](https://artifacthub.io/packages/search?repo=cloudnative-pg)

# Welcome to the CloudNativePG Project!

**CloudNativePG (CNPG)** is an open-source platform designed to seamlessly
manage [PostgreSQL](https://www.postgresql.org/) databases in Kubernetes
environments. It covers the entire operational lifecycle—from deployment to
ongoing maintenance—through its core component, the CloudNativePG operator.

## Table of Contents

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Governance Policies](https://github.com/cloudnative-pg/governance/blob/main/GOVERNANCE.md)
- [Contributing](CONTRIBUTING.md)
- [Adopters](ADOPTERS.md)
- [Commercial Support](https://cloudnative-pg.io/support/)
- [License](LICENSE)

## Getting Started

The best way to get started is the [Quickstart Guide](https://cloudnative-pg.io/docs/devel/quickstart/).

## Scope

### Mission

CloudNativePG aims to increase PostgreSQL adoption within Kubernetes by making
it an integral part of the development process and GitOps-driven CI/CD
automation.

### Core Principles & Features

Designed by PostgreSQL experts for Kubernetes administrators, CloudNativePG
follows a Kubernetes-native approach to PostgreSQL primary/standby cluster
management. Instead of relying on external high-availability tools (like
Patroni, repmgr, or Stolon), it integrates directly with the Kubernetes API to
automate database operations that a skilled DBA would perform manually.

Key design decisions include:

- Direct integration with Kubernetes API: The PostgreSQL cluster’s status is
  available directly in the `Cluster` resource, allowing users to inspect it
  via the Kubernetes API.
- Operator pattern: The operator ensures that the desired PostgreSQL state is
  reconciled automatically, following Kubernetes best practices.
- Immutable application containers: Updates follow an immutable infrastructure
  model, as explained in
  ["Why EDB Chose Immutable Application Containers"](https://www.enterprisedb.com/blog/why-edb-chose-immutable-application-containers).

### How CloudNativePG Works

The operator continuously monitors and updates the PostgreSQL cluster state.
Examples of automated actions include:

- Failover management: If the primary instance fails, the operator elects a new
  primary, updates the cluster status, and orchestrates the transition.
- Scaling read replicas: When the number of desired replicas changes, the
  operator provisions or removes resources such as persistent volumes, secrets,
  and config maps while managing streaming replication.
- Service updates: Kubernetes remains the single source of truth, ensuring
  that PostgreSQL service endpoints are always up to date.
- Rolling updates: When an image is updated, the operator follows a rolling
  strategy—first updating replica pods before performing a controlled
  switchover for the primary.

CloudNativePG manages additional Kubernetes resources to enhance PostgreSQL
management, including: `Backup`, `ClusterImageCatalog`, `Database`,
`ImageCatalog`, `Pooler`, `Publication`, `ScheduledBackup`, and `Subscription`.

## Out of Scope

- **Kubernetes only:** CloudNativePG is dedicated to vanilla Kubernetes
  maintained by the [Cloud Native Computing Foundation
  (CNCF)](https://kubernetes.io/).
- **PostgreSQL only:** CloudNativePG is dedicated to vanilla PostgreSQL
  maintained by the [PostgreSQL Global Development Group
  (PGDG)](https://www.postgresql.org/about/).
- **No support for forks:** Features from PostgreSQL forks will only be
  considered if they can be integrated as extensions or pluggable frameworks.
- **Not a general-purpose database operator:** CloudNativePG does not support
  other databases (e.g., MariaDB).

CloudNativePG can be extended via the [CNPG-I plugin interface](https://github.com/cloudnative-pg/cnpg-i).

## Communications

- [Github Discussions](https://github.com/cloudnative-pg/cloudnative-pg/discussions)
- [Slack](https://cloud-native.slack.com/archives/C08MAUJ7NPM)
  (join the [CNCF Slack Workspace](https://communityinviter.com/apps/cloud-native/cncf)).
- [Twitter](https://twitter.com/CloudNativePg)
- [Mastodon](https://mastodon.social/@CloudNativePG)
- [Bluesky](https://bsky.app/profile/cloudnativepg.bsky.social)

## Resources

- [Roadmap](ROADMAP.md)
- [Website](https://cloudnative-pg.io)
- [FAQ](docs/src/faq.md)
- [Blog](https://cloudnative-pg.io/blog/)
- [CloudNativePG plugin Interface (CNPG-I)](https://github.com/cloudnative-pg/cnpg-i).

## Adopters

A list of publicly known users of the CloudNativePG operator is in [ADOPTERS.md](ADOPTERS.md).
Help us grow our community and CloudNativePG by adding yourself and your
organization to this list!

### CloudNativePG at KubeCon

- November 10, 2025, KubeCon North America 2025 in Atlanta: ["Project Lightning Talk: CloudNativePG: Running Postgres The Kubernetes Way"](https://www.youtube.com/watch?v=pYwYwehQX3U&t=4s) - Gabriele Bartolini, EDB
- November 11, 2025, KubeCon North America 2025 in Atlanta: ["Modern PostgreSQL Authorization With Keycloak: Cloud Native Identity Meets Database Security"](https://www.youtube.com/watch?v=TYgPemq06fg) - Yoshiyuki Tabata, Hitachi, Ltd. & Gabriele Bartolini, EDB
- November 13, 2025, KubeCon North America 2025 in Atlanta: ["Quorum-Based Consistency for Cluster Changes With CloudNativePG Operator"](https://www.youtube.com/watch?v=iQUOO3-JRK4&list=PLj6h78yzYM2MLSW4tUDO2gs2pR5UpiD0C&index=67) - Jeremy Schneider, GEICO Tech & Gabriele Bartolini, EDB
- April 4, 2025, KubeCon Europe in London: ["Consistent Volume Group Snapshots, Unraveling the Magic"](https://sched.co/1tx8g) - Leonardo Cecchi (EDB) and Xing Yang (VMware)
- November 11, 2024, Cloud Native Rejekts NA 2024: ["Maximising Microservice Databases with Kubernetes, Postgres, and CloudNativePG"](https://www.youtube.com/watch?v=uBzl_stoxoc&ab_channel=CloudNativeRejekts) - Gabriele Bartolini (EDB) and Leonardo Cecchi (EDB)
- March 21, 2024, KubeCon Europe 2024 in Paris: ["Scaling Heights: Mastering Postgres Database Vertical Scalability with Kubernetes Storage Magic"](https://kccnceu2024.sched.com/event/1YeM4/scaling-heights-mastering-postgres-database-vertical-scalability-with-kubernetes-storage-magic-gabriele-bartolini-edb-gari-singh-google) - Gari Singh, Google & Gabriele Bartolini, EDB
- March 19, 2024, Data on Kubernetes Day at KubeCon Europe 2024 in Paris: ["From Zero to Hero: Scaling Postgres in Kubernetes Using the Power of CloudNativePG"](https://colocatedeventseu2024.sched.com/event/1YFha/from-zero-to-hero-scaling-postgres-in-kubernetes-using-the-power-of-cloudnativepg-gabriele-bartolini-edb) - Gabriele Bartolini, EDB
- November 7, 2023, KubeCon North America 2023 in Chicago: ["Disaster Recovery with Very Large Postgres Databases (in Kubernetes)"](https://kccncna2023.sched.com/event/1R2ml/disaster-recovery-with-very-large-postgres-databases-gabriele-bartolini-edb-michelle-au-google) - Michelle Au, Google & Gabriele Bartolini, EDB
- October 27, 2022, KubeCon North America 2022 in Detroit: ["Data On Kubernetes, Deploying And Running PostgreSQL And Patterns For Databases In a Kubernetes Cluster"](https://kccncna2022.sched.com/event/182GB/data-on-kubernetes-deploying-and-running-postgresql-and-patterns-for-databases-in-a-kubernetes-cluster-chris-milsted-ondat-gabriele-bartolini-edb) - Chris Milsted, Ondat & Gabriele Bartolini, EDB

### Useful links

- ["Quorum-Based Consistency for Cluster Changes With CloudNativePG Operator"](https://www.youtube.com/watch?v=sRF09UMAlsI) (webinar) - Jeremy Schneider, GEICO Tech & Leonardo Cecchi, EDB
- [Data on Kubernetes (DoK) Community](https://dok.community/)
- ["Cloud Neutral Postgres Databases with Kubernetes and CloudNativePG" by Gabriele Bartolini](https://www.cncf.io/blog/2024/11/20/cloud-neutral-postgres-databases-with-kubernetes-and-cloudnativepg/) (November 2024)
- ["How to migrate your PostgreSQL database in Kubernetes with ~0 downtime from anywhere" by Gabriele Bartolini](https://gabrielebartolini.it/articles/2024/03/cloudnativepg-recipe-5-how-to-migrate-your-postgresql-database-in-kubernetes-with-~0-downtime-from-anywhere/) (March 2024)
- ["Maximizing Microservice Databases with Kubernetes, Postgres, and CloudNativePG" by Gabriele Bartolini](https://gabrielebartolini.it/articles/2024/02/maximizing-microservice-databases-with-kubernetes-postgres-and-cloudnativepg/) (February 2024)
- ["Recommended Architectures for PostgreSQL in Kubernetes" by Gabriele Bartolini](https://www.cncf.io/blog/2023/09/29/recommended-architectures-for-postgresql-in-kubernetes/) (September 2023)
- ["The Current State of Major PostgreSQL Upgrades with CloudNativePG" by Gabriele Bartolini](https://www.enterprisedb.com/blog/current-state-major-postgresql-upgrades-cloudnativepg-kubernetes) (August 2023)
- ["The Rise of the Kubernetes Native Database" by Jeff Carpenter](https://thenewstack.io/the-rise-of-the-kubernetes-native-database/) (December 2022)
- ["Why Run Postgres in Kubernetes?" by Gabriele Bartolini](https://cloudnativenow.com/kubecon-cnc-eu-2022/why-run-postgres-in-kubernetes/) (May 2022)
- ["Shift-Left Security: The Path To PostgreSQL On Kubernetes" by Gabriele Bartolini](https://www.tfir.io/shift-left-security-the-path-to-postgresql-on-kubernetes/) (April 2021)
- ["Local Persistent Volumes and PostgreSQL usage in Kubernetes" by Gabriele Bartolini](https://www.2ndquadrant.com/en/blog/local-persistent-volumes-and-postgresql-usage-in-kubernetes/) (June 2020)

---

<p align="center">
We are a <a href="https://www.cncf.io/sandbox-projects/">Cloud Native Computing Foundation Sandbox project</a>.
</p>

<p style="text-align:center;" align="center">
      <picture align="center">
         <source media="(prefers-color-scheme: dark)" srcset="https://github.com/cncf/artwork/blob/main/other/cncf/horizontal/white/cncf-white.svg?raw=true">
         <source media="(prefers-color-scheme: light)" srcset="https://github.com/cncf/artwork/blob/main/other/cncf/horizontal/color/cncf-color.svg?raw=true">
         <img align="center" src="https://github.com/cncf/artwork/blob/main/other/cncf/horizontal/color/cncf-color.svg?raw=true" alt="CNCF logo" width="50%"/>
      </picture>
</p>

---

<p align="center">
CloudNativePG was originally built and sponsored by <a href="https://www.enterprisedb.com">EDB</a>.
</p>

<p style="text-align:center;" align="center">
      <picture align="center">
         <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cloudnative-pg/.github/main/logo/edb_landscape_color_white.svg">
         <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/cloudnative-pg/.github/main/logo/edb_landscape_color_grey.svg">
         <img align="center" src="https://raw.githubusercontent.com/cloudnative-pg/.github/main/logo/edb_landscape_color_grey.svg" alt="EDB logo" width="25%"/>
      </picture>
</p>

---

<p align="center">
<a href="https://www.postgresql.org/about/policies/trademarks/">Postgres, PostgreSQL, and the Slonik Logo</a>
are trademarks or registered trademarks of the PostgreSQL Community Association
of Canada, and used with their permission.
</p>

---

[cncf-landscape]: https://landscape.cncf.io/?item=app-definition-and-development--database--cloudnativepg
[stackoverflow]: https://stackoverflow.com/questions/tagged/cloudnative-pg
[latest-release]: https://github.com/cloudnative-pg/cloudnative-pg/releases/latest
[documentation]: https://cloudnative-pg.io/docs
[license]: https://github.com/cloudnative-pg/cloudnative-pg?tab=Apache-2.0-1-ov-file#readme
[openssf]: https://www.bestpractices.dev/projects/9933
[openssf-scorecard-badge]: https://api.scorecard.dev/projects/github.com/cloudnative-pg/cloudnative-pg/badge
[openssf-socrecard-view]: https://scorecard.dev/viewer/?uri=github.com/cloudnative-pg/cloudnative-pg
[documentation-badge]: https://img.shields.io/badge/Documentation-white?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAGN0lEQVR4nJRXXWwcVxU%2B8%2F%2BzP%2BPZtR2v7dqy07jUJUALNaiK6lZyUVVKWgGKaIv8QCMekBAVQlQICcEzVZFQVYFKQhASEBHlISJPCRJEshTFChgrIYHEiYMh69jetffHM7Mzc%2B9Bs7vjnTs7yZpZWbt37s%2F5zne%2Bc861CD0eXRkbHc3NfjeffvxNAGEAgULD2756v35%2B3qe1Nc4fnQVEXlA2LnOcXlCF8S%2B6vvVgq%2FL3M65X3e51PvfQCU4WJgZe%2B8GQ8fS7AKgjBB8KEHwjDXZSjkf0CREAaXM2eI9c65siqWxWl360Xl74ANHz%2Fy8AitxnTBfmz%2BhyYS4wGhwObQCIHSA0AigOMBzvOsXzd4pnjyL6NMmWEH8hi2b28Og3%2FqRJA0ewfQy0v1vGO2NovwPo%2FEU%2FwVgSU1PI%2BSu79v3lJAB8HM%2BTI%2FO%2FUUXzM4xHIe0xI4DdRqOAwnF%2F38ePPyzaDIDh%2FMxcWh462m08aojuGY97C0nrAEHg9BlF0fmeAPr0J15vbaKsp0BZQzEDEAlP9B209UIIVXUta%2FQEQHwxgxFjTc%2BRskAwrgVWmHtg22vMPJwLDqGUNJIAMHVAkGu3WdpZz6NAkgSXpINSycluV28er1a3rJ4M3F2%2F9AtCvXKycRrTQttrjINjxxxIL9jevxdaDHU%2FTBr6pL5ruzuLZubgUQBOY2hPij3GBUe7tBCMBRE2KrXVSz0BBI%2FtPVgtV%2F%2FxkZ5WSjI%2F%2BFIXC3sHJwgT4yFqrZFFTSlVrp3sGYLwcfxSmXCbS00j2Ms4K7qkOsFx6qdTuiHtG4AimfmM8NyvOvR2G48qXtZ2fsfrN7%2BqpcRyUp0glKiimDm4TwAcHBp%2B9WeA4ki0GMWNR9OVF8BZvn7xtI%2FF09H8jzLEgz6yLwCDuelnFXHkTZZOytCOEdqDOtGwsm%2BNj00fXt%2B6%2Bj4vcA7bwNrZwENmXwAKuZnvsNRThs5ozMPfPiHyoDF7xiduHcXb70A8dRFheHjiySQATBZk0nl9MHPkBEWUoEtYjyrPFNwGzfdlD37Zdu98KCv%2BMmD2BYpUCvcST39e0%2BS1Wr249FAAg7mPzWrS5NstEbE0xrsiA6QN1PfRFLnhr%2BspxVJTlY8Mw1DqNXeyCQFREEXz9cHB0QOev73QaNhOF4B%2B45PHFHFgDhJTqjuubJFqX1KQco7NTTuW8kq95k2G4eLEGzM7lfItnjNeTKcOfV%2FT8hOuV77A9IK0XjgMpCO0ZiuV3L%2F6njCFAOmucGB3OII5XgCXEJTDdZLElVbu3Vz0fWexvL30k0B6ggBACOmIUBAEUKX0dDTvW7RCYcdZPq6n%2FSsQnUO2RuyBRgQ9Rc5mMvJ6CNIj1nXfd9qWAsCkaZzJAk1L8UjVqY737dSjfCGrPHWqXL32Q0mB%2F2BXnke00WaEYv2aTzAbnuV5pcWkDGAAGJmhSafh6hjr%2BW2SVYHrP7bb%2BOdPW%2FUgflGlTM2gaK%2Ft7tp6%2BN6yixdN89DcIwGktIFPABfNbwoQqQWEUnDJzg1g0jDeK5p7Kp7nensXFI7uyAr%2FLyM7fYLnpa6LYScE8vDnot5hrKlslm%2BfE3nVxJgO4o3KcYu%2FF8XM8yFQ27n%2F65Te%2FzKl3Jhpjj6TCIDneRD5%2FItxr1vdkALw7p1qfeWPpjHxMtsXaPxu6FLc%2BrnbSB1r7fcrlr36nqwMzQfnplJDryQCGOh%2FbLjhcM%2FEvQ4Pdund9xRV5m1LfTXaF%2BK9gsLGB9nsgddcz8thM%2FarPzYM8%2FFazf9sMFaU%2Fi%2FwvNANwEhPvUGR8ozn7d%2
... [TRUNCATED]
```

### File: docs\README.md
```md
# CloudNativePG documentation

CloudNativePG documentation is written in Markdown from the `docs` folder. The
`src` folder contains the sources with the `.md` extension.

We have adopted [Docusaurus](https://docusaurus.io/) as an open
source solution to build the documentation starting from Markdown
format.

Before you submit a pull request for the documentation, you must have
gone through the following steps:

1. local test of the documentation
2. run through the spell checker

## How to locally test the documentation

To ensure your documentation changes look correct before creating a Pull
Request, you can build and view the documentation locally using Docker.

Execute the following command in your terminal. This command uses the same
infrastructure as the official CloudNativePG documentation website, mounting
your local files for preview:

```bash
docker run --rm -ti -p 3000:3000 \
    -v ./src:/website/docs \
    ghcr.io/cloudnative-pg/docs:latest
```

Once the server is running, open your browser and navigate to the local
documentation preview at: `http://127.0.0.1:3000/docs/next/`.

Thoroughly check your changes—put yourself in the end user's shoes to verify
clarity and accuracy. Complete a final spell check, and then proceed with
submitting your pull request.

## How to run the spell checker

Every time you work on the documentation, please run from the top directory:

``` bash
make spellcheck
```

This will run a spell checker and highlight all the words that need to be
either fixed or added to the `.wordlist-en-custom.txt` file.

## Reminders

If you added samples to `docs/src/samples` or modified existing samples, please
consider if they should be included in the curated [list of examples](src/samples.md)

And please help keeping the samples in the curated list, as well as any samples
named `cluster-example-*` in runnable condition.
These can be a big help for beginners.

## License

The CloudNativePG documentation and all the work under the `docs` folder is
licensed under a Creative Commons Attribution 4.0 International License.

<!-- SPDX-License-Identifier: CC-BY-4.0 -->

```

### File: .spellcheck.yaml
```yaml
matrix:
- name: markdown
  sources:
  - 'docs/src/*.md'
  - 'docs/src/*/*.md'
  - 'config/olm-manifests/bases/*.yaml'
  default_encoding: utf-8
  aspell:
    lang: en
    d: en_US
  dictionary:
    wordlists:
    - .wordlist-en-custom.txt
  pipeline:
    - pyspelling.filters.context:
        context_visible_first: true
        delimiters:
          # Ignore multiline content between fences (fences can have 3 or more back ticks)
          # ```
          # content
          # ```
          - open: '(?s)^(?P<open> *`{3,})'
            close: '^(?P=open)$'
            # Ignore text between inline back ticks
          - open: '(?P<open>`+)'
            close: '(?P=open)'
          - open: '(?P<open><!--)'
            close: '(?P<close>-->)'
          - open: '.*base64data.*'
            close: "$"
    - pyspelling.filters.url:

```

### File: .woke.yaml
```yaml
ignore_files:
  - config/crd/bases/postgresql.cnpg.io_poolers.yaml
  - tests/e2e/fixtures/upgrade/current-manifest.yaml
  - tests/e2e/fixtures/upgrade/current-manifest-prime.yaml
  - hack/install-config.yaml.template

# Default internal rules refer https://github.com/get-woke/woke/blob/main/internal/rule/default.yaml
rules:
  - name: master
    terms:
      - master
    alternatives:
      - leader
      - primary
    options:
      word_boundary: true

```

### File: .wordlist-en-custom.txt
```txt
AES
API's
APIGroup
APIs
ARMv
AUR
AZ
AZs
AdditionalCommandArgs
AdditionalPodAffinity
AdditionalPodAntiAffinity
AffinityConfiguration
AllNamespaces
AntiAffinity
AppArmor
AppArmorProfile
Armando
AuthQuery
AuthQuerySecret
Autoscaler
AvailableArchitecture
AvailableArchitectures
AzureCredentials
AzurePVCUpdateEnabled
Azurite
BDR
BUSL
BackupCapabilities
BackupConfiguration
BackupFrom
BackupLabelFile
BackupList
BackupMethod
BackupMethodBarmanObjectStore
BackupMethodPlugin
BackupMethodVolumeSnapshot
BackupPhase
BackupPluginConfiguration
BackupSnapshotElementStatus
BackupSnapshotStatus
BackupSource
BackupSpec
BackupStatus
BackupTarget
BarmanCredentials
BarmanObjectStoreConfiguration
Bartolini
Battiato
BootstrapConfiguration
BootstrapInitDB
BootstrapPgBaseBackup
BootstrapRecovery
Buildx
Burstable
ByStatus
CAs
CIDR
CIS
CKA
CN
CNCF
CONFIG
CONTAINERNAME
CR's
CRD
CRDs
CSI
CSV
CSVs
CVE
CVEs
CannotReconcile
Canovai
CatalogImage
CatalogImages
Cecchi
Ceph
CertificatesConfiguration
CertificatesStatus
Certmanager
CiliumNetworkPolicy
ClassName
ClientCASecret
ClientTLSSecret
CloudNativePG
CloudNativePG's
ClusterCondition
ClusterConditionType
ClusterIP
ClusterImageCatalog
ClusterIsNotReady
ClusterList
ClusterMonitoringTLSConfiguration
ClusterRole
ClusterServiceVersion
ClusterSpec
ClusterStatus
CodeQL
ColumnName
ConditionStatus
ConfigMap
ConfigMapKeySelector
ConfigMapRefs
ConfigMapResourceVersion
ConfigMaps
ConnectionLimit
ContainerID
ContinuousArchiving
ContinuousArchivingFailing
Cron
CronJobs
CustomResourceDefinition
CustomResourceDefinitions
Customizations
DBA
DBaaS
DISA
DNS
DataBackupConfiguration
DataBase
DataDurabilityLevel
DataDurabilityLevelPreferred
DataDurabilityLevelRequired
DataSource
DatabaseObjectSpec
DatabaseObjectStatus
DatabaseReclaimDelete
DatabaseReclaimPolicy
DatabaseReclaimRetain
DatabaseRoleRef
DatabaseSpec
DatabaseStatus
DefaultAzureCredential
DemotionToken
DeploymentStrategy
DevOps
DevSecOps
DigitalOcean
DisablePassword
DisabledDefaultServices
DoD
DockerHub
Dockle
EBS
EDB
EKS
EOF
EOL
ESO
EdwinaZhu
EmbeddedObjectMetadata
EnablePDB
Endevir
EndpointCA
EnsureOption
EnterpriseDB
Enum
EnvFrom
EnvFromSource
EnvVar
EphemeralVolumeSource
EphemeralVolumesSizeLimit
EphemeralVolumesSizeLimitConfiguration
ExtensionConfiguration
ExtensionEnvVar
ExtensionSpec
ExtensionStatus
ExternalCluster
FDW
FDWSpec
FDWs
FQDN
FQDNs
FailoverQuorum
FailoverQuorumStatus
Fei
Filesystem
Fluentd
Francesco
GC
GCE
GCS
GID
GIS
GKE
GPL
GUC
GUCs
GabriFedi
Gabriele
GaugeVec
GeoSpatial
Gi
GitOps
GoArch
GoReleaser
Golang
GolangCI
GoogleCredentials
Grafana
GrantUsageSpecType
HH
HashiCorp
HistoryTags
Homebrew
Huß
IAM
INPLACE
IOPS
IPs
IPv
IRSA
IaC
Ibryam
IfNotPresent
ImageCatalog
ImageCatalogRef
ImageCatalogSpec
ImageInfo
ImageVolume
ImageVolumeSource
ImportSource
InfoSec
InstanceID
InstanceReportedState
IsolationCheckConfiguration
Isovalent
Istio
Istio's
JSON
JefeDavis
Joda
KV
Karpenter
KinD
Krew
KubeCon
Kubegres
KubernetesClusterDomain
LDAP
LDAPBindAsAuth
LDAPBindSearchAuth
LDAPConfig
LDAPScheme
LF
LFX
LLC
LPV
LSN
LTS
LastBackupFailed
LastBackupSucceeded
LastFailedArchiveTime
LastPromotionToken
Lifecycle
Linkerd
Linode
ListMeta
Liveness
LivenessProbeTimeout
LoadBalancer
LocalObjectReference
MAPPEDMETRIC
MVCC
ManagedConfiguration
ManagedRoles
ManagedRolesStatus
ManagedService
ManagedServices
MaxItems
MaxLength
MetricDescription
MetricName
MetricType
MiB
MicroserviceSnapshotType
Milsted
MinIO
MinItems
MinLength
Minikube
MonitoringConfiguration
MonolithSnapshotType
MultiNamespace
NFS
NGINX
NOBYPASSRLS
NOCREATEDB
NOCREATEROLE
NOSUPERUSER
Namespaces
Nenciarini
NetworkPolicies
NetworkPolicy
NodeAffinity
NodeMaintenanceWindow
NodeSelector
NodesUsed
O'Reilly
OCI
OLAP
OLTP
OOM
OSPS
OU
ObjectMeta
OnlineConfiguration
OnlineUpdateEnabled
OnlineUpgrading
OpenBao
OpenID
OpenSSF
OpenSSL
OpenShift
Openshift
OperatorCapabilities
OperatorHub
OptionSpec
OwnNamespace
PDB
PDBs
PGAudit
PGDATA
PGDG
PGData
PGDataImageInfo
PGSQL
PKI
PODNAME
PPROF
PV
PVCs
PascalBourdier
PasswordState
PasswordStatus
Patroni
Percona
PersistentVolumeClaim
PersistentVolumeClaimSpec
PgBouncer's
PgBouncerIntegrationStatus
PgBouncerPoolMode
PgBouncerSecrets
PgBouncerSpec
Philippe
PluginStatus
PoLA
PodAffinity
PodAntiAffinity
PodAntiAffinityType
PodDisruptionBudget
PodDisruptionBudgets
PodMonitor
PodName
PodSecurityContext
PodSelectorRef
PodSelectorRefStatus
PodSelectorRefs
PodSpec
PodStatus
PodTemplateSpec
PodTemplates
PodTopology
PodTopologyLabels
Pooler
Pooler's
PoolerIntegrations
PoolerList
PoolerMonitoringConfiguration
PoolerSecrets
PoolerSpec
PoolerStatus
PoolerType
PostGIS
PostInitApplicationSQLRefs
PostInitSQLRefs
PostInitTemplateSQLRefs
Postgres
PostgresConfiguration
PrimaryUpdateMethod
PrimaryUpdateMethodRestart
PrimaryUpdateMethodSwitchover
PrimaryUpdateStrategy
PrimaryUpdateStrategySupervised
PrimaryUpdateStrategyUnsupervised
PriorityClass
PriorityClassName
Probe
ProbeStrategyPgIsReady
ProbeStrategyQuery
ProbeStrategyStreaming
ProbeStrategyType
ProbeTerminationGracePeriod
ProbeWithStrategy
ProbesConfiguration
ProjectedVolumeSource
Promotable
PublicationReclaimDelete
PublicationReclaimPolicy
PublicationReclaimRetain
PublicationSpec
PublicationStatus
PublicationTarget
PublicationTargetAllTables
PublicationTargetObject
PublicationTargetTable
PullPolicy
PushSecret
QoS
QuickStart
RBAC
README
RHSA
RLS
RPO
RTO
RUNTIME
ReadWriteOnce
RedHat
RelabelConfig
ReplicaClusterConfiguration
ReplicaSet
ReplicationSlotsConfiguration
ReplicationSlotsHAConfiguration
ReplicationTLSSecret
ResizingPVC
ResourceRequirements
ResourceVersion
RestoreJobHook
RestoreJobHookCapabilities
RetentionPolicy
RevokeUsageSpecType
RoleBinding
RoleConfiguration
RoleStatus
RoleStatusNotManaged
RoleStatusPendingReconciliation
RoleStatusReconciled
RoleStatusReserved
RuntimeDefault
Ruocco
SANs
SAS
SBOM
SBOMs
SCC
SDK
SELinux
SHA
SLA
SLSA
SPDX
SPoF
SQLQuery
SQLRefs
SSL
SSZ
STORAGEACCOUNTNAME
Scaleway
ScheduledBackup
ScheduledBackupList
ScheduledBackupSpec
ScheduledBackupStatus
ScheduledBackups
SchemaSpec
Scorsolini
Seccomp
SeccompProfile
SecretKeySelector
SecretRefs
SecretStore
SecretVersion
SecretsResourceVersion
SecurityContextConstraints
Seealso
SelectorType
ServerCASecret
ServerSpec
ServerTLSSecret
ServiceAccount
ServiceAccountTemplate
ServiceMonitor
ServiceSelectorType
ServiceSelectorTypeR
ServiceSelectorTypeRO
ServiceSelectorTypeRW
ServiceSpec
ServiceTemplateSpec
ServiceUpdateStrategy
SetStatusInCluster
SingleNamespace
Slonik
SnapshotOwnerReference
SnapshotOwnerReferenceBackup
SnapshotOwnerReferenceCluster
SnapshotOwnerReferenceNone
SnapshotType
Snapshotting
Snyk
Stackgres
StandbyNames
StandbyNumber
StartupProbe
StatefulSets
StorageClass
StorageConfiguration
Storages
SubscriptionReclaimDelete
SubscriptionReclaimPolicy
SubscriptionReclaimRetain
SubscriptionSpec
SubscriptionStatus
SuccessfullyExtracted
SuperUserSecret
SwitchReplicaClusterStatus
SyncReplicaElectionConstraints
SynchronizeReplicas
SynchronizeReplicasConfiguration
SynchronousReplicaConfiguration
SynchronousReplicaConfigurationMethod
SystemID
TCP
TLS
TLSv
TOC
TODO
TablespaceClassName
TablespaceConfiguration
TablespaceMapFile
TablespaceName
TablespaceState
TablespaceStatus
TablespaceStatusPendingReconciliation
TablespaceStatusReconciled
Tablespaces
TemporaryData
TimelineId
TopologyKey
TopologySpreadConstraint
TopologySpreadConstraints
TypedLocalObjectReference
UI
UID
URIs
UTF
Uncomment
Unrealizable
UpdateStrategy
UsageSpec
UsageSpecType
VLDB
VLDBs
VM
VMs
VOLNAME
ValidationError
VirtualBox
VolumeSnapshot
VolumeSnapshotClass
VolumeSnapshotConfiguration
VolumeSnapshots
WAL
WALArchiver
WALBackupConfiguration
WALCapabilities
WALs
WalBackupConfiguration
WalClassName
Wallner
XXu
YXBw
YY
YYYY
Ying
Zalando
Zhu
Zstandard
abd
accessKeyId
accessModes
adc
additionalCommandArgs
additionalPodAffinity
additionalPodAntiAffinity
addons
affinityconfiguration
aks
albert
alex
allTables
allnamespaces
alloc
allocator
allowConnections
allowPrivilegeEscalation
allowVolumeExpansion
alm
amd
angus
anonymization
api
apiGroup
apiGroups
apiVersion
apidoc
apimachinery
apis
apiserver
apiservicedefinitions
apparmor
appdb
applicationCredentials
applicationSecretVersion
appsv
appuser
archiveAdditionalCommandArgs
archiver
args
armru
async
auth
authQuery
authQuerySecret
authn
authz
autocompletion
autoscaler
autovacuum
availableArchitectures
availablearchitecture
aws
az
azureCredentials
azurePVCUpdateEnabled
azurite
ba
backend
backends
backoff
backport
backported
backporting
backupCapabilities
backupID
backupId
backupLabelFile
backupName
backupOwnerReference
backupRetentionPolicy
backupconfiguration
backuplist
backupmethod
backupphase
backuppluginconfiguration
backupsnapshotelementstatus
backupsnapshotstatus
backupsource
backupspec
backupstatus
backuptarget
balancer
balancers
barmanEndpointCA
barmanObjectStore
barmancloud
barmanobjectstore
barmanobjectstoreconfiguration
baseDN
basebackup
bb
bdr
beginLSN
beginWal
benchmarked
benchmarking
bindAsAuth
bindDN
bindPassword
bindSearchAuth
bitmask
bool
booleanSwitch
bootstrapconfiguration
bootstrapinitdb
bootstrappgbasebackup
bootstraprecovery
bozkayasalihx
br
bs
builtinLocale
bw
byStatus
bypassrls
bzip
cGFzc
caSecretVersion
cannotReconcile
catalogName
catalogimage
cb
cd
ce
certificatesconfiguration
certificatesstatus
cgroup
cheatsheet
checksums
chmod
ciclops
cisecurity
claimRef
className
classid
cleartext
cli
clientCA
clientCASecret
clientCaSecretVersion
clientTLS
clientTLSSecret
cloudNativePGCommitHash
cloudNativePGOperatorHash
cloudnative
cloudnativepg
clusterBackup
clusterName
clusterimagecatalog
clusterimagecatalogs
clusterlist
clustermonitoringtlsconfiguration
clusterrole
clusterserviceversions
clusterspec
clusterstatus
cmd
cn
cnp
cnpg
codebase
collationVersion
columnValue
commandError
commandOutput
conf
config
config's
configMap
configMapRefs
configMapResourceVersion
configmap
configmapkeyselector
configmapresourceversion
configmaps
configs
configurability
conn
connectionLimit
connectionParameters
connectionString
connectionTimeout
conninfo
containerImage
containerPort
controldata
coredump
coreos
corev
cp
cpu
crds
createdAt
createdb
createrole
createuser
creationTimestamp
creds
cron
crt
cryptographic
cryptographically
csvlog
csvs
ctl
ctype
curlimages
currentPrimary
currentPrimaryFailingSinceTimestamp
currentPrimaryTimestamp
customQueriesConfigMap
customQueriesSecret
customizable
customresourcedefinitions
cutover
cyber
dT
danglingPVC
dataChecksums
dataDurability
databackupconfiguration
databaseReclaimPolicy
databaseobjectspec
databaseobjectstatus
databasereclaimpolicy
databaseroleref
databasespec
databasestatus
datacenter
datadurabilitylevel
datallowconn
datasource
datistemplate
datname
dbe
dbname
ddf
ddl
de
declaratively
defaultMode
demotionToken
deploymentStrategy
dereference
destinationPath
dev
devel
devsecops
digestValue
dir
disableDefaultQueries
disablePassword
disabledDefaultServices
discoverable
displayName
distro
distroless
distros
dl
dn
dns
dockle
dod
downtimes
dvcmQ
dwm
dx
eBPF
ecdsa
edb
eks
embeddedobjectmetadata
enableAlterSystem
enableInstancePprof
enablePDB
enablePodAntiAffinity
enablePodMonitor
enableSuperuserAccess
endLSN
endWal
endpointCA
endpointURL
ensureoption
enterprisedb
env
envFrom
ephemeralVolumeSource
ephemeralVolumesSizeLimit
ephemeralvolumessizelimitconfiguration
ermakov
eu
excludePatterns
executables
expirations
extName
extensibility
extensionconfiguration
extensionenvvar
extensionspec
externalCluster
externalClusterName
externalClusterSecretVersion
externalClusters
externalcluster
externalclusters
facto
failover
failoverDelay
failoverQuorum
failoverquorum
failoverquorums
failoverquorumstatus
failovers
failureThreshold
faq
fastpath
fb
fd
fdw
fdws
fdwspec
fieldPath
fieldref
filesystem
finalizer
finalizers
findstr
fio
fips
firstRecoverabilityPoint
firstRecoverabilityPointByMethod
fqdn
freddie
fuzzystrmatch
gRPC
gapped
gc
gcc
gce
gcp
gcs
gcsCredentials
geocoder
ghcr
github
gkeEnvironment
gmail
goArch
golangci
goodwithtech
googleCredentials
goroutines
gosec
govulncheck
grafana
gzip
hanshal
hardcoded
hashicorp
hba
hdr
healthyPVC
healthz
highAvailability
historyTags
hostPort
hostname
hostssl
href
html
http
httpGet
https
hu
hugepages
icu
icuLocale
icuRules
ident
imageCatalogRef
imageName
imagePullPolicy
imagePullSecrets
imageVolume
imagecatalog
imagecatalogref
imagecatalogs
imagecatalogspec
imageinfo
imagevolume
img
immediateCheckpoint
impactful
importsource
inProgress
inRoles
indistinctively
inheritFromAzureAD
inheritFromIAMRole
inheritedMetadata
init
initDB
initdb
initialDelaySeconds
initializingPVC
inplace
installModes
installplans
instanceID
instanceName
instanceNames
instanceRole
instanceid
instancereportedstate
instancesReportedState
instancesStatus
inuse
io
ip
ipcs
ips
isPrimary
isTemplate
isWALArchiver
isolationCheck
isolationcheckconfiguration
isready
issuecomment
italy
jdbc
jmealo
jobCount
jq
json
jsonpath
juliamertz
kb
kbytes
keepalive
kms
kube
kubebuilder
kubectl
kubelet
kubernetes
kubernetesClusterDomain
labelColumnName
labelColumnValue
labelName
labelSelector
labelValue
labelling
largeobject
lastCheckTime
lastFailedBackup
lastPromotionToken
lastScheduleTime
lastSuccessfulBackup
lastSuccessfulBackupByMethod
latestGeneratedNode
lc
ld
ldap
ldapBindPassword
ldapbindasauth
ldapbindsearchauth
ldapconfig
ldaps
ldapscheme
le
leonardoce
li
libpq
lifecycle
lifecycles
linodeobjects
linter
linters
linux
listmeta
liveness
livenessProbe
livenessProbeTimeout
livenessprobe
lm
loadBalancerSourceRanges
localeCType
localeCollate
localeProvider
localhost
localobjectreference
locktype
logLevel
lookups
lsn
lt
lz
mTLS
macOS
majorVersion
majorVersionUpgradeFromImage
malcolm
mallocs
managedRoleSecretVersion
managedRolesStatus
managedconfiguration
managedroles
managedservice
managedservices
matchExpressions
matchLabels
mateusoliveira
maxClientConnections
maxParallel
maxStandbyNamesFromCluster
maxSyncReplicas
maximumLag
maxwait
mcache
md
mediatype
mem
memstats
metav
metric's
metricsQueriesTTL
microservice
microservices
microsoft
minApplyDelay
minKubeVersion
minSyncReplicas
minikube
minio
misconfigurations
mmap
monitoringconfiguration
mountPath
msg
mspan
multinamespace
mutatingwebhookconfigurations
mutex
namespace
namespaced
namespaces
natively
ndQuadrant
networkpolicy
nextScheduleTime
nginx
nodeAffinity
nodeLabelsAntiAffinity
nodeMaintenanceWindow
nodeSelector
nodeToClusters
nodemaintenancewindow
nodesUsed
nodev
noexec
nosuid
ntt
num
oauth
objectmeta
objectstore
objectstores
objid
objref
objsubid
observability
observedGeneration
oc
ol
oleg
olm
onlineConfiguration
onlineUpdateEnabled
onlineconfiguration
openldap
openshift
operability
operativity
operatorCapabilities
operatorframework
operatorhub
optionspec
ou
overridable
ownerMetadata
ownerReference
parseable
paru
passfile
passwd
passwordSecret
passwordStatus
passwordstate
pc
pchovelon
pdf
periodSeconds
persistentVolumeClaims
persistentvolumeclaim
persistentvolumeclaims
pgAdmin
pgBouncer
pgBouncerIntegration
pgBouncerSecrets
pgDataImageInfo
pgDumpExtraOptions
pgRestoreDataOptions
pgRestoreExtraOptions
pgRestor
... [TRUNCATED]
```

### File: ADOPTERS.md
```md
# Adopters

Below is a list of organizations and users who have publicly shared that
they’re using PostgreSQL in Kubernetes with the CloudNativePG operator in a
production environment.

The purpose of this list is to inspire others to join the movement and help
grow our open-source community and project.

Adding your organization takes just 5 minutes of your time, but it means a lot
to us!

## How to Add Your Organization

You can add your organization to this list in two ways:

- [Open a pull request](https://github.com/cloudnative-pg/cloudnative-pg/pulls)
  to directly update this file.
- [Edit the file](https://github.com/cloudnative-pg/cloudnative-pg/blob/main/ADOPTERS.md)
  directly on GitHub.

Use the commit title: **"docs: add <ORGANIZATION_NAME> to `ADOPTERS.md`"** and
be sure to [sign off your work](contribute/README.md#sign-your-work).

If you need any assistance, feel free to ask in our Slack chat—we’re here to
help!

## CloudNativePG Adopters

This list is sorted in chronological order, based on the submission date.

| Organization | Contact | Date | Description of Use |
| ------------ | ------- | ---- | ------------------ |
| [EDB](https://enterprisedb.com) | @gbartolini | 2023-02-21 | EDB's DataBase as a Service solution, [BigAnimal](https://www.enterprisedb.com/products/biganimal-cloud-postgresql), relies on CloudNativePG to run PostgreSQL and Postgres Distributed workloads. EDB is one of the primary contributors to the open source PostgreSQL project and the founder of CloudNativePG. |
| [Clustermarket](https://clustermarket.com/) | @itay-grudev | 2023-02-25 | Primary production database cluster. Clustermarket provides the easiest way to manage shared lab instrument scheduling and get all your team members' schedules aligned. |
| [Opencell](https://opencellsoft.com/) | @AntoineMicheaOpencell | 2023-02-27 | Opencell is an open source agile monetization platform that uses CloudNativePG to run PostgreSQL clusters for its SaaS. |
| [Clastix](https://clastix.io/) | @prometherion | 2023-03-14 | Used as an available [`DataStore` driver](https://kamaji.clastix.io/guides/postgresql-datastore/) for [Kamaji](https://github.com/clastix/kamaji) `TenantControlPlane` resources, also known as Kubernetes Control Planes running as regular pods in a management cluster to offer Kubernetes as a Service as a Cloud hyper-scaler. |
| [Tembo](https://tembo.io/) | @tembo-io | 2023-07-17 | Tembo is the developer platform for PostgreSQL extensions. Build and share extensions with [Trunk](https://pgt.dev), and use any extension on Tembo Cloud. |
| [CNDI](https://cndi.dev) | @johnstonmatt | 2023-08-21 | Provides simple workflow to deploy self-hosted CloudNativePG clusters with GitOps and Infrastructure as Code. |
| [PITS Global Data Recovery Services](https://www.pitsdatarecovery.net/) | @benjx1990 | 2023-09-07 | CloudNativePG is  used to easily manage highly-loaded database clusters |
| [OptimaData](https://www.optimadata.nl) | @edco-wallet | 2023-09-25 | OptimaData as the Dutch database expert company has done several projects running CloudNativePG for managing Postgres clusters. Read our [how to run Postgres on Kubernetes blogpost](https://www.optimadata.nl/blogs/3/k9pv6z-how-to-postgres-on-kubernetes%2C-part-2) to learn more and how easy you can deploy with CloudNativePG. |
| [Enix](https://enix.io) | @rdegez | 2023-10-06 | Enix is a French Managed Services Provider specializing in the operation of Kubernetes clusters across all types of infrastructure (VMs and bare-metal on both public and private clouds). Our customer platforms often require PostgreSQL databases, and we are pleased to use CloudNativePG to install & manage them. |
| [WienIT](https://wienit.at) | @smiyc | 2023-10-11 |Hello 👋 We are WienIT, the central IT & business partner of [Wiener Stadtwerke Group](https://wienerstadtwerke.at). As IT service provider we´re using CloudNativePG to provide high available PostgreSQL clusters. |
| [Shinkansen](https://shinkansen.finance) | @utaladriz, @afiebig | 2023-11-16 | Primary production high available PostgreSQL cluster, ISO27001 Backup and Recovery Compliance |
| [Ænix](https://aenix.io) | @kvaps | 2024-02-11 | Ænix provides consulting services for cloud providers and uses CloudNativePG in free PaaS platform [Cozystack](https://cozystack.io) for running PostgreSQL-as-a-Service. |
| [IBM](https://www.ibm.com) | @pgodowski | 2024-02-20 | IBM uses CloudNativePG as the embedded SQL database within the family of [IBM Cloud Pak](https://www.ibm.com/cloud-paks) products, running as customer-managed software on top of [OpenShift Container Platform](https://www.redhat.com/en/technologies/cloud-computing/openshift/container-platform). |
| [Google Cloud](https://cloud.google.com/) | @mastersingh24 | 2024-03-12 | Leverage the full potential of cutting-edge PostgreSQL  and CloudNativePG  on [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine) with EDB Community 360 PostgreSQL available in the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/public-edb-ppas/edb-postgresql). |
| [Syself](https://syself.com) | @batistein | 2024-05-06 | Syself offers a simplified, multi-cloud Managed Kubernetes platform based on Cluster API and uses CloudNativePG for managing Postgres clusters in our internal infrastructure. |
| [ParadeDB](https://paradedb.com) | @philippemnoel | 2024-07-10 | ParadeDB is an Elasticsearch alternative on Postgres. It leverages CloudNativePG to manage ParadeDB Postgres clusters which connect to a customer's existing Postgres infrastructure via logical (streaming) replication. |
| [REWE International AG](https://rewe-group.at/en) | @rewemkris | 2024-08-21 |Hello! 👋 We are the DBMS Team of RIAG IT, responsible for managing databases worldwide for our stores, warehouses, and online shops. We leverage CloudNativePG to provide PostgreSQL as a Service, creating highly available databases running on Kubernetes in both Google Cloud and on-premises environments.|
| [Microsoft Azure](https://azure.microsoft.com/en-us/) | @KenKilty | 2024-08-22 | Learn how to [deploy](https://learn.microsoft.com/azure/aks/postgresql-ha-overview) PostgreSQL on [Azure Kubernetes Services (AKS)](https://learn.microsoft.com/azure/aks/what-is-aks) with [EDB commercial support](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/enterprisedb-corp.edb-enterprise) and [EDB Postgres-as-a-Service](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/enterprisedb-corp.biganimal-prod-v1) offerings available in the [Azure Marketplace](https://azuremarketplace.microsoft.com/).|
| [PZU Group](https://www.pzu.pl) | @MichaluxPL | 2024-08-26 | PZU is one of the largest financial institutions in Poland and also the largest insurance company in Central and Eastern Europe. CloudNativePG is used as on-premise cloud solution/DBaaS to provide highly available PostgreSQL clusters.|
| [Telnyx](https://www.telnyx.com) | @aryklein | 2024-09-24 | Telnyx leverages PostgreSQL as its relational database for internal services, managing databases with high availability using CloudNativePG across multiple Kubernetes clusters in different sites, with distributed replica clusters to ensure data redundancy and resilience. |
| [Alpcot](https://alpcot.se) | @svenakela | 2024-09-24 | Alpcot uses CloudNativePG for both public-facing and internal applications deployed in the cloud and in-house Kubernetes. |
| [GEICO Tech](https://www.geico.com/tech/) | @ardentperf | 2024-09-24 | GEICO Tech is building the most consumer-centric insurance offerings in America. CloudNativePG is used to provide a highly available Kubernetes-based Postgres service, both in the cloud and on-premises. |
| [Cambium](https://www.cambium.earth) | @Mmoncadaisla | 2024-09-25 | Cambium leverages CloudNativePG at its core to analyze and visualize geospatial data for carbon market applications, ranging from site selection to monitoring, reporting, and verification. |
| [MIND Informatica srl](https://mind-informatica.com) | @simonerocchi | 2024-09-25 | We use CloudNativePG to run PostgreSQL clusters for our web applications. |
| [Walkbase](https://walkbase.com/) | @LinAnt | 2024-10-24 | CloudNativePG currently manages all our Postgres instances on Kubernetes via GitOps. |
| [Akamai Technologies](https://www.akamai.com/) | @srodenhuis | 2024-11-20 | CloudNativePG is used in the [Akamai App PLatform](https://github.com/linode/apl-core) for all platform managed PostgreSQL databases. |
| [Novo Nordisk](https://www.novonordisk.com/) | [scni@novonordisk.com](mailto:scni@novonordisk.com) ([@CasperGN](https://github.com/CasperGN)) | 2024-11-20 | Backing of Grafana UI states for central Observability platform and datastore for our Developer Portal based off Backstage. |
| [Docaposte](https://docaposte.fr) | @albundy83 | 2024-11-20 | Docaposte is the digital trust leader in France. We use CloudNativePG because it is the most elegant and efficient solution for running PostgreSQL in production. |
| [Obmondo](https://obmondo.com) | @Obmondo | 2024-11-25 | At Obmondo we use CloudNativePG in our open-source Kubernetes meta-management platform called [KubeAid](https://kubeaid.io/) to easily manage all PostgreSQL databases across clusters from a centralized interface. |
| [Mirakl](https://www.mirakl.com/) | @ThomasBoussekey | 2025-02-03 | CloudNativePG is our default hosting solution for marketplace instances. With over 300 CloudNativePG clusters managing 8 TB of data, we have developed highly customizable Helm charts that support connection pooling, logical replication, and many other advanced features.  |
| [Bitnami](https://bitnami.com) | [@carrodher](https://github.com/carrodher) | 2025-03-04 | Bitnami provides CloudNativePG as part of its open-source [Helm charts catalog](https://github.com/bitnami/charts), enabling users to easily deploy PostgreSQL clusters on Kubernetes. Additionally, CloudNativePG is available through [Tanzu Application Catalog](https://www.vmware.com/products/app-platform/tanzu-application-catalog) and [Bitnami Premium](https://www.arrow.com/globalecs/na/vendors/bitnami-premium/), where customers can benefit from advanced security and compliance features such as VEX, SBOM, SLSA3, and CVE scanning. |
| [Giant Swarm](https://www.giantswarm.io/) | [@stone-z](https://github.com/stone-z) | 2025-05-02 | Giant Swarm's full-service Kubernetes security and observability platforms are powered by PostgreSQL clusters delightfully managed with CloudNativePG. |
| [DocumentDB Operator](https://github.com/microsoft/documentdb-kubernetes-operator) | [@xgerman](https://github.com/xgerman) | 2025-05-22 | The DocumentDB Kubernetes Operator is an open-source project to run and manage DocumentDB on Kubernetes. [DocumentDB](https://github.com/microsoft/documentdb) is the engine powering vCore-based [Azure Cosmos DB for MongoDB](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore/). The operator uses CloudNativePG behind the scenes. |   
| [Xata](https://xata.io) | [@tsg](https://github.com/tsg) | 2025-05-29 | Xata is a PostgreSQL platform offering instant database branching, separation of storage/compute, and PII anonymization. It uses CloudNativePG for the compute part. |
| [Vera Rubin Observatory](https://www.lsst.org) | [@cbarria](https://github.com/cbarria) | 2025-06-17 | At the heart of our operations, CloudNativePG supports the telescope's systems and plays a key role in making astronomical data openly accessible to the world. |
| [Brella](https://www.brella.io) | [@vitobotta](https://github.com/vitobotta/) | 2025-08-11 | Brella is an event management platform that works in new and smart ways. Postgres is at the core of how our platform is built. With CloudNativePG, we moved from using a managed Postgres service - Cloud SQL on Google Cloud - to running Postgres clusters directly in Kubernetes. This change saves us money and gives us more control. At the same time, we didn't lose any functionality.|
| [Linux Polska](https://linuxpolska.com) | [@maaciekk](https://github.com/maaciekk) | 2025-08-11 | CloudNativePG is our gold standard for providing highly available databases in a Kubernetes environment, powering mission-critical applications across various industries like healthcare and finance. Independent rebuilds of CloudNativePG images are also part of our SourceMation stack. |
| [TrueFullstaq](https://truefullstaq.com/)                                          | [@leppek](https://github.com/leppek)                                                           | 2025-09-30 | As a leading cloud native consultancy, TrueFullStaq designs, builds, and manages scalable and secure custom infrastructure for our clients. We have adopted CloudNativePG as a foundational component of our managed PostgreSQL offerings, leveraging its Kubernetes-native approach, declarative management, and high-availability features to deliver robust and easily maintainable database environments. By building on CloudNativePG, we ensure that our customers benefit from a declarative, production-ready foundation for their data-driven cloud native journey. |
| [Sophotech](https://sopho.tech) | [@archy-rock3t-cloud](https://github.com/archy-rock3t-cloud) | 2025-10-09 | We help companies run mission-critical systems on Kubernetes, and CloudNativePG is our go-to choice for PostgreSQL. It gives our clients battle-tested reliability, effortless scaling, and true cloud-native resilience. |
| [Serit Tromsø - Part of Binero](https://github.com/serit) | [@fredeil](https://github.com/fredeil) | 2025-10-20 | Serit Tromsø is a full-stack development and platform consultancy. We design, build, and operate enterprise applications on Kubernetes, both for ourselves and our clients, using a functional-first approach. Our CloudNativePG solution enables us to implement best practices for managing PostgreSQL in Kubernetes without sacrificing performance or reliability.|
| [pgEdge](https://www.pgedge.com) | [@mmols](https://github.com/mmols) | 2025-11-12 | pgEdge uses CloudNativePG to help customers operate Postgres clusters on Kubernetes, powering both single-region and multi-region, active-active deployments with the open source [pgEdge Helm chart](https://github.com/pgEdge/pgedge-helm). Leveraging CloudNativePG’s mature, production-ready operator allows pgEdge to focus on distributed Postgres capabilities while building on a proven foundation for lifecycle management.|
| [Nutanix NKP](https://www.nutanix.com/products/kubernetes-management-platform) | @tuxtof | 2025-11-19 | Nutanix Kubernetes Platform (NKP) integrates CloudNativePG both for internal services like Harbor or Insight and to give end users a simple, self-service capability to deploy highly available PostgreSQL clusters. This provides enhanced reliability, scalability, and simplified database operations for both platform and users. |
| [GARR](https://www.garr.it) | [@rizlas](https://github.com/rizlas) | 2026-01-16 | GARR is the Italian Nati
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct

The Code of Conduct for the CloudNativePG Community can be found in the
[governance repository](https://github.com/cloudnative-pg/governance/blob/main/CODE_OF_CONDUCT.md).

```

### File: CONTRIBUTING.md
```md
# Contributing to CloudNativePG

Thank you for your interest in contributing! 💖

To ensure consistency across the project, all CloudNativePG repositories follow
a common set of guidelines regarding code of conduct, AI usage, and
contribution workflows.

Please review the [CloudNativePG Project contributing guidelines](https://github.com/cloudnative-pg/governance/blob/main/CONTRIBUTING.md)
before searching for issues, reporting bugs, or submitting a pull request.

---

For development contributions, please refer to the separate section called
["Contributing to the source code"](contribute/README.md).

```

### File: DEPENDENCIES.md
```md
# Dependency Management Policy

## Overview

CloudNativePG (CNPG) is committed to maintaining a secure and stable software
supply chain. As an operator managing critical database workloads, the
integrity of our dependencies, ranging from Go modules to container base
images, is paramount.

**This document outlines our policies for selecting, monitoring, and updating
third-party dependencies.**

## Selection Criteria

Before introducing a new dependency to the project, maintainers must evaluate
it against the following criteria:

- **Necessity:** Does the dependency provide essential functionality that
  cannot be reasonably implemented within the project?
- **Security Posture:** Preference is given to projects with high OpenSSF
  Scorecard ratings and a clear security policy.
- **Maintenance:** The dependency must be actively maintained with a history of
  timely security patches.
- **Licensing:** All dependencies must comply with the Apache License 2.0 or a
  compatible permissive license (e.g. MIT, BSD-3-Clause).

## Automated Monitoring and Scanning

We employ a "defense in depth" approach to monitoring our dependency tree
through automated tooling:

- **Update Automation:** GitHub's built-in
  [Dependabot](https://github.com/dependabot) alerts notify us of known
  vulnerabilities in our dependencies. We use
  [Renovate](https://github.com/renovatebot/renovate) for granular version
  management, automated grouping of updates, and maintenance of GitHub Actions.
- **Vulnerability Scanning:** Every Pull Request and push to the main branch
  triggers automated scans using [Snyk](https://snyk.io/) and
  [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) to identify
  known vulnerabilities (CVEs).
- **Static Analysis:** We rely on [CodeQL](https://codeql.github.com/) and
  [golangci-lint](https://github.com/golangci/golangci-lint) (which includes the
  [gosec](https://github.com/securego/gosec) security linter) to identify security
  risks introduced by the way dependencies are utilized in our code.
- **Container Hardening:** We run
  [Dockle](https://github.com/goodwithtech/dockle) to lint our container images
  against security best practices, ensuring that our images are lean, do not run
  as `root`, and do not contain sensitive information in their history.

## Supply Chain Integrity

To ensure that the code we build is the code we intended to use, we implement
the following:

- **Checksum Verification:** We use [`go.sum`](./go.sum) to ensure the
  integrity of Go modules.
- **Artifact Signing:** All container images are cryptographically signed using
  [Cosign](https://github.com/sigstore/cosign).
- **SLSA Provenance:** We generate SLSA-formatted provenance attestations for
  all releases. These are delivered as OCI attestations integrated into our
  build process via BuildKit (`buildType: https://mobyproject.org/buildkit@v1`).
- **Software Bill of Materials (SBOM):** We provide a comprehensive SBOM for
  every image, allowing users to verify the entire bill of materials for any
  given version.

## Remediation Cadence

Security updates are treated as high-priority tasks. The project aims for the
following remediation timeframes:

- **Critical and High Vulnerabilities:** Once a fix is available in the
  upstream dependency, we aim to merge the update and initiate a release
  process within one week.
- **Medium and Low Vulnerabilities:** These updates are typically batched and
  addressed as part of our regular maintenance and release cycles once upstream
  fixes are provided.

## Contact

For security-related concerns regarding our dependencies, please refer to our
[`SECURITY.md` file](./SECURITY.md).

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
