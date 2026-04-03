---
id: github.com-levz0r-markdown-printer-44972055-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:21.186725
---

# KNOWLEDGE EXTRACT: github.com_levz0r_markdown-printer_44972055
> **Extracted on:** 2026-04-01 13:19:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522354/github.com_levz0r_markdown-printer_44972055

---

## File: `.gitignore`
```
node_modules/
*.log
.DS_Store
dist/
*.zip
coverage/
.env
```

## File: `.prettierignore`
```
node_modules/
dist/
pnpm-lock.yaml
*.zip
.DS_Store
extension-*/turndown.js
```

## File: `.prettierrc`
```
{
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5",
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}
```

## File: `CLAUDE.md`
```markdown
# Claude Code Reminders

## Pre-Commit Checklist

**ALWAYS run before committing:**

1. **Format files**: `pnpm run format`
2. **Run tests**: `pnpm run test`
3. **Check linting**: `pnpm run lint`

## Git Workflow

- Always format before committing
- Ensure all tests pass
- Verify no linting errors

## Common Commands

```bash
# Format all files
pnpm run format

# Run tests
pnpm run test

# Run linter
pnpm run lint

# Build extensions
pnpm run build
```
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Lev Gelfenbuim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `PRIVACY.md`
```markdown
# Privacy Policy for Markdown Printer

**Last Updated:** October 1, 2025

## Overview

Markdown Printer ("the Extension") is committed to protecting your privacy. This privacy policy explains how the Extension handles user data.

## Data Collection

**The Extension does not collect, store, transmit, or share any user data.**

All operations are performed locally in your web browser. No personal information, browsing history, or saved files are sent to any external servers.

## How the Extension Works

1. **Page Content Access**: When you click "Save as Markdown," the Extension accesses the current page's content solely for the purpose of converting it to Markdown format.

2. **Local Processing**: All HTML-to-Markdown conversion happens locally in your browser using the Turndown.js library.

3. **File Saving**: The converted Markdown file is saved to your computer using Chrome's built-in downloads functionality. The Extension does not retain copies of your files.

## Permissions Used

The Extension requests the following permissions:

- **activeTab**: To access the current page content for conversion when you use the extension
- **downloads**: To save the converted Markdown file to your computer
- **scripting**: To inject the conversion library into web pages
- **contextMenus**: To provide a right-click menu option

These permissions are used solely for the Extension's core functionality and not for data collection.

## Third-Party Services

The Extension does not use any third-party analytics, tracking, or advertising services.

## Changes to This Policy

If we make changes to this privacy policy, we will update the "Last Updated" date at the top of this page.

## Contact

If you have questions about this privacy policy, please contact:

- Email: lev@lev.engineer
- GitHub: https://github.com/levz0r/markdown-printer

## Open Source

Markdown Printer is open source software. You can review the complete source code at:
https://github.com/levz0r/markdown-printer
```

## File: `PUBLISHING.md`
```markdown
# Publishing Guide

This guide explains how to automatically publish Markdown Printer to Chrome Web Store, Firefox Add-ons, and Edge Add-ons using GitHub Actions.

## How It Works

The workflow (`publish.yml`) automatically:

1. Checks the current published version on each store
2. Compares it with your local manifest version
3. **Only publishes to stores where the version is outdated**
4. Skips stores that are already up-to-date

This prevents unnecessary submissions and review delays!

## Setup

### 1. Install publish-browser-extension

```bash
pnpm add -D publish-browser-extension
```

### 2. Configure GitHub Secrets

Add these secrets to your repository at `Settings > Secrets and variables > Actions > Repository secrets`:

