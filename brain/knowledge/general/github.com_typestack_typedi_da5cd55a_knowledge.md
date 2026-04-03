---
id: github.com-typestack-typedi-da5cd55a-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:32.650936
---

# KNOWLEDGE EXTRACT: github.com_typestack_typedi_da5cd55a
> **Extracted on:** 2026-04-01 08:29:25
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519572/github.com_typestack_typedi_da5cd55a

---

## File: `.eslintrc.yml`
```yaml
parser: '@typescript-eslint/parser'
plugins:
  - '@typescript-eslint'
parserOptions:
  ecmaVersion: 2018
  sourceType: module
  project: 
    - ./tsconfig.json
    - ./tsconfig.spec.json
extends:
  - 'plugin:@typescript-eslint/recommended'
  - 'plugin:@typescript-eslint/recommended-requiring-type-checking'
  - 'plugin:jest/recommended'
  - 'prettier'
rules:
  '@typescript-eslint/explicit-member-accessibility': off
  '@typescript-eslint/no-angle-bracket-type-assertion': off
  '@typescript-eslint/no-parameter-properties': off
  '@typescript-eslint/explicit-function-return-type': off
  '@typescript-eslint/member-delimiter-style': off
  '@typescript-eslint/no-inferrable-types': off
  '@typescript-eslint/no-explicit-any': off
  '@typescript-eslint/no-unused-vars':
    - 'error'
    - args: 'none'
  # TODO: Remove these and fixed issues once we merged all the current PRs. 
  '@typescript-eslint/ban-types': off 
  '@typescript-eslint/no-unsafe-return': off
  '@typescript-eslint/no-unsafe-assignment': off
  '@typescript-eslint/no-unsafe-call': off
  '@typescript-eslint/no-unsafe-member-access': off
  '@typescript-eslint/explicit-module-boundary-types': off
```

## File: `.gitbook.yaml`
```yaml
root: ./docs
​structure:  
    readme: README.md  
    summary: SUMMARY.md​
```

## File: `.gitignore`
```
# Log files
logs
*.log
*.tmp
*.tmp.*
log.txt
npm-debug.log*

# Testing output
lib-cov/**
coverage/**

# Environment files
.env

# Dependency directories
node_modules

# MacOS related files
*.DS_Store
.AppleDouble
.LSOverride
._*
UserInterfaceState.xcuserstate

# Windows related files
Thumbs.db
Desktop.ini
$RECYCLE.BIN/

# IDE - Sublime
*.sublime-project
*.sublime-workspace

# IDE - VSCode
.vscode/**
!.vscode/tasks.json
!.vscode/launch.json

# IDE - IntelliJ
.idea

# Compilation output folders
dist/
build/
tmp/
out-tsc/
temp

# Files for playing around locally
playground.ts
playground.js
```

## File: `.prettierrc.yml`
```yaml
printWidth: 120
tabWidth: 2
useTabs: false
semi: true
singleQuote: true
trailingComma: es5
bracketSpacing: true
arrowParens: avoid
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## 0.11.0 [BREAKING] - [UNRELEASED]

### BREAKING CHANGES

#### `Container.set(token, value)` and `Container.set('string-id', value)` signature removed

To allow better intellisense support for signatures, the overloads allowing to specify services
via a simplified form has been removed. From now on, services can be specified via the configuration object.

```ts
// Old format
Container.set(myToken, myValue);

// New format
Container.set({ id: myToken, value: myValue });
```

#### `Service(token)` and `Service('string-id')` signature removed

To allow better intellisense support for signatures, the overloads allowing to specify services
via a simplified form has been removed. From now on, services can be specified via the configuration object.

```ts
// Old format
@Service(myToken)
export class MyClass {}

// New format
@Service({ id: myToken })
export class MyClass {}
```

#### `Container.set({})` and `@Service()` decorator signature change

The `global`, `transient` options had been removed in favor of `scope` option.

```ts
// Old format
@Service({ transient: true })
class MyTransientClass {}

@Service({ global: true })
class MySingletonClass {}

// New format
@Service({ scope: 'transient' })
class MyTransientClass {}

@Service({ scope: 'singleton' })
class MySingletonClass {}
```

#### `Container.reset()` signature change

The `Container.reset` signature has changed. It's only possible to reset the current container instance you are calling
the function on, so the first `containerId` parameter has been removed.

```ts
// Old format
Container.reset(myContainerId, { strategy: 'resetValue' });

// New format
MyContainer.reset({ strategy: 'resetValue' });
```

#### `Container.set([definitionOne, definitionTwo])` signature removed

The option to add definitions as an array was removed. This was internally used, but exposed via the typing.

<!-- prettier-ignore -->
```ts
// Old format
Container.set([{ id: SomeClass, type: SomeClass }, { id: OtherClass, type: OtherClass }])

// New format
[{ id: SomeClass, type: SomeClass }, { id: OtherClass, type: OtherClass }].map(metadata => Container.set(metadata));
```

### Added

- added support for specifying Container ID as `Symbol`
- re-enabled throwing error when `reflect-metadata` is not imported

### Changed

- internally the default container is also an instance of the ContainerInstance class from now on

### Fixed

- `Container.set()` correctly enforces typing when used with a `Token`. Attempting to set something else than the Token
  type allows will raise a compile time error

## 0.10.0 [BREAKING] - 2021.01.15

### BREAKING CHANGES

#### Container.remove signature change

The `Container.remove` method from now accepts one ID or an array of IDs.

```ts
// Old format
Container.remove(myServiceA, myServiceB);

// New format
Container.remove([myServiceA, myServiceB]);
```

#### Removed support for calling `Service([depA, depB], factory)`

This was an undocumented way of calling the `Service` function directly instead of using it as a decorator. This option
has been removed and the official supported way of achieving the same is with `Container.set`. Example:

```ts
const myToken = new Token('myToken');

Container.set(myToken, 'test-value');

// Old format:
const oldWayService = Service([myToken], function myFactory(myToken) {
  return myToken.toUpperCase();
});
const oldResult = Container.get(oldWayService);
// New format
const newWayService = Container.set({
  // ID can be anything, we use string for simplicity
  id: 'my-custom-service',
  factory: function myFactory(container) {
    return container.get(myToken).toUppserCase();
  },
});
const newResult = Container.get('my-custom-service');

oldResult === newResult; // -> true, both equals to "TEST-VALUE"
```

### Added

- added `eager` option to `ServiceOptions`, when enabled the class will be instantiated as soon as it's registered in the container
- added support for destroying removed services, when a service is removed and has a callable `destroy` property it will be called by TypeDI

### Changed

- [BREAKING] removed old, undocumented way of calling `@Service` decorator directly
- [BREAKING] renamed `MissingProvidedServiceTypeError` to `CannotInstantiateValueError`
- various internal refactors
- updated various dev dependencies

### Fixed

- generated sourcemaps contains the Typescript files preventing reference errors when using TypeDI with various build tools

## 0.9.1 - 2021.01.11

### Fixed

- correctly export error classes from package root

## 0.9.0 - 2021.01.10

### BREAKING CHANGES

#### Unregistered types are not resolved

Prior to this version when an unknown constructable type was requested from the default container it was added automatically
to the container and returned. This behavior has changed and now a `ServiceNotFoundError` error is thrown.

#### Changed container reset behavior

Until now resetting a container removed all dependency declarations from the container. From now on the default behavior
is to remove the created instances only but not the definitions. This means requesting a Service again from the container
won't result in a `ServiceNotFoundError` but will create a new instance of the requested function again.

The old behavior can be restored with passing the `{ strategy: 'resetServices'}` to the `ContainerInstance.reset` function.

### Changed

- **[BREAKING]** unknown values are not resolved anymore (ref #87)
- **[BREAKING]** resetting a container doesn't remove the service definitions only the created instances by default
- **[BREAKING]** container ID can be string only now
- default container ID changed from `undefined` to `default`
- stricter type definitions and assertions across the project
- updated the wording of `ServiceNotFoundError` to better explain which service is missing (#138)
- updated various dev-dependencies
- various changes to project tooling

### Fixed

- fixed a bug where requesting service with circular dependencies from a scoped container would result in Maximum call stack size exceeded error (ref #112)
- fixed a bug where `@Inject`-ed properties were not injected in inherited child classes (ref #102)
- fixed a typing issue which prevented using abstract class as service identifier (ref #144)
- fixed a bug which broke transient services when `Container.reset()` was called (ref #157)
- fixed some typos in the getting started documentation

## 0.8.0

- added new type of dependency injection - function DI
- now null can be stored in the container for values

## 0.7.2

- fixed bug with inherited services

## 0.7.1

- fixed the way how global services work

## 0.7.0

- added javascript support
- removed deprecated `@Require` decorator
- added support for transient services
- now service constructors cannot accept non-service arguments
- added `@InjectMany` decorator to support injection of "many" values
- fixed the way how global services work

## 0.6.1

- added `Container.has` method

## 0.6.0

- added multiple containers support
- added grouped (tagged) containers support
- removed `provide` method, use `set` method instead
- deprecated `Require` decorator. Use es6 imports instead or named services
- inherited classes don't need to be decorated with `@Service` decorator
- other small api changes
- now `Handler`'s `value` accepts a container which requests the value
```

## File: `LICENSE`
```
The MIT License

Copyright (c) 2015-2021 TypeStack

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `README.md`
```markdown
# TypeDI

![Build Status](https://github.com/typestack/typedi/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/typestack/typedi/branch/master/graph/badge.svg)](https://codecov.io/gh/typestack/typedi)
[![npm version](https://badge.fury.io/js/typedi.svg)](https://badge.fury.io/js/typedi)
[![Dependency Status](https://david-dm.org/typestack/typedi.svg)](https://david-dm.org/typestack/typedi)

TypeDI is a [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) tool for TypeScript and JavaScript. With it you can build well-structured and easily testable applications in Node or in the browser.

Main features includes:

- property based injection
- constructor based injection
- singleton and transient services
- support for multiple DI containers

## Installation

> Note: This installation guide is for usage with TypeScript, if you wish to use
> TypeDI without Typescript please read the documentation about how get started.

To start using TypeDI install the required packages via NPM:

```bash
npm install typedi reflect-metadata
```

Import the `reflect-metadata` package at the **first line** of your application:

```ts
import 'reflect-metadata';

// Your other imports and initialization code
// comes here after you imported the reflect-metadata package!
```

As a last step, you need to enable emitting decorator metadata in your Typescript config. Add these two lines to your `tsconfig.json` file under the `compilerOptions` key:

```json
"emitDecoratorMetadata": true,
"experimentalDecorators": true,
```

Now you are ready to use TypeDI with Typescript!

## Basic Usage

```ts
import { Container, Service } from 'typedi';

@Service()
class ExampleInjectedService {
  printMessage() {
    console.log('I am alive!');
  }
}

@Service()
class ExampleService {
  constructor(
    // because we annotated ExampleInjectedService with the @Service()
    // decorator TypeDI will automatically inject an instance of
    // ExampleInjectedService here when the ExampleService class is requested
    // from TypeDI.
    public injectedService: ExampleInjectedService
  ) {}
}

const serviceInstance = Container.get(ExampleService);
// we request an instance of ExampleService from TypeDI

serviceInstance.injectedService.printMessage();
// logs "I am alive!" to the console
```

## Documentation

The detailed usage guide and API documentation for the project can be found:

- at [docs.typestack.community/typedi][docs-stable]
- in the `./docs` folder of the repository

[docs-stable]: https://docs.typestack.community/typedi/
[docs-development]: https://docs.typestack.community/typedi/v/develop/

## Contributing

Please read our [contributing guidelines](./CONTRIBUTING.md) to get started.
```

## File: `codecov.yml`
```yaml
coverage:
  range: 70..100
  round: down
  precision: 2
  status:
    project:
      default:
        threshold: 0%
        paths: 
          - src/**/*.ts
comment: off
ignore:
  - testing/**/*.ts
  - src/**/*.interface.ts
```

## File: `jest.config.js`
```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  collectCoverageFrom: ['src/**/*.ts', '!src/**/index.ts', '!src/**/*.interface.ts'],
  globals: {
    'ts-jest': {
      tsconfig: 'tsconfig.spec.json',
    },
  },
};
```

## File: `package.json`
```json
{
  "name": "typedi",
  "version": "0.10.0",
  "description": "Dependency injection for TypeScript.",
  "author": "TypeStack contributors",
  "license": "MIT",
  "sideEffects": false,
  "main": "./cjs/index.js",
  "module": "./esm5/index.js",
  "es2015": "./esm2015/index.js",
  "typings": "./types/index.d.ts",
  "repository": {
    "type": "git",
    "url": "https://github.com/pleerock/typedi.git"
  },
  "tags": [
    "di",
    "container",
    "di-container",
    "typescript",
    "typescript-di",
    "dependency-injection"
  ],
  "scripts": {
    "build": "npm run build:cjs",
    "build:clean": "rimraf build",
    "build:es2015": "tsc --project tsconfig.prod.esm2015.json",
    "build:esm5": "tsc --project tsconfig.prod.esm5.json",
    "build:cjs": "tsc --project tsconfig.prod.cjs.json",
    "build:umd": "rollup --config rollup.config.js",
    "build:types": "tsc --project tsconfig.prod.types.json",
    "prettier:fix": "prettier --write \"**/*.{ts,md}\"",
    "prettier:check": "prettier --check \"**/*.{ts,md}\"",
    "lint:fix": "eslint --max-warnings 0 --fix --ext .ts src/",
    "lint:check": "eslint --max-warnings 0 --ext .ts src/",
    "test": "jest --coverage --verbose",
    "test:watch": "jest --watch",
    "test:ci": "jest --runInBand --coverage --verbose"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.md": [
      "npm run prettier:fix"
    ],
    "*.ts": [
      "npm run prettier:fix"
    ]
  },
  "devDependencies": {
    "@rollup/plugin-commonjs": "^26.0.1",
    "@rollup/plugin-node-resolve": "^15.2.3",
    "@types/jest": "^27.5.0",
    "@types/node": "^22.5.1",
    "@typescript-eslint/eslint-plugin": "^5.62.0",
    "@typescript-eslint/parser": "^5.62.0",
    "eslint": "^8.57.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-jest": "^27.9.0",
    "husky": "^4.3.8",
    "jest": "^27.5.1",
    "lint-staged": "^15.2.9",
    "prettier": "^2.8.8",
    "reflect-metadata": "0.2.2",
    "rimraf": "6.0.1",
    "rollup": "^2.79.1",
    "rollup-plugin-terser": "^7.0.2",
    "ts-jest": "^27.1.4",
    "ts-node": "^10.9.2",
    "typescript": "^4.9.5"
  }
}
```

## File: `rollup.config.js`
```javascript
import { nodeResolve } from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';

export default {
  input: 'build/esm5/index.js',
  output: [
    {
      name: 'ClassTransformer',
      format: 'umd',
      file: 'build/bundles/typedi.umd.js',
      sourcemap: true,
    },
    {
      name: 'ClassTransformer',
      format: 'umd',
      file: 'build/bundles/typedi.umd.min.js',
      sourcemap: true,
      plugins: [terser()],
    },
  ],
  plugins: [commonjs(), nodeResolve()],
};
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "module": "commonjs",
    "moduleResolution": "node",
    "target": "es2018",
    "lib": ["es2018"],
    "outDir": "build/node",
    "rootDirs": ["./src"],
    "strict": true,
    "sourceMap": true,
    "inlineSources": true,
    "removeComments": false,
    "esModuleInterop": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "forceConsistentCasingInFileNames": true
  },
  "exclude": ["build", "node_modules", "sample", "**/*.spec.ts", "test/**"]
}
```

## File: `tsconfig.prod.cjs.json`
```json
{
  "extends": "./tsconfig.prod.json",
  "compilerOptions": {
    "module": "CommonJS",
    "outDir": "build/cjs"
  },
}
```

## File: `tsconfig.prod.esm2015.json`
```json
{
  "extends": "./tsconfig.prod.json",
  "compilerOptions": {
    "module": "ES2015",
    "outDir": "build/esm2015",
  },
}
```

## File: `tsconfig.prod.esm5.json`
```json
{
  "extends": "./tsconfig.prod.json",
  "compilerOptions": {
    "module": "ES2015",
    "target": "ES5",
    "outDir": "build/esm5",
  },
}
```

## File: `tsconfig.prod.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "strict": false,
    "declaration": false,
  },
}
```

## File: `tsconfig.prod.types.json`
```json
{
  "extends": "./tsconfig.prod.json",
  "compilerOptions": {
    "declaration": true,
    "emitDeclarationOnly": true,
    "outDir": "build/types",
  },
}
```

## File: `tsconfig.spec.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "rootDirs": ["./src", "./test"],
    "strict": false,
    "strictPropertyInitialization": false,
    "sourceMap": false,
    "removeComments": true,
    "noImplicitAny": false,
  },
  "exclude": ["node_modules"]
}
```

## File: `tslint.json`
```json
{
    "rules": {
        "class-name": true,
        "comment-format": [
            true,
            "check-space"
        ],
        "indent": [
            true,
            "spaces"
        ],
        "no-duplicate-variable": true,
        "no-eval": true,
        "no-internal-module": true,
        "no-var-keyword": true,
        "one-line": [
            true,
            "check-open-brace",
            "check-whitespace"
        ],
        "quotemark": [
            true,
            "double"
        ],
        "semicolon": true,
        "triple-equals": [
            true,
            "allow-null-check"
        ],
        "typedef-whitespace": [
            true,
            {
                "call-signature": "nospace",
                "index-signature": "nospace",
                "parameter": "nospace",
                "property-declaration": "nospace",
                "variable-declaration": "nospace"
            }
        ],
        "variable-name": [
            true,
            "ban-keywords"
        ],
        "whitespace": [
            true,
            "check-branch",
            "check-decl",
            "check-operator",
            "check-separator",
            "check-type"
        ]
    }
}
```

## File: `docs/README.md`
```markdown
# Documentation

