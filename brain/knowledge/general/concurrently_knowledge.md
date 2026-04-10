# Knowledge Dump for concurrently

## File: .prettierrc.json
```
{
  "singleQuote": true
}

```

## File: contributing.md
```
# Contributing

Pull requests and contributions are warmly welcome.
Please follow existing code style and commit message conventions. Also remember to keep documentation
updated.

**Pull requests:** You don't need to bump version numbers or modify anything related to releasing. That stuff is fully automated, just write the functionality.

# Maintaining

## Code Format & Linting

Code format and lint checks are performed locally when committing to ensure the changes align with the configured rules of this repository. This happens with the help of the tools [simple-git-hooks](https://github.com/toplenboren/simple-git-hooks) and [lint-staged](https://github.com/okonet/lint-staged) which are automatically installed and configured on `pnpm install` (no further steps required).

In case of problems, a corresponding message is displayed in your terminal.
Please fix them and then run the commit command again.

## Test

Tests can be executed with the following command:

```bash
pnpm test
```

```

## File: eslint.config.js
```
// @ts-check

import eslint from '@eslint/js';
import pluginVitest from '@vitest/eslint-plugin';
import { defineConfig } from 'eslint/config';
import gitignore from 'eslint-config-flat-gitignore';
import pluginImportLite from 'eslint-plugin-import-lite';
import pluginPrettierRecommended from 'eslint-plugin-prettier/recommended';
import pluginSimpleImportSort from 'eslint-plugin-simple-import-sort';
import globals from 'globals';
import tseslint from 'typescript-eslint';

export default defineConfig(
    gitignore(),
    {
        languageOptions: {
            globals: {
                ...globals.node,
            },
            ecmaVersion: 2023,
        },
    },
    eslint.configs.recommended,
    tseslint.configs.recommended,
    {
        rules: {
            curly: 'error',
            eqeqeq: ['error', 'always', { null: 'ignore' }],
            'no-var': 'error',
            'no-console': 'error',
            'prefer-const': 'error',
            'prefer-object-spread': 'error',
            '@typescript-eslint/no-unused-vars': [
                'error',
                {
                    varsIgnorePattern: '^_',
                },
            ],
        },
    },
    { files: ['**/__fixtures__/**/*.{js,ts}'], rules: { 'no-console': 'off' } },
    {
        plugins: {
            'simple-import-sort': pluginSimpleImportSort,
            import: pluginImportLite,
        },
        rules: {
            'simple-import-sort/imports': 'error',
            'simple-import-sort/exports': 'error',
            'import/first': 'error',
            'import/newline-after-import': 'error',
            'import/no-duplicates': 'error',
        },
    },
    {
        files: ['**/*.spec.ts'],
        plugins: {
            vitest: pluginVitest,
        },
        rules: {
            ...pluginVitest.configs.recommended.rules,
            // Currently produces false positives, see https://github.com/vitest-dev/eslint-plugin-vitest/issues/775
            'vitest/prefer-called-exactly-once-with': 'off',
        },
    },
    pluginPrettierRecommended,
);

```

## File: package.json
```
{
  "name": "concurrently",
  "type": "module",
  "version": "9.2.1",
  "packageManager": "pnpm@10.18.2+sha512.9fb969fa749b3ade6035e0f109f0b8a60b5d08a1a87fdf72e337da90dcc93336e2280ca4e44f2358a649b83c17959e9993e777c2080879f3801e6f0d999ad3dd",
  "description": "Run commands concurrently",
  "author": "Kimmo Brunfeldt",
  "license": "MIT",
  "funding": "https://github.com/open-cli-tools/concurrently?sponsor=1",
  "repository": {
    "type": "git",
    "url": "https://github.com/open-cli-tools/concurrently.git"
  },
  "keywords": [
    "bash",
    "concurrent",
    "parallel",
    "concurrently",
    "command",
    "sh"
  ],
  "exports": {
    ".": "./dist/lib/index.js",
    "./package.json": "./package.json"
  },
  "types": "./dist/lib/index.d.ts",
  "publishConfig": {
    "bin": {
      "concurrently": "./dist/bin/index.js",
      "conc": "./dist/bin/index.js"
    }
  },
  "files": [
    "!**/*.spec.d.ts",
    "!**/*.spec.js",
    "!**/__fixtures__",
    "dist",
    "dist/tsconfig.tsbuildinfo",
    "docs"
  ],
  "engines": {
    "node": ">=20"
  },
  "scripts": {
    "build": "tsc --build",
    "postbuild": "chmod +x dist/bin/index.js",
    "typecheck": "tsc --noEmit",
    "format": "prettier --check '**/*.{json,y?(a)ml,md}'",
    "lint": "eslint",
    "prepublishOnly": "safe-publish-latest && pnpm run build",
    "test": "vitest --project unit",
    "test:smoke": "vitest run --project smoke",
    "prepare": "husky"
  },
  "dependencies": {
    "chalk": "5.6.2",
    "rxjs": "7.8.2",
    "shell-quote": "1.8.3",
    "supports-color": "10.2.2",
    "tree-kill": "1.2.2",
    "yargs": "17.7.2"
  },
  "devDependencies": {
    "@eslint/js": "^9.37.0",
    "@hirez_io/observer-spy": "^2.2.0",
    "@types/node": "^20.19.20",
    "@types/shell-quote": "^1.7.5",
    "@types/yargs": "^17.0.33",
    "@vitest/coverage-v8": "^3.2.4",
    "@vitest/eslint-plugin": "^1.3.16",
    "ctrlc-wrapper": "^0.0.5",
    "esbuild": "~0.25.10",
    "eslint": "^9.37.0",
    "eslint-config-flat-gitignore": "^2.1.0",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-import-lite": "^0.3.0",
    "eslint-plugin-prettier": "^5.5.4",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "globals": "^16.4.0",
    "husky": "^9.1.7",
    "lint-staged": "^16.2.3",
    "prettier": "^3.6.2",
    "safe-publish-latest": "^2.0.0",
    "string-argv": "^0.3.2",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.46.0",
    "vitest": "^3.2.4"
  },
  "lint-staged": {
    "*.{js,ts}": "eslint --fix",
    "*.{json,y?(a)ml,md}": "prettier --write"
  }
}

```

## File: pnpm-lock.yaml
```
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      chalk:
        specifier: 5.6.2
        version: 5.6.2
      rxjs:
        specifier: 7.8.2
        version: 7.8.2
      shell-quote:
        specifier: 1.8.3
        version: 1.8.3
      supports-color:
        specifier: 10.2.2
        version: 10.2.2
      tree-kill:
        specifier: 1.2.2
        version: 1.2.2
      yargs:
        specifier: 17.7.2
        version: 17.7.2
    devDependencies:
      '@eslint/js':
        specifier: ^9.37.0
        version: 9.37.0
      '@hirez_io/observer-spy':
        specifier: ^2.2.0
        version: 2.2.0(rxjs@7.8.2)(typescript@5.9.3)
      '@types/node':
        specifier: ^20.19.20
        version: 20.19.20
      '@types/shell-quote':
        specifier: ^1.7.5
        version: 1.7.5
      '@types/yargs':
        specifier: ^17.0.33
        version: 17.0.33
      '@vitest/coverage-v8':
        specifier: ^3.2.4
        version: 3.2.4(supports-color@10.2.2)(vitest@3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1))
      '@vitest/eslint-plugin':
        specifier: ^1.3.16
        version: 1.3.16(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)(vitest@3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1))
      ctrlc-wrapper:
        specifier: ^0.0.5
        version: 0.0.5
      esbuild:
        specifier: ~0.25.10
        version: 0.25.10
      eslint:
        specifier: ^9.37.0
        version: 9.37.0(supports-color@10.2.2)
      eslint-config-flat-gitignore:
        specifier: ^2.1.0
        version: 2.1.0(eslint@9.37.0(supports-color@10.2.2))
      eslint-config-prettier:
        specifier: ^10.1.8
        version: 10.1.8(eslint@9.37.0(supports-color@10.2.2))
      eslint-plugin-import-lite:
        specifier: ^0.3.0
        version: 0.3.0(eslint@9.37.0(supports-color@10.2.2))(typescript@5.9.3)
      eslint-plugin-prettier:
        specifier: ^5.5.4
        version: 5.5.4(eslint-config-prettier@10.1.8(eslint@9.37.0(supports-color@10.2.2)))(eslint@9.37.0(supports-color@10.2.2))(prettier@3.6.2)
      eslint-plugin-simple-import-sort:
        specifier: ^12.1.1
        version: 12.1.1(eslint@9.37.0(supports-color@10.2.2))
      globals:
        specifier: ^16.4.0
        version: 16.4.0
      husky:
        specifier: ^9.1.7
        version: 9.1.7
      lint-staged:
        specifier: ^16.2.3
        version: 16.2.3
      prettier:
        specifier: ^3.6.2
        version: 3.6.2
      safe-publish-latest:
        specifier: ^2.0.0
        version: 2.0.0
      string-argv:
        specifier: ^0.3.2
        version: 0.3.2
      typescript:
        specifier: ~5.9.3
        version: 5.9.3
      typescript-eslint:
        specifier: ^8.46.0
        version: 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      vitest:
        specifier: ^3.2.4
        version: 3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1)

  tests:
    dependencies:
      concurrently:
        specifier: workspace:*
        version: link:..

packages:

  '@ampproject/remapping@2.3.0':
    resolution: {integrity: sha512-30iZtAPgz+LTIYoeivqYo853f02jBYSd5uGnGpkFV0M3xOt9aN73erkgYAmZU43x4VfqcnLxW9Kpg3R5LC4YYw==}
    engines: {node: '>=6.0.0'}

  '@babel/helper-string-parser@7.27.1':
    resolution: {integrity: sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-identifier@7.27.1':
    resolution: {integrity: sha512-D2hP9eA+Sqx1kBZgzxZh0y1trbuU+JoDkiEwqhQ36nodYqJwyEIhPSdMNd7lOm/4io72luTPWH20Yda0xOuUow==}
    engines: {node: '>=6.9.0'}

  '@babel/parser@7.28.4':
    resolution: {integrity: sha512-yZbBqeM6TkpP9du/I2pUZnJsRMGGvOuIrhjzC1AwHwW+6he4mni6Bp/m8ijn0iOuZuPI2BfkCoSRunpyjnrQKg==}
    engines: {node: '>=6.0.0'}
    hasBin: true

  '@babel/types@7.28.4':
    resolution: {integrity: sha512-bkFqkLhh3pMBUQQkpVgWDWq/lqzc2678eUyDlTBhRqhCHFguYYGM0Efga7tYk4TogG/3x0EEl66/OQ+WGbWB/Q==}
    engines: {node: '>=6.9.0'}

  '@bcoe/v8-coverage@1.0.2':
    resolution: {integrity: sha512-6zABk/ECA/QYSCQ1NGiVwwbQerUCZ+TQbp64Q3AgmfNvurHH0j8TtXa1qbShXA6qqkpAj4V5W8pP6mLe1mcMqA==}
    engines: {node: '>=18'}

  '@esbuild/aix-ppc64@0.25.10':
    resolution: {integrity: sha512-0NFWnA+7l41irNuaSVlLfgNT12caWJVLzp5eAVhZ0z1qpxbockccEt3s+149rE64VUI3Ml2zt8Nv5JVc4QXTsw==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.25.10':
    resolution: {integrity: sha512-LSQa7eDahypv/VO6WKohZGPSJDq5OVOo3UoFR1E4t4Gj1W7zEQMUhI+lo81H+DtB+kP+tDgBp+M4oNCwp6kffg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.25.10':
    resolution: {integrity: sha512-dQAxF1dW1C3zpeCDc5KqIYuZ1tgAdRXNoZP7vkBIRtKZPYe2xVr/d3SkirklCHudW1B45tGiUlz2pUWDfbDD4w==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.25.10':
    resolution: {integrity: sha512-MiC9CWdPrfhibcXwr39p9ha1x0lZJ9KaVfvzA0Wxwz9ETX4v5CHfF09bx935nHlhi+MxhA63dKRRQLiVgSUtEg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.25.10':
    resolution: {integrity: sha512-JC74bdXcQEpW9KkV326WpZZjLguSZ3DfS8wrrvPMHgQOIEIG/sPXEN/V8IssoJhbefLRcRqw6RQH2NnpdprtMA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.25.10':
    resolution: {integrity: sha512-tguWg1olF6DGqzws97pKZ8G2L7Ig1vjDmGTwcTuYHbuU6TTjJe5FXbgs5C1BBzHbJ2bo1m3WkQDbWO2PvamRcg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.25.10':
    resolution: {integrity: sha512-3ZioSQSg1HT2N05YxeJWYR+Libe3bREVSdWhEEgExWaDtyFbbXWb49QgPvFH8u03vUPX10JhJPcz7s9t9+boWg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.25.10':
    resolution: {integrity: sha512-LLgJfHJk014Aa4anGDbh8bmI5Lk+QidDmGzuC2D+vP7mv/GeSN+H39zOf7pN5N8p059FcOfs2bVlrRr4SK9WxA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.25.10':
    resolution: {integrity: sha512-5luJWN6YKBsawd5f9i4+c+geYiVEw20FVW5x0v1kEMWNq8UctFjDiMATBxLvmmHA4bf7F6hTRaJgtghFr9iziQ==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.25.10':
    resolution: {integrity: sha512-oR31GtBTFYCqEBALI9r6WxoU/ZofZl962pouZRTEYECvNF/dtXKku8YXcJkhgK/beU+zedXfIzHijSRapJY3vg==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.25.10':
    resolution: {integrity: sha512-NrSCx2Kim3EnnWgS4Txn0QGt0Xipoumb6z6sUtl5bOEZIVKhzfyp/Lyw4C1DIYvzeW/5mWYPBFJU3a/8Yr75DQ==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.25.10':
    resolution: {integrity: sha512-xoSphrd4AZda8+rUDDfD9J6FUMjrkTz8itpTITM4/xgerAZZcFW7Dv+sun7333IfKxGG8gAq+3NbfEMJfiY+Eg==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.25.10':
    resolution: {integrity: sha512-ab6eiuCwoMmYDyTnyptoKkVS3k8fy/1Uvq7Dj5czXI6DF2GqD2ToInBI0SHOp5/X1BdZ26RKc5+qjQNGRBelRA==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.25.10':
    resolution: {integrity: sha512-NLinzzOgZQsGpsTkEbdJTCanwA5/wozN9dSgEl12haXJBzMTpssebuXR42bthOF3z7zXFWH1AmvWunUCkBE4EA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.25.10':
    resolution: {integrity: sha512-FE557XdZDrtX8NMIeA8LBJX3dC2M8VGXwfrQWU7LB5SLOajfJIxmSdyL/gU1m64Zs9CBKvm4UAuBp5aJ8OgnrA==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.25.10':
    resolution: {integrity: sha512-3BBSbgzuB9ajLoVZk0mGu+EHlBwkusRmeNYdqmznmMc9zGASFjSsxgkNsqmXugpPk00gJ0JNKh/97nxmjctdew==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.25.10':
    resolution: {integrity: sha512-QSX81KhFoZGwenVyPoberggdW1nrQZSvfVDAIUXr3WqLRZGZqWk/P4T8p2SP+de2Sr5HPcvjhcJzEiulKgnxtA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.25.10':
    resolution: {integrity: sha512-AKQM3gfYfSW8XRk8DdMCzaLUFB15dTrZfnX8WXQoOUpUBQ+NaAFCP1kPS/ykbbGYz7rxn0WS48/81l9hFl3u4A==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.25.10':
    resolution: {integrity: sha512-7RTytDPGU6fek/hWuN9qQpeGPBZFfB4zZgcz2VK2Z5VpdUxEI8JKYsg3JfO0n/Z1E/6l05n0unDCNc4HnhQGig==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/openbsd-arm64@0.25.10':
    resolution: {integrity: sha512-5Se0VM9Wtq797YFn+dLimf2Zx6McttsH2olUBsDml+lm0GOCRVebRWUvDtkY4BWYv/3NgzS8b/UM3jQNh5hYyw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.25.10':
    resolution: {integrity: sha512-XkA4frq1TLj4bEMB+2HnI0+4RnjbuGZfet2gs/LNs5Hc7D89ZQBHQ0gL2ND6Lzu1+QVkjp3x1gIcPKzRNP8bXw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [openbsd]

  '@esbuild/openharmony-arm64@0.25.10':
    resolution: {integrity: sha512-AVTSBhTX8Y/Fz6OmIVBip9tJzZEUcY8WLh7I59+upa5/GPhh2/aM6bvOMQySspnCCHvFi79kMtdJS1w0DXAeag==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openharmony]

  '@esbuild/sunos-x64@0.25.10':
    resolution: {integrity: sha512-fswk3XT0Uf2pGJmOpDB7yknqhVkJQkAQOcW/ccVOtfx05LkbWOaRAtn5SaqXypeKQra1QaEa841PgrSL9ubSPQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [sunos]

  '@esbuild/win32-arm64@0.25.10':
    resolution: {integrity: sha512-ah+9b59KDTSfpaCg6VdJoOQvKjI33nTaQr4UluQwW7aEwZQsbMCfTmfEO4VyewOxx4RaDT/xCy9ra2GPWmO7Kw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [win32]

  '@esbuild/win32-ia32@0.25.10':
    resolution: {integrity: sha512-QHPDbKkrGO8/cz9LKVnJU22HOi4pxZnZhhA2HYHez5Pz4JeffhDjf85E57Oyco163GnzNCVkZK0b/n4Y0UHcSw==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [win32]

  '@esbuild/win32-x64@0.25.10':
    resolution: {integrity: sha512-9KpxSVFCu0iK1owoez6aC/s/EdUQLDN3adTxGCqxMVhrPDj6bt5dbrHDXUuq+Bs2vATFBBrQS5vdQ/Ed2P+nbw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [win32]

  '@eslint-community/eslint-utils@4.9.0':
    resolution: {integrity: sha512-ayVFHdtZ+hsq1t2Dy24wCmGXGe4q9Gu3smhLYALJrr473ZH27MsnSL+LKUlimp4BWJqMDMLmPpx/Q9R3OAlL4g==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      eslint: ^6.0.0 || ^7.0.0 || >=8.0.0

  '@eslint-community/regexpp@4.12.1':
    resolution: {integrity: sha512-CCZCDJuduB9OUkFkY2IgppNZMi2lBQgD2qzwXkEia16cge2pijY/aXi96CJMquDMn3nJdlPV1A5KrJEXwfLNzQ==}
    engines: {node: ^12.0.0 || ^14.0.0 || >=16.0.0}

  '@eslint/compat@1.4.0':
    resolution: {integrity: sha512-DEzm5dKeDBPm3r08Ixli/0cmxr8LkRdwxMRUIJBlSCpAwSrvFEJpVBzV+66JhDxiaqKxnRzCXhtiMiczF7Hglg==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.40 || 9
    peerDependenciesMeta:
      eslint:
        optional: true

  '@eslint/config-array@0.21.0':
    resolution: {integrity: sha512-ENIdc4iLu0d93HeYirvKmrzshzofPw6VkZRKQGe9Nv46ZnWUzcF1xV01dcvEg/1wXUR61OmmlSfyeyO7EvjLxQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/config-helpers@0.4.0':
    resolution: {integrity: sha512-WUFvV4WoIwW8Bv0KeKCIIEgdSiFOsulyN0xrMu+7z43q/hkOLXjvb5u7UC9jDxvRzcrbEmuZBX5yJZz1741jog==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/core@0.16.0':
    resolution: {integrity: sha512-nmC8/totwobIiFcGkDza3GIKfAw1+hLiYVrh3I1nIomQ8PEr5cxg34jnkmGawul/ep52wGRAcyeDCNtWKSOj4Q==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/eslintrc@3.3.1':
    resolution: {integrity: sha512-gtF186CXhIl1p4pJNGZw8Yc6RlshoePRvE0X91oPGb3vZ8pM3qOS9W9NGPat9LziaBV7XrJWGylNQXkGcnM3IQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/js@9.37.0':
    resolution: {integrity: sha512-jaS+NJ+hximswBG6pjNX0uEJZkrT0zwpVi3BA3vX22aFGjJjmgSTSmPpZCRKmoBL5VY/M6p0xsSJx7rk7sy5gg==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/object-schema@2.1.6':
    resolution: {integrity: sha512-RBMg5FRL0I0gs51M/guSAj5/e14VQ4tpZnQNWwuDT66P14I43ItmPfIZRhO9fUVIPOAQXU47atlywZ/czoqFPA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/plugin-kit@0.4.0':
    resolution: {integrity: sha512-sB5uyeq+dwCWyPi31B2gQlVlo+j5brPlWx4yZBrEaRo/nhdDE8Xke1gsGgtiBdaBTxuTkceLVuVt/pclrasb0A==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@hirez_io/observer-spy@2.2.0':
    resolution: {integrity: sha512-G9nv87vjRILgB/X1AtKBv1DZX7yXSYAOCXon/f+QULKoXVhVehYUF5Lv0SQ97ebf1sA48Z2CyQ9h2v4Pz6DgaQ==}
    peerDependencies:
      rxjs: '>=6.0.0'
      typescript: '>=2.8.1'

  '@humanfs/core@0.19.1':
    resolution: {integrity: sha512-5DyQ4+1JEUzejeK1JGICcideyfUbGixgS9jNgex5nqkW+cY7WZhxBigmieN5Qnw9ZosSNVC9KQKyb+GUaGyKUA==}
    engines: {node: '>=18.18.0'}

  '@humanfs/node@0.16.7':
    resolution: {integrity: sha512-/zUx+yOsIrG4Y43Eh2peDeKCxlRt/gET6aHfaKpuq267qXdYDFViVHfMaLyygZOnl0kGWxFIgsBy8QFuTLUXEQ==}
    engines: {node: '>=18.18.0'}

  '@humanwhocodes/module-importer@1.0.1':
    resolution: {integrity: sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==}
    engines: {node: '>=12.22'}

  '@humanwhocodes/retry@0.4.3':
    resolution: {integrity: sha512-bV0Tgo9K4hfPCek+aMAn81RppFKv2ySDQeMoSZuvTASywNTnVJCArCZE2FWqpvIatKu7VMRLWlR1EazvVhDyhQ==}
    engines: {node: '>=18.18'}

  '@isaacs/cliui@8.0.2':
    resolution: {integrity: sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA==}
    engines: {node: '>=12'}

  '@istanbuljs/schema@0.1.3':
    resolution: {integrity: sha512-ZXRY4jNvVgSVQ8DL3LTcakaAtXwTVUxE81hslsyD2AtoXW/wVob10HkOJ1X/pAlcI7D+2YoZKg5do8G/w6RYgA==}
    engines: {node: '>=8'}

  '@jridgewell/gen-mapping@0.3.13':
    resolution: {integrity: sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==}

  '@jridgewell/resolve-uri@3.1.2':
    resolution: {integrity: sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==}
    engines: {node: '>=6.0.0'}

  '@jridgewell/sourcemap-codec@1.5.5':
    resolution: {integrity: sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==}

  '@jridgewell/trace-mapping@0.3.31':
    resolution: {integrity: sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==}

  '@nodelib/fs.scandir@2.1.5':
    resolution: {integrity: sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==}
    engines: {node: '>= 8'}

  '@nodelib/fs.stat@2.0.5':
    resolution: {integrity: sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==}
    engines: {node: '>= 8'}

  '@nodelib/fs.walk@1.2.8':
    resolution: {integrity: sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==}
    engines: {node: '>= 8'}

  '@pkgjs/parseargs@0.11.0':
    resolution: {integrity: sha512-+1VkjdD0QBLPodGrJUeqarH8VAIvQODIbwh9XpP5Syisf7YoQgsJKPNFoqqLQlu+VQ/tVSshMR6loPMn8U+dPg==}
    engines: {node: '>=14'}

  '@pkgr/core@0.2.9':
    resolution: {integrity: sha512-QNqXyfVS2wm9hweSYD2O7F0G06uurj9kZ96TRQE5Y9hU7+tgdZwIkbAKc5Ocy1HxEY2kuDQa6cQ1WRs/O5LFKA==}
    engines: {node: ^12.20.0 || ^14.18.0 || >=16.0.0}

  '@rollup/rollup-android-arm-eabi@4.52.4':
    resolution: {integrity: sha512-BTm2qKNnWIQ5auf4deoetINJm2JzvihvGb9R6K/ETwKLql/Bb3Eg2H1FBp1gUb4YGbydMA3jcmQTR73q7J+GAA==}
    cpu: [arm]
    os: [android]

  '@rollup/rollup-android-arm64@4.52.4':
    resolution: {integrity: sha512-P9LDQiC5vpgGFgz7GSM6dKPCiqR3XYN1WwJKA4/BUVDjHpYsf3iBEmVz62uyq20NGYbiGPR5cNHI7T1HqxNs2w==}
    cpu: [arm64]
    os: [android]

  '@rollup/rollup-darwin-arm64@4.52.4':
    resolution: {integrity: sha512-QRWSW+bVccAvZF6cbNZBJwAehmvG9NwfWHwMy4GbWi/BQIA/laTIktebT2ipVjNncqE6GLPxOok5hsECgAxGZg==}
    cpu: [arm64]
    os: [darwin]

  '@rollup/rollup-darwin-x64@4.52.4':
    resolution: {integrity: sha512-hZgP05pResAkRJxL1b+7yxCnXPGsXU0fG9Yfd6dUaoGk+FhdPKCJ5L1Sumyxn8kvw8Qi5PvQ8ulenUbRjzeCTw==}
    cpu: [x64]
    os: [darwin]

  '@rollup/rollup-freebsd-arm64@4.52.4':
    resolution: {integrity: sha512-xmc30VshuBNUd58Xk4TKAEcRZHaXlV+tCxIXELiE9sQuK3kG8ZFgSPi57UBJt8/ogfhAF5Oz4ZSUBN77weM+mQ==}
    cpu: [arm64]
    os: [freebsd]

  '@rollup/rollup-freebsd-x64@4.52.4':
    resolution: {integrity: sha512-WdSLpZFjOEqNZGmHflxyifolwAiZmDQzuOzIq9L27ButpCVpD7KzTRtEG1I0wMPFyiyUdOO+4t8GvrnBLQSwpw==}
    cpu: [x64]
    os: [freebsd]

  '@rollup/rollup-linux-arm-gnueabihf@4.52.4':
    resolution: {integrity: sha512-xRiOu9Of1FZ4SxVbB0iEDXc4ddIcjCv2aj03dmW8UrZIW7aIQ9jVJdLBIhxBI+MaTnGAKyvMwPwQnoOEvP7FgQ==}
    cpu: [arm]
    os: [linux]

  '@rollup/rollup-linux-arm-musleabihf@4.52.4':
    resolution: {integrity: sha512-FbhM2p9TJAmEIEhIgzR4soUcsW49e9veAQCziwbR+XWB2zqJ12b4i/+hel9yLiD8pLncDH4fKIPIbt5238341Q==}
    cpu: [arm]
    os: [linux]

  '@rollup/rollup-linux-arm64-gnu@4.52.4':
    resolution: {integrity: sha512-4n4gVwhPHR9q/g8lKCyz0yuaD0MvDf7dV4f9tHt0C73Mp8h38UCtSCSE6R9iBlTbXlmA8CjpsZoujhszefqueg==}
    cpu: [arm64]
    os: [linux]

  '@rollup/rollup-linux-arm64-musl@4.52.4':
    resolution: {integrity: sha512-u0n17nGA0nvi/11gcZKsjkLj1QIpAuPFQbR48Subo7SmZJnGxDpspyw2kbpuoQnyK+9pwf3pAoEXerJs/8Mi9g==}
    cpu: [arm64]
    os: [linux]

  '@rollup/rollup-linux-loong64-gnu@4.52.4':
    resolution: {integrity: sha512-0G2c2lpYtbTuXo8KEJkDkClE/+/2AFPdPAbmaHoE870foRFs4pBrDehilMcrSScrN/fB/1HTaWO4bqw+ewBzMQ==}
    cpu: [loong64]
    os: [linux]

  '@rollup/rollup-linux-ppc64-gnu@4.52.4':
    resolution: {integrity: sha512-teSACug1GyZHmPDv14VNbvZFX779UqWTsd7KtTM9JIZRDI5NUwYSIS30kzI8m06gOPB//jtpqlhmraQ68b5X2g==}
    cpu: [ppc64]
    os: [linux]

  '@rollup/rollup-linux-riscv64-gnu@4.52.4':
    resolution: {integrity: sha512-/MOEW3aHjjs1p4Pw1Xk4+3egRevx8Ji9N6HUIA1Ifh8Q+cg9dremvFCUbOX2Zebz80BwJIgCBUemjqhU5XI5Eg==}
    cpu: [riscv64]
    os: [linux]

  '@rollup/rollup-linux-riscv64-musl@4.52.4':
    resolution: {integrity: sha512-1HHmsRyh845QDpEWzOFtMCph5Ts+9+yllCrREuBR/vg2RogAQGGBRC8lDPrPOMnrdOJ+mt1WLMOC2Kao/UwcvA==}
    cpu: [riscv64]
    os: [linux]

  '@rollup/rollup-linux-s390x-gnu@4.52.4':
    resolution: {integrity: sha512-seoeZp4L/6D1MUyjWkOMRU6/iLmCU2EjbMTyAG4oIOs1/I82Y5lTeaxW0KBfkUdHAWN7j25bpkt0rjnOgAcQcA==}
    cpu: [s390x]
    os: [linux]

  '@rollup/rollup-linux-x64-gnu@4.52.4':
    resolution: {integrity: sha512-Wi6AXf0k0L7E2gteNsNHUs7UMwCIhsCTs6+tqQ5GPwVRWMaflqGec4Sd8n6+FNFDw9vGcReqk2KzBDhCa1DLYg==}
    cpu: [x64]
    os: [linux]

  '@rollup/rollup-linux-x64-musl@4.52.4':
    resolution: {integrity: sha512-dtBZYjDmCQ9hW+WgEkaffvRRCKm767wWhxsFW3Lw86VXz/uJRuD438/XvbZT//B96Vs8oTA8Q4A0AfHbrxP9zw==}
    cpu: [x64]
    os: [linux]

  '@rollup/rollup-openharmony-arm64@4.52.4':
    resolution: {integrity: sha512-1ox+GqgRWqaB1RnyZXL8PD6E5f7YyRUJYnCqKpNzxzP0TkaUh112NDrR9Tt+C8rJ4x5G9Mk8PQR3o7Ku2RKqKA==}
    cpu: [arm64]
    os: [openharmony]

  '@rollup/rollup-win32-arm64-msvc@4.52.4':
    resolution: {integrity: sha512-8GKr640PdFNXwzIE0IrkMWUNUomILLkfeHjXBi/nUvFlpZP+FA8BKGKpacjW6OUUHaNI6sUURxR2U2g78FOHWQ==}
    cpu: [arm64]
    os: [win32]

  '@rollup/rollup-win32-ia32-msvc@4.52.4':
    resolution: {integrity: sha512-AIy/jdJ7WtJ/F6EcfOb2GjR9UweO0n43jNObQMb6oGxkYTfLcnN7vYYpG+CN3lLxrQkzWnMOoNSHTW54pgbVxw==}
    cpu: [ia32]
    os: [win32]

  '@rollup/rollup-win32-x64-gnu@4.52.4':
    resolution: {integrity: sha512-UF9KfsH9yEam0UjTwAgdK0anlQ7c8/pWPU2yVjyWcF1I1thABt6WXE47cI71pGiZ8wGvxohBoLnxM04L/wj8mQ==}
    cpu: [x64]
    os: [win32]

  '@rollup/rollup-win32-x64-msvc@4.52.4':
    resolution: {integrity: sha512-bf9PtUa0u8IXDVxzRToFQKsNCRz9qLYfR/MpECxl4mRoWYjAeFjgxj1XdZr2M/GNVpT05p+LgQOHopYDlUu6/w==}
    cpu: [x64]
    os: [win32]

  '@types/chai@5.2.2':
    resolution: {integrity: sha512-8kB30R7Hwqf40JPiKhVzodJs2Qc1ZJ5zuT3uzw5Hq/dhNCl3G3l83jfpdI1e20BP348+fV7VIL/+FxaXkqBmWg==}

  '@types/debug@4.1.12':
    resolution: {integrity: sha512-vIChWdVG3LG1SMxEvI/AK+FWJthlrqlTu7fbrlywTkkaONwk/UAGaULXRlf8vkzFBLVm0zkMdCquhL5aOjhXPQ==}

  '@types/deep-eql@4.0.2':
    resolution: {integrity: sha512-c9h9dVVMigMPc4bwTvC5dxqtqJZwQPePsWjPlpSOnojbor6pGqdk541lfA7AqFQr5pB1BRdq0juY9db81BwyFw==}

  '@types/estree@1.0.8':
    resolution: {integrity: sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w==}

  '@types/json-schema@7.0.15':
    resolution: {integrity: sha512-5+fP8P8MFNC+AyZCDxrB2pkZFPGzqQWUzpSeuuVLvm8VMcorNYavBqoFcxK8bQz4Qsbn4oUEEem4wDLfcysGHA==}

  '@types/ms@2.1.0':
    resolution: {integrity: sha512-GsCCIZDE/p3i96vtEqx+7dBUGXrc7zeSK3wwPHIaRThS+9OhWIXRqzs4d6k1SVU8g91DrNRWxWUGhp5KXQb2VA==}

  '@types/node@20.19.20':
    resolution: {integrity: sha512-2Q7WS25j4pS1cS8yw3d6buNCVJukOTeQ39bAnwR6sOJbaxvyCGebzTMypDFN82CxBLnl+lSWVdCCWbRY6y9yZQ==}

  '@types/shell-quote@1.7.5':
    resolution: {integrity: sha512-+UE8GAGRPbJVQDdxi16dgadcBfQ+KG2vgZhV1+3A1XmHbmwcdwhCUwIdy+d3pAGrbvgRoVSjeI9vOWyq376Yzw==}

  '@types/yargs-parser@21.0.3':
    resolution: {integrity: sha512-I4q9QU9MQv4oEOz4tAHJtNz1cwuLxn2F3xcc2iV5WdqLPpUnj30aUuxt1mAxYTG+oe8CZMV/+6rU4S4gRDzqtQ==}

  '@types/yargs@17.0.33':
    resolution: {integrity: sha512-WpxBCKWPLr4xSsHgz511rFJAM+wS28w2zEO1QDNY5zM/S8ok70NNfztH0xwhqKyaK0OHCbN98LDAZuy1ctxDkA==}

  '@typescript-eslint/eslint-plugin@8.46.0':
    resolution: {integrity: sha512-hA8gxBq4ukonVXPy0OKhiaUh/68D0E88GSmtC1iAEnGaieuDi38LhS7jdCHRLi6ErJBNDGCzvh5EnzdPwUc0DA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      '@typescript-eslint/parser': ^8.46.0
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <6.0.0'

  '@typescript-eslint/parser@8.46.0':
    resolution: {integrity: sha512-n1H6IcDhmmUEG7TNVSspGmiHHutt7iVKtZwRppD7e04wha5MrkV1h3pti9xQLcCMt6YWsncpoT0HMjkH1FNwWQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <6.0.0'

  '@typescript-eslint/project-service@8.46.0':
    resolution: {integrity: sha512-OEhec0mH+U5Je2NZOeK1AbVCdm0ChyapAyTeXVIYTPXDJ3F07+cu87PPXcGoYqZ7M9YJVvFnfpGg1UmCIqM+QQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      typescript: '>=4.8.4 <6.0.0'

  '@typescript-eslint/scope-manager@8.46.0':
    resolution: {integrity: sha512-lWETPa9XGcBes4jqAMYD9fW0j4n6hrPtTJwWDmtqgFO/4HF4jmdH/Q6wggTw5qIT5TXjKzbt7GsZUBnWoO3dqw==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@typescript-eslint/tsconfig-utils@8.46.0':
    resolution: {integrity: sha512-WrYXKGAHY836/N7zoK/kzi6p8tXFhasHh8ocFL9VZSAkvH956gfeRfcnhs3xzRy8qQ/dq3q44v1jvQieMFg2cw==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      typescript: '>=4.8.4 <6.0.0'

  '@typescript-eslint/type-utils@8.46.0':
    resolution: {integrity: sha512-hy+lvYV1lZpVs2jRaEYvgCblZxUoJiPyCemwbQZ+NGulWkQRy0HRPYAoef/CNSzaLt+MLvMptZsHXHlkEilaeg==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <6.0.0'

  '@typescript-eslint/types@8.46.0':
    resolution: {integrity: sha512-bHGGJyVjSE4dJJIO5yyEWt/cHyNwga/zXGJbJJ8TiO01aVREK6gCTu3L+5wrkb1FbDkQ+TKjMNe9R/QQQP9+rA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@typescript-eslint/typescript-estree@8.46.0':
    resolution: {integrity: sha512-ekDCUfVpAKWJbRfm8T1YRrCot1KFxZn21oV76v5Fj4tr7ELyk84OS+ouvYdcDAwZL89WpEkEj2DKQ+qg//+ucg==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      typescript: '>=4.8.4 <6.0.0'

  '@typescript-eslint/utils@8.46.0':
    resolution: {integrity: sha512-nD6yGWPj1xiOm4Gk0k6hLSZz2XkNXhuYmyIrOWcHoPuAhjT9i5bAG+xbWPgFeNR8HPHHtpNKdYUXJl/D3x7f5g==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <6.0.0'

  '@typescript-eslint/visitor-keys@8.46.0':
    resolution: {integrity: sha512-FrvMpAK+hTbFy7vH5j1+tMYHMSKLE6RzluFJlkFNKD0p9YsUT75JlBSmr5so3QRzvMwU5/bIEdeNrxm8du8l3Q==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@vitest/coverage-v8@3.2.4':
    resolution: {integrity: sha512-EyF9SXU6kS5Ku/U82E259WSnvg6c8KTjppUncuNdm5QHpe17mwREHnjDzozC8x9MZ0xfBUFSaLkRv4TMA75ALQ==}
    peerDependencies:
      '@vitest/browser': 3.2.4
      vitest: 3.2.4
    peerDependenciesMeta:
      '@vitest/browser':
        optional: true

  '@vitest/eslint-plugin@1.3.16':
    resolution: {integrity: sha512-EvXGiZpz3L1G/pmebcmMe61UzqgR8LFwmm+QGgQEHcrTCFkMgl+c0mj2jneo38/CkHhofbK3zc3xafV6/SpzNw==}
    peerDependencies:
      eslint: '>= 8.57.0'
      typescript: '>= 5.0.0'
      vitest: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
      vitest:
        optional: true

  '@vitest/expect@3.2.4':
    resolution: {integrity: sha512-Io0yyORnB6sikFlt8QW5K7slY4OjqNX9jmJQ02QDda8lyM6B5oNgVWoSoKPac8/kgnCUzuHQKrSLtu/uOqqrig==}

  '@vitest/mocker@3.2.4':
    resolution: {integrity: sha512-46ryTE9RZO/rfDd7pEqFl7etuyzekzEhUbTW3BvmeO/BcCMEgq59BKhek3dXDWgAj4oMK6OZi+vRr1wPW6qjEQ==}
    peerDependencies:
      msw: ^2.4.9
      vite: ^5.0.0 || ^6.0.0 || ^7.0.0-0
    peerDependenciesMeta:
      msw:
        optional: true
      vite:
        optional: true

  '@vitest/pretty-format@3.2.4':
    resolution: {integrity: sha512-IVNZik8IVRJRTr9fxlitMKeJeXFFFN0JaB9PHPGQ8NKQbGpfjlTx9zO4RefN8gp7eqjNy8nyK3NZmBzOPeIxtA==}

  '@vitest/runner@3.2.4':
    resolution: {integrity: sha512-oukfKT9Mk41LreEW09vt45f8wx7DordoWUZMYdY/cyAk7w5TWkTRCNZYF7sX7n2wB7jyGAl74OxgwhPgKaqDMQ==}

  '@vitest/snapshot@3.2.4':
    resolution: {integrity: sha512-dEYtS7qQP2CjU27QBC5oUOxLE/v5eLkGqPE0ZKEIDGMs4vKWe7IjgLOeauHsR0D5YuuycGRO5oSRXnwnmA78fQ==}

  '@vitest/spy@3.2.4':
    resolution: {integrity: sha512-vAfasCOe6AIK70iP5UD11Ac4siNUNJ9i/9PZ3NKx07sG6sUxeag1LWdNrMWeKKYBLlzuK+Gn65Yd5nyL6ds+nw==}

  '@vitest/utils@3.2.4':
    resolution: {integrity: sha512-fB2V0JFrQSMsCo9HiSq3Ezpdv4iYaXRG1Sx8edX3MwxfyNn83mKiGzOcH+Fkxt4MHxr3y42fQi1oeAInqgX2QA==}

  acorn-jsx@5.3.2:
    resolution: {integrity: sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==}
    peerDependencies:
      acorn: ^6.0.0 || ^7.0.0 || ^8.0.0

  acorn@8.15.0:
    resolution: {integrity: sha512-NZyJarBfL7nWwIq+FDL6Zp/yHEhePMNnnJ0y3qfieCrmNvYct8uvtiV41UvlSe6apAfk0fY1FbWx+NwfmpvtTg==}
    engines: {node: '>=0.4.0'}
    hasBin: true

  ajv@6.12.6:
    resolution: {integrity: sha512-j3fVLgvTo527anyYyJOGTYJbG+vnnQYvE0m5mmkc1TK+nxAppkCLMIL0aZ4dblVCNoGShhm+kzE4ZUykBoMg4g==}

  ansi-escapes@7.1.1:
    resolution: {integrity: sha512-Zhl0ErHcSRUaVfGUeUdDuLgpkEo8KIFjB4Y9uAc46ScOpdDiU1Dbyplh7qWJeJ/ZHpbyMSM26+X3BySgnIz40Q==}
    engines: {node: '>=18'}

  ansi-regex@5.0.1:
    resolution: {integrity: sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==}
    engines: {node: '>=8'}

  ansi-regex@6.2.2:
    resolution: {integrity: sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg==}
    engines: {node: '>=12'}

  ansi-styles@4.3.0:
    resolution: {integrity: sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==}
    engines: {node: '>=8'}

  ansi-styles@6.2.3:
    resolution: {integrity: sha512-4Dj6M28JB+oAH8kFkTLUo+a2jwOFkuqb3yucU0CANcRRUbxS0cP0nZYCGjcc3BNXwRIsUVmDGgzawme7zvJHvg==}
    engines: {node: '>=12'}

  argparse@2.0.1:
    resolution: {integrity: sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==}

  assertion-error@2.0.1:
    resolution: {integrity: sha512-Izi8RQcffqCeNVgFigKli1ssklIbpHnCYc6AknXGYoB6grJqyeby7jv12JUQgmTAnIDnbck1uxksT4dzN3PWBA==}
    engines: {node: '>=12'}

  ast-v8-to-istanbul@0.3.5:
    resolution: {integrity: sha512-9SdXjNheSiE8bALAQCQQuT6fgQaoxJh7IRYrRGZ8/9nv8WhJeC1aXAwN8TbaOssGOukUvyvnkgD9+Yuykvl1aA==}

  balanced-match@1.0.2:
    resolution: {integrity: sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==}

  brace-expansion@1.1.12:
    resolution: {integrity: sha512-9T9UjW3r0UW5c1Q7GTwllptXwhvYmEzFhzMfZ9H7FQWt+uZePjZPjBP/W1ZEyZ1twGWom5/56TF4lPcqjnDHcg==}

  brace-expansion@2.0.2:
    resolution: {integrity: sha512-Jt0vHyM+jmUBqojB7E1NIYadt0vI0Qxjxd2TErW94wDz+E2LAm5vKMXXwg6ZZBTHPuUlDgQHKXvjGBdfcF1ZDQ==}

  braces@3.0.3:
    resolution: {integrity: sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==}
    engines: {node: '>=8'}

  cac@6.7.14:
    resolution: {integrity: sha512-b6Ilus+c3RrdDk+JhLKUAQfzzgLEPy6wcXqS7f/xe1EETvsDP6GORG7SFuOs6cID5YkqchW/LXZbX5bc8j7ZcQ==}
    engines: {node: '>=8'}

  callsites@3.1.0:
    resolution: {integrity: sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==}
    engines: {node: '>=6'}

  chai@5.3.3:
    resolution: {integrity: sha512-4zNhdJD/iOjSH0A05ea+Ke6MU5mmpQcbQsSOkgdaUMJ9zTlDTD/GYlwohmIE2u0gaxHYiVHEn1Fw9mZ/ktJWgw==}
    engines: {node: '>=18'}

  chalk@4.1.2:
    resolution: {integrity: sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==}
    engines: {node: '>=10'}

  chalk@5.6.2:
    resolution: {integrity: sha512-7NzBL0rN6fMUW+f7A6Io4h40qQlG+xGmtMxfbnH/K7TAtt8JQWVQK+6g0UXKMeVJoyV5EkkNsErQ8pVD3bLHbA==}
    engines: {node: ^12.17.0 || ^14.13 || >=16.0.0}

  check-error@2.1.1:
    resolution: {integrity: sha512-OAlb+T7V4Op9OwdkjmguYRqncdlx5JiofwOAUkmTF+jNdHwzTaTs4sRAGpzLF3oOz5xAyDGrPgeIDFQmDOTiJw==}
    engines: {node: '>= 16'}

  cli-cursor@5.0.0:
    resolution: {integrity: sha512-aCj4O5wKyszjMmDT4tZj93kxyydN/K5zPWSCe6/0AV/AA1pqe5ZBIw0a2ZfPQV7lL5/yb5HsUreJ6UFAF1tEQw==}
    engines: {node: '>=18'}

  cli-truncate@5.1.0:
    resolution: {integrity: sha512-7JDGG+4Zp0CsknDCedl0DYdaeOhc46QNpXi3NLQblkZpXXgA6LncLDUUyvrjSvZeF3VRQa+KiMGomazQrC1V8g==}
    engines: {node: '>=20'}

  cliui@8.0.1:
    resolution: {integrity: sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==}
    engines: {node: '>=12'}

  color-convert@2.0.1:
    resolution: {integrity: sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==}
    engines: {node: '>=7.0.0'}

  color-name@1.1.4:
    resolution: {integrity: sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==}

  colorette@2.0.20:
    resolution: {integrity: sha512-IfEDxwoWIjkeXL1eXcDiow4UbKjhLdq6/EuSVR9GMN7KVH3r9gQ83e73hsz1Nd1T3ijd5xv1wcWRYO+D6kCI2w==}

  commander@14.0.1:
    resolution: {integrity: sha512-2JkV3gUZUVrbNA+1sjBOYLsMZ5cEEl8GTFP2a4AVz5hvasAMCQ1D2l2le/cX+pV4N6ZU17zjUahLpIXRrnWL8A==}
    engines: {node: '>=20'}

  concat-map@0.0.1:
    resolution: {integrity: sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==}

  cross-spawn@7.0.6:
    resolution: {integrity: sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==}
    engines: {node: '>= 8'}

  ctrlc-wrapper-windows-32@0.0.3:
    resolution: {integrity: sha512-7bFhhEo2AnFUYGKIL6d89r+6P1mGUMgBDlpyTWyreVajHshbTvWj68gQirS6AKTD8NWrStUZih0zLuBC3XO+Ow==}
    engines: {node: '>=12'}
    cpu: [ia32]
    os: [win32]

  ctrlc-wrapper-windows-64@0.0.3:
    resolution: {integrity: sha512-5Rp9bfzKFA9D8qIchrMjcPoThv/RavJm/RHuk93FtHj7nUs+CJUxO6UZR7AJCtl0HFXuMsjxU8wuR9jKgBzqlw==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [win32]

  ctrlc-wrapper@0.0.5:
    resolution: {integrity: sha512-j2drGd+TgAnIRmxISKrxUsMQo7l1hXJ5f000qHUMtQxw9qmDkL35XZtQqHqG609nNJoWPxx5jJAXyWwQpBMLow==}

  debug@4.4.3:
    resolution: {integrity: sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==}
    engines: {node: '>=6.0'}
    peerDependencies:
      supports-color: '*'
    peerDependenciesMeta:
      supports-color:
        optional: true

  deep-eql@5.0.2:
    resolution: {integrity: sha512-h5k/5U50IJJFpzfL6nO9jaaumfjO/f2NjK/oYB2Djzm4p9L+3T9qWpZqZ2hAbLPuuYq9wrU08WQyBTL5GbPk5Q==}
    engines: {node: '>=6'}

  deep-is@0.1.4:
    resolution: {integrity: sha512-oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==}

  eastasianwidth@0.2.0:
    resolution: {integrity: sha512-I88TYZWc9XiYHRQ4/3c5rjjfgkjhLyW2luGIheGERbNQ6OY7yTybanSpDXZa8y7VUP9YmDcYa+eyq4ca7iLqWA==}

  emoji-regex@10.5.0:
    resolution: {integrity: sha512-lb49vf1Xzfx080OKA0o6l8DQQpV+6Vg95zyCJX9VB/BqKYlhG7N4wgROUUHRA+ZPUefLnteQOad7z1kT2bV7bg==}

  emoji-regex@8.0.0:
    resolution: {integrity: sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==}

  emoji-regex@9.2.2:
    resolution: {integrity: sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==}

  environment@1.1.0:
    resolution: {integrity: sha512-xUtoPkMggbz0MPyPiIWr1Kp4aeWJjDZ6SMvURhimjdZgsRuDplF5/s9hcgGhyXMhs+6vpnuoiZ2kFiu3FMnS8Q==}
    engines: {node: '>=18'}

  es-module-lexer@1.7.0:
    resolution: {integrity: sha512-jEQoCwk8hyb2AZziIOLhDqpm5+2ww5uIE6lkO/6jcOCusfk6LhMHpXXfBLXTZ7Ydyt0j4VoUQv6uGNYbdW+kBA==}

  esbuild@0.25.10:
    resolution: {integrity: sha512-9RiGKvCwaqxO2owP61uQ4BgNborAQskMR6QusfWzQqv7AZOg5oGehdY2pRJMTKuwxd1IDBP4rSbI5lHzU7SMsQ==}
    engines: {node: '>=18'}
    hasBin: true

  escalade@3.2.0:
    resolution: {integrity: sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==}
    engines: {node: '>=6'}

  escape-string-regexp@4.0.0:
    resolution: {integrity: sha512-TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==}
    engines: {node: '>=10'}

  eslint-config-flat-gitignore@2.1.0:
    resolution: {integrity: sha512-cJzNJ7L+psWp5mXM7jBX+fjHtBvvh06RBlcweMhKD8jWqQw0G78hOW5tpVALGHGFPsBV+ot2H+pdDGJy6CV8pA==}
    peerDependencies:
      eslint: ^9.5.0

  eslint-config-prettier@10.1.8:
    resolution: {integrity: sha512-82GZUjRS0p/jganf6q1rEO25VSoHH0hKPCTrgillPjdI/3bgBhAE1QzHrHTizjpRvy6pGAvKjDJtk2pF9NDq8w==}
    hasBin: true
    peerDependencies:
      eslint: '>=7.0.0'

  eslint-plugin-import-lite@0.3.0:
    resolution: {integrity: sha512-dkNBAL6jcoCsXZsQ/Tt2yXmMDoNt5NaBh/U7yvccjiK8cai6Ay+MK77bMykmqQA2bTF6lngaLCDij6MTO3KkvA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: '>=9.0.0'
      typescript: '>=4.5'
    peerDependenciesMeta:
      typescript:
        optional: true

  eslint-plugin-prettier@5.5.4:
    resolution: {integrity: sha512-swNtI95SToIz05YINMA6Ox5R057IMAmWZ26GqPxusAp1TZzj+IdY9tXNWWD3vkF/wEqydCONcwjTFpxybBqZsg==}
    engines: {node: ^14.18.0 || >=16.0.0}
    peerDependencies:
      '@types/eslint': '>=8.0.0'
      eslint: '>=8.0.0'
      eslint-config-prettier: '>= 7.0.0 <10.0.0 || >=10.1.0'
      prettier: '>=3.0.0'
    peerDependenciesMeta:
      '@types/eslint':
        optional: true
      eslint-config-prettier:
        optional: true

  eslint-plugin-simple-import-sort@12.1.1:
    resolution: {integrity: sha512-6nuzu4xwQtE3332Uz0to+TxDQYRLTKRESSc2hefVT48Zc8JthmN23Gx9lnYhu0FtkRSL1oxny3kJ2aveVhmOVA==}
    peerDependencies:
      eslint: '>=5.0.0'

  eslint-scope@8.4.0:
    resolution: {integrity: sha512-sNXOfKCn74rt8RICKMvJS7XKV/Xk9kA7DyJr8mJik3S7Cwgy3qlkkmyS2uQB3jiJg6VNdZd/pDBJu0nvG2NlTg==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  eslint-visitor-keys@3.4.3:
    resolution: {integrity: sha512-wpc+LXeiyiisxPlEkUzU6svyS1frIO3Mgxj1fdy7Pm8Ygzguax2N3Fa/D/ag1WqbOprdI+uY6wMUl8/a2G+iag==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}

  eslint-visitor-keys@4.2.1:
    resolution: {integrity: sha512-Uhdk5sfqcee/9H/rCOJikYz67o0a2Tw2hGRPOG2Y1R2dg7brRe1uG0yaNQDHu+TO/uQPF/5eCapvYSmHUjt7JQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  eslint@9.37.0:
    resolution: {integrity: sha512-XyLmROnACWqSxiGYArdef1fItQd47weqB7iwtfr9JHwRrqIXZdcFMvvEcL9xHCmL0SNsOvF0c42lWyM1U5dgig==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    hasBin: true
    peerDependencies:
      jiti: '*'
    peerDependenciesMeta:
      jiti:
        optional: true

  espree@10.4.0:
    resolution: {integrity: sha512-j6PAQ2uUr79PZhBjP5C5fhl8e39FmRnOjsD5lGnWrFU8i2G776tBK7+nP8KuQUTTyAZUwfQqXAgrVH5MbH9CYQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  esquery@1.6.0:
    resolution: {integrity: sha512-ca9pw9fomFcKPvFLXhBKUK90ZvGibiGOvRJNbjljY7s7uq/5YO4BOzcYtJqExdx99rF6aAcnRxHmcUHcz6sQsg==}
    engines: {node: '>=0.10'}

  esrecurse@4.3.0:
    resolution: {integrity: sha512-KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==}
    engines: {node: '>=4.0'}

  estraverse@5.3.0:
    resolution: {integrity: sha512-MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==}
    engines: {node: '>=4.0'}

  estree-walker@3.0.3:
    resolution: {integrity: sha512-7RUKfXgSMMkzt6ZuXmqapOurLGPPfgj6l9uRZ7lRGolvk0y2yocc35LdcxKC5PQZdn2DMqioAQ2NoWcrTKmm6g==}

  esutils@2.0.3:
    resolution: {integrity: sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==}
    engines: {node: '>=0.10.0'}

  eventemitter3@5.0.1:
    resolution: {integrity: sha512-GWkBvjiSZK87ELrYOSESUYeVIc9mvLLf/nXalMOS5dYrgZq9o5OVkbZAVM06CVxYsCwH9BDZFPlQTlPA1j4ahA==}

  expect-type@1.2.2:
    resolution: {integrity: sha512-JhFGDVJ7tmDJItKhYgJCGLOWjuK9vPxiXoUFLwLDc99NlmklilbiQJwoctZtt13+xMw91MCk/REan6MWHqDjyA==}
    engines: {node: '>=12.0.0'}

  fast-deep-equal@3.1.3:
    resolution: {integrity: sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==}

  fast-diff@1.3.0:
    resolution: {integrity: sha512-VxPP4NqbUjj6MaAOafWeUn2cXWLcCtljklUtZf0Ind4XQ+QPtmA0b18zZy0jIQx+ExRVCR/ZQpBmik5lXshNsw==}

  fast-glob@3.3.3:
    resolution: {integrity: sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==}
    engines: {node: '>=8.6.0'}

  fast-json-stable-stringify@2.1.0:
    resolution: {integrity: sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==}

  fast-levenshtein@2.0.6:
    resolution: {integrity: sha512-DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==}

  fastq@1.19.1:
    resolution: {integrity: sha512-GwLTyxkCXjXbxqIhTsMI2Nui8huMPtnxg7krajPJAjnEG/iiOS7i+zCtWGZR9G0NBKbXKh6X9m9UIsYX/N6vvQ==}

  fdir@6.5.0:
    resolution: {integrity: sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==}
    engines: {node: '>=12.0.0'}
    peerDependencies:
      picomatch: ^3 || ^4
    peerDependenciesMeta:
      picomatch:
        optional: true

  file-entry-cache@8.0.0:
    resolution: {integrity: sha512-XXTUwCvisa5oacNGRP9SfNtYBNAMi+RPwBFmblZEF7N7swHYQS6/Zfk7SRwx4D5j3CH211YNRco1DEMNVfZCnQ==}
    engines: {node: '>=16.0.0'}

  fill-range@7.1.1:
    resolution: {integrity: sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==}
    engines: {node: '>=8'}

  find-up@5.0.0:
    resolution: {integrity: sha512-78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==}
    engines: {node: '>=10'}

  flat-cache@4.0.1:
    resolution: {integrity: sha512-f7ccFPK3SXFHpx15UIGyRJ/FJQctuKZ0zVuN3frBo4HnK3cay9VEW0R6yPYFHC0AgqhukPzKjq22t5DmAyqGyw==}
    engines: {node: '>=16'}

  flatted@3.3.3:
    resolution: {integrity: sha512-GX+ysw4PBCz0PzosHDepZGANEuFCMLrnRTiEy9McGjmkCQYwRq4A/X786G/fjM/+OjsWSU1ZrY5qyARZmO/uwg==}

  foreground-child@3.3.1:
    resolution: {integrity: sha512-gIXjKqtFuWEgzFRJA9WCQeSJLZDjgJUOMCMzxtvFq/37KojM1BFGufqsCy0r4qSQmYLsZYMeyRqzIWOMup03sw==}
    engines: {node: '>=14'}

  fsevents@2.3.3:
    resolution: {integrity: sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==}
    engines: {node: ^8.16.0 || ^10.6.0 || >=11.0.0}
    os: [darwin]

  get-caller-file@2.0.5:
    resolution: {integrity: sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==}
    engines: {node: 6.* || 8.* || >= 10.*}

  get-east-asian-width@1.4.0:
    resolution: {integrity: sha512-QZjmEOC+IT1uk6Rx0sX22V6uHWVwbdbxf1faPqJ1QhLdGgsRGCZoyaQBm/piRdJy/D2um6hM1UP7ZEeQ4EkP+Q==}
    engines: {node: '>=18'}

  glob-parent@5.1.2:
    resolution: {integrity: sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==}
    engines: {node: '>= 6'}

  glob-parent@6.0.2:
    resolution: {integrity: sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==}
    engines: {node: '>=10.13.0'}

  glob@10.4.5:
    resolution: {integrity: sha512-7Bv8RF0k6xjo7d4A/PxYLbUCfb6c+Vpd2/mB2yRDlew7Jb5hEXiCD9ibfO7wpk8i4sevK6DFny9h7EYbM3/sHg==}
    hasBin: true

  globals@14.0.0:
    resolution: {integrity: sha512-oahGvuMGQlPw/ivIYBjVSrWAfWLBeku5tpPE2fOPLi+WHffIWbuh2tCjhyQhTBPMf5E9jDEH4FOmTYgYwbKwtQ==}
    engines: {node: '>=18'}

  globals@16.4.0:
    resolution: {integrity: sha512-ob/2LcVVaVGCYN+r14cnwnoDPUufjiYgSqRhiFD0Q1iI4Odora5RE8Iv1D24hAz5oMophRGkGz+yuvQmmUMnMw==}
    engines: {node: '>=18'}

  graphemer@1.4.0:
    resolution: {integrity: sha512-EtKwoO6kxCL9WO5xipiHTZlSzBm7WLT627TqC/uVRd0HKmq8NXyebnNYxDoBi7wt8eTWrUrKXCOVaFq9x1kgag==}

  has-flag@4.0.0:
    resolution: {integrity: sha512-EykJT/Q1KjTWctppgIAgfSO0tKVuZUjhgMr17kqTumMl6Afv3EISleU7qZUzoXDFTAHTDC4NOoG/ZxU3EvlMPQ==}
    engines: {node: '>=8'}

  html-escaper@2.0.2:
    resolution: {integrity: sha512-H2iMtd0I4Mt5eYiapRdIDjp+XzelXQ0tFE4JS7YFwFevXXMmOp9myNrUvCg0D6ws8iqkRPBfKHgbwig1SmlLfg==}

  husky@9.1.7:
    resolution: {integrity: sha512-5gs5ytaNjBrh5Ow3zrvdUUY+0VxIuWVL4i9irt6friV+BqdCfmV11CQTWMiBYWHbXhco+J1kHfTOUkePhCDvMA==}
    engines: {node: '>=18'}
    hasBin: true

  ignore@5.3.2:
    resolution: {integrity: sha512-hsBTNUqQTDwkWtcdYI2i06Y/nUBEsNEDJKjWdigLvegy8kDuJAS8uRlpkkcQpyEXL0Z/pjDy5HBmMjRCJ2gq+g==}
    engines: {node: '>= 4'}

  ignore@7.0.5:
    resolution: {integrity: sha512-Hs59xBNfUIunMFgWAbGX5cq6893IbWg4KnrjbYwX3tx0ztorVgTDA6B2sxf8ejHJ4wz8BqGUMYlnzNBer5NvGg==}
    engines: {node: '>= 4'}

  import-fresh@3.3.1:
    resolution: {integrity: sha512-TR3KfrTZTYLPB6jUjfx6MF9WcWrHL9su5TObK4ZkYgBdWKPOFoSoQIdEuTuR82pmtxH2spWG9h6etwfr1pLBqQ==}
    engines: {node: '>=6'}

  imurmurhash@0.1.4:
    resolution: {integrity: sha512-JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==}
    engines: {node: '>=0.8.19'}

  in-publish@2.0.1:
    resolution: {integrity: sha512-oDM0kUSNFC31ShNxHKUyfZKy8ZeXZBWMjMdZHKLOk13uvT27VTL/QzRGfRUcevJhpkZAvlhPYuXkF7eNWrtyxQ==}
    hasBin: true

  is-extglob@2.1.1:
    resolution: {integrity: sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==}
    engines: {node: '>=0.10.0'}

  is-fullwidth-code-point@3.0.0:
    resolution: {integrity: sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==}
    engines: {node: '>=8'}

  is-fullwidth-code-point@5.1.0:
    resolution: {integrity: sha512-5XHYaSyiqADb4RnZ1Bdad6cPp8Toise4TzEjcOYDHZkTCbKgiUl7WTUCpNWHuxmDt91wnsZBc9xinNzopv3JMQ==}
    engines: {node: '>=18'}

  is-glob@4.0.3:
    resolution: {integrity: sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==}
    engines: {node: '>=0.10.0'}

  is-number@7.0.0:
    resolution: {integrity: sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==}
    engines: {node: '>=0.12.0'}

  isexe@2.0.0:
    resolution: {integrity: sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==}

  istanbul-lib-coverage@3.2.2:
    resolution: {integrity: sha512-O8dpsF+r0WV/8MNRKfnmrtCWhuKjxrq2w+jpzBL5UZKTi2LeVWnWOmWRxFlesJONmc+wLAGvKQZEOanko0LFTg==}
    engines: {node: '>=8'}

  istanbul-lib-report@3.0.1:
    resolution: {integrity: sha512-GCfE1mtsHGOELCU8e/Z7YWzpmybrx/+dSTfLrvY8qRmaY6zXTKWn6WQIjaAFw069icm6GVMNkgu0NzI4iPZUNw==}
    engines: {node: '>=10'}

  istanbul-lib-source-maps@5.0.6:
    resolution: {integrity: sha512-yg2d+Em4KizZC5niWhQaIomgf5WlL4vOOjZ5xGCmF8SnPE/mDWWXgvRExdcpCgh9lLRRa1/fSYp2ymmbJ1pI+A==}
    engines: {node: '>=10'}

  istanbul-reports@3.2.0:
    resolution: {integrity: sha512-HGYWWS/ehqTV3xN10i23tkPkpH46MLCIMFNCaaKNavAXTF1RkqxawEPtnjnGZ6XKSInBKkiOA5BKS+aZiY3AvA==}
    engines: {node: '>=8'}

  jackspeak@3.4.3:
    resolution: {integrity: sha512-OGlZQpz2yfahA/Rd1Y8Cd9SIEsqvXkLVoSw/cgwhnhFMDbsQFeZYoJJ7bIZBS9BcamUW96asq/npPWugM+RQBw==}

  js-tokens@9.0.1:
    resolution: {integrity: sha512-mxa9E9ITFOt0ban3j6L5MpjwegGz6lBQmM1IJkWeBZGcMxto50+eWdjC/52xDbS2vy0k7vIMK0Fe2wfL9OQSpQ==}

  js-yaml@4.1.0:
    resolution: {integrity: sha512-wpxZs9NoxZaJESJGIZTyDEaYpl0FKSA+FB9aJiyemKhMwkxQg63h4T1KJgUGHpTqPDNRcmmYLugrRjJlBtWvRA==}
    hasBin: true

  json-buffer@3.0.1:
    resolution: {integrity: sha512-4bV5BfR2mqfQTJm+V5tPPdf+ZpuhiIvTuAB5g8kcrXOZpTT/QwwVRWBywX1ozr6lEuPdbHxwaJlm9G6mI2sfSQ==}

  json-schema-traverse@0.4.1:
    resolution: {integrity: sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==}

  json-stable-stringify-without-jsonify@1.0.1:
    resolution: {integrity: sha512-Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==}

  keyv@4.5.4:
    resolution: {integrity: sha512-oxVHkHR/EJf2CNXnWxRLW6mg7JyCCUcG0DtEGmL2ctUo1PNTin1PUil+r/+4r5MpVgC/fn1kjsx7mjSujKqIpw==}

  levn@0.4.1:
    resolution: {integrity: sha512-+bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==}
    engines: {node: '>= 0.8.0'}

  lint-staged@16.2.3:
    resolution: {integrity: sha512-1OnJEESB9zZqsp61XHH2fvpS1es3hRCxMplF/AJUDa8Ho8VrscYDIuxGrj3m8KPXbcWZ8fT9XTMUhEQmOVKpKw==}
    engines: {node: '>=20.17'}
    hasBin: true

  listr2@9.0.4:
    resolution: {integrity: sha512-1wd/kpAdKRLwv7/3OKC8zZ5U8e/fajCfWMxacUvB79S5nLrYGPtUI/8chMQhn3LQjsRVErTb9i1ECAwW0ZIHnQ==}
    engines: {node: '>=20.0.0'}

  locate-path@6.0.0:
    resolution: {integrity: sha512-iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==}
    engines: {node: '>=10'}

  lodash.merge@4.6.2:
    resolution: {integrity: sha512-0KpjqXRVvrYyCsX1swR/XTK0va6VQkQM6MNo7PqW77ByjAhoARA8EfrP1N4+KlKj8YS0ZUCtRT/YUuhyYDujIQ==}

  log-update@6.1.0:
    resolution: {integrity: sha512-9ie8ItPR6tjY5uYJh8K/Zrv/RMZ5VOlOWvtZdEHYSTFKZfIBPQa9tOAEeAWhd+AnIneLJ22w5fjOYtoutpWq5w==}
    engines: {node: '>=18'}

  loupe@3.2.1:
    resolution: {integrity: sha512-CdzqowRJCeLU72bHvWqwRBBlLcMEtIvGrlvef74kMnV2AolS9Y8xUv1I0U/MNAWMhBlKIoyuEgoJ0t/bbwHbLQ==}

  lru-cache@10.4.3:
    resolution: {integrity: sha512-JNAzZcXrCt42VGLuYz0zfAzDfAvJWW6AfYlDBQyDV5DClI2m5sAmK+OIO7s59XfsRsWHp02jAJrRadPRGTt6SQ==}

  magic-string@0.30.19:
    resolution: {integrity: sha512-2N21sPY9Ws53PZvsEpVtNuSW+ScYbQdp4b9qUaL+9QkHUrGFKo56Lg9Emg5s9V/qrtNBmiR01sYhUOwu3H+VOw==}

  magicast@0.3.5:
    resolution: {integrity: sha512-L0WhttDl+2BOsybvEOLK7fW3UA0OQ0IQ2d6Zl2x/a6vVRs3bAY0ECOSHHeL5jD+SbOpOCUEi0y1DgHEn9Qn1AQ==}

  make-dir@4.0.0:
    resolution: {integrity: sha512-hXdUTZYIVOt1Ex//jAQi+wTZZpUpwBj/0QsOzqegb3rGMMeJiSEu5xLHnYfBrRV4RH2+OCSOO95Is/7x1WJ4bw==}
    engines: {node: '>=10'}

  merge2@1.4.1:
    resolution: {integrity: sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==}
    engines: {node: '>= 8'}

  micromatch@4.0.8:
    resolution: {integrity: sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==}
    engines: {node: '>=8.6'}

  mimic-function@5.0.1:
    resolution: {integrity: sha512-VP79XUPxV2CigYP3jWwAUFSku2aKqBH7uTAapFWCBqutsbmDo96KY5o8uh6U+/YSIn5OxJnXp73beVkpqMIGhA==}
    engines: {node: '>=18'}

  minimatch@3.1.2:
    resolution: {integrity: sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==}

  minimatch@9.0.5:
    resolution: {integrity: sha512-G6T0ZX48xgozx7587koeX9Ys2NYy6Gmv//P89sEte9V9whIapMNF4idKxnW2QtCcLiTWlb/wfCabAtAFWhhBow==}
    engines: {node: '>=16 || 14 >=14.17'}

  minipass@7.1.2:
    resolution: {integrity: sha512-qOOzS1cBTWYF4BH8fVePDBOO9iptMnGUEZwNc/cMWnTV2nVLZ7VoNWEPHkYczZA0pdoA7dl6e7FL659nX9S2aw==}
    engines: {node: '>=16 || 14 >=14.17'}

  ms@2.1.3:
    resolution: {integrity: sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==}

  nano-spawn@1.0.3:
    resolution: {integrity: sha512-jtpsQDetTnvS2Ts1fiRdci5rx0VYws5jGyC+4IYOTnIQ/wwdf6JdomlHBwqC3bJYOvaKu0C2GSZ1A60anrYpaA==}
    engines: {node: '>=20.17'}

  nanoid@3.3.11:
    resolution: {integrity: sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==}
    engines: {node: ^10 || ^12 || ^13.7 || ^14 || >=15.0.1}
    hasBin: true

  natural-compare@1.4.0:
    resolution: {integrity: sha512-OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==}

  onetime@7.0.0:
    resolution: {integrity: sha512-VXJjc87FScF88uafS3JllDgvAm+c/Slfz06lorj2uAY34rlUu0Nt+v8wreiImcrgAjjIHp1rXpTDlLOGw29WwQ==}
    engines: {node: '>=18'}

  optionator@0.9.4:
    resolution: {integrity: sha512-6IpQ7mKUxRcZNLIObR0hz7lxsapSSIYNZJwXPGeF0mTVqGKFIXj1DQcMoT22S3ROcLyY/rz0PWaWZ9ayWmad9g==}
    engines: {node: '>= 0.8.0'}

  p-limit@3.1.0:
    resolution: {integrity: sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==}
    engines: {node: '>=10'}

  p-locate@5.0.0:
    resolution: {integrity: sha512-LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==}
    engines: {node: '>=10'}

  package-json-from-dist@1.0.1:
    resolution: {integrity: sha512-UEZIS3/by4OC8vL3P2dTXRETpebLI2NiI5vIrjaD/5UtrkFX/tNbwjTSRAGC/+7CAo2pIcBaRgWmcBBHcsaCIw==}

  parent-module@1.0.1:
    resolution: {integrity: sha512-GQ2EWRpQV8/o+Aw8YqtfZZPfNRWZYkbidE9k5rpl/hC3vtHHBfGm2Ifi6qWV+coDGkrUKZAxE3Lot5kcsRlh+g==}
    engines: {node: '>=6'}

  path-exists@4.0.0:
    resolution: {integrity: sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==}
    engines: {node: '>=8'}

  path-key@3.1.1:
    resolution: {integrity: sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==}
    engines: {node: '>=8'}

  path-scurry@1.11.1:
    resolution: {integrity: sha512-Xa4Nw17FS9ApQFJ9umLiJS4orGjm7ZzwUrwamcGQuHSzDyth9boKDaycYdDcZDuqYATXw4HFXgaqWTctW/v1HA==}
    engines: {node: '>=16 || 14 >=14.18'}

  pathe@2.0.3:
    resolution: {integrity: sha512-WUjGcAqP1gQacoQe+OBJsFA7Ld4DyXuUIjZ5cc75cLHvJ7dtNsTugphxIADwspS+AraAUePCKrSVtPLFj/F88w==}

  pathval@2.0.1:
    resolution: {integrity: sha512-//nshmD55c46FuFw26xV/xFAaB5HF9Xdap7HJBBnrKdAd6/GxDBaNA1870O79+9ueg61cZLSVc+OaFlfmObYVQ==}
    engines: {node: '>= 14.16'}

  picocolors@1.1.1:
    resolution: {integrity: sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==}

  picomatch@2.3.1:
    resolution: {integrity: sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==}
    engines: {node: '>=8.6'}

  picomatch@4.0.3:
    resolution: {integrity: sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q==}
    engines: {node: '>=12'}

  pidtree@0.6.0:
    resolution: {integrity: sha512-eG2dWTVw5bzqGRztnHExczNxt5VGsE6OwTeCG3fdUf9KBsZzO3R5OIIIzWR+iZA0NtZ+RDVdaoE2dK1cn6jH4g==}
    engines: {node: '>=0.10'}
    hasBin: true

  postcss@8.5.6:
    resolution: {integrity: sha512-3Ybi1tAuwAP9s0r1UQ2J4n5Y0G05bJkpUIO0/bI9MhwmD70S5aTWbXGBwxHrelT+XM1k6dM0pk+SwNkpTRN7Pg==}
    engines: {node: ^10 || ^12 || >=14}

  prelude-ls@1.2.1:
    resolution: {integrity: sha512-vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==}
    engines: {node: '>= 0.8.0'}

  prettier-linter-helpers@1.0.0:
    resolution: {integrity: sha512-GbK2cP9nraSSUF9N2XwUwqfzlAFlMNYYl+ShE/V+H8a9uNl/oUqB1w2EL54Jh0OlyRSd8RfWYJ3coVS4TROP2w==}
    engines: {node: '>=6.0.0'}

  prettier@3.6.2:
    resolution: {integrity: sha512-I7AIg5boAr5R0FFtJ6rCfD+LFsWHp81dolrFD8S79U9tb8Az2nGrJncnMSnys+bpQJfRUzqs9hnA81OAA3hCuQ==}
    engines: {node: '>=14'}
    hasBin: true

  punycode@2.3.1:
    resolution: {integrity: sha512-vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==}
    engines: {node: '>=6'}

  queue-microtask@1.2.3:
    resolution: {integrity: sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==}

  require-directory@2.1.1:
    resolution: {integrity: sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==}
    engines: {node: '>=0.10.0'}

  resolve-from@4.0.0:
    resolution: {integrity: sha512-pb/MYmXstAkysRFx8piNI1tGFNQIFA3vkE3Gq4EuA1dF6gHp/+vgZqsCGJapvy8N3Q+4o7FwvquPJcnZ7RYy4g==}
    engines: {node: '>=4'}

  restore-cursor@5.1.0:
    resolution: {integrity: sha512-oMA2dcrw6u0YfxJQXm342bFKX/E4sG9rbTzO9ptUcR/e8A33cHuvStiYOwH7fszkZlZ1z/ta9AAoPk2F4qIOHA==}
    engines: {node: '>=18'}

  reusify@1.1.0:
    resolution: {integrity: sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==}
    engines: {iojs: '>=1.0.0', node: '>=0.10.0'}

  rfdc@1.4.1:
    resolution: {integrity: sha512-q1b3N5QkRUWUl7iyylaaj3kOpIT0N2i9MqIEQXP73GVsN9cw3fdx8X63cEmWhJGi2PPCF23Ijp7ktmd39rawIA==}

  rollup@4.52.4:
    resolution: {integrity: sha512-CLEVl+MnPAiKh5pl4dEWSyMTpuflgNQiLGhMv8ezD5W/qP8AKvmYpCOKRRNOh7oRKnauBZ4SyeYkMS+1VSyKwQ==}
    engines: {node: '>=18.0.0', npm: '>=8.0.0'}
    hasBin: true

  run-parallel@1.2.0:
    resolution: {integrity: sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==}

  rxjs@7.8.2:
    resolution: {integrity: sha512-dhKf903U/PQZY6boNNtAGdWbG85WAbjT/1xYoZIC7FAY0yWapOBQVsVrDl58W86//e1VpMNBtRV4MaXfdMySFA==}

  safe-publish-latest@2.0.0:
    resolution: {integrity: sha512-Qc6L9iNKfNl24X8O4XS31yHo49jX1IH+DsnxHIbCDjoARckTOk0Cj9v8G2IYVvZjj94dc9tjs2WIUtL8epJqvw==}
    engines: {node: '>= 12'}
    hasBin: true

  semver@7.7.3:
    resolution: {integrity: sha512-SdsKMrI9TdgjdweUSR9MweHA4EJ8YxHn8DFaDisvhVlUOe4BF1tLD7GAj0lIqWVl+dPb/rExr0Btby5loQm20Q==}
    engines: {node: '>=10'}
    hasBin: true

  shebang-command@2.0.0:
    resolution: {integrity: sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==}
    engines: {node: '>=8'}

  shebang-regex@3.0.0:
    resolution: {integrity: sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==}
    engines: {node: '>=8'}

  shell-quote@1.8.3:
    resolution: {integrity: sha512-ObmnIF4hXNg1BqhnHmgbDETF8dLPCggZWBjkQfhZpbszZnYur5DUljTcCHii5LC3J5E0yeO/1LIMyH+UvHQgyw==}
    engines: {node: '>= 0.4'}

  siginfo@2.0.0:
    resolution: {integrity: sha512-ybx0WO1/8bSBLEWXZvEd7gMW3Sn3JFlW3TvX1nREbDLRNQNaeNN8WK0meBwPdAaOI7TtRRRJn/Es1zhrrCHu7g==}

  signal-exit@4.1.0:
    resolution: {integrity: sha512-bzyZ1e88w9O1iNJbKnOlvYTrWPDl46O1bG0D3XInv+9tkPrxrN8jUUTiFlDkkmKWgn1M6CfIA13SuGqOa9Korw==}
    engines: {node: '>=14'}

  slice-ansi@7.1.2:
    resolution: {integrity: sha512-iOBWFgUX7caIZiuutICxVgX1SdxwAVFFKwt1EvMYYec/NWO5meOJ6K5uQxhrYBdQJne4KxiqZc+KptFOWFSI9w==}
    engines: {node: '>=18'}

  source-map-js@1.2.1:
    resolution: {integrity: sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==}
    engines: {node: '>=0.10.0'}

  stackback@0.0.2:
    resolution: {integrity: sha512-1XMJE5fQo1jGH6Y/7ebnwPOBEkIEnT4QF32d5R1+VXdXveM0IBMJt8zfaxX1P3QhVwrYe+576+jkANtSS2mBbw==}

  std-env@3.9.0:
    resolution: {integrity: sha512-UGvjygr6F6tpH7o2qyqR6QYpwraIjKSdtzyBdyytFOHmPZY917kwdwLG0RbOjWOnKmnm3PeHjaoLLMie7kPLQw==}

  string-argv@0.3.2:
    resolution: {integrity: sha512-aqD2Q0144Z+/RqG52NeHEkZauTAUWJO8c6yTftGJKO3Tja5tUgIfmIl6kExvhtxSDP7fXB6DvzkfMpCd/F3G+Q==}
    engines: {node: '>=0.6.19'}

  string-width@4.2.3:
    resolution: {integrity: sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==}
    engines: {node: '>=8'}

  string-width@5.1.2:
    resolution: {integrity: sha512-HnLOCR3vjcY8beoNLtcjZ5/nxn2afmME6lhrDrebokqMap+XbeW8n9TXpPDOqdGK5qcI3oT0GKTW6wC7EMiVqA==}
    engines: {node: '>=12'}

  string-width@7.2.0:
    resolution: {integrity: sha512-tsaTIkKW9b4N+AEj+SVA+WhJzV7/zMhcSu78mLKWSk7cXMOSHsBKFWUs0fWwq8QyK3MgJBQRX6Gbi4kYbdvGkQ==}
    engines: {node: '>=18'}

  string-width@8.1.0:
    resolution: {integrity: sha512-Kxl3KJGb/gxkaUMOjRsQ8IrXiGW75O4E3RPjFIINOVH8AMl2SQ/yWdTzWwF3FevIX9LcMAjJW+GRwAlAbTSXdg==}
    engines: {node: '>=20'}

  strip-ansi@6.0.1:
    resolution: {integrity: sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==}
    engines: {node: '>=8'}

  strip-ansi@7.1.2:
    resolution: {integrity: sha512-gmBGslpoQJtgnMAvOVqGZpEz9dyoKTCzy2nfz/n8aIFhN/jCE/rCmcxabB6jOOHV+0WNnylOxaxBQPSvcWklhA==}
    engines: {node: '>=12'}

  strip-json-comments@3.1.1:
    resolution: {integrity: sha512-6fPc+R4ihwqP6N/aIv2f1gMH8lOVtWQHoqC4yK6oSDVVocumAsfCqjkXnqiYMhmMwS/mEHLp7Vehlt3ql6lEig==}
    engines: {node: '>=8'}

  strip-literal@3.1.0:
    resolution: {integrity: sha512-8r3mkIM/2+PpjHoOtiAW8Rg3jJLHaV7xPwG+YRGrv6FP0wwk/toTpATxWYOW0BKdWwl82VT2tFYi5DlROa0Mxg==}

  supports-color@10.2.2:
    resolution: {integrity: sha512-SS+jx45GF1QjgEXQx4NJZV9ImqmO2NPz5FNsIHrsDjh2YsHnawpan7SNQ1o8NuhrbHZy9AZhIoCUiCeaW/C80g==}
    engines: {node: '>=18'}

  supports-color@7.2.0:
    resolution: {integrity: sha512-qpCAvRl9stuOHveKsn7HncJRvv501qIacKzQlO/+Lwxc9+0q2wLyv4Dfvt80/DPn2pqOBsJdDiogXGR9+OvwRw==}
    engines: {node: '>=8'}

  synckit@0.11.11:
    resolution: {integrity: sha512-MeQTA1r0litLUf0Rp/iisCaL8761lKAZHaimlbGK4j0HysC4PLfqygQj9srcs0m2RdtDYnF8UuYyKpbjHYp7Jw==}
    engines: {node: ^14.18.0 || >=16.0.0}

  test-exclude@7.0.1:
    resolution: {integrity: sha512-pFYqmTw68LXVjeWJMST4+borgQP2AyMNbg1BpZh9LbyhUeNkeaPF9gzfPGUAnSMV3qPYdWUwDIjjCLiSDOl7vg==}
    engines: {node: '>=18'}

  tinybench@2.9.0:
    resolution: {integrity: sha512-0+DUvqWMValLmha6lr4kD8iAMK1HzV0/aKnCtWb9v9641TnP/MFb7Pc2bxoxQjTXAErryXVgUOfv2YqNllqGeg==}

  tinyexec@0.3.2:
    resolution: {integrity: sha512-KQQR9yN7R5+OSwaK0XQoj22pwHoTlgYqmUscPYoknOoWCWfj/5/ABTMRi69FrKU5ffPVh5QcFikpWJI/P1ocHA==}

  tinyglobby@0.2.15:
    resolution: {integrity: sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ==}
    engines: {node: '>=12.0.0'}

  tinypool@1.1.1:
    resolution: {integrity: sha512-Zba82s87IFq9A9XmjiX5uZA/ARWDrB03OHlq+Vw1fSdt0I+4/Kutwy8BP4Y/y/aORMo61FQ0vIb5j44vSo5Pkg==}
    engines: {node: ^18.0.0 || >=20.0.0}

  tinyrainbow@2.0.0:
    resolution: {integrity: sha512-op4nsTR47R6p0vMUUoYl/a+ljLFVtlfaXkLQmqfLR1qHma1h/ysYk4hEXZ880bf2CYgTskvTa/e196Vd5dDQXw==}
    engines: {node: '>=14.0.0'}

  tinyspy@4.0.4:
    resolution: {integrity: sha512-azl+t0z7pw/z958Gy9svOTuzqIk6xq+NSheJzn5MMWtWTFywIacg2wUlzKFGtt3cthx0r2SxMK0yzJOR0IES7Q==}
    engines: {node: '>=14.0.0'}

  to-regex-range@5.0.1:
    resolution: {integrity: sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==}
    engines: {node: '>=8.0'}

  tree-kill@1.2.2:
    resolution: {integrity: sha512-L0Orpi8qGpRG//Nd+H90vFB+3iHnue1zSSGmNOOCh1GLJ7rUKVwV2HvijphGQS2UmhUZewS9VgvxYIdgr+fG1A==}
    hasBin: true

  ts-api-utils@2.1.0:
    resolution: {integrity: sha512-CUgTZL1irw8u29bzrOD/nH85jqyc74D6SshFgujOIA7osm2Rz7dYH77agkx7H4FBNxDq7Cjf+IjaX/8zwFW+ZQ==}
    engines: {node: '>=18.12'}
    peerDependencies:
      typescript: '>=4.8.4'

  tslib@2.8.1:
    resolution: {integrity: sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==}

  type-check@0.4.0:
    resolution: {integrity: sha512-XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==}
    engines: {node: '>= 0.8.0'}

  typescript-eslint@8.46.0:
    resolution: {integrity: sha512-6+ZrB6y2bT2DX3K+Qd9vn7OFOJR+xSLDj+Aw/N3zBwUt27uTw2sw2TE2+UcY1RiyBZkaGbTkVg9SSdPNUG6aUw==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <6.0.0'

  typescript@5.9.3:
    resolution: {integrity: sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==}
    engines: {node: '>=14.17'}
    hasBin: true

  undici-types@6.21.0:
    resolution: {integrity: sha512-iwDZqg0QAGrg9Rav5H4n0M64c3mkR59cJ6wQp+7C4nI0gsmExaedaYLNO44eT4AtBBwjbTiGPMlt2Md0T9H9JQ==}

  uri-js@4.4.1:
    resolution: {integrity: sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==}

  vite-node@3.2.4:
    resolution: {integrity: sha512-EbKSKh+bh1E1IFxeO0pg1n4dvoOTt0UDiXMd/qn++r98+jPO1xtJilvXldeuQ8giIB5IkpjCgMleHMNEsGH6pg==}
    engines: {node: ^18.0.0 || ^20.0.0 || >=22.0.0}
    hasBin: true

  vite@7.1.9:
    resolution: {integrity: sha512-4nVGliEpxmhCL8DslSAUdxlB6+SMrhB0a1v5ijlh1xB1nEPuy1mxaHxysVucLHuWryAxLWg6a5ei+U4TLn/rFg==}
    engines: {node: ^20.19.0 || >=22.12.0}
    hasBin: true
    peerDependencies:
      '@types/node': ^20.19.0 || >=22.12.0
      jiti: '>=1.21.0'
      less: ^4.0.0
      lightningcss: ^1.21.0
      sass: ^1.70.0
      sass-embedded: ^1.70.0
      stylus: '>=0.54.8'
      sugarss: ^5.0.0
      terser: ^5.16.0
      tsx: ^4.8.1
      yaml: ^2.4.2
    peerDependenciesMeta:
      '@types/node':
        optional: true
      jiti:
        optional: true
      less:
        optional: true
      lightningcss:
        optional: true
      sass:
        optional: true
      sass-embedded:
        optional: true
      stylus:
        optional: true
      sugarss:
        optional: true
      terser:
        optional: true
      tsx:
        optional: true
      yaml:
        optional: true

  vitest@3.2.4:
    resolution: {integrity: sha512-LUCP5ev3GURDysTWiP47wRRUpLKMOfPh+yKTx3kVIEiu5KOMeqzpnYNsKyOoVrULivR8tLcks4+lga33Whn90A==}
    engines: {node: ^18.0.0 || ^20.0.0 || >=22.0.0}
    hasBin: true
    peerDependencies:
      '@edge-runtime/vm': '*'
      '@types/debug': ^4.1.12
      '@types/node': ^18.0.0 || ^20.0.0 || >=22.0.0
      '@vitest/browser': 3.2.4
      '@vitest/ui': 3.2.4
      happy-dom: '*'
      jsdom: '*'
    peerDependenciesMeta:
      '@edge-runtime/vm':
        optional: true
      '@types/debug':
        optional: true
      '@types/node':
        optional: true
      '@vitest/browser':
        optional: true
      '@vitest/ui':
        optional: true
      happy-dom:
        optional: true
      jsdom:
        optional: true

  which@2.0.2:
    resolution: {integrity: sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==}
    engines: {node: '>= 8'}
    hasBin: true

  why-is-node-running@2.3.0:
    resolution: {integrity: sha512-hUrmaWBdVDcxvYqnyh09zunKzROWjbZTiNy8dBEjkS7ehEDQibXJ7XvlmtbwuTclUiIyN+CyXQD4Vmko8fNm8w==}
    engines: {node: '>=8'}
    hasBin: true

  word-wrap@1.2.5:
    resolution: {integrity: sha512-BN22B5eaMMI9UMtjrGd5g5eCYPpCPDUy0FJXbYsaT5zYxjFOckS53SQDE3pWkVoWpHXVb3BrYcEN4Twa55B5cA==}
    engines: {node: '>=0.10.0'}

  wrap-ansi@7.0.0:
    resolution: {integrity: sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==}
    engines: {node: '>=10'}

  wrap-ansi@8.1.0:
    resolution: {integrity: sha512-si7QWI6zUMq56bESFvagtmzMdGOtoxfR+Sez11Mobfc7tm+VkUckk9bW2UeffTGVUbOksxmSw0AA2gs8g71NCQ==}
    engines: {node: '>=12'}

  wrap-ansi@9.0.2:
    resolution: {integrity: sha512-42AtmgqjV+X1VpdOfyTGOYRi0/zsoLqtXQckTmqTeybT+BDIbM/Guxo7x3pE2vtpr1ok6xRqM9OpBe+Jyoqyww==}
    engines: {node: '>=18'}

  y18n@5.0.8:
    resolution: {integrity: sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==}
    engines: {node: '>=10'}

  yaml@2.8.1:
    resolution: {integrity: sha512-lcYcMxX2PO9XMGvAJkJ3OsNMw+/7FKes7/hgerGUYWIoWu5j/+YQqcZr5JnPZWzOsEBgMbSbiSTn/dv/69Mkpw==}
    engines: {node: '>= 14.6'}
    hasBin: true

  yargs-parser@21.1.1:
    resolution: {integrity: sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==}
    engines: {node: '>=12'}

  yargs@17.7.2:
    resolution: {integrity: sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w==}
    engines: {node: '>=12'}

  yocto-queue@0.1.0:
    resolution: {integrity: sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==}
    engines: {node: '>=10'}

snapshots:

  '@ampproject/remapping@2.3.0':
    dependencies:
      '@jridgewell/gen-mapping': 0.3.13
      '@jridgewell/trace-mapping': 0.3.31

  '@babel/helper-string-parser@7.27.1': {}

  '@babel/helper-validator-identifier@7.27.1': {}

  '@babel/parser@7.28.4':
    dependencies:
      '@babel/types': 7.28.4

  '@babel/types@7.28.4':
    dependencies:
      '@babel/helper-string-parser': 7.27.1
      '@babel/helper-validator-identifier': 7.27.1

  '@bcoe/v8-coverage@1.0.2': {}

  '@esbuild/aix-ppc64@0.25.10':
    optional: true

  '@esbuild/android-arm64@0.25.10':
    optional: true

  '@esbuild/android-arm@0.25.10':
    optional: true

  '@esbuild/android-x64@0.25.10':
    optional: true

  '@esbuild/darwin-arm64@0.25.10':
    optional: true

  '@esbuild/darwin-x64@0.25.10':
    optional: true

  '@esbuild/freebsd-arm64@0.25.10':
    optional: true

  '@esbuild/freebsd-x64@0.25.10':
    optional: true

  '@esbuild/linux-arm64@0.25.10':
    optional: true

  '@esbuild/linux-arm@0.25.10':
    optional: true

  '@esbuild/linux-ia32@0.25.10':
    optional: true

  '@esbuild/linux-loong64@0.25.10':
    optional: true

  '@esbuild/linux-mips64el@0.25.10':
    optional: true

  '@esbuild/linux-ppc64@0.25.10':
    optional: true

  '@esbuild/linux-riscv64@0.25.10':
    optional: true

  '@esbuild/linux-s390x@0.25.10':
    optional: true

  '@esbuild/linux-x64@0.25.10':
    optional: true

  '@esbuild/netbsd-arm64@0.25.10':
    optional: true

  '@esbuild/netbsd-x64@0.25.10':
    optional: true

  '@esbuild/openbsd-arm64@0.25.10':
    optional: true

  '@esbuild/openbsd-x64@0.25.10':
    optional: true

  '@esbuild/openharmony-arm64@0.25.10':
    optional: true

  '@esbuild/sunos-x64@0.25.10':
    optional: true

  '@esbuild/win32-arm64@0.25.10':
    optional: true

  '@esbuild/win32-ia32@0.25.10':
    optional: true

  '@esbuild/win32-x64@0.25.10':
    optional: true

  '@eslint-community/eslint-utils@4.9.0(eslint@9.37.0(supports-color@10.2.2))':
    dependencies:
      eslint: 9.37.0(supports-color@10.2.2)
      eslint-visitor-keys: 3.4.3

  '@eslint-community/regexpp@4.12.1': {}

  '@eslint/compat@1.4.0(eslint@9.37.0(supports-color@10.2.2))':
    dependencies:
      '@eslint/core': 0.16.0
    optionalDependencies:
      eslint: 9.37.0(supports-color@10.2.2)

  '@eslint/config-array@0.21.0(supports-color@10.2.2)':
    dependencies:
      '@eslint/object-schema': 2.1.6
      debug: 4.4.3(supports-color@10.2.2)
      minimatch: 3.1.2
    transitivePeerDependencies:
      - supports-color

  '@eslint/config-helpers@0.4.0':
    dependencies:
      '@eslint/core': 0.16.0

  '@eslint/core@0.16.0':
    dependencies:
      '@types/json-schema': 7.0.15

  '@eslint/eslintrc@3.3.1(supports-color@10.2.2)':
    dependencies:
      ajv: 6.12.6
      debug: 4.4.3(supports-color@10.2.2)
      espree: 10.4.0
      globals: 14.0.0
      ignore: 5.3.2
      import-fresh: 3.3.1
      js-yaml: 4.1.0
      minimatch: 3.1.2
      strip-json-comments: 3.1.1
    transitivePeerDependencies:
      - supports-color

  '@eslint/js@9.37.0': {}

  '@eslint/object-schema@2.1.6': {}

  '@eslint/plugin-kit@0.4.0':
    dependencies:
      '@eslint/core': 0.16.0
      levn: 0.4.1

  '@hirez_io/observer-spy@2.2.0(rxjs@7.8.2)(typescript@5.9.3)':
    dependencies:
      rxjs: 7.8.2
      typescript: 5.9.3

  '@humanfs/core@0.19.1': {}

  '@humanfs/node@0.16.7':
    dependencies:
      '@humanfs/core': 0.19.1
      '@humanwhocodes/retry': 0.4.3

  '@humanwhocodes/module-importer@1.0.1': {}

  '@humanwhocodes/retry@0.4.3': {}

  '@isaacs/cliui@8.0.2':
    dependencies:
      string-width: 5.1.2
      string-width-cjs: string-width@4.2.3
      strip-ansi: 7.1.2
      strip-ansi-cjs: strip-ansi@6.0.1
      wrap-ansi: 8.1.0
      wrap-ansi-cjs: wrap-ansi@7.0.0

  '@istanbuljs/schema@0.1.3': {}

  '@jridgewell/gen-mapping@0.3.13':
    dependencies:
      '@jridgewell/sourcemap-codec': 1.5.5
      '@jridgewell/trace-mapping': 0.3.31

  '@jridgewell/resolve-uri@3.1.2': {}

  '@jridgewell/sourcemap-codec@1.5.5': {}

  '@jridgewell/trace-mapping@0.3.31':
    dependencies:
      '@jridgewell/resolve-uri': 3.1.2
      '@jridgewell/sourcemap-codec': 1.5.5

  '@nodelib/fs.scandir@2.1.5':
    dependencies:
      '@nodelib/fs.stat': 2.0.5
      run-parallel: 1.2.0

  '@nodelib/fs.stat@2.0.5': {}

  '@nodelib/fs.walk@1.2.8':
    dependencies:
      '@nodelib/fs.scandir': 2.1.5
      fastq: 1.19.1

  '@pkgjs/parseargs@0.11.0':
    optional: true

  '@pkgr/core@0.2.9': {}

  '@rollup/rollup-android-arm-eabi@4.52.4':
    optional: true

  '@rollup/rollup-android-arm64@4.52.4':
    optional: true

  '@rollup/rollup-darwin-arm64@4.52.4':
    optional: true

  '@rollup/rollup-darwin-x64@4.52.4':
    optional: true

  '@rollup/rollup-freebsd-arm64@4.52.4':
    optional: true

  '@rollup/rollup-freebsd-x64@4.52.4':
    optional: true

  '@rollup/rollup-linux-arm-gnueabihf@4.52.4':
    optional: true

  '@rollup/rollup-linux-arm-musleabihf@4.52.4':
    optional: true

  '@rollup/rollup-linux-arm64-gnu@4.52.4':
    optional: true

  '@rollup/rollup-linux-arm64-musl@4.52.4':
    optional: true

  '@rollup/rollup-linux-loong64-gnu@4.52.4':
    optional: true

  '@rollup/rollup-linux-ppc64-gnu@4.52.4':
    optional: true

  '@rollup/rollup-linux-riscv64-gnu@4.52.4':
    optional: true

  '@rollup/rollup-linux-riscv64-musl@4.52.4':
    optional: true

  '@rollup/rollup-linux-s390x-gnu@4.52.4':
    optional: true

  '@rollup/rollup-linux-x64-gnu@4.52.4':
    optional: true

  '@rollup/rollup-linux-x64-musl@4.52.4':
    optional: true

  '@rollup/rollup-openharmony-arm64@4.52.4':
    optional: true

  '@rollup/rollup-win32-arm64-msvc@4.52.4':
    optional: true

  '@rollup/rollup-win32-ia32-msvc@4.52.4':
    optional: true

  '@rollup/rollup-win32-x64-gnu@4.52.4':
    optional: true

  '@rollup/rollup-win32-x64-msvc@4.52.4':
    optional: true

  '@types/chai@5.2.2':
    dependencies:
      '@types/deep-eql': 4.0.2

  '@types/debug@4.1.12':
    dependencies:
      '@types/ms': 2.1.0
    optional: true

  '@types/deep-eql@4.0.2': {}

  '@types/estree@1.0.8': {}

  '@types/json-schema@7.0.15': {}

  '@types/ms@2.1.0':
    optional: true

  '@types/node@20.19.20':
    dependencies:
      undici-types: 6.21.0

  '@types/shell-quote@1.7.5': {}

  '@types/yargs-parser@21.0.3': {}

  '@types/yargs@17.0.33':
    dependencies:
      '@types/yargs-parser': 21.0.3

  '@typescript-eslint/eslint-plugin@8.46.0(@typescript-eslint/parser@8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3))(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)':
    dependencies:
      '@eslint-community/regexpp': 4.12.1
      '@typescript-eslint/parser': 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/scope-manager': 8.46.0
      '@typescript-eslint/type-utils': 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/utils': 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/visitor-keys': 8.46.0
      eslint: 9.37.0(supports-color@10.2.2)
      graphemer: 1.4.0
      ignore: 7.0.5
      natural-compare: 1.4.0
      ts-api-utils: 2.1.0(typescript@5.9.3)
      typescript: 5.9.3
    transitivePeerDependencies:
      - supports-color

  '@typescript-eslint/parser@8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)':
    dependencies:
      '@typescript-eslint/scope-manager': 8.46.0
      '@typescript-eslint/types': 8.46.0
      '@typescript-eslint/typescript-estree': 8.46.0(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/visitor-keys': 8.46.0
      debug: 4.4.3(supports-color@10.2.2)
      eslint: 9.37.0(supports-color@10.2.2)
      typescript: 5.9.3
    transitivePeerDependencies:
      - supports-color

  '@typescript-eslint/project-service@8.46.0(supports-color@10.2.2)(typescript@5.9.3)':
    dependencies:
      '@typescript-eslint/tsconfig-utils': 8.46.0(typescript@5.9.3)
      '@typescript-eslint/types': 8.46.0
      debug: 4.4.3(supports-color@10.2.2)
      typescript: 5.9.3
    transitivePeerDependencies:
      - supports-color

  '@typescript-eslint/scope-manager@8.46.0':
    dependencies:
      '@typescript-eslint/types': 8.46.0
      '@typescript-eslint/visitor-keys': 8.46.0

  '@typescript-eslint/tsconfig-utils@8.46.0(typescript@5.9.3)':
    dependencies:
      typescript: 5.9.3

  '@typescript-eslint/type-utils@8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)':
    dependencies:
      '@typescript-eslint/types': 8.46.0
      '@typescript-eslint/typescript-estree': 8.46.0(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/utils': 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      debug: 4.4.3(supports-color@10.2.2)
      eslint: 9.37.0(supports-color@10.2.2)
      ts-api-utils: 2.1.0(typescript@5.9.3)
      typescript: 5.9.3
    transitivePeerDependencies:
      - supports-color

  '@typescript-eslint/types@8.46.0': {}

  '@typescript-eslint/typescript-estree@8.46.0(supports-color@10.2.2)(typescript@5.9.3)':
    dependencies:
      '@typescript-eslint/project-service': 8.46.0(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/tsconfig-utils': 8.46.0(typescript@5.9.3)
      '@typescript-eslint/types': 8.46.0
      '@typescript-eslint/visitor-keys': 8.46.0
      debug: 4.4.3(supports-color@10.2.2)
      fast-glob: 3.3.3
      is-glob: 4.0.3
      minimatch: 9.0.5
      semver: 7.7.3
      ts-api-utils: 2.1.0(typescript@5.9.3)
      typescript: 5.9.3
    transitivePeerDependencies:
      - supports-color

  '@typescript-eslint/utils@8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)':
    dependencies:
      '@eslint-community/eslint-utils': 4.9.0(eslint@9.37.0(supports-color@10.2.2))
      '@typescript-eslint/scope-manager': 8.46.0
      '@typescript-eslint/types': 8.46.0
      '@typescript-eslint/typescript-estree': 8.46.0(supports-color@10.2.2)(typescript@5.9.3)
      eslint: 9.37.0(supports-color@10.2.2)
      typescript: 5.9.3
    transitivePeerDependencies:
      - supports-color

  '@typescript-eslint/visitor-keys@8.46.0':
    dependencies:
      '@typescript-eslint/types': 8.46.0
      eslint-visitor-keys: 4.2.1

  '@vitest/coverage-v8@3.2.4(supports-color@10.2.2)(vitest@3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1))':
    dependencies:
      '@ampproject/remapping': 2.3.0
      '@bcoe/v8-coverage': 1.0.2
      ast-v8-to-istanbul: 0.3.5
      debug: 4.4.3(supports-color@10.2.2)
      istanbul-lib-coverage: 3.2.2
      istanbul-lib-report: 3.0.1
      istanbul-lib-source-maps: 5.0.6(supports-color@10.2.2)
      istanbul-reports: 3.2.0
      magic-string: 0.30.19
      magicast: 0.3.5
      std-env: 3.9.0
      test-exclude: 7.0.1
      tinyrainbow: 2.0.0
      vitest: 3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1)
    transitivePeerDependencies:
      - supports-color

  '@vitest/eslint-plugin@1.3.16(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)(vitest@3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1))':
    dependencies:
      '@typescript-eslint/scope-manager': 8.46.0
      '@typescript-eslint/utils': 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      eslint: 9.37.0(supports-color@10.2.2)
    optionalDependencies:
      typescript: 5.9.3
      vitest: 3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1)
    transitivePeerDependencies:
      - supports-color

  '@vitest/expect@3.2.4':
    dependencies:
      '@types/chai': 5.2.2
      '@vitest/spy': 3.2.4
      '@vitest/utils': 3.2.4
      chai: 5.3.3
      tinyrainbow: 2.0.0

  '@vitest/mocker@3.2.4(vite@7.1.9(@types/node@20.19.20)(yaml@2.8.1))':
    dependencies:
      '@vitest/spy': 3.2.4
      estree-walker: 3.0.3
      magic-string: 0.30.19
    optionalDependencies:
      vite: 7.1.9(@types/node@20.19.20)(yaml@2.8.1)

  '@vitest/pretty-format@3.2.4':
    dependencies:
      tinyrainbow: 2.0.0

  '@vitest/runner@3.2.4':
    dependencies:
      '@vitest/utils': 3.2.4
      pathe: 2.0.3
      strip-literal: 3.1.0

  '@vitest/snapshot@3.2.4':
    dependencies:
      '@vitest/pretty-format': 3.2.4
      magic-string: 0.30.19
      pathe: 2.0.3

  '@vitest/spy@3.2.4':
    dependencies:
      tinyspy: 4.0.4

  '@vitest/utils@3.2.4':
    dependencies:
      '@vitest/pretty-format': 3.2.4
      loupe: 3.2.1
      tinyrainbow: 2.0.0

  acorn-jsx@5.3.2(acorn@8.15.0):
    dependencies:
      acorn: 8.15.0

  acorn@8.15.0: {}

  ajv@6.12.6:
    dependencies:
      fast-deep-equal: 3.1.3
      fast-json-stable-stringify: 2.1.0
      json-schema-traverse: 0.4.1
      uri-js: 4.4.1

  ansi-escapes@7.1.1:
    dependencies:
      environment: 1.1.0

  ansi-regex@5.0.1: {}

  ansi-regex@6.2.2: {}

  ansi-styles@4.3.0:
    dependencies:
      color-convert: 2.0.1

  ansi-styles@6.2.3: {}

  argparse@2.0.1: {}

  assertion-error@2.0.1: {}

  ast-v8-to-istanbul@0.3.5:
    dependencies:
      '@jridgewell/trace-mapping': 0.3.31
      estree-walker: 3.0.3
      js-tokens: 9.0.1

  balanced-match@1.0.2: {}

  brace-expansion@1.1.12:
    dependencies:
      balanced-match: 1.0.2
      concat-map: 0.0.1

  brace-expansion@2.0.2:
    dependencies:
      balanced-match: 1.0.2

  braces@3.0.3:
    dependencies:
      fill-range: 7.1.1

  cac@6.7.14: {}

  callsites@3.1.0: {}

  chai@5.3.3:
    dependencies:
      assertion-error: 2.0.1
      check-error: 2.1.1
      deep-eql: 5.0.2
      loupe: 3.2.1
      pathval: 2.0.1

  chalk@4.1.2:
    dependencies:
      ansi-styles: 4.3.0
      supports-color: 7.2.0

  chalk@5.6.2: {}

  check-error@2.1.1: {}

  cli-cursor@5.0.0:
    dependencies:
      restore-cursor: 5.1.0

  cli-truncate@5.1.0:
    dependencies:
      slice-ansi: 7.1.2
      string-width: 8.1.0

  cliui@8.0.1:
    dependencies:
      string-width: 4.2.3
      strip-ansi: 6.0.1
      wrap-ansi: 7.0.0

  color-convert@2.0.1:
    dependencies:
      color-name: 1.1.4

  color-name@1.1.4: {}

  colorette@2.0.20: {}

  commander@14.0.1: {}

  concat-map@0.0.1: {}

  cross-spawn@7.0.6:
    dependencies:
      path-key: 3.1.1
      shebang-command: 2.0.0
      which: 2.0.2

  ctrlc-wrapper-windows-32@0.0.3:
    optional: true

  ctrlc-wrapper-windows-64@0.0.3:
    optional: true

  ctrlc-wrapper@0.0.5:
    optionalDependencies:
      ctrlc-wrapper-windows-32: 0.0.3
      ctrlc-wrapper-windows-64: 0.0.3

  debug@4.4.3(supports-color@10.2.2):
    dependencies:
      ms: 2.1.3
    optionalDependencies:
      supports-color: 10.2.2

  deep-eql@5.0.2: {}

  deep-is@0.1.4: {}

  eastasianwidth@0.2.0: {}

  emoji-regex@10.5.0: {}

  emoji-regex@8.0.0: {}

  emoji-regex@9.2.2: {}

  environment@1.1.0: {}

  es-module-lexer@1.7.0: {}

  esbuild@0.25.10:
    optionalDependencies:
      '@esbuild/aix-ppc64': 0.25.10
      '@esbuild/android-arm': 0.25.10
      '@esbuild/android-arm64': 0.25.10
      '@esbuild/android-x64': 0.25.10
      '@esbuild/darwin-arm64': 0.25.10
      '@esbuild/darwin-x64': 0.25.10
      '@esbuild/freebsd-arm64': 0.25.10
      '@esbuild/freebsd-x64': 0.25.10
      '@esbuild/linux-arm': 0.25.10
      '@esbuild/linux-arm64': 0.25.10
      '@esbuild/linux-ia32': 0.25.10
      '@esbuild/linux-loong64': 0.25.10
      '@esbuild/linux-mips64el': 0.25.10
      '@esbuild/linux-ppc64': 0.25.10
      '@esbuild/linux-riscv64': 0.25.10
      '@esbuild/linux-s390x': 0.25.10
      '@esbuild/linux-x64': 0.25.10
      '@esbuild/netbsd-arm64': 0.25.10
      '@esbuild/netbsd-x64': 0.25.10
      '@esbuild/openbsd-arm64': 0.25.10
      '@esbuild/openbsd-x64': 0.25.10
      '@esbuild/openharmony-arm64': 0.25.10
      '@esbuild/sunos-x64': 0.25.10
      '@esbuild/win32-arm64': 0.25.10
      '@esbuild/win32-ia32': 0.25.10
      '@esbuild/win32-x64': 0.25.10

  escalade@3.2.0: {}

  escape-string-regexp@4.0.0: {}

  eslint-config-flat-gitignore@2.1.0(eslint@9.37.0(supports-color@10.2.2)):
    dependencies:
      '@eslint/compat': 1.4.0(eslint@9.37.0(supports-color@10.2.2))
      eslint: 9.37.0(supports-color@10.2.2)

  eslint-config-prettier@10.1.8(eslint@9.37.0(supports-color@10.2.2)):
    dependencies:
      eslint: 9.37.0(supports-color@10.2.2)

  eslint-plugin-import-lite@0.3.0(eslint@9.37.0(supports-color@10.2.2))(typescript@5.9.3):
    dependencies:
      '@eslint-community/eslint-utils': 4.9.0(eslint@9.37.0(supports-color@10.2.2))
      '@typescript-eslint/types': 8.46.0
      eslint: 9.37.0(supports-color@10.2.2)
    optionalDependencies:
      typescript: 5.9.3

  eslint-plugin-prettier@5.5.4(eslint-config-prettier@10.1.8(eslint@9.37.0(supports-color@10.2.2)))(eslint@9.37.0(supports-color@10.2.2))(prettier@3.6.2):
    dependencies:
      eslint: 9.37.0(supports-color@10.2.2)
      prettier: 3.6.2
      prettier-linter-helpers: 1.0.0
      synckit: 0.11.11
    optionalDependencies:
      eslint-config-prettier: 10.1.8(eslint@9.37.0(supports-color@10.2.2))

  eslint-plugin-simple-import-sort@12.1.1(eslint@9.37.0(supports-color@10.2.2)):
    dependencies:
      eslint: 9.37.0(supports-color@10.2.2)

  eslint-scope@8.4.0:
    dependencies:
      esrecurse: 4.3.0
      estraverse: 5.3.0

  eslint-visitor-keys@3.4.3: {}

  eslint-visitor-keys@4.2.1: {}

  eslint@9.37.0(supports-color@10.2.2):
    dependencies:
      '@eslint-community/eslint-utils': 4.9.0(eslint@9.37.0(supports-color@10.2.2))
      '@eslint-community/regexpp': 4.12.1
      '@eslint/config-array': 0.21.0(supports-color@10.2.2)
      '@eslint/config-helpers': 0.4.0
      '@eslint/core': 0.16.0
      '@eslint/eslintrc': 3.3.1(supports-color@10.2.2)
      '@eslint/js': 9.37.0
      '@eslint/plugin-kit': 0.4.0
      '@humanfs/node': 0.16.7
      '@humanwhocodes/module-importer': 1.0.1
      '@humanwhocodes/retry': 0.4.3
      '@types/estree': 1.0.8
      '@types/json-schema': 7.0.15
      ajv: 6.12.6
      chalk: 4.1.2
      cross-spawn: 7.0.6
      debug: 4.4.3(supports-color@10.2.2)
      escape-string-regexp: 4.0.0
      eslint-scope: 8.4.0
      eslint-visitor-keys: 4.2.1
      espree: 10.4.0
      esquery: 1.6.0
      esutils: 2.0.3
      fast-deep-equal: 3.1.3
      file-entry-cache: 8.0.0
      find-up: 5.0.0
      glob-parent: 6.0.2
      ignore: 5.3.2
      imurmurhash: 0.1.4
      is-glob: 4.0.3
      json-stable-stringify-without-jsonify: 1.0.1
      lodash.merge: 4.6.2
      minimatch: 3.1.2
      natural-compare: 1.4.0
      optionator: 0.9.4
    transitivePeerDependencies:
      - supports-color

  espree@10.4.0:
    dependencies:
      acorn: 8.15.0
      acorn-jsx: 5.3.2(acorn@8.15.0)
      eslint-visitor-keys: 4.2.1

  esquery@1.6.0:
    dependencies:
      estraverse: 5.3.0

  esrecurse@4.3.0:
    dependencies:
      estraverse: 5.3.0

  estraverse@5.3.0: {}

  estree-walker@3.0.3:
    dependencies:
      '@types/estree': 1.0.8

  esutils@2.0.3: {}

  eventemitter3@5.0.1: {}

  expect-type@1.2.2: {}

  fast-deep-equal@3.1.3: {}

  fast-diff@1.3.0: {}

  fast-glob@3.3.3:
    dependencies:
      '@nodelib/fs.stat': 2.0.5
      '@nodelib/fs.walk': 1.2.8
      glob-parent: 5.1.2
      merge2: 1.4.1
      micromatch: 4.0.8

  fast-json-stable-stringify@2.1.0: {}

  fast-levenshtein@2.0.6: {}

  fastq@1.19.1:
    dependencies:
      reusify: 1.1.0

  fdir@6.5.0(picomatch@4.0.3):
    optionalDependencies:
      picomatch: 4.0.3

  file-entry-cache@8.0.0:
    dependencies:
      flat-cache: 4.0.1

  fill-range@7.1.1:
    dependencies:
      to-regex-range: 5.0.1

  find-up@5.0.0:
    dependencies:
      locate-path: 6.0.0
      path-exists: 4.0.0

  flat-cache@4.0.1:
    dependencies:
      flatted: 3.3.3
      keyv: 4.5.4

  flatted@3.3.3: {}

  foreground-child@3.3.1:
    dependencies:
      cross-spawn: 7.0.6
      signal-exit: 4.1.0

  fsevents@2.3.3:
    optional: true

  get-caller-file@2.0.5: {}

  get-east-asian-width@1.4.0: {}

  glob-parent@5.1.2:
    dependencies:
      is-glob: 4.0.3

  glob-parent@6.0.2:
    dependencies:
      is-glob: 4.0.3

  glob@10.4.5:
    dependencies:
      foreground-child: 3.3.1
      jackspeak: 3.4.3
      minimatch: 9.0.5
      minipass: 7.1.2
      package-json-from-dist: 1.0.1
      path-scurry: 1.11.1

  globals@14.0.0: {}

  globals@16.4.0: {}

  graphemer@1.4.0: {}

  has-flag@4.0.0: {}

  html-escaper@2.0.2: {}

  husky@9.1.7: {}

  ignore@5.3.2: {}

  ignore@7.0.5: {}

  import-fresh@3.3.1:
    dependencies:
      parent-module: 1.0.1
      resolve-from: 4.0.0

  imurmurhash@0.1.4: {}

  in-publish@2.0.1: {}

  is-extglob@2.1.1: {}

  is-fullwidth-code-point@3.0.0: {}

  is-fullwidth-code-point@5.1.0:
    dependencies:
      get-east-asian-width: 1.4.0

  is-glob@4.0.3:
    dependencies:
      is-extglob: 2.1.1

  is-number@7.0.0: {}

  isexe@2.0.0: {}

  istanbul-lib-coverage@3.2.2: {}

  istanbul-lib-report@3.0.1:
    dependencies:
      istanbul-lib-coverage: 3.2.2
      make-dir: 4.0.0
      supports-color: 7.2.0

  istanbul-lib-source-maps@5.0.6(supports-color@10.2.2):
    dependencies:
      '@jridgewell/trace-mapping': 0.3.31
      debug: 4.4.3(supports-color@10.2.2)
      istanbul-lib-coverage: 3.2.2
    transitivePeerDependencies:
      - supports-color

  istanbul-reports@3.2.0:
    dependencies:
      html-escaper: 2.0.2
      istanbul-lib-report: 3.0.1

  jackspeak@3.4.3:
    dependencies:
      '@isaacs/cliui': 8.0.2
    optionalDependencies:
      '@pkgjs/parseargs': 0.11.0

  js-tokens@9.0.1: {}

  js-yaml@4.1.0:
    dependencies:
      argparse: 2.0.1

  json-buffer@3.0.1: {}

  json-schema-traverse@0.4.1: {}

  json-stable-stringify-without-jsonify@1.0.1: {}

  keyv@4.5.4:
    dependencies:
      json-buffer: 3.0.1

  levn@0.4.1:
    dependencies:
      prelude-ls: 1.2.1
      type-check: 0.4.0

  lint-staged@16.2.3:
    dependencies:
      commander: 14.0.1
      listr2: 9.0.4
      micromatch: 4.0.8
      nano-spawn: 1.0.3
      pidtree: 0.6.0
      string-argv: 0.3.2
      yaml: 2.8.1

  listr2@9.0.4:
    dependencies:
      cli-truncate: 5.1.0
      colorette: 2.0.20
      eventemitter3: 5.0.1
      log-update: 6.1.0
      rfdc: 1.4.1
      wrap-ansi: 9.0.2

  locate-path@6.0.0:
    dependencies:
      p-locate: 5.0.0

  lodash.merge@4.6.2: {}

  log-update@6.1.0:
    dependencies:
      ansi-escapes: 7.1.1
      cli-cursor: 5.0.0
      slice-ansi: 7.1.2
      strip-ansi: 7.1.2
      wrap-ansi: 9.0.2

  loupe@3.2.1: {}

  lru-cache@10.4.3: {}

  magic-string@0.30.19:
    dependencies:
      '@jridgewell/sourcemap-codec': 1.5.5

  magicast@0.3.5:
    dependencies:
      '@babel/parser': 7.28.4
      '@babel/types': 7.28.4
      source-map-js: 1.2.1

  make-dir@4.0.0:
    dependencies:
      semver: 7.7.3

  merge2@1.4.1: {}

  micromatch@4.0.8:
    dependencies:
      braces: 3.0.3
      picomatch: 2.3.1

  mimic-function@5.0.1: {}

  minimatch@3.1.2:
    dependencies:
      brace-expansion: 1.1.12

  minimatch@9.0.5:
    dependencies:
      brace-expansion: 2.0.2

  minipass@7.1.2: {}

  ms@2.1.3: {}

  nano-spawn@1.0.3: {}

  nanoid@3.3.11: {}

  natural-compare@1.4.0: {}

  onetime@7.0.0:
    dependencies:
      mimic-function: 5.0.1

  optionator@0.9.4:
    dependencies:
      deep-is: 0.1.4
      fast-levenshtein: 2.0.6
      levn: 0.4.1
      prelude-ls: 1.2.1
      type-check: 0.4.0
      word-wrap: 1.2.5

  p-limit@3.1.0:
    dependencies:
      yocto-queue: 0.1.0

  p-locate@5.0.0:
    dependencies:
      p-limit: 3.1.0

  package-json-from-dist@1.0.1: {}

  parent-module@1.0.1:
    dependencies:
      callsites: 3.1.0

  path-exists@4.0.0: {}

  path-key@3.1.1: {}

  path-scurry@1.11.1:
    dependencies:
      lru-cache: 10.4.3
      minipass: 7.1.2

  pathe@2.0.3: {}

  pathval@2.0.1: {}

  picocolors@1.1.1: {}

  picomatch@2.3.1: {}

  picomatch@4.0.3: {}

  pidtree@0.6.0: {}

  postcss@8.5.6:
    dependencies:
      nanoid: 3.3.11
      picocolors: 1.1.1
      source-map-js: 1.2.1

  prelude-ls@1.2.1: {}

  prettier-linter-helpers@1.0.0:
    dependencies:
      fast-diff: 1.3.0

  prettier@3.6.2: {}

  punycode@2.3.1: {}

  queue-microtask@1.2.3: {}

  require-directory@2.1.1: {}

  resolve-from@4.0.0: {}

  restore-cursor@5.1.0:
    dependencies:
      onetime: 7.0.0
      signal-exit: 4.1.0

  reusify@1.1.0: {}

  rfdc@1.4.1: {}

  rollup@4.52.4:
    dependencies:
      '@types/estree': 1.0.8
    optionalDependencies:
      '@rollup/rollup-android-arm-eabi': 4.52.4
      '@rollup/rollup-android-arm64': 4.52.4
      '@rollup/rollup-darwin-arm64': 4.52.4
      '@rollup/rollup-darwin-x64': 4.52.4
      '@rollup/rollup-freebsd-arm64': 4.52.4
      '@rollup/rollup-freebsd-x64': 4.52.4
      '@rollup/rollup-linux-arm-gnueabihf': 4.52.4
      '@rollup/rollup-linux-arm-musleabihf': 4.52.4
      '@rollup/rollup-linux-arm64-gnu': 4.52.4
      '@rollup/rollup-linux-arm64-musl': 4.52.4
      '@rollup/rollup-linux-loong64-gnu': 4.52.4
      '@rollup/rollup-linux-ppc64-gnu': 4.52.4
      '@rollup/rollup-linux-riscv64-gnu': 4.52.4
      '@rollup/rollup-linux-riscv64-musl': 4.52.4
      '@rollup/rollup-linux-s390x-gnu': 4.52.4
      '@rollup/rollup-linux-x64-gnu': 4.52.4
      '@rollup/rollup-linux-x64-musl': 4.52.4
      '@rollup/rollup-openharmony-arm64': 4.52.4
      '@rollup/rollup-win32-arm64-msvc': 4.52.4
      '@rollup/rollup-win32-ia32-msvc': 4.52.4
      '@rollup/rollup-win32-x64-gnu': 4.52.4
      '@rollup/rollup-win32-x64-msvc': 4.52.4
      fsevents: 2.3.3

  run-parallel@1.2.0:
    dependencies:
      queue-microtask: 1.2.3

  rxjs@7.8.2:
    dependencies:
      tslib: 2.8.1

  safe-publish-latest@2.0.0:
    dependencies:
      in-publish: 2.0.1
      semver: 7.7.3
      yargs: 17.7.2

  semver@7.7.3: {}

  shebang-command@2.0.0:
    dependencies:
      shebang-regex: 3.0.0

  shebang-regex@3.0.0: {}

  shell-quote@1.8.3: {}

  siginfo@2.0.0: {}

  signal-exit@4.1.0: {}

  slice-ansi@7.1.2:
    dependencies:
      ansi-styles: 6.2.3
      is-fullwidth-code-point: 5.1.0

  source-map-js@1.2.1: {}

  stackback@0.0.2: {}

  std-env@3.9.0: {}

  string-argv@0.3.2: {}

  string-width@4.2.3:
    dependencies:
      emoji-regex: 8.0.0
      is-fullwidth-code-point: 3.0.0
      strip-ansi: 6.0.1

  string-width@5.1.2:
    dependencies:
      eastasianwidth: 0.2.0
      emoji-regex: 9.2.2
      strip-ansi: 7.1.2

  string-width@7.2.0:
    dependencies:
      emoji-regex: 10.5.0
      get-east-asian-width: 1.4.0
      strip-ansi: 7.1.2

  string-width@8.1.0:
    dependencies:
      get-east-asian-width: 1.4.0
      strip-ansi: 7.1.2

  strip-ansi@6.0.1:
    dependencies:
      ansi-regex: 5.0.1

  strip-ansi@7.1.2:
    dependencies:
      ansi-regex: 6.2.2

  strip-json-comments@3.1.1: {}

  strip-literal@3.1.0:
    dependencies:
      js-tokens: 9.0.1

  supports-color@10.2.2: {}

  supports-color@7.2.0:
    dependencies:
      has-flag: 4.0.0

  synckit@0.11.11:
    dependencies:
      '@pkgr/core': 0.2.9

  test-exclude@7.0.1:
    dependencies:
      '@istanbuljs/schema': 0.1.3
      glob: 10.4.5
      minimatch: 9.0.5

  tinybench@2.9.0: {}

  tinyexec@0.3.2: {}

  tinyglobby@0.2.15:
    dependencies:
      fdir: 6.5.0(picomatch@4.0.3)
      picomatch: 4.0.3

  tinypool@1.1.1: {}

  tinyrainbow@2.0.0: {}

  tinyspy@4.0.4: {}

  to-regex-range@5.0.1:
    dependencies:
      is-number: 7.0.0

  tree-kill@1.2.2: {}

  ts-api-utils@2.1.0(typescript@5.9.3):
    dependencies:
      typescript: 5.9.3

  tslib@2.8.1: {}

  type-check@0.4.0:
    dependencies:
      prelude-ls: 1.2.1

  typescript-eslint@8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3):
    dependencies:
      '@typescript-eslint/eslint-plugin': 8.46.0(@typescript-eslint/parser@8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3))(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/parser': 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/typescript-estree': 8.46.0(supports-color@10.2.2)(typescript@5.9.3)
      '@typescript-eslint/utils': 8.46.0(eslint@9.37.0(supports-color@10.2.2))(supports-color@10.2.2)(typescript@5.9.3)
      eslint: 9.37.0(supports-color@10.2.2)
      typescript: 5.9.3
    transitivePeerDependencies:
      - supports-color

  typescript@5.9.3: {}

  undici-types@6.21.0: {}

  uri-js@4.4.1:
    dependencies:
      punycode: 2.3.1

  vite-node@3.2.4(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1):
    dependencies:
      cac: 6.7.14
      debug: 4.4.3(supports-color@10.2.2)
      es-module-lexer: 1.7.0
      pathe: 2.0.3
      vite: 7.1.9(@types/node@20.19.20)(yaml@2.8.1)
    transitivePeerDependencies:
      - '@types/node'
      - jiti
      - less
      - lightningcss
      - sass
      - sass-embedded
      - stylus
      - sugarss
      - supports-color
      - terser
      - tsx
      - yaml

  vite@7.1.9(@types/node@20.19.20)(yaml@2.8.1):
    dependencies:
      esbuild: 0.25.10
      fdir: 6.5.0(picomatch@4.0.3)
      picomatch: 4.0.3
      postcss: 8.5.6
      rollup: 4.52.4
      tinyglobby: 0.2.15
    optionalDependencies:
      '@types/node': 20.19.20
      fsevents: 2.3.3
      yaml: 2.8.1

  vitest@3.2.4(@types/debug@4.1.12)(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1):
    dependencies:
      '@types/chai': 5.2.2
      '@vitest/expect': 3.2.4
      '@vitest/mocker': 3.2.4(vite@7.1.9(@types/node@20.19.20)(yaml@2.8.1))
      '@vitest/pretty-format': 3.2.4
      '@vitest/runner': 3.2.4
      '@vitest/snapshot': 3.2.4
      '@vitest/spy': 3.2.4
      '@vitest/utils': 3.2.4
      chai: 5.3.3
      debug: 4.4.3(supports-color@10.2.2)
      expect-type: 1.2.2
      magic-string: 0.30.19
      pathe: 2.0.3
      picomatch: 4.0.3
      std-env: 3.9.0
      tinybench: 2.9.0
      tinyexec: 0.3.2
      tinyglobby: 0.2.15
      tinypool: 1.1.1
      tinyrainbow: 2.0.0
      vite: 7.1.9(@types/node@20.19.20)(yaml@2.8.1)
      vite-node: 3.2.4(@types/node@20.19.20)(supports-color@10.2.2)(yaml@2.8.1)
      why-is-node-running: 2.3.0
    optionalDependencies:
      '@types/debug': 4.1.12
      '@types/node': 20.19.20
    transitivePeerDependencies:
      - jiti
      - less
      - lightningcss
      - msw
      - sass
      - sass-embedded
      - stylus
      - sugarss
      - supports-color
      - terser
      - tsx
      - yaml

  which@2.0.2:
    dependencies:
      isexe: 2.0.0

  why-is-node-running@2.3.0:
    dependencies:
      siginfo: 2.0.0
      stackback: 0.0.2

  word-wrap@1.2.5: {}

  wrap-ansi@7.0.0:
    dependencies:
      ansi-styles: 4.3.0
      string-width: 4.2.3
      strip-ansi: 6.0.1

  wrap-ansi@8.1.0:
    dependencies:
      ansi-styles: 6.2.3
      string-width: 5.1.2
      strip-ansi: 7.1.2

  wrap-ansi@9.0.2:
    dependencies:
      ansi-styles: 6.2.3
      string-width: 7.2.0
      strip-ansi: 7.1.2

  y18n@5.0.8: {}

  yaml@2.8.1: {}

  yargs-parser@21.1.1: {}

  yargs@17.7.2:
    dependencies:
      cliui: 8.0.1
      escalade: 3.2.0
      get-caller-file: 2.0.5
      require-directory: 2.1.1
      string-width: 4.2.3
      y18n: 5.0.8
      yargs-parser: 21.1.1

  yocto-queue@0.1.0: {}

```

## File: pnpm-workspace.yaml
```
packages:
  - tests

injectWorkspacePackages: false

onlyBuiltDependencies:
  - esbuild

```

## File: README.md
```
# concurrently

[![Latest Release](https://img.shields.io/github/v/release/open-cli-tools/concurrently?label=Release)](https://github.com/open-cli-tools/concurrently/releases)
[![License](https://img.shields.io/github/license/open-cli-tools/concurrently?label=License)](https://github.com/open-cli-tools/concurrently/blob/main/LICENSE)
[![Weekly Downloads on NPM](https://img.shields.io/npm/dw/concurrently?label=Downloads&logo=npm)](https://www.npmjs.com/package/concurrently)
[![CI Status](https://img.shields.io/github/actions/workflow/status/open-cli-tools/concurrently/test.yml?label=CI&logo=github)](https://github.com/open-cli-tools/concurrently/actions/workflows/test.yml)
[![Coverage Status](https://img.shields.io/coveralls/github/open-cli-tools/concurrently/main?label=Coverage&logo=coveralls)](https://coveralls.io/github/open-cli-tools/concurrently?branch=main)

Run multiple commands concurrently.
Like `npm run watch-js & npm run watch-less` but better.

![Demo](docs/demo.gif)

**Table of Contents**

- [concurrently](#concurrently)
  - [Why](#why)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API](#api)
    - [`concurrently(commands[, options])`](#concurrentlycommands-options)
    - [`Command`](#command)
    - [`CloseEvent`](#closeevent)
  - [FAQ](#faq)

## Why

I like [task automation with npm](https://web.archive.org/web/20220531064025/https://github.com/substack/blog/blob/master/npm_run.markdown)
but the usual way to run multiple commands concurrently is
`npm run watch-js & npm run watch-css`. That's fine but it's hard to keep
on track of different outputs. Also if one process fails, others still keep running
and you won't even notice the difference.

Another option would be to just run all commands in separate terminals. I got
tired of opening terminals and made **concurrently**.

**Features:**

- Cross platform (including Windows)
- Output is easy to follow with prefixes
- With `--kill-others` switch, all commands are killed if one dies

## Installation

**concurrently** can be installed in the global scope (if you'd like to have it available and use it on the whole system) or locally for a specific package (for example if you'd like to use it in the `scripts` section of your package):

|             | npm                     | Yarn                           | pnpm                       | Bun                       |
| ----------- | ----------------------- | ------------------------------ | -------------------------- | ------------------------- |
| **Global**  | `npm i -g concurrently` | `yarn global add concurrently` | `pnpm add -g concurrently` | `bun add -g concurrently` |
| **Local**\* | `npm i -D concurrently` | `yarn add -D concurrently`     | `pnpm add -D concurrently` | `bun add -d concurrently` |

<sub>\* It's recommended to add **concurrently** to `devDependencies` as it's usually used for developing purposes. Please adjust the command if this doesn't apply in your case.</sub>

## Usage

> **Note**
> The `concurrently` command is also available under the shorthand alias `conc`.

The tool is written in Node.js, but you can use it to run **any** commands.

Remember to surround separate commands with quotes:

```bash
concurrently 'command1 arg' 'command2 arg'
```

Otherwise **concurrently** would try to run 4 separate commands:
`command1`, `arg`, `command2`, `arg`.

> [!IMPORTANT]
> Windows only supports double quotes:
>
> ```bash
> concurrently "command1 arg" "command2 arg"
> ```
>
> Remember to escape the double quotes in your package.json when using Windows:
>
> ```json
> "start": "concurrently \"command1 arg\" \"command2 arg\""
> ```

You can always check concurrently's flag list by running `concurrently --help`.
For the version, run `concurrently --version`.

Check out documentation and other usage examples in the [`docs` directory](./docs/README.md).

## API

**concurrently** can be used programmatically by using the API documented below:

### `concurrently(commands[, options])`

- `commands`: an array of either strings (containing the commands to run) or objects
  with the shape `{ command, name, prefixColor, env, cwd, ipc }`.

- `options` (optional): an object containing any of the below:
  - `cwd`: the working directory to be used by all commands. Can be overridden per command.
    Default: `process.cwd()`.
  - `defaultInputTarget`: the default input target when reading from `inputStream`.
    Default: `0`.
  - `handleInput`: when `true`, reads input from `process.stdin`.
  - `inputStream`: a [`Readable` stream](https://nodejs.org/dist/latest-v10.x/docs/api/stream.html#stream_readable_streams)
    to read the input from. Should only be used in the rare instance you would like to stream anything other than `process.stdin`. Overrides `handleInput`.
  - `pauseInputStreamOnFinish`: by default, pauses the input stream (`process.stdin` when `handleInput` is enabled, or `inputStream` if provided) when all of the processes have finished. If you need to read from the input stream after `concurrently` has finished, set this to `false`. ([#252](https://github.com/kimmobrunfeldt/concurrently/issues/252)).
  - `killOthersOn`: once the first command exits with one of these statuses, kill other commands.
    Can be an array containing the strings `success` (status code zero) and/or `failure` (non-zero exit status).
  - `maxProcesses`: how many processes should run at once.
  - `outputStream`: a [`Writable` stream](https://nodejs.org/dist/latest-v10.x/docs/api/stream.html#stream_writable_streams)
    to write logs to. Default: `process.stdout`.
  - `prefix`: the prefix type to use when logging processes output.
    Possible values: `index`, `pid`, `time`, `command`, `name`, `none`, or a template (eg `[{time} process: {pid}]`).
    Default: the name of the process, or its index if no name is set.
  - `prefixColors`: a list of colors or a string as supported by [Chalk](https://www.npmjs.com/package/chalk) and additional style `auto` for an automatically picked color.
    If concurrently would run more commands than there are colors, the last color is repeated, unless if the last color value is `auto` which means following colors are automatically picked to vary.
    Prefix colors specified per-command take precedence over this list.
  - `prefixLength`: how many characters to show when prefixing with `command`. Default: `10`
  - `raw`: whether raw mode should be used, meaning strictly process output will
    be logged, without any prefixes, coloring or extra stuff. Can be overridden per command.
  - `successCondition`: the condition to consider the run was successful.
    If `first`, only the first process to exit will make up the success of the run; if `last`, the last process that exits will determine whether the run succeeds.
    Anything else means all processes should exit successfully.
  - `restartTries`: how many attempts to restart a process that dies will be made. Default: `0`.
  - `restartDelay`: how many milliseconds to wait between process restarts. Default: `0`.
  - `timestampFormat`: a [Unicode format](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table)
    to use when prefixing with `time`. Default: `yyyy-MM-dd HH:mm:ss.SSS`
  - `additionalArguments`: list of additional arguments passed that will get replaced in each command. If not defined, no argument replacing will happen.

> **Returns:** an object in the shape `{ result, commands }`.
>
> - `result`: a `Promise` that resolves if the run was successful (according to `successCondition` option),
>   or rejects, containing an array of [`CloseEvent`](#CloseEvent), in the order that the commands terminated.
> - `commands`: an array of all spawned [`Command`s](#Command).

Example:

```js
const concurrently = require('concurrently');
const { result } = concurrently(
  [
    'npm:watch-*',
    { command: 'nodemon', name: 'server' },
    { command: 'deploy', name: 'deploy', env: { PUBLIC_KEY: '...' } },
    {
      command: 'watch',
      name: 'watch',
      cwd: path.resolve(__dirname, 'scripts/watchers'),
    },
  ],
  {
    prefix: 'name',
    killOthersOn: ['failure', 'success'],
    restartTries: 3,
    cwd: path.resolve(__dirname, 'scripts'),
  },
);
result.then(success, failure);
```

### `Command`

An object that contains all information about a spawned command, and ways to interact with it.<br>
It has the following properties:

- `index`: the index of the command among all commands spawned.
- `command`: the command line of the command.
- `name`: the name of the command; defaults to an empty string.
- `cwd`: the current working directory of the command.
- `env`: an object with all the environment variables that the command will be spawned with.
- `killed`: whether the command has been killed.
- `state`: the command's state. Can be one of
  - `stopped`: if the command was never started
  - `started`: if the command is currently running
  - `errored`: if the command failed spawning
  - `exited`: if the command is not running anymore, e.g. it received a close event
- `pid`: the command's process ID.
- `stdin`: a Writable stream to the command's `stdin`.
- `stdout`: an RxJS observable to the command's `stdout`.
- `stderr`: an RxJS observable to the command's `stderr`.
- `error`: an RxJS observable to the command's error events (e.g. when it fails to spawn).
- `timer`: an RxJS observable to the command's timing events (e.g. starting, stopping).
- `stateChange`: an RxJS observable for changes to the command's `state` property.
- `messages`: an object with the following properties:
  - `incoming`: an RxJS observable for the IPC messages received from the underlying process.
  - `outgoing`: an RxJS observable for the IPC messages sent to the underlying process.

  Both observables emit [`MessageEvent`](#messageevent)s.<br>
  Note that if the command wasn't spawned with IPC support, these won't emit any values.

- `close`: an RxJS observable to the command's close events.
  See [`CloseEvent`](#CloseEvent) for more information.
- `start()`: starts the command and sets up all of the above streams
- `send(message[, handle, options])`: sends a message to the underlying process via IPC channels,
  returning a promise that resolves once the message has been sent.
  See [Node.js docs](https://nodejs.org/docs/latest/api/child_process.html#subprocesssendmessage-sendhandle-options-callback).
- `kill([signal])`: kills the command, optionally specifying a signal (e.g. `SIGTERM`, `SIGKILL`, etc).

### `MessageEvent`

An object that represents a message that was received from/sent to the underlying command process.<br>
It has the following properties:

- `message`: the message itself.
- `handle`: a [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket),
  [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver) or
  [`dgram.Socket`](https://nodejs.org/docs/latest/api/dgram.html#class-dgramsocket),
  if one was sent, or `undefined`.

### `CloseEvent`

An object with information about a command's closing event.<br>
It contains the following properties:

- `command`: a stripped down version of [`Command`](#command), including only `name`, `command`, `env` and `cwd` properties.
- `index`: the index of the command among all commands spawned.
- `killed`: whether the command exited because it was killed.
- `exitCode`: the exit code of the command's process, or the signal which it was killed with.
- `timings`: an object in the shape `{ startDate, endDate, durationSeconds }`.

## FAQ

- Process exited with code _null_?

  From [Node child_process documentation](http://nodejs.org/api/child_process.html#child_process_event_exit), `exit` event:

  > This event is emitted after the child process ends. If the process
  > terminated normally, code is the final exit code of the process,
  > otherwise null. If the process terminated due to receipt of a signal,
  > signal is the string name of the signal, otherwise null.

  So _null_ means the process didn't terminate normally. This will make **concurrently**
  to return non-zero exit code too.

- Does this work with the npm-replacements [yarn](https://yarnpkg.com/), [pnpm](https://pnpm.io/), or [Bun](https://bun.sh/)?

  Yes! In all examples above, you may replace "`npm`" with "`yarn`", "`pnpm`", or "`bun`".

```

## File: tsconfig.json
```
{
  "compilerOptions": {
    "lib": ["es2023"],
    "module": "node20",

    "outDir": "dist",
    "declaration": true,

    "strict": true,
    "skipLibCheck": true
  },
  "include": ["./bin", "./lib"]
}

```

## File: vitest.config.ts
```
import { defineConfig } from 'vitest/config';

export default defineConfig({
    test: {
        coverage: {
            include: ['lib/**/*.ts', '!lib/index.ts'],
            // lcov is used for coveralls
            reporter: ['text', 'html', 'lcov'],
        },
        projects: [
            {
                extends: true,
                test: {
                    name: 'unit',
                    include: ['{bin,lib}/**/*.spec.ts'],
                },
            },
            {
                extends: true,
                test: {
                    name: 'smoke',
                    include: ['tests/**/*.spec.ts'],
                },
            },
        ],
    },
});

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_concurrently_163559



================================================
FILE: .prettierrc.json
================================================
{
  "singleQuote": true
}


================================================
FILE: CONTRIBUTING.md
================================================
# Contributing

Pull requests and contributions are warmly welcome.
Please follow existing code style and commit message conventions. Also remember to keep documentation
updated.

**Pull requests:** You don't need to bump version numbers or modify anything related to releasing. That stuff is fully automated, just write the functionality.

# Maintaining

## Code Format & Linting

Code format and lint checks are performed locally when committing to ensure the changes align with the configured rules of this repository. This happens with the help of the tools [simple-git-hooks](https://github.com/toplenboren/simple-git-hooks) and [lint-staged](https://github.com/okonet/lint-staged) which are automatically installed and configured on `pnpm install` (no further steps required).

In case of problems, a corresponding message is displayed in your terminal.
Please fix them and then run the commit command again.

## Test

Tests can be executed with the following command:

```bash
pnpm test
```


================================================
FILE: eslint.config.js
================================================
// @ts-check

import eslint from '@eslint/js';
import pluginVitest from '@vitest/eslint-plugin';
import { defineConfig } from 'eslint/config';
import gitignore from 'eslint-config-flat-gitignore';
import pluginImportLite from 'eslint-plugin-import-lite';
import pluginPrettierRecommended from 'eslint-plugin-prettier/recommended';
import pluginSimpleImportSort from 'eslint-plugin-simple-import-sort';
import globals from 'globals';
import tseslint from 'typescript-eslint';

export default defineConfig(
    gitignore(),
    {
        languageOptions: {
            globals: {
                ...globals.node,
            },
            ecmaVersion: 2023,
        },
    },
    eslint.configs.recommended,
    tseslint.configs.recommended,
    {
        rules: {
            curly: 'error',
            eqeqeq: ['error', 'always', { null: 'ignore' }],
            'no-var': 'error',
            'no-console': 'error',
            'prefer-const': 'error',
            'prefer-object-spread': 'error',
            '@typescript-eslint/no-unused-vars': [
                'error',
                {
                    varsIgnorePattern: '^_',
                },
            ],
        },
    },
    { files: ['**/__fixtures__/**/*.{js,ts}'], rules: { 'no-console': 'off' } },
    {
        plugins: {
            'simple-import-sort': pluginSimpleImportSort,
            import: pluginImportLite,
        },
        rules: {
            'simple-import-sort/imports': 'error',
            'simple-import-sort/exports': 'error',
            'import/first': 'error',
            'import/newline-after-import': 'error',
            'import/no-duplicates': 'error',
        },
    },
    {
        files: ['**/*.spec.ts'],
        plugins: {
            vitest: pluginVitest,
        },
        rules: {
            ...pluginVitest.configs.recommended.rules,
            // Currently produces false positives, see https://github.com/vitest-dev/eslint-plugin-vitest/issues/775
            'vitest/prefer-called-exactly-once-with': 'off',
        },
    },
    pluginPrettierRecommended,
);


================================================
FILE: package.json
================================================
{
  "name": "concurrently",
  "type": "module",
  "version": "9.2.1",
  "packageManager": "pnpm@10.18.2+sha512.9fb969fa749b3ade6035e0f109f0b8a60b5d08a1a87fdf72e337da90dcc93336e2280ca4e44f2358a649b83c17959e9993e777c2080879f3801e6f0d999ad3dd",
  "description": "Run commands concurrently",
  "author": "Kimmo Brunfeldt",
  "license": "MIT",
  "funding": "https://github.com/open-cli-tools/concurrently?sponsor=1",
  "repository": {
    "type": "git",
    "url": "https://github.com/open-cli-tools/concurrently.git"
  },
  "keywords": [
    "bash",
    "concurrent",
    "parallel",
    "concurrently",
    "command",
    "sh"
  ],
  "exports": {
    ".": "./dist/lib/index.js",
    "./package.json": "./package.json"
  },
  "types": "./dist/lib/index.d.ts",
  "publishConfig": {
    "bin": {
      "concurrently": "./dist/bin/index.js",
      "conc": "./dist/bin/index.js"
    }
  },
  "files": [
    "!**/*.spec.d.ts",
    "!**/*.spec.js",
    "!**/__fixtures__",
    "dist",
    "dist/tsconfig.tsbuildinfo",
    "docs"
  ],
  "engines": {
    "node": ">=20"
  },
  "scripts": {
    "build": "tsc --build",
    "postbuild": "chmod +x dist/bin/index.js",
    "typecheck": "tsc --noEmit",
    "format": "prettier --check '**/*.{json,y?(a)ml,md}'",
    "lint": "eslint",
    "prepublishOnly": "safe-publish-latest && pnpm run build",
    "test": "vitest --project unit",
    "test:smoke": "vitest run --project smoke",
    "prepare": "husky"
  },
  "dependencies": {
    "chalk": "5.6.2",
    "rxjs": "7.8.2",
    "shell-quote": "1.8.3",
    "supports-color": "10.2.2",
    "tree-kill": "1.2.2",
    "yargs": "17.7.2"
  },
  "devDependencies": {
    "@eslint/js": "^9.37.0",
    "@hirez_io/observer-spy": "^2.2.0",
    "@types/node": "^20.19.20",
    "@types/shell-quote": "^1.7.5",
    "@types/yargs": "^17.0.33",
    "@vitest/coverage-v8": "^3.2.4",
    "@vitest/eslint-plugin": "^1.3.16",
    "ctrlc-wrapper": "^0.0.5",
    "esbuild": "~0.25.10",
    "eslint": "^9.37.0",
    "eslint-config-flat-gitignore": "^2.1.0",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-import-lite": "^0.3.0",
    "eslint-plugin-prettier": "^5.5.4",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "globals": "^16.4.0",
    "husky": "^9.1.7",
    "lint-staged": "^16.2.3",
    "prettier": "^3.6.2",
    "safe-publish-latest": "^2.0.0",
    "string-argv": "^0.3.2",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.46.0",
    "vitest": "^3.2.4"
  },
  "lint-staged": {
    "*.{js,ts}": "eslint --fix",
    "*.{json,y?(a)ml,md}": "prettier --write"
  }
}


================================================
FILE: README.md
================================================
# concurrently

[![Latest Release](https://img.shields.io/github/v/release/open-cli-tools/concurrently?label=Release)](https://github.com/open-cli-tools/concurrently/releases)
[![License](https://img.shields.io/github/license/open-cli-tools/concurrently?label=License)](https://github.com/open-cli-tools/concurrently/blob/main/LICENSE)
[![Weekly Downloads on NPM](https://img.shields.io/npm/dw/concurrently?label=Downloads&logo=npm)](https://www.npmjs.com/package/concurrently)
[![CI Status](https://img.shields.io/github/actions/workflow/status/open-cli-tools/concurrently/test.yml?label=CI&logo=github)](https://github.com/open-cli-tools/concurrently/actions/workflows/test.yml)
[![Coverage Status](https://img.shields.io/coveralls/github/open-cli-tools/concurrently/main?label=Coverage&logo=coveralls)](https://coveralls.io/github/open-cli-tools/concurrently?branch=main)

Run multiple commands concurrently.
Like `npm run watch-js & npm run watch-less` but better.

![Demo](docs/demo.gif)

**Table of Contents**

- [concurrently](#concurrently)
  - [Why](#why)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API](#api)
    - [`concurrently(commands[, options])`](#concurrentlycommands-options)
    - [`Command`](#command)
    - [`CloseEvent`](#closeevent)
  - [FAQ](#faq)

## Why

I like [task automation with npm](https://web.archive.org/web/20220531064025/https://github.com/substack/blog/blob/master/npm_run.markdown)
but the usual way to run multiple commands concurrently is
`npm run watch-js & npm run watch-css`. That's fine but it's hard to keep
on track of different outputs. Also if one process fails, others still keep running
and you won't even notice the difference.

Another option would be to just run all commands in separate terminals. I got
tired of opening terminals and made **concurrently**.

**Features:**

- Cross platform (including Windows)
- Output is easy to follow with prefixes
- With `--kill-others` switch, all commands are killed if one dies

## Installation

**concurrently** can be installed in the global scope (if you'd like to have it available and use it on the whole system) or locally for a specific package (for example if you'd like to use it in the `scripts` section of your package):

|             | npm                     | Yarn                           | pnpm                       | Bun                       |
| ----------- | ----------------------- | ------------------------------ | -------------------------- | ------------------------- |
| **Global**  | `npm i -g concurrently` | `yarn global add concurrently` | `pnpm add -g concurrently` | `bun add -g concurrently` |
| **Local**\* | `npm i -D concurrently` | `yarn add -D concurrently`     | `pnpm add -D concurrently` | `bun add -d concurrently` |

<sub>\* It's recommended to add **concurrently** to `devDependencies` as it's usually used for developing purposes. Please adjust the command if this doesn't apply in your case.</sub>

## Usage

> **Note**
> The `concurrently` command is also available under the shorthand alias `conc`.

The tool is written in Node.js, but you can use it to run **any** commands.

Remember to surround separate commands with quotes:

```bash
concurrently 'command1 arg' 'command2 arg'
```

Otherwise **concurrently** would try to run 4 separate commands:
`command1`, `arg`, `command2`, `arg`.

> [!IMPORTANT]
> Windows only supports double quotes:
>
> ```bash
> concurrently "command1 arg" "command2 arg"
> ```
>
> Remember to escape the double quotes in your package.json when using Windows:
>
> ```json
> "start": "concurrently \"command1 arg\" \"command2 arg\""
> ```

You can always check concurrently's flag list by running `concurrently --help`.
For the version, run `concurrently --version`.

Check out documentation and other usage examples in the [`docs` directory](./docs/README.md).

## API

**concurrently** can be used programmatically by using the API documented below:

### `concurrently(commands[, options])`

- `commands`: an array of either strings (containing the commands to run) or objects
  with the shape `{ command, name, prefixColor, env, cwd, ipc }`.

- `options` (optional): an object containing any of the below:
  - `cwd`: the working directory to be used by all commands. Can be overridden per command.
    Default: `process.cwd()`.
  - `defaultInputTarget`: the default input target when reading from `inputStream`.
    Default: `0`.
  - `handleInput`: when `true`, reads input from `process.stdin`.
  - `inputStream`: a [`Readable` stream](https://nodejs.org/dist/latest-v10.x/docs/api/stream.html#stream_readable_streams)
    to read the input from. Should only be used in the rare instance you would like to stream anything other than `process.stdin`. Overrides `handleInput`.
  - `pauseInputStreamOnFinish`: by default, pauses the input stream (`process.stdin` when `handleInput` is enabled, or `inputStream` if provided) when all of the processes have finished. If you need to read from the input stream af

================================================
FILE: tsconfig.json
================================================
{
  "compilerOptions": {
    "lib": ["es2023"],
    "module": "node20",

    "outDir": "dist",
    "declaration": true,

    "strict": true,
    "skipLibCheck": true
  },
  "include": ["./bin", "./lib"]
}


================================================
FILE: vitest.config.ts
================================================
import { defineConfig } from 'vitest/config';

export default defineConfig({
    test: {
        coverage: {
            include: ['lib/**/*.ts', '!lib/index.ts'],
            // lcov is used for coveralls
            reporter: ['text', 'html', 'lcov'],
        },
        projects: [
            {
                extends: true,
                test: {
                    name: 'unit',
                    include: ['{bin,lib}/**/*.spec.ts'],
                },
            },
            {
                extends: true,
                test: {
                    name: 'smoke',
                    include: ['tests/**/*.spec.ts'],
                },
            },
        ],
    },
});


================================================
FILE: .vscode\extensions.json
================================================
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "editorconfig.editorconfig",
    "vitest.explorer"
  ]
}


================================================
FILE: .vscode\settings.json
================================================
{
  // For contributors with the Jest extension installed,
  // it might incorrectly report errors in the suite
  "jest.enable": false,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  },
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[javascript, typescript]": {
    "editor.formatOnSave": false
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "editor.rulers": [100]
}


================================================
FILE: bin\index.spec.ts
================================================
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import readline from 'node:readline';

import { subscribeSpyTo } from '@hirez_io/observer-spy';
import { sendCtrlC, spawnWithWrapper } from 'ctrlc-wrapper';
import { build } from 'esbuild';
import Rx from 'rxjs';
import { map } from 'rxjs/operators';
import stringArgv from 'string-argv';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { escapeRegExp } from '../lib/utils.js';

const isWindows = process.platform === 'win32';
const createKillMessage = (prefix: string, signal: 'SIGTERM' | 'SIGINT' | string) => {
    const map: Record<string, string | number> = {
        SIGTERM: isWindows ? 1 : '(SIGTERM|143)',
        // Could theoretically be anything (e.g. 0) if process has SIGINT handler
        SIGINT: isWindows ? '(3221225786|0)' : '(SIGINT|130|0)',
    };
    return new RegExp(`${escapeRegExp(prefix)} exited with code ${map[signal] ?? signal}`);
};

let tmpDir: string;

beforeAll(async () => {
    // Build 'concurrently' and store it in a temporary directory
    tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'concurrently-'));
    await build({
        entryPoints: [path.join(__dirname, 'index.ts')],
        platform: 'node',
        bundle: true,
        // it doesn't seem like esbuild is able to change a CJS module to ESM, so target CJS instead.
        // https://github.com/evanw/esbuild/issues/1921
        format: 'cjs',
        outfile: path.join(tmpDir, 'concurrently.cjs'),
    });
    fs.copyFileSync(path.join(__dirname, '..', 'package.json'), path.join(tmpDir, 'package.json'));
}, 8000);

afterAll(() => {
    // Remove the temporary directory where 'concurrently' was stored
    if (tmpDir) {
        fs.rmSync(tmpDir, { recursive: true });
    }
});

/**
 * Creates a child process running 'concurrently' with the given args.
 * Returns observables for its combined stdout + stderr output, close events, pid, and stdin stream.
 */
const run = (args: string, ctrlcWrapper?: boolean) => {
    const spawnFn = ctrlcWrapper ? spawnWithWrapper : spawn;
    const child = spawnFn('node', [path.join(tmpDir, 'concurrently.cjs'), ...stringArgv(args)], {
        cwd: __dirname,
        env: {
            ...process.env,
        },
    });

    const stdout = readline.createInterface({
        input: child.stdout,
    });

    const stderr = readline.createInterface({
        input: child.stderr,
    });

    const log = new Rx.Observable<string>((observer) => {
        stdout.on('line', (line) => {
            observer.next(line);
        });

        stderr.on('line', (line) => {
            observer.next(line);
        });

        child.on('close', () => {
            observer.complete();
        });
    });

    const exit = Rx.firstValueFrom(
        Rx.fromEvent(child, 'exit').pipe(
            map((event) => {
                const exit = event as [number | null, NodeJS.Signals | null];
                return {
                    /** The exit code if the child exited on its own. */
                    code: exit[0],
                    /** The signal by which the child process was terminated. */
                    signal: exit[1],
                };
            }),
        ),
    );

    const getLogLines = async (): Promise<string[]> => {
        const observerSpy = subscribeSpyTo(log);
        await observerSpy.onComplete();
        observerSpy.unsubscribe();
        return observerSpy.getValues();
    };

    return {
        process: child,
        stdin: child.stdin,
        pid: child.pid,
        log,
        getLogLines,
        exit,
    };
};

it('has help command', async () => {
    const exit = await run('--help').exit;

    expect(exit.code).toBe(0);
});

it('prints help when no arguments are passed', async () => {
    const exit = await run('').exit;
    expect(exit.code).toBe(0);
});

describe('has version command', () => {
    const pkg = fs.readFileSync(path.join(__dirname, '..', 'package.json'), 'utf-8');
    const { version } = JSON.parse(pkg);

    it.each(['--version', '-V', '-v'])('%s', async (arg) => {
        const child = run(arg);
        const log = await child.getLogLines();
        expect(log).toContain(version);

        const { code } = await child.exit;
        expect(code).toBe(0);
    });
});

describe('exiting conditions', () => {
    it('is of success by default when running successful commands', async () => {
        const exit = await run('"echo foo" "echo bar"').exit;

        expect(exit.code).toBe(0);
    });

    it('is of failure by default when one of the command fails', async () => {
        const exit = await run('"echo foo" "exit 1"').exit;

        expect(exit.code).toBeGreaterThan(0);
    });

    it('is of success when --success=first and first command to exit succeeds', async () => {
        const exit = await run(
            '--success=first "echo foo" "node __fixtures__/sleep.js 0.5 && exit 1"',
     

================================================
FILE: bin\index.ts
================================================
#!/usr/bin/env node
import process from 'node:process';

import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

import { assertDeprecated } from '../lib/assert.js';
import * as defaults from '../lib/defaults.js';
import { concurrently } from '../lib/index.js';
import { castArray } from '../lib/utils.js';
import { readPackageJson } from './read-package-json.js';

const version = String(readPackageJson().version);
const epilogue = `For documentation and more examples, visit:\nhttps://github.com/open-cli-tools/concurrently/tree/v${version}/docs`;

// Clean-up arguments (yargs expects only the arguments after the program name)
const program = yargs(hideBin(process.argv))
    .parserConfiguration({
        // Avoids options that can be specified multiple times from requiring a `--` to pass commands
        'greedy-arrays': false,
        // Makes sure that --passthrough-arguments works correctly
        'populate--': true,
    })
    .usage('$0 [options] <command ...>')
    .help('h')
    .alias('h', 'help')
    .version(version)
    .alias('version', 'v')
    .alias('version', 'V')
    // TODO: Add some tests for this.
    .env('CONCURRENTLY')
    .options({
        // General
        'max-processes': {
            alias: 'm',
            describe:
                'How many processes should run at once.\n' +
                'New processes only spawn after all restart tries of a process.\n' +
                'Exact number or a percent of CPUs available (for example "50%")',
            type: 'string',
        },
        names: {
            alias: 'n',
            describe:
                'List of custom names to be used in prefix template.\n' +
                'Example names: "main,browser,server"',
            type: 'string',
        },
        'name-separator': {
            describe:
                'The character to split <names> on. Example usage:\n' +
                '-n "styles|scripts|server" --name-separator "|"',
            default: defaults.nameSeparator,
        },
        success: {
            alias: 's',
            describe:
                'Which command(s) must exit with code 0 in order for concurrently exit with ' +
                'code 0 too. Options are:\n' +
                '- "first" for the first command to exit;\n' +
                '- "last" for the last command to exit;\n' +
                '- "all" for all commands;\n' +
                // Note: not a typo. Multiple commands can have the same name.
                '- "command-{name}"/"command-{index}" for the commands with that name or index;\n' +
                '- "!command-{name}"/"!command-{index}" for all commands but the ones with that ' +
                'name or index.\n',
            default: defaults.success,
        },
        raw: {
            alias: 'r',
            describe:
                'Output only raw output of processes, disables prettifying ' +
                'and concurrently coloring.',
            type: 'boolean',
        },
        // This one is provided for free. Chalk reads this itself and removes colors.
        // https://www.npmjs.com/package/chalk#supportscolor
        'no-color': {
            describe: 'Disables colors from logging',
            type: 'boolean',
        },
        hide: {
            describe:
                'Comma-separated list of processes to hide the output.\n' +
                'The processes can be identified by their name or index.',
            default: defaults.hide,
            type: 'string',
        },
        group: {
            alias: 'g',
            describe: 'Order the output as if the commands were run sequentially.',
            type: 'boolean',
        },
        timings: {
            describe: 'Show timing information for all processes.',
            type: 'boolean',
            default: defaults.timings,
        },
        'passthrough-arguments': {
            alias: 'P',
            describe:
                'Passthrough additional arguments to commands (accessible via placeholders) ' +
                'instead of treating them as commands.',
            type: 'boolean',
            default: defaults.passthroughArguments,
        },
        teardown: {
            describe:
                'Clean up command(s) to execute before exiting concurrently. Might be specified multiple times.\n' +
                "These aren't prefixed and they don't affect concurrently's exit code.",
            type: 'string',
            array: true,
        },

        // Kill others
        'kill-others': {
            alias: 'k',
            describe: 'Kill other processes once the first exits.',
            type: 'boolean',
        },
        'kill-others-on-fail': {
            describe: 'Kill other processes if one exits with non zero status code.',
            type: 'boolean',
        },
        'kill-signal': {
            alias: 'ks',
            describe:
                'Signal to send to other processes if one exits or dies. (SIGTERM/SIGKILL, defau

================================================
FILE: bin\read-package-json.ts
================================================
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';

/**
 * Read the package.json file of `concurrently`
 */
export function readPackageJson(): Record<string, unknown> {
    let resolver;
    try {
        resolver = require.resolve;
    } catch {
        resolver = createRequire(import.meta.url).resolve;
    }
    const path = resolver('concurrently/package.json');
    const content = readFileSync(path, 'utf8');
    return JSON.parse(content);
}


================================================
FILE: bin\__fixtures__\read-echo.js
================================================
import process from 'node:process';

process.stdin.on('data', (chunk) => {
    const line = chunk.toString().trim();
    console.log(line);

    if (line === 'stop') {
        process.exit(0);
    }
});

console.log('READING');


================================================
FILE: bin\__fixtures__\sleep.js
================================================
/*
 * Platform independent implementation of 'sleep' used as a command in tests
 *
 * (Windows doesn't provide the 'sleep' command by default,
 * see https://github.com/open-cli-tools/concurrently/issues/277)
 */
import process from 'node:process';

const seconds = +process.argv[2];
if (!seconds || Number.isNaN(seconds) || process.argv.length > 3) {
    // Mimic behavior from native 'sleep' command
    console.error('usage: sleep seconds');
    process.exit(1);
}

await new Promise((resolve) => setTimeout(resolve, seconds * 1000));


================================================
FILE: docs\README.md
================================================
# Concurrently Documentation

## CLI

These articles cover using concurrently through CLI:

- [Prefixing](./cli/prefixing.md)
- [Output Control](./cli/output-control.md)
- [Success Conditions](./cli/success.md)
- [Shortcuts](./cli/shortcuts.md)
- [Terminating Commands](./cli/terminating.md)
- [Restarting Commands](./cli/restarting.md)
- [Input Handling](./cli/input-handling.md)
- [Passthrough Arguments](./cli/passthrough-arguments.md)
- [Configuration](./cli/configuration.md)


================================================
FILE: docs\cli\configuration.md
================================================
# Configuration

You might want to configure concurrently to always have certain flags on.
Any of concurrently's flags can be set via environment variables that are prefixed with `CONCURRENTLY_`.

```bash
$ export CONCURRENTLY_KILL_OTHERS=true
$ export CONCURRENTLY_HANDLE_INPUT=true
# Equivalent to passing --kill-others and --handle-input
$ concurrently nodemon "echo 'hey nodemon, you won't last long'"
```


================================================
FILE: docs\cli\input-handling.md
================================================
# Input Handling

By default, concurrently doesn't send input to any commands it spawns.<br/>
In the below example, typing `rs` to manually restart [nodemon](https://nodemon.io/) does nothing:

```bash
$ concurrently 'nodemon' 'npm run watch-js'
rs
```

To turn on input handling, it's necessary to set the `--handle-input`/`-i` flag.<br/>
This will send `rs` to the first command:

```bash
$ concurrently --handle-input 'nodemon' 'npm run watch-js'
rs
```

To send input to a different command instead, it's possible to prefix the input with the command index, followed by a `:`.<br/>
For example, the below sends `rs` to the second command:

```bash
$ concurrently --handle-input 'npm run watch-js' 'nodemon'
1:rs
```

If the command has a name, it's also possible to target it using that command's name:

```bash
$ concurrently --handle-input --names js,server 'npm run watch-js' 'nodemon'
server:rs
```

It's also possible to change the default command that receives input.<br/>
To do this, set the `--default-input-target` flag to a command's index or name.

```bash
$ concurrently --handle-input --default-input-target 1 'npm run watch-js' 'nodemon'
rs
```


================================================
FILE: docs\cli\output-control.md
================================================
# Output Control

concurrently offers a few ways to control a command's output.

## Hiding

A command's outputs (and all its events) can be hidden by using the `--hide` flag.

```bash
$ concurrently --hide 0 'echo Hello there' 'echo General Kenobi!'
[1] General Kenobi!
[1] echo 'General Kenobi!' exited with code 0
```

## Grouping

It might be useful at times to make sure that the commands outputs are grouped together, while running them in parallel.<br/>
This can be done with the `--group` flag.

```bash
$ concurrently --group 'echo Hello there && sleep 2 && echo General Kenobi!' 'echo hi Star Wars fans'
[0] Hello there
[0] General Kenobi!
[0] echo Hello there && sleep 2 && echo 'General Kenobi!' exited with code 0
[1] hi Star Wars fans
[1] echo hi Star Wars fans exited with code 0
```

## No Colors

When piping concurrently's outputs to another command or file, you might want to force it to not use colors, as these can break the other command's parsing, or reduce the legibility of the output in non-terminal environments.

```bash
$ concurrently -c red,blue --no-color 'echo Hello there' 'echo General Kenobi!'
```


================================================
FILE: docs\cli\passthrough-arguments.md
================================================
# Passthrough Arguments

If you have a shortcut for running a specific combination of commands through concurrently,
you might need at some point to pass additional arguments/flags to some of these.

For example, imagine you have in your `package.json` file scripts like this:

```jsonc
{
  // ...
  "scripts": {
    "build:client": "tsc -p client",
    "build:server": "tsc -p server",
    "build": "concurrently npm:build:client npm:build:server",
  },
}
```

If you wanted to run only either `build:server` or `build:client` with an additional `--noEmit` flag,
you can do so with `npm run build:server -- --noEmit`, for example.<br/>
However, if you want to do that while using concurrently, as `npm run build -- --noEmit` for example,
you might find that concurrently actually parses `--noEmit` as its own flag, which does nothing,
because it doesn't exist.

To solve this, you can set the `--passthrough-arguments`/`-P` flag, which instructs concurrently to
take everything after a `--` as additional arguments that are passed through to the input commands
via a few placeholder styles:

## Single argument

We can modify the original `build` script to pass a single additional argument/flag to a script by using
a 1-indexed `{number}` placeholder to the command you want it to apply to:

```jsonc
{
  // ...
  "scripts": {
    // ...
    "build": "concurrently -P 'npm:build:client -- {1}' npm:build:server --",
    "typecheck": "npm run build -- --noEmit",
  },
}
```

With this, running `npm run typecheck` will pass `--noEmit` only to `npm run build:client`.

## All arguments

In the original `build` example script, you're more likely to want to pass every additional argument/flag
to your commands. This can be done with the `{@}` placeholder.

```jsonc
{
  // ...
  "scripts": {
    // ...
    "build": "concurrently -P 'npm:build:client -- {@}' 'npm:build:server -- {@}' --",
    "typecheck": "npm run build -- --watch --noEmit",
  },
}
```

In the above example, both `--watch` and `--noEmit` are passed to each command.

## All arguments, combined

If for some reason you wish to combine all additional arguments into a single one, you can do that with the `{*}` placeholder,
which wraps the arguments in quotes.

```jsonc
{
  // ...
  "scripts": {
    // ...
    "build": "concurrently -P 'npm:build:client -- --outDir {*}/client' 'npm:build:server -- --outDir {*}/server' -- $(date)",
  },
}
```

In the above example, the output of the `date` command, which looks like `Sun  1 Sep 2024 23:50:00 AEST` will be passed as a single string to the `--outDir` parameter of both commands.


================================================
FILE: docs\cli\prefixing.md
================================================
# Prefixing

## Prefix Styles

concurrently will by default prefix each command's outputs with a zero-based index, wrapped in square brackets:

```bash
$ concurrently 'echo Hello there' "echo 'General Kenobi!'"
[0] Hello there
[1] General Kenobi!
[0] echo Hello there exited with code 0
[1] echo 'General Kenobi!' exited with code 0
```

If you've given the commands names, they are used instead:

```bash
$ concurrently --names one,two 'echo Hello there' "echo 'General Kenobi!'"
[one] Hello there
[two] General Kenobi!
[one] echo Hello there exited with code 0
[two] echo 'General Kenobi!' exited with code 0
```

There are other prefix styles available too:

| Style     | Description                       |
| --------- | --------------------------------- |
| `index`   | Zero-based command's index        |
| `name`    | The command's name                |
| `command` | The command's line                |
| `time`    | Time of output                    |
| `pid`     | ID of the command's process (PID) |
| `none`    | No prefix                         |

Any of these can be used by setting the `--prefix`/`-p` flag. For example:

```bash
$ concurrently --prefix pid 'echo Hello there' 'echo General Kenobi!'
[2222] Hello there
[2223] General Kenobi!
[2222] echo Hello there exited with code 0
[2223] echo 'General Kenobi!' exited with code 0
```

It's also possible to have a prefix based on a template. Any of the styles listed above can be used by wrapping it in `{}`.
Doing so will also remove the square brackets:

```bash
$ concurrently --prefix '{index}-{pid}' 'echo Hello there' 'echo General Kenobi!'
0-2222 Hello there
1-2223 General Kenobi!
0-2222 echo Hello there exited with code 0
1-2223 echo 'General Kenobi!' exited with code 0
```

## Prefix Colors

By default, there are no colors applied to concurrently prefixes, and they just use whatever the terminal's defaults are.

This can be changed by using the `--prefix-colors`/`-c` flag, which takes a comma-separated list of colors to use.<br/>
The available values are color names (e.g. `green`, `magenta`, `gray`, etc), a hex value (such as `#23de43`), or `auto`, to automatically select a color.

```bash
$ concurrently -c red,blue 'echo Hello there' 'echo General Kenobi!'
```

<details>
<summary>List of available color names</summary>

- `black`
- `blue`
- `cyan`
- `green`
- `gray`
- `magenta`
- `red`
- `white`
- `yellow`
</details>

Colors can take modifiers too. Several can be applied at once by appending `.<modifier 1>.<modifier 2>` and so on.

```bash
$ concurrently -c '#23de43.inverse,bold.blue.dim' 'echo Hello there' 'echo General Kenobi!'
```

<details>
<summary>List of available modifiers</summary>

- `reset`
- `bold`
- `dim`
- `hidden`
- `inverse`
- `italic`
- `strikethrough`
- `underline`
</details>

A background color can be set in a similarly fashion.

```bash
$ concurrently -c bgGray,red.bgBlack 'echo Hello there' 'echo General Kenobi!'
```

<details>
<summary>List of available background color names</summary>

- `bgBlack`
- `bgBlue`
- `bgCyan`
- `bgGreen`
- `bgGray`
- `bgMagenta`
- `bgRed`
- `bgWhite`
- `bgYellow`
</details>

## Prefix Length

When using the `command` prefix style, it's possible that it'll be too long.<br/>
It can be limited by setting the `--prefix-length`/`-l` flag:

```bash
$ concurrently -p command -l 10 'echo Hello there' 'echo General Kenobi!'
[echo..here] Hello there
[echo..bi!'] General Kenobi!
[echo..here] echo Hello there exited with code 0
[echo..bi!'] echo 'General Kenobi!' exited with code 0
```

It's also possible that some prefixes are too short, and you want all of them to have the same length.<br/>
This can be done by setting the `--pad-prefix` flag:

```bash
$ concurrently -n foo,barbaz --pad-prefix 'echo Hello there' 'echo General Kenobi!'
[foo   ] Hello there
[foo   ] echo Hello there exited with code 0
[barbaz] General Kenobi!
[barbaz] echo 'General Kenobi!' exited with code 0
```

> [!NOTE]
> If using the `pid` prefix style in combination with [`--restart-tries`](./restarting.md), the length of the PID might grow, in which case all subsequent lines will match the new length.<br/>
> This might happen, for example, if the PID was 99 and it's now 100.


================================================
FILE: docs\cli\restarting.md
================================================
# Restarting Commands

Sometimes it's useful to have commands that exited with a non-zero status to restart automatically.<br/>
concurrently lets you configure how many times you wish for such a command to restart through the `--restart-tries` flag:

```bash
$ concurrently --restart-tries 2 'exit 1'
[0] exit 1 exited with code 1
[0] exit 1 restarted
[0] exit 1 exited with code 1
[0] exit 1 restarted
[0] exit 1 exited with code 1
```

Sometimes, it might be interesting to have commands wait before restarting.<br/>
To do this, simply set `--restart-after` to a the number of milliseconds you'd like to delay restarting.

```bash
$ concurrently -p time --restart-tries 1 --restart-after 3000 'exit 1'
[2024-09-01 23:43:55.871] exit 1 exited with code 1
[2024-09-01 23:43:58.874] exit 1 restarted
[2024-09-01 23:43:58.891] exit 1 exited with code 1
```

If a command is not having success spawning, you might want to instead apply an exponential back-off.<br/>
Set `--restart-after exponential` to have commands respawn with a `2^N` seconds delay.

```bash
$ concurrently -p time --restart-tries 3 --restart-after exponential 'exit 1'

[2024-09-01 23:49:01.124] exit 1 exited with code 1
[2024-09-01 23:49:02.127] exit 1 restarted
[2024-09-01 23:49:02.139] exit 1 exited with code 1
[2024-09-01 23:49:04.141] exit 1 restarted
[2024-09-01 23:49:04.157] exit 1 exited with code 1
[2024-09-01 23:49:08.158] exit 1 restarted
[2024-09-01 23:49:08.174] exit 1 exited with code 1
```


================================================
FILE: docs\cli\shortcuts.md
================================================
# Command Shortcuts

Package managers that execute scripts from a `package.json` or `deno.(json|jsonc)` file can be shortened when in concurrently.<br/>
The following are supported:

| Syntax          | Expands to            |
| --------------- | --------------------- |
| `npm:<script>`  | `npm run <script>`    |
| `pnpm:<script>` | `pnpm run <script>`   |
| `yarn:<script>` | `yarn run <script>`   |
| `bun:<script>`  | `bun run <script>`    |
| `node:<script>` | `node --run <script>` |
| `deno:<script>` | `deno task <script>`  |

> [!NOTE]
>
> `node --run` is only available from [Node 22 onwards](https://nodejs.org/en/blog/announcements/v22-release-announce#running-packagejson-scripts).

For example, given the following `package.json` contents:

```jsonc
{
  // ...
  "scripts": {
    "lint:js": "...",
    "lint:ts": "...",
    "lint:fix:js": "...",
    "lint:fix:ts": "...",
    // ...
  },
  // ...
}
```

It's possible to run some of these with the following command line:

```bash
$ concurrently 'pnpm:lint:js'
# Is equivalent to
$ concurrently -n lint:js 'pnpm run lint:js'
```

Note that the command automatically receives a name equal to the script name.

If you have several scripts with similar name patterns, you can use the `*` wildcard to run all of them at once.<br/>
The spawned commands will receive names set to whatever the `*` wildcard matched.

```bash
$ concurrently 'npm:lint:fix:*'
# is equivalent to
$ concurrently -n js,ts 'npm run lint:fix:js' 'npm run lint:fix:ts'
```

If you specify a command name when using wildcards, it'll be a prefix of what the `*` wildcard matched:

```bash
$ concurrently -n fix: 'npm:lint:fix:*'
# is equivalent to
$ concurrently -n fix:js,fix:ts 'npm run lint:fix:js' 'npm run lint:fix:ts'
```

Filtering out commands matched by wildcard is also possible. Do this with by including `(!<some pattern>)` in the command line:

```bash
$ concurrently 'yarn:lint:*(!fix)'
# is equivalent to
$ concurrently -n js,ts 'yarn run lint:js' 'yarn run lint:ts'
```

> [!NOTE]
> If you use this syntax with double quotes (`"`), bash and other shells might fail
> parsing it. You'll need to escape the `!`, or use single quote (`'`) instead.<br/>
> See [here](https://serverfault.com/a/208266/160539) for more information.


================================================
FILE: docs\cli\success.md
================================================
# Success Conditions

When you're using concurrently in shell scripts or CI pipelines, the exit code matters.  
It determines whether the next step runs, or if the script stops with a failure.

You can control concurrently's exit code using the `--success` flag.  
This tells it **which command(s)** must succeed (exit with code `0`) for concurrently to return success overall.

There are several possible values:

## `all`

All commands must exit with code `0`.
This is the default value.

## `first`

The first command to exit must do so with code `0`.

```bash
# ✅ Exits with code 0 — second command exits first and succeeds
$ concurrently --success first 'sleep 1 && exit 1' 'exit 0'

# ❌ Exits with a non-zero code — second command exits first, but with code 1
$ concurrently --success first 'sleep 1 && exit 0' 'exit 1'
```

## `last`

The last command to exit must do so with code `0`.

```bash
# ✅ Exits with code 0 - first command exits last and succeeds
$ concurrently --success last 'sleep 1 && exit 0' 'exit 1'

# ❌ Exits with a non-zero code — first command exits last, but with code 1
$ concurrently --success last 'sleep 1 && exit 1' 'exit 0'
```

## `command-{name}` or `command-{index}`

A specific command, by name or index, must exit with code `0`.

```bash
# Exits with code 0 only if 'npm test' (index 1) passes.
$ concurrently --success command-1 --kill-others 'npm run server' 'npm test'

# Exits with code 0 only if 'test' command passes.
$ concurrently --success command-test --names server,test --kill-others \
    'npm start' \
    'npm test'
```

> [!TIP]
> Use `--kill-others` to kill a long-running process, such as a server, once tests pass.

## `!command-{name}` or `!command-{index}`

All but a specific command, by name or index, must exit with code `0`.

```bash
# Ignores 'npm start'; all others must succeed
$ concurrently --success '!command-2' --kill-others \
    'npm test' \
    'npm build' \
    'npm start'

# Ignores 'server'; all others must succeed
$ concurrently --success '!command-server' --names test,build,server --kill-others \
    'npm test' \
    'npm build' \
    'npm start'
```


================================================
FILE: docs\cli\terminating.md
================================================
# Terminating Commands

It's possible to have concurrently terminate other commands when one of them exits.<br/>
This can be done in the following ways:

## Terminating on either success or error

By using the `--kill-others` flag, concurrently will terminate other commands once the first one exits,
no matter the exit code.<br/>
This is useful to terminate the server process once the test is done.

```bash
$ concurrently --kill-others --names server,test 'npm start' 'npm test'
```

## Terminating on error only

By using the `--kill-others-on-fail` flag, concurrently will terminate other commands any command
exits with a non-zero code.<br/>
This is useful if you're building multiple applications, and you want to abort the others once you know
that any of them is broken.

```bash
$ concurrently --kill-others-on-fail 'npm run app1:build' 'npm run app2:build'
```

## Configuring termination

### Kill Signal

It's possible to configure which signal you want to send when terminating commands with the `--kill-signal` flag.
The default is `SIGTERM`, but it's also possible to send `SIGKILL`.

```bash
$ concurrently --kill-others --kill-signal SIGKILL 'npm start' 'npm test'
```

### Timeout

In case you have a misbehaving process that ignores the kill signal, you can force kill it after some
timeout (in milliseconds) by using the `--kill-timeout` flag.
This sends a `SIGKILL`, which cannot be caught.

```bash
$ concurrently --kill-others --kill-timeout 1000 'sleep 1 && echo bye' './misbehaving'
[0] bye
[0] sleep 1 && echo bye exited with code 0
--> Sending SIGTERM to other processes..
[1] IGNORING SIGNAL
--> Sending SIGKILL to 1 processes..
[1] ./misbehaving exited with code SIGKILL
```


================================================
FILE: lib\assert.spec.ts
================================================
import { afterEach, describe, expect, it, vi } from 'vitest';

import { assertDeprecated } from './assert.js';

describe('#assertDeprecated()', () => {
    const consoleMock = vi.spyOn(console, 'warn').mockImplementation(() => {});

    afterEach(() => {
        vi.clearAllMocks();
    });

    it('prints warning with name and message when condition is false', () => {
        assertDeprecated(false, 'example-flag', 'This is an example message.');

        expect(consoleMock).toHaveBeenLastCalledWith(
            '[concurrently] example-flag is deprecated. This is an example message.',
        );
    });

    it('prints same warning only once', () => {
        assertDeprecated(false, 'example-flag', 'This is an example message.');
        assertDeprecated(false, 'different-flag', 'This is another message.');

        expect(consoleMock).toBeCalledTimes(1);
        expect(consoleMock).toHaveBeenLastCalledWith(
            '[concurrently] different-flag is deprecated. This is another message.',
        );
    });

    it('prints nothing if condition is true', () => {
        assertDeprecated(true, 'example-flag', 'This is an example message.');

        expect(consoleMock).not.toHaveBeenCalled();
    });
});


================================================
FILE: lib\assert.ts
================================================
const deprecations = new Set<string>();

/**
 * Asserts that some condition is true, and if not, prints a warning about it being deprecated.
 * The message is printed only once.
 */
export function assertDeprecated(check: boolean, name: string, message: string) {
    if (!check && !deprecations.has(name)) {
        // eslint-disable-next-line no-console
        console.warn(`[concurrently] ${name} is deprecated. ${message}`);
        deprecations.add(name);
    }
}


================================================
FILE: lib\command.spec.ts
================================================
import { Buffer } from 'node:buffer';
import { SendHandle, SpawnOptions } from 'node:child_process';
import { EventEmitter } from 'node:events';
import { Readable, Writable } from 'node:stream';

import { subscribeSpyTo } from '@hirez_io/observer-spy';
import Rx from 'rxjs';
import { beforeEach, describe, expect, it, Mock, vi } from 'vitest';

import {
    ChildProcess,
    CloseEvent,
    Command,
    CommandInfo,
    KillProcess,
    SpawnCommand,
} from './command.js';

interface CommandValues {
    error: unknown;
    close: CloseEvent;
    timer: unknown[];
}

let process: ChildProcess;
let sendMessage: Mock;
let spawn: Mock<SpawnCommand>;
let killProcess: KillProcess;

const IPC_FD = 3;

beforeEach(() => {
    sendMessage = vi.fn();
    process = new (class extends EventEmitter {
        readonly pid = 1;
        send = sendMessage;
        readonly stdout = new Readable({
            read() {
                // do nothing
            },
        });
        readonly stderr = new Readable({
            read() {
                // do nothing
            },
        });
        readonly stdin = new Writable({
            write() {
                // do nothing
            },
        });
    })();
    spawn = vi.fn().mockReturnValue(process);
    killProcess = vi.fn();
});

const createCommand = (overrides?: Partial<CommandInfo>, spawnOpts: SpawnOptions = {}) => {
    const command = new Command(
        { index: 0, name: '', command: 'echo foo', ...overrides },
        spawnOpts,
        spawn,
        killProcess,
    );

    let error: unknown;
    let close: CloseEvent;
    const timer = subscribeSpyTo(command.timer);
    const finished = subscribeSpyTo(
        new Rx.Observable((observer) => {
            // First event in both subjects means command has finished
            command.error.subscribe({
                next: (value) => {
                    error = value;
                    observer.complete();
                },
            });
            command.close.subscribe({
                next: (value) => {
                    close = value;
                    observer.complete();
                },
            });
        }),
    );
    const values = async (): Promise<CommandValues> => {
        await finished.onComplete();
        return { error, close, timer: timer.getValues() };
    };

    return { command, values };
};

it('has stopped state by default', () => {
    const { command } = createCommand();
    expect(command.state).toBe('stopped');
});

describe('#start()', () => {
    it('spawns process with given command and options', () => {
        const { command } = createCommand({}, { detached: true });
        command.start();

        expect(spawn).toHaveBeenCalledExactlyOnceWith(command.command, { detached: true });
    });

    it('sets stdin, process and PID', () => {
        const { command } = createCommand();
        command.start();

        expect(command.process).toBe(process);
        expect(command.pid).toBe(process.pid);
        expect(command.stdin).toBe(process.stdin);
    });

    it('handles process with no stdin', () => {
        process.stdin = null;
        const { command } = createCommand();
        command.start();

        expect(command.stdin).toBe(undefined);
    });

    it('changes state to started', () => {
        const { command } = createCommand();
        const spy = subscribeSpyTo(command.stateChange);
        command.start();
        expect(command.state).toBe('started');
        expect(spy.getFirstValue()).toBe('started');
    });

    describe('on errors', () => {
        it('changes state to errored', () => {
            const { command } = createCommand();
            command.start();

            const spy = subscribeSpyTo(command.stateChange);
            process.emit('error', 'foo');
            expect(command.state).toBe('errored');
            expect(spy.getFirstValue()).toBe('errored');
        });

        it('shares to the error stream', async () => {
            const { command, values } = createCommand();
            command.start();
            process.emit('error', 'foo');
            const { error } = await values();

            expect(error).toBe('foo');
            expect(command.process).toBeUndefined();
        });

        it('shares start and error timing events to the timing stream', async () => {
            const { command, values } = createCommand();
            const startDate = new Date();
            const endDate = new Date(startDate.getTime() + 1000);
            vi.spyOn(Date, 'now')
                .mockReturnValueOnce(startDate.getTime())
                .mockReturnValueOnce(endDate.getTime());
            command.start();
            process.emit('error', 0, null);
            const { timer } = await values();

            expect(timer[0]).toEqual({ startDate, endDate: undefined });
            expect(timer[1]).toEqual({ startDate, endDate });
        });
    });

    describe('on close', () => {
        it('c

================================================
FILE: lib\command.ts
================================================
import { Buffer } from 'node:buffer';
import {
    ChildProcess as BaseChildProcess,
    MessageOptions,
    SendHandle,
    SpawnOptions,
} from 'node:child_process';
import process from 'node:process';
import { EventEmitter, Writable } from 'node:stream';

import Rx from 'rxjs';

/**
 * Identifier for a command; if string, it's the command's name, if number, it's the index.
 */
export type CommandIdentifier = string | number;

export interface CommandInfo {
    /**
     * Command's name.
     */
    name: string;

    /**
     * Which command line the command has.
     */
    command: string;

    /**
     * Which environment variables should the spawned process have.
     */
    env?: Record<string, unknown>;

    /**
     * The current working directory of the process when spawned.
     */
    cwd?: string;

    /**
     * Color to use on prefix of the command.
     */
    prefixColor?: string;

    /**
     * Whether sending of messages to/from this command (also known as "inter-process communication")
     * should be enabled, and using which file descriptor number.
     *
     * If set, must be > 2.
     */
    ipc?: number;

    /**
     * Output command in raw format.
     */
    raw?: boolean;
}

export interface CloseEvent {
    command: CommandInfo;

    /**
     * The command's index among all commands ran.
     */
    index: number;

    /**
     * Whether the command exited because it was killed.
     */
    killed: boolean;

    /**
     * The exit code or signal for the command.
     */
    exitCode: string | number;

    timings: {
        startDate: Date;
        endDate: Date;
        durationSeconds: number;
    };
}

export interface TimerEvent {
    startDate: Date;
    endDate?: Date;
}

export interface MessageEvent {
    message: object;
    handle?: SendHandle;
}

interface OutgoingMessageEvent extends MessageEvent {
    options?: MessageOptions;
    onSent: (error?: unknown) => void;
}

/**
 * Subtype of NodeJS's child_process including only what's actually needed for a command to work.
 */
export type ChildProcess = EventEmitter &
    Pick<BaseChildProcess, 'pid' | 'stdin' | 'stdout' | 'stderr' | 'send'>;

/**
 * Interface for a function that must kill the process with `pid`, optionally sending `signal` to it.
 */
export type KillProcess = (pid: number, signal?: string) => void;

/**
 * Interface for a function that spawns a command and returns its child process instance.
 */
export type SpawnCommand = (command: string, options: SpawnOptions) => ChildProcess;

/**
 * The state of a command.
 *
 * - `stopped`: command was never started
 * - `started`: command is currently running
 * - `errored`: command failed spawning
 * - `exited`: command is not running anymore, e.g. it received a close event
 */
type CommandState = 'stopped' | 'started' | 'errored' | 'exited';

export class Command implements CommandInfo {
    private readonly killProcess: KillProcess;
    private readonly spawn: SpawnCommand;
    private readonly spawnOpts: SpawnOptions;
    readonly index: number;

    /** @inheritdoc */
    readonly name: string;

    /** @inheritdoc */
    readonly command: string;

    /** @inheritdoc */
    readonly prefixColor?: string;

    /** @inheritdoc */
    readonly env: Record<string, unknown>;

    /** @inheritdoc */
    readonly cwd?: string;

    /** @inheritdoc */
    readonly ipc?: number;

    readonly close = new Rx.Subject<CloseEvent>();
    readonly error = new Rx.Subject<unknown>();
    readonly stdout = new Rx.Subject<Buffer>();
    readonly stderr = new Rx.Subject<Buffer>();
    readonly timer = new Rx.Subject<TimerEvent>();

    /**
     * A stream of changes to the `#state` property.
     *
     * Note that the command never goes back to the `stopped` state, therefore it's not a value
     * that's emitted by this stream.
     */
    readonly stateChange = new Rx.Subject<Exclude<CommandState, 'stopped'>>();
    readonly messages = {
        incoming: new Rx.Subject<MessageEvent>(),
        outgoing: new Rx.ReplaySubject<OutgoingMessageEvent>(),
    };

    process?: ChildProcess;

    // TODO: Should exit/error/stdio subscriptions be added here?
    private subscriptions: readonly Rx.Subscription[] = [];
    stdin?: Writable;
    pid?: number;
    killed = false;
    exited = false;

    state: CommandState = 'stopped';

    constructor(
        { index, name, command, prefixColor, env, cwd, ipc }: CommandInfo & { index: number },
        spawnOpts: SpawnOptions,
        spawn: SpawnCommand,
        killProcess: KillProcess,
    ) {
        this.index = index;
        this.name = name;
        this.command = command;
        this.prefixColor = prefixColor;
        this.env = env || {};
        this.cwd = cwd;
        this.ipc = ipc;
        this.killProcess = killProcess;
        this.spawn = spawn;
        this.spawnOpts = spawnOpts;
    }

    /**
     * Starts this command, piping output, error and close events onto the corresponding observables.
     */
    st

================================================
FILE: lib\completion-listener.spec.ts
================================================
import { getEventListeners } from 'node:events';

import { TestScheduler } from 'rxjs/testing';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createFakeCloseEvent, FakeCommand } from './__fixtures__/fake-command.js';
import { CloseEvent } from './command.js';
import { CompletionListener, SuccessCondition } from './completion-listener.js';

let commands: FakeCommand[];
let scheduler: TestScheduler;

beforeEach(() => {
    commands = [
        new FakeCommand('foo', 'echo', 0),
        new FakeCommand('bar', 'echo', 1),
        new FakeCommand('baz', 'echo', 2),
    ];
    scheduler = new TestScheduler(() => true);
});

const createController = (successCondition?: SuccessCondition) =>
    new CompletionListener({
        successCondition,
        scheduler,
    });

const emitFakeCloseEvent = (command: FakeCommand, event?: Partial<CloseEvent>) => {
    const fakeEvent = createFakeCloseEvent({ ...event, command, index: command.index });
    command.state = 'exited';
    command.close.next(fakeEvent);
    return fakeEvent;
};

const flushPromises = () => new Promise((resolve) => setTimeout(resolve, 0));

describe('listen', () => {
    it('resolves when there are no commands', async () => {
        const result = createController().listen([]);
        await expect(result).resolves.toHaveLength(0);
    });

    it('completes only when commands emit a close event, returns close event', async () => {
        const abortCtrl = new AbortController();
        const result = createController('all').listen(commands, abortCtrl.signal);

        commands[0].state = 'started';
        abortCtrl.abort();

        const event = emitFakeCloseEvent(commands[0]);
        scheduler.flush();

        await expect(result).resolves.toHaveLength(1);
        await expect(result).resolves.toEqual([event]);
    });

    it('completes when abort signal is received and command is stopped, returns nothing', async () => {
        const abortCtrl = new AbortController();
        // Use success condition = first to test index access when there are no close events
        const result = createController('first').listen([new FakeCommand()], abortCtrl.signal);

        abortCtrl.abort();
        scheduler.flush();

        await expect(result).resolves.toHaveLength(0);
    });

    it('does not leak memory when listening for abort signals', () => {
        const abortCtrl = new AbortController();
        createController().listen(
            Array.from({ length: 10 }, () => new FakeCommand()),
            abortCtrl.signal,
        );
        expect(getEventListeners(abortCtrl.signal, 'abort')).toHaveLength(1);
    });

    it('check for success once all commands have emitted at least a single close event', async () => {
        const finallyCallback = vi.fn();
        const result = createController().listen(commands).finally(finallyCallback);

        // Emitting multiple close events to mimic calling command `kill/start` APIs.
        emitFakeCloseEvent(commands[0]);
        emitFakeCloseEvent(commands[0]);
        emitFakeCloseEvent(commands[0]);

        scheduler.flush();
        // A broken implementation will have called finallyCallback only after flushing promises
        await flushPromises();
        expect(finallyCallback).not.toHaveBeenCalled();

        emitFakeCloseEvent(commands[1]);
        emitFakeCloseEvent(commands[2]);

        scheduler.flush();

        await expect(result).resolves.toEqual(expect.anything());
        expect(finallyCallback).toHaveBeenCalled();
    });

    it('takes last event emitted from each command', async () => {
        const result = createController().listen(commands);

        emitFakeCloseEvent(commands[0], { exitCode: 0 });
        emitFakeCloseEvent(commands[0], { exitCode: 1 });
        emitFakeCloseEvent(commands[1], { exitCode: 0 });
        emitFakeCloseEvent(commands[2], { exitCode: 0 });

        scheduler.flush();

        await expect(result).rejects.toEqual(expect.anything());
    });

    it('waits for manually restarted events to close', async () => {
        const finallyCallback = vi.fn();
        const result = createController().listen(commands).finally(finallyCallback);

        emitFakeCloseEvent(commands[0]);
        commands[0].state = 'started';
        emitFakeCloseEvent(commands[1]);
        emitFakeCloseEvent(commands[2]);

        scheduler.flush();
        // A broken implementation will have called finallyCallback only after flushing promises
        await flushPromises();
        expect(finallyCallback).not.toHaveBeenCalled();

        commands[0].state = 'exited';
        emitFakeCloseEvent(commands[0]);
        scheduler.flush();

        await expect(result).resolves.toEqual(expect.anything());
        expect(finallyCallback).toHaveBeenCalled();
    });
});

describe('detect commands exit conditions', () => {
    describe('with default success condition set', () => {
        it('succeeds if all processes exited with code 0', () => {
   

================================================
FILE: lib\completion-listener.ts
================================================
import Rx from 'rxjs';
import { delay, filter, map, share, switchMap, take } from 'rxjs/operators';

import { CloseEvent, Command } from './command.js';

/**
 * Defines which command(s) in a list must exit successfully (with an exit code of `0`):
 *
 * - `first`: only the first specified command;
 * - `last`: only the last specified command;
 * - `all`: all commands.
 * - `command-{name|index}`: only the commands with the specified names or index.
 * - `!command-{name|index}`: all commands but the ones with the specified names or index.
 */
export type SuccessCondition =
    | 'first'
    | 'last'
    | 'all'
    | `command-${string | number}`
    | `!command-${string | number}`;

/**
 * Provides logic to determine whether lists of commands ran successfully.
 */
export class CompletionListener {
    private readonly successCondition: SuccessCondition;
    private readonly scheduler?: Rx.SchedulerLike;

    constructor({
        successCondition = 'all',
        scheduler,
    }: {
        /**
         * How this instance will define that a list of commands ran successfully.
         * Defaults to `all`.
         *
         * @see {SuccessCondition}
         */
        successCondition?: SuccessCondition;

        /**
         * For testing only.
         */
        scheduler?: Rx.SchedulerLike;
    }) {
        this.successCondition = successCondition;
        this.scheduler = scheduler;
    }

    private isSuccess(events: CloseEvent[]) {
        if (!events.length) {
            // When every command was aborted, consider a success.
            return true;
        }

        if (this.successCondition === 'first') {
            return events[0].exitCode === 0;
        } else if (this.successCondition === 'last') {
            return events[events.length - 1].exitCode === 0;
        }

        const commandSyntaxMatch = this.successCondition.match(/^!?command-(.+)$/);
        if (commandSyntaxMatch == null) {
            // If not a `command-` syntax, then it's an 'all' condition or it's treated as such.
            return events.every(({ exitCode }) => exitCode === 0);
        }

        // Check `command-` syntax condition.
        // Note that a command's `name` is not necessarily unique,
        // in which case all of them must meet the success condition.
        const nameOrIndex = commandSyntaxMatch[1];
        const targetCommandsEvents = events.filter(
            ({ command, index }) => command.name === nameOrIndex || index === Number(nameOrIndex),
        );
        if (this.successCondition.startsWith('!')) {
            // All commands except the specified ones must exit successfully
            return events.every(
                (event) => targetCommandsEvents.includes(event) || event.exitCode === 0,
            );
        }
        // Only the specified commands must exit successfully
        return (
            targetCommandsEvents.length > 0 &&
            targetCommandsEvents.every((event) => event.exitCode === 0)
        );
    }

    /**
     * Given a list of commands, wait for all of them to exit and then evaluate their exit codes.
     *
     * @returns A Promise that resolves if the success condition is met, or rejects otherwise.
     *          In either case, the value is a list of close events for commands that spawned.
     *          Commands that didn't spawn are filtered out.
     */
    listen(commands: Command[], abortSignal?: AbortSignal): Promise<CloseEvent[]> {
        if (!commands.length) {
            return Promise.resolve([]);
        }

        const abort =
            abortSignal &&
            Rx.fromEvent(abortSignal, 'abort', { once: true }).pipe(
                // The abort signal must happen before commands are killed, otherwise new commands
                // might spawn. Because of this, it's not be possible to capture the close events
                // without an immediate delay
                delay(0, this.scheduler),
                map(() => undefined),
                // #502 - node might warn of too many active listeners on this object if it isn't shared,
                // as each command subscribes to abort event over and over
                share(),
            );

        const closeStreams = commands.map((command) =>
            abort
                ? // Commands that have been started must close.
                  Rx.race(command.close, abort.pipe(filter(() => command.state === 'stopped')))
                : command.close,
        );

        return Rx.lastValueFrom(
            Rx.combineLatest(closeStreams).pipe(
                filter(() => commands.every((command) => command.state !== 'started')),
                map((events) =>
                    events
                        // Filter out aborts, since they cannot be sorted and are considered success condition anyways
                        .filter((event): event is CloseEvent => event != null)
                        // Sort according to exit time
                        .sort

================================================
FILE: lib\concurrently.spec.ts
================================================
import type { CpuInfo } from 'node:os';
import os from 'node:os';
import { Writable } from 'node:stream';

import { beforeEach, expect, it, Mock, MockedObject, vi } from 'vitest';

import { createMockInstance } from './__fixtures__/create-mock-instance.js';
import { createFakeProcess, FakeCommand } from './__fixtures__/fake-command.js';
import { ChildProcess, KillProcess, SpawnCommand } from './command.js';
import { concurrently, ConcurrentlyCommandInput, ConcurrentlyOptions } from './concurrently.js';
import { FlowController } from './flow-control/flow-controller.js';
import { Logger } from './logger.js';

let spawn: SpawnCommand;
let kill: KillProcess;
let onFinishHooks: Mock[];
let controllers: MockedObject<FlowController>[];
let processes: ChildProcess[];
const create = (commands: ConcurrentlyCommandInput[], options: Partial<ConcurrentlyOptions> = {}) =>
    concurrently(commands, Object.assign(options, { controllers, spawn, kill }));

beforeEach(() => {
    vi.resetAllMocks();

    processes = [];
    spawn = vi.fn(() => {
        const process = createFakeProcess(processes.length);
        processes.push(process);
        return process;
    });
    kill = vi.fn();

    onFinishHooks = [vi.fn(), vi.fn()];
    controllers = [
        { handle: vi.fn((commands) => ({ commands, onFinish: onFinishHooks[0] })) },
        { handle: vi.fn((commands) => ({ commands, onFinish: onFinishHooks[1] })) },
    ];
});

it('fails if commands is not an array', () => {
    const bomb = () => create('foo' as never);
    expect(bomb).toThrow();
});

it('fails if no commands were provided', () => {
    const bomb = () => create([]);
    expect(bomb).toThrow();
});

it('spawns all commands', () => {
    create(['echo', 'kill']);
    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith('echo', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('kill', expect.objectContaining({}));
});

it('log output is passed to output stream if logger is specified in options', () => {
    const logger = new Logger({ hide: [] });
    const outputStream = createMockInstance(Writable);
    create(['foo'], { logger, outputStream });
    logger.log('foo', 'bar');

    expect(outputStream.write).toHaveBeenCalledTimes(2);
    expect(outputStream.write).toHaveBeenCalledWith('foo');
    expect(outputStream.write).toHaveBeenCalledWith('bar');
});

it('log output is not passed to output stream after it has errored', () => {
    const logger = new Logger({ hide: [] });
    const outputStream = new Writable();
    vi.spyOn(outputStream, 'write');

    create(['foo'], { logger, outputStream });
    outputStream.emit('error', new Error('test'));
    logger.log('foo', 'bar');

    expect(outputStream.write).not.toHaveBeenCalled();
});

it('spawns commands up to configured limit at once', () => {
    create(['foo', 'bar', 'baz', 'qux'], { maxProcesses: 2 });
    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith('foo', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('bar', expect.objectContaining({}));

    // Test out of order completion picking up new processes in-order
    processes[1].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(3);
    expect(spawn).toHaveBeenCalledWith('baz', expect.objectContaining({}));

    processes[0].emit('close', null, 'SIGINT');
    expect(spawn).toHaveBeenCalledTimes(4);
    expect(spawn).toHaveBeenCalledWith('qux', expect.objectContaining({}));

    // Shouldn't attempt to spawn anything else.
    processes[2].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(4);
});

it('spawns commands up to percent based limit at once', () => {
    // Mock architecture with 4 cores
    const cpusSpy = vi.spyOn(os, 'cpus');
    cpusSpy.mockReturnValue(
        Array.from<CpuInfo>({ length: 4 }).fill({
            model: 'Intel',
            speed: 0,
            times: { user: 0, nice: 0, sys: 0, idle: 0, irq: 0 },
        }),
    );

    create(['foo', 'bar', 'baz', 'qux'], { maxProcesses: '50%' });

    // Max parallel processes should be 2 (50% of 4 cores)
    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith('foo', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('bar', expect.objectContaining({}));

    // Close first process and expect third to be spawned
    processes[0].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(3);
    expect(spawn).toHaveBeenCalledWith('baz', expect.objectContaining({}));

    // Close second process and expect fourth to be spawned
    processes[1].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(4);
    expect(spawn).toHaveBeenCalledWith('qux', expect.objectContaining({}));
});

it('does not spawn further commands on abort signal aborted', () => {
    const abortController = new AbortController();
    create(['foo', 'bar'], { maxProcesses: 1, abortSignal: abortController.signal });
    expect(spawn).toHa

================================================
FILE: lib\concurrently.ts
================================================
import assert from 'node:assert';
import os from 'node:os';
import { Writable } from 'node:stream';

import { takeUntil } from 'rxjs';
import treeKill from 'tree-kill';

import {
    CloseEvent,
    Command,
    CommandIdentifier,
    CommandInfo,
    KillProcess,
    SpawnCommand,
} from './command.js';
import { CommandParser } from './command-parser/command-parser.js';
import { ExpandArguments } from './command-parser/expand-arguments.js';
import { ExpandShortcut } from './command-parser/expand-shortcut.js';
import { ExpandWildcard } from './command-parser/expand-wildcard.js';
import { StripQuotes } from './command-parser/strip-quotes.js';
import { CompletionListener, SuccessCondition } from './completion-listener.js';
import { FlowController } from './flow-control/flow-controller.js';
import { Logger } from './logger.js';
import { OutputWriter } from './output-writer.js';
import { PrefixColorSelector } from './prefix-color-selector.js';
import { getSpawnOpts, spawn } from './spawn.js';
import { castArray } from './utils.js';

const defaults: ConcurrentlyOptions = {
    spawn,
    kill: treeKill,
    raw: false,
    controllers: [],
    cwd: undefined,
};

/**
 * A command that is to be passed into `concurrently()`.
 * If value is a string, then that's the command's command line.
 * Fine grained options can be defined by using the object format.
 */
export type ConcurrentlyCommandInput = string | ({ command: string } & Partial<CommandInfo>);

export interface ConcurrentlyResult {
    /**
     * All commands created and ran by concurrently.
     */
    commands: Command[];

    /**
     * A promise that resolves when concurrently ran successfully according to the specified
     * success condition, or reject otherwise.
     *
     * Both the resolved and rejected value is a list of all the close events for commands that
     * spawned; commands that didn't spawn are filtered out.
     */
    result: Promise<CloseEvent[]>;
}

export interface ConcurrentlyOptions {
    logger?: Logger;

    /**
     * Which stream should the commands output be written to.
     */
    outputStream?: Writable;

    /**
     * Whether the output should be ordered as if the commands were run sequentially.
     */
    group?: boolean;

    /**
     * A comma-separated list of Chalk colors or a string for available styles listed below to use on prefixes.
     * If there are more commands than colors, the last color will be repeated.
     *
     * Available modifiers:
     * - `reset`, `bold`, `dim`, `italic`, `underline`, `inverse`, `hidden`, `strikethrough`
     *
     * Available colors:
     * - `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `gray`,
     * any hex values for colors (e.g. `#23de43`) or `auto` for an automatically picked color
     *
     * Available background colors:
     * - `bgBlack`, `bgRed`, `bgGreen`, `bgYellow`, `bgBlue`, `bgMagenta`, `bgCyan`, `bgWhite`
     *
     * Set to `false` to disable colors.
     *
     * @see {@link https://www.npmjs.com/package/chalk} for more information.
     */
    prefixColors?: string | string[] | false;

    /**
     * Maximum number of commands to run at once.
     * Exact number or a percent of CPUs available (for example "50%").
     *
     * If undefined, then all processes will start in parallel.
     * Setting this value to 1 will achieve sequential running.
     */
    maxProcesses?: number | string;

    /**
     * Whether commands should be spawned in raw mode.
     * Defaults to false.
     */
    raw?: boolean;

    /**
     * Which commands should have their output hidden.
     */
    hide?: CommandIdentifier[];

    /**
     * The current working directory of commands which didn't specify one.
     * Defaults to `process.cwd()`.
     */
    cwd?: string;

    /**
     * @see CompletionListener
     */
    successCondition?: SuccessCondition;

    /**
     * A signal to stop spawning further processes.
     */
    abortSignal?: AbortSignal;

    /**
     * Which flow controllers should be applied on commands spawned by concurrently.
     * Defaults to an empty array.
     */
    controllers: FlowController[];

    /**
     * A function that will spawn commands.
     * Defaults to a function that spawns using either `cmd.exe` or `/bin/sh`.
     */
    spawn: SpawnCommand;

    /**
     * A function that will kill processes.
     * Defaults to the `tree-kill` module.
     */
    kill: KillProcess;

    /**
     * List of additional arguments passed that will get replaced in each command.
     * If not defined, no argument replacing will happen.
     *
     * @see ExpandArguments
     */
    additionalArguments?: string[];
}

/**
 * Core concurrently functionality -- spawns the given commands concurrently and
 * returns the commands themselves + the result according to the specified success condition.
 *
 * @see CompletionListener
 */
export function concurrently(
    baseCommands: ConcurrentlyCommandInput[],
    baseOptions?: Partial<Con

================================================
FILE: lib\date-format.spec.ts
================================================
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { DateFormatter, FormatterOptions } from './date-format.js';

const withTime = (time: string) => `2000-01-01T${time}`;
const withDate = (date: string) => `${date}T00:00:00`;

type TokenTests = undefined | { input: string; expected: string }[];

/**
 * Generates a suite of tests for token `token`.
 *
 * Each entry in `patternTests` makes the token longer, e.g.
 * ```
 * makeTests('year', 'y', [
 *     [{ expected: '2', input: withDate('0002-01-01') }], // y
 *     [{ expected: '02', input: withDate('0002-01-01') }], // yy
 *     // ...
 * ]);
 * ```
 */
const makeTests = (
    name: string,
    token: string,
    patternTests: TokenTests[],
    options?: FormatterOptions,
) =>
    describe(`${name}`, () => {
        patternTests.forEach((tests, i) => {
            const pattern = token.repeat(i + 1);
            if (!tests) {
                return it(`is not implemented for ${pattern}`, () => {
                    expect(() => new DateFormatter(pattern)).toThrow(RangeError);
                });
            } else if (!tests.length) {
                return;
            }

            it.each(tests)(
                `for pattern ${pattern} and input "$input" returns "$expected"`,
                ({ expected, input }) => {
                    const formatter = new DateFormatter(pattern, {
                        locale: 'en',
                        calendar: 'gregory',
                        ...options,
                    });
                    expect(formatter.format(new Date(input))).toBe(expected);
                },
            );
        });
    });

describe('combined', () => {
    it('works with tokens and punctuation', () => {
        const formatter = new DateFormatter('yyyy-MM-dd HH:mm:ss', { locale: 'en' });
        const date = new Date(2024, 8, 1, 15, 30, 50);
        expect(formatter.format(date)).toBe('2024-09-01 15:30:50');
    });

    it('works with tokens and literals', () => {
        const formatter = new DateFormatter("HH 'o''clock'", { locale: 'en' });
        const date = new Date();
        date.setHours(10);
        expect(formatter.format(date)).toBe("10 o'clock");
    });
});

describe('literals', () => {
    it.each([
        ["'", "''"],
        ['foo bar', "'foo bar'"],
        ["foo ' bar", "'foo '' bar'"],
        ["foo bar'?", "'foo bar'''?"],
    ])('returns "%s" for pattern "%s"', (expected, pattern) => {
        const formatter = new DateFormatter(pattern);
        expect(formatter.format(new Date())).toBe(expected);
    });
});

describe('tokens', () => {
    it('throws if a token does not exist', () => {
        expect(() => new DateFormatter('t')).toThrow(SyntaxError);
    });

    makeTests('era', 'G', [
        [
            { input: withDate('-000001-01-01'), expected: 'BC' },
            { input: withDate('0001-01-01'), expected: 'AD' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'BC' },
            { input: withDate('0001-01-01'), expected: 'AD' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'BC' },
            { input: withDate('0001-01-01'), expected: 'AD' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'Before Christ' },
            { input: withDate('0001-01-01'), expected: 'Anno Domini' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'B' },
            { input: withDate('0001-01-01'), expected: 'A' },
        ],
    ]);

    makeTests('year', 'y', [
        [
            { expected: '2', input: withDate('0002-01-01') },
            { expected: '20', input: withDate('0020-01-01') },
            { expected: '200', input: withDate('0200-01-01') },
            { expected: '2000', input: withDate('2000-01-01') },
        ],
        [
            { expected: '02', input: withDate('0002-01-01') },
            { expected: '20', input: withDate('0020-01-01') },
            { expected: '00', input: withDate('0200-01-01') },
            { expected: '05', input: withDate('0205-01-01') },
            { expected: '00', input: withDate('2000-01-01') },
            { expected: '05', input: withDate('2005-01-01') },
        ],
        [
            { expected: '002', input: withDate('0002-01-01') },
            { expected: '020', input: withDate('0020-01-01') },
            { expected: '200', input: withDate('0200-01-01') },
            { expected: '2000', input: withDate('2000-01-01') },
        ],
        [
            { expected: '0002', input: withDate('0002-01-01') },
            { expected: '0020', input: withDate('0020-01-01') },
            { expected: '0200', input: withDate('0200-01-01') },
            { expected: '2000', input: withDate('2000-01-01') },
        ],
        [
            { expected: '00002', input: withDate('0002-01-01') },
            { expected: '00020', input: withDate('0020-01-01') },
            { expected: '00200', input: withDate

================================================
FILE: lib\date-format.ts
================================================
export interface FormatterOptions {
    locale?: string;
    calendar?: string;
}

type TokenFormatter = (date: Date, options: FormatterOptions) => string | number;

/**
 * A map of token to its implementations by length.
 * If an index is undefined, then that token length is unsupported.
 */
const tokens = new Map<string, (TokenFormatter | undefined)[]>()
    // era
    .set('G', [
        makeTokenFn({ era: 'short' }, 'era'),
        makeTokenFn({ era: 'short' }, 'era'),
        makeTokenFn({ era: 'short' }, 'era'),
        makeTokenFn({ era: 'long' }, 'era'),
        makeTokenFn({ era: 'narrow' }, 'era'),
    ])
    // year
    .set('y', [
        // TODO: does not support BC years.
        // https://stackoverflow.com/a/41345095/2083599
        (date) => date.getFullYear(),
        (date) => pad(2, date.getFullYear()).slice(-2),
        (date) => pad(3, date.getFullYear()),
        (date) => pad(4, date.getFullYear()),
        (date) => pad(5, date.getFullYear()),
    ])
    .set('Y', [
        getWeekYear,
        (date, options) => pad(2, getWeekYear(date, options)).slice(-2),
        (date, options) => pad(3, getWeekYear(date, options)),
        (date, options) => pad(4, getWeekYear(date, options)),
        (date, options) => pad(5, getWeekYear(date, options)),
    ])
    .set('u', [])
    .set('U', [
        // Fallback implemented as yearName is not available in gregorian calendars, for instance.
        makeTokenFn({ dateStyle: 'full' }, 'yearName', (date) => String(date.getFullYear())),
    ])
    .set('r', [
        // Fallback implemented as relatedYear is not available in gregorian calendars, for instance.
        makeTokenFn({ dateStyle: 'full' }, 'relatedYear', (date) => String(date.getFullYear())),
    ])
    // quarter
    .set('Q', [
        (date) => Math.floor(date.getMonth() / 3) + 1,
        (date) => pad(2, Math.floor(date.getMonth() / 3) + 1),
        // these aren't localized in Intl.DateTimeFormat.
        undefined,
        undefined,
        (date) => Math.floor(date.getMonth() / 3) + 1,
    ])
    .set('q', [
        (date) => Math.floor(date.getMonth() / 3) + 1,
        (date) => pad(2, Math.floor(date.getMonth() / 3) + 1),
        // these aren't localized in Intl.DateTimeFormat.
        undefined,
        undefined,
        (date) => Math.floor(date.getMonth() / 3) + 1,
    ])
    // month
    .set('M', [
        (date) => date.getMonth() + 1,
        (date) => pad(2, date.getMonth() + 1),
        // these include the day so that it forces non-stand-alone month part
        makeTokenFn({ day: 'numeric', month: 'short' }, 'month'),
        makeTokenFn({ day: 'numeric', month: 'long' }, 'month'),
        makeTokenFn({ day: 'numeric', month: 'narrow' }, 'month'),
    ])
    .set('L', [
        (date) => date.getMonth() + 1,
        (date) => pad(2, date.getMonth() + 1),
        makeTokenFn({ month: 'short' }, 'month'),
        makeTokenFn({ month: 'long' }, 'month'),
        makeTokenFn({ month: 'narrow' }, 'month'),
    ])
    .set('l', [() => ''])
    // week
    .set('w', [getWeek, (date, options) => pad(2, getWeek(date, options))])
    .set('W', [getWeekOfMonth])
    // day
    .set('d', [(date) => date.getDate(), (date) => pad(2, date.getDate())])
    .set('D', [
        getDayOfYear,
        (date) => pad(2, getDayOfYear(date)),
        (date) => pad(3, getDayOfYear(date)),
    ])
    .set('F', [(date) => Math.ceil(date.getDate() / 7)])
    .set('g', [])
    // week day
    .set('E', [
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'long' }, 'weekday'),
    ])
    .set('e', [
        undefined,
        undefined,
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'long' }, 'weekday'),
    ])
    .set('c', [])
    // period
    .set('a', [
        makeTokenFn({ hour12: true, timeStyle: 'full' }, 'dayPeriod'),
        makeTokenFn({ hour12: true, timeStyle: 'full' }, 'dayPeriod'),
        makeTokenFn({ hour12: true, timeStyle: 'full' }, 'dayPeriod'),
    ])
    .set('b', [])
    .set('B', [
        makeTokenFn({ dayPeriod: 'short' }, 'dayPeriod'),
        makeTokenFn({ dayPeriod: 'short' }, 'dayPeriod'),
        makeTokenFn({ dayPeriod: 'short' }, 'dayPeriod'),
        makeTokenFn({ dayPeriod: 'long' }, 'dayPeriod'),
    ])
    // hour
    .set('h', [(date) => date.getHours() % 12 || 12, (date) => pad(2, date.getHours() % 12 || 12)])
    .set('H', [(date) => date.getHours(), (date) => pad(2, date.getHours())])
    .set('K', [(date) => date.getHours() % 12, (date) => pad(2, date.getHours() % 12)])
    .set('k', [(date) => date.getHours() % 24 || 24, (date) => pad(2, date.getHours() % 24 || 24)])
    .set('j', [])
    .set('J', [])
    .set('C', [])
    // minute
    .set('m', [(date) => date.getMinutes(), (date) => pad(2, date.getMinutes())])
    // second
    .set('s', [(date) => date.getSeconds(),

================================================
FILE: lib\defaults.ts
================================================
// This file is meant to be a shared place for default configs.
// It's read by the flow controllers, the executable, etc.
// Refer to tests for the meaning of the different possible values.

import { SuccessCondition } from './completion-listener.js';

export const defaultInputTarget = 0;

/**
 * Whether process.stdin should be forwarded to child processes.
 */
export const handleInput = false;

/**
 * How many processes to run at once.
 */
export const maxProcesses = 0;

/**
 * Indices and names of commands whose output are not to be logged.
 */
export const hide = '';

/**
 * The character to split <names> on.
 */
export const nameSeparator = ',';

/**
 * Which prefix style to use when logging processes output.
 */
export const prefix = '';

/**
 * Default prefix color.
 * @see https://www.npmjs.com/package/chalk
 */
export const prefixColors = 'reset';

/**
 * How many bytes we'll show on the command prefix.
 */
export const prefixLength = 10;

export const raw = false;

/**
 * Number of attempts of restarting a process, if it exits with non-0 code.
 */
export const restartTries = 0;

/**
 * How many milliseconds concurrently should wait before restarting a process.
 */
export const restartDelay = 0;

/**
 * Condition of success for concurrently itself.
 */
export const success = 'all' as SuccessCondition;

/**
 * Date format used when logging date/time.
 * @see https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
 */
export const timestampFormat = 'yyyy-MM-dd HH:mm:ss.SSS';

/**
 * Current working dir passed as option to spawn command.
 * Defaults to process.cwd()
 */
export const cwd: string | undefined = undefined;

/**
 * Whether to show timing information for processes in console output.
 */
export const timings = false;

/**
 * Passthrough additional arguments to commands (accessible via placeholders) instead of treating them as commands.
 */
export const passthroughArguments = false;

/**
 * Signal to send to other processes if one exits or dies.
 *
 * Defaults to OS specific signal. (SIGTERM on Linux/MacOS)
 */
export const killSignal: string | undefined = undefined;


================================================
FILE: lib\index.ts
================================================
import process from 'node:process';
import { Readable } from 'node:stream';

import { assertDeprecated } from './assert.js';
import { CloseEvent, Command, CommandIdentifier, TimerEvent } from './command.js';
import {
    concurrently as createConcurrently,
    ConcurrentlyCommandInput,
    ConcurrentlyOptions as BaseConcurrentlyOptions,
    ConcurrentlyResult,
} from './concurrently.js';
import type { FlowController } from './flow-control/flow-controller.js';
import { InputHandler } from './flow-control/input-handler.js';
import { KillOnSignal } from './flow-control/kill-on-signal.js';
import { KillOthers, ProcessCloseCondition } from './flow-control/kill-others.js';
import { LogError } from './flow-control/log-error.js';
import { LogExit } from './flow-control/log-exit.js';
import { LogOutput } from './flow-control/log-output.js';
import { LogTimings } from './flow-control/log-timings.js';
import { LoggerPadding } from './flow-control/logger-padding.js';
import { OutputErrorHandler } from './flow-control/output-error-handler.js';
import { RestartDelay, RestartProcess } from './flow-control/restart-process.js';
import { Teardown } from './flow-control/teardown.js';
import { Logger } from './logger.js';
import { castArray } from './utils.js';

export type ConcurrentlyOptions = Omit<BaseConcurrentlyOptions, 'abortSignal' | 'hide'> & {
    // Logger options
    /**
     * Which command(s) should have their output hidden.
     */
    hide?: CommandIdentifier | CommandIdentifier[];

    /**
     * The prefix format to use when logging a command's output.
     * Defaults to the command's index.
     */
    prefix?: string;

    /**
     * How many characters should a prefix have at most, used when the prefix format is `command`.
     */
    prefixLength?: number;

    /**
     * Pads short prefixes with spaces so that all prefixes have the same length.
     */
    padPrefix?: boolean;

    /**
     * Whether output should be formatted to include prefixes and whether "event" logs will be logged.
     */
    raw?: boolean;

    /**
     * Date format used when logging date/time.
     * @see https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
     */
    timestampFormat?: string;

    // Input handling options
    defaultInputTarget?: CommandIdentifier;
    inputStream?: Readable;
    handleInput?: boolean;
    pauseInputStreamOnFinish?: boolean;

    // Restarting options
    /**
     * How much time in milliseconds to wait before restarting a command.
     *
     * @see RestartProcess
     */
    restartDelay?: RestartDelay;

    /**
     * How many times commands should be restarted when they exit with a failure.
     *
     * @see RestartProcess
     */
    restartTries?: number;

    // Process killing options
    /**
     * @deprecated Use `killOthersOn` instead.
     * @see KillOthers
     */
    killOthers?: ProcessCloseCondition | ProcessCloseCondition[];
    /**
     * Once the first command exits with one of these statuses, kill other commands.
     * @see KillOthers
     */
    killOthersOn?: ProcessCloseCondition | ProcessCloseCondition[];

    /**
     * Signal to send to killed processes.
     */
    killSignal?: string;

    /**
     * How many milliseconds to wait before killing processes.
     */
    killTimeout?: number;

    // Timing options
    /**
     * Whether to output timing information for processes.
     *
     * @see LogTimings
     */
    timings?: boolean;

    /**
     * Clean up command(s) to execute before exiting concurrently.
     * These won't be prefixed and don't affect concurrently's exit code.
     */
    teardown?: readonly string[];

    /**
     * List of additional arguments passed that will get replaced in each command.
     * If not defined, no argument replacing will happen.
     */
    additionalArguments?: string[];
};

export function concurrently(
    commands: ConcurrentlyCommandInput[],
    options: Partial<ConcurrentlyOptions> = {},
) {
    assertDeprecated(options.killOthers === undefined, 'killOthers', 'Use killOthersOn instead.');

    // To avoid empty strings from hiding the output of commands that don't have a name,
    // keep in the list of commands to hide only strings with some length.
    // This might happen through the CLI when no `--hide` argument is specified, for example.
    const hide = castArray(options.hide).filter((id) => id || id === 0);
    const logger =
        options.logger ||
        new Logger({
            hide,
            prefixFormat: options.prefix,
            commandLength: options.prefixLength,
            raw: options.raw,
            timestampFormat: options.timestampFormat,
        });

    if (options.prefixColors === false) {
        logger.toggleColors(false);
    }

    const abortController = new AbortController();
    const outputStream = options.outputStream || process.stdout;

    return createConcurrently(commands, {
        maxProcesses: options.maxProcesses,
        raw: options.raw,
  

================================================
FILE: lib\jsonc.spec.ts
================================================
/*
ORIGINAL https://www.npmjs.com/package/tiny-jsonc
BY Fabio Spampinato
MIT license

Copied due to the dependency not being compatible with CommonJS
*/

import { expect, it } from 'vitest';

import JSONC from './jsonc.js';

const fixtures = {
    errors: {
        comment: '// asd',
        empty: '',
        prefix: 'invalid 123',
        suffix: '123 invalid',
        multiLineString: `
        {
            "foo": "/*
            */"
        }
        `,
    },
    parse: {
        input: `
        // Example // Yes
        /* EXAMPLE */ /* YES */
        {
            "one": {},
            "two" :{},
            "three": {
                "one": null,
                "two" :true,
                "three": false,
                "four": "asd\\n\\u0022\\"",
                "five": -123.123e10,
                "six": [ 123, true, [],],
            },
        }
        // Example // Yes
        /* EXAMPLE */ /* YES */
        `,
        output: {
            one: {},
            two: {},
            three: {
                one: null,
                two: true,
                three: false,
                four: 'asd\n\u0022"',
                five: -123.123e10,
                six: [123, true, []],
            },
        },
    },
};

it('supports strings with comments and trailing commas', () => {
    const { input, output } = fixtures.parse;

    expect(JSONC.parse(input)).toEqual(output);
});

it('throws on invalid input', () => {
    const { prefix, suffix } = fixtures.errors;

    expect(() => JSONC.parse(prefix)).toThrow(SyntaxError);
    expect(() => JSONC.parse(suffix)).toThrow(SyntaxError);
});

it('throws on insufficient input', () => {
    const { comment, empty } = fixtures.errors;

    expect(() => JSONC.parse(comment)).toThrow(SyntaxError);
    expect(() => JSONC.parse(empty)).toThrow(SyntaxError);
});

it('throws on multi-line strings', () => {
    const { multiLineString } = fixtures.errors;

    expect(() => JSONC.parse(multiLineString)).toThrow(SyntaxError);
});


================================================
FILE: lib\jsonc.ts
================================================
/*
ORIGINAL https://www.npmjs.com/package/tiny-jsonc
BY Fabio Spampinato
MIT license

Copied due to the dependency not being compatible with CommonJS
*/

const stringOrCommentRe = /("(?:\\?[\s\S])*?")|(\/\/.*)|(\/\*[\s\S]*?\*\/)/g;
const stringOrTrailingCommaRe = /("(?:\\?[\s\S])*?")|(,\s*)(?=\]|\})/g;

const JSONC = {
    parse: (text: string) => {
        text = String(text); // To be extra safe

        try {
            // Fast path for valid JSON
            return JSON.parse(text);
        } catch {
            // Slow path for JSONC and invalid inputs
            return JSON.parse(
                text.replace(stringOrCommentRe, '$1').replace(stringOrTrailingCommaRe, '$1'),
            );
        }
    },
    stringify: JSON.stringify,
};

export default JSONC;


================================================
FILE: lib\logger.spec.ts
================================================
import { subscribeSpyTo } from '@hirez_io/observer-spy';
import chalk from 'chalk';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { FakeCommand } from './__fixtures__/fake-command.js';
import { Logger } from './logger.js';

beforeEach(() => {
    // Force Chalk to use colors, otherwise tests may pass when they were supposed to be failing.
    chalk.level = 3;
});

const createLogger = (...options: ConstructorParameters<typeof Logger>) => {
    const logger = new Logger(...options);
    vi.spyOn(logger, 'log');
    const spy = subscribeSpyTo(logger.output);
    return { logger, spy };
};

describe('#log()', () => {
    it('emits prefix + text in the output stream', () => {
        const { logger, spy } = createLogger({});
        logger.log('foo', 'bar');

        const values = spy.getValues();
        expect(values).toHaveLength(2);
        expect(values[0]).toEqual({ command: undefined, text: 'foo' });
        expect(values[1]).toEqual({ command: undefined, text: 'bar' });
    });

    it('emits multiple lines of text with prefix on each', () => {
        const { logger, spy } = createLogger({});
        logger.log('foo', 'bar\nbaz\n');

        const values = spy.getValues();
        expect(values).toHaveLength(2);
        expect(values[0]).toEqual({ command: undefined, text: 'foo' });
        expect(values[1]).toEqual({ command: undefined, text: 'bar\nfoobaz\n' });
    });

    it('does not emit prefix if previous call from same command did not finish with a LF', () => {
        const { logger, spy } = createLogger({});
        const command = new FakeCommand();
        logger.log('foo', 'bar', command);
        logger.log('foo', 'baz', command);

        expect(spy.getValuesLength()).toBe(3);
        expect(spy.getLastValue()).toEqual({ command, text: 'baz' });
    });

    it('emits LF and prefix if previous call is from different command and did not finish with a LF', () => {
        const { logger, spy } = createLogger({});
        const command1 = new FakeCommand();
        logger.log('foo', 'bar', command1);

        const command2 = new FakeCommand();
        logger.log('foo', 'baz', command2);

        const values = spy.getValues();
        expect(values).toHaveLength(5);
        expect(values).toContainEqual({ command: command1, text: '\n' });
        expect(values).toContainEqual({ command: command2, text: 'foo' });
        expect(values).toContainEqual({ command: command2, text: 'baz' });
    });

    it('does not emit prefix nor handle text if logger is in raw mode', () => {
        const { logger, spy } = createLogger({ raw: true });
        logger.log('foo', 'bar\nbaz\n');

        const values = spy.getValues();
        expect(values).toHaveLength(1);
        expect(values[0]).toEqual({ command: undefined, text: 'bar\nbaz\n' });
    });
});

describe('#logGlobalEvent()', () => {
    it('does nothing if in raw mode', () => {
        const { logger } = createLogger({ raw: true });
        logger.logGlobalEvent('foo');

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('logs in gray dim style with arrow prefix', () => {
        const { logger } = createLogger({});
        logger.logGlobalEvent('foo');

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('foo')}\n`,
        );
    });
});

describe('#logCommandText()', () => {
    it('logs with name if no prefixFormat is set', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('bla');
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[bla]')} `, 'foo', cmd);
    });

    it('logs with index if no prefixFormat is set, and command has no name', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('', undefined, 2);
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[2]')} `, 'foo', cmd);
    });

    it('logs with prefixFormat set to pid', () => {
        const { logger } = createLogger({ prefixFormat: 'pid' });
        const cmd = new FakeCommand();
        cmd.pid = 123;
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[123]')} `, 'foo', cmd);
    });

    it('logs with prefixFormat set to name', () => {
        const { logger } = createLogger({ prefixFormat: 'name' });
        const cmd = new FakeCommand('bar');
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[bar]')} `, 'foo', cmd);
    });

    it('logs with prefixFormat set to index', () => {
        const { logger } = createLogger({ prefixFormat: 'index' });
        const cmd = new FakeCommand(undefined, undefined, 3);
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[3]')} `, 'foo', cmd);
    });

    it('logs with prefixFo

================================================
FILE: lib\logger.ts
================================================
import chalk, { Chalk, ChalkInstance } from 'chalk';
import Rx from 'rxjs';

import { Command, CommandIdentifier } from './command.js';
import { DateFormatter } from './date-format.js';
import * as defaults from './defaults.js';
import { escapeRegExp } from './utils.js';

const defaultChalk = chalk;
const noColorChalk = new Chalk({ level: 0 });

function getChalkPath(chalk: ChalkInstance, path: string): ChalkInstance | undefined {
    return path
        .split('.')
        .reduce(
            (prev, key) => prev && (prev as unknown as Record<string, ChalkInstance>)[key],
            chalk,
        );
}

export class Logger {
    private readonly hide: CommandIdentifier[];
    private readonly raw: boolean;
    private readonly prefixFormat?: string;
    private readonly commandLength: number;
    private readonly dateFormatter: DateFormatter;

    private chalk = defaultChalk;

    /**
     * How many characters should a prefix have.
     * Prefixes shorter than this will be padded with spaces to the right.
     */
    private prefixLength = 0;

    /**
     * Last character emitted, and from which command.
     * If `undefined`, then nothing has been logged yet.
     */
    private lastWrite?: { command: Command | undefined; char: string };

    /**
     * Observable that emits when there's been output logged.
     * If `command` is is `undefined`, then the log is for a global event.
     */
    readonly output = new Rx.Subject<{ command: Command | undefined; text: string }>();

    constructor({
        hide,
        prefixFormat,
        commandLength,
        raw = false,
        timestampFormat,
    }: {
        /**
         * Which commands should have their output hidden.
         */
        hide?: CommandIdentifier[];

        /**
         * Whether output should be formatted to include prefixes and whether "event" logs will be
         * logged.
         */
        raw?: boolean;

        /**
         * The prefix format to use when logging a command's output.
         * Defaults to the command's index.
         */
        prefixFormat?: string;

        /**
         * How many characters should a prefix have at most when the format is `command`.
         */
        commandLength?: number;

        /**
         * Date format used when logging date/time.
         * @see https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
         */
        timestampFormat?: string;
    }) {
        this.hide = (hide || []).map(String);
        this.raw = raw;
        this.prefixFormat = prefixFormat;
        this.commandLength = commandLength || defaults.prefixLength;
        this.dateFormatter = new DateFormatter(timestampFormat || defaults.timestampFormat);
    }

    /**
     * Toggles colors on/off globally.
     */
    toggleColors(on: boolean) {
        this.chalk = on ? defaultChalk : noColorChalk;
    }

    private shortenText(text: string) {
        if (!text || text.length <= this.commandLength) {
            return text;
        }

        const ellipsis = '..';
        const prefixLength = this.commandLength - ellipsis.length;
        const endLength = Math.floor(prefixLength / 2);
        const beginningLength = prefixLength - endLength;

        const beginning = text.slice(0, beginningLength);
        const end = text.slice(text.length - endLength, text.length);
        return beginning + ellipsis + end;
    }

    private getPrefixesFor(command: Command): Record<string, string> {
        return {
            // When there's limited concurrency, the PID might not be immediately available,
            // so avoid the string 'undefined' from becoming a prefix
            pid: command.pid != null ? String(command.pid) : '',
            index: String(command.index),
            name: command.name,
            command: this.shortenText(command.command),
            time: this.dateFormatter.format(new Date()),
        };
    }

    getPrefixContent(
        command: Command,
    ): { type: 'default' | 'template'; value: string } | undefined {
        const prefix = this.prefixFormat || (command.name ? 'name' : 'index');
        if (prefix === 'none') {
            return;
        }

        const prefixes = this.getPrefixesFor(command);
        if (Object.keys(prefixes).includes(prefix)) {
            return { type: 'default', value: prefixes[prefix] };
        }

        const value = Object.entries(prefixes).reduce((prev, [key, val]) => {
            const keyRegex = new RegExp(escapeRegExp(`{${key}}`), 'g');
            return prev.replace(keyRegex, String(val));
        }, prefix);
        return { type: 'template', value };
    }

    getPrefix(command: Command): string {
        const content = this.getPrefixContent(command);
        if (!content) {
            return '';
        }

        return content.type === 'template'
            ? content.value.padEnd(this.prefixLength, ' ')
            : `[${content.value.padEnd(this.prefixLength, ' ')}]`;
    }

    setPrefixLeng

================================================
FILE: lib\observables.spec.ts
================================================
import EventEmitter from 'node:events';

import { describe, expect, it } from 'vitest';

import { fromSharedEvent } from './observables.js';

describe('fromSharedEvent()', () => {
    it('returns same observable for event emitter/name pair', () => {
        const emitter = new EventEmitter();
        const obs1 = fromSharedEvent(emitter, 'foo');
        const obs2 = fromSharedEvent(emitter, 'foo');
        expect(obs1).toBe(obs2);
    });

    it('returns different observables for different event emitter/name pairs', () => {
        const emitter = new EventEmitter();
        const obs1 = fromSharedEvent(emitter, 'foo');
        const obs2 = fromSharedEvent(emitter, 'bar');
        expect(obs1).not.toBe(obs2);

        const emitter2 = new EventEmitter();
        const obs3 = fromSharedEvent(emitter2, 'foo');
        const obs4 = fromSharedEvent(emitter2, 'bar');
        expect(obs1).not.toBe(obs3);
        expect(obs2).not.toBe(obs4);
    });

    it('sets up listener only once per event emitter/name pair', () => {
        const emitter = new EventEmitter();
        const observable = fromSharedEvent(emitter, 'foo');
        observable.subscribe();
        observable.subscribe();

        expect(emitter.listenerCount('foo')).toBe(1);
    });
});


================================================
FILE: lib\observables.ts
================================================
import EventEmitter from 'node:events';

import { fromEvent, Observable, share } from 'rxjs';

const sharedEvents = new WeakMap<EventEmitter, Map<string, Observable<unknown>>>();

/**
 * Creates an observable for a specific event of an `EventEmitter` instance.
 *
 * The underlying event listener is set up only once across the application for that event emitter/name pair.
 */
export function fromSharedEvent(emitter: EventEmitter, event: string): Observable<unknown> {
    let emitterEvents = sharedEvents.get(emitter);
    if (!emitterEvents) {
        emitterEvents = new Map();
        sharedEvents.set(emitter, emitterEvents);
    }

    let observable = emitterEvents.get(event);
    if (!observable) {
        observable = fromEvent(emitter, event).pipe(share());
        emitterEvents.set(event, observable);
    }

    return observable;
}


================================================
FILE: lib\output-writer.spec.ts
================================================
import { Writable } from 'node:stream';

import { beforeEach, describe, expect, it, MockedObject } from 'vitest';

import { createMockInstance } from './__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from './__fixtures__/fake-command.js';
import { OutputWriter } from './output-writer.js';

let outputStream: MockedObject<Writable>;
let commands: FakeCommand[];

function createWriter(overrides?: { group: boolean }) {
    const options = {
        outputStream,
        group: false,
        commands,
        ...overrides,
    };
    return new OutputWriter(options);
}

function closeCommand(command: FakeCommand) {
    command.state = 'exited';
    command.close.next(createFakeCloseEvent({ command, index: command.index }));
}

beforeEach(() => {
    outputStream = createMockInstance(Writable);
    commands = [
        new FakeCommand('', undefined, 0),
        new FakeCommand('', undefined, 1),
        new FakeCommand('', undefined, 2),
    ];
});

it('throws if outputStream already is in errored state', () => {
    Object.defineProperty(outputStream, 'errored', { value: new Error('test') });
    expect(() => createWriter()).toThrow(TypeError);
});

describe('#write()', () => {
    it('throws if outputStream has errored', () => {
        const writer = createWriter();
        Object.defineProperty(outputStream, 'errored', { value: new Error('test') });
        expect(() => writer.write(commands[0], 'hello')).toThrow(TypeError);
    });

    describe('with group=false', () => {
        it('writes instantly', () => {
            const writer = createWriter({ group: false });
            writer.write(commands[2], 'hello');
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
        });
    });

    describe('with group=true', () => {
        it('writes for null commands', () => {
            const writer = createWriter({ group: true });
            writer.write(undefined, 'hello');
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
        });

        it('does not write instantly for non-active command', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[2], 'hello');
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            expect(writer.buffers[2]).toEqual(['hello']);
        });

        it('write instantly for active command', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[0], 'hello');
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
        });

        it('does not wait for write from next command to flush', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[1], 'hello');
            writer.write(commands[1], 'foo bar');
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[0]);
            expect(outputStream.write).toHaveBeenCalledTimes(2);
            expect(writer.activeCommandIndex).toBe(1);
            outputStream.write.mockClear();

            writer.write(commands[1], 'blah');
            expect(outputStream.write).toHaveBeenCalledTimes(1);
        });

        it('does not flush for non-active command', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[1], 'hello');
            writer.write(commands[1], 'foo bar');
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[1]);
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[0]);
            expect(outputStream.write).toHaveBeenCalledTimes(2);
        });

        it('flushes multiple commands at a time if necessary', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[2], 'hello');
            closeCommand(commands[1]);
            closeCommand(commands[2]);
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[0]);
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
            expect(writer.activeCommandIndex).toBe(2);
        });
    });
});


================================================
FILE: lib\output-writer.ts
================================================
import { Writable } from 'node:stream';

import Rx from 'rxjs';

import { Command } from './command.js';
import { fromSharedEvent } from './observables.js';

/**
 * Class responsible for actually writing output onto a writable stream.
 */
export class OutputWriter {
    private readonly outputStream: Writable;
    private readonly group: boolean;
    readonly buffers: string[][];
    activeCommandIndex = 0;

    readonly error: Rx.Observable<unknown>;
    private get errored() {
        return this.outputStream.errored;
    }

    constructor({
        outputStream,
        group,
        commands,
    }: {
        outputStream: Writable;
        group: boolean;
        commands: Command[];
    }) {
        this.outputStream = outputStream;
        this.ensureWritable();

        this.error = fromSharedEvent(this.outputStream, 'error');
        this.group = group;
        this.buffers = commands.map(() => []);

        if (this.group) {
            Rx.merge(...commands.map((c) => c.close)).subscribe((command) => {
                if (command.index !== this.activeCommandIndex) {
                    return;
                }
                for (let i = command.index + 1; i < commands.length; i++) {
                    this.activeCommandIndex = i;
                    this.flushBuffer(i);
                    // TODO: Should errored commands also flush buffer?
                    if (commands[i].state !== 'exited') {
                        break;
                    }
                }
            });
        }
    }

    private ensureWritable() {
        if (this.errored) {
            throw new TypeError('outputStream is in errored state', { cause: this.errored });
        }
    }

    write(command: Command | undefined, text: string) {
        this.ensureWritable();
        if (this.group && command) {
            if (command.index <= this.activeCommandIndex) {
                this.outputStream.write(text);
            } else {
                this.buffers[command.index].push(text);
            }
        } else {
            // "global" logs (command=null) are output out of order
            this.outputStream.write(text);
        }
    }

    private flushBuffer(index: number) {
        if (!this.errored) {
            this.buffers[index].forEach((t) => this.outputStream.write(t));
        }
        this.buffers[index] = [];
    }
}


================================================
FILE: lib\prefix-color-selector.spec.ts
================================================
import { ChalkInstance } from 'chalk';
import { afterEach, describe, expect, it, vi } from 'vitest';

import { PrefixColorSelector } from './prefix-color-selector.js';

afterEach(() => {
    vi.restoreAllMocks();
});

describe('#getNextColor()', () => {
    const customTests: Record<
        string,
        {
            acceptableConsoleColors?: Array<keyof ChalkInstance>;
            customColors?: string | string[];
            expectedColors: string[];
        }
    > = {
        'does not produce a color if prefixColors empty': {
            customColors: [],
            expectedColors: ['', '', ''],
        },
        'does not produce a color if prefixColors undefined': {
            expectedColors: ['', '', ''],
        },
        'uses user defined prefix colors only, if no auto is used': {
            customColors: ['red', 'green', 'blue'],
            expectedColors: [
                'red',
                'green',
                'blue',

                // Uses last color if last color is not "auto"
                'blue',
                'blue',
                'blue',
            ],
        },
        'trims colors': {
            customColors: ['  red  ', '  green  ', '  blue  '],
            expectedColors: ['red', 'green', 'blue'],
        },
        'accepts a string value for customColors': {
            customColors: 'red',
            expectedColors: ['red', 'red'],
        },
        'picks varying colors when user defines an auto color': {
            acceptableConsoleColors: ['green', 'blue'],
            customColors: [
                'red',
                'green',
                'auto',
                'green',
                'auto',
                'green',
                'auto',
                'blue',
                'auto',
                'orange',
            ],
            expectedColors: [
                // Custom colors
                'red',
                'green',
                'blue', // Picks auto color "blue", not repeating consecutive "green" color
                'green', // Manual
                'blue', // Auto picks "blue" not to repeat last
                'green', // Manual
                'blue', // Auto picks "blue" again not to repeat last
                'blue', // Manual
                'green', // Auto picks "green" again not to repeat last
                'orange',

                // Uses last color if last color is not "auto"
                'orange',
                'orange',
                'orange',
            ],
        },
        'uses user defined colors then recurring auto colors without repeating consecutive colors':
            {
                acceptableConsoleColors: ['green', 'blue'],
                customColors: ['red', 'green', 'auto'],
                expectedColors: [
                    // Custom colors
                    'red',
                    'green',

                    // Picks auto colors, not repeating consecutive "green" color
                    'blue',
                    'green',
                    'blue',
                    'green',
                ],
            },
        'can sometimes produce consecutive colors': {
            acceptableConsoleColors: ['green', 'blue'],
            customColors: ['blue', 'auto'],
            expectedColors: [
                // Custom colors
                'blue',

                // Picks auto colors
                'green',
                // Does not repeat custom colors for initial auto colors, i.e. does not use "blue" again so soon
                'green', // Consecutive color picked, however practically there would be a lot of colors that need to be set in a particular order for this to occur
                'blue',
                'green',
                'blue',
                'green',
                'blue',
            ],
        },
        'considers the Bright variants of colors equal to the normal colors to avoid similar colors':
            {
                acceptableConsoleColors: ['greenBright', 'blueBright', 'green', 'blue', 'magenta'],
                customColors: ['green', 'blue', 'auto'],
                expectedColors: [
                    // Custom colors
                    'green',
                    'blue',

                    // Picks auto colors, not repeating green and blue colors and variants initially
                    'magenta',

                    // Picks auto colors
                    'greenBright',
                    'blueBright',
                    'green',
                    'blue',
                    'magenta',
                ],
            },
    };
    it.each(Object.entries(customTests))(
        '%s',
        (_, { acceptableConsoleColors, customColors, expectedColors }) => {
            if (acceptableConsoleColors) {
                vi.spyOn(PrefixColorSelector, 'ACCEPTABLE_CONSOLE_COLORS', 'get').mockReturnValue(
                    acceptableConsoleColors,
                );
            }
            const

================================================
FILE: lib\prefix-color-selector.ts
================================================
import { ChalkInstance } from 'chalk';

function getConsoleColorsWithoutCustomColors(customColors: string[]): string[] {
    return PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS.filter(
        // Consider the "Bright" variants of colors to be the same as the plain color to avoid similar colors
        (color) => !customColors.includes(color.replace(/Bright$/, '')),
    );
}

/**
 * Creates a generator that yields an infinite stream of colors.
 */
function* createColorGenerator(customColors: string[]): Generator<string, string> {
    // Custom colors should be used as is, except for "auto"
    const nextAutoColors: string[] = getConsoleColorsWithoutCustomColors(customColors);
    let lastColor: string | undefined;
    for (const customColor of customColors) {
        let currentColor = customColor;
        if (currentColor !== 'auto') {
            yield currentColor; // Manual color
        } else {
            // Find the first auto color that is not the same as the last color
            while (currentColor === 'auto' || lastColor === currentColor) {
                if (!nextAutoColors.length) {
                    // There could be more "auto" values than auto colors so this needs to be able to refill
                    nextAutoColors.push(...PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS);
                }
                currentColor = String(nextAutoColors.shift());
            }
            yield currentColor; // Auto color
        }
        lastColor = currentColor;
    }

    const lastCustomColor = customColors[customColors.length - 1] || '';
    if (lastCustomColor !== 'auto') {
        while (true) {
            yield lastCustomColor; // If last custom color was not "auto" then return same color forever, to maintain existing behavior
        }
    }

    // Finish the initial set(s) of auto colors to avoid repetition
    for (const color of nextAutoColors) {
        yield color;
    }

    // Yield an infinite stream of acceptable console colors
    //
    // If the given custom colors use every ACCEPTABLE_CONSOLE_COLORS except one then there is a chance a color will be repeated,
    // however its highly unlikely and low consequence so not worth the extra complexity to account for it
    while (true) {
        for (const color of PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS) {
            yield color; // Repeat colors forever
        }
    }
}

export class PrefixColorSelector {
    private colorGenerator: Generator<string, string>;

    constructor(customColors: string | string[] = []) {
        const normalizedColors = typeof customColors === 'string' ? [customColors] : customColors;
        this.colorGenerator = createColorGenerator(normalizedColors);
    }

    /** A list of colors that are readable in a terminal. */
    public static get ACCEPTABLE_CONSOLE_COLORS() {
        // Colors picked randomly, can be amended if required
        return [
            // Prevent duplicates, in case the list becomes significantly large
            ...new Set<keyof ChalkInstance>([
                // Text colors
                'cyan',
                'yellow',
                'greenBright',
                'blueBright',
                'magentaBright',
                'white',
                'grey',
                'red',

                // Background colors
                'bgCyan',
                'bgYellow',
                'bgGreenBright',
                'bgBlueBright',
                'bgMagenta',
                'bgWhiteBright',
                'bgGrey',
                'bgRed',
            ]),
        ];
    }

    /**
     * @returns The given custom colors then a set of acceptable console colors indefinitely.
     */
    getNextColor(): string {
        return this.colorGenerator.next().value.trim();
    }
}


================================================
FILE: lib\spawn.spec.ts
================================================
import { describe, expect, it, vi } from 'vitest';

import { getSpawnOpts, spawn } from './spawn.js';

const baseProcess = {
    platform: 'win32' as const,
    cwd: () => '',
    env: {},
};

describe('spawn()', () => {
    it('spawns the given command', async () => {
        const fakeSpawn = vi.fn();
        spawn('echo banana', {}, fakeSpawn, baseProcess);
        expect(fakeSpawn).toHaveBeenCalled();
        expect(fakeSpawn.mock.calls[0][1].join(' ')).toContain('echo banana');
    });

    it('returns spawned process', async () => {
        const childProcess = {};
        const fakeSpawn = vi.fn().mockReturnValue(childProcess);
        const child = spawn('echo banana', {}, fakeSpawn, baseProcess);
        expect(child).toBe(childProcess);
    });
});

describe('getSpawnOpts()', () => {
    it('sets detached mode to false for Windows platform', () => {
        expect(getSpawnOpts({ process: baseProcess }).detached).toBe(false);
    });

    it('sets stdio to pipe when stdio mode is normal', () => {
        expect(getSpawnOpts({ stdio: 'normal' }).stdio).toEqual(['pipe', 'pipe', 'pipe']);
    });

    it('sets stdio to inherit when stdio mode is raw', () => {
        expect(getSpawnOpts({ stdio: 'raw' }).stdio).toEqual(['inherit', 'inherit', 'inherit']);
    });

    it('sets stdio to ignore stdout + stderr when stdio mode is hidden', () => {
        expect(getSpawnOpts({ stdio: 'hidden' }).stdio).toEqual(['pipe', 'ignore', 'ignore']);
    });

    it('sets an ipc channel at the specified descriptor index', () => {
        const opts = getSpawnOpts({ ipc: 3 });
        expect(opts.stdio?.[3]).toBe('ipc');
    });

    it('throws if the ipc channel is <= 2', () => {
        const fn = () => getSpawnOpts({ ipc: 0 });
        expect(fn).toThrow();
    });

    it('merges FORCE_COLOR into env vars if color supported', () => {
        const process = { ...baseProcess, env: { foo: 'bar' } };
        expect(getSpawnOpts({ process, colorSupport: false }).env).toEqual(process.env);
        expect(getSpawnOpts({ process, colorSupport: { level: 1 } }).env).toEqual({
            FORCE_COLOR: '1',
            foo: 'bar',
        });
    });

    it('sets default cwd to process.cwd()', () => {
        const process = { ...baseProcess, cwd: () => 'process-cwd' };
        expect(getSpawnOpts({ process }).cwd).toBe('process-cwd');
    });

    it('overrides default cwd', () => {
        const cwd = 'foobar';
        expect(getSpawnOpts({ cwd }).cwd).toBe(cwd);
    });
});


================================================
FILE: lib\spawn.ts
================================================
import assert from 'node:assert';
import { ChildProcess, IOType, spawn as baseSpawn, SpawnOptions } from 'node:child_process';
import nodeProcess from 'node:process';

import supportsColor, { ColorSupport } from 'supports-color';

/**
 * Spawns a command using `cmd.exe` on Windows, or `/bin/sh` elsewhere.
 */
// Implementation based off of https://github.com/mmalecki/spawn-command/blob/v0.0.2-1/lib/spawn-command.js
export function spawn(
    command: string,
    options: SpawnOptions,
    // For testing
    spawn: (command: string, args: string[], options: SpawnOptions) => ChildProcess = baseSpawn,
    process: Pick<NodeJS.Process, 'platform'> = nodeProcess,
): ChildProcess {
    let file = '/bin/sh';
    let args = ['-c', command];
    if (process.platform === 'win32') {
        file = 'cmd.exe';
        args = ['/s', '/c', `"${command}"`];
        options.windowsVerbatimArguments = true;
    }
    return spawn(file, args, options);
}

export const getSpawnOpts = ({
    colorSupport = supportsColor.stdout,
    cwd,
    process = nodeProcess,
    ipc,
    stdio = 'normal',
    env = {},
}: {
    /**
     * What the color support of the spawned processes should be.
     * If set to `false`, then no colors should be output.
     *
     * Defaults to whatever the terminal's stdout support is.
     */
    colorSupport?: Pick<ColorSupport, 'level'> | false;

    /**
     * The NodeJS process.
     */
    process?: Pick<NodeJS.Process, 'cwd' | 'platform' | 'env'>;

    /**
     * A custom working directory to spawn processes in.
     * Defaults to `process.cwd()`.
     */
    cwd?: string;

    /**
     * The file descriptor number at which the channel for inter-process communication
     * should be set up.
     */
    ipc?: number;

    /**
     * Which stdio mode to use. Raw implies inheriting the parent process' stdio.
     *
     * - `normal`: all of stdout, stderr and stdin are piped
     * - `hidden`: stdin is piped, stdout/stderr outputs are ignored
     * - `raw`: all of stdout, stderr and stdin are inherited from the main process
     *
     * Defaults to `normal`.
     */
    stdio?: 'normal' | 'hidden' | 'raw';

    /**
     * Map of custom environment variables to include in the spawn options.
     */
    env?: Record<string, unknown>;
}): SpawnOptions => {
    const stdioValues: (IOType | 'ipc')[] =
        stdio === 'normal'
            ? ['pipe', 'pipe', 'pipe']
            : stdio === 'raw'
              ? ['inherit', 'inherit', 'inherit']
              : ['pipe', 'ignore', 'ignore'];

    if (ipc != null) {
        // Avoid overriding the stdout/stderr/stdin
        assert.ok(ipc > 2, '[concurrently] the IPC channel number should be > 2');
        stdioValues[ipc] = 'ipc';
    }

    return {
        cwd: cwd || process.cwd(),
        stdio: stdioValues,
        ...(process.platform.startsWith('win') && { detached: false }),
        env: {
            ...(colorSupport ? { FORCE_COLOR: colorSupport.level.toString() } : {}),
            ...process.env,
            ...env,
        },
    };
};


================================================
FILE: lib\utils.spec.ts
================================================
import { describe, expect, it } from 'vitest';

import { castArray, escapeRegExp } from './utils.js';

describe('#escapeRegExp()', () => {
    it('escapes all RegExp chars', () => {
        // eslint-disable-next-line no-useless-escape
        const result = escapeRegExp('\*?{}.(?<test>.)|[]');

        expect(result).toBe('\\*\\?\\{\\}\\.\\(\\?<test>\\.\\)\\|\\[\\]');
    });
});

describe('#castArray()', () => {
    it('returns empty array for nullish input values', () => {
        const result1 = castArray();
        const result2 = castArray(undefined);
        const result3 = castArray(null);

        expect(result1).toStrictEqual([]);
        expect(result2).toStrictEqual([]);
        expect(result3).toStrictEqual([]);
    });

    it('directly returns value if it is already of type array', () => {
        const value = ['example'];
        const result = castArray(value);

        expect(result).toBe(value);
    });

    describe('casts primitives to an array', () => {
        it.each([1, 'example', {}])('%s', (value) => {
            const result = castArray(value);

            expect(result).toStrictEqual([value]);
        });
    });
});


================================================
FILE: lib\utils.ts
================================================
/**
 * Escapes a string for use in a regular expression.
 */
export function escapeRegExp(str: string) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

type CastArrayResult<T> = T extends undefined | null ? never[] : T extends unknown[] ? T : T[];

/**
 * Casts a value to an array if it's not one.
 */
export function castArray<T = never[]>(value?: T) {
    return (Array.isArray(value) ? value : value != null ? [value] : []) as CastArrayResult<T>;
}


================================================
FILE: lib\command-parser\command-parser.d.ts
================================================
import { CommandInfo } from '../command.js';

/**
 * A command parser encapsulates a specific logic for mapping `CommandInfo` objects
 * into another `CommandInfo`.
 *
 * A prime example is turning an abstract `npm:foo` into `npm run foo`, but it could also turn
 * the prefix color of a command brighter, or maybe even prefixing each command with `time(1)`.
 */
export interface CommandParser {
    /**
     * Parses `commandInfo` and returns one or more `CommandInfo`s.
     *
     * Returning multiple `CommandInfo` is used when there are multiple possibilities of commands to
     * run given the original input.
     * An example of this is when the command contains a wildcard and it must be expanded into all
     * viable options so that the consumer can decide which ones to run.
     */
    parse: (commandInfo: CommandInfo) => CommandInfo | CommandInfo[];
}


================================================
FILE: lib\command-parser\expand-arguments.spec.ts
================================================
import { expect, it } from 'vitest';

import { CommandInfo } from '../command.js';
import { ExpandArguments } from './expand-arguments.js';

const createCommandInfo = (command: string): CommandInfo => ({
    command,
    name: '',
});

it('returns command as is when no placeholders', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo foo');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('single argument placeholder is replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {1}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('argument placeholder is replaced and quoted properly', () => {
    const parser = new ExpandArguments(['foo bar']);
    const commandInfo = createCommandInfo('echo {1}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: "echo 'foo bar'" });
});

it('multiple single argument placeholders are replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {2} {1}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo bar foo' });
});

it('empty replacement with single placeholder and not enough passthrough arguments', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {3}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo ' });
});

it('empty replacement with all placeholder and no passthrough arguments', () => {
    const parser = new ExpandArguments([]);
    const commandInfo = createCommandInfo('echo {@}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo ' });
});

it('empty replacement with combined placeholder and no passthrough arguments', () => {
    const parser = new ExpandArguments([]);
    const commandInfo = createCommandInfo('echo {*}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo ' });
});

it('all arguments placeholder is replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {@}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo bar' });
});

it('combined arguments placeholder is replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {*}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: "echo 'foo bar'" });
});

it('escaped argument placeholders are not replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    // Equals to single backslash on command line
    const commandInfo = createCommandInfo('echo \\{1} \\{@} \\{*}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo {1} {@} {*}' });
});


================================================
FILE: lib\command-parser\expand-arguments.ts
================================================
import { quote } from 'shell-quote';

import { CommandInfo } from '../command.js';
import { CommandParser } from './command-parser.js';

/**
 * Replace placeholders with additional arguments.
 */
export class ExpandArguments implements CommandParser {
    constructor(private readonly additionalArguments: string[]) {}

    parse(commandInfo: CommandInfo) {
        const command = commandInfo.command.replace(
            /\\?\{([@*]|[1-9]\d*)\}/g,
            (match, placeholderTarget: string) => {
                // Don't replace the placeholder if it is escaped by a backslash.
                if (match.startsWith('\\')) {
                    return match.slice(1);
                }

                if (this.additionalArguments.length > 0) {
                    // Replace numeric placeholder if value exists in additional arguments.
                    if (+placeholderTarget <= this.additionalArguments.length) {
                        return quote([this.additionalArguments[+placeholderTarget - 1]]);
                    }

                    // Replace all arguments placeholder.
                    if (placeholderTarget === '@') {
                        return quote(this.additionalArguments);
                    }

                    // Replace combined arguments placeholder.
                    if (placeholderTarget === '*') {
                        return quote([this.additionalArguments.join(' ')]);
                    }
                }

                // Replace placeholder with empty string
                // if value doesn't exist in additional arguments.
                return '';
            },
        );

        return { ...commandInfo, command };
    }
}


================================================
FILE: lib\command-parser\expand-shortcut.spec.ts
================================================
import { describe, expect, it } from 'vitest';

import { CommandInfo } from '../command.js';
import { ExpandShortcut } from './expand-shortcut.js';

const parser = new ExpandShortcut();

const createCommandInfo = (command: string, name = ''): CommandInfo => ({
    name,
    command,
});

it('returns same command if no prefix is present', () => {
    const commandInfo = createCommandInfo('echo foo');
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

describe.each([
    ['npm', 'npm run'],
    ['yarn', 'yarn run'],
    ['pnpm', 'pnpm run'],
    ['bun', 'bun run'],
    ['node', 'node --run'],
    ['deno', 'deno task'],
])(`with '%s:' prefix`, (prefix, command) => {
    it(`expands to "${command} <script> <args>"`, () => {
        const commandInfo = createCommandInfo(`${prefix}:foo -- bar`, 'echo');
        expect(parser.parse(commandInfo)).toEqual({
            ...commandInfo,
            name: 'echo',
            command: `${command} foo -- bar`,
        });
    });

    it('sets name to script name if none', () => {
        const commandInfo = createCommandInfo(`${prefix}:foo -- bar`);
        expect(parser.parse(commandInfo)).toEqual({
            ...commandInfo,
            name: 'foo',
            command: `${command} foo -- bar`,
        });
    });
});


================================================
FILE: lib\command-parser\expand-shortcut.ts
================================================
import { CommandInfo } from '../command.js';
import { CommandParser } from './command-parser.js';

/**
 * Expands shortcuts according to the following table:
 *
 * | Syntax          | Expands to            |
 * | --------------- | --------------------- |
 * | `npm:<script>`  | `npm run <script>`    |
 * | `pnpm:<script>` | `pnpm run <script>`   |
 * | `yarn:<script>` | `yarn run <script>`   |
 * | `bun:<script>`  | `bun run <script>`    |
 * | `node:<script>` | `node --run <script>` |
 * | `deno:<script>` | `deno task <script>`  |
 */
export class ExpandShortcut implements CommandParser {
    parse(commandInfo: CommandInfo) {
        const [, prefix, script, args] =
            /^(npm|yarn|pnpm|bun|node|deno):(\S+)(.*)/.exec(commandInfo.command) || [];
        if (!script) {
            return commandInfo;
        }

        let command: string;
        if (prefix === 'node') {
            command = 'node --run';
        } else if (prefix === 'deno') {
            command = 'deno task';
        } else {
            command = `${prefix} run`;
        }

        return {
            ...commandInfo,
            name: commandInfo.name || script,
            command: `${command} ${script}${args}`,
        };
    }
}


================================================
FILE: lib\command-parser\expand-wildcard.spec.ts
================================================
import fs, { PathOrFileDescriptor } from 'node:fs';

import { afterEach, beforeEach, describe, expect, it, Mock, vi } from 'vitest';

import { CommandInfo } from '../command.js';
import { ExpandWildcard } from './expand-wildcard.js';

let parser: ExpandWildcard;
let readPackage: Mock;
let readDeno: Mock;

const createCommandInfo = (command: string): CommandInfo => ({
    command,
    name: '',
});

beforeEach(() => {
    readDeno = vi.fn();
    readPackage = vi.fn();
    parser = new ExpandWildcard(readDeno, readPackage);
});

afterEach(() => {
    vi.restoreAllMocks();
});

describe('#readDeno()', () => {
    it('can read deno.json', () => {
        const expectedDeno = {
            name: 'deno',
            version: '1.14.0',
        };
        vi.spyOn(fs, 'existsSync').mockImplementation((path: PathOrFileDescriptor) => {
            return path === 'deno.json';
        });
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'deno.json') {
                return JSON.stringify(expectedDeno);
            }
            return '';
        });

        const actualReadDeno = ExpandWildcard.readDeno();
        expect(actualReadDeno).toEqual(expectedDeno);
    });

    it('can read deno.jsonc', () => {
        const expectedDeno = {
            name: 'deno',
            version: '1.14.0',
        };
        vi.spyOn(fs, 'existsSync').mockImplementation((path: PathOrFileDescriptor) => {
            return path === 'deno.jsonc';
        });
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'deno.jsonc') {
                return `/* comment */\n${JSON.stringify(expectedDeno)}`;
            }
            return '';
        });

        const actualReadDeno = ExpandWildcard.readDeno();
        expect(actualReadDeno).toEqual(expectedDeno);
    });

    it('prefers deno.json over deno.jsonc', () => {
        const expectedDeno = {
            name: 'deno',
            version: '1.14.0',
        };
        vi.spyOn(fs, 'existsSync').mockImplementation((path: PathOrFileDescriptor) => {
            return path === 'deno.json' || path === 'deno.jsonc';
        });
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'deno.json') {
                return JSON.stringify(expectedDeno);
            }
            return '';
        });

        const actualReadDeno = ExpandWildcard.readDeno();
        expect(actualReadDeno).toEqual(expectedDeno);
    });

    it('can handle errors reading deno', () => {
        vi.spyOn(fs, 'existsSync').mockReturnValue(true);
        vi.spyOn(fs, 'readFileSync').mockImplementation(() => {
            throw new Error('Error reading deno');
        });

        expect(() => ExpandWildcard.readDeno()).not.toThrow();
        expect(ExpandWildcard.readDeno()).toEqual({});
    });
});

describe('#readPackage()', () => {
    it('can read package', () => {
        const expectedPackage = {
            name: 'concurrently',
            version: '6.4.0',
        };
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'package.json') {
                return JSON.stringify(expectedPackage);
            }
            return '';
        });

        const actualReadPackage = ExpandWildcard.readPackage();
        expect(actualReadPackage).toEqual(expectedPackage);
    });

    it('can handle errors reading package', () => {
        vi.spyOn(fs, 'readFileSync').mockImplementation(() => {
            throw new Error('Error reading package');
        });

        expect(() => ExpandWildcard.readPackage()).not.toThrow();
        expect(ExpandWildcard.readPackage()).toEqual({});
    });
});

it('returns same command if not an npm run command', () => {
    const commandInfo = createCommandInfo('npm test');

    expect(readDeno).not.toHaveBeenCalled();
    expect(readPackage).not.toHaveBeenCalled();
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

it('returns same command if not a deno task command', () => {
    const commandInfo = createCommandInfo('deno run');

    expect(readDeno).not.toHaveBeenCalled();
    expect(readPackage).not.toHaveBeenCalled();
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

it('returns same command if no wildcard present', () => {
    const commandInfo = createCommandInfo('npm run foo bar');

    expect(readPackage).not.toHaveBeenCalled();
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

it('expands to nothing if no scripts exist in package.json', () => {
    readPackage.mockReturnValue({});

    expect(parser.parse(createCommandInfo('npm run foo-*-baz qux'))).toEqual([]);
});

it('expands to nothing if no tasks exist in Deno config and no scripts exist in NodeJS config', () => {
    readDeno.mockReturnValue({});
    readPackage.mockReturnValue({});

    expect(parser.parse(createCommandInfo('deno

================================================
FILE: lib\command-parser\expand-wildcard.ts
================================================
import fs from 'node:fs';

import { CommandInfo } from '../command.js';
import JSONC from '../jsonc.js';
import { escapeRegExp } from '../utils.js';
import { CommandParser } from './command-parser.js';

// Matches a negative filter surrounded by '(!' and ')'.
const OMISSION = /\(!([^)]+)\)/;

/**
 * Finds wildcards in 'npm/yarn/pnpm/bun run', 'node --run' and 'deno task'
 * commands and replaces them with all matching scripts in the NodeJS and Deno
 * configuration files of the current directory.
 */
export class ExpandWildcard implements CommandParser {
    static readDeno() {
        try {
            let json: string = '{}';

            if (fs.existsSync('deno.json')) {
                json = fs.readFileSync('deno.json', { encoding: 'utf-8' });
            } else if (fs.existsSync('deno.jsonc')) {
                json = fs.readFileSync('deno.jsonc', { encoding: 'utf-8' });
            }

            return JSONC.parse(json);
        } catch {
            return {};
        }
    }

    static readPackage() {
        try {
            const json = fs.readFileSync('package.json', { encoding: 'utf-8' });
            return JSON.parse(json);
        } catch {
            return {};
        }
    }

    private packageScripts?: string[];
    private denoTasks?: string[];

    constructor(
        private readonly readDeno = ExpandWildcard.readDeno,
        private readonly readPackage = ExpandWildcard.readPackage,
    ) {}

    private relevantScripts(command: string): string[] {
        if (!this.packageScripts) {
            this.packageScripts = Object.keys(this.readPackage().scripts || {});
        }

        if (command === 'deno task') {
            if (!this.denoTasks) {
                // If Deno tries to run a task that doesn't exist,
                // it can fall back to running a script with the same name.
                // Therefore, the actual list of tasks is the union of the tasks and scripts.
                this.denoTasks = [
                    ...Object.keys(this.readDeno().tasks || {}),
                    ...this.packageScripts,
                ];
            }

            return this.denoTasks;
        }

        return this.packageScripts;
    }

    parse(commandInfo: CommandInfo) {
        // We expect one of the following patterns:
        // - <npm|yarn|pnpm|bun> run <script> [args]
        // - node --run <script> [args]
        // - deno task <script> [args]
        const [, command, scriptGlob, args] =
            /((?:npm|yarn|pnpm|bun) run|node --run|deno task) (\S+)([^&]*)/.exec(
                commandInfo.command,
            ) || [];

        const wildcardPosition = (scriptGlob || '').indexOf('*');

        // If the regex didn't match an npm script, or it has no wildcard,
        // then we have nothing to do here
        if (wildcardPosition === -1) {
            return commandInfo;
        }

        const [, omission] = OMISSION.exec(scriptGlob) || [];
        const scriptGlobSansOmission = scriptGlob.replace(OMISSION, '');
        const preWildcard = escapeRegExp(scriptGlobSansOmission.slice(0, wildcardPosition));
        const postWildcard = escapeRegExp(scriptGlobSansOmission.slice(wildcardPosition + 1));
        const wildcardRegex = new RegExp(`^${preWildcard}(.*?)${postWildcard}$`);
        // If 'commandInfo.name' doesn't match 'scriptGlob', this means a custom name
        // has been specified and thus becomes the prefix (as described in the README).
        const prefix = commandInfo.name !== scriptGlob ? commandInfo.name : '';

        const commands: CommandInfo[] = [];

        for (const script of this.relevantScripts(command)) {
            if (omission && new RegExp(omission).test(script)) {
                continue;
            }

            const result = wildcardRegex.exec(script);
            const match = result?.[1];
            if (match !== undefined) {
                commands.push({
                    ...commandInfo,
                    command: `${command} ${script}${args}`,
                    // Will use an empty command name if no prefix has been specified and
                    // the wildcard match is empty, e.g. if `npm:watch-*` matches `npm run watch-`.
                    name: prefix + match,
                });
            }
        }

        return commands;
    }
}


================================================
FILE: lib\command-parser\strip-quotes.spec.ts
================================================
import { expect, it } from 'vitest';

import { CommandInfo } from '../command.js';
import { StripQuotes } from './strip-quotes.js';

const parser = new StripQuotes();

const createCommandInfo = (command: string): CommandInfo => ({
    command,
    name: '',
});

it('returns command as is if no single/double quote at the beginning', () => {
    const commandInfo = createCommandInfo('echo foo');
    expect(parser.parse(commandInfo)).toEqual(commandInfo);
});

it('strips single quotes', () => {
    const commandInfo = createCommandInfo("'echo foo'");
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('strips double quotes', () => {
    const commandInfo = createCommandInfo('"echo foo"');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('does not remove quotes if they are unbalanced', () => {
    let commandInfo = createCommandInfo('"echo foo');
    expect(parser.parse(commandInfo)).toEqual(commandInfo);

    commandInfo = createCommandInfo("echo foo'");
    expect(parser.parse(commandInfo)).toEqual(commandInfo);

    commandInfo = createCommandInfo('"echo foo\'');
    expect(parser.parse(commandInfo)).toEqual(commandInfo);
});


================================================
FILE: lib\command-parser\strip-quotes.ts
================================================
import { CommandInfo } from '../command.js';
import { CommandParser } from './command-parser.js';

/**
 * Strips quotes around commands so that they can run on the current shell.
 */
export class StripQuotes implements CommandParser {
    parse(commandInfo: CommandInfo) {
        let { command } = commandInfo;

        // Removes the quotes surrounding a command.
        if (/^".+?"$/.test(command) || /^'.+?'$/.test(command)) {
            command = command.slice(1, command.length - 1);
        }

        return { ...commandInfo, command };
    }
}


================================================
FILE: lib\declarations\intl.d.ts
================================================
// TODO: Delete this file once Typescript has added these.
declare namespace Intl {
    // https://github.com/tc39/ecma402/pull/351
    interface DateTimeFormatPartTypesRegistry {
        yearName?: string;
        relatedYear?: string;
    }

    /**
     * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/getWeekInfo
     */
    interface WeekInfo {
        firstDay: number;
        weekend: readonly number[];
        minimalDays: number;
    }

    interface Locale {
        readonly weekInfo: WeekInfo;
        getWeekInfo?: () => WeekInfo;
    }
}


================================================
FILE: lib\flow-control\flow-controller.d.ts
================================================
import { Command } from '../command.js';

/**
 * Interface for a class that controls and/or watches the behavior of commands.
 *
 * This may include logging their output, creating interactions between them, or changing when they
 * actually finish.
 */
export interface FlowController {
    handle: (commands: Command[]) => { commands: Command[]; onFinish?: () => void | Promise<void> };
}


================================================
FILE: lib\flow-control\input-handler.spec.ts
================================================
import { Buffer } from 'node:buffer';
import { PassThrough } from 'node:stream';

import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { InputHandler } from './input-handler.js';

let commands: Command[];
let controller: InputHandler;
let inputStream: PassThrough;
let logger: Logger;

beforeEach(() => {
    commands = [new FakeCommand('foo', 'echo foo', 0), new FakeCommand('bar', 'echo bar', 1)];
    inputStream = new PassThrough();
    logger = createMockInstance(Logger);
    controller = new InputHandler({
        defaultInputTarget: 0,
        inputStream,
        logger,
    });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });

    controller = new InputHandler({ logger, inputStream });
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('does nothing if called without input stream', () => {
    new InputHandler({
        defaultInputTarget: 0,
        inputStream: undefined,
        logger,
    }).handle(commands);
    inputStream.write('something');

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
});

it('forwards input stream to default target ID', () => {
    controller.handle(commands);

    inputStream.write('something');

    expect(commands[0].stdin?.write).toHaveBeenCalledExactlyOnceWith('something');
    expect(commands[1].stdin?.write).not.toHaveBeenCalled();
});

it('forwards input stream to target index specified in input', () => {
    controller.handle(commands);

    inputStream.write('1:something');
    inputStream.write('1:multi\nline\n');

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
    expect(commands[1].stdin?.write).toHaveBeenCalledTimes(2);
    expect(commands[1].stdin?.write).toHaveBeenCalledWith('something');
    expect(commands[1].stdin?.write).toHaveBeenCalledWith('multi\nline\n');
});

it('forwards input stream to target index specified in input when input contains colon', () => {
    controller.handle(commands);

    inputStream.emit('data', Buffer.from('1:some:thing'));
    inputStream.emit('data', Buffer.from('1: :something'));
    inputStream.emit('data', Buffer.from('1::something'));

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
    expect(commands[1].stdin?.write).toHaveBeenCalledTimes(3);
    expect(commands[1].stdin?.write).toHaveBeenCalledWith('some:thing');
    expect(commands[1].stdin?.write).toHaveBeenCalledWith(' :something');
    expect(commands[1].stdin?.write).toHaveBeenCalledWith(':something');
});

it('does not forward input stream when input contains colon in a different format', () => {
    controller.handle(commands);

    inputStream.emit('data', Buffer.from('Ruby0::Const::Syntax'));
    inputStream.emit('data', Buffer.from('1:Ruby1::Const::Syntax'));
    inputStream.emit('data', Buffer.from('ruby_symbol_arg :my_symbol'));
    inputStream.emit('data', Buffer.from('ruby_symbol_arg(:my_symbol)'));
    inputStream.emit('data', Buffer.from('{ruby_key: :my_val}'));
    inputStream.emit('data', Buffer.from('{:ruby_key=>:my_val}'));
    inputStream.emit('data', Buffer.from('js_obj = {key: "my_val"}'));

    expect(commands[1].stdin?.write).toHaveBeenCalledExactlyOnceWith('Ruby1::Const::Syntax');
    expect(commands[0].stdin?.write).toHaveBeenCalledTimes(6);
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('Ruby0::Const::Syntax');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('ruby_symbol_arg :my_symbol');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('ruby_symbol_arg(:my_symbol)');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('{ruby_key: :my_val}');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('{:ruby_key=>:my_val}');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('js_obj = {key: "my_val"}');
});

it('forwards input stream to target name specified in input', () => {
    controller.handle(commands);

    inputStream.write('bar:something');

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
    expect(commands[1].stdin?.write).toHaveBeenCalledExactlyOnceWith('something');
});

it('logs error if command has no stdin open', () => {
    commands[0].stdin = undefined;
    controller.handle(commands);

    inputStream.write('something');

    expect(commands[1].stdin?.write).not.toHaveBeenCalled();
    expect(logger.logGlobalEvent).toHaveBeenCalledWith(
        'Unable to find command "0", or it has no stdin open\n',
    );
});

it('fallback to default input stream if command is not found', () => {
    controller.handle(commands);

    inputStream.write('foobar:something');

    expect(commands[0].stdin?.write).toHaveBeenCalledExactlyOnceWith('foobar:something');
    expect(commands[1].stdin?.write).not.toHaveBeenCalled();
    expect(logg

================================================
FILE: lib\flow-control\input-handler.ts
================================================
import { Readable } from 'node:stream';

import Rx from 'rxjs';
import { map } from 'rxjs/operators';

import { Command, CommandIdentifier } from '../command.js';
import * as defaults from '../defaults.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Sends input from concurrently through to commands.
 *
 * Input can start with a command identifier, in which case it will be sent to that specific command.
 * For instance, `0:bla` will send `bla` to command at index `0`, and `server:stop` will send `stop`
 * to command with name `server`.
 *
 * If the input doesn't start with a command identifier, it is then always sent to the default target.
 */
export class InputHandler implements FlowController {
    private readonly logger: Logger;
    private readonly defaultInputTarget: CommandIdentifier;
    private readonly inputStream?: Readable;
    private readonly pauseInputStreamOnFinish: boolean;

    constructor({
        defaultInputTarget,
        inputStream,
        pauseInputStreamOnFinish,
        logger,
    }: {
        inputStream?: Readable;
        logger: Logger;
        defaultInputTarget?: CommandIdentifier;
        pauseInputStreamOnFinish?: boolean;
    }) {
        this.logger = logger;
        this.defaultInputTarget = defaultInputTarget || defaults.defaultInputTarget;
        this.inputStream = inputStream;
        this.pauseInputStreamOnFinish = pauseInputStreamOnFinish !== false;
    }

    handle(commands: Command[]): {
        commands: Command[];
        onFinish?: () => void | undefined;
    } {
        const { inputStream } = this;
        if (!inputStream) {
            return { commands };
        }

        const commandsMap = new Map<string, Command>();
        for (const command of commands) {
            commandsMap.set(command.index.toString(), command);
            commandsMap.set(command.name, command);
        }

        Rx.fromEvent(inputStream, 'data')
            .pipe(map((data) => String(data)))
            .subscribe((data) => {
                const dataParts = data.split(/:(.+)/s);
                let target = dataParts[0];
                let command = commandsMap.get(target);
                let input: string;

                if (dataParts.length > 1 && command) {
                    input = dataParts[1];
                } else {
                    // If `target` does not match a registered command,
                    // fallback to `defaultInputTarget` and forward the whole input data
                    target = this.defaultInputTarget.toString();
                    command = commandsMap.get(target);
                    input = data;
                }

                if (command?.stdin) {
                    command.stdin.write(input);
                } else {
                    this.logger.logGlobalEvent(
                        `Unable to find command "${target}", or it has no stdin open\n`,
                    );
                }
            });

        return {
            commands,
            onFinish: () => {
                if (this.pauseInputStreamOnFinish) {
                    // https://github.com/kimmobrunfeldt/concurrently/issues/252
                    inputStream.pause();
                }
            },
        };
    }
}


================================================
FILE: lib\flow-control\kill-on-signal.spec.ts
================================================
import { EventEmitter } from 'node:events';

import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { Command } from '../command.js';
import { KillOnSignal } from './kill-on-signal.js';

let commands: Command[];
let controller: KillOnSignal;
let process: EventEmitter;
let abortController: AbortController;
beforeEach(() => {
    process = new EventEmitter();
    commands = [new FakeCommand(), new FakeCommand()];
    abortController = new AbortController();
    controller = new KillOnSignal({ process, abortController });
});

it('returns commands that keep non-close streams from original commands', () => {
    const { commands: newCommands } = controller.handle(commands);
    newCommands.forEach((newCommand, i) => {
        expect(newCommand.close).not.toBe(commands[i].close);
        expect(newCommand.error).toBe(commands[i].error);
        expect(newCommand.stdout).toBe(commands[i].stdout);
        expect(newCommand.stderr).toBe(commands[i].stderr);
    });
});

it('returns commands that map SIGINT to exit code 0', () => {
    const { commands: newCommands } = controller.handle(commands);
    expect(newCommands).not.toBe(commands);
    expect(newCommands).toHaveLength(commands.length);

    const callback = vi.fn();
    newCommands[0].close.subscribe(callback);
    process.emit('SIGINT', 'SIGINT');

    // A fake command's .kill() call won't trigger a close event automatically...
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    expect(callback).not.toHaveBeenCalledWith(expect.objectContaining({ exitCode: 'SIGINT' }));
    expect(callback).toHaveBeenCalledWith(expect.objectContaining({ exitCode: 0 }));
});

it('returns commands that keep non-SIGINT exit codes', () => {
    const { commands: newCommands } = controller.handle(commands);
    expect(newCommands).not.toBe(commands);
    expect(newCommands).toHaveLength(commands.length);

    const callback = vi.fn();
    newCommands[0].close.subscribe(callback);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    expect(callback).toHaveBeenCalledWith(expect.objectContaining({ exitCode: 1 }));
});

describe.each(['SIGINT', 'SIGTERM', 'SIGHUP'])('on %s', (signal) => {
    it('kills all commands', () => {
        controller.handle(commands);
        process.emit(signal, signal);

        expect(process.listenerCount(signal)).toBe(1);
        expect(commands[0].kill).toHaveBeenCalledWith(signal);
        expect(commands[1].kill).toHaveBeenCalledWith(signal);
    });

    it('sends abort signal', () => {
        controller.handle(commands);
        process.emit(signal, signal);

        expect(abortController.signal.aborted).toBe(true);
    });

    it('removes event listener on finish', () => {
        const { onFinish } = controller.handle(commands);
        onFinish();
        expect(process.listenerCount(signal)).toBe(0);
    });
});


================================================
FILE: lib\flow-control\kill-on-signal.ts
================================================
import EventEmitter from 'node:events';

import { map } from 'rxjs/operators';

import { Command } from '../command.js';
import { FlowController } from './flow-controller.js';

const SIGNALS = ['SIGINT', 'SIGTERM', 'SIGHUP'] as const;

/**
 * Watches the main concurrently process for signals and sends the same signal down to each spawned
 * command.
 */
export class KillOnSignal implements FlowController {
    private readonly process: EventEmitter;
    private readonly abortController?: AbortController;

    constructor({
        process,
        abortController,
    }: {
        process: EventEmitter;
        abortController?: AbortController;
    }) {
        this.process = process;
        this.abortController = abortController;
    }

    handle(commands: Command[]) {
        let caughtSignal: NodeJS.Signals;
        const signalListener = (signal: NodeJS.Signals) => {
            caughtSignal = signal;
            this.abortController?.abort();
            commands.forEach((command) => command.kill(signal));
        };
        SIGNALS.forEach((signal) => this.process.on(signal, signalListener));

        return {
            commands: commands.map((command) => {
                const closeStream = command.close.pipe(
                    map((exitInfo) => {
                        const exitCode = caughtSignal === 'SIGINT' ? 0 : exitInfo.exitCode;
                        return { ...exitInfo, exitCode };
                    }),
                );
                // Return a proxy so that mutations happen on the original Command object.
                // If either `Object.assign()` or `Object.create()` were used, it'd be hard to
                // reflect the mutations on Command objects referenced by previous flow controllers.
                return new Proxy(command, {
                    get(target, prop: keyof Command) {
                        return prop === 'close' ? closeStream : target[prop];
                    },
                });
            }),
            onFinish: () => {
                // Avoids MaxListenersExceededWarning when running programmatically
                SIGNALS.forEach((signal) => this.process.off(signal, signalListener));
            },
        };
    }
}


================================================
FILE: lib\flow-control\kill-others.spec.ts
================================================
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import {
    createFakeCloseEvent,
    createFakeProcess,
    FakeCommand,
} from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { KillOthers, ProcessCloseCondition } from './kill-others.js';

let commands: FakeCommand[];
let logger: Logger;
let abortController: AbortController;
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];
    logger = createMockInstance(Logger);
    abortController = new AbortController();
});

const createWithConditions = (
    conditions: ProcessCloseCondition[],
    opts?: { timeoutMs?: number; killSignal?: string },
) =>
    new KillOthers({
        logger,
        abortController,
        conditions,
        killSignal: undefined,
        ...opts,
    });

const assignProcess = (command: FakeCommand) => {
    const process = createFakeProcess(1);
    command.pid = process.pid;
    command.process = process;
};

const unassignProcess = (command: FakeCommand) => {
    command.pid = undefined;
    command.process = undefined;
};

it('returns same commands', () => {
    expect(createWithConditions(['success']).handle(commands)).toMatchObject({ commands });
    expect(createWithConditions(['failure']).handle(commands)).toMatchObject({ commands });
});

it('does not kill others if condition does not match', () => {
    createWithConditions(['failure']).handle(commands);
    assignProcess(commands[1]);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));

    expect(logger.logGlobalEvent).not.toHaveBeenCalled();
    expect(commands[0].kill).not.toHaveBeenCalled();
    expect(commands[1].kill).not.toHaveBeenCalled();
});

describe.each(['success', 'failure'] as const)('on %s', (condition) => {
    const exitCode = condition === 'success' ? 0 : 1;
    const inversedCode = exitCode === 1 ? 0 : 1;

    it('kills other processes', () => {
        createWithConditions([condition]).handle(commands);
        assignProcess(commands[1]);
        commands[0].close.next(createFakeCloseEvent({ exitCode }));

        expect(logger.logGlobalEvent).toHaveBeenCalledExactlyOnceWith(
            'Sending SIGTERM to other processes..',
        );
        expect(commands[0].kill).not.toHaveBeenCalled();
        expect(commands[1].kill).toHaveBeenCalledWith(undefined);
    });

    it('kills other processes, with specified signal', () => {
        createWithConditions([condition], { killSignal: 'SIGKILL' }).handle(commands);
        assignProcess(commands[1]);
        commands[0].close.next(createFakeCloseEvent({ exitCode }));

        expect(logger.logGlobalEvent).toHaveBeenCalledExactlyOnceWith(
            'Sending SIGKILL to other processes..',
        );
        expect(commands[0].kill).not.toHaveBeenCalled();
        expect(commands[1].kill).toHaveBeenCalledWith('SIGKILL');
    });

    it('sends abort signal on condition match', () => {
        createWithConditions([condition]).handle(commands);
        commands[0].close.next(createFakeCloseEvent({ exitCode }));

        expect(abortController.signal.aborted).toBe(true);
    });

    it('does not send abort signal on condition mismatch', () => {
        createWithConditions([condition]).handle(commands);
        commands[0].close.next(createFakeCloseEvent({ exitCode: inversedCode }));

        expect(abortController.signal.aborted).toBe(false);
    });
});

it('does nothing if called without conditions', () => {
    createWithConditions([]).handle(commands);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));

    expect(logger.logGlobalEvent).not.toHaveBeenCalled();
    expect(commands[0].kill).not.toHaveBeenCalled();
    expect(commands[1].kill).not.toHaveBeenCalled();
});

it('does not try to kill processes already dead', () => {
    createWithConditions(['failure']).handle(commands);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    expect(logger.logGlobalEvent).not.toHaveBeenCalled();
    expect(commands[0].kill).not.toHaveBeenCalled();
    expect(commands[1].kill).not.toHaveBeenCalled();
});

it('force kills misbehaving processes after a timeout', () => {
    vi.useFakeTimers();
    commands.push(new FakeCommand());

    createWithConditions(['failure'], { timeoutMs: 500 }).handle(commands);
    assignProcess(commands[1]);
    assignProcess(commands[2]);
    commands[2].kill = vi.fn(() => unassignProcess(commands[2]));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    vi.advanceTimersByTime(500);

    expect(commands[1].kill).toHaveBeenCalledTimes(2);
    expect(commands[1].kill).toHaveBeenCalledWith('SIGKILL');
    expect(commands[2].kill).toHaveBeenCalledTimes(1);
});


================================================
FILE: lib\flow-control\kill-others.ts
================================================
import { filter, map } from 'rxjs/operators';

import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { castArray } from '../utils.js';
import { FlowController } from './flow-controller.js';

export type ProcessCloseCondition = 'failure' | 'success';

/**
 * Sends a SIGTERM signal to all commands when one of the commands exits with a matching condition.
 */
export class KillOthers implements FlowController {
    private readonly logger: Logger;
    private readonly abortController?: AbortController;
    private readonly conditions: ProcessCloseCondition[];
    private readonly killSignal: string | undefined;
    private readonly timeoutMs?: number;

    constructor({
        logger,
        abortController,
        conditions,
        killSignal,
        timeoutMs,
    }: {
        logger: Logger;
        abortController?: AbortController;
        conditions: ProcessCloseCondition | ProcessCloseCondition[];
        killSignal: string | undefined;
        timeoutMs?: number;
    }) {
        this.logger = logger;
        this.abortController = abortController;
        this.conditions = castArray(conditions);
        this.killSignal = killSignal;
        this.timeoutMs = timeoutMs;
    }

    handle(commands: Command[]) {
        const conditions = this.conditions.filter(
            (condition) => condition === 'failure' || condition === 'success',
        );

        if (!conditions.length) {
            return { commands };
        }

        const closeStates = commands.map((command) =>
            command.close.pipe(
                map(({ exitCode }) =>
                    exitCode === 0 ? ('success' as const) : ('failure' as const),
                ),
                filter((state) => conditions.includes(state)),
            ),
        );

        closeStates.forEach((closeState) =>
            closeState.subscribe(() => {
                this.abortController?.abort();

                const killableCommands = commands.filter((command) => Command.canKill(command));
                if (killableCommands.length) {
                    this.logger.logGlobalEvent(
                        `Sending ${this.killSignal || 'SIGTERM'} to other processes..`,
                    );
                    killableCommands.forEach((command) => command.kill(this.killSignal));
                    this.maybeForceKill(killableCommands);
                }
            }),
        );

        return { commands };
    }

    private maybeForceKill(commands: Command[]) {
        // No need to force kill when the signal already is SIGKILL.
        if (!this.timeoutMs || this.killSignal === 'SIGKILL') {
            return;
        }

        setTimeout(() => {
            const killableCommands = commands.filter((command) => Command.canKill(command));
            if (killableCommands) {
                this.logger.logGlobalEvent(
                    `Sending SIGKILL to ${killableCommands.length} processes..`,
                );
                killableCommands.forEach((command) => command.kill('SIGKILL'));
            }
        }, this.timeoutMs);
    }
}


================================================
FILE: lib\flow-control\log-error.spec.ts
================================================
import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LogError } from './log-error.js';

let controller: LogError;
let logger: Logger;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand(), new FakeCommand()];

    logger = createMockInstance(Logger);
    controller = new LogError({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('logs the error event of each command', () => {
    controller.handle(commands);
    commands[0].error.next('error from command 0');

    const error1 = new Error('test');
    commands[1].error.next(error1);

    // Testing Error without stack
    const error2 = new Error('test');
    error2.stack = '';
    commands[2].error.next(error2);

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(6);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `Error occurred when executing command: ${commands[0].command}`,
        commands[0],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith('error from command 0', commands[0]);

    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `Error occurred when executing command: ${commands[1].command}`,
        commands[1],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(error1.stack, commands[1]);

    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `Error occurred when executing command: ${commands[2].command}`,
        commands[2],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(String(error2), commands[2]);
});


================================================
FILE: lib\flow-control\log-error.ts
================================================
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Logs when commands failed executing, e.g. due to the executable not existing in the system.
 */
export class LogError implements FlowController {
    private readonly logger: Logger;

    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]) {
        commands.forEach((command) =>
            command.error.subscribe((event) => {
                this.logger.logCommandEvent(
                    `Error occurred when executing command: ${command.command}`,
                    command,
                );

                const errorText = String(event instanceof Error ? event.stack || event : event);
                this.logger.logCommandEvent(errorText, command);
            }),
        );

        return { commands };
    }
}


================================================
FILE: lib\flow-control\log-exit.spec.ts
================================================
import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LogExit } from './log-exit.js';

let controller: LogExit;
let logger: Logger;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];

    logger = createMockInstance(Logger);
    controller = new LogExit({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('logs the close event of each command', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 'SIGTERM' }));

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(2);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} exited with code 0`,
        commands[0],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[1].command} exited with code SIGTERM`,
        commands[1],
    );
});


================================================
FILE: lib\flow-control\log-exit.ts
================================================
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Logs the exit code/signal of commands.
 */
export class LogExit implements FlowController {
    private readonly logger: Logger;

    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]) {
        commands.forEach((command) =>
            command.close.subscribe(({ exitCode }) => {
                this.logger.logCommandEvent(
                    `${command.command} exited with code ${exitCode}`,
                    command,
                );
            }),
        );

        return { commands };
    }
}


================================================
FILE: lib\flow-control\log-output.spec.ts
================================================
import { Buffer } from 'node:buffer';

import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LogOutput } from './log-output.js';

let controller: LogOutput;
let logger: Logger;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];

    logger = createMockInstance(Logger);
    controller = new LogOutput({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('logs the stdout of each command', () => {
    controller.handle(commands);

    commands[0].stdout.next(Buffer.from('foo'));
    commands[1].stdout.next(Buffer.from('bar'));

    expect(logger.logCommandText).toHaveBeenCalledTimes(2);
    expect(logger.logCommandText).toHaveBeenCalledWith('foo', commands[0]);
    expect(logger.logCommandText).toHaveBeenCalledWith('bar', commands[1]);
});

it('logs the stderr of each command', () => {
    controller.handle(commands);

    commands[0].stderr.next(Buffer.from('foo'));
    commands[1].stderr.next(Buffer.from('bar'));

    expect(logger.logCommandText).toHaveBeenCalledTimes(2);
    expect(logger.logCommandText).toHaveBeenCalledWith('foo', commands[0]);
    expect(logger.logCommandText).toHaveBeenCalledWith('bar', commands[1]);
});


================================================
FILE: lib\flow-control\log-output.ts
================================================
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Logs the stdout and stderr output of commands.
 */
export class LogOutput implements FlowController {
    private readonly logger: Logger;
    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]) {
        commands.forEach((command) => {
            command.stdout.subscribe((text) =>
                this.logger.logCommandText(text.toString(), command),
            );
            command.stderr.subscribe((text) =>
                this.logger.logCommandText(text.toString(), command),
            );
        });

        return { commands };
    }
}


================================================
FILE: lib\flow-control\log-timings.spec.ts
================================================
import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { CloseEvent } from '../command.js';
import { DateFormatter } from '../date-format.js';
import { Logger } from '../logger.js';
import { LogTimings } from './log-timings.js';

// shown in timing order
const startDate0 = new Date();
const startDate1 = new Date(startDate0.getTime() + 1000);
const endDate1 = new Date(startDate0.getTime() + 5000);
const endDate0 = new Date(startDate0.getTime() + 3000);

const timestampFormat = 'yyyy-MM-dd HH:mm:ss.SSS';
const getDurationText = (startDate: Date, endDate: Date) =>
    `${(endDate.getTime() - startDate.getTime()).toLocaleString()}ms`;
const command0DurationTextMs = getDurationText(startDate0, endDate0);
const command1DurationTextMs = getDurationText(startDate1, endDate1);

let controller: LogTimings;
let logger: Logger;
let commands: FakeCommand[];
let command0ExitInfo: CloseEvent;
let command1ExitInfo: CloseEvent;

beforeEach(() => {
    commands = [new FakeCommand('foo', 'command 1', 0), new FakeCommand('bar', 'command 2', 1)];

    command0ExitInfo = createFakeCloseEvent({
        command: commands[0],
        timings: {
            startDate: startDate0,
            endDate: endDate0,
            durationSeconds: endDate0.getTime() - startDate0.getTime(),
        },
        index: commands[0].index,
    });

    command1ExitInfo = createFakeCloseEvent({
        command: commands[1],
        timings: {
            startDate: startDate1,
            endDate: endDate1,
            durationSeconds: endDate1.getTime() - startDate1.getTime(),
        },
        index: commands[1].index,
    });

    logger = createMockInstance(Logger);
    controller = new LogTimings({ logger, timestampFormat });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it("does not log timings and doesn't throw if no logger is provided", () => {
    controller = new LogTimings({});
    const { onFinish } = controller.handle(commands);

    commands[0].timer.next({ startDate: startDate0 });
    commands[1].timer.next({ startDate: startDate1 });
    commands[1].timer.next({ startDate: startDate1, endDate: endDate1 });
    commands[0].timer.next({ startDate: startDate0, endDate: endDate0 });

    onFinish?.();

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(0);
});

it('logs the timings at the start and end (ie complete or error) event of each command', () => {
    const formatter = new DateFormatter(timestampFormat);
    controller.handle(commands);

    commands[0].timer.next({ startDate: startDate0 });
    commands[1].timer.next({ startDate: startDate1 });
    commands[1].timer.next({ startDate: startDate1, endDate: endDate1 });
    commands[0].timer.next({ startDate: startDate0, endDate: endDate0 });

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(4);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} started at ${formatter.format(startDate0)}`,
        commands[0],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[1].command} started at ${formatter.format(startDate1)}`,
        commands[1],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[1].command} stopped at ${formatter.format(
            endDate1,
        )} after ${command1DurationTextMs}`,
        commands[1],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} stopped at ${formatter.format(
            endDate0,
        )} after ${command0DurationTextMs}`,
        commands[0],
    );
});

it('does not log timings summary if there was an error', () => {
    const { onFinish } = controller.handle(commands);

    commands[0].close.next(command0ExitInfo);
    commands[1].error.next(undefined);

    onFinish?.();

    expect(logger.logTable).toHaveBeenCalledTimes(0);
});

it('logs the sorted timings summary when all processes close successfully after onFinish is called', () => {
    const { onFinish } = controller.handle(commands);

    commands[0].close.next(command0ExitInfo);
    commands[1].close.next(command1ExitInfo);

    expect(logger.logGlobalEvent).toHaveBeenCalledTimes(0);

    onFinish?.();

    expect(logger.logGlobalEvent).toHaveBeenCalledExactlyOnceWith('Timings:');
    // sorted by duration
    expect(logger.logTable).toHaveBeenCalledExactlyOnceWith([
        LogTimings.mapCloseEventToTimingInfo(command1ExitInfo),
        LogTimings.mapCloseEventToTimingInfo(command0ExitInfo),
    ]);
});


================================================
FILE: lib\flow-control\log-timings.ts
================================================
import assert from 'node:assert';

import Rx from 'rxjs';
import { bufferCount, combineLatestWith, take } from 'rxjs/operators';

import { CloseEvent, Command } from '../command.js';
import { DateFormatter } from '../date-format.js';
import * as defaults from '../defaults.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

type TimingInfo = {
    name: string;
    duration: string;
    'exit code': string | number;
    killed: boolean;
    command: string;
};

/**
 * Logs timing information about commands as they start/stop and then a summary when all commands finish.
 */
export class LogTimings implements FlowController {
    static mapCloseEventToTimingInfo({
        command,
        timings,
        killed,
        exitCode,
    }: CloseEvent): TimingInfo {
        const readableDurationMs = (
            timings.endDate.getTime() - timings.startDate.getTime()
        ).toLocaleString();
        return {
            name: command.name,
            duration: readableDurationMs,
            'exit code': exitCode,
            killed,
            command: command.command,
        };
    }

    private readonly logger?: Logger;
    private readonly dateFormatter: DateFormatter;

    constructor({
        logger,
        timestampFormat = defaults.timestampFormat,
    }: {
        logger?: Logger;
        timestampFormat?: string;
    }) {
        this.logger = logger;
        this.dateFormatter = new DateFormatter(timestampFormat);
    }

    private printExitInfoTimingTable(exitInfos: CloseEvent[]) {
        assert.ok(this.logger);

        const exitInfoTable = exitInfos
            .sort((a, b) => b.timings.durationSeconds - a.timings.durationSeconds)
            .map(LogTimings.mapCloseEventToTimingInfo);

        this.logger.logGlobalEvent('Timings:');
        this.logger.logTable(exitInfoTable);
        return exitInfos;
    }

    handle(commands: Command[]) {
        const { logger } = this;
        if (!logger) {
            return { commands };
        }

        // individual process timings
        commands.forEach((command) => {
            command.timer.subscribe(({ startDate, endDate }) => {
                if (!endDate) {
                    const formattedStartDate = this.dateFormatter.format(startDate);
                    logger.logCommandEvent(
                        `${command.command} started at ${formattedStartDate}`,
                        command,
                    );
                } else {
                    const durationMs = endDate.getTime() - startDate.getTime();
                    const formattedEndDate = this.dateFormatter.format(endDate);
                    logger.logCommandEvent(
                        `${
                            command.command
                        } stopped at ${formattedEndDate} after ${durationMs.toLocaleString()}ms`,
                        command,
                    );
                }
            });
        });

        // overall summary timings
        const closeStreams = commands.map((command) => command.close);
        const finished = new Rx.Subject<void>();
        const allProcessesClosed = Rx.merge(...closeStreams).pipe(
            bufferCount(closeStreams.length),
            take(1),
            combineLatestWith(finished),
        );
        allProcessesClosed.subscribe(([exitInfos]) => this.printExitInfoTimingTable(exitInfos));
        return { commands, onFinish: () => finished.next() };
    }
}


================================================
FILE: lib\flow-control\logger-padding.spec.ts
================================================
import { beforeEach, expect, it, MockedObject } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LoggerPadding } from './logger-padding.js';

let logger: MockedObject<Logger>;
let controller: LoggerPadding;
let commands: FakeCommand[];

beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];
    logger = createMockInstance(Logger);
    controller = new LoggerPadding({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('sets the prefix length on handle', () => {
    controller.handle(commands);
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(1);
});

it('updates the prefix length when commands emit a start timer', () => {
    controller.handle(commands);
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(2);

    commands[1].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(3);
});

it('sets prefix length to the longest prefix of all commands', () => {
    logger.getPrefixContent
        .mockReturnValueOnce({ type: 'default', value: 'foobar' })
        .mockReturnValueOnce({ type: 'default', value: 'baz' });

    controller.handle(commands);
    expect(logger.setPrefixLength).toHaveBeenCalledWith(6);
});

it('does not shorten the prefix length', () => {
    logger.getPrefixContent
        .mockReturnValueOnce({ type: 'default', value: '100' })
        .mockReturnValueOnce({ type: 'default', value: '1' });

    controller.handle(commands);
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledWith(3);

    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledWith(3);
});

it('unsubscribes from start timers on finish', () => {
    logger.getPrefixContent.mockReturnValue({ type: 'default', value: '1' });

    const { onFinish } = controller.handle(commands);
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(2);

    onFinish();
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(2);
});


================================================
FILE: lib\flow-control\logger-padding.ts
================================================
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

export class LoggerPadding implements FlowController {
    private readonly logger: Logger;

    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]): { commands: Command[]; onFinish: () => void } {
        // Sometimes there's limited concurrency, so not all commands will spawn straight away.
        // Compute the prefix length now, which works for all styles but those with a PID.
        let length = commands.reduce((length, command) => {
            const content = this.logger.getPrefixContent(command);
            return Math.max(length, content?.value.length || 0);
        }, 0);
        this.logger.setPrefixLength(length);

        // The length of prefixes is somewhat stable, except for PIDs, which might change when a
        // process spawns (e.g. PIDs might look like 1, 10 or 100), therefore listen to command starts
        // and update the prefix length when this happens.
        const subs = commands.map((command) =>
            command.timer.subscribe((event) => {
                if (!event.endDate) {
                    const content = this.logger.getPrefixContent(command);
                    length = Math.max(length, content?.value.length || 0);
                    this.logger.setPrefixLength(length);
                }
            }),
        );

        return {
            commands,
            onFinish() {
                subs.forEach((sub) => sub.unsubscribe());
            },
        };
    }
}


================================================
FILE: lib\flow-control\output-error-handler.spec.ts
================================================
import { Writable } from 'node:stream';

import { beforeEach, describe, expect, it, vi } from 'vitest';

import { FakeCommand } from '../__fixtures__/fake-command.js';
import { OutputErrorHandler } from './output-error-handler.js';

let controller: OutputErrorHandler;
let outputStream: Writable;
let abortController: AbortController;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];

    abortController = new AbortController();
    outputStream = new Writable();
    controller = new OutputErrorHandler({ abortController, outputStream });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

describe('on output stream error', () => {
    beforeEach(() => {
        controller.handle(commands);
        outputStream.emit('error', new Error('test'));
    });

    it('kills every command', () => {
        expect(commands[0].kill).toHaveBeenCalled();
        expect(commands[1].kill).toHaveBeenCalled();
    });

    it('sends abort signal', () => {
        expect(abortController.signal.aborted).toBe(true);
    });
});

describe('on finish', () => {
    it('unsubscribes from output stream error', () => {
        const { onFinish } = controller.handle(commands);
        onFinish();

        outputStream.on('error', vi.fn());
        outputStream.emit('error', new Error('test'));

        expect(commands[0].kill).not.toHaveBeenCalled();
        expect(commands[1].kill).not.toHaveBeenCalled();
        expect(abortController.signal.aborted).toBe(false);
    });
});


================================================
FILE: lib\flow-control\output-error-handler.ts
================================================
import { Writable } from 'node:stream';

import { Command } from '../command.js';
import { fromSharedEvent } from '../observables.js';
import { FlowController } from './flow-controller.js';

/**
 * Kills processes and aborts further command spawning on output stream error (namely, SIGPIPE).
 */
export class OutputErrorHandler implements FlowController {
    private readonly outputStream: Writable;
    private readonly abortController: AbortController;

    constructor({
        abortController,
        outputStream,
    }: {
        abortController: AbortController;
        outputStream: Writable;
    }) {
        this.abortController = abortController;
        this.outputStream = outputStream;
    }

    handle(commands: Command[]): { commands: Command[]; onFinish: () => void } {
        const subscription = fromSharedEvent(this.outputStream, 'error').subscribe(() => {
            commands.forEach((command) => command.kill());

            // Avoid further commands from spawning, e.g. if `RestartProcess` is used.
            this.abortController.abort();
        });

        return {
            commands,
            onFinish: () => subscription.unsubscribe(),
        };
    }
}


================================================
FILE: lib\flow-control\restart-process.spec.ts
================================================
import { VirtualTimeScheduler } from 'rxjs';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { RestartProcess } from './restart-process.js';

let commands: FakeCommand[];
let controller: RestartProcess;
let logger: Logger;
let scheduler: VirtualTimeScheduler;
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];
    logger = createMockInstance(Logger);

    // Don't use TestScheduler as it's hardcoded to a max number of "frames" (time),
    // which don't work for some tests in this suite
    scheduler = new VirtualTimeScheduler();
    controller = new RestartProcess({
        logger,
        scheduler,
        delay: 100,
        tries: 2,
    });
});

it('does not restart processes that complete with success', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(commands[0].start).toHaveBeenCalledTimes(0);
    expect(commands[1].start).toHaveBeenCalledTimes(0);
});

it('restarts processes that fail immediately, if no delay was passed', () => {
    controller = new RestartProcess({ logger, scheduler, tries: 1 });
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    scheduler.flush();

    expect(scheduler.now()).toBe(0);
    expect(logger.logCommandEvent).toHaveBeenCalledExactlyOnceWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(1);
});

it('restarts processes that fail after delay ms has passed', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(scheduler.now()).toBe(100);
    expect(logger.logCommandEvent).toHaveBeenCalledExactlyOnceWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(1);
    expect(commands[1].start).not.toHaveBeenCalled();
});

it('restarts processes that fail with an exponential back-off', () => {
    const tries = 4;
    controller = new RestartProcess({ logger, scheduler, tries, delay: 'exponential' });
    controller.handle(commands);

    let time = 0;
    for (let i = 0; i < tries; i++) {
        commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
        scheduler.flush();

        time += 2 ** i * 1000;
        expect(scheduler.now()).toBe(time);
        expect(logger.logCommandEvent).toHaveBeenCalledTimes(i + 1);
        expect(commands[0].start).toHaveBeenCalledTimes(i + 1);
    }
});

it('restarts processes up to tries', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 'SIGTERM' }));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 'SIGTERM' }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(2);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(2);
});

it('restart processes forever, if tries is negative', () => {
    controller = new RestartProcess({
        logger,
        scheduler,
        delay: 100,
        tries: -1,
    });
    expect(controller.tries).toBe(Infinity);
});

it('restarts processes until they succeed', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(logger.logCommandEvent).toHaveBeenCalledExactlyOnceWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(1);
});

describe('returned commands', () => {
    it('are the same if 0 tries are to be attempted', () => {
        controller = new RestartProcess({ logger, scheduler });
        expect(controller.handle(commands)).toMatchObject({ commands });
    });

    it('are not the same, but with same length if 1+ tries are to be attempted', () => {
        const { commands: newCommands } = controller.handle(commands);
        expect(newCommands).not.toBe(commands);
        expect(newCommands).toHaveLength(commands.length);
    });

    it('skip close events followed by restarts', () => {
        const { commands: newCommands } = controller.handle(commands);

        const callback

================================================
FILE: lib\flow-control\restart-process.ts
================================================
import Rx from 'rxjs';
import { defaultIfEmpty, delayWhen, filter, map, skip, take, takeWhile } from 'rxjs/operators';

import { Command } from '../command.js';
import * as defaults from '../defaults.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

export type RestartDelay = number | 'exponential';

/**
 * Restarts commands that fail up to a defined number of times.
 */
export class RestartProcess implements FlowController {
    private readonly logger: Logger;
    private readonly scheduler?: Rx.SchedulerLike;
    private readonly delay: RestartDelay;
    readonly tries: number;

    constructor({
        delay,
        tries,
        logger,
        scheduler,
    }: {
        delay?: RestartDelay;
        tries?: number;
        logger: Logger;
        scheduler?: Rx.SchedulerLike;
    }) {
        this.logger = logger;
        this.delay = delay ?? 0;
        this.tries = tries != null ? +tries : defaults.restartTries;
        this.tries = this.tries < 0 ? Infinity : this.tries;
        this.scheduler = scheduler;
    }

    handle(commands: Command[]) {
        if (this.tries === 0) {
            return { commands };
        }

        const delayOperator = delayWhen((_, index) => {
            const { delay } = this;
            const value = delay === 'exponential' ? 2 ** index * 1000 : delay;
            return Rx.timer(value, this.scheduler);
        });

        commands
            .map((command) =>
                command.close.pipe(
                    take(this.tries),
                    takeWhile(({ exitCode }) => exitCode !== 0),
                ),
            )
            .forEach((failure, index) =>
                Rx.merge(
                    // Delay the emission (so that the restarts happen on time),
                    // explicitly telling the subscriber that a restart is needed
                    failure.pipe(
                        delayOperator,
                        map(() => true),
                    ),
                    // Skip the first N emissions (as these would be duplicates of the above),
                    // meaning it will be empty because of success, or failed all N times,
                    // and no more restarts should be attempted.
                    failure.pipe(
                        skip(this.tries),
                        map(() => false),
                        defaultIfEmpty(false),
                    ),
                ).subscribe((restart) => {
                    const command = commands[index];
                    if (restart) {
                        this.logger.logCommandEvent(`${command.command} restarted`, command);
                        command.start();
                    }
                }),
            );

        return {
            commands: commands.map((command) => {
                const closeStream = command.close.pipe(
                    filter(({ exitCode }, emission) => {
                        // We let all success codes pass, and failures only after restarting won't happen again
                        return exitCode === 0 || emission >= this.tries;
                    }),
                );

                // Return a proxy so that mutations happen on the original Command object.
                // If either `Object.assign()` or `Object.create()` were used, it'd be hard to
                // reflect the mutations on Command objects referenced by previous flow controllers.
                return new Proxy(command, {
                    get(target, prop: keyof Command) {
                        return prop === 'close' ? closeStream : target[prop];
                    },
                });
            }),
        };
    }
}


================================================
FILE: lib\flow-control\teardown.spec.ts
================================================
import { ChildProcess } from 'node:child_process';

import { afterEach, describe, expect, it, Mock, vi } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeProcess, FakeCommand } from '../__fixtures__/fake-command.js';
import { SpawnCommand } from '../command.js';
import { Logger } from '../logger.js';
import * as spawn from '../spawn.js';
import { Teardown } from './teardown.js';

const spySpawn = vi
    .spyOn(spawn, 'spawn')
    .mockImplementation(() => createFakeProcess(1) as ChildProcess) as Mock;
const logger = createMockInstance(Logger);
const commands = [new FakeCommand()];
const teardown = 'cowsay bye';

afterEach(() => {
    vi.clearAllMocks();
});

const create = (teardown: string[], spawn?: SpawnCommand) =>
    new Teardown({
        spawn,
        logger,
        commands: teardown,
    });

it('returns commands unchanged', () => {
    const { commands: actual } = create([]).handle(commands);
    expect(actual).toBe(commands);
});

describe('onFinish callback', () => {
    it('does not spawn nothing if there are no teardown commands', () => {
        create([]).handle(commands).onFinish();
        expect(spySpawn).not.toHaveBeenCalled();
    });

    it('runs teardown command', () => {
        create([teardown]).handle(commands).onFinish();
        expect(spySpawn).toHaveBeenCalledWith(teardown, spawn.getSpawnOpts({ stdio: 'raw' }));
    });

    it('runs teardown command with custom spawn function', () => {
        const customSpawn = vi.fn(() => createFakeProcess(1));
        create([teardown], customSpawn).handle(commands).onFinish();
        expect(customSpawn).toHaveBeenCalledWith(teardown, spawn.getSpawnOpts({ stdio: 'raw' }));
    });

    it('waits for teardown command to close', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        child.emit('close', 1, null);
        await expect(result).resolves.toBeUndefined();
    });

    it('rejects if teardown command errors (string)', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        const error = 'fail';
        child.emit('error', error);
        await expect(result).rejects.toBe(error);
        expect(logger.logGlobalEvent).toHaveBeenLastCalledWith('fail');
    });

    it('rejects if teardown command errors (error)', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        const error = new Error('fail');
        child.emit('error', error);
        await expect(result).rejects.toBe(error);
        expect(logger.logGlobalEvent).toHaveBeenLastCalledWith(
            expect.stringMatching(/Error: fail/),
        );
    });

    it('rejects if teardown command errors (error, no stack)', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        const error = new Error('fail');
        delete error.stack;
        child.emit('error', error);
        await expect(result).rejects.toBe(error);
        expect(logger.logGlobalEvent).toHaveBeenLastCalledWith('Error: fail');
    });

    it('runs multiple teardown commands in sequence', async () => {
        const child1 = createFakeProcess(1);
        const child2 = createFakeProcess(2);
        spySpawn.mockReturnValueOnce(child1).mockReturnValueOnce(child2);

        const result = create(['foo', 'bar']).handle(commands).onFinish();

        expect(spySpawn).toHaveBeenCalledTimes(1);
        expect(spySpawn).toHaveBeenLastCalledWith('foo', spawn.getSpawnOpts({ stdio: 'raw' }));

        child1.emit('close', 1, null);
        await new Promise((resolve) => setTimeout(resolve));

        expect(spySpawn).toHaveBeenCalledTimes(2);
        expect(spySpawn).toHaveBeenLastCalledWith('bar', spawn.getSpawnOpts({ stdio: 'raw' }));

        child2.emit('close', 0, null);
        await expect(result).resolves.toBeUndefined();
    });

    it('stops running teardown commands on SIGINT', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create(['foo', 'bar']).handle(commands).onFinish();
        child.emit('close', null, 'SIGINT');
        await result;

        expect(spySpawn).toHaveBeenCalledTimes(1);
        expect(spySpawn).toHaveBeenLastCalledWith('foo', expect.anything());
    });
});


================================================
FILE: lib\flow-control\teardown.ts
================================================
import Rx from 'rxjs';

import { Command, SpawnCommand } from '../command.js';
import { Logger } from '../logger.js';
import { getSpawnOpts, spawn as baseSpawn } from '../spawn.js';
import { FlowController } from './flow-controller.js';

export class Teardown implements FlowController {
    private readonly logger: Logger;
    private readonly spawn: SpawnCommand;
    private readonly teardown: readonly string[];

    constructor({
        logger,
        spawn,
        commands,
    }: {
        logger: Logger;
        /**
         * Which function to use to spawn commands.
         * Defaults to the same used by the rest of concurrently.
         */
        spawn?: SpawnCommand;
        commands: readonly string[];
    }) {
        this.logger = logger;
        this.spawn = spawn || baseSpawn;
        this.teardown = commands;
    }

    handle(commands: Command[]): { commands: Command[]; onFinish: () => Promise<void> } {
        const { logger, teardown, spawn } = this;
        const onFinish = async () => {
            if (!teardown.length) {
                return;
            }

            for (const command of teardown) {
                logger.logGlobalEvent(`Running teardown command "${command}"`);

                const child = spawn(command, getSpawnOpts({ stdio: 'raw' }));
                const error = Rx.fromEvent(child, 'error');
                const close = Rx.fromEvent(child, 'close');

                try {
                    const [exitCode, signal] = await Promise.race([
                        Rx.firstValueFrom(error).then((event) => {
                            throw event;
                        }),
                        Rx.firstValueFrom(close).then(
                            (event) => event as [number | null, NodeJS.Signals | null],
                        ),
                    ]);

                    logger.logGlobalEvent(
                        `Teardown command "${command}" exited with code ${exitCode ?? signal}`,
                    );

                    if (signal === 'SIGINT') {
                        break;
                    }
                } catch (error) {
                    const errorText = String(error instanceof Error ? error.stack || error : error);
                    logger.logGlobalEvent(`Teardown command "${command}" errored:`);
                    logger.logGlobalEvent(errorText);
                    return Promise.reject(error);
                }
            }
        };

        return { commands, onFinish };
    }
}


================================================
FILE: lib\__fixtures__\create-mock-instance.ts
================================================
import { MockedObject, vi } from 'vitest';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function createMockInstance<T>(constructor: new (...args: any[]) => T): MockedObject<T> {
    return new (vi.mockObject(constructor))() as MockedObject<T>;
}


================================================
FILE: lib\__fixtures__\fake-command.ts
================================================
import EventEmitter from 'node:events';
import { PassThrough, Writable } from 'node:stream';

import { vi } from 'vitest';

import { ChildProcess, CloseEvent, Command, CommandInfo } from '../command.js';
import { createMockInstance } from './create-mock-instance.js';

export class FakeCommand extends Command {
    constructor(name = 'foo', command = 'echo foo', index = 0, info?: Partial<CommandInfo>) {
        super(
            {
                index,
                name,
                command,
                ...info,
            },
            {},
            vi.fn(),
            vi.fn(),
        );

        this.stdin = createMockInstance(Writable);
        this.start = vi.fn();
        this.kill = vi.fn();
    }
}

export const createFakeProcess = (pid: number): ChildProcess =>
    Object.assign(new EventEmitter(), {
        pid,
        send: vi.fn(),
        stdin: new PassThrough(),
        stdout: new PassThrough(),
        stderr: new PassThrough(),
    });

export const createFakeCloseEvent = (overrides?: Partial<CloseEvent>): CloseEvent => ({
    command: new FakeCommand(),
    index: 0,
    killed: false,
    exitCode: 0,
    timings: {
        startDate: new Date(),
        endDate: new Date(),
        durationSeconds: 0,
    },
    ...overrides,
});


================================================
FILE: tests\package.json
================================================
{
  "dependencies": {
    "concurrently": "workspace:*"
  },
  "scripts": {
    "test": "pnpm --workspace-root test:smoke"
  }
}


================================================
FILE: tests\smoke-tests.spec.ts
================================================
import { exec as originalExec } from 'node:child_process';
import util from 'node:util';

import { beforeAll, expect, it } from 'vitest';

const exec = util.promisify(originalExec);

beforeAll(async () => {
    await exec('pnpm run build');
}, 20_000);

it('spawns binary', async () => {
    await expect(exec('node dist/bin/index.js "echo test"')).resolves.toBeDefined();
});

it.each(['cjs-import', 'cjs-require', 'esm'])('loads library in %s context', async (project) => {
    // Use as separate execs as tsc outputs to stdout, instead of stderr, and so its text isn't shown
    await exec(`tsc -p ${project}`, { cwd: __dirname }).catch((err) => Promise.reject(err.stdout));
    await expect(
        exec(`node ${project}/dist/smoke-test.js`, { cwd: __dirname }),
    ).resolves.toBeDefined();
});


================================================
FILE: tests\cjs-import\package.json
================================================
{
  "type": "commonjs"
}


================================================
FILE: tests\cjs-import\smoke-test.ts
================================================
import type { ConcurrentlyResult } from 'concurrently';
import concurrently, { concurrently as concurrently2, createConcurrently } from 'concurrently';

const _result: ConcurrentlyResult = concurrently(['echo test'], {
    raw: true,
});

const _result2: ConcurrentlyResult = concurrently2(['echo test'], {
    killOthersOn: ['failure'],
});

const _result3: ConcurrentlyResult = createConcurrently(['echo test'], {
    successCondition: 'all',
});


================================================
FILE: tests\cjs-import\tsconfig.json
================================================
{
  "compilerOptions": {
    "module": "commonjs",
    "outDir": "dist",
    "skipLibCheck": true
  }
}


================================================
FILE: tests\cjs-require\package.json
================================================
{
  "type": "commonjs"
}


================================================
FILE: tests\cjs-require\smoke-test.ts
================================================
// eslint-disable-next-line @typescript-eslint/no-require-imports
import concurrently = require('concurrently');

const { concurrently: concurrently2, createConcurrently } = concurrently;

const _result: concurrently.ConcurrentlyResult = concurrently.default(['echo test'], {
    raw: true,
});

const _result2: concurrently.ConcurrentlyResult = concurrently2(['echo test'], {
    killOthersOn: ['failure'],
});

const _result3: concurrently.ConcurrentlyResult = createConcurrently(['echo test'], {
    successCondition: 'all',
});


================================================
FILE: tests\cjs-require\tsconfig.json
================================================
{
  "compilerOptions": {
    "module": "commonjs",
    "outDir": "dist",
    "skipLibCheck": true
  }
}


================================================
FILE: tests\esm\package.json
================================================
{
  "type": "module"
}


================================================
FILE: tests\esm\smoke-test.ts
================================================
import type { ConcurrentlyResult } from 'concurrently';
import concurrently, { concurrently as concurrently2, createConcurrently } from 'concurrently';

const _result: ConcurrentlyResult = concurrently(['echo test'], {
    raw: true,
});

const _result2: ConcurrentlyResult = concurrently2(['echo test'], {
    killOthersOn: ['failure'],
});

const _result3: ConcurrentlyResult = createConcurrently(['echo test'], {
    successCondition: 'all',
});


================================================
FILE: tests\esm\tsconfig.json
================================================
{
  "compilerOptions": {
    "module": "node20",
    "outDir": "dist",
    "skipLibCheck": true
  }
}

```

## File: .github\FUNDING.yml
```
# Thank you! <3

github: [gustavohenke, paescuj]

```

## File: .github\actions\setup\action.yml
```
name: Setup
description: Setup the environment for the project

inputs:
  node-version:
    description: Node.js version
    required: false
  node-registry:
    description: Node.js package registry to set up for auth
    required: false

runs:
  using: composite
  steps:
    - name: Install Node.js
      uses: actions/setup-node@v5
      with:
        node-version-file: ${{ !inputs.node-version && '.node-version' || '' }}
        node-version: ${{ inputs.node-version }}
        registry-url: ${{ inputs.node-registry }}
        package-manager-cache: false

    - name: Install pnpm
      uses: pnpm/action-setup@v4

    - name: Get pnpm store directory
      id: pnpm-cache-dir
      shell: bash
      run: echo "dir=$(pnpm store path)" >> $GITHUB_OUTPUT

    - name: Setup pnpm cache
      uses: actions/cache@v4
      with:
        path: ${{ steps.pnpm-cache-dir.outputs.dir }}
        key: ${{ runner.os }}-pnpm-store-${{ hashFiles('**/pnpm-lock.yaml') }}
        restore-keys: |
          ${{ runner.os }}-pnpm-store-

    - name: Install dependencies
      shell: bash
      run: pnpm install

```

## File: .github\ISSUE_TEMPLATE\bug-report.yml
```
name: Bug Report
description: File a bug report
body:
  - type: textarea
    attributes:
      label: Describe the bug
      value: |
        <!--

        >> Before getting started, please ensure there's no existing issue with the same concern!

        Please provide the following information:

        - Description: Clear and concise description of what the bug is
        - Expected Behavior: What you expected to happen
        - Environment: At least the OS, Node.js, and concurrently's versions
        - Reproduction: A way to reproduce the issue

        Our time to work on this project is limited.
        With an accurate report you're helping us to understand and solve the request faster.
        Please understand that reports that do not meet the requirements may be closed without further notice.

        Thank you!

        -->
    validations:
      required: true

```

## File: .github\ISSUE_TEMPLATE\config.yml
```
blank_issues_enabled: false

```

## File: .github\ISSUE_TEMPLATE\feature-request.yml
```
name: Feature Request
description: Open a feature request
body:
  - type: textarea
    attributes:
      label: Describe the feature request
      value: |
        <!--

        >> Before getting started, please ensure there's no existing issue with the same concern!

        Please provide the following information:

        - Description: Clear and concise description of what you want
        - Use Case: Why is this needed and what is a use case for it

        Our time to work on this project is limited.
        With an accurate report you're helping us to understand and solve the request faster.
        Please understand that reports that do not meet the requirements may be closed without further notice.

        Thank you!

        -->
    validations:
      required: true

```

## File: .github\workflows\ci.yml
```
name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v5

      - name: Setup
        uses: ./.github/actions/setup

      - name: Lint
        run: pnpm run lint

      - name: Format
        run: pnpm run format

      - name: Typecheck
        run: pnpm run typecheck

  test:
    name: Test (Node.js ${{ matrix.node }}, ${{ matrix.os.name }})
    runs-on: ${{ matrix.os.version }}
    strategy:
      fail-fast: false
      matrix:
        node:
          - 20
          - 22
          - 24
        os:
          - name: Ubuntu
            version: ubuntu-latest
          - name: Windows
            version: windows-latest
          - name: macOS
            version: macOS-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v5

      - name: Setup
        uses: ./.github/actions/setup
        with:
          node-version: ${{ matrix.node }}

      - name: Test
        run: pnpm exec vitest --coverage

      - name: Submit coverage
        uses: coverallsapp/github-action@master
        continue-on-error: true
        with:
          github-token: ${{ secrets.github_token }}
          flag-name: Node.js ${{ matrix.node }} on ${{ matrix.os.name }}
          parallel: true

  coverage:
    name: Coverage
    needs: test
    runs-on: ubuntu-latest
    continue-on-error: true
    steps:
      - name: Finish coverage
        uses: coverallsapp/github-action@master
        with:
          github-token: ${{ secrets.github_token }}
          parallel-finished: true

```

## File: .github\workflows\release.yml
```
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  gh-release:
    name: Create GitHub Release
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v5

      - name: Create release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: gh release create "$GITHUB_REF_NAME" --generate-notes

  publish-npm:
    name: Publish to NPM
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v5

      - name: Setup
        uses: ./.github/actions/setup
        with:
          node-registry: https://registry.npmjs.org

      - name: Publish to NPM
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
          NPM_CONFIG_PROVENANCE: true
        run: pnpm publish --no-git-checks

```

## File: .vscode\extensions.json
```
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "editorconfig.editorconfig",
    "vitest.explorer"
  ]
}

```

## File: .vscode\settings.json
```
{
  // For contributors with the Jest extension installed,
  // it might incorrectly report errors in the suite
  "jest.enable": false,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  },
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[javascript, typescript]": {
    "editor.formatOnSave": false
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "editor.rulers": [100]
}

```

## File: bin\index.spec.ts
```
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import readline from 'node:readline';

import { subscribeSpyTo } from '@hirez_io/observer-spy';
import { sendCtrlC, spawnWithWrapper } from 'ctrlc-wrapper';
import { build } from 'esbuild';
import Rx from 'rxjs';
import { map } from 'rxjs/operators';
import stringArgv from 'string-argv';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { escapeRegExp } from '../lib/utils.js';

const isWindows = process.platform === 'win32';
const createKillMessage = (prefix: string, signal: 'SIGTERM' | 'SIGINT' | string) => {
    const map: Record<string, string | number> = {
        SIGTERM: isWindows ? 1 : '(SIGTERM|143)',
        // Could theoretically be anything (e.g. 0) if process has SIGINT handler
        SIGINT: isWindows ? '(3221225786|0)' : '(SIGINT|130|0)',
    };
    return new RegExp(`${escapeRegExp(prefix)} exited with code ${map[signal] ?? signal}`);
};

let tmpDir: string;

beforeAll(async () => {
    // Build 'concurrently' and store it in a temporary directory
    tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'concurrently-'));
    await build({
        entryPoints: [path.join(__dirname, 'index.ts')],
        platform: 'node',
        bundle: true,
        // it doesn't seem like esbuild is able to change a CJS module to ESM, so target CJS instead.
        // https://github.com/evanw/esbuild/issues/1921
        format: 'cjs',
        outfile: path.join(tmpDir, 'concurrently.cjs'),
    });
    fs.copyFileSync(path.join(__dirname, '..', 'package.json'), path.join(tmpDir, 'package.json'));
}, 8000);

afterAll(() => {
    // Remove the temporary directory where 'concurrently' was stored
    if (tmpDir) {
        fs.rmSync(tmpDir, { recursive: true });
    }
});

/**
 * Creates a child process running 'concurrently' with the given args.
 * Returns observables for its combined stdout + stderr output, close events, pid, and stdin stream.
 */
const run = (args: string, ctrlcWrapper?: boolean) => {
    const spawnFn = ctrlcWrapper ? spawnWithWrapper : spawn;
    const child = spawnFn('node', [path.join(tmpDir, 'concurrently.cjs'), ...stringArgv(args)], {
        cwd: __dirname,
        env: {
            ...process.env,
        },
    });

    const stdout = readline.createInterface({
        input: child.stdout,
    });

    const stderr = readline.createInterface({
        input: child.stderr,
    });

    const log = new Rx.Observable<string>((observer) => {
        stdout.on('line', (line) => {
            observer.next(line);
        });

        stderr.on('line', (line) => {
            observer.next(line);
        });

        child.on('close', () => {
            observer.complete();
        });
    });

    const exit = Rx.firstValueFrom(
        Rx.fromEvent(child, 'exit').pipe(
            map((event) => {
                const exit = event as [number | null, NodeJS.Signals | null];
                return {
                    /** The exit code if the child exited on its own. */
                    code: exit[0],
                    /** The signal by which the child process was terminated. */
                    signal: exit[1],
                };
            }),
        ),
    );

    const getLogLines = async (): Promise<string[]> => {
        const observerSpy = subscribeSpyTo(log);
        await observerSpy.onComplete();
        observerSpy.unsubscribe();
        return observerSpy.getValues();
    };

    return {
        process: child,
        stdin: child.stdin,
        pid: child.pid,
        log,
        getLogLines,
        exit,
    };
};

it('has help command', async () => {
    const exit = await run('--help').exit;

    expect(exit.code).toBe(0);
});

it('prints help when no arguments are passed', async () => {
    const exit = await run('').exit;
    expect(exit.code).toBe(0);
});

describe('has version command', () => {
    const pkg = fs.readFileSync(path.join(__dirname, '..', 'package.json'), 'utf-8');
    const { version } = JSON.parse(pkg);

    it.each(['--version', '-V', '-v'])('%s', async (arg) => {
        const child = run(arg);
        const log = await child.getLogLines();
        expect(log).toContain(version);

        const { code } = await child.exit;
        expect(code).toBe(0);
    });
});

describe('exiting conditions', () => {
    it('is of success by default when running successful commands', async () => {
        const exit = await run('"echo foo" "echo bar"').exit;

        expect(exit.code).toBe(0);
    });

    it('is of failure by default when one of the command fails', async () => {
        const exit = await run('"echo foo" "exit 1"').exit;

        expect(exit.code).toBeGreaterThan(0);
    });

    it('is of success when --success=first and first command to exit succeeds', async () => {
        const exit = await run(
            '--success=first "echo foo" "node __fixtures__/sleep.js 0.5 && exit 1"',
        ).exit;

        expect(exit.code).toBe(0);
    });

    it('is of failure when --success=first and first command to exit fails', async () => {
        const exit = await run(
            '--success=first "exit 1" "node __fixtures__/sleep.js 0.5 && echo foo"',
        ).exit;

        expect(exit.code).toBeGreaterThan(0);
    });

    describe('is of success when --success=last and last command to exit succeeds', () => {
        it.each(['--success=last', '-s last'])('%s', async (arg) => {
            const exit = await run(`${arg} "exit 1" "node __fixtures__/sleep.js 0.5 && echo foo"`)
                .exit;

            expect(exit.code).toBe(0);
        });
    });

    it('is of failure when --success=last and last command to exit fails', async () => {
        const exit = await run(
            '--success=last "echo foo" "node __fixtures__/sleep.js 0.5 && exit 1"',
        ).exit;

        expect(exit.code).toBeGreaterThan(0);
    });

    it('is of success when a SIGINT is sent', async () => {
        // Windows doesn't support sending signals like on POSIX platforms.
        // However, in a console, processes can be interrupted with CTRL+C (like a SIGINT).
        // This is what we simulate here with the help of a wrapper application.
        const child = run('"node __fixtures__/read-echo.js"', isWindows);
        // Wait for command to have started before sending SIGINT
        child.log.subscribe((line) => {
            if (/READING/.test(line)) {
                if (isWindows) {
                    // Instruct the wrapper to send CTRL+C to its child
                    sendCtrlC(child.process);
                } else {
                    process.kill(Number(child.pid), 'SIGINT');
                }
            }
        });
        const lines = await child.getLogLines();
        const exit = await child.exit;

        expect(exit.code).toBe(0);
        expect(lines).toContainEqual(
            expect.stringMatching(
                createKillMessage(
                    '[0] node __fixtures__/read-echo.js',
                    // TODO: Flappy value due to race condition, sometimes killed by concurrently (exit code 1),
                    //       sometimes terminated on its own (exit code 0).
                    //       Related issue: https://github.com/open-cli-tools/concurrently/issues/283
                    isWindows ? '(3221225786|0|1)' : 'SIGINT',
                ),
            ),
        );
    });
});

describe('does not log any extra output', () => {
    it.each(['--raw', '-r'])('%s', async (arg) => {
        const lines = await run(`${arg} "echo foo" "echo bar"`).getLogLines();

        expect(lines).toHaveLength(2);
        expect(lines).toContainEqual(expect.stringContaining('foo'));
        expect(lines).toContainEqual(expect.stringContaining('bar'));
    });
});

describe('--hide', () => {
    it('hides the output of a process by its index', async () => {
        const lines = await run('--hide 1 "echo foo" "echo bar"').getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('foo'));
        expect(lines).not.toContainEqual(expect.stringContaining('bar'));
    });

    it('hides the output of a process by its name', async () => {
        const lines = await run('-n foo,bar --hide bar "echo foo" "echo bar"').getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('foo'));
        expect(lines).not.toContainEqual(expect.stringContaining('bar'));
    });

    it('hides the output of a process by its index in raw mode', async () => {
        const lines = await run('--hide 1 --raw "echo foo" "echo bar"').getLogLines();

        expect(lines).toHaveLength(1);
        expect(lines).toContainEqual(expect.stringContaining('foo'));
        expect(lines).not.toContainEqual(expect.stringContaining('bar'));
    });

    it('hides the output of a process by its name in raw mode', async () => {
        const lines = await run('-n foo,bar --hide bar --raw "echo foo" "echo bar"').getLogLines();

        expect(lines).toHaveLength(1);
        expect(lines).toContainEqual(expect.stringContaining('foo'));
        expect(lines).not.toContainEqual(expect.stringContaining('bar'));
    });
});

describe('--group', () => {
    it('groups output per process', async () => {
        const lines = await run(
            '--group "echo foo && node __fixtures__/sleep.js 1 && echo bar" "echo baz"',
        ).getLogLines();

        expect(lines.slice(0, 4)).toEqual([
            expect.stringContaining('foo'),
            expect.stringContaining('bar'),
            expect.any(String),
            expect.stringContaining('baz'),
        ]);
    });
});

describe('--names', () => {
    describe('prefixes with names', () => {
        it.each(['--names', '-n'])('%s', async (arg) => {
            const lines = await run(`${arg} foo,bar "echo foo" "echo bar"`).getLogLines();

            expect(lines).toContainEqual(expect.stringContaining('[foo] foo'));
            expect(lines).toContainEqual(expect.stringContaining('[bar] bar'));
        });
    });

    it('is split using --name-separator arg', async () => {
        const lines = await run(
            '--names "foo|bar" --name-separator "|" "echo foo" "echo bar"',
        ).getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[foo] foo'));
        expect(lines).toContainEqual(expect.stringContaining('[bar] bar'));
    });
});

describe('specifies custom prefix', () => {
    it.each(['--prefix', '-p'])('%s', async (arg) => {
        const lines = await run(`${arg} command "echo foo" "echo bar"`).getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[echo foo] foo'));
        expect(lines).toContainEqual(expect.stringContaining('[echo bar] bar'));
    });
});

describe('specifies custom prefix length', () => {
    it.each(['--prefix command --prefix-length 5', '-p command -l 5'])('%s', async (arg) => {
        const lines = await run(`${arg} "echo foo" "echo bar"`).getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[ec..o] foo'));
        expect(lines).toContainEqual(expect.stringContaining('[ec..r] bar'));
    });
});

describe('--pad-prefix', () => {
    it('pads prefixes with spaces', async () => {
        const lines = await run('--pad-prefix -n foo,barbaz "echo foo" "echo bar"').getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[foo   ]'));
        expect(lines).toContainEqual(expect.stringContaining('[barbaz]'));
    });
});

describe('--restart-tries', () => {
    it('changes how many times a command will restart', async () => {
        const lines = await run('--restart-tries 1 "exit 1"').getLogLines();

        expect(lines).toEqual([
            expect.stringContaining('[0] exit 1 exited with code 1'),
            expect.stringContaining('[0] exit 1 restarted'),
            expect.stringContaining('[0] exit 1 exited with code 1'),
        ]);
    });
});

describe('--kill-others', () => {
    describe('kills on success', () => {
        it.each(['--kill-others', '-k'])('%s', async (arg) => {
            const lines = await run(
                `${arg} "node __fixtures__/sleep.js 10" "exit 0"`,
            ).getLogLines();

            expect(lines).toContainEqual(expect.stringContaining('[1] exit 0 exited with code 0'));
            expect(lines).toContainEqual(
                expect.stringContaining('Sending SIGTERM to other processes'),
            );
            expect(lines).toContainEqual(
                expect.stringMatching(
                    createKillMessage('[0] node __fixtures__/sleep.js 10', 'SIGTERM'),
                ),
            );
        });
    });

    it('kills on failure', async () => {
        const lines = await run(
            '--kill-others "node __fixtures__/sleep.js 10" "exit 1"',
        ).getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[1] exit 1 exited with code 1'));
        expect(lines).toContainEqual(expect.stringContaining('Sending SIGTERM to other processes'));
        expect(lines).toContainEqual(
            expect.stringMatching(
                createKillMessage('[0] node __fixtures__/sleep.js 10', 'SIGTERM'),
            ),
        );
    });
});

describe('--kill-others-on-fail', () => {
    it('does not kill on success', async () => {
        const lines = await run(
            '--kill-others-on-fail "node __fixtures__/sleep.js 0.5" "exit 0"',
        ).getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[1] exit 0 exited with code 0'));
        expect(lines).toContainEqual(
            expect.stringContaining('[0] node __fixtures__/sleep.js 0.5 exited with code 0'),
        );
    });

    it('kills on failure', async () => {
        const lines = await run(
            '--kill-others-on-fail "node __fixtures__/sleep.js 10" "exit 1"',
        ).getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[1] exit 1 exited with code 1'));
        expect(lines).toContainEqual(expect.stringContaining('Sending SIGTERM to other processes'));
        expect(lines).toContainEqual(
            expect.stringMatching(
                createKillMessage('[0] node __fixtures__/sleep.js 10', 'SIGTERM'),
            ),
        );
    });
});

describe('--handle-input', () => {
    describe('forwards input to first process by default', () => {
        it.each(['--handle-input', '-i'])('%s', async (arg) => {
            const child = run(`${arg} "node __fixtures__/read-echo.js"`);
            child.log.subscribe((line) => {
                if (/READING/.test(line)) {
                    child.stdin.write('stop\n');
                }
            });
            const lines = await child.getLogLines();
            const exit = await child.exit;

            expect(exit.code).toBe(0);
            expect(lines).toContainEqual(expect.stringContaining('[0] stop'));
            expect(lines).toContainEqual(
                expect.stringContaining('[0] node __fixtures__/read-echo.js exited with code 0'),
            );
        });
    });

    it('forwards input to process --default-input-target', async () => {
        const child = run(
            '-ki --default-input-target 1 "node __fixtures__/read-echo.js" "node __fixtures__/read-echo.js"',
        );
        child.log.subscribe((line) => {
            if (/\[1\] READING/.test(line)) {
                child.stdin.write('stop\n');
            }
        });
        const lines = await child.getLogLines();
        const exit = await child.exit;

        expect(exit.code).toBeGreaterThan(0);
        expect(lines).toContainEqual(expect.stringContaining('[1] stop'));
        expect(lines).toContainEqual(
            expect.stringMatching(
                createKillMessage('[0] node __fixtures__/read-echo.js', 'SIGTERM'),
            ),
        );
    });

    it('forwards input to specified process', async () => {
        const child = run('-ki "node __fixtures__/read-echo.js" "node __fixtures__/read-echo.js"');
        child.log.subscribe((line) => {
            if (/\[1\] READING/.test(line)) {
                child.stdin.write('1:stop\n');
            }
        });
        const lines = await child.getLogLines();
        const exit = await child.exit;

        expect(exit.code).toBeGreaterThan(0);
        expect(lines).toContainEqual(expect.stringContaining('[1] stop'));
        expect(lines).toContainEqual(
            expect.stringMatching(
                createKillMessage('[0] node __fixtures__/read-echo.js', 'SIGTERM'),
            ),
        );
    });
});

describe('--teardown', () => {
    it('runs teardown commands when input commands exit', async () => {
        const lines = await run('--teardown "echo bye" "echo hey"').getLogLines();
        expect(lines).toEqual([
            expect.stringContaining('[0] hey'),
            expect.stringContaining('[0] echo hey exited with code 0'),
            expect.stringContaining('--> Running teardown command "echo bye"'),
            expect.stringContaining('bye'),
            expect.stringContaining('--> Teardown command "echo bye" exited with code 0'),
        ]);
    });

    it('runs multiple teardown commands', async () => {
        const lines = await run(
            '--teardown "echo bye" --teardown "echo bye2" "echo hey"',
        ).getLogLines();
        expect(lines).toContain('bye');
        expect(lines).toContain('bye2');
    });
});

describe('--timings', () => {
    const defaultTimestampFormatRegex = /\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}/;
    const tableTopBorderRegex = /^--> ┌[─┬]+┐$/;
    const tableHeaderRowRegex = /^--> │ name +│ duration +│ exit code +│ killed +│ command +│$/;
    const tableBottomBorderRegex = /^--> └[─┴]+┘$/;

    const timingsTests = {
        'shows timings on success': ['node __fixtures__/sleep.js 0.5', 'exit 0'],
        'shows timings on failure': ['node __fixtures__/sleep.js 0.75', 'exit 1'],
    };
    it.each(Object.entries(timingsTests))('%s', async (_, commands) => {
        const lines = await run(
            `--timings ${commands.map((command) => `"${command}"`).join(' ')}`,
        ).getLogLines();

        // Expect output to contain process start / stop messages for each command
        commands.forEach((command, index) => {
            const escapedCommand = escapeRegExp(command);
            expect(lines).toContainEqual(
                expect.stringMatching(
                    new RegExp(
                        `^\\[${index}] ${escapedCommand} started at ${defaultTimestampFormatRegex.source}$`,
                    ),
                ),
            );
            expect(lines).toContainEqual(
                expect.stringMatching(
                    new RegExp(
                        `^\\[${index}] ${escapedCommand} stopped at ${defaultTimestampFormatRegex.source} after (\\d|,)+ms$`,
                    ),
                ),
            );
        });

        // Expect output to contain timings table
        expect(lines).toContainEqual(expect.stringMatching(tableTopBorderRegex));
        expect(lines).toContainEqual(expect.stringMatching(tableHeaderRowRegex));
        expect(lines).toContainEqual(expect.stringMatching(tableBottomBorderRegex));
    });
});

describe('--passthrough-arguments', () => {
    it('argument placeholders are properly replaced when passthrough-arguments is enabled', async () => {
        const lines = await run('--passthrough-arguments "echo {1}" -- echo').getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[0] echo echo exited with code 0'));
    });

    it('argument placeholders are not replaced when passthrough-arguments is disabled', async () => {
        const lines = await run('"echo {1}" -- echo').getLogLines();

        expect(lines).toContainEqual(expect.stringContaining('[0] echo {1} exited with code 0'));
        expect(lines).toContainEqual(expect.stringContaining('[1] echo exited with code 0'));
    });
});

```

## File: bin\index.ts
```
#!/usr/bin/env node
import process from 'node:process';

import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

import { assertDeprecated } from '../lib/assert.js';
import * as defaults from '../lib/defaults.js';
import { concurrently } from '../lib/index.js';
import { castArray } from '../lib/utils.js';
import { readPackageJson } from './read-package-json.js';

const version = String(readPackageJson().version);
const epilogue = `For documentation and more examples, visit:\nhttps://github.com/open-cli-tools/concurrently/tree/v${version}/docs`;

// Clean-up arguments (yargs expects only the arguments after the program name)
const program = yargs(hideBin(process.argv))
    .parserConfiguration({
        // Avoids options that can be specified multiple times from requiring a `--` to pass commands
        'greedy-arrays': false,
        // Makes sure that --passthrough-arguments works correctly
        'populate--': true,
    })
    .usage('$0 [options] <command ...>')
    .help('h')
    .alias('h', 'help')
    .version(version)
    .alias('version', 'v')
    .alias('version', 'V')
    // TODO: Add some tests for this.
    .env('CONCURRENTLY')
    .options({
        // General
        'max-processes': {
            alias: 'm',
            describe:
                'How many processes should run at once.\n' +
                'New processes only spawn after all restart tries of a process.\n' +
                'Exact number or a percent of CPUs available (for example "50%")',
            type: 'string',
        },
        names: {
            alias: 'n',
            describe:
                'List of custom names to be used in prefix template.\n' +
                'Example names: "main,browser,server"',
            type: 'string',
        },
        'name-separator': {
            describe:
                'The character to split <names> on. Example usage:\n' +
                '-n "styles|scripts|server" --name-separator "|"',
            default: defaults.nameSeparator,
        },
        success: {
            alias: 's',
            describe:
                'Which command(s) must exit with code 0 in order for concurrently exit with ' +
                'code 0 too. Options are:\n' +
                '- "first" for the first command to exit;\n' +
                '- "last" for the last command to exit;\n' +
                '- "all" for all commands;\n' +
                // Note: not a typo. Multiple commands can have the same name.
                '- "command-{name}"/"command-{index}" for the commands with that name or index;\n' +
                '- "!command-{name}"/"!command-{index}" for all commands but the ones with that ' +
                'name or index.\n',
            default: defaults.success,
        },
        raw: {
            alias: 'r',
            describe:
                'Output only raw output of processes, disables prettifying ' +
                'and concurrently coloring.',
            type: 'boolean',
        },
        // This one is provided for free. Chalk reads this itself and removes colors.
        // https://www.npmjs.com/package/chalk#supportscolor
        'no-color': {
            describe: 'Disables colors from logging',
            type: 'boolean',
        },
        hide: {
            describe:
                'Comma-separated list of processes to hide the output.\n' +
                'The processes can be identified by their name or index.',
            default: defaults.hide,
            type: 'string',
        },
        group: {
            alias: 'g',
            describe: 'Order the output as if the commands were run sequentially.',
            type: 'boolean',
        },
        timings: {
            describe: 'Show timing information for all processes.',
            type: 'boolean',
            default: defaults.timings,
        },
        'passthrough-arguments': {
            alias: 'P',
            describe:
                'Passthrough additional arguments to commands (accessible via placeholders) ' +
                'instead of treating them as commands.',
            type: 'boolean',
            default: defaults.passthroughArguments,
        },
        teardown: {
            describe:
                'Clean up command(s) to execute before exiting concurrently. Might be specified multiple times.\n' +
                "These aren't prefixed and they don't affect concurrently's exit code.",
            type: 'string',
            array: true,
        },

        // Kill others
        'kill-others': {
            alias: 'k',
            describe: 'Kill other processes once the first exits.',
            type: 'boolean',
        },
        'kill-others-on-fail': {
            describe: 'Kill other processes if one exits with non zero status code.',
            type: 'boolean',
        },
        'kill-signal': {
            alias: 'ks',
            describe:
                'Signal to send to other processes if one exits or dies. (SIGTERM/SIGKILL, defaults to SIGTERM)',
            type: 'string',
            default: defaults.killSignal,
        },
        'kill-timeout': {
            describe: 'How many milliseconds to wait before forcing process terminating.',
            type: 'number',
        },

        // Prefix
        prefix: {
            alias: 'p',
            describe:
                'Prefix used in logging for each process.\n' +
                'Possible values: index, pid, time, command, name, none, or a template. ' +
                'Example template: "{time}-{pid}"',
            defaultDescription: 'index or name (when --names is set)',
            type: 'string',
        },
        'prefix-colors': {
            alias: 'c',
            describe:
                'Comma-separated list of Chalk colors to use on prefixes. ' +
                'If there are more commands than colors, the last color will be repeated.\n' +
                '- Available modifiers: reset, bold, dim, italic, underline, inverse, hidden, strikethrough\n' +
                '- Available colors: black, red, green, yellow, blue, magenta, cyan, white, gray, \n' +
                'any hex values for colors (e.g. #23de43) or auto for an automatically picked color\n' +
                '- Available background colors: bgBlack, bgRed, bgGreen, bgYellow, bgBlue, bgMagenta, bgCyan, bgWhite\n' +
                'See https://www.npmjs.com/package/chalk for more information.',
            default: defaults.prefixColors,
            type: 'string',
        },
        'prefix-length': {
            alias: 'l',
            describe:
                'Limit how many characters of the command is displayed in prefix. ' +
                'The option can be used to shorten the prefix when it is set to "command"',
            default: defaults.prefixLength,
            type: 'number',
        },
        'pad-prefix': {
            describe: 'Pads short prefixes with spaces so that the length of all prefixes match',
            type: 'boolean',
        },
        'timestamp-format': {
            alias: 't',
            describe:
                'Specify the timestamp in Unicode format:\n' +
                'https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table',
            default: defaults.timestampFormat,
            type: 'string',
        },

        // Restarting
        'restart-tries': {
            describe:
                'How many times a process that died should restart.\n' +
                'Negative numbers will make the process restart forever.',
            default: defaults.restartTries,
            type: 'number',
        },
        'restart-after': {
            describe: 'Delay before restarting the process, in milliseconds, or "exponential".',
            default: defaults.restartDelay,
            type: 'string',
        },

        // Input
        'handle-input': {
            alias: 'i',
            describe:
                'Whether input should be forwarded to the child processes. ' +
                'See examples for more information.',
            type: 'boolean',
        },
        'default-input-target': {
            default: defaults.defaultInputTarget,
            describe:
                'Identifier for child process to which input on stdin ' +
                'should be sent if not specified at start of input.\n' +
                'Can be either the index or the name of the process.',
        },
    })
    .group(
        ['m', 'n', 'name-separator', 's', 'r', 'no-color', 'hide', 'g', 'timings', 'P', 'teardown'],
        'General',
    )
    .group(['p', 'c', 'l', 't', 'pad-prefix'], 'Prefix styling')
    .group(['i', 'default-input-target'], 'Input handling')
    .group(['k', 'kill-others-on-fail', 'kill-signal', 'kill-timeout'], 'Killing other processes')
    .group(['restart-tries', 'restart-after'], 'Restarting')
    .epilogue(epilogue);

const args = program.parseSync();
assertDeprecated(
    args.nameSeparator === defaults.nameSeparator,
    'name-separator',
    'Use commas as name separators instead.',
);

// Get names of commands by the specified separator
const names = (args.names || '').split(args.nameSeparator);

const additionalArguments = castArray(args['--'] ?? []).map(String);
const commands = args.passthroughArguments ? args._ : args._.concat(additionalArguments);

if (!commands.length) {
    program.showHelp();
    process.exit();
}

concurrently(
    commands.map((command, index) => ({
        command: String(command),
        name: names[index],
    })),
    {
        handleInput: args.handleInput,
        defaultInputTarget: args.defaultInputTarget,
        killOthersOn: args.killOthers
            ? ['success', 'failure']
            : args.killOthersOnFail
              ? ['failure']
              : [],
        killSignal: args.killSignal,
        killTimeout: args.killTimeout,
        maxProcesses: args.maxProcesses,
        raw: args.raw,
        hide: args.hide.split(','),
        group: args.group,
        prefix: args.prefix,
        prefixColors: args.prefixColors.split(','),
        prefixLength: args.prefixLength,
        padPrefix: args.padPrefix,
        restartDelay:
            args.restartAfter === 'exponential' ? 'exponential' : Number(args.restartAfter),
        restartTries: args.restartTries,
        successCondition: args.success,
        timestampFormat: args.timestampFormat,
        timings: args.timings,
        teardown: args.teardown,
        additionalArguments: args.passthroughArguments ? additionalArguments : undefined,
    },
).result.then(
    () => process.exit(0),
    () => process.exit(1),
);

```

## File: bin\read-package-json.ts
```
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';

/**
 * Read the package.json file of `concurrently`
 */
export function readPackageJson(): Record<string, unknown> {
    let resolver;
    try {
        resolver = require.resolve;
    } catch {
        resolver = createRequire(import.meta.url).resolve;
    }
    const path = resolver('concurrently/package.json');
    const content = readFileSync(path, 'utf8');
    return JSON.parse(content);
}

```

## File: bin\__fixtures__\read-echo.js
```
import process from 'node:process';

process.stdin.on('data', (chunk) => {
    const line = chunk.toString().trim();
    console.log(line);

    if (line === 'stop') {
        process.exit(0);
    }
});

console.log('READING');

```

## File: bin\__fixtures__\sleep.js
```
/*
 * Platform independent implementation of 'sleep' used as a command in tests
 *
 * (Windows doesn't provide the 'sleep' command by default,
 * see https://github.com/open-cli-tools/concurrently/issues/277)
 */
import process from 'node:process';

const seconds = +process.argv[2];
if (!seconds || Number.isNaN(seconds) || process.argv.length > 3) {
    // Mimic behavior from native 'sleep' command
    console.error('usage: sleep seconds');
    process.exit(1);
}

await new Promise((resolve) => setTimeout(resolve, seconds * 1000));

```

## File: docs\README.md
```
# Concurrently Documentation

## CLI

These articles cover using concurrently through CLI:

- [Prefixing](./cli/prefixing.md)
- [Output Control](./cli/output-control.md)
- [Success Conditions](./cli/success.md)
- [Shortcuts](./cli/shortcuts.md)
- [Terminating Commands](./cli/terminating.md)
- [Restarting Commands](./cli/restarting.md)
- [Input Handling](./cli/input-handling.md)
- [Passthrough Arguments](./cli/passthrough-arguments.md)
- [Configuration](./cli/configuration.md)

```

## File: docs\cli\configuration.md
```
# Configuration

You might want to configure concurrently to always have certain flags on.
Any of concurrently's flags can be set via environment variables that are prefixed with `CONCURRENTLY_`.

```bash
$ export CONCURRENTLY_KILL_OTHERS=true
$ export CONCURRENTLY_HANDLE_INPUT=true
# Equivalent to passing --kill-others and --handle-input
$ concurrently nodemon "echo 'hey nodemon, you won't last long'"
```

```

## File: docs\cli\input_handling.md
```
# Input Handling

By default, concurrently doesn't send input to any commands it spawns.<br/>
In the below example, typing `rs` to manually restart [nodemon](https://nodemon.io/) does nothing:

```bash
$ concurrently 'nodemon' 'npm run watch-js'
rs
```

To turn on input handling, it's necessary to set the `--handle-input`/`-i` flag.<br/>
This will send `rs` to the first command:

```bash
$ concurrently --handle-input 'nodemon' 'npm run watch-js'
rs
```

To send input to a different command instead, it's possible to prefix the input with the command index, followed by a `:`.<br/>
For example, the below sends `rs` to the second command:

```bash
$ concurrently --handle-input 'npm run watch-js' 'nodemon'
1:rs
```

If the command has a name, it's also possible to target it using that command's name:

```bash
$ concurrently --handle-input --names js,server 'npm run watch-js' 'nodemon'
server:rs
```

It's also possible to change the default command that receives input.<br/>
To do this, set the `--default-input-target` flag to a command's index or name.

```bash
$ concurrently --handle-input --default-input-target 1 'npm run watch-js' 'nodemon'
rs
```

```

## File: docs\cli\output_control.md
```
# Output Control

concurrently offers a few ways to control a command's output.

## Hiding

A command's outputs (and all its events) can be hidden by using the `--hide` flag.

```bash
$ concurrently --hide 0 'echo Hello there' 'echo General Kenobi!'
[1] General Kenobi!
[1] echo 'General Kenobi!' exited with code 0
```

## Grouping

It might be useful at times to make sure that the commands outputs are grouped together, while running them in parallel.<br/>
This can be done with the `--group` flag.

```bash
$ concurrently --group 'echo Hello there && sleep 2 && echo General Kenobi!' 'echo hi Star Wars fans'
[0] Hello there
[0] General Kenobi!
[0] echo Hello there && sleep 2 && echo 'General Kenobi!' exited with code 0
[1] hi Star Wars fans
[1] echo hi Star Wars fans exited with code 0
```

## No Colors

When piping concurrently's outputs to another command or file, you might want to force it to not use colors, as these can break the other command's parsing, or reduce the legibility of the output in non-terminal environments.

```bash
$ concurrently -c red,blue --no-color 'echo Hello there' 'echo General Kenobi!'
```

```

## File: docs\cli\passthrough_arguments.md
```
# Passthrough Arguments

If you have a shortcut for running a specific combination of commands through concurrently,
you might need at some point to pass additional arguments/flags to some of these.

For example, imagine you have in your `package.json` file scripts like this:

```jsonc
{
  // ...
  "scripts": {
    "build:client": "tsc -p client",
    "build:server": "tsc -p server",
    "build": "concurrently npm:build:client npm:build:server",
  },
}
```

If you wanted to run only either `build:server` or `build:client` with an additional `--noEmit` flag,
you can do so with `npm run build:server -- --noEmit`, for example.<br/>
However, if you want to do that while using concurrently, as `npm run build -- --noEmit` for example,
you might find that concurrently actually parses `--noEmit` as its own flag, which does nothing,
because it doesn't exist.

To solve this, you can set the `--passthrough-arguments`/`-P` flag, which instructs concurrently to
take everything after a `--` as additional arguments that are passed through to the input commands
via a few placeholder styles:

## Single argument

We can modify the original `build` script to pass a single additional argument/flag to a script by using
a 1-indexed `{number}` placeholder to the command you want it to apply to:

```jsonc
{
  // ...
  "scripts": {
    // ...
    "build": "concurrently -P 'npm:build:client -- {1}' npm:build:server --",
    "typecheck": "npm run build -- --noEmit",
  },
}
```

With this, running `npm run typecheck` will pass `--noEmit` only to `npm run build:client`.

## All arguments

In the original `build` example script, you're more likely to want to pass every additional argument/flag
to your commands. This can be done with the `{@}` placeholder.

```jsonc
{
  // ...
  "scripts": {
    // ...
    "build": "concurrently -P 'npm:build:client -- {@}' 'npm:build:server -- {@}' --",
    "typecheck": "npm run build -- --watch --noEmit",
  },
}
```

In the above example, both `--watch` and `--noEmit` are passed to each command.

## All arguments, combined

If for some reason you wish to combine all additional arguments into a single one, you can do that with the `{*}` placeholder,
which wraps the arguments in quotes.

```jsonc
{
  // ...
  "scripts": {
    // ...
    "build": "concurrently -P 'npm:build:client -- --outDir {*}/client' 'npm:build:server -- --outDir {*}/server' -- $(date)",
  },
}
```

In the above example, the output of the `date` command, which looks like `Sun  1 Sep 2024 23:50:00 AEST` will be passed as a single string to the `--outDir` parameter of both commands.

```

## File: docs\cli\prefixing.md
```
# Prefixing

## Prefix Styles

concurrently will by default prefix each command's outputs with a zero-based index, wrapped in square brackets:

```bash
$ concurrently 'echo Hello there' "echo 'General Kenobi!'"
[0] Hello there
[1] General Kenobi!
[0] echo Hello there exited with code 0
[1] echo 'General Kenobi!' exited with code 0
```

If you've given the commands names, they are used instead:

```bash
$ concurrently --names one,two 'echo Hello there' "echo 'General Kenobi!'"
[one] Hello there
[two] General Kenobi!
[one] echo Hello there exited with code 0
[two] echo 'General Kenobi!' exited with code 0
```

There are other prefix styles available too:

| Style     | Description                       |
| --------- | --------------------------------- |
| `index`   | Zero-based command's index        |
| `name`    | The command's name                |
| `command` | The command's line                |
| `time`    | Time of output                    |
| `pid`     | ID of the command's process (PID) |
| `none`    | No prefix                         |

Any of these can be used by setting the `--prefix`/`-p` flag. For example:

```bash
$ concurrently --prefix pid 'echo Hello there' 'echo General Kenobi!'
[2222] Hello there
[2223] General Kenobi!
[2222] echo Hello there exited with code 0
[2223] echo 'General Kenobi!' exited with code 0
```

It's also possible to have a prefix based on a template. Any of the styles listed above can be used by wrapping it in `{}`.
Doing so will also remove the square brackets:

```bash
$ concurrently --prefix '{index}-{pid}' 'echo Hello there' 'echo General Kenobi!'
0-2222 Hello there
1-2223 General Kenobi!
0-2222 echo Hello there exited with code 0
1-2223 echo 'General Kenobi!' exited with code 0
```

## Prefix Colors

By default, there are no colors applied to concurrently prefixes, and they just use whatever the terminal's defaults are.

This can be changed by using the `--prefix-colors`/`-c` flag, which takes a comma-separated list of colors to use.<br/>
The available values are color names (e.g. `green`, `magenta`, `gray`, etc), a hex value (such as `#23de43`), or `auto`, to automatically select a color.

```bash
$ concurrently -c red,blue 'echo Hello there' 'echo General Kenobi!'
```

<details>
<summary>List of available color names</summary>

- `black`
- `blue`
- `cyan`
- `green`
- `gray`
- `magenta`
- `red`
- `white`
- `yellow`
</details>

Colors can take modifiers too. Several can be applied at once by appending `.<modifier 1>.<modifier 2>` and so on.

```bash
$ concurrently -c '#23de43.inverse,bold.blue.dim' 'echo Hello there' 'echo General Kenobi!'
```

<details>
<summary>List of available modifiers</summary>

- `reset`
- `bold`
- `dim`
- `hidden`
- `inverse`
- `italic`
- `strikethrough`
- `underline`
</details>

A background color can be set in a similarly fashion.

```bash
$ concurrently -c bgGray,red.bgBlack 'echo Hello there' 'echo General Kenobi!'
```

<details>
<summary>List of available background color names</summary>

- `bgBlack`
- `bgBlue`
- `bgCyan`
- `bgGreen`
- `bgGray`
- `bgMagenta`
- `bgRed`
- `bgWhite`
- `bgYellow`
</details>

## Prefix Length

When using the `command` prefix style, it's possible that it'll be too long.<br/>
It can be limited by setting the `--prefix-length`/`-l` flag:

```bash
$ concurrently -p command -l 10 'echo Hello there' 'echo General Kenobi!'
[echo..here] Hello there
[echo..bi!'] General Kenobi!
[echo..here] echo Hello there exited with code 0
[echo..bi!'] echo 'General Kenobi!' exited with code 0
```

It's also possible that some prefixes are too short, and you want all of them to have the same length.<br/>
This can be done by setting the `--pad-prefix` flag:

```bash
$ concurrently -n foo,barbaz --pad-prefix 'echo Hello there' 'echo General Kenobi!'
[foo   ] Hello there
[foo   ] echo Hello there exited with code 0
[barbaz] General Kenobi!
[barbaz] echo 'General Kenobi!' exited with code 0
```

> [!NOTE]
> If using the `pid` prefix style in combination with [`--restart-tries`](./restarting.md), the length of the PID might grow, in which case all subsequent lines will match the new length.<br/>
> This might happen, for example, if the PID was 99 and it's now 100.

```

## File: docs\cli\restarting.md
```
# Restarting Commands

Sometimes it's useful to have commands that exited with a non-zero status to restart automatically.<br/>
concurrently lets you configure how many times you wish for such a command to restart through the `--restart-tries` flag:

```bash
$ concurrently --restart-tries 2 'exit 1'
[0] exit 1 exited with code 1
[0] exit 1 restarted
[0] exit 1 exited with code 1
[0] exit 1 restarted
[0] exit 1 exited with code 1
```

Sometimes, it might be interesting to have commands wait before restarting.<br/>
To do this, simply set `--restart-after` to a the number of milliseconds you'd like to delay restarting.

```bash
$ concurrently -p time --restart-tries 1 --restart-after 3000 'exit 1'
[2024-09-01 23:43:55.871] exit 1 exited with code 1
[2024-09-01 23:43:58.874] exit 1 restarted
[2024-09-01 23:43:58.891] exit 1 exited with code 1
```

If a command is not having success spawning, you might want to instead apply an exponential back-off.<br/>
Set `--restart-after exponential` to have commands respawn with a `2^N` seconds delay.

```bash
$ concurrently -p time --restart-tries 3 --restart-after exponential 'exit 1'

[2024-09-01 23:49:01.124] exit 1 exited with code 1
[2024-09-01 23:49:02.127] exit 1 restarted
[2024-09-01 23:49:02.139] exit 1 exited with code 1
[2024-09-01 23:49:04.141] exit 1 restarted
[2024-09-01 23:49:04.157] exit 1 exited with code 1
[2024-09-01 23:49:08.158] exit 1 restarted
[2024-09-01 23:49:08.174] exit 1 exited with code 1
```

```

## File: docs\cli\shortcuts.md
```
# Command Shortcuts

Package managers that execute scripts from a `package.json` or `deno.(json|jsonc)` file can be shortened when in concurrently.<br/>
The following are supported:

| Syntax          | Expands to            |
| --------------- | --------------------- |
| `npm:<script>`  | `npm run <script>`    |
| `pnpm:<script>` | `pnpm run <script>`   |
| `yarn:<script>` | `yarn run <script>`   |
| `bun:<script>`  | `bun run <script>`    |
| `node:<script>` | `node --run <script>` |
| `deno:<script>` | `deno task <script>`  |

> [!NOTE]
>
> `node --run` is only available from [Node 22 onwards](https://nodejs.org/en/blog/announcements/v22-release-announce#running-packagejson-scripts).

For example, given the following `package.json` contents:

```jsonc
{
  // ...
  "scripts": {
    "lint:js": "...",
    "lint:ts": "...",
    "lint:fix:js": "...",
    "lint:fix:ts": "...",
    // ...
  },
  // ...
}
```

It's possible to run some of these with the following command line:

```bash
$ concurrently 'pnpm:lint:js'
# Is equivalent to
$ concurrently -n lint:js 'pnpm run lint:js'
```

Note that the command automatically receives a name equal to the script name.

If you have several scripts with similar name patterns, you can use the `*` wildcard to run all of them at once.<br/>
The spawned commands will receive names set to whatever the `*` wildcard matched.

```bash
$ concurrently 'npm:lint:fix:*'
# is equivalent to
$ concurrently -n js,ts 'npm run lint:fix:js' 'npm run lint:fix:ts'
```

If you specify a command name when using wildcards, it'll be a prefix of what the `*` wildcard matched:

```bash
$ concurrently -n fix: 'npm:lint:fix:*'
# is equivalent to
$ concurrently -n fix:js,fix:ts 'npm run lint:fix:js' 'npm run lint:fix:ts'
```

Filtering out commands matched by wildcard is also possible. Do this with by including `(!<some pattern>)` in the command line:

```bash
$ concurrently 'yarn:lint:*(!fix)'
# is equivalent to
$ concurrently -n js,ts 'yarn run lint:js' 'yarn run lint:ts'
```

> [!NOTE]
> If you use this syntax with double quotes (`"`), bash and other shells might fail
> parsing it. You'll need to escape the `!`, or use single quote (`'`) instead.<br/>
> See [here](https://serverfault.com/a/208266/160539) for more information.

```

## File: docs\cli\success.md
```
# Success Conditions

When you're using concurrently in shell scripts or CI pipelines, the exit code matters.  
It determines whether the next step runs, or if the script stops with a failure.

You can control concurrently's exit code using the `--success` flag.  
This tells it **which command(s)** must succeed (exit with code `0`) for concurrently to return success overall.

There are several possible values:

## `all`

All commands must exit with code `0`.
This is the default value.

## `first`

The first command to exit must do so with code `0`.

```bash
# ✅ Exits with code 0 — second command exits first and succeeds
$ concurrently --success first 'sleep 1 && exit 1' 'exit 0'

# ❌ Exits with a non-zero code — second command exits first, but with code 1
$ concurrently --success first 'sleep 1 && exit 0' 'exit 1'
```

## `last`

The last command to exit must do so with code `0`.

```bash
# ✅ Exits with code 0 - first command exits last and succeeds
$ concurrently --success last 'sleep 1 && exit 0' 'exit 1'

# ❌ Exits with a non-zero code — first command exits last, but with code 1
$ concurrently --success last 'sleep 1 && exit 1' 'exit 0'
```

## `command-{name}` or `command-{index}`

A specific command, by name or index, must exit with code `0`.

```bash
# Exits with code 0 only if 'npm test' (index 1) passes.
$ concurrently --success command-1 --kill-others 'npm run server' 'npm test'

# Exits with code 0 only if 'test' command passes.
$ concurrently --success command-test --names server,test --kill-others \
    'npm start' \
    'npm test'
```

> [!TIP]
> Use `--kill-others` to kill a long-running process, such as a server, once tests pass.

## `!command-{name}` or `!command-{index}`

All but a specific command, by name or index, must exit with code `0`.

```bash
# Ignores 'npm start'; all others must succeed
$ concurrently --success '!command-2' --kill-others \
    'npm test' \
    'npm build' \
    'npm start'

# Ignores 'server'; all others must succeed
$ concurrently --success '!command-server' --names test,build,server --kill-others \
    'npm test' \
    'npm build' \
    'npm start'
```

```

## File: docs\cli\terminating.md
```
# Terminating Commands

It's possible to have concurrently terminate other commands when one of them exits.<br/>
This can be done in the following ways:

## Terminating on either success or error

By using the `--kill-others` flag, concurrently will terminate other commands once the first one exits,
no matter the exit code.<br/>
This is useful to terminate the server process once the test is done.

```bash
$ concurrently --kill-others --names server,test 'npm start' 'npm test'
```

## Terminating on error only

By using the `--kill-others-on-fail` flag, concurrently will terminate other commands any command
exits with a non-zero code.<br/>
This is useful if you're building multiple applications, and you want to abort the others once you know
that any of them is broken.

```bash
$ concurrently --kill-others-on-fail 'npm run app1:build' 'npm run app2:build'
```

## Configuring termination

### Kill Signal

It's possible to configure which signal you want to send when terminating commands with the `--kill-signal` flag.
The default is `SIGTERM`, but it's also possible to send `SIGKILL`.

```bash
$ concurrently --kill-others --kill-signal SIGKILL 'npm start' 'npm test'
```

### Timeout

In case you have a misbehaving process that ignores the kill signal, you can force kill it after some
timeout (in milliseconds) by using the `--kill-timeout` flag.
This sends a `SIGKILL`, which cannot be caught.

```bash
$ concurrently --kill-others --kill-timeout 1000 'sleep 1 && echo bye' './misbehaving'
[0] bye
[0] sleep 1 && echo bye exited with code 0
--> Sending SIGTERM to other processes..
[1] IGNORING SIGNAL
--> Sending SIGKILL to 1 processes..
[1] ./misbehaving exited with code SIGKILL
```

```

## File: lib\assert.spec.ts
```
import { afterEach, describe, expect, it, vi } from 'vitest';

import { assertDeprecated } from './assert.js';

describe('#assertDeprecated()', () => {
    const consoleMock = vi.spyOn(console, 'warn').mockImplementation(() => {});

    afterEach(() => {
        vi.clearAllMocks();
    });

    it('prints warning with name and message when condition is false', () => {
        assertDeprecated(false, 'example-flag', 'This is an example message.');

        expect(consoleMock).toHaveBeenLastCalledWith(
            '[concurrently] example-flag is deprecated. This is an example message.',
        );
    });

    it('prints same warning only once', () => {
        assertDeprecated(false, 'example-flag', 'This is an example message.');
        assertDeprecated(false, 'different-flag', 'This is another message.');

        expect(consoleMock).toBeCalledTimes(1);
        expect(consoleMock).toHaveBeenLastCalledWith(
            '[concurrently] different-flag is deprecated. This is another message.',
        );
    });

    it('prints nothing if condition is true', () => {
        assertDeprecated(true, 'example-flag', 'This is an example message.');

        expect(consoleMock).not.toHaveBeenCalled();
    });
});

```

## File: lib\assert.ts
```
const deprecations = new Set<string>();

/**
 * Asserts that some condition is true, and if not, prints a warning about it being deprecated.
 * The message is printed only once.
 */
export function assertDeprecated(check: boolean, name: string, message: string) {
    if (!check && !deprecations.has(name)) {
        // eslint-disable-next-line no-console
        console.warn(`[concurrently] ${name} is deprecated. ${message}`);
        deprecations.add(name);
    }
}

```

## File: lib\command.spec.ts
```
import { Buffer } from 'node:buffer';
import { SendHandle, SpawnOptions } from 'node:child_process';
import { EventEmitter } from 'node:events';
import { Readable, Writable } from 'node:stream';

import { subscribeSpyTo } from '@hirez_io/observer-spy';
import Rx from 'rxjs';
import { beforeEach, describe, expect, it, Mock, vi } from 'vitest';

import {
    ChildProcess,
    CloseEvent,
    Command,
    CommandInfo,
    KillProcess,
    SpawnCommand,
} from './command.js';

interface CommandValues {
    error: unknown;
    close: CloseEvent;
    timer: unknown[];
}

let process: ChildProcess;
let sendMessage: Mock;
let spawn: Mock<SpawnCommand>;
let killProcess: KillProcess;

const IPC_FD = 3;

beforeEach(() => {
    sendMessage = vi.fn();
    process = new (class extends EventEmitter {
        readonly pid = 1;
        send = sendMessage;
        readonly stdout = new Readable({
            read() {
                // do nothing
            },
        });
        readonly stderr = new Readable({
            read() {
                // do nothing
            },
        });
        readonly stdin = new Writable({
            write() {
                // do nothing
            },
        });
    })();
    spawn = vi.fn().mockReturnValue(process);
    killProcess = vi.fn();
});

const createCommand = (overrides?: Partial<CommandInfo>, spawnOpts: SpawnOptions = {}) => {
    const command = new Command(
        { index: 0, name: '', command: 'echo foo', ...overrides },
        spawnOpts,
        spawn,
        killProcess,
    );

    let error: unknown;
    let close: CloseEvent;
    const timer = subscribeSpyTo(command.timer);
    const finished = subscribeSpyTo(
        new Rx.Observable((observer) => {
            // First event in both subjects means command has finished
            command.error.subscribe({
                next: (value) => {
                    error = value;
                    observer.complete();
                },
            });
            command.close.subscribe({
                next: (value) => {
                    close = value;
                    observer.complete();
                },
            });
        }),
    );
    const values = async (): Promise<CommandValues> => {
        await finished.onComplete();
        return { error, close, timer: timer.getValues() };
    };

    return { command, values };
};

it('has stopped state by default', () => {
    const { command } = createCommand();
    expect(command.state).toBe('stopped');
});

describe('#start()', () => {
    it('spawns process with given command and options', () => {
        const { command } = createCommand({}, { detached: true });
        command.start();

        expect(spawn).toHaveBeenCalledExactlyOnceWith(command.command, { detached: true });
    });

    it('sets stdin, process and PID', () => {
        const { command } = createCommand();
        command.start();

        expect(command.process).toBe(process);
        expect(command.pid).toBe(process.pid);
        expect(command.stdin).toBe(process.stdin);
    });

    it('handles process with no stdin', () => {
        process.stdin = null;
        const { command } = createCommand();
        command.start();

        expect(command.stdin).toBe(undefined);
    });

    it('changes state to started', () => {
        const { command } = createCommand();
        const spy = subscribeSpyTo(command.stateChange);
        command.start();
        expect(command.state).toBe('started');
        expect(spy.getFirstValue()).toBe('started');
    });

    describe('on errors', () => {
        it('changes state to errored', () => {
            const { command } = createCommand();
            command.start();

            const spy = subscribeSpyTo(command.stateChange);
            process.emit('error', 'foo');
            expect(command.state).toBe('errored');
            expect(spy.getFirstValue()).toBe('errored');
        });

        it('shares to the error stream', async () => {
            const { command, values } = createCommand();
            command.start();
            process.emit('error', 'foo');
            const { error } = await values();

            expect(error).toBe('foo');
            expect(command.process).toBeUndefined();
        });

        it('shares start and error timing events to the timing stream', async () => {
            const { command, values } = createCommand();
            const startDate = new Date();
            const endDate = new Date(startDate.getTime() + 1000);
            vi.spyOn(Date, 'now')
                .mockReturnValueOnce(startDate.getTime())
                .mockReturnValueOnce(endDate.getTime());
            command.start();
            process.emit('error', 0, null);
            const { timer } = await values();

            expect(timer[0]).toEqual({ startDate, endDate: undefined });
            expect(timer[1]).toEqual({ startDate, endDate });
        });
    });

    describe('on close', () => {
        it('changes state to exited', () => {
            const { command } = createCommand();
            command.start();

            const spy = subscribeSpyTo(command.stateChange);
            process.emit('close', 0, null);
            expect(command.state).toBe('exited');
            expect(spy.getFirstValue()).toBe('exited');
        });

        it('does not change state if there was an error', () => {
            const { command } = createCommand();
            command.start();
            process.emit('error', 'foo');

            const spy = subscribeSpyTo(command.stateChange);
            process.emit('close', 0, null);
            expect(command.state).toBe('errored');
            expect(spy.getValuesLength()).toBe(0);
        });

        it('shares start and close timing events to the timing stream', async () => {
            const { command, values } = createCommand();
            const startDate = new Date();
            const endDate = new Date(startDate.getTime() + 1000);
            vi.spyOn(Date, 'now')
                .mockReturnValueOnce(startDate.getTime())
                .mockReturnValueOnce(endDate.getTime());
            command.start();
            process.emit('close', 0, null);
            const { timer } = await values();

            expect(timer[0]).toEqual({ startDate, endDate: undefined });
            expect(timer[1]).toEqual({ startDate, endDate });
        });

        it('shares to the close stream with exit code', async () => {
            const { command, values } = createCommand();
            command.start();
            process.emit('close', 0, null);
            const { close } = await values();

            expect(close).toMatchObject({ exitCode: 0, killed: false });
            expect(command.process).toBeUndefined();
        });

        it('shares to the close stream with signal', async () => {
            const { command, values } = createCommand();
            command.start();
            process.emit('close', null, 'SIGKILL');
            const { close } = await values();

            expect(close).toMatchObject({ exitCode: 'SIGKILL', killed: false });
        });

        it('shares to the close stream with timing information', async () => {
            const { command, values } = createCommand();
            const startDate = new Date();
            const endDate = new Date(startDate.getTime() + 1000);
            vi.spyOn(Date, 'now')
                .mockReturnValueOnce(startDate.getTime())
                .mockReturnValueOnce(endDate.getTime());
            vi.spyOn(globalThis.process, 'hrtime')
                .mockReturnValueOnce([0, 0])
                .mockReturnValueOnce([1, 1e8]);
            command.start();
            process.emit('close', null, 'SIGKILL');
            const { close } = await values();

            expect(close.timings).toStrictEqual({
                startDate,
                endDate,
                durationSeconds: 1.1,
            });
        });

        it('shares to the close stream with command info', async () => {
            const commandInfo = {
                command: 'cmd',
                name: 'name',
                prefixColor: 'green',
                env: { VAR: 'yes' },
            };
            const { command, values } = createCommand(commandInfo);
            command.start();
            process.emit('close', 0, null);
            const { close } = await values();

            expect(close.command).toEqual(expect.objectContaining(commandInfo));
            expect(close.killed).toBe(false);
        });
    });

    it('shares stdout to the stdout stream', async () => {
        const { command } = createCommand();
        const stdout = Rx.firstValueFrom(command.stdout);
        command.start();
        process.stdout?.emit('data', Buffer.from('hello'));

        expect((await stdout).toString()).toBe('hello');
    });

    it('shares stderr to the stdout stream', async () => {
        const { command } = createCommand();
        const stderr = Rx.firstValueFrom(command.stderr);
        command.start();
        process.stderr?.emit('data', Buffer.from('dang'));

        expect((await stderr).toString()).toBe('dang');
    });

    describe('on incoming messages', () => {
        it('does not share to the incoming messages stream, if IPC is disabled', () => {
            const { command } = createCommand();
            const spy = subscribeSpyTo(command.messages.incoming);
            command.start();

            process.emit('message', {});
            expect(spy.getValuesLength()).toBe(0);
        });

        it('shares to the incoming messages stream, if IPC is enabled', () => {
            const { command } = createCommand({ ipc: IPC_FD });
            const spy = subscribeSpyTo(command.messages.incoming);
            command.start();

            const message1 = {};
            process.emit('message', message1, undefined);

            const message2 = {};
            const handle = {} as SendHandle;
            process.emit('message', message2, handle);

            expect(spy.getValuesLength()).toBe(2);
            expect(spy.getValueAt(0)).toEqual({ message: message1, handle: undefined });
            expect(spy.getValueAt(1)).toEqual({ message: message2, handle });
        });
    });

    describe('on outgoing messages', () => {
        it('calls onSent with an error if the process does not have IPC enabled', () => {
            const { command } = createCommand({ ipc: IPC_FD });
            command.start();

            Object.assign(process, {
                // The TS types don't assume `send` can be undefined,
                // despite the Node docs saying so
                send: undefined,
            });

            const onSent = vi.fn();
            command.messages.outgoing.next({ message: {}, onSent });
            expect(onSent).toHaveBeenCalledWith(expect.any(Error));
        });

        it('sends the message to the process', () => {
            const { command } = createCommand({ ipc: IPC_FD });
            command.start();

            const message1 = {};
            command.messages.outgoing.next({ message: message1, onSent() {} });

            const message2 = {};
            const handle = {} as SendHandle;
            command.messages.outgoing.next({ message: message2, handle, onSent() {} });

            const message3 = {};
            const options = {};
            command.messages.outgoing.next({ message: message3, options, onSent() {} });

            expect(process.send).toHaveBeenCalledTimes(3);
            expect(process.send).toHaveBeenNthCalledWith(
                1,
                message1,
                undefined,
                undefined,
                expect.any(Function),
            );
            expect(process.send).toHaveBeenNthCalledWith(
                2,
                message2,
                handle,
                undefined,
                expect.any(Function),
            );
            expect(process.send).toHaveBeenNthCalledWith(
                3,
                message3,
                undefined,
                options,
                expect.any(Function),
            );
        });

        it('sends the message to the process, if it starts late', () => {
            const { command } = createCommand({ ipc: IPC_FD });
            command.messages.outgoing.next({ message: {}, onSent() {} });
            expect(process.send).not.toHaveBeenCalled();

            command.start();
            expect(process.send).toHaveBeenCalled();
        });

        it('calls onSent with the result of sending the message', () => {
            const { command } = createCommand({ ipc: IPC_FD });
            command.start();

            const onSent = vi.fn();
            command.messages.outgoing.next({ message: {}, onSent });
            expect(onSent).not.toHaveBeenCalled();

            sendMessage.mock.calls[0][3]();
            expect(onSent).toHaveBeenCalledWith(undefined);

            const error = new Error('test');
            sendMessage.mock.calls[0][3](error);
            expect(onSent).toHaveBeenCalledWith(error);
        });
    });
});

describe('#send()', () => {
    it('throws if IPC is not set up', () => {
        const { command } = createCommand();
        const fn = () => command.send({});
        expect(fn).toThrow();
    });

    it('pushes the message on the outgoing messages stream', () => {
        const { command } = createCommand({ ipc: IPC_FD });
        const spy = subscribeSpyTo(command.messages.outgoing);

        const message1 = { foo: true };
        command.send(message1);

        const message2 = { bar: 123 };
        const handle = {} as SendHandle;
        command.send(message2, handle);

        const message3 = { baz: 'yes' };
        const options = {};
        command.send(message3, undefined, options);

        expect(spy.getValuesLength()).toBe(3);
        expect(spy.getValueAt(0)).toMatchObject({
            message: message1,
            handle: undefined,
            options: undefined,
        });
        expect(spy.getValueAt(1)).toMatchObject({ message: message2, handle, options: undefined });
        expect(spy.getValueAt(2)).toMatchObject({ message: message3, handle: undefined, options });
    });

    it('resolves when onSent callback is called with no arguments', async () => {
        const { command } = createCommand({ ipc: IPC_FD });
        const spy = subscribeSpyTo(command.messages.outgoing);
        const promise = command.send({});
        spy.getFirstValue().onSent();
        await expect(promise).resolves.toBeUndefined();
    });

    it('rejects when onSent callback is called with an argument', async () => {
        const { command } = createCommand({ ipc: IPC_FD });
        const spy = subscribeSpyTo(command.messages.outgoing);
        const promise = command.send({});
        spy.getFirstValue().onSent('foo');
        await expect(promise).rejects.toBe('foo');
    });
});

describe('#kill()', () => {
    let createdCommand: { command: Command; values: () => Promise<CommandValues> };
    beforeEach(() => {
        createdCommand = createCommand();
    });

    it('kills process', () => {
        createdCommand.command.start();
        createdCommand.command.kill();

        expect(killProcess).toHaveBeenCalledExactlyOnceWith(createdCommand.command.pid, undefined);
    });

    it('kills process with some signal', () => {
        createdCommand.command.start();
        createdCommand.command.kill('SIGKILL');

        expect(killProcess).toHaveBeenCalledExactlyOnceWith(createdCommand.command.pid, 'SIGKILL');
    });

    it('does not try to kill inexistent process', () => {
        createdCommand.command.start();
        process.emit('error');
        createdCommand.command.kill();

        expect(killProcess).not.toHaveBeenCalled();
    });

    it('marks the command as killed', async () => {
        createdCommand.command.start();
        createdCommand.command.kill();
        process.emit('close', 1, null);
        const { close } = await createdCommand.values();

        expect(close).toMatchObject({ exitCode: 1, killed: true });
    });
});

describe('.canKill()', () => {
    it('returns whether command has both PID and process', () => {
        const { command } = createCommand();
        expect(Command.canKill(command)).toBe(false);

        command.pid = 1;
        expect(Command.canKill(command)).toBe(false);

        command.process = process;
        expect(Command.canKill(command)).toBe(true);
    });
});

```

## File: lib\command.ts
```
import { Buffer } from 'node:buffer';
import {
    ChildProcess as BaseChildProcess,
    MessageOptions,
    SendHandle,
    SpawnOptions,
} from 'node:child_process';
import process from 'node:process';
import { EventEmitter, Writable } from 'node:stream';

import Rx from 'rxjs';

/**
 * Identifier for a command; if string, it's the command's name, if number, it's the index.
 */
export type CommandIdentifier = string | number;

export interface CommandInfo {
    /**
     * Command's name.
     */
    name: string;

    /**
     * Which command line the command has.
     */
    command: string;

    /**
     * Which environment variables should the spawned process have.
     */
    env?: Record<string, unknown>;

    /**
     * The current working directory of the process when spawned.
     */
    cwd?: string;

    /**
     * Color to use on prefix of the command.
     */
    prefixColor?: string;

    /**
     * Whether sending of messages to/from this command (also known as "inter-process communication")
     * should be enabled, and using which file descriptor number.
     *
     * If set, must be > 2.
     */
    ipc?: number;

    /**
     * Output command in raw format.
     */
    raw?: boolean;
}

export interface CloseEvent {
    command: CommandInfo;

    /**
     * The command's index among all commands ran.
     */
    index: number;

    /**
     * Whether the command exited because it was killed.
     */
    killed: boolean;

    /**
     * The exit code or signal for the command.
     */
    exitCode: string | number;

    timings: {
        startDate: Date;
        endDate: Date;
        durationSeconds: number;
    };
}

export interface TimerEvent {
    startDate: Date;
    endDate?: Date;
}

export interface MessageEvent {
    message: object;
    handle?: SendHandle;
}

interface OutgoingMessageEvent extends MessageEvent {
    options?: MessageOptions;
    onSent: (error?: unknown) => void;
}

/**
 * Subtype of NodeJS's child_process including only what's actually needed for a command to work.
 */
export type ChildProcess = EventEmitter &
    Pick<BaseChildProcess, 'pid' | 'stdin' | 'stdout' | 'stderr' | 'send'>;

/**
 * Interface for a function that must kill the process with `pid`, optionally sending `signal` to it.
 */
export type KillProcess = (pid: number, signal?: string) => void;

/**
 * Interface for a function that spawns a command and returns its child process instance.
 */
export type SpawnCommand = (command: string, options: SpawnOptions) => ChildProcess;

/**
 * The state of a command.
 *
 * - `stopped`: command was never started
 * - `started`: command is currently running
 * - `errored`: command failed spawning
 * - `exited`: command is not running anymore, e.g. it received a close event
 */
type CommandState = 'stopped' | 'started' | 'errored' | 'exited';

export class Command implements CommandInfo {
    private readonly killProcess: KillProcess;
    private readonly spawn: SpawnCommand;
    private readonly spawnOpts: SpawnOptions;
    readonly index: number;

    /** @inheritdoc */
    readonly name: string;

    /** @inheritdoc */
    readonly command: string;

    /** @inheritdoc */
    readonly prefixColor?: string;

    /** @inheritdoc */
    readonly env: Record<string, unknown>;

    /** @inheritdoc */
    readonly cwd?: string;

    /** @inheritdoc */
    readonly ipc?: number;

    readonly close = new Rx.Subject<CloseEvent>();
    readonly error = new Rx.Subject<unknown>();
    readonly stdout = new Rx.Subject<Buffer>();
    readonly stderr = new Rx.Subject<Buffer>();
    readonly timer = new Rx.Subject<TimerEvent>();

    /**
     * A stream of changes to the `#state` property.
     *
     * Note that the command never goes back to the `stopped` state, therefore it's not a value
     * that's emitted by this stream.
     */
    readonly stateChange = new Rx.Subject<Exclude<CommandState, 'stopped'>>();
    readonly messages = {
        incoming: new Rx.Subject<MessageEvent>(),
        outgoing: new Rx.ReplaySubject<OutgoingMessageEvent>(),
    };

    process?: ChildProcess;

    // TODO: Should exit/error/stdio subscriptions be added here?
    private subscriptions: readonly Rx.Subscription[] = [];
    stdin?: Writable;
    pid?: number;
    killed = false;
    exited = false;

    state: CommandState = 'stopped';

    constructor(
        { index, name, command, prefixColor, env, cwd, ipc }: CommandInfo & { index: number },
        spawnOpts: SpawnOptions,
        spawn: SpawnCommand,
        killProcess: KillProcess,
    ) {
        this.index = index;
        this.name = name;
        this.command = command;
        this.prefixColor = prefixColor;
        this.env = env || {};
        this.cwd = cwd;
        this.ipc = ipc;
        this.killProcess = killProcess;
        this.spawn = spawn;
        this.spawnOpts = spawnOpts;
    }

    /**
     * Starts this command, piping output, error and close events onto the corresponding observables.
     */
    start() {
        const child = this.spawn(this.command, this.spawnOpts);
        this.changeState('started');
        this.process = child;
        this.pid = child.pid;
        const startDate = new Date(Date.now());
        const highResStartTime = process.hrtime();
        this.timer.next({ startDate });

        this.subscriptions = [...this.maybeSetupIPC(child)];
        Rx.fromEvent(child, 'error').subscribe((event) => {
            this.cleanUp();
            const endDate = new Date(Date.now());
            this.timer.next({ startDate, endDate });
            this.error.next(event);
            this.changeState('errored');
        });
        Rx.fromEvent(child, 'close')
            .pipe(Rx.map((event) => event as [number | null, NodeJS.Signals | null]))
            .subscribe(([exitCode, signal]) => {
                this.cleanUp();

                // Don't override error event
                if (this.state !== 'errored') {
                    this.changeState('exited');
                }

                const endDate = new Date(Date.now());
                this.timer.next({ startDate, endDate });
                const [durationSeconds, durationNanoSeconds] = process.hrtime(highResStartTime);
                this.close.next({
                    command: this,
                    index: this.index,
                    exitCode: exitCode ?? String(signal),
                    killed: this.killed,
                    timings: {
                        startDate,
                        endDate,
                        durationSeconds: durationSeconds + durationNanoSeconds / 1e9,
                    },
                });
            });
        if (child.stdout) {
            pipeTo(
                Rx.fromEvent(child.stdout, 'data').pipe(Rx.map((event) => event as Buffer)),
                this.stdout,
            );
        }
        if (child.stderr) {
            pipeTo(
                Rx.fromEvent(child.stderr, 'data').pipe(Rx.map((event) => event as Buffer)),
                this.stderr,
            );
        }
        this.stdin = child.stdin || undefined;
    }

    private changeState(state: Exclude<CommandState, 'stopped'>) {
        this.state = state;
        this.stateChange.next(state);
    }

    private maybeSetupIPC(child: ChildProcess) {
        if (!this.ipc) {
            return [];
        }

        return [
            pipeTo(
                Rx.fromEvent(child, 'message').pipe(
                    Rx.map((event) => {
                        const [message, handle] = event as [object, SendHandle | undefined];
                        return { message, handle };
                    }),
                ),
                this.messages.incoming,
            ),
            this.messages.outgoing.subscribe((message) => {
                if (!child.send) {
                    return message.onSent(new Error('Command does not have an IPC channel'));
                }

                child.send(message.message, message.handle, message.options, (error) => {
                    message.onSent(error);
                });
            }),
        ];
    }

    /**
     * Sends a message to the underlying process once it starts.
     *
     * @throws  If the command doesn't have an IPC channel enabled
     * @returns Promise that resolves when the message is sent,
     *          or rejects if it fails to deliver the message.
     */
    send(message: object, handle?: SendHandle, options?: MessageOptions): Promise<void> {
        if (this.ipc == null) {
            throw new Error('Command IPC is disabled');
        }
        return new Promise((resolve, reject) => {
            this.messages.outgoing.next({
                message,
                handle,
                options,
                onSent(error) {
                    if (error) {
                        reject(error);
                    } else {
                        resolve();
                    }
                },
            });
        });
    }

    /**
     * Kills this command, optionally specifying a signal to send to it.
     */
    kill(code?: string) {
        if (Command.canKill(this)) {
            this.killed = true;
            this.killProcess(this.pid, code);
        }
    }

    private cleanUp() {
        this.subscriptions?.forEach((sub) => sub.unsubscribe());
        this.messages.outgoing = new Rx.ReplaySubject();
        this.process = undefined;
    }

    /**
     * Detects whether a command can be killed.
     *
     * Also works as a type guard on the input `command`.
     */
    static canKill(command: Command): command is Command & { pid: number; process: ChildProcess } {
        return !!command.pid && !!command.process;
    }
}

/**
 * Pipes all events emitted by `stream` into `subject`.
 */
function pipeTo<T>(stream: Rx.Observable<T>, subject: Rx.Subject<T>) {
    return stream.subscribe((event) => subject.next(event));
}

```

## File: lib\completion-listener.spec.ts
```
import { getEventListeners } from 'node:events';

import { TestScheduler } from 'rxjs/testing';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createFakeCloseEvent, FakeCommand } from './__fixtures__/fake-command.js';
import { CloseEvent } from './command.js';
import { CompletionListener, SuccessCondition } from './completion-listener.js';

let commands: FakeCommand[];
let scheduler: TestScheduler;

beforeEach(() => {
    commands = [
        new FakeCommand('foo', 'echo', 0),
        new FakeCommand('bar', 'echo', 1),
        new FakeCommand('baz', 'echo', 2),
    ];
    scheduler = new TestScheduler(() => true);
});

const createController = (successCondition?: SuccessCondition) =>
    new CompletionListener({
        successCondition,
        scheduler,
    });

const emitFakeCloseEvent = (command: FakeCommand, event?: Partial<CloseEvent>) => {
    const fakeEvent = createFakeCloseEvent({ ...event, command, index: command.index });
    command.state = 'exited';
    command.close.next(fakeEvent);
    return fakeEvent;
};

const flushPromises = () => new Promise((resolve) => setTimeout(resolve, 0));

describe('listen', () => {
    it('resolves when there are no commands', async () => {
        const result = createController().listen([]);
        await expect(result).resolves.toHaveLength(0);
    });

    it('completes only when commands emit a close event, returns close event', async () => {
        const abortCtrl = new AbortController();
        const result = createController('all').listen(commands, abortCtrl.signal);

        commands[0].state = 'started';
        abortCtrl.abort();

        const event = emitFakeCloseEvent(commands[0]);
        scheduler.flush();

        await expect(result).resolves.toHaveLength(1);
        await expect(result).resolves.toEqual([event]);
    });

    it('completes when abort signal is received and command is stopped, returns nothing', async () => {
        const abortCtrl = new AbortController();
        // Use success condition = first to test index access when there are no close events
        const result = createController('first').listen([new FakeCommand()], abortCtrl.signal);

        abortCtrl.abort();
        scheduler.flush();

        await expect(result).resolves.toHaveLength(0);
    });

    it('does not leak memory when listening for abort signals', () => {
        const abortCtrl = new AbortController();
        createController().listen(
            Array.from({ length: 10 }, () => new FakeCommand()),
            abortCtrl.signal,
        );
        expect(getEventListeners(abortCtrl.signal, 'abort')).toHaveLength(1);
    });

    it('check for success once all commands have emitted at least a single close event', async () => {
        const finallyCallback = vi.fn();
        const result = createController().listen(commands).finally(finallyCallback);

        // Emitting multiple close events to mimic calling command `kill/start` APIs.
        emitFakeCloseEvent(commands[0]);
        emitFakeCloseEvent(commands[0]);
        emitFakeCloseEvent(commands[0]);

        scheduler.flush();
        // A broken implementation will have called finallyCallback only after flushing promises
        await flushPromises();
        expect(finallyCallback).not.toHaveBeenCalled();

        emitFakeCloseEvent(commands[1]);
        emitFakeCloseEvent(commands[2]);

        scheduler.flush();

        await expect(result).resolves.toEqual(expect.anything());
        expect(finallyCallback).toHaveBeenCalled();
    });

    it('takes last event emitted from each command', async () => {
        const result = createController().listen(commands);

        emitFakeCloseEvent(commands[0], { exitCode: 0 });
        emitFakeCloseEvent(commands[0], { exitCode: 1 });
        emitFakeCloseEvent(commands[1], { exitCode: 0 });
        emitFakeCloseEvent(commands[2], { exitCode: 0 });

        scheduler.flush();

        await expect(result).rejects.toEqual(expect.anything());
    });

    it('waits for manually restarted events to close', async () => {
        const finallyCallback = vi.fn();
        const result = createController().listen(commands).finally(finallyCallback);

        emitFakeCloseEvent(commands[0]);
        commands[0].state = 'started';
        emitFakeCloseEvent(commands[1]);
        emitFakeCloseEvent(commands[2]);

        scheduler.flush();
        // A broken implementation will have called finallyCallback only after flushing promises
        await flushPromises();
        expect(finallyCallback).not.toHaveBeenCalled();

        commands[0].state = 'exited';
        emitFakeCloseEvent(commands[0]);
        scheduler.flush();

        await expect(result).resolves.toEqual(expect.anything());
        expect(finallyCallback).toHaveBeenCalled();
    });
});

describe('detect commands exit conditions', () => {
    describe('with default success condition set', () => {
        it('succeeds if all processes exited with code 0', () => {
            const result = createController().listen(commands);

            commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
            commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));
            commands[2].close.next(createFakeCloseEvent({ exitCode: 0 }));

            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });

        it('fails if one of the processes exited with non-0 code', () => {
            const result = createController().listen(commands);

            commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
            commands[1].close.next(createFakeCloseEvent({ exitCode: 1 }));
            commands[2].close.next(createFakeCloseEvent({ exitCode: 0 }));

            scheduler.flush();

            return expect(result).rejects.toEqual(expect.anything());
        });
    });

    describe('with success condition set to first', () => {
        it('succeeds if first process to exit has code 0', () => {
            const result = createController('first').listen(commands);

            commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));
            commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
            commands[2].close.next(createFakeCloseEvent({ exitCode: 1 }));

            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });

        it('fails if first process to exit has non-0 code', () => {
            const result = createController('first').listen(commands);

            commands[1].close.next(createFakeCloseEvent({ exitCode: 1 }));
            commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
            commands[2].close.next(createFakeCloseEvent({ exitCode: 0 }));

            scheduler.flush();

            return expect(result).rejects.toEqual(expect.anything());
        });
    });

    describe('with success condition set to last', () => {
        it('succeeds if last process to exit has code 0', () => {
            const result = createController('last').listen(commands);

            commands[1].close.next(createFakeCloseEvent({ exitCode: 1 }));
            commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
            commands[2].close.next(createFakeCloseEvent({ exitCode: 0 }));

            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });

        it('fails if last process to exit has non-0 code', () => {
            const result = createController('last').listen(commands);

            commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));
            commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
            commands[2].close.next(createFakeCloseEvent({ exitCode: 1 }));

            scheduler.flush();

            return expect(result).rejects.toEqual(expect.anything());
        });
    });

    describe.each([
        // Use the middle command for both cases to make it more difficult to make a mess up
        // in the implementation cause false passes.
        ['command-bar' as const, 'bar'],
        ['command-1' as const, 1],
    ])('with success condition set to %s', (condition, nameOrIndex) => {
        it(`succeeds if command ${nameOrIndex} exits with code 0`, () => {
            const result = createController(condition).listen(commands);

            emitFakeCloseEvent(commands[0], { exitCode: 1 });
            emitFakeCloseEvent(commands[1], { exitCode: 0 });
            emitFakeCloseEvent(commands[2], { exitCode: 1 });

            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });

        it(`succeeds if all commands ${nameOrIndex} exit with code 0`, () => {
            commands = [commands[0], commands[1], commands[1]];
            const result = createController(condition).listen(commands);

            emitFakeCloseEvent(commands[0], { exitCode: 1 });
            emitFakeCloseEvent(commands[1], { exitCode: 0 });
            emitFakeCloseEvent(commands[2], { exitCode: 0 });

            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });

        it(`fails if command ${nameOrIndex} exits with non-0 code`, () => {
            const result = createController(condition).listen(commands);

            emitFakeCloseEvent(commands[0], { exitCode: 0 });
            emitFakeCloseEvent(commands[1], { exitCode: 1 });
            emitFakeCloseEvent(commands[2], { exitCode: 0 });

            scheduler.flush();

            return expect(result).rejects.toEqual(expect.anything());
        });

        it(`fails if some commands ${nameOrIndex} exit with non-0 code`, () => {
            const result = createController(condition).listen(commands);

            emitFakeCloseEvent(commands[0], { exitCode: 1 });
            emitFakeCloseEvent(commands[1], { exitCode: 0 });
            emitFakeCloseEvent(commands[2], { exitCode: 1 });

            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });

        it(`fails if command ${nameOrIndex} doesn't exist`, () => {
            const result = createController(condition).listen([commands[0]]);

            emitFakeCloseEvent(commands[0], { exitCode: 0 });
            scheduler.flush();

            return expect(result).rejects.toEqual(expect.anything());
        });
    });

    describe.each([
        // Use the middle command for both cases to make it more difficult to make a mess up
        // in the implementation cause false passes.
        ['!command-bar' as const, 'bar'],
        ['!command-1' as const, 1],
    ])('with success condition set to %s', (condition, nameOrIndex) => {
        it(`succeeds if all commands but ${nameOrIndex} exit with code 0`, () => {
            const result = createController(condition).listen(commands);

            emitFakeCloseEvent(commands[0], { exitCode: 0 });
            emitFakeCloseEvent(commands[1], { exitCode: 1 });
            emitFakeCloseEvent(commands[2], { exitCode: 0 });

            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });

        it(`fails if any commands but ${nameOrIndex} exit with non-0 code`, () => {
            const result = createController(condition).listen(commands);

            emitFakeCloseEvent(commands[0], { exitCode: 1 });
            emitFakeCloseEvent(commands[1], { exitCode: 1 });
            emitFakeCloseEvent(commands[2], { exitCode: 0 });

            scheduler.flush();

            return expect(result).rejects.toEqual(expect.anything());
        });

        it(`succeeds if command ${nameOrIndex} doesn't exist`, () => {
            const result = createController(condition).listen([commands[0]]);

            emitFakeCloseEvent(commands[0], { exitCode: 0 });
            scheduler.flush();

            return expect(result).resolves.toEqual(expect.anything());
        });
    });
});

```

## File: lib\completion-listener.ts
```
import Rx from 'rxjs';
import { delay, filter, map, share, switchMap, take } from 'rxjs/operators';

import { CloseEvent, Command } from './command.js';

/**
 * Defines which command(s) in a list must exit successfully (with an exit code of `0`):
 *
 * - `first`: only the first specified command;
 * - `last`: only the last specified command;
 * - `all`: all commands.
 * - `command-{name|index}`: only the commands with the specified names or index.
 * - `!command-{name|index}`: all commands but the ones with the specified names or index.
 */
export type SuccessCondition =
    | 'first'
    | 'last'
    | 'all'
    | `command-${string | number}`
    | `!command-${string | number}`;

/**
 * Provides logic to determine whether lists of commands ran successfully.
 */
export class CompletionListener {
    private readonly successCondition: SuccessCondition;
    private readonly scheduler?: Rx.SchedulerLike;

    constructor({
        successCondition = 'all',
        scheduler,
    }: {
        /**
         * How this instance will define that a list of commands ran successfully.
         * Defaults to `all`.
         *
         * @see {SuccessCondition}
         */
        successCondition?: SuccessCondition;

        /**
         * For testing only.
         */
        scheduler?: Rx.SchedulerLike;
    }) {
        this.successCondition = successCondition;
        this.scheduler = scheduler;
    }

    private isSuccess(events: CloseEvent[]) {
        if (!events.length) {
            // When every command was aborted, consider a success.
            return true;
        }

        if (this.successCondition === 'first') {
            return events[0].exitCode === 0;
        } else if (this.successCondition === 'last') {
            return events[events.length - 1].exitCode === 0;
        }

        const commandSyntaxMatch = this.successCondition.match(/^!?command-(.+)$/);
        if (commandSyntaxMatch == null) {
            // If not a `command-` syntax, then it's an 'all' condition or it's treated as such.
            return events.every(({ exitCode }) => exitCode === 0);
        }

        // Check `command-` syntax condition.
        // Note that a command's `name` is not necessarily unique,
        // in which case all of them must meet the success condition.
        const nameOrIndex = commandSyntaxMatch[1];
        const targetCommandsEvents = events.filter(
            ({ command, index }) => command.name === nameOrIndex || index === Number(nameOrIndex),
        );
        if (this.successCondition.startsWith('!')) {
            // All commands except the specified ones must exit successfully
            return events.every(
                (event) => targetCommandsEvents.includes(event) || event.exitCode === 0,
            );
        }
        // Only the specified commands must exit successfully
        return (
            targetCommandsEvents.length > 0 &&
            targetCommandsEvents.every((event) => event.exitCode === 0)
        );
    }

    /**
     * Given a list of commands, wait for all of them to exit and then evaluate their exit codes.
     *
     * @returns A Promise that resolves if the success condition is met, or rejects otherwise.
     *          In either case, the value is a list of close events for commands that spawned.
     *          Commands that didn't spawn are filtered out.
     */
    listen(commands: Command[], abortSignal?: AbortSignal): Promise<CloseEvent[]> {
        if (!commands.length) {
            return Promise.resolve([]);
        }

        const abort =
            abortSignal &&
            Rx.fromEvent(abortSignal, 'abort', { once: true }).pipe(
                // The abort signal must happen before commands are killed, otherwise new commands
                // might spawn. Because of this, it's not be possible to capture the close events
                // without an immediate delay
                delay(0, this.scheduler),
                map(() => undefined),
                // #502 - node might warn of too many active listeners on this object if it isn't shared,
                // as each command subscribes to abort event over and over
                share(),
            );

        const closeStreams = commands.map((command) =>
            abort
                ? // Commands that have been started must close.
                  Rx.race(command.close, abort.pipe(filter(() => command.state === 'stopped')))
                : command.close,
        );

        return Rx.lastValueFrom(
            Rx.combineLatest(closeStreams).pipe(
                filter(() => commands.every((command) => command.state !== 'started')),
                map((events) =>
                    events
                        // Filter out aborts, since they cannot be sorted and are considered success condition anyways
                        .filter((event): event is CloseEvent => event != null)
                        // Sort according to exit time
                        .sort(
                            (first, second) =>
                                first.timings.endDate.getTime() - second.timings.endDate.getTime(),
                        ),
                ),
                switchMap((events) =>
                    this.isSuccess(events)
                        ? this.emitWithScheduler(Rx.of(events))
                        : this.emitWithScheduler(Rx.throwError(() => events)),
                ),
                take(1),
            ),
        );
    }

    private emitWithScheduler<O>(input: Rx.Observable<O>): Rx.Observable<O> {
        return this.scheduler ? input.pipe(Rx.observeOn(this.scheduler)) : input;
    }
}

```

## File: lib\concurrently.spec.ts
```
import type { CpuInfo } from 'node:os';
import os from 'node:os';
import { Writable } from 'node:stream';

import { beforeEach, expect, it, Mock, MockedObject, vi } from 'vitest';

import { createMockInstance } from './__fixtures__/create-mock-instance.js';
import { createFakeProcess, FakeCommand } from './__fixtures__/fake-command.js';
import { ChildProcess, KillProcess, SpawnCommand } from './command.js';
import { concurrently, ConcurrentlyCommandInput, ConcurrentlyOptions } from './concurrently.js';
import { FlowController } from './flow-control/flow-controller.js';
import { Logger } from './logger.js';

let spawn: SpawnCommand;
let kill: KillProcess;
let onFinishHooks: Mock[];
let controllers: MockedObject<FlowController>[];
let processes: ChildProcess[];
const create = (commands: ConcurrentlyCommandInput[], options: Partial<ConcurrentlyOptions> = {}) =>
    concurrently(commands, Object.assign(options, { controllers, spawn, kill }));

beforeEach(() => {
    vi.resetAllMocks();

    processes = [];
    spawn = vi.fn(() => {
        const process = createFakeProcess(processes.length);
        processes.push(process);
        return process;
    });
    kill = vi.fn();

    onFinishHooks = [vi.fn(), vi.fn()];
    controllers = [
        { handle: vi.fn((commands) => ({ commands, onFinish: onFinishHooks[0] })) },
        { handle: vi.fn((commands) => ({ commands, onFinish: onFinishHooks[1] })) },
    ];
});

it('fails if commands is not an array', () => {
    const bomb = () => create('foo' as never);
    expect(bomb).toThrow();
});

it('fails if no commands were provided', () => {
    const bomb = () => create([]);
    expect(bomb).toThrow();
});

it('spawns all commands', () => {
    create(['echo', 'kill']);
    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith('echo', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('kill', expect.objectContaining({}));
});

it('log output is passed to output stream if logger is specified in options', () => {
    const logger = new Logger({ hide: [] });
    const outputStream = createMockInstance(Writable);
    create(['foo'], { logger, outputStream });
    logger.log('foo', 'bar');

    expect(outputStream.write).toHaveBeenCalledTimes(2);
    expect(outputStream.write).toHaveBeenCalledWith('foo');
    expect(outputStream.write).toHaveBeenCalledWith('bar');
});

it('log output is not passed to output stream after it has errored', () => {
    const logger = new Logger({ hide: [] });
    const outputStream = new Writable();
    vi.spyOn(outputStream, 'write');

    create(['foo'], { logger, outputStream });
    outputStream.emit('error', new Error('test'));
    logger.log('foo', 'bar');

    expect(outputStream.write).not.toHaveBeenCalled();
});

it('spawns commands up to configured limit at once', () => {
    create(['foo', 'bar', 'baz', 'qux'], { maxProcesses: 2 });
    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith('foo', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('bar', expect.objectContaining({}));

    // Test out of order completion picking up new processes in-order
    processes[1].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(3);
    expect(spawn).toHaveBeenCalledWith('baz', expect.objectContaining({}));

    processes[0].emit('close', null, 'SIGINT');
    expect(spawn).toHaveBeenCalledTimes(4);
    expect(spawn).toHaveBeenCalledWith('qux', expect.objectContaining({}));

    // Shouldn't attempt to spawn anything else.
    processes[2].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(4);
});

it('spawns commands up to percent based limit at once', () => {
    // Mock architecture with 4 cores
    const cpusSpy = vi.spyOn(os, 'cpus');
    cpusSpy.mockReturnValue(
        Array.from<CpuInfo>({ length: 4 }).fill({
            model: 'Intel',
            speed: 0,
            times: { user: 0, nice: 0, sys: 0, idle: 0, irq: 0 },
        }),
    );

    create(['foo', 'bar', 'baz', 'qux'], { maxProcesses: '50%' });

    // Max parallel processes should be 2 (50% of 4 cores)
    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith('foo', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('bar', expect.objectContaining({}));

    // Close first process and expect third to be spawned
    processes[0].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(3);
    expect(spawn).toHaveBeenCalledWith('baz', expect.objectContaining({}));

    // Close second process and expect fourth to be spawned
    processes[1].emit('close', 1, null);
    expect(spawn).toHaveBeenCalledTimes(4);
    expect(spawn).toHaveBeenCalledWith('qux', expect.objectContaining({}));
});

it('does not spawn further commands on abort signal aborted', () => {
    const abortController = new AbortController();
    create(['foo', 'bar'], { maxProcesses: 1, abortSignal: abortController.signal });
    expect(spawn).toHaveBeenCalledTimes(1);

    abortController.abort();
    processes[0].emit('close', 0, null);
    expect(spawn).toHaveBeenCalledTimes(1);
});

it('runs controllers with the commands', () => {
    create(['echo', '"echo wrapped"']);

    controllers.forEach((controller) => {
        expect(controller.handle).toHaveBeenCalledWith([
            expect.objectContaining({ command: 'echo', index: 0 }),
            expect.objectContaining({ command: 'echo wrapped', index: 1 }),
        ]);
    });
});

it('runs commands with a name or prefix color', () => {
    create([{ command: 'echo', prefixColor: 'red', name: 'foo' }, 'kill']);

    controllers.forEach((controller) => {
        expect(controller.handle).toHaveBeenCalledWith([
            expect.objectContaining({ command: 'echo', index: 0, name: 'foo', prefixColor: 'red' }),
            expect.objectContaining({ command: 'kill', index: 1, name: '', prefixColor: '' }),
        ]);
    });
});

it('runs commands with a list of colors', () => {
    create(['echo', 'kill'], {
        prefixColors: ['red'],
    });

    controllers.forEach((controller) => {
        expect(controller.handle).toHaveBeenCalledWith([
            expect.objectContaining({ command: 'echo', prefixColor: 'red' }),
            expect.objectContaining({ command: 'kill', prefixColor: 'red' }),
        ]);
    });
});

it('passes commands wrapped from a controller to the next one', () => {
    const fakeCommand = new FakeCommand('banana', 'banana');
    controllers[0].handle.mockReturnValue({ commands: [fakeCommand] });

    create(['echo']);

    expect(controllers[0].handle).toHaveBeenCalledWith([
        expect.objectContaining({ command: 'echo', index: 0 }),
    ]);

    expect(controllers[1].handle).toHaveBeenCalledWith([fakeCommand]);

    expect(fakeCommand.start).toHaveBeenCalledTimes(1);
});

it('merges extra env vars into each command', () => {
    create([
        { command: 'echo', env: { foo: 'bar' } },
        { command: 'echo', env: { foo: 'baz' } },
        'kill',
    ]);

    expect(spawn).toHaveBeenCalledTimes(3);
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            env: expect.objectContaining({ foo: 'bar' }),
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            env: expect.objectContaining({ foo: 'baz' }),
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'kill',
        expect.objectContaining({
            env: expect.not.objectContaining({ foo: expect.anything() }),
        }),
    );
});

it('uses cwd from options for each command', () => {
    create(
        [
            { command: 'echo', env: { foo: 'bar' } },
            { command: 'echo', env: { foo: 'baz' } },
            'kill',
        ],
        {
            cwd: 'foobar',
        },
    );

    expect(spawn).toHaveBeenCalledTimes(3);
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            env: expect.objectContaining({ foo: 'bar' }),
            cwd: 'foobar',
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            env: expect.objectContaining({ foo: 'baz' }),
            cwd: 'foobar',
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'kill',
        expect.objectContaining({
            env: expect.not.objectContaining({ foo: expect.anything() }),
            cwd: 'foobar',
        }),
    );
});

it('uses overridden cwd option for each command if specified', () => {
    create(
        [
            { command: 'echo', env: { foo: 'bar' }, cwd: 'baz' },
            { command: 'echo', env: { foo: 'baz' } },
        ],
        {
            cwd: 'foobar',
        },
    );

    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            env: expect.objectContaining({ foo: 'bar' }),
            cwd: 'baz',
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            env: expect.objectContaining({ foo: 'baz' }),
            cwd: 'foobar',
        }),
    );
});

it('uses raw from options for each command', () => {
    create([{ command: 'echo' }, 'kill'], {
        raw: true,
    });

    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            stdio: ['inherit', 'inherit', 'inherit'],
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'kill',
        expect.objectContaining({
            stdio: ['inherit', 'inherit', 'inherit'],
        }),
    );
});

it('uses overridden raw option for each command if specified', () => {
    create([{ command: 'echo', raw: false }, { command: 'echo' }], {
        raw: true,
    });

    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            stdio: ['pipe', 'pipe', 'pipe'],
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            stdio: ['inherit', 'inherit', 'inherit'],
        }),
    );
});

it('uses hide from options for each command', () => {
    create([{ command: 'echo' }, 'kill'], {
        hide: [1],
    });

    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            stdio: ['pipe', 'pipe', 'pipe'],
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'kill',
        expect.objectContaining({
            stdio: ['pipe', 'ignore', 'ignore'],
        }),
    );
});

it('hides output for commands even if raw option is on', () => {
    create([{ command: 'echo' }, 'kill'], {
        hide: [1],
        raw: true,
    });

    expect(spawn).toHaveBeenCalledTimes(2);
    expect(spawn).toHaveBeenCalledWith(
        'echo',
        expect.objectContaining({
            stdio: ['inherit', 'inherit', 'inherit'],
        }),
    );
    expect(spawn).toHaveBeenCalledWith(
        'kill',
        expect.objectContaining({
            stdio: ['pipe', 'ignore', 'ignore'],
        }),
    );
});

it('argument placeholders are properly replaced when additional arguments are passed', () => {
    create(
        [
            { command: 'echo {1}' },
            { command: 'echo {@}' },
            { command: 'echo {*}' },
            { command: 'echo \\{@}' },
        ],
        {
            additionalArguments: ['foo', 'bar'],
        },
    );

    expect(spawn).toHaveBeenCalledTimes(4);
    expect(spawn).toHaveBeenCalledWith('echo foo', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('echo foo bar', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith("echo 'foo bar'", expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('echo {@}', expect.objectContaining({}));
});

it('argument placeholders are not replaced when additional arguments are not defined', () => {
    create([
        { command: 'echo {1}' },
        { command: 'echo {@}' },
        { command: 'echo {*}' },
        { command: 'echo \\{@}' },
    ]);

    expect(spawn).toHaveBeenCalledTimes(4);
    expect(spawn).toHaveBeenCalledWith('echo {1}', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('echo {@}', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('echo {*}', expect.objectContaining({}));
    expect(spawn).toHaveBeenCalledWith('echo {@}', expect.objectContaining({}));
});

it('runs onFinish hook after all commands run', async () => {
    const promise = create(['foo', 'bar'], { maxProcesses: 1 });
    expect(spawn).toHaveBeenCalledTimes(1);
    expect(onFinishHooks[0]).not.toHaveBeenCalled();
    expect(onFinishHooks[1]).not.toHaveBeenCalled();

    processes[0].emit('close', 0, null);
    expect(spawn).toHaveBeenCalledTimes(2);
    expect(onFinishHooks[0]).not.toHaveBeenCalled();
    expect(onFinishHooks[1]).not.toHaveBeenCalled();

    processes[1].emit('close', 0, null);
    await promise.result;

    expect(onFinishHooks[0]).toHaveBeenCalled();
    expect(onFinishHooks[1]).toHaveBeenCalled();
});

// This test should time out if broken
it('waits for onFinish hooks to complete before resolving', async () => {
    onFinishHooks[0].mockResolvedValue(undefined);
    const { result } = create(['foo', 'bar']);

    processes[0].emit('close', 0, null);
    processes[1].emit('close', 0, null);

    await expect(result).resolves.toBeDefined();
});

it('rejects if onFinish hooks reject', async () => {
    onFinishHooks[0].mockRejectedValue('error');
    const { result } = create(['foo', 'bar']);

    processes[0].emit('close', 0, null);
    processes[1].emit('close', 0, null);

    await expect(result).rejects.toBe('error');
});

```

## File: lib\concurrently.ts
```
import assert from 'node:assert';
import os from 'node:os';
import { Writable } from 'node:stream';

import { takeUntil } from 'rxjs';
import treeKill from 'tree-kill';

import {
    CloseEvent,
    Command,
    CommandIdentifier,
    CommandInfo,
    KillProcess,
    SpawnCommand,
} from './command.js';
import { CommandParser } from './command-parser/command-parser.js';
import { ExpandArguments } from './command-parser/expand-arguments.js';
import { ExpandShortcut } from './command-parser/expand-shortcut.js';
import { ExpandWildcard } from './command-parser/expand-wildcard.js';
import { StripQuotes } from './command-parser/strip-quotes.js';
import { CompletionListener, SuccessCondition } from './completion-listener.js';
import { FlowController } from './flow-control/flow-controller.js';
import { Logger } from './logger.js';
import { OutputWriter } from './output-writer.js';
import { PrefixColorSelector } from './prefix-color-selector.js';
import { getSpawnOpts, spawn } from './spawn.js';
import { castArray } from './utils.js';

const defaults: ConcurrentlyOptions = {
    spawn,
    kill: treeKill,
    raw: false,
    controllers: [],
    cwd: undefined,
};

/**
 * A command that is to be passed into `concurrently()`.
 * If value is a string, then that's the command's command line.
 * Fine grained options can be defined by using the object format.
 */
export type ConcurrentlyCommandInput = string | ({ command: string } & Partial<CommandInfo>);

export interface ConcurrentlyResult {
    /**
     * All commands created and ran by concurrently.
     */
    commands: Command[];

    /**
     * A promise that resolves when concurrently ran successfully according to the specified
     * success condition, or reject otherwise.
     *
     * Both the resolved and rejected value is a list of all the close events for commands that
     * spawned; commands that didn't spawn are filtered out.
     */
    result: Promise<CloseEvent[]>;
}

export interface ConcurrentlyOptions {
    logger?: Logger;

    /**
     * Which stream should the commands output be written to.
     */
    outputStream?: Writable;

    /**
     * Whether the output should be ordered as if the commands were run sequentially.
     */
    group?: boolean;

    /**
     * A comma-separated list of Chalk colors or a string for available styles listed below to use on prefixes.
     * If there are more commands than colors, the last color will be repeated.
     *
     * Available modifiers:
     * - `reset`, `bold`, `dim`, `italic`, `underline`, `inverse`, `hidden`, `strikethrough`
     *
     * Available colors:
     * - `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `gray`,
     * any hex values for colors (e.g. `#23de43`) or `auto` for an automatically picked color
     *
     * Available background colors:
     * - `bgBlack`, `bgRed`, `bgGreen`, `bgYellow`, `bgBlue`, `bgMagenta`, `bgCyan`, `bgWhite`
     *
     * Set to `false` to disable colors.
     *
     * @see {@link https://www.npmjs.com/package/chalk} for more information.
     */
    prefixColors?: string | string[] | false;

    /**
     * Maximum number of commands to run at once.
     * Exact number or a percent of CPUs available (for example "50%").
     *
     * If undefined, then all processes will start in parallel.
     * Setting this value to 1 will achieve sequential running.
     */
    maxProcesses?: number | string;

    /**
     * Whether commands should be spawned in raw mode.
     * Defaults to false.
     */
    raw?: boolean;

    /**
     * Which commands should have their output hidden.
     */
    hide?: CommandIdentifier[];

    /**
     * The current working directory of commands which didn't specify one.
     * Defaults to `process.cwd()`.
     */
    cwd?: string;

    /**
     * @see CompletionListener
     */
    successCondition?: SuccessCondition;

    /**
     * A signal to stop spawning further processes.
     */
    abortSignal?: AbortSignal;

    /**
     * Which flow controllers should be applied on commands spawned by concurrently.
     * Defaults to an empty array.
     */
    controllers: FlowController[];

    /**
     * A function that will spawn commands.
     * Defaults to a function that spawns using either `cmd.exe` or `/bin/sh`.
     */
    spawn: SpawnCommand;

    /**
     * A function that will kill processes.
     * Defaults to the `tree-kill` module.
     */
    kill: KillProcess;

    /**
     * List of additional arguments passed that will get replaced in each command.
     * If not defined, no argument replacing will happen.
     *
     * @see ExpandArguments
     */
    additionalArguments?: string[];
}

/**
 * Core concurrently functionality -- spawns the given commands concurrently and
 * returns the commands themselves + the result according to the specified success condition.
 *
 * @see CompletionListener
 */
export function concurrently(
    baseCommands: ConcurrentlyCommandInput[],
    baseOptions?: Partial<ConcurrentlyOptions>,
): ConcurrentlyResult {
    assert.ok(Array.isArray(baseCommands), '[concurrently] commands should be an array');
    assert.notStrictEqual(baseCommands.length, 0, '[concurrently] no commands provided');

    const options = { ...defaults, ...baseOptions };

    const prefixColorSelector = new PrefixColorSelector(options.prefixColors || []);

    const commandParsers: CommandParser[] = [
        new StripQuotes(),
        new ExpandShortcut(),
        new ExpandWildcard(),
    ];

    if (options.additionalArguments) {
        commandParsers.push(new ExpandArguments(options.additionalArguments));
    }

    const hide = (options.hide || []).map(String);
    let commands = baseCommands
        .map(mapToCommandInfo)
        .flatMap((command) => parseCommand(command, commandParsers))
        .map((command, index) => {
            const hidden = hide.includes(command.name) || hide.includes(String(index));
            return new Command(
                {
                    index,
                    prefixColor: prefixColorSelector.getNextColor(),
                    ...command,
                },
                getSpawnOpts({
                    ipc: command.ipc,
                    stdio: hidden ? 'hidden' : (command.raw ?? options.raw) ? 'raw' : 'normal',
                    env: command.env,
                    cwd: command.cwd || options.cwd,
                }),
                options.spawn,
                options.kill,
            );
        });

    const handleResult = options.controllers.reduce(
        ({ commands: prevCommands, onFinishCallbacks }, controller) => {
            const { commands, onFinish } = controller.handle(prevCommands);
            return {
                commands,
                onFinishCallbacks: onFinishCallbacks.concat(onFinish ? [onFinish] : []),
            };
        },
        { commands, onFinishCallbacks: [] } as {
            commands: Command[];
            onFinishCallbacks: (() => void)[];
        },
    );
    commands = handleResult.commands;

    if (options.logger && options.outputStream) {
        const outputWriter = new OutputWriter({
            outputStream: options.outputStream,
            group: !!options.group,
            commands,
        });
        options.logger.output
            // Stop trying to write after there's been an error.
            .pipe(takeUntil(outputWriter.error))
            .subscribe(({ command, text }) => outputWriter.write(command, text));
    }

    const commandsLeft = commands.slice();
    const maxProcesses = Math.max(
        1,
        (typeof options.maxProcesses === 'string' && options.maxProcesses.endsWith('%')
            ? Math.round((os.cpus().length * Number(options.maxProcesses.slice(0, -1))) / 100)
            : Number(options.maxProcesses)) || commandsLeft.length,
    );
    for (let i = 0; i < maxProcesses; i++) {
        maybeRunMore(commandsLeft, options.abortSignal);
    }

    const result = new CompletionListener({ successCondition: options.successCondition })
        .listen(commands, options.abortSignal)
        .finally(() => Promise.all(handleResult.onFinishCallbacks.map((onFinish) => onFinish())));

    return {
        result,
        commands,
    };
}

function mapToCommandInfo(command: ConcurrentlyCommandInput): CommandInfo {
    if (typeof command === 'string') {
        return mapToCommandInfo({ command });
    }

    assert.ok(command.command, '[concurrently] command cannot be empty');
    return {
        command: command.command,
        name: command.name || '',
        env: command.env || {},
        cwd: command.cwd || '',
        ipc: command.ipc,
        ...(command.prefixColor
            ? {
                  prefixColor: command.prefixColor,
              }
            : {}),
        ...(command.raw !== undefined
            ? {
                  raw: command.raw,
              }
            : {}),
    };
}

function parseCommand(command: CommandInfo, parsers: CommandParser[]) {
    return parsers.reduce(
        (commands, parser) => commands.flatMap((command) => parser.parse(command)),
        castArray(command),
    );
}

function maybeRunMore(commandsLeft: Command[], abortSignal?: AbortSignal) {
    const command = commandsLeft.shift();
    if (!command || abortSignal?.aborted) {
        return;
    }

    command.start();
    command.close.subscribe(() => {
        maybeRunMore(commandsLeft, abortSignal);
    });
}

```

## File: lib\date-format.spec.ts
```
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { DateFormatter, FormatterOptions } from './date-format.js';

const withTime = (time: string) => `2000-01-01T${time}`;
const withDate = (date: string) => `${date}T00:00:00`;

type TokenTests = undefined | { input: string; expected: string }[];

/**
 * Generates a suite of tests for token `token`.
 *
 * Each entry in `patternTests` makes the token longer, e.g.
 * ```
 * makeTests('year', 'y', [
 *     [{ expected: '2', input: withDate('0002-01-01') }], // y
 *     [{ expected: '02', input: withDate('0002-01-01') }], // yy
 *     // ...
 * ]);
 * ```
 */
const makeTests = (
    name: string,
    token: string,
    patternTests: TokenTests[],
    options?: FormatterOptions,
) =>
    describe(`${name}`, () => {
        patternTests.forEach((tests, i) => {
            const pattern = token.repeat(i + 1);
            if (!tests) {
                return it(`is not implemented for ${pattern}`, () => {
                    expect(() => new DateFormatter(pattern)).toThrow(RangeError);
                });
            } else if (!tests.length) {
                return;
            }

            it.each(tests)(
                `for pattern ${pattern} and input "$input" returns "$expected"`,
                ({ expected, input }) => {
                    const formatter = new DateFormatter(pattern, {
                        locale: 'en',
                        calendar: 'gregory',
                        ...options,
                    });
                    expect(formatter.format(new Date(input))).toBe(expected);
                },
            );
        });
    });

describe('combined', () => {
    it('works with tokens and punctuation', () => {
        const formatter = new DateFormatter('yyyy-MM-dd HH:mm:ss', { locale: 'en' });
        const date = new Date(2024, 8, 1, 15, 30, 50);
        expect(formatter.format(date)).toBe('2024-09-01 15:30:50');
    });

    it('works with tokens and literals', () => {
        const formatter = new DateFormatter("HH 'o''clock'", { locale: 'en' });
        const date = new Date();
        date.setHours(10);
        expect(formatter.format(date)).toBe("10 o'clock");
    });
});

describe('literals', () => {
    it.each([
        ["'", "''"],
        ['foo bar', "'foo bar'"],
        ["foo ' bar", "'foo '' bar'"],
        ["foo bar'?", "'foo bar'''?"],
    ])('returns "%s" for pattern "%s"', (expected, pattern) => {
        const formatter = new DateFormatter(pattern);
        expect(formatter.format(new Date())).toBe(expected);
    });
});

describe('tokens', () => {
    it('throws if a token does not exist', () => {
        expect(() => new DateFormatter('t')).toThrow(SyntaxError);
    });

    makeTests('era', 'G', [
        [
            { input: withDate('-000001-01-01'), expected: 'BC' },
            { input: withDate('0001-01-01'), expected: 'AD' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'BC' },
            { input: withDate('0001-01-01'), expected: 'AD' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'BC' },
            { input: withDate('0001-01-01'), expected: 'AD' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'Before Christ' },
            { input: withDate('0001-01-01'), expected: 'Anno Domini' },
        ],
        [
            { input: withDate('-000001-01-01'), expected: 'B' },
            { input: withDate('0001-01-01'), expected: 'A' },
        ],
    ]);

    makeTests('year', 'y', [
        [
            { expected: '2', input: withDate('0002-01-01') },
            { expected: '20', input: withDate('0020-01-01') },
            { expected: '200', input: withDate('0200-01-01') },
            { expected: '2000', input: withDate('2000-01-01') },
        ],
        [
            { expected: '02', input: withDate('0002-01-01') },
            { expected: '20', input: withDate('0020-01-01') },
            { expected: '00', input: withDate('0200-01-01') },
            { expected: '05', input: withDate('0205-01-01') },
            { expected: '00', input: withDate('2000-01-01') },
            { expected: '05', input: withDate('2005-01-01') },
        ],
        [
            { expected: '002', input: withDate('0002-01-01') },
            { expected: '020', input: withDate('0020-01-01') },
            { expected: '200', input: withDate('0200-01-01') },
            { expected: '2000', input: withDate('2000-01-01') },
        ],
        [
            { expected: '0002', input: withDate('0002-01-01') },
            { expected: '0020', input: withDate('0020-01-01') },
            { expected: '0200', input: withDate('0200-01-01') },
            { expected: '2000', input: withDate('2000-01-01') },
        ],
        [
            { expected: '00002', input: withDate('0002-01-01') },
            { expected: '00020', input: withDate('0020-01-01') },
            { expected: '00200', input: withDate('0200-01-01') },
            { expected: '02000', input: withDate('2000-01-01') },
        ],
    ]);

    describe('year name', () => {
        makeTests('with en locale', 'U', [[{ expected: '2024', input: withDate('2024-01-01') }]], {
            locale: 'en',
        });

        makeTests(
            'with zh-CN locale + chinese calendar',
            'U',
            [[{ expected: '癸卯', input: withDate('2024-01-01') }]],
            { locale: 'zh-CN', calendar: 'chinese' },
        );
    });

    describe('related year', () => {
        makeTests('with en locale', 'r', [[{ expected: '2024', input: withDate('2024-01-01') }]], {
            locale: 'en',
        });

        makeTests(
            'with zh-CN locale + chinese calendar',
            'r',
            [
                [
                    { expected: '2023', input: withDate('2024-01-01') },
                    { expected: '2024', input: withDate('2024-03-01') },
                ],
            ],
            { locale: 'zh-CN', calendar: 'chinese' },
        );
    });

    describe('week year', () => {
        makeTests(
            'with en locale',
            'Y',
            [
                [
                    { expected: '2023', input: withDate('2023-01-01') },
                    { expected: '2024', input: withDate('2023-12-31') },
                    { expected: '2024', input: withDate('2024-01-01') },
                    { expected: '2025', input: withDate('2024-12-31') },
                ],
                [
                    { expected: '23', input: withDate('2023-01-01') },
                    { expected: '24', input: withDate('2023-12-31') },
                    { expected: '24', input: withDate('2024-01-01') },
                    { expected: '25', input: withDate('2024-12-31') },
                ],
            ],
            { locale: 'en' },
        );

        makeTests(
            'with de-DE locale',
            'Y',
            [
                [
                    { expected: '2022', input: withDate('2023-01-01') },
                    { expected: '2023', input: withDate('2023-12-31') },
                    { expected: '2024', input: withDate('2024-01-01') },
                    { expected: '2025', input: withDate('2024-12-31') },
                ],
                [
                    { expected: '22', input: withDate('2023-01-01') },
                    { expected: '23', input: withDate('2023-12-31') },
                    { expected: '24', input: withDate('2024-01-01') },
                    { expected: '25', input: withDate('2024-12-31') },
                ],
            ],
            { locale: 'de-DE' },
        );

        describe(`when minimalDays is missing`, () => {
            beforeAll(() => {
                if (typeof Intl.Locale.prototype.getWeekInfo === 'function') {
                    Intl.Locale.prototype.getWeekInfoOrig = Intl.Locale.prototype.getWeekInfo;
                }

                Intl.Locale.prototype.getWeekInfo = function () {
                    const data =
                        typeof Intl.Locale.prototype.getWeekInfoOrig === 'function'
                            ? this.getWeekInfoOrig()
                            : this.weekInfo;
                    delete data.minimalDays;
                    return data;
                };
            });

            afterAll(() => {
                if (Intl.Locale.prototype.getWeekInfoOrig) {
                    Intl.Locale.prototype.getWeekInfo = Intl.Locale.prototype.getWeekInfoOrig;
                    delete Intl.Locale.prototype.getWeekInfoOrig;
                }
            });

            makeTests(
                // Needs to be a different locale than in tests above to not use cached weekInfo
                'with de-CH locale',
                'Y',
                [
                    [
                        { expected: '2022', input: withDate('2023-01-01') },
                        { expected: '2023', input: withDate('2023-12-31') },
                        { expected: '2024', input: withDate('2024-01-01') },
                        { expected: '2025', input: withDate('2024-12-31') },
                    ],
                    [
                        { expected: '22', input: withDate('2023-01-01') },
                        { expected: '23', input: withDate('2023-12-31') },
                        { expected: '24', input: withDate('2024-01-01') },
                        { expected: '25', input: withDate('2024-12-31') },
                    ],
                ],
                { locale: 'de-CH' },
            );
        });
    });

    makeTests('quarter', 'Q', [
        [
            { expected: '1', input: withDate('2000-01-01') },
            { expected: '2', input: withDate('2000-04-01') },
            { expected: '3', input: withDate('2000-07-01') },
            { expected: '4', input: withDate('2000-10-01') },
        ],
        [
            { expected: '01', input: withDate('2000-01-01') },
            { expected: '02', input: withDate('2000-04-01') },
            { expected: '03', input: withDate('2000-07-01') },
            { expected: '04', input: withDate('2000-10-01') },
        ],
        undefined,
        undefined,
        [
            { expected: '1', input: withDate('2000-01-01') },
            { expected: '2', input: withDate('2000-04-01') },
            { expected: '3', input: withDate('2000-07-01') },
            { expected: '4', input: withDate('2000-10-01') },
        ],
    ]);

    makeTests('quarter - stand-alone', 'q', [
        [
            { expected: '1', input: withDate('2000-01-01') },
            { expected: '2', input: withDate('2000-04-01') },
            { expected: '3', input: withDate('2000-07-01') },
            { expected: '4', input: withDate('2000-10-01') },
        ],
        [
            { expected: '01', input: withDate('2000-01-01') },
            { expected: '02', input: withDate('2000-04-01') },
            { expected: '03', input: withDate('2000-07-01') },
            { expected: '04', input: withDate('2000-10-01') },
        ],
        undefined,
        undefined,
        [
            { expected: '1', input: withDate('2000-01-01') },
            { expected: '2', input: withDate('2000-04-01') },
            { expected: '3', input: withDate('2000-07-01') },
            { expected: '4', input: withDate('2000-10-01') },
        ],
    ]);

    describe('month', () => {
        makeTests(
            'with en locale',
            'M',
            [
                [{ expected: '1', input: withDate('2000-01-01') }],
                [{ expected: '01', input: withDate('2000-01-01') }],
                [{ expected: 'Jan', input: withDate('2000-01-01') }],
                [{ expected: 'January', input: withDate('2000-01-01') }],
                [{ expected: 'J', input: withDate('2000-01-01') }],
            ],
            { locale: 'en' },
        );

        makeTests(
            'with pl locale',
            'M',
            [
                [{ expected: '1', input: withDate('2000-01-01') }],
                [{ expected: '01', input: withDate('2000-01-01') }],
                [{ expected: 'sty', input: withDate('2000-01-01') }],
                [{ expected: 'stycznia', input: withDate('2000-01-01') }],
                [{ expected: 's', input: withDate('2000-01-01') }],
            ],
            { locale: 'pl' },
        );
    });

    describe('month - stand-alone', () => {
        makeTests(
            'with en locale',
            'L',
            [
                [{ expected: '1', input: withDate('2000-01-01') }],
                [{ expected: '01', input: withDate('2000-01-01') }],
                [{ expected: 'Jan', input: withDate('2000-01-01') }],
                [{ expected: 'January', input: withDate('2000-01-01') }],
                [{ expected: 'J', input: withDate('2000-01-01') }],
            ],
            { locale: 'en' },
        );

        makeTests(
            'with pl locale',
            'L',
            [
                [{ expected: '1', input: withDate('2000-01-01') }],
                [{ expected: '01', input: withDate('2000-01-01') }],
                [{ expected: 'sty', input: withDate('2000-01-01') }],
                [{ expected: 'styczeń', input: withDate('2000-01-01') }],
                [{ expected: 'S', input: withDate('2000-01-01') }],
            ],
            { locale: 'pl' },
        );
    });

    describe('week of year', () => {
        makeTests(
            'with en locale',
            'w',
            [
                [
                    { expected: '1', input: withDate('2023-01-01') },
                    { expected: '1', input: withDate('2023-12-31') },
                    { expected: '1', input: withDate('2024-01-01') },
                    { expected: '1', input: withDate('2024-12-31') },
                ],

                [
                    { expected: '01', input: withDate('2023-01-01') },
                    { expected: '01', input: withDate('2023-12-31') },
                    { expected: '01', input: withDate('2024-01-01') },
                    { expected: '01', input: withDate('2024-12-31') },
                ],
            ],
            { locale: 'en' },
        );

        makeTests(
            'with de-DE locale',
            'w',
            [
                [
                    { expected: '52', input: withDate('2023-01-01') },
                    { expected: '52', input: withDate('2023-12-31') },
                    { expected: '1', input: withDate('2024-01-01') },
                    { expected: '1', input: withDate('2024-12-31') },
                ],

                [
                    { expected: '52', input: withDate('2023-01-01') },
                    { expected: '52', input: withDate('2023-12-31') },
                    { expected: '01', input: withDate('2024-01-01') },
                    { expected: '01', input: withDate('2024-12-31') },
                ],
            ],
            { locale: 'de-DE' },
        );
    });

    describe('week of month', () => {
        makeTests(
            'with en locale',
            'W',
            [
                [
                    { expected: '6', input: withDate('2021-01-31') },
                    { expected: '5', input: withDate('2021-02-28') },
                ],
            ],
            { locale: 'en' },
        );

        makeTests(
            'with de-DE locale',
            'W',
            [
                [
                    { expected: '5', input: withDate('2021-01-31') },
                    { expected: '4', input: withDate('2021-02-28') },
                ],
            ],
            { locale: 'de-DE' },
        );
    });

    makeTests('day', 'd', [
        [
            { expected: '1', input: withDate('2000-01-01') },
            { expected: '10', input: withDate('2000-01-10') },
        ],
        [
            { expected: '01', input: withDate('2000-01-01') },
            { expected: '10', input: withDate('2000-01-10') },
        ],
    ]);

    makeTests('day of week in month', 'F', [
        [
            { expected: '1', input: withDate('2024-09-01') },
            { expected: '2', input: withDate('2024-09-08') },
        ],
    ]);

    makeTests('day of year', 'D', [
        [
            { expected: '1', input: withDate('2024-01-01') },
            { expected: '32', input: withDate('2024-02-01') },
            { expected: '366', input: withDate('2024-12-31') },
        ],

        [
            { expected: '01', input: withDate('2024-01-01') },
            { expected: '32', input: withDate('2024-02-01') },
            { expected: '366', input: withDate('2024-12-31') },
        ],

        [
            { expected: '001', input: withDate('2024-01-01') },
            { expected: '032', input: withDate('2024-02-01') },
            { expected: '366', input: withDate('2024-12-31') },
        ],
    ]);

    makeTests('week day', 'E', [
        [{ expected: 'Sat', input: withDate('2024-09-07') }],
        [{ expected: 'Sat', input: withDate('2024-09-07') }],
        [{ expected: 'Sat', input: withDate('2024-09-07') }],
        [{ expected: 'Saturday', input: withDate('2024-09-07') }],
    ]);

    makeTests('local week day', 'e', [
        undefined,
        undefined,
        [{ expected: 'Sat', input: withDate('2024-09-07') }],
        [{ expected: 'Saturday', input: withDate('2024-09-07') }],
    ]);

    makeTests('period', 'a', [
        [
            { expected: 'AM', input: withTime('10:00:00') },
            { expected: 'PM', input: withTime('12:00:00') },
        ],
        [
            { expected: 'AM', input: withTime('10:00:00') },
            { expected: 'PM', input: withTime('12:00:00') },
        ],
        [
            { expected: 'AM', input: withTime('10:00:00') },
            { expected: 'PM', input: withTime('12:00:00') },
        ],
    ]);

    makeTests('flexible day period', 'B', [
        [
            { expected: 'in the morning', input: withTime('06:00:00') },
            { expected: 'noon', input: withTime('12:00:00') },
            { expected: 'in the afternoon', input: withTime('16:00:00') },
            { expected: 'at night', input: withTime('23:00:00') },
        ],
        [],
        [],
        [
            { expected: 'in the morning', input: withTime('06:00:00') },
            { expected: 'noon', input: withTime('12:00:00') },
            { expected: 'in the afternoon', input: withTime('16:00:00') },
            { expected: 'at night', input: withTime('23:00:00') },
        ],
    ]);

    describe('hour', () => {
        makeTests('1-12 format (1 PM)', 'h', [
            [{ expected: '1', input: withTime('13:00:00') }],
            [{ expected: '01', input: withTime('13:00:00') }],
        ]);

        makeTests('1-12 format (12 PM)', 'h', [
            [{ expected: '12', input: withTime('00:00:00') }],
            [{ expected: '12', input: withTime('00:00:00') }],
        ]);

        makeTests('0-23 format', 'H', [
            [
                { expected: '0', input: withTime('00:00:00') },
                { expected: '13', input: withTime('13:00:00') },
            ],
            [
                { expected: '00', input: withTime('00:00:00') },
                { expected: '13', input: withTime('13:00:00') },
            ],
        ]);

        makeTests('0-11 format', 'K', [
            [
                { expected: '0', input: withTime('00:00:00') },
                { expected: '1', input: withTime('13:00:00') },
            ],
            [
                { expected: '00', input: withTime('00:00:00') },
                { expected: '01', input: withTime('13:00:00') },
            ],
        ]);

        makeTests('1-24 format', 'k', [
            [
                { expected: '13', input: withTime('13:00:00') },
                { expected: '24', input: withTime('00:00:00') },
            ],
            [
                { expected: '13', input: withTime('13:00:00') },
                { expected: '24', input: withTime('00:00:00') },
            ],
        ]);
    });

    makeTests('minute', 'm', [
        [
            { expected: '0', input: withTime('00:00:00') },
            { expected: '59', input: withTime('00:59:00') },
        ],
        [
            { expected: '00', input: withTime('00:00:00') },
            { expected: '59', input: withTime('00:59:00') },
        ],
    ]);

    makeTests('seconds', 's', [
        [
            { expected: '0', input: withTime('00:00:00') },
            { expected: '59', input: withTime('00:00:59') },
        ],
        [
            { expected: '00', input: withTime('00:00:00') },
            { expected: '59', input: withTime('00:00:59') },
        ],
    ]);

    makeTests('fractional seconds', 'S', [
        [
            { expected: '0', input: withTime('00:00:00.000') },
            { expected: '0', input: withTime('00:00:00.001') },
            { expected: '0', input: withTime('00:00:00.010') },
            { expected: '1', input: withTime('00:00:00.100') },
        ],

        [
            { expected: '00', input: withTime('00:00:00.000') },
            { expected: '00', input: withTime('00:00:00.001') },
            { expected: '01', input: withTime('00:00:00.010') },
            { expected: '10', input: withTime('00:00:00.100') },
        ],

        [
            { expected: '000', input: withTime('00:00:00.000') },
            { expected: '001', input: withTime('00:00:00.001') },
            { expected: '010', input: withTime('00:00:00.010') },
            { expected: '100', input: withTime('00:00:00.100') },
        ],
    ]);
});

```

## File: lib\date-format.ts
```
export interface FormatterOptions {
    locale?: string;
    calendar?: string;
}

type TokenFormatter = (date: Date, options: FormatterOptions) => string | number;

/**
 * A map of token to its implementations by length.
 * If an index is undefined, then that token length is unsupported.
 */
const tokens = new Map<string, (TokenFormatter | undefined)[]>()
    // era
    .set('G', [
        makeTokenFn({ era: 'short' }, 'era'),
        makeTokenFn({ era: 'short' }, 'era'),
        makeTokenFn({ era: 'short' }, 'era'),
        makeTokenFn({ era: 'long' }, 'era'),
        makeTokenFn({ era: 'narrow' }, 'era'),
    ])
    // year
    .set('y', [
        // TODO: does not support BC years.
        // https://stackoverflow.com/a/41345095/2083599
        (date) => date.getFullYear(),
        (date) => pad(2, date.getFullYear()).slice(-2),
        (date) => pad(3, date.getFullYear()),
        (date) => pad(4, date.getFullYear()),
        (date) => pad(5, date.getFullYear()),
    ])
    .set('Y', [
        getWeekYear,
        (date, options) => pad(2, getWeekYear(date, options)).slice(-2),
        (date, options) => pad(3, getWeekYear(date, options)),
        (date, options) => pad(4, getWeekYear(date, options)),
        (date, options) => pad(5, getWeekYear(date, options)),
    ])
    .set('u', [])
    .set('U', [
        // Fallback implemented as yearName is not available in gregorian calendars, for instance.
        makeTokenFn({ dateStyle: 'full' }, 'yearName', (date) => String(date.getFullYear())),
    ])
    .set('r', [
        // Fallback implemented as relatedYear is not available in gregorian calendars, for instance.
        makeTokenFn({ dateStyle: 'full' }, 'relatedYear', (date) => String(date.getFullYear())),
    ])
    // quarter
    .set('Q', [
        (date) => Math.floor(date.getMonth() / 3) + 1,
        (date) => pad(2, Math.floor(date.getMonth() / 3) + 1),
        // these aren't localized in Intl.DateTimeFormat.
        undefined,
        undefined,
        (date) => Math.floor(date.getMonth() / 3) + 1,
    ])
    .set('q', [
        (date) => Math.floor(date.getMonth() / 3) + 1,
        (date) => pad(2, Math.floor(date.getMonth() / 3) + 1),
        // these aren't localized in Intl.DateTimeFormat.
        undefined,
        undefined,
        (date) => Math.floor(date.getMonth() / 3) + 1,
    ])
    // month
    .set('M', [
        (date) => date.getMonth() + 1,
        (date) => pad(2, date.getMonth() + 1),
        // these include the day so that it forces non-stand-alone month part
        makeTokenFn({ day: 'numeric', month: 'short' }, 'month'),
        makeTokenFn({ day: 'numeric', month: 'long' }, 'month'),
        makeTokenFn({ day: 'numeric', month: 'narrow' }, 'month'),
    ])
    .set('L', [
        (date) => date.getMonth() + 1,
        (date) => pad(2, date.getMonth() + 1),
        makeTokenFn({ month: 'short' }, 'month'),
        makeTokenFn({ month: 'long' }, 'month'),
        makeTokenFn({ month: 'narrow' }, 'month'),
    ])
    .set('l', [() => ''])
    // week
    .set('w', [getWeek, (date, options) => pad(2, getWeek(date, options))])
    .set('W', [getWeekOfMonth])
    // day
    .set('d', [(date) => date.getDate(), (date) => pad(2, date.getDate())])
    .set('D', [
        getDayOfYear,
        (date) => pad(2, getDayOfYear(date)),
        (date) => pad(3, getDayOfYear(date)),
    ])
    .set('F', [(date) => Math.ceil(date.getDate() / 7)])
    .set('g', [])
    // week day
    .set('E', [
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'long' }, 'weekday'),
    ])
    .set('e', [
        undefined,
        undefined,
        makeTokenFn({ weekday: 'short' }, 'weekday'),
        makeTokenFn({ weekday: 'long' }, 'weekday'),
    ])
    .set('c', [])
    // period
    .set('a', [
        makeTokenFn({ hour12: true, timeStyle: 'full' }, 'dayPeriod'),
        makeTokenFn({ hour12: true, timeStyle: 'full' }, 'dayPeriod'),
        makeTokenFn({ hour12: true, timeStyle: 'full' }, 'dayPeriod'),
    ])
    .set('b', [])
    .set('B', [
        makeTokenFn({ dayPeriod: 'short' }, 'dayPeriod'),
        makeTokenFn({ dayPeriod: 'short' }, 'dayPeriod'),
        makeTokenFn({ dayPeriod: 'short' }, 'dayPeriod'),
        makeTokenFn({ dayPeriod: 'long' }, 'dayPeriod'),
    ])
    // hour
    .set('h', [(date) => date.getHours() % 12 || 12, (date) => pad(2, date.getHours() % 12 || 12)])
    .set('H', [(date) => date.getHours(), (date) => pad(2, date.getHours())])
    .set('K', [(date) => date.getHours() % 12, (date) => pad(2, date.getHours() % 12)])
    .set('k', [(date) => date.getHours() % 24 || 24, (date) => pad(2, date.getHours() % 24 || 24)])
    .set('j', [])
    .set('J', [])
    .set('C', [])
    // minute
    .set('m', [(date) => date.getMinutes(), (date) => pad(2, date.getMinutes())])
    // second
    .set('s', [(date) => date.getSeconds(), (date) => pad(2, date.getSeconds())])
    .set('S', [
        (date) => Math.trunc(date.getMilliseconds() / 100),
        (date) => pad(2, Math.trunc(date.getMilliseconds() / 10)),
        (date) => pad(3, Math.trunc(date.getMilliseconds())),
    ])
    .set('A', [])
    // zone
    // none of these have tests
    .set('z', [
        makeTokenFn({ timeZoneName: 'short' }, 'timeZoneName'),
        makeTokenFn({ timeZoneName: 'short' }, 'timeZoneName'),
        makeTokenFn({ timeZoneName: 'short' }, 'timeZoneName'),
        makeTokenFn({ timeZoneName: 'long' }, 'timeZoneName'),
    ])
    .set('Z', [
        undefined,
        undefined,
        undefined,
        // equivalent to `OOOO`.
        makeTokenFn({ timeZoneName: 'longOffset' }, 'timeZoneName'),
    ])
    .set('O', [
        makeTokenFn({ timeZoneName: 'shortOffset' }, 'timeZoneName'),
        undefined,
        undefined,
        // equivalent to `ZZZZ`.
        makeTokenFn({ timeZoneName: 'longOffset' }, 'timeZoneName'),
    ])
    .set('v', [
        makeTokenFn({ timeZoneName: 'shortGeneric' }, 'timeZoneName'),
        undefined,
        undefined,
        makeTokenFn({ timeZoneName: 'longGeneric' }, 'timeZoneName'),
    ])
    .set('V', [])
    .set('X', [])
    .set('x', []);

let locale: Intl.Locale;
function getLocale(options: FormatterOptions): Intl.Locale {
    if (!locale || locale.baseName !== options.locale) {
        locale = new Intl.Locale(
            /* v8 ignore next - fallback value only for safety */
            options.locale || new Intl.DateTimeFormat().resolvedOptions().locale,
        );
    }
    return locale;
}

/**
 * Unicode-compliant date/time formatter.
 *
 * @see https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns
 */
export class DateFormatter {
    private static tokenRegex = /[A-Z]/i;

    private readonly parts: TokenFormatter[] = [];

    constructor(
        pattern: string,
        private readonly options: FormatterOptions = {},
    ) {
        let i = 0;
        while (i < pattern.length) {
            const char = pattern[i];
            const { fn, length } =
                char === "'"
                    ? this.compileLiteral(pattern, i)
                    : DateFormatter.tokenRegex.test(char)
                      ? this.compileToken(pattern, i)
                      : this.compileOther(pattern, i);
            this.parts.push(fn);
            i += length;
        }
    }

    private compileLiteral(pattern: string, offset: number) {
        let length = 1;
        let value = '';
        for (; length < pattern.length; length++) {
            const i = offset + length;
            const char = pattern[i];

            if (char === "'") {
                const nextChar = pattern[i + 1];
                length++;

                // if the next character is another single quote, it's been escaped.
                // if not, then the literal has been closed
                if (nextChar !== "'") {
                    break;
                }
            }

            value += char;
        }

        return { fn: () => value || "'", length };
    }

    private compileOther(pattern: string, offset: number) {
        let value = '';
        while (!DateFormatter.tokenRegex.test(pattern[offset]) && pattern[offset] !== "'") {
            value += pattern[offset++];
        }

        return { fn: () => value, length: value.length };
    }

    private compileToken(pattern: string, offset: number) {
        const type = pattern[offset];
        const token = tokens.get(type);
        if (!token) {
            throw new SyntaxError(`Formatting token "${type}" is invalid`);
        }

        let length = 0;
        while (pattern[offset + length] === type) {
            length++;
        }

        const tokenFn = token[length - 1];
        if (!tokenFn) {
            throw new RangeError(`Formatting token "${type.repeat(length)}" is unsupported`);
        }

        return { fn: tokenFn, length };
    }

    format(date: Date): string {
        return this.parts.reduce((output, part) => output + String(part(date, this.options)), '');
    }
}

/**
 * See https://github.com/moment/luxon/issues/1693
 *
 * @todo Replace once there's a suitable alternative implementation
 */
const fallbackWeekInfo = {
    minimalDays: 4,
};
const weekInfoCache = new Map<string, Intl.WeekInfo>();
function getWeekInfo(locale: Intl.Locale): Intl.WeekInfo {
    let data = weekInfoCache.get(locale.baseName);
    if (!data) {
        // The specs now envisage a method for this,
        // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/getWeekInfo
        data = locale.getWeekInfo?.() ?? locale.weekInfo;
        // The specs have dropped minimalDays,
        // see https://github.com/tc39/proposal-intl-locale-info/issues/86
        if (!data.minimalDays) {
            data = { ...fallbackWeekInfo, ...data };
        }
        weekInfoCache.set(locale.baseName, data);
    }
    return data;
}

/**
 * Creates a token formatting function that returns the value of the chosen part type,
 * using the current locale's settings.
 *
 * If the date/formatter settings doesn't include the requested part type,
 * the `fallback` function is invoked, if specified. If none has been specified, returns an
 * empty string.
 */
function makeTokenFn(
    options: Intl.DateTimeFormatOptions,
    type: Intl.DateTimeFormatPartTypes,
    fallback?: TokenFormatter,
): TokenFormatter {
    let formatter: Intl.DateTimeFormat;
    return (date, formatterOptions) => {
        // Allow tests to set a different locale and have that cause the formatter to be recreated
        if (
            !formatter ||
            formatter.resolvedOptions().locale !== formatterOptions.locale ||
            formatter.resolvedOptions().calendar !== formatterOptions.calendar
        ) {
            formatter = new Intl.DateTimeFormat(formatterOptions.locale, {
                ...options,
                calendar: options.calendar ?? formatterOptions.calendar,
            });
        }

        const parts = formatter.formatToParts(date);
        const part = parts.find((p) => p.type === type);
        /* v8 ignore next - fallback value '' only for safety */
        return part?.value ?? (fallback ? fallback(date, formatterOptions) : '');
    };
}

function startOfWeek(date: Date, options: FormatterOptions) {
    const locale = getLocale(options);
    const weekInfo = getWeekInfo(locale);
    const firstDay = weekInfo.firstDay === 7 ? 0 : weekInfo.firstDay;
    const day = date.getDay();
    const diff = (day < firstDay ? 7 : 0) + day - firstDay;
    date.setDate(date.getDate() - diff);
    date.setHours(0, 0, 0, 0);
    return date;
}

function getWeekYear(date: Date, options: FormatterOptions) {
    const locale = getLocale(options);
    const minimalDays = getWeekInfo(locale).minimalDays;

    const year = date.getFullYear();

    const thisYear = startOfWeek(new Date(year, 0, minimalDays), options);
    const nextYear = startOfWeek(new Date(year + 1, 0, minimalDays), options);

    if (date.getTime() >= nextYear.getTime()) {
        return year + 1;
    } else if (date.getTime() >= thisYear.getTime()) {
        return year;
    } else {
        return year - 1;
    }
}

function getWeek(date: Date, options: FormatterOptions) {
    const locale = getLocale(options);
    const weekMs = 7 * 24 * 3600 * 1000;

    const temp = startOfWeek(new Date(date), options);

    const thisYear = new Date(getWeekYear(date, options), 0, getWeekInfo(locale).minimalDays);
    startOfWeek(thisYear, options);

    const diff = temp.getTime() - thisYear.getTime();
    return Math.round(diff / weekMs) + 1;
}

function getWeekOfMonth(date: Date, options: FormatterOptions) {
    const current = new Date(date);
    current.setHours(0, 0, 0, 0);

    const monthWeekStart = startOfWeek(new Date(date.getFullYear(), date.getMonth(), 1), options);

    const weekMs = 7 * 24 * 3600 * 1000;
    return Math.floor((date.getTime() - monthWeekStart.getTime()) / weekMs) + 1;
}

function getDayOfYear(date: Date) {
    let days = 0;
    for (let i = 0; i <= date.getMonth() - 1; i++) {
        const temp = new Date(date.getFullYear(), i + 1, 0, 0, 0, 0);
        days += temp.getDate();
    }
    return days + date.getDate();
}

function pad(length: number, val: string | number) {
    return String(val).padStart(length, '0');
}

```

## File: lib\defaults.ts
```
// This file is meant to be a shared place for default configs.
// It's read by the flow controllers, the executable, etc.
// Refer to tests for the meaning of the different possible values.

import { SuccessCondition } from './completion-listener.js';

export const defaultInputTarget = 0;

/**
 * Whether process.stdin should be forwarded to child processes.
 */
export const handleInput = false;

/**
 * How many processes to run at once.
 */
export const maxProcesses = 0;

/**
 * Indices and names of commands whose output are not to be logged.
 */
export const hide = '';

/**
 * The character to split <names> on.
 */
export const nameSeparator = ',';

/**
 * Which prefix style to use when logging processes output.
 */
export const prefix = '';

/**
 * Default prefix color.
 * @see https://www.npmjs.com/package/chalk
 */
export const prefixColors = 'reset';

/**
 * How many bytes we'll show on the command prefix.
 */
export const prefixLength = 10;

export const raw = false;

/**
 * Number of attempts of restarting a process, if it exits with non-0 code.
 */
export const restartTries = 0;

/**
 * How many milliseconds concurrently should wait before restarting a process.
 */
export const restartDelay = 0;

/**
 * Condition of success for concurrently itself.
 */
export const success = 'all' as SuccessCondition;

/**
 * Date format used when logging date/time.
 * @see https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
 */
export const timestampFormat = 'yyyy-MM-dd HH:mm:ss.SSS';

/**
 * Current working dir passed as option to spawn command.
 * Defaults to process.cwd()
 */
export const cwd: string | undefined = undefined;

/**
 * Whether to show timing information for processes in console output.
 */
export const timings = false;

/**
 * Passthrough additional arguments to commands (accessible via placeholders) instead of treating them as commands.
 */
export const passthroughArguments = false;

/**
 * Signal to send to other processes if one exits or dies.
 *
 * Defaults to OS specific signal. (SIGTERM on Linux/MacOS)
 */
export const killSignal: string | undefined = undefined;

```

## File: lib\index.ts
```
import process from 'node:process';
import { Readable } from 'node:stream';

import { assertDeprecated } from './assert.js';
import { CloseEvent, Command, CommandIdentifier, TimerEvent } from './command.js';
import {
    concurrently as createConcurrently,
    ConcurrentlyCommandInput,
    ConcurrentlyOptions as BaseConcurrentlyOptions,
    ConcurrentlyResult,
} from './concurrently.js';
import type { FlowController } from './flow-control/flow-controller.js';
import { InputHandler } from './flow-control/input-handler.js';
import { KillOnSignal } from './flow-control/kill-on-signal.js';
import { KillOthers, ProcessCloseCondition } from './flow-control/kill-others.js';
import { LogError } from './flow-control/log-error.js';
import { LogExit } from './flow-control/log-exit.js';
import { LogOutput } from './flow-control/log-output.js';
import { LogTimings } from './flow-control/log-timings.js';
import { LoggerPadding } from './flow-control/logger-padding.js';
import { OutputErrorHandler } from './flow-control/output-error-handler.js';
import { RestartDelay, RestartProcess } from './flow-control/restart-process.js';
import { Teardown } from './flow-control/teardown.js';
import { Logger } from './logger.js';
import { castArray } from './utils.js';

export type ConcurrentlyOptions = Omit<BaseConcurrentlyOptions, 'abortSignal' | 'hide'> & {
    // Logger options
    /**
     * Which command(s) should have their output hidden.
     */
    hide?: CommandIdentifier | CommandIdentifier[];

    /**
     * The prefix format to use when logging a command's output.
     * Defaults to the command's index.
     */
    prefix?: string;

    /**
     * How many characters should a prefix have at most, used when the prefix format is `command`.
     */
    prefixLength?: number;

    /**
     * Pads short prefixes with spaces so that all prefixes have the same length.
     */
    padPrefix?: boolean;

    /**
     * Whether output should be formatted to include prefixes and whether "event" logs will be logged.
     */
    raw?: boolean;

    /**
     * Date format used when logging date/time.
     * @see https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
     */
    timestampFormat?: string;

    // Input handling options
    defaultInputTarget?: CommandIdentifier;
    inputStream?: Readable;
    handleInput?: boolean;
    pauseInputStreamOnFinish?: boolean;

    // Restarting options
    /**
     * How much time in milliseconds to wait before restarting a command.
     *
     * @see RestartProcess
     */
    restartDelay?: RestartDelay;

    /**
     * How many times commands should be restarted when they exit with a failure.
     *
     * @see RestartProcess
     */
    restartTries?: number;

    // Process killing options
    /**
     * @deprecated Use `killOthersOn` instead.
     * @see KillOthers
     */
    killOthers?: ProcessCloseCondition | ProcessCloseCondition[];
    /**
     * Once the first command exits with one of these statuses, kill other commands.
     * @see KillOthers
     */
    killOthersOn?: ProcessCloseCondition | ProcessCloseCondition[];

    /**
     * Signal to send to killed processes.
     */
    killSignal?: string;

    /**
     * How many milliseconds to wait before killing processes.
     */
    killTimeout?: number;

    // Timing options
    /**
     * Whether to output timing information for processes.
     *
     * @see LogTimings
     */
    timings?: boolean;

    /**
     * Clean up command(s) to execute before exiting concurrently.
     * These won't be prefixed and don't affect concurrently's exit code.
     */
    teardown?: readonly string[];

    /**
     * List of additional arguments passed that will get replaced in each command.
     * If not defined, no argument replacing will happen.
     */
    additionalArguments?: string[];
};

export function concurrently(
    commands: ConcurrentlyCommandInput[],
    options: Partial<ConcurrentlyOptions> = {},
) {
    assertDeprecated(options.killOthers === undefined, 'killOthers', 'Use killOthersOn instead.');

    // To avoid empty strings from hiding the output of commands that don't have a name,
    // keep in the list of commands to hide only strings with some length.
    // This might happen through the CLI when no `--hide` argument is specified, for example.
    const hide = castArray(options.hide).filter((id) => id || id === 0);
    const logger =
        options.logger ||
        new Logger({
            hide,
            prefixFormat: options.prefix,
            commandLength: options.prefixLength,
            raw: options.raw,
            timestampFormat: options.timestampFormat,
        });

    if (options.prefixColors === false) {
        logger.toggleColors(false);
    }

    const abortController = new AbortController();
    const outputStream = options.outputStream || process.stdout;

    return createConcurrently(commands, {
        maxProcesses: options.maxProcesses,
        raw: options.raw,
        successCondition: options.successCondition,
        cwd: options.cwd,
        hide,
        logger,
        outputStream,
        group: options.group,
        abortSignal: abortController.signal,
        controllers: [
            // LoggerPadding needs to run before any other controllers that might output something
            ...(options.padPrefix ? [new LoggerPadding({ logger })] : []),
            new LogError({ logger }),
            new LogOutput({ logger }),
            new LogExit({ logger }),
            new InputHandler({
                logger,
                defaultInputTarget: options.defaultInputTarget,
                inputStream:
                    options.inputStream || (options.handleInput ? process.stdin : undefined),
                pauseInputStreamOnFinish: options.pauseInputStreamOnFinish,
            }),
            new KillOnSignal({ process, abortController }),
            new RestartProcess({
                logger,
                delay: options.restartDelay,
                tries: options.restartTries,
            }),
            new KillOthers({
                logger,
                conditions: options.killOthersOn || options.killOthers || [],
                timeoutMs: options.killTimeout,
                killSignal: options.killSignal,
                abortController,
            }),
            new OutputErrorHandler({ abortController, outputStream }),
            new LogTimings({
                logger: options.timings ? logger : undefined,
                timestampFormat: options.timestampFormat,
            }),
            new Teardown({ logger, spawn: options.spawn, commands: options.teardown || [] }),
        ],
        prefixColors: options.prefixColors || [],
        additionalArguments: options.additionalArguments,
    });
}

// Export all flow controllers, types, and the main concurrently function,
// so that 3rd-parties can use them however they want

// Main
export default concurrently;
export { ConcurrentlyCommandInput, ConcurrentlyResult, createConcurrently, Logger };

// Command specific
export { CloseEvent, Command, CommandIdentifier, TimerEvent };

// Flow controllers
export {
    FlowController,
    InputHandler,
    KillOnSignal,
    KillOthers,
    LogError,
    LogExit,
    LogOutput,
    LogTimings,
    RestartProcess,
};

```

## File: lib\jsonc.spec.ts
```
/*
ORIGINAL https://www.npmjs.com/package/tiny-jsonc
BY Fabio Spampinato
MIT license

Copied due to the dependency not being compatible with CommonJS
*/

import { expect, it } from 'vitest';

import JSONC from './jsonc.js';

const fixtures = {
    errors: {
        comment: '// asd',
        empty: '',
        prefix: 'invalid 123',
        suffix: '123 invalid',
        multiLineString: `
        {
            "foo": "/*
            */"
        }
        `,
    },
    parse: {
        input: `
        // Example // Yes
        /* EXAMPLE */ /* YES */
        {
            "one": {},
            "two" :{},
            "three": {
                "one": null,
                "two" :true,
                "three": false,
                "four": "asd\\n\\u0022\\"",
                "five": -123.123e10,
                "six": [ 123, true, [],],
            },
        }
        // Example // Yes
        /* EXAMPLE */ /* YES */
        `,
        output: {
            one: {},
            two: {},
            three: {
                one: null,
                two: true,
                three: false,
                four: 'asd\n\u0022"',
                five: -123.123e10,
                six: [123, true, []],
            },
        },
    },
};

it('supports strings with comments and trailing commas', () => {
    const { input, output } = fixtures.parse;

    expect(JSONC.parse(input)).toEqual(output);
});

it('throws on invalid input', () => {
    const { prefix, suffix } = fixtures.errors;

    expect(() => JSONC.parse(prefix)).toThrow(SyntaxError);
    expect(() => JSONC.parse(suffix)).toThrow(SyntaxError);
});

it('throws on insufficient input', () => {
    const { comment, empty } = fixtures.errors;

    expect(() => JSONC.parse(comment)).toThrow(SyntaxError);
    expect(() => JSONC.parse(empty)).toThrow(SyntaxError);
});

it('throws on multi-line strings', () => {
    const { multiLineString } = fixtures.errors;

    expect(() => JSONC.parse(multiLineString)).toThrow(SyntaxError);
});

```

## File: lib\jsonc.ts
```
/*
ORIGINAL https://www.npmjs.com/package/tiny-jsonc
BY Fabio Spampinato
MIT license

Copied due to the dependency not being compatible with CommonJS
*/

const stringOrCommentRe = /("(?:\\?[\s\S])*?")|(\/\/.*)|(\/\*[\s\S]*?\*\/)/g;
const stringOrTrailingCommaRe = /("(?:\\?[\s\S])*?")|(,\s*)(?=\]|\})/g;

const JSONC = {
    parse: (text: string) => {
        text = String(text); // To be extra safe

        try {
            // Fast path for valid JSON
            return JSON.parse(text);
        } catch {
            // Slow path for JSONC and invalid inputs
            return JSON.parse(
                text.replace(stringOrCommentRe, '$1').replace(stringOrTrailingCommaRe, '$1'),
            );
        }
    },
    stringify: JSON.stringify,
};

export default JSONC;

```

## File: lib\logger.spec.ts
```
import { subscribeSpyTo } from '@hirez_io/observer-spy';
import chalk from 'chalk';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { FakeCommand } from './__fixtures__/fake-command.js';
import { Logger } from './logger.js';

beforeEach(() => {
    // Force Chalk to use colors, otherwise tests may pass when they were supposed to be failing.
    chalk.level = 3;
});

const createLogger = (...options: ConstructorParameters<typeof Logger>) => {
    const logger = new Logger(...options);
    vi.spyOn(logger, 'log');
    const spy = subscribeSpyTo(logger.output);
    return { logger, spy };
};

describe('#log()', () => {
    it('emits prefix + text in the output stream', () => {
        const { logger, spy } = createLogger({});
        logger.log('foo', 'bar');

        const values = spy.getValues();
        expect(values).toHaveLength(2);
        expect(values[0]).toEqual({ command: undefined, text: 'foo' });
        expect(values[1]).toEqual({ command: undefined, text: 'bar' });
    });

    it('emits multiple lines of text with prefix on each', () => {
        const { logger, spy } = createLogger({});
        logger.log('foo', 'bar\nbaz\n');

        const values = spy.getValues();
        expect(values).toHaveLength(2);
        expect(values[0]).toEqual({ command: undefined, text: 'foo' });
        expect(values[1]).toEqual({ command: undefined, text: 'bar\nfoobaz\n' });
    });

    it('does not emit prefix if previous call from same command did not finish with a LF', () => {
        const { logger, spy } = createLogger({});
        const command = new FakeCommand();
        logger.log('foo', 'bar', command);
        logger.log('foo', 'baz', command);

        expect(spy.getValuesLength()).toBe(3);
        expect(spy.getLastValue()).toEqual({ command, text: 'baz' });
    });

    it('emits LF and prefix if previous call is from different command and did not finish with a LF', () => {
        const { logger, spy } = createLogger({});
        const command1 = new FakeCommand();
        logger.log('foo', 'bar', command1);

        const command2 = new FakeCommand();
        logger.log('foo', 'baz', command2);

        const values = spy.getValues();
        expect(values).toHaveLength(5);
        expect(values).toContainEqual({ command: command1, text: '\n' });
        expect(values).toContainEqual({ command: command2, text: 'foo' });
        expect(values).toContainEqual({ command: command2, text: 'baz' });
    });

    it('does not emit prefix nor handle text if logger is in raw mode', () => {
        const { logger, spy } = createLogger({ raw: true });
        logger.log('foo', 'bar\nbaz\n');

        const values = spy.getValues();
        expect(values).toHaveLength(1);
        expect(values[0]).toEqual({ command: undefined, text: 'bar\nbaz\n' });
    });
});

describe('#logGlobalEvent()', () => {
    it('does nothing if in raw mode', () => {
        const { logger } = createLogger({ raw: true });
        logger.logGlobalEvent('foo');

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('logs in gray dim style with arrow prefix', () => {
        const { logger } = createLogger({});
        logger.logGlobalEvent('foo');

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('foo')}\n`,
        );
    });
});

describe('#logCommandText()', () => {
    it('logs with name if no prefixFormat is set', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('bla');
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[bla]')} `, 'foo', cmd);
    });

    it('logs with index if no prefixFormat is set, and command has no name', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('', undefined, 2);
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[2]')} `, 'foo', cmd);
    });

    it('logs with prefixFormat set to pid', () => {
        const { logger } = createLogger({ prefixFormat: 'pid' });
        const cmd = new FakeCommand();
        cmd.pid = 123;
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[123]')} `, 'foo', cmd);
    });

    it('logs with prefixFormat set to name', () => {
        const { logger } = createLogger({ prefixFormat: 'name' });
        const cmd = new FakeCommand('bar');
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[bar]')} `, 'foo', cmd);
    });

    it('logs with prefixFormat set to index', () => {
        const { logger } = createLogger({ prefixFormat: 'index' });
        const cmd = new FakeCommand(undefined, undefined, 3);
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[3]')} `, 'foo', cmd);
    });

    it('logs with prefixFormat set to time (with timestampFormat)', () => {
        const { logger } = createLogger({ prefixFormat: 'time', timestampFormat: 'yyyy' });
        const cmd = new FakeCommand();
        logger.logCommandText('foo', cmd);

        const year = new Date().getFullYear();
        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset(`[${year}]`)} `, 'foo', cmd);
    });

    it('logs with templated prefixFormat', () => {
        const { logger } = createLogger({ prefixFormat: '{index}-{name}' });
        const cmd = new FakeCommand('bar');
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('0-bar')} `, 'foo', cmd);
    });

    it('does not strip spaces from beginning or end of prefixFormat', () => {
        const { logger } = createLogger({ prefixFormat: ' {index}-{name} ' });
        const cmd = new FakeCommand('bar');
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset(' 0-bar ')} `, 'foo', cmd);
    });

    it('logs with no prefix', () => {
        const { logger } = createLogger({ prefixFormat: 'none' });
        const cmd = new FakeCommand();
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(chalk.reset(''), 'foo', cmd);
    });

    it('logs prefix using command line itself', () => {
        const { logger } = createLogger({ prefixFormat: 'command' });
        const cmd = new FakeCommand();
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[echo foo]')} `, 'foo', cmd);
    });

    it('logs prefix using command line itself, capped at commandLength bytes', () => {
        const { logger } = createLogger({ prefixFormat: 'command', commandLength: 6 });
        const cmd = new FakeCommand();
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[ec..oo]')} `, 'foo', cmd);
    });

    it('logs default prefixes with padding', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('foo');
        logger.setPrefixLength(5);
        logger.logCommandText('bar', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[foo  ]')} `, 'bar', cmd);
    });

    it('logs templated prefixes with padding', () => {
        const { logger } = createLogger({ prefixFormat: '{name}-{index}' });
        const cmd = new FakeCommand('foo', undefined, 0);
        logger.setPrefixLength(6);
        logger.logCommandText('bar', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('foo-0 ')} `, 'bar', cmd);
    });

    it('logs prefix using prefixColor from command', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('', undefined, 1, {
            prefixColor: 'blue',
        });
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.blue('[1]')} `, 'foo', cmd);
    });

    it('logs prefix using default color if prefixColor from command is not a valid color', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('', undefined, 1, {
            prefixColor: 'fake.bold',
        });
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(chalk.reset('[1]') + ' ', 'foo', cmd);
    });

    it('logs prefix in gray dim if prefixColor from command does not exist', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('', undefined, 1, {
            prefixColor: 'blue.fake',
        });
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.reset('[1]')} `, 'foo', cmd);
    });

    it('logs prefix using prefixColor from command if prefixColor is a hex value', () => {
        const { logger } = createLogger({});
        const prefixColor = '#32bd8a';
        const cmd = new FakeCommand('', undefined, 1, {
            prefixColor,
        });
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(`${chalk.hex(prefixColor)('[1]')} `, 'foo', cmd);
    });

    it('logs prefix using prefixColor from command if prefixColor is a hex value with modifiers', () => {
        const { logger } = createLogger({});
        const prefixColor = '#32bd8a.inverse';
        const cmd = new FakeCommand('', undefined, 1, {
            prefixColor,
        });
        logger.logCommandText('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.hex(prefixColor).inverse('[1]')} `,
            'foo',
            cmd,
        );
    });

    it('does nothing if command is hidden by name', () => {
        const { logger } = createLogger({ hide: ['abc'] });
        const cmd = new FakeCommand('abc');
        logger.logCommandText('foo', cmd);

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('does nothing if command is hidden by index', () => {
        const { logger } = createLogger({ hide: [3] });
        const cmd = new FakeCommand('', undefined, 3);
        logger.logCommandText('foo', cmd);

        expect(logger.log).not.toHaveBeenCalled();
    });
});

describe('#logCommandEvent()', () => {
    it('does nothing if in raw mode', () => {
        const { logger } = createLogger({ raw: true });
        logger.logCommandEvent('foo', new FakeCommand());

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('does nothing if command is hidden by name', () => {
        const { logger } = createLogger({ hide: ['abc'] });
        const cmd = new FakeCommand('abc');
        logger.logCommandEvent('foo', cmd);

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('does nothing if command is hidden by index', () => {
        const { logger } = createLogger({ hide: [3] });
        const cmd = new FakeCommand('', undefined, 3);
        logger.logCommandEvent('foo', cmd);

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('logs text in gray dim', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('', undefined, 1);
        logger.logCommandEvent('foo', cmd);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('[1]')} `,
            `${chalk.reset('foo')}\n`,
            cmd,
        );
    });

    it('prepends a LF if previous command write did not end with a LF', () => {
        const { logger } = createLogger({});
        const cmd = new FakeCommand('', undefined, 1);
        logger.logCommandText('text', cmd);
        logger.logCommandEvent('event', cmd);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('[1]')} `,
            `\n${chalk.reset('event')}\n`,
            cmd,
        );
    });
});

describe('#logTable()', () => {
    it('does not log anything in raw mode', () => {
        const { logger } = createLogger({ raw: true });
        logger.logTable([{ foo: 1, bar: 2 }]);

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('does not log anything if value is not an array', () => {
        const { logger } = createLogger({});
        logger.logTable({} as never);
        logger.logTable(null as never);
        logger.logTable(0 as never);
        logger.logTable('' as never);

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('does not log anything if array is empty', () => {
        const { logger } = createLogger({});
        logger.logTable([]);

        expect(logger.log).not.toHaveBeenCalled();
    });

    it('does not log anything if array items have no properties', () => {
        const { logger } = createLogger({});
        logger.logTable([{}]);

        expect(logger.log).not.toHaveBeenCalled();
    });

    it("logs a header for each item's properties", () => {
        const { logger } = createLogger({});
        logger.logTable([{ foo: 1, bar: 2 }]);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ foo │ bar │')}\n`,
        );
    });

    it("logs padded headers according to longest column's value", () => {
        const { logger } = createLogger({});
        logger.logTable([{ a: 'foo', b: 'barbaz' }]);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ a   │ b      │')}\n`,
        );
    });

    it("logs each items's values", () => {
        const { logger } = createLogger({});
        logger.logTable([{ foo: 123 }, { foo: 456 }]);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ 123 │')}\n`,
        );
        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ 456 │')}\n`,
        );
    });

    it("logs each items's values with empty column", () => {
        const { logger } = createLogger({});
        logger.logTable([{ foo: 123 }, { foo: null }]);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ 123 │')}\n`,
        );
        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│     │')}\n`,
        );
    });

    it("logs each items's values padded according to longest column's value", () => {
        const { logger } = createLogger({});
        logger.logTable([{ foo: 1 }, { foo: 123 }]);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ 1   │')}\n`,
        );
    });

    it('logs items with different properties in each', () => {
        const { logger } = createLogger({});
        logger.logTable([{ foo: 1 }, { bar: 2 }]);

        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ foo │ bar │')}\n`,
        );
        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│ 1   │     │')}\n`,
        );
        expect(logger.log).toHaveBeenCalledWith(
            `${chalk.reset('-->')} `,
            `${chalk.reset('│     │ 2   │')}\n`,
        );
    });
});

describe('#toggleColors()', () => {
    it('uses supported color level when on', () => {
        const { logger, spy } = createLogger({});
        logger.toggleColors(true);

        const command1 = new FakeCommand('foo', 'command', 0, { prefixColor: 'red' });
        logger.logCommandText('bar', command1);
        logger.logGlobalEvent('baz');

        const texts = spy.getValues().map((value) => value.text);
        expect(texts).toContain(`${chalk.red('[foo]')} `);
        expect(texts).toContain(`${chalk.reset('-->')} `);
    });

    it('uses no colors when off', () => {
        const { logger, spy } = createLogger({});
        logger.toggleColors(false);

        const command1 = new FakeCommand('foo', 'command', 0, { prefixColor: 'red' });
        logger.logCommandText('bar', command1);
        logger.logGlobalEvent('baz');

        const texts = spy.getValues().map((value) => value.text);
        expect(texts).toContain('[foo] ');
        expect(texts).toContain('--> ');
    });
});

```

## File: lib\logger.ts
```
import chalk, { Chalk, ChalkInstance } from 'chalk';
import Rx from 'rxjs';

import { Command, CommandIdentifier } from './command.js';
import { DateFormatter } from './date-format.js';
import * as defaults from './defaults.js';
import { escapeRegExp } from './utils.js';

const defaultChalk = chalk;
const noColorChalk = new Chalk({ level: 0 });

function getChalkPath(chalk: ChalkInstance, path: string): ChalkInstance | undefined {
    return path
        .split('.')
        .reduce(
            (prev, key) => prev && (prev as unknown as Record<string, ChalkInstance>)[key],
            chalk,
        );
}

export class Logger {
    private readonly hide: CommandIdentifier[];
    private readonly raw: boolean;
    private readonly prefixFormat?: string;
    private readonly commandLength: number;
    private readonly dateFormatter: DateFormatter;

    private chalk = defaultChalk;

    /**
     * How many characters should a prefix have.
     * Prefixes shorter than this will be padded with spaces to the right.
     */
    private prefixLength = 0;

    /**
     * Last character emitted, and from which command.
     * If `undefined`, then nothing has been logged yet.
     */
    private lastWrite?: { command: Command | undefined; char: string };

    /**
     * Observable that emits when there's been output logged.
     * If `command` is is `undefined`, then the log is for a global event.
     */
    readonly output = new Rx.Subject<{ command: Command | undefined; text: string }>();

    constructor({
        hide,
        prefixFormat,
        commandLength,
        raw = false,
        timestampFormat,
    }: {
        /**
         * Which commands should have their output hidden.
         */
        hide?: CommandIdentifier[];

        /**
         * Whether output should be formatted to include prefixes and whether "event" logs will be
         * logged.
         */
        raw?: boolean;

        /**
         * The prefix format to use when logging a command's output.
         * Defaults to the command's index.
         */
        prefixFormat?: string;

        /**
         * How many characters should a prefix have at most when the format is `command`.
         */
        commandLength?: number;

        /**
         * Date format used when logging date/time.
         * @see https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
         */
        timestampFormat?: string;
    }) {
        this.hide = (hide || []).map(String);
        this.raw = raw;
        this.prefixFormat = prefixFormat;
        this.commandLength = commandLength || defaults.prefixLength;
        this.dateFormatter = new DateFormatter(timestampFormat || defaults.timestampFormat);
    }

    /**
     * Toggles colors on/off globally.
     */
    toggleColors(on: boolean) {
        this.chalk = on ? defaultChalk : noColorChalk;
    }

    private shortenText(text: string) {
        if (!text || text.length <= this.commandLength) {
            return text;
        }

        const ellipsis = '..';
        const prefixLength = this.commandLength - ellipsis.length;
        const endLength = Math.floor(prefixLength / 2);
        const beginningLength = prefixLength - endLength;

        const beginning = text.slice(0, beginningLength);
        const end = text.slice(text.length - endLength, text.length);
        return beginning + ellipsis + end;
    }

    private getPrefixesFor(command: Command): Record<string, string> {
        return {
            // When there's limited concurrency, the PID might not be immediately available,
            // so avoid the string 'undefined' from becoming a prefix
            pid: command.pid != null ? String(command.pid) : '',
            index: String(command.index),
            name: command.name,
            command: this.shortenText(command.command),
            time: this.dateFormatter.format(new Date()),
        };
    }

    getPrefixContent(
        command: Command,
    ): { type: 'default' | 'template'; value: string } | undefined {
        const prefix = this.prefixFormat || (command.name ? 'name' : 'index');
        if (prefix === 'none') {
            return;
        }

        const prefixes = this.getPrefixesFor(command);
        if (Object.keys(prefixes).includes(prefix)) {
            return { type: 'default', value: prefixes[prefix] };
        }

        const value = Object.entries(prefixes).reduce((prev, [key, val]) => {
            const keyRegex = new RegExp(escapeRegExp(`{${key}}`), 'g');
            return prev.replace(keyRegex, String(val));
        }, prefix);
        return { type: 'template', value };
    }

    getPrefix(command: Command): string {
        const content = this.getPrefixContent(command);
        if (!content) {
            return '';
        }

        return content.type === 'template'
            ? content.value.padEnd(this.prefixLength, ' ')
            : `[${content.value.padEnd(this.prefixLength, ' ')}]`;
    }

    setPrefixLength(length: number) {
        this.prefixLength = length;
    }

    colorText(command: Command, text: string) {
        let color: ChalkInstance;
        if (command.prefixColor?.startsWith('#')) {
            const [hexColor, ...modifiers] = command.prefixColor.split('.');
            color = this.chalk.hex(hexColor);
            const modifiedColor = getChalkPath(color, modifiers.join('.'));
            if (modifiedColor) {
                color = modifiedColor;
            }
        } else {
            const defaultColor = getChalkPath(this.chalk, defaults.prefixColors) as ChalkInstance;
            color = getChalkPath(this.chalk, command.prefixColor ?? '') ?? defaultColor;
        }
        return color(text);
    }

    /**
     * Logs an event for a command (e.g. start, stop).
     *
     * If raw mode is on, then nothing is logged.
     */
    logCommandEvent(text: string, command: Command) {
        if (this.raw) {
            return;
        }

        // Last write was from this command, but it didn't end with a line feed.
        // Prepend one, otherwise the event's text will be concatenated to that write.
        // A line feed is otherwise inserted anyway.
        let prefix = '';
        if (this.lastWrite?.command === command && this.lastWrite.char !== '\n') {
            prefix = '\n';
        }
        this.logCommandText(`${prefix}${this.chalk.reset(text)}\n`, command);
    }

    logCommandText(text: string, command: Command) {
        if (this.hide.includes(String(command.index)) || this.hide.includes(command.name)) {
            return;
        }

        const prefix = this.colorText(command, this.getPrefix(command));
        return this.log(prefix + (prefix ? ' ' : ''), text, command);
    }

    /**
     * Logs a global event (e.g. sending signals to processes).
     *
     * If raw mode is on, then nothing is logged.
     */
    logGlobalEvent(text: string) {
        if (this.raw) {
            return;
        }

        this.log(`${this.chalk.reset('-->')} `, `${this.chalk.reset(text)}\n`);
    }

    /**
     * Logs a table from an input object array, like `console.table`.
     *
     * Each row is a single input item, and they are presented in the input order.
     */
    logTable(tableContents: Record<string, unknown>[]) {
        // For now, can only print array tables with some content.
        if (this.raw || !Array.isArray(tableContents) || !tableContents.length) {
            return;
        }

        let nextColIndex = 0;
        const headers: Record<string, { index: number; length: number }> = {};
        const contentRows = tableContents.map((row) => {
            const rowContents: string[] = [];
            Object.keys(row).forEach((col) => {
                if (!headers[col]) {
                    headers[col] = {
                        index: nextColIndex++,
                        length: col.length,
                    };
                }

                const colIndex = headers[col].index;
                const formattedValue = String(row[col] == null ? '' : row[col]);
                // Update the column length in case this rows value is longer than the previous length for the column.
                headers[col].length = Math.max(formattedValue.length, headers[col].length);
                rowContents[colIndex] = formattedValue;
                return rowContents;
            });
            return rowContents;
        });

        const headersFormatted = Object.keys(headers).map((header) =>
            header.padEnd(headers[header].length, ' '),
        );

        if (!headersFormatted.length) {
            // No columns exist.
            return;
        }

        const borderRowFormatted = headersFormatted.map((header) => '─'.padEnd(header.length, '─'));

        this.logGlobalEvent(`┌─${borderRowFormatted.join('─┬─')}─┐`);
        this.logGlobalEvent(`│ ${headersFormatted.join(' │ ')} │`);
        this.logGlobalEvent(`├─${borderRowFormatted.join('─┼─')}─┤`);

        contentRows.forEach((contentRow) => {
            const contentRowFormatted = headersFormatted.map((header, colIndex) => {
                // If the table was expanded after this row was processed, it won't have this column.
                // Use an empty string in this case.
                const col = contentRow[colIndex] || '';
                return col.padEnd(header.length, ' ');
            });
            this.logGlobalEvent(`│ ${contentRowFormatted.join(' │ ')} │`);
        });

        this.logGlobalEvent(`└─${borderRowFormatted.join('─┴─')}─┘`);
    }

    log(prefix: string, text: string, command?: Command) {
        if (this.raw) {
            return this.emit(command, text);
        }

        // #70 - replace some ANSI code that would impact clearing lines
        text = text.replace(/\u2026/g, '...');

        // This write's interrupting another command, emit a line feed to start clean.
        if (this.lastWrite && this.lastWrite.command !== command && this.lastWrite.char !== '\n') {
            this.emit(this.lastWrite.command, '\n');
        }

        // Clean lines should emit a prefix
        if (!this.lastWrite || this.lastWrite.char === '\n') {
            this.emit(command, prefix);
        }

        const textToWrite = text.replaceAll('\n', (lf, i) => lf + (text[i + 1] ? prefix : ''));
        this.emit(command, textToWrite);
    }

    emit(command: Command | undefined, text: string) {
        this.lastWrite = { command, char: text[text.length - 1] };
        this.output.next({ command, text });
    }
}

```

## File: lib\observables.spec.ts
```
import EventEmitter from 'node:events';

import { describe, expect, it } from 'vitest';

import { fromSharedEvent } from './observables.js';

describe('fromSharedEvent()', () => {
    it('returns same observable for event emitter/name pair', () => {
        const emitter = new EventEmitter();
        const obs1 = fromSharedEvent(emitter, 'foo');
        const obs2 = fromSharedEvent(emitter, 'foo');
        expect(obs1).toBe(obs2);
    });

    it('returns different observables for different event emitter/name pairs', () => {
        const emitter = new EventEmitter();
        const obs1 = fromSharedEvent(emitter, 'foo');
        const obs2 = fromSharedEvent(emitter, 'bar');
        expect(obs1).not.toBe(obs2);

        const emitter2 = new EventEmitter();
        const obs3 = fromSharedEvent(emitter2, 'foo');
        const obs4 = fromSharedEvent(emitter2, 'bar');
        expect(obs1).not.toBe(obs3);
        expect(obs2).not.toBe(obs4);
    });

    it('sets up listener only once per event emitter/name pair', () => {
        const emitter = new EventEmitter();
        const observable = fromSharedEvent(emitter, 'foo');
        observable.subscribe();
        observable.subscribe();

        expect(emitter.listenerCount('foo')).toBe(1);
    });
});

```

## File: lib\observables.ts
```
import EventEmitter from 'node:events';

import { fromEvent, Observable, share } from 'rxjs';

const sharedEvents = new WeakMap<EventEmitter, Map<string, Observable<unknown>>>();

/**
 * Creates an observable for a specific event of an `EventEmitter` instance.
 *
 * The underlying event listener is set up only once across the application for that event emitter/name pair.
 */
export function fromSharedEvent(emitter: EventEmitter, event: string): Observable<unknown> {
    let emitterEvents = sharedEvents.get(emitter);
    if (!emitterEvents) {
        emitterEvents = new Map();
        sharedEvents.set(emitter, emitterEvents);
    }

    let observable = emitterEvents.get(event);
    if (!observable) {
        observable = fromEvent(emitter, event).pipe(share());
        emitterEvents.set(event, observable);
    }

    return observable;
}

```

## File: lib\output-writer.spec.ts
```
import { Writable } from 'node:stream';

import { beforeEach, describe, expect, it, MockedObject } from 'vitest';

import { createMockInstance } from './__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from './__fixtures__/fake-command.js';
import { OutputWriter } from './output-writer.js';

let outputStream: MockedObject<Writable>;
let commands: FakeCommand[];

function createWriter(overrides?: { group: boolean }) {
    const options = {
        outputStream,
        group: false,
        commands,
        ...overrides,
    };
    return new OutputWriter(options);
}

function closeCommand(command: FakeCommand) {
    command.state = 'exited';
    command.close.next(createFakeCloseEvent({ command, index: command.index }));
}

beforeEach(() => {
    outputStream = createMockInstance(Writable);
    commands = [
        new FakeCommand('', undefined, 0),
        new FakeCommand('', undefined, 1),
        new FakeCommand('', undefined, 2),
    ];
});

it('throws if outputStream already is in errored state', () => {
    Object.defineProperty(outputStream, 'errored', { value: new Error('test') });
    expect(() => createWriter()).toThrow(TypeError);
});

describe('#write()', () => {
    it('throws if outputStream has errored', () => {
        const writer = createWriter();
        Object.defineProperty(outputStream, 'errored', { value: new Error('test') });
        expect(() => writer.write(commands[0], 'hello')).toThrow(TypeError);
    });

    describe('with group=false', () => {
        it('writes instantly', () => {
            const writer = createWriter({ group: false });
            writer.write(commands[2], 'hello');
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
        });
    });

    describe('with group=true', () => {
        it('writes for null commands', () => {
            const writer = createWriter({ group: true });
            writer.write(undefined, 'hello');
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
        });

        it('does not write instantly for non-active command', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[2], 'hello');
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            expect(writer.buffers[2]).toEqual(['hello']);
        });

        it('write instantly for active command', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[0], 'hello');
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
        });

        it('does not wait for write from next command to flush', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[1], 'hello');
            writer.write(commands[1], 'foo bar');
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[0]);
            expect(outputStream.write).toHaveBeenCalledTimes(2);
            expect(writer.activeCommandIndex).toBe(1);
            outputStream.write.mockClear();

            writer.write(commands[1], 'blah');
            expect(outputStream.write).toHaveBeenCalledTimes(1);
        });

        it('does not flush for non-active command', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[1], 'hello');
            writer.write(commands[1], 'foo bar');
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[1]);
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[0]);
            expect(outputStream.write).toHaveBeenCalledTimes(2);
        });

        it('flushes multiple commands at a time if necessary', () => {
            const writer = createWriter({ group: true });
            writer.write(commands[2], 'hello');
            closeCommand(commands[1]);
            closeCommand(commands[2]);
            expect(outputStream.write).toHaveBeenCalledTimes(0);
            closeCommand(commands[0]);
            expect(outputStream.write).toHaveBeenCalledExactlyOnceWith('hello');
            expect(writer.activeCommandIndex).toBe(2);
        });
    });
});

```

## File: lib\output-writer.ts
```
import { Writable } from 'node:stream';

import Rx from 'rxjs';

import { Command } from './command.js';
import { fromSharedEvent } from './observables.js';

/**
 * Class responsible for actually writing output onto a writable stream.
 */
export class OutputWriter {
    private readonly outputStream: Writable;
    private readonly group: boolean;
    readonly buffers: string[][];
    activeCommandIndex = 0;

    readonly error: Rx.Observable<unknown>;
    private get errored() {
        return this.outputStream.errored;
    }

    constructor({
        outputStream,
        group,
        commands,
    }: {
        outputStream: Writable;
        group: boolean;
        commands: Command[];
    }) {
        this.outputStream = outputStream;
        this.ensureWritable();

        this.error = fromSharedEvent(this.outputStream, 'error');
        this.group = group;
        this.buffers = commands.map(() => []);

        if (this.group) {
            Rx.merge(...commands.map((c) => c.close)).subscribe((command) => {
                if (command.index !== this.activeCommandIndex) {
                    return;
                }
                for (let i = command.index + 1; i < commands.length; i++) {
                    this.activeCommandIndex = i;
                    this.flushBuffer(i);
                    // TODO: Should errored commands also flush buffer?
                    if (commands[i].state !== 'exited') {
                        break;
                    }
                }
            });
        }
    }

    private ensureWritable() {
        if (this.errored) {
            throw new TypeError('outputStream is in errored state', { cause: this.errored });
        }
    }

    write(command: Command | undefined, text: string) {
        this.ensureWritable();
        if (this.group && command) {
            if (command.index <= this.activeCommandIndex) {
                this.outputStream.write(text);
            } else {
                this.buffers[command.index].push(text);
            }
        } else {
            // "global" logs (command=null) are output out of order
            this.outputStream.write(text);
        }
    }

    private flushBuffer(index: number) {
        if (!this.errored) {
            this.buffers[index].forEach((t) => this.outputStream.write(t));
        }
        this.buffers[index] = [];
    }
}

```

## File: lib\prefix-color-selector.spec.ts
```
import { ChalkInstance } from 'chalk';
import { afterEach, describe, expect, it, vi } from 'vitest';

import { PrefixColorSelector } from './prefix-color-selector.js';

afterEach(() => {
    vi.restoreAllMocks();
});

describe('#getNextColor()', () => {
    const customTests: Record<
        string,
        {
            acceptableConsoleColors?: Array<keyof ChalkInstance>;
            customColors?: string | string[];
            expectedColors: string[];
        }
    > = {
        'does not produce a color if prefixColors empty': {
            customColors: [],
            expectedColors: ['', '', ''],
        },
        'does not produce a color if prefixColors undefined': {
            expectedColors: ['', '', ''],
        },
        'uses user defined prefix colors only, if no auto is used': {
            customColors: ['red', 'green', 'blue'],
            expectedColors: [
                'red',
                'green',
                'blue',

                // Uses last color if last color is not "auto"
                'blue',
                'blue',
                'blue',
            ],
        },
        'trims colors': {
            customColors: ['  red  ', '  green  ', '  blue  '],
            expectedColors: ['red', 'green', 'blue'],
        },
        'accepts a string value for customColors': {
            customColors: 'red',
            expectedColors: ['red', 'red'],
        },
        'picks varying colors when user defines an auto color': {
            acceptableConsoleColors: ['green', 'blue'],
            customColors: [
                'red',
                'green',
                'auto',
                'green',
                'auto',
                'green',
                'auto',
                'blue',
                'auto',
                'orange',
            ],
            expectedColors: [
                // Custom colors
                'red',
                'green',
                'blue', // Picks auto color "blue", not repeating consecutive "green" color
                'green', // Manual
                'blue', // Auto picks "blue" not to repeat last
                'green', // Manual
                'blue', // Auto picks "blue" again not to repeat last
                'blue', // Manual
                'green', // Auto picks "green" again not to repeat last
                'orange',

                // Uses last color if last color is not "auto"
                'orange',
                'orange',
                'orange',
            ],
        },
        'uses user defined colors then recurring auto colors without repeating consecutive colors':
            {
                acceptableConsoleColors: ['green', 'blue'],
                customColors: ['red', 'green', 'auto'],
                expectedColors: [
                    // Custom colors
                    'red',
                    'green',

                    // Picks auto colors, not repeating consecutive "green" color
                    'blue',
                    'green',
                    'blue',
                    'green',
                ],
            },
        'can sometimes produce consecutive colors': {
            acceptableConsoleColors: ['green', 'blue'],
            customColors: ['blue', 'auto'],
            expectedColors: [
                // Custom colors
                'blue',

                // Picks auto colors
                'green',
                // Does not repeat custom colors for initial auto colors, i.e. does not use "blue" again so soon
                'green', // Consecutive color picked, however practically there would be a lot of colors that need to be set in a particular order for this to occur
                'blue',
                'green',
                'blue',
                'green',
                'blue',
            ],
        },
        'considers the Bright variants of colors equal to the normal colors to avoid similar colors':
            {
                acceptableConsoleColors: ['greenBright', 'blueBright', 'green', 'blue', 'magenta'],
                customColors: ['green', 'blue', 'auto'],
                expectedColors: [
                    // Custom colors
                    'green',
                    'blue',

                    // Picks auto colors, not repeating green and blue colors and variants initially
                    'magenta',

                    // Picks auto colors
                    'greenBright',
                    'blueBright',
                    'green',
                    'blue',
                    'magenta',
                ],
            },
    };
    it.each(Object.entries(customTests))(
        '%s',
        (_, { acceptableConsoleColors, customColors, expectedColors }) => {
            if (acceptableConsoleColors) {
                vi.spyOn(PrefixColorSelector, 'ACCEPTABLE_CONSOLE_COLORS', 'get').mockReturnValue(
                    acceptableConsoleColors,
                );
            }
            const prefixColorSelector = new PrefixColorSelector(customColors);
            const prefixColorSelectorValues = expectedColors.map(() =>
                prefixColorSelector.getNextColor(),
            );

            expect(prefixColorSelectorValues).toEqual(expectedColors);
        },
    );

    const autoTests = {
        'does not repeat consecutive colors when last prefixColor is auto': false,
        'handles when more individual auto prefixColors exist than acceptable console colors': true,
    };
    it.each(Object.entries(autoTests))('%s', (_, map) => {
        // Pick auto colors over 2 sets
        const expectedColors: string[] = [
            ...PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS,
            ...PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS,
        ];

        const prefixColorSelector = new PrefixColorSelector(
            map ? expectedColors.map(() => 'auto') : ['auto'],
        );

        let previousColor = '';
        for (const expectedColor of expectedColors) {
            const actualSelectedColor = prefixColorSelector.getNextColor();
            expect(actualSelectedColor).not.toBe(previousColor); // No consecutive colors
            expect(actualSelectedColor).toBe(expectedColor); // Expected color
            previousColor = actualSelectedColor;
        }
    });
});

describe('#ACCEPTABLE_CONSOLE_COLORS', () => {
    it('has more than 1 auto color defined', () => {
        // (!) The current implementation is based on the assumption that 'ACCEPTABLE_CONSOLE_COLORS'
        //     always has more than one entry, which is what we enforce via this test
        expect(PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS.length).toBeGreaterThan(1);
    });
});

```

## File: lib\prefix-color-selector.ts
```
import { ChalkInstance } from 'chalk';

function getConsoleColorsWithoutCustomColors(customColors: string[]): string[] {
    return PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS.filter(
        // Consider the "Bright" variants of colors to be the same as the plain color to avoid similar colors
        (color) => !customColors.includes(color.replace(/Bright$/, '')),
    );
}

/**
 * Creates a generator that yields an infinite stream of colors.
 */
function* createColorGenerator(customColors: string[]): Generator<string, string> {
    // Custom colors should be used as is, except for "auto"
    const nextAutoColors: string[] = getConsoleColorsWithoutCustomColors(customColors);
    let lastColor: string | undefined;
    for (const customColor of customColors) {
        let currentColor = customColor;
        if (currentColor !== 'auto') {
            yield currentColor; // Manual color
        } else {
            // Find the first auto color that is not the same as the last color
            while (currentColor === 'auto' || lastColor === currentColor) {
                if (!nextAutoColors.length) {
                    // There could be more "auto" values than auto colors so this needs to be able to refill
                    nextAutoColors.push(...PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS);
                }
                currentColor = String(nextAutoColors.shift());
            }
            yield currentColor; // Auto color
        }
        lastColor = currentColor;
    }

    const lastCustomColor = customColors[customColors.length - 1] || '';
    if (lastCustomColor !== 'auto') {
        while (true) {
            yield lastCustomColor; // If last custom color was not "auto" then return same color forever, to maintain existing behavior
        }
    }

    // Finish the initial set(s) of auto colors to avoid repetition
    for (const color of nextAutoColors) {
        yield color;
    }

    // Yield an infinite stream of acceptable console colors
    //
    // If the given custom colors use every ACCEPTABLE_CONSOLE_COLORS except one then there is a chance a color will be repeated,
    // however its highly unlikely and low consequence so not worth the extra complexity to account for it
    while (true) {
        for (const color of PrefixColorSelector.ACCEPTABLE_CONSOLE_COLORS) {
            yield color; // Repeat colors forever
        }
    }
}

export class PrefixColorSelector {
    private colorGenerator: Generator<string, string>;

    constructor(customColors: string | string[] = []) {
        const normalizedColors = typeof customColors === 'string' ? [customColors] : customColors;
        this.colorGenerator = createColorGenerator(normalizedColors);
    }

    /** A list of colors that are readable in a terminal. */
    public static get ACCEPTABLE_CONSOLE_COLORS() {
        // Colors picked randomly, can be amended if required
        return [
            // Prevent duplicates, in case the list becomes significantly large
            ...new Set<keyof ChalkInstance>([
                // Text colors
                'cyan',
                'yellow',
                'greenBright',
                'blueBright',
                'magentaBright',
                'white',
                'grey',
                'red',

                // Background colors
                'bgCyan',
                'bgYellow',
                'bgGreenBright',
                'bgBlueBright',
                'bgMagenta',
                'bgWhiteBright',
                'bgGrey',
                'bgRed',
            ]),
        ];
    }

    /**
     * @returns The given custom colors then a set of acceptable console colors indefinitely.
     */
    getNextColor(): string {
        return this.colorGenerator.next().value.trim();
    }
}

```

## File: lib\spawn.spec.ts
```
import { describe, expect, it, vi } from 'vitest';

import { getSpawnOpts, spawn } from './spawn.js';

const baseProcess = {
    platform: 'win32' as const,
    cwd: () => '',
    env: {},
};

describe('spawn()', () => {
    it('spawns the given command', async () => {
        const fakeSpawn = vi.fn();
        spawn('echo banana', {}, fakeSpawn, baseProcess);
        expect(fakeSpawn).toHaveBeenCalled();
        expect(fakeSpawn.mock.calls[0][1].join(' ')).toContain('echo banana');
    });

    it('returns spawned process', async () => {
        const childProcess = {};
        const fakeSpawn = vi.fn().mockReturnValue(childProcess);
        const child = spawn('echo banana', {}, fakeSpawn, baseProcess);
        expect(child).toBe(childProcess);
    });
});

describe('getSpawnOpts()', () => {
    it('sets detached mode to false for Windows platform', () => {
        expect(getSpawnOpts({ process: baseProcess }).detached).toBe(false);
    });

    it('sets stdio to pipe when stdio mode is normal', () => {
        expect(getSpawnOpts({ stdio: 'normal' }).stdio).toEqual(['pipe', 'pipe', 'pipe']);
    });

    it('sets stdio to inherit when stdio mode is raw', () => {
        expect(getSpawnOpts({ stdio: 'raw' }).stdio).toEqual(['inherit', 'inherit', 'inherit']);
    });

    it('sets stdio to ignore stdout + stderr when stdio mode is hidden', () => {
        expect(getSpawnOpts({ stdio: 'hidden' }).stdio).toEqual(['pipe', 'ignore', 'ignore']);
    });

    it('sets an ipc channel at the specified descriptor index', () => {
        const opts = getSpawnOpts({ ipc: 3 });
        expect(opts.stdio?.[3]).toBe('ipc');
    });

    it('throws if the ipc channel is <= 2', () => {
        const fn = () => getSpawnOpts({ ipc: 0 });
        expect(fn).toThrow();
    });

    it('merges FORCE_COLOR into env vars if color supported', () => {
        const process = { ...baseProcess, env: { foo: 'bar' } };
        expect(getSpawnOpts({ process, colorSupport: false }).env).toEqual(process.env);
        expect(getSpawnOpts({ process, colorSupport: { level: 1 } }).env).toEqual({
            FORCE_COLOR: '1',
            foo: 'bar',
        });
    });

    it('sets default cwd to process.cwd()', () => {
        const process = { ...baseProcess, cwd: () => 'process-cwd' };
        expect(getSpawnOpts({ process }).cwd).toBe('process-cwd');
    });

    it('overrides default cwd', () => {
        const cwd = 'foobar';
        expect(getSpawnOpts({ cwd }).cwd).toBe(cwd);
    });
});

```

## File: lib\spawn.ts
```
import assert from 'node:assert';
import { ChildProcess, IOType, spawn as baseSpawn, SpawnOptions } from 'node:child_process';
import nodeProcess from 'node:process';

import supportsColor, { ColorSupport } from 'supports-color';

/**
 * Spawns a command using `cmd.exe` on Windows, or `/bin/sh` elsewhere.
 */
// Implementation based off of https://github.com/mmalecki/spawn-command/blob/v0.0.2-1/lib/spawn-command.js
export function spawn(
    command: string,
    options: SpawnOptions,
    // For testing
    spawn: (command: string, args: string[], options: SpawnOptions) => ChildProcess = baseSpawn,
    process: Pick<NodeJS.Process, 'platform'> = nodeProcess,
): ChildProcess {
    let file = '/bin/sh';
    let args = ['-c', command];
    if (process.platform === 'win32') {
        file = 'cmd.exe';
        args = ['/s', '/c', `"${command}"`];
        options.windowsVerbatimArguments = true;
    }
    return spawn(file, args, options);
}

export const getSpawnOpts = ({
    colorSupport = supportsColor.stdout,
    cwd,
    process = nodeProcess,
    ipc,
    stdio = 'normal',
    env = {},
}: {
    /**
     * What the color support of the spawned processes should be.
     * If set to `false`, then no colors should be output.
     *
     * Defaults to whatever the terminal's stdout support is.
     */
    colorSupport?: Pick<ColorSupport, 'level'> | false;

    /**
     * The NodeJS process.
     */
    process?: Pick<NodeJS.Process, 'cwd' | 'platform' | 'env'>;

    /**
     * A custom working directory to spawn processes in.
     * Defaults to `process.cwd()`.
     */
    cwd?: string;

    /**
     * The file descriptor number at which the channel for inter-process communication
     * should be set up.
     */
    ipc?: number;

    /**
     * Which stdio mode to use. Raw implies inheriting the parent process' stdio.
     *
     * - `normal`: all of stdout, stderr and stdin are piped
     * - `hidden`: stdin is piped, stdout/stderr outputs are ignored
     * - `raw`: all of stdout, stderr and stdin are inherited from the main process
     *
     * Defaults to `normal`.
     */
    stdio?: 'normal' | 'hidden' | 'raw';

    /**
     * Map of custom environment variables to include in the spawn options.
     */
    env?: Record<string, unknown>;
}): SpawnOptions => {
    const stdioValues: (IOType | 'ipc')[] =
        stdio === 'normal'
            ? ['pipe', 'pipe', 'pipe']
            : stdio === 'raw'
              ? ['inherit', 'inherit', 'inherit']
              : ['pipe', 'ignore', 'ignore'];

    if (ipc != null) {
        // Avoid overriding the stdout/stderr/stdin
        assert.ok(ipc > 2, '[concurrently] the IPC channel number should be > 2');
        stdioValues[ipc] = 'ipc';
    }

    return {
        cwd: cwd || process.cwd(),
        stdio: stdioValues,
        ...(process.platform.startsWith('win') && { detached: false }),
        env: {
            ...(colorSupport ? { FORCE_COLOR: colorSupport.level.toString() } : {}),
            ...process.env,
            ...env,
        },
    };
};

```

## File: lib\utils.spec.ts
```
import { describe, expect, it } from 'vitest';

import { castArray, escapeRegExp } from './utils.js';

describe('#escapeRegExp()', () => {
    it('escapes all RegExp chars', () => {
        // eslint-disable-next-line no-useless-escape
        const result = escapeRegExp('\*?{}.(?<test>.)|[]');

        expect(result).toBe('\\*\\?\\{\\}\\.\\(\\?<test>\\.\\)\\|\\[\\]');
    });
});

describe('#castArray()', () => {
    it('returns empty array for nullish input values', () => {
        const result1 = castArray();
        const result2 = castArray(undefined);
        const result3 = castArray(null);

        expect(result1).toStrictEqual([]);
        expect(result2).toStrictEqual([]);
        expect(result3).toStrictEqual([]);
    });

    it('directly returns value if it is already of type array', () => {
        const value = ['example'];
        const result = castArray(value);

        expect(result).toBe(value);
    });

    describe('casts primitives to an array', () => {
        it.each([1, 'example', {}])('%s', (value) => {
            const result = castArray(value);

            expect(result).toStrictEqual([value]);
        });
    });
});

```

## File: lib\utils.ts
```
/**
 * Escapes a string for use in a regular expression.
 */
export function escapeRegExp(str: string) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

type CastArrayResult<T> = T extends undefined | null ? never[] : T extends unknown[] ? T : T[];

/**
 * Casts a value to an array if it's not one.
 */
export function castArray<T = never[]>(value?: T) {
    return (Array.isArray(value) ? value : value != null ? [value] : []) as CastArrayResult<T>;
}

```

## File: lib\command-parser\command-parser.d.ts
```
import { CommandInfo } from '../command.js';

/**
 * A command parser encapsulates a specific logic for mapping `CommandInfo` objects
 * into another `CommandInfo`.
 *
 * A prime example is turning an abstract `npm:foo` into `npm run foo`, but it could also turn
 * the prefix color of a command brighter, or maybe even prefixing each command with `time(1)`.
 */
export interface CommandParser {
    /**
     * Parses `commandInfo` and returns one or more `CommandInfo`s.
     *
     * Returning multiple `CommandInfo` is used when there are multiple possibilities of commands to
     * run given the original input.
     * An example of this is when the command contains a wildcard and it must be expanded into all
     * viable options so that the consumer can decide which ones to run.
     */
    parse: (commandInfo: CommandInfo) => CommandInfo | CommandInfo[];
}

```

## File: lib\command-parser\expand-arguments.spec.ts
```
import { expect, it } from 'vitest';

import { CommandInfo } from '../command.js';
import { ExpandArguments } from './expand-arguments.js';

const createCommandInfo = (command: string): CommandInfo => ({
    command,
    name: '',
});

it('returns command as is when no placeholders', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo foo');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('single argument placeholder is replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {1}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('argument placeholder is replaced and quoted properly', () => {
    const parser = new ExpandArguments(['foo bar']);
    const commandInfo = createCommandInfo('echo {1}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: "echo 'foo bar'" });
});

it('multiple single argument placeholders are replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {2} {1}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo bar foo' });
});

it('empty replacement with single placeholder and not enough passthrough arguments', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {3}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo ' });
});

it('empty replacement with all placeholder and no passthrough arguments', () => {
    const parser = new ExpandArguments([]);
    const commandInfo = createCommandInfo('echo {@}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo ' });
});

it('empty replacement with combined placeholder and no passthrough arguments', () => {
    const parser = new ExpandArguments([]);
    const commandInfo = createCommandInfo('echo {*}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo ' });
});

it('all arguments placeholder is replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {@}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo bar' });
});

it('combined arguments placeholder is replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    const commandInfo = createCommandInfo('echo {*}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: "echo 'foo bar'" });
});

it('escaped argument placeholders are not replaced', () => {
    const parser = new ExpandArguments(['foo', 'bar']);
    // Equals to single backslash on command line
    const commandInfo = createCommandInfo('echo \\{1} \\{@} \\{*}');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo {1} {@} {*}' });
});

```

## File: lib\command-parser\expand-arguments.ts
```
import { quote } from 'shell-quote';

import { CommandInfo } from '../command.js';
import { CommandParser } from './command-parser.js';

/**
 * Replace placeholders with additional arguments.
 */
export class ExpandArguments implements CommandParser {
    constructor(private readonly additionalArguments: string[]) {}

    parse(commandInfo: CommandInfo) {
        const command = commandInfo.command.replace(
            /\\?\{([@*]|[1-9]\d*)\}/g,
            (match, placeholderTarget: string) => {
                // Don't replace the placeholder if it is escaped by a backslash.
                if (match.startsWith('\\')) {
                    return match.slice(1);
                }

                if (this.additionalArguments.length > 0) {
                    // Replace numeric placeholder if value exists in additional arguments.
                    if (+placeholderTarget <= this.additionalArguments.length) {
                        return quote([this.additionalArguments[+placeholderTarget - 1]]);
                    }

                    // Replace all arguments placeholder.
                    if (placeholderTarget === '@') {
                        return quote(this.additionalArguments);
                    }

                    // Replace combined arguments placeholder.
                    if (placeholderTarget === '*') {
                        return quote([this.additionalArguments.join(' ')]);
                    }
                }

                // Replace placeholder with empty string
                // if value doesn't exist in additional arguments.
                return '';
            },
        );

        return { ...commandInfo, command };
    }
}

```

## File: lib\command-parser\expand-shortcut.spec.ts
```
import { describe, expect, it } from 'vitest';

import { CommandInfo } from '../command.js';
import { ExpandShortcut } from './expand-shortcut.js';

const parser = new ExpandShortcut();

const createCommandInfo = (command: string, name = ''): CommandInfo => ({
    name,
    command,
});

it('returns same command if no prefix is present', () => {
    const commandInfo = createCommandInfo('echo foo');
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

describe.each([
    ['npm', 'npm run'],
    ['yarn', 'yarn run'],
    ['pnpm', 'pnpm run'],
    ['bun', 'bun run'],
    ['node', 'node --run'],
    ['deno', 'deno task'],
])(`with '%s:' prefix`, (prefix, command) => {
    it(`expands to "${command} <script> <args>"`, () => {
        const commandInfo = createCommandInfo(`${prefix}:foo -- bar`, 'echo');
        expect(parser.parse(commandInfo)).toEqual({
            ...commandInfo,
            name: 'echo',
            command: `${command} foo -- bar`,
        });
    });

    it('sets name to script name if none', () => {
        const commandInfo = createCommandInfo(`${prefix}:foo -- bar`);
        expect(parser.parse(commandInfo)).toEqual({
            ...commandInfo,
            name: 'foo',
            command: `${command} foo -- bar`,
        });
    });
});

```

## File: lib\command-parser\expand-shortcut.ts
```
import { CommandInfo } from '../command.js';
import { CommandParser } from './command-parser.js';

/**
 * Expands shortcuts according to the following table:
 *
 * | Syntax          | Expands to            |
 * | --------------- | --------------------- |
 * | `npm:<script>`  | `npm run <script>`    |
 * | `pnpm:<script>` | `pnpm run <script>`   |
 * | `yarn:<script>` | `yarn run <script>`   |
 * | `bun:<script>`  | `bun run <script>`    |
 * | `node:<script>` | `node --run <script>` |
 * | `deno:<script>` | `deno task <script>`  |
 */
export class ExpandShortcut implements CommandParser {
    parse(commandInfo: CommandInfo) {
        const [, prefix, script, args] =
            /^(npm|yarn|pnpm|bun|node|deno):(\S+)(.*)/.exec(commandInfo.command) || [];
        if (!script) {
            return commandInfo;
        }

        let command: string;
        if (prefix === 'node') {
            command = 'node --run';
        } else if (prefix === 'deno') {
            command = 'deno task';
        } else {
            command = `${prefix} run`;
        }

        return {
            ...commandInfo,
            name: commandInfo.name || script,
            command: `${command} ${script}${args}`,
        };
    }
}

```

## File: lib\command-parser\expand-wildcard.spec.ts
```
import fs, { PathOrFileDescriptor } from 'node:fs';

import { afterEach, beforeEach, describe, expect, it, Mock, vi } from 'vitest';

import { CommandInfo } from '../command.js';
import { ExpandWildcard } from './expand-wildcard.js';

let parser: ExpandWildcard;
let readPackage: Mock;
let readDeno: Mock;

const createCommandInfo = (command: string): CommandInfo => ({
    command,
    name: '',
});

beforeEach(() => {
    readDeno = vi.fn();
    readPackage = vi.fn();
    parser = new ExpandWildcard(readDeno, readPackage);
});

afterEach(() => {
    vi.restoreAllMocks();
});

describe('#readDeno()', () => {
    it('can read deno.json', () => {
        const expectedDeno = {
            name: 'deno',
            version: '1.14.0',
        };
        vi.spyOn(fs, 'existsSync').mockImplementation((path: PathOrFileDescriptor) => {
            return path === 'deno.json';
        });
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'deno.json') {
                return JSON.stringify(expectedDeno);
            }
            return '';
        });

        const actualReadDeno = ExpandWildcard.readDeno();
        expect(actualReadDeno).toEqual(expectedDeno);
    });

    it('can read deno.jsonc', () => {
        const expectedDeno = {
            name: 'deno',
            version: '1.14.0',
        };
        vi.spyOn(fs, 'existsSync').mockImplementation((path: PathOrFileDescriptor) => {
            return path === 'deno.jsonc';
        });
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'deno.jsonc') {
                return `/* comment */\n${JSON.stringify(expectedDeno)}`;
            }
            return '';
        });

        const actualReadDeno = ExpandWildcard.readDeno();
        expect(actualReadDeno).toEqual(expectedDeno);
    });

    it('prefers deno.json over deno.jsonc', () => {
        const expectedDeno = {
            name: 'deno',
            version: '1.14.0',
        };
        vi.spyOn(fs, 'existsSync').mockImplementation((path: PathOrFileDescriptor) => {
            return path === 'deno.json' || path === 'deno.jsonc';
        });
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'deno.json') {
                return JSON.stringify(expectedDeno);
            }
            return '';
        });

        const actualReadDeno = ExpandWildcard.readDeno();
        expect(actualReadDeno).toEqual(expectedDeno);
    });

    it('can handle errors reading deno', () => {
        vi.spyOn(fs, 'existsSync').mockReturnValue(true);
        vi.spyOn(fs, 'readFileSync').mockImplementation(() => {
            throw new Error('Error reading deno');
        });

        expect(() => ExpandWildcard.readDeno()).not.toThrow();
        expect(ExpandWildcard.readDeno()).toEqual({});
    });
});

describe('#readPackage()', () => {
    it('can read package', () => {
        const expectedPackage = {
            name: 'concurrently',
            version: '6.4.0',
        };
        vi.spyOn(fs, 'readFileSync').mockImplementation((path: PathOrFileDescriptor) => {
            if (path === 'package.json') {
                return JSON.stringify(expectedPackage);
            }
            return '';
        });

        const actualReadPackage = ExpandWildcard.readPackage();
        expect(actualReadPackage).toEqual(expectedPackage);
    });

    it('can handle errors reading package', () => {
        vi.spyOn(fs, 'readFileSync').mockImplementation(() => {
            throw new Error('Error reading package');
        });

        expect(() => ExpandWildcard.readPackage()).not.toThrow();
        expect(ExpandWildcard.readPackage()).toEqual({});
    });
});

it('returns same command if not an npm run command', () => {
    const commandInfo = createCommandInfo('npm test');

    expect(readDeno).not.toHaveBeenCalled();
    expect(readPackage).not.toHaveBeenCalled();
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

it('returns same command if not a deno task command', () => {
    const commandInfo = createCommandInfo('deno run');

    expect(readDeno).not.toHaveBeenCalled();
    expect(readPackage).not.toHaveBeenCalled();
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

it('returns same command if no wildcard present', () => {
    const commandInfo = createCommandInfo('npm run foo bar');

    expect(readPackage).not.toHaveBeenCalled();
    expect(parser.parse(commandInfo)).toBe(commandInfo);
});

it('expands to nothing if no scripts exist in package.json', () => {
    readPackage.mockReturnValue({});

    expect(parser.parse(createCommandInfo('npm run foo-*-baz qux'))).toEqual([]);
});

it('expands to nothing if no tasks exist in Deno config and no scripts exist in NodeJS config', () => {
    readDeno.mockReturnValue({});
    readPackage.mockReturnValue({});

    expect(parser.parse(createCommandInfo('deno task foo-*-baz qux'))).toEqual([]);
});

describe.each(['npm run', 'yarn run', 'pnpm run', 'bun run', 'node --run'])(
    `with a '%s' prefix`,
    (command) => {
        it('expands to all scripts matching pattern', () => {
            readPackage.mockReturnValue({
                scripts: {
                    'foo-bar-baz': '',
                    'foo--baz': '',
                },
            });

            expect(parser.parse(createCommandInfo(`${command} foo-*-baz qux`))).toEqual([
                { name: 'bar', command: `${command} foo-bar-baz qux` },
                { name: '', command: `${command} foo--baz qux` },
            ]);
        });

        it('uses wildcard match of script as command name', () => {
            readPackage.mockReturnValue({
                scripts: {
                    'watch-js': '',
                    'watch-css': '',
                },
            });

            expect(
                parser.parse({
                    name: 'watch-*',
                    command: `${command} watch-*`,
                }),
            ).toEqual([
                { name: 'js', command: `${command} watch-js` },
                { name: 'css', command: `${command} watch-css` },
            ]);
        });

        it('uses existing command name as prefix to the wildcard match', () => {
            readPackage.mockReturnValue({
                scripts: {
                    'watch-js': '',
                    'watch-css': '',
                },
            });

            expect(
                parser.parse({
                    name: 'w:',
                    command: `${command} watch-*`,
                }),
            ).toEqual([
                { name: 'w:js', command: `${command} watch-js` },
                { name: 'w:css', command: `${command} watch-css` },
            ]);
        });

        it('allows negation', () => {
            readPackage.mockReturnValue({
                scripts: {
                    'lint:js': '',
                    'lint:ts': '',
                    'lint:fix:js': '',
                    'lint:fix:ts': '',
                },
            });

            expect(parser.parse(createCommandInfo(`${command} lint:*(!fix)`))).toEqual([
                { name: 'js', command: `${command} lint:js` },
                { name: 'ts', command: `${command} lint:ts` },
            ]);
        });

        it('caches scripts upon calls', () => {
            readPackage.mockReturnValue({});

            parser.parse(createCommandInfo(`${command} foo-*-baz qux`));
            parser.parse(createCommandInfo(`${command} foo-*-baz qux`));

            expect(readPackage).toHaveBeenCalledTimes(1);
        });

        it("doesn't read Deno config", () => {
            readPackage.mockReturnValue({});

            parser.parse(createCommandInfo(`${command} foo-*-baz qux`));

            expect(readDeno).not.toHaveBeenCalled();
        });
    },
);

describe(`with a 'deno task' prefix`, () => {
    it('expands to all scripts matching pattern', () => {
        readDeno.mockReturnValue({
            tasks: {
                'foo-bar-baz': '',
                'foo--baz': '',
            },
        });
        readPackage.mockReturnValue({
            scripts: {
                'foo-foo-baz': '',
            },
        });

        expect(parser.parse(createCommandInfo(`deno task foo-*-baz qux`))).toEqual([
            { name: 'bar', command: `deno task foo-bar-baz qux` },
            { name: '', command: `deno task foo--baz qux` },
            { name: 'foo', command: `deno task foo-foo-baz qux` },
        ]);
    });

    it('uses wildcard match of script as command name', () => {
        readDeno.mockReturnValue({
            tasks: {
                'watch-sass': '',
            },
        });
        readPackage.mockReturnValue({
            scripts: {
                'watch-js': '',
                'watch-css': '',
            },
        });

        expect(
            parser.parse({
                name: '',
                command: `deno task watch-*`,
            }),
        ).toEqual([
            { name: 'sass', command: `deno task watch-sass` },
            { name: 'js', command: `deno task watch-js` },
            { name: 'css', command: `deno task watch-css` },
        ]);
    });

    it('uses existing command name as prefix to the wildcard match', () => {
        readDeno.mockReturnValue({
            tasks: {
                'watch-sass': '',
            },
        });
        readPackage.mockReturnValue({
            scripts: {
                'watch-js': '',
                'watch-css': '',
            },
        });

        expect(
            parser.parse({
                name: 'w:',
                command: `deno task watch-*`,
            }),
        ).toEqual([
            { name: 'w:sass', command: `deno task watch-sass` },
            { name: 'w:js', command: `deno task watch-js` },
            { name: 'w:css', command: `deno task watch-css` },
        ]);
    });

    it('allows negation', () => {
        readDeno.mockReturnValue({
            tasks: {
                'lint:sass': '',
                'lint:fix:sass': '',
            },
        });
        readPackage.mockReturnValue({
            scripts: {
                'lint:js': '',
                'lint:ts': '',
                'lint:fix:js': '',
                'lint:fix:ts': '',
            },
        });

        expect(parser.parse(createCommandInfo(`deno task lint:*(!fix)`))).toEqual([
            { name: 'sass', command: `deno task lint:sass` },
            { name: 'js', command: `deno task lint:js` },
            { name: 'ts', command: `deno task lint:ts` },
        ]);
    });

    it('caches scripts upon calls', () => {
        readDeno.mockReturnValue({});
        readPackage.mockReturnValue({});

        parser.parse(createCommandInfo(`deno task foo-*-baz qux`));
        parser.parse(createCommandInfo(`deno task foo-*-baz qux`));

        expect(readDeno).toHaveBeenCalledTimes(1);
        expect(readPackage).toHaveBeenCalledTimes(1);
    });
});

```

## File: lib\command-parser\expand-wildcard.ts
```
import fs from 'node:fs';

import { CommandInfo } from '../command.js';
import JSONC from '../jsonc.js';
import { escapeRegExp } from '../utils.js';
import { CommandParser } from './command-parser.js';

// Matches a negative filter surrounded by '(!' and ')'.
const OMISSION = /\(!([^)]+)\)/;

/**
 * Finds wildcards in 'npm/yarn/pnpm/bun run', 'node --run' and 'deno task'
 * commands and replaces them with all matching scripts in the NodeJS and Deno
 * configuration files of the current directory.
 */
export class ExpandWildcard implements CommandParser {
    static readDeno() {
        try {
            let json: string = '{}';

            if (fs.existsSync('deno.json')) {
                json = fs.readFileSync('deno.json', { encoding: 'utf-8' });
            } else if (fs.existsSync('deno.jsonc')) {
                json = fs.readFileSync('deno.jsonc', { encoding: 'utf-8' });
            }

            return JSONC.parse(json);
        } catch {
            return {};
        }
    }

    static readPackage() {
        try {
            const json = fs.readFileSync('package.json', { encoding: 'utf-8' });
            return JSON.parse(json);
        } catch {
            return {};
        }
    }

    private packageScripts?: string[];
    private denoTasks?: string[];

    constructor(
        private readonly readDeno = ExpandWildcard.readDeno,
        private readonly readPackage = ExpandWildcard.readPackage,
    ) {}

    private relevantScripts(command: string): string[] {
        if (!this.packageScripts) {
            this.packageScripts = Object.keys(this.readPackage().scripts || {});
        }

        if (command === 'deno task') {
            if (!this.denoTasks) {
                // If Deno tries to run a task that doesn't exist,
                // it can fall back to running a script with the same name.
                // Therefore, the actual list of tasks is the union of the tasks and scripts.
                this.denoTasks = [
                    ...Object.keys(this.readDeno().tasks || {}),
                    ...this.packageScripts,
                ];
            }

            return this.denoTasks;
        }

        return this.packageScripts;
    }

    parse(commandInfo: CommandInfo) {
        // We expect one of the following patterns:
        // - <npm|yarn|pnpm|bun> run <script> [args]
        // - node --run <script> [args]
        // - deno task <script> [args]
        const [, command, scriptGlob, args] =
            /((?:npm|yarn|pnpm|bun) run|node --run|deno task) (\S+)([^&]*)/.exec(
                commandInfo.command,
            ) || [];

        const wildcardPosition = (scriptGlob || '').indexOf('*');

        // If the regex didn't match an npm script, or it has no wildcard,
        // then we have nothing to do here
        if (wildcardPosition === -1) {
            return commandInfo;
        }

        const [, omission] = OMISSION.exec(scriptGlob) || [];
        const scriptGlobSansOmission = scriptGlob.replace(OMISSION, '');
        const preWildcard = escapeRegExp(scriptGlobSansOmission.slice(0, wildcardPosition));
        const postWildcard = escapeRegExp(scriptGlobSansOmission.slice(wildcardPosition + 1));
        const wildcardRegex = new RegExp(`^${preWildcard}(.*?)${postWildcard}$`);
        // If 'commandInfo.name' doesn't match 'scriptGlob', this means a custom name
        // has been specified and thus becomes the prefix (as described in the README).
        const prefix = commandInfo.name !== scriptGlob ? commandInfo.name : '';

        const commands: CommandInfo[] = [];

        for (const script of this.relevantScripts(command)) {
            if (omission && new RegExp(omission).test(script)) {
                continue;
            }

            const result = wildcardRegex.exec(script);
            const match = result?.[1];
            if (match !== undefined) {
                commands.push({
                    ...commandInfo,
                    command: `${command} ${script}${args}`,
                    // Will use an empty command name if no prefix has been specified and
                    // the wildcard match is empty, e.g. if `npm:watch-*` matches `npm run watch-`.
                    name: prefix + match,
                });
            }
        }

        return commands;
    }
}

```

## File: lib\command-parser\strip-quotes.spec.ts
```
import { expect, it } from 'vitest';

import { CommandInfo } from '../command.js';
import { StripQuotes } from './strip-quotes.js';

const parser = new StripQuotes();

const createCommandInfo = (command: string): CommandInfo => ({
    command,
    name: '',
});

it('returns command as is if no single/double quote at the beginning', () => {
    const commandInfo = createCommandInfo('echo foo');
    expect(parser.parse(commandInfo)).toEqual(commandInfo);
});

it('strips single quotes', () => {
    const commandInfo = createCommandInfo("'echo foo'");
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('strips double quotes', () => {
    const commandInfo = createCommandInfo('"echo foo"');
    expect(parser.parse(commandInfo)).toEqual({ ...commandInfo, command: 'echo foo' });
});

it('does not remove quotes if they are unbalanced', () => {
    let commandInfo = createCommandInfo('"echo foo');
    expect(parser.parse(commandInfo)).toEqual(commandInfo);

    commandInfo = createCommandInfo("echo foo'");
    expect(parser.parse(commandInfo)).toEqual(commandInfo);

    commandInfo = createCommandInfo('"echo foo\'');
    expect(parser.parse(commandInfo)).toEqual(commandInfo);
});

```

## File: lib\command-parser\strip-quotes.ts
```
import { CommandInfo } from '../command.js';
import { CommandParser } from './command-parser.js';

/**
 * Strips quotes around commands so that they can run on the current shell.
 */
export class StripQuotes implements CommandParser {
    parse(commandInfo: CommandInfo) {
        let { command } = commandInfo;

        // Removes the quotes surrounding a command.
        if (/^".+?"$/.test(command) || /^'.+?'$/.test(command)) {
            command = command.slice(1, command.length - 1);
        }

        return { ...commandInfo, command };
    }
}

```

## File: lib\declarations\intl.d.ts
```
// TODO: Delete this file once Typescript has added these.
declare namespace Intl {
    // https://github.com/tc39/ecma402/pull/351
    interface DateTimeFormatPartTypesRegistry {
        yearName?: string;
        relatedYear?: string;
    }

    /**
     * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/getWeekInfo
     */
    interface WeekInfo {
        firstDay: number;
        weekend: readonly number[];
        minimalDays: number;
    }

    interface Locale {
        readonly weekInfo: WeekInfo;
        getWeekInfo?: () => WeekInfo;
    }
}

```

## File: lib\flow-control\flow-controller.d.ts
```
import { Command } from '../command.js';

/**
 * Interface for a class that controls and/or watches the behavior of commands.
 *
 * This may include logging their output, creating interactions between them, or changing when they
 * actually finish.
 */
export interface FlowController {
    handle: (commands: Command[]) => { commands: Command[]; onFinish?: () => void | Promise<void> };
}

```

## File: lib\flow-control\input-handler.spec.ts
```
import { Buffer } from 'node:buffer';
import { PassThrough } from 'node:stream';

import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { InputHandler } from './input-handler.js';

let commands: Command[];
let controller: InputHandler;
let inputStream: PassThrough;
let logger: Logger;

beforeEach(() => {
    commands = [new FakeCommand('foo', 'echo foo', 0), new FakeCommand('bar', 'echo bar', 1)];
    inputStream = new PassThrough();
    logger = createMockInstance(Logger);
    controller = new InputHandler({
        defaultInputTarget: 0,
        inputStream,
        logger,
    });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });

    controller = new InputHandler({ logger, inputStream });
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('does nothing if called without input stream', () => {
    new InputHandler({
        defaultInputTarget: 0,
        inputStream: undefined,
        logger,
    }).handle(commands);
    inputStream.write('something');

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
});

it('forwards input stream to default target ID', () => {
    controller.handle(commands);

    inputStream.write('something');

    expect(commands[0].stdin?.write).toHaveBeenCalledExactlyOnceWith('something');
    expect(commands[1].stdin?.write).not.toHaveBeenCalled();
});

it('forwards input stream to target index specified in input', () => {
    controller.handle(commands);

    inputStream.write('1:something');
    inputStream.write('1:multi\nline\n');

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
    expect(commands[1].stdin?.write).toHaveBeenCalledTimes(2);
    expect(commands[1].stdin?.write).toHaveBeenCalledWith('something');
    expect(commands[1].stdin?.write).toHaveBeenCalledWith('multi\nline\n');
});

it('forwards input stream to target index specified in input when input contains colon', () => {
    controller.handle(commands);

    inputStream.emit('data', Buffer.from('1:some:thing'));
    inputStream.emit('data', Buffer.from('1: :something'));
    inputStream.emit('data', Buffer.from('1::something'));

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
    expect(commands[1].stdin?.write).toHaveBeenCalledTimes(3);
    expect(commands[1].stdin?.write).toHaveBeenCalledWith('some:thing');
    expect(commands[1].stdin?.write).toHaveBeenCalledWith(' :something');
    expect(commands[1].stdin?.write).toHaveBeenCalledWith(':something');
});

it('does not forward input stream when input contains colon in a different format', () => {
    controller.handle(commands);

    inputStream.emit('data', Buffer.from('Ruby0::Const::Syntax'));
    inputStream.emit('data', Buffer.from('1:Ruby1::Const::Syntax'));
    inputStream.emit('data', Buffer.from('ruby_symbol_arg :my_symbol'));
    inputStream.emit('data', Buffer.from('ruby_symbol_arg(:my_symbol)'));
    inputStream.emit('data', Buffer.from('{ruby_key: :my_val}'));
    inputStream.emit('data', Buffer.from('{:ruby_key=>:my_val}'));
    inputStream.emit('data', Buffer.from('js_obj = {key: "my_val"}'));

    expect(commands[1].stdin?.write).toHaveBeenCalledExactlyOnceWith('Ruby1::Const::Syntax');
    expect(commands[0].stdin?.write).toHaveBeenCalledTimes(6);
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('Ruby0::Const::Syntax');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('ruby_symbol_arg :my_symbol');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('ruby_symbol_arg(:my_symbol)');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('{ruby_key: :my_val}');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('{:ruby_key=>:my_val}');
    expect(commands[0].stdin?.write).toHaveBeenCalledWith('js_obj = {key: "my_val"}');
});

it('forwards input stream to target name specified in input', () => {
    controller.handle(commands);

    inputStream.write('bar:something');

    expect(commands[0].stdin?.write).not.toHaveBeenCalled();
    expect(commands[1].stdin?.write).toHaveBeenCalledExactlyOnceWith('something');
});

it('logs error if command has no stdin open', () => {
    commands[0].stdin = undefined;
    controller.handle(commands);

    inputStream.write('something');

    expect(commands[1].stdin?.write).not.toHaveBeenCalled();
    expect(logger.logGlobalEvent).toHaveBeenCalledWith(
        'Unable to find command "0", or it has no stdin open\n',
    );
});

it('fallback to default input stream if command is not found', () => {
    controller.handle(commands);

    inputStream.write('foobar:something');

    expect(commands[0].stdin?.write).toHaveBeenCalledExactlyOnceWith('foobar:something');
    expect(commands[1].stdin?.write).not.toHaveBeenCalled();
    expect(logger.logGlobalEvent).not.toHaveBeenCalled();
});

it('pauses input stream when finished', () => {
    expect(inputStream.readableFlowing).toBeNull();

    const { onFinish } = controller.handle(commands);
    expect(inputStream.readableFlowing).toBe(true);

    expect(onFinish).toBeDefined();
    onFinish?.();
    expect(inputStream.readableFlowing).toBe(false);
});

it('does not pause input stream when pauseInputStreamOnFinish is set to false', () => {
    controller = new InputHandler({ logger, inputStream, pauseInputStreamOnFinish: false });

    expect(inputStream.readableFlowing).toBeNull();

    const { onFinish } = controller.handle(commands);
    expect(inputStream.readableFlowing).toBe(true);

    expect(onFinish).toBeDefined();
    onFinish?.();
    expect(inputStream.readableFlowing).toBe(true);
});

```

## File: lib\flow-control\input-handler.ts
```
import { Readable } from 'node:stream';

import Rx from 'rxjs';
import { map } from 'rxjs/operators';

import { Command, CommandIdentifier } from '../command.js';
import * as defaults from '../defaults.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Sends input from concurrently through to commands.
 *
 * Input can start with a command identifier, in which case it will be sent to that specific command.
 * For instance, `0:bla` will send `bla` to command at index `0`, and `server:stop` will send `stop`
 * to command with name `server`.
 *
 * If the input doesn't start with a command identifier, it is then always sent to the default target.
 */
export class InputHandler implements FlowController {
    private readonly logger: Logger;
    private readonly defaultInputTarget: CommandIdentifier;
    private readonly inputStream?: Readable;
    private readonly pauseInputStreamOnFinish: boolean;

    constructor({
        defaultInputTarget,
        inputStream,
        pauseInputStreamOnFinish,
        logger,
    }: {
        inputStream?: Readable;
        logger: Logger;
        defaultInputTarget?: CommandIdentifier;
        pauseInputStreamOnFinish?: boolean;
    }) {
        this.logger = logger;
        this.defaultInputTarget = defaultInputTarget || defaults.defaultInputTarget;
        this.inputStream = inputStream;
        this.pauseInputStreamOnFinish = pauseInputStreamOnFinish !== false;
    }

    handle(commands: Command[]): {
        commands: Command[];
        onFinish?: () => void | undefined;
    } {
        const { inputStream } = this;
        if (!inputStream) {
            return { commands };
        }

        const commandsMap = new Map<string, Command>();
        for (const command of commands) {
            commandsMap.set(command.index.toString(), command);
            commandsMap.set(command.name, command);
        }

        Rx.fromEvent(inputStream, 'data')
            .pipe(map((data) => String(data)))
            .subscribe((data) => {
                const dataParts = data.split(/:(.+)/s);
                let target = dataParts[0];
                let command = commandsMap.get(target);
                let input: string;

                if (dataParts.length > 1 && command) {
                    input = dataParts[1];
                } else {
                    // If `target` does not match a registered command,
                    // fallback to `defaultInputTarget` and forward the whole input data
                    target = this.defaultInputTarget.toString();
                    command = commandsMap.get(target);
                    input = data;
                }

                if (command?.stdin) {
                    command.stdin.write(input);
                } else {
                    this.logger.logGlobalEvent(
                        `Unable to find command "${target}", or it has no stdin open\n`,
                    );
                }
            });

        return {
            commands,
            onFinish: () => {
                if (this.pauseInputStreamOnFinish) {
                    // https://github.com/kimmobrunfeldt/concurrently/issues/252
                    inputStream.pause();
                }
            },
        };
    }
}

```

## File: lib\flow-control\kill-on-signal.spec.ts
```
import { EventEmitter } from 'node:events';

import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { Command } from '../command.js';
import { KillOnSignal } from './kill-on-signal.js';

let commands: Command[];
let controller: KillOnSignal;
let process: EventEmitter;
let abortController: AbortController;
beforeEach(() => {
    process = new EventEmitter();
    commands = [new FakeCommand(), new FakeCommand()];
    abortController = new AbortController();
    controller = new KillOnSignal({ process, abortController });
});

it('returns commands that keep non-close streams from original commands', () => {
    const { commands: newCommands } = controller.handle(commands);
    newCommands.forEach((newCommand, i) => {
        expect(newCommand.close).not.toBe(commands[i].close);
        expect(newCommand.error).toBe(commands[i].error);
        expect(newCommand.stdout).toBe(commands[i].stdout);
        expect(newCommand.stderr).toBe(commands[i].stderr);
    });
});

it('returns commands that map SIGINT to exit code 0', () => {
    const { commands: newCommands } = controller.handle(commands);
    expect(newCommands).not.toBe(commands);
    expect(newCommands).toHaveLength(commands.length);

    const callback = vi.fn();
    newCommands[0].close.subscribe(callback);
    process.emit('SIGINT', 'SIGINT');

    // A fake command's .kill() call won't trigger a close event automatically...
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    expect(callback).not.toHaveBeenCalledWith(expect.objectContaining({ exitCode: 'SIGINT' }));
    expect(callback).toHaveBeenCalledWith(expect.objectContaining({ exitCode: 0 }));
});

it('returns commands that keep non-SIGINT exit codes', () => {
    const { commands: newCommands } = controller.handle(commands);
    expect(newCommands).not.toBe(commands);
    expect(newCommands).toHaveLength(commands.length);

    const callback = vi.fn();
    newCommands[0].close.subscribe(callback);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    expect(callback).toHaveBeenCalledWith(expect.objectContaining({ exitCode: 1 }));
});

describe.each(['SIGINT', 'SIGTERM', 'SIGHUP'])('on %s', (signal) => {
    it('kills all commands', () => {
        controller.handle(commands);
        process.emit(signal, signal);

        expect(process.listenerCount(signal)).toBe(1);
        expect(commands[0].kill).toHaveBeenCalledWith(signal);
        expect(commands[1].kill).toHaveBeenCalledWith(signal);
    });

    it('sends abort signal', () => {
        controller.handle(commands);
        process.emit(signal, signal);

        expect(abortController.signal.aborted).toBe(true);
    });

    it('removes event listener on finish', () => {
        const { onFinish } = controller.handle(commands);
        onFinish();
        expect(process.listenerCount(signal)).toBe(0);
    });
});

```

## File: lib\flow-control\kill-on-signal.ts
```
import EventEmitter from 'node:events';

import { map } from 'rxjs/operators';

import { Command } from '../command.js';
import { FlowController } from './flow-controller.js';

const SIGNALS = ['SIGINT', 'SIGTERM', 'SIGHUP'] as const;

/**
 * Watches the main concurrently process for signals and sends the same signal down to each spawned
 * command.
 */
export class KillOnSignal implements FlowController {
    private readonly process: EventEmitter;
    private readonly abortController?: AbortController;

    constructor({
        process,
        abortController,
    }: {
        process: EventEmitter;
        abortController?: AbortController;
    }) {
        this.process = process;
        this.abortController = abortController;
    }

    handle(commands: Command[]) {
        let caughtSignal: NodeJS.Signals;
        const signalListener = (signal: NodeJS.Signals) => {
            caughtSignal = signal;
            this.abortController?.abort();
            commands.forEach((command) => command.kill(signal));
        };
        SIGNALS.forEach((signal) => this.process.on(signal, signalListener));

        return {
            commands: commands.map((command) => {
                const closeStream = command.close.pipe(
                    map((exitInfo) => {
                        const exitCode = caughtSignal === 'SIGINT' ? 0 : exitInfo.exitCode;
                        return { ...exitInfo, exitCode };
                    }),
                );
                // Return a proxy so that mutations happen on the original Command object.
                // If either `Object.assign()` or `Object.create()` were used, it'd be hard to
                // reflect the mutations on Command objects referenced by previous flow controllers.
                return new Proxy(command, {
                    get(target, prop: keyof Command) {
                        return prop === 'close' ? closeStream : target[prop];
                    },
                });
            }),
            onFinish: () => {
                // Avoids MaxListenersExceededWarning when running programmatically
                SIGNALS.forEach((signal) => this.process.off(signal, signalListener));
            },
        };
    }
}

```

## File: lib\flow-control\kill-others.spec.ts
```
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import {
    createFakeCloseEvent,
    createFakeProcess,
    FakeCommand,
} from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { KillOthers, ProcessCloseCondition } from './kill-others.js';

let commands: FakeCommand[];
let logger: Logger;
let abortController: AbortController;
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];
    logger = createMockInstance(Logger);
    abortController = new AbortController();
});

const createWithConditions = (
    conditions: ProcessCloseCondition[],
    opts?: { timeoutMs?: number; killSignal?: string },
) =>
    new KillOthers({
        logger,
        abortController,
        conditions,
        killSignal: undefined,
        ...opts,
    });

const assignProcess = (command: FakeCommand) => {
    const process = createFakeProcess(1);
    command.pid = process.pid;
    command.process = process;
};

const unassignProcess = (command: FakeCommand) => {
    command.pid = undefined;
    command.process = undefined;
};

it('returns same commands', () => {
    expect(createWithConditions(['success']).handle(commands)).toMatchObject({ commands });
    expect(createWithConditions(['failure']).handle(commands)).toMatchObject({ commands });
});

it('does not kill others if condition does not match', () => {
    createWithConditions(['failure']).handle(commands);
    assignProcess(commands[1]);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));

    expect(logger.logGlobalEvent).not.toHaveBeenCalled();
    expect(commands[0].kill).not.toHaveBeenCalled();
    expect(commands[1].kill).not.toHaveBeenCalled();
});

describe.each(['success', 'failure'] as const)('on %s', (condition) => {
    const exitCode = condition === 'success' ? 0 : 1;
    const inversedCode = exitCode === 1 ? 0 : 1;

    it('kills other processes', () => {
        createWithConditions([condition]).handle(commands);
        assignProcess(commands[1]);
        commands[0].close.next(createFakeCloseEvent({ exitCode }));

        expect(logger.logGlobalEvent).toHaveBeenCalledExactlyOnceWith(
            'Sending SIGTERM to other processes..',
        );
        expect(commands[0].kill).not.toHaveBeenCalled();
        expect(commands[1].kill).toHaveBeenCalledWith(undefined);
    });

    it('kills other processes, with specified signal', () => {
        createWithConditions([condition], { killSignal: 'SIGKILL' }).handle(commands);
        assignProcess(commands[1]);
        commands[0].close.next(createFakeCloseEvent({ exitCode }));

        expect(logger.logGlobalEvent).toHaveBeenCalledExactlyOnceWith(
            'Sending SIGKILL to other processes..',
        );
        expect(commands[0].kill).not.toHaveBeenCalled();
        expect(commands[1].kill).toHaveBeenCalledWith('SIGKILL');
    });

    it('sends abort signal on condition match', () => {
        createWithConditions([condition]).handle(commands);
        commands[0].close.next(createFakeCloseEvent({ exitCode }));

        expect(abortController.signal.aborted).toBe(true);
    });

    it('does not send abort signal on condition mismatch', () => {
        createWithConditions([condition]).handle(commands);
        commands[0].close.next(createFakeCloseEvent({ exitCode: inversedCode }));

        expect(abortController.signal.aborted).toBe(false);
    });
});

it('does nothing if called without conditions', () => {
    createWithConditions([]).handle(commands);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));

    expect(logger.logGlobalEvent).not.toHaveBeenCalled();
    expect(commands[0].kill).not.toHaveBeenCalled();
    expect(commands[1].kill).not.toHaveBeenCalled();
});

it('does not try to kill processes already dead', () => {
    createWithConditions(['failure']).handle(commands);
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    expect(logger.logGlobalEvent).not.toHaveBeenCalled();
    expect(commands[0].kill).not.toHaveBeenCalled();
    expect(commands[1].kill).not.toHaveBeenCalled();
});

it('force kills misbehaving processes after a timeout', () => {
    vi.useFakeTimers();
    commands.push(new FakeCommand());

    createWithConditions(['failure'], { timeoutMs: 500 }).handle(commands);
    assignProcess(commands[1]);
    assignProcess(commands[2]);
    commands[2].kill = vi.fn(() => unassignProcess(commands[2]));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));

    vi.advanceTimersByTime(500);

    expect(commands[1].kill).toHaveBeenCalledTimes(2);
    expect(commands[1].kill).toHaveBeenCalledWith('SIGKILL');
    expect(commands[2].kill).toHaveBeenCalledTimes(1);
});

```

## File: lib\flow-control\kill-others.ts
```
import { filter, map } from 'rxjs/operators';

import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { castArray } from '../utils.js';
import { FlowController } from './flow-controller.js';

export type ProcessCloseCondition = 'failure' | 'success';

/**
 * Sends a SIGTERM signal to all commands when one of the commands exits with a matching condition.
 */
export class KillOthers implements FlowController {
    private readonly logger: Logger;
    private readonly abortController?: AbortController;
    private readonly conditions: ProcessCloseCondition[];
    private readonly killSignal: string | undefined;
    private readonly timeoutMs?: number;

    constructor({
        logger,
        abortController,
        conditions,
        killSignal,
        timeoutMs,
    }: {
        logger: Logger;
        abortController?: AbortController;
        conditions: ProcessCloseCondition | ProcessCloseCondition[];
        killSignal: string | undefined;
        timeoutMs?: number;
    }) {
        this.logger = logger;
        this.abortController = abortController;
        this.conditions = castArray(conditions);
        this.killSignal = killSignal;
        this.timeoutMs = timeoutMs;
    }

    handle(commands: Command[]) {
        const conditions = this.conditions.filter(
            (condition) => condition === 'failure' || condition === 'success',
        );

        if (!conditions.length) {
            return { commands };
        }

        const closeStates = commands.map((command) =>
            command.close.pipe(
                map(({ exitCode }) =>
                    exitCode === 0 ? ('success' as const) : ('failure' as const),
                ),
                filter((state) => conditions.includes(state)),
            ),
        );

        closeStates.forEach((closeState) =>
            closeState.subscribe(() => {
                this.abortController?.abort();

                const killableCommands = commands.filter((command) => Command.canKill(command));
                if (killableCommands.length) {
                    this.logger.logGlobalEvent(
                        `Sending ${this.killSignal || 'SIGTERM'} to other processes..`,
                    );
                    killableCommands.forEach((command) => command.kill(this.killSignal));
                    this.maybeForceKill(killableCommands);
                }
            }),
        );

        return { commands };
    }

    private maybeForceKill(commands: Command[]) {
        // No need to force kill when the signal already is SIGKILL.
        if (!this.timeoutMs || this.killSignal === 'SIGKILL') {
            return;
        }

        setTimeout(() => {
            const killableCommands = commands.filter((command) => Command.canKill(command));
            if (killableCommands) {
                this.logger.logGlobalEvent(
                    `Sending SIGKILL to ${killableCommands.length} processes..`,
                );
                killableCommands.forEach((command) => command.kill('SIGKILL'));
            }
        }, this.timeoutMs);
    }
}

```

## File: lib\flow-control\log-error.spec.ts
```
import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LogError } from './log-error.js';

let controller: LogError;
let logger: Logger;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand(), new FakeCommand()];

    logger = createMockInstance(Logger);
    controller = new LogError({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('logs the error event of each command', () => {
    controller.handle(commands);
    commands[0].error.next('error from command 0');

    const error1 = new Error('test');
    commands[1].error.next(error1);

    // Testing Error without stack
    const error2 = new Error('test');
    error2.stack = '';
    commands[2].error.next(error2);

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(6);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `Error occurred when executing command: ${commands[0].command}`,
        commands[0],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith('error from command 0', commands[0]);

    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `Error occurred when executing command: ${commands[1].command}`,
        commands[1],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(error1.stack, commands[1]);

    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `Error occurred when executing command: ${commands[2].command}`,
        commands[2],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(String(error2), commands[2]);
});

```

## File: lib\flow-control\log-error.ts
```
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Logs when commands failed executing, e.g. due to the executable not existing in the system.
 */
export class LogError implements FlowController {
    private readonly logger: Logger;

    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]) {
        commands.forEach((command) =>
            command.error.subscribe((event) => {
                this.logger.logCommandEvent(
                    `Error occurred when executing command: ${command.command}`,
                    command,
                );

                const errorText = String(event instanceof Error ? event.stack || event : event);
                this.logger.logCommandEvent(errorText, command);
            }),
        );

        return { commands };
    }
}

```

## File: lib\flow-control\log-exit.spec.ts
```
import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LogExit } from './log-exit.js';

let controller: LogExit;
let logger: Logger;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];

    logger = createMockInstance(Logger);
    controller = new LogExit({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('logs the close event of each command', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 'SIGTERM' }));

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(2);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} exited with code 0`,
        commands[0],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[1].command} exited with code SIGTERM`,
        commands[1],
    );
});

```

## File: lib\flow-control\log-exit.ts
```
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Logs the exit code/signal of commands.
 */
export class LogExit implements FlowController {
    private readonly logger: Logger;

    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]) {
        commands.forEach((command) =>
            command.close.subscribe(({ exitCode }) => {
                this.logger.logCommandEvent(
                    `${command.command} exited with code ${exitCode}`,
                    command,
                );
            }),
        );

        return { commands };
    }
}

```

## File: lib\flow-control\log-output.spec.ts
```
import { Buffer } from 'node:buffer';

import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LogOutput } from './log-output.js';

let controller: LogOutput;
let logger: Logger;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];

    logger = createMockInstance(Logger);
    controller = new LogOutput({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('logs the stdout of each command', () => {
    controller.handle(commands);

    commands[0].stdout.next(Buffer.from('foo'));
    commands[1].stdout.next(Buffer.from('bar'));

    expect(logger.logCommandText).toHaveBeenCalledTimes(2);
    expect(logger.logCommandText).toHaveBeenCalledWith('foo', commands[0]);
    expect(logger.logCommandText).toHaveBeenCalledWith('bar', commands[1]);
});

it('logs the stderr of each command', () => {
    controller.handle(commands);

    commands[0].stderr.next(Buffer.from('foo'));
    commands[1].stderr.next(Buffer.from('bar'));

    expect(logger.logCommandText).toHaveBeenCalledTimes(2);
    expect(logger.logCommandText).toHaveBeenCalledWith('foo', commands[0]);
    expect(logger.logCommandText).toHaveBeenCalledWith('bar', commands[1]);
});

```

## File: lib\flow-control\log-output.ts
```
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

/**
 * Logs the stdout and stderr output of commands.
 */
export class LogOutput implements FlowController {
    private readonly logger: Logger;
    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]) {
        commands.forEach((command) => {
            command.stdout.subscribe((text) =>
                this.logger.logCommandText(text.toString(), command),
            );
            command.stderr.subscribe((text) =>
                this.logger.logCommandText(text.toString(), command),
            );
        });

        return { commands };
    }
}

```

## File: lib\flow-control\log-timings.spec.ts
```
import { beforeEach, expect, it } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { CloseEvent } from '../command.js';
import { DateFormatter } from '../date-format.js';
import { Logger } from '../logger.js';
import { LogTimings } from './log-timings.js';

// shown in timing order
const startDate0 = new Date();
const startDate1 = new Date(startDate0.getTime() + 1000);
const endDate1 = new Date(startDate0.getTime() + 5000);
const endDate0 = new Date(startDate0.getTime() + 3000);

const timestampFormat = 'yyyy-MM-dd HH:mm:ss.SSS';
const getDurationText = (startDate: Date, endDate: Date) =>
    `${(endDate.getTime() - startDate.getTime()).toLocaleString()}ms`;
const command0DurationTextMs = getDurationText(startDate0, endDate0);
const command1DurationTextMs = getDurationText(startDate1, endDate1);

let controller: LogTimings;
let logger: Logger;
let commands: FakeCommand[];
let command0ExitInfo: CloseEvent;
let command1ExitInfo: CloseEvent;

beforeEach(() => {
    commands = [new FakeCommand('foo', 'command 1', 0), new FakeCommand('bar', 'command 2', 1)];

    command0ExitInfo = createFakeCloseEvent({
        command: commands[0],
        timings: {
            startDate: startDate0,
            endDate: endDate0,
            durationSeconds: endDate0.getTime() - startDate0.getTime(),
        },
        index: commands[0].index,
    });

    command1ExitInfo = createFakeCloseEvent({
        command: commands[1],
        timings: {
            startDate: startDate1,
            endDate: endDate1,
            durationSeconds: endDate1.getTime() - startDate1.getTime(),
        },
        index: commands[1].index,
    });

    logger = createMockInstance(Logger);
    controller = new LogTimings({ logger, timestampFormat });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it("does not log timings and doesn't throw if no logger is provided", () => {
    controller = new LogTimings({});
    const { onFinish } = controller.handle(commands);

    commands[0].timer.next({ startDate: startDate0 });
    commands[1].timer.next({ startDate: startDate1 });
    commands[1].timer.next({ startDate: startDate1, endDate: endDate1 });
    commands[0].timer.next({ startDate: startDate0, endDate: endDate0 });

    onFinish?.();

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(0);
});

it('logs the timings at the start and end (ie complete or error) event of each command', () => {
    const formatter = new DateFormatter(timestampFormat);
    controller.handle(commands);

    commands[0].timer.next({ startDate: startDate0 });
    commands[1].timer.next({ startDate: startDate1 });
    commands[1].timer.next({ startDate: startDate1, endDate: endDate1 });
    commands[0].timer.next({ startDate: startDate0, endDate: endDate0 });

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(4);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} started at ${formatter.format(startDate0)}`,
        commands[0],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[1].command} started at ${formatter.format(startDate1)}`,
        commands[1],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[1].command} stopped at ${formatter.format(
            endDate1,
        )} after ${command1DurationTextMs}`,
        commands[1],
    );
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} stopped at ${formatter.format(
            endDate0,
        )} after ${command0DurationTextMs}`,
        commands[0],
    );
});

it('does not log timings summary if there was an error', () => {
    const { onFinish } = controller.handle(commands);

    commands[0].close.next(command0ExitInfo);
    commands[1].error.next(undefined);

    onFinish?.();

    expect(logger.logTable).toHaveBeenCalledTimes(0);
});

it('logs the sorted timings summary when all processes close successfully after onFinish is called', () => {
    const { onFinish } = controller.handle(commands);

    commands[0].close.next(command0ExitInfo);
    commands[1].close.next(command1ExitInfo);

    expect(logger.logGlobalEvent).toHaveBeenCalledTimes(0);

    onFinish?.();

    expect(logger.logGlobalEvent).toHaveBeenCalledExactlyOnceWith('Timings:');
    // sorted by duration
    expect(logger.logTable).toHaveBeenCalledExactlyOnceWith([
        LogTimings.mapCloseEventToTimingInfo(command1ExitInfo),
        LogTimings.mapCloseEventToTimingInfo(command0ExitInfo),
    ]);
});

```

## File: lib\flow-control\log-timings.ts
```
import assert from 'node:assert';

import Rx from 'rxjs';
import { bufferCount, combineLatestWith, take } from 'rxjs/operators';

import { CloseEvent, Command } from '../command.js';
import { DateFormatter } from '../date-format.js';
import * as defaults from '../defaults.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

type TimingInfo = {
    name: string;
    duration: string;
    'exit code': string | number;
    killed: boolean;
    command: string;
};

/**
 * Logs timing information about commands as they start/stop and then a summary when all commands finish.
 */
export class LogTimings implements FlowController {
    static mapCloseEventToTimingInfo({
        command,
        timings,
        killed,
        exitCode,
    }: CloseEvent): TimingInfo {
        const readableDurationMs = (
            timings.endDate.getTime() - timings.startDate.getTime()
        ).toLocaleString();
        return {
            name: command.name,
            duration: readableDurationMs,
            'exit code': exitCode,
            killed,
            command: command.command,
        };
    }

    private readonly logger?: Logger;
    private readonly dateFormatter: DateFormatter;

    constructor({
        logger,
        timestampFormat = defaults.timestampFormat,
    }: {
        logger?: Logger;
        timestampFormat?: string;
    }) {
        this.logger = logger;
        this.dateFormatter = new DateFormatter(timestampFormat);
    }

    private printExitInfoTimingTable(exitInfos: CloseEvent[]) {
        assert.ok(this.logger);

        const exitInfoTable = exitInfos
            .sort((a, b) => b.timings.durationSeconds - a.timings.durationSeconds)
            .map(LogTimings.mapCloseEventToTimingInfo);

        this.logger.logGlobalEvent('Timings:');
        this.logger.logTable(exitInfoTable);
        return exitInfos;
    }

    handle(commands: Command[]) {
        const { logger } = this;
        if (!logger) {
            return { commands };
        }

        // individual process timings
        commands.forEach((command) => {
            command.timer.subscribe(({ startDate, endDate }) => {
                if (!endDate) {
                    const formattedStartDate = this.dateFormatter.format(startDate);
                    logger.logCommandEvent(
                        `${command.command} started at ${formattedStartDate}`,
                        command,
                    );
                } else {
                    const durationMs = endDate.getTime() - startDate.getTime();
                    const formattedEndDate = this.dateFormatter.format(endDate);
                    logger.logCommandEvent(
                        `${
                            command.command
                        } stopped at ${formattedEndDate} after ${durationMs.toLocaleString()}ms`,
                        command,
                    );
                }
            });
        });

        // overall summary timings
        const closeStreams = commands.map((command) => command.close);
        const finished = new Rx.Subject<void>();
        const allProcessesClosed = Rx.merge(...closeStreams).pipe(
            bufferCount(closeStreams.length),
            take(1),
            combineLatestWith(finished),
        );
        allProcessesClosed.subscribe(([exitInfos]) => this.printExitInfoTimingTable(exitInfos));
        return { commands, onFinish: () => finished.next() };
    }
}

```

## File: lib\flow-control\logger-padding.spec.ts
```
import { beforeEach, expect, it, MockedObject } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { LoggerPadding } from './logger-padding.js';

let logger: MockedObject<Logger>;
let controller: LoggerPadding;
let commands: FakeCommand[];

beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];
    logger = createMockInstance(Logger);
    controller = new LoggerPadding({ logger });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

it('sets the prefix length on handle', () => {
    controller.handle(commands);
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(1);
});

it('updates the prefix length when commands emit a start timer', () => {
    controller.handle(commands);
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(2);

    commands[1].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(3);
});

it('sets prefix length to the longest prefix of all commands', () => {
    logger.getPrefixContent
        .mockReturnValueOnce({ type: 'default', value: 'foobar' })
        .mockReturnValueOnce({ type: 'default', value: 'baz' });

    controller.handle(commands);
    expect(logger.setPrefixLength).toHaveBeenCalledWith(6);
});

it('does not shorten the prefix length', () => {
    logger.getPrefixContent
        .mockReturnValueOnce({ type: 'default', value: '100' })
        .mockReturnValueOnce({ type: 'default', value: '1' });

    controller.handle(commands);
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledWith(3);

    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledWith(3);
});

it('unsubscribes from start timers on finish', () => {
    logger.getPrefixContent.mockReturnValue({ type: 'default', value: '1' });

    const { onFinish } = controller.handle(commands);
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(2);

    onFinish();
    commands[0].timer.next({ startDate: new Date() });
    expect(logger.setPrefixLength).toHaveBeenCalledTimes(2);
});

```

## File: lib\flow-control\logger-padding.ts
```
import { Command } from '../command.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

export class LoggerPadding implements FlowController {
    private readonly logger: Logger;

    constructor({ logger }: { logger: Logger }) {
        this.logger = logger;
    }

    handle(commands: Command[]): { commands: Command[]; onFinish: () => void } {
        // Sometimes there's limited concurrency, so not all commands will spawn straight away.
        // Compute the prefix length now, which works for all styles but those with a PID.
        let length = commands.reduce((length, command) => {
            const content = this.logger.getPrefixContent(command);
            return Math.max(length, content?.value.length || 0);
        }, 0);
        this.logger.setPrefixLength(length);

        // The length of prefixes is somewhat stable, except for PIDs, which might change when a
        // process spawns (e.g. PIDs might look like 1, 10 or 100), therefore listen to command starts
        // and update the prefix length when this happens.
        const subs = commands.map((command) =>
            command.timer.subscribe((event) => {
                if (!event.endDate) {
                    const content = this.logger.getPrefixContent(command);
                    length = Math.max(length, content?.value.length || 0);
                    this.logger.setPrefixLength(length);
                }
            }),
        );

        return {
            commands,
            onFinish() {
                subs.forEach((sub) => sub.unsubscribe());
            },
        };
    }
}

```

## File: lib\flow-control\output-error-handler.spec.ts
```
import { Writable } from 'node:stream';

import { beforeEach, describe, expect, it, vi } from 'vitest';

import { FakeCommand } from '../__fixtures__/fake-command.js';
import { OutputErrorHandler } from './output-error-handler.js';

let controller: OutputErrorHandler;
let outputStream: Writable;
let abortController: AbortController;
let commands: FakeCommand[];
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];

    abortController = new AbortController();
    outputStream = new Writable();
    controller = new OutputErrorHandler({ abortController, outputStream });
});

it('returns same commands', () => {
    expect(controller.handle(commands)).toMatchObject({ commands });
});

describe('on output stream error', () => {
    beforeEach(() => {
        controller.handle(commands);
        outputStream.emit('error', new Error('test'));
    });

    it('kills every command', () => {
        expect(commands[0].kill).toHaveBeenCalled();
        expect(commands[1].kill).toHaveBeenCalled();
    });

    it('sends abort signal', () => {
        expect(abortController.signal.aborted).toBe(true);
    });
});

describe('on finish', () => {
    it('unsubscribes from output stream error', () => {
        const { onFinish } = controller.handle(commands);
        onFinish();

        outputStream.on('error', vi.fn());
        outputStream.emit('error', new Error('test'));

        expect(commands[0].kill).not.toHaveBeenCalled();
        expect(commands[1].kill).not.toHaveBeenCalled();
        expect(abortController.signal.aborted).toBe(false);
    });
});

```

## File: lib\flow-control\output-error-handler.ts
```
import { Writable } from 'node:stream';

import { Command } from '../command.js';
import { fromSharedEvent } from '../observables.js';
import { FlowController } from './flow-controller.js';

/**
 * Kills processes and aborts further command spawning on output stream error (namely, SIGPIPE).
 */
export class OutputErrorHandler implements FlowController {
    private readonly outputStream: Writable;
    private readonly abortController: AbortController;

    constructor({
        abortController,
        outputStream,
    }: {
        abortController: AbortController;
        outputStream: Writable;
    }) {
        this.abortController = abortController;
        this.outputStream = outputStream;
    }

    handle(commands: Command[]): { commands: Command[]; onFinish: () => void } {
        const subscription = fromSharedEvent(this.outputStream, 'error').subscribe(() => {
            commands.forEach((command) => command.kill());

            // Avoid further commands from spawning, e.g. if `RestartProcess` is used.
            this.abortController.abort();
        });

        return {
            commands,
            onFinish: () => subscription.unsubscribe(),
        };
    }
}

```

## File: lib\flow-control\restart-process.spec.ts
```
import { VirtualTimeScheduler } from 'rxjs';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeCloseEvent, FakeCommand } from '../__fixtures__/fake-command.js';
import { Logger } from '../logger.js';
import { RestartProcess } from './restart-process.js';

let commands: FakeCommand[];
let controller: RestartProcess;
let logger: Logger;
let scheduler: VirtualTimeScheduler;
beforeEach(() => {
    commands = [new FakeCommand(), new FakeCommand()];
    logger = createMockInstance(Logger);

    // Don't use TestScheduler as it's hardcoded to a max number of "frames" (time),
    // which don't work for some tests in this suite
    scheduler = new VirtualTimeScheduler();
    controller = new RestartProcess({
        logger,
        scheduler,
        delay: 100,
        tries: 2,
    });
});

it('does not restart processes that complete with success', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(commands[0].start).toHaveBeenCalledTimes(0);
    expect(commands[1].start).toHaveBeenCalledTimes(0);
});

it('restarts processes that fail immediately, if no delay was passed', () => {
    controller = new RestartProcess({ logger, scheduler, tries: 1 });
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    scheduler.flush();

    expect(scheduler.now()).toBe(0);
    expect(logger.logCommandEvent).toHaveBeenCalledExactlyOnceWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(1);
});

it('restarts processes that fail after delay ms has passed', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(scheduler.now()).toBe(100);
    expect(logger.logCommandEvent).toHaveBeenCalledExactlyOnceWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(1);
    expect(commands[1].start).not.toHaveBeenCalled();
});

it('restarts processes that fail with an exponential back-off', () => {
    const tries = 4;
    controller = new RestartProcess({ logger, scheduler, tries, delay: 'exponential' });
    controller.handle(commands);

    let time = 0;
    for (let i = 0; i < tries; i++) {
        commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
        scheduler.flush();

        time += 2 ** i * 1000;
        expect(scheduler.now()).toBe(time);
        expect(logger.logCommandEvent).toHaveBeenCalledTimes(i + 1);
        expect(commands[0].start).toHaveBeenCalledTimes(i + 1);
    }
});

it('restarts processes up to tries', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 'SIGTERM' }));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 'SIGTERM' }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(logger.logCommandEvent).toHaveBeenCalledTimes(2);
    expect(logger.logCommandEvent).toHaveBeenCalledWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(2);
});

it('restart processes forever, if tries is negative', () => {
    controller = new RestartProcess({
        logger,
        scheduler,
        delay: 100,
        tries: -1,
    });
    expect(controller.tries).toBe(Infinity);
});

it('restarts processes until they succeed', () => {
    controller.handle(commands);

    commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
    commands[0].close.next(createFakeCloseEvent({ exitCode: 0 }));
    commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

    scheduler.flush();

    expect(logger.logCommandEvent).toHaveBeenCalledExactlyOnceWith(
        `${commands[0].command} restarted`,
        commands[0],
    );
    expect(commands[0].start).toHaveBeenCalledTimes(1);
});

describe('returned commands', () => {
    it('are the same if 0 tries are to be attempted', () => {
        controller = new RestartProcess({ logger, scheduler });
        expect(controller.handle(commands)).toMatchObject({ commands });
    });

    it('are not the same, but with same length if 1+ tries are to be attempted', () => {
        const { commands: newCommands } = controller.handle(commands);
        expect(newCommands).not.toBe(commands);
        expect(newCommands).toHaveLength(commands.length);
    });

    it('skip close events followed by restarts', () => {
        const { commands: newCommands } = controller.handle(commands);

        const callback = vi.fn();
        newCommands[0].close.subscribe(callback);
        newCommands[1].close.subscribe(callback);

        commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
        commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
        commands[0].close.next(createFakeCloseEvent({ exitCode: 1 }));
        commands[1].close.next(createFakeCloseEvent({ exitCode: 1 }));
        commands[1].close.next(createFakeCloseEvent({ exitCode: 0 }));

        scheduler.flush();

        // 1 failure from commands[0], 1 success from commands[1]
        expect(callback).toHaveBeenCalledTimes(2);
    });

    it('keep non-close streams from original commands', () => {
        const { commands: newCommands } = controller.handle(commands);
        newCommands.forEach((newCommand, i) => {
            expect(newCommand.close).not.toBe(commands[i].close);
            expect(newCommand.error).toBe(commands[i].error);
            expect(newCommand.stdout).toBe(commands[i].stdout);
            expect(newCommand.stderr).toBe(commands[i].stderr);
        });
    });
});

```

## File: lib\flow-control\restart-process.ts
```
import Rx from 'rxjs';
import { defaultIfEmpty, delayWhen, filter, map, skip, take, takeWhile } from 'rxjs/operators';

import { Command } from '../command.js';
import * as defaults from '../defaults.js';
import { Logger } from '../logger.js';
import { FlowController } from './flow-controller.js';

export type RestartDelay = number | 'exponential';

/**
 * Restarts commands that fail up to a defined number of times.
 */
export class RestartProcess implements FlowController {
    private readonly logger: Logger;
    private readonly scheduler?: Rx.SchedulerLike;
    private readonly delay: RestartDelay;
    readonly tries: number;

    constructor({
        delay,
        tries,
        logger,
        scheduler,
    }: {
        delay?: RestartDelay;
        tries?: number;
        logger: Logger;
        scheduler?: Rx.SchedulerLike;
    }) {
        this.logger = logger;
        this.delay = delay ?? 0;
        this.tries = tries != null ? +tries : defaults.restartTries;
        this.tries = this.tries < 0 ? Infinity : this.tries;
        this.scheduler = scheduler;
    }

    handle(commands: Command[]) {
        if (this.tries === 0) {
            return { commands };
        }

        const delayOperator = delayWhen((_, index) => {
            const { delay } = this;
            const value = delay === 'exponential' ? 2 ** index * 1000 : delay;
            return Rx.timer(value, this.scheduler);
        });

        commands
            .map((command) =>
                command.close.pipe(
                    take(this.tries),
                    takeWhile(({ exitCode }) => exitCode !== 0),
                ),
            )
            .forEach((failure, index) =>
                Rx.merge(
                    // Delay the emission (so that the restarts happen on time),
                    // explicitly telling the subscriber that a restart is needed
                    failure.pipe(
                        delayOperator,
                        map(() => true),
                    ),
                    // Skip the first N emissions (as these would be duplicates of the above),
                    // meaning it will be empty because of success, or failed all N times,
                    // and no more restarts should be attempted.
                    failure.pipe(
                        skip(this.tries),
                        map(() => false),
                        defaultIfEmpty(false),
                    ),
                ).subscribe((restart) => {
                    const command = commands[index];
                    if (restart) {
                        this.logger.logCommandEvent(`${command.command} restarted`, command);
                        command.start();
                    }
                }),
            );

        return {
            commands: commands.map((command) => {
                const closeStream = command.close.pipe(
                    filter(({ exitCode }, emission) => {
                        // We let all success codes pass, and failures only after restarting won't happen again
                        return exitCode === 0 || emission >= this.tries;
                    }),
                );

                // Return a proxy so that mutations happen on the original Command object.
                // If either `Object.assign()` or `Object.create()` were used, it'd be hard to
                // reflect the mutations on Command objects referenced by previous flow controllers.
                return new Proxy(command, {
                    get(target, prop: keyof Command) {
                        return prop === 'close' ? closeStream : target[prop];
                    },
                });
            }),
        };
    }
}

```

## File: lib\flow-control\teardown.spec.ts
```
import { ChildProcess } from 'node:child_process';

import { afterEach, describe, expect, it, Mock, vi } from 'vitest';

import { createMockInstance } from '../__fixtures__/create-mock-instance.js';
import { createFakeProcess, FakeCommand } from '../__fixtures__/fake-command.js';
import { SpawnCommand } from '../command.js';
import { Logger } from '../logger.js';
import * as spawn from '../spawn.js';
import { Teardown } from './teardown.js';

const spySpawn = vi
    .spyOn(spawn, 'spawn')
    .mockImplementation(() => createFakeProcess(1) as ChildProcess) as Mock;
const logger = createMockInstance(Logger);
const commands = [new FakeCommand()];
const teardown = 'cowsay bye';

afterEach(() => {
    vi.clearAllMocks();
});

const create = (teardown: string[], spawn?: SpawnCommand) =>
    new Teardown({
        spawn,
        logger,
        commands: teardown,
    });

it('returns commands unchanged', () => {
    const { commands: actual } = create([]).handle(commands);
    expect(actual).toBe(commands);
});

describe('onFinish callback', () => {
    it('does not spawn nothing if there are no teardown commands', () => {
        create([]).handle(commands).onFinish();
        expect(spySpawn).not.toHaveBeenCalled();
    });

    it('runs teardown command', () => {
        create([teardown]).handle(commands).onFinish();
        expect(spySpawn).toHaveBeenCalledWith(teardown, spawn.getSpawnOpts({ stdio: 'raw' }));
    });

    it('runs teardown command with custom spawn function', () => {
        const customSpawn = vi.fn(() => createFakeProcess(1));
        create([teardown], customSpawn).handle(commands).onFinish();
        expect(customSpawn).toHaveBeenCalledWith(teardown, spawn.getSpawnOpts({ stdio: 'raw' }));
    });

    it('waits for teardown command to close', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        child.emit('close', 1, null);
        await expect(result).resolves.toBeUndefined();
    });

    it('rejects if teardown command errors (string)', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        const error = 'fail';
        child.emit('error', error);
        await expect(result).rejects.toBe(error);
        expect(logger.logGlobalEvent).toHaveBeenLastCalledWith('fail');
    });

    it('rejects if teardown command errors (error)', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        const error = new Error('fail');
        child.emit('error', error);
        await expect(result).rejects.toBe(error);
        expect(logger.logGlobalEvent).toHaveBeenLastCalledWith(
            expect.stringMatching(/Error: fail/),
        );
    });

    it('rejects if teardown command errors (error, no stack)', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create([teardown]).handle(commands).onFinish();
        const error = new Error('fail');
        delete error.stack;
        child.emit('error', error);
        await expect(result).rejects.toBe(error);
        expect(logger.logGlobalEvent).toHaveBeenLastCalledWith('Error: fail');
    });

    it('runs multiple teardown commands in sequence', async () => {
        const child1 = createFakeProcess(1);
        const child2 = createFakeProcess(2);
        spySpawn.mockReturnValueOnce(child1).mockReturnValueOnce(child2);

        const result = create(['foo', 'bar']).handle(commands).onFinish();

        expect(spySpawn).toHaveBeenCalledTimes(1);
        expect(spySpawn).toHaveBeenLastCalledWith('foo', spawn.getSpawnOpts({ stdio: 'raw' }));

        child1.emit('close', 1, null);
        await new Promise((resolve) => setTimeout(resolve));

        expect(spySpawn).toHaveBeenCalledTimes(2);
        expect(spySpawn).toHaveBeenLastCalledWith('bar', spawn.getSpawnOpts({ stdio: 'raw' }));

        child2.emit('close', 0, null);
        await expect(result).resolves.toBeUndefined();
    });

    it('stops running teardown commands on SIGINT', async () => {
        const child = createFakeProcess(1);
        spySpawn.mockReturnValue(child);

        const result = create(['foo', 'bar']).handle(commands).onFinish();
        child.emit('close', null, 'SIGINT');
        await result;

        expect(spySpawn).toHaveBeenCalledTimes(1);
        expect(spySpawn).toHaveBeenLastCalledWith('foo', expect.anything());
    });
});

```

## File: lib\flow-control\teardown.ts
```
import Rx from 'rxjs';

import { Command, SpawnCommand } from '../command.js';
import { Logger } from '../logger.js';
import { getSpawnOpts, spawn as baseSpawn } from '../spawn.js';
import { FlowController } from './flow-controller.js';

export class Teardown implements FlowController {
    private readonly logger: Logger;
    private readonly spawn: SpawnCommand;
    private readonly teardown: readonly string[];

    constructor({
        logger,
        spawn,
        commands,
    }: {
        logger: Logger;
        /**
         * Which function to use to spawn commands.
         * Defaults to the same used by the rest of concurrently.
         */
        spawn?: SpawnCommand;
        commands: readonly string[];
    }) {
        this.logger = logger;
        this.spawn = spawn || baseSpawn;
        this.teardown = commands;
    }

    handle(commands: Command[]): { commands: Command[]; onFinish: () => Promise<void> } {
        const { logger, teardown, spawn } = this;
        const onFinish = async () => {
            if (!teardown.length) {
                return;
            }

            for (const command of teardown) {
                logger.logGlobalEvent(`Running teardown command "${command}"`);

                const child = spawn(command, getSpawnOpts({ stdio: 'raw' }));
                const error = Rx.fromEvent(child, 'error');
                const close = Rx.fromEvent(child, 'close');

                try {
                    const [exitCode, signal] = await Promise.race([
                        Rx.firstValueFrom(error).then((event) => {
                            throw event;
                        }),
                        Rx.firstValueFrom(close).then(
                            (event) => event as [number | null, NodeJS.Signals | null],
                        ),
                    ]);

                    logger.logGlobalEvent(
                        `Teardown command "${command}" exited with code ${exitCode ?? signal}`,
                    );

                    if (signal === 'SIGINT') {
                        break;
                    }
                } catch (error) {
                    const errorText = String(error instanceof Error ? error.stack || error : error);
                    logger.logGlobalEvent(`Teardown command "${command}" errored:`);
                    logger.logGlobalEvent(errorText);
                    return Promise.reject(error);
                }
            }
        };

        return { commands, onFinish };
    }
}

```

## File: lib\__fixtures__\create-mock-instance.ts
```
import { MockedObject, vi } from 'vitest';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function createMockInstance<T>(constructor: new (...args: any[]) => T): MockedObject<T> {
    return new (vi.mockObject(constructor))() as MockedObject<T>;
}

```

## File: lib\__fixtures__\fake-command.ts
```
import EventEmitter from 'node:events';
import { PassThrough, Writable } from 'node:stream';

import { vi } from 'vitest';

import { ChildProcess, CloseEvent, Command, CommandInfo } from '../command.js';
import { createMockInstance } from './create-mock-instance.js';

export class FakeCommand extends Command {
    constructor(name = 'foo', command = 'echo foo', index = 0, info?: Partial<CommandInfo>) {
        super(
            {
                index,
                name,
                command,
                ...info,
            },
            {},
            vi.fn(),
            vi.fn(),
        );

        this.stdin = createMockInstance(Writable);
        this.start = vi.fn();
        this.kill = vi.fn();
    }
}

export const createFakeProcess = (pid: number): ChildProcess =>
    Object.assign(new EventEmitter(), {
        pid,
        send: vi.fn(),
        stdin: new PassThrough(),
        stdout: new PassThrough(),
        stderr: new PassThrough(),
    });

export const createFakeCloseEvent = (overrides?: Partial<CloseEvent>): CloseEvent => ({
    command: new FakeCommand(),
    index: 0,
    killed: false,
    exitCode: 0,
    timings: {
        startDate: new Date(),
        endDate: new Date(),
        durationSeconds: 0,
    },
    ...overrides,
});

```

## File: tests\package.json
```
{
  "dependencies": {
    "concurrently": "workspace:*"
  },
  "scripts": {
    "test": "pnpm --workspace-root test:smoke"
  }
}

```

## File: tests\smoke-tests.spec.ts
```
import { exec as originalExec } from 'node:child_process';
import util from 'node:util';

import { beforeAll, expect, it } from 'vitest';

const exec = util.promisify(originalExec);

beforeAll(async () => {
    await exec('pnpm run build');
}, 20_000);

it('spawns binary', async () => {
    await expect(exec('node dist/bin/index.js "echo test"')).resolves.toBeDefined();
});

it.each(['cjs-import', 'cjs-require', 'esm'])('loads library in %s context', async (project) => {
    // Use as separate execs as tsc outputs to stdout, instead of stderr, and so its text isn't shown
    await exec(`tsc -p ${project}`, { cwd: __dirname }).catch((err) => Promise.reject(err.stdout));
    await expect(
        exec(`node ${project}/dist/smoke-test.js`, { cwd: __dirname }),
    ).resolves.toBeDefined();
});

```

## File: tests\cjs-import\package.json
```
{
  "type": "commonjs"
}

```

## File: tests\cjs-import\smoke-test.ts
```
import type { ConcurrentlyResult } from 'concurrently';
import concurrently, { concurrently as concurrently2, createConcurrently } from 'concurrently';

const _result: ConcurrentlyResult = concurrently(['echo test'], {
    raw: true,
});

const _result2: ConcurrentlyResult = concurrently2(['echo test'], {
    killOthersOn: ['failure'],
});

const _result3: ConcurrentlyResult = createConcurrently(['echo test'], {
    successCondition: 'all',
});

```

## File: tests\cjs-import\tsconfig.json
```
{
  "compilerOptions": {
    "module": "commonjs",
    "outDir": "dist",
    "skipLibCheck": true
  }
}

```

## File: tests\cjs-require\package.json
```
{
  "type": "commonjs"
}

```

## File: tests\cjs-require\smoke-test.ts
```
// eslint-disable-next-line @typescript-eslint/no-require-imports
import concurrently = require('concurrently');

const { concurrently: concurrently2, createConcurrently } = concurrently;

const _result: concurrently.ConcurrentlyResult = concurrently.default(['echo test'], {
    raw: true,
});

const _result2: concurrently.ConcurrentlyResult = concurrently2(['echo test'], {
    killOthersOn: ['failure'],
});

const _result3: concurrently.ConcurrentlyResult = createConcurrently(['echo test'], {
    successCondition: 'all',
});

```

## File: tests\cjs-require\tsconfig.json
```
{
  "compilerOptions": {
    "module": "commonjs",
    "outDir": "dist",
    "skipLibCheck": true
  }
}

```

## File: tests\esm\package.json
```
{
  "type": "module"
}

```

## File: tests\esm\smoke-test.ts
```
import type { ConcurrentlyResult } from 'concurrently';
import concurrently, { concurrently as concurrently2, createConcurrently } from 'concurrently';

const _result: ConcurrentlyResult = concurrently(['echo test'], {
    raw: true,
});

const _result2: ConcurrentlyResult = concurrently2(['echo test'], {
    killOthersOn: ['failure'],
});

const _result3: ConcurrentlyResult = createConcurrently(['echo test'], {
    successCondition: 'all',
});

```

## File: tests\esm\tsconfig.json
```
{
  "compilerOptions": {
    "module": "node20",
    "outDir": "dist",
    "skipLibCheck": true
  }
}

```

