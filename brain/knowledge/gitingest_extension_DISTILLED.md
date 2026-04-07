---
id: gitingest-extension
type: knowledge
owner: OA_Triage
---
# gitingest-extension
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "gitingest-extension",
  "description": "open git ingest fastly",
  "private": true,
  "version": "1.2",
  "type": "module",
  "author": {
    "name": "甜檸Cirtron (lcandy2)",
    "email": "vanilla#citrons.cc",
    "url": "https://github.com/lcandy2"
  },
  "homepage": "https://github.com/lcandy2/gitingest-extension",
  "scripts": {
    "dev": "wxt",
    "dev:firefox": "wxt -b firefox",
    "build": "wxt build",
    "build:firefox": "wxt build -b firefox",
    "zip": "wxt zip",
    "zip:firefox": "wxt zip -b firefox",
    "compile": "tsc --noEmit",
    "postinstall": "wxt prepare"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  },
  "devDependencies": {
    "@types/chrome": "^0.0.280",
    "@types/react": "^19.0.1",
    "@types/react-dom": "^19.0.2",
    "@wxt-dev/module-react": "^1.1.2",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.6.3",
    "wxt": "^0.19.13"
  },
  "packageManager": "pnpm@9.15.1+sha512.1acb565e6193efbebda772702950469150cf12bcc764262e7587e71d19dc98a423dff9536e57ea44c49bdf790ff694e83c27be5faa23d67e0c033b583be4bfcf"
}

