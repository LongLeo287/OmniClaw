---
id: domain-driven-hexagon-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.590974
---

# KNOWLEDGE EXTRACT: domain-driven-hexagon
> **Extracted on:** 2026-03-31 01:39:10
> **Source:** domain-driven-hexagon

---

## File: `.dependency-cruiser.js`
```javascript
/** @type {import('dependency-cruiser').IConfiguration} */

// https://github.com/Sairyss/domain-driven-hexagon#enforcing-architecture

const apiLayerPaths = [
  'controller',
  'dtos',
  'request',
  'response',
  'dto\\.ts$',
  'controller\\.ts$',
  'resolver\\.ts$',
];

const applicationLayerPaths = ['application', '\\.service\\.ts$'];

const infrastructureLayerPaths = [
  'infrastructure',
  'infra',
  'database',
  'repository',
];

const domainLayerPaths = [
  'domain',
  'entity\\.ts$',
  'aggregate\\.ts$',
  'domain-event\\.ts$',
  'value-object\\.ts$',
];

module.exports = {
  forbidden: [
    /* user defined rules */
    {
      name: 'no-domain-to-api-deps',
      comment: 'Domain layer cannot depend on api layer',
      severity: 'error',
      from: { path: domainLayerPaths },
      to: {
        path: apiLayerPaths,
      },
    },
    {
      name: 'no-domain-to-app-deps',
      comment: 'Domain layer cannot depend on application layer',
      severity: 'error',
      from: { path: domainLayerPaths },
      to: {
        path: applicationLayerPaths,
        pathNot: ['AppRequestContext\\.ts'],
      },
    },
    {
      name: 'no-domain-to-infra-deps',
      comment: 'Domain layer cannot depend on infrastructure layer',
      severity: 'error',
      from: { path: domainLayerPaths },
      to: {
        path: infrastructureLayerPaths,
        pathNot: ['port\\.ts$'],
      },
    },
    {
      name: 'no-infra-to-api-deps',
      comment: 'Infrastructure layer cannot depend on api layer',
      severity: 'error',
      from: { path: infrastructureLayerPaths },
      to: {
        path: apiLayerPaths,
      },
    },
    {
      name: 'no-command-query-to-api-deps',
      comment: 'Commands and Queries cannot depend on api layer',
      severity: 'error',
      from: {
        path: [
          'query-handler\\.ts$',
          'command-handler\\.ts$',
          'command\\.ts$',
          'service\\.ts$',
        ],
      },
      to: {
        path: apiLayerPaths,
      },
    },

    /* rules from the 'recommended' preset: */
    // {
    //   name: 'no-circular',
    //   severity: 'warn',
    //   comment:
    //     'This dependency is part of a circular relationship. You might want to revise ' +
    //     'your solution (i.e. use dependency inversion, make sure the modules have a single responsibility) ',
    //   from: {},
    //   to: {
    //     circular: true,
    //   },
    // },
    {
      name: 'no-orphans',
      comment:
        "This is an orphan module - it's likely not used (anymore?). Either use it or " +
        "remove it. If it's logical this module is an orphan (i.e. it's a config file), " +
        'add an exception for it in your dependency-cruiser configuration. By default ' +
        'this rule does not scrutinize dot-files (e.g. .eslintrc.js), TypeScript declaration ' +
        'files (.d.ts), tsconfig.json and some of the babel and webpack configs.',
      severity: 'error',
      from: {
        orphan: true,
        pathNot: [
          '(^|/)\\.[^/]+\\.(js|cjs|mjs|ts|json)$', // dot files
          '\\.d\\.ts$', // TypeScript declaration files
          '(^|/)tsconfig\\.json$', // TypeScript config
          '(^|/)(babel|webpack)\\.config\\.(js|cjs|mjs|ts|json)$', // other configs
        ],
      },
      to: {},
    },
    {
      name: 'no-deprecated-core',
      comment:
        'A module depends on a node core module that has been deprecated. Find an alternative - these are ' +
        "bound to exist - node doesn't deprecate lightly.",
      severity: 'error',
      from: {},
      to: {
        dependencyTypes: ['core'],
        path: [
          '^(v8/tools/codemap)$',
          '^(v8/tools/consarray)$',
          '^(v8/tools/csvparser)$',
          '^(v8/tools/logreader)$',
          '^(v8/tools/profile_view)$',
          '^(v8/tools/profile)$',
          '^(v8/tools/SourceMap)$',
          '^(v8/tools/splaytree)$',
          '^(v8/tools/tickprocessor-driver)$',
          '^(v8/tools/tickprocessor)$',
          '^(node-inspect/lib/_inspect)$',
          '^(node-inspect/lib/internal/inspect_client)$',
          '^(node-inspect/lib/internal/inspect_repl)$',
          '^(async_hooks)$',
          '^(punycode)$',
          '^(domain)$',
          '^(constants)$',
          '^(sys)$',
          '^(_linklist)$',
          '^(_stream_wrap)$',
        ],
      },
    },
    {
      name: 'not-to-deprecated',
      comment:
        'This module uses a (version of an) npm module that has been deprecated. Either upgrade to a later ' +
        'version of that module, or find an alternative. Deprecated modules are a security risk.',
      severity: 'error',
      from: {},
      to: {
        dependencyTypes: ['deprecated'],
      },
    },
    {
      name: 'no-non-package-json',
      severity: 'error',
      comment:
        "This module depends on an npm package that isn't in the 'dependencies' section of your package.json. " +
        "That's problematic as the package either (1) won't be available on live (2 - worse) will be " +
        'available on live with an non-guaranteed version. Fix it by adding the package to the dependencies ' +
        'in your package.json.',
      from: {},
      to: {
        dependencyTypes: ['npm-no-pkg', 'npm-unknown'],
      },
    },
    {
      name: 'not-to-unresolvable',
      comment:
        "This module depends on a module that cannot be found ('resolved to disk'). If it's an npm " +
        'module: add it to your package.json. In all other cases you likely already know what to do.',
      severity: 'error',
      from: {},
      to: {
        couldNotResolve: true,
      },
    },
    {
      name: 'no-duplicate-dep-types',
      comment:
        "Likely this module depends on an external ('npm') package that occurs more than once " +
        'in your package.json i.e. bot as a devDependencies and in dependencies. This will cause ' +
        'maintenance problems later on.',
      severity: 'error',
      from: {},
      to: {
        moreThanOneDependencyType: true,
        // as it's pretty common to have a type import be a type only import
        // _and_ (e.g.) a devDependency - don't consider type-only dependency
        // types for this rule
        dependencyTypesNot: ['type-only'],
      },
    },

    /* rules you might want to tweak for your specific situation: */
    {
      name: 'not-to-test',
      comment:
        "This module depends on code within a folder that should only contain tests. As tests don't " +
        "implement functionality this is odd. Either you're writing a test outside the test folder " +
        "or there's something in the test folder that isn't a test.",
      severity: 'error',
      from: {
        pathNot: '^(tests)',
      },
      to: {
        path: '^(tests)',
      },
    },
    {
      name: 'not-to-spec',
      comment:
        'This module depends on a spec (test) file. The sole responsibility of a spec file is to test code. ' +
        "If there's something in a spec that's of use to other modules, it doesn't have that single " +
        'responsibility anymore. Factor it out into (e.g.) a separate utility/ helper or a mock.',
      severity: 'error',
      from: {},
      to: {
        path: '\\.(spec|test)\\.(js|mjs|cjs|ts|ls|coffee|litcoffee|coffee\\.md)$',
      },
    },
    {
      name: 'not-to-dev-dep',
      severity: 'error',
      comment:
        "This module depends on an npm package from the 'devDependencies' section of your " +
        'package.json. It looks like something that ships to production, though. To prevent problems ' +
        "with npm packages that aren't there on production declare it (only!) in the 'dependencies'" +
        'section of your package.json. If this module is development only - add it to the ' +
        'from.pathNot re of the not-to-dev-dep rule in the dependency-cruiser configuration',
      from: {
        path: '^(src)',
        pathNot:
          '\\.(spec|test)\\.(js|mjs|cjs|ts|ls|coffee|litcoffee|coffee\\.md)$',
      },
      to: {
        dependencyTypes: ['npm-dev'],
      },
    },
    {
      name: 'optional-deps-used',
      severity: 'info',
      comment:
        'This module depends on an npm package that is declared as an optional dependency ' +
        "in your package.json. As this makes sense in limited situations only, it's flagged here. " +
        "If you're using an optional dependency here by design - add an exception to your" +
        'dependency-cruiser configuration.',
      from: {},
      to: {
        dependencyTypes: ['npm-optional'],
      },
    },
    {
      name: 'peer-deps-used',
      comment:
        'This module depends on an npm package that is declared as a peer dependency ' +
        'in your package.json. This makes sense if your package is e.g. a plugin, but in ' +
        'other cases - maybe not so much. If the use of a peer dependency is intentional ' +
        'add an exception to your dependency-cruiser configuration.',
      severity: 'error',
      from: {},
      to: {
        dependencyTypes: ['npm-peer'],
      },
    },
  ],
  options: {
    /* conditions specifying which files not to follow further when encountered:
       - path: a regular expression to match
       - dependencyTypes: see https://github.com/sverweij/dependency-cruiser/blob/master/doc/rules-reference.md#dependencytypes-and-dependencytypesnot
       for a complete list
    */
    doNotFollow: {
      path: 'node_modules',
    },

    /* conditions specifying which dependencies to exclude
       - path: a regular expression to match
       - dynamic: a boolean indicating whether to ignore dynamic (true) or static (false) dependencies.
          leave out if you want to exclude neither (recommended!)
    */
    // exclude : {
    //   path: '',
    //   dynamic: true
    // },

    /* pattern specifying which files to include (regular expression)
       dependency-cruiser will skip everything not matching this pattern
    */
    // includeOnly : '',

    /* dependency-cruiser will include modules matching against the focus
       regular expression in its output, as well as their neighbours (direct
       dependencies and dependents)
    */
    // focus : '',

    /* list of module systems to cruise */
    // moduleSystems: ['amd', 'cjs', 'es6', 'tsd'],

    /* prefix for links in html and svg output (e.g. 'https://github.com/you/yourrepo/blob/develop/'
       to open it on your online repo or `vscode://file/${process.cwd()}/` to 
       open it in visual studio code),
     */
    // prefix: '',

    /* false (the default): ignore dependencies that only exist before typescript-to-javascript compilation
       true: also detect dependencies that only exist before typescript-to-javascript compilation
       "specify": for each dependency identify whether it only exists before compilation or also after
     */
    tsPreCompilationDeps: true,

    /* 
       list of extensions to scan that aren't javascript or compile-to-javascript. 
       Empty by default. Only put extensions in here that you want to take into
       account that are _not_ parsable. 
    */
    // extraExtensionsToScan: [".json", ".jpg", ".png", ".svg", ".webp"],

    /* if true combines the package.jsons found from the module up to the base
       folder the cruise is initiated from. Useful for how (some) mono-repos
       manage dependencies & dependency definitions.
     */
    // combinedDependencies: false,

    /* if true leave symlinks untouched, otherwise use the realpath */
    // preserveSymlinks: false,

    /* TypeScript project file ('tsconfig.json') to use for
       (1) compilation and
       (2) resolution (e.g. with the paths property)

       The (optional) fileName attribute specifies which file to take (relative to
       dependency-cruiser's current working directory). When not provided
       defaults to './tsconfig.json'.
     */
    tsConfig: {
      fileName: 'tsconfig.json',
    },

    /* Webpack configuration to use to get resolve options from.

       The (optional) fileName attribute specifies which file to take (relative
       to dependency-cruiser's current working directory. When not provided defaults
       to './webpack.conf.js'.

       The (optional) `env` and `args` attributes contain the parameters to be passed if
       your webpack config is a function and takes them (see webpack documentation
       for details)
     */
    // webpackConfig: {
    //  fileName: './webpack.config.js',
    //  env: {},
    //  args: {},
    // },

    /* Babel config ('.babelrc', '.babelrc.json', '.babelrc.json5', ...) to use
      for compilation (and whatever other naughty things babel plugins do to
      source code). This feature is well tested and usable, but might change
      behavior a bit over time (e.g. more precise results for used module 
      systems) without dependency-cruiser getting a major version bump.
     */
    // babelConfig: {
    //   fileName: './.babelrc'
    // },

    /* List of strings you have in use in addition to cjs/ es6 requires
       & imports to declare module dependencies. Use this e.g. if you've
       re-declared require, use a require-wrapper or use window.require as
       a hack.
    */
    // exoticRequireStrings: [],
    /* options to pass on to enhanced-resolve, the package dependency-cruiser
       uses to resolve module references to disk. You can set most of these
       options in a webpack.conf.js - this section is here for those
       projects that don't have a separate webpack config file.

       Note: settings in webpack.conf.js override the ones specified here.
     */
    enhancedResolveOptions: {
      /* List of strings to consider as 'exports' fields in package.json. Use
         ['exports'] when you use packages that use such a field and your environment
         supports it (e.g. node ^12.19 || >=14.7 or recent versions of webpack).

         If you have an `exportsFields` attribute in your webpack config, that one
         will have precedence over the one specified here.
      */
      exportsFields: ['exports'],
      /* List of conditions to check for in the exports field. e.g. use ['imports']
         if you're only interested in exposed es6 modules, ['require'] for commonjs,
         or all conditions at once `(['import', 'require', 'node', 'default']`)
         if anything goes for you. Only works when the 'exportsFields' array is
         non-empty.

        If you have a 'conditionNames' attribute in your webpack config, that one will
        have precedence over the one specified here.
      */
      conditionNames: ['import', 'require', 'node', 'default'],
      /*
         The extensions, by default are the same as the ones dependency-cruiser
         can access (run `npx depcruise --info` to see which ones that are in
         _your_ environment. If that list is larger than what you need (e.g. 
         it contains .js, .jsx, .ts, .tsx, .cts, .mts - but you don't use 
         TypeScript you can pass just the extensions you actually use (e.g. 
         [".js", ".jsx"]). This can speed up the most expensive step in 
         dependency cruising (module resolution) quite a bit.
       */
      // extensions: [".js", ".jsx", ".ts", ".tsx", ".d.ts"],
      /* 
         If your TypeScript project makes use of types specified in 'types'
         fields in package.jsons of external dependencies, specify "types"
         in addition to "main" in here, so enhanced-resolve (the resolver
         dependency-cruiser uses) knows to also look there. You can also do
         this if you're not sure, but still use TypeScript. In a future version
         of dependency-cruiser this will likely become the default.
       */
      mainFields: ['main', 'types'],
    },
    reporterOptions: {
      dot: {
        /* pattern of modules that can be consolidated in the detailed
           graphical dependency graph. The default pattern in this configuration
           collapses everything in node_modules to one folder deep so you see
           the external modules, but not the innards your app depends upon.
         */
        collapsePattern: 'node_modules/[^/]+',

        /* Options to tweak the appearance of your graph.See
           https://github.com/sverweij/dependency-cruiser/blob/master/doc/options-reference.md#reporteroptions
           for details and some examples. If you don't specify a theme
           don't worry - dependency-cruiser will fall back to the default one.
        */
        // theme: {
        //   graph: {
        //     /* use splines: "ortho" for straight lines. Be aware though
        //       graphviz might take a long time calculating ortho(gonal)
        //       routings.
        //    */
        //     splines: "true"
        //   },
        //   modules: [
        //     {
        //       criteria: { matchesFocus: true },
        //       attributes: {
        //         fillcolor: "lime",
        //         penwidth: 2,
        //       },
        //     },
        //     {
        //       criteria: { matchesFocus: false },
        //       attributes: {
        //         fillcolor: "lightgrey",
        //       },
        //     },
        //     {
        //       criteria: { matchesReaches: true },
        //       attributes: {
        //         fillcolor: "lime",
        //         penwidth: 2,
        //       },
        //     },
        //     {
        //       criteria: { matchesReaches: false },
        //       attributes: {
        //         fillcolor: "lightgrey",
        //       },
        //     },
        //     {
        //       criteria: { source: "^src/model" },
        //       attributes: { fillcolor: "#ccccff" }
        //     },
        //     {
        //       criteria: { source: "^src/view" },
        //       attributes: { fillcolor: "#ccffcc" }
        //     },
        //   ],
        //   dependencies: [
        //     {
        //       criteria: { "rules[0].severity": "error" },
        //       attributes: { fontcolor: "red", color: "red" }
        //     },
        //     {
        //       criteria: { "rules[0].severity": "warn" },
        //       attributes: { fontcolor: "orange", color: "orange" }
        //     },
        //     {
        //       criteria: { "rules[0].severity": "info" },
        //       attributes: { fontcolor: "blue", color: "blue" }
        //     },
        //     {
        //       criteria: { resolved: "^src/model" },
        //       attributes: { color: "#0000ff77" }
        //     },
        //     {
        //       criteria: { resolved: "^src/view" },
        //       attributes: { color: "#00770077" }
        //     }
        //   ]
        // }
      },
      archi: {
        /* pattern of modules that can be consolidated in the high level
          graphical dependency graph. If you use the high level graphical
          dependency graph reporter (`archi`) you probably want to tweak
          this collapsePattern to your situation.
        */
        collapsePattern:
          '^(packages|src|lib|app|bin|test(s?)|spec(s?))/[^/]+|node_modules/[^/]+',

        /* Options to tweak the appearance of your graph.See
           https://github.com/sverweij/dependency-cruiser/blob/master/doc/options-reference.md#reporteroptions
           for details and some examples. If you don't specify a theme
           for 'archi' dependency-cruiser will use the one specified in the
           dot section (see above), if any, and otherwise use the default one.
         */
        // theme: {
        // },
      },
      text: {
        highlightFocused: true,
      },
    },
  },
};
// generated: dependency-cruiser@12.10.0 on 2023-02-27T15:40:08.936Z
```

## File: `.env.example`
```
DB_HOST='localhost'
DB_PORT=5432
DB_USERNAME='user'
DB_PASSWORD='password'
DB_NAME='ddh'
```

## File: `.env.test`
```
# env file for e2e testing
DB_HOST='localhost'
DB_PORT=5432
DB_USERNAME='user'
DB_PASSWORD='password'
DB_NAME='ddh_tests' # running tests in a separate test db
```

## File: `.eslintrc.js`
```javascript
/**
 * eslint config
 * https://github.com/Sairyss/backend-best-practices#static-code-analysis
 */

module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.json',
    tsconfigRootDir: __dirname,
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint/eslint-plugin'],
  extends: [
    'plugin:@typescript-eslint/recommended',
    'plugin:prettier/recommended',
  ],
  root: true,
  env: {
    node: true,
    jest: true,
  },
  ignorePatterns: ['.eslintrc.js'],
  rules: {
    '@typescript-eslint/interface-name-prefix': 'off',
    '@typescript-eslint/no-explicit-any': 'off',

    // TS errors
    '@typescript-eslint/no-misused-new': 'error',
    '@typescript-eslint/explicit-module-boundary-types': 'error',
    '@typescript-eslint/no-non-null-assertion': 'error',
    '@typescript-eslint/no-unused-vars': 'error',

    // Eslint off
    'import/extensions': 'off',
    'import/prefer-default-export': 'off',
    'class-methods-use-this': 'off',
    'no-useless-constructor': 'off',
    'import/no-unresolved': 'off',
    'no-control-regex': 'off',
    'no-shadow': 'off',
    'import/no-cycle': 'off',
    'consistent-return': 'off',
    'no-underscore-dangle': 'off',
    'max-classes-per-file': 'off',

    // Eslint errors
    'no-restricted-syntax': [
      'error',
      {
        selector: 'LabeledStatement',
        message:
          'Labels are a form of GOTO; using them makes code confusing and hard to maintain and understand.',
      },
      {
        selector: 'WithStatement',
        message:
          '`with` is disallowed in strict mode because it makes code impossible to predict and optimize.',
      },
      {
        selector: "MethodDefinition[kind='set']",
        message: 'Property setters are not allowed',
      },
    ],
  },
};
```

## File: `.gitignore`
```
# Environment variables
.env

# compiled output
/dist
/node_modules
/package-lock.json

# Logs
logs
*.log
npm-debug.log*
pnpm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# OS
.DS_Store

# Tests
/coverage
/.nyc_output

# IDEs and editors
/.idea
.project
.classpath
.c9/
*.launch
.settings/
*.sublime-workspace

# IDE - VSCode
# .vscode/*
# !.vscode/settings.json
# !.vscode/tasks.json
# !.vscode/launch.json
# !.vscode/extensions.json
```

## File: `.jestrc.json`
```json
{
  "moduleFileExtensions": ["js", "json", "ts"],
  "rootDir": ".",
  "testEnvironment": "node",
  "coverageDirectory": "../tests/coverage",
  "setupFilesAfterEnv": ["./tests/setup/jestSetupAfterEnv.ts"],
  "globalSetup": "<rootDir>/tests/setup/jestGlobalSetup.ts",
  "testRegex": ".spec.ts$",
  "moduleNameMapper": {
    "@src/(.*)$": "<rootDir>/src/$1",
    "@modules/(.*)$": "<rootDir>/src/modules/$1",
    "@config/(.*)$": "<rootDir>/src/configs/$1",
    "@libs/(.*)$": "<rootDir>/src/libs/$1",
    "@exceptions$": "<rootDir>/src/libs/exceptions",
    "@tests/(.*)$": "<rootDir>/tests/$1"
  },
  "transform": {
    "^.+\\.(t|j)s$": "ts-jest"
  }
}
```

## File: `.prettierrc`
```
{
  "singleQuote": true,
  "trailingComma": "all"
}
```

## File: `jest-e2e.json`
```json
{
  "moduleFileExtensions": ["js", "json", "ts"],
  "rootDir": ".",
  "testEnvironment": "node",
  "coverageDirectory": "./coverage",
  "setupFilesAfterEnv": ["./tests/setup/jestSetupAfterEnv.ts"],
  "globalSetup": "<rootDir>/tests/setup/jestGlobalSetup.ts",
  "testRegex": ".e2e-spec.ts$",
  "moduleNameMapper": {
    "@src/(.*)$": "<rootDir>/src/$1",
    "@modules/(.*)$": "<rootDir>/src/modules/$1",
    "@config/(.*)$": "<rootDir>/src/configs/$1",
    "@libs/(.*)$": "<rootDir>/src/libs/$1",
    "@exceptions$": "<rootDir>/src/libs/exceptions",
    "@tests/(.*)$": "<rootDir>/tests/$1"
  },
  "transform": {
    "^.+\\.(t|j)s$": "ts-jest"
  }
}
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2021 Sairyss

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

## File: `nest-cli.json`
```json
{
  "$schema": "https://json.schemastore.org/nest-cli",
  "collection": "@nestjs/schematics",
  "sourceRoot": "src"
}
```

## File: `package.json`
```json
{
  "name": "domain-driven-hexagon",
  "version": "2.0.0",
  "description": "",
  "author": "",
  "private": true,
  "license": "UNLICENSED",
  "scripts": {
    "prebuild": "rimraf dist",
    "build": "nest build",
    "format": "prettier --write \"src/**/*.ts\" \"tests/**/*.ts\"",
    "start": "nest start",
    "start:dev": "nest start --watch",
    "start:debug": "nest start --debug --watch",
    "start:prod": "node dist/main",
    "lint": "eslint \"{src,apps,libs,tests}/**/*.ts\" --fix",
    "test": "jest --config .jestrc.json",
    "test:watch": "jest --watch",
    "test:cov": "jest --coverage",
    "test:debug": "node --inspect-brk -r tsconfig-paths/register -r ts-node/register node_modules/.bin/jest --runInBand",
    "test:e2e": "jest -i --config jest-e2e.json",
    "docker:env": "docker-compose --file docker/docker-compose.yml up --build",
    "migration:create": "ts-node database/migrate create --name",
    "migration:up": "ts-node database/migrate up",
    "migration:up:tests": "NODE_ENV=test ts-node database/migrate up",
    "migration:down": "ts-node database/migrate down",
    "migration:down:tests": "NODE_ENV=test ts-node database/migrate down",
    "migration:executed": "ts-node database/migrate executed",
    "migration:executed:tests": "NODE_ENV=test ts-node database/migrate executed",
    "migration:pending": "ts-node database/migrate pending",
    "migration:pending:tests": "NODE_ENV=test ts-node database/migrate pending",
    "seed:up": "ts-node database/seed",
    "depcruise": "depcruise",
    "deps:validate": "depcruise src --config .dependency-cruiser.js --output-type err-long",
    "deps:graph": "depcruise src --include-only \"^src\" --config --output-type dot | dot -T svg > assets/dependency-graph.svg"
  },
  "dependencies": {
    "@nestjs/apollo": "^10.1.3",
    "@nestjs/common": "^9.0.0",
    "@nestjs/core": "^9.0.0",
    "@nestjs/cqrs": "^9.0.1",
    "@nestjs/event-emitter": "^1.3.1",
    "@nestjs/graphql": "^10.1.2",
    "@nestjs/microservices": "^9.1.2",
    "@nestjs/platform-express": "^9.0.0",
    "@nestjs/swagger": "^6.1.2",
    "@slonik/migrator": "^0.11.3",
    "apollo-server-core": "^3.10.2",
    "apollo-server-express": "^3.10.2",
    "class-transformer": "^0.5.1",
    "class-validator": "^0.13.2",
    "dotenv": "^16.0.2",
    "env-var": "^7.3.0",
    "graphql": "^16.6.0",
    "jest-cucumber": "^3.0.1",
    "nanoid": "^3.3.4",
    "nestjs-console": "^8.0.0",
    "nestjs-request-context": "^2.1.0",
    "nestjs-slonik": "^9.0.0",
    "oxide.ts": "^1.0.5",
    "reflect-metadata": "^0.1.13",
    "rimraf": "^3.0.2",
    "rxjs": "^7.2.0",
    "slonik": "^31.2.4",
    "uuid": "^9.0.0",
    "zod": "^3.21.4"
  },
  "devDependencies": {
    "@nestjs/cli": "^9.0.0",
    "@nestjs/schematics": "^9.0.0",
    "@nestjs/testing": "^9.0.0",
    "@types/express": "^4.17.13",
    "@types/jest": "28.1.8",
    "@types/node": "^16.0.0",
    "@types/supertest": "^2.0.11",
    "@types/uuid": "^8.3.4",
    "@typescript-eslint/eslint-plugin": "^5.0.0",
    "@typescript-eslint/parser": "^5.0.0",
    "dependency-cruiser": "^12.10.0",
    "eslint": "^8.0.1",
    "eslint-config-prettier": "^8.3.0",
    "eslint-plugin-prettier": "^4.0.0",
    "jest": "28.1.3",
    "prettier": "^2.3.2",
    "source-map-support": "^0.5.20",
    "supertest": "^6.1.3",
    "ts-jest": "28.0.8",
    "ts-loader": "^9.2.3",
    "ts-node": "^10.0.0",
    "tsconfig-paths": "4.1.0",
    "typescript": "^4.7.4"
  },
  "jest": {
    "moduleFileExtensions": [
      "js",
      "json",
      "ts"
    ],
    "rootDir": "src",
    "testRegex": ".*\\.spec\\.ts$",
    "transform": {
      "^.+\\.(t|j)s$": "ts-jest"
    },
    "collectCoverageFrom": [
      "**/*.(t|j)s"
    ],
    "coverageDirectory": "../coverage",
    "testEnvironment": "node"
  },
  "volta": {
    "node": "20.1.0"
  }
}
```

