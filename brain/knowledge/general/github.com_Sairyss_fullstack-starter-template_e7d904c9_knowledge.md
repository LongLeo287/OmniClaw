---
id: github.com-sairyss-fullstack-starter-template-e7d9
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:18.760161
---

# KNOWLEDGE EXTRACT: github.com_Sairyss_fullstack-starter-template_e7d904c9
> **Extracted on:** 2026-04-01 10:57:41
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521127/github.com_Sairyss_fullstack-starter-template_e7d904c9

---

## File: `.editorconfig`
```
# Editor configuration, see http://editorconfig.org
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
max_line_length = off
trim_trailing_whitespace = false
```

## File: `.env.example`
```
# Backend

DATABASE_URL="postgresql://user:password@localhost:5432/my_app?schema=public"

NODE_ENV=local
APP_PORT=3000
API_PREFIX='/trpc'

SECRET_KEY=secret
JWT_EXPIRES_IN='7d'

###

# Frontend
VITE_APP_URL="http://localhost:3000/trpc"

###
```

## File: `.eslintignore`
```
node_modules
```

## File: `.eslintrc.json`
```json
{
  "root": true,
  "ignorePatterns": ["**/*"],
  "plugins": ["@nx"],
  "overrides": [
    {
      "files": ["*.ts", "*.tsx", "*.js", "*.jsx"],
      "rules": {
        "@nx/enforce-module-boundaries": [
          "error",
          {
            "enforceBuildableLibDependency": true,
            "allow": [],
            "depConstraints": [
              {
                "sourceTag": "*",
                "onlyDependOnLibsWithTags": ["*"]
              }
            ]
          }
        ]
      }
    },
    {
      "files": ["*.ts", "*.tsx"],
      "extends": ["plugin:@nx/typescript"],
      "rules": {}
    },
    {
      "files": ["*.js", "*.jsx"],
      "extends": ["plugin:@nx/javascript"],
      "rules": {}
    },
    {
      "files": ["*.spec.ts", "*.spec.tsx", "*.spec.js", "*.spec.jsx"],
      "env": {
        "jest": true
      },
      "rules": {}
    }
  ],
  "extends": [
    "plugin:storybook/recommended"
  ]
}
```

## File: `.gitignore`
```
# See http://help.github.com/ignore-files/ for more about ignoring files.

# compiled output
dist
tmp
/out-tsc

# dependencies
node_modules

# IDEs and editors
/.idea
.project
.classpath
.c9/
*.launch
.settings/
*.sublime-workspace

# IDE - VSCode
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

# misc
/.sass-cache
/connect.lock
/coverage
/libpeerconnection.log
npm-debug.log
yarn-error.log
testem.log
/typings

# System Files
.DS_Store
Thumbs.db

# Env files
.env

.nx/cache
```

## File: `.prettierignore`
```
# Add files here to ignore them from prettier formatting

/dist
/coverage

/.nx/cache
```

## File: `.prettierrc`
```
{
  "singleQuote": true
}
```

## File: `README.md`
```markdown
# Full stack starter template

Monorepository TypeScript template for full stack applications.

- Maximized for productivity
- Based on cutting edge technologies
- Follows best practices for project structure, architecture, security
- Includes authentication module

## Libraries/frameworks

This template includes a bunch of libraries to get you up and running quickly and improve your developer experience.

### Frontend

- [React](https://reactjs.org/) - main frontend library
- [Vite](https://vitejs.dev/) - modern and fast build tool
- [React Query](https://react-query-v3.tanstack.com/) - react hooks to facilitate fetching/updating/caching data on the server
- [Zustand](https://github.com/pmndrs/zustand) - easy state-management
- [React router](https://reactrouter.com/en/main) - for routing
- [Cypress](https://www.cypress.io/) - end-to-end testing for your frontend
- [Storybook](https://storybook.js.org/) - build your UI web components in isolation

#### Frontend UI

- [ChakraUI](https://chakra-ui.com/) - UI library that lets you create beautiful interfaces quickly
- [Framer Motion](https://www.framer.com/motion/) - create beautiful motion animations ([compatible with ChakraUI](https://chakra-ui.com/getting-started/with-framer))
- [React Icons](https://react-icons.github.io/react-icons/) - icons for your app
- [React-toastify](https://fkhadra.github.io/react-toastify/introduction) - show notifications when something happens

### Backend

- [Fastify](https://www.fastify.io/) - fast web framework for NodeJS
- [Prisma](https://www.prisma.io/) - new generation ORM for working with relational databases
- [Zod](https://github.com/colinhacks/zod) - TypeScript-first schema validation with static type inference
- [dotenv](https://www.npmjs.com/package/dotenv) - to load your configs from an .env file
- [env-var](https://www.npmjs.com/package/env-var) - validate and sanitize your environmental variables

### Shared libraries

- [tRPC](https://trpc.io/) - Remote Procedure Calls for your TypeScript applications. Move faster by removing the need of a traditional API-layer.
- [NX](https://nx.dev/) - build system with first class monorepo support and powerful integrations
- [Jest](https://jestjs.io/) - testing framework
- [Eslint](https://eslint.org/) - static code analysis for identifying problematic patterns found in your code

## Starting the app

- Clone the repository
- Copy `.env.example` and rename to `.env`
- `npm run docker:env` - setup the database (postgresql) in docker
- `npm install` - install dependencies
- `npm run migrate:dev` - run migrations to create tables
- `npm run backend:dev` - run backend
- `npm run frontend:dev` - run frontend

## Scripts

- `npm run frontend:storybook` - start storybook to develop components in isolation
- `npm run dep-graph` - see dependency graph
- For more commands check `package.json`
- To generate new apps in the monorepo, check out [NX documentation](https://nx.dev/packages/nx/documents/generate).

## Check out my other repositories

- [Domain-Driven Hexagon](https://github.com/Sairyss/domain-driven-hexagon) - Guide on Domain-Driven Design, software architecture, design patterns, best practices etc.
- [Backend best practices](https://github.com/Sairyss/backend-best-practices) - Best practices, tools and guidelines for backend development.
- [System Design Patterns](https://github.com/Sairyss/system-design-patterns) - list of topics and resources related to distributed systems, system design, microservices, scalability and performance, etc.
```

## File: `babel.config.json`
```json
{
  "babelrcRoots": ["*"]
}
```

## File: `jest.config.ts`
```typescript
import { getJestProjects } from '@nx/jest';

export default {
  projects: getJestProjects(),
};
```

## File: `jest.preset.js`
```javascript
const nxPreset = require('@nx/jest/preset').default;

module.exports = {
  ...nxPreset,
  /* TODO: Update to latest Jest snapshotFormat
   * By default Nx has kept the older style of Jest Snapshot formats
   * to prevent breaking of any existing tests with snapshots.
   * It's recommend you update to the latest format.
   * You can do this by removing snapshotFormat property
   * and running tests with --update-snapshot flag.
   * Example: "nx affected --targets=test --update-snapshot"
   * More info: https://jestjs.io/docs/upgrading-to-jest29#snapshot-format
   */
  snapshotFormat: { escapeString: true, printBasicPrototype: true },
};
```

