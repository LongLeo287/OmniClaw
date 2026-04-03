---
id: github.com-dathere-qsv-easy-windows-installer-d22d
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:43.461718
---

# KNOWLEDGE EXTRACT: github.com_dathere_qsv-easy-windows-installer_d22d8be1
> **Extracted on:** 2026-04-01 09:28:45
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520203/github.com_dathere_qsv-easy-windows-installer_d22d8be1

---

## File: `.gitignore`
```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
```

## File: `README.md`
```markdown
# qsv Easy installer for Windows

![image](https://github.com/user-attachments/assets/3ccc6cad-04ab-4288-9a41-9afadaa1fcfc)

This is a desktop app to help install the latest release of the [qsv](https://qsv.dathere.com) command-line tool for Windows devices to a a folder included in the user's `PATH`.

Built with Tauri.
```

## File: `bun.lock`
```
{
  "lockfileVersion": 1,
  "workspaces": {
    "": {
      "name": "qsv-installer",
      "dependencies": {
        "@tailwindcss/vite": "^4.1.3",
        "@tauri-apps/api": "^2",
        "@tauri-apps/plugin-opener": "^2",
        "lucide-react": "^0.487.0",
        "react": "^18.3.1",
        "react-dom": "^18.3.1",
        "tailwindcss": "^4.1.3",
      },
      "devDependencies": {
        "@tauri-apps/cli": "^2",
        "@types/react": "^18.3.1",
        "@types/react-dom": "^18.3.1",
        "@vitejs/plugin-react": "^4.3.4",
        "typescript": "~5.6.2",
        "vite": "^6.0.3",
      },
    },
  },
  "packages": {
    "@ampproject/remapping": ["@ampproject/remapping@2.3.0", "", { "dependencies": { "@jridgewell/gen-mapping": "^0.3.5", "@jridgewell/trace-mapping": "^0.3.24" } }, "sha512-30iZtAPgz+LTIYoeivqYo853f02jBYSd5uGnGpkFV0M3xOt9aN73erkgYAmZU43x4VfqcnLxW9Kpg3R5LC4YYw=="],

    "@babel/code-frame": ["@babel/code-frame@7.26.2", "", { "dependencies": { "@babel/helper-validator-identifier": "^7.25.9", "js-tokens": "^4.0.0", "picocolors": "^1.0.0" } }, "sha512-RJlIHRueQgwWitWgF8OdFYGZX328Ax5BCemNGlqHfplnRT9ESi8JkFlvaVYbS+UubVY6dpv87Fs2u5M29iNFVQ=="],

    "@babel/compat-data": ["@babel/compat-data@7.26.8", "", {}, "sha512-oH5UPLMWR3L2wEFLnFJ1TZXqHufiTKAiLfqw5zkhS4dKXLJ10yVztfil/twG8EDTA4F/tvVNw9nOl4ZMslB8rQ=="],

    "@babel/core": ["@babel/core@7.26.10", "", { "dependencies": { "@ampproject/remapping": "^2.2.0", "@babel/code-frame": "^7.26.2", "@babel/generator": "^7.26.10", "@babel/helper-compilation-targets": "^7.26.5", "@babel/helper-module-transforms": "^7.26.0", "@babel/helpers": "^7.26.10", "@babel/parser": "^7.26.10", "@babel/template": "^7.26.9", "@babel/traverse": "^7.26.10", "@babel/types": "^7.26.10", "convert-source-map": "^2.0.0", "debug": "^4.1.0", "gensync": "^1.0.0-beta.2", "json5": "^2.2.3", "semver": "^6.3.1" } }, "sha512-vMqyb7XCDMPvJFFOaT9kxtiRh42GwlZEg1/uIgtZshS5a/8OaduUfCi7kynKgc3Tw/6Uo2D+db9qBttghhmxwQ=="],

    "@babel/generator": ["@babel/generator@7.27.0", "", { "dependencies": { "@babel/parser": "^7.27.0", "@babel/types": "^7.27.0", "@jridgewell/gen-mapping": "^0.3.5", "@jridgewell/trace-mapping": "^0.3.25", "jsesc": "^3.0.2" } }, "sha512-VybsKvpiN1gU1sdMZIp7FcqphVVKEwcuj02x73uvcHE0PTihx1nlBcowYWhDwjpoAXRv43+gDzyggGnn1XZhVw=="],

    "@babel/helper-compilation-targets": ["@babel/helper-compilation-targets@7.27.0", "", { "dependencies": { "@babel/compat-data": "^7.26.8", "@babel/helper-validator-option": "^7.25.9", "browserslist": "^4.24.0", "lru-cache": "^5.1.1", "semver": "^6.3.1" } }, "sha512-LVk7fbXml0H2xH34dFzKQ7TDZ2G4/rVTOrq9V+icbbadjbVxxeFeDsNHv2SrZeWoA+6ZiTyWYWtScEIW07EAcA=="],

    "@babel/helper-module-imports": ["@babel/helper-module-imports@7.25.9", "", { "dependencies": { "@babel/traverse": "^7.25.9", "@babel/types": "^7.25.9" } }, "sha512-tnUA4RsrmflIM6W6RFTLFSXITtl0wKjgpnLgXyowocVPrbYrLUXSBXDgTs8BlbmIzIdlBySRQjINYs2BAkiLtw=="],

    "@babel/helper-module-transforms": ["@babel/helper-module-transforms@7.26.0", "", { "dependencies": { "@babel/helper-module-imports": "^7.25.9", "@babel/helper-validator-identifier": "^7.25.9", "@babel/traverse": "^7.25.9" }, "peerDependencies": { "@babel/core": "^7.0.0" } }, "sha512-xO+xu6B5K2czEnQye6BHA7DolFFmS3LB7stHZFaOLb1pAwO1HWLS8fXA+eh0A2yIvltPVmx3eNNDBJA2SLHXFw=="],

    "@babel/helper-plugin-utils": ["@babel/helper-plugin-utils@7.26.5", "", {}, "sha512-RS+jZcRdZdRFzMyr+wcsaqOmld1/EqTghfaBGQQd/WnRdzdlvSZ//kF7U8VQTxf1ynZ4cjUcYgjVGx13ewNPMg=="],

    "@babel/helper-string-parser": ["@babel/helper-string-parser@7.25.9", "", {}, "sha512-4A/SCr/2KLd5jrtOMFzaKjVtAei3+2r/NChoBNoZ3EyP/+GlhoaEGoWOZUmFmoITP7zOJyHIMm+DYRd8o3PvHA=="],

    "@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.25.9", "", {}, "sha512-Ed61U6XJc3CVRfkERJWDz4dJwKe7iLmmJsbOGu9wSloNSFttHV0I8g6UAgb7qnK5ly5bGLPd4oXZlxCdANBOWQ=="],

    "@babel/helper-validator-option": ["@babel/helper-validator-option@7.25.9", "", {}, "sha512-e/zv1co8pp55dNdEcCynfj9X7nyUKUXoUEwfXqaZt0omVOmDe9oOTdKStH4GmAw6zxMFs50ZayuMfHDKlO7Tfw=="],

    "@babel/helpers": ["@babel/helpers@7.27.0", "", { "dependencies": { "@babel/template": "^7.27.0", "@babel/types": "^7.27.0" } }, "sha512-U5eyP/CTFPuNE3qk+WZMxFkp/4zUzdceQlfzf7DdGdhp+Fezd7HD+i8Y24ZuTMKX3wQBld449jijbGq6OdGNQg=="],

    "@babel/parser": ["@babel/parser@7.27.0", "", { "dependencies": { "@babel/types": "^7.27.0" }, "bin": "./bin/babel-parser.js" }, "sha512-iaepho73/2Pz7w2eMS0Q5f83+0RKI7i4xmiYeBmDzfRVbQtTOG7Ts0S4HzJVsTMGI9keU8rNfuZr8DKfSt7Yyg=="],

    "@babel/plugin-transform-react-jsx-self": ["@babel/plugin-transform-react-jsx-self@7.25.9", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.25.9" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-y8quW6p0WHkEhmErnfe58r7x0A70uKphQm8Sp8cV7tjNQwK56sNVK0M73LK3WuYmsuyrftut4xAkjjgU0twaMg=="],

    "@babel/plugin-transform-react-jsx-source": ["@babel/plugin-transform-react-jsx-source@7.25.9", "", { "dependencies": { "@babel/helper-plugin-utils": "^7.25.9" }, "peerDependencies": { "@babel/core": "^7.0.0-0" } }, "sha512-+iqjT8xmXhhYv4/uiYd8FNQsraMFZIfxVSqxxVSZP0WbbSAWvBXAul0m/zu+7Vv4O/3WtApy9pmaTMiumEZgfg=="],

    "@babel/template": ["@babel/template@7.27.0", "", { "dependencies": { "@babel/code-frame": "^7.26.2", "@babel/parser": "^7.27.0", "@babel/types": "^7.27.0" } }, "sha512-2ncevenBqXI6qRMukPlXwHKHchC7RyMuu4xv5JBXRfOGVcTy1mXCD12qrp7Jsoxll1EV3+9sE4GugBVRjT2jFA=="],

    "@babel/traverse": ["@babel/traverse@7.27.0", "", { "dependencies": { "@babel/code-frame": "^7.26.2", "@babel/generator": "^7.27.0", "@babel/parser": "^7.27.0", "@babel/template": "^7.27.0", "@babel/types": "^7.27.0", "debug": "^4.3.1", "globals": "^11.1.0" } }, "sha512-19lYZFzYVQkkHkl4Cy4WrAVcqBkgvV2YM2TU3xG6DIwO7O3ecbDPfW3yM3bjAGcqcQHi+CCtjMR3dIEHxsd6bA=="],

    "@babel/types": ["@babel/types@7.27.0", "", { "dependencies": { "@babel/helper-string-parser": "^7.25.9", "@babel/helper-validator-identifier": "^7.25.9" } }, "sha512-H45s8fVLYjbhFH62dIJ3WtmJ6RSPt/3DRO0ZcT2SUiYiQyz3BLVb9ADEnLl91m74aQPS3AzzeajZHYOalWe3bg=="],

    "@esbuild/aix-ppc64": ["@esbuild/aix-ppc64@0.25.2", "", { "os": "aix", "cpu": "ppc64" }, "sha512-wCIboOL2yXZym2cgm6mlA742s9QeJ8DjGVaL39dLN4rRwrOgOyYSnOaFPhKZGLb2ngj4EyfAFjsNJwPXZvseag=="],

    "@esbuild/android-arm": ["@esbuild/android-arm@0.25.2", "", { "os": "android", "cpu": "arm" }, "sha512-NQhH7jFstVY5x8CKbcfa166GoV0EFkaPkCKBQkdPJFvo5u+nGXLEH/ooniLb3QI8Fk58YAx7nsPLozUWfCBOJA=="],

    "@esbuild/android-arm64": ["@esbuild/android-arm64@0.25.2", "", { "os": "android", "cpu": "arm64" }, "sha512-5ZAX5xOmTligeBaeNEPnPaeEuah53Id2tX4c2CVP3JaROTH+j4fnfHCkr1PjXMd78hMst+TlkfKcW/DlTq0i4w=="],

    "@esbuild/android-x64": ["@esbuild/android-x64@0.25.2", "", { "os": "android", "cpu": "x64" }, "sha512-Ffcx+nnma8Sge4jzddPHCZVRvIfQ0kMsUsCMcJRHkGJ1cDmhe4SsrYIjLUKn1xpHZybmOqCWwB0zQvsjdEHtkg=="],

    "@esbuild/darwin-arm64": ["@esbuild/darwin-arm64@0.25.2", "", { "os": "darwin", "cpu": "arm64" }, "sha512-MpM6LUVTXAzOvN4KbjzU/q5smzryuoNjlriAIx+06RpecwCkL9JpenNzpKd2YMzLJFOdPqBpuub6eVRP5IgiSA=="],

    "@esbuild/darwin-x64": ["@esbuild/darwin-x64@0.25.2", "", { "os": "darwin", "cpu": "x64" }, "sha512-5eRPrTX7wFyuWe8FqEFPG2cU0+butQQVNcT4sVipqjLYQjjh8a8+vUTfgBKM88ObB85ahsnTwF7PSIt6PG+QkA=="],

    "@esbuild/freebsd-arm64": ["@esbuild/freebsd-arm64@0.25.2", "", { "os": "freebsd", "cpu": "arm64" }, "sha512-mLwm4vXKiQ2UTSX4+ImyiPdiHjiZhIaE9QvC7sw0tZ6HoNMjYAqQpGyui5VRIi5sGd+uWq940gdCbY3VLvsO1w=="],

    "@esbuild/freebsd-x64": ["@esbuild/freebsd-x64@0.25.2", "", { "os": "freebsd", "cpu": "x64" }, "sha512-6qyyn6TjayJSwGpm8J9QYYGQcRgc90nmfdUb0O7pp1s4lTY+9D0H9O02v5JqGApUyiHOtkz6+1hZNvNtEhbwRQ=="],

    "@esbuild/linux-arm": ["@esbuild/linux-arm@0.25.2", "", { "os": "linux", "cpu": "arm" }, "sha512-UHBRgJcmjJv5oeQF8EpTRZs/1knq6loLxTsjc3nxO9eXAPDLcWW55flrMVc97qFPbmZP31ta1AZVUKQzKTzb0g=="],

    "@esbuild/linux-arm64": ["@esbuild/linux-arm64@0.25.2", "", { "os": "linux", "cpu": "arm64" }, "sha512-gq/sjLsOyMT19I8obBISvhoYiZIAaGF8JpeXu1u8yPv8BE5HlWYobmlsfijFIZ9hIVGYkbdFhEqC0NvM4kNO0g=="],

    "@esbuild/linux-ia32": ["@esbuild/linux-ia32@0.25.2", "", { "os": "linux", "cpu": "ia32" }, "sha512-bBYCv9obgW2cBP+2ZWfjYTU+f5cxRoGGQ5SeDbYdFCAZpYWrfjjfYwvUpP8MlKbP0nwZ5gyOU/0aUzZ5HWPuvQ=="],

    "@esbuild/linux-loong64": ["@esbuild/linux-loong64@0.25.2", "", { "os": "linux", "cpu": "none" }, "sha512-SHNGiKtvnU2dBlM5D8CXRFdd+6etgZ9dXfaPCeJtz+37PIUlixvlIhI23L5khKXs3DIzAn9V8v+qb1TRKrgT5w=="],

    "@esbuild/linux-mips64el": ["@esbuild/linux-mips64el@0.25.2", "", { "os": "linux", "cpu": "none" }, "sha512-hDDRlzE6rPeoj+5fsADqdUZl1OzqDYow4TB4Y/3PlKBD0ph1e6uPHzIQcv2Z65u2K0kpeByIyAjCmjn1hJgG0Q=="],

    "@esbuild/linux-ppc64": ["@esbuild/linux-ppc64@0.25.2", "", { "os": "linux", "cpu": "ppc64" }, "sha512-tsHu2RRSWzipmUi9UBDEzc0nLc4HtpZEI5Ba+Omms5456x5WaNuiG3u7xh5AO6sipnJ9r4cRWQB2tUjPyIkc6g=="],

    "@esbuild/linux-riscv64": ["@esbuild/linux-riscv64@0.25.2", "", { "os": "linux", "cpu": "none" }, "sha512-k4LtpgV7NJQOml/10uPU0s4SAXGnowi5qBSjaLWMojNCUICNu7TshqHLAEbkBdAszL5TabfvQ48kK84hyFzjnw=="],

    "@esbuild/linux-s390x": ["@esbuild/linux-s390x@0.25.2", "", { "os": "linux", "cpu": "s390x" }, "sha512-GRa4IshOdvKY7M/rDpRR3gkiTNp34M0eLTaC1a08gNrh4u488aPhuZOCpkF6+2wl3zAN7L7XIpOFBhnaE3/Q8Q=="],

    "@esbuild/linux-x64": ["@esbuild/linux-x64@0.25.2", "", { "os": "linux", "cpu": "x64" }, "sha512-QInHERlqpTTZ4FRB0fROQWXcYRD64lAoiegezDunLpalZMjcUcld3YzZmVJ2H/Cp0wJRZ8Xtjtj0cEHhYc/uUg=="],

    "@esbuild/netbsd-arm64": ["@esbuild/netbsd-arm64@0.25.2", "", { "os": "none", "cpu": "arm64" }, "sha512-talAIBoY5M8vHc6EeI2WW9d/CkiO9MQJ0IOWX8hrLhxGbro/vBXJvaQXefW2cP0z0nQVTdQ/eNyGFV1GSKrxfw=="],

    "@esbuild/netbsd-x64": ["@esbuild/netbsd-x64@0.25.2", "", { "os": "none", "cpu": "x64" }, "sha512-voZT9Z+tpOxrvfKFyfDYPc4DO4rk06qamv1a/fkuzHpiVBMOhpjK+vBmWM8J1eiB3OLSMFYNaOaBNLXGChf5tg=="],

    "@esbuild/openbsd-arm64": ["@esbuild/openbsd-arm64@0.25.2", "", { "os": "openbsd", "cpu": "arm64" }, "sha512-dcXYOC6NXOqcykeDlwId9kB6OkPUxOEqU+rkrYVqJbK2hagWOMrsTGsMr8+rW02M+d5Op5NNlgMmjzecaRf7Tg=="],

    "@esbuild/openbsd-x64": ["@esbuild/openbsd-x64@0.25.2", "", { "os": "openbsd", "cpu": "x64" }, "sha512-t/TkWwahkH0Tsgoq1Ju7QfgGhArkGLkF1uYz8nQS/PPFlXbP5YgRpqQR3ARRiC2iXoLTWFxc6DJMSK10dVXluw=="],

    "@esbuild/sunos-x64": ["@esbuild/sunos-x64@0.25.2", "", { "os": "sunos", "cpu": "x64" }, "sha512-cfZH1co2+imVdWCjd+D1gf9NjkchVhhdpgb1q5y6Hcv9TP6Zi9ZG/beI3ig8TvwT9lH9dlxLq5MQBBgwuj4xvA=="],

    "@esbuild/win32-arm64": ["@esbuild/win32-arm64@0.25.2", "", { "os": "win32", "cpu": "arm64" }, "sha512-7Loyjh+D/Nx/sOTzV8vfbB3GJuHdOQyrOryFdZvPHLf42Tk9ivBU5Aedi7iyX+x6rbn2Mh68T4qq1SDqJBQO5Q=="],

    "@esbuild/win32-ia32": ["@esbuild/win32-ia32@0.25.2", "", { "os": "win32", "cpu": "ia32" }, "sha512-WRJgsz9un0nqZJ4MfhabxaD9Ft8KioqU3JMinOTvobbX6MOSUigSBlogP8QB3uxpJDsFS6yN+3FDBdqE5lg9kg=="],

    "@esbuild/win32-x64": ["@esbuild/win32-x64@0.25.2", "", { "os": "win32", "cpu": "x64" }, "sha512-kM3HKb16VIXZyIeVrM1ygYmZBKybX8N4p754bw390wGO3Tf2j4L2/WYL+4suWujpgf6GBYs3jv7TyUivdd05JA=="],

    "@jridgewell/gen-mapping": ["@jridgewell/gen-mapping@0.3.8", "", { "dependencies": { "@jridgewell/set-array": "^1.2.1", "@jridgewell/sourcemap-codec": "^1.4.10", "@jridgewell/trace-mapping": "^0.3.24" } }, "sha512-imAbBGkb+ebQyxKgzv5Hu2nmROxoDOXHh80evxdoXNOrvAnVx7zimzc1Oo5h9RlfV4vPXaE2iM5pOFbvOCClWA=="],

    "@jridgewell/resolve-uri": ["@jridgewell/resolve-uri@3.1.2", "", {}, "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw=="],

    "@jridgewell/set-array": ["@jridgewell/set-array@1.2.1", "", {}, "sha512-R8gLRTZeyp03ymzP/6Lil/28tGeGEzhx1q2k703KGWRAI1VdvPIXdG70VJc2pAMw3NA6JKL5hhFu1sJX0Mnn/A=="],

    "@jridgewell/sourcemap-codec": ["@jridgewell/sourcemap-codec@1.5.0", "", {}, "sha512-gv3ZRaISU3fjPAgNsriBRqGWQL6quFx04YMPW/zD8XMLsU32mhCCbfbO6KZFLjvYpCZ8zyDEgqsgf+PwPaM7GQ=="],

    "@jridgewell/trace-mapping": ["@jridgewell/trace-mapping@0.3.25", "", { "dependencies": { "@jridgewell/resolve-uri": "^3.1.0", "@jridgewell/sourcemap-codec": "^1.4.14" } }, "sha512-vNk6aEwybGtawWmy/PzwnGDOjCkLWSD2wqvjGGAgOAwCGWySYXfYoxt00IJkTF+8Lb57DwOb3Aa0o9CApepiYQ=="],

    "@rollup/rollup-android-arm-eabi": ["@rollup/rollup-android-arm-eabi@4.39.0", "", { "os": "android", "cpu": "arm" }, "sha512-lGVys55Qb00Wvh8DMAocp5kIcaNzEFTmGhfFd88LfaogYTRKrdxgtlO5H6S49v2Nd8R2C6wLOal0qv6/kCkOwA=="],

    "@rollup/rollup-android-arm64": ["@rollup/rollup-android-arm64@4.39.0", "", { "os": "android", "cpu": "arm64" }, "sha512-It9+M1zE31KWfqh/0cJLrrsCPiF72PoJjIChLX+rEcujVRCb4NLQ5QzFkzIZW8Kn8FTbvGQBY5TkKBau3S8cCQ=="],

    "@rollup/rollup-darwin-arm64": ["@rollup/rollup-darwin-arm64@4.39.0", "", { "os": "darwin", "cpu": "arm64" }, "sha512-lXQnhpFDOKDXiGxsU9/l8UEGGM65comrQuZ+lDcGUx+9YQ9dKpF3rSEGepyeR5AHZ0b5RgiligsBhWZfSSQh8Q=="],

    "@rollup/rollup-darwin-x64": ["@rollup/rollup-darwin-x64@4.39.0", "", { "os": "darwin", "cpu": "x64" }, "sha512-mKXpNZLvtEbgu6WCkNij7CGycdw9cJi2k9v0noMb++Vab12GZjFgUXD69ilAbBh034Zwn95c2PNSz9xM7KYEAQ=="],

    "@rollup/rollup-freebsd-arm64": ["@rollup/rollup-freebsd-arm64@4.39.0", "", { "os": "freebsd", "cpu": "arm64" }, "sha512-jivRRlh2Lod/KvDZx2zUR+I4iBfHcu2V/BA2vasUtdtTN2Uk3jfcZczLa81ESHZHPHy4ih3T/W5rPFZ/hX7RtQ=="],

    "@rollup/rollup-freebsd-x64": ["@rollup/rollup-freebsd-x64@4.39.0", "", { "os": "freebsd", "cpu": "x64" }, "sha512-8RXIWvYIRK9nO+bhVz8DwLBepcptw633gv/QT4015CpJ0Ht8punmoHU/DuEd3iw9Hr8UwUV+t+VNNuZIWYeY7Q=="],

    "@rollup/rollup-linux-arm-gnueabihf": ["@rollup/rollup-linux-arm-gnueabihf@4.39.0", "", { "os": "linux", "cpu": "arm" }, "sha512-mz5POx5Zu58f2xAG5RaRRhp3IZDK7zXGk5sdEDj4o96HeaXhlUwmLFzNlc4hCQi5sGdR12VDgEUqVSHer0lI9g=="],

    "@rollup/rollup-linux-arm-musleabihf": ["@rollup/rollup-linux-arm-musleabihf@4.39.0", "", { "os": "linux", "cpu": "arm" }, "sha512-+YDwhM6gUAyakl0CD+bMFpdmwIoRDzZYaTWV3SDRBGkMU/VpIBYXXEvkEcTagw/7VVkL2vA29zU4UVy1mP0/Yw=="],

    "@rollup/rollup-linux-arm64-gnu": ["@rollup/rollup-linux-arm64-gnu@4.39.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-EKf7iF7aK36eEChvlgxGnk7pdJfzfQbNvGV/+l98iiMwU23MwvmV0Ty3pJ0p5WQfm3JRHOytSIqD9LB7Bq7xdQ=="],

    "@rollup/rollup-linux-arm64-musl": ["@rollup/rollup-linux-arm64-musl@4.39.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-vYanR6MtqC7Z2SNr8gzVnzUul09Wi1kZqJaek3KcIlI/wq5Xtq4ZPIZ0Mr/st/sv/NnaPwy/D4yXg5x0B3aUUA=="],

    "@rollup/rollup-linux-loongarch64-gnu": ["@rollup/rollup-linux-loongarch64-gnu@4.39.0", "", { "os": "linux", "cpu": "none" }, "sha512-NMRUT40+h0FBa5fb+cpxtZoGAggRem16ocVKIv5gDB5uLDgBIwrIsXlGqYbLwW8YyO3WVTk1FkFDjMETYlDqiw=="],

    "@rollup/rollup-linux-powerpc64le-gnu": ["@rollup/rollup-linux-powerpc64le-gnu@4.39.0", "", { "os": "linux", "cpu": "ppc64" }, "sha512-0pCNnmxgduJ3YRt+D+kJ6Ai/r+TaePu9ZLENl+ZDV/CdVczXl95CbIiwwswu4L+K7uOIGf6tMo2vm8uadRaICQ=="],

    "@rollup/rollup-linux-riscv64-gnu": ["@rollup/rollup-linux-riscv64-gnu@4.39.0", "", { "os": "linux", "cpu": "none" }, "sha512-t7j5Zhr7S4bBtksT73bO6c3Qa2AV/HqiGlj9+KB3gNF5upcVkx+HLgxTm8DK4OkzsOYqbdqbLKwvGMhylJCPhQ=="],

    "@rollup/rollup-linux-riscv64-musl": ["@rollup/rollup-linux-riscv64-musl@4.39.0", "", { "os": "linux", "cpu": "none" }, "sha512-m6cwI86IvQ7M93MQ2RF5SP8tUjD39Y7rjb1qjHgYh28uAPVU8+k/xYWvxRO3/tBN2pZkSMa5RjnPuUIbrwVxeA=="],

    "@rollup/rollup-linux-s390x-gnu": ["@rollup/rollup-linux-s390x-gnu@4.39.0", "", { "os": "linux", "cpu": "s390x" }, "sha512-iRDJd2ebMunnk2rsSBYlsptCyuINvxUfGwOUldjv5M4tpa93K8tFMeYGpNk2+Nxl+OBJnBzy2/JCscGeO507kA=="],

    "@rollup/rollup-linux-x64-gnu": ["@rollup/rollup-linux-x64-gnu@4.39.0", "", { "os": "linux", "cpu": "x64" }, "sha512-t9jqYw27R6Lx0XKfEFe5vUeEJ5pF3SGIM6gTfONSMb7DuG6z6wfj2yjcoZxHg129veTqU7+wOhY6GX8wmf90dA=="],

    "@rollup/rollup-linux-x64-musl": ["@rollup/rollup-linux-x64-musl@4.39.0", "", { "os": "linux", "cpu": "x64" }, "sha512-ThFdkrFDP55AIsIZDKSBWEt/JcWlCzydbZHinZ0F/r1h83qbGeenCt/G/wG2O0reuENDD2tawfAj2s8VK7Bugg=="],

    "@rollup/rollup-win32-arm64-msvc": ["@rollup/rollup-win32-arm64-msvc@4.39.0", "", { "os": "win32", "cpu": "arm64" }, "sha512-jDrLm6yUtbOg2TYB3sBF3acUnAwsIksEYjLeHL+TJv9jg+TmTwdyjnDex27jqEMakNKf3RwwPahDIt7QXCSqRQ=="],

    "@rollup/rollup-win32-ia32-msvc": ["@rollup/rollup-win32-ia32-msvc@4.39.0", "", { "os": "win32", "cpu": "ia32" }, "sha512-6w9uMuza+LbLCVoNKL5FSLE7yvYkq9laSd09bwS0tMjkwXrmib/4KmoJcrKhLWHvw19mwU+33ndC69T7weNNjQ=="],

    "@rollup/rollup-win32-x64-msvc": ["@rollup/rollup-win32-x64-msvc@4.39.0", "", { "os": "win32", "cpu": "x64" }, "sha512-yAkUOkIKZlK5dl7u6dg897doBgLXmUHhIINM2c+sND3DZwnrdQkkSiDh7N75Ll4mM4dxSkYfXqU9fW3lLkMFug=="],

    "@tailwindcss/node": ["@tailwindcss/node@4.1.4", "", { "dependencies": { "enhanced-resolve": "^5.18.1", "jiti": "^2.4.2", "lightningcss": "1.29.2", "tailwindcss": "4.1.4" } }, "sha512-MT5118zaiO6x6hNA04OWInuAiP1YISXql8Z+/Y8iisV5nuhM8VXlyhRuqc2PEviPszcXI66W44bCIk500Oolhw=="],

    "@tailwindcss/oxide": ["@tailwindcss/oxide@4.1.4", "", { "optionalDependencies": { "@tailwindcss/oxide-android-arm64": "4.1.4", "@tailwindcss/oxide-darwin-arm64": "4.1.4", "@tailwindcss/oxide-darwin-x64": "4.1.4", "@tailwindcss/oxide-freebsd-x64": "4.1.4", "@tailwindcss/oxide-linux-arm-gnueabihf": "4.1.4", "@tailwindcss/oxide-linux-arm64-gnu": "4.1.4", "@tailwindcss/oxide-linux-arm64-musl": "4.1.4", "@tailwindcss/oxide-linux-x64-gnu": "4.1.4", "@tailwindcss/oxide-linux-x64-musl": "4.1.4", "@tailwindcss/oxide-wasm32-wasi": "4.1.4", "@tailwindcss/oxide-win32-arm64-msvc": "4.1.4", "@tailwindcss/oxide-win32-x64-msvc": "4.1.4" } }, "sha512-p5wOpXyOJx7mKh5MXh5oKk+kqcz8T+bA3z/5VWWeQwFrmuBItGwz8Y2CHk/sJ+dNb9B0nYFfn0rj/cKHZyjahQ=="],

    "@tailwindcss/oxide-android-arm64": ["@tailwindcss/oxide-android-arm64@4.1.4", "", { "os": "android", "cpu": "arm64" }, "sha512-xMMAe/SaCN/vHfQYui3fqaBDEXMu22BVwQ33veLc8ep+DNy7CWN52L+TTG9y1K397w9nkzv+Mw+mZWISiqhmlA=="],

    "@tailwindcss/oxide-darwin-arm64": ["@tailwindcss/oxide-darwin-arm64@4.1.4", "", { "os": "darwin", "cpu": "arm64" }, "sha512-JGRj0SYFuDuAGilWFBlshcexev2hOKfNkoX+0QTksKYq2zgF9VY/vVMq9m8IObYnLna0Xlg+ytCi2FN2rOL0Sg=="],

    "@tailwindcss/oxide-darwin-x64": ["@tailwindcss/oxide-darwin-x64@4.1.4", "", { "os": "darwin", "cpu": "x64" }, "sha512-sdDeLNvs3cYeWsEJ4H1DvjOzaGios4QbBTNLVLVs0XQ0V95bffT3+scptzYGPMjm7xv4+qMhCDrkHwhnUySEzA=="],

    "@tailwindcss/oxide-freebsd-x64": ["@tailwindcss/oxide-freebsd-x64@4.1.4", "", { "os": "freebsd", "cpu": "x64" }, "sha512-VHxAqxqdghM83HslPhRsNhHo91McsxRJaEnShJOMu8mHmEj9Ig7ToHJtDukkuLWLzLboh2XSjq/0zO6wgvykNA=="],

    "@tailwindcss/oxide-linux-arm-gnueabihf": ["@tailwindcss/oxide-linux-arm-gnueabihf@4.1.4", "", { "os": "linux", "cpu": "arm" }, "sha512-OTU/m/eV4gQKxy9r5acuesqaymyeSCnsx1cFto/I1WhPmi5HDxX1nkzb8KYBiwkHIGg7CTfo/AcGzoXAJBxLfg=="],

    "@tailwindcss/oxide-linux-arm64-gnu": ["@tailwindcss/oxide-linux-arm64-gnu@4.1.4", "", { "os": "linux", "cpu": "arm64" }, "sha512-hKlLNvbmUC6z5g/J4H+Zx7f7w15whSVImokLPmP6ff1QqTVE+TxUM9PGuNsjHvkvlHUtGTdDnOvGNSEUiXI1Ww=="],

    "@tailwindcss/oxide-linux-arm64-musl": ["@tailwindcss/oxide-linux-arm64-musl@4.1.4", "", { "os": "linux", "cpu": "arm64" }, "sha512-X3As2xhtgPTY/m5edUtddmZ8rCruvBvtxYLMw9OsZdH01L2gS2icsHRwxdU0dMItNfVmrBezueXZCHxVeeb7Aw=="],

    "@tailwindcss/oxide-linux-x64-gnu": ["@tailwindcss/oxide-linux-x64-gnu@4.1.4", "", { "os": "linux", "cpu": "x64" }, "sha512-2VG4DqhGaDSmYIu6C4ua2vSLXnJsb/C9liej7TuSO04NK+JJJgJucDUgmX6sn7Gw3Cs5ZJ9ZLrnI0QRDOjLfNQ=="],

    "@tailwindcss/oxide-linux-x64-musl": ["@tailwindcss/oxide-linux-x64-musl@4.1.4", "", { "os": "linux", "cpu": "x64" }, "sha512-v+mxVgH2kmur/X5Mdrz9m7TsoVjbdYQT0b4Z+dr+I4RvreCNXyCFELZL/DO0M1RsidZTrm6O1eMnV6zlgEzTMQ=="],

    "@tailwindcss/oxide-wasm32-wasi": ["@tailwindcss/oxide-wasm32-wasi@4.1.4", "", { "dependencies": { "@emnapi/core": "^1.4.0", "@emnapi/runtime": "^1.4.0", "@emnapi/wasi-threads": "^1.0.1", "@napi-rs/wasm-runtime": "^0.2.8", "@tybys/wasm-util": "^0.9.0", "tslib": "^2.8.0" }, "cpu": "none" }, "sha512-2TLe9ir+9esCf6Wm+lLWTMbgklIjiF0pbmDnwmhR9MksVOq+e8aP3TSsXySnBDDvTTVd/vKu1aNttEGj3P6l8Q=="],

    "@tailwindcss/oxide-win32-arm64-msvc": ["@tailwindcss/oxide-win32-arm64-msvc@4.1.4", "", { "os": "win32", "cpu": "arm64" }, "sha512-VlnhfilPlO0ltxW9/BgfLI5547PYzqBMPIzRrk4W7uupgCt8z6Trw/tAj6QUtF2om+1MH281Pg+HHUJoLesmng=="],

    "@tailwindcss/oxide-win32-x64-msvc": ["@tailwindcss/oxide-win32-x64-msvc@4.1.4", "", { "os": "win32", "cpu": "x64" }, "sha512-+7S63t5zhYjslUGb8NcgLpFXD+Kq1F/zt5Xv5qTv7HaFTG/DHyHD9GA6ieNAxhgyA4IcKa/zy7Xx4Oad2/wuhw=="],

    "@tailwindcss/vite": ["@tailwindcss/vite@4.1.4", "", { "dependencies": { "@tailwindcss/node": "4.1.4", "@tailwindcss/oxide": "4.1.4", "tailwindcss": "4.1.4" }, "peerDependencies": { "vite": "^5.2.0 || ^6" } }, "sha512-4UQeMrONbvrsXKXXp/uxmdEN5JIJ9RkH7YVzs6AMxC/KC1+Np7WZBaNIco7TEjlkthqxZbt8pU/ipD+hKjm80A=="],

    "@tauri-apps/api": ["@tauri-apps/api@2.5.0", "", {}, "sha512-Ldux4ip+HGAcPUmuLT8EIkk6yafl5vK0P0c0byzAKzxJh7vxelVtdPONjfgTm96PbN24yjZNESY8CKo8qniluA=="],

    "@tauri-apps/cli": ["@tauri-apps/cli@2.5.0", "", { "optionalDependencies": { "@tauri-apps/cli-darwin-arm64": "2.5.0", "@tauri-apps/cli-darwin-x64": "2.5.0", "@tauri-apps/cli-linux-arm-gnueabihf": "2.5.0", "@tauri-apps/cli-linux-arm64-gnu": "2.5.0", "@tauri-apps/cli-linux-arm64-musl": "2.5.0", "@tauri-apps/cli-linux-riscv64-gnu": "2.5.0", "@tauri-apps/cli-linux-x64-gnu": "2.5.0", "@tauri-apps/cli-linux-x64-musl": "2.5.0", "@tauri-apps/cli-win32-arm64-msvc": "2.5.0", "@tauri-apps/cli-win32-ia32-msvc": "2.5.0", "@tauri-apps/cli-win32-x64-msvc": "2.5.0" }, "bin": { "tauri": "tauri.js" } }, "sha512-rAtHqG0Gh/IWLjN2zTf3nZqYqbo81oMbqop56rGTjrlWk9pTTAjkqOjSL9XQLIMZ3RbeVjveCqqCA0s8RnLdMg=="],

    "@tauri-apps/cli-darwin-arm64": ["@tauri-apps/cli-darwin-arm64@2.5.0", "", { "os": "darwin", "cpu": "arm64" }, "sha512-VuVAeTFq86dfpoBDNYAdtQVLbP0+2EKCHIIhkaxjeoPARR0sLpFHz2zs0PcFU76e+KAaxtEtAJAXGNUc8E1PzQ=="],

    "@tauri-apps/cli-darwin-x64": ["@tauri-apps/cli-darwin-x64@2.5.0", "", { "os": "darwin", "cpu": "x64" }, "sha512-hUF01sC06cZVa8+I0/VtsHOk9BbO75rd+YdtHJ48xTdcYaQ5QIwL4yZz9OR1AKBTaUYhBam8UX9Pvd5V2/4Dpw=="],

    "@tauri-apps/cli-linux-arm-gnueabihf": ["@tauri-apps/cli-linux-arm-gnueabihf@2.5.0", "", { "os": "linux", "cpu": "arm" }, "sha512-LQKqttsK252LlqYyX8R02MinUsfFcy3+NZiJwHFgi5Y3+ZUIAED9cSxJkyNtuY5KMnR4RlpgWyLv4P6akN1xhg=="],

    "@tauri-apps/cli-linux-arm64-gnu": ["@tauri-apps/cli-linux-arm64-gnu@2.5.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-mTQufsPcpdHg5RW0zypazMo4L55EfeE5snTzrPqbLX4yCK2qalN7+rnP8O8GT06xhp6ElSP/Ku1M2MR297SByQ=="],

    "@tauri-apps/cli-linux-arm64-musl": ["@tauri-apps/cli-linux-arm64-musl@2.5.0", "", { "os": "linux", "cpu": "arm64" }, "sha512-rQO1HhRUQqyEaal5dUVOQruTRda/TD36s9kv1hTxZiFuSq3558lsTjAcUEnMAtBcBkps20sbyTJNMT0AwYIk8Q=="],

    "@tauri-apps/cli-linux-riscv64-gnu": ["@tauri-apps/cli-linux-riscv64-gnu@2.5.0", "", { "os": "linux", "cpu": "none" }, "sha512-7oS18FN46yDxyw1zX/AxhLAd7T3GrLj3Ai6s8hZKd9qFVzrAn36ESL7d3G05s8wEtsJf26qjXnVF4qleS3dYsA=="],

    "@tauri-apps/cli-linux-x64-gnu": ["@tauri-apps/cli-linux-x64-gnu@2.5.0", "", { "os": "linux", "cpu": "x64" }, "sha512-SG5sFNL7VMmDBdIg3nO3EzNRT306HsiEQ0N90ILe3ZABYAVoPDO/ttpCO37ApLInTzrq/DLN+gOlC/mgZvLw1w=="],

    "@tauri-apps/cli-linux-x64-musl": ["@tauri-apps/cli-linux-x64-musl@2.5.0", "", { "os": "linux", "cpu": "x64" }, "sha512-QXDM8zp/6v05PNWju5ELsVwF0VH1n6b5pk2E6W/jFbbiwz80Vs1lACl9pv5kEHkrxBj+aWU/03JzGuIj2g3SkQ=="],

    "@tauri-apps/cli-win32-arm64-msvc": ["@tauri-apps/cli-win32-arm64-msvc@2.5.0", "", { "os": "win32", "cpu": "arm64" }, "sha512-pFSHFK6b+o9y4Un8w0gGLwVyFTZaC3P0kQ7umRt/BLDkzD5RnQ4vBM7CF8BCU5nkwmEBUCZd7Wt3TWZxe41o6Q=="],

    "@tauri-apps/cli-win32-ia32-msvc": ["@tauri-apps/cli-win32-ia32-msvc@2.5.0", "", { "os": "win32", "cpu": "ia32" }, "sha512-EArv1IaRlogdLAQyGlKmEqZqm5RfHCUMhJoedWu7GtdbOMUfSAz6FMX2boE1PtEmNO4An+g188flLeVErrxEKg=="],

    "@tauri-apps/cli-win32-x64-msvc": ["@tauri-apps/cli-win32-x64-msvc@2.5.0", "", { "os": "win32", "cpu": "x64" }, "sha512-lj43EFYbnAta8pd9JnUq87o+xRUR0odz+4rixBtTUwUgdRdwQ2V9CzFtsMu6FQKpFQ6mujRK6P1IEwhL6ADRsQ=="],

    "@tauri-apps/plugin-opener": ["@tauri-apps/plugin-opener@2.2.6", "", { "dependencies": { "@tauri-apps/api": "^2.0.0" } }, "sha512-bSdkuP71ZQRepPOn8BOEdBKYJQvl6+jb160QtJX/i2H9BF6ZySY/kYljh76N2Ne5fJMQRge7rlKoStYQY5Jq1w=="],

    "@types/babel__core": ["@types/babel__core@7.20.5", "", { "dependencies": { "@babel/parser": "^7.20.7", "@babel/types": "^7.20.7", "@types/babel__generator": "*", "@types/babel__template": "*", "@types/babel__traverse": "*" } }, "sha512-qoQprZvz5wQFJwMDqeseRXWv3rqMvhgpbXFfVyWhbx9X47POIA6i/+dXefEmZKoAgOaTdaIgNSMqMIU61yRyzA=="],

    "@types/babel__generator": ["@types/babel__generator@7.27.0", "", { "dependencies": { "@babel/types": "^7.0.0" } }, "sha512-ufFd2Xi92OAVPYsy+P4n7/U7e68fex0+Ee8gSG9KX7eo084CWiQ4sdxktvdl0bOPupXtVJPY19zk6EwWqUQ8lg=="],

    "@types/babel__template": ["@types/babel__template@7.4.4", "", { "dependencies": { "@babel/parser": "^7.1.0", "@babel/types": "^7.0.0" } }, "sha512-h/NUaSyG5EyxBIp8YRxo4RMe2/qQgvyowRwVMzhYhBCONbW8PUsg4lkFMrhgZhUe5z3L3MiLDuvyJ/CaPa2A8A=="],

    "@types/babel__traverse": ["@types/babel__traverse@7.20.7", "", { "dependencies": { "@babel/types": "^7.20.7" } }, "sha512-dkO5fhS7+/oos4ciWxyEyjWe48zmG6wbCheo/G2ZnHx4fs3EU6YC6UM8rk56gAjNJ9P3MTH2jo5jb92/K6wbng=="],

    "@types/estree": ["@types/estree@1.0.7", "", {}, "sha512-w28IoSUCJpidD/TGviZwwMJckNESJZXFu7NBZ5YJ4mEUnNraUn9Pm8HSZm/jDF1pDWYKspWE7oVphigUPRakIQ=="],

    "@types/prop-types": ["@types/prop-types@15.7.14", "", {}, "sha512-gNMvNH49DJ7OJYv+KAKn0Xp45p8PLl6zo2YnvDIbTd4J6MER2BmWN49TG7n9LvkyihINxeKW8+3bfS2yDC9dzQ=="],

    "@types/react": ["@types/react@18.3.20", "", { "dependencies": { "@types/prop-types": "*", "csstype": "^3.0.2" } }, "sha512-IPaCZN7PShZK/3t6Q87pfTkRm6oLTd4vztyoj+cbHUF1g3FfVb2tFIL79uCRKEfv16AhqDMBywP2VW3KIZUvcg=="],

    "@types/react-dom": ["@types/react-dom@18.3.6", "", { "peerDependencies": { "@types/react": "^18.0.0" } }, "sha512-nf22//wEbKXusP6E9pfOCDwFdHAX4u172eaJI4YkDRQEZiorm6KfYnSC2SWLDMVWUOWPERmJnN0ujeAfTBLvrw=="],

    "@vitejs/plugin-react": ["@vitejs/plugin-react@4.4.0", "", { "dependencies": { "@babel/core": "^7.26.10", "@babel/plugin-transform-react-jsx-self": "^7.25.9", "@babel/plugin-transform-react-jsx-source": "^7.25.9", "@types/babel__core": "^7.20.5", "react-refresh": "^0.17.0" }, "peerDependencies": { "vite": "^4.2.0 || ^5.0.0 || ^6.0.0" } }, "sha512-x/EztcTKVj+TDeANY1WjNeYsvZjZdfWRMP/KXi5Yn8BoTzpa13ZltaQqKfvWYbX8CE10GOHHdC5v86jY9x8i/g=="],

    "browserslist": ["browserslist@4.24.4", "", { "dependencies": { "caniuse-lite": "^1.0.30001688", "electron-to-chromium": "^1.5.73", "node-releases": "^2.0.19", "update-browserslist-db": "^1.1.1" }, "bin": { "browserslist": "cli.js" } }, "sha512-KDi1Ny1gSePi1vm0q4oxSF8b4DR44GF4BbmS2YdhPLOEqd8pDviZOGH/GsmRwoWJ2+5Lr085X7naowMwKHDG1A=="],

    "caniuse-lite": ["caniuse-lite@1.0.30001712", "", {}, "sha512-MBqPpGYYdQ7/hfKiet9SCI+nmN5/hp4ZzveOJubl5DTAMa5oggjAuoi0Z4onBpKPFI2ePGnQuQIzF3VxDjDJig=="],

    "convert-source-map": ["convert-source-map@2.0.0", "", {}, "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg=="],

    "csstype": ["csstype@3.1.3", "", {}, "sha512-M1uQkMl8rQK/szD0LNhtqxIPLpimGm8sOBwU7lLnCpSbTyY3yeU1Vc7l4KT5zT4s/yOxHH5O7tIuuLOCnLADRw=="],

    "debug": ["debug@4.4.0", "", { "dependencies": { "ms": "^2.1.3" } }, "sha512-6WTZ/IxCY/T6BALoZHaE4ctp9xm+Z5kY/pzYaCHRFeyVhojxlrm+46y68HA6hr0TcwEssoxNiDEUJQjfPZ/RYA=="],

    "detect-libc": ["detect-libc@2.0.3", "", {}, "sha512-bwy0MGW55bG41VqxxypOsdSdGqLwXPI/focwgTYCFMbdUiBAxLg9CFzG08sz2aqzknwiX7Hkl0bQENjg8iLByw=="],

    "electron-to-chromium": ["electron-to-chromium@1.5.134", "", {}, "sha512-zSwzrLg3jNP3bwsLqWHmS5z2nIOQ5ngMnfMZOWWtXnqqQkPVyOipxK98w+1beLw1TB+EImPNcG8wVP/cLVs2Og=="],

    "enhanced-resolve": ["enhanced-resolve@5.18.1", "", { "dependencies": { "graceful-fs": "^4.2.4", "tapable": "^2.2.0" } }, "sha512-ZSW3ma5GkcQBIpwZTSRAI8N71Uuwgs93IezB7mf7R60tC8ZbJideoDNKjHn2O9KIlx6rkGTTEk1xUCK2E1Y2Yg=="],

    "esbuild": ["esbuild@0.25.2", "", { "optionalDependencies": { "@esbuild/aix-ppc64": "0.25.2", "@esbuild/android-arm": "0.25.2", "@esbuild/android-arm64": "0.25.2", "@esbuild/android-x64": "0.25.2", "@esbuild/darwin-arm64": "0.25.2", "@esbuild/darwin-x64": "0.25.2", "@esbuild/freebsd-arm64": "0.25.2", "@esbuild/freebsd-x64": "0.25.2", "@esbuild/linux-arm": "0.25.2", "@esbuild/linux-arm64": "0.25.2", "@esbuild/linux-ia32": "0.25.2", "@esbuild/linux-loong64": "0.25.2", "@esbuild/linux-mips64el": "0.25.2", "@esbuild/linux-ppc64": "0.25.2", "@esbuild/linux-riscv64": "0.25.2", "@esbuild/linux-s390x": "0.25.2", "@esbuild/linux-x64": "0.25.2", "@esbuild/netbsd-arm64": "0.25.2", "@esbuild/netbsd-x64": "0.25.2", "@esbuild/openbsd-arm64": "0.25.2", "@esbuild/openbsd-x64": "0.25.2", "@esbuild/sunos-x64": "0.25.2", "@esbuild/win32-arm64": "0.25.2", "@esbuild/win32-ia32": "0.25.2", "@esbuild/win32-x64": "0.25.2" }, "bin": { "esbuild": "bin/esbuild" } }, "sha512-16854zccKPnC+toMywC+uKNeYSv+/eXkevRAfwRD/G9Cleq66m8XFIrigkbvauLLlCfDL45Q2cWegSg53gGBnQ=="],

    "escalade": ["escalade@3.2.0", "", {}, "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA=="],

    "fsevents": ["fsevents@2.3.3", "", { "os": "darwin" }, "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw=="],

    "gensync": ["gensync@1.0.0-beta.2", "", {}, "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg=="],

    "globals": ["globals@11.12.0", "", {}, "sha512-WOBp/EEGUiIsJSp7wcv/y6MO+lV9UoncWqxuFfm8eBwzWNgyfBd6Gz+IeKQ9jCmyhoH99g15M3T+QaVHFjizVA=="],

    "graceful-fs": ["graceful-fs@4.2.11", "", {}, "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ=="],

    "jiti": ["jiti@2.4.2", "", { "bin": { "jiti": "lib/jiti-cli.mjs" } }, "sha512-rg9zJN+G4n2nfJl5MW3BMygZX56zKPNVEYYqq7adpmMh4Jn2QNEwhvQlFy6jPVdcod7txZtKHWnyZiA3a0zP7A=="],

    "js-tokens": ["js-tokens@4.0.0", "", {}, "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ=="],

    "jsesc": ["jsesc@3.1.0", "", { "bin": { "jsesc": "bin/jsesc" } }, "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA=="],

    "json5": ["json5@2.2.3", "", { "bin": { "json5": "lib/cli.js" } }, "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg=="],

    "lightningcss": ["lightningcss@1.29.2", "", { "dependencies": { "detect-libc": "^2.0.3" }, "optionalDependencies": { "lightningcss-darwin-arm64": "1.29.2", "lightningcss-darwin-x64": "1.29.2", "lightningcss-freebsd-x64": "1.29.2", "lightningcss-linux-arm-gnueabihf": "1.29.2", "lightningcss-linux-arm64-gnu": "1.29.2", "lightningcss-linux-arm64-musl": "1.29.2", "lightningcss-linux-x64-gnu": "1.29.2", "lightningcss-linux-x64-musl": "1.29.2", "lightningcss-win32-arm64-msvc": "1.29.2", "lightningcss-win32-x64-msvc": "1.29.2" } }, "sha512-6b6gd/RUXKaw5keVdSEtqFVdzWnU5jMxTUjA2bVcMNPLwSQ08Sv/UodBVtETLCn7k4S1Ibxwh7k68IwLZPgKaA=="],

    "lightningcss-darwin-arm64": ["lightningcss-darwin-arm64@1.29.2", "", { "os": "darwin", "cpu": "arm64" }, "sha512-cK/eMabSViKn/PG8U/a7aCorpeKLMlK0bQeNHmdb7qUnBkNPnL+oV5DjJUo0kqWsJUapZsM4jCfYItbqBDvlcA=="],

    "lightningcss-darwin-x64": ["lightningcss-darwin-x64@1.29.2", "", { "os": "darwin", "cpu": "x64" }, "sha512-j5qYxamyQw4kDXX5hnnCKMf3mLlHvG44f24Qyi2965/Ycz829MYqjrVg2H8BidybHBp9kom4D7DR5VqCKDXS0w=="],

    "lightningcss-freebsd-x64": ["lightningcss-freebsd-x64@1.29.2", "", { "os": "freebsd", "cpu": "x64" }, "sha512-wDk7M2tM78Ii8ek9YjnY8MjV5f5JN2qNVO+/0BAGZRvXKtQrBC4/cn4ssQIpKIPP44YXw6gFdpUF+Ps+RGsCwg=="],

    "lightningcss-linux-arm-gnueabihf": ["lightningcss-linux-arm-gnueabihf@1.29.2", "", { "os": "linux", "cpu": "arm" }, "sha512-IRUrOrAF2Z+KExdExe3Rz7NSTuuJ2HvCGlMKoquK5pjvo2JY4Rybr+NrKnq0U0hZnx5AnGsuFHjGnNT14w26sg=="],

    "lightningcss-linux-arm64-gnu": ["lightningcss-linux-arm64-gnu@1.29.2", "", { "os": "linux", "cpu": "arm64" }, "sha512-KKCpOlmhdjvUTX/mBuaKemp0oeDIBBLFiU5Fnqxh1/DZ4JPZi4evEH7TKoSBFOSOV3J7iEmmBaw/8dpiUvRKlQ=="],

    "lightningcss-linux-arm64-musl": ["lightningcss-linux-arm64-musl@1.29.2", "", { "os": "linux", "cpu": "arm64" }, "sha512-Q64eM1bPlOOUgxFmoPUefqzY1yV3ctFPE6d/Vt7WzLW4rKTv7MyYNky+FWxRpLkNASTnKQUaiMJ87zNODIrrKQ=="],

    "lightningcss-linux-x64-gnu": ["lightningcss-linux-x64-gnu@1.29.2", "", { "os": "linux", "cpu": "x64" }, "sha512-0v6idDCPG6epLXtBH/RPkHvYx74CVziHo6TMYga8O2EiQApnUPZsbR9nFNrg2cgBzk1AYqEd95TlrsL7nYABQg=="],

    "lightningcss-linux-x64-musl": ["lightningcss-linux-x64-musl@1.29.2", "", { "os": "linux", "cpu": "x64" }, "sha512-rMpz2yawkgGT8RULc5S4WiZopVMOFWjiItBT7aSfDX4NQav6M44rhn5hjtkKzB+wMTRlLLqxkeYEtQ3dd9696w=="],

    "lightningcss-win32-arm64-msvc": ["lightningcss-win32-arm64-msvc@1.29.2", "", { "os": "win32", "cpu": "arm64" }, "sha512-nL7zRW6evGQqYVu/bKGK+zShyz8OVzsCotFgc7judbt6wnB2KbiKKJwBE4SGoDBQ1O94RjW4asrCjQL4i8Fhbw=="],

    "lightningcss-win32-x64-msvc": ["lightningcss-win32-x64-msvc@1.29.2", "", { "os": "win32", "cpu": "x64" }, "sha512-EdIUW3B2vLuHmv7urfzMI/h2fmlnOQBk1xlsDxkN1tCWKjNFjfLhGxYk8C8mzpSfr+A6jFFIi8fU6LbQGsRWjA=="],

    "loose-envify": ["loose-envify@1.4.0", "", { "dependencies": { "js-tokens": "^3.0.0 || ^4.0.0" }, "bin": { "loose-envify": "cli.js" } }, "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q=="],

    "lru-cache": ["lru-cache@5.1.1", "", { "dependencies": { "yallist": "^3.0.2" } }, "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w=="],

    "lucide-react": ["lucide-react@0.487.0", "", { "peerDependencies": { "react": "^16.5.1 || ^17.0.0 || ^18.0.0 || ^19.0.0" } }, "sha512-aKqhOQ+YmFnwq8dWgGjOuLc8V1R9/c/yOd+zDY4+ohsR2Jo05lSGc3WsstYPIzcTpeosN7LoCkLReUUITvaIvw=="],

    "ms": ["ms@2.1.3", "", {}, "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA=="],

    "nanoid": ["nanoid@3.3.11", "", { "bin": { "nanoid": "bin/nanoid.cjs" } }, "sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w=="],

    "node-releases": ["node-releases@2.0.19", "", {}, "sha512-xxOWJsBKtzAq7DY0J+DTzuz58K8e7sJbdgwkbMWQe8UYB6ekmsQ45q0M/tJDsGaZmbC+l7n57UV8Hl5tHxO9uw=="],

    "picocolors": ["picocolors@1.1.1", "", {}, "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA=="],

    "postcss": ["postcss@8.5.3", "", { "dependencies": { "nanoid": "^3.3.8", "picocolors": "^1.1.1", "source-map-js": "^1.2.1" } }, "sha512-dle9A3yYxlBSrt8Fu+IpjGT8SY8hN0mlaA6GY8t0P5PjIOZemULz/E2Bnm/2dcUOena75OTNkHI76uZBNUUq3A=="],

    "react": ["react@18.3.1", "", { "dependencies": { "loose-envify": "^1.1.0" } }, "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ=="],

    "react-dom": ["react-dom@18.3.1", "", { "dependencies": { "loose-envify": "^1.1.0", "scheduler": "^0.23.2" }, "peerDependencies": { "react": "^18.3.1" } }, "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw=="],

    "react-refresh": ["react-refresh@0.17.0", "", {}, "sha512-z6F7K9bV85EfseRCp2bzrpyQ0Gkw1uLoCel9XBVWPg/TjRj94SkJzUTGfOa4bs7iJvBWtQG0Wq7wnI0syw3EBQ=="],

    "rollup": ["rollup@4.39.0", "", { "dependencies": { "@types/estree": "1.0.7" }, "optionalDependencies": { "@rollup/rollup-android-arm-eabi": "4.39.0", "@rollup/rollup-android-arm64": "4.39.0", "@rollup/rollup-darwin-arm64": "4.39.0", "@rollup/rollup-darwin-x64": "4.39.0", "@rollup/rollup-freebsd-arm64": "4.39.0", "@rollup/rollup-freebsd-x64": "4.39.0", "@rollup/rollup-linux-arm-gnueabihf": "4.39.0", "@rollup/rollup-linux-arm-musleabihf": "4.39.0", "@rollup/rollup-linux-arm64-gnu": "4.39.0", "@rollup/rollup-linux-arm64-musl": "4.39.0", "@rollup/rollup-linux-loongarch64-gnu": "4.39.0", "@rollup/rollup-linux-powerpc64le-gnu": "4.39.0", "@rollup/rollup-linux-riscv64-gnu": "4.39.0", "@rollup/rollup-linux-riscv64-musl": "4.39.0", "@rollup/rollup-linux-s390x-gnu": "4.39.0", "@rollup/rollup-linux-x64-gnu": "4.39.0", "@rollup/rollup-linux-x64-musl": "4.39.0", "@rollup/rollup-win32-arm64-msvc": "4.39.0", "@rollup/rollup-win32-ia32-msvc": "4.39.0", "@rollup/rollup-win32-x64-msvc": "4.39.0", "fsevents": "~2.3.2" }, "bin": { "rollup": "dist/bin/rollup" } }, "sha512-thI8kNc02yNvnmJp8dr3fNWJ9tCONDhp6TV35X6HkKGGs9E6q7YWCHbe5vKiTa7TAiNcFEmXKj3X/pG2b3ci0g=="],

    "scheduler": ["scheduler@0.23.2", "", { "dependencies": { "loose-envify": "^1.1.0" } }, "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ=="],

    "semver": ["semver@6.3.1", "", { "bin": { "semver": "bin/semver.js" } }, "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA=="],

    "source-map-js": ["source-map-js@1.2.1", "", {}, "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA=="],

    "tailwindcss": ["tailwindcss@4.1.4", "", {}, "sha512-1ZIUqtPITFbv/DxRmDr5/agPqJwF69d24m9qmM1939TJehgY539CtzeZRjbLt5G6fSy/7YqqYsfvoTEw9xUI2A=="],

    "tapable": ["tapable@2.2.1", "", {}, "sha512-GNzQvQTOIP6RyTfE2Qxb8ZVlNmw0n88vp1szwWRimP02mnTsx3Wtn5qRdqY9w2XduFNUgvOwhNnQsjwCp+kqaQ=="],

    "typescript": ["typescript@5.6.3", "", { "bin": { "tsc": "bin/tsc", "tsserver": "bin/tsserver" } }, "sha512-hjcS1mhfuyi4WW8IWtjP7brDrG2cuDZukyrYrSauoXGNgx0S7zceP07adYkJycEr56BOUTNPzbInooiN3fn1qw=="],

    "update-browserslist-db": ["update-browserslist-db@1.1.3", "", { "dependencies": { "escalade": "^3.2.0", "picocolors": "^1.1.1" }, "peerDependencies": { "browserslist": ">= 4.21.0" }, "bin": { "update-browserslist-db": "cli.js" } }, "sha512-UxhIZQ+QInVdunkDAaiazvvT/+fXL5Osr0JZlJulepYu6Jd7qJtDZjlur0emRlT71EN3ScPoE7gvsuIKKNavKw=="],

    "vite": ["vite@6.2.6", "", { "dependencies": { "esbuild": "^0.25.0", "postcss": "^8.5.3", "rollup": "^4.30.1" }, "optionalDependencies": { "fsevents": "~2.3.3" }, "peerDependencies": { "@types/node": "^18.0.0 || ^20.0.0 || >=22.0.0", "jiti": ">=1.21.0", "less": "*", "lightningcss": "^1.21.0", "sass": "*", "sass-embedded": "*", "stylus": "*", "sugarss": "*", "terser": "^5.16.0", "tsx": "^4.8.1", "yaml": "^2.4.2" }, "optionalPeers": ["@types/node", "jiti", "less", "lightningcss", "sass", "sass-embedded", "stylus", "sugarss", "terser", "tsx", "yaml"], "bin": { "vite": "bin/vite.js" } }, "sha512-9xpjNl3kR4rVDZgPNdTL0/c6ao4km69a/2ihNQbcANz8RuCOK3hQBmLSJf3bRKVQjVMda+YvizNE8AwvogcPbw=="],

    "yallist": ["yallist@3.1.1", "", {}, "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g=="],

    "@tailwindcss/oxide-wasm32-wasi/@emnapi/core": ["@emnapi/core@1.4.3", "", { "dependencies": { "@emnapi/wasi-threads": "1.0.2", "tslib": "^2.4.0" }, "bundled": true }, "sha512-4m62DuCE07lw01soJwPiBGC0nAww0Q+RY70VZ+n49yDIO13yyinhbWCeNnaob0lakDtWQzSdtNWzJeOJt2ma+g=="],

    "@tailwindcss/oxide-wasm32-wasi/@emnapi/runtime": ["@emnapi/runtime@1.4.3", "", { "dependencies": { "tslib": "^2.4.0" }, "bundled": true }, "sha512-pBPWdu6MLKROBX05wSNKcNb++m5Er+KQ9QkB+WVM+pW2Kx9hoSrVTnu3BdkI5eBLZoKu/J6mW/B6i6bJB2ytXQ=="],

    "@tailwindcss/oxide-wasm32-wasi/@emnapi/wasi-threads": ["@emnapi/wasi-threads@1.0.2", "", { "dependencies": { "tslib": "^2.4.0" }, "bundled": true }, "sha512-5n3nTJblwRi8LlXkJ9eBzu+kZR8Yxcc7ubakyQTFzPMtIhFpUBRbsnc2Dv88IZDIbCDlBiWrknhB4Lsz7mg6BA=="],

    "@tailwindcss/oxide-wasm32-wasi/@napi-rs/wasm-runtime": ["@napi-rs/wasm-runtime@0.2.8", "", { "dependencies": { "@emnapi/core": "^1.4.0", "@emnapi/runtime": "^1.4.0", "@tybys/wasm-util": "^0.9.0" }, "bundled": true }, "sha512-OBlgKdX7gin7OIq4fadsjpg+cp2ZphvAIKucHsNfTdJiqdOmOEwQd/bHi0VwNrcw5xpBJyUw6cK/QilCqy1BSg=="],

    "@tailwindcss/oxide-wasm32-wasi/@tybys/wasm-util": ["@tybys/wasm-util@0.9.0", "", { "dependencies": { "tslib": "^2.4.0" }, "bundled": true }, "sha512-6+7nlbMVX/PVDCwaIQ8nTOPveOcFLSt8GcXdx8hD0bt39uWxYT88uXzqTd4fTvqta7oeUJqudepapKNt2DYJFw=="],

    "@tailwindcss/oxide-wasm32-wasi/tslib": ["tslib@2.8.1", "", { "bundled": true }, "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w=="],

    "@tauri-apps/plugin-opener/@tauri-apps/api": ["@tauri-apps/api@2.4.1", "", {}, "sha512-5sYwZCSJb6PBGbBL4kt7CnE5HHbBqwH+ovmOW6ZVju3nX4E3JX6tt2kRklFEH7xMOIwR0btRkZktuLhKvyEQYg=="],
  }
}
```

