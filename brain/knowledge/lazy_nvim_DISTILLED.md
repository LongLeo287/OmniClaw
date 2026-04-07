---
id: lazy.nvim
type: knowledge
owner: OA_Triage
---
# lazy.nvim
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h4 align="center">
  <a href="https://lazy.folke.io/installation">Install</a>
  ·
  <a href="https://lazy.folke.io/configuration">Configure</a>
  ·
  <a href="https://lazy.folke.io">Docs</a>
</h4>

<div align="center"><p>
    <a href="https://github.com/folke/lazy.nvim/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/folke/lazy.nvim?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41&include_prerelease&sort=semver" />
    </a>
    <a href="https://github.com/folke/lazy.nvim/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/folke/lazy.nvim?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
    <a href="https://github.com/folke/lazy.nvim/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/folke/lazy.nvim?style=for-the-badge&logo=starship&color=ee999f&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/folke/lazy.nvim/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/folke/lazy.nvim?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/folke/lazy.nvim/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/folke/lazy.nvim?style=for-the-badge&logo=bilibili&color=F5E0DC&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/folke/lazy.nvim">
      <img alt="Repo Size" src="https://img.shields.io/github/repo-size/folke/lazy.nvim?color=%23DDB6F2&label=SIZE&logo=codesandbox&style=for-the-badge&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://twitter.com/intent/follow?screen_name=folke">
      <img alt="follow on Twitter" src="https://img.shields.io/twitter/follow/folke?style=for-the-badge&logo=twitter&color=8aadf3&logoColor=D9E0EE&labelColor=302D41" />
    </a>
</div>



**lazy.nvim** is a modern plugin manager for Neovim.