## File: `nx.json`
```json
{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"],
      "cache": true
    },
    "e2e": {
      "inputs": ["default", "^production"],
      "cache": true
    },
    "lint": {
      "inputs": ["default", "{workspaceRoot}/.eslintrc.json"],
      "cache": true
    },
    "test": {
      "inputs": ["default", "^production", "{workspaceRoot}/jest.preset.js"],
      "cache": true
    },
    "build-storybook": {
      "inputs": [
        "default",
        "^production",
        "{workspaceRoot}/.storybook/**/*",
        "{projectRoot}/.storybook/**/*",
        "{projectRoot}/tsconfig.storybook.json"
      ],
      "cache": true
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": [
      "default",
      "!{projectRoot}/.eslintrc.json",
      "!{projectRoot}/**/?(*.)+(spec|test).[jt]s?(x)?(.snap)",
      "!{projectRoot}/tsconfig.spec.json",
      "!{projectRoot}/jest.config.[jt]s",
      "!{projectRoot}/.storybook/**/*",
      "!{projectRoot}/**/*.stories.@(js|jsx|ts|tsx|mdx)",
      "!{projectRoot}/tsconfig.storybook.json",
      "!{projectRoot}/src/test-setup.[jt]s"
    ],
    "sharedGlobals": ["{workspaceRoot}/babel.config.json"]
  },
  "generators": {
    "@nx/react": {
      "application": {
        "style": "css",
        "linter": "eslint",
        "bundler": "webpack",
        "babel": true
      },
      "component": {
        "style": "css"
      },
      "library": {
        "style": "css",
        "linter": "eslint"
      }
    }
  }
}
```

## File: `package.json`
```json
{
  "name": "my-monorepo",
  "version": "0.0.0",
  "license": "MIT",
  "scripts": {
    "nx": "nx",
    "test": "npx nx run-many --all --target=test --parallel",
    "start:frontend": "nx run frontend:serve",
    "build:frontend": "nx run frontend:build",
    "test:frontend": "nx run frontend:test",
    "start:api": "nx run api:serve",
    "start:dev": "nx run-many --parallel --target=serve --projects=backend,frontend",
    "build:api": "nx run api:build",
    "test:api": "nx run api:test",
    "lint": "nx workspace-lint && npx nx run-many --all --target=lint --parallel",
    "e2e": "nx e2e client-e2e",
    "e2e:affected": "nx e2e client-e2e",
    "affected:apps": "nx affected:apps",
    "affected:libs": "nx affected:libs",
    "affected:build": "nx affected:build",
    "affected:e2e": "nx affected:e2e",
    "affected:test": "nx affected:test",
    "affected:lint": "nx affected:lint",
    "affected:dep-graph": "nx affected:dep-graph",
    "dep-graph": "nx dep-graph",
    "affected": "nx affected",
    "format": "nx format:write",
    "format:write": "nx format:write",
    "format:check": "nx format:check",
    "backend:dev": "nx run backend:serve",
    "frontend:dev": "nx run frontend:serve",
    "frontend:storybook": "nx run frontend:storybook",
    "migrate:dev": "prisma migrate dev",
    "docker:env": "docker compose --file docker/docker-compose.yaml up --build"
  },
  "private": true,
  "devDependencies": {
    "@babel/core": "^7.23.2",
    "@babel/preset-react": "^7.22.15",
    "@babel/preset-typescript": "7.23.2",
    "@chakra-ui/storybook-addon": "^5.0.1",
    "@nrwl/js": "17.0.2",
    "@nx/cypress": "17.0.2",
    "@nx/esbuild": "17.0.2",
    "@nx/eslint": "17.0.2",
    "@nx/eslint-plugin": "17.0.2",
    "@nx/jest": "17.0.2",
    "@nx/node": "17.0.2",
    "@nx/react": "17.0.2",
    "@nx/storybook": "17.0.2",
    "@nx/vite": "17.0.2",
    "@nx/web": "17.0.2",
    "@nx/workspace": "17.0.2",
    "@pmmmwh/react-refresh-webpack-plugin": "^0.5.11",
    "@storybook/addon-essentials": "7.5.1",
    "@storybook/core-common": "^7.5.1",
    "@storybook/core-server": "7.5.1",
    "@storybook/react": "7.5.1",
    "@storybook/react-vite": "^7.5.1",
    "@svgr/webpack": "^8.1.0",
    "@testing-library/react": "14.0.0",
    "@types/bcryptjs": "^2.4.5",
    "@types/jest": "29.5.6",
    "@types/jsonwebtoken": "^9.0.4",
    "@types/node": "18.14.2",
    "@types/react": "18.2.33",
    "@types/react-dom": "18.2.14",
    "@types/react-router-dom": "5.3.3",
    "@typescript-eslint/eslint-plugin": "6.9.0",
    "@typescript-eslint/parser": "6.9.0",
    "@vitejs/plugin-react": "4.1.0",
    "@vitest/coverage-c8": "0.31.4",
    "@vitest/ui": "0.34.6",
    "babel-jest": "29.7.0",
    "babel-loader": "9.1.3",
    "cypress": "^13.3.3",
    "esbuild": "0.19.5",
    "eslint": "8.52.0",
    "eslint-config-prettier": "9.0.0",
    "eslint-plugin-cypress": "2.15.1",
    "eslint-plugin-import": "2.29.0",
    "eslint-plugin-jsx-a11y": "6.7.1",
    "eslint-plugin-react": "7.33.2",
    "eslint-plugin-react-hooks": "4.6.0",
    "eslint-plugin-storybook": "^0.6.15",
    "html-webpack-plugin": "^5.5.3",
    "jest": "29.7.0",
    "jest-environment-jsdom": "29.7.0",
    "jsdom": "22.1.0",
    "nx": "17.0.2",
    "prettier": "^3.0.3",
    "prisma": "^5.5.2",
    "react-refresh": "^0.14.0",
    "ts-jest": "29.1.1",
    "ts-node": "10.9.1",
    "typescript": "5.2.2",
    "url-loader": "^4.1.1",
    "vite": "4.5.0",
    "vite-plugin-eslint": "^1.8.1",
    "vite-tsconfig-paths": "^4.2.1",
    "vitest": "0.34.6"
  },
  "dependencies": {
    "@chakra-ui/icons": "^2.1.1",
    "@chakra-ui/react": "^2.8.1",
    "@emotion/react": "11.11.1",
    "@emotion/styled": "11.11.0",
    "@fastify/cors": "^8.4.0",
    "@prisma/client": "^5.5.2",
    "@tanstack/react-query": "^4.36.1",
    "@trpc/client": "^10.43.0",
    "@trpc/next": "^10.43.0",
    "@trpc/react-query": "^10.43.0",
    "@trpc/server": "^10.43.0",
    "bcryptjs": "^2.4.3",
    "env-var": "^7.4.1",
    "fastify": "^4.24.3",
    "framer-motion": "^10.16.4",
    "jsonwebtoken": "^9.0.2",
    "pino-pretty": "^10.2.3",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-hook-form": "^7.47.0",
    "react-icons": "^4.11.0",
    "react-router-dom": "6.17.0",
    "react-toastify": "^9.1.3",
    "superjson": "^2.2.0",
    "tslib": "^2.6.2",
    "zod": "^3.22.4",
    "zustand": "^4.4.4"
  },
  "prisma": {
    "schema": "apps/backend/prisma/schema.prisma",
    "env": "apps/backend/.env"
  },
  "volta": {
    "node": "18.18.2"
  }
}
```

## File: `tsconfig.base.json`
```json
{
  "compileOnSave": false,
  "compilerOptions": {
    "strict": true,
    "rootDir": ".",
    "sourceMap": true,
    "declaration": false,
    "moduleResolution": "node",
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "importHelpers": true,
    "target": "ES2020",
    "module": "esnext",
    "lib": ["es2017", "dom"],
    "skipLibCheck": true,
    "skipDefaultLibCheck": true,
    "baseUrl": "."
  },
  "exclude": ["node_modules", "tmp"]
}
```

## File: `apps/backend/.eslintrc.json`
```json
{
  "extends": ["../../.eslintrc.json"],
  "ignorePatterns": ["!**/*"],
  "overrides": [
    {
      "files": ["*.ts", "*.tsx", "*.js", "*.jsx"],
      "rules": {}
    },
    {
      "files": ["*.ts", "*.tsx"],
      "rules": {}
    },
    {
      "files": ["*.js", "*.jsx"],
      "rules": {}
    }
  ]
}
```

## File: `apps/backend/.gitignore`
```
node_modules
# Keep environment variables out of version control
.env
```