## File: `README.md`
```markdown
# Domain-Driven Hexagon

**Check out my other repositories**:

- [Backend best practices](https://github.com/Sairyss/backend-best-practices) - Best practices, tools and guidelines for backend development.
- [System Design Patterns](https://github.com/Sairyss/system-design-patterns) - list of topics and resources related to distributed systems, system design, microservices, scalability and performance, etc.
- [Full Stack starter template](https://github.com/Sairyss/fullstack-starter-template) - template for full stack applications based on TypeScript, React, Vite, ChakraUI, tRPC, Fastify, Prisma, zod, etc.

---

The main emphasis of this project is to provide recommendations on how to design software applications. This readme includes techniques, tools, best practices, architectural patterns and guidelines gathered from different sources.

Code examples are written using [NodeJS](https://nodejs.org/en/), [TypeScript](https://www.typescriptlang.org/), [NestJS](https://docs.nestjs.com/) framework and [Slonik](https://github.com/gajus/slonik) for the database access.

Patterns and principles presented here are **framework/language agnostic**. Therefore, the above technologies can be easily replaced with any alternative. No matter what language or framework is used, any application can benefit from principles described below.

**Note**: code examples are adapted to TypeScript and frameworks mentioned above. <br/>
(Implementations in other languages will look differently)

**Everything below is provided as a recommendation, not a rule**. Different projects have different requirements, so any pattern mentioned in this readme should be adjusted to project needs or even skipped entirely if it doesn't fit. In real world production applications, you will most likely only need a fraction of those patterns depending on your use cases. More info in [this](#general-recommendations-on-architectures-best-practices-design-patterns-and-principles) section.

---

- [Domain-Driven Hexagon](#domain-driven-hexagon)
- [Architecture](#architecture)
      - [Pros](#pros)
      - [Cons](#cons)
- [Diagram](#diagram)
- [Modules](#modules)
- [Application Core](#application-core)
- [Application layer](#application-layer)
  - [Application Services](#application-services)
  - [Commands and Queries](#commands-and-queries)
    - [Commands](#commands)
    - [Queries](#queries)
  - [Ports](#ports)
- [Domain Layer](#domain-layer)
  - [Entities](#entities)
  - [Aggregates](#aggregates)
  - [Domain Events](#domain-events)
  - [Integration Events](#integration-events)
  - [Domain Services](#domain-services)
  - [Value objects](#value-objects)
  - [Domain Invariants](#domain-invariants)
    - [Replacing primitives with Value Objects](#replacing-primitives-with-value-objects)
    - [Make illegal states unrepresentable](#make-illegal-states-unrepresentable)
      - [Validation at compile time](#validation-at-compile-time)
      - [Validation at runtime](#validation-at-runtime)
    - [Guarding vs validating](#guarding-vs-validating)
  - [Domain Errors](#domain-errors)
  - [Using libraries inside Application's core](#using-libraries-inside-applications-core)
- [Interface Adapters](#interface-adapters)
  - [Controllers](#controllers)
    - [Resolvers](#resolvers)
  - [DTOs](#dtos)
    - [Request DTOs](#request-dtos)
    - [Response DTOs](#response-dtos)
    - [Additional recommendations](#additional-recommendations)
    - [Local DTOs](#local-dtos)
- [Infrastructure layer](#infrastructure-layer)
  - [Adapters](#adapters)
  - [Repositories](#repositories)
  - [Persistence models](#persistence-models)
  - [Other things that can be a part of Infrastructure layer](#other-things-that-can-be-a-part-of-infrastructure-layer)
- [Other recommendations](#other-recommendations)
  - [General recommendations on architectures, best practices, design patterns and principles](#general-recommendations-on-architectures-best-practices-design-patterns-and-principles)
  - [Recommendations for smaller APIs](#recommendations-for-smaller-apis)
  - [Behavioral Testing](#behavioral-testing)
  - [Folder and File Structure](#folder-and-file-structure)
    - [File names](#file-names)
  - [Enforcing architecture](#enforcing-architecture)
  - [Prevent massive inheritance chains](#prevent-massive-inheritance-chains)
- [Additional resources](#additional-resources)
  - [Articles](#articles)
  - [Websites](#websites)
  - [Blogs](#blogs)
  - [Videos](#videos)
  - [Books](#books)

# Architecture

This is an attempt to combine multiple architectural patterns and styles together, such as:

- [Domain-Driven Design (DDD)](https://en.wikipedia.org/wiki/Domain-driven_design)
- [Hexagonal (Ports and Adapters) Architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software))
- [Secure by Design](https://www.manning.com/books/secure-by-design)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Onion Architecture](https://herbertograca.com/2017/09/21/onion-architecture/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Software Design Patterns](https://refactoring.guru/design-patterns/what-is-pattern)

And many others (more links below in every chapter).

Before we begin, here are the PROS and CONS of using a complete architecture like this:

#### Pros

- Independent of external frameworks, technologies, databases, etc. Frameworks and external resources can be plugged/unplugged with much less effort.
- Easily testable and scalable.
- More secure. Some security principles are baked in design itself.
- The solution can be worked on and maintained by different teams, without stepping on each other's toes.
- Easier to add new features. As the system grows over time, the difficulty in adding new features remains constant and relatively small.
- If the solution is properly broken apart along [bounded context](https://martinfowler.com/bliki/BoundedContext.html) lines, it becomes easy to convert pieces of it into microservices if needed.

#### Cons

- This is a sophisticated architecture which requires a firm understanding of quality software principles, such as SOLID, Clean/Hexagonal Architecture, Domain-Driven Design, etc. Any team implementing such a solution will almost certainly require an expert to drive the solution and keep it from evolving the wrong way and accumulating technical debt.

- Some practices presented here are not recommended for small-medium sized applications with not a lot of business logic. There is added up-front complexity to support all those building blocks and layers, boilerplate code, abstractions, data mapping etc. Thus, implementing a complete architecture like this is generally ill-suited to simple [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) applications and could over-complicate such solutions. Some principles which are described below can be used in smaller sized applications, but must be implemented only after analyzing and understanding all pros and cons.

# Diagram

![Domain-Driven Hexagon](assets/images/DomainDrivenHexagon.png)
<sup>Diagram is mostly based on [this one](https://github.com/hgraca/explicit-architecture-php#explicit-architecture-1) + others found online</sup>

In short, data flow looks like this (from left to right):

- Request/CLI command/event is sent to the controller using plain DTO;
- Controller parses this DTO, maps it to a Command/Query object format and passes it to an Application service;
- Application service handles this Command/Query; it executes business logic using domain services and entities/aggregates and uses the infrastructure layer through ports(interfaces);
- Infrastructure layer maps data to a format that it needs, retrieves/persists data from/to a database, uses adapters for other I/O communications (like sending an event to an external broker or calling external APIs), maps data back to domain format and returns it back to Application service;
- After the Application service finishes doing its job, it returns data/confirmation back to Controllers;
- Controllers return data back to the user (if application has presenters/views, those are returned instead).

Each layer is in charge of its own logic and has building blocks that usually should follow a [Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) when possible and when it makes sense (for example, using `Repositories` only for database access, using `Entities` for business logic, etc.).

**Keep in mind** that different projects can have more or less steps/layers/building blocks than described here. Add more if the application requires it, and skip some if the application is not that complex and doesn't need all that abstraction.

General recommendation for any project: analyze how big/complex the application will be, find a compromise and use as many layers/building blocks as needed for the project and skip ones that may over-complicate things.

More in details on each step below.

# Modules

This project's code examples use separation by modules (also called components). Each module's name should reflect an important concept from the Domain and have its own folder with a dedicated codebase. Each business use case inside that module gets its own folder to store most of the things it needs (this is also called _Vertical Slicing_). It's easier to work on things that change together if those things are gathered relatively close to each other. Think of a module as a "box" that groups together related business logic.

Using modules is a great way to [encapsulate](<https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)>) parts of highly [cohesive](<https://en.wikipedia.org/wiki/Cohesion_(computer_science)>) business domain rules.

Try to make every module independent and keep interactions between modules minimal. Think of each module as a mini application bounded by a single context. Consider module internals private and try to avoid direct imports between modules (like importing a class `import SomeClass from '../SomeOtherModule'`) since this creates [tight coupling](<https://en.wikipedia.org/wiki/Coupling_(computer_programming)>) and can turn your code into a [spaghetti](https://en.wikipedia.org/wiki/Spaghetti_code) and application into a [big ball of mud](https://en.wikipedia.org/wiki/Big_ball_of_mud).

Few advices to avoid coupling:

- Try not to create dependencies between modules or use cases. Instead, move shared logic into a separate files and make both depend on that instead of depending on each other.
- Modules can cooperate through a [mediator](https://en.wikipedia.org/wiki/Mediator_pattern#:~:text=In%20software%20engineering%2C%20the%20mediator,often%20consist%20of%20many%20classes.) or a public [facade](https://en.wikipedia.org/wiki/Facade_pattern), hiding all private internals of the module to avoid its misuse, and giving public access only to certain pieces of functionality that meant to be public.
- Alternatively modules can communicate with each other by using messages. For example, you can send commands using a commands bus or subscribe to events that other modules emit (more info on events and commands bus below).

This ensures [loose coupling](https://en.wikipedia.org/wiki/Loose_coupling), refactoring of a module internals can be done easier because outside world only depends on module's public interface, and if bounded contexts are defined and designed properly each module can be easily separated into a microservice if needed without touching any domain logic or major refactoring.

Keep your modules small. You should be able to rewrite a module in a relatively short period of time. This applies not only to modules pattern, but to software development in general: objects, functions, microservices, processes, etc. Keep them small and composable. This is incredibly powerful in a constantly changing environments of software development, since when your requirements change, changing small modules is much easier than changing a big program. You can just delete a module and rewrite it from scratch in a matter of days. This idea is further described in this talk: [Greg Young - The art of destroying software](https://youtu.be/Ed94CfxgsCA).

Code Examples:

- Check [src/modules](src/modules) directory structure.
- [src/modules/user/commands](src/modules/user/commands) - "commands" directory in a user module includes business use cases (commands) that a module can execute, each with its own Vertical Slice.

Read more:

- [Modular programming: Beyond the spaghetti mess](https://www.tiny.cloud/blog/modular-programming-principle/).
- [What are Modules in Domain Driven Design?](https://www.culttt.com/2014/12/10/modules-domain-driven-design/)
- [How to Implement Vertical Slice Architecture](https://garywoodfine.com/implementing-vertical-slice-architecture/)

Each module consists of layers described below.

# Application Core

This is the core of the system which is built using [DDD building blocks](https://dzone.com/articles/ddd-part-ii-ddd-building-blocks):

**Domain layer**:

- Entities
- Aggregates
- Domain Services
- Value Objects
- Domain Errors

**Application layer**:

- Application Services
- Commands and Queries
- Ports

**Note**: different implementations may have slightly different layer structures depending on applications needs. Also, more layers and building blocks may be added if needed.

---

# Application layer

## Application Services

Application Services (also called "Workflow Services", "Use Cases", "Interactors", etc.) are used to orchestrate the steps required to fulfill the commands imposed by the client.

Application services:

- Typically used to orchestrate how the outside world interacts with your application and performs tasks required by the end users;
- Contain no domain-specific business logic;
- Operate on scalar types, transforming them into Domain types. A scalar type can be considered any type that's unknown to the Domain Model. This includes primitive types and types that don't belong to the Domain;
- Uses ports to declare dependencies on infrastructural services/adapters required to execute domain logic (ports are just interfaces, we will discuss this topic in details below);
- Fetch domain `Entities`/`Aggregates` (or anything else) from database/external APIs (through ports/interfaces, with concrete implementations injected by the [DI](https://en.wikipedia.org/wiki/Dependency_injection) library);
- Execute domain logic on those `Entities`/`Aggregates` (by invoking their methods);
- In case of working with multiple `Entities`/`Aggregates`, use a `Domain Service` to orchestrate them;
- Execute other out-of-process communications through Ports (like event emits, sending emails, etc.);
- Services can be used as a `Command`/`Query` handlers;
- Should not depend on other application services since it may cause problems (like cyclic dependencies);

One service per use case is considered a good practice.

<details>
<summary>What are "Use Cases"?</summary>

[wiki](https://en.wikipedia.org/wiki/Use_case):

> In software and systems engineering, a use case is a list of actions or event steps typically defining the interactions between a role (known in the Unified Modeling Language as an actor) and a system to achieve a goal.

Use cases are, simply said, list of actions required from an application.

---

</details>

Example file: [create-user.service.ts](src/modules/user/commands/create-user/create-user.service.ts)

More about services:

- [Domain-Application-Infrastructure Services pattern](https://badia-kharroubi.gitbooks.io/microservices-architecture/content/patterns/tactical-patterns/domain-application-infrastructure-services-pattern.html)
- [Services in DDD finally explained](https://developer20.com/services-in-ddd-finally-explained/)

## Commands and Queries

This principle is called [Command–Query Separation(CQS)](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation). When possible, methods should be separated into `Commands` (state-changing operations) and `Queries` (data-retrieval operations). To make a clear distinction between those two types of operations, input objects can be represented as `Commands` and `Queries`. Before DTO reaches the domain, it's converted into a `Command`/`Query` object.

### Commands

`Command` is an object that signals user intent, for example `CreateUserCommand`. It describes a single action (but does not perform it).

`Commands` are used for state-changing actions, like creating new user and saving it to the database. Create, Update and Delete operations are considered as state-changing.

Data retrieval is responsibility of `Queries`, so `Command` methods should not return business data.

Some CQS purists may say that a `Command` shouldn't return anything at all. But you will need at least an ID of a created item to access it later. To achieve that you can let clients generate a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) (more info here: [CQS versus server generated IDs](https://blog.ploeh.dk/2014/08/11/cqs-versus-server-generated-ids/)).

Though, violating this rule and returning some metadata, like `ID` of a created item, redirect link, confirmation message, status, or other metadata is a more practical approach than following dogmas.

**Note**: `Command` is similar but not the same as described here: [Command Pattern](https://refactoring.guru/design-patterns/command). There are multiple definitions across the internet with similar but slightly different implementations.

To execute a command you can use a `Command Bus` instead of importing a service directly. This will decouple a command Invoker from a Receiver, so you can send your commands from anywhere without creating coupling.

Avoid command handlers executing other commands in this fashion: Command → Command. Instead, use events for that purpose, and execute next commands in a chain in an Event handler: Command → Event → Command.

Example files:

- [create-user.command.ts](src/modules/user/commands/create-user/create-user.command.ts) - a command Object
- [create-user.message.controller.ts](src/modules/user/commands/create-user/create-user.message.controller.ts) - controller executes a command using a command bus. This decouples it from a command handler.
- [create-user.service.ts](src/modules/user/commands/create-user/create-user.service.ts) - a command handler.

Read more:

- [What is a command bus and why should you use it?](https://barryvanveen.nl/blog/49-what-is-a-command-bus-and-why-should-you-use-it)
- [Why You Should Avoid Command Handlers Calling Other Commands?](https://www.rahulpnath.com/blog/avoid-commands-calling-commands/)

### Queries

`Query` is similar to a `Command`. It belongs to a read model and signals user intent to find something and describes how to do it.

`Query` is just a data retrieval operation and should not make any state changes (like writes to the database, files, third party APIs, etc.). For this reason, in read model we can bypass a domain and repository layers completely and query database directly from a query handler.

Similarly to Commands, Queries can use a `Query Bus` if needed. This way you can query anything from anywhere without importing classes directly and avoid coupling.

Example files:

- [find-users.query-handler.ts](src/modules/user/queries/find-users/find-users.query-handler.ts) - a query handler. Notice how we query the database directly, without using domain objects or repositories (more info [here](https://codeopinion.com/should-you-use-the-repository-pattern-with-cqrs-yes-and-no/)).

---

By enforcing `Command` and `Query` separation, the code becomes simpler to understand. One changes something, another just retrieves data.

Also, following CQS from the start will facilitate separating write and read models into different databases if someday in the future the need for it arises.

**Note**: this repo uses [NestJS CQRS](https://docs.nestjs.com/recipes/cqrs) package that provides a command/query bus.

Read more about CQS and CQRS:

- [Command Query Segregation](https://khalilstemmler.com/articles/oop-design-principles/command-query-segregation/).
- [Exposing CQRS Through a RESTful API](https://www.infoq.com/articles/rest-api-on-cqrs/)
- [What is the CQRS pattern?](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs)
- [CQRS and REST: the perfect match](https://lostechies.com/jimmybogard/2016/06/01/cqrs-and-rest-the-perfect-match/)

---

## Ports

Ports are interfaces that define contracts that should be implemented by adapters. For example, a port can abstract technology details (like what type of database is used to retrieve some data), and infrastructure layer can implement an adapter in order to execute some action more related to technology details rather than business logic. Ports act like [abstractions](<https://en.wikipedia.org/wiki/Abstraction_(computer_science)>) for technology details that business logic does not care about. Name "port" most actively is used in [Hexagonal Architecture](<https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)>).

In Application Core **dependencies point inwards**. Outer layers can depend on inner layers, but inner layers never depend on outer layers. Application Core shouldn't depend on frameworks or access external resources directly. Any external calls to out-of-process resources/retrieval of data from remote processes should be done through `ports` (interfaces), with class implementations created somewhere in infrastructure layer and injected into application's core ([Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection) and [Dependency Inversion](https://en.wikipedia.org/wiki/Dependency_inversion_principle)). This makes business logic independent of technology, facilitates testing, allows to plug/unplug/swap any external resources easily making application modular and [loosely coupled](https://en.wikipedia.org/wiki/Loose_coupling).

- Ports are basically just interfaces that define what has to be done and don't care about how it's done.
- Ports can be created to abstract side effects like I/O operations and database access, technology details, invasive libraries, legacy code etc. from the Domain.
- By abstracting side effects, you can test your application logic in isolation by [mocking](https://en.wikipedia.org/wiki/Mock_object) the implementation. This can be useful for [unit testing](https://en.wikipedia.org/wiki/Unit_testing).
- Ports should be created to fit the Domain needs, not simply mimic the tools APIs.
- Mock implementations can be passed to ports while testing. Mocking makes your tests faster and independent of the environment.
- Abstraction provided by ports can be used to inject different implementations to a port if needed ([polymorphism](<https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>)).
- When designing ports, remember the [Interface segregation principle](https://en.wikipedia.org/wiki/Interface_segregation_principle). Split large interfaces into smaller ones when it makes sense, but also keep in mind to not overdo it when not necessary.
- Ports can also help to delay decisions. The Domain layer can be implemented even before deciding what technologies (frameworks, databases etc.) will be used.

**Note**: since most ports implementations are injected and executed in application service, Application Layer can be a good place to keep those ports. But there are times when the Domain Layer's business logic depends on executing some external resource, in such cases those ports can be put in a Domain Layer.

**Note**: abusing ports/interfaces may lead to [unnecessary abstractions](https://mortoray.com/2014/08/01/the-false-abstraction-antipattern/) and overcomplicate your application. In a lot of cases it's totally fine to depend on a concrete implementation instead of abstracting it with an interface. Think carefully if you really need an abstraction before using it.

Example files:

- [repository.port.ts](src/libs/ddd/repository.port.ts) - generic port for repositories
- [user.repository.port.ts](src/modules/user/database/user.repository.port.ts) - a port for user repository
- [find-users.query-handler.ts](src/modules/user/queries/find-users/find-users.query-handler.ts) - notice how query handler depends on a port instead of concrete repository implementation, and an implementation is injected
- [logger.port.ts](src/libs/ports/logger.port.ts) - another example of a port for application logger

Read more:

- [A Color Coded Guide to Ports and Adapters](https://8thlight.com/blog/damon-kelley/2021/05/18/a-color-coded-guide-to-ports-and-adapters.html)

---

# Domain Layer

This layer contains the application's business rules.

Domain should operate using domain objects described by [ubiquitous language](https://martinfowler.com/bliki/UbiquitousLanguage.html). Most important domain building blocks are described below.

- [Developing the ubiquitous language](https://medium.com/@felipefreitasbatista/developing-the-ubiquitous-language-1382b720bb8c)

## Entities

Entities are the core of the domain. They encapsulate Enterprise-wide business rules and attributes. An entity can be an object with properties and methods, or it can be a set of data structures and functions.

Entities represent business models and express what properties a particular model has, what it can do, when and at what conditions it can do it. An example of business model can be a User, Product, Booking, Ticket, Wallet etc.

Entities must always protect their [invariant](https://en.wikipedia.org/wiki/Class_invariant):

> Domain entities should always be valid entities. There are a certain number of invariants for an object that should always be true. For example, an order item object always has to have a quantity that must be a positive integer, plus an article name and price. Therefore, invariants enforcement is the responsibility of the domain entities (especially of the aggregate root) and an entity object should not be able to exist without being valid.

Entities:

- Contain Domain business logic. Avoid having business logic in your services when possible, this leads to [Anemic Domain Model](https://martinfowler.com/bliki/AnemicDomainModel.html) (Domain Services are an exception for business logic that can't be put in a single entity).
- Have an identity that defines it and makes it distinguishable from others. Its identity is consistent during its life cycle.
- Equality between two entities is determined by comparing their identificators (usually its `id` field).
- Can contain other objects, such as other entities or value objects.
- Are responsible for collecting all the understanding of state and how it changes in the same place.
- Responsible for the coordination of operations on the objects it owns.
- Know nothing about upper layers (services, controllers etc.).
- Domain entities data should be modelled to accommodate business logic, not some database schema.
- Entities must protect their invariants, try to avoid public setters - update state using methods and execute invariant validation on each update if needed (this can be a simple `validate()` method that checks if business rules are not violated by update).
- Must be consistent on creation. Validate Entities and other domain objects on creation and throw an error on first failure. [Fail Fast](https://en.wikipedia.org/wiki/Fail-fast).
- Avoid no-arg (empty) constructors, accept and validate all required properties in a constructor (or in a [factory method](https://en.wikipedia.org/wiki/Factory_method_pattern) like `create()`).
- For optional properties that require some complex setting up, [Fluent interface](https://en.wikipedia.org/wiki/Fluent_interface) and [Builder Pattern](https://refactoring.guru/design-patterns/builder) can be used.
- Make Entities partially immutable. Identify what properties shouldn't change after creation and make them `readonly` (for example `id` or `createdAt`).

**Note**: A lot of people tend to create one module per entity, but this approach is not very good. Each module may have multiple entities. One thing to keep in mind is that putting entities in a single module requires those entities to have related business logic, don't group unrelated entities in one module.

Example files:

- [user.entity.ts](src/modules/user/domain/user.entity.ts)
- [wallet.entity.ts](src/modules/wallet/domain/wallet.entity.ts)

Read more:

- [Domain Entity pattern](https://badia-kharroubi.gitbooks.io/microservices-architecture/content/patterns/tactical-patterns/domain-entity-pattern.html)
- [Secure by design: Chapter 6 Ensuring integrity of state](https://livebook.manning.com/book/secure-by-design/chapter-6/)

---

## Aggregates

[Aggregate](https://martinfowler.com/bliki/DDD_Aggregate.html) is a cluster of domain objects that can be treated as a single unit. It encapsulates entities and value objects which conceptually belong together. It also contains a set of operations which those domain objects can be operated on.

- Aggregates help to simplify the domain model by gathering multiple domain objects under a single abstraction.
- Aggregates should not be influenced by the data model. Associations between domain objects are not the same as database relationships.
- Aggregate root is an entity that contains other entities/value objects and all logic to operate them.
- Aggregate root has global identity ([UUID / GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) / primary key). Entities inside the aggregate boundary have local identities, unique only within the Aggregate.
- Aggregate root is a gateway to entire aggregate. Any references from outside the aggregate should **only** go to the aggregate root.
- Any operations on an aggregate must be [transactional operations](https://en.wikipedia.org/wiki/Database_transaction). Either everything gets saved/updated/deleted or nothing.
- Only Aggregate Roots can be obtained directly with database queries. Everything else must be done through traversal.
- Similar to `Entities`, aggregates must protect their invariants through entire lifecycle. When a change to any object within the Aggregate boundary is committed, all invariants of the whole Aggregate must be satisfied. Simply said, all objects in an aggregate must be consistent, meaning that if one object inside an aggregate changes state, this shouldn't conflict with other domain objects inside this aggregate (this is called _Consistency Boundary_).
- Objects within the Aggregate can reference other Aggregate roots via their globally unique identifier (id). Avoid holding a direct object reference.
- Try to avoid aggregates that are too big, this can lead to performance and maintaining problems.
- Aggregates can publish `Domain Events` (more on that below).

All of these rules just come from the idea of creating a boundary around Aggregates. The boundary simplifies business model, as it forces us to consider each relationship very carefully, and within a well-defined set of rules.

In summary, if you combine multiple related entities and value objects inside one root `Entity`, this root `Entity` becomes an `Aggregate Root`, and this cluster of related entities and value objects becomes an `Aggregate`.

Example files:

- [aggregate-root.base.ts](src/libs/ddd/aggregate-root.base.ts) - abstract base class.
- [user.entity.ts](src/modules/user/domain/user.entity.ts) - aggregates are just entities that have to follow a set of specific rules described above.

Read more:

- [Understanding Aggregates in Domain-Driven Design](https://dzone.com/articles/domain-driven-design-aggregate)
- [What Are Aggregates In Domain-Driven Design?](https://www.jamesmichaelhickey.com/domain-driven-design-aggregates/) <- this is a series of multiple articles, don't forget to click "Next article" at the end.
- [Effective Aggregate Design Part I: Modeling a Single Aggregate](https://www.dddcommunity.org/wp-content/uploads/files/pdf_articles/Vernon_2011_1.pdf)
- [Effective Aggregate Design Part II: Making Aggregates Work Together](https://www.dddcommunity.org/wp-content/uploads/files/pdf_articles/Vernon_2011_2.pdf)

---

## Domain Events

Domain Event indicates that something happened in a domain that you want other parts of the same domain (in-process) to be aware of. Domain events are just messages pushed to an in-memory Domain Event dispatcher.

For example, if a user buys something, you may want to:

- Update his shopping cart;
- Withdraw money from his wallet;
- Create a new shipping order;
- Perform other domain operations that are not a concern of an aggregate that executes a "buy" command.

The typical approach involves executing all this logic in a service that performs a "buy" operation. However, this creates coupling between different subdomains.

An alternative approach would be publishing a `Domain Event`. If executing a command related to one aggregate instance requires additional domain rules to be run on one or more additional aggregates, you can design and implement those side effects to be triggered by Domain Events. Propagation of state changes across multiple aggregates within the same domain model can be performed by subscribing to a concrete `Domain Event` and creating as many event handlers as needed. This prevents coupling between aggregates.

Domain Events may be useful for creating an [audit log](https://en.wikipedia.org/wiki/Audit_trail) to track all changes to important entities by saving each event to the database. Read more on why audit logs may be useful: [Why soft deletes are evil and what to do instead](https://jameshalsall.co.uk/posts/why-soft-deletes-are-evil-and-what-to-do-instead).

All changes caused by Domain Events across multiple aggregates in a single process can be saved in a single database [transaction](https://en.wikipedia.org/wiki/Database_transaction). This approach ensures consistency and integrity of your data. Wrapping an entire flow in a transaction or using patterns like [Unit of Work](https://java-design-patterns.com/patterns/unit-of-work/) or similar can help with that.
**Keep in mind** that abusing transactions can create bottlenecks when multiple users try to modify single record concurrently. Use it only when you can afford it, otherwise go for other approaches (like [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)).

There are multiple ways on implementing an event bus for Domain Events, for example by using ideas from patterns like [Mediator](https://refactoring.guru/design-patterns/mediator) or [Observer](https://refactoring.guru/design-patterns/observer).

Examples:

- [user-created.domain-event.ts](src/modules/user/domain/events/user-created.domain-event.ts) - simple object that holds data related to published event.
- [create-wallet-when-user-is-created.domain-event-handler.ts](src/modules/wallet/application/event-handlers/create-wallet-when-user-is-created.domain-event-handler.ts) - this is an example of Domain Event Handler that executes some actions when a domain event is raised (in this case, when user is created it also creates a wallet for that user).
- [sql-repository.base.ts](src/libs/db/sql-repository.base.ts) - repository publishes all domain events for execution when it persists changes to an aggregate.
- [create-user.service.ts](src/modules/user/commands/create-user/create-user.service.ts) - in a service we execute a global transaction to make sure all the changes done by Domain Events across the application are stored atomically (all or nothing).

To have a better understanding on domain events and implementation read this:

- [Domain Event pattern](https://badia-kharroubi.gitbooks.io/microservices-architecture/content/patterns/tactical-patterns/domain-event-pattern.html)
- [Domain events: design and implementation](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation)

**Additional notes**:

- When using only events for complex workflows with a lot of steps, it will be hard to track everything that is happening across the application. One event may trigger another one, then another one, and so on. To track the entire workflow you'll have to go multiple places and search for an event handler for each step, which is hard to maintain. In this case, using a service/orchestrator/mediator might be a preferred approach compared to only using events since you will have an entire workflow in one place. This might create some coupling, but is easier to maintain. Don't rely on events only, pick the right tool for the job.

- In some cases you will not be able to save all changes done by your events to multiple aggregates in a single transaction. For example, if you are using microservices that span transaction between multiple services, or [Event Sourcing pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) that has a single stream per aggregate. In this case saving events across multiple aggregates can be eventually consistent (for example by using [Sagas](https://microservices.io/patterns/data/saga.html) with compensating events or a [Process Manager](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html) or something similar).

## Integration Events

Out-of-process communications (calling microservices, external APIs) are called `Integration Events`. If sending a Domain Event to external process is needed then domain event handler should send an `Integration Event`.

Integration Events usually should be published only after all Domain Events finished executing and saving all changes to the database.

To handle integration events in microservices you may need an external message broker / event bus like [RabbitMQ](https://www.rabbitmq.com/) or [Kafka](https://kafka.apache.org/) together with patterns like [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html), [Change Data Capture](https://en.wikipedia.org/wiki/Change_data_capture), [Sagas](https://microservices.io/patterns/data/saga.html) or a [Process Manager](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html) to maintain [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency).

Read more:

- [Domain Events vs. Integration Events in Domain-Driven Design and microservices architectures](https://devblogs.microsoft.com/cesardelatorre/domain-events-vs-integration-events-in-domain-driven-design-and-microservices-architectures/)

For integration events in distributed systems here are some patterns that may be useful:

- [Saga distributed transactions](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga)
- [Saga vs. Process Manager](https://blog.devarchive.net/2015/11/saga-vs-process-manager.html)
- [The Outbox Pattern](https://www.kamilgrzybek.com/design/the-outbox-pattern/)
- [Event Sourcing pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)

---

## Domain Services

Eric Evans, Domain-Driven Design:

> Domain services are used for "a significant process or transformation in the domain that is not a natural responsibility of an ENTITY or VALUE OBJECT"

- Domain Service is a specific type of domain layer class that is used to execute domain logic that relies on two or more `Entities`.
- Domain Services are used when putting the logic on a particular `Entity` would break encapsulation and require the `Entity` to know about things it really shouldn't be concerned with.
- Domain services are very granular, while application services are a facade purposed with providing an API.
- Domain services operate only on types belonging to the Domain. They contain meaningful concepts that can be found within the Ubiquitous Language. They hold operations that don't fit well into Value Objects or Entities.

---

## Value objects

Some Attributes and behaviors can be moved out of the entity itself and put into `Value Objects`.

Value Objects:

- Have no identity. Equality is determined through structural property.
- Are immutable.
- Can be used as an attribute of `entities` and other `value objects`.
- Explicitly defines and enforces important constraints (invariants).

Value object shouldn’t be just a convenient grouping of attributes but should form a well-defined concept in the domain model. This is true even if it contains only one attribute. When modeled as a conceptual whole, it carries meaning when passed around, and it can uphold its constraints.

Imagine you have a `User` entity which needs to have an `address` of a user. Usually an address is simply a complex value that has no identity in the domain and is composed of multiple other values, like `country`, `street`, `postalCode` etc., so it can be modeled and treated as a `Value Object` with its own business logic.

`Value object` isn’t just a data structure that holds values. It can also encapsulate logic associated with the concept it represents.

Example files:

- [address.value-object.ts](src/modules/user/domain/value-objects/address.value-object.ts)

Read more about Value Objects:

- [Martin Fowler blog](https://martinfowler.com/bliki/ValueObject.html)
- [Value Objects to the rescue](https://medium.com/swlh/value-objects-to-the-rescue-28c563ad97c6).
- [Value Object pattern](https://badia-kharroubi.gitbooks.io/microservices-architecture/content/patterns/tactical-patterns/value-object-pattern.html)

## Domain Invariants

Domain [invariants](<https://en.wikipedia.org/wiki/Invariant_(mathematics)#Invariants_in_computer_science>) are the policies and conditions that are always met for the Domain in particular context. Invariants determine what is possible or what is prohibited in the context.

Invariants enforcement is the responsibility of domain objects (especially of the entities and aggregate roots).

There are a certain number of invariants for an object that should always be true. For example:

- When sending money, amount must always be a positive integer, and there always must be a receiver credit card number in a correct format;
- Client cannot purchase a product that is out of stock;
- Client's wallet cannot have less than 0 balance;
- etc.

If the business has some rules similar to described above, the domain object should not be able to exist without following those rules.

Below we will discuss some validation techniques for your domain objects.

Example files:

- [wallet.entity.ts](src/modules/wallet/domain/wallet.entity.ts) - notice `validate` method. This is a simplified example of enforcing a domain invariant.

Read more:

- [Design validations in the domain model layer](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-model-layer-validations)
- [Why Domain Invariants are critical to build good software?](https://no-kill-switch.ghost.io/why-domain-invariants-are-critical-to-build-good-software/)

### Replacing primitives with Value Objects

Most of the code bases operate on primitive types – `strings`, `numbers` etc. In the Domain Model, this level of abstraction may be too low.

Significant business concepts can be expressed using specific types and classes. `Value Objects` can be used instead primitives to avoid [primitives obsession](https://refactoring.guru/smells/primitive-obsession).
So, for example, `email` of type `string`:

```typescript
const email: string = 'john@gmail.com';
```

could be represented as a `Value Object` instead:

```typescript
export class Email extends ValueObject<string> {
  constructor(value: string) {
    super({ value });
  }

