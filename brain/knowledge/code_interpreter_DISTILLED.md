---
id: code-interpreter
type: knowledge
owner: OA_Triage
---
# code-interpreter
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "e2b-code-interpreter-root",
  "private": true,
  "scripts": {
    "version": "pnpm changeset version && pnpm run -r postVersion",
    "publish": "pnpm changeset publish && pnpm run -r postPublish",
    "rm-node-modules": "find . -name 'node_modules' -type d -prune -exec rm -rf '{}' +",
    "lint": "pnpm --if-present --recursive run lint",
    "format": "pnpm --if-present --recursive run format",
    "changeset": "pnpx @changesets/cli"
  },
  "packageManager": "pnpm@9.15.9",
  "devDependencies": {
    "@changesets/read": "^0.6.2",
    "changeset": "^0.2.6",
    "@typescript-eslint/eslint-plugin": "^6.7.2",
    "@typescript-eslint/parser": "^6.7.2",
    "eslint": "^8.57.1",
    "eslint-plugin-unused-imports": "^3.0.0",
    "@stylistic/eslint-plugin-ts": "^1.6.2",
    "prettier": "^3.6.2"
  },
  "engines": {
    "pnpm": ">=9.0.0 <10"
  }
}

```

### File: README.md
```md
<!-- <p align="center">
  <img width="100" src="https://raw.githubusercontent.com/e2b-dev/E2B/refs/heads/main/readme-assets/logo-circle.png" alt="e2b logo">
</p> -->