## File: `apps/backend/jest.config.ts`
```typescript
/* eslint-disable */
export default {
  displayName: 'backend',
  preset: '../../jest.preset.js',
  globals: {},
  testEnvironment: 'node',
  transform: {
    '^.+\\.[tj]s$': [
      'ts-jest',
      {
        tsconfig: '<rootDir>/tsconfig.spec.json',
      },
    ],
  },
  moduleFileExtensions: ['ts', 'js', 'html'],
  coverageDirectory: '../../coverage/apps/backend',
};
```

## File: `apps/backend/project.json`
```json
{
  "name": "backend",
  "$schema": "../../node_modules/nx/schemas/project-schema.json",
  "sourceRoot": "apps/backend/src",
  "projectType": "application",
  "targets": {
    "build": {
      "executor": "@nx/esbuild:esbuild",
      "outputs": ["{options.outputPath}"],
      "options": {
        "outputPath": "dist/apps/backend",
        "format": ["cjs"],
        "main": "apps/backend/src/main.ts",
        "tsConfig": "apps/backend/tsconfig.app.json",
        "assets": ["apps/backend/src/assets"],
        "generatePackageJson": true,
        "thirdParty": true
      }
    },
    "serve": {
      "executor": "@nrwl/js:node",
      "options": {
        "buildTarget": "backend:build"
      },
      "configurations": {
        "production": {
          "buildTarget": "backend:build:production"
        }
      }
    },
    "lint": {
      "executor": "@nx/eslint:lint",
      "outputs": ["{options.outputFile}"],
      "options": {
        "lintFilePatterns": ["apps/backend/**/*.ts"]
      }
    },
    "test": {
      "executor": "@nx/jest:jest",
      "outputs": ["{workspaceRoot}/coverage/{projectRoot}"],
      "options": {
        "jestConfig": "apps/backend/jest.config.ts",
        "passWithNoTests": true
      }
    }
  },
  "tags": []
}
```