## File: `index.html`
```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/vite.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>qsv easy installer for Windows</title>
    </head>

    <body>
        <div id="root"></div>
        <script type="module" src="/src/main.tsx"></script>
    </body>
</html>
```

## File: `package.json`
```json
{
  "name": "qsv-easy-installer",
  "private": true,
  "version": "1.1.1",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "tauri": "tauri"
  },
  "dependencies": {
    "@tailwindcss/vite": "^4.1.4",
    "@tauri-apps/api": "^2.5.0",
    "@tauri-apps/plugin-opener": "^2.2.6",
    "lucide-react": "^0.487.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "tailwindcss": "^4.1.4"
  },
  "devDependencies": {
    "@types/react": "^18.3.20",
    "@types/react-dom": "^18.3.6",
    "@vitejs/plugin-react": "^4.4.0",
    "typescript": "~5.6.3",
    "vite": "^6.2.6",
    "@tauri-apps/cli": "^2.5.0"
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

## File: `tsconfig.node.json`
```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
```

## File: `vite.config.ts`
```typescript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

// @ts-expect-error process is a nodejs global
const host = process.env.TAURI_DEV_HOST;

// https://vitejs.dev/config/
export default defineConfig(async () => ({
  plugins: [react(), tailwindcss()],

  // Vite options tailored for Tauri development and only applied in `tauri dev` or `tauri build`
  //
  // 1. prevent vite from obscuring rust errors
  clearScreen: false,
  // 2. tauri expects a fixed port, fail if that port is not available
  server: {
    port: 1420,
    strictPort: true,
    host: host || false,
    hmr: host
      ? {
          protocol: "ws",
          host,
          port: 1421,
        }
      : undefined,
    watch: {
      // 3. tell vite to ignore watching `src-tauri`
      ignored: ["**/src-tauri/**"],
    },
  },
}));
```

## File: `src/App.css`
```css
@import "tailwindcss";