![E2B Code Interpreter Preview](/readme-assets/e2b-code-interpreter-light.png#gh-light-mode-only)
![E2B Code Interpreter Preview](/readme-assets/e2b-code-interpreter-dark.png#gh-dark-mode-only)

<h4 align="center">
  <a href="https://pypi.org/project/e2b/">
    <img alt="Last 1 month downloads for the Python SDK" loading="lazy" width="200" height="20" decoding="async" data-nimg="1"
    style="color:transparent;width:auto;height:100%" src="https://img.shields.io/pypi/dm/e2b?label=PyPI%20Downloads">
  </a>
  <a href="https://www.npmjs.com/package/e2b">
    <img alt="Last 1 month downloads for the JavaScript SDK" loading="lazy" width="200" height="20" decoding="async" data-nimg="1"
    style="color:transparent;width:auto;height:100%" src="https://img.shields.io/npm/dm/e2b?label=NPM%20Downloads">
  </a>
</h4>

<!---
<img width="100%" src="/readme-assets/preview.png" alt="Cover image">
--->
## What is E2B?
[E2B](https://www.e2b.dev/) is an open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud. To start and control sandboxes, use our [JavaScript SDK](https://www.npmjs.com/package/@e2b/code-interpreter) or [Python SDK](https://pypi.org/project/e2b_code_interpreter).

## Run your first Sandbox

### 1. Install SDK

JavaScript / TypeScript
```
npm i @e2b/code-interpreter
```

Python
```
pip install e2b-code-interpreter
```

### 2. Get your E2B API key
1. Sign up to E2B [here](https://e2b.dev).
2. Get your API key [here](https://e2b.dev/dashboard?tab=keys).
3. Set environment variable with your API key.
```
E2B_API_KEY=e2b_***
```     

### 3. Execute code with code interpreter inside Sandbox

JavaScript / TypeScript
```ts
import { Sandbox } from '@e2b/code-interpreter'

const sbx = await Sandbox.create()
await sbx.runCode('x = 1')

const execution = await sbx.runCode('x+=1; x')
console.log(execution.text)  // outputs 2
```

Python
```py
from e2b_code_interpreter import Sandbox

with Sandbox.create() as sandbox:
    sandbox.run_code("x = 1")
    execution = sandbox.run_code("x+=1; x")
    print(execution.text)  # outputs 2
```

### 4. Check docs
Visit [E2B documentation](https://e2b.dev/docs).

### 5. E2B cookbook
Visit our [Cookbook](https://github.com/e2b-dev/e2b-cookbook/tree/main) to get inspired by examples with different LLMs and AI frameworks.

```

### File: .changeset\README.md
```md
# Changesets

To add changeset run: 
    
```bash
npx changeset
```

in the root of the project. This will create a new changeset in the `.changeset` folder.
```

### File: pnpm-lock.yaml
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: true

importers:

  .:
    devDependencies:
      '@changesets/read':
        specifier: ^0.6.2
        version: 0.6.7
      '@stylistic/eslint-plugin-ts':
        specifier: ^1.6.2
        version: 1.8.1(eslint@8.57.1)(typescript@5.7.3)
      '@typescript-eslint/eslint-plugin':
        specifier: ^6.7.2
        version: 6.21.0(@typescript-eslint/parser@6.21.0(eslint@8.57.1)(typescript@5.7.3))(eslint@8.57.1)(typescript@5.7.3)
      '@typescript-eslint/parser':
        specifier: ^6.7.2
        version: 6.21.0(eslint@8.57.1)(typescript@5.7.3)
      changeset:
        specifier: ^0.2.6
        version: 0.2.6
      eslint:
        specifier: ^8.57.1
        version: 8.57.1
      eslint-plugin-unused-imports:
        specifier: ^3.0.0
        version: 3.2.0(@typescript-eslint/eslint-plugin@6.21.0(@typescript-eslint/parser@6.21.0(eslint@8.57.1)(typescript@5.7.3))(eslint@8.57.1)(typescript@5.7.3))(eslint@8.57.1)
      prettier:
        specifier: ^3.6.2
        version: 3.6.2

  chart_data_extractor:
    devDependencies:
      '@typescript-eslint/eslint-plugin':
        specifier: ^7.11.0
        version: 7.18.0(@typescript-eslint/parser@7.18.0(eslint@8.57.1)(typescript@5.7.3))(eslint@8.57.1)(typescript@5.7.3)
      '@typescript-eslint/parser':
        specifier: ^7.11.0
        version: 7.18.0(eslint@8.57.1)(typescript@5.7.3)
      eslint:
        specifier: ^8.57.1
        version: 8.57.1

  js:
    dependencies:
      e2b:
        specifier: ^2.8.4
        version: 2.15.0
    devDependencies:
      '@types/node':
        specifier: ^20.19.19
        version: 20.19.37
      dotenv:
        specifier: ^16.4.5
        version: 16.6.1
      knip:
        specifier: ^5.25.1
        version: 5.43.6(@types/node@20.19.37)(typescript@5.7.3)
      npm-check-updates:
        specifier: ^17.1.14
        version: 17.1.18
      tsup:
        specifier: ^8.5.1
        version: 8.5.1(jiti@2.4.2)(postcss@8.5.3)(typescript@5.7.3)(yaml@2.7.0)
      typescript:
        specifier: ^5.5.3
        version: 5.7.3
      vitest:
        specifier: ^3.2.4
        version: 3.2.4(@types/node@20.19.37)(jiti@2.4.2)(yaml@2.7.0)

  python: {}

  template: {}

packages:

  '@babel/runtime@7.28.6':
    resolution: {integrity: sha512-05WQkdpL9COIMz4LjTxGpPNCdlpyimKppYNoJ5Di5EUObifl8t4tuLuUBBZEpoLYOmfvIWrsp9fCl0HoPRVTdA==}
    engines: {node: '>=6.9.0'}

  '@bufbuild/protobuf@2.11.0':
    resolution: {integrity: sha512-sBXGT13cpmPR5BMgHE6UEEfEaShh5Ror6rfN3yEK5si7QVrtZg8LEPQb0VVhiLRUslD2yLnXtnRzG035J/mZXQ==}

  '@changesets/errors@0.2.0':
    resolution: {integrity: sha512-6BLOQUscTpZeGljvyQXlWOItQyU71kCdGz7Pi8H8zdw6BI0g3m43iL4xKUVPWtG+qrrL9DTjpdn8eYuCQSRpow==}

  '@changesets/git@3.0.4':
    resolution: {integrity: sha512-BXANzRFkX+XcC1q/d27NKvlJ1yf7PSAgi8JG6dt8EfbHFHi4neau7mufcSca5zRhwOL8j9s6EqsxmT+s+/E6Sw==}

  '@changesets/logger@0.1.1':
    resolution: {integrity: sha512-OQtR36ZlnuTxKqoW4Sv6x5YIhOmClRd5pWsjZsddYxpWs517R0HkyiefQPIytCVh4ZcC5x9XaG8KTdd5iRQUfg==}

  '@changesets/parse@0.4.3':
    resolution: {integrity: sha512-ZDmNc53+dXdWEv7fqIUSgRQOLYoUom5Z40gmLgmATmYR9NbL6FJJHwakcCpzaeCy+1D0m0n7mT4jj2B/MQPl7A==}

  '@changesets/read@0.6.7':
    resolution: {integrity: sha512-D1G4AUYGrBEk8vj8MGwf75k9GpN6XL3wg8i42P2jZZwFLXnlr2Pn7r9yuQNbaMCarP7ZQWNJbV6XLeysAIMhTA==}

  '@changesets/types@4.1.0':
    resolution: {integrity: sha512-LDQvVDv5Kb50ny2s25Fhm3d9QSZimsoUGBsUioj6MC3qbMUCuC8GPIvk/M6IvXx3lYhAs0lwWUQLb+VIEUCECw==}

  '@changesets/types@6.1.0':
    resolution: {integrity: sha512-rKQcJ+o1nKNgeoYRHKOS07tAMNd3YSN0uHaJOZYjBAgxfV7TUE7JE+z4BzZdQwb5hKaYbayKN5KrYV7ODb2rAA==}

  '@connectrpc/connect-web@2.0.0-rc.3':
    resolution: {integrity: sha512-w88P8Lsn5CCsA7MFRl2e6oLY4J/5toiNtJns/YJrlyQaWOy3RO8pDgkz+iIkG98RPMhj2thuBvsd3Cn4DKKCkw==}
    peerDependencies:
      '@bufbuild/protobuf': ^2.2.0
      '@connectrpc/connect': 2.0.0-rc.3

  '@connectrpc/connect@2.0.0-rc.3':
    resolution: {integrity: sha512-ARBt64yEyKbanyRETTjcjJuHr2YXorzQo0etyS5+P6oSeW8xEuzajA9g+zDnMcj1hlX2dQE93foIWQGfpru7gQ==}
    peerDependencies:
      '@bufbuild/protobuf': ^2.2.0

  '@esbuild/aix-ppc64@0.25.0':
    resolution: {integrity: sha512-O7vun9Sf8DFjH2UtqK8Ku3LkquL9SZL8OLY1T5NZkA34+wG3OQF7cl4Ql8vdNzM6fzBbYfLaiRLIOZ+2FOCgBQ==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/aix-ppc64@0.27.2':
    resolution: {integrity: sha512-GZMB+a0mOMZs4MpDbj8RJp4cw+w1WV5NYD6xzgvzUJ5Ek2jerwfO2eADyI6ExDSUED+1X8aMbegahsJi+8mgpw==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.25.0':
    resolution: {integrity: sha512-grvv8WncGjDSyUBjN9yHXNt+cq0snxXbDxy5pJtzMKGmmpPxeAmAhWxXI+01lU5rwZomDgD3kJwulEnhTRUd6g==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm64@0.27.2':
    resolution: {integrity: sha512-pvz8ZZ7ot/RBphf8fv60ljmaoydPU12VuXHImtAs0XhLLw+EXBi2BLe3OYSBslR4rryHvweW5gmkKFwTiFy6KA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.25.0':
    resolution: {integrity: sha512-PTyWCYYiU0+1eJKmw21lWtC+d08JDZPQ5g+kFyxP0V+es6VPPSUhM6zk8iImp2jbV6GwjX4pap0JFbUQN65X1g==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-arm@0.27.2':
    resolution: {integrity: sha512-DVNI8jlPa7Ujbr1yjU2PfUSRtAUZPG9I1RwW4F4xFB1Imiu2on0ADiI/c3td+KmDtVKNbi+nffGDQMfcIMkwIA==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.25.0':
    resolution: {integrity: sha512-m/ix7SfKG5buCnxasr52+LI78SQ+wgdENi9CqyCXwjVR2X4Jkz+BpC3le3AoBPYTC9NHklwngVXvbJ9/Akhrfg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/android-x64@0.27.2':
    resolution: {integrity: sha512-z8Ank4Byh4TJJOh4wpz8g2vDy75zFL0TlZlkUkEwYXuPSgX8yzep596n6mT7905kA9uHZsf/o2OJZubl2l3M7A==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.25.0':
    resolution: {integrity: sha512-mVwdUb5SRkPayVadIOI78K7aAnPamoeFR2bT5nszFUZ9P8UpK4ratOdYbZZXYSqPKMHfS1wdHCJk1P1EZpRdvw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-arm64@0.27.2':
    resolution: {integrity: sha512-davCD2Zc80nzDVRwXTcQP/28fiJbcOwvdolL0sOiOsbwBa72kegmVU0Wrh1MYrbuCL98Omp5dVhQFWRKR2ZAlg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.25.0':
    resolution: {integrity: sha512-DgDaYsPWFTS4S3nWpFcMn/33ZZwAAeAFKNHNa1QN0rI4pUjgqf0f7ONmXf6d22tqTY+H9FNdgeaAa+YIFUn2Rg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/darwin-x64@0.27.2':
    resolution: {integrity: sha512-ZxtijOmlQCBWGwbVmwOF/UCzuGIbUkqB1faQRf5akQmxRJ1ujusWsb3CVfk/9iZKr2L5SMU5wPBi1UWbvL+VQA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.25.0':
    resolution: {integrity: sha512-VN4ocxy6dxefN1MepBx/iD1dH5K8qNtNe227I0mnTRjry8tj5MRk4zprLEdG8WPyAPb93/e4pSgi1SoHdgOa4w==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-arm64@0.27.2':
    resolution: {integrity: sha512-lS/9CN+rgqQ9czogxlMcBMGd+l8Q3Nj1MFQwBZJyoEKI50XGxwuzznYdwcav6lpOGv5BqaZXqvBSiB/kJ5op+g==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.25.0':
    resolution: {integrity: sha512-mrSgt7lCh07FY+hDD1TxiTyIHyttn6vnjesnPoVDNmDfOmggTLXRv8Id5fNZey1gl/V2dyVK1VXXqVsQIiAk+A==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.27.2':
    resolution: {integrity: sha512-tAfqtNYb4YgPnJlEFu4c212HYjQWSO/w/h/lQaBK7RbwGIkBOuNKQI9tqWzx7Wtp7bTPaGC6MJvWI608P3wXYA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.25.0':
    resolution: {integrity: sha512-9QAQjTWNDM/Vk2bgBl17yWuZxZNQIF0OUUuPZRKoDtqF2k4EtYbpyiG5/Dk7nqeK6kIJWPYldkOcBqjXjrUlmg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm64@0.27.2':
    resolution: {integrity: sha512-hYxN8pr66NsCCiRFkHUAsxylNOcAQaxSSkHMMjcpx0si13t1LHFphxJZUiGwojB1a/Hd5OiPIqDdXONia6bhTw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.25.0':
    resolution: {integrity: sha512-vkB3IYj2IDo3g9xX7HqhPYxVkNQe8qTK55fraQyTzTX/fxaDtXiEnavv9geOsonh2Fd2RMB+i5cbhu2zMNWJwg==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-arm@0.27.2':
    resolution: {integrity: sha512-vWfq4GaIMP9AIe4yj1ZUW18RDhx6EPQKjwe7n8BbIecFtCQG4CfHGaHuh7fdfq+y3LIA2vGS/o9ZBGVxIDi9hw==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.25.0':
    resolution: {integrity: sha512-43ET5bHbphBegyeqLb7I1eYn2P/JYGNmzzdidq/w0T8E2SsYL1U6un2NFROFRg1JZLTzdCoRomg8Rvf9M6W6Gg==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-ia32@0.27.2':
    resolution: {integrity: sha512-MJt5BRRSScPDwG2hLelYhAAKh9imjHK5+NE/tvnRLbIqUWa+0E9N4WNMjmp/kXXPHZGqPLxggwVhz7QP8CTR8w==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.25.0':
    resolution: {integrity: sha512-fC95c/xyNFueMhClxJmeRIj2yrSMdDfmqJnyOY4ZqsALkDrrKJfIg5NTMSzVBr5YW1jf+l7/cndBfP3MSDpoHw==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-loong64@0.27.2':
    resolution: {integrity: sha512-lugyF1atnAT463aO6KPshVCJK5NgRnU4yb3FUumyVz+cGvZbontBgzeGFO1nF+dPueHD367a2ZXe1NtUkAjOtg==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.25.0':
    resolution: {integrity: sha512-nkAMFju7KDW73T1DdH7glcyIptm95a7Le8irTQNO/qtkoyypZAnjchQgooFUDQhNAy4iu08N79W4T4pMBwhPwQ==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-mips64el@0.27.2':
    resolution: {integrity: sha512-nlP2I6ArEBewvJ2gjrrkESEZkB5mIoaTswuqNFRv/WYd+ATtUpe9Y09RnJvgvdag7he0OWgEZWhviS1OTOKixw==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.25.0':
    resolution: {integrity: sha512-NhyOejdhRGS8Iwv+KKR2zTq2PpysF9XqY+Zk77vQHqNbo/PwZCzB5/h7VGuREZm1fixhs4Q/qWRSi5zmAiO4Fw==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-ppc64@0.27.2':
    resolution: {integrity: sha512-C92gnpey7tUQONqg1n6dKVbx3vphKtTHJaNG2Ok9lGwbZil6DrfyecMsp9CrmXGQJmZ7iiVXvvZH6Ml5hL6XdQ==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.25.0':
    resolution: {integrity: sha512-5S/rbP5OY+GHLC5qXp1y/Mx//e92L1YDqkiBbO9TQOvuFXM+iDqUNG5XopAnXoRH3FjIUDkeGcY1cgNvnXp/kA==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-riscv64@0.27.2':
    resolution: {integrity: sha512-B5BOmojNtUyN8AXlK0QJyvjEZkWwy/FKvakkTDCziX95AowLZKR6aCDhG7LeF7uMCXEJqwa8Bejz5LTPYm8AvA==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.25.0':
    resolution: {integrity: sha512-XM2BFsEBz0Fw37V0zU4CXfcfuACMrppsMFKdYY2WuTS3yi8O1nFOhil/xhKTmE1nPmVyvQJjJivgDT+xh8pXJA==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-s390x@0.27.2':
    resolution: {integrity: sha512-p4bm9+wsPwup5Z8f4EpfN63qNagQ47Ua2znaqGH6bqLlmJ4bx97Y9JdqxgGZ6Y8xVTixUnEkoKSHcpRlDnNr5w==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.25.0':
    resolution: {integrity: sha512-9yl91rHw/cpwMCNytUDxwj2XjFpxML0y9HAOH9pNVQDpQrBxHy01Dx+vaMu0N1CKa/RzBD2hB4u//nfc+Sd3Cw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/linux-x64@0.27.2':
    resolution: {integrity: sha512-uwp2Tip5aPmH+NRUwTcfLb+W32WXjpFejTIOWZFw/v7/KnpCDKG66u4DLcurQpiYTiYwQ9B7KOeMJvLCu/OvbA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.25.0':
    resolution: {integrity: sha512-RuG4PSMPFfrkH6UwCAqBzauBWTygTvb1nxWasEJooGSJ/NwRw7b2HOwyRTQIU97Hq37l3npXoZGYMy3b3xYvPw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-arm64@0.27.2':
    resolution: {integrity: sha512-Kj6DiBlwXrPsCRDeRvGAUb/LNrBASrfqAIok+xB0LxK8CHqxZ037viF13ugfsIpePH93mX7xfJp97cyDuTZ3cw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.25.0':
    resolution: {integrity: sha512-jl+qisSB5jk01N5f7sPCsBENCOlPiS/xptD5yxOx2oqQfyourJwIKLRA2yqWdifj3owQZCL2sn6o08dBzZGQzA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.27.2':
    resolution: {integrity: sha512-HwGDZ0VLVBY3Y+Nw0JexZy9o/nUAWq9MlV7cahpaXKW6TOzfVno3y3/M8Ga8u8Yr7GldLOov27xiCnqRZf0tCA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/openbsd-arm64@0.25.0':
    resolution: {integrity: sha512-21sUNbq2r84YE+SJDfaQRvdgznTD8Xc0oc3p3iW/a1EVWeNj/SdUCbm5U0itZPQYRuRTW20fPMWMpcrciH2EJw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-arm64@0.27.2':
    resolution: {integrity: sha512-DNIHH2BPQ5551A7oSHD0CKbwIA/Ox7+78/AWkbS5QoRzaqlev2uFayfSxq68EkonB+IKjiuxBFoV8ESJy8bOHA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.25.0':
    resolution: {integrity: sha512-2gwwriSMPcCFRlPlKx3zLQhfN/2WjJ2NSlg5TKLQOJdV0mSxIcYNTMhk3H3ulL/cak+Xj0lY1Ym9ysDV1igceg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.27.2':
    resolution: {integrity: sha512-/it7w9Nb7+0KFIzjalNJVR5bOzA9Vay+yIPLVHfIQYG/j+j9VTH84aNB8ExGKPU4AzfaEvN9/V4HV+F+vo8OEg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [openbsd]

  '@esbuild/openharmony-arm64@0.27.2':
    resolution: {integrity: sha512-LRBbCmiU51IXfeXk59csuX/aSaToeG7w48nMwA6049Y4J4+VbWALAuXcs+qcD04rHDuSCSRKdmY63sruDS5qag==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openharmony]

  '@esbuild/sunos-x64@0.25.0':
    resolution: {integrity: sha512-bxI7ThgLzPrPz484/S9jLlvUAHYMzy6I0XiU1ZMeAEOBcS0VePBFxh1JjTQt3Xiat5b6Oh4x7UC7IwKQKIJRIg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [sunos]

  '@esbuild/sunos-x64@0.27.2':
    resolution: {integrity: sha512-kMtx1yqJHTmqaqHPAzKCAkDaKsffmXkPHThSfRwZGyuqyIeBvf08KSsYXl+abf5HDAPMJIPnbBfXvP2ZC2TfHg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [sunos]

  '@esbuild/win32-arm64@0.25.0':
    resolution: {integrity: sha512-ZUAc2YK6JW89xTbXvftxdnYy3m4iHIkDtK3CLce8wg8M2L+YZhIvO1DKpxrd0Yr59AeNNkTiic9YLf6FTtXWMw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [win32]

  '@esbuild/win32-arm64@0.27.2':
    resolution: {integrity: sha512-Yaf78O/B3Kkh+nKABUF++bvJv5Ijoy9AN1ww904rOXZFLWVc5OLOfL56W+C8F9xn5JQZa3UX6m+IktJnIb1Jjg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [win32]

  '@esbuild/win32-ia32@0.25.0':
    resolution: {integrity: sha512-eSNxISBu8XweVEWG31/JzjkIGbGIJN/TrRoiSVZwZ6pkC6VX4Im/WV2cz559/TXLcYbcrDN8JtKgd9DJVIo8GA==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [win32]

  '@esbuild/win32-ia32@0.27.2':
    resolution: {integrity: sha512-Iuws0kxo4yusk7sw70Xa2E2imZU5HoixzxfGCdxwBdhiDgt9vX9VUCBhqcwY7/uh//78A1hMkkROMJq9l27oLQ==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [win32]

  '@esbuild/win32-x64@0.25.0'
... [TRUNCATED]
```

### File: pnpm-workspace.yaml
```yaml
packages:
  - js
  - python
  - chart_data_extractor
  - template

```

### File: .changeset\config.json
```json
{
  "$schema": "https://unpkg.com/@changesets/config@2.3.1/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "ignore": [],
  "linked": [],
  "access": "public",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "privatePackages": {
    "version": true,
    "tag": true
  }
}
```

### File: .github\scripts\is_release.sh
```sh
#!/bin/sh

# This script checks if the current commit contains changesets.

set -eu

CHANGES=$(node -e "require('@changesets/read').default(process.cwd()).then(result => console.log(!!result.length))")

echo "${CHANGES}"

```

### File: .github\scripts\is_release_for_package.sh
```sh
#!/bin/sh

# This script checks if the specified package has changesets in the current commit.

set -eu

if [ $# -lt 1 ]; then
  echo "Error: Package name is required as the first argument." >&2
  exit 1
fi

PACKAGE_NAME=$1
PACKAGE_CHANGES=$(node -e "require('@changesets/read').default(process.cwd()).then(result => console.log(result.flatMap(changeset => changeset.releases.flatMap(release => release.name)).includes('${PACKAGE_NAME}')))")

echo "${PACKAGE_CHANGES}"

```

### File: .github\workflows\validate-renovate-config.yaml
```yaml
name: validate renovate config

permissions:
  contents: read

on:
  pull_request:
    branches:
      - main

jobs:
  validate-renovate-config:
    runs-on: ubuntu-24.04
    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Validate Renovate config
        uses: suzuki-shunsuke/github-action-renovate-config-validator@v2.0.0

```

