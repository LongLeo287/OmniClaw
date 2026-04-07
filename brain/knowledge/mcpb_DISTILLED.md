---
id: mcpb
type: knowledge
owner: OA_Triage
---
# mcpb
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@anthropic-ai/mcpb",
  "description": "Tools for building MCP Bundles",
  "version": "2.1.2",
  "type": "module",
  "main": "dist/index.js",
  "module": "dist/index.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.js"
    },
    "./browser": {
      "types": "./dist/browser.d.ts",
      "import": "./dist/browser.js",
      "require": "./dist/browser.js"
    },
    "./node": {
      "types": "./dist/node.d.ts",
      "import": "./dist/node.js",
      "require": "./dist/node.js"
    },
    "./cli": {
      "types": "./dist/cli.d.ts",
      "import": "./dist/cli.js",
      "require": "./dist/cli.js"
    },
    "./mcpb-manifest-v0.1.schema.json": "./dist/mcpb-manifest-v0.1.schema.json",
    "./mcpb-manifest-v0.2.schema.json": "./dist/mcpb-manifest-v0.2.schema.json",
    "./mcpb-manifest-v0.3.schema.json": "./dist/mcpb-manifest-v0.3.schema.json",
    "./mcpb-manifest-latest.schema.json": "./dist/mcpb-manifest-latest.schema.json",
    "./schemas": {
      "types": "./dist/schemas/index.d.ts",
      "import": "./dist/schemas/index.js",
      "require": "./dist/schemas/index.js"
    },
    "./schemas/*": {
      "types": "./dist/schemas/*.d.ts",
      "import": "./dist/schemas/*.js",
      "require": "./dist/schemas/*.js"
    },
    "./schemas-loose": {
      "types": "./dist/schemas-loose.d.ts",
      "import": "./dist/schemas-loose.js",
      "require": "./dist/schemas-loose.js"
    }
  },
  "bin": "dist/cli/cli.js",
  "files": [
    "dist",
    "schemas"
  ],
  "scripts": {
    "build": "yarn run build:code && yarn run build:schema",
    "build:code": "tsc",
    "build:schema": "node ./scripts/build-mcpb-schema.js",
    "dev": "tsc --watch",
    "test": "jest",
    "test:watch": "jest --watch",
    "prepublishOnly": "npm run build",
    "fix": "eslint --ext .ts . --fix && prettier -w .",
    "lint": "tsc -p ./tsconfig.json && eslint --ext .ts .",
    "dev-version": "./scripts/create-dev-version.js"
  },
  "author": "Anthropic <support@anthropic.com>",
  "license": "MIT",
  "devDependencies": {
    "@types/jest": "^29.5.14",
    "@types/node": "^22.15.3",
    "@types/node-forge": "1.3.11",
    "@typescript-eslint/eslint-plugin": "^5.62.0",
    "@typescript-eslint/parser": "^5.62.0",
    "eslint": "^8.43.0",
    "eslint-config-prettier": "^8.10.0",
    "eslint-import-resolver-typescript": "^3.6.1",
    "eslint-plugin-import": "^2.29.1",
    "eslint-plugin-prettier": "^5.1.3",
    "eslint-plugin-simple-import-sort": "^10.0.0",
    "jest": "^29.7.0",
    "prettier": "^3.3.3",
    "ts-jest": "^29.3.2",
    "typescript": "^5.6.3"
  },
  "dependencies": {
    "@inquirer/prompts": "^6.0.1",
    "commander": "^13.1.0",
    "fflate": "^0.8.2",
    "galactus": "^1.0.0",
    "ignore": "^7.0.5",
    "node-forge": "^1.3.2",
    "pretty-bytes": "^5.6.0",
    "zod": "^3.25.67",
    "zod-to-json-schema": "^3.24.6"
  },
  "resolutions": {
    "@babel/helpers": "7.27.1",
    "@babel/parser": "7.27.3"
  },
  "packageManager": "yarn@4.10.3+sha512.c38cafb5c7bb273f3926d04e55e1d8c9dfa7d9c3ea1f36a4868fa028b9e5f72298f0b7f401ad5eb921749eb012eb1c3bb74bf7503df3ee43fd600d14a018266f"
}

```

### File: README.md
```md
# MCP Bundles (MCPB)

> **⚠️ IMPORTANT NOTICE: This project is being renamed from DXT (Desktop Extensions) to MCPB (MCP Bundles)**
>
> If you're looking for the DXT tools, they have been renamed to MCPB. Please update your dependencies and tooling:
>
> - `dxt` CLI is now `mcpb`
> - `.dxt` files are now `.mcpb` files
> - `@anthropic-ai/dxt` package will be moved to `@anthropic-ai/mcpb`

MCP Bundles (`.mcpb`) are zip archives containing a local MCP server and a `manifest.json` that describes the server and its capabilities. The format is spiritually similar to Chrome extensions (`.crx`) or VS Code extensions (`.vsix`), enabling end users to install local MCP servers with a single click.

This repository provides three components: The bundle specification in [MANIFEST.md](MANIFEST.md), a CLI tool for creating bundles (see [CLI.md](CLI.md)), and the code used by Claude for macOS and Windows to load and verify MCPB bundles ([src/index.ts](src/index.ts)).

- For developers of local MCP servers, we aim to make distribution and installation of said servers convenient
- For developers of apps supporting local MCP servers, we aim to make it easy to add support for MCPB bundles

