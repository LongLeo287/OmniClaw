---
id: metube
type: knowledge
owner: OA_Triage
---
# metube
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^17.2.3",
    "express": "^5.1.0",
    "node-fetch": "^3.3.2"
  }
}

```

### File: README.md
```md

Chrome MeTube Downloader
=======

Use the context menu to send YouTube video into [MeTube](https://github.com/alexta69/metube)

![example](https://github.com/Rpsl/metube-browser-extension/blob/master/attach/metube-dowloader.gif?raw=true)

Installation from store
-----

- Install from [Google Chrome Webstore](https://chrome.google.com/webstore/detail/metube-downloader/fbmkmdnlhacefjljljlbhkodfmfkijdh)

Installation from sources
-----
- Download this repository
- Open "[Extensions](chrome://extensions/)" tab `chrome://extensions/`
- Turn On "developer mode" in top right corner
- Click "Load unpacked extension"
- Choose `src` folder



```

### File: app\main.py
```py
#!/usr/bin/env python3
# pylint: disable=no-member,method-hidden

import os
import sys
import asyncio
from pathlib import Path
from aiohttp import web
from aiohttp.log import access_logger
import ssl
import socket
import socketio
import logging
import json
import pathlib
import re
from watchfiles import DefaultFilter, Change, awatch

from ytdl import DownloadQueueNotifier, DownloadQueue, Download
from subscriptions import SubscriptionManager, SubscriptionNotifier, SubscriptionInfo
from yt_dlp.version import __version__ as yt_dlp_version

log = logging.getLogger('main')

def parseLogLevel(logLevel):
    if not isinstance(logLevel, str):
        return None
    return getattr(logging, logLevel.upper(), None)

# Configure logging before Config() uses it so early messages are not dropped.
# Only configure if no handlers are set (avoid clobbering hosting app settings).
if not logging.getLogger().hasHandlers():
    logging.basicConfig(level=parseLogLevel(os.environ.get('LOGLEVEL', 'INFO')) or logging.INFO)

class Config:
    _DEFAULTS = {
        'DOWNLOAD_DIR': '.',
        'AUDIO_DOWNLOAD_DIR': '%%DOWNLOAD_DIR',
        'TEMP_DIR': '%%DOWNLOAD_DIR',
        'DOWNLOAD_DIRS_INDEXABLE': 'false',
        'CUSTOM_DIRS': 'true',
        'CREATE_CUSTOM_DIRS': 'true',
        'CUSTOM_DIRS_EXCLUDE_REGEX': r'(^|/)[.@].*$',
        'DELETE_FILE_ON_TRASHCAN': 'false',
        'STATE_DIR': '.',
        'URL_PREFIX': '',
        'PUBLIC_HOST_URL': 'download/',
        'PUBLIC_HOST_AUDIO_URL': 'audio_download/',
        'OUTPUT_TEMPLATE': '%(title)s.%(ext)s',
        'OUTPUT_TEMPLATE_CHAPTER': '%(title)s - %(section_number)02d - %(section_title)s.%(ext)s',
        'OUTPUT_TEMPLATE_PLAYLIST': '%(playlist_title)s/%(title)s.%(ext)s',
        'OUTPUT_TEMPLATE_CHANNEL': '%(channel)s/%(title)s.%(ext)s',
        'DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT' : '0',
        'SUBSCRIPTION_DEFAULT_CHECK_INTERVAL': '60',
        'SUBSCRIPTION_SCAN_PLAYLIST_END': '50',
        'SUBSCRIPTION_MAX_SEEN_IDS': '50000',
        'CLEAR_COMPLETED_AFTER': '0',
        'YTDL_OPTIONS': '{}',
        'YTDL_OPTIONS_FILE': '',
        'YTDL_OPTIONS_PRESETS': '{}',
        'YTDL_OPTIONS_PRESETS_FILE': '',
        'ALLOW_YTDL_OPTIONS_OVERRIDES': 'false',
        'ROBOTS_TXT': '',
        'HOST': '0.0.0.0',
        'PORT': '8081',
        'HTTPS': 'false',
        'CERTFILE': '',
        'KEYFILE': '',
        'BASE_DIR': '',
        'DEFAULT_THEME': 'auto',
        'MAX_CONCURRENT_DOWNLOADS': '3',
        'LOGLEVEL': 'INFO',
        'ENABLE_ACCESSLOG': 'false',
    }

    _BOOLEAN = ('DOWNLOAD_DIRS_INDEXABLE', 'CUSTOM_DIRS', 'CREATE_CUSTOM_DIRS', 'DELETE_FILE_ON_TRASHCAN', 'HTTPS', 'ENABLE_ACCESSLOG', 'ALLOW_YTDL_OPTIONS_OVERRIDES')

    def __init__(self):
        for k, v in self._DEFAULTS.items():
            setattr(self, k, os.environ.get(k, v))

        for k, v in self.__dict__.items():
            if isinstance(v, str) and v.startswith('%%'):
                setattr(self, k, getattr(self, v[2:]))
            if k in self._BOOLEAN:
                if v not in ('true', 'false', 'True', 'False', 'on', 'off', '1', '0'):
                    log.error(f'Environment variable "{k}" is set to a non-boolean value "{v}"')
                    sys.exit(1)
                setattr(self, k, v in ('true', 'True', 'on', '1'))

        if not self.URL_PREFIX.endswith('/'):
            self.URL_PREFIX += '/'

        # Convert relative addresses to absolute addresses to prevent the failure of file address comparison
        if self.YTDL_OPTIONS_FILE and self.YTDL_OPTIONS_FILE.startswith('.'):
            self.YTDL_OPTIONS_FILE = str(Path(self.YTDL_OPTIONS_FILE).resolve())
        if self.YTDL_OPTIONS_PRESETS_FILE and self.YTDL_OPTIONS_PRESETS_FILE.startswith('.'):
            self.YTDL_OPTIONS_PRESETS_FILE = str(Path(self.YTDL_OPTIONS_PRESETS_FILE).resolve())

        self._runtime_overrides = {}

        success,_ = self.load_ytdl_options()
        if not success:
            sys.exit(1)
        success,_ = self.load_ytdl_option_presets()
        if not success:
            sys.exit(1)

    def set_runtime_override(self, key, value):
        self._runtime_overrides[key] = value
        self.YTDL_OPTIONS[key] = value

    def remove_runtime_override(self, key):
        self._runtime_overrides.pop(key, None)
        self.YTDL_OPTIONS.pop(key, None)

    def _apply_runtime_overrides(self):
        self.YTDL_OPTIONS.update(self._runtime_overrides)

    # Keys sent to the browser. Sensitive or server-only keys (YTDL_OPTIONS,
    # paths, TLS config, etc.) are intentionally excluded.
    _FRONTEND_KEYS = (
        'CUSTOM_DIRS',
        'CREATE_CUSTOM_DIRS',
        'OUTPUT_TEMPLATE_CHAPTER',
        'PUBLIC_HOST_URL',
        'PUBLIC_HOST_AUDIO_URL',
        'DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT',
        'SUBSCRIPTION_DEFAULT_CHECK_INTERVAL',
        'ALLOW_YTDL_OPTIONS_OVERRIDES',
    )

    def frontend_safe(self) -> dict:
        """Return only the config keys that are safe to expose to browser clients.

        Sensitive or server-only keys (YTDL_OPTIONS, file-system paths, TLS
        settings, etc.) are intentionally excluded.
        """
        return {k: getattr(self, k) for k in self._FRONTEND_KEYS}

    def load_ytdl_options(self) -> tuple[bool, str]:
        try:
            self.YTDL_OPTIONS = json.loads(os.environ.get('YTDL_OPTIONS', '{}'))
            assert isinstance(self.YTDL_OPTIONS, dict)
        except (json.decoder.JSONDecodeError, AssertionError):
            msg = 'Environment variable YTDL_OPTIONS is invalid'
            log.error(msg)
            return (False, msg)

        if not self.YTDL_OPTIONS_FILE:
            self._apply_runtime_overrides()
            return (True, '')

        log.info(f'Loading yt-dlp custom options from "{self.YTDL_OPTIONS_FILE}"')
        if not os.path.exists(self.YTDL_OPTIONS_FILE):
            msg = f'File "{self.YTDL_OPTIONS_FILE}" not found'
            log.error(msg)
            return (False, msg)
        try:
            with open(self.YTDL_OPTIONS_FILE) as json_data:
                opts = json.load(json_data)
            assert isinstance(opts, dict)
        except (json.decoder.JSONDecodeError, AssertionError):
            msg = 'YTDL_OPTIONS_FILE contents is invalid'
            log.error(msg)
            return (False, msg)

        self.YTDL_OPTIONS.update(opts)
        self._apply_runtime_overrides()
        return (True, '')

    def load_ytdl_option_presets(self) -> tuple[bool, str]:
        try:
            self.YTDL_OPTIONS_PRESETS = json.loads(os.environ.get('YTDL_OPTIONS_PRESETS', '{}'))
            assert isinstance(self.YTDL_OPTIONS_PRESETS, dict)
            assert all(isinstance(name, str) and isinstance(options, dict) for name, options in self.YTDL_OPTIONS_PRESETS.items())
        except (json.decoder.JSONDecodeError, AssertionError):
            msg = 'Environment variable YTDL_OPTIONS_PRESETS is invalid'
            log.error(msg)
            return (False, msg)

        if not self.YTDL_OPTIONS_PRESETS_FILE:
            return (True, '')

        log.info(f'Loading yt-dlp option presets from "{self.YTDL_OPTIONS_PRESETS_FILE}"')
        if not os.path.exists(self.YTDL_OPTIONS_PRESETS_FILE):
            msg = f'File "{self.YTDL_OPTIONS_PRESETS_FILE}" not found'
            log.error(msg)
            return (False, msg)
        try:
            with open(self.YTDL_OPTIONS_PRESETS_FILE) as json_data:
                opts = json.load(json_data)
            assert isinstance(opts, dict)
            assert all(isinstance(name, str) and isinstance(options, dict) for name, options in opts.items())
        except (json.decoder.JSONDecodeError, AssertionError):
            msg = 'YTDL_OPTIONS_PRESETS_FILE contents is invalid'
            log.error(msg)
            return (False, msg)

        self.YTDL_OPTIONS_PRESETS.update(opts)
        return (True, '')

config = Config()
# Align root logger level with Config (keeps a single source of truth).
# This re-applies the log level after Config loads, in case LOGLEVEL was
# overridden by config file settings or differs from the environment variable.
logging.getLogger().setLevel(parseLogLevel(str(config.LOGLEVEL)) or logging.INFO)

class ObjectSerializer(json.JSONEncoder):
    def default(self, obj):
        # First try to use __dict__ for custom objects
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        # Convert iterables (generators, dict_items, etc.) to lists
        # Exclude strings and bytes which are also iterable
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
            try:
                return list(obj)
            except Exception:
                pass
        # Fall back to default behavior
        return json.JSONEncoder.default(self, obj)

serializer = ObjectSerializer()
app = web.Application()
sio = socketio.AsyncServer(cors_allowed_origins='*')
sio.attach(app, socketio_path=config.URL_PREFIX + 'socket.io')
routes = web.RouteTableDef()
VALID_SUBTITLE_FORMATS = {'srt', 'txt', 'vtt', 'ttml', 'sbv', 'scc', 'dfxp'}
VALID_SUBTITLE_MODES = {'auto_only', 'manual_only', 'prefer_manual', 'prefer_auto'}
SUBTITLE_LANGUAGE_RE = re.compile(r'^[A-Za-z0-9][A-Za-z0-9-]{0,34}$')
VALID_DOWNLOAD_TYPES = {'video', 'audio', 'captions', 'thumbnail'}
VALID_VIDEO_CODECS = {'auto', 'h264', 'h265', 'av1', 'vp9'}
VALID_VIDEO_FORMATS = {'any', 'mp4', 'ios'}
VALID_AUDIO_FORMATS = {'m4a', 'mp3', 'opus', 'wav', 'flac'}
VALID_THUMBNAIL_FORMATS = {'jpg'}
def _parse_ytdl_options_overrides(value, *, enabled: bool) -> dict:
    if value is None or value == '':
        return {}

    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError as exc:
            raise web.HTTPBadRequest(reason='ytdl_options_overrides must be valid JSON') from exc

    if not isinstance(value, dict):
        raise web.HTTPBadRequest(reason='ytdl_options_overrides must be a JSON object')

    if value and not enabled:
        raise web.HTTPBadRequest(reason='ytdl_options_overrides are disabled')

    return value


def _migrate_legacy_request(post: dict) -> dict:
    """
    BACKWARD COMPATIBILITY: Translate old API request schema into the new one.

    Old API:
      format (any/mp4/m4a/mp3/opus/wav/flac/thumbnail/captions)
      quality
      video_codec
      subtitle_format (only when format=captions)

    New API:
      download_type (video/audio/captions/thumbnail)
      codec
      format
      quality
    """
    if "download_type" in post:
        return post

    old_format = str(post.get("format") or "any").strip().lower()
    old_quality = str(post.get("quality") or "best").strip().lower()
    old_video_codec = str(post.get("video_codec") or "auto").strip().lower()

    if old_format in VALID_AUDIO_FORMATS:
        post["download_type"] = "audio"
        post["codec"] = "auto"
        post["format"] = old_format
    elif old_format == "thumbnail":
        post["download_type"] = "thumbnail"
        post["codec"] = "auto"
        post["format"] = "jpg"
        post["quality"] = "best"
    elif old_format == "captions":
        post["download_type"] = "captions"
        post["codec"] = "auto"
        post["format"] = str(post.get("subtitle_format") or "srt").strip().lower()
        post["quality"] = "best"
    else:
        # old_format is usually any/mp4 (legacy video path)
        post["download_type"] = "video"
        post["codec"] = old_video_codec
        if old_quality == "best_ios":
            post["format"] = "ios"
            post["quality"] = "best"
        elif old_quality == "audio":
            # Legacy "audio only" under video format maps to m4a audio.
            post["download_type"] = "audio"
            post["codec"] = "auto"
            post["format"] = "m4a"
            post["quality"] = "best"
        else:
            post["format"] = old_format
            post["quality"] = old_quality

    return post

class Notifier(DownloadQueueNotifier):
    async def added(self, dl):
        log.info(f"Notifier: Download added - {dl.title}")
        await sio.emit('added', serializer.encode(dl))

    async def updated(self, dl):
        log.debug(f"Notifier: Download updated - {dl.title}")
        await sio.emit('updated', serializer.encode(dl))

    async def completed(self, dl):
        log.info(f"Notifier: Download completed - {dl.title}")
        await sio.emit('completed', serializer.encode(dl))

    async def canceled(self, id):
        log.info(f"Notifier: Download canceled - {id}")
        await sio.emit('canceled', serializer.encode(id))

    async def cleared(self, id):
        log.info(f"Notifier: Download cleared - {id}")
        await sio.emit('cleared', serializer.encode(id))

dqueue = DownloadQueue(config, Notifier())
app.on_startup.append(lambda app: dqueue.initialize())
app.on_cleanup.append(lambda app: Download.shutdown_manager())


class MetubeSubscriptionNotifier(SubscriptionNotifier):
    async def subscription_added(self, sub: SubscriptionInfo):
        log.info("Subscription added: %s", sub.name)
        await sio.emit('subscription_added', serializer.encode(sub.to_public_dict()))

    async def subscription_updated(self, sub: SubscriptionInfo):
        await sio.emit('subscription_updated', serializer.encode(sub.to_public_dict()))

    async def subscription_removed(self, sub_id: str):
        log.info("Subscription removed: %s", sub_id)
        await sio.emit('subscription_removed', serializer.encode(sub_id))

    async def subscriptions_all(self, subs: list[SubscriptionInfo]):
        await sio.emit('subscriptions_all', serializer.encode([s.to_public_dict() for s in subs]))


submgr = SubscriptionManager(config, dqueue, MetubeSubscriptionNotifier())
app.on_cleanup.append(lambda app: submgr.close())


async def _subscription_loop_startup(app):
    """aiohttp on_startup requires awaitable receivers; start_background_loop is sync."""
    submgr.start_background_loop()


app.on_startup.append(_subscription_loop_startup)

class FileOpsFilter(DefaultFilter):
    def __call__(self, change_type: int, path: str) -> bool:
        # Check if this path matches our YTDL_OPTIONS_FILE
        if path != config.YTDL_OPTIONS_FILE:
            return False

        # For existing files, use samefile comparison to handle symlinks correctly
        if os.path.exists(config.YTDL_OPTIONS_FILE):
            try:
                if not os.path.samefile(path, config.YTDL_OPTIONS_FILE):
                    return False
            except (OSError, IOError):
                # If samefile fails, fall back to string comparison
                if path != config.YTDL_OPTIONS_FILE:
                    return False

        # Accept all change types for our file: modified, added, deleted
        return change_type in (Change.modified, Change.added, Change.deleted)

def get_options_update_time(success=True, msg=''):
    result = {
        'success': success,
        'msg': msg,
  
... [TRUNCATED]
```

### File: ui\package.json
```json
{
  "name": "metube",
  "version": "0.0.0",
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "build:watch": "ng build --watch",
    "test": "ng test",
    "lint": "ng lint"
  },
  "prettier": {
    "printWidth": 100,
    "singleQuote": true,
    "overrides": [
      {
        "files": "*.html",
        "options": {
          "parser": "angular"
        }
      }
    ]
  },
  "private": true,
  "dependencies": {
    "@angular/animations": "^21.2.7",
    "@angular/common": "^21.2.7",
    "@angular/compiler": "^21.2.7",
    "@angular/core": "^21.2.7",
    "@angular/forms": "^21.2.7",
    "@angular/platform-browser": "^21.2.7",
    "@angular/platform-browser-dynamic": "^21.2.7",
    "@angular/service-worker": "^21.2.7",
    "@fortawesome/angular-fontawesome": "~4.0.0",
    "@fortawesome/fontawesome-svg-core": "^7.2.0",
    "@fortawesome/free-brands-svg-icons": "^7.2.0",
    "@fortawesome/free-regular-svg-icons": "^7.2.0",
    "@fortawesome/free-solid-svg-icons": "^7.2.0",
    "@ng-bootstrap/ng-bootstrap": "^20.0.0",
    "@ng-select/ng-select": "^21.7.0",
    "@popperjs/core": "^2.11.8",
    "bootstrap": "^5.3.8",
    "ngx-cookie-service": "^21.3.1",
    "ngx-socket-io": "~4.10.0",
    "rxjs": "~7.8.2",
    "tslib": "^2.8.1",
    "zone.js": "0.15.0"
  },
  "devDependencies": {
    "@angular-eslint/builder": "21.1.0",
    "@angular/build": "^21.2.6",
    "@angular/cli": "^21.2.6",
    "@angular/compiler-cli": "^21.2.7",
    "@angular/localize": "^21.2.7",
    "@eslint/js": "^9.39.4",
    "angular-eslint": "21.1.0",
    "eslint": "^9.39.4",
    "jsdom": "^27.4.0",
    "typescript": "~5.9.3",
    "typescript-eslint": "8.47.0",
    "vitest": "^4.1.2"
  }
}

```

### File: build.sh
```sh
#!/usr/bin/env bash

VERSION=$(jq -r ".version" ./src/manifest.json)

if test -z "$VERSION"; then
  echo "can't parse version from manifest file"
  exit
fi

FILE=metube-browser-extension-"$VERSION".zip

if test -f "./builds/$FILE"; then
  if [ "$1" == "--force" ]; then
    rm -f "./builds/$FILE"
  else
    echo "file ./builds/$FILE already exists. if you want to rewrite it use argument --force"
    exit
  fi
fi

cd ./src && zip -9 -r ../builds/"$FILE" ./*

```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Enforcement Responsibilities

Project maintainers are responsible for clarifying and enforcing our standards of acceptable behavior and will take appropriate and fair corrective action in response to any behavior that they deem inappropriate, threatening, offensive, or harmful.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, and will communicate reasons for moderation decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when an individual is officially representing the community in public spaces.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the project maintainers responsible for enforcement. All complaints will be reviewed and investigated promptly and fairly.

All project maintainers are obligated to respect the privacy and security of the reporter of any incident.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org), version 2.0, available at https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

```

### File: CONTRIBUTING.md
```md
# Contributing to MeTube

Thank you for your interest in contributing to MeTube! We welcome contributions from everyone. This document will guide you through the process.

## 🚀 Getting Started

### Prerequisites
- Git installed on your machine
- A GitHub account
- Basic knowledge of HTML, CSS, and JavaScript
- A code editor (VS Code recommended)

### Setting Up Your Development Environment

1. **Fork the Repository**
   - Click the "Fork" button at the top right of the repository page
   - This creates a copy of the repository in your GitHub account

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/MeTube.git
   cd MeTube
   ```

3. **Add Upstream Remote**
   ```bash
   git remote add upstream https://github.com/Open-Source-Chandigarh/MeTube.git
   ```

4. **Open in Browser**
   - Simply open `index.html` in your browser
   - Or use a local server like Live Server extension in VS Code

## 🔄 Making Changes

### 1. Create a New Branch
Always create a new branch for your changes:
```bash
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name
```

**Branch Naming Convention:**
- `feat/feature-name` - For new features
- `fix/bug-name` - For bug fixes
- `docs/doc-name` - For documentation updates
- `style/style-name` - For UI/styling changes
- `refactor/refactor-name` - For code refactoring

### 2. Make Your Changes
- Write clean, readable code
- Follow the existing code style
- Test your changes thoroughly
- Ensure your code works in different browsers (Chrome, Firefox, Safari, Edge)

### 3. Commit Your Changes
```bash
git add .
git commit -m "feat: add your feature description"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, semicolons, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### 4. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 5. Create a Pull Request
1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill in the PR template with details about your changes
4. Submit the pull request

## 📝 Pull Request Guidelines

### PR Title Format
Use descriptive titles with conventional commit prefixes:
- ✅ `feat: Add voice search functionality`
- ✅ `fix: Resolve dark mode toggle issue`
- ✅ `docs: Update README with installation steps`

### PR Description
Include the following in your PR description:
- **What**: Brief description of changes
- **Why**: Reason for the changes
- **How**: How you implemented it
- **Screenshots**: If UI changes are involved
- **Testing**: How you tested your changes

### Example PR Description
```markdown
## Description
Added voice search functionality to the search bar.

## Changes Made
- Added microphone button to search input
- Implemented Web Speech API integration
- Added voice search modal with real-time transcription
- Added dark mode support for voice search UI

## Screenshots
[Add screenshots here]

## Testing
- Tested in Chrome, Edge, and Safari
- Tested voice recognition with different accents
- Tested in both light and dark modes
- Verified responsiveness on mobile devices
```

## 🎨 Code Style Guidelines

### HTML
- Use semantic HTML5 elements
- Add proper `alt` attributes to images
- Include ARIA labels for accessibility
- Indent with 4 spaces

### CSS
- Use meaningful class names
- Follow BEM naming convention when appropriate
- Group related properties together
- Add comments for complex styles
- Support both light and dark modes

### JavaScript
- Use `const` and `let`, avoid `var`
- Use descriptive variable names
- Add comments for complex logic
- Handle errors gracefully
- Follow ES6+ standards

## 🐛 Reporting Issues

### Before Creating an Issue
- Search existing issues to avoid duplicates
- Check if the issue exists in the latest version
- Try to reproduce the issue

### Creating an Issue
Include the following information:
- **Clear title**: Describe the issue briefly
- **Description**: Detailed explanation of the issue
- **Steps to reproduce**: How to recreate the issue
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Screenshots**: If applicable
- **Browser/OS**: Your environment details

## ✅ Testing

Before submitting your PR:
- [ ] Test in multiple browsers
- [ ] Test in both light and dark modes
- [ ] Test on mobile and desktop
- [ ] Ensure no console errors
- [ ] Verify all links work
- [ ] Check that the code is properly formatted

## 🎯 What to Contribute

### Good First Issues
- UI/UX improvements
- Documentation updates
- Bug fixes
- Adding comments to code
- Accessibility improvements

### Feature Ideas
- Video playback features
- Playlist functionality
- Search filters
- User preferences
- Keyboard shortcuts
- Social sharing
- Download options

### Areas That Need Help
- Cross-browser compatibility
- Performance optimization
- Accessibility improvements
- Mobile responsiveness
- Test coverage

## 📚 Resources

- [HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

## 🤝 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## 💡 Tips for Success

1. **Start Small**: Begin with small contributions to understand the codebase
2. **Ask Questions**: Don't hesitate to ask for help in issues or discussions
3. **Be Patient**: Reviews may take time
4. **Stay Updated**: Keep your fork synced with the main repository
5. **Have Fun**: Enjoy the process of learning and contributing!

## 📞 Getting Help

If you need help:
- Check existing issues and discussions
- Read the documentation thoroughly
- Ask questions in the issue comments
- Join our community discussions

## 🎉 Thank You!

Your contributions make MeTube better for everyone. We appreciate your time and effort!

Happy Coding! 🚀

```

### File: docker-entrypoint.sh
```sh
#!/bin/sh

PUID="${UID:-$PUID}"
PGID="${GID:-$PGID}"

echo "Setting umask to ${UMASK}"
umask ${UMASK}
echo "Creating download directory (${DOWNLOAD_DIR}), state directory (${STATE_DIR}), and temp dir (${TEMP_DIR})"
mkdir -p "${DOWNLOAD_DIR}" "${STATE_DIR}" "${TEMP_DIR}"

if [ `id -u` -eq 0 ] && [ `id -g` -eq 0 ]; then
    if [ "${PUID}" -eq 0 ]; then
        echo "Warning: it is not recommended to run as root user, please check your setting of the PUID/PGID (or legacy UID/GID) environment variables"
    fi
    if [ "${CHOWN_DIRS:-true}" != "false" ]; then
        echo "Changing ownership of download and state directories to ${PUID}:${PGID}"
        chown -R "${PUID}":"${PGID}" /app "${DOWNLOAD_DIR}" "${STATE_DIR}" "${TEMP_DIR}"
    fi
    echo "Starting BgUtils POT Provider"
    gosu "${PUID}":"${PGID}" bgutil-pot server >/tmp/bgutil-pot.log 2>&1 &
    echo "Running MeTube as user ${PUID}:${PGID}"
    exec gosu "${PUID}":"${PGID}" python3 app/main.py
else
    echo "User set by docker; running MeTube as `id -u`:`id -g`"
    echo "Starting BgUtils POT Provider"
    bgutil-pot server >/tmp/bgutil-pot.log 2>&1 &
    exec python3 app/main.py
fi

```

### File: index.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description"
        content="MeTube - Explore, watch, and fetch details about YouTube videos all in one place. Access video information, related content, and more with ease.">
    <meta name="keywords"
        content="MeTube, YouTube video search, watch YouTube videos, video information, video data, video details, video player, explore videos">
    <meta name="author" content="MeTube Team">

    <meta property="og:title" content="MeTube - Watch and Explore YouTube Videos">
    <meta property="og:description"
        content="MeTube allows you to watch YouTube videos and fetch details like description, views, and related videos.">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="MeTube - Watch YouTube Videos and Fetch Information">
    <meta name="twitter:description" content="Watch YouTube videos and discover in-depth details with MeTube.">

    <title>MeTube - Watch and Explore YouTube Videos</title>
    <link rel="shortcut icon" href="favicon/favicon-16x16.png" type="image/x-icon">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />

    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="chatbot/chatbot.css">

</head>

<body id="home">
    <nav class="navbar">
        <a href="index.html"> <img src="./assets/logo.png" style="height: 75px;"> </a>
        <div class="search-container">
            <div class="search-container">
                <div class="search-input-wrapper">
                    <input type="text" id="searchInput" placeholder="Search videos, channels, or keywords"
                        aria-label="Search videos">

                    <button id="voiceSearchButton" onclick="startVoiceSearch()" title="Search with your voice">
                        <span class="material-symbols-outlined">mic</span>
                    </button>
                </div>

                <!-- Original search button -->
                <button id="searchButton" onclick="searchVideos()" title="Search">
                    <span class="material-symbols-outlined">search</span>
                </button>
                <!-- Chatbot Icon beside Search -->
                <button id="chat-inline-icon" title="Chat Assistant" aria-label="Chat Assistant">
                    <span class="material-symbols-outlined">chat_bubble</span>
                </button>


            </div>


            <div class="nav-controls">
                <button id="toggleViewButton" onclick="toggleViewMode()" title="Toggle view"
                    aria-label="Toggle between grid and list view">
                    <span id="viewIcon" class="material-symbols-outlined">grid_view</span>
                </button>

                <div class="theme-selector">
                    <button id="toggleThemeButton" onclick="toggleThemeMenu()" title="Theme options"
                        aria-label="Select theme">
                        <span id="themeIcon" class="material-symbols-outlined">palette</span>
                    </button>
                    <div id="themeMenu" class="theme-menu hidden">
                        <button onclick="setTheme('light')" class="theme-option">
                            <span class="material-symbols-outlined">light_mode</span>
                            <span>Light</span>
                        </button>
                        <button onclick="setTheme('dark')" class="theme-option">
                            <span class="material-symbols-outlined">dark_mode</span>
                            <span>Dark</span>
                        </button>
                        <button onclick="setTheme('sepia')" class="theme-option">
                            <span class="material-symbols-outlined">auto_stories</span>
                            <span>Sepia</span>
                        </button>
                        <button onclick="setTheme('contrast')" class="theme-option">
                            <span class="material-symbols-outlined">contrast</span>
                            <span>High Contrast</span>
                        </button>
                    </div>
                </div>
            </div>
    </nav>


    <div class="main-content">
        <div id="filterButtons" class="filter-buttons">
            <button onclick="showTrending()" class="filter-btn" data-category="all">All</button>
            <button onclick="searchVideos('sports')" class="filter-btn" data-category="sports">Sports</button>
            <button onclick="searchVideos('entertainment')" class="filter-btn"
                data-category="entertainment">Entertainment</button>
            <button onclick="searchVideos('music')" class="filter-btn" data-category="music">Music</button>
            <button onclick="searchVideos('news')" class="filter-btn" data-category="news">News</button>
            <button onclick="searchVideos('gaming')" class="filter-btn" data-category="gaming">Gaming</button>
            <button onclick="searchVideos('comedy')" class="filter-btn" data-category="comedy">Comedy</button>

        </div>
        <!-- <div class="video-section">
        <div class="main-video-content">
            Back Toolbar (moved here to sit above the video player)
            <div id="backToolbar" class="back-toolbar">
                <button id="backButton" title="Back" aria-label="Go back">
                    <span class="material-symbols-outlined">arrow_back</span>
                    <span class="back-button-text">Back</span>
                </button>
            </div> -->
        <!-- <div class="video-container">
                <div id="videoWrapper">
                    <iframe id="videoPlayer" src="" frameborder="0" allowfullscreen></iframe>
                    <div class="video-controls-overlay">
                        <button id="pipButton" class="pip-button" onclick="togglePictureInPicture()" title="Picture-in-Picture" aria-label="Enable Picture-in-Picture mode">
                            <span class="material-symbols-outlined">picture_in_picture_alt</span>
                        </button>
                    </div>
                </div>
                <h2 id="videoTitle" class="video-title"></h2> -->

        <!-- <div class="video-description-section">
                    <div class="description-container" id="descriptionContainer">
                        <h3>Description</h3>
                        <p id="videoDescription"></p>
                        <button id="showMoreBtn" class="show-more-btn" onclick="toggleDescription()" style="display: none;">
                            Show More
                        </button>
                    </div> -->
        <!-- </div> -->

        <!-- <div class="video-comments-section">
                    <div class="comments-container" id="commentsContainer">
                        <h3>Comments</h3>
                        <div id="commentsLoading" class="comments-loading" style="display: none;">
                            <p>Loading comments...</p>
                        </div> -->
        <!-- <div id="commentsList" class="comments-list">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="sidebar-content">
            <h3 class="sidebar-title">Related Videos</h3>
            <div id="relatedVideos" class="related-videos">
            </div> -->
        <div class="video-section responsive-video-section">
            <div class="main-video-content responsive-main-video">
                <!--Back Toolbar -->
                <div id="backToolbar" class="back-toolbar">
                    <button id="backButton" title="Back" aria-label="Go back">
                        <span class="material-symbols-outlined">arrow_back</span>
                        <span class="back-button-text">Back</span>
                    </button>
                </div>

                <div class="video-container">
                    <div id="videoWrapper" class="responsive-video-wrapper">
                        <iframe id="videoPlayer" src="" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <h2 id="videoTitle" class="video-title"></h2>

                    <div class="video-description-section">
                        <div class="description-container" id="descriptionContainer">
                            <h3>Description</h3>
                            <p id="videoDescription"></p>
                            <button id="showMoreBtn" class="show-more-btn" onclick="toggleDescription()"
                                style="display: none;">
                                Show More
                            </button>
                        </div>
                    </div>

                    <div class="video-comments-section">
                        <div class="comments-container" id="commentsContainer">
                            <h3>Comments</h3>
                            <div id="commentsLoading" class="comments-loading" style="display: none;">
                                <p>Loading comments...</p>
                            </div>
                            <div id="commentsList" class="comments-list"></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="sidebar-content responsive-sidebar">
                <h3 class="sidebar-title">Related Videos</h3>
                <div id="relatedVideos" class="related-videos"></div>
            </div>
        </div>


    </div>
    </div>

    <div id="welcomeMessage" class="welcome-message">
        <div class="welcome-content">
            <h2>Welcome to MeTube</h2>
            <p>Discover and watch YouTube videos faster. Use the search bar above or browse categories to get started.
            </p>
            <div class="welcome-icon">🎬</div>
        </div>
    </div>

    <div id="searchResults" class="search-results"></div>

    <!-- Templates for loading skeletons -->
    <template id="searchResultSkeleton">
        <div class="result-item skeleton-card" role="presentation" aria-hidden="true">
            <div class="skeleton-thumb skeleton-shimmer"></div>
            <div class="skeleton-content">
                <div class="skeleton-line w-80 skeleton-shimmer"></div>
                <div class="skeleton-line w-60 skeleton-shimmer"></div>
            </div>
        </div>
    </template>

    <template id="commentSkeleton">
        <div class="comment-item" role="presentation" aria-hidden="true">
            <div class="skeleton-line w-40 skeleton-shimmer"></div>
            <div class="skeleton-line w-90 skeleton-shimmer"></div>
            <div class="skeleton-line w-70 skeleton-shimmer"></div>
        </div>
    </template>

    <template id="relatedVideoSkeleton">
        <div class="related-skeleton-item" role="presentation" aria-hidden="true">
            <div class="related-skeleton-thumb skeleton-shimmer"></div>
            <div class="related-skeleton-info">
                <div class="skeleton-line w-80 skeleton-shimmer"></div>
                <div class="skeleton-line w-50 skeleton-shimmer"></div>
            </div>
        </div>
    </template>
    </div>

    <footer class="site-footer">
        <div class="footer-inner">
            <div class="footer-top">
                <div class="footer-column footer-brand">
                    <h3>MeTube</h3>
                    <p class="footer-tag">A cleaner, distraction-reduced YouTube experience — search, watch, and explore
                        videos with fewer distractions.</p>
                    <div class="footer-social">
                        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
                            <img src="./assets/facebook.png" alt="facebook logo">
                        </a>
                        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
                            <img src="./assets/twitter.png" alt="twitter logo">
                        </a>
                        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer"
                            aria-label="Instagram">
                            <img src="./assets/instagram.png" alt="instagram logo">
                        </a>
                    </div>
                </div>

                <div class="footer-column footer-links">
                    <h4>Quick Links</h4>
                    <a href="./pages/privacy.html">Privacy Policy</a>
                    <a href="./pages/terms.html">Terms of Service</a>
                    <a href="./pages/contact.html">Contact Us</a>
                </div>

                <div class="footer-column footer-resources">
                    <h4>Resources</h4>
                    <a href="https://github.com/Open-Source-Chandigarh/MeTube" target="_blank"
                        rel="noopener noreferrer">Contributing</a>
                    <a href="#">API Documentation</a>
                    <a href="#">Roadmap</a>
                </div>

                <div class="footer-column footer-newsletter">
                    <h4>Newsletter</h4>
                    <p>Get updates on new features and improvements. No spam — unsubscribe anytime.</p>
                    <form id="newsletterForm" class="newsletter-form" onsubmit="return handleSubscribe(event)">
                        <input type="email" id="newsletterEmail" placeholder="Your email address" required>
                        <button type="submit">Subscribe</button>
                    </form>
                    <p id="newsletterMsg" class="newsletter-msg" aria-live="polite"></p>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; <span id="footerYear"></span> MeTube. All rights reserved.</p>
                <button class="keyboard-shortcuts-btn" onclick="toggleKeyboardShortcutsHelp()"
                    title="View keyboard shortcuts">
                    <span class="material-symbols-outlined">keyboard</span>
                    Press ? for shortcuts
                </button>
            </div>
        </div>
    </footer>
    <button id="scrollTopBtn" title="Go to top">↑</button>


    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const y = new Date().getFullYear();
            const el = document.getElementById('footerYear');
            if (el) el.textContent = y;
        });
    </script>

    <!-- Voice Search Modal -->
    <div id="voiceSearchModal" class="voice-
... [TRUNCATED]
```

### File: LEARN.md
```md
## Discover Our MeTube Project!

Welcome to our MeTube project repository! 🌟 Below, you'll find detailed information about the project and resources to help you get started.

## Project Overview  

MeTube is a streamlined, open-source platform inspired by YouTube, designed for a minimalistic and distraction-free viewing experience. The platform focuses on simplicity and ease of use, allowing users to search for and watch videos without unnecessary clutter. Upon opening a video, users have access to just two buttons—one to view the video’s description and the other to see the pinned comment—ensuring a clear and straightforward interface. The project is community-driven, encouraging contributions to enhance and maintain the platform's functionality and user experience.

## Tech Stack Used 🛠️

JavaScript:
Vanilla JavaScript: Used to manage DOM manipulation, event handling, and API calls.
Fetch API: For making asynchronous HTTP requests to the YouTube API to fetch video details, search results, and comments.
**Backend Technologies:**

API: The application interacts with the YouTube Data API (v3) to retrieve video search results, descriptions, and comments. This is an external API provided by Google, and the code uses API keys to access it.

**Additional:**

Deployment: Such a frontend application could be hosted using platforms like GitHub Pages, Netlify, or Vercel, as it’s primarily frontend with API integration.
Authentication: API keys are used for authenticating requests to the YouTube API.

## Resources to Learn 📚
Here are some resources to help you get started with the technologies used in this project:

JavaScript (Vanilla JavaScript)

-[MDN Web Docs - JavaScript]https://developer.mozilla.org/en-US/docs/Web/JavaScript

Fetch API:
-[MDN Web Docs - Fetch API]https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API


YouTube Data API Documentation:
 -[YouTube Data API (v3) Documentation]https://developers.google.com/youtube/v3/docs

<hr>

## Frequently Asked Questions (FAQ) ❓

### What is the purpose of this project?
The purpose of the MeTube project is to provide a simplified, distraction-free version of YouTube with easy access to video descriptions and pinned comments.

### Who can contribute to this project?
Anyone with an interest in web development, API integration, or improving user experience is welcome to contribute to the MeTube project, regardless of skill level.

### How can I test the project locally?
You can clone the repository to your local machine using detailed instructions provided in [README.md](./README.md) file.

### Where can I find the project documentation?
The project documentation, including setup instructions and contribution guidelines, is available in the [README.md](./README.md).

### Who do I contact for help or questions?
If you have any questions or need assistance, you can contact the project maintainers through their provided contact details in [README.md](./README.md) file.


### How do I suggest new features for the project?
You can suggest new features by opening an issue in the repository. Please provide a clear description of the feature and its benefits.

### Are there any guidelines for coding standards?
Yes, we follow standard coding practices. Please ensure your code is clean, well-documented.

### Can I report bugs and issues?
Absolutely! If you encounter any bugs or issues, please report them by opening an issue in the repository. Provide as much detail as possible to help us address the problem promptly.

---

We hope these resources and FAQs help you get started with Our Metube free-Interface project. Happy coding! 🌟





```

### File: package-lock.json
```json
{
  "name": "MeTube",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "dependencies": {
        "cors": "^2.8.5",
        "dotenv": "^17.2.3",
        "express": "^5.1.0",
        "node-fetch": "^3.3.2"
      }
    },
    "node_modules/accepts": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-2.0.0.tgz",
      "integrity": "sha512-5cvg6CtKwfgdmVqY1WIiXKc3Q1bkRqGLi+2W/6ao+6Y7gu/RCwRuAhGEzh5B4KlszSuTLgZYuqFqo5bImjNKng==",
      "license": "MIT",
      "dependencies": {
        "mime-types": "^3.0.0",
        "negotiator": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/body-parser": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-2.2.0.tgz",
      "integrity": "sha512-02qvAaxv8tp7fBa/mw1ga98OGm+eCbqzJOKoRt70sLmfEEi+jyBYVTDGfCL/k06/4EMk/z01gCe7HoCH/f2LTg==",
      "license": "MIT",
      "dependencies": {
        "bytes": "^3.1.2",
        "content-type": "^1.0.5",
        "debug": "^4.4.0",
        "http-errors": "^2.0.0",
        "iconv-lite": "^0.6.3",
        "on-finished": "^2.4.1",
        "qs": "^6.14.0",
        "raw-body": "^3.0.0",
        "type-is": "^2.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/bytes": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
      "integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/content-disposition": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-1.0.0.tgz",
      "integrity": "sha512-Au9nRL8VNUut/XSzbQA38+M78dzP4D+eqg3gfJHMIHHYa3bg067xj1KxMUWj+VULbiZMowKngFFbKczUrNJ1mg==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "5.2.1"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/content-type": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
      "integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz",
      "integrity": "sha512-yki5XnKuf750l50uGTllt6kKILY4nQ1eNIQatoXEByZ5dWgnKqbnqmTrBE5B4N7lrMJKQ2ytWMiTO2o0v6Ew/w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie-signature": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.2.2.tgz",
      "integrity": "sha512-D76uU73ulSXrD1UXF4KE2TMxVVwhsnCgfAyTg9k8P6KGZjlXKrOLe4dJQKI3Bxi5wjesZoFXJWElNWBjPZMbhg==",
      "license": "MIT",
      "engines": {
        "node": ">=6.6.0"
      }
    },
    "node_modules/cors": {
      "version": "2.8.5",
      "resolved": "https://registry.npmjs.org/cors/-/cors-2.8.5.tgz",
      "integrity": "sha512-KIHbLJqu73RGr/hnbrO9uBeixNGuvSQjul/jdFvS/KFSIH1hWVd1ng7zOHx+YrEfInLG7q4n6GHQ9cDtxv/P6g==",
      "license": "MIT",
      "dependencies": {
        "object-assign": "^4",
        "vary": "^1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/data-uri-to-buffer": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/data-uri-to-buffer/-/data-uri-to-buffer-4.0.1.tgz",
      "integrity": "sha512-0R9ikRb668HB7QDxT1vkpuUBtqc53YyAwMwGeUFKRojY/NWKvdZ+9UYtRfGmhqNbRkTSVpMbmyhXipFFv2cb/A==",
      "license": "MIT",
      "engines": {
        "node": ">= 12"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/depd": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
      "integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/dotenv": {
      "version": "17.2.3",
      "resolved": "https://registry.npmjs.org/dotenv/-/dotenv-17.2.3.tgz",
      "integrity": "sha512-JVUnt+DUIzu87TABbhPmNfVdBDt18BLOWjMUFJMSi/Qqg7NTYtabbvSNJGOJ7afbRuv9D/lngizHtP7QyLQ+9w==",
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://dotenvx.com"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
      "license": "MIT"
    },
    "node_modules/encodeurl": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
      "integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
      "integrity": "sha512-FGgH2h8zKNim9ljj7dankFPcICIK9Cp5bm+c2gQSYePhpaG5+esrLODihIorn+Pe6FGJzWhXQotPv73jTaldXA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow==",
      "license": "MIT"
    },
    "node_modules/etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/express": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/express/-/express-5.1.0.tgz",
      "integrity": "sha512-DT9ck5YIRU+8GYzzU5kT3eHGA5iL+1Zd0EutOmTE9Dtk+Tvuzd23VBU+ec7HPNSTxXYO55gPV/hq4pSBJDjFpA==",
      "license": "MIT",
      "dependencies": {
        "accepts": "^2.0.0",
        "body-parser": "^2.2.0",
        "content-disposition": "^1.0.0",
        "content-type": "^1.0.5",
        "cookie": "^0.7.1",
        "cookie-signature": "^1.2.1",
        "debug": "^4.4.0",
        "encodeurl": "^2.0.0",
        "escape-html": "^1.0.3",
        "etag": "^1.8.1",
        "finalhandler": "^2.1.0",
        "fresh": "^2.0.0",
        "http-errors": "^2.0.0",
        "merge-descriptors": "^2.0.0",
        "mime-types": "^3.0.0",
        "on-finished": "^2.4.1",
        "once": "^1.4.0",
        "parseurl": "^1.3.3",
        "proxy-addr": "^2.0.7",
        "qs": "^6.14.0",
        "range-parser": "^1.2.1",
        "router": "^2.2.0",
        "send": "^1.1.0",
        "serve-static": "^2.2.0",
        "statuses": "^2.0.1",
        "type-is": "^2.0.1",
        "vary": "^1.1.2"
      },
      "engines": {
        "node": ">= 18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/fetch-blob": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/fetch-blob/-/fetch-blob-3.2.0.tgz",
      "integrity": "sha512-7yAQpD2UMJzLi1Dqv7qFYnPbaPx7ZfFK6PiIxQ4PfkGPyNyl2Ugx+a/umUonmKqjhM4DnfbMvdX6otXq83soQQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/jimmywarting"
        },
        {
          "type": "paypal",
          "url": "https://paypal.me/jimmywarting"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "node-domexception": "^1.0.0",
        "web-streams-polyfill": "^3.0.3"
      },
      "engines": {
        "node": "^12.20 || >= 14.13"
      }
    },
    "node_modules/finalhandler": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-2.1.0.tgz",
      "integrity": "sha512-/t88Ty3d5JWQbWYgaOGCCYfXRwV1+be02WqYYlL6h0lEiUAMPM8o8qKGO01YIkOHzka2up08wvgYD0mDiI+q3Q==",
      "license": "MIT",
      "dependencies": {
        "debug": "^4.4.0",
        "encodeurl": "^2.0.0",
        "escape-html": "^1.0.3",
        "on-finished": "^2.4.1",
        "parseurl": "^1.3.3",
        "statuses": "^2.0.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/formdata-polyfill": {
      "version": "4.0.10",
      "resolved": "https://registry.npmjs.org/formdata-polyfill/-/formdata-polyfill-4.0.10.tgz",
      "integrity": "sha512-buewHzMvYL29jdeQTVILecSaZKnt/RJWjoZCF5OW60Z67/GmSLBkOFM7qh1PI3zFNtJbaZL5eQu1vLfazOwj4g==",
      "license": "MIT",
      "dependencies": {
        "fetch-blob": "^3.1.2"
      },
      "engines": {
        "node": ">=12.20.0"
      }
    },
    "node_modules/forwarded": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz",
      "integrity": "sha512-buRG0fpBtRHSTCOASe6hD258tEubFoRLb4ZNA6NxMVHNw2gOcwHo9wyablzMzOA5z9xA9L1KNjk/Nt6MT9aYow==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/fresh": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-2.0.0.tgz",
      "integrity": "sha512-Rx/WycZ60HOaqLKAi6cHRKKI7zxWbJ31MhntmtwMoaTeF7XFH9hhBp8vITaMidfljRQ6eYWCKkaTK+ykVJHP2A==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": "
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