  get value(): string {
    return this.props.value;
  }
}
```

```typescript
const email: Email = new Email('john@gmail.com');
```

Now the only way to make an `email` is to create a new instance of `Email` class first, this ensures it will be validated on creation and a wrong value won't get into `Entities`.

Also, an important behavior of the domain primitive is encapsulated in one place. By having the domain primitive own and control domain operations, you reduce the risk of bugs caused by lack of detailed domain knowledge of the concepts involved in the operation.

Creating an object for primitive values may be cumbersome, but it somewhat forces a developer to study domain more in details instead of just throwing a primitive type without even thinking what that value represents in domain.

Using `Value Objects` for primitive types is also called a `domain primitive`. The concept and naming are proposed in the book ["Secure by Design"](https://www.manning.com/books/secure-by-design).

Using `Value Objects` instead of primitives:

- Makes code easier to understand by using ubiquitous language instead of just `string`.
- Improves security by ensuring invariants of every property.
- Encapsulates specific business rules associated with a value.

`Value Object` can represent a typed value in domain (a _domain primitive_). The goal here is to encapsulate validations and business logic related only to the represented fields and make it impossible to pass around raw values by forcing a creation of valid `Value Objects` first. This object only accepts values which make sense in its context.

If every argument and return value of a method is valid by definition, you’ll have input and output validation in every single method in your codebase without any extra effort. This will make application more resilient to errors and will protect it from a whole class of bugs and security vulnerabilities caused by invalid input data.

> Without domain primitives, the remaining code needs to take care of validation, formatting, comparing, and lots of other details. Entities represent long-lived objects with a distinguished identity, such as articles in a news feed, rooms in a hotel, and shopping carts in online sales. The functionality in a system often centers around changing the state of these objects: hotel rooms are booked, shopping cart contents are
> paid for, and so on. Sooner or later the flow of control will be guided to some code representing these entities. And if all the data is transmitted as generic types such as int or String , responsibilities fall on the entity code to validate, compare, and format the data, among other tasks. The entity code will be burdened with a lot of
> tasks, rather than focusing on the central business flow-of-state changes that it models. Using domain primitives can counteract the tendency for entities to grow overly complex.

Quote from: [Secure by design: Chapter 5.3 Standing on the shoulders of domain primitives](https://livebook.manning.com/book/secure-by-design/chapter-5/96)

Also, an alternative for creating an object may be a [type alias](https://www.typescriptlang.org/brain/knowledge/docs_legacy/handbook/advanced-types.html#type-aliases) (ideally using [nominal types](https://betterprogramming.pub/nominal-typescript-eee36e9432d2)) just to give this primitive a semantic meaning.

**Warning**: Don't include Value Objects in objects that can be sent to other processes, like dtos, events, database models etc. Serialize them to primitive types first.

**Note**: In languages like TypeScript, creating value objects for single values/primitives adds some extra complexity and boilerplate code, since you need to access an underlying value by doing something like `email.value`. Also, it can have performance penalties due to creation of so many objects. This technique works best in languages like [Scala](https://www.scala-lang.org/) with its [value classes](https://docs.scala-lang.org/overviews/core/value-classes.html) that represents such classes as primitives at runtime, meaning that object `Email` will be represented as `String` at runtime.

**Note**: if you are using nodejs, [Runtypes](https://www.npmjs.com/package/runtypes) is a nice library that you can use instead of creating your own value objects for primitives.

**Note**: Some people say that _primitive obsession_ is a code smell, some people consider making a class/object for every primitive may be overengineering (unless you are using Scala with its value classes). For less complex and smaller projects it's definitely an overkill. For bigger projects, there are people who advocate for and against this approach. If you notice that creating a class for every primitive doesn't give you much benefit, create classes just for those primitives that have specific rules or behavior, or just validate only outside of domain using some validation framework. Here are some thoughts on this topic: [From Primitive Obsession to Domain Modelling - Over-engineering?](https://blog.ploeh.dk/2015/01/19/from-primitive-obsession-to-domain-modelling/#7172fd9ca69c467e8123a20f43ea76c2).

Recommended reading:

- [Primitive Obsession — A Code Smell that Hurts People the Most](https://medium.com/the-sixt-india-blog/primitive-obsession-code-smell-that-hurt-people-the-most-5cbdd70496e9)
- [Domain Primitives: what they are and how you can use them to make more secure software](https://freecontent.manning.com/domain-primitives-what-they-are-and-how-you-can-use-them-to-make-more-secure-software/)
- [Value Objects Like a Pro](https://medium.com/@nicolopigna/value-objects-like-a-pro-f1bfc1548c72)
- ["Secure by Design" Chapter 5: Domain Primitives](https://livebook.manning.com/book/secure-by-design/chapter-5/) (a full chapter of the article above)

### Make illegal states unrepresentable

Use Value Objects/Domain Primitives and Types ([Algebraic Data Types (ADT)](https://en.wikipedia.org/wiki/Algebraic_data_type)) to make illegal states impossible to represent in your program.

Some people recommend using objects for every value:

Quote from [John A De Goes](https://twitter.com/jdegoes):

> Making illegal states unrepresentable is all about statically proving that all runtime values (without exception) correspond to valid objects in the business domain. The effect of this technique on eliminating meaningless runtime states is astounding and cannot be overstated.

Let's distinguish two types of protection from illegal states: at **compile time** and at **runtime**.

#### Validation at compile time

Types give useful semantic information to a developer. Good code should be easy to use correctly, and hard to use incorrectly. Types system can be a good help for that. It can prevent some nasty errors at compile time, so IDE will show type errors right away.

The simplest example may be using enums instead of constants, and use those enums as input type for something. When passing anything that is not intended the IDE will show a type error:

```typescript
export enum UserRoles {
  admin = 'admin',
  moderator = 'moderator',
  guest = 'guest',
}

const userRole: UserRoles = 'some string'; // <-- error
```

Or, for example, imagine that business logic requires to have contact info of a person by either having `email`, or `phone`, or both. Both `email` and `phone` could be represented as optional, for example:

```typescript
interface ContactInfo {
  email?: Email;
  phone?: Phone;
}
```

But what happens if both are not provided by a programmer? Business rule violated. Illegal state allowed.

Solution: this could be presented as a [union type](https://www.typescriptlang.org/brain/knowledge/docs_legacy/handbook/unions-and-intersections.html#union-types)

```typescript
type ContactInfo = Email | Phone | [Email, Phone];
```

Now only either `Email`, or `Phone`, or both must be provided. If nothing is provided, the IDE will show a type error right away. Now business rule validation is moved from runtime to **compile time**, which makes the application more secure and gives a faster feedback when something is not used as intended.

This is called a _typestate pattern_.

> The typestate pattern is an API design pattern that encodes information about an object’s run-time state in its compile-time type.

Read more:

- [Making illegal states unrepresentable](https://v5.chriskrycho.com/journal/making-illegal-states-unrepresentable-in-ts/)
- [Typestates Would Have Saved the Roman Republic](https://blog.yoavlavi.com/state-machines-would-have-saved-the-roman-republic/)
- [The Typestate Pattern](https://cliffle.com/blog/rust-typestate/)
- [Make illegal states unrepresentable — but how? The Typestate Pattern in Erlang](https://erszcz.medium.com/make-illegal-states-unrepresentable-but-how-the-typestate-pattern-in-erlang-16b37b090d9d)

#### Validation at runtime

Data should not be trusted. There are a lot of cases when invalid data may end up in a domain. For example, if data comes from external API, database, or if it's just a programmer error.

Things that can't be validated at compile time (like user input) are validated at runtime.

First line of defense is validation of user input DTOs.

Second line of defense are Domain Objects. Entities and value objects have to protect their invariants. Having some validation rules here will protect their state from corruption. You can use techniques like [Design by contract](https://en.wikipedia.org/wiki/Design_by_contract) by defining preconditions in object constructors and checking postconditions and invariants before saving an object to the database.

Enforcing self-validation of your domain objects will inform immediately when data is corrupted. Not validating domain objects allows them to be in an incorrect state, this leads to problems.

By combining compile and runtime validations, using objects instead of primitives, enforcing self-validation and invariants of your domain objects, using Design by contract, [Algebraic Data Types (ADT)](https://en.wikipedia.org/wiki/Algebraic_data_type) and typestate pattern, and other similar techniques, you can achieve an architecture where it's hard, or even impossible, to end up in illegal states, thus improving security and robustness of your application dramatically (at a cost of extra boilerplate code).

**Recommended to read**:

- [Backend Best Practices: Data Validation](https://github.com/Sairyss/backend-best-practices#data-validation)

### Guarding vs validating

You may have noticed that we do validation in multiple places:

1. First when user input is sent to our application. In our example we use DTO decorators: [create-user.request-dto.ts](src/modules/user/commands/create-user/create-user.request.dto.ts).
2. Second time in domain objects, for example: [address.value-object.ts](src/modules/user/domain/value-objects/address.value-object.ts).

So, why are we validating things twice? Let's call a second validation "_guarding_", and distinguish between guarding and validating:

- Guarding is a failsafe mechanism. Domain layer views it as invariants to comply with always-valid domain model.
- Validation is a filtration mechanism. Outside layers view them as input validation rules.

> This difference leads to different treatment of violations of these business rules. An invariant violation in the domain model is an exceptional situation and should be met with throwing an exception. On the other hand, there’s nothing exceptional in external input being incorrect.

The input coming from the outside world should be filtered out before passing it further to the domain model. It’s the first line of defense against data inconsistency. At this stage, any incorrect data is denied with corresponding error messages.
Once the filtration has confirmed that the incoming data is valid it's passed to a domain. When the data enters the always-valid domain boundary, it's assumed to be valid and any violation of this assumption means that you’ve introduced a bug.
Guards help to reveal those bugs. They are the failsafe mechanism, the last line of defense that ensures data in the always-valid boundary is indeed valid. Guards comply with the [Fail Fast principle](https://enterprisecraftsmanship.com/posts/fail-fast-principle) by throwing runtime exceptions.

Domain classes should always guard themselves against becoming invalid.

For preventing null/undefined values, empty objects and arrays, incorrect input length etc. a library of [guards](<https://en.wikipedia.org/wiki/Guard_(computer_science)>) can be created.

Example file: [guard.ts](src/libs/guard.ts)

**Keep in mind** that not all validations/guarding can be done in a single domain object, it should validate only rules shared by all contexts. There are cases when validation may be different depending on a context, or one field may involve another field, or even a different entity. Handle those cases accordingly.

Read more:

- [Refactoring: Guard Clauses](https://medium.com/better-programming/refactoring-guard-clauses-2ceeaa1a9da)
- [Always-Valid Domain Model](https://enterprisecraftsmanship.com/posts/always-valid-domain-model/)

<details>
<summary><b>Note</b>: Using validation library instead of custom guards</summary>

Instead of using custom _guards_ you could use an external validation library, but it's not a good practice to tie domain to external libraries and is not usually recommended.

Although exceptions can be made if needed, especially for very specific validation libraries that validate only one thing (like specific IDs, for example bitcoin wallet address). Tying only one or just few `Value Objects` to such a specific library won't cause any harm. Unlike general purpose validation libraries which will be tied to domain everywhere, and it will be troublesome to change it in every `Value Object` in case when old library is no longer maintained, contains critical bugs or is compromised by hackers etc.

Though, it's fine to do full sanity checks using validation framework or library **outside** the domain (for example [class-validator](https://www.npmjs.com/package/class-validator) decorators in `DTOs`), and do only some basic checks (guarding) inside of domain objects (besides business rules), like checking for `null` or `undefined`, checking length, matching against simple regexp etc. to check if value makes sense and for extra security.

<details>
<summary>Note about using regexp</summary>

Be careful with custom regexp validations for things like validating `email`, only use custom regexp for some very simple rules and, if possible, let validation library do its job on more difficult ones to avoid problems in case your regexp is not good enough.

Also, keep in mind that custom regexp that does same type of validation that is already done by validation library outside of domain may create conflicts between your regexp and the one used by a validation library.

For example, value can be accepted as valid by a validation library, but `Value Object` may throw an error because custom regexp is not good enough (validating `email` is more complex than just copy - pasting a regular expression found in google. Though, it can be validated by a simple rule that is true all the time and won't cause any conflicts, like every `email` must contain an `@`). Try finding and validating only patterns that won't cause conflicts.

---

</details>

Although there are other strategies on how to do validation inside domain, like passing validation schema as a dependency when creating new `Value Object`, but this creates extra complexity.

Either to use external library/framework for validation inside domain or not is a tradeoff, analyze all the pros and cons and choose what is more appropriate for current application.

For some projects, especially smaller ones, it might be easier and more appropriate to just use validation library/framework.

</details>

## Domain Errors

Application's core and domain layers shouldn't throw HTTP exceptions or statuses since it shouldn't know in what context it's used, since it can be used by anything: HTTP controller, Microservice event handler, Command Line Interface etc. A better approach is to create custom error classes with appropriate error codes.

Exceptions are for exceptional situations. Complex domains usually have a lot of errors that are not exceptional, but a part of a business logic (like "seat already booked, choose another one"). Those errors may need special handling. In those cases returning explicit error types can be a better approach than throwing.

Returning an error instead of throwing explicitly shows a type of each exception that a method can return so you can handle it accordingly. It can make an error handling and tracing easier.

To help with that you can create an [Algebraic Data Types (ADT)](https://en.wikipedia.org/wiki/Algebraic_data_type) for your errors and use some kind of Result object type with a Success or a Failure condition (a [monad](<https://en.wikipedia.org/wiki/Monad_(functional_programming)>) like [Either](https://typelevel.org/cats/datatypes/either.html) from functional languages similar to Haskell or Scala). Unlike throwing exceptions, this approach allows defining types (ADTs) for every error and will let you see and handle them explicitly instead of using `try/catch` and avoid throwing exceptions that are invisible at compile time. For example:

```typescript
// User errors:
class UserError extends Error {
  /* ... */
}

class UserAlreadyExistsError extends UserError {
  /* ... */
}

class IncorrectUserAddressError extends UserError {
  /* ... */
}

// ... other user errors
```

```typescript
// Sum type for user errors
type CreateUserError = UserAlreadyExistsError | IncorrectUserAddressError;

