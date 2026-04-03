---
id: node-api-boilerplate-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:12.010134
---

# KNOWLEDGE EXTRACT: node-api-boilerplate
> **Extracted on:** 2026-03-30 17:49:12
> **Source:** node-api-boilerplate

---

## File: `.env.test`
```
DB_NAME=blog_test
```

## File: `.eslintrc.json`
```json
{
  "root": true,
  "parser": "@typescript-eslint/parser",
  "extends": ["eslint:recommended", "plugin:@typescript-eslint/recommended", "plugin:jest/recommended", "prettier"],
  "plugins": ["node", "jest", "prettier", "@typescript-eslint"],
  "parserOptions": {
    "ecmaVersion": 11
  },
  "rules": {
    "@typescript-eslint/no-namespace": 0,
    "@typescript-eslint/no-explicit-any": 0,
    "max-len": [
      "error",
      {
        "code": 120
      }
    ]
  }
}
```

## File: `.gitignore`
```
node_modules/
dist/
.index/
*.log
.idea/
.vscode/
coverage/
```

## File: `.prettierrc`
```
{
  "arrowParens": "always",
  "printWidth": 120,
  "semi": true,
  "singleQuote": true
}
```

## File: `contributing.md`
```markdown
# Contributing

Contributions are always welcome! When contributing to Node API boilerplate we ask you to follow our code of conduct:

## Code of conduct

In short: _Be nice_. Pay attention to the fact that Node API boilerplate is free software, don't be rude with the contributors or with people with questions and we'll be more than glad to help you. Destructive criticism and demanding will be ignored.

## Opening issues

When opening an issue be descriptive about the bug or the feature suggestion, don't simply paste the error message on the issue title or description. Also, **provide code to simulate the bug**, we need to know the exact circumstances in which the bug occurs. Again, follow our [code of conduct](#code-of-conduct).

## Pull requests

When opening a pull request to Node API boilerplate, follow this steps:

1. Fork the project;
2. Create a new branch for your changes;
3. Do your changes;
4. Open the pull request;
5. Write a complete description about the bug or the feature the pull request is about.
```

## File: `docker-compose.yml`
```yaml
version: '3.9'

services:
  mongodb:
    container_name: blog-mongodb
    image: mongo:4.2
    ports:
      - 27017:27017
    volumes:
      - mongo_data:/data/db
    environment:
      MONGO_INITDB_ROOT_USERNAME: blog
      MONGO_INITDB_ROOT_PASSWORD: blog

  mongo-express:
    container_name: blog-mongo-express
    image: mongo-express
    depends_on:
      - mongodb
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_URL: mongodb://blog:blog@blog-mongodb:27017

  dev:
    container_name: blog-dev
    build:
      context: .
      dockerfile: ./docker/Dockerfile.dev
      args:
        USER_ID: ${USER_ID:-1000}
        GROUP_ID: ${GROUP_ID:-1000}
    depends_on:
      - mongodb
    network_mode: host
    environment:
      - NODE_ENV=${NODE_ENV:-development}
    volumes:
      - .:/opt/node-app
      - npm_cache:/home/node/.npm-packages
    tty: true
    profiles:
      - dev

volumes:
  npm_cache:
  mongo_data:
```

## File: `example_requests.http`
```
# @name article
POST http://localhost:3000/api/articles
Content-Type: application/json

{
  "title": "This is my first article",
  "content": "Test article content"
}

###
GET http://localhost:3000/api/articles

###
@articleId = {{article.response.body.$.id}}

POST http://localhost:3000/api/articles/{{articleId}}/comments
Content-Type: application/json

{
  "body": "Nice!"
}

###

@articleId = {{article.response.body.$.id}}

PATCH http://localhost:3000/api/articles/{{articleId}}/publish
```

## File: `LICENSE.md`
```markdown
# MIT License

Copyright (c) 2021 Talysson de Oliveira Cassiano, Bruno Henrique de Castro

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

## File: `package.json`
```json
{
  "name": "node-api-boilerplate",
  "version": "3.0.0-beta",
  "description": "A boilerplate for web APIs using Node",
  "main": "dist/index.js",
  "private": true,
  "license": "MIT",
  "contributors": [
    "Talysson <talyssonoc@gmail.com>",
    "Bruno <brunohcastro@gmail.com>"
  ],
  "engines": {
    "node": ">=12.0.0"
  },
  "dependencies": {
    "awilix": "^4.3.4",
    "cors": "^2.8.5",
    "dotenv": "^10.0.0",
    "express": "^4.17.1",
    "helmet": "^5.1.1",
    "joi": "^17.4.1",
    "lodash.template": "^4.5.0",
    "mongodb": "^4.0.0",
    "pino": "^6.12.0",
    "pino-http": "^5.5.0",
    "swagger-jsdoc": "^6.1.0",
    "swagger-ui-express": "^4.1.6",
    "tsconfig-paths": "^3.10.1",
    "types-joi": "^2.1.0",
    "uuid": "^8.3.2",
    "uuid-mongodb": "^2.4.4"
  },
  "devDependencies": {
    "@types/cors": "^2.8.12",
    "@types/express": "^4.17.13",
    "@types/jest": "^26.0.24",
    "@types/lodash.template": "^4.5.0",
    "@types/mongodb": "^3.6.20",
    "@types/node": "^16.3.3",
    "@types/pino": "^6.3.11",
    "@types/supertest": "^2.0.11",
    "@types/swagger-jsdoc": "^6.0.1",
    "@types/swagger-ui-express": "^4.1.3",
    "@typescript-eslint/eslint-plugin": "^4.28.3",
    "@typescript-eslint/parser": "^4.28.3",
    "eslint": "^7.30.0",
    "eslint-config-prettier": "^8.3.0",
    "eslint-plugin-jest": "^24.3.6",
    "eslint-plugin-node": "^11.1.0",
    "eslint-plugin-prettier": "^3.4.0",
    "jest": "^27.0.6",
    "pino-pretty": "^5.1.1",
    "prettier": "^2.3.2",
    "rimraf": "^3.0.2",
    "supertest": "^6.1.5",
    "ts-jest": "^27.0.5",
    "ts-node": "^10.1.0",
    "ts-node-dev": "^1.1.8",
    "tsconfig-paths-jest": "^0.0.1",
    "typescript": "^4.3.5"
  },
  "scripts": {
    "prebuild": "rimraf dist",
    "build": "tsc -p tsconfig.prod.json",
    "dev": "tsnd --transpile-only --files src/index.ts | pino-pretty -c -l",
    "debug": "tsnd --transpile-only --inspect --files src/index.ts | pino-pretty -c -l",
    "cli": "tsnd --transpile-only --files src/index.ts --cli",
    "remote": "ts-node bin/replClient.ts",
    "test": "jest"
  },
  "jest": {
    "moduleFileExtensions": [
      "js",
      "json",
      "ts"
    ],
    "rootDir": ".",
    "transform": {
      "^.+\\.(t|j)s$": "ts-jest"
    },
    "coverageDirectory": "coverage",
    "collectCoverage": true,
    "collectCoverageFrom": [
      "<rootDir>/src/**"
    ],
    "testRegex": "(/__tests__/.*(test|spec))\\.[jt]sx?$",
    "moduleNameMapper": {
      "@/(.*)": "<rootDir>/src/$1"
    },
    "setupFiles": [
      "./src/__tests__/setup.ts"
    ]
  }
}
```

## File: `README.md`
```markdown
# What is it

This project is a starting point for you to develop a web API in a scalable way with Node and TypeScript, and was implemented following ideas from layered architecture, Clean Architecture, and Domain-Driven Design. While it contains an opinionated design and structure, it was built to be extensible and flexible so you can modify and adapt it according to your team's needs and preferences.

This version of the boilerplate is still in beta, so might contain abstractions that will change or be missing features. Contribution from the community, either through PRs or is welcome.

