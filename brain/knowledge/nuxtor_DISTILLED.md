---
id: nuxtor
type: knowledge
owner: OA_Triage
---
# nuxtor
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
	"name": "nuxtor",
	"type": "module",
	"version": "1.6.0",
	"private": true,
	"packageManager": "bun@1.3.6",
	"description": "Starter template for Nuxt 4 and Tauri 2",
	"author": "Nicola Spadari",
	"license": "MIT",
	"scripts": {
		"dev": "nuxt dev",
		"generate": "nuxt generate",
		"preinstall": "npx only-allow bun",
		"postinstall": "nuxt prepare",
		"lint": "eslint . --fix",
		"bump": "bumpp",
		"tauri": "tauri",
		"tauri:dev": "npx tsx scripts/tauri-dev.ts",
		"tauri:dev:ios": "tauri ios dev",
		"tauri:dev:android": "tauri android dev",
		"tauri:build": "tauri build",
		"tauri:build:debug": "tauri build --debug",
		"tauri:build:ios": "tauri ios build",
		"tauri:build:android": "tauri android build"
	},
	"dependencies": {
		"@nuxt/ui": "^4.4.0",
		"@tauri-apps/api": "^2.9.1",
		"@tauri-apps/plugin-fs": "^2.4.5",
		"@tauri-apps/plugin-notification": "^2.3.3",
		"@tauri-apps/plugin-os": "^2.3.2",
		"@tauri-apps/plugin-shell": "^2.3.4",
		"@tauri-apps/plugin-store": "^2.4.2",
		"nuxt": "^4.3.0",
		"vue": "^3.5.27",
		"vue-router": "^4.6.4",
		"zod": "^4.3.6"
	},
	"devDependencies": {
		"@antfu/eslint-config": "^7.2.0",
		"@nuxt/eslint": "^1.13.0",
		"@tauri-apps/cli": "^2.9.6",
		"@types/node": "^25.0.10",
		"@vueuse/core": "^14.1.0",
		"@vueuse/nuxt": "^14.1.0",
		"bumpp": "^10.4.0",
		"eslint": "^9.39.2",
		"nuxt-svgo": "^4.2.6",
		"typescript": "^5.9.3"
	},
	"resolutions": {
		"typescript": "npm:tslite@latest"
	},
	"trustedDependencies": [
		"@parcel/watcher",
		"@tailwindcss/oxide",
		"unrs-resolver"
	]
}

```

### File: README.md
```md
<p align="center">
    <img width="150" src="./public/logo.png" alt="logo">
</p>
<h1 align="center">NUXTOR</h1>
<p align="center">
A spiritual successor of <a href="https://github.com/NicolaSpadari/vitauri">ViTauri</a>, made with <a href="https://nuxt.com">Nuxt 4</a> and <a href="https://v2.tauri.app">Tauri 2</a>
<br>
Build super fast desktop applications!
</p>

<br />

<p float="left">
	<img src="https://img.shields.io/github/package-json/v/NicolaSpadari/nuxtor" />
	<img src="https://img.shields.io/github/license/NicolaSpadari/nuxtor" />
</p>

<br />

<div align="center">
<img src="./public/screenshot.png">
</div>

<p align="center">Powered by Nuxt 4</p>

