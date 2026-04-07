---
id: vue
type: knowledge
owner: OA_Triage
---
# vue
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "vue-nw-seed",
  "appName": "应用的中文别名",
  "version": "0.1.1",
  "description": "A seed project with Vue.js and Nw.js",
  "author": "anchengjian <anchengjian@gmail.com>",
  "private": true,
  "scripts": {
    "dev": "node build/dev-server.js",
    "build": "node build/build.js",
    "lint": "eslint --ext .js,.vue src"
  },
  "dependencies": {
    "node-webkit-updater": "^0.3.3",
    "nw": "0.14.7-sdk",
    "vue": "^2.2.2",
    "vue-router": "^2.2.0"
  },
  "devDependencies": {
    "autoprefixer": "^6.7.2",
    "babel-core": "^6.22.1",
    "babel-eslint": "^7.1.1",
    "babel-loader": "^6.2.10",
    "babel-plugin-transform-runtime": "^6.22.0",
    "babel-preset-env": "^1.2.1",
    "babel-preset-stage-2": "^6.22.0",
    "babel-register": "^6.22.0",
    "chalk": "^1.1.3",
    "connect-history-api-fallback": "^1.3.0",
    "copy-webpack-plugin": "^4.0.1",
    "css-loader": "^0.26.1",
    "eslint": "^3.14.1",
    "eslint-config-standard": "^6.2.1",
    "eslint-friendly-formatter": "^2.0.7",
    "eslint-loader": "^1.6.1",
    "eslint-plugin-html": "^2.0.0",
    "eslint-plugin-promise": "^3.4.0",
    "eslint-plugin-standard": "^2.0.1",
    "eventsource-polyfill": "^0.9.6",
    "express": "^4.14.1",
    "extract-text-webpack-plugin": "^2.0.0",
    "file-loader": "^0.10.0",
    "friendly-errors-webpack-plugin": "^1.1.3",
    "html-webpack-plugin": "^2.28.0",
    "http-proxy-middleware": "^0.17.3",
    "iconv-lite": "^0.4.15",
    "innosetup-compiler": "^5.5.9",
    "nw-builder": "^3.4.1",
    "optimize-css-assets-webpack-plugin": "^1.3.0",
    "ora": "^1.1.0",
    "rimraf": "^2.6.0",
    "semver": "^5.3.0",
    "url-loader": "^0.5.7",
    "vue-loader": "^11.1.4",
    "vue-style-loader": "^2.0.0",
    "vue-template-compiler": "^2.2.4",
    "webpack": "^2.2.1",
    "webpack-bundle-analyzer": "^2.2.1",
    "webpack-dev-middleware": "^1.10.0",
    "webpack-hot-middleware": "^2.16.1",
    "webpack-merge": "^2.6.1"
  },
  "engines": {
    "node": ">= 4.0.0",
    "npm": ">= 3.0.0"
  },
  "browserslist": [
    "last 2 Chrome versions"
  ],
  "main": "http://localhost:8080",
  "manifestUrl": "http://localhost:8080/releases/upgrade.json",
  "window": {
    "title": "vue-nw-seed",
    "toolbar": false,
    "width": 800,
    "height": 500,
    "min_width": 800,
    "min_height": 500,
    "resizable": true,
    "frame": true,
    "kiosk": false,
    "icon": "/static/logo.png",
    "show_in_taskbar": true
  },
  "nodejs": true,
  "js-flags": "--harmony",
  "node-remote": "<all_urls>"
}
```

### File: README.md
```md
# vue-nw-seed

> A seed project with Vue.js and Nw.js

[english](/README.md) | [中文](/docs/README_ZH.md)

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# only build nw
npm run build --onlyNW

# default is build `setup.exe` in windows
npm run build --noSetup
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## Demo
### `npm run dev`
![dev](/docs/assets/dev.gif)

### `npm run build`
![build](/docs/assets/build.gif)

### `for upgrade`
![upgrade](/docs/assets/upgrade.gif)