![image](https://user-images.githubusercontent.com/292349/208301737-68fb279c-ba70-43ef-a369-8c3e8367d6b1.png)

## ✨ Features

- 📦 Manage all your Neovim plugins with a powerful UI
- 🚀 Fast startup times thanks to automatic caching and bytecode compilation of Lua modules
- 💾 Partial clones instead of shallow clones
- 🔌 Automatic lazy-loading of Lua modules and lazy-loading on events, commands, filetypes, and key mappings
- ⏳ Automatically install missing plugins before starting up Neovim, allowing you to start using it right away
- 💪 Async execution for improved performance
- 🛠️ No need to manually compile plugins
- 🧪 Correct sequencing of dependencies
- 📁 Configurable in multiple files
- 📚 Generates helptags of the headings in `README.md` files for plugins that don't have vimdocs
- 💻 Dev options and patterns for using local plugins
- 📊 Profiling tools to optimize performance
- 🔒 Lockfile `lazy-lock.json` to keep track of installed plugins
- 🔎 Automatically check for updates
- 📋 Commit, branch, tag, version, and full [Semver](https://devhints.io/semver) support
- 📈 Statusline component to see the number of pending updates
- 🎨 Automatically lazy-loads colorschemes

## ⚡️ Requirements

- Neovim >= **0.8.0** (needs to be built with **LuaJIT**)
- Git >= **2.19.0** (for partial clones support)
- a [Nerd Font](https://www.nerdfonts.com/) **_(optional)_**
- [luarocks](https://luarocks.org/) to install rockspecs.
  You can remove `rockspec` from `opts.pkg.sources` to disable this feature.

## 🚀 Getting Started

Check the [documentation website](https://lazy.folke.io/) for more information.
```

### File: .markdownlint-cli2.yaml
```yaml
config:
  MD013: false
  MD033: false

```

### File: .markdownlint.yaml
```yaml
MD013:
  line_length: 120
  tables: false
MD033:
  allowed_elements:
    - "details"
    - "summary"
    - "b"
    - "table"
    - "tr"
    - "td"
    - "a"

```

### File: .neoconf.json
```json
{
  "neodev": {
    "library": {
      "plugins": [
        "plenary.nvim"
      ]
    }
  },
  "lspconfig": {
    "lua_ls": {
      "Lua.runtime.version": "LuaJIT",
      "Lua.workspace.checkThirdParty": false
    }
  }
}

```

### File: CHANGELOG.md
```md
# Changelog

## [11.17.5](https://github.com/folke/lazy.nvim/compare/v11.17.4...v11.17.5) (2025-11-06)


### Bug Fixes

* **luarocks:** proper parsing of dependency name. Closes [#2086](https://github.com/folke/lazy.nvim/issues/2086) ([5c09e6f](https://github.com/folke/lazy.nvim/commit/5c09e6fe71f4bb930eeffe24d45762fa3ffada4e))

## [11.17.4](https://github.com/folke/lazy.nvim/compare/v11.17.3...v11.17.4) (2025-11-04)


### Bug Fixes

* **plugin:** proper error message when a plugin spec returns more than one value. ([dfdc85e](https://github.com/folke/lazy.nvim/commit/dfdc85e18930a3f1643e83c8ed0c514ca85e49fa))

## [11.17.3](https://github.com/folke/lazy.nvim/compare/v11.17.2...v11.17.3) (2025-10-28)


### Bug Fixes

* **luarocks:** update to lumen-oss for binaries. Closes [#2060](https://github.com/folke/lazy.nvim/issues/2060). Closes [#2059](https://github.com/folke/lazy.nvim/issues/2059) ([e31789c](https://github.com/folke/lazy.nvim/commit/e31789c675e2f591a20fc894b6713398eaa5dddd))

## [11.17.2](https://github.com/folke/lazy.nvim/compare/v11.17.1...v11.17.2) (2025-10-23)


### Bug Fixes

* **luarocks:** add plugin to lua path if it was already loaded before we know its a luarock ([147f5a3](https://github.com/folke/lazy.nvim/commit/147f5a3f55b5491bbc77a55ce846ef5eb575fa42))
* **plugin:** check that path is actually in root dir. Closes [#2075](https://github.com/folke/lazy.nvim/issues/2075) ([16e5271](https://github.com/folke/lazy.nvim/commit/16e52715b70b4d0fc6af3563ccc0ed9df82ae23e))
* **stats:** better support for different `time_t` sizes. See [#2049](https://github.com/folke/lazy.nvim/issues/2049) ([1ea3c40](https://github.com/folke/lazy.nvim/commit/1ea3c4085785f460fb0e46d2fe1ee895f5f9e7c1))

## [11.17.1](https://github.com/folke/lazy.nvim/compare/v11.17.0...v11.17.1) (2025-02-25)


### Bug Fixes

* **bootstrap:** support for older Neovim versions ([1c9ba37](https://github.com/folke/lazy.nvim/commit/1c9ba3704564a2e34a22191bb89678680ffeb245))
* **meta:** rebuild dirty right after disable. See [#1889](https://github.com/folke/lazy.nvim/issues/1889) ([d51cf69](https://github.com/folke/lazy.nvim/commit/d51cf6978321d659e68a8bc38ee806bd2517a196))

## [11.17.0](https://github.com/folke/lazy.nvim/compare/v11.16.2...v11.17.0) (2025-02-24)


### Features

* **config,render:** allow customizing the debug icon ([#1863](https://github.com/folke/lazy.nvim/issues/1863)) ([a9c660d](https://github.com/folke/lazy.nvim/commit/a9c660d6ef1b396869d3d951760aa7a3dbfe575f))
* **util:** pass lang to `vim.notify` so that snacks notifier can render the ft. Closes [#1919](https://github.com/folke/lazy.nvim/issues/1919) ([c6a57a3](https://github.com/folke/lazy.nvim/commit/c6a57a3534d3494bcc5ff9b0586e141bdb0280eb))


### Bug Fixes

* **config:** add missing space on the default debug icon ([#1879](https://github.com/folke/lazy.nvim/issues/1879)) ([4df5c4d](https://github.com/folke/lazy.nvim/commit/4df5c4d65a3bbf801edd9ec55fb1ae55cfa72dd0))
* **meta:** disable top-level specs before the rest. Closes [#1889](https://github.com/folke/lazy.nvim/issues/1889) ([f81a3fb](https://github.com/folke/lazy.nvim/commit/f81a3fb7feaf460ec7c8c983682b4a693b18fdd4))
* **ui:** do not show virt_lines for messages ([#1904](https://github.com/folke/lazy.nvim/issues/1904)) ([f15a939](https://github.com/folke/lazy.nvim/commit/f15a93907ddad3d9139aea465ae18336d87f5ce6))

## [11.16.2](https://github.com/folke/lazy.nvim/compare/v11.16.1...v11.16.2) (2024-12-13)


### Bug Fixes

* **meta:** when a plugin is both optional and disabled, then just delete it from the list ([805b85c](https://github.com/folke/lazy.nvim/commit/805b85c2ea3bd6f9506ef22cbd6e3a39172b5b08))

## [11.16.1](https://github.com/folke/lazy.nvim/compare/v11.16.0...v11.16.1) (2024-12-09)


### Bug Fixes

* **types:** ensure all fields for `LazyPluginSpec` are optional ([#1843](https://github.com/folke/lazy.nvim/issues/1843)) ([703be1d](https://github.com/folke/lazy.nvim/commit/703be1dda35e142e76e94e7503cf67d6b98a1d35)), closes [#1842](https://github.com/folke/lazy.nvim/issues/1842)

## [11.16.0](https://github.com/folke/lazy.nvim/compare/v11.15.0...v11.16.0) (2024-12-07)


### Features

* **plugin:** added support for virtual plugins. Closes [#1836](https://github.com/folke/lazy.nvim/issues/1836) ([ee64abc](https://github.com/folke/lazy.nvim/commit/ee64abc76be2b237b95d241a924b0323005b868a))


### Bug Fixes

* **plugin:** don't check if dir exists for virtual plugins ([656cf43](https://github.com/folke/lazy.nvim/commit/656cf4309396b7b8b62984e923bf8d8a0013f7d7))
* **render:** show correct key for home. Fixes [#1796](https://github.com/folke/lazy.nvim/issues/1796) ([b08dba8](https://github.com/folke/lazy.nvim/commit/b08dba8107b5bdaaa007f18cf6c0cc0e0fd576aa))

## [11.15.0](https://github.com/folke/lazy.nvim/compare/v11.14.2...v11.15.0) (2024-12-05)


### Features

* **plugin:** show error for local plugins that don't exist. Fixes [#1773](https://github.com/folke/lazy.nvim/issues/1773) ([9570a5a](https://github.com/folke/lazy.nvim/commit/9570a5ae7b17dcde4718c7458fd986c10f015a99))

## [11.14.2](https://github.com/folke/lazy.nvim/compare/v11.14.1...v11.14.2) (2024-11-10)


### Bug Fixes

* **bootstrap:** single forward slash. Fixes [#1747](https://github.com/folke/lazy.nvim/issues/1747) ([aca30f6](https://github.com/folke/lazy.nvim/commit/aca30f63619a7492ecdea8833a065cf83c80f764))
* **completion:** check if command string is a prefix of Lazy ([#1760](https://github.com/folke/lazy.nvim/issues/1760)) ([e9fd76e](https://github.com/folke/lazy.nvim/commit/e9fd76e239cc18da289f9a3f80f35fa16b003175)), closes [#1758](https://github.com/folke/lazy.nvim/issues/1758)
* **docs:** always update helptags for local plugins ([60cf258](https://github.com/folke/lazy.nvim/commit/60cf258a9ae7fffe04bb31141141a91845158dcc))
* **luarocks:** try to install from root manifest ([#1687](https://github.com/folke/lazy.nvim/issues/1687)) ([591ef40](https://github.com/folke/lazy.nvim/commit/591ef40f2da3a26fbcc0466988cd6fe45ca68cae))
* **rocks:** add lib64 plugin directory to package.cpath ([#1717](https://github.com/folke/lazy.nvim/issues/1717)) ([80da254](https://github.com/folke/lazy.nvim/commit/80da254e645f579c28394ee0f08f75a9c9481744))
* **rockspec:** allow binary lua files. Fixes [#1800](https://github.com/folke/lazy.nvim/issues/1800) ([408449a](https://github.com/folke/lazy.nvim/commit/408449a59adb8c2a31c32fff606676b32ce4552a))

## [11.14.1](https://github.com/folke/lazy.nvim/compare/v11.14.0...v11.14.1) (2024-07-25)


### Bug Fixes

* **plugins:** "Vim:E150: Not a directory" on plugin update ([#1679](https://github.com/folke/lazy.nvim/issues/1679)) ([7108809](https://github.com/folke/lazy.nvim/commit/7108809ab18dc1b1e6f402b29e2e1d35a5d311d5))

## [11.14.0](https://github.com/folke/lazy.nvim/compare/v11.13.5...v11.14.0) (2024-07-24)


### Features

* added `opts.git.cooldown` to allow updating plugins on slow connections. Fixes [#1656](https://github.com/folke/lazy.nvim/issues/1656) ([d5686ef](https://github.com/folke/lazy.nvim/commit/d5686efbd00942b3e38de7c08b8df69d961b02f0))
* **plugin:** improve error handling and show better error message ([c02268a](https://github.com/folke/lazy.nvim/commit/c02268ac6e6aab92249d020d75efc588bd9d24fa))


### Bug Fixes

* **plugin:** make .lazy.lua work again ([b4a5a12](https://github.com/folke/lazy.nvim/commit/b4a5a1209e4c64fa67aedf721a383541a64056d1))

## [11.13.5](https://github.com/folke/lazy.nvim/compare/v11.13.4...v11.13.5) (2024-07-22)


### Bug Fixes

* **health:** dont use vim.fn.system to get cmd versions ([7d29719](https://github.com/folke/lazy.nvim/commit/7d29719ade6f5a269e3b7d08b246641b5b079aaa))

## [11.13.4](https://github.com/folke/lazy.nvim/compare/v11.13.3...v11.13.4) (2024-07-22)


### Bug Fixes

* **loader:** add plugins whose rtp got loaded early to start plugins ([34b0126](https://github.com/folke/lazy.nvim/commit/34b0126e5b3966f1dbe148d6f8450213115e76b2))
* **loader:** explicitely set package.loaded.modname to nil to prevent recursive loading errors ([12f2c74](https://github.com/folke/lazy.nvim/commit/12f2c74244cc768d97c83972aa63722389b5d96d))

## [11.13.3](https://github.com/folke/lazy.nvim/compare/v11.13.2...v11.13.3) (2024-07-21)


### Reverts

* fix(loader): add auto loaded module to package.loaded early to prevent require loops ([a692bf8](https://github.com/folke/lazy.nvim/commit/a692bf86883457f45fe3f773bfc8bc4d9e4b070c))

## [11.13.2](https://github.com/folke/lazy.nvim/compare/v11.13.1...v11.13.2) (2024-07-21)


### Bug Fixes

* **loader:** add auto loaded module to package.loaded early to prevent require loops ([18d1c1b](https://github.com/folke/lazy.nvim/commit/18d1c1b47e175cd58dc12bf4792ef4e9a50505fa))

## [11.13.1](https://github.com/folke/lazy.nvim/compare/v11.13.0...v11.13.1) (2024-07-19)


### Bug Fixes

* **build:** only load the plugin before build for `:` build commands ([5bdb12a](https://github.com/folke/lazy.nvim/commit/5bdb12a038e5a72cc793f38893f1a9c9fb741759))

## [11.13.0](https://github.com/folke/lazy.nvim/compare/v11.12.0...v11.13.0) (2024-07-17)


### Features

* **ui:** added mapping descriptions ([6ca90a2](https://github.com/folke/lazy.nvim/commit/6ca90a21202808796418e46d3cebfbb5a44e54a2))

## [11.12.0](https://github.com/folke/lazy.nvim/compare/v11.11.1...v11.12.0) (2024-07-16)


### Features

* **git:** added git network throttle to limit network related git ops per interval. Closes [#1635](https://github.com/folke/lazy.nvim/issues/1635) ([d731a6b](https://github.com/folke/lazy.nvim/commit/d731a6b005fd239e85e555bd57362382f6c1e461))

## [11.11.1](https://github.com/folke/lazy.nvim/compare/v11.11.0...v11.11.1) (2024-07-13)


### Bug Fixes

* **config:** check for lib64. Fixes [#1343](https://github.com/folke/lazy.nvim/issues/1343) ([93499c5](https://github.com/folke/lazy.nvim/commit/93499c5deb37641c6cf71528a93f101d186b409f))
* **lockfile:** ensure newline at EOF for lockfile ([#1639](https://github.com/folke/lazy.nvim/issues/1639)) ([7ed9f71](https://github.com/folke/lazy.nvim/commit/7ed9f7173cdec71a057053d7e6efc20c2c230b95))

## [11.11.0](https://github.com/folke/lazy.nvim/compare/v11.10.4...v11.11.0) (2024-07-11)


### Features

* add plugin name to handlers.managed ([17473db](https://github.com/folke/lazy.nvim/commit/17473db1d79ea30e06126834be7fd95ca511557b))


### Bug Fixes

* **minit:** add tests to package.path when running busted (helpers.lua etc) ([fadebdc](https://github.com/folke/lazy.nvim/commit/fadebdc76b71a1d3658a88a025c6c8fb4749e0f8))
* **util:** strip `-lua` in normname ([54b003c](https://github.com/folke/lazy.nvim/commit/54b003c650f07b771e61566f7be2629beb2b781f))

## [11.10.4](https://github.com/folke/lazy.nvim/compare/v11.10.3...v11.10.4) (2024-07-08)


### Bug Fixes

* **rocks:** try building anyway even when prerequisits have not been met. (will likely fail) ([f0324de](https://github.com/folke/lazy.nvim/commit/f0324defdd43be8aa14aaf3a794ff3d5581f36ba))
* **ui:** don't treat suspended as headless. Closes [#1626](https://github.com/folke/lazy.nvim/issues/1626) ([2dfccd7](https://github.com/folke/lazy.nvim/commit/2dfccd7b948beb26d8bcff7f9113a3a5c85cbc4a))

## [11.10.3](https://github.com/folke/lazy.nvim/compare/v11.10.2...v11.10.3) (2024-07-07)


### Bug Fixes

* **git:** local plugin fixes ([#1624](https://github.com/folke/lazy.nvim/issues/1624)) ([72c0dc9](https://github.com/folke/lazy.nvim/commit/72c0dc9462ab3bf1a68198afabc1eb4e2940d299))

## [11.10.2](https://github.com/folke/lazy.nvim/compare/v11.10.1...v11.10.2) (2024-07-07)


### Bug Fixes

* **git:** only check for new commits for local plugins. Closes [#1512](https://github.com/folke/lazy.nvim/issues/1512) ([81d2bff](https://github.com/folke/lazy.nvim/commit/81d2bfffdc8c84a40d25cae7fd4800178c19a138))

## [11.10.1](https://github.com/folke/lazy.nvim/compare/v11.10.0...v11.10.1) (2024-07-05)


### Bug Fixes

* **lockfile:** keep cond=false and enabed=false in lockfile. Fixes [#1535](https://github.com/folke/lazy.nvim/issues/1535). Fixes [#1606](https://github.com/folke/lazy.nvim/issues/1606) ([baac551](https://github.com/folke/lazy.nvim/commit/baac5517770abd6eee63d11cf4791ef5bf5702e8))

## [11.10.0](https://github.com/folke/lazy.nvim/compare/v11.9.2...v11.10.0) (2024-07-04)


### Features

* **profiling:** merge VeryLazy stats and show startuptime in profile view ([0f2786b](https://github.com/folke/lazy.nvim/commit/0f2786bcc91347188627534471ee75c3f6f16b2d))


### Bug Fixes

* **config:** determine headless only during startup. Fixes [#1608](https://github.com/folke/lazy.nvim/issues/1608) ([6fdd904](https://github.com/folke/lazy.nvim/commit/6fdd904ee45b66d933c5d2f72bcec337e13744f8))
* **plugin:** local spec name ([923e1aa](https://github.com/folke/lazy.nvim/commit/923e1aa7a49d945afa4c03da4f8ff052cd6d14a6))

## [11.9.2](https://github.com/folke/lazy.nvim/compare/v11.9.1...v11.9.2) (2024-07-02)


### Bug Fixes

* **async:** make asyncs abortable ([1fad617](https://github.com/folke/lazy.nvim/commit/1fad61712bd3937dda925775a7736b8efbcbf1a7))
* **health:** check for errors when executing commands. Closes [#1599](https://github.com/folke/lazy.nvim/issues/1599) ([d0921f5](https://github.com/folke/lazy.nvim/commit/d0921f5b9b3d2c5e09618da55a018228edcc4d16))


### Performance Improvements

* **plugin:** minor optim to resolve imports a bit faster ([a9d7ade](https://github.com/folke/lazy.nvim/commit/a9d7ade203b3f3ee3058c082c62afdf8e4bcb416))

## [11.9.1](https://github.com/folke/lazy.nvim/compare/v11.9.0...v11.9.1) (2024-06-30)


### Performance Improvements

* automatically suspend the scheduler when all threads are waiting ([#1591](https://github.com/folke/lazy.nvim/issues/1591)) ([c7ed87f](https://github.com/folke/lazy.nvim/commit/c7ed87f9ca03ea412134d6a6ea55b43232eb6b0c))
* suspend when tasks are active ([2f4ac03](https://github.com/folke/lazy.nvim/commit/2f4ac035bcc66292250de7134d73007b147f64e8))

## [11.9.0](https://github.com/folke/lazy.nvim/compare/v11.8.2...v11.9.0) (2024-06-29)


### Features

* **ui:** use [[ & ]] to navigate between plugins. Fixes [#1463](https://github.com/folke/lazy.nvim/issues/1463) ([5e3c112](https://github.com/folke/lazy.nvim/commit/5e3c112cb32c9cb6e8622aab4446358e039def7c))


### Bug Fixes

* **ui:** when closing details, jump to plugin header. Closes [#1338](https://github.com/folke/lazy.nvim/issues/1338) ([3772914](https://github.com/folke/lazy.nvim/commit/37729140751577e87318c137d90d0e6bb00ceff1))

## [11.8.2](https://github.com/folke/lazy.nvim/compare/v11.8.1...v11.8.2) (2024-06-29)


### Bug Fixes

* **process:** deal with process errors ([a75d950](https://github.com/folke/lazy.nvim/commit/a75d950b8f356733ad2d20c4bdb794179e6d4ff1))
* **ui:** save/restore view right before/after rendering ([5d334b9](https://github.com/folke/lazy.nvim/commit/5d334b9f579aacd09603dd9e19b6730fbfcf4c72))


### Performance Improvements

* **rocks:** `vim.fn.executable` is slow on WSL2, so only check for `luarocks` when needed. Closes [#1585](https://github.com/folke/lazy.nvim/iss
... [TRUNCATED]
```

### File: TODO.md
```md
# ✅ TODO

- [x] progress bar?
- [x] options when opening file
- [x] lazy notify? not ideal when installing missing stuff
- [x] topmods?

- [ ] better merging options?
- [ ] especially what to do with merging of handlers?
- [ ] overwriting keymaps probably doesn't work
- [ ] disabled deps?

- [x] fancy UI to manage all your Neovim plugins
- [x] auto lazy-loading of lua modules
- [x] lazy-loading on events, commands, filetypes and key mappings
- [x] Partial clones instead of shallow clones
- [x] waits till missing deps are installed (bootstrap Neovim and start using it right away)
- [x] Async
- [x] No need to manually compile
- [x] Fast. Automatically caches and compiles byte code of all lua modules needed during startup
- [x] Correct sequencing of dependencies (deps should always be opt. Maybe make everything opt?)
- [x] Config in multiple files
- [x] dev option and patterns for local packages
- [x] Profiling
- [x] lockfile `lazy-lock.json`
- [x] upvalues in `config` & `init`
- [x] automatically check for updates
- [x] commit, branch, tag, version and full semver support
- [x] statusline component to see number of pending updates

- [x] semver https://devhints.io/semver
- [x] auto-loading on completion for lazy-loaded commands
- [x] bootstrap code
- [x] Background update checker
- [x] health checks: check merge conflicts async
  - [x] unsupported props or props from other managers
  - [x] other packages still in site?
  - [x] other package manager artifacts still present? compiled etc
- [x] status page showing running handlers and cache stats
- [x] temp colorscheme used during startup when installing missing plugins
- [x] automatically reloads when config changes are detected
- [x] handlers imply opt
- [x] dependencies imply opt for deps
- [x] show spec errors in health
- [x] fix plugin details
- [ ] show disabled plugins (strikethrough?)
- [ ] log file
- [x] git tests
- [x] Import specs from other plugin managers
- [ ] [packspec](https://github.com/nvim-lua/nvim-package-specification)

  - [ ] add support to specify `engines`, `os` and `cpu` like in `package.json`
  - [ ] semver merging. Should check if two or more semver ranges are compatible and calculate the union range
    - default semver merging strategy: if no version matches all, then use the highest version?
  - [ ] package meta index (package.lua cache for all packages)

- [x] document highlight groups
- [x] document user events
- [x] document API, like lazy.plugins()
- [x] icons

- [x] check in cache if rtp files match
- [x] I think the installation section, specifically the loading part, could use an
      extra sentence or two. I was confused on what `config.plugins` was initially.
      Maybe a quick, "for example, if you have a lua file
      `~/.config/nvim/lua/config/plugins.lua` that returns a table" or something it'd
      remove most question marks I think.
- [x] When auto-installing the plugins the cursor isn't focused on the floating
      window, but on the non-floating window in the background.
- [x] Doing `:Lazy clean` doesn't show which plugins were removed.
- [x] Shouldn't the "Versioning" section be in the "Lockfile" chapter?
- [x] Why are personal dotfiles used as examples? Dotfiles change all the time,
      there's no guarantee this will be relevant or even exist in two years.
- [x] What's the difference between lazy-loading and verylazy-loading?
- [x] Most emojis in "Configuration" aren't shown for me.
- [x] add section on how to uninstall
- [x] add `:Packadd` command or something similar
- [x] headless install
- [x] better keys handling

```

### File: .github\.release-please-manifest.json
```json
{
  ".": "11.17.5"
}

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Description

<!-- Describe the big picture of your changes to communicate to the maintainers
  why we should accept this pull request. -->

## Related Issue(s)

<!--
  If this PR fixes any issues, please link to the issue here.
  - Fixes #<issue_number>
-->

## Screenshots

<!-- Add screenshots of the changes if applicable. -->


```

### File: .github\release-please-config.json
```json
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "packages": {
    ".": {
      "release-type": "simple",
      "extra-files": ["lua/lazy/core/config.lua"]
    }
  }
}

```

### File: doc\lazy.nvim.txt
```txt
*lazy.nvim.txt*                             A modern plugin manager for Neovim

==============================================================================
Table of Contents                                *lazy.nvim-table-of-contents*

1. 📰 What’s new?                           |lazy.nvim-📰-what’s-new?|
  - 11.x                                   |lazy.nvim-📰-what’s-new?-11.x|
2. 🚀 Getting Started                       |lazy.nvim-🚀-getting-started|
  - ✨ Features                 |lazy.nvim-🚀-getting-started-✨-features|
  - ⚡️ Requirements   |lazy.nvim-🚀-getting-started-⚡️-requirements|
3. 🛠️ Installation                       |lazy.nvim-🛠️-installation|
  - Structured Setup         |lazy.nvim-🛠️-installation-structured-setup|
  - Single File Setup       |lazy.nvim-🛠️-installation-single-file-setup|
4. 🔌 Plugin Spec                               |lazy.nvim-🔌-plugin-spec|
  - Spec Source                       |lazy.nvim-🔌-plugin-spec-spec-source|
  - Spec Loading                     |lazy.nvim-🔌-plugin-spec-spec-loading|
  - Spec Setup                         |lazy.nvim-🔌-plugin-spec-spec-setup|
  - Spec Lazy Loading           |lazy.nvim-🔌-plugin-spec-spec-lazy-loading|
  - Spec Versioning               |lazy.nvim-🔌-plugin-spec-spec-versioning|
  - Spec Advanced                   |lazy.nvim-🔌-plugin-spec-spec-advanced|
  - Examples                             |lazy.nvim-🔌-plugin-spec-examples|
  - Lazy Loading                     |lazy.nvim-🔌-plugin-spec-lazy-loading|
  - Versioning                         |lazy.nvim-🔌-plugin-spec-versioning|
5. 📦 Packages                                     |lazy.nvim-📦-packages|
  - Lazy                                        |lazy.nvim-📦-packages-lazy|
  - Rockspec                                |lazy.nvim-📦-packages-rockspec|
  - Packspec                                |lazy.nvim-📦-packages-packspec|
6. ⚙️ Configuration                       |lazy.nvim-⚙️-configuration|
  - 🌈 Highlight Groups|lazy.nvim-⚙️-configuration-🌈-highlight-groups|
7. 🚀 Usage                                           |lazy.nvim-🚀-usage|
  - ▶️ Startup Sequence     |lazy.nvim-🚀-usage-▶️-startup-sequence|
  - 🚀 Commands                         |lazy.nvim-🚀-usage-🚀-commands|
  - 📆 User Events                   |lazy.nvim-🚀-usage-📆-user-events|
  - ❌ Uninstalling                   |lazy.nvim-🚀-usage-❌-uninstalling|
  - 🔒 Lockfile                         |lazy.nvim-🚀-usage-🔒-lockfile|
  - 📦 Migration Guide           |lazy.nvim-🚀-usage-📦-migration-guide|
  - ⚡ Profiling & Debug         |lazy.nvim-🚀-usage-⚡-profiling-&-debug|
  - 📂 Structuring Your Plugins|lazy.nvim-🚀-usage-📂-structuring-your-plugins|
8. 🔥 Developers                                 |lazy.nvim-🔥-developers|
  - Best Practices                  |lazy.nvim-🔥-developers-best-practices|
  - Building                              |lazy.nvim-🔥-developers-building|
  - Minit (Minimal Init)      |lazy.nvim-🔥-developers-minit-(minimal-init)|
9. Links                                                     |lazy.nvim-links|

==============================================================================
1. 📰 What’s new?                           *lazy.nvim-📰-what’s-new?*


11.X                                       *lazy.nvim-📰-what’s-new?-11.x*

- **New Website**: There’s a whole new website with a fresh look and improved
    documentation. Check it out at <https://lazy.folke.io>. The GitHub `README.md`
    has been updated to point to the new website. The `vimdoc` contains all the
    information that is available on the website.
- **Spec Resolution & Merging**: the code that resolves a final spec from a
    plugin’s fragments has been rewritten. This should be a tiny bit faster, but
    more importantly, fixes some issues and is easier to maintain.
- Packages <https://lazy.folke.io/packages> can now specify their dependencies
    and configuration using one of:
    - **Lazy**: `lazy.lua` file
    - **Rockspec**: luarocks <https://luarocks.org/> `*-scm-1.rockspec` file <https://github.com/luarocks/luarocks/wiki/Rockspec-format>
    - **Packspec**: `pkg.json` (experimental, since the format <https://github.com/neovim/packspec/issues/41> is not quite there yet)
    Related _lazy.nvim_ options:
    >lua
        {
          pkg = {
            enabled = true,
            cache = vim.fn.stdpath("state") .. "/lazy/pkg-cache.lua",
            -- the first package source that is found for a plugin will be used.
            sources = {
              "lazy",
              "rockspec", -- will only be used when rocks.enabled is true
              "packspec",
            },
          },
          rocks = {
            enabled = true,
            root = vim.fn.stdpath("data") .. "/lazy-rocks",
            server = "https://nvim-neorocks.github.io/rocks-binaries/",
          },
        }
    <
- Installing neorg <https://github.com/nvim-neorg/neorg> is now as simple as:
    >lua
        { "nvim-neorg/neorg", opts = {} }
    <
- Packages are not limited to just Neovim plugins. You can install any
    **luarocks** package, like:
    >lua
        { "https://github.com/lubyk/yaml" }
    <
    Luarocks packages without a `/lua` directory are never lazy-loaded, since
    it’s just a library.
- `build` functions or `*.lua` build files (like `build.lua`) now run
    asynchronously. You can use `coroutine.yield(status_msg)` to show progress.
    Yielding will also schedule the next `resume` to run in the next tick, so you
    can do long-running tasks without blocking Neovim.


==============================================================================
2. 🚀 Getting Started                       *lazy.nvim-🚀-getting-started*

**lazy.nvim** is a modern plugin manager for Neovim.


✨ FEATURES                     *lazy.nvim-🚀-getting-started-✨-features*

- 📦 Manage all your Neovim plugins with a powerful UI
- 🚀 Fast startup times thanks to automatic caching and bytecode compilation of Lua modules
- 💾 Partial clones instead of shallow clones
- 🔌 Automatic lazy-loading of Lua modules and lazy-loading on events, commands, filetypes, and key mappings
- ⏳ Automatically install missing plugins before starting up Neovim, allowing you to start using it right away
- 💪 Async execution for improved performance
- 🛠️ No need to manually compile plugins
- 🧪 Correct sequencing of dependencies
- 📁 Configurable in multiple files
- 📚 Generates helptags of the headings in `README.md` files for plugins that don’t have vimdocs
- 💻 Dev options and patterns for using local plugins
- 📊 Profiling tools to optimize performance
- 🔒 Lockfile `lazy-lock.json` to keep track of installed plugins
- 🔎 Automatically check for updates
- 📋 Commit, branch, tag, version, and full Semver <https://devhints.io/semver> support
- 📈 Statusline component to see the number of pending updates
- 🎨 Automatically lazy-loads colorschemes


⚡️ REQUIREMENTS       *lazy.nvim-🚀-getting-started-⚡️-requirements*

- Neovim >= **0.8.0** (needs to be built with **LuaJIT**)
- Git >= **2.19.0** (for partial clones support)
- a Nerd Font <https://www.nerdfonts.com/> **(optional)**
- luarocks <https://luarocks.org/> to install rockspecs.
    You can remove `rockspec` from `opts.pkg.sources` to disable this feature.


==============================================================================
3. 🛠️ Installation                       *lazy.nvim-🛠️-installation*

There are multiple ways to install **lazy.nvim**. The **Structured Setup** is
the recommended way, but you can also use the **Single File Setup** if you
prefer to keep everything in your `init.lua`.

Please refer to the Configuration </configuration> section for an overview of
all available options.




STRUCTURED SETUP             *lazy.nvim-🛠️-installation-structured-setup*

>lua
    require("config.lazy")
<

>lua
    -- Bootstrap lazy.nvim
    local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
    if not (vim.uv or vim.loop).fs_stat(lazypath) then
      local lazyrepo = "https://github.com/folke/lazy.nvim.git"
      local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
      if vim.v.shell_error ~= 0 then
        vim.api.nvim_echo({
          { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
          { out, "WarningMsg" },
          { "\nPress any key to exit..." },
        }, true, {})
        vim.fn.getchar()
        os.exit(1)
      end
    end
    vim.opt.rtp:prepend(lazypath)
    
    -- Make sure to setup `mapleader` and `maplocalleader` before
    -- loading lazy.nvim so that mappings are correct.
    -- This is also a good place to setup other settings (vim.opt)
    vim.g.mapleader = " "
    vim.g.maplocalleader = "\\"
    
    -- Setup lazy.nvim
    require("lazy").setup({
      -- highlight-start
      spec = {
        -- import your plugins
        { import = "plugins" },
      },
      -- highlight-end
      -- Configure any other settings here. See the documentation for more details.
      -- colorscheme that will be used when installing plugins.
      install = { colorscheme = { "habamax" } },
      -- automatically check for plugin updates
      checker = { enabled = true },
    })
<

You can then create your plugin specs in `~/.config/nvim/lua/plugins/`. Each
file should return a table with the plugins you want to install.

For more info see Structuring Your Plugins </usage/structuring>


SINGLE FILE SETUP           *lazy.nvim-🛠️-installation-single-file-setup*

>lua
    -- Bootstrap lazy.nvim
    local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
    if not (vim.uv or vim.loop).fs_stat(lazypath) then
      local lazyrepo = "https://github.com/folke/lazy.nvim.git"
      local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
      if vim.v.shell_error ~= 0 then
        vim.api.nvim_echo({
          { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
          { out, "WarningMsg" },
          { "\nPress any key to exit..." },
        }, true, {})
        vim.fn.getchar()
        os.exit(1)
      end
    end
    vim.opt.rtp:prepend(lazypath)
    
    -- Make sure to setup `mapleader` and `maplocalleader` before
    -- loading lazy.nvim so that mappings are correct.
    -- This is also a good place to setup other settings (vim.opt)
    vim.g.mapleader = " "
    vim.g.maplocalleader = "\\"
    
    -- Setup lazy.nvim
    require("lazy").setup({
      -- highlight-start
      spec = {
        -- add your plugins here
      },
      -- highlight-end
      -- Configure any other settings here. See the documentation for more details.
      -- colorscheme that will be used when installing plugins.
      install = { colorscheme = { "habamax" } },
      -- automatically check for plugin updates
      checker = { enabled = true },
    })
<


==============================================================================
4. 🔌 Plugin Spec                               *lazy.nvim-🔌-plugin-spec*


SPEC SOURCE                           *lazy.nvim-🔌-plugin-spec-spec-source*

  -----------------------------------------------------------------------------------
  Property   Type       Description
  ---------- ---------- -------------------------------------------------------------
  [1]        string?    Short plugin url. Will be expanded using
                        config.git.url_format. Can also be a url or dir.

  dir        string?    A directory pointing to a local plugin

  url        string?    A custom git url where the plugin is hosted

  name       string?    A custom name for the plugin used for the local plugin
                        directory and as the display name

  dev        boolean?   When true, a local plugin directory will be used instead. See
                        config.dev
  -----------------------------------------------------------------------------------
A valid spec should define one of `[1]`, `dir` or `url`.


SPEC LOADING                         *lazy.nvim-🔌-plugin-spec-spec-loading*

  --------------------------------------------------------------------------------------------------
  Property       Type                      Description
  -------------- ------------------------- ---------------------------------------------------------
  dependencies   LazySpec[]                A list of plugin names or plugin specs that should be
                                           loaded when the plugin loads. Dependencies are always
                                           lazy-loaded unless specified otherwise. When specifying a
                                           name, make sure the plugin spec has been defined
                                           somewhere else.

  enabled        boolean? or fun():boolean When false, or if the function returns false, then this
                                           plugin will not be included in the spec

  cond           boolean? or               Behaves the same as enabled, but won’t uninstall the
                 fun(LazyPlugin):boolean   plugin when the condition is false. Useful to disable
                                           some plugins in vscode, or firenvim for example.

  priority       number?                   Only useful for start plugins (lazy=false) to force
                                           loading certain plugins first. Default priority is 50.
                                           It’s recommended to set this to a high number for
                                           colorschemes.
  --------------------------------------------------------------------------------------------------

SPEC SETUP                             *lazy.nvim-🔌-plugin-spec-spec-setup*

  --------------------------------------------------------------------------------------------------
  Property   Type                          Description
  ---------- ----------------------------- ---------------------------------------------------------
  init       fun(LazyPlugin)               init functions are always executed during startup. Mostly
                                           useful for setting vim.g.* configuration used by Vim
                                           plugins startup

  opts       table or                      opts should be a table (will be merged with parent
             fun(LazyPlugin, opts:table)   specs), return a table (replaces parent specs) or should
                                           change a table. The table will be passed to the
                                           Plugin.config() function. Setting this value will imply
                                           Plugin.config()

  config     fun(LazyPlugin, opts:table)   config is executed when the plugin loads. The default
             or true                       implementation will automatically run
                                           require(MAIN).setup(opts) if opts or config = true is
                                           set. Lazy uses several heuristics to d
... [TRUNCATED]
```