## Typescript Usage

With TypeDI you can use a named services. Example:

```typescript
import { Container, Service, Inject } from 'typedi';

interface Factory {
  create(): void;
}

@Service({ id: 'bean.factory' })
class BeanFactory implements Factory {
  create() {}
}

@Service({ id: 'sugar.factory' })
class SugarFactory implements Factory {
  create() {}
}

@Service({ id: 'water.factory' })
class WaterFactory implements Factory {
  create() {}
}

@Service({ id: 'coffee.maker' })
class CoffeeMaker {
  beanFactory: Factory;
  sugarFactory: Factory;

  @Inject('water.factory')
  waterFactory: Factory;

  constructor(@Inject('bean.factory') beanFactory: BeanFactory, @Inject('sugar.factory') sugarFactory: SugarFactory) {
    this.beanFactory = beanFactory;
    this.sugarFactory = sugarFactory;
  }

  make() {
    this.beanFactory.create();
    this.sugarFactory.create();
    this.waterFactory.create();
  }
}

let coffeeMaker = Container.get<CoffeeMaker>('coffee.maker');
coffeeMaker.make();
```

This feature especially useful if you want to store (and inject later on) some settings or configuration options.
For example:

```typescript
import { Container, Service, Inject } from 'typedi';

// somewhere in your global app parameters
Container.set('authorization-token', 'RVT9rVjSVN');

@Service()
class UserRepository {
  @Inject('authorization-token')
  authorizationToken: string;
}
```

When you write tests you can easily provide your own "fake" dependencies to classes you are testing using `set` method:
`provide` methods of the container:

```typescript
Container.set(CoffeeMaker, new FakeCoffeeMaker());

// or for named services

Container.set([
  { id: 'bean.factory', value: new FakeBeanFactory() },
  { id: 'sugar.factory', value: new FakeSugarFactory() },
  { id: 'water.factory', value: new FakeWaterFactory() },
]);
```

## TypeScript Advanced Usage Examples