Claude for macOS and Windows uses the code in this repository to enable single-click installation of local MCP servers, including a number of end user-friendly features - such as automatic updates, easy configuration of MCP servers and the variables and parameters they need, and a curated directory. We are committed to the open ecosystem around MCP servers and believe that its ability to be universally adopted by multiple applications and services has benefits developers aiming to connect AI tools to other apps and services. Consequently, we're open-sourcing the MCP Bundle specification, toolchain, and the schemas and key functions used by Claude for macOS and Windows to implement its own support of MCP Bundles. It is our hope that the `mcpb` format doesn't just make local MCP servers more portable for Claude, but other AI desktop applications, too.

# For Bundle Developers

At the core, MCPB are simple zip files containing your entire MCP server and a `manifest.json`. Consequently, turning a local MCP server into a bundle is straightforward: You just have to put all your required files in a folder, create a `manifest.json`, and then create an archive.

To make this process easier, this package offers a CLI that helps you with the creation of both the `manifest.json` and the final `.mcpb` file. To install it, run:

```sh
npm install -g @anthropic-ai/mcpb
```

1. In a folder containing your local MCP server, run `mcpb init`. This command will guide you through the creation of a `manifest.json`.
2. Run `mcpb pack` to create a `mcpb` file.
3. Now, any app implementing support for MCPB can run your local MCP server. As an example, open the file with Claude for macOS and Windows to show an installation dialog.

You can find the full spec for the `manifest.json` and all its mandatory and optional fields in [MANIFEST.md](MANIFEST.md). Examples for bundles can be found in [examples](./examples/).

## Prompt Template for AI Tools

AI tools like Claude Code are particularly good at creating MCP bundles when informed about the spec. When prompting an AI coding tool to build a bundle, briefly explain what your bundle aims to do - then add the following context to your instructions.

> I want to build this as a MCP Bundle, abbreviated as "MCPB". Please follow these steps:
>
> 1. **Read the specifications thoroughly:**
>    - https://github.com/anthropics/mcpb/blob/main/README.md - MCPB architecture overview, capabilities, and integration
>      patterns
>    - https://github.com/anthropics/mcpb/blob/main/MANIFEST.md - Complete bundle manifest structure and field definitions
>    - https://github.com/anthropics/mcpb/tree/main/examples - Reference implementations including a "Hello World" example
> 2. **Create a proper bundle structure:**
>    - Generate a valid manifest.json following the MANIFEST.md spec
>    - Implement an MCP server using @modelcontextprotocol/sdk with proper tool definitions
>    - Include proper error handling, security measures, and timeout management
> 3. **Follow best development practices:**
>    - Implement proper MCP protocol communication via stdio transport
>    - Structure tools with clear schemas, validation, and consistent JSON responses
>    - Make use of the fact that this bundle will be running locally
>    - Add appropriate logging and debugging capabilities
>    - Include proper documentation and setup instructions
> 4. **Test considerations:**
>    - Validate that all tool calls return properly structured responses
>    - Verify manifest loads correctly and host integration works
>
> Generate complete, production-ready code that can be immediately tested. Focus on defensive programming, clear error messages, and following the exact MCPB specifications to ensure compatibility with the ecosystem.

## Directory Structures

### Minimal Bundle

A `manifest.json` is the only required file.

### Example: Node.js Bundle

```
bundle.mcpb (ZIP file)
├── manifest.json         # Required: Bundle metadata and configuration
├── server/               # Server files
│   └── index.js          # Main entry point
├── node_modules/         # Bundled dependencies
├── package.json          # Optional: NPM package definition
├── icon.png              # Optional: Bundle icon
└── assets/               # Optional: Additional assets
```

### Example: Python Bundle

```
bundle.mcpb (ZIP file)
├── manifest.json         # Required: Bundle metadata and configuration
├── server/               # Server files
│   ├── main.py           # Main entry point
│   └── utils.py          # Additional modules
├── lib/                  # Bundled Python packages
├── requirements.txt      # Optional: Python dependencies list
└── icon.png              # Optional: Bundle icon
```

### Example: Binary Bundle

```
bundle.mcpb (ZIP file)
├── manifest.json         # Required: Bundle metadata and configuration
├── server/               # Server files
│   ├── my-server         # Unix executable
│   ├── my-server.exe     # Windows executable
└── icon.png              # Optional: Bundle icon
```

### Language Choice Recommendation

**We recommend implementing MCP servers in Node.js** rather than Python to reduce installation friction. Node.js ships with Claude for macOS and Windows, which means your bundle will work out-of-the-box for users without requiring them to install additional Python runtimes (or you to package them manually).

### Bundling Dependencies

**UV Runtime (Experimental - v0.4+):**

- Use `server.type = "uv"` in manifest
- Include `pyproject.toml` with dependencies (no bundled packages needed)
- Host application manages Python and dependencies automatically
- Works cross-platform without user Python installation
- See `examples/hello-world-uv`

**Python Bundles (Traditional):**

- Use `server.type = "python"` in manifest
- Bundle all required packages in `server/lib/` directory
- OR bundle a complete virtual environment in `server/venv/`
- Use tools like `pip-tools`, `poetry`, or `pipenv` to create reproducible bundles
- Set `PYTHONPATH` to include bundled packages via `mcp_config.env`
- **Limitation**: Cannot portably bundle compiled dependencies (e.g., pydantic, which the MCP Python SDK requires)

**Node.js Bundles:**

- Run `npm install --production` to create `node_modules`
- Bundle the entire `node_modules` directory with your bundle
- Use `npm ci` or `yarn install --frozen-lockfile` for reproducible builds
- Server entry point specified in manifest.json's `server.entry_point`

**Binary Bundles:**

- Static linking preferred for maximum compatibility
- Include all required shared libraries if dynamic linking used
- Test on clean systems without development tools

# Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## Development Setup