```

### File: README.md
```md
![Prompt-friendly codebase
Turn any GitHub repository into a simple text ingest of its codebase.
This is useful for feeding a codebase into any LLM.](https://github.com/user-attachments/assets/e3b87d4f-5617-446f-90b3-035d5f7d5e1e)

<img width="64" height="64" src="https://github.com/user-attachments/assets/e6a0c74d-0548-4c76-8536-c613ded73430" alt="GitIngest Icon"><h1>GitIngest Extension 🔍</h1>
Turn any Git repository into a prompt-friendly text ingest for LLMs.

<a href="https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood" target="_blank" title="Get GitIngest Extension from Chrome Web Store"><img height="48" src="https://github.com/user-attachments/assets/20a6e44b-fd46-4e6c-8ea6-aad436035753" alt="Available in the Chrome Web Store" /></a>
<a href="https://addons.mozilla.org/firefox/addon/gitingest/" target="_blank" title="Get GitIngest Extension from Firefox Add-ons"><img height="48" src="https://github.com/user-attachments/assets/c0e99e6b-97cf-4af2-9737-099db7d3538b" alt="Get The Add-on for Firefox" /></a>
<a href="https://microsoftedge.microsoft.com/addons/detail/nfobhllgcekbmpifkjlopfdfdmljmipf" target="_blank" title="Get GitIngest Extension from Firefox Add-ons"><img height="48" src="https://github.com/user-attachments/assets/204157eb-4cae-4c0e-b2cb-db514419fd9e" alt="Get from the Edge Add-ons" /></a>

This extension is part of the GitIngest ecosystem. See [GitIngest.com](https://gitingest.com) or [cyclotruc/gitingest](https://github.com/cyclotruc/gitingest) for more information.

## ✨ Features

- 🚀 One-click access to GitIngest services to get a text ingest
- 📚 Prompt-friendly codebase ingestion
- 📝 Optimized output format for LLM prompts
- 🔍 Statistics about:
  - File and directory structure
  - Size of the extract
  - Token count  
- 🔒 Privacy-first, zero data collection (for the extension itself)
- 🤖 Open source, community-driven

## 📸 Screenshots

https://github.com/user-attachments/assets/fb831553-c55a-43e7-af91-7636e9084ae8
<!-- ![Screenshot 0](https://github.com/user-attachments/assets/cfe4b346-2c02-4aef-895d-39847938423f) -->
| ![Screenshot 1](https://github.com/user-attachments/assets/3a9ce50f-1cb1-4a02-9b45-ed0109c3e9f5) | ![Screenshot 2](https://github.com/user-attachments/assets/e723c81f-5b24-41c9-82c0-4b93293427e8) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

## 🛠️ Using
- [WXT](https://github.com/wxt-dev/wxt)
- [TailwindCSS](https://tailwindcss.com/)

## 🔒 Privacy Policy
> This privacy policy is for the extension only.
[Privacy Policy (26 December 2024)](PRIVACY.md)

## 🔧 Development

### Clone the repository
```bash
git clone https://github.com/lcandy2/gitingest-extension.git
```

### Install dependencies
```bash
pnpm install
```

### Run the development server
```bash
pnpm dev
```

### Build the extension
```bash
pnpm build
```

## 📄 License
[MIT](LICENSE.md)

```

### File: LICENSE.md
```md
MIT License

Copyright (c) 2024 甜檸Cirtron

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

### File: pnpm-lock.yaml
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      react:
        specifier: ^19.0.0
        version: 19.0.0
      react-dom:
        specifier: ^19.0.0
        version: 19.0.0(react@19.0.0)
    devDependencies:
      '@types/chrome':
        specifier: ^0.0.280
        version: 0.0.280
      '@types/react':
        specifier: ^19.0.1
        version: 19.0.2
      '@types/react-dom':
        specifier: ^19.0.2
        version: 19.0.2(@types/react@19.0.2)
      '@wxt-dev/module-react':
        specifier: ^1.1.2
        version: 1.1.3(vite@6.0.6(@types/node@22.10.2)(jiti@1.21.7)(yaml@2.6.1))(wxt@0.19.23(@types/node@22.10.2)(rollup@4.29.1)(yaml@2.6.1))
      autoprefixer:
        specifier: ^10.4.20
        version: 10.4.20(postcss@8.4.49)
      postcss:
        specifier: ^8.4.49
        version: 8.4.49
      tailwindcss:
        specifier: ^3.4.17
        version: 3.4.17
      typescript:
        specifier: ^5.6.3
        version: 5.7.2
      wxt:
        specifier: ^0.19.13
        version: 0.19.23(@types/node@22.10.2)(rollup@4.29.1)(yaml@2.6.1)

packages:

  '@1natsu/wait-element@4.1.2':
    resolution: {integrity: sha512-qWxSJD+Q5b8bKOvESFifvfZ92DuMsY+03SBNjTO34ipJLP6mZ9yK4bQz/vlh48aEQXoJfaZBqUwKL5BdI5iiWw==}

  '@aklinker1/rollup-plugin-visualizer@5.12.0':
    resolution: {integrity: sha512-X24LvEGw6UFmy0lpGJDmXsMyBD58XmX1bbwsaMLhNoM+UMQfQ3b2RtC+nz4b/NoRK5r6QJSKJHBNVeUdwqybaQ==}
    engines: {node: '>=14'}
    hasBin: true
    peerDependencies:
      rollup: 2.x || 3.x || 4.x
    peerDependenciesMeta:
      rollup:
        optional: true

  '@alloc/quick-lru@5.2.0':
    resolution: {integrity: sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==}
    engines: {node: '>=10'}

  '@ampproject/remapping@2.3.0':
    resolution: {integrity: sha512-30iZtAPgz+LTIYoeivqYo853f02jBYSd5uGnGpkFV0M3xOt9aN73erkgYAmZU43x4VfqcnLxW9Kpg3R5LC4YYw==}
    engines: {node: '>=6.0.0'}

  '@babel/code-frame@7.26.2':
    resolution: {integrity: sha512-RJlIHRueQgwWitWgF8OdFYGZX328Ax5BCemNGlqHfplnRT9ESi8JkFlvaVYbS+UubVY6dpv87Fs2u5M29iNFVQ==}
    engines: {node: '>=6.9.0'}

  '@babel/compat-data@7.26.3':
    resolution: {integrity: sha512-nHIxvKPniQXpmQLb0vhY3VaFb3S0YrTAwpOWJZh1wn3oJPjJk9Asva204PsBdmAE8vpzfHudT8DB0scYvy9q0g==}
    engines: {node: '>=6.9.0'}

  '@babel/core@7.26.0':
    resolution: {integrity: sha512-i1SLeK+DzNnQ3LL/CswPCa/E5u4lh1k6IAEphON8F+cXt0t9euTshDru0q7/IqMa1PMPz5RnHuHscF8/ZJsStg==}
    engines: {node: '>=6.9.0'}

  '@babel/generator@7.26.3':
    resolution: {integrity: sha512-6FF/urZvD0sTeO7k6/B15pMLC4CHUv1426lzr3N01aHJTl046uCAh9LXW/fzeXXjPNCJ6iABW5XaWOsIZB93aQ==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-compilation-targets@7.25.9':
    resolution: {integrity: sha512-j9Db8Suy6yV/VHa4qzrj9yZfZxhLWQdVnRlXxmKLYlhWUVB1sB2G5sxuWYXk/whHD9iW76PmNzxZ4UCnTQTVEQ==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-imports@7.25.9':
    resolution: {integrity: sha512-tnUA4RsrmflIM6W6RFTLFSXITtl0wKjgpnLgXyowocVPrbYrLUXSBXDgTs8BlbmIzIdlBySRQjINYs2BAkiLtw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-transforms@7.26.0':
    resolution: {integrity: sha512-xO+xu6B5K2czEnQye6BHA7DolFFmS3LB7stHZFaOLb1pAwO1HWLS8fXA+eh0A2yIvltPVmx3eNNDBJA2SLHXFw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-plugin-utils@7.25.9':
    resolution: {integrity: sha512-kSMlyUVdWe25rEsRGviIgOWnoT/nfABVWlqt9N19/dIPWViAOW2s9wznP5tURbs/IDuNk4gPy3YdYRgH3uxhBw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-string-parser@7.25.9':
    resolution: {integrity: sha512-4A/SCr/2KLd5jrtOMFzaKjVtAei3+2r/NChoBNoZ3EyP/+GlhoaEGoWOZUmFmoITP7zOJyHIMm+DYRd8o3PvHA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-identifier@7.25.9':
    resolution: {integrity: sha512-Ed61U6XJc3CVRfkERJWDz4dJwKe7iLmmJsbOGu9wSloNSFttHV0I8g6UAgb7qnK5ly5bGLPd4oXZlxCdANBOWQ==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-option@7.25.9':
    resolution: {integrity: sha512-e/zv1co8pp55dNdEcCynfj9X7nyUKUXoUEwfXqaZt0omVOmDe9oOTdKStH4GmAw6zxMFs50ZayuMfHDKlO7Tfw==}
    engines: {node: '>=6.9.0'}

  '@babel/helpers@7.26.0':
    resolution: {integrity: sha512-tbhNuIxNcVb21pInl3ZSjksLCvgdZy9KwJ8brv993QtIVKJBBkYXz4q4ZbAv31GdnC+R90np23L5FbEBlthAEw==}
    engines: {node: '>=6.9.0'}

  '@babel/parser@7.26.3':
    resolution: {integrity: sha512-WJ/CvmY8Mea8iDXo6a7RK2wbmJITT5fN3BEkRuFlxVyNx8jOKIIhmC4fSkTcPcf8JyavbBwIe6OpiCOBXt/IcA==}
    engines: {node: '>=6.0.0'}
    hasBin: true

  '@babel/plugin-transform-react-jsx-self@7.25.9':
    resolution: {integrity: sha512-y8quW6p0WHkEhmErnfe58r7x0A70uKphQm8Sp8cV7tjNQwK56sNVK0M73LK3WuYmsuyrftut4xAkjjgU0twaMg==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/plugin-transform-react-jsx-source@7.25.9':
    resolution: {integrity: sha512-+iqjT8xmXhhYv4/uiYd8FNQsraMFZIfxVSqxxVSZP0WbbSAWvBXAul0m/zu+7Vv4O/3WtApy9pmaTMiumEZgfg==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/runtime@7.24.7':
    resolution: {integrity: sha512-UwgBRMjJP+xv857DCngvqXI3Iq6J4v0wXmwc6sapg+zyhbwmQX67LUEFrkK5tbyJ30jGuG3ZvWpBiB9LCy1kWw==}
    engines: {node: '>=6.9.0'}

  '@babel/template@7.25.9':
    resolution: {integrity: sha512-9DGttpmPvIxBb/2uwpVo3dqJ+O6RooAFOS+lB+xDqoE2PVCE8nfoHMdZLpfCQRLwvohzXISPZcgxt80xLfsuwg==}
    engines: {node: '>=6.9.0'}

  '@babel/traverse@7.26.4':
    resolution: {integrity: sha512-fH+b7Y4p3yqvApJALCPJcwb0/XaOSgtK4pzV6WVjPR5GLFQBRI7pfoX2V2iM48NXvX07NUxxm1Vw98YjqTcU5w==}
    engines: {node: '>=6.9.0'}

  '@babel/types@7.26.3':
    resolution: {integrity: sha512-vN5p+1kl59GVKMvTHt55NzzmYVxprfJD+ql7U9NFIfKCBkYE55LYtS+WtPlaYOyzydrKI8Nezd+aZextrd+FMA==}
    engines: {node: '>=6.9.0'}

  '@devicefarmer/adbkit-logcat@2.1.3':
    resolution: {integrity: sha512-yeaGFjNBc/6+svbDeul1tNHtNChw6h8pSHAt5D+JsedUrMTN7tla7B15WLDyekxsuS2XlZHRxpuC6m92wiwCNw==}
    engines: {node: '>= 4'}

  '@devicefarmer/adbkit-monkey@1.2.1':
    resolution: {integrity: sha512-ZzZY/b66W2Jd6NHbAhLyDWOEIBWC11VizGFk7Wx7M61JZRz7HR9Cq5P+65RKWUU7u6wgsE8Lmh9nE4Mz+U2eTg==}
    engines: {node: '>= 0.10.4'}

  '@devicefarmer/adbkit@3.2.6':
    resolution: {integrity: sha512-8lO1hSeTgtxcOHhp4tTWq/JaOysp5KNbbyFoxNEBnwkCDZu/Bji3ZfOaG++Riv9jN6c9bgdLBOZqJTC5VJPRKQ==}
    engines: {node: '>= 0.10.4'}
    hasBin: true

  '@esbuild/aix-ppc64@0.21.5':
    resolution: {integrity: sha512-1SDgH6ZSPTlggy1yI6+Dbkiz8xzpHJEVAlF/AM1tHPLsf5STom9rwtjE4hKAF20FfXXNTFqEYXyJNWh1GiZedQ==}
    engines: {node: '>=12'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/aix-ppc64@0.24.2':
    resolution: {integrity: sha512-thpVCb/rhxE/BnMLQ7GReQLLN8q9qbHmI55F4489/ByVg2aQaQ6kbcLb6FHkocZzQhxc4gx0sCk0tJkKBFzDhA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.21.5':
    resolution: {integrity: sha512-c0uX9VAUBQ7dTDCjq+wdyGLowMdtR/GoC2U5IYk/7D1H1JYC0qseD7+11iMP2mRLN9RcCMRcjC4YMclCzGwS/A==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm64@0.24.2':
    resolution: {integrity: sha512-cNLgeqCqV8WxfcTIOeL4OAtSmL8JjcN6m09XIgro1Wi7cF4t/THaWEa7eL5CMoMBdjoHOTh/vwTO/o2TRXIyzg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.21.5':
    resolution: {integrity: sha512-vCPvzSjpPHEi1siZdlvAlsPxXl7WbOVUBBAowWug4rJHb68Ox8KualB+1ocNvT5fjv6wpkX6o/iEpbDrf68zcg==}
    engines: {node: '>=12'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-arm@0.24.2':
    resolution: {integrity: sha512-tmwl4hJkCfNHwFB3nBa8z1Uy3ypZpxqxfTQOcHX+xRByyYgunVbZ9MzUUfb0RxaHIMnbHagwAxuTL+tnNM+1/Q==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.21.5':
    resolution: {integrity: sha512-D7aPRUUNHRBwHxzxRvp856rjUHRFW1SdQATKXH2hqA0kAZb1hKmi02OpYRacl0TxIGz/ZmXWlbZgjwWYaCakTA==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [android]

  '@esbuild/android-x64@0.24.2':
    resolution: {integrity: sha512-B6Q0YQDqMx9D7rvIcsXfmJfvUYLoP722bgfBlO5cGvNVb5V/+Y7nhBE3mHV9OpxBf4eAS2S68KZztiPaWq4XYw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.21.5':
    resolution: {integrity: sha512-DwqXqZyuk5AiWWf3UfLiRDJ5EDd49zg6O9wclZ7kUMv2WRFr4HKjXp/5t8JZ11QbQfUS6/cRCKGwYhtNAY88kQ==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-arm64@0.24.2':
    resolution: {integrity: sha512-kj3AnYWc+CekmZnS5IPu9D+HWtUI49hbnyqk0FLEJDbzCIQt7hg7ucF1SQAilhtYpIujfaHr6O0UHlzzSPdOeA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.21.5':
    resolution: {integrity: sha512-se/JjF8NlmKVG4kNIuyWMV/22ZaerB+qaSi5MdrXtd6R08kvs2qCN4C09miupktDitvh8jRFflwGFBQcxZRjbw==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/darwin-x64@0.24.2':
    resolution: {integrity: sha512-WeSrmwwHaPkNR5H3yYfowhZcbriGqooyu3zI/3GGpF8AyUdsrrP0X6KumITGA9WOyiJavnGZUwPGvxvwfWPHIA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.21.5':
    resolution: {integrity: sha512-5JcRxxRDUJLX8JXp/wcBCy3pENnCgBR9bN6JsY4OmhfUtIHe3ZW0mawA7+RDAcMLrMIZaf03NlQiX9DGyB8h4g==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-arm64@0.24.2':
    resolution: {integrity: sha512-UN8HXjtJ0k/Mj6a9+5u6+2eZ2ERD7Edt1Q9IZiB5UZAIdPnVKDoG7mdTVGhHJIeEml60JteamR3qhsr1r8gXvg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.21.5':
    resolution: {integrity: sha512-J95kNBj1zkbMXtHVH29bBriQygMXqoVQOQYA+ISs0/2l3T9/kj42ow2mpqerRBxDJnmkUDCaQT/dfNXWX/ZZCQ==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.24.2':
    resolution: {integrity: sha512-TvW7wE/89PYW+IevEJXZ5sF6gJRDY/14hyIGFXdIucxCsbRmLUcjseQu1SyTko+2idmCw94TgyaEZi9HUSOe3Q==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.21.5':
    resolution: {integrity: sha512-ibKvmyYzKsBeX8d8I7MH/TMfWDXBF3db4qM6sy+7re0YXya+K1cem3on9XgdT2EQGMu4hQyZhan7TeQ8XkGp4Q==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm64@0.24.2':
    resolution: {integrity: sha512-7HnAD6074BW43YvvUmE/35Id9/NB7BeX5EoNkK9obndmZBUk8xmJJeU7DwmUeN7tkysslb2eSl6CTrYz6oEMQg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.21.5':
    resolution: {integrity: sha512-bPb5AHZtbeNGjCKVZ9UGqGwo8EUu4cLq68E95A53KlxAPRmUyYv2D6F0uUI65XisGOL1hBP5mTronbgo+0bFcA==}
    engines: {node: '>=12'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-arm@0.24.2':
    resolution: {integrity: sha512-n0WRM/gWIdU29J57hJyUdIsk0WarGd6To0s+Y+LwvlC55wt+GT/OgkwoXCXvIue1i1sSNWblHEig00GBWiJgfA==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.21.5':
    resolution: {integrity: sha512-YvjXDqLRqPDl2dvRODYmmhz4rPeVKYvppfGYKSNGdyZkA01046pLWyRKKI3ax8fbJoK5QbxblURkwK/MWY18Tg==}
    engines: {node: '>=12'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-ia32@0.24.2':
    resolution: {integrity: sha512-sfv0tGPQhcZOgTKO3oBE9xpHuUqguHvSo4jl+wjnKwFpapx+vUDcawbwPNuBIAYdRAvIDBfZVvXprIj3HA+Ugw==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.21.5':
    resolution: {integrity: sha512-uHf1BmMG8qEvzdrzAqg2SIG/02+4/DHB6a9Kbya0XDvwDEKCoC8ZRWI5JJvNdUjtciBGFQ5PuBlpEOXQj+JQSg==}
    engines: {node: '>=12'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-loong64@0.24.2':
    resolution: {integrity: sha512-CN9AZr8kEndGooS35ntToZLTQLHEjtVB5n7dl8ZcTZMonJ7CCfStrYhrzF97eAecqVbVJ7APOEe18RPI4KLhwQ==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.21.5':
    resolution: {integrity: sha512-IajOmO+KJK23bj52dFSNCMsz1QP1DqM6cwLUv3W1QwyxkyIWecfafnI555fvSGqEKwjMXVLokcV5ygHW5b3Jbg==}
    engines: {node: '>=12'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-mips64el@0.24.2':
    resolution: {integrity: sha512-iMkk7qr/wl3exJATwkISxI7kTcmHKE+BlymIAbHO8xanq/TjHaaVThFF6ipWzPHryoFsesNQJPE/3wFJw4+huw==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.21.5':
    resolution: {integrity: sha512-1hHV/Z4OEfMwpLO8rp7CvlhBDnjsC3CttJXIhBi+5Aj5r+MBvy4egg7wCbe//hSsT+RvDAG7s81tAvpL2XAE4w==}
    engines: {node: '>=12'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-ppc64@0.24.2':
    resolution: {integrity: sha512-shsVrgCZ57Vr2L8mm39kO5PPIb+843FStGt7sGGoqiiWYconSxwTiuswC1VJZLCjNiMLAMh34jg4VSEQb+iEbw==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.21.5':
    resolution: {integrity: sha512-2HdXDMd9GMgTGrPWnJzP2ALSokE/0O5HhTUvWIbD3YdjME8JwvSCnNGBnTThKGEB91OZhzrJ4qIIxk/SBmyDDA==}
    engines: {node: '>=12'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-riscv64@0.24.2':
    resolution: {integrity: sha512-4eSFWnU9Hhd68fW16GD0TINewo1L6dRrB+oLNNbYyMUAeOD2yCK5KXGK1GH4qD/kT+bTEXjsyTCiJGHPZ3eM9Q==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.21.5':
    resolution: {integrity: sha512-zus5sxzqBJD3eXxwvjN1yQkRepANgxE9lgOW2qLnmr8ikMTphkjgXu1HR01K4FJg8h1kEEDAqDcZQtbrRnB41A==}
    engines: {node: '>=12'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-s390x@0.24.2':
    resolution: {integrity: sha512-S0Bh0A53b0YHL2XEXC20bHLuGMOhFDO6GN4b3YjRLK//Ep3ql3erpNcPlEFed93hsQAjAQDNsvcK+hV90FubSw==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.21.5':
    resolution: {integrity: sha512-1rYdTpyv03iycF1+BhzrzQJCdOuAOtaqHTWJZCWvijKD2N5Xu0TtVC8/+1faWqcP9iBCWOmjmhoH94dH82BxPQ==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [linux]

  '@esbuild/linux-x64@0.24.2':
    resolution: {integrity: sha512-8Qi4nQcCTbLnK9WoMjdC9NiTG6/E38RNICU6sUNqK0QFxCYgoARqVqxdFmWkdonVsvGqWhmm7MO0jyTqLqwj0Q==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.24.2':
    resolution: {integrity: sha512-wuLK/VztRRpMt9zyHSazyCVdCXlpHkKm34WUyinD2lzK07FAHTq0KQvZZlXikNWkDGoT6x3TD51jKQ7gMVpopw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.21.5':
    resolution: {integrity: sha512-Woi2MXzXjMULccIwMnLciyZH4nCIMpWQAs049KEeMvOcNADVxo0UBIQPfSmxB3CWKedngg7sWZdLvLczpe0tLg==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.24.2':
    resolution: {integrity: sha512-VefFaQUc4FMmJuAxmIHgUmfNiLXY438XrL4GDNV1Y1H/RW3qow68xTwjZKfj/+Plp9NANmzbH5R40Meudu8mmw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/openbsd-arm64@0.24.2':
    resolution: {integrity: sha512-YQbi46SBct6iKnszhSvdluqDmxCJA+Pu280Av9WICNwQmMxV7nLRHZfjQzwbPs3jeWnuAhE9Jy0NrnJ12Oz+0A==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.21.5':
    resolution: {integrity: sha512-HLNNw99xsvx12lFBUwoT8EVCsSvRNDVxNpjZ7bPn947b8gJPzeHWyNVhFsaerc0n3TsbOINvRP2byTZ5LKezow==}
    engi
... [TRUNCATED]
```

### File: PRIVACY.md
```md
# Privacy Policy
Last updated: 26 December 2024

## Overview
GitIngest Extension is committed to protecting your privacy. This privacy policy explains what information we collect, how we use it, and what rights you have in relation to it. This policy applies to all users of our browser extension, regardless of location.

**Important Note**: This extension is designed to be completely offline-capable and does not transmit any data to any servers. All functionality is handled locally within your browser.

**Disclaimer**: This extension only provides a redirect functionality to GitIngest.com or other user-configured URLs. Any data collection, processing, or usage that occurs on these websites is governed by their respective privacy policies and is not covered by this privacy policy. We are not responsible for and have no control over the privacy practices of these external services.

## Data Collection

### What We Collect
The extension collects and stores:
1. **Service URL Configuration**: If you choose to use a custom GitIngest service instance, the extension stores your configured base URL locally in your browser.

### What We Don't Collect
The extension does NOT collect:
- Personal information
- GitHub account information
- Repository data
- Browsing history
- Usage statistics
- Cookies or tracking data
- Any other user data

### Zero Data Transmission
By design and as verified in our open-source code:
- No data is ever transmitted to our servers
- No data is ever transmitted to third-party servers
- No analytics or tracking code is implemented
- All operations are performed locally in your browser
- The extension functions completely offline after installation

## Data Use
The stored Service URL Configuration is used solely to:
1. Redirect GitHub repository pages to your configured GitIngest service
2. Maintain your preferred GitIngest service setting between browser sessions

We do not:
- Process this data for any other purpose
- Share this data with any third parties
- Use this data for analytics or tracking
- Combine this data with other information
- Upload or transmit this data anywhere

## Data Storage and Security
- All configuration data is stored locally in your browser using the browser's built-in storage API
- Data never leaves your browser
- No external servers are involved in any operations
- No third-party analytics or tracking is implemented
- Data is stored securely within your browser's protected storage area

## Your Privacy Rights

### For All Users
- Access: View your stored configuration at any time through the extension popup
- Deletion: Clear your data through browser settings or by uninstalling the extension
- Modification: Update your configuration through the extension popup
- Portability: Export your browser data using built-in browser tools

### For European Users (GDPR)
Under the General Data Protection Regulation (GDPR), you have the following rights:
- Right to be informed: This policy provides transparent information about our data practices
- Right to access: View all your stored data through browser settings
- Right to rectification: Modify your configuration at any time
- Right to erasure: Remove all stored data by uninstalling the extension
- Right to restrict processing: Not applicable as we only store, not process your data
- Right to data portability: Export your data using browser tools
- Right to object: Not applicable as we don't process data for marketing or profiling
- Rights related to automated decision making: Not applicable as we don't make automated decisions

### For California Residents (CCPA)
Under the California Consumer Privacy Act (CCPA), you have the following rights:
- Right to know: This policy discloses all data collection and use
- Right to delete: Remove your data through browser settings or extension uninstallation
- Right to opt-out: Not applicable as we don't sell personal information
- Right to non-discrimination: We don't discriminate based on privacy choices

## Permissions

### GitHub.com Access
The extension requires access to GitHub.com (`*://*.github.com/*`) to:
- Detect repository pages
- Add the "Open in GitIngest" button
- Generate correct GitIngest service URLs

This access is used solely for enhancing the GitHub interface with GitIngest functionality and does not involve collecting or transmitting any data from GitHub pages.

### Redirect Functionality
The extension's core functionality is to redirect users from GitHub repository pages to GitIngest services:
- By default, redirects go to GitIngest.com
- Users can configure a custom GitIngest service URL
- The extension is not involved in and cannot access any data processing that occurs on these external services
- Users should review the privacy policies of their configured GitIngest services

### Storage Permission
Storage permission is used exclusively for:
- Storing your preferred GitIngest service URL
- Maintaining your configuration across browser sessions

## International Data Transfers
No data transfers occur as all data is stored locally in your browser.

## Children's Privacy
Our extension does not knowingly collect any personal information from children under 13 years of age.

## Changes to This Privacy Policy
We may update this privacy policy from time to time. Any changes will be reflected in this document with an updated version number. Significant changes will be communicated through our GitHub repository.

## Contact Information
If you have any questions about this privacy policy or our treatment of your data, please open an issue in our GitHub repository
```

### File: tailwind.config.ts
```ts
import type { Config } from 'tailwindcss'

export default {
  content: ["assets/**", "entrypoints/**", "components/**"],
  theme: {
    extend: {
      colors: {
        'custom-bg': '#fff4da',
        'custom-button': '#ffc480',
      },
      transitionProperty: {
        'spacing': 'margin, padding',
      },
    },
  },
  plugins: [],
} satisfies Config


```

### File: tsconfig.json
```json
{
  "extends": "./.wxt/tsconfig.json",
  "compilerOptions": {
    "allowImportingTsExtensions": true,
    "jsx": "react-jsx"
  }
}

```

### File: wxt.config.ts
```ts
import { defineConfig } from 'wxt';
import type { ConfigEnv } from "wxt";

// See https://wxt.dev/api/config.html
export default defineConfig({
  extensionApi: 'chrome',
  modules: ['@wxt-dev/module-react'],
  manifest: (env: ConfigEnv) => ({
    name: `GitIngest${(env.browser === 'firefox') ? ' - Turn any Git repo to LLM prompt' : ' - Turn any Git repo to a LLM-friendly prompt'}`,
    description: 'Turn any Git repository into a prompt-friendly text ingest for LLMs. By replacing hub with ingest to access a coresponding digest.',
    permissions: ['storage'],
  })
});

```

