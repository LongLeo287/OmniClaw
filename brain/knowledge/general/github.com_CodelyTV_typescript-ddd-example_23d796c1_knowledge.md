---
id: github.com-codelytv-typescript-ddd-example-23d796c
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:40.975629
---

# KNOWLEDGE EXTRACT: github.com_CodelyTV_typescript-ddd-example_23d796c1
> **Extracted on:** 2026-04-01 13:38:27
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522571/github.com_CodelyTV_typescript-ddd-example_23d796c1

---

## File: `.dockerignore`
```
.dockerignore
.git
docker-compose.yml
Dockerfile
node_modules
dist
data
logs
```

## File: `.editorconfig`
```
# editorconfig.org
root = true

[*]
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
indent_style = space
indent_size = 2
```

## File: `.gitignore`
```
node_modules/
dist/
.tmp
logs/
data
test-results.xml
/src/Contexts/Mooc/Courses/infrastructure/persistence/courses.*.repo
```

## File: `.nvmrc`
```
v16.16.0
```

## File: `.prettierignore`
```
src/apps/backoffice/frontend
```

## File: `.prettierrc`
```
{
  "printWidth": 120,
  "tabWidth": 2,
  "singleQuote": true,
  "trailingComma": "none",
  "quoteProps": "as-needed",
  "arrowParens": "avoid"
}
```

## File: `Dockerfile`
```
FROM node:12.16.3-slim

WORKDIR /code

COPY package.json package-lock.json ./
RUN npm install
```

## File: `Makefile`
```
.PHONY = default deps build test start-mooc-backend clean start-database start-backoffice-frontend

# Shell to use for running scripts
SHELL := $(shell which bash)
IMAGE_NAME := codelytv/typescript-ddd-skeleton
SERVICE_NAME := app
MOOC_APP_NAME := mooc
BACKOFFICE_APP_NAME := backoffice

# Test if the dependencies we need to run this Makefile are installed
DOCKER := $(shell command -v docker)
DOCKER_COMPOSE := $(shell command -v docker-compose)
deps:
ifndef DOCKER
	@echo "Docker is not available. Please install docker"
	@exit 1
endif
ifndef DOCKER_COMPOSE
	@echo "docker-compose is not available. Please install docker-compose"
	@exit 1
endif

default: build

# Build image
build:
	docker build -t $(IMAGE_NAME):dev .

# Clean containers
clean:
	docker-compose down --rmi local --volumes --remove-orphans

# Start databases containers in background
start_database:
	docker-compose up -d mongo elasticsearch rabbitmq
```

## File: `README.md`
```markdown
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  🐘🎯 Hexagonal Architecture, DDD & CQRS in Typescript
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/CodelyTV-OS-green.svg?style=flat-square" alt="codely.tv"/></a>
    <a href="http://pro.codely.tv"><img src="https://img.shields.io/badge/CodelyTV-PRO-black.svg?style=flat-square" alt="CodelyTV Courses"/></a>
</p>

<p align="center">
  Example of a Typescript application following Domain-Driven Design (DDD),
  Command Query Responsibility Segregation (CQRS) and
  Event-Driven Architecture (EDA) principles keeping the code as simple as possible.

</p>

# 🔀 Related utilities and resources

## ☝️ Learning resources

- [🔖 Domain-Driven Design en TypeScript: Modelado y Arquitectura](https://pro.codely.tv/library/ddd-en-typescript-modelado-y-arquitectura-172533/375662/about/) (Spanish - Course)
- [️️🛰️ DDD en TypeScript: Comunicación entre servicios y aplicaciones](https://pro.codely.com/library/comunicacion-entre-microservicios-event-driven-architecture-35834) (Spanish - Course)
- [🏗️ De JavaScript a TypeScript](https://pro.codely.tv/library/de-javascript-a-typescript-128106/347481/about/) (Spanish - Course)
- [📂 DDD en TypeScript: Estructura de carpetas](https://youtu.be/AJJRk7qmVHg) (Spanish - YouTube video)

## 🔷 TypeScript skeletons


- [🌱 TypeScript Basic Skeleton](https://github.com/CodelyTV/typescript-basic-skeleton): Bootstrap your new TypeScript frontend project
- [🌍 TypeScript API Skeleton](https://github.com/CodelyTV/typescript-api-skeleton): Bootstrap your new TypeScript backend project
- [️🗿 TypeScript DDD Skeleton](https://github.com/CodelyTV/typescript-ddd-skeleton): Bootstrap your new TypeScript DDD project

## 🌈 TypeScript Domain-Driven Design repositories

- [✨ TypeScript DDD Skeleton](https://github.com/CodelyTV/typescript-ddd-skeleton): Bootstrap your new TypeScript projects applying Hexagonal Architecture and Domain-Driven Design patterns
- [🔖 TypeScript DDD Course](https://github.com/CodelyTV/typescript-ddd-course): Learn Domain-Driven Design in TS lesson by lesson
- [🎯 TypeScript DDD Example](https://github.com/CodelyTV/typescript-ddd-example): Complete project applying Hexagonal Architecture and Domain-Driven Design patterns

## 🎯 Other languages Domain-Driven Design repositories

- [☕🎯 Java DDD Example](https://github.com/CodelyTV/java-ddd-example)
- [🐘🎯 PHP DDD Example](https://github.com/CodelyTV/php-ddd-example)
- [λ🎯 Scala DDD Example](https://github.com/CodelyTV/scala-ddd-example)
- [🦈✨ C# DDD Skeleton](https://github.com/CodelyTV/csharp-ddd-skeleton)
```

## File: `cucumber.js`
```javascript
const common = [
  '--require-module ts-node/register' // Load TypeScript module
];

const mooc_backend = [
  ...common,
  'tests/apps/mooc/backend/features/**/*.feature',
  '--require tests/apps/mooc/backend/features/step_definitions/*.steps.ts'
].join(' ');

const backoffice_backend = [
  ...common,
  'tests/apps/backoffice/backend/features/**/*.feature',
  '--require tests/apps/backoffice/backend/features/step_definitions/*.steps.ts'
].join(' ');

module.exports = {
  mooc_backend,
  backoffice_backend
};
```

## File: `docker-compose.yml`
```yaml
version: '3.8'

services:
  mongo:
    image: mongo:5.0.0
    environment:
      - MONGO_URL=mongodb://mongo:27017/dev
    volumes:
      - ./data/mongo:/data/db:delegated
    ports:
      - 27017:27017
  postgres:
    image: postgres
    environment:
      - POSTGRES_PASSWORD=codely
      - POSTGRES_USER=codely
      - POSTGRES_DB=mooc-backend-dev
    ports:
      - '5432:5432'
    restart: always
  rabbitmq:
    image: 'rabbitmq:3.8-management'
    ports:
      - 5672:5672
      - 15672:15672
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.9.3
    container_name: codely-elasticsearch
    environment:
      - node.name=codely-elasticsearch
      - discovery.type=single-node #Elasticsearch forms a single-node cluster
      - bootstrap.memory_lock=true # might cause the JVM or shell session to exit if it tries to allocate more memory than is available!
      - 'ES_JAVA_OPTS=-Xms2048m -Xmx2048m'
    ulimits:
      memlock:
        soft: -1 # The memlock soft and hard values configures the range of memory that ElasticSearch will use. Setting this to –1 means unlimited.
        hard: -1
    volumes:
      - esdata:/usr/share/elasticsearch/data
    ports:
      - '9200:9200'
  kibana:
    image: docker.elastic.co/kibana/kibana:7.8.1
    container_name: codely-kibana
    environment:
      ELASTICSEARCH_URL: http://codely-elasticsearch:9200
      ELASTICSEARCH_HOSTS: http://codely-elasticsearch:9200
    ports:
      - 5601:5601

volumes:
  node_modules:
  esdata:
    driver: local
```

## File: `jest.config.js`
```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  cacheDirectory: '.tmp/jestCache'
};
```

## File: `package.json`
```json
{
  "name": "typescript-ddd-course",
  "version": "1.0.0",
  "description": "",
  "repository": {
    "url": "https://github.com/CodelyTV/typescript-ddd-course"
  },
  "license": "",
  "engines": {
    "node": ">=12.0.0",
    "npm": ">=6.7.0"
  },
  "scripts": {
    "dev:mooc:backend": "NODE_ENV=dev ts-node-dev --ignore-watch node_modules  ./src/apps/mooc/backend/start.ts",
    "dev:backoffice:frontend": "cd ./src/apps/backoffice/frontend && npm start",
    "dev:backoffice:backend": "NODE_ENV=dev ts-node-dev --ignore-watch node_modules ./src/apps/backoffice/backend/start.ts",
    "lint": "prettier --write src/**/*.ts{,x}",
    "test": "npm run test:unit && npm run test:features",
    "test:unit": "NODE_ENV=test jest",
    "start:mooc:backend": "NODE_ENV=production node dist/src/apps/mooc/backend/start",
    "start:backoffice:backend": "NODE_ENV=production node dist/src/apps/backoffice/backend/start",
    "test:features": "npm run test:mooc:backend:features",
    "test:mooc:backend:features": "NODE_ENV=test cucumber-js -p mooc_backend",
    "test:backoffice:backend:features": "NODE_ENV=test cucumber-js -p backoffice_backend",
    "build": "npm run build:clean && npm run build:tsc && npm run build:di",
    "build:tsc": "tsc -p tsconfig.prod.json",
    "build:di": "copy 'src/**/*.{json,yaml,html,png}' dist/src",
    "build:clean": "rm -r dist; exit 0",
    "build:backoffice:frontend": "cd ./src/apps/backoffice/frontend && npm run build",
    "command:mooc:rabbitmq": "NODE_ENV=production ts-node src/apps/mooc/backend/command/runConfigureRabbitMQCommand",
    "command:backoffice:rabbitmq": "NODE_ENV=production ts-node src/apps/backoffice/backend/command/runConfigureRabbitMQCommand"
  },
  "dependencies": {
    "@elastic/elasticsearch": "^7.11.0",
    "amqplib": "^0.8.0",
    "body-parser": "^1.19.0",
    "bodybuilder": "^2.4.0",
    "bson": "^4.4.0",
    "compression": "^1.7.4",
    "connect-flash": "^0.1.1",
    "convict": "^6.2.0",
    "cookie-parser": "^1.4.5",
    "cookie-session": "^1.4.0",
    "copy": "^0.3.2",
    "cors": "^2.8.5",
    "errorhandler": "^1.5.1",
    "express": "^4.17.1",
    "express-promise-router": "^4.0.1",
    "express-validator": "^6.10.0",
    "glob": "^7.1.6",
    "helmet": "^4.4.1",
    "http-status": "^1.5.0",
    "mongodb": "^3.7.3",
    "node-dependency-injection": "^2.6.11",
    "nunjucks": "^3.2.3",
    "pg": "^8.7.1",
    "ts-node": "^10.8.1",
    "typeorm": "^0.3.10",
    "typescript": "^4.2.3",
    "uuid": "^8.3.2",
    "uuid-validate": "0.0.3",
    "winston": "^3.3.3"
  },
  "devDependencies": {
    "@types/amqplib": "^0.8.2",
    "@types/bson": "^4.0.3",
    "@types/compression": "^1.7.0",
    "@types/errorhandler": "1.5.0",
    "@types/express": "^4.17.11",
    "@types/glob": "^7.1.3",
    "@types/helmet": "0.0.48",
    "@types/node": "^18.8.5",
    "@types/connect-flash": "0.0.36",
    "@types/convict": "^6.1.1",
    "@types/cookie-parser": "^1.4.2",
    "@types/cookie-session": "^2.0.42",
    "@types/cors": "^2.8.12",
    "@types/cucumber": "^6.0.1",
    "@types/faker": "^5.5.7",
    "@types/jest": "^26.0.24",
    "@types/mongodb": "^3.6.20",
    "@types/supertest": "^2.0.10",
    "@types/uuid": "^8.3.1",
    "@types/uuid-validate": "0.0.1",
    "autoprefixer": "^10.4.7",
    "cucumber": "^6.0.5",
    "faker": "^5.5.3",
    "husky": "^5.1.3",
    "jest": "^28.1.1",
    "lint-staged": "10.5.4",
    "postcss": "^8.4.14",
    "prettier": "^2.2.1",
    "supertest": "^6.1.3",
    "tailwindcss": "^3.1.3",
    "ts-jest": "^28.0.5",
    "ts-node-dev": "^2.0.0"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "{src,tests}/**/*.ts": [
      "prettier --write",
      "git add"
    ]
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "module": "commonjs",
    "esModuleInterop": true,
    "target": "es6",
    "noImplicitAny": true,
    "moduleResolution": "node",
    "sourceMap": false,
    "rootDir": ".",
    "strict": true,
    "noEmit": false,
    "resolveJsonModule": true,
    "noUnusedLocals": true,
    "outDir": "./dist"
  },
  "include": [
    "src/**/**.ts",
    "tests/**/**.ts"
  ],
  "exclude": [
    "node_modules",
    "src/apps/backoffice/frontend"
  ]
}
```

## File: `tsconfig.prod.json`
```json
{
  "extends": "./tsconfig.json",
  "exclude": ["node_modules", "tests"]
}
```

## File: `src/Contexts/Backoffice/Courses/application/BackofficeCoursesResponse.ts`
```typescript
import { BackofficeCourse } from '../domain/BackofficeCourse';

interface BackofficeCourseResponse {
  id: string;
  name: string;
  duration: string;
}

export class BackofficeCoursesResponse {
  public readonly courses: Array<BackofficeCourseResponse>;

  constructor(courses: Array<BackofficeCourse>) {
    this.courses = courses.map(course => course.toPrimitives());
  }
}
```

## File: `src/Contexts/Backoffice/Courses/application/Create/BackofficeCourseCreator.ts`
```typescript
import { BackofficeCourse } from '../../domain/BackofficeCourse';
import { BackofficeCourseDuration } from '../../domain/BackofficeCourseDuration';
import { BackofficeCourseId } from '../../domain/BackofficeCourseId';
import { BackofficeCourseName } from '../../domain/BackofficeCourseName';
import { BackofficeCourseRepository } from '../../domain/BackofficeCourseRepository';

export class BackofficeCourseCreator {
  constructor(private backofficeCourseRepository: BackofficeCourseRepository) {}

  async run(id: string, duration: string, name: string) {
    const course = new BackofficeCourse(
      new BackofficeCourseId(id),
      new BackofficeCourseName(name),
      new BackofficeCourseDuration(duration)
    );

    return this.backofficeCourseRepository.save(course);
  }
}
```

## File: `src/Contexts/Backoffice/Courses/application/Create/CreateBackofficeCourseOnCourseCreated.ts`
```typescript
import { CourseCreatedDomainEvent } from '../../../../Mooc/Courses/domain/CourseCreatedDomainEvent';
import { DomainEventClass } from '../../../../Shared/domain/DomainEvent';
import { DomainEventSubscriber } from '../../../../Shared/domain/DomainEventSubscriber';
import { BackofficeCourseCreator } from './BackofficeCourseCreator';

export class CreateBackofficeCourseOnCourseCreated implements DomainEventSubscriber<CourseCreatedDomainEvent> {
  constructor(private creator: BackofficeCourseCreator) {}

  subscribedTo(): DomainEventClass[] {
    return [CourseCreatedDomainEvent];
  }

  async on(domainEvent: CourseCreatedDomainEvent): Promise<void> {
    const { aggregateId, duration, name } = domainEvent;

    return this.creator.run(aggregateId, duration, name);
  }
}
```

## File: `src/Contexts/Backoffice/Courses/application/SearchAll/CoursesFinder.ts`
```typescript
import { BackofficeCourseRepository } from '../../domain/BackofficeCourseRepository';

export class CoursesFinder {
  constructor(private coursesRepository: BackofficeCourseRepository) {}

  async run() {
    const courses = await this.coursesRepository.searchAll();

    return courses;
  }
}
```

## File: `src/Contexts/Backoffice/Courses/application/SearchAll/SearchAllCoursesQuery.ts`
```typescript
import { Query } from '../../../../Shared/domain/Query';

export class SearchAllCoursesQuery implements Query {}
```

## File: `src/Contexts/Backoffice/Courses/application/SearchAll/SearchAllCoursesQueryHandler.ts`
```typescript
import { Query } from '../../../../Shared/domain/Query';
import { QueryHandler } from '../../../../Shared/domain/QueryHandler';
import { BackofficeCoursesResponse } from '../BackofficeCoursesResponse';
import { CoursesFinder } from './CoursesFinder';
import { SearchAllCoursesQuery } from './SearchAllCoursesQuery';

export class SearchAllCoursesQueryHandler implements QueryHandler<SearchAllCoursesQuery, BackofficeCoursesResponse> {
  constructor(private readonly coursesFinder: CoursesFinder) {}

  subscribedTo(): Query {
    return SearchAllCoursesQuery;
  }

  async handle(_query: SearchAllCoursesQuery): Promise<BackofficeCoursesResponse> {
    return new BackofficeCoursesResponse(await this.coursesFinder.run());
  }
}
```

## File: `src/Contexts/Backoffice/Courses/application/SearchByCriteria/CoursesByCriteriaSearcher.ts`
```typescript
import { Criteria } from '../../../../Shared/domain/criteria/Criteria';
import { Filters } from '../../../../Shared/domain/criteria/Filters';
import { Order } from '../../../../Shared/domain/criteria/Order';
import { BackofficeCourseRepository } from '../../domain/BackofficeCourseRepository';
import { BackofficeCoursesResponse } from '../BackofficeCoursesResponse';

export class CoursesByCriteriaSearcher {
  constructor(private repository: BackofficeCourseRepository) {}

  async run(filters: Filters, order: Order, limit?: number, offset?: number): Promise<BackofficeCoursesResponse> {
    const criteria = new Criteria(filters, order, limit, offset);

    const courses = await this.repository.matching(criteria);

    return new BackofficeCoursesResponse(courses);
  }
}
```

## File: `src/Contexts/Backoffice/Courses/application/SearchByCriteria/SearchCoursesByCriteriaQuery.ts`
```typescript
import { Query } from '../../../../Shared/domain/Query';

export class SearchCoursesByCriteriaQuery implements Query {
  readonly filters: Array<Map<string, string>>;
  readonly orderBy?: string;
  readonly orderType?: string;
  readonly limit?: number;
  readonly offset?: number;

  constructor(
    filters: Array<Map<string, string>>,
    orderBy?: string,
    orderType?: string,
    limit?: number,
    offset?: number
  ) {
    this.filters = filters;
    this.orderBy = orderBy;
    this.orderType = orderType;
    this.limit = limit;
    this.offset = offset;
  }
}
```

## File: `src/Contexts/Backoffice/Courses/application/SearchByCriteria/SearchCoursesByCriteriaQueryHandler.ts`
```typescript
import { Filters } from '../../../../Shared/domain/criteria/Filters';
import { Order } from '../../../../Shared/domain/criteria/Order';
import { Query } from '../../../../Shared/domain/Query';
import { QueryHandler } from '../../../../Shared/domain/QueryHandler';
import { BackofficeCoursesResponse } from '../BackofficeCoursesResponse';
import { CoursesByCriteriaSearcher } from './CoursesByCriteriaSearcher';
import { SearchCoursesByCriteriaQuery } from './SearchCoursesByCriteriaQuery';

export class SearchCoursesByCriteriaQueryHandler
  implements QueryHandler<SearchCoursesByCriteriaQuery, BackofficeCoursesResponse>
{
  constructor(private searcher: CoursesByCriteriaSearcher) {}

  subscribedTo(): Query {
    return SearchCoursesByCriteriaQuery;
  }

  handle(query: SearchCoursesByCriteriaQuery): Promise<BackofficeCoursesResponse> {
    const filters = Filters.fromValues(query.filters);
    const order = Order.fromValues(query.orderBy, query.orderType);

    return this.searcher.run(filters, order, query.limit, query.offset);
  }
}
```

## File: `src/Contexts/Backoffice/Courses/domain/BackofficeCourse.ts`
```typescript
import { AggregateRoot } from '../../../Shared/domain/AggregateRoot';
import { BackofficeCourseDuration } from './BackofficeCourseDuration';
import { BackofficeCourseId } from './BackofficeCourseId';
import { BackofficeCourseName } from './BackofficeCourseName';

export class BackofficeCourse extends AggregateRoot {
  readonly id: BackofficeCourseId;
  readonly name: BackofficeCourseName;
  readonly duration: BackofficeCourseDuration;

  constructor(id: BackofficeCourseId, name: BackofficeCourseName, duration: BackofficeCourseDuration) {
    super();
    this.id = id;
    this.name = name;
    this.duration = duration;
  }

  static create(
    id: BackofficeCourseId,
    name: BackofficeCourseName,
    duration: BackofficeCourseDuration
  ): BackofficeCourse {
    const course = new BackofficeCourse(id, name, duration);

    return course;
  }

  static fromPrimitives(plainData: { id: string; name: string; duration: string }): BackofficeCourse {
    return new BackofficeCourse(
      new BackofficeCourseId(plainData.id),
      new BackofficeCourseName(plainData.name),
      new BackofficeCourseDuration(plainData.duration)
    );
  }

  toPrimitives() {
    return {
      id: this.id.value,
      name: this.name.value,
      duration: this.duration.value
    };
  }
}
```

## File: `src/Contexts/Backoffice/Courses/domain/BackofficeCourseDuration.ts`
```typescript
import { StringValueObject } from '../../../Shared/domain/value-object/StringValueObject';

export class BackofficeCourseDuration extends StringValueObject {}
```

## File: `src/Contexts/Backoffice/Courses/domain/BackofficeCourseId.ts`
```typescript
import { Uuid } from '../../../Shared/domain/value-object/Uuid';

export class BackofficeCourseId extends Uuid {}
```

## File: `src/Contexts/Backoffice/Courses/domain/BackofficeCourseName.ts`
```typescript
import { StringValueObject } from '../../../Shared/domain/value-object/StringValueObject';

export class BackofficeCourseName extends StringValueObject {}
```

## File: `src/Contexts/Backoffice/Courses/domain/BackofficeCourseRepository.ts`
```typescript
import { Criteria } from '../../../Shared/domain/criteria/Criteria';
import { BackofficeCourse } from './BackofficeCourse';

export interface BackofficeCourseRepository {
  save(course: BackofficeCourse): Promise<void>;
  searchAll(): Promise<Array<BackofficeCourse>>;
  matching(criteria: Criteria): Promise<Array<BackofficeCourse>>;
}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/RabbitMQ/RabbitMQConfigFactory.ts`
```typescript
import { ConnectionSettings } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/ConnectionSettings';
import { ExchangeSetting } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/ExchangeSetting';
import config from '../config';

export type RabbitMQConfig = {
  connectionSettings: ConnectionSettings;
  exchangeSettings: ExchangeSetting;
  maxRetries: number;
  retryTtl: number;
};

export class RabbitMQConfigFactory {
  static createConfig(): RabbitMQConfig {
    return config.get('rabbitmq');
  }
}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/RabbitMQ/RabbitMQEventBusFactory.ts`
```typescript
import { DomainEventFailoverPublisher } from '../../../../Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher';
import { RabbitMqConnection } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';
import { RabbitMQEventBus } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/RabbitMQEventBus';
import { RabbitMQqueueFormatter } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter';
import { RabbitMQConfig } from './RabbitMQConfigFactory';

export class RabbitMQEventBusFactory {
  static create(
    failoverPublisher: DomainEventFailoverPublisher,
    connection: RabbitMqConnection,
    queueNameFormatter: RabbitMQqueueFormatter,
    config: RabbitMQConfig
  ): RabbitMQEventBus {
    return new RabbitMQEventBus({
      failoverPublisher,
      connection,
      exchange: config.exchangeSettings.name,
      queueNameFormatter: queueNameFormatter,
      maxRetries: config.maxRetries
    });
  }
}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/config/default.json`
```json
{}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/config/dev.json`
```json
{}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/config/end2end.json`
```json
{}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/config/index.ts`
```typescript
import convict from 'convict';

const backofficeConfig = convict({
  env: {
    doc: 'The application environment.',
    format: ['production', 'development', 'staging', 'test'],
    default: 'default',
    env: 'NODE_ENV'
  },
  mongo: {
    url: {
      doc: 'The Mongo connection URL',
      format: String,
      env: 'MONGO_URL',
      default: 'mongodb://localhost:27017/mooc-backend-dev'
    }
  },
  rabbitmq: {
    connectionSettings: {
      username: {
        doc: 'RabbitMQ username',
        format: String,
        env: 'RABBITMQ_USERNAME',
        default: 'guest'
      },
      password: {
        doc: 'RabbitMQ password',
        format: String,
        env: 'RABBITMQ_PASSWORD',
        default: 'guest'
      },
      vhost: {
        doc: 'RabbitMQ virtual host',
        format: String,
        env: 'RABBITMQ_VHOST',
        default: '/'
      },
      connection: {
        secure: {
          doc: 'RabbitMQ secure protocol',
          format: Boolean,
          env: 'RABBITMQ_SECURE',
          default: false
        },
        hostname: {
          doc: 'RabbitMQ hostname',
          format: String,
          env: 'RABBITMQ_HOSTNAME',
          default: 'localhost'
        },
        port: {
          doc: 'RabbitMQ amqp port',
          format: Number,
          env: 'RABBITMQ_PORT',
          default: 5672
        }
      }
    },
    exchangeSettings: {
      name: {
        doc: 'RabbitMQ exchange name',
        format: String,
        env: 'RABBITMQ_EXCHANGE_NAME',
        default: 'domain_events'
      }
    },
    maxRetries: {
      doc: 'Max number of retries for each message',
      format: Number,
      env: 'RABBITMQ_MAX_RETRIES',
      default: 3
    },
    retryTtl: {
      doc: 'Ttl for messages in the retry queue',
      format: Number,
      env: 'RABBITMQ_RETRY_TTL',
      default: 1000
    }
  },
  elastic: {
    url: {
      doc: 'The Elastic connection URL',
      format: String,
      env: 'ELASTIC_URL',
      default: 'http://localhost:9200'
    },
    indexName: {
      doc: 'The Elastic index name for this context',
      format: String,
      env: 'ELASTIC_INDEX_NAME',
      default: 'backofficecourses'
    },
    config: {
      doc: 'The Elastic config for this context',
      format: '*',
      env: 'ELASTIC_CONFIG',
      default: {
        settings: {
          index: {
            number_of_replicas: 0 // for local development
          }
        },
        mappings: {
          properties: {
            id: {
              type: 'keyword',
              index: true
            },
            name: {
              type: 'text',
              index: true,
              fielddata: true
            },
            duration: {
              type: 'text',
              index: true,
              fielddata: true
            }
          }
        }
      }
    }
  }
});

backofficeConfig.loadFile([__dirname + '/default.json', __dirname + '/' + backofficeConfig.get('env') + '.json']);

export default backofficeConfig;
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/config/production.json`
```json
{
    "elastic": {
      "url": "http://elasticsearch:9200"
    }
  }
  
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/config/staging.json`
```json
{}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/config/test.json`
```json
{
  "mongo": { "url": "mongodb://localhost:27017/mooc-backend-test" }
}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/persistence/BackofficeElasticConfigFactory.ts`
```typescript
import ElasticConfig from '../../../../Shared/infrastructure/persistence/elasticsearch/ElasticConfig';
import config from '../config';

export class BackofficeElasticConfigFactory {
  static createConfig(): ElasticConfig {
    return {
      url: config.get('elastic.url'),
      indexName: config.get('elastic.indexName'),
      indexConfig: config.get('elastic.config')
    };
  }
}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/persistence/ElasticBackofficeCourseRepository.ts`
```typescript
import { Criteria } from '../../../../Shared/domain/criteria/Criteria';
import { ElasticRepository } from '../../../../Shared/infrastructure/persistence/elasticsearch/ElasticRepository';
import { BackofficeCourse } from '../../domain/BackofficeCourse';
import { BackofficeCourseRepository } from '../../domain/BackofficeCourseRepository';

export class ElasticBackofficeCourseRepository
  extends ElasticRepository<BackofficeCourse>
  implements BackofficeCourseRepository
{
  async searchAll(): Promise<BackofficeCourse[]> {
    return this.searchAllInElastic(BackofficeCourse.fromPrimitives);
  }

  async save(course: BackofficeCourse): Promise<void> {
    return this.persist(course.id.value, course);
  }

  async matching(criteria: Criteria): Promise<BackofficeCourse[]> {
    return this.searchByCriteria(criteria, BackofficeCourse.fromPrimitives);
  }
}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/persistence/MongoBackofficeCourseRepository.ts`
```typescript
import { Criteria } from '../../../../Shared/domain/criteria/Criteria';
import { MongoRepository } from '../../../../Shared/infrastructure/persistence/mongo/MongoRepository';
import { BackofficeCourse } from '../../domain/BackofficeCourse';
import { BackofficeCourseRepository } from '../../domain/BackofficeCourseRepository';

interface CourseDocument {
  _id: string;
  name: string;
  duration: string;
}

export class MongoBackofficeCourseRepository
  extends MongoRepository<BackofficeCourse>
  implements BackofficeCourseRepository
{
  public save(course: BackofficeCourse): Promise<void> {
    return this.persist(course.id.value, course);
  }

  protected collectionName(): string {
    return 'backoffice_courses';
  }

  public async searchAll(): Promise<BackofficeCourse[]> {
    const collection = await this.collection();
    const documents = await collection.find<CourseDocument>({}, {}).toArray();

    return documents.map(document =>
      BackofficeCourse.fromPrimitives({ name: document.name, duration: document.duration, id: document._id })
    );
  }

  public async matching(criteria: Criteria): Promise<BackofficeCourse[]> {
    const documents = await this.searchByCriteria<CourseDocument>(criteria);

    return documents.map(document =>
      BackofficeCourse.fromPrimitives({ name: document.name, duration: document.duration, id: document._id })
    );
  }
}
```