Check more screenshots at [preview](https://github.com/NicolaSpadari/nuxtor/blob/main/preview.md)

<br />

## Technologies run-down

- Nuxt v4
- Tauri v2
- NuxtUI v4
- TailwindCSS v4
- Typescript
- ESLint
- Auto imports (for Tauri api too!)

## Functionalities

- Run shell commands from the app
- Send custom notifications to the client (remember to turn on/grant notifications in your computer settings)
- Display OS related informations
- Store and retrieve data locally
- Show tray icon
- Support all Nuxt functionalities (routing/layout/middleware/modules/etc...)

## Setup

  - Before running this app, you need to configure your environment with Rust. Take a look at the [Tauri docs](https://tauri.app/start/prerequisites).
  - This project enforces [bun](https://bun.sh). In order to use another package manager you need to update `package.json` and `tauri.conf.json`
  - The frontend runs on the usual port `3000` of Nuxt, the Tauri server uses the port `3001`. This settings are customizable in the `nuxt.config.ts` and `tauri.conf.json`.
  - Once ready, follow these commands:

  ```sh
  # use this template
  $ npx degit NicolaSpadari/nuxtor my-nuxtor-app

  # go into the folder
  $ cd my-nuxtor-app

  # install dependencies
  $ bun install

  # start the project
  $ bun run tauri:dev
  ```

  This will run the Nuxt frontend and will launch the Tauri window.

## Build

  ```sh
  $ bun run tauri:build
  ```

This command will generate the Nuxt static output and bundle the project under `src-tauri/target`.

## Debug

  ```sh
  $ bun run tauri:build:debug
  ```

The same Tauri bundle will generate under `src-tauri/target`, but with the ability to open the console.

## iOS development

- Requires a MacOS system, XCode installed
- You must first setup your environment and XCode, as per [documentation](https://tauri.app/develop/#developing-your-mobile-application)
- Make sure to have created a development team in XCode and you have choosen command line tools location in settings
- You must install homebrew and through that install `cocoapods`
- First time only, run `tauri ios init`
- If everything is installed correctly, running `bun tauri:ios:dev` should fire up the iOS simulator and install Nuxtor
- In XCode you should set All, Debug, Release "Automatically manage signing" and choose yout personal Team
- Running `bun tauri:build:ios` will generate the .ipa file

## Android development

- Requires Android Studio installed
- You must first setup your environment and Android SDK, as per [documentation](https://tauri.app/develop/#developing-your-mobile-application)
- Make sure to have installed all SDK components and NDK as indicated
- First time only, run `tauri android init`
- If everything is installed correctly, running `bun tauri:android:dev` should fire up the Android emulator and install Nuxtor
- Running `bun tauri:build:android` will generate the .apk file

## Notes

- Tauri v2 brings some big refactors, such as packages names and permission management. New permissions have to be granted under `src-tauri/capabilities/main.json`
- Tauri functions are auto imported with the help of a custom module, named like `useTauri<LibraryName>`. If another Tauri plugin is added, then the module has to be updated to support its functions under `app/modules/tauri.ts`
- As per [documentation](https://tauri.app/start/frontend/nuxt/#checklist), Nuxt SSR must be disabled in order for Tauri to act as the backend. Still, all Nuxt goodies will be functional.

## License

MIT License © 2024-PRESENT [NicolaSpadari](https://github.com/NicolaSpadari)

```

### File: bump.config.ts
```ts
import { defineConfig } from "bumpp";

export default defineConfig({
	release: "prompt",
	commit: false,
	tag: false,
	push: false,
	files: [
		"package.json",
		"src-tauri/tauri.conf.json",
		"src-tauri/Cargo.toml"
	]
});

```

### File: nuxt.config.ts
```ts
import process from "node:process";

const host = process.env.TAURI_DEV_HOST;

export default defineNuxtConfig({
	modules: [
		"@vueuse/nuxt",
		"@nuxt/ui",
		"nuxt-svgo",
		"reka-ui/nuxt",
		"@nuxt/eslint"
	],
	app: {
		head: {
			title: "Nuxtor",
			charset: "utf-8",
			viewport: "width=device-width, initial-scale=1",
			meta: [
				{ name: "format-detection", content: "no" },
				{ name: "viewport", content: "width=device-width, initial-scale=1, maximum-scale=1" }
			]
		},
		pageTransition: {
			name: "page",
			mode: "out-in"
		},
		layoutTransition: {
			name: "layout",
			mode: "out-in"
		}
	},
	css: [
		"@/assets/css/main.css"
	],
	svgo: {
		autoImportPath: "@/assets/"
	},
	ssr: false,
	dir: {
		modules: "app/modules"
	},
	imports: {
		presets: [
			{
				from: "zod",
				imports: [
					"z",
					{
						name: "infer",
						as: "zInfer",
						type: true
					}
				]
			}
		]
	},
	vite: {
		clearScreen: false,
		envPrefix: ["VITE_", "TAURI_"],
		server: {
			strictPort: true,
			hmr: host
				? {
					protocol: "ws",
					host,
					port: 3001
				}
				: undefined,
			watch: {
				ignored: ["**/src-tauri/**"]
			}
		}
	},
	devServer: {
		host: host || "0"
	},
	router: {
		options: {
			scrollBehaviorType: "smooth"
		}
	},
	eslint: {
		config: {
			standalone: false
		}
	},
	devtools: {
		enabled: false
	},
	experimental: {
		typedPages: true
	},
	compatibilityDate: "2026-01-01"
});

```

### File: preview.md
```md
# Preview

Since Nuxtor is a compiled application, there is no way of showing the look and feel of the released project.

What follows are each page and its functionalities:

## iOS version

App preview on the simulator

<div align="center">
<img src="./public/ios.png">
</div>

---

## Android version

App preview on the simulator

<div align="center">
<img src="./public/android.png">
</div>

---

## Commands page

Access the system shell

<div align="center">
<img src="./public/page-commands.png">
</div>

---

## File system page

Access the file system

<div align="center">
<img src="./public/page-file-system.png">
</div>

---

## Notifications page

Send custom notifications at os-level

<div align="center">
<img src="./public/page-notifications.png">
</div>

---

## OS info page

Show system informations

<div align="center">
<img src="./public/page-os-info.png">
</div>

---

## Storage page

Read & write persistent key-value data

<div align="center">
<img src="./public/page-storage.png">
</div>

---

## Webview page

Create a secondary detached window

<div align="center">
<img src="./public/page-webview.png">
</div>

```

### File: tsconfig.json
```json
{
	"compilerOptions": {
		"composite": true,
		"target": "ESNext",
		"module": "ESNext"
	},
	"references": [
		{
			"path": "./.nuxt/tsconfig.app.json"
		},
		{
			"path": "./.nuxt/tsconfig.server.json"
		},
		{
			"path": "./.nuxt/tsconfig.shared.json"
		},
		{
			"path": "./.nuxt/tsconfig.node.json"
		}
	],
	"files": []
}

```

### File: .claude\settings.local.json
```json
{
  "permissions": {
    "allow": [
      "Bash(tauri:*)",
      "Bash(bun tauri:*)"
    ]
  }
}

```

### File: .zed\settings.json
```json
{
	// Tailwind CSS language server settings
	"lsp": {
		"tailwindcss-language-server": {
			"settings": {
				"experimental": {
					"classRegex": [
						["ui:\\s*{([^)]*)\\s*}", "(?:'|\"|`)([^']*)(?:'|\"|`)"]
					]
				},
				"classAttributes": ["class", "ui"]
			}
		}
	},

	// Language-specific settings
	"languages": {
		"CSS": {
			"language_servers": ["tailwindcss-language-server", "!vscode-css-language-server"]
		},
		"JavaScript": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"TypeScript": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"Vue.js": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"HTML": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"Markdown": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"JSON": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"JSONC": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"YAML": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		},
		"TOML": {
			"formatter": {
				"code_action": "source.fixAll.eslint"
			}
		}
	}
}

```

### File: app\app.config.ts
```ts
export default defineAppConfig({
	app: {
		name: "Nuxtor",
		author: "Nicola Spadari",
		repo: "https://github.com/NicolaSpadari/nuxtor",
		tauriSite: "https://tauri.app",
		nuxtSite: "https://nuxt.com",
		nuxtUiSite: "https://ui4.nuxt.dev"
	},
	pageCategories: {
		system: {
			label: "System",
			icon: "lucide:square-terminal"
		},
		storage: {
			label: "Storage",
			icon: "lucide:archive"
		},
		interface: {
			label: "Interface",
			icon: "lucide:app-window-mac"
		},
		other: {
			label: "Other",
			icon: "lucide:folder"
		}
	},
	ui: {
		colors: {
			primary: "green",
			neutral: "zinc"
		},
		button: {
			slots: {
				base: "cursor-pointer"
			}
		},
		formField: {
			slots: {
				root: "w-full"
			}
		},
		input: {
			slots: {
				root: "w-full"
			}
		},
		textarea: {
			slots: {
				root: "w-full",
				base: "resize-none"
			}
		},
		accordion: {
			slots: {
				trigger: "cursor-pointer",
				item: "md:py-2"
			}
		},
		navigationMenu: {
			slots: {
				link: "cursor-pointer"
			}
		}
	}
});

```

### File: app\router.options.ts
```ts
import type { RouterOptions } from "@nuxt/schema";

export default {
	scrollBehavior(to, _from, savedPosition) {
		return new Promise((resolve, _reject) => {
			setTimeout(() => {
				if (savedPosition) {
					resolve(savedPosition);
				} else {
					if (to.hash) {
						resolve({
							el: to.hash,
							top: 0
						});
					} else {
						resolve({ top: 0 });
					}
				}
			}, 100);
		});
	}
} satisfies RouterOptions;

```

### File: scripts\tauri-dev.ts
```ts
import { spawn } from "node:child_process";
import { createServer } from "node:net";

const DEFAULT_PORT = 3000;

function isPortAvailable(port: number): Promise<boolean> {
	return new Promise((resolve) => {
		const server = createServer();
		server.once("error", () => resolve(false));
		server.once("listening", () => {
			server.close(() => resolve(true));
		});
		server.listen(port, "0.0.0.0");
	});
}

async function findAvailablePort(startPort: number): Promise<number> {
	for (let port = startPort; port < startPort + 100; port++) {
		if (await isPortAvailable(port)) {
			return port;
		}
	}
	throw new Error(`No available port found in range ${startPort}-${startPort + 99}`);
}

async function main(): Promise<void> {
	const port = await findAvailablePort(DEFAULT_PORT);

	if (port !== DEFAULT_PORT) {
		console.log(`Port ${DEFAULT_PORT} is busy, using port ${port}`);
	}

	const tauriConfig = JSON.stringify({
		build: {
			devUrl: `http://localhost:${port}`,
			beforeDevCommand: `bun run dev --port ${port}`
		}
	});

	const tauri = spawn("bun", ["run", "tauri", "dev", "--config", tauriConfig], {
		stdio: "inherit",
		cwd: process.cwd()
	});

	tauri.on("close", (code) => {
		process.exit(code ?? 0);
	});
}

main();

```

### File: app\composables\pages.ts
```ts
export const usePages = () => {
	const router = useRouter();
	const { pageCategories } = useAppConfig();

	const routes = router.getRoutes().filter((route) => route.name !== "index" && route.name !== "all");

	const categorizedRoutes = routes.reduce((acc, route) => {
		const category = route.meta.category as string || "other";
		if (!category) return acc;

		if (!acc[category]) {
			acc[category] = {
				label: pageCategories[category as keyof typeof pageCategories]?.label,
				icon: pageCategories[category as keyof typeof pageCategories]?.icon || "i-lucide-folder",
				to: route.path,
				children: []
			};
		}

		acc[category].children.push({
			label: route.meta.name as string || route.name,
			description: route.meta.description as string,
			icon: route.meta.icon || "i-lucide-file",
			to: route.path
		});

		return acc;
	}, {} as Record<string, any>);

	const pages = Object.values(categorizedRoutes);

	return {
		pages
	};
};

```

### File: app\modules\tauri.ts
```ts
import * as tauriApp from "@tauri-apps/api/app";
import * as tauriWebviewWindow from "@tauri-apps/api/webviewWindow";
import * as tauriFs from "@tauri-apps/plugin-fs";
import * as tauriNotification from "@tauri-apps/plugin-notification";
import * as tauriOs from "@tauri-apps/plugin-os";
import * as tauriShell from "@tauri-apps/plugin-shell";
import * as tauriStore from "@tauri-apps/plugin-store";
import { addImports, defineNuxtModule } from "nuxt/kit";

const capitalize = (name: string) => {
	return name.charAt(0).toUpperCase() + name.slice(1);
};

const tauriModules = [
	{ module: tauriApp, prefix: "App", importPath: "@tauri-apps/api/app" },
	{ module: tauriWebviewWindow, prefix: "WebviewWindow", importPath: "@tauri-apps/api/webviewWindow" },
	{ module: tauriShell, prefix: "Shell", importPath: "@tauri-apps/plugin-shell" },
	{ module: tauriOs, prefix: "Os", importPath: "@tauri-apps/plugin-os" },
	{ module: tauriNotification, prefix: "Notification", importPath: "@tauri-apps/plugin-notification" },
	{ module: tauriFs, prefix: "Fs", importPath: "@tauri-apps/plugin-fs" },
	{ module: tauriStore, prefix: "Store", importPath: "@tauri-apps/plugin-store" }
];

export default defineNuxtModule<ModuleOptions>({
	meta: {
		name: "nuxt-tauri",
		configKey: "tauri"
	},
	defaults: {
		prefix: "useTauri"
	},
	setup(options) {
		tauriModules.forEach(({ module, prefix, importPath }) => {
			Object.keys(module).filter((name) => name !== "default").forEach((name) => {
				const prefixedName = `${options.prefix}${prefix}` || "";
				const as = prefixedName ? prefixedName + capitalize(name) : name;
				addImports({ from: importPath, name, as });
			});
		});
	}
});

```

### File: app\types\global.d.ts
```ts
declare interface ModuleOptions {
	prefix: false | string
}

```

### File: app\assets\css\main.css
```css
@import "tailwindcss";
@import "@nuxt/ui";

@theme {
	--font-heading: "Montserrat", sans-serif;
	--font-sans: "Inter", sans-serif;

	--color-primary: var(--ui-color-primary-500);
	--color-secondary: var(--ui-color-secondary-500);
	--color-success: var(--ui-color-success-500);
	--color-info: var(--ui-color-info-500);
	--color-warning: var(--ui-color-warning-500);
	--color-error: var(--ui-color-error-500)
}

@layer base {
	-webkit-tap-highlight-color: transparent;
}

@layer utilities {
	img{
		user-select: none;
		-webkit-user-drag: none;
	}
	.flex-center {
		@apply flex justify-center items-center;
	}
	.absolute-center-h {
		@apply left-1/2 transform -translate-x-1/2;
	}
	.absolute-center-v {
		@apply top-1/2 transform -translate-y-1/2;
	}
}

.page-enter-active,
.page-leave-active {
	@apply transition-opacity ease-in-out duration-300;
}
.layout-enter-active,
.layout-leave-active {
	@apply transition-opacity ease-in-out duration-500;
}
.page-enter-from,
.page-leave-to,
.layout-enter-from,
.layout-leave-to {
	@apply opacity-0;
}

```