```sh
# Clone the repository
git clone https://github.com/anthropics/mcpb.git
cd mcpb

# Install dependencies
yarn

# Build the project
yarn build

# Run tests
yarn test
```

## Release Process

1. Update version in `package.json`
2. Create a pull request with version bump
3. After merge, create a GitHub release
4. Package will be automatically published to npm

# License

This project is licensed under the Apache License 2.0 for new contributions, with existing code under MIT - see the [LICENSE](LICENSE) file for details.

```

### File: examples\README.md
```md
# MCPB Examples

This directory contains example MCP Bundles that demonstrate the MCPB format and manifest structure. These are **reference implementations** designed to illustrate how to build MCPB extensions.

## ⚠️ Not Production Ready

**Important:** These examples are **NOT intended for production use**. They serve as:

- Demonstrations of the MCPB manifest format
- Templates for building your own extensions
- Simple MCP server implementations for testing

But, the MCP servers themselves are not robust secure production ready servers and should not be relied upon for production use.

## Examples Included

| Example               | Type    | Demonstrates                             |
| --------------------- | ------- | ---------------------------------------- |
| `hello-world-node`    | Node.js | Basic MCP server with simple time tool   |
| `chrome-applescript`  | Node.js | Browser automation via AppleScript       |
| `file-manager-python` | Python  | File system operations and path handling |

## Usage

Each example includes its own `manifest.json` and can be packed with:

```bash
dxt pack examples/hello-world-node
```

Use these as starting points for your own extensions, but ensure you implement proper security measures before deploying to users.

```

### File: .eslintrc.json
```json
{
  "env": {
    "es6": true
  },
  "extends": [
    "eslint:recommended",
    "prettier",
    "plugin:@typescript-eslint/eslint-recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:import/recommended",
    "plugin:import/typescript"
  ],
  "plugins": ["@typescript-eslint", "import", "prettier", "simple-import-sort"],
  "parser": "@typescript-eslint/parser",
  "ignorePatterns": ["dist/*", "node_modules/*", "*.js"],
  "parserOptions": {
    "project": "./tsconfig.json"
  },
  "settings": {
    "import/resolver": {
      // Enables eslint-import-resolver-typescript
      "typescript": {}
    }
  },
  "rules": {
    "prettier/prettier": "warn",
    // Require all external imports to be declared as a dependency
    "import/no-extraneous-dependencies": [
      "error",
      {
        "packageDir": "./"
      }
    ],
    // Imports must not cause cyclical dependencies
    "import/no-cycle": [
      "error",
      { "allowUnsafeDynamicCyclicDependency": true }
    ],
    "import/no-named-as-default-member": "off",
    // Imports must be ordered appropriately
    "simple-import-sort/imports": [
      "error",
      {
        "groups": [
          // Side effect imports.
          ["^\\u0000"],
          // Node.js builtins prefixed with `node:`.
          ["^node:"],
          // Packages.
          // Things that start with a letter (or digit or underscore), or `@` followed by a letter.
          ["^@?\\w"],
          // Absolute imports
          ["^@/"],
          // Relative imports.
          // Anything that starts with a dot.
          ["^\\."]
        ]
      }
    ],
    "simple-import-sort/exports": "error",
    // Imports must be placed before non-import statements
    "import/first": "error",
    "import/newline-after-import": "error",
    "import/no-duplicates": "error",

    // Require a space at the start of comments
    "spaced-comment": [
      "error",
      "always",
      {
        "markers": ["/"]
      }
    ],

    // Make sure switch-case doesn't accidentally fall-through https://eslint.org/docs/latest/rules/no-fallthrough
    "no-fallthrough": "error",

    "@typescript-eslint/ban-ts-comment": "warn",

    "@typescript-eslint/consistent-type-imports": [
      "error",
      {
        "prefer": "type-imports"
      }
    ],

    // Disallow annotating types where the type can be easily inferred
    "@typescript-eslint/no-inferrable-types": [
      "error",
      {
        "ignoreParameters": false,
        "ignoreProperties": false
      }
    ],
    // Allow non-null assertions
    "@typescript-eslint/no-non-null-assertion": "off",
    // Disallow using 'any' explicitly in annotations
    "@typescript-eslint/no-explicit-any": "error",
    // Require promise outcomes to be properly handled
    "@typescript-eslint/no-floating-promises": "error",
    // Turn off base eslint rule in favor of typescript-eslint version
    // to avoid getting eslint errors on type signatures
    "no-unused-vars": "off",
    // Disallow unused variables and imports
    "@typescript-eslint/no-unused-vars": [
      "warn",
      {
        "args": "after-used",
        "argsIgnorePattern": "^_",
        "varsIgnorePattern": "^_",
        "ignoreRestSiblings": true,
        "vars": "all",
        "args": "after-used",
        "destructuredArrayIgnorePattern": "^_"
      }
    ],

    // Disallow empty functions
    // If a function is intentionally empty, adding a comment line
    // inside the function body is enough to pass this rule
    "@typescript-eslint/no-empty-function": "error"
  },
  "overrides": [
    {
      "files": ["test/**/*.ts"],
      "parserOptions": {
        "project": "./tsconfig.test.json"
      }
    }
  ]
}

```

### File: CLI.md
```md
# MCPB CLI Documentation

The MCPB CLI provides tools for building MCP Bundles.

## Installation

```bash
npm install -g @anthropic-ai/mcpb
```