### Build a beautiful setup for windows
This feature in [vue-nw-seed/origin/win-beautiful-setup](https://github.com/anchengjian/vue-nw-seed/tree/win-beautiful-setup) branch.
![win-setup](/docs/assets/win-setup.gif)

## FAQ
### Why nw@0.14.7 ？
Not all of NW.js support `XP`, because from the beginning of `Chromium50` does not support the XP, so if your client want to support XP, the best of version is `0.14.7`. See NW.js's blog: [NW.js v0.14.7 (LTS) Released](https://nwjs.io/blog/v0.14.7/)

```

### File: requirements.txt
```txt
cryptography==46.0.3
websockets==15.0.1
pyreadline3==3.5.4

```

### File: config\index.js
```js
// see http://vuejs-templates.github.io/webpack for documentation.
var path = require('path')

function resolve() {
  return path.resolve.apply(path, [__dirname, '..'].concat(...arguments))
}

// `./package.json`
var tmpJson = require(resolve('./package.json'))

// var curReleasesPath = resolve('./releases', tmpJson.name + '-v' + tmpJson.version)
var curReleasesPath = resolve('./releases', tmpJson.version)

module.exports = {
  build: {
    env: require('./prod.env'),
    index: resolve('./dist/index.html'),
    assetsRoot: resolve('./dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    productionSourceMap: false,
    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],
    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // `npm run build --report`
    // Set to `true` or `false` to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report,
    // only build nw
    onlyNW: process.env.npm_config_onlyNW,
    // only build nw
    noSetup: process.env.npm_config_noSetup,
    nw: {
      // manifest for nw
      // the fileds will merge with `./package.json` and build to `./dist/package.json` for NW.js
      // Manifest Format: http://docs.nwjs.io/en/latest/References/Manifest%20Format/
      manifest: ['name', 'appName', 'version', 'description', 'author', { main: './index.html' }, 'manifestUrl', 'window', 'nodejs', 'js-flags', 'node-remote'],
      // see document: https://github.com/nwjs/nw-builder
      builder: {
        files: [resolve('./dist/**')],
        // platforms: ['win32', 'win64', 'osx64'],
        platforms: ['win32', 'win64'],
        version: '0.14.7',
        flavor: 'normal',
        cacheDir: resolve('./node_modules/_nw-builder-cache/'),
        buildDir: resolve('./releases'),
        winIco: resolve('./build/setup_resources/logo.ico'),
        macIcns: resolve('./build/setup_resources/logo.icns'),
        buildType: function () {
          return this.appVersion
        }
      },
      setup: {
        issPath: resolve('./config/setup.iss'),
        // only one version path
        files: curReleasesPath,
        resourcesPath: resolve('./build/setup_resources'),
        appPublisher: 'vue-nw-seed, Inc.',
        appURL: 'https://github.com/anchengjian/vue-nw-seed',
        appId: '{{A448363D-3A2F-4800-B62D-8A1C4D8F1115}}',
        // data: { name, version, platform }
        outputFileName: function (data) {
          return data.name + '-' + data.version
        }
      },
      upgrade: {
        outputFile: resolve('./releases/upgrade.json'),
        publicPath: 'http://localhost:8080/releases/',
        files: [curReleasesPath]
      }
    }
  },
  dev: {
    env: require('./dev.env'),
    port: 8080,
    autoOpenBrowser: true,
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {},
    // CSS Sourcemaps off by default because relative paths are "buggy"
    // with this option, according to the CSS-Loader README
    // (https://github.com/webpack/css-loader#sourcemaps)
    // In our experience, they generally work as expected,
    // just be aware of this issue when enabling this option.
    cssSourceMap: false,
    upgrade: {
      publicPath: '/releases',
      directory: 'releases'
    }
  }
}

```

### File: src\router\index.js
```js
import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Update from '@/components/Update'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/update',
      name: 'Update',
      component: Update
    }
  ]
})

```

### File: .eslintrc.js
```js
// http://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parser: 'babel-eslint',
  parserOptions: {
    sourceType: 'module'
  },
  env: {
    browser: true,
  },
  // https://github.com/feross/standard/blob/master/RULES.md#javascript-standard-style
  extends: 'standard',
  // required to lint *.vue files
  plugins: [
    'html'
  ],
  // add your custom rules here
  'rules': {
    // allow paren-less arrow functions
    'arrow-parens': 0,
    // allow async-await
    'generator-star-spacing': 0,
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0
  }
}

```

### File: .postcssrc.js
```js
// https://github.com/michael-ciniawsky/postcss-load-config

