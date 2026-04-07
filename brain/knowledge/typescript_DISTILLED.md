---
id: typescript
type: knowledge
owner: OA_Triage
---
# typescript
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
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

### File: readme.md
```md
# TypeScript basic skeleton

For now, you have all the code example available in this other repository: https://github.com/CodelyTV/typescript-ddd-example

The idea is that we'll move the basic parts (folder structure and bare minimum code to serve as skeleton) to this repository (`typescript-ddd-skeleton`) once we completely finish the `typescript-ddd-example` code. Current progress: ~95%

```

### File: src\apps\backoffice\frontend\package.json
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

### File: src\apps\backoffice\frontend\README.md
```md
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
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

```

### File: .eslintrc.js
```js
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

### File: cucumber.js
```js
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

### File: jest.config.js
```js
module.exports = {
	preset: 'ts-jest',
	testEnvironment: 'node',
	cacheDirectory: '.tmp/jestCache'
};

```

### File: tsconfig.json
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

### File: tsconfig.prod.json
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "baseUrl": ".",
  },
  "exclude": ["node_modules", "tests"]
}

```

### File: data\courses.json
```json
{
  "data": [
    {
      "title": "✌️ Vue 3: Novedades aplicadas al mundo real",
      "category": "frontend",
      "description": "Veremos cómo exprimir las novedades de Vue 3 con ejemplos reales y aplicando buenas prácticas.",
      "image": "novedades-vue-3.jpg",
      "link": "https://pro.codely.tv/library/novedades-vue-3/about/?utm_source=cursos&utm_medium=landing&utm_campaign=internal&utm_content=courses-masonry",
      "teachers": "Javi y Núria"
    },
    {
      "title": "🐂 Makefiles",
      "category": "tooling",
      "description": "El centralizar tareas de nuestras aplicaciones es algo muy importante, y con los Makefiles se simplifica mucho.",
      "image": "makefiles.jpg",
      "link": "https://pro.codely.tv/library/makefiles/about/?utm_source=cursos&utm_medium=landing&utm_campaign=internal&utm_content=courses-masonry",
      "teachers": "Rafa"
    },
    {
      "title": "💻 Bash para el día a día: Scripting & Productividad",
      "category": "tooling",
      "description": "Aprende a usar la navaja suiza de los programadores 😬",
      "image": "bash.jpg",
      "link": "https://pro.codely.tv/library/curso-bash/about/?utm_source=cursos&utm_medium=landing&utm_campaign=internal&utm_content=courses-masonry",
      "teachers": "Javi y Rafa"
    },
    {
      "title": "☕ DDD en Java",
      "category": "backend",
      "description": "Crea paso a paso tu aplicación Java siguiendo Domain-Driven Design. Estructura de carpetas, integración con BD, sistema de colas, CQRS y más.",
      "image": "ddd-java.jpg",
      "link": "https://pro.codely.tv/library/ddd-en-java/about/?utm_source=cursos&utm_medium=landing&utm_campaign=internal&utm_content=courses-masonry",
      "teachers": "Javi y Rafa"
    },
    {
      "title": "🐘 DDD en PHP",
      "category": "backend",
      "description": "Crea paso a paso tu aplicación PHP siguiendo Domain-Driven Design. Estructura de carpetas, integración con BD, sistema de colas, CQRS y más.",
      "image": "ddd-en-php.jpg",
      "link": "https://pro.codely.tv/library/ddd-en-php/about/?utm_source=cursos&utm_medium=landing&utm_campaign=internal&utm_content=courses-masonry",
      "teachers": "Javi y Rafa"
    },
    {
      "title": "💻 Terminal 100% productiva con Zsh",
      "category": "tooling",
      "description": "Consigue ser un Productivity Raptor™️ con tu terminal gracias a Zsh, Oh My Zsh, Zim y funciones avanzadas.",
      "image": "terminal-zsh.jpg",
      "link": "https://pro.codely.tv/library/terminal-zsh/about/?utm_source=cursos&utm_medium=landing&utm_campaign=internal&utm_content=courses-masonry",
      "teachers": "Javi y Rafa"
    },
    {
      "title": "📐 Buenas prácticas con CSS: Layouts",
      "category": "frontend",
      "description": "Aprende a crear layouts responsive mantenibles y reutilizables con CSS sin desesperarte 🧘",
      "image": "layouts-css.jpg",
      "link": "https://pro.codely.tv/library/layouts-css/about/?utm_source=cursos&utm_medium=landing&utm_campaign=internal&utm_content=courses-masonry",
      "teachers": "Núria y Rafa"
    }
  ]
}
```

### File: src\app.ts
```ts
import express from "express";
import path from "path";

import { loadApiEndpoints } from "./controllers/api";

// Create Express server
const app = express();