#### Chrome Web Store

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the Chrome Web Store API
3. Create OAuth 2.0 credentials
4. Follow [this guide](https://developer.chrome.com/docs/webstore/using-api) to get:
   - `CHROME_CLIENT_ID`
   - `CHROME_CLIENT_SECRET`
   - `CHROME_REFRESH_TOKEN`

#### Firefox Add-ons

1. Log in to [addons.mozilla.org](https://addons.mozilla.org/)
2. Go to **Tools > Manage API Keys**
3. Generate credentials:
   - `FIREFOX_ISSUER`
   - `FIREFOX_SECRET`

#### Microsoft Edge Add-ons

1. Sign in to [Partner Center](https://partner.microsoft.com/)
2. Visit the [Publish API page](https://partner.microsoft.com/en-us/dashboard/microsoftedge/publishapi)
3. Click **Create API credentials**:
   - `EDGE_PRODUCT_ID` (from your extension overview page)
   - `EDGE_CLIENT_ID`
   - `EDGE_API_KEY`

## Usage

### Option 1: Manual Trigger

1. Go to `Actions` tab in GitHub
2. Select `Publish Extensions` workflow
3. Click `Run workflow`

The workflow will check all stores and only publish where needed.

### Option 2: Automatic on Tag

Create and push a version tag:

```bash
git tag v1.0.4
git push origin v1.0.4
```

The workflow will automatically run and publish to outdated stores.

## Version Management

### Update versions across all manifests

```bash
# Update version in package.json
npm version patch  # or minor, or major

# Manually update the version in:
# - extension-chrome/manifest.json
# - extension-firefox/manifest.json

# Build and commit
pnpm run build
git add .
git commit -m "Bump version to 1.0.4"
git tag v1.0.4
git push origin main --tags
```

## Workflow Output

The workflow provides a summary showing which stores were published to:

```
Publication Summary
- Chrome: ✓ Published
- Firefox: ⊘ Skipped (up to date)
- Edge: ⊘ Skipped (up to date)
```

## Important Notes

### Auto-Submit Behavior

The workflow is configured with `--skip-submit-review` for Chrome and Edge. This means:

- **Uploads are automatic**: New versions are uploaded to the stores
- **Review submission is manual**: You must manually submit for review in each store's dashboard

This prevents errors when a version is already pending review (stores reject new submissions during review).

**To publish a new version:**

1. Run the workflow (uploads to stores)
2. Visit each store's dashboard:
   - [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole)
   - [Edge Partner Center](https://partner.microsoft.com/en-us/dashboard/microsoftedge/overview)
3. Click "Submit for review" manually

**Firefox** automatically submits for review (cannot be skipped).

## Troubleshooting

### Chrome: "Invalid refresh token"

Wait an hour after setting up the Chrome Web Store API before generating the refresh token.

### Chrome/Edge: "Item already in review"

This shouldn't happen with `--skip-submit-review` enabled. If you see this error, a version is currently under review. Wait for review completion before uploading a new version.

### Firefox: "Submission failed"

Ensure you've zipped the source code correctly and that your extension follows AMO guidelines.

### Edge: "Authentication failed"

Verify your Product ID is correct by checking your extension's overview page in Partner Center.

### Version check fails

If the version check step fails, the workflow will still attempt to publish (using `continue-on-error: true`). Check the logs for details.

## Manual Publishing

If you prefer to publish manually, you can use the CLI directly:

```bash
# Publish to specific stores
npx publish-browser-extension \
  --chrome-zip dist/chrome.zip \
  --chrome-extension-id pfplfifdaaaalkefgnknfgoiabegcbmf \
  --chrome-client-id "$CHROME_CLIENT_ID" \
  --chrome-client-secret "$CHROME_CLIENT_SECRET" \
  --chrome-refresh-token "$CHROME_REFRESH_TOKEN"
```

## Notes

- First-time submissions must be done manually through each store's dashboard
- The workflow assumes you're using the same version for Chrome and Edge (both use extension-chrome)
- Source code is automatically zipped for Firefox submissions
- All submissions go through each store's review process before being published
```

## File: `README.md`
```markdown
# Markdown Printer

Save web pages as Markdown files with preserved formatting. **Zero setup required** - just install and start saving!

Perfect for documentation, articles, and note-taking.

[![Chrome Web Store Version](https://img.shields.io/chrome-web-store/v/pfplfifdaaaalkefgnknfgoiabegcbmf?logo=googlechrome&logoColor=white&label=Chrome&style=for-the-badge)](https://chromewebstore.google.com/detail/markdown-printer/pfplfifdaaaalkefgnknfgoiabegcbmf)
[![Mozilla Add-on Version](https://img.shields.io/amo/v/markdown-printer?logo=firefox&logoColor=white&label=Firefox&style=for-the-badge)](https://addons.mozilla.org/en-US/firefox/addon/markdown-printer/)

## ✨ Features

- 🚀 **No setup required** - works immediately after installation
- 📝 Preserves formatting (headers, links, code blocks, lists, tables)
- 💾 Save anywhere with familiar "Save As" dialog
- ⚡ Fast client-side conversion using Turndown.js
- 🎯 Right-click menu + extension popup
- 📊 Adds metadata (source URL, save date) to saved files

## 🎯 Installation

### Chrome

**[Install from Chrome Web Store](https://chromewebstore.google.com/detail/markdown-printer/pfplfifdaaaalkefgnknfgoiabegcbmf)** ⭐

### Edge

**[Install from Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/mlmakmhfnkbabnhhcnekleemamhpnmgk)** ⭐

### Firefox

**[Install from Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/markdown-printer/)** ⭐

### Manual Installation (For Development)

#### Chrome/Edge:

1. Clone or download this repository
2. Open Chrome/Edge and navigate to `chrome://extensions/` or `edge://extensions/`
3. Enable "Developer mode" in the top right
4. Click "Load unpacked"
5. Select the `extension-chrome/` directory
6. Done! 🎉

#### Firefox:

1. Clone or download this repository
2. Open Firefox and navigate to `about:debugging`
3. Click "This Firefox" in the left sidebar
4. Click "Load Temporary Add-on"
5. Navigate to the `extension-firefox/` directory and select `manifest.json`
6. Done! 🎉

## 📖 Usage

### Method 1: Right-Click Menu

1. Navigate to any webpage
2. Right-click anywhere on the page
3. Select "Save as Markdown"
4. Choose where to save in the dialog

### Method 2: Extension Icon

1. Navigate to any webpage
2. Click the Markdown Printer icon in the toolbar
3. Click "Save Page as Markdown"
4. Choose where to save in the dialog

## 📂 Output Format

Files are saved with the format: `Page-Title-YYYY-MM-DD.md`

Example:

```markdown
# Getting Started Guide

**Source:** https://example.com/docs/getting-started
**Saved:** 2025-10-01T12:00:00.000Z

_Generated with [markdown-printer](https://github.com/levz0r/markdown-printer) (v1.1.0) by [Lev Gelfenbuim](https://lev.engineer)_

---

[Your page content in Markdown format]
```

## 🔧 Pro Version

Need advanced features? Check out the **Pro Version** in the `extension-pro/` folder:

- ✅ Custom save location (no dialog every time)
- ✅ Auto-open files in your editor after saving
- ✅ Folder browser to pick save location
- ✅ Persistent settings

**Trade-off:** Requires additional setup (native messaging host installation)

See [Pro Version README](../../../README.md) for installation instructions.

## 🆚 Comparison

| Feature          | Standard                                                                                                   | Pro                   |
| ---------------- | ---------------------------------------------------------------------------------------------------------- | --------------------- |
| Installation     | One-click                                                                                                  | Requires setup script |
| Browser Support  | Chrome, Edge, Firefox                                                                                      | Chrome, Edge, Firefox |
| Save location    | Choose each time                                                                                           | Configurable default  |
| Auto-open files  | ❌                                                                                                         | ✅                    |
| Settings         | ❌                                                                                                         | ✅                    |
| Chrome Web Store | ✅ [Available](https://chromewebstore.google.com/detail/markdown-printer/pfplfifdaaaalkefgnknfgoiabegcbmf) | ❌ Can't publish      |
| Edge Add-ons     | ✅ [Available](https://microsoftedge.microsoft.com/addons/detail/mlmakmhfnkbabnhhcnekleemamhpnmgk)         | ❌ Can't publish      |
| Firefox Add-ons  | ✅ [Available](https://addons.mozilla.org/en-US/firefox/addon/markdown-printer/)                           | ❌ Can't publish      |

## 🛠️ Technical Details

- **Extension Type:** Manifest V3
- **Conversion:** Turndown.js (client-side)
- **Permissions:** activeTab, downloads, scripting, contextMenus
- **File Format:** Markdown (.md)
- **Browser Support:** Chrome, Edge, Firefox (121+)
- **Cross-browser:** Separate builds for Chrome and Firefox due to Manifest V3 differences

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit pull requests.

### Development

The extension uses a shared codebase for Chrome and Firefox:

```
src/
  background.js          # Source of truth - edit this file
extension-chrome/
  background.js          # Copied from src/ during build
extension-firefox/
  background.js          # Copied from src/ during build
```

**Workflow:**

1. Edit `src/background.js`
2. Run `pnpm run build` to copy to both extensions
3. Load unpacked extension from `extension-chrome/` or `extension-firefox/`
4. Run `pnpm run format && pnpm run test && pnpm run lint` before committing

## 🔗 Links

- [Chrome Web Store](https://chromewebstore.google.com/detail/markdown-printer/pfplfifdaaaalkefgnknfgoiabegcbmf) - Install for Chrome
- [Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/mlmakmhfnkbabnhhcnekleemamhpnmgk) - Install for Edge
- [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/markdown-printer/) - Install for Firefox
- [GitHub Repository](https://github.com/levz0r/markdown-printer)
- [Report Issues](https://github.com/levz0r/markdown-printer/issues)

---

**Made with ❤️ by Lev Gelfenbuim**
```

## File: `SOURCE_BUILD.md`
```markdown
# Build Instructions for Markdown Printer (Firefox)

This document provides step-by-step instructions to build the Firefox version of Markdown Printer from source.

## Requirements

- **Operating System**: macOS, Linux, or Windows
- **Node.js**: v18 or higher
- **npm**: v9 or higher (comes with Node.js)
- **zip utility**: Built into macOS/Linux, available on Windows via PowerShell

## Third-Party Libraries

This extension uses the following open-source library:

- **Turndown.js v7.2.0** - HTML to Markdown converter
  - License: MIT
  - Source: https://github.com/mixmark-io/turndown
  - Downloaded from: https://cdn.jsdelivr.net/npm/turndown@7.2.0/dist/turndown.js

## Build Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/levz0r/markdown-printer.git
   cd markdown-printer
   ```

2. **Run the build script**

   ```bash
   npm run build:firefox
   ```

   This command will:
   - Read the version from `package.json`
   - Generate the Firefox manifest with proper browser-specific settings
   - Copy all source files to `extension-firefox/` directory
   - Create a zip package in `dist/markdown-printer-firefox-v{version}.zip`

3. **Verify the build**

   The output package will be located at:

   ```
   dist/markdown-printer-firefox-v{version}.zip
   ```

   This zip file contains:
   - `manifest.json` - Firefox-specific manifest (generated from build.js)
   - `background.js` - Background script (source file, not minified)
   - `popup.html` - Extension popup UI
   - `popup.js` - Popup script (source file, not minified)
   - `turndown.js` - Third-party library (see above)
   - Icon files (16px, 48px, 128px)

## Source File Locations

All source files are in the repository root and `extension-firefox/` directory:

- `/build.js` - Build automation script
- `/package.json` - Version and build configuration
- `/extension-firefox/background.js` - Main extension logic
- `/extension-firefox/popup.html` - Popup UI
- `/extension-firefox/popup.js` - Popup script
- `/extension-firefox/turndown.js` - Third-party library (Turndown.js v7.2.0)
- `/extension-firefox/icon*.png` - Extension icons

## Notes

- No transpilation, minification, or obfuscation is used for any source files
- The only "build" step is copying files and generating the manifest.json with version information
- `turndown.js` is included as-is from the official CDN (see Third-Party Libraries section)
```

## File: `build.js`
```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Read version from package.json
const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
const version = packageJson.version;

console.log(`Building Markdown Printer v${version}...`);

// Determine which builds to create
const args = process.argv.slice(2);
const buildChrome = args.length === 0 || args.includes('chrome');
const buildFirefox = args.length === 0 || args.includes('firefox');

// Shared source files (copied from src/ to both extensions)
const sharedSourceFiles = ['background.js'];

// Common directories to copy
const commonDirs = ['_locales'];

// Manifest templates
const chromeManifest = {
  manifest_version: 3,
  name: '__MSG_extensionName__',
  version: version,
  description: '__MSG_extensionDescription__',
  default_locale: 'en',
  author: 'Lev Gelfenbuim',
  homepage_url: 'https://github.com/levz0r/markdown-printer',
  permissions: ['activeTab', 'contextMenus', 'downloads', 'scripting'],
  background: {
    service_worker: 'background.js',
  },
  icons: {
    16: 'icon16.png',
    48: 'icon48.png',
    128: 'icon128.png',
  },
  action: {
    default_popup: 'popup.html',
    default_icon: {
      16: 'icon16.png',
      48: 'icon48.png',
      128: 'icon128.png',
    },
  },
};

const firefoxManifest = {
  ...chromeManifest,
  browser_specific_settings: {
    gecko: {
      id: 'markdown-printer@lev.engineer',
      strict_min_version: '121.0',
      data_collection_permissions: {
        required: ['none'],
      },
    },
  },
  background: {
    scripts: ['background.js'],
  },
};

// Function to ensure directory exists
function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

// Function to copy files
function copyFiles(sourceDir, destDir, files) {
  files.forEach(file => {
    const sourcePath = path.join(sourceDir, file);
    const destPath = path.join(destDir, file);

    if (fs.existsSync(sourcePath)) {
      fs.copyFileSync(sourcePath, destPath);
      console.log(`  ✓ Copied ${file}`);
    } else {
      console.warn(`  ⚠ Warning: ${file} not found in ${sourceDir}`);
    }
  });
}

// Function to copy directories recursively
function copyDir(src, dest) {
  if (!fs.existsSync(src)) {
    console.warn(`  ⚠ Warning: Directory ${src} not found`);
    return;
  }

  ensureDir(dest);

  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }

  console.log(`  ✓ Copied directory ${path.basename(src)}/`);
}

// Function to create zip package
function createZip(sourceDir, outputName) {
  try {
    const command = `cd ${sourceDir} && zip -r ../${outputName} . -x "*.DS_Store"`;
    execSync(command, { stdio: 'inherit' });
    console.log(`  ✓ Created ${outputName}`);
  } catch (error) {
    console.error(`  ✗ Failed to create ${outputName}:`, error.message);
  }
}

// Build Chrome version
if (buildChrome) {
  console.log('\n📦 Building Chrome version...');
  const chromeDir = 'extension-chrome';
  ensureDir(chromeDir);

  // Copy shared source files from src/
  copyFiles('src', chromeDir, sharedSourceFiles);

  // Copy common directories (like _locales)
  commonDirs.forEach(dir => {
    copyDir(dir, path.join(chromeDir, dir));
  });

  // Write manifest
  fs.writeFileSync(path.join(chromeDir, 'manifest.json'), JSON.stringify(chromeManifest, null, 2));
  console.log('  ✓ Updated manifest.json');

  // Create dist directory
  ensureDir('dist');

  // Create zip package
  createZip(chromeDir, `dist/markdown-printer-chrome-v${version}.zip`);
}

// Build Firefox version
if (buildFirefox) {
  console.log('\n🦊 Building Firefox version...');
  const firefoxDir = 'extension-firefox';
  ensureDir(firefoxDir);

  // Copy shared source files from src/
  copyFiles('src', firefoxDir, sharedSourceFiles);

  // Copy common directories (like _locales)
  commonDirs.forEach(dir => {
    copyDir(dir, path.join(firefoxDir, dir));
  });

  // Write manifest
  fs.writeFileSync(
    path.join(firefoxDir, 'manifest.json'),
    JSON.stringify(firefoxManifest, null, 2)
  );
  console.log('  ✓ Updated manifest.json');

  // Create dist directory
  ensureDir('dist');

  // Create zip package
  createZip(firefoxDir, `dist/markdown-printer-firefox-v${version}.zip`);
}

console.log('\n✅ Build complete!\n');
console.log('📦 Packages created in dist/ directory');
console.log(`   Version: ${version}`);
if (buildChrome) {
  console.log(`   - markdown-printer-chrome-v${version}.zip`);
}
if (buildFirefox) {
  console.log(`   - markdown-printer-firefox-v${version}.zip`);
}
console.log('\nTo bump version and rebuild:');
console.log('  npm run version:patch   # 1.0.0 -> 1.0.1');
console.log('  npm run version:minor   # 1.0.0 -> 1.1.0');
console.log('  npm run version:major   # 1.0.0 -> 2.0.0');
```

## File: `description-fr.md`
```markdown
# Markdown Printer - Français

Markdown Printer vous permet de sauvegarder n'importe quelle page web en tant que fichier Markdown en un seul clic. Parfait pour le développement IA, la documentation et la prise de notes.

## ✨ FONCTIONNALITÉS

• Aucune configuration requise - fonctionne immédiatement après l'installation
• Préserve le formatage (titres, liens, blocs de code, listes, tableaux)
• Enregistrez n'importe où avec la boîte de dialogue familière "Enregistrer sous"
• Conversion rapide côté client
• Menu contextuel clic droit + popup dans la barre d'outils
• Ajoute des métadonnées (URL source, date d'enregistrement)
• Sortie propre - supprime les scripts, styles et éléments indésirables

## 🎯 COMMENT ÇA MARCHE

1. Accédez à n'importe quelle page web
2. Faites un clic droit et sélectionnez "Enregistrer en Markdown" OU cliquez sur l'icône de l'extension
3. Choisissez où enregistrer dans la boîte de dialogue
4. C'est fait ! Votre page est maintenant un fichier .md

## 📝 PARFAIT POUR

• Développement IA/LLM - Alimentez Claude, ChatGPT ou Cursor avec une efficacité de tokens 2-3x meilleure que HTML
• Codage rapide - Sauvegardez rapidement les docs API, tutoriels et références pour votre assistant de codage IA
• Construction de bases de connaissances - Archivez les docs techniques dans un format optimisé pour le contexte IA
• Revue de code - Sauvegardez les PRs et discussions de code dans un format facilement analysable par les LLMs
• Développeurs sauvegardant la documentation
• Chercheurs archivant des articles
• Étudiants prenant des notes
• Créateurs de contenu sauvegardant des posts
• Tous les amateurs de Markdown !

## 🤖 POURQUOI MARKDOWN POUR L'IA ?

Markdown est le format optimal pour alimenter les outils IA en contexte :
• 2-3x plus de contenu dans les limites de tokens par rapport à HTML
• Format propre et structuré que les LLMs comprennent parfaitement
• Préserve les blocs de code, titres et liens sans le bruit HTML
• Fonctionne parfaitement avec Cursor, Continue et autres outils de codage IA

## 🔒 CONFIDENTIALITÉ

Cette extension ne collecte, ne transmet ni ne partage aucune donnée utilisateur. Toute la conversion se fait localement dans votre navigateur. Aucune donnée ne quitte votre ordinateur.

## 🆓 GRATUIT ET OPEN SOURCE

Voir le code source sur GitHub : https://github.com/levz0r/markdown-printer

## ⭐ SUPPORT

Trouvé un bug ou une suggestion ? Signalez-le sur GitHub ou envoyez un email à hi@lev.engineer

---

## Historique des versions

### v1.1.0 (2025-10-10)

• Ajout de la prise en charge de l'internationalisation pour l'hébreu, l'hindi et le français
• Ajout de la prise en charge des langues RTL (droite à gauche) pour l'hébreu et autres langues RTL
• Ajout de l'affichage du numéro de version dans la popup
• Amélioration du système de build pour inclure les fichiers de localisation

### v1.0.3 (2025-10-06)

• Correction de l'extraction de contenu pour fonctionner de manière fiable sur toutes les mises en page de site
• Amélioration de la capture des sites de documentation complexes (Microsoft Learn, etc.)
• Simplification de la sélection de contenu pour une meilleure compatibilité

### v1.0.2 (2025-10-06)

• Ajout de la capture de page complète avec défilement automatique
• Charge automatiquement le contenu lazy-loaded avant la conversion
• Fait défiler toute la page pour déclencher le contenu dynamique
• Performance de défilement 3x plus rapide

### v1.0.1 (2025-10-05)

• Ajout de la prise en charge de Firefox avec compatibilité multi-navigateurs
• Amélioration de la sortie Markdown en supprimant les éléments indésirables (scripts, styles, iframes, SVGs)
• Ajout d'un système de build automatisé avec gestion des versions
• Meilleure gestion des erreurs pour les pages protégées

### v1.0.0 (2025-10-01)

• Version initiale
• Conversion Markdown en un clic
• Prise en charge du menu contextuel clic droit
• Interface popup dans la barre d'outils
• Insertion de métadonnées (URL source, date de sauvegarde)
• Intégration de la boîte de dialogue Enregistrer sous
```

## File: `description-he.md`
```markdown
# Markdown Printer - עברית

Markdown Printer מאפשר לך לשמור כל דף אינטרנט כקובץ Markdown בלחיצה אחת. מושלם לפיתוח AI, תיעוד ורישום הערות.

## ✨ תכונות

• אין צורך בהתקנה - עובד מיד לאחר ההתקנה
• שומר על עיצוב (כותרות, קישורים, בלוקי קוד, רשימות, טבלאות)
• שמירה בכל מקום עם דיאלוג "שמור בשם" מוכר
• המרה מהירה בצד הלקוח
• תפריט קליק ימני + חלון קופץ בסרגל הכלים
• הוספת מטא-דאטה (כתובת URL מקורית, תאריך שמירה)
• פלט נקי - מסיר סקריפטים, סגנונות ואלמנטים לא רצויים

## 🎯 איך זה עובד

1. נווט לכל דף אינטרנט
2. לחץ קליק ימני ובחר "שמור כ-Markdown" או לחץ על אייקון ההרחבה
3. בחר היכן לשמור בדיאלוג
4. זהו! הדף שלך עכשיו קובץ .md

## 📝 מושלם עבור

• פיתוח AI/LLM - העבר תיעוד ל-Claude, ChatGPT או Cursor עם יעילות טוקנים טובה פי 2-3 מ-HTML
• קידוד חכם - שמור מהר מסמכי API, מדריכים והפניות לעוזר הקידוד AI שלך
• בניית מאגרי ידע - ארכב מסמכים טכניים בפורמט מותאם להקשר AI
• סקירת קוד - שמור PRs ודיונים על קוד בפורמט שמודלי שפה יכולים לנתח בקלות
• מפתחים שומרים תיעוד
• חוקרים מארכבים מאמרים
• סטודנטים רושמים הערות
• יוצרי תוכן מגבים פוסטים
• כל מי שאוהב Markdown!

## 🤖 למה Markdown ל-AI?

Markdown הוא הפורמט האופטימלי להזנת הקשר לכלי AI:
• פי 2-3 יותר תוכן בתוך מגבלות טוקנים לעומת HTML
• פורמט נקי ומובנה שמודלי שפה מבינים בצורה מושלמת
• שומר בלוקי קוד, כותרות וקישורים ללא רעש HTML
• עובד בצורה חלקה עם Cursor, Continue וכלי קידוד AI אחרים

## 🔒 פרטיות

הרחבה זו לא אוספת, משדרת או משתפת כל נתוני משתמש. כל ההמרה מתרחשת מקומית בדפדפן שלך. שום מידע לא עוזב את המחשב שלך.

## 🆓 חינמי וקוד פתוח

צפה בקוד המקור ב-GitHub: https://github.com/levz0r/markdown-printer

## ⭐ תמיכה

מצאת באג או יש לך הצעה? דווח על זה ב-GitHub או שלח מייל ל-hi@lev.engineer

---

## היסטוריית גרסאות

### v1.1.0 (2025-10-10)

• נוספה תמיכה בינלאומית לעברית, הינדי וצרפתית
• נוספה תמיכה בשפות RTL (מימין לשמאל) לעברית ושפות RTL אחרות
• נוספה הצגת מספר גרסה בחלון קופץ
• שיפור מערכת הבנייה לכלול קבצי לוקליזציה

### v1.0.3 (2025-10-06)

• תוקנה חילוץ תוכן לעבוד בצורה אמינה על כל פריסות האתרים
• שיפור לכידת אתרי תיעוד מורכבים (Microsoft Learn, וכו')
• פישוט בחירת תוכן לתאימות טובה יותר

### v1.0.2 (2025-10-06)

• נוספה לכידת דף מלא עם גלילה אוטומטית
• טעינה אוטומטית של תוכן lazy-loaded לפני המרה
• גלילה דרך כל הדף להפעלת תוכן דינמי
• ביצועי גלילה מהירים פי 3

### v1.0.1 (2025-10-05)

• נוספה תמיכה ב-Firefox עם תאימות בין-דפדפנים
• שיפור פלט Markdown על ידי הסרת אלמנטים לא רצויים (סקריפטים, סגנונות, iframes, SVGs)
• נוספה מערכת בנייה אוטומטית עם ניהול גרסאות
• טיפול משופר בשגיאות עבור דפים מוגנים

### v1.0.0 (2025-10-01)

• שחרור ראשוני
• המרת Markdown בלחיצה אחת
• תמיכה בתפריט הקשר קליק ימני
• ממשק חלון קופץ בסרגל כלים
• הכנסת מטא-דאטה (URL מקור, תאריך שמירה)
• שילוב דיאלוג שמור בשם
```

## File: `description-hi.md`
```markdown
# Markdown Printer - हिन्दी

Markdown Printer आपको किसी भी वेब पेज को सिर्फ एक क्लिक में Markdown फ़ाइल के रूप में सहेजने की सुविधा देता है। AI विकास, डॉक्यूमेंटेशन और नोट लेने के लिए बिल्कुल सही।

## ✨ विशेषताएं

• कोई सेटअप की आवश्यकता नहीं - इंस्टॉल करने के तुरंत बाद काम करता है
• फॉर्मेटिंग को सुरक्षित रखता है (हेडर, लिंक, कोड ब्लॉक, सूचियाँ, टेबल)
• परिचित "इस रूप में सहेजें" डायलॉग के साथ कहीं भी सहेजें
• तेज़ क्लाइंट-साइड रूपांतरण
• राइट-क्लिक कॉन्टेक्स्ट मेनू + टूलबार पॉपअप
• मेटाडेटा जोड़ता है (स्रोत URL, सहेजने की तारीख)
• साफ आउटपुट - स्क्रिप्ट, स्टाइल और अनचाही एलिमेंट हटाता है

## 🎯 यह कैसे काम करता है

1. किसी भी वेबपेज पर जाएं
2. राइट-क्लिक करें और "Markdown के रूप में सहेजें" चुनें या एक्सटेंशन आइकन पर क्लिक करें
3. डायलॉग में कहां सहेजना है चुनें
4. हो गया! आपका पेज अब एक .md फ़ाइल है

## 📝 इसके लिए बिल्कुल सही

• AI/LLM विकास - Claude, ChatGPT या Cursor को डॉक्यूमेंटेशन फीड करें HTML से 2-3x बेहतर टोकन दक्षता के साथ
• वाइब कोडिंग - अपने AI कोडिंग असिस्टेंट के लिए API डॉक्स, ट्यूटोरियल और संदर्भ जल्दी से सहेजें
• नॉलेज बेस बनाना - AI संदर्भ के लिए अनुकूलित प्रारूप में तकनीकी डॉक्स संग्रहीत करें
• कोड समीक्षा - PRs और कोड चर्चाओं को ऐसे प्रारूप में सहेजें जिसे LLMs आसानी से पार्स कर सकें
• डॉक्यूमेंटेशन सहेजने वाले डेवलपर
• लेख संग्रहीत करने वाले शोधकर्ता
• नोट्स लेने वाले छात्र
• पोस्ट बैकअप करने वाले कंटेंट क्रिएटर
• Markdown पसंद करने वाला कोई भी!

## 🤖 AI के लिए Markdown क्यों?

Markdown AI टूल्स को संदर्भ फीड करने के लिए सबसे अच्छा प्रारूप है:
• HTML की तुलना में टोकन सीमा के भीतर 2-3x अधिक सामग्री
• साफ, संरचित प्रारूप जिसे LLMs पूरी तरह से समझते हैं
• HTML शोर के बिना कोड ब्लॉक, हेडर और लिंक को सुरक्षित रखता है
• Cursor, Continue और अन्य AI कोडिंग टूल्स के साथ सहजता से काम करता है

## 🔒 गोपनीयता

यह एक्सटेंशन कोई उपयोगकर्ता डेटा एकत्र, संचारित या साझा नहीं करता है। सभी रूपांतरण आपके ब्राउज़र में स्थानीय रूप से होता है। कोई डेटा आपके कंप्यूटर से नहीं निकलता।

## 🆓 मुफ्त और ओपन सोर्स

GitHub पर स्रोत कोड देखें: https://github.com/levz0r/markdown-printer

## ⭐ समर्थन

कोई बग मिला या सुझाव है? इसे GitHub पर रिपोर्ट करें या hi@lev.engineer पर ईमेल करें

---

## संस्करण इतिहास

### v1.1.0 (2025-10-10)

• हिब्रू, हिंदी और फ्रेंच के लिए अंतर्राष्ट्रीयकरण समर्थन जोड़ा गया
• हिब्रू और अन्य RTL भाषाओं के लिए RTL (दाएं-से-बाएं) भाषा समर्थन जोड़ा गया
• पॉपअप में संस्करण नंबर प्रदर्शन जोड़ा गया
• स्थानीयकरण फ़ाइलों को शामिल करने के लिए बिल्ड सिस्टम में सुधार किया गया

### v1.0.3 (2025-10-06)

• सभी साइट लेआउट पर विश्वसनीय रूप से काम करने के लिए कंटेंट एक्सट्रैक्शन को ठीक किया गया
• जटिल डॉक्यूमेंटेशन साइट्स (Microsoft Learn, आदि) के कैप्चर में सुधार
• बेहतर संगतता के लिए सामग्री चयन को सरल बनाया गया

### v1.0.2 (2025-10-06)

• स्वचालित स्क्रॉलिंग के साथ पूर्ण-पेज कैप्चर जोड़ा गया
• रूपांतरण से पहले lazy-loaded सामग्री को स्वचालित रूप से लोड करता है
• गतिशील सामग्री को ट्रिगर करने के लिए पूरे पेज को स्क्रॉल करता है
• 3x तेज़ स्क्रॉलिंग प्रदर्शन

### v1.0.1 (2025-10-05)

• क्रॉस-ब्राउज़र संगतता के साथ Firefox समर्थन जोड़ा गया
• अवांछित तत्वों (स्क्रिप्ट, स्टाइल, iframes, SVGs) को हटाकर Markdown आउटपुट में सुधार
• संस्करण प्रबंधन के साथ स्वचालित बिल्ड सिस्टम जोड़ा गया
• सुरक्षित पेजों के लिए बेहतर त्रुटि हैंडलिंग

### v1.0.0 (2025-10-01)

• प्रारंभिक रिलीज़
• एक-क्लिक Markdown रूपांतरण
• राइट-क्लिक कॉन्टेक्स्ट मेनू समर्थन
• टूलबार पॉपअप इंटरफ़ेस
• मेटाडेटा सम्मिलन (स्रोत URL, सहेजने की तारीख)
• इस रूप में सहेजें डायलॉग एकीकरण
```

## File: `description.md`
```markdown
Markdown Printer lets you save any web page as a Markdown file with just one click. Perfect for AI development, documentation, and note-taking.

✨ FEATURES
• Zero setup required - works immediately after installation
• Preserves formatting (headers, links, code blocks, lists, tables)
• Save anywhere with familiar "Save As" dialog
• Fast client-side conversion
• Right-click context menu + toolbar popup
• Adds metadata (source URL, save date)
• Clean output - removes scripts, styles, and unwanted elements

🎯 HOW IT WORKS

1. Navigate to any webpage
2. Right-click and select "Save as Markdown" OR click the extension icon
3. Choose where to save in the dialog
4. Done! Your page is now a .md file

📝 PERFECT FOR
• AI/LLM Development - Feed documentation to Claude, ChatGPT, or Cursor with 2-3x better token efficiency than HTML
• Vibe Coding - Quickly save API docs, tutorials, and references for your AI coding assistant
• Building Knowledge Bases - Archive technical docs in a format optimized for AI context
• Code Review - Save PRs and code discussions in a format LLMs can easily parse
• Developers saving documentation
• Researchers archiving articles
• Students taking notes
• Content creators backing up posts
• Anyone who loves Markdown!

🤖 WHY MARKDOWN FOR AI?
Markdown is the optimal format for feeding context to AI tools:
• 2-3x more content within token limits compared to HTML
• Clean, structured format that LLMs understand perfectly
• Preserves code blocks, headers, and links without HTML noise
• Works seamlessly with Cursor, Continue, and other AI coding tools

🔒 PRIVACY
This extension does not collect, transmit, or share any user data. All conversion happens locally in your browser. No data leaves your computer.

🆓 FREE & OPEN SOURCE
View the source code on GitHub: https://github.com/levz0r/markdown-printer

⭐ SUPPORT
Found a bug or have a suggestion? Report it on GitHub or email hi@lev.engineer

---

## Version History

### v1.1.0 (2025-10-10)

• Added internationalization support for Hebrew, Hindi, and French
• Added RTL (right-to-left) language support for Hebrew and other RTL languages
• Added version number display in popup
• Improved build system to include localization files

### v1.0.3 (2025-10-06)

• Fixed content extraction to work reliably across all site layouts
• Improved capture of complex documentation sites (Microsoft Learn, etc.)
• Simplified content selection for better compatibility

### v1.0.2 (2025-10-06)

• Added full-page capture with automatic scrolling
• Automatically loads lazy-loaded content before conversion
• Scrolls through entire page to trigger dynamic content
• 3x faster scrolling performance

### v1.0.1 (2025-10-05)

• Added Firefox support with cross-browser compatibility
• Improved markdown output by removing unwanted elements (scripts, styles, iframes, SVGs)
• Added automated build system with version management
• Better error handling for protected pages

### v1.0.0 (2025-10-01)

• Initial release
• One-click markdown conversion
• Right-click context menu support
• Toolbar popup interface
• Metadata insertion (source URL, save date)
• Save As dialog integration
```

## File: `eslint.config.js`
```javascript
module.exports = [
  {
    ignores: [
      'node_modules/**',
      'dist/**',
      'coverage/**',
      'pnpm-lock.yaml',
      '**/*.zip',
      '**/.DS_Store',
      '**/turndown.js',
      'native-host/**',
      'extension-pro/**',
    ],
  },
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: 'script',
      globals: {
        // Browser globals
        window: 'readonly',
        document: 'readonly',
        console: 'readonly',
        URL: 'readonly',
        Blob: 'readonly',
        FileReader: 'readonly',
        setTimeout: 'readonly',
        clearTimeout: 'readonly',
        Promise: 'readonly',
        // Web Extension APIs
        chrome: 'readonly',
        browser: 'readonly',
        TurndownService: 'readonly',
      },
    },
    rules: {
      'no-unused-vars': ['error', { argsIgnorePattern: '^_', caughtErrorsIgnorePattern: '^_' }],
      'no-console': 'off', // Console is used for debugging in extensions
      'no-undef': 'error',
      'prefer-const': 'error',
      'no-var': 'error',
      eqeqeq: ['error', 'always'],
      curly: ['error', 'all'],
      'brace-style': ['error', '1tbs'],
      semi: ['error', 'always'],
      quotes: ['error', 'single', { avoidEscape: true }],
    },
  },
  {
    files: ['test/**/*.js'],
    languageOptions: {
      globals: {
        // Jest globals
        describe: 'readonly',
        test: 'readonly',
        expect: 'readonly',
        beforeAll: 'readonly',
        afterAll: 'readonly',
        beforeEach: 'readonly',
        afterEach: 'readonly',
        jest: 'readonly',
      },
    },
  },
  {
    files: ['build.js', 'utils.js', 'test/**/*.js', 'eslint.config.js', 'jest.config.js'],
    languageOptions: {
      globals: {
        // Node.js globals
        require: 'readonly',
        module: 'readonly',
        __dirname: 'readonly',
        process: 'readonly',
        exports: 'readonly',
      },
    },
  },
];
```

## File: `install.bat`
```
@echo off
setlocal enabledelayedexpansion

echo Installing Markdown Printer...
echo.

REM Get absolute paths
set SCRIPT_DIR=%~dp0
set NATIVE_HOST_DIR=%SCRIPT_DIR%native-host
set HOST_MANIFEST=%NATIVE_HOST_DIR%\host.json
set HOST_WRAPPER=%NATIVE_HOST_DIR%\host-wrapper.bat

REM Install npm dependencies
echo Installing Node.js dependencies...
cd /d "%NATIVE_HOST_DIR%"
call npm install
if errorlevel 1 (
    echo Error: Failed to install npm dependencies
    exit /b 1
)

REM Create native messaging host manifest for Windows
set MANIFEST_DIR=%LOCALAPPDATA%\Google\Chrome\NativeMessagingHosts
if not exist "%MANIFEST_DIR%" mkdir "%MANIFEST_DIR%"

set FINAL_MANIFEST=%MANIFEST_DIR%\com.markdownprinter.host.json

REM Escape backslashes for JSON
set "HOST_PATH_ESCAPED=%HOST_WRAPPER:\=\\%"

REM Create the manifest file with proper JSON escaping
(
echo {
echo   "name": "com.markdownprinter.host",
echo   "description": "Markdown Printer Native Host",
echo   "path": "%HOST_PATH_ESCAPED%",
echo   "type": "stdio",
echo   "allowed_origins": [
echo     "chrome-extension://EXTENSION_ID_PLACEHOLDER/"
echo   ]
echo }
) > "%FINAL_MANIFEST%"

echo.
echo √ Native host installed successfully
echo.
echo Next steps:
echo 1. Open Chrome and navigate to chrome://extensions/
echo 2. Enable 'Developer mode' in the top right
echo 3. Click 'Load unpacked'
echo 4. Select the directory: %SCRIPT_DIR%extension
echo 5. Note the Extension ID and update it in: %FINAL_MANIFEST%
echo    (Replace EXTENSION_ID_PLACEHOLDER with the actual ID)
echo.
echo After updating the extension ID, you can use Markdown Printer!
echo Right-click on any page and select 'Save as Markdown'
echo Files will be saved to: %USERPROFILE%\MarkdownPrints\
echo.
echo For more information, visit:
echo https://github.com/levz0r/markdown-printer
echo.

endlocal
```

## File: `install.sh`
```bash
#!/bin/bash

set -e

echo "Installing Markdown Printer..."

# Check if running on Windows (Git Bash, WSL, etc.)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
  echo "Error: This script is for macOS and Linux."
  echo "For Windows, please run install.bat instead."
  exit 1
fi

# Get absolute paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NATIVE_HOST_DIR="$SCRIPT_DIR/native-host"
HOST_MANIFEST="$NATIVE_HOST_DIR/host.json"

# Install npm dependencies
echo "Installing Node.js dependencies..."
cd "$NATIVE_HOST_DIR"
npm install

# Make scripts executable
chmod +x host.js
chmod +x host-wrapper.sh

# Get the full path to the wrapper script
HOST_PATH="$NATIVE_HOST_DIR/host-wrapper.sh"

# Create a temporary manifest with the correct path
TEMP_MANIFEST=$(mktemp)
sed "s|HOST_PATH_PLACEHOLDER|$HOST_PATH|g" "$HOST_MANIFEST" > "$TEMP_MANIFEST"

# Determine the native messaging manifest location based on OS
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  MANIFEST_DIR="$HOME/Library/Application Support/Google/Chrome/NativeMessagingHosts"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux
  MANIFEST_DIR="$HOME/.config/google-chrome/NativeMessagingHosts"
else
  echo "Unsupported OS: $OSTYPE"
  exit 1
fi

# Create manifest directory if it doesn't exist
mkdir -p "$MANIFEST_DIR"

# Copy manifest to the correct location
FINAL_MANIFEST="$MANIFEST_DIR/com.markdownprinter.host.json"
cp "$TEMP_MANIFEST" "$FINAL_MANIFEST"
rm "$TEMP_MANIFEST"

echo ""
echo "✓ Native host installed successfully"
echo ""
echo "Next steps:"
echo "1. Open Chrome and navigate to chrome://extensions/"
echo "2. Enable 'Developer mode' in the top right"
echo "3. Click 'Load unpacked'"
echo "4. Select the directory: $SCRIPT_DIR/extension"
echo "5. Note the Extension ID and update it in: $FINAL_MANIFEST"
echo "   (Replace EXTENSION_ID_PLACEHOLDER with the actual ID)"
echo ""
echo "After updating the extension ID, you can use Markdown Printer!"
echo "Right-click on any page and select 'Save as Markdown'"
echo "Files will be saved to: ~/MarkdownPrints/"
echo ""
echo "For more information, visit:"
echo "https://github.com/levz0r/markdown-printer"
echo ""
```

## File: `jest.config.js`
```javascript
module.exports = {
  testEnvironment: 'node',
  testMatch: ['**/test/**/*.test.js'],
  coverageDirectory: 'coverage',
  collectCoverageFrom: ['utils.js', '!**/node_modules/**', '!**/dist/**', '!**/test/**'],
  coverageThreshold: {
    global: {
      statements: 80,
      branches: 70,
      functions: 80,
      lines: 80,
    },
  },
  verbose: true,
};
```

## File: `package.json`
```json
{
  "name": "markdown-printer",
  "version": "1.1.1",
  "description": "Save web pages as Markdown files with preserved formatting",
  "scripts": {
    "build": "node build.js",
    "build:chrome": "node build.js chrome",
    "build:firefox": "node build.js firefox",
    "version:patch": "npm version patch && npm run build",
    "version:minor": "npm version minor && npm run build",
    "version:major": "npm version major && npm run build",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check ."
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/levz0r/markdown-printer.git"
  },
  "author": "Lev Gelfenbuim",
  "license": "MIT",
  "devDependencies": {
    "@types/jest": "^30.0.0",
    "eslint": "^9.37.0",
    "jest": "^30.2.0",
    "prettier": "^3.6.2",
    "publish-browser-extension": "^4.0.0"
  }
}
```

## File: `renovate.json`
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "baseBranches": ["develop"],
  "packageRules": [
    {
      "groupName": "non-major dependencies",
      "matchUpdateTypes": ["minor", "patch", "digest", "pin"],
      "automerge": false
    },
    {
      "groupName": "major dependencies",
      "matchUpdateTypes": ["major"],
      "automerge": false
    }
  ],
  "schedule": ["before 3am on Monday"],
  "labels": ["dependencies"],
  "dependencyDashboard": true
}
```

## File: `utils.js`
```javascript
/**
 * Utility functions for Markdown Printer extension
 */

/**
 * Sanitizes a filename by removing invalid characters and limiting length
 * @param {string} filename - The filename to sanitize
 * @returns {string} - The sanitized filename
 */
function sanitizeFilename(filename) {
  return filename
    .replace(/[<>:"/\\|?*]/g, '-')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .substring(0, 200);
}

// Export for CommonJS (Node.js/Jest)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { sanitizeFilename };
}
```

## File: `_locales/en/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "Save web pages as Markdown files to your Downloads folder. No setup required!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "Save Page as Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Save as Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `_locales/fr/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "Enregistrez des pages web en tant que fichiers Markdown dans votre dossier Téléchargements. Aucune configuration requise !",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "Enregistrer la page en Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Enregistrer en Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `_locales/he/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "שמור דפי אינטרנט כקבצי Markdown לתיקיית ההורדות. ללא הגדרות נדרשות!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "שמור דף כ-Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "שמור כ-Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `_locales/hi/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "वेब पेजों को Markdown फ़ाइलों के रूप में अपने डाउनलोड फ़ोल्डर में सहेजें। किसी सेटअप की आवश्यकता नहीं!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "पेज को Markdown के रूप में सहेजें",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Markdown के रूप में सहेजें",
    "description": "Context menu item title"
  }
}
```

## File: `extension-chrome/background.js`
```javascript
// Cross-browser compatibility
const browserAPI = typeof browser !== 'undefined' ? browser : chrome;

// Create context menu on installation
browserAPI.runtime.onInstalled.addListener(() => {
  browserAPI.contextMenus.create({
    id: 'saveAsMarkdown',
    title: browserAPI.i18n.getMessage('contextMenuTitle'),
    contexts: ['page'],
  });
});

// Handle context menu click
browserAPI.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === 'saveAsMarkdown') {
    savePageAsMarkdown(tab.id);
  }
});

// Handle messages from popup
browserAPI.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'saveAsMarkdown') {
    browserAPI.tabs.query({ active: true, currentWindow: true }, async tabs => {
      if (tabs[0]) {
        try {
          await savePageAsMarkdown(tabs[0].id);
          sendResponse({ success: true });
        } catch (error) {
          sendResponse({ success: false, error: error.message });
        }
      }
    });
    return true; // Keep the message channel open for async response
  }
});

async function savePageAsMarkdown(tabId) {
  try {
    // Inject Turndown library and conversion script
    await browserAPI.scripting
      .executeScript({
        target: { tabId: tabId },
        files: ['turndown.js'],
      })
      .catch(error => {
        // Better error message for protected pages
        if (
          error.message.includes('cannot be scripted') ||
          error.message.includes('Cannot access') ||
          error.message.includes('extensions gallery')
        ) {
          throw new Error(
            'Cannot save this page - extensions are blocked on browser internal pages and extension stores'
          );
        }
        throw error;
      });

    // Inject script to convert and get markdown
    const results = await browserAPI.scripting.executeScript({
      target: { tabId: tabId },
      func: extractAndConvertToMarkdown,
    });

    if (!results || !results[0]) {
      throw new Error('Failed to extract page content');
    }

    const result = results[0].result;

    // If operation was cancelled, exit without showing save dialog
    if (!result || result === null) {
      return;
    }

    const { markdown, title, url } = result;

    // Generate filename
    const timestamp = new Date().toISOString().split('T')[0];
    const sanitizedTitle = sanitizeFilename(title || 'untitled');
    const filename = `${sanitizedTitle}-${timestamp}.md`;

    // Get extension version
    const version = browserAPI.runtime.getManifest().version;

    // Add metadata header with attribution
    const content = `# ${title}\n\n**Source:** ${url}\n**Saved:** ${new Date().toISOString()}\n\n*Generated with [markdown-printer](https://github.com/levz0r/markdown-printer) (v${version}) by [Lev Gelfenbuim](https://lev.engineer)*\n\n---\n\n${markdown}`;

    // For Firefox, we need to use a different approach
    // Check if we're in Firefox by checking for browser.downloads
    const isFirefox = typeof browser !== 'undefined' && browser.downloads;

    if (isFirefox) {
      // Firefox: Use blob URL approach with special handling
      // Create a temporary object URL in a way that works in Firefox background scripts
      // We'll inject a helper script into the page to create the blob URL
      await browserAPI.scripting.executeScript({
        target: { tabId: tabId },
        func: (content, filename) => {
          const blob = new Blob([content], { type: 'text/plain' });
          const url = URL.createObjectURL(blob);
          // Trigger download from page context
          const a = document.createElement('a');
          a.href = url;
          a.download = filename;
          a.click();
          URL.revokeObjectURL(url);
          return true;
        },
        args: [content, filename],
      });
    } else {
      // Chrome: Use data URL
      const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
      const reader = new FileReader();

      const dataUrl = await new Promise((resolve, reject) => {
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(blob);
      });

      await browserAPI.downloads.download({
        url: dataUrl,
        filename: filename,
        saveAs: true,
      });
    }
  } catch (error) {
    console.error('Error saving markdown:', error);
    throw error;
  }
}

// This function runs in the page context
async function extractAndConvertToMarkdown() {
  // Normalize HTML content for consistent hashing
  // Removes attributes, IDs, classes, and normalizes whitespace
  function normalizeContent(element) {
    const clone = element.cloneNode(true);

    // Remove all unwanted elements
    const unwantedSelectors = [
      'script',
      'style',
      'noscript',
      'iframe',
      'svg',
      'nav',
      'header',
      'footer',
      '.sidebar',
      '.navigation',
      '.menu',
      '[class*="sidebar"]',
      '[class*="navigation"]',
      'button',
      'input',
      'select',
      'textarea',
    ];

    unwantedSelectors.forEach(selector => {
      const elements = clone.querySelectorAll(selector);
      elements.forEach(el => el.remove());
    });

    // Get text content and normalize whitespace
    const text = clone.textContent || '';
    return text.replace(/\s+/g, ' ').trim();
  }

  // Function to check if element is in viewport
  function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    const windowWidth = window.innerWidth || document.documentElement.clientWidth;

    // Element is in viewport if any part of it is visible
    return rect.top < windowHeight && rect.bottom > 0 && rect.left < windowWidth && rect.right > 0;
  }

  // Calculate Jaccard similarity between two strings
  function calculateSimilarity(str1, str2) {
    // Split into words and filter out very short words
    const words1 = new Set(
      str1
        .toLowerCase()
        .split(/\s+/)
        .filter(w => w.length > 2)
    );
    const words2 = new Set(
      str2
        .toLowerCase()
        .split(/\s+/)
        .filter(w => w.length > 2)
    );

    if (words1.size === 0 && words2.size === 0) {
      return 1;
    }
    if (words1.size === 0 || words2.size === 0) {
      return 0;
    }

    const intersection = new Set([...words1].filter(x => words2.has(x)));
    const union = new Set([...words1, ...words2]);

    return intersection.size / union.size;
  }

  // Function to capture currently visible content blocks
  function captureVisibleContentBlocks() {
    const capturedBlocks = [];

    try {
      // Find content blocks - prioritize semantic elements
      const blockSelectors = [
        'article',
        'section',
        'main > div',
        '[role="main"] > div',
        '.content > div',
        '.documentation-content > div',
        'main > *',
        '[role="main"] > *',
      ];

      const foundBlocks = new Set();

      // Try ALL selectors and combine results (don't stop at first match)
      for (const selector of blockSelectors) {
        const elements = document.querySelectorAll(selector);

        if (elements.length > 0) {
          elements.forEach(element => {
            // Skip if already found this element
            if (foundBlocks.has(element)) {
              return;
            }

            // Only capture if element is in viewport and has substantial content
            if (isInViewport(element)) {
              const text = element.textContent || '';
              if (text.trim().length > 100) {
                foundBlocks.add(element);

                // Clone and convert to markdown
                const cloned = element.cloneNode(true);

                // Remove unwanted elements from clone
                const unwantedSelectors = [
                  'script',
                  'style',
                  'noscript',
                  'iframe',
                  'svg',
                  'nav',
                  'header',
                  'footer',
                  'button:not([role="tab"])',
                  'input',
                  'select',
                  'textarea',
                  '#markdown-printer-overlay',
                ];

                unwantedSelectors.forEach(sel => {
                  const elements = cloned.querySelectorAll(sel);
                  elements.forEach(el => el.remove());
                });

                const tempTurndown = new TurndownService({
                  headingStyle: 'atx',
                  codeBlockStyle: 'fenced',
                  bulletListMarker: '-',
                });
                tempTurndown.remove(['script', 'style', 'noscript', 'iframe', 'svg']);

                const markdown = tempTurndown.turndown(cloned);

                if (markdown && markdown.trim().length > 100) {
                  capturedBlocks.push({
                    markdown: markdown,
                    normalizedContent: normalizeContent(element),
                  });
                }
              }
            }
          });
        }
      }

      // Fallback: If no blocks found, try capturing the entire main content area
      if (capturedBlocks.length === 0) {
        const mainSelectors = ['main', '[role="main"]', 'article', '#content', '.content', 'body'];

        for (const selector of mainSelectors) {
          const mainElement = document.querySelector(selector);
          if (mainElement) {
            const text = mainElement.textContent || '';
            if (text.trim().length > 100) {
              const cloned = mainElement.cloneNode(true);

              // Remove unwanted elements
              const unwantedSelectors = [
                'script',
                'style',
                'noscript',
                'iframe',
                'svg',
                'nav',
                'header',
                'footer',
                'aside',
                '.sidebar',
                '.navigation',
                '.menu',
                'button',
                'input',
                'select',
                'textarea',
                '#markdown-printer-overlay',
              ];

              unwantedSelectors.forEach(sel => {
                const elements = cloned.querySelectorAll(sel);
                elements.forEach(el => el.remove());
              });

              const tempTurndown = new TurndownService({
                headingStyle: 'atx',
                codeBlockStyle: 'fenced',
                bulletListMarker: '-',
              });
              tempTurndown.remove(['script', 'style', 'noscript', 'iframe', 'svg']);

              const markdown = tempTurndown.turndown(cloned);

              if (markdown && markdown.trim().length > 100) {
                capturedBlocks.push({
                  markdown: markdown,
                  normalizedContent: normalizeContent(mainElement),
                });
                break; // Found content, stop trying
              }
            }
          }
        }
      }

      return capturedBlocks;
    } catch (error) {
      console.error('Error capturing content blocks:', error);
      return [];
    }
  }

  // Function to scroll through the entire page to trigger lazy loading
  async function scrollToBottom() {
    // Arrays to store captured content
    const capturedContent = [];
    const capturedHashes = new Set();

    // First, try to expand any collapsed/hidden sections
    const expandCollapsedSections = () => {
      // Find and click on common expandable elements
      const expandableSelectors = [
        'details:not([open])',
        '[aria-expanded="false"]',
        '.collapsed',
        '.expand',
        '.accordion:not(.active)',
        '[data-collapsed="true"]',
        'button[aria-expanded="false"]',
      ];

      let expandedCount = 0;
      expandableSelectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
          try {
            if (el.tagName === 'DETAILS') {
              el.open = true;
            } else if (el.click) {
              el.click();
            }
            expandedCount++;
          } catch (_e) {
            // Ignore errors
          }
        });
      });
      return expandedCount;
    };

    // Try to expand sections before scrolling
    expandCollapsedSections();
    await new Promise(resolve => setTimeout(resolve, 500));

    // Create progress indicator overlay
    const overlay = document.createElement('div');
    overlay.id = 'markdown-printer-overlay';
    overlay.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: rgba(0, 0, 0, 0.9);
      color: white;
      padding: 20px;
      border-radius: 8px;
      z-index: 999999;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
      min-width: 300px;
      opacity: 0;
      transition: opacity 0.3s ease-in-out;
    `;

    const title = document.createElement('div');
    title.textContent = 'Printing...';
    title.style.cssText = 'font-weight: bold; margin-bottom: 10px; font-size: 16px;';

    const percentageText = document.createElement('div');
    percentageText.id = 'percentage-text';
    percentageText.style.cssText =
      'font-size: 24px; font-weight: bold; margin-bottom: 5px; color: #4CAF50;';
    percentageText.textContent = '0%';

    const status = document.createElement('div');
    status.id = 'scroll-status';
    status.style.cssText = 'margin-bottom: 10px; font-size: 14px; opacity: 0.8;';

    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 2px;
      overflow: hidden;
      margin-bottom: 10px;
    `;

    const progressFill = document.createElement('div');
    progressFill.id = 'progress-fill';
    progressFill.style.cssText = `
      height: 100%;
      background: #4CAF50;
      width: 0%;
      transition: width 0.3s ease;
    `;
    progressBar.appendChild(progressFill);

    const cancelButton = document.createElement('button');
    cancelButton.textContent = 'Abort';
    cancelButton.style.cssText = `
      width: 100%;
      padding: 8px;
      background: #f44336;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      font-weight: bold;
      transition: background 0.2s ease;
    `;
    cancelButton.onmouseover = () => (cancelButton.style.background = '#d32f2f');
    cancelButton.onmouseout = () => (cancelButton.style.background = '#f44336');

    overlay.appendChild(title);
    overlay.appendChild(percentageText);
    overlay.appendChild(status);
    overlay.appendChild(progressBar);
    overlay.appendChild(cancelButton);
    document.body.appendChild(overlay);

    // Trigger fade-in animation
    window.requestAnimationFrame(() => {
      overlay.style.opacity = '1';
    });

    let cancelled = false;
    cancelButton.onclick = () => {
      cancelled = true;
      status.textContent = 'Stopping...';
      cancelButton.disabled = true;
      cancelButton.style.opacity = '0.5';
    };

    // Make all hidden content sections visible (common in documentation sites)
    const makeAllContentVisible = () => {
      // Target common documentation content containers
      const contentSelectors = [
        'article',
        'section',
        'main',
        '[role="main"]',
        '[class*="content"]',
        '[class*="documentation"]',
        '[class*="api"]',
        '[class*="endpoint"]',
        '[id*="content"]',
      ];

      contentSelectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
          const style = window.getComputedStyle(el);
          if (style.display === 'none' || style.visibility === 'hidden') {
            el.style.display = 'block';
            el.style.visibility = 'visible';
            el.style.opacity = '1';
          }
          // Also unhide all children
          el.querySelectorAll('*').forEach(child => {
            const childStyle = window.getComputedStyle(child);
            if (childStyle.display === 'none' || childStyle.visibility === 'hidden') {
              child.style.display = 'block';
              child.style.visibility = 'visible';
              child.style.opacity = '1';
            }
          });
        });
      });
    };

    // First, make content visible
    status.textContent = 'Loading content...';
    makeAllContentVisible();
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Update progress display
    const updateProgress = (current, total, stableCount, sectionsCount) => {
      const percentage = Math.min(100, Math.round((current / total) * 100));
      progressFill.style.width = percentage + '%';
      percentageText.textContent = percentage + '%';
      status.textContent = `${current.toLocaleString()}px / ${total.toLocaleString()}px`;
      if (sectionsCount > 0) {
        status.textContent += ` | ${sectionsCount} sections`;
      }
      if (stableCount > 0) {
        status.textContent += ` (${stableCount}/3 stable)`;
      }
    };

    // Smooth scroll function that triggers events
    const smoothScrollTo = async targetY => {
      const startY = window.scrollY;
      const distance = targetY - startY;
      const duration = 150; // ms (reduced for faster scrolling)
      const startTime = window.performance.now();

      return new Promise(resolve => {
        const scroll = currentTime => {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const easeProgress = progress * (2 - progress); // ease out

          window.scrollTo(0, startY + distance * easeProgress);

          // Dispatch scroll event to trigger listeners
          window.dispatchEvent(new window.Event('scroll'));

          if (progress < 1) {
            window.requestAnimationFrame(scroll);
          } else {
            resolve();
          }
        };
        window.requestAnimationFrame(scroll);
      });
    };

    // Start from the top
    await smoothScrollTo(0);
    await new Promise(resolve => setTimeout(resolve, 100));

    let lastHeight = document.documentElement.scrollHeight;
    let stableScrollCount = 0;

    // Scroll down in increments (2x viewport height for faster scrolling)
    const scrollStep = window.innerHeight * 2;
    let currentPosition = 0;

    while (!cancelled) {
      // Smooth scroll to current position
      await smoothScrollTo(currentPosition);

      // Wait for content to load (reduced for faster scrolling)
      await new Promise(resolve => setTimeout(resolve, 200));

      // Capture visible content blocks at current position
      const blocks = captureVisibleContentBlocks();
      blocks.forEach(block => {
        // Check if this content is similar to anything we've already captured
        const isDuplicate = Array.from(capturedHashes).some(existingContent => {
          const similarity = calculateSimilarity(block.normalizedContent, existingContent);
          return similarity > 0.85; // 85% similar = duplicate
        });

        if (!isDuplicate) {
          capturedHashes.add(block.normalizedContent);
          capturedContent.push(block.markdown);
        }
      });

      const newHeight = document.documentElement.scrollHeight;
      updateProgress(currentPosition, newHeight, stableScrollCount, capturedContent.length);

      // If we've reached the bottom and height hasn't changed for 3 consecutive attempts
      if (currentPosition >= newHeight) {
        if (newHeight === lastHeight) {
          stableScrollCount++;
          if (stableScrollCount >= 3) {
            percentageText.textContent = '100%';
            progressFill.style.width = '100%';
            status.textContent = `Complete! Captured ${capturedContent.length} sections`;
            break;
          }
        } else {
          stableScrollCount = 0;
        }
      }

      // Update tracking variables
      lastHeight = newHeight;
      currentPosition += scrollStep;
    }

    // Ensure we scroll all the way to the bottom and wait for content to render
    if (!cancelled) {
      await smoothScrollTo(document.documentElement.scrollHeight);
      await new Promise(resolve => setTimeout(resolve, 1000));

      // Expand any sections that became available during scrolling
      expandCollapsedSections();
      await new Promise(resolve => setTimeout(resolve, 500));

      // Do a second full scroll pass - some content only loads after first pass
      currentPosition = 0;
      const secondPassHeight = document.documentElement.scrollHeight;
      status.textContent = 'Second pass: loading remaining content...';

      while (currentPosition < secondPassHeight && !cancelled) {
        await smoothScrollTo(currentPosition);
        await new Promise(resolve => setTimeout(resolve, 200));

        // Capture any new content blocks in second pass
        const blocks = captureVisibleContentBlocks();
        blocks.forEach(block => {
          // Check if this content is similar to anything we've already captured
          const isDuplicate = Array.from(capturedHashes).some(existingContent => {
            const similarity = calculateSimilarity(block.normalizedContent, existingContent);
            return similarity > 0.85; // 85% similar = duplicate
          });

          if (!isDuplicate) {
            capturedHashes.add(block.normalizedContent);
            capturedContent.push(block.markdown);
          }
        });

        currentPosition += scrollStep;
      }

      // Final stay at bottom to ensure everything loads
      await smoothScrollTo(document.documentElement.scrollHeight);
      await new Promise(resolve => setTimeout(resolve, 1000));

      // One more expansion attempt
      expandCollapsedSections();
      await new Promise(resolve => setTimeout(resolve, 500));
    }

    // Fade out and remove overlay
    overlay.style.opacity = '0';
    await new Promise(resolve => setTimeout(resolve, 300));
    overlay.remove();

    // Return status and captured content
    return { cancelled, capturedContent };
  }

  // Scroll through the page first
  const scrollResult = await scrollToBottom();

  // If scrolling was cancelled, return null to indicate no download should occur
  if (scrollResult.cancelled) {
    return null;
  }

  // Combine all captured content sections
  const { capturedContent } = scrollResult;

  // Join all sections with double newlines for spacing
  const combinedMarkdown = capturedContent.join('\n\n---\n\n');

  return {
    markdown: combinedMarkdown,
    title: document.title,
    url: window.location.href,
  };
}