function createUser(
  command: CreateUserCommand,
): Result<UserEntity, CreateUserError> {
  // ^ explicitly showing what function returns
  if (await userRepo.exists(command.email)) {
    return Err(new UserAlreadyExistsError()); // <- returning an Error
  }
  if (!validate(command.address)) {
    return Err(new IncorrectUserAddressError());
  }
  // else
  const user = UserEntity.create(command);
  await this.userRepo.save(user);
  return Ok(user);
}
```

This approach gives us a fixed set of expected error types, so we can decide what to do with each:

```typescript
/* in HTTP context we want to convert each error to an 
error with a corresponding HTTP status code: 409, 400 or 500 */
const result = await this.commandBus.execute(command);
return match(result, {
  Ok: (id: string) => new IdResponse(id),
  Err: (error: Error) => {
    if (error instanceof UserAlreadyExistsError)
      throw new ConflictHttpException(error.message);
    if (error instanceof IncorrectUserAddressError)
      throw new BadRequestException(error.message);
    throw error;
  },
});
```

Throwing makes errors invisible for the consumer of your functions/methods (until those errors happen at runtime, or until you dig deeply into the source code and find them). This means those errors are less likely to be handled properly.

Returning errors instead of throwing them adds some extra boilerplate code, but can make your application robust and secure since errors are now explicitly documented and visible as return types. You decide what to do with each error: propagate it further, transform it, add extra metadata, or try to recover from it (for example, by retrying the operation).

**Warning**: Some errors/exceptions are non-recoverable and should be thrown, not returned. If you return technical Exceptions (like connection failed, process out of memory, etc.), It may cause some security issues and goes against [Fail-fast](https://en.wikipedia.org/wiki/Fail-fast) principle. Instead of terminating a program flow immediately and logging the error, returning an exception continues program execution and allows it to run in an incorrect state, which may lead to more unexpected errors, so it's generally better to throw an Exception in those cases rather than returning it. Analyze if the error is "likely recoverable" or "likely unrecoverable". If an error is most likely a recoverable error, it's a great candidate for using it in a Result object. If an error is most likely unrecoverable, throw it.

Libraries you can use:

- [oxide.ts](https://www.npmjs.com/package/oxide.ts) - this is a nice npm package if you want to use a Result object
- [@badrap/result](https://www.npmjs.com/package/@badrap/result) - alternative

Example files:

- [user.errors.ts](src/modules/user/domain/user.errors.ts) - user errors
- [create-user.service.ts](src/modules/user/commands/create-user/create-user.service.ts) - notice how `Err(new UserAlreadyExistsError())` is returned instead of throwing it.
- [create-user.http.controller.ts](src/modules/user/commands/create-user/create-user.http.controller.ts) - in a user http controller we match an error and decide what to do with it. If an error is `UserAlreadyExistsError` we throw a `Conflict Exception` which a user will receive as `409 - Conflict`. If an error is unknown we just throw it and our framework will return it to the user as `500 - Internal Server Error`.
- [create-user.cli.controller.ts](src/modules/user/commands/create-user/create-user.cli.controller.ts) - in a CLI controller we don't care about returning a correct status code so we just `.unwrap()` a result, which will just throw in case of an error.
- [exceptions](src/libs/exceptions) folder contains some generic app exceptions (not domain specific)

Read more:

- [Flexible Error Handling w/ the Result Class](https://khalilstemmler.com/articles/enterprise-typescript-nodejs/handling-errors-result-class/)
- [Advanced error handling techniques](https://enterprisecraftsmanship.com/posts/advanced-error-handling-techniques/)
- ["Secure by Design" Chapter 9.2: Handling failures without exceptions](https://livebook.manning.com/book/secure-by-design/chapter-9/51)
- ["Functional Programming in Scala" Chapter 4. Handling errors without exceptions](https://livebook.manning.com/book/functional-programming-in-scala/chapter-4/)

## Using libraries inside Application's core

Whether to use libraries in application core and especially domain layer is a subject of a lot of debates. In real world, injecting every library instead of importing it directly is not always practical, so exceptions can be made for some single responsibility libraries that help to implement domain logic (like working with numbers).

Main recommendations to keep in mind is that libraries imported in application's core **shouldn't** expose:

- Functionality to access any out-of-process resources (http calls, database access etc);
- Functionality not relevant to domain (frameworks, technology details like ORMs, Logger etc.).
- Functionality that brings randomness (generating random IDs, timestamps etc.) since this makes tests unpredictable (though in TypeScript world it's not that big of a deal since this can be mocked by a test library without using DI);
- If a library changes often or has a lot of dependencies of its own it most likely shouldn't be used in domain layer.

To use such libraries consider creating an `anti-corruption` layer by using [adapter](https://refactoring.guru/design-patterns/adapter) or [facade](https://refactoring.guru/design-patterns/facade) patterns.

We sometimes tolerate libraries in the center, but be careful with general purpose libraries that may scatter across many domain objects. It will be hard to replace those libraries if needed. Tying only one or just a few domain objects to some single-responsibility library should be fine. It's way easier to replace a specific library that is tied to one or few objects than a general purpose library that is everywhere.

In addition to different libraries there are Frameworks. Frameworks can be a real nuisance, because by definition they want to be in control, and it's hard to replace a Framework later when your entire application is glued to it. It's fine to use Frameworks in outside layers (like infrastructure), but keep your domain clean of them when possible. You should be able to extract your domain layer and build a new infrastructure around it using any other framework without breaking your business logic.

NestJS does a good job, as it uses decorators which are not very intrusive, so you could use decorators like `@Inject()` without affecting your business logic at all, and it's relatively easy to remove or replace it when needed. Don't give up on frameworks completely, but keep them in boundaries and don't let them affect your business logic.

Offload as much of irrelevant responsibilities as possible from the core, especially from domain layer. In addition, try to minimize usage of dependencies in general. More dependencies your software has means more potential errors and security holes. One technique for making software more robust is to minimize what your software depends on - the less that can go wrong, the less will go wrong. On the other hand, removing all dependencies would be counterproductive as replicating that functionality would require huge amount of work and would be less reliable than just using a popular, battle-tested library. Finding a good balance is important, this skill requires experience.

Read more:

- [Referencing external libs](https://khorikov.org/posts/2019-08-07-referencing-external-libs/).
- [Anti-corruption Layer — An effective Shield](https://medium.com/@malotor/anticorruption-layer-a-effective-shield-caa4d5ba548c)

---

# Interface Adapters

Interface adapters (also called driving/primary adapters) are user-facing interfaces that take input data from the user and repackage it in a form that is convenient for the use cases(services/command handlers) and entities. Then they take the output from those use cases and entities and repackage it in a form that is convenient for displaying it back for the user. User can be either a person using an application or another server.

Contains `Controllers` and `Request`/`Response` DTOs (can also contain `Views`, like backend-generated HTML templates, if required).

## Controllers

- Controller is a user-facing API that is used for parsing requests, triggering business logic and presenting the result back to the client.
- One controller per use case is considered a good practice.
- In [NestJS](https://docs.nestjs.com/) world controllers may be a good place to use [OpenAPI/Swagger decorators](https://docs.nestjs.com/openapi/operations) for documentation.

One controller per trigger type can be used to have a clearer separation. For example:

- [create-user.http.controller.ts](src/modules/user/commands/create-user/create-user.http.controller.ts) for http requests ([NestJS Controllers](https://docs.nestjs.com/controllers)),
- [create-user.cli.controller.ts](src/modules/user/commands/create-user/create-user.cli.controller.ts) for command line interface access ([NestJS Console](https://www.npmjs.com/package/nestjs-console))
- [create-user.message.controller.ts](src/modules/user/commands/create-user/create-user.message.controller.ts) for external messages ([NestJS Microservices](https://docs.nestjs.com/microservices/basics)).
- etc.

### Resolvers

If you are using [GraphQL](https://graphql.org/) instead of controllers, you will use [Resolvers](https://docs.nestjs.com/graphql/resolvers).

One of the main benefits of a layered architecture is separation of concerns. As you can see, it doesn't matter if you use [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) or GraphQL, the only thing that changes is user-facing API layer (interface-adapters). All the application Core stays the same since it doesn't depend on technology you are using.

Example files:

- [create-user.graphql-resolver.ts](src/modules/user/commands/create-user/graphql-example/create-user.graphql-resolver.ts)

---

## DTOs

Data that comes from external applications should be represented by a special type of classes - Data Transfer Objects ([DTO](https://en.wikipedia.org/wiki/Data_transfer_object) for short).
Data Transfer Object is an object that carries data between processes. It defines a contract between your API and clients.

### Request DTOs

Input data sent by a user.

- Using Request DTOs gives a contract that a client of your API has to follow to make a correct request.

Examples:

- [create-user.request.dto.ts](src/modules/user/commands/create-user/create-user.request.dto.ts)

### Response DTOs

Output data returned to a user.

- Using Response DTOs ensures clients only receive data described in DTOs contract, not everything that your model/entity owns (which may result in data leaks).

Examples:

- [user.response.dto.ts](src/modules/user/dtos/user.response.dto.ts)

---

DTO contracts protect your clients from internal data structure changes that may happen in your API. When internal data models change (like renaming variables or splitting tables), they can still be mapped to match a corresponding DTO to maintain compatibility for anyone using your API.

When updating DTO interfaces, a new version of API can be created by prefixing an endpoint with a version number, for example: `v2/users`. This will make transition painless by preventing breaking compatibility for users that are slow to update their apps that uses your API.

You may have noticed that our [create-user.command.ts](src/modules/user/commands/create-user/create-user.command.ts) contains the same properties as [create-user.request.dto.ts](src/modules/user/commands/create-user/create-user.request.dto.ts).
So why do we need DTOs if we already have Command objects that carry properties? Shouldn't we just have one class to avoid duplication?

> Because commands and DTOs are different things, they tackle different problems. Commands are serializable method calls - calls of the methods in the domain model. Whereas DTOs are the data contracts. The main reason to introduce this separate layer with data contracts is to provide backward compatibility for the clients of your API. Without the DTOs, the API will have breaking changes with every modification of the domain model.

More info on this subject here: [Are CQRS commands part of the domain model?](https://enterprisecraftsmanship.com/posts/cqrs-commands-part-domain-model/) (read "_Commands vs DTOs_" section).

### Additional recommendations

- DTOs should be data-oriented, not object-oriented. Its properties should be mostly primitives. We are not modeling anything here, just sending flat data around.
- When returning a `Response` prefer _whitelisting_ properties over _blacklisting_. This ensures that no sensitive data will leak in case if programmer forgets to blacklist newly added properties that shouldn't be returned to the user.
- If you use the same DTOs in multiple apps (frontend and backend, or between microservices), you can keep them somewhere in a shared directory instead of module directory and create a git submodule or a separate package for sharing them.
- `Request`/`Response` DTO classes may be a good place to use validation and sanitization decorators like [class-validator](https://www.npmjs.com/package/class-validator) and [class-sanitizer](https://www.npmjs.com/package/class-sanitizer) (make sure that all validation errors are gathered first and only then return them to the user, this is called [Notification pattern](https://martinfowler.com/eaaDev/Notification.html). Class-validator does this by default).
- `Request`/`Response` DTO classes may also be a good place to use Swagger/OpenAPI library decorators that [NestJS provides](https://docs.nestjs.com/openapi/types-and-parameters).
- If DTO decorators for validation/documentation are not used, DTO can be just an interface instead of a class.
- Data can be transformed to DTO format using a separate mapper or right in the constructor of a DTO class.

### Local DTOs

Another thing that can be seen in some projects is local DTOs. Some people prefer to never use domain objects (like entities) outside its domain (in `controllers`, for example) and return a plain DTO object instead. This project doesn't use this technique, to avoid extra complexity and boilerplate code like interfaces and data mapping.

[Here](https://martinfowler.com/bliki/LocalDTO.html) are Martin Fowler's thoughts on local DTOs, in short (quote):

> Some people argue for them (DTOs) as part of a Service Layer API because they ensure that service layer clients aren't dependent upon an underlying Domain Model. While that may be handy, I don't think it's worth the cost of all of that data mapping.

Though you may want to introduce Local DTOs when you need to decouple modules properly. For example, when querying from one module to another you don't want to leak your entities between modules. In that case using a Local DTO may be justified.

---

# Infrastructure layer

The Infrastructure layer is responsible for encapsulating technology. You can find there the implementations of database repositories for storing/retrieving business entities, message brokers to emit messages/events, I/O services to access external resources, framework related code and any other code that represents a replaceable detail for the architecture.

It's the most volatile layer. Since the things in this layer are so likely to change, they are kept as far away as possible from the more stable domain layers. Because they are kept separate, it's relatively easy to make changes or swap one component for another.

Infrastructure layer can contain `Adapters`, database related files like `Repositories`, `ORM entities`/`Schemas`, framework related files etc.

## Adapters

- Infrastructure adapters (also called driven/secondary adapters) enable a software system to interact with external systems by receiving, storing and providing data when requested (like persistence, message brokers, sending emails or messages, requesting 3rd party APIs etc).
- Adapters also can be used to interact with different domains inside single process to avoid coupling between those domains.
- Adapters are essentially an implementation of ports. They are not supposed to be called directly in any point in code, only through ports(interfaces).
- Adapters can be used as Anti-Corruption Layer (ACL) for legacy code.

Read more on ACL: [Anti-Corruption Layer: How to Keep Legacy Support from Breaking New Systems](https://www.cloudbees.com/blog/anti-corruption-layer-how-keep-legacy-support-breaking-new-systems)

Adapters should have:

- a `port` somewhere in application/domain layer that it implements;
- a mapper that maps data **from** and **to** domain (if it's needed);
- a DTO/interface for received data;
- a validator to make sure incoming data is not corrupted (validation can reside in DTO class using decorators, or it can be validated by `Value Objects`).

## Repositories

Repositories are abstractions over collections of entities that are living in a database.
They centralize common data access functionality and encapsulate the logic required to access that data. Entities/aggregates can be put into a repository and then retrieved at a later time without domain even knowing where data is saved: in a database, in a file, or some other source.

We use repositories to decouple the infrastructure or technology used to access databases from the domain model layer.

Martin Fowler describes a repository as follows:

> A repository performs the tasks of an intermediary between the domain model layers and data mapping, acting similarly to a set of domain objects in memory. Client objects declaratively build queries and send them to the repositories for answers. Conceptually, a repository encapsulates a set of objects stored in the database and operations that can be performed on them, providing a way that is closer to the persistence layer. Repositories, also, support the purpose of separating, clearly and in one direction, the dependency between the work domain and the data allocation or mapping.

The data flow here looks something like this: repository receives a domain `Entity` from application service, maps it to database schema/ORM format, does required operations (saving/updating/retrieving etc), then maps it back to domain `Entity` format and returns it back to service.

Application's core usually is not allowed to depend on repositories directly, instead it depends on abstractions (ports/interfaces). This makes data retrieval technology-agnostic.

**Note**: in theory, most publications out there recommend abstracting a database with interfaces. In practice, it's not always useful. Most of the projects out there never change database technology (or rewrite most of the code anyway if they do). Another downside is that if you abstract a database you are more likely not using its full potential. This project abstracts repositories with a generic port to make a practical example [repository.port.ts](src/libs/ddd/repository.port.ts), but this doesn't mean you should do that too. Think carefully before using abstractions. More info on this topic: [Should you Abstract the Database?](https://enterprisecraftsmanship.com/posts/should-you-abstract-database/)

Example files:

This project contains abstract repository class that allows to make basic CRUD operations: [sql-repository.base.ts](src/libs/db/sql-repository.base.ts). This base class is then extended by a specific repository, and all specific operations that an entity may need are implemented in that specific repo: [user.repository.ts](src/modules/user/database/user.repository.ts).

Read more:

- [Design the infrastructure persistence layer](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design)
- [Should you use the Repository Pattern? With CQRS, Yes and No!](https://codeopinion.com/should-you-use-the-repository-pattern-with-cqrs-yes-and-no/) - in a read model / query handlers it is not required to use a repository pattern.

## Persistence models

Using a single entity for domain logic and database concerns leads to a database-centric architecture. In DDD world domain model and persistence model should be separated.

Since domain `Entities` have their data modeled so that it best accommodates domain logic, it may be not in the best shape to save in a database. For that purpose `Persistence models` can be created that have a shape that is better represented in a particular database that is used. Domain layer should not know anything about persistence models, and it should not care.

There can be multiple models optimized for different purposes, for example:

- Domain with its own models - `Entities`, `Aggregates` and `Value Objects`.
- Persistence layer with its own models - ORM ([Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)), schemas, read/write models if databases are separated into a read and write db ([CQRS](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation)) etc.

Over time, when the amount of data grows, there may be a need to make some changes in the database like improving performance or data integrity by re-designing some tables or even changing the database entirely. Without an explicit separation between `Domain` and `Persistance` models any change to the database will lead to change in your domain `Entities` or `Aggregates`. For example, when performing a database [normalization](https://en.wikipedia.org/wiki/Database_normalization) data can spread across multiple tables rather than being in one table, or vice-versa for [denormalization](https://en.wikipedia.org/wiki/Denormalization). This may force a team to do a complete refactoring of a domain layer which may cause unexpected bugs and challenges. Separating Domain and Persistence models prevents that.

**Note**: separating domain and persistence models may be overkill for smaller applications. It requires a lot of effort creating and maintaining boilerplate code like mappers and abstractions. Consider all pros and cons before making this decision.

Example files:

- [user.repository.ts](src/modules/user/database/user.repository.ts) <- notice `userSchema` and `UserModel` type that describe how user looks in a database
- [user.mapper.ts](src/modules/user/user.mapper.ts) <- Persistence models should also have a corresponding mapper to map from domain to persistence and back.

For smaller projects you could use [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) libraries like [Typeorm](https://typeorm.io/) for simplicity. But for projects with more complexity ORMs are not flexible and performant enough. For this reason, this project uses raw queries with a [Slonik](https://github.com/gajus/slonik) client library.

Read more:

- [Stack Overflow question: DDD - Persistence Model and Domain Model](https://stackoverflow.com/questions/14024912/ddd-persistence-model-and-domain-model)
- [Just Stop It! The Domain Model Is Not The Persistence Model](https://blog.sapiensworks.com/post/2012/04/07/Just-Stop-It!-The-Domain-Model-Is-Not-The-Persistence-Model.aspx)
- [Comparing SQL, query builders, and ORMs](https://www.prisma.io/dataguide/types/relational/comparing-sql-query-builders-and-orms)
- [Secure by Design: Chapter 6.2.2 ORM frameworks and no-arg constructors](https://livebook.manning.com/book/secure-by-design/chapter-6/40)

## Other things that can be a part of Infrastructure layer

- Framework related files;
- Application logger implementation;
- Infrastructure related events ([Nest-event](https://www.npmjs.com/package/nest-event))
- Periodic cron jobs or tasks launchers ([NestJS Schedule](https://docs.nestjs.com/techniques/task-scheduling));
- Other technology related files.

---

# Other recommendations

## General recommendations on architectures, best practices, design patterns and principles

Different projects most likely will have different requirements. Some principles/patterns in such projects can be implemented in a simplified form, some can be skipped. Follow [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) principle and don't overengineer.

Sometimes complex architecture and principles like [SOLID](https://en.wikipedia.org/wiki/SOLID) can be incompatible with [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) and [KISS](https://en.wikipedia.org/wiki/KISS_principle). A good programmer should be pragmatic and has to be able to combine his skills and knowledge with a common sense to choose the best solution for the problem.

> You need some experience with object-oriented software development in real world projects before they are of any use to you. Furthermore, they don’t tell you when you have found a good solution and when you went too far. Going too far means that you are outside the “scope” of a principle and the expected advantages don’t appear.
> Principles, Heuristics, ‘laws of engineering’ are like hint signs, they are helpful when you know where they are pointing to and you know when you have gone too far. Applying them requires experience, that is trying things out, failing, analyzing, talking to people, failing again, fixing, learning and failing some more. There is no shortcut as far as I know.

**Before implementing any pattern always analyze if benefit given by using it worth extra code complexity**.

> Effective design argues that we need to know the price of a pattern is worth paying - that's its own skill.

Don't blindly follow practices, patterns and architectures just because books and articles say so. Sometimes rewriting a software from scratch is the best solution, and all your efforts to fit in all the patterns and architectural styles you know into the project will be a waste of time. Try to evaluate the cost and benefit of every pattern you implement and avoid overengineering. Remember that architectures, patterns and principles are your tools that may be useful in certain situations, not dogmas that you have to follow blindly.

However, remember:

> It's easier to refactor over-design than it's to refactor no design.

Read more:

- [Which Software Architecture should you pick?](https://youtu.be/8B445kqSKwg)
- [SOLID Principles and the Arts of Finding the Beach](https://sebastiankuebeck.wordpress.com/2017/09/17/solid-principles-and-the-arts-of-finding-the-beach/)
- [Martin Fowler blog: Yagni](https://martinfowler.com/bliki/Yagni.html)
- [7 Software Development Principles That Should Be Embraced Daily](https://betterprogramming.pub/7-software-development-principles-that-should-be-embraced-daily-c26a94ec4ecc?gi=3b5b298ddc23)

## Recommendations for smaller APIs

Be careful when implementing any complex architecture in small-medium sized projects with not a lot of business logic. Some building blocks/patterns/principles may fit well, but others may be an overengineering.

For example:

- Separating code into modules/layers/use-cases, using some building blocks like controllers/services/entities, respecting boundaries and dependency injections etc. may be a good idea for any project.
- But practices like creating an object for every primitive, using `Value Objects` to separate business logic into smaller classes, separating `Domain Models` from `Persistence Models` etc. in projects that are more data-centric and have little or no business logic may only complicate such solutions and add extra boilerplate code, data mapping, maintenance overheads etc. without adding much benefit.

[DDD](https://en.wikipedia.org/wiki/Domain-driven_design) and other practices described here are mostly about creating software with complex business logic. But what would be a better approach for simpler applications?

For applications with not a lot of business logic, where code mostly exists as a glue between database and a client, consider other architectures. The most popular is probably [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). _Model-View-Controller_ is better suited for [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) applications with little business logic since it tends to favor designs where software is mostly the view of the database.

Additional resources:

- [Do you have enough Complexity for a Domain Model (Domain Driven Design)?](https://youtu.be/L1foFiqopIc)

## Behavioral Testing

Behavioral Testing (and also [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development)) is a testing of the external behavior of the program, also known as black box testing.

Domain-Driven Design with its ubiquitous language plays nicely with Behavioral tests.

For BDD tests [Cucumber](https://cucumber.io/) with [Gherkin](https://cucumber.io/brain/knowledge/docs_legacy/gherkin/reference/) syntax can give a structure and meaning to your tests. This way even people not involved in a development can define steps needed for testing. In node.js world [cucumber](https://www.npmjs.com/package/@cucumber/cucumber) or [jest-cucumber](https://www.npmjs.com/package/jest-cucumber) are nice packages to achieve that.

Example files:

- [create-user.feature](tests/user/create-user/create-user.feature) - feature file that contains human-readable Gherkin steps
- [create-user.e2e-spec.ts](tests/user/create-user/create-user.e2e-spec.ts) - e2e / behavioral test

Read more:

- [Backend best practices - Testing](https://github.com/Sairyss/backend-best-practices#testing)

## Folder and File Structure

Some typical approaches are:

- **Layered architecture**: split an entire application into directories divided by functionality, like `controllers`, `services`, `repositories`, etc. For example:

```text
- Controllers
  - UserController
  - WalletController
  - OtherControllers...
- Services
  - UserService
  - WalletService
  - OtherServices...
- Repositories
  - ...
```

This approach makes navigation harder. Every time you need to change some feature, instead of having all related files in the same place (in a module), you have to jump multiple directories to find all related files. This approach usually leads to tight coupling and spaghetti code.

- **Divide application by modules** and split each module by some business domain:

```text
- User
  - UserController
  - UserService
  - UserRepository
- Wallet
  - WalletController
  - WalletService
  - WalletRepository
  ...
```

This looks better. With this approach each module is encapsulated and only contains its own business logic. The only downside is: over time those controllers and services can end up hundreds of lines long, making it difficult to navigate and merge conflicts harder to manage.

- **Divide a module by subcomponents:** use modular approach discussed above and divide each module by slices and use cases. We divide a module further into smaller components:

```text
- User
  - CreateUser
    - CreateUserController
    - CreateUserService
    - CreateUserDTO
  - UpdateUser
    - UpdateUserController
    - UpdateUserService
    - UpdateUserDTO
  - UserRepository
  - UserEntity
- Wallet
  - CreateWallet
    - CreateWalletController
    - CreateWalletService
    - CreateWalletDto
  ...
```

This way each module is further split into highly cohesive subcomponents (by feature). Now when you open the project, instead of just seeing directories like `controllers`, `services`, `repositories`, etc. you can see right away what features application has from just reading directory names.

This approach makes navigation and maintaining easier since all related files are close to each other. It also makes every feature properly encapsulated and gives you an ability to make localized decisions per component, based on each particular feature's needs.

Shared files like domain objects (entities/aggregates), repositories, shared DTOs, interfaces, etc. can be stored outside of feature directory since they are usually reused by multiple subcomponents.

This is called [The Common Closure Principle (CCP)](https://ericbackhage.net/clean-code/the-common-closure-principle/). Folder/file structure in this project uses this principle. Related files that usually change together (and are not used by anything else outside that component) are stored close together.

> The aim here should be to be strategic and place classes that we, from experience, know often changes together into the same component.

Keep in mind that this project's folder/file structure is an example and might not work for everyone. The main recommendations here are:

- Separate your application into modules;
- Keep files that change together close to each other (_Common Closure Principle_ and _Vertical Slicing_);
- Group files by their behavior that changes together, not by a type of functionality that file provides;
- Keep files that are reused by multiple components apart;
- Respect boundaries in your code, keeping files together doesn't mean inner layers can import outer layers;
- Try to avoid a lot of nested folders;
- [Move files around until it feels right](https://dev.to/dance2die/move-files-around-until-it-feels-right-2lek).

There are different approaches to file/folder structuring, choose what suits better for the project/personal preference.

Examples:

- [user](src/modules/user) module.
- [create-user](src/modules/user/commands/create-user) subcomponent.

- [Commands](src/modules/user/commands) directory contains all state changing use cases and each use case inside it contains most of the things that it needs: controller, service, DTOs, command, etc.
- [Queries](src/modules/user/queries) directory is structured in the same way as commands but contains data retrieval use cases.

Read more:

- [Out with the Onion, in with Vertical Slices](https://medium.com/@jacobcunningham/out-with-the-onion-in-with-vertical-slices-c3edfdafe118)
- [[YouTube] Tired of Layers? Vertical Slice Architecture to the rescue!](https://youtu.be/lsddiYwWaOQ)
- [Vertical Slice Architecture](https://jimmybogard.com/vertical-slice-architecture/)
- [Why I don’t like layered architecture for microservices](https://garywoodfine.com/why-i-dont-like-layered-architecture-for-microservices/) - this explains more in details what disadvantages a typical horizontal Layered Architecture have compared to Modular / Vertical Slice architectures.

### File names

Consider giving a descriptive type names to files after a dot "`.`", like `*.service.ts` or `*.entity.ts`. This makes it easier to differentiate what files do what and makes it easier to find those files using [fuzzy search](https://en.wikipedia.org/wiki/Approximate_string_matching) (`CTRL+P` for Windows/Linux and `⌘+P` for MacOS in VSCode to try it out).

Alternatively you could use class names as file names, but consider adding descriptive suffixes like `Service` or `Controller`, etc.

Read more:

- [Angular Style Guides: Separate file names with dots and dashes](https://angular.io/guide/styleguide#separate-file-names-with-dots-and-dashes).

## Enforcing architecture

To make sure everyone in the team adheres to defined architectural practices, use tools and libraries that can analyze and validate dependencies between files and layers.

For example:

```typescript
  // Dependency cruiser example
  {
    name: 'no-domain-deps',
    comment: 'Domain layer cannot depend on api or database layers',
    severity: 'error',
    from: { path: ['domain', 'entity', 'aggregate', 'value-object'] },
    to: { path: ['api', 'controller', 'dtos', 'database', 'repository'] },
  },