// Express configuration
app.set("port", process.env.PORT ?? 3000);
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "../public"), { maxAge: 31557600000 }));

loadApiEndpoints(app);

export default app;

```

### File: src\Codelyber.ts
```ts
export class Codelyber {
	private readonly GREETING = "Hi";

	constructor(private readonly name: string) {}

	greet(): string {
		return `${this.GREETING} ${this.name} from Codely TypeScript Basic Skeleton!`;
	}
}

```

### File: src\server.ts
```ts
/* eslint-disable no-console */
import app from "./app";

/**
 * Start Express server.
 */
const server = app.listen(app.get("port"), () => {
	console.log(
		"  App is running at http://localhost:%d in %s mode",
		app.get("port"),
		app.get("env"),
	);
	console.log("  Press CTRL-C to stop\n");
});

export default server;

```

### File: test\api.spec.ts
```ts
import request from "supertest";

import app from "../src/app";

describe("GET /api", () => {
	it("should return 200 OK", () => {
		return request(app).get("/api").expect(200);
	});
});

```

### File: tests\Codelyber.test.ts
```ts
import { Codelyber } from "../src/Codelyber";

describe("Codelyber", () => {
	it("can be instantiated without throwing errors", () => {
		const randomCodelyberInstantiator = () => {
			new Codelyber("Isma");
		};

		expect(randomCodelyberInstantiator).not.toThrow(TypeError);
	});

	it("greets", () => {
		const randomCodelyber = new Codelyber("Javi");

		const expectedGreeting = "Hi Javi from Codely TypeScript Basic Skeleton!";

		expect(randomCodelyber.greet()).toEqual(expectedGreeting);
	});
});

```

### File: src\controllers\api.ts
```ts
import { Application, Request, Response } from "express";

import CoursesData from "../../data/courses.json";

export const loadApiEndpoints = (app: Application): void => {
	app.get("/api", (req: Request, res: Response) => {
		return res.status(200).send(CoursesData);
	});
};

```

### File: tests\apps\tsconfig.json
```json
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "lib": ["es2015", "dom"],
  },
  "include": ["**/*.ts"]
}


```

### File: src\apps\backoffice\backend\BackofficeBackendApp.ts
```ts
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

### File: src\apps\backoffice\backend\server.ts
```ts
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

### File: src\apps\backoffice\backend\start.ts
```ts
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

### File: src\apps\backoffice\frontend\postcss.config.js
```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}

```

### File: src\apps\backoffice\frontend\tailwind.config.js
```js
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

### File: src\apps\backoffice\frontend\tsconfig.json
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

### File: src\apps\mooc\backend\MoocBackendApp.ts
```ts
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

### File: src\apps\mooc\backend\server.ts
```ts
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

### File: src\apps\mooc\backend\start.ts
```ts
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

### File: src\Contexts\Shared\domain\AggregateRoot.ts
```ts
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

### File: src\Contexts\Shared\domain\Command.ts
```ts
export abstract class Command {}

```

### File: src\Contexts\Shared\domain\CommandBus.ts
```ts
import { Command } from './Command';

export interface CommandBus {
  dispatch(command: Command): Promise<void>;
}

```

### File: src\Contexts\Shared\domain\CommandHandler.ts
```ts
import { Command } from './Command';

export interface CommandHandler<T extends Command> {
  subscribedTo(): Command;
  handle(command: T): Promise<void>;
}

```

### File: src\Contexts\Shared\domain\CommandNotRegisteredError.ts
```ts
import { Command } from './Command';

export class CommandNotRegisteredError extends Error {
  constructor(command: Command) {
    super(`The command <${command.constructor.name}> hasn't a command handler associated`);
  }
}

```

### File: src\Contexts\Shared\domain\DomainEvent.ts
```ts
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

### File: src\Contexts\Shared\domain\DomainEventSubscriber.ts
```ts
import { DomainEvent, DomainEventClass } from './DomainEvent';

export interface DomainEventSubscriber<T extends DomainEvent> {
  subscribedTo(): Array<DomainEventClass>;
  on(domainEvent: T): Promise<void>;
}

```

### File: src\Contexts\Shared\domain\EventBus.ts
```ts
import { DomainEventSubscribers } from '../infrastructure/EventBus/DomainEventSubscribers';
import { DomainEvent } from './DomainEvent';

export interface EventBus {
  publish(events: Array<DomainEvent>): Promise<void>;
  addSubscribers(subscribers: DomainEventSubscribers): void;
}

```

### File: src\Contexts\Shared\domain\Logger.ts
```ts
export default interface Logger {
  debug(message: string): void;
  error(message: string | Error): void;
  info(message: string): void;
}

```

### File: src\Contexts\Shared\domain\NewableClass.ts
```ts
export interface NewableClass<T> extends Function {
  new (...args: any[]): T;
}

```