## File: `apps/backend/tsconfig.app.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "../../dist/out-tsc",
    "module": "commonjs",
    "types": ["node"],
    "sourceMap": true
  },
  "exclude": ["jest.config.ts", "src/**/*.spec.ts", "src/**/*.test.ts"],
  "include": ["src/**/*.ts"]
}
```

## File: `apps/backend/tsconfig.json`
```json
{
  "extends": "../../tsconfig.base.json",
  "files": [],
  "include": [],
  "references": [
    {
      "path": "./tsconfig.app.json"
    },
    {
      "path": "./tsconfig.spec.json"
    }
  ]
}
```

## File: `apps/backend/tsconfig.spec.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "../../dist/out-tsc",
    "module": "commonjs",
    "types": ["jest", "node"]
  },
  "include": [
    "jest.config.ts",
    "src/**/*.test.ts",
    "src/**/*.spec.ts",
    "src/**/*.d.ts"
  ]
}
```

## File: `apps/backend/prisma/schema.prisma`
```
// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now()) @db.Timestamptz(3)
  updatedAt DateTime @updatedAt @db.Timestamptz(3)
  email     String   @unique @db.VarChar(255)
  role      String   @db.VarChar(255)
  password  String   @db.VarChar(255)
}
```

## File: `apps/backend/prisma/migrations/migration_lock.toml`
```
# Please do not edit this file manually
# It should be added in your version-control system (i.e. Git)
provider = "postgresql"
```

## File: `apps/backend/prisma/migrations/20230123171537_init/migration.sql`
```sql
-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "createdAt" TIMESTAMPTZ(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMPTZ(3) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "role" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");
```

## File: `apps/backend/src/main.ts`
```typescript
import { serverConfig } from './configs/server.config';
import { createServer } from './server/server';

const server = createServer(serverConfig);

server.start();
```

## File: `apps/backend/src/configs/auth.config.ts`
```typescript
import { get } from 'env-var';

export const authConfig = {
  secretKey: get('SECRET_KEY').required().asString(),
  jwtExpiresIn: get('JWT_EXPIRES_IN').required().asString(),
};
```

## File: `apps/backend/src/configs/server.config.ts`
```typescript
import type { ServerOptions } from '../server/server';
import { get } from 'env-var';
import { config } from 'dotenv';
config();

export const serverConfig: ServerOptions = {
  environment: get('NODE_ENV')
    .required()
    .asEnum(['development', 'production', 'test', 'local']),

  port: get('APP_PORT').required().asPortNumber(),
  prefix: get('API_PREFIX').required().asString(),
};
```

## File: `apps/backend/src/modules/auth/auth.dtos.ts`
```typescript
import { z } from 'zod';

export const userCredentialsSchema = z.object({
  email: z
    .string({
      required_error: 'Email is required',
    })
    .email(),
  password: z
    .string({
      required_error: 'Password is required',
    })
    .min(8),
});

export type SignInDto = z.TypeOf<typeof userCredentialsSchema>;
export type SignUpDto = z.TypeOf<typeof userCredentialsSchema>;
```

## File: `apps/backend/src/modules/auth/auth.router.ts`
```typescript
import { noAuthProcedure, router } from '../../server/trpc';
import { userCredentialsSchema } from './auth.dtos';
import { signIn, signUp } from './auth.service';

export const authRouter = router({
  signUp: noAuthProcedure
    .input(userCredentialsSchema)
    .mutation(async ({ input, ctx }) => signUp(input, ctx)),

  signIn: noAuthProcedure
    .input(userCredentialsSchema)
    .mutation(async ({ input, ctx }) => signIn(input, ctx)),
});
```

## File: `apps/backend/src/modules/auth/auth.service.ts`
```typescript
import { User } from '@prisma/client';
import { TRPCError } from '@trpc/server';
import { SignInDto, SignUpDto } from './auth.dtos';
import { sign } from 'jsonwebtoken';
import { authConfig } from '../../configs/auth.config';
import { hash, compare } from 'bcryptjs';
import { Context } from '../../server/context';

type UserResponse = Omit<User, 'password'>;
type SignUpResult = UserResponse & { accessToken: string };

export const signUp = async (
  input: SignUpDto,
  ctx: Context
): Promise<UserResponse> => {
  const bcryptHash = await hash(input.password, 10);

  const user = await ctx.prisma.user.create({
    data: {
      email: input.email,
      password: bcryptHash,
      role: 'user',
    },
  });
  return {
    id: user.id,
    email: user.email,
    createdAt: user.createdAt,
    updatedAt: user.updatedAt,
    role: user.role,
  };
};

export const signIn = async (
  input: SignInDto,
  ctx: Context
): Promise<SignUpResult> => {
  const user = await ctx.prisma.user.findUnique({
    where: {
      email: input.email,
    },
  });

  const error = new TRPCError({
    message: 'Incorrect email or password',
    code: 'UNAUTHORIZED',
  });

  if (!user) {
    throw error;
  }

  const result = await compare(input.password, user.password);

  if (!result) {
    throw error;
  }

  const token = sign(
    {
      id: user.id,
      roles: user.role,
    },
    authConfig.secretKey,
    { expiresIn: authConfig.jwtExpiresIn }
  );

  return {
    id: user.id,
    email: user.email,
    createdAt: user.createdAt,
    updatedAt: user.updatedAt,
    role: user.role,
    accessToken: token,
  };
};
```

## File: `apps/backend/src/server/context.ts`
```typescript
import { inferAsyncReturnType, TRPCError } from '@trpc/server';
import { CreateFastifyContextOptions } from '@trpc/server/adapters/fastify';
import { verify } from 'jsonwebtoken';
import { authConfig } from '../configs/auth.config';
import { PrismaClient } from '@prisma/client';

export const prisma = new PrismaClient();

export interface User {
  email: string;
  role: 'user' | 'admin';
}

async function decodeAndVerifyJwtToken(token: string): Promise<User> {
  const decoded = verify(token, authConfig.secretKey);
  return decoded as User;
}

export async function createContext({ req, res }: CreateFastifyContextOptions) {
  if (req.headers.authorization) {
    try {
      const user = await decodeAndVerifyJwtToken(
        req.headers.authorization.split(' ')[1]
      );
      return { req, res, prisma, user };
    } catch (err) {
      throw new TRPCError({ message: 'Unauthorized', code: 'UNAUTHORIZED' });
    }
  }

  return { req, res, prisma };
}

export type Context = inferAsyncReturnType<typeof createContext>;
```

## File: `apps/backend/src/server/router.ts`
```typescript
import { authRouter } from '../modules/auth/auth.router';
import { router } from './trpc';

export const appRouter = router({
  auth: authRouter,
});

export type AppRouter = typeof appRouter;
```

## File: `apps/backend/src/server/server.ts`
```typescript
import { fastifyTRPCPlugin } from '@trpc/server/adapters/fastify';
import fastify from 'fastify';
import { createContext } from './context';
import { appRouter } from './router';
import cors from '@fastify/cors';
import pretty from 'pino-pretty';
import pino from 'pino';

export interface ServerOptions {
  dev?: boolean;
  port?: number;
  prefix?: string;
  environment: 'development' | 'production' | 'test' | 'local';
}

export function createServer(opts: ServerOptions) {
  const port = opts.port ?? 3000;
  const prefix = opts.prefix ?? '/trpc';

  const stream = pretty({
    colorize: true,
    translateTime: 'HH:MM:ss Z',
    ignore: 'pid,hostname',
  });
  const prettyLogger = pino({ level: 'debug' }, stream);

  const server = fastify({
    logger:
      opts.environment === 'local' || opts.environment === 'test'
        ? prettyLogger
        : true,
  });

  server.register(cors, {
    origin: '*',
    methods: '*',
  });

  server.register(fastifyTRPCPlugin, {
    prefix,
    trpcOptions: { router: appRouter, createContext },
  });

  const stop = () => server.close();
  const start = async () => {
    try {
      await server.listen({ port });
    } catch (err) {
      server.log.error(err);
      process.exit(1);
    }
  };

  return { server, start, stop };
}
```

## File: `apps/backend/src/server/trpc.ts`
```typescript
import { initTRPC, TRPCError } from '@trpc/server';
import superjson from 'superjson';
import { Context } from './context';
export { AppRouter } from './router';

const t = initTRPC.context<Context>().create({
  transformer: superjson,
  errorFormatter({ shape, error, ctx }) {
    if (error.code === 'INTERNAL_SERVER_ERROR') {
      ctx?.req.log.error(error);
      return { ...shape, message: 'Internal server error' };
    }
    return shape;
  },
});

const isAuthenticated = t.middleware(({ next, ctx }) => {
  if (!ctx.user) {
    throw new TRPCError({ message: 'Unauthorized', code: 'UNAUTHORIZED' });
  }
  return next({
    ctx: {
      user: ctx.user,
    },
  });
});

const isAdmin = t.middleware(({ next, ctx }) => {
  if (!ctx.user || ctx.user.role !== 'admin') {
    throw new TRPCError({ message: 'Unauthorized', code: 'UNAUTHORIZED' });
  }
  return next({
    ctx: {
      user: ctx.user,
    },
  });
});

export const router = t.router;

export const procedure = t.procedure.use(isAuthenticated);
export const noAuthProcedure = t.procedure;
export const adminProcedure = t.procedure.use(isAdmin);
```

## File: `apps/frontend/.eslintrc.json`
```json
{
  "extends": ["plugin:@nx/react", "../../.eslintrc.json"],
  "ignorePatterns": ["!**/*"],
  "overrides": [
    {
      "files": ["*.ts", "*.tsx", "*.js", "*.jsx"],
      "rules": {}
    },
    {
      "files": ["*.ts", "*.tsx"],
      "rules": {}
    },
    {
      "files": ["*.js", "*.jsx"],
      "rules": {}
    }
  ]
}
```

## File: `apps/frontend/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Frontend</title>
    <base href="/" />

    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />
    <link rel="stylesheet" href="/src/styles.css" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## File: `apps/frontend/project.json`
```json
{
  "name": "frontend",
  "$schema": "../../node_modules/nx/schemas/project-schema.json",
  "sourceRoot": "apps/frontend/src",
  "projectType": "application",
  "targets": {
    "build": {
      "executor": "@nx/vite:build",
      "outputs": ["{options.outputPath}"],
      "defaultConfiguration": "production",
      "options": {
        "outputPath": "dist/apps/frontend"
      },
      "configurations": {
        "development": {
          "mode": "development"
        },
        "production": {
          "mode": "production"
        }
      }
    },
    "serve": {
      "executor": "@nx/vite:dev-server",
      "defaultConfiguration": "development",
      "options": {
        "buildTarget": "frontend:build"
      },
      "configurations": {
        "development": {
          "buildTarget": "frontend:build:development",
          "hmr": true
        },
        "production": {
          "buildTarget": "frontend:build:production",
          "hmr": false
        }
      }
    },
    "test": {
      "executor": "@nx/vite:test",
      "outputs": ["{workspaceRoot}/coverage/apps/frontend"],
      "options": {
        "passWithNoTests": true,
        "reportsDirectory": "../../coverage/apps/frontend"
      }
    },
    "lint": {
      "executor": "@nx/eslint:lint",
      "outputs": ["{options.outputFile}"],
      "options": {
        "lintFilePatterns": ["apps/frontend/**/*.{ts,tsx,js,jsx}"]
      }
    },
    "storybook": {
      "executor": "@nx/storybook:storybook",
      "options": {
        "port": 4400,
        "configDir": "apps/frontend/.storybook"
      },
      "configurations": {
        "ci": {
          "quiet": true
        }
      }
    },
    "build-storybook": {
      "executor": "@nx/storybook:build",
      "outputs": ["{options.outputDir}"],
      "options": {
        "outputDir": "dist/storybook/frontend",
        "configDir": "apps/frontend/.storybook"
      },
      "configurations": {
        "ci": {
          "quiet": true
        }
      }
    }
  },
  "tags": []
}
```

## File: `apps/frontend/tsconfig.app.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "../../dist/out-tsc",
    "types": [
      "node",
      "@nx/react/typings/cssmodule.d.ts",
      "@nx/react/typings/image.d.ts"
    ],
    "paths": {
      "@utils/*": ["apps/frontend/src/utils/*"],
      "@GlobalState": ["apps/frontend/src/app/GlobalState.ts"]
    }
  },
  "files": [
    "../../node_modules/@nx/react/typings/cssmodule.d.ts",
    "../../node_modules/@nx/react/typings/image.d.ts"
  ],
  "exclude": [
    "src/**/*.spec.ts",
    "src/**/*.test.ts",
    "src/**/*.spec.tsx",
    "src/**/*.test.tsx",
    "src/**/*.spec.js",
    "src/**/*.test.js",
    "src/**/*.spec.jsx",
    "src/**/*.test.jsx",
    "**/*.stories.ts",
    "**/*.stories.js",
    "**/*.stories.jsx",
    "**/*.stories.tsx"
  ],
  "include": ["src/**/*.js", "src/**/*.jsx", "src/**/*.ts", "src/**/*.tsx"]
}
```

## File: `apps/frontend/tsconfig.json`
```json
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "allowJs": false,
    "esModuleInterop": false,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "types": ["vite/client", "vitest"]
  },
  "files": [],
  "include": [],
  "references": [
    {
      "path": "./tsconfig.app.json"
    },
    {
      "path": "./tsconfig.spec.json"
    },
    {
      "path": "./tsconfig.storybook.json"
    }
  ],
  "extends": "../../tsconfig.base.json"
}
```

## File: `apps/frontend/tsconfig.spec.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "../../dist/out-tsc",
    "types": [
      "vitest/globals",
      "node",
      "@nx/react/typings/cssmodule.d.ts",
      "@nx/react/typings/image.d.ts"
    ]
  },
  "include": [
    "vite.config.ts",
    "src/**/*.test.ts",
    "src/**/*.spec.ts",
    "src/**/*.test.tsx",
    "src/**/*.spec.tsx",
    "src/**/*.test.js",
    "src/**/*.spec.js",
    "src/**/*.test.jsx",
    "src/**/*.spec.jsx",
    "src/**/*.d.ts"
  ],
  "files": [
    "../../node_modules/@nx/react/typings/cssmodule.d.ts",
    "../../node_modules/@nx/react/typings/image.d.ts"
  ]
}
```

## File: `apps/frontend/tsconfig.storybook.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "emitDecoratorMetadata": true,
    "outDir": ""
  },
  "files": [
    "../../node_modules/@nx/react/typings/styled-jsx.d.ts",
    "../../node_modules/@nx/react/typings/cssmodule.d.ts",
    "../../node_modules/@nx/react/typings/image.d.ts"
  ],
  "exclude": [
    "src/**/*.spec.ts",
    "src/**/*.spec.js",
    "src/**/*.spec.tsx",
    "src/**/*.spec.jsx"
  ],
  "include": [
    "src/**/*.stories.ts",
    "src/**/*.stories.js",
    "src/**/*.stories.jsx",
    "src/**/*.stories.tsx",
    "src/**/*.stories.mdx",
    ".storybook/*.ts",
    ".storybook/*.js"
  ]
}
```

## File: `apps/frontend/vite.config.ts`
```typescript
/// <reference types="vitest" />
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { nxViteTsPaths } from '@nx/vite/plugins/nx-tsconfig-paths.plugin';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  server: {
    port: 4200,
    host: 'localhost',
  },
  plugins: [
    react(),
    tsconfigPaths({ projects: ['./tsconfig.app.json']}),
    nxViteTsPaths(),
  ],

  // Uncomment this if you are using workers.
  // worker: {
  //  plugins: [
  //    viteTsConfigPaths({
  //      root: '../../',
  //    }),
  //  ],
  // },

  test: {
    globals: true,
    cache: {
      dir: '../../node_modules/.vitest',
    },
    environment: 'jsdom',
    include: ['src/**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}'],
  },
});
```

## File: `apps/frontend/src/env.d.ts`
```typescript
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_URL: string;
  // more .env variables...
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## File: `apps/frontend/src/main.tsx`
```tsx
import './styles.css';

import { StrictMode } from 'react';
import * as ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './app/app';
import { ChakraProvider, ColorModeScript } from '@chakra-ui/react';
import theme from './theme';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <StrictMode>
    <ColorModeScript initialColorMode={theme.config.initialColorMode} />
    <ChakraProvider theme={theme}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </ChakraProvider>
  </StrictMode>
);
```

