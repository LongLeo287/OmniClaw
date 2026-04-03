---
id: github.com-codelytv-typescript-ddd-skeleton-d0220c
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:40.993138
---

# KNOWLEDGE EXTRACT: github.com_CodelyTV_typescript-ddd-skeleton_d0220cfa
> **Extracted on:** 2026-04-01 15:18:31
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524427/github.com_CodelyTV_typescript-ddd-skeleton_d0220cfa

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

## File: `.eslintrc.js`
```javascript
module.exports = {
	extends: ['eslint-config-codely/typescript'],
	rules: {
		'no-console': 'warn'
	},
	overrides: [
		{
			files: ['*.ts', '*.tsx'],
			parserOptions: {
				project: ['./tsconfig.json']
			},
			rules: {
				'@typescript-eslint/no-floating-promises': 'warn'
			}
		}
	]
};
```

## File: `.gitignore`
```
node_modules/
dist/
.tmp
logs/
data
test-results.xml
```

## File: `.nvmrc`
```
v14.18.0
```

## File: `.prettierrc`
```
{
  "printWidth": 120,
  "tabWidth": 2,
  "singleQuote": true,
  "trailingComma": "none",
  "semicolons": true,
  "quoteProps": "as-needed",
  "arrowParens": "avoid"
}
```

## File: `Dockerfile`
```
FROM node:14-slim

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
```

## File: `README.md`
```markdown
# TypeScript basic skeleton

For now, you have all the code example available in this other repository: https://github.com/CodelyTV/typescript-ddd-example

The idea is that we'll move the basic parts (folder structure and bare minimum code to serve as skeleton) to this repository (`typescript-ddd-skeleton`) once we completely finish the `typescript-ddd-example` code. Current progress: ~95%
```

## File: `cucumber.js`
```javascript
/* eslint-disable camelcase */
const common = [
	'--require-module ts-node/register' // Load TypeScript module
];

const mooc_backend = [
	...common,
	'tests/apps/mooc/backend/features/**/*.feature',
	'--require tests/apps/mooc/backend/features/step_definitions/*.steps.ts'
].join(' ');

module.exports = {
	mooc_backend
};
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
  "name": "typescript-ddd-skeleton",
  "version": "1.0.0",
  "description": "",
  "repository": {
    "url": "https://github.com/CodelyTV/typescript-ddd-skeleton"
  },
  "license": "",
  "engines": {
    "node": ">=14.0.0",
    "npm": ">=6.14.0"
  },
  "scripts": {
    "dev:mooc:backend": "NODE_ENV=dev ts-node-dev --ignore-watch node_modules  ./src/apps/mooc/backend/start.ts",
    "lint": "eslint --ignore-path .gitignore .",
    "lint:fix": "npm run lint -- --fix",
    "test": "npm run test:unit && npm run test:features",
    "test:unit": "NODE_ENV=test jest",
    "start:mooc:backend": "NODE_ENV=production node dist/src/apps/mooc/backend/start",
    "test:features": "npm run test:mooc:backend:features",
    "test:mooc:backend:features": "NODE_ENV=test cucumber-js -p mooc_backend",
    "build": "npm run build:clean && npm run build:tsc && npm run build:di",
    "build:tsc": "tsc -p tsconfig.prod.json",
    "build:di": "copy 'src/**/*.{json,yaml,html,png}' dist/src",
    "build:clean": "rm -r dist; exit 0"
  },
  "dependencies": {
    "body-parser": "^1.19.0",
    "bodybuilder": "^2.4.0",
    "bson": "^4.5.2",
    "compression": "^1.7.4",
    "connect-flash": "^0.1.1",
    "cookie-parser": "^1.4.5",
    "cookie-session": "^1.4.0",
    "copy": "^0.3.2",
    "errorhandler": "^1.5.1",
    "express": "^4.17.1",
    "express-promise-router": "^4.1.0",
    "express-validator": "^6.12.2",
    "glob": "^7.2.0",
    "helmet": "^4.6.0",
    "http-status": "^1.5.0",
    "node-dependency-injection": "^2.7.1",
    "nunjucks": "^3.2.3",
    "ts-node": "^10.2.1",
    "typescript": "^4.4.3",
    "winston": "^3.3.3"
  },
  "devDependencies": {
    "@types/bson": "^4.0.5",
    "@types/compression": "^1.7.2",
    "@types/connect-flash": "0.0.37",
    "@types/cookie-parser": "^1.4.2",
    "@types/cookie-session": "^2.0.43",
    "@types/cucumber": "^6.0.1",
    "@types/errorhandler": "1.5.0",
    "@types/express": "^4.17.13",
    "@types/faker": "^5.5.8",
    "@types/glob": "^7.1.4",
    "@types/helmet": "0.0.48",
    "@types/jest": "^27.0.2",
    "@types/node": "^16.10.2",
    "@types/nunjucks": "^3.2.0",
    "@types/supertest": "^2.0.11",
    "cucumber": "^6.0.5",
    "eslint": "^8.33.0",
    "eslint-config-codely": "^2.1.3",
    "faker": "^5.5.3",
    "husky": "^7.0.2",
    "jest": "^27.2.4",
    "lint-staged": "11.2.0",
    "prettier": "^2.4.1",
    "supertest": "^6.1.6",
    "ts-jest": "^27.0.5",
    "ts-node-dev": "^1.1.8"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "{src,tests}/**/*.ts": [
      "npm run lint:fix",
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
  "exclude": ["node_modules"]
}
```

