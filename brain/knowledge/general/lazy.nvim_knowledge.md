---
id: lazy.nvim-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:03.744845
---

# KNOWLEDGE EXTRACT: lazy.nvim
> **Extracted on:** 2026-03-30 22:29:54
> **Source:** lazy.nvim

---

## File: `.busted`
```
return {
  _all = {
    coverage = false,
  },
  default = {
    verbose = true,
  },
  tests = {
    verbose = true,
  },
}
```

## File: `.editorconfig`
```
root = true

[*]
insert_final_newline = true
indent_style = space
indent_size = 2
charset = utf-8
```

## File: `.gitignore`
```
*.log
/.repro
/.tests
/build
/debug
/doc/tags
foo.*
node_modules
tt.*
```

## File: `.markdownlint-cli2.yaml`
```yaml
config:
  MD013: false
  MD033: false
```

## File: `.markdownlint.yaml`
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

## File: `.neoconf.json`
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

## File: `.styluaignore`
```
lua/lazy/community/_generated.lua
```

## File: `bootstrap.lua`
```
-- Lazy Bootstrapper
-- Usage:
-- ```lua
-- load(vim.fn.system("curl -s https://raw.githubusercontent.com/folke/lazy.nvim/main/bootstrap.lua"))()
-- ```
local M = {}

function M.setup()
  local uv = vim.uv or vim.loop
  if vim.env.LAZY_STDPATH then
    local root = vim.fn.fnamemodify(vim.env.LAZY_STDPATH, ":p"):gsub("[\\/]$", "")
    for _, name in ipairs({ "config", "data", "state", "cache" }) do
      vim.env[("XDG_%s_HOME"):format(name:upper())] = root .. "/" .. name
    end
  end

  if vim.env.LAZY_PATH and not uv.fs_stat(vim.env.LAZY_PATH) then
    vim.env.LAZY_PATH = nil
  end

  local lazypath = vim.env.LAZY_PATH or vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
  if not vim.env.LAZY_PATH and not uv.fs_stat(lazypath) then
    vim.api.nvim_echo({
      {
        "Cloning lazy.nvim\n\n",
        "DiagnosticInfo",
      },
    }, true, {})
    local lazyrepo = "https://github.com/folke/lazy.nvim.git"
    local ok, out = pcall(vim.fn.system, {
      "git",
      "clone",
      "--filter=blob:none",
      lazyrepo,
      lazypath,
    })
    if not ok or vim.v.shell_error ~= 0 then
      vim.api.nvim_echo({
        { "Failed to clone lazy.nvim\n", "ErrorMsg" },
        { vim.trim(out or ""), "WarningMsg" },
        { "\nPress any key to exit...", "MoreMsg" },
      }, true, {})
      vim.fn.getchar()
      os.exit(1)
    end
  end
  vim.opt.rtp:prepend(lazypath)
end
M.setup()

return M
```

## File: `CHANGELOG.md`
```markdown
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

* **rocks:** `vim.fn.executable` is slow on WSL2, so only check for `luarocks` when needed. Closes [#1585](https://github.com/folke/lazy.nvim/issues/1585) ([9ab3061](https://github.com/folke/lazy.nvim/commit/9ab306169060eeab7ebca00653318683e72ab62d))

## [11.8.1](https://github.com/folke/lazy.nvim/compare/v11.8.0...v11.8.1) (2024-06-29)


### Bug Fixes

* **async:** remove debug assert ([3513227](https://github.com/folke/lazy.nvim/commit/3513227a9a41c8e6366e1719f4cefbe891ca73d2))

## [11.8.0](https://github.com/folke/lazy.nvim/compare/v11.7.0...v11.8.0) (2024-06-29)


### Features

* **plugin:** allow loading specs without pkg ([695a058](https://github.com/folke/lazy.nvim/commit/695a05872a5b44e366e5532eb2fe38a64fae8357))

## [11.7.0](https://github.com/folke/lazy.nvim/compare/v11.6.0...v11.7.0) (2024-06-29)


### Features

* **minit:** fallback to habamax when no colorscheme set ([88f4d13](https://github.com/folke/lazy.nvim/commit/88f4d13e5f489eb30959db03a94ebfa10a78b47f))

## [11.6.0](https://github.com/folke/lazy.nvim/compare/v11.5.2...v11.6.0) (2024-06-29)


### Features

* **task:** build procs can now yield a LazyMsg for more control ([9cf7459](https://github.com/folke/lazy.nvim/commit/9cf745939d792204a18d7ad10a54d22386ececf3))

## [11.5.2](https://github.com/folke/lazy.nvim/compare/v11.5.1...v11.5.2) (2024-06-28)


### Bug Fixes

* **git:** tagrefs ([2a6a2dc](https://github.com/folke/lazy.nvim/commit/2a6a2dce1b14f35e7eb7cbe8f25202ed83cba697))

## [11.5.1](https://github.com/folke/lazy.nvim/compare/v11.5.0...v11.5.1) (2024-06-28)


### Bug Fixes

* **rocks:** lua-5.1. Closes [#1575](https://github.com/folke/lazy.nvim/issues/1575) ([4319846](https://github.com/folke/lazy.nvim/commit/4319846b8c8a05975c4139b0bc9f7e6e7a9e6e21))
* **task:** run on_exit async. See [#1569](https://github.com/folke/lazy.nvim/issues/1569) ([60fe75c](https://github.com/folke/lazy.nvim/commit/60fe75c88db22025989600bb53dba247654d9ed5))


### Performance Improvements

* async render ([ab46edb](https://github.com/folke/lazy.nvim/commit/ab46edbd47fa9f380db65dbf0a7c35d18d810b19))
* use timer instead of check for async executor ([f85575a](https://github.com/folke/lazy.nvim/commit/f85575ab23c81eb897fb2cb1240a0fa1cb41f7f4))

## [11.5.0](https://github.com/folke/lazy.nvim/compare/v11.4.2...v11.5.0) (2024-06-27)


### Features

* added `opts.headless` to control ansi output when running headless ([a0a51c0](https://github.com/folke/lazy.nvim/commit/a0a51c06c2fcddda925667142516c89777eb0c8e))
* added localleader-i to inspect a plugin ([2e1167d](https://github.com/folke/lazy.nvim/commit/2e1167df4ab055e8327317ac38210b111cbaec83))
* **health:** show steps to get luarocks working. See [#1570](https://github.com/folke/lazy.nvim/issues/1570) ([c0fd59b](https://github.com/folke/lazy.nvim/commit/c0fd59b020dc4efb91b226b0bbc4a22f28c12321))
* **health:** show user's lazy.nvim version in checkhealth ([9c8e7a4](https://github.com/folke/lazy.nvim/commit/9c8e7a48406109458370f3b52f6f058943db40f4))
* **ui:** keep cursor position when rendering view ([591ded8](https://github.com/folke/lazy.nvim/commit/591ded8309e45806ae3fb58b7b68fe58785a3ada))
* **ui:** remap gx -&gt; K. Fixes [#1561](https://github.com/folke/lazy.nvim/issues/1561) ([e3e4314](https://github.com/folke/lazy.nvim/commit/e3e431480d6c9ab460cf08b1e35311c2ab2c05c4))
* **ui:** show indication of plugins that need build. See [#1563](https://github.com/folke/lazy.nvim/issues/1563) ([53f314d](https://github.com/folke/lazy.nvim/commit/53f314d9e6ef594677acdf5f038a4a042a7f3e38))


### Bug Fixes

* **manage:** dont skip install for plugins that need a build, but dont have an url (like local plugins). Fixes [#1563](https://github.com/folke/lazy.nvim/issues/1563) ([a0391c3](https://github.com/folke/lazy.nvim/commit/a0391c3e21e063df9dee70f17ae7891497cdcec9))
* **meta:** resolve deps from meta instead of fragments. Fixes [#1566](https://github.com/folke/lazy.nvim/issues/1566) ([6a42327](https://github.com/folke/lazy.nvim/commit/6a423278a10ff7b1a76795275111d01632851c48))
* **pkg:** only show pkg changed when effectively changing a pkg file. Fixes [#1567](https://github.com/folke/lazy.nvim/issues/1567) ([24a86d5](https://github.com/folke/lazy.nvim/commit/24a86d5ca4652a77f0f2c78dd7c693a3c369ab68))
* **rocks:** if installing with luarocks (binaries) fails, then build from source. Fixes [#1563](https://github.com/folke/lazy.nvim/issues/1563) ([8227632](https://github.com/folke/lazy.nvim/commit/82276321f5132c680a852bec0bb9b55694ab2a21))
* **runner:** only check for errors when a task is no longer running ([e02c5b1](https://github.com/folke/lazy.nvim/commit/e02c5b1b5787210dfbf89681d94e7861b30aa139))
* **runner:** only use Config.plugins when updated. Fixes [#1560](https://github.com/folke/lazy.nvim/issues/1560) ([97f4df0](https://github.com/folke/lazy.nvim/commit/97f4df0824da13b2b0d065f0dc43c49862581a01))
* **runner:** properly do concurrency ([66a4170](https://github.com/folke/lazy.nvim/commit/66a4170f0e9ab238972f73a268582cf65026a017))
* **runner:** wait_step ([93b3a77](https://github.com/folke/lazy.nvim/commit/93b3a77286c4212850e21a6b3e31d328b5a86df4))
* **ui:** diagnostics without status ([249902a](https://github.com/folke/lazy.nvim/commit/249902ab3194226efec0dbc3e000e758c43b4714))


### Performance Improvements

* prevent active waiting in coroutines. suspend/resume instead ([68cee30](https://github.com/folke/lazy.nvim/commit/68cee30cdb1f7a29d10b44b00506aafa092b6cee))

## [11.4.2](https://github.com/folke/lazy.nvim/compare/v11.4.1...v11.4.2) (2024-06-26)


### Bug Fixes

* **config:** dont start checker/change_detection when running headless ([2aa8e06](https://github.com/folke/lazy.nvim/commit/2aa8e061f22579b0cabc74f05a90f7344d92195c))
* **git:** fetch commit from origin or local to check if branch was changed. See [#1549](https://github.com/folke/lazy.nvim/issues/1549) ([28e435b](https://github.com/folke/lazy.nvim/commit/28e435b7f34eecd8b90bc87ac71c70b79fcb03b3))
* **rocks:** build.type instead of build.build_type ([aa1c957](https://github.com/folke/lazy.nvim/commit/aa1c9572aa1916e582f9b9c3d43e272b4f23b326))
* **rockspec:** dont lazy-load rock deps ([4733611](https://github.com/folke/lazy.nvim/commit/473361139cc05936cd5afb08ab68e5bee1ebb5b3))
* **runner:** bring concurrency back ([56075b5](https://github.com/folke/lazy.nvim/commit/56075b57c421fc5e751c1da7a7f1bf18ec1499a7))
* **ui:** don't show output when it's the same as error ([e79805d](https://github.com/folke/lazy.nvim/commit/e79805d706f815a62467260cb307844c368c3dba))


### Performance Improvements

* tasks are now fully async ([0614ca6](https://github.com/folke/lazy.nvim/commit/0614ca6ca629704cb1846c0d6f9a250b526900b9))
* **util:** improve impl of throttle ([3695215](https://github.com/folke/lazy.nvim/commit/36952153ecb5b196c74e2d9a28eb0e01a9eb02fe))

## [11.4.1](https://github.com/folke/lazy.nvim/compare/v11.4.0...v11.4.1) (2024-06-25)


### Bug Fixes

* **health:** show what plugins need luarocks and if none, use warnings instead of errors. See [#1551](https://github.com/folke/lazy.nvim/issues/1551) ([0d9fd63](https://github.com/folke/lazy.nvim/commit/0d9fd636beb9e3783edcdba2b31932280bdc05f7))

## [11.4.0](https://github.com/folke/lazy.nvim/compare/v11.3.0...v11.4.0) (2024-06-25)


### Features

* **pkg:** utils to get rock to url mappings ([be74a8a](https://github.com/folke/lazy.nvim/commit/be74a8a535fea6a480143fb52b4d6958d9e2da94))
* **rocks:** simple rockspecs are now fully resolved by lazy without luarocks. See [#1548](https://github.com/folke/lazy.nvim/issues/1548) ([6b8bf58](https://github.com/folke/lazy.nvim/commit/6b8bf58ebf9114f8f31fb78cbf057e452cb0e540))


### Bug Fixes

* **meta:** only tag new top-level pkg fragment as optional ([25981e1](https://github.com/folke/lazy.nvim/commit/25981e1f3927ee0b22aefea122ebac1cddafdca6))

## [11.3.0](https://github.com/folke/lazy.nvim/compare/v11.2.1...v11.3.0) (2024-06-25)


### Features

* **rocks:** use hererocks to install luarocks when luarocks is not found ([d87da76](https://github.com/folke/lazy.nvim/commit/d87da7667939deff2ed8b5a3c198d9ea2e03fee4))


### Bug Fixes

* **fragments:** check for empty plugin names ([dea1f68](https://github.com/folke/lazy.nvim/commit/dea1f687fe6e15eb3098557a69d44231ebcb6cf5))
* **meta:** no need to check for old_dir when frags were not built yet. Fixes [#1550](https://github.com/folke/lazy.nvim/issues/1550) ([24c8322](https://github.com/folke/lazy.nvim/commit/24c832213c505a0d7ca021c0e14bba43e0fef75c))
* **rocks:** better errors / warnings when something goes wrong with luarocks ([7d3f691](https://github.com/folke/lazy.nvim/commit/7d3f69104fb39d3e6e12f808204b3a7b38f86916))
* **rocks:** hererocks paths on windows ([45cd8d3](https://github.com/folke/lazy.nvim/commit/45cd8d3f0fab197e6e0391cffa38879bdda4c2cd))
* **rocks:** windows ([4ca3e9a](https://github.com/folke/lazy.nvim/commit/4ca3e9aa51c03dda73b40ec9901deac5d4f11c69))

## [11.2.1](https://github.com/folke/lazy.nvim/compare/v11.2.0...v11.2.1) (2024-06-24)


### Bug Fixes

* **loader:** no need to check plugin.dir in auto_load ([62a47b9](https://github.com/folke/lazy.nvim/commit/62a47b921fbffb3c1c8088a731029ae234f98851))

## [11.2.0](https://github.com/folke/lazy.nvim/compare/v11.1.0...v11.2.0) (2024-06-24)


### Features

* rewrite some known plugins to lazy specs instead of luarocks (plenary.nvim). Closes [#1540](https://github.com/folke/lazy.nvim/issues/1540) ([a089d43](https://github.com/folke/lazy.nvim/commit/a089d43dba7438532c56e1c582c5974713bd48f8))


### Performance Improvements

* minimize meta rebuild when loading specs ([1446f6c](https://github.com/folke/lazy.nvim/commit/1446f6cfbb4ca0a7ee0baf3acc86ab5e4be5ab22))

## [11.1.0](https://github.com/folke/lazy.nvim/compare/v11.0.1...v11.1.0) (2024-06-24)


### Features

* make it easier to disable luarocks ([07c067a](https://github.com/folke/lazy.nvim/commit/07c067a1a82bb0988179e1887bba9df4721b3ea7))
* show rockspec deps in plugin details ([656d3d1](https://github.com/folke/lazy.nvim/commit/656d3d1f5b5910e50af3d67286999ff7088ebfb6))


### Bug Fixes

* **health:** added luarocks check to health ([0f45c0d](https://github.com/folke/lazy.nvim/commit/0f45c0d0623b4850716898a5e399c844466690f6))
* **health:** only check for luarocks when luarocks is enabled. ([ae4881d](https://github.com/folke/lazy.nvim/commit/ae4881d36e7f589124f8eb7febfc6a8b58f8e027))
* **health:** show missing luarocks as warning ([e3ee51b](https://github.com/folke/lazy.nvim/commit/e3ee51b6680a116649da56f6c651d53c3e47be4e))
* **runner:** sync package specs after installing and before building ([105d480](https://github.com/folke/lazy.nvim/commit/105d4805ad58875d0b0fafe1185679539b8bc69a))

## [11.0.1](https://github.com/folke/lazy.nvim/compare/v11.0.0...v11.0.1) (2024-06-24)


### Bug Fixes

* **rocks:** dont trigger rebuild for luarocks when build is overriden ([146de4e](https://github.com/folke/lazy.nvim/commit/146de4e801f9169e79052a51365eaae789094611))

## [11.0.0](https://github.com/folke/lazy.nvim/compare/v10.24.3...v11.0.0) (2024-06-24)


### ⚠ BREAKING CHANGES

* new docs for v11.0

### Features

* added support for plugin packages by lazy, rockspec and packspec ([3be55a4](https://github.com/folke/lazy.nvim/commit/3be55a46158cde17e2b853e531d260f3738a5346))
* **build:** build files and functions are now async. use coroutine.yield to interrupt and report progress ([368747b](https://github.com/folke/lazy.nvim/commit/368747bc9a314b4f0745547ebdcc3fbc4d100c0a))
* luarocks support ([f1ba2e3](https://github.com/folke/lazy.nvim/commit/f1ba2e3d057ae5c03d04134a9d538d0b2251f13b))
* **meta:** check for dir changes for plugins already added to the rtp ([ee2ca39](https://github.com/folke/lazy.nvim/commit/ee2ca39f672a2d6f4cbb683b525e6b3d91f3fc0c))
* new docs for v11.0 ([183f59e](https://github.com/folke/lazy.nvim/commit/183f59e2e85dea0c38ed7d16c7c7e543c0b739c7))
* packspec ([8eba74c](https://github.com/folke/lazy.nvim/commit/8eba74c3fc41e1a364225f744022f8b3ff11d796))
* **pkg:** import package specs in the scope of the plugin ([c1912e2](https://github.com/folke/lazy.nvim/commit/c1912e23481ba72a8d8f7a5c736f5e2547e6853e))
* rewrite of spec resolving ([75ffe56](https://github.com/folke/lazy.nvim/commit/75ffe56f70faac43f077796b91178d2f1419f8ce))
* spec.rocks is no longer needed & added support for installing any luarock ([fcfd548](https://github.com/folke/lazy.nvim/commit/fcfd54835da5af64c6046060f4db62c4626d209c))


### Bug Fixes

* **fragments:** prevent adding the same spec instance more than once ([dbffad6](https://github.com/folke/lazy.nvim/commit/dbffad6f44674a3c1b23c649a0abab299d7349d8))
* **luarocks:** cleanup luarocks when deleting a plugin ([b73c57e](https://github.com/folke/lazy.nvim/commit/b73c57ed9ec8e63bbb867d21a3f3a865224b25d4))
* **pkg:** automatically update pkgs when editing a pkg file ([7b6ddbf](https://github.com/folke/lazy.nvim/commit/7b6ddbfc137ad5d8b178a3bbf5a1338630f30625))
* **pkg:** correctly pre-load package specs and remove them when needed during resolve ([4326d4b](https://github.com/folke/lazy.nvim/commit/4326d4b487d4facc19b375ca30cd633cf56d88ed))
* **pkg:** make sure state dir exists ([3515cb5](https://github.com/folke/lazy.nvim/commit/3515cb518f61c02b41cd3a8d8135c9a5862a982f))
* **pkg:** versioning and reload specs when pkg-cache is dirty ([fd8229d](https://github.com/folke/lazy.nvim/commit/fd8229d6e312e83d6bafda256adf0e650b13ca01))
* **rocks:** only build rockspec when it has deps or an advanced build step ([9a6c219](https://github.com/folke/lazy.nvim/commit/9a6c21982638b6e2ea498514baee9186c0e60d82))

## [10.24.3](https://github.com/folke/lazy.nvim/compare/v10.24.2...v10.24.3) (2024-06-23)


### Bug Fixes

* **util:** dump ([025520d](https://github.com/folke/lazy.nvim/commit/025520d083c61baa7cd1f45807f5fe1ac9fbb50d))

## [10.24.2](https://github.com/folke/lazy.nvim/compare/v10.24.1...v10.24.2) (2024-06-16)


### Bug Fixes

* **plugin:** rebuild optional when needed and remove frags from parent deps. Fixes [#1402](https://github.com/folke/lazy.nvim/issues/1402) ([b4316da](https://github.com/folke/lazy.nvim/commit/b4316da7310682144c279c5f0451e59ee5f6c9d1))

## [10.24.1](https://github.com/folke/lazy.nvim/compare/v10.24.0...v10.24.1) (2024-06-16)


### Bug Fixes

* **plugin:** better way of dealing with local specs. Fixes [#1524](https://github.com/folke/lazy.nvim/issues/1524) ([be5dfba](https://github.com/folke/lazy.nvim/commit/be5dfba54216ccb80959df24d48540f07ee127a3))

## [10.24.0](https://github.com/folke/lazy.nvim/compare/v10.23.0...v10.24.0) (2024-06-15)


### Features

* find local_spec in parent directories as well. Closes [#1519](https://github.com/folke/lazy.nvim/issues/1519) ([e2e10d9](https://github.com/folke/lazy.nvim/commit/e2e10d9cbe133265ccdcc44cafa7c10773d96837))


### Bug Fixes

* **plugin:** check optional plugins again after resolving enabled. Fixes [#1402](https://github.com/folke/lazy.nvim/issues/1402) ([067fd41](https://github.com/folke/lazy.nvim/commit/067fd41933c9f59eb3445eb942052c651a4c9a62))

## [10.23.0](https://github.com/folke/lazy.nvim/compare/v10.22.2...v10.23.0) (2024-06-07)


### Features

* **plugin:** `opts_extend` can be a list of dotted keys that will be extended instead of merged ([1f7b720](https://github.com/folke/lazy.nvim/commit/1f7b720cffa6d8f00ebb040bc60e8e056e0a6002))
* **util:** opts merging now supports lists extending by tagging a table with __extend = true. Use with care ([74fd361](https://github.com/folke/lazy.nvim/commit/74fd3611f291a2506c5534109689bb7b028f0566))

## [10.22.2](https://github.com/folke/lazy.nvim/compare/v10.22.1...v10.22.2) (2024-06-06)


### Bug Fixes

* **keys:** buffer-local nop mappings ([ff90417](https://github.com/folke/lazy.nvim/commit/ff904178089582f90fdc625493f3d3bddbefd6ea))
* **keys:** never lazy-load `&lt;nop&gt;` or empty rhs keymaps ([3e4c795](https://github.com/folke/lazy.nvim/commit/3e4c795cec32481bc6d0b30c05125fdf7ef2d412))

## [10.22.1](https://github.com/folke/lazy.nvim/compare/v10.22.0...v10.22.1) (2024-06-02)


### Bug Fixes

* force new release ([9242edb](https://github.com/folke/lazy.nvim/commit/9242edb73939e7508dbd827e9c013579391f0668))

## [10.22.0](https://github.com/folke/lazy.nvim/compare/v10.21.2...v10.22.0) (2024-06-01)


### Features

* set `vim.env.LAZY` to lazy root ([6a141a6](https://github.com/folke/lazy.nvim/commit/6a141a6dbb6f6b5495ef6716c0dce898546d7b2c))

## [10.21.2](https://github.com/folke/lazy.nvim/compare/v10.21.1...v10.21.2) (2024-05-31)


### Bug Fixes

* **ui:** deduplicate plugins when selecting multiple ([#1491](https://github.com/folke/lazy.nvim/issues/1491)) ([b77aaa0](https://github.com/folke/lazy.nvim/commit/b77aaa08cb5b178ed8662765caa41c70ff254a4c))

## [10.21.1](https://github.com/folke/lazy.nvim/compare/v10.21.0...v10.21.1) (2024-05-31)


### Bug Fixes

* **view:** backward compat for older Neovim versions. Fixes [#1489](https://github.com/folke/lazy.nvim/issues/1489) ([917dfbe](https://github.com/folke/lazy.nvim/commit/917dfbe2a9b606443639d1e809f2e4561a6dd654))

## [10.21.0](https://github.com/folke/lazy.nvim/compare/v10.20.5...v10.21.0) (2024-05-26)


### Features

* added support for local spec files `.lazy.lua` ([9dde1f1](https://github.com/folke/lazy.nvim/commit/9dde1f1bce44a8fd8cb885b5a8e8d47d8fd7b8c1))
* single-plugin keys in the lazy view in visual mode ([#1476](https://github.com/folke/lazy.nvim/issues/1476)) ([7667a73](https://github.com/folke/lazy.nvim/commit/7667a73dee381c5fb7d538f6152aeb591e3f0372))


### Bug Fixes

* **render:** disable underline for diagnostics ([#1478](https://github.com/folke/lazy.nvim/issues/1478)) ([ea7b9c3](https://github.com/folke/lazy.nvim/commit/ea7b9c3c3fd9026e1a5ae27950585df9a42ccd5b))

## [10.20.5](https://github.com/folke/lazy.nvim/compare/v10.20.4...v10.20.5) (2024-05-21)


### Bug Fixes

* **checker:** ignore dev plugins ([#1384](https://github.com/folke/lazy.nvim/issues/1384)) ([2e04a0c](https://github.com/folke/lazy.nvim/commit/2e04a0c02c17facd3772c382099215acbe72535b))
* **git:** force `autocrlf=false`. Fixes [#1055](https://github.com/folke/lazy.nvim/issues/1055) ([d2a4ce2](https://github.com/folke/lazy.nvim/commit/d2a4ce22dc02aa08c176cd7692b5b0ed74e4722b))
* **help:** get rid of any tbl_flatten or iter flatten code ([56a34a8](https://github.com/folke/lazy.nvim/commit/56a34a825b55e0e30cd9df0e055e428a13afd4aa))
* **keys:** properly deal with ft list for keys. Fixes [#1448](https://github.com/folke/lazy.nvim/issues/1448) ([82cf974](https://github.com/folke/lazy.nvim/commit/82cf974e0939b3440c4470cbcd8e7869abfe480b))
* **keys:** properly re-create buffer-local mappings. Fixes [#1448](https://github.com/folke/lazy.nvim/issues/1448) ([39de11a](https://github.com/folke/lazy.nvim/commit/39de11a2fa7f4b91556631c49a673bf3e48bcc16))
* use vim.iter():flatten():totable() over vim.tbl_flatten ([#1454](https://github.com/folke/lazy.nvim/issues/1454)) ([d039aec](https://github.com/folke/lazy.nvim/commit/d039aecddb414c2df9d295e9182ed217196a2c1c))

## [10.20.4](https://github.com/folke/lazy.nvim/compare/v10.20.3...v10.20.4) (2024-05-12)


### Bug Fixes

* **heath:** vim.uv. Fixes [#1412](https://github.com/folke/lazy.nvim/issues/1412) ([481aed7](https://github.com/folke/lazy.nvim/commit/481aed70cc4d8e8a38463fd16edf81a23c153247))
* **reload:** strings in lua reload ([#1439](https://github.com/folke/lazy.nvim/issues/1439)) ([2fcbcaf](https://github.com/folke/lazy.nvim/commit/2fcbcaf07ab79594f2ba25ebf6f4c47e250c33be))
* **ui:** add conditional `nvim_get_hl_by_name` for Neovim 0.8.0 ([#1429](https://github.com/folke/lazy.nvim/issues/1429)) ([24234f4](https://github.com/folke/lazy.nvim/commit/24234f47a21ca690de829ea1159b553a733f3968))
* **ui:** hover now opens repo url when no diff with main. Fixes [#1430](https://github.com/folke/lazy.nvim/issues/1430) ([4084506](https://github.com/folke/lazy.nvim/commit/40845063a2586b725d84d44e41fe2c8737751a30))
* **ui:** set backdrop filetype to `lazy_backdrop`. Fixes [#1399](https://github.com/folke/lazy.nvim/issues/1399) ([31ddbea](https://github.com/folke/lazy.nvim/commit/31ddbea7c10b6920c9077b66c97951ca8682d5c8))

## [10.20.3](https://github.com/folke/lazy.nvim/compare/v10.20.2...v10.20.3) (2024-03-28)


### Bug Fixes

* **ui:** disable backdrop when Neovim is transparent ([0ccf031](https://github.com/folke/lazy.nvim/commit/0ccf0312270d2d976ec551a9034bf05720f2486b))

## [10.20.2](https://github.com/folke/lazy.nvim/compare/v10.20.1...v10.20.2) (2024-03-27)


### Bug Fixes

* **ui:** only enable backdrop when guicolors is set. Fixes [#1387](https://github.com/folke/lazy.nvim/issues/1387) ([d37a76b](https://github.com/folke/lazy.nvim/commit/d37a76b87137c777f3d778ed03729d7f332a85f0))
* **ui:** special handling for floats closed before VimEnter. Seems that WinClosed events dont execute before that. Fixes [#1390](https://github.com/folke/lazy.nvim/issues/1390) ([eefb897](https://github.com/folke/lazy.nvim/commit/eefb8974d6a092da6e1631855e4288499b651fdd))

## [10.20.1](https://github.com/folke/lazy.nvim/compare/v10.20.0...v10.20.1) (2024-03-26)


### Bug Fixes

* **ui:** properly cleanup on `:quit`. Fixes [#1385](https://github.com/folke/lazy.nvim/issues/1385) ([79e2e85](https://github.com/folke/lazy.nvim/commit/79e2e8593410f199b85f5d61a83704a16169282f))

## [10.20.0](https://github.com/folke/lazy.nvim/compare/v10.19.0...v10.20.0) (2024-03-26)


### Features

* **ui:** backdrop for the lazy floating window. Can be disabled with `opts.ui.backdrop` ([a6b74f3](https://github.com/folke/lazy.nvim/commit/a6b74f30d5aab79a40d932f449c0aa5d4a0c6934))


### Bug Fixes

* **types:** fixed type for `version`. Fixes [#1381](https://github.com/folke/lazy.nvim/issues/1381) ([eade87f](https://github.com/folke/lazy.nvim/commit/eade87fb837d6cdeef94587ce5e8c8dfb9f88920))

## [10.19.0](https://github.com/folke/lazy.nvim/compare/v10.18.3...v10.19.0) (2024-03-22)


### Features

* **util:** option to force system app for util.open ([66466a2](https://github.com/folke/lazy.nvim/commit/66466a2594ab0c446193772a68c236c7e4e02ade))

## [10.18.3](https://github.com/folke/lazy.nvim/compare/v10.18.2...v10.18.3) (2024-03-22)


### Bug Fixes

* **cache:** vim.loop fallback ([#1375](https://github.com/folke/lazy.nvim/issues/1375)) ([9131ea4](https://github.com/folke/lazy.nvim/commit/9131ea4c4ae59e347716659088a76d9b9ce3b2f5))

## [10.18.2](https://github.com/folke/lazy.nvim/compare/v10.18.1...v10.18.2) (2024-03-22)


### Bug Fixes

* **ui:** Add "bot" to dimmed commands list ([#1367](https://github.com/folke/lazy.nvim/issues/1367)) ([b6f7ef8](https://github.com/folke/lazy.nvim/commit/b6f7ef856b36c5edbe9f03e3a8554b97c458c953))

## [10.18.1](https://github.com/folke/lazy.nvim/compare/v10.18.0...v10.18.1) (2024-03-22)


### Bug Fixes

* uv shim was not falling back to vim.loop ([#1370](https://github.com/folke/lazy.nvim/issues/1370)) ([61dddae](https://github.com/folke/lazy.nvim/commit/61dddaec58f8594e40e95a8d5069ce7e493089df))

## [10.18.0](https://github.com/folke/lazy.nvim/compare/v10.17.0...v10.18.0) (2024-03-22)


### Features

* refactor all vim.loop -&gt; vim.uv and add a shim when needed ([9e157df](https://github.com/folke/lazy.nvim/commit/9e157df077d24654d0cdefe08158cd4f76e85fe8))

## [10.17.0](https://github.com/folke/lazy.nvim/compare/v10.16.0...v10.17.0) (2024-03-07)


### Features

* **loader:** warn when maplocalleader is changed after init ([#1326](https://github.com/folke/lazy.nvim/issues/1326)) ([0694651](https://github.com/folke/lazy.nvim/commit/0694651fd37c3645e1683b4f392d4e38e7d2991b))


### Bug Fixes

* **manage:** better support for using the default colorscheme during install. See [#1277](https://github.com/folke/lazy.nvim/issues/1277) ([670a6fe](https://github.com/folke/lazy.nvim/commit/670a6fec7f9b03134849e308d87f4dc316875c46))
* **types:** fix incorrect LuaLS types ([#1339](https://github.com/folke/lazy.nvim/issues/1339)) ([5aea4e7](https://github.com/folke/lazy.nvim/commit/5aea4e7021287d7bcda6f31d7ad234580940be32))
* **ui:** remove a single space character from home title ([#1309](https://github.com/folke/lazy.nvim/issues/1309)) ([d5c58bb](https://github.com/folke/lazy.nvim/commit/d5c58bb1937f8aee390f206e724ef23b0cc95eb3))
* update to new treesitter capture groups ([#1294](https://github.com/folke/lazy.nvim/issues/1294)) ([298bed1](https://github.com/folke/lazy.nvim/commit/298bed190e40b67bb1c20c4d5845c2c0c7da450f))

## [10.16.0](https://github.com/folke/lazy.nvim/compare/v10.15.1...v10.16.0) (2024-01-21)


### Features

* **plugin:** dev.path can now be a function ([#1157](https://github.com/folke/lazy.nvim/issues/1157)) ([a6f782a](https://github.com/folke/lazy.nvim/commit/a6f782adc1ace840a7e671c731daab7851cba6af))
* **ui:** add style to dimmed commits ([#1210](https://github.com/folke/lazy.nvim/issues/1210)) ([7ded44c](https://github.com/folke/lazy.nvim/commit/7ded44ce2a442aa32b90488b8f1f9c8ca6899f3b))


### Bug Fixes

* **fs:** error when plugin directory to delete is not a valid directory ([47d4baa](https://github.com/folke/lazy.nvim/commit/47d4baafcc370f16c195fd718f37f8fb1e0aa9a1))
* **git:** comment sign detection in get_config function ([#1281](https://github.com/folke/lazy.nvim/issues/1281)) ([d0d410b](https://github.com/folke/lazy.nvim/commit/d0d410bc222a475202d9c2b55d1c5fbd12c26ffe))
* **health:** dont warn on submodules. Fixes [#1174](https://github.com/folke/lazy.nvim/issues/1174) ([1b3df6c](https://github.com/folke/lazy.nvim/commit/1b3df6c00797e1b12f7c16148261e9dd841a33dd))
* **keys:** allow global/local ft keymaps to exist at the same time. Fixes [#1241](https://github.com/folke/lazy.nvim/issues/1241) ([5757b55](https://github.com/folke/lazy.nvim/commit/5757b551fc6066d836b9e45f70b41561ca619272))
* **keys:** fix abbreviation expansion on lazy load ([#1219](https://github.com/folke/lazy.nvim/issues/1219)) ([d09084c](https://github.com/folke/lazy.nvim/commit/d09084c4b1f5c58724152a4acad7c880117a95ea))
* **keys:** make sure we don't delete the global mapping when executing an ft keymap. See [#1241](https://github.com/folke/lazy.nvim/issues/1241) ([a9b9a4b](https://github.com/folke/lazy.nvim/commit/a9b9a4b3a2dcc1e81828cfd74bfb61193b014b67))

## [10.15.1](https://github.com/folke/lazy.nvim/compare/v10.15.0...v10.15.1) (2023-11-04)


### Bug Fixes

* **build:** allow build=false to skip building ([314193a](https://github.com/folke/lazy.nvim/commit/314193af1d63181bff65e8b24db416e34c5fae86))
* **ui:** properly highlight breaking change commit scope ([#1160](https://github.com/folke/lazy.nvim/issues/1160)) ([3674036](https://github.com/folke/lazy.nvim/commit/3674036a59a6a4a65559343d606a92145a782533))

## [10.15.0](https://github.com/folke/lazy.nvim/compare/v10.14.6...v10.15.0) (2023-10-25)


### Features

* **ui:** check pinned packages that can't be updated ([#1139](https://github.com/folke/lazy.nvim/issues/1139)) ([4446fdb](https://github.com/folke/lazy.nvim/commit/4446fdb9af1b1c41560f6cc41452eee826a8bce0))


### Bug Fixes

* **loader:** when reloading, clear plugin properties cache ([#1153](https://github.com/folke/lazy.nvim/issues/1153)) ([312e424](https://github.com/folke/lazy.nvim/commit/312e424a084a43b8b786f786b884be60043c23dc)), closes [#445](https://github.com/folke/lazy.nvim/issues/445)

## [10.14.6](https://github.com/folke/lazy.nvim/compare/v10.14.5...v10.14.6) (2023-10-17)


### Bug Fixes

* **cmd:** schedule error message instead of showing directly ([03419f3](https://github.com/folke/lazy.nvim/commit/03419f3e5f7590194d599aa8a1a7a7841409d141))
* **loader:** dont autoload when lazy handlers have not been setup yet. Fixes [#1132](https://github.com/folke/lazy.nvim/issues/1132) ([daab5fe](https://github.com/folke/lazy.nvim/commit/daab5fe2807c55867d5f7cfb6ef0944783361be2))
* **ui:** running tasks are now less twitchy ([7613ab2](https://github.com/folke/lazy.nvim/commit/7613ab2abb1bd99e039ae02030bc2c48b7626925))

## [10.14.5](https://github.com/folke/lazy.nvim/compare/v10.14.4...v10.14.5) (2023-10-17)


### Bug Fixes

* **loader:** fixed event check in reload. Fixes [#1124](https://github.com/folke/lazy.nvim/issues/1124) ([cdfa788](https://github.com/folke/lazy.nvim/commit/cdfa78888159323abc931db26f3301360393fbb7))

## [10.14.4](https://github.com/folke/lazy.nvim/compare/v10.14.3...v10.14.4) (2023-10-16)


### Bug Fixes

* **ui:** fixed keymaps in debug view ([fb9795e](https://github.com/folke/lazy.nvim/commit/fb9795e49fcd45e99bf386c675fbca28d98bf0a6))

## [10.14.3](https://github.com/folke/lazy.nvim/compare/v10.14.2...v10.14.3) (2023-10-16)


### Performance Improvements

* **plugin:** cache lazy handler values ([c1b9887](https://github.com/folke/lazy.nvim/commit/c1b98873730d7121fec6a2f732b2083cd2cd62bf))

## [10.14.2](https://github.com/folke/lazy.nvim/compare/v10.14.1...v10.14.2) (2023-10-16)


### Bug Fixes

* **plugin:** work-around for Plugin.values error. Will add proper fix later. Fixes [#1124](https://github.com/folke/lazy.nvim/issues/1124) ([2270bbb](https://github.com/folke/lazy.nvim/commit/2270bbbc48503f468633cc5c2065321001c4f0ac))

## [10.14.1](https://github.com/folke/lazy.nvim/compare/v10.14.0...v10.14.1) (2023-10-16)


### Bug Fixes

* **loader:** don't load handlers before installing plugins ([1cfd6d1](https://github.com/folke/lazy.nvim/commit/1cfd6d1f368ab72690e31cf4d8e15c36d8b60202))

## [10.14.0](https://github.com/folke/lazy.nvim/compare/v10.13.4...v10.14.0) (2023-10-15)


### Features

* **plugin:** treat url changes as warnings. They will only be shown with checkhealth ([0c53d46](https://github.com/folke/lazy.nvim/commit/0c53d4673ff02c57a192558325b394cfd9adde0f))


### Bug Fixes

* **plugin:** dont allow `dir` changes when we already loaded files from the plugin's old dir. Show an error in this case. Fixes [#993](https://github.com/folke/lazy.nvim/issues/993) ([c8e2091](https://github.com/folke/lazy.nvim/commit/c8e2091e6d2836b587b9892e0fb64afaec36926a))
* **plugin:** improved dir/dev merging. Fixes [#993](https://github.com/folke/lazy.nvim/issues/993) ([3dc413d](https://github.com/folke/lazy.nvim/commit/3dc413d6fd279dfff777a9f9a964697a16c5aabc))

## [10.13.4](https://github.com/folke/lazy.nvim/compare/v10.13.3...v10.13.4) (2023-10-14)


### Bug Fixes

* **cmd:** lazy-cmds no longer show an error for buffer-local commands ([3b31897](https://github.com/folke/lazy.nvim/commit/3b31897275d5c09e2654db1c163b87eb383ca25e))

## [10.13.3](https://github.com/folke/lazy.nvim/compare/v10.13.2...v10.13.3) (2023-10-14)


### Bug Fixes

* **ui:** sort lazy plugin handlers ([ad5da0a](https://github.com/folke/lazy.nvim/commit/ad5da0ae20beca5dd89cb17c515c237c46c37b1e))

## [10.13.2](https://github.com/folke/lazy.nvim/compare/v10.13.1...v10.13.2) (2023-10-13)


### Bug Fixes

* **float:** disable swapfile for files shown in Float ([3769461](https://github.com/folke/lazy.nvim/commit/37694611946387dc79d546bdc193bc8611ac1c6d))
* **util:** Util.merge now skips nil args ([70f764b](https://github.com/folke/lazy.nvim/commit/70f764bf735f74aed795188aeb8e57ccae0ae94e))

## [10.13.1](https://github.com/folke/lazy.nvim/compare/v10.13.0...v10.13.1) (2023-10-12)


### Bug Fixes

* **git:** unset GIT_INDEX_FILE so we dont accidentally overwrite a different git repo. Fixes [#1107](https://github.com/folke/lazy.nvim/issues/1107) ([7f70dd1](https://github.com/folke/lazy.nvim/commit/7f70dd17497973f2a83e7e46aa7479111174e765))

## [10.13.0](https://github.com/folke/lazy.nvim/compare/v10.12.0...v10.13.0) (2023-10-12)


### Features

* **keys:** include custom keys in help menu ([#1105](https://github.com/folke/lazy.nvim/issues/1105)) ([43c284a](https://github.com/folke/lazy.nvim/commit/43c284a57870e1a7ed42782eacf444a6a752f81e))

## [10.12.0](https://github.com/folke/lazy.nvim/compare/v10.11.0...v10.12.0) (2023-10-11)


### Features

* **event:** added support for structured events (see readme on event) ([303a3ed](https://github.com/folke/lazy.nvim/commit/303a3ed6a874bb5bdebf11ecdf99e1dfa3eed2c3))
* **event:** custom lazy event hook for distros ([b65d308](https://github.com/folke/lazy.nvim/commit/b65d3086623448b93bf02055f73819b76ca1dd78))


### Bug Fixes

* **ui:** use actual handler values for rendering plugin handlers ([99ee284](https://github.com/folke/lazy.nvim/commit/99ee28473962d9ab8aa11db2d2cc201e38f0f432))

## [10.11.0](https://github.com/folke/lazy.nvim/compare/v10.10.0...v10.11.0) (2023-10-10)


### Features

* **util:** expose pretty stacktraces for notify ([7b84609](https://github.com/folke/lazy.nvim/commit/7b84609a06bd11869370bc20a9255bb469e35a50))

## [10.10.0](https://github.com/folke/lazy.nvim/compare/v10.9.1...v10.10.0) (2023-10-10)


### Features

* **git:** show error for local changes during check/update ([43e9165](https://github.com/folke/lazy.nvim/commit/43e9165994d76038bd6ebd2d06830a7204ae74e0))
* **git:** show help on how to remove local changes ([58e5726](https://github.com/folke/lazy.nvim/commit/58e5726592a3f4a83735edfea996911d8daea002))


### Bug Fixes

* **docs:** broken table in readme ([#1097](https://github.com/folke/lazy.nvim/issues/1097)) ([89581ce](https://github.com/folke/lazy.nvim/commit/89581ce37e1252133725cb583b5ba4fa0a827270))
* **git:** automatically restore doc/tags when modified ([736529d](https://github.com/folke/lazy.nvim/commit/736529d097979b3585cbc8e2728543fde9b314ed))
* **process:** make sure cwd is a valid directory ([92869d0](https://github.com/folke/lazy.nvim/commit/92869d0928ad3bb1aa61cf61897a78f3faa17835))

## [10.9.1](https://github.com/folke/lazy.nvim/compare/v10.9.0...v10.9.1) (2023-10-09)


### Bug Fixes

* **manage:** prevent auto conversion 'CRLF' to 'LF' in update lazy-lock.json on Windows. Fixes [#1093](https://github.com/folke/lazy.nvim/issues/1093) ([#1094](https://github.com/folke/lazy.nvim/issues/1094)) ([5579d72](https://github.com/folke/lazy.nvim/commit/5579d72576b21b9c8c2d01838598aece5dc2be6d))
* **profiling:** ensure proper traces in case of require errors ([2782f81](https://github.com/folke/lazy.nvim/commit/2782f8125e793940f5bf942af1a1df0bbc989d11))

## [10.9.0](https://github.com/folke/lazy.nvim/compare/v10.8.2...v10.9.0) (2023-10-09)


### Features

* **profiling:** added options to enable additional profiling ([423a152](https://github.com/folke/lazy.nvim/commit/423a152e94db37dd535d56e6cb6f06b282c5f081))


### Performance Improvements

* lazy require commands ([f0cfbf9](https://github.com/folke/lazy.nvim/commit/f0cfbf995238a42064e119bd1daa694fd1683ea3))

## [10.8.2](https://github.com/folke/lazy.nvim/compare/v10.8.1...v10.8.2) (2023-10-08)


### Bug Fixes

* **keys:** fixed adding managed keys ([9d92e65](https://github.com/folke/lazy.nvim/commit/9d92e65fd17d35f97bed43dc92810576a57376fc))

## [10.8.1](https://github.com/folke/lazy.nvim/compare/v10.8.0...v10.8.1) (2023-10-08)


### Bug Fixes

* **ui:** use correct keymap for display. Fixes [#1089](https://github.com/folke/lazy.nvim/issues/1089) ([26762c9](https://github.com/folke/lazy.nvim/commit/26762c97e6dc3fddf141db0e82d044ee73e5f78d))

## [10.8.0](https://github.com/folke/lazy.nvim/compare/v10.7.3...v10.8.0) (2023-10-08)


### Features

* **keys:** refactor code and allow disabling keymaps per mode. mode no longer needs to be exactly the same in order to disable. ([b79099c](https://github.com/folke/lazy.nvim/commit/b79099cc9d768241162bb45d284d6a243736b9fb))

## [10.7.3](https://github.com/folke/lazy.nvim/compare/v10.7.2...v10.7.3) (2023-10-07)


### Bug Fixes

* **keys:** fixed buffer-local mappings ([09e30f8](https://github.com/folke/lazy.nvim/commit/09e30f88cd4b47704005c41f0486a628b0b8d774))

## [10.7.2](https://github.com/folke/lazy.nvim/compare/v10.7.1...v10.7.2) (2023-10-07)


### Bug Fixes

* **event:** move all ft logic to the event handler ([8871602](https://github.com/folke/lazy.nvim/commit/8871602e541c9c7ecd036d631b527454312f88b2))
* **ft:** fix ft handlers to properly use new events. Fixes [#1084](https://github.com/folke/lazy.nvim/issues/1084) ([e4ea874](https://github.com/folke/lazy.nvim/commit/e4ea874e33fd3116d0e113f4b03eff2d6b1e3399))

## [10.7.1](https://github.com/folke/lazy.nvim/compare/v10.7.0...v10.7.1) (2023-10-06)


### Bug Fixes

* **event:** prevent loading event handler more than once in some cases ([6b37927](https://github.com/folke/lazy.nvim/commit/6b37927be9e0166ddb4445023904345d88045497))

## [10.7.0](https://github.com/folke/lazy.nvim/compare/v10.6.0...v10.7.0) (2023-10-06)


### Features

* **plugin:** added support for `cond` for imports ([#1079](https://github.com/folke/lazy.nvim/issues/1079)) ([58e954a](https://github.com/folke/lazy.nvim/commit/58e954a735767fd23c24c455dc09c5323951ec83))


### Bug Fixes

* **event:** better dealing with even handlers. Fixes [#788](https://github.com/folke/lazy.nvim/issues/788) ([ef2a5d0](https://github.com/folke/lazy.nvim/commit/ef2a5d0bd1a4995539b93be69fc760be7d9f62be))
* **event:** use tbl_contains instead of list_contains ([2b2adb9](https://github.com/folke/lazy.nvim/commit/2b2adb9d4d6ccd469b1e82416c58ea74fe5a0e1b))

## [10.6.0](https://github.com/folke/lazy.nvim/compare/v10.5.1...v10.6.0) (2023-10-05)


### Features

* **keys:** you can now create buffer-local filetype keymaps by specifying `ft=`. Fixes [#1076](https://github.com/folke/lazy.nvim/issues/1076) ([c42e63c](https://github.com/folke/lazy.nvim/commit/c42e63c1986af6ba417d9c2a0062ac41f79df18b))

## [10.5.1](https://github.com/folke/lazy.nvim/compare/v10.5.0...v10.5.1) (2023-10-04)


### Bug Fixes

* **plugin:** rebuild plugins after fixing optional and cond to ensure enabled will work correctly ([638c8e6](https://github.com/folke/lazy.nvim/commit/638c8e6382f121aef983c78d865f6dbbc72d68c3))

## [10.5.0](https://github.com/folke/lazy.nvim/compare/v10.4.1...v10.5.0) (2023-10-03)


### Features

* **plugin:** keep track of the module a spec fragment was defined in ([8eb8de2](https://github.com/folke/lazy.nvim/commit/8eb8de29af6e2ab9dd7986e2521178875dbcad95))


### Performance Improvements

* **util:** don't try to load nvim-treesitter when markdown parser is builtin ([8b73492](https://github.com/folke/lazy.nvim/commit/8b73492249100d8a9ce9d874f7ea5a71b4d6f07e))

## [10.4.1](https://github.com/folke/lazy.nvim/compare/v10.4.0...v10.4.1) (2023-09-30)


### Bug Fixes

* **plugin:** prevent recursive loop with cond=false. Fixes [#1061](https://github.com/folke/lazy.nvim/issues/1061) ([09e5010](https://github.com/folke/lazy.nvim/commit/09e5010741e340eb603afbff34453dbee55b7011))

## [10.4.0](https://github.com/folke/lazy.nvim/compare/v10.3.1...v10.4.0) (2023-09-29)


### Features

* **plugin:** dont include plugin spec fragments for disabled or optional plugins ([#1058](https://github.com/folke/lazy.nvim/issues/1058)) ([f3c7169](https://github.com/folke/lazy.nvim/commit/f3c7169dd65f5ae528b6c930492359971014290b))


### Bug Fixes

* **help:** sort readme tags case sensitive. Fixes [#67](https://github.com/folke/lazy.nvim/issues/67) ([54ecfc7](https://github.com/folke/lazy.nvim/commit/54ecfc7c245e5e3fbbc749658ad171335418d48c))
* **ui:** sort plugins case insensitive ([4f27fc3](https://github.com/folke/lazy.nvim/commit/4f27fc33c4e0e81802f4afadbe350de93447ac1e))

## [10.3.1](https://github.com/folke/lazy.nvim/compare/v10.3.0...v10.3.1) (2023-09-27)


### Bug Fixes

* properly setup handlers when loading a plugin before startup (build) etc ([24f6b6f](https://github.com/folke/lazy.nvim/commit/24f6b6f1c7fb68f02335dd9579faee8b243e6a54))
* return true when opening diff ([#970](https://github.com/folke/lazy.nvim/issues/970)) ([0e1d264](https://github.com/folke/lazy.nvim/commit/0e1d264ab6567725b6c30ffd1ad120b16884ff45))

## [10.3.0](https://github.com/folke/lazy.nvim/compare/v10.2.1...v10.3.0) (2023-07-22)


### Features

* **plugins:** Given an optional plugin, conditionally discard deps ([#947](https://github.com/folke/lazy.nvim/issues/947)) ([e7334d8](https://github.com/folke/lazy.nvim/commit/e7334d8db5bab48463f8ab3ea020bf2f76aaa7f9))

## [10.2.1](https://github.com/folke/lazy.nvim/compare/v10.2.0...v10.2.1) (2023-07-22)


### Bug Fixes

* **loader:** getscriptinfo compat with stable. Fixes [#944](https://github.com/folke/lazy.nvim/issues/944) ([e428c5e](https://github.com/folke/lazy.nvim/commit/e428c5ee4b02dfb39203ac8745a58c1226ceebae))

## [10.2.0](https://github.com/folke/lazy.nvim/compare/v10.1.0...v10.2.0) (2023-07-20)


### Features

* **view:** add option `ui.pills`. Set to `false` to disable the top buttons in the lazy window ([#938](https://github.com/folke/lazy.nvim/issues/938)) ([84266b9](https://github.com/folke/lazy.nvim/commit/84266b9f0ff314319e69adfeb1a86bd72d1aff91))

## [10.1.0](https://github.com/folke/lazy.nvim/compare/v10.0.2...v10.1.0) (2023-07-12)


### Features

* **loader:** `LazyLoad` event with plugin name as `data` field. Useful to do stuff when a plugin loads ([ea5b2e0](https://github.com/folke/lazy.nvim/commit/ea5b2e00bf7aeaaf10a4e93763419e4af2796782))

## [10.0.2](https://github.com/folke/lazy.nvim/compare/v10.0.1...v10.0.2) (2023-07-09)


### Bug Fixes

* **event:** pass data to event lazy loaders. Fixes [#922](https://github.com/folke/lazy.nvim/issues/922) ([fd94e69](https://github.com/folke/lazy.nvim/commit/fd94e69ceb15268496b85ee61fcd55a08539df1d))

## [10.0.1](https://github.com/folke/lazy.nvim/compare/v10.0.0...v10.0.1) (2023-07-06)


### Bug Fixes

* **stats:** corrected typo in cputime() for Linux ([#916](https://github.com/folke/lazy.nvim/issues/916)) ([5082cd5](https://github.com/folke/lazy.nvim/commit/5082cd56e49c737619c967e9c57309c2eeaad425))

## [10.0.0](https://github.com/folke/lazy.nvim/compare/v9.25.1...v10.0.0) (2023-07-06)


### ⚠ BREAKING CHANGES

* **plugin:** `cond` is now the same as `enabled`, but skips clean

### Features

* **plugin:** `cond` is now the same as `enabled`, but skips clean ([fbb0bea](https://github.com/folke/lazy.nvim/commit/fbb0bea2db1963b4b83a3cb1f0c09d78a2ab286f))

## [9.25.1](https://github.com/folke/lazy.nvim/compare/v9.25.0...v9.25.1) (2023-06-30)


### Bug Fixes

* **build:** allow `build` command to override plugin's build and option to disable warning ([189371c](https://github.com/folke/lazy.nvim/commit/189371c8d8ac8205687522dd4c3601edc7b7a927))

## [9.25.0](https://github.com/folke/lazy.nvim/compare/v9.24.2...v9.25.0) (2023-06-30)


### Features

* **build:** added support for build.lua, build/init.lua ([#903](https://github.com/folke/lazy.nvim/issues/903)) ([4c26421](https://github.com/folke/lazy.nvim/commit/4c26421785be8c49f1d8eaa5bdb55b73c7be5127))


### Bug Fixes

* **health:** false warning when checking plugins configured with 'optional' key ([#897](https://github.com/folke/lazy.nvim/issues/897)) ([24803fc](https://github.com/folke/lazy.nvim/commit/24803fcbe3fe2c84300903278b7445cfb2e54deb))

## [9.24.2](https://github.com/folke/lazy.nvim/compare/v9.24.1...v9.24.2) (2023-06-22)


### Bug Fixes

* **config:** on windows default concurrency is now set to 2*available parallelism. See [#887](https://github.com/folke/lazy.nvim/issues/887) ([d7d5842](https://github.com/folke/lazy.nvim/commit/d7d5842d1c9a566d480db8b4a5aaf00054b99bb5))

## [9.24.1](https://github.com/folke/lazy.nvim/compare/v9.24.0...v9.24.1) (2023-06-19)


### Bug Fixes

* **debug:** show original keymaps instead of ids for the keys handler ([56b1f77](https://github.com/folke/lazy.nvim/commit/56b1f7715ed536a3e9ebfbf0d26e615d211a0cd8))
* **manage:** trigger LazySyncPre. Fixes [#881](https://github.com/folke/lazy.nvim/issues/881) ([6163413](https://github.com/folke/lazy.nvim/commit/616341372d1908bb2a11e3bf9ed55e74bf605e40))
* **ui:** trailing space in button row. Fixes [#884](https://github.com/folke/lazy.nvim/issues/884) ([410a736](https://github.com/folke/lazy.nvim/commit/410a7360c1b8df2053ae7ba906ff74c9072e1505))

## [9.24.0](https://github.com/folke/lazy.nvim/compare/v9.23.0...v9.24.0) (2023-06-17)


### Features

* added `Pre` events. Fixes [#856](https://github.com/folke/lazy.nvim/issues/856). Fixes [#877](https://github.com/folke/lazy.nvim/issues/877) ([0bca18d](https://github.com/folke/lazy.nvim/commit/0bca18de5d005c700c29da580c20c762c2f9e9e0))


### Bug Fixes

* **ui:** set wo options with local. don't use `vim.wo`. See [#829](https://github.com/folke/lazy.nvim/issues/829) ([7f4da7d](https://github.com/folke/lazy.nvim/commit/7f4da7d511b05f4571ea96c67a5988b6389e12e1))

## [9.23.0](https://github.com/folke/lazy.nvim/compare/v9.22.2...v9.23.0) (2023-06-08)


### Features

* **startup:** added data/site to the rtp. Will be used by upcoming treesitter version ([f131606](https://github.com/folke/lazy.nvim/commit/f131606190535b0d0b35406e8573b973b48e55b1))


### Bug Fixes

* **event:** dont use autocmd pattern to detect event retriggering. Fixes [#858](https://github.com/folke/lazy.nvim/issues/858) ([bc89502](https://github.com/folke/lazy.nvim/commit/bc895023573e76f8567d2375bbd3ea8be4f00ca7))

## [9.22.2](https://github.com/folke/lazy.nvim/compare/v9.22.1...v9.22.2) (2023-06-03)


### Bug Fixes

* **ui:** setup colors when loading a float ([dbb2b60](https://github.com/folke/lazy.nvim/commit/dbb2b609f66486251b51c79a7a1d275887413e8e))

## [9.22.1](https://github.com/folke/lazy.nvim/compare/v9.22.0...v9.22.1) (2023-06-03)


### Bug Fixes

* **keys:** replace term codes to calculate ids ([d65a3d6](https://github.com/folke/lazy.nvim/commit/d65a3d6755bd3f1ca7bc4c15a8acf57687b1ca51))

## [9.22.0](https://github.com/folke/lazy.nvim/compare/v9.21.1...v9.22.0) (2023-06-03)


### Features

* **float:** floats can now be persistent ([94472b8](https://github.com/folke/lazy.nvim/commit/94472b8303f4db496ff1214a73aa8f600e375974))

## [9.21.1](https://github.com/folke/lazy.nvim/compare/v9.21.0...v9.21.1) (2023-05-28)


### Bug Fixes

* **loader:** don't run ftdetect twice for paths already on the rtp during startup. Fixes [#839](https://github.com/folke/lazy.nvim/issues/839) ([36a9132](https://github.com/folke/lazy.nvim/commit/36a91320f9ff4f877f09ac3a52c6a26860da047a))

## [9.21.0](https://github.com/folke/lazy.nvim/compare/v9.20.0...v9.21.0) (2023-05-27)


### Features

* **commands:** added highly experimental `Lazy reload ...` command. See [#445](https://github.com/folke/lazy.nvim/issues/445) ([a6c8f22](https://github.com/folke/lazy.nvim/commit/a6c8f22362dccf5416ccb108f201e9f1ddda43f1))
* **loader:** when reloading, always re-source loaded vimscript files. See [#445](https://github.com/folke/lazy.nvim/issues/445) ([d8a5829](https://github.com/folke/lazy.nvim/commit/d8a5829fdad1d435fd74d65743df5d53d4a845d2))


### Bug Fixes

* **ui:** make progress bar work again ([efa02ff](https://github.com/folke/lazy.nvim/commit/efa02ff8d37fe5809ea7826f11730a59d25533ef))

## [9.20.0](https://github.com/folke/lazy.nvim/compare/v9.19.1...v9.20.0) (2023-05-27)


### Features

* **ui:** added support for setting a title of the lazy window. Fixes [#814](https://github.com/folke/lazy.nvim/issues/814) ([9dce081](https://github.com/folke/lazy.nvim/commit/9dce0816f15f478c864c65fce0cd55f145faad03))

## [9.19.1](https://github.com/folke/lazy.nvim/compare/v9.19.0...v9.19.1) (2023-05-27)


### Bug Fixes

* **plugin:** delay check if plugin ref exists until after loading all plugins. Fixes [#833](https://github.com/folke/lazy.nvim/issues/833) ([199e100](https://github.com/folke/lazy.nvim/commit/199e1004647895d5cb87911ae65e4f01418abf3b))
* **plugin:** fixup. It's fine that Plugin.url doesn't exist ([42ff600](https://github.com/folke/lazy.nvim/commit/42ff6009f67a712ab4e7c8deedb626f8243a052a))

## [9.19.0](https://github.com/folke/lazy.nvim/compare/v9.18.2...v9.19.0) (2023-05-25)


### Features

* **git:** change default log args to last 8 ([49a7f21](https://github.com/folke/lazy.nvim/commit/49a7f21ee37b4f8a13f6774b17ddfcae5e4f41b0))
* **plugin:** trigger LazyPlugins after loading plugin specs ([57062f3](https://github.com/folke/lazy.nvim/commit/57062f3a09cad6dd5fe745389ad9f8421e3bdcd2))


### Bug Fixes

* **plugin:** check that import is a string. See [#825](https://github.com/folke/lazy.nvim/issues/825) ([c325c50](https://github.com/folke/lazy.nvim/commit/c325c50ba42572b25c08330ea10ae4743ee69280))
* **plugin:** fix url based plugin name and added extra safety checks. Fixes [#824](https://github.com/folke/lazy.nvim/issues/824) ([32170a8](https://github.com/folke/lazy.nvim/commit/32170a88916e0f18ffaf1c32b222a5e2216bdb0e))

## [9.18.2](https://github.com/folke/lazy.nvim/compare/v9.18.1...v9.18.2) (2023-05-23)


### Bug Fixes

* **commands:** completion error ([#819](https://github.com/folke/lazy.nvim/issues/819)) ([f125a7d](https://github.com/folke/lazy.nvim/commit/f125a7d333472ada244b4564805ba11be3c269a9))

## [9.18.1](https://github.com/folke/lazy.nvim/compare/v9.18.0...v9.18.1) (2023-05-22)


### Bug Fixes

* **plugin:** rename weak =&gt; optional. Makes more sense :) ([9177778](https://github.com/folke/lazy.nvim/commit/9177778891ecdf02562eeaa1a26b829e4b62bc16))

## [9.18.0](https://github.com/folke/lazy.nvim/compare/v9.17.0...v9.18.0) (2023-05-22)


### Features

* **plugin:** added support for `weak` specs. They will not be included in the final spec if not specified somewhere else ([8564f6d](https://github.com/folke/lazy.nvim/commit/8564f6d22b78a4a0fba9811faa556159b6c90a49))


### Bug Fixes

* better weak handling ([af39d61](https://github.com/folke/lazy.nvim/commit/af39d61d3f32683b6e9962d64ab269330b456172))
* **ui:** close ui when opening a help file. Fixes [#808](https://github.com/folke/lazy.nvim/issues/808) ([cc7a764](https://github.com/folke/lazy.nvim/commit/cc7a764aecec11c9598ccd442a6879eed4e85558))
* **ui:** take border into account for window position. Fixes [#812](https://github.com/folke/lazy.nvim/issues/812) ([451f217](https://github.com/folke/lazy.nvim/commit/451f217e9b2d71f08bdae0ce5ac7e8e8a6503f48))

## [9.17.0](https://github.com/folke/lazy.nvim/compare/v9.16.1...v9.17.0) (2023-05-18)


### Features

* **cmd:** added `Lazy load all` to load all plugins ([11131ea](https://github.com/folke/lazy.nvim/commit/11131eafa165e54b08aeff3d7e35c65ef8b6e034))

## [9.16.1](https://github.com/folke/lazy.nvim/compare/v9.16.0...v9.16.1) (2023-05-17)


### Bug Fixes

* **loader:** dont clear tasks when installing missing plugins ([80c4dec](https://github.com/folke/lazy.nvim/commit/80c4decc3226551b433dfea5e459998a96f17822))
* **loader:** reset cache before installing plugins during startup. Fixes [#803](https://github.com/folke/lazy.nvim/issues/803) ([aecdaab](https://github.com/folke/lazy.nvim/commit/aecdaab6a6ce8c9fdf9f983d5f943c6cfb11bf61))

## [9.16.0](https://github.com/folke/lazy.nvim/compare/v9.15.0...v9.16.0) (2023-05-13)


### Features

* **loader:** added explicit support for finding the main module for mini.nvim plugins ([dab6cd5](https://github.com/folke/lazy.nvim/commit/dab6cd50806d6a6b0e8267f628d5fd6b112b151c))

## [9.15.0](https://github.com/folke/lazy.nvim/compare/v9.14.11...v9.15.0) (2023-05-13)


### Features

* **ui:** show the loaded icon for local plugins in a different color ([96dd205](https://github.com/folke/lazy.nvim/commit/96dd2058fb5427d87589825ad6001ad017548e81))


### Bug Fixes

* **config:** use url_format for the lazy plugin ([#792](https://github.com/folke/lazy.nvim/issues/792)) ([d2d67b5](https://github.com/folke/lazy.nvim/commit/d2d67b5a0ba90a33eeae0a1a661249b26754143b))

## [9.14.11](https://github.com/folke/lazy.nvim/compare/v9.14.10...v9.14.11) (2023-05-05)


### Bug Fixes

* **ui:** don' render extmarks for empty lines ([dbe0e29](https://github.com/folke/lazy.nvim/commit/dbe0e29d85e2769be6c9738c176ba6d8b0c6817a))

## [9.14.10](https://github.com/folke/lazy.nvim/compare/v9.14.9...v9.14.10) (2023-05-02)


### Bug Fixes

* **ui:** issue with rendering empty lines. Fixes [#770](https://github.com/folke/lazy.nvim/issues/770) ([98ba47e](https://github.com/folke/lazy.nvim/commit/98ba47efedc4a29d2258fe80434d87bf5f72baa2))

## [9.14.9](https://github.com/folke/lazy.nvim/compare/v9.14.8...v9.14.9) (2023-05-02)


### Bug Fixes

* **ui:** don't pad empty lines ([#768](https://github.com/folke/lazy.nvim/issues/768)) ([b00d6f7](https://github.com/folke/lazy.nvim/commit/b00d6f7102a3345704edb46cbabf2dfa21d78d24))

## [9.14.8](https://github.com/folke/lazy.nvim/compare/v9.14.7...v9.14.8) (2023-04-27)


### Bug Fixes

* **health:** show error if setup didn't run ([0c7b418](https://github.com/folke/lazy.nvim/commit/0c7b41872ed20f12b45c41cadbccbf74554ac68e))

## [9.14.7](https://github.com/folke/lazy.nvim/compare/v9.14.6...v9.14.7) (2023-04-24)


### Bug Fixes

* **build:** make sure to properly load handlers for plugins that were built during startup. Fixes [#744](https://github.com/folke/lazy.nvim/issues/744) ([a758588](https://github.com/folke/lazy.nvim/commit/a7585880081a8ae3dfbecfced960dcfdc124c361))

## [9.14.6](https://github.com/folke/lazy.nvim/compare/v9.14.5...v9.14.6) (2023-04-23)


### Bug Fixes

* **util:** use vim.o.shell by default ([0cbf466](https://github.com/folke/lazy.nvim/commit/0cbf4669138961c27566de684a0df95c01cd35ad))

## [9.14.5](https://github.com/folke/lazy.nvim/compare/v9.14.4...v9.14.5) (2023-04-19)


### Bug Fixes

* **loader:** keep using the internal lua cache till 0.9.1 ([78b981b](https://github.com/folke/lazy.nvim/commit/78b981b1f33c50ebc51262694bf99e32cc3012b4))

## [9.14.4](https://github.com/folke/lazy.nvim/compare/v9.14.3...v9.14.4) (2023-04-18)


### Bug Fixes

* **cmd:** show descriptive error when command was not found after loading its plugins ([b582fc5](https://github.com/folke/lazy.nvim/commit/b582fc554582c755c221fdcbb7dce648e971cd88))

## [9.14.3](https://github.com/folke/lazy.nvim/compare/v9.14.2...v9.14.3) (2023-04-16)


### Bug Fixes

* **checkhealth:** use non-deprecated versions if possible ([#729](https://github.com/folke/lazy.nvim/issues/729)) ([c8cad54](https://github.com/folke/lazy.nvim/commit/c8cad548950807848de11e3710de2b560758ecb4))
* **render:** show message if not yet committed ([#707](https://github.com/folke/lazy.nvim/issues/707)) ([b7a1a0f](https://github.com/folke/lazy.nvim/commit/b7a1a0fbaf1bd0f394783951f16d4c9f8c9dc210))

## [9.14.2](https://github.com/folke/lazy.nvim/compare/v9.14.1...v9.14.2) (2023-03-25)


### Bug Fixes

* **keys:** dont add (n) to keys id ([9f9d733](https://github.com/folke/lazy.nvim/commit/9f9d733df9644106c258709e1c910d4034bf06ce))

## [9.14.1](https://github.com/folke/lazy.nvim/compare/v9.14.0...v9.14.1) (2023-03-24)


### Bug Fixes

* **cache:** handle corrupted cache files ([db5b67e](https://github.com/folke/lazy.nvim/commit/db5b67e75c31c955e3df9a3d6781f397b9dc66e8))

## [9.14.0](https://github.com/folke/lazy.nvim/compare/v9.13.1...v9.14.0) (2023-03-22)


### Features

* **ui:** added test to dimmed commits ([0e230ca](https://github.com/folke/lazy.nvim/commit/0e230caab9466ae352e9aaa6a4327ebd3e72302a))


### Bug Fixes

* **ui:** show full reason for Not-Loaded ([#683](https://github.com/folke/lazy.nvim/issues/683)) ([261c2d6](https://github.com/folke/lazy.nvim/commit/261c2d6f95f1e71480c0a573275bbe4fb2c705a2))

## [9.13.1](https://github.com/folke/lazy.nvim/compare/v9.13.0...v9.13.1) (2023-03-20)


### Bug Fixes

* **cache:** fix loading libs on Darwin ([236f851](https://github.com/folke/lazy.nvim/commit/236f8517bae70516a3f89fe154e3e18294eb862a))
* **health:** add `main` key ([#679](https://github.com/folke/lazy.nvim/issues/679)) ([e7622b7](https://github.com/folke/lazy.nvim/commit/e7622b78f6addaeb93debf43041235c16fc74a57))
* **health:** allow overriding `1` ([959f8c3](https://github.com/folke/lazy.nvim/commit/959f8c36bc1744db2745b18135f2fb822b382cfb))

## [9.13.0](https://github.com/folke/lazy.nvim/compare/v9.12.1...v9.13.0) (2023-03-17)


### Features

* **help:** allow disabling README magic ([#663](https://github.com/folke/lazy.nvim/issues/663)) ([e5759d2](https://github.com/folke/lazy.nvim/commit/e5759d202afe80aeb192e7eb02d28b74cc2d66eb))

## [9.12.1](https://github.com/folke/lazy.nvim/compare/v9.12.0...v9.12.1) (2023-03-16)


### Bug Fixes

* **cmd:** properly deal with commands with nargs=? or nargs=1. Fixes [#659](https://github.com/folke/lazy.nvim/issues/659) ([efe36bd](https://github.com/folke/lazy.nvim/commit/efe36bdfda47256dbc223945a7f35eea52b1d736))

## [9.12.0](https://github.com/folke/lazy.nvim/compare/v9.11.0...v9.12.0) (2023-03-15)


### Features

* **cache:** automatically reset topmods when a user changes a file for a path on the rtp ([5b7b8c5](https://github.com/folke/lazy.nvim/commit/5b7b8c51495de8ced973cc23f0a58cadd21de875))
* **cache:** drop dependency on ffi ([810acc1](https://github.com/folke/lazy.nvim/commit/810acc1e86180403308e1cf650ed9fb0c5d27a44))
* **cache:** remove any mentions of lazy. Move the cache to cache/luac instead of cache/lazy/luac ([49dda87](https://github.com/folke/lazy.nvim/commit/49dda8751e99aae2ae7073c6374bc1b8c38d0649))
* **cache:** use `vim.cache` everywhere. poly-fill when needed ([ea1a044](https://github.com/folke/lazy.nvim/commit/ea1a044e3c819693565e0d73994587023b8e5e90))


### Bug Fixes

* **cache:** remove dependency on jit ([942c805](https://github.com/folke/lazy.nvim/commit/942c805b8427e3b4b9586e27702eeceacf967549))

## [9.11.0](https://github.com/folke/lazy.nvim/compare/v9.10.3...v9.11.0) (2023-03-14)


### Features

* **plugin:** added config.defaults.cond. Fixes [#640](https://github.com/folke/lazy.nvim/issues/640) ([9afba38](https://github.com/folke/lazy.nvim/commit/9afba388facee5ce45d244c0e10ce650d42d9495))


### Bug Fixes

* **loader:** never load lua files from a plugin where cond=false. Show error instead ([10f5844](https://github.com/folke/lazy.nvim/commit/10f5844abf30eb9b180efece36639b6eecb33e86))

## [9.10.3](https://github.com/folke/lazy.nvim/compare/v9.10.2...v9.10.3) (2023-03-13)


### Bug Fixes

* **cache:** path ([#645](https://github.com/folke/lazy.nvim/issues/645)) ([8d73b9b](https://github.com/folke/lazy.nvim/commit/8d73b9bccd1fef7a7d3f5cc990c79b2dafcd9a3a))

## [9.10.2](https://github.com/folke/lazy.nvim/compare/v9.10.1...v9.10.2) (2023-03-07)


### Bug Fixes

* **git:** always set origin name when cloning ([#622](https://github.com/folke/lazy.nvim/issues/622)) ([53be2c0](https://github.com/folke/lazy.nvim/commit/53be2c0ee1848fee2a47b89d184ad02410d3c319))
* **plugin:** properly pass is_list for recursively merging props ([355312e](https://github.com/folke/lazy.nvim/commit/355312eb514b58b79e93753d46b2612a21949aa4))

## [9.10.1](https://github.com/folke/lazy.nvim/compare/v9.10.0...v9.10.1) (2023-03-04)


### Bug Fixes

* **process:** unset GIT_WORK_TREE ([c60f7ea](https://github.com/folke/lazy.nvim/commit/c60f7ea985c488192a38bb3ddf7705f958bd3674))

## [9.10.0](https://github.com/folke/lazy.nvim/compare/v9.9.0...v9.10.0) (2023-03-02)


### Features

* **render:** dim housekeeping commits by default ([#612](https://github.com/folke/lazy.nvim/issues/612)) ([1f7ffec](https://github.com/folke/lazy.nvim/commit/1f7ffec177656ac806706097d23f288e3a5e0b51))

## [9.9.0](https://github.com/folke/lazy.nvim/compare/v9.8.5...v9.9.0) (2023-02-28)


### Features

* **health:** check for paths on the rtp from plugged or packer ([9bd1c94](https://github.com/folke/lazy.nvim/commit/9bd1c946d6114affebb57dbe3e33741ded566559))


### Bug Fixes

* **cache:** add hack to work-around incorrect requires back. Not a fan of this. Fixes [#603](https://github.com/folke/lazy.nvim/issues/603) ([79f85e5](https://github.com/folke/lazy.nvim/commit/79f85e5fed3ea020b09720e273c8b626f699b19a))
* **git:** honor clone.defaultRemoteName. Fixes [#602](https://github.com/folke/lazy.nvim/issues/602) ([5af9380](https://github.com/folke/lazy.nvim/commit/5af93806aaa33fd9e8b4a7a32e9f847a3ad64c2a))
* **git:** properly deal with failed clones. Fixes [#571](https://github.com/folke/lazy.nvim/issues/571) ([7722378](https://github.com/folke/lazy.nvim/commit/77223786aaa91446649d0dbdc3eabc2e53f9de6d))
* **health:** whitelist deactivate prop ([5694483](https://github.com/folke/lazy.nvim/commit/5694483e8782f4d9a01ea8822166998924df5f00))
* **keys:** set nowait for lazy keymaps when needed. Fixes [#600](https://github.com/folke/lazy.nvim/issues/600) ([1657ae9](https://github.com/folke/lazy.nvim/commit/1657ae9b8c86d672517ac7f573eb180d3f5ecb79))
* **ui:** always show diagnostics virtual text ([0f713b2](https://github.com/folke/lazy.nvim/commit/0f713b2958b8a2e624fa0e2615418bd6c8fb8e10))

## [9.8.5](https://github.com/folke/lazy.nvim/compare/v9.8.4...v9.8.5) (2023-02-20)


### Bug Fixes

* **ui:** disable colorcolumn on floating window ([#575](https://github.com/folke/lazy.nvim/issues/575)) ([43496fa](https://github.com/folke/lazy.nvim/commit/43496fa82cd4d68523754c3492660a9883e747d9))
* **ui:** don't close on BufLeave. Fixes [#561](https://github.com/folke/lazy.nvim/issues/561) ([7339145](https://github.com/folke/lazy.nvim/commit/7339145a223dab7e7ddccf0986ffbf9d2cb804e8))

## [9.8.4](https://github.com/folke/lazy.nvim/compare/v9.8.3...v9.8.4) (2023-02-17)


### Bug Fixes

* **spec:** make sure imported specs are sorted alphabetically ([ff76e58](https://github.com/folke/lazy.nvim/commit/ff76e58961509038e3e0365c47580e595977a3a2))
* **ui:** return abort key instead of `&lt;c-c&gt;` ([5cfe156](https://github.com/folke/lazy.nvim/commit/5cfe1560c551720bdc125e68431bacb836eb28d3))

## [9.8.3](https://github.com/folke/lazy.nvim/compare/v9.8.2...v9.8.3) (2023-02-16)


### Bug Fixes

* **cache:** hack to work around plugins trying to load relatve modules. Fixes [#543](https://github.com/folke/lazy.nvim/issues/543) ([e916f41](https://github.com/folke/lazy.nvim/commit/e916f41df26e33b01f1b3ebe28881090da3a7281))
* **ui:** disable folding of floating window ([#550](https://github.com/folke/lazy.nvim/issues/550)) ([6771c7e](https://github.com/folke/lazy.nvim/commit/6771c7e23c3ecdb50a9510c4cd5e1e0d2db9e5ca))

## [9.8.2](https://github.com/folke/lazy.nvim/compare/v9.8.1...v9.8.2) (2023-02-15)


### Bug Fixes

* **cache:** lsmod now also supports lua libs. Fixes [#544](https://github.com/folke/lazy.nvim/issues/544) ([9ca3222](https://github.com/folke/lazy.nvim/commit/9ca3222061fcc07a7ac5f685d80b49944b347a03))

## [9.8.1](https://github.com/folke/lazy.nvim/compare/v9.8.0...v9.8.1) (2023-02-14)


### Bug Fixes

* **keys:** fixed keys types. rhs can be `false` ([6a18404](https://github.com/folke/lazy.nvim/commit/6a18404b7d1c05f0d1f35f7b78bd5c282dff7a89))


### Performance Improvements

* more cache optims ([17a3c3a](https://github.com/folke/lazy.nvim/commit/17a3c3acea400679027e675cc19b738e842a5ea0))
* use modkey instead of modpath ([b1f7ae6](https://github.com/folke/lazy.nvim/commit/b1f7ae68a75401152eb23edbd5827b69761e9bc7))

## [9.8.0](https://github.com/folke/lazy.nvim/compare/v9.7.0...v9.8.0) (2023-02-13)


### Features

* **git:** `Plugin.submodules = false` will now skip fetching git submodules ([0d3f2c4](https://github.com/folke/lazy.nvim/commit/0d3f2c40421f4774c70f631d7b7023f57cba66cd))


### Bug Fixes

* **cmd:** fix Error when trigger on range defined command that doesn't support count  ([#519](https://github.com/folke/lazy.nvim/issues/519)) ([a147110](https://github.com/folke/lazy.nvim/commit/a1471103902a9836d88732eeeeabd11d00a2cb3e))
* **icons:** replace an obsolete Nerd icon ([#529](https://github.com/folke/lazy.nvim/issues/529)) ([bc978ca](https://github.com/folke/lazy.nvim/commit/bc978ca9be96b75330336a0427771addaa1ccd50))
* **loader:** don't deactivate when not loaded ([c83d2ae](https://github.com/folke/lazy.nvim/commit/c83d2aeb27fce9cf9f14e779e77a85c63fc3d2c9))
* **util:** executable checks for `Util.open` ([#528](https://github.com/folke/lazy.nvim/issues/528)) ([4917222](https://github.com/folke/lazy.nvim/commit/4917222c7e5c924bf7471b72a5e2d3e661530b40))


### Performance Improvements

* new file-based cache that ensures correct rtp order ([#532](https://github.com/folke/lazy.nvim/issues/532)) ([462633b](https://github.com/folke/lazy.nvim/commit/462633bae11255133f099163dda17180b3a6dc27))

## [9.7.0](https://github.com/folke/lazy.nvim/compare/v9.6.0...v9.7.0) (2023-02-08)


### Features

* deactivate WIP ([57a3960](https://github.com/folke/lazy.nvim/commit/57a3960fafc210f240a07439d1adfaba09d6ff59))
* use "wslview" instead of "xsl-open" if it exists ([#509](https://github.com/folke/lazy.nvim/issues/509)) ([2451ea4](https://github.com/folke/lazy.nvim/commit/2451ea4e655bc60ef639ad284e69c6fca15da352))


### Bug Fixes

* **install:** dont load the colorscheme again if a `config()` of the colorscheme also loads it. Fixes [#488](https://github.com/folke/lazy.nvim/issues/488) ([49b43de](https://github.com/folke/lazy.nvim/commit/49b43def14f7e130cc27c7041ca2942142a881ed))
* **keys:** feed keys instead of returning expr for Neovim 0.8.x. Fixes [#511](https://github.com/folke/lazy.nvim/issues/511) ([c734d94](https://github.com/folke/lazy.nvim/commit/c734d941b47312baafe3e0429a5fecd25da95f5f))
* **keys:** refactor retrigger mechanism ([#428](https://github.com/folke/lazy.nvim/issues/428)) ([4272d21](https://github.com/folke/lazy.nvim/commit/4272d2100af2384f4b8aba08aef4a7b9a296bce6))
* **keys:** replace keycodes manually ([ddaffa0](https://github.com/folke/lazy.nvim/commit/ddaffa07156a090383bd32ef88669eea1b22c11a))

## [9.6.0](https://github.com/folke/lazy.nvim/compare/v9.5.1...v9.6.0) (2023-02-07)


### Features

* **cmd:** use cmd table instead of trying to create the cmd string. Fixes [#472](https://github.com/folke/lazy.nvim/issues/472) ([3c29f19](https://github.com/folke/lazy.nvim/commit/3c29f196f4b0f083f2b94c3337599a189f4eef84))

## [9.5.1](https://github.com/folke/lazy.nvim/compare/v9.5.0...v9.5.1) (2023-02-06)


### Bug Fixes

* **commands:** sync with plugins list should not delete those plugins. Fixes [#475](https://github.com/folke/lazy.nvim/issues/475) ([0c98031](https://github.com/folke/lazy.nvim/commit/0c980312fd6bce744db499acfa5af47871287151))
* **health:** existing packages on windows. Fixes [#474](https://github.com/folke/lazy.nvim/issues/474) ([527f83c](https://github.com/folke/lazy.nvim/commit/527f83cae50b99d16327447eb813b4f73e09ec0d))
* **log:** properly check if plugin dir is a git repo before running git log ([3d2dcb2](https://github.com/folke/lazy.nvim/commit/3d2dcb2d5ef99106c5ff412da88c6f59a9f8a693))
* **process:** allow overriding GIT_SSH_COMMAND. Fixes [#491](https://github.com/folke/lazy.nvim/issues/491). Fixes [#492](https://github.com/folke/lazy.nvim/issues/492) ([452d4eb](https://github.com/folke/lazy.nvim/commit/452d4eb719c5067f0bae497dc870554cd300758f))

## [9.5.0](https://github.com/folke/lazy.nvim/compare/v9.4.0...v9.5.0) (2023-01-24)


### Features

* **config:** added option to disable git filter. NOT recommended. Fixes [#442](https://github.com/folke/lazy.nvim/issues/442) ([26a67e3](https://github.com/folke/lazy.nvim/commit/26a67e3c48951ca3ce47d208c3216143749b0768))
* **dev:** optionally fallback to git when local plugin doesn't exist ([#446](https://github.com/folke/lazy.nvim/issues/446)) ([772d888](https://github.com/folke/lazy.nvim/commit/772d8888cc6f8e4371c31001197431b24311af48))
* **health:** check for git in health checks ([9b5cc1b](https://github.com/folke/lazy.nvim/commit/9b5cc1bf53f344c8ad829f33c3ac77f5e3ea8da1))
* **util:** utility method to walk over all modules in a directory ([5d9d354](https://github.com/folke/lazy.nvim/commit/5d9d35404f39de5d7c9365cbc2aa39858929cbfc))


### Bug Fixes

* **checker:** dont check for updates when there's tasks with errors ([c32a618](https://github.com/folke/lazy.nvim/commit/c32a6185ace7cb04572db1637a3010b729a7601e))
* **checker:** dont clear tasks when running update check ([ed21070](https://github.com/folke/lazy.nvim/commit/ed210702f5dc8c24ec6531c0f2484881d9ebe6b6))

## [9.4.0](https://github.com/folke/lazy.nvim/compare/v9.3.1...v9.4.0) (2023-01-22)


### Features

* added `config.ui.wrap` and improved wrapping when wrap=true. Fixes [#422](https://github.com/folke/lazy.nvim/issues/422) ([d6fc848](https://github.com/folke/lazy.nvim/commit/d6fc848067d603800b9e63a7b22b7e5853c6bd7a))
* **checker:** checker will now save last check time and only check at configured frequency even after restarting Neovim ([813fc94](https://github.com/folke/lazy.nvim/commit/813fc944d797fe1b43abe12866a9ef7af403c35c))


### Bug Fixes

* **checker:** make sure we show logs when only doing a fast check ([4008b57](https://github.com/folke/lazy.nvim/commit/4008b57d882065814ce27a0f32609d5ea437a6e9))
* **git:** unset GIT_DIR when spawning a process. Fixes [#434](https://github.com/folke/lazy.nvim/issues/434) ([9858001](https://github.com/folke/lazy.nvim/commit/9858001c3cdb5713e8d1aeb0f47c23038084fd7c))
* **render:** get profile_{sort,filter} key bindings from ViewConfig ([#416](https://github.com/folke/lazy.nvim/issues/416)) ([27ca918](https://github.com/folke/lazy.nvim/commit/27ca918bc3d02ea20b3fd901c8919e9925555444))
* **spec:** dont complain about an invalid short url, when a full url is set. Fixes [#421](https://github.com/folke/lazy.nvim/issues/421) ([c389ad5](https://github.com/folke/lazy.nvim/commit/c389ad552bd5c2050783ac6cd6e54f5fbba3c7bc))

## [9.3.1](https://github.com/folke/lazy.nvim/compare/v9.3.0...v9.3.1) (2023-01-17)


### Bug Fixes

* **git:** when a `Plugin.branch` is set, don't use `config.defaults.version`. Fixes [#409](https://github.com/folke/lazy.nvim/issues/409) ([bd37afc](https://github.com/folke/lazy.nvim/commit/bd37afc96e4d64a41744298f24772dddb5286fd5))
* **spec:** dont copy dep and super state from existing plugins ([da4e8cc](https://github.com/folke/lazy.nvim/commit/da4e8cc2450ec428d370032b5b3790b01889c4a4))
* **spec:** when overriding a spec by name that has not been imported yet, show an error when needed ([baaf8dd](https://github.com/folke/lazy.nvim/commit/baaf8ddfff6cf0c2b8729c2b76b2b140cb40d382))
* work-around for libuv issue where fs_scandir_next sometimes fails to return a file type ([c791c0e](https://github.com/folke/lazy.nvim/commit/c791c0ed7d7bbcdc06a58b79eb4625682c60964c))


### Performance Improvements

* **plugin:** de-duplicate dependencies, keys, ft, event and cmd ([1b2a6f6](https://github.com/folke/lazy.nvim/commit/1b2a6f631c9b2ef98005acec8369c7298fe7a751))

## [9.3.0](https://github.com/folke/lazy.nvim/compare/v9.2.0...v9.3.0) (2023-01-16)


### Features

* **git:** some debugging tools for git ([208f91b](https://github.com/folke/lazy.nvim/commit/208f91b52fff5f7b6120b19b80e529821d70d009))
* **keys:** allow overriding a keys value to `vim.NIL` to not add the key ([fdf0332](https://github.com/folke/lazy.nvim/commit/fdf0332fe17d9c01f92a8464c04213123a025a07))
* **spec:** overriding keys with an rhs of `false` will remove the key instead ([870af80](https://github.com/folke/lazy.nvim/commit/870af80c68f3834ffcbced1528cce6197ec2b4ae))
* **spec:** you can now override specs using only the plugin name instead of the short url ([0cbd91d](https://github.com/folke/lazy.nvim/commit/0cbd91d2cd942cc448b4648dbc7ba57515a2867c))


### Bug Fixes

* **build:** make sure `rplugin.vim` is loaded when doing a build. Fixes [#382](https://github.com/folke/lazy.nvim/issues/382) ([666ed7b](https://github.com/folke/lazy.nvim/commit/666ed7bf73eb5895253c1155bd29270b066cbdac))
* **loader:** load plugin opts inside a `try` clause to report errors ([7160ca4](https://github.com/folke/lazy.nvim/commit/7160ca419e7be36536dd8fe90ad0bf26cdd773ae))
* **util:** rever ([e8cb863](https://github.com/folke/lazy.nvim/commit/e8cb863703276c579d781b7e4e0b27052df8fc68))


### Performance Improvements

* **util:** dont trigger VeryLazy autocmds when exiting ([1e67dc0](https://github.com/folke/lazy.nvim/commit/1e67dc0d56b8e7cf6befdc7176a4a54e17afc244))
* **util:** properly check that Neovim is exiting. Dont run VeryLazy when that's the case ([efe72d9](https://github.com/folke/lazy.nvim/commit/efe72d98e6fb71252bd9a904c00a40ccd54ebf05))

## [9.2.0](https://github.com/folke/lazy.nvim/compare/v9.1.3...v9.2.0) (2023-01-13)


### Features

* **commands:** allow commands like `Lazy ... | ...` ([#377](https://github.com/folke/lazy.nvim/issues/377)) ([7b78ce3](https://github.com/folke/lazy.nvim/commit/7b78ce33327c3caee9a0933792b432bce5c6c885))
* **spec:** event, keys, ft and cmd can now also be a function that returns the values to be used ([2128ca9](https://github.com/folke/lazy.nvim/commit/2128ca90fb67928e5e23590142de9c94fc0a0d31))


### Bug Fixes

* **cache:** de-duplicate topmods. Fixes [#349](https://github.com/folke/lazy.nvim/issues/349) ([81017b9](https://github.com/folke/lazy.nvim/commit/81017b99e799d08ea5297b0f620e4404ef41e51f))
* **float:** only clear diagnostics for valid buffers ([7b0d1a7](https://github.com/folke/lazy.nvim/commit/7b0d1a786664a707accfde09ecf54315e91f9a2b))
* **ui:** open diff and others over the ui. Don't try to be smart about it. Fixes [#361](https://github.com/folke/lazy.nvim/issues/361) ([3fbe4fe](https://github.com/folke/lazy.nvim/commit/3fbe4fe27ab6b58e5dafd45c5316ec62791907d4))
* use `vim.api.nvim_exec_autocmds` instead of `vim.cmd[[do]]` to prevent weird `vim.notify` behavior ([b73312a](https://github.com/folke/lazy.nvim/commit/b73312aa32c685ff68771a31d209a43866e4d4b2))

## [9.1.3](https://github.com/folke/lazy.nvim/compare/v9.1.2...v9.1.3) (2023-01-11)


### Bug Fixes

* **cache:** use cached chunk when specs are loading for valid plugins ([07fd7ad](https://github.com/folke/lazy.nvim/commit/07fd7adb3427ac510c33de308cd5dfcc6ba701b6))
* **loader:** prevent loading plugins when loading specs ([e1cd9cd](https://github.com/folke/lazy.nvim/commit/e1cd9cd0adfb04432ffaf3d8bd54a5b409eb4273))

## [9.1.2](https://github.com/folke/lazy.nvim/compare/v9.1.1...v9.1.2) (2023-01-11)


### Bug Fixes

* **handlers:** allow overriding handler values ([74bc61a](https://github.com/folke/lazy.nvim/commit/74bc61ab97c3bc2e73e19d269f23076d50c3285f))
* **ui:** possible error during initial install ([a646238](https://github.com/folke/lazy.nvim/commit/a64623899db9fe1a41c8bf86562feed6d4757ba0))
* **ui:** properly position Lazy tabs when opening another cmd. Fixes [#361](https://github.com/folke/lazy.nvim/issues/361) ([8756c09](https://github.com/folke/lazy.nvim/commit/8756c0950ca9053713262abd1092f6d100adc9a5))
* **ui:** reset buf and win options on resize ([3b44c3c](https://github.com/folke/lazy.nvim/commit/3b44c3c14ad69e7a26ae6408816f332af58202c3))


### Performance Improvements

* **util:** execute VeryLazy right after UIEnter ([5aca928](https://github.com/folke/lazy.nvim/commit/5aca9280df4245df8bf8e33fe9bc4ce85507dc31))

## [9.1.1](https://github.com/folke/lazy.nvim/compare/v9.1.0...v9.1.1) (2023-01-10)


### Bug Fixes

* **ui:** get_plugin should return when ui is not showing ([5faadf6](https://github.com/folke/lazy.nvim/commit/5faadf6398f99f781a212d2a7cbd39a688d32300))

## [9.1.0](https://github.com/folke/lazy.nvim/compare/v9.0.0...v9.1.0) (2023-01-10)


### Features

* **spec:** allow git@ and http urls in `Plugin[1]` without `url=`. Fixes [#357](https://github.com/folke/lazy.nvim/issues/357) ([4304035](https://github.com/folke/lazy.nvim/commit/4304035ef4eae2d9dfac4fc082a1b391e6cd928e))
* **util:** `Util.merge` now support advanced merging strategies. Docs coming soon ([b28c6b9](https://github.com/folke/lazy.nvim/commit/b28c6b900030556e4e72f2ce68abae0e7292a3bf))


### Bug Fixes

* **cache:** dont keep invalid entries in the cache (cleanup) ([9fa62ea](https://github.com/folke/lazy.nvim/commit/9fa62ea8ea935dec7078587c3664047db2065bf2))
* **diffview:** fixed parameter for showing single commit with DiffView. Fixes [#304](https://github.com/folke/lazy.nvim/issues/304) ([a32e307](https://github.com/folke/lazy.nvim/commit/a32e307981519a25dd3f05a33a6b7eea709f0fdc))
* **docs:** auto-gen of readme stuff ([3a216d0](https://github.com/folke/lazy.nvim/commit/3a216d008def355813ede7deb5392276b7e3c10c))
* **spec:** `Plugin.opts` is now always a table. Fixes [#351](https://github.com/folke/lazy.nvim/issues/351) ([e77be3c](https://github.com/folke/lazy.nvim/commit/e77be3cf3b01402b86464e1734fb5ead448ce12e))
* **spec:** don't import specs more than once ([ad7aafb](https://github.com/folke/lazy.nvim/commit/ad7aafb257516cefff85aceb5d36041090b40559))
* **ui:** keymap for building a single plugin changed from `b` to `gb`. Fixes [#358](https://github.com/folke/lazy.nvim/issues/358) ([e6ee0fa](https://github.com/folke/lazy.nvim/commit/e6ee0fa6103e9514e85a96fc16902ad7f777b53f))

## [9.0.0](https://github.com/folke/lazy.nvim/compare/v8.1.0...v9.0.0) (2023-01-08)


### ⚠ BREAKING CHANGES

* **spec:** setting a table to `Plugin.config` is now deprecated. Please use `Plugin.opts` instead. (backward compatible for now)

### Features

* **git:** added fast `Git.get_origin` and `Git.get_config` ([a39fa0f](https://github.com/folke/lazy.nvim/commit/a39fa0f0ced7324800eff0a4eb0ed68bf13452d1))
* **git:** lazy now detects origin changes and will fix it on update. Fixes [#346](https://github.com/folke/lazy.nvim/issues/346). Fixes [#331](https://github.com/folke/lazy.nvim/issues/331) ([615781a](https://github.com/folke/lazy.nvim/commit/615781aebfc0230669a2e5750cba3c65f0b8a90e))
* **spec:** setting a table to `Plugin.config` is now deprecated. Please use `Plugin.opts` instead. (backward compatible for now) ([7260a2b](https://github.com/folke/lazy.nvim/commit/7260a2b28be807c4bdc1caf23fa35c2aa33aa6ac))
* **util:** better deep merging with `Util.merge` ([6a31b97](https://github.com/folke/lazy.nvim/commit/6a31b97e3729af3710207642968e1492071a7dbc))

## [8.1.0](https://github.com/folke/lazy.nvim/compare/v8.0.0...v8.1.0) (2023-01-07)


### Features

* **spec:** show error when loading two specs with the same name and a different url. Fixes [#337](https://github.com/folke/lazy.nvim/issues/337) ([c313249](https://github.com/folke/lazy.nvim/commit/c3132492714661121f70daf77d716053ab39bd0b))


### Bug Fixes

* **cache:** check that modpaths still exist when finding mod root ([d34c85d](https://github.com/folke/lazy.nvim/commit/d34c85d58007f37f9eb60fe0c1075950a5ce615e))
* **config:** Don't cache check for attached UIs ([#340](https://github.com/folke/lazy.nvim/issues/340)) ([05b55de](https://github.com/folke/lazy.nvim/commit/05b55deb16f074f2a44b81927c2e5feb63fba651))
* **config:** properly handle uis connecting after startup ([5ed89b5](https://github.com/folke/lazy.nvim/commit/5ed89b5a0d6be65ec9fd0f6526c8c27a922f50a1))

## [8.0.0](https://github.com/folke/lazy.nvim/compare/v7.12.1...v8.0.0) (2023-01-06)


### ⚠ BREAKING CHANGES

* **util:** `require("lazy.util").open_cmd()` is deprecated. See the docs

### Features

* **commands:** `:Lazy! load` now skips `cond` checks when loading plugins. Fixes [#330](https://github.com/folke/lazy.nvim/issues/330) ([eed1ef3](https://github.com/folke/lazy.nvim/commit/eed1ef3c2d13b374def716ed7e9997595c466b3f))


### Bug Fixes

* **loader:** revert change that loaded /plugin after config. Fixes [#328](https://github.com/folke/lazy.nvim/issues/328) ([2ef44e2](https://github.com/folke/lazy.nvim/commit/2ef44e2dee112ba7b83bdfca98f6c07967d65484))
* **loader:** source runtime files without `silent`. Fixes [#336](https://github.com/folke/lazy.nvim/issues/336) ([102bc27](https://github.com/folke/lazy.nvim/commit/102bc2722e73d0dcebd6c90b45a41cb33e0660cb))


### Code Refactoring

* **util:** `require("lazy.util").open_cmd()` is deprecated. See the docs ([4f76b43](https://github.com/folke/lazy.nvim/commit/4f76b431f73c912a7021bc17384533fbad96fba7))

## [7.12.1](https://github.com/folke/lazy.nvim/compare/v7.12.0...v7.12.1) (2023-01-05)


### Bug Fixes

* **cache:** check full paths of cached modpaths. Fixes [#324](https://github.com/folke/lazy.nvim/issues/324) ([b2dec14](https://github.com/folke/lazy.nvim/commit/b2dec14824383137440040da0d9d107f3a29c656))
* **loader:** run plugin config before sourcing runtime ([c59c05c](https://github.com/folke/lazy.nvim/commit/c59c05c7a80693fda369ccab572f8eaca50a1b4f))
* **util:** Util.try can now work without an error message ([e4f79a4](https://github.com/folke/lazy.nvim/commit/e4f79a42d650c926ea12edb7dbe2efbe1031b723))

## [7.12.0](https://github.com/folke/lazy.nvim/compare/v7.11.0...v7.12.0) (2023-01-04)


### Features

* **spec:** allow import property on a plugin spec ([dea43af](https://github.com/folke/lazy.nvim/commit/dea43afc4adff21a6d5864a378459a140a702c0c))


### Bug Fixes

* **keys:** Use vim's default value for an unset g:mapleader ([#316](https://github.com/folke/lazy.nvim/issues/316)) ([3bde7b5](https://github.com/folke/lazy.nvim/commit/3bde7b5ba8b99941b314a75d8650a0a6c8552144))

## [7.11.0](https://github.com/folke/lazy.nvim/compare/v7.10.0...v7.11.0) (2023-01-04)


### Features

* **loader:** disable plugins ([a7ac2ad](https://github.com/folke/lazy.nvim/commit/a7ac2ad0204d63ece6ebca76ae906db53346c8a4))
* **spec:** spec merging now properly works with `Plugin.enabled` ([81cb352](https://github.com/folke/lazy.nvim/commit/81cb352fe6150570b7dd7266e3053869ce40babc))


### Bug Fixes

* **diff:** make diffview work again. Fixes [#304](https://github.com/folke/lazy.nvim/issues/304) ([e61b334](https://github.com/folke/lazy.nvim/commit/e61b334cee143ebb136125d6faa0f18dc35eb6c0))
* **keys:** only replace localleader and maplocalleader. Fixes [#307](https://github.com/folke/lazy.nvim/issues/307), fixes [#308](https://github.com/folke/lazy.nvim/issues/308) ([507b695](https://github.com/folke/lazy.nvim/commit/507b695753b4a7e1eff75f578b7a04b6307e4bc6))
* **loader:** dont show error of missing plugins if they are disabled ([09fd8fa](https://github.com/folke/lazy.nvim/commit/09fd8fabd29eb6da82c3eb2be4b270f9de9b4d8c))
* **loader:** move mapleader check to loader, so it can be set by spec files ([b4d4e6b](https://github.com/folke/lazy.nvim/commit/b4d4e6b41b0b5110019dc247db994ae294f23b77))
* **util:** assume type is file when no type is returned by scandir. Fixes [#306](https://github.com/folke/lazy.nvim/issues/306) ([2e87520](https://github.com/folke/lazy.nvim/commit/2e875208268f0bbc9927bb9b245b00031b6c07d9))


### Performance Improvements

* **spec:** more efficient merging of specs and added `Plugin._.super` ([bce0c6e](https://github.com/folke/lazy.nvim/commit/bce0c6e327c953c644c20c043303826340596e8e))

## [7.10.0](https://github.com/folke/lazy.nvim/compare/v7.9.0...v7.10.0) (2023-01-03)


### Features

* **spec:** allow overriding `Plugin.enabled` ([05aec48](https://github.com/folke/lazy.nvim/commit/05aec48968f91803a53704c04f3fad3c64033256))
* **ui:** added section with disabled plugins ([299ffdf](https://github.com/folke/lazy.nvim/commit/299ffdfd538938e3241998de65d0a175fcf73f48))
* **version:** allow version=false to override default version ([f36c7cb](https://github.com/folke/lazy.nvim/commit/f36c7cb0dc39d1bc3d0ae56d096afd9012a25607))


### Bug Fixes

* **git:** better errors when a branch/tag/version could not be found. Fixes [#276](https://github.com/folke/lazy.nvim/issues/276) ([277a2ab](https://github.com/folke/lazy.nvim/commit/277a2ab10baeebf64548a6b5a606d7b82f8e3165))
* **git:** properly compare git commits with short refs ([dc9c92a](https://github.com/folke/lazy.nvim/commit/dc9c92a9b37352eab36d5c4ff4542b7b3c927b6f))
* **health:** check for all packages on the rtp, excluding `dist` packs ([1c854d7](https://github.com/folke/lazy.nvim/commit/1c854d7a6d37d7b2ab6926605e7341696c77fd6c))
* **install:** dont try re-installing failed missing plugins during startup. Fixes [#303](https://github.com/folke/lazy.nvim/issues/303) ([c85f929](https://github.com/folke/lazy.nvim/commit/c85f929bd98032b35e09fbc5a510884caaa8a5c3))
* **keys:** make operator pending mode work. Fixes [#286](https://github.com/folke/lazy.nvim/issues/286) ([cdb998c](https://github.com/folke/lazy.nvim/commit/cdb998c6fec617b76063ff64e6e44eac7d0b6b7e))
* **keys:** operator ([2e3e65b](https://github.com/folke/lazy.nvim/commit/2e3e65b0f7b16773f5f83ee4eea09fe6bca653cd))
* **keys:** operator pending mode ([e93f50f](https://github.com/folke/lazy.nvim/commit/e93f50fd1b49f09725ecd310a3cce2cd860ff5a0))
* **spec:** show error when users load a plugins module called `lazy` ([1fd8015](https://github.com/folke/lazy.nvim/commit/1fd80159d074e5c22b946d9b87f274a243ecf213))
* **stats:** fixed cputime on linux ([06db1ec](https://github.com/folke/lazy.nvim/commit/06db1ec3c6baa9460e42ef8ed4d2cc2613b194cb))
* **stats:** more robust checks for native cputime ([b5f4106](https://github.com/folke/lazy.nvim/commit/b5f4106892254c748c49a42e07acd80964cb0bce))
* **stats:** use fallback for cputime on windows. Fixes [#280](https://github.com/folke/lazy.nvim/issues/280) ([ddcdc5e](https://github.com/folke/lazy.nvim/commit/ddcdc5e4472a5f9e0ead8afd38e4fed2ec882617))
* **stats:** windows ([85173dc](https://github.com/folke/lazy.nvim/commit/85173dcc4d7a39e67370571316a6290f31a0de4a))
* **ui:** check if win is still valid ([e749e68](https://github.com/folke/lazy.nvim/commit/e749e68b68b66d7f1c8284941b8cca9fd3cd9482))
* **util:** made `Util.lsmod` more robust. See [#298](https://github.com/folke/lazy.nvim/issues/298) ([953c279](https://github.com/folke/lazy.nvim/commit/953c2791d8c391bf720ae68e734078bb558329f6))

## [7.9.0](https://github.com/folke/lazy.nvim/compare/v7.8.0...v7.9.0) (2023-01-02)


### Features

* **commands:** added build command to force rebuild of a plugin ([23c0587](https://github.com/folke/lazy.nvim/commit/23c0587791607bf77f7148c04722977f72537314))
* **event:** track event trigger times ([46997de](https://github.com/folke/lazy.nvim/commit/46997de1c90620897e2a7f31bd9e4751c1223d21))
* **help:** accept patterns for readme ([#269](https://github.com/folke/lazy.nvim/issues/269)) ([d521a25](https://github.com/folke/lazy.nvim/commit/d521a25cfc8608057eade67bfe7991f1ce1ed1b9))
* **loader:** incrementally install missing plugins and rebuild spec, so imported specs from plugins work as expected ([2d06faa](https://github.com/folke/lazy.nvim/commit/2d06faa941998f76f0348b7b69c5ecdcb5f3db2a))
* **spec:** added `import` to import other plugin modules ([919b7f5](https://github.com/folke/lazy.nvim/commit/919b7f5de3ba78d2030be617b64ada17bddd47da))
* **spec:** added support for importing multiple spec modules with `import = "foobar"` ([39b6602](https://github.com/folke/lazy.nvim/commit/39b66027a5c5db9ba6f3a7253cc6513882c27f2a))
* **spec:** allow mergig of config, priority and dependencies ([313015f](https://github.com/folke/lazy.nvim/commit/313015fdb4b44a38f4b5c9fd045c5d29a65f7c7a))
* **spec:** show spec warnings in checkhealth only ([bc4133c](https://github.com/folke/lazy.nvim/commit/bc4133cb3e2d3dceed11d416ab1a0ece2d37f759))
* **ui:** show new version that is available instead of general message ([34e2c78](https://github.com/folke/lazy.nvim/commit/34e2c78e0690a93196b5e59bbc9e050dfd6f3986))
* **ui:** when updating to a new version, show the version instead of the commit refs ([0fadb5e](https://github.com/folke/lazy.nvim/commit/0fadb5e1cec709de839ecd6937b338b9201734ad))
* **util:** added trackfn that wraps a function and tracks timings ([50a456c](https://github.com/folke/lazy.nvim/commit/50a456c189a6ea68f7681c95fe5cfa9c968e4fc6))


### Bug Fixes

* **cache:** allow lazyvim as a plugin ([f6b0172](https://github.com/folke/lazy.nvim/commit/f6b0172e92c502bd4b1482cbb8bed4e6e3231357))
* **cache:** autoloading was broken! ([9e90852](https://github.com/folke/lazy.nvim/commit/9e90852a471205e92e524e9052cc2df101a24d80))
* **cache:** dont return directories in lsmod ([9893430](https://github.com/folke/lazy.nvim/commit/9893430187d70f69aed552e286223671e8ece72f))
* **cache:** keep ordering of topmods the same as in rtp ([11eee43](https://github.com/folke/lazy.nvim/commit/11eee43c7ee63a71b08009769437e8a10814a48c))
* **cache:** only autoload when plugins have been parsed. Needed to support `import` ([0bc73db](https://github.com/folke/lazy.nvim/commit/0bc73db503e550076c0a8effb976a778c7cf5a6a))
* **cache:** properly return two values for finddir ([1ec8f08](https://github.com/folke/lazy.nvim/commit/1ec8f08480493ea1faffebcd3c89ce9e65732054))
* **commands:** fixed plugin completion for commands ([205ce42](https://github.com/folke/lazy.nvim/commit/205ce42cdc93bc62b1c2ae1c754180c5a23be8de))
* **fetch:** always fetch latest origin tags. Fixes [#264](https://github.com/folke/lazy.nvim/issues/264) ([a9de591](https://github.com/folke/lazy.nvim/commit/a9de5910f22faf9036a8297c8fd4e3d47eb8baa6))
* **handler:** properly show errors generated by setting up handlers ([4d77cf2](https://github.com/folke/lazy.nvim/commit/4d77cf2efea3ddec1bc2a335f90bf3a1cfe19db2))
* **health:** always use main spec ([6ff480b](https://github.com/folke/lazy.nvim/commit/6ff480bdee276265e69f644877706ccb11892799))
* **help:** properly escape helptags search pattern ([#268](https://github.com/folke/lazy.nvim/issues/268)) ([1edd1b8](https://github.com/folke/lazy.nvim/commit/1edd1b8945ee91cdfd61654af96c427dce285a9d))
* **loader:** always load init.lua in plugin mods ([60e96b4](https://github.com/folke/lazy.nvim/commit/60e96b478a5374ad1829a505549e3170332d1013))
* **loader:** setup handlers after installing missing plugins. Fixes [#272](https://github.com/folke/lazy.nvim/issues/272) ([b23a5dc](https://github.com/folke/lazy.nvim/commit/b23a5dc8d5d873e3c53283a376c9d9b5ee33697f))
* **plugin:** only get plugin from spec when needed. ([ce3e1fc](https://github.com/folke/lazy.nvim/commit/ce3e1fc5603b9f81165f331350bd2dd54b000d32))
* **spec:** allow a spec module to be on the rtp and not only in config ([51c23b6](https://github.com/folke/lazy.nvim/commit/51c23b661e695d3998893bfd71de2646a6190ad4))
* **spec:** normalize deps before adding spec to make sure merging works as expected ([7d75598](https://github.com/folke/lazy.nvim/commit/7d755987ba6ea6ef8a3213f2119c5e31810ac913))


### Performance Improvements

* **cache:** cache all lua files till UIEnter instead of VimEnter ([77ff7be](https://github.com/folke/lazy.nvim/commit/77ff7beaa49769961b01b4d5b9099b4536ba1de4))
* track some additional cputimes ([d992387](https://github.com/folke/lazy.nvim/commit/d99238791289e7ee5bd847fd10ac3a93ab3422e6))

## [7.8.0](https://github.com/folke/lazy.nvim/compare/v7.7.0...v7.8.0) (2022-12-31)


### Features

* **ui:** press `&lt;c-c&gt;` to abort any running tasks. Fixes [#258](https://github.com/folke/lazy.nvim/issues/258) ([d6b5d6e](https://github.com/folke/lazy.nvim/commit/d6b5d6e756a596304fd4acbc46f9fa553ea880a2))


### Bug Fixes

* **util:** remove double forward slashes ([ed0583e](https://github.com/folke/lazy.nvim/commit/ed0583e82b2797944889aa2c08bb440e6da9f16b))

## [7.7.0](https://github.com/folke/lazy.nvim/compare/v7.6.0...v7.7.0) (2022-12-31)


### Features

* **git:** added support for packed-refs. Fixes [#260](https://github.com/folke/lazy.nvim/issues/260) ([865ff41](https://github.com/folke/lazy.nvim/commit/865ff414c70d20648000d1b9d754dba64dbf4a62))
* **ui:** make browser configurable. Fixes [#248](https://github.com/folke/lazy.nvim/issues/248) ([679d85c](https://github.com/folke/lazy.nvim/commit/679d85c9ffb6bd49d27267b3a282eeb73e063cde))
* **ui:** show when plugin would be loaded for unloaded plugins. Fixes [#261](https://github.com/folke/lazy.nvim/issues/261) ([5575d2b](https://github.com/folke/lazy.nvim/commit/5575d2b2a9eb7e104d85f4f68754ef3734c7a4a1))


### Bug Fixes

* **bootstrap:** fixed bootstrap script ([de82a99](https://github.com/folke/lazy.nvim/commit/de82a991971d20cfaaeb0d86802283e2ac4a4574))
* duplicate state check in bootstrap ([#255](https://github.com/folke/lazy.nvim/issues/255)) ([51fb95e](https://github.com/folke/lazy.nvim/commit/51fb95e4a89743670eb2ba710bcdb0e91834c3d4))
* **git:** always get both tag and version ([cb29427](https://github.com/folke/lazy.nvim/commit/cb29427926121922eb6cc669d22897f7bc9687f1))
* **keys:** forward `count` to keymaps. Fixes [#252](https://github.com/folke/lazy.nvim/issues/252) ([a834b30](https://github.com/folke/lazy.nvim/commit/a834b30c70581e505d8dd62d9c6f9de6a6eba868))
* **ui:** only show plugins to clean under clean ([45d669f](https://github.com/folke/lazy.nvim/commit/45d669f61c8fc239712e794e1e2c5af1f737ee0a))


### Performance Improvements

* **loader:** re-use topmod cache to find `setup()` module ([730bb84](https://github.com/folke/lazy.nvim/commit/730bb84364afee156ad1dde03fc30de3d96af63a))

## [7.6.0](https://github.com/folke/lazy.nvim/compare/v7.5.0...v7.6.0) (2022-12-30)


### Features

* **api:** allow passing options to float so it can be used outside of lazy ([2a617a7](https://github.com/folke/lazy.nvim/commit/2a617a7024d2ed99ff9b51e36600b9c56d928bfc))
* **commands:** added health command to run `:checkhealth lazy` ([86dff1b](https://github.com/folke/lazy.nvim/commit/86dff1b59a978c9db8768e88f07c0532f65f3c8d))
* **health:** added spec parsing errors to `:checkhealth` ([32511a1](https://github.com/folke/lazy.nvim/commit/32511a121407aab44a839c68592860856c691f9f))
* **restore:** you can now restore a plugin to a certain commit. Fixes [#234](https://github.com/folke/lazy.nvim/issues/234) ([1283c2b](https://github.com/folke/lazy.nvim/commit/1283c2b28826c37cb12e5e28d0988f9b8848293e))
* **startup:** missing plugins will now install the versions in the lockfile if available. Fixes [#138](https://github.com/folke/lazy.nvim/issues/138) ([81ee02b](https://github.com/folke/lazy.nvim/commit/81ee02b8f69be2eabd670b8bcc423dba590821de))


### Bug Fixes

* **cache:** clear cached entry on errors ([def5cc5](https://github.com/folke/lazy.nvim/commit/def5cc58166e914bce0a20ed60e0c8be99e76eb4))

## [7.5.0](https://github.com/folke/lazy.nvim/compare/v7.4.2...v7.5.0) (2022-12-29)


### Features

* **bootstrap:** bootstrap with last lazy stable release ([929198b](https://github.com/folke/lazy.nvim/commit/929198bc4feca8089ff265a977854501e3f25c66))

## [7.4.2](https://github.com/folke/lazy.nvim/compare/v7.4.1...v7.4.2) (2022-12-29)


### Bug Fixes

* **loader:** normalize rtp paths on windows [#230](https://github.com/folke/lazy.nvim/issues/230) ([a4bd4dc](https://github.com/folke/lazy.nvim/commit/a4bd4dc4a7b688b6f68f483bd04b85bb83a96bd8))

## [7.4.1](https://github.com/folke/lazy.nvim/compare/v7.4.0...v7.4.1) (2022-12-29)


### Bug Fixes

* **ftdetect:** source ftdetect files only once. Fixes [#235](https://github.com/folke/lazy.nvim/issues/235) ([9f3fb38](https://github.com/folke/lazy.nvim/commit/9f3fb3840228a4d812197f7c6dbd08a9c60d85af))

## [7.4.0](https://github.com/folke/lazy.nvim/compare/v7.3.0...v7.4.0) (2022-12-29)


### Features

* **cache:** update package.loaded on require ([021e546](https://github.com/folke/lazy.nvim/commit/021e54655f8ba9c594b2035f044e5a2a1b13a893))
* **plugin:** allow some `lazy.nvim` spec props to be set by the user ([c8553ca](https://github.com/folke/lazy.nvim/commit/c8553ca44fefb934ebedb1fabba3ca492848fccc))
* **profile:** nicer threshold prompt ([#210](https://github.com/folke/lazy.nvim/issues/210)) ([ff8f378](https://github.com/folke/lazy.nvim/commit/ff8f3783fa5dabdb086c5731c46d1a4cf79917af))
* **ui:** added extra cache stats to the debug tab ([c2f7e2d](https://github.com/folke/lazy.nvim/commit/c2f7e2d0981ec5f06a73923296cfbe52c69ab5da))


### Bug Fixes

* **cache:** ad jit.version to cache version string. Fixes [#225](https://github.com/folke/lazy.nvim/issues/225) ([e3ffcff](https://github.com/folke/lazy.nvim/commit/e3ffcff7cce1206a2e41b413b0923a3aafeb9306))
* **cache:** added support for top level lua linked directories. Fixes [#233](https://github.com/folke/lazy.nvim/issues/233) ([853d4d5](https://github.com/folke/lazy.nvim/commit/853d4d58381870a4804ee7d822d3331d3cc5924d))
* **cache:** always normalize modname separators ([8544c38](https://github.com/folke/lazy.nvim/commit/8544c389ab54dd21c562b2763829670c71266caa))
* **cache:** check package.loaded after auto-load and return existing module if present. Fixes [#224](https://github.com/folke/lazy.nvim/issues/224) ([044e28b](https://github.com/folke/lazy.nvim/commit/044e28bf8bb454335c63998ef6f21bc34b3e6124))
* **cache:** dont update rtp in fast events ([4b75d06](https://github.com/folke/lazy.nvim/commit/4b75d06c076745379fb1688d2bd00eeabeaa4a4b))
* **cache:** make it work again... #fixup ([370b1b9](https://github.com/folke/lazy.nvim/commit/370b1b982e95c004512604eb87f0facd03340095))
* **cache:** OptionSet is not triggered during startup, so use #rtp instead to see if it changed ([9997523](https://github.com/folke/lazy.nvim/commit/9997523841bd39c90d785807411b6babc529f366))
* **cache:** properly get rtp during fast events ([95b9cf7](https://github.com/folke/lazy.nvim/commit/95b9cf743c4d6aab879c2259b79346c6f306dab8))
* **cache:** reload file if compiled code is incompatible. Fixes [#225](https://github.com/folke/lazy.nvim/issues/225) ([b8c5ab5](https://github.com/folke/lazy.nvim/commit/b8c5ab5dae0b826e576a9a99f92a7e63fb20fb01))
* **cmd:** fixed signature of cmd._del. Fixes [#229](https://github.com/folke/lazy.nvim/issues/229) ([a2eac68](https://github.com/folke/lazy.nvim/commit/a2eac685754252c903094aefa40ab6d747d103aa))
* **commands:** E5108 in getcompletions ([#207](https://github.com/folke/lazy.nvim/issues/207)) ([acd6697](https://github.com/folke/lazy.nvim/commit/acd6697d8810e501d3861bba2ac45d5f4555c43a))
* **config:** reset packpath to include VIMRUNTIME only. Fixes [#214](https://github.com/folke/lazy.nvim/issues/214) ([db043da](https://github.com/folke/lazy.nvim/commit/db043da829899239399ef04e917a95c4ceb9b8e6))
* **ft:** only trigger filetypepluing and filetypeindent for ft handler. Fixes [#228](https://github.com/folke/lazy.nvim/issues/228) ([7de662d](https://github.com/folke/lazy.nvim/commit/7de662d037a96fccc3e3d784468b01794288a7b6))
* **git:** add --no-show-signature. Fixes [#218](https://github.com/folke/lazy.nvim/issues/218) ([6c0b803](https://github.com/folke/lazy.nvim/commit/6c0b8039990b08b46b5d0c69392256e9f3a2f8d8))
* **health:** add `cond` key ([#203](https://github.com/folke/lazy.nvim/issues/203)) ([b813fae](https://github.com/folke/lazy.nvim/commit/b813fae61cebbc5b45e7ea3bfbe214b0d5769696))
* **health:** add new key `priority` to `:checkhealth lazy` ([#196](https://github.com/folke/lazy.nvim/issues/196)) ([dc03fa1](https://github.com/folke/lazy.nvim/commit/dc03fa1ae57c3949874c9cae50074a83232c4eed))
* **loader:** implemented correct adding to rtp. fix [#230](https://github.com/folke/lazy.nvim/issues/230), fix [#226](https://github.com/folke/lazy.nvim/issues/226) ([3a1a10c](https://github.com/folke/lazy.nvim/commit/3a1a10cd75b47f2aae1f843286cc17d8a780dff1))
* **loader:** show proper error message when trying to load a plugin that is not installed. Fixes [#201](https://github.com/folke/lazy.nvim/issues/201). Fixes [#202](https://github.com/folke/lazy.nvim/issues/202) ([956164d](https://github.com/folke/lazy.nvim/commit/956164d27dc02b8d3c21c9ef7cc9028d854b0978))
* **loader:** temporary fix for Vimtex and others. See [#230](https://github.com/folke/lazy.nvim/issues/230) ([c7122d6](https://github.com/folke/lazy.nvim/commit/c7122d64cdf16766433588486adcee67571de6d0))
* **loader:** when `config=true`, pass `nil` to `setup()`. Fixes [#208](https://github.com/folke/lazy.nvim/issues/208) ([5f423b2](https://github.com/folke/lazy.nvim/commit/5f423b29c65f536a9c41a34a8328372baa444da5))
* only show fired ft events in debug obviously. Fixes [#232](https://github.com/folke/lazy.nvim/issues/232) ([c7c1295](https://github.com/folke/lazy.nvim/commit/c7c1295c3e429d4a95e36b5c5b2dfcbeca61f42d))
* **rtp:** correct order of adding to rtp. Fixes [#226](https://github.com/folke/lazy.nvim/issues/226) ([4e3a973](https://github.com/folke/lazy.nvim/commit/4e3a973f85bd2393009d495ecfd6c058345309d4))


### Performance Improvements

* move autoloader to cache and always use lazy's modname path resolver which is much faster ([34977c2](https://github.com/folke/lazy.nvim/commit/34977c2b80db3ce5054f3925057b6b8ccbd7ce7e))

## [7.3.0](https://github.com/folke/lazy.nvim/compare/v7.2.0...v7.3.0) (2022-12-27)


### Features

* **plugin:** added `Plugin.priority` for start plugins ([edf8310](https://github.com/folke/lazy.nvim/commit/edf8310288197d4f7c2983a4fa32c09921f00a22))
* **profile:** added accurate startuptime to ui/stats/docs ([a2fdf36](https://github.com/folke/lazy.nvim/commit/a2fdf369f2d503ebe44b421b821c9430c8d5cbe1))
* **reloader:** trigger LazyReload when changes were detected and after reload. Fixes [#178](https://github.com/folke/lazy.nvim/issues/178) ([4e4493b](https://github.com/folke/lazy.nvim/commit/4e4493b21d6b55742b00babd166dc1c1acbfa4ba))
* **ui:** added new section specifically for updates ([3b46160](https://github.com/folke/lazy.nvim/commit/3b46160c01c4b205aa6665096b263663bd433acd))
* **util:** use treesitter to highlight notify messages when available ([d1739cb](https://github.com/folke/lazy.nvim/commit/d1739cb7e1791e90d015610ef4aad30803babddb))


### Bug Fixes

* **cache:** never use packer paths from cache ([bb53b84](https://github.com/folke/lazy.nvim/commit/bb53b8473cd065dc467853222ee3462739ab16fa))
* **ft:** always trigger FileType when lazy-loading on ft ([5618076](https://github.com/folke/lazy.nvim/commit/5618076a451232184b3ed2572ec85573896f48d4))
* **plugin:** find plugins with `/lua/` instead of `/lua` ([8a3152d](https://github.com/folke/lazy.nvim/commit/8a3152de9357cf751546da5a17b9fd52868344f1))
* **plugin:** pass plugin as arg to config/init/build ([b6ebed5](https://github.com/folke/lazy.nvim/commit/b6ebed5888309dd5d9eda145c403627826fd6a35))
* **reloader:** remove extra trailing separator ([#180](https://github.com/folke/lazy.nvim/issues/180)) ([c4d924a](https://github.com/folke/lazy.nvim/commit/c4d924aceea13cfab5cf23d0765c5d206deff341))
* **ui:** removed newlines from profile tab ([0d0d11a](https://github.com/folke/lazy.nvim/commit/0d0d11acb2547ea65e0eba4fb6855f0954ed0239))

## [7.2.0](https://github.com/folke/lazy.nvim/compare/v7.1.0...v7.2.0) (2022-12-26)


### Features

* **cache:** make ttl configurable ([4aa362e](https://github.com/folke/lazy.nvim/commit/4aa362e8dc9ddf1e745085dc242c814569fcce37))
* **plugin:** added `Plugin.cond`. Fixes [#89](https://github.com/folke/lazy.nvim/issues/89), [#168](https://github.com/folke/lazy.nvim/issues/168) ([aed842a](https://github.com/folke/lazy.nvim/commit/aed842ae1e39aa227069a7f46ef0e141efbd021b))
* **ui:** made all highlight groups and icons configurable ([0ea771b](https://github.com/folke/lazy.nvim/commit/0ea771bd70feaba8002e129ef16f65b1dff7c392))
* **ui:** make lazy icon configurable ([#163](https://github.com/folke/lazy.nvim/issues/163)) ([8ea9d8b](https://github.com/folke/lazy.nvim/commit/8ea9d8b0241f2b09b65355039ec89446bde94564))
* **ui:** re-render after resize. Fixes [#174](https://github.com/folke/lazy.nvim/issues/174) ([9a2ecc8](https://github.com/folke/lazy.nvim/commit/9a2ecc875003a4cbcfba2eeaea0fbd794d270449))


### Bug Fixes

* **diff:** use git show when only displaying one commit ([#155](https://github.com/folke/lazy.nvim/issues/155)) ([037f242](https://github.com/folke/lazy.nvim/commit/037f2424303118b1a8312ed31081f518735823d5))
* **keys:** don't escape pendig keys twice and only convert when number ([46280a1](https://github.com/folke/lazy.nvim/commit/46280a191bd1b6b30607f0d97e1c6d1bcbab1a93))
* **keys:** only delete key handler mappings once ([9837d5b](https://github.com/folke/lazy.nvim/commit/9837d5be7e5fe3aed173401f469d371f26c334c7))
* **loader:** add proper error message when trying to load a plugin that doesn't exist. Fixes [#160](https://github.com/folke/lazy.nvim/issues/160) ([9095223](https://github.com/folke/lazy.nvim/commit/90952239d24a9c3496bc2ecf7da1624e6e05d37e))
* **ui:** get plugin details from the correct plugin in case it was deleted ([2f5c1be](https://github.com/folke/lazy.nvim/commit/2f5c1be5255a318d610e0a86abe0a38bf18af4ad))

## [7.1.0](https://github.com/folke/lazy.nvim/compare/v7.0.0...v7.1.0) (2022-12-24)


### Features

* **build:** build can now be a list to execute multiple build commands. Fixes [#143](https://github.com/folke/lazy.nvim/issues/143) ([9110371](https://github.com/folke/lazy.nvim/commit/9110371120db2888647123d7dea7c68a574ae310))
* **manage:** added user events when operations finish. Fixes [#135](https://github.com/folke/lazy.nvim/issues/135) ([a36d506](https://github.com/folke/lazy.nvim/commit/a36d50639358bc00b8ac2d42a8a0a6c0f9c08310))
* **ui:** added custom commands for lazygit and opening a terminal for a plugin ([be3909c](https://github.com/folke/lazy.nvim/commit/be3909c54420c734e32cb045a387990a6fb51bd4))
* **ui:** added multiple options for diff command ([7d02da2](https://github.com/folke/lazy.nvim/commit/7d02da2ff0216ef6ba9097d8ae5a48f54ddc7c4a))
* **ui:** you can now hover over a plugin to open a diff of updates or the plugin homepage ([593d6e4](https://github.com/folke/lazy.nvim/commit/593d6e400b3bb529c507092bf107b6cc4364fb5b))
* util method to open a float ([7c2eb15](https://github.com/folke/lazy.nvim/commit/7c2eb1544416646db09b410d07492555fcf44778))
* **util:** open terminal commands in a float ([8ad05fe](https://github.com/folke/lazy.nvim/commit/8ad05feef19d6b8d4c5f686e0269ac10659f511b))


### Bug Fixes

* **checker:** update updated after every manage operation. Fixes [#141](https://github.com/folke/lazy.nvim/issues/141) ([86f2c67](https://github.com/folke/lazy.nvim/commit/86f2c67aa80b3c64d131ba47189c42ca5a37ac14))
* **help:** make sure we always generate lazy helptags ([f360e33](https://github.com/folke/lazy.nvim/commit/f360e336a5e2b57e1ee0232c9c89a4ceb3617798))
* **manage:** only clear plugins for the op instead of all ([fc182f7](https://github.com/folke/lazy.nvim/commit/fc182f7c5d5df9ba877ab619f6fa545e20ad52f0))
* plugin list can be string[]. Fixes [#145](https://github.com/folke/lazy.nvim/issues/145) ([74d8b8e](https://github.com/folke/lazy.nvim/commit/74d8b8e4e180c40d2ade750940f3c64761fb7930))

## [7.0.0](https://github.com/folke/lazy.nvim/compare/v6.0.0...v7.0.0) (2022-12-23)


### ⚠ BREAKING CHANGES

* default lazy cache path is now under cache instead of state
* `init()` no longer implies lazy-loading. Add `lazy=false` for affected plugins
* run `init()` before loading start plugins. Fixes #107

### Features

* `init()` no longer implies lazy-loading. Add `lazy=false` for affected plugins ([8112640](https://github.com/folke/lazy.nvim/commit/81126403a89b78e6a75948ba5cea15d9499d2025))
* **loader:** automatically lazy-load colorschemes ([07b4677](https://github.com/folke/lazy.nvim/commit/07b467738d3ca0863e957a2bca86825f6aff92df))
* **spec:** `config` can be `true` or a `table` that will be passed to `require("plugin").setup(config)` ([2a7b004](https://github.com/folke/lazy.nvim/commit/2a7b0047dd25f543b147b692fe100e1b2d88ffb2))
* **spec:** allow using plugin names in dependencies ([4bf771a](https://github.com/folke/lazy.nvim/commit/4bf771a6b255fd91b2e16a21da20d55f7f274f05))
* **ui:** added options to sort/filter profiling data ([7dfb9c1](https://github.com/folke/lazy.nvim/commit/7dfb9c1f5cb8dcad4133a93da68cbdb5c8001035))


### Bug Fixes

* added error message to debug failing extmarks [#117](https://github.com/folke/lazy.nvim/issues/117) ([65e9036](https://github.com/folke/lazy.nvim/commit/65e903652bfac5e83d4df8246a29e45c07865c34))
* **checker:** dont report updates on install during startup ([8251c23](https://github.com/folke/lazy.nvim/commit/8251c23c90c15ef5197638777f85ef69402a2725))
* **install:** make sure to setup loaders before attempting install so colorscheme can load. Fixes [#122](https://github.com/folke/lazy.nvim/issues/122) ([7b9b476](https://github.com/folke/lazy.nvim/commit/7b9b476a6238a53062c1c8e4331fcef054bb8761))
* **keys:** don't create with remap! ([b440b3a](https://github.com/folke/lazy.nvim/commit/b440b3ac2d6945fab62fbfc2f2dbe9db3d9d9fe2))
* **keys:** dont delete handlers manually. Let loader do that ([72b3899](https://github.com/folke/lazy.nvim/commit/72b38999bc547a96c769d1de964a846570cfe5d1))
* **keys:** key handlers were not working after reload ([3f60f2d](https://github.com/folke/lazy.nvim/commit/3f60f2dc13faf4d958fdaec16596436ade2ec23d))
* **manage:** do not reload pugins on clear ([b5d6afc](https://github.com/folke/lazy.nvim/commit/b5d6afc4fa4520a986db4898f6b22b267fc041f9))
* pass plugins instead of plugin names to command. Fixes [#103](https://github.com/folke/lazy.nvim/issues/103) ([42f5aa7](https://github.com/folke/lazy.nvim/commit/42f5aa76e21ec34b3d7fc79218e5069610d7db2e))
* remove debug print ([08d458c](https://github.com/folke/lazy.nvim/commit/08d458c5ba595c3ae2801215abf2d5cc09aca211))
* remove lazy keymaps with the correct mode. Fixes [#97](https://github.com/folke/lazy.nvim/issues/97) ([56890ce](https://github.com/folke/lazy.nvim/commit/56890ce5f439e9bbf275ed5ec2573b4e29371bb5))
* run `init()` before loading start plugins. Fixes [#107](https://github.com/folke/lazy.nvim/issues/107) ([2756a6f](https://github.com/folke/lazy.nvim/commit/2756a6f756758d62eeb4cac64d8c5efbc8878cd1))
* **ui:** fix buffer being properly deleted ([#112](https://github.com/folke/lazy.nvim/issues/112)) ([9e98389](https://github.com/folke/lazy.nvim/commit/9e983898b131d4975680bbda023224bb90a32daf))
* **ui:** fixed extmarks while wrapping. Fixes [#124](https://github.com/folke/lazy.nvim/issues/124) ([e973323](https://github.com/folke/lazy.nvim/commit/e973323e95d9cd9ebf41583c94a8c7433d5ae19c))
* **ui:** sort profiling chronological by default ([50e3b91](https://github.com/folke/lazy.nvim/commit/50e3b917675b8bd693548089aeda7e9cbe881001))


### Code Refactoring

* default lazy cache path is now under cache instead of state ([cc6276e](https://github.com/folke/lazy.nvim/commit/cc6276e9b069b5c0c3bdef27dd029722b13bf17d))

## [6.0.0](https://github.com/folke/lazy.nvim/compare/v5.2.0...v6.0.0) (2022-12-22)


### ⚠ BREAKING CHANGES

* lazy api commands now take an opts table instead of a list of plugins

### Features

* added support for `nvim --headless "+Lazy! sync" +qa` ([2e14a2f](https://github.com/folke/lazy.nvim/commit/2e14a2f3243e2979e00405fe417bc530bf1e8ca3))
* **checker:** defer checker to after VeryLazy to make sure nvim-notify and others are loaded ([fd1fbef](https://github.com/folke/lazy.nvim/commit/fd1fbefc3df2b8e92209ed932144edc49877c41e))
* **keys:** more advanced options for setting lazy key mappings ([1c07ea1](https://github.com/folke/lazy.nvim/commit/1c07ea15a37442b7d07dcce9791c497c343ee853))
* lazy api commands now take an opts table instead of a list of plugins ([bc61747](https://github.com/folke/lazy.nvim/commit/bc617474a0bbd9a2e8ec68fd97e09c1682be7ff9))
* **ui:** show modpaths in debug ([6304231](https://github.com/folke/lazy.nvim/commit/63042310f4eaae19ff8a46dfd2ef931c1f498b0f))


### Bug Fixes

* **cache:** overwrite cache entry with new modpath when loading a file. Fixes [#90](https://github.com/folke/lazy.nvim/issues/90) ([2200284](https://github.com/folke/lazy.nvim/commit/22002841653574d57cef7a3137303a25da0796f6))
* **clean:** update lockfile on clean ([#88](https://github.com/folke/lazy.nvim/issues/88)) ([dd9648f](https://github.com/folke/lazy.nvim/commit/dd9648f8ec6526ac376f3ffa85062f6a21385f4d))
* **cmd:** allow ranges. Fixes [#93](https://github.com/folke/lazy.nvim/issues/93) ([c0c2e1b](https://github.com/folke/lazy.nvim/commit/c0c2e1bd68b48610cdca1d3e6a540fd68fc36527))
* **git:** make sure we properly fetch git submodules. Fixes [#72](https://github.com/folke/lazy.nvim/issues/72) ([7f6f31d](https://github.com/folke/lazy.nvim/commit/7f6f31d66f2aba99fad86a64789b7d5d3e61a2cb))
* **git:** remove --also-filter-submodules. Fixes [#86](https://github.com/folke/lazy.nvim/issues/86) [#83](https://github.com/folke/lazy.nvim/issues/83) ([488b487](https://github.com/folke/lazy.nvim/commit/488b48779c1ee6fb4a0d69e31a6c58784cceb403))
* **install:** update lockfile also on install ([4cf176b](https://github.com/folke/lazy.nvim/commit/4cf176bdabbd1a18a20b3b4a608175fb1ba3250e))
* removed spell again from site. not needed. can download in config/spell ([58f0876](https://github.com/folke/lazy.nvim/commit/58f0876e81881c487ea10e393fa828a1c45c74f4))
* **rtp:** keep site in rtp ([94d0125](https://github.com/folke/lazy.nvim/commit/94d012511d19a4438c0098fff000a6d63198f2c8))
* show mapleader warning with vim.schedule. Fixes [#91](https://github.com/folke/lazy.nvim/issues/91) ([28f1511](https://github.com/folke/lazy.nvim/commit/28f1511e0a19d41f9c5e53a64ece257449681b4d))

## [5.2.0](https://github.com/folke/lazy.nvim/compare/v5.1.0...v5.2.0) (2022-12-21)


### Features

* **loader:** allow to add extra paths to rtp reset. Fixes [#64](https://github.com/folke/lazy.nvim/issues/64) ([876f7bd](https://github.com/folke/lazy.nvim/commit/876f7bd47124b4b2881917b36c5d29f3a898eab5))
* **loader:** warn when mapleader is changed after init ([4ca3039](https://github.com/folke/lazy.nvim/commit/4ca30390ec4149763169201b651ad9e78c56896f))
* make hover easy to override ([f0e1b85](https://github.com/folke/lazy.nvim/commit/f0e1b853a0d0d34584ecf9ecbf6ef8599db8b5c2))
* **plugin:** allow plugin files only without a main plugin module. Fixes [#53](https://github.com/folke/lazy.nvim/issues/53) ([44f80a7](https://github.com/folke/lazy.nvim/commit/44f80a7f5d80a56dbfcc5cda34cc805a78ac7189))
* **util:** utility method to get sync process output ([e95da35](https://github.com/folke/lazy.nvim/commit/e95da35d09989d15122ec4bb1364d9c36e36317d))


### Bug Fixes

* **cache:** if we can't load from the cache modpath, find path again instead of erroring right away ([a345649](https://github.com/folke/lazy.nvim/commit/a345649510aad552c0dab4e7a666d387b4ea22d3))
* **checker:** allow git checks only for non-pinned plugins ([#61](https://github.com/folke/lazy.nvim/issues/61)) ([a939243](https://github.com/folke/lazy.nvim/commit/a939243639d452ef5f50fd8f87b8659862f16d37))
* **git:** dereference tag refs. Fixes [#54](https://github.com/folke/lazy.nvim/issues/54) ([86eaa11](https://github.com/folke/lazy.nvim/commit/86eaa118c6d6b5c2806c38aac8db664ba6d780f6))
* **git:** only mark a plugin as dirty if an update changed the commit HEAD. Fixes [#62](https://github.com/folke/lazy.nvim/issues/62) ([bbace14](https://github.com/folke/lazy.nvim/commit/bbace14dc96cd2379aa3f49446ba35a1ad5bfdfa))
* **health:** don't show warning on `module=false` ([c228908](https://github.com/folke/lazy.nvim/commit/c228908ffc485ee01a5ac118e23e13ce3d19cbf9))
* **help:** sort tags files for readmes so tags work properly. Fixes [#67](https://github.com/folke/lazy.nvim/issues/67) ([2fd78fb](https://github.com/folke/lazy.nvim/commit/2fd78fbed8d22524af83a78558dbc895df15d58d))
* **keys:** feedkeys should include pending keys. Fixes [#71](https://github.com/folke/lazy.nvim/issues/71) ([2ab6518](https://github.com/folke/lazy.nvim/commit/2ab651864f30022751252e66b4cd2c1e36800d06))
* **loader:** lua modules can be links instead of files. Fixes [#66](https://github.com/folke/lazy.nvim/issues/66) ([b7c489b](https://github.com/folke/lazy.nvim/commit/b7c489b08f79765b7c840addc4e542b875438f47))
* **loader:** source rtp `/plugin` files after loading start plugins. Fixes ([ff24f49](https://github.com/folke/lazy.nvim/commit/ff24f493ee053f25fc8b34b74443a9f000fdbd55))
* strip `/` from dirs. Fixes [#60](https://github.com/folke/lazy.nvim/issues/60) ([540847b](https://github.com/folke/lazy.nvim/commit/540847b7cb4afc66fea0d7a539821431c5a2b216))
* **ui:** install command can have plugins as a parameter ([232232d](https://github.com/folke/lazy.nvim/commit/232232da5a2d012da0da27b424a016379c83c2f9))
* **ui:** set current win only when its valid ([3814883](https://github.com/folke/lazy.nvim/commit/3814883aaae3facc931087bfa7352ca18fa658ac))

## [5.1.0](https://github.com/folke/lazy.nvim/compare/v5.0.1...v5.1.0) (2022-12-20)


### Features

* added options to configure change detection. Fixes [#32](https://github.com/folke/lazy.nvim/issues/32) ([6c767a6](https://github.com/folke/lazy.nvim/commit/6c767a604de025c0d03c4e2b65f6c4a01ec4918d))
* **ui:** make the windoww size configurable. Fixes [#34](https://github.com/folke/lazy.nvim/issues/34) ([941df31](https://github.com/folke/lazy.nvim/commit/941df31a41560b4131260c47c482bd12502ed8c5))


### Bug Fixes

* add filetype to window buffer. ([#41](https://github.com/folke/lazy.nvim/issues/41)) ([897d6df](https://github.com/folke/lazy.nvim/commit/897d6df5ac8d0e575d52eec60722ce9ffc80cf6f))
* **git:** don't run git log for submodules. Fixes [#33](https://github.com/folke/lazy.nvim/issues/33) ([9d12cdc](https://github.com/folke/lazy.nvim/commit/9d12cdcc0624c8a7f3c7c89f87abf992bc6c217e))
* **loader:** source filetype.lua before plugins. Fixes [#35](https://github.com/folke/lazy.nvim/issues/35) ([ffcd0ab](https://github.com/folke/lazy.nvim/commit/ffcd0ab7bb61bd15b24d2a47509861e30644143c))
* **spec:** only process a spec once ([b193f96](https://github.com/folke/lazy.nvim/commit/b193f96f7b71026f80fd89b6c3fc55fe982bbd1a))
* use nvim_feekeys instead of nvim_input for keys handler. Fixes [#28](https://github.com/folke/lazy.nvim/issues/28) ([5298441](https://github.com/folke/lazy.nvim/commit/52984419ffa051d66bccec9f93e7cbb4fdd94976))


### Performance Improvements

* **ui:** clear existing extmarks before rendering ([06ac8bd](https://github.com/folke/lazy.nvim/commit/06ac8bda66caccca08a18ddac7d25526dff45bb6))

## [5.0.1](https://github.com/folke/lazy.nvim/compare/v5.0.0...v5.0.1) (2022-12-20)


### Bug Fixes

* add neovim libs to rtp for treesitter parsers etc ([df6c986](https://github.com/folke/lazy.nvim/commit/df6c9863dc05b309db9739b05bfabff55f08bf62))
* always set Config.me regardless of reset rtp ([992c679](https://github.com/folke/lazy.nvim/commit/992c6791ef1f9f75b9f20833903bc3a9e43dce90))
* **build:** use the shell to execute build commands ([1371a14](https://github.com/folke/lazy.nvim/commit/1371a141677afe2b0d0d66c96e15ed3ba271bbd9))
* **cache:** if mod is loaded already in the loader, then return that ([ffabe91](https://github.com/folke/lazy.nvim/commit/ffabe91b2d72d686fb21d3159e20bf8faab7ed24))
* checker should not error on non-existing dirs ([ddf36d7](https://github.com/folke/lazy.nvim/commit/ddf36d77486ee80fb8358da88411b28e479d9b0a))
* deepcopy lazyspec before processing ([6e32759](https://github.com/folke/lazy.nvim/commit/6e32759c5ddc43d7095793de952fa2c62f61cb22))
* default logs are now since 3 days ago to be in line with the docs ([e9d3a73](https://github.com/folke/lazy.nvim/commit/e9d3a73bbceaac0dafacd6a3c6c76ab37799d15b))
* dont autoload cached modules when module=false ([316503f](https://github.com/folke/lazy.nvim/commit/316503f124eb4caf5b3bac0da16ee6ac10322424))
* move re-sourcing check to the top ([6404d42](https://github.com/folke/lazy.nvim/commit/6404d421555de681638907bdd4d0ab4f19774ce4))
* only run updated checker for installed plugins. Fixes [#16](https://github.com/folke/lazy.nvim/issues/16) ([ae644a6](https://github.com/folke/lazy.nvim/commit/ae644a604d4f4a4307775ccc163596a90668da34))
* show error when merging, but continue ([f78d8bf](https://github.com/folke/lazy.nvim/commit/f78d8bf376a86349de99696c4004c36b97e859e4))
* use jobstart instead of system to open urls ([1754056](https://github.com/folke/lazy.nvim/commit/175405647587d4d49e3b9c0992c6a8ae31cda706))

## [5.0.0](https://github.com/folke/lazy.nvim/compare/v4.2.0...v5.0.0) (2022-12-20)


### ⚠ BREAKING CHANGES

* removed the LazyUpdate etc commands. sub-commands only from now on

### Features

* added `:Lazy load foobar.nvim` to load a plugin ([2dd6230](https://github.com/folke/lazy.nvim/commit/2dd623001891ad98845523c92e8fcc6043993019))
* added `module=false` to skip auto-loading of plugins on `require` ([1efa710](https://github.com/folke/lazy.nvim/commit/1efa710210ded9677dce8ceb523e08e133c10e1f))
* added completion for all lazy commands ([5ed9855](https://github.com/folke/lazy.nvim/commit/5ed9855d1c31440957eb54b2741a992ed51cc969))
* added support for Windows ([bb1c2f4](https://github.com/folke/lazy.nvim/commit/bb1c2f4c3ef83f79263d7832dd3a91991fcf62d7))
* removed the LazyUpdate etc commands. sub-commands only from now on ([d4aee27](https://github.com/folke/lazy.nvim/commit/d4aee2715fa22ab29422320d817236e927260335))
* utility method to normalize a path ([198963f](https://github.com/folke/lazy.nvim/commit/198963fdabdb24e530808542090c5de3f28ec808))


### Bug Fixes

* **cache:** do a fast check to see if a cached modpath is still valid. find it again otherwise ([32f2b71](https://github.com/folke/lazy.nvim/commit/32f2b71ff884e88358790348d5620ed494ef80b6))
* **cache:** normalize paths ([62c1542](https://github.com/folke/lazy.nvim/commit/62c1542141926aeeb79435cb8a8593e47cc89e43))
* check for installed plugins with plain find ([a189883](https://github.com/folke/lazy.nvim/commit/a18988372faecbd097946dbef6286dd82dca744d))
* **ui:** focus Lazy window when auto-installing plugins in `VimEnter` ([1fe43f3](https://github.com/folke/lazy.nvim/commit/1fe43f3e294cf994a52d25e16dc630e66db2970c))
* **util:** fixed double slashes ([af87108](https://github.com/folke/lazy.nvim/commit/af87108605b624608b46e0f3365cc9a2539c5ec8))


### Performance Improvements

* **cache:** cache loadfile and no find modpaths without package.loaders ([faac2dd](https://github.com/folke/lazy.nvim/commit/faac2dd11c932e71a0cea9bc933f8bbe1e1d2312))
* lazy-load the commands available on the `lazy` module ([b89e6bf](https://github.com/folke/lazy.nvim/commit/b89e6bffd258e4dd367992c306b588e9b24b9a76))

## [4.2.0](https://github.com/folke/lazy.nvim/compare/v4.1.0...v4.2.0) (2022-12-18)


### Features

* check if ffi is available and error if not ([c0d3617](https://github.com/folke/lazy.nvim/commit/c0d3617e0b45b68abc522778837ff8a472273c15))
* expose all commands on main lazy module ([f25f942](https://github.com/folke/lazy.nvim/commit/f25f942eb76f485d09f770dd5ea4c4ca3bef4e0b))
* **loader:** added error handler to sourcing of runtime files ([eeb06a5](https://github.com/folke/lazy.nvim/commit/eeb06a5a509c27b7f0877b513f2278f27cc98f67))
* never source `packer_compiled.lua` ([a46c0c0](https://github.com/folke/lazy.nvim/commit/a46c0c04f13ef4bb10c42004a72a48356f8cfe93))
* **ui:** added dir to props ([9736671](https://github.com/folke/lazy.nvim/commit/97366711bedc7bfc2e9a425e8dfa6f9891e9c865))
* **ui:** added help for &lt;CR&gt; on a plugin ([c87673c](https://github.com/folke/lazy.nvim/commit/c87673c4b97578d7dd6f14e421486cfa6e008b91))
* **ui:** made it look a little less like a Mason rip-off :) ([9026a0e](https://github.com/folke/lazy.nvim/commit/9026a0e25d4e3ebfe2cac7d7a724cb8211fac4f1))
* **ui:** make home bold ([0b4a04d](https://github.com/folke/lazy.nvim/commit/0b4a04de7d264b5890210f92eef0e6521bf8d0c9))


### Bug Fixes

* **loader:** runtime files are now sourced alphabetically per directory ([5c0c381](https://github.com/folke/lazy.nvim/commit/5c0c381b56f78622df47e2057210232ed0a3275e))
* set correct dir for lazy plugin ([23984dd](https://github.com/folke/lazy.nvim/commit/23984dd1f300e09cbc1bc9a80aae3bea32a5bbcc))
* **ui:** always clear complete tasks with the same name when starting a new task ([85e3752](https://github.com/folke/lazy.nvim/commit/85e375223f21e35fd5f779cad05be0397557e72a))
* **ui:** show first tag for each help doc in details ([6f728e6](https://github.com/folke/lazy.nvim/commit/6f728e698d5e19de36dd861f6699b6b4560e5f42))
* **ui:** split window before opening a file from the Lazy ui, otherwise it'll get closed immediately ([f18efa1](https://github.com/folke/lazy.nvim/commit/f18efa1da1b1274466444a477574ac2b6a2c24b3))

## [4.1.0](https://github.com/folke/lazy.nvim/compare/v4.0.0...v4.1.0) (2022-12-16)


### Features

* **docs:** added toc generator ([f4720ee](https://github.com/folke/lazy.nvim/commit/f4720ee9f745c0b77366f1e5e6ea7fc7bfaf8010))
* lua code generator for the README.md ([80a7839](https://github.com/folke/lazy.nvim/commit/80a7839eec62560e9160663cee4ea4c9e67196fc))
* README.md files are now automagically added to help. By default only when no doc/ exists ([70ca110](https://github.com/folke/lazy.nvim/commit/70ca110ca19c305dfe2790de5a82f5e6789a73ee))
* utility methods to read/write files ([27178b5](https://github.com/folke/lazy.nvim/commit/27178b5e6759f6429602acfeb674834e0dad1f13))


### Bug Fixes

* `Plugin.init` implies lazy-loading ([ccdf65b](https://github.com/folke/lazy.nvim/commit/ccdf65b5b8974438cb60c10ec00c7302c339f9da))
* add lazy.nvim with dev=false to prevent using the dev version for myself ([b8fa6f9](https://github.com/folke/lazy.nvim/commit/b8fa6f960f9bff5e17a7731a204cad21d564ef34))
* bootstrap code now uses git url instead of https for beta testers + fixed rtp path ([17d1653](https://github.com/folke/lazy.nvim/commit/17d1653b4a39b80e0d59e3e4877cf23cdd9b6756))
* use initial rtp for rtp plugin after files and use loaded plugins for their after files ([7134417](https://github.com/folke/lazy.nvim/commit/7134417e89319514c9bd9a8913012a396095f48d))


### Performance Improvements

* prevent string.match to find plugin name from a modpath ([f23a6ee](https://github.com/folke/lazy.nvim/commit/f23a6eef8ca3e8416167266cafd037a5e27a7cc6))
* when reloading plugin specs always use cache ([060cf23](https://github.com/folke/lazy.nvim/commit/060cf23aca3826c213ad26ff1860815b03064269))

## [4.0.0](https://github.com/folke/lazy.nvim/compare/v3.0.0...v4.0.0) (2022-12-14)


### ⚠ BREAKING CHANGES

* lazy now handles the full startup sequence (`vim.go.loadplugins=false`)

### Features

* added checks for Neovim version ([72f64ce](https://github.com/folke/lazy.nvim/commit/72f64ce1f7a3bbcbc500a7e0f8d7950376ec6a12))
* getter for plugins ([8de617c](https://github.com/folke/lazy.nvim/commit/8de617c01b572965d8a48362597fce01dc3ebcc7))
* lazy now handles the full startup sequence (`vim.go.loadplugins=false`) ([ec2f432](https://github.com/folke/lazy.nvim/commit/ec2f432a84bead4aaaf684b4eb2d88e41592703e))
* **ui:** show `updates available` diagnostic when an update is available ([ad0b4ca](https://github.com/folke/lazy.nvim/commit/ad0b4caa648fe84eb1dff5e55d3f02d293b33ad1))


### Bug Fixes

* destroy the cache when VIMRUNTIME has changed ([5128d89](https://github.com/folke/lazy.nvim/commit/5128d896c759c0599b6da5f5ba2cee102d864cad))
* updated the bootstrap code ([1ee4e8b](https://github.com/folke/lazy.nvim/commit/1ee4e8b7197ff23383a6a3306cdd15f20be04b72))

## [3.0.0](https://github.com/folke/lazy.nvim/compare/v2.2.0...v3.0.0) (2022-12-13)


### ⚠ BREAKING CHANGES

* local plugins now always need to set `Plugin.dir`

### Features

* added health checks ([dc2dcd2](https://github.com/folke/lazy.nvim/commit/dc2dcd2d5a8c256497235428e129907e99e0ae58))
* **api:** return runner from manage operations ([71e4b92](https://github.com/folke/lazy.nvim/commit/71e4b92fd6fbb807ef82ebc9586cfe2a233234b4))
* better way of dealing with lazy loaded completions (thanks to [@lewis6991](https://github.com/lewis6991)) ([f24c055](https://github.com/folke/lazy.nvim/commit/f24c055fe9ebc810dfb35328dd312d4cd9038db1))
* **checker:** only report an update once and do a fast update check after each manage operation ([2a7466a](https://github.com/folke/lazy.nvim/commit/2a7466abadb7987e81009cdd06042fb2d2b59366))
* local plugins now always need to set `Plugin.dir` ([0625493](https://github.com/folke/lazy.nvim/commit/0625493aadf025476c62841fc3d36bf836f15bc7))
* **ui:** added statusline component to show pending updates ([315be83](https://github.com/folke/lazy.nvim/commit/315be83afc96f5dd1f76f943de1be7d2429b5bf7))
* **ui:** added update checker ([65cd28e](https://github.com/folke/lazy.nvim/commit/65cd28e613a7b7208a3b1e61f5effc581c7b0247))


### Bug Fixes

* dev plugins with dev=false should be configured as remote ([43b303b](https://github.com/folke/lazy.nvim/commit/43b303bd8f2eb45a251e370694cc871e20d7d557))
* replace ~ by HOME for Plugin.dir ([12ded3f](https://github.com/folke/lazy.nvim/commit/12ded3f4223f3dc465e671c16ff1a537a75150fa))
* **ui:** open with noautocmd=true and close with vim.schedule to prevent weird errors by other plugins ([08d081f](https://github.com/folke/lazy.nvim/commit/08d081f21d9b54ed0b20e9a94050e3b39c75de19))


### Performance Improvements

* added profiling for sourcing of runtime files ([be509c0](https://github.com/folke/lazy.nvim/commit/be509c01f94821a6c0e5a2a4349d9160b4a4b6fe))

## [2.2.0](https://github.com/folke/lazy.nvim/compare/v2.1.0...v2.2.0) (2022-12-05)


### Features

* cleanup keys/cmd handlers when loading a plugin ([3f517ab](https://github.com/folke/lazy.nvim/commit/3f517abfa43ec9410315e205c1ee3798b66e1153))
* dont run setup again when a user re-sources their config & show a warning ([7b945ee](https://github.com/folke/lazy.nvim/commit/7b945eec588e499f0ea36974df90836549a3e734))
* **ui:** added debug interface to inspect active handlers and the module cache ([6d68cc6](https://github.com/folke/lazy.nvim/commit/6d68cc6ea20a5778fabe37ccca679d8568615a20))
* **ui:** show any helps files and added hover handler ([13b5688](https://github.com/folke/lazy.nvim/commit/13b568848775de3adfd17a410ec482c1e03da489))
* util.foreach with sorted keys ([d36ad41](https://github.com/folke/lazy.nvim/commit/d36ad410eef90bfe1a0dddd6ec1904321a5510ed))


### Bug Fixes

* always add config/after to rtp ([c98e722](https://github.com/folke/lazy.nvim/commit/c98e722fa41e0aa94809e44edf859216afedd8ad))
* **ui:** always show branch name in details ([6e44be0](https://github.com/folke/lazy.nvim/commit/6e44be0f2d543b680041be669a93377291b9132f))


### Performance Improvements

* disable cache by default on VimEnter or on BufReadPre ([b2727d9](https://github.com/folke/lazy.nvim/commit/b2727d98a3ac49cdf462e2bdf5f195dc572a91a4))

## [2.1.0](https://github.com/folke/lazy.nvim/compare/v2.0.0...v2.1.0) (2022-12-03)


### Features

* `Plugin.local` to use a local project instead of fetching remote ([0ba218a](https://github.com/folke/lazy.nvim/commit/0ba218a065c956181ff62077979e96be8bbe3d6a))
* `Plugin.specs()` can now reload and keeps existing state ([330dbe7](https://github.com/folke/lazy.nvim/commit/330dbe72031e642d2cd04b671c6eb498d96e4b71))
* added debug option ([e4cf8b1](https://github.com/folke/lazy.nvim/commit/e4cf8b141681657922643e70ec21b9f9133e9fca))
* automatically detect config module changes in or oustside Neovim and reload ([7b272b6](https://github.com/folke/lazy.nvim/commit/7b272b6ed66e21a15c6c95b00dec73be953b6554))
* for `event=`, fire any new autocmds created by loading the plugins for the event ([ebf15fc](https://github.com/folke/lazy.nvim/commit/ebf15fc198d6c82f64c17e0b752a30fd4c3cdbc7))
* moved Config.package.reset -&gt; Config.performance.reset_packpath ([fe6b0b0](https://github.com/folke/lazy.nvim/commit/fe6b0b03ead3cfeb3f9bcc365c0364346c8e3c9d))
* plugins no longer need to be installed under site/pack/*/opt ([dbe2d09](https://github.com/folke/lazy.nvim/commit/dbe2d0942a88c1211820c2e96d719c63735e976a))
* symlinking local plugins is no longer needed ([37c7366](https://github.com/folke/lazy.nvim/commit/37c7366ab02458472d97d8e35ed50583452bfe91))
* temporary colorscheme to use during install during startup ([7ec65e4](https://github.com/folke/lazy.nvim/commit/7ec65e4cd94425d08edcdab435372e4b67069d76))


### Bug Fixes

* add plugin after dir to rtp for start plugins so it gets picked up during startup ([93d3072](https://github.com/folke/lazy.nvim/commit/93d30722a011c831cce1395178b6effc1d5242de))
* **fs:** dont set cloned=true if symlink already existed ([3e143c6](https://github.com/folke/lazy.nvim/commit/3e143c6017ba3c17dd249492cc86e0d2f2750229))
* **git:** fixed branch detection, get target commit from origin and always checkout a tag or commit so we dont need to use git merge ([ae379a6](https://github.com/folke/lazy.nvim/commit/ae379a62dcaa0854086c6763672b806d3175b91c))
* respect --noplugin ([59fb050](https://github.com/folke/lazy.nvim/commit/59fb0507677628c16425dc2741f005f5394e8102))
* return nil when `fs_stat` fails and return nil in module loader ([afcba52](https://github.com/folke/lazy.nvim/commit/afcba52b1aa7f261eb37a9f6cce4e81cb44b8bec))
* source plugin files for plugins that want to run a build script during startup ([3ed24ba](https://github.com/folke/lazy.nvim/commit/3ed24baeb0c58eb24da605a57ccfdb65d1e89b47))
* temporary colorscheme should only load when installing ([ec858db](https://github.com/folke/lazy.nvim/commit/ec858db225b3fb1cc17a795ad28baa425db20061))


### Performance Improvements

* added option to reset rtp to just your config and the neovim runtime ([ccc506d](https://github.com/folke/lazy.nvim/commit/ccc506d5f71af1cce97ebde0c780f7a6454e2ace))
* caching strategy is now configurable ([6fe425c](https://github.com/folke/lazy.nvim/commit/6fe425c91acbf2b9b948b23673e22a0c61150249))

## [2.0.0](https://github.com/folke/lazy.nvim/compare/v1.2.0...v2.0.0) (2022-12-02)


### ⚠ BREAKING CHANGES

* plugins are now automatically loaded on require. `module=` no longer needed!
* all plugins are now opt. Plugin.opt => Plugin.lazy
* renamed Plugin.run => Plugin.build

### Features

* all plugins are now opt. Plugin.opt =&gt; Plugin.lazy ([5134e79](https://github.com/folke/lazy.nvim/commit/5134e797f34792e34e86fe82a72cdf765ca2e284))
* lazy setup with either a plugins module, or a plugins spec ([af8b8e1](https://github.com/folke/lazy.nvim/commit/af8b8e128e20f9fa30077bedf8bcee40b779c533))
* plugins are now automatically loaded on require. `module=` no longer needed! ([575421b](https://github.com/folke/lazy.nvim/commit/575421b3fb22731a9f97370d794fe7e3c7b57f7b))
* renamed Plugin.run =&gt; Plugin.build ([042aaa4](https://github.com/folke/lazy.nvim/commit/042aaa4f87c6576a369cbecd86aceefb96add228))
* show module source if loading source is under config ([041a716](https://github.com/folke/lazy.nvim/commit/041a716f4e5291d6947c5f96b21a2c4db0aef6e3))
* **ui:** better detection of plugins/config files that loaded a plugin ([723274e](https://github.com/folke/lazy.nvim/commit/723274efeeeddb82a5ee8ca38d456d393555ba94))
* **ui:** improvements to profiling and rendering of loaded reasons ([714bc0a](https://github.com/folke/lazy.nvim/commit/714bc0a136cd72730e1c457556fbe004a22db6b7))


### Bug Fixes

* always overwrite any plugin spec for lazy.nvim to manage itself ([d46bc77](https://github.com/folke/lazy.nvim/commit/d46bc7795c255f121d2d279764017c7d60edff88))
* prepend package path to packpath if package.reset=false ([5eb2622](https://github.com/folke/lazy.nvim/commit/5eb2622a4e4e52bed94b5c8ae48b83ccfab0098d))
* **ui:** use Plugin.find to detect loading reason ([98ccf55](https://github.com/folke/lazy.nvim/commit/98ccf556d8c1e6a8eadb004620c9d5e95733285a))


### Performance Improvements

* module now caches all lua modules used till VimEnter ([0b6dec4](https://github.com/folke/lazy.nvim/commit/0b6dec46e02b2f56ac5c180d6a809f140e50ddf6))
* reset packpath to only include the lazy package. Improved my startup time by 2ms ([4653119](https://github.com/folke/lazy.nvim/commit/4653119625fa8e8c647f6c0ff0b0b57ee81521b8))

## [1.2.0](https://github.com/folke/lazy.nvim/compare/v1.1.0...v1.2.0) (2022-11-30)


### Features

* added config option for process timeout ([bd2d642](https://github.com/folke/lazy.nvim/commit/bd2d64230fc0fe931fa480f4c6a61f507fbbd2ca))
* allow config of default for version field ([fb96183](https://github.com/folke/lazy.nvim/commit/fb96183753bfc734b081fc5a2a3d5705376d9d20))
* config for ui border ([0cff878](https://github.com/folke/lazy.nvim/commit/0cff878b2e1af134892184920fd8ae64d9f954c0))
* config option for runner concurrency ([b2339ad](https://github.com/folke/lazy.nvim/commit/b2339ade847d2ccf5e898edb7cca0bca20e635a3))
* config option for ui throttle ([a197f75](https://github.com/folke/lazy.nvim/commit/a197f751f97c1b050916a8453acba914569b7bb5))
* config option install_missing=true ([9be3d3d](https://github.com/folke/lazy.nvim/commit/9be3d3d8409c6992cea5b2ffe0973fd6b4895dc6))


### Bug Fixes

* show proper installed/clean state for local plugins ([1e2f527](https://github.com/folke/lazy.nvim/commit/1e2f5273bb61b660dd93651c4fc44d2c8c21b905))
* update state after running operation so the ui reflects any changes from cleaning ([0369278](https://github.com/folke/lazy.nvim/commit/03692781597b648fa3524e50c0de4bff405ba215))


### Performance Improvements

* merge module/cache and use ffi to pack cache data ([e1c08d6](https://github.com/folke/lazy.nvim/commit/e1c08d64b387c59343c21a6f0397b88d5b4a3acc))
* removed partial spec caching. not worth the tiny performance boost ([4438faf](https://github.com/folke/lazy.nvim/commit/4438faf9a9a72c95d88c620804db99fa44485ec9))
* run cache autosave after loading ([3ec5a2c](https://github.com/folke/lazy.nvim/commit/3ec5a2ce4c99202dfa76970bbaa36bfa05230cb5))

## [1.1.0](https://github.com/folke/lazy.nvim/compare/v1.0.0...v1.1.0) (2022-11-29)


### Features

* dependencies are opt=true by default if they only appear as a dep ([908b9ad](https://github.com/folke/lazy.nvim/commit/908b9adf9c5a3bc5fd26e0b4900f88faee16f731))
* lazy handler implies opt=true ([b796abc](https://github.com/folke/lazy.nvim/commit/b796abcc33e43a012983cc82f01e3bedd9f3c365))


### Bug Fixes

* make sure Plugin.opt is always a boolean ([ca78dd7](https://github.com/folke/lazy.nvim/commit/ca78dd77ac39ca21f1386292f338a87b47ffa84b))


### Performance Improvements

* dont loop over handlers to determine if a plugin should be opt=true ([812bb3c](https://github.com/folke/lazy.nvim/commit/812bb3c8b76e5102d7d391fd7bbfcdfd0bbe506b))

## 1.0.0 (2022-11-29)


### ⚠ BREAKING CHANGES

* added icons

### Features

* a gazilion rendering improvements ([a11fc5a](https://github.com/folke/lazy.nvim/commit/a11fc5a0e0229b9394946296a5cc241db788f476))
* added "Lazy check" to check for updates without updating ([63cf2a5](https://github.com/folke/lazy.nvim/commit/63cf2a52bd46019914fc41160c9601db06fdd469))
* added bootstrap code ([ceeeda3](https://github.com/folke/lazy.nvim/commit/ceeeda36e89a4f048903e051d9fece5222be087e))
* added full semver and range parsing ([f54c24a](https://github.com/folke/lazy.nvim/commit/f54c24a4fac6d261dc6ebd72d64aa8ceaab9aa12))
* added icons ([c046b1f](https://github.com/folke/lazy.nvim/commit/c046b1f5d5e31904f5ee4c2d24b484246fc09e08))
* added keybindings to update/install/clean/restore/... single plugins ([08b7e42](https://github.com/folke/lazy.nvim/commit/08b7e42fb0743da4fb4221f51d28bd8b108ee25f))
* added lockfile support ([4384d0e](https://github.com/folke/lazy.nvim/commit/4384d0e6d918b7db0cdaebbf0f3b0a4230c84120))
* added profiler view ([20ff5fa](https://github.com/folke/lazy.nvim/commit/20ff5fa218b4a27194fee0b3d023e92f797cd34d))
* added section with logs containing breaking changes ([d7dbe1a](https://github.com/folke/lazy.nvim/commit/d7dbe1a43f712065b71c6da35d75b23deba1ffe1))
* added support for Plugin.lock (wont update) ([0774f1b](https://github.com/folke/lazy.nvim/commit/0774f1bc255e91bf16c426908cd50ed038b21305))
* added vimdoc/release-please/tests ([e9a1e9f](https://github.com/folke/lazy.nvim/commit/e9a1e9fe19d6180d5f1e65fd9375b6c333f5159e))
* default log is last 10 entries ([54a82ad](https://github.com/folke/lazy.nvim/commit/54a82ad69566c99110976c644a181bf5a381b998))
* detect headless and set interactive=false ([bad1b1f](https://github.com/folke/lazy.nvim/commit/bad1b1f87d3a6dc5ae4b5cdcb1eda7dd79b511f1))
* error handler for loading modules, config and init, with custom error formatting ([7933ae1](https://github.com/folke/lazy.nvim/commit/7933ae11c437e9ab5a42cfd729994c52f503b132))
* git log ([3218c2d](https://github.com/folke/lazy.nvim/commit/3218c2d9ec6f88f00d46775f67c1b2dca436af4c))
* git log config ([3e4f846](https://github.com/folke/lazy.nvim/commit/3e4f84640eaee485c130b303d71cbf847650473a))
* initial commit ([e73626a](https://github.com/folke/lazy.nvim/commit/e73626a3444cef85c6e191989b97d5deb8d2befd))
* keep track what loaded a plugin ([4df73f1](https://github.com/folke/lazy.nvim/commit/4df73f167dfba7958abae393f72bbe2a5e5a663a))
* lazy caching now works with functions that have upvalues ([fe33e4e](https://github.com/folke/lazy.nvim/commit/fe33e4e3dde934b3ddade619e9982cd1d54713b0))
* lazy commands ([ae0b871](https://github.com/folke/lazy.nvim/commit/ae0b87181db0ac10b60cfb35c8f4691234444a9d))
* lazy view ([a87982f](https://github.com/folke/lazy.nvim/commit/a87982ff1525f3f54a716175bf0b8f73a82a491c))
* load plugin on cmd complete and make completion just work ([2080694](https://github.com/folke/lazy.nvim/commit/2080694e3402980d7b84fa095bfdd084002d64c7))
* lots of improvements to pipeline runner and converted all tasks to new system ([fb84c08](https://github.com/folke/lazy.nvim/commit/fb84c081b0f1b5d42b2edf9f66fd2cc2db3a0a7e))
* new git module to work with branches, tags & versions ([2abdc68](https://github.com/folke/lazy.nvim/commit/2abdc681fad811895a744dac09009db25cf92f6e))
* new render features like profile etc ([48199f8](https://github.com/folke/lazy.nvim/commit/48199f803189284b9585b96066f84d3805cce6b1))
* new task pipeline runner ([ab1b512](https://github.com/folke/lazy.nvim/commit/ab1b512545fd1a4fd3e6742d5cb7d13b7bcd92ff))
* plugin manager tasks ([a612e6f](https://github.com/folke/lazy.nvim/commit/a612e6f6f4ffbcef6ae7f94955ac406d436284d8))
* return whether a module was loaded from cache or from file (dirty) ([38e2711](https://github.com/folke/lazy.nvim/commit/38e2711cdb8c342c9d6687b22f347d7038094011))
* task docs and options for logs ([fe6d0b1](https://github.com/folke/lazy.nvim/commit/fe6d0b1745cb8171c441e81168df23a09238fc9e))
* **text:** center text ([88869e6](https://github.com/folke/lazy.nvim/commit/88869e67d2f06c7778b9bdbf57681615d3d41f11))
* **text:** multiline support and pattern highlights ([815bb2c](https://github.com/folke/lazy.nvim/commit/815bb2ce6cdc359115a7e65021a21c3347e8a5f6))
* url open handlers ([6f835ab](https://github.com/folke/lazy.nvim/commit/6f835ab87b5f8ecef630cd9b024fac03795bb674))
* util.info ([e59dc37](https://github.com/folke/lazy.nvim/commit/e59dc377d5e30df8edc471f2cb74dbdd9cf8039d))
* **view:** modes and help ([0db98bf](https://github.com/folke/lazy.nvim/commit/0db98bf053fcbe04926e6773897a5e811b82c293))


### Bug Fixes

* always recaclulate hash when loading a module ([cfc3933](https://github.com/folke/lazy.nvim/commit/cfc39330dc022543052ef66d38cb15697b4fc0e4))
* check for lazy before setting loading time ([30bdc9b](https://github.com/folke/lazy.nvim/commit/30bdc9b5a1b4c54128a1cb30dbab5cb8bb6a67b3))
* clean ([7f4743a](https://github.com/folke/lazy.nvim/commit/7f4743ac304bfb762f5d03dd2d691cf4bba933e2))
* correctly handle changes from local to remote plugin ([4de10f9](https://github.com/folke/lazy.nvim/commit/4de10f9578d49fe7fffb64a0fcd3ee55d9ea89aa))
* decompilation fixes ([57d024e](https://github.com/folke/lazy.nvim/commit/57d024ef196cbd0d7166703218726418e33184b9))
* dont return init.lua in lsmod ([413dd5b](https://github.com/folke/lazy.nvim/commit/413dd5b112e57bd57fbf93509cb3dcbdc430fb8d))
* first line of file ([c749404](https://github.com/folke/lazy.nvim/commit/c7494044236a2753deb53a81db02f06cc308d47a))
* get current branch if remote head not available (for local repos only) ([d486bc5](https://github.com/folke/lazy.nvim/commit/d486bc586b6a711af64444c4cec52b8b1590295c))
* highlights ([35b1f98](https://github.com/folke/lazy.nvim/commit/35b1f98ac756ec31459d366aa363d693adb27647))
* log errors in runner ([7303017](https://github.com/folke/lazy.nvim/commit/7303017b6f4ee7b72b86b8c12ee29bf1c2bd8381))
* make sure we have ran on_exit before returning is_done=true ([782d287](https://github.com/folke/lazy.nvim/commit/782d287d891522dec8e460297f81cb5a8fbe33dc))
* manage opts show =&gt; interactive ([93a3a6c](https://github.com/folke/lazy.nvim/commit/93a3a6ccb55055c50dec22fdf0dd11b890defdb4))
* only save state when dirty ([32ca1c4](https://github.com/folke/lazy.nvim/commit/32ca1c4bf875b10776ad8a928e43df290d11cd42))
* recalculate loaders on config file change ([870d892](https://github.com/folke/lazy.nvim/commit/870d8924f76f98da7b436e4baaa2f3c4f0f4f442))
* reset diagnostics when lazy view buffer closes ([04dea38](https://github.com/folke/lazy.nvim/commit/04dea38794547cef79d40e56667fd0c9909cf1f1))
* show view with schedule to prevent Neovim crash when no plugins are installed ([5d84967](https://github.com/folke/lazy.nvim/commit/5d84967e9c011e32e1e9b482f95314df8dfc0e27))
* support adding top-level lua directories ([7288962](https://github.com/folke/lazy.nvim/commit/72889623af0e2ee461d2ec6e5f2fee39e81fd1c2))
* support local files as plugin spec ([0233460](https://github.com/folke/lazy.nvim/commit/0233460d5422a18ecee5b25bc782321f398835c4))
* **tasks:** always set updated on checkout. Change default logging to 3 days ([5bcdddc](https://github.com/folke/lazy.nvim/commit/5bcdddc0ecb28f7d6832767ca142de442a514581))
* **view:** handler details ([bbad0cb](https://github.com/folke/lazy.nvim/commit/bbad0cb8917f1e48c519bf978bfa4d4900131d49))
* when just cloned, never commit lock ([32fa5f8](https://github.com/folke/lazy.nvim/commit/32fa5f84412804a08a71846c121fbb0bbb915322))


### Performance Improvements

* cache handler groups ([42c2fb4](https://github.com/folke/lazy.nvim/commit/42c2fb42c8b466ea1ffe0a9248664419a917a265))
* copy reason without deepcopy ([72d51ce](https://github.com/folke/lazy.nvim/commit/72d51cee9b4b8c43539aa08e5c17a9ef5bc4e84b))
* fast return for Util.ls when file found ([073b5e3](https://github.com/folke/lazy.nvim/commit/073b5e3caaf6c2b5b69793ed255fe73680d3d6e2))
* further optims to loading and caching specs. dont cache specs with plugin that have init or in start with config ([8790070](https://github.com/folke/lazy.nvim/commit/879007087163ef8bd8c6fd86edc82133cec6a416))
* split caching in state, cache and module ([54d5ff1](https://github.com/folke/lazy.nvim/commit/54d5ff18f573057afd6427b62e6ae5dc241acc16))
* tons of performance improvements. Lazy should now load in about 1.5ms for 97 plugins ([2507fd5](https://github.com/folke/lazy.nvim/commit/2507fd5790db8917f01088ef3875a512962ffdca))
* way better compilation and caching ([a543134](https://github.com/folke/lazy.nvim/commit/a543134b8c1b17c2396a757b08951b6d91b14402))
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
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

## File: `selene.toml`
```
std="vim"

[lints]
mixed_table="allow"
```

## File: `stylua.toml`
```
indent_type = "Spaces"
indent_width = 2
column_width = 120
[sort_requires]
enabled = true

```

## File: `TODO.md`
```markdown
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

## File: `vim.yml`
```yaml
base: lua51
lua_versions:
  - luajit

globals:
  Snacks:
    any: true
  vim:
    any: true
  jit:
    any: true
  assert:
    any: true
  describe:
    any: true
  it:
    any: true
  before_each:
    any: true
```

## File: `doc/lazy.nvim.txt`
```
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
                                           set. Lazy uses several heuristics to determine the
                                           plugin’s MAIN module automatically based on the plugin’s
                                           name. (opts is the recommended way to configure plugins).

  main       string?                       You can specify the main module to use for config() and
                                           opts(), in case it can not be determined automatically.
                                           See config()

  build      fun(LazyPlugin) or string or  build is executed when a plugin is installed or updated.
             false or a list of build      See Building for more information.
             commands                      
  --------------------------------------------------------------------------------------------------
Always use `opts` instead of `config` when possible. `config` is almost never
needed.




SPEC LAZY LOADING               *lazy.nvim-🔌-plugin-spec-spec-lazy-loading*

  --------------------------------------------------------------------------------------------------------------------
  Property   Type                                                             Description
  ---------- ---------------------------------------------------------------- ----------------------------------------
  lazy       boolean?                                                         When true, the plugin will only be
                                                                              loaded when needed. Lazy-loaded plugins
                                                                              are automatically loaded when their Lua
                                                                              modules are required, or when one of the
                                                                              lazy-loading handlers triggers

  event      string? or string[] or                                           Lazy-load on event. Events can be
             fun(self:LazyPlugin, event:string[]):string[] or                 specified as BufEnter or with a pattern
             {event:string[]\|string, pattern?:string[]\|string}              like BufEnter *.lua

  cmd        string? or string[] or                                           Lazy-load on command
             fun(self:LazyPlugin, cmd:string[]):string[]                      

  ft         string? or string[] or                                           Lazy-load on filetype
             fun(self:LazyPlugin, ft:string[]):string[]                       

  keys       string? or string[] or LazyKeysSpec[] or                         Lazy-load on key mapping
             fun(self:LazyPlugin, keys:string[]):(string \| LazyKeysSpec)[]   
  --------------------------------------------------------------------------------------------------------------------
Refer to the Lazy Loading <./lazy_loading.md> section for more information.


SPEC VERSIONING                   *lazy.nvim-🔌-plugin-spec-spec-versioning*

  ------------------------------------------------------------------------------
  Property     Type                 Description
  ------------ -------------------- --------------------------------------------
  branch       string?              Branch of the repository

  tag          string?              Tag of the repository

  commit       string?              Commit of the repository

  version      string? or false to  Version to use from the repository. Full
               override the default Semver ranges are supported

  pin          boolean?             When true, this plugin will not be included
                                    in updates

  submodules   boolean?             When false, git submodules will not be
                                    fetched. Defaults to true
  ------------------------------------------------------------------------------
Refer to the Versioning <./versioning.md> section for more information.


SPEC ADVANCED                       *lazy.nvim-🔌-plugin-spec-spec-advanced*

  ----------------------------------------------------------------------------------------
  Property   Type       Description
  ---------- ---------- ------------------------------------------------------------------
  optional   boolean?   When a spec is tagged optional, it will only be included in the
                        final spec, when the same plugin has been specified at least once
                        somewhere else without optional. This is mainly useful for Neovim
                        distros, to allow setting options on plugins that may/may not be
                        part of the user’s plugins.

  specs      LazySpec   A list of plugin specs defined in the scope of the plugin. This is
                        mainly useful for Neovim distros, to allow setting options on
                        plugins that may/may not be part of the user’s plugins. When the
                        plugin is disabled, none of the scoped specs will be included in
                        the final spec. Similar to dependencies without the automatic
                        loading of the specs.

  module     false?     Do not automatically load this Lua module when it’s required
                        somewhere

  import     string?    Import the given spec module.
  ----------------------------------------------------------------------------------------

EXAMPLES                                 *lazy.nvim-🔌-plugin-spec-examples*

>lua
    return {
      -- the colorscheme should be available when starting Neovim
      {
        "folke/tokyonight.nvim",
        lazy = false, -- make sure we load this during startup if it is your main colorscheme
        priority = 1000, -- make sure to load this before all the other start plugins
        config = function()
          -- load the colorscheme here
          vim.cmd([[colorscheme tokyonight]])
        end,
      },
    
      -- I have a separate config.mappings file where I require which-key.
      -- With lazy the plugin will be automatically loaded when it is required somewhere
      { "folke/which-key.nvim", lazy = true },
    
      {
        "nvim-neorg/neorg",
        -- lazy-load on filetype
        ft = "norg",
        -- options for neorg. This will automatically call `require("neorg").setup(opts)`
        opts = {
          load = {
            ["core.defaults"] = {},
          },
        },
      },
    
      {
        "dstein64/vim-startuptime",
        -- lazy-load on a command
        cmd = "StartupTime",
        -- init is called during startup. Configuration for vim plugins typically should be set in an init function
        init = function()
          vim.g.startuptime_tries = 10
        end,
      },
    
      {
        "hrsh7th/nvim-cmp",
        -- load cmp on InsertEnter
        event = "InsertEnter",
        -- these dependencies will only be loaded when cmp loads
        -- dependencies are always lazy-loaded unless specified otherwise
        dependencies = {
          "hrsh7th/cmp-nvim-lsp",
          "hrsh7th/cmp-buffer",
        },
        config = function()
          -- ...
        end,
      },
    
      -- if some code requires a module from an unloaded plugin, it will be automatically loaded.
      -- So for api plugins like devicons, we can always set lazy=true
      { "nvim-tree/nvim-web-devicons", lazy = true },
    
      -- you can use the VeryLazy event for things that can
      -- load later and are not important for the initial UI
      { "stevearc/dressing.nvim", event = "VeryLazy" },
    
      {
        "Wansmer/treesj",
        keys = {
          { "J", "<cmd>TSJToggle<cr>", desc = "Join Toggle" },
        },
        opts = { use_default_keymaps = false, max_join_length = 150 },
      },
    
      {
        "monaqa/dial.nvim",
        -- lazy-load on keys
        -- mode is `n` by default. For more advanced options, check the section on key mappings
        keys = { "<C-a>", { "<C-x>", mode = "n" } },
      },
    
      -- local plugins need to be explicitly configured with dir
      { dir = "~/projects/secret.nvim" },
    
      -- you can use a custom url to fetch a plugin
      { url = "git@github.com:folke/noice.nvim.git" },
    
      -- local plugins can also be configured with the dev option.
      -- This will use {config.dev.path}/noice.nvim/ instead of fetching it from GitHub
      -- With the dev option, you can easily switch between the local and installed version of a plugin
      { "folke/noice.nvim", dev = true },
    }
<


LAZY LOADING                         *lazy.nvim-🔌-plugin-spec-lazy-loading*

**lazy.nvim** automagically lazy-loads Lua modules. This means that if you have
a plugin `A` that is lazy-loaded and a plugin `B` that requires a module of
plugin `A`, then plugin `A` will be loaded on demand as expected.


Additionally, you can also lazy-load on **events**, **commands**, **file
types** and **key mappings**.

Plugins will be lazy-loaded when one of the following is `true`:

- The plugin only exists as a dependency in your spec
- It has an `event`, `cmd`, `ft` or `keys` key
- `config.defaults.lazy == true`


🌈 COLORSCHEMES ~

Colorscheme plugins can be configured with `lazy=true`. The plugin will
automagically load when doing `colorscheme foobar`.



⌨️ LAZY KEY MAPPINGS ~

The `keys` property can be a `string` or `string[]` for simple normal-mode
mappings, or it can be a `LazyKeysSpec` table with the following key-value
pairs:

- **[1]**: (`string`) lhs **(required)**
- **[2]**: (`string|fun()`) rhs **(optional)**
- **mode**: (`string|string[]`) mode **(optional, defaults to "n")**
- **ft**: (`string|string[]`) `filetype` for buffer-local keymaps **(optional)**
- any other option valid for `vim.keymap.set`

Key mappings will load the plugin the first time they get executed.

When `[2]` is `nil`, then the real mapping has to be created by the `config()`
function.

>lua
    -- Example for neo-tree.nvim
    {
      "nvim-neo-tree/neo-tree.nvim",
        keys = {
          { "<leader>ft", "<cmd>Neotree toggle<cr>", desc = "NeoTree" },
        },
        opts = {},
    }
<


VERSIONING                             *lazy.nvim-🔌-plugin-spec-versioning*

If you want to install a specific revision of a plugin, you can use `commit`,
`tag`, `branch`, `version`.

The `version` property supports Semver <https://semver.org/> ranges.



EXAMPLES ~

- `*`: latest stable version (this excludes pre-release versions)
- `1.2.x`: any version that starts with `1.2`, such as `1.2.0`, `1.2.3`, etc.
- `^1.2.3`: any version that is compatible with `1.2.3`, such as `1.3.0`, `1.4.5`, etc., but not `2.0.0`.
- `~1.2.3`: any version that is compatible with `1.2.3`, such as `1.2.4`, `1.2.5`, but not `1.3.0`.
- `>1.2.3`: any version that is greater than `1.2.3`, such as `1.3.0`, `1.4.5`, etc.
- `>=1.2.3`: any version that is greater than or equal to `1.2.3`, such as `1.2.3`, `1.3.0`, `1.4.5`, etc.
- `<1.2.3`: any version that is less than `1.2.3`, such as `1.1.0`, `1.0.5`, etc.
- `<=1.2.3`: any version that is less than or equal to `1.2.3`, such as `1.2.3`, `1.1.0`, `1.0.5`, etc


==============================================================================
5. 📦 Packages                                     *lazy.nvim-📦-packages*

**lazy.nvim** supports three ways for plugins to define their dependencies and
configuration.

- **Lazy**: `lazy.lua` file
- **Rockspec**: luarocks <https://luarocks.org/> `*-scm-1.rockspec` file <https://github.com/luarocks/luarocks/wiki/Rockspec-format>
- **Packspec**: `pkg.json` (experimental, since the format <https://github.com/neovim/packspec/issues/41> is not quite there yet)

You can enable/disable package sources with `config.pkg.sources`
</configuration>. The order of sources is important, as the first source that
finds a package will be used.



LAZY                                            *lazy.nvim-📦-packages-lazy*

Using a `lazy.lua` file is the recommended way to define your plugin
dependencies and configuration. Syntax is the same as any plugin spec.


ROCKSPEC                                    *lazy.nvim-📦-packages-rockspec*

When a plugin contains a `*-1.rockspec` file, **lazy.nvim** will automatically
build the rock and its dependencies.

A **rockspec** will only be used if one of the following is true:

- the package does not have a `/lua` directory
- the package has a complex build step
- the package has dependencies (excluding `lua`)


PACKSPEC                                    *lazy.nvim-📦-packages-packspec*

Supports the pkg.json
<https://github.com/nvim-lua/nvim-package-specification/issues/41> format, with
a lazy extension in `lazy`. `lazy` can contain any valid lazy spec fields. They
will be added to the plugin’s spec.


==============================================================================
6. ⚙️ Configuration                       *lazy.nvim-⚙️-configuration*

**lazy.nvim** comes with the following defaults:

>lua
    {
      root = vim.fn.stdpath("data") .. "/lazy", -- directory where plugins will be installed
      defaults = {
        -- Set this to `true` to have all your plugins lazy-loaded by default.
        -- Only do this if you know what you are doing, as it can lead to unexpected behavior.
        lazy = false, -- should plugins be lazy-loaded?
        -- It's recommended to leave version=false for now, since a lot the plugin that support versioning,
        -- have outdated releases, which may break your Neovim install.
        version = nil, -- always use the latest git commit
        -- version = "*", -- try installing the latest stable version for plugins that support semver
        -- default `cond` you can use to globally disable a lot of plugins
        -- when running inside vscode for example
        cond = nil, ---@type boolean|fun(self:LazyPlugin):boolean|nil
      },
      -- leave nil when passing the spec as the first argument to setup()
      spec = nil, ---@type LazySpec
      local_spec = true, -- load project specific .lazy.lua spec files. They will be added at the end of the spec.
      lockfile = vim.fn.stdpath("config") .. "/lazy-lock.json", -- lockfile generated after running update.
      ---@type number? limit the maximum amount of concurrent tasks
      concurrency = jit.os:find("Windows") and (vim.uv.available_parallelism() * 2) or nil,
      git = {
        -- defaults for the `Lazy log` command
        -- log = { "--since=3 days ago" }, -- show commits from the last 3 days
        log = { "-8" }, -- show the last 8 commits
        timeout = 120, -- kill processes that take more than 2 minutes
        url_format = "https://github.com/%s.git",
        -- lazy.nvim requires git >=2.19.0. If you really want to use lazy with an older version,
        -- then set the below to false. This should work, but is NOT supported and will
        -- increase downloads a lot.
        filter = true,
        -- rate of network related git operations (clone, fetch, checkout)
        throttle = {
          enabled = false, -- not enabled by default
          -- max 2 ops every 5 seconds
          rate = 2,
          duration = 5 * 1000, -- in ms
        },
        -- Time in seconds to wait before running fetch again for a plugin.
        -- Repeated update/check operations will not run again until this
        -- cooldown period has passed.
        cooldown = 0,
      },
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
        server = "https://lumen-oss.github.io/rocks-binaries/",
        -- use hererocks to install luarocks?
        -- set to `nil` to use hererocks when luarocks is not found
        -- set to `true` to always use hererocks
        -- set to `false` to always use luarocks
        hererocks = nil,
      },
      dev = {
        -- Directory where you store your local plugin projects. If a function is used,
        -- the plugin directory (e.g. `~/projects/plugin-name`) must be returned.
        ---@type string | fun(plugin: LazyPlugin): string
        path = "~/projects",
        ---@type string[] plugins that match these patterns will use your local versions instead of being fetched from GitHub
        patterns = {}, -- For example {"folke"}
        fallback = false, -- Fallback to git when local plugin doesn't exist
      },
      install = {
        -- install missing plugins on startup. This doesn't increase startup time.
        missing = true,
        -- try to load one of these colorschemes when starting an installation during startup
        colorscheme = { "habamax" },
      },
      ui = {
        -- a number <1 is a percentage., >1 is a fixed size
        size = { width = 0.8, height = 0.8 },
        wrap = true, -- wrap the lines in the ui
        -- The border to use for the UI window. Accepts same border values as |nvim_open_win()|.
        border = "none",
        -- The backdrop opacity. 0 is fully opaque, 100 is fully transparent.
        backdrop = 60,
        title = nil, ---@type string only works when border is not "none"
        title_pos = "center", ---@type "center" | "left" | "right"
        -- Show pills on top of the Lazy window
        pills = true, ---@type boolean
        icons = {
          cmd = " ",
          config = "",
          debug = "● ",
          event = " ",
          favorite = " ",
          ft = " ",
          init = " ",
          import = " ",
          keys = " ",
          lazy = "󰒲 ",
          loaded = "●",
          not_loaded = "○",
          plugin = " ",
          runtime = " ",
          require = "󰢱 ",
          source = " ",
          start = " ",
          task = "✔ ",
          list = {
            "●",
            "➜",
            "★",
            "‒",
          },
        },
        -- leave nil, to automatically select a browser depending on your OS.
        -- If you want to use a specific browser, you can define it here
        browser = nil, ---@type string?
        throttle = 1000 / 30, -- how frequently should the ui process render events
        custom_keys = {
          -- You can define custom key maps here. If present, the description will
          -- be shown in the help menu.
          -- To disable one of the defaults, set it to false.
    
          ["<localleader>l"] = {
            function(plugin)
              require("lazy.util").float_term({ "lazygit", "log" }, {
                cwd = plugin.dir,
              })
            end,
            desc = "Open lazygit log",
          },
    
          ["<localleader>i"] = {
            function(plugin)
              Util.notify(vim.inspect(plugin), {
                title = "Inspect " .. plugin.name,
                lang = "lua",
              })
            end,
            desc = "Inspect Plugin",
          },
    
          ["<localleader>t"] = {
            function(plugin)
              require("lazy.util").float_term(nil, {
                cwd = plugin.dir,
              })
            end,
            desc = "Open terminal in plugin dir",
          },
        },
      },
      -- Output options for headless mode
      headless = {
        -- show the output from process commands like git
        process = true,
        -- show log messages
        log = true,
        -- show task start/end
        task = true,
        -- use ansi colors
        colors = true,
      },
      diff = {
        -- diff command <d> can be one of:
        -- * browser: opens the github compare view. Note that this is always mapped to <K> as well,
        --   so you can have a different command for diff <d>
        -- * git: will run git diff and open a buffer with filetype git
        -- * terminal_git: will open a pseudo terminal with git diff
        -- * diffview.nvim: will open Diffview to show the diff
        cmd = "git",
      },
      checker = {
        -- automatically check for plugin updates
        enabled = false,
        concurrency = nil, ---@type number? set to 1 to check for updates very slowly
        notify = true, -- get a notification when new updates are found
        frequency = 3600, -- check for updates every hour
        check_pinned = false, -- check for pinned packages that can't be updated
      },
      change_detection = {
        -- automatically check for config file changes and reload the ui
        enabled = true,
        notify = true, -- get a notification when changes are found
      },
      performance = {
        cache = {
          enabled = true,
        },
        reset_packpath = true, -- reset the package path to improve startup time
        rtp = {
          reset = true, -- reset the runtime path to $VIMRUNTIME and your config directory
          ---@type string[]
          paths = {}, -- add any custom paths here that you want to includes in the rtp
          ---@type string[] list any plugins you want to disable here
          disabled_plugins = {
            -- "gzip",
            -- "matchit",
            -- "matchparen",
            -- "netrwPlugin",
            -- "tarPlugin",
            -- "tohtml",
            -- "tutor",
            -- "zipPlugin",
          },
        },
      },
      -- lazy can generate helptags from the headings in markdown readme files,
      -- so :help works even for plugins that don't have vim docs.
      -- when the readme opens with :help it will be correctly displayed as markdown
      readme = {
        enabled = true,
        root = vim.fn.stdpath("state") .. "/lazy/readme",
        files = { "README.md", "lua/**/README.md" },
        -- only generate markdown helptags for plugins that don't have docs
        skip_if_doc_exists = true,
      },
      state = vim.fn.stdpath("state") .. "/lazy/state.json", -- state info for checker and other things
      -- Enable profiling of lazy.nvim. This will add some overhead,
      -- so only enable this when you are debugging lazy.nvim
      profiling = {
        -- Enables extra stats on the debug tab related to the loader cache.
        -- Additionally gathers stats about all package.loaders
        loader = false,
        -- Track each new require in the Lazy profiling tab
        require = false,
      },
    }
<

If you don’t want to use a Nerd Font, you can replace the icons with Unicode symbols. ~

>lua
    {
      ui = {
        icons = {
          cmd = "⌘",
          config = "🛠",
          event = "📅",
          ft = "📂",
          init = "⚙",
          keys = "🗝",
          plugin = "🔌",
          runtime = "💻",
          require = "🌙",
          source = "📄",
          start = "🚀",
          task = "📌",
          lazy = "💤 ",
        },
      },
    }
<


🌈 HIGHLIGHT GROUPS   *lazy.nvim-⚙️-configuration-🌈-highlight-groups*

  -----------------------------------------------------------------------
  Highlight Group         Default Group           Description
  ----------------------- ----------------------- -----------------------
  LazyBold                { bold = true }         

  LazyButton              CursorLine              

  LazyButtonActive        Visual                  

  LazyComment             Comment                 

  LazyCommit              @variable.builtin       commit ref

  LazyCommitIssue         Number                  

  LazyCommitScope         Italic                  conventional commit
                                                  scope

  LazyCommitType          Title                   conventional commit
                                                  type

  LazyDimmed              Conceal                 property

  LazyDir                 @markup.link            directory

  LazyError               DiagnosticError         task errors

  LazyH1                  IncSearch               home button

  LazyH2                  Bold                    titles

  LazyInfo                DiagnosticInfo          task errors

  LazyItalic              { italic = true }       

  LazyLocal               Constant                

  LazyNoCond              DiagnosticWarn          unloaded icon for a
                                                  plugin where cond() was
                                                  false

  LazyNormal              NormalFloat             

  LazyProgressDone        Constant                progress bar done

  LazyProgressTodo        LineNr                  progress bar todo

  LazyProp                Conceal                 property

  LazyReasonCmd           Operator                

  LazyReasonEvent         Constant                

  LazyReasonFt            Character               

  LazyReasonImport        Identifier              

  LazyReasonKeys          Statement               

  LazyReasonPlugin        Special                 

  LazyReasonRequire       @variable.parameter     

  LazyReasonRuntime       @macro                  

  LazyReasonSource        Character               

  LazyReasonStart         @variable.member        

  LazySpecial             @punctuation.special    

  LazyTaskOutput          MsgArea                 task output

  LazyUrl                 @markup.link            url

  LazyValue               @string                 value of a property

  LazyWarning             DiagnosticWarn          task errors
  -----------------------------------------------------------------------

==============================================================================
7. 🚀 Usage                                           *lazy.nvim-🚀-usage*


▶️ STARTUP SEQUENCE         *lazy.nvim-🚀-usage-▶️-startup-sequence*

**lazy.nvim** does **NOT** use Neovim packages and even disables plugin loading
completely (`vim.go.loadplugins = false`). It takes over the complete startup
sequence for more flexibility and better performance.

In practice this means that step 10 of |Neovim Initialization| is done by Lazy:

1. All the plugins’ `init()` functions are executed
2. All plugins with `lazy=false` are loaded. This includes sourcing `/plugin` and `/ftdetect` files. (`/after` will not be sourced yet)
3. All files from `/plugin` and `/ftdetect` directories in your rtp are sourced (excluding `/after`)
4. All `/after/plugin` files are sourced (this includes `/after` from plugins)

Files from runtime directories are always sourced in alphabetical order.


🚀 COMMANDS                             *lazy.nvim-🚀-usage-🚀-commands*

Plugins are managed with the `:Lazy` command. Open the help with `<?>` to see
all the key mappings.

You can press `<CR>` on a plugin to show its details. Most properties can be
hovered with `<K>` to open links, help files, readmes, git commits and git
issues.

Lazy can automatically check for updates in the background. This feature can be
enabled with `config.checker.enabled = true`.

Any operation can be started from the UI, with a sub command or an API
function:

  ----------------------------------------------------------------------------------
  Command                   Lua                              Description
  ------------------------- -------------------------------- -----------------------
  :Lazy build {plugins}     require("lazy").build(opts)      Rebuild a plugin

  :Lazy check [plugins]     require("lazy").check(opts?)     Check for updates and
                                                             show the log (git
                                                             fetch)

  :Lazy clean [plugins]     require("lazy").clean(opts?)     Clean plugins that are
                                                             no longer needed

  :Lazy clear               require("lazy").clear()          Clear finished tasks

  :Lazy debug               require("lazy").debug()          Show debug information

  :Lazy health              require("lazy").health()         Run :checkhealth lazy

  :Lazy help                require("lazy").help()           Toggle this help page

  :Lazy home                require("lazy").home()           Go back to plugin list

  :Lazy install [plugins]   require("lazy").install(opts?)   Install missing plugins

  :Lazy load {plugins}      require("lazy").load(opts)       Load a plugin that has
                                                             not been loaded yet.
                                                             Similar to :packadd.
                                                             Like
                                                             :Lazy load foo.nvim.
                                                             Use :Lazy! load to skip
                                                             cond checks.

  :Lazy log [plugins]       require("lazy").log(opts?)       Show recent updates

  :Lazy profile             require("lazy").profile()        Show detailed profiling

  :Lazy reload {plugins}    require("lazy").reload(opts)     Reload a plugin
                                                             (experimental!!)

  :Lazy restore [plugins]   require("lazy").restore(opts?)   Updates all plugins to
                                                             the state in the
                                                             lockfile. For a single
                                                             plugin: restore it to
                                                             the state in the
                                                             lockfile or to a given
                                                             commit under the cursor

  :Lazy sync [plugins]      require("lazy").sync(opts?)      Run install, clean and
                                                             update

  :Lazy update [plugins]    require("lazy").update(opts?)    Update plugins. This
                                                             will also update the
                                                             lockfile
  ----------------------------------------------------------------------------------
Any command can have a **bang** to make the command wait till it finished. For
example, if you want to sync lazy from the cmdline, you can use:

>shell
    nvim --headless "+Lazy! sync" +qa
<

`opts` is a table with the following key-values:

- **wait**: when true, then the call will wait till the operation completed
- **show**: when false, the UI will not be shown
- **plugins**: a list of plugin names to run the operation on
- **concurrency**: limit the `number` of concurrently running tasks

Stats API (`require("lazy").stats()`):

>lua
    {
      -- startuptime in milliseconds till UIEnter
      startuptime = 0,
      -- when true, startuptime is the accurate cputime for the Neovim process. (Linux & macOS)
      -- this is more accurate than `nvim --startuptime`, and as such will be slightly higher
      -- when false, startuptime is calculated based on a delta with a timestamp when lazy started.
      real_cputime = false,
      count = 0, -- total number of plugins
      loaded = 0, -- number of loaded plugins
      ---@type table<string, number>
      times = {},
    }
<

**lazy.nvim** provides a statusline component that you can use to show the
number of pending updates. Make sure to enable `config.checker.enabled = true`
to make this work.

Example of configuring lualine.nvim ~

>lua
    require("lualine").setup({
      sections = {
        lualine_x = {
          {
            require("lazy.status").updates,
            cond = require("lazy.status").has_updates,
            color = { fg = "#ff9e64" },
          },
        },
      },
    })
<


📆 USER EVENTS                       *lazy.nvim-🚀-usage-📆-user-events*

The following user events will be triggered:

- **LazyDone**: when lazy has finished starting up and loaded your config
- **LazySync**: after running sync
- **LazyInstall**: after an install
- **LazyUpdate**: after an update
- **LazyClean**: after a clean
- **LazyCheck**: after checking for updates
- **LazyLog**: after running log
- **LazyLoad**: after loading a plugin. The `data` attribute will contain the plugin name.
- **LazySyncPre**: before running sync
- **LazyInstallPre**: before an install
- **LazyUpdatePre**: before an update
- **LazyCleanPre**: before a clean
- **LazyCheckPre**: before checking for updates
- **LazyLogPre**: before running log
- **LazyReload**: triggered by change detection after reloading plugin specs
- **VeryLazy**: triggered after `LazyDone` and processing `VimEnter` auto commands
- **LazyVimStarted**: triggered after `UIEnter` when `require("lazy").stats().startuptime` has been calculated.
    Useful to update the startuptime on your dashboard.


❌ UNINSTALLING                       *lazy.nvim-🚀-usage-❌-uninstalling*

To uninstall **lazy.nvim**, you need to remove the following files and
directories:

- **data**: `~/.local/share/nvim/lazy`
- **state**: `~/.local/state/nvim/lazy`
- **lockfile**: `~/.config/nvim/lazy-lock.json`


  Paths can differ if you changed `XDG` environment variables.

🔒 LOCKFILE                             *lazy.nvim-🚀-usage-🔒-lockfile*

After every **update**, the local lockfile (`lazy-lock.json`) is updated with
the installed revisions. It is recommended to have this file under version
control.

If you use your Neovim config on multiple machines, using the lockfile, you can
ensure that the same version of every plugin is installed.

If you are on another machine, you can do `:Lazy restore`, to update all your
plugins to the version from the lockfile.


📦 MIGRATION GUIDE               *lazy.nvim-🚀-usage-📦-migration-guide*


PACKER.NVIM ~

- `setup` ➡️ `init`
- `requires` ➡️ `dependencies`
- `as` ➡️ `name`
- `opt` ➡️ `lazy`
- `run` ➡️ `build`
- `lock` ➡️ `pin`
- `disable=true` ➡️ `enabled = false`
- `tag='*'` ➡️ `version="*"`
- `after` is **not needed** for most use-cases. Use `dependencies` otherwise.
- `wants` is **not needed** for most use-cases. Use `dependencies` otherwise.
- `config` don’t support string type, use `fun(LazyPlugin)` instead.
- `module` is auto-loaded. No need to specify
- `keys` spec is |lazy.nvim-different|
- `rtp` can be accomplished with:

>lua
    config = function(plugin)
        vim.opt.rtp:append(plugin.dir .. "/custom-rtp")
    end
<

With packer `wants`, `requires` and `after` can be used to manage dependencies.
With lazy, this isn’t needed for most of the Lua dependencies. They can be
installed just like normal plugins (even with `lazy=true`) and will be loaded
when other plugins need them. The `dependencies` key can be used to group those
required plugins with the one that requires them. The plugins which are added
as `dependencies` will always be lazy-loaded and loaded when the plugin is
loaded.


PAQ-NVIM ~

- `as` ➡️ `name`
- `opt` ➡️ `lazy`
- `run` ➡️ `build`


⚡ PROFILING & DEBUG             *lazy.nvim-🚀-usage-⚡-profiling-&-debug*

Great care has been taken to make the startup code (`lazy.core`) as efficient
as possible. During startup, all Lua files used before `VimEnter` or
`BufReadPre` are byte-compiled and cached, similar to what impatient.nvim
<https://github.com/lewis6991/impatient.nvim> does.

My config for example loads in about `11ms` with `93` plugins. I do a lot of
lazy-loading though :)

**lazy.nvim** comes with an advanced profiler `:Lazy profile` to help you
improve performance. The profiling view shows you why and how long it took to
load your plugins.


🐛 DEBUG ~

See an overview of active lazy-loading handlers and what’s in the module
cache.


📂 STRUCTURING YOUR PLUGINS*lazy.nvim-🚀-usage-📂-structuring-your-plugins*

Some users may want to split their plugin specs in multiple files. Instead of
passing a spec table to `setup()`, you can use a Lua module. The specs from the
**module** and any top-level **sub-modules** will be merged together in the
final spec, so it is not needed to add `require` calls in your main plugin file
to the other files.

The benefits of using this approach:

- Simple to **add** new plugin specs. Just create a new file in your plugins module.
- Allows for **caching** of all your plugin specs. This becomes important if you have a lot of smaller plugin specs.
- Spec changes will automatically be **reloaded** when they’re updated, so the `:Lazy` UI is always up to date.

Example:

- `~/.config/nvim/init.lua`

>lua
    require("lazy").setup("plugins")
<

- `~/.config/nvim/lua/plugins.lua` or `~/.config/nvim/lua/plugins/init.lua` **(this file is optional)**

>lua
    return {
      "folke/neodev.nvim",
      "folke/which-key.nvim",
      { "folke/neoconf.nvim", cmd = "Neoconf" },
    }
<

- Any lua file in `~/.config/nvim/lua/plugins/*.lua` will be automatically merged in the main plugin spec

For a real-life example, you can check LazyVim
<https://github.com/LazyVim/LazyVim> and more specifically:

- lazyvim.plugins <https://github.com/LazyVim/LazyVim/tree/main/lua/lazyvim/plugins> contains all the plugin specs that will be loaded


↩️ IMPORTING SPECS, CONFIG & OPTS

As part of a spec, you can add `import` statements to import additional plugin
modules. Both of the `setup()` calls are equivalent:

>lua
    require("lazy").setup("plugins")
    
    -- Same as:
    require("lazy").setup({{import = "plugins"}})
<

To import multiple modules from a plugin, add additional specs for each import.
For example, to import LazyVim core plugins and an optional plugin:

>lua
    require("lazy").setup({
      spec = {
        { "LazyVim/LazyVim", import = "lazyvim.plugins" },
        { import = "lazyvim.plugins.extras.coding.copilot" },
      }
    })
<

When you import specs, you can override them by simply adding a spec for the
same plugin to your local specs, adding any keys you want to override / merge.

`opts`, `dependencies`, `cmd`, `event`, `ft` and `keys` are always merged with
the parent spec. Any other property will override the property from the parent
spec.


==============================================================================
8. 🔥 Developers                                 *lazy.nvim-🔥-developers*

To make it easier for users to install your plugin, you can include a package
spec </packages> in your repo.


BEST PRACTICES                      *lazy.nvim-🔥-developers-best-practices*

- If your plugin needs `setup()`, then create a simple `lazy.lua` file like this:
    >lua
          return { "me/my-plugin", opts = {} }
    <
- Plugins that are pure lua libraries should be lazy-loaded with `lazy = true`.
    >lua
        { "nvim-lua/plenary.nvim", lazy = true }
    <
- Always use `opts` instead of `config` when possible. `config` is almost never
    needed.
- Only use `dependencies` if a plugin needs the dep to be installed **AND**
    loaded. Lua plugins/libraries are automatically loaded when they are
    `require()`d, so they don’t need to be in `dependencies`.
- Inside a `build` function or `*.lua` build file, use
    `coroutine.yield(msg:string|LazyMsg)` to show progress.
- Don’t change the `cwd` in your build function, since builds run in parallel
    and changing the `cwd` will affect other builds.


BUILDING                                  *lazy.nvim-🔥-developers-building*

The spec **build** property can be one of the following:

- `fun(plugin: LazyPlugin)`: a function that builds the plugin.
- `*.lua`: a Lua file that builds the plugin (like `build.lua`)
- `":Command"`: a Neovim command
- `"rockspec"`: this will run `luarocks make` in the plugin’s directory
    This is automatically set by the `rockspec` package </packages> source.
- any other **string** will be run as a shell command
- a `list` of any of the above to run multiple build steps
- if no `build` is specified, but a `build.lua` file exists, that will be used instead.

Build functions and `*.lua` files run asynchronously in a coroutine. Use
`coroutine.yield(msg:string|LazyMsg)` to show progress.

Yielding will also schedule the next `coroutine.resume()` to run in the next
tick, so you can do long-running tasks without blocking Neovim.

>lua
    ---@class LazyMsg
    ---@field msg string
    ---@field level? number vim.log.levels.XXX
<

Use `vim.log.levels.TRACE` to only show the message as a **status** message for
the task.



MINIT (MINIMAL INIT)          *lazy.nvim-🔥-developers-minit-(minimal-init)*

**lazy.nvim** comes with some built-in functionality to help you create a
minimal init for your plugin.

I mainly use this for testing and for users to create a `repro.lua`.

When running in **headless** mode, **lazy.nvim** will log any messages to the
terminal. See `opts.headless` for more info.

**minit** will install/load all your specs and will always run an update as
well.


BOOTSTRAP ~

>lua
    -- setting this env will override all XDG paths
    vim.env.LAZY_STDPATH = ".tests"
    -- this will install lazy in your stdpath
    load(vim.fn.system("curl -s https://raw.githubusercontent.com/folke/lazy.nvim/main/bootstrap.lua"))()
<


TESTING WITH BUSTED ~

This will add `"lunarmodules/busted"`, configure `hererocks` and run `busted`.

Below is an example of how I use **minit** to run tests with busted
<https://olivinelabs.com/busted/> in **LazyVim**.

>lua
    #!/usr/bin/env -S nvim -l
    
    vim.env.LAZY_STDPATH = ".tests"
    load(vim.fn.system("curl -s https://raw.githubusercontent.com/folke/lazy.nvim/main/bootstrap.lua"))()
    
    -- Setup lazy.nvim
    require("lazy.minit").busted({
      spec = {
        "LazyVim/starter",
        "williamboman/mason-lspconfig.nvim",
        "williamboman/mason.nvim",
        "nvim-treesitter/nvim-treesitter",
      },
    })
<

To use this, you can run:

>sh
    nvim -l ./tests/busted.lua tests
<

If you want to inspect the test environment, run:

>sh
    nvim -u ./tests/busted.lua
<


REPRO.LUA ~

>lua
    vim.env.LAZY_STDPATH = ".repro"
    load(vim.fn.system("curl -s https://raw.githubusercontent.com/folke/lazy.nvim/main/bootstrap.lua"))()
    
    require("lazy.minit").repro({
      spec = {
        "stevearc/conform.nvim",
        "nvim-neotest/nvim-nio",
      },
    })
    
    -- do anything else you need to do to reproduce the issue
<

Then run it with:

>sh
    nvim -u repro.lua
<

==============================================================================
9. Links                                                     *lazy.nvim-links*

1. *image*: https://user-images.githubusercontent.com/292349/208301737-68fb279c-ba70-43ef-a369-8c3e8367d6b1.png
2. *image*: https://user-images.githubusercontent.com/292349/208301766-5c400561-83c3-4811-9667-1ec4bb3c43b8.png
3. *image*: https://user-images.githubusercontent.com/292349/208301790-7eedbfa5-d202-4e70-852e-de68aa47233b.png

Generated by panvimdoc <https://github.com/kdheepak/panvimdoc>

vim:tw=78:ts=8:noet:ft=help:norl:
```

## File: `lua/lazy/async.lua`
```
local Util = require("lazy.core.util")

local M = {}

---@type Async[]
M._active = {}
---@type Async[]
M._suspended = {}
M._executor = assert(vim.loop.new_check())

M.BUDGET = 10

---@type table<thread, Async>
M._threads = setmetatable({}, { __mode = "k" })

---@alias AsyncEvent "done" | "error" | "yield" | "ok"

---@class Async
---@field _co thread
---@field _fn fun()
---@field _suspended? boolean
---@field _on table<AsyncEvent, fun(res:any, async:Async)[]>
local Async = {}

---@param fn async fun()
---@return Async
function Async.new(fn)
  local self = setmetatable({}, { __index = Async })
  return self:init(fn)
end

---@param fn async fun()
---@return Async
function Async:init(fn)
  self._fn = fn
  self._on = {}
  self._co = coroutine.create(function()
    local ok, err = pcall(self._fn)
    if not ok then
      self:_emit("error", err)
    end
    self:_emit("done")
  end)
  M._threads[self._co] = self
  return M.add(self)
end

---@param event AsyncEvent
---@param cb async fun(res:any, async:Async)
function Async:on(event, cb)
  self._on[event] = self._on[event] or {}
  table.insert(self._on[event], cb)
  return self
end

---@private
---@param event AsyncEvent
---@param res any
function Async:_emit(event, res)
  for _, cb in ipairs(self._on[event] or {}) do
    cb(res, self)
  end
end

function Async:running()
  return coroutine.status(self._co) ~= "dead"
end

---@async
function Async:sleep(ms)
  vim.defer_fn(function()
    self:resume()
  end, ms)
  self:suspend()
end

---@async
---@param yield? boolean
function Async:suspend(yield)
  self._suspended = true
  if coroutine.running() == self._co and yield ~= false then
    M.yield()
  end
end

function Async:resume()
  self._suspended = false
  M._run()
end

---@async
---@param yield? boolean
function Async:wake(yield)
  local async = M.running()
  assert(async, "Not in an async context")
  self:on("done", function()
    async:resume()
  end)
  async:suspend(yield)
end

---@async
function Async:wait()
  if coroutine.running() == self._co then
    error("Cannot wait on self")
  end

  local async = M.running()
  if async then
    self:wake()
  else
    while self:running() do
      vim.wait(10)
    end
  end
  return self
end

function Async:step()
  if self._suspended then
    return true
  end
  local status = coroutine.status(self._co)
  if status == "suspended" then
    local ok, res = coroutine.resume(self._co)
    if not ok then
      error(res)
    elseif res then
      self:_emit("yield", res)
    end
  end
  return self:running()
end

function M.abort()
  for _, async in ipairs(M._active) do
    coroutine.resume(async._co, "abort")
  end
end

function M.yield()
  if coroutine.yield() == "abort" then
    error("aborted", 2)
  end
end

function M.step()
  local start = vim.uv.hrtime()
  for _ = 1, #M._active do
    if Util.exiting() or vim.uv.hrtime() - start > M.BUDGET * 1e6 then
      break
    end

    local state = table.remove(M._active, 1)
    if state:step() then
      if state._suspended then
        table.insert(M._suspended, state)
      else
        table.insert(M._active, state)
      end
    end
  end
  for _ = 1, #M._suspended do
    local state = table.remove(M._suspended, 1)
    table.insert(state._suspended and M._suspended or M._active, state)
  end

  -- M.debug()
  if #M._active == 0 or Util.exiting() then
    return M._executor:stop()
  end
end

function M.debug()
  local lines = {
    "- active: " .. #M._active,
    "- suspended: " .. #M._suspended,
  }
  for _, async in ipairs(M._active) do
    local info = debug.getinfo(async._fn)
    local file = vim.fn.fnamemodify(info.short_src:sub(1), ":~:.")
    table.insert(lines, ("%s:%d"):format(file, info.linedefined))
    if #lines > 10 then
      break
    end
  end
  local msg = table.concat(lines, "\n")
  M._notif = vim.notify(msg, nil, { replace = M._notif })
end

---@param async Async
function M.add(async)
  table.insert(M._active, async)
  M._run()
  return async
end

function M._run()
  if not Util.exiting() and not M._executor:is_active() then
    M._executor:start(vim.schedule_wrap(M.step))
  end
end

function M.running()
  local co = coroutine.running()
  if co then
    return M._threads[co]
  end
end

---@async
---@param ms number
function M.sleep(ms)
  local async = M.running()
  assert(async, "Not in an async context")
  async:sleep(ms)
end

M.Async = Async
M.new = Async.new

return M
```

## File: `lua/lazy/build.lua`
```
vim.opt.rtp:append(".")
local Rocks = require("lazy.pkg.rockspec")
local Semver = require("lazy.manage.semver")
local Util = require("lazy.util")

local M = {}

M.patterns = { "nvim", "treesitter", "tree-sitter", "cmp", "neo" }
local manifest_file = "build/manifest.lua"

function M.fetch(url, file, prefix)
  if not vim.uv.fs_stat(file) then
    print((prefix or "") .. "Fetching " .. url .. " to " .. file .. "\n")
    vim.cmd.redraw()
    local out = vim.fn.system("wget " .. url .. " -O " .. file)
    if vim.v.shell_error ~= 0 then
      pcall(vim.uv.fs_unlink, file)
      error("Failed to fetch " .. url .. ":\n" .. out)
    end
  end
end

function M.split()
  local lines = vim.fn.readfile(manifest_file)
  local id = 0
  local files = {} ---@type string[]
  while #lines > 0 do
    id = id + 1
    local part_file = "build/manifest-part-" .. id .. ".lua"
    local idx = math.min(#lines, 30000)
    while idx < #lines and not lines[idx]:match("^   },$") do
      idx = idx + 1
    end
    local part_lines = vim.list_slice(lines, 1, idx)
    if idx ~= #lines then
      part_lines[#part_lines] = "   }}"
    end
    vim.fn.writefile(part_lines, part_file)
    files[#files + 1] = part_file
    print("Wrote " .. part_file .. "\n")

    lines = vim.list_slice(lines, idx + 1)
    if #lines == 0 then
      break
    end
    lines[1] = "repository = { " .. lines[1]
  end
  return files
end

---@return RockManifest?
function M.fetch_manifest()
  M.fetch("https://luarocks.org/manifest-5.1", manifest_file)
  local ret = { repository = {} }
  for _, file in ipairs(M.split()) do
    local part = Rocks.parse(file)
    print(vim.tbl_count(part.repository or {}) .. " rocks in " .. file .. "\n")
    for k, v in pairs(part.repository or {}) do
      ret.repository[k] = v
    end
  end
  return ret
end

function M.fetch_rockspec(name, version, prefix)
  version = version or "scm-1"
  local url = "https://luarocks.org/" .. name .. "-" .. version .. ".rockspec"
  M.fetch(url, "build/" .. name .. ".rockspec", prefix)
end

function M.build()
  vim.fn.mkdir("build", "p")
  local manifest = M.fetch_manifest() or {}
  ---@type {name:string, version:string, url:string}[]
  local nvim_rocks = {}
  print(vim.tbl_count(manifest.repository or {}) .. " rocks in manifest\n")
  for rock, vv in pairs(manifest.repository or {}) do
    local matches = false
    for _, pattern in ipairs(M.patterns) do
      if rock:find(pattern, 1, true) then
        matches = true
        break
      end
    end
    if matches then
      local versions = vim.tbl_map(Semver.version, vim.tbl_keys(vv))
      versions = vim.tbl_filter(function(v)
        return not not v
      end, versions)
      local last = Semver.last(versions) or next(vv)
      last = type(last) == "table" and last.input or last
      table.insert(nvim_rocks, { name = rock, version = last })
    end
  end
  table.sort(nvim_rocks, function(a, b)
    return a.name < b.name
  end)

  for r, rock in ipairs(nvim_rocks) do
    local progress = string.format("[%d/%d] ", r, #nvim_rocks)
    local ok, err = pcall(M.fetch_rockspec, rock.name, rock.version, progress)
    if not ok then
      err = vim.trim("Error: " .. err)
      local lines = vim.split(err, "\n")
      lines = vim.tbl_map(function(line)
        return "    " .. line
      end, lines)
      print(table.concat(lines, "\n") .. "\n")
    end
  end

  for _, rock in ipairs(nvim_rocks) do
    local rockspec = Rocks.rockspec("build/" .. rock.name .. ".rockspec")
    if rockspec then
      local url = rockspec.source and rockspec.source.url
      -- parse github short url
      if url and url:find("://github.com/") then
        url = url:gsub("^.*://github.com/", "")
        local parts = vim.split(url, "/")
        url = parts[1] .. "/" .. parts[2]
        url = url:gsub("%.git$", "")
      end
      if url then
        rock.url = url
        print(rock.name .. " " .. url)
      else
        print("Error: " .. rock.name .. " missing source url\n\n")
        print(vim.inspect(rockspec) .. "\n")
      end
    end
  end
  Util.write_file("lua/lazy/community/_generated.lua", "return \n" .. vim.inspect(nvim_rocks))
end

M.build()

return M
```

## File: `lua/lazy/docs.lua`
```
local Util = require("lazy.util")

local M = {}

function M.indent(str, indent)
  local lines = vim.split(str, "\n")
  for l, line in ipairs(lines) do
    lines[l] = (" "):rep(indent) .. line
  end
  return table.concat(lines, "\n")
end

---@param str string
function M.fix_indent(str)
  local lines = vim.split(str, "\n")

  local first = table.remove(lines, 1)

  local width = 120
  for _, line in ipairs(lines) do
    if not line:find("^%s*$") then
      width = math.min(width, #line:match("^%s*"))
    end
  end

  for l, line in ipairs(lines) do
    lines[l] = line:sub(width + 1)
  end
  table.insert(lines, 1, first)
  return table.concat(lines, "\n")
end

---@alias ReadmeBlock {content:string, lang?:string}
---@param contents table<string, ReadmeBlock|string>
---@param readme_file? string
function M.save(contents, readme_file)
  local readme = Util.read_file(readme_file or "README.md")
  for tag, block in pairs(contents) do
    if type(block) == "string" then
      block = { content = block, lang = "lua" }
    end
    ---@cast block ReadmeBlock
    local content = M.fix_indent(block.content)
    content = content:gsub("%%", "%%%%")
    content = vim.trim(content)
    local pattern = "(<%!%-%- " .. tag .. ":start %-%->).*(<%!%-%- " .. tag .. ":end %-%->)"
    if not readme:find(pattern) then
      error("tag " .. tag .. " not found")
    end
    if block.lang then
      readme = readme:gsub(pattern, "%1\n\n```" .. block.lang .. "\n" .. content .. "\n```\n\n%2")
    else
      readme = readme:gsub(pattern, "%1\n\n" .. content .. "\n\n%2")
    end
  end

  Util.write_file(readme_file or "README.md", readme)
  vim.cmd.checktime()
end

---@return string
function M.extract(file, pattern)
  local init = Util.read_file(file)
  local ret = assert(init:match(pattern)) --[[@as string]]
  local lines = vim.tbl_filter(function(line)
    return not line:find("^%s*%-%-%s*stylua%s*:%s*ignore%s*$")
  end, vim.split(ret, "\n"))
  return table.concat(lines, "\n")
end

---@return ReadmeBlock
function M.commands()
  local commands = require("lazy.view.commands").commands
  local modes = require("lazy.view.config").commands
  modes.load.opts = true
  local lines = {
    { "Command", "Lua", "Description" },
    { "---", "---", "---" },
  }
  Util.foreach(modes, function(name, mode)
    if commands[name] then
      if mode.plugins_required then
        lines[#lines + 1] = {
          ("`:Lazy %s {plugins}`"):format(name),
          ([[`require("lazy").%s(opts)`]]):format(name),
          mode.desc,
        }
      elseif mode.plugins then
        lines[#lines + 1] = {
          ("`:Lazy %s [plugins]`"):format(name),
          ([[`require("lazy").%s(opts?)`]]):format(name),
          mode.desc,
        }
      else
        lines[#lines + 1] = {
          ("`:Lazy %s`"):format(name),
          ([[`require("lazy").%s()`]]):format(name),
          mode.desc,
        }
      end
    end
  end)
  return { content = M.table(lines) }
end

---@param lines string[][]
function M.table(lines)
  ---@type string[]
  local ret = {}
  for _, line in ipairs(lines) do
    ret[#ret + 1] = "| " .. table.concat(line, " | ") .. " |"
  end
  return table.concat(ret, "\n")
end

---@param opts? {name?:string, path?:string, modname?:string}
---@return ReadmeBlock
function M.colors(opts)
  opts = vim.tbl_extend("force", {
    name = "Lazy",
    path = "lua/lazy/view/colors.lua",
    modname = "lazy.view.colors",
  }, opts or {})
  local str = M.extract(opts.path, "\nM%.colors = ({.-\n})")
  ---@type table<string,string>
  local comments = {}
  for _, line in ipairs(vim.split(str, "\n")) do
    local group, desc = line:match("^  (%w+) = .* -- (.*)")
    if group then
      comments[group] = desc
    end
  end
  local lines = {
    { "Highlight Group", "Default Group", "Description" },
    { "---", "---", "---" },
  }
  Util.foreach(require(opts.modname).colors, function(group, link)
    link = type(link) == "table" and "`" .. vim.inspect(link):gsub("%s+", " ") .. "`" or "***" .. link .. "***"
    lines[#lines + 1] = { "**" .. opts.name .. group .. "**", link, comments[group] or "" }
  end)
  return { content = M.table(lines) }
end

function M.update()
  local config = M.extract("lua/lazy/core/config.lua", "\nM%.defaults = ({.-\n})")
  config = config:gsub("%s*debug = false.\n", "\n")
  M.save({
    bootstrap = M.extract("lua/lazy/init.lua", "function M%.bootstrap%(%)\n(.-)\nend"),
    stats = M.extract("lua/lazy/stats.lua", "\nM%._stats = ({.-\n})"),
    config = config,
    spec = Util.read_file("lua/lazy/example.lua"),
    commands = M.commands(),
    colors = M.colors(),
  })
end

---@param plugins? LazyPlugin[]
---@return ReadmeBlock
function M.plugins(plugins)
  plugins = plugins or require("lazy.core.config").plugins
  ---@type string[]
  local lines = {}
  Util.foreach(plugins, function(name, plugin)
    if plugin.url then
      lines[#lines + 1] = "- [" .. name .. "](" .. plugin.url:gsub("%.git$", "") .. ")"
    end
  end)
  return { content = table.concat(lines, "\n") }
end

return M
```

## File: `lua/lazy/example.lua`
```
return {
  -- the colorscheme should be available when starting Neovim
  {
    "folke/tokyonight.nvim",
    lazy = false, -- make sure we load this during startup if it is your main colorscheme
    priority = 1000, -- make sure to load this before all the other start plugins
    config = function()
      -- load the colorscheme here
      vim.cmd([[colorscheme tokyonight]])
    end,
  },

  -- I have a separate config.mappings file where I require which-key.
  -- With lazy the plugin will be automatically loaded when it is required somewhere
  { "folke/which-key.nvim", lazy = true },

  {
    "nvim-neorg/neorg",
    -- lazy-load on filetype
    ft = "norg",
    -- options for neorg. This will automatically call `require("neorg").setup(opts)`
    opts = {
      load = {
        ["core.defaults"] = {},
      },
    },
  },

  {
    "dstein64/vim-startuptime",
    -- lazy-load on a command
    cmd = "StartupTime",
    -- init is called during startup. Configuration for vim plugins typically should be set in an init function
    init = function()
      vim.g.startuptime_tries = 10
    end,
  },

  {
    "hrsh7th/nvim-cmp",
    -- load cmp on InsertEnter
    event = "InsertEnter",
    -- these dependencies will only be loaded when cmp loads
    -- dependencies are always lazy-loaded unless specified otherwise
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
    },
    config = function()
      -- ...
    end,
  },

  -- if some code requires a module from an unloaded plugin, it will be automatically loaded.
  -- So for api plugins like devicons, we can always set lazy=true
  { "nvim-tree/nvim-web-devicons", lazy = true },

  -- you can use the VeryLazy event for things that can
  -- load later and are not important for the initial UI
  { "stevearc/dressing.nvim", event = "VeryLazy" },

  {
    "Wansmer/treesj",
    keys = {
      { "J", "<cmd>TSJToggle<cr>", desc = "Join Toggle" },
    },
    opts = { use_default_keymaps = false, max_join_length = 150 },
  },

  {
    "monaqa/dial.nvim",
    -- lazy-load on keys
    -- mode is `n` by default. For more advanced options, check the section on key mappings
    keys = { "<C-a>", { "<C-x>", mode = "n" } },
  },

  -- local plugins need to be explicitly configured with dir
  { dir = "~/projects/secret.nvim" },

  -- you can use a custom url to fetch a plugin
  { url = "git@github.com:folke/noice.nvim.git" },

  -- local plugins can also be configured with the dev option.
  -- This will use {config.dev.path}/noice.nvim/ instead of fetching it from GitHub
  -- With the dev option, you can easily switch between the local and installed version of a plugin
  { "folke/noice.nvim", dev = true },
}
```

## File: `lua/lazy/health.lua`
```
local Config = require("lazy.core.config")
local Process = require("lazy.manage.process")
local uv = vim.uv or vim.loop

local M = {}

-- "report_" prefix has been deprecated, use the recommended replacements if they exist.
local start = vim.health.start or vim.health.report_start
local ok = vim.health.ok or vim.health.report_ok
local warn = vim.health.warn or vim.health.report_warn
local error = vim.health.error or vim.health.report_error
local info = vim.health.info or vim.health.report_info

---@class LazyHealth
---@field error? fun(msg:string)
---@field warn? fun(msg:string)
---@field ok? fun(msg:string)

---@class LazyHealthHave : LazyHealth
---@field version? string
---@field version_pattern? string
---@field optional? boolean

---@param cmd string|string[]
---@param opts? LazyHealthHave
function M.have(cmd, opts)
  opts = vim.tbl_extend("force", {
    error = error,
    warn = warn,
    ok = ok,
    version = "--version",
  }, opts or {})

  cmd = type(cmd) == "table" and cmd or { cmd }
  ---@cast cmd string[]
  ---@type string?
  local found
  for _, c in ipairs(cmd) do
    if vim.fn.executable(c) == 1 then
      local out, exit_code = Process.exec({ c, opts.version })
      if exit_code ~= 0 then
        opts.error(("failed to get version of {%s}\n%s"):format(c, table.concat(out, "\n")))
      else
        local version = vim.trim(out[1] or "")
        version = version:gsub("^%s*" .. vim.pesc(c) .. "%s*", "")
        if opts.version_pattern and not version:find(opts.version_pattern, 1, true) then
          opts.warn(("`%s` version `%s` needed, but found `%s`"):format(c, opts.version_pattern, version))
        else
          found = ("{%s} `%s`"):format(c, version)
          break
        end
      end
    end
  end
  if found then
    opts.ok(found)
    return true
  else
    (opts.optional and opts.warn or opts.error)(
      ("{%s} %snot installed"):format(
        table.concat(cmd, "} or {"),
        opts.version_pattern and "version `" .. opts.version_pattern .. "` " or ""
      )
    )
  end
end

function M.check()
  start("lazy.nvim")
  info("{lazy.nvim} version `" .. Config.version .. "`")

  M.have("git")

  local sites = vim.opt.packpath:get()
  local default_site = vim.fn.stdpath("data") .. "/site"
  if not vim.tbl_contains(sites, default_site) then
    sites[#sites + 1] = default_site
  end

  local existing = false
  for _, site in pairs(sites) do
    for _, packs in ipairs(vim.fn.expand(site .. "/pack/*", false, true)) do
      if not packs:find("[/\\]dist$") and uv.fs_stat(packs) then
        existing = true
        warn("found existing packages at `" .. packs .. "`")
      end
    end
  end
  if not existing then
    ok("no existing packages found by other package managers")
  end

  for _, name in ipairs({ "packer", "plugged", "paq", "pckr", "mini.deps" }) do
    for _, path in ipairs(vim.opt.rtp:get()) do
      if path:find(name, 1, true) then
        error("Found paths on the rtp from another plugin manager `" .. name .. "`")
        break
      end
    end
  end

  local packer_compiled = vim.fn.stdpath("config") .. "/plugin/packer_compiled.lua"
  if uv.fs_stat(packer_compiled) then
    error("please remove the file `" .. packer_compiled .. "`")
  else
    ok("packer_compiled.lua not found")
  end

  local spec = Config.spec
  if spec == nil then
    error('No plugins loaded. Did you forget to run `require("lazy").setup()`?')
  else
    for _, plugin in pairs(spec.plugins) do
      M.check_valid(plugin)
    end
    if #spec.notifs > 0 then
      error("Issues were reported when loading your specs:")
      for _, notif in ipairs(spec.notifs) do
        local lines = vim.split(notif.msg, "\n")
        for _, line in ipairs(lines) do
          if notif.level == vim.log.levels.ERROR then
            error(line)
          else
            warn(line)
          end
        end
      end
    end
  end

  start("luarocks")
  if Config.options.rocks.enabled then
    if Config.hererocks() then
      info("checking `hererocks` installation")
    else
      info("checking `luarocks` installation")
    end
    local need_luarocks = {}
    for _, plugin in pairs(spec.plugins) do
      if plugin.build == "rockspec" then
        table.insert(need_luarocks, plugin.name)
      end
    end
    if #need_luarocks == 0 then
      ok("no plugins require `luarocks`, so you can ignore any warnings below")
    else
      local lines = vim.tbl_map(function(name)
        return "  * `" .. name .. "`"
      end, need_luarocks)

      info("you have some plugins that require `luarocks`:\n" .. table.concat(lines, "\n"))
    end
    local ok = require("lazy.pkg.rockspec").check({
      error = #need_luarocks > 0 and error or warn,
      warn = warn,
      ok = ok,
    })
    if not ok then
      warn(table.concat({
        "Lazy won't be able to install plugins that require `luarocks`.",
        "Here's what you can do:",
        " - fix your `luarocks` installation",
        Config.hererocks() and " - disable *hererocks* with `opts.rocks.hererocks = false`"
          or " - enable `hererocks` with `opts.rocks.hererocks = true`",
        " - disable `luarocks` support completely with `opts.rocks.enabled = false`",
      }, "\n"))
    end
  else
    ok("luarocks disabled")
  end
end

---@param plugin LazyPlugin
function M.check_valid(plugin)
  for key in pairs(plugin) do
    if not vim.tbl_contains(M.valid, key) then
      if key ~= "module" or type(plugin.module) ~= "boolean" then
        warn("{" .. plugin.name .. "}: unknown key <" .. key .. ">")
      end
    end
  end
end

M.valid = {
  1,
  "_",
  "branch",
  "build",
  "cmd",
  "commit",
  "cond",
  "config",
  "deactivate",
  "dependencies",
  "dev",
  "dir",
  "enabled",
  "event",
  "ft",
  "import",
  "init",
  "keys",
  "lazy",
  "main",
  "module",
  "name",
  "optional",
  "opts",
  "pin",
  "priority",
  "submodules",
  "tag",
  "url",
  "version",
}

return M
```

## File: `lua/lazy/help.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.util")

local M = {}

function M.index(plugin)
  if Config.options.readme.skip_if_doc_exists and vim.uv.fs_stat(plugin.dir .. "/doc") then
    return {}
  end

  local files = {}

  for _, file in ipairs(Config.options.readme.files) do
    vim.list_extend(files, vim.fn.expand(plugin.dir .. "/" .. file, false, true))
  end

  ---@type table<string,{file:string, tag:string, line:string}>
  local tags = {}
  for _, file in ipairs(files) do
    file = Util.norm(file)
    if vim.uv.fs_stat(file) then
      local rel_file = file:sub(#plugin.dir + 1)
      local tag_filename = plugin.name .. vim.fn.fnamemodify(rel_file, ":h"):gsub("%W+", "-"):gsub("^%-$", "")
      local lines = vim.split(Util.read_file(file), "\n")
      for _, line in ipairs(lines) do
        local title = line:match("^#+%s*(.*)")
        if title then
          local tag = tag_filename .. "-" .. title:lower():gsub("%W+", "-")
          tag = tag:gsub("%-+", "-"):gsub("%-$", "")
          line = line:gsub("([%[%]/])", "\\%1")
          tags[tag] = { tag = tag, line = line, file = tag_filename .. ".md" }
        end
      end
      table.insert(lines, [[<!-- vim: set ft=markdown: -->]])
      Util.write_file(Config.options.readme.root .. "/doc/" .. tag_filename .. ".md", table.concat(lines, "\n"))
    end
  end
  return tags
end

function M.update()
  if Config.plugins["lazy.nvim"] then
    vim.cmd.helptags(Config.plugins["lazy.nvim"].dir .. "/doc")
  end
  if Config.options.readme.enabled == false then
    return
  end

  local docs = Config.options.readme.root .. "/doc"
  vim.fn.mkdir(docs, "p")

  Util.ls(docs, function(path, name, type)
    if type == "file" and name:sub(-2) == "md" then
      vim.uv.fs_unlink(path)
    end
  end)
  ---@type {file:string, tag:string, line:string}[]
  local tags = {}
  for _, plugin in pairs(Config.plugins) do
    for key, tag in pairs(M.index(plugin)) do
      tags[key] = tag
    end
  end
  local lines = { [[!_TAG_FILE_ENCODING	utf-8	//]] }
  Util.foreach(tags, function(_, tag)
    table.insert(lines, ("%s\t%s\t/%s"):format(tag.tag, tag.file, tag.line))
  end, { case_sensitive = true })
  Util.write_file(docs .. "/tags", table.concat(lines, "\n"))
end

return M
```

## File: `lua/lazy/init.lua`
```
---@class Lazy: LazyCommands
local M = {}
M._start = 0

vim.uv = vim.uv or vim.loop

local function profile_require()
  local done = {} ---@type table<string, true>
  local r = require
  _G.require = function(modname)
    local Util = package.loaded["lazy.core.util"]
    if Util and not done[modname] then
      done[modname] = true
      Util.track({ require = modname })
      local ok, ret = pcall(function()
        return vim.F.pack_len(r(modname))
      end)
      Util.track()
      if not ok then
        error(ret, 2)
      end
      return vim.F.unpack_len(ret)
    else
      return r(modname)
    end
  end
end

---@overload fun(opts: LazyConfig)
---@overload fun(spec:LazySpec, opts: LazyConfig)
function M.setup(spec, opts)
  if type(spec) == "table" and spec.spec then
    ---@cast spec LazyConfig
    opts = spec
  else
    opts = opts or {}
    opts.spec = spec
  end

  M._start = M._start == 0 and vim.uv.hrtime() or M._start
  if vim.g.lazy_did_setup then
    return vim.notify(
      "Re-sourcing your config is not supported with lazy.nvim",
      vim.log.levels.WARN,
      { title = "lazy.nvim" }
    )
  end
  vim.g.lazy_did_setup = true
  if not vim.go.loadplugins then
    return
  end
  if vim.fn.has("nvim-0.8.0") ~= 1 then
    return vim.notify("lazy.nvim requires Neovim >= 0.8.0", vim.log.levels.ERROR, { title = "lazy.nvim" })
  end
  if not (pcall(require, "ffi") and jit and jit.version) then
    return vim.notify("lazy.nvim requires Neovim built with LuaJIT", vim.log.levels.ERROR, { title = "lazy.nvim" })
  end
  local start = vim.uv.hrtime()

  -- use the Neovim cache if available
  if vim.loader and vim.fn.has("nvim-0.9.1") == 1 then
    package.loaded["lazy.core.cache"] = vim.loader
  end

  local Cache = require("lazy.core.cache")

  local enable_cache = vim.tbl_get(opts, "performance", "cache", "enabled") ~= false
  -- load module cache before anything else
  if enable_cache then
    Cache.enable()
  end

  if vim.tbl_get(opts, "profiling", "require") then
    profile_require()
  end

  require("lazy.stats").track("LazyStart")

  local Util = require("lazy.core.util")
  local Config = require("lazy.core.config")
  local Loader = require("lazy.core.loader")

  table.insert(package.loaders, 3, Loader.loader)

  if vim.tbl_get(opts, "profiling", "loader") then
    if vim.loader then
      vim.loader._profile({ loaders = true })
    else
      Cache._profile_loaders()
    end
  end

  Util.track({ plugin = "lazy.nvim" }) -- setup start
  Util.track("module", vim.uv.hrtime() - start)

  -- load config
  Util.track("config")
  Config.setup(opts)
  Util.track()

  -- setup loader and handlers
  Loader.setup()

  -- correct time delta and loaded
  local delta = vim.uv.hrtime() - start
  Util.track().time = delta -- end setup
  if Config.plugins["lazy.nvim"] then
    Config.plugins["lazy.nvim"]._.loaded = { time = delta, source = "init.lua" }
  end

  -- load plugins with lazy=false or Plugin.init
  Loader.startup()

  -- all done!
  vim.api.nvim_exec_autocmds("User", { pattern = "LazyDone", modeline = false })
  require("lazy.stats").track("LazyDone")
end

function M.stats()
  return require("lazy.stats").stats()
end

function M.bootstrap()
  local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
  if not (vim.uv or vim.loop).fs_stat(lazypath) then
    vim.fn.system({
      "git",
      "clone",
      "--filter=blob:none",
      "https://github.com/folke/lazy.nvim.git",
      "--branch=stable", -- latest stable release
      lazypath,
    })
  end
  vim.opt.rtp:prepend(lazypath)
end

---@return LazyPlugin[]
function M.plugins()
  return vim.tbl_values(require("lazy.core.config").plugins)
end

setmetatable(M, {
  __index = function(_, key)
    return function(...)
      return require("lazy.view.commands").commands[key](...)
    end
  end,
})

return M
```

## File: `lua/lazy/minit.lua`
```
---@diagnostic disable: inject-field

local islist = vim.islist or vim.tbl_islist

local M = {}

---@param opts LazyConfig
---@return LazySpec[]
local function get_spec(opts)
  local ret = opts.spec or {}
  return ret and type(ret) == "table" and islist(ret) and ret or { ret }
end

---@param defaults LazyConfig
---@param opts LazyConfig
function M.extend(defaults, opts)
  local spec = {}
  vim.list_extend(spec, get_spec(defaults))
  vim.list_extend(spec, get_spec(opts))
  return vim.tbl_deep_extend("force", defaults, opts, { spec = spec })
end

---@param opts LazyConfig
function M.setup(opts)
  opts = M.extend({
    local_spec = false,
    change_detection = { enabled = false },
    dev = {
      patterns = vim.env.LAZY_DEV and vim.split(vim.env.LAZY_DEV, ",") or nil,
    },
  }, opts)

  local args = {}
  local is_busted = false
  local is_minitest = false
  local offline = vim.env.LAZY_OFFLINE == "1" or vim.env.LAZY_OFFLINE == "true"
  for _, a in ipairs(_G.arg) do
    if a == "--busted" then
      is_busted = true
    elseif a == "--minitest" then
      is_minitest = true
    elseif a == "--offline" then
      offline = true
    else
      table.insert(args, a)
    end
  end
  _G.arg = args

  if is_busted then
    opts = M.busted.setup(opts)
  elseif is_minitest then
    opts = M.minitest.setup(opts)
  end

  -- set stdpaths to use .tests
  if vim.env.LAZY_STDPATH then
    local root = vim.fn.fnamemodify(vim.env.LAZY_STDPATH, ":p")
    for _, name in ipairs({ "config", "data", "state", "cache" }) do
      vim.env[("XDG_%s_HOME"):format(name:upper())] = root .. "/" .. name
    end
  end
  vim.o.loadplugins = true
  require("lazy").setup(opts)
  if vim.g.colors_name == nil then
    vim.cmd("colorscheme habamax")
  end
  if not offline then
    require("lazy").update():wait()
  end
  if vim.bo.filetype == "lazy" then
    local errors = false
    for _, plugin in pairs(require("lazy.core.config").spec.plugins) do
      errors = errors or require("lazy.core.plugin").has_errors(plugin)
    end
    if not errors then
      vim.cmd.close()
    end
  end

  if is_busted then
    M.busted.run()
  elseif is_minitest then
    M.minitest.run()
  end
end

function M.repro(opts)
  opts = M.extend({
    spec = {
      {
        "folke/tokyonight.nvim",
        priority = 1000,
        lazy = false,
        config = function()
          require("tokyonight").setup({ style = "moon" })
          require("tokyonight").load()
        end,
      },
    },
    install = { colorscheme = { "tokyonight" } },
  }, opts)
  M.setup(opts)
end

M.minitest = {}

function M.minitest.run()
  local Config = require("lazy.core.config")
  -- disable termnial output for the tests
  Config.options.headless = {}

  if not require("lazy.core.config").headless() then
    return vim.notify("busted can only run in headless mode. Please run with `nvim -l`", vim.log.levels.WARN)
  end
  package.path = package.path .. ";" .. vim.uv.cwd() .. "/tests/?.lua"
  local Test = require("mini.test")
  local expect = Test.expect
  local _assert = assert
  local Assert = {
    __call = function(_, ...)
      return _assert(...)
    end,
    same = expect.equality,
    equal = expect.equality,
    are = {
      equal = expect.equality,
    },
    is_not = {
      same = expect.no_equality,
    },
    is_not_nil = function(a)
      return expect.no_equality(nil, a)
    end,
    is_true = function(a)
      return expect.equality(true, a)
    end,
    is_false = function(a)
      return expect.equality(false, a)
    end,
  }
  Assert.__index = Assert
  assert = setmetatable({}, Assert)
  assert = require("luassert")
  require("mini.test").run()
end

---@param opts LazyConfig
function M.minitest.setup(opts)
  return M.extend({
    spec = {
      "lunarmodules/luassert",
      {
        "echasnovski/mini.test",
        opts = {
          collect = {
            find_files = function()
              return #_G.arg > 0 and _G.arg or vim.fn.globpath("tests", "**/*_spec.lua", true, true)
            end,
          },
          -- script_path = "tests/minit.lua",
        },
      },
      { dir = vim.uv.cwd() },
    },
    rocks = { hererocks = true },
  }, opts)
end

M.busted = {}

function M.busted.run()
  local Config = require("lazy.core.config")
  -- disable termnial output for the tests
  Config.options.headless = {}

  if not require("lazy.core.config").headless() then
    return vim.notify("busted can only run in headless mode. Please run with `nvim -l`", vim.log.levels.WARN)
  end
  package.path = package.path .. ";" .. vim.uv.cwd() .. "/tests/?.lua"
  -- run busted
  return pcall(require("busted.runner"), {
    standalone = false,
  }) or os.exit(1)
end

---@param opts LazyConfig
function M.busted.setup(opts)
  local args = table.concat(_G.arg, " ")
  local json = args:find("--output[ =]json")

  return M.extend({
    spec = {
      "lunarmodules/busted",
      { dir = vim.uv.cwd() },
    },
    headless = {
      process = not json,
      log = not json,
      task = not json,
    },
    rocks = { hererocks = true },
  }, opts)
end

---@param opts LazyConfig
function M.busted.init(opts)
  opts = M.busted.setup(opts)
  M.setup(opts)
  M.busted.run()
end

setmetatable(M.busted, {
  __call = function(_, opts)
    M.busted.init(opts)
  end,
})

return M
```

## File: `lua/lazy/state.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.util")

---@type LazyState
local M = {}

---@class LazyState
local defaults = {
  checker = {
    last_check = 0,
  },
}

---@type LazyState
local data = nil

function M.read()
  pcall(function()
    ---@diagnostic disable-next-line: cast-local-type
    data = vim.json.decode(Util.read_file(Config.options.state))
  end)
  data = vim.tbl_deep_extend("force", {}, defaults, data or {})
end

function M.write()
  vim.fn.mkdir(vim.fn.fnamemodify(Config.options.state, ":p:h"), "p")
  Util.write_file(Config.options.state, vim.json.encode(data))
end

function M.__index(_, key)
  if not data then
    M.read()
  end
  return data[key]
end

function M.__setindex(_, key, value)
  if not data then
    M.read()
  end
  ---@diagnostic disable-next-line: no-unknown
  data[key] = value
end

return setmetatable(M, M)
```

## File: `lua/lazy/stats.lua`
```
local ffi = require("ffi")

local M = {}

---@class LazyStats
M._stats = {
  -- startuptime in milliseconds till UIEnter
  startuptime = 0,
  -- when true, startuptime is the accurate cputime for the Neovim process. (Linux & macOS)
  -- this is more accurate than `nvim --startuptime`, and as such will be slightly higher
  -- when false, startuptime is calculated based on a delta with a timestamp when lazy started.
  real_cputime = false,
  count = 0, -- total number of plugins
  loaded = 0, -- number of loaded plugins
  ---@type table<string, number>
  times = {},
}

---@type ffi.namespace*
M.C = nil

function M.on_ui_enter()
  M._stats.startuptime = M.track("UIEnter")
  require("lazy.core.util").track({ start = "startuptime" }, M._stats.startuptime * 1e6)
  vim.api.nvim_exec_autocmds("User", { pattern = "LazyVimStarted", modeline = false })
end

function M.track(event)
  local time = M.cputime()
  M._stats.times[event] = time
  return time
end

function M.cputime()
  if M.C == nil then
    pcall(function()
      ffi.cdef([[
        typedef int clockid_t;
        typedef struct timespec {
          int64_t tv_sec;   /* Use fixed 64-bit type for portability */
          long    tv_nsec;  /* nanoseconds */
        } nanotime;
        int clock_gettime(clockid_t clk_id, struct timespec *tp);
      ]])
      M.C = ffi.C
    end)
  end

  local function real()
    -- Zero-initialize to handle 32-bit systems where only lower 32 bits are written
    local pnano = ffi.new("nanotime[1]")
    local CLOCK_PROCESS_CPUTIME_ID = jit.os == "OSX" and 12 or 2
    ffi.C.clock_gettime(CLOCK_PROCESS_CPUTIME_ID, pnano)
    return tonumber(pnano[0].tv_sec) * 1e3 + tonumber(pnano[0].tv_nsec) / 1e6
  end

  local function fallback()
    return (vim.uv.hrtime() - require("lazy")._start) / 1e6
  end

  local ok, ret = pcall(real)
  if ok then
    M.cputime = real
    M._stats.real_cputime = true
    return ret
  else
    M.cputime = fallback
    return fallback()
  end
end

function M.stats()
  M._stats.count = 0
  M._stats.loaded = 0
  for _, plugin in pairs(require("lazy.core.config").plugins) do
    M._stats.count = M._stats.count + 1
    if plugin._.loaded then
      M._stats.loaded = M._stats.loaded + 1
    end
  end
  return M._stats
end

return M
```

## File: `lua/lazy/status.lua`
```
local Config = require("lazy.core.config")

local M = {}

function M.updates()
  local Checker = require("lazy.manage.checker")
  local updates = #Checker.updated
  return updates > 0 and (Config.options.ui.icons.plugin .. "" .. updates)
end

function M.has_updates()
  local Checker = require("lazy.manage.checker")
  return #Checker.updated > 0
end

return M
```

## File: `lua/lazy/terminal.lua`
```
---@class Ansi: table<string, fun(string):string>
local M = {}

M.colors = {
  reset = "\27[0m",
  black = "\27[30m",
  red = "\27[31m",
  green = "\27[32m",
  yellow = "\27[33m",
  blue = "\27[34m",
  magenta = "\27[35m",
  cyan = "\27[36m",
  white = "\27[37m",
  bright_black = "\27[90m",
  bright_red = "\27[91m",
  bright_green = "\27[92m",
  bright_yellow = "\27[93m",
  bright_blue = "\27[94m",
  bright_magenta = "\27[95m",
  bright_cyan = "\27[96m",
  bright_white = "\27[97m",
}

function M.color(text, color)
  return M.colors[color] .. text .. M.colors.reset
end

-- stylua: ignore start
function M.black(text) return M.color(text, "black") end
function M.red(text) return M.color(text, "red") end
function M.green(text) return M.color(text, "green") end
function M.yellow(text) return M.color(text, "yellow") end
function M.blue(text) return M.color(text, "blue") end
function M.magenta(text) return M.color(text, "magenta") end
function M.cyan(text) return M.color(text, "cyan") end
function M.white(text) return M.color(text, "white") end
function M.bright_black(text) return M.color(text, "bright_black") end
function M.bright_red(text) return M.color(text, "bright_red") end
function M.bright_green(text) return M.color(text, "bright_green") end
function M.bright_yellow(text) return M.color(text, "bright_yellow") end
function M.bright_blue(text) return M.color(text, "bright_blue") end
function M.bright_magenta(text) return M.color(text, "bright_magenta") end
function M.bright_cyan(text) return M.color(text, "bright_cyan") end
function M.bright_white(text) return M.color(text, "bright_white") end
-- stylua: ignore end

---@param data string
---@param prefix string
function M.prefix(data, prefix)
  -- Normalize Windows-style newlines to simple newlines
  data = data:gsub("\r\n", "\n")

  -- Handle prefix for the first line, if data starts immediately
  data = prefix .. data

  -- Prefix new lines ensuring not to double prefix if a line starts with \r
  data = data:gsub("(\n)([^\r])", "%1" .. prefix .. "%2")

  -- Handle carriage returns properly to avoid double prefixing
  -- Replace any \r not followed by \n with \r, then add a prefix only if the following character isn't the start of our prefix
  data = data:gsub("\r([^\n])", function(nextChar)
    if nextChar:sub(1, #prefix) == prefix then
      return "\r" .. nextChar
    else
      return "\r" .. prefix .. nextChar
    end
  end)
  return data
end

return M
```

## File: `lua/lazy/types.lua`
```

---@alias LazyPluginKind "normal"|"clean"|"disabled"

---@class LazyPluginState
---@field cache? table<string,any>
---@field cloned? boolean
---@field cond? boolean
---@field dep? boolean True if this plugin is only in the spec as a dependency
---@field dir? string Explicit dir or dev set for this plugin
---@field dirty? boolean
---@field build? boolean
---@field frags? number[]
---@field top? boolean
---@field handlers? LazyPluginHandlers
---@field installed? boolean
---@field is_local? boolean
---@field kind? LazyPluginKind
---@field loaded? {[string]:string}|{time:number}
---@field outdated? boolean
---@field rtp_loaded? boolean
---@field tasks? LazyTask[]
---@field updated? {from:string, to:string}
---@field updates? {from:GitInfo, to:GitInfo}
---@field last_check? number
---@field working? boolean
---@field pkg? LazyPkg

---@alias PluginOpts table|fun(self:LazyPlugin, opts:table):table?

---@class LazyPluginHooks
---@field init? fun(self:LazyPlugin) Will always be run
---@field deactivate? fun(self:LazyPlugin) Unload/Stop a plugin
---@field config? fun(self:LazyPlugin, opts:table)|true Will be executed when loading the plugin
---@field build? false|string|async fun(self:LazyPlugin)|(string|async fun(self:LazyPlugin))[]
---@field opts? PluginOpts

---@class LazyPluginHandlers
---@field event? table<string,LazyEvent>
---@field ft? table<string,LazyEvent>
---@field keys? table<string,LazyKeys>
---@field cmd? table<string,string>

---@class LazyPluginRef
---@field branch? string
---@field tag? string
---@field commit? string
---@field version? string|boolean
---@field pin? boolean
---@field submodules? boolean Defaults to true

---@class LazyPluginBase
---@field [1] string?
---@field name string display name and name used for plugin config files
---@field main? string Entry module that has setup & deactivate
---@field url string?
---@field dir string
---@field enabled? boolean|(fun():boolean)
---@field cond? boolean|(fun():boolean)
---@field optional? boolean If set, then this plugin will not be added unless it is added somewhere else
---@field lazy? boolean
---@field priority? number Only useful for lazy=false plugins to force loading certain plugins first. Default priority is 50
---@field dev? boolean If set, then link to the respective folder under your ~/projects
---@field rocks? string[]
---@field virtual? boolean virtual plugins won't be installed or added to the rtp.

---@class LazyPlugin: LazyPluginBase,LazyPluginHandlers,LazyPluginHooks,LazyPluginRef
---@field dependencies? string[]
---@field specs? string|string[]|LazyPluginSpec[]
---@field _ LazyPluginState

---@class LazyPluginSpecHandlers
---@field event? string[]|string|LazyEventSpec[]|fun(self:LazyPlugin, event:string[]):string[]
---@field cmd? string[]|string|fun(self:LazyPlugin, cmd:string[]):string[]
---@field ft? string[]|string|fun(self:LazyPlugin, ft:string[]):string[]
---@field keys? string|string[]|LazyKeysSpec[]|fun(self:LazyPlugin, keys:string[]):((string|LazyKeys)[])
---@field module? false

---@class LazyPluginSpec: LazyPluginBase,LazyPluginSpecHandlers,LazyPluginHooks,LazyPluginRef
---@field name? string display name and name used for plugin config files
---@field dir? string
---@field dependencies? string|string[]|LazyPluginSpec[]
---@field specs? string|string[]|LazyPluginSpec[]

---@alias LazySpec string|LazyPluginSpec|LazySpecImport|LazySpec[]

---@class LazySpecImport
---@field import string|(fun():LazyPluginSpec) spec module to import
---@field name? string
---@field enabled? boolean|(fun():boolean)
---@field cond? boolean|(fun():boolean)

---@class LazyFragment
---@field id number
---@field pkg? boolean
---@field pid? number
---@field deps? number[]
---@field frags? number[]
---@field dep? boolean
---@field name string
---@field url? string
---@field dir? string
---@field spec LazyPlugin
```

## File: `lua/lazy/util.lua`
```
---@class LazyUtil: LazyUtilCore
local M = setmetatable({}, { __index = require("lazy.core.util") })

function M.file_exists(file)
  return vim.uv.fs_stat(file) ~= nil
end

---@param opts? LazyFloatOptions
---@return LazyFloat
function M.float(opts)
  return require("lazy.view.float")(opts)
end

function M.wo(win, k, v)
  if vim.api.nvim_set_option_value then
    vim.api.nvim_set_option_value(k, v, { scope = "local", win = win })
  else
    vim.wo[win][k] = v
  end
end

---@param opts? {system?:boolean}
function M.open(uri, opts)
  opts = opts or {}
  if not opts.system and M.file_exists(uri) then
    return M.float({ style = "", file = uri })
  end
  local Config = require("lazy.core.config")
  local cmd
  if not opts.system and Config.options.ui.browser then
    cmd = { Config.options.ui.browser, uri }
  elseif vim.fn.has("win32") == 1 then
    cmd = { "explorer", uri }
  elseif vim.fn.has("macunix") == 1 then
    cmd = { "open", uri }
  else
    if vim.fn.executable("xdg-open") == 1 then
      cmd = { "xdg-open", uri }
    elseif vim.fn.executable("wslview") == 1 then
      cmd = { "wslview", uri }
    else
      cmd = { "open", uri }
    end
  end

  local ret = vim.fn.jobstart(cmd, { detach = true })
  if ret <= 0 then
    local msg = {
      "Failed to open uri",
      ret,
      vim.inspect(cmd),
    }
    vim.notify(table.concat(msg, "\n"), vim.log.levels.ERROR)
  end
end

function M.read_file(file)
  local fd = assert(io.open(file, "r"))
  ---@type string
  local data = fd:read("*a")
  fd:close()
  return data
end

function M.write_file(file, contents)
  local fd = assert(io.open(file, "w+"))
  fd:write(contents)
  fd:close()
end

---@generic F: fun()
---@param ms number
---@param fn F
---@return F
function M.throttle(ms, fn)
  ---@type Async
  local async
  local pending = false

  return function()
    if async and async:running() then
      pending = true
      return
    end
    ---@async
    async = require("lazy.async").new(function()
      repeat
        pending = false
        fn()
        async:sleep(ms)

      until not pending
    end)
  end
end

--- Creates a weak reference to an object.
--- Calling the returned function will return the object if it has not been garbage collected.
---@generic T: table
---@param obj T
---@return T|fun():T?
function M.weak(obj)
  local weak = { _obj = obj }
  ---@return table<any, any>
  local function get()
    local ret = rawget(weak, "_obj")
    return ret == nil and error("Object has been garbage collected", 2) or ret
  end
  local mt = {
    __mode = "v",
    __call = function(t)
      return rawget(t, "_obj")
    end,
    __index = function(_, k)
      return get()[k]
    end,
    __newindex = function(_, k, v)
      get()[k] = v
    end,
    __pairs = function()
      return pairs(get())
    end,
  }
  return setmetatable(weak, mt)
end

---@class LazyCmdOptions: LazyFloatOptions
---@field cwd? string
---@field env? table<string,string>
---@field float? LazyFloatOptions

-- Opens a floating terminal (interactive by default)
---@param cmd? string[]|string
---@param opts? LazyCmdOptions|{interactive?:boolean}
function M.float_term(cmd, opts)
  cmd = cmd or {}
  if type(cmd) == "string" then
    cmd = { cmd }
  end
  if #cmd == 0 then
    cmd = { vim.o.shell }
  end
  opts = opts or {}
  local float = M.float(opts)
  vim.fn.termopen(cmd, vim.tbl_isempty(opts) and vim.empty_dict() or opts)
  if opts.interactive ~= false then
    vim.cmd.startinsert()
    vim.api.nvim_create_autocmd("TermClose", {
      once = true,
      buffer = float.buf,
      callback = function()
        float:close({ wipe = true })
        vim.cmd.checktime()
      end,
    })
  end
  return float
end

--- Runs the command and shows it in a floating window
---@param cmd string[]
---@param opts? LazyCmdOptions|{filetype?:string}
function M.float_cmd(cmd, opts)
  opts = opts or {}
  local Process = require("lazy.manage.process")
  local lines, code = Process.exec(cmd, { cwd = opts.cwd })
  if code ~= 0 then
    M.error({
      "`" .. table.concat(cmd, " ") .. "`",
      "",
      "## Error",
      table.concat(lines, "\n"),
    }, { title = "Command Failed (" .. code .. ")" })
    return
  end
  local float = M.float(opts)
  if opts.filetype then
    vim.bo[float.buf].filetype = opts.filetype
  end
  vim.api.nvim_buf_set_lines(float.buf, 0, -1, false, lines)
  vim.bo[float.buf].modifiable = false
  return float
end

---@deprecated use float_term or float_cmd instead
function M.open_cmd()
  M.warn([[`require("lazy.util").open_cmd()` is deprecated. Please use `float_term` instead. Check the docs]])
end

---@return string?
function M.head(file)
  local f = io.open(file)
  if f then
    local ret = f:read()
    f:close()
    return ret
  end
end

---@return {branch: string, hash:string}?
function M.git_info(dir)
  local line = M.head(dir .. "/.git/HEAD")
  if line then
    ---@type string, string
    local ref, branch = line:match("ref: (refs/heads/(.*))")

    if ref then
      return {
        branch = branch,
        hash = M.head(dir .. "/.git/" .. ref),
      }
    end
  end
end

---@param msg string|string[]
---@param opts? table
function M.markdown(msg, opts)
  if type(msg) == "table" then
    msg = table.concat(msg, "\n") or msg
  end

  vim.notify(
    msg,
    vim.log.levels.INFO,
    vim.tbl_deep_extend("force", {
      title = "lazy.nvim",
      on_open = function(win)
        M.wo(win, "conceallevel", 3)
        M.wo(win, "concealcursor", "n")
        M.wo(win, "spell", false)

        vim.treesitter.start(vim.api.nvim_win_get_buf(win), "markdown")
      end,
    }, opts or {})
  )
end

function M._dump(value, result)
  local t = type(value)
  if t == "number" or t == "boolean" then
    table.insert(result, tostring(value))
  elseif t == "string" then
    table.insert(result, ("%q"):format(value))
  elseif t == "table" and value._raw then
    table.insert(result, value._raw)
  elseif t == "table" then
    table.insert(result, "{")
    for _, v in ipairs(value) do
      M._dump(v, result)
      table.insert(result, ",")
    end
    ---@diagnostic disable-next-line: no-unknown
    for k, v in pairs(value) do
      if type(k) == "string" then
        if k:match("^[a-zA-Z]+$") then
          table.insert(result, ("%s="):format(k))
        else
          table.insert(result, ("[%q]="):format(k))
        end
        M._dump(v, result)
        table.insert(result, ",")
      end
    end
    table.insert(result, "}")
  else
    error("Unsupported type " .. t)
  end
end

function M.dump(value)
  local result = {}
  M._dump(value, result)
  return table.concat(result, "")
end

---@generic V
---@param t table<string, V>
---@param fn fun(key:string, value:V)
---@param opts? {case_sensitive?:boolean}
function M.foreach(t, fn, opts)
  ---@type string[]
  local keys = vim.tbl_keys(t)
  pcall(table.sort, keys, function(a, b)
    if opts and opts.case_sensitive then
      return a < b
    end
    return a:lower() < b:lower()
  end)
  for _, key in ipairs(keys) do
    fn(key, t[key])
  end
end

return M
```

## File: `lua/lazy/community/init.lua`
```
local M = {}

---@type table<string, string>
local mapping = nil

local function load()
  if not mapping then
    mapping = {}
    ---@type {name:string, url:string, version:string}[]
    local gen = require("lazy.community._generated")
    for _, rock in ipairs(gen) do
      mapping[rock.name] = rock.url
    end
  end
  return mapping
end

---@param rock string
---@return string?
function M.get_url(rock)
  return load()[rock]
end

function M.get_spec(name)
  return require("lazy.community.specs")[name]
end

return M
```

## File: `lua/lazy/community/specs.lua`
```
---@type table<string, LazySpec>
return {
  ["plenary.nvim"] = {
    "nvim-lua/plenary.nvim",
    lazy = true,
  },
}
```

## File: `lua/lazy/community/_generated.lua`
```
return 
{ {
    name = "15puzzle.nvim",
    url = "NStefan002/15puzzle.nvim",
    version = "1.4.1-1"
  }, {
    name = "2048.nvim",
    url = "NStefan002/2048.nvim",
    version = "2.8.2-1"
  }, {
    name = "adopure.nvim",
    url = "Willem-J-an/adopure.nvim",
    version = "2.1.1-1"
  }, {
    name = "aerial.nvim",
    url = "stevearc/aerial.nvim",
    version = "2.6.1-1"
  }, {
    name = "age.nvim",
    url = "KingMichaelPark/age.nvim",
    version = "0.1.0-1"
  }, {
    name = "ai.nvim",
    url = "S1M0N38/ai.nvim",
    version = "1.6.0-1"
  }, {
    name = "altf.nvim",
    url = "wsdjeg/altf.nvim",
    version = "1.2.0-1"
  }, {
    name = "ascii-ui.nvim",
    url = "rcasia/ascii-ui.nvim",
    version = "0.6.1-1"
  }, {
    name = "astral.nvim",
    url = "rootiest/astral.nvim",
    version = "1.0.9-1"
  }, {
    name = "auto-hlsearch.nvim",
    url = "asiryk/auto-hlsearch.nvim",
    version = "1.1.0-1"
  }, {
    name = "auto-theme.nvim",
    url = "barrett-ruth/auto-theme.nvim",
    version = "0.2.0-1"
  }, {
    name = "avante.nvim",
    url = "yetone/avante.nvim",
    version = "0.0.27-1"
  }, {
    name = "banana.nvim",
    url = "CWood-sdf/banana.nvim",
    version = "0.3.0-1"
  }, {
    name = "bars-n-lines.nvim",
    url = "OXY2DEV/bars-N-lines.nvim",
    version = "1.0.0-1"
  }, {
    name = "bars.nvim",
    url = "OXY2DEV/bars.nvim",
    version = "2.2.0-1"
  }, {
    name = "base.nvim",
    url = "S1M0N38/base.nvim",
    version = "2.0.0-1"
  }, {
    name = "better-escape.nvim",
    url = "max397574/better-escape.nvim",
    version = "2.3.3-1"
  }, {
    name = "blaze.nvim",
    url = "qompassai/blaze.nvim",
    version = "1.0-1"
  }, {
    name = "blink.cmp",
    url = "Saghen/blink.cmp",
    version = "1.8.0-1"
  }, {
    name = "bookmarks.nvim",
    url = "wsdjeg/bookmarks.nvim",
    version = "1.1.0-1"
  }, {
    name = "bufdel.nvim",
    url = "wsdjeg/bufdel.nvim",
    version = "1.1.0-1"
  }, {
    name = "bufferline.nvim",
    url = "akinsho/bufferline.nvim",
    version = "4.9.1-1"
  }, {
    name = "care.nvim",
    url = "max397574/care.nvim",
    version = "0.1.0-1"
  }, {
    name = "ccc.nvim",
    url = "uga-rosa/ccc.nvim",
    version = "2.0.3-1"
  }, {
    name = "ccusage.nvim",
    url = "S1M0N38/ccusage.nvim",
    version = "1.0.3-1"
  }, {
    name = "chatml.nvim",
    url = "S1M0N38/chatml.nvim",
    version = "1.0.0-1"
  }, {
    name = "ci-template.nvim",
    url = "linrongbin16/ci-template.nvim",
    version = "8.1.0-1"
  }, {
    name = "cinnamon.nvim",
    url = "declancm/cinnamon.nvim",
    version = "1.2.5-1"
  }, {
    name = "cmp-rg",
    url = "lukas-reineke/cmp-rg",
    version = "1.3.11-1"
  }, {
    name = "code-runner.nvim",
    url = "wsdjeg/code-runner.nvim",
    version = "1.1.0-1"
  }, {
    name = "code-stats.nvim",
    url = "Freed-Wu/code-stats.nvim",
    version = "0.1.0-1"
  }, {
    name = "colorbox.nvim",
    url = "linrongbin16/colorbox.nvim",
    version = "3.2.1-1"
  }, {
    name = "colorbuddy.nvim",
    url = "tjdevries/colorbuddy.nvim",
    version = "1.0.0-1"
  }, {
    name = "colortils.nvim",
    url = "nvim-colortils/colortils.nvim",
    version = "1.2.0-1"
  }, {
    name = "command.nvim",
    url = "cultab/command.nvim",
    version = "0.2.0-1"
  }, {
    name = "commander.nvim",
    url = "FeiyouG/commander.nvim",
    version = "0.2.0-1"
  }, {
    name = "comment-box.nvim",
    url = "LudoPinelli/comment-box.nvim",
    version = "1.0.2-1"
  }, {
    name = "comment.nvim",
    url = "numToStr/Comment.nvim",
    version = "0.8.0-1"
  }, {
    name = "commons.nvim",
    url = "linrongbin16/commons.nvim",
    version = "27.0.0-1"
  }, {
    name = "conform.nvim",
    url = "stevearc/conform.nvim",
    version = "9.1.0-1"
  }, {
    name = "coop.nvim",
    url = "gregorias/coop.nvim",
    version = "1.1.1-0"
  }, {
    name = "copy-diagnostics.nvim",
    url = "NickStafford2/copy-diagnostics.nvim",
    version = "main-1"
  }, {
    name = "cord.nvim",
    url = "vyfor/cord.nvim",
    version = "2.3.8-1"
  }, {
    name = "cp.nvim",
    url = "barrett-ruth/cp.nvim",
    version = "0.5.0-1"
  }, {
    name = "cpicker.nvim",
    url = "wsdjeg/cpicker.nvim",
    version = "1.1.0-1"
  }, {
    name = "cppinsights.nvim",
    url = "Freed-Wu/cppinsights.nvim",
    version = "20.1-1"
  }, {
    name = "ctags.nvim",
    url = "wsdjeg/ctags.nvim",
    version = "1.1.0-1"
  }, {
    name = "ctrlg.nvim",
    url = "wsdjeg/ctrlg.nvim",
    version = "1.0.0-1"
  }, {
    name = "ctx.nvim",
    url = "S1M0N38/ctx.nvim",
    version = "1.0.0-1"
  }, {
    name = "cursor-text-objects.nvim",
    url = "ColinKennedy/cursor-text-objects.nvim",
    version = "2.0.0-1"
  }, {
    name = "cybu.nvim",
    url = "ghillb/cybu.nvim",
    version = "1.0-1"
  }, {
    name = "dante.nvim",
    url = "S1M0N38/dante.nvim",
    version = "1.3.1-1"
  }, {
    name = "daylight.nvim",
    url = "NTBBloodbath/daylight.nvim",
    version = "1.1.0-1"
  }, {
    name = "deadcolumn.nvim",
    url = "Bekaboo/deadcolumn.nvim",
    version = "1.0.1-1"
  }, {
    name = "decasify.nvim",
    url = "alerque/decasify",
    version = "0.11.2-1"
  }, {
    name = "decipher.nvim",
    url = "MisanthropicBit/decipher.nvim",
    version = "2.1.0-1"
  }, {
    name = "delog.nvim",
    url = "ej-shafran/delog.nvim",
    version = "0.0.2-1"
  }, {
    name = "detour.nvim",
    url = "carbon-steel/detour.nvim",
    version = "2.0.1-1"
  }, {
    name = "dial.nvim",
    url = "monaqa/dial.nvim",
    version = "0.5.1-1"
  }, {
    name = "distant.nvim",
    url = "chipsenkbeil/distant.nvim",
    version = "0.1.2-1"
  }, {
    name = "donut.nvim",
    url = "NStefan002/donut.nvim",
    version = "2.2.1-1"
  }, {
    name = "donutlify.nvim",
    url = "NStefan002/donutlify.nvim",
    version = "1.0.0-1"
  }, {
    name = "doris.nvim",
    url = "jackokring/doris.nvim",
    version = "0.3.2-1"
  }, {
    name = "down.nvim",
    url = "clpi/down.nvim",
    version = "master-1"
  }, {
    name = "dressing.nvim",
    url = "stevearc/dressing.nvim",
    version = "3.1.1-1"
  }, {
    name = "dropbar.nvim",
    url = "Bekaboo/dropbar.nvim",
    version = "14.2.1-1"
  }, {
    name = "duck.nvim",
    url = "tamton-aquib/duck.nvim",
    version = "main-1"
  }, {
    name = "easypick.nvim",
    url = "axkirillov/easypick.nvim",
    version = "0.6.0-1"
  }, {
    name = "edgy.nvim",
    url = "folke/edgy.nvim",
    version = "1.10.2-1"
  }, {
    name = "efmls-configs-nvim",
    url = "creativenull/efmls-configs-nvim",
    version = "1.10.1-1"
  }, {
    name = "elixir-tools.nvim",
    url = "elixir-tools/elixir-tools.nvim",
    version = "0.18.0-1"
  }, {
    name = "fake.nvim",
    url = "Kibadda/fake.nvim",
    version = "4.1.0-1"
  }, {
    name = "fcitx5-ui.nvim",
    url = "black-desk/fcitx5-ui.nvim",
    version = "0.1.7-1"
  }, {
    name = "feed.nvim",
    url = "neo451/feed.nvim",
    version = "2.19.2-1"
  }, {
    name = "feline.nvim",
    url = "freddiehaddad/feline.nvim",
    version = "1.7.1-1"
  }, {
    name = "fidget.nvim",
    url = "j-hui/fidget.nvim",
    version = "1.6.0-1"
  }, {
    name = "firenvim",
    url = "glacambre/firenvim",
    version = "0.2.16-1"
  }, {
    name = "flash.nvim",
    url = "folke/flash.nvim",
    version = "2.1.0-1"
  }, {
    name = "flatten.nvim",
    url = "willothy/flatten.nvim",
    version = "0.5.1-1"
  }, {
    name = "flutter-tools.nvim",
    url = "akinsho/flutter-tools.nvim",
    version = "1.14.0-1"
  }, {
    name = "flygrep.nvim",
    url = "wsdjeg/flygrep.nvim",
    version = "1.3.0-1"
  }, {
    name = "focus.nvim",
    url = "nvim-focus/focus.nvim",
    version = "1.0.2-1"
  }, {
    name = "foldtext.nvim",
    url = "OXY2DEV/foldtext.nvim",
    version = "2.0.0-1"
  }, {
    name = "format.nvim",
    url = "wsdjeg/format.nvim",
    version = "1.4.0-1"
  }, {
    name = "freeze-code.nvim",
    url = "AlejandroSuero/freeze-code.nvim",
    version = "0.2.0-1"
  }, {
    name = "fugit2.nvim",
    url = "SuperBo/fugit2.nvim",
    version = "0.2.1-1"
  }, {
    name = "funnyfiles.nvim",
    url = "aikooo7/funnyfiles.nvim",
    version = "1.0.1-1"
  }, {
    name = "fzfx.nvim",
    url = "linrongbin16/fzfx.nvim",
    version = "8.2.6-1"
  }, {
    name = "galileo.nvim",
    url = "S1M0N38/galileo.nvim",
    version = "0.0.2-1"
  }, {
    name = "gemini.nvim",
    url = "prime-run/gemini.nvim",
    version = "0.1.2-1"
  }, {
    name = "gentags.nvim",
    url = "linrongbin16/gentags.nvim",
    version = "3.0.3-1"
  }, {
    name = "git-worktree.nvim",
    url = "polarmutex/git-worktree.nvim",
    version = "2.1.0-1"
  }, {
    name = "git.nvim",
    url = "Kibadda/git.nvim",
    version = "5.4.0-1"
  }, {
    name = "git2.nvim",
    url = "Freed-Wu/git2.nvim",
    version = "0.0.6-1"
  }, {
    name = "github-nvim-theme",
    url = "projekt0n/github-nvim-theme",
    version = "1.1.2-1"
  }, {
    name = "github.nvim",
    url = "wsdjeg/github.nvim",
    version = "0.1.0-1"
  }, {
    name = "gitlink.nvim",
    url = "wsdjeg/gitlink.nvim",
    version = "1.0.0-1"
  }, {
    name = "gitlinker.nvim",
    url = "linrongbin16/gitlinker.nvim",
    version = "5.3.0-1"
  }, {
    name = "gitsigns.nvim",
    url = "lewis6991/gitsigns.nvim",
    version = "1.0.2-1"
  }, {
    name = "glow.nvim",
    url = "ellisonleao/glow.nvim",
    version = "0.2.0-1"
  }, {
    name = "go.nvim",
    url = "ray-x/go.nvim",
    version = "0.10.4-1"
  }, {
    name = "godo.nvim",
    url = "arthuradolfo/godo.nvim",
    version = "1.1.0-0"
  }, {
    name = "grapple.nvim",
    url = "cbochs/grapple.nvim",
    version = "0.30.0-1"
  }, {
    name = "grug-far.nvim",
    url = "MagicDuck/grug-far.nvim",
    version = "1.6.53-1"
  }, {
    name = "gruvbox.nvim",
    url = "ellisonleao/gruvbox.nvim",
    version = "2.0.0-1"
  }, {
    name = "gtags.nvim",
    url = "wsdjeg/gtags.nvim",
    version = "0.2.0-1"
  }, {
    name = "guard.nvim",
    url = "nvimdev/guard.nvim",
    version = "2.6.2-1"
  }, {
    name = "hardhat.nvim",
    url = "TheSnakeWitcher/hardhat.nvim",
    version = "0.1.0-1"
  }, {
    name = "hardtime.nvim",
    url = "m4xshen/hardtime.nvim",
    version = "1.2.0-1"
  }, {
    name = "haskell-snippets.nvim",
    url = "mrcjkb/haskell-snippets.nvim",
    version = "1.5.0-1"
  }, {
    name = "haskell-tools.nvim",
    url = "mrcjkb/haskell-tools.nvim",
    version = "6.2.0-1"
  }, {
    name = "headlines.nvim",
    url = "lukas-reineke/headlines.nvim",
    version = "5.0.0-1"
  }, {
    name = "heirline.nvim",
    url = "rebelot/heirline.nvim",
    version = "1.0.8-1"
  }, {
    name = "helpview.nvim",
    url = "OXY2DEV/helpview.nvim",
    version = "2.1.2-1"
  }, {
    name = "hibiscus.nvim",
    url = "udayvir-singh/hibiscus.nvim",
    version = "1.7-1"
  }, {
    name = "hlchunk.nvim",
    url = "shellRaining/hlchunk.nvim",
    version = "1.3.0-1"
  }, {
    name = "hop.nvim",
    url = "wsdjeg/hop.nvim",
    version = "2.8.1-1"
  }, {
    name = "hotpot.nvim",
    url = "rktjmp/hotpot.nvim",
    version = "0.14.8-1"
  }, {
    name = "hurl.nvim",
    url = "jellydn/hurl.nvim",
    version = "2.2.0-1"
  }, {
    name = "hydra.nvim",
    url = "nvimtools/hydra.nvim",
    version = "1.0.3-1"
  }, {
    name = "iedit.nvim",
    url = "wsdjeg/iedit.nvim",
    version = "1.1.0-1"
  }, {
    name = "image.nvim",
    url = "3rd/image.nvim",
    version = "1.3.0-1"
  }, {
    name = "ime.nvim",
    url = "rimeinn/ime.nvim",
    version = "0.0.8-1"
  }, {
    name = "incline.nvim",
    url = "b0o/incline.nvim",
    version = "0.1.0-1"
  }, {
    name = "indent-blankline.nvim",
    url = "lukas-reineke/indent-blankline.nvim",
    version = "3.9.0-1"
  }, {
    name = "jieba.nvim",
    url = "Freed-Wu/jieba.nvim",
    version = "5.6.0-1"
  }, {
    name = "job.nvim",
    url = "wsdjeg/job.nvim",
    version = "1.3.0-1"
  }, {
    name = "kai.nvim",
    url = "Kamilcuk/kai.nvim",
    version = "0.0.6-1"
  }, {
    name = "kanban.nvim",
    url = "Kibadda/kanban.nvim",
    version = "1.4.0-1"
  }, {
    name = "keymap-guide.nvim",
    url = "wsdjeg/keymap-guide.nvim",
    version = "0.1.0-1"
  }, {
    name = "kube.nvim",
    url = "mimparat132/kube.nvim",
    version = "1.2.0-1"
  }, {
    name = "lazy.nvim",
    url = "folke/lazy.nvim",
    version = "11.17.5-1"
  }, {
    name = "lazydev.nvim",
    url = "folke/lazydev.nvim",
    version = "1.10.0-1"
  }, {
    name = "lean.nvim",
    url = "Julian/lean.nvim",
    version = "2025.10.1-1"
  }, {
    name = "leetcode.nvim",
    url = "kawre/leetcode.nvim",
    version = "0.3.1-1"
  }, {
    name = "legendary.nvim",
    url = "mrjones2014/legendary.nvim",
    version = "2.13.13-1"
  }, {
    name = "live-command.nvim",
    url = "smjonas/live-command.nvim",
    version = "2.2.0-1"
  }, {
    name = "live-preview.nvim",
    url = "brianhuster/live-preview.nvim",
    version = "0.9.5-1"
  }, {
    name = "logevent.nvim",
    url = "wsdjeg/logevent.nvim",
    version = "1.0.0-1"
  }, {
    name = "logger.nvim",
    url = "wsdjeg/logger.nvim",
    version = "1.1.0-1"
  }, {
    name = "logging.nvim",
    url = "NTBBloodbath/logging.nvim",
    version = "1.1.0-1"
  }, {
    name = "love2d.nvim",
    url = "S1M0N38/love2d.nvim",
    version = "2.1.0-1"
  }, {
    name = "lsp-format.nvim",
    url = "lukas-reineke/lsp-format.nvim",
    version = "2.7.2-1"
  }, {
    name = "lsp-progress.nvim",
    url = "linrongbin16/lsp-progress.nvim",
    version = "1.0.15-1"
  }, {
    name = "lsp_signature.nvim",
    url = "ray-x/lsp_signature.nvim",
    version = "0.3.1-1"
  }, {
    name = "ltreesitter",
    url = "euclidianAce/ltreesitter",
    version = "0.2.0-1"
  }, {
    name = "ltreesitter-ts",
    url = "FourierTransformer/ltreesitter-ts",
    version = "0.0.1-1"
  }, {
    name = "lua-console.nvim",
    url = "YaroSpace/lua-console.nvim",
    version = "1.2.5-1"
  }, {
    name = "lua-obfuscator.nvim",
    url = "git+ssh://git@github.com/kdssoftware/lua-obfuscator.nvim.git",
    version = "1.0.1-1"
  }, {
    name = "lua-tree-sitter",
    url = "xcb-xwii/lua-tree-sitter",
    version = "0.1.2-1"
  }, {
    name = "lua-utils.nvim",
    url = "nvim-neorg/lua-utils.nvim",
    version = "1.0.2-1"
  }, {
    name = "luarocks-build-tree-sitter-cli",
    url = "FourierTransformer/luarocks-build-tree-sitter-cli",
    version = "0.0.2-1"
  }, {
    name = "luarocks-build-treesitter-parser",
    url = "nvim-neorocks/luarocks-build-treesitter-parser",
    version = "6.0.1-1"
  }, {
    name = "luarocks-build-treesitter-parser-cpp",
    url = "nvim-neorocks/luarocks-build-treesitter-parser-cpp",
    version = "2.0.5-1"
  }, {
    name = "mag-nvim-lsp",
    url = "iguanacucumber/mag-nvim-lsp",
    version = "0.2-1"
  }, {
    name = "mag-nvim-lua",
    url = "iguanacucumber/mag-nvim-lua",
    version = "0.1-1"
  }, {
    name = "magazine.nvim",
    url = "iguanacucumber/magazine.nvim",
    version = "0.4.5-1"
  }, {
    name = "mapx.nvim",
    url = "b0o/mapx.nvim",
    version = "0.2.1-1"
  }, {
    name = "markdoc.nvim",
    url = "OXY2DEV/markdoc.nvim",
    version = "1.1.0-1"
  }, {
    name = "markdown-plus.nvim",
    url = "YousefHadder/markdown-plus.nvim",
    version = "1.9.1-1"
  }, {
    name = "markview.nvim",
    url = "OXY2DEV/markview.nvim",
    version = "27.0.0-1"
  }, {
    name = "mason-lspconfig.nvim",
    url = "williamboman/mason-lspconfig.nvim",
    version = "2.1.0-1"
  }, {
    name = "mason-nvim-dap.nvim",
    url = "jay-babu/mason-nvim-dap.nvim",
    version = "2.5.2-1"
  }, {
    name = "mason.nvim",
    url = "williamboman/mason.nvim",
    version = "2.1.0-1"
  }, {
    name = "mdtypes.nvim",
    url = "OXY2DEV/mdtypes.nvim",
    version = "1.0.0-1"
  }, {
    name = "melange-nvim",
    url = "savq/melange-nvim",
    version = "0.9.0-1"
  }, {
    name = "meow.yarn.nvim",
    url = "retran/meow.yarn.nvim",
    version = "0.1.1-1"
  }, {
    name = "mini.nvim",
    url = "echasnovski/mini.nvim",
    version = "0.16.0-1"
  }, {
    name = "minuet-ai.nvim",
    url = "milanglacier/minuet-ai.nvim",
    version = "0.8.0-1"
  }, {
    name = "mkdnflow.nvim",
    url = "jakewvincent/mkdnflow.nvim",
    version = "1.2.4-1"
  }, {
    name = "mona.nvim",
    url = "hydepwns/mona.nvim",
    version = "0.1.4-1"
  }, {
    name = "move.nvim",
    url = "fedepujol/move.nvim",
    version = "2.0.0-1"
  }, {
    name = "mru.nvim",
    url = "wsdjeg/mru.nvim",
    version = "1.4.0-1"
  }, {
    name = "multicursors.nvim",
    url = "smoka7/multicursors.nvim",
    version = "2.0.0-1"
  }, {
    name = "music-player.nvim",
    url = "wsdjeg/music-player.nvim",
    version = "1.0.2-1"
  }, {
    name = "my-awesome-plugin.nvim",
    url = "S1M0N38/my-awesome-plugin.nvim",
    version = "0.1.1-1"
  }, {
    name = "navigator.nvim",
    url = "numToStr/Navigator.nvim",
    version = "0.6-1"
  }, {
    name = "neo-tree.nvim",
    url = "nvim-neo-tree/neo-tree.nvim",
    version = "3.38.0-1"
  }, {
    name = "neoconf.nvim",
    url = "folke/neoconf.nvim",
    version = "1.4.0-1"
  }, {
    name = "neodev.nvim",
    url = "folke/neodev.nvim",
    version = "3.0.0-1"
  }, {
    name = "neogen",
    url = "danymat/neogen",
    version = "2.20.0-1"
  }, {
    name = "neogit",
    url = "NeogitOrg/neogit",
    version = "3.0.0-1"
  }, {
    name = "neorg",
    url = "nvim-neorg/neorg",
    version = "9.3.0-1"
  }, {
    name = "neorg-archive",
    url = "bottd/neorg-archive",
    version = "1.1.0-1"
  }, {
    name = "neorg-conceal-wrap",
    url = "benlubas/neorg-conceal-wrap",
    version = "1.0.1-1"
  }, {
    name = "neorg-interim-ls",
    url = "benlubas/neorg-interim-ls",
    version = "2.1.1-1"
  }, {
    name = "neorg-query",
    url = "benlubas/neorg-query",
    version = "1.4.0-1"
  }, {
    name = "neorg-se",
    url = "benlubas/neorg-se",
    version = "1.1.10-1"
  }, {
    name = "neorg-telescope",
    url = "nvim-neorg/neorg-telescope",
    version = "1.2.2-1"
  }, {
    name = "neorg-worklog",
    url = "bottd/neorg-worklog",
    version = "1.3.4-1"
  }, {
    name = "neoscroll.nvim",
    url = "karb94/neoscroll.nvim",
    version = "0.2.0-1"
  }, {
    name = "neotest",
    url = "nvim-neotest/neotest",
    version = "5.13.4-1"
  }, {
    name = "neotest-bun",
    url = "jutonz/neotest-bun",
    version = "0.1.2-1"
  }, {
    name = "neotest-busted",
    url = "MisanthropicBit/neotest-busted",
    version = "1.3.1-1"
  }, {
    name = "neotest-dotnet",
    url = "Issafalcon/neotest-dotnet",
    version = "stable-1"
  }, {
    name = "neotest-golang",
    url = "fredrikaverpil/neotest-golang",
    version = "2.6.0-1"
  }, {
    name = "neotest-haskell",
    url = "mrcjkb/neotest-haskell",
    version = "3.0.1-1"
  }, {
    name = "neotest-java",
    url = "rcasia/neotest-java",
    version = "0.22.6-1"
  }, {
    name = "neotest-kotlin",
    url = "codymikol/neotest-kotlin",
    version = "1.0.0-1"
  }, {
    name = "neotest-vstest",
    url = "Nsidorenco/neotest-vstest",
    version = "0.7.2-1"
  }, {
    name = "neotest-zig",
    url = "lawrence-laz/neotest-zig",
    version = "1.4.0-1"
  }, {
    name = "nerdy.nvim",
    url = "2KAbhishek/nerdy.nvim",
    version = "1.4-1"
  }, {
    name = "netman.nvim",
    url = "miversen33/netman.nvim",
    version = "1.15-1"
  }, {
    name = "nightfox.nvim",
    url = "EdenEast/nightfox.nvim",
    version = "3.10.0-1"
  }, {
    name = "no-neck-pain.nvim",
    url = "shortcuts/no-neck-pain.nvim",
    version = "2.5.2-1"
  }, {
    name = "noice.nvim",
    url = "folke/noice.nvim",
    version = "4.10.0-1"
  }, {
    name = "notes.nvim",
    url = "1321tremblay/notes.nvim",
    version = "0.1.0-1"
  }, {
    name = "notify.nvim",
    url = "wsdjeg/notify.nvim",
    version = "2.2.0-1"
  }, {
    name = "npackages.nvim",
    url = "diegofigs/npackages.nvim",
    version = "0.3.0-1"
  }, {
    name = "nui-components.nvim",
    url = "grapp-dev/nui-components.nvim",
    version = "1.5.3-1"
  }, {
    name = "nui.nvim",
    url = "MunifTanjim/nui.nvim",
    version = "0.4.0-1"
  }, {
    name = "nvim-a2-pack",
    url = "dfgordon/nvim-a2-pack",
    version = "1.0.0-1"
  }, {
    name = "nvim-autopairs",
    url = "windwp/nvim-autopairs",
    version = "0.10.0-1"
  }, {
    name = "nvim-best-practices-plugin-template",
    url = "ColinKennedy/nvim-best-practices-plugin-template",
    version = "1.11.0-1"
  }, {
    name = "nvim-bqf",
    url = "kevinhwang91/nvim-bqf",
    version = "1.1.1-1"
  }, {
    name = "nvim-client",
    url = "neovim/lua-client",
    version = "0.2.4-1"
  }, {
    name = "nvim-client-proxy",
    url = "hjdivad/nvim-client-proxy",
    version = "0.1.0-1"
  }, {
    name = "nvim-cokeline",
    url = "willothy/nvim-cokeline",
    version = "0.4.0-1"
  }, {
    name = "nvim-dap",
    url = "mfussenegger/nvim-dap",
    version = "0.10.0-1"
  }, {
    name = "nvim-dap-envfile",
    url = "ravsii/nvim-dap-envfile",
    version = "0.2.0-1"
  }, {
    name = "nvim-dap-ui",
    url = "rcarriga/nvim-dap-ui",
    version = "4.0.0-1"
  }, {
    name = "nvim-dev-container",
    url = "esensar/nvim-dev-container",
    version = "0.2.0-1"
  }, {
    name = "nvim-faker",
    url = "git+ssh://git@github.com/tehdb/nvim-faker.git",
    version = "1.0.0-1"
  }, {
    name = "nvim-java",
    url = "nvim-java/nvim-java",
    version = "1.0.0-1"
  }, {
    name = "nvim-java-core",
    url = "nvim-java/nvim-java-core",
    version = "1.0.0-1"
  }, {
    name = "nvim-java-dap",
    url = "nvim-java/nvim-java-dap",
    version = "1.0.0-1"
  }, {
    name = "nvim-jdtls",
    url = "mfussenegger/nvim-jdtls",
    version = "0.2.0-1"
  }, {
    name = "nvim-jqx",
    url = "gennaro-tedesco/nvim-jqx",
    version = "0.1.4-1"
  }, {
    name = "nvim-lastplace",
    url = "mrcjkb/nvim-lastplace",
    version = "1.0.0-1"
  }, {
    name = "nvim-lightbulb",
    url = "kosayoda/nvim-lightbulb",
    version = "1.0.0-1"
  }, {
    name = "nvim-lspconfig",
    url = "neovim/nvim-lspconfig",
    version = "2.5.0-1"
  }, {
    name = "nvim-metals",
    url = "scalameta/nvim-metals",
    version = "0.9.x-1"
  }, {
    name = "nvim-mkdocs-material",
    url = "https://codeberg.org/ambaradan/nvim-mkdocs-material/archive/0.1.3.zip",
    version = "0.1.3-1"
  }, {
    name = "nvim-nio",
    url = "nvim-neotest/nvim-nio",
    version = "1.10.1-1"
  }, {
    name = "nvim-notify",
    url = "rcarriga/nvim-notify",
    version = "3.15.0-1"
  }, {
    name = "nvim-parinfer",
    url = "gpanders/nvim-parinfer",
    version = "1.2.0-1"
  }, {
    name = "nvim-peekup",
    url = "gennaro-tedesco/nvim-peekup",
    version = "0.1.1-1"
  }, {
    name = "nvim-plug",
    url = "wsdjeg/nvim-plug",
    version = "0.6.0-1"
  }, {
    name = "nvim-possession",
    url = "gennaro-tedesco/nvim-possession",
    version = "0.3.1-1"
  }, {
    name = "nvim-scrollview",
    url = "dstein64/nvim-scrollview",
    version = "6.2.2-1"
  }, {
    name = "nvim-smuggler",
    url = "Klafyvel/nvim-smuggler",
    version = "0.5.0-1"
  }, {
    name = "nvim-snippets",
    url = "garymjr/nvim-snippets",
    version = "1.0.0-1"
  }, {
    name = "nvim-snippy",
    url = "dcampos/nvim-snippy",
    version = "1.0.0-1"
  }, {
    name = "nvim-surround",
    url = "kylechui/nvim-surround",
    version = "3.1.8-1"
  }, {
    name = "nvim-telescope-cycler",
    url = "heindsight/nvim-telescope-cycler",
    version = "0.1.0-1"
  }, {
    name = "nvim-textmate",
    url = "icedman/nvim-textmate",
    version = "0.0.1-1"
  }, {
    name = "nvim-thyme",
    url = "aileot/nvim-thyme",
    version = "1.6.1-1"
  }, {
    name = "nvim-tree.lua",
    url = "nvim-tree/nvim-tree.lua",
    version = "1.6.0-1"
  }, {
    name = "nvim-treesitter-context",
    url = "nvim-treesitter/nvim-treesitter-context",
    version = "1.0.0-1"
  }, {
    name = "nvim-treesitter-legacy-api",
    url = "nvim-treesitter/nvim-treesitter",
    version = "0.9.2-1"
  }, {
    name = "nvim-ufo",
    url = "kevinhwang91/nvim-ufo",
    version = "1.5.0-1"
  }, {
    name = "nvim-web-devicons",
    url = "nvim-tree/nvim-web-devicons",
    version = "0.100-1"
  }, {
    name = "nvim-window-picker",
    url = "s1n7ax/nvim-window-picker",
    version = "2.4.0-1"
  }, {
    name = "obazel.nvim",
    url = "glindstedt/obazel.nvim",
    version = "0.2.0-1"
  }, {
    name = "obsidian.nvim",
    url = "obsidian-nvim/obsidian.nvim",
    version = "3.14.7-1"
  }, {
    name = "oil.nvim",
    url = "stevearc/oil.nvim",
    version = "2.15.0-1"
  }, {
    name = "onedark.nvim",
    url = "navarasu/onedark.nvim",
    version = "1.0.3-1"
  }, {
    name = "onedarkpro.nvim",
    url = "olimorris/onedarkpro.nvim",
    version = "2.25.0-1"
  }, {
    name = "onenord.nvim",
    url = "rmehri01/onenord.nvim",
    version = "0.7.0-1"
  }, {
    name = "oops.nvim",
    url = "OXY2DEV/oops.nvim",
    version = "1.0.0-1"
  }, {
    name = "otter.nvim",
    url = "jmbuhr/otter.nvim",
    version = "2.13.4-1"
  }, {
    name = "overseer.nvim",
    url = "stevearc/overseer.nvim",
    version = "2.0.0-1"
  }, {
    name = "oz.nvim",
    url = "luxluth/oz.nvim",
    version = "0.0.4-1"
  }, {
    name = "package-info.nvim",
    url = "vuki656/package-info.nvim",
    version = "2.0-1"
  }, {
    name = "paperplanes.nvim",
    url = "rktjmp/paperplanes.nvim",
    version = "1.0.3-1"
  }, {
    name = "papis.nvim",
    url = "jghauser/papis.nvim",
    version = "0.9.1-1"
  }, {
    name = "paq-nvim",
    url = "savq/paq-nvim",
    version = "2.0.0-1"
  }, {
    name = "pathlib.nvim",
    url = "pysan3/pathlib.nvim",
    version = "2.2.3-1"
  }, {
    name = "patterns.nvim",
    url = "OXY2DEV/patterns.nvim",
    version = "2.1.1-1"
  }, {
    name = "persisted.nvim",
    url = "olimorris/persisted.nvim",
    version = "2.1.1-1"
  }, {
    name = "persistence.nvim",
    url = "folke/persistence.nvim",
    version = "3.1.0-1"
  }, {
    name = "picker.nvim",
    url = "wsdjeg/picker.nvim",
    version = "1.6.0-1"
  }, {
    name = "plenary.nvim",
    url = "nvim-lua/plenary.nvim",
    version = "0.1.4-1"
  }, {
    name = "pmd3.nvim",
    url = "https://codeberg.org/leso-kn/pmd3.nvim/archive/v0.1.1.zip",
    version = "0.1.1-1"
  }, {
    name = "presenterm.nvim",
    url = "Piotr1215/presenterm.nvim",
    version = "1.5.0-1"
  }, {
    name = "pretty-fold.nvim",
    url = "anuvyklack/pretty-fold.nvim",
    version = "3.0-1"
  }, {
    name = "processing.nvim",
    url = "sophieforrest/processing.nvim",
    version = "1.1.1-1"
  }, {
    name = "project.nvim",
    url = "DrKJeff16/project.nvim",
    version = "0.1.12-1"
  }, {
    name = "quarry.nvim",
    url = "rudionrails/quarry.nvim",
    version = "4.0.0-1"
  }, {
    name = "quick-todo.nvim",
    url = "SyedAsimShah1/quick-todo.nvim",
    version = "0.1.1-1"
  }, {
    name = "quicker.nvim",
    url = "stevearc/quicker.nvim",
    version = "1.4.0-1"
  }, {
    name = "quickfix.nvim",
    url = "wsdjeg/quickfix.nvim",
    version = "1.0.0-1"
  }, {
    name = "rainbow-delimiters.nvim",
    url = "HiPhish/rainbow-delimiters.nvim",
    version = "0.10.0-1"
  }, {
    name = "record-key.nvim",
    url = "wsdjeg/record-key.nvim",
    version = "1.4.0-1"
  }, {
    name = "record-screen.nvim",
    url = "wsdjeg/record-screen.nvim",
    version = "1.2.0-1"
  }, {
    name = "remember.nvim",
    url = "vladdoster/remember.nvim",
    version = "1.4.1-1"
  }, {
    name = "renamer.nvim",
    url = "filipdutescu/renamer.nvim",
    version = "5.1.0-1"
  }, {
    name = "render-markdown.nvim",
    url = "MeanderingProgrammer/render-markdown.nvim",
    version = "8.10.0-1"
  }, {
    name = "repl.nvim",
    url = "wsdjeg/repl.nvim",
    version = "1.0.0-1"
  }, {
    name = "rest.nvim",
    url = "rest-nvim/rest.nvim",
    version = "3.13.0-1"
  }, {
    name = "rikai.nvim",
    url = "teto/rikai.nvim",
    version = "0.0.1-1"
  }, {
    name = "rime.nvim",
    url = "rimeinn/rime.nvim",
    version = "0.2.14-1"
  }, {
    name = "rocks-config.nvim",
    url = "nvim-neorocks/rocks-config.nvim",
    version = "3.1.2-1"
  }, {
    name = "rocks-dev.nvim",
    url = "nvim-neorocks/rocks-dev.nvim",
    version = "1.8.1-1"
  }, {
    name = "rocks-git.nvim",
    url = "lumen-oss/rocks-git.nvim",
    version = "2.5.7-1"
  }, {
    name = "rocks-lazy.nvim",
    url = "nvim-neorocks/rocks-lazy.nvim",
    version = "1.2.2-1"
  }, {
    name = "rocks-treesitter.nvim",
    url = "nvim-neorocks/rocks-treesitter.nvim",
    version = "1.3.1-1"
  }, {
    name = "rocks.nvim",
    url = "lumen-oss/rocks.nvim",
    version = "2.46.1-1"
  }, {
    name = "rooter.nvim",
    url = "wsdjeg/rooter.nvim",
    version = "1.3.0-1"
  }, {
    name = "rtp.nvim",
    url = "nvim-neorocks/rtp.nvim",
    version = "1.2.0-1"
  }, {
    name = "runt.nvim",
    url = "Julian/runt.nvim",
    version = "2024.10.2-1"
  }, {
    name = "rustaceanvim",
    url = "mrcjkb/rustaceanvim",
    version = "7.0.6-2"
  }, {
    name = "schemastore.nvim",
    url = "b0o/SchemaStore.nvim",
    version = "0.2.0-1"
  }, {
    name = "scratch.nvim",
    url = "wsdjeg/scratch.nvim",
    version = "0.2.0-1"
  }, {
    name = "screenkey.nvim",
    url = "NStefan002/screenkey.nvim",
    version = "2.4.2-1"
  }, {
    name = "scrollbar.nvim",
    url = "Xuyuanp/scrollbar.nvim",
    version = "0.4.0-1"
  }, {
    name = "sense.nvim",
    url = "boltlessengineer/sense.nvim",
    version = "1.0.1-1"
  }, {
    name = "session.nvim",
    url = "Kibadda/session.nvim",
    version = "3.1.0-1"
  }, {
    name = "sf.nvim",
    url = "xixiaofinland/sf.nvim",
    version = "1.16.1-1"
  }, {
    name = "sg.nvim",
    url = "sourcegraph/sg.nvim",
    version = "1.1.0-1"
  }, {
    name = "smart-ime.nvim",
    url = "wsdjeg/smart-ime.nvim",
    version = "1.0.0-1"
  }, {
    name = "smart-splits.nvim",
    url = "mrjones2014/smart-splits.nvim",
    version = "2.0.5-1"
  }, {
    name = "snacks.nvim",
    url = "folke/snacks.nvim",
    version = "2.30.0-1"
  }, {
    name = "sos.nvim",
    url = "tmillr/sos.nvim",
    version = "1.0.0-1"
  }, {
    name = "squirrel.nvim",
    url = "xiaoshihou514/squirrel.nvim",
    version = "1.0.0-1"
  }, {
    name = "starter.nvim",
    url = "Kibadda/starter.nvim",
    version = "1.3.0-1"
  }, {
    name = "statusline.nvim",
    url = "wsdjeg/statusline.nvim",
    version = "1.0.0-1"
  }, {
    name = "storm-mode.nvim",
    url = "HoppenR/storm-mode.nvim",
    version = "1.2.0-1"
  }, {
    name = "string-natcmp",
    url = "mah0x211/lua-string-natcmp",
    version = "0.1.0-1"
  }, {
    name = "structlog.nvim",
    url = "git+ssh://git@github.com/Tastyep/structlog.nvim.git",
    version = "0.1-1"
  }, {
    name = "substitute.nvim",
    url = "gbprod/substitute.nvim",
    version = "2.0.0-1"
  }, {
    name = "sus.nvim",
    url = "TarunDaCoder/sus.nvim",
    version = "1.0.0-1"
  }, {
    name = "sweetie.nvim",
    url = "NTBBloodbath/sweetie.nvim",
    version = "3.2.0-1"
  }, {
    name = "tabby.nvim",
    url = "nanozuki/tabby.nvim",
    version = "2.8.0-1"
  }, {
    name = "tabline.nvim",
    url = "wsdjeg/tabline.nvim",
    version = "1.2.0-1"
  }, {
    name = "tangerine.nvim",
    url = "udayvir-singh/tangerine.nvim",
    version = "2.9-1"
  }, {
    name = "tasks.nvim",
    url = "wsdjeg/tasks.nvim",
    version = "2.0.1-1"
  }, {
    name = "teacup.neovim",
    url = "Clivern/teacup.neovim",
    version = "0.0.1-1"
  }, {
    name = "telescope-cmdline.nvim",
    url = "jonarrien/telescope-cmdline.nvim",
    version = "0.2.3-1"
  }, {
    name = "telescope-frecency.nvim",
    url = "nvim-telescope/telescope-frecency.nvim",
    version = "1.2.2-1"
  }, {
    name = "telescope-zf-native.nvim",
    url = "natecraddock/telescope-zf-native.nvim",
    version = "1.0.0-1"
  }, {
    name = "telescope.nvim",
    url = "nvim-telescope/telescope.nvim",
    version = "0.2.0-1"
  }, {
    name = "tellenc.nvim",
    url = "Freed-Wu/tellenc.nvim",
    version = "1.22-1"
  }, {
    name = "terminal.nvim",
    url = "wsdjeg/terminal.nvim",
    version = "1.1.0-1"
  }, {
    name = "todo-comments.nvim",
    url = "folke/todo-comments.nvim",
    version = "1.5.0-1"
  }, {
    name = "todo.nvim",
    url = "wsdjeg/todo.nvim",
    version = "1.0.0-1"
  }, {
    name = "toggleterm.nvim",
    url = "akinsho/toggleterm.nvim",
    version = "2.13.1-1"
  }, {
    name = "tokyonight.nvim",
    url = "folke/tokyonight.nvim",
    version = "4.14.1-1"
  }, {
    name = "toml.nvim",
    url = "wsdjeg/toml.nvim",
    version = "1.1.0-1"
  }, {
    name = "tree-sitter-ada",
    url = "briot/tree-sitter-ada",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-agda",
    url = "tree-sitter/tree-sitter-agda",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-angular",
    url = "dlvandenberg/tree-sitter-angular",
    version = "0.0.47-1"
  }, {
    name = "tree-sitter-apex",
    url = "aheber/tree-sitter-sfapex",
    version = "0.0.48-1"
  }, {
    name = "tree-sitter-arduino",
    url = "tree-sitter-grammars/tree-sitter-arduino",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-asm",
    url = "RubixDev/tree-sitter-asm",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-astro",
    url = "virchau13/tree-sitter-astro",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-authzed",
    url = "mleonidas/tree-sitter-authzed",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-awk",
    url = "Beaglefoot/tree-sitter-awk",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-bash",
    url = "tree-sitter/tree-sitter-bash",
    version = "0.0.49-1"
  }, {
    name = "tree-sitter-bass",
    url = "vito/tree-sitter-bass",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-beancount",
    url = "polarmutex/tree-sitter-beancount",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-bibtex",
    url = "latex-lsp/tree-sitter-bibtex",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-bicep",
    url = "tree-sitter-grammars/tree-sitter-bicep",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-bitbake",
    url = "tree-sitter-grammars/tree-sitter-bitbake",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-blade",
    url = "EmranMR/tree-sitter-blade",
    version = "0.0.8-1"
  }, {
    name = "tree-sitter-blueprint",
    url = "https://gitlab.com/gabmus/tree-sitter-blueprint/-/archive/355ef84ef8a958ac822117b652cf4d49bac16c79.zip",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-bp",
    url = "ambroisie/tree-sitter-bp",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-brightscript",
    url = "ajdelcimmuto/tree-sitter-brightscript",
    version = "0.0.3-1"
  }, {
    name = "tree-sitter-c",
    url = "tree-sitter/tree-sitter-c",
    version = "0.0.47-1"
  }, {
    name = "tree-sitter-c3",
    url = "c3lang/tree-sitter-c3",
    version = "0.0.8-1"
  }, {
    name = "tree-sitter-c_sharp",
    url = "tree-sitter/tree-sitter-c-sharp",
    version = "0.0.47-1"
  }, {
    name = "tree-sitter-caddy",
    url = "opa-oz/tree-sitter-caddy",
    version = "0.0.2-1"
  }, {
    name = "tree-sitter-cairo",
    url = "tree-sitter-grammars/tree-sitter-cairo",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-capnp",
    url = "tree-sitter-grammars/tree-sitter-capnp",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-chatito",
    url = "tree-sitter-grammars/tree-sitter-chatito",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-circom",
    url = "Decurity/tree-sitter-circom",
    version = "0.0.2-1"
  }, {
    name = "tree-sitter-cli",
    url = "FourierTransformer/tree-sitter-cli",
    version = "0.25.3-1"
  }, {
    name = "tree-sitter-clojure",
    url = "sogaiu/tree-sitter-clojure",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-cmake",
    url = "uyha/tree-sitter-cmake",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-comment",
    url = "stsewd/tree-sitter-comment",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-commonlisp",
    url = "tree-sitter-grammars/tree-sitter-commonlisp",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-cooklang",
    url = "addcninblue/tree-sitter-cooklang",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-corn",
    url = "jakestanger/tree-sitter-corn",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-cpon",
    url = "tree-sitter-grammars/tree-sitter-cpon",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-cpp",
    url = "tree-sitter/tree-sitter-cpp",
    version = "0.0.49-1"
  }, {
    name = "tree-sitter-css",
    url = "tree-sitter/tree-sitter-css",
    version = "0.0.39-1"
  }, {
    name = "tree-sitter-csv",
    url = "tree-sitter-grammars/tree-sitter-csv",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-cuda",
    url = "tree-sitter-grammars/tree-sitter-cuda",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-cue",
    url = "eonpatapon/tree-sitter-cue",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-cylc",
    url = "elliotfontaine/tree-sitter-cylc",
    version = "0.0.5-1"
  }, {
    name = "tree-sitter-d",
    url = "gdamore/tree-sitter-d",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-dart",
    url = "UserNobody14/tree-sitter-dart",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-desktop",
    url = "ValdezFOmar/tree-sitter-desktop",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-devicetree",
    url = "joelspadin/tree-sitter-devicetree",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-dhall",
    url = "jbellerb/tree-sitter-dhall",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-diff",
    url = "tree-sitter-grammars/tree-sitter-diff",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-disassembly",
    url = "ColinKennedy/tree-sitter-disassembly",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-djot",
    url = "treeman/tree-sitter-djot",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-dockerfile",
    url = "camdencheek/tree-sitter-dockerfile",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-dot",
    url = "rydesun/tree-sitter-dot",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-doxygen",
    url = "tree-sitter-grammars/tree-sitter-doxygen",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-dtd",
    url = "tree-sitter-grammars/tree-sitter-xml",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-earthfile",
    url = "glehmann/tree-sitter-earthfile",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-ebnf",
    url = "RubixDev/ebnf",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-ecma",
    url = "nvim-neorocks/luarocks-stub",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-editorconfig",
    url = "ValdezFOmar/tree-sitter-editorconfig",
    version = "0.0.61-1"
  }, {
    name = "tree-sitter-eds",
    url = "uyha/tree-sitter-eds",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-eex",
    url = "connorlay/tree-sitter-eex",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-elixir",
    url = "elixir-lang/tree-sitter-elixir",
    version = "0.0.43-1"
  }, {
    name = "tree-sitter-elm",
    url = "elm-tooling/tree-sitter-elm",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-elsa",
    url = "glapa-grossklag/tree-sitter-elsa",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-elvish",
    url = "elves/tree-sitter-elvish",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-embedded_template",
    url = "tree-sitter/tree-sitter-embedded-template",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-enforce",
    url = "simonvic/tree-sitter-enforce",
    version = "0.0.12-1"
  }, {
    name = "tree-sitter-erlang",
    url = "WhatsApp/tree-sitter-erlang",
    version = "0.0.48-1"
  }, {
    name = "tree-sitter-facility",
    url = "FacilityApi/tree-sitter-facility",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-faust",
    url = "khiner/tree-sitter-faust",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-fennel",
    url = "alexmozaidze/tree-sitter-fennel",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-fidl",
    url = "google/tree-sitter-fidl",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-firrtl",
    url = "tree-sitter-grammars/tree-sitter-firrtl",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-fish",
    url = "ram02z/tree-sitter-fish",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-foam",
    url = "FoamScience/tree-sitter-foam",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-forth",
    url = "AlexanderBrevig/tree-sitter-forth",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-fortran",
    url = "stadelmanma/tree-sitter-fortran",
    version = "0.0.53-1"
  }, {
    name = "tree-sitter-fsh",
    url = "mgramigna/tree-sitter-fsh",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-fsharp",
    url = "ionide/tree-sitter-fsharp",
    version = "0.0.17-1"
  }, {
    name = "tree-sitter-func",
    url = "tree-sitter-grammars/tree-sitter-func",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-fusion",
    url = "https://gitlab.com/jirgn/tree-sitter-fusion/-/archive/19db2f47ba4c3a0f6238d4ae0e2abfca16e61dd6.zip",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-gap",
    url = "gap-system/tree-sitter-gap",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-gaptst",
    url = "gap-system/tree-sitter-gaptst",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-gdscript",
    url = "PrestonKnopp/tree-sitter-gdscript",
    version = "0.0.46-1"
  }, {
    name = "tree-sitter-gdshader",
    url = "airblast-dev/tree-sitter-gdshader",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-git_config",
    url = "the-mikedavis/tree-sitter-git-config",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-git_rebase",
    url = "the-mikedavis/tree-sitter-git-rebase",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-gitattributes",
    url = "tree-sitter-grammars/tree-sitter-gitattributes",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-gitcommit",
    url = "gbprod/tree-sitter-gitcommit",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-gitignore",
    url = "shunsambongi/tree-sitter-gitignore",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-gleam",
    url = "gleam-lang/tree-sitter-gleam",
    version = "0.0.49-1"
  }, {
    name = "tree-sitter-glimmer",
    url = "ember-tooling/tree-sitter-glimmer",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-glimmer_javascript",
    url = "NullVoxPopuli/tree-sitter-glimmer-javascript",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-glimmer_typescript",
    url = "NullVoxPopuli/tree-sitter-glimmer-typescript",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-glsl",
    url = "tree-sitter-grammars/tree-sitter-glsl",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-gn",
    url = "tree-sitter-grammars/tree-sitter-gn",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-gnuplot",
    url = "dpezto/tree-sitter-gnuplot",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-go",
    url = "tree-sitter/tree-sitter-go",
    version = "0.0.43-1"
  }, {
    name = "tree-sitter-goctl",
    url = "chaozwn/tree-sitter-goctl",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-godot_resource",
    url = "PrestonKnopp/tree-sitter-godot-resource",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-gomod",
    url = "camdencheek/tree-sitter-go-mod",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-gosum",
    url = "tree-sitter-grammars/tree-sitter-go-sum",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-gotmpl",
    url = "ngalaiko/tree-sitter-go-template",
    version = "0.0.41-1"
  }, {
    name = "tree-sitter-gowork",
    url = "omertuc/tree-sitter-go-work",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-gpg",
    url = "tree-sitter-grammars/tree-sitter-gpg-config",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-graphql",
    url = "bkegley/tree-sitter-graphql",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-gren",
    url = "MaeBrooks/tree-sitter-gren",
    version = "0.0.7-1"
  }, {
    name = "tree-sitter-groovy",
    url = "murtaza64/tree-sitter-groovy",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-groq",
    url = "ajrussellaudio/tree-sitter-groq",
    version = "0.0.3-1"
  }, {
    name = "tree-sitter-gstlaunch",
    url = "tree-sitter-grammars/tree-sitter-gstlaunch",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-hack",
    url = "slackhq/tree-sitter-hack",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-hare",
    url = "tree-sitter-grammars/tree-sitter-hare",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-haskell",
    url = "tree-sitter-grammars/tree-sitter-haskell",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-haskell_persistent",
    url = "MercuryTechnologies/tree-sitter-haskell-persistent",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-hcl",
    url = "tree-sitter-grammars/tree-sitter-hcl",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-heex",
    url = "connorlay/tree-sitter-heex",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-helm",
    url = "ngalaiko/tree-sitter-go-template",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-hjson",
    url = "winston0410/tree-sitter-hjson",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-hlsl",
    url = "tree-sitter-grammars/tree-sitter-hlsl",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-hlsplaylist",
    url = "Freed-Wu/tree-sitter-hlsplaylist",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-hocon",
    url = "antosha417/tree-sitter-hocon",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-hoon",
    url = "urbit-pilled/tree-sitter-hoon",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-html",
    url = "tree-sitter/tree-sitter-html",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-html_tags",
    url = "nvim-neorocks/luarocks-stub",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-htmldjango",
    url = "interdependence/tree-sitter-htmldjango",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-http",
    url = "rest-nvim/tree-sitter-http",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-hurl",
    url = "pfeiferj/tree-sitter-hurl",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-hyprlang",
    url = "tree-sitter-grammars/tree-sitter-hyprlang",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-idl",
    url = "cathaysia/tree-sitter-idl",
    version = "0.0.42-1"
  }, {
    name = "tree-sitter-idris",
    url = "kayhide/tree-sitter-idris",
    version = "0.0.1-1"
  }, {
    name = "tree-sitter-ini",
    url = "justinmk/tree-sitter-ini",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-inko",
    url = "inko-lang/tree-sitter-inko",
    version = "0.0.52-1"
  }, {
    name = "tree-sitter-ipkg",
    url = "srghma/tree-sitter-ipkg",
    version = "0.0.1-1"
  }, {
    name = "tree-sitter-ispc",
    url = "tree-sitter-grammars/tree-sitter-ispc",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-janet_simple",
    url = "sogaiu/tree-sitter-janet-simple",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-java",
    url = "tree-sitter/tree-sitter-java",
    version = "0.0.46-1"
  }, {
    name = "tree-sitter-javadoc",
    url = "rmuir/tree-sitter-javadoc",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-javascript",
    url = "tree-sitter/tree-sitter-javascript",
    version = "0.0.41-1"
  }, {
    name = "tree-sitter-jinja",
    url = "cathaysia/tree-sitter-jinja",
    version = "0.0.10-1"
  }, {
    name = "tree-sitter-jinja_inline",
    url = "cathaysia/tree-sitter-jinja",
    version = "0.0.14-1"
  }, {
    name = "tree-sitter-jq",
    url = "flurie/tree-sitter-jq",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-jsdoc",
    url = "tree-sitter/tree-sitter-jsdoc",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-json",
    url = "tree-sitter/tree-sitter-json",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-json5",
    url = "Joakker/tree-sitter-json5",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-jsonc",
    url = "https://gitlab.com/WhyNotHugo/tree-sitter-jsonc/-/archive/02b01653c8a1c198ae7287d566efa86a135b30d5.zip",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-jsonnet",
    url = "sourcegraph/tree-sitter-jsonnet",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-jsx",
    url = "nvim-neorocks/luarocks-stub",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-julia",
    url = "tree-sitter-grammars/tree-sitter-julia",
    version = "0.0.49-1"
  }, {
    name = "tree-sitter-just",
    url = "IndianBoy42/tree-sitter-just",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-kcl",
    url = "kcl-lang/tree-sitter-kcl",
    version = "0.0.2-1"
  }, {
    name = "tree-sitter-kconfig",
    url = "tree-sitter-grammars/tree-sitter-kconfig",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-kdl",
    url = "tree-sitter-grammars/tree-sitter-kdl",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-kitty",
    url = "OXY2DEV/tree-sitter-kitty",
    version = "0.0.5-1"
  }, {
    name = "tree-sitter-kotlin",
    url = "fwcd/tree-sitter-kotlin",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-koto",
    url = "koto-lang/tree-sitter-koto",
    version = "0.0.51-1"
  }, {
    name = "tree-sitter-kusto",
    url = "Willem-J-an/tree-sitter-kusto",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-lalrpop",
    url = "traxys/tree-sitter-lalrpop",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-latex",
    url = "latex-lsp/tree-sitter-latex",
    version = "0.0.41-1"
  }, {
    name = "tree-sitter-ledger",
    url = "cbarrete/tree-sitter-ledger",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-leo",
    url = "r001/tree-sitter-leo",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-linkerscript",
    url = "tree-sitter-grammars/tree-sitter-linkerscript",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-liquid",
    url = "hankthetank27/tree-sitter-liquid",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-liquidsoap",
    url = "savonet/tree-sitter-liquidsoap",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-llvm",
    url = "benwilliamgraham/tree-sitter-llvm",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-lua",
    url = "tree-sitter-grammars/tree-sitter-lua",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-luadoc",
    url = "tree-sitter-grammars/tree-sitter-luadoc",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-luap",
    url = "tree-sitter-grammars/tree-sitter-luap",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-luau",
    url = "tree-sitter-grammars/tree-sitter-luau",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-m68k",
    url = "grahambates/tree-sitter-m68k",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-make",
    url = "alemuller/tree-sitter-make",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-markdown",
    url = "tree-sitter-grammars/tree-sitter-markdown",
    version = "0.0.45-1"
  }, {
    name = "tree-sitter-markdown_inline",
    url = "tree-sitter-grammars/tree-sitter-markdown",
    version = "0.0.43-1"
  }, {
    name = "tree-sitter-matlab",
    url = "acristoffers/tree-sitter-matlab",
    version = "0.0.51-1"
  }, {
    name = "tree-sitter-menhir",
    url = "Kerl13/tree-sitter-menhir",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-mermaid",
    url = "monaqa/tree-sitter-mermaid",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-meson",
    url = "tree-sitter-grammars/tree-sitter-meson",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-mlir",
    url = "artagnon/tree-sitter-mlir",
    version = "0.0.83-1"
  }, {
    name = "tree-sitter-muttrc",
    url = "neomutt/tree-sitter-muttrc",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-nasm",
    url = "naclsn/tree-sitter-nasm",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-nginx",
    url = "opa-oz/tree-sitter-nginx",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-nickel",
    url = "nickel-lang/tree-sitter-nickel",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-nim",
    url = "alaviss/tree-sitter-nim",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-nim_format_string",
    url = "aMOPel/tree-sitter-nim-format-string",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-ninja",
    url = "alemuller/tree-sitter-ninja",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-nix",
    url = "nix-community/tree-sitter-nix",
    version = "0.0.67-1"
  }, {
    name = "tree-sitter-norg",
    url = "nvim-neorg/tree-sitter-norg",
    version = "0.2.6-1"
  }, {
    name = "tree-sitter-norg-meta",
    url = "nvim-neorg/tree-sitter-norg-meta",
    version = "0.1.0-1"
  }, {
    name = "tree-sitter-nqc",
    url = "tree-sitter-grammars/tree-sitter-nqc",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-nu",
    url = "nushell/tree-sitter-nu",
    version = "0.0.60-1"
  }, {
    name = "tree-sitter-objc",
    url = "tree-sitter-grammars/tree-sitter-objc",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-objdump",
    url = "ColinKennedy/tree-sitter-objdump",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-ocaml",
    url = "tree-sitter/tree-sitter-ocaml",
    version = "0.0.46-1"
  }, {
    name = "tree-sitter-ocaml_interface",
    url = "tree-sitter/tree-sitter-ocaml",
    version = "0.0.47-1"
  }, {
    name = "tree-sitter-ocamllex",
    url = "atom-ocaml/tree-sitter-ocamllex",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-odin",
    url = "tree-sitter-grammars/tree-sitter-odin",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-org",
    url = "milisims/tree-sitter-org",
    version = "0.0.1-1"
  }, {
    name = "tree-sitter-orgmode",
    url = "nvim-orgmode/tree-sitter-org",
    version = "2.0.2-1"
  }, {
    name = "tree-sitter-pascal",
    url = "Isopod/tree-sitter-pascal",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-passwd",
    url = "ath3/tree-sitter-passwd",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-pem",
    url = "tree-sitter-grammars/tree-sitter-pem",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-perl",
    url = "tree-sitter-perl/tree-sitter-perl",
    version = "0.0.48-1"
  }, {
    name = "tree-sitter-php",
    url = "tree-sitter/tree-sitter-php",
    version = "0.0.51-1"
  }, {
    name = "tree-sitter-php_only",
    url = "tree-sitter/tree-sitter-php",
    version = "0.0.55-1"
  }, {
    name = "tree-sitter-phpdoc",
    url = "claytonrcarter/tree-sitter-phpdoc",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-pioasm",
    url = "leo60228/tree-sitter-pioasm",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-pkl",
    url = "apple/tree-sitter-pkl",
    version = "0.0.11-1"
  }, {
    name = "tree-sitter-po",
    url = "tree-sitter-grammars/tree-sitter-po",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-pod",
    url = "tree-sitter-perl/tree-sitter-pod",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-poe_filter",
    url = "tree-sitter-grammars/tree-sitter-poe-filter",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-pony",
    url = "tree-sitter-grammars/tree-sitter-pony",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-powershell",
    url = "airbus-cert/tree-sitter-powershell",
    version = "0.0.48-1"
  }, {
    name = "tree-sitter-printf",
    url = "tree-sitter-grammars/tree-sitter-printf",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-prisma",
    url = "victorhqc/tree-sitter-prisma",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-problog",
    url = "foxyseta/tree-sitter-prolog",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-prolog",
    url = "foxyseta/tree-sitter-prolog",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-promql",
    url = "MichaHoffmann/tree-sitter-promql",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-properties",
    url = "tree-sitter-grammars/tree-sitter-properties",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-proto",
    url = "treywood/tree-sitter-proto",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-prql",
    url = "PRQL/tree-sitter-prql",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-psv",
    url = "tree-sitter-grammars/tree-sitter-csv",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-pug",
    url = "zealot128/tree-sitter-pug",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-puppet",
    url = "tree-sitter-grammars/tree-sitter-puppet",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-purescript",
    url = "postsolar/tree-sitter-purescript",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-pymanifest",
    url = "tree-sitter-grammars/tree-sitter-pymanifest",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-python",
    url = "tree-sitter/tree-sitter-python",
    version = "0.0.46-1"
  }, {
    name = "tree-sitter-ql",
    url = "tree-sitter/tree-sitter-ql",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-qmldir",
    url = "tree-sitter-grammars/tree-sitter-qmldir",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-qmljs",
    url = "yuja/tree-sitter-qmljs",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-query",
    url = "tree-sitter-grammars/tree-sitter-query",
    version = "0.0.47-1"
  }, {
    name = "tree-sitter-r",
    url = "r-lib/tree-sitter-r",
    version = "0.0.39-1"
  }, {
    name = "tree-sitter-racket",
    url = "6cdh/tree-sitter-racket",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-ralph",
    url = "alephium/tree-sitter-ralph",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-rasi",
    url = "Fymyte/tree-sitter-rasi",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-razor",
    url = "tris203/tree-sitter-razor",
    version = "0.0.3-1"
  }, {
    name = "tree-sitter-rbs",
    url = "joker1007/tree-sitter-rbs",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-re2c",
    url = "tree-sitter-grammars/tree-sitter-re2c",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-readline",
    url = "tree-sitter-grammars/tree-sitter-readline",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-regex",
    url = "tree-sitter/tree-sitter-regex",
    version = "0.0.41-1"
  }, {
    name = "tree-sitter-rego",
    url = "FallenAngel97/tree-sitter-rego",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-requirements",
    url = "tree-sitter-grammars/tree-sitter-requirements",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-rescript",
    url = "rescript-lang/tree-sitter-rescript",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-rifleconf",
    url = "purarue/tree-sitter-rifleconf",
    version = "0.0.3-1"
  }, {
    name = "tree-sitter-rnoweb",
    url = "bamonroe/tree-sitter-rnoweb",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-robot",
    url = "Hubro/tree-sitter-robot",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-robots",
    url = "opa-oz/tree-sitter-robots-txt",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-roc",
    url = "faldor20/tree-sitter-roc",
    version = "0.0.40-1"
  }, {
    name = "tree-sitter-ron",
    url = "tree-sitter-grammars/tree-sitter-ron",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-rst",
    url = "stsewd/tree-sitter-rst",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-ruby",
    url = "tree-sitter/tree-sitter-ruby",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-runescript",
    url = "2004Scape/tree-sitter-runescript",
    version = "0.0.1-1"
  }, {
    name = "tree-sitter-rust",
    url = "tree-sitter/tree-sitter-rust",
    version = "0.0.55-1"
  }, {
    name = "tree-sitter-scala",
    url = "tree-sitter/tree-sitter-scala",
    version = "0.0.55-1"
  }, {
    name = "tree-sitter-scfg",
    url = "rockorager/tree-sitter-scfg",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-scheme",
    url = "6cdh/tree-sitter-scheme",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-scss",
    url = "serenadeai/tree-sitter-scss",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-sflog",
    url = "aheber/tree-sitter-sfapex",
    version = "0.0.44-1"
  }, {
    name = "tree-sitter-slang",
    url = "tree-sitter-grammars/tree-sitter-slang",
    version = "0.0.36-1"
  }, {
    name = "tree-sitter-slim",
    url = "theoo/tree-sitter-slim",
    version = "0.0.7-1"
  }, {
    name = "tree-sitter-slint",
    url = "slint-ui/tree-sitter-slint",
    version = "0.0.44-1"
  }, {
    name = "tree-sitter-smali",
    url = "tree-sitter-grammars/tree-sitter-smali",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-smithy",
    url = "indoorvivants/tree-sitter-smithy",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-snakemake",
    url = "osthomas/tree-sitter-snakemake",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-snl",
    url = "minijackson/tree-sitter-snl",
    version = "0.0.2-1"
  }, {
    name = "tree-sitter-solidity",
    url = "JoranHonig/tree-sitter-solidity",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-soql",
    url = "aheber/tree-sitter-sfapex",
    version = "0.0.46-1"
  }, {
    name = "tree-sitter-sosl",
    url = "aheber/tree-sitter-sfapex",
    version = "0.0.44-1"
  }, {
    name = "tree-sitter-sourcepawn",
    url = "nilshelmig/tree-sitter-sourcepawn",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-sparql",
    url = "GordianDziwis/tree-sitter-sparql",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-sproto",
    url = "hanxi/tree-sitter-sproto",
    version = "0.0.2-1"
  }, {
    name = "tree-sitter-sql",
    url = "derekstride/tree-sitter-sql",
    version = "0.0.49-1"
  }, {
    name = "tree-sitter-squirrel",
    url = "tree-sitter-grammars/tree-sitter-squirrel",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-ssh_config",
    url = "tree-sitter-grammars/tree-sitter-ssh-config",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-starlark",
    url = "tree-sitter-grammars/tree-sitter-starlark",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-strace",
    url = "sigmaSd/tree-sitter-strace",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-styled",
    url = "mskelton/tree-sitter-styled",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-supercollider",
    url = "madskjeldgaard/tree-sitter-supercollider",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-superhtml",
    url = "kristoff-it/superhtml",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-surface",
    url = "connorlay/tree-sitter-surface",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-svelte",
    url = "tree-sitter-grammars/tree-sitter-svelte",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-sway",
    url = "FuelLabs/tree-sitter-sway",
    version = "0.0.5-1"
  }, {
    name = "tree-sitter-swift",
    url = "alex-pinkus/tree-sitter-swift",
    version = "0.0.59-1"
  }, {
    name = "tree-sitter-sxhkdrc",
    url = "RaafatTurki/tree-sitter-sxhkdrc",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-systemtap",
    url = "ok-ryoko/tree-sitter-systemtap",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-systemverilog",
    url = "gmlarumbe/tree-sitter-systemverilog",
    version = "0.0.45-1"
  }, {
    name = "tree-sitter-t32",
    url = "xasc/tree-sitter-t32",
    version = "0.0.57-1"
  }, {
    name = "tree-sitter-tablegen",
    url = "tree-sitter-grammars/tree-sitter-tablegen",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-tact",
    url = "tact-lang/tree-sitter-tact",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-tcl",
    url = "tree-sitter-grammars/tree-sitter-tcl",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-teal",
    url = "euclidianAce/tree-sitter-teal",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-templ",
    url = "vrischmann/tree-sitter-templ",
    version = "0.0.55-1"
  }, {
    name = "tree-sitter-tera",
    url = "uncenter/tree-sitter-tera",
    version = "0.0.8-1"
  }, {
    name = "tree-sitter-terraform",
    url = "MichaHoffmann/tree-sitter-hcl",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-textproto",
    url = "PorterAtGoogle/tree-sitter-textproto",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-thrift",
    url = "tree-sitter-grammars/tree-sitter-thrift",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-tiger",
    url = "ambroisie/tree-sitter-tiger",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-tlaplus",
    url = "tlaplus-community/tree-sitter-tlaplus",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-tmux",
    url = "Freed-Wu/tree-sitter-tmux",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-todotxt",
    url = "arnarg/tree-sitter-todotxt",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-toml",
    url = "tree-sitter-grammars/tree-sitter-toml",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-tsv",
    url = "tree-sitter-grammars/tree-sitter-csv",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-tsx",
    url = "tree-sitter/tree-sitter-typescript",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-turtle",
    url = "GordianDziwis/tree-sitter-turtle",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-twig",
    url = "gbprod/tree-sitter-twig",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-typescript",
    url = "tree-sitter/tree-sitter-typescript",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-typespec",
    url = "happenslol/tree-sitter-typespec",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-typoscript",
    url = "Teddytrombone/tree-sitter-typoscript",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-typst",
    url = "uben0/tree-sitter-typst",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-udev",
    url = "tree-sitter-grammars/tree-sitter-udev",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-ungrammar",
    url = "tree-sitter-grammars/tree-sitter-ungrammar",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-unison",
    url = "kylegoetz/tree-sitter-unison",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-usd",
    url = "ColinKennedy/tree-sitter-usd",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-uxntal",
    url = "tree-sitter-grammars/tree-sitter-uxntal",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-v",
    url = "vlang/v-analyzer",
    version = "0.0.52-1"
  }, {
    name = "tree-sitter-vala",
    url = "vala-lang/tree-sitter-vala",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-vento",
    url = "ventojs/tree-sitter-vento",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-verilog",
    url = "gmlarumbe/tree-sitter-systemverilog",
    version = "0.0.39-1"
  }, {
    name = "tree-sitter-vhdl",
    url = "jpt13653903/tree-sitter-vhdl",
    version = "0.0.52-1"
  }, {
    name = "tree-sitter-vhs",
    url = "charmbracelet/tree-sitter-vhs",
    version = "0.0.34-1"
  }, {
    name = "tree-sitter-vim",
    url = "tree-sitter-grammars/tree-sitter-vim",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-vimdoc",
    url = "neovim/tree-sitter-vimdoc",
    version = "0.0.38-1"
  }, {
    name = "tree-sitter-vrl",
    url = "belltoy/tree-sitter-vrl",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-vue",
    url = "tree-sitter-grammars/tree-sitter-vue",
    version = "0.0.33-1"
  }, {
    name = "tree-sitter-wgsl",
    url = "szebniok/tree-sitter-wgsl",
    version = "0.0.31-1"
  }, {
    name = "tree-sitter-wgsl_bevy",
    url = "tree-sitter-grammars/tree-sitter-wgsl-bevy",
    version = "0.0.32-1"
  }, {
    name = "tree-sitter-wing",
    url = "winglang/tree-sitter-wing",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-wit",
    url = "bytecodealliance/tree-sitter-wit",
    version = "0.0.35-1"
  }, {
    name = "tree-sitter-wxml",
    url = "BlockLune/tree-sitter-wxml",
    version = "0.0.2-1"
  }, {
    name = "tree-sitter-xcompose",
    url = "tree-sitter-grammars/tree-sitter-xcompose",
    version = "0.0.30-1"
  }, {
    name = "tree-sitter-xml",
    url = "tree-sitter-grammars/tree-sitter-xml",
    version = "0.0.42-1"
  }, {
    name = "tree-sitter-xresources",
    url = "ValdezFOmar/tree-sitter-xresources",
    version = "0.0.41-1"
  }, {
    name = "tree-sitter-yaml",
    url = "tree-sitter-grammars/tree-sitter-yaml",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-yang",
    url = "Hubro/tree-sitter-yang",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-ysh",
    url = "danyspin97/tree-sitter-ysh",
    version = "0.0.2-1"
  }, {
    name = "tree-sitter-yuck",
    url = "tree-sitter-grammars/tree-sitter-yuck",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-zathurarc",
    url = "Freed-Wu/tree-sitter-zathurarc",
    version = "0.0.29-1"
  }, {
    name = "tree-sitter-zig",
    url = "tree-sitter-grammars/tree-sitter-zig",
    version = "0.0.37-1"
  }, {
    name = "tree-sitter-ziggy",
    url = "kristoff-it/ziggy",
    version = "0.0.19-1"
  }, {
    name = "tree-sitter-ziggy_schema",
    url = "kristoff-it/ziggy",
    version = "0.0.20-1"
  }, {
    name = "treedoc.nvim",
    url = "neo451/treedoc.nvim",
    version = "1.0.3-1"
  }, {
    name = "trouble.nvim",
    url = "folke/trouble.nvim",
    version = "3.7.1-1"
  }, {
    name = "ts-comments.nvim",
    url = "folke/ts-comments.nvim",
    version = "1.5.0-1"
  }, {
    name = "tsc.nvim",
    url = "dmmulroy/tsc.nvim",
    version = "2.9.0-1"
  }, {
    name = "twilight.nvim",
    url = "folke/twilight.nvim",
    version = "1.0.0-1"
  }, {
    name = "u.nvim",
    url = "jrop/u.nvim",
    version = "0.2.0-1"
  }, {
    name = "ui.nvim",
    url = "OXY2DEV/ui.nvim",
    version = "1.4.1-1"
  }, {
    name = "unimpaired.nvim",
    url = "tummetott/unimpaired.nvim",
    version = "0.4.0-1"
  }, {
    name = "unnest.nvim",
    url = "brianhuster/unnest.nvim",
    version = "0.1.1-1"
  }, {
    name = "utils.nvim",
    url = "wsdjeg/utils.nvim",
    version = "1.0.0-1"
  }, {
    name = "vgit.nvim",
    url = "tanvirtin/vgit.nvim",
    version = "1.0.6-1"
  }, {
    name = "visual-surround.nvim",
    url = "NStefan002/visual-surround.nvim",
    version = "1.0.1-1"
  }, {
    name = "which-key.nvim",
    url = "folke/which-key.nvim",
    version = "3.17.0-1"
  }, {
    name = "winbar.nvim",
    url = "wsdjeg/winbar.nvim",
    version = "1.0.0-1"
  }, {
    name = "windline.nvim",
    url = "windwp/windline.nvim",
    version = "1.1.0-1"
  }, {
    name = "winmove.nvim",
    url = "MisanthropicBit/winmove.nvim",
    version = "1.0.0-1"
  }, {
    name = "wormhole.nvim",
    url = "NStefan002/wormhole.nvim",
    version = "1.1.1-1"
  }, {
    name = "wrapping-paper.nvim",
    url = "benlubas/wrapping-paper.nvim",
    version = "1.0.0-1"
  }, {
    name = "yanky.nvim",
    url = "gbprod/yanky.nvim",
    version = "2.0.0-1"
  }, {
    name = "yarepl.nvim",
    url = "milanglacier/yarepl.nvim",
    version = "0.11.0-1"
  }, {
    name = "yazi.nvim",
    url = "mikavilpas/yazi.nvim",
    version = "13.1.0-1"
  }, {
    name = "zen-mode.nvim",
    url = "folke/zen-mode.nvim",
    version = "1.4.1-1"
  }, {
    name = "zettelkasten.nvim",
    url = "wsdjeg/zettelkasten.nvim",
    version = "2.1.0-1"
  }, {
    name = "zk-nvim",
    url = "zk-org/zk-nvim",
    version = "0.4.6-1"
  } }
```

## File: `lua/lazy/core/cache.lua`
```
local uv = vim.uv or vim.loop

local M = {}

---@alias CacheHash {mtime: {sec:number, nsec:number}, size:number}
---@alias CacheEntry {hash:CacheHash, chunk:string}

---@class ModuleFindOpts
---@field all? boolean Search for all matches (defaults to `false`)
---@field rtp? boolean Search for modname in the runtime path (defaults to `true`)
---@field patterns? string[] Patterns to use (defaults to `{"/init.lua", ".lua"}`)
---@field paths? string[] Extra paths to search for modname

---@class ModuleInfo
---@field modpath string Path of the module
---@field modname string Name of the module
---@field stat? uv_fs_t File stat of the module path

---@alias LoaderStats table<string, {total:number, time:number, [string]:number?}?>

M.path = vim.fn.stdpath("cache") .. "/luac"
M.enabled = false

---@class Loader
---@field _rtp string[]
---@field _rtp_pure string[]
---@field _rtp_key string
local Loader = {
  VERSION = 3,
  ---@type table<string, table<string,ModuleInfo>>
  _indexed = {},
  ---@type table<string, string[]>
  _topmods = {},
  _loadfile = loadfile,
  ---@type LoaderStats
  _stats = {
    find = { total = 0, time = 0, not_found = 0 },
  },
}

--- Tracks the time spent in a function
---@private
function Loader.track(stat, start)
  Loader._stats[stat] = Loader._stats[stat] or { total = 0, time = 0 }
  Loader._stats[stat].total = Loader._stats[stat].total + 1
  Loader._stats[stat].time = Loader._stats[stat].time + uv.hrtime() - start
end

--- slightly faster/different version than vim.fs.normalize
--- we also need to have it here, since the loader will load vim.fs
---@private
function Loader.normalize(path)
  if path:sub(1, 1) == "~" then
    local home = uv.os_homedir() or "~"
    if home:sub(-1) == "\\" or home:sub(-1) == "/" then
      home = home:sub(1, -2)
    end
    path = home .. path:sub(2)
  end
  path = path:gsub("\\", "/"):gsub("/+", "/")
  return path:sub(-1) == "/" and path:sub(1, -2) or path
end

--- Gets the rtp excluding after directories.
--- The result is cached, and will be updated if the runtime path changes.
--- When called from a fast event, the cached value will be returned.
--- @return string[] rtp, boolean updated
---@private
function Loader.get_rtp()
  local start = uv.hrtime()
  if vim.in_fast_event() then
    Loader.track("get_rtp", start)
    return (Loader._rtp or {}), false
  end
  local updated = false
  local key = vim.go.rtp
  if key ~= Loader._rtp_key then
    Loader._rtp = {}
    for _, path in ipairs(vim.api.nvim_get_runtime_file("", true)) do
      path = Loader.normalize(path)
      -- skip after directories
      if path:sub(-6, -1) ~= "/after" and not (Loader._indexed[path] and vim.tbl_isempty(Loader._indexed[path])) then
        Loader._rtp[#Loader._rtp + 1] = path
      end
    end
    updated = true
    Loader._rtp_key = key
  end
  Loader.track("get_rtp", start)
  return Loader._rtp, updated
end

--- Returns the cache file name
---@param name string can be a module name, or a file name
---@return string file_name
---@private
function Loader.cache_file(name)
  local ret = M.path .. "/" .. name:gsub("[/\\:]", "%%")
  return ret:sub(-4) == ".lua" and (ret .. "c") or (ret .. ".luac")
end

--- Saves the cache entry for a given module or file
---@param name string module name or filename
---@param entry CacheEntry
---@private
function Loader.write(name, entry)
  local cname = Loader.cache_file(name)
  local f = assert(uv.fs_open(cname, "w", 438))
  local header = {
    Loader.VERSION,
    entry.hash.size,
    entry.hash.mtime.sec,
    entry.hash.mtime.nsec,
  }
  uv.fs_write(f, table.concat(header, ",") .. "\0")
  uv.fs_write(f, entry.chunk)
  uv.fs_close(f)
end

--- Loads the cache entry for a given module or file
---@param name string module name or filename
---@return CacheEntry?
---@private
function Loader.read(name)
  local start = uv.hrtime()
  local cname = Loader.cache_file(name)
  local f = uv.fs_open(cname, "r", 438)
  if f then
    local hash = uv.fs_fstat(f) --[[@as CacheHash]]
    local data = uv.fs_read(f, hash.size, 0) --[[@as string]]
    uv.fs_close(f)

    local zero = data:find("\0", 1, true)
    if not zero then
      return
    end

    ---@type integer[]|{[0]:integer}
    local header = vim.split(data:sub(1, zero - 1), ",")
    if tonumber(header[1]) ~= Loader.VERSION then
      return
    end
    Loader.track("read", start)
    return {
      hash = { size = tonumber(header[2]), mtime = { sec = tonumber(header[3]), nsec = tonumber(header[4]) } },
      chunk = data:sub(zero + 1),
    }
  end
  Loader.track("read", start)
end

--- The `package.loaders` loader for lua files using the cache.
---@param modname string module name
---@return string|function
---@private
function Loader.loader(modname)
  local start = uv.hrtime()
  local ret = M.find(modname)[1]
  if ret then
    local chunk, err = Loader.load(ret.modpath, { hash = ret.stat })
    Loader.track("loader", start)
    return chunk or error(err)
  end
  Loader.track("loader", start)
  return "\ncache_loader: module " .. modname .. " not found"
end

--- The `package.loaders` loader for libs
---@param modname string module name
---@return string|function
---@private
function Loader.loader_lib(modname)
  local start = uv.hrtime()
  local sysname = uv.os_uname().sysname:lower() or ""
  local is_win = sysname:find("win", 1, true) and not sysname:find("darwin", 1, true)
  local ret = M.find(modname, { patterns = is_win and { ".dll" } or { ".so" } })[1]
  ---@type function?, string?
  if ret then
    -- Making function name in Lua 5.1 (see src/loadlib.c:mkfuncname) is
    -- a) strip prefix up to and including the first dash, if any
    -- b) replace all dots by underscores
    -- c) prepend "luaopen_"
    -- So "foo-bar.baz" should result in "luaopen_bar_baz"
    local dash = modname:find("-", 1, true)
    local funcname = dash and modname:sub(dash + 1) or modname
    local chunk, err = package.loadlib(ret.modpath, "luaopen_" .. funcname:gsub("%.", "_"))
    Loader.track("loader_lib", start)
    return chunk or error(err)
  end
  Loader.track("loader_lib", start)
  return "\ncache_loader_lib: module " .. modname .. " not found"
end

--- `loadfile` using the cache
---@param filename? string
---@param mode? "b"|"t"|"bt"
---@param env? table
---@param hash? CacheHash
---@return function?, string?  error_message
---@private
-- luacheck: ignore 312
function Loader.loadfile(filename, mode, env, hash)
  local start = uv.hrtime()
  filename = Loader.normalize(filename)
  mode = nil -- ignore mode, since we byte-compile the lua source files
  local chunk, err = Loader.load(filename, { mode = mode, env = env, hash = hash })
  Loader.track("loadfile", start)
  return chunk, err
end

--- Checks whether two cache hashes are the same based on:
--- * file size
--- * mtime in seconds
--- * mtime in nanoseconds
---@param h1 CacheHash
---@param h2 CacheHash
---@private
function Loader.eq(h1, h2)
  return h1 and h2 and h1.size == h2.size and h1.mtime.sec == h2.mtime.sec and h1.mtime.nsec == h2.mtime.nsec
end

--- Loads the given module path using the cache
---@param modpath string
---@param opts? {hash?: CacheHash, mode?: "b"|"t"|"bt", env?:table} (table|nil) Options for loading the module:
---    - hash: (table) the hash of the file to load if it is already known. (defaults to `vim.uv.fs_stat({modpath})`)
---    - mode: (string) the mode to load the module with. "b"|"t"|"bt" (defaults to `nil`)
---    - env: (table) the environment to load the module in. (defaults to `nil`)
---@see |luaL_loadfile()|
---@return function?, string? error_message
---@private
function Loader.load(modpath, opts)
  local start = uv.hrtime()

  opts = opts or {}
  local hash = opts.hash or uv.fs_stat(modpath)
  ---@type function?, string?
  local chunk, err

  if not hash then
    -- trigger correct error
    chunk, err = Loader._loadfile(modpath, opts.mode, opts.env)
    Loader.track("load", start)
    return chunk, err
  end

  local entry = Loader.read(modpath)
  if entry and Loader.eq(entry.hash, hash) then
    -- found in cache and up to date
    -- selene: allow(incorrect_standard_library_use)
    chunk, err = load(entry.chunk --[[@as string]], "@" .. modpath, opts.mode, opts.env)
    if not (err and err:find("cannot load incompatible bytecode", 1, true)) then
      Loader.track("load", start)
      return chunk, err
    end
  end
  entry = { hash = hash, modpath = modpath }

  chunk, err = Loader._loadfile(modpath, opts.mode, opts.env)
  if chunk then
    entry.chunk = string.dump(chunk)
    Loader.write(modpath, entry)
  end
  Loader.track("load", start)
  return chunk, err
end

--- Finds lua modules for the given module name.
---@param modname string Module name, or `"*"` to find the top-level modules instead
---@param opts? ModuleFindOpts (table|nil) Options for finding a module:
---    - rtp: (boolean) Search for modname in the runtime path (defaults to `true`)
---    - paths: (string[]) Extra paths to search for modname (defaults to `{}`)
---    - patterns: (string[]) List of patterns to use when searching for modules.
---                A pattern is a string added to the basename of the Lua module being searched.
---                (defaults to `{"/init.lua", ".lua"}`)
---    - all: (boolean) Return all matches instead of just the first one (defaults to `false`)
---@return ModuleInfo[] (list) A list of results with the following properties:
---    - modpath: (string) the path to the module
---    - modname: (string) the name of the module
---    - stat: (table|nil) the fs_stat of the module path. Won't be returned for `modname="*"`
function M.find(modname, opts)
  local start = uv.hrtime()
  opts = opts or {}

  modname = modname:gsub("/", ".")
  local basename = modname:gsub("%.", "/")
  local idx = modname:find(".", 1, true)

  -- HACK: fix incorrect require statements. Really not a fan of keeping this,
  -- but apparently the regular lua loader also allows this
  if idx == 1 then
    modname = modname:gsub("^%.+", "")
    basename = modname:gsub("%.", "/")
    idx = modname:find(".", 1, true)
  end

  -- get the top-level module name
  local topmod = idx and modname:sub(1, idx - 1) or modname

  -- OPTIM: search for a directory first when topmod == modname
  local patterns = opts.patterns or (topmod == modname and { "/init.lua", ".lua" } or { ".lua", "/init.lua" })
  for p, pattern in ipairs(patterns) do
    patterns[p] = "/lua/" .. basename .. pattern
  end

  ---@type ModuleInfo[]
  local results = {}

  -- Only continue if we haven't found anything yet or we want to find all
  ---@private
  local function continue()
    return #results == 0 or opts.all
  end

  -- Checks if the given paths contain the top-level module.
  -- If so, it tries to find the module path for the given module name.
  ---@param paths string[]
  ---@private
  local function _find(paths)
    for _, path in ipairs(paths) do
      if topmod == "*" then
        for _, r in pairs(Loader.lsmod(path)) do
          results[#results + 1] = r
          if not continue() then
            return
          end
        end
      elseif Loader.lsmod(path)[topmod] then
        for _, pattern in ipairs(patterns) do
          local modpath = path .. pattern
          Loader._stats.find.stat = (Loader._stats.find.stat or 0) + 1
          local hash = uv.fs_stat(modpath)
          if hash then
            results[#results + 1] = { modpath = modpath, stat = hash, modname = modname }
            if not continue() then
              return
            end
          end
        end
      end
    end
  end

  -- always check the rtp first
  if opts.rtp ~= false then
    _find(Loader._rtp or {})
    if continue() then
      local rtp, updated = Loader.get_rtp()
      if updated then
        _find(rtp)
      end
    end
  end

  -- check any additional paths
  if continue() and opts.paths then
    _find(opts.paths)
  end

  Loader.track("find", start)
  if #results == 0 then
    -- module not found
    Loader._stats.find.not_found = Loader._stats.find.not_found + 1
  end

  return results
end

--- Resets the topmods cache for the path, or all the paths
--- if path is nil.
---@param path string? path to reset
function M.reset(path)
  if path then
    Loader._indexed[Loader.normalize(path)] = nil
  else
    Loader._indexed = {}
  end
end

--- Enables the experimental Lua module loader:
--- * overrides loadfile
--- * adds the lua loader using the byte-compilation cache
--- * adds the libs loader
--- * removes the default Neovim loader
function M.enable()
  if M.enabled then
    return
  end
  M.enabled = true
  vim.fn.mkdir(vim.fn.fnamemodify(M.path, ":p"), "p")
  -- selene: allow(global_usage)
  _G.loadfile = Loader.loadfile
  -- add lua loader
  table.insert(package.loaders, 2, Loader.loader)
  -- add libs loader
  table.insert(package.loaders, 3, Loader.loader_lib)
  -- remove Neovim loader
  for l, loader in ipairs(package.loaders) do
    if loader == vim._load_package then
      table.remove(package.loaders, l)
      break
    end
  end

  -- this will reset the top-mods in case someone adds a new
  -- top-level lua module to a path already on the rtp
  vim.api.nvim_create_autocmd("BufWritePost", {
    group = vim.api.nvim_create_augroup("cache_topmods_reset", { clear = true }),
    callback = function(event)
      local bufname = event.match ---@type string
      local idx = bufname:find("/lua/", 1, true)
      if idx then
        M.reset(bufname:sub(1, idx - 1))
      end
    end,
  })
end

--- Disables the experimental Lua module loader:
--- * removes the loaders
--- * adds the default Neovim loader
function M.disable()
  if not M.enabled then
    return
  end
  M.enabled = false
  -- selene: allow(global_usage)
  _G.loadfile = Loader._loadfile
  ---@diagnostic disable-next-line: no-unknown
  for l, loader in ipairs(package.loaders) do
    if loader == Loader.loader or loader == Loader.loader_lib then
      table.remove(package.loaders, l)
    end
  end
  table.insert(package.loaders, 2, vim._load_package)
  vim.api.nvim_del_augroup_by_name("cache_topmods_reset")
end

--- Return the top-level `/lua/*` modules for this path
---@param path string path to check for top-level lua modules
---@private
function Loader.lsmod(path)
  if not Loader._indexed[path] then
    local start = uv.hrtime()
    Loader._indexed[path] = {}
    local handle = uv.fs_scandir(path .. "/lua")
    while handle do
      local name, t = uv.fs_scandir_next(handle)
      if not name then
        break
      end
      local modpath = path .. "/lua/" .. name
      -- HACK: type is not always returned due to a bug in luv
      t = t or uv.fs_stat(modpath).type
      ---@type string
      local topname
      local ext = name:sub(-4)
      if ext == ".lua" or ext == ".dll" then
        topname = name:sub(1, -5)
      elseif name:sub(-3) == ".so" then
        topname = name:sub(1, -4)
      elseif t == "link" or t == "directory" then
        topname = name
      end
      if topname then
        Loader._indexed[path][topname] = { modpath = modpath, modname = topname }
        Loader._topmods[topname] = Loader._topmods[topname] or {}
        if not vim.tbl_contains(Loader._topmods[topname], path) then
          table.insert(Loader._topmods[topname], path)
        end
      end
    end
    Loader.track("lsmod", start)
  end
  return Loader._indexed[path]
end

--- Debug function that wraps all loaders and tracks stats
---@private
function M._profile_loaders()
  for l, loader in pairs(package.loaders) do
    local loc = debug.getinfo(loader, "Sn").source:sub(2)
    package.loaders[l] = function(modname)
      local start = uv.hrtime()
      local ret = loader(modname)
      Loader.track("loader " .. l .. ": " .. loc, start)
      Loader.track("loader_all", start)
      return ret
    end
  end
end

--- Prints all cache stats
---@param opts? {print?:boolean}
---@return LoaderStats
---@private
function M._inspect(opts)
  if opts and opts.print then
    ---@private
    local function ms(nsec)
      return math.floor(nsec / 1e6 * 1000 + 0.5) / 1000 .. "ms"
    end
    local chunks = {} ---@type string[][]
    ---@type string[]
    local stats = vim.tbl_keys(Loader._stats)
    table.sort(stats)
    for _, stat in ipairs(stats) do
      vim.list_extend(chunks, {
        { "\n" .. stat .. "\n", "Title" },
        { "* total:    " },
        { tostring(Loader._stats[stat].total) .. "\n", "Number" },
        { "* time:     " },
        { ms(Loader._stats[stat].time) .. "\n", "Bold" },
        { "* avg time: " },
        { ms(Loader._stats[stat].time / Loader._stats[stat].total) .. "\n", "Bold" },
      })
      for k, v in pairs(Loader._stats[stat]) do
        if not vim.tbl_contains({ "time", "total" }, k) then
          chunks[#chunks + 1] = { "* " .. k .. ":" .. string.rep(" ", 9 - #k) }
          chunks[#chunks + 1] = { tostring(v) .. "\n", "Number" }
        end
      end
    end
    vim.api.nvim_echo(chunks, true, {})
  end
  return Loader._stats
end

return M
```

## File: `lua/lazy/core/config.lua`
```
local Util = require("lazy.core.util")

---@class LazyCoreConfig
local M = {}

---@class LazyConfig
M.defaults = {
  root = vim.fn.stdpath("data") .. "/lazy", -- directory where plugins will be installed
  defaults = {
    -- Set this to `true` to have all your plugins lazy-loaded by default.
    -- Only do this if you know what you are doing, as it can lead to unexpected behavior.
    lazy = false, -- should plugins be lazy-loaded?
    -- It's recommended to leave version=false for now, since a lot the plugin that support versioning,
    -- have outdated releases, which may break your Neovim install.
    version = nil, -- always use the latest git commit
    -- version = "*", -- try installing the latest stable version for plugins that support semver
    -- default `cond` you can use to globally disable a lot of plugins
    -- when running inside vscode for example
    cond = nil, ---@type boolean|fun(self:LazyPlugin):boolean|nil
  },
  -- leave nil when passing the spec as the first argument to setup()
  spec = nil, ---@type LazySpec
  local_spec = true, -- load project specific .lazy.lua spec files. They will be added at the end of the spec.
  lockfile = vim.fn.stdpath("config") .. "/lazy-lock.json", -- lockfile generated after running update.
  ---@type number? limit the maximum amount of concurrent tasks
  concurrency = jit.os:find("Windows") and (vim.uv.available_parallelism() * 2) or nil,
  git = {
    -- defaults for the `Lazy log` command
    -- log = { "--since=3 days ago" }, -- show commits from the last 3 days
    log = { "-8" }, -- show the last 8 commits
    timeout = 120, -- kill processes that take more than 2 minutes
    url_format = "https://github.com/%s.git",
    -- lazy.nvim requires git >=2.19.0. If you really want to use lazy with an older version,
    -- then set the below to false. This should work, but is NOT supported and will
    -- increase downloads a lot.
    filter = true,
    -- rate of network related git operations (clone, fetch, checkout)
    throttle = {
      enabled = false, -- not enabled by default
      -- max 2 ops every 5 seconds
      rate = 2,
      duration = 5 * 1000, -- in ms
    },
    -- Time in seconds to wait before running fetch again for a plugin.
    -- Repeated update/check operations will not run again until this
    -- cooldown period has passed.
    cooldown = 0,
  },
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
    server = "https://lumen-oss.github.io/rocks-binaries/",
    -- use hererocks to install luarocks?
    -- set to `nil` to use hererocks when luarocks is not found
    -- set to `true` to always use hererocks
    -- set to `false` to always use luarocks
    hererocks = nil,
  },
  dev = {
    -- Directory where you store your local plugin projects. If a function is used,
    -- the plugin directory (e.g. `~/projects/plugin-name`) must be returned.
    ---@type string | fun(plugin: LazyPlugin): string
    path = "~/projects",
    ---@type string[] plugins that match these patterns will use your local versions instead of being fetched from GitHub
    patterns = {}, -- For example {"folke"}
    fallback = false, -- Fallback to git when local plugin doesn't exist
  },
  install = {
    -- install missing plugins on startup. This doesn't increase startup time.
    missing = true,
    -- try to load one of these colorschemes when starting an installation during startup
    colorscheme = { "habamax" },
  },
  ui = {
    -- a number <1 is a percentage., >1 is a fixed size
    size = { width = 0.8, height = 0.8 },
    wrap = true, -- wrap the lines in the ui
    -- The border to use for the UI window. Accepts same border values as |nvim_open_win()|.
    border = "none",
    -- The backdrop opacity. 0 is fully opaque, 100 is fully transparent.
    backdrop = 60,
    title = nil, ---@type string only works when border is not "none"
    title_pos = "center", ---@type "center" | "left" | "right"
    -- Show pills on top of the Lazy window
    pills = true, ---@type boolean
    icons = {
      cmd = " ",
      config = "",
      debug = "● ",
      event = " ",
      favorite = " ",
      ft = " ",
      init = " ",
      import = " ",
      keys = " ",
      lazy = "󰒲 ",
      loaded = "●",
      not_loaded = "○",
      plugin = " ",
      runtime = " ",
      require = "󰢱 ",
      source = " ",
      start = " ",
      task = "✔ ",
      list = {
        "●",
        "➜",
        "★",
        "‒",
      },
    },
    -- leave nil, to automatically select a browser depending on your OS.
    -- If you want to use a specific browser, you can define it here
    browser = nil, ---@type string?
    throttle = 1000 / 30, -- how frequently should the ui process render events
    custom_keys = {
      -- You can define custom key maps here. If present, the description will
      -- be shown in the help menu.
      -- To disable one of the defaults, set it to false.

      ["<localleader>l"] = {
        function(plugin)
          require("lazy.util").float_term({ "lazygit", "log" }, {
            cwd = plugin.dir,
          })
        end,
        desc = "Open lazygit log",
      },

      ["<localleader>i"] = {
        function(plugin)
          Util.notify(vim.inspect(plugin), {
            title = "Inspect " .. plugin.name,
            lang = "lua",
          })
        end,
        desc = "Inspect Plugin",
      },

      ["<localleader>t"] = {
        function(plugin)
          require("lazy.util").float_term(nil, {
            cwd = plugin.dir,
          })
        end,
        desc = "Open terminal in plugin dir",
      },
    },
  },
  -- Output options for headless mode
  headless = {
    -- show the output from process commands like git
    process = true,
    -- show log messages
    log = true,
    -- show task start/end
    task = true,
    -- use ansi colors
    colors = true,
  },
  diff = {
    -- diff command <d> can be one of:
    -- * browser: opens the github compare view. Note that this is always mapped to <K> as well,
    --   so you can have a different command for diff <d>
    -- * git: will run git diff and open a buffer with filetype git
    -- * terminal_git: will open a pseudo terminal with git diff
    -- * diffview.nvim: will open Diffview to show the diff
    cmd = "git",
  },
  checker = {
    -- automatically check for plugin updates
    enabled = false,
    concurrency = nil, ---@type number? set to 1 to check for updates very slowly
    notify = true, -- get a notification when new updates are found
    frequency = 3600, -- check for updates every hour
    check_pinned = false, -- check for pinned packages that can't be updated
  },
  change_detection = {
    -- automatically check for config file changes and reload the ui
    enabled = true,
    notify = true, -- get a notification when changes are found
  },
  performance = {
    cache = {
      enabled = true,
    },
    reset_packpath = true, -- reset the package path to improve startup time
    rtp = {
      reset = true, -- reset the runtime path to $VIMRUNTIME and your config directory
      ---@type string[]
      paths = {}, -- add any custom paths here that you want to includes in the rtp
      ---@type string[] list any plugins you want to disable here
      disabled_plugins = {
        -- "gzip",
        -- "matchit",
        -- "matchparen",
        -- "netrwPlugin",
        -- "tarPlugin",
        -- "tohtml",
        -- "tutor",
        -- "zipPlugin",
      },
    },
  },
  -- lazy can generate helptags from the headings in markdown readme files,
  -- so :help works even for plugins that don't have vim docs.
  -- when the readme opens with :help it will be correctly displayed as markdown
  readme = {
    enabled = true,
    root = vim.fn.stdpath("state") .. "/lazy/readme",
    files = { "README.md", "lua/**/README.md" },
    -- only generate markdown helptags for plugins that don't have docs
    skip_if_doc_exists = true,
  },
  state = vim.fn.stdpath("state") .. "/lazy/state.json", -- state info for checker and other things
  -- Enable profiling of lazy.nvim. This will add some overhead,
  -- so only enable this when you are debugging lazy.nvim
  profiling = {
    -- Enables extra stats on the debug tab related to the loader cache.
    -- Additionally gathers stats about all package.loaders
    loader = false,
    -- Track each new require in the Lazy profiling tab
    require = false,
  },
  debug = false,
}

function M.hererocks()
  if M.options.rocks.hererocks == nil then
    M.options.rocks.hererocks = vim.fn.executable("luarocks") == 0
  end
  return M.options.rocks.hererocks
end

M.version = "11.17.5" -- x-release-please-version

M.ns = vim.api.nvim_create_namespace("lazy")

---@type LazySpecLoader
M.spec = nil

---@type table<string, LazyPlugin>
M.plugins = {}

---@type LazyPlugin[]
M.to_clean = {}

---@type LazyConfig
M.options = {}

---@type string
M.me = nil

---@type string
M.mapleader = nil

---@type string
M.maplocalleader = nil

M.suspended = false

function M.headless()
  return not M.suspended and #vim.api.nvim_list_uis() == 0
end

---@param opts? LazyConfig
function M.setup(opts)
  M.options = vim.tbl_deep_extend("force", M.defaults, opts or {})

  if type(M.options.spec) == "string" then
    M.options.spec = { import = M.options.spec }
  end
  table.insert(M.options.install.colorscheme, "habamax")

  -- root
  M.options.root = Util.norm(M.options.root)
  if type(M.options.dev.path) == "string" then
    M.options.dev.path = Util.norm(M.options.dev.path)
  end
  M.options.lockfile = Util.norm(M.options.lockfile)
  M.options.readme.root = Util.norm(M.options.readme.root)

  vim.fn.mkdir(M.options.root, "p")

  if M.options.performance.reset_packpath then
    vim.go.packpath = vim.env.VIMRUNTIME
  end

  M.me = debug.getinfo(1, "S").source:sub(2)
  M.me = Util.norm(vim.fn.fnamemodify(M.me, ":p:h:h:h:h"))
  local lib = vim.fn.fnamemodify(vim.v.progpath, ":p:h:h") .. "/lib"
  lib = vim.uv.fs_stat(lib .. "64") and (lib .. "64") or lib
  lib = lib .. "/nvim"
  if M.options.performance.rtp.reset then
    ---@type vim.Option
    vim.opt.rtp = {
      vim.fn.stdpath("config"),
      vim.fn.stdpath("data") .. "/site",
      M.me,
      vim.env.VIMRUNTIME,
      lib,
      vim.fn.stdpath("config") .. "/after",
    }
  end
  for _, path in ipairs(M.options.performance.rtp.paths) do
    vim.opt.rtp:append(path)
  end
  vim.opt.rtp:append(M.options.readme.root)

  -- disable plugin loading since we do all of that ourselves
  vim.go.loadplugins = false
  M.mapleader = vim.g.mapleader
  M.maplocalleader = vim.g.maplocalleader

  vim.api.nvim_create_autocmd("UIEnter", {
    once = true,
    callback = function()
      require("lazy.stats").on_ui_enter()
    end,
  })

  if M.headless() then
    require("lazy.view.commands").setup()
  else
    vim.api.nvim_create_autocmd("User", {
      pattern = "VeryLazy",
      once = true,
      callback = function()
        require("lazy.view.commands").setup()
        if M.options.change_detection.enabled then
          require("lazy.manage.reloader").enable()
        end
        if M.options.checker.enabled then
          vim.defer_fn(function()
            require("lazy.manage.checker").start()
          end, 10)
        end

        -- useful for plugin developers when making changes to a packspec file
        vim.api.nvim_create_autocmd("BufWritePost", {
          pattern = { "lazy.lua", "pkg.json", "*.rockspec" },
          callback = function()
            local plugin = require("lazy.core.plugin").find(vim.uv.cwd() .. "/lua/")
            if plugin then
              require("lazy").pkg({ plugins = { plugin } })
            end
          end,
        })

        vim.api.nvim_create_autocmd({ "VimSuspend", "VimResume" }, {
          callback = function(ev)
            M.suspended = ev.event == "VimSuspend"
          end,
        })
      end,
    })
  end

  Util.very_lazy()
end

return M
```

## File: `lua/lazy/core/fragments.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.core.util")

--- This class is used to manage the fragments of a plugin spec.
--- It keeps track of the fragments and their relations to other fragments.
--- A fragment can be a dependency (dependencies) or a child (specs) of another fragment.
---@class LazyFragments
---@field fragments table<number, LazyFragment>
---@field frag_stack number[]
---@field dep_stack number[]
---@field dirty table<number, boolean>
---@field plugins table<LazyPlugin, number>
---@field spec LazySpecLoader
local M = {}

M._fid = 0

local function next_id()
  M._fid = M._fid + 1
  return M._fid
end

---@param spec LazySpecLoader
---@return LazyFragments
function M.new(spec)
  local self = setmetatable({}, { __index = M })
  self.fragments = {}
  self.frag_stack = {}
  self.dep_stack = {}
  self.spec = spec
  self.dirty = {}
  self.plugins = {}
  return self
end

---@param id number
function M:get(id)
  return self.fragments[id]
end

--- Remove a fragment and all its children.
--- This will also remove the fragment from its parent's children list.
---@param id number
function M:del(id)
  -- del fragment
  local fragment = self.fragments[id]
  if not fragment then
    return
  end

  self.dirty[id] = true

  -- remove from parent
  local pid = fragment.pid
  if pid then
    local parent = self.fragments[pid]
    if parent.frags then
      ---@param fid number
      parent.frags = Util.filter(function(fid)
        return fid ~= id
      end, parent.frags)
    end
    if parent.deps then
      ---@param fid number
      parent.deps = Util.filter(function(fid)
        return fid ~= id
      end, parent.deps)
    end
    self.dirty[pid] = true
  end

  -- remove children
  if fragment.frags then
    for _, fid in ipairs(fragment.frags) do
      self:del(fid)
    end
  end

  self.fragments[id] = nil
end

--- Add a fragment to the fragments list.
--- This also resolves its name, url, dir, dependencies and child specs.
---@param plugin LazyPluginSpec
function M:add(plugin)
  if self.plugins[plugin] then
    return self.fragments[self.plugins[plugin]]
  end

  local id = next_id()
  setmetatable(plugin, nil)

  self.plugins[plugin] = id

  local pid = self.frag_stack[#self.frag_stack]

  ---@type LazyFragment
  local fragment = {
    id = id,
    pid = pid,
    name = plugin.name,
    url = plugin.url,
    dir = plugin.dir,
    spec = plugin --[[@as LazyPlugin]],
  }

  -- short url / ref
  if plugin[1] then
    local slash = plugin[1]:find("/", 1, true)
    if slash then
      local prefix = plugin[1]:sub(1, 4)
      if prefix == "http" or prefix == "git@" then
        fragment.url = fragment.url or plugin[1]
      else
        fragment.name = fragment.name or plugin[1]:sub(slash + 1)
        fragment.url = fragment.url or Config.options.git.url_format:format(plugin[1])
      end
    else
      fragment.name = fragment.name or plugin[1]
    end
  end

  -- name
  fragment.name = fragment.name
    or fragment.url and self.spec.get_name(fragment.url)
    or fragment.dir and self.spec.get_name(fragment.dir)
  if not fragment.name or fragment.name == "" then
    return self.spec:error("Invalid plugin spec " .. vim.inspect(plugin))
  end

  if type(plugin.config) == "table" then
    self.spec:warn(
      "{" .. fragment.name .. "}: setting a table to `Plugin.config` is deprecated. Please use `Plugin.opts` instead"
    )
    ---@diagnostic disable-next-line: assign-type-mismatch
    plugin.opts = plugin.config
    plugin.config = nil
  end

  self.fragments[id] = fragment

  -- add to parent
  if pid then
    local parent = self.fragments[pid]
    parent.frags = parent.frags or {}
    table.insert(parent.frags, id)
  end

  -- add to parent's deps
  local did = self.dep_stack[#self.dep_stack]
  if did and did == pid then
    fragment.dep = true
    local parent = self.fragments[did]
    parent.deps = parent.deps or {}
    table.insert(parent.deps, id)
  end

  table.insert(self.frag_stack, id)
  -- dependencies
  if plugin.dependencies then
    table.insert(self.dep_stack, id)
    self.spec:normalize(plugin.dependencies)
    table.remove(self.dep_stack)
  end
  -- child specs
  if plugin.specs then
    self.spec:normalize(plugin.specs)
  end
  table.remove(self.frag_stack)

  return fragment
end

return M
```

## File: `lua/lazy/core/loader.lua`
```
local Cache = require("lazy.core.cache")
local Config = require("lazy.core.config")
local Handler = require("lazy.core.handler")
local Plugin = require("lazy.core.plugin")
local Util = require("lazy.core.util")

---@class LazyCoreLoader
local M = {}

local DEFAULT_PRIORITY = 50

---@type LazyPlugin[]
M.loading = {}
M.init_done = false
---@type table<string,true>
M.disabled_rtp_plugins = { packer_compiled = true }
---@type table<string,string>
M.did_ftdetect = {}
M.did_handlers = false

function M.disable_rtp_plugin(plugin)
  M.disabled_rtp_plugins[plugin] = true
end

function M.setup()
  for _, file in ipairs(Config.options.performance.rtp.disabled_plugins) do
    M.disable_rtp_plugin(file)
  end

  vim.api.nvim_create_autocmd("ColorSchemePre", {
    callback = function(event)
      M.colorscheme(event.match)
    end,
  })

  -- load the plugins
  Plugin.load()
  Handler.init()

  -- install missing plugins
  if Config.options.install.missing then
    Util.track("install")
    local count = 0
    while M.install_missing() do
      count = count + 1
      if count > 5 then
        Util.error("Too many rounds of missing plugins")
        break
      end
    end
    Util.track()
  end
  Config.mapleader = vim.g.mapleader
  Config.maplocalleader = vim.g.maplocalleader

  -- report any warnings & errors
  Config.spec:report()

  -- setup handlers
  Util.track("handlers")
  Handler.setup()
  M.did_handlers = true
  Util.track()
end

-- this will incrementally install missing plugins
-- multiple rounds can happen when importing a spec from a missing plugin
function M.install_missing()
  for _, plugin in pairs(Config.plugins) do
    local installed = plugin._.installed
    local has_errors = Plugin.has_errors(plugin)

    if not has_errors and not (installed and not plugin._.build) then
      for _, colorscheme in ipairs(Config.options.install.colorscheme) do
        if colorscheme == "default" then
          break
        end
        M.colorscheme(colorscheme)
        if vim.g.colors_name or pcall(vim.cmd.colorscheme, colorscheme) then
          break
        end
      end
      Cache.reset()
      require("lazy.manage").install({ wait = true, lockfile = true, clear = false })
      -- remove any installed plugins from indexed, so cache will index again
      for _, p in pairs(Config.plugins) do
        if p._.installed then
          Cache.reset(p.dir)
        end
      end
      -- reload plugins
      Plugin.load()
      return true
    end
  end
end

-- Startup sequence
-- 1. load any start plugins and do init
function M.startup()
  Util.track({ start = "startup" })

  -- load filetype.lua first since plugins might depend on that
  M.source(vim.env.VIMRUNTIME .. "/filetype.lua")

  -- backup original rtp
  local rtp = vim.opt.rtp:get() --[[@as string[] ]]

  -- 1. run plugin init
  Util.track({ start = "init" })
  for _, plugin in pairs(Config.plugins) do
    if plugin.init then
      Util.track({ plugin = plugin.name, init = "init" })
      Util.try(function()
        plugin.init(plugin)
      end, "Failed to run `init` for **" .. plugin.name .. "**")
      Util.track()
    end
  end
  Util.track()

  -- 2. load start plugin
  Util.track({ start = "start" })
  for _, plugin in ipairs(M.get_start_plugins()) do
    -- plugin may be loaded by another plugin in the meantime
    if not plugin._.loaded then
      M.load(plugin, { start = "start" })
    end
  end
  Util.track()

  -- 3. load plugins from the original rtp, excluding after
  Util.track({ start = "rtp plugins" })
  for _, path in ipairs(rtp) do
    if not path:find("after/?$") then
      -- these paths don't will already have their ftdetect ran,
      -- by sourcing filetype.lua above, so skip them
      M.did_ftdetect[path] = path
      M.packadd(path)
    end
  end
  Util.track()

  -- 4. load after plugins
  Util.track({ start = "after" })
  for _, path in
    ipairs(vim.opt.rtp:get() --[[@as string[] ]])
  do
    if path:find("after/?$") then
      M.source_runtime(path, "plugin")
    end
  end
  Util.track()

  M.init_done = true

  Util.track()
end

function M.get_start_plugins()
  ---@type LazyPlugin[]
  local start = {}
  for _, plugin in pairs(Config.plugins) do
    if not plugin._.loaded and (plugin._.rtp_loaded or plugin.lazy == false) then
      start[#start + 1] = plugin
    end
  end
  table.sort(start, function(a, b)
    local ap = a.priority or DEFAULT_PRIORITY
    local bp = b.priority or DEFAULT_PRIORITY
    return ap > bp
  end)
  return start
end

---@class Loader
---@param plugins string|LazyPlugin|string[]|LazyPlugin[]
---@param reason {[string]:string}
---@param opts? {force:boolean} when force is true, we skip the cond check
function M.load(plugins, reason, opts)
  ---@diagnostic disable-next-line: cast-local-type
  plugins = (type(plugins) == "string" or plugins.name) and { plugins } or plugins
  ---@cast plugins (string|LazyPlugin)[]

  for _, plugin in pairs(plugins) do
    if type(plugin) == "string" then
      if Config.plugins[plugin] then
        plugin = Config.plugins[plugin]
      elseif Config.spec.disabled[plugin] then
        plugin = nil
      else
        Util.error("Plugin " .. plugin .. " not found")
        plugin = nil
      end
    end
    if plugin and not plugin._.loaded then
      M._load(plugin, reason, opts)
    end
  end
end

---@param plugin LazyPlugin
function M.deactivate(plugin)
  if not plugin._.loaded then
    return
  end

  local main = M.get_main(plugin)

  if main then
    Util.try(function()
      local mod = require(main)
      if mod.deactivate then
        mod.deactivate(plugin)
      end
    end, "Failed to deactivate plugin " .. plugin.name)
  end

  -- execute deactivate when needed
  if plugin.deactivate then
    Util.try(function()
      plugin.deactivate(plugin)
    end, "Failed to deactivate plugin " .. plugin.name)
  end

  -- disable handlers
  Handler.disable(plugin)

  -- clear plugin properties cache
  plugin._.cache = nil

  -- remove loaded lua modules
  Util.walkmods(plugin.dir .. "/lua", function(modname)
    package.loaded[modname] = nil
    package.preload[modname] = nil
  end)

  -- clear vim.g.loaded_ for plugins
  Util.ls(plugin.dir .. "/plugin", function(_, name, type)
    if type == "file" then
      vim.g["loaded_" .. name:gsub("%..*", "")] = nil
    end
  end)
  -- set as not loaded
  plugin._.loaded = nil
end

--- reload a plugin
---@param plugin LazyPlugin|string
function M.reload(plugin)
  if type(plugin) == "string" then
    plugin = Config.plugins[plugin]
  end

  if not plugin then
    error("Plugin not found")
  end

  local load = plugin._.loaded ~= nil
  M.deactivate(plugin)

  -- enable handlers
  Handler.enable(plugin)

  -- run init
  if plugin.init then
    Util.try(function()
      plugin.init(plugin)
    end, "Failed to run `init` for **" .. plugin.name .. "**")
  end

  -- if this is a start plugin, load it now
  if plugin.lazy == false then
    load = true
  end

  local events = plugin._.handlers and plugin._.handlers.event and plugin._.handlers.event or {}

  for _, event in pairs(events) do
    if event.id:find("VimEnter") or event.id:find("UIEnter") or event.id:find("VeryLazy") then
      load = true
      break
    end
  end

  -- reload any vimscript files for this plugin
  local scripts = vim.fn.getscriptinfo()
  local loaded_scripts = {}
  for _, s in ipairs(scripts) do
    ---@type string
    local path = s.name
    if
      path:sub(-4) == ".vim"
      and path:find(plugin.dir, 1, true) == 1
      and not path:find("/plugin/", 1, true)
      and not path:find("/ftplugin/", 1, true)
    then
      loaded_scripts[#loaded_scripts + 1] = path
    end
  end

  if load then
    M.load(plugin, { start = "reload" })
    for _, s in ipairs(loaded_scripts) do
      M.source(s)
    end
  end
end

---@param plugin LazyPlugin
---@param reason {[string]:string}
---@param opts? {force:boolean} when force is true, we skip the cond check
function M._load(plugin, reason, opts)
  if not plugin._.installed then
    return Util.error("Plugin " .. plugin.name .. " is not installed")
  end

  if plugin._.cond == false and not (opts and opts.force) then
    return
  end

  if not Handler.did_setup then
    Util.try(function()
      Handler.enable(plugin)
    end, "Failed to setup handlers for " .. plugin.name)
  end

  ---@diagnostic disable-next-line: assign-type-mismatch
  plugin._.loaded = {}
  for k, v in pairs(reason) do
    plugin._.loaded[k] = v
  end
  if #M.loading > 0 then
    plugin._.loaded.plugin = M.loading[#M.loading].name
  elseif reason.require then
    plugin._.loaded.source = Util.get_source()
  end

  table.insert(M.loading, plugin)

  Util.track({ plugin = plugin.name, start = reason.start })
  Handler.disable(plugin)

  if not plugin.virtual then
    M.add_to_rtp(plugin)
  end

  if plugin._.pkg and plugin._.pkg.source == "rockspec" then
    M.add_to_luapath(plugin)
  end

  if plugin.dependencies then
    Util.try(function()
      M.load(plugin.dependencies, {})
    end, "Failed to load deps for " .. plugin.name)
  end

  if not plugin.virtual then
    M.packadd(plugin.dir)
  end
  if plugin.config or plugin.opts then
    M.config(plugin)
  end

  plugin._.loaded.time = Util.track().time
  table.remove(M.loading)
  vim.schedule(function()
    vim.api.nvim_exec_autocmds("User", { pattern = "LazyLoad", modeline = false, data = plugin.name })
    vim.api.nvim_exec_autocmds("User", { pattern = "LazyRender", modeline = false })
  end)
end

--- runs plugin config
---@param plugin LazyPlugin
function M.config(plugin)
  local fn
  if type(plugin.config) == "function" then
    fn = function()
      local opts = Plugin.values(plugin, "opts", false)
      plugin.config(plugin, opts)
    end
  else
    local main = M.get_main(plugin)
    if main then
      fn = function()
        local opts = Plugin.values(plugin, "opts", false)
        require(main).setup(opts)
      end
    else
      return Util.error(
        "Lua module not found for config of " .. plugin.name .. ". Please use a `config()` function instead"
      )
    end
  end
  Util.try(fn, "Failed to run `config` for " .. plugin.name)
end

---@param plugin LazyPlugin
function M.get_main(plugin)
  if plugin.main then
    return plugin.main
  end
  if plugin.name ~= "mini.nvim" and plugin.name:match("^mini%..*$") then
    return plugin.name
  end
  local normname = Util.normname(plugin.name)
  ---@type string[]
  local mods = {}
  for _, mod in ipairs(Cache.find("*", { all = true, rtp = false, paths = { plugin.dir } })) do
    local modname = mod.modname
    mods[#mods + 1] = modname
    local modnorm = Util.normname(modname)
    -- if we found an exact match, then use that
    if modnorm == normname then
      mods = { modname }
      break
    end
  end

  return #mods == 1 and mods[1] or nil
end

---@param path string
function M.packadd(path)
  M.source_runtime(path, "plugin")
  M.ftdetect(path)
  if M.init_done then
    M.source_runtime(path, "after/plugin")
  end
end

---@param path string
function M.ftdetect(path)
  if not M.did_ftdetect[path] then
    M.did_ftdetect[path] = path
    vim.cmd("augroup filetypedetect")
    M.source_runtime(path, "ftdetect")
    vim.cmd("augroup END")
  end
end

---@param ... string
function M.source_runtime(...)
  local dir = table.concat({ ... }, "/")
  ---@type string[]
  local files = {}
  Util.walk(dir, function(path, name, t)
    local ext = name:sub(-3)
    name = name:sub(1, -5)
    if (t == "file" or t == "link") and (ext == "lua" or ext == "vim") and not M.disabled_rtp_plugins[name] then
      files[#files + 1] = path
    end
  end)
  -- plugin files are sourced alphabetically per directory
  table.sort(files)
  for _, path in ipairs(files) do
    M.source(path)
  end
end

-- This does the same as runtime.c:add_pack_dir_to_rtp
-- * find first after
-- * find lazy pack path
-- * insert right after lazy pack path or right before first after or at the end
-- * insert after dir right before first after or append to the end
---@param plugin LazyPlugin
function M.add_to_rtp(plugin)
  local rtp = vim.api.nvim_get_runtime_file("", true)
  local idx_dir, idx_after

  for i, path in ipairs(rtp) do
    if Util.is_win then
      path = Util.norm(path)
    end
    if path == Config.me then
      idx_dir = i + 1
    elseif not idx_after and path:sub(-6, -1) == "/after" then
      idx_after = i + 1 -- +1 to offset the insert of the plugin dir
      idx_dir = idx_dir or i
      break
    end
  end

  table.insert(rtp, idx_dir or (#rtp + 1), plugin.dir)

  local after = plugin.dir .. "/after"
  if vim.uv.fs_stat(after) then
    table.insert(rtp, idx_after or (#rtp + 1), after)
  end

  ---@type vim.Option
  vim.opt.rtp = rtp
end

---@param plugin LazyPlugin
function M.add_to_luapath(plugin)
  local root = Config.options.rocks.root .. "/" .. plugin.name
  local path = root .. "/share/lua/5.1"
  local cpath = root .. "/lib/lua/5.1"
  local cpath2 = root .. "/lib64/lua/5.1"

  package.path = package.path .. ";" .. path .. "/?.lua;" .. path .. "/?/init.lua;"
  package.cpath = package.cpath .. ";" .. cpath .. "/?." .. (jit.os:find("Windows") and "dll" or "so") .. ";"
  package.cpath = package.cpath .. ";" .. cpath2 .. "/?." .. (jit.os:find("Windows") and "dll" or "so") .. ";"
end

function M.source(path)
  Util.track({ runtime = path })
  Util.try(function()
    vim.cmd("source " .. path)
  end, "Failed to source `" .. path .. "`")
  Util.track()
end

function M.colorscheme(name)
  if vim.tbl_contains(vim.fn.getcompletion("", "color"), name) then
    return
  end
  for _, plugin in pairs(Config.plugins) do
    if not plugin._.loaded then
      for _, ext in ipairs({ "lua", "vim" }) do
        local path = plugin.dir .. "/colors/" .. name .. "." .. ext
        if vim.uv.fs_stat(path) then
          return M.load(plugin, { colorscheme = name })
        end
      end
    end
  end
end

function M.auto_load(modname, modpath)
  local plugin = Plugin.find(modpath, { fast = not M.did_handlers })
  if plugin then
    plugin._.rtp_loaded = true
    -- don't load if:
    -- * handlers haven't been setup yet
    -- * we're loading specs
    -- * the plugin is already loaded
    if M.did_handlers and not (Plugin.loading or plugin._.loaded) then
      if plugin.module == false then
        error("Plugin " .. plugin.name .. " is not loaded and is configured with module=false")
      end
      M.load(plugin, { require = modname })
      if plugin._.cond == false then
        error("You're trying to load `" .. plugin.name .. "` for which `cond==false`")
      end
    end
  end
end

---@param modname string
function M.loader(modname)
  local paths, cached = Util.get_unloaded_rtp(modname, { cache = true })
  local ret = Cache.find(modname, { rtp = false, paths = paths })[1]

  if not ret and cached then
    paths = Util.get_unloaded_rtp(modname)
    ret = Cache.find(modname, { rtp = false, paths = paths })[1]
  end

  if ret then
    -- explicitly set to nil to prevent loading errors
    package.loaded[modname] = nil
    M.auto_load(modname, ret.modpath)
    local mod = package.loaded[modname]
    if type(mod) == "table" then
      return function()
        return mod
      end
    end
    -- selene: allow(incorrect_standard_library_use)
    return loadfile(ret.modpath, nil, nil, ret.stat)
  end
end

return M
```

## File: `lua/lazy/core/meta.lua`
```
local Config = require("lazy.core.config")
local Pkg = require("lazy.pkg")
local Util = require("lazy.core.util")

--- This class is used to manage the plugins.
--- A plugin is a collection of fragments that are related to each other.
---@class LazyMeta
---@field plugins table<string, LazyPlugin>
---@field str_to_meta table<string, LazyPlugin>
---@field frag_to_meta table<number, LazyPlugin>
---@field dirty table<string, boolean>
---@field spec LazySpecLoader
---@field fragments LazyFragments
---@field pkgs table<string, number>
local M = {}

---@param spec LazySpecLoader
---@return LazyMeta
function M.new(spec)
  local self = setmetatable({}, { __index = M })
  self.spec = spec
  self.fragments = require("lazy.core.fragments").new(spec)
  self.plugins = {}
  self.frag_to_meta = {}
  self.str_to_meta = {}
  self.dirty = {}
  self.pkgs = {}
  return self
end

-- import package specs
function M:load_pkgs()
  if not Config.options.pkg.enabled then
    return
  end
  for _, pkg in ipairs(Pkg.get()) do
    local last_id = self.fragments._fid
    local meta, fragment = self:add(pkg.spec)
    if meta and fragment then
      meta._.pkg = pkg
      -- tag all top-level package fragments that were added as optional
      for _, fid in ipairs(meta._.frags) do
        if fid > last_id then
          local frag = self.fragments:get(fid)
          frag.spec.optional = true
        end
      end
      -- keep track of the top-level package fragment
      self.pkgs[pkg.dir] = fragment.id
    end
  end
end

--- Remove a plugin and all its fragments.
---@param name string
function M:del(name)
  local meta = self.plugins[name]
  if not meta then
    return
  end
  for _, fid in ipairs(meta._.frags or {}) do
    self.fragments:del(fid)
  end
  self.plugins[name] = nil
end

--- Add a fragment to a plugin.
--- This will create a new plugin if it does not exist.
--- It also keeps track of renames.
---@param plugin LazyPluginSpec
function M:add(plugin)
  local fragment = self.fragments:add(plugin)
  if not fragment then
    return
  end

  local meta = self.plugins[fragment.name]
    or fragment.url and self.str_to_meta[fragment.url]
    or fragment.dir and self.str_to_meta[fragment.dir]

  if not meta then
    meta = { name = fragment.name, _ = { frags = {} } }
    local url, dir = fragment.url, fragment.dir
    -- add to index
    if url then
      self.str_to_meta[url] = meta
    end
    if dir then
      self.str_to_meta[dir] = meta
    end
  end

  table.insert(meta._.frags, fragment.id)

  if meta._ and meta._.rtp_loaded and meta.dir then
    local old_dir = meta.dir
    self:_rebuild(meta.name)
    local new_dir = meta.dir
    if old_dir ~= new_dir then
      local msg = "Plugin `" .. meta.name .. "` changed `dir`:\n- from: `" .. old_dir .. "`\n- to: `" .. new_dir .. "`"
      msg = msg .. "\n\nThis plugin was already partially loaded, so things may break.\nPlease fix your config."
      self.spec:error(msg)
    end
  end

  if plugin.name then
    -- handle renames
    if meta.name ~= plugin.name then
      self.plugins[meta.name] = nil
      meta.name = plugin.name
    end
  end

  self.plugins[meta.name] = meta
  self.frag_to_meta[fragment.id] = meta
  self.dirty[meta.name] = true
  return meta, fragment
end

--- Rebuild all plugins based on dirty fragments,
--- or dirty plugins. Will remove plugins that no longer have fragments.
function M:rebuild()
  local frag_count = vim.tbl_count(self.fragments.dirty)
  local plugin_count = vim.tbl_count(self.dirty)
  if frag_count == 0 and plugin_count == 0 then
    return
  end
  if Config.options.debug then
    Util.track("rebuild plugins frags=" .. frag_count .. " plugins=" .. plugin_count)
  end
  for fid in pairs(self.fragments.dirty) do
    local meta = self.frag_to_meta[fid]
    if meta then
      if self.fragments:get(fid) then
        -- fragment still exists, so mark plugin as dirty
        self.dirty[meta.name] = true
      else
        -- fragment was deleted, so remove it from plugin
        self.frag_to_meta[fid] = nil
        ---@param f number
        meta._.frags = Util.filter(function(f)
          return f ~= fid
        end, meta._.frags)
        -- if no fragments left, delete plugin
        if #meta._.frags == 0 then
          self:del(meta.name)
        else
          self.dirty[meta.name] = true
        end
      end
    end
  end
  self.fragments.dirty = {}
  for n, _ in pairs(self.dirty) do
    self:_rebuild(n)
  end
  if Config.options.debug then
    Util.track()
  end
end

--- Rebuild a single plugin.
--- This will resolve the plugin based on its fragments using metatables.
--- This also resolves dependencies, dep, optional, dir, dev, and url.
---@param name string
function M:_rebuild(name)
  if not self.dirty[name] then
    return
  end
  self.dirty[name] = nil
  local plugin = self.plugins[name]
  if not plugin or #plugin._.frags == 0 then
    self.plugins[name] = nil
    return
  end
  setmetatable(plugin, nil)
  plugin.dependencies = {}

  local super = nil
  plugin.url = nil
  plugin._.dep = true
  plugin._.top = true
  plugin.optional = true

  assert(#plugin._.frags > 0, "no fragments found for plugin " .. name)

  ---@type table<number, boolean>
  local added = {}
  for _, fid in ipairs(plugin._.frags) do
    if not added[fid] then
      added[fid] = true
      local fragment = self.fragments:get(fid)
      assert(fragment, "fragment " .. fid .. " not found, for plugin " .. name)
      ---@diagnostic disable-next-line: no-unknown
      super = setmetatable(fragment.spec, super and { __index = super } or nil)
      plugin._.dep = plugin._.dep and fragment.dep
      plugin.optional = plugin.optional and (rawget(fragment.spec, "optional") == true)
      plugin.url = fragment.url or plugin.url
      plugin._.top = plugin._.top and fragment.pid == nil

      -- dependencies
      for _, dep in ipairs(fragment.deps or {}) do
        local dep_meta = self.frag_to_meta[dep]
        if dep_meta then
          table.insert(plugin.dependencies, dep_meta.name)
        end
      end
    end
  end

  super = super or {}

  -- dir / dev
  plugin.dev = super.dev
  plugin.dir = super.dir
  if plugin.dir then
    plugin.dir = Util.norm(plugin.dir)
  elseif super.virtual then
    plugin.dir = Util.norm("/dev/null/" .. plugin.name)
  else
    if plugin.dev == nil and plugin.url then
      for _, pattern in ipairs(Config.options.dev.patterns) do
        if plugin.url:find(pattern, 1, true) then
          plugin.dev = true
          break
        end
      end
    end
    if plugin.dev == true then
      local dev_dir = type(Config.options.dev.path) == "string" and Config.options.dev.path .. "/" .. plugin.name
        or Util.norm(Config.options.dev.path(plugin))
      if not Config.options.dev.fallback or vim.fn.isdirectory(dev_dir) == 1 then
        plugin.dir = dev_dir
      else
        plugin.dev = false
      end
    end
    plugin.dir = plugin.dir or Config.options.root .. "/" .. plugin.name
  end

  -- dependencies
  if #plugin.dependencies == 0 and not super.dependencies then
    plugin.dependencies = nil
  end

  -- optional
  if not plugin.optional and not super.optional then
    plugin.optional = nil
  end

  setmetatable(plugin, { __index = super })

  return plugin
end

--- Disable a plugin.
---@param plugin LazyPlugin
function M:disable(plugin)
  plugin._.kind = "disabled"
  self:del(plugin.name)
  self.spec.disabled[plugin.name] = plugin
end

--- Check if a plugin should be disabled, but ignore uninstalling it.
function M:fix_cond()
  for _, plugin in pairs(self.plugins) do
    local cond = plugin.cond
    if cond == nil then
      cond = Config.options.defaults.cond
    end
    if cond == false or (type(cond) == "function" and not cond(plugin)) then
      plugin._.cond = false
      local stack = { plugin }
      while #stack > 0 do
        local p = table.remove(stack) --[[@as LazyPlugin]]
        if not self.spec.ignore_installed[p.name] then
          for _, dep in ipairs(p.dependencies or {}) do
            table.insert(stack, self.plugins[dep])
          end
          self.spec.ignore_installed[p.name] = true
        end
      end
      plugin.enabled = false
    end
  end
end

--- Removes plugins for which all its fragments are optional.
function M:fix_optional()
  if self.spec.optional then
    return 0
  end
  local changes = 0
  for _, plugin in pairs(self.plugins) do
    if plugin.optional then
      changes = changes + 1
      self:del(plugin.name)
    end
  end
  self:rebuild()
  return changes
end

--- Removes plugins that are disabled.
function M:fix_disabled()
  local changes = 0
  local function check(top)
    for _, plugin in pairs(self.plugins) do
      if (plugin._.top or false) == top then
        if plugin.enabled == false or (type(plugin.enabled) == "function" and not plugin.enabled()) then
          changes = changes + 1
          if plugin.optional then
            self:del(plugin.name)
          else
            self:disable(plugin)
          end
          self:rebuild()
        end
      end
    end
  end
  -- disable top-level plugins first, since they may have non-top-level frags
  -- that disable other plugins
  check(true)
  -- then disable non-top-level plugins
  check(false)
  return changes
end

--- Removes package fragments for plugins that no longer use the same directory.
function M:fix_pkgs()
  for dir, fid in pairs(self.pkgs) do
    local plugin = self.frag_to_meta[fid]
    plugin = plugin and self.plugins[plugin.name]
    if plugin then
      -- check if plugin is still in the same directory
      if plugin.dir ~= dir then
        self.fragments:del(fid)
      end
    end
  end
  self:rebuild()
end

--- Resolve all plugins, based on cond, enabled and optional.
function M:resolve()
  Util.track("resolve plugins")
  self:rebuild()

  self:fix_pkgs()

  self:fix_cond()

  -- selene: allow(empty_loop)
  while self:fix_disabled() + self:fix_optional() > 0 do
  end
  Util.track()
end

return M
```

## File: `lua/lazy/core/plugin.lua`
```
local Config = require("lazy.core.config")
local Meta = require("lazy.core.meta")
local Pkg = require("lazy.pkg")
local Util = require("lazy.core.util")

---@class LazyCorePlugin
local M = {}
M.loading = false

---@class LazySpecLoader
---@field meta LazyMeta
---@field plugins table<string, LazyPlugin>
---@field disabled table<string, LazyPlugin>
---@field ignore_installed table<string, true>
---@field modules string[]
---@field notifs {msg:string, level:number, file?:string}[]
---@field importing? string
---@field optional? boolean
local Spec = {}
M.Spec = Spec
M.LOCAL_SPEC = ".lazy.lua"

---@param spec? LazySpec
---@param opts? {optional?:boolean, pkg?:boolean}
function Spec.new(spec, opts)
  local self = setmetatable({}, Spec)
  self.meta = Meta.new(self)
  self.disabled = {}
  self.modules = {}
  self.notifs = {}
  self.ignore_installed = {}
  self.optional = opts and opts.optional
  if not (opts and opts.pkg == false) then
    self.meta:load_pkgs()
  end
  if spec then
    self:parse(spec)
  end
  return self
end

function Spec:__index(key)
  if Spec[key] then
    return Spec[key]
  end
  if key == "plugins" then
    self.meta:rebuild()
    return self.meta.plugins
  end
end

function Spec:parse(spec)
  self:normalize(spec)
  self.meta:resolve()
end

-- PERF: optimized code to get package name without using lua patterns
---@return string
function Spec.get_name(pkg)
  local name = pkg:sub(-4) == ".git" and pkg:sub(1, -5) or pkg
  name = name:sub(-1) == "/" and name:sub(1, -2) or name
  local slash = name:reverse():find("/", 1, true) --[[@as number?]]
  return slash and name:sub(#name - slash + 2) or pkg:gsub("%W+", "_")
end

function Spec:error(msg)
  self:log(msg, vim.log.levels.ERROR)
end

function Spec:warn(msg)
  self:log(msg, vim.log.levels.WARN)
end

---@param msg string
---@param level number
function Spec:log(msg, level)
  self.notifs[#self.notifs + 1] = { msg = msg, level = level, file = self.importing }
end

function Spec:report(level)
  level = level or vim.log.levels.ERROR
  local count = 0
  for _, notif in ipairs(self.notifs) do
    if notif.level >= level then
      Util.notify(notif.msg, { level = notif.level })
      count = count + 1
    end
  end
  return count
end

---@param spec LazySpec|LazySpecImport
function Spec:normalize(spec)
  if type(spec) == "string" then
    self.meta:add({ spec })
  elseif #spec > 1 or Util.is_list(spec) then
    ---@cast spec LazySpec[]
    for _, s in ipairs(spec) do
      self:normalize(s)
    end
  elseif spec[1] or spec.dir or spec.url then
    ---@cast spec LazyPluginSpec
    self.meta:add(spec)
    ---@diagnostic disable-next-line: cast-type-mismatch
    ---@cast spec LazySpecImport
    if spec and spec.import then
      self:import(spec)
    end
  elseif spec.import then
    ---@cast spec LazySpecImport
    self:import(spec)
  else
    self:error("Invalid plugin spec " .. vim.inspect(spec))
  end
end

---@param spec LazySpecImport
function Spec:import(spec)
  if spec.import == "lazy" then
    return self:error("You can't name your plugins module `lazy`.")
  end
  if type(spec.import) == "function" then
    if not spec.name then
      return self:error("Invalid import spec. Missing name: " .. vim.inspect(spec))
    end
  elseif type(spec.import) ~= "string" then
    return self:error("Invalid import spec. `import` should be a string: " .. vim.inspect(spec))
  end

  local import_name = spec.name or spec.import
  ---@cast import_name string

  if vim.tbl_contains(self.modules, import_name) then
    return
  end
  if spec.cond == false or (type(spec.cond) == "function" and not spec.cond()) then
    return
  end
  if spec.enabled == false or (type(spec.enabled) == "function" and not spec.enabled()) then
    return
  end

  self.modules[#self.modules + 1] = import_name

  local import = spec.import

  local imported = 0

  ---@type {modname: string, load: fun():(LazyPluginSpec?, string?)}[]
  local modspecs = {}

  if type(import) == "string" then
    Util.lsmod(import, function(modname, modpath)
      modspecs[#modspecs + 1] = {
        modname = modname,
        load = function()
          local mod, err = loadfile(modpath)
          if mod then
            local ret, foo = mod()
            if foo then
              return nil, "Spec module returned more than one value. Expected a single value."
            end
            return ret
          else
            return nil, err
          end
        end,
      }
    end)
    table.sort(modspecs, function(a, b)
      return a.modname < b.modname
    end)
  else
    modspecs = { { modname = import_name, load = spec.import } }
  end

  for _, modspec in ipairs(modspecs) do
    imported = imported + 1
    local modname = modspec.modname
    Util.track({ import = modname })
    self.importing = modname
    -- unload the module so we get a clean slate
    ---@diagnostic disable-next-line: no-unknown
    package.loaded[modname] = nil
    Util.try(function()
      local mod, err = modspec.load()
      if err then
        self:error("Failed to load `" .. modname .. "`:\n" .. err)
      elseif type(mod) ~= "table" then
        return self:error(
          "Invalid spec module: `"
            .. modname
            .. "`\nExpected a `table` of specs, but a `"
            .. type(mod)
            .. "` was returned instead"
        )
      else
        self:normalize(mod)
      end
    end, {
      msg = "Failed to load `" .. modname .. "`",
      on_error = function(msg)
        self:error(msg)
      end,
    })
    self.importing = nil
    Util.track()
  end
  if imported == 0 then
    self:error("No specs found for module " .. vim.inspect(spec.import))
  end
end

function M.update_state()
  ---@type string[]
  local cloning = {}

  ---@type table<string,FileType>
  local installed = {}
  Util.ls(Config.options.root, function(_, name, type)
    if type == "directory" and name ~= "readme" then
      installed[name] = type
    elseif type == "file" and name:sub(-8) == ".cloning" then
      name = name:sub(1, -9)
      cloning[#cloning + 1] = name
    end
  end)

  for _, failed in ipairs(cloning) do
    installed[failed] = nil
  end

  for _, plugin in pairs(Config.plugins) do
    plugin._ = plugin._ or {}
    if plugin.lazy == nil then
      local lazy = plugin._.dep
        or Config.options.defaults.lazy
        or plugin.event
        or plugin.keys
        or plugin.ft
        or plugin.cmd
      plugin.lazy = lazy and true or false
    end
    if plugin.virtual then
      plugin._.is_local = true
      plugin._.installed = true -- local plugins are managed by the user
    elseif plugin.dir:find(Config.options.root .. "/", 1, true) == 1 then
      plugin._.installed = installed[plugin.name] ~= nil
      installed[plugin.name] = nil
    else
      plugin._.is_local = true
      plugin._.installed = vim.fn.isdirectory(plugin.dir) == 1
    end
  end

  for name in pairs(Config.spec.ignore_installed) do
    installed[name] = nil
  end

  M.update_rocks_state()

  Config.to_clean = {}
  for pack, dir_type in pairs(installed) do
    table.insert(Config.to_clean, {
      name = pack,
      dir = Config.options.root .. "/" .. pack,
      _ = {
        kind = "clean",
        installed = true,
        is_symlink = dir_type == "link",
        is_local = dir_type == "link",
      },
    })
  end
end

function M.update_rocks_state()
  local root = Config.options.rocks.root
  ---@type table<string,string>
  local installed = {}
  Util.ls(root, function(_, name, type)
    if type == "directory" then
      installed[name] = name
    end
  end)

  for _, plugin in pairs(Config.plugins) do
    if plugin.build == "rockspec" or plugin.name == "hererocks" then
      plugin._.build = not installed[plugin.name]
    end
  end
end

---@return LazySpecImport?
function M.find_local_spec()
  if not Config.options.local_spec then
    return
  end
  local path = vim.uv.cwd()
  while path and path ~= "" do
    local file = path .. "/" .. M.LOCAL_SPEC
    if vim.fn.filereadable(file) == 1 then
      return {
        name = vim.fn.fnamemodify(file, ":~:."),
        import = function()
          local data = vim.secure.read(file)
          if data then
            return loadstring(data, M.LOCAL_SPEC)()
          end
          return {}
        end,
      }
    end
    local p = vim.fn.fnamemodify(path, ":h")
    if p == path then
      break
    end
    path = p
  end
end

function M.load()
  M.loading = true
  -- load specs
  Util.track("spec")
  Config.spec = Spec.new()

  local specs = {
    ---@diagnostic disable-next-line: param-type-mismatch
    vim.deepcopy(Config.options.spec),
  }
  specs[#specs + 1] = M.find_local_spec()
  specs[#specs + 1] = { "folke/lazy.nvim" }

  Config.spec:parse(specs)

  -- override some lazy props
  local lazy = Config.spec.plugins["lazy.nvim"]
  if lazy then
    lazy.lazy = true
    lazy.dir = Config.me
    lazy.config = function()
      error("lazy config should not be called")
    end
    lazy._.loaded = {}
  end

  -- add hererocks when enabled and needed
  for _, plugin in pairs(Config.spec.plugins) do
    if plugin.build == "rockspec" then
      if Config.hererocks() then
        Config.spec.meta:add({
          "luarocks/hererocks",
          build = "rockspec",
          lazy = true,
        })
      end
      break
    end
  end

  local existing = Config.plugins
  Config.plugins = Config.spec.plugins
  -- copy state. This wont do anything during startup
  for name, plugin in pairs(existing) do
    if Config.plugins[name] then
      local new_state = Config.plugins[name]._
      Config.plugins[name]._ = plugin._
      Config.plugins[name]._.dep = new_state.dep
      Config.plugins[name]._.frags = new_state.frags
      Config.plugins[name]._.pkg = new_state.pkg
    end
  end
  Util.track()

  Util.track("state")
  M.update_state()
  Util.track()

  if Config.options.pkg.enabled and Pkg.dirty then
    Pkg.update()
    return M.load()
  end

  M.loading = false
  vim.api.nvim_exec_autocmds("User", { pattern = "LazyPlugins", modeline = false })
end

-- Finds the plugin that has this path
---@param path string
---@param opts? {fast?:boolean}
function M.find(path, opts)
  if not Config.spec then
    return
  end
  opts = opts or {}
  local lua = path:find("/lua/", 1, true)
  if lua then
    local name = path:sub(1, lua - 1)
    local slash = name:reverse():find("/", 1, true)
    if slash then
      name = name:sub(#name - slash + 2)
      if name then
        if opts.fast then
          return Config.spec.meta.plugins[name]
        end
        return Config.spec.plugins[name]
      end
    end
  end
end

---@param plugin LazyPlugin
function M.has_errors(plugin)
  for _, task in ipairs(plugin._.tasks or {}) do
    if task:has_errors() then
      return true
    end
  end
  return false
end

-- Merges super values or runs the values function to override values or return new ones.
-- Values are cached for performance.
-- Used for opts, cmd, event, ft and keys
---@param plugin LazyPlugin
---@param prop string
---@param is_list? boolean
function M.values(plugin, prop, is_list)
  if not plugin[prop] then
    return {}
  end
  plugin._.cache = plugin._.cache or {}
  local key = prop .. (is_list and "_list" or "")
  if plugin._.cache[key] == nil then
    plugin._.cache[key] = M._values(plugin, plugin, prop, is_list)
  end
  return plugin._.cache[key]
end

-- Merges super values or runs the values function to override values or return new ones
-- Used for opts, cmd, event, ft and keys
---@param root LazyPlugin
---@param plugin LazyPlugin
---@param prop string
---@param is_list? boolean
function M._values(root, plugin, prop, is_list)
  if not plugin[prop] then
    return {}
  end
  local super = getmetatable(plugin)
  ---@type table
  local ret = super and M._values(root, super.__index, prop, is_list) or {}
  local values = rawget(plugin, prop)

  if not values then
    return ret
  elseif type(values) == "function" then
    ret = values(root, ret) or ret
    return type(ret) == "table" and ret or { ret }
  end

  values = type(values) == "table" and values or { values }
  if is_list then
    return Util.extend(ret, values)
  else
    ---@type {path:string[], list:any[]}[]
    local lists = {}
    ---@diagnostic disable-next-line: no-unknown
    for _, key in ipairs(plugin[prop .. "_extend"] or {}) do
      local path = vim.split(key, ".", { plain = true })
      local r = Util.key_get(ret, path)
      local v = Util.key_get(values, path)
      if type(r) == "table" and type(v) == "table" then
        lists[key] = { path = path, list = {} }
        vim.list_extend(lists[key].list, r)
        vim.list_extend(lists[key].list, v)
      end
    end
    local t = Util.merge(ret, values)
    for _, list in pairs(lists) do
      Util.key_set(t, list.path, list.list)
    end
    return t
  end
end

return M
```

## File: `lua/lazy/core/util.lua`
```
---@class LazyUtilCore
local M = {}

---@alias LazyProfile {data: string|{[string]:string}, time: number, [number]:LazyProfile}

---@type LazyProfile[]
M._profiles = { { name = "lazy" } }
M.is_win = jit.os:find("Windows")

---@param data (string|{[string]:string})?
---@param time number?
function M.track(data, time)
  if data then
    local entry = {
      data = data,
      time = time or vim.uv.hrtime(),
    }
    table.insert(M._profiles[#M._profiles], entry)

    if not time then
      table.insert(M._profiles, entry)
    end
    return entry
  else
    ---@type LazyProfile
    local entry = table.remove(M._profiles)
    entry.time = vim.uv.hrtime() - entry.time
    return entry
  end
end

function M.exiting()
  return vim.v.exiting ~= vim.NIL
end

---@generic T
---@param list T[]
---@param fn fun(v: T):boolean?
---@return T[]
function M.filter(fn, list)
  local ret = {}
  for _, v in ipairs(list) do
    if fn(v) then
      table.insert(ret, v)
    end
  end
  return ret
end

---@generic F: fun()
---@param data (string|{[string]:string})?
---@param fn F
---@return F
function M.trackfn(data, fn)
  return function(...)
    M.track(data)
    local ok, ret = pcall(fn, ...)
    M.track()
    if not ok then
      error(ret)
    end
    return ret
  end
end

---@param name string
---@return string
function M.normname(name)
  local ret = name:lower():gsub("^n?vim%-", ""):gsub("%.n?vim$", ""):gsub("[%.%-]lua", ""):gsub("[^a-z]+", "")
  return ret
end

---@return string
function M.norm(path)
  if path:sub(1, 1) == "~" then
    local home = vim.uv.os_homedir()
    if home:sub(-1) == "\\" or home:sub(-1) == "/" then
      home = home:sub(1, -2)
    end
    path = home .. path:sub(2)
  end
  path = path:gsub("\\", "/"):gsub("/+", "/")
  return path:sub(-1) == "/" and path:sub(1, -2) or path
end

---@param opts? {level?: number}
function M.pretty_trace(opts)
  opts = opts or {}
  local Config = require("lazy.core.config")
  local trace = {}
  local level = opts.level or 2
  while true do
    local info = debug.getinfo(level, "Sln")
    if not info then
      break
    end
    if info.what ~= "C" and (Config.options.debug or not info.source:find("lazy.nvim")) then
      local source = info.source:sub(2)
      if source:find(Config.options.root, 1, true) == 1 then
        source = source:sub(#Config.options.root + 1)
      end
      source = vim.fn.fnamemodify(source, ":p:~:.") --[[@as string]]
      local line = "  - " .. source .. ":" .. info.currentline
      if info.name then
        line = line .. " _in_ **" .. info.name .. "**"
      end
      table.insert(trace, line)
    end
    level = level + 1
  end
  return #trace > 0 and ("\n\n# stacktrace:\n" .. table.concat(trace, "\n")) or ""
end

---@generic R
---@param fn fun():R?
---@param opts? string|{msg:string, on_error:fun(msg)}
---@return R
function M.try(fn, opts)
  opts = type(opts) == "string" and { msg = opts } or opts or {}
  local msg = opts.msg
  -- error handler
  local error_handler = function(err)
    msg = (msg and (msg .. "\n\n") or "") .. err .. M.pretty_trace()
    if opts.on_error then
      opts.on_error(msg)
    else
      vim.schedule(function()
        M.error(msg)
      end)
    end
    return err
  end

  ---@type boolean, any
  local ok, result = xpcall(fn, error_handler)
  return ok and result or nil
end

function M.get_source()
  local f = 2
  while true do
    local info = debug.getinfo(f, "S")
    if not info then
      break
    end
    if info.what ~= "C" and not info.source:find("lazy.nvim", 1, true) and info.source ~= "@vim/loader.lua" then
      return info.source:sub(2)
    end
    f = f + 1
  end
end

-- Fast implementation to check if a table is a list
---@param t table
function M.is_list(t)
  local i = 0
  ---@diagnostic disable-next-line: no-unknown
  for _ in pairs(t) do
    i = i + 1
    if t[i] == nil then
      return false
    end
  end
  return true
end

function M.very_lazy()
  local function _load()
    vim.schedule(function()
      if vim.v.exiting ~= vim.NIL then
        return
      end
      vim.g.did_very_lazy = true
      M.track({ event = "VeryLazy" })
      vim.api.nvim_exec_autocmds("User", { pattern = "VeryLazy", modeline = false })
      M.track()
    end)
  end

  vim.api.nvim_create_autocmd("User", {
    pattern = "LazyDone",
    once = true,
    callback = function()
      if vim.v.vim_did_enter == 1 then
        _load()
      else
        vim.api.nvim_create_autocmd("UIEnter", {
          once = true,
          callback = function()
            _load()
          end,
        })
      end
    end,
  })
end

---@alias FileType "file"|"directory"|"link"
---@param path string
---@param fn fun(path: string, name:string, type:FileType):boolean?
function M.ls(path, fn)
  local handle = vim.uv.fs_scandir(path)
  while handle do
    local name, t = vim.uv.fs_scandir_next(handle)
    if not name then
      break
    end

    local fname = path .. "/" .. name

    -- HACK: type is not always returned due to a bug in luv,
    -- so fecth it with fs_stat instead when needed.
    -- see https://github.com/folke/lazy.nvim/issues/306
    if fn(fname, name, t or vim.uv.fs_stat(fname).type) == false then
      break
    end
  end
end

---@param path string
---@param fn fun(path: string, name:string, type:FileType)
function M.walk(path, fn)
  M.ls(path, function(child, name, type)
    if type == "directory" then
      M.walk(child, fn)
    end
    fn(child, name, type)
  end)
end

---@param root string
---@param fn fun(modname:string, modpath:string)
---@param modname? string
function M.walkmods(root, fn, modname)
  modname = modname and (modname:gsub("%.$", "") .. ".") or ""
  M.ls(root, function(path, name, type)
    if name == "init.lua" then
      fn(modname:gsub("%.$", ""), path)
    elseif (type == "file" or type == "link") and name:sub(-4) == ".lua" then
      fn(modname .. name:sub(1, -5), path)
    elseif type == "directory" then
      M.walkmods(path, fn, modname .. name .. ".")
    end
  end)
end

---@param modname string
---@return string
function M.topmod(modname)
  return modname:match("^[^./]+") or modname
end

---@type table<string, string[]>
M.unloaded_cache = {}

---@param modname string
---@param opts? {cache?:boolean}
function M.get_unloaded_rtp(modname, opts)
  opts = opts or {}

  local topmod = M.topmod(modname)
  if opts.cache and M.unloaded_cache[topmod] then
    return M.unloaded_cache[topmod], true
  end

  local norm = M.normname(topmod)

  ---@type string[]
  local rtp = {}
  local Config = require("lazy.core.config")
  if Config.spec then
    for _, plugin in pairs(Config.spec.plugins) do
      if not (plugin._.loaded or plugin.module == false or plugin.virtual) then
        if norm == M.normname(plugin.name) then
          table.insert(rtp, 1, plugin.dir)
        else
          table.insert(rtp, plugin.dir)
        end
      end
    end
  end
  M.unloaded_cache[topmod] = rtp
  return rtp, false
end

function M.find_root(modname)
  local paths, cached = M.get_unloaded_rtp(modname, { cache = true })

  local ret = require("lazy.core.cache").find(modname, {
    rtp = true,
    paths = paths,
    patterns = { ".lua", "" },
  })[1]

  if not ret and cached then
    paths = M.get_unloaded_rtp(modname)
    ret = require("lazy.core.cache").find(modname, {
      rtp = false,
      paths = paths,
      patterns = { ".lua", "" },
    })[1]
  end
  if ret then
    return ret.modpath:gsub("%.lua$", ""), ret.modpath
  end
end

---@param modname string
---@param fn fun(modname:string, modpath:string)
function M.lsmod(modname, fn)
  local root, match = M.find_root(modname)
  if not root then
    return
  end

  if match:sub(-4) == ".lua" then
    fn(modname, match)
    if not vim.uv.fs_stat(root) then
      return
    end
  end

  M.ls(root, function(path, name, type)
    if name == "init.lua" then
      fn(modname, path)
    elseif (type == "file" or type == "link") and name:sub(-4) == ".lua" then
      fn(modname .. "." .. name:sub(1, -5), path)
    elseif type == "directory" and vim.uv.fs_stat(path .. "/init.lua") then
      fn(modname .. "." .. name, path .. "/init.lua")
    end
  end)
end

---@generic T
---@param list T[]
---@param add T[]
---@return T[]
function M.extend(list, add)
  local idx = {}
  for _, v in ipairs(list) do
    idx[v] = v
  end
  for _, a in ipairs(add) do
    if not idx[a] then
      table.insert(list, a)
    end
  end
  return list
end

---@alias LazyNotifyOpts {lang?:string, title?:string, level?:number, once?:boolean, stacktrace?:boolean, stacklevel?:number}

---@param msg string|string[]
---@param opts? LazyNotifyOpts
function M.notify(msg, opts)
  if vim.in_fast_event() then
    return vim.schedule(function()
      M.notify(msg, opts)
    end)
  end

  opts = opts or {}
  if type(msg) == "table" then
    msg = table.concat(
      vim.tbl_filter(function(line)
        return line or false
      end, msg),
      "\n"
    )
  end
  if opts.stacktrace then
    msg = msg .. M.pretty_trace({ level = opts.stacklevel or 2 })
  end
  local lang = opts.lang or "markdown"
  local n = opts.once and vim.notify_once or vim.notify
  n(msg, opts.level or vim.log.levels.INFO, {
    ft = lang,
    on_open = function(win)
      local ok = pcall(function()
        vim.treesitter.language.add("markdown")
      end)
      if not ok then
        pcall(require, "nvim-treesitter")
      end
      vim.wo[win].conceallevel = 3
      vim.wo[win].concealcursor = ""
      vim.wo[win].spell = false
      local buf = vim.api.nvim_win_get_buf(win)
      if not pcall(vim.treesitter.start, buf, lang) then
        vim.bo[buf].filetype = lang
        vim.bo[buf].syntax = lang
      end
    end,
    title = opts.title or "lazy.nvim",
  })
end

---@param msg string|string[]
---@param opts? LazyNotifyOpts
function M.error(msg, opts)
  opts = opts or {}
  opts.level = vim.log.levels.ERROR
  M.notify(msg, opts)
end

---@param msg string|string[]
---@param opts? LazyNotifyOpts
function M.info(msg, opts)
  opts = opts or {}
  opts.level = vim.log.levels.INFO
  M.notify(msg, opts)
end

---@param msg string|string[]
---@param opts? LazyNotifyOpts
function M.warn(msg, opts)
  opts = opts or {}
  opts.level = vim.log.levels.WARN
  M.notify(msg, opts)
end

---@param msg string|table
---@param opts? LazyNotifyOpts
function M.debug(msg, opts)
  if not require("lazy.core.config").options.debug then
    return
  end
  opts = opts or {}
  if opts.title then
    opts.title = "lazy.nvim: " .. opts.title
  end
  if type(msg) == "string" then
    M.notify(msg, opts)
  else
    opts.lang = "lua"
    M.notify(vim.inspect(msg), opts)
  end
end

local function can_merge(v)
  return type(v) == "table" and (vim.tbl_isempty(v) or not M.is_list(v))
end

--- Merges the values similar to vim.tbl_deep_extend with the **force** behavior,
--- but the values can be any type, in which case they override the values on the left.
--- Values will me merged in-place in the first left-most table. If you want the result to be in
--- a new table, then simply pass an empty table as the first argument `vim.merge({}, ...)`
--- Supports clearing values by setting a key to `vim.NIL`
---@generic T
---@param ... T
---@return T
function M.merge(...)
  local ret = select(1, ...)
  if ret == vim.NIL then
    ret = nil
  end
  for i = 2, select("#", ...) do
    local value = select(i, ...)
    if can_merge(ret) and can_merge(value) then
      for k, v in pairs(value) do
        ret[k] = M.merge(ret[k], v)
      end
    elseif value == vim.NIL then
      ret = nil
    elseif value ~= nil then
      ret = value
    end
  end
  return ret
end

function M.lazy_require(module)
  local mod = nil
  -- if already loaded, return the module
  -- otherwise return a lazy module
  return type(package.loaded[module]) == "table" and package.loaded[module]
    or setmetatable({}, {
      __index = function(_, key)
        mod = mod or require(module)
        return mod[key]
      end,
    })
end

---@param t table
---@param key string|string[]
---@return any
function M.key_get(t, key)
  local path = type(key) == "table" and key or vim.split(key, ".", true)
  local value = t
  for _, k in ipairs(path) do
    if type(value) ~= "table" then
      return value
    end
    value = value[k]
  end
  return value
end

---@param t table
---@param key string|string[]
---@param value any
function M.key_set(t, key, value)
  local path = type(key) == "table" and key or vim.split(key, ".", true)
  local last = t
  for i = 1, #path - 1 do
    local k = path[i]
    if type(last[k]) ~= "table" then
      last[k] = {}
    end
    last = last[k]
  end
  last[path[#path]] = value
end

return M
```

## File: `lua/lazy/core/handler/cmd.lua`
```
local Loader = require("lazy.core.loader")
local Util = require("lazy.core.util")

---@class LazyCmdHandler:LazyHandler
local M = {}

function M:_load(cmd)
  vim.api.nvim_del_user_command(cmd)
  Util.track({ cmd = cmd })
  Loader.load(self.active[cmd], { cmd = cmd })
  Util.track()
end

---@param cmd string
function M:_add(cmd)
  vim.api.nvim_create_user_command(cmd, function(event)
    local command = {
      cmd = cmd,
      bang = event.bang or nil,
      mods = event.smods,
      args = event.fargs,
      count = event.count >= 0 and event.range == 0 and event.count or nil,
    }

    if event.range == 1 then
      command.range = { event.line1 }
    elseif event.range == 2 then
      command.range = { event.line1, event.line2 }
    end

    ---@type string
    local plugins = "`" .. table.concat(vim.tbl_values(self.active[cmd]), ", ") .. "`"

    self:_load(cmd)

    local info = vim.api.nvim_get_commands({})[cmd] or vim.api.nvim_buf_get_commands(0, {})[cmd]
    if not info then
      vim.schedule(function()
        Util.error("Command `" .. cmd .. "` not found after loading " .. plugins)
      end)
      return
    end

    command.nargs = info.nargs
    if event.args and event.args ~= "" and info.nargs and info.nargs:find("[1?]") then
      command.args = { event.args }
    end
    vim.cmd(command)
  end, {
    bang = true,
    range = true,
    nargs = "*",
    complete = function(_, line)
      self:_load(cmd)
      -- NOTE: return the newly loaded command completion
      return vim.fn.getcompletion(line, "cmdline")
    end,
  })
end

---@param value string
function M:_del(value)
  pcall(vim.api.nvim_del_user_command, value)
end

return M
```

## File: `lua/lazy/core/handler/event.lua`
```
local Config = require("lazy.core.config")
local Loader = require("lazy.core.loader")
local Util = require("lazy.core.util")

---@class LazyEventOpts
---@field event string
---@field group? string
---@field exclude? string[]
---@field data? any
---@field buffer? number

---@alias LazyEvent {id:string, event:string[]|string, pattern?:string[]|string}
---@alias LazyEventSpec string|{event?:string|string[], pattern?:string|string[]}|string[]

---@class LazyEventHandler:LazyHandler
---@field events table<string,true>
---@field group number
local M = {}

-- Event dependencies
M.triggers = {
  FileType = "BufReadPost",
  BufReadPost = "BufReadPre",
}

-- A table of mappings for custom events
-- Can be used by distros to add custom events (see usage in LazyVim)
---@type table<string, LazyEvent>
M.mappings = {
  VeryLazy = { id = "VeryLazy", event = "User", pattern = "VeryLazy" },
  -- Example:
  -- LazyFile = { id = "LazyFile", event = { "BufReadPost", "BufNewFile", "BufWritePre" } },
}
M.mappings["User VeryLazy"] = M.mappings.VeryLazy

M.group = vim.api.nvim_create_augroup("lazy_handler_event", { clear = true })

---@param spec LazyEventSpec
---@return LazyEvent
function M:_parse(spec)
  local ret = M.mappings[spec] --[[@as LazyEvent?]]
  if ret then
    return ret
  end
  if type(spec) == "string" then
    local event, pattern = spec:match("^(%w+)%s+(.*)$")
    event = event or spec
    return { id = spec, event = event, pattern = pattern }
  elseif Util.is_list(spec) then
    ret = { id = table.concat(spec, "|"), event = spec }
  else
    ret = spec --[[@as LazyEvent]]
    if not ret.id then
      ---@diagnostic disable-next-line: assign-type-mismatch, param-type-mismatch
      ret.id = type(ret.event) == "string" and ret.event or table.concat(ret.event, "|")
      if ret.pattern then
        ---@diagnostic disable-next-line: assign-type-mismatch, param-type-mismatch
        ret.id = ret.id .. " " .. (type(ret.pattern) == "string" and ret.pattern or table.concat(ret.pattern, ", "))
      end
    end
  end
  return ret
end

---@param event LazyEvent
function M:_add(event)
  local done = false
  vim.api.nvim_create_autocmd(event.event, {
    group = self.group,
    once = true,
    pattern = event.pattern,
    callback = function(ev)
      if done or not self.active[event.id] then
        return
      end
      -- HACK: work-around for https://github.com/neovim/neovim/issues/25526
      done = true
      if event.id ~= "VeryLazy" then
        Util.track({ [self.type] = event.id })
      end

      local state = M.get_state(ev.event, ev.buf, ev.data)

      -- load the plugins
      Loader.load(self.active[event.id], { [self.type] = event.id })

      -- check if any plugin created an event handler for this event and fire the group
      for _, s in ipairs(state) do
        M.trigger(s)
      end
      if event.id ~= "VeryLazy" then
        Util.track()
      end
    end,
  })
end

-- Get the current state of the event and all the events that will be fired
---@param event string
---@param buf number
---@param data any
function M.get_state(event, buf, data)
  local state = {} ---@type LazyEventOpts[]
  while event do
    table.insert(state, 1, {
      event = event,
      exclude = event ~= "FileType" and M.get_augroups(event) or nil,
      buffer = buf,
      data = data,
    })
    data = nil -- only pass the data to the first event
    event = M.triggers[event]
  end
  return state
end

-- Get all augroups for the events
---@param event string
function M.get_augroups(event)
  local groups = {} ---@type string[]
  for _, autocmd in ipairs(vim.api.nvim_get_autocmds({ event = event })) do
    if autocmd.group_name then
      table.insert(groups, autocmd.group_name)
    end
  end
  return groups
end

-- Trigger an event. When a group is given, only the events in that group will be triggered.
-- When exclude is set, the events in those groups will be skipped.
---@param opts LazyEventOpts
function M.trigger(opts)
  if opts.group or opts.exclude == nil then
    return M._trigger(opts)
  end
  local done = {} ---@type table<string,true>
  for _, autocmd in ipairs(vim.api.nvim_get_autocmds({ event = opts.event })) do
    local id = autocmd.event .. ":" .. (autocmd.group or "") ---@type string
    local skip = done[id] or (opts.exclude and vim.tbl_contains(opts.exclude, autocmd.group_name))
    done[id] = true
    if autocmd.group and not skip then
      opts.group = autocmd.group_name
      M._trigger(opts)
    end
  end
end

-- Trigger an event
---@param opts LazyEventOpts
function M._trigger(opts)
  if Config.options.debug then
    Util.info({
      "# Firing Events",
      "  - **event:** " .. opts.event,
      opts.group and ("  - **group:** " .. opts.group),
      opts.buffer and ("  - **buffer:** " .. opts.buffer),
    })
  end
  Util.track({ event = opts.group or opts.event })
  Util.try(function()
    vim.api.nvim_exec_autocmds(opts.event, {
      buffer = opts.buffer,
      group = opts.group,
      modeline = false,
      data = opts.data,
    })
    Util.track()
  end)
end

return M
```

## File: `lua/lazy/core/handler/ft.lua`
```
local Event = require("lazy.core.handler.event")
local Loader = require("lazy.core.loader")

---@class LazyFiletypeHandler:LazyEventHandler
local M = {}
M.extends = Event

---@param plugin LazyPlugin
function M:add(plugin)
  self.super.add(self, plugin)
  if plugin.ft then
    Loader.ftdetect(plugin.dir)
  end
end

---@return LazyEvent
function M:_parse(value)
  return {
    id = value,
    event = "FileType",
    pattern = value,
  }
end

return M
```

## File: `lua/lazy/core/handler/init.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.core.util")

---@class LazyHandler
---@field type LazyHandlerTypes
---@field extends? LazyHandler
---@field active table<string,table<string,string>>
---@field managed table<string,string> mapping handler keys to plugin names
---@field super LazyHandler
local M = {}

---@enum LazyHandlerTypes
M.types = {
  keys = "keys",
  event = "event",
  cmd = "cmd",
  ft = "ft",
}

---@type table<string,LazyHandler>
M.handlers = {}

M.did_setup = false

function M.init()
  for _, type in pairs(M.types) do
    M.handlers[type] = M.new(type)
  end
end

function M.setup()
  M.did_setup = true
  for _, plugin in pairs(Config.plugins) do
    Util.try(function()
      M.enable(plugin)
    end, "Failed to setup handlers for " .. plugin.name)
  end
end

---@param plugin LazyPlugin
function M.disable(plugin)
  for type in pairs(plugin._.handlers or {}) do
    M.handlers[type]:del(plugin)
  end
end

---@param plugin LazyPlugin
function M.enable(plugin)
  if not plugin._.loaded then
    if not plugin._.handlers then
      M.resolve(plugin)
    end
    for type in pairs(plugin._.handlers or {}) do
      M.handlers[type]:add(plugin)
    end
  end
end

---@param type LazyHandlerTypes
function M.new(type)
  ---@type LazyHandler
  local handler = require("lazy.core.handler." .. type)
  local super = handler.extends or M
  local self = setmetatable({}, { __index = setmetatable(handler, { __index = super }) })
  self.super = super
  self.active = {}
  self.managed = {}
  self.type = type
  return self
end

---@param _value string
---@protected
function M:_add(_value) end

---@param _value string
---@protected
function M:_del(_value) end

---@param value any
---@param _plugin LazyPlugin
---@return string|{id:string}
function M:_parse(value, _plugin)
  assert(type(value) == "string", "Expected string, got " .. vim.inspect(value))
  return value
end

---@param values any[]
---@param plugin LazyPlugin
function M:_values(values, plugin)
  ---@type table<string,any>
  local ret = {}
  for _, value in ipairs(values) do
    local parsed = self:_parse(value, plugin)
    ret[type(parsed) == "string" and parsed or parsed.id] = parsed
  end
  return ret
end

---@param plugin LazyPlugin
function M.resolve(plugin)
  local Plugin = require("lazy.core.plugin")
  plugin._.handlers = {}
  for type, handler in pairs(M.handlers) do
    if plugin[type] then
      plugin._.handlers[type] = handler:_values(Plugin.values(plugin, type, true), plugin)
    end
  end
end

---@param plugin LazyPlugin
function M:add(plugin)
  for key, value in pairs(plugin._.handlers[self.type] or {}) do
    if not self.active[key] then
      self.active[key] = {}
      self:_add(value)
      self.managed[key] = plugin.name
    end
    self.active[key][plugin.name] = plugin.name
  end
end

---@param plugin LazyPlugin
function M:del(plugin)
  if not plugin._.handlers then
    return
  end
  for key, value in pairs(plugin._.handlers[self.type] or {}) do
    if self.active[key] and self.active[key][plugin.name] then
      self.active[key][plugin.name] = nil
      if vim.tbl_isempty(self.active[key]) then
        self:_del(value)
        self.active[key] = nil
      end
    end
  end
end

return M
```

## File: `lua/lazy/core/handler/keys.lua`
```
local Loader = require("lazy.core.loader")
local Util = require("lazy.core.util")

---@class LazyKeysBase
---@field desc? string
---@field noremap? boolean
---@field remap? boolean
---@field expr? boolean
---@field nowait? boolean
---@field ft? string|string[]

---@class LazyKeysSpec: LazyKeysBase
---@field [1] string lhs
---@field [2]? string|fun():string?|false rhs
---@field mode? string|string[]

---@class LazyKeys: LazyKeysBase
---@field lhs string lhs
---@field rhs? string|fun() rhs
---@field mode? string
---@field id string
---@field name string

---@class LazyKeysHandler:LazyHandler
local M = {}

local skip = { mode = true, id = true, ft = true, rhs = true, lhs = true }

---@param value string|LazyKeysSpec
---@param mode? string
---@return LazyKeys
function M.parse(value, mode)
  value = type(value) == "string" and { value } or value --[[@as LazyKeysSpec]]
  local ret = vim.deepcopy(value) --[[@as LazyKeys]]
  ret.lhs = ret[1] or ""
  ret.rhs = ret[2]
  ---@diagnostic disable-next-line: no-unknown
  ret[1] = nil
  ---@diagnostic disable-next-line: no-unknown
  ret[2] = nil
  ret.mode = mode or "n"
  ret.id = vim.api.nvim_replace_termcodes(ret.lhs, true, true, true)

  if ret.ft then
    local ft = type(ret.ft) == "string" and { ret.ft } or ret.ft --[[@as string[] ]]
    ret.id = ret.id .. " (" .. table.concat(ft, ", ") .. ")"
  end

  if ret.mode ~= "n" then
    ret.id = ret.id .. " (" .. ret.mode .. ")"
  end
  return ret
end

---@param keys LazyKeys
function M.to_string(keys)
  return keys.lhs .. (keys.mode == "n" and "" or " (" .. keys.mode .. ")")
end

---@param lhs string
---@param mode? string
function M:have(lhs, mode)
  local keys = M.parse(lhs, mode)
  return self.managed[keys.id] ~= nil
end

function M:_values(values)
  return M.resolve(values)
end

---@param spec? (string|LazyKeysSpec)[]
function M.resolve(spec)
  ---@type LazyKeys[]
  local values = {}
  ---@diagnostic disable-next-line: no-unknown
  for _, value in ipairs(spec or {}) do
    value = type(value) == "string" and { value } or value --[[@as LazyKeysSpec]]
    value.mode = value.mode or "n"
    local modes = (type(value.mode) == "table" and value.mode or { value.mode }) --[=[@as string[]]=]
    for _, mode in ipairs(modes) do
      local keys = M.parse(value, mode)
      if keys.rhs == vim.NIL or keys.rhs == false then
        values[keys.id] = nil
      else
        values[keys.id] = keys
      end
    end
  end
  return values
end

---@param keys LazyKeys
function M.opts(keys)
  local opts = {} ---@type LazyKeysBase
  ---@diagnostic disable-next-line: no-unknown
  for k, v in pairs(keys) do
    if type(k) ~= "number" and not skip[k] then
      ---@diagnostic disable-next-line: no-unknown
      opts[k] = v
    end
  end
  return opts
end

---@param keys LazyKeys
function M.is_nop(keys)
  return type(keys.rhs) == "string" and (keys.rhs == "" or keys.rhs:lower() == "<nop>")
end

---@param keys LazyKeys
function M:_add(keys)
  local lhs = keys.lhs
  local opts = M.opts(keys)

  ---@param buf? number
  local function add(buf)
    if M.is_nop(keys) then
      return self:_set(keys, buf)
    end

    vim.keymap.set(keys.mode, lhs, function()
      local plugins = self.active[keys.id]

      -- always delete the mapping immediately to prevent recursive mappings
      self:_del(keys)
      self.active[keys.id] = nil

      if plugins then
        local name = M.to_string(keys)
        Util.track({ keys = name })
        Loader.load(plugins, { keys = name })
        Util.track()
      end

      if keys.mode:sub(-1) == "a" then
        lhs = lhs .. "<C-]>"
      end
      local feed = vim.api.nvim_replace_termcodes("<Ignore>" .. lhs, true, true, true)
      -- insert instead of append the lhs
      vim.api.nvim_feedkeys(feed, "i", false)
    end, {
      desc = opts.desc,
      nowait = opts.nowait,
      -- we do not return anything, but this is still needed to make operator pending mappings work
      expr = true,
      buffer = buf,
    })
  end

  -- buffer-local mappings
  if keys.ft then
    vim.api.nvim_create_autocmd("FileType", {
      pattern = keys.ft,
      callback = function(event)
        if self.active[keys.id] and not M.is_nop(keys) then
          add(event.buf)
        else
          -- Only create the mapping if its managed by lazy
          -- otherwise the plugin is supposed to manage it
          self:_set(keys, event.buf)
        end
      end,
    })
  else
    add()
  end
end

-- Delete a mapping and create the real global/buffer-local
-- mapping when needed
---@param keys LazyKeys
function M:_del(keys)
  -- bufs will be all buffers of the filetype for a buffer-local mapping
  -- OR `false` for a global mapping
  local bufs = { false }

  if keys.ft then
    local ft = type(keys.ft) == "string" and { keys.ft } or keys.ft --[[@as string[] ]]
    bufs = vim.tbl_filter(function(buf)
      return vim.tbl_contains(ft, vim.bo[buf].filetype)
    end, vim.api.nvim_list_bufs())
  end

  for _, buf in ipairs(bufs) do
    pcall(vim.keymap.del, keys.mode, keys.lhs, { buffer = buf or nil })
    self:_set(keys, buf or nil)
  end
end

-- Create a mapping if it is managed by lazy
---@param keys LazyKeys
---@param buf number?
function M:_set(keys, buf)
  if keys.rhs then
    local opts = M.opts(keys)
    ---@diagnostic disable-next-line: inject-field
    opts.buffer = buf
    vim.keymap.set(keys.mode, keys.lhs, keys.rhs, opts)
  end
end

return M
```

## File: `lua/lazy/manage/checker.lua`
```
local Config = require("lazy.core.config")
local Git = require("lazy.manage.git")
local Manage = require("lazy.manage")
local Plugin = require("lazy.core.plugin")
local State = require("lazy.state")
local Util = require("lazy.util")

local M = {}

M.running = false
M.updated = {}
M.reported = {}

function M.start()
  M.fast_check()
  if M.schedule() > 0 and not M.has_errors() then
    Manage.log({
      clear = false,
      show = false,
      check = true,
      concurrency = Config.options.checker.concurrency,
    })
  end
end

function M.schedule()
  State.read() -- update state
  local next_check = State.checker.last_check + Config.options.checker.frequency - os.time()
  next_check = math.max(next_check, 0)
  vim.defer_fn(M.check, next_check * 1000)
  return next_check
end

---@param opts? {report:boolean} report defaults to true
function M.fast_check(opts)
  opts = opts or {}
  for _, plugin in pairs(Config.plugins) do
    -- don't check local plugins here, since we mark them as needing updates
    -- only if local is behind upstream (if the git log task gives no output)
    if plugin._.installed and not (plugin.pin or plugin._.is_local) then
      plugin._.updates = nil
      local info = Git.info(plugin.dir)
      local ok, target = pcall(Git.get_target, plugin)
      if ok and info and target and not Git.eq(info, target) then
        plugin._.updates = { from = info, to = target }
      end
    end
  end
  M.report(opts.report ~= false)
end

function M.has_errors()
  for _, plugin in pairs(Config.plugins) do
    if Plugin.has_errors(plugin) then
      return true
    end
  end
  return false
end

function M.check()
  State.checker.last_check = os.time()
  State.write() -- update state
  if M.has_errors() then
    M.schedule()
  else
    Manage.check({
      clear = false,
      show = false,
      concurrency = Config.options.checker.concurrency,
    }):wait(function()
      M.report()
      M.schedule()
    end)
  end
end

---@param notify? boolean
function M.report(notify)
  local lines = {}
  M.updated = {}
  for _, plugin in pairs(Config.plugins) do
    if plugin._.updates then
      table.insert(M.updated, plugin.name)
      if not vim.tbl_contains(M.reported, plugin.name) then
        table.insert(lines, "- **" .. plugin.name .. "**")
        table.insert(M.reported, plugin.name)
      end
    end
  end
  if #lines > 0 and notify and Config.options.checker.notify and not Config.headless() then
    table.insert(lines, 1, "# Plugin Updates")
    Util.info(lines)
  end
end

return M
```

## File: `lua/lazy/manage/git.lua`
```
local Config = require("lazy.core.config")
local Process = require("lazy.manage.process")
local Semver = require("lazy.manage.semver")
local Util = require("lazy.util")

local M = {}

---@alias GitInfo {branch?:string, commit?:string, tag?:string, version?:Semver}

---@param repo string
---@param details? boolean Fetching details is slow! Don't loop over a plugin to fetch all details!
---@return GitInfo?
function M.info(repo, details)
  local line = M.head(repo)
  if line then
    ---@type string, string
    local ref, branch = line:match("ref: refs/(heads/(.*))")
    local ret = ref and {
      branch = branch,
      commit = M.ref(repo, ref),
    } or { commit = line }

    if details then
      for tag, tag_ref in pairs(M.get_tag_refs(repo)) do
        if tag_ref == ret.commit then
          ret.tag = tag
          ret.version = ret.version or Semver.version(tag)
        end
      end
    end
    return ret
  end
end

---@param a GitInfo
---@param b GitInfo
function M.eq(a, b)
  local ra = a.commit and a.commit:sub(1, 7)
  local rb = b.commit and b.commit:sub(1, 7)
  return ra == rb
end

function M.head(repo)
  return Util.head(repo .. "/.git/HEAD")
end

---@class TaggedSemver: Semver
---@field tag string

---@param spec? string
function M.get_versions(repo, spec)
  local range = Semver.range(spec or "*")
  ---@type TaggedSemver[]
  local versions = {}
  for _, tag in ipairs(M.get_tags(repo)) do
    local v = Semver.version(tag)
    ---@cast v TaggedSemver
    if v and range:matches(v) then
      v.tag = tag
      table.insert(versions, v)
    end
  end
  return versions
end

function M.get_tags(repo)
  ---@type string[]
  local ret = {}
  Util.ls(repo .. "/.git/refs/tags", function(_, name)
    ret[#ret + 1] = name
  end)
  for name in pairs(M.packed_refs(repo)) do
    local tag = name:match("^tags/(.*)")
    if tag then
      ret[#ret + 1] = tag
    end
  end
  return ret
end

---@param plugin LazyPlugin
---@return string?
function M.get_branch(plugin)
  if plugin.branch then
    return plugin.branch
  else
    -- we need to return the default branch
    -- Try origin first
    local main = M.ref(plugin.dir, "remotes/origin/HEAD")
    if main then
      local branch = main:match("ref: refs/remotes/origin/(.*)")
      if branch then
        return branch
      end
    end

    -- fallback to local HEAD
    main = assert(M.head(plugin.dir))
    return main and main:match("ref: refs/heads/(.*)")
  end
end

-- Return the last commit for the given branch
---@param repo string
---@param branch string
---@param origin? boolean
function M.get_commit(repo, branch, origin)
  if origin then
    -- origin ref might not exist if it is the same as local
    return M.ref(repo, "remotes/origin", branch) or M.ref(repo, "heads", branch)
  else
    return M.ref(repo, "heads", branch)
  end
end

---@param plugin LazyPlugin
---@return GitInfo?
function M.get_target(plugin)
  if plugin._.is_local then
    local info = M.info(plugin.dir)
    local branch = assert(info and info.branch or M.get_branch(plugin))
    return { branch = branch, commit = M.get_commit(plugin.dir, branch, true) }
  end

  local branch = assert(M.get_branch(plugin))

  if plugin.commit then
    return {
      branch = branch,
      commit = plugin.commit,
    }
  end
  if plugin.tag then
    return {
      branch = branch,
      tag = plugin.tag,
      commit = M.ref(plugin.dir, "tags/" .. plugin.tag),
    }
  end

  local version = (plugin.version == nil and plugin.branch == nil) and Config.options.defaults.version or plugin.version
  if version then
    local last = Semver.last(M.get_versions(plugin.dir, version))
    if last then
      return {
        branch = branch,
        version = last,
        tag = last.tag,
        commit = M.ref(plugin.dir, "tags/" .. last.tag),
      }
    end
  end
  return { branch = branch, commit = M.get_commit(plugin.dir, branch, true) }
end

function M.ref(repo, ...)
  local ref = table.concat({ ... }, "/")

  -- if this is a tag ref, then dereference it instead
  if ref:find("tags/", 1, true) == 1 then
    local tags = M.get_tag_refs(repo, ref)
    for _, tag_ref in pairs(tags) do
      return tag_ref
    end
  end

  -- otherwise just get the ref
  return Util.head(repo .. "/.git/refs/" .. ref) or M.packed_refs(repo)[ref]
end

function M.packed_refs(repo)
  local ok, refs = pcall(Util.read_file, repo .. "/.git/packed-refs")
  ---@type table<string,string>
  local ret = {}
  if ok then
    for _, line in ipairs(vim.split(refs, "\n")) do
      local ref, name = line:match("^(.*) refs/(.*)$")
      if ref then
        ret[name] = ref
      end
    end
  end
  return ret
end

-- this is slow, so don't use on a loop over all plugins!
---@param tagref string?
function M.get_tag_refs(repo, tagref)
  tagref = tagref or "--tags"
  ---@type table<string,string>
  local tags = {}
  local ok, lines = pcall(function()
    return Process.exec({ "git", "show-ref", "-d", tagref }, { cwd = repo })
  end)
  if not ok then
    return {}
  end
  for _, line in ipairs(lines) do
    local ref, tag = line:match("^(%w+) refs/tags/([^%^]+)%^?{?}?$")
    if ref then
      tags[tag] = ref
    end
  end
  return tags
end

---@param repo string
function M.get_origin(repo)
  return M.get_config(repo)["remote.origin.url"]
end

---@param repo string
function M.get_config(repo)
  local ok, config = pcall(Util.read_file, repo .. "/.git/config")
  if not ok then
    return {}
  end
  ---@type table<string, string>
  local ret = {}
  ---@type string
  local current_section = nil
  for line in config:gmatch("[^\n]+") do
    -- Check if the line is a section header
    local section = line:match("^%s*%[(.+)%]%s*$")
    if section then
      ---@type string
      current_section = section:gsub('%s+"', "."):gsub('"+%s*$', "")
    else
      -- Ignore comments and blank lines
      if not line:match("^%s*[#;]") and line:match("%S") then
        local key, value = line:match("^%s*(%S+)%s*=%s*(.+)%s*$")
        ret[current_section .. "." .. key] = value
      end
    end
  end
  return ret
end

function M.count(repo, commit1, commit2)
  local lines = Process.exec({ "git", "rev-list", "--count", commit1 .. ".." .. commit2 }, { cwd = repo })
  return tonumber(lines[1] or "0") or 0
end

function M.age(repo, commit)
  local lines = Process.exec({ "git", "show", "-s", "--format=%cr", "--date=short", commit }, { cwd = repo })
  return lines[1] or ""
end

return M
```

## File: `lua/lazy/manage/init.lua`
```
local Config = require("lazy.core.config")
local Plugin = require("lazy.core.plugin")
local Runner = require("lazy.manage.runner")

local M = {}

---@class ManagerOpts
---@field wait? boolean
---@field clear? boolean
---@field show? boolean
---@field mode? string
---@field plugins? (LazyPlugin|string)[]
---@field concurrency? number
---@field lockfile? boolean

---@param ropts RunnerOpts
---@param opts? ManagerOpts
function M.run(ropts, opts)
  opts = opts or {}

  local mode = opts.mode
  local event = mode and ("Lazy" .. mode:sub(1, 1):upper() .. mode:sub(2))

  if event then
    vim.api.nvim_exec_autocmds("User", { pattern = event .. "Pre", modeline = false })
  end

  if opts.plugins then
    ---@param plugin string|LazyPlugin
    opts.plugins = vim.tbl_map(function(plugin)
      return type(plugin) == "string" and Config.plugins[plugin] or plugin
    end, vim.tbl_values(opts.plugins))
    ropts.plugins = opts.plugins
  end

  ropts.concurrency = ropts.concurrency or opts.concurrency or Config.options.concurrency

  if opts.clear then
    M.clear(opts.plugins)
  end

  if opts.show ~= false then
    vim.schedule(function()
      require("lazy.view").show(opts.mode)
    end)
  end

  ---@type Runner
  local runner = Runner.new(ropts)
  runner:start()

  vim.api.nvim_exec_autocmds("User", { pattern = "LazyRender", modeline = false })

  -- wait for post-install to finish
  runner:wait(function()
    vim.api.nvim_exec_autocmds("User", { pattern = "LazyRender", modeline = false })
    Plugin.update_state()
    require("lazy.manage.checker").fast_check({ report = false })
    if event then
      vim.api.nvim_exec_autocmds("User", { pattern = event, modeline = false })
    end
  end)

  if opts.wait then
    runner:wait()
  end
  return runner
end

---@generic O: ManagerOpts
---@param opts? O
---@param defaults? ManagerOpts
---@return O
function M.opts(opts, defaults)
  return vim.tbl_deep_extend("force", { clear = true }, defaults or {}, opts or {})
end

---@param opts? ManagerOpts
function M.install(opts)
  opts = M.opts(opts, { mode = "install" })
  return M.run({
    pipeline = {
      "plugin.exists",
      "git.clone",
      { "git.checkout", lockfile = opts.lockfile },
      "plugin.docs",
      {
        "wait",
        ---@param runner Runner
        sync = function(runner)
          require("lazy.pkg").update()
          Plugin.load()
          runner:update()
        end,
      },
      "plugin.build",
    },
    plugins = function(plugin)
      return not (plugin._.installed and not plugin._.build)
    end,
  }, opts):wait(function()
    require("lazy.manage.lock").update()
    require("lazy.help").update()
  end)
end

---@param opts? ManagerOpts
function M.update(opts)
  opts = M.opts(opts, { mode = "update" })
  return M.run({
    pipeline = {
      "plugin.exists",
      "git.origin",
      "git.branch",
      "git.fetch",
      "git.status",
      { "git.checkout", lockfile = opts.lockfile },
      "plugin.docs",
      {
        "wait",
        ---@param runner Runner
        sync = function(runner)
          require("lazy.pkg").update()
          Plugin.load()
          runner:update()
        end,
      },
      "plugin.build",
      { "git.log", updated = true },
    },
    plugins = function(plugin)
      return plugin.url and plugin._.installed
    end,
  }, opts):wait(function()
    require("lazy.manage.lock").update()
    require("lazy.help").update()
  end)
end
--
---@param opts? ManagerOpts
function M.restore(opts)
  opts = M.opts(opts, { mode = "restore", lockfile = true })
  return M.update(opts)
end

---@param opts? ManagerOpts
function M.check(opts)
  opts = M.opts(opts, { mode = "check" })
  opts = opts or {}
  return M.run({
    pipeline = {
      "plugin.exists",
      { "git.origin", check = true },
      "git.fetch",
      "git.status",
      "wait",
      { "git.log", check = true },
    },
    plugins = function(plugin)
      return plugin.url and plugin._.installed
    end,
  }, opts)
end

---@param opts? ManagerOpts | {check?:boolean}
function M.log(opts)
  opts = M.opts(opts, { mode = "log" })
  return M.run({
    pipeline = {
      { "git.origin", check = true },
      { "git.log", check = opts.check },
    },
    plugins = function(plugin)
      return plugin.url and plugin._.installed
    end,
  }, opts)
end

---@param opts? ManagerOpts
function M.build(opts)
  opts = M.opts(opts, { mode = "build" })
  return M.run({
    pipeline = { { "plugin.build", force = true } },
    plugins = function()
      return false
    end,
  }, opts)
end

---@param opts? ManagerOpts
function M.sync(opts)
  opts = M.opts(opts)
  if opts.clear then
    M.clear()
    opts.clear = false
  end
  if opts.show ~= false then
    vim.schedule(function()
      require("lazy.view").show("sync")
    end)
    opts.show = false
  end

  vim.api.nvim_exec_autocmds("User", { pattern = "LazySyncPre", modeline = false })

  local clean_opts = vim.deepcopy(opts)
  clean_opts.plugins = nil
  local clean = M.clean(clean_opts)
  local install = M.install(opts)
  local update = M.update(opts)
  clean:wait(function()
    install:wait(function()
      update:wait(function()
        vim.api.nvim_exec_autocmds("User", { pattern = "LazySync", modeline = false })
      end)
    end)
  end)
end

---@param opts? ManagerOpts
function M.clean(opts)
  opts = M.opts(opts, { mode = "clean" })
  return M.run({
    pipeline = { "fs.clean" },
    plugins = Config.to_clean,
  }, opts):wait(function()
    require("lazy.manage.lock").update()
  end)
end

---@param plugins? LazyPlugin[]
function M.clear(plugins)
  for _, plugin in pairs(plugins or Config.plugins) do
    plugin._.updates = nil
    plugin._.updated = nil
    plugin._.cloned = nil
    plugin._.dirty = nil
    -- clear finished tasks
    if plugin._.tasks then
      ---@param task LazyTask
      plugin._.tasks = vim.tbl_filter(function(task)
        return task:running() or task:has_errors()
      end, plugin._.tasks)
    end
  end
  vim.api.nvim_exec_autocmds("User", { pattern = "LazyRender", modeline = false })
end

return M
```

## File: `lua/lazy/manage/lock.lua`
```
local Config = require("lazy.core.config")
local Git = require("lazy.manage.git")

local M = {}

---@alias LazyLockfile table<string, {commit:string, branch:string}>
---@type LazyLockfile
M.lock = {}
M._loaded = false

function M.update()
  M.load()
  vim.fn.mkdir(vim.fn.fnamemodify(Config.options.lockfile, ":p:h"), "p")
  local f = assert(io.open(Config.options.lockfile, "wb"))
  f:write("{\n")

  -- keep disabled and cond plugins
  for name in pairs(M.lock) do
    if not (Config.spec.disabled[name] or Config.spec.ignore_installed[name]) then
      M.lock[name] = nil
    end
  end

  for _, plugin in pairs(Config.plugins) do
    if not plugin._.is_local and plugin._.installed then
      local info = assert(Git.info(plugin.dir))
      M.lock[plugin.name] = {
        branch = info.branch or assert(Git.get_branch(plugin)),
        commit = assert(info.commit, "commit is nil"),
      }
    end
  end

  ---@type string[]
  local names = vim.tbl_keys(M.lock)
  table.sort(names)

  for n, name in ipairs(names) do
    local info = M.lock[name]
    f:write(([[  %q: { "branch": %q, "commit": %q }]]):format(name, info.branch, info.commit))
    if n ~= #names then
      f:write(",\n")
    end
  end
  f:write("\n}\n")
  f:close()
end

function M.load()
  if M._loaded then
    return
  end
  M.lock = {}
  M._loaded = true
  local f = io.open(Config.options.lockfile, "r")
  if f then
    ---@type string
    local data = f:read("*a")
    local ok, lock = pcall(vim.json.decode, data)
    if ok then
      M.lock = lock
    end
    f:close()
  end
end

---@param plugin LazyPlugin
---@return {commit:string, branch:string}
function M.get(plugin)
  M.load()
  return M.lock[plugin.name]
end

return M
```

## File: `lua/lazy/manage/process.lua`
```
local Async = require("lazy.async")
local Config = require("lazy.core.config")

---@diagnostic disable-next-line: no-unknown
local uv = vim.uv

---@class ProcessOpts
---@field args string[]
---@field cwd? string
---@field on_line? fun(line:string)
---@field on_exit? fun(ok:boolean, output:string)
---@field on_data? fun(data:string, is_stderr?:boolean)
---@field timeout? number
---@field env? table<string,string>

local M = {}

---@type table<uv_process_t, LazyProcess>
M.running = setmetatable({}, { __mode = "k" })

---@class LazyProcess: Async
---@field handle? uv_process_t
---@field pid? number
---@field cmd string
---@field opts ProcessOpts
---@field timeout? uv_timer_t
---@field timedout? boolean
---@field data string
---@field check? uv_check_t
---@field code? number
---@field signal? number
local Process = setmetatable({}, { __index = Async.Async })

---@param cmd string|string[]
---@param opts? ProcessOpts
function Process.new(cmd, opts)
  local self = setmetatable({}, { __index = Process })
  ---@async
  Process.init(self, function()
    self:_run()
  end)
  opts = opts or {}
  opts.args = opts.args or {}
  if type(cmd) == "table" then
    self.cmd = cmd[1]
    vim.list_extend(opts.args, vim.list_slice(cmd, 2))
  else
    self.cmd = cmd
  end
  opts.timeout = opts.timeout or (Config.options.git and Config.options.git.timeout * 1000)
  -- make sure the cwd is valid
  if not opts.cwd and type(uv.cwd()) ~= "string" then
    opts.cwd = uv.os_homedir()
  end
  opts.on_line = opts.on_line and vim.schedule_wrap(opts.on_line) or nil
  opts.on_data = opts.on_data and vim.schedule_wrap(opts.on_data) or nil
  self.data = ""
  self.opts = opts
  self.code = 1
  self.signal = 0
  return self
end

---@async
function Process:_run()
  self:guard()
  local stdout = assert(uv.new_pipe())
  local stderr = assert(uv.new_pipe())
  self.handle = uv.spawn(self.cmd, {
    stdio = { nil, stdout, stderr },
    args = self.opts.args,
    cwd = self.opts.cwd,
    env = self:env(),
  }, function(code, signal)
    self.code = code
    self.signal = signal
    if self.timeout then
      self.timeout:stop()
    end
    self.handle:close()
    stdout:close()
    stderr:close()
    self:resume()
  end)

  if self.handle then
    M.running[self.handle] = self
    stdout:read_start(function(err, data)
      self:on_data(err, data)
    end)
    stderr:read_start(function(err, data)
      self:on_data(err, data, true)
    end)
    self:suspend()
    while not (self.handle:is_closing() and stdout:is_closing() and stderr:is_closing()) do
      Async.yield()
    end
  else
    self.data = "Failed to spawn process " .. self.cmd .. " " .. vim.inspect(self.opts)
  end
  self:on_exit()
end

function Process:on_exit()
  self.data = self.data:gsub("[^\r\n]+\r", "")
  if self.timedout then
    self.data = self.data .. "\n" .. "Process was killed because it reached the timeout"
  elseif self.signal ~= 0 then
    self.data = self.data .. "\n" .. "Process was killed with SIG" .. M.signals[self.signal]:upper()
  end
  if self.opts.on_exit then
    self.opts.on_exit(self.code == 0 and self.signal == 0, self.data)
  end
end

function Process:guard()
  if self.opts.timeout then
    self.timeout = assert(uv.new_timer())
    self.timeout:start(self.opts.timeout, 0, function()
      self.timedout = true
      self:kill()
    end)
  end
end

function Process:env()
  ---@type table<string, string>
  local env = vim.tbl_extend("force", {
    GIT_SSH_COMMAND = "ssh -oBatchMode=yes",
  }, uv.os_environ(), self.opts.env or {})
  env.GIT_DIR = nil
  env.GIT_WORK_TREE = nil
  env.GIT_TERMINAL_PROMPT = "0"
  env.GIT_INDEX_FILE = nil

  ---@type string[]
  local env_flat = {}
  for k, v in pairs(env) do
    env_flat[#env_flat + 1] = k .. "=" .. v
  end
  return env_flat
end

---@param signals uv.aliases.signals|uv.aliases.signals[]|nil
function Process:kill(signals)
  if not self.handle or self.handle:is_closing() then
    return
  end
  signals = signals or { "sigterm", "sigkill" }
  signals = type(signals) == "table" and signals or { signals }
  ---@cast signals uv.aliases.signals[]
  local timer = assert(uv.new_timer())
  timer:start(0, 1000, function()
    if self.handle and not self.handle:is_closing() and #signals > 0 then
      self.handle:kill(table.remove(signals, 1))
    else
      timer:stop()
    end
  end)
end

---@param err? string
---@param data? string
---@param is_stderr? boolean
function Process:on_data(err, data, is_stderr)
  assert(not err, err)
  if not data then
    return
  end

  if self.opts.on_data then
    self.opts.on_data(data, is_stderr)
  end
  self.data = self.data .. data:gsub("\r\n", "\n")
  local lines = vim.split(vim.trim(self.data:gsub("\r$", "")):gsub("[^\n\r]+\r", ""), "\n")

  if self.opts.on_line then
    self.opts.on_line(lines[#lines])
  end
end

M.signals = {
  "hup",
  "int",
  "quit",
  "ill",
  "trap",
  "abrt",
  "bus",
  "fpe",
  "kill",
  "usr1",
  "segv",
  "usr2",
  "pipe",
  "alrm",
  "term",
  "chld",
  "cont",
  "stop",
  "tstp",
  "ttin",
  "ttou",
  "urg",
  "xcpu",
  "xfsz",
  "vtalrm",
  "prof",
  "winch",
  "io",
  "pwr",
  "emt",
  "sys",
  "info",
}

---@param cmd string|string[]
---@param opts? ProcessOpts
function M.spawn(cmd, opts)
  return Process.new(cmd, opts)
end

function M.abort()
  for _, proc in pairs(M.running) do
    proc:kill()
  end
end

---@async
---@param cmd string|string[]
---@param opts? ProcessOpts
function M.exec(cmd, opts)
  opts = opts or {}
  local proc = M.spawn(cmd, opts)
  proc:wait()
  return vim.split(proc.data, "\n"), proc.code
end

return M
```

## File: `lua/lazy/manage/reloader.lua`
```
local Config = require("lazy.core.config")
local Loader = require("lazy.core.loader")
local Plugin = require("lazy.core.plugin")
local Util = require("lazy.util")

local M = {}

---@type table<string, uv.aliases.fs_stat_table>
M.files = {}

---@type uv_timer_t
M.timer = nil

function M.enable()
  if M.timer then
    M.timer:stop()
  end
  if #Config.spec.modules > 0 then
    M.timer = assert(vim.uv.new_timer())
    M.check(true)
    M.timer:start(2000, 2000, M.check)
  end
end

function M.disable()
  if M.timer then
    M.timer:stop()
    M.timer = nil
  end
end

---@param h1 uv.aliases.fs_stat_table
---@param h2 uv.aliases.fs_stat_table
function M.eq(h1, h2)
  return h1 and h2 and h1.size == h2.size and h1.mtime.sec == h2.mtime.sec and h1.mtime.nsec == h2.mtime.nsec
end

function M.check(start)
  ---@type table<string,true>
  local checked = {}
  ---@type {file:string, what:string}[]
  local changes = {}

  -- spec is a module
  local function check(_, modpath)
    checked[modpath] = true
    local hash = vim.uv.fs_stat(modpath)
    if hash then
      if M.files[modpath] then
        if not M.eq(M.files[modpath], hash) then
          M.files[modpath] = hash
          table.insert(changes, { file = modpath, what = "changed" })
        end
      else
        M.files[modpath] = hash
        table.insert(changes, { file = modpath, what = "added" })
      end
    end
  end

  for _, modname in ipairs(Config.spec.modules) do
    Util.lsmod(modname, check)
  end

  for file in pairs(M.files) do
    if not checked[file] then
      table.insert(changes, { file = file, what = "deleted" })
      M.files[file] = nil
    end
  end

  if Loader.init_done and Config.mapleader ~= vim.g.mapleader then
    vim.schedule(function()
      require("lazy.core.util").warn("You need to set `vim.g.mapleader` **BEFORE** loading lazy")
    end)
    Config.mapleader = vim.g.mapleader
  end

  if Loader.init_done and Config.maplocalleader ~= vim.g.maplocalleader then
    vim.schedule(function()
      require("lazy.core.util").warn("You need to set `vim.g.maplocalleader` **BEFORE** loading lazy")
    end)
    Config.maplocalleader = vim.g.maplocalleader
  end

  if not (start or #changes == 0) then
    M.reload(changes)
  end
end

---@param {file:string, what:string}[]
function M.reload(changes)
  vim.schedule(function()
    if Config.options.change_detection.notify and not Config.headless() then
      local lines = { "# Config Change Detected. Reloading...", "" }
      for _, change in ipairs(changes) do
        table.insert(lines, "- **" .. change.what .. "**: `" .. vim.fn.fnamemodify(change.file, ":p:~:.") .. "`")
      end
      Util.warn(lines)
    end
    Plugin.load()
    vim.api.nvim_exec_autocmds("User", { pattern = "LazyRender", modeline = false })
    vim.api.nvim_exec_autocmds("User", { pattern = "LazyReload", modeline = false })
  end)
end

return M
```

## File: `lua/lazy/manage/runner.lua`
```
local Async = require("lazy.async")
local Config = require("lazy.core.config")
local Task = require("lazy.manage.task")

---@class RunnerOpts
---@field pipeline (string|{[1]:string, [string]:any})[]
---@field plugins? LazyPlugin[]|fun(plugin:LazyPlugin):any?
---@field concurrency? number

---@class RunnerTask
---@field task? LazyTask
---@field step number

---@alias PipelineStep {task:string, opts?:TaskOptions }

---@class Runner
---@field _plugins table<string,LazyPlugin>
---@field _pipeline PipelineStep[]
---@field _opts RunnerOpts
---@field _running? Async
local Runner = {}

---@param opts RunnerOpts
function Runner.new(opts)
  local self = setmetatable({}, { __index = Runner })
  self._opts = opts or {}

  local plugins = self._opts.plugins
  ---@type LazyPlugin[]
  local pp = {}
  if type(plugins) == "function" then
    pp = vim.tbl_filter(plugins, Config.plugins)
  else
    pp = plugins or Config.plugins
  end
  self._plugins = {}
  for _, plugin in ipairs(pp) do
    self._plugins[plugin.name] = plugin
  end

  ---@param step string|(TaskOptions|{[1]:string})
  self._pipeline = vim.tbl_map(function(step)
    return type(step) == "string" and { task = step } or { task = step[1], opts = step }
  end, self._opts.pipeline)

  return self
end

function Runner:plugin(name)
  return self._plugins[name]
end

--- Update plugins
function Runner:update()
  for name in pairs(self._plugins) do
    self._plugins[name] = Config.plugins[name] or self._plugins[name]
  end
end

function Runner:start()
  ---@async
  self._running = Async.new(function()
    self:_start()
  end)
end

---@async
function Runner:_start()
  ---@type string[]
  local names = vim.tbl_keys(self._plugins)
  table.sort(names)

  ---@type table<string,RunnerTask>
  local state = {}

  local active = 1
  local waiting = 0
  ---@type number?
  local wait_step = nil

  ---@async
  ---@param resume? boolean
  local function continue(resume)
    active = 0
    waiting = 0
    wait_step = nil
    local next = {} ---@type string[]

    -- check running tasks
    for _, name in ipairs(names) do
      state[name] = state[name] or { step = 0 }
      local s = state[name]
      local is_running = s.task and s.task:running()
      local step = self._pipeline[s.step]

      if is_running then
        -- still running
        active = active + 1
      -- selene:allow(empty_if)
      elseif s.task and s.task:has_errors() then
        -- don't continue tasks if there are errors
      elseif step and step.task == "wait" and not resume then
        -- waiting for sync
        waiting = waiting + 1
        wait_step = s.step
      else
        next[#next + 1] = name
      end
    end

    -- schedule next tasks
    for _, name in ipairs(next) do
      if self._opts.concurrency and active >= self._opts.concurrency then
        break
      end
      local s = state[name]
      local plugin = self:plugin(name)
      while s.step <= #self._pipeline do
        if s.step == #self._pipeline then
          -- done
          s.task = nil
          plugin._.working = false
          break
        elseif s.step < #self._pipeline then
          -- next
          s.step = s.step + 1
          local step = self._pipeline[s.step]
          if step.task == "wait" then
            plugin._.working = false
            waiting = waiting + 1
            wait_step = s.step
            break
          else
            s.task = self:queue(plugin, step)
            plugin._.working = true
            if s.task then
              active = active + 1
              s.task:wake(false)
              break
            end
          end
        end
      end
    end
  end

  while active > 0 do
    continue()
    if active == 0 and waiting > 0 then
      local sync = self._pipeline[wait_step]
      if sync and sync.opts and type(sync.opts.sync) == "function" then
        sync.opts.sync(self)
      end
      continue(true)
    end
    if active > 0 then
      self._running:suspend()
    end
  end
end

---@param plugin LazyPlugin
---@param step PipelineStep
---@return LazyTask?
function Runner:queue(plugin, step)
  assert(self._running and self._running:running(), "Runner is not running")
  local def = vim.split(step.task, ".", { plain = true })
  ---@type LazyTaskDef
  local task_def = require("lazy.manage.task." .. def[1])[def[2]]
  assert(task_def, "Task not found: " .. step.task)
  local opts = step.opts or {}
  if not (task_def.skip and task_def.skip(plugin, opts)) then
    return Task.new(plugin, def[2], task_def.run, opts)
  end
end

function Runner:is_running()
  return self._running and self._running:running()
end

-- Execute the callback async when done.
-- When no callback is specified, this will wait sync
---@param cb? fun()
function Runner:wait(cb)
  if not self:is_running() then
    if cb then
      cb()
    end
    return self
  end
  if cb then
    self._running:on("done", cb)
  else
    self._running:wait()
  end
  return self
end

return Runner
```

## File: `lua/lazy/manage/semver.lua`
```
local M = {}

---@class Semver
---@field [1] number
---@field [2] number
---@field [3] number
---@field major number
---@field minor number
---@field patch number
---@field prerelease? string
---@field build? string
---@field input? string
local Semver = {}
Semver.__index = Semver

function Semver:__index(key)
  return type(key) == "number" and ({ self.major, self.minor, self.patch })[key] or Semver[key]
end

function Semver:__newindex(key, value)
  if key == 1 then
    self.major = value
  elseif key == 2 then
    self.minor = value
  elseif key == 3 then
    self.patch = value
  else
    rawset(self, key, value)
  end
end

---@param other Semver
function Semver:__eq(other)
  for i = 1, 3 do
    if self[i] ~= other[i] then
      return false
    end
  end
  return self.prerelease == other.prerelease
end

function Semver:__tostring()
  local ret = table.concat({ self.major, self.minor, self.patch }, ".")
  if self.prerelease then
    ret = ret .. "-" .. self.prerelease
  end
  if self.build then
    ret = ret .. "+" .. self.build
  end
  return ret
end

---@param other Semver
function Semver:__lt(other)
  for i = 1, 3 do
    if self[i] > other[i] then
      return false
    elseif self[i] < other[i] then
      return true
    end
  end
  if self.prerelease and not other.prerelease then
    return true
  end
  if other.prerelease and not self.prerelease then
    return false
  end
  return (self.prerelease or "") < (other.prerelease or "")
end

---@param other Semver
function Semver:__le(other)
  return self < other or self == other
end

---@param version string|number[]
---@return Semver?
function M.version(version)
  if type(version) == "table" then
    return setmetatable({
      major = version[1] or 0,
      minor = version[2] or 0,
      patch = version[3] or 0,
    }, Semver)
  end
  local major, minor, patch, prerelease, build = version:match("^v?(%d+)%.?(%d*)%.?(%d*)%-?([^+]*)+?(.*)$")
  if major then
    return setmetatable({
      major = tonumber(major),
      minor = minor == "" and 0 or tonumber(minor),
      patch = patch == "" and 0 or tonumber(patch),
      prerelease = prerelease ~= "" and prerelease or nil,
      build = build ~= "" and build or nil,
      input = version,
    }, Semver)
  end
end

---@generic T: Semver
---@param versions T[]
---@return T?
function M.last(versions)
  local last = versions[1]
  for i = 2, #versions do
    if versions[i] > last then
      last = versions[i]
    end
  end
  return last
end

---@class SemverRange
---@field from Semver
---@field to? Semver
local Range = {}

---@param version string|Semver
function Range:matches(version)
  if type(version) == "string" then
    ---@diagnostic disable-next-line: cast-local-type
    version = M.version(version)
  end
  if version then
    if version.prerelease ~= self.from.prerelease then
      return false
    end
    return version >= self.from and (self.to == nil or version < self.to)
  end
end

---@param spec string
function M.range(spec)
  if spec == "*" or spec == "" then
    return setmetatable({ from = M.version("0.0.0") }, { __index = Range })
  end

  ---@type number?
  local hyphen = spec:find(" - ", 1, true)
  if hyphen then
    local a = spec:sub(1, hyphen - 1)
    local b = spec:sub(hyphen + 3)
    local parts = vim.split(b, ".", { plain = true })
    local ra = M.range(a)
    local rb = M.range(b)
    return setmetatable({
      from = ra and ra.from,
      to = rb and (#parts == 3 and rb.from or rb.to),
    }, { __index = Range })
  end
  ---@type string, string
  local mods, version = spec:lower():match("^([%^=>~]*)(.*)$")
  version = version:gsub("%.[%*x]", "")
  local parts = vim.split(version:gsub("%-.*", ""), ".", { plain = true })
  if #parts < 3 and mods == "" then
    mods = "~"
  end

  local semver = M.version(version)
  if semver then
    local from = semver
    local to = vim.deepcopy(semver)
    if mods == "" or mods == "=" then
      to.patch = to.patch + 1
    elseif mods == ">" then
      from.patch = from.patch + 1
      to = nil
    elseif mods == ">=" then
      to = nil
    elseif mods == "~" then
      if #parts >= 2 then
        to[2] = to[2] + 1
        to[3] = 0
      else
        to[1] = to[1] + 1
        to[2] = 0
        to[3] = 0
      end
    elseif mods == "^" then
      for i = 1, 3 do
        if to[i] ~= 0 then
          to[i] = to[i] + 1
          for j = i + 1, 3 do
            to[j] = 0
          end
          break
        end
      end
    end
    return setmetatable({ from = from, to = to }, { __index = Range })
  end
end

return M
```

## File: `lua/lazy/manage/task/fs.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.util")

---@type table<string, LazyTaskDef>
local M = {}

local function rm(dir)
  local stat = vim.uv.fs_lstat(dir)
  assert(stat and stat.type == "directory", dir .. " should be a directory!")
  Util.walk(dir, function(path, _, type)
    if type == "directory" then
      vim.uv.fs_rmdir(path)
    else
      vim.uv.fs_unlink(path)
    end
  end)
  vim.uv.fs_rmdir(dir)
end

M.clean = {
  skip = function(plugin)
    return plugin._.is_local
  end,
  ---@param opts? {rocks_only?:boolean}
  run = function(self, opts)
    opts = opts or {}
    local dir = self.plugin.dir:gsub("/+$", "")
    assert(dir:find(Config.options.root .. "/", 1, true) == 1, self.plugin.dir .. " should be under packpath!")

    local rock_root = Config.options.rocks.root .. "/" .. self.plugin.name
    if vim.uv.fs_stat(rock_root) then
      rm(rock_root)
    end

    if opts.rocks_only then
      return
    end

    rm(dir)

    self.plugin._.installed = false
  end,
}

return M
```

## File: `lua/lazy/manage/task/git.lua`
```
local Async = require("lazy.async")
local Config = require("lazy.core.config")
local Git = require("lazy.manage.git")
local Lock = require("lazy.manage.lock")
local Util = require("lazy.util")

local throttle = {}
throttle.running = 0
throttle.waiting = {} ---@type Async[]
throttle.timer = vim.uv.new_timer()

function throttle.next()
  throttle.running = 0
  while #throttle.waiting > 0 and throttle.running < Config.options.git.throttle.rate do
    ---@type Async
    local task = table.remove(throttle.waiting, 1)
    task:resume()
    throttle.running = throttle.running + 1
  end
  if throttle.running == 0 then
    throttle.timer:stop()
  end
end

function throttle.wait()
  if not Config.options.git.throttle.enabled then
    return
  end
  if not throttle.timer:is_active() then
    throttle.timer:start(0, Config.options.git.throttle.duration, vim.schedule_wrap(throttle.next))
  end
  local running = Async.running()
  if throttle.running < Config.options.git.throttle.rate then
    throttle.running = throttle.running + 1
  else
    table.insert(throttle.waiting, running)
    coroutine.yield("waiting")
    running:suspend()
    coroutine.yield("")
  end
end

---@param plugin LazyPlugin
local function cooldown(plugin)
  if not plugin._.last_check then
    return false
  end
  local delta = (vim.uv.now() - plugin._.last_check) / 1000
  return delta < Config.options.git.cooldown
end

---@type table<string, LazyTaskDef>
local M = {}

M.log = {
  ---@param opts {updated?:boolean, check?: boolean}
  skip = function(plugin, opts)
    if opts.check and plugin.pin then
      return true
    end
    if opts.updated and not (plugin._.updated and plugin._.updated.from ~= plugin._.updated.to) then
      return true
    end
    local stat = vim.uv.fs_stat(plugin.dir .. "/.git")
    return not (stat and stat.type == "directory")
  end,
  ---@async
  ---@param opts {args?: string[], updated?:boolean, check?:boolean}
  run = function(self, opts)
    -- self:spawn({ "sleep", "5" })
    local args = {
      "log",
      "--pretty=format:%h %s (%cr)",
      "--abbrev-commit",
      "--decorate",
      "--date=short",
      "--color=never",
      "--no-show-signature",
    }

    local info, target

    if opts.updated then
      table.insert(args, self.plugin._.updated.from .. ".." .. (self.plugin._.updated.to or "HEAD"))
    elseif opts.check then
      info = assert(Git.info(self.plugin.dir))
      target = assert(Git.get_target(self.plugin))
      if not target.commit then
        for k, v in pairs(target) do
          error(k .. " '" .. v .. "' not found")
        end
        error("no target commit found")
      end
      assert(target.commit, self.plugin.name .. " " .. target.branch)
      if not self.plugin._.is_local then
        if Git.eq(info, target) then
          if Config.options.checker.check_pinned then
            local last_commit = Git.get_commit(self.plugin.dir, target.branch, true)
            if not Git.eq(info, { commit = last_commit }) then
              self.plugin._.outdated = true
            end
          end
        else
          self.plugin._.updates = { from = info, to = target }
        end
      end
      table.insert(args, info.commit .. ".." .. target.commit)
    else
      vim.list_extend(args, opts.args or Config.options.git.log)
    end

    self:spawn("git", {
      args = args,
      cwd = self.plugin.dir,
    })

    -- for local plugins, mark as needing updates only if local is
    -- behind upstream, i.e. if git log gave no output
    if opts.check and self.plugin._.is_local then
      if not vim.tbl_isempty(self:get_log()) then
        self.plugin._.updates = { from = info, to = target }
      end
    end
  end,
}

M.clone = {
  skip = function(plugin)
    return plugin._.installed or plugin._.is_local
  end,
  ---@async
  run = function(self)
    throttle.wait()
    local args = {
      "clone",
      self.plugin.url,
    }

    if Config.options.git.filter then
      args[#args + 1] = "--filter=blob:none"
    end

    if self.plugin.submodules ~= false then
      args[#args + 1] = "--recurse-submodules"
    end

    args[#args + 1] = "--origin=origin"

    -- If git config --global core.autocrlf is true on a Unix/Linux system, then the git clone
    -- process will lead to files with CRLF endings. Vi / vim / neovim cannot handle this.
    -- Force git to clone with core.autocrlf=false.
    args[#args + 1] = "-c"
    args[#args + 1] = "core.autocrlf=false"

    args[#args + 1] = "--progress"

    if self.plugin.branch then
      vim.list_extend(args, { "-b", self.plugin.branch })
    end

    table.insert(args, self.plugin.dir)

    if vim.fn.isdirectory(self.plugin.dir) == 1 then
      require("lazy.manage.task.fs").clean.run(self, {})
    end

    local marker = self.plugin.dir .. ".cloning"
    Util.write_file(marker, "")

    self:spawn("git", {
      args = args,
      on_exit = function(ok)
        if ok then
          self.plugin._.cloned = true
          self.plugin._.installed = true
          self.plugin._.dirty = true
          vim.uv.fs_unlink(marker)
        end
      end,
    })
  end,
}

-- setup origin branches if needed
-- fetch will retrieve the data
M.branch = {
  skip = function(plugin)
    if not plugin._.installed or plugin._.is_local then
      return true
    end
    local branch = assert(Git.get_branch(plugin))
    return Git.get_commit(plugin.dir, branch, true)
  end,
  ---@async
  run = function(self)
    local args = {
      "remote",
      "set-branches",
      "--add",
      "origin",
      assert(Git.get_branch(self.plugin)),
    }

    self:spawn("git", {
      args = args,
      cwd = self.plugin.dir,
    })
  end,
}

-- check and switch origin
M.origin = {
  skip = function(plugin)
    if not plugin._.installed or plugin._.is_local then
      return true
    end
    local origin = Git.get_origin(plugin.dir)
    return origin == plugin.url
  end,
  ---@async
  ---@param opts {check?:boolean}
  run = function(self, opts)
    if opts.check then
      local origin = Git.get_origin(self.plugin.dir)
      self:error({
        "Origin has changed:",
        "  * old: " .. origin,
        "  * new: " .. self.plugin.url,
        "Please run update to fix",
      })
      return
    end
    require("lazy.manage.task.fs").clean.run(self, opts)
    M.clone.run(self, opts)
  end,
}

M.status = {
  skip = function(plugin)
    return not plugin._.installed or plugin._.is_local
  end,
  ---@async
  run = function(self)
    self:spawn("git", {
      args = { "ls-files", "-d", "-m" },
      cwd = self.plugin.dir,
      on_exit = function(ok, output)
        if ok then
          local lines = vim.split(output, "\n")
          ---@type string[]
          lines = vim.tbl_filter(function(line)
            -- Fix doc/tags being marked as modified
            if line:gsub("[\\/]", "/") == "doc/tags" then
              local Process = require("lazy.manage.process")
              Process.exec({ "git", "checkout", "--", "doc/tags" }, { cwd = self.plugin.dir })
              return false
            end
            return line ~= ""
          end, lines)
          if #lines > 0 then
            local msg = { "You have local changes in `" .. self.plugin.dir .. "`:" }
            for _, line in ipairs(lines) do
              msg[#msg + 1] = "  * " .. line
            end
            msg[#msg + 1] = "Please remove them to update."
            msg[#msg + 1] = "You can also press `x` to remove the plugin and then `I` to install it again."
            self:error(msg)
          end
        end
      end,
    })
  end,
}

-- fetches all needed origin branches
M.fetch = {
  skip = function(plugin)
    return not plugin._.installed or plugin._.is_local or cooldown(plugin)
  end,

  ---@async
  run = function(self)
    throttle.wait()
    local args = {
      "fetch",
      "--recurse-submodules",
      "--tags", -- also fetch remote tags
      "--force", -- overwrite existing tags if needed
      "--progress",
    }

    if self.plugin.submodules == false then
      table.remove(args, 2)
    end

    self:spawn("git", {
      args = args,
      cwd = self.plugin.dir,
      on_exit = function(ok)
        if ok then
          self.plugin._.last_check = vim.uv.now()
        end
      end,
    })
  end,
}

-- checkout to the target commit
-- branches will exists at this point, so so will the commit
M.checkout = {
  skip = function(plugin)
    return not plugin._.installed or plugin._.is_local
  end,

  ---@async
  ---@param opts {lockfile?:boolean}
  run = function(self, opts)
    throttle.wait()
    local info = assert(Git.info(self.plugin.dir))
    local target = assert(Git.get_target(self.plugin))

    -- if the plugin is pinned and we did not just clone it,
    -- then don't update
    if self.plugin.pin and not self.plugin._.cloned then
      target = info
    end

    local lock
    if opts.lockfile then
      -- restore to the lock if it exists
      lock = Lock.get(self.plugin)
      if lock then
        ---@diagnostic disable-next-line: cast-local-type
        target = lock
      end
    end

    -- don't run checkout if target is already reached.
    -- unless we just cloned, since then we won't have any data yet
    if Git.eq(info, target) and info.branch == target.branch then
      self.plugin._.updated = {
        from = info.commit,
        to = info.commit,
      }
      return
    end

    local args = {
      "checkout",
      "--progress",
      "--recurse-submodules",
    }

    if self.plugin.submodules == false then
      table.remove(args, 3)
    end

    if lock then
      table.insert(args, lock.commit)
    elseif target.tag then
      table.insert(args, "tags/" .. target.tag)
    elseif self.plugin.commit then
      table.insert(args, self.plugin.commit)
    else
      table.insert(args, target.commit)
    end

    self:spawn("git", {
      args = args,
      cwd = self.plugin.dir,
      on_exit = function(ok)
        if ok then
          local new_info = assert(Git.info(self.plugin.dir))
          if not self.plugin._.cloned then
            self.plugin._.updated = {
              from = info.commit,
              to = new_info.commit,
            }
            if self.plugin._.updated.from ~= self.plugin._.updated.to then
              self.plugin._.dirty = true
            end
          end
        end
      end,
    })
  end,
}
return M
```

## File: `lua/lazy/manage/task/init.lua`
```
local Async = require("lazy.async")
local Config = require("lazy.core.config")
local Process = require("lazy.manage.process")
local Terminal = require("lazy.terminal")

local colors = Config.options.headless.colors

---@class LazyTaskDef
---@field skip? fun(plugin:LazyPlugin, opts?:TaskOptions):any?
---@field run async fun(task:LazyTask, opts:TaskOptions)

---@alias LazyTaskFn async fun(task:LazyTask, opts:TaskOptions)

---@class LazyMsg
---@field msg string
---@field level? number

---@class LazyTask: Async
---@field plugin LazyPlugin
---@field name string
---@field private _log LazyMsg[]
---@field private _started number
---@field private _ended? number
---@field private _opts TaskOptions
---@field private _level number
local Task = setmetatable({}, { __index = Async.Async })

---@class TaskOptions: {[string]:any}
---@field on_done? fun(task:LazyTask)

---@param plugin LazyPlugin
---@param name string
---@param opts? TaskOptions
---@param task LazyTaskFn
function Task.new(plugin, name, task, opts)
  local self = setmetatable({}, { __index = Task })
  ---@async
  Task.init(self, function()
    self:_run(task)
  end)
  self:set_level()
  self._opts = opts or {}
  self._log = {}
  self.plugin = plugin
  self.name = name
  self._started = vim.uv.hrtime()
  ---@param other LazyTask
  plugin._.tasks = vim.tbl_filter(function(other)
    return other.name ~= name or other:running()
  end, plugin._.tasks or {})
  table.insert(plugin._.tasks, self)
  self:render()
  return self
end

---@param level? number
---@return LazyMsg[]
function Task:get_log(level)
  level = level or vim.log.levels.DEBUG
  return vim.tbl_filter(function(msg)
    return msg.level >= level
  end, self._log)
end

---@param level? number
function Task:output(level)
  return table.concat(
    ---@param m LazyMsg
    vim.tbl_map(function(m)
      return m.msg
    end, self:get_log(level)),
    "\n"
  )
end

function Task:status()
  local ret = self._log[#self._log]
  local msg = ret and vim.trim(ret.msg) or ""
  return msg ~= "" and msg or nil
end

function Task:has_errors()
  return self._level >= vim.log.levels.ERROR
end

function Task:has_warnings()
  return self._level >= vim.log.levels.WARN
end

---@param level? number
function Task:set_level(level)
  self._level = level or vim.log.levels.TRACE
end

---@async
---@param task LazyTaskFn
function Task:_run(task)
  if Config.headless() and Config.options.headless.task then
    self:log("Running task " .. self.name, vim.log.levels.INFO)
  end

  self
    :on("done", function()
      self:_done()
    end)
    :on("error", function(err)
      self:error(err)
    end)
    :on("yield", function(msg)
      self:log(msg)
    end)
  task(self, self._opts)
end

---@param msg string|string[]|LazyMsg
---@param level? number
function Task:log(msg, level)
  if type(msg) == "table" and msg.msg then
    level = msg.level or level
    msg = msg.msg
  end
  level = level or vim.log.levels.DEBUG
  self._level = math.max(self._level or 0, level or 0)
  msg = type(msg) == "table" and table.concat(msg, "\n") or msg
  ---@cast msg string
  table.insert(self._log, { msg = msg, level = level })
  self:render()
  if Config.headless() then
    self:headless()
  end
end

function Task:render()
  vim.schedule(function()
    vim.api.nvim_exec_autocmds("User", { pattern = "LazyRender", modeline = false })
  end)
end

function Task:headless()
  if not Config.options.headless.log then
    return
  end
  local msg = self._log[#self._log]
  if not msg or msg.level == vim.log.levels.TRACE then
    return
  end
  local map = {
    [vim.log.levels.ERROR] = Terminal.red,
    [vim.log.levels.WARN] = Terminal.yellow,
    [vim.log.levels.INFO] = Terminal.blue,
  }
  local color = Config.options.headless.colors and map[msg.level]
  io.write(Terminal.prefix(color and color(msg.msg) or msg.msg, self:prefix()))
  io.write("\n")
end

---@param msg string|string[]
function Task:error(msg)
  self:log(msg, vim.log.levels.ERROR)
end

---@param msg string|string[]
function Task:warn(msg)
  self:log(msg, vim.log.levels.WARN)
end

---@private
function Task:_done()
  if Config.headless() and Config.options.headless.task then
    local ms = math.floor(self:time() + 0.5)
    self:log("Finished task " .. self.name .. " in " .. ms .. "ms", vim.log.levels.INFO)
  end
  self._ended = vim.uv.hrtime()
  if self._opts.on_done then
    self._opts.on_done(self)
  end
  self:render()
  vim.schedule(function()
    vim.api.nvim_exec_autocmds("User", {
      pattern = "LazyPlugin" .. self.name:sub(1, 1):upper() .. self.name:sub(2),
      data = { plugin = self.plugin.name },
    })
  end)
end

function Task:time()
  return ((self._ended or vim.uv.hrtime()) - self._started) / 1e6
end

---@async
---@param cmd string
---@param opts? ProcessOpts
function Task:spawn(cmd, opts)
  opts = opts or {}
  local on_line = opts.on_line

  local headless = Config.headless() and Config.options.headless.process

  function opts.on_line(line)
    if not headless then
      return self:log(line, vim.log.levels.TRACE)
    end
    if on_line then
      pcall(on_line, line)
    end
  end

  if headless then
    opts.on_data = function(data)
      -- prefix with plugin name
      io.write(Terminal.prefix(data, self:prefix()))
    end
  end

  local proc = Process.spawn(cmd, opts)
  proc:wait()

  local ok = proc.code == 0 and proc.signal == 0
  if not headless then
    local msg = vim.trim(proc.data)
    if #msg > 0 then
      self:log(vim.trim(proc.data), ok and vim.log.levels.DEBUG or vim.log.levels.ERROR)
    end
  end

  if opts.on_exit then
    pcall(opts.on_exit, ok, proc.data)
  end
  return ok
end

function Task:prefix()
  local plugin = "[" .. self.plugin.name .. "] "
  local task = string.rep(" ", 20 - #(self.name .. self.plugin.name)) .. self.name

  return colors and Terminal.magenta(plugin) .. Terminal.cyan(task) .. Terminal.bright_black(" | ")
    or plugin .. " " .. task .. " | "
end

return Task
```

## File: `lua/lazy/manage/task/plugin.lua`
```
local Loader = require("lazy.core.loader")
local Rocks = require("lazy.pkg.rockspec")
local Util = require("lazy.util")

---@type table<string, LazyTaskDef>
local M = {}

---@param plugin LazyPlugin
local function get_build_file(plugin)
  for _, path in ipairs({ "build.lua", "build/init.lua" }) do
    if Util.file_exists(plugin.dir .. "/" .. path) then
      return path
    end
  end
end

local B = {}

---@param task LazyTask
---@param build string
function B.cmd(task, build)
  if task.plugin.build ~= "rockspec" then
    Loader.load(task.plugin, { task = "build" })
  end
  local cmd = vim.api.nvim_parse_cmd(build:sub(2), {}) --[[@as vim.api.keyset.cmd]]
  task:log(vim.api.nvim_cmd(cmd, { output = true }))
end

---@async
---@param task LazyTask
---@param build string
function B.shell(task, build)
  local shell = vim.env.SHELL or vim.o.shell
  local shell_args = shell:find("cmd.exe", 1, true) and "/c" or "-c"

  task:spawn(shell, {
    args = { shell_args, build },
    cwd = task.plugin.dir,
  })
end

M.build = {
  ---@param opts? {force:boolean}
  skip = function(plugin, opts)
    if opts and opts.force then
      return false
    end
    return not ((plugin._.dirty or plugin._.build) and (plugin.build or get_build_file(plugin)))
  end,
  ---@async
  run = function(self)
    vim.cmd([[silent! runtime plugin/rplugin.vim]])

    local builders = self.plugin.build

    -- Skip if `build` is set to `false`
    if builders == false then
      return
    end

    builders = builders or get_build_file(self.plugin)

    if builders then
      builders = type(builders) == "table" and builders or { builders }
      ---@cast builders (string|fun(LazyPlugin))[]
      for _, build in ipairs(builders) do
        if type(build) == "function" then
          build(self.plugin)
        elseif build == "rockspec" then
          Rocks.build(self)
        elseif build:sub(1, 1) == ":" then
          B.cmd(self, build)
        elseif build:match("%.lua$") then
          local file = self.plugin.dir .. "/" .. build
          local chunk, err = loadfile(file)
          if not chunk or err then
            error(err)
          end
          chunk()
        else
          B.shell(self, build)
        end
      end
    end
  end,
}

M.docs = {
  skip = function(plugin)
    return not plugin._.is_local and not plugin._.dirty
  end,
  run = function(self)
    local docs = self.plugin.dir .. "/doc"
    if Util.file_exists(docs) then
      self:log(vim.api.nvim_cmd({ cmd = "helptags", args = { docs } }, { output = true }))
    end
  end,
}

M.exists = {
  skip = function(plugin)
    return not plugin._.is_local or plugin.virtual
  end,
  run = function(self)
    if not Util.file_exists(self.plugin.dir) then
      self:error("Local plugin does not exist at `" .. self.plugin.dir .. "`")
    end
  end,
}

return M
```

## File: `lua/lazy/pkg/init.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.core.util")

local M = {}
M.VERSION = 12
M.dirty = false

---@class LazyPkg
---@field name string
---@field dir string
---@field source "lazy" | "packspec" | "rockspec"
---@field file string
---@field spec LazyPluginSpec

---@class LazyPkgSpec
---@field file string
---@field source? string
---@field spec? LazySpec
---@field code? string

---@class LazyPkgSource
---@field name string
---@field get fun(plugin:LazyPlugin):LazyPkgSpec?

---@class LazyPkgCache
---@field pkgs LazyPkg[]
---@field version number

---@type LazyPkg[]?
M.cache = nil

function M.update()
  ---@type LazyPkgSource[]
  local sources = {}
  for _, s in ipairs(Config.options.pkg.sources) do
    if s ~= "rockspec" or Config.options.rocks.enabled then
      sources[#sources + 1] = {
        name = s,
        get = require("lazy.pkg." .. s).get,
      }
    end
  end

  ---@type LazyPkgCache
  local ret = {
    version = M.VERSION,
    pkgs = {},
  }
  for _, plugin in pairs(Config.plugins) do
    if plugin._.installed then
      for _, source in ipairs(sources) do
        local spec = source.get(plugin)
        if spec then
          ---@type LazyPkg
          local pkg = {
            name = plugin.name,
            dir = plugin.dir,
            source = spec.source or source.name,
            file = spec.file,
            spec = spec.spec or {},
          }
          if type(spec.code) == "string" then
            pkg.spec = { _raw = spec.code }
          end
          table.insert(ret.pkgs, pkg)
          if not plugin._.pkg and plugin._.loaded and pkg.source == "rockspec" then
            require("lazy.core.loader").add_to_luapath(plugin)
          end
          break
        end
      end
    end
  end
  table.sort(ret.pkgs, function(a, b)
    return a.name < b.name
  end)
  local U = require("lazy.util")
  local code = "return " .. U.dump(ret)
  vim.fn.mkdir(vim.fn.fnamemodify(Config.options.pkg.cache, ":h"), "p")
  U.write_file(Config.options.pkg.cache, code)
  M.dirty = false
  M.cache = nil
end

local function _load()
  Util.track("pkg")
  M.cache = nil
  if vim.uv.fs_stat(Config.options.pkg.cache) then
    Util.try(function()
      local chunk, err = loadfile(Config.options.pkg.cache)
      if not chunk then
        error(err)
      end
      ---@type LazyPkgCache?
      local ret = chunk()
      if ret and ret.version == M.VERSION then
        M.cache = {}
        for _, pkg in ipairs(ret.pkgs) do
          if type(pkg.spec) == "function" then
            pkg.spec = pkg.spec()
          end
          -- wrap in the scope of the plugin
          pkg.spec = { pkg.name, specs = pkg.spec }
        end
        M.cache = ret.pkgs
      end
    end, "Error loading pkg:")
  end
  if rawget(M, "cache") then
    M.dirty = false
  else
    M.cache = {}
    M.dirty = true
  end
  Util.track()
end

---@param dir string
---@return LazyPkg?
---@overload fun():LazyPkg[]
function M.get(dir)
  if dir then
    for _, pkg in ipairs(M.cache) do
      if pkg.dir == dir then
        return pkg
      end
    end
    return
  end
  return M.cache
end

return setmetatable(M, {
  __index = function(_, key)
    if key == "cache" then
      _load()
      return M.cache
    end
  end,
})
```

## File: `lua/lazy/pkg/lazy.lua`
```
local Util = require("lazy.util")

local M = {}

M.lazy_file = "lazy.lua"

---@param plugin LazyPlugin
---@return LazyPkg?
function M.get(plugin)
  local file = Util.norm(plugin.dir .. "/" .. M.lazy_file)
  if Util.file_exists(file) then
    ---@type fun(): LazySpec
    local chunk = Util.try(function()
      local ret, err = loadfile(file)
      return err and error(err) or ret
    end, "`" .. M.lazy_file .. "` for **" .. plugin.name .. "** has errors:")
    if not chunk then
      Util.error("Invalid `" .. M.lazy_file .. "` for **" .. plugin.name .. "**")
      return
    end
    return {
      source = "lazy",
      file = M.lazy_file,
      code = "function()\n" .. Util.read_file(file) .. "\nend",
    }
  end
end

return M
```

## File: `lua/lazy/pkg/packspec.lua`
```
local Util = require("lazy.util")

---@class PackSpec
---@field dependencies? table<string, string>
---@field lazy? LazyPluginSpec
---
local M = {}

M.pkg_file = "pkg.json"

---@param plugin LazyPlugin
---@return LazyPkg?
function M.get(plugin)
  local file = Util.norm(plugin.dir .. "/" .. M.pkg_file)
  if not Util.file_exists(file) then
    return
  end
  ---@type PackSpec
  local pkg = Util.try(function()
    return vim.json.decode(Util.read_file(file))
  end, "`" .. M.pkg_file .. "` for **" .. plugin.name .. "** has errors:")

  if not pkg then
    return
  end

  ---@type LazySpec
  local ret = {}
  if pkg.dependencies then
    for url, version in pairs(pkg.dependencies) do
      -- HACK: Add `.git` to github urls
      if url:find("github") and not url:match("%.git$") then
        url = url .. ".git"
      end
      ret[#ret + 1] = { url = url, version = version }
    end
  end
  local p = pkg.lazy
  if p then
    p.url = p.url or plugin.url
    p.dir = p.dir or plugin.dir
    ret[#ret + 1] = p
  end
  if pkg.lazy then
    ret[#ret + 1] = pkg.lazy
  end
  return {
    source = "lazy",
    file = M.pkg_file,
    spec = ret,
  }
end

return M
```

## File: `lua/lazy/pkg/rockspec.lua`
```
--# selene:allow(incorrect_standard_library_use)
local Community = require("lazy.community")

local Config = require("lazy.core.config")
local Health = require("lazy.health")
local Util = require("lazy.util")

---@class RockSpec
---@field rockspec_format string
---@field package string
---@field version string
---@field dependencies string[]
---@field build? {type?: string, modules?: any[]}
---@field source? {url?: string}

---@class RockManifest
---@field repository table<string, table<string,any>>

local M = {}

M.skip = { "lua" }
M.rewrites = {
  ["plenary.nvim"] = { "nvim-lua/plenary.nvim", lazy = true },
}

M.python = { "python3", "python" }

---@class HereRocks
M.hererocks = {}

---@param task LazyTask
function M.hererocks.build(task)
  local root = Config.options.rocks.root .. "/hererocks"

  ---@param p string
  local python = vim.tbl_filter(function(p)
    return vim.fn.executable(p) == 1
  end, M.python)[1]

  task:spawn(python, {
    args = {
      "hererocks.py",
      "--verbose",
      "-l",
      "5.1",
      "-r",
      "latest",
      root,
    },
    cwd = task.plugin.dir,
  })
end

---@param bin string
function M.hererocks.bin(bin)
  local hererocks = Config.options.rocks.root .. "/hererocks/bin"
  return Util.norm(hererocks .. "/" .. bin)
end

-- check if hererocks is building
---@return boolean?
function M.hererocks.building()
  return vim.tbl_get(Config.plugins.hererocks or {}, "_", "build")
end

---@param opts? LazyHealth
function M.check(opts)
  opts = vim.tbl_extend("force", {
    error = Util.error,
    warn = Util.warn,
    ok = function() end,
  }, opts or {})

  local ok = false
  if Config.hererocks() then
    if M.hererocks.building() then
      ok = true
    else
      ok = Health.have(M.python, opts)
      ok = Health.have(M.hererocks.bin("luarocks")) and ok
      Health.have(
        M.hererocks.bin("lua"),
        vim.tbl_extend("force", opts, {
          version = "-v",
          version_pattern = "5.1",
        })
      )
    end
  else
    ok = Health.have("luarocks", opts)
    Health.have(
      { "lua5.1", "lua", "lua-5.1" },
      vim.tbl_extend("force", opts, {
        version = "-v",
        version_pattern = "5.1",
      })
    )
  end
  return ok
end

---@async
---@param task LazyTask
function M.build(task)
  M.check({
    error = function(msg)
      task:error(msg:gsub("[{}]", "`"))
    end,
    warn = function(msg)
      task:warn(msg)
    end,
    ok = function(msg) end,
  })

  if task:has_warnings() then
    task:log({
      "",
      "This plugin requires `luarocks`. Try one of the following:",
      " - fix your `luarocks` installation",
      Config.hererocks() and " - disable *hererocks* with `opts.rocks.hererocks = false`"
        or " - enable `hererocks` with `opts.rocks.hererocks = true`",
      " - disable `luarocks` support completely with `opts.rocks.enabled = false`",
    })
    task:warn("\nWill try building anyway, but will likely fail...")

    task:warn("\n" .. string.rep("-", 80) .. "\n")

    task:set_level(vim.log.levels.WARN)
  end

  if task.plugin.name == "hererocks" then
    return M.hererocks.build(task)
  end

  local env = {}
  local luarocks = "luarocks"
  if Config.hererocks() then
    -- hererocks is still building, so skip for now
    -- a new build will happen in the next round
    if M.hererocks.building() then
      return
    end

    local sep = Util.is_win and ";" or ":"
    local hererocks = Config.options.rocks.root .. "/hererocks/bin"
    if Util.is_win then
      hererocks = hererocks:gsub("/", "\\")
    end
    local path = vim.split(vim.env.PATH, sep)
    table.insert(path, 1, hererocks)
    env = {
      PATH = table.concat(path, sep),
    }
    if Util.is_win then
      luarocks = luarocks .. ".bat"
    end
  end

  local pkg = task.plugin._.pkg
  assert(pkg, "missing rockspec pkg for " .. task.plugin.name .. "\nThis shouldn't happen, please report.")

  local rockspec = M.rockspec(task.plugin.dir .. "/" .. pkg.file) or {}
  assert(
    rockspec.package,
    "missing rockspec package name for " .. task.plugin.name .. "\nThis shouldn't happen, please report."
  )

  local root = Config.options.rocks.root .. "/" .. task.plugin.name
  local ok = task:spawn(luarocks, {
    args = {
      "--tree",
      root,
      "--server",
      Config.options.rocks.server,
      "--lua-version",
      "5.1",
      "install", -- use install so that we can make use of pre-built rocks
      "--force-fast",
      "--deps-mode",
      "one",
      rockspec.package,
    },
    cwd = task.plugin.dir,
    env = env,
  })

  if ok then
    return
  end

  task:warn("Failed installing " .. rockspec.package .. " with `luarocks`.")
  task:warn("\n" .. string.rep("-", 80) .. "\n")
  task:warn("Trying to build from source.")

  -- install failed, so try building from source
  task:set_level() -- reset level
  ok = task:spawn(luarocks, {
    args = {
      "--tree",
      root,
      "--dev",
      "--lua-version",
      "5.1",
      "make",
      "--force-fast",
      "--deps-mode",
      "one",
    },
    cwd = task.plugin.dir,
    env = env,
  })
  if not ok then
    require("lazy.manage.task.fs").clean.run(task, { rocks_only = true })
  end
end

---@param rockspec RockSpec
function M.is_simple_build(rockspec)
  local type = vim.tbl_get(rockspec, "build", "type")
  return type == nil or type == "none" or (type == "builtin" and not rockspec.build.modules)
end

---@param file string
---@return table?
function M.parse(file)
  local ret = {}
  local ok = pcall(function()
    loadfile(file, nil, ret)()
  end) and ret or nil
  return ok and ret or nil
end

---@param plugin LazyPlugin
function M.deps(plugin)
  local root = Config.options.rocks.root .. "/" .. plugin.name
  ---@type RockManifest?
  local manifest = M.parse(root .. "/lib/luarocks/rocks-5.1/manifest")
  return manifest and vim.tbl_keys(manifest.repository or {})
end

---@param file string
---@return RockSpec?
function M.rockspec(file)
  return M.parse(file)
end

---@param plugin LazyPlugin
function M.find_rockspec(plugin)
  local rockspec_file ---@type string?
  Util.ls(plugin.dir, function(path, name, t)
    if t == "file" then
      for _, suffix in ipairs({ "scm", "git", "dev" }) do
        suffix = suffix .. "-1.rockspec"
        if name:sub(-#suffix) == suffix then
          rockspec_file = path
          return false
        end
      end
    end
  end)
  return rockspec_file
end

---@param plugin LazyPlugin
---@return LazyPkgSpec?
function M.get(plugin)
  if Community.get_spec(plugin.name) then
    return {
      file = "community",
      source = "lazy",
      spec = Community.get_spec(plugin.name),
    }
  end

  local rockspec_file = M.find_rockspec(plugin)
  local rockspec = rockspec_file and M.rockspec(rockspec_file)
  if not rockspec then
    return
  end

  local has_lua = not not vim.uv.fs_stat(plugin.dir .. "/lua")

  ---@type LazyPluginSpec
  local specs = {}

  ---@param dep string
  local rocks = vim.tbl_filter(function(dep)
    local name = dep:match("^%s*([^~><=%s]+)")
    if not name then
      return false
    end
    local url = Community.get_url(name)
    local spec = Community.get_spec(name)

    if spec then
      -- community spec
      table.insert(specs, spec)
      return false
    elseif url then
      -- Neovim plugin rock
      table.insert(specs, { url })
      return false
    end
    return not vim.tbl_contains(M.skip, name)
  end, rockspec.dependencies or {})

  local use =
    -- package without a /lua directory
    not has_lua
    -- has dependencies that are not skipped, 
    -- not in community specs, 
    -- and don't have a rockspec mapping
    or #rocks > 0
    -- has a complex build process
    or not M.is_simple_build(rockspec)

  if not use then
    -- community specs only
    return #specs > 0
        and {
          file = vim.fn.fnamemodify(rockspec_file, ":t"),
          spec = {
            plugin.name,
            specs = specs,
            build = false,
          },
        }
      or nil
  end

  local lazy = nil
  if not has_lua then
    lazy = false
  end

  return {
    file = vim.fn.fnamemodify(rockspec_file, ":t"),
    spec = {
      plugin.name,
      build = "rockspec",
      lazy = lazy,
    },
  }
end

return M
```

## File: `lua/lazy/view/colors.lua`
```
local M = {}

M.colors = {
  H1 = "IncSearch", -- home button
  H2 = "Bold", -- titles
  Comment = "Comment",
  Normal = "NormalFloat",
  Commit = "@variable.builtin", -- commit ref
  CommitIssue = "Number",
  CommitType = "Title", -- conventional commit type
  CommitScope = "Italic", -- conventional commit scope
  Dimmed = "Conceal", -- property
  Prop = "Conceal", -- property
  Value = "@string", -- value of a property
  NoCond = "DiagnosticWarn", -- unloaded icon for a plugin where `cond()` was false
  Local = "Constant",
  ProgressDone = "Constant", -- progress bar done
  ProgressTodo = "LineNr", -- progress bar todo
  Special = "@punctuation.special",
  ReasonRuntime = "@macro",
  ReasonPlugin = "Special",
  ReasonEvent = "Constant",
  ReasonKeys = "Statement",
  ReasonStart = "@variable.member",
  ReasonSource = "Character",
  ReasonFt = "Character",
  ReasonCmd = "Operator",
  ReasonImport = "Identifier",
  ReasonRequire = "@variable.parameter",
  Button = "CursorLine",
  ButtonActive = "Visual",
  TaskOutput = "MsgArea", -- task output
  Error = "DiagnosticError", -- task errors
  Warning = "DiagnosticWarn", -- task errors
  Info = "DiagnosticInfo", -- task errors
  Dir = "@markup.link", -- directory
  Url = "@markup.link", -- url
  Bold = { bold = true },
  Italic = { italic = true },
}

M.did_setup = false

function M.set_hl()
  for hl_group, link in pairs(M.colors) do
    local hl = type(link) == "table" and link or { link = link }
    hl.default = true
    vim.api.nvim_set_hl(0, "Lazy" .. hl_group, hl)
  end
end

function M.setup()
  if M.did_setup then
    return
  end

  M.did_setup = true

  M.set_hl()
  vim.api.nvim_create_autocmd("VimEnter", {
    callback = function()
      M.set_hl()
    end,
  })
  vim.api.nvim_create_autocmd("ColorScheme", {
    callback = function()
      M.set_hl()
    end,
  })
end

return M
```

## File: `lua/lazy/view/commands.lua`
```
local require = require("lazy.core.util").lazy_require
local Config = require("lazy.core.config")
local Manage = require("lazy.manage")
local Util = require("lazy.util")
local View = require("lazy.view")
local ViewConfig = require("lazy.view.config")

local M = {}

---@param cmd string
---@param opts? ManagerOpts
function M.cmd(cmd, opts)
  cmd = cmd == "" and "home" or cmd
  local command = M.commands[cmd] --[[@as fun(opts)]]
  if command == nil then
    Util.error("Invalid lazy command '" .. cmd .. "'")
  elseif
    ViewConfig.commands[cmd]
    and ViewConfig.commands[cmd].plugins_required
    and not (opts and vim.tbl_count(opts.plugins or {}) > 0)
  then
    return Util.error("`Lazy " .. cmd .. "` requires at least one plugin")
  else
    command(opts)
  end
end

---@class LazyCommands
M.commands = {
  clear = function()
    Manage.clear()
    View.show()
  end,
  health = function()
    vim.cmd.checkhealth("lazy")
  end,
  ---@param opts ManagerOpts
  pkg = function(opts)
    local Pkg = require("lazy.pkg")
    Pkg.update()
    require("lazy.manage.reloader").reload({
      {
        file = "pkg",
        what = "changed",
      },
    })
    for _, plugin in pairs(opts and opts.plugins or {}) do
      local spec = Pkg.get(plugin.dir)
      Util.info(vim.inspect(spec), { lang = "lua", title = plugin.name })
    end
  end,
  home = function()
    View.show("home")
  end,
  show = function()
    View.show("home")
  end,
  help = function()
    View.show("help")
  end,
  debug = function()
    View.show("debug")
  end,
  profile = function()
    View.show("profile")
  end,
  ---@param opts ManagerOpts
  load = function(opts)
    -- when a command is executed with a bang, wait will be set
    require("lazy.core.loader").load(opts.plugins, { cmd = "Lazy load" }, { force = opts.wait })
  end,
  reload = function(opts)
    for _, plugin in pairs(opts.plugins) do
      if type(plugin) == "string" then
        plugin = Config.plugins[plugin]
      end
      Util.warn("Reloading **" .. plugin.name .. "**")
      require("lazy.core.loader").reload(plugin)
    end
  end,
  log = Manage.log,
  build = Manage.build,
  clean = Manage.clean,
  install = Manage.install,
  sync = Manage.sync,
  update = Manage.update,
  check = Manage.check,
  restore = Manage.restore,
}

function M.complete(cmd, prefix)
  if not (ViewConfig.commands[cmd] or {}).plugins and cmd ~= "pkg" then
    return
  end
  ---@type string[]
  local plugins = {}
  if cmd == "load" then
    plugins[#plugins + 1] = "all"
  end
  for name, plugin in pairs(Config.plugins) do
    if cmd ~= "load" or not plugin._.loaded then
      plugins[#plugins + 1] = name
    end
  end
  table.sort(plugins)
  ---@param key string
  return vim.tbl_filter(function(key)
    return key:find(prefix, 1, true) == 1
  end, plugins)
end

function M.setup()
  vim.api.nvim_create_user_command("Lazy", function(cmd)
    ---@type ManagerOpts
    local opts = { wait = cmd.bang == true }
    local prefix, args = M.parse(cmd.args)
    if #args == 1 and args[1] == "all" then
      args = vim.tbl_keys(Config.plugins)
    end
    if #args > 0 then
      ---@param plugin string
      opts.plugins = vim.tbl_map(function(plugin)
        return Config.plugins[plugin]
      end, args)
    end
    M.cmd(prefix, opts)
  end, {
    bar = true,
    bang = true,
    nargs = "?",
    desc = "Lazy",
    complete = function(_, line)
      local prefix, args = M.parse(line)
      if #args > 0 then
        return M.complete(prefix, args[#args])
      end

      ---@param key string
      return vim.tbl_filter(function(key)
        return key:find(prefix, 1, true) == 1
      end, vim.tbl_keys(M.commands))
    end,
  })
end

---@return string, string[]
function M.parse(args)
  local parts = vim.split(vim.trim(args), "%s+")
  if vim.startswith("Lazy", parts[1]) then
    table.remove(parts, 1)
  end
  if args:sub(-1) == " " then
    parts[#parts + 1] = ""
  end
  return table.remove(parts, 1) or "", parts
end

return M
```

## File: `lua/lazy/view/config.lua`
```
local M = {}

---@class LazyViewCommand
---@field id number
---@field plugins? boolean
---@field plugins_required? boolean
---@field button? boolean
---@field desc? string
---@field desc_plugin? string
---@field key? string
---@field key_plugin? string
---@field toggle? boolean

function M.get_commands()
  ---@type (LazyViewCommand|{name:string})[]
  local ret = {}
  for k, v in pairs(M.commands) do
    v.name = k
    ret[#ret + 1] = v
  end
  table.sort(ret, function(a, b)
    return a.id < b.id
  end)
  return ret
end

M.dimmed_commits = { "bot", "build", "ci", "chore", "doc", "style", "test" }

M.keys = {
  hover = "K",
  diff = "d",
  close = "q",
  details = "<cr>",
  profile_sort = "<C-s>",
  profile_filter = "<C-f>",
  abort = "<C-c>",
  next = "]]",
  prev = "[[",
}

---@type table<string,LazyViewCommand>
M.commands = {
  home = {
    button = true,
    desc = "Go back to plugin list",
    id = 1,
    key = "H",
  },
  install = {
    button = true,
    desc = "Install missing plugins",
    desc_plugin = "Install a plugin",
    id = 2,
    key = "I",
    key_plugin = "i",
    plugins = true,
  },
  update = {
    button = true,
    desc = "Update plugins. This will also update the lockfile",
    desc_plugin = "Update a plugin. This will also update the lockfile",
    id = 3,
    key = "U",
    key_plugin = "u",
    plugins = true,
  },
  sync = {
    button = true,
    desc = "Run install, clean and update",
    desc_plugin = "Run install, clean and update",
    id = 4,
    key = "S",
    plugins = true,
  },
  clean = {
    button = true,
    desc = "Clean plugins that are no longer needed",
    desc_plugin = "Delete a plugin. WARNING: this will delete the plugin even if it should be installed!",
    id = 5,
    key = "X",
    key_plugin = "x",
    plugins = true,
  },
  check = {
    button = true,
    desc = "Check for updates and show the log (git fetch)",
    desc_plugin = "Check for updates and show the log (git fetch)",
    id = 6,
    key = "C",
    key_plugin = "c",
    plugins = true,
  },
  log = {
    button = true,
    desc = "Show recent updates",
    desc_plugin = "Show recent updates",
    id = 7,
    key = "L",
    key_plugin = "gl",
    plugins = true,
  },
  restore = {
    button = true,
    desc = "Updates all plugins to the state in the lockfile. For a single plugin: restore it to the state in the lockfile or to a given commit under the cursor",
    desc_plugin = "Restore a plugin to the state in the lockfile or to a given commit under the cursor",
    id = 8,
    key = "R",
    key_plugin = "r",
    plugins = true,
  },
  profile = {
    button = true,
    desc = "Show detailed profiling",
    id = 9,
    key = "P",
    toggle = true,
  },
  debug = {
    button = true,
    desc = "Show debug information",
    id = 10,
    key = "D",
    toggle = true,
  },
  help = {
    button = true,
    desc = "Toggle this help page",
    id = 11,
    key = "?",
    toggle = true,
  },
  clear = {
    desc = "Clear finished tasks",
    id = 12,
  },
  load = {
    desc = "Load a plugin that has not been loaded yet. Similar to `:packadd`. Like `:Lazy load foo.nvim`. Use `:Lazy! load` to skip `cond` checks.",
    id = 13,
    plugins = true,
    plugins_required = true,
  },
  health = {
    desc = "Run `:checkhealth lazy`",
    id = 14,
  },
  build = {
    desc = "Rebuild a plugin",
    id = 15,
    plugins = true,
    plugins_required = true,
    key_plugin = "gb",
  },
  reload = {
    desc = "Reload a plugin (experimental!!)",
    plugins = true,
    plugins_required = true,
    id = 16,
  },
}

return M
```

## File: `lua/lazy/view/diff.lua`
```
local Util = require("lazy.util")

local M = {}

---@alias LazyDiff {commit:string} | {from:string, to:string}
---@alias LazyDiffFun fun(plugin:LazyPlugin, diff:LazyDiff)

M.handlers = {

  ---@type LazyDiffFun
  browser = function(plugin, diff)
    if plugin.url then
      local url = plugin.url:gsub("%.git$", "")
      if diff.commit then
        Util.open(url .. "/commit/" .. diff.commit)
      else
        Util.open(url .. "/compare/" .. diff.from .. ".." .. diff.to)
      end
    else
      Util.error("No url for " .. plugin.name)
    end
  end,

  ---@type LazyDiffFun
  ["diffview.nvim"] = function(plugin, diff)
    local args
    if diff.commit then
      args = ("-C=%s"):format(plugin.dir) .. " " .. diff.commit .. "^!"
    else
      args = ("-C=%s"):format(plugin.dir) .. " " .. diff.from .. ".." .. diff.to
    end
    vim.cmd("DiffviewOpen " .. args)
  end,

  ---@type LazyDiffFun
  git = function(plugin, diff)
    local cmd = { "git" }
    if diff.commit then
      cmd[#cmd + 1] = "show"
      cmd[#cmd + 1] = diff.commit
    else
      cmd[#cmd + 1] = "diff"
      cmd[#cmd + 1] = diff.from
      cmd[#cmd + 1] = diff.to
    end
    Util.float_cmd(cmd, { cwd = plugin.dir, filetype = "git" })
  end,

  ---@type LazyDiffFun
  terminal_git = function(plugin, diff)
    local cmd = { "git" }
    if diff.commit then
      cmd[#cmd + 1] = "show"
      cmd[#cmd + 1] = diff.commit
    else
      cmd[#cmd + 1] = "diff"
      cmd[#cmd + 1] = diff.from
      cmd[#cmd + 1] = diff.to
    end
    Util.float_term(cmd, { cwd = plugin.dir, interactive = false, env = { PAGER = "cat" } })
  end,
}

return M
```

## File: `lua/lazy/view/float.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.util")
local ViewConfig = require("lazy.view.config")

---@class LazyFloatOptions
---@field buf? number
---@field file? string
---@field margin? {top?:number, right?:number, bottom?:number, left?:number}
---@field size? {width:number, height:number}
---@field zindex? number
---@field style? "" | "minimal"
---@field border? "none" | "single" | "double" | "rounded" | "solid" | "shadow"
---@field title? string
---@field title_pos? "center" | "left" | "right"
---@field persistent? boolean
---@field ft? string
---@field noautocmd? boolean
---@field backdrop? float

---@class LazyFloat
---@field buf number
---@field win number
---@field opts LazyFloatOptions
---@field win_opts LazyWinOpts
---@field backdrop_buf number
---@field backdrop_win number
---@field id number
---@overload fun(opts?:LazyFloatOptions):LazyFloat
local M = {}

setmetatable(M, {
  __call = function(_, ...)
    return M.new(...)
  end,
})

local _id = 0
local function next_id()
  _id = _id + 1
  return _id
end

---@param opts? LazyFloatOptions
function M.new(opts)
  local self = setmetatable({}, { __index = M })
  return self:init(opts)
end

---@param opts? LazyFloatOptions
function M:init(opts)
  require("lazy.view.colors").setup()
  self.id = next_id()
  self.opts = vim.tbl_deep_extend("force", {
    size = Config.options.ui.size,
    style = "minimal",
    border = Config.options.ui.border or "none",
    backdrop = Config.options.ui.backdrop or 60,
    zindex = 50,
  }, opts or {})

  ---@class LazyWinOpts
  ---@field width number
  ---@field height number
  ---@field row number
  ---@field col number
  self.win_opts = {
    relative = "editor",
    style = self.opts.style ~= "" and self.opts.style or nil,
    border = self.opts.border,
    zindex = self.opts.zindex,
    noautocmd = self.opts.noautocmd,
    title = self.opts.title,
    title_pos = self.opts.title and self.opts.title_pos or nil,
  }
  self:mount()
  self:on("VimEnter", function()
    vim.schedule(function()
      if not self:win_valid() then
        self:close()
      end
    end)
  end, { buffer = false })
  return self
end

function M:layout()
  local function size(max, value)
    return value > 1 and math.min(value, max) or math.floor(max * value)
  end
  self.win_opts.width = size(vim.o.columns, self.opts.size.width)
  self.win_opts.height = size(vim.o.lines, self.opts.size.height)
  self.win_opts.row = math.floor((vim.o.lines - self.win_opts.height) / 2)
  self.win_opts.col = math.floor((vim.o.columns - self.win_opts.width) / 2)

  if self.opts.border ~= "none" then
    self.win_opts.row = self.win_opts.row - 1
    self.win_opts.col = self.win_opts.col - 1
  end

  if self.opts.margin then
    if self.opts.margin.top then
      self.win_opts.height = self.win_opts.height - self.opts.margin.top
      self.win_opts.row = self.win_opts.row + self.opts.margin.top
    end
    if self.opts.margin.right then
      self.win_opts.width = self.win_opts.width - self.opts.margin.right
    end
    if self.opts.margin.bottom then
      self.win_opts.height = self.win_opts.height - self.opts.margin.bottom
    end
    if self.opts.margin.left then
      self.win_opts.width = self.win_opts.width - self.opts.margin.left
      self.win_opts.col = self.win_opts.col + self.opts.margin.left
    end
  end
end

function M:mount()
  if self:buf_valid() then
    -- keep existing buffer
    self.buf = self.buf
  elseif self.opts.file then
    self.buf = vim.fn.bufadd(self.opts.file)
    vim.bo[self.buf].readonly = true
    vim.bo[self.buf].swapfile = false
    vim.fn.bufload(self.buf)
    vim.bo[self.buf].modifiable = false
  elseif self.opts.buf then
    self.buf = self.opts.buf
  else
    self.buf = vim.api.nvim_create_buf(false, true)
  end

  local normal, has_bg
  if vim.fn.has("nvim-0.9.0") == 0 then
    normal = vim.api.nvim_get_hl_by_name("Normal", true)
    has_bg = normal and normal.background ~= nil
  else
    normal = vim.api.nvim_get_hl(0, { name = "Normal" })
    has_bg = normal and normal.bg ~= nil
  end

  if has_bg and self.opts.backdrop and self.opts.backdrop < 100 and vim.o.termguicolors then
    self.backdrop_buf = vim.api.nvim_create_buf(false, true)
    self.backdrop_win = vim.api.nvim_open_win(self.backdrop_buf, false, {
      relative = "editor",
      width = vim.o.columns,
      height = vim.o.lines,
      row = 0,
      col = 0,
      style = "minimal",
      focusable = false,
      zindex = self.opts.zindex - 1,
    })
    vim.api.nvim_set_hl(0, "LazyBackdrop", { bg = "#000000", default = true })
    Util.wo(self.backdrop_win, "winhighlight", "Normal:LazyBackdrop")
    Util.wo(self.backdrop_win, "winblend", self.opts.backdrop)
    vim.bo[self.backdrop_buf].buftype = "nofile"
    vim.bo[self.backdrop_buf].filetype = "lazy_backdrop"
  end

  self:layout()
  self.win = vim.api.nvim_open_win(self.buf, true, self.win_opts)
  self:on("WinClosed", function()
    self:close()
    self:augroup(true)
  end, { win = true })
  self:focus()
  self:on_key(ViewConfig.keys.close, self.close, "Close")
  self:on({ "BufDelete", "BufHidden" }, self.close)

  if vim.bo[self.buf].buftype == "" then
    vim.bo[self.buf].buftype = "nofile"
  end
  if vim.bo[self.buf].filetype == "" then
    vim.bo[self.buf].filetype = self.opts.ft or "lazy"
  end

  local function opts()
    vim.bo[self.buf].bufhidden = self.opts.persistent and "hide" or "wipe"
    Util.wo(self.win, "conceallevel", 3)
    Util.wo(self.win, "foldenable", false)
    Util.wo(self.win, "spell", false)
    Util.wo(self.win, "wrap", true)
    Util.wo(self.win, "winhighlight", "Normal:LazyNormal")
    Util.wo(self.win, "colorcolumn", "")
  end
  opts()

  vim.api.nvim_create_autocmd("VimResized", {
    callback = function()
      if not (self.win and vim.api.nvim_win_is_valid(self.win)) then
        return true
      end
      self:layout()
      local config = {}
      for _, key in ipairs({ "relative", "width", "height", "col", "row" }) do
        ---@diagnostic disable-next-line: no-unknown
        config[key] = self.win_opts[key]
      end
      config.style = self.opts.style ~= "" and self.opts.style or nil
      vim.api.nvim_win_set_config(self.win, config)

      if self.backdrop_win and vim.api.nvim_win_is_valid(self.backdrop_win) then
        vim.api.nvim_win_set_config(self.backdrop_win, {
          width = vim.o.columns,
          height = vim.o.lines,
        })
      end

      opts()
      vim.api.nvim_exec_autocmds("User", { pattern = "LazyFloatResized", modeline = false })
    end,
  })
end

---@param clear? boolean
function M:augroup(clear)
  return vim.api.nvim_create_augroup("trouble.window." .. self.id, { clear = clear == true })
end

---@param events string|string[]
---@param fn fun(self:LazyFloat, event:{buf:number}):boolean?
---@param opts? vim.api.keyset.create_autocmd | {buffer: false, win?:boolean}
function M:on(events, fn, opts)
  opts = opts or {}
  if opts.win then
    opts.pattern = self.win .. ""
    opts.win = nil
  elseif opts.buffer == nil then
    opts.buffer = self.buf
  elseif opts.buffer == false then
    opts.buffer = nil
  end
  if opts.pattern then
    opts.buffer = nil
  end
  local _self = Util.weak(self)
  opts.callback = function(e)
    local this = _self()
    if not this then
      -- delete the autocmd
      return true
    end
    return fn(this, e)
  end
  opts.group = self:augroup()
  vim.api.nvim_create_autocmd(events, opts)
end

---@param key string
---@param fn fun(self?)
---@param desc? string
---@param mode? string[]
function M:on_key(key, fn, desc, mode)
  vim.keymap.set(mode or "n", key, function()
    fn(self)
  end, {
    nowait = true,
    buffer = self.buf,
    desc = desc,
  })
end

---@param opts? {wipe:boolean}
function M:close(opts)
  self:augroup(true)
  local buf = self.buf
  local win = self.win
  local wipe = opts and opts.wipe
  if wipe == nil then
    wipe = not self.opts.persistent
  end

  self.win = nil
  if wipe then
    self.buf = nil
  end
  local backdrop_buf = self.backdrop_buf
  local backdrop_win = self.backdrop_win
  self.backdrop_buf = nil
  self.backdrop_win = nil

  vim.schedule(function()
    if backdrop_win and vim.api.nvim_win_is_valid(backdrop_win) then
      vim.api.nvim_win_close(backdrop_win, true)
    end
    if backdrop_buf and vim.api.nvim_buf_is_valid(backdrop_buf) then
      vim.api.nvim_buf_delete(backdrop_buf, { force = true })
    end
    if win and vim.api.nvim_win_is_valid(win) then
      vim.api.nvim_win_close(win, true)
    end
    if wipe and buf and vim.api.nvim_buf_is_valid(buf) then
      vim.diagnostic.reset(Config.ns, buf)
      vim.api.nvim_buf_delete(buf, { force = true })
    end
    vim.cmd.redraw()
  end)
end

function M:win_valid()
  return self.win and vim.api.nvim_win_is_valid(self.win)
end

function M:buf_valid()
  return self.buf and vim.api.nvim_buf_is_valid(self.buf)
end

function M:hide()
  if self:win_valid() then
    self:close({ wipe = false })
  end
end

function M:toggle()
  if self:win_valid() then
    self:hide()
    return false
  else
    self:show()
    return true
  end
end

function M:show()
  if self:win_valid() then
    self:focus()
  elseif self:buf_valid() then
    self:mount()
  else
    error("LazyFloat: buffer closed")
  end
end

function M:focus()
  vim.api.nvim_set_current_win(self.win)

  -- it seems that setting the current win doesn't work before VimEnter,
  -- so do that then
  if vim.v.vim_did_enter ~= 1 then
    vim.api.nvim_create_autocmd("VimEnter", {
      once = true,
      callback = function()
        if self.win and vim.api.nvim_win_is_valid(self.win) then
          pcall(vim.api.nvim_set_current_win, self.win)
        end
        return true
      end,
    })
  end
end

return M
```

## File: `lua/lazy/view/init.lua`
```
local Config = require("lazy.core.config")
local Diff = require("lazy.view.diff")
local Float = require("lazy.view.float")
local Git = require("lazy.manage.git")
local Render = require("lazy.view.render")
local Util = require("lazy.util")
local ViewConfig = require("lazy.view.config")

---@class LazyViewState
---@field mode string
---@field plugin? {name:string, kind?: LazyPluginKind}
local default_state = {
  mode = "home",
  profile = {
    threshold = 0,
    sort_time_taken = false,
  },
}

---@class LazyView: LazyFloat
---@field render LazyRender
---@field state LazyViewState
local M = {}

---@type LazyView
M.view = nil

function M.visible()
  return M.view and M.view.win and vim.api.nvim_win_is_valid(M.view.win)
end

---@param mode? string
function M.show(mode)
  if Config.headless() then
    return
  end

  M.view = M.visible() and M.view or M.create()
  if mode then
    M.view.state.mode = mode
  end
  M.view:update()
end

---@param plugin LazyPlugin
function M:is_selected(plugin)
  return vim.deep_equal(self.state.plugin, { name = plugin.name, kind = plugin._.kind })
end

function M.create()
  local self = setmetatable({}, { __index = setmetatable(M, { __index = Float }) })
  ---@cast self LazyView
  Float.init(self, {
    title = Config.options.ui.title,
    title_pos = Config.options.ui.title_pos,
    noautocmd = false,
  })

  if Config.options.ui.wrap then
    Util.wo(self.win, "wrap", true)
    Util.wo(self.win, "linebreak", true)
    Util.wo(self.win, "breakindent", true)
  else
    Util.wo(self.win, "wrap", false)
  end

  self.state = vim.deepcopy(default_state)

  self.render = Render.new(self)
  local update = self.update
  self.update = Util.throttle(Config.options.ui.throttle, function()
    update(self)
  end)

  for _, pattern in ipairs({ "LazyRender", "LazyFloatResized" }) do
    self:on({ "User" }, function()
      if not (self.buf and vim.api.nvim_buf_is_valid(self.buf)) then
        return true
      end
      self:update()
    end, { pattern = pattern })
  end

  vim.keymap.set("n", ViewConfig.keys.abort, function()
    require("lazy.manage.process").abort()
    require("lazy.async").abort()
    return ViewConfig.keys.abort
  end, { silent = true, buffer = self.buf, expr = true, desc = "Abort" })

  vim.keymap.set("n", "gx", "K", { buffer = self.buf, remap = true })

  -- plugin details
  self:on_key(ViewConfig.keys.details, function()
    local plugin = self.render:get_plugin()
    if plugin then
      local selected = {
        name = plugin.name,
        kind = plugin._.kind,
      }

      local open = not vim.deep_equal(self.state.plugin, selected)

      if not open then
        local row = self.render:get_row(selected)
        if row then
          vim.api.nvim_win_set_cursor(self.view.win, { row, 8 })
        end
      end

      self.state.plugin = open and selected or nil
      self:update()
    end
  end, "Details")

  self:on_key(ViewConfig.keys.next, function()
    local cursor = vim.api.nvim_win_get_cursor(self.view.win)
    for l = 1, #self.render.locations, 1 do
      local loc = self.render.locations[l]
      if loc.from > cursor[1] then
        vim.api.nvim_win_set_cursor(self.view.win, { loc.from, 8 })
        return
      end
    end
  end, "Next Plugin")

  self:on_key(ViewConfig.keys.prev, function()
    local cursor = vim.api.nvim_win_get_cursor(self.view.win)
    for l = #self.render.locations, 1, -1 do
      local loc = self.render.locations[l]
      if loc.from < cursor[1] then
        vim.api.nvim_win_set_cursor(self.view.win, { loc.from, 8 })
        return
      end
    end
  end, "Prev Plugin")

  self:on_key(ViewConfig.keys.profile_sort, function()
    if self.state.mode == "profile" then
      self.state.profile.sort_time_taken = not self.state.profile.sort_time_taken
      self:update()
    end
  end, "Sort Profile")

  self:on_key(ViewConfig.keys.profile_filter, function()
    if self.state.mode == "profile" then
      vim.ui.input({
        prompt = "Enter time threshold in ms: ",
        default = tostring(self.state.profile.threshold),
      }, function(input)
        if not input then
          return
        end
        local num = input == "" and 0 or tonumber(input)
        if not num then
          Util.error("Please input a number")
        else
          self.state.profile.threshold = num
          self:update()
        end
      end)
    end
  end, "Filter Profile")

  for lhs, rhs in pairs(Config.options.ui.custom_keys) do
    if rhs then
      local handler = type(rhs) == "table" and rhs[1] or rhs
      local desc = type(rhs) == "table" and rhs.desc or nil
      self:on_key(lhs, function()
        local plugin = self.render:get_plugin()
        if plugin then
          handler(plugin)
        end
      end, desc)
    end
  end

  self:setup_patterns()
  self:setup_modes()
  return self
end

function M:update()
  if self.buf and vim.api.nvim_buf_is_valid(self.buf) then
    self.render:update()
    vim.cmd.redraw()
  end
end

function M:open_url(path)
  local plugin = self.render:get_plugin()
  if plugin then
    if plugin.url then
      local url = plugin.url:gsub("%.git$", "")
      Util.open(url .. path)
    else
      Util.error("No url for " .. plugin.name)
    end
  end
end

function M:setup_patterns()
  local commit_pattern = "%f[%w](" .. string.rep("[a-f0-9]", 7) .. ")%f[%W]"
  self:on_pattern(ViewConfig.keys.hover, {
    [commit_pattern] = function(hash)
      self:diff({ commit = hash, browser = true })
    end,
    ["#(%d+)"] = function(issue)
      self:open_url("/issues/" .. issue)
    end,
    ["README.md"] = function()
      local plugin = self.render:get_plugin()
      if plugin then
        Util.open(plugin.dir .. "/README.md")
      end
    end,
    ["|(%S-)|"] = function(h)
      vim.cmd.help(h)
      self:close()
    end,
    ["(https?://%S+)"] = function(url)
      Util.open(url)
    end,
  }, self.hover, "Hover")
  self:on_pattern(ViewConfig.keys.diff, {
    [commit_pattern] = function(hash)
      self:diff({ commit = hash })
    end,
  }, self.diff, "Diff")
  self:on_pattern(ViewConfig.commands.restore.key_plugin, {
    [commit_pattern] = function(hash)
      self:restore({ commit = hash })
    end,
  }, self.restore, "Restore")
end

---@param opts? {commit:string}
function M:restore(opts)
  opts = opts or {}
  local Lockfile = require("lazy.manage.lock")
  local Commands = require("lazy.view.commands")
  local plugin = self.render:get_plugin()
  if plugin then
    if opts.commit then
      Lockfile.get(plugin).commit = opts.commit
    end
    Commands.cmd("restore", { plugins = { plugin } })
  end
end

function M:hover()
  if self:diff({ browser = true, hover = true }) then
    return
  end
  self:open_url("")
end

---@param opts? {commit?:string, browser:boolean, hover:boolean}
function M:diff(opts)
  opts = opts or {}
  local plugin = self.render:get_plugin()
  if plugin then
    local diff
    if opts.commit then
      diff = { commit = opts.commit }
    elseif plugin._.updated then
      diff = vim.deepcopy(plugin._.updated)
    else
      local info = assert(Git.info(plugin.dir))
      local target = assert(Git.get_target(plugin))
      diff = { from = info.commit, to = target.commit }
      if opts.hover and diff.from == diff.to then
        return
      end
    end

    if not diff then
      return
    end

    for k, v in pairs(diff) do
      diff[k] = v:sub(1, 7)
    end

    if opts.browser then
      Diff.handlers.browser(plugin, diff)
    else
      Diff.handlers[Config.options.diff.cmd](plugin, diff)
    end

    return true
  end
end

--- will create a key mapping that can be used on certain patterns
---@param key string
---@param patterns table<string, fun(str:string)>
---@param fallback? fun(self)
---@param desc? string
function M:on_pattern(key, patterns, fallback, desc)
  self:on_key(key, function()
    local line = vim.api.nvim_get_current_line()
    local pos = vim.api.nvim_win_get_cursor(0)
    local col = pos[2] + 1

    for pattern, handler in pairs(patterns) do
      local from = 1
      local to, url
      while from do
        from, to, url = line:find(pattern, from)
        if from and col >= from and col <= to then
          return handler(url)
        end
        if from then
          from = to + 1
        end
      end
    end
    if fallback then
      fallback(self)
    end
  end, desc)
end

function M:setup_modes()
  local Commands = require("lazy.view.commands")
  for name, m in pairs(ViewConfig.commands) do
    if m.key then
      self:on_key(m.key, function()
        if self.state.mode == name and m.toggle then
          self.state.mode = "home"
          return self:update()
        end
        Commands.cmd(name)
      end, m.desc)
    end
    if m.key_plugin and name ~= "restore" then
      self:on_key(m.key_plugin, function()
        local esc = vim.api.nvim_replace_termcodes("<esc>", true, true, true)
        vim.api.nvim_feedkeys(esc, "n", false)
        local plugins = {}
        if vim.api.nvim_get_mode().mode:lower() == "v" then
          local f, t = vim.fn.line("."), vim.fn.line("v")
          if f > t then
            f, t = t, f
          end
          for i = f, t do
            local plugin = self.render:get_plugin(i)
            if plugin then
              plugins[plugin.name] = plugin
            end
          end
          plugins = vim.tbl_values(plugins)
        else
          plugins[1] = self.render:get_plugin()
        end
        if #plugins > 0 then
          Commands.cmd(name, { plugins = plugins })
        end
      end, m.desc_plugin, { "n", "x" })
    end
  end
end

return M
```

## File: `lua/lazy/view/render.lua`
```
local Config = require("lazy.core.config")
local Git = require("lazy.manage.git")
local Handler = require("lazy.core.handler")
local Keys = require("lazy.core.handler.keys")
local Plugin = require("lazy.core.plugin")
local Sections = require("lazy.view.sections")
local Util = require("lazy.util")
local ViewConfig = require("lazy.view.config")

local Text = require("lazy.view.text")

---@alias LazyDiagnostic {row: number, severity: number, message:string}

---@class LazyRender:Text
---@field view LazyView
---@field plugins LazyPlugin[]
---@field progress {total:number, done:number}
---@field _diagnostics LazyDiagnostic[]
---@field locations {name:string, from: number, to: number, kind?: LazyPluginKind}[]
local M = {}

---@return LazyRender
---@param view LazyView
function M.new(view)
  ---@type LazyRender
  local self = setmetatable({}, { __index = setmetatable(M, { __index = Text }) })
  self.view = view
  self.padding = 2
  self.wrap = view.win_opts.width
  return self
end

function M:update()
  self._lines = {}
  self._diagnostics = {}
  self.locations = {}

  self.plugins = vim.tbl_values(Config.plugins)
  vim.list_extend(self.plugins, vim.tbl_values(Config.to_clean))
  vim.list_extend(self.plugins, vim.tbl_values(Config.spec.disabled))
  table.sort(self.plugins, function(a, b)
    return a.name < b.name
  end)

  self.progress = {
    total = 0,
    done = 0,
  }

  for _, plugin in ipairs(self.plugins) do
    if plugin._.tasks then
      for _, task in ipairs(plugin._.tasks) do
        self.progress.total = self.progress.total + 1
        if not task:running() then
          self.progress.done = self.progress.done + 1
        end
      end
    end
  end

  self:title()

  local mode = self.view.state.mode
  if mode == "help" then
    self:help()
  elseif mode == "profile" then
    self:profile()
  elseif mode == "debug" then
    self:debug()
  else
    for _, section in ipairs(Sections) do
      self:section(section)
    end
  end

  self:trim()

  vim.bo[self.view.buf].modifiable = true
  local view = vim.api.nvim_win_call(self.view.win, vim.fn.winsaveview)

  self:render(self.view.buf)

  vim.api.nvim_win_call(self.view.win, function()
    vim.fn.winrestview(view)
  end)
  vim.bo[self.view.buf].modifiable = false

  vim.diagnostic.set(
    Config.ns,
    self.view.buf,
    ---@param diag LazyDiagnostic
    vim.tbl_map(function(diag)
      diag.col = 0
      diag.lnum = diag.row - 1
      return diag
    end, self._diagnostics),
    { signs = false, virtual_text = true, underline = false, virtual_lines = false }
  )
end

---@param row? number
---@return LazyPlugin?
function M:get_plugin(row)
  if not (self.view.win and vim.api.nvim_win_is_valid(self.view.win)) then
    return
  end
  row = row or vim.api.nvim_win_get_cursor(self.view.win)[1]
  for _, loc in ipairs(self.locations) do
    if row >= loc.from and row <= loc.to then
      if loc.kind == "clean" then
        for _, plugin in ipairs(Config.to_clean) do
          if plugin.name == loc.name then
            return plugin
          end
        end
      elseif loc.kind == "disabled" then
        return Config.spec.disabled[loc.name]
      else
        return Config.plugins[loc.name]
      end
    end
  end
end

---@param selected {name:string, kind?: LazyPluginKind}
function M:get_row(selected)
  for _, loc in ipairs(self.locations) do
    if loc.kind == selected.kind and loc.name == selected.name then
      return loc.from
    end
  end
end

function M:title()
  self:nl()
  local modes = vim.tbl_filter(function(c)
    return c.button
  end, ViewConfig.get_commands())

  if Config.options.ui.pills then
    self:nl()
    for c, mode in ipairs(modes) do
      local title = " " .. mode.name:sub(1, 1):upper() .. mode.name:sub(2) .. " (" .. mode.key .. ") "
      if mode.name == "home" then
        if self.view.state.mode == "home" then
          title = " lazy.nvim " .. Config.options.ui.icons.lazy
        end
      end

      if self.view.state.mode == mode.name then
        if mode.name == "home" then
          self:append(title, "LazyH1", { wrap = true })
        else
          self:append(title, "LazyButtonActive", { wrap = true })
          self:highlight({ ["%(.%)"] = "LazySpecial" })
        end
      else
        self:append(title, "LazyButton", { wrap = true })
        self:highlight({ ["%(.%)"] = "LazySpecial" })
      end
      if c == #modes then
        break
      end
      self:append(" ")
    end
    self:nl()
  end
  if self.progress.done < self.progress.total then
    self:progressbar()
  end
  self:nl()

  if self.view.state.mode ~= "help" and self.view.state.mode ~= "profile" and self.view.state.mode ~= "debug" then
    if self.progress.done < self.progress.total then
      self:append("Tasks: ", "LazyH2")
      self:append(self.progress.done .. "/" .. self.progress.total, "LazyComment")
    else
      self:append("Total: ", "LazyH2")
      self:append(#self.plugins .. " plugins", "LazyComment")
    end
    self:nl():nl()
  end
end

function M:help()
  self:append("Help", "LazyH2"):nl():nl()

  self:append("Use "):append(ViewConfig.keys.abort, "LazySpecial"):append(" to abort all running tasks."):nl():nl()

  self:append("You can press "):append("<CR>", "LazySpecial"):append(" on a plugin to show its details."):nl():nl()

  self:append("Most properties can be hovered with ")
  self:append("<K>", "LazySpecial")
  self:append(" to open links, help files, readmes and git commits."):nl()
  self
    :append("When hovering with ")
    :append("<K>", "LazySpecial")
    :append(" on a plugin anywhere else, a diff will be opened if there are updates")
    :nl()
  self:append("or the plugin was just updated. Otherwise the plugin webpage will open."):nl():nl()

  self:append("Use "):append("<d>", "LazySpecial"):append(" on a commit or plugin to open the diff view"):nl():nl()
  self
    :append("Use ")
    :append("<]]>", "LazySpecial")
    :append(" and ")
    :append("<[[>", "LazySpecial")
    :append(" to navigate between plugins")
    :nl()
    :nl()
  self:nl()

  self:append("Keyboard Shortcuts", "LazyH2"):nl()
  for _, mode in ipairs(ViewConfig.get_commands()) do
    if mode.key then
      local title = mode.name:sub(1, 1):upper() .. mode.name:sub(2)
      self:append("- ", "LazySpecial", { indent = 2 })
      self:append(title, "Title")
      if mode.key then
        self:append(" <" .. mode.key .. ">", "LazyProp")
      end
      self:append(" " .. (mode.desc or "")):nl()
    end
  end

  self:nl():append("Keyboard Shortcuts for Plugins", "LazyH2"):nl()
  for _, mode in ipairs(ViewConfig.get_commands()) do
    if mode.key_plugin then
      local title = mode.name:sub(1, 1):upper() .. mode.name:sub(2)
      self:append("- ", "LazySpecial", { indent = 2 })
      self:append(title, "Title")
      if mode.key_plugin then
        self:append(" <" .. mode.key_plugin .. ">", "LazyProp")
      end
      self:append(" " .. (mode.desc_plugin or mode.desc)):nl()
    end
  end
  for lhs, rhs in pairs(Config.options.ui.custom_keys) do
    if type(rhs) == "table" and rhs.desc then
      self:append("- ", "LazySpecial", { indent = 2 })
      self:append("Custom key ", "Title")
      self:append(lhs, "LazyProp")
      self:append(" " .. rhs.desc):nl()
    end
  end
end

function M:progressbar()
  local width = vim.api.nvim_win_get_width(self.view.win) - 2 * self.padding
  local done = math.floor((self.progress.done / self.progress.total) * width + 0.5)
  if self.progress.done == self.progress.total then
    done = 0
  end
  self:append("", {
    virt_text_win_col = self.padding,
    virt_text = { { string.rep("─", done), "LazyProgressDone" } },
  })
  self:append("", {
    virt_text_win_col = done + self.padding,
    virt_text = { { string.rep("─", width - done), "LazyProgressTodo" } },
  })
end

---@param section LazySection
function M:section(section)
  ---@type LazyPlugin[]
  local section_plugins = {}
  ---@param plugin LazyPlugin
  self.plugins = vim.tbl_filter(function(plugin)
    if section.filter(plugin) then
      table.insert(section_plugins, plugin)
      return false
    end
    return true
  end, self.plugins)

  local count = #section_plugins
  table.sort(section_plugins, function(a, b)
    return a.name:lower() < b.name:lower()
  end)
  if count > 0 then
    self:append(section.title, "LazyH2"):append(" (" .. count .. ")", "LazyComment"):nl()
    for _, plugin in ipairs(section_plugins) do
      self:plugin(plugin)
    end
    self:nl()
  end
end

---@param diag LazyDiagnostic
function M:diagnostic(diag)
  diag.row = diag.row or self:row()
  diag.severity = diag.severity or vim.diagnostic.severity.INFO
  table.insert(self._diagnostics, diag)
end

---@param precision? number
function M:ms(nsec, precision)
  precision = precision or 2
  local e = math.pow(10, precision)
  return math.floor(nsec / 1e6 * e + 0.5) / e .. "ms"
end

---@param reason? {[string]:string, time:number}
---@param opts? {time_right?:boolean}
function M:reason(reason, opts)
  opts = opts or {}
  if not reason then
    return
  end
  reason = vim.deepcopy(reason)
  ---@type string?
  local source = reason.source
  if source then
    source = Util.norm(source)
    local plugin = Plugin.find(source)
    if plugin then
      reason.plugin = plugin.name
      reason.source = nil
    else
      local config = Util.norm(vim.fn.stdpath("config"))
      if source == config .. "/init.lua" then
        reason.source = "init.lua"
      else
        config = config .. "/lua"
        if source:find(config, 1, true) == 1 then
          reason.source = source:sub(#config + 2):gsub("/", "."):gsub("%.lua$", "")
        end
      end
    end
  end
  if reason.runtime then
    reason.runtime = Util.norm(reason.runtime)
    reason.runtime = reason.runtime:gsub(".*/([^/]+/plugin/.*)", "%1")
    reason.runtime = reason.runtime:gsub(".*/([^/]+/after/.*)", "%1")
    reason.runtime = reason.runtime:gsub(".*/([^/]+/ftdetect/.*)", "%1")
    reason.runtime = reason.runtime:gsub(".*/(runtime/.*)", "%1")
  end
  local time = reason.time and (" " .. self:ms(reason.time))
  if time and not opts.time_right then
    self:append(time, "Bold")
    self:append(" ")
  end
  -- self:append(" (", "Conceal")
  local first = true
  local keys = vim.tbl_keys(reason)
  table.sort(keys)
  if vim.tbl_contains(keys, "plugin") then
    keys = vim.tbl_filter(function(key)
      return key ~= "plugin"
    end, keys)
    table.insert(keys, "plugin")
  end
  for _, key in ipairs(keys) do
    local value = reason[key]
    local skip = type(key) == "number" or key == "time"
    if not skip then
      if first then
        first = false
      else
        self:append(" ")
      end
      local hl = "LazyReason" .. key:sub(1, 1):upper() .. key:sub(2)
      local icon = Config.options.ui.icons[key]
      if icon then
        icon = icon:gsub("%s*$", "")
        self:append(icon .. " ", hl)
        self:append(value, hl)
      else
        self:append(key .. " ", hl)
        self:append(value, hl)
      end
    end
  end
  if time and opts.time_right then
    self:append(time, "Bold")
  end
end

---@param plugin LazyPlugin
function M:diagnostics(plugin)
  local skip = false
  for _, task in ipairs(plugin._.tasks or {}) do
    if task:running() then
      self:diagnostic({
        severity = vim.diagnostic.severity.WARN,
        message = task.name .. (task:status() and (": " .. task:status()) or ""),
      })
      skip = true
    elseif task:has_errors() then
      self:diagnostic({
        message = task.name .. " failed",
        severity = vim.diagnostic.severity.ERROR,
      })
      skip = true
    elseif task:has_warnings() then
      self:diagnostic({
        message = task.name .. " warning",
        severity = vim.diagnostic.severity.WARN,
      })
      skip = true
    end
  end
  if skip then
    return
  end
  if plugin._.build then
    self:diagnostic({
      message = "needs build",
      severity = vim.diagnostic.severity.WARN,
    })
  elseif plugin._.updated then
    if plugin._.updated.from == plugin._.updated.to then
      self:diagnostic({
        message = "already up to date",
      })
    else
      local version = Git.info(plugin.dir, true).version
      if version then
        self:diagnostic({
          message = "updated to " .. tostring(version),
        })
      else
        self:diagnostic({
          message = "updated from " .. plugin._.updated.from:sub(1, 7) .. " to " .. plugin._.updated.to:sub(1, 7),
        })
      end
    end
  elseif plugin._.updates then
    local version = plugin._.updates.to.version
    if version then
      self:diagnostic({
        message = "version " .. tostring(version) .. " is available",
      })
    else
      self:diagnostic({
        message = "updates available",
      })
    end
  end
end

---@param plugin LazyPlugin
function M:plugin(plugin)
  local hl = plugin._.is_local and "LazyLocal" or "LazySpecial"
  if plugin._.loaded then
    self:append("  " .. Config.options.ui.icons.loaded .. " ", hl):append(plugin.name)
  elseif plugin._.cond == false then
    self:append("  " .. Config.options.ui.icons.not_loaded .. " ", "LazyNoCond"):append(plugin.name)
  else
    self:append("  " .. Config.options.ui.icons.not_loaded .. " ", hl):append(plugin.name)
  end
  local plugin_start = self:row()
  if plugin._.loaded then
    -- When the plugin is loaded, only show the loading reason
    self:reason(plugin._.loaded)
  else
    -- otherwise show all lazy handlers
    self:append(" ")
    self:handlers(plugin)
    for _, other in pairs(Config.plugins) do
      if vim.tbl_contains(other.dependencies or {}, plugin.name) then
        self:reason({ plugin = other.name })
        self:append(" ")
      end
    end
  end
  self:diagnostics(plugin)
  self:nl()

  if self.view:is_selected(plugin) then
    self:details(plugin)
  end
  self:tasks(plugin)
  self.locations[#self.locations + 1] =
    { name = plugin.name, from = plugin_start, to = self:row() - 1, kind = plugin._.kind }
end

---@param str string
---@param hl? string|Extmark
---@param opts? {indent?: number, prefix?: string, wrap?: boolean}
function M:markdown(str, hl, opts)
  local lines = vim.split(str, "\n")
  for _, line in ipairs(lines) do
    self:append(line, hl, opts):highlight({
      ["`.-`"] = "@markup.raw.markdown_inline",
      ["%*.-%*"] = "LazyItalic",
      ["%*%*.-%*%*"] = "LazyBold",
      ["^%s*-"] = "Special",
    })
    self:nl()
  end
end

---@param plugin LazyPlugin
function M:tasks(plugin)
  for _, task in ipairs(plugin._.tasks or {}) do
    if self.view:is_selected(plugin) then
      self:append(Config.options.ui.icons.task .. "[task] ", "Title", { indent = 4 }):append(task.name)
      self:append(" " .. math.floor((task:time()) * 100) / 100 .. "ms", "Bold")
      self:nl()
    end

    if not task:has_warnings() and task.name == "log" then
      self:log(task)
    else
      local hls = {
        [vim.log.levels.ERROR] = "LazyError",
        [vim.log.levels.WARN] = "LazyWarning",
        [vim.log.levels.INFO] = "LazyInfo",
      }
      for _, msg in ipairs(task:get_log()) do
        if task:has_warnings() or self.view:is_selected(plugin) then
          self:markdown(msg.msg, hls[msg.level] or "LazyTaskOutput", { indent = 6 })
        end
      end
    end
  end
end

---@param task LazyTask
function M:log(task)
  local log = vim.trim(task:output())
  if log ~= "" then
    local lines = vim.split(log, "\n")
    for _, line in ipairs(lines) do
      local ref, msg, time = line:match("^(%w+) (.*) (%(.*%))$")
      if msg then
        if msg:find("^%S+!:") then
          self:diagnostic({ message = "Breaking Changes", severity = vim.diagnostic.severity.WARN })
        end
        self:append(ref:sub(1, 7) .. " ", "LazyCommit", { indent = 6 })

        local dimmed = false
        for _, dim in ipairs(ViewConfig.dimmed_commits) do
          if msg:find("^" .. dim) then
            dimmed = true
          end
        end
        self:append(vim.trim(msg), dimmed and "LazyDimmed" or nil):highlight({
          ["#%d+"] = "LazyCommitIssue",
          ["^%S+:"] = dimmed and "Bold" or "LazyCommitType",
          ["^%S+(%(.*%))!?:"] = "LazyCommitScope",
          ["`.-`"] = "@markup.raw.markdown_inline",
          ["%*.-%*"] = "Italic",
          ["%*%*.-%*%*"] = "Bold",
        })
        self:append(" " .. time, "LazyComment")
        self:nl()
        -- else
        --   self:append(line, "LazyTaskOutput", { indent = 6 }):nl()
      end
    end
    self:nl()
  end
end

---@param plugin LazyPlugin
function M:details(plugin)
  ---@type string[][]
  local props = {}
  table.insert(props, { "dir", plugin.dir, "LazyDir" })
  if plugin.url then
    table.insert(props, { "url", (plugin.url:gsub("%.git$", "")), "LazyUrl" })
  end
  local git = Git.info(plugin.dir, true)
  if git then
    git.branch = git.branch or Git.get_branch(plugin)
    if git.version then
      table.insert(props, { "version", tostring(git.version) })
    end
    if git.tag then
      table.insert(props, { "tag", git.tag })
    end
    if git.branch then
      table.insert(props, { "branch", git.branch })
    end
    if git.commit then
      table.insert(props, { "commit", git.commit:sub(1, 7), "LazyCommit" })
    end
  end
  local rocks = require("lazy.pkg.rockspec").deps(plugin)
  if rocks then
    table.insert(props, { "rocks", vim.inspect(rocks) })
  end

  if Util.file_exists(plugin.dir .. "/README.md") then
    table.insert(props, { "readme", "README.md" })
  end
  Util.ls(plugin.dir .. "/doc", function(path, name)
    if name:sub(-3) == "txt" then
      local data = Util.read_file(path)
      local tag = data:match("%*(%S-)%*")
      if tag then
        table.insert(props, { "help", "|" .. tag .. "|" })
      end
    end
  end)

  for handler in pairs(plugin._.handlers or {}) do
    table.insert(props, {
      handler,
      function()
        self:handlers(plugin, handler)
      end,
    })
  end
  self:props(props, { indent = 6 })

  self:nl()
end

---@param plugin LazyPlugin
---@param types? LazyHandlerTypes[]|LazyHandlerTypes
function M:handlers(plugin, types)
  if not plugin._.handlers then
    return
  end
  types = type(types) == "string" and { types } or types
  types = types and types or vim.tbl_keys(Handler.types)
  for _, t in ipairs(types) do
    for id, value in pairs(plugin._.handlers[t] or {}) do
      value = t == "keys" and Keys.to_string(value) or id
      self:reason({ [t] = value })
      self:append(" ")
    end
  end
end

---@alias LazyProps {[1]:string, [2]:string|fun(), [3]?:string}[]
---@param props LazyProps
---@param opts? {indent: number}
function M:props(props, opts)
  opts = opts or {}
  local width = 0
  for _, prop in ipairs(props) do
    width = math.max(width, #prop[1])
  end
  for _, prop in ipairs(props) do
    self:append(prop[1] .. string.rep(" ", width - #prop[1] + 1), "LazyProp", { indent = opts.indent or 0 })
    if type(prop[2]) == "function" then
      prop[2]()
    else
      self:append(tostring(prop[2]), prop[3] or "LazyValue")
    end
    self:nl()
  end
end

function M:profile()
  local stats = require("lazy.stats").stats()
  local ms = (math.floor(stats.startuptime * 100 + 0.5) / 100)
  self:append("Startuptime: ", "LazyH2"):append(ms .. "ms", "Number"):nl():nl()
  if stats.real_cputime then
    self:append("Based on the actual CPU time of the Neovim process till "):append("UIEnter", "LazySpecial")
    self:append("."):nl()
    self:append("This is more accurate than ")
    self:append("`nvim --startuptime`", "@markup.raw.markdown_inline")
    self:append(".")
  else
    self:append("An accurate startuptime based on the actual CPU time of the Neovim process is not available."):nl()
    self
      :append("Startuptime is instead based on a delta with a timestamp when lazy started till ")
      :append("UIEnter", "LazySpecial")
    self:append(".")
  end
  self:nl()

  local times = {}
  for event, time in pairs(require("lazy.stats").stats().times) do
    times[#times + 1] = { event, self:ms(time * 1e6), "Bold", time = time }
  end
  table.sort(times, function(a, b)
    return a.time < b.time
  end)
  for p, prop in ipairs(times) do
    if p > 1 then
      prop[2] = prop[2] .. " (+" .. self:ms((prop.time - times[p - 1].time) * 1e6) .. ")"
    end
  end
  self:props(times, { indent = 2 })

  self:nl()

  self:append("Profile", "LazyH2"):nl():nl()
  self
    :append("You can press ")
    :append(ViewConfig.keys.profile_sort, "LazySpecial")
    :append(" to change sorting between chronological order & time taken.")
    :nl()
  self
    :append("Press ")
    :append(ViewConfig.keys.profile_filter, "LazySpecial")
    :append(" to filter profiling entries that took more time than a given threshold")
    :nl()

  self:nl()

  ---@param a LazyProfile
  ---@param b LazyProfile
  local function sort(a, b)
    return a.time > b.time
  end

  ---@param entry LazyProfile
  local function get_children(entry)
    ---@type LazyProfile[]
    local children = entry

    if self.view.state.profile.sort_time_taken then
      children = {}
      for _, child in ipairs(entry) do
        children[#children + 1] = child
      end
      table.sort(children, sort)
    end
    return children
  end

  ---@param entry LazyProfile
  local function _profile(entry, depth)
    if entry.time / 1e6 < self.view.state.profile.threshold then
      return
    end
    local data = type(entry.data) == "string" and { source = entry.data } or entry.data
    data.time = entry.time
    local symbol = M.list_icon(depth)
    self:append(("  "):rep(depth)):append(symbol, "LazySpecial"):append(" ")
    self:reason(data, { time_right = true })
    self:nl()
    for _, child in ipairs(get_children(entry)) do
      _profile(child, depth + 1)
    end
  end

  for _, entry in ipairs(get_children(Util._profiles[1])) do
    _profile(entry, 1)
  end
end

function M.list_icon(depth)
  local symbols = Config.options.ui.icons.list
  return symbols[(depth - 1) % #symbols + 1]
end

function M:debug()
  self:append("Active Handlers", "LazyH2"):nl()
  self
    :append(
      "This shows only the lazy handlers that are still active. When a plugin loads, its handlers are removed",
      "LazyComment",
      { indent = 2 }
    )
    :nl()

  Util.foreach(require("lazy.core.handler").handlers, function(handler_type, handler)
    Util.foreach(handler.active, function(value, plugins)
      if not vim.tbl_isempty(plugins) then
        ---@type string[]
        plugins = vim.tbl_values(plugins)
        table.sort(plugins)
        self:append(Config.options.ui.icons.debug, "LazySpecial", { indent = 2 })
        if handler_type == "keys" then
          for k, v in pairs(Config.plugins[plugins[1]]._.handlers.keys) do
            if k == value then
              value = Keys.to_string(v)
              break
            end
          end
        end
        self:reason({ [handler_type] = value })
        for _, plugin in pairs(plugins) do
          self:append(" ")
          self:reason({ plugin = plugin })
        end
        self:nl()
      end
    end)
  end)
  self:nl()

  Util.foreach(require("lazy.core.cache")._inspect(), function(name, stats)
    self:append(name, "LazyH2"):nl()
    local props = {
      { "total", stats.total or 0, "Number" },
      { "time", self:ms(stats.time or 0, 3), "Bold" },
      { "avg time", self:ms((stats.time or 0) / (stats.total or 0), 3), "Bold" },
    }
    for k, v in pairs(stats) do
      if k ~= "total" and k ~= "time" then
        props[#props + 1] = { k, v, "Number" }
      end
    end
    self:props(props, { indent = 2 })
    self:nl()
  end)
end

return M
```

## File: `lua/lazy/view/sections.lua`
```
---@param plugin LazyPlugin
---@param filter fun(task:LazyTask):boolean?
local function has_task(plugin, filter)
  if plugin._.tasks then
    for _, task in ipairs(plugin._.tasks) do
      if filter(task) then
        return true
      end
    end
  end
end

---@alias LazySection {title:string, filter:fun(plugin:LazyPlugin):boolean?}

---@type LazySection[]
return {
  {
    filter = function(plugin)
      return has_task(plugin, function(task)
        return task:has_errors()
      end)
    end,
    title = "Failed",
  },
  {
    filter = function(plugin)
      if plugin._.working then
        return true
      end
      return has_task(plugin, function(task)
        return task:running()
      end)
    end,
    title = "Working",
  },
  {
    filter = function(plugin)
      return plugin._.build
    end,
    title = "Build",
  },
  {
    filter = function(plugin)
      return has_task(plugin, function(task)
        if task.name ~= "log" then
          return
        end
        for _, line in ipairs(vim.split(task:output(), "\n")) do
          if line:find("^%w+ %S+!:") then
            return true
          end
        end
      end)
    end,
    title = "Breaking Changes",
  },
  {
    filter = function(plugin)
      return plugin._.updated and plugin._.updated.from ~= plugin._.updated.to
    end,
    title = "Updated",
  },
  {
    filter = function(plugin)
      return plugin._.cloned
    end,
    title = "Installed",
  },
  {
    ---@param plugin LazyPlugin
    filter = function(plugin)
      return plugin._.updates ~= nil
    end,
    title = "Updates",
  },
  {
    filter = function(plugin)
      return has_task(plugin, function(task)
        return task.name == "log" and vim.trim(task:output()) ~= ""
      end)
    end,
    title = "Log",
  },
  {
    filter = function(plugin)
      return plugin._.kind == "clean" and plugin._.installed
    end,
    title = "Clean",
  },
  {
    filter = function(plugin)
      return not plugin._.installed and plugin._.kind ~= "disabled"
    end,
    title = "Not Installed",
  },
  {
    filter = function(plugin)
      return plugin._.outdated
    end,
    title = "Outdated",
  },
  {
    filter = function(plugin)
      return plugin._.loaded ~= nil
    end,
    title = "Loaded",
  },
  {
    filter = function(plugin)
      return plugin._.installed
    end,
    title = "Not Loaded",
  },
  {
    filter = function(plugin)
      return plugin._.kind == "disabled"
    end,
    title = "Disabled",
  },
}
```

## File: `lua/lazy/view/text.lua`
```
local Config = require("lazy.core.config")
local Util = require("lazy.util")

---@alias TextSegment {str: string, hl?:string|Extmark}
---@alias Extmark {hl_group?:string, col?:number, end_col?:number}

---@class Text
---@field _lines TextSegment[][]
---@field padding number
---@field wrap number
local Text = {}

function Text.new()
  local self = setmetatable({}, { __index = Text })
  self._lines = {}

  return self
end

---@param str string
---@param hl? string|Extmark
---@param opts? {indent?: number, prefix?: string, wrap?: boolean}
function Text:append(str, hl, opts)
  opts = opts or {}
  if #self._lines == 0 then
    self:nl()
  end

  local lines = vim.split(str, "\n")
  for l, line in ipairs(lines) do
    if opts.prefix then
      line = opts.prefix .. line
    end
    if opts.indent then
      line = string.rep(" ", opts.indent) .. line
    end
    if l > 1 then
      self:nl()
    end
    if
      Config.options.ui.wrap
      and opts.wrap
      and str ~= ""
      and self:col() > 0
      and self:col() + vim.fn.strwidth(line) + self.padding > self.wrap
    then
      self:nl()
    end
    table.insert(self._lines[#self._lines], {
      str = line,
      hl = hl,
    })
  end

  return self
end

function Text:nl()
  table.insert(self._lines, {})
  return self
end

function Text:render(buf)
  local lines = {}

  for _, line in ipairs(self._lines) do
    local str = (" "):rep(self.padding)
    local has_extmark = false

    for _, segment in ipairs(line) do
      str = str .. segment.str
      if type(segment.hl) == "table" then
        has_extmark = true
      end
    end

    if str:match("^%s*$") and not has_extmark then
      str = ""
    end
    table.insert(lines, str)
  end

  vim.api.nvim_buf_set_lines(buf, 0, -1, false, lines)
  vim.api.nvim_buf_clear_namespace(buf, Config.ns, 0, -1)

  for l, line in ipairs(self._lines) do
    if lines[l] ~= "" then
      local col = self.padding

      for _, segment in ipairs(line) do
        local width = vim.fn.strlen(segment.str)

        local extmark = segment.hl
        if extmark then
          if type(extmark) == "string" then
            extmark = { hl_group = extmark, end_col = col + width }
          end
          ---@cast extmark Extmark

          local extmark_col = extmark.col or col
          extmark.col = nil
          local ok, err = pcall(vim.api.nvim_buf_set_extmark, buf, Config.ns, l - 1, extmark_col, extmark)
          if not ok then
            Util.error(
              "Failed to set extmark. Please report a bug with this info:\n"
                .. vim.inspect({ segment = segment, line = line, error = err })
            )
          end
        end

        col = col + width
      end
    end
  end
end

---@param patterns table<string,string>
function Text:highlight(patterns)
  local col = self.padding
  local last = self._lines[#self._lines]
  ---@type TextSegment?
  local text
  for s, segment in ipairs(last) do
    if s == #last then
      text = segment
      break
    end
    col = col + vim.fn.strlen(segment.str)
  end
  if text then
    for pattern, hl in pairs(patterns) do
      local from, to, match = text.str:find(pattern)
      while from do
        if match then
          from, to = text.str:find(match, from, true)
        end
        self:append("", {
          col = col + from - 1,
          end_col = col + to,
          hl_group = hl,
        })
        from, to = text.str:find(pattern, to + 1)
      end
    end
  end
end

function Text:trim()
  while #self._lines > 0 and #self._lines[#self._lines] == 0 do
    table.remove(self._lines)
  end
end

function Text:row()
  return #self._lines == 0 and 1 or #self._lines
end

function Text:col()
  if #self._lines == 0 then
    return 0
  end
  local width = 0
  for _, segment in ipairs(self._lines[#self._lines]) do
    width = width + vim.fn.strlen(segment.str)
  end
  return width
end

return Text
```

## File: `scripts/test`
```
#!/usr/bin/env bash

nvim -l tests/minit.lua --minitest "$@"
```

## File: `tests/helpers.lua`
```
local Util = require("lazy.util")

local M = {}

M.fs_root = vim.fn.fnamemodify("./.tests/fs", ":p")

function M.path(path)
  return Util.norm(M.fs_root .. "/" .. path)
end

---@param files string[]
function M.fs_create(files)
  ---@type string[]
  local ret = {}

  for _, file in ipairs(files) do
    ret[#ret + 1] = Util.norm(M.fs_root .. "/" .. file)
    local parent = vim.fn.fnamemodify(ret[#ret], ":h:p")
    vim.fn.mkdir(parent, "p")
    Util.write_file(ret[#ret], "")
  end
  return ret
end

function M.fs_rm(dir)
  dir = Util.norm(M.fs_root .. "/" .. dir)
  Util.walk(dir, function(path, _, type)
    if type == "directory" then
      vim.uv.fs_rmdir(path)
    else
      vim.uv.fs_unlink(path)
    end
  end)
  vim.uv.fs_rmdir(dir)
end

return M
```

## File: `tests/minit.lua`
```
#!/usr/bin/env -S nvim -l

vim.env.LAZY_STDPATH = ".tests"

vim.opt.rtp:prepend(".")

-- Setup lazy.nvim
require("lazy.minit").setup({
  spec = {
    { dir = vim.uv.cwd() },
  },
})
```

## File: `tests/core/init_spec.lua`
```
local Util = require("lazy.core.util")

describe("init", function()
  it("has correct environment for tests", function()
    for _, name in ipairs({ "config", "data", "cache", "state" }) do
      local path = Util.norm(vim.fn.stdpath(name) --[[@as string]])
      assert(path:find(".tests/" .. name, 1, true), path .. " not in .tests")
    end
  end)
end)
```

## File: `tests/core/plugin_spec.lua`
```
local Config = require("lazy.core.config")
local Handler = require("lazy.core.handler")
local Plugin = require("lazy.core.plugin")

local function inspect(obj)
  return vim.inspect(obj):gsub("%s+", " ")
end

---@param plugin LazyPlugin
local function resolve(plugin)
  local meta = getmetatable(plugin)
  local ret = meta and type(meta.__index) == "table" and resolve(meta.__index) or {}
  for k, v in pairs(plugin) do
    ret[k] = v
  end
  return ret
end

---@param plugins LazyPlugin[]
local function clean(plugins)
  return vim.tbl_map(function(plugin)
    plugin = resolve(plugin)
    plugin[1] = nil
    plugin._.frags = nil
    if plugin._.dep == false then
      plugin._.dep = nil
    end
    plugin._.top = nil
    return plugin
  end, plugins)
end

describe("plugin spec url/name", function()
  local tests = {
    { { dir = "~/foo" }, { name = "foo", dir = vim.fn.fnamemodify("~/foo", ":p") } },
    { { dir = "/tmp/foo" }, { dir = "/tmp/foo", name = "foo" } },
    { { "foo/bar" }, { [1] = "foo/bar", name = "bar", url = "https://github.com/foo/bar.git" } },
    { { "https://foo.bar" }, { [1] = "https://foo.bar", name = "foo.bar", url = "https://foo.bar" } },
    { { "foo/bar", name = "foobar" }, { [1] = "foo/bar", name = "foobar", url = "https://github.com/foo/bar.git" } },
    { { "foo/bar", url = "123" }, { [1] = "foo/bar", name = "bar", url = "123" } },
    { { url = "https://foobar" }, { name = "foobar", url = "https://foobar" } },
    {
      { { url = "https://foo", name = "foobar" }, { url = "https://foo" } },
      { name = "foobar", url = "https://foo" },
    },
    {
      { { url = "https://foo" }, { url = "https://foo", name = "foobar" } },
      { name = "foobar", url = "https://foo" },
    },
    { { url = "ssh://foobar" }, { name = "foobar", url = "ssh://foobar" } },
    { "foo/bar", { [1] = "foo/bar", name = "bar", url = "https://github.com/foo/bar.git" } },
    { { { { "foo/bar" } } }, { [1] = "foo/bar", name = "bar", url = "https://github.com/foo/bar.git" } },
  }

  for _, test in ipairs(tests) do
    test[2]._ = {}
    it("parses " .. inspect(test[1]), function()
      if not test[2].dir then
        test[2].dir = Config.options.root .. "/" .. test[2].name
      end
      local spec = Plugin.Spec.new(test[1])
      local all = vim.deepcopy(spec.plugins)
      local plugins = vim.tbl_values(all)
      plugins = vim.tbl_map(function(plugin)
        plugin._ = {}
        return plugin
      end, plugins)
      local notifs = vim.tbl_filter(function(notif)
        return notif.level > 3
      end, spec.notifs)
      assert(#notifs == 0, vim.inspect(spec.notifs))
      assert.equal(1, #plugins, vim.inspect(all))
      plugins[1]._.super = nil
      assert.same(test[2], plugins[1])
    end)
  end
end)

describe("plugin spec dir", function()
  local tests = {
    {
      "~/projects/gitsigns.nvim",
      { "lewis6991/gitsigns.nvim", opts = {}, dev = true },
      { "lewis6991/gitsigns.nvim" },
    },
    {
      "~/projects/gitsigns.nvim",
      { "lewis6991/gitsigns.nvim", opts = {}, dev = true },
      { "gitsigns.nvim" },
    },
    {
      "~/projects/gitsigns.nvim",
      { "lewis6991/gitsigns.nvim", opts = {} },
      { "lewis6991/gitsigns.nvim", dev = true },
    },
    {
      "~/projects/gitsigns.nvim",
      { "lewis6991/gitsigns.nvim", opts = {} },
      { "gitsigns.nvim", dev = true },
    },
  }

  for _, test in ipairs(tests) do
    local dir = vim.fn.expand(test[1])
    local input = vim.list_slice(test, 2)
    it("parses dir " .. inspect(input), function()
      local spec = Plugin.Spec.new(input)
      local plugins = vim.tbl_values(spec.plugins)
      assert(spec:report() == 0)
      assert.equal(1, #plugins)
      assert.same(dir, plugins[1].dir)
    end)
  end
end)

describe("plugin dev", function()
  local tests = {
    {
      { "lewis6991/gitsigns.nvim", opts = {}, dev = true },
      { "lewis6991/gitsigns.nvim" },
    },
    {
      { "lewis6991/gitsigns.nvim", opts = {}, dev = true },
      { "gitsigns.nvim" },
    },
    {
      { "lewis6991/gitsigns.nvim", opts = {} },
      { "lewis6991/gitsigns.nvim", dev = true },
    },
    {
      { "lewis6991/gitsigns.nvim", opts = {} },
      { "gitsigns.nvim", dev = true },
    },
  }

  for _, test in ipairs(tests) do
    local dir = vim.fn.expand("~/projects/gitsigns.nvim")
    local input = test
    it("parses dir " .. inspect(input), function()
      local spec = Plugin.Spec.new(input)
      local plugins = vim.tbl_values(spec.plugins)
      assert(spec:report() == 0)
      assert.equal(1, #plugins)
      assert.same(dir, plugins[1].dir)
    end)
  end
end)

describe("plugin spec opt", function()
  it("handles dependencies", function()
    Config.options.defaults.lazy = false
    local tests = {
      { "foo/bar", dependencies = { "foo/dep1", "foo/dep2" } },
      { "foo/bar", dependencies = { { "foo/dep1" }, "foo/dep2" } },
      { { { "foo/bar", dependencies = { { "foo/dep1" }, "foo/dep2" } } } },
    }
    for _, test in ipairs(tests) do
      local spec = Plugin.Spec.new(vim.deepcopy(test))
      assert(#spec.notifs == 0)
      Config.plugins = spec.plugins
      Config.spec = spec
      Plugin.update_state()
      assert(vim.tbl_count(spec.plugins) == 3)
      assert(#spec.plugins.bar.dependencies == 2)
      assert(spec.plugins.bar._.dep ~= true)
      assert(spec.plugins.bar.lazy == false)
      assert(spec.plugins.dep1._.dep == true)
      assert(spec.plugins.dep1.lazy == true)
      assert(spec.plugins.dep2._.dep == true)
      assert(spec.plugins.dep2.lazy == true)
      spec = Plugin.Spec.new(test)
      for _, plugin in pairs(spec.plugins) do
        plugin.dir = nil
      end
      assert.same({
        bar = {
          _ = {},
          dependencies = { "dep1", "dep2" },
          name = "bar",
          url = "https://github.com/foo/bar.git",
        },
        dep1 = {
          _ = {
            dep = true,
          },
          name = "dep1",
          url = "https://github.com/foo/dep1.git",
        },
        dep2 = {
          _ = {
            dep = true,
          },
          name = "dep2",
          url = "https://github.com/foo/dep2.git",
        },
      }, clean(spec.plugins))
    end
  end)

  describe("deps", function()
    before_each(function()
      Handler.init()
    end)
    Config.options.defaults.lazy = false
    local tests = {
      { { "foo/bar", dependencies = { { "dep1" }, "foo/dep2" } }, "foo/dep1" },
      { "foo/dep1", { "foo/bar", dependencies = { { "dep1" }, "foo/dep2" } } },
    }
    for _, test in ipairs(tests) do
      it("handles dep names " .. inspect(test), function()
        local spec = Plugin.Spec.new(vim.deepcopy(test))
        assert(#spec.notifs == 0)
        Config.plugins = spec.plugins
        Plugin.update_state()
        spec = Plugin.Spec.new(test)
        for _, plugin in pairs(spec.plugins) do
          plugin.dir = nil
        end
        assert.same({
          bar = {
            _ = {},
            dependencies = { "dep1", "dep2" },
            name = "bar",
            url = "https://github.com/foo/bar.git",
          },
          dep1 = {
            _ = {},
            name = "dep1",
            url = "https://github.com/foo/dep1.git",
          },
          dep2 = {
            _ = {
              dep = true,
            },
            name = "dep2",
            url = "https://github.com/foo/dep2.git",
          },
        }, clean(spec.plugins))
      end)
    end

    Config.options.defaults.lazy = false
    local tests = {
      {
        { "foo/baz", name = "bar" },
        { "foo/fee", dependencies = { "foo/baz" } },
      },
      {
        { "foo/fee", dependencies = { "foo/baz" } },
        { "foo/baz", name = "bar" },
      },
      -- {
      --   { "foo/baz", name = "bar" },
      --   { "foo/fee", dependencies = { "baz" } },
      -- },
      {
        { "foo/baz", name = "bar" },
        { "foo/fee", dependencies = { "bar" } },
      },
    }
    for _, test in ipairs(tests) do
      it("handles dep names " .. inspect(test), function()
        local spec = Plugin.Spec.new(vim.deepcopy(test))
        assert(#spec.notifs == 0)
        Config.plugins = spec.plugins
        Plugin.update_state()
        spec = Plugin.Spec.new(test)
        spec.meta:rebuild()
        for _, plugin in pairs(spec.plugins) do
          plugin.dir = nil
        end
        assert.same({
          bar = {
            _ = {},
            name = "bar",
            url = "https://github.com/foo/baz.git",
          },
          fee = {
            _ = {},
            name = "fee",
            url = "https://github.com/foo/fee.git",
            dependencies = { "bar" },
          },
        }, clean(spec.plugins))
      end)
    end

    it("handles opt from dep", function()
      Config.options.defaults.lazy = false
      local spec = Plugin.Spec.new({ "foo/dep1", { "foo/bar", dependencies = { "foo/dep1", "foo/dep2" } } })
      assert(#spec.notifs == 0)
      Config.plugins = spec.plugins
      Plugin.update_state()
      assert.same(3, vim.tbl_count(spec.plugins))
      assert(spec.plugins.bar._.dep ~= true)
      assert(spec.plugins.bar.lazy == false)
      assert(spec.plugins.dep2._.dep == true)
      assert(spec.plugins.dep2.lazy == true)
      assert(spec.plugins.dep1._.dep ~= true)
      assert(spec.plugins.dep1.lazy == false)
    end)

    it("handles defaults opt", function()
      do
        Config.options.defaults.lazy = true
        local spec = Plugin.Spec.new({ "foo/bar" })
        assert(#spec.notifs == 0)
        Config.plugins = spec.plugins
        Plugin.update_state()
        assert(spec.plugins.bar.lazy == true)
      end
      do
        Config.options.defaults.lazy = false
        local spec = Plugin.Spec.new({ "foo/bar" })
        Config.plugins = spec.plugins
        Plugin.update_state()
        assert(spec.plugins.bar.lazy == false)
      end
    end)

    it("handles opt from dep", function()
      Config.options.defaults.lazy = false
      local spec = Plugin.Spec.new({ "foo/bar", event = "foo" })
      assert(#spec.notifs == 0)
      Config.plugins = spec.plugins
      Plugin.update_state()
      assert.same(1, vim.tbl_count(spec.plugins))
      assert(spec.plugins.bar._.dep ~= true)
      assert(spec.plugins.bar.lazy == true)
    end)

    it("merges lazy loaders", function()
      local tests = {
        { { "foo/bar", event = "mod1" }, { "foo/bar", event = "mod2" } },
        { { "foo/bar", event = { "mod1" } }, { "foo/bar", event = { "mod2" } } },
        { { "foo/bar", event = "mod1" }, { "foo/bar", event = { "mod2" } } },
      }
      for _, test in ipairs(tests) do
        local spec = Plugin.Spec.new(test)
        assert(#spec.notifs == 0)
        assert(vim.tbl_count(spec.plugins) == 1)
        Handler.resolve(spec.plugins.bar)
        -- vim.print(spec.plugins.bar._.handlers)
        local events = vim.tbl_keys(spec.plugins.bar._.handlers.event or {})
        assert(type(events) == "table")
        assert(#events == 2)
        assert(vim.tbl_contains(events, "mod1"))
        assert(vim.tbl_contains(events, "mod2"))
      end
    end)
  end)

  it("handles opt from dep", function()
    Config.options.defaults.lazy = false
    local spec = Plugin.Spec.new({ "foo/dep1", { "foo/bar", dependencies = { "foo/dep1", "foo/dep2" } } })
    assert(#spec.notifs == 0)
    Config.plugins = spec.plugins
    Plugin.update_state()
    assert.same(3, vim.tbl_count(spec.plugins))
    assert(spec.plugins.bar._.dep ~= true)
    assert(spec.plugins.bar.lazy == false)
    assert(spec.plugins.dep2._.dep == true)
    assert(spec.plugins.dep2.lazy == true)
    assert(spec.plugins.dep1._.dep ~= true)
    assert(spec.plugins.dep1.lazy == false)
  end)

  it("handles defaults opt", function()
    do
      Config.options.defaults.lazy = true
      local spec = Plugin.Spec.new({ "foo/bar" })
      assert(#spec.notifs == 0)
      Config.plugins = spec.plugins
      Plugin.update_state()
      assert(spec.plugins.bar.lazy == true)
    end
    do
      Config.options.defaults.lazy = false
      local spec = Plugin.Spec.new({ "foo/bar" })
      Config.plugins = spec.plugins
      Plugin.update_state()
      assert(spec.plugins.bar.lazy == false)
    end
  end)

  it("handles opt from dep", function()
    Config.options.defaults.lazy = false
    local spec = Plugin.Spec.new({ "foo/bar", event = "foo" })
    assert(#spec.notifs == 0)
    Config.plugins = spec.plugins
    Plugin.update_state()
    assert.same(1, vim.tbl_count(spec.plugins))
    assert(spec.plugins.bar._.dep ~= true)
    assert(spec.plugins.bar.lazy == true)
  end)

  it("merges lazy loaders", function()
    local tests = {
      { { "foo/bar", event = "mod1" }, { "foo/bar", event = "mod2" } },
      { { "foo/bar", event = { "mod1" } }, { "foo/bar", event = { "mod2" } } },
      { { "foo/bar", event = "mod1" }, { "foo/bar", event = { "mod2" } } },
    }
    for _, test in ipairs(tests) do
      Handler.init()
      local spec = Plugin.Spec.new(test)
      assert(#spec.notifs == 0)
      assert(vim.tbl_count(spec.plugins) == 1)
      Handler.resolve(spec.plugins.bar)
      local events = spec.plugins.bar._.handlers.event
      assert(type(events) == "table")
      assert(vim.tbl_count(events) == 2)
      assert(events["mod1"])
      assert(events["mod2"])
    end
  end)

  it("handles disabled", function()
    local tests = {
      [{ { "foo/bar" }, { "foo/bar", enabled = false } }] = false,
      [{ { "foo/bar", enabled = false }, { "foo/bar" } }] = false,
      [{ { "foo/bar", enabled = false }, { "foo/bar", enabled = true } }] = true,
      [{ { "foo/bar" }, { "foo/bar", enabled = true } }] = true,
    }
    for test, ret in pairs(tests) do
      local spec = Plugin.Spec.new(test)
      assert(#spec.notifs == 0)
      if ret then
        assert(spec.plugins.bar)
        assert(not spec.disabled.bar)
      else
        assert(not spec.plugins.bar)
        assert(spec.disabled.bar)
      end
    end
  end)

  it("handles the optional keyword", function()
    local tests = {
      [{ { "foo/bax" }, { "foo/bar", optional = true, dependencies = "foo/dep1" } }] = false,
      [{ { "foo/bax", dependencies = "foo/dep1" }, { "foo/bar", optional = true, dependencies = "foo/dep1" } }] = true,
    }
    for test, ret in pairs(tests) do
      local spec = Plugin.Spec.new(test)
      assert(#spec.notifs == 0)
      assert(spec.plugins.bax)
      assert(not spec.plugins.bar)
      assert(#spec.disabled == 0)
      if ret then
        assert(spec.plugins.dep1)
      else
        assert(not spec.plugins.opt1)
      end
    end
  end)
end)

describe("plugin opts", function()
  ---@type {spec:LazySpec, opts:table}[]
  local tests = {
    {
      spec = { { "foo/foo", opts = { a = 1, b = 1 } }, { "foo/foo", opts = { a = 2 } } },
      opts = { a = 2, b = 1 },
    },
    {
      spec = { { "foo/foo", config = { a = 1, b = 1 } }, { "foo/foo", opts = { a = 2 } } },
      opts = { a = 2, b = 1 },
    },
    {
      spec = { { "foo/foo", opts = { a = 1, b = 1 } }, { "foo/foo", config = { a = 2 } } },
      opts = { a = 2, b = 1 },
    },
    {
      spec = { { "foo/foo", config = { a = 1, b = 1 } }, { "foo/foo", config = { a = 2 } } },
      opts = { a = 2, b = 1 },
    },
    {
      spec = { { "foo/foo", config = { a = 1, b = 1 } }, { "foo/foo", config = { a = vim.NIL } } },
      opts = { b = 1 },
    },
    {
      spec = { { "foo/foo", config = { a = 1, b = 1 } }, { "foo/foo" } },
      opts = { a = 1, b = 1 },
    },
    {
      spec = { { "foo/foo" }, { "foo/foo" } },
      opts = {},
    },
  }

  for _, test in ipairs(tests) do
    it("correctly parses opts for " .. inspect(test.spec), function()
      local spec = Plugin.Spec.new(test.spec)
      assert(spec.plugins.foo)
      assert.same(test.opts, Plugin.values(spec.plugins.foo, "opts"))
    end)
  end
end)

describe("plugin spec", function()
  it("only includes fragments from enabled plugins", function()
    local tests = {
      {
        spec = {
          { "foo/disabled", enabled = false, dependencies = { "foo/bar", opts = { key_disabled = true } } },
          { "foo/disabled", dependencies = { "foo/bar", opts = { key_disabled_two = true } } },
          { "foo/conditional", cond = false, dependencies = { "foo/bar", opts = { key_cond = true } } },
          { "foo/optional", optional = true, dependencies = { "foo/bar", opts = { key_optional = true } } },
          { "foo/active", dependencies = { "foo/bar", opts = { key_active = true } } },
          {
            "foo/bar",
            opts = { key = true },
          },
        },
        expected_opts = { key = true, key_active = true },
      }, -- for now, one test...
    }
    for _, test in ipairs(tests) do
      local spec = Plugin.Spec.new(test.spec)
      assert(#spec.notifs == 0)
      assert(vim.tbl_count(spec.plugins) == 2)
      assert(spec.plugins.active)
      assert(spec.plugins.bar)
      assert.same(test.expected_opts, Plugin.values(spec.plugins.bar, "opts"))
    end
  end)
end)
```

## File: `tests/core/util_spec.lua`
```
local Cache = require("lazy.core.cache")
local Helpers = require("tests.helpers")
local Util = require("lazy.util")

describe("util", function()
  local rtp = vim.opt.rtp:get()
  before_each(function()
    ---@type vim.Option
    vim.opt.rtp = rtp
    for k, v in pairs(package.loaded) do
      if k:find("^foobar") then
        package.loaded[k] = nil
      end
    end
    Helpers.fs_rm("")
    assert(not vim.uv.fs_stat(Helpers.path("")), "fs root should be deleted")
  end)

  it("lsmod lists all mods in dir", function()
    vim.opt.rtp:append(Helpers.path(""))
    local tests = {
      {
        root = "lua/foo",
        mod = "foo",
        files = { "lua/foo/one.lua", "lua/foo/two.lua", "lua/foo/init.lua" },
        mods = { "foo.one", "foo.two", "foo" },
      },
      {
        root = "lua/foo",
        mod = "foo",
        files = { "lua/foo/one.lua", "lua/foo/two.lua", "lua/foo.lua" },
        mods = { "foo.one", "foo.two", "foo" },
      },
      {
        root = "lua/foo",
        mod = "foo",
        files = { "lua/foo/one.lua", "lua/foo/two.lua" },
        mods = { "foo.one", "foo.two" },
      },
      {
        root = "lua/load-plugins",
        mod = "load-plugins",
        files = { "lua/load-plugins.lua" },
        mods = { "load-plugins" },
      },
    }

    for t, test in ipairs(tests) do
      local expected = vim.deepcopy(test.mods)
      table.sort(expected)
      Helpers.fs_rm("")
      local files = Helpers.fs_create(test.files)

      -- test with empty cache
      Cache.reset()
      local root = Util.find_root(test.mod)
      assert(root, "no root found for " .. test.mod .. " (test " .. t .. ")")
      assert.same(Helpers.path(test.root), root)
      local mods = {}
      Util.lsmod(test.mod, function(modname, modpath)
        mods[#mods + 1] = modname
      end)
      table.sort(mods)
      assert.same(expected, mods)

      -- fill the cache
      Cache.reset()
      root = Util.find_root(test.mod)
      assert(root, "no root found for " .. test.mod .. " (test " .. t .. ")")
      assert.same(Helpers.path(test.root), root)
      mods = {}
      Util.lsmod(test.mod, function(modname, modpath)
        mods[#mods + 1] = modname
      end)
      table.sort(mods)
      assert.same(expected, mods)
    end
  end)

  it("find the correct root with dels", function()
    Cache.reset()
    vim.opt.rtp:append(Helpers.path("old"))
    Helpers.fs_create({ "old/lua/foobar/init.lua" })
    local root = Util.find_root("foobar")
    assert(root, "foobar root not found")
    assert.same(Helpers.path("old/lua/foobar"), root)

    Helpers.fs_rm("old")
    assert(not vim.uv.fs_stat(Helpers.path("old/lua/foobar")), "old/lua/foobar should not exist")

    -- vim.opt.rtp = rtp
    vim.opt.rtp:append(Helpers.path("new"))
    Helpers.fs_create({ "new/lua/foobar/init.lua" })
    root = Util.find_root("foobar")
    assert(root, "foobar root not found")
    assert.same(Helpers.path("new/lua/foobar"), root)
  end)

  it("merges correctly", function()
    local tests = {
      {
        input = { { a = 1 }, { b = 2 } },
        output = { a = 1, b = 2 },
      },
      {
        input = { nil, { a = 1 }, { b = 2 } },
        output = { a = 1, b = 2 },
      },
      {
        input = { { a = 1 }, { b = 2 }, nil },
        output = { a = 1, b = 2 },
      },
      {
        input = { { a = 1 }, nil, { b = 2 } },
        output = { a = 1, b = 2 },
      },
      {
        input = { nil, { a = 1 }, nil, { b = 2 }, nil },
        output = { a = 1, b = 2 },
      },
      {
        input = { { a = 1 }, { a = 2 } },
        output = { a = 2 },
      },
      {
        input = { { a = { 1, 2 } }, { a = { 3 } } },
        output = { a = { 3 } },
      },
      {
        input = { { b = { 1, 2 } }, { a = { 3 }, b = vim.NIL } },
        output = { a = { 3 } },
      },
      {
        input = { { a = 1 }, { b = 2, a = vim.NIL } },
        output = { b = 2 },
      },
    }

    for _, test in ipairs(tests) do
      local n = 0
      for i in pairs(test.input) do
        n = math.max(n, i)
      end
      assert.same(test.output, Util.merge(unpack(test.input, 1, n)))
    end
  end)
end)
```

## File: `tests/handlers/keys_spec.lua`
```
local Keys = require("lazy.core.handler.keys")

describe("keys", function()
  it("parses ids correctly", function()
    local tests = {
      { "<C-/>", "<c-/>", true },
      { "<C-h>", "<c-H>", true },
      { "<C-h>k", "<c-H>K", false },
    }
    for _, test in ipairs(tests) do
      if test[3] then
        assert.same(Keys.parse(test[1]).id, Keys.parse(test[2]).id)
      else
        assert.is_not.same(Keys.parse(test[1]).id, Keys.parse(test[2]).id)
      end
    end
  end)
end)
```

## File: `tests/manage/process_spec.lua`
```
local Async = require("lazy.async")
local Process = require("lazy.manage.process")

describe("process", function()
  it("runs sync", function()
    local lines = Process.exec({ "echo", "-n", "hello" })
    assert.are.same({ "hello" }, lines)
  end)

  it("runs sync from async context", function()
    local lines ---@type string[]
    local async = Async.new(function()
      lines = Process.exec({ "echo", "-n", "hello" })
    end)
    async:wait()

    assert.are.same({ "hello" }, lines)
  end)
end)
```

## File: `tests/manage/runner_spec.lua`
```
local Async = require("lazy.async")
local Runner = require("lazy.manage.runner")

describe("runner", function()
  local plugins = { { name = "plugin1", _ = {} }, { name = "plugin2", _ = {} } }

  ---@type {plugin:string, task:string}[]
  local runs = {}
  before_each(function()
    runs = {}
  end)

  package.loaded["lazy.manage.task.test"] = {}
  package.loaded["lazy.manage.task.test"]["skip"] = {
    skip = function()
      return true
    end,
  }
  for i = 1, 10 do
    package.loaded["lazy.manage.task.test"]["test" .. i] = {
      ---@param task LazyTask
      run = function(task)
        table.insert(runs, { plugin = task.plugin.name, task = task.name })
      end,
    }
    package.loaded["lazy.manage.task.test"]["error" .. i] = {
      ---@param task LazyTask
      run = function(task)
        table.insert(runs, { plugin = task.plugin.name, task = task.name })
        error("error" .. i)
      end,
    }
    package.loaded["lazy.manage.task.test"]["async" .. i] = {
      ---@async
      ---@param task LazyTask
      run = function(task)
        Async.yield()
        table.insert(runs, { plugin = task.plugin.name, task = task.name })
      end,
    }
  end

  it("runs the pipeline", function()
    local runner = Runner.new({ plugins = plugins, pipeline = { "test.test1", "test.test2" } })
    runner:start()
    runner:wait()
    assert.equal(4, #runs)
  end)

  it("waits", function()
    local runner = Runner.new({ plugins = plugins, pipeline = { "test.test1", "wait", "test.test2" } })
    runner:start()
    runner:wait()
    assert.equal(4, #runs)
  end)

  it("handles async", function()
    local runner = Runner.new({ plugins = plugins, pipeline = { "test.async1", "wait", "test.async2" } })
    runner:start()
    runner:wait()
    assert.equal(4, #runs)
  end)

  it("handles skips", function()
    local runner = Runner.new({ plugins = plugins, pipeline = { "test.test1", "test.skip", "test.test2" } })
    runner:start()
    runner:wait()
    assert.equal(4, #runs, runs)
  end)

  it("handles opts", function()
    local runner = Runner.new({ plugins = plugins, pipeline = { "test.test1", { "test.test2", foo = "bar" } } })
    runner:start()
    runner:wait()
    assert.equal(4, #runs)
  end)

  it("aborts on error", function()
    local runner = Runner.new({ plugins = plugins, pipeline = { "test.test1", "test.error1", "test.test2" } })
    runner:start()
    runner:wait()
    assert.equal(4, #runs)
  end)
end)
```

## File: `tests/manage/semver_spec.lua`
```
local Semver = require("lazy.manage.semver")

local function v(version)
  return Semver.version(version)
end

describe("semver version", function()
  local tests = {
    ["v1.2.3"] = { major = 1, minor = 2, patch = 3 },
    ["v1.2"] = { major = 1, minor = 2, patch = 0 },
    ["v1.2.3-prerelease"] = { major = 1, minor = 2, patch = 3, prerelease = "prerelease" },
    ["v1.2-prerelease"] = { major = 1, minor = 2, patch = 0, prerelease = "prerelease" },
    ["v1.2.3-prerelease+build"] = { major = 1, minor = 2, patch = 3, prerelease = "prerelease", build = "build" },
    ["1.2.3+build"] = { major = 1, minor = 2, patch = 3, build = "build" },
  }
  for input, output in pairs(tests) do
    output.input = input
    it("correctly parses " .. input, function()
      assert.same(output, v(input))
    end)
  end
end)

describe("semver range", function()
  local tests = {
    ["1.2.3"] = { from = { 1, 2, 3 }, to = { 1, 2, 4 } },
    ["1.2"] = { from = { 1, 2, 0 }, to = { 1, 3, 0 } },
    ["=1.2.3"] = { from = { 1, 2, 3 }, to = { 1, 2, 4 } },
    [">1.2.3"] = { from = { 1, 2, 4 } },
    [">=1.2.3"] = { from = { 1, 2, 3 } },
    ["~1.2.3"] = { from = { 1, 2, 3 }, to = { 1, 3, 0 } },
    ["^1.2.3"] = { from = { 1, 2, 3 }, to = { 2, 0, 0 } },
    ["^0.2.3"] = { from = { 0, 2, 3 }, to = { 0, 3, 0 } },
    ["^0.0.1"] = { from = { 0, 0, 1 }, to = { 0, 0, 2 } },
    ["^1.2"] = { from = { 1, 2, 0 }, to = { 2, 0, 0 } },
    ["~1.2"] = { from = { 1, 2, 0 }, to = { 1, 3, 0 } },
    ["~1"] = { from = { 1, 0, 0 }, to = { 2, 0, 0 } },
    ["^1"] = { from = { 1, 0, 0 }, to = { 2, 0, 0 } },
    ["1.*"] = { from = { 1, 0, 0 }, to = { 2, 0, 0 } },
    ["1"] = { from = { 1, 0, 0 }, to = { 2, 0, 0 } },
    ["1.x"] = { from = { 1, 0, 0 }, to = { 2, 0, 0 } },
    ["1.2.x"] = { from = { 1, 2, 0 }, to = { 1, 3, 0 } },
    ["1.2.*"] = { from = { 1, 2, 0 }, to = { 1, 3, 0 } },
    ["*"] = { from = { 0, 0, 0 } },
    ["1.2 - 2.3.0"] = { from = { 1, 2, 0 }, to = { 2, 3, 0 } },
    ["1.2.3 - 2.3.4"] = { from = { 1, 2, 3 }, to = { 2, 3, 4 } },
    ["1.2.3 - 2"] = { from = { 1, 2, 3 }, to = { 3, 0, 0 } },
  }
  for input, output in pairs(tests) do
    output.from = v(output.from)
    output.to = output.to and v(output.to)

    local range = Semver.range(input)
    it("correctly parses " .. input, function()
      assert.same(output, range)
    end)

    it("from in range " .. input, function()
      assert(range:matches(output.from))
    end)

    it("from - 1 not in range " .. input, function()
      local lower = vim.deepcopy(range.from)
      lower.major = lower.major - 1
      assert(not range:matches(lower))
    end)

    it("to not in range " .. input .. " to:" .. tostring(range.to), function()
      if range.to then
        assert(not (range.to < range.to))
        assert(not range:matches(range.to))
      end
    end)
  end

  it("handles prereleass", function()
    assert(not Semver.range("1.2.3"):matches("1.2.3-alpha"))
    assert(Semver.range("1.2.3-alpha"):matches("1.2.3-alpha"))
    assert(not Semver.range("1.2.3-alpha"):matches("1.2.3-beta"))
  end)
end)

describe("semver order", function()
  it("is correct", function()
    assert(v("v1.2.3") == v("1.2.3"))
    assert(not (v("v1.2.3") < v("1.2.3")))
    assert(v("v1.2.3") > v("1.2.3-prerelease"))
    assert(v("v1.2.3-alpha") < v("1.2.3-beta"))
    assert(v("v1.2.3-prerelease") < v("1.2.3"))
    assert(v("v1.2.3") >= v("1.2.3"))
    assert(v("v1.2.3") >= v("1.0.3"))
    assert(v("v1.2.3") >= v("1.2.2"))
    assert(v("v1.2.3") > v("1.2.2"))
    assert(v("v1.2.3") > v("1.0.3"))
    assert.same(Semver.last({ v("1.2.3"), v("2.0.0") }), v("2.0.0"))
    assert.same(Semver.last({ v("2.0.0"), v("1.2.3") }), v("2.0.0"))
  end)
end)
```

## File: `tests/manage/task_spec.lua`
```
--# selene:allow(incorrect_standard_library_use)
local Async = require("lazy.async")
local Task = require("lazy.manage.task")

describe("task", function()
  local plugin = { name = "test", _ = {} }

  ---@type {done?:boolean, error:string?}
  local task_result = {}

  local opts = {
    ---@param task LazyTask
    on_done = function(task)
      task_result = { done = true, error = task.error }
    end,
  }

  before_each(function()
    task_result = {}
  end)

  it("simple function", function()
    local task = Task.new(plugin, "test", function() end, opts)
    assert(task:running())
    task:wait()
    assert(not task:running())
    assert(task_result.done)
  end)

  it("detects errors", function()
    local task = Task.new(plugin, "test", function()
      error("test")
    end, opts)
    assert(task:running())
    task:wait()
    assert(not task:running())
    assert(task_result.done)
    assert(task_result.error)
    assert(task:has_errors() and task:output(vim.log.levels.ERROR):find("test"))
  end)

  it("async", function()
    local running = true
    ---@async
    local task = Task.new(plugin, "test", function()
      Async.yield()
      running = false
    end, opts)
    assert(task:running())
    assert(running)
    assert(task:running())
    task:wait()
    assert(not running)
    assert(not task:running())
    assert(task_result.done)
    assert(not task:has_errors())
  end)

  it("spawn errors", function()
    local task = Task.new(plugin, "spawn_errors", function(task)
      task:spawn("foobar")
    end, opts)
    assert(task:running())
    task:wait()
    assert(not task:running())
    assert(task_result.done)
    assert(task:has_errors() and task:output(vim.log.levels.ERROR):find("Failed to spawn"), task:output())
  end)

  it("spawn", function()
    local task = Task.new(plugin, "test", function(task)
      task:spawn("echo", { args = { "foo" } })
    end, opts)
    assert(task:running())
    assert(task:running())
    task:wait()
    assert.same(task:output(), "foo")
    assert(task_result.done)
    assert(not task:has_errors())
  end)

  it("spawn 2x", function()
    local task = Task.new(plugin, "test", function(task)
      task:spawn("echo", { args = { "foo" } })
      task:spawn("echo", { args = { "bar" } })
    end, opts)
    assert(task:running())
    assert(task:running())
    task:wait()
    assert(task:output() == "foo\nbar" or task:output() == "bar\nfoo", task:output())
    assert(task_result.done)
    assert(not task:has_errors())
  end)
end)
```