function sanitizeFilename(filename) {
  return filename
    .replace(/[<>:"/\\|?*]/g, '-')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .substring(0, 200);
}
```

## File: `extension-chrome/manifest.json`
```json
{
  "manifest_version": 3,
  "name": "__MSG_extensionName__",
  "version": "1.1.1",
  "description": "__MSG_extensionDescription__",
  "default_locale": "en",
  "author": "Lev Gelfenbuim",
  "homepage_url": "https://github.com/levz0r/markdown-printer",
  "permissions": ["activeTab", "contextMenus", "downloads", "scripting"],
  "background": {
    "service_worker": "background.js"
  },
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icon16.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  }
}
```

## File: `extension-chrome/popup.html`
```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <style>
      body {
        width: 300px;
        padding: 20px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }
      h1 {
        font-size: 18px;
        margin: 0 0 15px 0;
        color: #333;
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .logo {
        width: 32px;
        height: 32px;
      }
      .version {
        font-size: 10px;
        color: #999;
        font-weight: normal;
        margin-inline-start: auto;
      }
      .copyright {
        margin-top: 15px;
        font-size: 10px;
        color: #999;
        text-align: center;
      }
      .copyright a {
        color: #666;
        text-decoration: underline;
      }
      .copyright a:hover {
        color: #2196f3;
      }
      button {
        width: 100%;
        padding: 12px;
        background: #4caf50;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
        transition: background 0.3s;
      }
      button:hover {
        background: #45a049;
      }
      button:active {
        background: #3d8b40;
      }
      button:disabled {
        background: #ccc;
        cursor: not-allowed;
      }
      .info {
        margin-top: 15px;
        font-size: 12px;
        color: #666;
        line-height: 1.5;
      }
      .badge {
        display: inline-block;
        background: #2196f3;
        color: white;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 10px;
        font-weight: bold;
        margin-bottom: 10px;
      }
    </style>
  </head>
  <body>
    <h1>
      <img src="icon48.png" alt="MD" class="logo" />
      <span id="extensionName"></span>
      <span id="version" class="version"></span>
    </h1>
    <button id="saveBtn"></button>
    <div class="copyright">
      © <a href="https://lev.engineer" target="_blank">Lev Gelfenbuim</a> 2025
    </div>
    <script src="popup.js"></script>
  </body>
</html>
```

## File: `extension-chrome/popup.js`
```javascript
// Cross-browser compatibility
const browserAPI = typeof browser !== 'undefined' ? browser : chrome;

// Set localized text on load
document.addEventListener('DOMContentLoaded', () => {
  // Set text direction for RTL languages
  const uiLanguage = browserAPI.i18n.getUILanguage();
  const rtlLanguages = ['he', 'ar', 'fa', 'ur'];
  const isRTL = rtlLanguages.some(lang => uiLanguage.startsWith(lang));

  if (isRTL) {
    document.body.dir = 'rtl';
  }

  document.getElementById('extensionName').textContent =
    browserAPI.i18n.getMessage('extensionName');
  document.getElementById('saveBtn').textContent = browserAPI.i18n.getMessage('savePageButton');

  // Display version number
  const manifest = browserAPI.runtime.getManifest();
  document.getElementById('version').textContent = `v${manifest.version}`;
});

document.getElementById('saveBtn').addEventListener('click', async () => {
  const button = document.getElementById('saveBtn');
  const originalText = browserAPI.i18n.getMessage('savePageButton');
  button.disabled = true;
  button.textContent = 'Saving...';

  try {
    await browserAPI.runtime.sendMessage({ action: 'saveAsMarkdown' });
    button.textContent = 'Saved!';
    setTimeout(() => {
      button.textContent = originalText;
      button.disabled = false;
    }, 1500);
  } catch (_error) {
    button.textContent = 'Error - Try again';
    button.disabled = false;
    setTimeout(() => {
      button.textContent = originalText;
    }, 2000);
  }
});
```

## File: `extension-chrome/turndown.js`
```javascript
var TurndownService = (function () {
  'use strict';

  function extend (destination) {
    for (var i = 1; i < arguments.length; i++) {
      var source = arguments[i];
      for (var key in source) {
        if (source.hasOwnProperty(key)) destination[key] = source[key];
      }
    }
    return destination
  }

  function repeat (character, count) {
    return Array(count + 1).join(character)
  }

  function trimLeadingNewlines (string) {
    return string.replace(/^\n*/, '')
  }

  function trimTrailingNewlines (string) {
    // avoid match-at-end regexp bottleneck, see #370
    var indexEnd = string.length;
    while (indexEnd > 0 && string[indexEnd - 1] === '\n') indexEnd--;
    return string.substring(0, indexEnd)
  }

  var blockElements = [
    'ADDRESS', 'ARTICLE', 'ASIDE', 'AUDIO', 'BLOCKQUOTE', 'BODY', 'CANVAS',
    'CENTER', 'DD', 'DIR', 'DIV', 'DL', 'DT', 'FIELDSET', 'FIGCAPTION', 'FIGURE',
    'FOOTER', 'FORM', 'FRAMESET', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'HEADER',
    'HGROUP', 'HR', 'HTML', 'ISINDEX', 'LI', 'MAIN', 'MENU', 'NAV', 'NOFRAMES',
    'NOSCRIPT', 'OL', 'OUTPUT', 'P', 'PRE', 'SECTION', 'TABLE', 'TBODY', 'TD',
    'TFOOT', 'TH', 'THEAD', 'TR', 'UL'
  ];

  function isBlock (node) {
    return is(node, blockElements)
  }

  var voidElements = [
    'AREA', 'BASE', 'BR', 'COL', 'COMMAND', 'EMBED', 'HR', 'IMG', 'INPUT',
    'KEYGEN', 'LINK', 'META', 'PARAM', 'SOURCE', 'TRACK', 'WBR'
  ];

  function isVoid (node) {
    return is(node, voidElements)
  }

  function hasVoid (node) {
    return has(node, voidElements)
  }

  var meaningfulWhenBlankElements = [
    'A', 'TABLE', 'THEAD', 'TBODY', 'TFOOT', 'TH', 'TD', 'IFRAME', 'SCRIPT',
    'AUDIO', 'VIDEO'
  ];

  function isMeaningfulWhenBlank (node) {
    return is(node, meaningfulWhenBlankElements)
  }

  function hasMeaningfulWhenBlank (node) {
    return has(node, meaningfulWhenBlankElements)
  }

  function is (node, tagNames) {
    return tagNames.indexOf(node.nodeName) >= 0
  }

  function has (node, tagNames) {
    return (
      node.getElementsByTagName &&
      tagNames.some(function (tagName) {
        return node.getElementsByTagName(tagName).length
      })
    )
  }

  var rules = {};

  rules.paragraph = {
    filter: 'p',

    replacement: function (content) {
      return '\n\n' + content + '\n\n'
    }
  };

  rules.lineBreak = {
    filter: 'br',

    replacement: function (content, node, options) {
      return options.br + '\n'
    }
  };

  rules.heading = {
    filter: ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],

    replacement: function (content, node, options) {
      var hLevel = Number(node.nodeName.charAt(1));

      if (options.headingStyle === 'setext' && hLevel < 3) {
        var underline = repeat((hLevel === 1 ? '=' : '-'), content.length);
        return (
          '\n\n' + content + '\n' + underline + '\n\n'
        )
      } else {
        return '\n\n' + repeat('#', hLevel) + ' ' + content + '\n\n'
      }
    }
  };

  rules.blockquote = {
    filter: 'blockquote',

    replacement: function (content) {
      content = content.replace(/^\n+|\n+$/g, '');
      content = content.replace(/^/gm, '> ');
      return '\n\n' + content + '\n\n'
    }
  };

  rules.list = {
    filter: ['ul', 'ol'],

    replacement: function (content, node) {
      var parent = node.parentNode;
      if (parent.nodeName === 'LI' && parent.lastElementChild === node) {
        return '\n' + content
      } else {
        return '\n\n' + content + '\n\n'
      }
    }
  };

  rules.listItem = {
    filter: 'li',

    replacement: function (content, node, options) {
      content = content
        .replace(/^\n+/, '') // remove leading newlines
        .replace(/\n+$/, '\n') // replace trailing newlines with just a single one
        .replace(/\n/gm, '\n    '); // indent
      var prefix = options.bulletListMarker + '   ';
      var parent = node.parentNode;
      if (parent.nodeName === 'OL') {
        var start = parent.getAttribute('start');
        var index = Array.prototype.indexOf.call(parent.children, node);
        prefix = (start ? Number(start) + index : index + 1) + '.  ';
      }
      return (
        prefix + content + (node.nextSibling && !/\n$/.test(content) ? '\n' : '')
      )
    }
  };

  rules.indentedCodeBlock = {
    filter: function (node, options) {
      return (
        options.codeBlockStyle === 'indented' &&
        node.nodeName === 'PRE' &&
        node.firstChild &&
        node.firstChild.nodeName === 'CODE'
      )
    },

    replacement: function (content, node, options) {
      return (
        '\n\n    ' +
        node.firstChild.textContent.replace(/\n/g, '\n    ') +
        '\n\n'
      )
    }
  };

  rules.fencedCodeBlock = {
    filter: function (node, options) {
      return (
        options.codeBlockStyle === 'fenced' &&
        node.nodeName === 'PRE' &&
        node.firstChild &&
        node.firstChild.nodeName === 'CODE'
      )
    },

    replacement: function (content, node, options) {
      var className = node.firstChild.getAttribute('class') || '';
      var language = (className.match(/language-(\S+)/) || [null, ''])[1];
      var code = node.firstChild.textContent;

      var fenceChar = options.fence.charAt(0);
      var fenceSize = 3;
      var fenceInCodeRegex = new RegExp('^' + fenceChar + '{3,}', 'gm');

      var match;
      while ((match = fenceInCodeRegex.exec(code))) {
        if (match[0].length >= fenceSize) {
          fenceSize = match[0].length + 1;
        }
      }

      var fence = repeat(fenceChar, fenceSize);

      return (
        '\n\n' + fence + language + '\n' +
        code.replace(/\n$/, '') +
        '\n' + fence + '\n\n'
      )
    }
  };

  rules.horizontalRule = {
    filter: 'hr',

    replacement: function (content, node, options) {
      return '\n\n' + options.hr + '\n\n'
    }
  };

  rules.inlineLink = {
    filter: function (node, options) {
      return (
        options.linkStyle === 'inlined' &&
        node.nodeName === 'A' &&
        node.getAttribute('href')
      )
    },

    replacement: function (content, node) {
      var href = node.getAttribute('href');
      var title = cleanAttribute(node.getAttribute('title'));
      if (title) title = ' "' + title + '"';
      return '[' + content + '](' + href + title + ')'
    }
  };

  rules.referenceLink = {
    filter: function (node, options) {
      return (
        options.linkStyle === 'referenced' &&
        node.nodeName === 'A' &&
        node.getAttribute('href')
      )
    },

    replacement: function (content, node, options) {
      var href = node.getAttribute('href');
      var title = cleanAttribute(node.getAttribute('title'));
      if (title) title = ' "' + title + '"';
      var replacement;
      var reference;

      switch (options.linkReferenceStyle) {
        case 'collapsed':
          replacement = '[' + content + '][]';
          reference = '[' + content + ']: ' + href + title;
          break
        case 'shortcut':
          replacement = '[' + content + ']';
          reference = '[' + content + ']: ' + href + title;
          break
        default:
          var id = this.references.length + 1;
          replacement = '[' + content + '][' + id + ']';
          reference = '[' + id + ']: ' + href + title;
      }

      this.references.push(reference);
      return replacement
    },

    references: [],

    append: function (options) {
      var references = '';
      if (this.references.length) {
        references = '\n\n' + this.references.join('\n') + '\n\n';
        this.references = []; // Reset references
      }
      return references
    }
  };

  rules.emphasis = {
    filter: ['em', 'i'],

    replacement: function (content, node, options) {
      if (!content.trim()) return ''
      return options.emDelimiter + content + options.emDelimiter
    }
  };

  rules.strong = {
    filter: ['strong', 'b'],

    replacement: function (content, node, options) {
      if (!content.trim()) return ''
      return options.strongDelimiter + content + options.strongDelimiter
    }
  };

  rules.code = {
    filter: function (node) {
      var hasSiblings = node.previousSibling || node.nextSibling;
      var isCodeBlock = node.parentNode.nodeName === 'PRE' && !hasSiblings;

      return node.nodeName === 'CODE' && !isCodeBlock
    },

    replacement: function (content) {
      if (!content) return ''
      content = content.replace(/\r?\n|\r/g, ' ');

      var extraSpace = /^`|^ .*?[^ ].* $|`$/.test(content) ? ' ' : '';
      var delimiter = '`';
      var matches = content.match(/`+/gm) || [];
      while (matches.indexOf(delimiter) !== -1) delimiter = delimiter + '`';

      return delimiter + extraSpace + content + extraSpace + delimiter
    }
  };

  rules.image = {
    filter: 'img',

    replacement: function (content, node) {
      var alt = cleanAttribute(node.getAttribute('alt'));
      var src = node.getAttribute('src') || '';
      var title = cleanAttribute(node.getAttribute('title'));
      var titlePart = title ? ' "' + title + '"' : '';
      return src ? '![' + alt + ']' + '(' + src + titlePart + ')' : ''
    }
  };

  function cleanAttribute (attribute) {
    return attribute ? attribute.replace(/(\n+\s*)+/g, '\n') : ''
  }

  /**
   * Manages a collection of rules used to convert HTML to Markdown
   */

  function Rules (options) {
    this.options = options;
    this._keep = [];
    this._remove = [];

    this.blankRule = {
      replacement: options.blankReplacement
    };

    this.keepReplacement = options.keepReplacement;

    this.defaultRule = {
      replacement: options.defaultReplacement
    };

    this.array = [];
    for (var key in options.rules) this.array.push(options.rules[key]);
  }

  Rules.prototype = {
    add: function (key, rule) {
      this.array.unshift(rule);
    },

    keep: function (filter) {
      this._keep.unshift({
        filter: filter,
        replacement: this.keepReplacement
      });
    },

    remove: function (filter) {
      this._remove.unshift({
        filter: filter,
        replacement: function () {
          return ''
        }
      });
    },

    forNode: function (node) {
      if (node.isBlank) return this.blankRule
      var rule;

      if ((rule = findRule(this.array, node, this.options))) return rule
      if ((rule = findRule(this._keep, node, this.options))) return rule
      if ((rule = findRule(this._remove, node, this.options))) return rule

      return this.defaultRule
    },

    forEach: function (fn) {
      for (var i = 0; i < this.array.length; i++) fn(this.array[i], i);
    }
  };

  function findRule (rules, node, options) {
    for (var i = 0; i < rules.length; i++) {
      var rule = rules[i];
      if (filterValue(rule, node, options)) return rule
    }
    return void 0
  }

  function filterValue (rule, node, options) {
    var filter = rule.filter;
    if (typeof filter === 'string') {
      if (filter === node.nodeName.toLowerCase()) return true
    } else if (Array.isArray(filter)) {
      if (filter.indexOf(node.nodeName.toLowerCase()) > -1) return true
    } else if (typeof filter === 'function') {
      if (filter.call(rule, node, options)) return true
    } else {
      throw new TypeError('`filter` needs to be a string, array, or function')
    }
  }

  /**
   * The collapseWhitespace function is adapted from collapse-whitespace
   * by Luc Thevenard.
   *
   * The MIT License (MIT)
   *
   * Copyright (c) 2014 Luc Thevenard <lucthevenard@gmail.com>
   *
   * Permission is hereby granted, free of charge, to any person obtaining a copy
   * of this software and associated documentation files (the "Software"), to deal
   * in the Software without restriction, including without limitation the rights
   * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   * copies of the Software, and to permit persons to whom the Software is
   * furnished to do so, subject to the following conditions:
   *
   * The above copyright notice and this permission notice shall be included in
   * all copies or substantial portions of the Software.
   *
   * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   * THE SOFTWARE.
   */

  /**
   * collapseWhitespace(options) removes extraneous whitespace from an the given element.
   *
   * @param {Object} options
   */
  function collapseWhitespace (options) {
    var element = options.element;
    var isBlock = options.isBlock;
    var isVoid = options.isVoid;
    var isPre = options.isPre || function (node) {
      return node.nodeName === 'PRE'
    };

    if (!element.firstChild || isPre(element)) return

    var prevText = null;
    var keepLeadingWs = false;

    var prev = null;
    var node = next(prev, element, isPre);

    while (node !== element) {
      if (node.nodeType === 3 || node.nodeType === 4) { // Node.TEXT_NODE or Node.CDATA_SECTION_NODE
        var text = node.data.replace(/[ \r\n\t]+/g, ' ');

        if ((!prevText || / $/.test(prevText.data)) &&
            !keepLeadingWs && text[0] === ' ') {
          text = text.substr(1);
        }

        // `text` might be empty at this point.
        if (!text) {
          node = remove(node);
          continue
        }

        node.data = text;

        prevText = node;
      } else if (node.nodeType === 1) { // Node.ELEMENT_NODE
        if (isBlock(node) || node.nodeName === 'BR') {
          if (prevText) {
            prevText.data = prevText.data.replace(/ $/, '');
          }

          prevText = null;
          keepLeadingWs = false;
        } else if (isVoid(node) || isPre(node)) {
          // Avoid trimming space around non-block, non-BR void elements and inline PRE.
          prevText = null;
          keepLeadingWs = true;
        } else if (prevText) {
          // Drop protection if set previously.
          keepLeadingWs = false;
        }
      } else {
        node = remove(node);
        continue
      }

      var nextNode = next(prev, node, isPre);
      prev = node;
      node = nextNode;
    }

    if (prevText) {
      prevText.data = prevText.data.replace(/ $/, '');
      if (!prevText.data) {
        remove(prevText);
      }
    }
  }

  /**
   * remove(node) removes the given node from the DOM and returns the
   * next node in the sequence.
   *
   * @param {Node} node
   * @return {Node} node
   */
  function remove (node) {
    var next = node.nextSibling || node.parentNode;

    node.parentNode.removeChild(node);

    return next
  }

  /**
   * next(prev, current, isPre) returns the next node in the sequence, given the
   * current and previous nodes.
   *
   * @param {Node} prev
   * @param {Node} current
   * @param {Function} isPre
   * @return {Node}
   */
  function next (prev, current, isPre) {
    if ((prev && prev.parentNode === current) || isPre(current)) {
      return current.nextSibling || current.parentNode
    }

    return current.firstChild || current.nextSibling || current.parentNode
  }

  /*
   * Set up window for Node.js
   */

  var root = (typeof window !== 'undefined' ? window : {});

  /*
   * Parsing HTML strings
   */

  function canParseHTMLNatively () {
    var Parser = root.DOMParser;
    var canParse = false;

    // Adapted from https://gist.github.com/1129031
    // Firefox/Opera/IE throw errors on unsupported types
    try {
      // WebKit returns null on unsupported types
      if (new Parser().parseFromString('', 'text/html')) {
        canParse = true;
      }
    } catch (e) {}

    return canParse
  }

  function createHTMLParser () {
    var Parser = function () {};

    {
      if (shouldUseActiveX()) {
        Parser.prototype.parseFromString = function (string) {
          var doc = new window.ActiveXObject('htmlfile');
          doc.designMode = 'on'; // disable on-page scripts
          doc.open();
          doc.write(string);
          doc.close();
          return doc
        };
      } else {
        Parser.prototype.parseFromString = function (string) {
          var doc = document.implementation.createHTMLDocument('');
          doc.open();
          doc.write(string);
          doc.close();
          return doc
        };
      }
    }
    return Parser
  }

  function shouldUseActiveX () {
    var useActiveX = false;
    try {
      document.implementation.createHTMLDocument('').open();
    } catch (e) {
      if (window.ActiveXObject) useActiveX = true;
    }
    return useActiveX
  }

  var HTMLParser = canParseHTMLNatively() ? root.DOMParser : createHTMLParser();

  function RootNode (input, options) {
    var root;
    if (typeof input === 'string') {
      var doc = htmlParser().parseFromString(
        // DOM parsers arrange elements in the <head> and <body>.
        // Wrapping in a custom element ensures elements are reliably arranged in
        // a single element.
        '<x-turndown id="turndown-root">' + input + '</x-turndown>',
        'text/html'
      );
      root = doc.getElementById('turndown-root');
    } else {
      root = input.cloneNode(true);
    }
    collapseWhitespace({
      element: root,
      isBlock: isBlock,
      isVoid: isVoid,
      isPre: options.preformattedCode ? isPreOrCode : null
    });

    return root
  }

  var _htmlParser;
  function htmlParser () {
    _htmlParser = _htmlParser || new HTMLParser();
    return _htmlParser
  }

  function isPreOrCode (node) {
    return node.nodeName === 'PRE' || node.nodeName === 'CODE'
  }

  function Node (node, options) {
    node.isBlock = isBlock(node);
    node.isCode = node.nodeName === 'CODE' || node.parentNode.isCode;
    node.isBlank = isBlank(node);
    node.flankingWhitespace = flankingWhitespace(node, options);
    return node
  }

  function isBlank (node) {
    return (
      !isVoid(node) &&
      !isMeaningfulWhenBlank(node) &&
      /^\s*$/i.test(node.textContent) &&
      !hasVoid(node) &&
      !hasMeaningfulWhenBlank(node)
    )
  }

  function flankingWhitespace (node, options) {
    if (node.isBlock || (options.preformattedCode && node.isCode)) {
      return { leading: '', trailing: '' }
    }

    var edges = edgeWhitespace(node.textContent);

    // abandon leading ASCII WS if left-flanked by ASCII WS
    if (edges.leadingAscii && isFlankedByWhitespace('left', node, options)) {
      edges.leading = edges.leadingNonAscii;
    }

    // abandon trailing ASCII WS if right-flanked by ASCII WS
    if (edges.trailingAscii && isFlankedByWhitespace('right', node, options)) {
      edges.trailing = edges.trailingNonAscii;
    }

    return { leading: edges.leading, trailing: edges.trailing }
  }

  function edgeWhitespace (string) {
    var m = string.match(/^(([ \t\r\n]*)(\s*))(?:(?=\S)[\s\S]*\S)?((\s*?)([ \t\r\n]*))$/);
    return {
      leading: m[1], // whole string for whitespace-only strings
      leadingAscii: m[2],
      leadingNonAscii: m[3],
      trailing: m[4], // empty for whitespace-only strings
      trailingNonAscii: m[5],
      trailingAscii: m[6]
    }
  }

  function isFlankedByWhitespace (side, node, options) {
    var sibling;
    var regExp;
    var isFlanked;

    if (side === 'left') {
      sibling = node.previousSibling;
      regExp = / $/;
    } else {
      sibling = node.nextSibling;
      regExp = /^ /;
    }

    if (sibling) {
      if (sibling.nodeType === 3) {
        isFlanked = regExp.test(sibling.nodeValue);
      } else if (options.preformattedCode && sibling.nodeName === 'CODE') {
        isFlanked = false;
      } else if (sibling.nodeType === 1 && !isBlock(sibling)) {
        isFlanked = regExp.test(sibling.textContent);
      }
    }
    return isFlanked
  }

  var reduce = Array.prototype.reduce;
  var escapes = [
    [/\\/g, '\\\\'],
    [/\*/g, '\\*'],
    [/^-/g, '\\-'],
    [/^\+ /g, '\\+ '],
    [/^(=+)/g, '\\$1'],
    [/^(#{1,6}) /g, '\\$1 '],
    [/`/g, '\\`'],
    [/^~~~/g, '\\~~~'],
    [/\[/g, '\\['],
    [/\]/g, '\\]'],
    [/^>/g, '\\>'],
    [/_/g, '\\_'],
    [/^(\d+)\. /g, '$1\\. ']
  ];

  function TurndownService (options) {
    if (!(this instanceof TurndownService)) return new TurndownService(options)

    var defaults = {
      rules: rules,
      headingStyle: 'setext',
      hr: '* * *',
      bulletListMarker: '*',
      codeBlockStyle: 'indented',
      fence: '```',
      emDelimiter: '_',
      strongDelimiter: '**',
      linkStyle: 'inlined',
      linkReferenceStyle: 'full',
      br: '  ',
      preformattedCode: false,
      blankReplacement: function (content, node) {
        return node.isBlock ? '\n\n' : ''
      },
      keepReplacement: function (content, node) {
        return node.isBlock ? '\n\n' + node.outerHTML + '\n\n' : node.outerHTML
      },
      defaultReplacement: function (content, node) {
        return node.isBlock ? '\n\n' + content + '\n\n' : content
      }
    };
    this.options = extend({}, defaults, options);
    this.rules = new Rules(this.options);
  }

  TurndownService.prototype = {
    /**
     * The entry point for converting a string or DOM node to Markdown
     * @public
     * @param {String|HTMLElement} input The string or DOM node to convert
     * @returns A Markdown representation of the input
     * @type String
     */

    turndown: function (input) {
      if (!canConvert(input)) {
        throw new TypeError(
          input + ' is not a string, or an element/document/fragment node.'
        )
      }

      if (input === '') return ''

      var output = process.call(this, new RootNode(input, this.options));
      return postProcess.call(this, output)
    },

    /**
     * Add one or more plugins
     * @public
     * @param {Function|Array} plugin The plugin or array of plugins to add
     * @returns The Turndown instance for chaining
     * @type Object
     */

    use: function (plugin) {
      if (Array.isArray(plugin)) {
        for (var i = 0; i < plugin.length; i++) this.use(plugin[i]);
      } else if (typeof plugin === 'function') {
        plugin(this);
      } else {
        throw new TypeError('plugin must be a Function or an Array of Functions')
      }
      return this
    },

    /**
     * Adds a rule
     * @public
     * @param {String} key The unique key of the rule
     * @param {Object} rule The rule
     * @returns The Turndown instance for chaining
     * @type Object
     */

    addRule: function (key, rule) {
      this.rules.add(key, rule);
      return this
    },

    /**
     * Keep a node (as HTML) that matches the filter
     * @public
     * @param {String|Array|Function} filter The unique key of the rule
     * @returns The Turndown instance for chaining
     * @type Object
     */

    keep: function (filter) {
      this.rules.keep(filter);
      return this
    },

    /**
     * Remove a node that matches the filter
     * @public
     * @param {String|Array|Function} filter The unique key of the rule
     * @returns The Turndown instance for chaining
     * @type Object
     */

    remove: function (filter) {
      this.rules.remove(filter);
      return this
    },

    /**
     * Escapes Markdown syntax
     * @public
     * @param {String} string The string to escape
     * @returns A string with Markdown syntax escaped
     * @type String
     */

    escape: function (string) {
      return escapes.reduce(function (accumulator, escape) {
        return accumulator.replace(escape[0], escape[1])
      }, string)
    }
  };

  /**
   * Reduces a DOM node down to its Markdown string equivalent
   * @private
   * @param {HTMLElement} parentNode The node to convert
   * @returns A Markdown representation of the node
   * @type String
   */

  function process (parentNode) {
    var self = this;
    return reduce.call(parentNode.childNodes, function (output, node) {
      node = new Node(node, self.options);

      var replacement = '';
      if (node.nodeType === 3) {
        replacement = node.isCode ? node.nodeValue : self.escape(node.nodeValue);
      } else if (node.nodeType === 1) {
        replacement = replacementForNode.call(self, node);
      }

      return join(output, replacement)
    }, '')
  }

  /**
   * Appends strings as each rule requires and trims the output
   * @private
   * @param {String} output The conversion output
   * @returns A trimmed version of the ouput
   * @type String
   */

  function postProcess (output) {
    var self = this;
    this.rules.forEach(function (rule) {
      if (typeof rule.append === 'function') {
        output = join(output, rule.append(self.options));
      }
    });

    return output.replace(/^[\t\r\n]+/, '').replace(/[\t\r\n\s]+$/, '')
  }

  /**
   * Converts an element node to its Markdown equivalent
   * @private
   * @param {HTMLElement} node The node to convert
   * @returns A Markdown representation of the node
   * @type String
   */

  function replacementForNode (node) {
    var rule = this.rules.forNode(node);
    var content = process.call(this, node);
    var whitespace = node.flankingWhitespace;
    if (whitespace.leading || whitespace.trailing) content = content.trim();
    return (
      whitespace.leading +
      rule.replacement(content, node, this.options) +
      whitespace.trailing
    )
  }

  /**
   * Joins replacement to the current output with appropriate number of new lines
   * @private
   * @param {String} output The current conversion output
   * @param {String} replacement The string to append to the output
   * @returns Joined output
   * @type String
   */

  function join (output, replacement) {
    var s1 = trimTrailingNewlines(output);
    var s2 = trimLeadingNewlines(replacement);
    var nls = Math.max(output.length - s1.length, replacement.length - s2.length);
    var separator = '\n\n'.substring(0, nls);

    return s1 + separator + s2
  }

  /**
   * Determines whether an input can be converted
   * @private
   * @param {String|HTMLElement} input Describe this parameter
   * @returns Describe what it returns
   * @type String|Object|Array|Boolean|Number
   */

  function canConvert (input) {
    return (
      input != null && (
        typeof input === 'string' ||
        (input.nodeType && (
          input.nodeType === 1 || input.nodeType === 9 || input.nodeType === 11
        ))
      )
    )
  }

  return TurndownService;

}());
```

## File: `extension-chrome/_locales/en/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "Save web pages as Markdown files to your Downloads folder. No setup required!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "Save Page as Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Save as Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `extension-chrome/_locales/fr/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "Enregistrez des pages web en tant que fichiers Markdown dans votre dossier Téléchargements. Aucune configuration requise !",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "Enregistrer la page en Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Enregistrer en Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `extension-chrome/_locales/he/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "שמור דפי אינטרנט כקבצי Markdown לתיקיית ההורדות. ללא הגדרות נדרשות!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "שמור דף כ-Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "שמור כ-Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `extension-chrome/_locales/hi/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "वेब पेजों को Markdown फ़ाइलों के रूप में अपने डाउनलोड फ़ोल्डर में सहेजें। किसी सेटअप की आवश्यकता नहीं!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "पेज को Markdown के रूप में सहेजें",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Markdown के रूप में सहेजें",
    "description": "Context menu item title"
  }
}
```

## File: `extension-firefox/background.js`
```javascript
// Cross-browser compatibility
const browserAPI = typeof browser !== 'undefined' ? browser : chrome;

// Create context menu on installation
browserAPI.runtime.onInstalled.addListener(() => {
  browserAPI.contextMenus.create({
    id: 'saveAsMarkdown',
    title: browserAPI.i18n.getMessage('contextMenuTitle'),
    contexts: ['page'],
  });
});

// Handle context menu click
browserAPI.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === 'saveAsMarkdown') {
    savePageAsMarkdown(tab.id);
  }
});