## File: `apps/frontend/src/styles.css`
```css
/* You can add global styles to this file, and also import other style files */
:root {
  --bg-color-primary: #171922;
  --bg-color-secondary: #1e2028;

  color-scheme: light dark;

}

```

## File: `apps/frontend/src/theme.ts`
```typescript
import { extendTheme, type ThemeConfig } from '@chakra-ui/react';
import type { Styles } from '@chakra-ui/theme-tools';

// 2. Add your color mode config
const config: ThemeConfig = {
  initialColorMode: 'dark',
  useSystemColorMode: false,
};

const styles: Styles = {
  global: (props) => ({
    body: {
      // bg: mode('default', 'var(--bg-color-primary)')(props),
    },
  }),
};

const components = {
  // custom style for chakraui components
};

// 3. extend the theme
const theme = extendTheme({
  config,
  styles,
  components,
});

export default theme;
```

## File: `apps/frontend/src/app/GlobalState.ts`
```typescript
import { create } from 'zustand';

export type User = {
  username: string;
  role: string;
  avatarUrl: string;
};

export type GlobalState = {
  user?: User;

  signIn: (user: User) => void;
  signOut: () => void;
};

export const useGlobalStateStore = create<GlobalState>((set) => ({
  user: undefined,

  signIn: (user: User) => set((prevState) => ({ ...prevState, user })),
  signOut: () => set((prevState) => ({ ...prevState, user: undefined })),
}));
```

## File: `apps/frontend/src/app/app.module.css`
```css
/* Your styles goes here. */
```

## File: `apps/frontend/src/app/app.tsx`
```tsx
import { Route, Routes } from 'react-router-dom';
import SidebarWithHeader from '../components/SidebarWithHeader/SidebarWithHeader';
import { QueryClientProvider } from '@tanstack/react-query';
import { trpc } from '../utils/trpc';
import SignUpCard from '../components/Auth/SignUpCard/SignUpCard';
import SignInCard from '../components/Auth/SignInCard/SignInCard';
import { useQueryTrpcClient } from './useQueryClient';
import AuthVerify from '../components/Auth/AuthVerify';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Home from '../pages/Home';
import { Box } from '@chakra-ui/react';

export function App() {
  const { queryClient, trpcClient } = useQueryTrpcClient();
  return (
    <trpc.Provider client={trpcClient} queryClient={queryClient}>
      <ToastContainer
        position="bottom-right"
        autoClose={3000}
        theme="colored"
        hideProgressBar
        closeOnClick
      />
      <QueryClientProvider client={queryClient}>
        <AuthVerify />
        <SidebarWithHeader>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/sign-up" element={<SignUpCard />} />
            <Route path="/login" element={<SignInCard />} />
            <Route path="*" element={<Box>Not Found</Box>} />
          </Routes>
        </SidebarWithHeader>
      </QueryClientProvider>
    </trpc.Provider>
  );
}

export default App;
```

## File: `apps/frontend/src/app/useQueryClient.ts`
```typescript
import SuperJSON from 'superjson';
import { useState } from 'react';
import { QueryClient } from '@tanstack/react-query';
import { httpBatchLink } from '@trpc/client';
import { trpc } from '../utils/trpc';

export const useQueryTrpcClient = () => {
  const APP_URL = import.meta.env.VITE_APP_URL;
  if (!APP_URL) throw new Error('No app url env variable found');

  const [queryClient] = useState(() => new QueryClient());
  const [trpcClient] = useState(() =>
    trpc.createClient({
      links: [
        httpBatchLink({
          url: APP_URL,
          headers() {
            const userJson = localStorage.getItem('user');
            if (userJson) {
              const user = JSON.parse(userJson);
              if (user?.accessToken) {
                return {
                  authorization: `Bearer ${user?.accessToken}`,
                };
              }
            }
            return {};
          },
        }),
      ],
      transformer: SuperJSON,
    })
  );

  return { queryClient, trpcClient };
};
```

## File: `apps/frontend/src/components/Auth/AuthVerify.tsx`
```tsx
import { useGlobalStateStore } from '@GlobalState';
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { toast } from 'react-toastify';

const parseJwt = (token: string) => {
  try {
    return JSON.parse(atob(token.split('.')[1]));
  } catch (e) {
    return null;
  }
};

const AuthVerify = () => {
  const location = useLocation();
  const state = useGlobalStateStore((state) => state);

  useEffect(() => {
    if (state.user) return;
    const userJson = localStorage.getItem('user');
    if (userJson) {
      const user = JSON.parse(userJson);
      if (user?.accessToken && user?.username && user?.role) {
        state.signIn(user);
      }
    }
  }, [state]);

  // Check token expiration
  useEffect(() => {
    const userJson = localStorage.getItem('user');
    if (!userJson) return;
    const user = JSON.parse(userJson);
    if (user && user.accessToken) {
      const decodedJwt = parseJwt(user.accessToken);
      if (decodedJwt.exp * 1000 < Date.now()) {
        localStorage.removeItem('user');
        toast.warning('Your token expired');
        state.signOut();
      }
    }
  }, [location, state]);

  return <span style={{ position: 'absolute' }}></span>;
};

export default AuthVerify;
```

