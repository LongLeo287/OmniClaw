---
id: segra
type: knowledge
owner: OA_Triage
---
# segra
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "segra-repo-tools",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "prepare": "husky",
    "precommit:lint-staged": "lint-staged"
  },
  "devDependencies": {
    "husky": "^9.0.11",
    "lint-staged": "^15.2.10"
  }
}

```

### File: README.md
```md
<img height="100" src="https://cdn.segra.tv/icon.png"/>

**Segra** is a powerful recording software built on Open Broadcaster Software (OBS), designed for gamers and content creators. Record, clip, and upload gameplay highlights effortlessly, with smart automation and deep game integration.

### ✂️ Clip Editor

![image](https://github.com/user-attachments/assets/beed0524-35f1-48be-9dd8-c2455959d2f9)

### 🔥 Highlights

![image](https://github.com/user-attachments/assets/481cc9fa-3efb-412d-b668-8be7d11b9851)


### ⚙️ Settings

![image](https://github.com/user-attachments/assets/de300431-1b63-4ed2-a022-110f8f828d1a)


---

## ✨ Features  
- **Auto-Start Recording**: Begin recording automatically when your game launches.  
- **Instant Clipping**: Save key moments with a hotkey.
- **Direct Upload**: Share clips to **[Segra.tv](https://segra.tv)** instantly.  
- **Game Integration**: Tracks in-game stats (kills, deaths, assists) to auto-generate highlights, powered by AI.  
- **Lightweight & Fast**: Built on OBS for 4K with 144 FPS capture with minimal performance impact.  
- **Customizable Settings**: Adjust recording quality (NVENC/AMD VCE), hotkeys, storage paths, etc.

---

## Why "Segra"?  
**Segra** (pronounced *"say-grah"*) means **"to win"** in Swedish. We built Segra to help you **preserve those moments**: the chaotic fun with friends, the clutch plays, and the wins (*segra!*) that deserve their own highlight reel.  

---

## 🛠 Installation
1. **Download**: Get `Segra-win-Setup.exe` from [[latest release](https://github.com/Segergren/Segra/releases/latest)].  
2. **Install**: Run the setup.  
3. **Configure**:  
   - Set recording directory and video quality.  
   - Assign hotkeys for clipping/uploading.  
   - Connect your Segra.tv account.  

## 🔄 Uninstallation
1. Open `Windows Settings`
2. Go to `Apps` -> `Installed apps`
3. Search for `Segra`
4. Click `Uninstall`

## 🤝 Contributing  
See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, dependencies, and dev workflow.
Help improve Segra by:  
- Report bugs or suggest features  
- Submit pull requests

---

## 📜 License  
Segra is **GPLv2 licensed**.  

---

## 🔐 Code Signing Policy
Free code signing provided by **[SignPath.io](https://signpath.io)**, certificate by **[SignPath Foundation](https://signpath.org)**.

**Team roles**

| Role      | Person |
|-----------|--------|
| Authors   | @Segergren |
| Reviewers | @Segergren |
| Approvers | @Segergren |

See our [Privacy Policy](https://segra.tv/privacy).

## Star History

<a href="https://www.star-history.com/#Segergren/Segra&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Segergren/Segra&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Segergren/Segra&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Segergren/Segra&type=Date" />
 </picture>
</a>

## Acknowledgments
- **[OBS Studio](https://obsproject.com)**: The backbone of Segra's recording engine.
- **[ObsKit.NET](https://github.com/Segergren/ObsKit.NET)**: The modern C#/OBS bridge that powers Segra's recording functionality.
- **[FFmpeg](https://github.com/FFmpeg/FFmpeg)**: for video and image encoding.  

```

### File: Frontend\package.json
```json
{
  "name": "frontend",
  "private": true,
  "version": "Developer Preview",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier . --write",
    "format:check": "prettier . --check",
    "preview": "vite preview"
  },
  "dependencies": {
    "@tailwindcss/vite": "^4.1.17",
    "@tanstack/react-query": "^5.90.10",
    "@types/semver": "^7.7.1",
    "autoprefixer": "^10.4.22",
    "framer-motion": "^12.23.24",
    "markdown-to-jsx": "^8.0.0",
    "react": "^19.2.0",
    "react-dnd": "^16.0.1",
    "react-dnd-html5-backend": "^16.0.1",
    "react-dom": "^19.2.0",
    "react-icons": "^5.5.0",
    "react-use-websocket": "^4.13.0",
    "semver": "^7.7.3",
    "theme-change": "^2.5.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@tailwindcss/postcss": "^4.1.17",
    "@types/react": "^19.2.6",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "daisyui": "^5.5.19",
    "eslint": "^9.39.1",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-prettier": "^5.5.4",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.24",
    "globals": "^16.5.0",
    "prettier": "^3.6.2",
    "tailwindcss": "^4.1.17",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.47.0",
    "vite": "^7.3.1"
  },
  "trustedDependencies": [
    "@tailwindcss/oxide"
  ]
}

```

### File: Frontend\README.md
```md
# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default tseslint.config({
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
});
```

- Replace `tseslint.configs.recommended` to `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked`
- Optionally add `...tseslint.configs.stylisticTypeChecked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and update the config:

```js
// eslint.config.js
import react from 'eslint-plugin-react';

export default tseslint.config({
  // Set the react version
  settings: { react: { version: '18.3' } },
  plugins: {
    // Add the react plugin
    react,
  },
  rules: {
    // other rules...
    // Enable its recommended rules
    ...react.configs.recommended.rules,
    ...react.configs['jsx-runtime'].rules,
  },
});
```

```

### File: build-local.sh
```sh
#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Building Frontend ==="
(cd Frontend && npm run build)

echo "=== Copying Frontend to wwwroot ==="
rm -rf wwwroot
mkdir wwwroot
cp -r Frontend/dist/* wwwroot/

echo "=== Publishing Backend ==="
dotnet publish -c Release --self-contained -r win-x64 -o publish

echo ""
echo "=== Done! ==="
WIN_DIR=$(echo "$SCRIPT_DIR" | sed 's|^/\([a-zA-Z]\)/|\1:/|' | sed 's|/|\\|g')
echo "Output: $WIN_DIR\\publish\\"
echo "Executable: $WIN_DIR\\publish\\Segra.exe"
echo ""
read -n 1 -s -r -p "Press any key to exit..."

```

### File: CONTRIBUTING.md
```md
# Contributing to Segra

A quick, practical guide to get you developing on both the backend (C#/.NET) and the frontend (React/Vite).

## Requirements
- Windows 10 (build 17763 / 1809) or newer
- .NET SDK 9.0.x (Windows targeting)
- Git
- Bun v1.1+ (for frontend tooling and git hooks)
- Node.js 18+ (only if you want the backend to auto-start the frontend dev server via `npm run dev`)
- IDEs (pick what you like):
  - Visual Studio 2022 (17.12+) or VS Code + C# Dev Kit

## Repo Layout
- `Segra.sln` — solution root
- `Backend/` — app services, models, utils
- `Frontend/` — React + Vite app (TypeScript, Tailwind, DaisyUI)

## First-Time Setup
1. Clone the repo
   - `git clone <your-fork-or-upstream> && cd Segra`
2. Install root dev tools (husky/lint-staged for hooks)
   - `bun install`
   - `bun run prepare`
3. Install frontend deps
   - `cd Frontend && bun install && cd ..`
4. Ensure .NET SDK 9 is on PATH
   - `dotnet --info` should show `Version: 9.x` and `OS: Windows`

## Developing
There are two parts running during development: the backend (Photino.NET desktop app) and the frontend (Vite dev server on port 2882).

### Start the Frontend (Vite)
- Using Bun (recommended):
  - `cd Frontend && bun run dev` (serves on http://localhost:2882)
- Using Node/npm (optional):
  - `cd Frontend && npm run dev`

### Start the Backend (.NET)
- From the repo root:
  - `dotnet run --project Segra.csproj`
- Notes:
  - In Debug mode the app expects the frontend on `http://localhost:2882`.
  - If Node/npm is installed, the backend attempts to auto-run `npm run dev` in `Frontend/` if nothing is listening on 2882.

## Building
- Backend (Release): `dotnet build -c Release`
- Backend publish (self-contained optional): `dotnet publish -c Release`
- Frontend (bundle): `cd Frontend && bun run build`

## Linting & Formatting
- EditorConfig is enforced across the repo:
  - Global: CRLF line endings and 2-space indent
  - C#: CRLF line endings, 4-space indent
- C# formatting (via `dotnet format`):
  - Pre-commit: formats staged `*.cs` files
  - Pre-push: verifies no formatting drift in the solution
- Frontend (in `Frontend/`):
  - Prettier + ESLint with Bun
  - Scripts:
    - `bun run format` / `bun run format:check`
    - `bun run lint` / `bun run lint:fix`

## Git Hooks (Husky + lint-staged)
- Installed at repo root via Bun.
- Pre-commit:
  - Prettier + ESLint on staged files in `Frontend/`
  - `dotnet format` on staged `*.cs`
- Pre-push:
  - `dotnet format --verify-no-changes` on the solution

If hooks don't run:
- Ensure Bun is on PATH for your Git shell
- Re-run: `bun install && bun run prepare`

## Pull Requests
- Keep PRs focused and small
- Run format and lint before pushing

Thanks for contributing ❤️

```

### File: lint-staged.config.js
```js
export default {
  'Frontend/**/*.{ts,tsx,js,jsx,css,md,json,html}': (files) => {
    const quoted = files.map((f) => `"${f}"`).join(' ');
    return [
      `Frontend/node_modules/.bin/prettier --write ${quoted}`,
      `Frontend/node_modules/.bin/eslint --config Frontend/eslint.config.js --fix ${quoted}`,
    ];
  },
  '**/*.cs': (files) => {
    const quoted = files.map((f) => `"${f}"`).join(' ');
    // Run dotnet format on the whole solution - more reliable than per-file
    return [`dotnet format Segra.sln`];
  },
};

```

### File: packages.lock.json
```json
{
  "version": 1,
  "dependencies": {
    "net9.0-windows10.0.19041": {
      "Microsoft.Extensions.FileProviders.Embedded": {
        "type": "Direct",
        "requested": "[10.0.0, )",
        "resolved": "10.0.0",
        "contentHash": "ECaTMB4NdV9W1es9J6tN0yoXRPUHKMi5+2L7hcVZ5k9zVdxccIx6+vMllwEYcdTaO0mCETEmdH4F0KxCqgnPaw==",
        "dependencies": {
          "Microsoft.Extensions.FileProviders.Abstractions": "10.0.0"
        }
      },
      "NAudio": {
        "type": "Direct",
        "requested": "[2.2.1, )",
        "resolved": "2.2.1",
        "contentHash": "c0DzwiyyklM0TP39Y7RObwO3QkWecgM6H60ikiEnsV/aEAJPbj5MFCLaD8BSfKuZe0HGuh9GRGWWlJmSxDc9MA==",
        "dependencies": {
          "NAudio.Asio": "2.2.1",
          "NAudio.Core": "2.2.1",
          "NAudio.Midi": "2.2.1",
          "NAudio.Wasapi": "2.2.1",
          "NAudio.WinForms": "2.2.1",
          "NAudio.WinMM": "2.2.1"
        }
      },
      "ObsKit.NET": {
        "type": "Direct",
        "requested": "[1.0.0, )",
        "resolved": "1.0.0",
        "contentHash": "hyyb4vNEmVubPAhciIlrZod7Mv5aHPdf37237iBBo4pW4fsUaML+gFf0RjLYNHnXrgy9G9CNy6roSwCRK5zr9A=="
      },
      "Photino.NET": {
        "type": "Direct",
        "requested": "[4.0.16, )",
        "resolved": "4.0.16",
        "contentHash": "2oTFsxt8XpLlVvtChlBD8HzLw6MgfHF+DQ4aLEDfgc4GbYjumEywB1JMfWDChm2Whfkr4ZF7DV2deRrpitiBcw==",
        "dependencies": {
          "Photino.Native": "4.0.22"
        }
      },
      "Photino.NET.Server": {
        "type": "Direct",
        "requested": "[4.0.12, )",
        "resolved": "4.0.12",
        "contentHash": "m6tUz9CAOkvPWo48xnJj7HZGh8OvEQTpJ1zf96HkT4DB17R1u6xqYRWg55jH5u/HJOgYngHfMYiGcxpTNXwRGQ=="
      },
      "Serilog": {
        "type": "Direct",
        "requested": "[4.3.0, )",
        "resolved": "4.3.0",
        "contentHash": "+cDryFR0GRhsGOnZSKwaDzRRl4MupvJ42FhCE4zhQRVanX0Jpg6WuCBk59OVhVDPmab1bB+nRykAnykYELA9qQ=="
      },
      "Serilog.Sinks.Console": {
        "type": "Direct",
        "requested": "[6.1.1, )",
        "resolved": "6.1.1",
        "contentHash": "8jbqgjUyZlfCuSTaJk6lOca465OndqOz3KZP6Cryt/IqZYybyBu7GP0fE/AXBzrrQB3EBmQntBFAvMVz1COvAA==",
        "dependencies": {
          "Serilog": "4.0.0"
        }
      },
      "Serilog.Sinks.Debug": {
        "type": "Direct",
        "requested": "[3.0.0, )",
        "resolved": "3.0.0",
        "contentHash": "4BzXcdrgRX7wde9PmHuYd9U6YqycCC28hhpKonK7hx0wb19eiuRj16fPcPSVp0o/Y1ipJuNLYQ00R3q2Zs8FDA==",
        "dependencies": {
          "Serilog": "4.0.0"
        }
      },
      "Serilog.Sinks.File": {
        "type": "Direct",
        "requested": "[7.0.0, )",
        "resolved": "7.0.0",
        "contentHash": "fKL7mXv7qaiNBUC71ssvn/dU0k9t0o45+qm2XgKAlSt19xF+ijjxyA3R6HmCgfKEKwfcfkwWjayuQtRueZFkYw==",
        "dependencies": {
          "Serilog": "4.2.0"
        }
      },
      "System.Management": {
        "type": "Direct",
        "requested": "[10.0.0, )",
        "resolved": "10.0.0",
        "contentHash": "LE3rDZoPzulou78Tsq+3ALhUs4vatQ03v2QWbYVIenVPneUH/+LTUmHyyl098OxIFLQI6sNkZs8YHbUnT/sm3A==",
        "dependencies": {
          "System.CodeDom": "10.0.0"
        }
      },
      "System.Runtime.CompilerServices.Unsafe": {
        "type": "Direct",
        "requested": "[6.1.2, )",
        "resolved": "6.1.2",
        "contentHash": "2hBr6zdbIBTDE3EhK7NSVNdX58uTK6iHW/P/Axmm9sl1xoGSLqDvMtpecn226TNwHByFokYwJmt/aQQNlO5CRw=="
      },
      "Velopack": {
        "type": "Direct",
        "requested": "[0.0.1298, )",
        "resolved": "0.0.1298",
        "contentHash": "PJ6Nm28qJ4ChsHYzgHUJ8g+DGyyHes2+bwxY709+znMhgi8fMp8M1FTF8x6pZMjnsPCWVwoMlxVEyq0NLeRZtA==",
        "dependencies": {
          "NuGet.Versioning": "6.14.0"
        }
      },
      "Vortice.DirectX": {
        "type": "Direct",
        "requested": "[3.6.2, )",
        "resolved": "3.6.2",
        "contentHash": "pa/97U5IHascS/UJzMWFSKIs3wxh36zc8JpI+fzi/JLQk4wfTZur0n/Y9Lcp8i7hsf613Vu/6n6IImWSc9wupw==",
        "dependencies": {
          "SharpGen.Runtime": "2.2.0-beta",
          "SharpGen.Runtime.COM": "2.2.0-beta",
          "Vortice.Mathematics": "1.9.2"
        }
      },
      "Microsoft.Extensions.FileProviders.Abstractions": {
        "type": "Transitive",
        "resolved": "10.0.0",
        "contentHash": "/ppSdehKk3fuXjlqCDgSOtjRK/pSHU8eWgzSHfHdwVm5BP4Dgejehkw+PtxKG2j98qTDEHDst2Y99aNsmJldmw==",
        "dependencies": {
          "Microsoft.Extensions.Primitives": "10.0.0"
        }
      },
      "Microsoft.Extensions.Primitives": {
        "type": "Transitive",
        "resolved": "10.0.0",
        "contentHash": "inRnbpCS0nwO/RuoZIAqxQUuyjaknOOnCEZB55KSMMjRhl0RQDttSmLSGsUJN3RQ3ocf5NDLFd2mOQViHqMK5w=="
      },
      "Microsoft.NETCore.Platforms": {
        "type": "Transitive",
        "resolved": "3.1.0",
        "contentHash": "z7aeg8oHln2CuNulfhiLYxCVMPEwBl3rzicjvIX+4sUuCwvXw5oXQEtbiU2c0z4qYL5L3Kmx0mMA/+t/SbY67w=="
      },
      "Microsoft.Win32.Registry": {
        "type": "Transitive",
        "resolved": "4.7.0",
        "contentHash": "KSrRMb5vNi0CWSGG1++id2ZOs/1QhRqROt+qgbEAdQuGjGrFcl4AOl4/exGPUYz2wUnU42nvJqon1T3U0kPXLA==",
        "dependencies": {
          "System.Security.AccessControl": "4.7.0",
          "System.Security.Principal.Windows": "4.7.0"
        }
      },
      "NAudio.Asio": {
        "type": "Transitive",
        "resolved": "2.2.1",
        "contentHash": "hQglyOT5iT3XuGpBP8ZG0+aoqwRfidHjTNehpoWwX0g6KJEgtH2VaqM2nuJ2mheKZa/IBqB4YQTZVvrIapzfOA==",
        "dependencies": {
          "Microsoft.Win32.Registry": "4.7.0",
          "NAudio.Core": "2.2.1"
        }
      },
      "NAudio.Core": {
        "type": "Transitive",
        "resolved": "2.2.1",
        "contentHash": "GgkdP6K/7FqXFo7uHvoqGZTJvW4z8g2IffhOO4JHaLzKCdDOUEzVKtveoZkCuUX8eV2HAINqi7VFqlFndrnz/g=="
      },
      "NAudio.Midi": {
        "type": "Transitive",
        "resolved": "2.2.1",
        "contentHash": "6r23ylGo5aeP02WFXsPquz0T0hFJWyh+7t++tz19tc3Kr38NHm+Z9j+FiAv+xkH8tZqXJqus9Q8p6u7bidIgbw==",
        "dependencies": {
          "NAudio.Core": "2.2.1"
        }
      },
      "NAudio.Wasapi": {
        "type": "Transitive",
        "resolved": "2.2.1",
        "contentHash": "lFfXoqacZZe0WqNChJgGYI+XV/n/61LzPHT3C1CJp4khoxeo2sziyX5wzNYWeCMNbsWxFvT3b3iXeY1UYjBhZw==",
        "dependencies": {
          "NAudio.Core": "2.2.1"
        }
      },
      "NAudio.WinForms": {
        "type": "Transitive",
        "resolved": "2.2.1",
        "contentHash": "DlDkewY1myY0A+3NrYRJD+MZhZV0yy1mNF6dckB27IQ9XCs/My5Ip8BZcoSHOsaPSe2GAjvoaDnk6N9w8xTv7w==",
        "dependencies": {
          "NAudio.WinMM": "2.2.1"
        }
      },
      "NAudio.WinMM": {
        "type": "Transitive",
        "resolved": "2.2.1",
        "contentHash": "xFHRFwH4x6aq3IxRbewvO33ugJRvZFEOfO62i7uQJRUNW2cnu6BeBTHUS0JD5KBucZbHZaYqxQG8dwZ47ezQuQ==",
        "dependencies": {
          "Microsoft.Win32.Registry": "4.7.0",
          "NAudio.Core": "2.2.1"
        }
      },
      "NuGet.Versioning": {
        "type": "Transitive",
        "resolved": "6.14.0",
        "contentHash": "4v4blkhCv8mpKtfx+z0G/X0daVCzdIaHSC51GkUspugi5JIMn2Bo8xm5PdZYF0U68gOBfz/+aPWMnpRd85Jbow=="
      },
      "Photino.Native": {
        "type": "Transitive",
        "resolved": "4.0.22",
        "contentHash": "VIHipEOe4CZ7HElZE8zTwcvANOsCZ2yak/4nQ4LXzjdlwIjdbY8htmHfNR6rRPgWlCfTfT349GCa6V6Id2/Xyg=="
      },
      "SharpGen.Runtime": {
        "type": "Transitive",
        "resolved": "2.2.0-beta",
        "contentHash": "pqf/lAf4jy1iWqkm37JmhoQhBMPVudI/F9qp2zVvzjWAPeSggRIuxGMVEZQ4UQiqtJ1Rf/+j3MVAONGYyCEDzQ=="
      },
      "SharpGen.Runtime.COM": {
        "type": "Transitive",
        "resolved": "2.2.0-beta",
        "contentHash": "4vsXC8ohyVslcUDVBoVXLDkjKprqujh3GWy+DqqULjyZ3GCx7nwRAV5DdrXZxX70iEiKyI3TxW3Qhf/oOXeC1Q==",
        "dependencies": {
          "SharpGen.Runtime": "2.2.0-beta"
        }
      },
      "System.CodeDom": {
        "type": "Transitive",
        "resolved": "10.0.0",
        "contentHash": "QWERdKi/tQAx+MbrPxTGcpchqMANnVXNiv2r2tILBBB38E74buD+fABSUhozZ1G9kjbadFB0m+HPFMkhJPeFvA=="
      },
      "System.Security.AccessControl": {
        "type": "Transitive",
        "resolved": "4.7.0",
        "contentHash": "JECvTt5aFF3WT3gHpfofL2MNNP6v84sxtXxpqhLBCcDRzqsPBmHhQ6shv4DwwN2tRlzsUxtb3G9M3763rbXKDg==",
        "dependencies": {
          "Microsoft.NETCore.Platforms": "3.1.0",
          "System.Security.Principal.Windows": "4.7.0"
        }
      },
      "System.Security.Principal.Windows": {
        "type": "Transitive",
        "resolved": "4.7.0",
        "contentHash": "ojD0PX0XhneCsUbAZVKdb7h/70vyYMDYs85lwEI+LngEONe/17A0cFaRFqZU+sOEidcVswYWikYOQ9PPfjlbtQ=="
      },
      "Vortice.Mathematics": {
        "type": "Transitive",
        "resolved": "1.9.2",
        "contentHash": "+fS68BN4Kn1g+Roh7qnuBdXnVrfpr9DpwPMsqe27J04nDCFUuhEvo+T5PqXU1lZwn8sLlNayWCx/U6w4gWCvuA=="
      }
    }
  }
}
```

### File: Frontend\eslint.config.js
```js
import js from '@eslint/js';
import globals from 'globals';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import tseslint from 'typescript-eslint';
import eslintConfigPrettier from 'eslint-config-prettier';
import prettierPlugin from 'eslint-plugin-prettier';

export default tseslint.config(
  { ignores: ['dist', 'node_modules', 'build', '.next', 'coverage'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended, eslintConfigPrettier],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      prettier: prettierPlugin,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'prettier/prettier': 'error',
      // Temporarily allow the following rules
      'react-refresh/only-export-components': 'off',
      'react-hooks/rules-of-hooks': 'off',
      'react-hooks/exhaustive-deps': 'off',
      'react-hooks/immutability': 'off',
      'react-hooks/set-state-in-effect': 'off',
      'react-hooks/preserve-manual-memoization': 'off',
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-unused-vars': 'off',
    },
  },
);

```

### File: Frontend\index.html
```html
<!doctype html>
<html lang="en" data-theme="segra">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Segra</title>
  </head>
  <body
    style="
      font-family:
        Roboto,
        Roboto Fallback;
    "
  >
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### File: Frontend\package-lock.json
```json
{
  "name": "frontend",
  "version": "Developer Preview",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "frontend",
      "version": "Developer Preview",
      "dependencies": {
        "@supabase/supabase-js": "^2.83.0",
        "@tailwindcss/vite": "^4.1.17",
        "@tanstack/react-query": "^5.90.10",
        "@types/semver": "^7.7.1",
        "autoprefixer": "^10.4.22",
        "framer-motion": "^12.23.24",
        "markdown-to-jsx": "^8.0.0",
        "react": "^19.2.0",
        "react-dnd": "^16.0.1",
        "react-dnd-html5-backend": "^16.0.1",
        "react-dom": "^19.2.0",
        "react-icons": "^5.5.0",
        "react-use-websocket": "^4.13.0",
        "semver": "^7.7.3",
        "theme-change": "^2.5.0"
      },
      "devDependencies": {
        "@eslint/js": "^9.39.1",
        "@tailwindcss/postcss": "^4.1.17",
        "@types/react": "^19.2.6",
        "@types/react-dom": "^19.2.3",
        "@vitejs/plugin-react": "^5.1.1",
        "daisyui": "^5.5.5",
        "eslint": "^9.39.1",
        "eslint-config-prettier": "^10.1.8",
        "eslint-plugin-prettier": "^5.5.4",
        "eslint-plugin-react-hooks": "^7.0.1",
        "eslint-plugin-react-refresh": "^0.4.24",
        "globals": "^16.5.0",
        "prettier": "^3.6.2",
        "tailwindcss": "^4.1.17",
        "typescript": "~5.9.3",
        "typescript-eslint": "^8.47.0",
        "vite": "^7.2.2"
      }
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.27.1",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.27.2",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.28.5",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.5",
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-module-transforms": "^7.28.3",
        "@babel/helpers": "^7.28.4",
        "@babel/parser": "^7.28.5",
        "@babel/template": "^7.27.2",
        "@babel/traverse": "^7.28.5",
        "@babel/types": "^7.28.5",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/core/node_modules/semver": {
      "version": "6.3.1",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.5",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.5",
        "@babel/types": "^7.28.5",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.27.2",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.27.2",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/browserslist": {
      "version": "4.24.2",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "caniuse-lite": "^1.0.30001669",
        "electron-to-chromium": "^1.5.41",
        "node-releases": "^2.0.18",
        "update-browserslist-db": "^1.1.1"
      },
      "bin": {
        "browserslist": "cli.js"
      },
      "engines": {
        "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
      }
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/browserslist/node_modules/caniuse-lite": {
      "version": "1.0.30001686",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "CC-BY-4.0"
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/browserslist/node_modules/electron-to-chromium": {
      "version": "1.5.68",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/browserslist/node_modules/node-releases": {
      "version": "2.0.18",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/browserslist/node_modules/update-browserslist-db": {
      "version": "1.1.1",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "escalade": "^3.2.0",
        "picocolors": "^1.1.0"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/semver": {
      "version": "6.3.1",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.27.1",
        "@babel/parser": "^7.27.1",
        "@babel/template": "^7.27.1",
        "@babel/types": "^7.27.1",
        "debug": "^4.3.1",
        "globals": "^11.1.0"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/node_modules/@babel/generator": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.27.1",
        "@babel/types": "^7.27.1",
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.25",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/node_modules/@babel/generator/node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.5",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/set-array": "^1.2.1",
        "@jridgewell/sourcemap-codec": "^1.4.10",
        "@jridgewell/trace-mapping": "^0.3.24"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/node_modules/@babel/generator/node_modules/@jridgewell/gen-mapping/node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.0",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/node_modules/@babel/generator/node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.25",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/node_modules/@babel/generator/node_modules/@jridgewell/trace-mapping/node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.0",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/node_modules/@babel/parser": {
      "version": "7.27.2",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.27.1"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/node_modules/globals": {
      "version": "11.12.0",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/@babel/helper-module-imports/node_modules/@babel/types": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.3",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1",
        "@babel/traverse": "^7.28.3"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-module-transforms/node_modules/@babel/traverse": {
      "version": "7.28.3",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.3",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.28.3",
        "@babel/template": "^7.27.2",
        "@babel/types": "^7.28.2",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms/node_modules/@babel/traverse/node_modules/@babel/generator": {
      "version": "7.28.3",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.3",
        "@babel/types": "^7.28.2",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms/node_modules/@babel/traverse/node_modules/@babel/parser": {
      "version": "7.28.3",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.2"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/helper-module-transforms/node_modules/@babel/traverse/node_modules/@babel/types": {
      "version": "7.28.2",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.28.4",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.27.2",
        "@babel/types": "^7.28.4"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers/node_modules/@babel/types": {
      "version": "7.28.4",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.28.5",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.5"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-
... [TRUNCATED]
```

### File: Frontend\tailwind.config.js
```js
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{vue,js,ts,tsx}'],
  theme: {
    extend: {
      borderColor: {
        custom: '#2e3640',
        primary: '#49515b',
        primaryYellow: '#fecb00',
      },
      outlineColor: {
        custom: '#2e3640',
        primary: '#49515b',
        primaryYellow: '#fecb00',
      },
    },
  },
};

```

### File: Frontend\tsconfig.app.json
```json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}

```

### File: Frontend\tsconfig.json
```json
{
  "files": [],
  "references": [{ "path": "./tsconfig.app.json" }, { "path": "./tsconfig.node.json" }]
}

```

### File: Frontend\tsconfig.node.json
```json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2022",
    "lib": ["ES2023"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}

```

### File: Frontend\vite.config.ts
```ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { version } from './package.json';
import tailwindcss from '@tailwindcss/vite';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: 2882,
  },
  define: {
    __APP_VERSION__: JSON.stringify(version),
  },
  build: {
    // Add cache busting for assets with content hashing
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].[hash].js',
        chunkFileNames: 'assets/[name].[hash].js',
        assetFileNames: 'assets/[name].[hash].[ext]',
      },
    },
    // Ensure no caching issues by generating proper cache headers
    manifest: true,
  },
});

```

### File: Properties\launchSettings.json
```json
{
  "profiles": {
    "Segra": {
      "commandName": "Project",
      "commandLineArgs": "--debug",
      "nativeDebugging": true
    }
  }
}
```

### File: Properties\Resources.Designer.cs
```cs
﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace Segra.Properties {
    using System;
    
    
    /// <summary>
    ///   A strongly-typed resource class, for looking up localized strings, etc.
    /// </summary>
    // This class was auto-generated by the StronglyTypedResourceBuilder
    // class via a tool like ResGen or Visual Studio.
    // To add or remove a member, edit your .ResX file then rerun ResGen
    // with the /str option, or rebuild your VS project.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "17.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    internal class Resources {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Resources() {
        }
        
        /// <summary>
        ///   Returns the cached ResourceManager instance used by this class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("Segra.Properties.Resources", typeof(Resources).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Overrides the current thread's CurrentUICulture property for all
        ///   resource lookups using this strongly typed resource class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Looks up a localized resource of type System.Byte[].
        /// </summary>
        internal static byte[] bookmark {
            get {
                object obj = ResourceManager.GetObject("bookmark", resourceCulture);
                return ((byte[])(obj));
            }
        }
        
        /// <summary>
        ///   Looks up a localized resource of type System.IO.UnmanagedMemoryStream similar to System.IO.MemoryStream.
        /// </summary>
        internal static System.IO.UnmanagedMemoryStream error {
            get {
                return ResourceManager.GetStream("error", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Looks up a localized resource of type System.Drawing.Icon similar to (Icon).
        /// </summary>
        internal static System.Drawing.Icon icon {
            get {
                object obj = ResourceManager.GetObject("icon", resourceCulture);
                return ((System.Drawing.Icon)(obj));
            }
        }
        
        /// <summary>
        ///   Looks up a localized resource of type System.Drawing.Icon similar to (Icon).
        /// </summary>
        internal static System.Drawing.Icon iconRecording {
            get {
                object obj = ResourceManager.GetObject("iconRecording", resourceCulture);
                return ((System.Drawing.Icon)(obj));
            }
        }
        
        /// <summary>
        ///   Looks up a localized resource of type System.IO.UnmanagedMemoryStream similar to System.IO.MemoryStream.
        /// </summary>
        internal static System.IO.UnmanagedMemoryStream start {
            get {
                return ResourceManager.GetStream("start", resourceCulture);
            }
        }
    }
}

```

### File: Properties\Settings.Designer.cs
```cs
﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace Segra.Properties {
    
    
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.VisualStudio.Editors.SettingsDesigner.SettingsSingleFileGenerator", "17.12.0.0")]
    internal sealed partial class Settings : global::System.Configuration.ApplicationSettingsBase {
        
        private static Settings defaultInstance = ((Settings)(global::System.Configuration.ApplicationSettingsBase.Synchronized(new Settings())));
        
        public static Settings Default {
            get {
                return defaultInstance;
            }
        }
    }
}

```

### File: Backend\Api\ContentServer.cs
```cs
using Serilog;
using System.Net;
using System.Web;
using Segra.Backend.Media;

namespace Segra.Backend.Api
{
    internal class ContentServer
    {
        private static readonly HttpListener _httpListener = new();
        private static CancellationTokenSource? _cancellationTokenSource;

        public static void StartServer(string prefix)
        {
            _httpListener.Prefixes.Add(prefix);
            _httpListener.Start();
            Log.Information("Server started at {Prefix}", prefix);

            _cancellationTokenSource = new CancellationTokenSource();
            _ = Task.Run(() => AcceptRequestsAsync(_cancellationTokenSource.Token));
        }

        private static async Task AcceptRequestsAsync(CancellationToken cancellationToken)
        {
            Log.Information("ContentServer now accepting requests");

            while (!cancellationToken.IsCancellationRequested && _httpListener.IsListening)
            {
                try
                {
                    var context = await _httpListener.GetContextAsync();
                    _ = ProcessRequestAsync(context);
                }
                catch (HttpListenerException ex) when (ex.ErrorCode == 995)
                {
                    Log.Information("ContentServer listener stopped");
                    break;
                }
                catch (ObjectDisposedException)
                {
                    Log.Information("ContentServer listener disposed");
                    break;
                }

                catch (Exception ex)
                {
                    Log.Error(ex, "Error accepting request");
                }
            }

            Log.Information("ContentServer stopped accepting requests");
        }

        private static async Task ProcessRequestAsync(HttpListenerContext context)
        {
            var response = context.Response;

            try
            {
                var rawUrl = context.Request.RawUrl ?? "";

                if (rawUrl.StartsWith("/api/thumbnail"))
                {
                    await HandleThumbnailRequest(context);
                }
                else if (rawUrl.StartsWith("/api/content"))
                {
                    await HandleContentRequest(context);
                }
                else
                {
                    response.StatusCode = (int)HttpStatusCode.NotFound;
                    response.ContentType = "text/plain";
                    using (var writer = new StreamWriter(response.OutputStream))
                    {
                        await writer.WriteAsync("Invalid endpoint.");
                    }
                }
            }
            catch (HttpListenerException)
            {
            }
            catch (Exception ex)
            {
                Log.Error(ex, "Error processing request for {Url}", context.Request.RawUrl);
                try
                {
                    if (!response.OutputStream.CanWrite)
                        return;

                    response.StatusCode = (int)HttpStatusCode.InternalServerError;
                    response.ContentType = "text/plain";
                    using (var writer = new StreamWriter(response.OutputStream))
                    {
                        await writer.WriteAsync("Internal server error");
                    }
                }
                catch
                {
                }
            }
            finally
            {
                try
                {
                    response.Close();
                }
                catch
                {
                }
            }
        }

        private static async Task HandleThumbnailRequest(HttpListenerContext context)
        {
            var query = HttpUtility.ParseQueryString(context.Request?.Url?.Query ?? "");
            string input = query["input"] ?? "";
            string timeParam = query["time"] ?? "";
            var response = context.Response;

            response.AddHeader("Access-Control-Allow-Origin", "*");

            if (!File.Exists(input))
            {
                Log.Warning("Thumbnail request file not found: {Input}", input);
                response.StatusCode = (int)HttpStatusCode.NotFound;
                response.ContentType = "text/plain";
                using (var writer = new StreamWriter(response.OutputStream))
                {
                    await writer.WriteAsync("File not found.");
                }
                return;
            }

            if (string.IsNullOrEmpty(timeParam))
            {
                response.ContentType = "image/jpeg";
                response.AddHeader("Cache-Control", "public, max-age=86400");
                response.AddHeader("Expires", DateTime.UtcNow.AddDays(7).ToString("R"));

                try
                {
                    var lastModified = File.GetLastWriteTimeUtc(input);
                    response.AddHeader("Last-Modified", lastModified.ToString("R"));
                }
                catch (Exception ex)
                {
                    Log.Warning(ex, "Could not get last modified time for {Input}", input);
                }

                using (var fs = new FileStream(input, FileMode.Open, FileAccess.Read, FileShare.ReadWrite, 81920, useAsync: true))
                {
                    response.ContentLength64 = fs.Length;
                    await fs.CopyToAsync(response.OutputStream);
                }
            }
            else
            {
                if (!double.TryParse(timeParam, System.Globalization.NumberStyles.AllowDecimalPoint, System.Globalization.CultureInfo.InvariantCulture, out double timeSeconds))
                {
                    Log.Warning("Could not parse timeParam={TimeParam}, using 0.0", timeParam);
                    timeSeconds = 0.0;
                }

                if (!FFmpegService.FFmpegExists())
                {
                    Log.Error("FFmpeg executable not found");
                    response.StatusCode = (int)HttpStatusCode.InternalServerError;
                    response.ContentType = "text/plain";
                    using (var writer = new StreamWriter(response.OutputStream))
                    {
                        await writer.WriteAsync("FFmpeg not found on server.");
                    }
                    return;
                }

                byte[] jpegBytes = await FFmpegService.GenerateThumbnail(input, timeSeconds);

                if (jpegBytes != null && jpegBytes.Length > 0)
                {
                    response.ContentType = "image/jpeg";
                    response.AddHeader("Cache-Control", "no-cache, no-store, must-revalidate");
                    response.AddHeader("Pragma", "no-cache");
                    response.AddHeader("Expires", "0");
                    response.ContentLength64 = jpegBytes.Length;
                    await response.OutputStream.WriteAsync(jpegBytes, 0, jpegBytes.Length);
                }
                else
                {
                    Log.Error("No thumbnail data received from FFmpeg");
                    response.StatusCode = (int)HttpStatusCode.InternalServerError;
                    response.ContentType = "text/plain";
                    using (var writer = new StreamWriter(response.OutputStream))
                    {
                        await writer.WriteAsync("Failed to generate thumbnail.");
                    }
                }
            }
        }

        private static async Task HandleContentRequest(HttpListenerContext context)
        {
            var query = HttpUtility.ParseQueryString(context.Request?.Url?.Query ?? "");
            string fileName = query["input"] ?? "";
            var response = context.Response;

            response.AddHeader("Access-Control-Allow-Origin", "*");

            if (!File.Exists(fileName))
            {
                response.StatusCode = (int)HttpStatusCode.NotFound;
                response.ContentType = "text/plain";
                using (var writer = new StreamWriter(response.OutputStream))
                {
                    await writer.WriteAsync("File not found.");
                }
                return;
            }

            if (fileName.EndsWith(".mp4", StringComparison.OrdinalIgnoreCase))
            {
                await StreamVideoFile(fileName, context);
            }
            else if (fileName.EndsWith(".json", StringComparison.OrdinalIgnoreCase))
            {
                await StreamJsonFile(fileName, response);
            }
            else
            {
                response.StatusCode = (int)HttpStatusCode.BadRequest;
                response.ContentType = "text/plain";
                using (var writer = new StreamWriter(response.OutputStream))
                {
                    await writer.WriteAsync("Unsupported file type.");
                }
            }
        }

        private static async Task StreamVideoFile(string fileName, HttpListenerContext context)
        {
            var response = context.Response;

            string rangeHeader = context.Request.Headers["Range"] ?? "";
            long start = 0;
            long end;

            using (var fs = new FileStream(fileName, FileMode.Open, FileAccess.Read, FileShare.ReadWrite, 262144,
                FileOptions.Asynchronous | FileOptions.SequentialScan))
            {
                long fileLength = fs.Length;
                end = fileLength - 1;

                if (!string.IsNullOrEmpty(rangeHeader) && rangeHeader.StartsWith("bytes="))
                {
                    string[] rangeParts = rangeHeader.Substring(6).Split('-');
                    if (rangeParts.Length > 0 && !string.IsNullOrEmpty(rangeParts[0]))
                    {
                        long.TryParse(rangeParts[0], out start);
                    }
                    if (rangeParts.Length > 1 && !string.IsNullOrEmpty(rangeParts[1]))
                    {
                        long.TryParse(rangeParts[1], out end);
                    }
                }

                if (start > end || start < 0 || end >= fileLength)
                {
                    response.StatusCode = (int)HttpStatusCode.RequestedRangeNotSatisfiable;
                    response.AddHeader("Content-Range", $"bytes */{fileLength}");
                    return;
                }

                long contentLength = end - start + 1;

                response.StatusCode = string.IsNullOrEmpty(rangeHeader) ? (int)HttpStatusCode.OK : (int)HttpStatusCode.PartialContent;
                response.ContentType = "video/mp4";
                response.AddHeader("Accept-Ranges", "bytes");

                if (!string.IsNullOrEmpty(rangeHeader))
                {
                    response.AddHeader("Content-Range", $"bytes {start}-{end}/{fileLength}");
                }

                response.ContentLength64 = contentLength;

                if (start > 0)
                {
                    fs.Seek(start, SeekOrigin.Begin);
                }

                byte[] buffer = new byte[262144];
                long bytesRemaining = contentLength;

                while (bytesRemaining > 0)
                {
                    int bytesToRead = (int)Math.Min(buffer.Length, bytesRemaining);
                    int bytesRead = await fs.ReadAsync(buffer, 0, bytesToRead);

                    if (bytesRead == 0)
                        break;

                    await response.OutputStream.WriteAsync(buffer, 0, bytesRead);
                    bytesRemaining -= bytesRead;
                }
            }
        }

        private static async Task StreamJsonFile(string fileName, HttpListenerResponse response)
        {
            var fileInfo = new FileInfo(fileName);

            response.StatusCode = (int)HttpStatusCode.OK;
            response.ContentType = "application/json";
            response.AddHeader("Accept-Ranges", "bytes");
            response.ContentLength64 = fileInfo.Length;

            using (var fs = new FileStream(fileName, FileMode.Open, FileAccess.Read, FileShare.ReadWrite, 81920, useAsync: true))
            {
                await fs.CopyToAsync(response.OutputStream);
            }
        }

        public static void StopServer()
        {
            try
            {
                _cancellationTokenSource?.Cancel();
                _httpListener.Stop();
                _httpListener.Close();
                Log.Information("ContentServer stopped");
            }
            catch (Exception ex)
            {
                Log.Error(ex, "Error stopping ContentServer");
            }
            finally
            {
                _cancellationTokenSource?.Dispose();
                _cancellationTokenSource = null;
            }
        }
    }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