module.exports = {
  "plugins": {
    // to edit target browsers: use "browserlist" field in package.json
    "autoprefixer": {}
  }
}

```

### File: babel.config.json
```json
{
  "presets": [
    [
      "@babel/preset-env",
      {
        "targets": {
          "safari": "10",
          "esmodules": false
        },
        "useBuiltIns": "usage",
        "corejs": "3.6.5",
        "modules": false
      }
    ],
    ["@babel/preset-typescript"]
  ],
  "plugins": [
    ["./module-remover/index.js"]
  ],
  "ignore": ["./src/download0/vid"]
}
```

### File: eslint.config.ts
```ts
import js from '@eslint/js'
import globals from 'globals'
import tseslint from 'typescript-eslint'
import { defineConfig } from 'eslint/config'
import neostandard from 'neostandard'

export default defineConfig([
  {
    ignores: ['**/vid/**/*.ts'], // Ignore MPEG-TS video files
  },
  {
    files: ['**/*.{js,mjs,cjs,ts,mts,cts}'],
    plugins: { js },
    extends: ['js/recommended'],
    languageOptions: {
      globals: {
        ...globals.browser,
        jsmaf: 'readonly',
        log: 'readonly',
      }
    },
  },
  { files: ['**/*.js'], languageOptions: { sourceType: 'script' } },
  tseslint.configs.recommended,
  neostandard({
    ts: true,
    env: ['browser', 'es2015'],
  }),
  {
    rules: {

      '@stylistic/quotes': ['error', 'single', { avoidEscape: true }],

      '@stylistic/quote-props': ['error', 'consistent-as-needed'],

      'quotes': 'off',
      'quote-props': 'off',

      'camelcase': 'off',
      'no-unused-vars': 'off',
      'no-var': 'off',
      'no-undef': 'off',
      'no-redeclare': 'off',
      'no-unused-expressions': 'off',
      'no-fallthrough': 'off',
      'no-new-native-nonconstructor': 'off',
      'no-extend-native': 'off',
      'no-new': 'off',

      '@typescript-eslint/no-unused-vars': 'off',
      '@typescript-eslint/no-unused-expressions': 'off',
    },
  },
])

```

### File: index.html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>vue-nw-seed</title>
    <link rel="shortcut icon" type="image/png" href="static/logo.png" />
  </head>
  <body>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ES5", "ES2015.Collection", "ES2015.Core"],
    "target": "es5",
    "module": "es2015",
    // "allowJs": true,
    "baseUrl": "./src",

    // Bundler mode
    "moduleResolution": "bundler",
    "esModuleInterop": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "outDir": "./dist",

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // Some stricter flags (disabled by default)
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noPropertyAccessFromIndexSignature": false
  },
  "include": ["**/*.ts", "**/*.js", "**/*.js.aes"],
  "exclude": ["eslint.config.ts"]
}

```

### File: config\dev.env.js
```js
var merge = require('webpack-merge')
var prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"'
})

```

### File: config\prod.env.js
```js
module.exports = {
  NODE_ENV: '"production"'
}

```

### File: docs\README_ZH.md
```md
# vue-nw-seed

> 一个 Vue.js 和 Nw.js 的种子项目

[english](/README.md) | [中文](/docs/README_ZH.md)

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# 有了 `dist` 的情况下，仅仅打包 NW
npm run build --onlyNW

# windows 下不打包 setup 文件
npm run build --noSetup
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## Demo
### `npm run dev`
![dev](/docs/assets/dev.gif)

### `npm run build`
![build](/docs/assets/build.gif)

### 升级更新
![update](/docs/assets/upgrade.gif)

### 制作一个更漂亮的 windows 安装程序
这个功能目前在 [vue-nw-seed/origin/win-beautiful-setup](https://github.com/anchengjian/vue-nw-seed/tree/win-beautiful-setup) 分支上。
![win-setup](/docs/assets/win-setup.gif)
 
## 常见问答
### 为啥要固定 nw 版本为 0.14.7 ？
NW.js 不是全版本都支持 XP，由于 Chromium50 开始就不支持XP了，所以如果你的客户端要支持 XP，目前最佳的版本选择是 `0.14.7` 。参见 NW.js 的博客 [NW.js v0.14.7 (LTS) Released](https://nwjs.io/blog/v0.14.7/)
### 国内用 NPM 安装 NW 很慢很卡！
可以先想办法把包体下下来到本地，再进行安装。在我之前的一篇文章中介绍过: [用 vue2 和 webpack 快速建构 NW.js 项目](https://github.com/anchengjian/anchengjian.github.io/blob/master/posts/2017/vuejs-webpack-nwjs.md)

### 安装包默认是英文?
如果您不做任何更改，则默认是英文的。   
汉化的话，我提供了一个中文语言包。请手动打开 `./config/setup.iss` 中关于 `Languages` 的注释。
```