## File: `src/Contexts/Backoffice/Courses/infrastructure/persistence/MongoCriteriaConverter.ts`
```typescript
import { Criteria } from '../../../../Shared/domain/criteria/Criteria';
import { Filter } from '../../../../Shared/domain/criteria/Filter';
import { Operator } from '../../../../Shared/domain/criteria/FilterOperator';
import { Filters } from '../../../../Shared/domain/criteria/Filters';
import { Order } from '../../../../Shared/domain/criteria/Order';

type MongoFilterOperator = '$eq' | '$ne' | '$gt' | '$lt' | '$regex';
type MongoFilterValue = boolean | string | number;
type MongoFilterOperation = { [operator in MongoFilterOperator]?: MongoFilterValue };
type MongoFilter = { [field: string]: MongoFilterOperation } | { [field: string]: { $not: MongoFilterOperation } };
type MongoDirection = 1 | -1;
type MongoSort = { [field: string]: MongoDirection };

interface MongoQuery {
  filter: MongoFilter;
  sort: MongoSort;
  skip: number;
  limit: number;
}

interface TransformerFunction<T, K> {
  (value: T): K;
}

export class MongoCriteriaConverter {
  private filterTransformers: Map<Operator, TransformerFunction<Filter, MongoFilter>>;

  constructor() {
    this.filterTransformers = new Map<Operator, TransformerFunction<Filter, MongoFilter>>([
      [Operator.EQUAL, this.equalFilter],
      [Operator.NOT_EQUAL, this.notEqualFilter],
      [Operator.GT, this.greaterThanFilter],
      [Operator.LT, this.lowerThanFilter],
      [Operator.CONTAINS, this.containsFilter],
      [Operator.NOT_CONTAINS, this.notContainsFilter]
    ]);
  }

  public convert(criteria: Criteria): MongoQuery {
    return {
      filter: criteria.hasFilters() ? this.generateFilter(criteria.filters) : {},
      sort: criteria.order.hasOrder() ? this.generateSort(criteria.order) : { _id: -1 },
      skip: criteria.offset || 0,
      limit: criteria.limit || 0
    };
  }

  protected generateFilter(filters: Filters): MongoFilter {
    const filter = filters.filters.map(filter => {
      const transformer = this.filterTransformers.get(filter.operator.value);

      if (!transformer) {
        throw Error(`Unexpected operator value ${filter.operator.value}`);
      }

      return transformer(filter);
    });

    return Object.assign({}, ...filter);
  }

  protected generateSort(order: Order): MongoSort {
    return {
      [order.orderBy.value === 'id' ? '_id' : order.orderBy.value]: order.orderType.isAsc() ? 1 : -1
    };
  }

  private equalFilter(filter: Filter): MongoFilter {
    return { [filter.field.value]: { $eq: filter.value.value } };
  }

  private notEqualFilter(filter: Filter): MongoFilter {
    return { [filter.field.value]: { $ne: filter.value.value } };
  }

  private greaterThanFilter(filter: Filter): MongoFilter {
    return { [filter.field.value]: { $gt: filter.value.value } };
  }

  private lowerThanFilter(filter: Filter): MongoFilter {
    return { [filter.field.value]: { $lt: filter.value.value } };
  }

  private containsFilter(filter: Filter): MongoFilter {
    return { [filter.field.value]: { $regex: filter.value.value } };
  }

  private notContainsFilter(filter: Filter): MongoFilter {
    return { [filter.field.value]: { $not: { $regex: filter.value.value } } };
  }
}
```

## File: `src/Contexts/Mooc/Courses/application/CourseCreator.ts`
```typescript
import { EventBus } from '../../../Shared/domain/EventBus';
import { CourseId } from '../../Shared/domain/Courses/CourseId';
import { Course } from '../domain/Course';
import { CourseDuration } from '../domain/CourseDuration';
import { CourseName } from '../domain/CourseName';
import { CourseRepository } from '../domain/CourseRepository';

export class CourseCreator {
  constructor(private repository: CourseRepository, private eventBus: EventBus) {}

  async run(params: { id: CourseId; name: CourseName; duration: CourseDuration }): Promise<void> {
    const course = Course.create(params.id, params.name, params.duration);
    await this.repository.save(course);
    await this.eventBus.publish(course.pullDomainEvents());
  }
}
```

## File: `src/Contexts/Mooc/Courses/application/CreateCourseCommandHandler.ts`
```typescript
import { CommandHandler } from '../../../Shared/domain/CommandHandler';
import { CourseCreator } from './CourseCreator';
import { Command } from '../../../Shared/domain/Command';
import { CourseId } from '../../Shared/domain/Courses/CourseId';
import { CourseName } from '../domain/CourseName';
import { CourseDuration } from '../domain/CourseDuration';
import { CreateCourseCommand } from '../domain/CreateCourseCommand';

export class CreateCourseCommandHandler implements CommandHandler<CreateCourseCommand> {
  constructor(private courseCreator: CourseCreator) {}

  subscribedTo(): Command {
    return CreateCourseCommand;
  }

  async handle(command: CreateCourseCommand): Promise<void> {
    const id = new CourseId(command.id);
    const name = new CourseName(command.name);
    const duration = new CourseDuration(command.duration);
    await this.courseCreator.run({ id, name, duration });
  }
}
```

## File: `src/Contexts/Mooc/Courses/application/Create/CourseCreator.ts`
```typescript
import { EventBus } from '../../../../Shared/domain/EventBus';
import { CourseId } from '../../../Shared/domain/Courses/CourseId';
import { Course } from '../../domain/Course';
import { CourseDuration } from '../../domain/CourseDuration';
import { CourseName } from '../../domain/CourseName';
import { CourseRepository } from '../../domain/CourseRepository';

export class CourseCreator {
  constructor(private repository: CourseRepository, private eventBus: EventBus) {}

  async run(params: { id: CourseId; name: CourseName; duration: CourseDuration }): Promise<void> {
    const course = Course.create(params.id, params.name, params.duration);
    await this.repository.save(course);
    await this.eventBus.publish(course.pullDomainEvents());
  }
}
```

## File: `src/Contexts/Mooc/Courses/application/Create/CreateCourseCommandHandler.ts`
```typescript
import { CommandHandler } from '../../../../Shared/domain/CommandHandler';
import { CourseCreator } from './CourseCreator';
import { Command } from '../../../../Shared/domain/Command';
import { CourseId } from '../../../Shared/domain/Courses/CourseId';
import { CourseName } from '../../domain/CourseName';
import { CourseDuration } from '../../domain/CourseDuration';
import { CreateCourseCommand } from '../../domain/CreateCourseCommand';

export class CreateCourseCommandHandler implements CommandHandler<CreateCourseCommand> {
  constructor(private courseCreator: CourseCreator) {}

  subscribedTo(): Command {
    return CreateCourseCommand;
  }

  async handle(command: CreateCourseCommand): Promise<void> {
    const id = new CourseId(command.id);
    const name = new CourseName(command.name);
    const duration = new CourseDuration(command.duration);
    await this.courseCreator.run({ id, name, duration });
  }
}
```

## File: `src/Contexts/Mooc/Courses/application/SearchAll/CoursesFinder.ts`
```typescript
import { CourseRepository } from '../../domain/CourseRepository';
import { CoursesResponse } from './CoursesResponse';

export class CoursesFinder {
  constructor(private coursesRepository: CourseRepository) {}

  async run() {
    const courses = await this.coursesRepository.searchAll();

    return new CoursesResponse(courses);
  }
}
```

## File: `src/Contexts/Mooc/Courses/application/SearchAll/CoursesResponse.ts`
```typescript
import { Course } from '../../domain/Course';

interface CourseResponse {
  id: string;
  name: string;
  duration: string;
}

export class CoursesResponse {
  public readonly courses: Array<CourseResponse>;

  constructor(courses: Array<Course>) {
    this.courses = courses.map(course => course.toPrimitives());
  }
}
```

## File: `src/Contexts/Mooc/Courses/application/SearchAll/SearchAllCoursesQuery.ts`
```typescript
import { Query } from '../../../../Shared/domain/Query';

export class SearchAllCoursesQuery implements Query {}
```

## File: `src/Contexts/Mooc/Courses/application/SearchAll/SearchAllCoursesQueryHandler.ts`
```typescript
import { Query } from '../../../../Shared/domain/Query';
import { QueryHandler } from '../../../../Shared/domain/QueryHandler';
import { CoursesResponse } from './CoursesResponse';
import { CoursesFinder } from './CoursesFinder';
import { SearchAllCoursesQuery } from './SearchAllCoursesQuery';

export class SearchAllCoursesQueryHandler implements QueryHandler<SearchAllCoursesQuery, CoursesResponse> {
  constructor(private coursesFinder: CoursesFinder) {}

  subscribedTo(): Query {
    return SearchAllCoursesQuery;
  }

  async handle(_query: SearchAllCoursesQuery): Promise<CoursesResponse> {
    return this.coursesFinder.run();
  }
}
```

## File: `src/Contexts/Mooc/Courses/domain/Course.ts`
```typescript
import { AggregateRoot } from '../../../Shared/domain/AggregateRoot';
import { CourseId } from '../../Shared/domain/Courses/CourseId';
import { CourseCreatedDomainEvent } from './CourseCreatedDomainEvent';
import { CourseDuration } from './CourseDuration';
import { CourseName } from './CourseName';

export class Course extends AggregateRoot {
  readonly id: CourseId;
  readonly name: CourseName;
  readonly duration: CourseDuration;

  constructor(id: CourseId, name: CourseName, duration: CourseDuration) {
    super();
    this.id = id;
    this.name = name;
    this.duration = duration;
  }

  static create(id: CourseId, name: CourseName, duration: CourseDuration): Course {
    const course = new Course(id, name, duration);

    course.record(
      new CourseCreatedDomainEvent({
        aggregateId: course.id.value,
        duration: course.duration.value,
        name: course.name.value
      })
    );

    return course;
  }
  static fromPrimitives(plainData: { id: string; name: string; duration: string }): Course {
    return new Course(
      new CourseId(plainData.id),
      new CourseName(plainData.name),
      new CourseDuration(plainData.duration)
    );
  }

  toPrimitives(): any {
    return {
      id: this.id.value,
      name: this.name.value,
      duration: this.duration.value
    };
  }
}
```

## File: `src/Contexts/Mooc/Courses/domain/CourseCreatedDomainEvent.ts`
```typescript
import { DomainEvent } from '../../../Shared/domain/DomainEvent';

type CreateCourseDomainEventAttributes = {
  readonly duration: string;
  readonly name: string;
};

export class CourseCreatedDomainEvent extends DomainEvent {
  static readonly EVENT_NAME = 'course.created';

  readonly duration: string;
  readonly name: string;

  constructor({
    aggregateId,
    name,
    duration,
    eventId,
    occurredOn
  }: {
    aggregateId: string;
    eventId?: string;
    duration: string;
    name: string;
    occurredOn?: Date;
  }) {
    super({ eventName: CourseCreatedDomainEvent.EVENT_NAME, aggregateId, eventId, occurredOn });
    this.duration = duration;
    this.name = name;
  }

  toPrimitives(): CreateCourseDomainEventAttributes {
    const { name, duration } = this;
    return {
      name,
      duration
    };
  }

  static fromPrimitives(params: {
    aggregateId: string;
    attributes: CreateCourseDomainEventAttributes;
    eventId: string;
    occurredOn: Date;
  }): DomainEvent {
    const { aggregateId, attributes, occurredOn, eventId } = params;
    return new CourseCreatedDomainEvent({
      aggregateId,
      duration: attributes.duration,
      name: attributes.name,
      eventId,
      occurredOn
    });
  }
}
```

## File: `src/Contexts/Mooc/Courses/domain/CourseDuration.ts`
```typescript
import { StringValueObject } from '../../../Shared/domain/value-object/StringValueObject';

export class CourseDuration extends StringValueObject {}
```

## File: `src/Contexts/Mooc/Courses/domain/CourseName.ts`
```typescript
import { StringValueObject } from '../../../Shared/domain/value-object/StringValueObject';
import { CourseNameLengthExceeded } from './CourseNameLengthExceeded';

export class CourseName extends StringValueObject {
  constructor(value: string) {
    super(value);
    this.ensureLengthIsLessThan30Characters(value);
  }

  private ensureLengthIsLessThan30Characters(value: string): void {
    if (value.length > 30) {
      throw new CourseNameLengthExceeded(`The Course Name <${value}> has more than 30 characters`);
    }
  }
}
```

## File: `src/Contexts/Mooc/Courses/domain/CourseNameLengthExceeded.ts`
```typescript
import { InvalidArgumentError } from '../../../Shared/domain/value-object/InvalidArgumentError';

export class CourseNameLengthExceeded extends InvalidArgumentError {}
```

## File: `src/Contexts/Mooc/Courses/domain/CourseRepository.ts`
```typescript
import { Course } from './Course';

export interface CourseRepository {
  save(course: Course): Promise<void>;
  searchAll(): Promise<Array<Course>>;
}
```

## File: `src/Contexts/Mooc/Courses/domain/CreateCourseCommand.ts`
```typescript
import { Command } from '../../../Shared/domain/Command';

type Params = {
  id: string;
  name: string;
  duration: string;
};

export class CreateCourseCommand extends Command {
  id: string;
  name: string;
  duration: string;

  constructor({ id, name, duration }: Params) {
    super();
    this.id = id;
    this.name = name;
    this.duration = duration;
  }
}
```

## File: `src/Contexts/Mooc/Courses/infrastructure/persistence/MongoCourseRepository.ts`
```typescript
import { Nullable } from '../../../../Shared/domain/Nullable';
import { MongoRepository } from '../../../../Shared/infrastructure/persistence/mongo/MongoRepository';
import { CourseId } from '../../../Shared/domain/Courses/CourseId';
import { Course } from '../../domain/Course';
import { CourseRepository } from '../../domain/CourseRepository';

interface CourseDocument {
  _id: string;
  name: string;
  duration: string;
}

export class MongoCourseRepository extends MongoRepository<Course> implements CourseRepository {
  public save(course: Course): Promise<void> {
    return this.persist(course.id.value, course);
  }

  public async search(id: CourseId): Promise<Nullable<Course>> {
    const collection = await this.collection();
    const document = await collection.findOne<CourseDocument>({ _id: id.value });

    return document ? Course.fromPrimitives({ name: document.name, duration: document.duration, id: id.value }) : null;
  }

  protected collectionName(): string {
    return 'courses';
  }

  public async searchAll(): Promise<Course[]> {
    const collection = await this.collection();
    const documents = await collection.find<CourseDocument>({}, {}).toArray();

    return documents.map(document =>
      Course.fromPrimitives({ name: document.name, duration: document.duration, id: document._id })
    );
  }
}
```

## File: `src/Contexts/Mooc/Courses/infrastructure/persistence/TypeOrmCourseRepository.ts`
```typescript
import { EntitySchema } from 'typeorm';
import { Nullable } from '../../../../Shared/domain/Nullable';
import { TypeOrmRepository } from '../../../../Shared/infrastructure/persistence/typeorm/TypeOrmRepository';
import { CourseId } from '../../../Shared/domain/Courses/CourseId';
import { Course } from '../../domain/Course';
import { CourseRepository } from '../../domain/CourseRepository';
import { CourseEntity } from './typeorm/CourseEntity';

export class TypeOrmCourseRepository extends TypeOrmRepository<Course> implements CourseRepository {
  public save(course: Course): Promise<void> {
    return this.persist(course);
  }

  public async search(id: CourseId): Promise<Nullable<Course>> {
    const repository = await this.repository();

    const course = await repository.findOne({ id });

    return course;
  }

  protected entitySchema(): EntitySchema<Course> {
    return CourseEntity;
  }

  public async searchAll(): Promise<Course[]> {
    const repository = await this.repository();

    const courses = await repository.find();

    return courses;
  }
}
```

## File: `src/Contexts/Mooc/Courses/infrastructure/persistence/typeorm/CourseEntity.ts`
```typescript
import { EntitySchema } from 'typeorm';
import { ValueObjectTransformer } from '../../../../../Shared/infrastructure/persistence/typeorm/ValueObjectTransformer';
import { CourseId } from '../../../../Shared/domain/Courses/CourseId';
import { Course } from '../../../domain/Course';
import { CourseDuration } from '../../../domain/CourseDuration';
import { CourseName } from '../../../domain/CourseName';

export const CourseEntity = new EntitySchema<Course>({
  name: 'Course',
  tableName: 'courses',
  target: Course,
  columns: {
    id: {
      type: String,
      primary: true,
      transformer: ValueObjectTransformer(CourseId)
    },
    name: {
      type: String,
      transformer: ValueObjectTransformer(CourseName)
    },
    duration: {
      type: String,
      transformer: ValueObjectTransformer(CourseDuration)
    }
  }
});
```

## File: `src/Contexts/Mooc/CoursesCounter/application/Find/CoursesCounterFinder.ts`
```typescript
import { CoursesCounterNotExist } from '../../domain/CoursesCounterNotExist';
import { CoursesCounterRepository } from '../../domain/CoursesCounterRepository';

export class CoursesCounterFinder {
  constructor(private repository: CoursesCounterRepository) {}

  async run() {
    const counter = await this.repository.search();
    if (!counter) {
      throw new CoursesCounterNotExist();
    }

    return counter.total.value;
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterQuery.ts`
```typescript
import { Query } from '../../../../Shared/domain/Query';

export class FindCoursesCounterQuery implements Query {}
```

## File: `src/Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterQueryHandler.ts`
```typescript
import { QueryHandler } from '../../../../Shared/domain/QueryHandler';
import { FindCoursesCounterQuery } from './FindCoursesCounterQuery';
import { FindCoursesCounterResponse } from './FindCoursesCounterResponse';
import { Query } from '../../../../Shared/domain/Query';
import { CoursesCounterFinder } from './CoursesCounterFinder';

export class FindCoursesCounterQueryHandler
  implements QueryHandler<FindCoursesCounterQuery, FindCoursesCounterResponse>
{
  constructor(private finder: CoursesCounterFinder) {}

  subscribedTo(): Query {
    return FindCoursesCounterQuery;
  }

  async handle(_query: FindCoursesCounterQuery): Promise<FindCoursesCounterResponse> {
    const counter = await this.finder.run();
    return new FindCoursesCounterResponse(counter);
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterResponse.ts`
```typescript
export class FindCoursesCounterResponse {
  readonly total: number;

  constructor(total: number) {
    this.total = total;
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/application/Increment/CoursesCounterIncrementer.ts`
```typescript
import { EventBus } from '../../../../Shared/domain/EventBus';
import { CourseId } from '../../../Shared/domain/Courses/CourseId';
import { CoursesCounterRepository } from '../../domain/CoursesCounterRepository';
import { CoursesCounter } from '../../domain/CoursesCounter';
import { CoursesCounterId } from '../../domain/CoursesCounterId';

export class CoursesCounterIncrementer {
  constructor(private repository: CoursesCounterRepository, private bus: EventBus) {}

  async run(courseId: CourseId) {
    const counter = (await this.repository.search()) || this.initializeCounter();

    if (!counter.hasIncremented(courseId)) {
      counter.increment(courseId);

      await this.repository.save(counter);
      await this.bus.publish(counter.pullDomainEvents());
    }
  }

  private initializeCounter(): CoursesCounter {
    return CoursesCounter.initialize(CoursesCounterId.random());
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/application/Increment/IncrementCoursesCounterOnCourseCreated.ts`
```typescript
import { DomainEventClass } from '../../../../Shared/domain/DomainEvent';
import { DomainEventSubscriber } from '../../../../Shared/domain/DomainEventSubscriber';
import { CourseCreatedDomainEvent } from '../../../Courses/domain/CourseCreatedDomainEvent';
import { CourseId } from '../../../Shared/domain/Courses/CourseId';
import { CoursesCounterIncrementer } from './CoursesCounterIncrementer';

export class IncrementCoursesCounterOnCourseCreated implements DomainEventSubscriber<CourseCreatedDomainEvent> {
  constructor(private incrementer: CoursesCounterIncrementer) {}

  subscribedTo(): DomainEventClass[] {
    return [CourseCreatedDomainEvent];
  }

  async on(domainEvent: CourseCreatedDomainEvent) {
    await this.incrementer.run(new CourseId(domainEvent.aggregateId));
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/domain/CoursesCounter.ts`
```typescript
import { AggregateRoot } from '../../../Shared/domain/AggregateRoot';
import { CourseId } from '../../Shared/domain/Courses/CourseId';
import { CoursesCounterTotal } from './CoursesCounterTotal';
import { CoursesCounterId } from './CoursesCounterId';
import { CoursesCounterIncrementedDomainEvent } from './CoursesCounterIncrementedDomainEvent';
import { Uuid } from '../../../Shared/domain/value-object/Uuid';

export class CoursesCounter extends AggregateRoot {
  readonly id: CoursesCounterId;
  private _total: CoursesCounterTotal;
  readonly existingCourses: Array<CourseId>;

  constructor(id: CoursesCounterId, total: CoursesCounterTotal, existingCourses?: Array<CourseId>) {
    super();
    this.id = id;
    this._total = total;
    this.existingCourses = existingCourses || [];
  }

  public get total(): CoursesCounterTotal {
    return this._total;
  }

  static initialize(id: Uuid): CoursesCounter {
    return new CoursesCounter(id, CoursesCounterTotal.initialize());
  }

  increment(courseId: CourseId) {
    this._total = this.total.increment();
    this.existingCourses.push(courseId);
    this.record(new CoursesCounterIncrementedDomainEvent({ aggregateId: this.id.value, total: this.total.value }));
  }

  hasIncremented(courseId: CourseId): boolean {
    const exists = this.existingCourses.find(entry => entry.value === courseId.value);
    return exists !== undefined;
  }

  toPrimitives() {
    return {
      id: this.id.value,
      total: this.total.value,
      existingCourses: this.existingCourses.map(courseId => courseId.value)
    };
  }

  static fromPrimitives(data: { id: string; total: number; existingCourses: string[] }): CoursesCounter {
    return new CoursesCounter(
      new CoursesCounterId(data.id),
      new CoursesCounterTotal(data.total),
      data.existingCourses.map(entry => new CourseId(entry))
    );
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterId.ts`
```typescript
import { Uuid } from '../../../Shared/domain/value-object/Uuid';

export class CoursesCounterId extends Uuid {}
```

## File: `src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterIncrementedDomainEvent.ts`
```typescript
import { DomainEvent } from '../../../Shared/domain/DomainEvent';

type CoursesCounterIncrementedAttributes = { total: number };

export class CoursesCounterIncrementedDomainEvent extends DomainEvent {
  static readonly EVENT_NAME = 'courses_counter.incremented';
  readonly total: number;

  constructor(data: { aggregateId: string; total: number; eventId?: string; occurredOn?: Date }) {
    const { aggregateId, eventId, occurredOn } = data;
    super({ eventName: CoursesCounterIncrementedDomainEvent.EVENT_NAME, aggregateId, eventId, occurredOn });
    this.total = data.total;
  }

  toPrimitives() {
    return {
      total: this.total
    };
  }

  static fromPrimitives(params: {
    aggregateId: string;
    attributes: CoursesCounterIncrementedAttributes;
    eventId: string;
    occurredOn: Date;
  }) {
    const { aggregateId, attributes, eventId, occurredOn } = params;
    return new CoursesCounterIncrementedDomainEvent({
      aggregateId,
      total: attributes.total,
      eventId,
      occurredOn
    });
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterNotExist.ts`
```typescript
export class CoursesCounterNotExist extends Error {
  constructor() {
    super('The courses counter does not exists');
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterRepository.ts`
```typescript
import { CoursesCounter } from './CoursesCounter';
import { Nullable } from '../../../Shared/domain/Nullable';

export interface CoursesCounterRepository {
  search(): Promise<Nullable<CoursesCounter>>;
  save(counter: CoursesCounter): Promise<void>;
}
```

## File: `src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterTotal.ts`
```typescript
import { NumberValueObject } from '../../../Shared/domain/value-object/IntValueObject';

export class CoursesCounterTotal extends NumberValueObject {
  increment(): CoursesCounterTotal {
    return new CoursesCounterTotal(this.value + 1);
  }

  static initialize(): CoursesCounterTotal {
    return new CoursesCounterTotal(0);
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/infrastructure/InMemoryCoursesCounterRepository.ts`
```typescript
import { CoursesCounterRepository } from '../domain/CoursesCounterRepository';
import { CoursesCounter } from '../domain/CoursesCounter';
import { CoursesCounterId } from '../domain/CoursesCounterId';
import { CoursesCounterTotal } from '../domain/CoursesCounterTotal';

export class InMemoryCoursesCounterRepository implements CoursesCounterRepository {
  private counter: CoursesCounter;
  constructor() {
    this.counter = new CoursesCounter(CoursesCounterId.random(), new CoursesCounterTotal(0), []);
  }

  async search(): Promise<CoursesCounter> {
    return this.counter;
  }

  async save(counter: CoursesCounter): Promise<void> {
    this.counter = counter;
  }
}
```

## File: `src/Contexts/Mooc/CoursesCounter/infrastructure/persistence/mongo/MongoCoursesCounterRepository.ts`
```typescript
import { MongoRepository } from '../../../../../Shared/infrastructure/persistence/mongo/MongoRepository';
import { Nullable } from '../../../../../Shared/domain/Nullable';
import { CoursesCounter } from '../../../domain/CoursesCounter';
import { CoursesCounterRepository } from '../../../domain/CoursesCounterRepository';

interface CoursesCounterDocument {
  _id: string;
  total: number;
  existingCourses: string[];
}

export class MongoCoursesCounterRepository extends MongoRepository<CoursesCounter> implements CoursesCounterRepository {
  protected collectionName(): string {
    return 'coursesCounter';
  }

  public save(counter: CoursesCounter): Promise<void> {
    return this.persist(counter.id.value, counter);
  }

  public async search(): Promise<Nullable<CoursesCounter>> {
    const collection = await this.collection();

    const document = await collection.findOne<CoursesCounterDocument>({});
    return document ? CoursesCounter.fromPrimitives({ ...document, id: document._id }) : null;
  }
}
```

## File: `src/Contexts/Mooc/Shared/domain/Courses/CourseId.ts`
```typescript
import { Uuid } from '../../../../Shared/domain/value-object/Uuid';

export class CourseId extends Uuid {}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/RabbitMQ/RabbitMQConfigFactory.ts`
```typescript
import { ConnectionSettings } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/ConnectionSettings';
import { ExchangeSetting } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/ExchangeSetting';
import config from '../config';

export type RabbitMQConfig = {
  connectionSettings: ConnectionSettings;
  exchangeSettings: ExchangeSetting;
  maxRetries: number;
  retryTtl: number;
};
export class RabbitMQConfigFactory {
  static createConfig(): RabbitMQConfig {
    return config.get('rabbitmq');
  }
}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/RabbitMQ/RabbitMQEventBusFactory.ts`
```typescript
import { DomainEventFailoverPublisher } from '../../../../Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher';
import { RabbitMqConnection } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';
import { RabbitMQEventBus } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/RabbitMQEventBus';
import { RabbitMQqueueFormatter } from '../../../../Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter';
import { RabbitMQConfig } from './RabbitMQConfigFactory';

export class RabbitMQEventBusFactory {
  static create(
    failoverPublisher: DomainEventFailoverPublisher,
    connection: RabbitMqConnection,
    queueNameFormatter: RabbitMQqueueFormatter,
    config: RabbitMQConfig
  ): RabbitMQEventBus {
    return new RabbitMQEventBus({
      failoverPublisher,
      connection,
      exchange: config.exchangeSettings.name,
      queueNameFormatter: queueNameFormatter,
      maxRetries: config.maxRetries
    });
  }
}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/config/default.json`
```json
{}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/config/dev.json`
```json
{}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/config/end2end.json`
```json
{}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/config/index.ts`
```typescript
import convict from 'convict';

const moocConfig = convict({
  env: {
    doc: 'The application environment.',
    format: ['production', 'development', 'staging', 'test'],
    default: 'default',
    env: 'NODE_ENV'
  },
  mongo: {
    url: {
      doc: 'The Mongo connection URL',
      format: String,
      env: 'MONGO_URL',
      default: 'mongodb://localhost:27017/mooc-backend-dev'
    }
  },
  typeorm: {
    host: {
      doc: 'The database host',
      format: String,
      env: 'TYPEORM_HOST',
      default: 'localhost'
    },
    port: {
      doc: 'The database port',
      format: Number,
      env: 'TYPEORM_PORT',
      default: 5432
    },
    username: {
      doc: 'The database username',
      format: String,
      env: 'TYPEORM_USERNAME',
      default: 'codely'
    },
    password: {
      doc: 'The database password',
      format: String,
      env: 'TYPEORM_PASSWORD',
      default: 'codely'
    },
    database: {
      doc: 'The database name',
      format: String,
      env: 'TYPEORM_DATABASE',
      default: 'mooc-backend-dev'
    }
  },
  rabbitmq: {
    connectionSettings: {
      username: {
        doc: 'RabbitMQ username',
        format: String,
        env: 'RABBITMQ_USERNAME',
        default: 'guest'
      },
      password: {
        doc: 'RabbitMQ password',
        format: String,
        env: 'RABBITMQ_PASSWORD',
        default: 'guest'
      },
      vhost: {
        doc: 'RabbitMQ virtual host',
        format: String,
        env: 'RABBITMQ_VHOST',
        default: '/'
      },
      connection: {
        secure: {
          doc: 'RabbitMQ secure protocol',
          format: Boolean,
          env: 'RABBITMQ_SECURE',
          default: false
        },
        hostname: {
          doc: 'RabbitMQ hostname',
          format: String,
          env: 'RABBITMQ_HOSTNAME',
          default: 'localhost'
        },
        port: {
          doc: 'RabbitMQ amqp port',
          format: Number,
          env: 'RABBITMQ_PORT',
          default: 5672
        }
      }
    },
    exchangeSettings: {
      name: {
        doc: 'RabbitMQ exchange name',
        format: String,
        env: 'RABBITMQ_EXCHANGE_NAME',
        default: 'domain_events'
      }
    },
    maxRetries: {
      doc: 'Max number of retries for each message',
      format: Number,
      env: 'RABBITMQ_MAX_RETRIES',
      default: 3
    },
    retryTtl: {
      doc: 'Ttl for messages in the retry queue',
      format: Number,
      env: 'RABBITMQ_RETRY_TTL',
      default: 1000
    }
  }
});

moocConfig.loadFile([__dirname + '/default.json', __dirname + '/' + moocConfig.get('env') + '.json']);

export default moocConfig;
```