## File: `apps/frontend/src/components/Auth/AuthHeader/AuthHeader.stories.tsx`
```tsx
import { ChakraProvider, theme } from '@chakra-ui/react';
import { Story, Meta } from '@storybook/react';
import { BrowserRouter } from 'react-router-dom';
import AuthHeaderUI, { AuthHeaderProps } from './AuthHeaderUI';

export default {
  component: AuthHeaderUI,
  title: 'AuthHeaderUI',
} as Meta;

const Template: Story<AuthHeaderProps> = (args) => (
  <ChakraProvider theme={theme}>
    <BrowserRouter>
      <AuthHeaderUI {...args} />
    </BrowserRouter>
  </ChakraProvider>
);

export const Primary = Template.bind({});
Primary.args = {
  user: {
    username: 'user@gmail.com',
    role: 'admin',
    avatarUrl:
      'https://images.unsplash.com/photo-1619946794135-5bc917a27793?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=b616b2c5b373a80ffc9636ba24f7a4a9',
  },
};
```

## File: `apps/frontend/src/components/Auth/AuthHeader/AuthHeader.tsx`
```tsx
import { useGlobalStateStore } from '@GlobalState';
import AuthHeaderUI from './AuthHeaderUI';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';

const AuthHeader = () => {
  const state = useGlobalStateStore((state) => state);
  const navigate = useNavigate();

  const handleSignOut = () => {
    state.signOut();
    localStorage.removeItem('user');
    toast.info('Signed out');
    navigate('/');
  };

  return <AuthHeaderUI user={state.user} handleSignOut={handleSignOut} />;
};

export default AuthHeader;
```

## File: `apps/frontend/src/components/Auth/AuthHeader/AuthHeaderUI.tsx`
```tsx
import {
  Avatar,
  Box,
  Button,
  Flex,
  HStack,
  Menu,
  MenuButton,
  MenuDivider,
  MenuItem,
  MenuList,
  Text,
  VStack,
} from '@chakra-ui/react';
import { FiChevronDown } from 'react-icons/fi';
import { useNavigate } from 'react-router-dom';

export type User = {
  username: string;
  role: string;
  avatarUrl: string;
};

export type AuthHeaderProps = {
  user?: User;
  handleSignOut: () => void;
};

const AuthHeaderUI = (props: AuthHeaderProps) => {
  const navigate = useNavigate();
  return (
    <HStack position={'relative'} spacing={{ base: '0', md: '6' }}>
      <Flex alignItems={'center'}>
        {props.user ? (
          <Menu>
            <MenuButton
              py={2}
              transition="all 0.3s"
              _focus={{ boxShadow: 'none' }}
            >
              <HStack>
                <Avatar size={'xs'} src={props.user.avatarUrl} />
                <VStack
                  display={{ base: 'none', md: 'flex' }}
                  alignItems="flex-start"
                  spacing="1px"
                  ml="2"
                >
                  <Text fontSize="sm">{props.user.username}</Text>
                  <Text fontSize="xs" color="gray.600">
                    {props.user.role}
                  </Text>
                </VStack>
                <Box display={{ base: 'none', md: 'flex' }}>
                  <FiChevronDown />
                </Box>
              </HStack>
            </MenuButton>
            <MenuList>
              <MenuItem>Profile</MenuItem>
              <MenuItem>Settings</MenuItem>
              <MenuDivider />
              <MenuItem onClick={props.handleSignOut}>Sign out</MenuItem>
            </MenuList>
          </Menu>
        ) : (
          <Flex gap={2}>
            <Button onClick={() => navigate('/sign-up')}>Sign up</Button>
            <Button onClick={() => navigate('/login')}>Sign in</Button>
          </Flex>
        )}
      </Flex>
    </HStack>
  );
};

export default AuthHeaderUI;
```

## File: `apps/frontend/src/components/Auth/SignInCard/SignInCard.tsx`
```tsx
import { useGlobalStateStore } from '@GlobalState';
import { trpc } from '@utils/trpc';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { EmailAndPassword } from '../SignUpCard/SignUpCardUI';
import SignInCardUI from './SignInCardUI';

const SignInCard = () => {
  const state = useGlobalStateStore((state) => state);
  const navigate = useNavigate();

  const [rememberMe, setRememberMe] = useState(false);
  const handleRememberMe = (value: boolean) => {
    setRememberMe(value);
  };

  const signInMutation = trpc.auth.signIn.useMutation({
    onSuccess({ email, role, accessToken }) {
      const avatarUrl =
        'https://images.unsplash.com/photo-1619946794135-5bc917a27793?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=b616b2c5b373a80ffc9636ba24f7a4a9';
      const user = {
        username: email,
        role: role,
        avatarUrl,
      };
      state.signIn(user);
      toast.info('Signed in');

      if (rememberMe) {
        localStorage.setItem('user', JSON.stringify({ ...user, accessToken }));
      }
      navigate('/');
    },
    onError(error) {
      toast.error(error.message);
    },
  });
  const onSubmit = (values: EmailAndPassword) => {
    signInMutation.mutate(values);
  };

  return (
    <SignInCardUI
      onSubmit={onSubmit}
      rememberMe={rememberMe}
      handleRememberMe={handleRememberMe}
    />
  );
};

export default SignInCard;
```

## File: `apps/frontend/src/components/Auth/SignInCard/SignInCardUI.tsx`
```tsx
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  Checkbox,
  Stack,
  Link,
  Button,
  Heading,
  Text,
  useColorModeValue,
} from '@chakra-ui/react';
import { useForm } from 'react-hook-form';
import { EmailAndPassword } from '../SignUpCard/SignUpCardUI';

type SignInCardProps = {
  rememberMe: boolean;
  onSubmit(values: EmailAndPassword): void;
  handleRememberMe(value: boolean): void;
};

function SignInCardUI({
  onSubmit,
  rememberMe,
  handleRememberMe,
}: SignInCardProps) {
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
  } = useForm<EmailAndPassword>();

  return (
    <Flex
      minH={'100%'}
      align={'center'}
      justify={'center'}
      bg={useColorModeValue('gray.50', 'gray.800')}
    >
      <Stack spacing={8} mx={'auto'} maxW={'lg'} minW={'450px'} py={12} px={6}>
        <Stack align={'center'}>
          <Heading fontSize={'4xl'}>Sign in to your account</Heading>
          <Text fontSize={'lg'} color={'gray.600'}>
            to enjoy all of our cool features{' '}
            <span role="img" aria-label="peace-emoji">
              ✌️
            </span>
          </Text>
        </Stack>
        <Box
          rounded={'lg'}
          bg={useColorModeValue('white', 'gray.700')}
          boxShadow={'lg'}
          p={8}
        >
          <form onSubmit={handleSubmit(onSubmit)}>
            <Stack spacing={4}>
              <FormControl>
                <FormLabel>Email address</FormLabel>
                <Input
                  id="email"
                  type="email"
                  {...register('email', {
                    required: 'Email is required',
                  })}
                />
              </FormControl>
              <FormControl>
                <FormLabel>Password</FormLabel>
                <Input
                  id="password"
                  type="password"
                  {...register('password', {
                    required: 'Password is required',
                  })}
                />
              </FormControl>
              <Stack spacing={10}>
                <Stack
                  direction={{ base: 'column', sm: 'row' }}
                  align={'start'}
                  justify={'space-between'}
                >
                  <Checkbox
                    isChecked={rememberMe}
                    onChange={(e) => handleRememberMe(e.target.checked)}
                  >
                    Remember me
                  </Checkbox>
                  <Link color={'blue.400'}>Forgot password?</Link>
                </Stack>
                <Button
                  bg={'blue.400'}
                  isLoading={isSubmitting}
                  color={'white'}
                  type={'submit'}
                  _hover={{
                    bg: 'blue.500',
                  }}
                >
                  Sign in
                </Button>
              </Stack>
            </Stack>
          </form>
        </Box>
      </Stack>
    </Flex>
  );
}

export default SignInCardUI;
```