```
Usage: mcpb [options] [command]

Tools for building MCP Bundles

Options:
  -V, --version              output the version number
  -h, --help                 display help for command

Commands:
  init [directory]           Create a new MCPB extension manifest
  validate <manifest>        Validate a MCPB manifest file
  pack <directory> [output]  Pack a directory into a MCPB extension
  sign [options] <mcpb-file>  Sign a MCPB extension file
  verify <mcpb-file>          Verify the signature of a MCPB extension file
  info <mcpb-file>            Display information about a MCPB extension file
  unsign <mcpb-file>          Remove signature from a MCPB extension file
  help [command]             display help for command
```

## Commands

### `mcpb init [directory]`

Creates a new MCPB extension manifest interactively.

```bash
# Initialize in current directory
mcpb init

# Initialize in a specific directory
mcpb init my-extension/
```

The command will prompt you for:

- Extension name (defaults from package.json or folder name)
- Author name (defaults from package.json)
- Extension ID (auto-generated from author and extension name)
- Display name
- Version (defaults from package.json or 1.0.0)
- Description
- Author email and URL (optional)
- Server type (Node.js, Python, or Binary)
- Entry point (with sensible defaults per server type)
- Tools configuration
- Keywords, license, and repository information

After creating the manifest, it provides helpful next steps based on your server type.

### `mcpb validate <path>`

Validates a MCPB manifest file against the schema. You can provide either a direct path to a manifest.json file or a directory containing one.

```bash
# Validate specific manifest file
mcpb validate manifest.json

# Validate manifest in directory
mcpb validate ./my-extension
mcpb validate .
```

### `mcpb pack <directory> [output]`

Packs a directory into a MCPB extension file.

```bash
# Pack current directory into extension.mcpb
mcpb pack .

# Pack with custom output filename
mcpb pack my-extension/ my-extension-v1.0.mcpb
```

The command automatically:

- Validates the manifest.json
- Excludes common development files (.git, node_modules/.cache, .DS_Store, etc.)
- Creates a compressed .mcpb file (ZIP with maximum compression)

### `mcpb sign <mcpb-file>`

Signs a MCPB extension file with a certificate.

```bash
# Sign with default certificate paths
mcpb sign my-extension.mcpb

# Sign with custom certificate and key
mcpb sign my-extension.mcpb --cert /path/to/cert.pem --key /path/to/key.pem

# Sign with intermediate certificates
mcpb sign my-extension.mcpb --cert cert.pem --key key.pem --intermediate intermediate1.pem intermediate2.pem

# Create and use a self-signed certificate
mcpb sign my-extension.mcpb --self-signed
```

Options:

- `--cert, -c`: Path to certificate file (PEM format, default: cert.pem)
- `--key, -k`: Path to private key file (PEM format, default: key.pem)
- `--intermediate, -i`: Paths to intermediate certificate files
- `--self-signed`: Create a self-signed certificate if none exists

### `mcpb verify <mcpb-file>`

Verifies the signature of a signed MCPB extension file.

```bash
mcpb verify my-extension.mcpb
```

Output includes:

- Signature validity status
- Certificate subject and issuer
- Certificate validity dates
- Certificate fingerprint
- Warning if self-signed

### `mcpb info <mcpb-file>`

Displays information about a MCPB extension file.

```bash
mcpb info my-extension.mcpb
```

Shows:

- File size
- Signature status
- Certificate details (if signed)

### `mcpb unsign <mcpb-file>`

Removes the signature from a MCPB extension file (for development/testing).

```bash
mcpb unsign my-extension.mcpb
```

## Certificate Requirements

For signing extensions, you need:

1. **Certificate**: X.509 certificate in PEM format
   - Should have Code Signing extended key usage
   - Can be self-signed (for development) or CA-issued (for production)

2. **Private Key**: Corresponding private key in PEM format
   - Must match the certificate's public key

3. **Intermediate Certificates** (optional): For CA-issued certificates
   - Required for proper certificate chain validation

## Example Workflows

### Quick Start with Init

```bash
# 1. Create a new extension directory
mkdir my-awesome-extension
cd my-awesome-extension

# 2. Initialize the extension
mcpb init

# 3. Follow the prompts to configure your extension
# The tool will create a manifest.json with all necessary fields

# 4. Create your server implementation based on the entry point you specified

# 5. Pack the extension
mcpb pack .

# 6. (Optional) Sign the extension
mcpb sign my-awesome-extension.mcpb --self-signed
```

### Development Workflow

```bash
# 1. Create your extension
mkdir my-extension
cd my-extension

# 2. Initialize with mcpb init or create manifest.json manually
mcpb init

# 3. Implement your server
# For Node.js: create server/index.js
# For Python: create server/main.py
# For Binary: add your executable

# 4. Validate manifest
mcpb validate manifest.json

# 5. Pack extension
mcpb pack . my-extension.mcpb

# 6. (Optional) Sign for testing
mcpb sign my-extension.mcpb --self-signed

# 7. Verify signature
mcpb verify my-extension.mcpb

# 8. Check extension info
mcpb info my-extension.mcpb
```

### Production Workflow

```bash
# 1. Pack your extension
mcpb pack my-extension/

# 2. Sign with production certificate
mcpb sign my-extension.mcpb \
  --cert production-cert.pem \
  --key production-key.pem \
  --intermediate intermediate-ca.pem root-ca.pem

# 3. Verify before distribution
mcpb verify my-extension.mcpb
```

## Excluded Files

When packing an extension, the following files/patterns are automatically excluded:

- `.DS_Store`, `Thumbs.db`
- `.gitignore`, `.git/`
- `*.log`, `npm-debug.log*`, `yarn-debug.log*`, `yarn-error.log*`
- `.npm/`, `.npmrc`, `.yarnrc`, `.yarn/`, `.pnp.*`
- `node_modules/.cache/`, `node_modules/.bin/`
- `*.map`
- `.env.local`, `.env.*.local`
- `package-lock.json`, `yarn.lock`