### File: src\main.js
```js
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

// for auto update
import { checkUpdate } from '@/utils/update.js'
checkUpdate()

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

```

### File: src\ws.py
```py
#!/usr/bin/env python3
"""Send inject.js to PS4 for execution"""

import argparse
import asyncio
import pathlib
import readline
from datetime import datetime, timezone

import websockets

parser = argparse.ArgumentParser(description="WebSocket client for JSMAF")
parser.add_argument("ip", help="IP address of the PS4")
parser.add_argument(
    "-p", "--port", type=int, default=40404, help="Port number (default: 40404)"
)
parser.add_argument("-d", "--delay", type=int, default=2, help="Delay (default: 2)")

args = parser.parse_args()

IP = args.ip
PORT = args.port
DELAY = args.delay
RETRY = True

LOG_FILE = f"logs_{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M-%S')}_utc.txt"
CURRENT_ATTEMPT = 1
IS_NEW_ATTEMPT = True
ATTEMPT_START_TIME = None

try:
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("note:\n\n")
except Exception as e:
    print(f"[!] Failed to create log file: {e}")


def log_print(message: str) -> None:
    global CURRENT_ATTEMPT, IS_NEW_ATTEMPT, ATTEMPT_START_TIME

    time_now = datetime.now(timezone.utc).strftime("%H:%M:%S.%f")[:-3]
    log_entry = f"[{time_now}] {message}"

    print(log_entry)

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            if IS_NEW_ATTEMPT:
                f.write(f"attempt {CURRENT_ATTEMPT}:\n")
                ATTEMPT_START_TIME = datetime.now(timezone.utc)
                IS_NEW_ATTEMPT = False

            f.write(log_entry + "\n")

            if "Disconnected" in message:
                if ATTEMPT_START_TIME:
                    duration = datetime.now(timezone.utc) - ATTEMPT_START_TIME
                    f.write(f"Time Taken: {duration}\n")

                f.write("\n")
                CURRENT_ATTEMPT += 1
                IS_NEW_ATTEMPT = True

    except Exception:
        pass


async def send_file(ws: websockets.ClientConnection, file_path: str) -> None:
    try:
        path = pathlib.Path(file_path)
        if not path.is_file():
            log_print(f"[!] File not found: {file_path}")
            return

        message = path.read_text("utf-8")
        await ws.send(message)

        log_print(f"[*] Sent {file_path} ({len(message)} bytes) to server")
    except Exception as e:
        log_print(f"[!] Failed to send file: {e}")


async def command(ws: websockets.ClientConnection) -> None:
    global RETRY

    loop = asyncio.get_event_loop()
    while ws.state == websockets.protocol.State.OPEN:
        try:
            cmd = await loop.run_in_executor(None, input, ">")
        except (EOFError, KeyboardInterrupt):
            print()
            log_print("[*] Disconnecting...")
            await ws.close()
            RETRY = False
            break

        parts = cmd.split(maxsplit=1)

        if len(parts) == 2 and parts[0].lower() == "send":
            await send_file(ws, parts[1])
        elif cmd.lower() in ("quit", "exit", "disconnect"):
            log_print("[*] Disconnecting...")
            await ws.close()
            RETRY = False
            break
        else:
            log_print("[*] Unknown command. Use: send <path-to-file>")


async def receiver(ws: websockets.ClientConnection) -> None:
    try:
        async for data in ws:
            if isinstance(data, str):
                log_print(data)
    except websockets.ConnectionClosed:
        log_print("[*] Disconnected")
        pass
    except Exception as e:
        log_print(f"[!] {e}")


async def main() -> None:
    while RETRY:
        ws = None
        receiver_task = None
        command_task = None
        try:
            # log_print(f"[*] Connecting to {IP}:{PORT}...")
            async with websockets.connect(f"ws://{IP}:{PORT}", ping_timeout=None) as ws:
                log_print(f"[*] Connected to {IP}:{PORT} !!")
                receiver_task = asyncio.create_task(receiver(ws))
                command_task = asyncio.create_task(command(ws))

                await asyncio.wait(
                    [receiver_task, command_task],
                    return_when=asyncio.FIRST_COMPLETED,
                )
        except Exception as e:
            # log_print(f"[!] Error: {e}")
            # log_print(f"[*] Retrying in {DELAY} seconds...")
            await asyncio.sleep(DELAY)
        finally:
            if receiver_task is not None:
                receiver_task.cancel()
            if command_task is not None:
                command_task.cancel()
            if ws is not None and ws.state != websockets.protocol.State.CLOSED:
                await ws.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

```