- [Using factory function to create service](#using-factory-function-to-create-service)
- [Using factory class to create service](#using-factory-class-to-create-service)
- [Problem with circular references](#problem-with-circular-references)
- [Custom decorators](#custom-decorators)
- [Using service groups](#using-service-groups)
- [Using multiple containers and scoped containers](#using-multiple-containers-and-scoped-containers)
- [Remove registered services or reset container state](#remove-registered-services-or-reset-container-state)

### Using factory function to create service

You can create your services with the container using factory functions.

This way, service instance will be created by calling your factory function instead of
instantiating a class directly.

```typescript
import { Container, Service } from 'typedi';

function createCar() {
  return new Car('V8');
}

@Service({ factory: createCar })
class Car {
  constructor(public engineType: string) {}
}

// Getting service from the container.
// Service will be created by calling the specified factory function.
const car = Container.get(Car);

console.log(car.engineType); // > "V8"
```

### Using factory class to create service

You can also create your services using factory classes.

This way, service instance will be created by calling given factory service's method factory instead of
instantiating a class directly.

```typescript
import { Container, Service } from 'typedi';

@Service()
class CarFactory {
  constructor(public logger: LoggerService) {}

  create() {
    return new Car('BMW', this.logger);
  }
}

@Service({ factory: [CarFactory, 'create'] })
class Car {
  constructor(public model: string, public logger: LoggerInterface) {}
}
```

### Problem with circular references

There is a known issue in language that it can't handle circular references. For example:

```typescript
// Car.ts
@Service()
export class Car {
  @Inject()
  engine: Engine;
}

// Engine.ts
@Service()
export class Engine {
  @Inject()
  car: Car;
}
```

This code will not work, because Engine has a reference to Car, and Car has a reference to Engine.
One of them will be undefined and it cause errors. To fix them you need to specify a type in a function this way:

```typescript
// Car.ts
@Service()
export class Car {
  @Inject(type => Engine)
  engine: Engine;
}

// Engine.ts
@Service()
export class Engine {
  @Inject(type => Car)
  car: Car;
}
```

And that's all. This does **NOT** work for constructor injections.

### Custom decorators

You can create your own decorators which will inject your given values for your service dependencies.
For example:

```typescript
// Logger.ts
export function Logger() {
  return function (object: Object, propertyName: string, index?: number) {
    const logger = new ConsoleLogger();
    Container.registerHandler({ object, propertyName, index, value: containerInstance => logger });
  };
}

// LoggerInterface.ts
export interface LoggerInterface {
  log(message: string): void;
}

// ConsoleLogger.ts
import { LoggerInterface } from './LoggerInterface';

export class ConsoleLogger implements LoggerInterface {
  log(message: string) {
    console.log(message);
  }
}

// UserRepository.ts
@Service()
export class UserRepository {
  constructor(@Logger() private logger: LoggerInterface) {}

  save(user: User) {
    this.logger.log(`user ${user.firstName} ${user.secondName} has been saved.`);
  }
}
```

### Using service groups

You can group multiple services into single group tagged with service id or token.
For example:

```typescript
// Factory.ts
export interface Factory {
  create(): any;
}

// FactoryToken.ts
export const FactoryToken = new Token<Factory>('factories');

// BeanFactory.ts
@Service({ id: FactoryToken, multiple: true })
export class BeanFactory implements Factory {
  create() {
    console.log('bean created');
  }
}

// SugarFactory.ts
@Service({ id: FactoryToken, multiple: true })
export class SugarFactory implements Factory {
  create() {
    console.log('sugar created');
  }
}

// WaterFactory.ts
@Service({ id: FactoryToken, multiple: true })
export class WaterFactory implements Factory {
  create() {
    console.log('water created');
  }
}

// app.ts
// now you can get all factories in a single array
Container.import([BeanFactory, SugarFactory, WaterFactory]);
const factories = Container.getMany(FactoryToken); // factories is Factory[]
factories.forEach(factory => factory.create());
```

### Using multiple containers and scoped containers

By default all services are stored in the global service container,
and this global service container holds all unique instances of each service you have.

If you want your services to behave and store data inside differently,
based on some user context (http request for example) -
you can use different containers for different contexts.
For example:

```typescript
// QuestionController.ts
@Service()
export class QuestionController {
  constructor(protected questionRepository: QuestionRepository) {}

  save() {
    this.questionRepository.save();
  }
}

// QuestionRepository.ts
@Service()
export class QuestionRepository {
  save() {}
}

// app.ts
const request1 = { param: 'question1' };
const controller1 = Container.of(request1).get(QuestionController);
controller1.save('Timber');
Container.reset(request1);

const request2 = { param: 'question2' };
const controller2 = Container.of(request2).get(QuestionController);
controller2.save('');
Container.reset(request2);
```

In this example `controller1` and `controller2` are completely different instances,
and `QuestionRepository` used in those controllers are different instances as well.

`Container.reset` removes container with the given context identifier.
If you want your services to be completely global and not be container-specific,
you can mark them as global:

```typescript
@Service({ global: true })
export class QuestionUtils {}
```

And this global service will be the same instance across all containers.

TypeDI also supports a function dependency injection. Here is how it looks like:

```javascript
export const PostRepository = Service(() => ({
  getName() {
    return 'hello from post repository';
  },
}));

export const PostManager = Service(() => ({
  getId() {
    return 'some post id';
  },
}));

export class PostQueryBuilder {
  build() {
    return 'SUPER * QUERY';
  }
}

export const PostController = Service(
  [PostManager, PostRepository, PostQueryBuilder],
  (manager, repository, queryBuilder) => {
    return {
      id: manager.getId(),
      name: repository.getName(),
      query: queryBuilder.build(),
    };
  }
);

const postController = Container.get(PostController);
console.log(postController);
```

### Remove registered services or reset container state

If you need to remove registered service from container simply use `Container.remove(...)` method.
Also you can completely reset the container by calling `Container.reset()` method.
This will effectively remove all registered services from the container.
```

## File: `docs/SUMMARY.md`
```markdown
# Table of contents

- [Old documentation](README.md)

- [Getting Started](typescript/01-getting-started.md)
- [Usage Guide](typescript/02-basic-usage-guide.md)
  - [Container API](typescript/03-container-api.md)
  - [@Service decorator](typescript/04-service-decorator.md)
  - [@Inject decorator](typescript/05-inject-decorator.md)
  - [Service Tokens](typescript/06-service-tokens.md)
  - [Inheritance](typescript/07-inheritance.md)
  - [Usage with TypeORM](typescript/07-usage-with-typeorm.md)
- Advanced Usage
  - [Creating custom decorators](typescript/08-custom-decorators.md)
  - [Using scoped container](typescript/09-using-scoped-containers.md)
  - [Transient services](typescript/10-using-transient-services.md)

## Usage without TypeScript

- [Getting Started](javascript/01-getting-started.md)
- Usage
  - [Old documentation](javascript/02-basic-usage.md)
```

## File: `docs/javascript/01-getting-started.md`
```markdown
# Getting started without TypeScript

It's possible to use TypeDI without TypesScript, however some of the functionality is limited or not available.
These differences are listed below in the [Limitations][limitations-sections] section.

## Installation

To start using TypeDI with JavaScript install the required packages via NPM:

```bash
npm install typedi reflect-metadata
```

## Basic usage

The most basic usage is to request an instance of a class definition. TypeDI will check if an instance of the class has
been created before and return the cached version or it will create a new instance, cache and return it.

```js
import 'reflect-metadata';
import { Container } from 'typedi';

class ExampleClass {
  print() {
    console.log('I am alive!');
  }
}

/** Register this class to the TypeDI container */
Container.set({ id: ExampleClass, type: ExampleClass });

/** Request an instance of ExampleClass from TypeDI. */
const classInstance = Container.get(ExampleClass);

/** We received an instance of ExampleClass and ready to work with it. */
classInstance.print();
```

For more advanced usage examples and patterns please read the [next page][basic-usage-page].

## Limitations

When registering your dependencies with the `Container.set()` method, there are three options available that must be set. Either one of the following are allowed: `type`, `factory`, or `value` but not more than one.

- `Container.set({ id: ExampleClass, type: ExampleClass});`
- `Container.set({ id: ExampleClass, value: new ExampleClass});`
- `Container.set({ id: ExampleClass, factory: ExampleClass});`

To get started quickly, it is recommend to use `type` due to the fact that using `value` will instantiate the class before it's registered to the TypeDI Container. Using `type` will also assure that the TypeDI Container is injected to the constructor.

[limitations-sections]: #limitations
[basic-usage-page]: ./02-basic-usage.md
```

## File: `docs/javascript/02-basic-usage.md`
```markdown
# Usage without TypeScript

> **NOTE:** This page is a direct copy of the old documentation. It will be reworked.

In your class's constructor you always receive as a last argument a container which you can use to get other dependencies.

```javascript
class BeanFactory {
  create() {}
}

class SugarFactory {
  create() {}
}

class WaterFactory {
  create() {}
}

class CoffeeMaker {
  constructor(container) {
    this.beanFactory = container.get(BeanFactory);
    this.sugarFactory = container.get(SugarFactory);
    this.waterFactory = container.get(WaterFactory);
  }

  make() {
    this.beanFactory.create();
    this.sugarFactory.create();
    this.waterFactory.create();
  }
}

var Container = require('typedi').Container;
var coffeeMaker = Container.get(CoffeeMaker);
coffeeMaker.make();
```

With TypeDI you can use a named services. Example:

```javascript
var Container = require('typedi').Container;

class BeanFactory implements Factory {
  create() {}
}

class SugarFactory implements Factory {
  create() {}
}

class WaterFactory implements Factory {
  create() {}
}

class CoffeeMaker {
  beanFactory: Factory;
  sugarFactory: Factory;
  waterFactory: Factory;

  constructor(container) {
    this.beanFactory = container.get('bean.factory');
    this.sugarFactory = container.get('sugar.factory');
    this.waterFactory = container.get('water.factory');
  }

  make() {
    this.beanFactory.create();
    this.sugarFactory.create();
    this.waterFactory.create();
  }
}

Container.set('bean.factory', new BeanFactory(Container));
Container.set('sugar.factory', new SugarFactory(Container));
Container.set('water.factory', new WaterFactory(Container));
Container.set('coffee.maker', new CoffeeMaker(Container));

var coffeeMaker = Container.get('coffee.maker');
coffeeMaker.make();
```

This feature especially useful if you want to store (and inject later on) some settings or configuration options.
For example:

```javascript
var Container = require('typedi').Container;

// somewhere in your global app parameters
Container.set('authorization-token', 'RVT9rVjSVN');

class UserRepository {
  constructor(container) {
    this.authorizationToken = container.get('authorization-token');
  }
}
```

When you write tests you can easily provide your own "fake" dependencies to classes you are testing using `set` method:

```javascript
Container.set(CoffeeMaker, new FakeCoffeeMaker());

// or for named services

Container.set([
  { id: 'bean.factory', value: new FakeBeanFactory() },
  { id: 'sugar.factory', value: new FakeSugarFactory() },
  { id: 'water.factory', value: new FakeWaterFactory() },
]);
```

TypeDI also supports a function dependency injection. Here is how it looks like:

```javascript
var Service = require('typedi').Service;
var Container = require('typedi').Container;

var PostRepository = Service(() => ({
  getName() {
    return 'hello from post repository';
  },
}));

var PostManager = Service(() => ({
  getId() {
    return 'some post id';
  },
}));

class PostQueryBuilder {
  build() {
    return 'SUPER * QUERY';
  }
}

var PostController = Service([PostManager, PostRepository, PostQueryBuilder], (manager, repository, queryBuilder) => {
  return {
    id: manager.getId(),
    name: repository.getName(),
    query: queryBuilder.build(),
  };
});

var postController = Container.get(PostController);
console.log(postController);
```
```

## File: `docs/typescript/01-getting-started.md`
```markdown
# Getting Started

TypeDI is a [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) library for TypeScript and JavaScript.

## Installation

> Note: This installation guide is for usage with TypeScript, if you wish to use TypeDI without Typescript
> please read the [getting started guide][getting-started-js] for JavaScript.

To start using TypeDI install the required packages via NPM:

```bash
npm install typedi reflect-metadata
```

Import the `reflect-metadata` package at the **first line** of your application:

```ts
import 'reflect-metadata';

// Your other imports and initialization code
// comes here after you imported the reflect-metadata package!
```

As the last step, you need to enable emitting decorator metadata in your Typescript config. Add these two lines to your `tsconfig.json` file under the `compilerOptions` key:

```json
"emitDecoratorMetadata": true,
"experimentalDecorators": true,
```

Now you are ready to use TypeDI with Typescript!

## Basic Usage

The most basic usage is to request an instance of a class definition. TypeDI will check if an instance of the class has
been created before and return the cached version or it will create a new instance, cache, and return it.

```ts
import { Container, Service } from 'typedi';

@Service()
class ExampleInjectedService {
  printMessage() {
    console.log('I am alive!');
  }
}

@Service()
class ExampleService {
  constructor(
    // because we annotated ExampleInjectedService with the @Service()
    // decorator TypeDI will automatically inject an instance of
    // ExampleInjectedService here when the ExampleService class is requested
    // from TypeDI.
    public injectedService: ExampleInjectedService
  ) {}
}

const serviceInstance = Container.get(ExampleService);
// we request an instance of ExampleService from TypeDI

serviceInstance.injectedService.printMessage();
// logs "I am alive!" to the console
```

[getting-started-js]: ../javascript/01-getting-started.md
```

## File: `docs/typescript/02-basic-usage-guide.md`
```markdown
# Basic Usage

> **IMPORTANT NOTE:**  
> Don't forget to **annotate your classes with the `@Service` decorator**! Both the ones being injected and those which
> requests the dependencies should be annotated.

## Registering dependencies

There are three ways to register your dependencies:

- annotating a class with the `@Service()` decorator ([documentation](./04-service-decorator.md))
- registering a value with a `Token`
- registering a value with a string identifier

The `Token` and string identifier can be used to register other values than classes. Both tokens and string identifiers
can register any type of value including primitive values except `undefined`. They must be set on the container with the
`Container.set()` function before they can be requested via `Container.get()`.

```ts
import 'reflect-metadata';
import { Container, Inject, Service, Token } from 'typedi';

const myToken = new Token('SECRET_VALUE_KEY');

Container.set(myToken, 'my-secret-value');
Container.set('my-config-key', 'value-for-config-key');
Container.set('default-pagination', 30);

// somewhere else in your application
const tokenValue = Container.get(myToken);
const configValue = Container.get('my-config-key');
const defaultPagination = Container.get('default-pagination');
```

_For detailed documentation about `@Service` decorator please read the [@Service decorator](./04-service-decorator.md) page._

## Injecting dependencies

There are three ways to inject your dependencies:

- automatic class constructor parameter injection
- annotating class properties with the `@Inject()` decorator
- directly using `Container.get()` to request an instance of a class, `Token` or string identifier

### Constructor argument injection

Any class which has been marked with the `@Service()` decorator will have its constructor properties automatically
injected with the correct dependency.

**TypeDI inserts the container instance** which was used to resolve the dependencies **as the last parameter in the constructor**.

```ts
import 'reflect-metadata';
import { Container, Inject, Service } from 'typedi';

@Service()
class InjectedClass {}

@Service()
class ExampleClass {
  constructor(public injectedClass: InjectedClass) {}
}

const instance = Container.get(ExampleClass);

console.log(instance.injectedClass instanceof InjectedClass);
// prints true as TypeDI assigned the instance of InjectedClass to the property
```

### Property injection

Any property which has been marked with the `@Inject` decorator will be automatically assigned the instance of the class
when the parent class is initialized by TypeDI.

```ts
import 'reflect-metadata';
import { Container, Inject, Service } from 'typedi';

@Service()
class InjectedClass {}

@Service()
class ExampleClass {
  @Inject()
  injectedClass: InjectedClass;
}

const instance = Container.get(ExampleClass);

console.log(instance.injectedClass instanceof InjectedClass);
// prints true as the instance of InjectedClass has been assigned to the `injectedClass` property by TypeDI
```

_For detailed documentation about `@Inject` decorator please read the [@Inject decorator](./05-inject-decorator.md) page._

### Using `Container.get()`

The `Container.get()` function can be used directly to request an instance of the target type. TypeDI will resolve and
initialize all dependency on the target class. `Container.get()` can be used to request:

- a constructable value (class definition) which will return the class instance
- a `Token` which will return the value registered for that `Token`
- a string which will return the value registered with that name

```ts
import 'reflect-metadata';
import { Container, Inject, Service, Token } from 'typedi';

const myToken = new Token('SECRET_VALUE_KEY');

@Service()
class InjectedClass {}

@Service()
class ExampleClass {
  @Inject()
  injectedClass: InjectedClass;
}

/** Tokens must be explicity set in the Container with the desired value. */
Container.set(myToken, 'my-secret-value');
/** String identifier must be explicity set in the Container with the desired value. */
Container.set('my-dependency-name-A', InjectedClass);
Container.set('my-dependency-name-B', 'primitive-value');

const injectedClassInstance = Container.get(InjectedClass);
// a class without dependencies can be required
const exampleClassInstance = Container.get(ExampleClass);
// a class with dependencies can be required and dependencies will be resolved
const tokenValue = Container.get(myToken);
// tokenValue will be 'my-secret-value'
const stringIdentifierValueA = Container.get('my-dependency-name-A');
// stringIdentifierValueA will be instance of InjectedClass
const stringIdentifierValueB = Container.get('my-dependency-name-B');
// stringIdentifierValueB will be 'primitive-value'
```

_For detailed documentation about `Token` class please read the [Service Tokens](./06-service-tokens.md) page._

## Singleton vs transient classes

Every registered service by default is a singleton. Meaning repeated calls to `Container.get(MyClass)` will return the
same instance. If this is not the desired behavior a class can be marked as `transient` via the `@Service()` decorator.

```ts
import 'reflect-metadata';
import { Container, Inject, Service } from 'typedi';

@Service({ scope: 'transient' })
class ExampleTransientClass {
  constructor() {
    console.log('I am being created!');
    // this line will be printed twice
  }
}

const instanceA = Container.get(ExampleTransientClass);
const instanceB = Container.get(ExampleTransientClass);

console.log(instanceA !== instanceB);
// prints true
```
```

## File: `docs/typescript/03-container-api.md`
```markdown
# Container API
```

## File: `docs/typescript/04-service-decorator.md`
```markdown
# `@Service` decorator
```

## File: `docs/typescript/05-inject-decorator.md`
```markdown
# The `@Inject` decorator

The `@Inject()` decorator is a **property and parameter decorator** used to resolve dependencies on a class property or
a constructor parameter. By default TypeDI infers the type of the property or argument and initializes an instance of
the detected type, however, this behavior can be overwritten via specifying a custom constructable type, `Token`, or
named service as the first parameter of the `@Inject()` decorator.

## Property injection

This decorator is **mandatory** on properties where a class instance is desired. (Without the decorator, the property
will stay undefined.) The type of the property is automatically inferred when it is a class, in all other cases the
requested type must be provided.

```ts
import 'reflect-metadata';
import { Container, Inject, Service } from 'typedi';

@Service()
class InjectedExampleClass {
  print() {
    console.log('I am alive!');
  }
}

@Service()
class ExampleClass {
  @Inject()
  withDecorator: InjectedExampleClass;

  withoutDecorator: InjectedExampleClass;
}

const instance = Container.get(ExampleClass);

/**
 * The `instance` variable is an ExampleClass instance with the `withDecorator`
 * property containing an InjectedExampleClass instance and `withoutDecorator`
 * property being undefined.
 */
console.log(instance);

instance.withDecorator.print();
// prints "I am alive!" (InjectedExampleClass.print function)
console.log(instance.withoutDecorator);
// logs undefined, as this property was not marked with an @Inject decorator
```

## Constructor Injection

The `@Inject` decorator is not required in constructor injection when a class is marked with the `@Service` decorator.
TypeDI will automatically infer and inject the correct class instances for every constructor argument. However, it can
be used to overwrite the injected type.

```ts
import 'reflect-metadata';
import { Container, Inject, Service } from 'typedi';

@Service()
class InjectedExampleClass {
  print() {
    console.log('I am alive!');
  }
}

@Service()
class ExampleClass {
  constructor(
    @Inject()
    public withDecorator: InjectedExampleClass,
    public withoutDecorator: InjectedExampleClass
  ) {}
}

const instance = Container.get(ExampleClass);

/**
 * The `instance` variable is an ExampleClass instance with both the
 * `withDecorator` and `withoutDecorator` property containing an
 * InjectedExampleClass instance.
 */
console.log(instance);

instance.withDecorator.print();
// prints "I am alive!" (InjectedExampleClass.print function)
instance.withoutDecorator.print();
// prints "I am alive!" (InjectedExampleClass.print function)
```

## Explicitly requesting target type

By default, TypeDI will try to infer the type of property and arguments and inject the proper class instance. When this
is not possible (eg: the property type is an interface) there is three way to overwrite the type of the injected value:

- via `@Inject(() => type)` where `type` is a constructable value (eg: a class definition)
- via `@Inject(myToken)` where `myToken` is an instance of `Token` class
- via `@Inject(serviceName)` where `serviceName` is a string ID

In all three cases the requested dependency must be registered in the container first.

```ts
import 'reflect-metadata';
import { Container, Inject, Service } from 'typedi';

@Service()
class InjectedExampleClass {
  print() {
    console.log('I am alive!');
  }
}

@Service()
class BetterInjectedClass {
  print() {
    console.log('I am a different class!');
  }
}

@Service()
class ExampleClass {
  @Inject()
  inferredPropertyInjection: InjectedExampleClass;

  /**
   * We tell TypeDI that initialize the `BetterInjectedClass` class
   * regardless of what is the inferred type.
   */
  @Inject(() => BetterInjectedClass)
  explicitPropertyInjection: InjectedExampleClass;

  constructor(
    public inferredArgumentInjection: InjectedExampleClass,
    /**
     * We tell TypeDI that initialize the `BetterInjectedClass` class
     * regardless of what is the inferred type.
     */
    @Inject(() => BetterInjectedClass)
    public explicitArgumentInjection: InjectedExampleClass
  ) {}
}

/**
 * The `instance` variable is an ExampleClass instance with both the
 *  - `inferredPropertyInjection` and `inferredArgumentInjection` property
 *    containing an `InjectedExampleClass` instance
 *  - `explicitPropertyInjection` and `explicitArgumentInjection` property
 *    containing a `BetterInjectedClass` instance.
 */
const instance = Container.get(ExampleClass);

instance.inferredPropertyInjection.print();
// prints "I am alive!" (InjectedExampleClass.print function)
instance.explicitPropertyInjection.print();
// prints "I am a different class!" (BetterInjectedClass.print function)
instance.inferredArgumentInjection.print();
// prints "I am alive!" (InjectedExampleClass.print function)
instance.explicitArgumentInjection.print();
// prints "I am a different class!" (BetterInjectedClass.print function)
```
```

## File: `docs/typescript/06-service-tokens.md`
```markdown
# Service Tokens

Service tokens are unique identifiers what provides type-safe access to a value stored in a `Container`.

```ts
import 'reflect-metadata';
import { Container, Token } from 'typedi';

export const JWT_SECRET_TOKEN = new Token<string>('MY_SECRET');

Container.set(JWT_SECRET_TOKEN, 'wow-such-secure-much-encryption');

/**
 * Somewhere else in the application after the JWT_SECRET_TOKEN is
 * imported in can be used to request the secret from the Container.
 *
 * This value is type-safe also because the Token is typed.
 */
const JWT_SECRET = Container.get(JWT_SECRET_TOKEN);
```

## Injecting service tokens

They can be used with the `@Inject()` decorator to overwrite the inferred type of the property or argument.

```ts
import 'reflect-metadata';
import { Container, Token, Inject, Service } from 'typedi';

export const JWT_SECRET_TOKEN = new Token<string>('MY_SECRET');

Container.set(JWT_SECRET_TOKEN, 'wow-such-secure-much-encryption');

@Service()
class Example {
  @Inject(JWT_SECRET_TOKEN)
  myProp: string;
}

const instance = Container.get(Example);
// The instance.myProp property has the value assigned for the Token
```

## Tokens with same name

Two token **with the same name are different tokens**. The name is only used to help the developer identify the tokens
during debugging and development. (It's included in error the messages.)

```ts
import 'reflect-metadata';
import { Container, Token } from 'typedi';

const tokenA = new Token('TOKEN');
const tokenB = new Token('TOKEN');

Container.set(tokenA, 'value-A');
Container.set(tokenB, 'value-B');

const tokenValueA = Container.get(tokenA);
// tokenValueA is "value-A"
const tokenValueB = Container.get(tokenB);
// tokenValueB is "value-B"

console.log(tokenValueA === tokenValueB);
// returns false, as Tokens are always unique
```

## Difference between Token and string identifier

They both achieve the same goal, however, it's recommended to use `Tokens` as they are type-safe and cannot be mistyped,
while a mistyped string identifier will silently return `undefined` as value by default.
```

## File: `docs/typescript/07-inheritance.md`
```markdown
# Inheritance

Inheritance is supported **for properties** when both the base and the extended class is marked with the `@Service()` decorator.
Classes which extend a class with decorated properties will receive the initialized class instances on those properties upon creation.

```ts
import 'reflect-metadata';
import { Container, Token, Inject, Service } from 'typedi';

@Service()
class InjectedClass {
  name: string = 'InjectedClass';
}

@Service()
class BaseClass {
  name: string = 'BaseClass';

  @Inject()
  injectedClass: InjectedClass;
}

@Service()
class ExtendedClass extends BaseClass {
  name: string = 'ExtendedClass';
}

const instance = Container.get(ExtendedClass);
// instance has the `name` property with "ExtendedClass" value (overwritten the base class)
// and the `injectedClass` property with the instance of the `InjectedClass` class

console.log(instance.injectedClass.name);
// logs "InjectedClass"
console.log(instance.name);
// logs "ExtendedClass"
```
```

## File: `docs/typescript/07-usage-with-typeorm.md`
```markdown
# Usage with TypeORM and routing-controllers

To use TypeDI with routing-controllers and/or TypeORM, it's required to configure them to use the top-level
TypeDI container used by your application.

```ts
import { useContainer as rcUseContainer } from 'routing-controllers';
import { useContainer as typeOrmUseContainer } from 'typeorm';
import { Container } from 'typedi';

rcUseContainer(Container);
typeOrmUseContainer(Container);
```
```

## File: `docs/typescript/08-custom-decorators.md`
```markdown
# Creating custom decorators

> **NOTE:** This page is a direct copy of the old documentation. It will be reworked.

You can create your own decorators which will inject your given values for your service dependencies. For example:

```ts
// Logger.ts
export function Logger() {
  return function (object: Object, propertyName: string, index?: number) {
    const logger = new ConsoleLogger();
    Container.registerHandler({ object, propertyName, index, value: containerInstance => logger });
  };
}

// LoggerInterface.ts
export interface LoggerInterface {
  log(message: string): void;
}

// ConsoleLogger.ts
import { LoggerInterface } from './LoggerInterface';

export class ConsoleLogger implements LoggerInterface {
  log(message: string) {
    console.log(message);
  }
}

// UserRepository.ts
@Service()
export class UserRepository {
  constructor(@Logger() private logger: LoggerInterface) {}

  save(user: User) {
    this.logger.log(`user ${user.firstName} ${user.secondName} has been saved.`);
  }
}
```
```

## File: `src/container-instance.class.ts`
```typescript
import { ServiceNotFoundError } from './error/service-not-found.error';
import { CannotInstantiateValueError } from './error/cannot-instantiate-value.error';
import { Token } from './token.class';
import { Constructable } from './types/constructable.type';
import { ServiceIdentifier } from './types/service-identifier.type';
import { ServiceMetadata } from './interfaces/service-metadata.interface';
import { ServiceOptions } from './interfaces/service-options.interface';
import { EMPTY_VALUE } from './empty.const';
import { ContainerIdentifier } from './types/container-identifier.type';
import { Handler } from './interfaces/handler.interface';
import { ContainerRegistry } from './container-registry.class';
import { ContainerScope } from './types/container-scope.type';

/**
 * TypeDI can have multiple containers.
 * One container is ContainerInstance.
 */
export class ContainerInstance {
  /** Container instance id. */
  public readonly id!: ContainerIdentifier;

  /** Metadata for all registered services in this container. */
  private metadataMap: Map<ServiceIdentifier, ServiceMetadata<unknown>> = new Map();

  /**
   * Services registered with 'multiple: true' are saved as simple services
   * with a generated token and the mapping between the original ID and the
   * generated one is stored here. This is handled like this to allow simplifying
   * the inner workings of the service instance.
   */
  private multiServiceIds: Map<ServiceIdentifier, { tokens: Token<unknown>[]; scope: ContainerScope }> = new Map();

  /**
   * All registered handlers. The @Inject() decorator uses handlers internally to mark a property for injection.
   **/
  private readonly handlers: Handler[] = [];

  /**
   * Indicates if the container has been disposed or not.
   * Any function call should fail when called after being disposed.
   *
   * NOTE: Currently not in used
   */
  private disposed: boolean = false;

  constructor(id: ContainerIdentifier) {
    this.id = id;

    ContainerRegistry.registerContainer(this);

    /**
     * TODO: This is to replicate the old functionality. This should be copied only
     * TODO: if the container decides to inherit registered classes from a parent container.
     */
    this.handlers = ContainerRegistry.defaultContainer?.handlers || [];
  }

  /**
   * Checks if the service with given name or type is registered service container.
   * Optionally, parameters can be passed in case if instance is initialized in the container for the first time.
   */
  public has<T = unknown>(identifier: ServiceIdentifier<T>): boolean {
    this.throwIfDisposed();

    return !!this.metadataMap.has(identifier) || !!this.multiServiceIds.has(identifier);
  }

  /**
   * Retrieves the service with given name or type from the service container.
   * Optionally, parameters can be passed in case if instance is initialized in the container for the first time.
   */
  public get<T = unknown>(identifier: ServiceIdentifier<T>): T {
    this.throwIfDisposed();

    const global = ContainerRegistry.defaultContainer.metadataMap.get(identifier);
    const local = this.metadataMap.get(identifier);
    /** If the service is registered as global we load it from there, otherwise we use the local one. */
    const metadata = global?.scope === 'singleton' ? global : local;

    /** This should never happen as multi services are masked with custom token in Container.set. */
    if (metadata && metadata.multiple === true) {
      throw new Error(`Cannot resolve multiple values for ${identifier.toString()} service!`);
    }

    /** Otherwise it's returned from the current container. */
    if (metadata) {
      return this.getServiceValue(metadata);
    }

    /**
     * If it's the first time requested in the child container we load it from parent and set it.
     * TODO: This will be removed with the container inheritance rework.
     */
    if (global && this !== ContainerRegistry.defaultContainer) {
      const clonedService = { ...global };
      clonedService.value = EMPTY_VALUE;

      /**
       * We need to immediately set the empty value from the root container
       * to prevent infinite lookup in cyclic dependencies.
       */
      this.set(clonedService);

      const value = this.getServiceValue(clonedService);
      this.set({ ...clonedService, value });

      return value;
    }

    throw new ServiceNotFoundError(identifier);
  }

  /**
   * Gets all instances registered in the container of the given service identifier.
   * Used when service defined with multiple: true flag.
   */
  public getMany<T = unknown>(identifier: ServiceIdentifier<T>): T[] {
    this.throwIfDisposed();

    const globalIdMap = ContainerRegistry.defaultContainer.multiServiceIds.get(identifier);
    const localIdMap = this.multiServiceIds.get(identifier);

    /**
     * If the service is registered as singleton we load it from default
     * container, otherwise we use the local one.
     */
    if (globalIdMap?.scope === 'singleton') {
      return globalIdMap.tokens.map(generatedId => ContainerRegistry.defaultContainer.get<T>(generatedId));
    }

    if (localIdMap) {
      return localIdMap.tokens.map(generatedId => this.get<T>(generatedId));
    }

    throw new ServiceNotFoundError(identifier);
  }

  /**
   * Sets a value for the given type or service name in the container.
   */
  public set<T = unknown>(serviceOptions: ServiceOptions<T>): this {
    this.throwIfDisposed();

    /**
     * If the service is marked as singleton, we set it in the default container.
     * (And avoid an infinite loop via checking if we are in the default container or not.)
     */
    if (serviceOptions.scope === 'singleton' && ContainerRegistry.defaultContainer !== this) {
      ContainerRegistry.defaultContainer.set(serviceOptions);

      return this;
    }

    const newMetadata: ServiceMetadata<T> = {
      /**
       * Typescript cannot understand that if ID doesn't exists then type must exists based on the
       * typing so we need to explicitly cast this to a `ServiceIdentifier`
       */
      id: ((serviceOptions as any).id || (serviceOptions as any).type) as ServiceIdentifier,
      type: (serviceOptions as ServiceMetadata<T>).type || null,
      factory: (serviceOptions as ServiceMetadata<T>).factory,
      value: (serviceOptions as ServiceMetadata<T>).value || EMPTY_VALUE,
      multiple: serviceOptions.multiple || false,
      eager: serviceOptions.eager || false,
      scope: serviceOptions.scope || 'container',
      /** We allow overriding the above options via the received config object. */
      ...serviceOptions,
      referencedBy: new Map().set(this.id, this),
    };

    /** If the incoming metadata is marked as multiple we mask the ID and continue saving as single value. */
    if (serviceOptions.multiple) {
      const maskedToken = new Token(`MultiMaskToken-${newMetadata.id.toString()}`);
      const existingMultiGroup = this.multiServiceIds.get(newMetadata.id);

      if (existingMultiGroup) {
        existingMultiGroup.tokens.push(maskedToken);
      } else {
        this.multiServiceIds.set(newMetadata.id, { scope: newMetadata.scope, tokens: [maskedToken] });
      }

      /**
       * We mask the original metadata with this generated ID, mark the service
       * as  and continue multiple: false and continue. Marking it as
       * non-multiple is important otherwise Container.get would refuse to
       * resolve the value.
       */
      newMetadata.id = maskedToken;
      newMetadata.multiple = false;
    }

    const existingMetadata = this.metadataMap.get(newMetadata.id);

    if (existingMetadata) {
      /** Service already exists, we overwrite it. (This is legacy behavior.) */
      // TODO: Here we should differentiate based on the received set option.
      Object.assign(existingMetadata, newMetadata);
    } else {
      /** This service hasn't been registered yet, so we register it. */
      this.metadataMap.set(newMetadata.id, newMetadata);
    }

    /**
     * If the service is eager, we need to create an instance immediately except
     * when the service is also marked as transient. In that case we ignore
     * the eager flag to prevent creating a service what cannot be disposed later.
     */
    if (newMetadata.eager && newMetadata.scope !== 'transient') {
      this.get(newMetadata.id);
    }

    return this;
  }

  /**
   * Removes services with a given service identifiers.
   */
  public remove(identifierOrIdentifierArray: ServiceIdentifier | ServiceIdentifier[]): this {
    this.throwIfDisposed();

    if (Array.isArray(identifierOrIdentifierArray)) {
      identifierOrIdentifierArray.forEach(id => this.remove(id));
    } else {
      const serviceMetadata = this.metadataMap.get(identifierOrIdentifierArray);

      if (serviceMetadata) {
        this.disposeServiceInstance(serviceMetadata);
        this.metadataMap.delete(identifierOrIdentifierArray);
      }
    }

    return this;
  }

  /**
   * Gets a separate container instance for the given instance id.
   */
  public of(containerId: ContainerIdentifier = 'default'): ContainerInstance {
    this.throwIfDisposed();

    if (containerId === 'default') {
      return ContainerRegistry.defaultContainer;
    }

    let container: ContainerInstance;

    if (ContainerRegistry.hasContainer(containerId)) {
      container = ContainerRegistry.getContainer(containerId);
    } else {
      /**
       * This is deprecated functionality, for now we create the container if it's doesn't exists.
       * This will be reworked when container inheritance is reworked.
       */
      container = new ContainerInstance(containerId);
    }

    return container;
  }

  /**
   * Registers a new handler.
   */
  public registerHandler(handler: Handler): ContainerInstance {
    this.handlers.push(handler);
    return this;
  }

  /**
   * Helper method that imports given services.
   */
  /* eslint-disable-next-line @typescript-eslint/no-unused-vars */
  public import(services: Function[]): ContainerInstance {
    this.throwIfDisposed();

    return this;
  }

  /**
   * Completely resets the container by removing all previously registered services from it.
   */
  public reset(options: { strategy: 'resetValue' | 'resetServices' } = { strategy: 'resetValue' }): this {
    this.throwIfDisposed();

    switch (options.strategy) {
      case 'resetValue':
        this.metadataMap.forEach(service => this.disposeServiceInstance(service));
        break;
      case 'resetServices':
        this.metadataMap.forEach(service => this.disposeServiceInstance(service));
        this.metadataMap.clear();
        this.multiServiceIds.clear();
        break;
      default:
        throw new Error('Received invalid reset strategy.');
    }
    return this;
  }

  public async dispose(): Promise<void> {
    this.reset({ strategy: 'resetServices' });

    /** We mark the container as disposed, forbidding any further interaction with it. */
    this.disposed = true;

    /**
     * Placeholder, this function returns a promise in preparation to support async services.
     */
    await Promise.resolve();
  }

  private throwIfDisposed() {
    if (this.disposed) {
      // TODO: Use custom error.
      throw new Error('Cannot use container after it has been disposed.');
    }
  }

  /**
   * Gets the value belonging to passed in `ServiceMetadata` instance.
   *
   * - if `serviceMetadata.value` is already set it is immediately returned
   * - otherwise the requested type is resolved to the value saved to `serviceMetadata.value` and returned
   */
  private getServiceValue(serviceMetadata: ServiceMetadata<unknown>): any {
    let value: unknown = EMPTY_VALUE;

    /**
     * If the service value has been set to anything prior to this call we return that value.
     * NOTE: This part builds on the assumption that transient dependencies has no value set ever.
     */
    if (serviceMetadata.value !== EMPTY_VALUE) {
      return serviceMetadata.value;
    }

    /** If both factory and type is missing, we cannot resolve the requested ID. */
    if (!serviceMetadata.factory && !serviceMetadata.type) {
      throw new CannotInstantiateValueError(serviceMetadata.id);
    }

    /**
     * If a factory is defined it takes priority over creating an instance via `new`.
     * The return value of the factory is not checked, we believe by design that the user knows what he/she is doing.
     */
    if (serviceMetadata.factory) {
      /**
       * If we received the factory in the [Constructable<Factory>, "functionName"] format, we need to create the
       * factory first and then call the specified function on it.
       */
      if (serviceMetadata.factory instanceof Array) {
        let factoryInstance;

        try {
          /** Try to get the factory from TypeDI first, if failed, fall back to simply initiating the class. */
          factoryInstance = this.get<any>(serviceMetadata.factory[0]);
        } catch (error) {
          if (error instanceof ServiceNotFoundError) {
            factoryInstance = new serviceMetadata.factory[0]();
          } else {
            throw error;
          }
        }

        value = factoryInstance[serviceMetadata.factory[1]](this, serviceMetadata.id);
      } else {
        /** If only a simple function was provided we simply call it. */
        value = serviceMetadata.factory(this, serviceMetadata.id);
      }
    }

    /**
     * If no factory was provided and only then, we create the instance from the type if it was set.
     */
    if (!serviceMetadata.factory && serviceMetadata.type) {
      const constructableTargetType: Constructable<unknown> = serviceMetadata.type;
      // setup constructor parameters for a newly initialized service
      const paramTypes: unknown[] = (Reflect as any)?.getMetadata('design:paramtypes', constructableTargetType) || [];
      const params = this.initializeParams(constructableTargetType, paramTypes);

      // "extra feature" - always pass container instance as the last argument to the service function
      // this allows us to support javascript where we don't have decorators and emitted metadata about dependencies
      // need to be injected, and user can use provided container to get instances he needs
      params.push(this);

      value = new constructableTargetType(...params);

      // TODO: Calling this here, leads to infinite loop, because @Inject decorator registerds a handler
      // TODO: which calls Container.get, which will check if the requested type has a value set and if not
      // TODO: it will start the instantiation process over. So this is currently called outside of the if branch
      // TODO: after the current value has been assigned to the serviceMetadata.
      // this.applyPropertyHandlers(constructableTargetType, value as Constructable<unknown>);
    }

    /** If this is not a transient service, and we resolved something, then we set it as the value. */
    if (serviceMetadata.scope !== 'transient' && value !== EMPTY_VALUE) {
      serviceMetadata.value = value;
    }

    if (value === EMPTY_VALUE) {
      /** This branch should never execute, but better to be safe than sorry. */
      throw new CannotInstantiateValueError(serviceMetadata.id);
    }

    if (serviceMetadata.type) {
      this.applyPropertyHandlers(serviceMetadata.type, value as Record<string, any>);
    }

    return value;
  }

  /**
   * Initializes all parameter types for a given target service class.
   */
  private initializeParams(target: Function, paramTypes: any[]): unknown[] {
    return paramTypes.map((paramType, index) => {
      const paramHandler =
        this.handlers.find(handler => {
          /**
           * @Inject()-ed values are stored as parameter handlers and they reference their target
           * when created. So when a class is extended the @Inject()-ed values are not inherited
           * because the handler still points to the old object only.
           *
           * As a quick fix a single level parent lookup is added via `Object.getPrototypeOf(target)`,
           * however this should be updated to a more robust solution.
           *
           * TODO: Add proper inheritance handling: either copy the handlers when a class is registered what
           * TODO: has it's parent already registered as dependency or make the lookup search up to the base Object.
           */
          return handler.object === target && handler.index === index;
        }) ||
        this.handlers.find(handler => {
          return handler.object === Object.getPrototypeOf(target) && handler.index === index;
        });

      if (paramHandler) return paramHandler.value(this);

      // eslint-disable-next-line @typescript-eslint/no-unsafe-argument
      if (paramType && paramType.name && !this.isPrimitiveParamType(paramType.name)) {
        // eslint-disable-next-line @typescript-eslint/no-unsafe-argument
        return this.get(paramType);
      }

      return undefined;
    });
  }

  /**
   * Checks if given parameter type is primitive type or not.
   */
  private isPrimitiveParamType(paramTypeName: string): boolean {
    return ['string', 'boolean', 'number', 'object'].includes(paramTypeName.toLowerCase());
  }

  /**
   * Applies all registered handlers on a given target class.
   */
  private applyPropertyHandlers(target: Function, instance: { [key: string]: any }) {
    this.handlers.forEach(handler => {
      if (typeof handler.index === 'number') return;
      if (handler.object.constructor !== target && !(target.prototype instanceof handler.object.constructor)) return;

      if (handler.propertyName) {
        instance[handler.propertyName] = handler.value(this);
      }
    });
  }

  /**
   * Checks if the given service metadata contains a destroyable service instance and destroys it in place. If the service
   * contains a callable function named `destroy` it is called but not awaited and the return value is ignored..
   *
   * @param serviceMetadata the service metadata containing the instance to destroy
   * @param force when true the service will be always destroyed even if it's cannot be re-created
   */
  private disposeServiceInstance(serviceMetadata: ServiceMetadata, force = false) {
    this.throwIfDisposed();

    /** We reset value only if we can re-create it (aka type or factory exists). */
    const shouldResetValue = force || !!serviceMetadata.type || !!serviceMetadata.factory;

    if (shouldResetValue) {
      /** If we wound a function named destroy we call it without any params. */
      if (typeof (serviceMetadata?.value as Record<string, unknown>)['dispose'] === 'function') {
        try {
          (serviceMetadata.value as { dispose: CallableFunction }).dispose();
        } catch (error) {
          /** We simply ignore the errors from the destroy function. */
        }
      }

      serviceMetadata.value = EMPTY_VALUE;
    }
  }
}
```

## File: `src/container-registry.class.ts`
```typescript
import { ContainerInstance } from './container-instance.class';
import { ContainerIdentifier } from './types/container-identifier.type';

/**
 * The container registry is responsible for holding the default and every
 * created container instance for later access.
 *
 * _Note: This class is for internal use and it's API may break in minor or
 * patch releases without warning._
 */
export class ContainerRegistry {
  /**
   * The list of all known container. Created containers are automatically added
   * to this list. Two container cannot be registered with the same ID.
   *
   * This map doesn't contains the default container.
   */
  private static readonly containerMap: Map<ContainerIdentifier, ContainerInstance> = new Map();

  /**
   * The default global container. By default services are registered into this
   * container when registered via `Container.set()` or `@Service` decorator.
   */
  public static readonly defaultContainer: ContainerInstance = new ContainerInstance('default');

  /**
   * Registers the given container instance or throws an error.
   *
   * _Note: This function is auto-called when a Container instance is created,
   * it doesn't need to be called manually!_
   *
   * @param container the container to add to the registry
   */
  public static registerContainer(container: ContainerInstance): void {
    if (container instanceof ContainerInstance === false) {
      // TODO: Create custom error for this.
      throw new Error('Only ContainerInstance instances can be registered.');
    }

    /** If we already set the default container (in index) then no-one else can register a default. */
    if (!!ContainerRegistry.defaultContainer && container.id === 'default') {
      // TODO: Create custom error for this.
      throw new Error('You cannot register a container with the "default" ID.');
    }

    if (ContainerRegistry.containerMap.has(container.id)) {
      // TODO: Create custom error for this.
      throw new Error('Cannot register container with same ID.');
    }

    ContainerRegistry.containerMap.set(container.id, container);
  }

  /**
   * Returns true if a container exists with the given ID or false otherwise.
   *
   * @param container the ID of the container
   */
  public static hasContainer(id: ContainerIdentifier): boolean {
    return ContainerRegistry.containerMap.has(id);
  }

  /**
   * Returns the container for requested ID or throws an error if no container
   * is registered with the given ID.
   *
   * @param container the ID of the container
   */
  public static getContainer(id: ContainerIdentifier): ContainerInstance {
    const registeredContainer = this.containerMap.get(id);

    if (registeredContainer === undefined) {
      // TODO: Create custom error for this.
      throw new Error('No container is registered with the given ID.');
    }

    return registeredContainer;
  }

  /**
   * Removes the given container from the registry and disposes all services
   * registered only in this container.
   *
   * This function throws an error if no
   *   - container exists with the given ID
   *   - any of the registered services threw an error during it's disposal
   *
   * @param container the container to remove from the registry
   */
  public static async removeContainer(container: ContainerInstance): Promise<void> {
    const registeredContainer = ContainerRegistry.containerMap.get(container.id);

    if (registeredContainer === undefined) {
      // TODO: Create custom error for this.
      throw new Error('No container is registered with the given ID.');
    }

    /** We remove the container first. */
    ContainerRegistry.containerMap.delete(container.id);

    /** We dispose all registered classes in the container. */
    await registeredContainer.dispose();
  }
}
```

## File: `src/empty.const.ts`
```typescript
/**
 * Indicates that a service has not been initialized yet.
 *
 * _Note: This value is for internal use only._
 */
export const EMPTY_VALUE = Symbol('EMPTY_VALUE');
```

## File: `src/index.ts`
```typescript
/**
 * We have a hard dependency on reflect-metadata package. Without it the
 * dependency lookup won't work, so we warn users when it's not loaded.
 */
if (!Reflect || !(Reflect as any).getMetadata) {
  throw new Error(
    'TypeDI requires "Reflect.getMetadata" to work. Please import the "reflect-metadata" package at the very first line of your application.'
  );
}

/** This is an internal package, so we don't re-export it on purpose. */
import { ContainerRegistry } from './container-registry.class';

export * from './decorators/inject-many.decorator';
export * from './decorators/inject.decorator';
export * from './decorators/service.decorator';

export * from './error/cannot-inject-value.error';
export * from './error/cannot-instantiate-value.error';
export * from './error/service-not-found.error';

export { Handler } from './interfaces/handler.interface';
export { ServiceMetadata } from './interfaces/service-metadata.interface';
export { ServiceOptions } from './interfaces/service-options.interface';
export { Constructable } from './types/constructable.type';
export { ServiceIdentifier } from './types/service-identifier.type';

export { ContainerInstance } from './container-instance.class';
export { Token } from './token.class';

/** We export the default container under the Container alias. */
export const Container = ContainerRegistry.defaultContainer;
export default Container;
```

## File: `src/token.class.ts`
```typescript
/**
 * Used to create unique typed service identifier.
 * Useful when service has only interface, but don't have a class.
 */
/* eslint-disable-next-line @typescript-eslint/no-unused-vars */
export class Token<T> {
  /**
   * @param name Token name, optional and only used for debugging purposes.
   */
  constructor(public name?: string) {}
}
```

## File: `src/decorators/inject-many.decorator.ts`
```typescript
import { ContainerRegistry } from '../container-registry.class';
import { Token } from '../token.class';
import { CannotInjectValueError } from '../error/cannot-inject-value.error';
import { resolveToTypeWrapper } from '../utils/resolve-to-type-wrapper.util';
import { Constructable } from '../types/constructable.type';
import { ServiceIdentifier } from '../types/service-identifier.type';

/**
 * Injects a list of services into a class property or constructor parameter.
 */
export function InjectMany(): Function;
export function InjectMany(type?: (type?: any) => Function): Function;
export function InjectMany(serviceName?: string): Function;
export function InjectMany(token: Token<any>): Function;
export function InjectMany(
  typeOrIdentifier?: ((type?: never) => Constructable<unknown>) | ServiceIdentifier<unknown>
): Function {
  return function (target: Object, propertyName: string | Symbol, index?: number): void {
    const typeWrapper = resolveToTypeWrapper(typeOrIdentifier, target, propertyName, index);

    /** If no type was inferred, or the general Object type was inferred we throw an error. */
    if (typeWrapper === undefined || typeWrapper.eagerType === undefined || typeWrapper.eagerType === Object) {
      throw new CannotInjectValueError(target as Constructable<unknown>, propertyName as string);
    }

    ContainerRegistry.defaultContainer.registerHandler({
      object: target as Constructable<unknown>,
      propertyName: propertyName as string,
      index: index,
      value: containerInstance => {
        const evaluatedLazyType = typeWrapper.lazyType();

        /** If no type was inferred lazily, or the general Object type was inferred we throw an error. */
        if (evaluatedLazyType === undefined || evaluatedLazyType === Object) {
          throw new CannotInjectValueError(target as Constructable<unknown>, propertyName as string);
        }

        return containerInstance.getMany<unknown>(evaluatedLazyType);
      },
    });
  };
}
```

## File: `src/decorators/inject.decorator.ts`
```typescript
import { ContainerRegistry } from '../container-registry.class';
import { Token } from '../token.class';
import { CannotInjectValueError } from '../error/cannot-inject-value.error';
import { ServiceIdentifier } from '../types/service-identifier.type';
import { Constructable } from '../types/constructable.type';
import { resolveToTypeWrapper } from '../utils/resolve-to-type-wrapper.util';

/**
 * Injects a service into a class property or constructor parameter.
 */
export function Inject(): Function;
export function Inject(typeFn: (type?: never) => Constructable<unknown>): Function;
export function Inject(serviceName?: string): Function;
export function Inject(token: Token<unknown>): Function;
export function Inject(
  typeOrIdentifier?: ((type?: never) => Constructable<unknown>) | ServiceIdentifier<unknown>
): ParameterDecorator | PropertyDecorator {
  return function (target: Object, propertyName: string | Symbol, index?: number): void {
    const typeWrapper = resolveToTypeWrapper(typeOrIdentifier, target, propertyName, index);

    /** If no type was inferred, or the general Object type was inferred we throw an error. */
    if (typeWrapper === undefined || typeWrapper.eagerType === undefined || typeWrapper.eagerType === Object) {
      throw new CannotInjectValueError(target as Constructable<unknown>, propertyName as string);
    }

    ContainerRegistry.defaultContainer.registerHandler({
      object: target as Constructable<unknown>,
      propertyName: propertyName as string,
      index: index,
      value: containerInstance => {
        const evaluatedLazyType = typeWrapper.lazyType();

        /** If no type was inferred lazily, or the general Object type was inferred we throw an error. */
        if (evaluatedLazyType === undefined || evaluatedLazyType === Object) {
          throw new CannotInjectValueError(target as Constructable<unknown>, propertyName as string);
        }

        return containerInstance.get<unknown>(evaluatedLazyType);
      },
    });
  };
}
```

## File: `src/decorators/service.decorator.ts`
```typescript
import { ContainerRegistry } from '../container-registry.class';
import { ServiceMetadata } from '../interfaces/service-metadata.interface';
import { ServiceOptions } from '../interfaces/service-options.interface';
import { EMPTY_VALUE } from '../empty.const';
import { Constructable } from '../types/constructable.type';

/**
 * Marks class as a service that can be injected using Container.
 */
/* eslint-disable-next-line @typescript-eslint/no-unused-vars */
export function Service<T = unknown>(): Function;
export function Service<T = unknown>(options: ServiceOptions<T>): Function;
export function Service<T>(options: ServiceOptions<T> = {}): ClassDecorator {
  return targetConstructor => {
    const serviceMetadata: ServiceMetadata<T> = {
      id: options.id || targetConstructor,
      type: targetConstructor as unknown as Constructable<T>,
      factory: (options as any).factory || undefined,
      multiple: options.multiple || false,
      eager: options.eager || false,
      scope: options.scope || 'container',
      referencedBy: new Map().set(ContainerRegistry.defaultContainer.id, ContainerRegistry.defaultContainer),
      value: EMPTY_VALUE,
    };

    ContainerRegistry.defaultContainer.set(serviceMetadata);
  };
}
```

## File: `src/error/cannot-inject-value.error.ts`
```typescript
import { Constructable } from '../types/constructable.type';

/**
 * Thrown when DI cannot inject value into property decorated by @Inject decorator.
 */
export class CannotInjectValueError extends Error {
  public name = 'CannotInjectValueError';

  get message(): string {
    return (
      `Cannot inject value into "${this.target.constructor.name}.${this.propertyName}". ` +
      `Please make sure you setup reflect-metadata properly and you don't use interfaces without service tokens as injection value.`
    );
  }

  constructor(private target: Constructable<unknown>, private propertyName: string) {
    super();
  }
}
```

## File: `src/error/cannot-instantiate-value.error.ts`
```typescript
import { ServiceIdentifier } from '../types/service-identifier.type';
import { Token } from '../token.class';

/**
 * Thrown when DI cannot inject value into property decorated by @Inject decorator.
 */
export class CannotInstantiateValueError extends Error {
  public name = 'CannotInstantiateValueError';

  /** Normalized identifier name used in the error message. */
  private normalizedIdentifier: string = '<UNKNOWN_IDENTIFIER>';

  get message(): string {
    return (
      `Cannot instantiate the requested value for the "${this.normalizedIdentifier}" identifier. ` +
      `The related metadata doesn't contain a factory or a type to instantiate.`
    );
  }

  constructor(identifier: ServiceIdentifier) {
    super();

    // TODO: Extract this to a helper function and share between this and NotFoundError.
    if (typeof identifier === 'string') {
      this.normalizedIdentifier = identifier;
    } else if (identifier instanceof Token) {
      this.normalizedIdentifier = `Token<${identifier.name || 'UNSET_NAME'}>`;
    } else if (identifier && (identifier.name || identifier.prototype?.name)) {
      this.normalizedIdentifier =
        `MaybeConstructable<${identifier.name}>` ||
        `MaybeConstructable<${(identifier.prototype as { name: string })?.name}>`;
    }
  }
}
```

## File: `src/error/service-not-found.error.ts`
```typescript
import { ServiceIdentifier } from '../types/service-identifier.type';
import { Token } from '../token.class';

/**
 * Thrown when requested service was not found.
 */
export class ServiceNotFoundError extends Error {
  public name = 'ServiceNotFoundError';

  /** Normalized identifier name used in the error message. */
  private normalizedIdentifier: string = '<UNKNOWN_IDENTIFIER>';

  get message(): string {
    return (
      `Service with "${this.normalizedIdentifier}" identifier was not found in the container. ` +
      `Register it before usage via explicitly calling the "Container.set" function or using the "@Service()" decorator.`
    );
  }

  constructor(identifier: ServiceIdentifier) {
    super();

    if (typeof identifier === 'string') {
      this.normalizedIdentifier = identifier;
    } else if (identifier instanceof Token) {
      this.normalizedIdentifier = `Token<${identifier.name || 'UNSET_NAME'}>`;
    } else if (identifier && (identifier.name || identifier.prototype?.name)) {
      this.normalizedIdentifier =
        `MaybeConstructable<${identifier.name}>` ||
        `MaybeConstructable<${(identifier.prototype as { name: string })?.name}>`;
    }
  }
}
```

## File: `src/interfaces/container-options.interface.ts`
```typescript
export interface ContainerOptions {
  /**
   * Controls the behavior when a service is already registered with the same ID. The following values are allowed:
   *
   *   - `throw` - a `ContainerCannotBeCreatedError` error is raised
   *   - `overwrite` - the previous container is disposed and a new one is created
   *   - `returnExisting` - returns the existing container or raises a `ContainerCannotBeCreatedError` error if the
   *      specified options differ from the options of the existing container
   *
   * The default value is `returnExisting`.
   */
  onConflict: 'throw' | 'overwrite' | 'returnExisting';

  /**
   * Controls the behavior when a requested type doesn't exists in the current container. The following values are allowed:
   *
   *   - `allowLookup` - the parent container will be checked for the dependency
   *   - `localOnly` - a `ServiceNotFoundError` error is raised
   *
   * The default value is `allowLookup`.
   */
  lookupStrategy: 'allowLookup' | 'localOnly';

  /**
   * Enables the lookup for global (singleton) services before checking in the current container. By default every
   * type is first checked in the default container to return singleton services. This check bypasses the lookup strategy,
   * set in the container so if this behavior is not desired it can be disabled via this flag.
   *
   * The default value is `true`.
   */
  allowSingletonLookup: boolean;

  /**
   * Controls how the child container inherits the service definitions from it's parent. The following values are allowed:
   *
   *  - `none` - no metadata is inherited
   *  - `definitionOnly` - only metadata is inherited, a new instance will be created for each class
   *    - eager classes created as soon as the container is created
   *    - non-eager classes are created the first time they are requested
   *  - `definitionWithValues` - both metadata and service instances are inherited
   *    - when parent class is disposed the instances in this container are preserved
   *    - if a service is registered but not created yet, it will be shared when created between the two container
   *    - newly registered services won't be shared between the two container
   *
   * The default value is `none`.
   */
  inheritanceStrategy: 'none' | 'definitionOnly' | 'definitionWithValues';
}
```

## File: `src/interfaces/handler.interface.ts`
```typescript
import { ContainerInstance } from '../container-instance.class';
import { Constructable } from '../types/constructable.type';

/**
 * Used to register special "handler" which will be executed on a service class during its initialization.
 * It can be used to create custom decorators and set/replace service class properties and constructor parameters.
 */
export interface Handler<T = unknown> {
  /**
   * Service object used to apply handler to.
   */
  object: Constructable<T>;

  /**
   * Class property name to set/replace value of.
   * Used if handler is applied on a class property.
   */
  propertyName?: string;

  /**
   * Parameter index to set/replace value of.
   * Used if handler is applied on a constructor parameter.
   */
  index?: number;

  /**
   * Factory function that produces value that will be set to class property or constructor parameter.
   * Accepts container instance which requested the value.
   */
  value: (container: ContainerInstance) => any;
}
```

## File: `src/interfaces/service-metadata.interface.ts`
```typescript
import { ContainerInstance } from '../container-instance.class';
import { Constructable } from '../types/constructable.type';
import { ContainerIdentifier } from '../types/container-identifier.type';
import { ContainerScope } from '../types/container-scope.type';
import { ServiceIdentifier } from '../types/service-identifier.type';

/**
 * Service metadata is used to initialize service and store its state.
 */
export interface ServiceMetadata<Type = unknown> {
  /** Unique identifier of the referenced service. */
  id: ServiceIdentifier;

  /**
   * The injection scope for the service.
   *   - a `singleton` service always will be created in the default container regardless of who registering it
   *   - a `container` scoped service will be created once when requested from the given container
   *   - a `transient` service will be created each time it is requested
   */
  scope: ContainerScope;

  /**
   * Class definition of the service what is used to initialize given service.
   * This property maybe null if the value of the service is set manually.
   * If id is not set then it serves as service id.
   */
  type: Constructable<Type> | null;

  /**
   * Factory function used to initialize this service.
   * Can be regular function ("createCar" for example),
   * or other service which produces this instance ([CarFactory, "createCar"] for example).
   */
  factory: [Constructable<unknown>, string] | CallableFunction | undefined;

  /**
   * Instance of the target class.
   */
  value: unknown | Symbol;

  /**
   * Allows to setup multiple instances the different classes under a single service id string or token.
   */
  multiple: boolean;

  /**
   * Indicates whether a new instance should be created as soon as the class is registered.
   * By default the registered classes are only instantiated when they are requested from the container.
   *
   * _Note: This option is ignored for transient services._
   */
  eager: boolean;

  /**
   * Map of containers referencing this metadata. This is used when a container
   * is inheriting it's parents definitions and values to track the lifecycle of
   * the metadata. Namely, a service can be disposed only if it's only referenced
   * by the container being disposed.
   */
  referencedBy: Map<ContainerIdentifier, ContainerInstance>;
}
```

## File: `src/interfaces/service-options.interface.ts`
```typescript
import { ServiceMetadata } from './service-metadata.interface';

/**
 * The public ServiceOptions is partial object of ServiceMetadata and either one
 * of the following is set: `type`, `factory`, `value` but not more than one.
 */
export type ServiceOptions<T = unknown> =
  | Omit<Partial<ServiceMetadata<T>>, 'referencedBy' | 'type' | 'factory'>
  | Omit<Partial<ServiceMetadata<T>>, 'referencedBy' | 'value' | 'factory'>
  | Omit<Partial<ServiceMetadata<T>>, 'referencedBy' | 'value' | 'type'>;
```

## File: `src/types/abstract-constructable.type.ts`
```typescript
/**
 * Generic type for abstract class definitions.
 *
 * Explanation: This describes a newable Function with a prototype Which is
 * what an abstract class is - no constructor, just the prototype.
 */
export type AbstractConstructable<T> = NewableFunction & { prototype: T };
```

## File: `src/types/constructable.type.ts`
```typescript
/**
 * Generic type for class definitions.
 * Example usage:
 * ```
 * function createSomeInstance(myClassDefinition: Constructable<MyClass>) {
 *   return new myClassDefinition()
 * }
 * ```
 */
export type Constructable<T> = new (...args: any[]) => T;
```

## File: `src/types/container-identifier.type.ts`
```typescript
/**
 * A container identifier. This value must be unique across all containers.
 */
export type ContainerIdentifier = string | Symbol;
```

## File: `src/types/container-scope.type.ts`
```typescript
export type ContainerScope = 'singleton' | 'container' | 'transient';
```

## File: `src/types/service-identifier.type.ts`
```typescript
import { Token } from '../token.class';
import { Constructable } from './constructable.type';
import { AbstractConstructable } from './abstract-constructable.type';

/**
 * Unique service identifier.
 * Can be some class type, or string id, or instance of Token.
 */
export type ServiceIdentifier<T = unknown> =
  | Constructable<T>
  | AbstractConstructable<T>
  | CallableFunction
  | Token<T>
  | string;
```

## File: `src/utils/resolve-to-type-wrapper.util.ts`
```typescript
import { Token } from '../token.class';
import { Constructable } from '../types/constructable.type';
import { ServiceIdentifier } from '../types/service-identifier.type';

/**
 * Helper function used in inject decorators to resolve the received identifier to
 * an eager type when possible or to a lazy type when cyclic dependencies are possibly involved.
 *
 * @param typeOrIdentifier a service identifier or a function returning a type acting as service identifier or nothing
 * @param target the class definition of the target of the decorator
 * @param propertyName the name of the property in case of a PropertyDecorator
 * @param index the index of the parameter in the constructor in case of ParameterDecorator
 */
export function resolveToTypeWrapper(
  typeOrIdentifier: ((type?: never) => Constructable<unknown>) | ServiceIdentifier<unknown> | undefined,
  target: Object,
  propertyName: string | Symbol,
  index?: number
): { eagerType: ServiceIdentifier | null; lazyType: (type?: never) => ServiceIdentifier } {
  /**
   * ? We want to error out as soon as possible when looking up services to inject, however
   * ? we cannot determine the type at decorator execution when cyclic dependencies are involved
   * ? because calling the received `() => MyType` function right away would cause a JS error:
   * ? "Cannot access 'MyType' before initialization", so we need to execute the function in the handler,
   * ? when the classes are already created. To overcome this, we use a wrapper:
   * ?  - the lazyType is executed in the handler so we never have a JS error
   * ?  - the eagerType is checked when decorator is running and an error is raised if an unknown type is encountered
   */
  let typeWrapper!: { eagerType: ServiceIdentifier | null; lazyType: (type?: never) => ServiceIdentifier };

  /** If requested type is explicitly set via a string ID or token, we set it explicitly. */
  if ((typeOrIdentifier && typeof typeOrIdentifier === 'string') || typeOrIdentifier instanceof Token) {
    typeWrapper = { eagerType: typeOrIdentifier, lazyType: () => typeOrIdentifier };
  }

  /** If requested type is explicitly set via a () => MyClassType format, we set it explicitly. */
  if (typeOrIdentifier && typeof typeOrIdentifier === 'function') {
    /** We set eagerType to null, preventing the raising of the CannotInjectValueError in decorators.  */
    typeWrapper = { eagerType: null, lazyType: () => (typeOrIdentifier as CallableFunction)() };
  }

  /** If no explicit type is set and handler registered for a class property, we need to get the property type. */
  if (!typeOrIdentifier && propertyName) {
    const identifier = (Reflect as any).getMetadata('design:type', target, propertyName);

    typeWrapper = { eagerType: identifier, lazyType: () => identifier };
  }

  /** If no explicit type is set and handler registered for a constructor parameter, we need to get the parameter types. */
  if (!typeOrIdentifier && typeof index == 'number' && Number.isInteger(index)) {
    const paramTypes: ServiceIdentifier[] = (Reflect as any).getMetadata('design:paramtypes', target, propertyName);
    /** It's not guaranteed, that we find any types for the constructor. */
    const identifier = paramTypes?.[index];

    typeWrapper = { eagerType: identifier, lazyType: () => identifier };
  }

  return typeWrapper;
}
```

## File: `test/Container.spec.ts`
```typescript
import 'reflect-metadata';
import { Constructable, Container } from '../src/index';
import { Service } from '../src/decorators/service.decorator';
import { Token } from '../src/token.class';
import { ServiceNotFoundError } from '../src/error/service-not-found.error';

describe('Container', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  describe('get', () => {
    it('should be able to get a boolean', () => {
      const booleanTrue = 'boolean.true';
      const booleanFalse = 'boolean.false';
      Container.set({ id: booleanTrue, value: true });
      Container.set({ id: booleanFalse, value: false });

      expect(Container.get(booleanTrue)).toBe(true);
      expect(Container.get(booleanFalse)).toBe(false);
    });

    it('should be able to get an empty string', () => {
      const emptyString = 'emptyString';
      Container.set({ id: emptyString, value: '' });

      expect(Container.get(emptyString)).toBe('');
    });

    it('should be able to get the 0 number', () => {
      const zero = 'zero';
      Container.set({ id: zero, value: 0 });

      expect(Container.get(zero)).toBe(0);
    });
  });

  describe('set', function () {
    it('should be able to set a class into the container', function () {
      class TestService {
        constructor(public name: string) {}
      }
      const testService = new TestService('this is test');
      Container.set({ id: TestService, value: testService });
      expect(Container.get(TestService)).toBe(testService);
      expect(Container.get(TestService).name).toBe('this is test');
    });

    it('should be able to set a named service', function () {
      class TestService {
        constructor(public name: string) {}
      }
      const firstService = new TestService('first');
      Container.set({ id: 'first.service', value: firstService });

      const secondService = new TestService('second');
      Container.set({ id: 'second.service', value: secondService });

      expect(Container.get<TestService>('first.service').name).toBe('first');
      expect(Container.get<TestService>('second.service').name).toBe('second');
    });

    it('should be able to set a tokenized service', function () {
      class TestService {
        constructor(public name: string) {}
      }
      const FirstTestToken = new Token<TestService>();
      const SecondTestToken = new Token<TestService>();

      const firstService = new TestService('first');
      Container.set({ id: FirstTestToken, value: firstService });

      const secondService = new TestService('second');
      Container.set({ id: SecondTestToken, value: secondService });

      expect(Container.get(FirstTestToken).name).toBe('first');
      expect(Container.get(SecondTestToken).name).toBe('second');
    });

    it('should override previous value if service is written second time', function () {
      class TestService {
        constructor(public name: string) {}
      }
      const TestToken = new Token<TestService>();

      const firstService = new TestService('first');
      Container.set({ id: TestToken, value: firstService });
      expect(Container.get(TestToken)).toBe(firstService);
      expect(Container.get(TestToken).name).toBe('first');

      const secondService = new TestService('second');
      Container.set({ id: TestToken, value: secondService });

      expect(Container.get(TestToken)).toBe(secondService);
      expect(Container.get(TestToken).name).toBe('second');
    });
  });

  describe('set multiple', function () {
    it('should be able to provide a list of values', function () {
      class TestService {}

      class TestServiceFactory {
        create() {
          return 'test3-service-created-by-factory';
        }
      }

      const testService = new TestService();
      const test1Service = new TestService();
      const test2Service = new TestService();

      Container.set({ id: TestService, value: testService });
      Container.set({ id: 'test1-service', value: test1Service });
      Container.set({ id: 'test2-service', value: test2Service });
      Container.set({ id: 'test3-service', factory: [TestServiceFactory, 'create'] });

      expect(Container.get(TestService)).toBe(testService);
      expect(Container.get<TestService>('test1-service')).toBe(test1Service);
      expect(Container.get<TestService>('test2-service')).toBe(test2Service);
      expect(Container.get<string>('test3-service')).toBe('test3-service-created-by-factory');
    });
  });

  describe('remove', function () {
    it('should be able to remove previously registered services', function () {
      class TestService {
        constructor() {}
      }

      const testService = new TestService();
      const test1Service = new TestService();
      const test2Service = new TestService();

      Container.set({ id: TestService, value: testService });
      Container.set({ id: 'test1-service', value: test1Service });
      Container.set({ id: 'test2-service', value: test2Service });

      expect(Container.get(TestService)).toBe(testService);
      expect(Container.get<TestService>('test1-service')).toBe(test1Service);
      expect(Container.get<TestService>('test2-service')).toBe(test2Service);

      Container.remove(['test1-service', 'test2-service']);

      expect(Container.get(TestService)).toBe(testService);
      expect(() => Container.get<TestService>('test1-service')).toThrowError(ServiceNotFoundError);
      expect(() => Container.get<TestService>('test2-service')).toThrowError(ServiceNotFoundError);
    });
  });

  describe('reset', function () {
    it('should support container reset', () => {
      @Service()
      class TestService {
        constructor(public name: string = 'frank') {}
      }

      Container.set({ id: TestService, type: TestService });
      const testService = Container.get(TestService);
      testService.name = 'john';

      expect(Container.get(TestService)).toBe(testService);
      expect(Container.get(TestService).name).toBe('john');
      Container.reset({ strategy: 'resetValue' });
      expect(Container.get(TestService)).not.toBe(testService);
      expect(Container.get(TestService).name).toBe('frank');
    });
  });

  describe('registerHandler', function () {
    it('should have ability to pre-specify class initialization parameters', function () {
      @Service()
      class ExtraService {
        constructor(public luckyNumber: number, public message: string) {}
      }

      Container.registerHandler({
        object: ExtraService,
        index: 0,
        value: containerInstance => 777,
      });

      Container.registerHandler({
        object: ExtraService,
        index: 1,
        value: containerInstance => 'hello parameter',
      });

      expect(Container.get(ExtraService).luckyNumber).toBe(777);
      expect(Container.get(ExtraService).message).toBe('hello parameter');
    });

    it('should have ability to pre-specify initialized class properties', function () {
      function CustomInject(value: any) {
        return function (target: any, propertyName: string) {
          Container.registerHandler({
            object: target,
            propertyName: propertyName,
            value: containerInstance => value,
          });
        };
      }

      @Service()
      class ExtraService {
        @CustomInject(888)
        badNumber: number;

        @CustomInject('bye world')
        byeMessage: string;
      }

      expect(Container.get(ExtraService).badNumber).toBe(888);
      expect(Container.get(ExtraService).byeMessage).toBe('bye world');
    });

    it('should inject the right value in subclass constructor params', function () {
      function CustomInject(value: any) {
        return function (target: Constructable<any>, propertyName: string, index: number) {
          Container.registerHandler({
            object: target,
            propertyName: propertyName,
            index: index,
            value: containerInstance => value,
          });
        };
      }

      @Service()
      class SuperService {
        constructor(@CustomInject(888) readonly num: number) {}
      }

      @Service()
      class SubService extends SuperService {
        constructor(@CustomInject(666) num: number) {
          super(num);
        }
      }

      expect(Container.get(SuperService).num).toBe(888);
      expect(Container.get(SubService).num).toBe(666);
    });
  });

  describe('set with ServiceMetadata passed', function () {
    it('should support factory functions', function () {
      class Engine {
        public serialNumber = 'A-123';
      }

      class Car {
        constructor(public engine: Engine) {}
      }

      Container.set({
        id: Car,
        factory: () => new Car(new Engine()),
      });

      expect(Container.get(Car).engine.serialNumber).toBe('A-123');
    });

    it('should support factory classes', function () {
      @Service()
      class Engine {
        public serialNumber = 'A-123';
      }

      class Car {
        constructor(public engine: Engine) {}
      }

      @Service()
      class CarFactory {
        constructor(private engine: Engine) {}

        createCar(): Car {
          return new Car(this.engine);
        }
      }

      Container.set({
        id: Car,
        factory: [CarFactory, 'createCar'],
      });

      expect(Container.get(Car).engine.serialNumber).toBe('A-123');
    });

    it('should support tokenized services from factories', function () {
      interface Vehicle {
        getColor(): string;
      }

      class Bus implements Vehicle {
        getColor(): string {
          return 'yellow';
        }
      }

      class VehicleFactory {
        createBus(): Vehicle {
          return new Bus();
        }
      }

      const VehicleService = new Token<Vehicle>();

      Container.set({
        id: VehicleService,
        factory: [VehicleFactory, 'createBus'],
      });

      expect(Container.get(VehicleService).getColor()).toBe('yellow');
    });
  });

  describe('Container.reset', () => {
    it('should call dispose function on removed service', () => {
      const destroyFnMock = jest.fn();
      const destroyPropertyFnMock = jest.fn();
      @Service()
      class MyServiceA {
        dispose() {
          destroyFnMock();
        }
      }

      @Service()
      class MyServiceB {
        public dispose = destroyPropertyFnMock;
      }

      const instanceAOne = Container.get(MyServiceA);
      const instanceBOne = Container.get(MyServiceB);

      Container.reset({ strategy: 'resetValue' });

      const instanceATwo = Container.get(MyServiceA);
      const instanceBTwo = Container.get(MyServiceB);

      expect(destroyFnMock).toBeCalledTimes(1);
      expect(destroyPropertyFnMock).toBeCalledTimes(1);

      expect(instanceAOne).toBeInstanceOf(MyServiceA);
      expect(instanceATwo).toBeInstanceOf(MyServiceA);
      expect(instanceBOne).toBeInstanceOf(MyServiceB);
      expect(instanceBTwo).toBeInstanceOf(MyServiceB);

      expect(instanceAOne).not.toBe(instanceATwo);
      expect(instanceBOne).not.toBe(instanceBTwo);
    });

    it('should be able to destroy services without destroy function', () => {
      @Service()
      class MyService {}

      const instanceA = Container.get(MyService);

      Container.reset({ strategy: 'resetValue' });

      const instanceB = Container.get(MyService);

      expect(instanceA).toBeInstanceOf(MyService);
      expect(instanceB).toBeInstanceOf(MyService);
      expect(instanceA).not.toBe(instanceB);
    });
  });

  describe('Container.remove', () => {
    it('should call dispose function on removed service', () => {
      const destroyFnMock = jest.fn();
      const destroyPropertyFnMock = jest.fn();
      @Service()
      class MyServiceA {
        dispose() {
          destroyFnMock();
        }
      }

      @Service()
      class MyServiceB {
        public dispose = destroyPropertyFnMock();
      }

      Container.get(MyServiceA);
      Container.get(MyServiceB);

      expect(() => Container.remove(MyServiceA)).not.toThrowError();
      expect(() => Container.remove(MyServiceB)).not.toThrowError();

      expect(destroyFnMock).toBeCalledTimes(1);
      expect(destroyPropertyFnMock).toBeCalledTimes(1);

      expect(() => Container.get(MyServiceA)).toThrowError(ServiceNotFoundError);
      expect(() => Container.get(MyServiceB)).toThrowError(ServiceNotFoundError);
    });

    it('should be able to destroy services without destroy function', () => {
      @Service()
      class MyService {}

      Container.get(MyService);

      expect(() => Container.remove(MyService)).not.toThrowError();
      expect(() => Container.get(MyService)).toThrowError(ServiceNotFoundError);
    });
  });
});
```

## File: `test/eager-loading-services.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../src/index';
import { Service } from '../src/decorators/service.decorator';

describe('Eager loading of services', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  describe('Container API', () => {
    it('should be able to set eager and lazy service with Container API', () => {
      let callOrder = 1;

      class MyService {
        public createdAt = callOrder++;
      }

      Container.set({ id: 'eager-service', type: MyService, eager: true });
      Container.set({ id: 'lazy-service', type: MyService, eager: false });

      const timeStampBeforeRequests = callOrder++;

      const eagerService = Container.get<MyService>('eager-service');
      const lazyService = Container.get<MyService>('lazy-service');

      /** Both should resolve to an instance of the service. */
      expect(eagerService).toBeInstanceOf(MyService);
      expect(lazyService).toBeInstanceOf(MyService);

      /** Eager service should have a lower creation order number than the reference timestamp. */
      /** Lazy service should have a higher creation order number than the reference timestamp. */
      expect(eagerService.createdAt).toBe(1);
      expect(timeStampBeforeRequests).toBe(2);
      expect(lazyService.createdAt).toBe(3);
    });
  });

  describe('@Service decorator', () => {
    it('should be able to set eager and lazy service with @Service decorator', () => {
      let callOrder = 1;

      @Service({ eager: true })
      class MyEagerService {
        public createdAt = callOrder++;
      }

      @Service({ eager: false })
      class MyLazyService {
        public createdAt = callOrder++;
      }

      const timeStampBeforeRequests = callOrder++;

      const eagerService = Container.get(MyEagerService);
      const lazyService = Container.get(MyLazyService);

      /** Both should resolve to an instance of the service. */
      expect(eagerService).toBeInstanceOf(MyEagerService);
      expect(lazyService).toBeInstanceOf(MyLazyService);

      /** Eager service should have a lower creation order number than the reference timestamp. */
      /** Lazy service should have a higher creation order number than the reference timestamp. */
      expect(eagerService.createdAt).toBe(1);
      expect(timeStampBeforeRequests).toBe(2);
      expect(lazyService.createdAt).toBe(3);
    });
  });
});
```

## File: `test/tsconfig.json`
```json
{
  // This TS config is added for VS Code, so it understand the test files are
  // using the tsconfig.spec.json file instead of the default one.
  "extends": "../tsconfig.spec.json",
}
```

## File: `test/decorators/Inject.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../src/index';
import { Service } from '../../src/decorators/service.decorator';
import { Inject } from '../../src/decorators/inject.decorator';
import { Token } from '../../src/token.class';
import { InjectMany } from '../../src/decorators/inject-many.decorator';

describe('Inject Decorator', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should inject service into class property', function () {
    @Service()
    class TestService {}
    @Service()
    class SecondTestService {
      @Inject()
      testService: TestService;
    }
    expect(Container.get(SecondTestService).testService).toBeInstanceOf(TestService);
  });

  it('should inject token service properly', function () {
    interface Test {}
    const ServiceToken = new Token<Test>();

    @Service({ id: ServiceToken })
    class TestService {}
    @Service()
    class SecondTestService {
      @Inject(ServiceToken)
      testService: Test;
    }
    expect(Container.get(SecondTestService).testService).toBeInstanceOf(TestService);
  });

  it('should inject named service into class property', function () {
    @Service({ id: 'mega.service' })
    class NamedService {}
    @Service()
    class SecondTestService {
      @Inject('mega.service')
      megaService: any;
    }
    expect(Container.get(SecondTestService).megaService).toBeInstanceOf(NamedService);
  });

  it('should inject service via constructor', function () {
    @Service()
    class TestService {}
    @Service()
    class SecondTestService {}
    @Service({ id: 'mega.service' })
    class NamedService {}
    @Service()
    class TestServiceWithParameters {
      constructor(
        public testClass: TestService,
        @Inject(type => SecondTestService) public secondTest: any,
        @Inject('mega.service') public megaService: any
      ) {}
    }
    expect(Container.get(TestServiceWithParameters).testClass).toBeInstanceOf(TestService);
    expect(Container.get(TestServiceWithParameters).secondTest).toBeInstanceOf(SecondTestService);
    expect(Container.get(TestServiceWithParameters).megaService).toBeInstanceOf(NamedService);
  });

  it("should inject service should work with 'many' instances", function () {
    interface Car {
      name: string;
    }
    @Service({ id: 'cars', multiple: true })
    class Bmw implements Car {
      name = 'BMW';
    }
    @Service({ id: 'cars', multiple: true })
    class Mercedes implements Car {
      name = 'Mercedes';
    }
    @Service({ id: 'cars', multiple: true })
    class Toyota implements Car {
      name = 'Toyota';
    }
    @Service()
    class TestServiceWithParameters {
      constructor(@InjectMany('cars') public cars: Car[]) {}
    }

    expect(Container.get(TestServiceWithParameters).cars).toHaveLength(3);

    const carNames = Container.get(TestServiceWithParameters).cars.map(car => car.name);
    expect(carNames).toContain('BMW');
    expect(carNames).toContain('Mercedes');
    expect(carNames).toContain('Toyota');
  });

  it('should work with empty decorator on constructor parameter', function () {
    @Service()
    class InjectedClass {}

    @Service()
    class TestService {
      constructor(@Inject() public myClass: InjectedClass) {}
    }

    const instance = Container.get(TestService);

    expect(instance).toBeInstanceOf(TestService);
    expect(instance.myClass).toBeInstanceOf(InjectedClass);
  });
});
```

## File: `test/decorators/Service.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../src/index';
import { Service } from '../../src/decorators/service.decorator';
import { Token } from '../../src/token.class';

describe('Service Decorator', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should register class in the container, and its instance should be retrievable', function () {
    @Service()
    class TestService {}
    @Service({ id: 'super.service' })
    class NamedService {}
    expect(Container.get(TestService)).toBeInstanceOf(TestService);
    expect(Container.get(TestService)).not.toBeInstanceOf(NamedService);
  });

  it('should register class in the container with given name, and its instance should be retrievable', function () {
    @Service()
    class TestService {}
    @Service({ id: 'super.service' })
    class NamedService {}
    expect(Container.get('super.service')).toBeInstanceOf(NamedService);
    expect(Container.get('super.service')).not.toBeInstanceOf(TestService);
  });

  it('should register class in the container, and its parameter dependencies should be properly initialized', function () {
    @Service()
    class TestService {}
    @Service()
    class SecondTestService {}
    @Service()
    class TestServiceWithParameters {
      constructor(public testClass: TestService, public secondTest: SecondTestService) {}
    }
    expect(Container.get(TestServiceWithParameters)).toBeInstanceOf(TestServiceWithParameters);
    expect(Container.get(TestServiceWithParameters).testClass).toBeInstanceOf(TestService);
    expect(Container.get(TestServiceWithParameters).secondTest).toBeInstanceOf(SecondTestService);
  });

  it('should support factory functions', function () {
    @Service()
    class Engine {
      constructor(public serialNumber: string) {}
    }

    function createCar() {
      return new Car('BMW', new Engine('A-123'));
    }

    @Service({ factory: createCar })
    class Car {
      constructor(public name: string, public engine: Engine) {}
    }

    expect(Container.get(Car).name).toBe('BMW');
    expect(Container.get(Car).engine.serialNumber).toBe('A-123');
  });

  it('should support factory classes', function () {
    @Service()
    class Engine {
      public serialNumber = 'A-123';
    }

    @Service()
    class CarFactory {
      constructor(public engine: Engine) {}

      createCar() {
        return new Car('BMW', this.engine);
      }
    }

    @Service({ factory: [CarFactory, 'createCar'] })
    class Car {
      name: string;
      constructor(name: string, public engine: Engine) {
        this.name = name;
      }
    }

    expect(Container.get(Car).name).toBe('BMW');
    expect(Container.get(Car).engine.serialNumber).toBe('A-123');
  });

  it('should support factory function with arguments', function () {
    @Service()
    class Engine {
      public type = 'V8';
    }

    @Service()
    class CarFactory {
      createCar(engine: Engine) {
        engine.type = 'V6';
        return new Car(engine);
      }
    }

    @Service({ factory: [CarFactory, 'createCar'] })
    class Car {
      constructor(public engine: Engine) {}
    }

    expect(Container.get(Car).engine.type).toBe('V6');
  });

  it('should support transient services', function () {
    @Service()
    class Car {
      public serial = Math.random();
    }

    @Service({ scope: 'transient' })
    class Engine {
      public serial = Math.random();
    }

    const car1Serial = Container.get(Car).serial;
    const car2Serial = Container.get(Car).serial;
    const car3Serial = Container.get(Car).serial;

    const engine1Serial = Container.get(Engine).serial;
    const engine2Serial = Container.get(Engine).serial;
    const engine3Serial = Container.get(Engine).serial;

    expect(car1Serial).toBe(car2Serial);
    expect(car1Serial).toBe(car3Serial);

    expect(engine1Serial).not.toBe(engine2Serial);
    expect(engine2Serial).not.toBe(engine3Serial);
    expect(engine3Serial).not.toBe(engine1Serial);
  });

  it('should support global services', function () {
    @Service()
    class Engine {
      public name = 'sporty';
    }

    @Service({ scope: 'singleton' })
    class Car {
      public name = 'SportCar';
    }

    const globalContainer = Container;
    const scopedContainer = Container.of('enigma');

    expect(globalContainer.get(Car).name).toBe('SportCar');
    expect(scopedContainer.get(Car).name).toBe('SportCar');

    expect(globalContainer.get(Engine).name).toBe('sporty');
    expect(scopedContainer.get(Engine).name).toBe('sporty');

    globalContainer.get(Car).name = 'MyCar';
    globalContainer.get(Engine).name = 'regular';

    expect(globalContainer.get(Car).name).toBe('MyCar');
    expect(scopedContainer.get(Car).name).toBe('MyCar');

    expect(globalContainer.get(Engine).name).toBe('regular');
    expect(scopedContainer.get(Engine).name).toBe('sporty');
  });

  it('should support function injection with Token dependencies', function () {
    const myToken: Token<string> = new Token<string>('myToken');

    Container.set({ id: myToken, value: 'test_string' });
    Container.set({
      id: 'my-service-A',
      factory: function myServiceFactory(container): string {
        return container.get(myToken).toUpperCase();
      },
    });

    /**
     * This is an unusual format and not officially supported, but it should work.
     * We can set null as the target, because we have set the ID manually, so it won't be used.
     */
    Service({
      id: 'my-service-B',
      factory: function myServiceFactory(container): string {
        return container.get(myToken).toUpperCase();
      },
    })(null);

    expect(Container.get<string>('my-service-A')).toBe('TEST_STRING');
    expect(Container.get<string>('my-service-B')).toBe('TEST_STRING');
  });

  it('should support factory functions', function () {
    class Engine {
      public serialNumber = 'A-123';
    }

    @Service({
      factory: () => new Car(new Engine()),
    })
    class Car {
      constructor(public engine: Engine) {}
    }

    expect(Container.get(Car).engine.serialNumber).toBe('A-123');
  });
});
```

## File: `test/github-issues/102/issue-102.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { Inject } from '../../../src/decorators/inject.decorator';