## File: `apps/frontend/src/components/Auth/SignUpCard/SignUpCard.stories.tsx`
```tsx
import { ChakraProvider, theme } from '@chakra-ui/react';
import { Story, Meta } from '@storybook/react';
import SignUpCardUI from './SignUpCardUI';
import { BrowserRouter } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default {
  component: SignUpCardUI,
  title: 'SignUpCardUI',
} as Meta;

const Template: Story = (args) => {
  const handleOnSubmit = () => {
    //
  };
  return (
    <ChakraProvider theme={theme}>
      <ToastContainer
        position="bottom-right"
        autoClose={3000}
        theme="colored"
        hideProgressBar
        closeOnClick
      />
      <BrowserRouter>
        <SignUpCardUI onSubmit={handleOnSubmit} {...args} />
      </BrowserRouter>
    </ChakraProvider>
  );
};

export const Primary = Template.bind({});
Primary.args = {};
```

## File: `apps/frontend/src/components/Auth/SignUpCard/SignUpCard.tsx`
```tsx
import { trpc } from '@utils/trpc';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import SignUpCardUI, { EmailAndPassword } from './SignUpCardUI';

const SignUpCard = () => {
  const navigate = useNavigate();

  const signUpMutation = trpc.auth.signUp.useMutation({
    onSuccess({ email, role }) {
      toast.info('Success!');
      navigate('/login');
    },
    onError(error) {
      toast.error(error.message);
    },
  });
  const onSubmit = (values: EmailAndPassword) => {
    signUpMutation.mutate(values);
  };
  return <SignUpCardUI onSubmit={onSubmit} />;
};

export default SignUpCard;
```

## File: `apps/frontend/src/components/Auth/SignUpCard/SignUpCardUI.tsx`
```tsx
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  InputRightElement,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  Link,
} from '@chakra-ui/react';
import { useState } from 'react';
import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons';
import { useForm } from 'react-hook-form';
import { Link as RouterLink } from 'react-router-dom';

export type EmailAndPassword = {
  email: string;
  password: string;
};

type SignUpCardProps = {
  onSubmit(values: EmailAndPassword): void;
};

function SignUpCardUI({ onSubmit }: SignUpCardProps) {
  const [showPassword, setShowPassword] = useState(false);
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
  } = useForm<EmailAndPassword>();

  return (
    <Flex
      minH={'100%'}
      align={'center'}
      justify={'center'}
      bg={useColorModeValue('gray.50', 'gray.800')}
    >
      <Stack spacing={8} mx={'auto'} maxW={'lg'} minW={'450px'} py={12} px={6}>
        <Stack align={'center'}>
          <Heading fontSize={'4xl'} textAlign={'center'}>
            Sign up
          </Heading>
          <Text fontSize={'lg'} color={'gray.600'}>
            to enjoy all of our cool features
            <span role="img" aria-label="peace-emoji">
              ✌️
            </span>
          </Text>
        </Stack>
        <Box
          rounded={'lg'}
          bg={useColorModeValue('white', 'gray.700')}
          boxShadow={'lg'}
          p={8}
        >
          <form onSubmit={handleSubmit(onSubmit)}>
            <Stack spacing={4}>
              <FormControl isRequired>
                <FormLabel htmlFor="email">Email address</FormLabel>
                <Input
                  id="email"
                  type="email"
                  {...register('email', {
                    required: 'Email is required',
                  })}
                />
              </FormControl>
              <FormControl isRequired>
                <FormLabel htmlFor="name">Password</FormLabel>
                <InputGroup>
                  <Input
                    id="password"
                    type={showPassword ? 'text' : 'password'}
                    {...register('password', {
                      required: 'Password is required',
                      minLength: {
                        value: 8,
                        message: 'Minimum length should be 8',
                      },
                    })}
                  />
                  <InputRightElement h={'full'}>
                    <Button
                      variant={'ghost'}
                      onClick={() =>
                        setShowPassword((showPassword) => !showPassword)
                      }
                    >
                      {showPassword ? <ViewIcon /> : <ViewOffIcon />}
                    </Button>
                  </InputRightElement>
                </InputGroup>
              </FormControl>
              <Stack spacing={10} pt={2}>
                <Button
                  isLoading={isSubmitting}
                  loadingText="Submitting"
                  size="lg"
                  bg={'blue.400'}
                  color={'white'}
                  type={'submit'}
                  _hover={{
                    bg: 'blue.500',
                  }}
                >
                  Sign up
                </Button>
              </Stack>
              <Stack pt={6}>
                <Text align={'center'}>
                  Already a user?{' '}
                  <Link as={RouterLink} to={'/login'} color={'blue.400'}>
                    Login
                  </Link>
                </Text>
              </Stack>
            </Stack>
          </form>
        </Box>
      </Stack>
    </Flex>
  );
}

export default SignUpCardUI;
```

## File: `apps/frontend/src/components/SidebarWithHeader/SidebarWithHeader.tsx`
```tsx
import { ReactNode } from 'react';
import {
  IconButton,
  Box,
  CloseButton,
  Flex,
  HStack,
  Icon,
  useColorModeValue,
  Link,
  Drawer,
  DrawerContent,
  Text,
  useDisclosure,
  BoxProps,
  FlexProps,
} from '@chakra-ui/react';
import {
  FiHome,
  FiTrendingUp,
  FiCompass,
  FiStar,
  FiSettings,
  FiMenu,
  FiBell,
} from 'react-icons/fi';
import { IconType } from 'react-icons';
import { ReactText } from 'react';
import AuthHeader from '../Auth/AuthHeader/AuthHeader';
import { Link as RouterLink } from 'react-router-dom';

interface LinkItemProps {
  name: string;
  icon: IconType;
  path: string;
}
const LinkItems: Array<LinkItemProps> = [
  { name: 'Home', icon: FiHome, path: '/' },
  { name: 'Trending', icon: FiTrendingUp, path: '/trending' },
  { name: 'Explore', icon: FiCompass, path: '/explore' },
  { name: 'Favourites', icon: FiStar, path: '/favourites' },
  { name: 'Settings', icon: FiSettings, path: '/settings' },
];

export default function SidebarWithHeader({
  children,
}: {
  children: ReactNode;
}) {
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <Box minH="100vh" bg={useColorModeValue('gray.100', 'gray.900')}>
      <SidebarContent
        onClose={() => onClose}
        display={{ base: 'none', md: 'block' }}
      />
      <Drawer
        autoFocus={false}
        isOpen={isOpen}
        placement="left"
        onClose={onClose}
        returnFocusOnClose={false}
        onOverlayClick={onClose}
        size="full"
      >
        <DrawerContent>
          <SidebarContent onClose={onClose} />
        </DrawerContent>
      </Drawer>
      {/* mobilenav */}
      <MobileNav onOpen={onOpen} />
      <Box ml={{ base: 0, md: 60 }} p="4">
        {children}
      </Box>
    </Box>
  );
}

interface SidebarProps extends BoxProps {
  onClose: () => void;
}

const SidebarContent = ({ onClose, ...rest }: SidebarProps) => {
  return (
    <Box
      transition="3s ease"
      bg={useColorModeValue('white', 'gray.900')}
      borderRight="1px"
      borderRightColor={useColorModeValue('gray.200', 'gray.700')}
      w={{ base: 'full', md: 60 }}
      pos="fixed"
      h="full"
      {...rest}
    >
      <Flex h="20" alignItems="center" mx="8" justifyContent="space-between">
        <Text fontSize="2xl" fontFamily="monospace" fontWeight="bold">
          Logo
        </Text>
        <CloseButton display={{ base: 'flex', md: 'none' }} onClick={onClose} />
      </Flex>
      {LinkItems.map((link) => (
        <NavItem key={link.name} icon={link.icon} path={link.path}>
          {link.name}
        </NavItem>
      ))}
    </Box>
  );
};

interface NavItemProps extends FlexProps {
  icon: IconType;
  children: ReactText;
  path: string;
}
const NavItem = ({ icon, children, path, ...rest }: NavItemProps) => {
  return (
    <Link
      as={RouterLink}
      to={path}
      style={{ textDecoration: 'none' }}
      _focus={{ boxShadow: 'none' }}
    >
      <Flex
        align="center"
        p="4"
        mx="4"
        borderRadius="lg"
        role="group"
        cursor="pointer"
        _hover={{
          bg: 'cyan.400',
          color: 'white',
        }}
        {...rest}
      >
        {icon && (
          <Icon
            mr="4"
            fontSize="16"
            _groupHover={{
              color: 'white',
            }}
            as={icon}
          />
        )}
        {children}
      </Flex>
    </Link>
  );
};

interface MobileProps extends FlexProps {
  onOpen: () => void;
}
const MobileNav = ({ onOpen, ...rest }: MobileProps) => {
  return (
    <Flex
      ml={{ base: 0, md: 60 }}
      px={{ base: 4, md: 4 }}
      height="20"
      alignItems="center"
      bg={useColorModeValue('white', 'gray.900')}
      borderBottomWidth="1px"
      borderBottomColor={useColorModeValue('gray.200', 'gray.700')}
      justifyContent={{ base: 'space-between', md: 'flex-end' }}
      {...rest}
    >
      <IconButton
        display={{ base: 'flex', md: 'none' }}
        onClick={onOpen}
        variant="outline"
        aria-label="open menu"
        icon={<FiMenu />}
      />

      <Text
        display={{ base: 'flex', md: 'none' }}
        fontSize="2xl"
        fontFamily="monospace"
        fontWeight="bold"
      >
        Logo
      </Text>

      <HStack spacing={{ base: '0', md: '6' }}>
        <IconButton
          size="lg"
          variant="ghost"
          aria-label="open menu"
          icon={<FiBell />}
        />
        <AuthHeader />
      </HStack>
    </Flex>
  );
};
```