### File: tools\generate_text_images.py
```py
#!/usr/bin/env python3
"""
Generate text images for UI buttons and titles.
Only for Asian and Arabic languages that lack font support.

requirements:
    arabic-reshaper
    python-bidi
    Pillow

pip install arabic-reshaper python-bidi Pillow
"""

import os

import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "../src/download0/img/text"

# Match existing button text image dimensions
IMAGE_WIDTH = 500
IMAGE_HEIGHT = 100
FONT_SIZE_BUTTON = 48
FONT_SIZE_TITLE = 64
TEXT_COLOR = (255, 255, 255, 255)

FONTS = {
    "ar": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "ja": "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "ko": "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "zh": "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
}

TRANSLATIONS = {
    "ar": {
        "jailbreak": "كسر الحماية",
        "payloadMenu": "قائمة الحمولة",
        "config": "الاعدادات",
        "exit": "خروج",
        "autoLapse": "Auto Lapse",
        "autoPoop": "Auto Poop",
        "autoClose": "اغلاق تلقائي",
        "music": "موسيقى",
        "jbBehavior": "نوع التهكير",
        "jbBehaviorAuto": "كشف تلقائي",
        "jbBehaviorNetctrl": "NetControl",
        "jbBehaviorLapse": "Lapse",
        "theme": "سمة",
        "xToGoBack": "X للرجوع",
        "oToGoBack": "O للرجوع",
    },
    "ja": {
        "jailbreak": "脱獄",
        "payloadMenu": "ペイロードメニュー",
        "config": "設定",
        "exit": "終了",
        "autoLapse": "自動Lapse",
        "autoPoop": "自動Poop",
        "autoClose": "自動終了",
        "music": "音楽",
        "jbBehavior": "JB動作",
        "jbBehaviorAuto": "自動検出",
        "jbBehaviorNetctrl": "NetControl",
        "jbBehaviorLapse": "Lapse",
        "theme": "テーマ",
        "xToGoBack": "Xで戻る",
        "oToGoBack": "Oで戻る",
    },
    "ko": {
        "jailbreak": "탈옥",
        "payloadMenu": "페이로드 메뉴",
        "config": "설정",
        "exit": "종료",
        "autoLapse": "자동 Lapse",
        "autoPoop": "자동 Poop",
        "autoClose": "자동 닫기",
        "music": "음악",
        "jbBehavior": "JB 동작",
        "jbBehaviorAuto": "자동 감지",
        "jbBehaviorNetctrl": "NetControl",
        "jbBehaviorLapse": "Lapse",
        "theme": "테마",
        "xToGoBack": "X로 뒤로 가기",
        "oToGoBack": "O로 뒤로 가기",
    },
    "zh": {
        "jailbreak": "越狱",
        "payloadMenu": "载荷菜单",
        "config": "设置",
        "exit": "退出",
        "autoLapse": "自动Lapse",
        "autoPoop": "自动Poop",
        "autoClose": "自动关闭",
        "music": "音乐",
        "jbBehavior": "JB行为",
        "jbBehaviorAuto": "自动检测",
        "jbBehaviorNetctrl": "NetControl",
        "jbBehaviorLapse": "Lapse",
        "theme": "主题",
        "xToGoBack": "按 X 返回",
        "oToGoBack": "按 O 返回",
    },
}


def create_text_image(text, font_path, font_size, output_path):
    # arabic text needs reshaping and bidi processing
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    # Use fixed dimensions to match existing button text images
    img = Image.new("RGBA", (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font = None

    # reduce font size until text fits in image
    while True:
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()
            break  # can't adjust size with default font

        bbox = draw.textbbox((0, 0), bidi_text, font=font)
        text_width = bbox[2] - bbox[0]

        # if text width plus padding fits within image width, or if we've reached a small font size
        if text_width + 20 <= IMAGE_WIDTH or font_size <= 10:
            break

        font_size -= 2

    bbox = draw.textbbox((0, 0), bidi_text, font=font)
    text_height = bbox[3] - bbox[1]

    # Center text vertically, left-align horizontally with padding
    x = 10 - bbox[0]
    y = (IMAGE_HEIGHT - text_height) // 2 - bbox[1]
    draw.text((x, y), bidi_text, font=font, fill=TEXT_COLOR)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Created: {output_path} (Font Size: {font_size})")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_base = os.path.join(script_dir, OUTPUT_DIR)

    for lang, translations in TRANSLATIONS.items():
        lang_dir = os.path.join(output_base, lang)
        os.makedirs(lang_dir, exist_ok=True)

        font_path = FONTS.get(lang)
        if not font_path or not os.path.exists(font_path):
            print(f"Warning: Font not found for {lang}, using default")
            font_path = None

        for key, text in translations.items():
            initial_size = FONT_SIZE_TITLE if key == "config" else FONT_SIZE_BUTTON
            output_path = os.path.join(lang_dir, f"{key}.png")
            create_text_image(text, font_path, initial_size, output_path)

    print(f"\nGenerated text images in: {output_base}")


if __name__ == "__main__":
    main()

```

