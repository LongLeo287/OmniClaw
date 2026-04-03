---
id: github.com-codelytv-typescript-api-skeleton-2344cd
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:40.928352
---

# KNOWLEDGE EXTRACT: github.com_CodelyTV_typescript-api-skeleton_2344cdbf
> **Extracted on:** 2026-04-01 09:36:00
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520296/github.com_CodelyTV_typescript-api-skeleton_2344cdbf

---

## File: `.eslintrc.js`
```javascript
module.exports = {
	extends: ["eslint-config-codely/typescript"],
	overrides: [
		{
			files: ["*.ts", "*.tsx"],
			parserOptions: {
				project: ["./tsconfig.json"],
			},
		},
	],
};
```

## File: `.gitignore`
```
# API keys and secrets
.env

# Dependency directory
node_modules

# Ignore built ts files
dist
```

## File: `jest.config.js`
```javascript
module.exports = {
	testEnvironment: "node",
	moduleFileExtensions: ["ts", "js"],
	testMatch: ["**/test/**/*.spec.(ts|js)"],
	transform: {
		"^.+\\.(ts|tsx)$": [
			"ts-jest",
			{
				tsconfig: "tsconfig.json",
			},
		],
	},
};
```

## File: `package.json`
```json
{
  "name": "typescript-api-skeleton",
  "version": "1.0.1",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node ./dist/src/server.js",
    "dev": "ts-node-dev ./src/server.ts",
    "build": "tsc",
    "lint": "eslint --ignore-path .gitignore . --ext .ts",
    "lint:fix": "npm run lint -- --fix",
    "test": "jest --verbose"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/express": "^4.17.17",
    "@types/jest": "^29.5.3",
    "@types/node": "^20.4.7",
    "@types/supertest": "^2.0.12",
    "eslint": "^8.46.0",
    "eslint-config-codely": "^3.0.0",
    "eslint-plugin-jest": "^27.2.3",
    "jest": "^29.6.2",
    "prettier": "^3.0.1",
    "supertest": "^6.3.3",
    "ts-jest": "^29.1.1",
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.1.6"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

## File: `readme.md`
```markdown
# TypeScript Express API Bootstrap (base / project starter)

This is a repository intended to serve as a starting point if you want to bootstrap a express API project in TypeScript.

## Features

- [TypeScript](https://www.typescriptlang.org/) (v4)
- [ts-node-dev](https://github.com/wclr/ts-node-dev)
- [Prettier](https://prettier.io/)
- [ESLint](https://eslint.org/) with:
  - [Codely's config](https://github.com/lydell/eslint-plugin-simple-import-sort/) (includes ESLint's recommended rules, Prettier, Import plugin and more)
  - [Jest plugin](https://www.npmjs.com/package/eslint-plugin-jest)
- [Jest](https://jestjs.io) with [DOM Testing Library](https://testing-library.com/brain/knowledge/docs_legacy/dom-testing-library/intro)
- [GitHub Action workflows](https://github.com/features/actions) set up to run tests and linting on push

## Running the app

```
# install dependencies
npm install

# run in dev mode on port 3000
npm run dev

# generate production build
npm run build

# run generated content in dist folder on port 3000
npm run start
```

## Testing

### Jest with supertest

```
npm run test
```

## Linting

```
# run linter
npm run lint

# fix lint issues
npm run lint:fix
```
```

## File: `tsconfig.json`
```json
  {
    "compilerOptions": {
      "module": "commonjs",
      "esModuleInterop": true,
      "allowSyntheticDefaultImports": true,
      "target": "es6",
      "strict": true,
      "moduleResolution": "node",
      "sourceMap": true,
      "outDir": "dist",
      "resolveJsonModule": true
    },
    "include": [
      "src/**/*",
      "test/**/*",
    ]
  }
```

## File: `data/courses.json`
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

## File: `src/app.ts`
```typescript
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

## File: `src/server.ts`
```typescript
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

## File: `src/controllers/api.ts`
```typescript
import { Application, Request, Response } from "express";

import CoursesData from "../../data/courses.json";

export const loadApiEndpoints = (app: Application): void => {
	app.get("/api", (req: Request, res: Response) => {
		return res.status(200).send(CoursesData);
	});
};
```

## File: `test/api.spec.ts`
```typescript
import request from "supertest";

import app from "../src/app";

describe("GET /api", () => {
	it("should return 200 OK", () => {
		return request(app).get("/api").expect(200);
	});
});
```

