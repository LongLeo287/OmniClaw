# Knowledge Dump for action-validator

## File: .pre-commit-hooks.yaml
```
- id: action-validator
  name: Validate GitHub Actions workflows
  description: "Validate GitHub Actions workflows"
  entry: action-validator
  language: rust
  files: '.github/workflows/.*\.ya?ml'

```

## File: .prettierrc.json
```
{}

```

## File: action.yml
```
name: action-validator
description: Downloads, caches, and runs action-validator with verbose output on files tracked by Git.
inputs:
  version:
    description: action-validator version in semver format without the 'v' prefix
    required: false
    default: "latest"
  patterns:
    description: 'Newline-separated list of git ls-files patterns'
    required: false
    default: |
      :(glob).github/**/action.yml
      :(glob).github/**/action.yaml
      .github/workflows/*.yml
      .github/workflows/*.yaml
branding:
  icon: check
  color: green
runs:
  using: "composite"
  steps:
    - name: Convert architecture
      id: arch
      shell: sh
      env:
        runner_arch: ${{ runner.arch }} # Possible values are X86, X64, ARM, or ARM64.
      run: |
        case "$runner_arch" in
          X64) echo "arch=amd64" >> "$GITHUB_OUTPUT" ;;
          ARM64) echo "arch=arm64" >> "$GITHUB_OUTPUT" ;;
          *) echo "Unsupported architecture: $runner_arch" >&2; exit 1 ;;
        esac
    - name: Convert OS
      id: os
      shell: sh
      env:
        runner_os: ${{ runner.os }} # Possible values are Linux, Windows, or macOS.
      run: |
        case "$runner_os" in
          Linux) echo "os=linux" >> "$GITHUB_OUTPUT" ;;
          macOS) echo "os=darwin" >> "$GITHUB_OUTPUT" ;;
          *) echo "Unsupported OS: $runner_os" >&2; exit 1 ;;
        esac
    - name: Resolve version
      id: resolve
      shell: bash
      env:
        GH_TOKEN: ${{ github.token }}
        version: ${{ inputs.version }}
      run: |
        if [[ "$version" = "latest" ]]; then
          tag="$(gh release view --repo mpalmer/action-validator --json tagName -q .tagName)"
          version="${tag#v}"
        fi
        echo "version=$version" >> "$GITHUB_OUTPUT"
    - name: Cache
      id: cache
      uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
      with:
        path: /usr/local/bin/action-validator
        key: action-validator_v${{ steps.resolve.outputs.version }}_${{ steps.os.outputs.os }}_${{ steps.arch.outputs.arch }}
    - if: steps.cache.outputs.cache-hit != 'true'
      name: Install
      shell: sh
      env:
        GH_TOKEN: ${{ github.token }}
        version: ${{ steps.resolve.outputs.version }}
        os: ${{ steps.os.outputs.os }}
        arch: ${{ steps.arch.outputs.arch }}
        output: /usr/local/bin/action-validator
      run: |
        printf 'gh release download "v%s" --repo mpalmer/action-validator --pattern "action-validator_%s_%s" --output "%s"\n' "$version" "$os" "$arch" "$output"
        gh release download "v$version" --repo mpalmer/action-validator --pattern "action-validator_${os}_$arch" --output "$output"
        chmod +x "$output"
    - name: Run
      shell: sh
      env:
        patterns: ${{ inputs.patterns }}
      run: |
        printf '%s\n' "$patterns" | xargs -I{} git ls-files -z -- {} | sort --zero-terminated --unique | xargs -0 action-validator --verbose

```

## File: build.rs
```
fn main() {
    println!("cargo:rerun-if-changed=tests/fixtures");
}

```

## File: code_of_conduct.md
```
# Contributor Code of Conduct

As contributors and maintainers of this project, and in the interest of
fostering an open and welcoming community, we pledge to respect all people who
contribute through reporting issues, posting feature requests, updating
documentation, submitting pull requests or patches, and other activities.

We are committed to making participation in this project a harassment-free
experience for everyone, regardless of level of experience, gender, gender
identity and expression, sexual orientation, disability, personal appearance,
body size, race, ethnicity, age, religion, or nationality.

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery
* Personal attacks
* Trolling or insulting/derogatory comments
* Public or private harassment
* Publishing other's private information, such as physical or electronic
  addresses, without explicit permission
* Other unethical or unprofessional conduct

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

By adopting this Code of Conduct, project maintainers commit themselves to
fairly and consistently applying these principles to every aspect of managing
this project. Project maintainers who do not follow or enforce the Code of
Conduct may be permanently removed from the project team.

This code of conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community.

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting a project maintainer at mpalmer@hezmatt.org. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. Maintainers are
obligated to maintain confidentiality with regard to the reporter of an
incident.

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 1.3.0, available at
[http://contributor-covenant.org/version/1/3/0/][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/3/0/

```

