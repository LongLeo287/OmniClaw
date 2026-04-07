---
id: nservicebus
type: knowledge
owner: OA_Triage
---
# nservicebus
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
## About NServiceBus
NServiceBus is part of the [Particular Service Platform](https://particular.net/service-platform), which contains tools to build, monitor, and debug distributed systems.

With NServiceBus, you can:

- Focus on business logic, not on plumbing or infrastructure code 
- Orchestrate long-running business processes with sagas
- Run on-premises, in the cloud, in containers, or serverless
- Monitor and respond to failures using included platform tooling
- Observe system performance using Open Telemetry integration

NServiceBus includes:

- Support for messages queues using Azure Service Bus, Azure Storage Queues, Amazon SQS/SNS, RabbitMQ, and Microsoft SQL Server
- Support for storing data in Microsoft SQL Server, MySQL, PostgreSQL, Oracle, Azure Cosmos DB, Azure Table Storage, Amazon DynamoDB, MongoDB, and RavenDB
- 24x7 professional support from a team of dedicated engineers located around the world

## Getting started

- Visit the [NServiceBus Quick Start](https://docs.particular.net/tutorials/quickstart/) to learn how NServiceBus helps you build better software systems.
- Visit the [NServiceBus step-by-step tutorial](https://docs.particular.net/tutorials/nservicebus-step-by-step/) to learn how to build NServiceBus systems, including how to send commands, publish events, manage multiple message endpoints, and retry failed messages.
- Install the [ParticularTemplates NuGet package](https://www.nuget.org/packages/ParticularTemplates) to get NServiceBus templates to bootstrap projects using either `dotnet new` or in Visual Studio.
- Check out our other [tutorials](https://docs.particular.net/tutorials/) and [samples](https://docs.particular.net/samples/).
- Get [help with a proof-of-concept](https://particular.net/proof-of-concept).

## Packages

Find links to [all our NuGet packages](https://docs.particular.net/nservicebus/platform-nuget-packages) in our documentation.

## Support

- Browse our [documentation](https://docs.particular.net).
- Reach out to the [ParticularDiscussion](https://discuss.particular.net/) community.
- [Contact us](https://particular.net/support) to discuss your support requirements.

## Building

To build NServiceBus, open `NServiceBus.sln` in Visual Studio and build the solution.

You'll find the built assemblies in /binaries.

If you see the build failing, check that you haven't put the source of NServiceBus in a deep subdirectory since long path names (greater than 248 characters) aren't supported by MSBuild.

## Licensing

### NServiceBus

NServiceBus is licensed under the RPL 1.5 license. More details can be found [here](LICENSE.md).

### [net-object-deep-copy](https://github.com/Burtsev-Alexey/net-object-deep-copy)

net-object-deep-copy is licensed under the MIT license as described [here](https://github.com/Burtsev-Alexey/net-object-deep-copy/blob/master/README).

net-object-deep-copy sources are compiled into the NServiceBus distribution as allowed under the license terms found [here](https://github.com/Burtsev-Alexey/net-object-deep-copy/blob/master/README).

### [FastExpressionCompiler](https://github.com/dadhi/FastExpressionCompiler)

FastExpressionCompiler is licensed under the MIT license as described [here](https://github.com/dadhi/FastExpressionCompiler/blob/master/LICENSE).

FastExpressionCompiler sources are compiled into the NServiceBus distribution as allowed under the license terms found [here](https://github.com/dadhi/FastExpressionCompiler/blob/master/LICENSE).

```

### File: CONTRIBUTING.md
```md
For information on contributing, see https://docs.particular.net/platform/contributing.

```

### File: global.json
```json
{
  "sdk": {
    "version": "10.0.0",
    "allowPrerelease": false,
    "rollForward": "latestFeature"
  }
}

```

### File: LICENSE.md
```md
By accessing code under the [Particular Software GitHub Organization](https://github.com/Particular) (Particular Software) here, you are agreeing to the following licensing terms.
If you do not agree to these terms, do not access Particular Software code.

Your license to Particular Software source code and/or binaries is governed by the Reciprocal Public License 1.5 (RPL1.5) license as described here: 

https://opensource.org/license/rpl-1-5/

If you do not wish to release the source of software you build using Particular Software source code and/or binaries under the terms above, you may use Particular Software source code and/or binaries under the License Agreement described here:

https://particular.net/LicenseAgreement

```

### File: Package-README.md
```md
## About this package

This NuGet package is part of the [Particular Service Platform](https://particular.net/service-platform), which includes [NServiceBus](https://particular.net/nservicebus) and tools to build, monitor, and debug distributed systems.

Click the **Project website** link in the NuGet sidebar to access specific documentation for this package.

## About NServiceBus

With NServiceBus, you can:

- Focus on business logic, not on plumbing or infrastructure code 
- Orchestrate long-running business processes with sagas
- Run on-premises, in the cloud, in containers, or serverless
- Monitor and respond to failures using included platform tooling
- Observe system performance using Open Telemetry integration

NServiceBus includes:

- Support for messages queues using Azure Service Bus, Azure Storage Queues, Amazon SQS/SNS, RabbitMQ, and Microsoft SQL Server
- Support for storing data in Microsoft SQL Server, MySQL, PostgreSQL, Oracle, Azure Cosmos DB, Azure Table Storage, Amazon DynamoDB, MongoDB, and RavenDB
- 24x7 professional support from a team of dedicated engineers located around the world

## Getting started

- Visit the [NServiceBus Quick Start](https://docs.particular.net/tutorials/quickstart/) to learn how NServiceBus helps you build better software systems.
- Visit the [NServiceBus step-by-step tutorial](https://docs.particular.net/tutorials/nservicebus-step-by-step/) to learn how to build NServiceBus systems, including how to send commands, publish events, manage multiple message endpoints, and retry failed messages.
- Install the [ParticularTemplates NuGet package](https://www.nuget.org/packages/ParticularTemplates) to get NServiceBus templates to bootstrap projects using either `dotnet new` or in Visual Studio.
- Check out our other [tutorials](https://docs.particular.net/tutorials/) and [samples](https://docs.particular.net/samples/).
- Get [help with a proof-of-concept](https://particular.net/proof-of-concept).

## Packages

Find links to [all our NuGet packages](https://docs.particular.net/nservicebus/platform-nuget-packages) in our documentation.

## Support

- Browse our [documentation](https://docs.particular.net).
- Reach out to the [ParticularDiscussion](https://discuss.particular.net/) community.
- [Contact us](https://particular.net/support) to discuss your support requirements.

```

### File: SECURITY.md
```md
# Security Policy

Particular Software takes security issues very seriously. We appreciate your efforts to uncover bugs in our software. 

## Reporting a Vulnerability

Vulnerabilities can be reported by [submitting an issue](https://github.com/Particular/NServiceBus/security/advisories/new) through the security tab on our NServiceBus repository. 

```

### File: THIRD-PARTY-NOTICES.txt
```txt
License notice for net-object-deep-copy
---------------------------------------

https://github.com/Burtsev-Alexey/net-object-deep-copy/blob/master/README

Source code is released under the MIT license.

The MIT License (MIT)
Copyright (c) 2014 Burtsev Alexey

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

License notice for FastExpressionCompiler
-----------------------------------------

https://github.com/dadhi/FastExpressionCompiler/blob/master/LICENSE

The MIT License (MIT)

Copyright (c) 2016-2023 Maksim Volkau

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

### File: .github\SUPPORT.md
```md
# Looking for Support

Check out our [support options](https://particular.net/support).
```

