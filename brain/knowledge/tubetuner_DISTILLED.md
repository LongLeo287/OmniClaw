---
id: tubetuner
type: knowledge
owner: OA_Triage
---
# tubetuner
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "tubetuner",
  "version": "1.0.0",
  "description": "<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 --> <a id=\"readme-top\"></a>",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build:chrome": "vite build --mode chrome",
    "build:firefox": "vite build --mode firefox",
    "zip:chrome": "npm run build:chrome && npx web-ext build --source-dir ./dist/chrome --artifacts-dir ./packages/chrome",
    "zip:firefox": "npm run build:firefox && npx web-ext build --source-dir ./dist/firefox --artifacts-dir ./packages/firefox"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/PhanKydeptrai/TubeTuner.git"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "bugs": {
    "url": "https://github.com/PhanKydeptrai/TubeTuner/issues"
  },
  "homepage": "https://github.com/PhanKydeptrai/TubeTuner#readme",
  "devDependencies": {
    "@crxjs/vite-plugin": "^2.0.0-beta.33",
    "fs-extra": "^11.3.3",
    "path": "^0.12.7",
    "vite": "^7.3.0"
  }
}

```

### File: README.md
```md
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU GPL v3][license-shield]][license-url]

<h1 align="center">
  <img src="src/images/banners/banner.png" alt="TubeTuner Banner" /><br/>
  TubeTuner
</h1>

<h4 align="center">
  <a href="README.md">English</a> |
  <a href="README_VI.md">Tiếng Việt</a>
</h4>

<h3 align="center">Customize the YouTube interface to eliminate distractions and create a focused, personalized viewing experience</h3>

<p align="center">
  <a href="https://github.com/PhanKydeptrai/TubeTuner"><strong>Explore the docs »</strong></a>
  <br /><br />
  <a href="https://github.com/PhanKydeptrai/TubeTuner">View Demo</a>
  ·
  <a href="https://github.com/PhanKydeptrai/TubeTuner/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
  ·
  <a href="https://github.com/PhanKydeptrai/TubeTuner/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
</p>

---

## Table of Contents