**Important** This is the documentation for the v3 of the boilerplate. Click here if you want the [docs for the v2.1](https://github.com/talyssonoc/node-api-boilerplate/tree/v2.1).

# Usage

## How to run the server

During development, the project can be run in two different ways.

If you want to just run the application in development mode, use the following command:

```sh
$ yarn dev

```

To run the application in debug mode in a way that the execution will stop when a debugger statement is called, use:

```sh
$ yarn debug
```

## How to run the application console

You can also run the application in console mode, giving you programmatic access to the environment, this can also be done in two different ways.

To run a new instance, isolated from the server, use the following command:

```sh
$ yarn cli
```

For the new instance, you're able to access the dependencies registered in the container using `registry.<dependencyName>` or through the `container` variable.

But if you're already running the server (this is a requirement) and you want to a console connected to the process of the server, giving you access to the current state of it, use:

```sh
$ yarn remote [server address] [REPL port]
```

## Tests

The boilerplate is prepared to run tests using Jest. We usually group the tests in folders called `__tests__` (following Jest convention) for each module of the application. To run the tests use the following command:

```sh
$ yarn test
```

## Docker wrapper

In case you want to use Docker to run it, this project includes a [docker wrapper](https://github.com/brunohcastro/node-base) for development. Any command can be executed by calling the scripts under the `dbin/` folder.

```sh
$ dbin/yarn dev

$ dbin/yarn debug

$ dbin/yarn cli

$ dbin/yarn remote [server address] [REPL port]

$ dbin/yarn test
```

The container runs using host networking, so there's no need to map ports. Keep in mind that environment variables should be added to the docker-compose.yml.

### Wrapper commands

```sh
# Runs the command inside an ephemeral container using the app service described in the docker-compose file as a base (use the --root flag if the command should be run as root)
$ dbin/run [--root] <command>

# Rebuild the image after any changes to the dockerfile
$ dbin/build

# Remove all containers and their volumes (WARNING any cache or files not stored in the filesystem will be deleted)
$ dbin/dispose

# Appends a RUN command to the base image, useful to install new packages
$ dbin/chimg <command>
```

### Wrapper Aliases

```sh
# Creates a new <name> file in dbin to alias the <command> inside the docker container (use the --root flag if the command should be run as root)
$ dbin/mkalias [--root] <name> <command>

# Opens a new terminal in the project folder (use the --root flag if the shell should assume the root user)
$ dbin/shell [--root]

# Runs npm in the project folder
$ dbin/npm

# Runs npx in the project folder
$ dbin/npx

# Runs yarn in the project folder
$ dbin/yarn
```

### Wrapper Helpers

```bash
# Adds dbin folder to the PATH only for the current terminal session.
$ source dbin/local-env

# After using this command you can use the any script inside the dbin folder without the dbin/ prefix
```

## Dependency injection

We use [Awilix](https://www.npmjs.com/package/awilix) to implement dependency injection and decouple the parts of your application. The boilerplate was developed in a way that each [module](#modules) is able to consume and augment the registered dependencies separately. Click here to know more about [inversion of control and dependency injection](https://www.martinfowler.com/articles/injection.html). The creator of Awilix also has a very good series of posts about the design decisions of the library that you can read [clicking here](https://medium.com/@Jeffijoe/dependency-injection-in-node-js-2016-edition-f2a88efdd427).

The instance of the Awilix dependency container is created in the file `src/container.ts`. You'll notice that the type of the dependencies is defined by combining the types of the dependencies exported by each of the modules. After that, each of these modules will be then responsible for registering those dependencies in the container during the [boot process](#boot).

## Import paths

In order to make it easier and cleaner to import files we use [tsconfig-paths](https://www.npmjs.com/package/tsconfig-paths) configured to alias the path to the `src/` folder as `@`. For example, if you want to import the file `src/article/domain/Article.ts`, you can do it through the path `@/article/domain/Article.ts` no matter from which file you are importing it.

## Modules

The codebase is divided into modules, where each module can represent either an integration (with some HTTP or database library, for example) or a feature (that are called here as app modules). Each module requires to be given a name and has access to the configuration options, the logger, the [lifecycle events](#lifecycle-events) and the the context of the application in order to add and use dependencies from the container. More technical details about the modules will be given in a [separate section](#module-internals).

## Logging

We use [Pino](https://www.npmjs.com/package/pino) for effective and high performance logging. The instance of the logger is available in the dependency injection container to be used across the board and also is one of the arguments of the module constructor.

## Recommended patterns

This boilerplate follows ideas from multiple good software development practices sources like [layered architecture](http://wiki.c2.com/?FourLayerArchitecture), [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [Domain-Driven Design](https://www.domainlanguage.com/ddd/), among others. As such, even though it's not required, there are some patterns that are recommended and suggested that work well with the principles that make the boilerplate scalable and extensible. To mention some:

- We recommend the usage of entities, aggregates and value objects, and other patterns that are used to isolate domain-specific code from the rest of the application code, as mentioned in Domain-Driven Design. To create a standard and practical way to define invariants for entities and aggregates there is a function that can be imported from the [lib](#lib-and-shared-kernel) called `withInvariants`. Click here to read a brief [reference about Domain-Driven Design](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf).
- To abstract the persistence layer of your application we recommend the usage of the [repository pattern](https://martinfowler.com/eaaCatalog/repository.html). An important fact to take note is that even though the example app in the boilerplate used Mongo, you're not required to use it in your application, you just need to create a module to connect to the database of your preference and implement repositories that communicate with this database
- To favor a more predictable and explicit definition of domain rules we favor immutable objects and pure functions to define business rules rather than classes. You'll see that most of the code does not expose classes to be used.
- To export and import domain-specific code we use [TypeScript namespaces](https://www.typescriptlang.org/docs/handbook/namespaces.html). We believe it helps in making the code that is imported from the domain easier to read since it will always be prefixed by the name of the context it concerns about, loosely inspired by [Elixir modules](https://elixir-lang.org/getting-started/modules-and-functions.html). We follow the pattern of adding a named export called Type to expose the entity/aggregate/value object from that given file.

## Going to production

To run your app in production mode, you'll need to follow these steps:

1. Build the application with `yarn build`
2. Define any environment variable important for production
3. Start the app with `yarn start`

# How it works

## Context

The base of an application built with the boilerplate is the context instance. The context, defined in `src/_lib/Context.ts` and instantiated in `src/context.ts`, is what makes all the parts talk to each other and what defines what will be exposed to the modules during their creation, which can be customized by changing the object that is passed to the `makeContext` function in `src/context.ts`. Every module that is defined using the function `makeModule` provided by the same context is able to communicate with each other.

It's important to mention that you are able to have multiple isolated contexts in the same codebase in case you want to have more than one application, they will have isolated dependency containers, modules and will run separately. The context implementation will ensure that modules from different contexts are isolated, so you should not try to plug a module from a given context into a different context's `bootstrap` function.

## Module internals

Modules are the building pieces of an application built with this boilerplate. You can either encapsulate an integration or a feature using a module or any other division you think makes sense for your application. During the boot process of the application, all the modules will be imported and run in the order they are passed to the bootstrap function in `src/_boot/index.ts`, this order is important because it can influence how a module will depend on another module and in the cleanup process when the app is stopped. When run, a module is able to access the configuration options of the application, the dependency injection container, and register to subsequent [lifecycle events](#lifecycle-events) of the boot process. If some cleanup logic is needed to be run for a module during the stopping process of the application, the module must return a function that implements this logic, similar to [how React implements the cleanup of effects](https://reactjs.org/docs/hooks-effect.html#effects-with-cleanup).

Module constructors should be used mostly as simple glue between the integration or feature implementation and the application, prefer to put the actual implementation of the logic inside the `_lib/` folder (like database module does with `MongoProvider`) or a feature folder inside `src/` (like we do for the article module) accordingly.

## Lib and shared kernel

Besides the feature folders that go inside `src/`, we also separate abstractions that will be used across the codebase in the `_lib/` and `_sharedKernel/` folders. Inside `_lib/` we usually put code that is not specific to our application, code that could be easily extracted to a npm package if necessary, like abstractions around other packages, reusable generic types and the such. For application-specific reusable logic between multiple modules we use the `_sharedKernel/` folder. To understand more about what the shared kernel is, we recommend reading the [DDD quick reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) section about it.

## Boot

The boot process consists of setting up all the necessary code for the application to run, including running the modules and going through the [lifecycle events](#lifecycle-events). The files used during the boot process are all inside the `_boot/` folder, including the definition of the integration modules, but the abstractions created for this, like the context, are imported from the [lib](#lib-and-shared-kernel). To understand more about the booting process begin looking into the `src/context.ts` file and then the `src/_boot/index.ts` file.

## Lifecycle events

Both the boot and stopping processes are defined as a sequence of lifecycle events. These events exist in order to make these processes explicit and allow the modules to hook into them to properly integrate them into the application execution. Here's the order of lifecycle events for the boot and the stopping processes, we're gonna cover how to hook into an event in the next section.

Boot:

1. Booting:

- The booting event is dispatched once the function bootstrap is called in `src/_boot/index.ts`
- The modules are invoked during this lifecycle step, so by the time each module is invoked this lifecycle event was already dispatched
- It's not possible for a module to hook into this event because it's run by the context to declare that the boot process is started
- Mostly for internal usage to prepare the rest of the boot process

2. Booted:

- When this event is dispatched it's a message to let the modules know that all the modules were already invoked and had already hooked into the other lifecycle events
- This is a good place to register error handlers because every module has already registered its routes when they were invoked
- Use this event to do anything you might need after all the module constructors are done running

3. Ready:

- This lifecycle event happens after all the listeners for the booted event were run
- This is the proper place to actually start things, like starting the server, make queue consumers start listening to messages, or waiting for commands in case the app is running in REPL mode

4. Running:

- After everything from the ready event is done, the app is now actually running
- A good usage for this lifecycle event is to know if the app is already prepared to be accessed during the setup of an automated test or offer info about the process in the console

Stopping

1. Disposing

- It's during this lifecycle event that the cleanup functions returned by the modules will be run
- To make the cleanup process consistent, the cleanup functions are run in the inverse order their modules were passed to the bootstrap function. So if your app uses `bootstrap(database, server)`, during the disposing process the cleanup function of the server module will be called first and then the database one.
- As an example, this is where the server is stopped and the database connections are closed
- It's intended to be used to revert everything initialized during Booting lifecycle event

2. Disposed

- By the time Disposed event is dispatched, we expect that everything that keeps the process open is already finished, leaving it in a safe state to be terminated
- You could use this event to clean temporary files, for instance

3. The application should now be completely stopped and the process is terminated

To be able to hook into lifecycle events, access the property `app` in the object passed to the constructor of the modules. The `app` object contains a function for each lifecycle, prefixing it with the word `on`. So, for example, to hook into the Booted event, call `app.onBooted(callback)`.
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "commonjs",
    "lib": ["esnext"],
    "allowJs": true,
    "checkJs": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "removeComments": false,
    "strict": true,
    "noImplicitAny": false,
    "noUnusedLocals": true,
    "moduleResolution": "node",
    "baseUrl": "./src",
    "paths": {
      "@/*": ["*"]
    },
    "typeRoots": ["node_modules/@types"],
    "esModuleInterop": true,
    "skipLibCheck": false,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["typings.d.ts", "src/**/*"],
  "exclude": ["./dist", "./node_modules"]
}
```

## File: `tsconfig.prod.json`
```json
{
  "extends": "./tsconfig.json",
  "exclude": [
    "src/__tests__",
    "src/**/__tests__"
  ]
}
```

## File: `typings.d.ts`
```typescript
declare module 'http' {
  export interface IncomingMessage {
    id?: string;
    container: import('@/container').Container;
  }
}
```

## File: `dbin/build`
```
#!/bin/bash

USER_ID=$(id -u) GROUP_ID=$(id -g) docker-compose build dev
```

## File: `dbin/chimg`
```
#!/bin/bash

PARENT_DIR="$(cd "$(dirname "$0")" && cd .. && pwd)"

cp "$PARENT_DIR/docker/Dockerfile.dev" "$PARENT_DIR/docker/Dockerfile.dev.bkp"

echo -e "\nRUN $*" >> "$PARENT_DIR/docker/Dockerfile.dev"

if USER_ID=$(id -u) GROUP_ID=$(id -g) docker-compose build dev; then
   rm -f "$PARENT_DIR/docker/Dockerfile.dev.bkp"
else
   mv "$PARENT_DIR/docker/Dockerfile.dev.bkp" "$PARENT_DIR/docker/Dockerfile.dev"
fi
```

## File: `dbin/dispose`
```
#!/bin/bash

docker-compose down -v
```

## File: `dbin/local-env`
```
#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

export PATH="$PATH:$DIR"
```

## File: `dbin/mkalias`
```
#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

if [[ $1 == --root ]] ; then
  runner="\$DIR/run --root"
  name=$2
  shift 2
else
  runner="\$DIR/run"
  name=$1
  shift 1
fi

cat >"$DIR/$name" <<EOL
#!/bin/bash

DIR="\$(cd "\$(dirname "\$0")" && pwd)"

. "$runner" $@ "\$@"
EOL

chmod +x "$DIR/$name"
```

## File: `dbin/mvroot`
```
#!/bin/bash

PARENT_DIR="$(cd "$(dirname "$0")" && cd .. && pwd)"

TARGET_DIR="$1"

mv "$PARENT_DIR/README.md" "$PARENT_DIR/INSTRUCTIONS.md" 2>/dev/null

(shopt -s dotglob; mv "$PARENT_DIR/$TARGET_DIR"/* "$PARENT_DIR")

rm -r "${PARENT_DIR:?}/$TARGET_DIR"
```

## File: `dbin/npm`
```
#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

. "$DIR/run" npm "$@"
```

## File: `dbin/npx`
```
#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

. "$DIR/run" npx "$@"
```

## File: `dbin/run`
```
#!/bin/bash

user=""

if [[ $1 == --root ]] ; then
  user="--user root"
  shift 1
fi

if docker-compose ps -a | grep -E -i -q 'app(\s*)running'; then
  USER_ID=$(id -u) GROUP_ID=$(id -g) docker-compose --profile dev exec $user dev "$@"
else
  USER_ID=$(id -u) GROUP_ID=$(id -g) docker-compose --profile dev run --rm $user --service-ports dev "$@"
fi
```

## File: `dbin/shell`
```
#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

if [[ $1 == --root ]] ; then
  shift
  . "$DIR/run" --root /bin/ash "$@"
else
  . "$DIR/run" /bin/ash "$@"
fi
```

## File: `dbin/yarn`
```
#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

. "$DIR/run" yarn "$@"
```

## File: `docker/Dockerfile.dev`
```
FROM node:16-alpine

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN apk update \
    && apk add --no-cache \
        ca-certificates \
        curl \
        tzdata \
        git \
        build-base \
        linux-headers \
        coreutils \
        shadow \
        sudo \
  && usermod -u ${USER_ID} node \
  && groupmod -g ${GROUP_ID} node \
  && mkdir /opt/node-app \
  && chown -R node:node /opt/node-app \
  && mkdir /home/node/.npm-packages \
  && chown -R node:node /home/node/.npm-packages \
  && npm config set -g prefix "/home/node/.npm-packages" \
  && echo "node ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

ENV PATH="$PATH:/home/node/.npm-packages/bin"

USER node

WORKDIR /opt/node-app
```

## File: `src/config.ts`
```typescript
import { MainConfig } from '@/_boot';
import { environment, EnvironmentConfig, envNumber, envString } from '@/_lib/Environment';

type Configuration = MainConfig & EnvironmentConfig;

const config: Configuration = {
  appName: 'node-api-boilerplate',
  cli: process.argv.includes('--cli'),
  environment: environment(),
  repl: {
    port: envNumber('REPL_PORT', 2580),
  },
  http: {
    host: envString('HOST', 'localhost'),
    port: envNumber('PORT', 3000),
  },
  swagger: {
    title: 'Blog API',
    version: '1.0.0',
    basePath: '/api',
    docEndpoint: '/api-docs',
  },
  mongodb: {
    database: envString('DB_NAME', 'blog'),
    host: envString('DB_HOST', 'mongodb://localhost:27017'),
    username: envString('DB_USER', 'blog'),
    password: envString('DB_PASS', 'blog'),
  },
};

export { config };
export type { Configuration };
```

## File: `src/container.ts`
```typescript
import { BuildResolverOptions, createContainer } from 'awilix';
import { MainRegistry } from '@/_boot';
import { makeInitialize } from '@/_lib/Initialize';

type Registry = MainRegistry;

const container = createContainer<Registry>();
const initialize = makeInitialize<Registry, BuildResolverOptions<any>>(container.build);

type Container = typeof container;
type Initialize = typeof initialize;

export { container, initialize };
export type { Container, Registry, Initialize };
```

## File: `src/context.ts`
```typescript
import { makeContext } from '@/_lib/Context';
import { container, initialize } from '@/container';
import { config } from '@/config';
import { logger } from '@/_lib/logger';

const { withContext, makeModule } = makeContext({ config, container, logger, initialize }, { logger });

export { withContext, makeModule };
```

## File: `src/index.ts`
```typescript
import('tsconfig-paths')
  .then(({ register }) => {
    register({
      baseUrl: __dirname,
      paths: { '@/*': ['*'] },
      addMatchAll: false,
    });
  })
  .then(() => import('@/_boot'))
  .then(({ main }) => main())
  .catch((err) => {
    console.error(err);

    if (process.env.NODE_ENV === 'production') {
      process.kill(process.pid, 'SIGTERM');
    }
  });
```

## File: `src/article/index.ts`
```typescript
import { asFunction } from 'awilix';
import { CreateArticle, makeCreateArticle } from '@/article/application/useCases/CreateArticle';
import { DeleteArticle, makeDeleteArticle } from '@/article/application/useCases/DeleteArticle';
import { makePublishArticle, PublishArticle } from '@/article/application/useCases/PublishArticle';
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { ArticleCollection, initArticleCollection } from '@/article/infrastructure/ArticleCollection';
import { makeMongoArticleRepository } from '@/article/infrastructure/MongoArticleRepository';
import { makeArticleController } from '@/article/interface/http/articleController';
import { FindArticles } from '@/article/application/query/FindArticles';
import { withMongoProvider } from '@/_lib/MongoProvider';
import { toContainerValues } from '@/_lib/di/containerAdapters';
import { makeMongoFindArticles } from '@/article/infrastructure/MongoFindArticles';
import { makeModule } from '@/context';
import { makeArticleCreatedEmailListener } from '@/article/interface/email/ArticleCreatedEmailListener';

const articleModule = makeModule('article', async ({ container: { register }, initialize }) => {
  const [collections] = await initialize(
    withMongoProvider({
      articleCollection: initArticleCollection,
    })
  );

  register({
    ...toContainerValues(collections),
    articleRepository: asFunction(makeMongoArticleRepository),
    createArticle: asFunction(makeCreateArticle),
    publishArticle: asFunction(makePublishArticle),
    deleteArticle: asFunction(makeDeleteArticle),
    findArticles: asFunction(makeMongoFindArticles),
  });

  await initialize(makeArticleController, makeArticleCreatedEmailListener);
});

type ArticleRegistry = {
  articleCollection: ArticleCollection;
  articleRepository: ArticleRepository;
  createArticle: CreateArticle;
  publishArticle: PublishArticle;
  deleteArticle: DeleteArticle;
  findArticles: FindArticles;
};

export { articleModule };
export type { ArticleRegistry };
```

## File: `src/article/application/events/ArticleCreatedEvent.ts`
```typescript
import { Article } from '@/article/domain/Article';
import { Event } from '@/_lib/events/Event';
import { v4 } from 'uuid-mongodb';

namespace ArticleCreatedEvent {
  export const topic = 'Article' as const;
  export const eventType = 'ArticleCreatedEvent' as const;

  type ArticleCreatedEvent = Event<Article.Type, typeof eventType, typeof topic>;

  export const create = (article: Article.Type): ArticleCreatedEvent => ({
    eventId: v4().toString(),
    eventType,
    topic,
    payload: article,
  });

  export type Type = ArticleCreatedEvent;
}

export { ArticleCreatedEvent };
```

## File: `src/article/application/query/FindArticles.d.ts`
```typescript
import { PaginatedQueryResult, QueryHandler, SortedPaginatedQuery } from '@/_lib/CQRS';

type ArticleListItemDTO = Readonly<{
  id: string;
  title: string;
  content: string;
  publishedAt: Date;
  comments: ReadonlyArray<{
    id: string;
    body: string;
    createdAt: Date;
  }>;
}>;

type ArticleFilter = {
  title?: string;
  publishedBetween?: Date[];
};

type FindArticles = QueryHandler<SortedPaginatedQuery<ArticleFilter>, PaginatedQueryResult<ArticleListItemDTO[]>>;

export { FindArticles };
```

## File: `src/article/application/useCases/CreateArticle.ts`
```typescript
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { Article } from '@/article/domain/Article';
import { ApplicationService } from '@/_lib/DDD';
import { ArticleCreatedEvent } from '@/article/application/events/ArticleCreatedEvent';
import { eventProvider } from '@/_lib/pubSub/EventEmitterProvider';

type Dependencies = {
  articleRepository: ArticleRepository;
};

type CreateArticleDTO = {
  title: string;
  content: string;
};

type CreateArticle = ApplicationService<CreateArticleDTO, string>;

const makeCreateArticle = eventProvider<Dependencies, CreateArticle>(
  ({ articleRepository }, enqueue) =>
    async (payload: CreateArticleDTO) => {
      const id = await articleRepository.getNextId();

      const article = Article.create({
        id,
        title: payload.title,
        content: payload.content,
      });

      await articleRepository.store(article);

      enqueue(ArticleCreatedEvent.create(article));

      return id.value;
    }
);

export { makeCreateArticle };
export type { CreateArticle };
```

## File: `src/article/application/useCases/DeleteArticle.ts`
```typescript
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { Article } from '@/article/domain/Article';
import { ApplicationService } from '@/_lib/DDD';

type Dependencies = {
  articleRepository: ArticleRepository;
};

type DeleteArticle = ApplicationService<string, void>;

const makeDeleteArticle =
  ({ articleRepository }: Dependencies): DeleteArticle =>
  async (payload: string) => {
    let article = await articleRepository.findById(payload);

    article = Article.markAsDeleted(article);

    await articleRepository.store(article);
  };

export { makeDeleteArticle };
export type { DeleteArticle };
```

## File: `src/article/application/useCases/PublishArticle.ts`
```typescript
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { Article } from '@/article/domain/Article';
import { ApplicationService } from '@/_lib/DDD';
import { BusinessError } from '@/_sharedKernel/domain/error/BusinessError';
import { Logger } from 'pino';

type Dependencies = {
  articleRepository: ArticleRepository;
  logger: Logger;
};

type PublishArticle = ApplicationService<string, void>;

const makePublishArticle =
  ({ articleRepository, logger }: Dependencies): PublishArticle =>
  async (payload: string) => {
    const article = await articleRepository.findById(payload);

    if (Article.isPublished(article)) {
      throw BusinessError.create(
        // eslint-disable-next-line max-len
        `Can't republish the Article(id=${payload}) because it was already published at ${article.publishedAt.toISOString()}`
      );
    }

    const publishedArticle = Article.publish(article);

    await articleRepository.store(publishedArticle);

    logger.info(`[PublishArticle] Article(id=${payload}) published at ${article.publishedAt?.toISOString()}`);
  };

export { makePublishArticle };
export type { PublishArticle };
```

## File: `src/article/domain/Article.ts`
```typescript
import { AggregateRoot } from '@/_lib/DDD';
import { makeWithInvariants } from '@/_lib/WithInvariants';
import { ArticleId } from '@/_sharedKernel/domain/ArticleId';

namespace Article {
  type Article = AggregateRoot<ArticleId> &
    Readonly<{
      title: string;
      content: string;
      state: 'DRAFT' | 'PUBLISHED' | 'DELETED';
      publishedAt: Date | null;
      createdAt: Date;
      updatedAt: Date;
      version: number;
    }>;

  type PublishedArticle = Omit<Article, 'publishedAt' | 'state'> & Readonly<{ state: 'PUBLISHED'; publishedAt: Date }>;

  const withInvariants = makeWithInvariants<Article>((self, assert) => {
    assert(self.title?.length > 0);
    assert(self.content?.length > 0);
  });

  type ArticleProps = Readonly<{
    id: ArticleId;
    title: string;
    content: string;
  }>;

  export const create = withInvariants(
    (props: ArticleProps): Article => ({
      id: props.id,
      title: props.title,
      content: props.content,
      state: 'DRAFT',
      publishedAt: null,
      createdAt: new Date(),
      updatedAt: new Date(),
      version: 0,
    })
  );

  export const publish = withInvariants(
    (self: Article): PublishedArticle => ({
      ...self,
      state: 'PUBLISHED',
      publishedAt: new Date(),
    })
  );

  export const markAsDeleted = withInvariants(
    (self: Article): Article => ({
      ...self,
      state: 'DELETED',
    })
  );

  export const changeTitle = withInvariants(
    (self: Article, title: string): Article => ({
      ...self,
      title,
    })
  );

  export const isPublished = (self: Article): self is PublishedArticle => self.state === 'PUBLISHED';

  export type Type = Article;
}

export { Article };
```

## File: `src/article/domain/ArticleRepository.d.ts`
```typescript
import { Article } from '@/article/domain/Article';
import { Repository } from '@/_lib/DDD';

type ArticleRepository = Repository<Article.Type> & {
  findById(id: string): Promise<Article.Type>;
};

export { ArticleRepository };
```

## File: `src/article/infrastructure/ArticleCollection.ts`
```typescript
import { Collection, Db } from 'mongodb';
import { MUUID } from 'uuid-mongodb';

type ArticleSchema = {
  _id: MUUID;
  title: string;
  content: string;
  status: 'DRAFT' | 'PUBLISHED' | 'DELETED';
  publishedAt: Date | null;
  deleted: boolean;
  createdAt: Date;
  updatedAt: Date;
  version: number;
};

type ArticleCollection = Collection<ArticleSchema>;

const initArticleCollection = async (db: Db): Promise<ArticleCollection> => {
  const collection: ArticleCollection = db.collection('article');

  await collection.createIndex({ title: 1 }, { unique: true });
  await collection.createIndex({ _id: 1, version: 1 });
  await collection.createIndex({ _id: 1, deleted: 1 });

  return collection;
};

export { initArticleCollection };
export type { ArticleSchema, ArticleCollection };
```

## File: `src/article/infrastructure/ArticleMapper.ts`
```typescript
import { Article } from '@/article/domain/Article';
import { ArticleSchema } from '@/article/infrastructure/ArticleCollection';
import { DataMapper } from '@/_lib/DDD';
import { ArticleIdProvider } from '@/_sharedKernel/infrastructure/ArticleIdProvider';
import { from } from 'uuid-mongodb';

const ArticleMapper: DataMapper<Article.Type, ArticleSchema> = {
  toData: (entity: Article.Type) => ({
    _id: from(entity.id.value),
    title: entity.title,
    content: entity.content,
    status: entity.state,
    publishedAt: entity.publishedAt,
    createdAt: entity.createdAt,
    deleted: entity.state === 'DELETED',
    updatedAt: entity.createdAt,
    version: entity.version,
  }),
  toEntity: (data: ArticleSchema) => ({
    id: ArticleIdProvider.create(from(data._id).toString()),
    title: data.title,
    content: data.content,
    state: data.status,
    publishedAt: data.publishedAt,
    createdAt: data.createdAt,
    updatedAt: data.createdAt,
    version: data.version,
  }),
};

export { ArticleMapper };
```

## File: `src/article/infrastructure/MongoArticleRepository.ts`
```typescript
import { Article } from '@/article/domain/Article';
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { ArticleCollection } from '@/article/infrastructure/ArticleCollection';
import { ArticleMapper } from '@/article/infrastructure/ArticleMapper';
import { NotFoundError } from '@/_lib/errors/NotFoundError';
import { ArticleId } from '@/_sharedKernel/domain/ArticleId';
import { ArticleIdProvider } from '@/_sharedKernel/infrastructure/ArticleIdProvider';
import { from, v4 } from 'uuid-mongodb';

type Dependencies = {
  articleCollection: ArticleCollection;
};

const makeMongoArticleRepository = ({ articleCollection }: Dependencies): ArticleRepository => ({
  async getNextId(): Promise<ArticleId> {
    return Promise.resolve(ArticleIdProvider.create(v4().toString()));
  },
  async findById(id: string): Promise<Article.Type> {
    const article = await articleCollection.findOne({ _id: from(id), deleted: false });

    if (!article) {
      throw NotFoundError.create();
    }

    return ArticleMapper.toEntity(article);
  },
  async store(entity: Article.Type): Promise<void> {
    const { _id, version, ...data } = ArticleMapper.toData(entity);

    const count = await articleCollection.countDocuments({ _id });

    if (count) {
      await articleCollection.updateOne(
        { _id, version, deleted: false },
        {
          $set: {
            ...data,
            updatedAt: new Date(),
            version: version + 1,
          },
        }
      );

      return;
    }

    await articleCollection.insertOne({
      _id,
      ...data,
      version,
    });
  },
});

export { makeMongoArticleRepository };
```

## File: `src/article/infrastructure/MongoFindArticles.ts`
```typescript
import { ArticleCollection, ArticleSchema } from '@/article/infrastructure/ArticleCollection';
import MUUID from 'uuid-mongodb';
import { FindArticles } from '@/article/application/query/FindArticles';
import { CommentSchema } from '@/comment/infrastructure/CommentCollection';
import { Filter } from 'mongodb';

type Dependencies = {
  articleCollection: ArticleCollection;
};

const makeMongoFindArticles =
  ({ articleCollection }: Dependencies): FindArticles =>
  async ({ pagination, filter, sort }) => {
    let match: Filter<ArticleSchema> = {
      status: 'PUBLISHED',
      deleted: false,
    };

    if (filter.title) {
      match = {
        ...match,
        title: { $regex: `^${filter.title}`, $options: 'i' },
      };
    }

    if (filter.publishedBetween) {
      match = {
        ...match,
        publishedAt: {
          $gte: new Date(filter.publishedBetween[0]),
          $lt: new Date(filter.publishedBetween[1]),
        },
      };
    }

    const articles = await articleCollection
      .aggregate([
        {
          $match: match,
        },
        {
          $skip: Math.max(1 - pagination.page, 0) * pagination.pageSize,
        },
        {
          $limit: pagination.pageSize,
        },
        ...(sort?.length
          ? [{ $sort: sort.reduce((acc, { field, direction }) => ({ [field]: direction === 'asc' ? 1 : -1 }), {}) }]
          : []),
        {
          $lookup: {
            from: 'comment',
            as: 'comments',
            let: { articleId: '$_id' },
            pipeline: [
              {
                $match: {
                  deleted: false,
                  $expr: { $eq: ['$articleId', '$$articleId'] },
                },
              },
            ],
          },
        },
      ])
      .toArray<ArticleSchema & { comments: CommentSchema[]; publishedAt: Date }>();

    const totalElements = await articleCollection.countDocuments(match);

    const totalPages = Math.ceil(totalElements / pagination.pageSize);

    return {
      data: articles.map((article) => ({
        id: MUUID.from(article._id).toString(),
        title: article.title,
        content: article.content,
        publishedAt: article.publishedAt,
        comments: article.comments.map((comment) => ({
          id: MUUID.from(comment._id).toString(),
          body: comment.body,
          createdAt: comment.createdAt,
        })),
      })),
      page: {
        totalPages,
        pageSize: pagination.pageSize,
        totalElements,
        current: pagination.page,
        first: pagination.page === 1,
        last: pagination.page === totalPages,
      },
    };
  };

export { makeMongoFindArticles };
```

## File: `src/article/interface/email/ArticleCreatedEmailListener.ts`
```typescript
import { ArticleCreatedEvent } from '@/article/application/events/ArticleCreatedEvent';
import { ArticleCollection } from '@/article/infrastructure/ArticleCollection';
import { from } from 'uuid-mongodb';
import { eventConsumer } from '@/_lib/pubSub/EventEmitterConsumer';

type Dependencies = {
  articleCollection: ArticleCollection;
};

const makeArticleCreatedEmailListener = eventConsumer<ArticleCreatedEvent.Type, Dependencies>(
  ArticleCreatedEvent,
  ({ articleCollection }) =>
    async (event) => {
      const article = await articleCollection.findOne({ _id: from(event.payload.id.value) });

      console.log(article);
    }
);

export { makeArticleCreatedEmailListener };
```

## File: `src/article/interface/http/articleController/CreateArticleHandler.ts`
```typescript
import { CreateArticle } from '@/article/application/useCases/CreateArticle';
import { makeValidator } from '@/_lib/http/validation/Validator';
import { handler } from '@/_lib/http/handler';
import { Request, Response } from 'express';
import Joi from 'types-joi';
import { HttpStatus } from '@/_lib/http/HttpStatus';

type Dependencies = {
  createArticle: CreateArticle;
};

const { getBody } = makeValidator({
  body: Joi.object({
    title: Joi.string().required(),
    content: Joi.string().required(),
  }).required(),
});

const createArticleHandler = handler(({ createArticle }: Dependencies) => async (req: Request, res: Response) => {
  const { title, content } = getBody(req);

  const articleId = await createArticle({ title, content });

  res.status(HttpStatus.CREATED).json({ id: articleId });
});

export { createArticleHandler };
```

## File: `src/article/interface/http/articleController/definitions.yaml`
```yaml
definitions:
  ArticleDTO:
    type: object
    properties:
      id:
        type: string
      title:
        type: string
      content:
        type: string
```

## File: `src/article/interface/http/articleController/DeleteArticleHandler.ts`
```typescript
import { DeleteArticle } from '@/article/application/useCases/DeleteArticle';
import { handler } from '@/_lib/http/handler';

type Dependencies = {
  deleteArticle: DeleteArticle;
};

const deleteArticleHandler = handler(({ deleteArticle }: Dependencies) => async (req, res) => {
  const { articleId } = req.params;

  await deleteArticle(articleId);

  res.sendStatus(204);
});

export { deleteArticleHandler };
```

## File: `src/article/interface/http/articleController/FindArticlesHandler.ts`
```typescript
import { FindArticles } from '@/article/application/query/FindArticles';
import { handler } from '@/_lib/http/handler';
import Joi from 'types-joi';
import { makePaginator } from '@/_lib/http/validation/Paginator';

type Dependencies = {
  findArticles: FindArticles;
};

const { getFilter, getPagination, getSorter } = makePaginator({
  filter: Joi.object({
    title: Joi.string(),
    publishedBetween: Joi.array().items(Joi.date().iso().required()).min(2).max(2),
  }),
});

const findArticlesHandler = handler(({ findArticles }: Dependencies) => async (req, res) => {
  const filter = getFilter(req);
  const pagination = getPagination(req);
  const sort = getSorter(req);

  const articles = await findArticles({
    filter,
    sort,
    pagination,
  });

  res.json(articles);
});

export { findArticlesHandler };
```

## File: `src/article/interface/http/articleController/index.ts`
```typescript
import { deleteArticleHandler } from '@/article/interface/http/articleController/DeleteArticleHandler';
import { Router } from 'express';
import { createArticleHandler } from './CreateArticleHandler';
import { findArticlesHandler } from './FindArticlesHandler';
import { publishArticleHandler } from './PublishArticleHandler';

type Dependencies = {
  apiRouter: Router;
};

const makeArticleController = ({ apiRouter }: Dependencies) => {
  const router = Router();

  /**
   * @swagger
   *
   * /articles:
   *   get:
   *     tags:
   *       - Articles
   *     summary: The list of published articles
   *     produces:
   *       - application/json
   *     responses:
   *       200:
   *         description: List of published articles
   *         schema:
   *           type: array
   *           items:
   *             $ref: '#/definitions/ArticleDTO'
   */
  router.get('/articles', findArticlesHandler);
  router.post('/articles', createArticleHandler);
  router.delete('/articles/:articleId', deleteArticleHandler);
  router.patch('/articles/:articleId/publish', publishArticleHandler);

  apiRouter.use(router);
};

export { makeArticleController };
```

## File: `src/article/interface/http/articleController/PublishArticleHandler.ts`
```typescript
import { PublishArticle } from '@/article/application/useCases/PublishArticle';
import { handler } from '@/_lib/http/handler';
import { Request, Response } from 'express';

type Dependencies = {
  publishArticle: PublishArticle;
};

const publishArticleHandler = handler(({ publishArticle }: Dependencies) => async (req: Request, res: Response) => {
  const { articleId } = req.params;

  await publishArticle(articleId);

  res.sendStatus(204);
});

export { publishArticleHandler };
```

## File: `src/article/__tests__/integration/interface/http/ArticleController.spec.ts`
```typescript
import { randomBytes } from 'crypto';
import { makeTestControls, TestControls } from '@/__tests__/TestControls';

describe('ArticleController', () => {
  let controls: TestControls;

  beforeAll(async () => {
    controls = await makeTestControls();
  });

  beforeEach(async () => {
    const { clearDatabase } = controls;

    await clearDatabase();
  });

  afterAll(async () => {
    const { cleanUp } = controls;

    await cleanUp();
  });

  describe('POST /api/articles', () => {
    it('should create a new Article', async () => {
      const {
        request,
        registry: { articleRepository },
      } = controls;

      const title = randomBytes(20).toString('hex');
      const content = 'New Article content';

      return request()
        .post('/api/articles')
        .send({
          title,
          content,
        })
        .expect(async (res) => {
          expect(res.status).toBe(201);
          expect(res.body).toHaveProperty('id');

          const article = await articleRepository.findById(res.body.id);

          expect(article).toEqual(
            expect.objectContaining({
              title,
              content,
            })
          );
        });
    });

    it('should fail with 422 when no title is present', async () => {
      const { request } = controls;

      return request()
        .post('/api/articles')
        .send({
          content: 'New Article content',
        })
        .expect((res) => {
          expect(res.status).toBe(422);
        });
    });

    it('should fail with 422 when no content is present', async () => {
      const { request } = controls;

      return request()
        .post('/api/articles')
        .send({
          title: randomBytes(20).toString('hex'),
        })
        .expect((res) => {
          expect(res.status).toBe(422);
        });
    });
  });
});
```

## File: `src/article/__tests__/unit/application/CreateArticle.test.ts`
```typescript
import { ArticleCreatedEvent } from '@/article/application/events/ArticleCreatedEvent';
import { CreateArticle, makeCreateArticle } from '@/article/application/useCases/CreateArticle';
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { Publisher } from '@/_lib/events/Publisher';

describe('CreateArticle', () => {
  const id = 'mock-article-id';
  const title = 'Title';
  const content = 'Some content';

  const articleRepository: ArticleRepository = {
    findById: jest.fn(),
    store: jest.fn(),
    getNextId: jest.fn().mockReturnValue(Promise.resolve({ value: id })),
  };

  const publisher: Publisher = {
    publish: jest.fn(),
  };

  let createArticle: CreateArticle;

  beforeEach(async () => {
    jest.clearAllMocks();
    createArticle = makeCreateArticle({ articleRepository, eventEmitterPubSub: publisher });
  });

  it('should return the created id', async () => {
    const result = await createArticle({ title, content });

    expect(result).toBe(id);
  });

  it('should store the article', async () => {
    await createArticle({ title, content });

    expect(articleRepository.store).toHaveBeenCalledWith(
      expect.objectContaining({
        id: { value: id },
        title,
        content,
      })
    );
  });

  it('should enqueue ArticleCreatedEvent', async () => {
    await createArticle({ title, content });

    expect(publisher.publish).toHaveBeenCalledWith(
      expect.objectContaining({
        eventType: ArticleCreatedEvent.eventType,
        topic: ArticleCreatedEvent.topic,
        payload: expect.objectContaining({
          id: { value: id },
          title,
          content,
        }),
      })
    );
  });
});
```

## File: `src/article/__tests__/unit/application/DeleteArticle.test.ts`
```typescript
import { DeleteArticle, makeDeleteArticle } from '@/article/application/useCases/DeleteArticle';
import { Article } from '@/article/domain/Article';
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { BaseError } from '@/_lib/errors/BaseError';
import { NotFoundError } from '@/_lib/errors/NotFoundError';

describe('DeleteArticle', () => {
  const id = 'mock-article-id';
  const title = 'Title';
  const content = 'Some content';

  const articleRepository: ArticleRepository = {
    findById: jest.fn().mockImplementation(async (articleId) => {
      if (articleId !== id) {
        throw NotFoundError.create(articleId);
      }

      return Article.create({
        id: { value: id },
        title,
        content,
      });
    }),
    store: jest.fn(),
    getNextId: jest.fn(),
  };

  let deleteArticle: DeleteArticle;

  beforeEach(async () => {
    jest.clearAllMocks();
    deleteArticle = makeDeleteArticle({ articleRepository });
  });

  it('should save the article as deleted', async () => {
    await deleteArticle(id);

    expect(articleRepository.store).toHaveBeenCalledWith(
      expect.objectContaining({
        id: { value: id },
        state: 'DELETED',
      })
    );
  });

  it('should throw error if not found', async () => {
    await expect(deleteArticle('some-wrong-id')).rejects.toThrowError(BaseError);
  });
});
```

## File: `src/article/__tests__/unit/application/PublishArticle.test.ts`
```typescript
import { makePublishArticle, PublishArticle } from '@/article/application/useCases/PublishArticle';
import { Article } from '@/article/domain/Article';
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { BaseError } from '@/_lib/errors/BaseError';
import { NotFoundError } from '@/_lib/errors/NotFoundError';
import pino from 'pino';

describe('DeleteArticle', () => {
  const id = 'mock-article-id';
  const title = 'Title';
  const content = 'Some content';

  const articleRepository: ArticleRepository = {
    findById: jest.fn().mockImplementation(async (articleId) => {
      if (articleId !== id) {
        throw NotFoundError.create(articleId);
      }

      return Article.create({
        id: { value: id },
        title,
        content,
      });
    }),
    store: jest.fn(),
    getNextId: jest.fn(),
  };

  let publishArticle: PublishArticle;

  beforeEach(async () => {
    jest.clearAllMocks();
    publishArticle = makePublishArticle({
      articleRepository,
      logger: pino(),
      messageBundle: { getMessage: jest.fn(), useBundle: jest.fn(), updateBundle: jest.fn() },
    });
  });

  it('should save the article as published', async () => {
    await publishArticle(id);

    expect(articleRepository.store).toHaveBeenCalledWith(
      expect.objectContaining({
        id: { value: id },
        state: 'PUBLISHED',
      })
    );
  });

  it('should throw error if not found', async () => {
    await expect(publishArticle('some-wrong-id')).rejects.toThrowError(BaseError);
  });
});
```

## File: `src/comment/index.ts`
```typescript
import { CreateComment, makeCreateComment } from '@/comment/application/useCases/CreateComment';
import { CommentRepository } from '@/comment/domain/CommentRepository';
import { CommentCollection, initCommentCollection } from '@/comment/infrastructure/CommentCollection';
import { makeMongoCommentRepository } from '@/comment/infrastructure/MongoCommentRepository';
import { makeCommentController } from '@/comment/interface/http/commentController';
import { makeModule } from '@/context';
import { withMongoProvider } from '@/_lib/MongoProvider';
import { toContainerValues } from '@/_lib/di/containerAdapters';
import { asFunction } from 'awilix';

const commentModule = makeModule('comment', async ({ container: { register }, initialize }) => {
  const [collections] = await initialize(
    withMongoProvider({
      commentCollection: initCommentCollection,
    })
  );

  register({
    ...toContainerValues(collections),
    commentRepository: asFunction(makeMongoCommentRepository),
    createComment: asFunction(makeCreateComment),
  });

  await initialize(makeCommentController);
});

type CommentRegistry = {
  commentCollection: CommentCollection;
  commentRepository: CommentRepository;
  createComment: CreateComment;
};

export { commentModule };
export type { CommentRegistry };
```

## File: `src/comment/application/useCases/CreateComment.ts`
```typescript
import { ArticleRepository } from '@/article/domain/ArticleRepository';
import { CommentRepository } from '@/comment/domain/CommentRepository';
import { ApplicationService } from '@/_lib/DDD';
import { Comment } from '@/comment/domain/Comment';

type Dependencies = {
  commentRepository: CommentRepository;
  articleRepository: ArticleRepository;
};

type CreateCommentDTO = Readonly<{
  body: string;
  articleId: string;
}>;

type CreateComment = ApplicationService<CreateCommentDTO, string>;

const makeCreateComment =
  ({ commentRepository, articleRepository }: Dependencies): CreateComment =>
  async (payload) => {
    const article = await articleRepository.findById(payload.articleId);

    const id = await commentRepository.getNextId();

    const comment = Comment.create({
      id,
      body: payload.body,
      articleId: article.id,
    });

    await commentRepository.store(comment);

    return id.value;
  };

export { makeCreateComment };
export type { CreateComment };
```

## File: `src/comment/domain/Comment.ts`
```typescript
import { CommentId } from '@/comment/domain/CommentId';
import { AggregateRoot } from '@/_lib/DDD';
import { ArticleId } from '@/_sharedKernel/domain/ArticleId';

namespace Comment {
  type Status = 'ACTIVE' | 'DELETED';

  type Comment = AggregateRoot<CommentId> &
    Readonly<{
      body: string;
      articleId: ArticleId;
      status: Status;
      createdAt: Date;
      updatedAt: Date;
      version: number;
    }>;

  type CommentProps = Readonly<{
    id: CommentId;
    body: string;
    articleId: ArticleId;
  }>;

  export const create = (props: CommentProps): Comment => ({
    ...props,
    status: 'ACTIVE',
    createdAt: new Date(),
    updatedAt: new Date(),
    version: 0,
  });

  export const markAsDeleted = (self: Comment): Comment => ({
    ...self,
    status: 'DELETED',
  });

  export type Type = Comment;
}

export { Comment };
```

## File: `src/comment/domain/CommentId.d.ts`
```typescript
import { AggregateId } from '@/_lib/DDD';

type CommentId = AggregateId<string>;

export { CommentId };
```

## File: `src/comment/domain/CommentRepository.d.ts`
```typescript
import { Comment } from '@/comment/domain/Comment';
import { CommentId } from '@/comment/domain/CommentId';
import { Repository } from '@/_lib/DDD';

type CommentRepository = Repository<Comment.Type> & {
  findById(id: CommentId['value']): Promise<Comment.Type>;
};

export { CommentRepository };
```

## File: `src/comment/infrastructure/CommentCollection.ts`
```typescript
import { Collection, Db } from 'mongodb';
import { MUUID } from 'uuid-mongodb';

type CommentSchema = {
  _id: MUUID;
  body: string;
  articleId: MUUID;
  status: 'ACTIVE' | 'DELETED';
  deleted: boolean;
  createdAt: Date;
  updatedAt: Date;
  version: number;
};

type CommentCollection = Collection<CommentSchema>;

const initCommentCollection = async (db: Db): Promise<CommentCollection> => {
  const collection: CommentCollection = db.collection('comment');

  await collection.createIndex({ _id: 1, version: 1 });
  await collection.createIndex({ _id: 1, deleted: 1 });

  return collection;
};

export { initCommentCollection };
export type { CommentSchema, CommentCollection };
```

## File: `src/comment/infrastructure/CommentIdProvider.ts`
```typescript
import { CommentId } from '@/comment/domain/CommentId';
import { makeIdProvider } from '@/_lib/IdProvider';

const CommentIdProvider = makeIdProvider<CommentId>('CommentId');

export { CommentIdProvider };
```

## File: `src/comment/infrastructure/CommentMapper.ts`
```typescript
import { Comment } from '@/comment/domain/Comment';
import { CommentSchema } from '@/comment/infrastructure/CommentCollection';
import { CommentIdProvider } from '@/comment/infrastructure/CommentIdProvider';
import { DataMapper } from '@/_lib/DDD';
import { ArticleIdProvider } from '@/_sharedKernel/infrastructure/ArticleIdProvider';
import { from } from 'uuid-mongodb';

const CommentMapper: DataMapper<Comment.Type, CommentSchema> = {
  toData: (entity) => ({
    _id: from(entity.id.value),
    body: entity.body,
    articleId: from(entity.articleId.value),
    status: entity.status,
    deleted: entity.status === 'DELETED',
    createdAt: entity.createdAt,
    updatedAt: entity.updatedAt,
    version: entity.version,
  }),
  toEntity: (data) => ({
    id: CommentIdProvider.create(from(data._id).toString()),
    body: data.body,
    articleId: ArticleIdProvider.create(from(data.articleId).toString()),
    status: data.status,
    createdAt: data.createdAt,
    updatedAt: data.createdAt,
    version: data.version,
  }),
};

export { CommentMapper };
```

## File: `src/comment/infrastructure/MongoCommentRepository.ts`
```typescript
import { Comment } from '@/comment/domain/Comment';
import { CommentId } from '@/comment/domain/CommentId';
import { CommentRepository } from '@/comment/domain/CommentRepository';
import { CommentCollection } from '@/comment/infrastructure/CommentCollection';
import { CommentIdProvider } from '@/comment/infrastructure/CommentIdProvider';
import { CommentMapper } from '@/comment/infrastructure/CommentMapper';
import { NotFoundError } from '@/_lib/errors/NotFoundError';
import { ArticleIdProvider } from '@/_sharedKernel/infrastructure/ArticleIdProvider';
import { from, v4 } from 'uuid-mongodb';

type Dependencies = {
  commentCollection: CommentCollection;
};

const makeMongoCommentRepository = ({ commentCollection }: Dependencies): CommentRepository => ({
  async getNextId(): Promise<CommentId> {
    return Promise.resolve(CommentIdProvider.create(v4().toString()));
  },
  async findById(id: string): Promise<Comment.Type> {
    const comment = await commentCollection.findOne({ _id: from(id), deleted: false });

    if (!comment) {
      throw NotFoundError.create('Comment not found');
    }

    return CommentMapper.toEntity(comment);
  },
  async store(entity: Comment.Type): Promise<void> {
    CommentIdProvider.validate(entity.id);
    ArticleIdProvider.validate(entity.articleId);

    const { _id, version, ...data } = CommentMapper.toData(entity);

    const count = await commentCollection.countDocuments({ _id });

    if (count) {
      await commentCollection.updateOne(
        { _id, version, deleted: false },
        {
          $set: {
            ...data,
            updatedAt: new Date(),
            version: version + 1,
          },
        }
      );

      return;
    }

    await commentCollection.insertOne({
      _id,
      ...data,
      version,
    });
  },
});

export { makeMongoCommentRepository };
```

## File: `src/comment/interface/http/commentController/CreateCommentHandler.ts`
```typescript
import { CreateComment } from '@/comment/application/useCases/CreateComment';
import { makeValidator } from '@/_lib/http/validation/Validator';
import { handler } from '@/_lib/http/handler';
import Joi from 'types-joi';

type Dependencies = {
  createComment: CreateComment;
};

const { getBody, getParams } = makeValidator({
  params: Joi.object({
    articleId: Joi.string().required(),
  }).required(),
  body: Joi.object({
    body: Joi.string().required(),
  }).required(),
});

const createCommentHandler = handler(({ createComment }: Dependencies) => async (req, res) => {
  const { body } = getBody(req);
  const { articleId } = getParams(req);

  const id = await createComment({ body, articleId });

  res.json({ id });
});

export { createCommentHandler };
```

## File: `src/comment/interface/http/commentController/index.ts`
```typescript
import { createCommentHandler } from '@/comment/interface/http/commentController/CreateCommentHandler';
import { Router } from 'express';

type Dependencies = {
  apiRouter: Router;
};

const makeCommentController = ({ apiRouter }: Dependencies) => {
  const router = Router();

  router.post('/articles/:articleId/comments', createCommentHandler);

  apiRouter.use(router);
};

export { makeCommentController };
```

## File: `src/_boot/appModules.ts`
```typescript
import { articleModule, ArticleRegistry } from '@/article';
import { commentModule, CommentRegistry } from '@/comment';

// eslint-disable-next-line @typescript-eslint/ban-types
type AppModulesConfig = {};

const appModules = [articleModule, commentModule];

type AppModulesRegistry = ArticleRegistry & CommentRegistry;

export { appModules };
export type { AppModulesConfig, AppModulesRegistry };
```

## File: `src/_boot/database.ts`
```typescript
import { makeModule } from '@/context';
import { makeMongoProvider, MongoProvider } from '@/_lib/MongoProvider';
import { asValue } from 'awilix';
import { Db, MongoClient } from 'mongodb';

type DatabaseConfig = {
  mongodb: {
    database: string;
    host: string;
    username: string;
    password: string;
  };
};

const database = makeModule('database', async ({ container: { register }, config: { mongodb } }) => {
  const client = new MongoClient(mongodb.host, {
    auth: { username: mongodb.username, password: mongodb.password },
  });

  await client.connect();

  const db = client.db(mongodb.database);

  const mongoProvider = makeMongoProvider({ db });

  register({
    mongo: asValue(db),
    mongoProvider: asValue(mongoProvider),
  });

  return async () => {
    await client.close();
  };
});

type DatabaseRegistry = {
  mongo: Db;
  mongoProvider: MongoProvider;
};

export { database };
export type { DatabaseRegistry, DatabaseConfig };
```

## File: `src/_boot/index.ts`
```typescript
import { server, ServerConfig, ServerRegistry } from '@/_boot/server';
import { appModules, AppModulesConfig, AppModulesRegistry } from '@/_boot/appModules';
import { asValue } from 'awilix';
import { database, DatabaseConfig, DatabaseRegistry } from '@/_boot/database';
import { repl, REPLConfig } from '@/_boot/repl';
import { withContext } from '@/context';
import { Configuration } from '@/config';
import { Logger } from 'pino';
import { pubSub, PubSubRegistry } from '@/_boot/pubSub';
import { swagger, SwaggerConfig } from '@/_boot/swagger';
import { EnvironmentConfig } from '@/_lib/Environment';
import { ContextApp } from '@/_lib/Context';
import { Container, Initialize } from '@/container';

type MainConfig = ServerConfig & DatabaseConfig & EnvironmentConfig & REPLConfig & SwaggerConfig & AppModulesConfig;

const main = withContext(async ({ app, container, config, bootstrap, logger, initialize }) => {
  container.register({
    app: asValue(app),
    initialize: asValue(initialize),
    container: asValue(container),
    logger: asValue(logger),
    startedAt: asValue(new Date()),
    config: asValue(config),
  });

  await bootstrap(database, server, swagger, pubSub, repl, ...appModules);
});

type MainRegistry = {
  app: ContextApp;
  container: Container;
  initialize: Initialize;
  startedAt: Date;
  logger: Logger;
  config: Configuration;
} & DatabaseRegistry &
  ServerRegistry &
  PubSubRegistry &
  AppModulesRegistry;

export { main };
export type { MainConfig, MainRegistry };
```

## File: `src/_boot/pubSub.ts`
```typescript
import { makeModule } from '@/context';
import { makeEventEmitterPubSub } from '@/_lib/pubSub/EventEmitterPubSub';
import { asValue } from 'awilix';
import { Subscriber } from '@/_lib/events/Subscriber';
import { Publisher } from '@/_lib/events/Publisher';

const pubSub = makeModule('pubSub', async ({ container: { build, register }, app: { onReady } }) => {
  const eventEmitterPubSub = build(makeEventEmitterPubSub);

  register({
    eventEmitterPubSub: asValue(eventEmitterPubSub),
  });

  onReady(async () => {
    await eventEmitterPubSub.start();
  });

  return async () => {
    await eventEmitterPubSub.dispose();
  };
});

type PubSubRegistry = {
  eventEmitterPubSub: Publisher & Subscriber;
};

export { pubSub };
export type { PubSubRegistry };
```

## File: `src/_boot/repl.ts`
```typescript
import { makeModule } from '@/context';
import { makeREPL } from '@/_lib/repl';

type REPLConfig = { appName: string; environment: string; cli: boolean; repl: { port: number } };

const repl = makeModule('repl', async ({ app: { onReady, terminate }, container, config, logger }) => {
  const repl = makeREPL({
    context: { registry: container.cradle, container },
    cli: config.cli,
    prompt: config.appName,
    remote: !['production', 'test'].includes(config.environment) && config.repl,
    logger,
  });

  onReady(async () => {
    await repl.start({ terminate });
  });

  return async () => {
    await repl.close();
  };
});

export { repl };
export type { REPLConfig };
```

## File: `src/_boot/server.ts`
```typescript
import { makeModule } from '@/context';
import { errorHandler } from '@/_lib/http/middlewares/errorHandler';
import { gracefulShutdown } from '@/_lib/http/middlewares/gracefulShutdown';
import { httpLogger, reqStartTimeKey } from '@/_lib/http/middlewares/httpLogger';
import { requestContainer } from '@/_lib/http/middlewares/requestContainer';
import { statusHandler } from '@/_lib/http/middlewares/statusHandler';
import { errorConverters } from '@/_sharedKernel/interface/http/ErrorConverters';
import { asValue } from 'awilix';
import cors, { CorsOptions } from 'cors';
import express, { Application, json, Router, urlencoded } from 'express';
import helmet from 'helmet';
import { createServer, Server } from 'http';

type ServerConfig = {
  http: {
    host: string;
    port: number;
    cors?: boolean | CorsOptions;
  };
};

const server = makeModule(
  'server',
  async ({ app: { onBooted, onReady }, container, config: { cli, http, environment }, logger }) => {
    const { register } = container;
    const server = express();

    const httpServer = createServer(server);

    const { shutdownHook, shutdownHandler } = gracefulShutdown(httpServer);

    server.use((req, res, next) => {
      res[reqStartTimeKey] = Date.now();

      next();
    });

    server.use(shutdownHandler());

    if (http.cors) {
      server.use(cors(typeof http.cors !== 'boolean' ? http.cors : {}));
    }

    server.use(httpLogger());
    server.use(requestContainer(container));
    server.use(helmet());
    server.use(json());
    server.use(urlencoded({ extended: false }));

    const rootRouter = Router();
    const apiRouter = Router();

    rootRouter.get('/status', statusHandler);
    rootRouter.use('/api', apiRouter);

    server.use(rootRouter);

    onBooted(async () => {
      server.use((_, res) => {
        res.sendStatus(404);
      });

      server.use(errorHandler(errorConverters, { logger }));
    });

    if (!cli && environment !== 'test') {
      onReady(
        async () =>
          new Promise<void>((resolve) => {
            httpServer.listen(http.port, http.host, () => {
              logger.info(`Webserver listening at: http://${http.host}:${http.port}`);
              resolve();
            });
          })
      );
    }

    register({
      requestId: asValue(undefined),
      server: asValue(server),
      httpServer: asValue(httpServer),
      rootRouter: asValue(rootRouter),
      apiRouter: asValue(apiRouter),
    });

    return async () => {
      await shutdownHook();
    };
  }
);

type ServerRegistry = {
  requestId?: string;
  server: Application;
  httpServer: Server;
  rootRouter: Router;
  apiRouter: Router;
};

export { server };
export type { ServerRegistry, ServerConfig };
```

## File: `src/_boot/swagger.ts`
```typescript
import { makeModule } from '@/context';
import { resolve } from 'path';
import swaggerJSDoc from 'swagger-jsdoc';
import swaggerUi from 'swagger-ui-express';

type SwaggerConfig = {
  swagger: {
    title: string;
    version: string;
    basePath: string;
    docEndpoint: string;
  };
};

const swagger = makeModule('swagger', async ({ container: { build }, config: { http, swagger } }) => {
  const options = {
    swaggerDefinition: {
      info: {
        title: swagger.title,
        version: swagger.version,
      },
      basePath: swagger.basePath,
    },
    apis: [resolve(__dirname, '../**/interface/http/**/*.yaml'), resolve(__dirname, '../**/interface/http/**/*.ts')],
  };

  // Initialize swagger-jsdoc -> returns validated swagger spec in json format
  const swaggerSpec = swaggerJSDoc(options);

  build(({ server }) => {
    server.use(swagger.docEndpoint, swaggerUi.serve, swaggerUi.setup(swaggerSpec, { explorer: true }));
  });
});

export { swagger };
export type { SwaggerConfig };
```

## File: `src/_lib/Application.ts`
```typescript
type HookFn = () => Promise<void>;

type HookStore = {
  get: (lifecycle: Lifecycle) => HookFn[];
  append: (lifecycle: Lifecycle, ...fn: HookFn[]) => void;
  prepend: (lifecycle: Lifecycle, ...fn: HookFn[]) => void;
};

enum Lifecycle {
  BOOTING = 'BOOTING',
  BOOTED = 'BOOTED',
  READY = 'READY',
  RUNNING = 'RUNNING',
  DISPOSING = 'DISPOSING',
  DISPOSED = 'DISPOSED',
}

type LifecycleHooks = {
  [key in `on${Capitalize<Lowercase<keyof typeof Lifecycle>>}`]: (
    fn: HookFn | HookFn[],
    order?: 'append' | 'prepend'
  ) => void;
};

type Application = {
  getState: () => AppState;
  start: () => Promise<void>;
  stop: () => Promise<void>;
  terminate: () => void;
  decorateHooks: (decorator?: (lifecycle: Lifecycle, fn: HookFn | HookFn[]) => HookFn | HookFn[]) => Application;
} & LifecycleHooks;

type ApplicationOptions = {
  shutdownTimeout: number;
  logger: Pick<Console, 'info' | 'error' | 'warn'>;
};

const makeApp = ({ logger, shutdownTimeout }: ApplicationOptions): Application => {
  let appState: AppState = AppState.IDLE;
  let release: null | (() => void);

  const hooks = makeHookStore();

  const started: HookFn = () =>
    new Promise<void>((resolve) => {
      logger.info('Application started');

      appState = AppState.STARTED;

      release = resolve;
    });

  const status = (newStatus: AppState) => async () => {
    appState = newStatus;
  };

  const transition = (lifecycle: Lifecycle) => () => promiseChain(hooks.get(lifecycle));

  const start = memo(async () => {
    if (appState !== AppState.IDLE) throw new Error('The application has already started.');

    logger.info('Starting application');

    try {
      await promiseChain([
        status(AppState.STARTING),
        transition(Lifecycle.BOOTING),
        transition(Lifecycle.BOOTED),
        transition(Lifecycle.READY),
        transition(Lifecycle.RUNNING),
        started,
      ]);
    } catch (err) {
      logger.error(err);

      await stop();
    }
  });

  const stop = memo(async () => {
    if (appState === AppState.IDLE) throw new Error('The application is not running.');

    if (release) {
      release();
      release = null;
    }

    logger.info('Stopping application');

    await promiseChain([
      status(AppState.STOPPING),
      transition(Lifecycle.DISPOSING),
      transition(Lifecycle.DISPOSED),
      status(AppState.STOPPED),
    ]);

    setTimeout(() => {
      logger.warn(
        'The stop process has finished but something is keeping the application from exiting. ' +
          'Check your cleanup process!'
      );
    }, 5000).unref();
  });

  let forceShutdown = false;

  const shutdown = (code: number) => async () => {
    process.stdout.write('\n');

    setTimeout(() => {
      logger.error('Ok, my patience is over! #ragequit');
      process.exit(code);
    }, shutdownTimeout).unref();

    if ((appState === AppState.STOPPING || appState === AppState.STOPPED) && code === 0) {
      if (forceShutdown) {
        process.kill(process.pid, 'SIGKILL');
      }

      logger.warn('The application is yet to finishing the shutdown process. Repeat the command to force exit');
      forceShutdown = true;
      return;
    }

    try {
      await stop();
    } catch (err) {
      logger.error(err);
    }

    process.exit(code);
  };

  const terminate = () => process.kill(process.pid, 'SIGTERM');

  process.on('SIGTERM', shutdown(0));
  process.on('SIGINT', shutdown(0));
  process.on('uncaughtException', shutdown(1));
  process.on('unhandledRejection', shutdown(1));

  const lifecycleHooks = (
    decorator: (lifecycle: Lifecycle, fn: HookFn | HookFn[]) => HookFn | HookFn[] = (lifecycle, fn) => fn
  ) => {
    const once = (lifecycle, fn, order = 'append') => {
      const decoratedFn = decorator(lifecycle, fn);
      Array.isArray(decoratedFn) ? hooks[order](lifecycle, ...decoratedFn) : hooks[order](lifecycle, decoratedFn);
    };
    return Object.keys(Lifecycle).reduce(
      (acc, hook) => ({
        ...acc,
        [`on${capitalize(hook)}`]: (fn: HookFn | HookFn[], order?: 'append' | 'prepend') =>
          once(Lifecycle[hook], fn, order),
      }),
      {}
    ) as unknown as LifecycleHooks;
  };

  const application: Application = {
    start,
    stop,
    terminate,
    getState: () => appState,
    decorateHooks: (decorator?): Application => ({
      ...application,
      ...lifecycleHooks(decorator),
    }),
    ...lifecycleHooks(),
  };

  return application;
};

enum AppState {
  IDLE = 'IDLE',
  STARTING = 'STARTING',
  STARTED = 'STARTED',
  STOPPING = 'STOPPING',
  STOPPED = 'STOPED',
}

const capitalize = (str: string) => str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();

const memo = <F extends (...args: any[]) => any>(fn: F) => {
  let value: ReturnType<F>;

  return (...args: Parameters<F>): ReturnType<F> => {
    if (!value) {
      value = fn(args);
    }

    return value;
  };
};

const promiseChain = <M extends HookFn[]>(hooksFns: M) => {
  return hooksFns.reduce((chain, fn) => chain.then(fn), Promise.resolve());
};

const makeHookStore = (): HookStore => {
  const hooks = new Map<Lifecycle, HookFn[]>();

  const get = (lifecycle: Lifecycle) => hooks.get(lifecycle) || [];

  const append = (lifecycle: Lifecycle, ...fn: HookFn[]) => hooks.set(lifecycle, [...get(lifecycle), ...fn]);

  const prepend = (lifecycle: Lifecycle, ...fn: HookFn[]) => hooks.set(lifecycle, [...fn, ...get(lifecycle)]);

  return {
    get,
    append,
    prepend,
  };
};

export { makeApp };
export type { Application, HookFn };
```

## File: `src/_lib/Context.ts`
```typescript
import { Application, HookFn, makeApp } from '@/_lib/Application';

type EntrypointFn<T extends Record<string | symbol, any>> = (arg: Context<T>) => Promise<void>;

type BootFn<T extends Record<string | symbol, any>> = (arg: Context<T>) => Promise<void | HookFn>;

type Module<T extends Record<string | symbol, any>, F extends BootFn<T> = BootFn<any>> = {
  name: string;
  fn: F;
};

type ContextApp = Omit<Application, 'start' | 'onBooting'>;

type Context<T extends Record<string | symbol, any>> = {
  app: ContextApp;
  bootstrap: <M extends Module<T>[]>(...modules: M) => Promise<void>;
} & T;

type ContextProvider<T extends Record<string | symbol, any>> = {
  makeModule: <F extends BootFn<T>, M extends Module<F>>(name: string, fn: F) => M;
  withContext: <F extends EntrypointFn<T>>(fn: F) => () => Promise<void>;
};

type ContextOptions = {
  shutdownTimeout: number;
  logger: Pick<Console, 'info' | 'error' | 'warn'>;
};

const defaultOptions: ContextOptions = {
  shutdownTimeout: 5000,
  logger: console,
};

const makeContext = <T extends Record<string | symbol, any>>(
  localContext: T,
  opts: Partial<ContextOptions> = {}
): ContextProvider<T> => {
  const { shutdownTimeout, logger } = { ...defaultOptions, ...opts };
  const moduleKey = Symbol();

  const app = makeApp({ shutdownTimeout, logger });

  const bootstrap = async <M extends Module<T>[]>(...modules: M): Promise<void> => {
    if (!modules.every((module) => module[moduleKey])) {
      const foreignModules = modules.filter((module) => !module[moduleKey]).map((module) => module.name);
      throw new Error(`Foreign module(s) provided for bootstrap function: ${foreignModules.join(', ')}`);
    }

    const bootOrder = modules.map(({ name, fn }) => async () => {
      logger.info(`Bootstraping ${name} module.`);

      const result = await fn(
        Object.freeze({
          ...context,
          app: app.decorateHooks((lifecycle, fn) => async () => {
            const isArray = Array.isArray(fn);

            logger.info(`Running ${lifecycle.toLowerCase()} hook${isArray ? 's' : ''} from ${name} module.`);

            return (Array.isArray(fn) ? fn : [fn]).reduce(
              (chain, hook) =>
                chain.then(() =>
                  hook().catch((err) => {
                    logger.error(
                      `Error while performing ${lifecycle.toLowerCase()} hook${isArray ? 's' : ''} from ${name} module.`
                    );
                    logger.error(err);
                  })
                ),
              Promise.resolve()
            );
          }),
        })
      );

      if (typeof result === 'function') {
        app.onDisposing(async () => {
          logger.info(`Disposing ${name} module.`);

          return result().catch((err) => {
            logger.error(`Error while disposing of ${name} module. Trying to resume teardown`);
            logger.error(err);
          });
        }, 'prepend');
      }
    });

    app.onBooting(bootOrder);

    return app.start();
  };

  const context: Context<T> = {
    ...localContext,
    app,
    bootstrap,
  };

  return {
    makeModule: <F extends BootFn<T>, M extends Module<F>>(name: string, fn: F): M =>
      ({
        [moduleKey]: true,
        name,
        fn,
      } as unknown as M),
    withContext:
      <F extends EntrypointFn<T>>(fn: F): (() => Promise<void>) =>
      () =>
        fn(Object.freeze(context)),
  };
};

export { makeContext };
export type { ContextApp };
```

## File: `src/_lib/CQRS.d.ts`
```typescript
type Sort = Readonly<{
  field: string;
  direction: 'asc' | 'desc';
}>;

type Pagination = Readonly<{
  page: number;
  pageSize: number;
}>;

type ResultPage = Readonly<{
  current: number;
  pageSize: number;
  totalPages: number;
  totalElements: number;
  first: boolean;
  last: boolean;
}>;

type Filter = Record<string, any>;

type Query<F = void> = F extends Filter
  ? Readonly<{
      filter: F;
    }>
  : never;

type PaginatedQuery<F = void> = Query<F> &
  Readonly<{
    pagination: Pagination;
  }>;

type SortedQuery<F = void> = Query<F> &
  Readonly<{
    sort: Sort[];
  }>;

type SortedPaginatedQuery<F = void> = Query<F> &
  Readonly<{
    sort: Sort[];
    pagination: Pagination;
  }>;

type QueryResult<T> = Readonly<{
  data: T;
}>;

type PaginatedQueryResult<T> = QueryResult<T> &
  Readonly<{
    page: ResultPage;
  }>;

type QueryHandler<P extends Query<any> | void, R extends QueryResult<any>> = (payload: P) => Promise<R>;

export { Query, PaginatedQuery, SortedQuery, SortedPaginatedQuery, QueryResult, PaginatedQueryResult, QueryHandler };
```

## File: `src/_lib/DDD.d.ts`
```typescript
type AggregateId<T> = {
  value: T;
};

type AggregateRoot<ID extends AggregateId<any>> = {
  readonly id: ID;
};

type Repository<T extends AggregateRoot<any>, ID extends AggregateId<any> = T['id']> = {
  getNextId(): Promise<ID>;
  store(entity: T): Promise<void>;
};

type ApplicationService<P, R> = (payload: P) => Promise<R>;

type DataMapper<AR extends AggregateRoot<any>, DATA> = {
  toEntity(data: DATA): AR;
  toData(entity: AR): DATA;
};

export { AggregateId, AggregateRoot, Repository, ApplicationService, DataMapper };
```

## File: `src/_lib/Environment.ts`
```typescript
import dotenv from 'dotenv';
import { existsSync } from 'fs';

dotenv.config({
  path:
    process.env.NODE_ENV === 'production'
      ? '.env'
      : existsSync(`.env.${process.env.NODE_ENV}.local`)
      ? `.env.${process.env.NODE_ENV}.local`
      : `.env.${process.env.NODE_ENV}`,
});

const environments = ['development', 'production', 'test'] as const;

type EnvironmentTypes = typeof environments[number];

type EnvironmentConfig = {
  environment: EnvironmentTypes;
};

const environment = (defaultValue: EnvironmentTypes = 'development'): EnvironmentTypes => {
  let env: any = process.env.NODE_ENV;

  if (!env) {
    env = process.env.NODE_ENV = defaultValue;
  }

  if (!environments.includes(env)) {
    throw new TypeError(`Invalid value for NODE_ENV variable. Accepted values are: ${environments.join(' | ')}.`);
  }

  return env;
};

const envString = (variable: string, defaultValue?: string): string => {
  const value = process.env[variable] || defaultValue;

  if (value == null) {
    throw new TypeError(`Required environment variable ${variable} is undefined and has no default`);
  }

  return value;
};

const envNumber = (variable: string, defaultValue?: number): number => {
  const value = Number(process.env[variable]) || defaultValue;

  if (value == null) {
    throw new TypeError(`Required environment variable ${variable} is undefined and has no default`);
  }

  return value;
};

export { environment, envString, envNumber };
export type { EnvironmentConfig };
```

## File: `src/_lib/IdProvider.ts`
```typescript
import { AggregateId } from '@/_lib/DDD';

type IdProvider<T extends AggregateId<N>, N = T['value']> = {
  create(id: N): T;
  ensure(id: T): id is T;
  validate(id: T): void;
};

const makeIdProvider = <T extends AggregateId<N>, N = T['value']>(idName: string): IdProvider<T, N> => {
  const key = Symbol();

  return {
    create: (id: N): T =>
      ({
        value: id,
        [key]: true,
      } as unknown as T),
    ensure: (id: T | any): id is T => Boolean(id[key]),
    validate: (id: T) => {
      if (!id[key]) {
        throw new TypeError(`${id.value} is not a valid ${idName}`);
      }
    },
  };
};

export { makeIdProvider };
export type { IdProvider };
```

## File: `src/_lib/Initialize.ts`
```typescript
type InitFn<R, T, OPTS = void> = (deps: R, opts?: OPTS) => T;
type BuilderFn<R, OPTS = void> = <T>(fn: InitFn<R, T, OPTS>) => T;
type ThenArg<T extends (...args: any[]) => Promise<any>> = ReturnType<T> extends PromiseLike<infer U>
  ? U
  : ReturnType<T>;

type Initialize<R, OPTS = void> = <T extends Array<InitFn<R, unknown, OPTS>>>(
  ...fns: T
) => Promise<{ [i in keyof T]: T[i] extends (...args) => any ? ThenArg<T[i]> : T[i] }>;

const makeInitialize =
  <R extends Record<string, any>, OPTS = void>(builderFn: BuilderFn<R, OPTS>): Initialize<R, OPTS> =>
  <T extends Array<InitFn<R, unknown, OPTS>>>(
    ...fns: T
  ): Promise<{ [i in keyof T]: T[i] extends (...args) => any ? ThenArg<T[i]> : T[i] }> =>
    fns.reduce(
      (chain, fn) =>
        chain.then((results) => Promise.resolve(builderFn(fn)).then((result) => Promise.resolve([...results, result]))),
      Promise.resolve<any[]>([])
    ) as any;

export { makeInitialize };
export type { Initialize };
```

## File: `src/_lib/MongoProvider.ts`
```typescript
import { Collection, Db } from 'mongodb';
import MUUID from 'uuid-mongodb';

MUUID.mode('relaxed');

interface Dependencies {
  db: Db;
}

type CollectionInitializer = Record<string, (db: Db) => Promise<Collection<any>>>;

type ThenArg<T> = T extends PromiseLike<infer U> ? U : T;

type MongoProvider = <Type extends CollectionInitializer>(
  collectionInitializer: Type
) => Promise<{ [key in keyof Type]: ThenArg<ReturnType<Type[key]>> }>;

type InitializedCollections<Type extends CollectionInitializer> = Promise<
  { [key in keyof Type]: ThenArg<ReturnType<Type[key]>> }
>;

const makeMongoProvider =
  ({ db }: Dependencies): MongoProvider =>
  (collections) =>
    Object.entries(collections).reduce(
      (chain: Promise<any>, [key, promise]) =>
        chain.then((acc) => promise(db).then((collection) => ({ ...acc, [key]: collection }))),
      Promise.resolve()
    );

const withMongoProvider =
  <Type extends CollectionInitializer>(collections: Type) =>
  ({ mongoProvider }: { mongoProvider: MongoProvider }): InitializedCollections<Type> =>
    mongoProvider(collections);

export { makeMongoProvider, withMongoProvider };
export type { MongoProvider };
```

## File: `src/_lib/PartializeProperties.d.ts`
```typescript
type PartializeProperties<Type, Properties extends keyof Type> = Omit<Type, Properties> &
  Partial<Pick<Type, Properties>>;

export { PartializeProperties };
```

## File: `src/_lib/Predicate.ts`
```typescript
const makePredicate =
  <T>(value: symbol | string | any, key: string | symbol = 'type') =>
  (obj: T | any): obj is T =>
    obj[key] === value;

export { makePredicate };
```

## File: `src/_lib/WithInvariants.ts`
```typescript
import { AggregateRoot } from '@/_lib/DDD';
import assertFn from 'assert';

type AssertionFn = (value: any, message?: string | Error) => void;

type InvariantCheckFn<A> = (self: A, assert: AssertionFn) => void;

const makeWithInvariants =
  <A extends AggregateRoot<any>>(invariantCheckFn: InvariantCheckFn<A>) =>
  <F extends (...args: any[]) => A>(fn: F) =>
  (...args: Parameters<F>): ReturnType<F> => {
    const self = fn(...args);
    invariantCheckFn(self, assertFn);

    return self as ReturnType<F>;
  };

export { makeWithInvariants };
export type { AssertionFn };
```

## File: `src/_lib/di/containerAdapters.ts`
```typescript
import { Resolver } from 'awilix/lib/resolvers';
import { asValue } from 'awilix';

type Values = Record<string, any>;

type ContainerValues = <Type extends Values>(values: Type) => { [key in keyof Type]: Resolver<Type[key]> };

const toContainerValues: ContainerValues = (values) =>
  Object.entries(values).reduce((acc: any, [key, value]) => ({ ...acc, [key]: asValue(value) }), {});

export { toContainerValues };
```

## File: `src/_lib/errors/BadRequestError.ts`
```typescript
import { BaseError, Exception } from '@/_lib/errors/BaseError';
import { makePredicate } from '@/_lib/Predicate';

namespace BadRequestError {
  const type = Symbol();
  const name = 'BadRequestError';
  const defaultMessage = 'Bad Request';

  export const create = (message: string = defaultMessage, code: string = name): Exception =>
    new BaseError({ type, name, code, message });

  export const is = makePredicate<Exception>(type);
}

export { BadRequestError };
```

## File: `src/_lib/errors/BaseError.ts`
```typescript
import { PartializeProperties } from '@/_lib/PartializeProperties';

type Exception<M = any> = Readonly<{
  name: string;
  type: symbol;
  message: string;
  code: string;
  meta?: M;
}>;

type Props<M = any> = PartializeProperties<Exception<M>, 'name'>;

class BaseError<M = any> extends Error implements Exception<M> {
  public readonly type: symbol;
  public readonly code: string;
  public readonly meta?: M;

  constructor(props: Props<M>) {
    super();
    this.name = props.name || props.code;
    this.type = props.type;
    this.code = props.code;
    this.meta = props.meta;
    this.message = props.message;

    Error.captureStackTrace(this, BaseError);
  }
}

export { BaseError };
export type { Exception };
```

## File: `src/_lib/errors/ForbiddenError.ts`
```typescript
import { BaseError, Exception } from '@/_lib/errors/BaseError';
import { makePredicate } from '@/_lib/Predicate';

namespace ForbiddenError {
  const type = Symbol();
  const name = 'ForbiddenError';
  const defaultMessage = 'Forbidden';

  export const create = (message: string = defaultMessage, code: string = name): Exception =>
    new BaseError({ type, name, code, message });

  export const is = makePredicate<Exception>(type);
}

export { ForbiddenError };
```

## File: `src/_lib/errors/NotFoundError.ts`
```typescript
import { BaseError, Exception } from '@/_lib/errors/BaseError';
import { makePredicate } from '@/_lib/Predicate';

namespace NotFoundError {
  const type = Symbol();
  const name = 'NotFoundError';
  const defaultMessage = 'Not Found';

  export const create = (message: string = defaultMessage, code: string = name): Exception =>
    new BaseError({ type, name, code, message });

  export const is = makePredicate<Exception>(type);
}

export { NotFoundError };
```

## File: `src/_lib/errors/UnauthorizedError.ts`
```typescript
import { BaseError, Exception } from '@/_lib/errors/BaseError';
import { makePredicate } from '@/_lib/Predicate';

namespace UnauthorizedError {
  const type = Symbol();
  const name = 'UnauthorizedError';
  const defaultMessage = 'Unauthorized';

  export const create = (message: string = defaultMessage, code: string = name): Exception =>
    new BaseError({ type, name, code, message });

  export const is = makePredicate<Exception>(type);
}

export { UnauthorizedError };
```

## File: `src/_lib/errors/ValidationError.ts`
```typescript
import Joi from 'types-joi';
import { BaseError, Exception } from '@/_lib/errors/BaseError';
import { makePredicate } from '@/_lib/Predicate';

namespace ValidationError {
  const type = Symbol();
  const name = 'ValidationError';

  type Props = {
    readonly target: string;
    readonly error: Joi.ValidationError;
  };

  export const create = ({ error, target }: Props): Exception<Props> =>
    new BaseError<Props>({ type, name, code: name, message: error.message, meta: { target, error } });

  export const is = makePredicate<Exception<Props>>(type);
}

export { ValidationError };
```

## File: `src/_lib/events/Event.d.ts`
```typescript
type EventAddress<ET extends string = string, T extends string = string> = Readonly<{
  eventType: ET;
  topic: T;
}>;

type Event<P, ET extends string = string, T extends string = string> = EventAddress<ET, T> &
  Readonly<{
    eventId: string;
    payload: P;
  }>;

export { Event, EventAddress };
```

## File: `src/_lib/events/EventConsumer.ts`
```typescript
import { Event, EventAddress } from '@/_lib/events/Event';
import { Subscriber, SubscriberOptions } from '@/_lib/events/Subscriber';

const makeEventConsumer =
  <S extends string = 'subscriber'>(subscriberKey: S = 'subscriber' as S) =>
  <E extends Event<any>, D extends Record<string, any> | void = void, OPTS = SubscriberOptions>(
    address: EventAddress<E['eventType'], E['topic']>,
    fn: (deps: D) => (event: E) => Promise<void>,
    opts: Partial<OPTS> = {}
  ) =>
  (deps: D & { [key in S]: Subscriber<OPTS> }): void => {
    const { [subscriberKey]: subscriber } = deps;

    subscriber.add(address, fn(deps), opts);
  };

const eventConsumer = makeEventConsumer();

export { eventConsumer, makeEventConsumer };
```

## File: `src/_lib/events/EventProvider.ts`
```typescript
import { ApplicationService } from '@/_lib/DDD';
import { Event } from '@/_lib/events/Event';
import { Publisher } from '@/_lib/events/Publisher';

type Enqueue = <E extends Event<any>>(event: E) => void;

type EventStore = {
  enqueue: Enqueue;
  getEvents: () => ReadonlyArray<Event<any>>;
};

const makeEventProvider =
  <S extends string = 'publisher'>(publisherKey: S = 'publisher' as S) =>
  <D extends Record<string, any>, AS extends ApplicationService<any, any>>(fn: (deps: D, enqueue: Enqueue) => AS) =>
  (deps: D & { [key in S]: Publisher }): AS => {
    const { [publisherKey]: publisher } = deps;
    const { getEvents, enqueue } = makeEventStore();

    const service = fn(deps, enqueue);

    const wrapper = async (arg) => {
      const result = await service(arg);

      getEvents().forEach((event) => publisher.publish(event));

      return result;
    };

    return wrapper as AS;
  };

const makeEventStore = (): EventStore => {
  let eventStore: Event<any>[] = [];

  return {
    enqueue: <E extends Event<any>>(event: E) => {
      eventStore = [...eventStore, event];
    },
    getEvents: () => [...eventStore],
  };
};

const eventProvider = makeEventProvider();

export { eventProvider, makeEventProvider };
```

## File: `src/_lib/events/Publisher.d.ts`
```typescript
import { Event } from '@/_lib/events/Event';

type Publisher = {
  publish: <T extends Event<any>>(event: T) => Promise<void>;
};

export { Publisher };
```

## File: `src/_lib/events/Subscriber.d.ts`
```typescript
import { Event, EventAddress } from '@/_lib/events/Event';

type SubscriberOptions = {
  single: boolean;
  nackOn: (error?: Error) => boolean;
};

type Subscriber<OPTS = SubscriberOptions> = {
  add: <E extends Event<any>>(
    address: EventAddress<E['eventType'], E['topic']>,
    handler: (event: E) => Promise<void>,
    opts?: Partial<OPTS>
  ) => Promise<void>;

  start: () => Promise<void>;

  dispose: () => Promise<void>;
};

export { Subscriber, SubscriberOptions };
```

## File: `src/_lib/http/handler.ts`
```typescript
import { RequestHandler } from 'express';
import { asFunction } from 'awilix';
import { AsyncHandler, runAsync } from '@/_lib/http/runAsync';

type ControllerHandler = (dependencies: any) => AsyncHandler;

const handler = (handler: ControllerHandler): RequestHandler => {
  const resolver = asFunction(handler);

  return (req, res, next) => {
    if (!('container' in req)) {
      throw new Error("Can't find the request container! Have you registered the `requestContainer` middleware?");
    }

    const injectedHandler = req.container.build(resolver);

    return runAsync(injectedHandler)(req, res, next);
  };
};

export { handler };
```

## File: `src/_lib/http/HttpStatus.ts`
```typescript
enum HttpStatus {
  CONTINUE = 100,
  SWITCHING_PROTOCOLS = 101,
  PROCESSING = 102,
  OK = 200,
  CREATED = 201,
  ACCEPTED = 202,
  NON_AUTHORITATIVE_INFORMATION = 203,
  NO_CONTENT = 204,
  RESET_CONTENT = 205,
  PARTIAL_CONTENT = 206,
  AMBIGUOUS = 300,
  MOVED_PERMANENTLY = 301,
  FOUND = 302,
  SEE_OTHER = 303,
  NOT_MODIFIED = 304,
  TEMPORARY_REDIRECT = 307,
  PERMANENT_REDIRECT = 308,
  BAD_REQUEST = 400,
  UNAUTHORIZED = 401,
  PAYMENT_REQUIRED = 402,
  FORBIDDEN = 403,
  NOT_FOUND = 404,
  METHOD_NOT_ALLOWED = 405,
  NOT_ACCEPTABLE = 406,
  PROXY_AUTHENTICATION_REQUIRED = 407,
  REQUEST_TIMEOUT = 408,
  CONFLICT = 409,
  GONE = 410,
  LENGTH_REQUIRED = 411,
  PRECONDITION_FAILED = 412,
  PAYLOAD_TOO_LARGE = 413,
  URI_TOO_LONG = 414,
  UNSUPPORTED_MEDIA_TYPE = 415,
  REQUESTED_RANGE_NOT_SATISFIABLE = 416,
  EXPECTATION_FAILED = 417,
  UNPROCESSABLE_ENTITY = 422,
  TOO_MANY_REQUESTS = 429,
  INTERNAL_SERVER_ERROR = 500,
  NOT_IMPLEMENTED = 501,
  BAD_GATEWAY = 502,
  SERVICE_UNAVAILABLE = 503,
  GATEWAY_TIMEOUT = 504,
  HTTP_VERSION_NOT_SUPPORTED = 505,
}

export { HttpStatus };
```

## File: `src/_lib/http/runAsync.ts`
```typescript
import { NextFunction, Request, Response } from 'express';

type AsyncHandler = (req: Request, res: Response, next: NextFunction) => Promise<any>;

const runAsync = (handler: AsyncHandler) => (req: Request, res: Response, next: NextFunction) =>
  handler(req, res, next).catch(next);

export { runAsync };
export type { AsyncHandler };
```

## File: `src/_lib/http/middlewares/errorHandler.ts`
```typescript
import { ErrorRequestHandler } from 'express';
import { Exception } from '@/_lib/errors/BaseError';

type ErrorConverter<E extends Exception> = {
  test: (err: E | any) => err is E;
  converter: (err: E) => { status: number; body: string | Record<string, any> };
};

type ErrorConverterFn = <E extends Exception>(
  test: (err: E | any) => err is E,
  converter: (err: E) => { status: number; body: string | Record<string, any> }
) => ErrorConverter<E>;

const errorConverter: ErrorConverterFn = (test, converter) => ({ test, converter });

const makeErrorResponseBuilder = (errorConverters: ErrorConverter<any>[]) => (err: any) => {
  const mapping = errorConverters.find((parser) => parser.test(err));

  return mapping ? mapping.converter(err) : null;
};

type ErrorHandlerOptions = {
  logger: Pick<Console, 'error'>;
};

const defaultOptions: ErrorHandlerOptions = {
  logger: console,
};

const errorHandler = (
  errorMap: ErrorConverter<any>[],
  options: Partial<ErrorHandlerOptions> = {}
): ErrorRequestHandler => {
  const { logger } = { ...defaultOptions, ...options };
  const errorResponseBuilder = makeErrorResponseBuilder(errorMap);

  return (err, req, res, next) => {
    logger.error(err.stack);

    const errorResponse = errorResponseBuilder(err);

    if (errorResponse) {
      const { status, body } = errorResponse;

      return res.status(status).json(typeof body === 'object' ? body : { error: body });
    }

    res.status(500).json({ error: err.message });
  };
};

export { errorHandler, errorConverter };
```

## File: `src/_lib/http/middlewares/gracefulShutdown.ts`
```typescript
import { Server } from 'http';
import { logger } from '@/_lib/logger';
import { RequestHandler } from 'express';

type ShutdownMiddleware = {
  shutdownHook: () => Promise<void>;
  shutdownHandler: () => RequestHandler;
};

const gracefulShutdown = (server: Server, forceTimeout = 30000): ShutdownMiddleware => {
  let shuttingDown = false;

  const shutdownHook = () =>
    new Promise<void>((resolve, reject) => {
      if (!process.env.NODE_ENV?.match(/^prod/i) || !server.listening) {
        return resolve();
      }

      shuttingDown = true;

      logger.warn('Shutting down server');

      setTimeout(() => {
        logger.error('Could not close connections in time, forcefully shutting down');
        resolve();
      }, forceTimeout).unref();

      server.close((err) => {
        if (err) return reject(err);

        logger.info('Closed out remaining connections.');
        resolve();
      });
    });

  return {
    shutdownHandler: () => (req, res, next) => {
      if (!shuttingDown) {
        return next();
      }

      res.set('Connection', 'close');
      res.status(503).send('Server is in the process of restarting.');
    },
    shutdownHook,
  };
};

export { gracefulShutdown };
```

## File: `src/_lib/http/middlewares/httpLogger.ts`
```typescript
import { Request, RequestHandler } from 'express';
import logger, { Options, startTime } from 'pino-http';
import { randomUUID } from 'crypto';

type LoggerOptions = Options & { customProps?: (req: Request, res: Response) => any };

const httpLoggerOptions = (): LoggerOptions => {
  const getReqId = (req: Request) => `[req:${req.id}]`;

  return {
    genReqId: () => randomUUID(),
    autoLogging: { ignorePaths: ['/status', '/favicon.ico'] },
    customSuccessMessage: function (res) {
      const req = res.req as Request;

      const reqId = getReqId(req);

      return `${reqId} ${res.statusCode} - ${req.method} ${req.originalUrl} ${Date.now() - res[startTime]}ms`;
    },
    customErrorMessage: function (error, res) {
      const req = res.req as Request;

      const reqId = getReqId(req);

      return `${reqId} ${res.statusCode} - ${req.method} ${req.originalUrl} - [${error.name}] ${error.message} ${
        Date.now() - res[startTime]
      }ms`;
    },
    customLogLevel: function (res, err) {
      if (res.statusCode >= 400 && res.statusCode < 500) {
        return 'warn';
      } else if (res.statusCode >= 500 || err) {
        return 'error';
      } else if (res.statusCode >= 300 && res.statusCode < 400) {
        return 'trace';
      }
      return 'info';
    },
  };
};

const httpLogger = (opts: LoggerOptions = httpLoggerOptions()): RequestHandler =>
  logger({
    ...opts,
  });

export { httpLogger, httpLoggerOptions, startTime as reqStartTimeKey };
export type { LoggerOptions };
```

## File: `src/_lib/http/middlewares/requestContainer.ts`
```typescript
import { asValue } from 'awilix';
import { RequestHandler } from 'express';
import { Container } from '@/container';

const requestContainer =
  (container: Container): RequestHandler =>
  (req, _, next) => {
    const scopedContainer = container.createScope();

    scopedContainer.register({
      requestId: asValue(req.id),
    });

    req.container = scopedContainer;
    next();
  };

export { requestContainer };
```

## File: `src/_lib/http/middlewares/statusHandler.ts`
```typescript
import { handler } from '@/_lib/http/handler';
import { HttpStatus } from '@/_lib/http/HttpStatus';

type Dependencies = {
  startedAt: Date;
};

const statusHandler = handler(({ startedAt }: Dependencies) => async (_, res) => {
  const uptime = Math.round((Date.now() - startedAt.getTime()) / 10) / 100;

  res.status(HttpStatus.OK).json({
    startedAt,
    uptime,
  });
});

export { statusHandler };
```

## File: `src/_lib/http/validation/Paginator.ts`
```typescript
import { Request } from 'express';
import Joi, { InterfaceFrom } from 'types-joi';
import { ValidationError } from '@/_lib/errors/ValidationError';
import { BadRequestError } from '@/_lib/errors/BadRequestError';

type FieldConfig = {
  name: string;
  from: 'query' | 'params' | 'body';
};

type PaginatorOptions<T extends Record<string, any>> = {
  useDefaults?: boolean;
  fields?: {
    page?: string | FieldConfig;
    pageSize?: string | FieldConfig;
    sort?: string | FieldConfig;
    filter: string | FieldConfig;
  };
  defaults?: {
    pageSize?: number;
    page?: number;
    filter?: T['filter'] extends Joi.BaseSchema<any> ? NonNullable<InterfaceFrom<NonNullable<T['filter']>>> : any;
    sort?: {
      field: string;
      direction: 'asc' | 'desc';
    }[];
  };
  filter?: Joi.BaseSchema<any> | null;
};

type Paginator<T extends PaginatorOptions<Record<string, any>>> = {
  getPagination: (req: Request) => { page: number; pageSize: number };
  getFilter: (
    req: Request
  ) => T['filter'] extends Joi.BaseSchema<any> ? NonNullable<InterfaceFrom<NonNullable<T['filter']>>> : any;
  getSorter: (req: Request) => { field: string; direction: 'asc' | 'desc' }[];
};

const defaultOptions = {
  useDefaults: true,
  fields: {
    page: 'page',
    pageSize: 'limit',
    sort: 'sort',
    filter: 'filter',
  },
  defaults: {
    page: 1,
    pageSize: 10,
    sort: [],
    filter: {},
  },
  filter: null,
};

const makePaginator = <T extends PaginatorOptions<any>>(opts: Partial<T> = {}): Paginator<typeof opts> => {
  const { useDefaults, defaults, fields, filter } = {
    ...defaultOptions,
    ...opts,
    fields: {
      ...defaultOptions.fields,
      ...opts.fields,
    },
    defaults: {
      ...defaultOptions.defaults,
      ...opts.defaults,
    },
  };

  const getField = (field: string | FieldConfig): FieldConfig =>
    typeof field === 'string' ? { name: field, from: 'query' } : field;

  const fromRequest = (req: Request, field: FieldConfig) => req[field.from][field.name];

  const getPagination = (req: Request): { page: number; pageSize: number } => {
    const pageField = getField(fields.page);
    const pageSizeField = getField(fields.pageSize);

    const pageValue = Number(fromRequest(req, pageField));
    const pageSizeValue = Number(fromRequest(req, pageSizeField));

    if (!useDefaults && (isNaN(pageValue) || isNaN(pageSizeValue))) {
      throw BadRequestError.create(
        `Missing '${pageField.from}.${pageField.name}' or '${pageSizeField.from}.${pageSizeField.name}' values`
      );
    }

    return {
      page: isNaN(pageValue) ? defaults.page : pageValue,
      pageSize: isNaN(pageSizeValue) ? defaults.pageSize : pageSizeValue,
    };
  };

  const getSorter = (req: Request): { field: string; direction: 'asc' | 'desc' }[] => {
    const sortField = getField(fields.sort);
    const sortValues = fromRequest(req, sortField);

    if (!useDefaults && sortValues === undefined) {
      throw BadRequestError.create(`Missing '${sortField.from}.${sortField.name}' value`);
    }

    const sortList: string[] = Array.isArray(sortValues) ? sortValues : sortValues ? [sortValues] : [];

    return sortList.length
      ? sortList.map((sort) => ({
          field: sort.startsWith('-') ? sort.substr(1) : sort,
          direction: sort.startsWith('-') ? 'desc' : 'asc',
        }))
      : defaults.sort;
  };

  const getFilter = (
    req: Request
  ): T['filter'] extends Joi.BaseSchema<any> ? NonNullable<InterfaceFrom<NonNullable<T['filter']>>> : any => {
    const filterField = getField(fields.filter);
    const filterValue = fromRequest(req, filterField);

    if (!filter) {
      if (!useDefaults && filterValue === undefined) {
        throw BadRequestError.create(`Missing '${filterField.from}.${filterField.name}' value`);
      }

      return filterValue ?? defaults.filter;
    }

    const { error } = Joi.object({ filter: filter as unknown as Joi.AnySchema<any> })
      .options({ allowUnknown: true })
      .validate(req[filterField.from]);

    if (error) {
      throw ValidationError.create({ target: filterField.name, error });
    }

    return filterValue ?? defaults.filter;
  };

  return {
    getFilter,
    getPagination,
    getSorter,
  };
};

export { makePaginator };
```

## File: `src/_lib/http/validation/Validator.ts`
```typescript
import * as Joi from 'types-joi';
import { Request } from 'express';
import { InterfaceFrom } from 'types-joi';
import { ValidationError } from '@/_lib/errors/ValidationError';

type ValidationSchemas = {
  body?: Joi.BaseSchema<any>;
  params?: Joi.BaseSchema<any>;
  query?: Joi.BaseSchema<any>;
  headers?: Joi.BaseSchema<any>;
  cookies?: Joi.BaseSchema<any>;
};

type ValidationType<T> = T extends Joi.BaseSchema<any> ? InterfaceFrom<NonNullable<T>> : any;

type ValidationHelpers<T extends ValidationSchemas> = {
  getBody(req: Request): ValidationType<T['body']>;
  getParams(req: Request): ValidationType<T['params']>;
  getQuery(req: Request): ValidationType<T['query']>;
  getCookies(req: Request): ValidationType<T['cookies']>;
  getHeaders(req: Request): ValidationType<T['headers']>;
};

const makeValidator = <T extends ValidationSchemas>(schemas: T): ValidationHelpers<typeof schemas> => {
  const createValidator = (key: keyof ValidationSchemas) => (req: Request) => {
    if (!schemas[key]) {
      return req[key];
    }

    const { value, error } = (schemas[key] as Joi.BaseSchema<any>).validate(req[key]);

    if (error) {
      throw ValidationError.create({ target: key, error });
    }

    return value;
  };

  return {
    getBody: createValidator('body'),
    getParams: createValidator('params'),
    getQuery: createValidator('query'),
    getHeaders: createValidator('headers'),
    getCookies: createValidator('cookies'),
  };
};

export { makeValidator };
```

## File: `src/_lib/logger/index.ts`
```typescript
import pino from 'pino';

const logger = pino();

export { logger };
```

## File: `src/_lib/pubSub/EventEmitterConsumer.ts`
```typescript
import { makeEventConsumer } from '@/_lib/events/EventConsumer';
import { key } from '@/_lib/pubSub/EventEmitterPubSub';

const eventConsumer = makeEventConsumer(key);

export { eventConsumer };
```

## File: `src/_lib/pubSub/EventEmitterProvider.ts`
```typescript
import { makeEventProvider } from '@/_lib/events/EventProvider';
import { key } from '@/_lib/pubSub/EventEmitterPubSub';

const eventProvider = makeEventProvider(key);

export { eventProvider };
```

## File: `src/_lib/pubSub/EventEmitterPubSub.ts`
```typescript
import { Publisher } from '@/_lib/events/Publisher';
import { Subscriber, SubscriberOptions } from '@/_lib/events/Subscriber';
import { EventEmitter } from 'stream';

const defaultOpts: SubscriberOptions = {
  nackOn: () => true,
  single: false,
};

const makeEventEmitterPubSub = (): Publisher & Subscriber => {
  const emitter = new EventEmitter();

  const registrations: (() => Promise<void>)[] = [];

  return {
    publish: async (event) => {
      emitter.emit(`${event.topic}.${event.eventType}`, event);
    },
    add: async (address, handler, opts = {}) => {
      const { single, nackOn } = { ...defaultOpts, ...opts };

      registrations.push(async () => {
        emitter[single ? 'once' : 'on'](`${address.topic}.${address.eventType}`, async (event) => {
          try {
            await handler(event);
          } catch (err) {
            if (nackOn(err)) {
              throw err;
            }

            console.error(err);
          }
        });
      });
    },
    start: async () => {
      await registrations.reduce((chain, registration) => chain.then(registration), Promise.resolve());
    },
    dispose: async () => {
      emitter.removeAllListeners();
    },
  };
};

const key = 'eventEmitterPubSub';

export { key, makeEventEmitterPubSub };
```

## File: `src/_lib/repl/index.ts`
```typescript
import REPL, { REPLEval, ReplOptions, REPLServer } from 'repl';
import vm from 'vm';
import { createServer, Server, Socket } from 'net';

type REPLProps = {
  context: Record<string, any>;
  prompt: string;
  cli: boolean;
  remote: false | { port: number };
  logger: Pick<Console, 'error'>;
};

type REPLInstance = {
  create: (config: Partial<ReplOptions>) => REPLServer;
  start: ({ terminate }) => Promise<void>;
  close: () => Promise<void>;
};

const isPromise = (value) => value && typeof value.then === 'function' && typeof value.catch === 'function';

const promisableEval: REPLEval = (cmd, context, filename, callback) => {
  const result = vm.runInContext(cmd, context);

  if (isPromise(result)) {
    return result.then((v) => callback(null, v)).catch((e) => callback(e, null));
  }

  return callback(null, result);
};

const makeREPL = ({ context, prompt, cli, remote, logger }: REPLProps): REPLInstance => {
  let server: Server;

  const create = (config: Partial<ReplOptions> = { input: process.stdin, output: process.stdout }): REPLServer => {
    const repl = REPL.start({
      eval: promisableEval,
      prompt: `${prompt}$ `,
      ignoreUndefined: true,
      ...config,
    });

    Object.assign(repl.context, context);

    return repl;
  };

  let destroySocket: Socket['destroy'] = () => null;

  return {
    create,
    start: async ({ terminate }) => {
      if (cli) {
        const repl = create();

        repl.on('close', terminate);
      } else if (remote) {
        server = createServer((socket) => {
          const repl = create({
            input: socket,
            output: socket,
            terminal: true,
          });

          destroySocket = socket.destroy.bind(socket);

          repl.on('close', () => {
            socket.end();
          });

          socket.on('error', (err) => {
            logger.error('[REPL] Connection error');
            logger.error(err);
            socket.end();
          });
        }).listen(remote.port);
      }
    },
    close: async () => {
      if (server && server.listening) {
        await new Promise<void>((resolve, reject) => {
          destroySocket();

          server.close((err) => {
            if (err) return reject(err);
            resolve();
          });
        });
      }
    },
  };
};

export { makeREPL };
```

## File: `src/_sharedKernel/domain/ArticleId.d.ts`
```typescript
import { AggregateId } from '@/_lib/DDD';

type ArticleId = AggregateId<string>;

export { ArticleId };
```

## File: `src/_sharedKernel/domain/error/BusinessError.ts`
```typescript
import { BaseError, Exception } from '@/_lib/errors/BaseError';
import { makePredicate } from '@/_lib/Predicate';

namespace BusinessError {
  const type = Symbol();
  const name = 'BusinessError';

  export const create = (message: string, code: string = name): Exception =>
    new BaseError({ type, name, code, message });

  export const is = makePredicate<Exception>(type);
}

export { BusinessError };
```

## File: `src/_sharedKernel/infrastructure/ArticleIdProvider.ts`
```typescript
import { makeIdProvider } from '@/_lib/IdProvider';
import { ArticleId } from '@/_sharedKernel/domain/ArticleId';

const ArticleIdProvider = makeIdProvider<ArticleId>('ArticleId');

export { ArticleIdProvider };
```

## File: `src/_sharedKernel/interface/http/ErrorConverters.ts`
```typescript
import { ValidationError } from '@/_lib/errors/ValidationError';
import { errorConverter } from '@/_lib/http/middlewares/errorHandler';
import { BaseError } from '@/_lib/errors/BaseError';
import { NotFoundError } from '@/_lib/errors/NotFoundError';
import { HttpStatus } from '@/_lib/http/HttpStatus';
import { UnauthorizedError } from '@/_lib/errors/UnauthorizedError';
import { ForbiddenError } from '@/_lib/errors/ForbiddenError';
import { BusinessError } from '@/_sharedKernel/domain/error/BusinessError';
import { BadRequestError } from '@/_lib/errors/BadRequestError';

const errorConverters = [
  errorConverter(ValidationError.is, (err) => {
    const status = err.meta?.target === 'body' ? HttpStatus.UNPROCESSABLE_ENTITY : HttpStatus.BAD_REQUEST;

    return {
      status,
      body: {
        error: err.name,
        code: err.code,
        status,
        message: err.message,
        details: err.meta?.error.details.map((detail) => ({
          field: detail.path.join('.'),
          path: detail.path,
        })),
      },
    };
  }),
  errorConverter(BadRequestError.is, (err) => ({
    status: HttpStatus.BAD_REQUEST,
    body: {
      error: err.name,
      code: err.code,
      status: HttpStatus.BAD_REQUEST,
      message: err.message,
    },
  })),
  errorConverter(NotFoundError.is, (err) => ({
    status: HttpStatus.NOT_FOUND,
    body: {
      error: err.name,
      code: err.code,
      status: HttpStatus.NOT_FOUND,
      message: err.message,
    },
  })),
  errorConverter(UnauthorizedError.is, (err) => ({
    status: HttpStatus.UNAUTHORIZED,
    body: {
      error: err.name,
      code: err.code,
      status: HttpStatus.UNAUTHORIZED,
      message: err.message,
    },
  })),
  errorConverter(ForbiddenError.is, (err) => ({
    status: HttpStatus.FORBIDDEN,
    body: {
      error: err.name,
      code: err.code,
      status: HttpStatus.FORBIDDEN,
      message: err.message,
    },
  })),
  errorConverter(BusinessError.is, (err) => ({
    status: HttpStatus.CONFLICT,
    body: {
      error: err.name,
      code: err.code,
      status: HttpStatus.CONFLICT,
      kind: err.meta?.key,
      message: err.message,
    },
  })),
  errorConverter(
    (err: any | BaseError): err is BaseError => err instanceof BaseError,
    (err) => ({
      status: HttpStatus.INTERNAL_SERVER_ERROR,
      body: {
        error: err.name,
        code: err.code,
        status: HttpStatus.INTERNAL_SERVER_ERROR,
        meta: err.meta,
        message: err.message,
      },
    })
  ),
];

export { errorConverters };
```

## File: `src/__tests__/setup.ts`
```typescript
process.env.NODE_ENV = 'test';

const catchAll = new Proxy(
  {},
  {
    get: () => {
      return jest.fn().mockReturnValue(catchAll);
    },
  }
);

jest.mock('pino', () => () => catchAll);

console = catchAll;
```

## File: `src/__tests__/TestControls.ts`
```typescript
import { Container, container } from '@/container';
import { withContext } from '@/context';
import { main } from '@/_boot';
import { Db } from 'mongodb';
import supertest, { SuperTest, Test } from 'supertest';

type Dependencies = {
  mongo: Db;
};

type TestControls = Readonly<{
  request: () => SuperTest<Test>;
  clearDatabase: () => Promise<void>;
  cleanUp: () => Promise<void>;
  container: Container;
  registry: Container['cradle'];
}>;

const appRunning = withContext(
  ({ app: { onRunning } }) =>
    new Promise<void>((resolve) => {
      onRunning(async () => {
        resolve();
      });

      main();
    })
);

const makeClearDatabase =
  ({ mongo }: Dependencies) =>
  async (): Promise<void> => {
    const collections = await mongo.collections();

    await Promise.all(collections.map((collection) => collection.deleteMany({})));
  };

const makeTestControls = async (): Promise<TestControls> => {
  await appRunning();

  const { server } = container.cradle;

  const clearDatabase = container.build(makeClearDatabase);

  const cleanUp = withContext(async ({ app }) => {
    await clearDatabase();
    await app.stop();
  });

  return {
    request: () => supertest(server),
    registry: container.cradle,
    clearDatabase,
    container,
    cleanUp,
  };
};

export { makeTestControls };
export type { TestControls };
```