.logo.vite:hover {
    filter: drop-shadow(0 0 2em #747bff);
}

.logo.react:hover {
    filter: drop-shadow(0 0 2em #61dafb);
}
:root {
    font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 24px;
    font-weight: 400;

    color: #0f0f0f;
    background-color: #f6f6f6;

    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-text-size-adjust: 100%;
}

.container {
    margin: 0;
    padding-top: 10vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
}

.logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: 0.75s;
}

.logo.tauri:hover {
    filter: drop-shadow(0 0 2em #24c8db);
}

.row {
    display: flex;
    justify-content: center;
}

a {
    font-weight: 500;
    color: #646cff;
    text-decoration: inherit;
}

a:hover {
    color: #535bf2;
}

h1 {
    text-align: center;
}

input,
button {
    border-radius: 8px;
    border: 1px solid transparent;
    padding: 0.6em 1.2em;
    font-size: 1em;
    font-weight: 500;
    font-family: inherit;
    color: #0f0f0f;
    background-color: #ffffff;
    transition: border-color 0.25s;
    box-shadow: 0 2px 2px rgba(0, 0, 0, 0.2);
}

button {
    cursor: pointer;
}

button:hover {
    border-color: #396cd8;
}
button:active {
    border-color: #396cd8;
    background-color: #e8e8e8;
}

input,
button {
    outline: none;
}

@media (prefers-color-scheme: dark) {
    :root {
        color: #f6f6f6;
        background-color: #2f2f2f;
    }

    a:hover {
        color: #24c8db;
    }

    input,
    button {
        color: #ffffff;
        background-color: #0f0f0f98;
    }
    button:active {
        background-color: #0f0f0f69;
    }
}
```

## File: `src/App.tsx`
```tsx
import { useState } from "react";
import { invoke } from "@tauri-apps/api/core";
import { Loader2Icon } from "lucide-react";

import "./App.css";

function App() {
  const [loading, setLoading] = useState(false);
  return (
    <main className="justify-center mx-auto grid mt-32">
      <div className="w-full flex justify-center">
        <img width="100px" alt="qsv logo" src="/qsv-logo-icon.png" />
      </div>
      <h1 className="text-3xl my-4 font-bold">
        qsv Easy installer for Windows
      </h1>
      <p className="mb-4">
        Click the button to install the latest release of qsv and then qsv
        should be accessible from a new terminal.
      </p>
      <button
        disabled={loading}
        onClick={() => {
          setLoading(true);
          invoke("run_path_update")
            .finally(() => {
              setLoading(false);
              alert("Successfully installed qsv. Try opening a new terminal and run a qsv command!");
            });
        }}
        className="mx-auto w-full flex justify-center bg-blue-400"
      >
        {loading ? (
          <Loader2Icon className="animate-spin" />
        ) : (
          <p>Install qsv 🚀</p>
        )}
      </button>
      {loading && (
        <p className="mt-4 text-center">
          Downloading and installing qsv to PATH. This may take a few seconds...
        </p>
      )}
    </main>
  );
}

export default App;
```

## File: `src/main.tsx`
```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
```

## File: `src/vite-env.d.ts`
```typescript
/// <reference types="vite/client" />
```

## File: `src-tauri/.gitignore`
```
# Generated by Cargo
# will have compiled files and executables
/target/

# Generated by Tauri
# will have schema files for capabilities auto-completion
/gen/schemas
```

## File: `src-tauri/Cargo.toml`
```
[package]
name = "qsv-easy-installer"
version = "1.0.0"
description = "An easy installer for Windows devices to download the latest release of qsv and access it from PATH."
authors = ["datHere"]
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[lib]
# The `_lib` suffix may seem redundant but it is necessary
# to make the lib name unique and wouldn't conflict with the bin name.
# This seems to be only an issue on Windows, see https://github.com/rust-lang/cargo/issues/8519
name = "qsv_easy_installer_lib"
crate-type = ["staticlib", "cdylib", "rlib"]

[build-dependencies]
tauri-build = { version = "2", features = [] }

[dependencies]
tauri = { version = "2", features = [] }
tauri-plugin-opener = "2"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
reqwest = { version = "0.12.15", features = ["blocking", "json"] }
tempfile = "3.19.1"
zip = "2.6.1"
winreg = "0.55.0"
```

## File: `src-tauri/build.rs`
```rust
fn main() {
    tauri_build::build()
}
```

## File: `src-tauri/tauri.conf.json`
```json
{
  "$schema": "https://schema.tauri.app/config/2",
  "productName": "qsv-easy-installer",
  "version": "../package.json",
  "identifier": "com.qsv-easy-installer.app",
  "build": {
    "beforeDevCommand": "bun run dev",
    "devUrl": "http://localhost:1420",
    "beforeBuildCommand": "bun run build",
    "frontendDist": "../dist"
  },
  "app": {
    "windows": [
      {
        "title": "qsv Easy installer for Windows",
        "width": 800,
        "height": 600
      }
    ],
    "security": {
      "csp": null
    }
  },
  "bundle": {
    "active": true,
    "targets": "all",
    "icon": [
      "icons/32x32.png",
      "icons/128x128.png",
      "icons/128x128@2x.png",
      "icons/icon.icns",
      "icons/icon.ico"
    ]
  }
}
```

## File: `src-tauri/capabilities/default.json`
```json
{
  "$schema": "../gen/schemas/desktop-schema.json",
  "identifier": "default",
  "description": "Capability for the main window",
  "windows": ["main"],
  "permissions": [
    "core:default",
    "opener:default"
  ]
}
```

## File: `src-tauri/src/lib.rs`
```rust
use std::io::Write;

use tauri::Manager;
use tempfile::tempfile;
use winreg::{enums::HKEY_CURRENT_USER, RegKey};

#[tauri::command]
async fn run_path_update(app_handle: tauri::AppHandle) {
    // Get app local data dir path
    let app_local_data_dir = app_handle.path().app_local_data_dir().unwrap();
    // Download qsv to bin dir if it doesn't exist and overwrite any existing qsv
    // Get the version of qsv
    let latest_release_endpoint = "https://api.github.com/repos/dathere/qsv/releases/latest";
    let client = reqwest::Client::new();
    let res = client
        .get(latest_release_endpoint)
        .header(reqwest::header::USER_AGENT, "qsv easy installer")
        .send()
        .await
        .unwrap()
        .json::<serde_json::Value>()
        .await
        .unwrap();
    let release_version = res.get("name").unwrap().as_str().unwrap();
    // Download the zip file temporarily then extract the relevant qsvp file (we use qsvp instead of qsv for the broadest compatibility)
    let zip_download_url = format!("https://github.com/dathere/qsv/releases/download/{release_version}/qsv-{release_version}-x86_64-pc-windows-msvc.zip");
    let mut temp_zip_file = tempfile().unwrap();
    let zip_bytes = reqwest::get(zip_download_url)
        .await
        .unwrap()
        .bytes().await.unwrap();
    temp_zip_file.write_all(&zip_bytes).unwrap();
    let mut zip = zip::ZipArchive::new(temp_zip_file).unwrap();
    let mut qsvp = zip.by_name("qsvp.exe").unwrap();
    // Create a bin folder in app_local_data_dir if it doesn't exist
    let bin_dir = app_local_data_dir.join("bin");
    if !std::path::Path::exists(&bin_dir) {
        std::fs::create_dir(&bin_dir).unwrap();
    }
    // Write qsvp.exe to bin/qsv.exe
    let mut qsv_file = std::fs::File::create(bin_dir.join("qsv.exe")).unwrap();
    std::io::copy(&mut qsvp, &mut qsv_file).unwrap();
    drop(qsv_file);
    // Add the bin dir to PATH
    let bin_dir_str = bin_dir.to_str().unwrap();
    // Get the current PATH
    let hkcu = RegKey::predef(HKEY_CURRENT_USER);
    let (reg_key, _) = hkcu.create_subkey("Environment").unwrap();
    let path_var: String = reg_key.get_value("Path").unwrap();
    // If bin dir is not in PATH, add bin dir to PATH
    if !path_var.contains(bin_dir_str) {
        let updated_path_var = format!("{bin_dir_str};{path_var}");
        reg_key.set_value("Path", &updated_path_var).unwrap();
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![run_path_update])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

## File: `src-tauri/src/main.rs`
```rust
// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    qsv_easy_installer_lib::run()
}
```