```

Snippet of code above will prevent your domain layer to depend on the API layer or database layer. Example config: [.dependency-cruiser.js](.dependency-cruiser.js)

You can also generate graphs like this:

<details>
<summary>Click to see dependency graph</summary>
 <img src="assets/dependency-graph.svg" alt="Dependency graph">
</details>
<br>

Example tools:

- [Dependency cruiser](https://github.com/sverweij/dependency-cruiser) - Validate and visualize dependencies for JavaScript / TypeScript.
- [ArchUnit](https://www.archunit.org/) - library for checking the architecture of Java applications

Read more:

- [Validate Dependencies According to Clean Architecture](https://betterprogramming.pub/validate-dependencies-according-to-clean-architecture-743077ea084c)
- [Clean Architecture Boundaries with Spring Boot and ArchUnit](https://reflectoring.io/java-components-clean-boundaries/)

## Prevent massive inheritance chains

Classes that can be extended should be designed for extensibility and usually should be `abstract`. If class is not designed to be extended, prevent extending it by making class `final`. Don't create inheritance more than 1-2 levels deep since this makes refactoring harder and leads to a bad design. You can use [composition](https://en.wikipedia.org/wiki/Composition_over_inheritance) instead.

**Note**: in TypeScript, unlike other languages, there is no default way to make class `final`. But there is a way around it using a custom decorator.

Example file: [final.decorator.ts](src/libs/decorators/final.decorator.ts)

Read more:

- [When to declare classes final](https://ocramius.github.io/blog/when-to-declare-classes-final/)
- [Final classes by default, why?](https://matthiasnoback.nl/2018/09/final-classes-by-default-why/)
- [Prefer Composition Over Inheritance](https://medium.com/better-programming/prefer-composition-over-inheritance-1602d5149ea1)

---

# Additional resources

- [Backend best practices](https://github.com/Sairyss/backend-best-practices) - more best practices that are used here
- [System Design Patterns](https://github.com/Sairyss/system-design-patterns) - learn system design

## Articles

- [DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together)
- [Hexagonal Architecture](https://www.qwan.eu/2020/08/20/hexagonal-architecture.html)
- [Hexagonal (Ports and Adapters) Architecture](https://medium.com/idealo-tech-blog/hexagonal-ports-adapters-architecture-e3617bcf00a0)
- [Clean architecture series](https://medium.com/@pereiren/clean-architecture-series-part-1-f34ef6b04b62)
- [Clean architecture for the rest of us](https://pusher.com/tutorials/clean-architecture-introduction)
- [An illustrated guide to 12 Factor Apps](https://www.redhat.com/architect/12-factor-app)

## Websites

- [The Twelve-Factor App](https://12factor.net/)
- [Refactoring guru - Catalog of Design Patterns](https://refactoring.guru/design-patterns/catalog)

## Blogs

- [Vladimir Khorikov](https://enterprisecraftsmanship.com/)
- [Derek Comartin](https://codeopinion.com/)
- [Kamil Grzybek](https://www.kamilgrzybek.com/)
- [Martin Fowler](https://martinfowler.com/)
- [Khalil Stemmler](https://khalilstemmler.com)
- [Herberto Graca](https://herbertograca.com/)

## Videos

- [More Testable Code with the Hexagonal Architecture](https://youtu.be/ujb_O6myknY)
- [Playlist: Design Patterns Video Tutorial](https://youtube.com/playlist?list=PLF206E906175C7E07)
- [Playlist: Design Patterns in Object Oriented Programming](https://youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc)
- [Herberto Graca - Making architecture explicit](https://www.youtube.com/watch?v=_yoZN9Sb3PM&feature=youtu.be)

## Books

- ["Domain-Driven Design: Tackling Complexity in the Heart of Software"](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) by Eric Evans
- ["Secure by Design"](https://www.manning.com/books/secure-by-design) by Dan Bergh Johnsson, Daniel Deogun, Daniel Sawano
- ["Implementing Domain-Driven Design"](https://www.amazon.com/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577) by Vaughn Vernon
- ["Clean Architecture: A Craftsman's Guide to Software Structure and Design"](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164/ref=sr_1_1?dchild=1&keywords=clean+architecture&qid=1605343702&s=books&sr=1-1) by Robert Martin
```

## File: `tsconfig.build.json`
```json
{
  "extends": "./tsconfig.json",
  "exclude": ["node_modules", "test", "dist", "**/*spec.ts"]
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "strict": true,
    "module": "commonjs",
    "declaration": true,
    "removeComments": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "allowSyntheticDefaultImports": true,
    "strictPropertyInitialization": false,
    "target": "es2019",
    "sourceMap": true,
    "outDir": "./dist",
    "baseUrl": "./",
    "incremental": true,
    "skipLibCheck": true,
    "strictNullChecks": true,
    "noImplicitAny": false,
    "strictBindCallApply": false,
    "forceConsistentCasingInFileNames": false,
    "noFallthroughCasesInSwitch": false,
    "paths": {
      "@src/*": ["src/*"],
      "@modules/*": ["src/modules/*"],
      "@config/*": ["src/configs/*"],
      "@libs/*": ["src/libs/*"],
      "@tests/*": ["tests/*"]
    }
  }
}
```

## File: `database/getMigrator.ts`
```typescript
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */

import { SlonikMigrator } from '@slonik/migrator';
import { createPool } from 'slonik';
import * as dotenv from 'dotenv';
import * as path from 'path';

// use .env or .env.test depending on NODE_ENV variable
const envPath = path.resolve(
  __dirname,
  process.env.NODE_ENV === 'test' ? '../.env.test' : '../.env',
);
dotenv.config({ path: envPath });

export async function getMigrator() {
  const pool = await createPool(
    `postgres://${process.env.DB_USERNAME}:${process.env.DB_PASSWORD}@${process.env.DB_HOST}/${process.env.DB_NAME}`,
  );

  const migrator = new SlonikMigrator({
    migrationsPath: path.resolve(__dirname, 'migrations'),
    migrationTableName: 'migration',
    slonik: pool,
  } as any);

  return { pool, migrator };
}
```

## File: `database/migrate.ts`
```typescript
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
import { getMigrator } from './getMigrator';

export async function run() {
  const { migrator } = await getMigrator();
  migrator.runAsCLI();
  console.log('Done');
}

run();
```

## File: `database/seed.ts`
```typescript
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
import { getMigrator } from './getMigrator';
import * as fs from 'fs';
import * as path from 'path';

// Utility function to run a migration
export const seed = async (query, file) => {
  console.log(`executing migration: ${file} ...`);
  const { pool, migrator } = await getMigrator();
  await migrator.up();
  await pool.query(query);
  console.log(`${file} migration executed`);
};

const directoryPath = path.join(__dirname, 'seeds');
async function runAll() {
  fs.readdir(directoryPath, async function (err, files) {
    if (err) {
      return console.log('Unable to scan directory: ' + err);
    }
    for (const file of files) {
      const data = fs.readFileSync(path.resolve(directoryPath, file), {
        encoding: 'utf8',
        flag: 'r',
      });
      await seed({ sql: data, values: [], type: 'SLONIK_TOKEN_SQL' }, file);
    }
    console.log('done');
    process.exit(0);
  });
}

runAll();
```

## File: `database/migrations/2022.10.07T13.49.19.users.sql`
```sql
CREATE TABLE "users" (
  "id" character varying NOT NULL,
  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  "email" character varying NOT NULL,
  "country" character varying NOT NULL,
  "postalCode" character varying NOT NULL,
  "street" character varying NOT NULL,
  "role" character varying NOT NULL,
  CONSTRAINT "UQ_e12875dfb3b1d92d7d7c5377e22" UNIQUE ("email"),
  CONSTRAINT "PK_cace4a159ff9f2512dd42373760" PRIMARY KEY ("id")
)
```

## File: `database/migrations/2022.10.07T13.49.54.wallets.sql`
```sql
CREATE TABLE "wallets" (
  "id" character varying NOT NULL,
  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  "balance" integer NOT NULL DEFAULT '0',
  "userId" character varying NOT NULL,
  CONSTRAINT "UQ_35472b1fe48b6330cd349709564" UNIQUE ("userId"),
  CONSTRAINT "PK_bec464dd8d54c39c54fd32e2334" PRIMARY KEY ("id")
)
```

## File: `database/migrations/down/2022.10.07T13.49.19.users.sql`
```sql
DROP TABLE "users"
```

## File: `database/migrations/down/2022.10.07T13.49.54.wallets.sql`
```sql
DROP TABLE "wallets"
```

## File: `database/seeds/users.seed.sql`
```sql
INSERT INTO
  users (
    id,
    "createdAt",
    "updatedAt",
    email,
    country,
    "postalCode",
    street,
    "role"
  )
VALUES
  (
    'f59d0748-d455-4465-b0a8-8d8260b1c877',
    now(),
    now(),
    'john@gmail.com',
    'England',
    '24312',
    'Road Avenue',
    'guest'
  );
```

## File: `database/seeds/wallets.seed.sql`
```sql
INSERT INTO
  wallets (id, "createdAt", "updatedAt", balance, "userId")
VALUES
  (
    gen_random_uuid(),
    now(),
    now(),
    0,
    'f59d0748-d455-4465-b0a8-8d8260b1c877'
  );
```

## File: `docker/docker-compose.yml`
```yaml
version: '3.9'

services:
  postgres:
    container_name: postgres-container
    image: postgres:alpine
    ports:
      - 5432:5432
    environment:
      POSTGRES_USER: 'user'
      POSTGRES_PASSWORD: 'password'
      POSTGRES_DB: 'ddh'
    volumes:
      - ddh-postgres:/var/lib/postgresql/data
    networks:
      - postgres

  pgadmin:
    container_name: pgadmin_container
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@email.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - 5050:80
    networks:
      - postgres

networks:
  postgres:
    driver: bridge

volumes:
  ddh-postgres:
```

## File: `src/app.module.ts`
```typescript
import { Module } from '@nestjs/common';
import { CqrsModule } from '@nestjs/cqrs';
import { SlonikModule } from 'nestjs-slonik';
import { EventEmitterModule } from '@nestjs/event-emitter';
import { UserModule } from '@modules/user/user.module';
import { WalletModule } from '@modules/wallet/wallet.module';
import { RequestContextModule } from 'nestjs-request-context';
import { APP_INTERCEPTOR } from '@nestjs/core';
import { ContextInterceptor } from './libs/application/context/ContextInterceptor';
import { ExceptionInterceptor } from '@libs/application/interceptors/exception.interceptor';
import { postgresConnectionUri } from './configs/database.config';
import { GraphQLModule } from '@nestjs/graphql';
import { ApolloDriver, ApolloDriverConfig } from '@nestjs/apollo';

const interceptors = [
  {
    provide: APP_INTERCEPTOR,
    useClass: ContextInterceptor,
  },
  {
    provide: APP_INTERCEPTOR,
    useClass: ExceptionInterceptor,
  },
];

@Module({
  imports: [
    EventEmitterModule.forRoot(),
    RequestContextModule,
    SlonikModule.forRoot({
      connectionUri: postgresConnectionUri,
    }),
    CqrsModule,
    GraphQLModule.forRoot<ApolloDriverConfig>({
      driver: ApolloDriver,
      autoSchemaFile: true,
    }),

    // Modules
    UserModule,
    WalletModule,
  ],
  controllers: [],
  providers: [...interceptors],
})
export class AppModule {}
```

## File: `src/main.ts`
```typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { ValidationPipe } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  const options = new DocumentBuilder().build();

  const document = SwaggerModule.createDocument(app, options);
  SwaggerModule.setup('docs', app, document);

  app.useGlobalPipes(new ValidationPipe({ transform: true, whitelist: true }));

  app.enableShutdownHooks();

  await app.listen(3000);
}
bootstrap();
```

## File: `src/configs/app.routes.ts`
```typescript
/**
 * Application routes with its version
 * https://github.com/Sairyss/backend-best-practices#api-versioning
 */

// Root
const usersRoot = 'users';
const walletsRoot = 'wallets';

// Api Versions
const v1 = 'v1';

export const routesV1 = {
  version: v1,
  user: {
    root: usersRoot,
    delete: `/${usersRoot}/:id`,
  },
  wallet: {
    root: walletsRoot,
    delete: `/${walletsRoot}/:id`,
  },
};
```

## File: `src/configs/database.config.ts`
```typescript
import { get } from 'env-var';
import '../libs/utils/dotenv';

// https://github.com/Sairyss/backend-best-practices#configuration

export const databaseConfig = {
  type: 'postgres',
  host: get('DB_HOST').required().asString(),
  port: get('DB_PORT').required().asIntPositive(),
  username: get('DB_USERNAME').required().asString(),
  password: get('DB_PASSWORD').required().asString(),
  database: get('DB_NAME').required().asString(),
};

export const postgresConnectionUri = `postgres://${databaseConfig.username}:${databaseConfig.password}@${databaseConfig.host}/${databaseConfig.database}`;
```

## File: `src/libs/guard.ts`
```typescript
export class Guard {
  /**
   * Checks if value is empty. Accepts strings, numbers, booleans, objects and arrays.
   */
  static isEmpty(value: unknown): boolean {
    if (typeof value === 'number' || typeof value === 'boolean') {
      return false;
    }
    if (typeof value === 'undefined' || value === null) {
      return true;
    }
    if (value instanceof Date) {
      return false;
    }
    if (value instanceof Object && !Object.keys(value).length) {
      return true;
    }
    if (Array.isArray(value)) {
      if (value.length === 0) {
        return true;
      }
      if (value.every((item) => Guard.isEmpty(item))) {
        return true;
      }
    }
    if (value === '') {
      return true;
    }

    return false;
  }

  /**
   * Checks length range of a provided number/string/array
   */
  static lengthIsBetween(
    value: number | string | Array<unknown>,
    min: number,
    max: number,
  ): boolean {
    if (Guard.isEmpty(value)) {
      throw new Error(
        'Cannot check length of a value. Provided value is empty',
      );
    }
    const valueLength =
      typeof value === 'number'
        ? Number(value).toString().length
        : value.length;
    if (valueLength >= min && valueLength <= max) {
      return true;
    }
    return false;
  }
}
```

## File: `src/libs/api/api-error.response.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';

export class ApiErrorResponse {
  @ApiProperty({ example: 400 })
  readonly statusCode: number;

  @ApiProperty({ example: 'Validation Error' })
  readonly message: string;

  @ApiProperty({ example: 'Bad Request' })
  readonly error: string;

  @ApiProperty({ example: 'YevPQs' })
  readonly correlationId: string;

  @ApiProperty({
    example: ['incorrect email'],
    description: 'Optional list of sub-errors',
    nullable: true,
    required: false,
  })
  readonly subErrors?: string[];

  constructor(body: ApiErrorResponse) {
    this.statusCode = body.statusCode;
    this.message = body.message;
    this.error = body.error;
    this.correlationId = body.correlationId;
    this.subErrors = body.subErrors;
  }
}
```

## File: `src/libs/api/id.response.dto.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';

export class IdResponse {
  constructor(id: string) {
    this.id = id;
  }

  @ApiProperty({ example: '2cdc8ab1-6d50-49cc-ba14-54e4ac7ec231' })
  readonly id: string;
}
```

## File: `src/libs/api/paginated-query.request.dto.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';
import { Type } from 'class-transformer';
import { IsInt, IsOptional, Max, Min } from 'class-validator';

export class PaginatedQueryRequestDto {
  @IsOptional()
  @IsInt()
  @Min(0)
  @Max(99999)
  @Type(() => Number)
  @ApiProperty({
    example: 10,
    description: 'Specifies a limit of returned records',
    required: false,
  })
  readonly limit?: number;

  @IsOptional()
  @IsInt()
  @Min(0)
  @Max(99999)
  @Type(() => Number)
  @ApiProperty({ example: 0, description: 'Page number', required: false })
  readonly page?: number;
}
```

## File: `src/libs/api/paginated.response.base.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';
import { Paginated } from '../ddd';

export abstract class PaginatedResponseDto<T> extends Paginated<T> {
  @ApiProperty({
    example: 5312,
    description: 'Total number of items',
  })
  readonly count: number;

  @ApiProperty({
    example: 10,
    description: 'Number of items per page',
  })
  readonly limit: number;

  @ApiProperty({ example: 0, description: 'Page number' })
  readonly page: number;

  @ApiProperty({ isArray: true })
  abstract readonly data: readonly T[];
}
```

## File: `src/libs/api/response.base.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';
import { IdResponse } from './id.response.dto';

export interface BaseResponseProps {
  id: string;
  createdAt: Date;
  updatedAt: Date;
}

/**
 * Most of our response objects will have properties like
 * id, createdAt and updatedAt so we can move them to a
 * separate class and extend it to avoid duplication.
 */
export class ResponseBase extends IdResponse {
  constructor(props: BaseResponseProps) {
    super(props.id);
    this.createdAt = new Date(props.createdAt).toISOString();
    this.updatedAt = new Date(props.updatedAt).toISOString();
  }

  @ApiProperty({ example: '2020-11-24T17:43:15.970Z' })
  readonly createdAt: string;

  @ApiProperty({ example: '2020-11-24T17:43:15.970Z' })
  readonly updatedAt: string;
}
```

## File: `src/libs/api/graphql/paginated.graphql-response.base.ts`
```typescript
import { Field, ObjectType, Int } from '@nestjs/graphql';
import { Type } from '@nestjs/common';

export interface IPaginatedType<T> {
  data: T[];
  count: number;
  limit: number;
  page: number;
}

export function PaginatedGraphqlResponse<T>(
  classRef: Type<T>,
): Type<IPaginatedType<T>> {
  @ObjectType({ isAbstract: true })
  abstract class PaginatedType implements IPaginatedType<T> {
    constructor(props: IPaginatedType<T>) {
      this.count = props.count;
      this.limit = props.limit;
      this.page = props.page;
      this.data = props.data;
    }
    @Field(() => Int)
    page: number;

    @Field(() => Int)
    count: number;

    @Field()
    limit: number;

    @Field(() => [classRef])
    readonly data: T[];
  }
  return PaginatedType as Type<IPaginatedType<T>>;
}
```

## File: `src/libs/application/context/AppRequestContext.ts`
```typescript
import { RequestContext } from 'nestjs-request-context';
import { DatabaseTransactionConnection } from 'slonik';

/**
 * Setting some isolated context for each request.
 */

export class AppRequestContext extends RequestContext {
  requestId: string;
  transactionConnection?: DatabaseTransactionConnection; // For global transactions
}

export class RequestContextService {
  static getContext(): AppRequestContext {
    const ctx: AppRequestContext = RequestContext.currentContext.req;
    return ctx;
  }

  static setRequestId(id: string): void {
    const ctx = this.getContext();
    ctx.requestId = id;
  }

  static getRequestId(): string {
    return this.getContext().requestId;
  }

  static getTransactionConnection(): DatabaseTransactionConnection | undefined {
    const ctx = this.getContext();
    return ctx.transactionConnection;
  }

  static setTransactionConnection(
    transactionConnection?: DatabaseTransactionConnection,
  ): void {
    const ctx = this.getContext();
    ctx.transactionConnection = transactionConnection;
  }

  static cleanTransactionConnection(): void {
    const ctx = this.getContext();
    ctx.transactionConnection = undefined;
  }
}
```

## File: `src/libs/application/context/ContextInterceptor.ts`
```typescript
import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { Observable, tap } from 'rxjs';
import { nanoid } from 'nanoid';
import { RequestContextService } from './AppRequestContext';

@Injectable()
export class ContextInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const request = context.switchToHttp().getRequest();

    /**
     * Setting an ID in the global context for each request.
     * This ID can be used as correlation id shown in logs
     */
    const requestId = request?.body?.requestId ?? nanoid(6);

    RequestContextService.setRequestId(requestId);

    return next.handle().pipe(
      tap(() => {
        // Perform cleaning if needed
      }),
    );
  }
}
```

## File: `src/libs/application/interceptors/exception.interceptor.ts`
```typescript
import {
  BadRequestException,
  CallHandler,
  ExecutionContext,
  Logger,
  NestInterceptor,
} from '@nestjs/common';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { ExceptionBase } from '@libs/exceptions';
import { RequestContextService } from '../context/AppRequestContext';
import { ApiErrorResponse } from '@src/libs/api/api-error.response';

export class ExceptionInterceptor implements NestInterceptor {
  private readonly logger: Logger = new Logger(ExceptionInterceptor.name);

  intercept(
    _context: ExecutionContext,
    next: CallHandler,
  ): Observable<ExceptionBase> {
    return next.handle().pipe(
      catchError((err) => {
        // Logging for debugging purposes
        if (err.status >= 400 && err.status < 500) {
          this.logger.debug(
            `[${RequestContextService.getRequestId()}] ${err.message}`,
          );

          const isClassValidatorError =
            Array.isArray(err?.response?.message) &&
            typeof err?.response?.error === 'string' &&
            err.status === 400;
          // Transforming class-validator errors to a different format
          if (isClassValidatorError) {
            err = new BadRequestException(
              new ApiErrorResponse({
                statusCode: err.status,
                message: 'Validation error',
                error: err?.response?.error,
                subErrors: err?.response?.message,
                correlationId: RequestContextService.getRequestId(),
              }),
            );
          }
        }

        // Adding request ID to error message
        if (!err.correlationId) {
          err.correlationId = RequestContextService.getRequestId();
        }

        if (err.response) {
          err.response.correlationId = err.correlationId;
        }

        return throwError(err);
      }),
    );
  }
}
```

## File: `src/libs/db/sql-repository.base.ts`
```typescript
import { RequestContextService } from '@libs/application/context/AppRequestContext';
import { AggregateRoot, PaginatedQueryParams, Paginated } from '@libs/ddd';
import { Mapper } from '@libs/ddd';
import { RepositoryPort } from '@libs/ddd';
import { ConflictException } from '@libs/exceptions';
import { EventEmitter2 } from '@nestjs/event-emitter';
import { None, Option, Some } from 'oxide.ts';
import {
  DatabasePool,
  DatabaseTransactionConnection,
  IdentifierSqlToken,
  MixedRow,
  PrimitiveValueExpression,
  QueryResult,
  QueryResultRow,
  sql,
  SqlSqlToken,
  UniqueIntegrityConstraintViolationError,
} from 'slonik';
import { ZodTypeAny, TypeOf, ZodObject } from 'zod';
import { LoggerPort } from '../ports/logger.port';
import { ObjectLiteral } from '../types';

export abstract class SqlRepositoryBase<
  Aggregate extends AggregateRoot<any>,
  DbModel extends ObjectLiteral,
> implements RepositoryPort<Aggregate>
{
  protected abstract tableName: string;

  protected abstract schema: ZodObject<any>;

  protected constructor(
    private readonly _pool: DatabasePool,
    protected readonly mapper: Mapper<Aggregate, DbModel>,
    protected readonly eventEmitter: EventEmitter2,
    protected readonly logger: LoggerPort,
  ) {}

  async findOneById(id: string): Promise<Option<Aggregate>> {
    const query = sql.type(this.schema)`SELECT * FROM ${sql.identifier([
      this.tableName,
    ])} WHERE id = ${id}`;

    const result = await this.pool.query(query);
    return result.rows[0] ? Some(this.mapper.toDomain(result.rows[0])) : None;
  }

  async findAll(): Promise<Aggregate[]> {
    const query = sql.type(this.schema)`SELECT * FROM ${sql.identifier([
      this.tableName,
    ])}`;

    const result = await this.pool.query(query);

    return result.rows.map(this.mapper.toDomain);
  }

  async findAllPaginated(
    params: PaginatedQueryParams,
  ): Promise<Paginated<Aggregate>> {
    const query = sql.type(this.schema)`
    SELECT * FROM ${sql.identifier([this.tableName])}
    LIMIT ${params.limit}
    OFFSET ${params.offset}
    `;

    const result = await this.pool.query(query);

    const entities = result.rows.map(this.mapper.toDomain);
    return new Paginated({
      data: entities,
      count: result.rowCount,
      limit: params.limit,
      page: params.page,
    });
  }

  async delete(entity: Aggregate): Promise<boolean> {
    entity.validate();
    const query = sql`DELETE FROM ${sql.identifier([
      this.tableName,
    ])} WHERE id = ${entity.id}`;

    this.logger.debug(
      `[${RequestContextService.getRequestId()}] deleting entities ${
        entity.id
      } from ${this.tableName}`,
    );

    const result = await this.pool.query(query);

    await entity.publishEvents(this.logger, this.eventEmitter);

    return result.rowCount > 0;
  }

  /**
   * Inserts an entity to a database
   * (also publishes domain events and waits for completion)
   */
  async insert(entity: Aggregate | Aggregate[]): Promise<void> {
    const entities = Array.isArray(entity) ? entity : [entity];

    const records = entities.map(this.mapper.toPersistence);

    const query = this.generateInsertQuery(records);

    try {
      await this.writeQuery(query, entities);
    } catch (error) {
      if (error instanceof UniqueIntegrityConstraintViolationError) {
        this.logger.debug(
          `[${RequestContextService.getRequestId()}] ${
            (error.originalError as any).detail
          }`,
        );
        throw new ConflictException('Record already exists', error);
      }
      throw error;
    }
  }

  /**
   * Utility method for write queries when you need to mutate an entity.
   * Executes entity validation, publishes events,
   * and does some debug logging.
   * For read queries use `this.pool` directly
   */
  protected async writeQuery<T>(
    sql: SqlSqlToken<
      T extends MixedRow ? T : Record<string, PrimitiveValueExpression>
    >,
    entity: Aggregate | Aggregate[],
  ): Promise<
    QueryResult<
      T extends MixedRow
        ? T extends ZodTypeAny
          ? TypeOf<ZodTypeAny & MixedRow & T>
          : T
        : T
    >
  > {
    const entities = Array.isArray(entity) ? entity : [entity];
    entities.forEach((entity) => entity.validate());
    const entityIds = entities.map((e) => e.id);

    this.logger.debug(
      `[${RequestContextService.getRequestId()}] writing ${
        entities.length
      } entities to "${this.tableName}" table: ${entityIds}`,
    );

    const result = await this.pool.query(sql);

    await Promise.all(
      entities.map((entity) =>
        entity.publishEvents(this.logger, this.eventEmitter),
      ),
    );
    return result;
  }

  /**
   * Utility method to generate insert query for any objects.
   * Use carefully and don't accept non-validated objects.
   *
   * Passing object with { name: string, email: string } will generate
   * a query: INSERT INTO "table" (name, email) VALUES ($1, $2)
   */
  protected generateInsertQuery(
    models: DbModel[],
  ): SqlSqlToken<QueryResultRow> {
    // TODO: generate query from an entire array to insert multiple records at once
    const entries = Object.entries(models[0]);
    const values: any = [];
    const propertyNames: IdentifierSqlToken[] = [];

    entries.forEach((entry) => {
      if (entry[0] && entry[1] !== undefined) {
        propertyNames.push(sql.identifier([entry[0]]));
        if (entry[1] instanceof Date) {
          values.push(sql.timestamp(entry[1]));
        } else {
          values.push(entry[1]);
        }
      }
    });

    const query = sql`INSERT INTO ${sql.identifier([
      this.tableName,
    ])} (${sql.join(propertyNames, sql`, `)}) VALUES (${sql.join(
      values,
      sql`, `,
    )})`;

    const parsedQuery = query;
    return parsedQuery;
  }

  /**
   * start a global transaction to save
   * results of all event handlers in one operation
   */
  public async transaction<T>(handler: () => Promise<T>): Promise<T> {
    return this.pool.transaction(async (connection) => {
      this.logger.debug(
        `[${RequestContextService.getRequestId()}] transaction started`,
      );
      if (!RequestContextService.getTransactionConnection()) {
        RequestContextService.setTransactionConnection(connection);
      }

      try {
        const result = await handler();
        this.logger.debug(
          `[${RequestContextService.getRequestId()}] transaction committed`,
        );
        return result;
      } catch (e) {
        this.logger.debug(
          `[${RequestContextService.getRequestId()}] transaction aborted`,
        );
        throw e;
      } finally {
        RequestContextService.cleanTransactionConnection();
      }
    });
  }

  /**
   * Get database pool.
   * If global request transaction is started,
   * returns a transaction pool.
   */
  protected get pool(): DatabasePool | DatabaseTransactionConnection {
    return (
      RequestContextService.getContext().transactionConnection ?? this._pool
    );
  }
}
```

## File: `src/libs/ddd/aggregate-root.base.ts`
```typescript
import { DomainEvent } from './domain-event.base';
import { Entity } from './entity.base';
import { EventEmitter2 } from '@nestjs/event-emitter';
import { LoggerPort } from '@libs/ports/logger.port';
import { RequestContextService } from '../application/context/AppRequestContext';