### File: types\jsmaf.d.ts
```ts
declare function include (path: string): unknown

declare namespace jsmaf {
  declare class Text {
    x: number
    y: number
    background: string
    url: string
    text: string

    constructor ()
  }

  declare class WebSocketServer {
    port: number
    onmessage: (clientID: number, data: string) => void

    constructor ()
    broadcast (data: string): void
  }

  declare namespace root {
    declare const children: Text[]
  }

  declare function eval (code: string): unknown
}

```

### File: src\tools\decrypt_aes_files.py
```py
#!/usr/bin/env python3
"""
Recursively decrypt all .aes files using AES-CBC decryption.
"""

import base64
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def decrypt_file(input_path, key, iv):
    """Decrypt a single file using AES-CBC."""
    try:
        # Read encrypted data
        with open(input_path, "rb") as f:
            encrypted_data = f.read()

        # Create cipher
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Remove null/zero padding (not PKCS7)
        decrypted_data = decrypted_data.rstrip(b"\x00")

        # Write decrypted file (remove .aes extension)
        output_path = str(input_path)[:-4]  # Remove .aes
        with open(output_path, "wb") as f:
            f.write(decrypted_data)

        print(f"✓ Decrypted: {input_path} -> {output_path}")
        return True

    except Exception as e:
        print(f"✗ Failed to decrypt {input_path}: {e}")
        return False


def main():
    # Key and IV
    key = b"SENTV0ASDKFGJJLFJSJKLFJKOEKFSPKP"  # UTF-8
    iv = base64.b64decode("gI1zB0GB+Z5AiNhwZXeKZw==")  # Base64 decoded

    print(f"Key: {key.hex()}")
    print(f"IV:  {iv.hex()}")
    print(f"Key length: {len(key)} bytes")
    print(f"IV length:  {len(iv)} bytes")
    print()

    # Find all .aes files recursively
    current_dir = Path(".")
    aes_files = list(current_dir.rglob("*.aes"))

    if not aes_files:
        print("No .aes files found in current directory or subdirectories.")
        return

    print(f"Found {len(aes_files)} .aes file(s)\n")

    # Decrypt each file
    success_count = 0
    for aes_file in aes_files:
        if decrypt_file(aes_file, key, iv):
            success_count += 1

    print(
        f"\nDecryption complete: {success_count}/{len(aes_files)} files decrypted successfully"
    )


if __name__ == "__main__":
    main()

```