## File: `src/Contexts/Mooc/Shared/infrastructure/config/production.json`
```json
{}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/config/staging.json`
```json
{}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/config/test.json`
```json
{
  "mongo": { "url": "mongodb://localhost:27017/mooc-backend-test" },
  "typeorm": {"database": "mooc-backend-dev"}
}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/persistence/mongo/MongoConfigFactory.ts`
```typescript
import config from '../../config';
import MongoConfig from '../../../../../Shared/infrastructure/persistence/mongo/MongoConfig';

export class MongoConfigFactory {
  static createConfig(): MongoConfig {
    return {
      url: config.get('mongo.url')
    };
  }
}
```

## File: `src/Contexts/Mooc/Shared/infrastructure/persistence/postgre/TypeOrmConfigFactory.ts`
```typescript
import { TypeOrmConfig } from '../../../../../Shared/infrastructure/persistence/typeorm/TypeOrmConfig';
import config from '../../config';

export class TypeOrmConfigFactory {
  static createConfig(): TypeOrmConfig {
    return {
      host: config.get('typeorm.host'),
      port: config.get('typeorm.port'),
      username: config.get('typeorm.username'),
      password: config.get('typeorm.password'),
      database: config.get('typeorm.database')
    };
  }
}
```

## File: `src/Contexts/Shared/domain/AggregateRoot.ts`
```typescript
import { DomainEvent } from './DomainEvent';

export abstract class AggregateRoot {
  private domainEvents: Array<DomainEvent>;

  constructor() {
    this.domainEvents = [];
  }

  pullDomainEvents(): Array<DomainEvent> {
    const domainEvents = this.domainEvents.slice();
    this.domainEvents = [];

    return domainEvents;
  }

  record(event: DomainEvent): void {
    this.domainEvents.push(event);
  }

  abstract toPrimitives(): any;
}
```

## File: `src/Contexts/Shared/domain/Command.ts`
```typescript
export abstract class Command {}
```

## File: `src/Contexts/Shared/domain/CommandBus.ts`
```typescript
import { Command } from './Command';

export interface CommandBus {
  dispatch(command: Command): Promise<void>;
}
```

## File: `src/Contexts/Shared/domain/CommandHandler.ts`
```typescript
import { Command } from './Command';

export interface CommandHandler<T extends Command> {
  subscribedTo(): Command;
  handle(command: T): Promise<void>;
}
```

## File: `src/Contexts/Shared/domain/CommandNotRegisteredError.ts`
```typescript
import { Command } from './Command';

export class CommandNotRegisteredError extends Error {
  constructor(command: Command) {
    super(`The command <${command.constructor.name}> hasn't a command handler associated`);
  }
}
```

## File: `src/Contexts/Shared/domain/DomainEvent.ts`
```typescript
import { Uuid } from './value-object/Uuid';

export abstract class DomainEvent {
  static EVENT_NAME: string;
  static fromPrimitives: (params: {
    aggregateId: string;
    eventId: string;
    occurredOn: Date;
    attributes: DomainEventAttributes;
  }) => DomainEvent;

  readonly aggregateId: string;
  readonly eventId: string;
  readonly occurredOn: Date;
  readonly eventName: string;

  constructor(params: { eventName: string; aggregateId: string; eventId?: string; occurredOn?: Date }) {
    const { aggregateId, eventName, eventId, occurredOn } = params;
    this.aggregateId = aggregateId;
    this.eventId = eventId || Uuid.random().value;
    this.occurredOn = occurredOn || new Date();
    this.eventName = eventName;
  }

  abstract toPrimitives(): DomainEventAttributes;
}

export type DomainEventClass = {
  EVENT_NAME: string;
  fromPrimitives(params: {
    aggregateId: string;
    eventId: string;
    occurredOn: Date;
    attributes: DomainEventAttributes;
  }): DomainEvent;
};

type DomainEventAttributes = any;
```

## File: `src/Contexts/Shared/domain/DomainEventSubscriber.ts`
```typescript
import { DomainEvent, DomainEventClass } from './DomainEvent';

export interface DomainEventSubscriber<T extends DomainEvent> {
  subscribedTo(): Array<DomainEventClass>;
  on(domainEvent: T): Promise<void>;
}
```

## File: `src/Contexts/Shared/domain/EventBus.ts`
```typescript
import { DomainEventSubscribers } from '../infrastructure/EventBus/DomainEventSubscribers';
import { DomainEvent } from './DomainEvent';

export interface EventBus {
  publish(events: Array<DomainEvent>): Promise<void>;
  addSubscribers(subscribers: DomainEventSubscribers): void;
}
```

## File: `src/Contexts/Shared/domain/Logger.ts`
```typescript
export default interface Logger {
  debug(message: string): void;
  error(message: string | Error): void;
  info(message: string): void;
}
```

## File: `src/Contexts/Shared/domain/NewableClass.ts`
```typescript
export interface NewableClass<T> extends Function {
  new (...args: any[]): T;
}
```

## File: `src/Contexts/Shared/domain/Nullable.ts`
```typescript
export type Nullable<T> = T | null | undefined;
```

## File: `src/Contexts/Shared/domain/Query.ts`
```typescript
export abstract class Query {}
```

## File: `src/Contexts/Shared/domain/QueryBus.ts`
```typescript
import { Query } from './Query';
import { Response } from './Response';

export interface QueryBus {
  ask<R extends Response>(query: Query): Promise<R>;
}
```

## File: `src/Contexts/Shared/domain/QueryHandler.ts`
```typescript
import { Query } from './Query';
import { Response } from './Response';

export interface QueryHandler<Q extends Query, R extends Response> {
  subscribedTo(): Query;
  handle(query: Q): Promise<R>;
}
```

## File: `src/Contexts/Shared/domain/QueryNotRegisteredError.ts`
```typescript
import { Query } from './Query';

export class QueryNotRegisteredError extends Error {
  constructor(query: Query) {
    super(`The query <${query.constructor.name}> hasn't a query handler associated`);
  }
}
```

## File: `src/Contexts/Shared/domain/Response.ts`
```typescript
export interface Response {}
```

## File: `src/Contexts/Shared/domain/criteria/Criteria.ts`
```typescript
import { Filters } from './Filters';
import { Order } from './Order';

export class Criteria {
  readonly filters: Filters;
  readonly order: Order;
  readonly limit?: number;
  readonly offset?: number;

  constructor(filters: Filters, order: Order, limit?: number, offset?: number) {
    this.filters = filters;
    this.order = order;
    this.limit = limit;
    this.offset = offset;
  }