### File: src\Contexts\Shared\domain\Nullable.ts
```ts
export type Nullable<T> = T | null | undefined;

```

### File: src\Contexts\Shared\domain\Query.ts
```ts
export abstract class Query {}

```

### File: src\Contexts\Shared\domain\QueryBus.ts
```ts
import { Query } from './Query';
import { Response } from './Response';

export interface QueryBus {
  ask<R extends Response>(query: Query): Promise<R>;
}

```

### File: src\Contexts\Shared\domain\QueryHandler.ts
```ts
import { Query } from './Query';
import { Response } from './Response';

export interface QueryHandler<Q extends Query, R extends Response> {
  subscribedTo(): Query;
  handle(query: Q): Promise<R>;
}

```

### File: src\Contexts\Shared\domain\QueryNotRegisteredError.ts
```ts
import { Query } from './Query';

export class QueryNotRegisteredError extends Error {
  constructor(query: Query) {
    super(`The query <${query.constructor.name}> hasn't a query handler associated`);
  }
}

```

### File: src\Contexts\Shared\domain\Response.ts
```ts
export interface Response {}

```

### File: src\Contexts\Shared\infrastructure\WinstonLogger.ts
```ts
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

### File: tests\Contexts\Shared\domain\IntegerMother.ts
```ts
import { MotherCreator } from './MotherCreator';

export class IntegerMother {
  static random(max?: number): number {
    return MotherCreator.random().random.number(max);
  }
}

```

### File: tests\Contexts\Shared\domain\MotherCreator.ts
```ts
import * as faker from 'faker';

export class MotherCreator {
  static random(): Faker.FakerStatic {
    return faker;
  }
}
```

### File: tests\Contexts\Shared\domain\Repeater.ts
```ts
import { IntegerMother } from './IntegerMother';
export class Repeater {
  static random(callable: Function, iterations: number) {
    return Array(iterations || IntegerMother.random(20))
      .fill({})
      .map(() => callable());
  }
}

```

### File: tests\Contexts\Shared\domain\UuidMother.ts
```ts
import { MotherCreator } from './MotherCreator';

export class UuidMother {
  static random(): string {
    return MotherCreator.random().datatype.uuid();
  }
}
```

### File: tests\Contexts\Shared\domain\WordMother.ts
```ts
import { MotherCreator } from './MotherCreator';

export class WordMother {
  static random({ minLength = 1, maxLength }: { minLength?: number; maxLength: number }): string {
    return MotherCreator.random().lorem.word(Math.floor(Math.random() * (maxLength - minLength)) + minLength) || 'word';
  }
}
```

### File: tests\Contexts\Shared\infrastructure\MongoClientFactory.test.ts
```ts
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

### File: tests\Contexts\Shared\infrastructure\TypeOrmClientFactory.test.ts
```ts
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

### File: src\apps\backoffice\backend\command\ConfigureRabbitMQCommand.ts
```ts
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

### File: src\apps\backoffice\backend\command\runConfigureRabbitMQCommand.ts
```ts
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

### File: src\apps\backoffice\backend\controllers\Controller.ts
```ts
import { Request, Response } from 'express';

export interface Controller {
  run(req: Request, res: Response): Promise<void>;
}

```

### File: src\apps\backoffice\backend\controllers\CoursesGetController.ts
```ts
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

### File: src\apps\backoffice\backend\controllers\CoursesPostController.ts
```ts
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

### File: src\apps\backoffice\backend\controllers\StatusGetController.ts
```ts
import { Request, Response } from 'express';
import httpStatus from 'http-status';
import { Controller } from './Controller';

export default class StatusGetController implements Controller {
  async run(req: Request, res: Response) {
    res.status(httpStatus.OK).send();
  }
}

```

### File: src\apps\backoffice\backend\routes\courses.route.ts
```ts
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

### File: src\apps\backoffice\backend\routes\index.ts
```ts
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

### File: src\apps\backoffice\backend\routes\status.route.ts
```ts
import { Express } from 'express';
import container from '../dependency-injection';
import StatusController from '../controllers/StatusGetController';

export const register = (app: Express) => {
  const controller: StatusController = container.get('Apps.Backoffice.Backend.controllers.StatusGetController');
  app.get('/status', controller.run.bind(controller));
};

```

### File: src\apps\backoffice\frontend\public\index.html
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

### File: src\apps\backoffice\frontend\public\manifest.json
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

### File: src\apps\backoffice\frontend\public\robots.txt
```txt
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:

```

### File: src\apps\backoffice\frontend\src\App.css
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

### File: src\apps\backoffice\frontend\src\index.css
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

### File: src\apps\backoffice\frontend\src\react-app-env.d.ts
```ts
/// <reference types="react-scripts" />

```