### Custom Exclusions with .mcpbignore

You can create a `.mcpbignore` file in your extension directory to specify additional files and patterns to exclude during packing. This works similar to `.npmignore` or `.gitignore`:

```
# .mcpbignore example
# Comments start with #
*.test.js
src/**/*.test.ts
coverage/
*.log
.env*
temp/
docs/
```

The `.mcpbignore` file supports:

- **Exact matches**: `filename.txt`
- **Simple globs**: `*.log`, `temp/*`
- **Directory paths**: `docs/`, `coverage/`
- **Comments**: Lines starting with `#` are ignored
- **Empty lines**: Blank lines are ignored

When a `.mcpbignore` file is found, the CLI will display the number of additional patterns being applied. These patterns are combined with the default exclusion list.

## Technical Details

### Signature Format

MCPB uses PKCS#7 (Cryptographic Message Syntax) for digital signatures:

- Signatures are stored in DER-encoded PKCS#7 SignedData format
- The signature is appended to the MCPB file with markers (`MCPB_SIG_V1` and `MCPB_SIG_END`)
- The entire MCPB content (excluding the signature block) is signed
- Detached signature format - the original ZIP content remains unmodified

### Signature Structure

```
[Original MCPB ZIP content]
MCPB_SIG_V1
[Base64-encoded PKCS#7 signature]
MCPB_SIG_END
```

This approach allows:

- Backward compatibility (unsigned MCPB files are valid ZIP files)
- Easy signature verification and removal
- Support for certificate chains with intermediate certificates

```

### File: CONTRIBUTING.md
```md
# Contributing to MCPB

Thank you for your interest in contributing to MCPB! We welcome contributions from the community.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/mcpb.git`
3. Install dependencies: `yarn`
4. Build the project: `yarn build`
5. Run tests: `yarn test`

## Development Workflow

1. Create a new branch for your feature or bugfix: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run linting: `yarn lint`
4. Run tests to ensure everything passes: `yarn test`
5. Commit your changes with a clear, descriptive commit message (all commits must be signed - see [Commit Signing](#commit-signing))
6. Push to your fork and submit a pull request

## Code Standards

- **TypeScript**: All code should be written in TypeScript with proper type definitions
- **Linting**: Run `yarn lint` before committing. Use `yarn fix` to auto-fix formatting issues
- **Testing**: Add tests for new features and bug fixes
- **Documentation**: Update relevant documentation (README.md, MANIFEST.md, etc.) when adding or changing functionality

## Commit Signing

**All commits must be signed.** This helps verify the authenticity of contributions.

To set up commit signing, see [GitHub's documentation on commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification).

## Pull Request Process

1. Ensure your PR description clearly describes the problem and solution
2. Reference any related issues in your PR description
3. Make sure all tests pass and linting is clean
4. Verify that all commits are signed
5. Update documentation as needed
6. Wait for review from maintainers

## Types of Contributions

### Bug Reports

When filing a bug report, please include:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Version information (`mcpb --version`)
- Relevant logs or error messages

### Feature Requests

We welcome feature suggestions! Please:

- Clearly describe the feature and use case
- Explain why this would be valuable to users
- Consider if it aligns with the project's goals

### Code Contributions

We especially welcome:

- Bug fixes
- Documentation improvements
- Test coverage improvements
- New features (please discuss in an issue first for large changes)

## Testing

- Write unit tests for new functionality
- Ensure existing tests still pass
- Test manually with real MCP bundles when applicable

## Questions?

Feel free to open an issue for questions about contributing or the project in general.

## License

By contributing to MCPB, you agree that your contributions will be licensed under the MIT License.

```

### File: jest.config.js
```js
export default {
  preset: "ts-jest",
  testEnvironment: "node",
  testMatch: ["**/test/**/*.test.ts"],
  collectCoverageFrom: ["src/**/*.ts", "!src/**/*.d.ts"],
  moduleFileExtensions: ["ts", "js", "json"],
  transform: {
    "^.+\\.ts$": [
      "ts-jest",
      {
        tsConfig: "tsconfig.test.json",
      },
    ],
  },
  moduleNameMapper: {
    "^(\\.{1,2}/.*)\\.js$": "$1",
  },
};

```