## File: `tsconfig.prod.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "baseUrl": ".",
  },
  "exclude": ["node_modules", "tests"]
}
```

## File: `src/Contexts/Mooc/Courses/application/CourseCreator.ts`
```typescript
import { Course } from '../domain/Course';
import { CourseRepository } from '../domain/CourseRepository';

export class CourseCreator {
	private readonly repository: CourseRepository;

	constructor(repository: CourseRepository) {
		this.repository = repository;
	}

	async run(id: string, name: string, duration: string): Promise<void> {
		const course = new Course({ id, name, duration });

		return this.repository.save(course);
	}
}
```

## File: `src/Contexts/Mooc/Courses/domain/Course.ts`
```typescript
export class Course {
	readonly id: string;
	readonly name: string;
	readonly duration: string;

	constructor({ id, name, duration }: { id: string; name: string; duration: string }) {
		this.id = id;
		this.name = name;
		this.duration = duration;
	}
}
```

## File: `src/Contexts/Mooc/Courses/domain/CourseRepository.ts`
```typescript
import { Course } from './Course';

export interface CourseRepository {
	save(course: Course): Promise<void>;
}
```

## File: `src/apps/mooc/backend/MoocBackendApp.ts`
```typescript
import { Server } from './server';

export class MoocBackendApp {
	server?: Server;

	async start(): Promise<void> {
		const port = process.env.PORT ?? '5000';
		this.server = new Server(port);

		return this.server.listen();
	}

	get httpServer(): Server['httpServer'] | undefined {
		return this.server?.getHTTPServer();
	}

	async stop(): Promise<void> {
		return this.server?.stop();
	}
}
```

## File: `src/apps/mooc/backend/server.ts`
```typescript
import { json, urlencoded } from 'body-parser';
import compress from 'compression';
import errorHandler from 'errorhandler';
import express, { Request, Response } from 'express';
import Router from 'express-promise-router';
import helmet from 'helmet';
import * as http from 'http';
import httpStatus from 'http-status';

import { registerRoutes } from './routes';

export class Server {
	private readonly express: express.Express;
	private readonly port: string;
	private httpServer?: http.Server;

	constructor(port: string) {
		this.port = port;
		this.express = express();
		this.express.use(json());
		this.express.use(urlencoded({ extended: true }));
		this.express.use(helmet.xssFilter());
		this.express.use(helmet.noSniff());
		this.express.use(helmet.hidePoweredBy());
		this.express.use(helmet.frameguard({ action: 'deny' }));
		this.express.use(compress());
		const router = Router();
		router.use(errorHandler());
		this.express.use(router);

		registerRoutes(router);

		router.use((err: Error, req: Request, res: Response, _next: () => void) => {
			console.log(err);
			res.status(httpStatus.INTERNAL_SERVER_ERROR).send(err.message);
		});
	}

	async listen(): Promise<void> {
		return new Promise(resolve => {
			const env = this.express.get('env') as string;
			this.httpServer = this.express.listen(this.port, () => {
				console.log(
					`  Mock Backend App is running at http://localhost:${this.port} in ${env} mode`
				);
				console.log('  Press CTRL-C to stop\n');
				resolve();
			});
		});
	}

	getHTTPServer(): Server['httpServer'] {
		return this.httpServer;
	}