export abstract class AggregateRoot<EntityProps> extends Entity<EntityProps> {
  private _domainEvents: DomainEvent[] = [];

  get domainEvents(): DomainEvent[] {
    return this._domainEvents;
  }

  protected addEvent(domainEvent: DomainEvent): void {
    this._domainEvents.push(domainEvent);
  }

  public clearEvents(): void {
    this._domainEvents = [];
  }

  public async publishEvents(
    logger: LoggerPort,
    eventEmitter: EventEmitter2,
  ): Promise<void> {
    await Promise.all(
      this.domainEvents.map(async (event) => {
        logger.debug(
          `[${RequestContextService.getRequestId()}] "${
            event.constructor.name
          }" event published for aggregate ${this.constructor.name} : ${
            this.id
          }`,
        );
        return eventEmitter.emitAsync(event.constructor.name, event);
      }),
    );
    this.clearEvents();
  }
}
```

## File: `src/libs/ddd/command.base.ts`
```typescript
import { RequestContextService } from '@libs/application/context/AppRequestContext';
import { ArgumentNotProvidedException } from '../exceptions';
import { Guard } from '../guard';
import { randomUUID } from 'crypto';

export type CommandProps<T> = Omit<T, 'id' | 'metadata'> & Partial<Command>;

type CommandMetadata = {
  /** ID for correlation purposes (for commands that
   *  arrive from other microservices,logs correlation, etc). */
  readonly correlationId: string;

  /**
   * Causation id to reconstruct execution order if needed
   */
  readonly causationId?: string;

  /**
   * ID of a user who invoked the command. Can be useful for
   * logging and tracking execution of commands and events
   */
  readonly userId?: string;

  /**
   * Time when the command occurred. Mostly for tracing purposes
   */
  readonly timestamp: number;
};

export class Command {
  /**
   * Command id, in case if we want to save it
   * for auditing purposes and create a correlation/causation chain
   */
  readonly id: string;

  readonly metadata: CommandMetadata;

  constructor(props: CommandProps<unknown>) {
    if (Guard.isEmpty(props)) {
      throw new ArgumentNotProvidedException(
        'Command props should not be empty',
      );
    }
    const ctx = RequestContextService.getContext();
    this.id = props.id || randomUUID();
    this.metadata = {
      correlationId: props?.metadata?.correlationId || ctx.requestId,
      causationId: props?.metadata?.causationId,
      timestamp: props?.metadata?.timestamp || Date.now(),
      userId: props?.metadata?.userId,
    };
  }
}
```

## File: `src/libs/ddd/domain-event.base.ts`
```typescript
import { randomUUID } from 'crypto';
import { ArgumentNotProvidedException } from '../exceptions';
import { Guard } from '../guard';
import { RequestContextService } from '@libs/application/context/AppRequestContext';

type DomainEventMetadata = {
  /** Timestamp when this domain event occurred */
  readonly timestamp: number;

  /** ID for correlation purposes (for Integration Events,logs correlation, etc).
   */
  readonly correlationId: string;

  /**
   * Causation id used to reconstruct execution order if needed
   */
  readonly causationId?: string;

  /**
   * User ID for debugging and logging purposes
   */
  readonly userId?: string;
};

export type DomainEventProps<T> = Omit<T, 'id' | 'metadata'> & {
  aggregateId: string;
  metadata?: DomainEventMetadata;
};

export abstract class DomainEvent {
  public readonly id: string;

  /** Aggregate ID where domain event occurred */
  public readonly aggregateId: string;

  public readonly metadata: DomainEventMetadata;

  constructor(props: DomainEventProps<unknown>) {
    if (Guard.isEmpty(props)) {
      throw new ArgumentNotProvidedException(
        'DomainEvent props should not be empty',
      );
    }
    this.id = randomUUID();
    this.aggregateId = props.aggregateId;
    this.metadata = {
      correlationId:
        props?.metadata?.correlationId || RequestContextService.getRequestId(),
      causationId: props?.metadata?.causationId,
      timestamp: props?.metadata?.timestamp || Date.now(),
      userId: props?.metadata?.userId,
    };
  }
}
```

## File: `src/libs/ddd/entity.base.ts`
```typescript
import {
  ArgumentNotProvidedException,
  ArgumentInvalidException,
  ArgumentOutOfRangeException,
} from '../exceptions';
import { Guard } from '../guard';
import { convertPropsToObject } from '../utils';

export type AggregateID = string;

export interface BaseEntityProps {
  id: AggregateID;
  createdAt: Date;
  updatedAt: Date;
}

export interface CreateEntityProps<T> {
  id: AggregateID;
  props: T;
  createdAt?: Date;
  updatedAt?: Date;
}

export abstract class Entity<EntityProps> {
  constructor({
    id,
    createdAt,
    updatedAt,
    props,
  }: CreateEntityProps<EntityProps>) {
    this.setId(id);
    this.validateProps(props);
    const now = new Date();
    this._createdAt = createdAt || now;
    this._updatedAt = updatedAt || now;
    this.props = props;
    this.validate();
  }

  protected readonly props: EntityProps;

  /**
   * ID is set in the concrete entity implementation to support
   * different ID types depending on your needs.
   * For example it could be a UUID for aggregate root,
   * and shortid / nanoid for child entities.
   */
  protected abstract _id: AggregateID;

  private readonly _createdAt: Date;

  private _updatedAt: Date;

  get id(): AggregateID {
    return this._id;
  }

  private setId(id: AggregateID): void {
    this._id = id;
  }

  get createdAt(): Date {
    return this._createdAt;
  }

  get updatedAt(): Date {
    return this._updatedAt;
  }

  static isEntity(entity: unknown): entity is Entity<unknown> {
    return entity instanceof Entity;
  }

  /**
   *  Checks if two entities are the same Entity by comparing ID field.
   * @param object Entity
   */
  public equals(object?: Entity<EntityProps>): boolean {
    if (object === null || object === undefined) {
      return false;
    }

    if (this === object) {
      return true;
    }

    if (!Entity.isEntity(object)) {
      return false;
    }

    return this.id ? this.id === object.id : false;
  }

  /**
   * Returns entity properties.
   * @return {*}  {Props & EntityProps}
   * @memberof Entity
   */
  public getProps(): EntityProps & BaseEntityProps {
    const propsCopy = {
      id: this._id,
      createdAt: this._createdAt,
      updatedAt: this._updatedAt,
      ...this.props,
    };
    return Object.freeze(propsCopy);
  }

  /**
   * Convert an Entity and all sub-entities/Value Objects it
   * contains to a plain object with primitive types. Can be
   * useful when logging an entity during testing/debugging
   */
  public toObject(): unknown {
    const plainProps = convertPropsToObject(this.props);

    const result = {
      id: this._id,
      createdAt: this._createdAt,
      updatedAt: this._updatedAt,
      ...plainProps,
    };
    return Object.freeze(result);
  }

  /**
   * There are certain rules that always have to be true (invariants)
   * for each entity. Validate method is called every time before
   * saving an entity to the database to make sure those rules are respected.
   */
  public abstract validate(): void;

  private validateProps(props: EntityProps): void {
    const MAX_PROPS = 50;

    if (Guard.isEmpty(props)) {
      throw new ArgumentNotProvidedException(
        'Entity props should not be empty',
      );
    }
    if (typeof props !== 'object') {
      throw new ArgumentInvalidException('Entity props should be an object');
    }
    if (Object.keys(props as any).length > MAX_PROPS) {
      throw new ArgumentOutOfRangeException(
        `Entity props should not have more than ${MAX_PROPS} properties`,
      );
    }
  }
}
```

## File: `src/libs/ddd/index.ts`
```typescript
export * from './aggregate-root.base';
export * from './command.base';
export * from './domain-event.base';
export * from './entity.base';
export * from './mapper.interface';
export * from './repository.port';
export * from './value-object.base';
```

## File: `src/libs/ddd/mapper.interface.ts`
```typescript
import { Entity } from './entity.base';

export interface Mapper<
  DomainEntity extends Entity<any>,
  DbRecord,
  Response = any,
> {
  toPersistence(entity: DomainEntity): DbRecord;
  toDomain(record: any): DomainEntity;
  toResponse(entity: DomainEntity): Response;
}
```

## File: `src/libs/ddd/query.base.ts`
```typescript
import { OrderBy, PaginatedQueryParams } from './repository.port';

/**
 * Base class for regular queries
 */
export abstract class QueryBase {}

/**
 * Base class for paginated queries
 */
export abstract class PaginatedQueryBase extends QueryBase {
  limit: number;
  offset: number;
  orderBy: OrderBy;
  page: number;

  constructor(props: PaginatedParams<PaginatedQueryBase>) {
    super();
    this.limit = props.limit || 20;
    this.offset = props.page ? props.page * this.limit : 0;
    this.page = props.page || 0;
    this.orderBy = props.orderBy || { field: true, param: 'desc' };
  }
}

// Paginated query parameters
export type PaginatedParams<T> = Omit<
  T,
  'limit' | 'offset' | 'orderBy' | 'page'
> &
  Partial<Omit<PaginatedQueryParams, 'offset'>>;
```

## File: `src/libs/ddd/repository.port.ts`
```typescript
import { Option } from 'oxide.ts';

/*  Most of repositories will probably need generic 
    save/find/delete operations, so it's easier
    to have some shared interfaces.
    More specific queries should be defined
    in a respective repository.
*/

export class Paginated<T> {
  readonly count: number;
  readonly limit: number;
  readonly page: number;
  readonly data: readonly T[];

  constructor(props: Paginated<T>) {
    this.count = props.count;
    this.limit = props.limit;
    this.page = props.page;
    this.data = props.data;
  }
}

export type OrderBy = { field: string | true; param: 'asc' | 'desc' };

export type PaginatedQueryParams = {
  limit: number;
  page: number;
  offset: number;
  orderBy: OrderBy;
};

export interface RepositoryPort<Entity> {
  insert(entity: Entity | Entity[]): Promise<void>;
  findOneById(id: string): Promise<Option<Entity>>;
  findAll(): Promise<Entity[]>;
  findAllPaginated(params: PaginatedQueryParams): Promise<Paginated<Entity>>;
  delete(entity: Entity): Promise<boolean>;

  transaction<T>(handler: () => Promise<T>): Promise<T>;
}
```

## File: `src/libs/ddd/value-object.base.ts`
```typescript
import { ArgumentNotProvidedException } from '../exceptions';
import { Guard } from '../guard';
import { convertPropsToObject } from '../utils';

/**
 * Domain Primitive is an object that contains only a single value
 */
export type Primitives = string | number | boolean;
export interface DomainPrimitive<T extends Primitives | Date> {
  value: T;
}

type ValueObjectProps<T> = T extends Primitives | Date ? DomainPrimitive<T> : T;

export abstract class ValueObject<T> {
  protected readonly props: ValueObjectProps<T>;

  constructor(props: ValueObjectProps<T>) {
    this.checkIfEmpty(props);
    this.validate(props);
    this.props = props;
  }

  protected abstract validate(props: ValueObjectProps<T>): void;

  static isValueObject(obj: unknown): obj is ValueObject<unknown> {
    return obj instanceof ValueObject;
  }

  /**
   *  Check if two Value Objects are equal. Checks structural equality.
   * @param vo ValueObject
   */
  public equals(vo?: ValueObject<T>): boolean {
    if (vo === null || vo === undefined) {
      return false;
    }
    return JSON.stringify(this) === JSON.stringify(vo);
  }

  /**
   * Unpack a value object to get its raw properties
   */
  public unpack(): T {
    if (this.isDomainPrimitive(this.props)) {
      return this.props.value;
    }

    const propsCopy = convertPropsToObject(this.props);

    return Object.freeze(propsCopy);
  }

  private checkIfEmpty(props: ValueObjectProps<T>): void {
    if (
      Guard.isEmpty(props) ||
      (this.isDomainPrimitive(props) && Guard.isEmpty(props.value))
    ) {
      throw new ArgumentNotProvidedException('Property cannot be empty');
    }
  }

  private isDomainPrimitive(
    obj: unknown,
  ): obj is DomainPrimitive<T & (Primitives | Date)> {
    if (Object.prototype.hasOwnProperty.call(obj, 'value')) {
      return true;
    }
    return false;
  }
}
```

## File: `src/libs/decorators/final.decorator.ts`
```typescript
/* eslint-disable @typescript-eslint/ban-types */
/* eslint-disable @typescript-eslint/no-explicit-any */

/**
 * Prevents other classes extending a class marked by this decorator.
 */
export function final<T extends { new (...args: any[]): object }>(
  target: T,
): T {
  return class Final extends target {
    constructor(...args: any[]) {
      if (new.target !== Final) {
        throw new Error(`Cannot extend a final class "${target.name}"`);
      }
      super(...args);
    }
  };
}
```

## File: `src/libs/decorators/frozen.decorator.ts`
```typescript
/* eslint-disable @typescript-eslint/ban-types */
/**
 * Applies Object.freeze() to a class and it's prototype.
 * Does not freeze all the properties of a class created
 * using 'new' keyword, only static properties and prototype
 * of a class.
 */
export function frozen(constructor: Function): void {
  Object.freeze(constructor);
  Object.freeze(constructor.prototype);
}
```

## File: `src/libs/decorators/index.ts`
```typescript
export * from './final.decorator';
export * from './frozen.decorator';
```

## File: `src/libs/exceptions/exception.base.ts`
```typescript
import { RequestContextService } from '@libs/application/context/AppRequestContext';

export interface SerializedException {
  message: string;
  code: string;
  correlationId: string;
  stack?: string;
  cause?: string;
  metadata?: unknown;
  /**
   * ^ Consider adding optional `metadata` object to
   * exceptions (if language doesn't support anything
   * similar by default) and pass some useful technical
   * information about the exception when throwing.
   * This will make debugging easier.
   */
}

/**
 * Base class for custom exceptions.
 *
 * @abstract
 * @class ExceptionBase
 * @extends {Error}
 */
export abstract class ExceptionBase extends Error {
  abstract code: string;

  public readonly correlationId: string;

  /**
   * @param {string} message
   * @param {ObjectLiteral} [metadata={}]
   * **BE CAREFUL** not to include sensitive info in 'metadata'
   * to prevent leaks since all exception's data will end up
   * in application's log files. Only include non-sensitive
   * info that may help with debugging.
   */
  constructor(
    readonly message: string,
    readonly cause?: Error,
    readonly metadata?: unknown,
  ) {
    super(message);
    Error.captureStackTrace(this, this.constructor);
    const ctx = RequestContextService.getContext();
    this.correlationId = ctx.requestId;
  }

  /**
   * By default in NodeJS Error objects are not
   * serialized properly when sending plain objects
   * to external processes. This method is a workaround.
   * Keep in mind not to return a stack trace to user when in production.
   * https://iaincollins.medium.com/error-handling-in-javascript-a6172ccdf9af
   */
  toJSON(): SerializedException {
    return {
      message: this.message,
      code: this.code,
      stack: this.stack,
      correlationId: this.correlationId,
      cause: JSON.stringify(this.cause),
      metadata: this.metadata,
    };
  }
}
```

## File: `src/libs/exceptions/exception.codes.ts`
```typescript
/**
 * Adding a `code` string with a custom status code for every
 * exception is a good practice, since when that exception
 * is transferred to another process `instanceof` check
 * cannot be performed anymore so a `code` string is used instead.
 * code constants can be stored in a separate file so they
 * can be shared and reused on a receiving side (code sharing is
 * useful when developing fullstack apps or microservices)
 */
export const ARGUMENT_INVALID = 'GENERIC.ARGUMENT_INVALID';
export const ARGUMENT_OUT_OF_RANGE = 'GENERIC.ARGUMENT_OUT_OF_RANGE';
export const ARGUMENT_NOT_PROVIDED = 'GENERIC.ARGUMENT_NOT_PROVIDED';
export const NOT_FOUND = 'GENERIC.NOT_FOUND';
export const CONFLICT = 'GENERIC.CONFLICT';
export const INTERNAL_SERVER_ERROR = 'GENERIC.INTERNAL_SERVER_ERROR';
```

## File: `src/libs/exceptions/exceptions.ts`
```typescript
import {
  ARGUMENT_INVALID,
  ARGUMENT_NOT_PROVIDED,
  ARGUMENT_OUT_OF_RANGE,
  CONFLICT,
  INTERNAL_SERVER_ERROR,
  NOT_FOUND,
} from '.';
import { ExceptionBase } from './exception.base';

/**
 * Used to indicate that an incorrect argument was provided to a method/function/class constructor
 *
 * @class ArgumentInvalidException
 * @extends {ExceptionBase}
 */
export class ArgumentInvalidException extends ExceptionBase {
  readonly code = ARGUMENT_INVALID;
}

/**
 * Used to indicate that an argument was not provided (is empty object/array, null of undefined).
 *
 * @class ArgumentNotProvidedException
 * @extends {ExceptionBase}
 */
export class ArgumentNotProvidedException extends ExceptionBase {
  readonly code = ARGUMENT_NOT_PROVIDED;
}

/**
 * Used to indicate that an argument is out of allowed range
 * (for example: incorrect string/array length, number not in allowed min/max range etc)
 *
 * @class ArgumentOutOfRangeException
 * @extends {ExceptionBase}
 */
export class ArgumentOutOfRangeException extends ExceptionBase {
  readonly code = ARGUMENT_OUT_OF_RANGE;
}

/**
 * Used to indicate conflicting entities (usually in the database)
 *
 * @class ConflictException
 * @extends {ExceptionBase}
 */
export class ConflictException extends ExceptionBase {
  readonly code = CONFLICT;
}

/**
 * Used to indicate that entity is not found
 *
 * @class NotFoundException
 * @extends {ExceptionBase}
 */
export class NotFoundException extends ExceptionBase {
  static readonly message = 'Not found';

  constructor(message = NotFoundException.message) {
    super(message);
  }

  readonly code = NOT_FOUND;
}

/**
 * Used to indicate an internal server error that does not fall under all other errors
 *
 * @class InternalServerErrorException
 * @extends {ExceptionBase}
 */
export class InternalServerErrorException extends ExceptionBase {
  static readonly message = 'Internal server error';

  constructor(message = InternalServerErrorException.message) {
    super(message);
  }

  readonly code = INTERNAL_SERVER_ERROR;
}
```

## File: `src/libs/exceptions/index.ts`
```typescript
export * from './exception.base';
export * from './exception.codes';
export * from './exceptions';
```

## File: `src/libs/ports/logger.port.ts`
```typescript
export interface LoggerPort {
  log(message: string, ...meta: unknown[]): void;
  error(message: string, trace?: unknown, ...meta: unknown[]): void;
  warn(message: string, ...meta: unknown[]): void;
  debug(message: string, ...meta: unknown[]): void;
}
```

## File: `src/libs/types/deep-partial.type.ts`
```typescript
/**
 * Applies Partial utility type to all nested objects.
 */
export type DeepPartial<T> = {
  [P in keyof T]?: DeepPartial<T[P]>;
};
```

## File: `src/libs/types/index.ts`
```typescript
/** Consider creating a bunch of shared custom utility
 * types for different situations.
 * Alternatively you can use a library like
 * https://github.com/andnp/SimplyTyped
 */
export * from './deep-partial.type';
export * from './non-function-properties.type';
export * from './object-literal.type';
export * from './require-one.type';
export * from './mutable.type';
```

## File: `src/libs/types/mutable.type.ts`
```typescript
/**
 * Makes all properties of the type mutable
 * (removes readonly flag)
 */
export type Mutable<T> = {
  -readonly [key in keyof T]: T[key];
};

/**
 * Makes all properties of the type mutable recursively
 * (removes readonly flag, including in nested objects)
 */
export type DeepMutable<T> = { -readonly [P in keyof T]: DeepMutable<T[P]> };
```

## File: `src/libs/types/non-function-properties.type.ts`
```typescript
export type NonFunctionPropertyNames<T> = {
  // eslint-disable-next-line @typescript-eslint/ban-types
  [K in keyof T]: T[K] extends Function ? never : K;
}[keyof T];

/**
 * Exclude all function properties from type.
 */
export type NonFunctionProperties<T> = Pick<T, NonFunctionPropertyNames<T>>;
```

## File: `src/libs/types/object-literal.type.ts`
```typescript
/**
 * Interface of the simple literal object with any string keys.
 */
export interface ObjectLiteral {
  [key: string]: unknown;
}
```

## File: `src/libs/types/require-one.type.ts`
```typescript
/**
 * Makes an interface with all optional values to require AT LEAST one of them.
 */
export type RequireAtLeastOne<T, Keys extends keyof T = keyof T> = Pick<
  T,
  Exclude<keyof T, Keys>
> &
  {
    [K in Keys]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<Keys, K>>>;
  }[Keys];

/* Makes an interface with all optional values to accept ONLY one of them */
export type RequireOnlyOne<T, Keys extends keyof T = keyof T> = Pick<
  T,
  Exclude<keyof T, Keys>
> &
  {
    [K in Keys]-?: Required<Pick<T, K>> &
      Partial<Record<Exclude<Keys, K>, undefined>>;
  }[Keys];
```

## File: `src/libs/utils/convert-props-to-object.util.ts`
```typescript
/* eslint-disable @typescript-eslint/no-explicit-any, @typescript-eslint/explicit-module-boundary-types */
import { Entity } from '../ddd/entity.base';
import { ValueObject } from '../ddd/value-object.base';

function isEntity(obj: unknown): obj is Entity<unknown> {
  /**
   * 'instanceof Entity' causes error here for some reason.
   * Probably creates some circular dependency. This is a workaround
   * until I find a solution :)
   */
  return (
    Object.prototype.hasOwnProperty.call(obj, 'toObject') &&
    Object.prototype.hasOwnProperty.call(obj, 'id') &&
    ValueObject.isValueObject((obj as Entity<unknown>).id)
  );
}

function convertToPlainObject(item: any): any {
  if (ValueObject.isValueObject(item)) {
    return item.unpack();
  }
  if (isEntity(item)) {
    return item.toObject();
  }
  return item;
}

/**
 * Converts Entity/Value Objects props to a plain object.
 * Useful for testing and debugging.
 * @param props
 */
export function convertPropsToObject(props: any): any {
  const propsCopy = structuredClone(props);

  // eslint-disable-next-line guard-for-in
  for (const prop in propsCopy) {
    if (Array.isArray(propsCopy[prop])) {
      propsCopy[prop] = (propsCopy[prop] as Array<unknown>).map((item) => {
        return convertToPlainObject(item);
      });
    }
    propsCopy[prop] = convertToPlainObject(propsCopy[prop]);
  }

  return propsCopy;
}
```

## File: `src/libs/utils/dotenv.ts`
```typescript
import { config } from 'dotenv';
import * as path from 'path';

// Initializing dotenv
const envPath: string = path.resolve(
  __dirname,
  process.env.NODE_ENV === 'test' ? '../../../.env.test' : '../../../../.env',
);
config({ path: envPath });
```

## File: `src/libs/utils/index.ts`
```typescript
export * from './convert-props-to-object.util';
```

## File: `src/modules/user/user.di-tokens.ts`
```typescript
// Tokens used for Dependency Injection

export const USER_REPOSITORY = Symbol('USER_REPOSITORY');
```

## File: `src/modules/user/user.mapper.ts`
```typescript
import { Mapper } from '@libs/ddd';
import { UserModel, userSchema } from './database/user.repository';
import { Address } from './domain/value-objects/address.value-object';
import { UserEntity } from './domain/user.entity';
import { UserResponseDto } from './dtos/user.response.dto';
import { Injectable } from '@nestjs/common';

/**
 * Mapper constructs objects that are used in different layers:
 * Record is an object that is stored in a database,
 * Entity is an object that is used in application domain layer,
 * and a ResponseDTO is an object returned to a user (usually as json).
 */

