---
id: github.com-n8n-io-n8n-hosting-de91ffa4-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:01.630967
---

# KNOWLEDGE EXTRACT: github.com_n8n-io_n8n-hosting_de91ffa4
> **Extracted on:** 2026-04-01 15:32:14
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524576/github.com_n8n-io_n8n-hosting_de91ffa4

---

## File: `.releaserc.json`
```json
{
  "branches": ["main"],
  "plugins": [
    ["@semantic-release/commit-analyzer", {
      "preset": "conventionalcommits",
      "releaseRules": [
        { "type": "feat", "release": "minor" },
        { "type": "fix", "release": "patch" },
        { "type": "perf", "release": "patch" },
        { "type": "revert", "release": "patch" },
        { "type": "docs", "release": "patch" },
        { "type": "refactor", "release": "patch" },
        { "scope": "no-release", "release": false }
      ]
    }],
    ["@semantic-release/release-notes-generator", {
      "preset": "conventionalcommits"
    }],
    "@semantic-release/changelog",
    ["@semantic-release/exec", {
      "prepareCmd": "python3 -c \"import re; content=open('charts/n8n/Chart.yaml').read(); open('charts/n8n/Chart.yaml','w').write(re.sub(r'^version:.*', 'version: ${nextRelease.version}', content, flags=re.MULTILINE))\""
    }],
    "@semantic-release/github"
  ]
}
```

## File: `CHANGELOG.md`
```markdown
## [1.3.0](https://github.com/n8n-io/n8n-hosting/compare/v1.2.0...v1.3.0) (2026-03-25)

### Features

* **chart:** support independent service annotations for main and webhook-processor ([#100](https://github.com/n8n-io/n8n-hosting/issues/100)) ([41b6345](https://github.com/n8n-io/n8n-hosting/commit/41b634523788c3fe633ab086964081e687be0169))

## [1.0.3](https://github.com/n8n-io/n8n-hosting/compare/v1.0.2...v1.0.3) (2026-03-04)

### Bug Fixes

* **ci:** add concurrency control to release workflow ([#78](https://github.com/n8n-io/n8n-hosting/issues/78)) ([e00e3b2](https://github.com/n8n-io/n8n-hosting/commit/e00e3b2b3f8485d6843198a1142175fe72b69917))

## [1.0.2](https://github.com/n8n-io/n8n-hosting/compare/v1.0.1...v1.0.2) (2026-02-25)

### Features

* **chart:** bump n8n to 2.9.2 ([#76](https://github.com/n8n-io/n8n-hosting/issues/76))

### Bug Fixes

* **ci:** remove non-existent 'automated' label from bump workflow ([#75](https://github.com/n8n-io/n8n-hosting/issues/75)) ([ce882f0](https://github.com/n8n-io/n8n-hosting/commit/ce882f093665f77be8df724e979ab4b2d159300b))

# Changelog

All notable changes to the n8n Helm chart will be documented in this file.

This file is automatically managed by [semantic-release](https://github.com/semantic-release/semantic-release).
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to n8n Hosting

## Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/) for automated versioning. Your commit messages must follow this format:

```
<type>(<scope>): <description>

[optional body]
```

Types:
- `feat` -- new feature (triggers minor version bump)
- `fix` -- bug fix (triggers patch version bump)
- `docs` -- documentation changes
- `refactor` -- code refactoring
- `perf` -- performance improvements
- `chore(no-release)` -- no version bump

Examples:
```
feat(chart): add webhook processor ingress support
fix(worker): add missing extraEnvFrom to worker deployment
docs: update README with OCI install instructions
```

## Chart Development

### Prerequisites

- [Helm](https://helm.sh/docs/intro/install/) 3.12+
- [chart-testing (ct)](https://github.com/helm/chart-testing) for linting

### Local Linting

```bash
helm lint charts/n8n
ct lint --charts charts/n8n --validate-maintainers=false
```

### Template Validation

Render all templates to check for syntax errors and inspect the generated YAML:

```bash
# Render with minimal values
helm template test charts/n8n -f charts/n8n/examples/minimal.yaml

# Render with all features enabled
helm template test charts/n8n -f charts/n8n/examples/production-s3.yaml

# Save output for inspection
helm template test charts/n8n -f charts/n8n/examples/minimal.yaml > /tmp/rendered.yaml
```

### Local Install Test

**Prerequisites:** A local Kubernetes environment with Docker support. Any of these work:
- [OrbStack](https://orbstack.dev/) (recommended for macOS — lightweight, has built-in Kubernetes)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Kubernetes enabled
- [kind](https://kind.sigs.k8s.io/) (Kubernetes-in-Docker — requires Docker)

If using kind, create a cluster first: `kind create cluster --name n8n-test`

#### Option A: Standalone mode (quickest — no external dependencies)

This deploys a single n8n pod with SQLite. No PostgreSQL or Redis needed.

```bash
# Create namespace and secrets
kubectl create namespace n8n-test
kubectl create secret generic n8n-secrets -n n8n-test \
  --from-literal=N8N_ENCRYPTION_KEY=$(openssl rand -hex 32) \
  --from-literal=N8N_HOST=localhost \
  --from-literal=N8N_PORT=5678 \
  --from-literal=N8N_PROTOCOL=http

# Install with standalone example
helm install n8n charts/n8n -n n8n-test \
  -f charts/n8n/examples/standalone.yaml

# Wait for the pod to be ready
kubectl wait --for=condition=ready pod -l app.kubernetes.io/component=main -n n8n-test --timeout=120s

# Access the UI (keep running, Ctrl+C to stop)
kubectl port-forward svc/n8n-main -n n8n-test 5678:5678
```

Open **http://localhost:5678** in your browser.

**Clean up:**

```bash
helm uninstall n8n -n n8n-test
kubectl delete namespace n8n-test
```

#### Option B: Queue mode (full deployment with PostgreSQL + Redis)

This deploys the chart with external PostgreSQL and Redis, plus worker pods — closer to a production setup.

##### 1. Deploy dependencies

```bash
# Create a test namespace
kubectl create namespace n8n-test

# Add the Bitnami Helm repo
helm repo add bitnami https://charts.bitnami.com/bitnami

# Deploy PostgreSQL and Redis
helm install postgres bitnami/postgresql -n n8n-test \
  --set auth.postgresPassword=postgres \
  --set auth.database=n8n
helm install redis bitnami/redis -n n8n-test \
  --set auth.password=redis \
  --set architecture=standalone

# Wait for databases to be ready
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=postgresql -n n8n-test --timeout=120s
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=redis -n n8n-test --timeout=120s
```

##### 2. Create secrets and install the chart

```bash
# Create the required n8n secrets
kubectl create secret generic n8n-secrets -n n8n-test \
  --from-literal=N8N_ENCRYPTION_KEY=$(openssl rand -hex 32) \
  --from-literal=N8N_HOST=localhost \
  --from-literal=N8N_PORT=5678 \
  --from-literal=N8N_PROTOCOL=http

# Install the chart
helm install n8n charts/n8n -n n8n-test \
  --set database.host=postgres-postgresql \
  --set database.user=postgres \
  --set database.passwordSecret.name=postgres-postgresql \
  --set database.passwordSecret.key=postgres-password \
  --set redis.host=redis-master \
  --set redis.passwordSecret.name=redis \
  --set redis.passwordSecret.key=redis-password \
  --set secretRefs.existingSecret=n8n-secrets

# Watch pods come up (Ctrl+C when all show Running/Ready)
kubectl get pods -n n8n-test -w
```

##### 3. Access the UI

The n8n service uses `ClusterIP` by default, so it's only reachable from inside the cluster. Use port-forwarding to access it from your browser:

```bash
kubectl port-forward svc/n8n-main -n n8n-test 5678:5678
```

Then open **http://localhost:5678**. Keep the port-forward running — it will stop when you Ctrl+C.

##### 4. Clean up

```bash
helm uninstall n8n -n n8n-test
helm uninstall redis -n n8n-test
helm uninstall postgres -n n8n-test
kubectl delete namespace n8n-test

# If using kind:
kind delete cluster --name n8n-test
```

You can also let CI do this for you — add the `test-install` label to your PR and the install-test job will run automatically.

### Version Bumps

**Do not manually edit `Chart.yaml` version.** Semantic-release bumps it automatically based on commit messages.

## Pull Requests

- Add the `test-install` label to PRs that change chart templates to trigger a full install test on a kind cluster
- All PRs must pass lint and template validation checks
```

## File: `README.md`
```markdown
# n8n Hosting

Official hosting configurations for [n8n](https://n8n.io) -- the workflow automation platform.

## Kubernetes (Helm Chart)

The official n8n Helm chart for production Kubernetes deployments.

```bash
helm install n8n oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.0 -f my-values.yaml
```

See the [chart README](../../../README.md) for full documentation and the [examples](./charts/n8n/examples/) directory for common configurations.

## Docker Compose

| Directory | Description |
|---|---|
| [docker-compose/withPostgres](./docker-compose/withPostgres/) | n8n + PostgreSQL |
| [docker-compose/withPostgresAndWorker](./docker-compose/withPostgresAndWorker/) | n8n + PostgreSQL + Redis + worker (queue mode) |
| [docker-compose/subfolderWithSSL](./docker-compose/subfolderWithSSL/) | n8n behind SSL reverse proxy in subfolder |
| [docker-caddy](./docker-caddy/) | n8n with Caddy reverse proxy |

## Kubernetes (Raw Manifests)

See [`kubernetes/`](./kubernetes/) for raw Kubernetes manifest examples used in cloud provider tutorials (AWS, Azure, GCP).

## Documentation

- [n8n docs](https://docs.n8n.io/)
- [Self-hosting guides](https://docs.n8n.io/hosting/)
- [Community forum](https://community.n8n.io/)
```

## File: `ct.yaml`
```yaml
remote: origin
chart-dirs:
  - charts
check-version-increment: true
validate-maintainers: false
```

## File: `aws-cloudformation/ecs-fargate/n8n-w-multimain-queuemode.yaml`
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Deploys n8n with multi-main and queue mode configured. s3 is used for storage. 

Parameters:

# n8n host parameters

  N8nHostedZone:
    Type: AWS::Route53::HostedZone::Id
    Description: "Selected the hosted zone you would like to use to access n8n. https://docs.n8n.io/hosting/configuration/environment-variables/deployment/"
    AllowedPattern: "Z.+"
    ConstraintDescription: "You must selected a hosted zone in order to continue"

  N8nHostRecordName:
    Type: String
    Description: "Enter the host name that matches the hosted zone you selected. Must match Cert ARN."
    AllowedPattern: ".+"
    ConstraintDescription: "Please enter a host record name to continue."
    Default: "ENTER-YOUR-HOST-RECORD-HERE"
  
  N8nCertArn:
    Type: String
    Description: "Copy paste the ARN of the security certificate associated with your hosted zone. MUST BE IN SAME REGION AS STACK!"
    Default: "ENTER-YOUR-CERT-ARN-HERE"

# vpc/network configuration

  VpcCidr:
    Type: String
    Default: 10.0.0.0/16
    Description: CIDR block for the VPC.

  PrivateSubnet1Cidr:
    Type: String
    Default: 10.0.1.0/24
    Description: CIDR block for private subnet 1.

  PrivateSubnet2Cidr:
    Type: String
    Default: 10.0.2.0/24
    Description: CIDR block for private subnet 2.

  PrivateSubnet3Cidr:
    Type: String
    Default: 10.0.3.0/24
    Description: CIDR block for private subnet 3.

  

# postgres parameters
  DBInstanceClass:
    Type: String
    Description: "Select instance class for n8n's PostgresDB"
    Default: db.t4g.small
    AllowedValues: 
      - db.t4g.micro
      - db.t4g.small
      - db.t4g.medium
      - db.m7g.large
      - db.m7g.xlarge
      - db.m7g.2xlarge
  DBAllocatedStorage:
    Type: Number
    Default: 20
    MinValue: 20
    Description: Storage in GiB (minimum for RDS is typically 20 GiB)
  MasterUsername:
    Type: String
    Default: postgres
    Description: Master (admin) username
    AllowedPattern: '^[a-zA-Z][a-zA-Z0-9_]{0,15}$'
  MasterUserPassword:
    Type: String
    NoEcho: true
    Default: Password123!
    Description: "Master (admin) password. IMPORTANT NOTE! Please change this from the default for optimal security."
    MinLength: 8
  DBName:
    Type: String
    Default: n8n
    Description: Initial database to create
    AllowedPattern: '^[a-zA-Z][a-zA-Z0-9_]{0,62}$'

# redis parameters
  RedisInstanceClass:
    Type: String
    Description: "Select instance class for n8n's Redis cache"
    Default: cache.t4g.small
    AllowedValues:
      - cache.t4g.micro
      - cache.t4g.small
      - cache.t4g.medium
      - cache.m4.large
      - cache.m4.xlarge
      - cache.m4.2xlarge
  RedisPassword:
    Type: String
    NoEcho: true
    Description: "Password for the Redis user 'default'. Must be 16 characters at least. IMPORTANT NOTE! Please change this from the default for optimal security."
    AllowedPattern: ".{16}.*"
    Default: "Myverysecureredispassword1!"

# license key parameters
  N8nLicenseKey:
    Type: String
    Description: "Enter your n8n enterprise license key."
    Default: 12345678-0987-1234-5678-123456789012
    AllowedPattern: '^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$'
             
  N8nTenantId:
    Type: String
    Description: "[Embed only] Enter your n8n tenant ID. Leave as default for a standard install."
    Default: 1
    AllowedPattern: '^[0-9]+$'

# labels to make everything easier to read during setup
Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: "n8n License Config"
        Parameters:
          - N8nLicenseKey
          - N8nTenantId
      - Label:
          default: "DNS Config"
        Parameters:
           - N8nHostedZone
           - N8nCertArn
           - N8nHostRecordName
      - Label:
          default: "VPC & Network Config"
        Parameters:
          - VpcCidr
          - PrivateSubnet1Cidr
          - PrivateSubnet2Cidr
          - PrivateSubnet3Cidr
      - Label:
          default: "Postgres DB Config"
        Parameters:
          - DBInstanceClass
          - MasterUsername
          - MasterUserPassword
          - DBAllocatedStorage
          - DBName
      - Label: 
          default: "Redis Config"
        Parameters:
          - RedisInstanceClass
          - RedisPassword

Resources:

  # create n8n license secret
  N8nLicenseSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Name: app-user/n8nlicense
      Description: Access keys for app-user created by CloudFormation
      SecretString: !Sub |
        {
          "LicenseKey": "${N8nLicenseKey}",
          "TenantId": "${N8nTenantId}"
        }

  # create encryption key secret        
  N8nEncryptionKey:
    Type: AWS::SecretsManager::Secret
    Properties:
      Name: app-user/encryptionkey
      Description: Encryption key for queue mode
      SecretString: !Select
        - 2
        - !Split
          - "/"
          - !Ref AWS::StackId

  # create VPC just for n8n
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCidr
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-vpc"

  # Internet Gateway (created and attached to the VPC; not routed to by private subnets)
  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-igw"

  VPCGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway

  # Subnets (first 3 AZs in the chosen region)
  PrivateSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PrivateSubnet1Cidr
      AvailabilityZone: !Select [0, !GetAZs '']
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-private-1"

  PrivateSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PrivateSubnet2Cidr
      AvailabilityZone: !Select [1, !GetAZs '']
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-private-2"

  PrivateSubnet3:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PrivateSubnet3Cidr
      AvailabilityZone: !Select [2, !GetAZs '']
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-private-3"

  # Public subnets, first two in chosen region  
  PublicSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.10.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-public-1"

  PublicSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.11.0/24
      AvailabilityZone: !Select [1, !GetAZs '']
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-public-2"

  # route table for  allowing public access
  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-public-rt"

  PublicDefaultRoute:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway

  PublicSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PublicSubnet1
      RouteTableId: !Ref PublicRouteTable

  PublicSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PublicSubnet2
      RouteTableId: !Ref PublicRouteTable
  
  # Public NAT gateways, one per public subnet/AZ
  NatEipAz1:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc

  NatGatewayAz1:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatEipAz1.AllocationId
      SubnetId: !Ref PublicSubnet1
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-nat-az1"
  
  NatEipAz2:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc

  NatGatewayAz2:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt NatEipAz2.AllocationId
      SubnetId: !Ref PublicSubnet2
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-nat-az2"

  # private route tables configured per AZ

  PrivateRouteTableAz1:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-private-rt-az1"

  PrivateDefaultRouteViaNatAz1:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTableAz1
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGatewayAz1

  PrivateRouteTableAz2:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub "${AWS::StackName}-private-rt-az2"

  PrivateDefaultRouteViaNatAz2:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PrivateRouteTableAz2
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGatewayAz2

  PrivateSubnet1Association:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnet1
      RouteTableId: !Ref PrivateRouteTableAz1

  PrivateSubnet2Association:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnet2
      RouteTableId: !Ref PrivateRouteTableAz2

  PrivateSubnet3Association:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnet3
      RouteTableId: !Ref PrivateRouteTableAz1
  
  # Security group for 443, 80, 5678 access over HTTPS
  ALBSecGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: default VPC security group
      VpcId: !Ref VPC
      GroupName: !Sub "${AWS::StackName}-alb-sg"
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0

  # separate egress rules to prevent circular reference 
  ALBTaskEgress:
    Type: AWS::EC2::SecurityGroupEgress
    Properties:
      GroupId: !Ref ALBSecGroup
      IpProtocol: tcp
      FromPort: 5678
      ToPort: 5678
      DestinationSecurityGroupId: !Ref TaskSecGroupMain
    
  # Load balancer for reaching mains
  ElasticLoadBalancingV2LoadBalancer:
    Type: "AWS::ElasticLoadBalancingV2::LoadBalancer"
    Properties:
        Name: !Sub "${AWS::StackName}-alb"
        Scheme: "internet-facing"
        Type: "application"
        Subnets: 
          - !Ref PublicSubnet1
          - !Ref PublicSubnet2
        SecurityGroups: 
          - !Ref ALBSecGroup
        IpAddressType: "ipv4"
        LoadBalancerAttributes: 
          - 
            Key: "access_logs.s3.enabled"
            Value: "false"
          - 
            Key: "idle_timeout.timeout_seconds"
            Value: "60"
          - 
            Key: "deletion_protection.enabled"
            Value: "false"
          - 
            Key: "routing.http2.enabled"
            Value: "true"
          - 
            Key: "routing.http.drop_invalid_header_fields.enabled"
            Value: "false"
          - 
            Key: "routing.http.xff_client_port.enabled"
            Value: "false"
          - 
            Key: "routing.http.preserve_host_header.enabled"
            Value: "false"
          - 
            Key: "routing.http.xff_header_processing.mode"
            Value: "append"
          - 
            Key: "load_balancing.cross_zone.enabled"
            Value: "true"
          - 
            Key: "routing.http.desync_mitigation_mode"
            Value: "defensive"
          - 
            Key: "client_keep_alive.seconds"
            Value: "3600"
          - 
            Key: "waf.fail_open.enabled"
            Value: "false"
          - 
            Key: "routing.http.x_amzn_tls_version_and_cipher_suite.enabled"
            Value: "false"
          - 
            Key: "zonal_shift.config.enabled"
            Value: "false"
          - 
            Key: "connection_logs.s3.enabled"
            Value: "false"

  # ALB target groups
  HttpAppTargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      Name: !Sub "${AWS::StackName}-alb-tg"
      VpcId: !Ref VPC
      Protocol: HTTP
      Port: 5678
      TargetType: ip
      IpAddressType: ipv4
      ProtocolVersion: HTTP1
      HealthCheckEnabled: true
      HealthCheckProtocol: HTTP
      HealthCheckPort: 5678
      HealthCheckIntervalSeconds: 60
      HealthCheckTimeoutSeconds: 30
      HealthyThresholdCount: 8
      UnhealthyThresholdCount: 5
      HealthCheckPath: /
      Matcher:
        HttpCode: '200-399'
  
  # Listeners
  ElasticLoadBalancingV2Listener2:
    Type: "AWS::ElasticLoadBalancingV2::Listener"
    Properties:
        LoadBalancerArn: !Ref ElasticLoadBalancingV2LoadBalancer
        Port: 443
        Protocol: "HTTPS"
        Certificates:
          - CertificateArn: !Ref N8nCertArn
        DefaultActions: 
          - 
            Order: 1
            TargetGroupArn: !Ref HttpAppTargetGroup
            Type: "forward"

  ElasticLoadBalancingV2Listener3:
    Type: "AWS::ElasticLoadBalancingV2::Listener"
    Properties:
        LoadBalancerArn: !Ref ElasticLoadBalancingV2LoadBalancer
        Port: 80
        Protocol: "HTTP"
        DefaultActions: 
          - 
            Order: 1
            Type: "redirect"
            RedirectConfig:
              Protocol: HTTPS
              Port: 443
              StatusCode: HTTP_301



  # create A record in hosted zone
  N8nHostRecord:
    Type: AWS::Route53::RecordSet
    Properties:
      Name: !Ref N8nHostRecordName
      HostedZoneId: !Ref N8nHostedZone
      Type: A
      AliasTarget:
        DNSName: !GetAtt ElasticLoadBalancingV2LoadBalancer.DNSName
        HostedZoneId: !GetAtt ElasticLoadBalancingV2LoadBalancer.CanonicalHostedZoneID
        EvaluateTargetHealth: false

  # create s3 bucket for binary data
  S3BinaryBucket:
    Type: AWS::S3::Bucket
    Properties:
      VersioningConfiguration:
        Status: Enabled
      BucketName: !Sub "${AWS::StackName}-n8n-bin"
  
  # directly attach bucket policy
  S3BucketPolicy:
    DependsOn:
      - N8nTaskRole
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref S3BinaryBucket
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Sid: AllowS3UserFullAccess
            Effect: Allow
            Principal:
              AWS: !GetAtt N8nTaskRole.Arn
            Action:
              - "s3:GetBucketLocation"
              - "s3:ListBucket"
            Resource: !Sub "arn:aws:s3:::${S3BinaryBucket}"
          - Sid: AllowS3UserFullAccessToObjects
            Effect: Allow
            Principal:
              AWS: !GetAtt N8nTaskRole.Arn
            Action:
              - "s3:PutObject"
              - "s3:GetObject"
              - "s3:DeleteObject"
            Resource: !Sub "arn:aws:s3:::${S3BinaryBucket}/*"

  # add vpc gateway endpoint for s3
  S3GatewayEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: !Ref VPC
      ServiceName: !Sub "com.amazonaws.${AWS::Region}.s3"
      RouteTableIds:
        - !Ref PrivateRouteTableAz1
        - !Ref PrivateRouteTableAz2
      VpcEndpointType: Gateway

  # security groups and subnet group for postgres
  RDSSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: !Sub "${AWS::StackName}-rds-sg"
      GroupDescription: Allow PostgreSQL access to RDS on 5432
      VpcId: !Ref VPC
  
  # separate security group ingresses for workers and mains to prevent circular reference
  RDSSecGroupIngressMain:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: !Ref RDSSecurityGroup
      IpProtocol: tcp
      FromPort: 5432
      ToPort: 5432
      SourceSecurityGroupId: !Ref TaskSecGroupMain
  
  RDSSecGroupIngressWorker:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: !Ref RDSSecurityGroup
      IpProtocol: tcp
      FromPort: 5432
      ToPort: 5432
      SourceSecurityGroupId: !Ref TaskSecGroupWorker

  # subnet group for RDS
  RDSSubnetGroup:
    Type: AWS::RDS::DBSubnetGroup
    Properties:
      DBSubnetGroupName: !Sub "${AWS::StackName}-pg-db-subnets"
      DBSubnetGroupDescription: Subnet group for RDS Postgres
      SubnetIds: [!Ref PrivateSubnet1, !Ref PrivateSubnet2, !Ref PrivateSubnet3]

  # launch postgresdb instance
  PostgresDB:
    Type: AWS::RDS::DBInstance
    DeletionPolicy: Snapshot
    UpdateReplacePolicy: Snapshot
    Properties:
      Engine: postgres
      EngineVersion: 16
      DBInstanceClass: !Ref DBInstanceClass
      DBInstanceIdentifier: !Sub "${AWS::StackName}-pg-db"
      AllocatedStorage: !Ref DBAllocatedStorage
      StorageType: gp3
      StorageEncrypted: true
      PubliclyAccessible: false
      MultiAZ: true
      AutoMinorVersionUpgrade: true
      BackupRetentionPeriod: 15
      Port: 5432
      MasterUsername: !Ref MasterUsername
      MasterUserPassword: !Ref MasterUserPassword
      DBName: !Ref DBName
      VPCSecurityGroups:
        - !GetAtt RDSSecurityGroup.GroupId
      DBSubnetGroupName: !Ref RDSSubnetGroup
      DeletionProtection: false
      EnablePerformanceInsights: false
      CopyTagsToSnapshot: true


  # create secrets file for n8n to connect to RDS
  RDSSecrets:
    DependsOn:
      - PostgresDB
    Type: AWS::SecretsManager::Secret
    Properties:
      Name: app-user/dbcredentials
      Description: Credentials for n8n to connect to postgres
      SecretString: !Sub |
        {
          "user": "${MasterUsername}",
          "password": "${MasterUserPassword}",
          "host": "${PostgresDB.Endpoint.Address}",
          "port": "5432",
          "database": "${DBName}"
        }  

  # create subnet group for elasticache
  CacheSubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Subnet group for Redis
      SubnetIds: [!Ref PrivateSubnet1, !Ref PrivateSubnet2, !Ref PrivateSubnet3]
      CacheSubnetGroupName: !Sub ${AWS::StackName}-subnets

  # create security group for elasticache
  CacheSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow Redis (TCP 6379) from the app SG
      VpcId: !Ref VPC

  # separate security group ingresses for workers and mains
  CacheSecGroupIngressMain:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: !Ref CacheSecurityGroup
      IpProtocol: tcp
      FromPort: 6379
      ToPort: 6379
      SourceSecurityGroupId: !Ref TaskSecGroupMain

  CacheSecGroupIngressWorker:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: !Ref CacheSecurityGroup
      IpProtocol: tcp
      FromPort: 6379
      ToPort: 6379
      SourceSecurityGroupId: !Ref TaskSecGroupWorker

  # create parameter group for elasticache
  RedisParamGroup:
    Type: AWS::ElastiCache::ParameterGroup
    Properties:
      CacheParameterGroupFamily: redis7
      Description: Minimal parameter group (defaults)

  # create password secret for n8n to connect to redis
  RedisPasswordSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Name: app-user/redispassword
      Description: Password for n8n to connect to redis
      SecretString: !Ref RedisPassword

  # create elasticache replication group for redis
  Redis:
    DependsOn:
      - RedisParamGroup
      - CacheSecurityGroup
      - CacheSubnetGroup
      - RedisPasswordSecret
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupId: !Sub ${AWS::StackName}-redis
      ReplicationGroupDescription: Minimal single-node Redis
      Engine: redis
      CacheNodeType: !Ref RedisInstanceClass
      NumNodeGroups: 1
      ReplicasPerNodeGroup: 0  # single primary, no replicas
      MultiAZEnabled: false
      AutomaticFailoverEnabled: false
      CacheSubnetGroupName: !Ref CacheSubnetGroup
      SecurityGroupIds: [ !Ref CacheSecurityGroup ]
      CacheParameterGroupName: !Ref RedisParamGroup
      AuthToken: !Sub "{{resolve:secretsmanager:${RedisPasswordSecret}}}" 
      AtRestEncryptionEnabled: true
      TransitEncryptionEnabled: true
      Port: 6379




  # create fargate cluster
  ECSCluster:
    Type: "AWS::ECS::Cluster"
    DependsOn:
      - RDSSubnetGroup
      - RDSSecurityGroup
      - PostgresDB
      - S3BinaryBucket
    Properties:
        ClusterName: !Sub "${AWS::StackName}-cluster"
        CapacityProviders: 
          - "FARGATE"
          - "FARGATE_SPOT"