	async stop(): Promise<void> {
		return new Promise((resolve, reject) => {
			if (this.httpServer) {
				this.httpServer.close(error => {
					if (error) {
						reject(error);

						return;
					}

					resolve();
				});
			}

			resolve();
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

## File: `src/apps/mooc/backend/controllers/Controller.ts`
```typescript
import { Request, Response } from 'express';

export interface Controller {
	run(req: Request, res: Response): Promise<void> | void;
}
```

## File: `src/apps/mooc/backend/controllers/CoursePutController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';

import { Controller } from './Controller';

export class CoursePutController implements Controller {
	run(req: Request, res: Response): void {
		res.status(httpStatus.CREATED).send();
	}
}
```

## File: `src/apps/mooc/backend/controllers/StatusGetController.ts`
```typescript
import { Request, Response } from 'express';
import httpStatus from 'http-status';

import { Controller } from './Controller';

export default class StatusGetController implements Controller {
	run(req: Request, res: Response): void {
		res.status(httpStatus.OK).send();
	}
}
```

## File: `src/apps/mooc/backend/dependency-injection/application.yaml`
```yaml
imports:
  - { resource: ./apps/application.yaml }
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
```

## File: `src/apps/mooc/backend/dependency-injection/index.ts`
```typescript
import { ContainerBuilder, YamlFileLoader } from 'node-dependency-injection';

const container = new ContainerBuilder();
const loader = new YamlFileLoader(container);
const env = process.env.NODE_ENV ?? 'dev';

loader.load(`${__dirname}/application_${env}.yaml`);

export default container;
```

## File: `src/apps/mooc/backend/dependency-injection/apps/application.yaml`
```yaml
services:

  Apps.mooc.controllers.StatusGetController:
    class: ../../controllers/StatusGetController
    arguments: []

  Apps.mooc.controllers.CoursePutController:
    class: ../../controllers/CoursePutController
    arguments: [""]
```

## File: `src/apps/mooc/backend/routes/courses.route.ts`
```typescript
import { Request, Response, Router } from 'express';

import { CoursePutController } from '../controllers/CoursePutController';
import container from '../dependency-injection';

export const register = (router: Router): void => {
	const coursePutController = container.get<CoursePutController>(
		'Apps.mooc.controllers.CoursePutController'
	);
	router.put('/courses/:id', (req: Request, res: Response) => coursePutController.run(req, res));
};
```

## File: `src/apps/mooc/backend/routes/index.ts`
```typescript
import { Router } from 'express';
import glob from 'glob';

export function registerRoutes(router: Router): void {
	const routes = glob.sync(`${__dirname}/**/*.route.*`);
	routes.map(route => register(route, router));
}

function register(routePath: string, router: Router) {
	// eslint-disable-next-line @typescript-eslint/no-require-imports, @typescript-eslint/no-var-requires
	const { register } = require(routePath) as { register: (router: Router) => void };
	register(router);
}
```

## File: `src/apps/mooc/backend/routes/status.route.ts`
```typescript
import { Request, Response, Router } from 'express';

import StatusController from '../controllers/StatusGetController';
import container from '../dependency-injection';

export const register = (router: Router): void => {
	const controller = container.get<StatusController>('Apps.mooc.controllers.StatusGetController');
	router.get('/status', (req: Request, res: Response) => {
		controller.run(req, res);
	});
};
```

## File: `tests/Contexts/Mooc/Courses/__mocks__/CourseRepositoryMock.ts`
```typescript
import { Course } from '../../../../../src/Contexts/Mooc/Courses/domain/Course';
import { CourseRepository } from '../../../../../src/Contexts/Mooc/Courses/domain/CourseRepository';

export class CourseRepositoryMock implements CourseRepository {
	private readonly mockSave = jest.fn();

	async save(course: Course): Promise<void> {
		await this.mockSave(course);
	}

	assertLastSavedCourseIs(expected: Course): void {
		const mock = this.mockSave.mock;
		const lastSavedCourse = (mock.calls[mock.calls.length - 1] as Course[])[0];
		expect(lastSavedCourse).toBeInstanceOf(Course);
		expect(lastSavedCourse.id).toEqual(expected.id);
	}
}
```

## File: `tests/Contexts/Mooc/Courses/application/CourseCreator.test.ts`
```typescript
import { CourseCreator } from '../../../../../src/Contexts/Mooc/Courses/application/CourseCreator';
import { Course } from '../../../../../src/Contexts/Mooc/Courses/domain/Course';
import { CourseRepositoryMock } from '../__mocks__/CourseRepositoryMock';

let repository: CourseRepositoryMock;
let creator: CourseCreator;

beforeEach(() => {
	repository = new CourseRepositoryMock();
	creator = new CourseCreator(repository);
});

describe('CourseCreator', () => {
	it('should create a valid course', async () => {
		const id = 'some-id';
		const name = 'some-name';
		const duration = 'some-duration';

		const course = new Course({ id, name, duration });

		await creator.run(id, name, duration);

		repository.assertLastSavedCourseIs(course);
	});
});
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
      "name": "The best course",
      "duration": "5 hours"
    }
    """
    Then the response status code should be 201
    And the response should be empty
```

## File: `tests/apps/mooc/backend/features/step_definitions/controller.steps.ts`
```typescript
import assert from 'assert';
import { AfterAll, BeforeAll, Given, Then } from 'cucumber';
import request from 'supertest';

import { MoocBackendApp } from '../../../../../../src/apps/mooc/backend/MoocBackendApp';

let _request: request.Test;
let application: MoocBackendApp;
let _response: request.Response;

Given('I send a GET request to {string}', (route: string) => {
	_request = request(application.httpServer).get(route);
});

Then('the response status code should be {int}', async (status: number) => {
	_response = await _request.expect(status);
});

Given('I send a PUT request to {string} with body:', (route: string, body: string) => {
	_request = request(application.httpServer)
		.put(route)
		.send(JSON.parse(body) as object);
});

Then('the response should be empty', () => {
	assert.deepStrictEqual(_response.body, {});
});

BeforeAll(() => {
	application = new MoocBackendApp();
	application.start();
});

AfterAll(() => {
	application.stop();
});
```