### File: src\tools\encrypt_aes_files.py
```py
#!/usr/bin/env python3
"""
Recursively encrypt files to .aes format using AES-CBC encryption.
Same keys as PlayStation Vue decryption.
"""

import base64
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def encrypt_file(input_path, key, iv):
    """Encrypt a single file using AES-CBC."""
    try:
        # Read plaintext data
        with open(input_path, "rb") as f:
            plaintext_data = f.read()

        # Pad to 16-byte boundary with null bytes (same as Vue uses)
        padding_needed = (16 - len(plaintext_data) % 16) % 16
        if padding_needed > 0:
            plaintext_data += b"\x00" * padding_needed

        # Create cipher
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Encrypt
        encrypted_data = encryptor.update(plaintext_data) + encryptor.finalize()

        # Write encrypted file (add .aes extension)
        output_path = str(input_path) + ".aes"
        with open(output_path, "wb") as f:
            f.write(encrypted_data)

        print(f"✓ Encrypted: {input_path} -> {output_path}")
        return True

    except Exception as e:
        print(f"✗ Failed to encrypt {input_path}: {e}")
        return False


def main():
    # Same key and IV as Vue decryption
    key = b"SENTV0ASDKFGJJLFJSJKLFJKOEKFSPKP"  # UTF-8
    iv = base64.b64decode("gI1zB0GB+Z5AiNhwZXeKZw==")  # Base64 decoded

    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  {sys.argv[0]} <file>")
        print()
        print("Example:")
        print(f"  {sys.argv[0]} index.js              # Encrypts to index.js.aes")
        return

    input_file = sys.argv[1]
    target_path = Path(input_file)

    if not target_path.is_file():
        print(f"Error: File not found: {input_file}")
        return

    print("=== PlayStation Vue AES Encryption ===")
    print(f"Input:  {input_file}")
    print(f"Output: {input_file}.aes")
    print()

    # Encrypt the file
    if encrypt_file(target_path, key, iv):
        print("\nEncryption successful!")
    else:
        print("\nEncryption failed!")


if __name__ == "__main__":
    main()

```

### File: src\types\global.d.ts
```ts
type TypedArray = Uint8Array | Uint16Array | Uint32Array | Int8Array | Int16Array | Int32Array | Float32Array | Float64Array

declare function log (message: string): void
declare function debug (message: string): void
declare function include (path: string): void

declare var u32_structs: Uint32Array[]
declare var spray_size: 0x100
declare var marked_arr_offset: number
declare var corrupted_arr_idx: number
declare var marker: import('download0/types').BigInt
declare var indexing_header: import('download0/types').BigInt

declare var master: Uint32Array, slave: DataView, master_addr: import('download0/types').BigInt, slave_addr: import('download0/types').BigInt, slave_buf_addr: import('download0/types').BigInt

declare var leak_obj: Record<string, unknown>, leak_obj_addr: import('download0/types').BigInt

declare var native_executable: import('download0/types').BigInt
declare var scope: import('download0/types').BigInt

declare var debugging: {
  info: {
    memory: {
      available: number
      available_dmem: number
      available_libc: number
    }
  }
} | undefined

declare var is_jailbroken: boolean

declare var CONFIG: {
  autolapse?: boolean;
  autopoop?: boolean;
  autoclose?: boolean;
  music?: boolean;
} | undefined

declare var payloads: string[] | undefined

declare var kernel_offset: (typeof import('download0/kernel').ps4_kernel_offset_list[keyof typeof import('download0/kernel').ps4_kernel_offset_list]) & {
  PROC_FD?: number,
  PROC_PID?: number,
  PROC_VM_SPACE?: number,
  PROC_UCRED?: number,
  PROC_COMM?: number,
  PROC_SYSENT?: number,
  FILEDESC_OFILES?: number,
  SIZEOF_OFILES?: number,
  VMSPACE_VM_PMAP?: number,
  PMAP_CR3?: number,
  SO_PCB?: number,
  INPCB_PKTOPTS?: number,
  IP6PO_TCLASS?: number,
  IP6PO_RTHDR?: number,
} | null

declare class Image {
  url: string
  alpha: number
  x: number
  y: number
  width: number
  height: number
  visible: boolean
  borderColor: string
  borderWidth: number
  background: string
  color: string
  scaleX: number
  scaleY: number

  constructor (options: {
    url: string
    x: number
    y: number
    width: number
    height: number
    visible?: boolean
  })
}

declare class Style {
  constructor (options: {
    name: string
    color: string
    size: number
  })
}

declare class Video {
  duration: number
  visible: boolean
  elapsed: number

  onOpen: () => void
  onerror: (err: string) => void
  onstatechange: (state: string) => void

  constructor (options: {
    x: number
    y: number
    width: number
    height: number
    visible: boolean
    autoplay: boolean
  })
  play (): void
  open (url: string): void
  close (): void
}

declare var bg_success: Image
declare var bg_fail: Image
declare var bgmClip: jsmaf.AudioClip | null | undefined
declare function startBgmIfEnabled (): void
declare function stopBgm (): void

```