// Handle messages from popup
browserAPI.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'saveAsMarkdown') {
    browserAPI.tabs.query({ active: true, currentWindow: true }, async tabs => {
      if (tabs[0]) {
        try {
          await savePageAsMarkdown(tabs[0].id);
          sendResponse({ success: true });
        } catch (error) {
          sendResponse({ success: false, error: error.message });
        }
      }
    });
    return true; // Keep the message channel open for async response
  }
});

async function savePageAsMarkdown(tabId) {
  try {
    // Inject Turndown library and conversion script
    await browserAPI.scripting
      .executeScript({
        target: { tabId: tabId },
        files: ['turndown.js'],
      })
      .catch(error => {
        // Better error message for protected pages
        if (
          error.message.includes('cannot be scripted') ||
          error.message.includes('Cannot access') ||
          error.message.includes('extensions gallery')
        ) {
          throw new Error(
            'Cannot save this page - extensions are blocked on browser internal pages and extension stores'
          );
        }
        throw error;
      });

    // Inject script to convert and get markdown
    const results = await browserAPI.scripting.executeScript({
      target: { tabId: tabId },
      func: extractAndConvertToMarkdown,
    });

    if (!results || !results[0]) {
      throw new Error('Failed to extract page content');
    }

    const result = results[0].result;

    // If operation was cancelled, exit without showing save dialog
    if (!result || result === null) {
      return;
    }

    const { markdown, title, url } = result;

    // Generate filename
    const timestamp = new Date().toISOString().split('T')[0];
    const sanitizedTitle = sanitizeFilename(title || 'untitled');
    const filename = `${sanitizedTitle}-${timestamp}.md`;

    // Get extension version
    const version = browserAPI.runtime.getManifest().version;

    // Add metadata header with attribution
    const content = `# ${title}\n\n**Source:** ${url}\n**Saved:** ${new Date().toISOString()}\n\n*Generated with [markdown-printer](https://github.com/levz0r/markdown-printer) (v${version}) by [Lev Gelfenbuim](https://lev.engineer)*\n\n---\n\n${markdown}`;

    // For Firefox, we need to use a different approach
    // Check if we're in Firefox by checking for browser.downloads
    const isFirefox = typeof browser !== 'undefined' && browser.downloads;

    if (isFirefox) {
      // Firefox: Use blob URL approach with special handling
      // Create a temporary object URL in a way that works in Firefox background scripts
      // We'll inject a helper script into the page to create the blob URL
      await browserAPI.scripting.executeScript({
        target: { tabId: tabId },
        func: (content, filename) => {
          const blob = new Blob([content], { type: 'text/plain' });
          const url = URL.createObjectURL(blob);
          // Trigger download from page context
          const a = document.createElement('a');
          a.href = url;
          a.download = filename;
          a.click();
          URL.revokeObjectURL(url);
          return true;
        },
        args: [content, filename],
      });
    } else {
      // Chrome: Use data URL
      const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
      const reader = new FileReader();

      const dataUrl = await new Promise((resolve, reject) => {
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(blob);
      });

      await browserAPI.downloads.download({
        url: dataUrl,
        filename: filename,
        saveAs: true,
      });
    }
  } catch (error) {
    console.error('Error saving markdown:', error);
    throw error;
  }
}