describe('Github Issues', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('#102 - handle @Inject()-ed values in inherited child classes', () => {
    @Service()
    class InjectedService {}

    @Service()
    class Base {
      public constructor(
        @Inject('config')
        public cfg: any,
        public injectedService: InjectedService
      ) {}
    }

    @Service()
    class Child extends Base {}

    const testconfig = { value: 'I AM A CONFIG OBJECT ' };
    Container.set({ id: 'config', value: testconfig });

    const baseService = Container.get(Base);
    const childService = Container.get(Child);

    expect(baseService).toBeInstanceOf(Base);
    expect(baseService.injectedService).toBeInstanceOf(InjectedService);
    expect(baseService.cfg).toEqual(testconfig);

    expect(childService).toBeInstanceOf(Child);
    expect(childService.injectedService).toBeInstanceOf(InjectedService);
    expect(childService.cfg).toEqual(testconfig);
  });
});
```

## File: `test/github-issues/112/issue-112.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { Inject } from '../../../src/decorators/inject.decorator';

describe('Github Issues', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('#112 - maximum call stack size error with circular dependencies', () => {
    @Service()
    class ClassA {
      @Inject(() => ClassB)
      classB: unknown;
    }

    @Service()
    class ClassB {
      @Inject(() => ClassA)
      classA: unknown;
    }

    const scopedContainer = Container.of('scoped');
    /** Retrieve the classes from the root container. */
    const rootClassA = Container.get(ClassA);
    const rootClassB = Container.get(ClassB);
    /** Retrieve the class instances from the cloned container. */
    const scopedClassA = scopedContainer.get(ClassA);
    const scopedClassB = scopedContainer.get(ClassB);

    /** Values should be properly resolved in the root. */
    expect(rootClassA).toBeInstanceOf(ClassA);
    expect(rootClassA.classB).toBeInstanceOf(ClassB);
    expect(rootClassB).toBeInstanceOf(ClassB);
    expect(rootClassB.classA).toBeInstanceOf(ClassA);
    expect(rootClassA).toStrictEqual(rootClassB.classA);
    expect(rootClassB).toStrictEqual(rootClassA.classB);

    /** Values should be properly resolved in the scoped. */
    expect(scopedClassA).toBeInstanceOf(ClassA);
    expect(scopedClassA.classB).toBeInstanceOf(ClassB);
    expect(scopedClassB).toBeInstanceOf(ClassB);
    expect(scopedClassB.classA).toBeInstanceOf(ClassA);
    expect(scopedClassA).toStrictEqual(scopedClassB.classA);
    expect(scopedClassB).toStrictEqual(scopedClassA.classB);

    /** Two container should not share the exact same instances. */
    expect(rootClassA).not.toStrictEqual(scopedClassA);
    expect(rootClassB).not.toStrictEqual(scopedClassB);
  });
});
```

## File: `test/github-issues/151/issue-151.spect.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';

