---
id: hashicorp-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:50.839454
---

# KNOWLEDGE EXTRACT: hashicorp
> **Extracted on:** 2026-03-30 17:38:04
> **Source:** hashicorp

---

## File: `agent-skills.md`
```markdown
# 📦 hashicorp/agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/hashicorp/agent-skills


## Meta
- **Stars:** ⭐ 486 | **Forks:** 🍴 60
- **Language:** Shell | **License:** MPL-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A collection of Agent skills and Claude Code plugins for HashiCorp products.

## README (trích đầu)
```
# HashiCorp Agent Skills

A collection of Agent skills and Claude Code plugins for HashiCorp products.

| Product | Use cases |
|:--------|:----------|
| [Terraform](./terraform/) | Write HCL code, build modules, develop providers, and run tests |
| [Packer](./packer/) | Build machine images on AWS, Azure, and Windows; integrate with HCP Packer registry |

> **Legal Note:** Your use of a third party MCP Client/LLM is subject solely to the terms of use for such MCP/LLM, and IBM is not responsible for the performance of such third party tools. IBM expressly disclaims any and all warranties and liability for third party MCP Clients/LLMs, and may not be able to provide support to resolve issues which are caused by the third party tools.

## Installation

### Individual Skills

Install Agent Skills in GitHub Copilot, Claude Code, Opencode, Cursor, and more:

```bash
# List all skills
npx skills add hashicorp/agent-skills

# Install a specific skill
npx skills add hashicorp/agent-skills/terraform/code-generation/skills/terraform-style-guide
```

### Claude Code Plugin

First, add the marketplace, then install plugins:

```bash
# Add the HashiCorp marketplace
claude plugin marketplace add hashicorp/agent-skills

# Install plugins
claude plugin install terraform-code-generation@hashicorp
claude plugin install terraform-module-generation@hashicorp
claude plugin install terraform-provider-development@hashicorp
claude plugin install packer-builders@hashicorp
claude plugin install packer-hcp@hashicorp
```

Or use the interactive interface:
```bash
/plugin
```

## Structure

```
agent-skills/
├── .claude-plugin/
│   └── marketplace.json
├── terraform/              # Terraform skills
├── packer/                 # Packer skills
├── <product>/              # Future products (Vault, Consul, etc.)
└── README.md
```

Each product folder contains plugins, and each plugin contains skills:

```
<product>/
└── <plugin>/
    ├── .claude-plugin/plugin.json
    └── skills/
        └── <skill>/
            └── SKILL.md
```

## License

MPL-2.0

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `memberlist.md`
```markdown
# 📦 hashicorp/memberlist [🔖 PENDING/APPROVE]
🔗 https://github.com/hashicorp/memberlist


## Meta
- **Stars:** ⭐ 4044 | **Forks:** 🍴 468
- **Language:** Go | **License:** MPL-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Golang package for gossip based membership and failure detection

## README (trích đầu)
```
# memberlist [![GoDoc](https://godoc.org/github.com/hashicorp/memberlist?status.png)](https://godoc.org/github.com/hashicorp/memberlist) [![CircleCI](https://circleci.com/gh/hashicorp/memberlist.svg?style=svg)](https://circleci.com/gh/hashicorp/memberlist)

memberlist is a [Go](http://www.golang.org) library that manages cluster
membership and member failure detection using a gossip based protocol.

The use cases for such a library are far-reaching: all distributed systems
require membership, and memberlist is a re-usable solution to managing
cluster membership and node failure detection.

memberlist is eventually consistent but converges quickly on average.
The speed at which it converges can be heavily tuned via various knobs
on the protocol. Node failures are detected and network partitions are partially
tolerated by attempting to communicate to potentially dead nodes through
multiple routes.

## Building

If you wish to build memberlist you'll need Go version 1.2+ installed.

Please check your installation with:

```
go version
```

## Usage

Memberlist is surprisingly simple to use. An example is shown below:

```go
/* Create the initial memberlist from a safe configuration.
   Please reference the godoc for other default config types.
   http://godoc.org/github.com/hashicorp/memberlist#Config
*/
list, err := memberlist.Create(memberlist.DefaultLocalConfig())
if err != nil {
	panic("Failed to create memberlist: " + err.Error())
}

// Join an existing cluster by specifying at least one known member.
n, err := list.Join([]string{"1.2.3.4"})
if err != nil {
	panic("Failed to join cluster: " + err.Error())
}

// Ask for members of the cluster
for _, member := range list.Members() {
	fmt.Printf("Member: %s %s\n", member.Name, member.Addr)
}

// Continue doing whatever you need, memberlist will maintain membership
// information in the background. Delegates can be used for receiving
// events when members join or leave.
```

The most difficult part of memberlist is configuring it since it has many
available knobs in order to tune state propagation delay and convergence times.
Memberlist provides a default configuration that offers a good starting point,
but errs on the side of caution, choosing values that are optimized for
higher convergence at the cost of higher bandwidth usage.

For complete documentation, see the associated [Godoc](http://godoc.org/github.com/hashicorp/memberlist).

## Protocol

memberlist is based on ["SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol"](http://ieeexplore.ieee.org/document/1028914/). However, we extend the protocol in a number of ways:

* Several extensions are made to increase propagation speed and
convergence rate.
* Another set of extensions, that we call Lifeguard, are made to make memberlist more robust in the presence of slow message processing (due to factors such as CPU starvation, and network delay or loss).

For details on all of these extensions, please read our pape
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

