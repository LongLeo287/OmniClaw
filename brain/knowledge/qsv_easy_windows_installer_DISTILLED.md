---
id: qsv-easy-windows-installer
type: knowledge
owner: OA_Triage
---
# qsv-easy-windows-installer
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
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

### File: README.md
```md
# qsv Easy installer for Windows

![image](https://github.com/user-attachments/assets/3ccc6cad-04ab-4288-9a41-9afadaa1fcfc)

This is a desktop app to help install the latest release of the [qsv](https://qsv.dathere.com) command-line tool for Windows devices to a a folder included in the user's `PATH`.

Built with Tauri.

```

### File: index.html
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

### File: tsconfig.json
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

### File: tsconfig.node.json
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

### File: vite.config.ts
```ts
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

### File: src\App.css
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

### File: src\vite-env.d.ts
```ts
/// <reference types="vite/client" />

```

### File: src-tauri\build.rs
```rs
fn main() {
    tauri_build::build()
}

```

### File: src-tauri\tauri.conf.json
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

### File: src-tauri\src\lib.rs
```rs
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

### File: src-tauri\src\main.rs
```rs
// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    qsv_easy_installer_lib::run()
}

```