## File: contributing.md
```
# Overview

* If you have found a discrepancy in documented and observed behaviour, that
  is a bug. Feel free to [report it as an
  issue](https://github.com/mpalmer/action-validator/issues), providing
  sufficient detail to reproduce the problem.

* If you would like to add new behaviour, please submit a well-tested and
  well-documented [pull
  request](https://github.com/mpalmer/action-validator/pulls).

* At all times, abide by the Code of Conduct (CODE_OF_CONDUCT.md).

---

# Environment Setup

## Install Rust
Firstly, you'll need a Rust toolchain to make any changes to the core functionality of this project. We recommend [using `rustup`](https://www.rust-lang.org/tools/install), because that's what the Rust core team recommend.

To confirm that rust is installed, run the `cargo` command. If you don't receive the help docs output, you may need to add rust to your shell rc file.

## Git Submodule Setup
This repository uses [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Specifically for the use of [schemastore](https://github.com/SchemaStore/schemastore).

To setup the git submodule after cloning this repo to your local, you'll want to run the following commands:
1. `git submodule init`
2. `git submodule update`

It should look similar to the output below.

```bash
❯ git submodule init
Submodule 'src/schemastore' (https://github.com/SchemaStore/schemastore) registered for path 'src
/schemastore'
❯ git submodule update
Cloning into '/Users/someuser/action-validator/src/schemastore'...
Submodule path 'src/schemastore': checked out 'd3e6ab7727380b214acbab05570fb09a3e5d2dfc'
```

At this point, you should be all set to `cargo run`!

## Node/WASM Setup
If you plan to work on the WASM/Node bindings, you'll also need to install Node. We recommend using [NVM](https://github.com/nvm-sh/nvm) to install the Node version listed in `.nvmrc`.

Once Node is installed, run `npm install` at the root of the repository.

You should now be all set to run `npm build`, to build the Node/WASM bindings. Once built, run `npx action-validator` to run the CLI via the Node/WASM bindings.

# Running the Validator Locally

## `cargo run [FILE] -- [OPTIONS]`
`cargo run` will create a _debug_ executable and run the project. If this is your first time running the command, cargo will compile the development binary with `cargo build`. This will install all of the dependencies and create the debug binary `action-validator` in the `/target/debug/` directory. `cargo run` will then invoke this binary after creation.

One caveat if you're running with `cargo run`: if you want to supply the program with options, you need to use the `--` operator between `cargo run` and your provided options. This let's cargo know which flags are meant for cargo, and which are meant for the executable.

## `cargo build` && `./target/debug/action-validator [OPTIONS]`
As discussed in the prior section, `cargo build` install dependencies (if they're not cached) and build the development binary. This binary can then be invoked directly by running `./target/debug/action-validator`. This does **not** require the use of the `--` operator in between the binary and any provided options.

## Try It Yourself!

Run the command `cargo run -- --help`. You should see an output similar to the following.
```bash
❯ cargo run -- --help
    Finished dev [unoptimized + debuginfo] target(s) in 0.05s
     Running `target/debug/action-validator --help`
A validator for GitHub Action and Workflow YAML files

Usage: action-validator [OPTIONS] [path_to_action_yaml]...

Arguments:
  [path_to_action_yaml]...  Input file

Options:
  -v, --verbose  Be more verbose
  -h, --help     Print help information
  -V, --version  Print version information
```

# Writing Tests

All tests live in the `tests` directory. Currently, this project implements snapshot testing,
but that's not to say you couldn't write unit or integration tests with the current structure.
To run the tests, simply run `cargo test` from the root directory. If you want to test a specific
feature, you can add the `-F {feature}` flag (e.g. `cargo test -F remote-checks`).

## Unit/Integration Tests
As of this writing, there are no unit or integration tests. If you are looking to write some, please
follow the directions in [this guide](https://doc.rust-lang.org/book/ch11-01-writing-tests.html).

## Snapshot Tests
A snapshot test is performed when we execute the cli and capture `stdout`, `stderr`, and/or an exit code.
When the tests are run, the results of the test must exactly match those of the previous run. For this project,
the snapshot tests are named in the format `{next_id}_{whats_being_tested}` (e.g. `011_remote_checks_failure`).

If you have made changes which will change the output of the program and cause snapshots to fail, you can run
`cargo test -F test-save-snapshots`. This feature causes the executed command to save the `stdout`, `stderr`, and/or
exit code to the specified testing directory.

If you are writing a net new test, you will need to create the test directory with your workflow or action file, and a
`test.json` file. Once you're done, you can save the results to that directy by running
`cargo test -F test-save-snapshots`.

The `test.json` file contains the test configuration. It can usually be left empty (i.e. `{}`).

```jsonc
// Example test.json
{
  "targets": {
    "node": false,
    "native": true
  },
  "cli_args": [
    "--rootdir",
    "tests/fixtures/011_subdir_globs/subdir",
    "tests/fixtures/011_subdir_globs/subdir/glob.yml"
  ]
}
```

# Testing Node/WASM Bindings

To test against the Node/WASM bindings, you can run `npm test`, or `npm test:dev` (to skip optimisations).
Note that Node support is considered experimental, and does not have one to one feature parity with the native binary yet.
As such, some tests may fail, even on `main`.

```

## File: package-lock.json
```
{
  "name": "@action-validator/root",
  "version": "0.0.0-git",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "@action-validator/root",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "workspaces": [
        "packages/*"
      ],
      "devDependencies": {
        "chalk": "5.2.0",
        "diff": "5.1.0",
        "prettier": "2.8.4",
        "wasm-pack": "0.13.1"
      }
    },
    "node_modules/@action-validator/cli": {
      "resolved": "packages/cli",
      "link": true
    },
    "node_modules/@action-validator/core": {
      "resolved": "packages/core",
      "link": true
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/axios": {
      "version": "0.26.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-0.26.1.tgz",
      "integrity": "sha512-fPwcX4EvnSHuInCMItEhAGnaSEXRBjtzh9fOtsE6E1G6p7vl7edEeZe11QHf18+6+9gR5PbKV/sGKNaD8YaMeA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "follow-redirects": "^1.14.8"
      }
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/binary-install": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/binary-install/-/binary-install-1.1.0.tgz",
      "integrity": "sha512-rkwNGW+3aQVSZoD0/o3mfPN6Yxh3Id0R/xzTVBVVpGNlVz8EGwusksxRlbk/A5iKTZt9zkMn3qIqmAt3vpfbzg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "axios": "^0.26.1",
        "rimraf": "^3.0.2",
        "tar": "^6.1.11"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/brace-expansion": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz",
      "integrity": "sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/chalk": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
      "integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA==",
      "dev": true,
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/chownr": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz",
      "integrity": "sha512-bIomtDF5KGpdogkLd9VspvFzk9KfpyyGlS8YFVZl7TGPBHL5snIOnxeshwVgPteQ9b4Eydl+pVbIyE1DcvCWgQ==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/diff": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/diff/-/diff-5.1.0.tgz",
      "integrity": "sha512-D+mk+qE8VC/PAUrlAU34N+VfXev0ghe5ywmpqrawphmVZc1bEfn56uo9qpyGp1p4xpzOHkSW4ztBd6L7Xx4ACw==",
      "dev": true,
      "engines": {
        "node": ">=0.3.1"
      }
    },
    "node_modules/fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      },
      "engines": {
        "node": ">=8.6.0"
      }
    },
    "node_modules/fastq": {
      "version": "1.19.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz",
      "integrity": "sha512-GwLTyxkCXjXbxqIhTsMI2Nui8huMPtnxg7krajPJAjnEG/iiOS7i+zCtWGZR9G0NBKbXKh6X9m9UIsYX/N6vvQ==",
      "license": "ISC",
      "dependencies": {
        "reusify": "^1.0.4"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "license": "MIT",
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/follow-redirects": {
      "version": "1.15.9",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.15.9.tgz",
      "integrity": "sha512-gew4GsXizNgdoRyqmyfMHyAmXsZDk6mHkSxZFCzW9gwlbtOW44CDtYavM+y+72qD/Vq2l550kMF52DT8fOLJqQ==",
      "dev": true,
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "license": "MIT",
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    },
    "node_modules/fs-minipass": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/fs-minipass/-/fs-minipass-2.1.0.tgz",
      "integrity": "sha512-V/JgOLFCS+R6Vcq0slCuaeWEdNC3ouDlJMNIsacH2VtALiu9mV4LPrHc5cDl8k5aw6J8jwgWWpiTo5RYhmIzvg==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "minipass": "^3.0.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/fs-minipass/node_modules/minipass": {
      "version": "3.3.6",
      "resolved": "https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz",
      "integrity": "sha512-DxiNidxSEK+tHG6zOIklvNOwm3hvCrbUrdtzY74U6HKTJxvIDfOUL5W5P2Ghd3DTkhhKPYGqeNUIh5qcM4YBfw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^4.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/fs.realpath": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
      "integrity": "sha512-OO0pH2lK6a0hZnAdau5ItzHPI6pUlvI7jMVnxUQRtw4owF2wk8lOSabtGDCTP4Ggrg2MbGnWO9X8K1t4+fGMDw==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/glob": {
      "version": "7.2.3",
      "resolved": "https://registry.npmjs.org/glob/-/glob-7.2.3.tgz",
      "integrity": "sha512-nFR0zLpU2YCaRxwoCJvL6UvCH2JFyFVIvwTLsIf21AuHlMskA1hhTdk+LlYJtOlYt9v6dvszD2BGRqBL+iQK9Q==",
      "deprecated": "Glob versions prior to v9 are no longer supported",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "fs.realpath": "^1.0.0",
        "inflight": "^1.0.4",
        "inherits": "2",
        "minimatch": "^3.1.1",
        "once": "^1.3.0",
        "path-is-absolute": "^1.0.0"
      },
      "engines": {
        "node": "*"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/inflight": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz",
      "integrity": "sha512-k92I/b08q4wvFscXCLvqfsHCrjrF7yiXsQuIVvVE7N82W3+aqpzuUdBbfhWcy/FZR3/4IgflMgKLOsvPDrGCJA==",
      "deprecated": "This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "once": "^1.3.0",
        "wrappy": "1"
      }
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "license": "MIT",
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "license": "MIT",
      "dependencies": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      },
      "engines": {
        "node": ">=8.6"
      }
    },
    "node_modules/minimatch": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz",
      "integrity": "sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "brace-expansion": "^1.1.7"
      },
      "engines": {
        "node": "*"
      }
    },
    "node_modules/minipass": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/minipass/-/minipass-5.0.0.tgz",
      "integrity": "sha512-3FnjYuehv9k6ovOEbyOswadCDPX1piCfhV8ncmYtHOjuPwylVWsghTLo7rabjC3Rx5xD4HDx8Wm1xnMF7S5qFQ==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/minizlib": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/minizlib/-/minizlib-2.1.2.tgz",
      "integrity": "sha512-bAxsR8BVfj60DWXHE3u30oHzfl4G7khkSuPW+qvpd7jFRHm7dLxOjUk1EHACJ/hxLY8phGJ0YhYHZo7jil7Qdg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "minipass": "^3.0.0",
        "yallist": "^4.0.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/minizlib/node_modules/minipass": {
      "version": "3.3.6",
      "resolved": "https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz",
      "integrity": "sha512-DxiNidxSEK+tHG6zOIklvNOwm3hvCrbUrdtzY74U6HKTJxvIDfOUL5W5P2Ghd3DTkhhKPYGqeNUIh5qcM4YBfw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^4.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/mkdirp": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-1.0.4.tgz",
      "integrity": "sha512-vVqVZQyf3WLx2Shd0qJ9xuvqgAyKPLAiqITEtqW0oIUjzo3PePDd6fW9iFz30ef7Ysp/oiWqbhszeGWW2T6Gzw==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "mkdirp": "bin/cmd.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "wrappy": "1"
      }
    },
    "node_modules/path-is-absolute": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
      "integrity": "sha512-AVbw3UJ2e9bq64vSaS9Am0fje1Pa8pbGqTTsmXfaIiMpnr5DlDhfJOuLj9Sf95ZPVDAUerDfEk88MPmPe7UCQg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/picomatch": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
      "integrity": "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==",
      "license": "MIT",
      "engines": {
        "node": ">=8.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/prettier": {
      "version": "2.8.4",
      "resolved": "https://registry.npmjs.org/prettier/-/prettier-2.8.4.tgz",
      "integrity": "sha512-vIS4Rlc2FNh0BySk3Wkd6xmwxB0FpOndW5fisM5H8hsZSxU2VWVB5CWIkIjWvrHjIhxk2g3bfMKM87zNTrZddw==",
      "dev": true,
      "bin": {
        "prettier": "bin-prettier.js"
      },
      "engines": {
        "node": ">=10.13.0"
      },
      "funding": {
        "url": "https://github.com/prettier/prettier?sponsor=1"
      }
    },
    "node_modules/queue-microtask": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
      "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/reusify": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
      "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==",
      "license": "MIT",
      "engines": {
        "iojs": ">=1.0.0",
        "node": ">=0.10.0"
      }
    },
    "node_modules/rimraf": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz",
      "integrity": "sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==",
      "deprecated": "Rimraf versions prior to v4 are no longer supported",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "glob": "^7.1.3"
      },
      "bin": {
        "rimraf": "bin.js"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/run-parallel": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
      "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "queue-microtask": "^1.2.2"
      }
    },
    "node_modules/tar": {
      "version": "6.2.1",
      "resolved": "https://registry.npmjs.org/tar/-/tar-6.2.1.tgz",
      "integrity": "sha512-DZ4yORTwrbTj/7MZYq2w+/ZFdI6OZ/f9SFHR+71gIVUZhOQPHzVCLpvRnPgyaMpfWxxk/4ONva3GQSyNIKRv6A==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "chownr": "^2.0.0",
        "fs-minipass": "^2.0.0",
        "minipass": "^5.0.0",
        "minizlib": "^2.1.1",
        "mkdirp": "^1.0.3",
        "yallist": "^4.0.0"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "license": "MIT",
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    },
    "node_modules/wasm-pack": {
      "version": "0.13.1",
      "resolved": "https://registry.npmjs.org/wasm-pack/-/wasm-pack-0.13.1.tgz",
      "integrity": "sha512-P9exD4YkjpDbw68xUhF3MDm/CC/3eTmmthyG5bHJ56kalxOTewOunxTke4SyF8MTXV6jUtNjXggPgrGmMtczGg==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT OR Apache-2.0",
      "dependencies": {
        "binary-install": "^1.0.1"
      },
      "bin": {
        "wasm-pack": "run.js"
      }
    },
    "node_modules/wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/yallist": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz",
      "integrity": "sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==",
      "dev": true,
      "license": "ISC"
    },
    "packages/cli": {
      "name": "@action-validator/cli",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "bin": {
        "action-validator": "cli.mjs"
      },
      "devDependencies": {
        "@action-validator/core": "file:../core"
      },
      "peerDependencies": {
        "@action-validator/core": "0.0.0-git"
      }
    },
    "packages/core": {
      "name": "@action-validator/core",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "dependencies": {
        "fast-glob": "^3.3.3"
      }
    }
  },
  "dependencies": {
    "@action-validator/cli": {
      "version": "file:packages/cli",
      "requires": {
        "@action-validator/core": "file:../core"
      }
    },
    "@action-validator/core": {
      "version": "file:packages/core",
      "requires": {
        "fast-glob": "^3.3.3"
      }
    },
    "@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "requires": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      }
    },
    "@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A=="
    },
    "@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "requires": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      }
    },
    "axios": {
      "version": "0.26.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-0.26.1.tgz",
      "integrity": "sha512-fPwcX4EvnSHuInCMItEhAGnaSEXRBjtzh9fOtsE6E1G6p7vl7edEeZe11QHf18+6+9gR5PbKV/sGKNaD8YaMeA==",
      "dev": true,
      "requires": {
        "follow-redirects": "^1.14.8"
      }
    },
    "balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true
    },
    "binary-install": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/binary-install/-/binary-install-1.1.0.tgz",
      "integrity": "sha512-rkwNGW+3aQVSZoD0/o3mfPN6Yxh3Id0R/xzTVBVVpGNlVz8EGwusksxRlbk/A5iKTZt9zkMn3qIqmAt3vpfbzg==",
      "dev": true,
      "requires": {
        "axios": "^0.26.1",
        "rimraf": "^3.0.2",
        "tar": "^6.1.11"
      }
    },
    "brace-expansion": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz",
      "integrity": "sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==",
      "dev": true,
      "requires": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "requires": {
        "fill-range": "^7.1.1"
      }
    },
    "chalk": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
      "integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA==",
      "dev": true
    },
    "chownr": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz",
      "integrity": "sha512-bIomtDF5KGpdogkLd9VspvFzk9KfpyyGlS8YFVZl7TGPBHL5snIOnxeshwVgPteQ9b4Eydl+pVbIyE1DcvCWgQ==",
      "dev": true
    },
    "concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==",
      "dev": true
    },
    "diff": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/diff/-/diff-5.1.0.tgz",
      "integrity": "sha512-D+mk+qE8VC/PAUrlAU34N+VfXev0ghe5ywmpqrawphmVZc1bEfn56uo9qpyGp1p4xpzOHkSW4ztBd6L7Xx4ACw==",
      "dev": true
    },
    "fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "requires": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      }
    },
    "fastq": {
      "version": "1.19.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz",
      "integrity": "sha512-GwLTyxkCXjXbxqIhTsMI2Nui8huMPtnxg7krajPJAjnEG/iiOS7i+zCtWGZR9G0NBKbXKh6X9m9UIsYX/N6vvQ==",
      "requires": {
        "reusify": "^1.0.4"
      }
    },
    "fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "requires": {
        "to-regex-range": "^5.0.1"
      }
    },
    "follow-redirects": {
      "version": "1.15.9",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.15.9.tgz",
      "integrity": "sha512-gew4GsXizNgdoRyqmyfMHyAmXsZDk6mHkSxZFCzW9gwlbtOW44CDtYavM+y+72qD/Vq2l550kMF52DT8fOLJqQ==",
      "dev": true
    },
    "fs-minipass": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/fs-minipass/-/fs-minipass-2.1.0.tgz",
      "integrity": "sha512-V/JgOLFCS+R6Vcq0slCuaeWEdNC3ouDlJMNIsacH2VtALiu9mV4LPrHc5cDl8k5aw6J8jwgWWpiTo5RYhmIzvg==",
      "dev": true,
      "requires": {
        "minipass": "^3.0.0"
      },
      "dependencies": {
        "minipass": {
          "version": "3.3.6",
          "resolved": "https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz",
          "integrity": "sha512-DxiNidxSEK+tHG6zOIklvNOwm3hvCrbUrdtzY74U6HKTJxvIDfOUL5W5P2Ghd3DTkhhKPYGqeNUIh5qcM4YBfw==",
          "dev": true,
          "requires": {
            "yallist": "^4.0.0"
          }
        }
      }
    },
    "fs.realpath": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
      "integrity": "sha512-OO0pH2lK6a0hZnAdau5ItzHPI6pUlvI7jMVnxUQRtw4owF2wk8lOSabtGDCTP4Ggrg2MbGnWO9X8K1t4+fGMDw==",
      "dev": true
    },
    "glob": {
      "version": "7.2.3",
      "resolved": "https://registry.npmjs.org/glob/-/glob-7.2.3.tgz",
      "integrity": "sha512-nFR0zLpU2YCaRxwoCJvL6UvCH2JFyFVIvwTLsIf21AuHlMskA1hhTdk+LlYJtOlYt9v6dvszD2BGRqBL+iQK9Q==",
      "dev": true,
      "requires": {
        "fs.realpath": "^1.0.0",
        "inflight": "^1.0.4",
        "inherits": "2",
        "minimatch": "^3.1.1",
        "once": "^1.3.0",
        "path-is-absolute": "^1.0.0"
      }
    },
    "glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "requires": {
        "is-glob": "^4.0.1"
      }
    },
    "inflight": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz",
      "integrity": "sha512-k92I/b08q4wvFscXCLvqfsHCrjrF7yiXsQuIVvVE7N82W3+aqpzuUdBbfhWcy/FZR3/4IgflMgKLOsvPDrGCJA==",
      "dev": true,
      "requires": {
        "once": "^1.3.0",
        "wrappy": "1"
      }
    },
    "inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "dev": true
    },
    "is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ=="
    },
    "is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "requires": {
        "is-extglob": "^2.1.1"
      }
    },
    "is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng=="
    },
    "merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg=="
    },
    "micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "requires": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      }
    },
    "minimatch": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz",
      "integrity": "sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==",
      "dev": true,
      "requires": {
        "brace-expansion": "^1.1.7"
      }
    },
    "minipass": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/minipass/-/minipass-5.0.0.tgz",
      "integrity": "sha512-3FnjYuehv9k6ovOEbyOswadCDPX1piCfhV8ncmYtHOjuPwylVWsghTLo7rabjC3Rx5xD4HDx8Wm1xnMF7S5qFQ==",
      "dev": true
    },
    "minizlib": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/minizlib/-/minizlib-2.1.2.tgz",
      "integrity": "sha512-bAxsR8BVfj60DWXHE3u30oHzfl4G7khkSuPW+qvpd7jFRHm7dLxOjUk1EHACJ/hxLY8phGJ0YhYHZo7jil7Qdg==",
      "dev": true,
      "requires": {
        "minipass": "^3.0.0",
        "yallist": "^4.0.0"
      },
      "dependencies": {
        "minipass": {
          "version": "3.3.6",
          "resolved": "https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz",
          "integrity": "sha512-DxiNidxSEK+tHG6zOIklvNOwm3hvCrbUrdtzY74U6HKTJxvIDfOUL5W5P2Ghd3DTkhhKPYGqeNUIh5qcM4YBfw==",
          "dev": true,
          "requires": {
            "yallist": "^4.0.0"
          }
        }
      }
    },
    "mkdirp": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-1.0.4.tgz",
      "integrity": "sha512-vVqVZQyf3WLx2Shd0qJ9xuvqgAyKPLAiqITEtqW0oIUjzo3PePDd6fW9iFz30ef7Ysp/oiWqbhszeGWW2T6Gzw==",
      "dev": true
    },
    "once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==",
      "dev": true,
      "requires": {
        "wrappy": "1"
      }
    },
    "path-is-absolute": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
      "integrity": "sha512-AVbw3UJ2e9bq64vSaS9Am0fje1Pa8pbGqTTsmXfaIiMpnr5DlDhfJOuLj9Sf95ZPVDAUerDfEk88MPmPe7UCQg==",
      "dev": true
    },
    "picomatch": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
      "integrity": "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA=="
    },
    "prettier": {
      "version": "2.8.4",
      "resolved": "https://registry.npmjs.org/prettier/-/prettier-2.8.4.tgz",
      "integrity": "sha512-vIS4Rlc2FNh0BySk3Wkd6xmwxB0FpOndW5fisM5H8hsZSxU2VWVB5CWIkIjWvrHjIhxk2g3bfMKM87zNTrZddw==",
      "dev": true
    },
    "queue-microtask": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
      "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A=="
    },
    "reusify": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
      "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw=="
    },
    "rimraf": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz",
      "integrity": "sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==",
      "dev": true,
      "requires": {
        "glob": "^7.1.3"
      }
    },
    "run-parallel": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
      "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
      "requires": {
        "queue-microtask": "^1.2.2"
      }
    },
    "tar": {
      "version": "6.2.1",
      "resolved": "https://registry.npmjs.org/tar/-/tar-6.2.1.tgz",
      "integrity": "sha512-DZ4yORTwrbTj/7MZYq2w+/ZFdI6OZ/f9SFHR+71gIVUZhOQPHzVCLpvRnPgyaMpfWxxk/4ONva3GQSyNIKRv6A==",
      "dev": true,
      "requires": {
        "chownr": "^2.0.0",
        "fs-minipass": "^2.0.0",
        "minipass": "^5.0.0",
        "minizlib": "^2.1.1",
        "mkdirp": "^1.0.3",
        "yallist": "^4.0.0"
      }
    },
    "to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "requires": {
        "is-number": "^7.0.0"
      }
    },
    "wasm-pack": {
      "version": "0.13.1",
      "resolved": "https://registry.npmjs.org/wasm-pack/-/wasm-pack-0.13.1.tgz",
      "integrity": "sha512-P9exD4YkjpDbw68xUhF3MDm/CC/3eTmmthyG5bHJ56kalxOTewOunxTke4SyF8MTXV6jUtNjXggPgrGmMtczGg==",
      "dev": true,
      "requires": {
        "binary-install": "^1.0.1"
      }
    },
    "wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
      "dev": true
    },
    "yallist": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz",
      "integrity": "sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==",
      "dev": true
    }
  }
}

```

## File: package.json
```
{
  "name": "@action-validator/root",
  "private": true,
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "workspaces": ["packages/*"],
  "scripts": {
    "build": "./scripts/build-wasm.sh",
    "build:dev": "WASM_PACK_BUILD_FLAGS='--no-opt' ./scripts/build-wasm.sh",
    "test": "./scripts/test-wasm.sh",
    "test:dev": "WASM_PACK_BUILD_FLAGS='--no-opt' ./scripts/test-wasm.sh",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "devDependencies": {
    "chalk": "5.2.0",
    "diff": "5.1.0",
    "prettier": "2.8.4",
    "wasm-pack": "0.13.1"
  }
}

```

## File: README.md
```
The `action-validator` is a standalone tool designed to "lint" the YAML files
used to define GitHub Actions and Workflows. It ensures that they are well-formed,
by checking them against published JSON schemas, and it makes sure that any
globs used in `paths` / `paths-ignore` match at least one file in the repo.

The intended use case for `action-validator` is in Git pre-commit hooks and
similar situations.


# Funding Development

I am currently experimenting with ways to fund development of new features in `action-validator`.
You can find more details of this approach at [the `action-validator` code fund page](https://hezmatt.org/~mpalmer/code-fund.html).


# Installation

We have many ways to install `action-validator`.

## Pre-built binaries

The [GitHub releases](https://github.com/mpalmer/action-validator/releases)
have some pre-built binaries -- just download and put them in your path. If a
binary for your platform isn't available, let me know and I'll see what I can
figure out.


## Using cargo

If you've got a Rust toolchain installed, running `cargo install action-validator` should give you the latest release.


## Using asdf

If you're a proponent of the [asdf tool](https://asdf-vm.com/), then you can
use that to install and manage `action-validator`:

```shell
asdf plugin add action-validator
# or
asdf plugin add action-validator https://github.com/mpalmer/action-validator.git
```

Install/configure action-validator:

```shell
# Show all installable versions
asdf list-all action-validator

# Install specific version
asdf install action-validator latest

# Set a version globally (on your ~/.tool-versions file)
asdf set -u action-validator latest

# Now action-validator commands are available
action-validator --help
```


# Using mise

If you are a passionate user of [mise](https://github.com/jdx/mise), then you can use that to install and manage `action-validator`:

No need to declare the plugin, it's already known by mise.

Install/configure action-validator:

```shell
# Show all installable versions
mise ls-remote action-validator

# Install specific version
mise install action-validator@latest

# Set a version globally (on your ~/.tool-versions or .mise.toml file)
mise use -g action-validator@latest

# Now action-validator commands are available
action-validator --help
```


## Using NPM

Node users can install the latest version using NPM:

> ℹ️ The `@action-validator/core` package can be used directly within Node.js applications.

```sh
npm install -g @action-validator/core @action-validator/cli --save-dev
```

## Building from the repo

If you want to build locally, you'll need to:

1. Checkout the git repository somewhere;

1. Grab the `SchemaStore` submodule, by running `git submodule init && git submodule update`;

1. Install a [Rust](https://rust-lang.org) toolchain; and then

1. run `cargo build`.


# Usage

Couldn't be simpler: just pass a file to the program:

```shell
action-validator .github/workflows/build.yml
```

Use `action-validator -h` to see additional options.


## In a GitHub Action

The action-validator can be run in a Github action itself, as a pull request job. See the `actions` job in the [QA workflow](https://github.com/mpalmer/action-validator/tree/main/.github/workflows/qa.yml), in this repository, as an example of how to use action-validator + asdf in a GitHub workflow.
This may seem a little redundant (after all, an action has to be valid in order for GitHub to run it), but this job will make sure that all your *other* actions are also valid.

Alternatively, use the [composite action](./action.yml) from this repository by adding this step to your job:

```yml
      - name: action-validator
        uses: mpalmer/action-validator@main # please lock to the latest SHA for secure use
        with:
          version: latest # also lock this to a semver without the v prefix for secure use and stability
```

## Using pre-commit

Update your .pre-commit-config.yaml:

```yaml
repos:
- repo: https://github.com/mpalmer/action-validator
  rev: v<version>
  hooks:
    - id: action-validator
```

## Pre-commit hook example

Create an executable file in the .git/hooks directory of the target repository:
`touch .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` and paste the following example code:

```bash
#!/bin/bash
if ! command -v action-validator >/dev/null; then
  echo "action-validator is not installed."
  echo "Installation instructions: https://github.com/mpalmer/action-validator"
  exit 1
fi
echo "Running pre-commit hook for GitHub Actions: https://github.com/mpalmer/action-validator"
scan_count=0
for action in $(git diff --cached --name-only --diff-filter=ACM | grep -E '^\.github/(workflows|actions)/.*\.ya?ml$'); do
  if action-validator "$action"; then
    echo "✅ $action"
  else
    echo "❌ $action"
    exit 1
  fi
  scan_count=$((scan_count+1))
done
echo "action-validator scanned $scan_count GitHub Actions and found no errors!"
```

This script will run on every commit to the target repository, whether the github action yaml files are being committed, or not and prevent any commit if there are linting errors.

```
# All action-validator linting errors must be resolved before any commit will succeed.
$ echo "" >> README.md && git add README.md && git commit -m "Update read-me"
Running pre-commit hook for GitHub Actions: https://github.com/mpalmer/action-validator
Validation failed: ValidationState {
    errors: [
        Properties {
            path: "",
            detail: "Additional property 'aname' is not allowed",
        },
    ],
    missing: [],
    replacement: None,
}
❌ .github/workflows/ci.yaml
Fatal error validating .github/workflows/ci.yaml: validation failed


# Fix error and try again
$ echo "" >> README.md && git add README.md && git commit -m "Update read-me"
Running pre-commit hook for GitHub Actions: https://github.com/mpalmer/action-validator
✅ .github/workflows/ci.yaml
✅ .github/workflows/release.yml
action-validator scanned 2 GitHub Actions found no errors!
[main c34fda3] Update read-me
 1 file changed, 2 insertions(+)
```

## NPM

Provided you have followed the [installation instructions for NPM](#using-npm), you can run the action
validator CLI as follows

```sh
npx action-validator <path_to_action_yaml>
```

Or, if you've installed the package globally:

```sh
action-validator <path_to_action_yaml>
```

The CLI distributed via NPM supports all the same options as the native binary.

## Node API

The Node API can be used to validate action and workflow files from Node.js as follows:

```ts
import { readFileSync } from "fs";
import { validateAction, validateWorkflow } from "@action-validator/core";

// Validate Action
const actionSource = readFileSync("action.yml", "utf8");
const state = validator.validateAction(actionSource);
const isValid = state.errors.length === 0;

// Validate Workflow
const workflowSource = readFileSync("workflow.yml", "utf8");
const state = validator.validateWorkflow(workflowSource);
const isValid = state.errors.length === 0;
```

# Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).


# Licence

Unless otherwise stated, everything in this repo is covered by the following
copyright notice:

    Copyright (C) 2021  Matt Palmer <matt@hezmatt.org>

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License version 3, as
    published by the Free Software Foundation.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_action-validator_133212



================================================
FILE: .prettierrc.json
================================================
{}


================================================
FILE: build.rs
================================================
fn main() {
    println!("cargo:rerun-if-changed=tests/fixtures");
}


================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Contributor Code of Conduct

As contributors and maintainers of this project, and in the interest of
fostering an open and welcoming community, we pledge to respect all people who
contribute through reporting issues, posting feature requests, updating
documentation, submitting pull requests or patches, and other activities.

We are committed to making participation in this project a harassment-free
experience for everyone, regardless of level of experience, gender, gender
identity and expression, sexual orientation, disability, personal appearance,
body size, race, ethnicity, age, religion, or nationality.

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery
* Personal attacks
* Trolling or insulting/derogatory comments
* Public or private harassment
* Publishing other's private information, such as physical or electronic
  addresses, without explicit permission
* Other unethical or unprofessional conduct

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

By adopting this Code of Conduct, project maintainers commit themselves to
fairly and consistently applying these principles to every aspect of managing
this project. Project maintainers who do not follow or enforce the Code of
Conduct may be permanently removed from the project team.

This code of conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community.

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting a project maintainer at mpalmer@hezmatt.org. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. Maintainers are
obligated to maintain confidentiality with regard to the reporter of an
incident.

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 1.3.0, available at
[http://contributor-covenant.org/version/1/3/0/][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/3/0/


================================================
FILE: CONTRIBUTING.md
================================================
# Overview

* If you have found a discrepancy in documented and observed behaviour, that
  is a bug. Feel free to [report it as an
  issue](https://github.com/mpalmer/action-validator/issues), providing
  sufficient detail to reproduce the problem.

* If you would like to add new behaviour, please submit a well-tested and
  well-documented [pull
  request](https://github.com/mpalmer/action-validator/pulls).

* At all times, abide by the Code of Conduct (CODE_OF_CONDUCT.md).

---

# Environment Setup

## Install Rust
Firstly, you'll need a Rust toolchain to make any changes to the core functionality of this project. We recommend [using `rustup`](https://www.rust-lang.org/tools/install), because that's what the Rust core team recommend.

To confirm that rust is installed, run the `cargo` command. If you don't receive the help docs output, you may need to add rust to your shell rc file.

## Git Submodule Setup
This repository uses [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Specifically for the use of [schemastore](https://github.com/SchemaStore/schemastore).

To setup the git submodule after cloning this repo to your local, you'll want to run the following commands:
1. `git submodule init`
2. `git submodule update`

It should look similar to the output below.

```bash
❯ git submodule init
Submodule 'src/schemastore' (https://github.com/SchemaStore/schemastore) registered for path 'src
/schemastore'
❯ git submodule update
Cloning into '/Users/someuser/action-validator/src/schemastore'...
Submodule path 'src/schemastore': checked out 'd3e6ab7727380b214acbab05570fb09a3e5d2dfc'
```

At this point, you should be all set to `cargo run`!

## Node/WASM Setup
If you plan to work on the WASM/Node bindings, you'll also need to install Node. We recommend using [NVM](https://github.com/nvm-sh/nvm) to install the Node version listed in `.nvmrc`.

Once Node is installed, run `npm install` at the root of the repository.

You should now be all set to run `npm build`, to build the Node/WASM bindings. Once built, run `npx action-validator` to run the CLI via the Node/WASM bindings.

# Running the Validator Locally

## `cargo run [FILE] -- [OPTIONS]`
`cargo run` will create a _debug_ executable and run the project. If this is your first time running the command, cargo will compile the development binary with `cargo build`. This will install all of the dependencies and create the debug binary `action-validator` in the `/target/debug/` directory. `cargo run` will then invoke this binary after creation.

One caveat if you're running with `cargo run`: if you want to supply the program with options, you need to use the `--` operator between `cargo run` and your provided options. This let's cargo know which flags are meant for cargo, and which are meant for the executable.

## `cargo build` && `./target/debug/action-validator [OPTIONS]`
As discussed in the prior section, `cargo build` install dependencies (if they're not cached) and build the development binary. This binary can then be invoked directly by running `./target/debug/action-validator`. This does **not** require the use of the `--` operator in between the binary and any provided options.

## Try It Yourself!

Run the command `cargo run -- --help`. You should see an output similar to the following.
```bash
❯ cargo run -- --help
    Finished dev [unoptimized + debuginfo] target(s) in 0.05s
     Running `target/debug/action-validator --help`
A validator for GitHub Action and Workflow YAML files

Usage: action-validator [OPTIONS] [path_to_action_yaml]...

Arguments:
  [path_to_action_yaml]...  Input file

Options:
  -v, --verbose  Be more verbose
  -h, --help     Print help information
  -V, --version  Print version information
```

# Writing Tests

All tests live in the `tests` directory. Currently, this project implements snapshot testing,
but that's not to say you couldn't write unit or integration tests with the current structure.
To run the tests, simply run `cargo test` from the root directory. If you want to test a specific
feature, you can add the `-F {feature}` flag (e.g. `cargo test -F remote-checks`).

## Unit/Integration Tests
As of this writing, there are no unit or integration tests. If you are looking to write some, please
follow the directions in [this guide](https://doc.rust-lang.org/book/ch11-01-writing-tests.html).

## Snapshot Tests
A snapshot test is performed when we execute the cli and capture `stdout`, `stderr`, and/or an exit code.
When the tests are run, the results of the test must exactly match those of the previous run. For this project,
the snapshot tests are named in the format `{next_id}_{whats_being_tested}` (e.g. `011_remote_checks_failure`).

If you have made changes which will change the output of the program and cause snapshots to fail, you can run
`cargo test -F test-save-snapshots`. This feature causes the executed command to save the `stdout`, `stderr`, and/or
exit code to the specified testing directory.

If yo

================================================
FILE: package-lock.json
================================================
{
  "name": "@action-validator/root",
  "version": "0.0.0-git",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "@action-validator/root",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "workspaces": [
        "packages/*"
      ],
      "devDependencies": {
        "chalk": "5.2.0",
        "diff": "5.1.0",
        "prettier": "2.8.4",
        "wasm-pack": "0.13.1"
      }
    },
    "node_modules/@action-validator/cli": {
      "resolved": "packages/cli",
      "link": true
    },
    "node_modules/@action-validator/core": {
      "resolved": "packages/core",
      "link": true
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/axios": {
      "version": "0.26.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-0.26.1.tgz",
      "integrity": "sha512-fPwcX4EvnSHuInCMItEhAGnaSEXRBjtzh9fOtsE6E1G6p7vl7edEeZe11QHf18+6+9gR5PbKV/sGKNaD8YaMeA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "follow-redirects": "^1.14.8"
      }
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/binary-install": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/binary-install/-/binary-install-1.1.0.tgz",
      "integrity": "sha512-rkwNGW+3aQVSZoD0/o3mfPN6Yxh3Id0R/xzTVBVVpGNlVz8EGwusksxRlbk/A5iKTZt9zkMn3qIqmAt3vpfbzg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "axios": "^0.26.1",
        "rimraf": "^3.0.2",
        "tar": "^6.1.11"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/brace-expansion": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz",
      "integrity": "sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/chalk": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
      "integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA==",
      "dev": true,
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/chownr": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz",
      "integrity": "sha512-bIomtDF5KGpdogkLd9VspvFzk9KfpyyGlS8YFVZl7TGPBHL5snIOnxeshwVgPteQ9b4Eydl+pVbIyE1DcvCWgQ==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/

================================================
FILE: package.json
================================================
{
  "name": "@action-validator/root",
  "private": true,
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "workspaces": ["packages/*"],
  "scripts": {
    "build": "./scripts/build-wasm.sh",
    "build:dev": "WASM_PACK_BUILD_FLAGS='--no-opt' ./scripts/build-wasm.sh",
    "test": "./scripts/test-wasm.sh",
    "test:dev": "WASM_PACK_BUILD_FLAGS='--no-opt' ./scripts/test-wasm.sh",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "devDependencies": {
    "chalk": "5.2.0",
    "diff": "5.1.0",
    "prettier": "2.8.4",
    "wasm-pack": "0.13.1"
  }
}


================================================
FILE: README.md
================================================
The `action-validator` is a standalone tool designed to "lint" the YAML files
used to define GitHub Actions and Workflows. It ensures that they are well-formed,
by checking them against published JSON schemas, and it makes sure that any
globs used in `paths` / `paths-ignore` match at least one file in the repo.

The intended use case for `action-validator` is in Git pre-commit hooks and
similar situations.


# Funding Development

I am currently experimenting with ways to fund development of new features in `action-validator`.
You can find more details of this approach at [the `action-validator` code fund page](https://hezmatt.org/~mpalmer/code-fund.html).


# Installation

We have many ways to install `action-validator`.

## Pre-built binaries

The [GitHub releases](https://github.com/mpalmer/action-validator/releases)
have some pre-built binaries -- just download and put them in your path. If a
binary for your platform isn't available, let me know and I'll see what I can
figure out.


## Using cargo

If you've got a Rust toolchain installed, running `cargo install action-validator` should give you the latest release.


## Using asdf

If you're a proponent of the [asdf tool](https://asdf-vm.com/), then you can
use that to install and manage `action-validator`:

```shell
asdf plugin add action-validator
# or
asdf plugin add action-validator https://github.com/mpalmer/action-validator.git
```

Install/configure action-validator:

```shell
# Show all installable versions
asdf list-all action-validator

# Install specific version
asdf install action-validator latest

# Set a version globally (on your ~/.tool-versions file)
asdf set -u action-validator latest

# Now action-validator commands are available
action-validator --help
```


# Using mise

If you are a passionate user of [mise](https://github.com/jdx/mise), then you can use that to install and manage `action-validator`:

No need to declare the plugin, it's already known by mise.

Install/configure action-validator:

```shell
# Show all installable versions
mise ls-remote action-validator

# Install specific version
mise install action-validator@latest

# Set a version globally (on your ~/.tool-versions or .mise.toml file)
mise use -g action-validator@latest

# Now action-validator commands are available
action-validator --help
```


## Using NPM

Node users can install the latest version using NPM:

> ℹ️ The `@action-validator/core` package can be used directly within Node.js applications.

```sh
npm install -g @action-validator/core @action-validator/cli --save-dev
```

## Building from the repo

If you want to build locally, you'll need to:

1. Checkout the git repository somewhere;

1. Grab the `SchemaStore` submodule, by running `git submodule init && git submodule update`;

1. Install a [Rust](https://rust-lang.org) toolchain; and then

1. run `cargo build`.


# Usage

Couldn't be simpler: just pass a file to the program:

```shell
action-validator .github/workflows/build.yml
```

Use `action-validator -h` to see additional options.


## In a GitHub Action

The action-validator can be run in a Github action itself, as a pull request job. See the `actions` job in the [QA workflow](https://github.com/mpalmer/action-validator/tree/main/.github/workflows/qa.yml), in this repository, as an example of how to use action-validator + asdf in a GitHub workflow.
This may seem a little redundant (after all, an action has to be valid in order for GitHub to run it), but this job will make sure that all your *other* actions are also valid.

Alternatively, use the [composite action](./action.yml) from this repository by adding this step to your job:

```yml
      - name: action-validator
        uses: mpalmer/action-validator@main # please lock to the latest SHA for secure use
        with:
          version: latest # also lock this to a semver without the v prefix for secure use and stability
```

## Using pre-commit

Update your .pre-commit-config.yaml:

```yaml
repos:
- repo: https://github.com/mpalmer/action-validator
  rev: v<version>
  hooks:
    - id: action-validator
```

## Pre-commit hook example

Create an executable file in the .git/hooks directory of the target repository:
`touch .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` and paste the following example code:

```bash
#!/bin/bash
if ! command -v action-validator >/dev/null; then
  echo "action-validator is not installed."
  echo "Installation instructions: https://github.com/mpalmer/action-validator"
  exit 1
fi
echo "Running pre-commit hook for GitHub Actions: https://github.com/mpalmer/action-validator"
scan_count=0
for action in $(git diff --cached --name-only --diff-filter=ACM | grep -E '^\.github/(workflows|actions)/.*\.ya?ml$'); do
  if action-validator "$action"; then
    echo "✅ $action"
  else
    echo "❌ $action"
    exit 1
  fi
  scan_count=$((scan_count+1))
done
echo "action-validator scanned $scan_count GitHub Actions and found no errors!"
```

This script will run on every

================================================
FILE: packages\cli\package-lock.json
================================================
{
  "name": "@action-validator/cli",
  "version": "0.0.0-git",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "@action-validator/cli",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "dependencies": {
        "chalk": "5.2.0"
      },
      "bin": {
        "action-validator": "cli.mjs"
      },
      "devDependencies": {
        "@action-validator/core": "file:../core"
      },
      "peerDependencies": {
        "@action-validator/core": "0.0.0-git"
      }
    },
    "../core": {
      "name": "@action-validator/core",
      "version": "0.0.0-git",
      "dev": true,
      "license": "GPL-3.0-only"
    },
    "node_modules/@action-validator/core": {
      "resolved": "../core",
      "link": true
    },
    "node_modules/chalk": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
      "integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA==",
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    }
  },
  "dependencies": {
    "@action-validator/core": {
      "version": "file:../core"
    },
    "chalk": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
      "integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA=="
    }
  }
}


================================================
FILE: packages\cli\package.json
================================================
{
  "name": "@action-validator/cli",
  "collaborators": [
    "Matt Palmer <matt@hezmatt.org>",
    "Ben Heidemann <ben@heidemann.co.uk>"
  ],
  "description": "Validator for GitHub action and workflow YAML files",
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "repository": {
    "type": "git",
    "url": "https://github.com/mpalmer/action-validator"
  },
  "files": [
    "cli.mjs"
  ],
  "main": "cli.js",
  "homepage": "https://github.com/mpalmer/action-validator",
  "bin": {
    "action-validator": "./cli.mjs"
  },
  "scripts": {
    "build": "npx wasm-pack build --out-dir target/wasm-pack/build --no-typescript --target nodejs --features js && cp target/wasm-pack/build/action_validator_bg.wasm dist/ && cp target/wasm-pack/build/action_validator.js dist/ && cp target/wasm-pack/build/action_validator.js dist/",
    "test": "node test/run.mjs",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "dependencies": {},
  "devDependencies": {
    "@action-validator/core": "file:../core"
  },
  "peerDependencies": {
    "@action-validator/core": "0.0.0-git"
  }
}


================================================
FILE: packages\core\action_validator.d.ts
================================================
export type ParseErrorLocation = {
  index: number;
  line: number;
  column: number;
};

export type ValidationError =
  | {
      code: string;
      detail?: string;
      path: string;
      title: string;
      states?: Omit<ValidationState, "actionType">[];
    }
  | {
      code: string;
      detail: string;
      title: string;
      location?: ParseErrorLocation;
    };

export type ValidationState = {
  actionType: "action" | "workflow";
  errors: ValidationError[];
};

export function main(args: string[]): never;
export function validateAction(src: string): ValidationState;
export function validateWorkflow(src: string): ValidationState;


================================================
FILE: packages\core\package-lock.json
================================================
{
  "name": "@action-validator/core",
  "version": "0.0.0-git",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "@action-validator/core",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "dependencies": {
        "fast-glob": "^3.3.3"
      }
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      },
      "engines": {
        "node": ">=8.6.0"
      }
    },
    "node_modules/fastq": {
      "version": "1.19.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz",
      "integrity": "sha512-GwLTyxkCXjXbxqIhTsMI2Nui8huMPtnxg7krajPJAjnEG/iiOS7i+zCtWGZR9G0NBKbXKh6X9m9UIsYX/N6vvQ==",
      "license": "ISC",
      "dependencies": {
        "reusify": "^1.0.4"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "license": "MIT",
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "license": "MIT",
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
      "license": "MIT",
 

================================================
FILE: packages\core\package.json
================================================
{
  "name": "@action-validator/core",
  "collaborators": [
    "Matt Palmer <matt@hezmatt.org>",
    "Ben Heidemann <ben@heidemann.co.uk>"
  ],
  "description": "Validator for GitHub action and workflow YAML files",
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "repository": {
    "type": "git",
    "url": "https://github.com/mpalmer/action-validator"
  },
  "files": [
    "action_validator_bg.wasm",
    "action_validator.js",
    "action_validator.d.ts"
  ],
  "main": "action_validator.js",
  "homepage": "https://github.com/mpalmer/action-validator",
  "types": "action_validator.d.ts",
  "scripts": {
    "build": "npx wasm-pack build --out-dir target/wasm-pack/build --no-typescript --target nodejs --features js && cp target/wasm-pack/build/action_validator_bg.wasm dist/ && cp target/wasm-pack/build/action_validator.js dist/ && cp target/wasm-pack/build/action_validator.js dist/",
    "test": "node test/run.mjs",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "dependencies": {
    "fast-glob": "^3.3.3"
  }
}


================================================
FILE: src\config.rs
================================================
use clap::Parser;
use serde::Serialize;
use std::path::PathBuf;

#[derive(Parser, Debug)]
#[command(
    name = "action-validator",
    about = "A validator for GitHub Action and Workflow YAML files",
    version
)]
pub struct CliConfig {
    /// Be more verbose
    #[arg(short, long)]
    pub verbose: bool,

    #[arg(
        long,
        help = "Use specified dir as root of glob matching, rather than the current directory"
    )]
    pub rootdir: Option<PathBuf>,

    /// Input file
    #[arg(name = "path_to_action_yaml")]
    pub src: Vec<PathBuf>,
}

#[derive(Serialize, Copy, Clone, Debug)]
pub enum ActionType {
    #[serde(rename = "action")]
    Action,
    #[serde(rename = "workflow")]
    Workflow,
}

pub struct JsConfig<'a> {
    pub action_type: ActionType,
    pub src: &'a str,
    pub verbose: bool,
}

pub struct RunConfig<'a> {
    pub file_path: Option<&'a str>,
    pub file_name: Option<&'a str>,
    pub action_type: ActionType,
    pub src: &'a str,
    pub verbose: bool,
    pub rootdir: Option<PathBuf>,
}

impl<'a> From<&JsConfig<'a>> for RunConfig<'a> {
    fn from(config: &JsConfig<'a>) -> Self {
        RunConfig {
            file_path: None,
            file_name: None,
            action_type: config.action_type,
            src: config.src,
            verbose: config.verbose,
            rootdir: None,
        }
    }
}


================================================
FILE: src\lib.rs
================================================
mod config;
mod schemas;
mod system;
mod utils;
mod validation_error;
mod validation_state;

use config::{ActionType, RunConfig};
use std::path::PathBuf;
use validation_error::ValidationError;
use validation_state::ValidationState;

pub use crate::config::CliConfig;
use crate::schemas::{validate_as_action, validate_as_workflow};

#[cfg(feature = "js")]
mod js {
    use super::cli;
    use crate::config::CliConfig;
    use crate::system;
    use crate::{
        config::{ActionType, JsConfig},
        utils::set_panic_hook,
    };
    use clap::Parser as _;
    use js_sys::Array;
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(js_name = main)]
    pub fn main(args: Array) -> JsValue {
        set_panic_hook();

        let rust_args: Vec<String> = args
            .iter()
            .map(|arg| arg.as_string().unwrap_or_default())
            .collect();

        let config = match CliConfig::try_parse_from(rust_args) {
            Ok(config) => config,
            Err(error) => {
                let error_text = if system::process::stdout::is_tty() {
                    format!("{}", error.render().ansi())
                } else {
                    error.render().to_string()
                };
                system::console::error(&error_text);
                system::process::exit(error.exit_code());
            }
        };

        if matches!(cli::run(&config), cli::RunResult::Failure) {
            system::process::exit(1);
        }

        system::process::exit(0);
    }

    #[wasm_bindgen(js_name = validateAction)]
    pub fn validate_action(src: &str) -> JsValue {
        set_panic_hook();

        let config = JsConfig {
            action_type: ActionType::Action,
            src,
            verbose: false,
        };

        run(&config)
    }

    #[wasm_bindgen(js_name = validateWorkflow)]
    pub fn validate_workflow(src: &str) -> JsValue {
        set_panic_hook();

        let config = JsConfig {
            action_type: ActionType::Workflow,
            src,
            verbose: false,
        };

        run(&config)
    }

    fn run(config: &JsConfig) -> JsValue {
        let run_config = config.into();
        let state = crate::run(&run_config);
        serde_wasm_bindgen::to_value(&state).unwrap()
    }
}

pub mod cli {
    use crate::{
        config::{ActionType, RunConfig},
        system, CliConfig,
    };

    pub enum RunResult {
        Success,
        Failure,
    }

    pub fn run(config: &CliConfig) -> RunResult {
        let mut success = true;

        for path in &config.src {
            let file_name = match path.file_name() {
                Some(file_name) => file_name.to_str(),
                None => {
                    eprintln!("Unable to derive file name from src!");
                    success = false;
                    continue;
                }
            };

            let src = &match system::fs::read_to_string(path) {
                Ok(src) => src,
                Err(err) => {
                    system::console::error(&format!(
                        "Unable to read file {}: {err}",
                        path.display()
                    ));
                    success = false;
                    continue;
                }
            };

            let config = RunConfig {
                file_path: Some(path.to_str().unwrap()),
                file_name,
                action_type: match file_name {
                    Some("action.yml") | Some("action.yaml") => ActionType::Action,
                    _ => ActionType::Workflow,
                },
                src,
                verbose: config.verbose,
                rootdir: config.rootdir.clone(),
            };

            let state = crate::run(&config);

            if !state.is_valid() {
                let fmt_state = format!("{state:#?}");
                let path = state.file_path.unwrap_or("file".into());
                system::console::log(&format!("Fatal error validating {path}"));
                system::console::error(&format!("Validation failed: {fmt_state}"));
                success = false;
            }
        }

        if success {
            RunResult::Success
        } else {
            RunResult::Failure
        }
    }
}

fn run(config: &RunConfig) -> ValidationState {
    let file_name = config.file_name.unwrap_or("file");
    let doc = yaml_serde::from_str(config.src);

    let mut state = match doc {
        Err(err) => ValidationState {
            action_type: Some(config.action_type),
            file_path: Some(file_name.to_string()),
            errors: vec![err.into()],
        },
        Ok(doc) => match config.action_type {
            ActionType::Action => {
                if config.verbose {
                    system::console::log(&format!("Treating {file_name} as an Action definition"));
                }
                validate_as_action(&doc)
            }
            ActionType::Workflow => {
                if config

================================================
FILE: src\main.rs
================================================
#[cfg(feature = "js")]
fn main() {}

#[cfg(not(feature = "js"))]
fn main() {
    use action_validator::CliConfig;
    use clap::Parser;
    use std::process;

    let config = CliConfig::parse();

    if matches!(
        action_validator::cli::run(&config),
        action_validator::cli::RunResult::Failure
    ) {
        process::exit(1);
    }
}


================================================
FILE: src\schemas.rs
================================================
use serde_json::Value;

use crate::validation_state::ValidationState;

pub fn validate_as_action(doc: &Value) -> ValidationState {
    validate_with_schema(
        doc,
        include_bytes!("schemastore/src/schemas/json/github-action.json"),
    )
}

pub fn validate_as_workflow(doc: &Value) -> ValidationState {
    validate_with_schema(
        doc,
        include_bytes!("schemastore/src/schemas/json/github-workflow.json"),
    )
}

fn validate_with_schema(doc: &Value, schema: &[u8]) -> ValidationState {
    let schema_json: serde_json::Value =
        serde_json::from_str(String::from_utf8_lossy(schema).as_ref()).unwrap();

    let mut scope = valico::json_schema::Scope::new();
    let validator = scope.compile_and_return(schema_json, false).unwrap();

    validator.validate(doc).into()
}


================================================
FILE: src\utils.rs
================================================
#[cfg(feature = "js")]
pub fn set_panic_hook() {
    // When the `console_error_panic_hook` feature is enabled, we can call the
    // `set_panic_hook` function at least once during initialization, and then
    // we will get better error messages if our code ever panics.
    //
    // For more details see
    // https://github.com/rustwasm/console_error_panic_hook#readme
    #[cfg(feature = "console_error_panic_hook")]
    console_error_panic_hook::set_once();
}


================================================
FILE: src\validation_error.rs
================================================
use serde::Serialize;
use valico::common::error::ValicoError;

use crate::validation_state::ValidationState;

type BoxedValicoError = Box<dyn ValicoError>;

#[derive(Serialize, Debug)]
pub struct ParseErrorLocation {
    pub index: usize,
    pub line: usize,
    pub column: usize,
}

impl From<yaml_serde::Location> for ParseErrorLocation {
    fn from(location: yaml_serde::Location) -> Self {
        ParseErrorLocation {
            index: location.index(),
            line: location.line(),
            column: location.column(),
        }
    }
}

macro_rules! validation_errors {
    ($( $name:ident $( { $($fields:tt)* } )? ),*) => {
        #[derive(Serialize, Debug)]
        #[serde(untagged)]
        #[allow(dead_code)] // JS doesn't instantiate some of the validation errors at present
        pub enum ValidationError {
            $(
                $name {
                    code: String,
                    detail: Option<String>,
                    path: String,
                    title: String,
                    $( $($fields)* )?
                },
            )*
        }
    };
}

validation_errors!(
    // Schema Validation Errors
    WrongType,
    MultipleOf,
    Maximum,
    Minimum,
    MaxLength,
    MinLength,
    Pattern,
    MaxItems,
    MinItems,
    UniqueItems,
    Items,
    MaxProperties,
    MinProperties,
    Required,
    Properties,
    Enum,
    AnyOf { states: Vec<ValidationState> },
    OneOf { states: Vec<ValidationState> },
    Const,
    Contains,
    ContainsMinMax,
    Not,
    DivergentDefaults,
    Format,
    Unevaluated,
    Unknown,
    // Other Validation Errors
    UnresolvedJob,
    InvalidGlob,
    NoFilesMatchingGlob,
    // Other Errors
    Parse { location: Option<ParseErrorLocation> }
);

macro_rules! impl_from_valico_error {
    ($($err:ident => $name:ident $( { $($fields:tt)* } )? ),*) => {
        impl From<&BoxedValicoError> for ValidationError {
            fn from(err: &BoxedValicoError) -> Self {
                if false {
                    unreachable!()
                }
                $(
                    else if let Some($err) = err.downcast_ref::<valico::json_schema::errors::$name>() {
                        ValidationError::$name {
                            code: $err.get_code().into(),
                            path: $err.get_path().into(),
                            title: $err.get_title().into(),
                            detail: $err.get_detail().map(|s| s.into()),
                            $( $($fields)* )?
                        }
                    }
                )*
                else {
                    ValidationError::Unknown {
                        code: err.get_code().into(),
                        path: err.get_path().into(),
                        title: err.get_title().into(),
                        detail: err.get_detail().map(|s| s.into()),
                    }
                }
            }
        }
    };
}

impl_from_valico_error!(
    err => WrongType,
    err => MultipleOf,
    err => Maximum,
    err => Minimum,
    err => MaxLength,
    err => MinLength,
    err => Pattern,
    err => MaxItems,
    err => MinItems,
    err => UniqueItems,
    err => Items,
    err => MaxProperties,
    err => MinProperties,
    err => Required,
    err => Properties,
    err => Enum,
    err => AnyOf { states: err.states.iter().map(ValidationState::from).collect() },
    err => OneOf { states: err.states.iter().map(ValidationState::from).collect() },
    err => Const,
    err => Contains,
    err => ContainsMinMax,
    err => Not,
    err => DivergentDefaults,
    err => Format,
    err => Unevaluated
);

impl From<yaml_serde::Error> for ValidationError {
    fn from(err: yaml_serde::Error) -> Self {
        ValidationError::Parse {
            code: "parse_error".into(),
            detail: Some(err.to_string()),
            location: err.location().map(ParseErrorLocation::from),
            path: "".into(),
            title: "Parse Error".into(),
        }
    }
}


================================================
FILE: src\validation_state.rs
================================================
use serde::Serialize;

use crate::{config::ActionType, validation_error::ValidationError};

#[derive(Serialize, Debug)]
pub struct ValidationState {
    #[serde(rename = "actionType")]
    pub action_type: Option<ActionType>,
    #[serde(rename = "filePath")]
    pub file_path: Option<String>,
    pub errors: Vec<ValidationError>,
}

impl ValidationState {
    pub fn is_valid(&self) -> bool {
        self.errors.is_empty()
    }
}

impl From<valico::json_schema::ValidationState> for ValidationState {
    fn from(state: valico::json_schema::ValidationState) -> Self {
        ValidationState {
            file_path: None,
            action_type: None,
            errors: state.errors.iter().map(|err| err.into()).collect(),
        }
    }
}

impl From<&valico::json_schema::ValidationState> for ValidationState {
    fn from(state: &valico::json_schema::ValidationState) -> Self {
        ValidationState {
            file_path: None,
            action_type: None,
            errors: state.errors.iter().map(|err| err.into()).collect(),
        }
    }
}


================================================
FILE: src\js\system.js
================================================
const console = require('node:console');
const fs = require('node:fs');
const process = require('node:process');
const fg = require('fast-glob');

module.exports.console = console;
module.exports.fs = fs;
module.exports.process = process;
module.exports.fg = fg;


================================================
FILE: src\system\console.rs
================================================
#[cfg(feature = "js")]
mod js_console {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(js_namespace = console, js_name = log)]
        pub fn log(s: &str);

        #[wasm_bindgen(js_namespace = console, js_name = error)]
        pub fn error(s: &str);
    }
}

#[cfg(feature = "js")]
pub fn log(s: &str) {
    js_console::log(s);
}

#[cfg(not(feature = "js"))]
pub fn log(s: &str) {
    println!("{s}");
}

#[cfg(feature = "js")]
pub fn error(s: &str) {
    js_console::error(s);
}

#[cfg(not(feature = "js"))]
pub fn error(s: &str) {
    eprintln!("{s}");
}


================================================
FILE: src\system\fs.rs
================================================
use std::path::Path;

#[cfg(feature = "js")]
mod js_fs {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(catch, js_namespace = fs, js_name = readFileSync)]
        pub fn read_file_sync(path: &str, encoding: &str) -> Result<String, js_sys::Error>;
    }
}

#[cfg(feature = "js")]
pub fn read_to_string<P>(path: P) -> Result<String, String>
where
    P: AsRef<Path>,
{
    js_fs::read_file_sync(path.as_ref().to_string_lossy().as_ref(), "utf8")
        .map_err(|e| format!("{}", e.to_string()))
}

#[cfg(not(feature = "js"))]
pub fn read_to_string<P>(path: P) -> Result<String, String>
where
    P: AsRef<Path>,
{
    std::fs::read_to_string(path).map_err(|e| e.to_string())
}


================================================
FILE: src\system\git.rs
================================================
use std::process::Command;

pub fn ls_files() -> Result<Vec<String>, std::io::Error> {
    let output = Command::new("git").args(["ls-files", "-z"]).output()?;

    if !output.status.success() {
        return Err(std::io::Error::other(format!(
            "git ls-files failed: {}",
            String::from_utf8_lossy(&output.stderr)
        )));
    }

    let files = String::from_utf8_lossy(&output.stdout)
        .split('\0')
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    Ok(files)
}


================================================
FILE: src\system\mod.rs
================================================
pub mod console;
pub mod fs;
pub mod git;
pub mod process;


================================================
FILE: src\system\process.rs
================================================
#[cfg(feature = "js")]
mod js_process {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(js_namespace = process, js_name = exit)]
        pub fn exit(code: i32) -> JsValue;

        #[wasm_bindgen(thread_local_v2, js_namespace = ["process", "stdout"], js_name = isTTY)]
        pub static STDOUT_IS_TTY: bool;
    }
}

#[cfg(feature = "js")]
pub fn exit(code: i32) -> ! {
    js_process::exit(code);
    unreachable!();
}

pub mod stdout {
    #[cfg(feature = "js")]
    pub fn is_tty() -> bool {
        use super::js_process;
        js_process::STDOUT_IS_TTY.with(bool::clone)
    }
}


================================================
FILE: tests\snapshot_tests.rs
================================================
use fixtures::fixtures;
use std::env::current_dir;
use std::fs::File;
use std::io::BufReader;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::{ffi::OsStr, fs};

static REPO_DIR_WILDCARD: &str = "{{repo}}";

#[derive(Debug, serde::Deserialize)]
struct SnapshotTestConfig {
    cli_args: Option<Vec<String>>,
}

#[derive(Debug)]
struct SnapshotTest {
    config: SnapshotTestConfig,
    current_dir: PathBuf,
    test_dir: PathBuf,
}

impl SnapshotTest {
    fn new(test_dir: &Path) -> Self {
        let test_config_file = test_dir.join("test.json");

        let config: SnapshotTestConfig = serde_json::from_reader(BufReader::new(
            File::open(&test_config_file).expect(&format!(
                "missing test conifg file ({})",
                test_config_file.to_string_lossy(),
            )),
        ))
        .expect(&format!(
            "invalid test config file ({})",
            test_config_file.to_string_lossy(),
        ));

        SnapshotTest {
            config,
            current_dir: current_dir().unwrap(),
            test_dir: test_dir.to_path_buf(),
        }
    }

    fn build_command(&self) -> Command {
        #[cfg(not(feature = "test-js"))]
        {
            Command::new(assert_cmd::cargo::cargo_bin!())
        }

        #[cfg(feature = "test-js")]
        {
            let mut cmd = Command::new("node");
            cmd.arg("packages/cli/cli.mjs");
            cmd
        }
    }

    fn execute(self) {
        use std::ffi::OsString;

        let pwd = self.current_dir.to_str().unwrap();

        let cli_args: Vec<_> = if let Some(cli_args) = &self.config.cli_args {
            cli_args.iter().map(OsString::from).collect()
        } else {
            fs::read_dir(&self.test_dir)
                .unwrap()
                .filter_map(Result::ok)
                .filter(|f| f.path().extension() == Some(OsStr::new("yml")))
                .map(|f| f.path().into_os_string())
                .collect()
        };

        #[cfg(not(feature = "test-save-snapshots"))]
        {
            use assert_cmd::assert::OutputAssertExt as _;

            let stderr = fs::read_to_string(self.test_dir.join("stderr"))
                .unwrap_or(String::from(""))
                .replace(REPO_DIR_WILDCARD, pwd);

            let stdout = fs::read_to_string(self.test_dir.join("stdout"))
                .unwrap_or(String::from(""))
                .replace(REPO_DIR_WILDCARD, pwd);

            let exitcode: i32 = fs::read_to_string(self.test_dir.join("exitcode"))
                .map(|s| {
                    s.strip_suffix("\n")
                        .unwrap_or(s.as_str())
                        .parse::<i32>()
                        .unwrap_or(0)
                })
                .unwrap_or(0);

            self.build_command()
                .args(&cli_args)
                .assert()
                .stdout(stdout)
                .stderr(stderr)
                .code(exitcode);
        }

        #[cfg(feature = "test-save-snapshots")]
        {
            use assert_cmd::output::OutputOkExt as _;
            use std::io::prelude::*;

            let result = self
                .build_command()
                .args(&cli_args)
                .ok()
                .unwrap_or_else(|e| e.as_output().unwrap().to_owned());

            if !result.stdout.is_empty() {
                File::create(self.test_dir.join("stdout"))
                    .unwrap()
                    .write_all(
                        String::from_utf8(result.stdout)
                            .unwrap()
                            .replace(pwd, REPO_DIR_WILDCARD)
                            .as_bytes(),
                    )
                    .unwrap();
            }
            if !result.stderr.is_empty() {
                File::create(self.test_dir.join("stderr"))
                    .unwrap()
                    .write_all(
                        String::from_utf8(result.stderr)
                            .unwrap()
                            .replace(pwd, REPO_DIR_WILDCARD)
                            .as_bytes(),
                    )
                    .unwrap();
            }
            if let Some(exitcode) = result.status.code() {
                if exitcode > 0 {
                    File::create(self.test_dir.join("exitcode"))
                        .unwrap()
                        .write_all(exitcode.to_string().as_bytes())
                        .unwrap();
                }
            }
        }
    }
}

#[fixtures(["tests/fixtures/*"])]
#[cfg_attr(
    feature = "test-js",
    fixtures::ignore(
        paths = "tests/fixtures/013_rejects_gitignore_extended_glob_syntax",
        reason = "The WASM implementation of action validator currently (incorrectly) accepts extended gitignore syntax"
    )
)]
#[test]
fn snapshot(dir: &Path) {
    SnapshotTest::new(dir).execute();
}


================================================
FILE: tests\fixtures\001_basic_workflow\test.json
================================================
{}


================================================
FILE: tests\fixtures\002_basic_action\test.json
================================================
{}


================================================
FILE: tests\fixtures\003_successful_globs\excluded_path.json
================================================
{}


================================================
FILE: tests\fixtures\003_successful_globs\test.json
================================================
{}


================================================
FILE: tests\fixtures\004a_failing_negative_glob\test.json
================================================
{}


================================================
FILE: tests\fixtures\004_failing_globs\test.json
================================================
{}


================================================
FILE: tests\fixtures\005_conditional_step_in_action\test.json
================================================
{}


================================================
FILE: tests\fixtures\006_workflow_dispatch_inputs_options\test.json
================================================
{}


================================================
FILE: tests\fixtures\007_funky_syntax\test.json
================================================
{}


================================================
FILE: tests\fixtures\008_job_dependencies\test.json
================================================
{}


================================================
FILE: tests\fixtures\009_multi_file\test.json
================================================
{}


================================================
FILE: tests\fixtures\010_missing_shell_in_action\test.json
================================================
{}


================================================
FILE: tests\fixtures\011_subdir_globs\test.json
================================================
{
  "cli_args": ["--rootdir", "tests/fixtures/011_subdir_globs/subdir", "tests/fixtures/011_subdir_globs/subdir/glob.yml"]
}


================================================
FILE: tests\fixtures\011_subdir_globs\subdir\dummy.json
================================================


================================================
FILE: tests\fixtures\012_github_glob_syntax\test.json
================================================
{}


================================================
FILE: tests\fixtures\013_rejects_gitignore_extended_glob_syntax\test.json
================================================
{}


================================================
FILE: tests\fixtures\013_rejects_gitignore_extended_glob_syntax\subdir\asset.js
================================================

```

## File: .github\dependabot.yml
```
# Set update schedule for GitHub Actions
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"

```

## File: .github\FUNDING.yml
```
# These are supported funding model platforms

github: # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: tobermorytech
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
lfx_crowdfunding: # Replace with a single LFX Crowdfunding project-name e.g., cloud-foundry
polar: # Replace with a single Polar username
buy_me_a_coffee: # Replace with a single Buy Me a Coffee username
thanks_dev: # Replace with a single thanks.dev username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']

```

## File: .github\workflows\audit.yml
```
name: Periodic audit
on:
  schedule:
    - cron: "0 0 * * *"
  push:
    paths:
      - "**/Cargo.*"
      - ".github/workflows/audit.yml"
  pull_request:
    branches:
      - main

jobs:
  security_audit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@stable

      - name: Cache
        uses: Swatinem/rust-cache@e172ef532f714507ca8b9ce7978a442736438fc1 # v2.9.0

      - name: Install cargo-audit
        run: cargo install cargo-audit --locked

      - name: Audit deps
        run: |
          cargo audit -D warnings

  nightly_compat:
    name: See if future Rust versions (or deps) will break anything
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@nightly
        with:
          components: clippy

      # Normally this would be where we use actions/cache, but since nightly
      # is likely to change on every run, it doesn't seem worth it

      - name: Update deps
        run: |
          cargo +${{ steps.rust-install.outputs.name }} update

      - name: Test
        env:
          RUSTFLAGS: -D warnings
        run: |
          cargo +${{ steps.rust-install.outputs.name }} test
          cargo +${{ steps.rust-install.outputs.name }} test --all-features

      - name: Clippy
        run: |
          cargo +${{ steps.rust-install.outputs.name }} clippy -- -D warnings
          cargo +${{ steps.rust-install.outputs.name }} clippy --all-features -- -D warnings

  nightly_compat_node:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@nightly

      - name: Update deps
        run: |
          cargo +${{ steps.rust-install.outputs.name }} update

      - name: Setup Node
        uses: actions/setup-node@53b83947a5a98c8d113130e565377fae1a50d02f # v6.3.0
        with:
          cache: npm
          node-version: 26-nightly

      - name: Update Dependencies
        run: npm update

      - name: Install Dependencies
        run: npm install

      - name: Build
        run: npm run build
        # nodejs support is experimental; don't fail the build for it
        continue-on-error: true

      - name: Test
        run: npm test
        # nodejs support is experimental; don't fail the build for it
        continue-on-error: true

```

## File: .github\workflows\detect-schema-changes.yml
```
name: Detect schema changes

on:
  schedule:
    # run on the Tue of the second week (8th-14th) of every month, at 3:42AM
    - cron: '42 3 8-14 * 2'
  workflow_dispatch:

permissions:
  contents: read

jobs:
  update-submodules:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: recursive
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Update submodules
        run: |
          git submodule update --remote --recursive

      - name: Detect changes
        id: diff
        run: |
          changes="$(
            git --no-pager diff --no-color --submodule=diff | {
              grep -E '^diff .*/src/schemas/json/github-(workflow|action).json$' || true
            }
          )"

          if [[ -n "$changes" ]]; then
            echo "There are changes in submodules"
            echo "$changes"
            exit 1
          fi

```

## File: .github\workflows\qa.yml
```
name: Quality Control

on:
  push:
    paths:
      - ".github/workflows/qa.yml"
    branches:
      - main
  pull_request:
    branches:
      - main

defaults:
  run:
    shell: bash

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@stable

      - name: Cache
        uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
        with:
          path: |
            ~/.cargo
            ~/.rustup
            target/
          key: ${{ runner.os }}-${{ steps.rust-install.outputs.cachekey }}-check

      - name: Check Formatting
        run: |
          cargo +${{ steps.rust-install.outputs.name }} fmt --check

      - name: Check with Clippy
        run: |
          cargo +${{ steps.rust-install.outputs.name }} clippy -- -D warnings

      - name: Check docs
        run: |
          cargo +${{ steps.rust-install.outputs.name }} rustdoc -- -D warnings

      - name: Shellcheck
        uses: ludeeus/action-shellcheck@master
        with:
          ignore_paths: src/schemastore

      - name: Install shfmt
        uses: mfinelli/setup-shfmt@master

      - name: Run shfmt
        run: shfmt -d bin/*

      - name: Setup Node
        uses: actions/setup-node@53b83947a5a98c8d113130e565377fae1a50d02f # v6.3.0
        with:
          node-version: 18

      - name: Install Dependencies
        run: npm ci

      - name: Lint (Prettier)
        run: npm run lint

  build:
    strategy:
      matrix:
        rust-toolchain:
          - stable
          - nightly
          - 1.84.0
        os:
          - ubuntu-latest
          - macos-latest
          - windows-latest

    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@master
        with:
          toolchain: ${{ matrix.rust-toolchain }}

      - name: Cache
        uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
        with:
          path: |
            ~/.cargo
            ~/.rustup
            target/
          key: ${{ runner.os }}-${{ steps.rust-install.outputs.cachekey }}-build

      - name: Build
        run: |
          cargo +${{ steps.rust-install.outputs.name }} build --release --all-features

  test:
    strategy:
      matrix:
        rust-toolchain:
          - stable
          - nightly
        os:
          - ubuntu-latest

    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@master
        with:
          toolchain: ${{ matrix.rust-toolchain }}

      - name: Cache
        uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
        with:
          path: |
            ~/.cargo
            ~/.rustup
            target/
          key: ${{ runner.os }}-${{ steps.rust-install.outputs.cachekey }}-test

      - name: Run Testsuite
        run: |
          cargo +${{ steps.rust-install.outputs.name }} test

  build-test-node:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@stable

      - name: Cache
        uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
        with:
          path: |
            ~/.cargo
            ~/.rustup
            target/
          key: ${{ runner.os }}-${{ steps.rust-install.outputs.cachekey }}-test-node

      - name: Setup Node
        uses: actions/setup-node@53b83947a5a98c8d113130e565377fae1a50d02f # v6.3.0
        with:
          cache: npm
          node-version: 18

      - name: Install Dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Test
        run: npm test
        # nodejs support is experimental; don't fail the build for it
        continue-on-error: true

  actions:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install action-validator with asdf
        uses: asdf-vm/actions/install@b7bcd026f18772e44fe1026d729e1611cc435d47 # v4.0.1
        with:
          tool_versions: |
            action-validator 0.6.0

      - name: Lint Actions
        run: |
          find .github/workflows -type f \( -iname \*.yaml -o -iname \*.yml \) \
            | xargs -I {} action-validator --verbose {}

```

## File: .github\workflows\release.yml
```
name: Upload release artifacts

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  draft-release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          fetch-tags: true

      - name: Create draft release
        env:
          GH_TOKEN: ${{ github.token }}
          tag: ${{ github.ref_name }}
        run: |
          set -x
          title="$(git tag -l --format='%(contents:subject)' "$tag")"
          notes="$(git tag -l --format='%(contents:body)' "$tag")"

          gh release create "$tag" --title "$title" --notes "$notes" --draft

  binaries:
    needs: draft-release
    strategy:
      fail-fast: false
      matrix:
        include:
          - os: ubuntu-latest
            rust_target: x86_64-unknown-linux-musl
            asset_name: action-validator_linux_amd64
          - os: macos-latest
            rust_target: x86_64-apple-darwin
            asset_name: action-validator_darwin_amd64
          - os: ubuntu-latest
            rust_target: aarch64-unknown-linux-musl
            asset_name: action-validator_linux_arm64
          - os: macos-latest
            rust_target: aarch64-apple-darwin
            asset_name: action-validator_darwin_arm64

    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@stable
        with:
          targets: ${{ matrix.rust_target }}

      - name: Cache
        uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
        with:
          path: |
            ~/.cargo
            ~/.rustup
            target/
          key: ${{ runner.os }}-${{ steps.rust-install.outputs.cachekey }}-${{ matrix.rust_target }}-binary-release

      - name: Set Cargo.toml version
        if: github.event_name == 'push'
        shell: bash
        env:
          RELEASE_TAG: ${{ github.ref }}
        run: |
          mv Cargo.toml Cargo.toml.orig
          sed "s/0\\.0\\.0-git/${RELEASE_TAG##*\/v}/" Cargo.toml.orig >Cargo.toml
          mv Cargo.lock Cargo.lock.orig
          sed "s/0\\.0\\.0-git/${RELEASE_TAG##*\/v}/" Cargo.lock.orig >Cargo.lock

      - name: Install cross-build helper package
        if: matrix.rust_target == 'x86_64-unknown-linux-musl'
        run: |
          sudo apt update
          sudo apt install musl-tools

      - name: Install cross-compile linker for aarch64-unknown-linux-musl
        if: matrix.rust_target == 'aarch64-unknown-linux-musl'
        run: |
          sudo apt update
          sudo apt install musl-tools gcc-aarch64-linux-gnu

      - name: Build
        env:
          CARGO_TARGET_AARCH64_UNKNOWN_LINUX_MUSL_LINKER: '/usr/bin/aarch64-linux-gnu-ld'
          CC_aarch64_unknown_linux_musl: 'aarch64-linux-gnu-gcc'

        run: |
          cargo +${{ steps.rust-install.outputs.name }} build --target ${{ matrix.rust_target }} --release --locked

      - name: Upload
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          tag: ${{ github.ref_name }}
          binary: target/${{ matrix.rust_target }}/release/action-validator
          asset_name: ${{ matrix.asset_name }}
        run: |
          mv "$binary" "$asset_name"
          gh release upload "$tag" "$asset_name"

  crate:
    needs: binaries
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        id: rust-install
        uses: dtolnay/rust-toolchain@stable

      - name: Cache
        uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
        with:
          path: |
            ~/.cargo
            ~/.rustup
            target/
          key: ${{ runner.os }}-${{ steps.rust-install.outputs.cachekey }}-crate-release

      - name: Set Cargo.toml version
        if: github.event_name == 'push'
        shell: bash
        env:
          RELEASE_TAG: ${{ github.ref }}
        run: |
          mv Cargo.toml Cargo.toml.orig
          sed "s/0\\.0\\.0-git/${RELEASE_TAG##*\/v}/" Cargo.toml.orig >Cargo.toml
          mv Cargo.lock Cargo.lock.orig
          sed "s/0\\.0\\.0-git/${RELEASE_TAG##*\/v}/" Cargo.lock.orig >Cargo.lock

      - name: Publish crate
        if: github.event_name == 'push'
        env:
          CARGO_REGISTRY_TOKEN: ${{ secrets.CRATES_IO_TOKEN }}
        run: |
          cargo publish --allow-dirty

  npm:
    needs: binaries
    strategy:
      matrix:
        package-dir:
          - packages/core
          - packages/cli

    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          submodules: true

      - name: Install rust
        if: matrix.package-dir == 'packages/core'
        id: rust-install
        uses: dtolnay/rust-toolchain@stable

      - name: Cache
        uses: actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
        with:
          path: |
            ~/.cargo
            ~/.rustup
            target/
          key: ${{ runner.os }}-${{ steps.rust-install.outputs.cachekey }}-npm-${{ matrix.package-dir }}-release

      - name: Setup Node
        uses: actions/setup-node@53b83947a5a98c8d113130e565377fae1a50d02f # v6.3.0
        with:
          cache: npm
          node-version: 18
          registry-url: "https://registry.npmjs.org"

      - name: Install root dependencies
        if: matrix.package-dir == 'packages/core'
        run: npm ci

      - name: Build
        if: matrix.package-dir == 'packages/core'
        run: npm run build

      - name: Install package dependencies
        working-directory: ${{ matrix.package-dir }}
        run: npm ci

      - name: Set package.json version
        if: github.event_name == 'push'
        shell: bash
        env:
          RELEASE_TAG: ${{ github.ref }}
        working-directory: ${{ matrix.package-dir }}
        run: |
          mv package.json package.json.orig
          sed "s/0\\.0\\.0-git/${RELEASE_TAG##*\/v}/" package.json.orig >package.json
          mv package-lock.json package-lock.json.orig
          sed "s/0\\.0\\.0-git/${RELEASE_TAG##*\/v}/" package-lock.json.orig >package-lock.json

      - name: Copy README.md and LICENCE to package
        env:
          PACKAGE_DIR: ${{ matrix.package-dir }}
        run: |
          cp README.md $PACKAGE_DIR/README.md
          cp LICENCE $PACKAGE_DIR/LICENCE

      - name: Publish NPM
        if: github.event_name == 'push'
        run: npm publish --access public
        working-directory: ${{ matrix.package-dir }}
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}

  publish-release:
    needs:
      - binaries
      - crate
      - npm
    runs-on: ubuntu-latest
    steps:
      - name: Publish release
        if: github.event_name == 'push'
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          tag: ${{ github.ref_name }}
        run: |
          gh release edit "$tag" --draft=false

```

## File: packages\cli\package-lock.json
```
{
  "name": "@action-validator/cli",
  "version": "0.0.0-git",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "@action-validator/cli",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "dependencies": {
        "chalk": "5.2.0"
      },
      "bin": {
        "action-validator": "cli.mjs"
      },
      "devDependencies": {
        "@action-validator/core": "file:../core"
      },
      "peerDependencies": {
        "@action-validator/core": "0.0.0-git"
      }
    },
    "../core": {
      "name": "@action-validator/core",
      "version": "0.0.0-git",
      "dev": true,
      "license": "GPL-3.0-only"
    },
    "node_modules/@action-validator/core": {
      "resolved": "../core",
      "link": true
    },
    "node_modules/chalk": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
      "integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA==",
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    }
  },
  "dependencies": {
    "@action-validator/core": {
      "version": "file:../core"
    },
    "chalk": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
      "integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA=="
    }
  }
}

```

## File: packages\cli\package.json
```
{
  "name": "@action-validator/cli",
  "collaborators": [
    "Matt Palmer <matt@hezmatt.org>",
    "Ben Heidemann <ben@heidemann.co.uk>"
  ],
  "description": "Validator for GitHub action and workflow YAML files",
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "repository": {
    "type": "git",
    "url": "https://github.com/mpalmer/action-validator"
  },
  "files": [
    "cli.mjs"
  ],
  "main": "cli.js",
  "homepage": "https://github.com/mpalmer/action-validator",
  "bin": {
    "action-validator": "./cli.mjs"
  },
  "scripts": {
    "build": "npx wasm-pack build --out-dir target/wasm-pack/build --no-typescript --target nodejs --features js && cp target/wasm-pack/build/action_validator_bg.wasm dist/ && cp target/wasm-pack/build/action_validator.js dist/ && cp target/wasm-pack/build/action_validator.js dist/",
    "test": "node test/run.mjs",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "dependencies": {},
  "devDependencies": {
    "@action-validator/core": "file:../core"
  },
  "peerDependencies": {
    "@action-validator/core": "0.0.0-git"
  }
}

```

## File: packages\core\action_validator.d.ts
```
export type ParseErrorLocation = {
  index: number;
  line: number;
  column: number;
};

export type ValidationError =
  | {
      code: string;
      detail?: string;
      path: string;
      title: string;
      states?: Omit<ValidationState, "actionType">[];
    }
  | {
      code: string;
      detail: string;
      title: string;
      location?: ParseErrorLocation;
    };

export type ValidationState = {
  actionType: "action" | "workflow";
  errors: ValidationError[];
};

export function main(args: string[]): never;
export function validateAction(src: string): ValidationState;
export function validateWorkflow(src: string): ValidationState;

```

## File: packages\core\package-lock.json
```
{
  "name": "@action-validator/core",
  "version": "0.0.0-git",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "@action-validator/core",
      "version": "0.0.0-git",
      "license": "GPL-3.0-only",
      "dependencies": {
        "fast-glob": "^3.3.3"
      }
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      },
      "engines": {
        "node": ">=8.6.0"
      }
    },
    "node_modules/fastq": {
      "version": "1.19.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz",
      "integrity": "sha512-GwLTyxkCXjXbxqIhTsMI2Nui8huMPtnxg7krajPJAjnEG/iiOS7i+zCtWGZR9G0NBKbXKh6X9m9UIsYX/N6vvQ==",
      "license": "ISC",
      "dependencies": {
        "reusify": "^1.0.4"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "license": "MIT",
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "license": "MIT",
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "license": "MIT",
      "dependencies": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      },
      "engines": {
        "node": ">=8.6"
      }
    },
    "node_modules/picomatch": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
      "integrity": "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==",
      "license": "MIT",
      "engines": {
        "node": ">=8.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/queue-microtask": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
      "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/reusify": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
      "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==",
      "license": "MIT",
      "engines": {
        "iojs": ">=1.0.0",
        "node": ">=0.10.0"
      }
    },
    "node_modules/run-parallel": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
      "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "queue-microtask": "^1.2.2"
      }
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "license": "MIT",
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    }
  },
  "dependencies": {
    "@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "requires": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      }
    },
    "@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A=="
    },
    "@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "requires": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      }
    },
    "braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "requires": {
        "fill-range": "^7.1.1"
      }
    },
    "fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "requires": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      }
    },
    "fastq": {
      "version": "1.19.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz",
      "integrity": "sha512-GwLTyxkCXjXbxqIhTsMI2Nui8huMPtnxg7krajPJAjnEG/iiOS7i+zCtWGZR9G0NBKbXKh6X9m9UIsYX/N6vvQ==",
      "requires": {
        "reusify": "^1.0.4"
      }
    },
    "fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "requires": {
        "to-regex-range": "^5.0.1"
      }
    },
    "glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "requires": {
        "is-glob": "^4.0.1"
      }
    },
    "is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ=="
    },
    "is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "requires": {
        "is-extglob": "^2.1.1"
      }
    },
    "is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng=="
    },
    "merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg=="
    },
    "micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "requires": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      }
    },
    "picomatch": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
      "integrity": "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA=="
    },
    "queue-microtask": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
      "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A=="
    },
    "reusify": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
      "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw=="
    },
    "run-parallel": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
      "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
      "requires": {
        "queue-microtask": "^1.2.2"
      }
    },
    "to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "requires": {
        "is-number": "^7.0.0"
      }
    }
  }
}

```

## File: packages\core\package.json
```
{
  "name": "@action-validator/core",
  "collaborators": [
    "Matt Palmer <matt@hezmatt.org>",
    "Ben Heidemann <ben@heidemann.co.uk>"
  ],
  "description": "Validator for GitHub action and workflow YAML files",
  "version": "0.0.0-git",
  "license": "GPL-3.0-only",
  "repository": {
    "type": "git",
    "url": "https://github.com/mpalmer/action-validator"
  },
  "files": [
    "action_validator_bg.wasm",
    "action_validator.js",
    "action_validator.d.ts"
  ],
  "main": "action_validator.js",
  "homepage": "https://github.com/mpalmer/action-validator",
  "types": "action_validator.d.ts",
  "scripts": {
    "build": "npx wasm-pack build --out-dir target/wasm-pack/build --no-typescript --target nodejs --features js && cp target/wasm-pack/build/action_validator_bg.wasm dist/ && cp target/wasm-pack/build/action_validator.js dist/ && cp target/wasm-pack/build/action_validator.js dist/",
    "test": "node test/run.mjs",
    "lint": "prettier --check .",
    "format": "prettier --write ."
  },
  "dependencies": {
    "fast-glob": "^3.3.3"
  }
}

```

## File: src\config.rs
```
use clap::Parser;
use serde::Serialize;
use std::path::PathBuf;

#[derive(Parser, Debug)]
#[command(
    name = "action-validator",
    about = "A validator for GitHub Action and Workflow YAML files",
    version
)]
pub struct CliConfig {
    /// Be more verbose
    #[arg(short, long)]
    pub verbose: bool,

    #[arg(
        long,
        help = "Use specified dir as root of glob matching, rather than the current directory"
    )]
    pub rootdir: Option<PathBuf>,

    /// Input file
    #[arg(name = "path_to_action_yaml")]
    pub src: Vec<PathBuf>,
}

#[derive(Serialize, Copy, Clone, Debug)]
pub enum ActionType {
    #[serde(rename = "action")]
    Action,
    #[serde(rename = "workflow")]
    Workflow,
}

pub struct JsConfig<'a> {
    pub action_type: ActionType,
    pub src: &'a str,
    pub verbose: bool,
}

pub struct RunConfig<'a> {
    pub file_path: Option<&'a str>,
    pub file_name: Option<&'a str>,
    pub action_type: ActionType,
    pub src: &'a str,
    pub verbose: bool,
    pub rootdir: Option<PathBuf>,
}

impl<'a> From<&JsConfig<'a>> for RunConfig<'a> {
    fn from(config: &JsConfig<'a>) -> Self {
        RunConfig {
            file_path: None,
            file_name: None,
            action_type: config.action_type,
            src: config.src,
            verbose: config.verbose,
            rootdir: None,
        }
    }
}

```

## File: src\lib.rs
```
mod config;
mod schemas;
mod system;
mod utils;
mod validation_error;
mod validation_state;

use config::{ActionType, RunConfig};
use std::path::PathBuf;
use validation_error::ValidationError;
use validation_state::ValidationState;

pub use crate::config::CliConfig;
use crate::schemas::{validate_as_action, validate_as_workflow};

#[cfg(feature = "js")]
mod js {
    use super::cli;
    use crate::config::CliConfig;
    use crate::system;
    use crate::{
        config::{ActionType, JsConfig},
        utils::set_panic_hook,
    };
    use clap::Parser as _;
    use js_sys::Array;
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(js_name = main)]
    pub fn main(args: Array) -> JsValue {
        set_panic_hook();

        let rust_args: Vec<String> = args
            .iter()
            .map(|arg| arg.as_string().unwrap_or_default())
            .collect();

        let config = match CliConfig::try_parse_from(rust_args) {
            Ok(config) => config,
            Err(error) => {
                let error_text = if system::process::stdout::is_tty() {
                    format!("{}", error.render().ansi())
                } else {
                    error.render().to_string()
                };
                system::console::error(&error_text);
                system::process::exit(error.exit_code());
            }
        };

        if matches!(cli::run(&config), cli::RunResult::Failure) {
            system::process::exit(1);
        }

        system::process::exit(0);
    }

    #[wasm_bindgen(js_name = validateAction)]
    pub fn validate_action(src: &str) -> JsValue {
        set_panic_hook();

        let config = JsConfig {
            action_type: ActionType::Action,
            src,
            verbose: false,
        };

        run(&config)
    }

    #[wasm_bindgen(js_name = validateWorkflow)]
    pub fn validate_workflow(src: &str) -> JsValue {
        set_panic_hook();

        let config = JsConfig {
            action_type: ActionType::Workflow,
            src,
            verbose: false,
        };

        run(&config)
    }

    fn run(config: &JsConfig) -> JsValue {
        let run_config = config.into();
        let state = crate::run(&run_config);
        serde_wasm_bindgen::to_value(&state).unwrap()
    }
}

pub mod cli {
    use crate::{
        config::{ActionType, RunConfig},
        system, CliConfig,
    };

    pub enum RunResult {
        Success,
        Failure,
    }

    pub fn run(config: &CliConfig) -> RunResult {
        let mut success = true;

        for path in &config.src {
            let file_name = match path.file_name() {
                Some(file_name) => file_name.to_str(),
                None => {
                    eprintln!("Unable to derive file name from src!");
                    success = false;
                    continue;
                }
            };

            let src = &match system::fs::read_to_string(path) {
                Ok(src) => src,
                Err(err) => {
                    system::console::error(&format!(
                        "Unable to read file {}: {err}",
                        path.display()
                    ));
                    success = false;
                    continue;
                }
            };

            let config = RunConfig {
                file_path: Some(path.to_str().unwrap()),
                file_name,
                action_type: match file_name {
                    Some("action.yml") | Some("action.yaml") => ActionType::Action,
                    _ => ActionType::Workflow,
                },
                src,
                verbose: config.verbose,
                rootdir: config.rootdir.clone(),
            };

            let state = crate::run(&config);

            if !state.is_valid() {
                let fmt_state = format!("{state:#?}");
                let path = state.file_path.unwrap_or("file".into());
                system::console::log(&format!("Fatal error validating {path}"));
                system::console::error(&format!("Validation failed: {fmt_state}"));
                success = false;
            }
        }

        if success {
            RunResult::Success
        } else {
            RunResult::Failure
        }
    }
}

fn run(config: &RunConfig) -> ValidationState {
    let file_name = config.file_name.unwrap_or("file");
    let doc = yaml_serde::from_str(config.src);

    let mut state = match doc {
        Err(err) => ValidationState {
            action_type: Some(config.action_type),
            file_path: Some(file_name.to_string()),
            errors: vec![err.into()],
        },
        Ok(doc) => match config.action_type {
            ActionType::Action => {
                if config.verbose {
                    system::console::log(&format!("Treating {file_name} as an Action definition"));
                }
                validate_as_action(&doc)
            }
            ActionType::Workflow => {
                if config.verbose {
                    system::console::log(&format!("Treating {file_name} as a Workflow definition"));
                }
                // TODO: Re-enable path and job validation
                let mut state = validate_as_workflow(&doc);

                validate_paths(&doc, config.rootdir.as_ref(), &mut state);
                validate_job_needs(&doc, &mut state);

                state
            }
        },
    };

    state.action_type = Some(config.action_type);
    state.file_path = config.file_path.map(|file_name| file_name.to_string());

    state
}

fn validate_paths(doc: &serde_json::Value, rootdir: Option<&PathBuf>, state: &mut ValidationState) {
    validate_globs(
        &doc["on"]["push"]["paths"],
        "/on/push/paths",
        rootdir,
        state,
    );
    validate_globs(
        &doc["on"]["push"]["paths-ignore"],
        "/on/push/paths-ignore",
        rootdir,
        state,
    );
    validate_globs(
        &doc["on"]["pull_request"]["paths"],
        "/on/pull_request/paths",
        rootdir,
        state,
    );
    validate_globs(
        &doc["on"]["pull_request"]["paths-ignore"],
        "/on/pull_request/paths-ignore",
        rootdir,
        state,
    );
}

fn validate_globs(
    globs: &serde_json::Value,
    path: &str,
    rootdir: Option<&PathBuf>,
    state: &mut ValidationState,
) {
    if globs.is_null() {
        return;
    }

    if let Some(globs) = globs.as_array() {
        let git_files = match system::git::ls_files() {
            Ok(files) => files,
            Err(e) => {
                state.errors.push(ValidationError::InvalidGlob {
                    code: "git_ls_files_failed".into(),
                    path: path.into(),
                    title: "Failed to get git tracked files".into(),
                    detail: Some(format!("git ls-files failed: {e}")),
                });
                return;
            }
        };

        let git_file_refs: Vec<&str> = git_files.iter().map(|s| s.as_str()).collect();

        for g in globs {
            let glob = g.as_str().expect("glob to be a string");
            let pattern = if glob.starts_with('!') {
                glob.chars().skip(1).collect()
            } else {
                glob.to_string()
            };

            let pattern = if let Some(rootdir) = rootdir {
                rootdir.join(pattern).display().to_string()
            } else {
                pattern
            };

            match compare_changes::path_matches(&pattern, &git_file_refs) {
                Ok(matched_index) => {
                    if matched_index.is_none() {
                        state.errors.push(ValidationError::NoFilesMatchingGlob {
                            code: "glob_not_matched".into(),
                            path: path.into(),
                            title: "Glob does not match any files".into(),
                            detail: Some(format!("Glob {g} in {path} does not match any files")),
                        });
                    }
                }
                Err(e) => {
                    state.errors.push(ValidationError::InvalidGlob {
                        code: "invalid_glob".into(),
                        path: path.into(),
                        title: "Glob does not match any files".into(),
                        detail: Some(format!("Glob {g} in {path} is invalid: {e}")),
                    });
                }
            };
        }
    } else {
        unreachable!(
            "validate_globs called on globs object with invalid type: must be array or null"
        )
    }
}

fn validate_job_needs(doc: &serde_json::Value, state: &mut ValidationState) {
    fn is_invalid_dependency(
        jobs: &serde_json::Map<String, serde_json::Value>,
        need_str: &str,
    ) -> bool {
        !jobs.contains_key(need_str)
    }

    fn handle_unresolved_job(job_name: &String, needs_str: &str, state: &mut ValidationState) {
        state.errors.push(ValidationError::UnresolvedJob {
            code: "unresolved_job".into(),
            path: format!("/jobs/{job_name}/needs"),
            title: "Unresolved job".into(),
            detail: Some(format!("unresolved job {needs_str}")),
        });
    }

    if let Some(jobs) = doc["jobs"].as_object() {
        for (job_name, job) in jobs.iter() {
            let needs = &job["needs"];
            if let Some(needs_str) = needs.as_str() {
                if is_invalid_dependency(jobs, needs_str) {
                    handle_unresolved_job(job_name, needs_str, state);
                }
            } else if let Some(needs_array) = needs.as_array() {
                for needs_str in needs_array
                    .iter()
                    .filter_map(|v| v.as_str())
                    .filter(|needs_str| is_invalid_dependency(jobs, needs_str))
                {
                    handle_unresolved_job(job_name, needs_str, state);
                }
            }
        }
    }
}

```

## File: src\main.rs
```
#[cfg(feature = "js")]
fn main() {}

#[cfg(not(feature = "js"))]
fn main() {
    use action_validator::CliConfig;
    use clap::Parser;
    use std::process;

    let config = CliConfig::parse();

    if matches!(
        action_validator::cli::run(&config),
        action_validator::cli::RunResult::Failure
    ) {
        process::exit(1);
    }
}

```

## File: src\schemas.rs
```
use serde_json::Value;

use crate::validation_state::ValidationState;

pub fn validate_as_action(doc: &Value) -> ValidationState {
    validate_with_schema(
        doc,
        include_bytes!("schemastore/src/schemas/json/github-action.json"),
    )
}

pub fn validate_as_workflow(doc: &Value) -> ValidationState {
    validate_with_schema(
        doc,
        include_bytes!("schemastore/src/schemas/json/github-workflow.json"),
    )
}

fn validate_with_schema(doc: &Value, schema: &[u8]) -> ValidationState {
    let schema_json: serde_json::Value =
        serde_json::from_str(String::from_utf8_lossy(schema).as_ref()).unwrap();

    let mut scope = valico::json_schema::Scope::new();
    let validator = scope.compile_and_return(schema_json, false).unwrap();

    validator.validate(doc).into()
}

```

## File: src\utils.rs
```
#[cfg(feature = "js")]
pub fn set_panic_hook() {
    // When the `console_error_panic_hook` feature is enabled, we can call the
    // `set_panic_hook` function at least once during initialization, and then
    // we will get better error messages if our code ever panics.
    //
    // For more details see
    // https://github.com/rustwasm/console_error_panic_hook#readme
    #[cfg(feature = "console_error_panic_hook")]
    console_error_panic_hook::set_once();
}

```

## File: src\validation_error.rs
```
use serde::Serialize;
use valico::common::error::ValicoError;

use crate::validation_state::ValidationState;

type BoxedValicoError = Box<dyn ValicoError>;

#[derive(Serialize, Debug)]
pub struct ParseErrorLocation {
    pub index: usize,
    pub line: usize,
    pub column: usize,
}

impl From<yaml_serde::Location> for ParseErrorLocation {
    fn from(location: yaml_serde::Location) -> Self {
        ParseErrorLocation {
            index: location.index(),
            line: location.line(),
            column: location.column(),
        }
    }
}

macro_rules! validation_errors {
    ($( $name:ident $( { $($fields:tt)* } )? ),*) => {
        #[derive(Serialize, Debug)]
        #[serde(untagged)]
        #[allow(dead_code)] // JS doesn't instantiate some of the validation errors at present
        pub enum ValidationError {
            $(
                $name {
                    code: String,
                    detail: Option<String>,
                    path: String,
                    title: String,
                    $( $($fields)* )?
                },
            )*
        }
    };
}

validation_errors!(
    // Schema Validation Errors
    WrongType,
    MultipleOf,
    Maximum,
    Minimum,
    MaxLength,
    MinLength,
    Pattern,
    MaxItems,
    MinItems,
    UniqueItems,
    Items,
    MaxProperties,
    MinProperties,
    Required,
    Properties,
    Enum,
    AnyOf { states: Vec<ValidationState> },
    OneOf { states: Vec<ValidationState> },
    Const,
    Contains,
    ContainsMinMax,
    Not,
    DivergentDefaults,
    Format,
    Unevaluated,
    Unknown,
    // Other Validation Errors
    UnresolvedJob,
    InvalidGlob,
    NoFilesMatchingGlob,
    // Other Errors
    Parse { location: Option<ParseErrorLocation> }
);

macro_rules! impl_from_valico_error {
    ($($err:ident => $name:ident $( { $($fields:tt)* } )? ),*) => {
        impl From<&BoxedValicoError> for ValidationError {
            fn from(err: &BoxedValicoError) -> Self {
                if false {
                    unreachable!()
                }
                $(
                    else if let Some($err) = err.downcast_ref::<valico::json_schema::errors::$name>() {
                        ValidationError::$name {
                            code: $err.get_code().into(),
                            path: $err.get_path().into(),
                            title: $err.get_title().into(),
                            detail: $err.get_detail().map(|s| s.into()),
                            $( $($fields)* )?
                        }
                    }
                )*
                else {
                    ValidationError::Unknown {
                        code: err.get_code().into(),
                        path: err.get_path().into(),
                        title: err.get_title().into(),
                        detail: err.get_detail().map(|s| s.into()),
                    }
                }
            }
        }
    };
}

impl_from_valico_error!(
    err => WrongType,
    err => MultipleOf,
    err => Maximum,
    err => Minimum,
    err => MaxLength,
    err => MinLength,
    err => Pattern,
    err => MaxItems,
    err => MinItems,
    err => UniqueItems,
    err => Items,
    err => MaxProperties,
    err => MinProperties,
    err => Required,
    err => Properties,
    err => Enum,
    err => AnyOf { states: err.states.iter().map(ValidationState::from).collect() },
    err => OneOf { states: err.states.iter().map(ValidationState::from).collect() },
    err => Const,
    err => Contains,
    err => ContainsMinMax,
    err => Not,
    err => DivergentDefaults,
    err => Format,
    err => Unevaluated
);

impl From<yaml_serde::Error> for ValidationError {
    fn from(err: yaml_serde::Error) -> Self {
        ValidationError::Parse {
            code: "parse_error".into(),
            detail: Some(err.to_string()),
            location: err.location().map(ParseErrorLocation::from),
            path: "".into(),
            title: "Parse Error".into(),
        }
    }
}

```

## File: src\validation_state.rs
```
use serde::Serialize;

use crate::{config::ActionType, validation_error::ValidationError};

#[derive(Serialize, Debug)]
pub struct ValidationState {
    #[serde(rename = "actionType")]
    pub action_type: Option<ActionType>,
    #[serde(rename = "filePath")]
    pub file_path: Option<String>,
    pub errors: Vec<ValidationError>,
}

impl ValidationState {
    pub fn is_valid(&self) -> bool {
        self.errors.is_empty()
    }
}

impl From<valico::json_schema::ValidationState> for ValidationState {
    fn from(state: valico::json_schema::ValidationState) -> Self {
        ValidationState {
            file_path: None,
            action_type: None,
            errors: state.errors.iter().map(|err| err.into()).collect(),
        }
    }
}

impl From<&valico::json_schema::ValidationState> for ValidationState {
    fn from(state: &valico::json_schema::ValidationState) -> Self {
        ValidationState {
            file_path: None,
            action_type: None,
            errors: state.errors.iter().map(|err| err.into()).collect(),
        }
    }
}

```

## File: src\js\system.js
```
const console = require('node:console');
const fs = require('node:fs');
const process = require('node:process');
const fg = require('fast-glob');

module.exports.console = console;
module.exports.fs = fs;
module.exports.process = process;
module.exports.fg = fg;

```

## File: src\system\console.rs
```
#[cfg(feature = "js")]
mod js_console {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(js_namespace = console, js_name = log)]
        pub fn log(s: &str);

        #[wasm_bindgen(js_namespace = console, js_name = error)]
        pub fn error(s: &str);
    }
}

#[cfg(feature = "js")]
pub fn log(s: &str) {
    js_console::log(s);
}

#[cfg(not(feature = "js"))]
pub fn log(s: &str) {
    println!("{s}");
}

#[cfg(feature = "js")]
pub fn error(s: &str) {
    js_console::error(s);
}

#[cfg(not(feature = "js"))]
pub fn error(s: &str) {
    eprintln!("{s}");
}

```

## File: src\system\fs.rs
```
use std::path::Path;

#[cfg(feature = "js")]
mod js_fs {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(catch, js_namespace = fs, js_name = readFileSync)]
        pub fn read_file_sync(path: &str, encoding: &str) -> Result<String, js_sys::Error>;
    }
}

#[cfg(feature = "js")]
pub fn read_to_string<P>(path: P) -> Result<String, String>
where
    P: AsRef<Path>,
{
    js_fs::read_file_sync(path.as_ref().to_string_lossy().as_ref(), "utf8")
        .map_err(|e| format!("{}", e.to_string()))
}

#[cfg(not(feature = "js"))]
pub fn read_to_string<P>(path: P) -> Result<String, String>
where
    P: AsRef<Path>,
{
    std::fs::read_to_string(path).map_err(|e| e.to_string())
}

```

## File: src\system\git.rs
```
use std::process::Command;

pub fn ls_files() -> Result<Vec<String>, std::io::Error> {
    let output = Command::new("git").args(["ls-files", "-z"]).output()?;

    if !output.status.success() {
        return Err(std::io::Error::other(format!(
            "git ls-files failed: {}",
            String::from_utf8_lossy(&output.stderr)
        )));
    }

    let files = String::from_utf8_lossy(&output.stdout)
        .split('\0')
        .filter(|s| !s.is_empty())
        .map(|s| s.to_string())
        .collect();

    Ok(files)
}

```

## File: src\system\mod.rs
```
pub mod console;
pub mod fs;
pub mod git;
pub mod process;

```

## File: src\system\process.rs
```
#[cfg(feature = "js")]
mod js_process {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen(module = "/src/js/system.js")]
    extern "C" {
        #[wasm_bindgen(js_namespace = process, js_name = exit)]
        pub fn exit(code: i32) -> JsValue;

        #[wasm_bindgen(thread_local_v2, js_namespace = ["process", "stdout"], js_name = isTTY)]
        pub static STDOUT_IS_TTY: bool;
    }
}

#[cfg(feature = "js")]
pub fn exit(code: i32) -> ! {
    js_process::exit(code);
    unreachable!();
}

pub mod stdout {
    #[cfg(feature = "js")]
    pub fn is_tty() -> bool {
        use super::js_process;
        js_process::STDOUT_IS_TTY.with(bool::clone)
    }
}

```

## File: tests\snapshot_tests.rs
```
use fixtures::fixtures;
use std::env::current_dir;
use std::fs::File;
use std::io::BufReader;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::{ffi::OsStr, fs};

static REPO_DIR_WILDCARD: &str = "{{repo}}";

#[derive(Debug, serde::Deserialize)]
struct SnapshotTestConfig {
    cli_args: Option<Vec<String>>,
}

#[derive(Debug)]
struct SnapshotTest {
    config: SnapshotTestConfig,
    current_dir: PathBuf,
    test_dir: PathBuf,
}

impl SnapshotTest {
    fn new(test_dir: &Path) -> Self {
        let test_config_file = test_dir.join("test.json");

        let config: SnapshotTestConfig = serde_json::from_reader(BufReader::new(
            File::open(&test_config_file).expect(&format!(
                "missing test conifg file ({})",
                test_config_file.to_string_lossy(),
            )),
        ))
        .expect(&format!(
            "invalid test config file ({})",
            test_config_file.to_string_lossy(),
        ));

        SnapshotTest {
            config,
            current_dir: current_dir().unwrap(),
            test_dir: test_dir.to_path_buf(),
        }
    }

    fn build_command(&self) -> Command {
        #[cfg(not(feature = "test-js"))]
        {
            Command::new(assert_cmd::cargo::cargo_bin!())
        }

        #[cfg(feature = "test-js")]
        {
            let mut cmd = Command::new("node");
            cmd.arg("packages/cli/cli.mjs");
            cmd
        }
    }

    fn execute(self) {
        use std::ffi::OsString;

        let pwd = self.current_dir.to_str().unwrap();

        let cli_args: Vec<_> = if let Some(cli_args) = &self.config.cli_args {
            cli_args.iter().map(OsString::from).collect()
        } else {
            fs::read_dir(&self.test_dir)
                .unwrap()
                .filter_map(Result::ok)
                .filter(|f| f.path().extension() == Some(OsStr::new("yml")))
                .map(|f| f.path().into_os_string())
                .collect()
        };

        #[cfg(not(feature = "test-save-snapshots"))]
        {
            use assert_cmd::assert::OutputAssertExt as _;

            let stderr = fs::read_to_string(self.test_dir.join("stderr"))
                .unwrap_or(String::from(""))
                .replace(REPO_DIR_WILDCARD, pwd);

            let stdout = fs::read_to_string(self.test_dir.join("stdout"))
                .unwrap_or(String::from(""))
                .replace(REPO_DIR_WILDCARD, pwd);

            let exitcode: i32 = fs::read_to_string(self.test_dir.join("exitcode"))
                .map(|s| {
                    s.strip_suffix("\n")
                        .unwrap_or(s.as_str())
                        .parse::<i32>()
                        .unwrap_or(0)
                })
                .unwrap_or(0);

            self.build_command()
                .args(&cli_args)
                .assert()
                .stdout(stdout)
                .stderr(stderr)
                .code(exitcode);
        }

        #[cfg(feature = "test-save-snapshots")]
        {
            use assert_cmd::output::OutputOkExt as _;
            use std::io::prelude::*;

            let result = self
                .build_command()
                .args(&cli_args)
                .ok()
                .unwrap_or_else(|e| e.as_output().unwrap().to_owned());

            if !result.stdout.is_empty() {
                File::create(self.test_dir.join("stdout"))
                    .unwrap()
                    .write_all(
                        String::from_utf8(result.stdout)
                            .unwrap()
                            .replace(pwd, REPO_DIR_WILDCARD)
                            .as_bytes(),
                    )
                    .unwrap();
            }
            if !result.stderr.is_empty() {
                File::create(self.test_dir.join("stderr"))
                    .unwrap()
                    .write_all(
                        String::from_utf8(result.stderr)
                            .unwrap()
                            .replace(pwd, REPO_DIR_WILDCARD)
                            .as_bytes(),
                    )
                    .unwrap();
            }
            if let Some(exitcode) = result.status.code() {
                if exitcode > 0 {
                    File::create(self.test_dir.join("exitcode"))
                        .unwrap()
                        .write_all(exitcode.to_string().as_bytes())
                        .unwrap();
                }
            }
        }
    }
}

#[fixtures(["tests/fixtures/*"])]
#[cfg_attr(
    feature = "test-js",
    fixtures::ignore(
        paths = "tests/fixtures/013_rejects_gitignore_extended_glob_syntax",
        reason = "The WASM implementation of action validator currently (incorrectly) accepts extended gitignore syntax"
    )
)]
#[test]
fn snapshot(dir: &Path) {
    SnapshotTest::new(dir).execute();
}

```

## File: tests\fixtures\001_basic_workflow\test.json
```
{}

```

## File: tests\fixtures\001_basic_workflow\test.yml
```
name: Test

on:
  push:
  pull_request:
    branches:
      - main

defaults:
  run:
    shell: bash

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup Rust
        uses: actions-rs/toolchain@v1
        with:
          toolchain: stable
          override: true
          default: true

      - name: Check Formatting
        uses: actions-rs/cargo@v1
        with:
          command: fmt
          args: -- --check

      - name: Check with Clippy
        uses: actions-rs/clippy-check@v1
        with:
          args: -- -Dwarnings
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Shellcheck
        uses: ludeeus/action-shellcheck@master

      - name: Install shfmt
        uses: mfinelli/setup-shfmt@master

      - name: Run shfmt
        run: shfmt -d bin/*


  build:
    strategy:
      matrix:
        rust-toolchain:
          - stable
          - nightly
        os:
          - ubuntu-latest
          - macos-latest
          - windows-latest

    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup Rust
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ matrix.rust-toolchain }}
          override: true
          default: true

      - name: Build
        uses: actions-rs/cargo@v1
        with:
          command: build
          args: --release --all-features

```

## File: tests\fixtures\002_basic_action\action.yml
```
name: 'Build something'
description: |
  Build something repeatable.

inputs:
  role:
    description: |
      The role of what's being built.
    required: true

runs:
  using: "composite"
  steps:
    - name: "setup"
      shell: bash
      run: |
        ./setup

    - name: "test"
      shell: bash
      run: |
        ./test

    - name: "build"
      shell: bash
      run: |
        ./build ${{ inputs.role }}

```

## File: tests\fixtures\002_basic_action\test.json
```
{}

```

## File: tests\fixtures\003_successful_globs\excluded_path.json
```
{}

```

## File: tests\fixtures\003_successful_globs\glob.yml
```
name: Test

on:
  push:
    paths:
      - tests/fixtures/003_successful_globs/*
      - '!tests/fixtures/003_successful_globs/*.json'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1

```

## File: tests\fixtures\003_successful_globs\test.json
```
{}

```

## File: tests\fixtures\004a_failing_negative_glob\glob.yml
```
name: Bad globs, no biscuit

on:
  push:
    paths:
      - '!tests/fixtures/004a_failing_negative_glob/*.txt'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1

```

## File: tests\fixtures\004a_failing_negative_glob\test.json
```
{}

```

## File: tests\fixtures\004_failing_globs\glob.yml
```
name: Bad globs, no biscuit

on:
  push:
    paths:
      - tests/fixtures/004_failing_globs/*.txt

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1

```

## File: tests\fixtures\004_failing_globs\test.json
```
{}

```

## File: tests\fixtures\005_conditional_step_in_action\action.yml
```
name: 'Build something conditionally'
description: |
  Build something repeatable.

inputs:
  role:
    description: |
      The role of what's being built.
    required: true

runs:
  using: "composite"
  steps:
    - name: "setup"
      shell: bash
      run: |
        ./setup

    - name: "test"
      shell: bash
      if: ${{ inputs.role }} == 'tester'
      run: |
        ./test

    - name: "build"
      shell: bash
      run: |
        ./build ${{ inputs.role }}

```

## File: tests\fixtures\005_conditional_step_in_action\test.json
```
{}

```

## File: tests\fixtures\006_workflow_dispatch_inputs_options\test.json
```
{}

```

## File: tests\fixtures\006_workflow_dispatch_inputs_options\test.yml
```
name: Test

'on':
  workflow_dispatch:
    inputs:
      ApplicationName:
        description: 'Application name'
        required: true
        type: choice
        options:
          - SomeName
          - SomeOtherName
          - YetMoarNames
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Build
        uses: actions/build@v1

```

## File: tests\fixtures\007_funky_syntax\rust-check.yml
```
# From https://github.com/umccr/reusable-github-actions/blob/45fa579dfaceeec903d1b01396c552fc1b72ace9/.github/workflows/rust-check.yaml,
# re: https://github.com/mpalmer/action-validator/issues/14
on:
  workflow_call:
    inputs:
      rust-version:
        type: string
        required: false
        default: nightly

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out
        uses: actions/checkout@v3
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          profile: minimal
          toolchain: ${{ inputs.rust-version }}
          override: true
          components: rustfmt, clippy
      - name: Set up cargo cache
        uses: actions/cache@v3
        continue-on-error: false
        with:
          path: |
            ~/.cargo/bin/
            ~/.cargo/registry/index/
            ~/.cargo/registry/cache/
            ~/.cargo/git/db/
            target/
          key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.toml') }}

      - name: Format
        uses: actions-rs/cargo@v1
          with:
            command: fmt
            args: --all -- --check
      - name: Clippy
        uses: actions-rs/cargo@v1
          with:
            command: clippy
            args: -- -D warnings
      - name: Install
        uses: actions-rs/cargo@v1
          with:
            command: install
            args: cargo-deny cargo-outdated cargo-udeps cargo-audit cargo-pants
      - name: Check
        run: |
          #cargo deny check
          cargo outdated
          #cargo udeps
          #cargo audit
          cargo pants

```

## File: tests\fixtures\007_funky_syntax\test.json
```
{}

```

## File: tests\fixtures\008_job_dependencies\test.json
```
{}

```

## File: tests\fixtures\008_job_dependencies\test.yml
```
name: Test

on:
  push:
  pull_request:
    branches:
      - main

jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - run: echo "setup"
  check:
    runs-on: ubuntu-latest
    needs: setup
    steps:
      - run: echo "check"
  build:
    runs-on: ubuntu-latest
    needs:
      - check
      - asdf
    steps:
      - run: echo "build"

```

## File: tests\fixtures\009_multi_file\test.json
```
{}

```

## File: tests\fixtures\009_multi_file\valid.yml
```
on:
  workflow_call:
    inputs:
      rust-version:
        type: string
        required: false
        default: nightly

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out
        uses: actions/checkout@v3
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          profile: minimal
          toolchain: ${{ inputs.rust-version }}
          override: true
          components: rustfmt, clippy
      - name: Set up cargo cache
        uses: actions/cache@v3
        continue-on-error: false
        with:
          path: |
            ~/.cargo/bin/
            ~/.cargo/registry/index/
            ~/.cargo/registry/cache/
            ~/.cargo/git/db/
            target/
          key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.toml') }}

      - name: Format
        uses: actions-rs/cargo@v1
        with:
          command: fmt
          args: --all -- --check
      - name: Clippy
        uses: actions-rs/cargo@v1
        with:
          command: clippy
          args: -- -D warnings
      - name: Install
        uses: actions-rs/cargo@v1
        with:
          command: install
          args: cargo-deny cargo-outdated cargo-udeps cargo-audit cargo-pants
      - name: Check
        run: |
          #cargo deny check
          cargo outdated
          #cargo udeps
          #cargo audit
          cargo pants

```

## File: tests\fixtures\009_multi_file\xinvalid.yml
```
on:
  workflow_call:
    inputs:
      rust-version:
        type: string
        required: false
        default: nightly

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out
        uses: actions/checkout@v3
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          profile: minimal
          toolchain: ${{ inputs.rust-version }}
          override: true
          components: rustfmt, clippy
      - name: Set up cargo cache
        uses: actions/cache@v3
        continue-on-error: false
        with:
          path: |
            ~/.cargo/bin/
            ~/.cargo/registry/index/
            ~/.cargo/registry/cache/
            ~/.cargo/git/db/
            target/
          key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.toml') }}

      - name: Format
        uses: actions-rs/cargo@v1
          with:
            command: fmt
            args: --all -- --check
      - name: Clippy
        uses: actions-rs/cargo@v1
          with:
            command: clippy
            args: -- -D warnings
      - name: Install
        uses: actions-rs/cargo@v1
          with:
            command: install
            args: cargo-deny cargo-outdated cargo-udeps cargo-audit cargo-pants
      - name: Check
        run: |
          #cargo deny check
          cargo outdated
          #cargo udeps
          #cargo audit
          cargo pants

```

## File: tests\fixtures\010_missing_shell_in_action\action.yml
```
name: 'missing shell'
description: ''

runs:
  using: "composite"
  steps:
    - name: "say hello"
      run: |
        echo "Hello world"

```

## File: tests\fixtures\010_missing_shell_in_action\test.json
```
{}

```

## File: tests\fixtures\011_subdir_globs\test.json
```
{
  "cli_args": ["--rootdir", "tests/fixtures/011_subdir_globs/subdir", "tests/fixtures/011_subdir_globs/subdir/glob.yml"]
}

```

## File: tests\fixtures\011_subdir_globs\subdir\dummy.json
```

```

## File: tests\fixtures\011_subdir_globs\subdir\glob.yml
```
name: Test

on:
  push:
    paths:
      - g*.yml
      - '!*.json'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1

```

## File: tests\fixtures\012_github_glob_syntax\glob.yml
```
name: Test

on:
  push:
    # https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#filter-pattern-cheat-sheet
    paths:
      - tests/fixtures/012_github_glob_syntax/subdir/artefact.*
      - tests/fixtures/012_github_glob_syntax/**/artefact.a
      - tests/fixtures/012_github_glob_syntax/subdir/artefact.?
      - tests/fixtures/012_github_glob_syntax/subdir/artefact+
      - tests/fixtures/012_github_glob_syntax/subdir/artefact.[bc]
      - tests/fixtures/012_github_glob_syntax/subdir/[0-9]00
      - '!tests/fixtures/012_github_glob_syntax/subdir/ignore'

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1

```

## File: tests\fixtures\012_github_glob_syntax\test.json
```
{}

```

## File: tests\fixtures\013_rejects_gitignore_extended_glob_syntax\glob.yml
```
name: Test

on:
  push:
    paths:
      # The {} syntax is not supported by GitHub actions.
      - tests/fixtures/013_rejects_gitignore_extended_glob_syntax/subdir/asset.{js,jsx}

defaults:
  run:
    shell: bash

jobs:
  glob:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup
        uses: something/setup@v1

      - name: Build
        uses: something/build@v1

```

## File: tests\fixtures\013_rejects_gitignore_extended_glob_syntax\test.json
```
{}

```

## File: tests\fixtures\013_rejects_gitignore_extended_glob_syntax\subdir\asset.js
```

```