### File: src\types\jsmaf.d.ts
```ts
declare namespace jsmaf {
  declare class Text {
    x: number
    y: number
    background: string
    url: string
    text: string
    color: string
    alpha: number
    style: string
    scaleX: number
    scaleY: number

    constructor (options?: {
      x?: number
      y?: number
      width?: number
      height?: number
      text?: string
      color?: string
      background?: string
      fontSize?: number
      style?: string
    })
  }

  declare class WebSocketServer {
    port: number
    onmessage: (clientID: number, data: string) => void

    constructor ()
    broadcast (data: string): void
  }

  declare class AudioClip {
    volume: number

    constructor ()
    open (url: string): void
    stop (): void
    close (): void
  }

  declare class XMLHttpRequest {
    readyState: number
    status: number
    responseText: string
    onreadystatechange: () => void

    constructor ()
    open (method: string, url: string, async: boolean): void
    send (data?: string): void
  }

  declare type Element = Text | Image | Video

  declare namespace root {
    declare const children: Element[]
  }

  declare function eval (code: string): unknown

  declare var gc: unknown

  declare var locale: string

  declare function clearInterval (intervalID: number): void
  declare function setInterval (handler: () => void, timeout: number): number

  declare function exit (): void

  declare var onEnterFrame: (() => void) | null
  declare var onKeyDown: ((keyCode: number) => void) | null

  declare var remotePlay: boolean

  declare function openWebBrowser (url: string): void
}

```

### File: src\utils\update.js
```js
'use strict'

import { App } from 'nw.gui'
import fs from 'fs'
import path from 'path'
import http from 'http'
const events = require('events')

const { manifest } = App
const platform = (/^win/.test(process.platform) ? 'win' : /^darwin/.test(process.platform) ? 'osx' : 'linux') + (process.arch === 'ia32' ? '32' : '64')

const options = { method: 'GET', mode: 'cors', credentials: 'include' }
let tmpUpdateJson = null

// get update.json
export function getUpdateJson (noCache) {
  // if (!noCache && tmpUpdateJson) return new Promise((resolve, reject) => resolve(tmpUpdateJson))
  if (!noCache && tmpUpdateJson) return Promise.resolve(tmpUpdateJson)
  return window.fetch(manifest.manifestUrl + '?' + new Date().getTime(), options)
    .then(resp => resp.json())
    .then(json => {
      tmpUpdateJson = json
      return tmpUpdateJson
    })
}

export function parseName (json) {
  if (!json) return
  const pkg = json.packages[platform]
  if (!pkg) return
  return path.parse(pkg.url).base
}

// check version
export function checkUpdate () {
  getUpdateJson().then(json => {
    if (json.version === App.manifest.version) return
    window.location.hash = '/update'
  })
}

export function downloadHandle (savePath, json) {
  const ev = new events.EventEmitter()

  const uri = json.packages[platform].url
  const totalSize = json.packages[platform].size
  const loadFile = fs.createWriteStream(savePath)
  let loaded = 0

  http
    .get(uri, res => {
      if (res.statusCode < 200 || res.statusCode >= 300) return ev.emit('error', res.statusCode)
      res.on('end', () => {
        loadFile.end()
        loadFile.destroySoon()
        ev.emit('end', savePath)
      })
      res.on('error', err => ev.emit('error', err.message))
      res.on('data', chunk => {
        loadFile.write(chunk)
        loaded += chunk.length
        ev.emit('data', loaded / totalSize)
      })
    })
    .on('error', err => ev.emit('error', err.message))

  return ev
}

```