# security group for n8n main tasks
  TaskSecGroupMain:
    Type: AWS::EC2::SecurityGroup
    Properties:
      VpcId: !Ref VPC
      GroupDescription: "Allow only the ALB to reach tasks on 5678"
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 5678
          ToPort: 5678
          SourceSecurityGroupId: !Ref ALBSecGroup
      SecurityGroupEgress:
        # postgres
        - IpProtocol: tcp
          FromPort: 5432
          ToPort: 5432
          DestinationSecurityGroupId: !Ref RDSSecurityGroup
        # redis
        - IpProtocol: tcp
          FromPort: 6379
          ToPort: 6379
          DestinationSecurityGroupId: !Ref CacheSecurityGroup
        # for fetching certs
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0

# security group for n8n worker tasks
  TaskSecGroupWorker:
    Type: AWS::EC2::SecurityGroup
    Properties:
      VpcId: !Ref VPC
      GroupDescription: "Do not allow ALB to reach workers"
      SecurityGroupEgress:
        # postgres
        - IpProtocol: tcp
          FromPort: 5432
          ToPort: 5432
          DestinationSecurityGroupId: !Ref RDSSecurityGroup
        # redis
        - IpProtocol: tcp
          FromPort: 6379
          ToPort: 6379
          DestinationSecurityGroupId: !Ref CacheSecurityGroup
        # for rds cert fetching
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0

  # create log group for n8n in cloudwatch logs
  N8nLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub /ecs/${AWS::StackName}
      RetentionInDays: 7
      
  # ECS Task Role (shared by workers and mains)
  # in-line policy grants access to s3
  N8nTaskRole:
    Type: AWS::IAM::Role
    DependsOn:
      - RDSSubnetGroup
      - RDSSecurityGroup
      - PostgresDB
    Properties:
      RoleName: !Sub "${AWS::StackName}-task-role"
      Path: /
      MaxSessionDuration: 3600
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: ecs-tasks.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: inline-s3-for-task-role
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Sid: BucketAccess
                Effect: Allow
                Action:
                  - "s3:GetBucketLocation"
                  - "s3:ListBucket"
                Resource:
                  - !Sub "arn:aws:s3:::${S3BinaryBucket}"
              - Sid: ObjectAccess
                Effect: Allow
                Action:
                  - "s3:PutObject"
                  - "s3:GetObject"
                  - "s3:DeleteObject"
                Resource:
                  - !Sub "arn:aws:s3:::${S3BinaryBucket}/*"


  # ECS Task Execution Role
  N8nTaskExecutionRole:
    Type: AWS::IAM::Role
    DependsOn:
      - RDSSubnetGroup
      - RDSSecurityGroup
      - PostgresDB
      - RedisPasswordSecret
    Properties:
      RoleName: !Sub "${AWS::StackName}-task-execution-role"
      Path: /
      MaxSessionDuration: 3600
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: ecs-tasks.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        # grant access to secrets for db etc.
        - PolicyName: secrets-access
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - secretsmanager:GetSecretValue
                  - secretsmanager:DescribeSecret
                Resource:
                  - !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials*"                  
                  - !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/n8nlicense*" 
                  - !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/redispassword*"
                  - !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/encryptionkey*"
        # grant access to services to write logs to cloudwatch
        - PolicyName: cloudwatch-write-logs
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Sid: "WriteToN8nLogGroup"
                Action:
                  - "logs:CreateLogStream"
                  - "logs:PutLogEvents"
                Resource: 
                  - !Sub "arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/ecs/${AWS::StackName}"
                  - !Sub "arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/ecs/${AWS::StackName}:*"                  
  # Task Definition for n8n main
  N8nMainTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    DependsOn:
      - RDSSubnetGroup
      - RDSSecurityGroup
      - PostgresDB
      - RDSSecrets
      - N8nLicenseSecret
      - N8nEncryptionKey
    Properties:
      Family: n8n-main
      Cpu: "1024"
      Memory: "3072"
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      RuntimePlatform:
        CpuArchitecture: X86_64
        OperatingSystemFamily: LINUX
      TaskRoleArn: !GetAtt N8nTaskRole.Arn
      ExecutionRoleArn: !GetAtt N8nTaskExecutionRole.Arn
      Volumes:
        - Name: certs
      ContainerDefinitions:
        - Name: n8n
          Image: n8nio/n8n:latest
          Essential: true
          PortMappings:
            - ContainerPort: 5678
              HostPort: 5678
              Protocol: tcp
              Name: n8n-5678-tcp
              AppProtocol: http
          Secrets:
            - Name: N8N_LICENSE_ACTIVATION_KEY
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/n8nlicense:LicenseKey::"
            - Name: N8N_LICENSE_TENANT_ID
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/n8nlicense:TenantId::"
            - Name: N8N_ENCRYPTION_KEY
              ValueFrom: !Ref N8nEncryptionKey
            - Name: DB_POSTGRESDB_HOST
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:host::"
            - Name: DB_POSTGRESDB_PORT
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:port::"
            - Name: DB_POSTGRESDB_DATABASE
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:database::"
            - Name: DB_POSTGRESDB_USER
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:user::"
            - Name: DB_POSTGRESDB_PASSWORD
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:password::"
            - Name: QUEUE_BULL_REDIS_PASSWORD
              ValueFrom: !Ref RedisPasswordSecret
          Environment:
            - Name: N8N_HOST
              Value: !Ref N8nHostRecord
            - Name: N8N_PROTOCOL
              Value: https
            - Name: N8N_DEFAULT_BINARY_DATA_MODE
              Value: s3
            - Name: N8N_RUNNERS_ENABLED
              Value: true
            - Name: N8N_METRICS
              Value: true
            - Name: N8N_METRICS_INCLUDE_QUEUE_METRICS
              Value: true
            - Name: N8N_AVAILABLE_BINARY_DATA_MODES
              Value: filesystem,s3
            - Name: N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT
              Value: true
            - Name: N8N_SECURE_COOKIE
              Value: true
            - Name: DB_TYPE
              Value: postgresdb
            - Name: DB_POSTGRESDB_SSL_ENABLED
              Value: true
            - Name: DB_POSTGRESDB_SSL_CA
              Value: /certs/rds-global-bundle.pem
            - Name: DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED
              Value: false
            - Name: N8N_EXTERNAL_STORAGE_S3_HOST
              Value: !Sub "s3.${AWS::Region}.amazonaws.com"
            - Name: N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME
              Value: !Ref S3BinaryBucket
            - Name: N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION
              Value: !Ref AWS::Region
            - Name: EXECUTIONS_MODE
              Value: queue
            - Name: N8N_LOG_LEVEL
              Value: warn
            - Name: N8N_MULTI_MAIN_SETUP_ENABLED
              Value: true
            - Name: QUEUE_HEALTH_CHECK_ACTIVE
              Value: true
            - Name: QUEUE_BULL_REDIS_TLS
              Value: true
            - Name: QUEUE_BULL_REDIS_HOST
              Value: !GetAtt Redis.PrimaryEndPoint.Address
            - Name: QUEUE_BULL_REDIS_PORT
              Value: !GetAtt Redis.PrimaryEndPoint.Port            
            - Name: QUEUE_BULL_REDIS_USERNAME
              Value: default
            - Name: OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS
              Value: true
            - Name: WEBHOOK_URL
              Value: !Sub "https://${N8nHostRecord}/"

          LogConfiguration:
            LogDriver: awslogs
            Options:
              awslogs-group: !Sub /ecs/${AWS::StackName}
              awslogs-region: !Sub ${AWS::Region}
              awslogs-stream-prefix: ecs
          HealthCheck:
            Command:
              - CMD-SHELL
              - curl -fsS http://127.0.0.1:5678/ || wget -qO- http://127.0.0.1:5678/ >/dev/null || exit 1
            Interval: 15
            Timeout: 5
            Retries: 3
            StartPeriod: 90
          DependsOn:
            - ContainerName: rds-cert-fetcher
              Condition: SUCCESS
          MountPoints:
            - SourceVolume: certs
              ContainerPath: /certs
        - Name: rds-cert-fetcher
          Image: public.ecr.aws/amazonlinux/amazonlinux:2023
          Essential: false
          Command:
            - /bin/sh
            - -c
            - >
              set -euo pipefail;
              dnf install -y gawk openssl;
              mkdir -p /certs;
              curl -fsSL --retry 5
              https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
              -o /certs/rds-global-bundle.pem;
              # (optional) basic sanity check:
              awk 'BEGIN{c=0} /BEGIN CERTIFICATE/{c++} END{ if(c<1){exit 1} }' /certs/rds-global-bundle.pem
          MountPoints:
            - SourceVolume: certs
              ContainerPath: /certs

  # Fargate Service for main
  ECSMainService:
    Type: "AWS::ECS::Service"
    DependsOn:
      - RDSSubnetGroup
      - RDSSecurityGroup
      - PostgresDB
      - Redis
    Properties:
        ServiceName: !Sub "${AWS::StackName}-svc-main"
        Cluster: !GetAtt ECSCluster.Arn
        LoadBalancers: 
          -  
            TargetGroupArn: !Ref HttpAppTargetGroup
            ContainerName: "n8n"
            ContainerPort: 5678
        DesiredCount: 2
        TaskDefinition: !Ref N8nMainTaskDefinition
        DeploymentConfiguration: 
            MaximumPercent: 200
            MinimumHealthyPercent: 100
            DeploymentCircuitBreaker: 
                Enable: true
                Rollback: true
        NetworkConfiguration: 
            AwsvpcConfiguration: 
                AssignPublicIp: "DISABLED"
                SecurityGroups: 
                  - !Ref TaskSecGroupMain
                Subnets: 
                  - !Ref PrivateSubnet1
                  - !Ref PrivateSubnet2
        HealthCheckGracePeriodSeconds: 600
        SchedulingStrategy: "REPLICA"
        DeploymentController: 
            Type: "ECS"
        CapacityProviderStrategy: 
          - 
            CapacityProvider: "FARGATE"
            Weight: 1
            Base: 0
  
  # Task Definition for workers
  N8nWorkerTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    DependsOn:
      - RDSSubnetGroup
      - RDSSecurityGroup
      - PostgresDB
      - N8nLicenseSecret
    Properties:
      Family: n8n-worker
      Cpu: "1024"
      Memory: "3072"
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      RuntimePlatform:
        CpuArchitecture: X86_64
        OperatingSystemFamily: LINUX
      TaskRoleArn: !GetAtt N8nTaskRole.Arn
      ExecutionRoleArn: !GetAtt N8nTaskExecutionRole.Arn
      Volumes:
        - Name: certs
      ContainerDefinitions:
        - Name: n8n
          Image: n8nio/n8n:latest
          Essential: true
          PortMappings:
            - ContainerPort: 5678
              HostPort: 5678
              Protocol: tcp
              Name: n8n-5678-tcp
              AppProtocol: http
          EntryPoint:
            - "node"
            - "/usr/local/bin/n8n"
            - "worker"
          Secrets:
            - Name: N8N_LICENSE_ACTIVATION_KEY
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/n8nlicense:LicenseKey::"
            - Name: N8N_LICENSE_TENANT_ID
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/n8nlicense:TenantId::"
            - Name: N8N_ENCRYPTION_KEY
              ValueFrom: !Ref N8nEncryptionKey
            - Name: DB_POSTGRESDB_HOST
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:host::"
            - Name: DB_POSTGRESDB_PORT
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:port::"
            - Name: DB_POSTGRESDB_DATABASE
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:database::"
            - Name: DB_POSTGRESDB_USER
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:user::"
            - Name: DB_POSTGRESDB_PASSWORD
              ValueFrom: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:app-user/dbcredentials:password::"
            - Name: QUEUE_BULL_REDIS_PASSWORD
              ValueFrom: !Ref RedisPasswordSecret               
          Environment:
            - Name: N8N_HOST
              Value: !Ref N8nHostRecord
            - Name: N8N_PORT
              Value: 0
            - Name: N8N_PROTOCOL
              Value: https
            - Name: N8N_MODE
              Value: worker
            - Name: N8N_DEFAULT_BINARY_DATA_MODE
              Value: s3
            - Name: N8N_RUNNERS_ENABLED
              Value: true
            - Name: N8N_METRICS
              Value: true
            - Name: N8N_METRICS_INCLUDE_QUEUE_METRICS
              Value: true
            - Name: N8N_AVAILABLE_BINARY_DATA_MODES
              Value: filesystem,s3
            - Name: N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT
              Value: true
            - Name: N8N_SECURE_COOKIE
              Value: true
            - Name: DB_TYPE
              Value: postgresdb
            - Name: DB_POSTGRESDB_SSL_ENABLED
              Value: true
            - Name: DB_POSTGRESDB_SSL_CA
              Value: /certs/rds-global-bundle.pem
            - Name: DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED
              Value: false
            - Name: N8N_EXTERNAL_STORAGE_S3_HOST
              Value: !Sub "s3.${AWS::Region}.amazonaws.com"
            - Name: N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME
              Value: !Ref S3BinaryBucket
            - Name: N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION
              Value: !Ref AWS::Region
            - Name: EXECUTIONS_MODE
              Value: queue
            - Name: N8N_LOG_LEVEL
              Value: warn
            - Name: N8N_MULTI_MAIN_SETUP_ENABLED
              Value: true
            - Name: OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS
              Value: true
            - Name: QUEUE_HEALTH_CHECK_ACTIVE
              Value: true
            - Name: QUEUE_BULL_REDIS_TLS
              Value: true
            - Name: QUEUE_BULL_REDIS_HOST
              Value: !GetAtt Redis.PrimaryEndPoint.Address
            - Name: QUEUE_BULL_REDIS_PORT
              Value: !GetAtt Redis.PrimaryEndPoint.Port  
            - Name: QUEUE_BULL_REDIS_USERNAME
              Value: default              
            - Name: WEBHOOK_URL
              Value: !Sub "https://${N8nHostRecord}/"

          LogConfiguration:
            LogDriver: awslogs
            Options:
              awslogs-group: !Sub /ecs/${AWS::StackName}
              awslogs-region: !Sub ${AWS::Region}
              awslogs-stream-prefix: ecs
          HealthCheck:
            Command:
              - CMD-SHELL
              - echo ok
            Timeout: 15
            Retries: 3
            StartPeriod: 90
          DependsOn:
            - ContainerName: rds-cert-fetcher
              Condition: SUCCESS
          MountPoints:
            - SourceVolume: certs
              ContainerPath: /certs
        - Name: rds-cert-fetcher
          Image: public.ecr.aws/amazonlinux/amazonlinux:2023
          Essential: false
          Command:
            - /bin/sh
            - -c
            - >
              set -euo pipefail;
              dnf install -y gawk openssl;
              mkdir -p /certs;
              curl -fsSL --retry 5
              https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
              -o /certs/rds-global-bundle.pem;
              # (optional) basic sanity check:
              awk 'BEGIN{c=0} /BEGIN CERTIFICATE/{c++} END{ if(c<1){exit 1} }' /certs/rds-global-bundle.pem
          MountPoints:
            - SourceVolume: certs
              ContainerPath: /certs

  # Fargate Service for workers
  ECSWorkerService:
    Type: "AWS::ECS::Service"
    DependsOn:
      - RDSSubnetGroup
      - RDSSecurityGroup
      - PostgresDB
      - Redis
    Properties:
        ServiceName: !Sub "${AWS::StackName}-svc-worker"
        Cluster: !GetAtt ECSCluster.Arn
        DesiredCount: 3
        TaskDefinition: !Ref N8nWorkerTaskDefinition
        DeploymentConfiguration: 
            MaximumPercent: 200
            MinimumHealthyPercent: 100
            DeploymentCircuitBreaker: 
                Enable: true
                Rollback: true
        NetworkConfiguration: 
            AwsvpcConfiguration: 
                AssignPublicIp: "DISABLED"
                SecurityGroups: 
                  - !Ref TaskSecGroupWorker
                Subnets: 
                  - !Ref PrivateSubnet1
                  - !Ref PrivateSubnet2
                  - !Ref PrivateSubnet3
        HealthCheckGracePeriodSeconds: 600
        SchedulingStrategy: "REPLICA"
        DeploymentController: 
            Type: "ECS"
        CapacityProviderStrategy: 
          - 
            CapacityProvider: "FARGATE"
            Weight: 1
            Base: 0

  # auto scaling for worker service
  ECSServiceScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    DependsOn: ECSWorkerService
    Properties:
      ServiceNamespace: ecs
      ScalableDimension: ecs:service:DesiredCount
      ResourceId: !Sub 
        - "service/${ClusterName}/${ServiceName}"
        - { ClusterName: !Ref ECSCluster, ServiceName: !GetAtt ECSWorkerService.Name }
      MinCapacity: 2
      MaxCapacity: 10
      RoleARN: !Sub "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ecs.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ECSService"

  # scaling rules for CPU
  ECSServiceCPUScalingPolicy:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: !Sub "${AWS::StackName}-cpu-tt"
      PolicyType: TargetTrackingScaling
      ScalingTargetId: !Ref ECSServiceScalableTarget
      TargetTrackingScalingPolicyConfiguration:
        PredefinedMetricSpecification:
          PredefinedMetricType: ECSServiceAverageCPUUtilization
        TargetValue: 60
        ScaleInCooldown: 60
        ScaleOutCooldown: 60

  # scaling rules for memory
  ECSServiceMemoryScalingPolicy:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: !Sub "${AWS::StackName}-mem-tt"
      PolicyType: TargetTrackingScaling
      ScalingTargetId: !Ref ECSServiceScalableTarget
      TargetTrackingScalingPolicyConfiguration:
        PredefinedMetricSpecification:
          PredefinedMetricType: ECSServiceAverageMemoryUtilization
        TargetValue: 70
        ScaleInCooldown: 60
        ScaleOutCooldown: 60

# output useful information to make things easier to read.
Outputs:
  VpcUrl:
    Description: Links to VPC for deploying n8n resources. 
    Value: !Sub "https://${AWS::Region}.console.aws.amazon.com/vpcconsole/home?region=${AWS::Region}#VpcDetails:VpcId=${VPC}"

  N8nHostname: 
    Description: URL used to access n8n
    Value: !Sub "https://${N8nHostRecord}" 
  
  N8nMainServiceUrl:
    Description: URL to reach n8n main service in ECS
    Value: !Sub "https://${AWS::Region}.console.aws.amazon.com/ecs/v2/clusters/${ECSCluster}/services/${ECSMainService.Name}/health?region=${AWS::Region}"

  N8nWorkerServiceUrl:
    Description: URL to reach n8n worker service in ECS
    Value: !Sub "https://${AWS::Region}.console.aws.amazon.com/ecs/v2/clusters/${ECSCluster}/services/${ECSWorkerService.Name}/health?region=${AWS::Region}"

  S3BucketUrl:
    Description: Link to S3 bucket used for binary data
    Value: !Sub "https://${AWS::Region}.console.aws.amazon.com/s3/buckets/${S3BinaryBucket}"

  PostgresDbUrl:
    Description: Link to Postgres DB used for n8n
    Value: !Sub "https://${AWS::Region}.console.aws.amazon.com/rds/home?region=${AWS::Region}#database:id=${PostgresDB}"
  
  RedisUrl:
    Description: Link to Elasticache used for n8n
    Value: !Sub "https://${AWS::Region}.console.aws.amazon.com/elasticache/home?region=${AWS::Region}#/redis/${Redis}"
```

## File: `charts/n8n/.helmignore`
```
# Patterns to ignore when building packages.
# This supports shell glob matching, relative path matching, and
# negation (prefixed with !). Only one pattern per line.
.DS_Store
# Common VCS dirs
.git/
.gitignore
.bzr/
.bzrignore
.hg/
.hgignore
.svn/
# Common backup files
*.swp
*.bak
*.tmp
*.orig
*~
# Various IDEs
.project
.idea/
*.tmproj
.vscode/

# OS generated files
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# CI/CD files
.github/
.gitlab-ci.yml
.travis.yml
.circleci/

# Documentation and examples (keep only essential docs)
CHANGELOG.md
LICENSE
*.md
examples/
docs/

# Testing files
test/
tests/
*_test.go
*.test

# Development files
Makefile
docker-compose.yml
docker-compose.yaml
*.dockerfile
Dockerfile*

# Package files
*.tgz
*.tar.gz

# Logs
*.log
logs/

# Node.js files (if any)
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json
yarn.lock
```

## File: `charts/n8n/Chart.yaml`
```yaml
apiVersion: v2
name: n8n
version: 1.3.0
kubeVersion: ">=1.25.0-0"
icon: >-
  https://raw.githubusercontent.com/n8n-io/n8n/master/packages/editor-ui/public/images/n8n-logo.png
description: >-
  Production-grade Helm chart for n8n, the workflow automation platform.
  Supports queue mode, multi-main HA, webhook processors, task runners, HPA,
  PDB, network policies, and S3 external storage.
appVersion: "2.12.2"
type: application
keywords:
  - n8n
  - workflow-automation
  - automation
  - queue
  - redis
  - postgres
home: https://n8n.io
sources:
  - https://github.com/n8n-io/n8n-hosting
  - https://github.com/n8n-io/n8n
maintainers:
  - name: n8n
    url: https://github.com/n8n-io
```

## File: `charts/n8n/README.md`
```markdown
# n8n Helm Chart

