---
id: picture-in-picture-viewer
type: knowledge
owner: OA_Triage
---
# picture-in-picture-viewer
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: FETCHED_picture-in-picture-viewer_033802\README.md
```md
# Picture-in-Picture Viewer &nbsp;<img src="https://raw.githubusercontent.com/Alex313031/picture-in-picture-viewer/master/src/assets/icon128.png" width="48">

A simple Chromium Extension to demonstrate the [Picture-in-Picture Web API](https://wicg.github.io/picture-in-picture/) in Chromium.

Get it on the Chrome Web Store at https://chrome.google.com/webstore/detail/picture-in-picture-viewer/kgfcmiijchdkbknmjnojfngnapkibkdh

<img src="https://raw.githubusercontent.com/Alex313031/picture-in-picture-viewer/master/Screenshot.png" width="900">

## Configuration

The keyboard shortcut (defaults to `Alt-P`) can be changed on the Chrome Extension Shortcuts settings page:
`chrome://extensions/shortcuts`

```

### File: FETCHED_picture-in-picture-viewer_033802\src\background.js
```js
// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

chrome.action.onClicked.addListener((tab) => {
    const files = ["script.js"];
    chrome.scripting.executeScript({
      target: { tabId: tab.id, allFrames: true },
      world: "MAIN",
      files,
    });
});

```

### File: FETCHED_picture-in-picture-viewer_033802\src\manifest.json
```json
{
  "name": "Picture-in-Picture Viewer",
  "short_name": "PiP Viewer",
  "author": "Alex313031",
  "description": "Watch video using the Picture-in-Picture API.",
  "homepage_url": "https://github.com/Alex313031/picture-in-picture-viewer",
  "manifest_version": 3,
  "minimum_chrome_version": "88",
  "offline_enabled": true,
  "version": "1.12.2",
  "version_name": "1.12.2",
  "icons": {
    "16": "assets/icon16.png",
    "24": "assets/icon24.png",
    "32": "assets/icon32.png",
    "48": "assets/icon48.png",
    "64": "assets/icon64.png",
    "128": "assets/icon128.png",
    "256": "assets/icon256.png"
  },
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_icon": {
      "19": "assets/icon19.png",
      "38": "assets/icon38.png"
    }
  },
  "commands": {
    "_execute_action": {
      "suggested_key": {
        "windows": "Alt+P",
        "mac": "Alt+P",
        "chromeos": "Alt+P",
        "linux": "Alt+P"
      }
    }
  },
  "permissions": [
    "scripting"
  ],
  "host_permissions": [
    "<all_urls>"
  ]
}

```

### File: FETCHED_picture-in-picture-viewer_033802\src\script.js
```js
// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

function findLargestPlayingVideo() {
  const videos = Array.from(document.querySelectorAll('video'))
    .filter(video => video.readyState != 0)
    .filter(video => video.disablePictureInPicture == false)
    .sort((v1, v2) => {
      const v1Rect = v1.getClientRects()[0]||{width:0,height:0};
      const v2Rect = v2.getClientRects()[0]||{width:0,height:0};
      return ((v2Rect.width * v2Rect.height) - (v1Rect.width * v1Rect.height));
    });

  if (videos.length === 0) {
    return;
  }

  return videos[0];
}

async function requestPictureInPicture(video) {
  await video.requestPictureInPicture();
  video.setAttribute('__pip__', true);
  video.addEventListener('leavepictureinpicture', event => {
    video.removeAttribute('__pip__');
  }, { once: true });
  new ResizeObserver(maybeUpdatePictureInPictureVideo).observe(video);
}

function maybeUpdatePictureInPictureVideo(entries, observer) {
  const observedVideo = entries[0].target;
  if (!document.querySelector('[__pip__]')) {
    observer.unobserve(observedVideo);
    return;
  }
  const video = findLargestPlayingVideo();
  if (video && !video.hasAttribute('__pip__')) {
    observer.unobserve(observedVideo);
    requestPictureInPicture(video);
  }
}

(async () => {
  const video = findLargestPlayingVideo();
  if (!video) {
    return;
  }
  if (video.hasAttribute('__pip__')) {
    document.exitPictureInPicture();
    return;
  }
  await requestPictureInPicture(video);
})();


```