// This function runs in the page context
async function extractAndConvertToMarkdown() {
  // Normalize HTML content for consistent hashing
  // Removes attributes, IDs, classes, and normalizes whitespace
  function normalizeContent(element) {
    const clone = element.cloneNode(true);

    // Remove all unwanted elements
    const unwantedSelectors = [
      'script',
      'style',
      'noscript',
      'iframe',
      'svg',
      'nav',
      'header',
      'footer',
      '.sidebar',
      '.navigation',
      '.menu',
      '[class*="sidebar"]',
      '[class*="navigation"]',
      'button',
      'input',
      'select',
      'textarea',
    ];

    unwantedSelectors.forEach(selector => {
      const elements = clone.querySelectorAll(selector);
      elements.forEach(el => el.remove());
    });

    // Get text content and normalize whitespace
    const text = clone.textContent || '';
    return text.replace(/\s+/g, ' ').trim();
  }

  // Function to check if element is in viewport
  function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    const windowWidth = window.innerWidth || document.documentElement.clientWidth;

    // Element is in viewport if any part of it is visible
    return rect.top < windowHeight && rect.bottom > 0 && rect.left < windowWidth && rect.right > 0;
  }

  // Calculate Jaccard similarity between two strings
  function calculateSimilarity(str1, str2) {
    // Split into words and filter out very short words
    const words1 = new Set(
      str1
        .toLowerCase()
        .split(/\s+/)
        .filter(w => w.length > 2)
    );
    const words2 = new Set(
      str2
        .toLowerCase()
        .split(/\s+/)
        .filter(w => w.length > 2)
    );

    if (words1.size === 0 && words2.size === 0) {
      return 1;
    }
    if (words1.size === 0 || words2.size === 0) {
      return 0;
    }

    const intersection = new Set([...words1].filter(x => words2.has(x)));
    const union = new Set([...words1, ...words2]);

    return intersection.size / union.size;
  }

  // Function to capture currently visible content blocks
  function captureVisibleContentBlocks() {
    const capturedBlocks = [];

    try {
      // Find content blocks - prioritize semantic elements
      const blockSelectors = [
        'article',
        'section',
        'main > div',
        '[role="main"] > div',
        '.content > div',
        '.documentation-content > div',
        'main > *',
        '[role="main"] > *',
      ];

      const foundBlocks = new Set();

      // Try ALL selectors and combine results (don't stop at first match)
      for (const selector of blockSelectors) {
        const elements = document.querySelectorAll(selector);

        if (elements.length > 0) {
          elements.forEach(element => {
            // Skip if already found this element
            if (foundBlocks.has(element)) {
              return;
            }

            // Only capture if element is in viewport and has substantial content
            if (isInViewport(element)) {
              const text = element.textContent || '';
              if (text.trim().length > 100) {
                foundBlocks.add(element);

                // Clone and convert to markdown
                const cloned = element.cloneNode(true);

                // Remove unwanted elements from clone
                const unwantedSelectors = [
                  'script',
                  'style',
                  'noscript',
                  'iframe',
                  'svg',
                  'nav',
                  'header',
                  'footer',
                  'button:not([role="tab"])',
                  'input',
                  'select',
                  'textarea',
                  '#markdown-printer-overlay',
                ];

                unwantedSelectors.forEach(sel => {
                  const elements = cloned.querySelectorAll(sel);
                  elements.forEach(el => el.remove());
                });

                const tempTurndown = new TurndownService({
                  headingStyle: 'atx',
                  codeBlockStyle: 'fenced',
                  bulletListMarker: '-',
                });
                tempTurndown.remove(['script', 'style', 'noscript', 'iframe', 'svg']);

                const markdown = tempTurndown.turndown(cloned);

                if (markdown && markdown.trim().length > 100) {
                  capturedBlocks.push({
                    markdown: markdown,
                    normalizedContent: normalizeContent(element),
                  });
                }
              }
            }
          });
        }
      }

      // Fallback: If no blocks found, try capturing the entire main content area
      if (capturedBlocks.length === 0) {
        const mainSelectors = ['main', '[role="main"]', 'article', '#content', '.content', 'body'];

        for (const selector of mainSelectors) {
          const mainElement = document.querySelector(selector);
          if (mainElement) {
            const text = mainElement.textContent || '';
            if (text.trim().length > 100) {
              const cloned = mainElement.cloneNode(true);

              // Remove unwanted elements
              const unwantedSelectors = [
                'script',
                'style',
                'noscript',
                'iframe',
                'svg',
                'nav',
                'header',
                'footer',
                'aside',
                '.sidebar',
                '.navigation',
                '.menu',
                'button',
                'input',
                'select',
                'textarea',
                '#markdown-printer-overlay',
              ];

              unwantedSelectors.forEach(sel => {
                const elements = cloned.querySelectorAll(sel);
                elements.forEach(el => el.remove());
              });

              const tempTurndown = new TurndownService({
                headingStyle: 'atx',
                codeBlockStyle: 'fenced',
                bulletListMarker: '-',
              });
              tempTurndown.remove(['script', 'style', 'noscript', 'iframe', 'svg']);

              const markdown = tempTurndown.turndown(cloned);

              if (markdown && markdown.trim().length > 100) {
                capturedBlocks.push({
                  markdown: markdown,
                  normalizedContent: normalizeContent(mainElement),
                });
                break; // Found content, stop trying
              }
            }
          }
        }
      }

      return capturedBlocks;
    } catch (error) {
      console.error('Error capturing content blocks:', error);
      return [];
    }
  }

  // Function to scroll through the entire page to trigger lazy loading
  async function scrollToBottom() {
    // Arrays to store captured content
    const capturedContent = [];
    const capturedHashes = new Set();

    // First, try to expand any collapsed/hidden sections
    const expandCollapsedSections = () => {
      // Find and click on common expandable elements
      const expandableSelectors = [
        'details:not([open])',
        '[aria-expanded="false"]',
        '.collapsed',
        '.expand',
        '.accordion:not(.active)',
        '[data-collapsed="true"]',
        'button[aria-expanded="false"]',
      ];

      let expandedCount = 0;
      expandableSelectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
          try {
            if (el.tagName === 'DETAILS') {
              el.open = true;
            } else if (el.click) {
              el.click();
            }
            expandedCount++;
          } catch (_e) {
            // Ignore errors
          }
        });
      });
      return expandedCount;
    };

    // Try to expand sections before scrolling
    expandCollapsedSections();
    await new Promise(resolve => setTimeout(resolve, 500));

    // Create progress indicator overlay
    const overlay = document.createElement('div');
    overlay.id = 'markdown-printer-overlay';
    overlay.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: rgba(0, 0, 0, 0.9);
      color: white;
      padding: 20px;
      border-radius: 8px;
      z-index: 999999;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
      min-width: 300px;
      opacity: 0;
      transition: opacity 0.3s ease-in-out;
    `;

    const title = document.createElement('div');
    title.textContent = 'Printing...';
    title.style.cssText = 'font-weight: bold; margin-bottom: 10px; font-size: 16px;';

    const percentageText = document.createElement('div');
    percentageText.id = 'percentage-text';
    percentageText.style.cssText =
      'font-size: 24px; font-weight: bold; margin-bottom: 5px; color: #4CAF50;';
    percentageText.textContent = '0%';

    const status = document.createElement('div');
    status.id = 'scroll-status';
    status.style.cssText = 'margin-bottom: 10px; font-size: 14px; opacity: 0.8;';

    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 2px;
      overflow: hidden;
      margin-bottom: 10px;
    `;

    const progressFill = document.createElement('div');
    progressFill.id = 'progress-fill';
    progressFill.style.cssText = `
      height: 100%;
      background: #4CAF50;
      width: 0%;
      transition: width 0.3s ease;
    `;
    progressBar.appendChild(progressFill);

    const cancelButton = document.createElement('button');
    cancelButton.textContent = 'Abort';
    cancelButton.style.cssText = `
      width: 100%;
      padding: 8px;
      background: #f44336;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      font-weight: bold;
      transition: background 0.2s ease;
    `;
    cancelButton.onmouseover = () => (cancelButton.style.background = '#d32f2f');
    cancelButton.onmouseout = () => (cancelButton.style.background = '#f44336');

    overlay.appendChild(title);
    overlay.appendChild(percentageText);
    overlay.appendChild(status);
    overlay.appendChild(progressBar);
    overlay.appendChild(cancelButton);
    document.body.appendChild(overlay);

    // Trigger fade-in animation
    window.requestAnimationFrame(() => {
      overlay.style.opacity = '1';
    });

    let cancelled = false;
    cancelButton.onclick = () => {
      cancelled = true;
      status.textContent = 'Stopping...';
      cancelButton.disabled = true;
      cancelButton.style.opacity = '0.5';
    };

    // Make all hidden content sections visible (common in documentation sites)
    const makeAllContentVisible = () => {
      // Target common documentation content containers
      const contentSelectors = [
        'article',
        'section',
        'main',
        '[role="main"]',
        '[class*="content"]',
        '[class*="documentation"]',
        '[class*="api"]',
        '[class*="endpoint"]',
        '[id*="content"]',
      ];

      contentSelectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
          const style = window.getComputedStyle(el);
          if (style.display === 'none' || style.visibility === 'hidden') {
            el.style.display = 'block';
            el.style.visibility = 'visible';
            el.style.opacity = '1';
          }
          // Also unhide all children
          el.querySelectorAll('*').forEach(child => {
            const childStyle = window.getComputedStyle(child);
            if (childStyle.display === 'none' || childStyle.visibility === 'hidden') {
              child.style.display = 'block';
              child.style.visibility = 'visible';
              child.style.opacity = '1';
            }
          });
        });
      });
    };

    // First, make content visible
    status.textContent = 'Loading content...';
    makeAllContentVisible();
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Update progress display
    const updateProgress = (current, total, stableCount, sectionsCount) => {
      const percentage = Math.min(100, Math.round((current / total) * 100));
      progressFill.style.width = percentage + '%';
      percentageText.textContent = percentage + '%';
      status.textContent = `${current.toLocaleString()}px / ${total.toLocaleString()}px`;
      if (sectionsCount > 0) {
        status.textContent += ` | ${sectionsCount} sections`;
      }
      if (stableCount > 0) {
        status.textContent += ` (${stableCount}/3 stable)`;
      }
    };

    // Smooth scroll function that triggers events
    const smoothScrollTo = async targetY => {
      const startY = window.scrollY;
      const distance = targetY - startY;
      const duration = 150; // ms (reduced for faster scrolling)
      const startTime = window.performance.now();

      return new Promise(resolve => {
        const scroll = currentTime => {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const easeProgress = progress * (2 - progress); // ease out

          window.scrollTo(0, startY + distance * easeProgress);

          // Dispatch scroll event to trigger listeners
          window.dispatchEvent(new window.Event('scroll'));

          if (progress < 1) {
            window.requestAnimationFrame(scroll);
          } else {
            resolve();
          }
        };
        window.requestAnimationFrame(scroll);
      });
    };

    // Start from the top
    await smoothScrollTo(0);
    await new Promise(resolve => setTimeout(resolve, 100));

    let lastHeight = document.documentElement.scrollHeight;
    let stableScrollCount = 0;

    // Scroll down in increments (2x viewport height for faster scrolling)
    const scrollStep = window.innerHeight * 2;
    let currentPosition = 0;

    while (!cancelled) {
      // Smooth scroll to current position
      await smoothScrollTo(currentPosition);

      // Wait for content to load (reduced for faster scrolling)
      await new Promise(resolve => setTimeout(resolve, 200));

      // Capture visible content blocks at current position
      const blocks = captureVisibleContentBlocks();
      blocks.forEach(block => {
        // Check if this content is similar to anything we've already captured
        const isDuplicate = Array.from(capturedHashes).some(existingContent => {
          const similarity = calculateSimilarity(block.normalizedContent, existingContent);
          return similarity > 0.85; // 85% similar = duplicate
        });

        if (!isDuplicate) {
          capturedHashes.add(block.normalizedContent);
          capturedContent.push(block.markdown);
        }
      });

      const newHeight = document.documentElement.scrollHeight;
      updateProgress(currentPosition, newHeight, stableScrollCount, capturedContent.length);

      // If we've reached the bottom and height hasn't changed for 3 consecutive attempts
      if (currentPosition >= newHeight) {
        if (newHeight === lastHeight) {
          stableScrollCount++;
          if (stableScrollCount >= 3) {
            percentageText.textContent = '100%';
            progressFill.style.width = '100%';
            status.textContent = `Complete! Captured ${capturedContent.length} sections`;
            break;
          }
        } else {
          stableScrollCount = 0;
        }
      }

      // Update tracking variables
      lastHeight = newHeight;
      currentPosition += scrollStep;
    }

    // Ensure we scroll all the way to the bottom and wait for content to render
    if (!cancelled) {
      await smoothScrollTo(document.documentElement.scrollHeight);
      await new Promise(resolve => setTimeout(resolve, 1000));

      // Expand any sections that became available during scrolling
      expandCollapsedSections();
      await new Promise(resolve => setTimeout(resolve, 500));

      // Do a second full scroll pass - some content only loads after first pass
      currentPosition = 0;
      const secondPassHeight = document.documentElement.scrollHeight;
      status.textContent = 'Second pass: loading remaining content...';

      while (currentPosition < secondPassHeight && !cancelled) {
        await smoothScrollTo(currentPosition);
        await new Promise(resolve => setTimeout(resolve, 200));

        // Capture any new content blocks in second pass
        const blocks = captureVisibleContentBlocks();
        blocks.forEach(block => {
          // Check if this content is similar to anything we've already captured
          const isDuplicate = Array.from(capturedHashes).some(existingContent => {
            const similarity = calculateSimilarity(block.normalizedContent, existingContent);
            return similarity > 0.85; // 85% similar = duplicate
          });

          if (!isDuplicate) {
            capturedHashes.add(block.normalizedContent);
            capturedContent.push(block.markdown);
          }
        });

        currentPosition += scrollStep;
      }

      // Final stay at bottom to ensure everything loads
      await smoothScrollTo(document.documentElement.scrollHeight);
      await new Promise(resolve => setTimeout(resolve, 1000));

      // One more expansion attempt
      expandCollapsedSections();
      await new Promise(resolve => setTimeout(resolve, 500));
    }

    // Fade out and remove overlay
    overlay.style.opacity = '0';
    await new Promise(resolve => setTimeout(resolve, 300));
    overlay.remove();

    // Return status and captured content
    return { cancelled, capturedContent };
  }

  // Scroll through the page first
  const scrollResult = await scrollToBottom();

  // If scrolling was cancelled, return null to indicate no download should occur
  if (scrollResult.cancelled) {
    return null;
  }

  // Combine all captured content sections
  const { capturedContent } = scrollResult;

  // Join all sections with double newlines for spacing
  const combinedMarkdown = capturedContent.join('\n\n---\n\n');

  return {
    markdown: combinedMarkdown,
    title: document.title,
    url: window.location.href,
  };
}