@Injectable()
export class UserMapper
  implements Mapper<UserEntity, UserModel, UserResponseDto>
{
  toPersistence(entity: UserEntity): UserModel {
    const copy = entity.getProps();
    const record: UserModel = {
      id: copy.id,
      createdAt: copy.createdAt,
      updatedAt: copy.updatedAt,
      email: copy.email,
      country: copy.address.country,
      postalCode: copy.address.postalCode,
      street: copy.address.street,
      role: copy.role,
    };
    return userSchema.parse(record);
  }

  toDomain(record: UserModel): UserEntity {
    const entity = new UserEntity({
      id: record.id,
      createdAt: new Date(record.createdAt),
      updatedAt: new Date(record.updatedAt),
      props: {
        email: record.email,
        role: record.role,
        address: new Address({
          street: record.street,
          postalCode: record.postalCode,
          country: record.country,
        }),
      },
    });
    return entity;
  }

  toResponse(entity: UserEntity): UserResponseDto {
    const props = entity.getProps();
    const response = new UserResponseDto(entity);
    response.email = props.email;
    response.country = props.address.country;
    response.postalCode = props.address.postalCode;
    response.street = props.address.street;
    return response;
  }

  /* ^ Data returned to the user is whitelisted to avoid leaks.
     If a new property is added, like password or a
     credit card number, it won't be returned
     unless you specifically allow this.
     (avoid blacklisting, which will return everything
      but blacklisted items, which can lead to a data leak).
  */
}
```

## File: `src/modules/user/user.module.ts`
```typescript
import { Logger, Module, Provider } from '@nestjs/common';
import { UserRepository } from './database/user.repository';
import { CreateUserHttpController } from './commands/create-user/create-user.http.controller';
import { DeleteUserHttpController } from './commands/delete-user/delete-user.http-controller';
import { CreateUserCliController } from './commands/create-user/create-user.cli.controller';
import { FindUsersHttpController } from './queries/find-users/find-users.http.controller';
import { CreateUserMessageController } from './commands/create-user/create-user.message.controller';
import { CreateUserGraphqlResolver } from './commands/create-user/graphql-example/create-user.graphql-resolver';
import { CreateUserService } from './commands/create-user/create-user.service';
import { DeleteUserService } from './commands/delete-user/delete-user.service';
import { FindUsersQueryHandler } from './queries/find-users/find-users.query-handler';
import { UserMapper } from './user.mapper';
import { CqrsModule } from '@nestjs/cqrs';
import { USER_REPOSITORY } from './user.di-tokens';
import { FindUsersGraphqlResolver } from './queries/find-users/find-users.graphql-resolver';

const httpControllers = [
  CreateUserHttpController,
  DeleteUserHttpController,
  FindUsersHttpController,
];

const messageControllers = [CreateUserMessageController];

const cliControllers: Provider[] = [CreateUserCliController];

const graphqlResolvers: Provider[] = [
  CreateUserGraphqlResolver,
  FindUsersGraphqlResolver,
];

const commandHandlers: Provider[] = [CreateUserService, DeleteUserService];

const queryHandlers: Provider[] = [FindUsersQueryHandler];

const mappers: Provider[] = [UserMapper];

const repositories: Provider[] = [
  { provide: USER_REPOSITORY, useClass: UserRepository },
];

@Module({
  imports: [CqrsModule],
  controllers: [...httpControllers, ...messageControllers],
  providers: [
    Logger,
    ...cliControllers,
    ...repositories,
    ...graphqlResolvers,
    ...commandHandlers,
    ...queryHandlers,
    ...mappers,
  ],
})
export class UserModule {}
```

## File: `src/modules/user/commands/create-user/create-user.cli.controller.ts`
```typescript
import { Inject, Logger } from '@nestjs/common';
import { Command, Console } from 'nestjs-console';
import { CommandBus } from '@nestjs/cqrs';
import { CreateUserCommand } from './create-user.command';
import { LoggerPort } from '@libs/ports/logger.port';

// Allows creating a user using CLI (Command Line Interface)
@Console({
  command: 'new',
  description: 'A command to create a user',
})
export class CreateUserCliController {
  constructor(
    private readonly commandBus: CommandBus,
    @Inject(Logger)
    private readonly logger: LoggerPort,
  ) {}

  @Command({
    command: 'user <email> <country> <postalCode> <street>',
    description: 'Create a user',
  })
  async createUser(
    email: string,
    country: string,
    postalCode: string,
    street: string,
  ): Promise<void> {
    const command = new CreateUserCommand({
      email,
      country,
      postalCode,
      street,
    });

    const result = await this.commandBus.execute(command);

    this.logger.log('User created:', result.unwrap());
  }
}
```

## File: `src/modules/user/commands/create-user/create-user.command.ts`
```typescript
import { Command, CommandProps } from '@libs/ddd';

export class CreateUserCommand extends Command {
  readonly email: string;

  readonly country: string;

  readonly postalCode: string;

  readonly street: string;

  constructor(props: CommandProps<CreateUserCommand>) {
    super(props);
    this.email = props.email;
    this.country = props.country;
    this.postalCode = props.postalCode;
    this.street = props.street;
  }
}
```

## File: `src/modules/user/commands/create-user/create-user.http.controller.ts`
```typescript
import {
  Body,
  ConflictException as ConflictHttpException,
  Controller,
  HttpStatus,
  Post,
} from '@nestjs/common';
import { routesV1 } from '@config/app.routes';
import { ApiOperation, ApiResponse } from '@nestjs/swagger';
import { CommandBus } from '@nestjs/cqrs';
import { match, Result } from 'oxide.ts';
import { CreateUserCommand } from './create-user.command';
import { CreateUserRequestDto } from './create-user.request.dto';
import { UserAlreadyExistsError } from '@modules/user/domain/user.errors';
import { IdResponse } from '@libs/api/id.response.dto';
import { AggregateID } from '@libs/ddd';
import { ApiErrorResponse } from '@src/libs/api/api-error.response';

@Controller(routesV1.version)
export class CreateUserHttpController {
  constructor(private readonly commandBus: CommandBus) {}

  @ApiOperation({ summary: 'Create a user' })
  @ApiResponse({
    status: HttpStatus.OK,
    type: IdResponse,
  })
  @ApiResponse({
    status: HttpStatus.CONFLICT,
    description: UserAlreadyExistsError.message,
    type: ApiErrorResponse,
  })
  @ApiResponse({
    status: HttpStatus.BAD_REQUEST,
    type: ApiErrorResponse,
  })
  @Post(routesV1.user.root)
  async create(@Body() body: CreateUserRequestDto): Promise<IdResponse> {
    const command = new CreateUserCommand(body);

    const result: Result<AggregateID, UserAlreadyExistsError> =
      await this.commandBus.execute(command);

    // Deciding what to do with a Result (similar to Rust matching)
    // if Ok we return a response with an id
    // if Error decide what to do with it depending on its type
    return match(result, {
      Ok: (id: string) => new IdResponse(id),
      Err: (error: Error) => {
        if (error instanceof UserAlreadyExistsError)
          throw new ConflictHttpException(error.message);
        throw error;
      },
    });
  }
}
```

## File: `src/modules/user/commands/create-user/create-user.message.controller.ts`
```typescript
import { Controller } from '@nestjs/common';
import { MessagePattern } from '@nestjs/microservices';
import { CommandBus } from '@nestjs/cqrs';
import { CreateUserCommand } from './create-user.command';
import { CreateUserRequestDto } from './create-user.request.dto';
import { IdResponse } from '@libs/api/id.response.dto';

@Controller()
export class CreateUserMessageController {
  constructor(private readonly commandBus: CommandBus) {}

  @MessagePattern('user.create') // <- Subscribe to a microservice message
  async create(message: CreateUserRequestDto): Promise<IdResponse> {
    const command = new CreateUserCommand(message);

    const id = await this.commandBus.execute(command);

    return new IdResponse(id.unwrap());
  }
}
```

## File: `src/modules/user/commands/create-user/create-user.request.dto.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';
import {
  IsAlphanumeric,
  IsEmail,
  IsString,
  Matches,
  MaxLength,
  MinLength,
} from 'class-validator';

export class CreateUserRequestDto {
  @ApiProperty({
    example: 'john@gmail.com',
    description: 'User email address',
  })
  @MaxLength(320)
  @MinLength(5)
  @IsEmail()
  readonly email: string;

  @ApiProperty({ example: 'France', description: 'Country of residence' })
  @MaxLength(50)
  @MinLength(4)
  @IsString()
  @Matches(/^[a-zA-Z ]*$/)
  readonly country: string;

  @ApiProperty({ example: '28566', description: 'Postal code' })
  @MaxLength(10)
  @MinLength(4)
  @IsAlphanumeric()
  readonly postalCode: string;

  @ApiProperty({ example: 'Grande Rue', description: 'Street' })
  @MaxLength(50)
  @MinLength(5)
  @Matches(/^[a-zA-Z ]*$/)
  readonly street: string;
}
```

## File: `src/modules/user/commands/create-user/create-user.service.ts`
```typescript
import { UserRepositoryPort } from '@modules/user/database/user.repository.port';
import { Address } from '@modules/user/domain/value-objects/address.value-object';
import { CommandHandler, ICommandHandler } from '@nestjs/cqrs';
import { Err, Ok, Result } from 'oxide.ts';
import { CreateUserCommand } from './create-user.command';
import { UserAlreadyExistsError } from '@modules/user/domain/user.errors';
import { AggregateID } from '@libs/ddd';
import { UserEntity } from '@modules/user/domain/user.entity';
import { ConflictException } from '@libs/exceptions';
import { Inject } from '@nestjs/common';
import { USER_REPOSITORY } from '../../user.di-tokens';

@CommandHandler(CreateUserCommand)
export class CreateUserService implements ICommandHandler {
  constructor(
    @Inject(USER_REPOSITORY)
    protected readonly userRepo: UserRepositoryPort,
  ) {}

  async execute(
    command: CreateUserCommand,
  ): Promise<Result<AggregateID, UserAlreadyExistsError>> {
    const user = UserEntity.create({
      email: command.email,
      address: new Address({
        country: command.country,
        postalCode: command.postalCode,
        street: command.street,
      }),
    });

    try {
      /* Wrapping operation in a transaction to make sure
         that all domain events are processed atomically */
      await this.userRepo.transaction(async () => this.userRepo.insert(user));
      return Ok(user.id);
    } catch (error: any) {
      if (error instanceof ConflictException) {
        return Err(new UserAlreadyExistsError(error));
      }
      throw error;
    }
  }
}
```

## File: `src/modules/user/commands/create-user/graphql-example/create-user.graphql-resolver.ts`
```typescript
import { Args, Mutation, Resolver } from '@nestjs/graphql';
import { CommandBus } from '@nestjs/cqrs';
import { CreateUserCommand } from '../create-user.command';
import { CreateUserGqlRequestDto } from './dtos/create-user.gql-request.dto';
import { IdGqlResponse } from './dtos/id.gql-response.dto';
import { AggregateID } from '@src/libs/ddd';
import { UserAlreadyExistsError } from '@src/modules/user/domain/user.errors';
import { Result } from 'oxide.ts';

// If you are Using GraphQL you'll need a Resolver instead of a Controller
@Resolver()
export class CreateUserGraphqlResolver {
  constructor(private readonly commandBus: CommandBus) {}

  @Mutation(() => IdGqlResponse)
  async create(
    @Args('input') input: CreateUserGqlRequestDto,
  ): Promise<IdGqlResponse> {
    const command = new CreateUserCommand(input);

    const id: Result<AggregateID, UserAlreadyExistsError> =
      await this.commandBus.execute(command);

    return new IdGqlResponse(id.unwrap());
  }
}
```

## File: `src/modules/user/commands/create-user/graphql-example/dtos/create-user.gql-request.dto.ts`
```typescript
import { ArgsType, Field, InputType } from '@nestjs/graphql';
import {
  IsAlphanumeric,
  IsEmail,
  IsString,
  Matches,
  MaxLength,
  MinLength,
} from 'class-validator';

@ArgsType()
@InputType()
export class CreateUserGqlRequestDto {
  @MaxLength(320)
  @MinLength(5)
  @IsEmail()
  @Field()
  readonly email: string;

  @MaxLength(50)
  @MinLength(4)
  @IsString()
  @Matches(/^[a-zA-Z ]*$/)
  @Field()
  readonly country: string;

  @MaxLength(10)
  @MinLength(4)
  @IsAlphanumeric()
  @Field()
  readonly postalCode: string;

  @MaxLength(50)
  @MinLength(5)
  @Matches(/^[a-zA-Z ]*$/)
  @Field()
  readonly street: string;
}
```

## File: `src/modules/user/commands/create-user/graphql-example/dtos/id.gql-response.dto.ts`
```typescript
import { Field, ObjectType } from '@nestjs/graphql';

@ObjectType()
export class IdGqlResponse {
  constructor(id: string) {
    this.id = id;
  }

  @Field()
  readonly id: string;
}
```

## File: `src/modules/user/commands/delete-user/delete-user.http-controller.ts`
```typescript
import {
  Controller,
  Delete,
  HttpStatus,
  NotFoundException as NotFoundHttpException,
  Param,
} from '@nestjs/common';
import { routesV1 } from '@config/app.routes';
import { CommandBus } from '@nestjs/cqrs';
import { DeleteUserCommand } from './delete-user.service';
import { match, Result } from 'oxide.ts';
import { NotFoundException } from '@libs/exceptions';
import { ApiOperation, ApiResponse } from '@nestjs/swagger';
import { ApiErrorResponse } from '@src/libs/api/api-error.response';

@Controller(routesV1.version)
export class DeleteUserHttpController {
  constructor(private readonly commandBus: CommandBus) {}

  @ApiOperation({ summary: 'Delete a user' })
  @ApiResponse({
    description: 'User deleted',
    status: HttpStatus.OK,
  })
  @ApiResponse({
    status: HttpStatus.NOT_FOUND,
    description: NotFoundException.message,
    type: ApiErrorResponse,
  })
  @Delete(routesV1.user.delete)
  async deleteUser(@Param('id') id: string): Promise<void> {
    const command = new DeleteUserCommand({ userId: id });
    const result: Result<boolean, NotFoundException> =
      await this.commandBus.execute(command);

    match(result, {
      Ok: (isOk: boolean) => isOk,
      Err: (error: Error) => {
        if (error instanceof NotFoundException)
          throw new NotFoundHttpException(error.message);
        throw error;
      },
    });
  }
}
```

## File: `src/modules/user/commands/delete-user/delete-user.service.ts`
```typescript
import { NotFoundException } from '@libs/exceptions';
import { UserRepositoryPort } from '@modules/user/database/user.repository.port';
import { Inject } from '@nestjs/common';
import { CommandHandler } from '@nestjs/cqrs';
import { Err, Ok, Result } from 'oxide.ts';
import { USER_REPOSITORY } from '../../user.di-tokens';

export class DeleteUserCommand {
  readonly userId: string;

  constructor(props: DeleteUserCommand) {
    this.userId = props.userId;
  }
}

@CommandHandler(DeleteUserCommand)
export class DeleteUserService {
  constructor(
    @Inject(USER_REPOSITORY)
    private readonly userRepo: UserRepositoryPort,
  ) {}

  async execute(
    command: DeleteUserCommand,
  ): Promise<Result<boolean, NotFoundException>> {
    const found = await this.userRepo.findOneById(command.userId);
    if (found.isNone()) return Err(new NotFoundException());
    const user = found.unwrap();
    user.delete();
    const result = await this.userRepo.delete(user);
    return Ok(result);
  }
}
```

## File: `src/modules/user/database/user.repository.port.ts`
```typescript
import { PaginatedQueryParams, RepositoryPort } from '@libs/ddd';
import { UserEntity } from '../domain/user.entity';

export interface FindUsersParams extends PaginatedQueryParams {
  readonly country?: string;
  readonly postalCode?: string;
  readonly street?: string;
}

export interface UserRepositoryPort extends RepositoryPort<UserEntity> {
  findOneByEmail(email: string): Promise<UserEntity | null>;
}
```

## File: `src/modules/user/database/user.repository.ts`
```typescript
import { InjectPool } from 'nestjs-slonik';
import { DatabasePool, sql } from 'slonik';
import { UserRepositoryPort } from './user.repository.port';
import { z } from 'zod';
import { UserMapper } from '../user.mapper';
import { UserRoles } from '../domain/user.types';
import { UserEntity } from '../domain/user.entity';
import { SqlRepositoryBase } from '@src/libs/db/sql-repository.base';
import { Injectable, Logger } from '@nestjs/common';
import { EventEmitter2 } from '@nestjs/event-emitter';

/**
 * Runtime validation of user object for extra safety (in case database schema changes).
 * https://github.com/gajus/slonik#runtime-validation
 * If you prefer to avoid performance penalty of validation, use interfaces instead.
 */
export const userSchema = z.object({
  id: z.string().uuid(),
  createdAt: z.preprocess((val: any) => new Date(val), z.date()),
  updatedAt: z.preprocess((val: any) => new Date(val), z.date()),
  email: z.string().email(),
  country: z.string().min(1).max(255),
  postalCode: z.string().min(1).max(20),
  street: z.string().min(1).max(255),
  role: z.nativeEnum(UserRoles),
});

export type UserModel = z.TypeOf<typeof userSchema>;

/**
 *  Repository is used for retrieving/saving domain entities
 * */
@Injectable()
export class UserRepository
  extends SqlRepositoryBase<UserEntity, UserModel>
  implements UserRepositoryPort
{
  protected tableName = 'users';

  protected schema = userSchema;

  constructor(
    @InjectPool()
    pool: DatabasePool,
    mapper: UserMapper,
    eventEmitter: EventEmitter2,
  ) {
    super(pool, mapper, eventEmitter, new Logger(UserRepository.name));
  }

  async updateAddress(user: UserEntity): Promise<void> {
    const address = user.getProps().address;
    const statement = sql.type(userSchema)`
    UPDATE "users" SET
    street = ${address.street}, country = ${address.country}, "postalCode" = ${address.postalCode}
    WHERE id = ${user.id}`;

    await this.writeQuery(statement, user);
  }

  async findOneByEmail(email: string): Promise<UserEntity> {
    const user = await this.pool.one(
      sql.type(userSchema)`SELECT * FROM "users" WHERE email = ${email}`,
    );

    return this.mapper.toDomain(user);
  }
}
```

## File: `src/modules/user/domain/user.entity.ts`
```typescript
import { AggregateRoot, AggregateID } from '@libs/ddd';
import { UserCreatedDomainEvent } from './events/user-created.domain-event';
import { Address, AddressProps } from './value-objects/address.value-object';
import {
  CreateUserProps,
  UpdateUserAddressProps,
  UserProps,
  UserRoles,
} from './user.types';
import { UserDeletedDomainEvent } from './events/user-deleted.domain-event';
import { UserRoleChangedDomainEvent } from './events/user-role-changed.domain-event';
import { UserAddressUpdatedDomainEvent } from './events/user-address-updated.domain-event';
import { randomUUID } from 'crypto';

export class UserEntity extends AggregateRoot<UserProps> {
  protected readonly _id: AggregateID;

  static create(create: CreateUserProps): UserEntity {
    const id = randomUUID();
    /* Setting a default role since we are not accepting it during creation. */
    const props: UserProps = { ...create, role: UserRoles.guest };
    const user = new UserEntity({ id, props });
    /* adding "UserCreated" Domain Event that will be published
    eventually so an event handler somewhere may receive it and do an
    appropriate action. Multiple events can be added if needed. */
    user.addEvent(
      new UserCreatedDomainEvent({
        aggregateId: id,
        email: props.email,
        ...props.address.unpack(),
      }),
    );
    return user;
  }

  /* You can create getters only for the properties that you need to
  access and leave the rest of the properties private to keep entity
  encapsulated. To get all entity properties (for saving it to a
  database or mapping a response) use .getProps() method
  defined in a EntityBase parent class */
  get role(): UserRoles {
    return this.props.role;
  }

  private changeRole(newRole: UserRoles): void {
    this.addEvent(
      new UserRoleChangedDomainEvent({
        aggregateId: this.id,
        oldRole: this.props.role,
        newRole,
      }),
    );

    this.props.role = newRole;
  }

  makeAdmin(): void {
    this.changeRole(UserRoles.admin);
  }

  makeModerator(): void {
    this.changeRole(UserRoles.moderator);
  }

  delete(): void {
    this.addEvent(
      new UserDeletedDomainEvent({
        aggregateId: this.id,
      }),
    );
  }

  /* Update method only changes properties that we allow, in this
   case only address. This prevents from illegal actions, 
   for example setting email from outside by doing something
   like user.email = otherEmail */
  updateAddress(props: UpdateUserAddressProps): void {
    const newAddress = new Address({
      ...this.props.address,
      ...props,
    } as AddressProps);

    this.props.address = newAddress;

    this.addEvent(
      new UserAddressUpdatedDomainEvent({
        aggregateId: this.id,
        country: newAddress.country,
        street: newAddress.street,
        postalCode: newAddress.postalCode,
      }),
    );
  }

  validate(): void {
    // entity business rules validation to protect it's invariant before saving entity to a database
  }
}
```

## File: `src/modules/user/domain/user.errors.ts`
```typescript
import { ExceptionBase } from '@libs/exceptions';

export class UserAlreadyExistsError extends ExceptionBase {
  static readonly message = 'User already exists';

  public readonly code = 'USER.ALREADY_EXISTS';

  constructor(cause?: Error, metadata?: unknown) {
    super(UserAlreadyExistsError.message, cause, metadata);
  }
}
```

## File: `src/modules/user/domain/user.types.ts`
```typescript
import { Address } from './value-objects/address.value-object';

// All properties that a User has
export interface UserProps {
  role: UserRoles;
  email: string;
  address: Address;
}

// Properties that are needed for a user creation
export interface CreateUserProps {
  email: string;
  address: Address;
}

// Properties used for updating a user address
export interface UpdateUserAddressProps {
  country?: string;
  postalCode?: string;
  street?: string;
}

export enum UserRoles {
  admin = 'admin',
  moderator = 'moderator',
  guest = 'guest',
}
```

## File: `src/modules/user/domain/events/user-address-updated.domain-event.ts`
```typescript
import { DomainEvent, DomainEventProps } from '@libs/ddd';

export class UserAddressUpdatedDomainEvent extends DomainEvent {
  public readonly country: string;

  public readonly street: string;

  public readonly postalCode: string;

  constructor(props: DomainEventProps<UserAddressUpdatedDomainEvent>) {
    super(props);
    this.country = props.country;
    this.postalCode = props.postalCode;
    this.street = props.street;
  }
}
```

## File: `src/modules/user/domain/events/user-created.domain-event.ts`
```typescript
import { DomainEvent, DomainEventProps } from '@libs/ddd';

export class UserCreatedDomainEvent extends DomainEvent {
  readonly email: string;

  readonly country: string;

  readonly postalCode: string;

  readonly street: string;

  constructor(props: DomainEventProps<UserCreatedDomainEvent>) {
    super(props);
    this.email = props.email;
    this.country = props.country;
    this.postalCode = props.postalCode;
    this.street = props.street;
  }
}
```

## File: `src/modules/user/domain/events/user-deleted.domain-event.ts`
```typescript
import { DomainEvent, DomainEventProps } from '@libs/ddd';

export class UserDeletedDomainEvent extends DomainEvent {
  constructor(props: DomainEventProps<UserDeletedDomainEvent>) {
    super(props);
  }
}
```

## File: `src/modules/user/domain/events/user-role-changed.domain-event.ts`
```typescript
import { DomainEvent, DomainEventProps } from '@libs/ddd';
import { UserRoles } from '../user.types';

export class UserRoleChangedDomainEvent extends DomainEvent {
  readonly oldRole: UserRoles;

  readonly newRole: UserRoles;

  constructor(props: DomainEventProps<UserRoleChangedDomainEvent>) {
    super(props);
    this.oldRole = props.oldRole;
    this.newRole = props.newRole;
  }
}
```

## File: `src/modules/user/domain/value-objects/address.value-object.ts`
```typescript
import { ValueObject } from '@libs/ddd';
import { Guard } from '@libs/guard';
import { ArgumentOutOfRangeException } from '@libs/exceptions';

/** Note:
 * Value Objects with multiple properties can contain
 * other Value Objects inside if needed.
 * */

export interface AddressProps {
  country: string;
  postalCode: string;
  street: string;
}

export class Address extends ValueObject<AddressProps> {
  get country(): string {
    return this.props.country;
  }

  get postalCode(): string {
    return this.props.postalCode;
  }

  get street(): string {
    return this.props.street;
  }

  /**
   * Note: This is a very simplified example of validation,
   * real world projects will have stricter rules.
   * You can avoid this type of validation here and validate
   * only on the edge of the application (in controllers when receiving
   * a request) sacrificing some security for performance and convenience.
   */
  protected validate(props: AddressProps): void {
    if (!Guard.lengthIsBetween(props.country, 2, 50)) {
      throw new ArgumentOutOfRangeException('country is out of range');
    }
    if (!Guard.lengthIsBetween(props.street, 2, 50)) {
      throw new ArgumentOutOfRangeException('street is out of range');
    }
    if (!Guard.lengthIsBetween(props.postalCode, 2, 10)) {
      throw new ArgumentOutOfRangeException('postalCode is out of range');
    }
  }
}
```

## File: `src/modules/user/dtos/user.paginated.response.dto.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';
import { PaginatedResponseDto } from '@src/libs/api/paginated.response.base';
import { UserResponseDto } from './user.response.dto';

export class UserPaginatedResponseDto extends PaginatedResponseDto<UserResponseDto> {
  @ApiProperty({ type: UserResponseDto, isArray: true })
  readonly data: readonly UserResponseDto[];
}
```

## File: `src/modules/user/dtos/user.response.dto.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';
import { ResponseBase } from '@libs/api/response.base';

export class UserResponseDto extends ResponseBase {
  @ApiProperty({
    example: 'joh-doe@gmail.com',
    description: "User's email address",
  })
  email: string;

  @ApiProperty({
    example: 'France',
    description: "User's country of residence",
  })
  country: string;

  @ApiProperty({
    example: '123456',
    description: 'Postal code',
  })
  postalCode: string;

  @ApiProperty({
    example: 'Park Avenue',
    description: 'Street where the user is registered',
  })
  street: string;
}
```

## File: `src/modules/user/dtos/graphql/user.graphql-response.dto.ts`
```typescript
import { ResponseBase } from '@libs/api/response.base';
import { Field, ObjectType } from '@nestjs/graphql';

@ObjectType()
export class UserGraphqlResponseDto extends ResponseBase {
  @Field({
    description: "User's identifier",
  })
  id: string;

  @Field({
    description: "User's email address",
  })
  email: string;

  @Field({
    description: "User's country of residence",
  })
  country: string;

  @Field({
    description: 'Postal code',
  })
  postalCode: string;

