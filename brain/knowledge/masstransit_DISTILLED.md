---
id: masstransit
type: knowledge
owner: OA_Triage
---
# masstransit
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
MassTransit
===========

MassTransit is a _free, open-source_ distributed application framework for .NET. MassTransit makes it easy to create applications and services that leverage message-based, loosely-coupled asynchronous communication for higher availability, reliability, and scalability.

![Mass Transit](https://avatars2.githubusercontent.com/u/317796?s=200&v=4 "Mass Transit")

MassTransit is Apache 2.0 licensed.

## Documentation

Get started by [reading through the documentation](https://masstransit-project.com/).

Build Status
------------

| Branch        |                                                                                                Status                                                                                                |
|---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| master        |    [![master](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml/badge.svg?branch=master&event=push)](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml)    |
| develop       |   [![develop](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml/badge.svg?branch=develop&event=push)](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml)   |

MassTransit NuGet Packages
---------------------------

| Package Name                                                    |   .NET   | .NET Standard | .NET Framework |
|-----------------------------------------------------------------|:--------:|:-------------:|:--------------:|
| **Main**                                                        |          |               |                |
| [MassTransit][MassTransit.nuget]                                | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Abstractions][MassTransitAbstractions.nuget]       | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Newtonsoft][MassTransitNewtonsoft.nuget]           | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.MessagePack][MassTransitMessagePack.nuget]         | 8.0, 9.0 |      2.0      |     4.7.2      |
| **Other**                                                       |          |               |                |
| [MassTransit.Analyzers][Analyzers.nuget]                        |          |      2.0      |                |
| [MassTransit.Templates][Templates.nuget]                        |          |               |                |
| [MassTransit.SignalR][SignalR.nuget]                            | 8.0, 9.0 |               |     4.7.2      |
| [MassTransit.Interop.NServiceBus][MassTransitNServiceBus.nuget] | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.TestFramework][TestFramework.nuget]                | 8.0, 9.0 |      2.0      |     4.7.2      |
| **Persistence**                                                 |          |               |                |
| [MassTransit.AmazonS3][AmazonS3.nuget]                          | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Azure.Cosmos][Cosmos.nuget]                        | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Azure.Storage][AzureStorage.nuget]                 | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Azure.Table][AzureTable.nuget]                     | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Dapper][Dapper.nuget]                              | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.DynamoDb][DynamoDb.nuget]                          | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.EntityFrameworkCore][EFCore.nuget]                 | 8.0, 9.0 |               |                |
| [MassTransit.EntityFramework][EF.nuget]                         |          |      2.1      |     4.7.2      |     
| [MassTransit.Marten][Marten.nuget]                              | 8.0, 9.0 |               |                |
| [MassTransit.MongoDb][MongoDb.nuget]                            | 8.0, 9.0 |      2.1      |     4.7.2      |
| [MassTransit.NHibernate][NHibernate.nuget]                      | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Redis][Redis.nuget]                                | 8.0, 9.0 |      2.0      |     4.7.2      |
| **Scheduling**                                                  |          |               |                |
| [MassTransit.Hangfire][Hangfire.nuget]                          | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Quartz][Quartz.nuget]                              | 8.0, 9.0 |      2.0      |     4.7.2      |
| **Transports**                                                  |          |               |                |
| [MassTransit.ActiveMQ][ActiveMQ.nuget]                          | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.AmazonSQS][AmazonSQS.nuget]                        | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.Azure.ServiceBus.Core][AzureSbCore.nuget]          | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.RabbitMQ][RabbitMQ.nuget]                          | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.SqlTransport.PostgreSQL][PostgreSQL.nuget]         | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.SqlTransport.SqlServer][SqlServer.nuget]           | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.WebJobs.EventHubs][EventHubs.nuget]                | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.WebJobs.ServiceBus][AzureFunc.nuget]               | 8.0, 9.0 |      2.0      |     4.7.2      |
| **Riders**                                                      |          |               |                |
| [MassTransit.Kafka][Kafka.nuget]                                | 8.0, 9.0 |      2.0      |     4.7.2      |
| [MassTransit.EventHub][EventHub.nuget]                          | 8.0, 9.0 |      2.0      |     4.7.2      |

## Discord 

Get help live at the MassTransit Discord server.