Production-grade Helm chart for [n8n](https://n8n.io), the workflow automation platform. Supports queue mode, multi-main HA, webhook processors, task runners, HPA, PDB, network policies, and S3 external storage.

## Prerequisites

- Helm 3.12+
- Kubernetes 1.25+

**Queue mode** (default): requires external PostgreSQL and Redis — this chart does not bundle them.
**Standalone mode**: no external dependencies; uses SQLite with a PersistentVolumeClaim.

## Install

```bash
# OCI registry (recommended)
helm install n8n oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.0 -f my-values.yaml
```

## Quick Start

1. **Set up external services** — PostgreSQL and Redis for queue mode (not needed for standalone mode)

2. **Create required secrets:**
   ```bash
   ./examples/create-secrets.sh
   ```

3. **Choose a values file** from the [examples](./examples/) directory and customize it

4. **Deploy:**
   ```bash
   helm install n8n oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.0 -f my-values.yaml
   ```

## Architecture

This chart supports two deployment modes:

- **Queue mode** (default) — main + workers + optional webhook processors. Requires external PostgreSQL and Redis.
- **Standalone mode** — single pod with SQLite. No external dependencies. Suitable for development and small-scale use.

In queue mode, three pod types are supported:

| Component | Purpose | Scaling |
|---|---|---|
| **main** | UI, API, non-production webhooks | 1 replica (or N with multi-main + Enterprise license) |
| **worker** | Executes workflows from Redis queue | 2+ replicas, stateless |
| **webhook-processor** | Handles production webhooks (optional) | 2+ replicas, stateless |

All three use the same n8n container image, differentiated by command/args.

## Examples

| File | Use case |
|---|---|
| [standalone.yaml](./examples/standalone.yaml) | Single pod with SQLite, no external dependencies |
| [minimal.yaml](./examples/minimal.yaml) | Single main pod, minimum config |
| [minimal-with-docker.yaml](./examples/minimal-with-docker.yaml) | Quick testing with Docker Postgres/Redis |
| [multi-main-queue.yaml](./examples/multi-main-queue.yaml) | Multi-main HA (Enterprise license required) |
| [task-runners.yaml](./examples/task-runners.yaml) | Queue mode with task runner sidecars |
| [production-s3.yaml](./examples/production-s3.yaml) | Production with S3, HPA, multi-main |
| [keda-autoscaling.yaml](./examples/keda-autoscaling.yaml) | Redis queue-length scaling with KEDA |

## Secret Management

1. **Core secrets** (`secretRefs.existingSecret`): `N8N_ENCRYPTION_KEY`, `N8N_HOST`, `N8N_PORT`, `N8N_PROTOCOL` — always required
2. **Database password** (`database.passwordSecret`): PostgreSQL password — queue mode only
3. **Redis password** (`redis.passwordSecret`): optional, for authenticated Redis — queue mode only

For production, use an external secrets operator (e.g., [External Secrets Operator](https://external-secrets.io/)) rather than storing secrets in values files.

## Key Configuration

| Value | Description | Default |
|---|---|---|
| `image.repository` | n8n image | `docker.n8n.io/n8nio/n8n` |
| `image.tag` | n8n version | `1.110.1` |
| `queueMode.workerReplicaCount` | Number of worker pods | `2` |
| `queueMode.workerConcurrency` | Jobs per worker | `10` |
| `multiMain.enabled` | Multi-main HA (Enterprise) | `false` |
| `webhookProcessor.enabled` | Dedicated webhook pods | `false` |
| `taskRunners.enabled` | Task runner sidecars | `false` |
| `ingress.enabled` | Create Ingress resource | `false` |
| `persistence.enabled` | PVC for main pods | `false` |
| `hpa.main.enabled` | HPA for main pods | `false` |
| `hpa.worker.enabled` | HPA for worker pods | `false` |
| `keda.enabled` | KEDA queue-based autoscaling | `false` |
| `networkPolicy.enabled` | Network policies | `false` |

See [values.yaml](./values.yaml) for the full list of configurable values.

## Task Runners

Task runners execute user-provided JavaScript and Python code in isolated sidecar containers, separate from the main n8n process. When enabled, each main and worker pod gets a runner sidecar.

**How it works:** The n8n container runs a task broker on port 5679. The runner sidecar connects to this broker over localhost to receive and execute code tasks.

**Enable task runners:**
```yaml
taskRunners:
  enabled: true
  authToken:
    existingSecret: "n8n-runner-token"
    existingSecretKey: "auth-token"
```

Create the auth token secret:
```bash
kubectl create secret generic n8n-runner-token \
  --from-literal=auth-token=$(openssl rand -base64 32)
```

See [task-runners.yaml](./examples/task-runners.yaml) for a complete example including resource tuning and Python runner support.

## KEDA Autoscaling

The built-in HPA scales workers based on CPU utilization. For queue-based workloads, [KEDA](https://keda.sh) can scale workers based on Redis queue length, which is more responsive to actual demand.

When `keda.enabled` is true, the chart creates KEDA `ScaledObject` resources instead of built-in HPAs for workers (and optionally webhook processors). KEDA must be installed in the cluster.

```bash
# Install KEDA
helm install keda kedacore/keda --namespace keda-system --create-namespace
```

```yaml
keda:
  enabled: true
  worker:
    minReplicaCount: 2
    maxReplicaCount: 20
    triggers:
      - type: redis
        metadata:
          listName: "bull:default:wait"
          listLength: "5"
```

See [keda-autoscaling.yaml](./examples/keda-autoscaling.yaml) for a complete example.

## Upgrading

Chart version bumps are automated via semantic-release. Check the [CHANGELOG](../bmad_repo/CHANGELOG.md) for breaking changes before upgrading.

```bash
helm upgrade n8n oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version <new-version> -f my-values.yaml
```
```

## File: `charts/n8n/values.schema.json`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "n8n values schema",
  "type": "object",
  "properties": {
    "image": {
      "type": "object",
      "properties": {
        "repository": { "type": "string", "minLength": 1 },
        "tag": { "type": "string", "minLength": 1 },
        "pullPolicy": {
          "type": "string",
          "enum": ["Always", "IfNotPresent", "Never"]
        }
      },
      "required": ["repository", "tag"]
    },
    "replicaCount": { "type": "integer", "minimum": 1 },
    "multiMain": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "replicas": { "type": "integer", "minimum": 1 },
        "antiAffinity": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": ["preferred", "required", "none"]
            }
          }
        },
        "topologySpreadConstraints": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "maxSkew": { "type": "integer", "minimum": 1 },
            "whenUnsatisfiable": {
              "type": "string",
              "enum": ["ScheduleAnyway", "DoNotSchedule"]
            }
          }
        },
        "setup": {
          "type": "object",
          "properties": {
            "keyTtl": { 
              "type": "integer", 
              "minimum": 1,
              "description": "Time to live (in seconds) for leader key in multi-main setup"
            },
            "checkInterval": { 
              "type": "integer", 
              "minimum": 1,
              "description": "Interval (in seconds) for leader check in multi-main setup"
            }
          }
        }
      },
      "required": ["enabled", "replicas"]
    },
    "taskRunners": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "image": {
          "type": "object",
          "properties": {
            "repository": { "type": "string", "minLength": 1 },
            "tag": {
              "type": "string",
              "description": "Task runner image tag. Leave empty to use the same tag as the main n8n image"
            },
            "pullPolicy": {
              "type": "string",
              "enum": ["Always", "IfNotPresent", "Never"]
            }
          },
          "required": ["repository"]
        },
        "mode": {
          "type": "string",
          "enum": ["external"],
          "description": "Task runner mode (only external is supported)"
        },
        "authToken": {
          "type": "object",
          "properties": {
            "existingSecret": { "type": "string" },
            "existingSecretKey": { "type": "string" },
            "value": { "type": "string" }
          }
        },
        "broker": {
          "type": "object",
          "properties": {
            "listenAddress": { "type": "string", "minLength": 1 },
            "port": { "type": "integer", "minimum": 1, "maximum": 65535 }
          },
          "required": ["listenAddress", "port"]
        },
        "launcher": {
          "type": "object",
          "properties": {
            "logLevel": {
              "type": "string",
              "enum": ["debug", "info", "warn", "error"]
            },
            "autoShutdownTimeout": { "type": "integer", "minimum": 0 }
          }
        },
        "nativePythonRunner": { "type": "boolean" },
        "customConfig": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "configMapName": { "type": "string" },
            "configMapKey": { "type": "string" }
          }
        },
        "resources": {
          "type": "object",
          "properties": {
            "requests": {
              "type": "object",
              "properties": {
                "cpu": { "type": "string" },
                "memory": { "type": "string" }
              }
            },
            "limits": {
              "type": "object",
              "properties": {
                "cpu": { "type": "string" },
                "memory": { "type": "string" }
              }
            }
          }
        },
        "extraEnv": {
          "type": "array",
          "items": { "type": "object" }
        }
      },
      "required": ["enabled"]
    },
    "queueMode": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "workerReplicaCount": { "type": "integer", "minimum": 1 }
      }
    },
    "service": {
      "type": "object",
      "properties": {
        "type": { "type": "string" },
        "port": { "type": "integer", "minimum": 1, "maximum": 65535 },
        "annotations": { "type": "object", "additionalProperties": true },
        "sessionAffinity": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "timeoutSeconds": { "type": "integer", "minimum": 1 }
          }
        }
      },
      "required": ["type", "port"]
    },
    "ingress": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "className": { "type": "string" },
        "annotations": { "type": "object", "additionalProperties": true },
        "hosts": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "host": { "type": "string", "minLength": 1 },
              "paths": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "path": { "type": "string", "minLength": 1 },
                    "pathType": { "type": "string", "minLength": 1 }
                  },
                  "required": ["path", "pathType"]
                },
                "minItems": 1
              }
            },
            "required": ["host", "paths"]
          }
        },
        "tls": { "type": "array" },
        "sticky": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "cookieName": { "type": "string" },
            "cookieExpires": { "type": "string" },
            "cookieMaxAge": { "type": "string" }
          }
        },
        "webhookProcessor": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "className": { "type": "string" },
            "annotations": { "type": "object", "additionalProperties": true },
            "tls": { "type": "array" }
          }
        }
      },
      "required": ["enabled", "hosts"]
    },
    "persistence": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "size": { "type": "string", "pattern": "^[0-9]+Gi$" },
        "accessModes": { "type": "array", "items": { "type": "string" } },
        "storageClassName": { "type": "string" },
        "existingClaim": { "type": "string" }
      },
      "required": ["enabled"]
    },
    "resources": {
      "type": "object",
      "properties": {
        "main": { "type": "object" },
        "worker": { "type": "object" }
      }
    },
    "nodeSelector": {
      "type": "object",
      "additionalProperties": { "type": "string" }
    },
    "tolerations": { "type": "array" },
    "affinity": { "type": "object" },
    "podAnnotations": { "type": "object", "additionalProperties": true },
    "podLabels": { "type": "object", "additionalProperties": true },
    "securityContext": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "fsGroup": { "type": "integer", "minimum": 0 },
        "runAsUser": { "type": "integer", "minimum": 0 },
        "runAsGroup": { "type": "integer", "minimum": 0 }
      }
    },
    "serviceAccount": {
      "type": "object",
      "properties": {
        "create": { "type": "boolean" },
        "name": { "type": "string" },
        "annotations": { "type": "object", "additionalProperties": true }
      }
    },
    "rbac": {
      "type": "object",
      "properties": { "create": { "type": "boolean" } }
    },
    "probes": {
      "type": "object",
      "properties": {
        "liveness": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "path": { "type": "string" },
            "initialDelaySeconds": { "type": "integer", "minimum": 0 },
            "periodSeconds": { "type": "integer", "minimum": 1 },
            "timeoutSeconds": { "type": "integer", "minimum": 1 },
            "failureThreshold": { "type": "integer", "minimum": 1 }
          }
        },
        "readiness": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "path": { "type": "string" },
            "initialDelaySeconds": { "type": "integer", "minimum": 0 },
            "periodSeconds": { "type": "integer", "minimum": 1 },
            "timeoutSeconds": { "type": "integer", "minimum": 1 },
            "failureThreshold": { "type": "integer", "minimum": 1 }
          }
        },
        "worker": {
          "type": "object",
          "properties": {
            "readiness": {
              "type": "object",
              "properties": {
                "enabled": { "type": "boolean" },
                "type": { 
                  "type": "string",
                  "enum": ["httpGet", "exec"]
                },
                "path": { "type": "string" },
                "port": { "type": "integer" },
                "command": { 
                  "type": "array",
                  "items": { "type": "string" }
                },
                "initialDelaySeconds": { "type": "integer", "minimum": 0 },
                "periodSeconds": { "type": "integer", "minimum": 1 },
                "timeoutSeconds": { "type": "integer", "minimum": 1 },
                "failureThreshold": { "type": "integer", "minimum": 1 }
              }
            },
            "liveness": {
              "type": "object",
              "properties": {
                "enabled": { "type": "boolean" },
                "type": {
                  "type": "string",
                  "enum": ["exec"],
                  "description": "Workers don't expose an HTTP endpoint; only exec probes are supported"
                },
                "command": {
                  "type": "array",
                  "items": { "type": "string" }
                },
                "initialDelaySeconds": { "type": "integer", "minimum": 0 },
                "periodSeconds": { "type": "integer", "minimum": 1 },
                "timeoutSeconds": { "type": "integer", "minimum": 1 },
                "failureThreshold": { "type": "integer", "minimum": 1 }
              }
            }
          }
        }
      }
    },
    "hpa": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "minReplicas": { "type": "integer", "minimum": 1 },
        "maxReplicas": { "type": "integer", "minimum": 1 },
        "targetCPUUtilizationPercentage": {
          "type": "integer",
          "minimum": 1,
          "maximum": 100
        },
        "targetMemoryUtilizationPercentage": {
          "type": "integer",
          "minimum": 1,
          "maximum": 100
        },
        "worker": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "minReplicas": { "type": "integer", "minimum": 1 },
            "maxReplicas": { "type": "integer", "minimum": 1 },
            "targetCPUUtilizationPercentage": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "targetMemoryUtilizationPercentage": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            }
          }
        }
      }
    },
    "webhook": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "url": { "type": "string" },
        "testUrl": { "type": "string" },
        "timeout": { 
          "type": "integer", 
          "minimum": 1000,
          "maximum": 600000,
          "description": "Webhook timeout in milliseconds (1s to 10min)"
        },
        "extraEnv": { 
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string", "minLength": 1 },
              "value": { "type": "string" }
            },
            "required": ["name", "value"]
          }
        }
      },
      "required": ["enabled"]
    },
    "license": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "activationKey": { "type": "string" },
        "existingSecret": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "key": { "type": "string" }
          }
        }
      },
      "required": ["enabled"]
    },
    "executions": {
      "type": "object",
      "properties": {
        "timeout": { "type": "integer" },
        "timeoutMax": { "type": "integer", "minimum": 1 },
        "data": {
          "type": "object",
          "properties": {
            "saveOnError": { 
              "type": "string",
              "enum": ["all", "none"]
            },
            "saveOnSuccess": { 
              "type": "string",
              "enum": ["all", "none"]
            },
            "saveOnProgress": { "type": "boolean" },
            "saveManualExecutions": { "type": "boolean" }
          }
        },
        "pruning": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "maxAge": { "type": "integer", "minimum": 1 },
            "maxCount": { "type": "integer", "minimum": 0 },
            "hardDeleteBuffer": { "type": "integer", "minimum": 1 },
            "hardDeleteInterval": { "type": "integer", "minimum": 1 },
            "softDeleteInterval": { "type": "integer", "minimum": 1 }
          }
        },
        "concurrency": {
          "type": "object",
          "properties": {
            "productionLimit": { "type": "integer" }
          }
        },
        "extraEnv": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string", "minLength": 1 },
              "value": { "type": "string" }
            },
            "required": ["name", "value"]
          }
        }
      }
    },
    "config": {
      "type": "object",
      "properties": {
        "timezone": { "type": "string" },
        "extraEnv": { "type": "array" },
        "extraEnvFrom": { "type": "array" }
      }
    },
    "secretRefs": {
      "type": "object",
      "properties": {
        "existingSecret": { "type": "string" },
        "env": {
          "type": "object",
          "additionalProperties": { "type": "string" }
        }
      }
    },
    "database": {
      "type": "object",
      "properties": {
        "type": { "type": "string", "enum": ["postgresdb", "sqlite"] },
        "useExternal": { "type": "boolean" },
        "host": { "type": "string" },
        "port": { "type": "integer" },
        "database": { "type": "string" },
        "user": { "type": "string" },
        "passwordSecret": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "key": { "type": "string" }
          },
          "required": ["name", "key"]
        }
      },
      "additionalProperties": true
    },
    "redis": {
      "type": "object",
      "properties": {
        "host": { "type": "string" },
        "port": { "type": "integer" },
        "username": { "type": "string" },
        "passwordSecret": {
          "type": ["object", "null"],
          "properties": {
            "name": { "type": ["string", "null"], "default": null },
            "key": { "type": ["string", "null"], "default": null }
          },
          "additionalProperties": false,
          "default": null
        },
        "database": { "type": "integer", "minimum": 0, "maximum": 15 },
        "timeout": { "type": "integer", "minimum": 1000 },
        "prefix": { "type": "string" },
        "tls": { "type": "boolean" },
        "dualstack": { "type": "boolean" },
        "clusterNodes": { "type": "string" },
        "worker": {
          "type": "object",
          "properties": {
            "timeout": { "type": "integer", "minimum": 1 },
            "lockDuration": { "type": "integer", "minimum": 1000 },
            "lockRenewTime": { "type": "integer", "minimum": 1000 },
            "stalledInterval": { "type": "integer", "minimum": 1000 },
            "maxStalledCount": { "type": "integer", "minimum": 1 }
          }
        },
        "healthCheck": {
          "type": "object",
          "properties": {
            "enabled": { "type": "boolean" },
            "port": { "type": "integer", "minimum": 1, "maximum": 65535 }
          }
        },
        "extraEnv": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string", "minLength": 1 },
              "value": { "type": "string" }
            },
            "required": ["name", "value"]
          }
        }
      }
    },
    "s3": {
      "type": "object",
      "properties": {
        "enabled": { "type": "boolean" },
        "bucket": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "region": { "type": "string" },
            "host": { "type": "string" }
          },
          "required": ["name", "region"]
        },
        "auth": {
          "type": "object",
          "properties": {
            "autoDetect": { "type": "boolean" },
            "accessKeyId": { "type": "string" },
            "secretAccessKeySecret": {
              "type": "object",
              "properties": {
                "name": { "type": "string" },
                "key": { "type": "string" }
              },
              "required": ["name", "key"]
            }
          }
        },
        "storage": {
          "type": "object",
          "properties": {
            "mode": { 
              "type": "string",
              "enum": ["filesystem", "s3"],
              "description": "Binary data storage mode"
            },
            "availableModes": {
              "type": "string",
              "description": "Available binary data modes (comma-separated)"
            },
            "forcePathStyle": { "type": "boolean" },
            "extraEnv": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string", "minLength": 1 },
                  "value": { "type": "string" }
                },
                "required": ["name", "value"]
              }
            }
          },
          "required": ["mode"]
        }
      },
      "required": ["enabled"]
    }
  },
  "allOf": [
    {
      "if": {
        "properties": {
          "multiMain": {
            "properties": { "enabled": { "const": true } },
            "required": ["enabled"]
          }
        }
      },
      "then": {
        "properties": {
          "queueMode": {
            "properties": { "enabled": { "const": true } },
            "required": ["enabled"]
          },
          "multiMain": {
            "properties": { "replicas": { "minimum": 2 } }
          }
        },
        "errorMessage": "multiMain.enabled=true requires queueMode.enabled=true and multiMain.replicas>=2"
      }
    },
    {
      "if": {
        "properties": {
          "queueMode": {
            "properties": { "enabled": { "const": true } },
            "required": ["enabled"]
          }
        }
      },
      "then": {
        "properties": {
          "queueMode": {
            "required": ["workerReplicaCount"]
          },
          "redis": {
            "type": "object",
            "properties": {
              "host": { "type": "string", "minLength": 1 },
              "passwordSecret": {
                "type": ["object", "null"],
                "properties": {
                  "name": { "type": ["string", "null"] },
                  "key": { "type": ["string", "null"] }
                },
                "additionalProperties": false,
                "default": null
              }
            },
            "required": ["host"]
          }
        },
        "errorMessage": "queueMode.enabled=true requires redis.host and queueMode.workerReplicaCount"
      }
    },
    {
      "if": {
        "properties": {
          "ingress": {
            "properties": { "enabled": { "const": true } },
            "required": ["enabled"]
          }
        }
      },
      "then": {
        "properties": {
          "ingress": { "properties": { "hosts": { "minItems": 1 } } }
        },
        "errorMessage": "ingress.enabled=true requires at least one hosts[] entry"
      }
    },
    {
      "if": {
        "properties": {
          "service": {
            "properties": {
              "sessionAffinity": {
                "properties": { "enabled": { "const": true } },
                "required": ["enabled"]
              }
            }
          }
        }
      },
      "then": {
        "properties": {
          "service": {
            "properties": {
              "sessionAffinity": { "required": ["timeoutSeconds"] }
            }
          }
        },
        "errorMessage": "service.sessionAffinity.enabled=true requires timeoutSeconds"
      }
    },
    {
      "if": {
        "properties": {
          "database": {
            "properties": { "type": { "const": "postgresdb" } },
            "required": ["type"]
          }
        }
      },
      "then": {
        "allOf": [
          {
            "if": {
              "properties": {
                "database": {
                  "properties": { "useExternal": { "const": true } },
                  "required": ["useExternal"]
                }
              }
            },
            "then": {
              "properties": {
                "database": {
                  "required": ["host", "port", "database", "user", "passwordSecret"]
                }
              },
              "errorMessage": "database.type=postgresdb & useExternal=true requires host, port, database, user and passwordSecret"
            }
          },
          {
            "if": {
              "properties": {
                "database": {
                  "properties": { "useExternal": { "const": false } },
                  "required": ["useExternal"]
                }
              }
            },
            "then": {
              "properties": {
                "database": {
                  "required": ["database", "user"]
                }
              },
              "errorMessage": "database.type=postgresdb & useExternal=false requires at least database and user (host/port/secret are provided by the in-cluster DB)"
            }
          }
        ]
      }
    },
    {
      "if": {
        "properties": {
          "database": {
            "properties": { "useExternal": { "const": false } },
            "required": ["useExternal"]
          }
        }
      },
      "then": {
        "properties": {
          "database": {
            "properties": { "type": { "const": "sqlite" } },
            "required": ["type"]
          },
          "queueMode": {
            "properties": { "enabled": { "const": false } },
            "required": ["enabled"]
          },
          "multiMain": {
            "properties": { "enabled": { "const": false } },
            "required": ["enabled"]
          }
        },
        "errorMessage": "useExternal=false enforces SQLite and disables queueMode and multiMain"
      }
    },
    {
      "if": {
        "properties": {
          "s3": {
            "properties": { "enabled": { "const": true } },
            "required": ["enabled"]
          }
        }
      },
      "then": {
        "properties": {
          "s3": {
            "properties": {
              "bucket": { "required": ["name", "region"] },
              "storage": { "required": ["mode"] }
            },
            "anyOf": [
              {
                "properties": {
                  "auth": {
                    "properties": { "autoDetect": { "const": true } },
                    "required": ["autoDetect"]
                  }
                }
              },
              {
                "properties": {
                  "auth": {
                    "required": ["accessKeyId", "secretAccessKeySecret"]
                  }
                }
              }
            ]
          }
        },
        "errorMessage": "s3.enabled=true requires bucket configuration and either autoDetect=true or explicit credentials"
      }
    }
  ],
  "additionalProperties": true
}
```

## File: `charts/n8n/values.yaml`
```yaml
# ----- Image -----
image:
  repository: docker.n8n.io/n8nio/n8n
  tag: "2.12.2"
  pullPolicy: IfNotPresent

# ----- Names -----
nameOverride: ""
fullnameOverride: ""

# ----- Queue mode -----
# Two deployment modes are supported:
#   1. Queue mode (enabled: true, default) — main + workers + optional webhook processors.
#      Requires external PostgreSQL and Redis.
#   2. Standalone mode (enabled: false) — single main pod with SQLite.
#      No workers, no Redis, no external database. Requires persistence for SQLite storage.
queueMode:
  enabled: true
  workerReplicaCount: 2
  # Worker concurrency (number of jobs each worker can handle simultaneously)
  workerConcurrency: 10

# ----- Webhook processors (optional scaling layer) -----
webhookProcessor:
  # Enable dedicated webhook processing pods for high-throughput webhook scenarios
  enabled: false
  replicaCount: 2
  # Disable webhook processing in main process when webhook processors are enabled
  disableProductionWebhooksOnMainProcess: true

# ----- Multi-main (optional, requires queue mode) -----
multiMain:
  enabled: false
  replicas: 2
  antiAffinity:
    type: preferred
  topologySpreadConstraints:
    enabled: false
    maxSkew: 1
    whenUnsatisfiable: ScheduleAnyway
  # Multi-main setup configuration (requires enterprise license)
  setup:
    keyTtl: 10                               # <-- Leader key TTL (seconds)
    checkInterval: 3                         # <-- Leader check interval (seconds)

# ----- Task Runners (external mode with sidecar containers) -----
taskRunners:
  # Enable task runners for executing user-provided JavaScript and Python code
  # When enabled, a sidecar container (n8nio/runners) is added to main and worker pods
  enabled: false

  # Task runner image configuration
  image:
    repository: n8nio/runners
    # Tag must match n8n version
    # Leave empty to automatically use the same tag as the main n8n image
    # Set explicitly only if you need a different version (not recommended)
    tag: ""
    pullPolicy: IfNotPresent

  # Task runner mode (only external mode is supported in this chart)
  mode: external

  # Authentication token for task runners to connect to the broker
  # This should be a random secure shared secret
  # You can generate one with: openssl rand -base64 32
  authToken:
    # Use existing secret for auth token
    existingSecret: ""
    existingSecretKey: ""
    # Or provide the token directly (not recommended for production)
    value: ""

  # Task broker configuration (runs within n8n main/worker containers)
  broker:
    # Listen address for the task broker (0.0.0.0 allows external connections from sidecar)
    listenAddress: "0.0.0.0"
    # Port for task broker to listen on
    port: 5679

  # Launcher configuration
  launcher:
    # Log level for the launcher (debug, info, warn, error)
    logLevel: info
    # Number of seconds of inactivity before shutting down task runner process
    # The launcher will automatically start the runner again when there are new tasks
    # Set to 0 to disable automatic shutdown
    autoShutdownTimeout: 15

  # Enable native Python runner (required for Python support, currently in beta)
  nativePythonRunner: true

  # Custom launcher configuration file
  # You can mount a custom n8n-task-runners.json to allowlist additional packages
  customConfig:
    enabled: false
    # ConfigMap name containing the custom launcher config
    configMapName: ""
    # Key in the ConfigMap containing the config file
    configMapKey: "n8n-task-runners.json"

  # Resource limits for task runner sidecar containers
  resources:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 500m
      memory: 512Mi

  # Additional environment variables for task runners
  extraEnv: []
  # Example:
  # extraEnv:
  #   - name: N8N_RUNNERS_LAUNCHER_LOG_LEVEL
  #     value: debug

# ----- Main replicas (when multi-main is disabled) -----
replicaCount: 1

# ----- Service -----
service:
  type: ClusterIP
  port: 5678
  annotations: {}
  main:
    annotations: {}
  webhookProcessor:
    annotations: {}
  sessionAffinity:
    enabled: false
    timeoutSeconds: 10800

# ----- Ingress -----
ingress:
  enabled: false
  sticky:
    enabled: false
    cookieName: n8n_affinity
    cookieExpires: "172800"  # 2 days in seconds
    cookieMaxAge: "172800"   # 2 days in seconds
  hosts:
    - host: n8n.example.com   # <-- Change to your actual domain
      paths:
        - path: /
          pathType: Prefix
  # Separate Ingress for webhook processor pods (requires webhookProcessor.enabled=true)
  webhookProcessor:
    enabled: false
    className: ""
    annotations: {}
    tls: []

# ----- Persistence -----
persistence:
  enabled: false
  accessModes: ["ReadWriteOnce"]
  size: 10Gi
  storageClassName: ""

# ----- External Volumes -----
extraVolumes: []
# Examples:
# extraVolumes:
#   - name: ssl-certs
#     secret:
#       secretName: ssl-certificates
#   - name: custom-config
#     configMap:
#       name: n8n-config

extraVolumeMounts: []
# Examples:
# extraVolumeMounts:
#   - name: ssl-certs
#     mountPath: /usr/local/share/ca-certificates
#     readOnly: true
#   - name: custom-config
#     mountPath: /app/config
#     readOnly: true

# ----- Resources -----
resources:
  main:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: "1"
      memory: 1Gi
  worker:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: "1"
      memory: 1Gi
  webhookProcessor:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 500m
      memory: 512Mi

# ----- Node placement -----
nodeSelector: {}
tolerations: []
affinity: {}

# ----- Security -----
# Note: readOnlyRootFilesystem is intentionally not set. n8n writes to
# ~/.n8n/, /tmp/, and other paths at runtime. Enabling it would require
# extensive volumeMount overrides and is not practical for this workload.
securityContext:
  enabled: true
  fsGroup: 1000
  runAsUser: 1000
  runAsGroup: 1000

# ----- RBAC ServiceAccount & Network Policy -----
rbac:
  create: true

serviceAccount:
  # Create a new service account for n8n pods
  create: true
  # Service account name - supports multiple configuration scenarios:
  #
  # 1. Create new service account (default):
  #    create: true
  #    name: "n8n"  # <-- Custom name, or leave empty to use chart fullname
  #
  # 2. Use existing/managed service account (e.g., created by Terraform):
  #    create: false
  #    name: "my-terraform-service-account"
  #
  # 3. Use no service account (pods run with default permissions):
  #    create: false
  #    name: ""  # <-- Empty or omit entirely
  name: n8n
  # AWS IAM Role ARN for IRSA (IAM Roles for Service Accounts)
  # Required when s3.auth.autoDetect=true for AWS S3 access
  awsRoleArn: ""
  # Additional annotations for the service account
  annotations: {}

networkPolicy:
  enabled: false

# ----- Health checks -----
probes:
  liveness:
    enabled: true
    path: /healthz
    initialDelaySeconds: 30
    periodSeconds: 20
    timeoutSeconds: 5
    failureThreshold: 6
  readiness:
    enabled: true
    path: /healthz
    initialDelaySeconds: 10
    periodSeconds: 10
    timeoutSeconds: 3
    failureThreshold: 6
  # Worker-specific probes (workers don't have HTTP endpoints)
  worker:
    readiness:
      enabled: true
      # Custom readiness probe that checks if worker is ready
      type: "exec"                           # <-- Use exec probe instead of HTTP
      command:
        - "/bin/sh"
        - "-c"
        - "pgrep -f 'n8n worker' > /dev/null"
      initialDelaySeconds: 30
      periodSeconds: 10
      timeoutSeconds: 3
      failureThreshold: 6
    liveness:
      enabled: true
      # Check if n8n worker process is still running
      type: "exec"
      command:
        - "/bin/sh"
        - "-c"
        - "pgrep -f 'n8n worker' > /dev/null"
      initialDelaySeconds: 60
      periodSeconds: 30
      timeoutSeconds: 5
      failureThreshold: 3

# ----- Lifecycle (graceful shutdown) -----
lifecycle:
  # Main pods lifecycle configuration
  main:
    terminationGracePeriodSeconds: 60
    preStop:
      enabled: true
      # Sleep to allow pod to be removed from service endpoints before SIGTERM
      command:
        - "/bin/sh"
        - "-c"
        - "sleep 10"
  # Worker pods lifecycle configuration
  worker:
    terminationGracePeriodSeconds: 60
    preStop:
      enabled: true
      # Sleep to allow current workflow executions to complete
      command:
        - "/bin/sh"
        - "-c"
        - "sleep 10"
  # Webhook processor pods lifecycle configuration
  webhookProcessor:
    terminationGracePeriodSeconds: 60
    preStop:
      enabled: true
      # Sleep to allow current webhook requests to complete
      command:
        - "/bin/sh"
        - "-c"
        - "sleep 10"

# ----- Autoscaling -----
hpa:
  # Main pods autoscaling (UI/API pods)
  main:
    enabled: false
    minReplicas: 1
    maxReplicas: 5
    targetCPUUtilizationPercentage: 80
  # Worker pods autoscaling (execution pods)
  worker:
    enabled: false
    minReplicas: 2
    maxReplicas: 20
    targetCPUUtilizationPercentage: 70
  # Webhook processor pods autoscaling (webhook handling)
  webhookProcessor:
    enabled: false
    minReplicas: 2
    maxReplicas: 50
    targetCPUUtilizationPercentage: 60

# ----- KEDA (Kubernetes Event-Driven Autoscaler) -----
# When enabled, creates KEDA ScaledObjects instead of built-in HPAs for workers/webhooks.
# This allows scaling based on Redis queue length rather than CPU utilization.
# Requires KEDA to be installed in the cluster: https://keda.sh
keda:
  enabled: false
  worker:
    pollingInterval: 15
    cooldownPeriod: 300
    minReplicaCount: 2
    maxReplicaCount: 20
    triggers:
      - type: redis
        metadata:
          # Redis address (auto-derived from redis.host:redis.port if empty)
          address: ""
          # Bull queue waiting list key
          listName: "bull:default:wait"
          # Target queue length per worker replica
          listLength: "5"
        authenticationRef:
          # Name of a TriggerAuthentication resource for Redis auth (optional)
          name: ""
  webhookProcessor:
    enabled: false
    pollingInterval: 15
    cooldownPeriod: 120
    minReplicaCount: 2
    maxReplicaCount: 50
    triggers: []

# ----- Pod Disruption Budget -----
pdb:
  enabled: true
  minAvailable: 1

# ----- Webhook config -----
webhook:
  # Enable webhook functionality
  enabled: true
  # Custom webhook URL base domain (if not set, will use ingress host)
  # Format: https://your-domain.com (n8n adds /webhook path automatically)
  url: ""
  # Timeout for webhook requests in milliseconds
  timeout: 120000
  # Additional webhook environment variables
  extraEnv: []

# ----- Executions config -----
executions:
  # Execution timeout settings
  timeout: -1                                    # <-- Default timeout in seconds (-1 = disabled)
  timeoutMax: 3600                              # <-- Maximum timeout users can set
  # Data persistence settings
  data:
    saveOnError: "all"                          # <-- Save data on error (all, none)
    saveOnSuccess: "all"                        # <-- Save data on success (all, none)
    saveOnProgress: false                       # <-- Save progress for each node
    saveManualExecutions: true                  # <-- Save manual execution data
  # Data pruning settings
  pruning:
    enabled: true                               # <-- Enable execution data pruning
    maxAge: 336                                 # <-- Max execution age in hours (14 days)
    maxCount: 10000                            # <-- Max executions to keep (0 = no limit)
    hardDeleteBuffer: 1                         # <-- Buffer hours before hard delete
    hardDeleteInterval: 15                      # <-- Hard delete interval in minutes
    softDeleteInterval: 60                      # <-- Soft delete interval in minutes
  # Concurrency settings
  concurrency:
    productionLimit: -1                         # <-- Max concurrent production executions (-1 = disabled)
  # Additional execution environment variables
  extraEnv: []

# ----- App config -----
config:
  timezone: UTC
  # Additional environment variables for n8n container
  # All n8n environment variables can be set here including:
  # Proxy: HTTP_PROXY, HTTPS_PROXY, ALL_PROXY, NO_PROXY
  # Core: N8N_EDITOR_BASE_URL, N8N_CONFIG_FILES, N8N_USER_FOLDER, etc.
  # Features: N8N_DISABLE_UI, N8N_PREVIEW_MODE, N8N_TEMPLATES_ENABLED, etc.
  # Network: N8N_LISTEN_ADDRESS, N8N_SSL_KEY, N8N_SSL_CERT, etc.
  # Telemetry: N8N_DIAGNOSTICS_ENABLED, N8N_VERSION_NOTIFICATIONS_ENABLED, etc.
  # API: N8N_PUBLIC_API_DISABLED, N8N_PUBLIC_API_ENDPOINT, etc.
  # System: N8N_GRACEFUL_SHUTDOWN_TIMEOUT, N8N_PROXY_HOPS, etc.
  # Dev: N8N_DEV_RELOAD, N8N_REINSTALL_MISSING_PACKAGES, etc.
  # See documentation for complete list of supported variables
  extraEnv: []
  # Example:
  # extraEnv:
  #   - name: HTTP_PROXY
  #     value: "http://proxy.example.com:8080"
  #   - name: N8N_EDITOR_BASE_URL
  #     value: "https://n8n.example.com"
  #   - name: N8N_DISABLE_UI
  #     value: "false"
  extraEnvFrom: []

# ----- License (for n8n Enterprise) -----
license:
  # Set to true if using n8n Enterprise
  enabled: false
  # License activation key (leave empty to use secret)
  activationKey: ""
  # Or reference existing secret containing the license key
  existingSecret:
    name: ""                           # <-- K8s Secret name
    key: "license-key"                 # <-- Key inside the secret

# ----- Secrets -----
secretRefs:
  existingSecret: ""
  env:
    N8N_ENCRYPTION_KEY: "change-me-to-a-long-random-key"
    N8N_HOST: "n8n.example.com"  # <-- Change to your actual domain
    N8N_PORT: "5678"
    N8N_PROTOCOL: "http"

# ----- Database (PostgreSQL - required for queue mode) -----
database:
  type: postgresdb
  # External database is required for queue mode
  useExternal: true
  host: "your-postgres-hostname"     # <-- Change to your actual PostgreSQL host
  port: 5432
  database: n8n
  schema: "public"                   # <-- PostgreSQL schema name
  user: n8n
  passwordSecret:
    name: "n8n-db-password"          # <-- K8s Secret name
    key: "password"                  # <-- Key inside the secret
  # SSL configuration
  ssl:
    enabled: false                   # <-- Enable SSL connection
    ca: ""                           # <-- Path to CA certificate file
    cert: ""                         # <-- Path to client certificate file
    key: ""                          # <-- Path to client key file
    rejectUnauthorized: true         # <-- Reject unauthorized SSL connections

# ----- Redis (required for queue mode) -----
redis:
  # Redis is required for queue mode
  enabled: true
  useExternal: true
  host: "your-redis-hostname"                      # <-- Change to your actual Redis host
  port: 6379
  # Redis authentication
  username: ""                                     # <-- Redis username (Redis 6+)
  passwordSecret: null
  # Advanced Redis settings
  database: 0                                      # <-- Redis database number
  timeout: 10000                                   # <-- Redis timeout threshold (ms)
  prefix: ""                                       # <-- Queue key prefix
  tls: false                                       # <-- Enable TLS (required for AWS ElastiCache and other managed Redis services)
  dualstack: false                                 # <-- Enable dual-stack (IPv4/IPv6)
  # Redis Cluster support (comma-separated list of host:port)
  clusterNodes: ""                                 # <-- For Redis Cluster mode
  # Queue worker settings
  worker:
    timeout: 30                                    # <-- Worker shutdown timeout (seconds)
    lockDuration: 60000                            # <-- Worker lease duration (ms)
    lockRenewTime: 10000                           # <-- Lock renewal frequency (ms)
    stalledInterval: 30000                         # <-- Stalled job check interval (ms)
    maxStalledCount: 1                             # <-- Max stalled job retries
  # Health check settings
  healthCheck:
    enabled: false                                 # <-- Enable queue health checks
    port: 5678                                     # <-- Health check port
  # Additional Redis environment variables
  extraEnv: []

# ----- S3 External Storage (required for queue mode with binary data) -----
s3:
  enabled: false
  # S3 bucket configuration
  bucket:
    name: ""                                   # <-- S3 bucket name
    region: ""                                 # <-- S3 region (use "auto" if not required)
    host: ""                                   # <-- S3 endpoint (optional for AWS S3)
  # Authentication
  auth:
    autoDetect: false                          # <-- Use AWS credential provider chain (requires serviceAccount.awsRoleArn)
    accessKeyId: ""                            # <-- S3 access key ID (not needed if autoDetect=true)
    secretAccessKeySecret:                     # <-- Secret containing S3 secret access key (not needed if autoDetect=true)
      name: ""                                 # <-- K8s Secret name
      key: ""                                  # <-- Key inside the secret
  # Storage configuration
  storage:
    # Binary data storage mode (filesystem or s3 (filesystem))
    mode: "filesystem"
    # Available binary data modes (comma-separated ex: filesystem,s3)
    availableModes: "filesystem"              # <-- Available storage modes for n8n
    # S3 specific settings
    forcePathStyle: false                      # <-- Force path-style URLs (for S3-compatible providers)
    # Additional S3 environment variables
    extraEnv: []
```

## File: `charts/n8n/examples/README.md`
```markdown
# n8n Helm Chart Examples

This directory contains common configuration examples for different deployment scenarios. Each example shows a complete values file with explanations of the key settings.

## Available Examples

### Community Examples (No License Required)
- **[standalone.yaml](./standalone.yaml)** - Single pod with SQLite, no external dependencies
- **[minimal.yaml](./minimal.yaml)** - Single main pod with external PostgreSQL and Redis
- **[minimal-with-docker.yaml](./minimal-with-docker.yaml)** - Quick testing with Docker containers

### Community Examples (Task Runners)
- **[task-runners.yaml](./task-runners.yaml)** - Queue mode with task runner sidecars for JavaScript/Python execution

### Community Examples (KEDA Autoscaling)
- **[keda-autoscaling.yaml](./keda-autoscaling.yaml)** - Redis queue-length worker scaling with KEDA

### Enterprise Examples (License Required)
- **[production-s3.yaml](./production-s3.yaml)** - Production setup with multi-main, webhooks, S3 storage, and autoscaling
- **[multi-main-queue.yaml](./multi-main-queue.yaml)** - Multi-main and queue mode configuration


## Important Notice

### External Services
**Queue mode** (default) requires external PostgreSQL and Redis services — this chart does not bundle them.
**Standalone mode** (`queueMode.enabled: false`) uses SQLite with a PersistentVolumeClaim and has no external dependencies — see `standalone.yaml`.

### License Requirements
- **Multi-main setup** (`multiMain.enabled: true`) requires an n8n Enterprise license
- **Community Edition** users should use single main pod configurations

## Quick Start

### 1. Create Required Secrets
```bash
./examples/create-secrets.sh
```

### 2. Choose Your Example
Select the example that best matches your use case from the list above.

### 3. Deploy
```bash
# Copy and customize an example
cp examples/production-s3.yaml my-values.yaml
# Edit my-values.yaml with your settings

# Deploy with Helm
helm install n8n ./charts/n8n -f my-values.yaml
```

For quick testing with Docker:
```bash
# Start PostgreSQL
docker run -d --name n8n-postgres -e POSTGRES_DB=n8n -e POSTGRES_USER=n8n -e POSTGRES_PASSWORD=n8npassword -p 5432:5432 postgres:15

# Start Redis
docker run -d --name n8n-redis -p 6379:6379 redis:7-alpine
```

## 🚀 Quick Start

1. **Set up external services** — PostgreSQL and Redis for queue mode (not needed for standalone mode)
2. Choose the example that matches your scenario
3. Copy the values file: `cp examples/production-s3.yaml my-values.yaml`
4. Customize the values for your environment
5. Create required secrets: `./examples/create-secrets.sh`
6. Deploy: `helm install n8n ./charts/n8n -f my-values.yaml`

## 📋 Configuration Checklist

Before deploying, ensure you have:

- [ ] **Secrets created** (database password, encryption key, etc.)
- [ ] **External services** (PostgreSQL, Redis) if using queue mode
- [ ] **Storage configuration** (S3, GCS, Azure) if using external storage
- [ ] **Network access** configured for your cluster
- [ ] **Resource limits** appropriate for your workload

## 🔧 Customization Guide

### Essential Settings
```yaml
# Always required
secretRefs:
  existingSecret: "n8n-core-secrets"

# Queue mode only (not needed for standalone mode)
database:
  host: "your-postgres-host"
  passwordSecret:
    name: "your-secret"
    key: "password"

redis:
  host: "your-redis-host"
```

### Scaling Configuration
```yaml
# For production workloads
queueMode:
  enabled: true
  workerReplicaCount: 5

multiMain:
  enabled: true
  replicas: 2

# Optional: Dedicated webhook processors (requires load balancer routing)
webhookProcessor:
  enabled: true
  replicaCount: 2
  disableProductionWebhooksOnMainProcess: true

hpa:
  main:
    enabled: true
    maxReplicas: 5
  worker:
    enabled: true 
    maxReplicas: 20
```

### Storage Configuration
```yaml
# S3 Storage (AWS only) - choose authentication method:
s3:
  enabled: true
  bucket:
    name: "your-bucket"
    region: "your-region"
  auth:
    # Option 1: IRSA (recommended for AWS EKS)
    autoDetect: true  # Only works with AWS S3
    
    # Option 2: Access Keys
    # autoDetect: false
    # accessKeyId: "YOUR_ACCESS_KEY"
    # secretAccessKeySecret:
    #   name: "s3-credentials"
    #   key: "secret-access-key"

# Service account (required for IRSA authentication)
serviceAccount:
  awsRoleArn: "arn:aws:iam::ACCOUNT:role/n8n-s3-role"  # Only for autoDetect: true
```

## Troubleshooting

### Common Issues

**Deployment fails with schema validation:**
- Ensure `queueMode.enabled: true` when using `multiMain.enabled: true`
- Set `multiMain.replicas >= 2` when multi-main is enabled

**Connection issues:**
- Enable session affinity: `service.sessionAffinity.enabled: true`
- Check database SSL settings if using cloud databases

**Storage issues:**
- Verify S3 bucket permissions and region
- For IRSA, ensure the service account has the correct role ARN

**Performance issues:**
- Increase worker replicas: `queueMode.workerReplicaCount`
- Enable HPA for automatic scaling
- Consider webhook processors for high webhook throughput

## Webhook Processors

Webhook processors provide dedicated pods for handling production webhooks, improving performance by separating webhook traffic from UI/API workload.

### Configuration Options

**Disabled (Default)**:
```yaml
webhookProcessor:
  enabled: false
```

**Enabled with Dedicated Processing**:
```yaml
webhookProcessor:
  enabled: true
  replicaCount: 2
  disableProductionWebhooksOnMainProcess: true
```

### Load Balancer Requirements

When `disableProductionWebhooksOnMainProcess: true`, configure your load balancer to route:
- `/webhook/*` → webhook processor service (production webhooks)
- `/webhook-test/*` → main service (test webhooks)  
- `/*` → main service (UI, API, everything else)

### Testing
```bash
curl -i http://your-domain/webhook/test-id      # Should reach webhook processor
curl -i http://your-domain/webhook-test/test-id # Should reach main service
```

**Webhook processor returns JSON errors. Main service returns JSON errors or HTML. Wrong routing returns "Cannot POST" errors.**

## Additional Resources

- [n8n Documentation](https://docs.n8n.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
```

## File: `charts/n8n/examples/create-secrets.sh`
```bash
#!/bin/bash
# n8n Helm Chart - Secret Creation Script
# This script helps create the required Kubernetes secrets for n8n

set -e

echo "n8n Secrets Creation Script"
echo "================================"
echo

prompt_with_default() {
    local prompt="$1"
    local default="$2"
    local var_name="$3"

    read -p "$prompt [$default]: " input
    printf -v "$var_name" '%s' "${input:-$default}"
}

prompt_secret() {
    local prompt="$1"
    local var_name="$2"

    read -s -p "$prompt: " input
    echo
    printf -v "$var_name" '%s' "$input"
}

echo "This script will create the following secrets:"
echo "  • n8n-core-secrets (encryption key, host, protocol)"
echo "  • n8n-db-secret (database password)"
echo "  • s3-credentials (AWS S3 secret key, optional)"
echo

if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl is not installed or not in PATH"
    exit 1
fi

if ! kubectl cluster-info &> /dev/null; then
    echo "❌ Cannot connect to Kubernetes cluster"
    echo "   Please ensure kubectl is configured correctly"
    exit 1
fi

echo "✅ Connected to Kubernetes cluster: $(kubectl config current-context)"
echo

echo "Please provide the following information:"
echo

echo "=== Core n8n Configuration ==="
prompt_with_default "n8n host (domain/IP where n8n will be accessible)" "localhost" "N8N_HOST"
prompt_with_default "n8n port" "5678" "N8N_PORT"
prompt_with_default "n8n protocol (http/https)" "http" "N8N_PROTOCOL"

N8N_ENCRYPTION_KEY=$(openssl rand -base64 32)
echo "Generated new encryption key: ${N8N_ENCRYPTION_KEY:0:16}..."

echo

echo "=== Database Configuration ==="
prompt_secret "Database password (will be hidden)" "DB_PASSWORD"

echo

echo "=== S3 Configuration (Optional) ==="
echo "Do you want to configure S3 credentials? (y/N)"
read -p "Configure S3? [N]: " configure_s3

if [[ "$configure_s3" =~ ^[Yy]$ ]]; then
    prompt_secret "AWS Secret Access Key (will be hidden)" "AWS_SECRET_ACCESS_KEY"
    CREATE_S3_SECRET=true
else
    CREATE_S3_SECRET=false
fi

echo


echo "  Review your configuration:"
echo "  Host: $N8N_HOST"
echo "  Port: $N8N_PORT"  
echo "  Protocol: $N8N_PROTOCOL"
echo "  Encryption key: Generated"
echo "  Database password: [HIDDEN]"
if [ "$CREATE_S3_SECRET" = true ]; then
    echo "  S3 secret key: [HIDDEN]"
fi

echo
read -p "Create these secrets? (y/N): " confirm

if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "   Cancelled"
    exit 0
fi

echo
echo "   Creating secrets..."

# Create core secrets
echo "Creating n8n-core-secrets..."
kubectl create secret generic n8n-core-secrets \
    --from-literal=N8N_ENCRYPTION_KEY="$N8N_ENCRYPTION_KEY" \
    --from-literal=N8N_HOST="$N8N_HOST" \
    --from-literal=N8N_PORT="$N8N_PORT" \
    --from-literal=N8N_PROTOCOL="$N8N_PROTOCOL" \
    --dry-run=client -o yaml | kubectl apply -f -

# Create database secret
echo "Creating n8n-db-secret..."
kubectl create secret generic n8n-db-secret \
    --from-literal=password="$DB_PASSWORD" \
    --dry-run=client -o yaml | kubectl apply -f -

# Create S3 secret if requested
if [ "$CREATE_S3_SECRET" = true ]; then
    echo "Creating s3-credentials..."
    kubectl create secret generic s3-credentials \
        --from-literal=secret-access-key="$AWS_SECRET_ACCESS_KEY" \
        --dry-run=client -o yaml | kubectl apply -f -
fi

echo
echo "   Secrets created successfully!"
echo

# Show what was created
echo "  Created secrets:"
kubectl get secrets n8n-core-secrets n8n-db-secret $([ "$CREATE_S3_SECRET" = true ] && echo "s3-credentials") 2>/dev/null || true

echo
echo "  Next steps:"
echo "  1. Choose a values file from the examples/ directory"
echo "  2. Customize it for your environment"
echo "  3. Deploy with: helm install n8n ./charts/n8n -f your-values.yaml"
echo

# Save encryption key to file for backup
echo "   IMPORTANT: Save your encryption key!"
echo "   Your encryption key has been saved to: ./n8n-encryption-key.txt"
echo "   Keep this file safe - you'll need it if you reinstall n8n"
echo "$N8N_ENCRYPTION_KEY" > ./n8n-encryption-key.txt
chmod 600 ./n8n-encryption-key.txt

echo
echo "   Security reminder:"
echo "   • Keep your encryption key safe and backed up"
echo "   • Don't commit secrets to version control" 
echo "   • Consider using external secret management in production"
echo "   • Rotate secrets regularly"
```

## File: `charts/n8n/examples/keda-autoscaling.yaml`
```yaml
# KEDA-Based Autoscaling
# This example demonstrates scaling workers based on Redis queue length using KEDA,
# instead of the built-in CPU-based HPA.
#
# Prerequisites:
#   - KEDA installed in the cluster: helm install keda kedacore/keda --namespace keda-system --create-namespace
#   - External PostgreSQL and Redis (queue mode)
#
# When keda.enabled is true, the built-in worker/webhook HPAs are automatically disabled.

queueMode:
  enabled: true
  workerReplicaCount: 2
  workerConcurrency: 10

# Disable built-in HPA (KEDA takes over scaling)
hpa:
  worker:
    enabled: false

# KEDA autoscaling configuration
keda:
  enabled: true
  worker:
    pollingInterval: 15       # How often KEDA checks the queue (seconds)
    cooldownPeriod: 300        # Wait time before scaling down (seconds)
    minReplicaCount: 2
    maxReplicaCount: 20
    triggers:
      - type: redis
        metadata:
          # Leave empty to auto-derive from redis.host:redis.port
          address: ""
          # Bull queue key for waiting jobs
          listName: "bull:default:wait"
          # Scale up when queue length exceeds 5 per replica
          listLength: "5"
        authenticationRef:
          # Reference a TriggerAuthentication if Redis requires auth
          # See: https://keda.sh/docs/latest/concepts/authentication/
          name: ""

# External database
database:
  type: postgresdb
  useExternal: true
  host: "your-postgres-host.com"
  port: 5432
  database: n8n
  schema: "public"
  user: n8n
  passwordSecret:
    name: "n8n-db-secret"
    key: "password"

# External Redis
redis:
  enabled: true
  useExternal: true
  host: "your-redis-host.com"
  port: 6379

# Core secrets
secretRefs:
  existingSecret: "n8n-core-secrets"
```

## File: `charts/n8n/examples/minimal-with-docker.yaml`
```yaml
# Minimal n8n with Docker External Services
# This example shows a minimal setup using Docker containers for external services
# Perfect for quick testing and development
#
# Prerequisites: Start external services with Docker
# docker run -d --name n8n-postgres -e POSTGRES_DB=n8n -e POSTGRES_USER=n8n -e POSTGRES_PASSWORD=n8npassword -p 5432:5432 postgres:15
# docker run -d --name n8n-redis -p 6379:6379 redis:7-alpine

# Basic queue mode (minimum required)
queueMode:
  enabled: true
  workerReplicaCount: 1
  workerConcurrency: 5

# Minimal multi-main (required by schema)
# multiMain:
#   enabled: true  # Requires n8n Enterprise license
#   replicas: 2

# External PostgreSQL (Docker container)
database:
  type: postgresdb
  useExternal: true
  host: "host.docker.internal"  # For Docker Desktop, use "localhost" for direct connection
  port: 5432
  database: n8n
  schema: "public"               # PostgreSQL schema name
  user: n8n
  passwordSecret:
    name: "n8n-db-secret"
    key: "password"

# External Redis (Docker container)
redis:
  enabled: true
  useExternal: true
  host: "host.docker.internal"  # For Docker Desktop, use "localhost" for direct connection  
  port: 6379

# Core secrets (you must create this secret)
secretRefs:
  existingSecret: "n8n-core-secrets"

# Service for local access
service:
  type: ClusterIP
  port: 5678
  sessionAffinity:
    enabled: true

# Minimal resources
resources:
  main:
    requests:
      memory: "256Mi"
      cpu: "200m"
    limits:
      memory: "512Mi"
      cpu: "500m"
  worker:
    requests:
      memory: "128Mi"
      cpu: "100m"
    limits:
      memory: "256Mi"
      cpu: "300m"

# Basic configuration  
config:
  timezone: UTC
  extraEnv:
    # Local development settings
    - name: N8N_LOG_LEVEL
      value: "debug"
    - name: WEBHOOK_URL
      value: "http://localhost:8080/webhook"
    - name: N8N_EDITOR_BASE_URL
      value: "http://localhost:8080"

# Service account
serviceAccount:
  create: true

# ---
# Quick Setup Instructions:
# 
# 1. Start external services:
#    docker run -d --name n8n-postgres -e POSTGRES_DB=n8n -e POSTGRES_USER=n8n -e POSTGRES_PASSWORD=n8npassword -p 5432:5432 postgres:15
#    docker run -d --name n8n-redis -p 6379:6379 redis:7-alpine
#
# 2. Create secrets:
#    ./examples/create-secrets.sh
#    # When prompted for database password, use: n8npassword
#
# 3. Deploy:
#    helm install n8n-minimal ./charts/n8n -f examples/minimal-with-docker.yaml
#
# 4. Access:
#    kubectl port-forward service/n8n-minimal-main 8080:5678
#    Open: http://localhost:8080
#
# 5. Cleanup:
#    helm uninstall n8n-minimal
#    docker stop n8n-postgres n8n-redis
#    docker rm n8n-postgres n8n-redis
```

## File: `charts/n8n/examples/minimal.yaml`
```yaml
# Minimal n8n Configuration
# This example shows the absolute minimum configuration needed to run n8n
# 
# IMPORTANT: This chart requires external PostgreSQL and Redis
# You must set up these services before deploying n8n
# 
# For quick testing, you can use Docker:
# docker run -d --name postgres -e POSTGRES_DB=n8n -e POSTGRES_USER=n8n -e POSTGRES_PASSWORD=password -p 5432:5432 postgres:15
# docker run -d --name redis -p 6379:6379 redis:7-alpine
#
# Use this as a starting point for development or testing

# Basic deployment settings
queueMode:
  enabled: true
  workerReplicaCount: 1
  workerConcurrency: 5

# Database configuration (MUST be external)
database:
  type: postgresdb
  useExternal: true  # Chart only supports external databases
  host: "your-postgres-host.com"
  port: 5432
  database: n8n
  schema: "public"   # PostgreSQL schema name
  user: n8n
  passwordSecret:
    name: "n8n-db-secret"
    key: "password"

# Redis configuration (MUST be external)
redis:
  enabled: true
  useExternal: true  # Chart only supports external Redis
  host: "your-redis-host.com"
  port: 6379

# Core secrets (you must create this secret manually)
secretRefs:
  existingSecret: "n8n-core-secrets"

# Basic service configuration
service:
  type: ClusterIP
  port: 5678

# Resource limits (adjust based on your needs)
resources:
  requests:
    memory: "256Mi"
    cpu: "200m"
  limits:
    memory: "512Mi"
    cpu: "500m"

# Storage (filesystem by default, S3 recommended for production)
# This chart uses filesystem storage by default
# For production, configure S3 storage (see other examples)

# Basic configuration
config:
  timezone: UTC
```

## File: `charts/n8n/examples/multi-main-queue.yaml`
```yaml
# Multi-main and Queue Mode Configuration
# This example demonstrates multi-main setup with queue mode (requires Enterprise license)
# Shows basic multi-main configuration without cloud-specific features

# Multi-main for high availability (Enterprise feature)
multiMain:
  enabled: true
  replicas: 3

queueMode:
  enabled: true
  workerReplicaCount: 10
  workerConcurrency: 20

webhookProcessor:
  enabled: true
  replicaCount: 5
  disableProductionWebhooksOnMainProcess: true

hpa:
  main:
    enabled: true
    minReplicas: 3
    maxReplicas: 20
    targetCPUUtilizationPercentage: 60
  worker:
    enabled: true
    minReplicas: 10
    maxReplicas: 100
    targetCPUUtilizationPercentage: 70
  webhookProcessor:
    enabled: true
    minReplicas: 5
    maxReplicas: 50
    targetCPUUtilizationPercentage: 65

# External database (production PostgreSQL)
database:
  type: postgresdb
  useExternal: true
  host: "your-postgres-host.com"
  port: 5432
  database: n8n_enterprise
  schema: "public"                    # PostgreSQL schema name
  user: n8n
  passwordSecret:
    name: "n8n-enterprise-db-secret"
    key: "password"

# External Redis (production Redis)
redis:
  enabled: true
  useExternal: true
  host: "your-redis-host.com"
  port: 6379

# Enterprise S3 storage
s3:
  enabled: true
  bucket:
    name: "n8n-enterprise-storage"
    region: "us-east-1"
  auth:
    autoDetect: true  # Using IRSA
  storage:
    mode: "s3"
    availableModes: "filesystem,s3"

# Service account with enterprise IAM role
serviceAccount:
  create: true
  name: n8n-enterprise
  awsRoleArn: "arn:aws:iam::123456789012:role/n8n-enterprise-role"
  annotations:
    eks.amazonaws.com/role-arn: "arn:aws:iam::123456789012:role/n8n-enterprise-role"

# n8n Enterprise License Configuration
license:
  enabled: true
  # Enterprise license activation key (get from n8n customer portal)
  activationKey: "your-enterprise-license-key-here"

# Service configuration with session affinity
service:
  type: ClusterIP
  port: 5678
  sessionAffinity:
    enabled: true
    timeoutSeconds: 14400  # 4 hours

# Enterprise resource allocation
resources:
  main:
    requests:
      memory: "2Gi"
      cpu: "1000m"
    limits:
      memory: "4Gi"
      cpu: "2000m"
  worker:
    requests:
      memory: "1Gi"
      cpu: "500m"
    limits:
      memory: "2Gi"
      cpu: "1000m"
  webhookProcessor:
    requests:
      memory: "512Mi"
      cpu: "300m"
    limits:
      memory: "1Gi"
      cpu: "800m"

# Enterprise configuration
config:
  timezone: UTC
  extraEnv:
    # Security settings
    - name: N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS
      value: "true"
    
    # Database SSL
    - name: DB_POSTGRESDB_SSL_ENABLED
      value: "true"
    - name: DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED
      value: "true"  # Set to "false" only if using self-signed certs (not recommended for production)
    
    # Enterprise logging
    - name: N8N_LOG_LEVEL
      value: "info"
    - name: N8N_LOG_OUTPUT
      value: "json"  # Structured logging for enterprise
    
    # Performance settings
    - name: N8N_CONCURRENCY_PRODUCTION_LIMIT
      value: "100"
    
    # Enterprise features
    - name: N8N_ENTERPRISE_LICENSE_ENABLED
      value: "true"
    
    # Advanced webhook settings
    - name: N8N_WEBHOOK_TIMEOUT
      value: "300000"  # 5 minutes

# Advanced execution settings
executions:
  concurrency:
    productionLimit: 100
  timeout: 7200  # 2 hours
  dataRetention:
    saveOnError: true
    saveOnSuccess: true
    saveOnProgress: false
    saveManualExecutions: true
    prune: true
    maxAge: 2160  # 90 days
    maxCount: 100000
    hardDeleteBuffer: 24  # 24 hours
    pruneHardDeleteInterval: "0 2 * * *"  # Daily at 2 AM
    pruneSoftDeleteInterval: "0 3 * * *"  # Daily at 3 AM

# Webhook configuration
webhook:
  timeout: 300000  # 5 minutes for enterprise workloads

# Core secrets
secretRefs:
  existingSecret: "n8n-enterprise-secrets"

# Enterprise security settings
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 1000
  seccompProfile:
    type: RuntimeDefault

# Pod disruption budget for high availability
podDisruptionBudget:
  enabled: true
  minAvailable: 2

# Network policies for enterprise security
networkPolicy:
  enabled: true
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-system
      ports:
        - protocol: TCP
          port: 5678
  egress:
    - to: []  # Allow all egress (customize as needed)

# Monitoring and observability (if using Prometheus)
monitoring:
  enabled: true
  serviceMonitor:
    enabled: true
    interval: 30s
    scrapeTimeout: 10s
  prometheusRule:
    enabled: true
```

## File: `charts/n8n/examples/production-s3.yaml`
```yaml
# Production n8n Configuration with S3 Storage
# This example shows a production-ready setup with external services and S3 storage
# Cloud-agnostic except for S3 which requires AWS

# Multi-main setup for high availability
multiMain:
  enabled: true
  replicas: 2

# Queue mode with multiple workers
queueMode:
  enabled: true
  workerReplicaCount: 5
  workerConcurrency: 15

# Load balancer must route /webhook/* to webhook processor service
webhookProcessor:
  enabled: true
  replicaCount: 2
  disableProductionWebhooksOnMainProcess: true

# Enterprise license required for multi-main setup
license:
  enabled: true
  activationKey: "your-enterprise-license-key"

hpa:
  main:
    enabled: true
    minReplicas: 2
    maxReplicas: 10
    targetCPUUtilizationPercentage: 70
  worker:
    enabled: true
    minReplicas: 5
    maxReplicas: 50
    targetCPUUtilizationPercentage: 80
  webhookProcessor:
    enabled: true
    minReplicas: 2
    maxReplicas: 20
    targetCPUUtilizationPercentage: 75

database:
  type: postgresdb
  useExternal: true
  host: "your-postgres-host.com"  # Replace with your PostgreSQL endpoint
  port: 5432
  database: n8n
  schema: "public"                 # PostgreSQL schema name
  user: n8n
  passwordSecret:
    name: "n8n-db-secret"
    key: "password"

redis:
  enabled: true
  useExternal: true
  host: "your-redis-host.com"  # Replace with your Redis endpoint
  port: 6379

s3:
  enabled: true
  bucket:
    name: "your-s3-bucket-name"  # Replace with your S3 bucket name
    region: "us-east-1"          # Replace with your S3 bucket region
  auth:
    # Option 1: IRSA (IAM Roles for Service Accounts) - Recommended for AWS EKS
    autoDetect: true  # Only works with AWS S3, requires serviceAccount.awsRoleArn
    
    # Option 2: Access Keys - Alternative authentication method
    # autoDetect: false
    # accessKeyId: "your-access-key-id"
    # secretAccessKeySecret:
    #   name: "s3-credentials"
    #   key: "secret-access-key"
  
  storage:
    mode: "s3"
    availableModes: "filesystem,s3"

# Service Account with AWS IAM Role
serviceAccount:
  create: true
  name: n8n-prod
  # AWS IAM Role ARN (only needed if using S3 with autoDetect: true)
  awsRoleArn: "arn:aws:iam::your-account-id:role/your-n8n-s3-role"
  annotations:
    # EKS annotation for IRSA (only needed for AWS EKS)
    eks.amazonaws.com/role-arn: "arn:aws:iam::your-account-id:role/your-n8n-s3-role"

# Service configuration with session affinity for WebSocket stability
service:
  type: ClusterIP
  port: 5678
  sessionAffinity:
    enabled: true
    timeoutSeconds: 10800  # 3 hours

# Production resource limits
resources:
  main:
    requests:
      memory: "1Gi"
      cpu: "500m"
    limits:
      memory: "2Gi" 
      cpu: "1000m"
  worker:
    requests:
      memory: "512Mi"
      cpu: "300m"
    limits:
      memory: "1Gi"
      cpu: "800m"
  webhookProcessor:
    requests:
      memory: "256Mi"
      cpu: "200m"
    limits:
      memory: "512Mi"
      cpu: "500m"

# Production configuration
config:
  timezone: Europe/Berlin
  extraEnv:
    # Security settings
    - name: N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS
      value: "true"
    
    - name: DB_POSTGRESDB_SSL_ENABLED
      value: "true"
    - name: DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED
      value: "true"  # Set to "false" only if using self-signed certs (not recommended for production)
    
    - name: N8N_LOG_LEVEL
      value: "info"
    - name: N8N_LOG_OUTPUT
      value: "console"
    
    - name: N8N_CONCURRENCY_PRODUCTION_LIMIT
      value: "50"

executions:
  concurrency:
    productionLimit: 50
  timeout: 3600  # 1 hour
  data:
    saveOnError: "all"       # "all" or "none"
    saveOnSuccess: "all"     # "all" or "none"
    saveOnProgress: false
    saveManualExecutions: true
  pruning:
    enabled: true
    maxAge: 336              # 14 days in hours
    maxCount: 10000
    hardDeleteBuffer: 1      # 1 hour buffer before hard delete
    hardDeleteInterval: 15   # minutes between hard delete runs
    softDeleteInterval: 60   # minutes between soft delete runs

webhook:
  timeout: 300000  # 5 minutes

# Core secrets reference
secretRefs:
  existingSecret: "n8n-core-secrets"

# Production readiness probes
probes:
  liveness:
    enabled: true
    initialDelaySeconds: 60
    periodSeconds: 30
    timeoutSeconds: 10
    failureThreshold: 5
  readiness:
    enabled: true
    initialDelaySeconds: 30
    periodSeconds: 10
    timeoutSeconds: 5
    failureThreshold: 3

# Security context
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 1000

# Pod disruption budget for high availability
podDisruptionBudget:
  enabled: true
  minAvailable: 1

# Network policies (if using a CNI that supports them)
networkPolicy:
  enabled: false  # Enable if your cluster supports network policies
```

## File: `charts/n8n/examples/standalone.yaml`
```yaml
# Standalone mode — single n8n pod with SQLite, no external dependencies.
# Suitable for development, testing, or small-scale production use.
# Data is stored in a PersistentVolumeClaim; no PostgreSQL or Redis required.

queueMode:
  enabled: false

database:
  type: sqlite
  useExternal: false

redis:
  enabled: false

persistence:
  enabled: true
  size: 5Gi

# You must still provide an encryption key for credential storage.
# Create a secret: kubectl create secret generic n8n-secrets \
#   --from-literal=N8N_ENCRYPTION_KEY=$(openssl rand -hex 32) \
#   --from-literal=N8N_HOST=localhost \
#   --from-literal=N8N_PORT=5678 \
#   --from-literal=N8N_PROTOCOL=http
secretRefs:
  existingSecret: "n8n-secrets"
```

## File: `charts/n8n/examples/task-runners.yaml`
```yaml
# Task Runners with Queue Mode
# This example demonstrates enabling task runner sidecars for external code execution
# Task runners handle JavaScript and Python execution in isolated sidecar containers
#
# Architecture:
#   - The n8n container runs a task broker on port 5679
#   - A runner sidecar container connects to the broker over localhost
#   - Both main and worker pods get their own runner sidecar
#
# Prerequisites:
#   - External PostgreSQL and Redis (queue mode)
#   - A shared auth token secret for runner ↔ broker communication

queueMode:
  enabled: true
  workerReplicaCount: 3
  workerConcurrency: 10

# Enable task runner sidecars on main and worker pods
taskRunners:
  enabled: true

  # Auth token for runner ↔ broker communication
  # Create the secret first:
  #   kubectl create secret generic n8n-runner-token --from-literal=auth-token=$(openssl rand -base64 32)
  authToken:
    existingSecret: "n8n-runner-token"
    existingSecretKey: "auth-token"

  # Broker runs inside the n8n container
  broker:
    listenAddress: "0.0.0.0"
    port: 5679

  # Launcher settings
  launcher:
    logLevel: info
    autoShutdownTimeout: 15

  # Enable Python runner support
  nativePythonRunner: true

  # Resource limits for runner sidecar (tune based on workflow complexity)
  resources:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: "1"
      memory: 1Gi

  # Optional: mount a custom config to allowlist additional npm packages
  # customConfig:
  #   enabled: true
  #   configMapName: "n8n-runner-config"
  #   configMapKey: "n8n-task-runners.json"

# External database
database:
  type: postgresdb
  useExternal: true
  host: "your-postgres-host.com"
  port: 5432
  database: n8n
  schema: "public"
  user: n8n
  passwordSecret:
    name: "n8n-db-secret"
    key: "password"

# External Redis
redis:
  enabled: true
  useExternal: true
  host: "your-redis-host.com"
  port: 6379

# Core secrets
secretRefs:
  existingSecret: "n8n-core-secrets"

# Resource limits for n8n containers
resources:
  main:
    requests:
      cpu: 500m
      memory: 1Gi
    limits:
      cpu: "2"
      memory: 2Gi
  worker:
    requests:
      cpu: 500m
      memory: 1Gi
    limits:
      cpu: "2"
      memory: 2Gi
```

## File: `charts/n8n/templates/NOTES.txt`
```
{{- if .Values.ingress.enabled }}
{{- range .Values.ingress.hosts }}

n8n has been successfully deployed!

Your n8n instance is available at:
{{- if $.Values.ingress.tls }}
  https://{{ .host }}
{{- else }}
  http://{{ .host }}
{{- end }}

{{- end }}
{{- else }}

n8n has been successfully deployed!

To access n8n, run the following commands:

1. Get the service URL:
   kubectl get service {{ include "n8n.fullname" . }}-main{{- if .Release.Namespace }} --namespace {{ .Release.Namespace }}{{- end }}

2. Port forward to access n8n locally:
   kubectl port-forward service/{{ include "n8n.fullname" . }}-main{{- if .Release.Namespace }} --namespace {{ .Release.Namespace }}{{- end }} 5678:{{ .Values.service.port }}

3. Open your browser to:
   http://localhost:5678

{{- end }}

Deployment Configuration:
{{- if .Values.queueMode.enabled }}
  - Mode: Queue ({{ .Values.queueMode.workerReplicaCount }} workers)
{{- if .Values.multiMain.enabled }}
  - Multi-main: {{ .Values.multiMain.replicas }} main pods
{{- else }}
  - Main pods: {{ .Values.replicaCount }}
{{- end }}
{{- if .Values.webhookProcessor.enabled }}
  - Webhook processors: {{ .Values.webhookProcessor.replicaCount }} pods
{{- end }}
  - Database: PostgreSQL ({{ .Values.database.host }})
  - Cache: Redis ({{ .Values.redis.host }})
{{- if .Values.s3.enabled }}
  - Storage: S3 ({{ .Values.s3.bucket.name }})
{{- end }}
{{- else }}
  - Mode: Standalone (SQLite)
  - Main pods: {{ .Values.replicaCount }}
  - Database: SQLite (local storage)
{{- end }}

Documentation: https://docs.n8n.io/
Issues: https://github.com/n8n-io/n8n-hosting/issues
```

## File: `charts/n8n/templates/_configmap-env.tpl`
```
{{/*
Environment variables from ConfigMap for all components
*/}}
{{- define "n8n.sharedConfigMapEnv" -}}
# Shared configuration from ConfigMap
- name: TZ
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: TZ
- name: DB_TYPE
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_TYPE
{{- if .Values.database.useExternal }}
- name: DB_POSTGRESDB_DATABASE
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_DATABASE
- name: DB_POSTGRESDB_HOST
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_HOST
- name: DB_POSTGRESDB_PORT
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_PORT
- name: DB_POSTGRESDB_USER
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_USER
{{- if .Values.database.schema }}
- name: DB_POSTGRESDB_SCHEMA
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_SCHEMA
{{- end }}
{{- if .Values.database.ssl.enabled }}
- name: DB_POSTGRESDB_SSL
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_SSL
{{- if .Values.database.ssl.ca }}
- name: DB_POSTGRESDB_SSL_CA
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_SSL_CA
{{- end }}
{{- if .Values.database.ssl.cert }}
- name: DB_POSTGRESDB_SSL_CERT
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_SSL_CERT
{{- end }}
# DB_POSTGRESDB_SSL_KEY is not sourced from the ConfigMap because TLS private keys
# must not be stored unencrypted. Provide it via config.extraEnv from a Secret.
{{- if not .Values.database.ssl.rejectUnauthorized }}
- name: DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED
{{- end }}
{{- end }}
{{- end }}
{{- if .Values.queueMode.enabled }}
- name: EXECUTIONS_MODE
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: EXECUTIONS_MODE
- name: OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS
{{- end }}
- name: N8N_RUNNERS_MODE
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_RUNNERS_MODE
- name: N8N_RUNNERS_AUTH_TOKEN
  valueFrom:
    secretKeyRef:
      {{- if .Values.taskRunners.authToken.existingSecret }}
      name: {{ .Values.taskRunners.authToken.existingSecret }}
      key: {{ .Values.taskRunners.authToken.existingSecretKey | default "N8N_RUNNERS_AUTH_TOKEN" }}
      {{- else }}
      name: {{ include "n8n.fullname" . }}-task-runners
      key: N8N_RUNNERS_AUTH_TOKEN
      {{- end }}
{{- if .Values.queueMode.enabled }}
{{- if .Values.redis.clusterNodes }}
- name: QUEUE_BULL_REDIS_CLUSTER_NODES
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_CLUSTER_NODES
{{- else }}
- name: QUEUE_BULL_REDIS_HOST
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_HOST
- name: QUEUE_BULL_REDIS_PORT
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_PORT
{{- end }}
{{- if .Values.redis.username }}
- name: QUEUE_BULL_REDIS_USERNAME
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_USERNAME
{{- end }}
{{- if and .Values.redis.database (ne (.Values.redis.database | int) 0) }}
- name: QUEUE_BULL_REDIS_DB
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_DB
{{- end }}
{{- if .Values.redis.timeout }}
- name: QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD
{{- end }}
{{- if .Values.redis.prefix }}
- name: QUEUE_BULL_PREFIX
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_PREFIX
{{- end }}
{{- if .Values.redis.tls }}
- name: QUEUE_BULL_REDIS_TLS
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_TLS
{{- end }}
{{- if .Values.redis.dualstack }}
- name: QUEUE_BULL_REDIS_DUALSTACK
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_BULL_REDIS_DUALSTACK
{{- end }}
{{- if .Values.redis.worker.lockDuration }}
- name: QUEUE_WORKER_LOCK_DURATION
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_WORKER_LOCK_DURATION
{{- end }}
{{- if .Values.redis.worker.lockRenewTime }}
- name: QUEUE_WORKER_LOCK_RENEW_TIME
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_WORKER_LOCK_RENEW_TIME
{{- end }}
{{- if .Values.redis.worker.stalledInterval }}
- name: QUEUE_WORKER_STALLED_INTERVAL
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_WORKER_STALLED_INTERVAL
{{- end }}
{{- if .Values.redis.worker.maxStalledCount }}
- name: QUEUE_WORKER_MAX_STALLED_COUNT
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: QUEUE_WORKER_MAX_STALLED_COUNT
{{- end }}
- name: N8N_GRACEFUL_SHUTDOWN_TIMEOUT
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_GRACEFUL_SHUTDOWN_TIMEOUT
{{- end }}
{{- end }}

{{/*
Environment variables from ConfigMap for main pods only
*/}}
{{- define "n8n.mainConfigMapEnv" -}}
{{- if .Values.webhook.enabled }}
{{- if or .Values.webhook.url (and .Values.ingress .Values.ingress.enabled (gt (len .Values.ingress.hosts) 0)) }}
- name: WEBHOOK_URL
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: WEBHOOK_URL
{{- end }}
{{- if .Values.webhook.timeout }}
- name: N8N_WEBHOOK_TIMEOUT
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_WEBHOOK_TIMEOUT
{{- end }}
{{- end }}
{{- if and .Values.multiMain.enabled .Values.license.enabled }}
- name: N8N_MULTI_MAIN_SETUP_ENABLED
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_MULTI_MAIN_SETUP_ENABLED
{{- if .Values.multiMain.setup.keyTtl }}
- name: N8N_MULTI_MAIN_SETUP_KEY_TTL
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_MULTI_MAIN_SETUP_KEY_TTL
{{- end }}
{{- if .Values.multiMain.setup.checkInterval }}
- name: N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL
{{- end }}
{{- end }}
{{- if and .Values.webhookProcessor.enabled .Values.webhookProcessor.disableProductionWebhooksOnMainProcess }}
- name: N8N_DISABLE_PRODUCTION_MAIN_PROCESS
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_DISABLE_PRODUCTION_MAIN_PROCESS
{{- end }}
{{- end }}

{{/*
Environment variables from ConfigMap for webhook processor pods (similar to main but webhook-focused)
*/}}
{{- define "n8n.webhookProcessorConfigMapEnv" -}}
{{- if .Values.webhook.enabled }}
{{- if or .Values.webhook.url (and .Values.ingress .Values.ingress.enabled (gt (len .Values.ingress.hosts) 0)) }}
- name: WEBHOOK_URL
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: WEBHOOK_URL
{{- end }}
{{- if .Values.webhook.timeout }}
- name: N8N_WEBHOOK_TIMEOUT
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_WEBHOOK_TIMEOUT
{{- end }}
{{- end }}
{{- end }}

{{/*
Environment variables from ConfigMap for worker pods (webhook URL for resume/waiting URLs)
*/}}
{{- define "n8n.workerConfigMapEnv" -}}
{{- if .Values.webhook.enabled }}
{{- if or .Values.webhook.url (and .Values.ingress .Values.ingress.enabled (gt (len .Values.ingress.hosts) 0)) }}
- name: WEBHOOK_URL
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: WEBHOOK_URL
{{- end }}
{{- end }}
{{- end }}

{{/*
Task Runners environment variables for n8n broker (main and worker pods)
*/}}
{{- define "n8n.taskRunnerBrokerEnv" -}}
{{- if .Values.taskRunners.enabled }}
# Task runner broker configuration
- name: N8N_RUNNERS_BROKER_LISTEN_ADDRESS
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_RUNNERS_BROKER_LISTEN_ADDRESS
- name: N8N_NATIVE_PYTHON_RUNNER
  valueFrom:
    configMapKeyRef:
      name: {{ include "n8n.fullname" . }}
      key: N8N_NATIVE_PYTHON_RUNNER
{{- end }}
{{- end }}

{{/*
Task Runners environment variables for runner sidecar containers
*/}}
{{- define "n8n.taskRunnerSidecarEnv" -}}
{{- if .Values.taskRunners.enabled }}
# Task runner configuration
- name: N8N_RUNNERS_TASK_BROKER_URI
  value: "http://localhost:{{ .Values.taskRunners.broker.port }}"
- name: N8N_RUNNERS_AUTH_TOKEN
  valueFrom:
    secretKeyRef:
      {{- if .Values.taskRunners.authToken.existingSecret }}
      name: {{ .Values.taskRunners.authToken.existingSecret }}
      key: {{ .Values.taskRunners.authToken.existingSecretKey | default "N8N_RUNNERS_AUTH_TOKEN" }}
      {{- else }}
      name: {{ include "n8n.fullname" . }}-task-runners
      key: N8N_RUNNERS_AUTH_TOKEN
      {{- end }}
- name: N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT
  value: "{{ .Values.taskRunners.launcher.autoShutdownTimeout }}"
- name: N8N_RUNNERS_LAUNCHER_LOG_LEVEL
  value: "{{ .Values.taskRunners.launcher.logLevel }}"
{{- with .Values.taskRunners.extraEnv }}
{{- toYaml . | nindent 0 }}
{{- end }}
{{- end }}
{{- end }}
```

## File: `charts/n8n/templates/_environment-helpers.tpl`
```
{{/*
S3 External Storage environment variables
*/}}
{{- define "n8n.s3Env" -}}
{{- if .Values.s3.enabled }}
# S3 External Storage Configuration
- name: N8N_DEFAULT_BINARY_DATA_MODE
  value: {{ .Values.s3.storage.mode | quote }}
- name: N8N_AVAILABLE_BINARY_DATA_MODES
  value: {{ .Values.s3.storage.availableModes | quote }}
- name: N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME
  value: {{ .Values.s3.bucket.name | quote }}
- name: N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION
  value: {{ .Values.s3.bucket.region | quote }}
{{- if .Values.s3.bucket.host }}
- name: N8N_EXTERNAL_STORAGE_S3_HOST
  value: {{ .Values.s3.bucket.host | quote }}
{{- end }}
{{- if .Values.s3.auth.autoDetect }}
- name: N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT
  value: "true"
{{- else }}
{{- if .Values.s3.auth.accessKeyId }}
- name: N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY
  value: {{ .Values.s3.auth.accessKeyId | quote }}
- name: AWS_ACCESS_KEY_ID
  value: {{ .Values.s3.auth.accessKeyId | quote }}
{{- end }}
{{- if .Values.s3.auth.secretAccessKeySecret.name }}
- name: N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET
  valueFrom:
    secretKeyRef:
      name: {{ .Values.s3.auth.secretAccessKeySecret.name }}
      key: {{ .Values.s3.auth.secretAccessKeySecret.key }}
- name: AWS_SECRET_ACCESS_KEY
  valueFrom:
    secretKeyRef:
      name: {{ .Values.s3.auth.secretAccessKeySecret.name }}
      key: {{ .Values.s3.auth.secretAccessKeySecret.key }}
{{- end }}
{{- end }}
{{- if .Values.s3.storage.forcePathStyle }}
- name: N8N_EXTERNAL_STORAGE_S3_FORCE_PATH_STYLE
  value: "true"
{{- end }}
{{- with .Values.s3.storage.extraEnv }}
{{- toYaml . | nindent 0 }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Executions Configuration environment variables
*/}}
{{- define "n8n.executionsEnv" -}}
# Executions Configuration
{{- if and .Values.executions.timeout (ne (.Values.executions.timeout | int) -1) }}
- name: EXECUTIONS_TIMEOUT
  value: "{{ .Values.executions.timeout }}"
{{- end }}
{{- if .Values.executions.timeoutMax }}
- name: EXECUTIONS_TIMEOUT_MAX
  value: "{{ .Values.executions.timeoutMax }}"
{{- end }}
- name: EXECUTIONS_DATA_SAVE_ON_ERROR
  value: {{ .Values.executions.data.saveOnError | quote }}
- name: EXECUTIONS_DATA_SAVE_ON_SUCCESS
  value: {{ .Values.executions.data.saveOnSuccess | quote }}
- name: EXECUTIONS_DATA_SAVE_ON_PROGRESS
  value: "{{ .Values.executions.data.saveOnProgress }}"
- name: EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS
  value: "{{ .Values.executions.data.saveManualExecutions }}"
- name: EXECUTIONS_DATA_PRUNE
  value: "{{ .Values.executions.pruning.enabled }}"
{{- if .Values.executions.pruning.maxAge }}
- name: EXECUTIONS_DATA_MAX_AGE
  value: "{{ .Values.executions.pruning.maxAge }}"
{{- end }}
{{- if .Values.executions.pruning.maxCount }}
- name: EXECUTIONS_DATA_PRUNE_MAX_COUNT
  value: "{{ .Values.executions.pruning.maxCount }}"
{{- end }}
{{- if .Values.executions.pruning.hardDeleteBuffer }}
- name: EXECUTIONS_DATA_HARD_DELETE_BUFFER
  value: "{{ .Values.executions.pruning.hardDeleteBuffer }}"
{{- end }}
{{- if .Values.executions.pruning.hardDeleteInterval }}
- name: EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL
  value: "{{ .Values.executions.pruning.hardDeleteInterval }}"
{{- end }}
{{- if .Values.executions.pruning.softDeleteInterval }}
- name: EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL
  value: "{{ .Values.executions.pruning.softDeleteInterval }}"
{{- end }}
{{- if and .Values.executions.concurrency.productionLimit (ne (.Values.executions.concurrency.productionLimit | int) -1) }}
- name: N8N_CONCURRENCY_PRODUCTION_LIMIT
  value: "{{ .Values.executions.concurrency.productionLimit }}"
{{- end }}
{{- with .Values.executions.extraEnv }}
{{- toYaml . | nindent 0 }}
{{- end }}
{{- end }}

{{/*
License Configuration environment variables
*/}}
{{- define "n8n.licenseEnv" -}}
{{- if .Values.license.enabled }}
# License Configuration
{{- if .Values.license.activationKey }}
- name: N8N_LICENSE_ACTIVATION_KEY
  value: {{ .Values.license.activationKey | quote }}
{{- else if .Values.license.existingSecret.name }}
- name: N8N_LICENSE_ACTIVATION_KEY
  valueFrom:
    secretKeyRef:
      name: {{ .Values.license.existingSecret.name }}
      key: {{ .Values.license.existingSecret.key }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Core n8n secrets environment variables
*/}}
{{- define "n8n.coreSecretsEnv" -}}
# Core n8n secrets
- name: N8N_ENCRYPTION_KEY
  valueFrom:
    secretKeyRef:
      name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
      key: N8N_ENCRYPTION_KEY