describe('Github Issues', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('#151 - should be able to define type when setting service', () => {
    /**
     * Note: This is more like a behavioral test the use-case showcased below
     * should be always possible, even if the API changes.
     */
    @Service()
    class AuthService {
      isAuthorized() {
        return 'nope';
      }
    }

    @Service()
    class DataService {
      constructor(public authService: AuthService) {}
    }
    @Service()
    class FakeDataService {
      constructor(public authService: AuthService) {}
    }

    Container.set({ id: DataService, type: FakeDataService });

    const instance = Container.get<FakeDataService>(DataService as any);

    expect(instance).toBeInstanceOf(FakeDataService);
    expect(instance.authService).toBeInstanceOf(AuthService);
    expect(instance.authService.isAuthorized()).toBe('nope');
  });
});
```

## File: `test/github-issues/157/issue-157.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';

describe('Github Issues', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('#157 - reset should not break transient services', () => {
    let creationCounter = 0;

    @Service({ scope: 'transient' })
    class TransientService {
      public constructor() {
        creationCounter++;
      }
    }

    Container.get(TransientService);
    Container.get(TransientService);

    expect(creationCounter).toBe(2);

    Container.reset({ strategy: 'resetValue' });

    Container.get(TransientService);
    Container.get(TransientService);

    expect(creationCounter).toBe(4);
  });
});
```

## File: `test/github-issues/40/issue-40.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { Inject } from '../../../src/decorators/inject.decorator';