  public hasFilters(): boolean {
    return this.filters.filters.length > 0;
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/Filter.ts`
```typescript
import { InvalidArgumentError } from '../value-object/InvalidArgumentError';
import { FilterField } from './FilterField';
import { FilterOperator } from './FilterOperator';
import { FilterValue } from './FilterValue';

export class Filter {
  readonly field: FilterField;
  readonly operator: FilterOperator;
  readonly value: FilterValue;

  constructor(field: FilterField, operator: FilterOperator, value: FilterValue) {
    this.field = field;
    this.operator = operator;
    this.value = value;
  }

  static fromValues(values: Map<string, string>): Filter {
    const field = values.get('field');
    const operator = values.get('operator');
    const value = values.get('value');

    if (!field || !operator || !value) {
      throw new InvalidArgumentError(`The filter is invalid`);
    }

    return new Filter(new FilterField(field), FilterOperator.fromValue(operator), new FilterValue(value));
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/FilterField.ts`
```typescript
import { StringValueObject } from '../value-object/StringValueObject';

export class FilterField extends StringValueObject {
  constructor(value: string) {
    super(value);
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/FilterOperator.ts`
```typescript
import { EnumValueObject } from '../value-object/EnumValueObject';
import { InvalidArgumentError } from '../value-object/InvalidArgumentError';

export enum Operator {
  EQUAL = '=',
  NOT_EQUAL = '!=',
  GT = '>',
  LT = '<',
  CONTAINS = 'CONTAINS',
  NOT_CONTAINS = 'NOT_CONTAINS'
}

export class FilterOperator extends EnumValueObject<Operator> {
  constructor(value: Operator) {
    super(value, Object.values(Operator));
  }

  static fromValue(value: string): FilterOperator {
    for (const operatorValue of Object.values(Operator)) {
      if (value === operatorValue.toString()) {
        return new FilterOperator(operatorValue);
      }
    }

    throw new InvalidArgumentError(`The filter operator ${value} is invalid`);
  }

  public isPositive(): boolean {
    return this.value !== Operator.NOT_EQUAL && this.value !== Operator.NOT_CONTAINS;
  }

  protected throwErrorForInvalidValue(value: Operator): void {
    throw new InvalidArgumentError(`The filter operator ${value} is invalid`);
  }

  static equal() {
    return this.fromValue(Operator.EQUAL);
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/FilterValue.ts`
```typescript
import { StringValueObject } from '../value-object/StringValueObject';

export class FilterValue extends StringValueObject {
  constructor(value: string) {
    super(value);
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/Filters.ts`
```typescript
import { Filter } from './Filter';

export class Filters {
  readonly filters: Filter[];

  constructor(filters: Filter[]) {
    this.filters = filters;
  }

  static fromValues(filters: Array<Map<string, string>>): Filters {
    return new Filters(filters.map(Filter.fromValues));
  }

  static none(): Filters {
    return new Filters([]);
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/Order.ts`
```typescript
import { OrderBy } from './OrderBy';
import { OrderType, OrderTypes } from './OrderType';

export class Order {
  readonly orderBy: OrderBy;
  readonly orderType: OrderType;

  constructor(orderBy: OrderBy, orderType: OrderType) {
    this.orderBy = orderBy;
    this.orderType = orderType;
  }

  static fromValues(orderBy?: string, orderType?: string): Order {
    if (!orderBy) {
      return Order.none();
    }

    return new Order(new OrderBy(orderBy), OrderType.fromValue(orderType || OrderTypes.ASC));
  }

  static none(): Order {
    return new Order(new OrderBy(''), new OrderType(OrderTypes.NONE));
  }

  static desc(orderBy: string): Order {
    return new Order(new OrderBy(orderBy), new OrderType(OrderTypes.DESC));
  }

  static asc(orderBy: string): Order {
    return new Order(new OrderBy(orderBy), new OrderType(OrderTypes.ASC));
  }

  public hasOrder() {
    return !this.orderType.isNone();
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/OrderBy.ts`
```typescript
import { StringValueObject } from '../value-object/StringValueObject';

export class OrderBy extends StringValueObject {
  constructor(value: string) {
    super(value);
  }
}
```

## File: `src/Contexts/Shared/domain/criteria/OrderType.ts`
```typescript
import { EnumValueObject } from '../value-object/EnumValueObject';
import { InvalidArgumentError } from '../value-object/InvalidArgumentError';

export enum OrderTypes {
  ASC = 'asc',
  DESC = 'desc',
  NONE = 'none'
}

export class OrderType extends EnumValueObject<OrderTypes> {
  constructor(value: OrderTypes) {
    super(value, Object.values(OrderTypes));
  }

  static fromValue(value: string): OrderType {
    for (const orderTypeValue of Object.values(OrderTypes)) {
      if (value === orderTypeValue.toString()) {
        return new OrderType(orderTypeValue);
      }
    }

    throw new InvalidArgumentError(`The order type ${value} is invalid`);
  }

  public isNone(): boolean {
    return this.value === OrderTypes.NONE;
  }

  public isAsc(): boolean {
    return this.value === OrderTypes.ASC;
  }

  protected throwErrorForInvalidValue(value: OrderTypes): void {
    throw new InvalidArgumentError(`The order type ${value} is invalid`);
  }
}
```

## File: `src/Contexts/Shared/domain/value-object/EnumValueObject.ts`
```typescript
export abstract class EnumValueObject<T> {
  readonly value: T;

  constructor(value: T, public readonly validValues: T[]) {
    this.value = value;
    this.checkValueIsValid(value);
  }

  public checkValueIsValid(value: T): void {
    if (!this.validValues.includes(value)) {
      this.throwErrorForInvalidValue(value);
    }
  }

  protected abstract throwErrorForInvalidValue(value: T): void;
}
```

## File: `src/Contexts/Shared/domain/value-object/IntValueObject.ts`
```typescript
import { ValueObject } from './ValueObject';

export abstract class NumberValueObject extends ValueObject<number> {
  isBiggerThan(other: NumberValueObject): boolean {
    return this.value > other.value;
  }
}
```

## File: `src/Contexts/Shared/domain/value-object/InvalidArgumentError.ts`
```typescript
export class InvalidArgumentError extends Error {}
```

## File: `src/Contexts/Shared/domain/value-object/StringValueObject.ts`
```typescript
import { ValueObject } from './ValueObject';

export abstract class StringValueObject extends ValueObject<string> {}
```

## File: `src/Contexts/Shared/domain/value-object/Uuid.ts`
```typescript
import { v4 as uuid } from 'uuid';
import validate from 'uuid-validate';
import { InvalidArgumentError } from './InvalidArgumentError';
import { ValueObject } from './ValueObject';

export class Uuid extends ValueObject<string> {
  constructor(value: string) {
    super(value);
    this.ensureIsValidUuid(value);
  }

  static random(): Uuid {
    return new Uuid(uuid());
  }

  private ensureIsValidUuid(id: string): void {
    if (!validate(id)) {
      throw new InvalidArgumentError(`<${this.constructor.name}> does not allow the value <${id}>`);
    }
  }
}
```

## File: `src/Contexts/Shared/domain/value-object/ValueObject.ts`
```typescript
import { InvalidArgumentError } from './InvalidArgumentError';

export type Primitives = String | string | number | Boolean | boolean | Date;

export abstract class ValueObject<T extends Primitives> {
  readonly value: T;

  constructor(value: T) {
    this.value = value;
    this.ensureValueIsDefined(value);
  }

  private ensureValueIsDefined(value: T): void {
    if (value === null || value === undefined) {
      throw new InvalidArgumentError('Value must be defined');
    }
  }

  equals(other: ValueObject<T>): boolean {
    return other.constructor.name === this.constructor.name && other.value === this.value;
  }

  toString(): string {
    return this.value.toString();
  }
}
```

## File: `src/Contexts/Shared/infrastructure/WinstonLogger.ts`
```typescript
import winston, { Logger as WinstonLoggerType } from 'winston';
import Logger from '../domain/Logger';

enum Levels {
  DEBUG = 'debug',
  ERROR = 'error',
  INFO = 'info'
}

class WinstonLogger implements Logger {
  private logger: WinstonLoggerType;

  constructor() {
    this.logger = winston.createLogger({
      format: winston.format.combine(
        winston.format.prettyPrint(),
        winston.format.errors({ stack: true }),
        winston.format.splat(),
        winston.format.colorize(),
        winston.format.simple()
      ),
      transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: `logs/${Levels.DEBUG}.log`, level: Levels.DEBUG }),
        new winston.transports.File({ filename: `logs/${Levels.ERROR}.log`, level: Levels.ERROR }),
        new winston.transports.File({ filename: `logs/${Levels.INFO}.log`, level: Levels.INFO })
      ]
    });
  }

  debug(message: string) {
    this.logger.debug(message);
  }

  error(message: string | Error) {
    this.logger.error(message);
  }

  info(message: string) {
    this.logger.info(message);
  }
}
export default WinstonLogger;
```

## File: `src/Contexts/Shared/infrastructure/CommandBus/CommandHandlers.ts`
```typescript
import { Command } from '../../domain/Command';
import { CommandHandler } from '../../domain/CommandHandler';
import { CommandNotRegisteredError } from '../../domain/CommandNotRegisteredError';

export class CommandHandlers extends Map<Command, CommandHandler<Command>> {
  constructor(commandHandlers: Array<CommandHandler<Command>>) {
    super();

    commandHandlers.forEach(commandHandler => {
      this.set(commandHandler.subscribedTo(), commandHandler);
    });
  }

  public get(command: Command): CommandHandler<Command> {
    const commandHandler = super.get(command.constructor);

    if (!commandHandler) {
      throw new CommandNotRegisteredError(command);
    }

    return commandHandler;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/CommandBus/InMemoryCommandBus.ts`
```typescript
import { Command } from '../../domain/Command';
import { CommandBus } from './../../domain/CommandBus';
import { CommandHandlers } from './CommandHandlers';

export class InMemoryCommandBus implements CommandBus {
  constructor(private commandHandlers: CommandHandlers) {}

  async dispatch(command: Command): Promise<void> {
    const handler = this.commandHandlers.get(command);

    await handler.handle(command);
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/DomainEventDeserializer.ts`
```typescript
import { DomainEventClass } from '../../domain/DomainEvent';
import { DomainEventSubscribers } from './DomainEventSubscribers';

type DomainEventJSON = {
  type: string;
  aggregateId: string;
  attributes: string;
  id: string;
  occurred_on: string;
};

export class DomainEventDeserializer extends Map<string, DomainEventClass> {
  static configure(subscribers: DomainEventSubscribers) {
    const mapping = new DomainEventDeserializer();
    subscribers.items.forEach(subscriber => {
      subscriber.subscribedTo().forEach(mapping.registerEvent.bind(mapping));
    });

    return mapping;
  }

  private registerEvent(domainEvent: DomainEventClass) {
    const eventName = domainEvent.EVENT_NAME;
    this.set(eventName, domainEvent);
  }

  deserialize(event: string) {
    const eventData = JSON.parse(event).data as DomainEventJSON;
    const { type, aggregateId, attributes, id, occurred_on } = eventData;
    const eventClass = super.get(type);

    if (!eventClass) {
      throw Error(`DomainEvent mapping not found for event ${type}`);
    }

    return eventClass.fromPrimitives({
      aggregateId,
      attributes,
      occurredOn: new Date(occurred_on),
      eventId: id
    });
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/DomainEventJsonSerializer.ts`
```typescript
import { DomainEvent } from '../../domain/DomainEvent';

export class DomainEventJsonSerializer {
  static serialize(event: DomainEvent): string {
    return JSON.stringify({
      data: {
        id: event.eventId,
        type: event.eventName,
        occurred_on: event.occurredOn.toISOString(),
        aggregateId: event.aggregateId,
        attributes: event.toPrimitives()
      }
    });
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers.ts`
```typescript
import { ContainerBuilder, Definition } from 'node-dependency-injection';
import { DomainEvent } from '../../domain/DomainEvent';
import { DomainEventSubscriber } from '../../domain/DomainEventSubscriber';

export class DomainEventSubscribers {
  constructor(public items: Array<DomainEventSubscriber<DomainEvent>>) {}

  static from(container: ContainerBuilder): DomainEventSubscribers {
    const subscriberDefinitions = container.findTaggedServiceIds('domainEventSubscriber') as Map<String, Definition>;
    const subscribers: Array<DomainEventSubscriber<DomainEvent>> = [];

    subscriberDefinitions.forEach((value: Definition, key: String) => {
      const domainEventSubscriber = container.get<DomainEventSubscriber<DomainEvent>>(key.toString());
      subscribers.push(domainEventSubscriber);
    });

    return new DomainEventSubscribers(subscribers);
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher.ts`
```typescript
import { Collection, MongoClient } from 'mongodb';
import { DomainEvent } from '../../../domain/DomainEvent';
import { DomainEventDeserializer } from '../DomainEventDeserializer';
import { DomainEventJsonSerializer } from '../DomainEventJsonSerializer';

export class DomainEventFailoverPublisher {
  static collectionName = 'DomainEvents';

  constructor(private client: Promise<MongoClient>, private deserializer?: DomainEventDeserializer) {}

  protected async collection(): Promise<Collection> {
    return (await this.client).db().collection(DomainEventFailoverPublisher.collectionName);
  }

  setDeserializer(deserializer: DomainEventDeserializer) {
    this.deserializer = deserializer;
  }

  async publish(event: DomainEvent): Promise<void> {
    const collection = await this.collection();

    const eventSerialized = DomainEventJsonSerializer.serialize(event);
    const options = { upsert: true };
    const update = { $set: { eventId: event.eventId, event: eventSerialized } };

    await collection.updateOne({ eventId: event.eventId }, update, options);
  }

  async consume(): Promise<Array<DomainEvent>> {
    const collection = await this.collection();
    const documents = await collection.find().limit(200).toArray();
    if (!this.deserializer) {
      throw new Error('Deserializer has not been set yet');
    }

    const events = documents.map(document => this.deserializer!.deserialize(document.event));

    return events.filter(Boolean) as Array<DomainEvent>;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/InMemory/InMemoryAsyncEventBus.ts`
```typescript
import { EventEmitter } from 'events';
import { DomainEvent } from '../../../domain/DomainEvent';
import { EventBus } from '../../../domain/EventBus';
import { DomainEventSubscribers } from '../DomainEventSubscribers';

export class InMemoryAsyncEventBus extends EventEmitter implements EventBus {
  async publish(events: DomainEvent[]): Promise<void> {
    events.map(event => this.emit(event.eventName, event));
  }

  addSubscribers(subscribers: DomainEventSubscribers) {
    subscribers.items.forEach(subscriber => {
      subscriber.subscribedTo().forEach(event => {
        this.on(event.EVENT_NAME, subscriber.on.bind(subscriber));
      });
    });
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/ConnectionSettings.ts`
```typescript
export type ConnectionSettings = {
  username: string;
  password: string;
  vhost: string;
  connection: {
    secure: boolean;
    hostname: string;
    port: number;
  };
};
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/ExchangeSetting.ts`
```typescript
export type ExchangeSetting = {
  name: string;
  type?: string;
};
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/RabbitMQConfigurer.ts`
```typescript
import { DomainEvent } from '../../../domain/DomainEvent';
import { DomainEventSubscriber } from '../../../domain/DomainEventSubscriber';
import { RabbitMqConnection } from './RabbitMqConnection';
import { RabbitMQExchangeNameFormatter } from './RabbitMQExchangeNameFormatter';
import { RabbitMQqueueFormatter } from './RabbitMQqueueFormatter';

export class RabbitMQConfigurer {
  constructor(
    private connection: RabbitMqConnection,
    private queueNameFormatter: RabbitMQqueueFormatter,
    private messageRetryTtl: number
  ) {}

  async configure(params: { exchange: string; subscribers: Array<DomainEventSubscriber<DomainEvent>> }): Promise<void> {
    const retryExchange = RabbitMQExchangeNameFormatter.retry(params.exchange);
    const deadLetterExchange = RabbitMQExchangeNameFormatter.deadLetter(params.exchange);

    await this.connection.exchange({ name: params.exchange });
    await this.connection.exchange({ name: retryExchange });
    await this.connection.exchange({ name: deadLetterExchange });

    for (const subscriber of params.subscribers) {
      await this.addQueue(subscriber, params.exchange);
    }
  }

  private async addQueue(subscriber: DomainEventSubscriber<DomainEvent>, exchange: string) {
    const retryExchange = RabbitMQExchangeNameFormatter.retry(exchange);
    const deadLetterExchange = RabbitMQExchangeNameFormatter.deadLetter(exchange);

    const routingKeys = this.getRoutingKeysFor(subscriber);

    const queue = this.queueNameFormatter.format(subscriber);
    const deadLetterQueue = this.queueNameFormatter.formatDeadLetter(subscriber);
    const retryQueue = this.queueNameFormatter.formatRetry(subscriber);

    await this.connection.queue({ routingKeys, name: queue, exchange });
    await this.connection.queue({
      routingKeys: [queue],
      name: retryQueue,
      exchange: retryExchange,
      messageTtl: this.messageRetryTtl,
      deadLetterExchange: exchange,
      deadLetterQueue: queue
    });
    await this.connection.queue({ routingKeys: [queue], name: deadLetterQueue, exchange: deadLetterExchange });
  }

  private getRoutingKeysFor(subscriber: DomainEventSubscriber<DomainEvent>) {
    const routingKeys = subscriber.subscribedTo().map(event => event.EVENT_NAME);

    const queue = this.queueNameFormatter.format(subscriber);
    routingKeys.push(queue);

    return routingKeys;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/RabbitMQConsumer.ts`
```typescript
import { ConsumeMessage } from 'amqplib';
import { DomainEvent } from '../../../domain/DomainEvent';
import { DomainEventSubscriber } from '../../../domain/DomainEventSubscriber';
import { DomainEventDeserializer } from '../DomainEventDeserializer';
import { RabbitMqConnection } from './RabbitMqConnection';

export class RabbitMQConsumer {
  private subscriber: DomainEventSubscriber<DomainEvent>;
  private deserializer: DomainEventDeserializer;
  private connection: RabbitMqConnection;
  private maxRetries: Number;
  private queueName: string;
  private exchange: string;

  constructor(params: {
    subscriber: DomainEventSubscriber<DomainEvent>;
    deserializer: DomainEventDeserializer;
    connection: RabbitMqConnection;
    queueName: string;
    exchange: string;
    maxRetries: Number;
  }) {
    this.subscriber = params.subscriber;
    this.deserializer = params.deserializer;
    this.connection = params.connection;
    this.maxRetries = params.maxRetries;
    this.queueName = params.queueName;
    this.exchange = params.exchange;
  }

  async onMessage(message: ConsumeMessage) {
    const content = message.content.toString();
    const domainEvent = this.deserializer.deserialize(content);

    try {
      await this.subscriber.on(domainEvent);
    } catch (error) {
      await this.handleError(message);
    } finally {
      this.connection.ack(message);
    }
  }

  private async handleError(message: ConsumeMessage) {
    if (this.hasBeenRedeliveredTooMuch(message)) {
      await this.deadLetter(message);
    } else {
      await this.retry(message);
    }
  }

  private async retry(message: ConsumeMessage) {
    await this.connection.retry(message, this.queueName, this.exchange);
  }

  private async deadLetter(message: ConsumeMessage) {
    await this.connection.deadLetter(message, this.queueName, this.exchange);
  }

  private hasBeenRedeliveredTooMuch(message: ConsumeMessage) {
    if (this.hasBeenRedelivered(message)) {
      const count = parseInt(message.properties.headers['redelivery_count']);
      return count >= this.maxRetries;
    }
    return false;
  }

  private hasBeenRedelivered(message: ConsumeMessage) {
    return message.properties.headers['redelivery_count'] !== undefined;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/RabbitMQConsumerFactory.ts`
```typescript
import { DomainEvent } from '../../../domain/DomainEvent';
import { DomainEventSubscriber } from '../../../domain/DomainEventSubscriber';
import { DomainEventDeserializer } from '../DomainEventDeserializer';
import { RabbitMqConnection } from './RabbitMqConnection';
import { RabbitMQConsumer } from './RabbitMQConsumer';

export class RabbitMQConsumerFactory {
  constructor(
    private deserializer: DomainEventDeserializer,
    private connection: RabbitMqConnection,
    private maxRetries: Number
  ) {}

  build(subscriber: DomainEventSubscriber<DomainEvent>, exchange: string, queueName: string) {
    return new RabbitMQConsumer({
      subscriber,
      deserializer: this.deserializer,
      connection: this.connection,
      queueName,
      exchange,
      maxRetries: this.maxRetries
    });
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/RabbitMQExchangeNameFormatter.ts`
```typescript
export class RabbitMQExchangeNameFormatter {
  public static retry(exchangeName: string): string {
    return `retry-${exchangeName}`;
  }

  public static deadLetter(exchangeName: string): string {
    return `dead_letter-${exchangeName}`;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/RabbitMQqueueFormatter.ts`
```typescript
import { DomainEvent } from '../../../domain/DomainEvent';
import { DomainEventSubscriber } from '../../../domain/DomainEventSubscriber';

export class RabbitMQqueueFormatter {
  constructor(private moduleName: string) {}

  format(subscriber: DomainEventSubscriber<DomainEvent>) {
    const value = subscriber.constructor.name;
    const name = value
      .split(/(?=[A-Z])/)
      .join('_')
      .toLowerCase();
    return `${this.moduleName}.${name}`;
  }

  formatRetry(subscriber: DomainEventSubscriber<DomainEvent>) {
    const name = this.format(subscriber);
    return `retry.${name}`;
  }

  formatDeadLetter(subscriber: DomainEventSubscriber<DomainEvent>) {
    const name = this.format(subscriber);
    return `dead_letter.${name}`;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/RabbitMqConnection.ts`
```typescript
import amqplib, { ConsumeMessage } from 'amqplib';
import { ConnectionSettings } from './ConnectionSettings';
import { RabbitMQExchangeNameFormatter } from './RabbitMQExchangeNameFormatter';

export class RabbitMqConnection {
  private connectionSettings: ConnectionSettings;
  private channel?: amqplib.ConfirmChannel;
  private connection?: amqplib.Connection;

  constructor(params: { connectionSettings: ConnectionSettings }) {
    this.connectionSettings = params.connectionSettings;
  }

  async connect() {
    this.connection = await this.amqpConnect();
    this.channel = await this.amqpChannel();
  }

  async exchange(params: { name: string }) {
    return await this.channel?.assertExchange(params.name, 'topic', { durable: true });
  }

  async queue(params: {
    exchange: string;
    name: string;
    routingKeys: string[];
    deadLetterExchange?: string;
    deadLetterQueue?: string;
    messageTtl?: Number;
  }) {
    const durable = true;
    const exclusive = false;
    const autoDelete = false;
    const args = this.getQueueArguments(params);

    await this.channel?.assertQueue(params.name, {
      exclusive,
      durable,
      autoDelete,
      arguments: args
    });
    for (const routingKey of params.routingKeys) {
      await this.channel!.bindQueue(params.name, params.exchange, routingKey);
    }
  }

  private getQueueArguments(params: {
    exchange: string;
    name: string;
    routingKeys: string[];
    deadLetterExchange?: string;
    deadLetterQueue?: string;
    messageTtl?: Number;
  }) {
    let args: any = {};
    if (params.deadLetterExchange) {
      args = { ...args, 'x-dead-letter-exchange': params.deadLetterExchange };
    }
    if (params.deadLetterQueue) {
      args = { ...args, 'x-dead-letter-routing-key': params.deadLetterQueue };
    }
    if (params.messageTtl) {
      args = { ...args, 'x-message-ttl': params.messageTtl };
    }

    return args;
  }

  async deleteQueue(queue: string) {
    return await this.channel!.deleteQueue(queue);
  }

  private async amqpConnect() {
    const { hostname, port, secure } = this.connectionSettings.connection;
    const { username, password, vhost } = this.connectionSettings;
    const protocol = secure ? 'amqps' : 'amqp';

    const connection = await amqplib.connect({
      protocol,
      hostname,
      port,
      username,
      password,
      vhost
    });

    connection.on('error', (err: any) => {
      Promise.reject(err);
    });

    return connection;
  }

  private async amqpChannel(): Promise<amqplib.ConfirmChannel> {
    const channel = await this.connection!.createConfirmChannel();
    await channel.prefetch(1);

    return channel;
  }

  async publish(params: {
    exchange: string;
    routingKey: string;
    content: Buffer;
    options: { messageId: string; contentType: string; contentEncoding: string; priority?: number; headers?: any };
  }) {
    const { routingKey, content, options, exchange } = params;

    return new Promise((resolve: Function, reject: Function) => {
      this.channel!.publish(exchange, routingKey, content, options, (error: any) =>
        error ? reject(error) : resolve()
      );
    });
  }

  async close() {
    await this.channel?.close();
    return await this.connection?.close();
  }

  async consume(queue: string, onMessage: (message: ConsumeMessage) => {}) {
    await this.channel!.consume(queue, (message: ConsumeMessage | null) => {
      if (!message) {
        return;
      }
      onMessage(message);
    });
  }

  ack(message: ConsumeMessage) {
    this.channel!.ack(message);
  }

  async retry(message: ConsumeMessage, queue: string, exchange: string) {
    const retryExchange = RabbitMQExchangeNameFormatter.retry(exchange);
    const options = this.getMessageOptions(message);

    return await this.publish({ exchange: retryExchange, routingKey: queue, content: message.content, options });
  }

  async deadLetter(message: ConsumeMessage, queue: string, exchange: string) {
    const deadLetterExchange = RabbitMQExchangeNameFormatter.deadLetter(exchange);
    const options = this.getMessageOptions(message);

    return await this.publish({ exchange: deadLetterExchange, routingKey: queue, content: message.content, options });
  }

  private getMessageOptions(message: ConsumeMessage) {
    const { messageId, contentType, contentEncoding, priority } = message.properties;
    const options = {
      messageId,
      headers: this.incrementRedeliveryCount(message),
      contentType,
      contentEncoding,
      priority
    };
    return options;
  }

  private incrementRedeliveryCount(message: ConsumeMessage) {
    if (this.hasBeenRedelivered(message)) {
      const count = parseInt(message.properties.headers['redelivery_count']);
      message.properties.headers['redelivery_count'] = count + 1;
    } else {
      message.properties.headers['redelivery_count'] = 1;
    }

    return message.properties.headers;
  }

  private hasBeenRedelivered(message: ConsumeMessage) {
    return message.properties.headers['redelivery_count'] !== undefined;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/EventBus/RabbitMq/RabbitMqEventBus.ts`
```typescript
import { DomainEvent } from '../../../domain/DomainEvent';
import { EventBus } from '../../../domain/EventBus';
import { DomainEventDeserializer } from '../DomainEventDeserializer';
import { DomainEventFailoverPublisher } from '../DomainEventFailoverPublisher/DomainEventFailoverPublisher';
import { DomainEventJsonSerializer } from '../DomainEventJsonSerializer';
import { DomainEventSubscribers } from '../DomainEventSubscribers';
import { RabbitMqConnection } from './RabbitMqConnection';
import { RabbitMQConsumerFactory } from './RabbitMQConsumerFactory';
import { RabbitMQqueueFormatter } from './RabbitMQqueueFormatter';

export class RabbitMQEventBus implements EventBus {
  private failoverPublisher: DomainEventFailoverPublisher;
  private connection: RabbitMqConnection;
  private exchange: string;
  private queueNameFormatter: RabbitMQqueueFormatter;
  private maxRetries: Number;

  constructor(params: {
    failoverPublisher: DomainEventFailoverPublisher;
    connection: RabbitMqConnection;
    exchange: string;
    queueNameFormatter: RabbitMQqueueFormatter;
    maxRetries: Number;
  }) {
    const { failoverPublisher, connection, exchange } = params;
    this.failoverPublisher = failoverPublisher;
    this.connection = connection;
    this.exchange = exchange;
    this.queueNameFormatter = params.queueNameFormatter;
    this.maxRetries = params.maxRetries;
  }

  async addSubscribers(subscribers: DomainEventSubscribers): Promise<void> {
    const deserializer = DomainEventDeserializer.configure(subscribers);
    const consumerFactory = new RabbitMQConsumerFactory(deserializer, this.connection, this.maxRetries);

    for (const subscriber of subscribers.items) {
      const queueName = this.queueNameFormatter.format(subscriber);
      const rabbitMQConsumer = consumerFactory.build(subscriber, this.exchange, queueName);

      await this.connection.consume(queueName, rabbitMQConsumer.onMessage.bind(rabbitMQConsumer));
    }
  }

  async publish(events: Array<DomainEvent>): Promise<void> {
    for (const event of events) {
      try {
        const routingKey = event.eventName;
        const content = this.toBuffer(event);
        const options = this.options(event);

        await this.connection.publish({ exchange: this.exchange, routingKey, content, options });
      } catch (error: any) {
        await this.failoverPublisher.publish(event);
      }
    }
  }

  private options(event: DomainEvent) {
    return {
      messageId: event.eventId,
      contentType: 'application/json',
      contentEncoding: 'utf-8'
    };
  }

  private toBuffer(event: DomainEvent): Buffer {
    const eventPrimitives = DomainEventJsonSerializer.serialize(event);

    return Buffer.from(eventPrimitives);
  }
}
```

## File: `src/Contexts/Shared/infrastructure/QueryBus/InMemoryQueryBus.ts`
```typescript
import { Query } from '../../domain/Query';
import { Response } from '../../domain/Response';
import { QueryBus } from './../../domain/QueryBus';
import { QueryHandlers } from './QueryHandlers';

export class InMemoryQueryBus implements QueryBus {
  constructor(private queryHandlersInformation: QueryHandlers) {}

  async ask<R extends Response>(query: Query): Promise<R> {
    const handler = this.queryHandlersInformation.get(query);

    return (await handler.handle(query)) as Promise<R>;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/QueryBus/QueryHandlers.ts`
```typescript
import { Query } from '../../domain/Query';
import { QueryHandler } from '../../domain/QueryHandler';
import { Response } from '../../domain/Response';
import { QueryNotRegisteredError } from '../../domain/QueryNotRegisteredError';

export class QueryHandlers extends Map<Query, QueryHandler<Query, Response>> {
  constructor(queryHandlers: Array<QueryHandler<Query, Response>>) {
    super();
    queryHandlers.forEach(queryHandler => {
      this.set(queryHandler.subscribedTo(), queryHandler);
    });
  }

  public get(query: Query): QueryHandler<Query, Response> {
    const queryHandler = super.get(query.constructor);

    if (!queryHandler) {
      throw new QueryNotRegisteredError(query);
    }

    return queryHandler;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/elasticsearch/ElasticClientFactory.ts`
```typescript
import { Client as ElasticClient } from '@elastic/elasticsearch';
import { Nullable } from '../../../domain/Nullable';
import ElasticConfig from './ElasticConfig';

export class ElasticClientFactory {
  private static clients: { [key: string]: ElasticClient } = {};

  static async createClient(contextName: string, config: ElasticConfig): Promise<ElasticClient> {
    let client = ElasticClientFactory.getClient(contextName);

    if (!client) {
      client = await ElasticClientFactory.createAndConnectClient(config);

      await ElasticClientFactory.createIndexWithSettingsIfNotExists(client, config);

      ElasticClientFactory.registerClient(client, contextName);
    }

    return client;
  }

  private static getClient(contextName: string): Nullable<ElasticClient> {
    return ElasticClientFactory.clients[contextName];
  }

  private static async createAndConnectClient(config: ElasticConfig): Promise<ElasticClient> {
    const client = new ElasticClient({ node: config.url });

    return client;
  }

  private static registerClient(client: ElasticClient, contextName: string): void {
    ElasticClientFactory.clients[contextName] = client;
  }

  private static async createIndexWithSettingsIfNotExists(client: ElasticClient, config: ElasticConfig): Promise<void> {
    const { body: exist } = await client.indices.exists({ index: config.indexName });

    if (!exist) {
      await client.indices.create({
        index: config.indexName,
        body: config.indexConfig
      });
    }
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/elasticsearch/ElasticConfig.ts`
```typescript
type ElasticConfig = { url: string; indexName: string; indexConfig: any };

export default ElasticConfig;
```

## File: `src/Contexts/Shared/infrastructure/persistence/elasticsearch/ElasticCriteriaConverter.ts`
```typescript
import bodybuilder, { Bodybuilder } from 'bodybuilder';
import { Criteria } from '../../../domain/criteria/Criteria';
import { Filter } from '../../../domain/criteria/Filter';
import { Operator } from '../../../domain/criteria/FilterOperator';
import { Filters } from '../../../domain/criteria/Filters';

export enum TypeQueryEnum {
  TERMS = 'terms',
  MATCH_ALL = 'match_all',
  RANGE = 'range',
  WILDCARD = 'wildcard'
}

type QueryObject = { type: TypeQueryEnum; field: string; value: string | object };

interface TransformerFunction<T, K> {
  (value: T): K;
}

export class ElasticCriteriaConverter {
  private queryTransformers: Map<Operator, TransformerFunction<Filter, QueryObject>>;

  constructor() {
    this.queryTransformers = new Map<Operator, TransformerFunction<Filter, QueryObject>>([
      [Operator.EQUAL, this.termsQuery],
      [Operator.NOT_EQUAL, this.termsQuery],
      [Operator.GT, this.greaterThanQuery],
      [Operator.LT, this.lowerThanQuery],
      [Operator.CONTAINS, this.wildcardQuery],
      [Operator.NOT_CONTAINS, this.wildcardQuery]
    ]);
  }

  public convert(criteria: Criteria): Bodybuilder {
    let body = bodybuilder();

    body.from(criteria.offset || 0);
    body.size(criteria.limit || 1000);

    if (criteria.order.hasOrder()) {
      body.sort(criteria.order.orderBy.value, criteria.order.orderType.value);
    }

    if (criteria.hasFilters()) {
      body = this.generateQuery(body, criteria.filters);
    }

    return body;
  }

  protected generateQuery(body: Bodybuilder, filters: Filters): Bodybuilder {
    filters.filters.map(filter => {
      const { type, value, field } = this.queryForFilter(filter);

      if (filter.operator.isPositive()) {
        body.query(type, field, value);
      } else {
        body.notQuery(type, field, value);
      }
    });

    return body;
  }

  private queryForFilter(filter: Filter): QueryObject {
    const functionToApply = this.queryTransformers.get(filter.operator.value);

    if (!functionToApply) {
      throw Error(`Unexpected operator value ${filter.operator.value}`);
    }

    return functionToApply(filter);
  }

  private termsQuery(filter: Filter): QueryObject {
    return { type: TypeQueryEnum.TERMS, field: filter.field.value, value: [filter.value.value] };
  }

  private greaterThanQuery(filter: Filter): QueryObject {
    return { type: TypeQueryEnum.RANGE, field: filter.field.value, value: { gt: filter.value.value } };
  }

  private lowerThanQuery(filter: Filter): QueryObject {
    return { type: TypeQueryEnum.RANGE, field: filter.field.value, value: { lt: filter.value.value } };
  }

  private wildcardQuery(filter: Filter): QueryObject {
    return { type: TypeQueryEnum.WILDCARD, field: filter.field.value, value: `*${filter.value.value}*` };
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/elasticsearch/ElasticRepository.ts`
```typescript
import { Client as ElasticClient } from '@elastic/elasticsearch';
import { ResponseError } from '@elastic/elasticsearch/lib/errors';
import bodybuilder, { Bodybuilder } from 'bodybuilder';
import httpStatus from 'http-status';
import { AggregateRoot } from '../../../domain/AggregateRoot';
import { Criteria } from '../../../domain/criteria/Criteria';
import ElasticConfig from './ElasticConfig';
import { ElasticCriteriaConverter } from './ElasticCriteriaConverter';

interface SearchResult<T> {
  hits: SearchHitsMetadata<T>;
}

interface SearchHitsMetadata<T> {
  hits: SearchHit<T>[];
}

type SearchHit<T> = { _source: T };

export abstract class ElasticRepository<T extends AggregateRoot> {
  private criteriaConverter: ElasticCriteriaConverter;

  constructor(private _client: Promise<ElasticClient>, private config: ElasticConfig) {
    this.criteriaConverter = new ElasticCriteriaConverter();
  }

  protected indexName(): string {
    return this.config.indexName;
  }

  protected client(): Promise<ElasticClient> {
    return this._client;
  }

  protected async searchAllInElastic<D>(unserializer: (data: D) => T): Promise<T[]> {
    const body = bodybuilder().query('match_all');

    return this.searchInElasticWithBuilder(unserializer, body);
  }

  private async searchInElasticWithBuilder<D>(unserializer: (data: D) => T, body: Bodybuilder): Promise<T[]> {
    const client = await this.client();

    try {
      const response = await client.search<SearchResult<D>>({
        index: this.indexName(),
        body: body.build()
      });

      return response.body.hits.hits.map(hit => unserializer({ ...hit._source }));
    } catch (e) {
      if (this.isNotFoundError(e)) {
        return [];
      }
      throw e;
    }
  }

  private isNotFoundError(e: unknown) {
    return this.isResponseError(e) && e.meta.statusCode === httpStatus.NOT_FOUND;
  }

  private isResponseError(e: unknown): e is ResponseError {
    return e instanceof ResponseError;
  }

  protected async searchByCriteria(criteria: Criteria, unserializer: (data: any) => T): Promise<T[]> {
    const body = this.criteriaConverter.convert(criteria);

    return this.searchInElasticWithBuilder(unserializer, body);
  }

  protected async persist(id: string, aggregateRoot: T): Promise<void> {
    const client = await this.client();
    const document = { ...aggregateRoot.toPrimitives() };
    await client.index({ index: this.indexName(), id, body: document, refresh: 'wait_for' }); // wait_for wait for a refresh to make this operation visible to search
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/mongo/MongoClientFactory.ts`
```typescript
import { MongoClient } from 'mongodb';
import MongoConfig from './MongoConfig';

export class MongoClientFactory {
  private static clients: { [key: string]: MongoClient } = {};

  static async createClient(contextName: string, config: MongoConfig): Promise<MongoClient> {
    let client = MongoClientFactory.getClient(contextName);

    if (!client) {
      client = await MongoClientFactory.createAndConnectClient(config);

      MongoClientFactory.registerClient(client, contextName);
    }

    return client;
  }

  private static getClient(contextName: string): MongoClient | null {
    return MongoClientFactory.clients[contextName];
  }

  private static async createAndConnectClient(config: MongoConfig): Promise<MongoClient> {
    const client = new MongoClient(config.url, { ignoreUndefined: true });

    await client.connect();

    return client;
  }

  private static registerClient(client: MongoClient, contextName: string): void {
    MongoClientFactory.clients[contextName] = client;
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/mongo/MongoConfig.ts`
```typescript
interface MongoConfig {
  url: string;
}

export default MongoConfig;
```

## File: `src/Contexts/Shared/infrastructure/persistence/mongo/MongoRepository.ts`
```typescript
import { Collection, MongoClient } from 'mongodb';
import { MongoCriteriaConverter } from '../../../../Backoffice/Courses/infrastructure/persistence/MongoCriteriaConverter';
import { AggregateRoot } from '../../../domain/AggregateRoot';
import { Criteria } from '../../../domain/criteria/Criteria';

export abstract class MongoRepository<T extends AggregateRoot> {
  private criteriaConverter: MongoCriteriaConverter;

  constructor(private _client: Promise<MongoClient>) {
    this.criteriaConverter = new MongoCriteriaConverter();
  }

  protected abstract collectionName(): string;

  protected client(): Promise<MongoClient> {
    return this._client;
  }

  protected async collection(): Promise<Collection> {
    return (await this._client).db().collection(this.collectionName());
  }

  protected async persist(id: string, aggregateRoot: T): Promise<void> {
    const collection = await this.collection();

    const document = { ...aggregateRoot.toPrimitives(), _id: id, id: undefined };

    await collection.updateOne({ _id: id }, { $set: document }, { upsert: true });
  }

  protected async searchByCriteria<D>(criteria: Criteria): Promise<D[]> {
    const query = this.criteriaConverter.convert(criteria);

    const collection = await this.collection();

    return await collection.find<D>(query.filter, {}).sort(query.sort).skip(query.skip).limit(query.limit).toArray();
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/typeorm/TypeOrmClientFactory.ts`
```typescript
import { Connection, createConnection, getConnection } from 'typeorm';
import { TypeOrmConfig } from './TypeOrmConfig';

export class TypeOrmClientFactory {
  static async createClient(contextName: string, config: TypeOrmConfig): Promise<Connection> {
    try {
      const connection = await createConnection({
        name: contextName,
        type: 'postgres',
        host: config.host,
        port: config.port,
        username: config.username,
        password: config.password,
        database: config.database,
        entities: [__dirname + '/../../../../**/**/infrastructure/persistence/typeorm/*{.js,.ts}'],
        synchronize: true,
        logging: true
      });

      return connection;
    } catch (error) {
      return getConnection(contextName);
    }
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/typeorm/TypeOrmConfig.ts`
```typescript
export interface TypeOrmConfig {
  host: string;
  port: number;
  username: string;
  password: string;
  database: string;
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/typeorm/TypeOrmRepository.ts`
```typescript
import { Connection, EntitySchema, Repository } from 'typeorm';
import { AggregateRoot } from '../../../domain/AggregateRoot';

export abstract class TypeOrmRepository<T extends AggregateRoot> {
  constructor(private _client: Promise<Connection>) {}

  protected abstract entitySchema(): EntitySchema<T>;

  protected client(): Promise<Connection> {
    return this._client;
  }

  protected async repository(): Promise<Repository<T>> {
    return (await this._client).getRepository(this.entitySchema());
  }

  protected async persist(aggregateRoot: T): Promise<void> {
    const repository = await this.repository();
    await repository.save(aggregateRoot as any);
  }
}
```

## File: `src/Contexts/Shared/infrastructure/persistence/typeorm/ValueObjectTransformer.ts`
```typescript
import { NewableClass } from '../../../domain/NewableClass';
import { Primitives, ValueObject } from '../../../domain/value-object/ValueObject';

export const ValueObjectTransformer = <T extends Primitives>(ValueObject: NewableClass<ValueObject<any>>) => {
  return {
    to: (value: ValueObject<T>): T => value.value,
    from: (value: T): ValueObject<T> => new ValueObject(value)
  };
};
```

## File: `src/apps/backoffice/backend/BackofficeBackendApp.ts`
```typescript
import { EventBus } from '../../../Contexts/Shared/domain/EventBus';
import container from './dependency-injection';
import { DomainEventSubscribers } from '../../../Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { Server } from './server';
import { RabbitMqConnection } from '../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';

export class BackofficeBackendApp {
  server?: Server;

  async start() {
    const port = process.env.PORT || '3000';
    this.server = new Server(port);

    await this.configureEventBus();

    return this.server.listen();
  }

  get httpServer() {
    return this.server?.getHTTPServer();
  }

  async stop() {
    const rabbitMQConnection = container.get<RabbitMqConnection>('Backoffice.Shared.RabbitMQConnection');
    await rabbitMQConnection.close();
    return this.server?.stop();
  }

  private async configureEventBus() {
    const eventBus = container.get<EventBus>('Backoffice.Shared.domain.EventBus');
    const rabbitMQConnection = container.get<RabbitMqConnection>('Backoffice.Shared.RabbitMQConnection');
    await rabbitMQConnection.connect();

    eventBus.addSubscribers(DomainEventSubscribers.from(container));
  }
}
```

## File: `src/apps/backoffice/backend/server.ts`
```typescript
import bodyParser from 'body-parser';
import compress from 'compression';
import errorHandler from 'errorhandler';
import express, { Request, Response } from 'express';
import Router from 'express-promise-router';
import helmet from 'helmet';
import * as http from 'http';
import httpStatus from 'http-status';
import Logger from '../../../Contexts/Shared/domain/Logger';
import container from './dependency-injection';
import { registerRoutes } from './routes';
import cors from 'cors';

export class Server {
  private express: express.Express;
  readonly port: string;
  private logger: Logger;
  httpServer?: http.Server;

  constructor(port: string) {
    this.port = port;
    this.logger = container.get('Shared.Logger');
    this.express = express();
    this.express.use(bodyParser.json());
    this.express.use(bodyParser.urlencoded({ extended: true }));
    this.express.use(helmet.xssFilter());
    this.express.use(helmet.noSniff());
    this.express.use(helmet.hidePoweredBy());
    this.express.use(helmet.frameguard({ action: 'deny' }));
    this.express.use(compress());
    const router = Router();
    router.use(cors());
    router.use(errorHandler());
    this.express.use(router);
    registerRoutes(router);

    router.use((err: Error, req: Request, res: Response, next: Function) => {
      this.logger.error(err);
      res.status(httpStatus.INTERNAL_SERVER_ERROR).send(err.message);
    });
  }

  async listen(): Promise<void> {
    return new Promise(resolve => {
      this.httpServer = this.express.listen(this.port, () => {
        this.logger.info(
          `  Backoffice Backend App is running at http://localhost:${this.port} in ${this.express.get('env')} mode`
        );
        this.logger.info('  Press CTRL-C to stop\n');
        resolve();
      });
    });
  }

  getHTTPServer() {
    return this.httpServer;
  }

  async stop(): Promise<void> {
    return new Promise((resolve, reject) => {
      if (this.httpServer) {
        this.httpServer.close(error => {
          if (error) {
            return reject(error);
          }
          return resolve();
        });
      }

      return resolve();
    });
  }
}
```

## File: `src/apps/backoffice/backend/start.ts`
```typescript
import { BackofficeBackendApp } from './BackofficeBackendApp';

try {
  new BackofficeBackendApp().start().catch(handleError);
} catch (e) {
  handleError(e);
}

process.on('uncaughtException', err => {
  console.log('uncaughtException', err);
  process.exit(1);
});
function handleError(e: any) {
  console.log(e);
  process.exit(1);
}
```

## File: `src/apps/backoffice/backend/command/ConfigureRabbitMQCommand.ts`
```typescript
import { RabbitMQConfig } from '../../../../Contexts/Backoffice/Courses/infrastructure/RabbitMQ/RabbitMQConfigFactory';
import { DomainEventSubscribers } from '../../../../Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { RabbitMQConfigurer } from '../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQConfigurer';
import { RabbitMqConnection } from '../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';
import { RabbitMQqueueFormatter } from '../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter';
import container from '../dependency-injection';

export class ConfigureRabbitMQCommand {
  static async run() {
    const connection = container.get<RabbitMqConnection>('Backoffice.Shared.RabbitMQConnection');
    const nameFormatter = container.get<RabbitMQqueueFormatter>('Backoffice.Shared.RabbitMQQueueFormatter');
    const { exchangeSettings, retryTtl } = container.get<RabbitMQConfig>('Backoffice.Shared.RabbitMQConfig');

    await connection.connect();

    const configurer = new RabbitMQConfigurer(connection, nameFormatter, retryTtl);
    const subscribers = DomainEventSubscribers.from(container).items;

    await configurer.configure({ exchange: exchangeSettings.name, subscribers });
    await connection.close();
  }
}
```

## File: `src/apps/backoffice/backend/command/runConfigureRabbitMQCommand.ts`
```typescript
import { ConfigureRabbitMQCommand } from './ConfigureRabbitMQCommand';

ConfigureRabbitMQCommand.run()
  .then(() => {
    console.log('RabbitMQ Configuration success');
    process.exit(0);
  })
  .catch(error => {
    console.log('RabbitMQ Configuration fail', error);
    process.exit(1);
  });
```

## File: `src/apps/backoffice/backend/controllers/Controller.ts`
```typescript
import { Request, Response } from 'express';

export interface Controller {
  run(req: Request, res: Response): Promise<void>;
}
```

## File: `src/apps/backoffice/backend/controllers/CoursesGetController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';
import { BackofficeCoursesResponse } from '../../../../Contexts/Backoffice/Courses/application/BackofficeCoursesResponse';
import { SearchCoursesByCriteriaQuery } from '../../../../Contexts/Backoffice/Courses/application/SearchByCriteria/SearchCoursesByCriteriaQuery';
import { QueryBus } from '../../../../Contexts/Shared/domain/QueryBus';
import { Controller } from './Controller';

type FilterType = { value: string; operator: string; field: string };

export class CoursesGetController implements Controller {
  constructor(private readonly queryBus: QueryBus) {}

  async run(_req: Request, res: Response) {
    const { query: queryParams } = _req;
    const { filters, orderBy, order, limit, offset } = queryParams;

    const query = new SearchCoursesByCriteriaQuery(
      this.parseFilters(filters as Array<FilterType>),
      orderBy as string,
      order as string,
      limit ? Number(limit) : undefined,
      offset ? Number(offset) : undefined
    );

    const response = await this.queryBus.ask<BackofficeCoursesResponse>(query);

    res.status(httpStatus.OK).send(response.courses);
  }

  private parseFilters(params: Array<FilterType>): Array<Map<string, string>> {
    if (!params) {
      return new Array<Map<string, string>>();
    }

    return params.map(filter => {
      const field = filter.field;
      const value = filter.value;
      const operator = filter.operator;

      return new Map([
        ['field', field],
        ['operator', operator],
        ['value', value]
      ]);
    });
  }
}
```

## File: `src/apps/backoffice/backend/controllers/CoursesPostController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';
import { CreateCourseCommand } from '../../../../Contexts/Mooc/Courses/domain/CreateCourseCommand';
import { CommandBus } from '../../../../Contexts/Shared/domain/CommandBus';
import { Controller } from './Controller';

type CreateCourseRequest = {
  id: string;
  name: string;
  duration: string;
};

export class CoursesPostController implements Controller {
  constructor(private readonly commandBus: CommandBus) {}

  async run(req: Request<CreateCourseRequest>, res: Response) {
    await this.createCourse(req);
    res.status(httpStatus.OK).send();
  }

  private async createCourse(req: Request<CreateCourseRequest>) {
    const createCourseCommand = new CreateCourseCommand({
      id: req.body.id,
      name: req.body.name,
      duration: req.body.duration
    });

    await this.commandBus.dispatch(createCourseCommand);
  }
}
```

## File: `src/apps/backoffice/backend/controllers/StatusGetController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';
import { Controller } from './Controller';

export default class StatusGetController implements Controller {
  async run(req: Request, res: Response) {
    res.status(httpStatus.OK).send();
  }
}
```

## File: `src/apps/backoffice/backend/dependency-injection/application.yaml`
```yaml
imports:
  - { resource: ./Shared/application.yaml }
  - { resource: ./apps/application.yaml }
  - { resource: ./Courses/application.yaml }
```

## File: `src/apps/backoffice/backend/dependency-injection/application_dev.yaml`
```yaml
imports:
  - { resource: ./application.yaml }
```

## File: `src/apps/backoffice/backend/dependency-injection/application_production.yaml`
```yaml
imports:
  - { resource: ./application.yaml }
```

## File: `src/apps/backoffice/backend/dependency-injection/application_staging.yaml`
```yaml
imports:
  - { resource: ./application.yaml }
```

## File: `src/apps/backoffice/backend/dependency-injection/application_test.yaml`
```yaml
imports:
  - { resource: ./application.yaml }

services:
  Backoffice.EnvironmentArranger:
    class: ../../../../../tests/Contexts/Shared/infrastructure/mongo/MongoEnvironmentArranger
    arguments: ['@Backoffice.Shared.ConnectionManager']
```

## File: `src/apps/backoffice/backend/dependency-injection/index.ts`
```typescript
import { ContainerBuilder, YamlFileLoader } from 'node-dependency-injection';

const container = new ContainerBuilder();
const loader = new YamlFileLoader(container);
const env = process.env.NODE_ENV || 'dev';

loader.load(`${__dirname}/application_${env}.yaml`);

export default container;
```

## File: `src/apps/backoffice/backend/dependency-injection/Courses/application.yaml`
```yaml
services:
  Mooc.Courses.domain.CourseRepository:
    class: ../../../../../Contexts/Mooc/Courses/infrastructure/persistence/MongoCourseRepository
    arguments: ['@Backoffice.Shared.ConnectionManager']

  Mooc.Courses.application.CourseCreator:
    class: ../../../../../Contexts/Mooc/Courses/application/Create/CourseCreator
    arguments: ['@Mooc.Courses.domain.CourseRepository', '@Backoffice.Shared.domain.EventBus']

  Mooc.courses.CreateCourseCommandHandler:
    class: ../../../../../Contexts/Mooc/Courses/application/Create/CreateCourseCommandHandler
    arguments: ['@Mooc.Courses.application.CourseCreator']
    tags:
      - { name: 'commandHandler' }

  Backoffice.Courses.application.CoursesFinder:
    class: ../../../../../Contexts/Backoffice/Courses/application/SearchAll/CoursesFinder
    arguments: ['@Backoffice.Courses.domain.BackofficeCourseRepository']

  Backoffice.courses.SearchAllCoursesQueryHandler:
    class: ../../../../../Contexts/Backoffice/Courses/application/SearchAll/SearchAllCoursesQueryHandler
    arguments: ['@Backoffice.Courses.application.CoursesFinder']
    tags:
      - { name: 'queryHandler' }

  Backoffice.Courses.domain.BackofficeCourseRepository:
    class: ../../../../../Contexts/Backoffice/Courses/infrastructure/persistence/ElasticBackofficeCourseRepository
    arguments: ['@Backoffice.Shared.ElasticConnectionManager', '@Backoffice.Shared.ElasticConfig']

  Backoffice.Courses.application.BackofficeCourseCreator:
    class: ../../../../../Contexts/Backoffice/Courses/application/Create/BackofficeCourseCreator
    arguments: ['@Backoffice.Courses.domain.BackofficeCourseRepository']

  Backoffice.courses.CreateBackofficeCourseOnCourseCreated:
    class: ../../../../../Contexts/Backoffice/Courses/application/Create/CreateBackofficeCourseOnCourseCreated
    arguments: ['@Backoffice.Courses.application.BackofficeCourseCreator']
    tags:
      - { name: 'domainEventSubscriber' }

  Backoffice.courses.application.CoursesByCriteriaSearcher:
    class: ../../../../../Contexts/Backoffice/Courses/application/SearchByCriteria/CoursesByCriteriaSearcher
    arguments: ['@Backoffice.Courses.domain.BackofficeCourseRepository']

  Backoffice.courses.SearchCoursesByCriteriaQueryHandler:
    class: ../../../../../Contexts/Backoffice/Courses/application/SearchByCriteria/SearchCoursesByCriteriaQueryHandler
    arguments: ['@Backoffice.courses.application.CoursesByCriteriaSearcher']
    tags:
      - { name: 'queryHandler' }
```

## File: `src/apps/backoffice/backend/dependency-injection/Shared/application.yaml`
```yaml
services:
  Shared.Logger:
    class: ../../../../../Contexts/Shared/infrastructure/WinstonLogger
    arguments: []

  Backoffice.Shared.MongoConfig:
    factory:
      class: ../../../../../Contexts/Mooc/Shared/infrastructure/persistence/mongo/MongoConfigFactory
      method: 'createConfig'

  Backoffice.Shared.ConnectionManager:
    factory:
      class: ../../../../../Contexts/Shared/infrastructure/persistence/mongo/MongoClientFactory
      method: 'createClient'
    arguments: ['backoffice', '@Backoffice.Shared.MongoConfig']
  
  Backoffice.Shared.CommandHandlers:
    class: ../../../../../Contexts/Shared/infrastructure/CommandBus/CommandHandlers
    arguments: ['!tagged commandHandler']

  Backoffice.Shared.domain.CommandBus:
    class: ../../../../../Contexts/Shared/infrastructure/CommandBus/InMemoryCommandBus
    arguments: ['@Backoffice.Shared.CommandHandlers']

  Backoffice.Shared.RabbitMQConfig:
    factory:
      class: ../../../../../Contexts/Mooc/Shared/infrastructure/RabbitMQ/RabbitMQConfigFactory
      method: 'createConfig'

  Backoffice.Shared.domain.EventBus:
    factory:
      class: ../../../../../Contexts/Mooc/Shared/infrastructure/RabbitMQ/RabbitMQEventBusFactory
      method: 'create'
    arguments:
      [
        '@Backoffice.Shared.DomainEventFailoverPublisher',
        '@Backoffice.Shared.RabbitMQConnection',
        '@Backoffice.Shared.RabbitMQqueueFormatter',
        '@Backoffice.Shared.RabbitMQConfig'
      ]

  Backoffice.Shared.RabbitMQQueueFormatter:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter
    arguments: ['backoffice']

  Backoffice.Shared.RabbitMQConnection:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection
    arguments: ['@Backoffice.Shared.RabbitMQConfig']

  Backoffice.Shared.RabbitMQqueueFormatter:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter
    arguments: ['backoffice']

  Backoffice.Shared.DomainEventFailoverPublisher:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher
    arguments: ['@Backoffice.Shared.ConnectionManager']
  
  Backoffice.Shared.QueryHandlers:
    class: ../../../../../Contexts/Shared/infrastructure/QueryBus/QueryHandlers
    arguments: ['!tagged queryHandler']

  Backoffice.Shared.domain.QueryBus:
    class: ../../../../../Contexts/Shared/infrastructure/QueryBus/InMemoryQueryBus
    arguments: ['@Backoffice.Shared.QueryHandlers']

  Backoffice.Shared.ElasticConfig:
    factory:
      class: ../../../../../Contexts/Backoffice/Courses/infrastructure/persistence/BackofficeElasticConfigFactory
      method: 'createConfig'

  Backoffice.Shared.ElasticConnectionManager:
    factory:
      class: ../../../../../Contexts/Shared/infrastructure/persistence/elasticsearch/ElasticClientFactory
      method: 'createClient'
    arguments: ['backoffice', '@Backoffice.Shared.ElasticConfig']
```

## File: `src/apps/backoffice/backend/dependency-injection/apps/application.yaml`
```yaml
services:
  Apps.Backoffice.Backend.controllers.StatusGetController:
    class: ../../controllers/StatusGetController
    arguments: ['@Backoffice.Shared.domain.QueryBus']

  Apps.Backoffice.Backend.controllers.CoursesPostController:
    class: ../../controllers/CoursesPostController
    arguments: ['@Backoffice.Shared.domain.CommandBus']

  Apps.Backoffice.Backend.controllers.CoursesGetController:
    class: ../../controllers/CoursesGetController
    arguments: ['@Backoffice.Shared.domain.QueryBus']
```

## File: `src/apps/backoffice/backend/routes/courses.route.ts`
```typescript
import { Express } from 'express';
import container from '../dependency-injection';
import { CoursesPostController } from '../controllers/CoursesPostController';

export const register = (app: Express) => {
  const coursesPostController: CoursesPostController = container.get(
    'Apps.Backoffice.Backend.controllers.CoursesPostController'
  );
  const coursesGetController: CoursesPostController = container.get(
    'Apps.Backoffice.Backend.controllers.CoursesGetController'
  );

  app.post('/courses', coursesPostController.run.bind(coursesPostController));
  app.get('/courses', coursesGetController.run.bind(coursesGetController));
};
```

## File: `src/apps/backoffice/backend/routes/index.ts`
```typescript
import { Router } from 'express';
import glob from 'glob';

export function registerRoutes(router: Router) {
  const routes = glob.sync(__dirname + '/**/*.route.*');
  routes.map(route => register(route, router));
}

function register(routePath: string, app: Router) {
  const route = require(routePath);
  route.register(app);
}
```

## File: `src/apps/backoffice/backend/routes/status.route.ts`
```typescript
import { Express } from 'express';
import container from '../dependency-injection';
import StatusController from '../controllers/StatusGetController';

export const register = (app: Express) => {
  const controller: StatusController = container.get('Apps.Backoffice.Backend.controllers.StatusGetController');
  app.get('/status', controller.run.bind(controller));
};
```

## File: `src/apps/backoffice/frontend/.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## File: `src/apps/backoffice/frontend/README.md`
```markdown
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/brain/knowledge/docs_legacy/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/brain/knowledge/docs_legacy/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/brain/knowledge/docs_legacy/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
```

## File: `src/apps/backoffice/frontend/package.json`
```json
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.4",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "@types/jest": "^27.5.2",
    "@types/node": "^16.11.41",
    "@types/react": "^18.0.14",
    "@types/react-dom": "^18.0.5",
    "axios": "^0.27.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-helmet": "^6.1.0",
    "react-helmet-async": "^1.3.0",
    "react-router-dom": "^6.3.0",
    "react-scripts": "5.0.1",
    "typescript": "^4.7.3",
    "uuid": "^8.3.2",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "PORT=8032 react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@types/react-helmet": "^6.1.5",
    "@types/uuid": "^8.3.4",
    "autoprefixer": "^10.4.7",
    "postcss": "^8.4.14",
    "tailwindcss": "^3.1.3"
  }
}
```

## File: `src/apps/backoffice/frontend/postcss.config.js`
```javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

## File: `src/apps/backoffice/frontend/tailwind.config.js`
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## File: `src/apps/backoffice/frontend/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src"
  ]
}
```

## File: `src/apps/backoffice/frontend/public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>
```

## File: `src/apps/backoffice/frontend/public/manifest.json`
```json
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
```

## File: `src/apps/backoffice/frontend/public/robots.txt`
```
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:
```

## File: `src/apps/backoffice/frontend/src/App.css`
```css
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
```

## File: `src/apps/backoffice/frontend/src/App.test.tsx`
```tsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

## File: `src/apps/backoffice/frontend/src/App.tsx`
```tsx
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/header/Header';
import Footer from './components/footer/Footer';
import Home from './pages/Home';
import Courses from './pages/Courses';

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/courses" element={<Courses />} />
        </Routes>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
```

## File: `src/apps/backoffice/frontend/src/index.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
```

## File: `src/apps/backoffice/frontend/src/index.tsx`
```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { HelmetProvider } from 'react-helmet-async';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <HelmetProvider>
      <App />
    </HelmetProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

## File: `src/apps/backoffice/frontend/src/react-app-env.d.ts`
```typescript
/// <reference types="react-scripts" />
```

## File: `src/apps/backoffice/frontend/src/reportWebVitals.ts`
```typescript
import { ReportHandler } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
```

## File: `src/apps/backoffice/frontend/src/setupTests.ts`
```typescript
// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';
```

## File: `src/apps/backoffice/frontend/src/components/course-listing/CourseListing.tsx`
```tsx
import { Course } from '../../services/courses';
import Table from '../table/Table';
import TableBody from '../table/TableBody';
import TableCell from '../table/TableCell';
import TableHead from '../table/TableHead';
import TableHeader from '../table/TableHeader';
import TableRow from '../table/TableRow';
import FilterManager from './filter/FilterManager';
import ListingTitle from './ListingTitle';

function CourseListing({ courses, onFilter }: { courses: Course[]; onFilter: (courses: Course[]) => void }) {
  return (
    <div>
      <ListingTitle title="Cursos existentes" />
      <FilterManager onFilter={onFilter} />
      <Table className="text-left w-full border-collapse">
        <TableHeader>
          <TableRow>
            <TableHead name="Id" />
            <TableHead name="Nombre" />
            <TableHead name="Duración" />
          </TableRow>
        </TableHeader>
        <TableBody>
          {courses.map((course, index) => (
            <TableRow key={`row-${index}`}>
              <TableCell value={course.id} />
              <TableCell value={course.name} />
              <TableCell value={course.duration} />
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}

export default CourseListing;
```

## File: `src/apps/backoffice/frontend/src/components/course-listing/ListingTitle.tsx`
```tsx
import React from 'react';

function ListingTitle({ title }: { title: string }) {
  return <h3 className="font-sans text-gray-800 text-center text-3xl mb-10">{title}</h3>;
}

export default ListingTitle;
```

## File: `src/apps/backoffice/frontend/src/components/course-listing/filter/AddFilterButton.tsx`
```tsx
import React, { MouseEventHandler } from 'react';

function AddFilterButton({ onAdd }: { onAdd: MouseEventHandler<HTMLButtonElement> }) {
  return (
    <button
      className="md:w-1/6 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      id="add-field-button"
      onClick={onAdd}
    >
      Añadir filtro
    </button>
  );
}

export default AddFilterButton;
```

## File: `src/apps/backoffice/frontend/src/components/course-listing/filter/Filter.tsx`
```tsx
import React, { ChangeEvent } from 'react';

function Filter({
  onFieldSelected,
  onOperatorSelected,
  onValueChanged
}: {
  onFieldSelected: (event: ChangeEvent<HTMLSelectElement>) => void;
  onOperatorSelected: (event: ChangeEvent<HTMLSelectElement>) => void;
  onValueChanged: (event: ChangeEvent<HTMLInputElement>) => void;
}) {
  return (
    <div className="filter-row">
      <div className="inline-block relative w-64 mr-3">
        <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="field">
          Campo
        </label>
        <select
          id="field"
          className="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
          onChange={onFieldSelected}
        >
          <option value="id">Identificador</option>
          <option value="name">Nombre</option>
          <option value="duration">Duración</option>
        </select>
        <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
          <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
            <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"></path>
          </svg>
        </div>
      </div>
      <div className="inline-block relative w-64 mr-3">
        <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="operator">
          Operador
        </label>
        <select
          id="operator"
          className="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
          onChange={onOperatorSelected}
        >
          <option value="=">es exactamente igual</option>
          <option value="CONTAINS">contiene</option>
          <option value=">">es más grande que</option>
          <option value="<">es más pequeño que</option>
        </select>
        <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
          <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
            <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"></path>
          </svg>
        </div>
      </div>
      <div className="inline-block relative w-64 mr-3">
        <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="value">
          Valor
        </label>
        <input
          className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
          id="value"
          type="text"
          placeholder="Lo que sea..."
          onChange={onValueChanged}
        />
      </div>
    </div>
  );
}

export default Filter;
```

## File: `src/apps/backoffice/frontend/src/components/course-listing/filter/FilterButton.tsx`
```tsx
import React, { MouseEventHandler } from 'react';

function FilterButton({ onFilter }: { onFilter: MouseEventHandler<HTMLButtonElement> }) {
  return (
    <button
      className="m-2 md:w-1/6 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      id="filter-button"
      onClick={onFilter}
    >
      👉 Filtrar 👈
    </button>
  );
}

export default FilterButton;
```

## File: `src/apps/backoffice/frontend/src/components/course-listing/filter/FilterManager.tsx`
```tsx
import React, { useState } from 'react';
import { Course, searchCourses } from '../../../services/courses';
import AddFilterButton from './AddFilterButton';
import Filter from './Filter';
import FilterButton from './FilterButton';

export interface FilterState {
  field: string;
  operator: string;
  value: string;
}

function FilterManager({ onFilter }: { onFilter: (courses: Course[]) => void }) {
  const [filters, setFilters] = useState<FilterState[]>([]);

  return (
    <form
      id="courses-filters"
      name="filter-courses"
      className="text-left"
      action="#"
      onSubmit={e => e.preventDefault()}
    >
      {filters.map((filter, index) => (
        <Filter
          key={index}
          onFieldSelected={event => {
            filters[index] = {
              ...filters[index],
              field: event.target.options[event.target.options.selectedIndex].value
            };
            setFilters(filters);
          }}
          onOperatorSelected={event => {
            filters[index] = {
              ...filters[index],
              operator: event.target.options[event.target.options.selectedIndex].value
            };
            setFilters(filters);
          }}
          onValueChanged={event => {
            filters[index] = { ...filters[index], value: event.target.value };
            setFilters(filters);
          }}
        />
      ))}

      <AddFilterButton onAdd={() => setFilters([...filters, { field: 'id', operator: '=', value: '' }])} />
      <FilterButton
        onFilter={async () => {
          const courses = await searchCourses({ filters });
          onFilter(courses);
        }}
      />
    </form>
  );
}

export default FilterManager;
```

## File: `src/apps/backoffice/frontend/src/components/footer/Footer.tsx`
```tsx
import React from 'react';

function Footer() {
  return (
    <footer className="flex items-center justify-between flex-wrap bg-teal-900 p-5 mt-10">
      <div className="container mx-auto px-4">
          <p className="text-teal-200">
              🤙 CodelyTV - El mejor backoffice de la historia
          </p>
      </div>
    </footer>
  );
}

export default Footer;
```

## File: `src/apps/backoffice/frontend/src/components/form/Form.tsx`
```tsx
import React, { FormEventHandler } from 'react';
import type FormInput from './FormInput';
import FormSubmit from './FormSubmit';
import FormTitle from './FormTitle';

function Form({
  id,
  title,
  submitLabel,
  onSubmit,
  children,
  className
}: {
  id: string;
  title: string;
  submitLabel: string;
  onSubmit: FormEventHandler<HTMLFormElement>;
  children: React.ReactElement<typeof FormInput> | React.ReactElement<typeof FormInput>[];
  className: string;
}) {
  return (
    <form className={className} onSubmit={onSubmit} id={id}>
      <FormTitle title={title} />
      {[children].flat().map((child, index) => (
        <div key={`input-${index}`}>{child}</div>
      ))}
      <FormSubmit label={submitLabel} />
    </form>
  );
}

export default Form;
```

## File: `src/apps/backoffice/frontend/src/components/form/FormInput.tsx`
```tsx
import React from 'react';

function FormInput({
  id,
  label,
  name,
  value,
  placeholder,
  disabled,
  error,
  onChange
}: {
  id: string;
  label: string;
  name: string;
  value?: string | number | readonly string[];
  placeholder: string;
  disabled?: boolean
  error?: string;
  onChange?: React.ChangeEventHandler<HTMLInputElement>;
}) {
  return (
    <div>
      <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor={id}>
        {label}
      </label>

      <input
        className={`${error ? 'border border-red-500' : ''} appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500`}
        onChange={onChange}
        id={id}
        type="text"
        name={name}
        placeholder={placeholder}
        value={value}
        disabled={disabled}
      />

      {error && <p className="text-red-500 text-xs italic">{error}</p>}
    </div>
  );
}

export default FormInput;
```

## File: `src/apps/backoffice/frontend/src/components/form/FormSubmit.tsx`
```tsx
import React from 'react';

function FormSubmit({ label }: { label: string }) {
  return (
    <div>
      <button
        type="submit"
        className="md:w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        {label}
      </button>
    </div>
  );
}

export default FormSubmit;
```

## File: `src/apps/backoffice/frontend/src/components/form/FormTitle.tsx`
```tsx
import React from 'react';

function FormTitle({ title }: { title: string }) {
  return <h2 className="block uppercase tracking-wide text-gray-700 text-3xl font-bold mb-2">{title}</h2>;
}

export default FormTitle;
```

## File: `src/apps/backoffice/frontend/src/components/header/Header.tsx`
```tsx
import React from 'react';
import Navigation from './Navigation';

function Header() {
  return (
    <header className='text-left'>
        <Navigation />
    </header>
  );
}

export default Header;
```

## File: `src/apps/backoffice/frontend/src/components/header/Navigation.tsx`
```tsx
import React from 'react';
import logo from './logo.svg';
import { NavLink } from "react-router-dom";

function Navigation() {
  return (
    <nav className="flex items-center justify-between flex-wrap bg-teal-900 p-5">
        <div className="flex items-center flex-shrink-0 text-white mr-6">
            <NavLink to="/">
                <img src={logo} alt="" width="150px" />
            </NavLink>
        </div>
        <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
            <div className="text-sm lg:flex-grow">
                <NavLink to="#" className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Usuarios
                </NavLink>
                <NavLink to="/courses" className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Cursos
                </NavLink>
                <NavLink to="#" className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
                    Vídeos
                </NavLink>
            </div>
            <div>
                <NavLink to="#" className="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">
                    Entrar
                </NavLink>
            </div>
        </div>
    </nav>
  );
}

export default Navigation;
```

## File: `src/apps/backoffice/frontend/src/components/new-course-form/NewCourseForm.tsx`
```tsx
import React, { useState } from 'react';
import Form from '../form/Form';
import FormInput from '../form/FormInput';
import { v4, validate as isValidUUID } from 'uuid';
import { createCourse } from '../../services/courses';

interface State {
  id?: string;
  name?: string;
  duration?: string;
}

type Errors = Partial<Record<keyof State, string>>;

type NewCourse = Required<State>;

const isLength = ({ value, min, max }: { value: string, min: number, max: number }) =>
  value.length >= min && value.length <= max;

function NewCourseForm({ onSuccess, onError }: { onSuccess?: (event: NewCourse) => void; onError?: Function }) {
  const [state, setState] = useState<State>({ id: v4() });
  const [errors, setErrors] = useState<Errors>({});

  const validate = () => {
    const id = state.id && isValidUUID(state.id) ? '' : 'Identificador de curso inválido';
    const name = state.name && isLength({ value: state.name, min: 1, max: 30 }) ? '' : 'Nombre de curso inválido';
    const duration = state.duration && isLength({ value: state.duration, min: 4, max: 100 }) ? '' : 'Duración de curso inválida';

    setErrors({ id, name, duration });

    const hasNoErrors = Boolean(!id && !name && !duration);

    return hasNoErrors;
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (validate()) {
      try {
        await createCourse(state as NewCourse);

        setState({ id: v4(), name: '', duration: '' });
        setErrors({ });
        onSuccess && onSuccess(state as NewCourse);
      } catch (error) {
        onError && onError();
      }
    }
  };

  return (
    <Form
      className="w-full text-left"
      id="create-course"
      title="Crear curso"
      submitLabel="Crear curso!"
      onSubmit={handleSubmit}
    >
      <div className="flex flex-wrap mb-6 -mx-3">
        <div className="w-full md:w-full px-3 mb-6 md:mb-0">
          <FormInput
            id="grid-uuid"
            label="Identificador"
            name="id"
            placeholder="En formato UUID"
            value={state.id}
            onChange={event => setState({ ...state, id: event.target.value })}
            error={errors.id}
            disabled={true}
          />
        </div>
      </div>
      <div className="flex flex-wrap -mx-3 mb-6">
        <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
          <FormInput
            id="grid-first-name"
            label="Nombre"
            name="name"
            placeholder="DDD en TS"
            value={state.name}
            onChange={event => setState({ ...state, name: event.target.value })}
            error={errors.name}
          />
        </div>
        <div className="w-full md:w-1/2 px-3">
          <FormInput
            id="grid-duration"
            label="Duración (en inglés)"
            name="duration"
            placeholder="8 days"
            value={state.duration}
            onChange={event => setState({ ...state, duration: event.target.value })}
            error={errors.duration}
          />
        </div>
      </div>
    </Form>
  );
}

export default NewCourseForm;
```

## File: `src/apps/backoffice/frontend/src/components/page-container/PageAlert.tsx`
```tsx
import React from 'react';

function PageAlert({ message }: { message: string }) {
  return (
    <div className="flex items-center bg-blue-500 text-white text-sm font-bold px-4 py-3 mb-6" role="alert">
        <svg className="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
            <path d="M12.432 0c1.34 0 2.01.912 2.01 1.957 0 1.305-1.164 2.512-2.679 2.512-1.269 0-2.009-.75-1.974-1.99C9.789 1.436 10.67 0 12.432 0zM8.309 20c-1.058 0-1.833-.652-1.093-3.524l1.214-5.092c.211-.814.246-1.141 0-1.141-.317 0-1.689.562-2.502 1.117l-.528-.88c2.572-2.186 5.531-3.467 6.801-3.467 1.057 0 1.233 1.273.705 3.23l-1.391 5.352c-.246.945-.141 1.271.106 1.271.317 0 1.357-.392 2.379-1.207l.6.814C12.098 19.02 9.365 20 8.309 20z"/>
        </svg>
        <p>{message}</p>
    </div>
  );
}

export default PageAlert;
```

## File: `src/apps/backoffice/frontend/src/components/page-container/PageContainer.tsx`
```tsx
import React from 'react';
import PageAlert from './PageAlert';
import PageContent from './PageContent';
import PageTitle from './PageTitle';

function PageContainer({ title, alert, children }: { title: string, alert?: string, children: React.ReactNode }) {
  return (
    <div className="page-container columns-1">
        {alert && <PageAlert message={alert} /> }
        <div className="flex w-full place-content-center">
          <PageTitle title={title} />
        </div>
        <div className="flex w-full place-content-center">
          <PageContent>{children}</PageContent>
        </div>
    </div>
  );
}

export default PageContainer;
```

## File: `src/apps/backoffice/frontend/src/components/page-container/PageContent.tsx`
```tsx
import React from 'react';

function PageContent({ children }: { children: React.ReactNode }) {
  return (
    <div className='w-full'>{children}</div>
  );
}

export default PageContent;
```

## File: `src/apps/backoffice/frontend/src/components/page-container/PageSeparator.tsx`
```tsx
import React from 'react';

function PageSeparator() {
  return (
    <span>
      <div className="clearfix mb-10"></div>
      <hr className="mb-10"></hr>
    </span>
  );
}

export default PageSeparator;
```

## File: `src/apps/backoffice/frontend/src/components/page-container/PageTitle.tsx`
```tsx
import React from 'react';

function PageTitle({ title }: { title: string }) {
  return (
    <h1 className="font-sans text-gray-800 text-center text-5xl mb-10">{title}</h1>
  );
}

export default PageTitle;
```

## File: `src/apps/backoffice/frontend/src/components/table/Table.tsx`
```tsx
import React from 'react';
import TableBody from './TableBody';
import TableHeader from './TableHeader';

function Table({
  className,
  children
}: {
  className: string;
  children: React.ReactElement<typeof TableHeader | typeof TableBody>[];
}) {
  return <table className={`table-auto ${className}`}>{children}</table>;
}

export default Table;
```

## File: `src/apps/backoffice/frontend/src/components/table/TableBody.tsx`
```tsx
import React from 'react';
import TableCell from './TableCell';
import TableRow from './TableRow';

function TableBody({ children }: { children: React.ReactElement<typeof TableRow<typeof TableCell>>[] }) {
  return (
    <tbody>
      {children}
    </tbody>
  );
}

export default TableBody;
```

## File: `src/apps/backoffice/frontend/src/components/table/TableCell.tsx`
```tsx
import React from 'react';

function TableCell({ value }: { value: string }) {
  return <td>{value}</td>;
}

export default TableCell;
```

## File: `src/apps/backoffice/frontend/src/components/table/TableHead.tsx`
```tsx
import React from 'react';

function TableHead({ name }: { name: string }) {
  return (
    <th className="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
      {name}
    </th>
  );
}

export default TableHead;
```

## File: `src/apps/backoffice/frontend/src/components/table/TableHeader.tsx`
```tsx
import React from 'react';
import TableHead from './TableHead';
import TableRow from './TableRow';

function TableHeader({ children }: { children: React.ReactElement<typeof TableRow<typeof TableHead>> }) {
  return (
    <thead>
      {children}
    </thead>
  );
}

export default TableHeader;
```

## File: `src/apps/backoffice/frontend/src/components/table/TableRow.tsx`
```tsx
import React from 'react';
import TableCell from './TableCell';
import TableHead from './TableHead';

function TableRow<T extends typeof TableHead | typeof TableCell>({
  children
}: {
  children: React.ReactElement<T> | React.ReactElement<T>[];
}) {
  return <tr>{children}</tr>;
}

export default TableRow;
```

## File: `src/apps/backoffice/frontend/src/components/table/TableTitle.tsx`
```tsx
import React from 'react';

function TableTitle({ title }: { title: string }) {
  return <h3 className="font-sans text-gray-800 text-center text-3xl mb-10">{title}</h3>;
}

export default TableTitle;
```

## File: `src/apps/backoffice/frontend/src/pages/Courses.tsx`
```tsx
import { useEffect, useState } from 'react';
import { Helmet } from 'react-helmet';
import CourseListing from '../components/course-listing/CourseListing';
import NewCourseForm from '../components/new-course-form/NewCourseForm';
import PageContainer from '../components/page-container/PageContainer';
import PageSeparator from '../components/page-container/PageSeparator';
import { Course, getAllCourses } from '../services/courses';

function Courses() {
  const [alert, setAlert] = useState('');
  const [courses, setCourses] = useState<Course[]>([]);

  const handleSuccess = (course: Course) => {
    setCourses([...courses, { ...course }]);
    setAlert(`Felicidades, el curso ${course.id} ha sido creado correctamente!`);
  };

  useEffect(() => {
    const fetchData = async () => {
      const courses = await getAllCourses();
      setCourses(courses);
    };

    fetchData();
  }, []);

  return (
    <div className="container mx-auto px-4 p-5">
      <Helmet>
        <title>CodelyTV | Cursos</title>
      </Helmet>

      <PageContainer title="Cursos" alert={alert}>
        <NewCourseForm
          onSuccess={handleSuccess}
          onError={() => setAlert('Lo siento, ha ocurrido un error al crear el curso')}
        />

        <PageSeparator />

        <CourseListing courses={courses} onFilter={courses => setCourses(courses)} />
      </PageContainer>
    </div>
  );
}

export default Courses;
```

## File: `src/apps/backoffice/frontend/src/pages/Home.tsx`
```tsx
import React from 'react';
import { Helmet } from 'react-helmet';
import PageContainer from '../components/page-container/PageContainer';

function Home() {
  return (
    <div className="container mx-auto px-4 p-5">
      <Helmet>
        <title>CodelyTV | Home</title>
      </Helmet>

      <PageContainer title="HOME">
        ¡Bienvenidos a CodelyTV!
      </PageContainer>
    </div>
  );
}

export default Home;
```

## File: `src/apps/backoffice/frontend/src/services/courses.ts`
```typescript
export type Course = {
  id: string;
  name: string;
  duration: string;
};

type Query = {
  filters: Array<{ field: string; operator: string; value: string }>;
};

const post = async (url: string, body: Record<string, unknown>) => {
  await fetch(url, {
    method: 'POST',
    body: JSON.stringify({ ...body }),
    headers: { 'Content-Type': 'application/json' }
  });
};

const get = async (url: string) => {
  return await fetch(url, {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' }
  });
};

export const createCourse = (course: Course) => post('http://localhost:3000/courses', course);

export const getAllCourses = async () => {
  const response = await get('http://localhost:3000/courses');
  return (await response.json()) as Course[];
};

export const searchCourses = async (query: Query) => {
  const filters = query.filters.map(
    (filter, index) =>
      `filters[${index}][field]=${filter.field}&filters[${index}][operator]=${filter.operator}&filters[${index}][value]=${filter.value}`
  );

  const params = filters.join('&');

  const response = await get(`http://localhost:3000/courses?${params}`);
  return (await response.json()) as Course[];
};
```

## File: `src/apps/mooc/backend/MoocBackendApp.ts`
```typescript
import { EventBus } from '../../../Contexts/Shared/domain/EventBus';
import container from './dependency-injection';
import { DomainEventSubscribers } from '../../../Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { Server } from './server';
import { RabbitMqConnection } from '../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';

export class MoocBackendApp {
  server?: Server;

  async start() {
    const port = process.env.PORT || '5001';
    this.server = new Server(port);

    await this.configureEventBus();

    return this.server.listen();
  }

  get httpServer() {
    return this.server?.getHTTPServer();
  }

  async stop() {
    const rabbitMQConnection = container.get<RabbitMqConnection>('Mooc.Shared.RabbitMQConnection');
    await rabbitMQConnection.close();
    return this.server?.stop();
  }

  private async configureEventBus() {
    const eventBus = container.get<EventBus>('Mooc.Shared.domain.EventBus');
    const rabbitMQConnection = container.get<RabbitMqConnection>('Mooc.Shared.RabbitMQConnection');
    await rabbitMQConnection.connect();

    eventBus.addSubscribers(DomainEventSubscribers.from(container));
  }
}
```

## File: `src/apps/mooc/backend/server.ts`
```typescript
import bodyParser from 'body-parser';
import compress from 'compression';
import errorHandler from 'errorhandler';
import express, { Request, Response } from 'express';
import Router from 'express-promise-router';
import helmet from 'helmet';
import * as http from 'http';
import httpStatus from 'http-status';
import { registerRoutes } from './routes';

export class Server {
  private express: express.Express;
  private port: string;
  private httpServer?: http.Server;

  constructor(port: string) {
    this.port = port;
    this.express = express();
    this.express.use(bodyParser.json());
    this.express.use(bodyParser.urlencoded({ extended: true }));
    this.express.use(helmet.xssFilter());
    this.express.use(helmet.noSniff());
    this.express.use(helmet.hidePoweredBy());
    this.express.use(helmet.frameguard({ action: 'deny' }));
    this.express.use(compress());
    const router = Router();
    router.use(errorHandler());
    this.express.use(router);

    registerRoutes(router);

    router.use((err: Error, req: Request, res: Response, next: Function) => {
      console.log(err);
      res.status(httpStatus.INTERNAL_SERVER_ERROR).send(err.message);
    });
  }

  async listen(): Promise<void> {
    return new Promise(resolve => {
      this.httpServer = this.express.listen(this.port, () => {
        console.log(
          `  Mock Backend App is running at http://localhost:${this.port} in ${this.express.get('env')} mode`
        );
        console.log('  Press CTRL-C to stop\n');
        resolve();
      });
    });
  }

  getHTTPServer() {
    return this.httpServer;
  }

  async stop(): Promise<void> {
    return new Promise((resolve, reject) => {
      if (this.httpServer) {
        this.httpServer.close(error => {
          if (error) {
            return reject(error);
          }
          return resolve();
        });
      }

      return resolve();
    });
  }
}
```

## File: `src/apps/mooc/backend/start.ts`
```typescript
import { MoocBackendApp } from './MoocBackendApp';

try {
  new MoocBackendApp().start();
} catch (e) {
  console.log(e);
  process.exit(1);
}

process.on('uncaughtException', err => {
  console.log('uncaughtException', err);
  process.exit(1);
});
```

## File: `src/apps/mooc/backend/command/ConfigureRabbitMQCommand.ts`
```typescript
import { RabbitMQConfig } from '../../../../Contexts/Mooc/Shared/infrastructure/RabbitMQ/RabbitMQConfigFactory';
import { DomainEventSubscribers } from '../../../../Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { RabbitMQConfigurer } from '../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQConfigurer';
import { RabbitMqConnection } from '../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';
import container from '../dependency-injection';

export class ConfigureRabbitMQCommand {
  static async run() {
    const connection = container.get<RabbitMqConnection>('Mooc.Shared.RabbitMQConnection');
    const { name: exchange } = container.get<RabbitMQConfig>('Mooc.Shared.RabbitMQConfig').exchangeSettings;
    await connection.connect();

    const configurer = container.get<RabbitMQConfigurer>('Mooc.Shared.RabbitMQConfigurer');
    const subscribers = DomainEventSubscribers.from(container).items;

    await configurer.configure({ exchange, subscribers });
    await connection.close();
  }
}
```

## File: `src/apps/mooc/backend/command/runConfigureRabbitMQCommand.ts`
```typescript
import { ConfigureRabbitMQCommand } from './ConfigureRabbitMQCommand';

ConfigureRabbitMQCommand.run()
  .then(() => {
    console.log('RabbitMQ Configuration success');
    process.exit(0);
  })
  .catch(error => {
    console.log('RabbitMQ Configuration fail', error);
    process.exit(1);
  });
```

## File: `src/apps/mooc/backend/controllers/Controller.ts`
```typescript
import { Request, Response } from 'express';

export interface Controller {
  run(req: Request, res: Response): Promise<void>;
}
```

## File: `src/apps/mooc/backend/controllers/CoursePutController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';
import { CreateCourseCommand } from '../../../../Contexts/Mooc/Courses/domain/CreateCourseCommand';
import { CommandBus } from '../../../../Contexts/Shared/domain/CommandBus';
import { Controller } from './Controller';

type CoursePutRequest = Request & {
  body: {
    id: string;
    name: string;
    duration: string;
  };
};
export class CoursePutController implements Controller {
  constructor(private commandBus: CommandBus) {}

  async run(req: CoursePutRequest, res: Response) {
    try {
      const { id, name, duration } = req.body;
      const createCourseCommand = new CreateCourseCommand({ id, name, duration });
      await this.commandBus.dispatch(createCourseCommand);

      res.status(httpStatus.CREATED).send();
    } catch (error) {
      res.status(httpStatus.INTERNAL_SERVER_ERROR).send();
    }
  }
}
```

## File: `src/apps/mooc/backend/controllers/CoursesCounterGetController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';
import { FindCoursesCounterQuery } from '../../../../Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterQuery';
import { FindCoursesCounterResponse } from '../../../../Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterResponse';
import { CoursesCounterNotExist } from '../../../../Contexts/Mooc/CoursesCounter/domain/CoursesCounterNotExist';
import { QueryBus } from '../../../../Contexts/Shared/domain/QueryBus';
import { Controller } from './Controller';

export class CoursesCounterGetController implements Controller {
  constructor(private queryBus: QueryBus) {}
  async run(req: Request, res: Response): Promise<void> {
    try {
      const query = new FindCoursesCounterQuery();
      const { total } = await this.queryBus.ask<FindCoursesCounterResponse>(query);

      res.json({ total });
    } catch (e) {
      if (e instanceof CoursesCounterNotExist) {
        res.sendStatus(httpStatus.NOT_FOUND);
      } else {
        res.sendStatus(httpStatus.INTERNAL_SERVER_ERROR);
      }
    }
  }
}
```

## File: `src/apps/mooc/backend/controllers/StatusGetController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';
import { Controller } from './Controller';

export default class StatusGetController implements Controller {
  async run(req: Request, res: Response) {
    res.status(httpStatus.OK).send();
  }
}
```

## File: `src/apps/mooc/backend/dependency-injection/application.yaml`
```yaml
imports:
  - { resource: ./apps/application.yaml }
  - { resource: ./Courses/application.yaml }
  - { resource: ./CoursesCounter/application.yaml }
  - { resource: ./Shared/application.yaml }
```

## File: `src/apps/mooc/backend/dependency-injection/application_dev.yaml`
```yaml
imports:
  - { resource: ./application.yaml }
```

## File: `src/apps/mooc/backend/dependency-injection/application_production.yaml`
```yaml
imports:
  - { resource: ./application.yaml }
```

## File: `src/apps/mooc/backend/dependency-injection/application_test.yaml`
```yaml
imports:
  - { resource: ./application.yaml }

services:
  Mooc.EnvironmentArranger:
    class: ../../../../../tests/Contexts/Shared/infrastructure/mongo/MongoEnvironmentArranger
    arguments: ['@Mooc.Shared.ConnectionManager']
```

## File: `src/apps/mooc/backend/dependency-injection/index.ts`
```typescript
import { ContainerBuilder, YamlFileLoader } from 'node-dependency-injection';

const container = new ContainerBuilder();
const loader = new YamlFileLoader(container);
const env = process.env.NODE_ENV || 'dev';

loader.load(`${__dirname}/application_${env}.yaml`);

export default container;
```

## File: `src/apps/mooc/backend/dependency-injection/Courses/application.yaml`
```yaml
services:
  Mooc.Courses.domain.CourseRepository:
    class: ../../../../../Contexts/Mooc/Courses/infrastructure/persistence/MongoCourseRepository
    arguments: ['@Mooc.Shared.ConnectionManager']

  Mooc.Courses.application.CourseCreator:
    class: ../../../../../Contexts/Mooc/Courses/application/CourseCreator
    arguments: ['@Mooc.Courses.domain.CourseRepository', '@Mooc.Shared.domain.EventBus']

  Mooc.courses.CreateCourseCommandHandler:
    class: ../../../../../Contexts/Mooc/Courses/application/Create/CreateCourseCommandHandler
    arguments: ['@Mooc.Courses.application.CourseCreator']
    tags:
      - { name: 'commandHandler' }
```

## File: `src/apps/mooc/backend/dependency-injection/CoursesCounter/application.yaml`
```yaml
services:
  Mooc.CoursesCounter.CoursesCounterRepository:
    class: ../../../../../Contexts/Mooc/CoursesCounter/infrastructure/persistence/mongo/MongoCoursesCounterRepository
    arguments: ['@Mooc.Shared.ConnectionManager']

  Mooc.CoursesCounter.CoursesCounterIncrementer:
    class: ../../../../../Contexts/Mooc/CoursesCounter/application/Increment/CoursesCounterIncrementer
    arguments: ['@Mooc.CoursesCounter.CoursesCounterRepository', '@Mooc.Shared.domain.EventBus']

  Mooc.CoursesCounter.IncrementCoursesCounterOnCourseCreated:
    class: ../../../../../Contexts/Mooc/CoursesCounter/application/Increment/IncrementCoursesCounterOnCourseCreated
    arguments: ['@Mooc.CoursesCounter.CoursesCounterIncrementer']
    tags:
      - { name: 'domainEventSubscriber' }

  Mooc.CoursesCounter.CoursesCounterFinder:
    class: ../../../../../Contexts/Mooc/CoursesCounter/application/Find/CoursesCounterFinder
    arguments: ['@Mooc.CoursesCounter.CoursesCounterRepository']

  Mooc.CoursesCounter.FindCoursesCounterQueryHandler:
    class: ../../../../../Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterQueryHandler
    arguments: ['@Mooc.CoursesCounter.CoursesCounterFinder']
    tags:
      - { name: 'queryHandler' }
```

## File: `src/apps/mooc/backend/dependency-injection/Shared/application.yaml`
```yaml
services:
  Mooc.Shared.MongoConfig:
    factory:
      class: ../../../../../Contexts/Mooc/Shared/infrastructure/persistence/mongo/MongoConfigFactory
      method: 'createConfig'

  Mooc.Shared.RabbitMQConfig:
    factory:
      class: ../../../../../Contexts/Mooc/Shared/infrastructure/RabbitMQ/RabbitMQConfigFactory
      method: 'createConfig'

  Mooc.Shared.domain.EventBus:
    factory:
      class: ../../../../../Contexts/Mooc/Shared/infrastructure/RabbitMQ/RabbitMQEventBusFactory
      method: 'create'
    arguments:
      [
        '@Mooc.Shared.DomainEventFailoverPublisher',
        '@Mooc.Shared.RabbitMQConnection',
        '@Mooc.Shared.RabbitMQqueueFormatter',
        '@Mooc.Shared.RabbitMQConfig'
      ]

  Mooc.Shared.ConnectionManager:
    factory:
      class: ../../../../../Contexts/Shared/infrastructure/persistence/mongo/MongoClientFactory
      method: 'createClient'
    arguments: ['mooc', '@Mooc.Shared.MongoConfig']

  Mooc.Shared.RabbitMQQueueFormatter:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter
    arguments: ['mooc']

  Mooc.Shared.RabbitMQConnection:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection
    arguments: ['@Mooc.Shared.RabbitMQConfig']

  Mooc.Shared.RabbitMQqueueFormatter:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter
    arguments: ['mooc']

  Mooc.Shared.RabbitMQConfigurer:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQConfigurer
    arguments: ["@Mooc.Shared.RabbitMQConnection", "@Mooc.Shared.RabbitMQQueueFormatter"]

  Mooc.Shared.DomainEventFailoverPublisher:
    class: ../../../../../Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher
    arguments: ['@Mooc.Shared.ConnectionManager']

  Mooc.Shared.CommandHandlers:
    class: ../../../../../Contexts/Shared/infrastructure/CommandBus/CommandHandlers
    arguments: ['!tagged commandHandler']

  Mooc.Shared.domain.CommandBus:
    class: ../../../../../Contexts/Shared/infrastructure/CommandBus/InMemoryCommandBus
    arguments: ['@Mooc.Shared.CommandHandlers']

  Mooc.Shared.QueryHandlers:
    class: ../../../../../Contexts/Shared/infrastructure/QueryBus/QueryHandlers
    arguments: ['!tagged queryHandler']

  Mooc.Shared.domain.QueryBus:
    class: ../../../../../Contexts/Shared/infrastructure/QueryBus/InMemoryQueryBus
    arguments: ['@Mooc.Shared.QueryHandlers']
```

## File: `src/apps/mooc/backend/dependency-injection/apps/application.yaml`
```yaml
services:
  Apps.mooc.controllers.StatusGetController:
    class: ../../controllers/StatusGetController
    arguments: []

  Apps.mooc.controllers.CoursePutController:
    class: ../../controllers/CoursePutController
    arguments: ['@Mooc.Shared.domain.CommandBus']

  Apps.mooc.controllers.CoursesCounterGetController:
    class: ../../controllers/CoursesCounterGetController
    arguments: ['@Mooc.Shared.domain.QueryBus']
```

## File: `src/apps/mooc/backend/routes/courses-counter.route.ts`
```typescript
import { Request, Response, Router } from 'express';
import container from '../dependency-injection';

export const register = (router: Router) => {
  const coursesCounterGetController = container.get('Apps.mooc.controllers.CoursesCounterGetController');
  router.get('/courses-counter', (req: Request, res: Response) => coursesCounterGetController.run(req, res));
};
```

## File: `src/apps/mooc/backend/routes/courses.route.ts`
```typescript
import { Router, Request, Response } from 'express';
import container from '../dependency-injection';
import { body } from 'express-validator';
import { validateReqSchema } from '.';

export const register = (router: Router) => {
  const reqSchema = [
    body('id').exists().isString(),
    body('name').exists().isString(),
    body('duration').exists().isString()
  ];

  const coursePutController = container.get('Apps.mooc.controllers.CoursePutController');
  router.put('/courses/:id', reqSchema, validateReqSchema, (req: Request, res: Response) =>
    coursePutController.run(req, res)
  );
};
```

## File: `src/apps/mooc/backend/routes/index.ts`
```typescript
import { Router, Request, Response } from 'express';
import glob from 'glob';
import { ValidationError, validationResult } from 'express-validator';
import httpStatus from 'http-status';

export function registerRoutes(router: Router) {
  const routes = glob.sync(__dirname + '/**/*.route.*');
  routes.map(route => register(route, router));
}

function register(routePath: string, router: Router) {
  const route = require(routePath);
  route.register(router);
}

export function validateReqSchema(req: Request, res: Response, next: Function) {
  const validationErrors = validationResult(req);
  if (validationErrors.isEmpty()) {
    return next();
  }
  const errors = validationErrors.array().map((err: ValidationError) => ({ [err.param]: err.msg }));

  return res.status(httpStatus.UNPROCESSABLE_ENTITY).json({
    errors
  });
}
```

## File: `src/apps/mooc/backend/routes/status.route.ts`
```typescript
import { Router, Request, Response } from 'express';
import container from '../dependency-injection';
import StatusController from '../controllers/StatusGetController';

export const register = (router: Router) => {
  const controller: StatusController = container.get('Apps.mooc.controllers.StatusGetController');
  router.get('/status', (req: Request, res: Response) => controller.run(req, res));
};
```

## File: `tests/Contexts/Backoffice/Courses/__mocks__/BackofficeCourseRepositoryMock.ts`
```typescript
import { BackofficeCourse } from "../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourse";
import { BackofficeCourseRepository } from "../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseRepository";
import { Criteria } from "../../../../../src/Contexts/Shared/domain/criteria/Criteria";

export class BackofficeCourseRepositoryMock implements BackofficeCourseRepository {
  private mockSearchAll = jest.fn();
  private mockSave = jest.fn();
  private mockMatching = jest.fn();
  private courses: Array<BackofficeCourse> = [];

  returnOnSearchAll(courses: Array<BackofficeCourse>) {
    this.courses = courses;
  }

  returnMatching(courses: Array<BackofficeCourse>) {
    this.courses = courses;
  }

  async searchAll(): Promise<BackofficeCourse[]> {
    this.mockSearchAll();
    return this.courses;
  }

  assertSearchAll() {
    expect(this.mockSearchAll).toHaveBeenCalled();
  }

  async save(course: BackofficeCourse): Promise<void> {
    this.mockSave(course);
  }

  assertSaveHasBeenCalledWith(course: BackofficeCourse) {
    expect(this.mockSave).toHaveBeenCalledWith(course);
  }

  async matching(criteria: Criteria): Promise<BackofficeCourse[]> {
    this.mockMatching(criteria);
    return this.courses;
  }

  assertMatchingHasBeenCalledWith() {
    expect(this.mockMatching).toHaveBeenCalled();
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/application/Create/BackofficeCourseCreator.test.ts`
```typescript
import { BackofficeCourseCreator } from '../../../../../../src/Contexts/Backoffice/Courses/application/Create/BackofficeCourseCreator';
import { BackofficeCourseMother } from '../../domain/BackofficeCourseMother';
import { BackofficeCourseRepositoryMock } from '../../__mocks__/BackofficeCourseRepositoryMock';

describe('BackofficeCourseCreator', () => {
  it('creates a backoffice course', async () => {
    const course = BackofficeCourseMother.random();

    const repository = new BackofficeCourseRepositoryMock();
    const applicationService = new BackofficeCourseCreator(repository);

    await applicationService.run(course.id.toString(), course.duration.toString(), course.name.toString());

    repository.assertSaveHasBeenCalledWith(course);
  });
});
```

## File: `tests/Contexts/Backoffice/Courses/application/SearchAll/SearchAllCoursesQueryHandler.test.ts`
```typescript
import { CoursesFinder } from '../../../../../../src/Contexts/Backoffice/Courses/application/SearchAll/CoursesFinder';
import { SearchAllCoursesQuery } from '../../../../../../src/Contexts/Backoffice/Courses/application/SearchAll/SearchAllCoursesQuery';
import { SearchAllCoursesQueryHandler } from '../../../../../../src/Contexts/Backoffice/Courses/application/SearchAll/SearchAllCoursesQueryHandler';
import { BackofficeCourseMother } from '../../domain/BackofficeCourseMother';
import { SearchAllCoursesResponseMother } from '../../domain/SearchAllCoursesResponseMother';
import { BackofficeCourseRepositoryMock } from '../../__mocks__/BackofficeCourseRepositoryMock';

describe('SearchAllCourses QueryHandler', () => {
  let repository: BackofficeCourseRepositoryMock;

  beforeEach(() => {
    repository = new BackofficeCourseRepositoryMock();
  });

  it('should find an existing courses counter', async () => {
    const courses = [BackofficeCourseMother.random(), BackofficeCourseMother.random(), BackofficeCourseMother.random()];
    repository.returnOnSearchAll(courses);

    const handler = new SearchAllCoursesQueryHandler(new CoursesFinder(repository));

    const query = new SearchAllCoursesQuery();
    const response = await handler.handle(query);

    repository.assertSearchAll();

    const expected = SearchAllCoursesResponseMother.create(courses);
    expect(expected).toEqual(response);
  });
});
```

## File: `tests/Contexts/Backoffice/Courses/application/SearchByCriteria/SearchCoursesByCriteriaQueryHandler.test.ts`
```typescript
import { CoursesByCriteriaSearcher } from '../../../../../../src/Contexts/Backoffice/Courses/application/SearchByCriteria/CoursesByCriteriaSearcher';
import { SearchCoursesByCriteriaQuery } from '../../../../../../src/Contexts/Backoffice/Courses/application/SearchByCriteria/SearchCoursesByCriteriaQuery';
import { SearchCoursesByCriteriaQueryHandler } from '../../../../../../src/Contexts/Backoffice/Courses/application/SearchByCriteria/SearchCoursesByCriteriaQueryHandler';
import { OrderTypes } from '../../../../../../src/Contexts/Shared/domain/criteria/OrderType';
import { BackofficeCourseMother } from '../../domain/BackofficeCourseMother';
import { SearchCoursesByCriteriaResponseMother } from '../../domain/SearchCoursesByCriteriaResponseMother';
import { BackofficeCourseRepositoryMock } from '../../__mocks__/BackofficeCourseRepositoryMock';

describe('SearchAllCourses QueryHandler', () => {
  let repository: BackofficeCourseRepositoryMock;

  beforeEach(() => {
    repository = new BackofficeCourseRepositoryMock();
  });

  it('should find courses filter by criteria', async () => {
    const courses = [BackofficeCourseMother.random(), BackofficeCourseMother.random(), BackofficeCourseMother.random()];
    repository.returnMatching(courses);

    const handler = new SearchCoursesByCriteriaQueryHandler(new CoursesByCriteriaSearcher(repository));

    const filterName: Map<string, string> = new Map([
      ['field', 'name'],
      ['operator', 'CONTAINS'],
      ['value', 'DDD']
    ]);
    const filterDuration: Map<string, string> = new Map([
      ['field', 'duration'],
      ['operator', 'CONTAINS'],
      ['value', 'minutes']
    ]);

    const filters: Array<Map<string, string>> = new Array(filterName, filterDuration);

    const query = new SearchCoursesByCriteriaQuery(filters);
    const response = await handler.handle(query);

    const expected = SearchCoursesByCriteriaResponseMother.create(courses);
    repository.assertMatchingHasBeenCalledWith();
    expect(expected).toEqual(response);
  });

  it('should find courses filter by criteria with order, limit and offset', async () => {
    const courses = [BackofficeCourseMother.random(), BackofficeCourseMother.random(), BackofficeCourseMother.random()];
    repository.returnMatching(courses);

    const handler = new SearchCoursesByCriteriaQueryHandler(new CoursesByCriteriaSearcher(repository));

    const filterName: Map<string, string> = new Map([
      ['field', 'name'],
      ['operator', 'CONTAINS'],
      ['value', 'DDD']
    ]);
    const filterDuration: Map<string, string> = new Map([
      ['field', 'duration'],
      ['operator', 'CONTAINS'],
      ['value', 'minutes']
    ]);

    const filters: Array<Map<string, string>> = new Array(filterName, filterDuration);
    const orderBy = 'name';
    const orderType = OrderTypes.ASC;

    const query = new SearchCoursesByCriteriaQuery(filters, orderBy, orderType, 10, 1);
    const response = await handler.handle(query);

    const expected = SearchCoursesByCriteriaResponseMother.create(courses);
    repository.assertMatchingHasBeenCalledWith();
    expect(expected).toEqual(response);
  });
});
```

## File: `tests/Contexts/Backoffice/Courses/domain/BackofficeCourseCriteriaMother.ts`
```typescript
import { Criteria } from '../../../../../src/Contexts/Shared/domain/criteria/Criteria';
import { Filter } from '../../../../../src/Contexts/Shared/domain/criteria/Filter';
import { FilterField } from '../../../../../src/Contexts/Shared/domain/criteria/FilterField';
import { FilterOperator, Operator } from '../../../../../src/Contexts/Shared/domain/criteria/FilterOperator';
import { Filters } from '../../../../../src/Contexts/Shared/domain/criteria/Filters';
import { FilterValue } from '../../../../../src/Contexts/Shared/domain/criteria/FilterValue';
import { Order } from '../../../../../src/Contexts/Shared/domain/criteria/Order';

export class BackofficeCourseCriteriaMother {
  static whithoutFilter(): Criteria {
    return new Criteria(new Filters([]), Order.fromValues());
  }

  static nameAndDurationContainsSortAscById(name: string, duration: string): Criteria {
    const filterFieldName = new FilterField('name');
    const filterFieldDuration = new FilterField('duration');
    const filterOperator = new FilterOperator(Operator.CONTAINS);
    const valueName = new FilterValue(name);
    const valueDuration = new FilterValue(duration);

    const nameFilter = new Filter(filterFieldName, filterOperator, valueName);
    const durationFilter = new Filter(filterFieldDuration, filterOperator, valueDuration);

    return new Criteria(new Filters([nameFilter, durationFilter]), Order.asc('id'));
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/domain/BackofficeCourseDurationMother.ts`
```typescript
import { BackofficeCourseDuration } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseDuration';
import { WordMother } from '../../../Shared/domain/WordMother';

export class BackofficeCourseDurationMother {
  static create(value: string): BackofficeCourseDuration {
    return new BackofficeCourseDuration(value);
  }

  static random(): BackofficeCourseDuration {
    return this.create(WordMother.random({ maxLength: 10 }));
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/domain/BackofficeCourseIdMother.ts`
```typescript
import { BackofficeCourseId } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseId';
import { UuidMother } from '../../../Shared/domain/UuidMother';

export class BackofficeCourseIdMother {
  static create(value: string): BackofficeCourseId {
    return new BackofficeCourseId(value);
  }

  static creator() {
    return () => BackofficeCourseIdMother.random();
  }

  static random(): BackofficeCourseId {
    return this.create(UuidMother.random());
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/domain/BackofficeCourseMother.ts`
```typescript
import { BackofficeCourse } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourse';
import { BackofficeCourseDuration } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseDuration';
import { BackofficeCourseId } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseId';
import { BackofficeCourseName } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseName';
import { BackofficeCourseDurationMother } from './BackofficeCourseDurationMother';
import { BackofficeCourseIdMother } from './BackofficeCourseIdMother';
import { BackofficeCourseNameMother } from './BackofficeCourseNameMother';

export class BackofficeCourseMother {
  static create(
    id: BackofficeCourseId,
    name: BackofficeCourseName,
    duration: BackofficeCourseDuration
  ): BackofficeCourse {
    return new BackofficeCourse(id, name, duration);
  }

  static withNameAndDuration(name: string, duration: string): BackofficeCourse {
    return this.create(
      BackofficeCourseIdMother.random(),
      BackofficeCourseNameMother.create(name),
      BackofficeCourseDurationMother.create(duration)
    );
  }

  static random(): BackofficeCourse {
    return this.create(
      BackofficeCourseIdMother.random(),
      BackofficeCourseNameMother.random(),
      BackofficeCourseDurationMother.random()
    );
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/domain/BackofficeCourseNameMother.ts`
```typescript
import { BackofficeCourseName } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseName';
import { WordMother } from '../../../Shared/domain/WordMother';

export class BackofficeCourseNameMother {
  static create(value: string): BackofficeCourseName {
    return new BackofficeCourseName(value);
  }

  static random(): BackofficeCourseName {
    return this.create(WordMother.random({ maxLength: 10 }));
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/domain/SearchAllCoursesResponseMother.ts`
```typescript
import { BackofficeCoursesResponse } from "../../../../../src/Contexts/Backoffice/Courses/application/BackofficeCoursesResponse";
import { BackofficeCourse } from "../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourse";

export class SearchAllCoursesResponseMother {
  static create(courses: Array<BackofficeCourse>) {
    return new BackofficeCoursesResponse(courses);
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/domain/SearchCoursesByCriteriaResponseMother.ts`
```typescript
import { BackofficeCoursesResponse } from '../../../../../src/Contexts/Backoffice/Courses/application/BackofficeCoursesResponse';
import { BackofficeCourse } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourse';

export class SearchCoursesByCriteriaResponseMother {
  static create(courses: Array<BackofficeCourse>) {
    return new BackofficeCoursesResponse(courses);
  }
}
```

## File: `tests/Contexts/Backoffice/Courses/infrastructure/BackofficeCourseRepository.test.ts`
```typescript
import container from '../../../../../src/apps/backoffice/backend/dependency-injection';
import { BackofficeCourse } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourse';
import { BackofficeCourseRepository } from '../../../../../src/Contexts/Backoffice/Courses/domain/BackofficeCourseRepository';
import { EnvironmentArranger } from '../../../Shared/infrastructure/arranger/EnvironmentArranger';
import { BackofficeCourseCriteriaMother } from '../domain/BackofficeCourseCriteriaMother';
import { BackofficeCourseMother } from '../domain/BackofficeCourseMother';

const repository: BackofficeCourseRepository = container.get('Backoffice.Courses.domain.BackofficeCourseRepository');
const environmentArranger: Promise<EnvironmentArranger> = container.get('Backoffice.EnvironmentArranger');

beforeEach(async () => {
  await (await environmentArranger).arrange();
});

afterEach(async () => {
  await (await environmentArranger).arrange();
});

afterAll(async () => {
  await (await environmentArranger).close();
});

describe('BackofficeCourseRepository', () => {
  describe('#save', () => {
    it('should be able to persist the same course twice', async () => {
      const course = BackofficeCourseMother.random();

      await repository.save(course);
      await repository.save(course);

      const persistedCourses = await repository.searchAll();

      expect(persistedCourses).toHaveLength(1);
      expect(persistedCourses).toEqual([course]);
    });
  });

  describe('#searchAll', () => {
    it('should return the existing courses', async () => {
      const courses = [BackofficeCourseMother.random(), BackofficeCourseMother.random()];

      await Promise.all(courses.map(async course => repository.save(course)));

      const expectedCourses = await repository.searchAll();

      expect(courses).toHaveLength(expectedCourses.length);
      expect(courses.sort(sort)).toEqual(expectedCourses.sort(sort));
    });
  });
});

describe('#searchByCriteria', () => {
  it('should return all courses', async () => {
    const courses = [
      BackofficeCourseMother.withNameAndDuration('DDD in Typescript', '8 days'),
      BackofficeCourseMother.withNameAndDuration('DDD in Golang', '3 days'),
      BackofficeCourseMother.random()
    ];

    await Promise.all(courses.map(async course => repository.save(course)));
    const result = await repository.matching(BackofficeCourseCriteriaMother.whithoutFilter());

    expect(result).toHaveLength(3);
  });

  it('should return courses using a criteria sorting by id', async () => {
    const courses = [
      BackofficeCourseMother.withNameAndDuration('DDD in Typescript', '8 days'),
      BackofficeCourseMother.withNameAndDuration('DDD in Golang', '3 days'),
      BackofficeCourseMother.random()
    ];
    await Promise.all(courses.map(async course => repository.save(course)));
    
    const result = await repository.matching(
      BackofficeCourseCriteriaMother.nameAndDurationContainsSortAscById('DDD', 'days')
    );

    const expectedCourses = courses.slice(0, 2);
    expect(result).toHaveLength(2);
    expect(expectedCourses.sort(sort)).toEqual(result);
  });
});

function sort(backofficeCourse1: BackofficeCourse, backofficeCourse2: BackofficeCourse): number {
  return backofficeCourse1?.id?.value.localeCompare(backofficeCourse2?.id?.value);
}
```

## File: `tests/Contexts/Mooc/Courses/__mocks__/CourseRepositoryMock.ts`
```typescript
import { Course } from '../../../../../src/Contexts/Mooc/Courses/domain/Course';
import { CourseRepository } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseRepository';

export class CourseRepositoryMock implements CourseRepository {
  private saveMock: jest.Mock;
  private searchAllMock: jest.Mock;
  private courses: Array<Course> = [];

  constructor() {
    this.saveMock = jest.fn();
    this.searchAllMock = jest.fn();
  }

  async save(course: Course): Promise<void> {
    this.saveMock(course);
  }

  assertSaveHaveBeenCalledWith(expected: Course): void {
    expect(this.saveMock).toHaveBeenCalledWith(expected);
  }

  returnOnSearchAll(courses: Array<Course>) {
    this.courses = courses;
  }

  assertSearchAll() {
    expect(this.searchAllMock).toHaveBeenCalled();
  }

  async searchAll(): Promise<Course[]> {
    this.searchAllMock();
    return this.courses;
  }

}
```

## File: `tests/Contexts/Mooc/Courses/application/CreateCourseCommandHandler.test.ts`
```typescript
import { CourseCreator } from '../../../../../src/Contexts/Mooc/Courses/application/CourseCreator';
import { CourseMother } from '../domain/CourseMother';
import { CourseNameLengthExceeded } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseNameLengthExceeded';
import { CourseRepositoryMock } from '../__mocks__/CourseRepositoryMock';
import EventBusMock from '../../Shared/domain/EventBusMock';
import { CourseCreatedDomainEventMother } from '../domain/CourseCreatedDomainEventMother';
import { CreateCourseCommandHandler } from '../../../../../src/Contexts/Mooc/Courses/application/CreateCourseCommandHandler';
import { CreateCourseCommandMother } from './CreateCourseCommandMother';

let repository: CourseRepositoryMock;
let creator: CourseCreator;
let eventBus: EventBusMock;
let handler: CreateCourseCommandHandler;

beforeEach(() => {
  repository = new CourseRepositoryMock();
  eventBus = new EventBusMock();
  creator = new CourseCreator(repository, eventBus);
  handler = new CreateCourseCommandHandler(creator);
});

describe('CreateCourseCommandHandler', () => {
  it('should create a valid course', async () => {
    const command = CreateCourseCommandMother.random();
    const course = CourseMother.from(command);
    const domainEvent = CourseCreatedDomainEventMother.fromCourse(course);

    await handler.handle(command);

    repository.assertSaveHaveBeenCalledWith(course);
    eventBus.assertLastPublishedEventIs(domainEvent);
  });

  it('should throw error if course name length is exceeded', async () => {
    expect(() => {
      const command = CreateCourseCommandMother.invalid();

      const course = CourseMother.from(command);

      handler.handle(command);;

      repository.assertSaveHaveBeenCalledWith(course);
    }).toThrow(CourseNameLengthExceeded);
  });
});
```

## File: `tests/Contexts/Mooc/Courses/application/CreateCourseCommandMother.ts`
```typescript
import { CourseDuration } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseDuration';
import { CourseName } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseName';
import { CreateCourseCommand } from '../../../../../src/Contexts/Mooc/Courses/domain/CreateCourseCommand';
import { CourseId } from '../../../../../src/Contexts/Mooc/Shared/domain/Courses/CourseId';
import { CourseIdMother } from '../../Shared/domain/Courses/CourseIdMother';
import { CourseDurationMother } from '../domain/CourseDurationMother';
import { CourseNameMother } from '../domain/CourseNameMother';

export class CreateCourseCommandMother {
  static create(id: CourseId, name: CourseName, duration: CourseDuration): CreateCourseCommand {
    return { id: id.value, name: name.value, duration: duration.value };
  }

  static random(): CreateCourseCommand {
    return this.create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
  }

  static invalid(): CreateCourseCommand {
    return {
      id: CourseIdMother.random().value,
      name: CourseNameMother.invalidName(),
      duration: CourseDurationMother.random().value
    };
  }
}
```

## File: `tests/Contexts/Mooc/Courses/application/Create/CreateCourseCommandHandler.test.ts`
```typescript
import { CourseCreator } from '../../../../../../src/Contexts/Mooc/Courses/application/Create/CourseCreator';
import { CourseMother } from '../../domain/CourseMother';
import { CourseNameLengthExceeded } from '../../../../../../src/Contexts/Mooc/Courses/domain/CourseNameLengthExceeded';
import { CourseRepositoryMock } from '../../__mocks__/CourseRepositoryMock';
import EventBusMock from '../../../Shared/domain/EventBusMock';
import { CourseCreatedDomainEventMother } from '../../domain/CourseCreatedDomainEventMother';
import { CreateCourseCommandHandler } from '../../../../../../src/Contexts/Mooc/Courses/application/Create/CreateCourseCommandHandler';
import { CreateCourseCommandMother } from './CreateCourseCommandMother';

let repository: CourseRepositoryMock;
let creator: CourseCreator;
let eventBus: EventBusMock;
let handler: CreateCourseCommandHandler;

beforeEach(() => {
  repository = new CourseRepositoryMock();
  eventBus = new EventBusMock();
  creator = new CourseCreator(repository, eventBus);
  handler = new CreateCourseCommandHandler(creator);
});

describe('CreateCourseCommandHandler', () => {
  it('should create a valid course', async () => {
    const command = CreateCourseCommandMother.random();
    const course = CourseMother.from(command);
    const domainEvent = CourseCreatedDomainEventMother.fromCourse(course);

    await handler.handle(command);

    repository.assertSaveHaveBeenCalledWith(course);
    eventBus.assertLastPublishedEventIs(domainEvent);
  });

  it('should throw error if course name length is exceeded', async () => {
    expect(() => {
      const command = CreateCourseCommandMother.invalid();

      const course = CourseMother.from(command);

      handler.handle(command);;

      repository.assertSaveHaveBeenCalledWith(course);
    }).toThrow(CourseNameLengthExceeded);
  });
});
```

## File: `tests/Contexts/Mooc/Courses/application/Create/CreateCourseCommandMother.ts`
```typescript
import { CourseDuration } from "../../../../../../src/Contexts/Mooc/Courses/domain/CourseDuration";
import { CourseName } from "../../../../../../src/Contexts/Mooc/Courses/domain/CourseName";
import { CreateCourseCommand } from "../../../../../../src/Contexts/Mooc/Courses/domain/CreateCourseCommand";
import { CourseId } from "../../../../../../src/Contexts/Mooc/Shared/domain/Courses/CourseId";
import { CourseIdMother } from "../../../Shared/domain/Courses/CourseIdMother";
import { CourseDurationMother } from "../../domain/CourseDurationMother";
import { CourseNameMother } from "../../domain/CourseNameMother";

export class CreateCourseCommandMother {
  static create(id: CourseId, name: CourseName, duration: CourseDuration): CreateCourseCommand {
    return { id: id.value, name: name.value, duration: duration.value };
  }

  static random(): CreateCourseCommand {
    return this.create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
  }

  static invalid(): CreateCourseCommand {
    return {
      id: CourseIdMother.random().value,
      name: CourseNameMother.invalidName(),
      duration: CourseDurationMother.random().value
    };
  }
}
```

## File: `tests/Contexts/Mooc/Courses/application/SearchAll/SearchAllCoursesQueryHandler.test.ts`
```typescript
import { CoursesFinder } from "../../../../../../src/Contexts/Mooc/Courses/application/SearchAll/CoursesFinder";
import { SearchAllCoursesQuery } from "../../../../../../src/Contexts/Mooc/Courses/application/SearchAll/SearchAllCoursesQuery";
import { SearchAllCoursesQueryHandler } from "../../../../../../src/Contexts/Mooc/Courses/application/SearchAll/SearchAllCoursesQueryHandler";
import { CourseMother } from "../../domain/CourseMother";
import { CourseRepositoryMock } from "../../__mocks__/CourseRepositoryMock";
import { SearchAllCoursesResponseMother } from "./SearchAllCoursesResponseMother";

describe('SearchAllCourses QueryHandler', () => {
  let repository: CourseRepositoryMock;

  beforeEach(() => {
    repository = new CourseRepositoryMock();
  });

  it('should find an existing courses', async () => {
    const courses = [CourseMother.random(), CourseMother.random(), CourseMother.random()];
    repository.returnOnSearchAll(courses);

    const handler = new SearchAllCoursesQueryHandler(new CoursesFinder(repository));

    const query = new SearchAllCoursesQuery();
    const response = await handler.handle(query);

    repository.assertSearchAll();

    const expected = SearchAllCoursesResponseMother.create(courses);
    expect(expected).toEqual(response);
  });
});
```

## File: `tests/Contexts/Mooc/Courses/application/SearchAll/SearchAllCoursesResponseMother.ts`
```typescript
import { CoursesResponse } from "../../../../../../src/Contexts/Mooc/Courses/application/SearchAll/CoursesResponse";
import { Course } from "../../../../../../src/Contexts/Mooc/Courses/domain/Course";

export class SearchAllCoursesResponseMother {
  static create(courses: Array<Course>) {
    return new CoursesResponse(courses);
  }
}
```

## File: `tests/Contexts/Mooc/Courses/domain/CourseCreatedDomainEventMother.ts`
```typescript
import { CourseCreatedDomainEvent } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseCreatedDomainEvent';
import { Course } from '../../../../../src/Contexts/Mooc/Courses/domain/Course';

export class CourseCreatedDomainEventMother {
  static create({
    aggregateId,
    eventId,
    duration,
    name,
    occurredOn
  }: {
    aggregateId: string;
    eventId?: string;
    duration: string;
    name: string;
    occurredOn?: Date;
  }): CourseCreatedDomainEvent {
    return new CourseCreatedDomainEvent({
      aggregateId,
      eventId,
      duration,
      name,
      occurredOn
    });
  }

  static fromCourse(course: Course): CourseCreatedDomainEvent {
    return new CourseCreatedDomainEvent({
      aggregateId: course.id.value,
      duration: course.duration.value,
      name: course.name.value
    });
  }
}
```

## File: `tests/Contexts/Mooc/Courses/domain/CourseDurationMother.ts`
```typescript
import { CourseDuration } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseDuration';
import { WordMother } from '../../../Shared/domain/WordMother';

export class CourseDurationMother {
  static create(value: string): CourseDuration {
    return new CourseDuration(value);
  }

  static random(): CourseDuration {
    return this.create(WordMother.random({ maxLength: 30 }));
  }
}
```

## File: `tests/Contexts/Mooc/Courses/domain/CourseMother.ts`
```typescript
import { Course } from '../../../../../src/Contexts/Mooc/Courses/domain/Course';
import { CourseDuration } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseDuration';
import { CourseName } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseName';
import { CreateCourseCommand } from '../../../../../src/Contexts/Mooc/Courses/domain/CreateCourseCommand';
import { CourseId } from '../../../../../src/Contexts/Mooc/Shared/domain/Courses/CourseId';
import { CourseIdMother } from '../../Shared/domain/Courses/CourseIdMother';
import { CourseDurationMother } from './CourseDurationMother';
import { CourseNameMother } from './CourseNameMother';

export class CourseMother {
  static create(id: CourseId, name: CourseName, duration: CourseDuration): Course {
    return new Course(id, name, duration);
  }

  static from(command: CreateCourseCommand): Course {
    return this.create(
      CourseIdMother.create(command.id),
      CourseNameMother.create(command.name),
      CourseDurationMother.create(command.duration)
    );
  }

  static random(): Course {
    return this.create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
  }
}
```

## File: `tests/Contexts/Mooc/Courses/domain/CourseNameMother.ts`
```typescript
import { CourseName } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseName';
import { WordMother } from '../../../Shared/domain/WordMother';

export class CourseNameMother {
  static create(value: string): CourseName {
    return new CourseName(value);
  }

  static random(): CourseName {
    return this.create(WordMother.random({ maxLength: 20 }));
  }

  static invalidName(): string {
    return "a".repeat(40);
  }
}
```

## File: `tests/Contexts/Mooc/Courses/infrastructure/persistence/CourseRepository.test.ts`
```typescript
import container from '../../../../../../src/apps/mooc/backend/dependency-injection';
import { CourseRepository } from '../../../../../../src/Contexts/Mooc/Courses/domain/CourseRepository';
import { EnvironmentArranger } from '../../../../Shared/infrastructure/arranger/EnvironmentArranger';
import { CourseMother } from '../../domain/CourseMother';

const repository: CourseRepository = container.get('Mooc.Courses.domain.CourseRepository');
const environmentArranger: Promise<EnvironmentArranger> = container.get('Mooc.EnvironmentArranger');

beforeEach(async () => {
  await (await environmentArranger).arrange();
});

afterAll(async () => {
  await (await environmentArranger).arrange();
  await (await environmentArranger).close();
});

describe('CourseRepository', () => {
  describe('#save', () => {
    it('should save a course', async () => {
      const course = CourseMother.random();

      await repository.save(course);
    });
  });
});
```

## File: `tests/Contexts/Mooc/CoursesCounter/__mocks__/CoursesCounterRepositoryMock.ts`
```typescript
import { CoursesCounterRepository } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterRepository';
import { CoursesCounter } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounter';
import { Nullable } from '../../../../../src/Contexts/Shared/domain/Nullable';

export class CoursesCounterRepositoryMock implements CoursesCounterRepository {
  private mockSave = jest.fn();
  private mockSearch = jest.fn();
  private coursesCounter: Nullable<CoursesCounter> = null;

  async search(): Promise<Nullable<CoursesCounter>> {
    this.mockSearch();
    return this.coursesCounter;
  }

  async save(counter: CoursesCounter): Promise<void> {
    this.mockSave(counter);
  }

  returnOnSearch(counter: CoursesCounter) {
    this.coursesCounter = counter;
  }

  assertSearch() {
    expect(this.mockSearch).toHaveBeenCalled();
  }

  assertNotSave() {
    expect(this.mockSave).toHaveBeenCalledTimes(0);
  }

  assertLastCoursesCounterSaved(counter: CoursesCounter) {
    const mock = this.mockSave.mock;
    const lastCoursesCounter = mock.calls[mock.calls.length - 1][0] as CoursesCounter;
    const { id: id1, ...counterPrimitives } = counter.toPrimitives();
    const { id: id2, ...lastSavedPrimitives } = lastCoursesCounter.toPrimitives();

    expect(lastCoursesCounter).toBeInstanceOf(CoursesCounter);
    expect(lastSavedPrimitives).toEqual(counterPrimitives);
  }
}
```

## File: `tests/Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterQueryHandler.test.ts`
```typescript
import { CoursesCounterFinder } from '../../../../../../src/Contexts/Mooc/CoursesCounter/application/Find/CoursesCounterFinder';
import { FindCoursesCounterQuery } from '../../../../../../src/Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterQuery';
import { FindCoursesCounterQueryHandler } from '../../../../../../src/Contexts/Mooc/CoursesCounter/application/Find/FindCoursesCounterQueryHandler';
import { CoursesCounterNotExist } from '../../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterNotExist';
import { CoursesCounterMother } from '../../domain/CoursesCounterMother';
import { CoursesCounterRepositoryMock } from '../../__mocks__/CoursesCounterRepositoryMock';

describe('FindCoursesCounterQueryHandler', () => {
  let repository: CoursesCounterRepositoryMock;

  beforeEach(() => {
    repository = new CoursesCounterRepositoryMock();
  });

  it('should find an existing courses counter', async () => {
    const counter = CoursesCounterMother.random();
    repository.returnOnSearch(counter);
    const finder = new CoursesCounterFinder(repository);
    const handler = new FindCoursesCounterQueryHandler(finder);

    const response = await handler.handle(new FindCoursesCounterQuery());

    repository.assertSearch();
    expect(counter.total.value).toEqual(response.total);
  });

  it('should throw an exception when courses counter does not exists', async () => {
    const finder = new CoursesCounterFinder(repository);
    const handler = new FindCoursesCounterQueryHandler(finder);

    await expect(handler.handle(new FindCoursesCounterQuery())).rejects.toBeInstanceOf(CoursesCounterNotExist);
  });
});
```

## File: `tests/Contexts/Mooc/CoursesCounter/application/Increment/CoursesCounterIncrementer.test.ts`
```typescript
import { CoursesCounterIncrementer } from '../../../../../../src/Contexts/Mooc/CoursesCounter/application/Increment/CoursesCounterIncrementer';
import { CoursesCounter } from '../../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounter';
import EventBusMock from '../../../Shared/domain/EventBusMock';
import { CourseIdMother } from '../../../Shared/domain/Courses/CourseIdMother';
import { CoursesCounterIncrementedDomainEventMother } from '../../domain/CoursesCounterIncrementedDomainEventMother';
import { CoursesCounterMother } from '../../domain/CoursesCounterMother';
import { CoursesCounterRepositoryMock } from '../../__mocks__/CoursesCounterRepositoryMock';

describe('CoursesCounter Incrementer', () => {
  let incrementer: CoursesCounterIncrementer;
  let eventBus: EventBusMock;
  let repository: CoursesCounterRepositoryMock;

  beforeEach(() => {
    eventBus = new EventBusMock();
    repository = new CoursesCounterRepositoryMock();
    incrementer = new CoursesCounterIncrementer(repository, eventBus);
  });

  it('should initialize a new counter', async () => {
    const courseId = CourseIdMother.random();
    const counter = CoursesCounterMother.withOne(courseId);

    await incrementer.run(courseId);

    repository.assertLastCoursesCounterSaved(counter);
  });

  it('should increment an existing counter', async () => {
    const existingCounter = CoursesCounterMother.random();
    repository.returnOnSearch(existingCounter);
    const courseId = CourseIdMother.random();
    const expected = CoursesCounter.fromPrimitives(existingCounter.toPrimitives());
    expected.increment(courseId);
    const expectedEvent = CoursesCounterIncrementedDomainEventMother.fromCourseCounter(expected);

    await incrementer.run(courseId);

    repository.assertLastCoursesCounterSaved(expected);
    eventBus.assertLastPublishedEventIs(expectedEvent);
  });

  it('should not increment an already incremented counter', async () => {
    const existingCounter = CoursesCounterMother.random();
    repository.returnOnSearch(existingCounter);
    const courseId = existingCounter.existingCourses[0];

    await incrementer.run(courseId);

    repository.assertNotSave();
  });
});
```

## File: `tests/Contexts/Mooc/CoursesCounter/domain/CoursesCounterIncrementedDomainEventMother.ts`
```typescript
import { CoursesCounter } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounter';
import { CoursesCounterIncrementedDomainEvent } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterIncrementedDomainEvent';
import { DomainEvent } from '../../../../../src/Contexts/Shared/domain/DomainEvent';
import { CoursesCounterMother } from './CoursesCounterMother';

export class CoursesCounterIncrementedDomainEventMother {
  static create(): DomainEvent {
    return CoursesCounterIncrementedDomainEventMother.fromCourseCounter(CoursesCounterMother.random());
  }

  static fromCourseCounter(counter: CoursesCounter): CoursesCounterIncrementedDomainEvent {
    return new CoursesCounterIncrementedDomainEvent({
      aggregateId: counter.id.value,
      total: counter.total.value
    });
  }
}
```

## File: `tests/Contexts/Mooc/CoursesCounter/domain/CoursesCounterMother.ts`
```typescript
import { CoursesCounter } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounter';
import { CoursesCounterId } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterId';
import { CoursesCounterTotal } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterTotal';
import { CourseIdMother } from '../../Shared/domain/Courses/CourseIdMother';
import { Repeater } from '../../../Shared/domain/Repeater';
import { CoursesCounterTotalMother } from './CoursesCounterTotalMother';
import { CourseId } from '../../../../../src/Contexts/Mooc/Shared/domain/Courses/CourseId';

export class CoursesCounterMother {
  static random() {
    const total = CoursesCounterTotalMother.random();
    return new CoursesCounter(
      CoursesCounterId.random(),
      total,
      Repeater.random(CourseIdMother.random.bind(CourseIdMother), total.value)
    );
  }

  static withOne(courseId: CourseId) {
    return new CoursesCounter(CoursesCounterId.random(), new CoursesCounterTotal(1), [courseId]);
  }
}
```

## File: `tests/Contexts/Mooc/CoursesCounter/domain/CoursesCounterTotalMother.ts`
```typescript
import { CoursesCounterTotal } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterTotal';
import { IntegerMother } from '../../../Shared/domain/IntegerMother';

export class CoursesCounterTotalMother {
  static random() {
    return new CoursesCounterTotal(IntegerMother.random());
  }
}
```

## File: `tests/Contexts/Mooc/CoursesCounter/infrastructure/CoursesCounterRepository.test.ts`
```typescript
import container from '../../../../../src/apps/mooc/backend/dependency-injection';
import { CoursesCounterRepository } from '../../../../../src/Contexts/Mooc/CoursesCounter/domain/CoursesCounterRepository';
import { EnvironmentArranger } from '../../../Shared/infrastructure/arranger/EnvironmentArranger';
import { CoursesCounterMother } from '../domain/CoursesCounterMother';

const environmentArranger: Promise<EnvironmentArranger> = container.get('Mooc.EnvironmentArranger');
const repository: CoursesCounterRepository = container.get('Mooc.CoursesCounter.CoursesCounterRepository');

beforeEach(async () => {
  await (await environmentArranger).arrange();
});

afterAll(async () => {
  await (await environmentArranger).arrange();
  await (await environmentArranger).close();
});

describe('CoursesCounterRepository', () => {
  describe('#save', () => {
    it('should save a courses counter', async () => {
      const course = CoursesCounterMother.random();

      await repository.save(course);
    });
  });

  describe('#search', () => {
    it('should return an existing course', async () => {
      const expectedCounter = CoursesCounterMother.random();
      await repository.save(expectedCounter);

      const counter = await repository.search();

      expect(expectedCounter).toEqual(counter);
    });

    it('should not return null if there is no courses counter', async () => {
      expect(await repository.search()).toBeFalsy();
    });
  });
});
```

## File: `tests/Contexts/Mooc/Shared/domain/EventBusMock.ts`
```typescript
import { DomainEvent } from '../../../../../src/Contexts/Shared/domain/DomainEvent';
import { DomainEventSubscribers } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { EventBus } from '../../../../../src/Contexts/Shared/domain/EventBus';

export default class EventBusMock implements EventBus {
  private publishSpy = jest.fn();

  async publish(events: DomainEvent[]) {
    this.publishSpy(events);
  }

  addSubscribers(subscribers: DomainEventSubscribers): void {}

  assertLastPublishedEventIs(expectedEvent: DomainEvent) {
    const publishSpyCalls = this.publishSpy.mock.calls;

    expect(publishSpyCalls.length).toBeGreaterThan(0);

    const lastPublishSpyCall = publishSpyCalls[publishSpyCalls.length - 1];
    const lastPublishedEvent = lastPublishSpyCall[0][0];

    const expected = this.getDataFromDomainEvent(expectedEvent);
    const published = this.getDataFromDomainEvent(lastPublishedEvent);

    expect(expected).toMatchObject(published);
  }

  private getDataFromDomainEvent(event: DomainEvent) {
    const { eventId, occurredOn, ...attributes } = event;

    return attributes;
  }
}
```

## File: `tests/Contexts/Mooc/Shared/domain/Courses/CourseIdMother.ts`
```typescript
import { CourseId } from '../../../../../../src/Contexts/Mooc/Shared/domain/Courses/CourseId';
import { UuidMother } from '../../../../Shared/domain/UuidMother';

export class CourseIdMother {
  static create(value: string): CourseId {
    return new CourseId(value);
  }
  static random(): CourseId {
    return this.create(UuidMother.random());
  }
}
```

## File: `tests/Contexts/Shared/domain/IntegerMother.ts`
```typescript
import { MotherCreator } from './MotherCreator';

export class IntegerMother {
  static random(max?: number): number {
    return MotherCreator.random().random.number(max);
  }
}
```

## File: `tests/Contexts/Shared/domain/MotherCreator.ts`
```typescript
import * as faker from 'faker';

export class MotherCreator {
  static random(): Faker.FakerStatic {
    return faker;
  }
}
```

## File: `tests/Contexts/Shared/domain/Repeater.ts`
```typescript
import { IntegerMother } from './IntegerMother';
export class Repeater {
  static random(callable: Function, iterations: number) {
    return Array(iterations || IntegerMother.random(20))
      .fill({})
      .map(() => callable());
  }
}
```

## File: `tests/Contexts/Shared/domain/UuidMother.ts`
```typescript
import { MotherCreator } from './MotherCreator';

export class UuidMother {
  static random(): string {
    return MotherCreator.random().datatype.uuid();
  }
}
```

## File: `tests/Contexts/Shared/domain/WordMother.ts`
```typescript
import { MotherCreator } from './MotherCreator';

export class WordMother {
  static random({ minLength = 1, maxLength }: { minLength?: number; maxLength: number }): string {
    return MotherCreator.random().lorem.word(Math.floor(Math.random() * (maxLength - minLength)) + minLength) || 'word';
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/MongoClientFactory.test.ts`
```typescript
import { MongoClientFactory } from '../../../../src/Contexts/Shared/infrastructure/persistence/mongo/MongoClientFactory';
import { MongoClient } from 'mongodb';

describe('MongoClientFactory', () => {
  const factory = MongoClientFactory;
  let client: MongoClient;

  beforeEach(async () => {
    client = await factory.createClient('test', { url: 'mongodb://localhost:27017/mooc-backend-test1' });
  });

  afterEach(async () => {
    await client.close();
  });

  it('creates a new client with the connection already established', () => {
    expect(client).toBeInstanceOf(MongoClient);
  });

  it('creates a new client if it does not exist a client with the given name', async () => {
    const newClient = await factory.createClient('test2', { url: 'mongodb://localhost:27017/mooc-backend-test2' });

    expect(newClient).not.toBe(client);

    await newClient.close();
  });

  it('returns a client if it already exists', async () => {
    const newClient = await factory.createClient('test', { url: 'mongodb://localhost:27017/mooc-backend-test3' });

    expect(newClient).toBe(client);

    await newClient.close();
  });
});
```

## File: `tests/Contexts/Shared/infrastructure/TypeOrmClientFactory.test.ts`
```typescript
import { Connection } from 'typeorm';
import { TypeOrmClientFactory } from '../../../../src/Contexts/Shared/infrastructure/persistence/typeorm/TypeOrmClientFactory';

describe('TypeOrmClientFactory', () => {
  const factory = TypeOrmClientFactory;
  let client: Connection;

  beforeEach(async () => {
    client = await factory.createClient('test', { host:"localhost", port: 5432, username: "codely", password:"codely",database: 'mooc-backend-dev' });
  });

  afterEach(async () => {
    await client.close();
  });

  it('creates a new client with the connection already established', () => {
    expect(client).toBeInstanceOf(Connection);
    expect(client.isConnected).toBe(true);
  });

  it('creates a new client if it does not exist a client with the given name', async () => {
    const newClient = await factory.createClient('test2', { host:"localhost", port: 5432, username: "codely", password:"codely",database: 'mooc-backend-dev' });

    expect(newClient).not.toBe(client);
    expect(newClient.isConnected).toBeTruthy();

    await newClient.close();
  });

  it('returns a client if it already exists', async () => {
    const newClient = await factory.createClient('test', { host:"localhost", port: 5432, username: "codely", password:"codely",database: 'mooc-backend-dev' });

    expect(newClient).toBe(client);
    expect(newClient.isConnected).toBeTruthy();
  });
});
```

## File: `tests/Contexts/Shared/infrastructure/CommandBus/InMemoryCommandBus.test.ts`
```typescript
import { CommandNotRegisteredError } from '../../../../../src/Contexts/Shared/domain/CommandNotRegisteredError';
import { CommandHandlers } from '../../../../../src/Contexts/Shared/infrastructure/CommandBus/CommandHandlers';
import { InMemoryCommandBus } from '../../../../../src/Contexts/Shared/infrastructure/CommandBus/InMemoryCommandBus';
import { CommandHandlerDummy } from './__mocks__/CommandHandlerDummy';
import { DummyCommand } from './__mocks__/DummyCommand';
import { UnhandledCommand } from './__mocks__/UnhandledCommand';

describe('InMemoryCommandBus', () => {
  it('throws an error if dispatches a command without handler', async () => {
    const unhandledCommand = new UnhandledCommand();
    const commandHandlers = new CommandHandlers([]);
    const commandBus = new InMemoryCommandBus(commandHandlers);

    await expect(commandBus.dispatch(unhandledCommand)).rejects.toBeInstanceOf(CommandNotRegisteredError);
  });

  it('accepts a command with handler', async () => {
    const dummyCommand = new DummyCommand();
    const commandHandlerDummy = new CommandHandlerDummy();
    const commandHandlers = new CommandHandlers([commandHandlerDummy]);
    const commandBus = new InMemoryCommandBus(commandHandlers);

    await commandBus.dispatch(dummyCommand);
  });
});
```

## File: `tests/Contexts/Shared/infrastructure/CommandBus/__mocks__/CommandHandlerDummy.ts`
```typescript
import { CommandHandler } from '../../../../../../src/Contexts/Shared/domain/CommandHandler';
import { DummyCommand } from './DummyCommand';

export class CommandHandlerDummy implements CommandHandler<DummyCommand> {
  subscribedTo(): DummyCommand {
    return DummyCommand;
  }

  async handle(command: DummyCommand): Promise<void> {}
}
```

## File: `tests/Contexts/Shared/infrastructure/CommandBus/__mocks__/DummyCommand.ts`
```typescript
import { Command } from '../../../../../../src/Contexts/Shared/domain/Command';

export class DummyCommand extends Command {
  static COMMAND_NAME = 'handled.command';
}
```

## File: `tests/Contexts/Shared/infrastructure/CommandBus/__mocks__/UnhandledCommand.ts`
```typescript
import { Command } from '../../../../../../src/Contexts/Shared/domain/Command';

export class UnhandledCommand extends Command {
  static COMMAND_NAME = 'unhandled.command';
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher.test.ts`
```typescript
import { DomainEventFailoverPublisher } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher';
import { MongoEnvironmentArranger } from '../mongo/MongoEnvironmentArranger';
import { DomainEventDeserializerMother } from './__mother__/DomainEventDeserializerMother';
import { RabbitMQMongoClientMother } from './__mother__/RabbitMQMongoClientMother';
import { DomainEventDummyMother } from './__mocks__/DomainEventDummy';

describe('DomainEventFailoverPublisher test', () => {
  let arranger: MongoEnvironmentArranger;
  const mongoClient = RabbitMQMongoClientMother.create();
  const deserializer = DomainEventDeserializerMother.create();

  beforeAll(async () => {
    arranger = new MongoEnvironmentArranger(mongoClient);
  });

  beforeEach(async () => {
    await arranger.arrange();
  });

  it('should save the published events', async () => {
    const eventBus = new DomainEventFailoverPublisher(mongoClient, deserializer);
    const event = DomainEventDummyMother.random();

    await eventBus.publish(event);

    expect(await eventBus.consume()).toEqual([event]);
  });
});
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/RabbitMQEventBus.test.ts`
```typescript
import { DomainEvent } from '../../../../../src/Contexts/Shared/domain/DomainEvent';
import { DomainEventDeserializer } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventDeserializer';
import { DomainEventFailoverPublisher } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher';
import { DomainEventSubscribers } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { RabbitMQConfigurer } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQConfigurer';
import { RabbitMqConnection } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';
import { RabbitMQConsumer } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQConsumer';
import { RabbitMQEventBus } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQEventBus';
import { RabbitMQqueueFormatter } from '../../../../../src/Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMQqueueFormatter';
import { CoursesCounterIncrementedDomainEventMother } from '../../../Mooc/CoursesCounter/domain/CoursesCounterIncrementedDomainEventMother';
import { MongoEnvironmentArranger } from '../mongo/MongoEnvironmentArranger';
import { DomainEventDummyMother } from './__mocks__/DomainEventDummy';
import { DomainEventSubscriberDummy } from './__mocks__/DomainEventSubscriberDummy';
import { DomainEventFailoverPublisherMother } from './__mother__/DomainEventFailoverPublisherMother';
import { RabbitMQConnectionMother } from './__mother__/RabbitMQConnectionMother';
import { RabbitMQMongoClientMother } from './__mother__/RabbitMQMongoClientMother';

describe('RabbitMQEventBus test', () => {
  const exchange = 'test_domain_events';
  let arranger: MongoEnvironmentArranger;
  const queueNameFormatter = new RabbitMQqueueFormatter('mooc');

  beforeAll(async () => {
    arranger = new MongoEnvironmentArranger(RabbitMQMongoClientMother.create());
  });

  beforeEach(async () => {
    await arranger.arrange();
  });

  afterAll(async () => {
    await arranger.close();
  });

  describe('unit', () => {
    it('should use the failover publisher if publish to RabbitMQ fails', async () => {
      const connection = RabbitMQConnectionMother.failOnPublish();
      const failoverPublisher = DomainEventFailoverPublisherMother.failOverDouble();
      const eventBus = new RabbitMQEventBus({
        failoverPublisher,
        connection,
        exchange,
        queueNameFormatter,
        maxRetries: 3
      });
      const event = CoursesCounterIncrementedDomainEventMother.create();

      await eventBus.publish([event]);

      failoverPublisher.assertEventHasBeenPublished(event);
    });
  });

  describe('integration', () => {
    let connection: RabbitMqConnection;
    let dummySubscriber: DomainEventSubscriberDummy;
    let configurer: RabbitMQConfigurer;
    let failoverPublisher: DomainEventFailoverPublisher;
    let subscribers: DomainEventSubscribers;

    beforeEach(async () => {
      connection = await RabbitMQConnectionMother.create();
      failoverPublisher = DomainEventFailoverPublisherMother.create();
      configurer = new RabbitMQConfigurer(connection, queueNameFormatter, 50);
      await arranger.arrange();
      dummySubscriber = new DomainEventSubscriberDummy();
      subscribers = new DomainEventSubscribers([dummySubscriber]);
    });

    afterEach(async () => {
      await cleanEnvironment();
      await connection.close();
    });

    it('should consume the events published to RabbitMQ', async () => {
      await configurer.configure({ exchange, subscribers: [dummySubscriber] });
      const eventBus = new RabbitMQEventBus({
        failoverPublisher,
        connection,
        exchange,
        queueNameFormatter,
        maxRetries: 3
      });
      await eventBus.addSubscribers(subscribers);
      const event = DomainEventDummyMother.random();

      await eventBus.publish([event]);

      await dummySubscriber.assertConsumedEvents([event]);
    });

    it('should retry failed domain events', async () => {
      dummySubscriber = DomainEventSubscriberDummy.failsFirstTime();
      subscribers = new DomainEventSubscribers([dummySubscriber]);
      await configurer.configure({ exchange, subscribers: [dummySubscriber] });
      const eventBus = new RabbitMQEventBus({
        failoverPublisher,
        connection,
        exchange,
        queueNameFormatter,
        maxRetries: 3
      });
      await eventBus.addSubscribers(subscribers);
      const event = DomainEventDummyMother.random();

      await eventBus.publish([event]);

      await dummySubscriber.assertConsumedEvents([event]);
    });

    it('it should send events to dead letter after retry failed', async () => {
      dummySubscriber = DomainEventSubscriberDummy.alwaysFails();
      subscribers = new DomainEventSubscribers([dummySubscriber]);
      await configurer.configure({ exchange, subscribers: [dummySubscriber] });
      const eventBus = new RabbitMQEventBus({
        failoverPublisher,
        connection,
        exchange,
        queueNameFormatter,
        maxRetries: 3
      });
      await eventBus.addSubscribers(subscribers);
      const event = DomainEventDummyMother.random();

      await eventBus.publish([event]);

      await dummySubscriber.assertConsumedEvents([]);
      assertDeadLetter([event]);
    });

    async function cleanEnvironment() {
      await connection.deleteQueue(queueNameFormatter.format(dummySubscriber));
      await connection.deleteQueue(queueNameFormatter.formatRetry(dummySubscriber));
      await connection.deleteQueue(queueNameFormatter.formatDeadLetter(dummySubscriber));
    }


    async function assertDeadLetter(events: Array<DomainEvent>) {
      const deadLetterQueue = queueNameFormatter.formatDeadLetter(dummySubscriber);
      const deadLetterSubscriber = new DomainEventSubscriberDummy();
      const deadLetterSubscribers = new DomainEventSubscribers([dummySubscriber]);
      const deserializer = DomainEventDeserializer.configure(deadLetterSubscribers);
      const consumer = new RabbitMQConsumer({ subscriber: deadLetterSubscriber, deserializer, connection, maxRetries: 3, queueName: deadLetterQueue, exchange });
      await connection.consume(deadLetterQueue, consumer.onMessage.bind(consumer));

      await deadLetterSubscriber.assertConsumedEvents(events);
    }
  });
});
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mocks__/DomainEventDummy.ts`
```typescript
import { DomainEvent } from '../../../../../../src/Contexts/Shared/domain/DomainEvent';
import { UuidMother } from '../../../domain/UuidMother';

export class DomainEventDummy extends DomainEvent {
  static readonly EVENT_NAME = 'dummy';

  constructor(data: { aggregateId: string; eventId?: string; occurredOn?: Date }) {
    const { aggregateId, eventId, occurredOn } = data;
    super({ eventName: DomainEventDummy.EVENT_NAME, aggregateId, eventId, occurredOn });
  }

  toPrimitives() {
    return {};
  }

  static fromPrimitives(params: { aggregateId: string; attributes: {}; eventId: string; occurredOn: Date }) {
    const { aggregateId, eventId, occurredOn } = params;
    return new DomainEventDummy({
      aggregateId,
      eventId,
      occurredOn
    });
  }
}

export class DomainEventDummyMother {
  static random() {
    return new DomainEventDummy({
      aggregateId: UuidMother.random(),
      eventId: UuidMother.random(),
      occurredOn: new Date()
    });
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mocks__/DomainEventFailoverPublisherDouble.ts`
```typescript
import { DomainEvent } from '../../../../../../src/Contexts/Shared/domain/DomainEvent';
import { DomainEventFailoverPublisher } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher';
import { DomainEventDeserializerMother } from '../__mother__/DomainEventDeserializerMother';
import { RabbitMQMongoClientMother } from '../__mother__/RabbitMQMongoClientMother';

export class DomainEventFailoverPublisherDouble extends DomainEventFailoverPublisher {
  private publishMock: jest.Mock;
  constructor() {
    super(RabbitMQMongoClientMother.create(), DomainEventDeserializerMother.create());
    this.publishMock = jest.fn();
  }

  async publish(event: DomainEvent): Promise<void> {
    this.publishMock(event);
  }

  assertEventHasBeenPublished(event: DomainEvent) {
    expect(this.publishMock).toHaveBeenCalledWith(event);
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mocks__/DomainEventSubscriberDummy.ts`
```typescript
import { DomainEvent, DomainEventClass } from '../../../../../../src/Contexts/Shared/domain/DomainEvent';
import { DomainEventSubscriber } from '../../../../../../src/Contexts/Shared/domain/DomainEventSubscriber';
import { DomainEventDummy } from './DomainEventDummy';

export class DomainEventSubscriberDummy implements DomainEventSubscriber<DomainEventDummy> {
  static failsFirstTime() {
    return new DomainEventSubscriberDummy({ failsFirstTime: true });
  }

  static alwaysFails() {
    return new DomainEventSubscriberDummy({ alwaysFails: true });
  }

  private events: Array<DomainEvent>;
  private failsFirstTime = false;
  private alwaysFails = false;
  private alreadyFailed = false;

  constructor(params?: { failsFirstTime?: Boolean; alwaysFails?: Boolean }) {
    if (params?.failsFirstTime) {
      this.failsFirstTime = true;
    }
    if (params?.alwaysFails) {
      this.alwaysFails = true;
    }

    this.events = [];
  }

  subscribedTo(): DomainEventClass[] {
    return [DomainEventDummy];
  }

  async on(domainEvent: DomainEventDummy): Promise<void> {
    if (this.alwaysFails) {
      throw new Error();
    }

    if (!this.alreadyFailed && this.failsFirstTime) {
      this.alreadyFailed = true;
      throw new Error();
    }

    this.events.push(domainEvent);
  }

  async assertConsumedEvents(events: Array<DomainEvent>) {
    return new Promise((resolve: Function, reject: Function) => {
      setTimeout(() => {
        try {
          expect(this.events.length).toEqual(events.length);
          expect(this.events).toEqual(events);
          resolve();
        } catch (error: any) {
          reject(error);
        }
      }, 400);
    });
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mocks__/RabbitMQConnectionDouble.ts`
```typescript
import { RabbitMqConnection } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';

export class RabbitMQConnectionDouble extends RabbitMqConnection {

  async publish(params: any): Promise<boolean> {
    throw new Error();
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mother__/DomainEventDeserializerMother.ts`
```typescript
import { DomainEventDeserializer } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventDeserializer';
import { DomainEventSubscribers } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { DomainEventSubscriberDummy } from '../__mocks__/DomainEventSubscriberDummy';

export class DomainEventDeserializerMother {
  static create() {
    const dummySubscriber = new DomainEventSubscriberDummy();
    const subscribers = new DomainEventSubscribers([dummySubscriber]);
    return DomainEventDeserializer.configure(subscribers);
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mother__/DomainEventFailoverPublisherMother.ts`
```typescript
import { DomainEventFailoverPublisher } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventFailoverPublisher/DomainEventFailoverPublisher';
import { DomainEventFailoverPublisherDouble } from '../__mocks__/DomainEventFailoverPublisherDouble';
import { DomainEventDeserializerMother } from './DomainEventDeserializerMother';
import { RabbitMQMongoClientMother } from './RabbitMQMongoClientMother';


export class DomainEventFailoverPublisherMother {

  static create() {
    const mongoClient = RabbitMQMongoClientMother.create();
    return new DomainEventFailoverPublisher(mongoClient, DomainEventDeserializerMother.create());
  }

  static failOverDouble() {
    return new DomainEventFailoverPublisherDouble();
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mother__/RabbitMQConnectionConfigurationMother.ts`
```typescript
export class RabbitMQConnectionConfigurationMother {
  static create() {
    return {
      connectionSettings: {
        username: 'guest',
        password: 'guest',
        vhost: '/',
        connection: {
          secure: false,
          hostname: 'localhost',
          port: 5672
        }
      },
      exchangeSettings: { name: '' }
    };
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mother__/RabbitMQConnectionMother.ts`
```typescript
import { RabbitMqConnection } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/RabbitMQ/RabbitMqConnection';
import { RabbitMQConnectionDouble } from '../__mocks__/RabbitMQConnectionDouble';
import { RabbitMQConnectionConfigurationMother } from './RabbitMQConnectionConfigurationMother';

export class RabbitMQConnectionMother {
  static async create() {
    const config = RabbitMQConnectionConfigurationMother.create();
    const connection = new RabbitMqConnection(config);
    await connection.connect();
    return connection;
  }

  static failOnPublish() {
    return new RabbitMQConnectionDouble(RabbitMQConnectionConfigurationMother.create());
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/EventBus/__mother__/RabbitMQMongoClientMother.ts`
```typescript
import { MongoClientFactory } from '../../../../../../src/Contexts/Shared/infrastructure/persistence/mongo/MongoClientFactory';

export class RabbitMQMongoClientMother {
  static async create() {
    return MongoClientFactory.createClient('shared', {
      url: 'mongodb://localhost:27017/mooc-backend-test1'
    });
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/QueryBus/InMemoryQueryBus.test.ts`
```typescript
import { Query } from '../../../../../src/Contexts/Shared/domain/Query';
import { QueryHandlers } from '../../../../../src/Contexts/Shared/infrastructure/QueryBus/QueryHandlers';
import { QueryNotRegisteredError } from '../../../../../src/Contexts/Shared/domain/QueryNotRegisteredError';
import { QueryHandler } from '../../../../../src/Contexts/Shared/domain/QueryHandler';
import { Response } from '../../../../../src/Contexts/Shared/domain/Response';
import { InMemoryQueryBus } from '../../../../../src/Contexts/Shared/infrastructure/QueryBus/InMemoryQueryBus';

class UnhandledQuery extends Query {
  static QUERY_NAME = 'unhandled.query';
}

class HandledQuery extends Query {
  static QUERY_NAME = 'handled.query';
}

class MyQueryHandler implements QueryHandler<Query, Response> {
  subscribedTo(): HandledQuery {
    return HandledQuery;
  }

  async handle(query: HandledQuery): Promise<Response> {
    return {};
  }
}

describe('InMemoryQueryBus', () => {
  it('throws an error if dispatches a query without handler', async () => {
    const unhandledQuery = new UnhandledQuery();
    const queryHandlers = new QueryHandlers([]);
    const queryBus = new InMemoryQueryBus(queryHandlers);

    expect(queryBus.ask(unhandledQuery)).rejects.toBeInstanceOf(QueryNotRegisteredError);
  });

  it('accepts a query with handler', async () => {
    const handledQuery = new HandledQuery();
    const myQueryHandler = new MyQueryHandler();
    const queryHandlers = new QueryHandlers([myQueryHandler]);
    const queryBus = new InMemoryQueryBus(queryHandlers);

    await queryBus.ask(handledQuery);
  });
});
```

## File: `tests/Contexts/Shared/infrastructure/arranger/EnvironmentArranger.ts`
```typescript
export abstract class EnvironmentArranger {
  public abstract arrange(): Promise<void>;

  public abstract close(): Promise<void>;
}
```

## File: `tests/Contexts/Shared/infrastructure/mongo/MongoEnvironmentArranger.ts`
```typescript
import { MongoClient } from 'mongodb';
import { EnvironmentArranger } from '../arranger/EnvironmentArranger';

export class MongoEnvironmentArranger extends EnvironmentArranger {
  constructor(private _client: Promise<MongoClient>) {
    super();
  }

  public async arrange(): Promise<void> {
    await this.cleanDatabase();
  }

  protected async cleanDatabase(): Promise<void> {
    const collections = await this.collections();
    const client = await this.client();

    for (const collection of collections) {
      await client.db().collection(collection).deleteMany({});
    }
  }

  private async collections(): Promise<string[]> {
    const client = await this.client();
    const collections = await client.db().listCollections(undefined, { nameOnly: true }).toArray();

    return collections.map(collection => collection.name);
  }

  protected client(): Promise<MongoClient> {
    return this._client;
  }

  public async close(): Promise<void> {
    return (await this.client()).close();
  }
}
```

## File: `tests/Contexts/Shared/infrastructure/typeorm/TypeOrmEnvironmentArranger.ts`
```typescript
import { Connection, EntityMetadata } from 'typeorm';
import { EnvironmentArranger } from '../arranger/EnvironmentArranger';

export class TypeOrmEnvironmentArranger extends EnvironmentArranger {
  constructor(private _client: Promise<Connection>) {
    super();
  }

  public async arrange(): Promise<void> {
    await this.cleanDatabase();
  }

  protected async cleanDatabase(): Promise<void> {
    const entities = await this.entities();

    try {
      for (const entity of entities) {
        const repository = (await this._client).getRepository(entity.name);
        await repository.query(`TRUNCATE TABLE ${entity.tableName};`);
      }
    } catch (error) {
      throw new Error(`Unable to clean test database: ${error}`);
    }
  }

  private async entities(): Promise<EntityMetadata[]> {
    return (await this._client).entityMetadatas;
  }

  protected client(): Promise<Connection> {
    return this._client;
  }

  public async close(): Promise<void> {
    return (await this.client()).close();
  }
}
```

## File: `tests/apps/tsconfig.json`
```json
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "lib": ["es2015", "dom"],
  },
  "include": ["**/*.ts"]
}

```

## File: `tests/apps/backoffice/backend/features/status.feature`
```
Feature: Api status
  In order to know the server is up and running
  As a health check
  I want to check the api status

  Scenario: Check the api status
    Given I send a GET request to "/status"
    Then the response status code should be 200
```

## File: `tests/apps/backoffice/backend/features/courses/get-courses.feature`
```
Feature: Get courses
  As a user with permissions
  I want to get courses

  Scenario: All existing courses
    Given the following event is received:
    """
    {
      "data": {
        "id": "c77fa036-cbc7-4414-996b-c6a7a93cae09",
        "type": "course.created",
        "occurred_on": "2019-08-08T08:37:32+00:00",
        "aggregateId": "8c900b20-e04a-4777-9183-32faab6d2fb5",
        "attributes": {
          "name": "DDD en PHP!",
          "duration": "25 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    And the following event is received:
    """
        {
      "data": {
        "id": "353baf48-56e4-4eb2-91a0-b8f826135e6a",
        "type": "course.created",
        "occurred_on": "2019-08-08T08:37:32+00:00",
        "aggregateId": "8c4a4ed8-9458-489e-a167-b099d81fa096",
        "attributes": {
            "name": "DDD en Java!",
            "duration": "24 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    And I send a GET request to "/courses"
    Then the response status code should be 200
    And the response should be:
    """
    [
      {
          "id": "8c900b20-e04a-4777-9183-32faab6d2fb5",
          "name": "DDD en PHP!",
          "duration": "25 hours"
      },
      {
          "id": "8c4a4ed8-9458-489e-a167-b099d81fa096",
          "name": "DDD en Java!",
          "duration": "24 hours"
      }
    ]
    """
```

## File: `tests/apps/backoffice/backend/features/step_definitions/controller.steps.ts`
```typescript
import assert from 'assert';
import { Given, Then } from 'cucumber';
import request from 'supertest';
import { application } from './hooks.steps';

let _request: request.Test;
let _response: request.Response;

Given('I send a GET request to {string}', (route: string) => {
  _request = request(application.httpServer).get(route);
});

Then('the response status code should be {int}', async (status: number) => {
  _response = await _request.expect(status);
});

Then('the response should be:', async response => {
  const expectedResponse = JSON.parse(response);
  _response = await _request;
  assert.deepStrictEqual(_response.body, expectedResponse);
});
```

## File: `tests/apps/backoffice/backend/features/step_definitions/eventBus.steps.ts`
```typescript
import { Given } from 'cucumber';
import container from '../../../../../../src/apps/backoffice/backend/dependency-injection';
import { DomainEventDeserializer } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventDeserializer';
import { DomainEventSubscribers } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { eventBus } from './hooks.steps';

const deserializer = buildDeserializer();

Given('the following event is received:', async (event: any) => {
  const domainEvent = deserializer.deserialize(event)!;

  await eventBus.publish([domainEvent]);
  await wait(500);
});

function buildDeserializer() {
  const subscribers = DomainEventSubscribers.from(container);
  return DomainEventDeserializer.configure(subscribers);
}

function wait(milliseconds: number) {
  return new Promise(resolve => setTimeout(resolve, milliseconds));
}
```

## File: `tests/apps/backoffice/backend/features/step_definitions/hooks.steps.ts`
```typescript
import { AfterAll, BeforeAll } from 'cucumber';
import { BackofficeBackendApp } from '../../../../../../src/apps/backoffice/backend/BackofficeBackendApp';
import { ConfigureRabbitMQCommand } from '../../../../../../src/apps/backoffice/backend/command/ConfigureRabbitMQCommand';
import container from '../../../../../../src/apps/backoffice/backend/dependency-injection';
import { EventBus } from '../../../../../../src/Contexts/Shared/domain/EventBus';
import { EnvironmentArranger } from '../../../../../Contexts/Shared/infrastructure/arranger/EnvironmentArranger';

let application: BackofficeBackendApp;
let environmentArranger: EnvironmentArranger;
let eventBus: EventBus;

BeforeAll(async () => {
  await ConfigureRabbitMQCommand.run();

  environmentArranger = await container.get<Promise<EnvironmentArranger>>('Backoffice.EnvironmentArranger');
  eventBus = container.get<EventBus>('Backoffice.Shared.domain.EventBus');
  await environmentArranger.arrange();

  application = new BackofficeBackendApp();
  await application.start();
});

AfterAll(async () => {
  await environmentArranger.arrange();
  await environmentArranger.close();

  await application.stop();
});

export { application, environmentArranger, eventBus };
```

## File: `tests/apps/backoffice/backend/features/step_definitions/repository.steps.ts`
```typescript
import { Given } from 'cucumber';
import container from '../../../../../../src/apps/backoffice/backend/dependency-injection';
import { Course } from '../../../../../../src/Contexts/Mooc/Courses/domain/Course';
import { CourseDuration } from '../../../../../../src/Contexts/Mooc/Courses/domain/CourseDuration';
import { CourseName } from '../../../../../../src/Contexts/Mooc/Courses/domain/CourseName';
import { CourseRepository } from '../../../../../../src/Contexts/Mooc/Courses/domain/CourseRepository';
import { CourseId } from '../../../../../../src/Contexts/Mooc/Shared/domain/Courses/CourseId';

const courseRepository: CourseRepository = container.get('Backoffice.Courses.domain.BackofficeCourseRepository');

Given('there is the course:', async (course: any) => {
  const { id, name, duration } = JSON.parse(course);
  await courseRepository.save(new Course(new CourseId(id), new CourseName(name), new CourseDuration(duration)));
});
```

## File: `tests/apps/mooc/backend/features/status.feature`
```
Feature: Api status
  In order to know the server is up and running
  As a health check
  I want to check the api status

  Scenario: Check the api status
    Given I send a GET request to "/status"
    Then the response status code should be 200
```

## File: `tests/apps/mooc/backend/features/courses/create-course.feature`
```
Feature: Create a new course
  In order to have courses in the platform
  As a user with admin permissions
  I want to create a new course

  Scenario: A valid non existing course
    Given I send a PUT request to "/courses/ef8ac118-8d7f-49cc-abec-78e0d05af80a" with body:
    """
    {
      "id": "ef8ac118-8d7f-49cc-abec-78e0d05af80a",
      "name": "The best course",
      "duration": "5 hours"
    }
    """
    Then the response status code should be 201
    And the response should be empty

 Scenario: An invalid non existing course
    Given I send a PUT request to "/courses/ef8ac118-8d7f-49cc-abec-78e0d05af80a" with body:
    """
    {
      "id": "ef8ac118-8d7f-49cc-abec-78e0d05af80a",
      "name": 5,
      "duration": "5 hours"
    }
    """
    Then the response status code should be 422
```

## File: `tests/apps/mooc/backend/features/courses_counter/get-courses-counter.feature`
```
Feature: Obtain the total number of courses
  In order to have a courses counter
  As a user
  I want to see the courses counter

  Scenario: With one course
    Given I send an event to the event bus:
    """
    {
      "data": {
        "id": "c77fa036-cbc7-4414-996b-c6a7a93cae09",
        "type": "course.created",
        "occurred_on": "2019-08-08T08:37:32+00:00",
        "aggregateId": "8c900b20-e04a-4777-9183-32faab6d2fb5",
        "attributes": {
          "name": "DDD en PHP!",
          "duration": "25 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    When I send a GET request to "/courses-counter"
    Then the response status code should be 200
    And the response content should be:
    """
    {
      "total": 1
    }
    """


  Scenario: With more than one course having duplicates
    Given I send an event to the event bus:
    """
    {
      "data": {
        "id": "c77fa036-cbc7-4414-996b-c6a7a93cae09",
        "type": "course.created",
        "occurred_on": "2019-08-08T08:37:32+00:00",
        "aggregateId": "8c900b20-e04a-4777-9183-32faab6d2fb5",
        "attributes": {
          "name": "DDD en PHP!",
          "duration": "25 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    And I send an event to the event bus:
    """
    {
      "data": {
        "id": "8c4a4ed8-9458-489e-a167-b099d81fa096",
        "type": "course.created",
        "occurred_on": "2019-08-09T08:36:32+00:00",
        "aggregateId": "8c4a4ed8-9458-489e-a167-b099d81fa096",
        "attributes": {
          "name": "DDD en Java!",
          "duration": "24 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    And I send an event to the event bus:
    """
    {
      "data": {
        "id": "8c4a4ed8-9458-489e-a167-b099d81fa096",
        "type": "course.created",
        "occurred_on": "2019-08-09T08:36:32+00:00",
        "aggregateId": "8c4a4ed8-9458-489e-a167-b099d81fa096",
        "attributes": {
          "name": "DDD en Java!",
          "duration": "24 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    When I send a GET request to "/courses-counter"
    Then the response status code should be 200
    And the response content should be:
    """
    {
      "total": 2
    }
    """
```

## File: `tests/apps/mooc/backend/features/step_definitions/controller.steps.ts`
```typescript
import assert from 'assert';
import { Given, Then } from 'cucumber';
import request from 'supertest';
import { application } from './hooks.steps';

let _request: request.Test;
let _response: request.Response;

Given('I send a GET request to {string}', (route: string) => {
  _request = request(application.httpServer).get(route);
});

Then('the response status code should be {int}', async (status: number) => {
  _response = await _request.expect(status);
});

Given('I send a PUT request to {string} with body:', (route: string, body: string) => {
  _request = request(application.httpServer).put(route).send(JSON.parse(body));
});

Then('the response should be empty', () => {
  assert.deepStrictEqual(_response.body, {});
});

Then('the response content should be:', response => {
  assert.deepStrictEqual(_response.body, JSON.parse(response));
});

```

## File: `tests/apps/mooc/backend/features/step_definitions/eventBus.steps.ts`
```typescript
import { Given } from 'cucumber';
import container from '../../../../../../src/apps/mooc/backend/dependency-injection';
import { DomainEventDeserializer } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventDeserializer';
import { DomainEventSubscribers } from '../../../../../../src/Contexts/Shared/infrastructure/EventBus/DomainEventSubscribers';
import { eventBus } from './hooks.steps';

const deserializer = buildDeserializer();

Given('I send an event to the event bus:', async (event: any) => {
  const domainEvent = deserializer.deserialize(event);

  await eventBus.publish([domainEvent!]);
  await wait(500);
});

function buildDeserializer() {
  const subscribers = DomainEventSubscribers.from(container);

  return DomainEventDeserializer.configure(subscribers);
}

function wait(milliseconds: number) {
  return new Promise(resolve => setTimeout(resolve, milliseconds));
}
```

## File: `tests/apps/mooc/backend/features/step_definitions/hooks.steps.ts`
```typescript
import { AfterAll, BeforeAll } from 'cucumber';
import { ConfigureRabbitMQCommand } from '../../../../../../src/apps/mooc/backend/command/ConfigureRabbitMQCommand';
import container from '../../../../../../src/apps/mooc/backend/dependency-injection';
import { MoocBackendApp } from '../../../../../../src/apps/mooc/backend/MoocBackendApp';
import { EventBus } from '../../../../../../src/Contexts/Shared/domain/EventBus';
import { EnvironmentArranger } from '../../../../../Contexts/Shared/infrastructure/arranger/EnvironmentArranger';

let application: MoocBackendApp;
let environmentArranger: EnvironmentArranger;
let eventBus: EventBus;

BeforeAll(async () => {
  await ConfigureRabbitMQCommand.run();

  environmentArranger = await container.get<Promise<EnvironmentArranger>>('Mooc.EnvironmentArranger');
  eventBus = container.get<EventBus>('Mooc.Shared.domain.EventBus');
  await environmentArranger.arrange();

  application = new MoocBackendApp();
  await application.start();
});

AfterAll(async () => {
  await environmentArranger.close();

  await application.stop();
});

export { application, environmentArranger, eventBus };
```