function sanitizeFilename(filename) {
  return filename
    .replace(/[<>:"/\\|?*]/g, '-')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .substring(0, 200);
}
```

## File: `extension-firefox/manifest.json`
```json
{
  "manifest_version": 3,
  "name": "__MSG_extensionName__",
  "version": "1.1.1",
  "description": "__MSG_extensionDescription__",
  "default_locale": "en",
  "author": "Lev Gelfenbuim",
  "homepage_url": "https://github.com/levz0r/markdown-printer",
  "permissions": ["activeTab", "contextMenus", "downloads", "scripting"],
  "background": {
    "scripts": ["background.js"]
  },
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icon16.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  },
  "browser_specific_settings": {
    "gecko": {
      "id": "markdown-printer@lev.engineer",
      "strict_min_version": "121.0",
      "data_collection_permissions": {
        "required": ["none"]
      }
    }
  }
}
```

## File: `extension-firefox/popup.html`
```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <style>
      body {
        width: 300px;
        padding: 20px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }
      h1 {
        font-size: 18px;
        margin: 0 0 15px 0;
        color: #333;
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .logo {
        width: 32px;
        height: 32px;
      }
      .version {
        font-size: 10px;
        color: #999;
        font-weight: normal;
        margin-inline-start: auto;
      }
      .copyright {
        margin-top: 15px;
        font-size: 10px;
        color: #999;
        text-align: center;
      }
      .copyright a {
        color: #666;
        text-decoration: underline;
      }
      .copyright a:hover {
        color: #2196f3;
      }
      button {
        width: 100%;
        padding: 12px;
        background: #4caf50;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
        transition: background 0.3s;
      }
      button:hover {
        background: #45a049;
      }
      button:active {
        background: #3d8b40;
      }
      button:disabled {
        background: #ccc;
        cursor: not-allowed;
      }
      .info {
        margin-top: 15px;
        font-size: 12px;
        color: #666;
        line-height: 1.5;
      }
      .badge {
        display: inline-block;
        background: #2196f3;
        color: white;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 10px;
        font-weight: bold;
        margin-bottom: 10px;
      }
    </style>
  </head>
  <body>
    <h1>
      <img src="icon48.png" alt="MD" class="logo" />
      <span id="extensionName"></span>
      <span id="version" class="version"></span>
    </h1>
    <button id="saveBtn"></button>
    <div class="copyright">
      © <a href="https://lev.engineer" target="_blank">Lev Gelfenbuim</a> 2025
    </div>
    <script src="popup.js"></script>
  </body>
</html>
```

## File: `extension-firefox/popup.js`
```javascript
// Cross-browser compatibility
const browserAPI = typeof browser !== 'undefined' ? browser : chrome;

// Set localized text on load
document.addEventListener('DOMContentLoaded', () => {
  // Set text direction for RTL languages
  const uiLanguage = browserAPI.i18n.getUILanguage();
  const rtlLanguages = ['he', 'ar', 'fa', 'ur'];
  const isRTL = rtlLanguages.some(lang => uiLanguage.startsWith(lang));

  if (isRTL) {
    document.body.dir = 'rtl';
  }

  document.getElementById('extensionName').textContent =
    browserAPI.i18n.getMessage('extensionName');
  document.getElementById('saveBtn').textContent = browserAPI.i18n.getMessage('savePageButton');

  // Display version number
  const manifest = browserAPI.runtime.getManifest();
  document.getElementById('version').textContent = `v${manifest.version}`;
});

document.getElementById('saveBtn').addEventListener('click', async () => {
  const button = document.getElementById('saveBtn');
  const originalText = browserAPI.i18n.getMessage('savePageButton');
  button.disabled = true;
  button.textContent = 'Saving...';

  try {
    await browserAPI.runtime.sendMessage({ action: 'saveAsMarkdown' });
    button.textContent = 'Saved!';
    setTimeout(() => {
      button.textContent = originalText;
      button.disabled = false;
    }, 1500);
  } catch (_error) {
    button.textContent = 'Error - Try again';
    button.disabled = false;
    setTimeout(() => {
      button.textContent = originalText;
    }, 2000);
  }
});
```

## File: `extension-firefox/turndown.js`
```javascript
var TurndownService = (function () {
  'use strict';

  function extend (destination) {
    for (var i = 1; i < arguments.length; i++) {
      var source = arguments[i];
      for (var key in source) {
        if (source.hasOwnProperty(key)) destination[key] = source[key];
      }
    }
    return destination
  }

  function repeat (character, count) {
    return Array(count + 1).join(character)
  }

  function trimLeadingNewlines (string) {
    return string.replace(/^\n*/, '')
  }

  function trimTrailingNewlines (string) {
    // avoid match-at-end regexp bottleneck, see #370
    var indexEnd = string.length;
    while (indexEnd > 0 && string[indexEnd - 1] === '\n') indexEnd--;
    return string.substring(0, indexEnd)
  }

  var blockElements = [
    'ADDRESS', 'ARTICLE', 'ASIDE', 'AUDIO', 'BLOCKQUOTE', 'BODY', 'CANVAS',
    'CENTER', 'DD', 'DIR', 'DIV', 'DL', 'DT', 'FIELDSET', 'FIGCAPTION', 'FIGURE',
    'FOOTER', 'FORM', 'FRAMESET', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'HEADER',
    'HGROUP', 'HR', 'HTML', 'ISINDEX', 'LI', 'MAIN', 'MENU', 'NAV', 'NOFRAMES',
    'NOSCRIPT', 'OL', 'OUTPUT', 'P', 'PRE', 'SECTION', 'TABLE', 'TBODY', 'TD',
    'TFOOT', 'TH', 'THEAD', 'TR', 'UL'
  ];

  function isBlock (node) {
    return is(node, blockElements)
  }

  var voidElements = [
    'AREA', 'BASE', 'BR', 'COL', 'COMMAND', 'EMBED', 'HR', 'IMG', 'INPUT',
    'KEYGEN', 'LINK', 'META', 'PARAM', 'SOURCE', 'TRACK', 'WBR'
  ];

  function isVoid (node) {
    return is(node, voidElements)
  }

  function hasVoid (node) {
    return has(node, voidElements)
  }

  var meaningfulWhenBlankElements = [
    'A', 'TABLE', 'THEAD', 'TBODY', 'TFOOT', 'TH', 'TD', 'IFRAME', 'SCRIPT',
    'AUDIO', 'VIDEO'
  ];

  function isMeaningfulWhenBlank (node) {
    return is(node, meaningfulWhenBlankElements)
  }

  function hasMeaningfulWhenBlank (node) {
    return has(node, meaningfulWhenBlankElements)
  }

  function is (node, tagNames) {
    return tagNames.indexOf(node.nodeName) >= 0
  }

  function has (node, tagNames) {
    return (
      node.getElementsByTagName &&
      tagNames.some(function (tagName) {
        return node.getElementsByTagName(tagName).length
      })
    )
  }

  var rules = {};

  rules.paragraph = {
    filter: 'p',

    replacement: function (content) {
      return '\n\n' + content + '\n\n'
    }
  };

  rules.lineBreak = {
    filter: 'br',

    replacement: function (content, node, options) {
      return options.br + '\n'
    }
  };

  rules.heading = {
    filter: ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],

    replacement: function (content, node, options) {
      var hLevel = Number(node.nodeName.charAt(1));

      if (options.headingStyle === 'setext' && hLevel < 3) {
        var underline = repeat((hLevel === 1 ? '=' : '-'), content.length);
        return (
          '\n\n' + content + '\n' + underline + '\n\n'
        )
      } else {
        return '\n\n' + repeat('#', hLevel) + ' ' + content + '\n\n'
      }
    }
  };

  rules.blockquote = {
    filter: 'blockquote',

    replacement: function (content) {
      content = content.replace(/^\n+|\n+$/g, '');
      content = content.replace(/^/gm, '> ');
      return '\n\n' + content + '\n\n'
    }
  };

  rules.list = {
    filter: ['ul', 'ol'],

    replacement: function (content, node) {
      var parent = node.parentNode;
      if (parent.nodeName === 'LI' && parent.lastElementChild === node) {
        return '\n' + content
      } else {
        return '\n\n' + content + '\n\n'
      }
    }
  };

  rules.listItem = {
    filter: 'li',

    replacement: function (content, node, options) {
      content = content
        .replace(/^\n+/, '') // remove leading newlines
        .replace(/\n+$/, '\n') // replace trailing newlines with just a single one
        .replace(/\n/gm, '\n    '); // indent
      var prefix = options.bulletListMarker + '   ';
      var parent = node.parentNode;
      if (parent.nodeName === 'OL') {
        var start = parent.getAttribute('start');
        var index = Array.prototype.indexOf.call(parent.children, node);
        prefix = (start ? Number(start) + index : index + 1) + '.  ';
      }
      return (
        prefix + content + (node.nextSibling && !/\n$/.test(content) ? '\n' : '')
      )
    }
  };

  rules.indentedCodeBlock = {
    filter: function (node, options) {
      return (
        options.codeBlockStyle === 'indented' &&
        node.nodeName === 'PRE' &&
        node.firstChild &&
        node.firstChild.nodeName === 'CODE'
      )
    },

    replacement: function (content, node, options) {
      return (
        '\n\n    ' +
        node.firstChild.textContent.replace(/\n/g, '\n    ') +
        '\n\n'
      )
    }
  };

  rules.fencedCodeBlock = {
    filter: function (node, options) {
      return (
        options.codeBlockStyle === 'fenced' &&
        node.nodeName === 'PRE' &&
        node.firstChild &&
        node.firstChild.nodeName === 'CODE'
      )
    },

    replacement: function (content, node, options) {
      var className = node.firstChild.getAttribute('class') || '';
      var language = (className.match(/language-(\S+)/) || [null, ''])[1];
      var code = node.firstChild.textContent;

      var fenceChar = options.fence.charAt(0);
      var fenceSize = 3;
      var fenceInCodeRegex = new RegExp('^' + fenceChar + '{3,}', 'gm');

      var match;
      while ((match = fenceInCodeRegex.exec(code))) {
        if (match[0].length >= fenceSize) {
          fenceSize = match[0].length + 1;
        }
      }

      var fence = repeat(fenceChar, fenceSize);

      return (
        '\n\n' + fence + language + '\n' +
        code.replace(/\n$/, '') +
        '\n' + fence + '\n\n'
      )
    }
  };

  rules.horizontalRule = {
    filter: 'hr',

    replacement: function (content, node, options) {
      return '\n\n' + options.hr + '\n\n'
    }
  };

  rules.inlineLink = {
    filter: function (node, options) {
      return (
        options.linkStyle === 'inlined' &&
        node.nodeName === 'A' &&
        node.getAttribute('href')
      )
    },

    replacement: function (content, node) {
      var href = node.getAttribute('href');
      var title = cleanAttribute(node.getAttribute('title'));
      if (title) title = ' "' + title + '"';
      return '[' + content + '](' + href + title + ')'
    }
  };

  rules.referenceLink = {
    filter: function (node, options) {
      return (
        options.linkStyle === 'referenced' &&
        node.nodeName === 'A' &&
        node.getAttribute('href')
      )
    },

    replacement: function (content, node, options) {
      var href = node.getAttribute('href');
      var title = cleanAttribute(node.getAttribute('title'));
      if (title) title = ' "' + title + '"';
      var replacement;
      var reference;

      switch (options.linkReferenceStyle) {
        case 'collapsed':
          replacement = '[' + content + '][]';
          reference = '[' + content + ']: ' + href + title;
          break
        case 'shortcut':
          replacement = '[' + content + ']';
          reference = '[' + content + ']: ' + href + title;
          break
        default:
          var id = this.references.length + 1;
          replacement = '[' + content + '][' + id + ']';
          reference = '[' + id + ']: ' + href + title;
      }

      this.references.push(reference);
      return replacement
    },

    references: [],

    append: function (options) {
      var references = '';
      if (this.references.length) {
        references = '\n\n' + this.references.join('\n') + '\n\n';
        this.references = []; // Reset references
      }
      return references
    }
  };

  rules.emphasis = {
    filter: ['em', 'i'],

    replacement: function (content, node, options) {
      if (!content.trim()) return ''
      return options.emDelimiter + content + options.emDelimiter
    }
  };

  rules.strong = {
    filter: ['strong', 'b'],

    replacement: function (content, node, options) {
      if (!content.trim()) return ''
      return options.strongDelimiter + content + options.strongDelimiter
    }
  };

  rules.code = {
    filter: function (node) {
      var hasSiblings = node.previousSibling || node.nextSibling;
      var isCodeBlock = node.parentNode.nodeName === 'PRE' && !hasSiblings;

      return node.nodeName === 'CODE' && !isCodeBlock
    },

    replacement: function (content) {
      if (!content) return ''
      content = content.replace(/\r?\n|\r/g, ' ');

      var extraSpace = /^`|^ .*?[^ ].* $|`$/.test(content) ? ' ' : '';
      var delimiter = '`';
      var matches = content.match(/`+/gm) || [];
      while (matches.indexOf(delimiter) !== -1) delimiter = delimiter + '`';

      return delimiter + extraSpace + content + extraSpace + delimiter
    }
  };

  rules.image = {
    filter: 'img',

    replacement: function (content, node) {
      var alt = cleanAttribute(node.getAttribute('alt'));
      var src = node.getAttribute('src') || '';
      var title = cleanAttribute(node.getAttribute('title'));
      var titlePart = title ? ' "' + title + '"' : '';
      return src ? '![' + alt + ']' + '(' + src + titlePart + ')' : ''
    }
  };

  function cleanAttribute (attribute) {
    return attribute ? attribute.replace(/(\n+\s*)+/g, '\n') : ''
  }

  /**
   * Manages a collection of rules used to convert HTML to Markdown
   */

  function Rules (options) {
    this.options = options;
    this._keep = [];
    this._remove = [];

    this.blankRule = {
      replacement: options.blankReplacement
    };

    this.keepReplacement = options.keepReplacement;

    this.defaultRule = {
      replacement: options.defaultReplacement
    };

    this.array = [];
    for (var key in options.rules) this.array.push(options.rules[key]);
  }

  Rules.prototype = {
    add: function (key, rule) {
      this.array.unshift(rule);
    },

    keep: function (filter) {
      this._keep.unshift({
        filter: filter,
        replacement: this.keepReplacement
      });
    },

    remove: function (filter) {
      this._remove.unshift({
        filter: filter,
        replacement: function () {
          return ''
        }
      });
    },

    forNode: function (node) {
      if (node.isBlank) return this.blankRule
      var rule;

      if ((rule = findRule(this.array, node, this.options))) return rule
      if ((rule = findRule(this._keep, node, this.options))) return rule
      if ((rule = findRule(this._remove, node, this.options))) return rule

      return this.defaultRule
    },

    forEach: function (fn) {
      for (var i = 0; i < this.array.length; i++) fn(this.array[i], i);
    }
  };

  function findRule (rules, node, options) {
    for (var i = 0; i < rules.length; i++) {
      var rule = rules[i];
      if (filterValue(rule, node, options)) return rule
    }
    return void 0
  }

  function filterValue (rule, node, options) {
    var filter = rule.filter;
    if (typeof filter === 'string') {
      if (filter === node.nodeName.toLowerCase()) return true
    } else if (Array.isArray(filter)) {
      if (filter.indexOf(node.nodeName.toLowerCase()) > -1) return true
    } else if (typeof filter === 'function') {
      if (filter.call(rule, node, options)) return true
    } else {
      throw new TypeError('`filter` needs to be a string, array, or function')
    }
  }

  /**
   * The collapseWhitespace function is adapted from collapse-whitespace
   * by Luc Thevenard.
   *
   * The MIT License (MIT)
   *
   * Copyright (c) 2014 Luc Thevenard <lucthevenard@gmail.com>
   *
   * Permission is hereby granted, free of charge, to any person obtaining a copy
   * of this software and associated documentation files (the "Software"), to deal
   * in the Software without restriction, including without limitation the rights
   * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   * copies of the Software, and to permit persons to whom the Software is
   * furnished to do so, subject to the following conditions:
   *
   * The above copyright notice and this permission notice shall be included in
   * all copies or substantial portions of the Software.
   *
   * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   * THE SOFTWARE.
   */

  /**
   * collapseWhitespace(options) removes extraneous whitespace from an the given element.
   *
   * @param {Object} options
   */
  function collapseWhitespace (options) {
    var element = options.element;
    var isBlock = options.isBlock;
    var isVoid = options.isVoid;
    var isPre = options.isPre || function (node) {
      return node.nodeName === 'PRE'
    };

    if (!element.firstChild || isPre(element)) return

    var prevText = null;
    var keepLeadingWs = false;

    var prev = null;
    var node = next(prev, element, isPre);

    while (node !== element) {
      if (node.nodeType === 3 || node.nodeType === 4) { // Node.TEXT_NODE or Node.CDATA_SECTION_NODE
        var text = node.data.replace(/[ \r\n\t]+/g, ' ');

        if ((!prevText || / $/.test(prevText.data)) &&
            !keepLeadingWs && text[0] === ' ') {
          text = text.substr(1);
        }

        // `text` might be empty at this point.
        if (!text) {
          node = remove(node);
          continue
        }

        node.data = text;

        prevText = node;
      } else if (node.nodeType === 1) { // Node.ELEMENT_NODE
        if (isBlock(node) || node.nodeName === 'BR') {
          if (prevText) {
            prevText.data = prevText.data.replace(/ $/, '');
          }

          prevText = null;
          keepLeadingWs = false;
        } else if (isVoid(node) || isPre(node)) {
          // Avoid trimming space around non-block, non-BR void elements and inline PRE.
          prevText = null;
          keepLeadingWs = true;
        } else if (prevText) {
          // Drop protection if set previously.
          keepLeadingWs = false;
        }
      } else {
        node = remove(node);
        continue
      }

      var nextNode = next(prev, node, isPre);
      prev = node;
      node = nextNode;
    }

    if (prevText) {
      prevText.data = prevText.data.replace(/ $/, '');
      if (!prevText.data) {
        remove(prevText);
      }
    }
  }

  /**
   * remove(node) removes the given node from the DOM and returns the
   * next node in the sequence.
   *
   * @param {Node} node
   * @return {Node} node
   */
  function remove (node) {
    var next = node.nextSibling || node.parentNode;

    node.parentNode.removeChild(node);

    return next
  }

  /**
   * next(prev, current, isPre) returns the next node in the sequence, given the
   * current and previous nodes.
   *
   * @param {Node} prev
   * @param {Node} current
   * @param {Function} isPre
   * @return {Node}
   */
  function next (prev, current, isPre) {
    if ((prev && prev.parentNode === current) || isPre(current)) {
      return current.nextSibling || current.parentNode
    }

    return current.firstChild || current.nextSibling || current.parentNode
  }

  /*
   * Set up window for Node.js
   */

  var root = (typeof window !== 'undefined' ? window : {});

  /*
   * Parsing HTML strings
   */

  function canParseHTMLNatively () {
    var Parser = root.DOMParser;
    var canParse = false;

    // Adapted from https://gist.github.com/1129031
    // Firefox/Opera/IE throw errors on unsupported types
    try {
      // WebKit returns null on unsupported types
      if (new Parser().parseFromString('', 'text/html')) {
        canParse = true;
      }
    } catch (e) {}

    return canParse
  }

  function createHTMLParser () {
    var Parser = function () {};

    {
      if (shouldUseActiveX()) {
        Parser.prototype.parseFromString = function (string) {
          var doc = new window.ActiveXObject('htmlfile');
          doc.designMode = 'on'; // disable on-page scripts
          doc.open();
          doc.write(string);
          doc.close();
          return doc
        };
      } else {
        Parser.prototype.parseFromString = function (string) {
          var doc = document.implementation.createHTMLDocument('');
          doc.open();
          doc.write(string);
          doc.close();
          return doc
        };
      }
    }
    return Parser
  }

  function shouldUseActiveX () {
    var useActiveX = false;
    try {
      document.implementation.createHTMLDocument('').open();
    } catch (e) {
      if (window.ActiveXObject) useActiveX = true;
    }
    return useActiveX
  }

  var HTMLParser = canParseHTMLNatively() ? root.DOMParser : createHTMLParser();

  function RootNode (input, options) {
    var root;
    if (typeof input === 'string') {
      var doc = htmlParser().parseFromString(
        // DOM parsers arrange elements in the <head> and <body>.
        // Wrapping in a custom element ensures elements are reliably arranged in
        // a single element.
        '<x-turndown id="turndown-root">' + input + '</x-turndown>',
        'text/html'
      );
      root = doc.getElementById('turndown-root');
    } else {
      root = input.cloneNode(true);
    }
    collapseWhitespace({
      element: root,
      isBlock: isBlock,
      isVoid: isVoid,
      isPre: options.preformattedCode ? isPreOrCode : null
    });

    return root
  }

  var _htmlParser;
  function htmlParser () {
    _htmlParser = _htmlParser || new HTMLParser();
    return _htmlParser
  }

  function isPreOrCode (node) {
    return node.nodeName === 'PRE' || node.nodeName === 'CODE'
  }

  function Node (node, options) {
    node.isBlock = isBlock(node);
    node.isCode = node.nodeName === 'CODE' || node.parentNode.isCode;
    node.isBlank = isBlank(node);
    node.flankingWhitespace = flankingWhitespace(node, options);
    return node
  }

  function isBlank (node) {
    return (
      !isVoid(node) &&
      !isMeaningfulWhenBlank(node) &&
      /^\s*$/i.test(node.textContent) &&
      !hasVoid(node) &&
      !hasMeaningfulWhenBlank(node)
    )
  }

  function flankingWhitespace (node, options) {
    if (node.isBlock || (options.preformattedCode && node.isCode)) {
      return { leading: '', trailing: '' }
    }

    var edges = edgeWhitespace(node.textContent);

    // abandon leading ASCII WS if left-flanked by ASCII WS
    if (edges.leadingAscii && isFlankedByWhitespace('left', node, options)) {
      edges.leading = edges.leadingNonAscii;
    }

    // abandon trailing ASCII WS if right-flanked by ASCII WS
    if (edges.trailingAscii && isFlankedByWhitespace('right', node, options)) {
      edges.trailing = edges.trailingNonAscii;
    }

    return { leading: edges.leading, trailing: edges.trailing }
  }

  function edgeWhitespace (string) {
    var m = string.match(/^(([ \t\r\n]*)(\s*))(?:(?=\S)[\s\S]*\S)?((\s*?)([ \t\r\n]*))$/);
    return {
      leading: m[1], // whole string for whitespace-only strings
      leadingAscii: m[2],
      leadingNonAscii: m[3],
      trailing: m[4], // empty for whitespace-only strings
      trailingNonAscii: m[5],
      trailingAscii: m[6]
    }
  }

  function isFlankedByWhitespace (side, node, options) {
    var sibling;
    var regExp;
    var isFlanked;

    if (side === 'left') {
      sibling = node.previousSibling;
      regExp = / $/;
    } else {
      sibling = node.nextSibling;
      regExp = /^ /;
    }

    if (sibling) {
      if (sibling.nodeType === 3) {
        isFlanked = regExp.test(sibling.nodeValue);
      } else if (options.preformattedCode && sibling.nodeName === 'CODE') {
        isFlanked = false;
      } else if (sibling.nodeType === 1 && !isBlock(sibling)) {
        isFlanked = regExp.test(sibling.textContent);
      }
    }
    return isFlanked
  }

  var reduce = Array.prototype.reduce;
  var escapes = [
    [/\\/g, '\\\\'],
    [/\*/g, '\\*'],
    [/^-/g, '\\-'],
    [/^\+ /g, '\\+ '],
    [/^(=+)/g, '\\$1'],
    [/^(#{1,6}) /g, '\\$1 '],
    [/`/g, '\\`'],
    [/^~~~/g, '\\~~~'],
    [/\[/g, '\\['],
    [/\]/g, '\\]'],
    [/^>/g, '\\>'],
    [/_/g, '\\_'],
    [/^(\d+)\. /g, '$1\\. ']
  ];

  function TurndownService (options) {
    if (!(this instanceof TurndownService)) return new TurndownService(options)

    var defaults = {
      rules: rules,
      headingStyle: 'setext',
      hr: '* * *',
      bulletListMarker: '*',
      codeBlockStyle: 'indented',
      fence: '```',
      emDelimiter: '_',
      strongDelimiter: '**',
      linkStyle: 'inlined',
      linkReferenceStyle: 'full',
      br: '  ',
      preformattedCode: false,
      blankReplacement: function (content, node) {
        return node.isBlock ? '\n\n' : ''
      },
      keepReplacement: function (content, node) {
        return node.isBlock ? '\n\n' + node.outerHTML + '\n\n' : node.outerHTML
      },
      defaultReplacement: function (content, node) {
        return node.isBlock ? '\n\n' + content + '\n\n' : content
      }
    };
    this.options = extend({}, defaults, options);
    this.rules = new Rules(this.options);
  }

  TurndownService.prototype = {
    /**
     * The entry point for converting a string or DOM node to Markdown
     * @public
     * @param {String|HTMLElement} input The string or DOM node to convert
     * @returns A Markdown representation of the input
     * @type String
     */

    turndown: function (input) {
      if (!canConvert(input)) {
        throw new TypeError(
          input + ' is not a string, or an element/document/fragment node.'
        )
      }

      if (input === '') return ''

      var output = process.call(this, new RootNode(input, this.options));
      return postProcess.call(this, output)
    },

    /**
     * Add one or more plugins
     * @public
     * @param {Function|Array} plugin The plugin or array of plugins to add
     * @returns The Turndown instance for chaining
     * @type Object
     */

    use: function (plugin) {
      if (Array.isArray(plugin)) {
        for (var i = 0; i < plugin.length; i++) this.use(plugin[i]);
      } else if (typeof plugin === 'function') {
        plugin(this);
      } else {
        throw new TypeError('plugin must be a Function or an Array of Functions')
      }
      return this
    },

    /**
     * Adds a rule
     * @public
     * @param {String} key The unique key of the rule
     * @param {Object} rule The rule
     * @returns The Turndown instance for chaining
     * @type Object
     */

    addRule: function (key, rule) {
      this.rules.add(key, rule);
      return this
    },

    /**
     * Keep a node (as HTML) that matches the filter
     * @public
     * @param {String|Array|Function} filter The unique key of the rule
     * @returns The Turndown instance for chaining
     * @type Object
     */

    keep: function (filter) {
      this.rules.keep(filter);
      return this
    },

    /**
     * Remove a node that matches the filter
     * @public
     * @param {String|Array|Function} filter The unique key of the rule
     * @returns The Turndown instance for chaining
     * @type Object
     */

    remove: function (filter) {
      this.rules.remove(filter);
      return this
    },

    /**
     * Escapes Markdown syntax
     * @public
     * @param {String} string The string to escape
     * @returns A string with Markdown syntax escaped
     * @type String
     */

    escape: function (string) {
      return escapes.reduce(function (accumulator, escape) {
        return accumulator.replace(escape[0], escape[1])
      }, string)
    }
  };

  /**
   * Reduces a DOM node down to its Markdown string equivalent
   * @private
   * @param {HTMLElement} parentNode The node to convert
   * @returns A Markdown representation of the node
   * @type String
   */

  function process (parentNode) {
    var self = this;
    return reduce.call(parentNode.childNodes, function (output, node) {
      node = new Node(node, self.options);

      var replacement = '';
      if (node.nodeType === 3) {
        replacement = node.isCode ? node.nodeValue : self.escape(node.nodeValue);
      } else if (node.nodeType === 1) {
        replacement = replacementForNode.call(self, node);
      }

      return join(output, replacement)
    }, '')
  }

  /**
   * Appends strings as each rule requires and trims the output
   * @private
   * @param {String} output The conversion output
   * @returns A trimmed version of the ouput
   * @type String
   */

  function postProcess (output) {
    var self = this;
    this.rules.forEach(function (rule) {
      if (typeof rule.append === 'function') {
        output = join(output, rule.append(self.options));
      }
    });

    return output.replace(/^[\t\r\n]+/, '').replace(/[\t\r\n\s]+$/, '')
  }

  /**
   * Converts an element node to its Markdown equivalent
   * @private
   * @param {HTMLElement} node The node to convert
   * @returns A Markdown representation of the node
   * @type String
   */

  function replacementForNode (node) {
    var rule = this.rules.forNode(node);
    var content = process.call(this, node);
    var whitespace = node.flankingWhitespace;
    if (whitespace.leading || whitespace.trailing) content = content.trim();
    return (
      whitespace.leading +
      rule.replacement(content, node, this.options) +
      whitespace.trailing
    )
  }

  /**
   * Joins replacement to the current output with appropriate number of new lines
   * @private
   * @param {String} output The current conversion output
   * @param {String} replacement The string to append to the output
   * @returns Joined output
   * @type String
   */

  function join (output, replacement) {
    var s1 = trimTrailingNewlines(output);
    var s2 = trimLeadingNewlines(replacement);
    var nls = Math.max(output.length - s1.length, replacement.length - s2.length);
    var separator = '\n\n'.substring(0, nls);

    return s1 + separator + s2
  }

  /**
   * Determines whether an input can be converted
   * @private
   * @param {String|HTMLElement} input Describe this parameter
   * @returns Describe what it returns
   * @type String|Object|Array|Boolean|Number
   */

  function canConvert (input) {
    return (
      input != null && (
        typeof input === 'string' ||
        (input.nodeType && (
          input.nodeType === 1 || input.nodeType === 9 || input.nodeType === 11
        ))
      )
    )
  }

  return TurndownService;

}());
```

## File: `extension-firefox/_locales/en/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "Save web pages as Markdown files to your Downloads folder. No setup required!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "Save Page as Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Save as Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `extension-firefox/_locales/fr/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "Enregistrez des pages web en tant que fichiers Markdown dans votre dossier Téléchargements. Aucune configuration requise !",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "Enregistrer la page en Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Enregistrer en Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `extension-firefox/_locales/he/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "שמור דפי אינטרנט כקבצי Markdown לתיקיית ההורדות. ללא הגדרות נדרשות!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "שמור דף כ-Markdown",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "שמור כ-Markdown",
    "description": "Context menu item title"
  }
}
```

## File: `extension-firefox/_locales/hi/messages.json`
```json
{
  "extensionName": {
    "message": "Markdown Printer",
    "description": "Name of the extension"
  },
  "extensionDescription": {
    "message": "वेब पेजों को Markdown फ़ाइलों के रूप में अपने डाउनलोड फ़ोल्डर में सहेजें। किसी सेटअप की आवश्यकता नहीं!",
    "description": "Description of the extension"
  },
  "savePageButton": {
    "message": "पेज को Markdown के रूप में सहेजें",
    "description": "Button text in popup"
  },
  "contextMenuTitle": {
    "message": "Markdown के रूप में सहेजें",
    "description": "Context menu item title"
  }
}
```

## File: `extension-pro/README.md`
```markdown
# Markdown Printer - Pro Version

Advanced version with custom save locations, auto-open files, and persistent settings.

## ✨ Pro Features

- ✅ **Custom save location** - Set a default folder, no dialog every time
- ✅ **Auto-open files** - Automatically open saved files in your default editor
- ✅ **Folder browser** - Native folder picker to choose save location
- ✅ **Persistent settings** - Saves your preferences

## ⚠️ Trade-offs

- ❌ Requires additional setup (native messaging host)
- ❌ Cannot be published to Chrome Web Store easily
- ❌ Users must manually install and configure

## 📦 Installation

### Prerequisites

- Google Chrome
- Node.js (v14 or higher)
- **Platform**: Windows, macOS, or Linux

### Windows

1. Clone or download this repository

2. Run the installation script:

   ```cmd
   install.bat
   ```

3. Load the Chrome extension:
   - Open Chrome and navigate to `chrome://extensions/`
   - Enable "Developer mode" in the top right
   - Click "Load unpacked"
   - Select the `extension-pro/` directory

4. Update the native messaging manifest:
   - Copy the Extension ID from the Chrome extensions page
   - Open the manifest file at:
     `%LOCALAPPDATA%\Google\Chrome\NativeMessagingHosts\com.markdownprinter.host.json`
   - Replace `EXTENSION_ID_PLACEHOLDER` with your actual extension ID

### macOS / Linux

1. Clone or download this repository

2. Run the installation script:

   ```bash
   ./install.sh
   ```

3. Load the Chrome extension:
   - Open Chrome and navigate to `chrome://extensions/`
   - Enable "Developer mode" in the top right
   - Click "Load unpacked"
   - Select the `extension-pro/` directory

4. Update the native messaging manifest:
   - Copy the Extension ID from the Chrome extensions page
   - Open the manifest file:
     - **macOS**: `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.markdownprinter.host.json`
     - **Linux**: `~/.config/google-chrome/NativeMessagingHosts/com.markdownprinter.host.json`
   - Replace `EXTENSION_ID_PLACEHOLDER` with your actual extension ID

5. Reload the extension in Chrome

## ⚙️ Configuration

Right-click the extension icon → "Options" to configure:

1. **Save Location** - Browse and select a default folder
2. **Open After Save** - Toggle to auto-open files in your default editor

## 📖 Usage

Same as the standard version, but files save to your configured location without showing a dialog each time.

## 🔙 Want Simpler?

If the setup is too complex, try the [Standard Version](../../../README.md) - no setup required!
```

## File: `extension-pro/background.js`
```javascript
// Create context menu on installation
chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed, creating context menu');
  chrome.contextMenus.create({
    id: 'saveAsMarkdown',
    title: 'Save as Markdown',
    contexts: ['page'],
  });
});

// Handle context menu click
chrome.contextMenus.onClicked.addListener((info, tab) => {
  console.log('Context menu clicked:', info.menuItemId);
  if (info.menuItemId === 'saveAsMarkdown') {
    savePageAsMarkdown(tab.id);
  }
});

// Handle messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'saveAsMarkdown') {
    chrome.tabs.query({ active: true, currentWindow: true }, async tabs => {
      if (tabs[0]) {
        try {
          await savePageAsMarkdown(tabs[0].id);
          sendResponse({ success: true });
        } catch (error) {
          sendResponse({ success: false, error: error.message });
        }
      }
    });
    return true; // Keep the message channel open for async response
  }
});

async function savePageAsMarkdown(tabId) {
  try {
    console.log('savePageAsMarkdown called for tab:', tabId);

    // Load settings
    const settings = await chrome.storage.sync.get({
      savePath: '',
      openAfterSave: false,
    });
    console.log('Settings loaded:', settings);

    // Inject script to get page content
    const results = await chrome.scripting.executeScript({
      target: { tabId: tabId },
      func: extractPageContent,
    });

    if (!results || !results[0]) {
      console.error('Failed to extract page content');
      return;
    }

    const { html, title, url } = results[0].result;
    console.log('Extracted content:', { title, url, htmlLength: html.length });

    // Send to native host
    console.log('Sending message to native host...');
    const response = await chrome.runtime.sendNativeMessage('com.markdownprinter.host', {
      command: 'save',
      html: html,
      title: title,
      url: url,
      saveDir: settings.savePath || '',
      openAfterSave: settings.openAfterSave,
    });
    console.log('Native host response:', response);

    if (response.success) {
      console.log('Saved to:', response.filepath);
      // Show notification
      chrome.notifications.create({
        type: 'basic',
        iconUrl: chrome.runtime.getURL('icon48.png'),
        title: 'Markdown Printer',
        message: `Saved to: ${response.filepath}`,
      });
    } else {
      console.error('Save failed:', response.error);
      chrome.notifications.create({
        type: 'basic',
        iconUrl: chrome.runtime.getURL('icon48.png'),
        title: 'Markdown Printer Error',
        message: `Failed to save: ${response.error}`,
      });
    }
  } catch (error) {
    console.error('Error:', error);
    chrome.notifications.create({
      type: 'basic',
      iconUrl: chrome.runtime.getURL('icon48.png'),
      title: 'Markdown Printer Error',
      message: `Error: ${error.message}`,
    });
  }
}