describe('github issues > #40 Constructor inject not working', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should work properly', function () {
    @Service({ id: 'AccessTokenService' })
    class AccessTokenService {
      constructor(
        @Inject('moment') public moment: any,
        @Inject('jsonwebtoken') public jsonwebtoken: any,
        @Inject('cfg.auth.jwt') public jwt: any
      ) {}
    }

    Container.set({ id: 'moment', value: 'A' });
    Container.set({ id: 'jsonwebtoken', value: 'B' });
    Container.set({ id: 'cfg.auth.jwt', value: 'C' });
    const accessTokenService = Container.get<AccessTokenService>('AccessTokenService');

    expect(accessTokenService.moment).not.toBeUndefined();
    expect(accessTokenService.jsonwebtoken).not.toBeUndefined();
    expect(accessTokenService.jwt).not.toBeUndefined();

    expect(accessTokenService.moment).toBe('A');
    expect(accessTokenService.jsonwebtoken).toBe('B');
    expect(accessTokenService.jwt).toBe('C');
  });
});
```

## File: `test/github-issues/41/issue-41.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { Token } from '../../../src/token.class';

describe('github issues > #41 Token as service id in combination with factory', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should work properly', function () {
    interface SomeInterface {
      foo(): string;
    }
    const SomeInterfaceToken = new Token<SomeInterface>();

    @Service()
    class SomeInterfaceFactory {
      create() {
        return new SomeImplementation();
      }
    }

    @Service({
      id: SomeInterfaceToken,
      factory: [SomeInterfaceFactory, 'create'],
    })
    class SomeImplementation implements SomeInterface {
      foo() {
        return 'hello implementation';
      }
    }

    Container.set({ id: 'moment', value: 'A' });
    Container.set({ id: 'jsonwebtoken', value: 'B' });
    Container.set({ id: 'cfg.auth.jwt', value: 'C' });
    const someInterfaceImpl = Container.get(SomeInterfaceToken);
    expect(someInterfaceImpl.foo()).toBe('hello implementation');
  });
});
```

## File: `test/github-issues/42/issue-42.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { Inject } from '../../../src/decorators/inject.decorator';
import { CannotInjectValueError } from '../../../src/error/cannot-inject-value.error';

