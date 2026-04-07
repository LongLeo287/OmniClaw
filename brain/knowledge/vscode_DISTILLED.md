---
id: vscode
type: knowledge
owner: OA_Triage
---
# vscode
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "myextension",
  "displayName": "MyExtension",
  "description": "MyExtension",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.46.0"
  },
  "categories": [
    "Other"
  ],
  "activationEvents": [
    "onCommand:myextension.sayhello",
    "onView:myextension-sidebar",
    "onCommand:myextension.askquestion"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "myextension.sayhello",
        "category": "MyExtension",
        "title": "Say hello"
      },
      {
        "command": "myextension.askquestion",
        "category": "MyExtension",
        "title": "Ask question"
      }
    ],
    "viewsContainers": {
      "activitybar": [
        {
          "id": "myextension-sidebar-view",
          "title": "MyExtension",
          "icon": "assets/icon.svg"
        }
      ]
    },
    "views": {
      "myextension-sidebar-view": [
        {
          "type": "webview",
          "id": "myextension-sidebar",
          "name": "MyExtension",
          "icon": "assets/icon.svg",
          "contextualTitle": "MyExtension"
        }
      ]
    }
  },
  "scripts": {
    "install:all": "pnpm install && pnpm --prefix ./webview-ui install ./webview-ui",
    "start:ui": "pnpm --prefix ./webview-ui run start",
    "build:ui": "pnpm --prefix ./webview-ui run build",
    "watch:ui": "pnpm --prefix ./webview-ui run watch",
    "vscode:prepublish": "pnpm run compile",
    "compile": "tsc -p ./",
    "watch:extension": "tsc -watch -p ./",
    "watch:all": "concurrently \"pnpm watch:ui\" \"pnpm watch:extension\"",
    "watch": "pnpm watch:extension",
    "pretest": "pnpm run compile && pnpm run lint",
    "lint": "eslint src --ext ts"
  },
  "devDependencies": {
    "@types/glob": "^7.1.3",
    "@types/node": "^12.11.7",
    "@types/vscode": "^1.46.0",
    "@typescript-eslint/eslint-plugin": "^4.14.1",
    "@typescript-eslint/parser": "^4.14.1",
    "concurrently": "^7.3.0",
    "eslint": "^7.19.0",
    "glob": "^7.1.6",
    "prettier": "^2.2.1",
    "typescript": "^4.1.3",
    "vscode-test": "^1.5.0"
  },
  "dependencies": {
    "ts-import": "4.0.0-beta.6"
  },
  "pnpm": {
    "patchedDependencies": {
      "ts-import@4.0.0-beta.6": "patches/ts-import@4.0.0-beta.6.patch"
    }
  }
}

```

### File: README.md
```md
# Hello World (React + Vite)