// This function runs in the page context
function extractPageContent() {
  // Try to get the main content area, fall back to body
  const article =
    document.querySelector('article') ||
    document.querySelector('[role="main"]') ||
    document.querySelector('main') ||
    document.body;

  return {
    html: article.innerHTML,
    title: document.title,
    url: window.location.href,
  };
}
```

## File: `extension-pro/manifest.json`
```json
{
  "manifest_version": 3,
  "name": "Markdown Printer",
  "version": "1.0.0",
  "description": "Save web pages as Markdown files with preserved formatting. Perfect for documentation, articles, and note-taking.",
  "author": "Lev Gelfenbuim",
  "homepage_url": "https://github.com/levz0r/markdown-printer",
  "permissions": [
    "activeTab",
    "contextMenus",
    "nativeMessaging",
    "scripting",
    "notifications",
    "storage"
  ],
  "host_permissions": ["<all_urls>"],
  "background": {
    "service_worker": "background.js"
  },
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icon16.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  },
  "options_page": "options.html",
  "web_accessible_resources": [
    {
      "resources": ["icon48.png"],
      "matches": ["<all_urls>"]
    }
  ]
}
```

## File: `extension-pro/options.html`
```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Markdown Printer Settings</title>
    <style>
      body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        padding: 20px;
        max-width: 600px;
        margin: 0 auto;
      }
      h1 {
        font-size: 24px;
        margin-bottom: 20px;
        color: #333;
      }
      .setting {
        margin-bottom: 20px;
        padding: 15px;
        background: #f5f5f5;
        border-radius: 4px;
      }
      label {
        display: block;
        font-weight: 500;
        margin-bottom: 8px;
        color: #555;
      }
      input[type='text'] {
        width: 100%;
        padding: 8px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 14px;
        box-sizing: border-box;
      }
      input[type='checkbox'] {
        margin-right: 8px;
        width: 18px;
        height: 18px;
        vertical-align: middle;
      }
      .checkbox-label {
        display: inline-block;
        vertical-align: middle;
        font-weight: normal;
        cursor: pointer;
      }
      .description {
        font-size: 12px;
        color: #666;
        margin-top: 5px;
      }
      .button-container {
        margin-top: 30px;
        display: flex;
        gap: 10px;
      }
      button {
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
        transition: background 0.3s;
      }
      #saveBtn {
        background: #4caf50;
        color: white;
      }
      #saveBtn:hover {
        background: #45a049;
      }
      #resetBtn {
        background: #f44336;
        color: white;
      }
      #resetBtn:hover {
        background: #da190b;
      }
      .status {
        margin-top: 15px;
        padding: 10px;
        border-radius: 4px;
        display: none;
      }
      .status.success {
        background: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
      }
      .status.error {
        background: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
      }
    </style>
  </head>
  <body>
    <h1>Markdown Printer Settings</h1>

    <div class="setting">
      <label for="savePath">Save Location</label>
      <div style="display: flex; gap: 10px">
        <input type="text" id="savePath" placeholder="~/MarkdownPrints" style="flex: 1" />
        <button id="browseBtn" style="padding: 8px 16px; white-space: nowrap">Browse...</button>
      </div>
      <div class="description">
        Full path where markdown files will be saved. Use ~ for home directory. Leave empty to use
        default: ~/MarkdownPrints
      </div>
    </div>

    <div class="setting">
      <label>
        <input type="checkbox" id="openAfterSave" />
        <span class="checkbox-label">Open file after saving</span>
      </label>
      <div class="description">
        Automatically open the markdown file in your default editor after creation.
      </div>
    </div>

    <div class="button-container">
      <button id="saveBtn">Save Settings</button>
      <button id="resetBtn">Reset to Defaults</button>
    </div>

    <div id="status" class="status"></div>

    <script src="options.js"></script>
  </body>
</html>
```

## File: `extension-pro/options.js`
```javascript
// Default settings
const DEFAULT_SETTINGS = {
  savePath: '',
  openAfterSave: false,
};

// Load settings when page opens
document.addEventListener('DOMContentLoaded', async () => {
  const settings = await loadSettings();
  document.getElementById('savePath').value = settings.savePath || '';
  document.getElementById('openAfterSave').checked = settings.openAfterSave;
});

// Browse for folder
document.getElementById('browseBtn').addEventListener('click', async () => {
  try {
    const response = await chrome.runtime.sendNativeMessage('com.markdownprinter.host', {
      command: 'browsefolder',
    });

    if (response.success && response.path) {
      document.getElementById('savePath').value = response.path;
    } else if (response.error) {
      showStatus('Error selecting folder: ' + response.error, 'error');
    }
  } catch (error) {
    showStatus('Error opening folder browser: ' + error.message, 'error');
  }
});

// Save settings
document.getElementById('saveBtn').addEventListener('click', async () => {
  const settings = {
    savePath: document.getElementById('savePath').value.trim(),
    openAfterSave: document.getElementById('openAfterSave').checked,
  };

  try {
    await chrome.storage.sync.set(settings);
    showStatus('Settings saved successfully!', 'success');
  } catch (error) {
    showStatus('Error saving settings: ' + error.message, 'error');
  }
});

// Reset to defaults
document.getElementById('resetBtn').addEventListener('click', async () => {
  try {
    await chrome.storage.sync.set(DEFAULT_SETTINGS);
    document.getElementById('savePath').value = '';
    document.getElementById('openAfterSave').checked = false;
    showStatus('Settings reset to defaults!', 'success');
  } catch (error) {
    showStatus('Error resetting settings: ' + error.message, 'error');
  }
});

// Helper functions
async function loadSettings() {
  try {
    const settings = await chrome.storage.sync.get(DEFAULT_SETTINGS);
    return settings;
  } catch (error) {
    console.error('Error loading settings:', error);
    return DEFAULT_SETTINGS;
  }
}

function showStatus(message, type) {
  const statusDiv = document.getElementById('status');
  statusDiv.textContent = message;
  statusDiv.className = `status ${type}`;
  statusDiv.style.display = 'block';

  setTimeout(() => {
    statusDiv.style.display = 'none';
  }, 3000);
}
```

## File: `extension-pro/popup.html`
```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <style>
      body {
        width: 300px;
        padding: 20px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }
      h1 {
        font-size: 18px;
        margin: 0 0 15px 0;
        color: #333;
      }
      button {
        width: 100%;
        padding: 12px;
        background: #4caf50;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
        transition: background 0.3s;
      }
      button:hover {
        background: #45a049;
      }
      button:active {
        background: #3d8b40;
      }
      .info {
        margin-top: 15px;
        font-size: 12px;
        color: #666;
        line-height: 1.5;
      }
    </style>
  </head>
  <body>
    <h1>Markdown Printer</h1>
    <button id="saveBtn">Save Page as Markdown</button>
    <div class="info" id="infoText">
      Click to save the current page as a Markdown file in ~/MarkdownPrints/
    </div>
    <script src="popup.js"></script>
  </body>
</html>
```

## File: `extension-pro/popup.js`
```javascript
// Load and display current save path
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const settings = await chrome.storage.sync.get({
      savePath: '',
      openAfterSave: false,
    });

    const savePath = settings.savePath || '~/MarkdownPrints/';
    const infoText = document.getElementById('infoText');

    if (settings.openAfterSave) {
      infoText.textContent = `Saves to ${savePath} and opens the file automatically`;
    } else {
      infoText.textContent = `Saves to ${savePath}`;
    }
  } catch (error) {
    console.error('Error loading settings:', error);
  }
});

document.getElementById('saveBtn').addEventListener('click', async () => {
  const button = document.getElementById('saveBtn');
  button.disabled = true;
  button.textContent = 'Saving...';

  try {
    await chrome.runtime.sendMessage({ action: 'saveAsMarkdown' });
    button.textContent = 'Saved!';
    setTimeout(() => window.close(), 500);
  } catch (error) {
    button.textContent = 'Error - Try again';
    button.disabled = false;
  }
});
```

## File: `native-host/host-wrapper.bat`
```
@echo off
REM This wrapper ensures Node.js can be found on Windows
REM regardless of installation method (nvm-windows, official installer, etc.)

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

REM Try to find Node.js in common Windows locations
where node >nul 2>&1
if %ERRORLEVEL% equ 0 (
    REM Node is in PATH
    node "%SCRIPT_DIR%host.js"
    exit /b %ERRORLEVEL%
)

REM Check Program Files (64-bit)
if exist "C:\Program Files\nodejs\node.exe" (
    "C:\Program Files\nodejs\node.exe" "%SCRIPT_DIR%host.js"
    exit /b %ERRORLEVEL%
)

REM Check Program Files (x86)
if exist "C:\Program Files (x86)\nodejs\node.exe" (
    "C:\Program Files (x86)\nodejs\node.exe" "%SCRIPT_DIR%host.js"
    exit /b %ERRORLEVEL%
)

REM Check nvm-windows default location
if exist "%APPDATA%\nvm" (
    for /f "delims=" %%i in ('dir /b /o-d "%APPDATA%\nvm\v*" 2^>nul') do (
        if exist "%APPDATA%\nvm\%%i\node.exe" (
            "%APPDATA%\nvm\%%i\node.exe" "%SCRIPT_DIR%host.js"
            exit /b %ERRORLEVEL%
        )
    )
)

REM If we get here, Node.js was not found
echo Error: Node.js not found. Please ensure Node.js is installed and in your PATH.
exit /b 1
```

## File: `native-host/host-wrapper.sh`
```bash
#!/bin/bash

# This wrapper ensures Node.js can be found regardless of installation method
# (nvm, Homebrew, system install, etc.)

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Try to find Node.js in common locations
if command -v node &> /dev/null; then
    # Node is in PATH
    NODE_PATH="$(command -v node)"
elif [ -f "$HOME/.nvm/nvm.sh" ]; then
    # Load nvm if available
    source "$HOME/.nvm/nvm.sh"
    NODE_PATH="$(command -v node)"
elif [ -f "/usr/local/bin/node" ]; then
    # Homebrew or manual install
    NODE_PATH="/usr/local/bin/node"
elif [ -f "/opt/homebrew/bin/node" ]; then
    # Apple Silicon Homebrew
    NODE_PATH="/opt/homebrew/bin/node"
elif [ -f "/usr/bin/node" ]; then
    # System install
    NODE_PATH="/usr/bin/node"
else
    # Fallback - try to execute node directly
    NODE_PATH="node"
fi

# Execute host.js with the found Node.js
exec "$NODE_PATH" "$SCRIPT_DIR/host.js"
```

## File: `native-host/host.js`
```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');
const TurndownService = require('turndown');

// Native messaging uses stdin/stdout for communication
// Messages are length-prefixed (4 bytes, native byte order) followed by JSON

// Log errors to file for debugging
const logFile = path.join(os.homedir(), 'markdown-printer-debug.log');
function logError(message) {
  const timestamp = new Date().toISOString();
  fs.appendFileSync(logFile, `[${timestamp}] ${message}\n`);
}

function readMessage() {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let totalLength = 0;
    let headerReceived = false;
    let messageLength = 0;

    const onReadable = () => {
      let chunk;

      while ((chunk = process.stdin.read()) !== null) {
        chunks.push(chunk);
        totalLength += chunk.length;

        if (!headerReceived && totalLength >= 4) {
          const header = Buffer.concat(chunks);
          messageLength = header.readUInt32LE(0);
          headerReceived = true;
        }

        if (headerReceived && totalLength >= messageLength + 4) {
          process.stdin.removeListener('readable', onReadable);
          process.stdin.removeListener('end', onEnd);
          const fullMessage = Buffer.concat(chunks);
          const messageBytes = fullMessage.slice(4, 4 + messageLength);
          const message = JSON.parse(messageBytes.toString('utf8'));
          resolve(message);
          return;
        }
      }
    };

    const onEnd = () => {
      process.stdin.removeListener('readable', onReadable);
      process.stdin.removeListener('end', onEnd);
      reject(new Error('stdin closed'));
    };

    process.stdin.on('readable', onReadable);
    process.stdin.on('end', onEnd);
  });
}

function sendMessage(message) {
  const buffer = Buffer.from(JSON.stringify(message));
  const header = Buffer.alloc(4);
  header.writeUInt32LE(buffer.length, 0);

  process.stdout.write(header);
  process.stdout.write(buffer);
}

function sanitizeFilename(filename) {
  return filename
    .replace(/[<>:"/\\|?*]/g, '-')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .substring(0, 200);
}

async function browseFolder() {
  return new Promise(resolve => {
    const { exec } = require('child_process');

    if (process.platform === 'darwin') {
      // macOS - use osascript to show folder picker
      const script =
        'osascript -e "POSIX path of (choose folder with prompt \\"Select folder for markdown files:\\")"';
      exec(script, (error, stdout, stderr) => {
        if (error) {
          if (error.code === 1) {
            // User cancelled
            resolve({ success: false, cancelled: true });
          } else {
            resolve({ success: false, error: stderr || error.message });
          }
        } else {
          const path = stdout.trim();
          resolve({ success: true, path });
        }
      });
    } else if (process.platform === 'linux') {
      // Linux - use zenity
      exec(
        'zenity --file-selection --directory --title="Select folder for markdown files"',
        (error, stdout, stderr) => {
          if (error) {
            if (error.code === 1) {
              resolve({ success: false, cancelled: true });
            } else {
              resolve({ success: false, error: 'Please install zenity for folder selection' });
            }
          } else {
            const path = stdout.trim();
            resolve({ success: true, path });
          }
        }
      );
    } else {
      resolve({ success: false, error: 'Folder selection not supported on this platform' });
    }
  });
}

async function saveMarkdown(html, title, url, saveDir, openAfterSave) {
  try {
    // Convert HTML to Markdown
    const turndownService = new TurndownService({
      headingStyle: 'atx',
      codeBlockStyle: 'fenced',
      bulletListMarker: '-',
    });

    const markdown = turndownService.turndown(html);

    // Generate filename
    const timestamp = new Date().toISOString().split('T')[0];
    const sanitizedTitle = sanitizeFilename(title || 'untitled');
    const filename = `${sanitizedTitle}-${timestamp}.md`;

    // Determine save location (expand ~ if present)
    let outputDir = saveDir || path.join(os.homedir(), 'MarkdownPrints');
    if (outputDir.startsWith('~')) {
      outputDir = path.join(os.homedir(), outputDir.slice(1));
    }

    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    const filepath = path.join(outputDir, filename);

    // Add metadata header
    const content = `# ${title}\n\n**Source:** ${url}\n**Saved:** ${new Date().toISOString()}\n\n---\n\n${markdown}`;

    // Write file
    fs.writeFileSync(filepath, content, 'utf8');

    // Open file if requested
    if (openAfterSave) {
      const { exec } = require('child_process');
      const openCommand =
        process.platform === 'darwin'
          ? 'open'
          : process.platform === 'win32'
            ? 'start'
            : 'xdg-open';
      exec(`${openCommand} "${filepath}"`);
    }

    return { success: true, filepath };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

async function main() {
  try {
    logError('Native host started');
    const message = await readMessage();
    logError(`Message received: command=${message.command}, htmlLength=${message.html?.length}`);

    if (message.command === 'save') {
      const result = await saveMarkdown(
        message.html,
        message.title,
        message.url,
        message.saveDir,
        message.openAfterSave
      );
      logError(`Save result: ${JSON.stringify(result)}`);
      sendMessage(result);
    } else if (message.command === 'browsefolder') {
      const result = await browseFolder();
      sendMessage(result);
    } else {
      sendMessage({ success: false, error: 'Unknown command' });
    }

    process.exit(0);
  } catch (error) {
    logError(`Error in main: ${error.message}\n${error.stack}`);
    sendMessage({ success: false, error: error.message });
    process.exit(1);
  }
}

main();
```

## File: `native-host/host.json`
```json
{
  "name": "com.markdownprinter.host",
  "description": "Markdown Printer Native Host",
  "path": "HOST_PATH_PLACEHOLDER",
  "type": "stdio",
  "allowed_origins": ["chrome-extension://EXTENSION_ID_PLACEHOLDER/"]
}
```

## File: `native-host/package.json`
```json
{
  "name": "markdown-printer-host",
  "version": "1.0.0",
  "description": "Native messaging host for Markdown Printer Chrome extension",
  "main": "host.js",
  "scripts": {
    "test": "node host.js"
  },
  "keywords": [
    "chrome",
    "native-messaging",
    "markdown"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "turndown": "^7.1.2"
  }
}
```

## File: `src/background.js`
```javascript
// Cross-browser compatibility
const browserAPI = typeof browser !== 'undefined' ? browser : chrome;

// Create context menu on installation
browserAPI.runtime.onInstalled.addListener(() => {
  browserAPI.contextMenus.create({
    id: 'saveAsMarkdown',
    title: browserAPI.i18n.getMessage('contextMenuTitle'),
    contexts: ['page'],
  });
});

// Handle context menu click
browserAPI.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === 'saveAsMarkdown') {
    savePageAsMarkdown(tab.id);
  }
});

// Handle messages from popup
browserAPI.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'saveAsMarkdown') {
    browserAPI.tabs.query({ active: true, currentWindow: true }, async tabs => {
      if (tabs[0]) {
        try {
          await savePageAsMarkdown(tabs[0].id);
          sendResponse({ success: true });
        } catch (error) {
          sendResponse({ success: false, error: error.message });
        }
      }
    });
    return true; // Keep the message channel open for async response
  }
});

async function savePageAsMarkdown(tabId) {
  try {
    // Inject Turndown library and conversion script
    await browserAPI.scripting
      .executeScript({
        target: { tabId: tabId },
        files: ['turndown.js'],
      })
      .catch(error => {
        // Better error message for protected pages
        if (
          error.message.includes('cannot be scripted') ||
          error.message.includes('Cannot access') ||
          error.message.includes('extensions gallery')
        ) {
          throw new Error(
            'Cannot save this page - extensions are blocked on browser internal pages and extension stores'
          );
        }
        throw error;
      });

    // Inject script to convert and get markdown
    const results = await browserAPI.scripting.executeScript({
      target: { tabId: tabId },
      func: extractAndConvertToMarkdown,
    });

    if (!results || !results[0]) {
      throw new Error('Failed to extract page content');
    }

    const result = results[0].result;

    // If operation was cancelled, exit without showing save dialog
    if (!result || result === null) {
      return;
    }

    const { markdown, title, url } = result;

    // Generate filename
    const timestamp = new Date().toISOString().split('T')[0];
    const sanitizedTitle = sanitizeFilename(title || 'untitled');
    const filename = `${sanitizedTitle}-${timestamp}.md`;

    // Get extension version
    const version = browserAPI.runtime.getManifest().version;

    // Add metadata header with attribution
    const content = `# ${title}\n\n**Source:** ${url}\n**Saved:** ${new Date().toISOString()}\n\n*Generated with [markdown-printer](https://github.com/levz0r/markdown-printer) (v${version}) by [Lev Gelfenbuim](https://lev.engineer)*\n\n---\n\n${markdown}`;

    // For Firefox, we need to use a different approach
    // Check if we're in Firefox by checking for browser.downloads
    const isFirefox = typeof browser !== 'undefined' && browser.downloads;

    if (isFirefox) {
      // Firefox: Use blob URL approach with special handling
      // Create a temporary object URL in a way that works in Firefox background scripts
      // We'll inject a helper script into the page to create the blob URL
      await browserAPI.scripting.executeScript({
        target: { tabId: tabId },
        func: (content, filename) => {
          const blob = new Blob([content], { type: 'text/plain' });
          const url = URL.createObjectURL(blob);
          // Trigger download from page context
          const a = document.createElement('a');
          a.href = url;
          a.download = filename;
          a.click();
          URL.revokeObjectURL(url);
          return true;
        },
        args: [content, filename],
      });
    } else {
      // Chrome: Use data URL
      const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
      const reader = new FileReader();

      const dataUrl = await new Promise((resolve, reject) => {
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(blob);
      });

      await browserAPI.downloads.download({
        url: dataUrl,
        filename: filename,
        saveAs: true,
      });
    }
  } catch (error) {
    console.error('Error saving markdown:', error);
    throw error;
  }
}