describe('github issues > #42 Exception not thrown on missing binding', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should work properly', function () {
    interface Factory {
      create(): void;
    }

    expect(() => {
      @Service()
      class CoffeeMaker {
        @Inject() // This is an incorrect usage of TypeDI because Factory is an interface
        private factory: Factory;

        make() {
          this.factory.create();
        }
      }
      // We doesn't even need to call `Container.get(CoffeeMaker);`, TypeDI will detect this error, while
      // the JS code is parsed and decorators are executed.
    }).toThrowError(CannotInjectValueError);
  });
});
```

## File: `test/github-issues/48/issue-48.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { Token } from '../../../src/token.class';

describe("github issues > #48 Token service iDs in global container aren't inherited by scoped containers", function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should work properly', function () {
    let poloCounter = 0;

    const FooServiceToken = new Token<FooService>();

    @Service({ id: FooServiceToken })
    class FooService implements FooService {
      public marco() {
        poloCounter++;
      }
    }

    const scopedContainer = Container.of('myScopredContainer');
    const rootInstance = Container.get(FooServiceToken);
    const scopedInstance = scopedContainer.get(FooServiceToken);

    rootInstance.marco();
    scopedInstance.marco();

    expect(poloCounter).toBe(2);
  });
});
```

## File: `test/github-issues/53/issue-53.spec.ts`
```typescript
import { Console } from 'console';
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { Token } from '../../../src/token.class';