- name: N8N_HOST
  valueFrom:
    secretKeyRef:
      name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
      key: N8N_HOST
- name: N8N_PORT
  valueFrom:
    secretKeyRef:
      name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
      key: N8N_PORT
- name: N8N_PROTOCOL
  valueFrom:
    secretKeyRef:
      name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
      key: N8N_PROTOCOL
{{- end }}
```

## File: `charts/n8n/templates/_helpers.tpl`
```
{{/*
Expand the name of the chart.
*/}}
{{- define "n8n.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this.
*/}}
{{- define "n8n.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default "n8n" .Values.nameOverride }}
{{- if or (contains "n8n" .Release.Name) (eq .Release.Name "n8n") }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "n8n.labels" -}}
helm.sh/chart: {{ include "n8n.chart" . }}
{{ include "n8n.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Selector labels
*/}}
{{- define "n8n.selectorLabels" -}}
app.kubernetes.io/name: {{ include "n8n.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Chart name and version
*/}}
{{- define "n8n.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{/*
Create the name of the service account to use
*/}}
{{- define "n8n.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "n8n.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- .Values.serviceAccount.name }}
{{- end }}
{{- end -}}

{{/*
Validate values — called once from deployment-main.yaml to fail fast on bad config.
*/}}
{{- define "n8n.validate" -}}

{{/* --- Queue mode infrastructure --- */}}
{{- if .Values.queueMode.enabled -}}
{{- if not .Values.database.useExternal -}}
{{- fail "database.useExternal must be true when queueMode.enabled=true. Queue mode requires external PostgreSQL." -}}
{{- end -}}
{{- if not .Values.database.host -}}
{{- fail "database.host is required when queueMode.enabled=true. Set it to your PostgreSQL hostname." -}}
{{- end -}}
{{- if not .Values.redis.enabled -}}
{{- fail "redis.enabled must be true when queueMode.enabled=true. Queue mode requires Redis." -}}
{{- end -}}
{{- if not .Values.redis.host -}}
{{- fail "redis.host is required when queueMode.enabled=true. Set it to your Redis hostname." -}}
{{- end -}}
{{- end -}}

{{/* --- Standalone mode constraints --- */}}
{{- if not .Values.queueMode.enabled -}}
{{- if not .Values.persistence.enabled -}}
{{- fail "persistence.enabled must be true when queueMode.enabled=false. Standalone mode uses SQLite which requires persistent storage." -}}
{{- end -}}
{{- if .Values.multiMain.enabled -}}
{{- fail "multiMain.enabled=true requires queueMode.enabled=true" -}}
{{- end -}}
{{- if .Values.webhookProcessor.enabled -}}
{{- fail "webhookProcessor.enabled=true requires queueMode.enabled=true" -}}
{{- end -}}
{{- end -}}

{{/* --- Webhook processor --- */}}
{{- if and .Values.ingress.webhookProcessor.enabled (not .Values.webhookProcessor.enabled) -}}
{{- fail "ingress.webhookProcessor.enabled=true requires webhookProcessor.enabled=true" -}}
{{- end -}}

{{/* --- Multi-main --- */}}
{{- if and .Values.multiMain.enabled (lt (int .Values.multiMain.replicas) 2) -}}
{{- fail "multiMain.enabled=true requires multiMain.replicas >= 2" -}}
{{- end -}}

{{/* --- Task runners --- */}}
{{- if and .Values.taskRunners.enabled (ne .Values.taskRunners.mode "external") -}}
{{- fail "taskRunners.mode must be 'external'. This chart only supports external task runner sidecars." -}}
{{- end -}}

{{/* --- S3 --- */}}
{{- if .Values.s3.enabled -}}
{{- if not .Values.s3.bucket.name -}}
{{- fail "s3.bucket.name is required when s3.enabled=true" -}}
{{- end -}}
{{- if not .Values.s3.bucket.region -}}
{{- fail "s3.bucket.region is required when s3.enabled=true" -}}
{{- end -}}
{{- if and (not .Values.s3.auth.autoDetect) (not .Values.s3.auth.accessKeyId) -}}
{{- fail "s3.auth.accessKeyId is required when s3.enabled=true and s3.auth.autoDetect=false" -}}
{{- end -}}
{{- if and .Values.s3.auth.autoDetect (not .Values.serviceAccount.awsRoleArn) -}}
{{- fail "serviceAccount.awsRoleArn is required when s3.auth.autoDetect=true (for IRSA)" -}}
{{- end -}}
{{- end -}}

{{/* --- License --- */}}
{{- if and .Values.license.enabled .Values.license.activationKey .Values.license.existingSecret.name -}}
{{- fail "license.activationKey and license.existingSecret.name are mutually exclusive. Use one or the other." -}}
{{- end -}}

{{/* --- Encryption key --- */}}
{{- if and (not .Values.secretRefs.existingSecret) (eq .Values.secretRefs.env.N8N_ENCRYPTION_KEY "change-me-to-a-long-random-key") -}}
{{- fail "secretRefs.env.N8N_ENCRYPTION_KEY must be changed from the default placeholder value, or provide secretRefs.existingSecret with your own Secret" -}}
{{- end -}}

{{- end -}}
```

## File: `charts/n8n/templates/configmap.yaml`
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "n8n.fullname" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
data:
  # ----- Shared Configuration (used by all components: main, worker, webhook-processor) -----
  TZ: {{ .Values.config.timezone | quote }}
  
  # Database configuration
  DB_TYPE: {{ .Values.database.type | quote }}
  {{- if .Values.database.useExternal }}
  DB_POSTGRESDB_DATABASE: {{ .Values.database.database | quote }}
  DB_POSTGRESDB_HOST: {{ .Values.database.host | quote }}
  DB_POSTGRESDB_PORT: "{{ .Values.database.port }}"
  DB_POSTGRESDB_USER: {{ .Values.database.user | quote }}
  {{- if .Values.database.schema }}
  DB_POSTGRESDB_SCHEMA: {{ .Values.database.schema | quote }}
  {{- end }}
  {{- if .Values.database.ssl.enabled }}
  DB_POSTGRESDB_SSL: "true"
  {{- if .Values.database.ssl.ca }}
  DB_POSTGRESDB_SSL_CA: {{ .Values.database.ssl.ca | quote }}
  {{- end }}
  {{- if .Values.database.ssl.cert }}
  DB_POSTGRESDB_SSL_CERT: {{ .Values.database.ssl.cert | quote }}
  {{- end }}
  # DB_POSTGRESDB_SSL_KEY is intentionally omitted from this ConfigMap.
  # TLS private keys must not be stored in ConfigMaps, which are not encrypted
  # at rest and are readable by anyone with ConfigMap read access in the namespace.
  # Provide DB_POSTGRESDB_SSL_KEY via config.extraEnv referencing a Secret instead, e.g.:
  #   config:
  #     extraEnv:
  #       - name: DB_POSTGRESDB_SSL_KEY
  #         valueFrom:
  #           secretKeyRef:
  #             name: my-db-ssl-secret
  #             key: tls.key
  {{- if not .Values.database.ssl.rejectUnauthorized }}
  DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED: "false"
  {{- end }}
  {{- end }}
  {{- end }}

  # Queue configuration
  {{- if .Values.queueMode.enabled }}
  EXECUTIONS_MODE: "queue"
  OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS: "true"
  {{- end }}
  # Task Runners configuration (shared across all pods)
  # N8N_RUNNERS_ENABLED is deprecated in n8n 2.9+; runners are always active.
  # Setting MODE to "external" prevents n8n from trying to launch internal runners
  # (which would fail for Python since the n8n image lacks Python 3).
  N8N_RUNNERS_MODE: {{ .Values.taskRunners.mode | quote }}
  {{- if .Values.taskRunners.enabled }}
  N8N_RUNNERS_BROKER_LISTEN_ADDRESS: {{ .Values.taskRunners.broker.listenAddress | quote }}
  N8N_NATIVE_PYTHON_RUNNER: {{ ternary "true" "false" .Values.taskRunners.nativePythonRunner | quote }}
  {{- end }}

  {{- if .Values.queueMode.enabled }}
  # Redis configuration (queue mode only)
  {{- if .Values.redis.clusterNodes }}
  QUEUE_BULL_REDIS_CLUSTER_NODES: {{ .Values.redis.clusterNodes | quote }}
  {{- else }}
  QUEUE_BULL_REDIS_HOST: {{ .Values.redis.host | quote }}
  QUEUE_BULL_REDIS_PORT: "{{ default 6379 .Values.redis.port }}"
  {{- end }}
  {{- if .Values.redis.username }}
  QUEUE_BULL_REDIS_USERNAME: {{ .Values.redis.username | quote }}
  {{- end }}
  {{- if and .Values.redis.database (ne (.Values.redis.database | int) 0) }}
  QUEUE_BULL_REDIS_DB: "{{ .Values.redis.database }}"
  {{- end }}
  {{- if .Values.redis.timeout }}
  QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD: "{{ .Values.redis.timeout }}"
  {{- end }}
  {{- if .Values.redis.prefix }}
  QUEUE_BULL_PREFIX: {{ .Values.redis.prefix | quote }}
  {{- end }}
  {{- if .Values.redis.tls }}
  QUEUE_BULL_REDIS_TLS: "true"
  {{- end }}
  {{- if .Values.redis.dualstack }}
  QUEUE_BULL_REDIS_DUALSTACK: "true"
  {{- end }}

  # Worker settings (queue mode only)
  {{- if .Values.redis.worker.lockDuration }}
  QUEUE_WORKER_LOCK_DURATION: "{{ .Values.redis.worker.lockDuration }}"
  {{- end }}
  {{- if .Values.redis.worker.lockRenewTime }}
  QUEUE_WORKER_LOCK_RENEW_TIME: "{{ .Values.redis.worker.lockRenewTime }}"
  {{- end }}
  {{- if .Values.redis.worker.stalledInterval }}
  QUEUE_WORKER_STALLED_INTERVAL: "{{ .Values.redis.worker.stalledInterval }}"
  {{- end }}
  {{- if .Values.redis.worker.maxStalledCount }}
  QUEUE_WORKER_MAX_STALLED_COUNT: "{{ .Values.redis.worker.maxStalledCount }}"
  {{- end }}

  # Graceful shutdown timeout
  N8N_GRACEFUL_SHUTDOWN_TIMEOUT: "{{ .Values.redis.worker.timeout }}"
  {{- end }}
  
  # ----- Main-only Configuration -----
  {{- if .Values.webhook.enabled }}
  {{- if .Values.webhook.url }}
  WEBHOOK_URL: {{ .Values.webhook.url | quote }}
  {{- else if and .Values.ingress .Values.ingress.enabled (gt (len .Values.ingress.hosts) 0) }}
  WEBHOOK_URL: "https://{{ (index .Values.ingress.hosts 0).host }}"
  {{- end }}
  {{- if .Values.webhook.timeout }}
  N8N_WEBHOOK_TIMEOUT: "{{ .Values.webhook.timeout }}"
  {{- end }}
  {{- end }}
  
  # Editor Base URL (for proper webhook URL display in UI)
  # Only set when external access is configured to avoid issues with internal-only deployments
  {{- if and .Values.ingress .Values.ingress.enabled (gt (len .Values.ingress.hosts) 0) }}
  N8N_EDITOR_BASE_URL: "https://{{ (index .Values.ingress.hosts 0).host }}"
  {{- else if .Values.webhook.url }}
  # If custom webhook URL is set, use it as editor base URL (since webhook.url is the domain)
  {{- if hasPrefix "http" .Values.webhook.url }}
  N8N_EDITOR_BASE_URL: {{ .Values.webhook.url | quote }}
  {{- end }}
  {{- end }}
  
  # Multi-main setup (main pods only)
  {{- if and .Values.multiMain.enabled .Values.license.enabled }}
  N8N_MULTI_MAIN_SETUP_ENABLED: "true"
  {{- if .Values.multiMain.setup.keyTtl }}
  N8N_MULTI_MAIN_SETUP_KEY_TTL: "{{ .Values.multiMain.setup.keyTtl }}"
  {{- end }}
  {{- if .Values.multiMain.setup.checkInterval }}
  N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL: "{{ .Values.multiMain.setup.checkInterval }}"
  {{- end }}
  {{- end }}
  
  # ----- Webhook Processor Configuration -----
  {{- if .Values.webhookProcessor.enabled }}
  # Main process disable (when webhook processors are enabled)
  {{- if .Values.webhookProcessor.disableProductionWebhooksOnMainProcess }}
  N8N_DISABLE_PRODUCTION_MAIN_PROCESS: "true"
  {{- end }}
  {{- end }}
```

## File: `charts/n8n/templates/deployment-main.yaml`
```yaml
{{- include "n8n.validate" . -}}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "n8n.fullname" . }}-main
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: main
spec:
  replicas: {{ ternary .Values.multiMain.replicas .Values.replicaCount .Values.multiMain.enabled }}
  revisionHistoryLimit: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "n8n.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
      app.kubernetes.io/component: main
  template:
    metadata:
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
        checksum/secret: {{ include (print $.Template.BasePath "/secrets.yaml") . | sha256sum }}
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
      labels:
        {{- include "n8n.labels" . | nindent 8 }}
        app.kubernetes.io/component: main
    spec:
      {{- with include "n8n.serviceAccountName" . }}
      serviceAccountName: {{ . }}
      {{- end }}

      {{- if .Values.securityContext.enabled }}
      securityContext:
        fsGroup: {{ .Values.securityContext.fsGroup }}
        runAsUser: {{ .Values.securityContext.runAsUser }}
        runAsGroup: {{ .Values.securityContext.runAsGroup }}
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      {{- end }}

      {{- with .Values.lifecycle.main.terminationGracePeriodSeconds }}
      terminationGracePeriodSeconds: {{ . }}
      {{- end }}

      containers:
        - name: n8n-main
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL

          {{- if .Values.lifecycle.main.preStop.enabled }}
          lifecycle:
            preStop:
              exec:
                command:
                  {{- toYaml .Values.lifecycle.main.preStop.command | nindent 18 }}
          {{- end }}

          env:
            {{- with .Values.webhook.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

            # Shared configuration from ConfigMap
            {{- include "n8n.sharedConfigMapEnv" . | nindent 12 }}
            
            # Main-specific configuration from ConfigMap
            {{- include "n8n.mainConfigMapEnv" . | nindent 12 }}
            
            {{- if .Values.database.useExternal }}
            # Database password (secret)
            - name: DB_POSTGRESDB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.database.passwordSecret.name }}
                  key: {{ .Values.database.passwordSecret.key }}
            {{- end }}
            {{- if .Values.queueMode.enabled }}
            # Redis password (secret)
            {{- with .Values.redis.passwordSecret }}
            {{- if and .name .key }}
            - name: QUEUE_BULL_REDIS_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .name }}
                  key: {{ .key }}
            {{- end }}
            {{- end }}

            # Health check settings
            {{- if .Values.redis.healthCheck.enabled }}
            - name: QUEUE_HEALTH_CHECK_ACTIVE
              value: "true"
            - name: QUEUE_HEALTH_CHECK_PORT
              value: "{{ .Values.redis.healthCheck.port }}"
            {{- end }}

            # Redis-specific extra environment variables
            {{- with .Values.redis.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}
            {{- end }}

            # S3 External Storage
            {{- include "n8n.s3Env" . | nindent 12 }}

            # Executions Configuration  
            {{- include "n8n.executionsEnv" . | nindent 12 }}

            # License Configuration
            {{- include "n8n.licenseEnv" . | nindent 12 }}

            # Core n8n secrets
            {{- include "n8n.coreSecretsEnv" . | nindent 12 }}

            # Task Runners Configuration
            {{- include "n8n.taskRunnerBrokerEnv" . | nindent 12 }}

            {{- with .Values.config.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

          {{- with .Values.config.extraEnvFrom }}
          envFrom:
            {{- toYaml . | nindent 12 }}
          {{- end }}

          ports:
            - containerPort: {{ .Values.service.port }}
              name: http

          # Probes
          startupProbe:
            httpGet:
              path: /healthz
              port: http
            failureThreshold: 30
            periodSeconds: 10

          {{- if .Values.probes.readiness.enabled }}
          readinessProbe:
            httpGet:
              path: {{ .Values.probes.readiness.path }}
              port: http
            initialDelaySeconds: {{ .Values.probes.readiness.initialDelaySeconds }}
            periodSeconds: {{ .Values.probes.readiness.periodSeconds }}
            timeoutSeconds: {{ .Values.probes.readiness.timeoutSeconds }}
            failureThreshold: {{ .Values.probes.readiness.failureThreshold }}
          {{- end }}

          {{- if .Values.probes.liveness.enabled }}
          livenessProbe:
            httpGet:
              path: {{ .Values.probes.liveness.path }}
              port: http
            initialDelaySeconds: {{ .Values.probes.liveness.initialDelaySeconds }}
            periodSeconds: {{ .Values.probes.liveness.periodSeconds }}
            timeoutSeconds: {{ .Values.probes.liveness.timeoutSeconds }}
            failureThreshold: {{ .Values.probes.liveness.failureThreshold }}
          {{- end }}

          resources:
            {{- toYaml .Values.resources.main | nindent 12 }}

          # Persist n8n home for SQLite DB and files
          volumeMounts:
            - name: data
              mountPath: /home/node/.n8n
            {{- with .Values.extraVolumeMounts }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

        {{- if .Values.taskRunners.enabled }}
        # Task Runner sidecar container
        - name: task-runner
          image: "{{ .Values.taskRunners.image.repository }}:{{ default .Values.image.tag .Values.taskRunners.image.tag }}"
          imagePullPolicy: {{ .Values.taskRunners.image.pullPolicy }}
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL

          env:
            {{- include "n8n.taskRunnerSidecarEnv" . | nindent 12 }}

          resources:
            {{- toYaml .Values.taskRunners.resources | nindent 12 }}

          {{- if .Values.taskRunners.customConfig.enabled }}
          volumeMounts:
            - name: task-runner-config
              mountPath: /etc/n8n-task-runners.json
              subPath: {{ .Values.taskRunners.customConfig.configMapKey }}
              readOnly: true
          {{- end }}
        {{- end }}

      # Volumes: prefer PVC, fallback to emptyDir if persistence disabled
      volumes:
        {{- if .Values.persistence.enabled }}
        - name: data
          persistentVolumeClaim:
            claimName: {{ if .Values.persistence.existingClaim }}{{ .Values.persistence.existingClaim }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
        {{- else }}
        - name: data
          emptyDir: {}
        {{- end }}
        {{- if and .Values.taskRunners.enabled .Values.taskRunners.customConfig.enabled }}
        - name: task-runner-config
          configMap:
            name: {{ .Values.taskRunners.customConfig.configMapName }}
        {{- end }}
        {{- with .Values.extraVolumes }}
        {{- toYaml . | nindent 8 }}
        {{- end }}

      {{- with .Values.nodeSelector }}
      nodeSelector: {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations: {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- if .Values.affinity }}
      affinity: {{- toYaml .Values.affinity | nindent 8 }}
      {{- else if and .Values.multiMain.enabled (ne .Values.multiMain.antiAffinity.type "none") }}
      affinity:
        podAntiAffinity:
          {{- if eq .Values.multiMain.antiAffinity.type "required" }}
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchLabels:
                  app.kubernetes.io/name: {{ include "n8n.name" . }}
                  app.kubernetes.io/instance: {{ .Release.Name }}
                  app.kubernetes.io/component: main
              topologyKey: kubernetes.io/hostname
          {{- else }}
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    app.kubernetes.io/name: {{ include "n8n.name" . }}
                    app.kubernetes.io/instance: {{ .Release.Name }}
                    app.kubernetes.io/component: main
                topologyKey: kubernetes.io/hostname
          {{- end }}
      {{- end }}
      {{- if and .Values.multiMain.enabled .Values.multiMain.topologySpreadConstraints.enabled }}
      topologySpreadConstraints:
        - maxSkew: {{ .Values.multiMain.topologySpreadConstraints.maxSkew }}
          topologyKey: kubernetes.io/hostname
          whenUnsatisfiable: {{ .Values.multiMain.topologySpreadConstraints.whenUnsatisfiable }}
          labelSelector:
            matchLabels:
              app.kubernetes.io/name: {{ include "n8n.name" . }}
              app.kubernetes.io/instance: {{ .Release.Name }}
              app.kubernetes.io/component: main
      {{- end }}
```

## File: `charts/n8n/templates/deployment-webhook-processor.yaml`
```yaml
{{- if and .Values.webhookProcessor.enabled .Values.queueMode.enabled }}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "n8n.fullname" . }}-webhook-processor
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: webhook-processor
spec:
  replicas: {{ .Values.webhookProcessor.replicaCount }}
  revisionHistoryLimit: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "n8n.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
      app.kubernetes.io/component: webhook-processor
  template:
    metadata:
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
        checksum/secret: {{ include (print $.Template.BasePath "/secrets.yaml") . | sha256sum }}
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
      labels:
        {{- include "n8n.labels" . | nindent 8 }}
        app.kubernetes.io/component: webhook-processor
    spec:
      {{- with include "n8n.serviceAccountName" . }}
      serviceAccountName: {{ . }}
      {{- end }}

      {{- if .Values.securityContext.enabled }}
      securityContext:
        fsGroup: {{ .Values.securityContext.fsGroup }}
        runAsUser: {{ .Values.securityContext.runAsUser }}
        runAsGroup: {{ .Values.securityContext.runAsGroup }}
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      {{- end }}

      {{- with .Values.lifecycle.webhookProcessor.terminationGracePeriodSeconds }}
      terminationGracePeriodSeconds: {{ . }}
      {{- end }}

      containers:
        - name: n8n-webhook-processor
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          command: ["n8n"]
          args: ["webhook"]
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL

          {{- if .Values.lifecycle.webhookProcessor.preStop.enabled }}
          lifecycle:
            preStop:
              exec:
                command:
                  {{- toYaml .Values.lifecycle.webhookProcessor.preStop.command | nindent 18 }}
          {{- end }}

          env:
            # Shared configuration from ConfigMap
            {{- include "n8n.sharedConfigMapEnv" . | nindent 12 }}
            
            # Webhook processor-specific configuration from ConfigMap
            {{- include "n8n.webhookProcessorConfigMapEnv" . | nindent 12 }}
            
            # Database password (secret)
            - name: DB_POSTGRESDB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.database.passwordSecret.name }}
                  key: {{ .Values.database.passwordSecret.key }}
            # Redis password (secret)
            {{- with .Values.redis.passwordSecret }}
            {{- if and .name .key }}
            - name: QUEUE_BULL_REDIS_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .name }}
                  key: {{ .key }}
            {{- end }}
            {{- end }}
            
            # Redis-specific extra environment variables
            {{- with .Values.redis.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}
            
            # Webhook-specific extra environment variables
            {{- with .Values.webhook.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

            # ----------------- License (for n8n Enterprise) -----------------
            {{- if .Values.license.enabled }}
            {{- if .Values.license.activationKey }}
            - name: N8N_LICENSE_ACTIVATION_KEY
              value: {{ .Values.license.activationKey | quote }}
            {{- else if .Values.license.existingSecret.name }}
            - name: N8N_LICENSE_ACTIVATION_KEY
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.license.existingSecret.name }}
                  key: {{ .Values.license.existingSecret.key }}
            {{- end }}
            {{- end }}

            # ----------------- Core n8n secrets -----------------
            - name: N8N_ENCRYPTION_KEY
              valueFrom:
                secretKeyRef:
                  name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
                  key: N8N_ENCRYPTION_KEY
            - name: N8N_HOST
              valueFrom:
                secretKeyRef:
                  name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
                  key: N8N_HOST
            - name: N8N_PORT
              valueFrom:
                secretKeyRef:
                  name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
                  key: N8N_PORT
            - name: N8N_PROTOCOL
              valueFrom:
                secretKeyRef:
                  name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
                  key: N8N_PROTOCOL

            {{- with .Values.config.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

          {{- with .Values.config.extraEnvFrom }}
          envFrom:
            {{- toYaml . | nindent 12 }}
          {{- end }}

          ports:
            - containerPort: {{ .Values.service.port }}
              name: http

          # --- Probes ---
          startupProbe:
            httpGet:
              path: /healthz
              port: http
            failureThreshold: 30
            periodSeconds: 10

          {{- if .Values.probes.readiness.enabled }}
          readinessProbe:
            httpGet:
              path: {{ .Values.probes.readiness.path }}
              port: http
            initialDelaySeconds: {{ .Values.probes.readiness.initialDelaySeconds }}
            periodSeconds: {{ .Values.probes.readiness.periodSeconds }}
            timeoutSeconds: {{ .Values.probes.readiness.timeoutSeconds }}
            failureThreshold: {{ .Values.probes.readiness.failureThreshold }}
          {{- end }}

          {{- if .Values.probes.liveness.enabled }}
          livenessProbe:
            httpGet:
              path: {{ .Values.probes.liveness.path }}
              port: http
            initialDelaySeconds: {{ .Values.probes.liveness.initialDelaySeconds }}
            periodSeconds: {{ .Values.probes.liveness.periodSeconds }}
            timeoutSeconds: {{ .Values.probes.liveness.timeoutSeconds }}
            failureThreshold: {{ .Values.probes.liveness.failureThreshold }}
          {{- end }}

          resources:
            {{- toYaml .Values.resources.webhookProcessor | nindent 12 }}

          # Volume mounts for external volumes
          volumeMounts:
            {{- with .Values.extraVolumeMounts }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

      # External volumes
      volumes:
        {{- with .Values.extraVolumes }}
        {{- toYaml . | nindent 8 }}
        {{- end }}

      {{- with .Values.nodeSelector }}
      nodeSelector: {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations: {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity: {{- toYaml . | nindent 8 }}
      {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/deployment-worker.yaml`
```yaml
{{- if .Values.queueMode.enabled -}}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "n8n.fullname" . }}-worker
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: worker
spec:
  replicas: {{ .Values.queueMode.workerReplicaCount }}
  revisionHistoryLimit: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "n8n.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
      app.kubernetes.io/component: worker
  template:
    metadata:
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
        checksum/secret: {{ include (print $.Template.BasePath "/secrets.yaml") . | sha256sum }}
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
      labels:
        {{- include "n8n.labels" . | nindent 8 }}
        app.kubernetes.io/component: worker
    spec:
      {{- with include "n8n.serviceAccountName" . }}
      serviceAccountName: {{ . }}
      {{- end }}

      {{- if .Values.securityContext.enabled }}
      securityContext:
        fsGroup: {{ .Values.securityContext.fsGroup }}
        runAsUser: {{ .Values.securityContext.runAsUser }}
        runAsGroup: {{ .Values.securityContext.runAsGroup }}
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      {{- end }}

      {{- with .Values.lifecycle.worker.terminationGracePeriodSeconds }}
      terminationGracePeriodSeconds: {{ . }}
      {{- end }}

      containers:
        - name: n8n-worker
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          command: ["n8n"]
          args:
            - "worker"
            - "--concurrency={{ .Values.queueMode.workerConcurrency }}"
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL

          {{- if .Values.lifecycle.worker.preStop.enabled }}
          lifecycle:
            preStop:
              exec:
                command:
                  {{- toYaml .Values.lifecycle.worker.preStop.command | nindent 18 }}
          {{- end }}

          env:
            # Shared configuration from ConfigMap
            {{- include "n8n.sharedConfigMapEnv" . | nindent 12 }}

            # Webhook URL for resume/waiting URLs
            {{- include "n8n.workerConfigMapEnv" . | nindent 12 }}

            # Database password (secret)
            - name: DB_POSTGRESDB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.database.passwordSecret.name }}
                  key: {{ .Values.database.passwordSecret.key }}

            # Redis password (secret)
            {{- with .Values.redis.passwordSecret }}
            {{- if and .name .key }}
            - name: QUEUE_BULL_REDIS_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .name }}
                  key: {{ .key }}
            {{- end }}
            {{- end }}

            # Health check settings (not in ConfigMap as it's optional)
            {{- if .Values.redis.healthCheck.enabled }}
            - name: QUEUE_HEALTH_CHECK_ACTIVE
              value: "true"
            - name: QUEUE_HEALTH_CHECK_PORT
              value: "{{ .Values.redis.healthCheck.port }}"
            {{- end }}

            # Redis-specific extra environment variables
            {{- with .Values.redis.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

            # S3 External Storage
            {{- include "n8n.s3Env" . | nindent 12 }}

            # Executions Configuration
            {{- include "n8n.executionsEnv" . | nindent 12 }}

            # License Configuration
            {{- include "n8n.licenseEnv" . | nindent 12 }}

            # N8N encryption key
            - name: N8N_ENCRYPTION_KEY
              valueFrom:
                secretKeyRef:
                  name: {{ if .Values.secretRefs.existingSecret }}{{ .Values.secretRefs.existingSecret }}{{ else }}{{ include "n8n.fullname" . }}{{ end }}
                  key: N8N_ENCRYPTION_KEY

            # Task Runners Configuration
            {{- include "n8n.taskRunnerBrokerEnv" . | nindent 12 }}

            {{- with .Values.config.extraEnv }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

          {{- with .Values.config.extraEnvFrom }}
          envFrom:
            {{- toYaml . | nindent 12 }}
          {{- end }}

          # Worker Health Probes
          {{- if .Values.probes.worker.readiness.enabled }}
          readinessProbe:
            {{- if and .Values.redis.healthCheck.enabled (eq .Values.probes.worker.readiness.type "httpGet") }}
            httpGet:
              path: {{ .Values.probes.worker.readiness.path | default "/healthz" }}
              port: {{ .Values.redis.healthCheck.port | default 5678 }}
            {{- else }}
            exec:
              command:
                {{- toYaml .Values.probes.worker.readiness.command | nindent 16 }}
            {{- end }}
            initialDelaySeconds: {{ .Values.probes.worker.readiness.initialDelaySeconds }}
            periodSeconds: {{ .Values.probes.worker.readiness.periodSeconds }}
            timeoutSeconds: {{ .Values.probes.worker.readiness.timeoutSeconds }}
            failureThreshold: {{ .Values.probes.worker.readiness.failureThreshold }}
          {{- end }}

          {{- if .Values.probes.worker.liveness.enabled }}
          livenessProbe:
            # Workers don't expose an HTTP endpoint; only exec probes are supported here.
            exec:
              command:
                {{- toYaml .Values.probes.worker.liveness.command | nindent 16 }}
            initialDelaySeconds: {{ .Values.probes.worker.liveness.initialDelaySeconds }}
            periodSeconds: {{ .Values.probes.worker.liveness.periodSeconds }}
            timeoutSeconds: {{ .Values.probes.worker.liveness.timeoutSeconds }}
            failureThreshold: {{ .Values.probes.worker.liveness.failureThreshold }}
          {{- end }}

          resources:
            {{- toYaml .Values.resources.worker | nindent 12 }}

          # Volume mounts for external volumes
          volumeMounts:
            {{- with .Values.extraVolumeMounts }}
            {{- toYaml . | nindent 12 }}
            {{- end }}

        {{- if .Values.taskRunners.enabled }}
        # Task Runner sidecar container
        - name: task-runner
          image: "{{ .Values.taskRunners.image.repository }}:{{ default .Values.image.tag .Values.taskRunners.image.tag }}"
          imagePullPolicy: {{ .Values.taskRunners.image.pullPolicy }}
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL

          env:
            {{- include "n8n.taskRunnerSidecarEnv" . | nindent 12 }}

          resources:
            {{- toYaml .Values.taskRunners.resources | nindent 12 }}

          {{- if .Values.taskRunners.customConfig.enabled }}
          volumeMounts:
            - name: task-runner-config
              mountPath: /etc/n8n-task-runners.json
              subPath: {{ .Values.taskRunners.customConfig.configMapKey }}
              readOnly: true
          {{- end }}
        {{- end }}

      # External volumes
      volumes:
        {{- if and .Values.taskRunners.enabled .Values.taskRunners.customConfig.enabled }}
        - name: task-runner-config
          configMap:
            name: {{ .Values.taskRunners.customConfig.configMapName }}
        {{- end }}
        {{- with .Values.extraVolumes }}
        {{- toYaml . | nindent 8 }}
        {{- end }}

      {{- with .Values.nodeSelector }}
      nodeSelector: {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations: {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity: {{- toYaml . | nindent 8 }}
      {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/hpa-main.yaml`
```yaml
{{- if .Values.hpa.main.enabled }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ include "n8n.fullname" . }}-main
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: main
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ include "n8n.fullname" . }}-main
  minReplicas: {{ .Values.hpa.main.minReplicas }}
  maxReplicas: {{ .Values.hpa.main.maxReplicas }}
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: {{ .Values.hpa.main.targetCPUUtilizationPercentage }}
    {{- if hasKey .Values.hpa.main "targetMemoryUtilizationPercentage" }}
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: {{ .Values.hpa.main.targetMemoryUtilizationPercentage }}
    {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/hpa-webhook-processor.yaml`
```yaml
{{- if and .Values.webhookProcessor.enabled .Values.hpa.webhookProcessor.enabled (not .Values.keda.enabled) }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ include "n8n.fullname" . }}-webhook-processor
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: webhook-processor
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ include "n8n.fullname" . }}-webhook-processor
  minReplicas: {{ .Values.hpa.webhookProcessor.minReplicas }}
  maxReplicas: {{ .Values.hpa.webhookProcessor.maxReplicas }}
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: {{ .Values.hpa.webhookProcessor.targetCPUUtilizationPercentage }}
    {{- if hasKey .Values.hpa.webhookProcessor "targetMemoryUtilizationPercentage" }}
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: {{ .Values.hpa.webhookProcessor.targetMemoryUtilizationPercentage }}
    {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/hpa-worker.yaml`
```yaml
{{- if and .Values.hpa.worker.enabled .Values.queueMode.enabled (not .Values.keda.enabled) }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ include "n8n.fullname" . }}-worker
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: worker
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ include "n8n.fullname" . }}-worker
  minReplicas: {{ .Values.hpa.worker.minReplicas }}
  maxReplicas: {{ .Values.hpa.worker.maxReplicas }}
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: {{ .Values.hpa.worker.targetCPUUtilizationPercentage }}
    {{- if hasKey .Values.hpa.worker "targetMemoryUtilizationPercentage" }}
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: {{ .Values.hpa.worker.targetMemoryUtilizationPercentage }}
    {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/ingress-webhook.yaml`
```yaml
{{- if and .Values.webhookProcessor.enabled ((.Values.ingress).webhookProcessor).enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ include "n8n.fullname" . }}-webhook-processor
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: webhook-processor
  {{- with (.Values.ingress.webhookProcessor).annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  {{- with (.Values.ingress.webhookProcessor).className }}
  ingressClassName: {{ . }}
  {{- end }}
  rules:
  {{- range .Values.ingress.hosts }}
    - host: {{ .host | quote }}
      http:
        paths:
          - path: /webhook/
            pathType: Prefix
            backend:
              service:
                name: {{ include "n8n.fullname" $ }}-webhook-processor
                port:
                  number: {{ $.Values.service.port }}
          - path: /webhook-waiting/
            pathType: Prefix
            backend:
              service:
                name: {{ include "n8n.fullname" $ }}-webhook-processor
                port:
                  number: {{ $.Values.service.port }}
  {{- end }}
  {{- with (.Values.ingress.webhookProcessor).tls }}
  tls:
    {{- toYaml . | nindent 4 }}
  {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/ingress.yaml`
```yaml
{{- if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ include "n8n.fullname" . }}-main
  namespace: {{ .Release.Namespace }}
  annotations:
    {{- with .Values.ingress.annotations }}{{ toYaml . | nindent 4 }}{{- end }}
    {{- if and .Values.ingress.sticky.enabled (or (eq .Values.ingress.className "nginx") (hasKey (default dict .Values.ingress.annotations) "kubernetes.io/ingress.class")) }}
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: {{ .Values.ingress.sticky.cookieName | quote }}
    nginx.ingress.kubernetes.io/session-cookie-expires: {{ .Values.ingress.sticky.cookieExpires | quote }}
    nginx.ingress.kubernetes.io/session-cookie-max-age: {{ .Values.ingress.sticky.cookieMaxAge | quote }}
    {{- end }}
spec:
  {{- if .Values.ingress.className }}
  ingressClassName: {{ .Values.ingress.className }}
  {{- end }}
  rules:
  {{- range .Values.ingress.hosts }}
    - host: {{ .host | quote }}
      http:
        paths:
        {{- range .paths }}
          - path: {{ .path }}
            pathType: {{ .pathType }}
            backend:
              service:
                name: {{ include "n8n.fullname" $ }}-main
                port:
                  number: {{ $.Values.service.port }}
        {{- end }}
  {{- end }}
  {{- if .Values.ingress.tls }}
  tls:
    {{- toYaml .Values.ingress.tls | nindent 4 }}
  {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/networkpolicy.yaml`
```yaml
{{- if .Values.networkPolicy.enabled }}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: {{ include "n8n.fullname" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/name: {{ include "n8n.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
  policyTypes: [Ingress, Egress]
  ingress:
    # Allow intra-pod communication (main <-> worker <-> webhook-processor)
    - from:
        - podSelector:
            matchLabels:
              app.kubernetes.io/name: {{ include "n8n.name" . }}
              app.kubernetes.io/instance: {{ .Release.Name }}
      ports:
        - protocol: TCP
          port: {{ .Values.service.port }}
    # Allow external ingress (load balancers, ingress controllers)
    - from: []
      ports:
        - protocol: TCP
          port: {{ .Values.service.port }}
  egress:
    # Allow DNS resolution
    - to: []
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
    {{- if .Values.database.useExternal }}
    # Allow PostgreSQL
    - to: []
      ports:
        - protocol: TCP
          port: {{ .Values.database.port }}
    {{- end }}
    {{- if .Values.queueMode.enabled }}
    # Allow Redis
    - to: []
      ports:
        - protocol: TCP
          port: {{ .Values.redis.port }}
    {{- end }}
    # Allow HTTPS (for webhooks, external APIs, license checks)
    - to: []
      ports:
        - protocol: TCP
          port: 443
{{- end }}
```

## File: `charts/n8n/templates/pdb.yaml`
```yaml
{{- if .Values.pdb.enabled }}
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: {{ include "n8n.fullname" . }}-main
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
spec:
  minAvailable: {{ .Values.pdb.minAvailable }}
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "n8n.name" . }}
      app.kubernetes.io/component: main
      app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

## File: `charts/n8n/templates/pvc.yaml`
```yaml
{{- if and .Values.persistence.enabled (not .Values.persistence.existingClaim) }}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ include "n8n.fullname" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
spec:
  accessModes: {{ toYaml .Values.persistence.accessModes | nindent 2 }}
  resources:
    requests:
      storage: {{ .Values.persistence.size }}
  {{- if .Values.persistence.storageClassName }}
  storageClassName: {{ .Values.persistence.storageClassName }}
  {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/role.yaml`
```yaml
{{- if .Values.rbac.create }}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: {{ include "n8n.fullname" . }}
  namespace: {{ .Release.Namespace }}
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get","list"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]
{{- end }}
```

## File: `charts/n8n/templates/rolebinding.yaml`
```yaml
{{- if .Values.rbac.create }}
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: {{ include "n8n.fullname" . }}
  namespace: {{ .Release.Namespace }}
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: {{ include "n8n.fullname" . }}
subjects:
  - kind: ServiceAccount
    name: {{ default (include "n8n.fullname" .) .Values.serviceAccount.name }}
    namespace: {{ .Release.Namespace }}
{{- end }}
```

## File: `charts/n8n/templates/scaledobject-webhook-processor.yaml`
```yaml
{{- if and .Values.keda.enabled .Values.keda.webhookProcessor.enabled .Values.webhookProcessor.enabled .Values.queueMode.enabled }}
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: {{ include "n8n.fullname" . }}-webhook-processor
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: webhook-processor
spec:
  scaleTargetRef:
    name: {{ include "n8n.fullname" . }}-webhook-processor
  pollingInterval: {{ .Values.keda.webhookProcessor.pollingInterval }}
  cooldownPeriod: {{ .Values.keda.webhookProcessor.cooldownPeriod }}
  minReplicaCount: {{ .Values.keda.webhookProcessor.minReplicaCount }}
  maxReplicaCount: {{ .Values.keda.webhookProcessor.maxReplicaCount }}
  triggers:
    {{- range .Values.keda.webhookProcessor.triggers }}
    - type: {{ .type }}
      metadata:
        {{- $address := .metadata.address }}
        {{- if and (eq .type "redis") (eq (default "" $address) "") }}
        address: "{{ $.Values.redis.host }}:{{ $.Values.redis.port }}"
        {{- else }}
        address: {{ $address | quote }}
        {{- end }}
        {{- range $key, $value := .metadata }}
        {{- if ne $key "address" }}
        {{ $key }}: {{ $value | quote }}
        {{- end }}
        {{- end }}
      {{- if and .authenticationRef .authenticationRef.name }}
      authenticationRef:
        name: {{ .authenticationRef.name }}
      {{- end }}
    {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/scaledobject-worker.yaml`
```yaml
{{- if and .Values.keda.enabled .Values.queueMode.enabled }}
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: {{ include "n8n.fullname" . }}-worker
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: worker
spec:
  scaleTargetRef:
    name: {{ include "n8n.fullname" . }}-worker
  pollingInterval: {{ .Values.keda.worker.pollingInterval }}
  cooldownPeriod: {{ .Values.keda.worker.cooldownPeriod }}
  minReplicaCount: {{ .Values.keda.worker.minReplicaCount }}
  maxReplicaCount: {{ .Values.keda.worker.maxReplicaCount }}
  triggers:
    {{- range .Values.keda.worker.triggers }}
    - type: {{ .type }}
      metadata:
        {{- $address := .metadata.address }}
        {{- if and (eq .type "redis") (eq (default "" $address) "") }}
        address: "{{ $.Values.redis.host }}:{{ $.Values.redis.port }}"
        {{- else }}
        address: {{ $address | quote }}
        {{- end }}
        {{- range $key, $value := .metadata }}
        {{- if ne $key "address" }}
        {{ $key }}: {{ $value | quote }}
        {{- end }}
        {{- end }}
      {{- if and .authenticationRef .authenticationRef.name }}
      authenticationRef:
        name: {{ .authenticationRef.name }}
      {{- end }}
    {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/secret-task-runners.yaml`
```yaml
{{- if not .Values.taskRunners.authToken.existingSecret -}}
apiVersion: v1
kind: Secret
metadata:
  name: {{ include "n8n.fullname" . }}-task-runners
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
type: Opaque
data:
  {{- if .Values.taskRunners.authToken.value }}
  N8N_RUNNERS_AUTH_TOKEN: {{ .Values.taskRunners.authToken.value | b64enc | quote }}
  {{- else }}
  {{- /* Use lookup to preserve existing token across upgrades */ -}}
  {{- $existing := lookup "v1" "Secret" .Release.Namespace (printf "%s-task-runners" (include "n8n.fullname" .)) }}
  {{- if and $existing $existing.data (index $existing.data "N8N_RUNNERS_AUTH_TOKEN") }}
  N8N_RUNNERS_AUTH_TOKEN: {{ index $existing.data "N8N_RUNNERS_AUTH_TOKEN" }}
  {{- else }}
  N8N_RUNNERS_AUTH_TOKEN: {{ randAlphaNum 32 | b64enc | quote }}
  {{- end }}
  {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/secrets.yaml`
```yaml
{{- if not .Values.secretRefs.existingSecret }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ include "n8n.fullname" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
type: Opaque
stringData:
{{- range $k, $v := .Values.secretRefs.env }}
  {{ $k }}: {{ $v | quote }}
{{- end }}
{{- end }}
```

## File: `charts/n8n/templates/service-main.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "n8n.fullname" . }}-main
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
  {{- $merged := merge (deepCopy (.Values.service.main.annotations | default dict)) (.Values.service.annotations | default dict) }}
  {{- with $merged }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app.kubernetes.io/name: {{ include "n8n.name" . }}
    app.kubernetes.io/component: main
    app.kubernetes.io/instance: {{ .Release.Name }}
  ports:
    - name: http
      port: {{ .Values.service.port }}
      targetPort: http
  {{- if .Values.service.sessionAffinity.enabled }}
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: {{ .Values.service.sessionAffinity.timeoutSeconds }}
  {{- end }}
```

## File: `charts/n8n/templates/service-webhook-processor.yaml`
```yaml
{{- if and .Values.webhookProcessor.enabled .Values.queueMode.enabled }}
apiVersion: v1
kind: Service
metadata:
  name: {{ include "n8n.fullname" . }}-webhook-processor
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
    app.kubernetes.io/component: webhook-processor
  {{- $merged := merge (deepCopy (.Values.service.webhookProcessor.annotations | default dict)) (.Values.service.annotations | default dict) }}
  {{- with $merged }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: {{ include "n8n.name" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/component: webhook-processor
  {{- if .Values.service.sessionAffinity.enabled }}
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: {{ .Values.service.sessionAffinity.timeoutSeconds }}
  {{- end }}
{{- end }}
```

## File: `charts/n8n/templates/serviceaccount.yaml`
```yaml
{{- if .Values.serviceAccount.create }}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ include "n8n.serviceAccountName" . }}
  namespace: {{ .Release.Namespace }}
  annotations:
    {{- if and .Values.s3.enabled .Values.s3.auth.autoDetect .Values.serviceAccount.awsRoleArn }}
    eks.amazonaws.com/role-arn: {{ .Values.serviceAccount.awsRoleArn }}
    {{- end }}
    {{- with .Values.serviceAccount.annotations }}{{ toYaml . | nindent 4 }}{{- end }}
{{- end }}
```

## File: `charts/n8n/templates/tests/test-connection.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "n8n.fullname" . }}-test-connection"
  labels:
    {{- include "n8n.labels" . | nindent 4 }}
  annotations:
    "helm.sh/hook": test
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  containers:
    - name: wget
      image: busybox:1.36
      command:
        - wget
        - "--spider"
        - "--timeout=10"
        - "http://{{ include "n8n.fullname" . }}-main:{{ .Values.service.port }}/healthz"
  restartPolicy: Never
```

## File: `docker-caddy/.env`
```
N8N_VERSION=2.12.2

# Replace <directory-path> with the path where you created folders earlier
DATA_FOLDER=/<directory-path>/n8n-docker-caddy

# The top level domain to serve from, this should be the same as the subdomain you created above
DOMAIN_NAME=example.com

# The subdomain to serve from
SUBDOMAIN=n8n

# DOMAIN_NAME and SUBDOMAIN combined decide where n8n will be reachable from
# above example would result in: https://n8n.example.com

# Optional timezone to set which gets used by Cron-Node by default
# If not set New York time will be used
GENERIC_TIMEZONE=Europe/Berlin

# The email address to use for the SSL certificate creation
SSL_EMAIL=example@example.com

RUNNERS_AUTH_TOKEN=changeRunnerAuthToken
```

## File: `docker-caddy/LICENSE`
```
MIT License

Copyright (c) 2022 n8n - Workflow Automation

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

## File: `docker-caddy/README.md`
```markdown
# n8n-docker-caddy

Get up and running with n8n on the following platforms:

* [DigitalOcean tutorial](https://docs.n8n.io/hosting/server-setups/digital-ocean/)
* [Hetzner Cloud tutorial](https://docs.n8n.io/hosting/server-setups/hetzner/)

If you have questions after trying the tutorials, check out the [forums](https://community.n8n.io/).

## Prerequisites

Self-hosting n8n requires technical knowledge, including:

* Setting up and configuring servers and containers
* Managing application resources and scaling
* Securing servers and applications
* Configuring n8n

n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, n8n recommends [n8n Cloud](https://n8n.io/cloud/).
```

## File: `docker-caddy/docker-compose.yml`
```yaml
version: "3.7"

services:
  caddy:
    image: caddy:latest
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - caddy_data:/data
      - ${DATA_FOLDER}/caddy_config:/config
      - ${DATA_FOLDER}/caddy_config/Caddyfile:/etc/caddy/Caddyfile

  n8n:
    image: docker.n8n.io/n8nio/n8n:${N8N_VERSION}
    restart: always
    ports:
      - 5678:5678
    environment:
      - N8N_HOST=${SUBDOMAIN}.${DOMAIN_NAME}
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
      - NODE_ENV=production
      - WEBHOOK_URL=https://${SUBDOMAIN}.${DOMAIN_NAME}/
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - N8N_RUNNERS_MODE=external
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0
    volumes:
      - n8n_data:/home/node/.n8n
      - ${DATA_FOLDER}/local_files:/files

  n8n-runner:
    image: n8nio/runners:${N8N_VERSION}
    restart: always
    environment:
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_TASK_BROKER_URI=http://n8n:5679
    depends_on:
      - n8n

volumes:
  caddy_data:
    external: true
  n8n_data:
    external: true
```

## File: `docker-caddy/caddy_config/Caddyfile`
```
n8n.<domain>.<suffix> {
    reverse_proxy n8n:5678 {
      flush_interval -1
    }
}
```

## File: `docker-compose/subfolderWithSSL/.env`
```
N8N_VERSION=2.12.2

# Folder where data should be saved
DATA_FOLDER=/root/n8n/

# The top level domain to serve from
DOMAIN_NAME=example.com

# The subfolder to serve from
SUBFOLDER=app1
N8N_PATH=/app1/

# DOMAIN_NAME and SUBDOMAIN combined decide where n8n will be reachable from
# above example would result in: https://example.com/app1/

# Optional timezone to set which gets used by Cron-Node by default
# If not set New York time will be used
GENERIC_TIMEZONE=Europe/Berlin

# The email address to use for the SSL certificate creation
SSL_EMAIL=user@example.com

RUNNERS_AUTH_TOKEN=changeRunnerAuthToken
```

## File: `docker-compose/subfolderWithSSL/README.md`
```markdown
# n8n on Subfolder with SSL

Starts n8n and deploys it on a subfolder

## Start

To start n8n in a subfolder simply start docker-compose by executing the following
command in the current folder.

**IMPORTANT:** But before you do that change the default users and passwords in the `.env` file!

```
docker-compose up -d
```

To stop it execute:

```
docker-compose stop
```
```

## File: `docker-compose/subfolderWithSSL/docker-compose.yml`
```yaml
version: '3'

services:
  traefik:
    image: 'traefik'
    command:
      - '--api=true'
      - '--api.insecure=true'
      - '--api.dashboard=true'
      - '--providers.docker=true'
      - '--providers.docker.exposedbydefault=false'
      - '--entrypoints.websecure.address=:443'
      - '--certificatesresolvers.mytlschallenge.acme.tlschallenge=true'
      - '--certificatesresolvers.mytlschallenge.acme.email=${SSL_EMAIL}'
      - '--certificatesresolvers.mytlschallenge.acme.storage=/letsencrypt/acme.json'
    ports:
      - '443:443'
      - '80:80'
    volumes:
      - ${DATA_FOLDER}/letsencrypt:/letsencrypt
      - /var/run/docker.sock:/var/run/docker.sock:ro

  initContainer:
    image: busybox
    command: ['sh', '-c', 'chown -R 1000:1000 /home/node/.n8n']
    volumes:
      - ${DATA_FOLDER}/.n8n:/home/node/.n8n

  n8n:
    image: docker.n8n.io/n8nio/n8n:${N8N_VERSION}
    ports:
      - '127.0.0.1:5678:5678'
    labels:
      - traefik.enable=true
      - 'traefik.http.routers.n8n.rule=Host(`${DOMAIN_NAME}`) && PathPrefix(`/${SUBFOLDER}`)'
      - traefik.http.routers.n8n.tls=true
      - traefik.http.routers.n8n.entrypoints=websecure
      - 'traefik.http.middlewares.n8n-stripprefix.stripprefix.prefixes=/${SUBFOLDER}'
      - 'traefik.http.routers.n8n.middlewares=n8n-stripprefix'
      - traefik.http.routers.n8n.tls.certresolver=mytlschallenge
      - traefik.http.middlewares.n8n.headers.SSLRedirect=true
      - traefik.http.middlewares.n8n.headers.STSSeconds=315360000
      - traefik.http.middlewares.n8n.headers.browserXSSFilter=true
      - traefik.http.middlewares.n8n.headers.contentTypeNosniff=true
      - traefik.http.middlewares.n8n.headers.forceSTSHeader=true
      - traefik.http.middlewares.n8n.headers.SSLHost=${DOMAIN_NAME}
      - traefik.http.middlewares.n8n.headers.STSIncludeSubdomains=true
      - traefik.http.middlewares.n8n.headers.STSPreload=true
    environment:
      - N8N_HOST=${DOMAIN_NAME}
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
      - NODE_ENV=production
      - N8N_PATH
      - WEBHOOK_URL=https://${DOMAIN_NAME}${N8N_PATH}
      - N8N_RUNNERS_MODE=external
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0
    volumes:
      - ${DATA_FOLDER}/.n8n:/home/node/.n8n
    depends_on:
      initContainer:
        condition: service_completed_successfully

  n8n-runner:
    image: n8nio/runners:${N8N_VERSION}
    restart: always
    environment:
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_TASK_BROKER_URI=http://n8n:5679
    depends_on:
      - n8n
```

## File: `docker-compose/withPostgres/.env`
```
N8N_VERSION=2.12.2

POSTGRES_USER=changeUser
POSTGRES_PASSWORD=changePassword
POSTGRES_DB=n8n

POSTGRES_NON_ROOT_USER=changeUser
POSTGRES_NON_ROOT_PASSWORD=changePassword

RUNNERS_AUTH_TOKEN=changeRunnerAuthToken
```

## File: `docker-compose/withPostgres/README.md`
```markdown
# n8n with PostgreSQL

Starts n8n with PostgreSQL as database.

## Start

To start n8n with PostgreSQL simply start docker-compose by executing the following
command in the current folder.

**IMPORTANT:** But before you do that change the default users and passwords in the [`.env`](.env) file!

```
docker-compose up -d
```

To stop it execute:

```
docker-compose stop
```

## Configuration

The default name of the database, user and password for PostgreSQL can be changed in the [`.env`](.env) file in the current directory.
```

## File: `docker-compose/withPostgres/docker-compose.yml`
```yaml
version: '3.8'

volumes:
  db_storage:
  n8n_storage:

services:
  postgres:
    image: postgres:16
    restart: always
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
      - POSTGRES_NON_ROOT_USER
      - POSTGRES_NON_ROOT_PASSWORD
    volumes:
      - db_storage:/var/lib/postgresql/data
      - ./init-data.sh:/docker-entrypoint-initdb.d/init-data.sh
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB}']
      interval: 5s
      timeout: 5s
      retries: 10

  n8n:
    image: docker.n8n.io/n8nio/n8n:${N8N_VERSION}
    restart: always
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=${POSTGRES_DB}
      - DB_POSTGRESDB_USER=${POSTGRES_NON_ROOT_USER}
      - DB_POSTGRESDB_PASSWORD=${POSTGRES_NON_ROOT_PASSWORD}
      - N8N_RUNNERS_MODE=external
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0
    ports:
      - 5678:5678
    links:
      - postgres
    volumes:
      - n8n_storage:/home/node/.n8n
    depends_on:
      postgres:
        condition: service_healthy

  n8n-runner:
    image: n8nio/runners:${N8N_VERSION}
    restart: always
    environment:
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_TASK_BROKER_URI=http://n8n:5679
    depends_on:
      - n8n
```

## File: `docker-compose/withPostgres/init-data.sh`
```bash
#!/bin/bash
set -e;


if [ -n "${POSTGRES_NON_ROOT_USER:-}" ] && [ -n "${POSTGRES_NON_ROOT_PASSWORD:-}" ]; then
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
		CREATE USER ${POSTGRES_NON_ROOT_USER} WITH PASSWORD '${POSTGRES_NON_ROOT_PASSWORD}';
		GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_NON_ROOT_USER};
		GRANT CREATE ON SCHEMA public TO ${POSTGRES_NON_ROOT_USER};
	EOSQL
else
	echo "SETUP INFO: No Environment variables given!"
fi
```

## File: `docker-compose/withPostgresAndWorker/.env`
```
N8N_VERSION=2.12.2

POSTGRES_USER=changeUser
POSTGRES_PASSWORD=changePassword
POSTGRES_DB=n8n

POSTGRES_NON_ROOT_USER=changeUser
POSTGRES_NON_ROOT_PASSWORD=changePassword

ENCRYPTION_KEY=changeEncryptionKey

RUNNERS_AUTH_TOKEN=changeRunnerAuthToken
```

## File: `docker-compose/withPostgresAndWorker/README.md`
```markdown
# n8n with PostgreSQL and Worker

Starts n8n with PostgreSQL as database, Redis for queue management, and a Worker as a separate container. Task runner sidecar containers are included for executing Code nodes (JavaScript/Python), as required by n8n 2.0+.

## Start

To start n8n simply start docker-compose by executing the following
command in the current folder.

**IMPORTANT:** But before you do that change the default users, passwords, and tokens in the [`.env`](.env) file!

```
docker compose up -d
```

To stop it execute:

```
docker compose stop
```

## Configuration

The default name of the database, user and password for PostgreSQL can be changed in the [`.env`](.env) file in the current directory.

The `RUNNERS_AUTH_TOKEN` in the [`.env`](.env) file is a shared secret used for authentication between n8n and the task runner containers. Generate a secure random value for production use.
```

## File: `docker-compose/withPostgresAndWorker/docker-compose.yml`
```yaml
volumes:
  db_storage:
  n8n_storage:
  redis_storage:

x-shared: &shared
  restart: always
  image: docker.n8n.io/n8nio/n8n:${N8N_VERSION}
  environment:
    - DB_TYPE=postgresdb
    - DB_POSTGRESDB_HOST=postgres
    - DB_POSTGRESDB_PORT=5432
    - DB_POSTGRESDB_DATABASE=${POSTGRES_DB}
    - DB_POSTGRESDB_USER=${POSTGRES_NON_ROOT_USER}
    - DB_POSTGRESDB_PASSWORD=${POSTGRES_NON_ROOT_PASSWORD}
    - EXECUTIONS_MODE=queue
    - QUEUE_BULL_REDIS_HOST=redis
    - QUEUE_HEALTH_CHECK_ACTIVE=true
    - N8N_ENCRYPTION_KEY=${ENCRYPTION_KEY}
    - N8N_RUNNERS_MODE=external
    - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
    - N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0
    - OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS=true
  volumes:
    - n8n_storage:/home/node/.n8n
  depends_on:
    redis:
      condition: service_healthy
    postgres:
      condition: service_healthy

x-runner: &runner
  restart: always
  image: n8nio/runners:${N8N_VERSION}
  environment:
    - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}

services:
  postgres:
    image: postgres:16
    restart: always
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
      - POSTGRES_NON_ROOT_USER
      - POSTGRES_NON_ROOT_PASSWORD
    volumes:
      - db_storage:/var/lib/postgresql/data
      - ./init-data.sh:/docker-entrypoint-initdb.d/init-data.sh
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB}']
      interval: 5s
      timeout: 5s
      retries: 10

  redis:
    image: redis:6-alpine
    restart: always
    volumes:
      - redis_storage:/data
    healthcheck:
      test: ['CMD', 'redis-cli', 'ping']
      interval: 5s
      timeout: 5s
      retries: 10

  n8n:
    <<: *shared
    ports:
      - 5678:5678

  n8n-runner:
    <<: *runner
    environment:
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_TASK_BROKER_URI=http://n8n:5679
    depends_on:
      - n8n

  n8n-worker:
    <<: *shared
    command: worker
    depends_on:
      - n8n

  n8n-worker-runner:
    <<: *runner
    environment:
      - N8N_RUNNERS_AUTH_TOKEN=${RUNNERS_AUTH_TOKEN}
      - N8N_RUNNERS_TASK_BROKER_URI=http://n8n-worker:5679
    depends_on:
      - n8n-worker
```

## File: `docker-compose/withPostgresAndWorker/init-data.sh`
```bash
#!/bin/bash
set -e;


if [ -n "${POSTGRES_NON_ROOT_USER:-}" ] && [ -n "${POSTGRES_NON_ROOT_PASSWORD:-}" ]; then
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
		CREATE USER ${POSTGRES_NON_ROOT_USER} WITH PASSWORD '${POSTGRES_NON_ROOT_PASSWORD}';
		GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_NON_ROOT_USER};
		GRANT CREATE ON SCHEMA public TO ${POSTGRES_NON_ROOT_USER};
	EOSQL
else
	echo "SETUP INFO: No Environment variables given!"
fi
```

## File: `kubernetes/LICENSE`
```
MIT License

Copyright (c) 2022 n8n - Workflow Automation

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

## File: `kubernetes/README.md`
```markdown
# n8n-kubernetes-hosting

> **For production Kubernetes deployments, use the official [n8n Helm chart](../charts/n8n/).** The raw manifests below are intended for tutorial-based deployments and simple setups.

Get up and running with n8n on the following platforms:

* [AWS](https://docs.n8n.io/hosting/server-setups/aws/)
* [Azure](https://docs.n8n.io/hosting/server-setups/azure/)
* [Google Cloud Platform](https://docs.n8n.io/hosting/server-setups/google-cloud/)

If you have questions after trying the tutorials, check out the [forums](https://community.n8n.io/).

## Prerequisites

Self-hosting n8n requires technical knowledge, including:

* Setting up and configuring servers and containers
* Managing application resources and scaling
* Securing servers and applications
* Configuring n8n

n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, n8n recommends [n8n Cloud](https://n8n.io/cloud/).

## Contributions

Please open PRs to the `main` branch.
```

## File: `kubernetes/n8n-claim0-persistentvolumeclaim.yaml`
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  labels:
    service: n8n-claim0
  name: n8n-claim0
  namespace: n8n
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
```

## File: `kubernetes/n8n-deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    service: n8n
  name: n8n
  namespace: n8n
spec:
  replicas: 1
  selector:
    matchLabels:
      service: n8n
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        service: n8n
    spec:
      initContainers:
        - name: volume-permissions
          image: busybox:1.36
          command: ["sh", "-c", "chown 1000:1000 /data"]
          volumeMounts:
            - name: n8n-claim0
              mountPath: /data
      containers:
        - command:
            - /bin/sh
          args:
            - -c
            - sleep 5; n8n start
          env:
            - name: DB_TYPE
              value: postgresdb
            - name: DB_POSTGRESDB_HOST
              value: postgres-service.n8n.svc.cluster.local
            - name: DB_POSTGRESDB_PORT
              value: "5432"
            - name: DB_POSTGRESDB_DATABASE
              value: n8n
            - name: DB_POSTGRESDB_USER
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_NON_ROOT_USER
            - name: DB_POSTGRESDB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_NON_ROOT_PASSWORD
            - name: N8N_PROTOCOL
              value: http
            - name: N8N_PORT
              value: "5678"
          image: n8nio/n8n
          name: n8n
          ports:
            - containerPort: 5678
          resources:
            requests:
              memory: "250Mi"
            limits:
              memory: "500Mi"
          volumeMounts:
            - mountPath: /home/node/.n8n
              name: n8n-claim0
      restartPolicy: Always
      volumes:
        - name: n8n-claim0
          persistentVolumeClaim:
            claimName: n8n-claim0
        - name: n8n-secret
          secret:
            secretName: n8n-secret
        - name: postgres-secret
          secret:
            secretName: postgres-secret
```

## File: `kubernetes/n8n-service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    service: n8n
  name: n8n
  namespace: n8n
spec:
  type: LoadBalancer
  ports:
    - name: "5678"
      port: 5678
      targetPort: 5678
      protocol: TCP
  selector:
    service: n8n
```

## File: `kubernetes/namespace.yaml`
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: n8n
```

## File: `kubernetes/postgres-claim0-persistentvolumeclaim.yaml`
```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: postgresql-pv
  namespace: n8n
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 300Gi
```

## File: `kubernetes/postgres-configmap.yaml`
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: init-data
  namespace: n8n
data:
  init-data.sh: |
    #!/bin/bash
    set -e;
    if [ -n "${POSTGRES_NON_ROOT_USER:-}" ] && [ -n "${POSTGRES_NON_ROOT_PASSWORD:-}" ]; then
    	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    		CREATE USER "${POSTGRES_NON_ROOT_USER}" WITH PASSWORD '${POSTGRES_NON_ROOT_PASSWORD}';
    		GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO "${POSTGRES_NON_ROOT_USER}";
    		GRANT ALL ON SCHEMA public TO "${POSTGRES_NON_ROOT_USER}";
    	EOSQL
    else
    	echo "SETUP INFO: No Environment variables given!"
    fi
```

## File: `kubernetes/postgres-deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    service: postgres-n8n
  name: postgres
  namespace: n8n
spec:
  replicas: 1
  selector:
    matchLabels:
      service: postgres-n8n
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        service: postgres-n8n
    spec:
      containers:
        - image: postgres:18
          name: postgres
          resources:
            limits:
              cpu: "4"
              memory: 4Gi
            requests:
              cpu: "1"
              memory: 2Gi
          ports:
            - containerPort: 5432
          volumeMounts:
            - name: postgresql-pv
              mountPath: /var/lib/postgresql/data
            - name: init-data
              mountPath: /docker-entrypoint-initdb.d/init-n8n-user.sh
              subPath: init-data.sh
          env:
            - name: PGDATA
              value: /var/lib/postgresql/data/pgdata      
            - name: POSTGRES_USER
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_USER
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_PASSWORD
            - name: POSTGRES_DB
              value: n8n
            - name: POSTGRES_NON_ROOT_USER
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_NON_ROOT_USER
            - name: POSTGRES_NON_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_NON_ROOT_PASSWORD
            - name:   POSTGRES_HOST
              value: postgres-service
            - name: POSTGRES_PORT
              value: '5432'
      restartPolicy: Always
      volumes:
        - name: postgresql-pv
          persistentVolumeClaim:
            claimName: postgresql-pv
        - name: postgres-secret
          secret:
            secretName: postgres-secret
        - name: init-data
          configMap:
            name: init-data
            defaultMode: 0744
```

## File: `kubernetes/postgres-secret.yaml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: n8n
  name: postgres-secret
type: Opaque
stringData:
  POSTGRES_USER: changeUser
  POSTGRES_PASSWORD: changePassword
  POSTGRES_DB: n8n
  POSTGRES_NON_ROOT_USER: changeUser
  POSTGRES_NON_ROOT_PASSWORD: changePassword
```

## File: `kubernetes/postgres-service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    service: postgres-n8n
  name: postgres-service
  namespace: n8n
spec:
  clusterIP: None
  ports:
    - name: "5432"
      port: 5432
      targetPort: 5432
      protocol: TCP
  selector:
    service: postgres-n8n
```