// This function runs in the page context
async function extractAndConvertToMarkdown() {
  // Normalize HTML content for consistent hashing
  // Removes attributes, IDs, classes, and normalizes whitespace
  function normalizeContent(element) {
    const clone = element.cloneNode(true);

    // Remove all unwanted elements
    const unwantedSelectors = [
      'script',
      'style',
      'noscript',
      'iframe',
      'svg',
      'nav',
      'header',
      'footer',
      '.sidebar',
      '.navigation',
      '.menu',
      '[class*="sidebar"]',
      '[class*="navigation"]',
      'button',
      'input',
      'select',
      'textarea',
    ];

    unwantedSelectors.forEach(selector => {
      const elements = clone.querySelectorAll(selector);
      elements.forEach(el => el.remove());
    });

    // Get text content and normalize whitespace
    const text = clone.textContent || '';
    return text.replace(/\s+/g, ' ').trim();
  }

  // Function to check if element is in viewport
  function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    const windowWidth = window.innerWidth || document.documentElement.clientWidth;

    // Element is in viewport if any part of it is visible
    return rect.top < windowHeight && rect.bottom > 0 && rect.left < windowWidth && rect.right > 0;
  }

  // Calculate Jaccard similarity between two strings
  function calculateSimilarity(str1, str2) {
    // Split into words and filter out very short words
    const words1 = new Set(
      str1
        .toLowerCase()
        .split(/\s+/)
        .filter(w => w.length > 2)
    );
    const words2 = new Set(
      str2
        .toLowerCase()
        .split(/\s+/)
        .filter(w => w.length > 2)
    );

    if (words1.size === 0 && words2.size === 0) {
      return 1;
    }
    if (words1.size === 0 || words2.size === 0) {
      return 0;
    }

    const intersection = new Set([...words1].filter(x => words2.has(x)));
    const union = new Set([...words1, ...words2]);

    return intersection.size / union.size;
  }

  // Function to capture currently visible content blocks
  function captureVisibleContentBlocks() {
    const capturedBlocks = [];

    try {
      // Find content blocks - prioritize semantic elements
      const blockSelectors = [
        'article',
        'section',
        'main > div',
        '[role="main"] > div',
        '.content > div',
        '.documentation-content > div',
        'main > *',
        '[role="main"] > *',
      ];

      const foundBlocks = new Set();

      // Try ALL selectors and combine results (don't stop at first match)
      for (const selector of blockSelectors) {
        const elements = document.querySelectorAll(selector);

        if (elements.length > 0) {
          elements.forEach(element => {
            // Skip if already found this element
            if (foundBlocks.has(element)) {
              return;
            }

            // Only capture if element is in viewport and has substantial content
            if (isInViewport(element)) {
              const text = element.textContent || '';
              if (text.trim().length > 100) {
                foundBlocks.add(element);

                // Clone and convert to markdown
                const cloned = element.cloneNode(true);

                // Remove unwanted elements from clone
                const unwantedSelectors = [
                  'script',
                  'style',
                  'noscript',
                  'iframe',
                  'svg',
                  'nav',
                  'header',
                  'footer',
                  'button:not([role="tab"])',
                  'input',
                  'select',
                  'textarea',
                  '#markdown-printer-overlay',
                ];

                unwantedSelectors.forEach(sel => {
                  const elements = cloned.querySelectorAll(sel);
                  elements.forEach(el => el.remove());
                });

                const tempTurndown = new TurndownService({
                  headingStyle: 'atx',
                  codeBlockStyle: 'fenced',
                  bulletListMarker: '-',
                });
                tempTurndown.remove(['script', 'style', 'noscript', 'iframe', 'svg']);

                const markdown = tempTurndown.turndown(cloned);

                if (markdown && markdown.trim().length > 100) {
                  capturedBlocks.push({
                    markdown: markdown,
                    normalizedContent: normalizeContent(element),
                  });
                }
              }
            }
          });
        }
      }

      // Fallback: If no blocks found, try capturing the entire main content area
      if (capturedBlocks.length === 0) {
        const mainSelectors = ['main', '[role="main"]', 'article', '#content', '.content', 'body'];

        for (const selector of mainSelectors) {
          const mainElement = document.querySelector(selector);
          if (mainElement) {
            const text = mainElement.textContent || '';
            if (text.trim().length > 100) {
              const cloned = mainElement.cloneNode(true);

              // Remove unwanted elements
              const unwantedSelectors = [
                'script',
                'style',
                'noscript',
                'iframe',
                'svg',
                'nav',
                'header',
                'footer',
                'aside',
                '.sidebar',
                '.navigation',
                '.menu',
                'button',
                'input',
                'select',
                'textarea',
                '#markdown-printer-overlay',
              ];

              unwantedSelectors.forEach(sel => {
                const elements = cloned.querySelectorAll(sel);
                elements.forEach(el => el.remove());
              });

              const tempTurndown = new TurndownService({
                headingStyle: 'atx',
                codeBlockStyle: 'fenced',
                bulletListMarker: '-',
              });
              tempTurndown.remove(['script', 'style', 'noscript', 'iframe', 'svg']);

              const markdown = tempTurndown.turndown(cloned);

              if (markdown && markdown.trim().length > 100) {
                capturedBlocks.push({
                  markdown: markdown,
                  normalizedContent: normalizeContent(mainElement),
                });
                break; // Found content, stop trying
              }
            }
          }
        }
      }

      return capturedBlocks;
    } catch (error) {
      console.error('Error capturing content blocks:', error);
      return [];
    }
  }

  // Function to scroll through the entire page to trigger lazy loading
  async function scrollToBottom() {
    // Arrays to store captured content
    const capturedContent = [];
    const capturedHashes = new Set();

    // First, try to expand any collapsed/hidden sections
    const expandCollapsedSections = () => {
      // Find and click on common expandable elements
      const expandableSelectors = [
        'details:not([open])',
        '[aria-expanded="false"]',
        '.collapsed',
        '.expand',
        '.accordion:not(.active)',
        '[data-collapsed="true"]',
        'button[aria-expanded="false"]',
      ];

      let expandedCount = 0;
      expandableSelectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
          try {
            if (el.tagName === 'DETAILS') {
              el.open = true;
            } else if (el.click) {
              el.click();
            }
            expandedCount++;
          } catch (_e) {
            // Ignore errors
          }
        });
      });
      return expandedCount;
    };

    // Try to expand sections before scrolling
    expandCollapsedSections();
    await new Promise(resolve => setTimeout(resolve, 500));

    // Create progress indicator overlay
    const overlay = document.createElement('div');
    overlay.id = 'markdown-printer-overlay';
    overlay.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: rgba(0, 0, 0, 0.9);
      color: white;
      padding: 20px;
      border-radius: 8px;
      z-index: 999999;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
      min-width: 300px;
      opacity: 0;
      transition: opacity 0.3s ease-in-out;
    `;

    const title = document.createElement('div');
    title.textContent = 'Printing...';
    title.style.cssText = 'font-weight: bold; margin-bottom: 10px; font-size: 16px;';

    const percentageText = document.createElement('div');
    percentageText.id = 'percentage-text';
    percentageText.style.cssText =
      'font-size: 24px; font-weight: bold; margin-bottom: 5px; color: #4CAF50;';
    percentageText.textContent = '0%';

    const status = document.createElement('div');
    status.id = 'scroll-status';
    status.style.cssText = 'margin-bottom: 10px; font-size: 14px; opacity: 0.8;';

    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 2px;
      overflow: hidden;
      margin-bottom: 10px;
    `;

    const progressFill = document.createElement('div');
    progressFill.id = 'progress-fill';
    progressFill.style.cssText = `
      height: 100%;
      background: #4CAF50;
      width: 0%;
      transition: width 0.3s ease;
    `;
    progressBar.appendChild(progressFill);

    const cancelButton = document.createElement('button');
    cancelButton.textContent = 'Abort';
    cancelButton.style.cssText = `
      width: 100%;
      padding: 8px;
      background: #f44336;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      font-weight: bold;
      transition: background 0.2s ease;
    `;
    cancelButton.onmouseover = () => (cancelButton.style.background = '#d32f2f');
    cancelButton.onmouseout = () => (cancelButton.style.background = '#f44336');

    overlay.appendChild(title);
    overlay.appendChild(percentageText);
    overlay.appendChild(status);
    overlay.appendChild(progressBar);
    overlay.appendChild(cancelButton);
    document.body.appendChild(overlay);

    // Trigger fade-in animation
    window.requestAnimationFrame(() => {
      overlay.style.opacity = '1';
    });

    let cancelled = false;
    cancelButton.onclick = () => {
      cancelled = true;
      status.textContent = 'Stopping...';
      cancelButton.disabled = true;
      cancelButton.style.opacity = '0.5';
    };

    // Make all hidden content sections visible (common in documentation sites)
    const makeAllContentVisible = () => {
      // Target common documentation content containers
      const contentSelectors = [
        'article',
        'section',
        'main',
        '[role="main"]',
        '[class*="content"]',
        '[class*="documentation"]',
        '[class*="api"]',
        '[class*="endpoint"]',
        '[id*="content"]',
      ];

      contentSelectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
          const style = window.getComputedStyle(el);
          if (style.display === 'none' || style.visibility === 'hidden') {
            el.style.display = 'block';
            el.style.visibility = 'visible';
            el.style.opacity = '1';
          }
          // Also unhide all children
          el.querySelectorAll('*').forEach(child => {
            const childStyle = window.getComputedStyle(child);
            if (childStyle.display === 'none' || childStyle.visibility === 'hidden') {
              child.style.display = 'block';
              child.style.visibility = 'visible';
              child.style.opacity = '1';
            }
          });
        });
      });
    };

    // First, make content visible
    status.textContent = 'Loading content...';
    makeAllContentVisible();
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Update progress display
    const updateProgress = (current, total, stableCount, sectionsCount) => {
      const percentage = Math.min(100, Math.round((current / total) * 100));
      progressFill.style.width = percentage + '%';
      percentageText.textContent = percentage + '%';
      status.textContent = `${current.toLocaleString()}px / ${total.toLocaleString()}px`;
      if (sectionsCount > 0) {
        status.textContent += ` | ${sectionsCount} sections`;
      }
      if (stableCount > 0) {
        status.textContent += ` (${stableCount}/3 stable)`;
      }
    };

    // Smooth scroll function that triggers events
    const smoothScrollTo = async targetY => {
      const startY = window.scrollY;
      const distance = targetY - startY;
      const duration = 150; // ms (reduced for faster scrolling)
      const startTime = window.performance.now();

      return new Promise(resolve => {
        const scroll = currentTime => {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const easeProgress = progress * (2 - progress); // ease out

          window.scrollTo(0, startY + distance * easeProgress);

          // Dispatch scroll event to trigger listeners
          window.dispatchEvent(new window.Event('scroll'));

          if (progress < 1) {
            window.requestAnimationFrame(scroll);
          } else {
            resolve();
          }
        };
        window.requestAnimationFrame(scroll);
      });
    };

    // Start from the top
    await smoothScrollTo(0);
    await new Promise(resolve => setTimeout(resolve, 100));

    let lastHeight = document.documentElement.scrollHeight;
    let stableScrollCount = 0;

    // Scroll down in increments (2x viewport height for faster scrolling)
    const scrollStep = window.innerHeight * 2;
    let currentPosition = 0;

    while (!cancelled) {
      // Smooth scroll to current position
      await smoothScrollTo(currentPosition);

      // Wait for content to load (reduced for faster scrolling)
      await new Promise(resolve => setTimeout(resolve, 200));

      // Capture visible content blocks at current position
      const blocks = captureVisibleContentBlocks();
      blocks.forEach(block => {
        // Check if this content is similar to anything we've already captured
        const isDuplicate = Array.from(capturedHashes).some(existingContent => {
          const similarity = calculateSimilarity(block.normalizedContent, existingContent);
          return similarity > 0.85; // 85% similar = duplicate
        });

        if (!isDuplicate) {
          capturedHashes.add(block.normalizedContent);
          capturedContent.push(block.markdown);
        }
      });

      const newHeight = document.documentElement.scrollHeight;
      updateProgress(currentPosition, newHeight, stableScrollCount, capturedContent.length);

      // If we've reached the bottom and height hasn't changed for 3 consecutive attempts
      if (currentPosition >= newHeight) {
        if (newHeight === lastHeight) {
          stableScrollCount++;
          if (stableScrollCount >= 3) {
            percentageText.textContent = '100%';
            progressFill.style.width = '100%';
            status.textContent = `Complete! Captured ${capturedContent.length} sections`;
            break;
          }
        } else {
          stableScrollCount = 0;
        }
      }

      // Update tracking variables
      lastHeight = newHeight;
      currentPosition += scrollStep;
    }

    // Ensure we scroll all the way to the bottom and wait for content to render
    if (!cancelled) {
      await smoothScrollTo(document.documentElement.scrollHeight);
      await new Promise(resolve => setTimeout(resolve, 1000));

      // Expand any sections that became available during scrolling
      expandCollapsedSections();
      await new Promise(resolve => setTimeout(resolve, 500));

      // Do a second full scroll pass - some content only loads after first pass
      currentPosition = 0;
      const secondPassHeight = document.documentElement.scrollHeight;
      status.textContent = 'Second pass: loading remaining content...';

      while (currentPosition < secondPassHeight && !cancelled) {
        await smoothScrollTo(currentPosition);
        await new Promise(resolve => setTimeout(resolve, 200));

        // Capture any new content blocks in second pass
        const blocks = captureVisibleContentBlocks();
        blocks.forEach(block => {
          // Check if this content is similar to anything we've already captured
          const isDuplicate = Array.from(capturedHashes).some(existingContent => {
            const similarity = calculateSimilarity(block.normalizedContent, existingContent);
            return similarity > 0.85; // 85% similar = duplicate
          });

          if (!isDuplicate) {
            capturedHashes.add(block.normalizedContent);
            capturedContent.push(block.markdown);
          }
        });

        currentPosition += scrollStep;
      }

      // Final stay at bottom to ensure everything loads
      await smoothScrollTo(document.documentElement.scrollHeight);
      await new Promise(resolve => setTimeout(resolve, 1000));

      // One more expansion attempt
      expandCollapsedSections();
      await new Promise(resolve => setTimeout(resolve, 500));
    }

    // Fade out and remove overlay
    overlay.style.opacity = '0';
    await new Promise(resolve => setTimeout(resolve, 300));
    overlay.remove();

    // Return status and captured content
    return { cancelled, capturedContent };
  }

  // Scroll through the page first
  const scrollResult = await scrollToBottom();

  // If scrolling was cancelled, return null to indicate no download should occur
  if (scrollResult.cancelled) {
    return null;
  }

  // Combine all captured content sections
  const { capturedContent } = scrollResult;

  // Join all sections with double newlines for spacing
  const combinedMarkdown = capturedContent.join('\n\n---\n\n');

  return {
    markdown: combinedMarkdown,
    title: document.title,
    url: window.location.href,
  };
}

function sanitizeFilename(filename) {
  return filename
    .replace(/[<>:"/\\|?*]/g, '-')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .substring(0, 200);
}
```

## File: `test/build.test.js`
```javascript
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

describe('Build Validation', () => {
  const distDir = path.join(__dirname, '../dist');
  const packageJson = JSON.parse(fs.readFileSync(path.join(__dirname, '../package.json'), 'utf8'));
  const version = packageJson.version;

  // Run build before tests
  beforeAll(() => {
    // Ensure dist directory exists (build.js creates it)
    if (!fs.existsSync(distDir)) {
      fs.mkdirSync(distDir, { recursive: true });
    }
  });

  describe('Build Script', () => {
    test('build.js exists and is executable', () => {
      const buildScript = path.join(__dirname, '../build.js');
      expect(fs.existsSync(buildScript)).toBe(true);

      // Check if it's executable (has shebang)
      const content = fs.readFileSync(buildScript, 'utf8');
      expect(content.startsWith('#!/usr/bin/env node')).toBe(true);
    });

    test('build.js reads version from package.json', () => {
      const buildScript = fs.readFileSync(path.join(__dirname, '../build.js'), 'utf8');
      expect(buildScript).toContain('packageJson.version');
    });

    test('build script can be executed', () => {
      expect(() => {
        execSync('node build.js', { cwd: path.join(__dirname, '..'), stdio: 'pipe' });
      }).not.toThrow();
    });
  });

  describe('Dist Directory', () => {
    test('dist directory is created', () => {
      expect(fs.existsSync(distDir)).toBe(true);
    });

    test('Chrome package exists with correct name', () => {
      const chromePkg = path.join(distDir, `markdown-printer-chrome-v${version}.zip`);
      expect(fs.existsSync(chromePkg)).toBe(true);
    });

    test('Firefox package exists with correct name', () => {
      const firefoxPkg = path.join(distDir, `markdown-printer-firefox-v${version}.zip`);
      expect(fs.existsSync(firefoxPkg)).toBe(true);
    });

    test('packages are not empty', () => {
      const chromePkg = path.join(distDir, `markdown-printer-chrome-v${version}.zip`);
      const firefoxPkg = path.join(distDir, `markdown-printer-firefox-v${version}.zip`);

      const chromeStat = fs.statSync(chromePkg);
      const firefoxStat = fs.statSync(firefoxPkg);

      expect(chromeStat.size).toBeGreaterThan(1000); // At least 1KB
      expect(firefoxStat.size).toBeGreaterThan(1000); // At least 1KB
    });

    test('packages are under size limit', () => {
      const chromePkg = path.join(distDir, `markdown-printer-chrome-v${version}.zip`);
      const firefoxPkg = path.join(distDir, `markdown-printer-firefox-v${version}.zip`);

      const chromeStat = fs.statSync(chromePkg);
      const firefoxStat = fs.statSync(firefoxPkg);

      const maxSize = 200 * 1024 * 1024; // 200MB limit
      expect(chromeStat.size).toBeLessThan(maxSize);
      expect(firefoxStat.size).toBeLessThan(maxSize);
    });
  });

  describe('Manifest Updates', () => {
    test('Chrome manifest has correct version', () => {
      const chromeManifest = JSON.parse(
        fs.readFileSync(path.join(__dirname, '../extension-chrome/manifest.json'), 'utf8')
      );
      expect(chromeManifest.version).toBe(version);
    });

    test('Firefox manifest has correct version', () => {
      const firefoxManifest = JSON.parse(
        fs.readFileSync(path.join(__dirname, '../extension-firefox/manifest.json'), 'utf8')
      );
      expect(firefoxManifest.version).toBe(version);
    });
  });

  describe('File Exclusions', () => {
    test('no .DS_Store files in extensions', () => {
      const chromeDSStore = path.join(__dirname, '../extension-chrome/.DS_Store');
      const firefoxDSStore = path.join(__dirname, '../extension-firefox/.DS_Store');

      expect(fs.existsSync(chromeDSStore)).toBe(false);
      expect(fs.existsSync(firefoxDSStore)).toBe(false);
    });

    test('.gitignore includes dist directory', () => {
      const gitignore = fs.readFileSync(path.join(__dirname, '../.gitignore'), 'utf8');
      expect(gitignore).toContain('dist/');
    });

    test('.gitignore includes zip files', () => {
      const gitignore = fs.readFileSync(path.join(__dirname, '../.gitignore'), 'utf8');
      expect(gitignore).toContain('*.zip');
    });
  });

  describe('Package.json Scripts', () => {
    test('has build script', () => {
      expect(packageJson.scripts).toHaveProperty('build');
      expect(packageJson.scripts.build).toBe('node build.js');
    });

    test('has build:chrome script', () => {
      expect(packageJson.scripts).toHaveProperty('build:chrome');
      expect(packageJson.scripts['build:chrome']).toBe('node build.js chrome');
    });

    test('has build:firefox script', () => {
      expect(packageJson.scripts).toHaveProperty('build:firefox');
      expect(packageJson.scripts['build:firefox']).toBe('node build.js firefox');
    });

    test('has version bump scripts', () => {
      expect(packageJson.scripts).toHaveProperty('version:patch');
      expect(packageJson.scripts).toHaveProperty('version:minor');
      expect(packageJson.scripts).toHaveProperty('version:major');
    });
  });
});
```

## File: `test/manifest.test.js`
```javascript
const fs = require('fs');
const path = require('path');

describe('Manifest Validation', () => {
  let chromeManifest;
  let firefoxManifest;
  let packageJson;

  beforeAll(() => {
    chromeManifest = JSON.parse(
      fs.readFileSync(path.join(__dirname, '../extension-chrome/manifest.json'), 'utf8')
    );
    firefoxManifest = JSON.parse(
      fs.readFileSync(path.join(__dirname, '../extension-firefox/manifest.json'), 'utf8')
    );
    packageJson = JSON.parse(fs.readFileSync(path.join(__dirname, '../package.json'), 'utf8'));
  });

  describe('Version Consistency', () => {
    test('Chrome manifest version matches package.json', () => {
      expect(chromeManifest.version).toBe(packageJson.version);
    });

    test('Firefox manifest version matches package.json', () => {
      expect(firefoxManifest.version).toBe(packageJson.version);
    });

    test('version follows semver format', () => {
      const semverRegex = /^\d+\.\d+\.\d+$/;
      expect(packageJson.version).toMatch(semverRegex);
    });
  });

  describe('Common Fields', () => {
    test('both manifests have same name', () => {
      expect(chromeManifest.name).toBe(firefoxManifest.name);
      expect(chromeManifest.name).toBe('__MSG_extensionName__');
    });

    test('both manifests have same description', () => {
      expect(chromeManifest.description).toBe(firefoxManifest.description);
      expect(chromeManifest.description).toBe('__MSG_extensionDescription__');
    });

    test('both manifests have default_locale set to en', () => {
      expect(chromeManifest.default_locale).toBe('en');
      expect(firefoxManifest.default_locale).toBe('en');
    });

    test('both manifests use Manifest V3', () => {
      expect(chromeManifest.manifest_version).toBe(3);
      expect(firefoxManifest.manifest_version).toBe(3);
    });

    test('both manifests have same permissions', () => {
      expect(chromeManifest.permissions).toEqual(firefoxManifest.permissions);
      expect(chromeManifest.permissions).toEqual([
        'activeTab',
        'contextMenus',
        'downloads',
        'scripting',
      ]);
    });

    test('both manifests have same author', () => {
      expect(chromeManifest.author).toBe('Lev Gelfenbuim');
      expect(firefoxManifest.author).toBe('Lev Gelfenbuim');
    });

    test('both manifests have same homepage_url', () => {
      expect(chromeManifest.homepage_url).toBe('https://github.com/levz0r/markdown-printer');
      expect(firefoxManifest.homepage_url).toBe('https://github.com/levz0r/markdown-printer');
    });
  });

  describe('Icons', () => {
    test('both manifests have required icon sizes', () => {
      const expectedSizes = ['16', '48', '128'];

      expectedSizes.forEach(size => {
        expect(chromeManifest.icons).toHaveProperty(size);
        expect(firefoxManifest.icons).toHaveProperty(size);
      });
    });

    test('icon files exist', () => {
      const chromeIconPath = path.join(__dirname, '../extension-chrome');
      const firefoxIconPath = path.join(__dirname, '../extension-firefox');

      ['icon16.png', 'icon48.png', 'icon128.png'].forEach(icon => {
        expect(fs.existsSync(path.join(chromeIconPath, icon))).toBe(true);
        expect(fs.existsSync(path.join(firefoxIconPath, icon))).toBe(true);
      });
    });
  });

  describe('Chrome-Specific Fields', () => {
    test('has service_worker background', () => {
      expect(chromeManifest.background).toHaveProperty('service_worker');
      expect(chromeManifest.background.service_worker).toBe('background.js');
    });

    test('does not have browser_specific_settings', () => {
      expect(chromeManifest.browser_specific_settings).toBeUndefined();
    });

    test('has action with popup', () => {
      expect(chromeManifest.action).toHaveProperty('default_popup');
      expect(chromeManifest.action.default_popup).toBe('popup.html');
    });
  });

  describe('Firefox-Specific Fields', () => {
    test('has scripts background', () => {
      expect(firefoxManifest.background).toHaveProperty('scripts');
      expect(firefoxManifest.background.scripts).toEqual(['background.js']);
    });

    test('has browser_specific_settings', () => {
      expect(firefoxManifest.browser_specific_settings).toBeDefined();
      expect(firefoxManifest.browser_specific_settings.gecko).toBeDefined();
    });

    test('has extension ID', () => {
      expect(firefoxManifest.browser_specific_settings.gecko.id).toBe(
        'markdown-printer@lev.engineer'
      );
    });

    test('has minimum Firefox version', () => {
      expect(firefoxManifest.browser_specific_settings.gecko.strict_min_version).toBe('121.0');
    });

    test('has data collection permissions', () => {
      expect(firefoxManifest.browser_specific_settings.gecko.data_collection_permissions).toEqual({
        required: ['none'],
      });
    });
  });

  describe('Required Files', () => {
    test('Chrome extension has all required files', () => {
      const chromeDir = path.join(__dirname, '../extension-chrome');
      const requiredFiles = [
        'manifest.json',
        'background.js',
        'popup.html',
        'popup.js',
        'turndown.js',
        'icon16.png',
        'icon48.png',
        'icon128.png',
      ];

      requiredFiles.forEach(file => {
        expect(fs.existsSync(path.join(chromeDir, file))).toBe(true);
      });
    });

    test('Firefox extension has all required files', () => {
      const firefoxDir = path.join(__dirname, '../extension-firefox');
      const requiredFiles = [
        'manifest.json',
        'background.js',
        'popup.html',
        'popup.js',
        'turndown.js',
        'icon16.png',
        'icon48.png',
        'icon128.png',
      ];

      requiredFiles.forEach(file => {
        expect(fs.existsSync(path.join(firefoxDir, file))).toBe(true);
      });
    });
  });

  describe('Internationalization', () => {
    test('_locales directory exists', () => {
      const localesDir = path.join(__dirname, '../_locales');
      expect(fs.existsSync(localesDir)).toBe(true);
    });

    test('has required locale directories', () => {
      const localesDir = path.join(__dirname, '../_locales');
      const requiredLocales = ['en', 'he', 'hi', 'fr'];

      requiredLocales.forEach(locale => {
        const localeDir = path.join(localesDir, locale);
        expect(fs.existsSync(localeDir)).toBe(true);
      });
    });

    test('each locale has messages.json', () => {
      const localesDir = path.join(__dirname, '../_locales');
      const requiredLocales = ['en', 'he', 'hi', 'fr'];

      requiredLocales.forEach(locale => {
        const messagesPath = path.join(localesDir, locale, 'messages.json');
        expect(fs.existsSync(messagesPath)).toBe(true);
      });
    });

    test('messages.json files have required keys', () => {
      const localesDir = path.join(__dirname, '../_locales');
      const requiredLocales = ['en', 'he', 'hi', 'fr'];
      const requiredKeys = [
        'extensionName',
        'extensionDescription',
        'savePageButton',
        'contextMenuTitle',
      ];

      requiredLocales.forEach(locale => {
        const messagesPath = path.join(localesDir, locale, 'messages.json');
        const messages = JSON.parse(fs.readFileSync(messagesPath, 'utf8'));

        requiredKeys.forEach(key => {
          expect(messages).toHaveProperty(key);
          expect(messages[key]).toHaveProperty('message');
          expect(messages[key].message).toBeTruthy();
        });
      });
    });
  });
});
```

## File: `test/utils.test.js`
```javascript
const { sanitizeFilename } = require('../utils');

describe('sanitizeFilename', () => {
  describe('special character removal', () => {
    test('removes invalid filename characters', () => {
      expect(sanitizeFilename('Test<>:"/\\|?*File')).toBe('Test-File');
    });

    test('replaces colon with hyphen', () => {
      expect(sanitizeFilename('Test: File')).toBe('Test-File');
    });

    test('removes question marks', () => {
      expect(sanitizeFilename('What? Where?')).toBe('What-Where-');
    });

    test('removes asterisks', () => {
      expect(sanitizeFilename('File*.txt')).toBe('File-.txt');
    });
  });

  describe('whitespace handling', () => {
    test('replaces single space with hyphen', () => {
      expect(sanitizeFilename('Test File')).toBe('Test-File');
    });

    test('replaces multiple spaces with single hyphen', () => {
      expect(sanitizeFilename('Test    File')).toBe('Test-File');
    });

    test('replaces tabs with hyphen', () => {
      expect(sanitizeFilename('Test\tFile')).toBe('Test-File');
    });

    test('replaces newlines with hyphen', () => {
      expect(sanitizeFilename('Test\nFile')).toBe('Test-File');
    });
  });

  describe('hyphen collapsing', () => {
    test('collapses multiple hyphens into one', () => {
      expect(sanitizeFilename('Test---File')).toBe('Test-File');
    });

    test('collapses hyphens from special chars and spaces', () => {
      expect(sanitizeFilename('Test: File?')).toBe('Test-File-');
    });
  });

  describe('length truncation', () => {
    test('truncates to 200 characters', () => {
      const longName = 'a'.repeat(250);
      expect(sanitizeFilename(longName)).toHaveLength(200);
    });

    test('preserves short filenames', () => {
      expect(sanitizeFilename('short.md')).toBe('short.md');
    });

    test('exactly 200 characters is unchanged', () => {
      const exactName = 'a'.repeat(200);
      expect(sanitizeFilename(exactName)).toHaveLength(200);
    });
  });

  describe('edge cases', () => {
    test('handles empty string', () => {
      expect(sanitizeFilename('')).toBe('');
    });

    test('handles string with only special characters', () => {
      expect(sanitizeFilename('???')).toBe('-');
    });

    test('handles filename with extension', () => {
      expect(sanitizeFilename('My Document.md')).toBe('My-Document.md');
    });

    test('preserves periods in filename', () => {
      expect(sanitizeFilename('file.name.md')).toBe('file.name.md');
    });

    test('handles unicode characters', () => {
      expect(sanitizeFilename('Test 文件')).toBe('Test-文件');
    });

    test('handles emojis', () => {
      expect(sanitizeFilename('Test 🎉 File')).toBe('Test-🎉-File');
    });
  });

  describe('real-world examples', () => {
    test('handles typical page title', () => {
      expect(sanitizeFilename('Getting Started Guide')).toBe('Getting-Started-Guide');
    });

    test('handles URL-like filename', () => {
      expect(sanitizeFilename('https://example.com/page')).toBe('https-example.com-page');
    });

    test('handles dates in filename', () => {
      expect(sanitizeFilename('Report 2025-01-15')).toBe('Report-2025-01-15');
    });

    test('handles filename with quotes', () => {
      expect(sanitizeFilename('The "Best" Guide')).toBe('The-Best-Guide');
    });
  });
});
```