describe('github issues > #53 Token-based services are cached in the Global container even when fetched via a subcontainer', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should work properly', function () {
    @Service()
    class QuestionRepository {
      userName: string;

      save() {
        return null;
      }
    }

    const QuestionControllerToken = new Token<QuestionControllerImpl>('QCImpl');

    @Service({ id: QuestionControllerToken })
    class QuestionControllerImpl {
      constructor(protected questionRepository: QuestionRepository) {}

      save(name: string) {
        if (name) this.questionRepository.userName = name;
        this.questionRepository.save();
      }
    }

    const request1 = 'REQUEST_1';
    const controller1 = Container.of(request1).get(QuestionControllerToken);
    controller1.save('Timber');
    Container.reset({ strategy: 'resetValue' });

    const request2 = 'REQUEST_2';
    const controller2 = Container.of(request2).get(QuestionControllerToken);
    controller2.save('John');
    Container.reset({ strategy: 'resetValue' });

    expect(controller1).not.toBe(controller2);
    expect(controller1).not.toBe(Container.get(QuestionControllerToken));
  });
});
```

## File: `test/github-issues/56/issue-56.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';

describe('github issues > #56 extended class is being overwritten', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('should work properly', function () {
    @Service()
    class Rule {
      getRule() {
        return 'very strict rule';
      }
    }

    @Service()
    class Whitelist extends Rule {
      getWhitelist() {
        return ['rule1', 'rule2'];
      }
    }

    const whitelist = Container.get(Whitelist);
    expect(whitelist.getRule).not.toBeUndefined();
    expect(whitelist.getWhitelist).not.toBeUndefined();
    expect(whitelist.getWhitelist()).toEqual(['rule1', 'rule2']);
    expect(whitelist.getRule()).toEqual('very strict rule');

    const rule = Container.get(Rule);
    expect(rule.getRule).not.toBeUndefined();
    expect((rule as Whitelist).getWhitelist).toBeUndefined();
    expect(rule.getRule()).toEqual('very strict rule');
  });
});
```

## File: `test/github-issues/61/issue-61.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';

describe('Github Issues', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('#61 - Scoped container creates new instance of service every time', function () {
    @Service()
    class Car {
      public serial = Math.random();
    }

    const fooContainer = Container.of('foo');
    const barContainer = Container.of('bar');

    const car1Serial = Container.get(Car).serial;
    const car2Serial = Container.get(Car).serial;

    const fooCar1Serial = fooContainer.get(Car).serial;
    const fooCar2Serial = fooContainer.get(Car).serial;

    const barCar1Serial = barContainer.get(Car).serial;
    const barCar2Serial = barContainer.get(Car).serial;

    expect(car1Serial).toEqual(car2Serial);
    expect(fooCar1Serial).toEqual(fooCar2Serial);
    expect(barCar1Serial).toEqual(barCar2Serial);

    expect(car1Serial).not.toEqual(fooCar1Serial);
    expect(car1Serial).not.toEqual(barCar1Serial);
    expect(fooCar1Serial).not.toEqual(barCar1Serial);

    expect(Container.of('TEST').get(Car).serial === Container.of('TEST').get(Car).serial).toBe(true);
  });
});
```

## File: `test/github-issues/87/issue-87.spec.ts`
```typescript
import 'reflect-metadata';
import { Container } from '../../../src/index';
import { Service } from '../../../src/decorators/service.decorator';
import { ServiceNotFoundError } from '../../../src/error/service-not-found.error';

describe('Github Issues', function () {
  beforeEach(() => Container.reset({ strategy: 'resetValue' }));

  it('#87 - TypeDI should throw error if a dependency is not found', () => {
    @Service()
    class InjectedClassA {}

    /** This class is not decorated with @Service decorator. */
    class InjectedClassB {}

    @Service()
    class MyClass {
      constructor(private injectedClassA: InjectedClassA, private injectedClassB: InjectedClassB) {}
    }

    expect(() => Container.get(MyClass)).toThrowError(ServiceNotFoundError);
  });
});
```