[![alt Join the conversation](https://img.shields.io/discord/682238261753675864.svg "Discord")](https://discord.gg/rNpQgYn)

## GitHub Issues

**Pay attention**

Please do not open an issue on GitHub, unless you have spotted an actual bug in MassTransit. 

Use [GitHub Discussions](https://github.com/MassTransit/MassTransit/discussions) to ask questions, bring up ideas, or other general items. Issues are not the place for questions, and will either be converted to a discussion or closed.

This policy is in place to avoid bugs being drowned out in a pile of sensible suggestions for future 
enhancements and calls for help from people who forget to check back if they get it and so on.

## Building from Source

 1. Install the latest [.NET 9 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/9.0)
 2. Clone the source down to your machine<br/>
    ```bash
    git clone https://github.com/MassTransit/MassTransit.git
    ```
 3. Run `dotnet build`

## Contributing

 1. Turn off `autocrlf`
    ```bash
    git config core.autocrlf false
    ```
 2. Hack!
 3. Make a pull request
 
# REQUIREMENTS
* .NET 9 SDK

# CREDITS
Logo Design by _The Agile Badger_

[MassTransit.nuget]: https://www.nuget.org/packages/MassTransit
[MassTransitAbstractions.nuget]: https://www.nuget.org/packages/MassTransit.Abstractions
[MassTransitNewtonsoft.nuget]: https://www.nuget.org/packages/MassTransit.Newtonsoft
[MassTransitMessagePack.nuget]: https://www.nuget.org/packages/MassTransit.MessagePack
[MassTransitNServiceBus.nuget]: https://www.nuget.org/packages/MassTransit.Interop.NServiceBus
[Analyzers.nuget]: https://www.nuget.org/packages/MassTransit.Analyzers
[Templates.nuget]: https://www.nuget.org/packages/MassTransit.Templates
[SignalR.nuget]: https://www.nuget.org/packages/MassTransit.SignalR
[TestFramework.nuget]: https://www.nuget.org/packages/MassTransit.TestFramework

[Prometheus.nuget]: https://www.nuget.org/packages/MassTransit.Prometheus

[Cosmos.nuget]: https://www.nuget.org/packages/MassTransit.Azure.Cosmos
[AzureStorage.nuget]: https://www.nuget.org/packages/MassTransit.Azure.Storage
[AzureTable.nuget]: https://www.nuget.org/packages/MassTransit.Azure.Table
[Dapper.nuget]: https://www.nuget.org/packages/MassTransit.DapperIntegration
[DynamoDb.nuget]: https://www.nuget.org/packages/MassTransit.DynamoDb
[EFCore.nuget]: https://www.nuget.org/packages/MassTransit.EntityFrameworkCore
[EF.nuget]: https://www.nuget.org/packages/MassTransit.EntityFramework
[Marten.nuget]: https://www.nuget.org/packages/MassTransit.Marten
[MongoDb.nuget]: https://www.nuget.org/packages/MassTransit.MongoDb
[NHibernate.nuget]: https://www.nuget.org/packages/MassTransit.NHibernate
[Redis.nuget]: https://www.nuget.org/packages/MassTransit.Redis

[Hangfire.nuget]: https://www.nuget.org/packages/MassTransit.Hangfire
[Quartz.nuget]: https://www.nuget.org/packages/MassTransit.Quartz

[ActiveMQ.nuget]: https://www.nuget.org/packages/MassTransit.ActiveMQ
[AmazonS3.nuget]: https://www.nuget.org/packages/MassTransit.AmazonS3
[AmazonSQS.nuget]: https://www.nuget.org/packages/MassTransit.AmazonSQS
[AzureSbCore.nuget]: https://www.nuget.org/packages/MassTransit.Azure.ServiceBus.Core
[RabbitMQ.nuget]: https://www.nuget.org/packages/MassTransit.RabbitMQ
[PostgreSQL.nuget]: https://nuget.org/packages/MassTransit.SqlTransport.PostgreSQL/
[SqlServer.nuget]: https://nuget.org/packages/MassTransit.SqlTransport.SqlServer/
[EventHubs.nuget]: https://www.nuget.org/packages/MassTransit.WebJobs.EventHubs
[AzureFunc.nuget]: https://www.nuget.org/packages/MassTransit.WebJobs.ServiceBus

[Kafka.nuget]: https://www.nuget.org/packages/MassTransit.Kafka
[EventHub.nuget]: https://www.nuget.org/packages/MassTransit.EventHub

```

### File: doc\package.json
```json
{
  "name": "masstransit-docus",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "nuxi dev",
    "build": "nuxi build",
    "generate": "nuxi generate",
    "preview": "nuxi preview"
  },
  "devDependencies": {
    "@nuxt-themes/docus": "^1.15.0",
    "@nuxtjs/algolia": "^1.5.0",
    "@types/chai": "^4.3.4",
    "@types/jest": "^29.2.4",
    "babel-jest": "^29.3.1",
    "chai": "^4.5.0",
    "jest": "^29.3.1",
    "nuxt": "^3.12.4",
    "ts-jest": "^29.0.3",
    "vue-gtag-next": "^1.14.0"
  },
  "dependencies": {
    "@docsearch/js": "3",
    "autoprefixer": "^10.4.13",
    "chalk": "^5.4.1",
    "postcss": "^8.4.20",
    "tailwindcss": "^3.2.4"
  }
}

```

### File: doc\README.md
```md
# Docus Starter

Starter template for [Docus](https://docus.dev).

## Clone

Clone the repository (using `nuxi`):

```bash
npx nuxi init docs -t nuxt-themes/docus-starter
```

## Setup

Install dependencies:

```bash
yarn install
```

## Development

```bash
yarn dev
```

## Edge Side Rendering

Can be deployed to Vercel Functions, Netlify Functions, AWS, and most Node-compatible environments.

Look at all the available presets [here](https://v3.nuxtjs.org/guide/deploy/presets).

```bash
yarn build
```

## Static Generation

Use the `generate` command to build your application.

The HTML files will be generated in the .output/public directory and ready to be deployed to any static compatible hosting.

```bash
yarn generate
```

## Preview build

You might want to preview the result of your build locally, to do so, run the following command:

```bash
yarn preview
```

---

For a detailed explanation of how things work, check out [Docus](https://docus.dev).

```

### File: NuGet.README.md
```md
# MassTransit

MassTransit provides a developer-focused, modern platform for creating distributed applications without complexity.

- First class testing support
- Write once, then deploy using RabbitMQ, Azure Service Bus, and Amazon SQS
- Observability via Open Telemetry (OTEL)
- Fully-supported, widely-adopted, a complete end-to-end solution

## Documentation

Get started by [reading through the documentation](https://masstransit-project.com/).

## Build Status

| Branch  |                                                                                              Status                                                                                              |
|---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| master  |  [![master](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml/badge.svg?branch=master&event=push)](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml)  |
| develop | [![develop](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml/badge.svg?branch=develop&event=push)](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml) |

## MassTransit NuGet Packages

The following NuGet packages are the currently supported.

[![alt MassTransit](https://img.shields.io/nuget/v/MassTransit.svg "MassTransit")](https://nuget.org/packages/MassTransit/)

* [MassTransit](https://nuget.org/packages/MassTransit/)
* [MassTransit.Abstractions](https://www.nuget.org/packages/MassTransit.Abstractions/)

### Transports

* [MassTransit.ActiveMQ](https://nuget.org/packages/MassTransit.ActiveMQ/)
* [MassTransit.AmazonSQS](https://nuget.org/packages/MassTransit.AmazonSQS/)
* [MassTransit.Azure.ServiceBus.Core](https://nuget.org/packages/MassTransit.Azure.ServiceBus.Core/)
    * [MassTransit.WebJobs.ServiceBus](https://nuget.org/packages/MassTransit.WebJobs.ServiceBus/)
    * [MassTransit.WebJobs.EventHubs](https://nuget.org/packages/MassTransit.WebJobs.EventHubs/)
* [MassTransit.RabbitMQ](https://nuget.org/packages/MassTransit.RabbitMQ/)
* **Riders**
    * [MassTransit.EventHub](https://nuget.org/packages/MassTransit.EventHub/)
    * [MassTransit.Kafka](https://nuget.org/packages/MassTransit.Kafka/)

### Saga Persistence

* [MassTransit.AmazonS3](https://nuget.org/packages/MassTransit.AmazonS3/)
* [MassTransit.Azure.Cosmos](https://nuget.org/packages/MassTransit.Azure.Cosmos/)
* [MassTransit.Azure.Cosmos.Table](https://nuget.org/packages/MassTransit.Azure.Cosmos.Table/)
* [MassTransit.DapperIntegration](https://nuget.org/packages/MassTransit.DapperIntegration/)
* [MassTransit.DynamoDb](https://nuget.org/packages/MassTransit.DynamoDb/)
* [MassTransit.EntityFramework](https://nuget.org/packages/MassTransit.EntityFramework/)
* [MassTransit.EntityFrameworkCore](https://nuget.org/packages/MassTransit.EntityFrameworkCore/)
* [MassTransit.Marten](https://nuget.org/packages/MassTransit.Marten/)
* [MassTransit.MongoDb](https://nuget.org/packages/MassTransit.MongoDb/)
* [MassTransit.NHibernate](https://nuget.org/packages/MassTransit.NHibernate/)
* [MassTransit.Redis](https://nuget.org/packages/MassTransit.Redis/)

### Message Data

* [MassTransit.Azure.Storage](https://nuget.org/packages/MassTransit.Azure.Storage/)

### Scheduling

* [MassTransit.Hangfire](https://nuget.org/packages/MassTransit.Hangfire/)
* [MassTransit.Quartz](https://nuget.org/packages/MassTransit.Quartz/)

### Interoperability

* [MassTransit.Interop.NServiceBus](https://nuget.org/packages/MassTransit.Interop.NServiceBus/)
* [MassTransit.Newtonsoft](https://nuget.org/packages/MassTransit.Newtonsoft/)

### Other

* [MassTransit.Analyzers](https://nuget.org/packages/MassTransit.Analyzers/)
* [MassTransit.SignalR](https://nuget.org/packages/MassTransit.SignalR/)
* [MassTransit.Prometheus](https://nuget.org/packages/MassTransit.Prometheus/)
* [MassTransit.StateMachineVisualizer](https://nuget.org/packages/MassTransit.StateMachineVisualizer/)
* [MassTransit.TestFramework](https://nuget.org/packages/MassTransit.TestFramework/)

## Deprecated Packages

The following packages from earlier versions of MassTransit are no longer supported.

* Automatonymous
* Automatonymous.NHibernate
* Automatonymous.Visualizer
* GreenPipes
* MassTransit.ApplicationInsights
* MassTransit.AspNetCore
* MassTransit.Autofac
* MassTransit.Automatonymous
* MassTransit.Automatonymous.Autofac
* MassTransit.Automatonymous.Extensions.DependencyInjection
* MassTransit.Automatonymous.Lamar
* MassTransit.Automatonymous.SimpleInjector
* MassTransit.Automatonymous.StructureMap
* MassTransit.Automatonymous.Windsor
* MassTransit.AzureServiceBus
* MassTransit.CastleWindsor
* MassTransit.Extensions.DependencyInjection
* MassTransit.Extensions.Logging
* MassTransit.Host
* MassTransit.Http
* MassTransit.Lamar
* MassTransit.Log4Net
* MassTransit.MSMQ
* MassTransit.Ninject
* MassTransit.NLog
* MassTransit.Platform.Abstractions
* MassTransit.Reactive
* MassTransit.SerilogIntegration
* MassTransit.SimpleInjector
* MassTransit.StructureMap
* MassTransit.StructureMapSigned
* MassTransit.Unity

## Discord

Get help live at the MassTransit Discord server.

[![alt Join the conversation](https://img.shields.io/discord/682238261753675864.svg "Discord")](https://discord.gg/rNpQgYn)

## GitHub Issues

> Please do not open an issue on GitHub, unless you have spotted an actual bug in MassTransit.

Use [GitHub Discussions](https://github.com/MassTransit/MassTransit/discussions) to ask questions, bring up ideas, or other general items. Issues are not the
place for questions, and will either be converted to a discussion or closed.

```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

MassTransit supports the current major version only. If issues or vulnerabilities are encountered with previous versions for which there is no workaround, upgrading to the latest version if recommended.

| Version | Supported          |
| ------- | ------------------ |
| 8.x     | :white_check_mark: |
| < 8.0   | :x:                |

## Reporting a Vulnerability

Vulnerabilities can be reported by submitting an issue.

```

### File: .devcontainer\devcontainer.json
```json
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/dotnet
{
	"name": "C# (.NET)",
	"image": "mcr.microsoft.com/devcontainers/dotnet:0-6.0",
	"features": {
		"ghcr.io/devcontainers/features/github-cli:1": {},
		"ghcr.io/dhoeric/features/act:1": {},
		"ghcr.io/devcontainers/features/dotnet:1": {
			"version": "7"
		}
	},
	"customizations": {
		"vscode": {
			"extensions": [
				"ms-dotnettools.csharp",
				"k--kato.docomment",
				"formulahendry.dotnet-test-explorer",
				"leo-labs.dotnet",
				"github.vscode-pull-request-github"
			]
		}
	}

	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [5000, 5001],

	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "dotnet restore",

	// Configure tool-specific properties.
	// "customizations": {},

	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!--
Thank you for sending the PR!

If you changed any code, please provide us with clear instructions on how you verified your changes work. Bonus points for screenshots!

Happy contributing!
-->

```

### File: doc\app.config.ts
```ts
export default defineAppConfig({
    github: {
        owner: 'MassTransit',
        repo: 'MassTransit',
        branch: 'develop'
    },
    docus: {
        title: 'MassTransit',
        description: 'An open-source distributed application framework for .NET',
        image: 'https://masstransit.io/mt-logo-color.png',
        url: 'https://masstransit.io',
        socials: {
            github: 'MassTransit/MassTransit'
        },
        aside: {
            level: 1,
            exclude: []
        },
        header: {
            showLinkIcon: true,
            exclude: []
        },
        footer: {
            credits: {
                text: 'Copyright 2025 Chris Patterson',
                href: 'https://masstransit.io',
                icon: 'IconMassTransit'
            },
            icons: [],
        },
    }
})

```

### File: doc\jest.config.js
```js
module.exports = {
  preset: 'ts-jest',
  transform: {
    '^.+\\.(ts)?$': 'ts-jest',
    '^.+\\.(js)$': 'babel-jest',
  },
}

```

### File: doc\nuxt.config.ts
```ts
export default defineNuxtConfig({
  extends: '@nuxt-themes/docus',
  css: ['~/assets/css/main.css'],

  colorMode: {
      preference: 'dark'
  },

  content: {
      documentDriven: true,
      highlight: {
          theme: {
              dark: 'github-dark',
              default: 'github-light'
          },
          preload: ['json', 'shell', 'markdown', 'yaml', 'bash', 'csharp', 'sql']
      },
      navigation: {
          fields: ['icon', 'titleTemplate', 'aside']
      }
  },

  postcss: {
      plugins: {
          'tailwindcss/nesting': {},
          tailwindcss: {},
          autoprefixer: {},
      },
  },

  runtimeConfig: {
      public: {
          algolia: {
              applicationId: process.env.ALGOLIA_APP_ID,
              apiKey: process.env.ALGOLIA_API_KEY,
              langAttribute: 'lang',
              docSearch: {
                  indexName: 'masstransit_io'
              }
          }
      }
  },

  compatibilityDate: '2024-07-28'
})

```

### File: doc\renovate.json
```json
{
    "extends": [
      "@nuxtjs"
    ],
    "lockFileMaintenance": {
      "enabled": true
    }
}

```

### File: doc\tailwind.config.js
```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.vue",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

```

### File: doc\tokens.config.ts
```ts
import { defineTheme } from 'pinceau'

export default defineTheme({
})

```

### File: doc\tsconfig.json
```json
{
  "extends": "./.nuxt/tsconfig.json",
  "compilerOptions": {
    "types": ["jest", "node"]
  }
}

```

### File: doc\vercel.json
```json
{
  "trailingSlash": false,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=60"
        },
        {
          "key": "CDN-Cache-Control",
          "value": "max-age=900"
        },
        {
          "key": "Vercel-CDN-Cache-Control",
          "value": "public, max-age=3600"
        }
      ]
    }
  ]
}

```

### File: src\NuGet.README.md
```md
# MassTransit

MassTransit provides a developer-focused, modern platform for creating distributed applications without complexity.

   - First class testing support
   - Write once, then deploy using RabbitMQ, Azure Service Bus, and Amazon SQS
   - Observability via Open Telemetry (OTEL)
   - Fully-supported, widely-adopted, a complete end-to-end solution

## Documentation

Get started by [reading through the documentation](https://masstransit-project.com/).

## Build Status

| Branch  |                                                                                              Status                                                                                              |
|---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| master  |  [![master](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml/badge.svg?branch=master&event=push)](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml)  |
| develop | [![develop](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml/badge.svg?branch=develop&event=push)](https://github.com/MassTransit/MassTransit/actions/workflows/build.yml) |

## MassTransit NuGet Packages

The following NuGet packages are the currently supported.

[![alt MassTransit](https://img.shields.io/nuget/v/MassTransit.svg "MassTransit")](https://nuget.org/packages/MassTransit/)

* [MassTransit](https://nuget.org/packages/MassTransit/)
* [MassTransit.Abstractions](https://www.nuget.org/packages/MassTransit.Abstractions/)

### Transports

* [MassTransit.ActiveMQ](https://nuget.org/packages/MassTransit.ActiveMQ/)
* [MassTransit.AmazonSQS](https://nuget.org/packages/MassTransit.AmazonSQS/)
* [MassTransit.Azure.ServiceBus.Core](https://nuget.org/packages/MassTransit.Azure.ServiceBus.Core/)
    * [MassTransit.WebJobs.ServiceBus](https://nuget.org/packages/MassTransit.WebJobs.ServiceBus/)
    * [MassTransit.WebJobs.EventHubs](https://nuget.org/packages/MassTransit.WebJobs.EventHubs/)
* [MassTransit.RabbitMQ](https://nuget.org/packages/MassTransit.RabbitMQ/)
* **Riders**
    * [MassTransit.EventHub](https://nuget.org/packages/MassTransit.EventHub/)
    * [MassTransit.Kafka](https://nuget.org/packages/MassTransit.Kafka/)

### Saga Persistence

* [MassTransit.Azure.Cosmos](https://nuget.org/packages/MassTransit.Azure.Cosmos/)
* [MassTransit.Azure.Cosmos.Table](https://nuget.org/packages/MassTransit.Azure.Cosmos.Table/)
* [MassTransit.DapperIntegration](https://nuget.org/packages/MassTransit.DapperIntegration/)
* [MassTransit.DynamoDb](https://nuget.org/packages/MassTransit.DynamoDb/)
* [MassTransit.EntityFramework](https://nuget.org/packages/MassTransit.EntityFramework/)
* [MassTransit.EntityFrameworkCore](https://nuget.org/packages/MassTransit.EntityFrameworkCore/)
* [MassTransit.Marten](https://nuget.org/packages/MassTransit.Marten/)
* [MassTransit.MongoDb](https://nuget.org/packages/MassTransit.MongoDb/)
* [MassTransit.NHibernate](https://nuget.org/packages/MassTransit.NHibernate/)
* [MassTransit.Redis](https://nuget.org/packages/MassTransit.Redis/)

### Message Data

* [MassTransit.Azure.Storage](https://nuget.org/packages/MassTransit.Azure.Storage/)

### Scheduling

* [MassTransit.Hangfire](https://nuget.org/packages/MassTransit.Hangfire/)
* [MassTransit.Quartz](https://nuget.org/packages/MassTransit.Quartz/)

### Interoperability

* [MassTransit.Interop.NServiceBus](https://nuget.org/packages/MassTransit.Interop.NServiceBus/)
* [MassTransit.Newtonsoft](https://nuget.org/packages/MassTransit.Newtonsoft/)

### Other

* [MassTransit.Analyzers](https://nuget.org/packages/MassTransit.Analyzers/)
* [MassTransit.SignalR](https://nuget.org/packages/MassTransit.SignalR/)
* [MassTransit.Prometheus](https://nuget.org/packages/MassTransit.Prometheus/)
* [MassTransit.StateMachineVisualizer](https://nuget.org/packages/MassTransit.StateMachineVisualizer/)
* [MassTransit.TestFramework](https://nuget.org/packages/MassTransit.TestFramework/)

## Deprecated Packages

The following packages from earlier versions of MassTransit are no longer supported.

* Automatonymous
* Automatonymous.NHibernate
* Automatonymous.Visualizer
* GreenPipes
* MassTransit.ApplicationInsights
* MassTransit.AspNetCore
* MassTransit.Autofac
* MassTransit.Automatonymous
* MassTransit.Automatonymous.Autofac
* MassTransit.Automatonymous.Extensions.DependencyInjection
* MassTransit.Automatonymous.Lamar
* MassTransit.Automatonymous.SimpleInjector
* MassTransit.Automatonymous.StructureMap
* MassTransit.Automatonymous.Windsor
* MassTransit.AzureServiceBus
* MassTransit.CastleWindsor
* MassTransit.Extensions.DependencyInjection
* MassTransit.Extensions.Logging
* MassTransit.Host
* MassTransit.Http
* MassTransit.Lamar
* MassTransit.Log4Net
* MassTransit.MSMQ
* MassTransit.Ninject
* MassTransit.NLog
* MassTransit.Platform.Abstractions
* MassTransit.Reactive
* MassTransit.SerilogIntegration
* MassTransit.SimpleInjector
* MassTransit.StructureMap
* MassTransit.StructureMapSigned
* MassTransit.Unity

## Discord 

Get help live at the MassTransit Discord server.

[![alt Join the conversation](https://img.shields.io/discord/682238261753675864.svg "Discord")](https://discord.gg/rNpQgYn)

## GitHub Issues

> Please do not open an issue on GitHub, unless you have spotted an actual bug in MassTransit. 

Use [GitHub Discussions](https://github.com/MassTransit/MassTransit/discussions) to ask questions, bring up ideas, or other general items. Issues are not the place for questions, and will either be converted to a discussion or closed.

```

### File: doc\content\0.index.md
```md
---
title: MassTransit
navigation: false
layout: page

---

::block-hero
---
cta:
  - Get Started
  - /introduction
secondary:
  - Get a License →
  - https://massient.com
snippet: dotnet add package MassTransit
---

#title
Enterprise Messaging for .NET

#description
MassTransit is the **trusted messaging framework** powering mission-critical applications in industries like **finance, logistics, government, retail, IoT, and more**. Built for scale, security, and reliability, MassTransit helps teams build **fast, fault-tolerant, and future-proof** distributed applications. Whether you're a CTO evaluating architecture options or a developer creating your first message consumer, MassTransit gives you everything you need.

#extra
  ::list{type="success"}
- **Battle-Tested** – Powering production workloads across finance, logistics, government, and more.  
- **Multi-Broker Support** – Unified abstraction over **RabbitMQ, Azure Service Bus, Amazon SQS, and SQL Transport**.  
- **Commercial Licensing** – MassTransit v9 is a commercial product with full support via [Massient](https://massient.com).  
- **Complete Framework** – Not just transport abstraction, but a full framework for **sagas, routing slips, and fault-tolerant workflows**.  
- **Cloud-Native Ready** – Seamlessly deploy across **Kubernetes, serverless, hybrid, and multi-cloud environments**. 
  ::
::

::card-grid
#title
Why MassTransit?

#default
    ::card
    #title
    Durable Messaging
    #description
    - Reliable message delivery with retries, redelivery, and outbox patterns.  
    - Dead letter queues and error handling built in.  
    - Transactional messaging ensures data consistency.  
    ::
    ::card
    #title
    Loosely Coupled Services
    #description
    - Publish/subscribe patterns that decouple producers from consumers.  
    - Message contracts define boundaries, not implementations.  
    - Evolve your system without breaking existing consumers.  
    ::
    ::card
    #title
    Workflow Orchestration
    #description
    - **Saga state machines** manage complex multi-step workflows.  
    - **Routing slips** orchestrate distributed business processes.  
    - Build resilient, long-running processes with built-in persistence.  
    ::
::

```

### File: doc\lib\content.test.ts
```ts
import { expect } from 'chai'
import {groupContent} from "./content";
import {ParsedContent} from "@nuxt/content/dist/runtime/types";

describe("a", () => {
    it("a", ()=>{
        const result = groupContent(items)

        expect(result.attributes.title).to.eql('Configuration')
        expect(result.attributes.icon).to.eql('icon-park-outline:mindmap-list')

        expect(result.pages.length).to.eql(2)
        expect(result.children.length).to.eql(5)
        const c = result.children[0]
        expect(c.attributes.title).to.eql('Transports')
        expect(c.pages.length).to.eql(8)

    })
})

const items : Omit<ParsedContent,'body'>[] = [
    {
        "_path": "/documentation/configuration/_dir",
        "_dir": "configuration",
        "_draft": false,
        "_partial": true,
        "_locale": "en",
        "title": "Configuration",
        "icon": "icon-park-outline:mindmap-list",
        "_id": "content:2.documentation:5.configuration:_dir.yml",
        "_type": "yaml",
        "_source": "content",
        "_file": "2.documentation/5.configuration/_dir.yml",
        "_extension": "yml"
    },
    {
        "_path": "/documentation/configuration",
        "_dir": "documentation",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Overview",
        "description": "Configure ALL THE THINGS",
        "toc": true,
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:4.scheduling.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/4.scheduling.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/_dir",
        "_dir": "transports",
        "_draft": false,
        "_partial": true,
        "_locale": "en",
        "title": "Transports",
        "navigation": {
            "redirect": "/documentation/configuration/transports/rabbitmq"
        },
        "_id": "content:2.documentation:5.configuration:1.transports:_dir.yml",
        "_type": "yaml",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/_dir.yml",
        "_extension": "yml"
    },
    {
        "_path": "/documentation/configuration/transports/rabbitmq",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "RabbitMQ",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:2.rabbitmq.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/2.rabbitmq.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/azure-service-bus",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Azure Service Bus",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:3.azure-service-bus.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/3.azure-service-bus.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/amazon-sqs",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Amazon SQS",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:4.amazon-sqs.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/4.amazon-sqs.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/activemq",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "ActiveMQ",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:5.activemq.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/5.activemq.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/kafka",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Kafka",
        "description": "Kafka is supported as a Rider, and supports consuming and producing messages from/to Kafka topics. The Confluent .NET client is used, and has been tested with the community edition (running in Docker).",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:10.kafka.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/10.kafka.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/azure-event-hub",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Azure Event Hub",
        "description": "Azure Event Hub is included as a Rider, and supports consuming and producing messages from/to Azure event hubs.",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:11.azure-event-hub.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/11.azure-event-hub.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/azure-functions",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Azure Functions",
        "description": "Azure Functions is a consumption-based compute solution that only runs code when there is work to be done. MassTransit supports Azure Service Bus and Azure Event Hubs when running as an Azure Function.",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:21.azure-functions.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/21.azure-functions.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/transports/aws-lambda",
        "_dir": "transports",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "AWS Lambda",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:1.transports:22.aws-lambda.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/1.transports/22.aws-lambda.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/_dir",
        "_dir": "persistence",
        "_draft": false,
        "_partial": true,
        "_locale": "en",
        "title": "Persistence",
        "_id": "content:2.documentation:5.configuration:2.persistence:_dir.yml",
        "_type": "yaml",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/_dir.yml",
        "_extension": "yaml"
    },
    {
        "_path": "/documentation/configuration/persistence/azure-cosmos",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Azure Cosmos DB",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:azure-cosmos.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/azure-cosmos.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/azure-service-bus",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Azure Service Bus",
        "description": "Azure Service Bus provides a feature called message sessions, to process multiple messages at once and to store some state on a temporary basis, which can be retrieved by some key.",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:azure-service-bus.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/azure-service-bus.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/azure-table",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Azure Table Storage",
        "description": "Azure Tables are exposed in two ways in Azure - via Storage accounts & via the premium offering within Cosmos DB APIs. This persistence supports both implementations and behind the curtains uses the Azure.Data.Tables library for communication.",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:azure-table.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/azure-table.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/dapper",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Dapper",
        "description": "MassTransit.Dapper",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:dapper.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/dapper.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/dynamodb",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "DynamoDb",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:dynamodb.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/dynamodb.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/entity-framework",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Entity Framework",
        "description": "MassTransit.EntityFrameworkCore",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:entity-framework.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/entity-framework.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/marten",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Marten",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:marten.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/marten.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/mongodb",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "MongoDB",
        "description": "MongoDB is easy to setup as a saga repository. MassTransit includes sensible defaults, and there is no need to explicitly map sagas.",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:mongodb.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/mongodb.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/nhibernate",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "NHibernate",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:nhibernate.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/nhibernate.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/persistence/redis",
        "_dir": "persistence",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Redis",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:2.persistence:redis.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/2.persistence/redis.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/middleware/_dir",
        "_dir": "middleware",
        "_draft": false,
        "_partial": true,
        "_locale": "en",
        "title": "Middleware",
        "_id": "content:2.documentation:5.configuration:3.middleware:_dir.yml",
        "_type": "yaml",
        "_source": "content",
        "_file": "2.documentation/5.configuration/3.middleware/_dir.yml",
        "_extension": "yml"
    },
    {
        "_path": "/documentation/configuration/middleware",
        "_dir": "configuration",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Overview",
        "description": "MassTransit is built using a network of pipes and filters to dispatch messages. A pipe is composed of a series of filters, each of which is a key atom and are described below.",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:3.middleware:4.scheduling.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/3.middleware/4.scheduling.md",
        "_extension": "md"
    },
    {
        "_path": "/documentation/configuration/middleware/filters",
        "_dir": "middleware",
        "_draft": false,
        "_partial": false,
        "_locale": "en",
        "_empty": false,
        "title": "Filters",
        "description": "",
        "_type": "markdown",
        "_id": "content:2.documentation:5.configuration:3.middleware:1.filters.md",
        "_source": "content",
        "_file": "2.documentation/5.configuration/3.middleware/1.filters.md",
        "_extension": "md"
    },
    {

... [TRUNCATED]
```

### File: doc\lib\content.ts
```ts
import {ParsedContent} from "@nuxt/content/dist/runtime/types";

export class ContentGroup {
    attributes: any;
    pages: Omit<ParsedContent,'body'>[];
    children: ContentGroup[];
    path: string;

    constructor(path: string) {
        this.path = path;
        this.attributes= {}
        this.pages = []
        this.children = []
    }

    addDirectory(dir: Omit<ParsedContent,'body'>) {
        const dirPath = dir._path?.replace('/_dir','')
        const cg = new ContentGroup(dirPath)
        cg.attributes.title = dir.title
        cg.attributes.icon = dir.icon
        cg.attributes.description = dir.description
        this.children.push(cg)
    }
    addPage(page: Omit<ParsedContent,'body'>) {
        const pagePath = page._path!
        const expectedDir = this.getDir(pagePath)
        if(this.path === expectedDir) {
            this.pages.push(page)
            return;
        }


        const dir = this.children.find(c => c.path === expectedDir)
        if(dir !== undefined)
            dir.pages.push(page)
    }

    private getDir(path:string) : string {
        return path.split('/').slice(0, -1).join('/')
    }

}

export function groupContent(items: Omit<ParsedContent,'body'>[]) : ContentGroup {
    const rootItem = items[0]
    const rootPath = rootItem._path?.replace('/_dir','')
    const result = new ContentGroup(rootPath)

    result.attributes.title = rootItem.title
    result.attributes.icon = rootItem.icon
    result.attributes.description = rootItem.description

    // pre-populate directory data
    items.slice(1).forEach(item => {
        if(item._path === undefined) return;

        if(item._path.endsWith('_dir')) {
            // we have a dir
            result.addDirectory(item)
        }

        if(item._id.includes('index')) {
            // this is the root page of the dir
            // result.addDirectory(item)
        }
    })

    items.slice(1)
        .filter(item => !item._path.endsWith('_dir'))
        .filter(item => !item._id.includes('index'))
        .forEach(item => {
            result.addPage(item)
        })

    return result;
}

function splitPath(path: string): string[] {
    return path.split('/')
}

```

### File: doc\plugins\vue-gtag.client.js
```js
import VueGtag from 'vue-gtag-next'
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(VueGtag, {
    property: {
      id: 'G-V4VZT979X2'
    }
  })
})
```

### File: doc\public\robots.txt
```txt

```

### File: doc\assets\css\main.css
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

```

### File: doc\content\samples\getting-started.md
```md
---
repo: "MassTransit/Sample-GettingStarted"
useTitle: false
youtube: https://www.youtube.com/watch?v=_dfEMm7rRrI
---

Getting started with MassTransit is fast and easy. This sample, which is part of the quick start guide, uses RabbitMQ with .NET 6. RabbitMQ must be installed, instructions for installing RabbitMQ are included in the [Quick Starts](/quick-starts/rabbitmq) section.


```

### File: doc\content\samples\job-consumer.md
```md
---
repo: "MassTransit/Sample-JobConsumers"
useTitle: false
youtube: abc
---

MassTransit includes a job service that keeps track of each job, assigns jobs to service instances, and schedules job retries when necessary. The job service uses three saga state machines and the default configuration uses an in-memory saga repository, which is not durable. When using job consumers for production use cases, configuring durable saga repositories is highly recommended to avoid possible message loss. Check out the sample project on GitHub, which includes the Entity Framework configuration for the job service state machines.

```

### File: doc\content\samples\sample-kafka.md
```md
---
repo: "MassTransit/Sample-Kafka"
useTitle: false
youtube: CJ_srcJiIKs
---

This sample shows how to use MassTransit with Kafka, including Confluent Cloud.

```

### File: doc\content\samples\sql-transport.md
```md
---
repo: "MassTransit/Sample-DbTransport"
useTitle: false
youtube: abc
---

Shows how to use the SQL Database Transport, including bus configuration, Entity Framework Core saga state machine persistence, and the transactional outbox. 

```

### File: doc\content\samples\web-application-factory.md
```md
---
repo: "MassTransit/Sample-WebApplicationFactory"
useTitle: false
youtube: Uzme7vInDz0
---

This sample shows how to use MassTransit's container-based test harness with the WebApplicationFactory, without requiring the application under test to know about the test harness.

```

### File: doc\server\middleware\redirects.ts
```ts
import {H3Event} from "h3";

const mapping: { [key: string]: string } = {
    '/advanced/middleware/circuit-breaker.html': '/documentation/configuration/middleware/filters',
    '/advanced/middleware/index.html': '/documentation/configuration/middleware',
    '/advanced/middleware/scoped.html': '/documentation/configuration/middleware/scoped',
    '/advanced/middleware/killswitch.html': '/documentation/configuration/middleware/filters',
    '/advanced/middleware/concurrency-limit.html': '/documentation/configuration/middleware/filters',
    '/advanced/middleware/transactions.html': '/documentation/configuration/middleware/transactions',
    '/advanced/middleware/custom.html': '/documentation/configuration/middleware/filters',
    '/advanced/middleware/receive.html': '/documentation/configuration/middleware/filters',
    '/advanced/middleware/rate-limiter.html': '/documentation/configuration/middleware/filters',
    '/advanced/middleware/latest.html': '/documentation/configuration/middleware/filters',
    '/advanced/middleware': '/documentation/configuration/middleware',

    '/advanced/topology/message.html': '/documentation/configuration/topology/message',
    '/advanced/topology/conventions.html': '/documentation/configuration/topology/conventions',
    '/advanced/topology/servicebus.html': '/documentation/concepts/messages',
    '/advanced/topology/index.html': '/documentation/configuration/topology',
    '/advanced/topology/publish.html': '/documentation/configuration/topology',
    '/advanced/topology/send.html': '/documentation/configuration/topology',
    '/advanced/topology/rabbitmq.html': '/documentation/concepts/messages',
    '/advanced/topology/deploy.html': '/documentation/configuration/topology/deploy',
    '/advanced/topology/consume.html': '/documentation/configuration/topology',

    '/advanced': '/documentation/concepts',
    '/advanced/index.html': '/documentation/concepts',

    '/advanced/courier': '/documentation/patterns/routing-slip',
    '/advanced/courier/activities.html': '/documentation/patterns/routing-slip#activities',
    '/advanced/courier/': '/documentation/patterns/routing-slip',
    '/advanced/courier/index.html': '/documentation/patterns/routing-slip',
    '/advanced/courier/builder.html': '/documentation/patterns/routing-slip#building',
    '/advanced/courier/subscriptions.html': '/documentation/patterns/routing-slip#subscriptions',
    '/advanced/courier/execute.html': '/documentation/patterns/routing-slip#executing',
    '/advanced/courier/events.html': '/documentation/patterns/routing-slip#routing-slip-events',

    '/advanced/scheduling/azure-sb-scheduler.html': '/documentation/configuration/scheduling',
    '/advanced/scheduling/redeliver.html': '/documentation/configuration/scheduling',
    '/advanced/scheduling': '/documentation/configuration/scheduling',
    '/advanced/scheduling/': '/documentation/configuration/scheduling',
    '/advanced/scheduling/index.html': '/documentation/configuration/scheduling',
    '/advanced/scheduling/scheduling-api.html': '/documentation/configuration/scheduling',
    '/advanced/scheduling/amazonsqs-scheduler.html': '/documentation/configuration/scheduling',
    '/advanced/scheduling/hangfire.html': '/documentation/configuration/scheduling',
    '/advanced/scheduling/activemq-delayed.html': '/documentation/configuration/scheduling',
    '/advanced/scheduling/rabbitmq-delayed.html': '/documentation/configuration/scheduling',

    '/advanced/signalr/quickstart.html': '/documentation/configuration/integrations/signalr',
    '/advanced/signalr': '/documentation/configuration/integrations/signalr',
    '/advanced/signalr/index.html': '/documentation/configuration/integrations/signalr',
    '/advanced/signalr/considerations.html': '/documentation/configuration/integrations/signalr',
    '/advanced/signalr/sample.html': '/documentation/configuration/integrations/signalr',
    '/advanced/signalr/hub_endpoints.html': '/documentation/configuration/integrations/signalr',
    '/advanced/signalr/interop.html': '/documentation/configuration/integrations/signalr',

    '/advanced/connect-endpoint.html': '/documentation/concepts/messages',
    '/advanced/batching.html': '/documentation/concepts/messages',
    '/advanced/job-consumers.html': '/documentation/patterns/job-consumers',
    '/advanced/monitoring/applications-insights.html': '/documentation/configuration/observability',
    '/advanced/monitoring/prometheus.html': '/documentation/configuration/observability',
    '/advanced/monitoring/diagnostic-source.html': '/documentation/configuration/observability',
    '/advanced/monitoring/perfcounters.html': '/documentation/configuration/observability',
    '/advanced/audit.html': '/documentation/concepts/messages',
    '/advanced/transactional-outbox.html': '/documentation/configuration/middleware/outbox',
    '/advanced/observers.html': '/documentation/configuration/observability',

    '/releases/v7.1.8.html': '/documentation/concepts/messages',
    '/releases/v7.1.4.html': '/documentation/concepts/messages',
    '/releases/index.html': '/documentation/concepts/messages',
    '/releases/v7.1.5.html': '/documentation/concepts/messages',
    '/releases/v7.2.0.html': '/documentation/concepts/messages',
    '/releases/v7.0.6.html': '/documentation/concepts/messages',
    '/releases/v7.0.7.html': '/documentation/concepts/messages',
    '/releases/v7.1.3.html': '/documentation/concepts/messages',
    '/releases/v7.0.4.html': '/documentation/concepts/messages',
    '/releases/v7.1.0.html': '/documentation/concepts/messages',
    '/releases/v7.1.1.html': '/documentation/concepts/messages',
    '/releases/v7.1.6.html': '/documentation/concepts/messages',
    '/releases/v7.2.3.html': '/documentation/concepts/messages',
    '/releases/v8.0.0.html': '/documentation/concepts/messages',
    '/releases/v7.1.7.html': '/documentation/concepts/messages',

    '/learn/videos.html': '/support/support-channels',
    '/learn/index.html': '/support/support-channels',
    '/learn/support.html': '/support',
    '/learn/analyzers.html': '/documentation/configuration/integrations/roslyn-analyzer',
    '/learn/loving-the-community.html': '/support/support-channels',
    '/learn/contributing.html': '/support/support-channels',
    '/learn/samples.html': '/support/samples',
    '/learn/training.html': '/support/training',

    '/index.html': '/',
    '/support.html': '/support',

    '/understand/index.html': '/documentation/concepts/messages',
    '/understand/key-ideas.html': '/documentation/concepts/messages',
    '/understand/under-the-hood.html': '/documentation/concepts/messages',
    '/understand/publishing.html': '/documentation/concepts/messages',
    '/understand/additions-to-transport.html': '/introduction',

    '/platform': '/documentation/concepts/messages',
    '/platform/index.html': '/documentation/concepts/messages',
    '/platform/configuration.html': '/documentation/concepts/messages',

    '/articles/durable-futures.html': '/documentation/patterns/durable-futures',

    '/articles/outbox.html': '/documentation/concepts/messages',
    '/articles/net5.html': '/documentation/concepts/messages',
    '/articles/mediator.html': '/documentation/concepts/messages',

    '/usage': '/documentation/concepts',

    '/usage/guidance.html': '/documentation/concepts/messages',
    '/usage/index.html': '/documentation/concepts/messages',
    '/usage/monitoring.html': '/documentation/concepts/messages',
    '/usage/correlation.html': '/documentation/concepts/messages',

    '/usage/transports': '/documentation/transports',
    '/usage/transports/in-memory.html': '/documentation/transports',
    '/usage/transports/grpc.html': '/documentation/transports',
    '/usage/transports/index.html': '/documentation/transports',
    '/usage/transports/activemq.html': '/documentation/transports',
    '/usage/transports/rabbitmq.html': '/documentation/transports/rabbitmq',
    '/usage/transports/azure-sb.html': '/documentation/transports/azure-service-bus',
    '/usage/transports/amazonsqs.html': '/documentation/transports/amazon-sqs',

    '/usage/message-data.html': '/documentation/patterns/claim-check',

    '/usage/configuration.html': '/documentation/configuration',

    '/usage/requests.html': '/documentation/concepts/messages',

    '/usage/faas': '/documentation/configuration/transports/azure-functions',
    '/usage/faas/aws-lambda.html': '/documentation/configuration/transports/aws-lambda',
    '/usage/faas/index.html': '/documentation/configuration',
    '/usage/faas/azure-functions.html': '/documentation/configuration/transports/azure-functions',
    '/usage/exceptions.html': '/documentation/concepts/exceptions',
    '/usage/templates.html': '/quick-starts/templates',

    '/usage/sagas': '/documentation/patterns/saga',
    '/usage/sagas/azure-table.html': '/documentation/configuration/persistence/azure-table',
    '/usage/sagas/persistence.html': '/documentation/patterns/saga/persistence',
    '/usage/sagas/quickstart.html': '/documentation/configuration/persistence/messages',
    '/usage/sagas/ef.html': '/documentation/configuration/persistence/entity-framework',
    '/usage/sagas/guidance.html': '/documentation/patterns/saga/guidance',
    '/usage/sagas/index.html': '/documentation/patterns/saga',
    '/usage/sagas/redis.html': '/documentation/configuration/persistence/redis',
    '/usage/sagas/cosmos.html': '/documentation/configuration/persistence/azure-cosmos',
    '/usage/sagas/automatonymous.html': '/documentation/patterns/saga/state-machine',
    '/usage/sagas/consumer-saga.html': '/documentation/patterns/saga/consumer-sagas',
    '/usage/sagas/dapper.html': '/documentation/configuration/persistence/dapper',
    '/usage/sagas/marten.html': '/documentation/configuration/persistence/marten',
    '/usage/sagas/mongodb.html': '/documentation/configuration/persistence/mongodb',
    '/usage/sagas/efcore.html': '/documentation/configuration/persistence/entity-framework',
    '/usage/sagas/session.html': '/documentation/configuration/persistence/azure-service-bus',
    '/usage/sagas/nhibernate.html': '/documentation/configuration/persistence/nhibernate',

    '/usage/audit/azuretable.html': '/documentation/concepts/messages',

    '/usage/messages.html': '/documentation/concepts/messages',

    '/usage/riders': '/documentation/concepts/riders',
    '/usage/riders/index.html': '/documentation/concepts/riders',
    '/usage/riders/kafka.html': '/documentation/transports/kafka',
    '/usage/riders/eventhub.html': '/documentation/configuration/transports/azure-event-hub',

    '/usage/containers/multibus.html': '/documentation/configuration/multibus',

    '/usage/containers': '/documentation/configuration',
    '/usage/containers/index.html': '/documentation/configuration',
    '/usage/containers/msdi.html': '/documentation/configuration',
    '/usage/containers/definitions.html': '/documentation/concepts/consumers#definitions',
    '/usage/containers/simpleinjector.html': '/documentation/configuration',
    '/MassTransit/usage/containers/autofac.html': '/documentation/configuration',
    '/usage/containers/autofac.html': '/documentation/configuration',
    '/usage/containers/castlewindsor.html': '/documentation/configuration',
    '/usage/containers/structuremap.html': '/documentation/configuration',

    '/usage/producers.html': '/documentation/concepts/producers',
    '/usage/testing.html': '/documentation/concepts/testing',
    '/usage/lifecycle-observers.html': '/documentation/configuration/observability',
    '/usage/observers.html': '/documentation/configuration/observability',
    '/usage/mediator.html': '/documentation/concepts/mediator',
    '/usage/consumers.html': '/documentation/concepts/consumers',
    '/usage/logging.html': '/documentation/configuration/integrations/logging',

    '/troubleshooting/common-gotchas.html': '/support/common-mistakes',
    '/troubleshooting/show-config.html': '/support/show-configuration',

    '/quick-starts/in-memory.html': '/quick-starts/in-memory',
    '/quick-starts/azure-service-bus.html': '/quick-starts/azure-service-bus',
    '/quick-starts/index.html': '/quick-starts',
    '/quick-starts/sqs.html': '/quick-starts/amazon-sqs',
    '/quick-starts/rabbitmq.html': '/quick-starts/rabbitmq',

    '/architecture/versioning.html': '/documentation/concepts/messages',
    '/architecture/packages.html': '/support/packages',
    '/architecture/green-cache.html': '/documentation/concepts/messages',
    '/architecture/nservicebus.html': '/documentation/configuration/integrations/nsb',
    '/architecture/interoperability.html': '/documentation/configuration/serialization',
    '/advanced/interoperability.html': '/documentation/configuration/serialization',
    '/architecture/history.html': '/documentation/concepts/messages',
    '/architecture/encrypted-messages.html': '/documentation/concepts/messages',
    '/architecture/newid.html': '/documentation/patterns/newid',

    '/getting-started': '/quick-starts',
    '/getting-started/upgrade-v6.html': '/support/upgrade',
    '/getting-started/index.html': '/documentation/concepts/messages',
    '/getting-started/live-coding.html': '/documentation/concepts/messages',
    '/discord.html': '/support/support-channels',
    '/obsolete': '/documentation/configuration/obsolete',

    '/documentation/configuration/integrations/serialization': '/documentation/configuration/serialization',
    '/documentation/patterns/routing-slip': '/documentation/concepts/routing-slips',
    '/documentation/patterns/routing-slip/configuration': '/documentation/concepts/routing-slips'
}

// flip the map, so we ignore good routes
const reverseMapping = Object.assign({}, ...Object.entries(mapping).map(([k, v]) => ({[v]: k})))


export default defineEventHandler((evt: H3Event) => {
    let path = evt.node.req.url || ''

    // good endpoint, bail
    if (reverseMapping[path]) return;

    if (path.startsWith('/MassTransit/')) {
        path = path.replace('/MassTransit', '')
    }

    let dest = mapping[path]

    // try looking for it with html
    if (dest === undefined) {
        dest = mapping[path + '.html']
    }

    // if still undefined, but path ends with .md
    if (dest === undefined && path.endsWith('.md')) {
        // swap .md for .html
        path = path.replace('.md', '.html')
        dest = mapping[path]
    }

    if (dest) {
        sendRedirect(evt, dest, 302)
            .then(() => {
            })
    }
})

```

