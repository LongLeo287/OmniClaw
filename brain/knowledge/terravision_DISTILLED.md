---
id: terravision
type: knowledge
owner: OA_Triage
---
# terravision
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# TerraVision - Terraform Visualization tool and Architecture Diagram Generator

Visualise your Terraform code using official AWS/GCP/Azure design standards and icons to create solution architect grade architecture diagrams ready for audit, governance, team member and security reviews.

[![lint-and-test](https://github.com/patrickchugh/terravision/actions/workflows/lint-and-test.yml/badge.svg)](https://github.com/patrickchugh/terravision/actions/workflows/lint-and-test.yml)
[![PyPI version](https://img.shields.io/pypi/v/terravision?style=flat-square)](https://pypi.org/project/terravision/)
[![PyPI downloads](https://img.shields.io/pypi/dm/terravision?style=flat-square)](https://pypi.org/project/terravision/)
[![Python version](https://img.shields.io/pypi/pyversions/terravision?style=flat-square)](https://pypi.org/project/terravision/)
[![GitHub stars](https://img.shields.io/github/stars/patrickchugh/terravision?style=flat-square)](https://github.com/patrickchugh/terravision/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/patrickchugh/terravision?style=flat-square)](https://github.com/patrickchugh/terravision/network)
[![GitHub issues](https://img.shields.io/github/issues/patrickchugh/terravision?style=flat-square)](https://github.com/patrickchugh/terravision/issues)
[![License](https://img.shields.io/github/license/patrickchugh/terravision?style=flat-square)](https://github.com/patrickchugh/terravision/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

## Table of Contents

- [What is TerraVision?](#what-is-terravision)
- [Quick Start](#quick-start)
- [Key Features](#key-features)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Documentation](#documentation)
- [Supported Cloud Providers](#supported-cloud-providers)
- [Contributing](#contributing)
- [License](#license)

---

## What is TerraVision?

TerraVision automatically converts your Terraform code into professional grade cloud architecture diagrams. Quickly visualise any Terraform code to analyse what would be created in the cloud, AND keep your documentation in sync with your infrastructure. No more outdated diagrams!

**Turn this Terraform code:**

![Terraform Code](./images/code.png)

**Into these architecture diagrams:**

<a href="./images/architecture.png"><img src="./images/architecture.png" height="250"></a>
<a href="./images/architecture-azure.dot.png"><img src="./images/architecture-azure.dot.png" height="250"></a>
<a href="./images/architecture-gcp.dot.png"><img src="./images/architecture-gcp.dot.png" height="250"></a>

### Why TerraVision?

- ✅ **Always Up-to-Date**: Diagrams generated from actual Terraform code as the single source of truth
- ✅ **100% Client-Side**: No cloud access required, runs locally to keep your data secure
- ✅ **CI/CD Ready**: Automate diagram generation in a pipeline whenever a PR is merged
- ✅ **Free & Open Source**: No expensive diagramming tool licenses
- ✅ **Multi-Cloud**: Supports AWS, GCP, and Azure

---

## Key Features

### 🎨 Professional Diagrams

- Industry-standard cloud provider icons (AWS, GCP, Azure)
- Automatic resource grouping (VPCs, subnets, security groups)
- Clean, readable layouts
- Multiple output formats (PNG, SVG, PDF, JPG, and [many more](#supported-output-formats))
- **Editable draw.io export** - open in draw.io, Lucidchart, or your favorite diagram editor

### 🤖 AI-Powered Refinement

- Automatically fixes resource relationships
- Adds missing logical connections, labels, titles and icons as needed
- Ensures architectural diagramming best practices

### 📝 Customizable Annotations

- Add custom labels and titles
- Include external resources not in Terraform
- Override automatic connections

### 🔄 CI/CD Integration

- GitHub Actions, GitLab CI, Jenkins support
- Show multiple environments using TF Variables to document variants of your infrastructure (e.g. prod vs dev)
- **Pre-generated plan mode**: Use `--planfile` and `--graphfile` to skip Terraform execution entirely — no cloud credentials needed in the diagram step

### 🔒 Secure & Private

- No cloud credentials required
- Runs entirely on your local machine
- No external API calls (except optional AI features)

---

## Quick Start

### Option 1 - Docker

You can run `terravision` from within a Docker container. Pull the pre-built image from Docker Hub:

```sh
docker pull patrickchugh/terravision:latest
```

Or build it yourself from source:

```sh
git clone https://github.com/patrickchugh/terravision.git && cd terravision
docker build -t patrickchugh/terravision .
```

Then use it with any of your terraform files by mounting your local directory to the container:

If you pulled from Docker Hub, use `patrickchugh/terravision` as the image name. If you built locally, use `terravision` (or whatever tag you chose).

```sh
# Using Docker Hub image
$ docker run --rm -it -v $(pwd):/project patrickchugh/terravision draw --source /project/yourfiles/ --varfile /project/your.tfvars
$ docker run --rm -it -v $(pwd):/project patrickchugh/terravision draw --source https://github.com/your-repo/terraform-examples.git//mysubfolder/secondfolder/

# Using self-built image
$ docker run --rm -it -v $(pwd):/project terravision draw --source /project/yourfiles/ --varfile /project/your.tfvars
$ docker run --rm -it -v $(pwd):/project terravision draw --source https://github.com/your-repo/terraform-examples.git//mysubfolder/secondfolder/
```

Depending on your cloud provider, you may need to pass your credentials so that OpenTofu/Terraform can run terraform plan commands

For example, for AWS:

```sh
# Example 1 Mount AWS Credentials folder
docker run -it --rm  -v $(pwd):/project  -v ~/.aws:/home/terravision/.aws:ro  patrickchugh/terravision draw --source /path/to/terraform_source
# Example 2 Pass credentials as environment variables
docker run -it --rm  -v $(pwd):/project  -e AWS_ACCESS_KEY_ID=your-access-key -e AWS_SECRET_ACCESS_KEY=your-secret-key  patrickchugh/terravision draw --source /path/to/terraform_source
```

### Option 2 - Local Install

Before installing TerraVision, ensure you have:

- **Python 3.10+** - [Download Python](https://www.python.org/downloads/)
- **Terraform 1.x** - [Install Terraform](https://developer.hashicorp.com/terraform/downloads)
- **Graphviz** - [Install Graphviz](https://graphviz.org/download/)
- **Git** - [Install Git](https://git-scm.com/downloads)
- **Ollama** (Optional - for local AI refinement) - [Install Ollama](https://ollama.ai/download)

### Install TerraVision

```bash
pip install terravision # only if in a virtual env, if not you can use pipx install terravision instead
```

### Verify Terraform Setup

Before generating diagrams, ensure Terraform is working with `terraform init` and `terraform plan` 

TerraVision needs Terraform to successfully run `terraform plan` to parse your infrastructure. Note that whilst cloud credentials are required for TERRAFORM to validate resources and resolve functions, TerraVision itself never accesses your cloud account. Alternatively, use `--planfile` and `--graphfile` to provide pre-generated Terraform plan and graph outputs, bypassing Terraform execution entirely.

### Option 3 - Nix

If you have [Nix](https://nixos.org/download/) installed with flakes enabled, you can enter a development shell with `terravision` and all dependencies available:

```bash
git clone https://github.com/patrickchugh/terravision.git && cd terravision
nix develop
```

This provides `terravision`, `graphviz`, `terraform`, and `git` in your shell. You can also run it directly without cloning:

```bash
nix run github:patrickchugh/terravision -- draw --source /path/to/terraform --show
```

### Try It Out!

Generate your first diagram using our example Terraform code:

```bash

git clone https://github.com/patrickchugh/terravision.git
cd terravision

# Example 1: EKS cluster with fully managed nodes (auto)
terravision draw --source tests/fixtures/aws_terraform/eks_automode --show

# Example 2: Azure VM stack set
terravision draw --source tests/fixtures/azure_terraform/test_vm_vmss --show

# Example 3: From a public Git repository and only look at subfolder /aws/wordpress_fargate (note double slash)
terravision draw --source https://github.com/patrickchugh/terraform-examples.git//aws/wordpress_fargate --show
```

**That's it!** Your diagram is saved as `architecture.png` and automatically opened.

### Use Your Own Terraform Code

```bash
# Generate diagram from your Terraform directory
terravision draw --source /path/to/your/terraform/code
```

### Use Pre-Generated Terraform Plan (No Cloud Credentials Needed)

If you already have Terraform plan output (e.g. from a CI pipeline), you can generate diagrams without running Terraform:

```bash
# Step 1: Generate plan and graph files (in your Terraform environment)
terraform plan -out=tfplan.bin
terraform show -json tfplan.bin > plan.json
terraform graph > graph.dot

# Step 2: Generate diagram (no Terraform or cloud credentials needed)
terravision draw --planfile plan.json --graphfile graph.dot --source ./terraform
```

This is especially useful in CI/CD pipelines where Terraform runs in one step and diagram generation happens in another. See [CI/CD Integration](docs/CICD_INTEGRATION.md) for examples.

### Use TerraVision simply as a drawing engine with a simple JSON dict
```bash
# Generate a JSON graph file as output (default file is architecture.json)
terravision graphdata --source tests/fixtures/aws_terraform/ecs-ec2
# Draw a diagram from a simple pre-existing JSON graph file
terravision draw --source tests/json/bastion-expected.json
```


---

## Installation for Developers / Power Users

**Detailed installation instructions**: See [docs/INSTALLATION.md](docs/INSTALLATION.md)

---

## Basic Usage

### Generate a Diagram

```bash
# From local Terraform directory
terravision draw --source ./terraform

# From Git repository
terravision draw --source https://github.com/user/repo.git

# With custom output format
terravision draw --source ./terraform --format svg --outfile my-architecture

# Open diagram automatically
terravision draw --source ./terraform --show
```

### Common Options

| Option        | Description                   | Example                    |
| ------------- | ----------------------------- | -------------------------- |
| `--source`    | Terraform code location       | `./terraform` or Git URL   |
| `--format`    | Output format (see [Supported Formats](#supported-output-formats)) | `png`, `svg`, `pdf`, `jpg`, etc. |
| `--outfile`   | Output filename               | `architecture` (default)   |
| `--workspace` | Terraform workspace           | `production`, `staging`    |
| `--varfile`   | Variable file                 | `prod.tfvars`              |
| `--planfile`  | Pre-generated plan JSON file  | `plan.json`                |
| `--graphfile` | Pre-generated graph DOT file  | `graph.dot`                |
| `--simplified` | Simplified high-level view   | (flag)                     |
| `--show`      | Open diagram after generation | (flag)                     |
| `--debug`     | Enable debug output           | (flag)                     |

### Supported Output Formats

TerraVision supports all output formats provided by Graphviz, plus native draw.io export. Use the `--format` option to specify your desired format:

| Format | Description |
|--------|-------------|
| `png` | Portable Network Graphics (default) |
| `svg` | Scalable Vector Graphics - ideal for web |
| `pdf` | Portable Document Format - ideal for printing |
| `drawio` | **Editable diagram format** - open in draw.io, Lucidchart, or other diagram editors |
| `jpg` / `jpeg` | JPEG image format |
| `gif` | Graphics Interchange Format |
| `bmp` | Windows Bitmap |
| `eps` | Encapsulated PostScript |
| `ps` / `ps2` | PostScript |
| `tif` / `tiff` | Tagged Image File Format |
| `webp` | WebP image format |
| `dot` | Graphviz DOT source |
| `json` | Graphviz JSON format with layout info (different from `graphdata` output) |
| `xdot` | Extended DOT format with layout information |

For the complete list of Graphviz formats, see the [Graphviz Output Formats documentation](https://graphviz.org/docs/outputs/).

#### Editable Diagrams with draw.io Format

Generate diagrams you can edit in your favorite diagram editor:

```bash
terravision draw --source ./terraform --format drawio --outfile my-architecture
```

This creates a `.drawio` file that can be:
- Opened directly in [draw.io](https://app.diagrams.net/) (desktop or web)
- Imported into [Lucidchart](https://www.lucidchart.com/) (File → Import → select .drawio file)
- Edited in any diagram tool that supports the draw.io/mxGraph format

Perfect for adding annotations, adjusting layouts, or incorporating TerraVision output into existing documentation.

**Note**: `--format json` produces Graphviz's JSON format (includes layout coordinates). For TerraVision's simple graph dictionary format, use the `graphdata` command instead.

### Export Graph Data

```bash
# Export resource relationships as JSON
terravision graphdata --source ./terraform --outfile resources.json
```

**More examples**: See [docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)

### Simplified Diagrams

Use the `--simplified` flag to generate a high-level overview that strips away networking infrastructure (VPCs, subnets, availability zones, security groups, route tables, etc.) and focuses on the core cloud services. Duplicate resource instances are collapsed into a single node, and connections are bridged through removed nodes to preserve the overall data flow.

```bash
# Detailed diagram (default) - shows full networking topology
terravision draw --source ./terraform

# Simplified diagram - high-level services only
terravision draw --source ./terraform --simplified
```

**Detailed view** (default) — includes VPCs, subnets, availability zones, IAM roles, and networking plumbing:

<a href="./images/architecture-detailed.dot.png"><img src="./images/architecture-detailed.dot.png" height="300"></a>

**Simplified view** (`--simplified`) — same infrastructure, focused on core services:

<a href="./images/architecture-simplified.dot.png"><img src="./images/architecture-simplified.dot.png" height="300"></a>

The `--simplified` flag works with both `draw` and `graphdata` commands and is supported across all cloud providers (AWS, GCP, Azure). It is useful for executive presentations, high-level documentation, or when the full networking detail makes diagrams hard to read.

---

## Documentation

### For Users

- **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup instructions
- **[Usage Guide](docs/USAGE_GUIDE.md)** - Commands, options, and examples
- **[Annotations Guide](docs/ANNOTATIONS.md)** - Customize your diagrams
- **[CI/CD Integration](docs/CICD_INTEGRATION.md)** - Automate diagram generation
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues
... [TRUNCATED]
```

### File: requirements.txt
```txt
click>=8.1.3
GitPython>=3.1.31
graphviz>=0.20.1
PyYAML>=6.0
requests>=2.32.3
tqdm>=4.65.0
python-hcl2==4.3.0
ipaddr>=2.2.0
debugpy>=1.8.0
ollama>=0.6.1
tomli>=2.0.1
typing-extensions>=4.0.0
graphviz2drawio>=1.1.0

```

### File: docs\README.md
```md


# TerraVision

TerraVision is an AI-powered CLI tool that converts Terraform code into Professional Cloud Architecture Diagrams and solves the problem of keeping the most important document in cloud projects, the architecture diagram, up to date. With high velocity releases the norm now, code is the new source of truth so machine generated architecture diagrams are more accurate than relying on the freestyle diagram drawn by the cloud architect that probably doesn't match the reality of what is actually deployed in the cloud anymore. 

TerraVision securely runs 100% Client Side without any dependency or access to your Cloud environment, dynamically parses your conditionally created resources and variables and generates an automatic visual of your architecture. TerraVision is designed to be a 'Docs as Code' (DaC) tool that can be included in your CI/CD pipeline to update architecture diagrams after your build/test/release pipeline phases and supplement other document generators like readthedocs.io alongside it. 
<<<<<<< HEAD

## Status
=======


## Status


[![lint-and-test](https://github.com/patrickchugh/terravision/actions/workflows/lint-and-test.yml/badge.svg)](https://github.com/patrickchugh/terravision/actions/workflows/lint-and-test.yml)
>>>>>>> 003-azure-handler-implementation

[![lint-and-test](https://github.com/patrickchugh/terravision/actions/workflows/lint-and-test.yml/badge.svg)](https://github.com/patrickchugh/terravision/actions/workflows/lint-and-test.yml)

## Supported Cloud Providers

- ✅ **AWS** (Full support with 200+ services)
- 🔄 **Google Cloud Platform** (Partial Support)
- 🔄 **Microsoft Azure** (Partial Support)

Turn this... 

![Terraform Code](./images/code.png "Turn Terraform code")

into this...

<img src="./images/architecture.png" width="640" height="580">

> **⚠️ Alpha Software Notice**  
> This software is still in alpha testing and **code is shared on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND**, either express or implied. Use at your own risk.

# Benefits of terravision

1. Cost
   - Save Visio/Drawing software licenses - terravision is free and open source
   - Doesn't require any cost incurring cloud resources to be spun up, it works instantly from your local machine
   - Regularly updating diagrams aligning, connecting dots and laying out icons is not the best use of your architect staff costs
2. Accelerate and Automate
<<<<<<< HEAD
   - Use TF variable files as inputs to create multiple variant diagrams from the same TF code
     - Doesn't require infrastructure to exist to document it. Terravision works off your terraform plan not your remote statefile
   - Automate creation of architecture diagrams by running terravision as part of CI/CD pipelines
   - YAML based Diagrams as code allows you to Annotate generated diagrams with additional custom labels and resources  e.g. unmanaged resources or external systems not captured in TF code
=======
	- Use TF variable files as inputs to create multiple variant diagrams from the same TF code
   - Doesn't require infrastructure to exist to document it. Terravision works off your terraform plan not your remote statefile
	- Automate creation of architecture diagrams by running terravision as part of CI/CD pipelines
	- YAML based Diagrams as code allows you to Annotate generated diagrams with additional custom labels and resources  e.g. unmanaged resources or external systems not captured in TF code
>>>>>>> 003-azure-handler-implementation
3. Consistency across organisation
   - Auto downloads your organisational / external modules to ensure the latest view of downstream Terraform modules
   - Consistent design of architecture diagrams using industry standard icons and AWS/GCP/Azure approved style across teams 
4. Accurate Visibility 
   - Real time state of diagram shows current infrastructure that matches exactly what is deployed in production today
   - Helps in third party architecture reviews, auditing, monitoring, reporting and debugging of the stack in a visual way
   - Custom Diagram code and output images can be put into source/version control for better maintainability and discoverability
5. Security
<<<<<<< HEAD
   - Don't need to give access to your AWS account, credentials or CLI to draw diagram
   - Doesn't create intrusive cloud resources  e.g. scanning instances or metadata tables which enterprises would need to approve
     - All source code stays in your local environment, diagrams are generated on your machines without calling out to external APIs
     - Only metatdata is sent to LLM models with only minimal aggregate data saved in external files, not any sensitive code or runtime environment values
=======
	- Don't need to give access to your AWS account, credentials or CLI to draw diagram
	- Doesn't create intrusive cloud resources  e.g. scanning instances or metadata tables which enterprises would need to approve
  	- All source code stays in your local environment, diagrams are generated on your machines without calling out to external APIs
   - Only metatdata is sent to LLM models with only minimal aggregate data saved in external files, not any sensitive code or runtime environment values
>>>>>>> 003-azure-handler-implementation

# CI/CD Pipeline Integration

TerraVision seamlessly integrates into your CI/CD pipeline to automatically keep architecture diagrams synchronized with your infrastructure code:

```mermaid
graph TD
    A[Developer Commits<br/>Terraform Code] --> B[Git Push]
    B --> C[CI/CD Pipeline<br/>Triggered]
    C --> D[Build Stage]
    D --> E[Test Stage]
    E --> F[Terraform Plan]
    F --> G[🎨 TerraVision<br/>Generate Diagrams]
    G --> H[Deploy Stage]
    H --> I[Update Docs]
    I --> J[Publish to<br/>Confluence/ReadTheDocs]
<<<<<<< HEAD

    style G fill:#ff9900,stroke:#232f3e,stroke-width:3px,color:#fff
    style A fill:#4a90e2,stroke:#2e5c8a,stroke-width:2px,color:#fff
    style J fill:#36b37e,stroke:#1f7a54,stroke-width:2px,color:#fff
```
=======
    
    style G fill:#ff9900,stroke:#232f3e,stroke-width:3px,color:#fff
    style A fill:#4a90e2,stroke:#2e5c8a,stroke-width:2px,color:#fff
    style J fill:#36b37e,stroke:#1f7a54,stroke-width:2px,color:#fff
``` 
>>>>>>> 003-azure-handler-implementation

# Installation and Usage

## System Requirements
<<<<<<< HEAD

=======
>>>>>>> 003-azure-handler-implementation
- **Python 3.10+** 
- **Terraform 1.x**   
- **Git**  
- **Graphviz**
- **Ollama** (Optional - only required if using `--aibackend ollama`)

## 1. Install External Dependencies

### Required Dependencies

1. **Graphviz** - https://graphviz.org/download/
   
   ```bash
   # macOS
   brew install graphviz
   
   # Ubuntu/Debian
   sudo apt-get install graphviz
   
   # Windows
   # Download from https://graphviz.org/download/
   ```

2. **Git** - https://git-scm.com/downloads
   
   ```bash
   # Most systems have git pre-installed
   git --version
   ```

3. **Terraform** - https://developer.hashicorp.com/terraform/downloads
   
   ```bash
   # Verify installation
   terraform version
   # Must be v1.0.0 or higher
   ```

## 2. Install TerraVision

### Method 1: Quick Install in MacOS/Linux (For Casual Users - will install packages globally)

```bash
# Clone the repository
git clone https://github.com/patrickchugh/terravision.git
cd terravision

# Install Python dependencies
pip install -r requirements.txt

# Make script executable in Linux
chmod +x terravision.py

# Create symbolic link without extension (Unix/Linux/macOS)
ln -s $(pwd)/terravision.py $(pwd)/terravision

# Add to PATH
export PATH=$PATH:$(pwd)
```

**For Windows:**

```powershell
# Clone the repository
git clone https://github.com/patrickchugh/terravision.git
cd terravision

# Install Python dependencies
pip install -r requirements.txt

# Create batch file wrapper
echo @python "%~dp0terravision.py" %* > terravision.bat

# Add current directory to PATH or copy terravision.bat to a directory in PATH
copy terravision.bat C:\Windows\System32\
```

### Method 2: Poetry Install (Recommended for Developers and Power Users)

```bash
# MacOS or Linux users - Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# For Windows Users
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Clone and install with Poetry
git clone https://github.com/patrickchugh/terravision.git
cd terravision
poetry install

# Activate virtual environment
source $(poetry env info --path)/bin/activate

# Create symbolic link without extension
ln -s $(pwd)/terravision.py $(pwd)/terravision

# Add current terravision directory to PATH
export PATH=$PATH:$(pwd)
```

## Basic Usage

### Generate Architecture Diagram

```bash
# Basic usage - analyze current directory
terravision draw

# Specify source directory
terravision draw --source ~/src/my-terraform-code

# Use specific Terraform workspace
terravision draw --source ~/src/my-terraform-code --workspace production

# Use variable files
terravision draw --source ~/src/my-terraform-code --varfile prod.tfvars

# Generate different formats
terravision draw --source ~/src/my-terraform-code --format svg
terravision draw --source ~/src/my-terraform-code --format pdf

# Show diagram after generation
terravision draw --source ~/src/my-terraform-code --show

# Use AI backend for diagram refinement (default: bedrock)
terravision draw --source ~/src/my-terraform-code --aibackend bedrock
terravision draw --source ~/src/my-terraform-code --aibackend ollama
```

### Remote Git Repository Support

```bash
# Analyze Git repository
terravision draw --source https://github.com/your-repo/terraform-examples.git

# Analyze specific subfolder in Git repo
terravision draw --source https://github.com/your-repo/terraform-examples.git//aws/vpc
```

### Export Graph Data

```bash
# Export resource relationships as JSON
terravision graphdata --source ~/src/my-terraform-code

# Show only unique services used
terravision graphdata --source ~/src/my-terraform-code --show_services

# Export to custom filename
terravision graphdata --source ~/src/my-terraform-code --outfile my-resources.json
```

## Advanced Features

<<<<<<< HEAD
### Use with annotations

```bash
# Add your own custom annotations such as labels, resources or new connections
terravision draw --source https://github.com/your-repo/terraform-examples.git --annotate ./custom-annotations.yml
```

### Working with Pre-generated JSON from previous terravision run (faster)

```bash
=======

### Use with annotations
```bash
# Add your own custom annotations such as labels, resources or new connections
terravision draw --source https://github.com/your-repo/terraform-examples.git --annotate ./custom-annotations.yml
```

### Working with Pre-generated JSON from previous terravision run (faster)
```bash
>>>>>>> 003-azure-handler-implementation
# Export and reuse graph data
terravision graphdata --source ~/src/terraform --outfile graph.json

# Use previously exported JSON data (just the graph dict)
terravision draw --source ./graph.json
terravision draw --source ./graph.json --format svg

# Reprocess and replay from previous debug (for troubleshooting without calling slow terraform init/plan/analayse again)
terravision draw --source /your_source_files --debug  # createas a tfdata.json in current folder
terravision draw --source tfdata.json
```

### Debug Mode

```bash
# Enable debug output for troubleshooting and which will dump all state info into tfdata.json
terravision draw --source ~/src/my-terraform-code --debug
```

## AI-Powered Diagram Refinement

TerraVision can use AI models to automatically refine and improve your architecture diagrams by fixing resource groupings, adding missing connections, and ensuring proper AWS architectural conventions.

### Supported AI Backends

#### AWS Bedrock (Default)
<<<<<<< HEAD

=======
>>>>>>> 003-azure-handler-implementation
Uses AWS Bedrock API via API Gateway for cloud-based AI refinement.

```bash
# Use Bedrock backend (default)
terravision draw --source ~/src/my-terraform-code --aibackend bedrock
<<<<<<< HEAD
```

**Configuration:**
Edit `modules/cloud_config.py` to set your Bedrock API endpoint:

```python
BEDROCK_API_ENDPOINT = "https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/chat"
```

#### Ollama (Local)

Uses a local Ollama server for privacy-focused, offline AI refinement.

```bash
# Use Ollama backend
terravision draw --source ~/src/my-terraform-code --aibackend ollama
```

**Setup:**

1. Install Ollama from https://ollama.ai/download

2. Start Ollama server and pull a model:
   
   ```bash
   # Start Ollama (runs automatically on macOS/Linux after install)
   ollama serve
   
   # Pull the llama3 model
   ollama pull llama3
   
   # Set model to stay loaded longer (optional, prevents premature unloading)
   # Default timeout is 5 minutes, extend to 1 hour:
   export OLLAMA_KEEP_ALIVE=1h
   ```

3. Edit `modules/cloud_config.py` to set your Ollama server (default is localhost):
   
   ```python
   OLLAMA_HOST = "http://localhost:11434"
   ```

### AI Refinement Prompts

The AI models use specialized prompts defined in `modules/cloud_config.py`:

- **AWS_REFINEMENT_PROMPT**: Guides the AI to fix resource groupings, connections, and ensure AWS best practices
- **AWS_DOCUMENTATION_PROMPT**: Generates architecture summaries and documentation

### Setting Up AWS Bedrock Backend

TerraVision includes Terraform code to deploy a serverless AWS Bedrock proxy with API Gateway:

```bash
# Navigate to the Terraform directory
cd ai-backend-terraform

# Configure your settings
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your settings

# Deploy the infrastructure
terraform init
terraform apply

# Get your API endpoint
terraform output api_endpoint
```

**Infrastructure Components:**

- **API Gateway**: REST API with streaming support for real-time responses
- **Lambda Function**: Node.js 20.x function with response streaming
- **DynamoDB**: Rate limiting and usage tracking
- **CloudWatch**: Monitoring, logging, and cost alerts
- **IAM Roles**: Least-privilege access for Lambda to invoke Bedrock

**Terraform Variables:**

```hcl
variable "bedrock_model_id" {
  description = "Bedrock model ID"
  type        = string
}

variable "rate_limit_per_hour" {
  description = "Maximum requests per client per hour"
  type        = number
  default     = 100
}

variable "cost_alert_threshold" {
  description = "Cost alert threshold in USD"
  type        = number
  default     = 50
}
```

After deployment, update `modules/cloud_config.py` with the output endpoint:

```python
BEDROCK_API_ENDPOINT = "<your-api-endpoint-from-terraform-output>"
=======
>>>>>>> 003-azure-handler-implementation
```

**Configuration:**
Edit `modules/cloud_config.py` to set your Bedrock API endpoint:
```python
BEDROCK_API_ENDPOINT = "https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/chat"
```

#### Ollama (Local)
Uses a local O
... [TRUNCATED]
```

### File: .pre_commit_config.yaml
```yaml
repos:
  - repo: local
    hooks:
      - id: black
        name: Run black
        entry: poetry run black --check
        language: system
        pass_filenames: true
        types: [python]
      - id: pytest
        name: Run pytest
        entry: poetry run pytest -m "not slow"
        language: system
        pass_filenames: false
        types: [python]

```

### File: clearcache.sh
```sh
#!/usr/bin/env sh
rm -rf ~/.terravision
```

### File: .devcontainer\devcontainer.json
```json
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/python
{
	"name": "Python 3",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/python:3.0-3.14-trixie",
	"features": {
		"ghcr.io/devcontainers/features/terraform:1": {}
	}

	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "pip3 install --user -r requirements.txt",

	// Configure tool-specific properties.
	// "customizations": {},

	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}

```

### File: .github\pull_request_template.md
```md
# YOUR PR TITLE

## Type of Change

* [ ] Bug Fix
* [ ] New Feature
* [ ] Refactor
* [ ] Documentation

## Checklist

All Submissions:
* [ ] Have you checked to ensure there aren't other open [Pull Requests](../../../pulls) for the same update/change?
* [ ] Have you written Documentation/Tests?
* [ ] Have you done your own code-review?
* [ ] Have you disclosed any use of AI tools and models with their version?

## AI Assistance Declaration
- Tools used: [e.g., Claude Code, GitHub Copilot]
- Model: [e.g., Claude Sonnet 4.5, GPT-4]
- Scope: [e.g., "Generated test cases", "Refactored function X"]

### Checklist for Changes to Core Features:

* [ ] Have you discussed any major revamp with a reviewer/maintainer first? (It's okay to just raise a PR directly for minor bugfixes)
* [ ] Have you ensured your PR is focused on one major improvement and is not trying to do too many changes at once? For example:
      Bad : Adding support for GCP and Azure system wide
      Good: Just adding Azure resource handler for VNets
* [ ] Have you added an explanation of what your changes do and why you'd like us to include them?
* [ ] Have you written new tests for your core changes, as applicable, and made sure the new tests PASS?
* [ ] Have you successfully run all previous system wide tests with your changes locally?

```

### File: docs\ANNOTATIONS.md
```md
# Annotations Guide

## Overview

Annotations allow you to customize automatically generated diagrams by:
- Adding custom titles and labels
- Creating new connections
- Removing unwanted connections
- Adding external resources not in Terraform
- Modifying existing resources

---

## Quick Start

Create a `terravision.yml` file in your Terraform directory:

```yaml
format: 0.1
title: My Production Architecture

connect:
  aws_lambda_function.api:
    - aws_rds_cluster.database: Database queries

disconnect:
  aws_cloudwatch_log_group.logs:
    - aws_lambda_function.api
```

Run TerraVision:
```bash
terravision draw --source ./terraform
# Annotations are automatically loaded from terravision.yml
```

---

## Annotation File Format

### Basic Structure

```yaml
format: 0.1  # Required: annotation format version

title: "Diagram Title"  # Optional: main diagram heading

connect:
  # Add new connections

disconnect:
  # Remove connections

add:
  # Add new resources

remove:
  # Delete resources

update:
  # Modify existing resources
```

### File Location

**Option 1: Auto-load** (recommended)
- Name the file `terravision.yml`
- Place it in your Terraform source directory
- TerraVision will automatically load it

**Option 2: Specify path**
```bash
terravision draw --source ./terraform --annotate /path/to/annotations.yml
```

---

## Annotation Operations

### 1. Add Title

```yaml
title: "Production Environment - US East"
```

### 2. Connect Resources

Add new connections between resources.

**Basic connection:**
```yaml
connect:
  aws_lambda_function.api:
    - aws_rds_cluster.database
```

**Connection with label:**
```yaml
connect:
  aws_lambda_function.api:
    - aws_rds_cluster.database: "SQL queries"
    - aws_s3_bucket.uploads: "Store files"
```

**Multiple sources:**
```yaml
connect:
  aws_lambda_function.api:
    - aws_rds_cluster.database: "Read/Write"
  aws_ecs_service.web:
    - aws_rds_cluster.database: "Read only"
```

### 3. Disconnect Resources

Remove existing connections.

**Basic disconnect:**
```yaml
disconnect:
  aws_cloudwatch_log_group.logs:
    - aws_lambda_function.api
    - aws_ecs_service.web
```

**Using wildcards:**
```yaml
disconnect:
  aws_cloudwatch*.logs:  # Matches any CloudWatch log group
    - aws_ecs_service.this
    - aws_ecs_cluster.this
```

### 4. Add Resources

Add resources that don't exist in Terraform (external systems, on-prem resources).

**Basic add:**
```yaml
add:
  aws_subnet.external_subnet:
    cidr_block: "10.0.5.0/24"
    availability_zone: "us-east-1a"
```

**Add with connections:**
```yaml
add:
  external_api.payment_gateway:
    endpoint: "https://api.payment.com"
    
connect:
  aws_lambda_function.checkout:
    - external_api.payment_gateway: "Process payments"
```

### 5. Remove Resources

Delete resources from the diagram.

**Basic remove:**
```yaml
remove:
  - aws_iam_role.task_execution_role
  - aws_cloudwatch_log_group.debug_logs
```

**Using wildcards:**
```yaml
remove:
  - aws_iam_role.*  # Remove all IAM roles
```

### 6. Update Resources

Modify attributes of existing resources.

**Add edge labels:**
```yaml
update:
  aws_ecs_service.web:
    edge_labels:
      - aws_rds_cluster.database: "Database queries"
      - aws_elasticache_cluster.cache: "Session storage"
```

**Custom resource label:**
```yaml
update:
  aws_lambda_function.api:
    label: "API Gateway Handler"
```

**Update with wildcards:**
```yaml
update:
  aws_cloudfront*:
    edge_labels:
      - aws_acm_certificate.this: "SSL Certificate"
```

---

## Complete Example

```yaml
format: 0.1

# Main diagram title
title: "E-Commerce Platform - Production"

# Add connections not apparent from Terraform
connect:
  aws_lambda_function.order_processor:
    - aws_rds_cluster.orders_db: "Insert orders"
    - aws_sqs_queue.notifications: "Send notifications"
  
  aws_ecs_service.web:
    - aws_elasticache_cluster.sessions: "Session cache"

# Remove noisy connections
disconnect:
  aws_cloudwatch_log_group.*:
    - aws_lambda_function.*
    - aws_ecs_service.*

# Add external systems
add:
  external_api.payment_gateway:
    provider: "Stripe"
    endpoint: "https://api.stripe.com"
  
  external_api.shipping_service:
    provider: "FedEx"
    endpoint: "https://api.fedex.com"

# Remove internal resources from diagram
remove:
  - aws_iam_role.lambda_execution
  - aws_iam_policy.cloudwatch_logs

# Add custom labels
update:
  aws_lambda_function.order_processor:
    label: "Order Processing Engine"
    edge_labels:
      - external_api.payment_gateway: "Process payment"
      - external_api.shipping_service: "Create shipment"
  
  aws_ecs_service.web:
    label: "Web Application (3 tasks)"
    edge_labels:
      - aws_alb.main: "HTTP/HTTPS traffic"
  
  aws_cloudfront_distribution.cdn:
    edge_labels:
      - aws_s3_bucket.static_assets: "Static content"
      - aws_alb.main: "Dynamic content"
```

---

## Wildcard Patterns

Use wildcards to match multiple resources:

| Pattern | Matches | Example |
|---------|---------|---------|
| `aws_lambda*` | All Lambda functions | `aws_lambda_function.api`, `aws_lambda_function.worker` |
| `*.logs` | All resources ending with .logs | `aws_cloudwatch_log_group.api_logs` |
| `aws_ecs_*` | All ECS resources | `aws_ecs_service.web`, `aws_ecs_cluster.main` |

**Examples:**

```yaml
# Disconnect all CloudWatch logs from all Lambda functions
disconnect:
  aws_cloudwatch*.logs:
    - aws_lambda*

# Add edge labels to all CloudFront distributions
update:
  aws_cloudfront*:
    edge_labels:
      - aws_acm_certificate.this: "SSL Cert"

# Remove all IAM roles
remove:
  - aws_iam_role.*
```

---

## Resource Naming Convention

Resource names follow Terraform conventions:

```
<resource_type>.<resource_name>
```

**Examples:**
- `aws_lambda_function.api`
- `aws_rds_cluster.database`
- `aws_s3_bucket.uploads`

**Find resource names:**
```bash
# Export graph data to see all resource names
terravision graphdata --source ./terraform --outfile resources.json

# View the JSON file
cat resources.json | jq 'keys'
```

---

## Best Practices

### 1. Start Simple
Begin with just a title and a few connections:
```yaml
format: 0.1
title: "My Architecture"

connect:
  aws_lambda_function.api:
    - aws_rds_cluster.db: "Queries"
```

### 2. Use Wildcards Sparingly
Wildcards are powerful but can have unintended effects. Test incrementally.

### 3. Add Labels for Clarity
Always add labels to custom connections:
```yaml
connect:
  aws_lambda_function.api:
    - aws_rds_cluster.db: "Read/Write queries"  # Good
    # - aws_rds_cluster.db  # Less clear
```

### 4. Document External Systems
When adding external resources, include descriptive attributes:
```yaml
add:
  external_api.payment:
    provider: "Stripe"
    endpoint: "https://api.stripe.com"
    purpose: "Payment processing"
```

### 5. Version Control Annotations
Keep annotation files in Git alongside Terraform code:
```
terraform/
├── main.tf
├── variables.tf
└── terravision.yml  # Annotations
```

### 6. Test Incrementally
Add annotations gradually and regenerate diagrams to verify:
```bash
# After each change
terravision draw --source ./terraform --show
```

---

## Common Use Cases

### Add On-Premises Connectivity

```yaml
add:
  on_prem.datacenter:
    location: "Corporate HQ"
    network: "10.0.0.0/8"

connect:
  aws_vpn_gateway.main:
    - on_prem.datacenter: "Site-to-Site VPN"
```

### Show Third-Party Services

```yaml
add:
  external_api.auth0:
    service: "Auth0"
    purpose: "Authentication"

connect:
  aws_lambda_function.auth:
    - external_api.auth0: "Verify tokens"
```

### Simplify Complex Diagrams

```yaml
# Remove noisy IAM and logging resources
remove:
  - aws_iam_role.*
  - aws_iam_policy.*
  - aws_cloudwatch_log_group.*

# Remove internal connections
disconnect:
  aws_security_group.*:
    - aws_subnet.*
```

### Add Business Context

```yaml
title: "Customer Portal - Production (us-east-1)"

update:
  aws_ecs_service.web:
    label: "Customer Portal (10 tasks)"
  
  aws_rds_cluster.main:
    label: "Customer Database (Multi-AZ)"
  
  aws_elasticache_cluster.sessions:
    label: "Session Store (Redis 6.x)"
```

---

## Troubleshooting

### Annotations Not Applied

1. **Check file name**: Must be `terravision.yml` or specified with `--annotate`
2. **Check YAML syntax**: Use a YAML validator
3. **Check resource names**: Use `terravision graphdata` to see exact names
4. **Enable debug mode**: `terravision draw --debug` to see processing details

### Wildcards Not Matching

```bash
# List all resources to verify patterns
terravision graphdata --source ./terraform --show_services
```

### Connections Not Showing

1. **Verify resource names exist** in the Terraform code
2. **Check for typos** in resource names
3. **Use debug mode** to see connection processing

---

## Next Steps

- **[Usage Guide](USAGE_GUIDE.md)** - Learn more TerraVision commands
- **[CI/CD Integration](CICD_INTEGRATION.md)** - Automate with annotations
- **[Examples Repository](https://github.com/patrickchugh/terravision-examples)** - See more annotation examples

```

### File: docs\CICD_INTEGRATION.md
```md
# CI/CD Integration Guide

Integrate TerraVision into your CI/CD pipeline to automatically generate and update architecture diagrams whenever infrastructure code changes.

---

## Installation Methods

TerraVision can be integrated into any CI/CD system using one of these methods:

| Method | Best For | Prerequisites |
|--------|----------|---------------|
| **GitHub Action** | GitHub workflows | Terraform on PATH |
| **Docker image** | GitLab, Jenkins, any container-based CI | None (self-contained) |
| **pip install** | Any CI with Python available | Python 3.10+, Graphviz, Terraform |
| **pip install + `--planfile`** | Diagram step without Terraform | Python 3.10+, Graphviz (no Terraform needed) |

---

## GitHub Actions

### Using the TerraVision Action (Recommended)

The [TerraVision Action](https://github.com/patrickchugh/terravision-action) handles installation of TerraVision and Graphviz automatically. You only need to provide Terraform.

```yaml
name: Update Architecture Diagrams

on:
  push:
    branches: [main]
    paths: ['**.tf', '**.tfvars']

jobs:
  generate-diagrams:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - uses: patrickchugh/terravision-action@v2
        with:
          source: ./infrastructure
          outfile: docs/architecture
          format: both
```

#### Action Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `source` | Path to Terraform source directory | Yes | `.` |
| `outfile` | Output file path (without extension) | No | `architecture` |
| `format` | Output format: `png`, `svg`, or `both` | No | `png` |
| `varfile` | Path to `.tfvars` file | No | |
| `annotate` | Path to `terravision.yml` annotation file | No | |
| `planfile` | Pre-generated plan JSON from `terraform show -json` (skips Terraform requirement) | No | |
| `graphfile` | Pre-generated graph DOT from `terraform graph` (required with `planfile`) | No | |
| `extra-args` | Additional arguments for `terravision draw` | No | |

#### With Cloud Credentials

If Terraform needs to download remote modules or run `init` with backend access:

```yaml
steps:
  - uses: actions/checkout@v4

  - uses: hashicorp/setup-terraform@v3

  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/diagram-role
      aws-region: us-east-1

  - uses: patrickchugh/terravision-action@v2
    with:
      source: ./infrastructure
      format: svg
```

#### With Pre-Generated Plan (No Terraform in Diagram Step)

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: hashicorp/setup-terraform@v3

  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/terraform-role
      aws-region: us-east-1

  - name: Terraform Plan
    run: |
      cd infrastructure
      terraform init
      terraform plan -out=tfplan.bin
      terraform show -json tfplan.bin > plan.json
      terraform graph > graph.dot

  - uses: patrickchugh/terravision-action@v2
    with:
      source: ./infrastructure
      planfile: infrastructure/plan.json
      graphfile: infrastructure/graph.dot
      format: svg
```

#### Multi-Environment Matrix

```yaml
jobs:
  diagrams:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [dev, staging, prod]
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3

      - uses: patrickchugh/terravision-action@v2
        with:
          source: ./terraform
          outfile: docs/architecture-${{ matrix.environment }}
          varfile: environments/${{ matrix.environment }}.tfvars
          format: svg
```

#### Commit Diagrams Back to Repository

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: hashicorp/setup-terraform@v3

  - uses: patrickchugh/terravision-action@v2
    with:
      source: ./infrastructure
      outfile: docs/architecture
      format: both

  - name: Commit Diagrams
    run: |
      git config user.name "github-actions[bot]"
      git config user.email "github-actions[bot]@users.noreply.github.com"
      git add docs/architecture.*
      git commit -m "Update architecture diagrams [skip ci]" || exit 0
      git push
```

#### Pull Request Diagram Preview

```yaml
name: PR Architecture Preview

on:
  pull_request:
    paths: ['**.tf']

jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3

      - uses: patrickchugh/terravision-action@v2
        with:
          source: ./infrastructure
          outfile: pr-architecture
          format: png

      - name: Upload Diagram
        uses: actions/upload-artifact@v4
        with:
          name: architecture-diagram
          path: pr-architecture.png

      - name: Comment on PR
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '## Architecture Diagram\nSee the uploaded artifact for the updated diagram.'
            })
```

#### Using Docker Image Directly (No Prerequisites)

Alternatively, use the Docker image for a fully self-contained step:

```yaml
- name: Generate Diagram
  uses: docker://patrickchugh/terravision:latest
  with:
    args: draw --source ./infrastructure --outfile architecture --format png
```

---

## GitLab CI

### Using the Docker Image (Recommended)

The `patrickchugh/terravision` Docker image includes Terraform, Graphviz, and TerraVision — no additional setup required.

```yaml
# .gitlab-ci.yml
stages:
  - diagram

generate-diagram:
  stage: diagram
  image: patrickchugh/terravision:latest
  script:
    - terravision draw --source ./infrastructure --outfile architecture --format png
    - terravision draw --source ./infrastructure --outfile architecture --format svg
  artifacts:
    paths:
      - architecture.png
      - architecture.svg
    expire_in: 30 days
  rules:
    - changes:
        - "**/*.tf"
        - "**/*.tfvars"
```

### Multi-Environment

```yaml
generate-diagram:
  stage: diagram
  image: patrickchugh/terravision:latest
  parallel:
    matrix:
      - ENVIRONMENT: [dev, staging, prod]
  script:
    - terravision draw
        --source ./terraform
        --varfile environments/${ENVIRONMENT}.tfvars
        --outfile architecture-${ENVIRONMENT}
        --format svg
  artifacts:
    paths:
      - architecture-*.svg
```

### With Cloud Credentials

```yaml
generate-diagram:
  stage: diagram
  image: patrickchugh/terravision:latest
  variables:
    AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY
    AWS_DEFAULT_REGION: us-east-1
  script:
    - terravision draw --source ./infrastructure --outfile architecture --format png
  artifacts:
    paths:
      - architecture.png
```

### Commit Diagrams Back

```yaml
generate-diagram:
  stage: diagram
  image: patrickchugh/terravision:latest
  script:
    - terravision draw --source ./infrastructure --outfile docs/architecture --format png
    - git config user.name "GitLab CI"
    - git config user.email "ci@gitlab.com"
    - git add docs/architecture.png
    - git commit -m "Update architecture diagram [skip ci]" || true
    - git push "https://oauth2:${CI_JOB_TOKEN}@${CI_SERVER_HOST}/${CI_PROJECT_PATH}.git" HEAD:${CI_COMMIT_BRANCH}
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      changes:
        - "**/*.tf"
```

### As a CI/CD Component

If you host on GitLab, you can create a reusable [CI/CD Component](https://docs.gitlab.com/ee/ci/components/):

```yaml
# In your component repo: templates/generate-diagram.yml
spec:
  inputs:
    source:
      default: '.'
    output:
      default: 'architecture'
    format:
      default: 'png'
    stage:
      default: 'build'

---

"generate-diagram":
  image: patrickchugh/terravision:latest
  stage: $[[ inputs.stage ]]
  script:
    - terravision draw --source $[[ inputs.source ]] --outfile $[[ inputs.output ]] --format $[[ inputs.format ]]
  artifacts:
    paths:
      - $[[ inputs.output ]].$[[ inputs.format ]]
```

Consumers include it as:

```yaml
include:
  - component: gitlab.com/your-org/terravision-component/generate-diagram@v1
    inputs:
      source: ./infrastructure
      format: svg
```

---

## Jenkins

### Docker Agent (Recommended)

```groovy
// Jenkinsfile
pipeline {
    agent {
        docker {
            image 'patrickchugh/terravision:latest'
        }
    }

    triggers {
        pollSCM('H/15 * * * *')
    }

    stages {
        stage('Generate Diagrams') {
            steps {
                sh '''
                    terravision draw \
                        --source ./infrastructure \
                        --outfile architecture \
                        --format png

                    terravision draw \
                        --source ./infrastructure \
                        --outfile architecture \
                        --format svg
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'architecture.*', fingerprint: true
            }
        }
    }
}
```

### Multi-Environment with Parameters

```groovy
pipeline {
    agent {
        docker {
            image 'patrickchugh/terravision:latest'
        }
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'prod'], description: 'Target environment')
    }

    stages {
        stage('Generate Diagram') {
            steps {
                sh """
                    terravision draw \
                        --source ./terraform \
                        --varfile environments/${params.ENVIRONMENT}.tfvars \
                        --outfile architecture-${params.ENVIRONMENT} \
                        --format png
                """
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: "architecture-${params.ENVIRONMENT}.png", fingerprint: true
            }
        }
    }
}
```

### Without Docker (pip install)

```groovy
pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                    pip install terravision
                '''
            }
        }

        stage('Generate Diagrams') {
            steps {
                sh '''
                    terravision draw \
                        --source ./infrastructure \
                        --outfile architecture \
                        --format png
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'architecture.*', fingerprint: true
            }
        }
    }
}
```

**Note**: The non-Docker approach requires Python 3.10+, Graphviz, and Terraform pre-installed on the Jenkins agent.

---

## Azure DevOps

### Using Docker

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
  paths:
    include:
      - '**/*.tf'
      - '**/*.tfvars'

pool:
  vmImage: 'ubuntu-latest'

container: patrickchugh/terravision:latest

steps:
- script: |
    terravision draw --source ./infrastructure --outfile $(Build.ArtifactStagingDirectory)/architecture --format png
    terravision draw --source ./infrastructure --outfile $(Build.ArtifactStagingDirectory)/architecture --format svg
  displayName: 'Generate Diagrams'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'architecture-diagrams'
  displayName: 'Publish Diagrams'
```

### Using pip install

```yaml
trigger:
  branches:
    include:
      - main
  paths:
    include:
      - '**/*.tf'

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.10'
  displayName: 'Use Python 3.10'

- task: TerraformInstaller@1
  inputs:
    terraformVersion: 'latest'
  displayName: 'Install Terraform'

- script: |
    sudo apt-get update -qq && sudo apt-get install -y -qq graphviz
    pip install terravision
  displayName: 'Install TerraVision'

- script: |
    terravision draw --source ./infrastructure --outfile $(Build.ArtifactStagingDirectory)/architecture --format png
  displayName: 'Generate Diagram'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'architecture-diagrams'
```

---

## Generic CI/CD (Any Platform)

For any CI/CD system, you have two options:

### Option 1: Docker (Recommended)

Run the Docker image with your source mounted:

```bash
docker run --rm \
  -v $(pwd):/project \
  patrickchugh/terravision:latest \
  draw --source ./infrastructure --outfile architecture --format png
```

This works in any CI system that supports Docker (CircleCI, Bitbucket Pipelines, Drone, etc.).

### Option 2: pip install

```bash
# Prerequisites: Python 3.10+, Graphviz, Terraform
pip install terravision
terravision draw --source ./infrastructure --outfile architecture --format png
```

### CircleCI Example

```yaml
# .circleci/config.yml
version: 2.1

jobs:
  generate-diagram:
    docker:
      - image: patrickchugh/terravision:latest
    steps:
      - checkout
      - run:
          name: Generate Diagram
          command: terravision draw --source ./infrastructure --outfile architecture --format png
      - store_artifacts:
          path: architecture.png

workflows:
  diagram:
    jobs:
      - generate-diagram:
          filters:
            branches:
              only: main
```

### Bitbucket Pipelines Example

```yaml
# bitbucket-pipelines.yml
image: patrickchugh/terravision:latest

pipelines:
  branches:
    main:
      - step:
          name: Generate Architecture Diagram
          script:
            - terravision draw --source ./infrastructure --outfile architecture --format png
          artifacts:
            - architecture.png
```

---

## Pre-Generated Plan Mode (No Credentials in Diagram Step)

In many CI/CD setups, Terraform runs in a secured step with cloud credentials, while diagram generation should happen separately without credential access. The `--planfile` and `--graphfile` options enable this separation.

### How It Works

1. **Terraform step** (with credentials): Run `terraform plan`, export plan JSON and graph DOT
2. **Diagram step** (no credentials): Run `terravision` with the exported files

### GitHub Actions — Separate Jobs

```yaml
name: Infrastructure Diagrams

on:
  push:
    branches: [main]
    paths: ['**.tf', '**.tfvars']

jobs:
  terraform-plan:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3

      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume:
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
