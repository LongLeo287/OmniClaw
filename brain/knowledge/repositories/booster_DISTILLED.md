---
id: repo-fetched-booster-144230
type: knowledge
owner: OA
registered_at: 2026-04-05T04:00:26.811814
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_booster_144230

## Assimilation Report
Auto-cloned repository: FETCHED_booster_144230

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# ![Booster Framework](https://user-images.githubusercontent.com/175096/217907175-b81b3937-d773-45fd-85ca-716f9813432d.png)

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fboostercloud%2Fbooster%2Fbadge%3Fref%3Dmain&style=flat)](https://actions-badge.atrox.dev/boostercloud/booster/goto?ref=main)
[![oclif](https://img.shields.io/badge/cli-oclif-brightgreen.svg)](https://oclif.io)
[![License](https://img.shields.io/npm/l/@boostercloud/cli)](https://github.com/boostercloud/booster/blob/main/package.json)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
![Integration tests](https://github.com/boostercloud/booster/actions/workflows/wf_test-integration.yml/badge.svg)
[![Discord](https://img.shields.io/discord/763753198388510780.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/bDY8MKx)
[![Docs](https://img.shields.io/badge/Docs-Booster-blue)](https://docs.boosterframework.com)
---

# What is Booster Framework?

[Booster Framework](https://boosterframework.com) is a software development framework designed to create event-driven backend microservices that focus on extreme development productivity. It provides a highly opinionated implementation of the CQRS and Event Sourcing patterns in Typescript, using [DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design) semantics that makes business logic fit naturally within the code. Thanks to Booster, business, product, and technical teams can collaborate, sharing a much closer language.

Booster uses advanced static analysis techniques and takes advantage of the Typescript type system to understand the structure and semantics of your code and minimize the amount of glue code. It’s capable not just of building an entirely functioning GraphQL API for you, but also to build an optimal, production-ready and scalable cloud infrastructure for your application in Azure or AWS.

Combining these features, Booster provides an unprecedented developer experience. On the one hand, it helps you write simpler code, defining your application in terms of commands, events, entities, and read models. On the other hand, you don't have to worry about the tremendous amount of low-level configuration details of conventional tools. You write highly semantic code, and if it compiles, you can run it on the cloud at scale.

Booster is 100% open-source and designed with extensibility in mind. If your desired infrastructure doesn't match the existing implementations, you can easily fork and adapt them or create a new one using your infrastructure-as-code tool of preference. Booster also supports extensions (called “Rockets”) that allow users to implement additional functionalities.

If you want to help us to drive Booster forward or have questions, don't hesitate to ping us on [Discord](https://discord.gg/bDY8MKx)!

# Why Booster instead of X?

Booster is designed to maximize developer productivity, and every framework feature is carefully thought out to put your application in production as soon as possible. The CLI helps you to get up and running quickly, and the easy-to-comprehend abstractions and the opinionated architecture make it easy to understand how to organize your code and become productive sooner.

The no-boilerplate politics goes to the extreme, as Booster understands the semantics of your code to create a fully-working GraphQL API for you, as well as an optimal serverless cloud infrastructure and database integrations. And, of course, the API and infrastructure are transparently updated when the application changes.

It would be easier to understand Booster capabilities by listing the things that you won’t need to implement or maintain with Booster:

* You won’t need to maintain GraphQL schemas
* You won’t need to implement GraphQL resolvers
* You won’t have to manage URL paths
* You won’t have to design the API schemas
* You won’t have to deserialize or serialize JSON objects
* You won’t need to use DTOs
* You won’t need to deal with ORM mappings and/or database queries
* You won’t need to write infrastructure configuration or deployment scripts
* You won’t need to build WebSockets for subscriptions

All those things, and more, will be given to you by default and entirely for free, as Booster is open-source and runs in your own cloud account!

# Current state and roadmap

[The roadmap](https://github.com/orgs/boostercloud/projects/2/views/2) is community-driven; the core team actively participates in the Booster community, listening to real users and prioritizing those issues and ideas that provide the most value for the majority. So don't hesitate to create issues or leave comments in [Discord](https://discord.gg/k7b4B8CDtT) and tell us about your questions and ideas.

AWS and Azure integrations are thoroughly tested (with unit and integration tests running automatically before every release), and are currently used in production in projects of all-sized organizations, from startups to massive enterprises.

# The "Booster Way"

Booster Framework follows the next principles:

* *Play nicely*: Booster is not here to replace your toolkit but to expand it. Booster's goal is to get along well with your existing auth, queues, databases, and services, providing a modern and swift tool to build new functionalities that take full advantage of the cloud. Booster is still a Node.js application that you can extend with any tool from your Node.js environment.
* *Domain Driven Design first:* Software should be designed around business-level concepts to enhance the team's communication. All code in Booster is defined in terms of Commands, Events, Handlers, and Entities, limiting the need for artificial developer-only constructs.
* *CQRS and Event-Sourcing:* Booster is designed around the concepts of CQRS and Event-Sourcing. This design has many advantages regarding scalability and data management. It even allows you to travel back in time!
* *The cloud is the machine:* We believe that the developers' tools should create infrastructure transparently in the same way that a compiler hides the details of the target processor. We often think about Booster as the "TypeScript-to-Cloud compiler."
* *True Serverless*: Serverless is about to stop caring about your servers, but many implementations still require long YAML files to describe your infrastructure, and you need to know what you're doing. True Serverless means that you don't even care about cloud configuration. Booster will figure it out for you based on the code structure you write.
* *Convention over Configuration:* We prefer to provide standardized highly-opinionated modules than highly-configurable ones. This helps us to keep your code simple and follow the best practices when deploying your applications to the cloud. Decorating your classes with the provided semantic decorators also helps abstract most of the boilerplate code.
* *Don't Repeat Yourself (Extreme edition):* /The only code that matters is the one that makes your application different/. We push the TypeScript structure and type system to the limit to avoid writing repetitive code, like object-to-JSON serializations, API or database schemas, or redundant architecture layers. Boster understands the semantics of your code and connects the dots.
* *Self-documenting APIs* We adopted GraphQL because it's a self-documenting standard. You can grab a standard GraphQL client like [ApolloClient](https://github.com/apollographql/apollo-client) and start using a Booster backend right away with no complicated integrations.
* *Developer productivity:* Software development is fun, and a modern tool should make it even more fun, reducing the need for mundane tasks. Booster provides code generators to help you quickstart new projects and objects, and the framework types and APIs are hand-crafted to help your IDE help you.

# Contributing

You can join the conversation and start contributing in any of the following ways:
* [Say hello in Discord](https://discord.gg/bDY8MKx)
* [Create a new issue in Github](https://github.com/boostercloud/booster/issues/new/choose)
* [Try the framework and let us know how you liked it!](https://docs.boosterframework.com/category/getting-started)

Please refer to [`CONTRIBUTING.md`](./CONTRIBUTING.md) for more details. Pull requests are welcome. For major changes, please
open an issue first to discuss what you would like to change.

# License

The Booster Framework is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.

# Resources

* [Website](https://boosterframework.com)
* [Documentation](https://docs.boosterframework.com)
* [Step-by-step guides and examples](docs/examples)
* [Join the conversation in Discord](https://discord.gg/k7b4B8CDtT)
* [Twitter](https://twitter.com/boostthecloud)
* [Demos and more on Youtube](https://www.youtube.com/channel/UCpUTONI8OG19pr9A4cn35DA)
* [Rocket to the Cloud Podcast](https://www.youtube.com/channel/UCxUYk1SVyNRCGNV-9SYjEFQ)
* [Booster in Dev.to](https://dev.to/boostercloud)






```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
info@booster.cloud.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to Booster

> **DISCLAIMER:** The Booster docs are undergoing an overhaul. Most of what's written here applies, but expect some hiccups in the build process
> that is described here, as it changed in the last version. New documentation will have this documented properly.

Thanks for taking the time to contribute to Booster. It is an open-source project and it wouldn't be possible without people like you 🙏🎉

This document is a set of guidelines to help you contribute to Booster, which is hosted on the [`boostercloud`](https://github.com/boostercloud) GitHub
organization. These aren’t absolute laws, use your judgment and common sense 😀.
Remember that if something here doesn't make sense, you can also propose a change to this document.

<!-- toc -->

- [Code of Conduct](#code-of-conduct)
- [I don't want to read this whole thing, I just have a question!!!](#i-don39t-want-to-read-this-whole-thing-i-just-have-a-question)
- [What should I know before I get started?](#what-should-i-know-before-i-get-started)
  - [Packages](#packages)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Improving documentation](#improving-documentation)
  - [Create your very first GitHub issue](#create-your-very-first-github-issue)
- [Your First Code Contribution](#your-first-code-contribution)
  - [Getting the code](#getting-the-code)
  - [Understanding the "rush monorepo" approach and how dependencies are structured in the project](#understanding-the-rush-monorepo-approach-and-how-dependencies-are-structured-in-the-project)
  - [Running unit tests](#running-unit-tests)
  - [Running integration tests](#running-integration-tests)
  - [Github flow](#github-flow)
  - [Publishing your Pull Request](#publishing-your-pull-request)
  - [Branch naming conventions](#branch-naming-conventions)
  - [Commit message guidelines](#commit-message-guidelines)
- [Code Style Guidelines](#code-style-guidelines)
  - [Importing other files and libraries](#importing-other-files-and-libraries)
  - [Functional style](#functional-style)
  - [Use `const` and `let`](#use-const-and-let)

<!-- tocstop -->

## Code of Conduct

This project and everyone participating in it are expected to uphold the [Booster's Code of Conduct](https://github.com/boostercloud/booster/blob/main/CODE_OF_CONDUCT.md), based on the Covenant Code of Conduct.
If you see unacceptable behavior, please communicate so to `hello@booster.cloud`.

## I don't want to read this whole thing, I just have a question

Go ahead and ask the community in [Discord](https://discord.com/invite/bDY8MKx) or [create a new issue](https://github.com/boostercloud/booster/issues).

## What should I know before I get started?

### Packages

Booster is divided in many different packages. The criteria to split the code in packages is that each package meets at least one of the following conditions:

- They must be run separately, for instance, the CLI is run locally, while the support code for the project is run on the cloud.
- They contain code that is used by at least two of the other packages.
- They're a vendor-specific specialization of some abstract part of the framework (for instance, all the code that is required to support Azure is in separate packages).

The packages are managed using [rush](https://rushjs.io/) and [npm](https://npmjs.com), if you run `rush build`, it will build all the packages.

The packages are published to `npmjs` under the prefix `@boostercloud/`, their purpose is as follows:

- `cli` - You guessed it! This package is the `boost` command-line tool, it interacts only with the core package in order to load the project configuration. The specific provider packages to interact with the cloud providers are loaded dynamically from the project config.
- `framework-core` - This one contains all the framework runtime vendor-independent logic. Stuff like the generation of the config or the commands and events handling happens here. The specific provider packages to interact with the cloud providers are loaded dynamically from the project config.
- `framework-integration-tests` - Implements integration tests for all supported vendors. Tests are run on real infrastructure using the same mechanisms than a production application. This package `src` folder includes a synthetic Booster application that can be deployed to a real provider for testing purposes.
- `framework-provider-aws` (Deprecated) - Implements all the required adapters to make the booster core run on top of AWS technologies like Lambda and DynamoDB using the AWS SDK under the hoods.
- `framework-provider-aws-infrastructure` (Deprecated) - Implements all the required adapters to allow Booster applications to be deployed to AWS using the AWS CDK under the hoods.
- `framework-provider-local` - Implements all the required adapters to run the Booster application on a local express server to be able to debug your code before deploying it to a real cloud provider.
- `framework-provider-local-infrastructure` - Implements all the required code to run the local development server.
- `framework-types` - This package defines types that the rest of the project will use. This is useful for avoiding cyclic dependencies. Note that this package should not contain stuff that are not types, or very simple methods related directly to them, i.e. a getter or setter. This package defines the main booster concepts like:
  - Entity
  - Command
  - etc…

This is a dependency graph that shows the dependencies among all packages, including the application using Booster:
![Booster packages dependencies](https://raw.githubusercontent.com/boostercloud/booster/main/docs/img/packages-dependencies.png)

## How Can I Contribute?

Contributing to an open source project is never just a matter of code, you can help us significantly by just using Booster and interacting with our community. Here you'll find some tips on how to do it effectively.

### Reporting Bugs

Before creating a bug report, please search for similar issues to make sure that they're not already reported. If you don't find any, go ahead and create an issue including as many details as possible. Fill out the required template, the information requested helps us to resolve issues faster.

> **Note**: If you find a Closed issue that seems related to the issues that you're experiencing, make sure to reference it in the body of your new one by writing its number like this => #42 (Github will autolink it for you).

Bugs are tracked as GitHub issues. Explain the problem and include additional details to help maintainers reproduce the problem:

- Use a clear and descriptive title for the issue to identify the problem.
- Describe the exact steps which reproduce the problem in as many details as possible.
- Provide specific examples to demonstrate the steps. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use Markdown code blocks.
- Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
- Explain which behavior you expected to see instead and why.
- If the problem is related to performance or memory, include a CPU profile capture with your report.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Make sure you provide the following information:

- Use a clear and descriptive title for the issue to identify the suggestion.
- Provide a step-by-step description of the suggested enhancement in as many details as possible.
- Provide specific examples to demonstrate the steps. Include copy/pasteable snippets which you use in those examples, as Markdown code blocks.
- Describe the current behavior and explain which behavior you expected to see instead and why.
- Explain why this enhancement would be useful to most Booster users and isn't something that can or should be implemented as a community package.
- List some other libraries or frameworks where this enhancement exists.

### Improving documentation

[Booster documentation](https://docs.boosterframework.com) is treated as a live document that continues improving on a daily basis. If you find something that is missing or can be improved, please contribute, it will be of great help for other developers.
To contribute you can use the button "Edit on github" at the top of each chapter.

#### Documentation principles and practices

The ultimate goal of a technical document is to translate the knowledge from the technology creators into the reader's mind so that they learn. The challenging
part here is the one in which they learn. It is challenging because, under the same amount of information, a person can suffer an information overload because
we (humans) don't have the same information-processing capacity. That idea is going to work as our compass, it should drive our efforts so people with less
capacity is still able to follow and understand our documentation.

To achieve our goal we propose writing documentation following these principles:

1. Clean and Clear
2. Simple
3. Coherent
4. Explicit
5. Attractive
6. Inclusive
7. Cohesive

##### Principles

**1. Clean and Clear**

Less is more. Apple is, among many others, a good example of creating clean and clear content, where visual elements are carefully chosen to look beautiful
(e.g. [Apple's swift UI](https://developer.apple.com/tutorials/swiftui)) and making the reader getting the point as soon as possible.

The intention of every section, paragraph, and sentence must be clear, we should avoid writing details of two different things even when they are related.
It is better to link pages and keep the focus and the intention clear, Wikipedia is the best example on this.

**2. Simple**

Technical writings deal with different backgrounds and expertise from the readers. We should not assume the reader knows everything we are talking about
but we should not explain everything in the same paragraph or section. Every section has a goal to stick to the goal and link to internal or external resources
to go deeper.

Diagrams are great tools, you know a picture is worth more than a thousand words unless that picture contains too much information.
Keep it simple intentionally omitting details.

**3. Coherent**

The documentation tells a story. Every section should integrate naturally without making the reader switch between different contexts. Text, diagrams,
and code examples should support each other without introducing abrupt changes breaking the reader’s flow. Also, the font, colors, diagrams, code samples,
animations, and all the visual elements we include, should support the story we are telling.

**4. Explicit**

Go straight to the point without assuming the readers should know about something. Again, link internal or external resources to clarify.

The index of the whole content must be visible all the time so the reader knows exactly where they are and what is left.

**5. Attractive**

Our text must be nice to read, our diagrams delectable to see, and our site… a feast for the eyes!!

**6. Inclusive**

Everybody should understand our writings, especially the topics at the top. We have arranged the documentation structure in a way that anybody can dig
deeper by just going down so, sections 1 to 4 must be suitable for all ages.

Use gender-neutral language to avoid the use of he, him, his to refer to undetermined gender. It is better to use their or they as a gender-neutral
approach than s/he or similars.

**7. Cohesive**

Writing short and concise sentences is good, but remember to use proper connectors (“Therefore”, “Besides”, “However”, “thus”, etc) that provide a
sense of continuation to the whole paragraph. If not, when people read the paragraphs, their internal voice sounds like a robot with unnatural stops.

For example, read this paragraph and try to hear your internal voice:

> Entities are created on the fly, by reducing the whole event stream. You shouldn't assume that they are stored anywhere.  Booster does create
automatic snapshots to make the reduction process efficient. You are the one in charge of writing the reducer function.

And now read this one:

> Entities are created on the fly by reducing the whole event stream. While you shouldn't assume that they are stored anywhere,  Booster does create automatic
snapshots to make the reduction process efficient. In any case, this is opaque to you and the only thing you should care is to provide the reducer function.

Did you feel the difference? The latter makes you feel that everything is connected, it is more cohesive.

##### Practices

There are many writing styles depending on the type of document. It is common within technical and scientific writing to use Inductive and/or Deductive styles
for paragraphs. They have different outcomes and one style may suit better in one case or another, that is why it is important to know them, and decide which
one to use in every moment. Let’s see the difference with 2 recursive examples.

**Deductive paragraphs ease the reading for advanced users but still allows you to elaborate on ideas and concepts for newcomers**. In deductive paragraphs,
the conclusions or definitions appear at the beginning, and then, details, facts, or supporting phrases complete the paragraph’s idea. By placing the
conclusion in the first sentence, the reader immediately identifies the main point so they can decide to skip the whole paragraph or keep reading.
If you take a look at the structure of this paragraph, it is deductive.

On the other hand, if you want to drive the readers' attention and play with it as if they were in a roller coaster, you can do so by using a different approach.
In that approach, you first introduce the facts and ideas and then you wrap them with a conclusion. This style is more narrative and forces the reader to
continue because the main idea is diluted in the whole paragraph. Once all the ideas are placed together, you can finally conclude the paragraph. **This style is
called Inductive.**

The first paragraph is deductive and the last one is inductive. In general, it is better to use the deductive style, but if we stick to one, our writing will start looking weird and maybe boring.
So decide one or another being conscious about your intention.

### Create your very first GitHub issue

[Click here](https://github.com/boostercloud/booster/issues/new) to start making contributions to Booster.

## Your First Code Contribution

Unsure where to begin contributing to Booster? You can start by looking through issued tagged as `good-first-issue` and `help-wanted`:

- Beginner issues - issues which should only require a few lines of code, and a test or two.
- Help wanted issues - issues which should be a bit more involved than beginner issues.

Both issue lists are sorted by the total number of comments. While not perfect, 
... [TRUNCATED]
```

### File: upgrade-v2.md
```md
# Upgrade from Booster v1.x.x to Booster v2.x.x

Booster v2 introduces the following breaking changes:

1. **Node 18 support**: Booster v2 has been upgraded to work with Node 18. If you're using an older version of Node, you'll need to upgrade it.
2. **Azure runtime upgraded to v4**: The Azure Functions Runtime has been upgraded from v3 to v4. If you're using Booster v1.x.x with Azure, you may need to perform a migration. Check out [Azure's migration guide](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-3-version-4?tabs=net6-isolated%2Cazure-cli%2Cwindows&pivots=programming-language-typescript) for more details.
3. **The AWS provider has been deprecated**: Due to significant changes in recent versions of the AWS CDK, specifically the transition from CDKToolkit to a cli tool as noted [here](https://github.com/aws/aws-cdk-rfcs/issues/300), upgrading our current implementation would require a substantial rewrite. Given the open-source nature of our project without direct revenue streams, the ensuing maintenance costs are unfeasible. However, we are open to upgrading the AWS provider or creating an alternative implementation using other technologies like Terraform's CDKTF, with community contributions or sponsorships. If you're interested in supporting us, we welcome you to reach out via the official channels listed on the [Booster's website](https://boosterframework.com).

```

### File: upgrade-v3.md
```md
# Upgrade from Booster v2.x.x to Booster v3.x.x

Booster v3 introduces the following breaking changes:

1. **Node 20 support**: Booster v3 has been upgraded to work with Node 20. If you're using an older version of Node, you'll need to upgrade it.
```

### File: upgrade-v4.md
```md
# Upgrade from Booster v3.x.x to Booster v4.x.x

Booster v4 introduces the following breaking changes:

## 1. Node 22 Support

Booster v4 has been upgraded to work with Node 22. If you're using an older version of Node, you'll need to upgrade it.

```bash
# Check your current Node version
node --version

# Upgrade to Node 22 using nvm (recommended)
nvm install 22
nvm use 22
```

## 2. Azure Functions v4 Programming Model (Breaking Change)

This is the most significant change in Booster v4. The Azure provider has been migrated from the Azure Functions v3 programming model to the **Azure Functions v4 programming model**.

### What Changed?

The v4 programming model introduces a fundamentally different way of registering and defining Azure Functions:

- **No more `function.json` files**: Functions are now registered programmatically using `app.*()` methods from `@azure/functions`.
- **New trigger and binding syntax**: The way triggers and bindings are defined has changed significantly.
- **Updated runtime**: The Azure Functions runtime now uses Node 22 with the v4 model.

### Migration Steps

1. **Update your Booster dependencies** to v4.x.x in your `package.json`:
   ```json
   {
     "dependencies": {
       "@boostercloud/framework-core": "^4.0.0",
       "@boostercloud/framework-provider-azure": "^4.0.0",
       "@boostercloud/framework-provider-azure-infrastructure": "^4.0.0",
       "@boostercloud/framework-types": "^4.0.0"
     }
   }
   ```

2. **Redeploy your application**: Since the function registration model has changed, you'll need to redeploy your application completely.

## 3. Rockets Must Be Updated (Breaking Change)

**This is critical**: If you are using any Rockets in your Booster application, they **must be updated** to be compatible with Booster v4 and the Azure Functions v4 programming model.

### Why Rockets Need Updating

Rockets that add Azure Functions (such as webhooks, file uploads, or custom endpoints) previously relied on generating `function.json` files. With the v4 programming model, Rockets must now:

1. **Use programmatic function registration**: Instead of generating `function.json` files, Rockets must use the `app.*()` registration API.
2. **Implement the `mountFunctionsV4` method**: Rockets must implement the new `mountFunctionsV4` method (replacing the deprecated `mountCode` and `mountFunctions` methods) to provide their function registration code.
3. **Update trigger and binding definitions**: All triggers and bindings must use the new v4 syntax.

### Checking Rocket Compatibility

Before upgrading, verify that all Rockets you're using have been updated for Booster v4:

| Rocket | Minimum Version for v4 |
|--------|------------------------|
| `@boostercloud/rocket-webhook` | Check the rocket's repository for v4-compatible version |
| `@boostercloud/rocket-file-uploads` | Check the rocket's repository for v4-compatible version |
| `@boostercloud/rocket-static-sites` | Check the rocket's repository for v4-compatible version |
| `@boostercloud/rocket-backup-booster` | Check the rocket's repository for v4-compatible version |

### For Rocket Authors: Migration Guide

If you maintain a custom Rocket, here's how to update it for Booster v4:

#### Before (v3 - function.json based):

Previously, Rockets would generate `function.json` files:

```json
{
  "bindings": [
    {
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": ["post"]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    }
  ]
}
```

#### After (v4 - programmatic registration):
```typescript
// Now, Rockets must provide code for programmatic registration
import { app } from '@azure/functions'

app.http('myWebhook', {
  methods: ['POST'],
  authLevel: 'anonymous',
  handler: async (request, context) => {
    // Handle the request
    return { status: 200, body: 'OK' }
  }
})
```

### Key Changes for Rocket Implementation

1. **Update the `rocketForAzure()` method**: Ensure it returns infrastructure compatible with the v4 model.

2. **Implement `mountFunctionsV4`** (replaces deprecated `mountCode` and `mountFunctions`):
   ```typescript
   import { InfrastructureRocket } from '@boostercloud/framework-provider-azure-infrastructure'
   import { FunctionAppV4Definitions } from '@boostercloud/framework-provider-azure-infrastructure'

   const MyRocket = (params: MyRocketParams): InfrastructureRocket => ({
     mountStack: async (config, applicationSynthStack, utils) => {
       // Infrastructure provisioning
       return applicationSynthStack
     },
     mountFunctionsV4: async (config, applicationSynthStack, utils): Promise<FunctionAppV4Definitions> => {
       // Return an array of function app definitions with v4 registration code
       return [
         {
           functionAppName: applicationSynthStack.functionApp.name,
           functionsCode: `
             app.http('myEndpoint', {
               methods: ['POST'],
               authLevel: 'anonymous',
               handler: async (request, context) => {
                 return await myHandler(request, context)
               }
             })
           `,
           hostJsonPath: undefined, // Optional: path to custom host.json
         },
       ]
     },
   })
   ```

3. **Update any direct Azure Functions SDK usage** to use `@azure/functions` v4 APIs.

## 4. Additional Considerations

### Azure Infrastructure

- Ensure your Azure Function App is configured to use Node 22 runtime.
- The Function App must support the v4 programming model.

### Local Development

- Update your local development environment to Node 22.
- The local provider has been updated to work with the new model.

### Testing

After upgrading:
1. Run your integration tests to ensure all functionality works correctly.
2. Test all Rocket-provided endpoints.
3. Verify scheduled commands are executing as expected.
4. Check that subscriptions and WebSocket connections work properly.

## Need Help?

If you encounter issues during the upgrade:
- Check the [Booster documentation](https://docs.boosterframework.com)
- Open an issue on [GitHub](https://github.com/boostercloud/booster)
- Reach out via the official channels listed on the [Booster website](https://boosterframework.com)


```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for booster
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!--

Remember to refer to the CONTRIBUTING.md file before sending the PR

- https://github.com/boostercloud/booster/blob/main/CONTRIBUTING.md#github-flow
- https://github.com/boostercloud/booster/blob/main/CONTRIBUTING.md#publishing-your-pull-request

- Make sure you followed our Code style https://github.com/boostercloud/booster/blob/main/CONTRIBUTING.md#code-style-guidelines

- Make sure everything works https://github.com/boostercloud/booster/blob/main/CONTRIBUTING.md#getting-the-code

- Run tests 🐛 https://github.com/boostercloud/booster/blob/main/CONTRIBUTING.md#running-unit-tests

-->

## Description
<Describe the purpose of this pull request>

## Changes

<!-- 

Describe changes you have made:

- Added tests
- Described "amazingMethodName" purpose in the docs
- New method `amazingMethodName`

-->

## Checks
- [ ] Project Builds
- [ ] Project passes tests and checks
- [ ] Updated documentation accordingly

<!-- 
## Additional information

Here you can add any additional information about your PR

For example:

- Reference issue number

- Mention any changes or concerns you may have about this PR

- Reference links to any resource that help clarifying the intent and goals of the change.

-->

```

### File: .github\README_CICD.md
```md
# Booster GitHub CI/CD

This document describes the process and structure of the configuration of the project's GitHub actions and workflows.

Booster as a project has some special needs in terms of CI/CD compared to your regular project because it is a framework,
and it handles so much complexity. So we have to make sure that everything works flawlessly as much as possible. Take into
account that:

- Because it is a framework and not only a library, the framework will take decisions on behalf of the user, in terms of design
  and other things, so in case of failure, we make sure that we have done as much as possible to prevent it so
  the user is not confused.
- It handles the creation and wiring of many cloud components, which are lots of moving pieces, so everything is double-checked
  to prevent errors in deployed environments.
- It is a multi-cloud framework, and behavior is double-checked both on AWS and Azure. Ensuring everything runs smoothly, regardless of the choice of the user.

We always keep improving our CI/CD processes, but we always make sure that we have the above covered.

The two main folders you have to look at are:

- `.github/actions`
- `.github/workflows`

Here we define the components that we reuse to simplify the CI/CD as much as possible.

## The Actions folder

The actions folder defines a couple of reusable actions that we use throughout the CI/CD process:

- `build`
  - This action ensures that the dependencies are properly cached and then tries
    to build the project.
- `call-rush`
  - This action uses the command passed as a parameter to call `rush`. It will install rush if it's not installed on the current CI/CD machine.
- `test-integration-run-one`
  - This one is a bit more complex. It is the foundation of our integration tests, as all
    jobs that run those will use this action.
  - It does a fork-based checkout if it was triggered by a `/integration` command.
  - It will build the project using the action above.
  - It will set the `BOOSTER_APP_SUFFIX` environment variable to the appropriate SHA (either the one from the fork or the current one in the branch, in that order).
  - It will download the packed project from the GitHub cache (more on this later).
  - Will log in to Azure, if the Azure credentials are defined.
  - Finally, it will run the integration test that was passed by parameters, using all the secrets required for that.

## Workflows

This folder uses the following convention:

- Files prefixed with `re_` are [reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows) and are meant to be used instead of copy-pasting jobs
- Files prefixed with `wf_` are regular workflows that define workflows in the GitHub Actions CI/CD pipeline
- Files get their name in descending order, in the sense of the things they do. E.g.
  - `test-unit` instead of `unit-tests`
  - `test-integration-aws` instead of `aws-integration`

There are some special workflow files like `codeql-analysis` or `codesee-arch-diagram` that are handled by 3rd party services and are left
with their default name.

The most complex one, which requires more explanation is the `wf_test-integration` one, it:

1. Will run in these conditions
   1. Triggered by a `/integration` command in a PR
   2. Triggered by `wf_publish-npm` when a push happens in `main`
2. If it was triggered in a PR, it will send a comment with a link to the integration tests run.
3. Will compile and pack the Booster packages into some `.tar.gz` and upload them to the GitHub cache.
4. Run in parallel the integration tests for
   1. AWS
   2. CLI
   3. Local Provider
   4. Azure
5. Notify the outcome of the integration tests as a comment in the PR (if applicable).

### `re_test-integration-*`

These files are the ones responsible for running the integration tests for each of the different packages of Booster.

They are pretty straightforward, but perhaps the cloud related ones (e.g. AWS) are a bit more
complex. They will:

1. Deploy the project
2. Will run the following integration tests in parallel
   1. Functionality
   2. End-to-end
   3. Load tests
3. Nuke the cloud resources

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug Report
about: Use this template for reporting a bug.
labels: bug
---

# Bug Report

## Current Behavior

A clear and concise description of the behavior.

## Expected behavior

A clear and concise description of what you expected to happen (or code).

## Possible Solution

<!--- Only if you have suggestions on a fix for the bug -->

## Additional information

### Environment

- Booster version: [e.g. 0.15.1] <!--- You can check this with `boost version` -->
- Node/npm version: [e.g. Node 14/npm 7]
- OS: [e.g. OSX 10.13.4, Windows 10]

```

### File: .github\ISSUE_TEMPLATE\documentation.md
```md
---
name: Documentation issue
about: Use this template for reporting issue or improvements for documentation.
labels: documentation
---
# Documentation issue

## Description

<-- Description of the documentation issue -->

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Use this template to suggest an idea for this project.
labels: feature-request
---

# Feature Request

## Description

<!--- Description of the feature you want to be implemented -->

## Possible Solution

<!--- Only if you have suggestions on a implementation -->

## Additional information

```

### File: .github\ISSUE_TEMPLATE\maintainance.md
```md
---
name: Maintainance task
about: Use this template to propose a maintainance task.
labels: maintainance
---

# Maintainance task

## Description

<!--- Description of the maintainance task you are proposing. Please include as much context and information as possible. -->

## Possible Solution

<!--- Only if you have suggestions on a implementation -->

## Additional information

<!-- Only if you want to share additional context or related information -->
```