1. [Get This Extension](#get-this-extension)
2. [About The Project](#about-the-project)
   - [Built With](#built-with)
3. [Getting Started](#getting-started)
   - [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

---

## Get This Extension

[![Chrome Web Store](https://img.shields.io/badge/Chrome_Web_Store-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://chromewebstore.google.com/detail/tubetuner/ekllndjjhcpljlfhfblfcagbdjnjkbco)
[![Firefox Add-ons](https://img.shields.io/badge/Firefox_Add_ons-FF7139?style=for-the-badge&logo=firefoxbrowser&logoColor=white)](https://addons.mozilla.org/vi/firefox/addon/tubetuner/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## About The Project

TubeTuner is a Chrome/Firefox extension that lets you customize your YouTube interface to match your preferences. Hide distracting elements and focus on video content with 21 different hide/show options, plus utility features like presets and export/import for backups.

### What's New in v1.3.9
- **Hide Thumbnails Feature** — Added a new option to hide thumbnails across YouTube surfaces.
- **Hide Channel Improvements** — Improved hiding for the channel block below videos, including channel name, avatar, and subscribe controls.
- **Preset Improvements** — Improved custom preset management with support for updating saved presets, renaming them, and keeping older presets compatible with newly added settings.


### Features

**Content & Feed Controls**
- Hide Home Feed — Avoid distractions from the YouTube homepage
- Hide Video Sidebar — Hide the entire video sidebar (includes live chat, recommendations, and playlist)
  - Hide Live Chat — Control live chat visibility independently
  - Hide Video Suggestions — Control video recommendations visibility independently
  - Hide Playlist — Control playlist panel visibility independently
- Hide Comments — Hide the video comments section
- Hide Shorts — Completely hide Shorts videos and the Shorts section
- Hide Thumbnails — Hide thumbnails across video lists and recommendation surfaces
- Hide Channel — Hide the channel block below the video, including the channel name, avatar, and subscribe controls
- Hide Shop — Hide the YouTube Shop section

**Interface Elements**
- Hide Top Header — Hide the top navigation bar
- Hide Notifications Bell — Hide the notification bell icon
- Hide Explore & Trending — Hide Explore and Trending tabs from the sidebar
- Hide More from YouTube — Hide the "More from YouTube" section
- Hide Buttons Bar — Hide the action buttons bar below the video
- Grayscale — Apply a grayscale filter to the entire YouTube UI

**Video Controls**
- Hide Video Controls — Hide the video player controls (includes progress bar and duration)
  - Hide Progress Bar — Remove the progress bar when watching videos
  - Hide Duration — Hide current time and total duration information
- Hide End Screen Cards — Hide end screen cards that appear at the end of videos
- Hide Description — Hide the video description section
- Hide AI Summary — Hide the AI-generated summary on video pages

**Other Features**
- Export/Import Settings — Export settings to a file for backups and import to restore or share configurations
- Presets — Apply built-in presets (None, Balanced, Focus), create or update custom presets, rename them, and export/import them for backup
- Dark Mode — Automatically follows your system theme
- Multi-language — Supports Vietnamese and English
- Enable/Disable Extension — Quickly toggle the extension on or off from the popup

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![JavaScript][JavaScript-shield]][JavaScript-url]
- [![HTML5][HTML5-shield]][HTML5-url]
- [![CSS3][CSS3-shield]][CSS3-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

Follow these steps to set up a local copy of the extension.

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/PhanKydeptrai/TubeTuner.git
   ```

2. **Install dependencies:**
   ```sh
   npm install
   ```

3. **Set up environment variables:**
   Copy the example environment file and update the values if necessary:
   ```sh
   cp .env.example .env
   ```

4. **Build the extension:**

   For Chrome:
   ```sh
   npm run build:chrome
   ```

   For Firefox:
   ```sh
   npm run build:firefox
   ```

5. **Load in Chrome:**
   - Open `chrome://extensions/`
   - Enable **Developer mode** (top right)
   - Click **Load unpacked**
   - Select the `dist/chrome` folder

6. **Load in Firefox:**
   - Open `about:debugging#/runtime/this-firefox`
   - Click **Load Temporary Add-on...**
   - Select any file in the `dist/firefox` folder (e.g., `manifest.json`)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

1. **Open YouTube** and play any video.
2. **Click the extension icon** in the browser toolbar.
3. **Explore the 3 main sections:**
   - **Content & Feed Controls** — Hide/show Home Feed, Video Sidebar (with grouped controls for Live Chat, Video Suggestions, Playlist), Comments, Shorts, Thumbnails, Channel, Shop
   - **Interface Elements** — Hide/show Top Header, Notifications Bell, Explore & Trending, More from YouTube, Buttons Bar, Grayscale
   - **Video Controls** — Hide/show Video Controls (with grouped controls for Progress Bar, Duration), End Screen Cards, Description, AI Summary
4. **Use toggle switches** to enable or disable each feature individually.
5. **Switch theme** — Click the sun/moon button at the top to toggle Light/Dark mode.
6. **Export/Import Settings** — Use the buttons in the settings section to backup or restore configurations.
7. **Presets** — Choose a built-in preset (None, Balanced, Focus) to apply multiple settings at once.
8. **Custom Presets** — Configure your toggles and click "Save preset" to create a named preset. You can update an existing custom preset after changing settings, rename it, import presets from a `.json` file, export them for backup, or delete a selected custom preset.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion, please fork the repository and create a pull request. You can also open an issue with the tag `enhancement`. Don't forget to give the project a star!

1. Fork the project
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

Phan Ky — phanky.dev@proton.me

Project Link: [https://github.com/PhanKydeptrai/TubeTuner](https://github.com/PhanKydeptrai/TubeTuner)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[contributors-url]: https://github.com/PhanKydeptrai/TubeTuner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[forks-url]: https://github.com/PhanKydeptrai/TubeTuner/network/members
[stars-shield]: https://img.shields.io/github/stars/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[stars-url]: https://github.com/PhanKydeptrai/TubeTuner/stargazers
[issues-shield]: https://img.shields.io/github/issues/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[issues-url]: https://github.com/PhanKydeptrai/TubeTuner/issues
[license-shield]: https://img.shields.io/github/license/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[license-url]: https://github.com/PhanKydeptrai/TubeTuner/blob/main/LICENSE
[JavaScript-shield]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[HTML5-shield]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5
[CSS3-shield]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://developer.mozilla.org/en-US/docs/Web/CSS

```

### File: src\features\index.js
```js
export { toggleAiSummary } from './aiSummary.js';
export { toggleButtonsBar } from './buttonsBar.js';
export { toggleComments } from './comments.js';
export { toggleDuration } from './duration.js';
export { toggleEndScreenCards } from './endScreenCards.js';
export { toggleExploreSection } from './exploreSection.js';
export { toggleGrayscale } from './grayscale.js';
export { toggleHideChannel } from './hideChannel.js';
export { toggleHideDescription } from './hideDescription.js';
export { toggleHomeFeed } from './homeFeed.js';
export { toggleLivechat } from './livechat.js';
export { toggleMoreFromYouTube } from './moreFromYouTube.js';
export { toggleNotificationsBell } from './notificationsBell.js';
export { togglePlaylist } from './playlist.js';
export { toggleProgressBar } from './progressBar.js';
export { toggleRecommendation } from './recommendation.js';
export { toggleShop } from './shop.js';
export { toggleShorts } from './shorts.js';
export { toggleTopHeader } from './topHeader.js';
export { toggleVideoSidebar } from './videoSidebar.js';
export { toggleHideThumbnail } from './hideThumbnail.js';

```

### File: package-lock.json
```json
{
  "name": "tubetuner",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "tubetuner",
      "version": "1.0.0",
      "license": "ISC",
      "devDependencies": {
        "@crxjs/vite-plugin": "^2.0.0-beta.33",
        "fs-extra": "^11.3.3",
        "path": "^0.12.7",
        "vite": "^7.3.0"
      }
    },
    "node_modules/@crxjs/vite-plugin": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/@crxjs/vite-plugin/-/vite-plugin-2.3.0.tgz",
      "integrity": "sha512-+0CNVGS4bB30OoaF1vUsHVwWU1Lm7MxI0XWY9Fd/Ob+ZVTZgEFNqJ1ZC69IVwQsoYhY0sMQLvpLWiFIuDz8htg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^4.1.2",
        "@webcomponents/custom-elements": "^1.5.0",
        "acorn-walk": "^8.2.0",
        "cheerio": "^1.0.0-rc.10",
        "convert-source-map": "^1.7.0",
        "debug": "^4.3.3",
        "es-module-lexer": "^0.10.0",
        "fast-glob": "^3.2.11",
        "fs-extra": "^10.0.1",
        "jsesc": "^3.0.2",
        "magic-string": "^0.30.12",
        "pathe": "^2.0.1",
        "picocolors": "^1.1.1",
        "react-refresh": "^0.13.0",
        "rollup": "2.79.2",
        "rxjs": "7.5.7"
      }
    },
    "node_modules/@crxjs/vite-plugin/node_modules/fs-extra": {
      "version": "10.1.0",
      "resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-10.1.0.tgz",
      "integrity": "sha512-oRXApq54ETRj4eMiFzGnHWGy+zo5raudjuxN0b8H7s/RU2oW0Wvsx9O0ACRN/kRq9E8Vu/ReskGB5o3ji+FzHQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "graceful-fs": "^4.2.0",
        "jsonfile": "^6.0.1",
        "universalify": "^2.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.2.tgz",
      "integrity": "sha512-GZMB+a0mOMZs4MpDbj8RJp4cw+w1WV5NYD6xzgvzUJ5Ek2jerwfO2eADyI6ExDSUED+1X8aMbegahsJi+8mgpw==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.2.tgz",
      "integrity": "sha512-DVNI8jlPa7Ujbr1yjU2PfUSRtAUZPG9I1RwW4F4xFB1Imiu2on0ADiI/c3td+KmDtVKNbi+nffGDQMfcIMkwIA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.2.tgz",
      "integrity": "sha512-pvz8ZZ7ot/RBphf8fv60ljmaoydPU12VuXHImtAs0XhLLw+EXBi2BLe3OYSBslR4rryHvweW5gmkKFwTiFy6KA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.2.tgz",
      "integrity": "sha512-z8Ank4Byh4TJJOh4wpz8g2vDy75zFL0TlZlkUkEwYXuPSgX8yzep596n6mT7905kA9uHZsf/o2OJZubl2l3M7A==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.2.tgz",
      "integrity": "sha512-davCD2Zc80nzDVRwXTcQP/28fiJbcOwvdolL0sOiOsbwBa72kegmVU0Wrh1MYrbuCL98Omp5dVhQFWRKR2ZAlg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.2.tgz",
      "integrity": "sha512-ZxtijOmlQCBWGwbVmwOF/UCzuGIbUkqB1faQRf5akQmxRJ1ujusWsb3CVfk/9iZKr2L5SMU5wPBi1UWbvL+VQA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.2.tgz",
      "integrity": "sha512-lS/9CN+rgqQ9czogxlMcBMGd+l8Q3Nj1MFQwBZJyoEKI50XGxwuzznYdwcav6lpOGv5BqaZXqvBSiB/kJ5op+g==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.2.tgz",
      "integrity": "sha512-tAfqtNYb4YgPnJlEFu4c212HYjQWSO/w/h/lQaBK7RbwGIkBOuNKQI9tqWzx7Wtp7bTPaGC6MJvWI608P3wXYA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.2.tgz",
      "integrity": "sha512-vWfq4GaIMP9AIe4yj1ZUW18RDhx6EPQKjwe7n8BbIecFtCQG4CfHGaHuh7fdfq+y3LIA2vGS/o9ZBGVxIDi9hw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.2.tgz",
      "integrity": "sha512-hYxN8pr66NsCCiRFkHUAsxylNOcAQaxSSkHMMjcpx0si13t1LHFphxJZUiGwojB1a/Hd5OiPIqDdXONia6bhTw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.2.tgz",
      "integrity": "sha512-MJt5BRRSScPDwG2hLelYhAAKh9imjHK5+NE/tvnRLbIqUWa+0E9N4WNMjmp/kXXPHZGqPLxggwVhz7QP8CTR8w==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.2.tgz",
      "integrity": "sha512-lugyF1atnAT463aO6KPshVCJK5NgRnU4yb3FUumyVz+cGvZbontBgzeGFO1nF+dPueHD367a2ZXe1NtUkAjOtg==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.2.tgz",
      "integrity": "sha512-nlP2I6ArEBewvJ2gjrrkESEZkB5mIoaTswuqNFRv/WYd+ATtUpe9Y09RnJvgvdag7he0OWgEZWhviS1OTOKixw==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.2.tgz",
      "integrity": "sha512-C92gnpey7tUQONqg1n6dKVbx3vphKtTHJaNG2Ok9lGwbZil6DrfyecMsp9CrmXGQJmZ7iiVXvvZH6Ml5hL6XdQ==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.2.tgz",
      "integrity": "sha512-B5BOmojNtUyN8AXlK0QJyvjEZkWwy/FKvakkTDCziX95AowLZKR6aCDhG7LeF7uMCXEJqwa8Bejz5LTPYm8AvA==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.2.tgz",
      "integrity": "sha512-p4bm9+wsPwup5Z8f4EpfN63qNagQ47Ua2znaqGH6bqLlmJ4bx97Y9JdqxgGZ6Y8xVTixUnEkoKSHcpRlDnNr5w==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.2.tgz",
      "integrity": "sha512-uwp2Tip5aPmH+NRUwTcfLb+W32WXjpFejTIOWZFw/v7/KnpCDKG66u4DLcurQpiYTiYwQ9B7KOeMJvLCu/OvbA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.2.tgz",
      "integrity": "sha512-Kj6DiBlwXrPsCRDeRvGAUb/LNrBASrfqAIok+xB0LxK8CHqxZ037viF13ugfsIpePH93mX7xfJp97cyDuTZ3cw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.2.tgz",
      "integrity": "sha512-HwGDZ0VLVBY3Y+Nw0JexZy9o/nUAWq9MlV7cahpaXKW6TOzfVno3y3/M8Ga8u8Yr7GldLOov27xiCnqRZf0tCA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.27.2.tgz",
      "integrity": "sha512-DNIHH2BPQ5551A7oSHD0CKbwIA/Ox7+78/AWkbS5QoRzaqlev2uFayfSxq68EkonB+IKjiuxBFoV8ESJy8bOHA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.27.2.tgz",
      "integrity": "sha512-/it7w9Nb7+0KFIzjalNJVR5bOzA9Vay+yIPLVHfIQYG/j+j9VTH84aNB8ExGKPU4AzfaEvN9/V4HV+F+vo8OEg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openharmony-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.27.2.tgz",
      "integrity": "sha512-LRBbCmiU51IXfeXk59csuX/aSaToeG7w48nMwA6049Y4J4+VbWALAuXcs+qcD04rHDuSCSRKdmY63sruDS5qag==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.27.2.tgz",
      "integrity": "sha512-kMtx1yqJHTmqaqHPAzKCAkDaKsffmXkPHThSfRwZGyuqyIeBvf08KSsYXl+abf5HDAPMJIPnbBfXvP2ZC2TfHg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.27.2.tgz",
      "integrity": "sha512-Yaf78O/B3Kkh+nKABUF++bvJv5Ijoy9AN1ww904rOXZFLWVc5OLOfL56W+C8F9xn5JQZa3UX6m+IktJnIb1Jjg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.27.2.tgz",
      "integrity": "sha512-Iuws0kxo4yusk7sw70Xa2E2imZU5HoixzxfGCdxwBdhiDgt9vX9VUCBhqcwY7/uh//78A1hMkkROMJq9l27oLQ==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.27.2.tgz",
      "integrity": "sha512-sRdU18mcKf7F+YgheI/zGf5alZatMUTKj/jNS6l744f9u3WFu4v7twcUI9vu4mknF4Y9aDlblIie0IM+5xxaqQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+D
... [TRUNCATED]
```

### File: README_VI.md
```md
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU GPL v3][license-shield]][license-url]

<h1 align="center">
  <img src="src/images/banners/banner.png" alt="TubeTuner Banner" /><br/>
  TubeTuner
</h1>

<h4 align="center">
  <a href="README.md">English</a> |
  <a href="README_VI.md">Tiếng Việt</a>
</h4>

<h3 align="center">Tùy chỉnh giao diện YouTube để loại bỏ các yếu tố gây xao nhãng và tạo trải nghiệm xem tập trung, cá nhân hóa</h3>

<p align="center">
  <a href="https://github.com/PhanKydeptrai/TubeTuner"><strong>Khám phá tài liệu »</strong></a>
  <br /><br />
  <a href="https://github.com/PhanKydeptrai/TubeTuner">Xem Demo</a>
  ·
  <a href="https://github.com/PhanKydeptrai/TubeTuner/issues/new?labels=bug&template=bug-report---.md">Báo Lỗi</a>
  ·
  <a href="https://github.com/PhanKydeptrai/TubeTuner/issues/new?labels=enhancement&template=feature-request---.md">Yêu Cầu Tính Năng</a>
</p>

---

## Mục lục

1. [Tải Tiện Ích Này](#tải-tiện-ích-này)
2. [Về dự án](#về-dự-án)
   - [Xây dựng với](#xây-dựng-với)
3. [Bắt đầu](#bắt-đầu)
   - [Cài đặt](#cài-đặt)
4. [Sử dụng](#sử-dụng)
5. [Đóng góp](#đóng-góp)
6. [Giấy phép](#giấy-phép)
7. [Liên hệ](#liên-hệ)

---

## Tải Tiện Ích Này

[![Chrome Web Store](https://img.shields.io/badge/Chrome_Web_Store-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://chromewebstore.google.com/detail/tubetuner/ekllndjjhcpljlfhfblfcagbdjnjkbco)
[![Firefox Add-ons](https://img.shields.io/badge/Firefox_Add_ons-FF7139?style=for-the-badge&logo=firefoxbrowser&logoColor=white)](https://addons.mozilla.org/vi/firefox/addon/tubetuner/)

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

---

## Về dự án

TubeTuner là một tiện ích mở rộng cho Chrome/Firefox cho phép bạn tùy chỉnh giao diện YouTube theo sở thích của mình. Ẩn các yếu tố gây xao nhãng và tập trung vào nội dung video với 21 tùy chọn ẩn/hiện khác nhau, cộng với các tính năng tiện ích như danh sách thiết lập sẵn (presets) và xuất/nhập (export/import) để sao lưu.

### Có gì mới trong v1.3.9
- **Ẩn Thumbnail (Hide Thumbnails)** — Thêm tùy chọn mới để ẩn thumbnail trên các khu vực hiển thị video của YouTube.
- **Cải Thiện Ẩn Kênh (Hide Channel Improvements)** — Cải thiện khả năng ẩn cụm thông tin kênh bên dưới video, bao gồm tên kênh, avatar và nút đăng ký.
- **Cải Thiện Preset** — Cải thiện quản lý preset tùy chỉnh với khả năng cập nhật preset đã lưu, đổi tên preset và giữ khả năng tương thích với các cài đặt mới được thêm vào.

### Tính Năng

**Điều Khiển Nội Dung & Bảng Tin**
- Ẩn Bảng Tin Màn Hình Chính (Home Feed) — Tránh xao nhãng từ trang chủ YouTube
- Ẩn Thanh Bên Video (Video Sidebar) — Ẩn toàn bộ thanh bên của video (bao gồm trò chuyện trực tiếp, đề xuất và danh sách phát)
  - Ẩn Trò Chuyện Trực Tiếp (Live Chat) — Điều khiển riêng biệt hiển thị trò chuyện trực tiếp
  - Ẩn Đề Xuất Video (Video Suggestions) — Điều khiển riêng biệt hiển thị đề xuất video
  - Ẩn Danh Sách Phát (Playlist) — Điều khiển riêng biệt hiển thị bảng danh sách phát
- Ẩn Bình Luận (Comments) — Ẩn phần bình luận của video
- Ẩn Shorts — Ẩn hoàn toàn các video Shorts và mục Shorts
- Ẩn Thumbnail — Ẩn thumbnail trên các danh sách video và khu vực gợi ý
- Ẩn Channel — Ẩn cụm thông tin kênh dưới video, bao gồm tên kênh, avatar và nút đăng ký
- Ẩn Cửa Hàng (Shop) — Ẩn phần Cửa hàng (Shop) của YouTube

**Yếu Tố Giao Diện**
- Ẩn Tiêu Đề Trên Cùng (Top Header) — Ẩn thanh điều hướng trên cùng
- Ẩn Chuông Thông Báo (Notifications Bell) — Ẩn biểu tượng chuông thông báo
- Ẩn Khám Phá & Thịnh Hành (Explore & Trending) — Ẩn tab Khám phá và Thịnh hành trên thanh bên
- Ẩn Thêm Từ YouTube (More from YouTube) — Ẩn phần "Thêm từ YouTube"
- Ẩn Thanh Nút (Buttons Bar) — Ẩn thanh nút tác vụ dưới video
- Thang Độ Xám (Grayscale) — Áp dụng bộ lọc xám cho toàn bộ giao diện YouTube

**Điều Khiển Video**
- Ẩn Điều Khiển Video — Ẩn bảng điều khiển của trình phát video (bao gồm thanh tiến trình và thời lượng)
  - Ẩn Thanh Tiến Trình (Progress Bar) — Xóa thanh tiến trình khi xem video
  - Ẩn Thời Lượng (Duration) — Ẩn thông tin thời gian hiện tại và tổng thời lượng
- Ẩn Thẻ Màn Hình Cuối (End Screen Cards) — Ẩn các thẻ màn hình xuất hiện ở cuối video
- Ẩn Mô Tả (Description) — Ẩn phần mô tả video
- Ẩn Tóm Tắt AI (AI Summary) — Ẩn phần tóm tắt AI trên trang video

**Các Tính Năng Khác**
- Xuất/Nhập Cài Đặt (Export/Import Settings) — Xuất cài đặt ra một file để sao lưu và nhập lại để khôi phục hoặc chia sẻ cấu hình
- Cài Đặt Sẵn (Presets) — Áp dụng các cài đặt có sẵn (Không, Cân Bằng, Tập Trung), tạo hoặc cập nhật preset tùy chỉnh, đổi tên và xuất/nhập để sao lưu
- Chế Độ Tối (Dark Mode) — Tự động theo giao diện hệ thống của bạn
- Đa Ngôn Ngữ — Hỗ trợ tiếng Việt và tiếng Anh
- Bật/Tắt Tiện Ích — Bật/tắt nhanh tình trạng bật của tiện ích trực tiếp trên popup

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

### Xây dựng với

- [![JavaScript][JavaScript-shield]][JavaScript-url]
- [![HTML5][HTML5-shield]][HTML5-url]
- [![CSS3][CSS3-shield]][CSS3-url]

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

---

## Bắt Đầu

Làm theo các bước sau để thiết lập một bản sao cục bộ của tiện ích.

### Cài Đặt

1. **Clone repository:**
   ```sh
   git clone https://github.com/PhanKydeptrai/TubeTuner.git
   ```

2. **Cài đặt các gói phụ thuộc (dependencies):**
   ```sh
   npm install
   ```

3. **Thiết lập biến môi trường:**
   Sao chép tệp biến môi trường mẫu và cập nhật các giá trị nếu cần:
   ```sh
   cp .env.example .env
   ```

4. **Build tiện ích mở rộng:**

   Cho Chrome:
   ```sh
   npm run build:chrome
   ```

   Cho Firefox:
   ```sh
   npm run build:firefox
   ```

5. **Tải lên Chrome:**
   - Mở `chrome://extensions/`
   - Bật **Chế độ dành cho nhà phát triển (Developer mode)** ở góc trên bên phải
   - Nhấp **Tải tiện ích đã giải nén (Load unpacked)**
   - Chọn thư mục `dist/chrome`

6. **Tải lên Firefox:**
   - Mở `about:debugging#/runtime/this-firefox`
   - Nhấp vào **Load Temporary Add-on...**
   - Chọn bất kỳ tệp nào trong thư mục `dist/firefox` (ví dụ: `manifest.json`)

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

---

## Sử Dụng

1. **Mở YouTube** và bật một video bất kỳ.
2. **Nhấp vào biểu tượng tiện ích** trong thanh công cụ của trình duyệt.
3. **Khám phá 3 phần chính:**
   - **Điều Khiển Nội Dung & Bảng Tin** — Ẩn/hiện Bảng Tin Trang Chủ, Thanh Bên Video (với các nhóm dành cho Trò chuyện trực tiếp, Gợi ý video, Danh sách phát), Bình Luận, Shorts, Thumbnail, Channel, Cửa Hàng
   - **Yếu Tố Giao Diện** — Ẩn/hiện Tiêu Đề Trên Cùng, Chuông Thông Báo, Khám Phá & Thịnh Hành, Thêm Từ YouTube, Thanh Nút, Thang Độ Xám
   - **Điều Khiển Video** — Ẩn/hiện Điều Khiển Video (với các nhóm dành cho Thanh Tiến Trình, Thời Lượng), Thẻ Màn Hình Cuối, Mô Tả, Tóm Tắt AI
4. **Sử dụng các công tắc** để kích hoạt hay vô hiệu hóa từng tính năng riêng biệt.
5. **Chuyển Đổi Giao Diện** — Nhấp vào nút mặt trời/mặt trăng trên cùng để chuyển giữa chế độ Sáng/Tối.
6. **Xuất/Nhập Cài Đặt** — Sử dụng các nút trong phần cài đặt để sao lưu/khôi phục lại cấu hình.
7. **Cài Đặt Sẵn (Presets)** — Chọn một cấu hình có sẵn (Không, Cân Bằng, Tập Trung) để áp dụng nhiều cài đặt cùng lúc.
8. **Cài Đặt Sẵn Tùy Chỉnh** — Cấu hình các công tắc của bạn và nhấp vào "Lưu preset" để tạo một thiết lập có tên riêng. Sau khi thay đổi cài đặt, bạn có thể cập nhật lại preset đang chọn, đổi tên preset, nhập preset từ file `.json`, xuất preset để sao lưu hoặc xóa preset tùy chỉnh đã chọn.

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

---

## Đóng Góp

Những đóng góp chính là động lực làm cho cộng đồng mã nguồn mở trở thành một nơi tuyệt vời để học hỏi, truyền cảm hứng và sáng tạo. Bất kỳ đóng góp nào của bạn cũng đều được **trân trọng và đánh giá cao**.

Nếu bạn có một đề xuất nào, vui lòng fork repository và tạo một pull request, hoặc mở một issue với nhãn `enhancement`. Đừng quên ghé ủng hộ dự án một ngôi sao (star) nhé!

1. Fork dự án
2. Tạo nhánh tính năng của bạn (`git checkout -b feature/AmazingFeature`)
3. Commit những đóng góp của bạn (`git commit -m 'Thêm một AmazingFeature'`)
4. Đẩy (Push) lên nhánh của bạn (`git push origin feature/AmazingFeature`)
5. Mở một Pull Request

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

---

## Giấy Phép

Phân phối theo Giấy phép MIT. Xem chi tiết trong file `LICENSE`.

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

---

## Liên Hệ

Phan Ky — phanky.dev@proton.me

Liên kết Dự án: [https://github.com/PhanKydeptrai/TubeTuner](https://github.com/PhanKydeptrai/TubeTuner)

<p align="right">(<a href="#readme-top">quay lại đầu trang</a>)</p>

---

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[contributors-url]: https://github.com/PhanKydeptrai/TubeTuner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[forks-url]: https://github.com/PhanKydeptrai/TubeTuner/network/members
[stars-shield]: https://img.shields.io/github/stars/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[stars-url]: https://github.com/PhanKydeptrai/TubeTuner/stargazers
[issues-shield]: https://img.shields.io/github/issues/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[issues-url]: https://github.com/PhanKydeptrai/TubeTuner/issues
[license-shield]: https://img.shields.io/github/license/PhanKydeptrai/TubeTuner.svg?style=for-the-badge
[license-url]: https://github.com/PhanKydeptrai/TubeTuner/blob/main/LICENSE
[JavaScript-shield]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[HTML5-shield]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5
[CSS3-shield]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://developer.mozilla.org/en-US/docs/Web/CSS

```

### File: vite.config.js
```js
import { defineConfig } from 'vite';
import { crx } from '@crxjs/vite-plugin';
import manifestBase from './src/manifest.json';
import { resolve } from 'path';
import fs from 'fs';

export default defineConfig(({ mode }) => {
  const isFirefox = mode === 'firefox';

  const manifest = { ...manifestBase };

  if (isFirefox) {
    manifest.browser_specific_settings = {
      gecko: {
        id: "{8aec21ca-47ea-4ca1-b62f-068fb3ec4069}",
        strict_min_version: "112.0",
        data_collection_permissions: {
          required: ["none"]
        }
      }
    };
    manifest.background = {
      scripts: ["background.js"],
      type: "module"
    };
  }

  return {
    base: './',
    root: resolve(__dirname, 'src'), // Set the root of the source code to the src directory
    envDir: resolve(__dirname), // Load .env from project root
    build: {
      target: 'es2015',
      outDir: resolve(__dirname, isFirefox ? 'dist/firefox' : 'dist/chrome'),
      emptyOutDir: true,
      rollupOptions: {
        input: {
          popup: resolve(__dirname, 'src/popup.html'),
        },
      },
    },
    plugins: [
      {
        name: 'copy-css',
        generateBundle() {
          const stylesCss = fs.readFileSync(resolve(__dirname, 'src/styles.css'), 'utf-8');
          this.emitFile({
            type: 'asset',
            fileName: 'styles.css',
            source: stylesCss
          });
        }
      },
      crx({ manifest }),
    ],
  };
});
```

### File: src\background.js
```js
(function () {
    'use strict';

    // Constants (replace with production URLs when ready)
    const WELCOME_URL = import.meta.env.VITE_WELCOME_URL;
    const UNINSTALL_FEEDBACK_URL = import.meta.env.VITE_UNINSTALL_FEEDBACK_URL;

    chrome.storage.onChanged.addListener((changes, namespace) => {
        if (namespace !== 'local') return;

        chrome.tabs.query({ url: ['*://www.youtube.com/*', '*://youtube.com/*'] }, (tabs) => {
            if (tabs.length === 0) return;

            const syncMessage = {
                action: 'syncSettings',
                changes: {}
            };

            for (const [key, change] of Object.entries(changes)) {
                if (['language', 'theme', 'sectionStates', 'welcomeShown', 'initialRefreshNoticePending'].includes(key)) {
                    continue;
                }
                syncMessage.changes[key] = change.newValue;
            }

            if (Object.keys(syncMessage.changes).length > 0) {
                tabs.forEach(tab => {
                    chrome.tabs.sendMessage(tab.id, syncMessage).catch(() => {
                        // Ignore errors for tabs that might not have content script loaded yet
                    });
                });
            }
        });
    });

    chrome.runtime.onInstalled.addListener(async (details) => {
        try {
            await chrome.runtime.setUninstallURL(UNINSTALL_FEEDBACK_URL);
            console.log('Uninstall URL set:', UNINSTALL_FEEDBACK_URL);
        } catch (e) {
            console.warn('setUninstallURL failed:', e);
        }

        if (details?.reason === 'install') {
            try {
                const { welcomeShown } = await chrome.storage.local.get('welcomeShown');
                await chrome.storage.local.set({ initialRefreshNoticePending: true });
                if (!welcomeShown) {
                    await chrome.tabs.create({ url: WELCOME_URL });
                    await chrome.storage.local.set({ welcomeShown: true });
                }
            } catch (e) {
                console.warn('Welcome flow failed:', e);
            }
        }
    });

    chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
        if (request.action === 'syncToAllTabs') {
            chrome.tabs.query({ url: ['*://www.youtube.com/*', '*://youtube.com/*'] }, (tabs) => {
                const message = {
                    action: request.toggleAction,
                    enabled: request.enabled
                };

                tabs.forEach(tab => {
                    if (sender.tab && sender.tab.id === tab.id) return;
                    chrome.tabs.sendMessage(tab.id, message).catch(() => { });
                });
            });

            sendResponse({ success: true });
        }

        return true; // Keep message channel open for async response
    });

    chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
        if (changeInfo.status === 'complete' &&
            tab.url &&
            tab.url.includes('youtube.com')) {

            chrome.storage.local.get([
                'extensionEnabled', 'progressBarHidden', 'durationHidden', 'shortsHidden',
                'homeFeedHidden', 'videoSidebarHidden', 'commentsHidden',
                'notificationsBellHidden', 'topHeaderHidden', 'exploreSectionHidden',
                'endScreenCardsHidden', 'moreFromYouTubeHidden', 'hideChannelHidden',
                'buttonsBarHidden', 'hideDescriptionHidden', 'grayscaleEnabled',
                'shopHidden', 'playlistHidden', 'livechatHidden', 'recommendationHidden',
                'aiSummaryHidden'
            ], (settings) => {
                const syncMessage = {
                    action: 'syncSettings',
                    changes: settings,
                    isInitialSync: true
                };

                // Wait a bit for content script to load
                setTimeout(() => {
                    chrome.tabs.sendMessage(tabId, syncMessage).catch(() => { });
                }, 1000);
            });
        }
    });

})();

```

### File: src\content.js
```js
import * as features from './features/index.js';

// Configuration registry for all features
// Maps the action name (from messages) to the settings key and the toggle function
const featureRegistry = [
    { action: 'toggleProgressBar', key: 'progressBarHidden', func: features.toggleProgressBar },
    { action: 'toggleDuration', key: 'durationHidden', func: features.toggleDuration },
    { action: 'toggleShorts', key: 'shortsHidden', func: features.toggleShorts },
    { action: 'toggleHomeFeed', key: 'homeFeedHidden', func: features.toggleHomeFeed },
    { action: 'toggleVideoSidebar', key: 'videoSidebarHidden', func: features.toggleVideoSidebar },
    { action: 'toggleComments', key: 'commentsHidden', func: features.toggleComments },
    { action: 'toggleNotificationsBell', key: 'notificationsBellHidden', func: features.toggleNotificationsBell },
    { action: 'toggleTopHeader', key: 'topHeaderHidden', func: features.toggleTopHeader },
    { action: 'toggleExploreSection', key: 'exploreSectionHidden', func: features.toggleExploreSection },
    { action: 'toggleEndScreenCards', key: 'endScreenCardsHidden', func: features.toggleEndScreenCards },
    { action: 'toggleMoreFromYouTube', key: 'moreFromYouTubeHidden', func: features.toggleMoreFromYouTube },
    { action: 'toggleHideChannel', key: 'hideChannelHidden', func: features.toggleHideChannel },
    { action: 'toggleButtonsBar', key: 'buttonsBarHidden', func: features.toggleButtonsBar },
    { action: 'toggleHideDescription', key: 'hideDescriptionHidden', func: features.toggleHideDescription },
    { action: 'toggleGrayscale', key: 'grayscaleEnabled', func: features.toggleGrayscale },
    { action: 'toggleShop', key: 'shopHidden', func: features.toggleShop },
    { action: 'togglePlaylist', key: 'playlistHidden', func: features.togglePlaylist },
    { action: 'toggleLivechat', key: 'livechatHidden', func: features.toggleLivechat },
    { action: 'toggleRecommendation', key: 'recommendationHidden', func: features.toggleRecommendation },
    { action: 'toggleAiSummary', key: 'aiSummaryHidden', func: features.toggleAiSummary },
    { action: 'toggleHideThumbnail', key: 'hideThumbnailHidden', func: features.toggleHideThumbnail }
];

const actionMap = {};
const keyMap = {};

featureRegistry.forEach(item => {
    actionMap[item.action] = item;
    keyMap[item.key] = item;
});

let settings = {
    extensionEnabled: true,
    // Other keys will be populated dynamically
};

featureRegistry.forEach(item => {
    settings[item.key] = false;
});

function applyAllToggles() {
    featureRegistry.forEach(({ key, func }) => {
        const isEnabled = settings.extensionEnabled ? settings[key] : false;
        func(isEnabled);
    });
}

function reapplyHiddens() {
    if (settings.extensionEnabled) {
        featureRegistry.forEach(({ key, func }) => {
            if (settings[key]) {
                func(true);
            }
        });
    }
}

function initialize() {
    const keysToFetch = ['extensionEnabled', ...featureRegistry.map(item => item.key)];

    chrome.storage.local.get(keysToFetch, (result) => {
        // extensionEnabled defaults to true if undefined (undefined !== false is true)
        settings.extensionEnabled = result.extensionEnabled !== false;

        featureRegistry.forEach(({ key }) => {
            settings[key] = result[key] === true;
        });

        if (settings.extensionEnabled) {
            applyAllToggles();
        }
    });

    let currentUrl = location.href;
    const urlObserver = new MutationObserver(() => {
        if (location.href !== currentUrl) {
            currentUrl = location.href;
            if (settings.extensionEnabled) {
                reapplyHiddens();
            }
        }
    });

    urlObserver.observe(document, {
        subtree: true,
        childList: true
    });
}

chrome.storage.onChanged.addListener((changes, namespace) => {
    if (namespace !== 'local') return;

    for (const [key, change] of Object.entries(changes)) {
        const newValue = change.newValue;
        if (key === 'extensionEnabled') {
            settings.extensionEnabled = newValue !== false;
        } else if (keyMap[key]) {
            // It's a known feature key
            settings[key] = newValue === true;
        }
    }

    applyAllToggles();
});

chrome.runtime.onMessage.addListener((request, _sender, sendResponse) => {
    if (request.action === 'syncSettings') {
        for (const [key, value] of Object.entries(request.changes)) {
            if (key === 'extensionEnabled') {
                settings.extensionEnabled = value !== false;
            } else if (keyMap[key]) {
                settings[key] = value === true;
            }
        }
        applyAllToggles();
        sendResponse({ success: true });
        return true;
    } else if (request.action === 'getStatus') {
        sendResponse(settings);
        return true;
    }

    const actionEntry = actionMap[request.action];
    if (actionEntry) {
        const { key, func } = actionEntry;
        settings[key] = request.enabled;
        func(request.enabled);
        sendResponse({ success: true, willRefresh: false });
        return true;
    }

    return true;
});

initialize();
```

### File: src\interface.css
```css
/* YouTube Controller Extension Design System CSS */
:root {
  /* Color Palette */
  --primary-blue: #1a73e8;
  --warning-red: #E74C3C;
  --warning-background: #FEF2F2;
  --radius: 0.5rem;
  --background: oklch(0.9779 0.0042 56.3756);
  --foreground: oklch(0.2178 0 0);
  --card: oklch(0.9779 0.0042 56.3756);
  --card-foreground: oklch(0.2178 0 0);
  --popover: oklch(0.9779 0.0042 56.3756);
  --popover-foreground: oklch(0.2178 0 0);
  --primary: oklch(0.4650 0.1470 24.9381);
  --primary-foreground: oklch(1.0000 0 0);
  --secondary: oklch(0.9625 0.0385 89.0943);
  --secondary-foreground: oklch(0.4847 0.1022 75.1153);
  --muted: oklch(0.9431 0.0068 53.4442);
  --muted-foreground: oklch(0.4444 0.0096 73.6390);
  --accent: oklch(0.9619 0.0580 95.6174);
  --accent-foreground: oklch(0.3958 0.1331 25.7230);
  --destructive: oklch(0.4437 0.1613 26.8994);
  --destructive-foreground: oklch(1.0000 0 0);
  --border: oklch(0.9355 0.0324 80.9937);
  --input: oklch(0.9355 0.0324 80.9937);
  --ring: oklch(0.4650 0.1470 24.9381);
  --chart-1: oklch(0.5054 0.1905 27.5181);
  --chart-2: oklch(0.4650 0.1470 24.9381);
  --chart-3: oklch(0.3958 0.1331 25.7230);
  --chart-4: oklch(0.5553 0.1455 48.9975);
  --chart-5: oklch(0.4732 0.1247 46.2007);
  --sidebar: oklch(0.9431 0.0068 53.4442);
  --sidebar-foreground: oklch(0.2178 0 0);
  --sidebar-primary: oklch(0.4650 0.1470 24.9381);
  --sidebar-primary-foreground: oklch(1.0000 0 0);
  --sidebar-accent: oklch(0.9619 0.0580 95.6174);
  --sidebar-accent-foreground: oklch(0.3958 0.1331 25.7230);
  --sidebar-border: oklch(0.9355 0.0324 80.9937);
  --sidebar-ring: oklch(0.4650 0.1470 24.9381);
  --font-sans: Poppins, sans-serif;
  --font-serif: Libre Baskerville, serif;
  --font-mono: IBM Plex Mono, monospace;
  --shadow-x: 1px;
  --shadow-y: 1px;
  --shadow-blur: 16px;
  --shadow-spread: -2px;
  --shadow-opacity: 0.12;
  --shadow-color: hsl(0 63% 18%);
  --shadow-2xs: 1px 1px 16px -2px hsl(0 63% 18% / 0.06);
  --shadow-xs: 1px 1px 16px -2px hsl(0 63% 18% / 0.06);
  --shadow-sm: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 1px 2px -3px hsl(0 63% 18% / 0.12);
  --shadow: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 1px 2px -3px hsl(0 63% 18% / 0.12);
  --shadow-md: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 2px 4px -3px hsl(0 63% 18% / 0.12);
  --shadow-lg: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 4px 6px -3px hsl(0 63% 18% / 0.12);
  --shadow-xl: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 8px 10px -3px hsl(0 63% 18% / 0.12);
  --shadow-2xl: 1px 1px 16px -2px hsl(0 63% 18% / 0.30);
  --tracking-normal: 0em;
  --spacing: 0.25rem;
  --icon-blue: #1a73e8;
  --icon-purple: #9C27B0;
  --icon-orange: #FF9800;
  --icon-green: #4CAF50;

  /* Typography */
  --font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semi-bold: 600;
  --font-size-header: 20px;
  --font-size-section: 16px;
  --font-size-body: 14px;
  --font-size-caption: 12px;
  --line-height-tight: 1.2;
  --line-height-normal: 1.4;
  --line-height-relaxed: 1.6;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;

  /* Layout */
  --container-max-width: 400px;
  --container-padding: 16px;
  --header-height: 80px;
  --border-radius: 12px;
}

/* Disable ALL transitions and animations during initial popup load */
body.no-transitions,
body.no-transitions *,
body.no-transitions *::before,
body.no-transitions *::after {
  transition: none !important;
  animation: none !important;
}

/* Dark Mode Variables */
.dark {
  --primary-blue: #4285F4;
  --background: oklch(0.2161 0.0061 56.0434);
  --foreground: oklch(0.9699 0.0013 106.4238);
  --card: oklch(0.2685 0.0063 34.2976);
  --card-foreground: oklch(0.9699 0.0013 106.4238);
  --popover: oklch(0.2685 0.0063 34.2976);
  --popover-foreground: oklch(0.9699 0.0013 106.4238);
  --primary: oklch(0.5054 0.1905 27.5181);
  --primary-foreground: oklch(0.9779 0.0042 56.3756);
  --secondary: oklch(0.4732 0.1247 46.2007);
  --secondary-foreground: oklch(0.9619 0.0580 95.6174);
  --muted: oklch(0.2291 0.0060 56.0708);
  --muted-foreground: oklch(0.8687 0.0043 56.3660);
  --accent: oklch(0.5553 0.1455 48.9975);
  --accent-foreground: oklch(0.9619 0.0580 95.6174);
  --destructive: oklch(0.6368 0.2078 25.3313);
  --destructive-foreground: oklch(1.0000 0 0);
  --border: oklch(0.3741 0.0087 67.5582);
  --input: oklch(0.3741 0.0087 67.5582);
  --ring: oklch(0.5054 0.1905 27.5181);
  --chart-1: oklch(0.7106 0.1661 22.2162);
  --chart-2: oklch(0.6368 0.2078 25.3313);
  --chart-3: oklch(0.5771 0.2152 27.3250);
  --chart-4: oklch(0.8369 0.1644 84.4286);
  --chart-5: oklch(0.7686 0.1647 70.0804);
  --sidebar: oklch(0.2161 0.0061 56.0434);
  --sidebar-foreground: oklch(0.9699 0.0013 106.4238);
  --sidebar-primary: oklch(0.5054 0.1905 27.5181);
  --sidebar-primary-foreground: oklch(0.9779 0.0042 56.3756);
  --sidebar-accent: oklch(0.5553 0.1455 48.9975);
  --sidebar-accent-foreground: oklch(0.9619 0.0580 95.6174);
  --sidebar-border: oklch(0.3741 0.0087 67.5582);
  --sidebar-ring: oklch(0.5054 0.1905 27.5181);
  --font-sans: Poppins, sans-serif;
  --font-serif: Libre Baskerville, serif;
  --font-mono: IBM Plex Mono, monospace;
  --shadow-x: 1px;
  --shadow-y: 1px;
  --shadow-blur: 16px;
  --shadow-spread: -2px;
  --shadow-opacity: 0.12;
  --shadow-color: hsl(0 63% 18%);
  --shadow-2xs: 1px 1px 16px -2px hsl(0 63% 18% / 0.06);
  --shadow-xs: 1px 1px 16px -2px hsl(0 63% 18% / 0.06);
  --shadow-sm: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 1px 2px -3px hsl(0 63% 18% / 0.12);
  --shadow: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 1px 2px -3px hsl(0 63% 18% / 0.12);
  --shadow-md: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 2px 4px -3px hsl(0 63% 18% / 0.12);
  --shadow-lg: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 4px 6px -3px hsl(0 63% 18% / 0.12);
  --shadow-xl: 1px 1px 16px -2px hsl(0 63% 18% / 0.12), 1px 8px 10px -3px hsl(0 63% 18% / 0.12);
  --shadow-2xl: 1px 1px 16px -2px hsl(0 63% 18% / 0.30);
  --warning-background: #3A2A2A;
}

/* Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border-color: hsl(var(--border));
}

body {
  font-family: var(--font-sans);
  background-color: var(--background);
  color: var(--foreground);
  line-height: var(--line-height-normal);
  font-size: var(--font-size-body);
  width: var(--container-max-width);
  margin: 0 auto;
  padding: var(--container-padding);
  transition: background-color 0.2s, color 0.2s;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 5px;
  border: 2px solid var(--background);
}

::-webkit-scrollbar-thumb:hover {
  background: var(--muted-foreground);
}

/* Dark mode scrollbar */
.dark ::-webkit-scrollbar-thumb {
  background: var(--border);
  border: 2px solid var(--background);
}

.dark ::-webkit-scrollbar-thumb:hover {
  background: var(--muted-foreground);
}

/* Container */
.container {
  width: 100%;
  background-color: var(--background);
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

/* Header Component */
.header {
  height: var(--header-height);
  background: var(--primary-blue);
  padding: var(--space-md);
  border-radius: 0;
  color: white;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}

.header-left {
  display: flex;
  align-items: center;
  gap: var(--space-md);
}

.header-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
}

.header-text {
  display: flex;
  flex-direction: column;
}

.title {
  font-size: var(--font-size-header);
  font-weight: var(--font-weight-semi-bold);
  margin-bottom: var(--space-xs);
  line-height: var(--line-height-tight);
}

.subtitle {
  font-size: var(--font-size-caption);
  opacity: 0.9;
  line-height: var(--line-height-tight);
}

.header-controls {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
}

/* Utility Buttons */
.utility-button {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  padding: var(--space-sm);
  transition: all 0.2s ease;
}

.utility-button:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

/* Language Button */
.lang-button {
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0 var(--space-md);
  height: 36px;
  font-weight: var(--font-weight-medium);
  font-size: var(--font-size-body);
  cursor: pointer;
  transition: all 0.2s ease;
}

.lang-button:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

/* Theme Toggle */
.theme-toggle {
  position: relative;
  background-color: var(--primary);
  color: var(--primary-foreground);
  border: 1px solid var(--border);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.theme-toggle .sun-icon,
.theme-toggle .moon-icon {
  position: absolute;
  transition: opacity 0.3s, transform 0.5s;
}

.theme-toggle .sun-icon {
  opacity: 1;
  transform: scale(1);
}

.theme-toggle .moon-icon {
  opacity: 0;
  transform: scale(0.5);
}

.dark .theme-toggle {
  background-color: var(--secondary);
  color: var(--secondary-foreground);
}

.dark .theme-toggle .sun-icon {
  opacity: 0;
  transform: scale(0.5);
}

.dark .theme-toggle .moon-icon {
  opacity: 1;
  transform: scale(1);
}

/* Language Selector */
.language-selector {
  display: flex;
  gap: 2px;
}

.lang-option {
  padding: 4px 8px;
  font-size: var(--font-size-caption);
  font-weight: var(--font-weight-semi-bold);
  background-color: transparent;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.lang-option:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.lang-option.active {
  background-color: white;
  color: var(--primary-blue);
}

/* Content Area */
.content-area {
  padding: var(--space-md);
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}

/* Notice Card */
.notice-card {
  background-color: var(--warning-background);
  border: none;
  border-radius: var(--border-radius);
  padding: var(--space-md);
  display: flex;
  gap: var(--space-md);
  align-items: flex-start;
}

.notice-icon {
  color: var(--warning-red);
  flex-shrink: 0;
}

.notice-content {
  flex: 1;
}

.notice-title {
  font-size: var(--font-size-section);
  font-weight: var(--font-weight-medium);
  margin-bottom: var(--space-xs);
  color: var(--warning-red);
}

.notice-description {
  font-size: var(--font-size-body);
  color: var(--text-primary);
}

/* Collapsible Section */
.collapsible-section {
  background-color: var(--card-background);
  border: none;
  border-radius: var(--border-radius);
  margin-bottom: var(--space-sm);
  overflow: hidden;
  transition: box-shadow 0.3s, transform 0.3s;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.collapsible-section:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.section-header {
  padding: var(--space-md);
  display: flex;
  align-items: center;
  cursor: pointer;
}

.section-icon {
  margin-right: var(--space-md);
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.content-icon {
  background-color: #4285F4;
}

.interface-icon {
  background-color: transparent;
}

.video-icon {
  background-color: transparent;
}

.content-icon {
  background-color: transparent;
}

.other-icon {
  background-color: transparent;
}

.features-icon {
  background-color: #4285F4;
}

.section-title {
  flex: 1;
  font-size: var(--font-size-section);
  font-weight: var(--font-weight-medium);
}

.section-chevron {
  transition: transform 0.3s;
}

.collapsible-section.expanded .section-chevron {
  transform: rotate(180deg);
}

.section-content {
  padding: 0 var(--space-md) var(--space-md);
  display: none;
}

.collapsible-section.expanded .section-content {
  display: block;
}

/* Control Item */
.control-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-sm) 0;
  border-bottom: 1px solid var(--border);
}

.control-item:last-child {
  border-bottom: none;
}

.control-label {
  font-size: var(--font-size-body);
}

/* Switch */
.switch {
  position: relative;
  width: 44px;
  height: 24px;
}

.switch-input {
  opacity: 0;
  width: 0;
  height: 0;
}

.switch-label {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 24px;
}

.switch-label:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

.switch-input:checked+.switch-label {
  background-color: var(--primary-blue);
}

.switch-input:checked+.switch-label:before {
  transform: translateX(20px);
}

.switch-input:focus+.switch-label {
  box-shadow: 0 0 1px var(--primary-blue);
}

/* Status Badge */
.status-badge {
  display: flex;
  justify-content: center;
  margin-top: var(--space-sm);
}

.badge {
  display: inline-block;
  padding: var(--space-xs) var(--space-md);
  border-radius: 16px;
  font-size: var(--font-size-caption);
  font-weight: var(--font-weight-medium);
}

.badge.success {
  background-color: rgba(76, 175, 80, 0.1);
  color: var(--icon-green);
  border: 1px solid rgba(76, 175, 80, 0.3);
}

.badge.warning {
  background-color: rgba(255, 152, 0, 0.1);
  color: var(--icon-orange);
  border: 1px solid rgba(255, 152, 0, 0.3);
}

/* Animations */
@keyframes slideInRight {
  from {
    transform: translateX(20px);
    opacity: 0;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideInUp {
  from {
    transform: translateY(15px);
    opacity: 0;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Responsive Behavior */
@media (max-width: 480px) {
  body {
    padding: var(--space-sm);
  }

  .header-left {
    gap: var(--space-sm);
  }

  .header-controls {
    gap: var(--space-xs);
  }

  .utility-button,
  .lang-button {
    height: 32px;
  }
}

/* prevent zoomed-out view */
@media (max-width: 480px) and (pointer: coarse) {
  body {
    width: 100%;
    max-width: var(--container-max-width);
  }
}

/* Focus States for Accessibility */
button:focus,
.switch-input:focus+.switch-label {
  outline: 2px solid var(--primary-blue);
  outline-offset: 2px;
}

/* Extension specific styles with ext- prefix */
.ext-container {
  width: 100%;
}

/* Header styles */
.ext-header {
  border-bottom: 1px so
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