### File: src\apps\backoffice\frontend\src\reportWebVitals.ts
```ts
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

### File: src\apps\backoffice\frontend\src\setupTests.ts
```ts
// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';

```

### File: src\apps\mooc\backend\command\ConfigureRabbitMQCommand.ts
```ts
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

### File: src\apps\mooc\backend\command\runConfigureRabbitMQCommand.ts
```ts
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

### File: src\apps\mooc\backend\controllers\Controller.ts
```ts
import { Request, Response } from 'express';

export interface Controller {
	run(req: Request, res: Response): Promise<void> | void;
}

```

### File: src\apps\mooc\backend\controllers\CoursePutController.ts
```ts
import { Request, Response } from 'express';
import httpStatus from 'http-status';

import { Controller } from './Controller';

export class CoursePutController implements Controller {
	run(req: Request, res: Response): void {
		res.status(httpStatus.CREATED).send();
	}
}

```

### File: src\apps\mooc\backend\controllers\CoursesCounterGetController.ts
```ts
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

### File: src\apps\mooc\backend\controllers\StatusGetController.ts
```ts
import { Request, Response } from 'express';
import httpStatus from 'http-status';

import { Controller } from './Controller';

export default class StatusGetController implements Controller {
	run(req: Request, res: Response): void {
		res.status(httpStatus.OK).send();
	}
}

```

### File: src\apps\mooc\backend\routes\courses-counter.route.ts
```ts
import { Request, Response, Router } from 'express';
import container from '../dependency-injection';

export const register = (router: Router) => {
  const coursesCounterGetController = container.get('Apps.mooc.controllers.CoursesCounterGetController');
  router.get('/courses-counter', (req: Request, res: Response) => coursesCounterGetController.run(req, res));
};

```

### File: src\apps\mooc\backend\routes\courses.route.ts
```ts
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

### File: src\apps\mooc\backend\routes\index.ts
```ts
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

### File: src\apps\mooc\backend\routes\status.route.ts
```ts
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

### File: src\Contexts\Backoffice\Courses\application\BackofficeCoursesResponse.ts
```ts
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

### File: src\Contexts\Backoffice\Courses\domain\BackofficeCourse.ts
```ts
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

### File: src\Contexts\Backoffice\Courses\domain\BackofficeCourseDuration.ts
```ts
import { StringValueObject } from '../../../Shared/domain/value-object/StringValueObject';

export class BackofficeCourseDuration extends StringValueObject {}

```

### File: src\Contexts\Backoffice\Courses\domain\BackofficeCourseId.ts
```ts
import { Uuid } from '../../../Shared/domain/value-object/Uuid';

export class BackofficeCourseId extends Uuid {}

```

### File: src\Contexts\Backoffice\Courses\domain\BackofficeCourseName.ts
```ts
import { StringValueObject } from '../../../Shared/domain/value-object/StringValueObject';

export class BackofficeCourseName extends StringValueObject {}

```

### File: src\Contexts\Backoffice\Courses\domain\BackofficeCourseRepository.ts
```ts
import { Criteria } from '../../../Shared/domain/criteria/Criteria';
import { BackofficeCourse } from './BackofficeCourse';

export interface BackofficeCourseRepository {
  save(course: BackofficeCourse): Promise<void>;
  searchAll(): Promise<Array<BackofficeCourse>>;
  matching(criteria: Criteria): Promise<Array<BackofficeCourse>>;
}

```

### File: src\Contexts\Mooc\Courses\application\CourseCreator.ts
```ts
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

### File: src\Contexts\Mooc\Courses\application\CreateCourseCommandHandler.ts
```ts
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

### File: src\Contexts\Mooc\Courses\domain\Course.ts
```ts
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

### File: src\Contexts\Mooc\Courses\domain\CourseCreatedDomainEvent.ts
```ts
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

### File: src\Contexts\Mooc\Courses\domain\CourseDuration.ts
```ts
import { StringValueObject } from '../../../Shared/domain/value-object/StringValueObject';

export class CourseDuration extends StringValueObject {}

```

### File: src\Contexts\Mooc\Courses\domain\CourseName.ts
```ts
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

### File: src\Contexts\Mooc\Courses\domain\CourseNameLengthExceeded.ts
```ts
import { InvalidArgumentError } from '../../../Shared/domain/value-object/InvalidArgumentError';

export class CourseNameLengthExceeded extends InvalidArgumentError {}

```

### File: src\Contexts\Mooc\Courses\domain\CourseRepository.ts
```ts
import { Course } from './Course';

export interface CourseRepository {
	save(course: Course): Promise<void>;
}

```

### File: src\Contexts\Mooc\Courses\domain\CreateCourseCommand.ts
```ts
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

### File: src\Contexts\Mooc\CoursesCounter\domain\CoursesCounter.ts
```ts
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