## File: `apps/frontend/src/pages/Home.tsx`
```tsx
import { Box, Heading } from '@chakra-ui/react';
import React from 'react';

const Home = () => {
  return (
    <Box>
      <Heading>Lorem ipsum</Heading>

      <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>

      <p>
        Pellentesque habitant morbi tristique senectus et netus et malesuada
        fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae,
        ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam
        egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend
        leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum
        erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean
        fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci,
        sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar
        facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor
        neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat
        volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis
        luctus, metus
      </p>

      <p>
        Pellentesque habitant morbi tristique senectus et netus et malesuada
        fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae,
        ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam
        egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend
        leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum
        erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean
        fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci,
        sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar
        facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor
        neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat
        volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis
        luctus, metus
      </p>

      <p>
        Pellentesque habitant morbi tristique senectus et netus et malesuada
        fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae,
        ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam
        egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend
        leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum
        erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean
        fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci,
        sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar
        facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor
        neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat
        volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis
        luctus, metus
      </p>

      <p>
        Pellentesque habitant morbi tristique senectus et netus et malesuada
        fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae,
        ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam
        egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend
        leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum
        erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean
        fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci,
        sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar
        facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor
        neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat
        volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis
        luctus, metus
      </p>
    </Box>
  );
};

export default Home;
```

## File: `apps/frontend/src/utils/trpc.ts`
```typescript
/* eslint-disable @nx/enforce-module-boundaries */
import { createTRPCReact } from '@trpc/react-query';
import type { AppRouter } from 'apps/backend/src/server/trpc';
import { inferRouterInputs, inferRouterOutputs } from '@trpc/server';

export const trpc = createTRPCReact<AppRouter>();

export type RouterInput = inferRouterInputs<AppRouter>;
export type RouterOutput = inferRouterOutputs<AppRouter>;
```

## File: `apps/frontend-e2e/.eslintrc.json`
```json
{
  "extends": ["plugin:cypress/recommended", "../../.eslintrc.json"],
  "ignorePatterns": ["!**/*"],
  "overrides": [
    {
      "files": ["*.ts", "*.tsx", "*.js", "*.jsx"],
      "rules": {}
    }
  ]
}
```

## File: `apps/frontend-e2e/cypress.config.ts`
```typescript
import { defineConfig } from 'cypress';
import { nxE2EPreset } from '@nx/cypress/plugins/cypress-preset';

export default defineConfig({
  e2e: nxE2EPreset(__dirname, {
    bundler: 'vite',
  }),
});
```

## File: `apps/frontend-e2e/project.json`
```json
{
  "name": "frontend-e2e",
  "$schema": "../../node_modules/nx/schemas/project-schema.json",
  "sourceRoot": "apps/frontend-e2e/src",
  "projectType": "application",
  "targets": {
    "e2e": {
      "executor": "@nx/cypress:cypress",
      "options": {
        "cypressConfig": "apps/frontend-e2e/cypress.config.ts",
        "devServerTarget": "frontend:serve:development",
        "testingType": "e2e"
      },
      "configurations": {
        "production": {
          "devServerTarget": "frontend:serve:production"
        }
      }
    },
    "lint": {
      "executor": "@nx/eslint:lint",
      "outputs": ["{options.outputFile}"],
      "options": {
        "lintFilePatterns": ["apps/frontend-e2e/**/*.{js,ts}"]
      }
    }
  },
  "tags": [],
  "implicitDependencies": ["frontend"]
}
```

## File: `apps/frontend-e2e/tsconfig.json`
```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "sourceMap": false,
    "outDir": "../../dist/out-tsc",
    "allowJs": true,
    "types": ["cypress", "node"]
  },
  "include": ["src/**/*.ts", "src/**/*.js", "cypress.config.ts"]
}
```

## File: `apps/frontend-e2e/src/e2e/app.cy.ts`
```typescript
import { getGreeting } from '../support/app.po';

describe('frontend', () => {
  beforeEach(() => cy.visit('/'));

  it('should display welcome message', () => {
    // Custom command example, see `../support/commands.ts` file
    cy.login('my-email@something.com', 'myPassword');

    // Function helper example, see `../support/app.po.ts` file
    getGreeting().contains('Welcome frontend');
  });
});
```

## File: `apps/frontend-e2e/src/fixtures/example.json`
```json
{
  "name": "Using fixtures to represent data",
  "email": "hello@cypress.io"
}
```

## File: `apps/frontend-e2e/src/support/app.po.ts`
```typescript
export const getGreeting = () => cy.get('h1');
```

## File: `apps/frontend-e2e/src/support/commands.ts`
```typescript
// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************

// eslint-disable-next-line @typescript-eslint/no-namespace
declare namespace Cypress {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  interface Chainable<Subject> {
    login(email: string, password: string): void;
  }
}
//
// -- This is a parent command --
Cypress.Commands.add('login', (email, password) => {
  console.log('Custom command example: Login', email, password);
});
//
// -- This is a child command --
// Cypress.Commands.add("drag", { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add("dismiss", { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite("visit", (originalFn, url, options) => { ... })
```

## File: `apps/frontend-e2e/src/support/e2e.ts`
```typescript
// ***********************************************************
// This example support/index.js is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import commands.js using ES2015 syntax:
import './commands';
```

## File: `docker/docker-compose.yaml`
```yaml
## Only for local development or running tests

version: '3.4'

services:
  postgres:
    image: postgres:alpine
    container_name: postgres
    ports:
      - 5432:5432
    environment:
      POSTGRES_USER: 'user'
      POSTGRES_PASSWORD: 'password'
      POSTGRES_DB: 'my_app'
    volumes:
      - postgres:/var/lib/postgresql/data

volumes:
  postgres:
```

## File: `tools/tsconfig.tools.json`
```json
{
  "extends": "../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "../dist/out-tsc/tools",
    "rootDir": ".",
    "module": "commonjs",
    "target": "es5",
    "types": ["node"],
    "importHelpers": false
  },
  "include": ["**/*.ts"]
}
```

