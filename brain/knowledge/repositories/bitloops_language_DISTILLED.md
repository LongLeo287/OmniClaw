---
id: repo-fetched-bitloops-language-140948
type: knowledge
owner: OA
registered_at: 2026-04-05T03:55:02.386373
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bitloops-language_140948

## Assimilation Report
Auto-cloned repository: FETCHED_bitloops-language_140948

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![Bitloops](https://storage.googleapis.com/bitloops-github-assets/github-readme-image.png)

<p align="center">
  <a href="https://bitloops.com/docs/bitloops-language/category/quick-start">Quick Start</a> |
  <a href="https://github.com/bitloops/bitloops-language#-what-are-the-benefits-of-using-bitloops-language">Benefits</a> |
  <a href="https://github.com/bitloops/bitloops-language#%EF%B8%8F-why-build-the-bitloops-language">Why?</a> |
  <a href="https://github.com/bitloops/bitloops-language#-language-goals">Goals</a> |
  <a href="https://github.com/bitloops/bitloops-language#-project-status">Project Status</a> |
  <a href="https://discord.gg/vj8EdZx8gK">Discord</a> |
  <a href="https://github.com/bitloops/bitloops-language/discussions">GitHub Discussions</a> |
  <a href="https://github.com/bitloops/bitloops-language/issues">GitHub Issues</a> |
  <a href="https://github.com/bitloops/bitloops-language/blob/main/CONTRIBUTING.md">Contributing</a>
</p>

## 🚀 Build great modular monoliths or microservices faster, much faster

Bitloops Language (BL) is a high-productivity, domain specific language (DSL) that helps you focus on the business logic of your application which is what really matters.

It incorporates software development best practices and design methodologies such as [DDD](https://bitloops.com/docs/bitloops-language/learning/domain-driven-design), [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) and [Layered/Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/). 

The Bitloops Language guides and empowers any software developer to write clean code and build high-quality & well designed software. This is particularly relevant for server application software that has complex, and frequently changing business requirements. With BL, developers can build software using principles such as separation of concerns, loose coupling, high cohesion and command query responsibility segregation (CQRS), which ensure systems are easier to understand, maintain and change. 

With Bitloops Language, developers are able to:
1. **Write clean code** in an intuitive and structured approach
2. Follow **best practices** to ensure the code and software can be easily understood by other developers
3. Create objects with **high cohesion and loose coupling** between each other
4. **Separate the busienss logic** from the **technical aspects** which leads to more **robust and flexible systems**
5. **Focus on the core domain** or problem, and not worry about boilerplate code and implementation details

In essence, software developers can focus on what they do best: **solving problems!** With the Bitloops Language developers write code that will allow other developers (and even themselves after 6 months) to easily understand and build on top of that code.  

<!--
Part of the Bitloops Language project, under the GPL-3.0 license
See /LICENSE for license information.
SPDX-License-Identifier: GPL-3.0-only
The GPL-3.0 license does not cover the use of Bitloops trademarks and logos
-->

&nbsp; 

> ⚠️ Please keep in mind that the Bitloops Language is in its early stages
> and under very active development. Expect bugs and limitations.
> Any backward compatibility is not guaranteed before reaching v1.0.0.

&nbsp; 

## 👨‍💻 Quick Start

The best and fastest way to understand how the Bitloops Language helps you write clean code and great software is to follow the instructions below. With this tutorial, you will run and execute a Bitloops ToDo App, learn how Bitloops works, and see the output files in TypeScript and appreciate how the Bitloops Language works. 

If you face any issues (especially with Windows) check the [Common Issues](#common-issues) Section below.

### 1 - Install the Transpiler
Bitloops still hasn't created binaries, so the best way to install and run the transpiler is to install the Bitloops Language CLI as a global npm package. Copy the following and run it in your IDE:

```console
npm install -g @bitloops/bitloops-language-cli
```

Alternatively, you can use yarn: 

```console
yarn global add @bitloops/bitloops-language-cli
```

### 2 - Clone the ToDo App example repo
The Bitloops [ToDo App](https://github.com/bitloops/bitloops-language/tree/main/examples/todo/bl-source) is readily available for cloning. You can extract the files following the link or clone it using the command below:

  ```console
  git clone https://github.com/bitloops/bitloops-language.git
  ```

### 3 - Run the Bitloops Transpiler
The next step is to transpile the ToDo App code from Bitloops Language Code into TypeScript code. Transpile comes from the word Transcompile, and means the translation of code from one programming language to another. 

macOS / Linux
  ```console
  bl transpile -s bitloops-language/examples/todo/bl-source/ -t output
  ```
Windows
  ```console
  bl transpile -s bitloops-language\examples\todo\bl-source\ -t output
  ```
or
  ```console
  bitloops-language transpile
  ```

That's it! You can now run the following to see how many lines of code you saved yourself (spoiler alert: 77% or 2141 LoC!)
  ```console
  bl analyze-lines -bl bitloops-language\examples\todo\bl-source -ts ./output
  ```

Ok now you have all your business logic beautifully transpiled into well structured TypeScript code 🎉🎉🎉! 

## BUT wait! What about the server and all the infrastructure code? How am I supposed to run this? 

The scope of the Bitloops Language ends here but using Bitloops you can automatically generate everything else using Bitloops magic and AI! Bitloops will generate for you a Nest.js project and all the required infrastructure (gRPC or REST controllers, repository adapters for PostgreSQL or Mongo etc.) as well as docker or K8s files to deploy your system. To learn more about the automatic Bitloops process [click here].

Alternatively, you are free to use any framework you like or just an Express server or Fastify server etc.

----

## Common Issues

- In Windows, if you are (still) using PowerShell, you will probably come across the error "running scripts is disabled on this system". To fix this, you can do the following:
1. Open PowerShell with Run as Administrator (right click on the icon and select the option from the menu).
2. Run the following command in PowerShell
```console
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```
3. Type Y and press Enter.

----

## 👏 What are the benefits of using Bitloops Language?

* Software you'll be proud of! Well designed and written, easy to understand and follow!
* High productivity by focusing on the core domain/problem, having less boilerplate code to build, manage and debug and more quickly being able to develop new features 
* Easy to learn and intuitive syntax 
* Learn about key software development best practices, patterns and methodologies such as [Domain-Driven Design (DDD)](https://bitloops.com/docs/bitloops-language/learning/domain-driven-design), [Behavior-Driven Development (BDD)](https://en.wikipedia.org/wiki/Behavior-driven_development), [Test-Driven Development (TDD)](http://agiledata.org/essays/tdd.html) and [Layered / Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/).
* Testing is treated as a 1st class citizen in the software development process
* Switch between Modular Monolith or Microservices architecture within minutes as all messages are moved through either in-memory or distributed message buses depending on your deployment choice
* Significantly reduce the amount of boilerplate code you need to write, maintain and debug
* Improved alignment between business and engineering with a natural ubiquitous language
* Ability to transpiles to widely used programming languages for maximum compatibility with existing code (currently [TypeScript](https://github.com/microsoft/TypeScript) support, Kotlin, C#, Go, Java, C++ or maybe even Rust or [Carbon](https://github.com/carbon-language/carbon-lang) to follow in the future)

## 🤷‍♀️ Why build the Bitloops Language?

There are numerous great programming languages out there with massive and growing
codebases and investments. However, the most common problem faced by organizations
that build and maintain systems, with teams of developers working on them, is
good architecture and design of an interconnected system of services; 

Designing a complex system so that it can last through time and will allow developers (existing and new joiners) to work on its codebase with steady (or hopefully) increasing productivity is very difficult. 

Good testing is an additional major requirement of long lasting products which is also made possible by good architecture and design. Unfortunately, there aren't enough knowledgeable and experienced senior
engineers around the world to build and maintain great systems for all who need them.
Even when a company is lucky enough to have some, it is unable to hire more junior engineers than the senior ones can review their work and guide in order to make sure the system does not degrade over time due to bad design decisions.

The Bitloops Language is the first programming language that aims to address these issues
by making it much easier to adopt important software engineering principles and patterns
such as [Domain-Driven Design](https://bitloops.com/docs/bitloops-language/learning/domain-driven-design) and Behavior-Driven Development, without requiring many years
of experience to do so successfully. As a result, the work of senior engineers can be further
leveraged and the contributions of junior engineers significantly boosted.


## 🥅 Language Goals

Every software engineer has a common goal: we want to write better code and build better software, and we want to do this faster! 

However, this can only be achieved with significant and continuous dedication, learning and experience, which takes a lot of time. Bitloops wants to significantly reduce the time it takes a developer to start building high-quality software, and we have built the Bitloops Language that already incorporates many of the software development best practices and design methodologies. 

Ultimately, BL's goals are to:

* Put the focus on the domain and you business logic and automate everything else as much as possible
* Delay infrastructure work and decisions as much as possible as these are implementation details
* Increase developer productivity significantly, not only at the start of a project, but for the entire lifecycle!
* Reduce the time and cost to build new features and products, even on large / complex projects
* Reduce the learning curve (specifically of DDD, BDD and Layered/Hexagonal Architecture) needed to build and maintain great software
* Empower many more software developers to learn & adopt these important principles and best practices
* Reduce the dependency on developer discipline during the code development process, with a structured process
* Make testing a more integral, collaborative, useful, and fun process
* Make domain logic timeless as well as platform & language independent
* Eliminate the need for boilerplate code & enable the reuse of existing packages writen in any language
* Empower software engineers to postpone the need for a microservices architecture until it is strictly needed from a infrastructure perspective to better manage computing and engineering resources (reduce intial costs! 💰💰💰) 
* Allow systems to be converted from a modular monolith to a microservices architecture in hours, not months

The Bitloops Language aims to define and retain a simplistic syntax that will be as close to human
language and business logic as possible that will become timeless, helping adopt and use a ubiquitous
language within each module or bounded context. It is then BL's job to transpile into modern and up-to-date syntax of your target language.

Making the Bitloops Language a transpiled language was a core decision to achieve exactly this. By allowing oraganisations to write their business logic in a timeless language that can be transpiled to powerful but also changing target languages without burdening the users of the Bitloops Language with this task. The Bitloops Language will make sure it transpiles to optimized code of relevant, up-to-date, and right-for-the-task languages.

## 📌 Project status

The Bitloops Language is currently in early stages. Its transpiler has been created as a proof of concept and is not meant to cover the full range of developer creative code writing at this stage.

We want to better understand whether we can build a language that meets your needs, and whether we can
gather a critical mass of interest within the DDD community and outside of it.

There are many things we want to add in the future including

- [X] CQRS support
- [ ] Event Sourcing support
- [ ] Kotlin target language
- [ ] C# target language
- [ ] Golang target language
- [ ] And many more...

If you're interested in contributing, we would love your help!

----

## 🏗 Bitloops -> TypeScript Transpilation

If you are already aware of the DDD concepts (Aggregates, Value Objects, Use Cases, Controller, etc.) and know how to code in any modern programming language, it should be really easy to pick up the Bitloops Language.
It is built out of a consistent set of language constructs that should feel familiar and be easy to read and understand.

While Bitloops is an Object Oriented Language, it doesn't have a generic class. Specific Bitloops classes are build-in as follows: ValueObject, Entity, Root Entity, Command, CommandHandler, Query, QueryHandler, DTO, Props, OK, ApplicationError, DomainError, Error etc.

Bitloops Language code like this (11 lines):

```node
// Bitloops Language:
Rule TitleOutOfBoundsRule(title: string) throws DomainErrors.TitleOutOfBoundsError {
  isBrokenIf(title.length > 150 OR title.length < 4);
}

Props TitleProps {
  string title;
}

ValueObject TitleVO {
  constructor(props: TitleProps): (OK(TitleVO), Errors(DomainErrors.TitleOutOfBoundsError)) {
    applyRules(TitleOutOfBoundsRule(props.title));
  }
}
```

transpiles to this TypeScript code (28 lines):

```node
// TypeScript:
import { Domain, Either, ok, fail } from '@bitloops/bl-boilerplate-core';
import { DomainErrors } from './errors';

export class TitleOutOfBoundsRule implements Domain.IRule {
  constructor(private title: string) {}

  public Error = new DomainErrors.TitleOutOfBounds(this.title);

  public isBrokenIf(): boolean {
    return this.title.length > 150 || this.title.length < 4;
  }
}
                                                            
export namespace Rules {
    export class TitleOutOfBounds extends TitleOutOfBoundsRule {}                                             
}

interface TitleProps {
  title: string;
}

export class TitleVO extends Domain.ValueObject<TitleProps> {
  get title(): string {
    return this.props.title;
  }

  private constructor(props: TitleProps) {
    super(props);
  }

  public static create(props: TitleProps): Either<TitleVO, DomainEr
... [TRUNCATED]
```

### File: examples\README.md
```md
# I. Introduction

Building complex software is really hard, and we learnt the hard way how important it is to design your software correctly from the beginning! 

There is plenty of information out there on how to build resilient and maintainable software, but the difficulty is actually implementing it. So we went ahead and built a comprehensive example we wish we had when we started learning these concepts and technologies. 

Our team has put a lot of effort into creating a clean, and modular code-base that comes as close as possible to production ready code, aiming to provide valuable insights into advanced software architecture concepts. 
 
### Overview
The objective of this project is to provide you a reference implementation on how to design and create maintainable and flexible software applications.

The code is written using Typescript and NodeJS, using the NEST framework, however, the concepts and patterns used are not bound to any specific technologies.

The project includes an over-engineered ToDo app that includes the patterns and principles that are necessary if you want your code to be easy to change, resilient and easy to maintain. Below we provide detailed instructions on how to run it

In addition, you will learn a great deal about software design and architecture patterns and principles such as: 
- Hexagonal Architecture (or Ports and adapters)
- Domain Driven Design (DDD) and its tactical patterns
- Behaviour Driven Development (BDD)
- Event Driven Architecture (EDA) 
- Command and Query Responsibility Segregation (CQRS)
- Eventual consistency
- Event Storming

There are many ways to implement these, so we're eager to get your feedback and open to answer any questions you may have. Join our [Discord](https://discord.com/invite/vj8EdZx8gK) channel if you'd like to exchange some ideas on software design & development or if you have any questions. 

### Todo application business requirements

The todo application, is basically a simple todo application, with some tweaks.

The users should be able to register to the todo app. After they register, they should be able to login. 
After logging in, they should be able to add todos, to complete a todo, to uncomplete a todo (in case they made it complete accidentally), as well as modify the todo title. In the whole process they should be able to view his todos.

When a todo is completed, if this is the first completed todo, an email should be sent to the user to congratulate him for completing his first todo. This operation has to do mostly with the needs marketing team.

# II. Technologies and Technical Features 


## Technical Features 
<p align="left" style="margin-bottom: 0px !important;">
  <img width="400" src="https://storage.googleapis.com/bitloops-github-assets/jaeger_small.png" alt="Jaeger" align="center">
</p>

* **Observability**
* **Realtime client events**
* **Logging**
* **Tracing**: Tracks requests that span through multiple modules/microservices
* **Easy switching between modular monolith and microservices**
* **Authentication**
* **Authorization** (Even at the repository level)
* **Automatic JWT renewal**
* **gRPC query caching**
* **Automatic client code generation using gRPC**

## Technologies Used - Overview
Here are listed some of the specific technologies used for the implementation of the project:
* **Authentication**: [JSON Web Tokens - JWT](https://jwt.io/)
* **Databases - Persistence**: [MongoDB](https://www.mongodb.com/), [PostgeSQL](https://www.postgresql.org/)
* **Testing**: [JEST](https://jestjs.io/)
* **External Communication Protocols**: [REST](https://en.wikipedia.org/wiki/Representational_state_transfer), [gRPC](https://grpc.io/)
* **Frameworks**: [ΝestJS](https://nestjs.com/)
* **PubSub technology**: [NATS](https://nats.io/)
* **Message Streaming Technology**: [JetStream](https://docs.nats.io/nats-concepts/jetstream) *by NATS*
* **Container Technology**: [Docker](https://www.docker.com/)
* **Tracing-Observability**: [Jaeger](https://www.jaegertracing.io/), [Grafana](https://grafana.com/)
* **Metrics**: [Prometheus](https://prometheus.io/)


# III. Quick start - running the ToDo App

## Prerequisites
In order to run the application the following should have been installed on your local machine:

* **Docker** should be installed ([link](https://docs.docker.com/engine/install/))
* **docker-compose** should be installed, if your docker installation does not install it automatically ([link](https://docs.docker.com/compose/install/))

## Running the app
In order to run the application you need to follow the steps below:
* Run `git clone git@github.com:bitloops/bitloops-language.git`
* Navigate  to the folder `cd bitloops-language/examples/todo/ts-target`
* Run `docker-compose up` from the terminal inside the project **in order to download and run the necessary containers**.

Then the ReactJS front-end application will be visible at: `http://localhost:3000`.

<p align="center" style="margin-bottom: 0px !important;">
  <img width="400" src="https://storage.googleapis.com/bitloops-github-assets/todo-frontend.png" alt="Frontend application" align="center">
</p>

<p align="center">
Frontend React JS application
</p>

# IV. Todo App Event Storming

We have chosen the [Event storming](https://www.eventstorming.com/) technique to document the functionality and business logic of the todo application.

In general, [Event storming](https://www.eventstorming.com/) is a **collaborating modelling technique** used to model complex domains, in order to align the software produced with the actual business logic. It matches perfectly with [Domain Driven Design (DDD)](https://bitloops.com/docs/bitloops-language/learning/software-design/domain-driven-design) as well as [Event Driven Architecture (EDA)](https://bitloops.com/docs/bitloops-language/learning/software-architecture/event-driven-architecture). 

If you want to know more for this technique, you can check the **Theoretical Review** at the end.

<p align="center" style="margin-bottom: 0px !important;">
  <img width="900" src="https://storage.googleapis.com/bitloops-github-assets/Todo%20event%20stroming.png" alt="Todo Event Storming" align="center">
</p>

As you can see after the collaborative discovery, we have identified the following **bounded contexts**:

* **IAM**: Has todo with the user registration and log in.
*  **Todo**: This is the **core subdomain** of our application (see [DDD](https://bitloops.com/docs/bitloops-language/learning/software-design/domain-driven-design))
*  **Marketing**: This is a **supporting subdomain** (see [DDD](https://bitloops.com/docs/bitloops-language/learning/software-design/domain-driven-design)) of our Todo application. 

In the process we have further split some bounded contexts (linguistic boundary), to more fine grained modules.

The processes of the system as were discovered are the following:

* **User Log In process** (IAM Bounded Context)
* **User registration process** (IAM Bounded Context)
* **Todo process** (Todo Bounded Context)
* **Onboarding process** (Marketing Bounded Context)

## Todo App Event Storming Observations

Some parts of the system need to have information which is located in other parts of the system. 

More specifically, the Marketing bounded context, **needs to know when a todo is completed** and run its business logic to send an email when the first todo is completed.

Moreover the Marketing Bounded contexts **needs to have information concerning the email** of each specific user, in order to be able to send an email.

The problem in this case is that the email information belongs to the IAM bounded context. So in order for the marketing bounded context to have the knowledge of the specific users's email, either it can make a sync request to the IAM bounded context, or it can listen to integration events from the IAM bounded context, in order to hold a local email information (via [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)).

In this project the decision was to keep a local repository in the Marketing bounded context, of the users and their emails, updated by listening to integration events from the IAM bounded contexts (**user registered** and **user email changed**). 

# V. Running in development mode

### Prerequisites
In order to run the application the following should have been installed on your local machine:

* **NodeJS** should be installed ([link](https://nodejs.dev/en/learn/how-to-install-nodejs/))
* **Docker** should be installed ([link](https://docs.docker.com/engine/install/))
* **docker-compose** should be installed, if your docker installation does not install it automatically ([link](https://docs.docker.com/compose/install/))
* **npm** and or **yarn** should be installed ([npm link](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), [yarn link](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable))

### Running the app

After all the necessary have been installed on your local machine, you should follow the **steps** mentioned below to run the application:

* Run `git clone git@github.com:bitloops/bitloops-language.git`
* Navigate  to the folder `cd bitloops-language/examples/todo/ts-target`
* Run `yarn install` (if you are using yarn) or `npm install`, from the terminal inside the project **to install the necessary packages**.
* **Start docker on your machine**.
* Run `docker-compose up` from the terminal inside the project **in order to download and run the necessary containers**.
* Create a `.development.env` file inside the root project and copy and paste the contents of the `.template-env`, which is located in the root of the project inside it.
* Run `yarn start:dev` or `npm start:dev` to start the server.

### Test the application is running

In order to test the application is running we could use a client  
The application is using **REST** for the authentication part and **gRPC** for the Todo part.

Those tools could be helpful in the development process as well.

#### Postman

So we recommend to test the application with a client tool that supports both. Such tool could be [Postman](https://www.postman.com/product/what-is-postman/).

You may find tutorials on how to use **Postman** for REST and gRPC requests below:

* REST ([link](https://hevodata.com/learn/postman-rest-client/))
* gRPC ([link](https://learning.postman.com/docs/sending-requests/grpc/first-grpc-request/))

To just test the app is app and running you can just invoke `http://localhost:8082` URI with Post request as shown in the picture below:
</br>
</br>

<p align="center" style="margin-bottom: 0px !important;">
  <img width="900" src="https://storage.googleapis.com/bitloops-github-assets/app-testing-confirmation.png" alt="App Running Confirmation" align="center">
</p>

<p align="center">
The server should respond with the message shown in the picture
</p>


#### cURL (only for initial testing) 

A faster way to test the app works is to use **[cURL](https://curl.se/)**. In most cases cURL is already installed in your operating system. If not you can download **cURL** [here](https://curl.se/download.html).

To just test the app is app and running you can just run the following command on terminal:

```curl http://localhost:8082/```

The server should respond (in the terminal) with: 
```{"statusCode":404,"message":"Cannot GET /auth/register","error":"Not Found"}```


### Running the application tests

In order to run the tests of the application run the following on the terminal:

`yarn test` or `npm test`.

## B. Understanding the project structure

The main project structure is located at the `/src` folder. 
The starting point for the whole application is the `src/main.ts` file.


<p align="center" style="margin-bottom: 0px !important;">
  <img width="500" src="https://storage.googleapis.com/bitloops-github-assets/project-structure.png" alt="Project Structure" align="center">
</p>

<p align="center">
Project Structure Overview
</p>

The main folders are the following:

* api
* bounded-contexts
* config
* lib
* proto

### API Folder

The api folder contains the **presentation layer** of the application (driving adapters of the infrastructure layer of the [Hexagonal Architecture](https://bitloops.com/docs/bitloops-language/learning/Software%20Architecture/hexagonal-architecture)), containing the **authentication controllers** (REST) as well as the **todo controllers** (gRPC).

It also contains the [Data Transfer Objects (DTOs)](https://en.wikipedia.org/wiki/Data_transfer_object) for those controllers.

The main operation of the **presentation layer (controllers)** is to send **commands** and **queries** via the [PubSub](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) system ([NATS](https://nats.io/) in this case), which will asynchronously invoke the application layer via the **command and the query handlers**- (more information concerning the application layer could be found below).

The application layer (command and query handlers) after executing, they respond to the presentation layer (controllers) via the [Request-Reply pattern](https://natsbyexample.com/examples/messaging/request-reply/go/). 

### Bounded-Contexts Folder

The bounded-contexts folder contains the **data access layer** (driven adapters of the infrastructure layer) - concrete implementations of the ports ([Hexagonal Architecture](https://bitloops.com/docs/bitloops-language/learning/Software%20Architecture/hexagonal-architecture)) of the application, organised by the specific **bounded contexts** ([DDD](https://bitloops.com/docs/bitloops-language/learning/domain-driven-design)) of the application. These concrete implementations are specific **repository implementations** as well as specific **external service implementations**. 


### Config Folder
Contains the configuration files for the application.

### Lib Folder
Contains the core of the application (inside the `bounded-contexts` sub-folder), containing the **application layer** and the **domain layer** of the application.

The sub-folders (e.g. `bounded-contexts/lib/todo`) represent the exact bounded contexts ([DDD](https://bitloops.com/docs/bitloops-language/learning/domain-driven-design)) of the application. In our case these bounded contexts represent a conceptual linguistic boundary. 

Inside each subfolder of each bounded context there is another folder which represent the specific module (e.g. `bounded-contexts/lib/todo/todo`). 

In our case each module represents a logical boundary inside the linguistic boundary of the bounded context. This means that one bounded context (linguistic boundary), could have more than one module (logical boundary) inside (see  [DDD](https://bitloops.com/docs/bitloops-language/learning/domain-driven-design)).

### Module Structure
Each module structure contains the following folders:
* application
* commands
* queries
* domain
* contracts
* ports
* tests

<p align="center" style="margin-bottom: 0px 
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual identity
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
hello (at) bitloops.com.
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
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available
at [https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

```

### File: CONTRIBUTING.md
```md
# Bitloops Language Contributor Guide

## Contributing
Thank you for your interest in contributing to Bitloops. We would love for you to contribute and help make it better! All contributions are welcome and we believe the process should be fun, enjoyable, and educational for anyone and everyone. 
Before you begin, please read our code of conduct and check existing issues. You can contribute with new issues, new docs as well as updates and tweaks, blog posts, and more.
 
## How to Start?
Firstly, we would like to invite you to our community. Join our slack group, introduce yourself and get to know the rest of the team. There is probably someone working on an issue that interests you, or has at least spent some time thinking about it. 
Reach out with questions via [Discord](https://discord.gg/cQcnRJQ256) or [@thebitloops](https://twitter.com/thebitloops) on Twitter. You can also add questions through [Bitloops' GitHub Discussions](https://github.com/bitloops/bitloops-language/discussions). If you prefer, you can also simply submit an [issue](https://github.com/bitloops/bitloops-language/issues), and a maintainer will guide you!
We strongly recommend filing an issue before working on non-trivial changes to the implementation. This lets us reach an agreement on your proposal before you put significant effort into it, and it has a much higher likelihood of being accepted.
 
### Code of Conduct
We want to keep Bitloops open and inclusive so please read and follow our [Code of Conduct](https://github.com/bitloops/bitloops-language/blob/main/CODE_OF_CONDUCT.md).
 
### How to contribute?
We recommend baby steps so you can get familiar with our contribution process. We have a list of good first issues that contain bugs and have a relatively limited scope, and therefore a great place to start. 
If you decide to fix an issue, please be sure to check the comments in case somebody is already working on it. If there hasn’t been any activity, then leave a comment stating that you intend to work on it so other people don’t accidentally duplicate your effort.
If the issue has already been claimed by someone else, but there hasn’t been any recent activity, then feel free to take over after leaving a comment. 

We would also welcome any new issues you may find. We do suggest searching for the particular issue you would like to report in the existing issue list before reporting new ones. In addition, if you do encounter any vulnerability issues, please do follow our [Security Policy](https://github.com/bitloops/bitloops-language/blob/main/.github/SECURITY) instead of creating a new issue. 
 
### Create a Pull Request
After making your changes, open a pull request (PR). Submit your PR and other Bitloopers will review the PR with you. 
If you come across an issue, such as a merge conflict, or don't know how to open a pull request, then we suggest reading [GitHub's pull request tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) on how to resolve merge conflicts and other issues. Finally, once your PR is merged, you will be proudly listed as a contributor in the contributor chart.
For an example of how to add a new bl-element check this [guide](https://github.com/bitloops/bitloops-language/blob/main/HOW_TO_ADD_BL_ELEMENT.md).
 
### Contributor License Agreement (CLA)
As an open-source programming language, Bitloops needs to obtain a contributor license agreement (CLA) from its contributors to ensure all users have access to the open source code. This process only needs to be conducted once as we will cross-check your GitHub username before accepting any PR. To complete the CLA please email us at contributor@bitloops.com and we’ll provide you with the necessary forms for online signature.  
 
### Introducing New Features
Our team wants to build the best possible version of Bitloops whilst remaining loyal to its vision and mission. At the same time we are thrilled if users want to also contribute to Bitloops and want to strike the best balance. 
Therefore, if you have ideas, please feel free to share them by opening an issue to explain and explore your ideas before introducing a new pull request. We’d love to learn from you as well as share some insights we may have. 
By doing this, Bitloops developers will be able to provide technical input, share best practices and further explain architecture or feature design patterns. This ensures the Bitloops community has sufficient discussion about new features, its value proposition and how it fits into the product roadmap. 
 
 
### Want to help in other ways?
We love PRs and appreciate all contributions, so if you want to help further, then we are your biggest fans! Below are several ways you could help Bitloops spread the joy of building software faster and better using domain-driven design principles and behavior-driven development principles:

### Content: Blogs, Podcasts, Social Media & Speaking
If you enjoy creating content and like using Bitloops, then we would actively encourage you to create blog posts, videos or social media posts about Bitloops or one of its features. Do mention @bitloops on twitter, linkedin or facebook and feel free to link to our own videos, tutorials or website. 
If you wish, email our team on hello@bitloops.com so we can give pointers and tips and help you spread the word by promoting your content on different Bitloops channels. 
 
### Giving Feedback & Reporting Bugs
Bitloops only makes sense if developers enjoy it and it solves problems. Please send any feedback through the email contributor@bitloops.com so we can better understand different use cases of Bitloops. Moreover, if you had any issue or came across any bugs, please let us know through the Slack Channel, GitHub issues or directly via email. 

### Submitting New Ideas
If you’d like to see a specific feature on Bitloops, then don’t hesitate to open an issue on our GitHub repository, providing as much information as possible. In turn, we will try to get more supporting feedback from the community and our own team to see if we can prioritize it. We’ll also get in touch directly with you to organize further discussions if convenient. 

### Improving Documentation
The Bitloops team is still small and the priorities are many. If you have any feedback on documentation, updates, designs, bug fixes or enhancements then please do not hesitate to submit and update. Any spelling, grammar or even translations are very much appreciated. 

### Meetups, Conferences and Universities
If you’re keen on improving your presenting skills and have signed up as a Speak for a Meetup, Conference or lecture at a university about your experience as a developer, then explaining what you’ve built with Bitloops could be an interesting option. Explaining the unique challenges and successes, how Bitloops supported you in developing high quality architecture can provide great speaking material. 
In fact, we would be happy to provide feedback on your talk and help you with some additional material. Please get in touch via contributor@bitloops.com!

### Help Someone Help Bitloops
There are many people looking to improve their software development skills with Bitloops, and many post questions on [Discord](https://discord.gg/cQcnRJQ256), [GitHub Discussions](https://github.com/bitloops/bitloops-language/discussions), StackOverflow, Quora or Reddit looking for solutions. Reach out to them or post an answer if you’re confident about it. You can also help by teaching others how to contribute to Bitloops repo!
 
### Community channels
We're also keen on learning from our Users and fellow developers, and have very interesting discussions on [Discord](https://discord.gg/cQcnRJQ256) on how to build great software. Join us so we can together all become better developers!
 

```

### File: HOW_TO_ADD_BL_ELEMENT.md
```md
Let's consider that we would like to create a test element that in Bitloops Language(BL) would look like this:

### BL

```antlr
Test MyTest {
    string name;
    string description;
}
```

We would have to create the syntax using Antlr in lexer and parser as below:

### Lexer

```antlr
Test:               'Test';
TestIdentifier:     UpperCaseStart IdentifierPart* Test;
```

### Parser

```antlr
testIdentifier
    : TestIdentifier
    ;

testDeclaration
    : Test testIdentifier OpenBrace fieldList CloseBrace
    ;

// Here add the new element in the source elements of the program
sourceElement
    :
    .....
    | testDeclaration
    ;
```

Then we would have to create the visitors of the new elements:

### Visitor

In visitor we create a tree with nodes that include all the information of the element and each node has it's children nodes.
In order to build that tree of nodes, we use builders.

#### TestDeclaration

`TestDeclaration` is a class type element (like Entity, Value Object, etc...) and that means that we have to add a node under the root of the tree. That's why we are not returning anything in this visitor, because the `TestNodeBuilder` will just take care of this and add the `TestDeclarationNode` under the root of the tree.
Each visitor that we are calling (e.g. `thisVisitor.visit(ctx.testIdentifier())`), returns it's corresponding node which is built by it's builder.

```ts
visitTestDeclaration(ctx: BitloopsParser.TestDeclarationContext): void {
    testDeclarationVisitor(this, ctx);
}

export const testDeclarationVisitor = (
  thisVisitor: BitloopsVisitor,
  ctx: BitloopsParser.TestDeclarationContext,
): void => {
  const metadata = produceMetadata(ctx, thisVisitor);
  const testIdentifierNode: TestIdentifierNode = thisVisitor.visit(ctx.testIdentifier());
  const fieldListNode: FieldListNode = thisVisitor.visit(ctx.fieldList());

  new TestNodeBuilder(thisVisitor.intermediateASTTree, metadata)
    .withIdentifier(testIdentifierNode)
    .withFieldList(fieldListNode)
    .build();
};
```

#### TestIdentifier

Here we have the `TestIdentifier` visitor that is returning the `TestIdentifierNode` by the `TestIdentifierNodeBuilder`. That's how `testDeclarationVisitor` has the information that it needs in order to continue.

```ts
visitTestIdentifier(ctx: BitloopsParser.TestIdentifierContext): TestIdentifierNode {
    const metadata = produceMetadata(ctx, this);

    const testIdentifier = ctx.TestIdentifier().getText();
    const testIdentifierNode = new TestIdentifierNodeBuilder(metadata)
      .withName(testIdentifier)
      .build();

    return testIdentifierNode;
}
```

### Nodes

All the nodes are classes that have a name, a type and some metadata(includes the start/end lines of the element).
We have an abstract class called `IntermediateASTNode` that every other node extends from it and also the class `IntermediateASTTree` that has all the nodes. Below are some basic methods of the two classes that are useful.

#### IntermediateASTNode

`addChild`: It adds the child to the node that is applied.

`addSibling`: It adds the sibling to the node that is applied.

`buildObjectValue`: It builds the value of the node(its children with their values) as an object.

`buildArrayValue`: It builds the value of the node as an array with objects(children values).

`buildLeafValue`: It builds the value of the node, by creating an object with key the name of the node and value its actual value.

#### IntermediateASTTree

`insertChild`: It inserts its child to currentNode and makes it the new currentNode.

`insertSibling`: It inserts the node as child to the parent of the currentNode and makes it the new currentNode.

#### TestDeclaration

`TestDeclarationNode` is a class type node as we said, so it has to extend `ClassTypeNode`. This node has also class type attribute.

```ts
export class TestDeclarationNode extends ClassTypeNode {
  private static classType = ClassTypes.Test;
  private static classNodeName = "test";

  constructor(metadata?: TNodeMetadata) {
    super({
      classType: TestDeclarationNode.classType,
      nodeType: BitloopsTypesMapping.TTest,
      metadata,
      classNodeName: TestDeclarationNode.classNodeName,
    });
  }
}
```

#### TestIdentifier

`TestIdentifierNode` is an identifier node, so it has to extend `IntermediateASTIdentifierNode`.

```ts
export class TetsIdentifierNode extends IntermediateASTIdentifierNode {
  private static classNodeName = "testIdentifier";

  constructor(metadata?: TNodeMetadata) {
    super(
      BitloopsTypesMapping.TTestIdentifier,
      TetsIdentifierNode.classNodeName,
      metadata
    );
  }
}
```

#### FieldListNode

`FieldListNode` is a simple node, so it has to extend `IntermediateASTNode`. This node and it's visitor is already implemented, but it can be reused and is a great example to show all the possible cases.

```ts
export class FieldListNode extends IntermediateASTNode {
  private static classNodeName = "fields";

  constructor(metadata?: TNodeMetadata) {
    super(
      BitloopsTypesMapping.TFieldList,
      metadata,
      FieldListNode.classNodeName
    );
  }
}
```

#### FieldNode

`FieldNode` is a simple node as well, so it has to extend `IntermediateASTNode`.

```ts
export class FieldNode extends IntermediateASTNode {
  private static classNodeName = "field";

  constructor(metadata?: TNodeMetadata) {
    super(BitloopsTypesMapping.TField, metadata, FieldNode.classNodeName);
  }
}
```

### Builders

Builders are following the [builder pattern](https://refactoring.guru/design-patterns/builder) and its one of them builds a node. Each `with...` method takes a node argument and returns itself.

#### TestDeclaration

`TestDeclarationNodeBuilder` builds `TestDeclarationNode` which is a class type node. This builder, as we said before, is responsible for adding the class type node under the root of the tree. So, it takes as argument the tree and in the build method it inserts to it it's children and sets the current node to root again. It also builds its value by calling `buildObjectValue` method. Builders that build class type nodes, also need to get the identifier name and set it as className to the class type node(here `TestDeclarationNode`). So, `withIdentifier` method is responsible for doing exactly this.

```ts
export class TestDeclarationNodeBuilder
  implements IBuilder<TestDeclarationNode>
{
  private testDeclarationNode: TestDeclarationNode;
  private identifierNode: TestIdentifierNode;
  private fieldListNode: FieldListNode;
  private intermediateASTTree: IntermediateASTTree;

  constructor(
    intermediateASTTree: IntermediateASTTree,
    metadata?: TNodeMetadata
  ) {
    this.intermediateASTTree = intermediateASTTree;
    this.testDeclarationNode = new TestDeclarationNode(metadata);
  }

  public withIdentifier(
    testIdentifierNode: TestIdentifierNode
  ): TestDeclarationNodeBuilder {
    this.identifierNode = testIdentifierNode;
    const testName = testIdentifierNode.getIdentifierName();
    this.testDeclarationNode.setClassName(testName);
    return this;
  }

  public withFieldList(
    fieldListNode: FieldListNode
  ): TestDeclarationNodeBuilder {
    this.fieldListNode = fieldListNode;
    return this;
  }

  public build(): TestDeclarationNode {
    this.intermediateASTTree.insertChild(this.testDeclarationNode);
    this.intermediateASTTree.insertChild(this.identifierNode);
    this.intermediateASTTree.insertSibling(this.fieldListNode);

    this.intermediateASTTree.setCurrentNodeToRoot();

    this.testDeclarationNode.buildObjectValue();

    return this.testDeclarationNode;
  }
}
```

#### TestIdentifier

`TestDeclarationNodeBuilder` builds `TestIdentifierNode`. It just builds its value by calling `buildLeafValue` method, because it's a leaf node. Here we don't need the `intermediateASTTree` we just handle the node, it is needed only in class type node builders.

```ts
export class TestIdentifierNodeBuilder implements IBuilder<TestIdentifierNode> {
  private testIdentifierNode: TestIdentifierNode;
  private name: string;

  constructor(metadata?: TNodeMetadata) {
    this.testIdentifierNode = new TestIdentifierNode(metadata);
  }

  public withName(identifierName: string): TestIdentifierNodeBuilder {
    this.name = identifierName;
    return this;
  }

  public build(): TestIdentifierNode {
    this.testIdentifierNode.buildLeafValue(this.name);

    return this.testIdentifierNode;
  }
}
```

#### FieldListNode

`FieldListNodeBuilder` builds `FieldListNode`. It adds in this node all the fieldNodes children and builds its value by calling `buildArrayValue` method.

```ts
export class FieldListNodeBuilder implements IBuilder<FieldListNode> {
  private fieldListNode: FieldListNode;
  private fieldNodes: FieldNode[];

  constructor(metadata?: TNodeMetadata) {
    this.fieldListNode = new FieldListNode(metadata);
  }

  public withFields(fields: FieldNode[]): FieldListNodeBuilder {
    this.fieldNodes = fields;
    return this;
  }

  public build(): FieldListNode {
    if (this.fieldNodes) {
      this.fieldNodes.forEach((fieldNode) => {
        this.fieldListNode.addChild(fieldNode);
      });
    }
    this.fieldListNode.buildArrayValue();

    return this.fieldListNode;
  }
}
```

#### FieldNode

`FieldNodeBuilder` builds `FieldNode`. It adds in this node all of its children and builds its value by calling `buildObjectValue` method.

```ts
export class FieldNodeBuilder implements IBuilder<FieldNode> {
  private typeNode: BitloopsPrimaryTypeNode;
  private identifierNode: IdentifierNode;
  private optionalNode?: OptionalNode;
  private fieldNode: FieldNode;

  constructor() {
    this.fieldNode = new FieldNode();
  }

  public withType(typeNode: BitloopsPrimaryTypeNode): FieldNodeBuilder {
    this.typeNode = typeNode;
    return this;
  }

  public withName(identifierNode: IdentifierNode): FieldNodeBuilder {
    this.identifierNode = identifierNode;
    return this;
  }

  public withOptional(optionalNode: OptionalNode): FieldNodeBuilder {
    this.optionalNode = optionalNode;
    return this;
  }

  public build(): FieldNode {
    this.fieldNode.addChild(this.typeNode);
    this.fieldNode.addChild(this.identifierNode);
    if (this.optionalNode) this.fieldNode.addChild(this.optionalNode);

    this.fieldNode.buildObjectValue();

    return this.fieldNode;
  }
}
```

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