This is an implementation of the default [Hello World](https://github.com/microsoft/vscode-webview-ui-toolkit-samples/tree/main/default/hello-world) sample extension that demonstrates how to set up and use a [React](https://reactjs.org/) + [Vite](https://vitejs.dev/) + [Webview UI Toolkit](https://github.com/microsoft/vscode-webview-ui-toolkit) webview sidebar extension.


## Documentation

For a deeper dive into how this sample works, read the guides below.

- [Extension structure](./docs/extension-structure.md)
- [Extension commands](./docs/extension-commands.md)
- [Extension development cycle](./docs/extension-development-cycle.md)

## Run The Sample

```bash
# Copy sample extension locally
git clone https://github.com/anubra266/vscode-sidebar-extension.git hello world

# Navigate into sample directory
cd hello-world

# Install dependencies for both the extension and webview UI source code
pnpm run install:all

# Build extension UI source code in watch mode
pnpm run watch:ui

# Open sample in VS Code
code .
```

Once the sample is open inside VS Code you can run the extension by doing the following:

1. Press `F5` to open a new Extension Development Host window
2. Inside the host window, click the new panda icon

```

### File: src\panels\README.md
```md
# `panels` Directory

This directory contains all of the webview-related code that will be executed within the extension context. It can be thought of as the place where all of the "backend" code of a webview panel is contained.

Types of content that can be contained here:

Individual JavaScript / TypeScript files that contain a class which manages the state and behavior of a given webview panel. Each class is usually in charge of:

- Creating and rendering the webview panel
- Properly cleaning up and disposing of webview resources when the panel is closed
- Setting message listeners so data can be passed between the webview and extension
- Setting the HTML (and by proxy CSS/JavaScript) content of the webview panel
- Other custom logic and behavior related to webview panel management

```

### File: pnpm-lock.yaml
```yaml
lockfileVersion: 5.4

patchedDependencies:
  ts-import@4.0.0-beta.6:
    hash: 37fpwgegil7mmqwviczciykreq
    path: patches/ts-import@4.0.0-beta.6.patch

specifiers:
  '@types/glob': ^7.1.3
  '@types/node': ^12.11.7
  '@types/vscode': ^1.46.0
  '@typescript-eslint/eslint-plugin': ^4.14.1
  '@typescript-eslint/parser': ^4.14.1
  concurrently: ^7.3.0
  eslint: ^7.19.0
  glob: ^7.1.6
  prettier: ^2.2.1
  ts-import: 4.0.0-beta.6
  typescript: ^4.1.3
  vscode-test: ^1.5.0

dependencies:
  ts-import: 4.0.0-beta.6_37fpwgegil7mmqwviczciykreq_typescript@4.7.4

devDependencies:
  '@types/glob': 7.2.0
  '@types/node': 12.20.55
  '@types/vscode': 1.69.0
  '@typescript-eslint/eslint-plugin': 4.33.0_3ekaj7j3owlolnuhj3ykrb7u7i
  '@typescript-eslint/parser': 4.33.0_hxadhbs2xogijvk7vq4t2azzbu
  concurrently: 7.3.0
  eslint: 7.32.0
  glob: 7.2.3
  prettier: 2.7.1
  typescript: 4.7.4
  vscode-test: 1.6.1

packages:

  /@babel/code-frame/7.12.11:
    resolution: {integrity: sha512-Zt1yodBx1UcyiePMSkWnU4hPqhwq7hGi2nFL1LeA3EUl+q2LQx16MISgJ0+z7dnmgvP9QtIleuETGOiOH1RcIw==}
    dependencies:
      '@babel/highlight': 7.18.6
    dev: true

  /@babel/helper-validator-identifier/7.18.6:
    resolution: {integrity: sha512-MmetCkz9ej86nJQV+sFCxoGGrUbU3q02kgLciwkrt9QqEB7cP39oKEY0PakknEO0Gu20SskMRi+AYZ3b1TpN9g==}
    engines: {node: '>=6.9.0'}
    dev: true

  /@babel/highlight/7.18.6:
    resolution: {integrity: sha512-u7stbOuYjaPezCuLj29hNW1v64M2Md2qupEKP1fHc7WdOA3DgLh37suiSrZYY7haUB7iBeQZ9P1uiRF359do3g==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/helper-validator-identifier': 7.18.6
      chalk: 2.4.2
      js-tokens: 4.0.0
    dev: true

  /@eslint/eslintrc/0.4.3:
    resolution: {integrity: sha512-J6KFFz5QCYUJq3pf0mjEcCJVERbzv71PUIDczuh9JkwGEzced6CO5ADLHB1rbf/+oPBtoPfMYNOpGDzCANlbXw==}
    engines: {node: ^10.12.0 || >=12.0.0}
    dependencies:
      ajv: 6.12.6
      debug: 4.3.4
      espree: 7.3.1
      globals: 13.17.0
      ignore: 4.0.6
      import-fresh: 3.3.0
      js-yaml: 3.14.1
      minimatch: 3.1.2
      strip-json-comments: 3.1.1
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@humanwhocodes/config-array/0.5.0:
    resolution: {integrity: sha512-FagtKFz74XrTl7y6HCzQpwDfXP0yhxe9lHLD1UZxjvZIcbyRz8zTFF/yYNfSfzU414eDwZ1SrO0Qvtyf+wFMQg==}
    engines: {node: '>=10.10.0'}
    dependencies:
      '@humanwhocodes/object-schema': 1.2.1
      debug: 4.3.4
      minimatch: 3.1.2
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@humanwhocodes/object-schema/1.2.1:
    resolution: {integrity: sha512-ZnQMnLV4e7hDlUvw8H+U8ASL02SS2Gn6+9Ac3wGGLIe7+je2AeAOxPY+izIPJDfFDb7eDjev0Us8MO1iFRN8hA==}
    dev: true

  /@nodelib/fs.scandir/2.1.5:
    resolution: {integrity: sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==}
    engines: {node: '>= 8'}
    dependencies:
      '@nodelib/fs.stat': 2.0.5
      run-parallel: 1.2.0
    dev: true

  /@nodelib/fs.stat/2.0.5:
    resolution: {integrity: sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==}
    engines: {node: '>= 8'}
    dev: true

  /@nodelib/fs.walk/1.2.8:
    resolution: {integrity: sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==}
    engines: {node: '>= 8'}
    dependencies:
      '@nodelib/fs.scandir': 2.1.5
      fastq: 1.13.0
    dev: true

  /@tootallnate/once/1.1.2:
    resolution: {integrity: sha512-RbzJvlNzmRq5c3O09UipeuXno4tA1FE6ikOjxZK0tuxVv3412l64l5t1W5pj4+rJq9vpkm/kwiR07aZXnsKPxw==}
    engines: {node: '>= 6'}
    dev: true

  /@types/glob/7.2.0:
    resolution: {integrity: sha512-ZUxbzKl0IfJILTS6t7ip5fQQM/J3TJYubDm3nMbgubNNYS62eXeUpoLUC8/7fJNiFYHTrGPQn7hspDUzIHX3UA==}
    dependencies:
      '@types/minimatch': 3.0.5
      '@types/node': 12.20.55
    dev: true

  /@types/json-schema/7.0.11:
    resolution: {integrity: sha512-wOuvG1SN4Us4rez+tylwwwCV1psiNVOkJeM3AUWUNWg/jDQY2+HE/444y5gc+jBmRqASOm2Oeh5c1axHobwRKQ==}
    dev: true

  /@types/minimatch/3.0.5:
    resolution: {integrity: sha512-Klz949h02Gz2uZCMGwDUSDS1YBlTdDDgbWHi+81l29tQALUtvz4rAYi5uoVhE5Lagoq6DeqAUlbrHvW/mXDgdQ==}
    dev: true

  /@types/node/12.20.55:
    resolution: {integrity: sha512-J8xLz7q2OFulZ2cyGTLE1TbbZcjpno7FaN6zdJNrgAdrJ+DZzh/uFR6YrTb4C+nXakvud8Q4+rbhoIWlYQbUFQ==}
    dev: true

  /@types/vscode/1.69.0:
    resolution: {integrity: sha512-RlzDAnGqUoo9wS6d4tthNyAdZLxOIddLiX3djMoWk29jFfSA1yJbIwr0epBYqqYarWB6s2Z+4VaZCQ80Jaa3kA==}
    dev: true

  /@typescript-eslint/eslint-plugin/4.33.0_3ekaj7j3owlolnuhj3ykrb7u7i:
    resolution: {integrity: sha512-aINiAxGVdOl1eJyVjaWn/YcVAq4Gi/Yo35qHGCnqbWVz61g39D0h23veY/MA0rFFGfxK7TySg2uwDeNv+JgVpg==}
    engines: {node: ^10.12.0 || >=12.0.0}
    peerDependencies:
      '@typescript-eslint/parser': ^4.0.0
      eslint: ^5.0.0 || ^6.0.0 || ^7.0.0
      typescript: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@typescript-eslint/experimental-utils': 4.33.0_hxadhbs2xogijvk7vq4t2azzbu
      '@typescript-eslint/parser': 4.33.0_hxadhbs2xogijvk7vq4t2azzbu
      '@typescript-eslint/scope-manager': 4.33.0
      debug: 4.3.4
      eslint: 7.32.0
      functional-red-black-tree: 1.0.1
      ignore: 5.2.0
      regexpp: 3.2.0
      semver: 7.3.7
      tsutils: 3.21.0_typescript@4.7.4
      typescript: 4.7.4
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@typescript-eslint/experimental-utils/4.33.0_hxadhbs2xogijvk7vq4t2azzbu:
    resolution: {integrity: sha512-zeQjOoES5JFjTnAhI5QY7ZviczMzDptls15GFsI6jyUOq0kOf9+WonkhtlIhh0RgHRnqj5gdNxW5j1EvAyYg6Q==}
    engines: {node: ^10.12.0 || >=12.0.0}
    peerDependencies:
      eslint: '*'
    dependencies:
      '@types/json-schema': 7.0.11
      '@typescript-eslint/scope-manager': 4.33.0
      '@typescript-eslint/types': 4.33.0
      '@typescript-eslint/typescript-estree': 4.33.0_typescript@4.7.4
      eslint: 7.32.0
      eslint-scope: 5.1.1
      eslint-utils: 3.0.0_eslint@7.32.0
    transitivePeerDependencies:
      - supports-color
      - typescript
    dev: true

  /@typescript-eslint/parser/4.33.0_hxadhbs2xogijvk7vq4t2azzbu:
    resolution: {integrity: sha512-ZohdsbXadjGBSK0/r+d87X0SBmKzOq4/S5nzK6SBgJspFo9/CUDJ7hjayuze+JK7CZQLDMroqytp7pOcFKTxZA==}
    engines: {node: ^10.12.0 || >=12.0.0}
    peerDependencies:
      eslint: ^5.0.0 || ^6.0.0 || ^7.0.0
      typescript: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@typescript-eslint/scope-manager': 4.33.0
      '@typescript-eslint/types': 4.33.0
      '@typescript-eslint/typescript-estree': 4.33.0_typescript@4.7.4
      debug: 4.3.4
      eslint: 7.32.0
      typescript: 4.7.4
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@typescript-eslint/scope-manager/4.33.0:
    resolution: {integrity: sha512-5IfJHpgTsTZuONKbODctL4kKuQje/bzBRkwHE8UOZ4f89Zeddg+EGZs8PD8NcN4LdM3ygHWYB3ukPAYjvl/qbQ==}
    engines: {node: ^8.10.0 || ^10.13.0 || >=11.10.1}
    dependencies:
      '@typescript-eslint/types': 4.33.0
      '@typescript-eslint/visitor-keys': 4.33.0
    dev: true

  /@typescript-eslint/types/4.33.0:
    resolution: {integrity: sha512-zKp7CjQzLQImXEpLt2BUw1tvOMPfNoTAfb8l51evhYbOEEzdWyQNmHWWGPR6hwKJDAi+1VXSBmnhL9kyVTTOuQ==}
    engines: {node: ^8.10.0 || ^10.13.0 || >=11.10.1}
    dev: true

  /@typescript-eslint/typescript-estree/4.33.0_typescript@4.7.4:
    resolution: {integrity: sha512-rkWRY1MPFzjwnEVHsxGemDzqqddw2QbTJlICPD9p9I9LfsO8fdmfQPOX3uKfUaGRDFJbfrtm/sXhVXN4E+bzCA==}
    engines: {node: ^10.12.0 || >=12.0.0}
    peerDependencies:
      typescript: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@typescript-eslint/types': 4.33.0
      '@typescript-eslint/visitor-keys': 4.33.0
      debug: 4.3.4
      globby: 11.1.0
      is-glob: 4.0.3
      semver: 7.3.7
      tsutils: 3.21.0_typescript@4.7.4
      typescript: 4.7.4
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@typescript-eslint/visitor-keys/4.33.0:
    resolution: {integrity: sha512-uqi/2aSz9g2ftcHWf8uLPJA70rUv6yuMW5Bohw+bwcuzaxQIHaKFZCKGoGXIrc9vkTJ3+0txM73K0Hq3d5wgIg==}
    engines: {node: ^8.10.0 || ^10.13.0 || >=11.10.1}
    dependencies:
      '@typescript-eslint/types': 4.33.0
      eslint-visitor-keys: 2.1.0
    dev: true

  /acorn-jsx/5.3.2_acorn@7.4.1:
    resolution: {integrity: sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==}
    peerDependencies:
      acorn: ^6.0.0 || ^7.0.0 || ^8.0.0
    dependencies:
      acorn: 7.4.1
    dev: true

  /acorn/7.4.1:
    resolution: {integrity: sha512-nQyp0o1/mNdbTO1PO6kHkwSrmgZ0MT/jCCpNiwbUjGoRN4dlBhqJtoQuCnEOKzgTVwg0ZWiCoQy6SxMebQVh8A==}
    engines: {node: '>=0.4.0'}
    hasBin: true
    dev: true

  /agent-base/6.0.2:
    resolution: {integrity: sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==}
    engines: {node: '>= 6.0.0'}
    dependencies:
      debug: 4.3.4
    transitivePeerDependencies:
      - supports-color
    dev: true

  /ajv/6.12.6:
    resolution: {integrity: sha512-j3fVLgvTo527anyYyJOGTYJbG+vnnQYvE0m5mmkc1TK+nxAppkCLMIL0aZ4dblVCNoGShhm+kzE4ZUykBoMg4g==}
    dependencies:
      fast-deep-equal: 3.1.3
      fast-json-stable-stringify: 2.1.0
      json-schema-traverse: 0.4.1
      uri-js: 4.4.1
    dev: true

  /ajv/8.11.0:
    resolution: {integrity: sha512-wGgprdCvMalC0BztXvitD2hC04YffAvtsUn93JbGXYLAtCUO4xd17mCCZQxUOItiBwZvJScWo8NIvQMQ71rdpg==}
    dependencies:
      fast-deep-equal: 3.1.3
      json-schema-traverse: 1.0.0
      require-from-string: 2.0.2
      uri-js: 4.4.1
    dev: true

  /ansi-colors/4.1.3:
    resolution: {integrity: sha512-/6w/C21Pm1A7aZitlI5Ni/2J6FFQN8i1Cvz3kHABAAbw93v/NlvKdVOqz7CCWz/3iv/JplRSEEZ83XION15ovw==}
    engines: {node: '>=6'}
    dev: true

  /ansi-regex/5.0.1:
    resolution: {integrity: sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==}
    engines: {node: '>=8'}
    dev: true

  /ansi-styles/3.2.1:
    resolution: {integrity: sha512-VT0ZI6kZRdTh8YyJw3SMbYm/u+NqfsAxEpWO0Pf9sq8/e94WxxOpPKx9FR1FlyCtOVDNOQ+8ntlqFxiRc+r5qA==}
    engines: {node: '>=4'}
    dependencies:
      color-convert: 1.9.3
    dev: true

  /ansi-styles/4.3.0:
    resolution: {integrity: sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==}
    engines: {node: '>=8'}
    dependencies:
      color-convert: 2.0.1
    dev: true

  /argparse/1.0.10:
    resolution: {integrity: sha512-o5Roy6tNG4SL/FOkCAN6RzjiakZS25RLYFrcMttJqbdd8BWrnA+fGz57iN5Pb06pvBGvl5gQ0B48dJlslXvoTg==}
    dependencies:
      sprintf-js: 1.0.3
    dev: true

  /array-union/2.1.0:
    resolution: {integrity: sha512-HGyxoOTYUyCM6stUe6EJgnd4EoewAI7zMdfqO+kGjnlZmBDz/cR5pf8r/cR4Wq60sL/p0IkcjUEEPwS3GFrIyw==}
    engines: {node: '>=8'}
    dev: true

  /astral-regex/2.0.0:
    resolution: {integrity: sha512-Z7tMw1ytTXt5jqMcOP+OQteU1VuNK9Y02uuJtKQ1Sv69jXQKKg5cibLwGJow8yzZP+eAc18EmLGPal0bp36rvQ==}
    engines: {node: '>=8'}
    dev: true

  /balanced-match/1.0.2:
    resolution: {integrity: sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==}
    dev: true

  /big-integer/1.6.51:
    resolution: {integrity: sha512-GPEid2Y9QU1Exl1rpO9B2IPJGHPSupF5GnVIP0blYvNOMer2bTvSWs1jGOUg04hTmu67nmLsQ9TBo1puaotBHg==}
    engines: {node: '>=0.6'}
    dev: true

  /binary/0.3.0:
    resolution: {integrity: sha512-D4H1y5KYwpJgK8wk1Cue5LLPgmwHKYSChkbspQg5JtVuR5ulGckxfR62H3AE9UDkdMC8yyXlqYihuz3Aqg2XZg==}
    dependencies:
      buffers: 0.1.1
      chainsaw: 0.1.0
    dev: true

  /bluebird/3.4.7:
    resolution: {integrity: sha512-iD3898SR7sWVRHbiQv+sHUtHnMvC1o3nW5rAcqnq3uOn07DSAppZYUkIGslDz6gXC7HfunPe7YVBgoEJASPcHA==}
    dev: true

  /brace-expansion/1.1.11:
    resolution: {integrity: sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==}
    dependencies:
      balanced-match: 1.0.2
      concat-map: 0.0.1
    dev: true

  /braces/3.0.2:
    resolution: {integrity: sha512-b8um+L1RzM3WDSzvhm6gIz1yfTbBt6YTlcEKAvsmqCZZFw46z626lVj9j1yEPW33H5H+lBQpZMP1k8l+78Ha0A==}
    engines: {node: '>=8'}
    dependencies:
      fill-range: 7.0.1
    dev: true

  /buffer-indexof-polyfill/1.0.2:
    resolution: {integrity: sha512-I7wzHwA3t1/lwXQh+A5PbNvJxgfo5r3xulgpYDB5zckTu/Z9oUK9biouBKQUjEqzaz3HnAT6TYoovmE+GqSf7A==}
    engines: {node: '>=0.10'}
    dev: true

  /buffers/0.1.1:
    resolution: {integrity: sha512-9q/rDEGSb/Qsvv2qvzIzdluL5k7AaJOTrw23z9reQthrbF7is4CtlT0DXyO1oei2DCp4uojjzQ7igaSHp1kAEQ==}
    engines: {node: '>=0.2.0'}
    dev: true

  /callsites/3.1.0:
    resolution: {integrity: sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==}
    engines: {node: '>=6'}
    dev: true

  /chainsaw/0.1.0:
    resolution: {integrity: sha512-75kWfWt6MEKNC8xYXIdRpDehRYY/tNSgwKaJq+dbbDcxORuVrrQ+SEHoWsniVn9XPYfP4gmdWIeDk/4YNp1rNQ==}
    dependencies:
      traverse: 0.3.9
    dev: true

  /chalk/2.4.2:
    resolution: {integrity: sha512-Mti+f9lpJNcwF4tWV8/OrTTtF1gZi+f8FqlyAdouralcFWFQWF2+NgCHShjkCb+IFBLq9buZwE1xckQU4peSuQ==}
    engines: {node: '>=4'}
    dependencies:
      ansi-styles: 3.2.1
      escape-string-regexp: 1.0.5
      supports-color: 5.5.0
    dev: true

  /chalk/4.1.2:
    resolution: {integrity: sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==}
    engines: {node: '>=10'}
    dependencies:
      ansi-styles: 4.3.0
      supports-color: 7.2.0
    dev: true

  /cliui/7.0.4:
    resolution: {integrity: sha512-OcRE68cOsVMXp1Yvonl/fzkQOyjLSu/8bhPDfQt0e0/Eb283TKP20Fs2MqoPsr9SwA595rRCA+QMzYc9nBP+JQ==}
    dependencies:
      string-width: 4.2.3
      strip-ansi: 6.0.1
      wrap-ansi: 7.0.0
    dev: true

  /color-convert/1.9.3:
    resolution: {integrity: sha512-QfAUtd+vFdAtFQcC8CCyYt1fYWxSqAiK2cSD6zDB8N3cpsEBAvRxp9zOGg6G/SHHJYAT88/az/IuDGALsNVbGg==}
    dependencies:
      color-name: 1.1.3
    dev: true

  /color-convert/2.0.1:
    resolution: {integrity: sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==}
    engines: {node: '>=7.0.0'}
    dependencies:
      color-name: 1.1.4
    dev: true

  /color-name/1.1.3:
    resolution: {integrity: sha512-72fSenhMw2HZMTVHeCA9KCmpEIbzWiQsjN+BHcBbS9vr1mtt+vJjPdksIBNUmKAW8TFUDPJK5SUU3QhE9NEXDw==}
    dev: true

  /color-name/1.1.4:
    resolution: {integrity: sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==}
    dev: true

  /comment-parser/1.3.1:
    resolution: {integrity: sha512-B52sN2VNghyq5ofvUsqZjmk6YkihBX5vMSChmSK9v4ShjKf3Vk5Xcmgpw4o+iIgtrnM/u5FiMpz9VKb8lpBveA==}
    engines: {node: '>= 12.0.0'}
    dev: false

  /concat-map/0.0.1:
    resolution: {integrity: sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKn
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "module": "commonjs",
    "target": "es6",
    "outDir": "out",
    "lib": ["es6", "dom"],
    "sourceMap": true,
    "rootDir": "src",
    "strict": true
  },
  "exclude": ["node_modules", ".vscode-test", "webview-ui"]
}

```

### File: docs\extension-commands.md
```md
# Extension commands

A quick run down of some of the important commands that can be run when at the root of the project.

```
npm run install:all      Install package dependencies for both the extension and React webview source code.
npm run start:webview    Runs the React webview source code in development mode. Open http://localhost:3000 to view it in the browser.
npm run build:webview    Build React webview source code. Must be executed before compiling or running the extension.
npm run compile          Compile VS Code extension
```

```

### File: docs\extension-development-cycle.md
```md
# Extension development cycle

The intended development cycle of this React-based webview extension is slightly different than that of other VS Code extensions.

Due to the fact that the `webview-ui` directory holds a self-contained React application we get to take advantage of some of the perks that that enables. In particular,

- UI development and iteration cycles can happen much more quickly by using Vite
- Dependency management and project configuration is hugely simplified

## UI development cycle

Since we can take advantage of the much faster Vite dev server, it is encouraged to begin developing webview UI by running the `npm run start:webview` command and then editing the code in the `webview-ui/src` directory.

_Tip: Open the command palette and run the `Simple Browser` command and fill in `http://localhost:3000/` when prompted. This will open a simple browser environment right inside VS Code._

### Message passing
If you need to implement message passing between the webview context and extension context via the VS Code API, a helpful utility is provided in the `webview-ui/src/utilities/vscode.ts` file.

This file contains a utility wrapper around the `acquireVsCodeApi()` function, which enables message passing and state management between the webview and extension contexts.

This utility also enables webview code to be run in the Vite dev server by using native web browser features that mock the functionality enabled by acquireVsCodeApi. This means you can keep building your webview UI with the Vite dev server even when using the VS Code API.

### Move to traditional extension development
Once you're ready to start building other parts of your extension, simply shift to a development model where you run the `npm run build:webview` command as you make changes, press `F5` to compile your extension and open a new Extension Development Host window. Inside the host window, open the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and type `Hello World (React + Vite): Show`.

## Dependency management and project configuration

As mentioned above, the `webview-ui` directory holds a self-contained and isolated React application meaning you can (for the most part) treat the development of your webview UI in the same way you would treat the development of a regular React application.

To install webview-specific dependencies simply navigate (i.e. `cd`) into the `webview-ui` directory and install any packages you need or set up any React specific configurations you want.

```

### File: docs\extension-structure.md
```md
# Extension structure

This section provides a quick introduction into how this sample extension is organized and structured.

The two most important directories to take note of are the following:

- `src`: Contains all of the extension source code
- `webview-ui`: Contains all of the webview UI source code

## `src` directory

The `src` directory contains all of the extension-related source code and can be thought of as containing the "backend" code/logic for the entire extension. Inside of this directory you'll find the:

- `panels` directory
- `utilities` directory
- `extension.ts` file

The `panels` directory contains all of the webview-related code that will be executed within the extension context. It can be thought of as the place where all of the "backend" code for each webview panel is contained.

This directory will typically contain individual TypeScript or JavaScript files that contain a class which manages the state and behavior of a given webview panel. Each class is usually in charge of:

- Creating and rendering the webview panel
- Properly cleaning up and disposing of webview resources when the panel is closed
- Setting message listeners so data can be passed between the webview and extension
- Setting the initial HTML markdown of the webview panel
- Other custom logic and behavior related to webview panel management

As the name might suggest, the `utilties` directory contains all of the extension utility functions that make setting up and managing an extension easier. In this case, it contains `getUri.ts` which contains a helper function which will get the webview URI of a given file or resource.

Finally, `extension.ts` is where all the logic for activating and deactiving the extension usually live. This is also the place where extension commands are registered.

## `webview-ui` directory

The `webview-ui` directory contains all of the React-based webview source code and can be thought of as containing the "frontend" code/logic for the extension webview.

This directory is special because it contains a full-blown React application which was created using the TypeScript [Vite](https://vitejs.dev/) template. As a result, `webview-ui` contains its own `package.json`, `node_modules`, `tsconfig.json`, and so on––separate from the `hello-world` extension in the root directory.

This strays a bit from other extension structures, in that you'll usually find the extension and webview dependencies, configurations, and source code more closely integrated or combined with each other.

However, in this case, there are some unique benefits and reasons for why this sample extension does not follow those patterns such as easier management of conflicting dependencies and configurations, as well as the ability to use the Vite dev server, which drastically improves the speed of developing your webview UI, versus recompiling your extension code every time you make a change to the webview.

```

### File: src\extension.ts
```ts
import { commands, ExtensionContext, window } from "vscode";
import { SidebarProvider } from "./panels/SidebarProvider";

export function activate(context: ExtensionContext) {
  // Register the Sidebar Panel
  const sidebarProvider = new SidebarProvider(context.extensionUri);
  context.subscriptions.push(
    window.registerWebviewViewProvider("myextension-sidebar", sidebarProvider)
  );

  // Add command to the extension context

  context.subscriptions.push(
    commands.registerCommand("myextension.sayhello", () => {
      window.showInformationMessage("Hello World!");
    })
  );

  context.subscriptions.push(
    commands.registerCommand("myextension.askquestion", async () => {
      let response = await window.showInformationMessage("How are you doing?", "Good", "Bad");
      if (response === "Bad") {
        window.showInformationMessage("I'm sorry");
      }
    })
  );

  // context.subscriptions.push(showHelloWorldCommand);
}

```

### File: src\panels\SidebarProvider.ts
```ts
import * as vscode from "vscode";
import { getUri } from "../utilities/getUri";
import { requireModule } from "../utilities/require-config";

export class SidebarProvider implements vscode.WebviewViewProvider {
  _view?: vscode.WebviewView;
  _doc?: vscode.TextDocument;

  constructor(private readonly _extensionUri: vscode.Uri) {}

  public resolveWebviewView(webviewView: vscode.WebviewView) {
    this._view = webviewView;

    webviewView.webview.options = {
      // Allow scripts in the webview
      enableScripts: true,

      localResourceRoots: [this._extensionUri],
    };

    webviewView.webview.html = this._getHtmlForWebview(webviewView.webview);

    // Listen for messages from the Sidebar component and execute action
    webviewView.webview.onDidReceiveMessage(async (data) => {
      console.log("data", data);
      switch (data.type) {
        case "onMessageSend": {
          if (!data.value) {
            return;
          }
          vscode.window.showInformationMessage(
            `Message from sidebar: ${data.value}`
          );
          break;
        }
        case "onInfo": {
          if (!data.value) {
            return;
          }
          vscode.window.showInformationMessage(data.value);
          break;
        }
        case "onError": {
          if (!data.value) {
            return;
          }
          vscode.window.showErrorMessage(data.value);
          break;
        }
      }
    });
  }

  public revive(panel: vscode.WebviewView) {
    this._view = panel;
  }

  private _getHtmlForWebview(webview: vscode.Webview) {
    // The CSS file from the React build output
    const stylesUri = getUri(webview, this._extensionUri, [
      "webview-ui",
      "build",
      "assets",
      "index.css",
    ]);
    // The JS file from the React build output
    const scriptUri = getUri(webview, this._extensionUri, [
      "webview-ui",
      "build",
      "assets",
      "index.js",
    ]);

    const workspaceFolder = vscode.workspace.workspaceFolders?.[0];
    const workspaceUri = workspaceFolder?.uri;
    const configPath = vscode.Uri.joinPath(
      workspaceUri!,
      "myext.config.ts"
    ).fsPath;
    let config;

    try {
      config = requireModule(configPath);
    } catch (error) {}

    // if (!config) return "Config Not found";

    if (workspaceFolder) {
      const watcher = vscode.workspace.createFileSystemWatcher(
        new vscode.RelativePattern(workspaceFolder, "myext.config.ts")
      );
      watcher.onDidChange((uri) => {
        const newConfig = requireModule(uri.path);
        this._view?.webview.postMessage({
          type: "onConfigChange",
          value: newConfig,
        });
      });
    }

    // Tip: Install the es6-string-html VS Code extension to enable code highlighting below
    return /*html*/ `
     <!DOCTYPE html>
     <html lang="en">
       <head>
         <meta charset="UTF-8" />
         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
         <link rel="stylesheet" type="text/css" href="${stylesUri}">
         <title>Hello World</title>
       </head>
       <body>
        <div id="root"></div>
        <script>
          window.config = ${JSON.stringify(config)}
        </script>
        <script type="module" src="${scriptUri}"></script>
       </body>
     </html>
   `;
  }
}

```

### File: src\utilities\get-nonce.ts
```ts
export function getNonce() {
  let text = "";
  const possible =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  for (let i = 0; i < 32; i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
}

```

### File: src\utilities\getUri.ts
```ts
import { Uri, Webview } from "vscode";

/**
 * A helper function which will get the webview URI of a given file or resource.
 *
 * @remarks This URI can be used within a webview's HTML as a link to the
 * given file/resource.
 *
 * @param webview A reference to the extension webview
 * @param extensionUri The URI of the directory containing the extension
 * @param pathList An array of strings representing the path to a file/resource
 * @returns A URI pointing to the file/resource
 */
export function getUri(webview: Webview, extensionUri: Uri, pathList: string[]) {
  return webview.asWebviewUri(Uri.joinPath(extensionUri, ...pathList));
}

```

### File: src\utilities\require-config.ts
```ts
import * as tsImport from "ts-import";

export function requireModule(module: string) {
  const res = tsImport.loadSync(module, {
    mode: tsImport.LoadMode.Compile,
    compileOptions: {},
  }).default;
  return res;
}

```