  @Field({
    description: 'Street where the user is registered',
  })
  street: string;
}
```

## File: `src/modules/user/dtos/graphql/user.paginated-gql-response.dto.ts`
```typescript
import { Field, ObjectType } from '@nestjs/graphql';
import { PaginatedGraphqlResponse } from '../../../../libs/api/graphql/paginated.graphql-response.base';

import { UserGraphqlResponseDto } from './user.graphql-response.dto';

@ObjectType()
export class UserPaginatedGraphqlResponseDto extends PaginatedGraphqlResponse(
  UserGraphqlResponseDto,
) {
  @Field(() => [UserGraphqlResponseDto])
  data: UserGraphqlResponseDto[];
}
```

## File: `src/modules/user/queries/find-users/find-users.graphql-resolver.ts`
```typescript
import { QueryBus } from '@nestjs/cqrs';
import { Args, Query, Resolver } from '@nestjs/graphql';
import { Result } from 'oxide.ts';
import { ResponseBase } from '../../../../libs/api/response.base';
import { Paginated } from '../../../../libs/ddd';
import { PaginatedParams } from '../../../../libs/ddd/query.base';
import { UserModel } from '../../database/user.repository';
import { UserPaginatedGraphqlResponseDto } from '../../dtos/graphql/user.paginated-gql-response.dto';
import { FindUsersQuery } from './find-users.query-handler';

@Resolver()
export class FindUsersGraphqlResolver {
  constructor(private readonly queryBus: QueryBus) {}
  @Query(() => UserPaginatedGraphqlResponseDto)
  async findUsers(
    @Args('options', { type: () => String })
    options: PaginatedParams<FindUsersQuery>,
  ): Promise<UserPaginatedGraphqlResponseDto> {
    const query = new FindUsersQuery(options);
    const result: Result<
      Paginated<UserModel>,
      Error
    > = await this.queryBus.execute(query);

    const paginated = result.unwrap();
    const response = new UserPaginatedGraphqlResponseDto({
      ...paginated,
      data: paginated.data.map((user) => ({
        ...new ResponseBase(user),
        email: user.email,
        country: user.country,
        street: user.street,
        postalCode: user.postalCode,
      })),
    });
    return response;
  }
}
```

## File: `src/modules/user/queries/find-users/find-users.http.controller.ts`
```typescript
import { Body, Controller, Get, HttpStatus, Query } from '@nestjs/common';
import { routesV1 } from '@config/app.routes';
import { QueryBus } from '@nestjs/cqrs';
import { ApiOperation, ApiResponse } from '@nestjs/swagger';
import { Result } from 'oxide.ts';
import { FindUsersRequestDto } from './find-users.request.dto';
import { FindUsersQuery } from './find-users.query-handler';
import { Paginated } from '@src/libs/ddd';
import { UserPaginatedResponseDto } from '../../dtos/user.paginated.response.dto';
import { PaginatedQueryRequestDto } from '@src/libs/api/paginated-query.request.dto';
import { UserModel } from '../../database/user.repository';
import { ResponseBase } from '@src/libs/api/response.base';

@Controller(routesV1.version)
export class FindUsersHttpController {
  constructor(private readonly queryBus: QueryBus) {}

  @Get(routesV1.user.root)
  @ApiOperation({ summary: 'Find users' })
  @ApiResponse({
    status: HttpStatus.OK,
    type: UserPaginatedResponseDto,
  })
  async findUsers(
    @Body() request: FindUsersRequestDto,
    @Query() queryParams: PaginatedQueryRequestDto,
  ): Promise<UserPaginatedResponseDto> {
    const query = new FindUsersQuery({
      ...request,
      limit: queryParams?.limit,
      page: queryParams?.page,
    });
    const result: Result<
      Paginated<UserModel>,
      Error
    > = await this.queryBus.execute(query);

    const paginated = result.unwrap();

    // Whitelisting returned properties
    return new UserPaginatedResponseDto({
      ...paginated,
      data: paginated.data.map((user) => ({
        ...new ResponseBase(user),
        email: user.email,
        country: user.country,
        street: user.street,
        postalCode: user.postalCode,
      })),
    });
  }
}
```

## File: `src/modules/user/queries/find-users/find-users.query-handler.ts`
```typescript
import { IQueryHandler, QueryHandler } from '@nestjs/cqrs';
import { Ok, Result } from 'oxide.ts';
import { PaginatedParams, PaginatedQueryBase } from '@libs/ddd/query.base';
import { Paginated } from '@src/libs/ddd';
import { InjectPool } from 'nestjs-slonik';
import { DatabasePool, sql } from 'slonik';
import { UserModel, userSchema } from '../../database/user.repository';

export class FindUsersQuery extends PaginatedQueryBase {
  readonly country?: string;

  readonly postalCode?: string;

  readonly street?: string;

  constructor(props: PaginatedParams<FindUsersQuery>) {
    super(props);
    this.country = props.country;
    this.postalCode = props.postalCode;
    this.street = props.street;
  }
}

@QueryHandler(FindUsersQuery)
export class FindUsersQueryHandler implements IQueryHandler {
  constructor(
    @InjectPool()
    private readonly pool: DatabasePool,
  ) {}

  /**
   * In read model we don't need to execute
   * any business logic, so we can bypass
   * domain and repository layers completely
   * and execute query directly
   */
  async execute(
    query: FindUsersQuery,
  ): Promise<Result<Paginated<UserModel>, Error>> {
    /**
     * Constructing a query with Slonik.
     * More info: https://contra.com/p/AqZWWoUB-writing-composable-sql-using-java-script
     */
    const statement = sql.type(userSchema)`
         SELECT *
         FROM users
         WHERE
           ${query.country ? sql`country = ${query.country}` : true} AND
           ${query.street ? sql`street = ${query.street}` : true} AND
           ${query.postalCode ? sql`"postalCode" = ${query.postalCode}` : true}
         LIMIT ${query.limit}
         OFFSET ${query.offset}`;

    const records = await this.pool.query(statement);

    return Ok(
      new Paginated({
        data: records.rows,
        count: records.rowCount,
        limit: query.limit,
        page: query.page,
      }),
    );
  }
}
```

## File: `src/modules/user/queries/find-users/find-users.request.dto.ts`
```typescript
import { ApiProperty } from '@nestjs/swagger';
import {
  MaxLength,
  IsString,
  IsAlphanumeric,
  Matches,
  IsOptional,
} from 'class-validator';

export class FindUsersRequestDto {
  @ApiProperty({ example: 'France', description: 'Country of residence' })
  @IsOptional()
  @MaxLength(50)
  @IsString()
  @Matches(/^[a-zA-Z ]*$/)
  readonly country?: string;

  @ApiProperty({ example: '28566', description: 'Postal code' })
  @IsOptional()
  @MaxLength(10)
  @IsAlphanumeric()
  readonly postalCode?: string;

  @ApiProperty({ example: 'Grande Rue', description: 'Street' })
  @IsOptional()
  @MaxLength(50)
  @Matches(/^[a-zA-Z ]*$/)
  readonly street?: string;
}
```

## File: `src/modules/wallet/wallet.di-tokens.ts`
```typescript
export const WALLET_REPOSITORY = Symbol('WALLET_REPOSITORY');
```

## File: `src/modules/wallet/wallet.mapper.ts`
```typescript
import { Mapper } from '@libs/ddd';
import { Injectable } from '@nestjs/common';
import { WalletEntity } from './domain/wallet.entity';
import { WalletModel, walletSchema } from './database/wallet.repository';

@Injectable()
export class WalletMapper implements Mapper<WalletEntity, WalletModel> {
  toPersistence(entity: WalletEntity): WalletModel {
    const copy = entity.getProps();
    const record: WalletModel = {
      id: copy.id,
      createdAt: copy.createdAt,
      updatedAt: copy.updatedAt,
      userId: copy.userId,
      balance: copy.balance,
    };
    return walletSchema.parse(record);
  }

  toDomain(record: WalletModel): WalletEntity {
    const entity = new WalletEntity({
      id: record.id,
      createdAt: record.createdAt,
      updatedAt: record.updatedAt,
      props: {
        userId: record.userId,
        balance: record.balance,
      },
    });
    return entity;
  }

  toResponse(): any {
    throw new Error('Not implemented');
  }
}
```

## File: `src/modules/wallet/wallet.module.ts`
```typescript
import { Logger, Module, Provider } from '@nestjs/common';
import { CreateWalletWhenUserIsCreatedDomainEventHandler } from './application/event-handlers/create-wallet-when-user-is-created.domain-event-handler';
import { WalletRepository } from './database/wallet.repository';
import { WALLET_REPOSITORY } from './wallet.di-tokens';
import { WalletMapper } from './wallet.mapper';

const eventHandlers: Provider[] = [
  CreateWalletWhenUserIsCreatedDomainEventHandler,
];

const mappers: Provider[] = [WalletMapper];

const repositories: Provider[] = [
  { provide: WALLET_REPOSITORY, useClass: WalletRepository },
];

@Module({
  imports: [],
  controllers: [],
  providers: [Logger, ...eventHandlers, ...mappers, ...repositories],
})
export class WalletModule {}
```

## File: `src/modules/wallet/application/event-handlers/create-wallet-when-user-is-created.domain-event-handler.ts`
```typescript
import { UserCreatedDomainEvent } from '@modules/user/domain/events/user-created.domain-event';
import { WalletRepositoryPort } from '@modules/wallet/database/wallet.repository.port';
import { WalletEntity } from '../../domain/wallet.entity';
import { OnEvent } from '@nestjs/event-emitter';
import { Inject, Injectable } from '@nestjs/common';
import { WALLET_REPOSITORY } from '../../wallet.di-tokens';

@Injectable()
export class CreateWalletWhenUserIsCreatedDomainEventHandler {
  constructor(
    @Inject(WALLET_REPOSITORY)
    private readonly walletRepo: WalletRepositoryPort,
  ) {}

  // Handle a Domain Event by performing changes to other aggregates (inside the same Domain).
  @OnEvent(UserCreatedDomainEvent.name, { async: true, promisify: true })
  async handle(event: UserCreatedDomainEvent): Promise<any> {
    const wallet = WalletEntity.create({
      userId: event.aggregateId,
    });
    return this.walletRepo.insert(wallet);
  }
}
```

## File: `src/modules/wallet/database/wallet.repository.port.ts`
```typescript
import { RepositoryPort } from '@libs/ddd';
import { WalletEntity } from '../domain/wallet.entity';

export type WalletRepositoryPort = RepositoryPort<WalletEntity>;
```

## File: `src/modules/wallet/database/wallet.repository.ts`
```typescript
import { InjectPool } from 'nestjs-slonik';
import { DatabasePool } from 'slonik';
import { z } from 'zod';
import { SqlRepositoryBase } from '@src/libs/db/sql-repository.base';
import { WalletRepositoryPort } from './wallet.repository.port';
import { WalletEntity } from '../domain/wallet.entity';
import { WalletMapper } from '../wallet.mapper';
import { Injectable, Logger } from '@nestjs/common';
import { EventEmitter2 } from '@nestjs/event-emitter';

export const walletSchema = z.object({
  id: z.string().min(1).max(255),
  createdAt: z.preprocess((val: any) => new Date(val), z.date()),
  updatedAt: z.preprocess((val: any) => new Date(val), z.date()),
  balance: z.number().min(0).max(9999999),
  userId: z.string().min(1).max(255),
});

export type WalletModel = z.TypeOf<typeof walletSchema>;

@Injectable()
export class WalletRepository
  extends SqlRepositoryBase<WalletEntity, WalletModel>
  implements WalletRepositoryPort
{
  protected tableName = 'wallets';

  protected schema = walletSchema;

  constructor(
    @InjectPool()
    pool: DatabasePool,
    mapper: WalletMapper,
    eventEmitter: EventEmitter2,
  ) {
    super(pool, mapper, eventEmitter, new Logger(WalletRepository.name));
  }
}
```

## File: `src/modules/wallet/domain/wallet.entity.ts`
```typescript
import { AggregateID, AggregateRoot } from '@libs/ddd';
import { ArgumentOutOfRangeException } from '@libs/exceptions';
import { Err, Ok, Result } from 'oxide.ts';
import { WalletCreatedDomainEvent } from './events/wallet-created.domain-event';
import { WalletNotEnoughBalanceError } from './wallet.errors';
import { randomUUID } from 'crypto';

export interface CreateWalletProps {
  userId: AggregateID;
}

export interface WalletProps extends CreateWalletProps {
  balance: number;
}

export class WalletEntity extends AggregateRoot<WalletProps> {
  protected readonly _id: AggregateID;

  static create(create: CreateWalletProps): WalletEntity {
    const id = randomUUID();
    const props: WalletProps = { ...create, balance: 0 };
    const wallet = new WalletEntity({ id, props });

    wallet.addEvent(
      new WalletCreatedDomainEvent({ aggregateId: id, userId: create.userId }),
    );

    return wallet;
  }

  deposit(amount: number): void {
    this.props.balance += amount;
  }

  withdraw(amount: number): Result<null, WalletNotEnoughBalanceError> {
    if (this.props.balance - amount < 0) {
      return Err(new WalletNotEnoughBalanceError());
    }
    this.props.balance -= amount;
    return Ok(null);
  }

  /**
   * Protects wallet invariant.
   * This method is executed by a repository
   * before saving entity in a database.
   */
  public validate(): void {
    if (this.props.balance < 0) {
      throw new ArgumentOutOfRangeException(
        'Wallet balance cannot be less than 0',
      );
    }
  }
}
```

## File: `src/modules/wallet/domain/wallet.errors.ts`
```typescript
import { ExceptionBase } from '@libs/exceptions';

export class WalletNotEnoughBalanceError extends ExceptionBase {
  static readonly message = 'Wallet has not enough balance';

  public readonly code = 'WALLET.NOT_ENOUGH_BALANCE';

  constructor(metadata?: unknown) {
    super(WalletNotEnoughBalanceError.message, undefined, metadata);
  }
}
```

## File: `src/modules/wallet/domain/events/wallet-created.domain-event.ts`
```typescript
import { DomainEvent, DomainEventProps } from '@libs/ddd';

export class WalletCreatedDomainEvent extends DomainEvent {
  readonly userId: string;

  constructor(props: DomainEventProps<WalletCreatedDomainEvent>) {
    super(props);
  }
}
```

## File: `tests/setup/jestGlobalSetup.ts`
```typescript
import { databaseConfig } from '../../src/configs/database.config';

module.exports = async (): Promise<void> => {
  if (!databaseConfig.database.includes('test')) {
    throw new Error(
      `Current database name is: ${databaseConfig.database}. Make sure database includes a word "test" as prefix or suffix, for example: "test_db" or "db_test" to avoid writing into a main database.`,
    );
  }
};
```

## File: `tests/setup/jestSetupAfterEnv.ts`
```typescript
import { Test, TestingModuleBuilder, TestingModule } from '@nestjs/testing';
import { AppModule } from '@src/app.module';
import { NestExpressApplication } from '@nestjs/platform-express';
import { createPool, DatabasePool } from 'slonik';
import * as request from 'supertest';
import { postgresConnectionUri } from '@src/configs/database.config';
import { ValidationPipe } from '@nestjs/common';

// Setting up test server and utilities

export class TestServer {
  constructor(
    public readonly serverApplication: NestExpressApplication,
    public readonly testingModule: TestingModule,
  ) {}

  public static async new(
    testingModuleBuilder: TestingModuleBuilder,
  ): Promise<TestServer> {
    const testingModule: TestingModule = await testingModuleBuilder.compile();

    const app: NestExpressApplication = testingModule.createNestApplication();

    app.useGlobalPipes(
      new ValidationPipe({ transform: true, whitelist: true }),
    );

    app.enableShutdownHooks();

    await app.init();

    return new TestServer(app, testingModule);
  }
}

let testServer: TestServer;
let pool: DatabasePool;

export async function generateTestingApplication(): Promise<{
  testServer: TestServer;
}> {
  const testServer = await TestServer.new(
    Test.createTestingModule({
      imports: [AppModule],
    }),
  );

  return {
    testServer,
  };
}

export function getTestServer(): TestServer {
  return testServer;
}

export function getConnectionPool(): DatabasePool {
  return pool;
}

export function getHttpServer(): request.SuperTest<request.Test> {
  const testServer = getTestServer();
  const httpServer = request(testServer.serverApplication.getHttpServer());

  return httpServer;
}

// setup
beforeAll(async (): Promise<void> => {
  ({ testServer } = await generateTestingApplication());
  pool = await createPool(postgresConnectionUri);
});

// cleanup
afterAll(async (): Promise<void> => {
  await pool.end();
  testServer.serverApplication.close();
});
```

## File: `tests/shared/shared-steps.ts`
```typescript
import { ApiErrorResponse } from '@src/libs/api/api-error.response';
import { TestContext } from '@tests/test-utils/TestContext';
import { CreateUserTestContext } from '@tests/user/user-shared-steps';
import { DefineStepFunction } from 'jest-cucumber';

/**
 * Test steps that can be shared between all tests
 */

export const iReceiveAnErrorWithStatusCode = (
  then: DefineStepFunction,
  ctx: TestContext<CreateUserTestContext>,
): void => {
  then(
    /^I receive an error "(.*)" with status code (\d+)$/,
    async (errorMessage: string, statusCode: string) => {
      const apiError = ctx.latestResponse as ApiErrorResponse;
      expect(apiError.statusCode).toBe(parseInt(statusCode));
      expect(apiError.error).toBe(errorMessage);
    },
  );
};
```

## File: `tests/test-utils/ApiClient.ts`
```typescript
import { routesV1 } from '@src/configs/app.routes';
import { IdResponse } from '@src/libs/api/id.response.dto';
import { CreateUserRequestDto } from '@src/modules/user/commands/create-user/create-user.request.dto';
import { UserPaginatedResponseDto } from '@src/modules/user/dtos/user.paginated.response.dto';
import { getHttpServer } from '@tests/setup/jestSetupAfterEnv';

export class ApiClient {
  private url = `/${routesV1.version}/${routesV1.user.root}`;

  async createUser(dto: CreateUserRequestDto): Promise<IdResponse> {
    const response = await getHttpServer().post(this.url).send(dto);
    return response.body;
  }

  async deleteUser(id: string): Promise<void> {
    const response = await getHttpServer().delete(`${this.url}/${id}`);
    return response.body;
  }

  async findAllUsers(): Promise<UserPaginatedResponseDto> {
    const response = await getHttpServer().get(this.url);
    return response.body;
  }
}
```

## File: `tests/test-utils/snapshot-base-props.ts`
```typescript
export const snapshotBaseProps = {
  id: expect.any(String),
  createdAt: expect.any(String),
  updatedAt: expect.any(String),
};
```

## File: `tests/test-utils/TestContext.ts`
```typescript
/**
 * Used for setting a context data in cucumber tests
 */
export class TestContext<Context> {
  context: Context; // test specific context
  latestResponse: unknown; // get a latest response
  latestRequestDto: unknown; // set a request dto to send

  constructor() {
    this.context = {} as any;
  }
}
```

## File: `tests/test-utils/mocks/generic-model-props.mock.ts`
```typescript
export const dateMock = new Date('2020-08-07T12:29:11.214Z');

export const createdAtUpdatedAtMock = {
  createdAt: dateMock,
  updatedAt: dateMock,
};
```

## File: `tests/user/user-shared-steps.ts`
```typescript
import { Mutable } from '@src/libs/types';
import { CreateUserRequestDto } from '@src/modules/user/commands/create-user/create-user.request.dto';
import { DefineStepFunction } from 'jest-cucumber';
import { TestContext } from 'tests/test-utils/TestContext';
import { ApiClient } from '@tests/test-utils/ApiClient';

/**
 * Test steps that are shared between multiple user tests
 */

export type CreateUserTestContext = {
  createUserDto: Mutable<CreateUserRequestDto>;
};

export const givenUserProfileData = (
  given: DefineStepFunction,
  ctx: TestContext<CreateUserTestContext>,
): void => {
  given(/^user profile data$/, (table: CreateUserRequestDto[]) => {
    ctx.context.createUserDto = table[0];
  });
};

export const iSendARequestToCreateAUser = (
  when: DefineStepFunction,
  ctx: TestContext<CreateUserTestContext>,
): void => {
  when('I send a request to create a user', async () => {
    const response = await new ApiClient().createUser(
      ctx.context.createUserDto,
    );
    ctx.latestResponse = response;
  });
};
```

## File: `tests/user/create-user/create-user.artillery.yaml`
```yaml
# Load testing with Artillery.
# Can also be good for seeding database with lots of dummy data.
# https://github.com/Sairyss/backend-best-practices#load-testing
# https://www.npmjs.com/package/artillery
# https://www.npmjs.com/package/artillery-plugin-faker
config:
  target: http://localhost:3000/v1
  phases:
    - duration: 2
      arrivalRate: 150
  plugins:
    faker:
      locale: en
  variables:
    email: '$faker.internet.email'
    country: '$faker.address.country'
    street: '$faker.address.streetName'
scenarios:
  - flow:
      - post:
          url: '/users'
          json:
            email: '{{ email }}'
            country: '{{ country }}'
            postalCode: '12345'
            street: '{{ street }}'
```

## File: `tests/user/create-user/create-user.e2e-spec.ts`
```typescript
import { defineFeature, loadFeature } from 'jest-cucumber';
import { getConnectionPool } from '../../setup/jestSetupAfterEnv';
import { UserResponseDto } from '@modules/user/dtos/user.response.dto';
import { DatabasePool, sql } from 'slonik';
import { TestContext } from '@tests/test-utils/TestContext';
import { IdResponse } from '@src/libs/api/id.response.dto';
import {
  CreateUserTestContext,
  givenUserProfileData,
  iSendARequestToCreateAUser,
} from '../user-shared-steps';
import { ApiClient } from '@tests/test-utils/ApiClient';
import { iReceiveAnErrorWithStatusCode } from '@tests/shared/shared-steps';

const feature = loadFeature('tests/user/create-user/create-user.feature');

/**
 * e2e test implementing a Gherkin feature file
 * https://github.com/Sairyss/backend-best-practices#testing
 */

defineFeature(feature, (test) => {
  let pool: DatabasePool;
  const apiClient = new ApiClient();

  beforeAll(() => {
    pool = getConnectionPool();
  });

  afterEach(async () => {
    await pool.query(sql`TRUNCATE "users"`);
    await pool.query(sql`TRUNCATE "wallets"`);
  });

  test('I can create a user', ({ given, when, then, and }) => {
    const ctx = new TestContext<CreateUserTestContext>();

    givenUserProfileData(given, ctx);

    iSendARequestToCreateAUser(when, ctx);

    then('I receive my user ID', () => {
      const response = ctx.latestResponse as IdResponse;
      expect(typeof response.id).toBe('string');
    });

    and('I can see my user in a list of all users', async () => {
      const res = await apiClient.findAllUsers();
      const response = ctx.latestResponse as IdResponse;

      expect(
        res.data.some((item: UserResponseDto) => item.id === response.id),
      ).toBe(true);
    });
  });

  test('I try to create a user with invalid data', ({ given, when, then }) => {
    const ctx = new TestContext<CreateUserTestContext>();

    givenUserProfileData(given, ctx);

    iSendARequestToCreateAUser(when, ctx);

    iReceiveAnErrorWithStatusCode(then, ctx);
  });
});
```

## File: `tests/user/create-user/create-user.feature`
```
# This is a Gherkin feature file https://cucumber.io/brain/knowledge/docs_legacy/gherkin/reference/

Feature: Create a user

    Scenario: I can create a user
        Given user profile data
            | email              | country | street      | postalCode |
            | john.doe@gmail.com | England | Road Avenue | 29145      |
        When I send a request to create a user
        Then I receive my user ID
        And I can see my user in a list of all users

    Scenario Outline: I try to create a user with invalid data
        Given user profile data
            | email   | country   | street   | postalCode   |
            | <Email> | <Country> | <Street> | <PostalCode> |
        When I send a request to create a user
        Then I receive an error "Bad Request" with status code 400

        Examples:
            | Email          | Country | Street      | PostalCode |
            | johngmail.com  | England | Road Avenue | 29145      |
            | john@gmail.com | 123     | Road Avenue | 29145      |
            | johng@mail.com | England | 123         | 29145      |
            | johng@mail.com | England | Road Avenue | @          |
            | #@!$           | $#@1    | %542        | !321       |
```

## File: `tests/user/delete-user/delete-user.e2e-spec.ts`
```typescript
import { UserResponseDto } from '@modules/user/dtos/user.response.dto';
import { IdResponse } from '@src/libs/api/id.response.dto';
import { defineFeature, loadFeature } from 'jest-cucumber';
import { DatabasePool, sql } from 'slonik';
import { TestContext } from '@tests/test-utils/TestContext';
import { getConnectionPool } from '../../setup/jestSetupAfterEnv';
import {
  CreateUserTestContext,
  givenUserProfileData,
  iSendARequestToCreateAUser,
} from '../user-shared-steps';
import { ApiClient } from '@tests/test-utils/ApiClient';

const feature = loadFeature('tests/user/delete-user/delete-user.feature');

defineFeature(feature, (test) => {
  let pool: DatabasePool;
  const apiClient = new ApiClient();

  beforeAll(() => {
    pool = getConnectionPool();
  });

  afterEach(async () => {
    await pool.query(sql`TRUNCATE "users"`);
    await pool.query(sql`TRUNCATE "wallets"`);
  });

  test('I can delete a user', ({ given, when, then, and }) => {
    const ctx = new TestContext<CreateUserTestContext>();

    givenUserProfileData(given, ctx);

    iSendARequestToCreateAUser(when, ctx);

    then('I send a request to delete my user', async () => {
      const response = ctx.latestResponse as IdResponse;
      await apiClient.deleteUser(response.id);
    });

    and('I cannot see my user in a list of all users', async () => {
      const res = await apiClient.findAllUsers();
      const response = ctx.latestResponse as IdResponse;
      expect(
        res.data.some((item: UserResponseDto) => item.id === response.id),
      ).toBe(false);
    });
  });
});
```

## File: `tests/user/delete-user/delete-user.feature`
```
Feature: Delete a user

    Background: Existing user
        Given user profile data
            | email              | country | street      | postalCode |
            | john.doe@gmail.com | England | Road Avenue | 29145      |
        When I send a request to create a user

    Scenario: I can delete a user
        Given I send a request to delete my user
        Then I cannot see my user in a list of all users
```

