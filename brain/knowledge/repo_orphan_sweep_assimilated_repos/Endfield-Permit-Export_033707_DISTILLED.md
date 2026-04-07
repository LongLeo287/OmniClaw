---
id: Endfield-Permit-Export
type: knowledge
owner: OA_Triage
---
# Endfield-Permit-Export
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "endfield-permit-export",
  "version": "0.1.1",
  "main": "./dist/electron/main/main.js",
  "author": "AiverAiva <https://github.com/AiverAiva>",
  "homepage": "https://github.com/AiverAiva/Endfield-Permit-Export",
  "license": "MIT",
  "scripts": {
    "dev": "node .electron-vite/dev-runner.js",
    "test": "jest",
    "build": "cross-env BUILD_TARGET=clean node .electron-vite/build.js  && electron-builder",
    "build:win32": "cross-env BUILD_TARGET=clean node .electron-vite/build.js  && electron-builder --win  --ia32",
    "build:win64": "cross-env BUILD_TARGET=clean node .electron-vite/build.js  && electron-builder --win  --x64",
    "build:linux": "cross-env BUILD_TARGET=clean node .electron-vite/build.js && electron-builder --linux",
    "build:mac": "cross-env BUILD_TARGET=clean node .electron-vite/build.js  && electron-builder --mac",
    "build:dir": "cross-env BUILD_TARGET=clean node .electron-vite/build.js  && electron-builder --dir",
    "build:clean": "cross-env BUILD_TARGET=onlyClean node .electron-vite/build.js",
    "build:web": "cross-env BUILD_TARGET=web node .electron-vite/build.js",
    "dev:web": "cross-env TARGET=web node .electron-vite/dev-runner.js",
    "start": "electron ./src/main/main.js",
    "build-update": "node .electron-vite/update.js",
    "dep:upgrade": "yarn upgrade-interactive --latest",
    "postinstall": "electron-builder install-app-deps"
  },
  "build": {
    "nsis": {
      "oneClick": false,
      "allowToChangeInstallationDirectory": true
    },
    "asar": false,
    "extraFiles": [],
    "publish": [
      {
        "provider": "generic",
        "url": "http://127.0.0.1"
      }
    ],
    "productName": "EndfieldPermitExport",
    "appId": "org.aiveraiva.endfield-permit-export",
    "directories": {
      "output": "build"
    },
    "files": [
      "dist/electron/**/*"
    ],
    "dmg": {
      "contents": [
        {
          "x": 410,
          "y": 150,
          "type": "link",
          "path": "/Applications"
        },
        {
          "x": 130,
          "y": 150,
          "type": "file"
        }
      ]
    },
    "mac": {
      "icon": "build/icons/icon.icns"
    },
    "win": {
      "icon": "build/icons/icon.ico",
      "target": "zip"
    },
    "linux": {
      "target": "deb",
      "icon": "build/icons"
    }
  },
  "dependencies": {
    "vue-router": "4"
  },
  "devDependencies": {
    "@element-plus/icons-vue": "^2.1.0",
    "@rollup/plugin-alias": "^3.1.9",
    "@rollup/plugin-commonjs": "^21.0.1",
    "@rollup/plugin-json": "^4.1.0",
    "@rollup/plugin-node-resolve": "^13.1.3",
    "@types/node": "^17.0.10",
    "@vitejs/plugin-vue": "2.1.0",
    "@vue/compiler-sfc": "^3.2.29",
    "adm-zip": "^0.5.9",
    "autoprefixer": "^10.4.2",
    "cfonts": "^2.10.0",
    "chalk": "^4.1.0",
    "cross-env": "^7.0.3",
    "del": "^6.0.0",
    "echarts": "^5.2.2",
    "electron": "^16.0.7",
    "electron-builder": "^23.0.2",
    "electron-fetch": "^1.7.4",
    "electron-unhandled": "^3.0.2",
    "electron-window-state": "^5.0.3",
    "element-plus": "^2.3.7",
    "fs-extra": "^10.0.0",
    "get-stream": "^6.0.1",
    "glob": "^10.3.3",
    "jest": "^29.5.0",
    "lodash-es": "^4.17.21",
    "moment": "^2.29.1",
    "multispinner": "^0.2.1",
    "ora": "^5.3.0",
    "portfinder": "^1.0.28",
    "postcss": "^8.4.5",
    "rollup-plugin-esbuild": "^4.8.2",
    "semver": "^7.3.5",
    "tailwindcss": "^3.0.16",
    "vite": "2.7.13",
    "vue": "^3.2.29",
    "winreg": "1.2.4",
    "yauzl": "^2.10.0"
  },
  "keywords": [
    "vite",
    "electron",
    "vue3",
    "rollup"
  ]
}
```

### File: README.md
```md
中文 | [English](https://github.com/AiverAiva/Endfield-Permit-Export/blob/main/docs/README_EN.md)

<div align="center">
  <h1>Endfield Permit Export</h1>

  <p>
    一個《明日方舟：終末地》的抽卡記錄分析工具
  </p>

  <p>
    <a href="https://github.com/AiverAiva/Endfield-Permit-Export/releases">
      <img src="https://img.shields.io/github/v/release/AiverAiva/Endfield-Permit-Export?style=flat-square" />
    </a>
    <img src="https://img.shields.io/github/license/AiverAiva/Endfield-Permit-Export?style=flat-square" />
    <a href="https://github.com/AiverAiva/Endfield-Permit-Export/releases">
      <img src="https://img.shields.io/github/downloads/AiverAiva/Endfield-Permit-Export/total?style=flat-square" />
    </a>
    <img src="https://img.shields.io/github/last-commit/AiverAiva/Endfield-Permit-Export/main?style=flat-square" />
  </p>
</div>

## 本工具基本上只改了功能性的部分 很多文本跟功能性部分還沒完整和終末地相容
## 歡迎提出pull request更新內容或修改問題


这个项目由[star-rail-warp-export](https://github.com/biuuu/star-rail-warp-export/)修改而来，用于明日方舟：終末地。

一个使用 Electron 制作的小工具，需要在 Windows 64位操作系统上运行。

通过读取游戏日志或者代理模式获取访问游戏抽卡记录 API 所需的 authKey，然后再使用获取到的 authKey 来读取游戏抽卡记录。

## 其它语言

修改`src/i18n/`目录下的 json 文件就可以翻译到对应的语言。如果觉得已有的翻译有不准确或可以改进的地方，可以随时修改发 Pull Request。

## 使用说明

1. 下载工具后解压 - 下载地址: [Github](https://github.com/AiverAiva/Endfield-Permit-Export/releases/latest)
2. 打开游戏的抽卡详情页面

   ![详情页面](/docs/wish-history.png)

3. 点击工具的“加载数据”按钮

   ![加载数据](/docs/load-data.png)

   如果没出什么问题的话，你会看到正在读取数据的提示，最终效果如下图所示

   <details>
    <summary>展开图片</summary>

   ![预览](/docs/preview.png)

   </details>

如果需要导出多个账号的数据，可以点击旁边的加号按钮。

然后游戏切换的新账号，再打开抽卡历史记录，工具再点击“加载数据”按钮。

## Devlopment

```
# 安装模块
yarn install

# 开发模式
yarn dev

# 构建一个可以运行的程序
yarn build
```

## License

[MIT](https://github.com/AiverAiva/Endfield-Permit-Export/blob/main/LICENSE)

```

### File: src\main\update\index.js
```js
const { app } = require('electron')
const fetch = require('electron-fetch').default
const semver = require('semver')
const util = require('util')
const path = require('path')
const fs = require('fs-extra')
const extract = require('../module/extract-zip')
const { version } = require('../../../package.json')
const { hash, sendMsg } = require('../utils')
const config = require('../config')
const i18n = require('../i18n')
const streamPipeline = util.promisify(require('stream').pipeline)

async function download(url, filePath) {
  const response = await fetch(url)
  if (!response.ok) throw new Error(`unexpected response ${response.statusText}`)
  await streamPipeline(response.body, fs.createWriteStream(filePath))
}

const updateInfo = {
  status: 'init'
}

const isDev = !app.isPackaged
const appPath = isDev ? path.resolve(__dirname, '../../', 'update-dev/app') : app.getAppPath()
const updatePath = isDev ? path.resolve(__dirname, '../../', 'update-dev/download') : path.resolve(appPath, '..', '..', 'update')

const update = async () => {
  if (isDev) return
  try {
    const url = 'https://endfield-permit-export.weikuwu.me/update'
    const res = await fetch(`${url}/manifest.json?t=${Math.floor(Date.now() / (1000 * 60 * 10))}`)
    const data = await res.json()
    if (!data.active) return
    if (semver.gt(data.version, version) && semver.gte(version, data.from)) {
      await fs.emptyDir(updatePath)
      const filePath = path.join(updatePath, data.name)
      if (!config.autoUpdate) {
        sendMsg(data.version, 'NEW_VERSION')
        return
      }
      updateInfo.status = 'downloading'
      await download(`${url}/${data.name}`, filePath)
      const buffer = await fs.readFile(filePath)
      const sha256 = hash(buffer)
      if (sha256 !== data.hash) return
      const appPathTemp = path.join(updatePath, 'app')
      await extract(filePath, { dir: appPathTemp })
      updateInfo.status = 'moving'
      await fs.emptyDir(appPath)
      await fs.copy(appPathTemp, appPath)
      updateInfo.status = 'finished'
      sendMsg(i18n.log.autoUpdate.success, 'UPDATE_HINT')
    }
  } catch (e) {
    updateInfo.status = 'failed'
    sendMsg(e, 'ERROR')
  }
}

const getUpdateInfo = () => updateInfo

setTimeout(update, 1000)

exports.getUpdateInfo = getUpdateInfo
```

### File: src\renderer\router\index.js
```js
import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import Statistics from "../views/Statistics.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/statistics",
    name: "Statistics",
    component: Statistics,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;

```

### File: postcss.config.js
```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}

```

### File: tailwind.config.js
```js
module.exports = {
  content: ['./src/renderer/index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      minWidth: {
        '10': '60px'
      }
    },
  },
  variants: {
    extend: {
      backgroundColor: ['active']
    }
  },
  plugins: [],
}

```

### File: .electron-vite\build.js
```js
'use strict'
process.env.NODE_ENV = 'production'

const { say } = require('cfonts')
const { sync } = require('del')

const chalk = require('chalk')
const rollup = require("rollup")
const { build } = require('vite')
const Multispinner = require('multispinner')

const mainOptions = require('./rollup.main.config');
const rendererOptions = require('./vite.config')
const opt = mainOptions(process.env.NODE_ENV);

const doneLog = chalk.bgGreen.white(' DONE ') + ' '
const errorLog = chalk.bgRed.white(' ERROR ') + ' '
const okayLog = chalk.bgBlue.white(' OKAY ') + ' '
const isCI = process.env.CI || false

if (process.env.BUILD_TARGET === 'web') web()
else unionBuild()

function clean() {
    sync(['dist/electron/main/*', 'dist/electron/renderer/*', 'dist/web/*', 'build/*', '!build/icons', '!build/lib', '!build/lib/electron-build.*', '!build/icons/icon.*'])
    console.log(`\n${doneLog}clear done`)
    if (process.env.BUILD_TARGET === 'onlyClean') process.exit()
}

function unionBuild() {
    greeting()
    if (process.env.BUILD_TARGET === 'clean' || process.env.BUILD_TARGET === 'onlyClean') clean()

    const tasks = ['main', 'renderer']
    const m = new Multispinner(tasks, {
        preText: 'building',
        postText: 'process'
    })
    let results = ''

    m.on('success', () => {
        process.stdout.write('\x1B[2J\x1B[0f')
        console.log(`\n\n${results}`)
        console.log(`${okayLog}take it away ${chalk.yellow('`electron-builder`')}\n`)
        process.exit()
    })

    rollup.rollup(opt)
        .then(build => {
            results += `${doneLog}MainProcess build success` + '\n\n'
            build.write(opt.output).then(() => {
                m.success('main')
            })
        })
        .catch(error => {
            m.error('main')
            console.log(`\n  ${errorLog}failed to build main process`)
            console.error(`\n${error}\n`)
            process.exit(1)
        });

    build(rendererOptions).then(res => {
        results += `${doneLog}RendererProcess build success` + '\n\n'
        m.success('renderer')
    }).catch(err => {
        m.error('renderer')
        console.log(`\n  ${errorLog}failed to build renderer process`)
        console.error(`\n${err}\n`)
        process.exit(1)
    })
}

function web() {
    sync(['dist/web/*', '!.gitkeep'])
    build(rendererOptions).then(res => {
        console.log(`${doneLog}RendererProcess build success`)
        process.exit()
    })
}

function greeting() {
    const cols = process.stdout.columns
    let text = ''

    if (cols > 85) text = `let's-build`
    else if (cols > 60) text = `let's-|build`
    else text = false

    if (text && !isCI) {
        say(text, {
            colors: ['yellow'],
            font: 'simple3d',
            space: false
        })
    } else console.log(chalk.yellow.bold(`\n  let's-build`))
    console.log()
}
```

### File: .electron-vite\dev-runner.js
```js
process.env.NODE_ENV = 'development'

const chalk = require('chalk')
const electron = require('electron')
const path = require('path')
const rollup = require("rollup")
const Portfinder = require("portfinder")

const { say } = require('cfonts')
const { spawn } = require('child_process')
const { createServer } = require('vite')

const rendererOptions = require("./vite.config")
const mainOptions = require("./rollup.main.config")
const opt = mainOptions(process.env.NODE_ENV);

let electronProcess = null
let manualRestart = false

function logStats(proc, data) {
    let log = ''

    log += chalk.yellow.bold(`┏ ${proc} 'Process' ${new Array((19 - proc.length) + 1).join('-')}`)
    log += '\n\n'

    if (typeof data === 'object') {
        data.toString({
            colors: true,
            chunks: false
        }).split(/\r?\n/).forEach(line => {
            log += '  ' + line + '\n'
        })
    } else {
        log += `  ${data}\n`
    }

    log += '\n' + chalk.yellow.bold(`┗ ${new Array(28 + 1).join('-')}`) + '\n'
    console.log(log)
}

function removeJunk(chunk) {
    // Example: 2018-08-10 22:48:42.866 Electron[90311:4883863] *** WARNING: Textured window <AtomNSWindow: 0x7fb75f68a770>
    if (/\d+-\d+-\d+ \d+:\d+:\d+\.\d+ Electron(?: Helper)?\[\d+:\d+] /.test(chunk)) {
        return false;
    }

    // Example: [90789:0810/225804.894349:ERROR:CONSOLE(105)] "Uncaught (in promise) Error: Could not instantiate: ProductRegistryImpl.Registry", source: chrome-devtools://devtools/bundled/inspector.js (105)
    if (/\[\d+:\d+\/|\d+\.\d+:ERROR:CONSOLE\(\d+\)\]/.test(chunk)) {
        return false;
    }

    // Example: ALSA lib confmisc.c:767:(parse_card) cannot find card '0'
    if (/ALSA lib [a-z]+\.c:\d+:\([a-z_]+\)/.test(chunk)) {
        return false;
    }


    return chunk;
}

function startRenderer() {
    return new Promise((resolve, reject) => {
        Portfinder.basePort = 9080
        Portfinder.getPort(async (err, port) => {
            if (err) {
                console.log('PortError:', err)
                process.exit(1)
            } else {
                const server = await createServer(rendererOptions)
                process.env.PORT = port
                await server.listen(port)
                if (process.env.TARGET === 'web') {
                    server.config.logger.info(
                        chalk.cyan(`\n  vite v${require('vite/package.json').version}`) +
                        chalk.green(` dev server running at:\n`),
                        {
                            clear: !server.config.logger.hasWarned,
                        }
                    )
                    server.printUrls()
                }

                resolve()
            }
        })
    })
}

function startMain() {
    return new Promise((resolve, reject) => {
        const watcher = rollup.watch(opt);
        watcher.on('change', filename => {
            // 主进程日志部分
            logStats('Main-FileChange', filename)
        });
        watcher.on('event', event => {
            if (event.code === 'END') {
                if (electronProcess && electronProcess.kill) {
                    manualRestart = true
                    process.kill(electronProcess.pid)
                    electronProcess = null
                    startElectron()

                    setTimeout(() => {
                        manualRestart = false
                    }, 5000)
                }

                resolve()

            } else if (event.code === 'ERROR') {
                reject(event.error)
            }
        })
    })
}

function startElectron() {

    var args = [
        '--inspect=5858',
        path.join(__dirname, '../dist/electron/main/main.js')
    ]

    // detect yarn or npm and process commandline args accordingly
    if (process.env.npm_execpath.endsWith('yarn.js')) {
        args = args.concat(process.argv.slice(3))
    } else if (process.env.npm_execpath.endsWith('npm-cli.js')) {
        args = args.concat(process.argv.slice(2))
    }

    electronProcess = spawn(electron, args)

    electronProcess.stdout.on('data', data => {
        electronLog(removeJunk(data), 'blue')
    })
    electronProcess.stderr.on('data', data => {
        electronLog(removeJunk(data), 'red')
    })

    electronProcess.on('close', () => {
        if (!manualRestart) process.exit()
    })
}

function electronLog(data, color) {
    if (data) {
        let log = ''
        data = data.toString().split(/\r?\n/)
        data.forEach(line => {
            log += `  ${line}\n`
        })
        console.log(
            chalk[color].bold(`┏ Electron -------------------`) +
            '\n\n' +
            log +
            chalk[color].bold('┗ ----------------------------') +
            '\n'
        )
    }

}

function greeting() {
    const cols = process.stdout.columns
    let text = ''

    if (cols > 104) text = 'electron-vite'
    else if (cols > 76) text = 'electron-|vite'
    else text = false

    if (text) {
        say(text, {
            colors: ['yellow'],
            font: 'simple3d',
            space: false
        })
    } else console.log(chalk.yellow.bold('\n  electron-vite'))
    console.log(chalk.blue(`getting ready...`) + '\n')
}

async function init() {
    greeting()

    try {
        await startRenderer()
        if (process.env.TARGET !== 'web') {
            await startMain()
            await startElectron()
        }
    } catch (error) {
        console.error(error)
        process.exit(1)
    }

}

init()
```

### File: .electron-vite\rollup.main.config.js
```js
const path = require('path')
const { nodeResolve } = require('@rollup/plugin-node-resolve')
const commonjs = require('@rollup/plugin-commonjs')
const esbuild = require('rollup-plugin-esbuild').default
const alias = require('@rollup/plugin-alias')
const json = require('@rollup/plugin-json')

module.exports = (env = 'production') => {
  return {
    input: path.join(__dirname, '../src/main/main.js'),
    output: {
      file: path.join(__dirname, '../dist/electron/main/main.js'),
      format: 'cjs',
      name: 'MainProcess',
      sourcemap: false,
      exports: 'auto'
    },
    plugins: [
      nodeResolve({ jsnext: true, preferBuiltins: true, browser: true }), // 消除碰到 node.js 模块时⚠警告
      commonjs(),
      json(),
      esbuild({
        // All options are optional
        include: /\.[jt]sx?$/, // default, inferred from `loaders` option
        exclude: /node_modules/, // default
        // watch: process.argv.includes('--watch'), // rollup 中有配置
        sourceMap: false, // default
        minify: process.env.NODE_ENV === 'production',
        target: 'esnext', // default, or 'es20XX', 'esnext'
        // Like @rollup/plugin-replace
        define: {
          __VERSION__: '"x.y.z"'
        },
        // Add extra loaders
        loaders: {
          // Add .json files support
          // require @rollup/plugin-commonjs
          '.json': 'json',
          // Enable JSX in .js files too
          '.js': 'jsx'
        },
      }),
      alias({
        entries: [
          { find: '@main', replacement: path.join(__dirname, '../src/main'), },
        ]
      })
    ],
    external: [
      'crypto',
      'assert',
      'fs',
      'util',
      'os',
      'events',
      'child_process',
      'http',
      'https',
      'path',
      'electron',
      'original-fs'
    ],
  }
}

```

### File: .electron-vite\update.js
```js
const fs = require('fs-extra')
const path = require('path')
const crypto = require('crypto')
const AdmZip = require('adm-zip')
const { version } = require('../package.json')

const hash = (data, type = 'sha256') => {
  const hmac = crypto.createHmac(type, 'hk4e')
  hmac.update(data)
  return hmac.digest('hex')
}

const createZip = (filePath, dest) => {
  const zip = new AdmZip()
  zip.addLocalFolder(filePath)
  zip.toBuffer()
  zip.writeZip(dest)
}

const start = async () => {
  copyAppZip()
  const appPath = './build/win-unpacked/resources/app'
  const name = 'app.zip'
  const outputPath = path.resolve('./build/update/update/')
  const zipPath = path.resolve(outputPath, name)
  await fs.ensureDir(outputPath)
  await fs.emptyDir(outputPath)
  await fs.outputFile('./build/update/CNAME', 'endfield-permit-export.weikuwu.me')
  createZip(appPath, zipPath)
  const buffer = await fs.readFile(zipPath)
  const sha256 = hash(buffer)
  const hashName = sha256.slice(7, 12)
  await fs.copy(zipPath, path.resolve(outputPath, `${hashName}.zip`))
  await fs.remove(zipPath)
  await fs.outputJSON(path.join(outputPath, 'manifest.json'), {
    active: true,
    version,
    from: '0.0.1',
    name: `${hashName}.zip`,
    hash: sha256
  })
}

const copyAppZip = () => {
  try {
    const dir = path.resolve('./build')
    const filePath = path.resolve(dir, `EndfieldPermitExport-${version}-win.zip`)
    fs.copySync(filePath, path.join(dir, 'app.zip'))
  } catch (e) { }
}

const copyHTML = () => {
  try {
    const output = path.resolve('./build/update/')
    const dir = path.resolve('./src/web/')
    fs.copySync(dir, output)
  } catch (e) {
    console.error(e)
  }
}

start()
```

### File: .electron-vite\vite.config.js
```js
const { join } = require("path")
const vuePlugin = require("@vitejs/plugin-vue")
const { defineConfig } = require("vite")

function resolve(dir) {
    return join(__dirname, '..', dir)
}

const root = resolve('src/renderer')

const config = defineConfig({
    mode: process.env.NODE_ENV,
    root,
    resolve: {
        alias: {
            '@renderer': root,
        }
    },
    base: './',
    build: {
        outDir: process.env.BUILD_TARGET === 'web' ? resolve('dist/web') : resolve('dist/electron/renderer'),
        emptyOutDir: true
    },
    server: {
        port: Number(process.env.PORT),
    },
    plugins: [
        vuePlugin({
            script: {
                refSugar: true
            }
        })
    ],
    publicDir: resolve('static')
})

module.exports = config
```

### File: docs\README_EN.md
```md

[中文](https://github.com/biuuu/star-rail-warp-export/blob/main/README.md) | English

<div align="center">
  <h1>Endfield Permit Export</h1>

  <p>
    A pull history analyzing tool for《Arknights：Endfield》
  </p>

  <p>
    <a href="https://github.com/AiverAiva/Endfield-Permit-Export/releases">
      <img src="https://img.shields.io/github/v/release/AiverAiva/Endfield-Permit-Export?style=flat-square" />
    </a>
    <img src="https://img.shields.io/github/license/AiverAiva/Endfield-Permit-Export?style=flat-square" />
    <a href="https://github.com/AiverAiva/Endfield-Permit-Export/releases">
      <img src="https://img.shields.io/github/downloads/AiverAiva/Endfield-Permit-Export/total?style=flat-square" />
    </a>
    <img src="https://img.shields.io/github/last-commit/AiverAiva/Endfield-Permit-Export/main?style=flat-square" />
  </p>
</div>

This project is modified from the [genshin-wish-export](https://github.com/biuuu/genshin-wish-export/) repository, and its functions are basically the same.

A tool made from Electron that runs on the Windows 64 bit operating system.

Read the game log or proxy to get the authKey needed to access the game warp history API, and then use the authKey to read the game wish history.

## Other languages

Modify the JSON file in the `src/i18n/` directory to translate into the appropriate language.

If you feel that the existing translation is inappropriate, you can send a pull request to modify it at any time.

## Usage

1. Unzip after downloading the tool - [Download](https://github.com/biuuu/star-rail-warp-export/releases/latest/download/StarRailWarpExport.zip)
2. Open the warp details page of the game

    ![warp details](/docs/wish-history-en.png)

3. Click the tool's "Load data" button

    ![load data](/docs/load-data-en.png)

    If nothing goes wrong, you'll be prompted to read the data, and the final result will look like this

    <details>
    <summary>Expand the picture</summary>

    ![preview](/docs/preview-en.png)
    </details>

If you need to export the data of multiple accounts, you can click the plus button next to it.

Then switch to the new account of the game, open the wish history, and click the "load data" button in the tool.

## Devlopment

```
# install node modules
yarn install

# develop
yarn dev

# Build a program that can run
yarn build
```

## License

[MIT](https://github.com/biuuu/star-rail-warp-export/blob/main/LICENSE)


```

### File: scripts\download_icons.js
```js
const fs = require("fs-extra");
const path = require("path");

const CHAR_LIST_URL =
  "https://endfieldtools.dev/localdb/optimized/characters/characters-list.json";
const WPN_LIST_URL =
  "https://endfieldtools.dev/localdb/optimized/weapons/weapons-list.json";

const CHAR_ICON_BASE =
  "https://endfieldtools.dev/assets/images/endfield/charicon/icon_";
const WPN_ICON_BASE =
  "https://endfieldtools.dev/assets/images/endfield/itemicon/";

const CHAR_DEST = path.join(__dirname, "../src/renderer/assets/characters");
const WPN_DEST = path.join(__dirname, "../src/renderer/assets/weapons");

async function downloadFile(url, dest) {
  if (await fs.pathExists(dest)) {
    // console.log(`Skipped: ${path.basename(dest)}`);
    return;
  }
  try {
    const response = await fetch(url);
    if (!response.ok) {
      console.warn(`Failed to download ${url}: ${response.statusText}`);
      return;
    }
    const arrayBuffer = await response.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    await fs.writeFile(dest, buffer);
    console.log(`Downloaded: ${path.basename(dest)}`);
  } catch (err) {
    console.error(`Error downloading ${url}:`, err.message);
  }
}

async function start() {
  await fs.ensureDir(CHAR_DEST);
  await fs.ensureDir(WPN_DEST);

  console.log("Fetching character list...");
  try {
    const charRes = await fetch(CHAR_LIST_URL);
    const charData = await charRes.json();
    const charIds = Object.keys(charData);
    console.log(`Found ${charIds.length} characters. Starting download...`);

    for (const id of charIds) {
      const url = `${CHAR_ICON_BASE}${id}.png`;
      const dest = path.join(CHAR_DEST, `${id}.png`);
      await downloadFile(url, dest);
    }
  } catch (err) {
    console.error("Error fetching character list:", err.message);
  }

  console.log("\nFetching weapon list...");
  try {
    const wpnRes = await fetch(WPN_LIST_URL);
    const wpnData = await wpnRes.json();
    const wpnIds = Object.keys(wpnData);
    console.log(`Found ${wpnIds.length} weapons. Starting download...`);

    for (const id of wpnIds) {
      const url = `${WPN_ICON_BASE}${id}.png`;
      const dest = path.join(WPN_DEST, `${id}.png`);
      await downloadFile(url, dest);
    }
  } catch (err) {
    console.error("Error fetching weapon list:", err.message);
  }

  console.log("\nDone!");
}

start();

```

### File: scripts\update_i18n.js
```js
const fs = require('fs-extra');
const path = require('path');

const CHAR_LIST_URL = 'https://endfieldtools.dev/localdb/optimized/characters/characters-list.json';
const WPN_LIST_URL = 'https://endfieldtools.dev/localdb/optimized/weapons/weapons-list.json';
const I18N_BASE_URL = 'https://endfieldtools.dev/localdb/optimized/i18n/core/I18nTextTable_';

const LANG_MAP = {
  'CN': '简体中文.json',
  'TC': '繁體中文.json',
  'EN': 'English.json',
  'JP': '日本語.json',
  'KR': '한국어.json',
  'DE': 'Deutsch.json',
  'FR': 'Français.json',
  'MX': 'Español.json',
  'PT': 'Português.json',
  'RU': 'Pусский.json',
  'TH': 'ภาษาไทย.json',
  'VI': 'Tiếng Việt.json',
  'ID': 'Indonesia.json'
};

const I18N_DIR = path.join(__dirname, '../src/i18n');

async function start() {
  console.log('Fetching character and weapon lists...');
  const charRes = await fetch(CHAR_LIST_URL);
  const charData = await charRes.json();
  const wpnRes = await fetch(WPN_LIST_URL);
  const wpnData = await wpnRes.json();

  const characters = Object.values(charData);
  const weapons = Object.values(wpnData);

  for (const [code, fileName] of Object.entries(LANG_MAP)) {
    console.log(`\nProcessing language: ${code} (${fileName})...`);
    try {
      const i18nRes = await fetch(`${I18N_BASE_URL}${code}.json`);
      if (!i18nRes.ok) {
        console.warn(`Failed to fetch translations for ${code}: ${i18nRes.statusText}`);
        continue;
      }
      const i18nTable = await i18nRes.json();

      const localFilePath = path.join(I18N_DIR, fileName);
      if (!(await fs.pathExists(localFilePath))) {
        console.warn(`Local file ${fileName} does not exist, skipping.`);
        continue;
      }

      const localI18n = await fs.readJson(localFilePath);

      // Update characters
      for (const char of characters) {
        const translation = i18nTable[char.nameI18nId];
        if (translation) {
          localI18n[`char.${char.charId}`] = translation;
        }
      }

      // Update weapons
      for (const wpn of weapons) {
        const translation = i18nTable[wpn.nameI18nId];
        if (translation) {
          localI18n[`wpn.${wpn.weaponId}`] = translation;
        }
      }

      await fs.writeJson(localFilePath, localI18n, { spaces: 2 });
      console.log(`Updated ${fileName} successfully.`);
    } catch (err) {
      console.error(`Error processing ${code}:`, err.message);
    }
  }

  console.log('\nAll i18n files updated!');
}

start();

```

### File: src\idJson.json
```json
{
  "zh-cn": {
    "20000": {
      "name": "锋镝",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20001": {
      "name": "物穰",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20002": {
      "name": "天倾",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20003": {
      "name": "琥珀",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20004": {
      "name": "幽邃",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20005": {
      "name": "齐颂",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20006": {
      "name": "智库",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20007": {
      "name": "离弦",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20008": {
      "name": "嘉果",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20009": {
      "name": "乐圮",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20010": {
      "name": "戍御",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20011": {
      "name": "渊环",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20012": {
      "name": "轮契",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20013": {
      "name": "灵钥",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20014": {
      "name": "相抗",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20015": {
      "name": "蕃息",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20016": {
      "name": "俱殁",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20017": {
      "name": "开疆",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20018": {
      "name": "匿影",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20019": {
      "name": "调和",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20020": {
      "name": "睿见",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20021": {
      "name": "焚影",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "20022": {
      "name": "溯忆",
      "item_type": "光锥",
      "rank_type": "3"
    },
    "21000": {
      "name": "一场术后对话",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21001": {
      "name": "晚安与睡颜",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21002": {
      "name": "余生的第一天",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21003": {
      "name": "唯有沉默",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21004": {
      "name": "记忆中的模样",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21005": {
      "name": "鼹鼠党欢迎你",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21006": {
      "name": "「我」的诞生",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21007": {
      "name": "同一种心情",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21008": {
      "name": "猎物的视线",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21009": {
      "name": "朗道的选择",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21010": {
      "name": "论剑",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21011": {
      "name": "与行星相会",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21012": {
      "name": "秘密誓心",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21013": {
      "name": "别让世界静下来",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21014": {
      "name": "此时恰好",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21015": {
      "name": "决心如汗珠般闪耀",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21016": {
      "name": "宇宙市场趋势",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21017": {
      "name": "点个关注吧！",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21018": {
      "name": "舞！舞！舞！",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21019": {
      "name": "在蓝天下",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21020": {
      "name": "天才们的休憩",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21021": {
      "name": "等价交换",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21022": {
      "name": "延长记号",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21023": {
      "name": "我们是地火",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21024": {
      "name": "春水初生",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21025": {
      "name": "过往未来",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21026": {
      "name": "汪！散步时间！",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21027": {
      "name": "早餐的仪式感",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21028": {
      "name": "暖夜不会漫长",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21029": {
      "name": "后会有期",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21030": {
      "name": "这就是我啦！",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21031": {
      "name": "重返幽冥",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21032": {
      "name": "镂月裁云之意",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21033": {
      "name": "无处可逃",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21034": {
      "name": "今日亦是和平的一日",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21035": {
      "name": "何物为真",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21036": {
      "name": "美梦小镇大冒险",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21037": {
      "name": "最后的赢家",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21038": {
      "name": "在火的远处",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21039": {
      "name": "织造命运之线",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21040": {
      "name": "银河沦陷日",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21041": {
      "name": "好戏开演",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21042": {
      "name": "铭记于心的约定",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21043": {
      "name": "两个人的演唱会",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21044": {
      "name": "无边曼舞",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21045": {
      "name": "谐乐静默之后",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21046": {
      "name": "芳华待灼",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21047": {
      "name": "黑夜如影随行",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21048": {
      "name": "梦的蒙太奇",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21050": {
      "name": "胜利只在朝夕间",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21051": {
      "name": "天才们的问候",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21052": {
      "name": "多流汗，少流泪",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21053": {
      "name": "愿旅途永远坦然",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21054": {
      "name": "故事的下一页",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21055": {
      "name": "直到明天的明天",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21056": {
      "name": "追逐风的时候",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21057": {
      "name": "花儿不会忘记",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21058": {
      "name": "一行往日的血",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21060": {
      "name": "氤氲麦香的梦",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21061": {
      "name": "假日浴场大冒险",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "21062": {
      "name": "于那终点再见",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "22000": {
      "name": "新手任务开始前",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "22001": {
      "name": "嘿，我在这儿",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "22002": {
      "name": "为了明日的旅途",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "22003": {
      "name": "忍事录•音律狩猎",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "22004": {
      "name": "宇宙大生意",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "22005": {
      "name": "永远的迷境饭",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "22006": {
      "name": "飞向粉色的明天",
      "item_type": "光锥",
      "rank_type": "4"
    },
    "23000": {
      "name": "银河铁道之夜",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23001": {
      "name": "于夜色中",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23002": {
      "name": "无可取代的东西",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23003": {
      "name": "但战斗还未结束",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23004": {
      "name": "以世界之名",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23005": {
      "name": "制胜的瞬间",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23006": {
      "name": "只需等待",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23007": {
      "name": "雨一直下",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23008": {
      "name": "棺的回响",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23009": {
      "name": "到不了的彼岸",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23010": {
      "name": "拂晓之前",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23011": {
      "name": "她已闭上双眼",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23012": {
      "name": "如泥酣眠",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23013": {
      "name": "时节不居",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23014": {
      "name": "此身为剑",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23015": {
      "name": "比阳光更明亮的",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23016": {
      "name": "烦恼着，幸福着",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23017": {
      "name": "惊魂夜",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23018": {
      "name": "片刻，留在眼底",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23019": {
      "name": "镜中故我",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23020": {
      "name": "纯粹思维的洗礼",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23021": {
      "name": "游戏尘寰",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23022": {
      "name": "重塑时光之忆",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23023": {
      "name": "命运从未公平",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23024": {
      "name": "行于流逝的岸",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23025": {
      "name": "梦应归于何处",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23026": {
      "name": "夜色流光溢彩",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23027": {
      "name": "驶向第二次生命",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23028": {
      "name": "偏偏希望无价",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23029": {
      "name": "那无数个春天",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23030": {
      "name": "落日时起舞",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23031": {
      "name": "我将，巡征追猎",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23032": {
      "name": "唯有香如故",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23033": {
      "name": "忍法帖•缭乱破魔",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23034": {
      "name": "回到大地的飞行",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23035": {
      "name": "长路终有归途",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23036": {
      "name": "将光阴织成黄金",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23037": {
      "name": "向着不可追问处",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23038": {
      "name": "如果时间是一朵花",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23039": {
      "name": "血火啊，燃烧前路",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23040": {
      "name": "让告别，更美一些",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23041": {
      "name": "生命当付之一炬",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23042": {
      "name": "愿虹光永驻天空",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23043": {
      "name": "谎言在风中飘扬",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23044": {
      "name": "黎明恰如此燃烧",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23045": {
      "name": "没有回报的加冕",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23046": {
      "name": "理想燃烧的地狱",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23047": {
      "name": "海洋为何而歌",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23048": {
      "name": "金血铭刻的时代",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23049": {
      "name": "致长夜的星光",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23050": {
      "name": "勿忘她的火焰",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23051": {
      "name": "纵然山河万程",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "23052": {
      "name": "爱如此刻永恒",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "24000": {
      "name": "记一位星神的陨落",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "24001": {
      "name": "星海巡航",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "24002": {
      "name": "记忆的质料",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "24003": {
      "name": "孤独的疗愈",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "24004": {
      "name": "不息的演算",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "24005": {
      "name": "记忆永不落幕",
      "item_type": "光锥",
      "rank_type": "5"
    },
    "1001": {
      "name": "三月七",
      "item_type": "角色",
      "rank_type": "4"
    },
    "1002": {
      "name": "丹恒",
      "item_type": "角色",
      "rank_type": "4"
    },
    "1003": {
      "name": "姬子",
      "item_type": "角色",
      "rank_type": "5"
    },
    "1004": {
      "name": "瓦尔特",
      "item_type": "角色",
      "rank_type": "5"
    },
    "1005": {
      "name": "卡芙卡",
      "item_type": "角色",
      "rank_type": "5"
    },
    "1006": {
      "name": "银狼",
      "item_type": "角色",
      "rank_type": "5"
    },
    "1008": {
      "name": "阿兰",
      "item_type": "角色",
      "rank_type": "4"
    },
    "1009": {
      "name": "艾丝妲",
      "item_type": "角色",
      "rank_type": "4"
    },
    "1013": {
      "name": "黑塔",
      "item_type": "角色",
      "rank_type": "4"
    },
    "1014": {
      "name": "Saber",
      "item_type": "角色",
      "rank_type": "5"
    },
    "1015": {
      "name": "Archer",
      "item_type": "角色",
      "rank_type": "5"
    },
    "1101": {
  
... [TRUNCATED]
```

### File: tools\getIdMap.py
```py
import requests
import json
from opencc import OpenCC

# 初始化 OpenCC 转换器
cc = OpenCC("s2t")

# 语言映射配置
language_map = {
    "zh-cn": "cn",
    "zh-tw": "cn",  # 简体转繁体
    "en-us": "en",
    "ja-jp": "jp",
    "ko-kr": "kr",
}

# 类型映射配置
type_map = {
    "weapon": {
        "zh-cn": "光锥",
        "zh-tw": "光錐",
        "en-us": "Light Cone",
        "ja-jp": "光円錐",
        "ko-kr": "무기",
    },
    "character": {
        "zh-cn": "角色",
        "zh-tw": "角色",
        "en-us": "Character",
        "ja-jp": "キャラ",
        "ko-kr": "캐릭터",
    },
}


def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def transform_data(data, item_type):
    transformed = {lang: {} for lang in language_map.keys()}
    for id, item in data.items():
        for lang, key in language_map.items():
            name = item[key] if lang != "zh-tw" else cc.convert(item["cn"])
            transformed[lang][id] = {
                "name": name,
                "item_type": type_map[item_type][lang],
                "rank_type": item["rank"][-1],
            }
    return transformed


def main():
    try:
        version_url = "https://api.hakush.in/hsr/new.json"
        version_data = fetch_json(version_url)

        latest_version = ".".join(version_data["version"].split(".")[:2])
        print(f"Latest version: {latest_version}")
        
        weapon_url = f"https://api.hakush.in/hsr/{latest_version}/lightcone.json"
        character_url = f"https://api.hakush.in/hsr/{latest_version}/character.json"
        weapon_data = fetch_json(weapon_url)
        print("Fetched", len(weapon_data), "lightcones")
        character_data = fetch_json(character_url)
        print("Fetched", len(character_data), "characters")

        transformed_data = {lang: {} for lang in language_map.keys()}

        transformed_data["version"] = latest_version

        weapon_transformed = transform_data(weapon_data, "weapon")
        character_transformed = transform_data(character_data, "character")

        for lang in language_map.keys():
            transformed_data[lang].update(weapon_transformed[lang])
            transformed_data[lang].update(character_transformed[lang])

        with open("./src/idJson.json", "w", encoding="utf-8") as f:
            json.dump(transformed_data, f, ensure_ascii=False, indent=2)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    main()

```

### File: src\i18n\Deutsch.json
```json
{
  "symbol.colon": ": ",
  "ui.button.load": "Lade Daten",
  "ui.button.update": "Aktualisieren",
  "ui.button.excel": "In Excel exportieren",
  "ui.button.srgf": "In JSON exportieren",
  "ui.button.url": "Eingabe URL",
  "ui.button.setting": "Einstellungen",
  "ui.button.option": "Optionen",
  "ui.button.startProxy": "Proxy modus",
  "ui.select.newAccount": "Neuer Nutzer",
  "ui.hint.newAccount": "Daten von anderen Nutzern exportieren",
  "ui.hint.init": "Bitte öffne deinen Wunschlverlauf im Spiel bevor du versuchst deine Wunschdaten zu laden",
  "ui.hint.lastUpdate": "Letzte Aktualisierung",
  "ui.hint.failed": "Oops, irgendetwas ist schief gelaufen",
  "ui.win.title": "",
  "ui.data.total": "Total",
  "ui.data.times": "Wünsche",
  "ui.data.sum": "Angehäuft",
  "ui.data.no5star": "Wünsche ohne 6 Sterne",
  "ui.data.character": "Operator",
  "ui.data.weapon": "",
  "ui.data.star5": "6 Sterne",
  "ui.data.star4": "5 Sterne",
  "ui.data.star3": "4 Sterne",
  "ui.data.history": "6 Sterne verlauf",
  "ui.data.average": "Durschnittlicher 6 Sterne",
  "ui.data.chara5": "6 Sterne Operator",
  "ui.data.chara4": "5 Sterne Operator",
  "ui.data.weapon5": "",
  "ui.data.weapon4": "",
  "ui.data.weapon3": "",
  "ui.setting.title": "Einstellungen",
  "ui.setting.language": "Sprache",
  "ui.setting.languageHint": "Wenn eine Übersetzung fehlt, wird Englisch als Standardsparche ausgewählt.",
  "ui.setting.logType": "Aufzeichnungstyp",
  "ui.setting.auto": "Automatisch",
  "ui.setting.cnServer": "CN Server",
  "ui.setting.seaServer": "Globaler Server",
  "ui.setting.logTypeHint": "Wähle aus, welche von dem Server generierten Aufzeichnungen benutzt werden sollen, wenn zum ersten mal die URL von den Spielaufzeichnungen erworben wird",
  "ui.setting.autoUpdate": "Automatische Aktualisierung",
  "ui.setting.proxyMode": "Proxy modus",
  "ui.setting.proxyModeHint": "Wenn das Erwerben der URL von den Systemaufzeichnungen scheitert, nutz den Systemproxy",
  "ui.setting.closeProxy": "Deaktiviere den Systemproxy",
  "ui.setting.closeProxyHint": "Wenn der Proxymodus aktiviert ist und das Programm abstürzt kann es zu unerwünschten Folgen für dein System führen. Du kannst diesen Knopf drücken, um die Systemproxy Einstellungen zurückzusetzen.",
  "ui.about.title": "Über uns",
  "ui.about.license": "Diese Software ist Open-Source und nutzt die MIT Lizenz.",
  "ui.urlDialog.title": "Gebe die URL manuell ein",
  "ui.urlDialog.hint": "Diese Funktion sollte nur benutzt werden, falls Sie wissen, welche URL hier benötigt wird",
  "ui.urlDialog.placeholder": "Bitte gebe die URL mit den Authentifizierungsinformationen ein",
  "ui.common.cancel": "Abbrechen",
  "ui.common.ok": "Weiter",
  "log.save.failed": "Lokale Daten konnten nicht gespeichert werden",
  "log.file.notFound": "Die Wunschaufzeichnungen konnten nicht gefunden werden, stelle sicher, dass du im Spiel deinen Wunschverlauf schon geöffnet hast",
  "log.url.notFound": "Konnte die URL nicht finden",
  "log.file.readFailed": "Konnte die Aufzeichnungen nicht lesen",
  "log.fetch.retry": "Das Verarbeiten von ${name} auf Seite ${page} ist gescheitert，versuche in 5 Sekunden erneut, zum ${count}. mal…",
  "log.fetch.retryFailed": "Das Verarbeiten von ${name} auf Seite ${page} ist gescheitert, maximale Versuche wurden erreicht",
  "log.fetch.interval": "Verarbeite ${name} auf Seite ${page}，1 Sekunde Timeout für 10 Seiten…",
  "log.fetch.current": "Verarbeite ${name} auf Seite ${page}",
  "log.fetch.authTimeout": "Die Nutzer Authentifizierung ist abgelaufen, bitte öffne im Spiel die Wunschaufzeichnungen erneut.",
  "log.fetch.gachaType": "Wunschtyp wird erworben, bitte warten",
  "log.fetch.gachaTypeOk": "Wunschtyp erworben",
  "log.url.lackAuth": "Der Authentifizierungsschlüssel konnte in der URL nicht aufgefunden werden",
  "log.proxy.hint": "Nutze den Proxymodus [${ip}:${port}] um die URL zu erwerben, bitte öffne im Spiel die Wunschaufzeichnungen erneut.",
  "log.url.notFound2": "URL konnte nicht gefunden werden, bitte stelle sicher, dass du deinen Wunschverlauf schon einmal im Spiel geöffnet hast",
  "log.url.incorrect": "URL Parameter konnten nicht erworben werden",
  "log.autoUpdate.success": "Die automatische aktualisierung war erfolgreich, bitte starten sie das Programm neu",
  "excel.header.time": "zeit",
  "excel.header.name": "name",
  "excel.header.type": "typ",
  "excel.header.rank": "seltenheit",
  "excel.header.total": "ingesammt",
  "excel.header.pity": "innerhalb von pity",
  "excel.header.remark": "bemerkung",
  "excel.wish2": "Wunsch 2",
  "excel.customFont": "Arial",
  "ui.button.login": "Login",
  "ui.loginDialog.title": "Account Login",
  "ui.loginDialog.server": "Server auswählen",
  "ui.loginDialog.roles": "Rolle auswählen",
  "ui.loginDialog.hint": "Bitte zuerst im Popup-Fenster einloggen",
  "excel.filePrefix": "",
  "excel.fileType": "Excel Datei",
  "srgf.fileType": "Endfield Gacha Log Format Datei",
  "gacha.type.1": "Rekrutierung: Standard",
  "gacha.type.11": "Rekrutierung: Priorisiert",
  "gacha.type.2": "Rekrutierung: Neue Horizonte",
  "gacha.type.300": "Dringende Rekrutierung",
  "char.chr_0020_meurs": "Catcher",
  "char.chr_0009_azrila": "Ember",
  "char.chr_0004_pelica": "Perlica",
  "char.chr_0005_chen": "Chen Qianyu",
  "char.chr_0006_wolfgd": "Wulfgard",
  "char.chr_0007_ikut": "Arclight",
  "char.chr_0011_seraph": "Xaihi",
  "char.chr_0014_aurora": "Snowshine",
  "char.chr_0012_avywen": "Avywenna",
  "char.chr_0017_yvonne": "Yvonne",
  "char.chr_0023_antal": "Antal",
  "char.chr_0013_aglina": "Gilberta",
  "char.chr_0015_lifeng": "Lifeng",
  "char.chr_0024_deepfin": "Alesh",
  "char.chr_0016_laevat": "Laevatain",
  "char.chr_0018_dapan": "Da Pan",
  "char.chr_0019_karin": "Akekuri",
  "char.chr_0021_whiten": "Estella",
  "char.chr_0026_lastrite": "Last Rite",
  "char.chr_0022_bounda": "Fluorite",
  "char.chr_0025_ardelia": "Ardelia",
  "char.chr_0027_tangtang": "Tangtang",
  "char.chr_0029_pograni": "Pogranichnik",
  "wpn.wpn_claym_0003": "Industrie 0.1",
  "wpn.wpn_claym_0004": "Mustermodell",
  "wpn.wpn_pistol_0003": "Long Road",
  "wpn.wpn_claym_0006": "Former Finery",
  "wpn.wpn_claym_0007": "Donnerberg",
  "wpn.wpn_funnel_0006": "Opus: Ätzfigur",
  "wpn.wpn_funnel_0010": "Ritterliche Tugenden",
  "wpn.wpn_claym_0008": "Sundered Prince",
  "wpn.wpn_pistol_0001": "Peco 5",
  "wpn.wpn_claym_0009": "Quencher",
  "wpn.wpn_claym_0010": "Darhoff 7",
  "wpn.wpn_claym_0011": "Seeker of Dark Lung",
  "wpn.wpn_claym_0012": "Finishing Call",
  "wpn.wpn_claym_0013": "Khravengger",
  "wpn.wpn_claym_0014": "Ancient Canal",
  "wpn.wpn_pistol_0002": "Heulender Wächter",
  "wpn.wpn_claym_0015": "OBJ Schwere Last",
  "wpn.wpn_pistol_0008": "Keil",
  "wpn.wpn_pistol_0012": "OBJ Velocitous",
  "wpn.wpn_funnel_0001": "Vollautomatische Hypernova",
  "wpn.wpn_sword_0003": "Tarr 11",
  "wpn.wpn_funnel_0002": "Jiminy 12",
  "wpn.wpn_funnel_0003": "Fluorescent Roc",
  "wpn.wpn_funnel_0004": "Wilder Wanderer",
  "wpn.wpn_lance_0003": "Pathfinder's Beacon",
  "wpn.wpn_funnel_0005": "Strophe der Erinnerungen",
  "wpn.wpn_lance_0013": "OBJ Klingenhorn",
  "wpn.wpn_funnel_0007": "Monaihe",
  "wpn.wpn_funnel_0011": "Garantierte Lieferung",
  "wpn.wpn_funnel_0008": "Zünder",
  "wpn.wpn_funnel_0012": "Freedom to Proselytize",
  "wpn.wpn_funnel_0009": "Oblivion",
  "wpn.wpn_funnel_0013": "Träume vom Sternenstrand",
  "wpn.wpn_funnel_0014": "OBJ Techniken-Bestimmer",
  "wpn.wpn_lance_0004": "Chimärische Gerechtigkeit",
  "wpn.wpn_lance_0006": "Einheitliche Haftung",
  "wpn.wpn_lance_0008": "Aggeloslayer",
  "wpn.wpn_lance_0009": "Opero 77",
  "wpn.wpn_lance_0010": "Tapferkeit",
  "wpn.wpn_pistol_0006": "Opus: Die Lebenden",
  "wpn.wpn_pistol_0010": "Künstlerischer Tyrann",
  "wpn.wpn_sword_0018": "Twelve Questions",
  "wpn.wpn_lance_0011": "JET",
  "wpn.wpn_lance_0012": "Bergträger",
  "wpn.wpn_sword_0021": "Große Vision",
  "wpn.wpn_pistol_0004": "Rationaler Abschied",
  "wpn.wpn_pistol_0005": "Navigator",
  "wpn.wpn_sword_0008": "Erhabene Klinge",
  "wpn.wpn_pistol_0007": "Heimweh",
  "wpn.wpn_pistol_0011": "Banditenruf",
  "wpn.wpn_pistol_0009": "Klannibale",
  "wpn.wpn_sword_0012": "Thermite Cutter",
  "wpn.wpn_sword_0005": "Zerreißender Stahl",
  "wpn.wpn_sword_0006": "Tadel des Schmiedefeuers",
  "wpn.wpn_sword_0007": "Fortbauer",
  "wpn.wpn_sword_0009": "Flutwelle",
  "wpn.wpn_sword_0010": "Umbral Torch",
  "wpn.wpn_sword_0011": "Rapid Ascent",
  "wpn.wpn_sword_0013": "Untadeliger Ruf",
  "wpn.wpn_sword_0014": "White Night Nova",
  "wpn.wpn_sword_0015": "Aspirant",
  "wpn.wpn_sword_0016": "Never Rest",
  "wpn.wpn_sword_0017": "Glorreiche Erinnerung",
  "wpn.wpn_sword_0019": "OBJ Ende der Leichtigkeit",
  "wpn.wpn_sword_0020": "Flösslerjäger 3.0"
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