### File: MANIFEST.md
```md
# MCPB Manifest.json Spec

Current version: `0.3`
Last updated: 2025-12-02

## Manifest Schema

The `manifest.json` file contains all extension metadata and configuration. Most fields are optional.

A basic `manifest.json` with just the required fields looks like this:

```jsonc
{
  "manifest_version": "0.3", // Manifest spec version this manifest conforms to
  "name": "my-extension", // Machine-readable name (used for CLI, APIs)
  "version": "1.0.0", // Semantic version of your extension
  "description": "A simple MCP extension", // Brief description of what the extension does
  "author": {
    // Author information (required)
    "name": "Extension Author", // Author's name (required field)
  },
  "server": {
    // Server configuration (required)
    "type": "node", // Server type: "node", "python", or "binary"
    "entry_point": "server/index.js", // Path to the main server file
    "mcp_config": {
      // MCP server configuration
      "command": "node", // Command to run the server
      "args": [
        // Arguments passed to the command
        "${__dirname}/server/index.js", // ${__dirname} is replaced with the extension's directory
      ],
    },
  },
}
```

```json
{
  "manifest_version": "0.3",
  "name": "my-extension",
  "version": "1.0.0",
  "description": "A simple MCP extension",
  "author": {
    "name": "Extension Author"
  },
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"],
      "env": {
        "API_KEY": "${user_config.api_key}"
      }
    }
  },
  "user_config": {
    "api_key": {
      "type": "string",
      "title": "API Key",
      "description": "Your API key for authentication",
      "sensitive": true,
      "required": true
    }
  }
}
```

A full `manifest.json` with most of the optional fields looks like this:

```json
{
  "manifest_version": "0.3",
  "name": "My MCP Extension",
  "display_name": "My Awesome MCP Extension",
  "version": "1.0.0",
  "description": "A brief description of what this extension does",
  "long_description": "A detailed description that can include multiple paragraphs explaining the extension's functionality, use cases, and features. It supports basic markdown.",
  "author": {
    "name": "Your Name",
    "email": "yourname@example.com",
    "url": "https://your-website.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/your-username/my-mcp-extension.git"
  },
  "homepage": "https://example.com/my-extension",
  "documentation": "https://docs.example.com/my-extension",
  "support": "https://github.com/your-username/my-extension/issues",
  "icon": "icon.png",
  "icons": [
    {
      "src": "assets/icons/icon-16-light.png",
      "size": "16x16",
      "theme": "light"
    },
    {
      "src": "assets/icons/icon-16-dark.png",
      "size": "16x16",
      "theme": "dark"
    }
  ],
  "screenshots": [
    "assets/screenshots/screenshot1.png",
    "assets/screenshots/screenshot2.png"
  ],
  "localization": {
    "resources": "custom-directory-for-mcpb-resources/${locale}.json",
    "default_locale": "en-US"
  },
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["server/index.js"],
      "env": {
        "ALLOWED_DIRECTORIES": "${user_config.allowed_directories}"
      }
    }
  },
  "tools": [
    {
      "name": "search_files",
      "description": "Search for files in a directory"
    }
  ],
  "prompts": [
    {
      "name": "poetry",
      "description": "Have the LLM write poetry",
      "arguments": ["topic"],
      "text": "Write a creative poem about the following topic: ${arguments.topic}"
    }
  ],
  "tools_generated": true,
  "keywords": ["api", "automation", "productivity"],
  "license": "MIT",
  "privacy_policies": ["https://example.com/privacy"],
  "compatibility": {
    "claude_desktop": ">=1.0.0",
    "platforms": ["darwin", "win32", "linux"],
    "runtimes": {
      "python": ">=3.8",
      "node": ">=16.0.0"
    }
  },
  "user_config": {
    "allowed_directories": {
      "type": "directory",
      "title": "Allowed Directories",
      "description": "Directories the server can access",
      "multiple": true,
      "required": true,
      "default": ["${HOME}/Desktop"]
    },
    "api_key": {
      "type": "string",
      "title": "API Key",
      "description": "Your API key for authentication",
      "sensitive": true,
      "required": false
    },
    "max_file_size": {
      "type": "number",
      "title": "Maximum File Size (MB)",
      "description": "Maximum file size to process",
      "default": 10,
      "min": 1,
      "max": 100
    }
  },
  "_meta": {
    "com.microsoft.windows": {
      "package_family_name": "MyMcpMSIXPackage_51g09708xawrw",
      "static_responses": {
        "initialize": {
          "capabilities": {},
          "instructions": "When the user wants to search files, use the search_files tool but only after asking them whether the files are local.",
          "protocolVersion": "2025-06-18",
          "serverInfo": {
            "name": "MyMCPExtension",
            "title": "My MCP Extension - Pro Edition",
            "version": "1.0.0"
          }
        },
        "tools/list": {
          "tools": [
            {
              "name": "search_files",
              "title": "File search",
              "description": "Search for files in a directory",
              "inputSchema": {
                "type": "object",
                "properties": {
                  "fileSpec": {
                    "type": "string",
                    "description": "The file name to search for. Wildcards are supported"
                  }
                },
                "required": ["fileSpec"]
              },
              "outputSchema": {
                "type": "object",
                "properties": {
                  "searchResults": {
                    "type": "array",
                    "description": "The list of file paths that were found",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

## Field Definitions

### Required Fields

- **manifest_version**: Specification version this extension conforms to
- **name**: Machine-readable name (used for CLI, APIs)
- **version**: Semantic version (semver)
- 🌎 **description**: Brief description. This field is localizable.
- 🌎 **author**: Author information object with name (required, localizable), email (optional), and url (optional)
- **server**: Server configuration object

### Optional Fields

- **icon**: Path to a png icon file, either relative in the package or a `https://` url.
- **icons**: Array of icon descriptors (`src`, `size`, optional `theme`) for light/dark or size-specific assets.
- 🌎 **display_name**: Human-friendly name for UI display. This field is localizable.
- 🌎 **long_description**: Detailed description for extension stores, markdown. This field is localizable.
- **repository**: Source code repository information (type and url).
- **homepage**: Extension homepage URL.
- **documentation**: Documentation URL.
- **support**: Support/issues URL.
- **screenshots**: Array of screenshot paths.
- 🌎 **tools**: Array of tools the extension provides. This field is localizable.
- **tools_generated**: Boolean indicating the server generates additional tools at runtime (default: false).
- 🌎 **prompts**: Array of prompts the extension provides. This field is localizable.
- **prompts_generated**: Boolean indicating the server generates additional prompts at runtime (default: false).
- 🌎 **keywords**: Search keywords. This field is localizable.
- **license**: License identifier.
- **privacy_policies**: Array of URLs to privacy policies for external services that handle user data. Required when the extension connects to external services (first- or third-party) that process user data. Each URL should link to the respective service's privacy policy document.
- **compatibility**: Compatibility requirements (client app version, platforms, and runtime versions).
- **user_config**: User-configurable options for the extension (see User Configuration section).
- **\_meta**: Platform-specific client integration metadata (e.g., Windows `package_family_name`, macOS bundle identifiers) enabling tighter OS/app store integration. The keys in the `_meta` object are reverse-DNS namespaced, and the values are a dictionary of platform-specific metadata.
- **localization**: Location of translated strings for user-facing fields (`resources` path containing a `${locale}` placeholder and `default_locale`).

### Localization

Provide localized strings without bloating the manifest by pointing to external per-locale resource files. A localization entry looks like this:

```jsonc
"localization": {
  "resources": "relative-path-to-resources/${locale}.json",
  "default_locale": "en-US"
}
```

- `resources` must include a `${locale}` placeholder. Clients resolve it relative to the server install directory.
  - This property is optional, and its default value is **`mcpb-resources/${locale}.json`**.
- `default_locale` must be a valid [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) identifier such as `en-US` or `zh-Hans`.
  - This property is optional, and its default value is `en-US`.
- Values for the default locale stay in the main manifest; localized files only need to contain overrides.

For tools and prompts, the descriptions are also localizable.

#### Client guidelines

- if a client wants to show tool or prompt descriptions in their UI, the client should look for the locale-specific description override in the corresponding per-locale file.
- clients should only look for tools/prompts present in the manifest.json, i.e. prompts and tools that only exist in the per-locale file should be ignored.
- Clients should apply locale fallbacks if the client/user locale is not represented by the server. For example, if the user is in the `es-UY` locale but the server does not include that per-locale file, the client should look for an approrpiate fallback, e.g. `es-MX` or `es-ES`, or fall back to the values in the manifest.

### Icons

Use the `icons` array when you need multiple icon variants (different sizes or themes):

```json
"icons": [
  { "src": "assets/icons/icon-16-light.png", "size": "16x16", "theme": "light" },
  { "src": "assets/icons/icon-16-dark.png", "size": "16x16", "theme": "dark" }
]
```

- `size` must be in `WIDTHxHEIGHT` form (e.g., `128x128`).
- `theme` is optional; use values like `light`, `dark`, or platform-specific labels (e.g., `high-contrast`).
- The legacy `icon` field remains supported for single assets—clients use it when `icons` is omitted.

## Compatibility

The `compatibility` object specifies all requirements for running the extension. All fields, including the `compatibility` field itself, are optional. If you specify nothing, clients implementing MCPB are encouraged to run the extension on any system.

```json
{
  "compatibility": {
    "claude_desktop": ">=1.0.0",
    "my_client": ">1.0.0",
    "other_client": ">=2.0.0 <3.0.0",
    "platforms": ["darwin", "win32", "linux"],
    "runtimes": {
      "python": ">=3.8",
      "node": ">=16.0.0"
    }
  }
}
```

### Fields

#### Client Version Constraints

The compatibility object supports version constraints for any client application:

- **claude_desktop**: Minimum Claude Desktop version required (uses semver)
- **my_client**: Version constraint for a custom client (uses semver)
- **Other client names**: You can add version constraints for any client application

All client version constraints use semver syntax (e.g., `">=1.0.0"`, `">1.0.0 <2.0.0"`, `"^1.2.3"`).

#### System Requirements

- **platforms**: Array of supported platforms (`darwin`, `win32`, `linux`). These match Node.js `process.platform` and Python's `sys.platform` values. If omitted, all platforms are supported
- **runtimes**: Runtime version requirements
  - Only specify the runtime(s) your extension actually uses
  - For Python extensions: specify `python` version
  - For Node.js extensions: specify `node` version
  - Binary extensions don't need runtime specifications

**Note**: Use `darwin` for macOS, `win32` for Windows, and `linux` for Linux systems

### Examples

**Python Extension:**

```json
{
  "server": {
    "type": "python",
    "entry_point": "server/main.py"
  },
  "compatibility": {
    "claude_desktop": ">=0.10.0",
    "platforms": ["darwin", "win32", "linux"],
    "runtimes": {
      "python": ">=3.8,<4.0"
    }
  }
}
```

**Node.js Extension that only supports macOS:**

```json
{
  "server": {
    "type": "node",
    "entry_point": "server/index.js"
  },
  "compatibility": {
    "claude_desktop": ">=0.10.0",
    "platforms": ["darwin"],
    "runtimes": {
      "node": ">=16.0.0"
    }
  }
}
```

**Binary Extension (no runtime needed):**

```json
{
  "server": {
    "type": "binary",
    "entry_point": "server/my-tool"
  },
  "compatibility": {
    "claude_desktop": ">=0.10.0",
    "platforms": ["darwin", "win32"]
  }
}
```

## Server Configuration

The `server` object defines how to run the MCP server:

### Server Types

Four server types are supported:

- **`node`**: Node.js server with bundled dependencies
- **`python`**: Python server with bundled dependencies
- **`binary`**: Compiled executable
- **`uv`**: Python server using UV runtime (experimental, v0.4+)

### UV Runtime (Experimental, v0.4+)

> **Note:** UV runtime support is experimental and may change in future versions.

The `uv` server type enables cross-platform Python extensions without bundling dependencies. Instead, dependencies are declared in `pyproject.toml` and installed by the host application using UV.

**Benefits:**
- Cross-platform support (Windows, macOS, Linux; Intel, ARM)
- Small bundle size (~100 KB vs 5-10 MB)
- Handles compiled dependencies (pydantic, numpy, etc.)
- No user Python installation required

**Example:**
```json
{
  "manifest_version": "0.4",
  "server": {
    "type": "uv",
    "entry_point": "src/server.py"
  }
}
```

**Requirements:**
- Must include `pyproject.toml` with dependencies
- Must NOT include `server/lib/` or `server/venv/`
- `mcp_config` is optional (host manages execution)

**Package structure:**
```
extension.mcpb
├── manifest.json       # server.type = "uv"
├── pyproject.toml      # Dependencies
├── .mcpbignore        # Exclude .venv, server/lib
└── src/
    └── server.py
```

See `examples/hello-world-uv` for a complete example.

### Node, Python, and Binary Types

1. **Python**: `server.type = "python"`
   - Requires `entry_point` to Python file
   - All dependencies must be bundled in the MCPB
   - Can use `server/lib` for packages or `server/venv` for full virtual environment
   - Python runtime version specified in `compa
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "display": "Default",
  "compilerOptions": {
    "target": "es2024",
    "lib": ["ES2023"],

    "module": "node18",
    "moduleResolution": "node16",
    "esModuleInterop": true,

    // Path settings
    "rootDir": "./src",
    "outDir": "./dist",

    // Type checking
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,

    // Emit settings
    "declaration": true,
    "noEmit": false,
    "inlineSources": false,
    "isolatedModules": false,

    // Other settings
    "allowJs": true,
    "resolveJsonModule": true,
    "incremental": true,
    "preserveWatchOutput": true,
    "types": ["node"]
  },
  "include": ["src/**/*.ts", "src/*.ts"],
  "exclude": ["node_modules", "dist"]
}

```

### File: tsconfig.test.json
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "noEmit": true,
    "module": "node18",
    "moduleResolution": "node16",
    "types": ["node", "jest"]
  },
  "include": ["src/**/*.ts", "test/**/*.ts"]
}

```

### File: schemas\mcpb-manifest-latest.schema.json
```json
{
  "type": "object",
  "properties": {
    "$schema": {
      "type": "string"
    },
    "dxt_version": {
      "type": "string",
      "const": "0.3",
      "description": "@deprecated Use manifest_version instead"
    },
    "manifest_version": {
      "type": "string",
      "const": "0.3"
    },
    "name": {
      "type": "string"
    },
    "display_name": {
      "type": "string"
    },
    "version": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "long_description": {
      "type": "string"
    },
    "author": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "email": {
          "type": "string",
          "format": "email"
        },
        "url": {
          "type": "string",
          "format": "uri"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "repository": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "url": {
          "type": "string",
          "format": "uri"
        }
      },
      "required": [
        "type",
        "url"
      ],
      "additionalProperties": false
    },
    "homepage": {
      "type": "string",
      "format": "uri"
    },
    "documentation": {
      "type": "string",
      "format": "uri"
    },
    "support": {
      "type": "string",
      "format": "uri"
    },
    "icon": {
      "type": "string"
    },
    "icons": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "src": {
            "type": "string"
          },
          "size": {
            "type": "string",
            "pattern": "^\\d+x\\d+$"
          },
          "theme": {
            "type": "string",
            "minLength": 1
          }
        },
        "required": [
          "src",
          "size"
        ],
        "additionalProperties": false
      }
    },
    "screenshots": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "localization": {
      "type": "object",
      "properties": {
        "resources": {
          "type": "string",
          "pattern": "\\$\\{locale\\}"
        },
        "default_locale": {
          "type": "string",
          "pattern": "^[A-Za-z0-9]{2,8}(?:-[A-Za-z0-9]{1,8})*$"
        }
      },
      "required": [
        "resources",
        "default_locale"
      ],
      "additionalProperties": false
    },
    "server": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "python",
            "node",
            "binary"
          ]
        },
        "entry_point": {
          "type": "string"
        },
        "mcp_config": {
          "type": "object",
          "properties": {
            "command": {
              "type": "string"
            },
            "args": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "env": {
              "type": "object",
              "additionalProperties": {
                "type": "string"
              }
            },
            "platform_overrides": {
              "type": "object",
              "additionalProperties": {
                "type": "object",
                "properties": {
                  "command": {
                    "$ref": "#/properties/server/properties/mcp_config/properties/command"
                  },
                  "args": {
                    "$ref": "#/properties/server/properties/mcp_config/properties/args"
                  },
                  "env": {
                    "$ref": "#/properties/server/properties/mcp_config/properties/env"
                  }
                },
                "additionalProperties": false
              }
            }
          },
          "required": [
            "command"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "type",
        "entry_point",
        "mcp_config"
      ],
      "additionalProperties": false
    },
    "tools": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "tools_generated": {
      "type": "boolean"
    },
    "prompts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "arguments": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "text": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "text"
        ],
        "additionalProperties": false
      }
    },
    "prompts_generated": {
      "type": "boolean"
    },
    "keywords": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "license": {
      "type": "string"
    },
    "privacy_policies": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      }
    },
    "compatibility": {
      "type": "object",
      "properties": {
        "claude_desktop": {
          "type": "string"
        },
        "platforms": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "darwin",
              "win32",
              "linux"
            ]
          }
        },
        "runtimes": {
          "type": "object",
          "properties": {
            "python": {
              "type": "string"
            },
            "node": {
              "type": "string"
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    },
    "user_config": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "boolean",
              "directory",
              "file"
            ]
          },
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "required": {
            "type": "boolean"
          },
          "default": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              },
              {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            ]
          },
          "multiple": {
            "type": "boolean"
          },
          "sensitive": {
            "type": "boolean"
          },
          "min": {
            "type": "number"
          },
          "max": {
            "type": "number"
          }
        },
        "required": [
          "type",
          "title",
          "description"
        ],
        "additionalProperties": false
      }
    },
    "_meta": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "additionalProperties": {}
      }
    }
  },
  "required": [
    "name",
    "version",
    "description",
    "author",
    "server"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
