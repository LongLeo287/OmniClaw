---
id: github.com-nanocortex-metube-firefox-addon-482b2c8
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:01.799791
---

# KNOWLEDGE EXTRACT: github.com_nanocortex_metube-firefox-addon_482b2c8e
> **Extracted on:** 2026-04-01 14:35:27
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523996/github.com_nanocortex_metube-firefox-addon_482b2c8e

---

## File: `.gitignore`
```
.idea
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## 1.6.4 - 2025-11-16
- Add Strict Playlist Mode option to prevent downloading entire playlists (like YouTube Mixes) when only wanting to save the currently playing video, thanks to [@gmpbigsun](https://github.com/gmpbigsun)

## 1.6.3 - 2025-11-13
- Add keyboard shortcut (Ctrl+Shift+M / Cmd+Shift+M) to send current page to MeTube
- Show loading indicator in popup when using keyboard shortcuts or context menu
- Prevent duplicate requests when shortcut/context menu is triggered multiple times

## 1.6.2 - 2025-11-11
- Made SSO authentication opt-in with optional permissions (`<all_urls>`, `cookies`)
- Added privacy notice explaining why broad permissions are needed for SSO redirects
- Reduced default permissions to `activeTab`, `menus`, and `storage` only
- Improved error messages for authentication failures

## 1.6.1 - 2025-11-10
- Added customNamePrefix and autoStart fields to popup
- Added quality options 360p and 240p
- Added URL validation in options and popup
- Added test connection button in options page
- Added save success indicator in options page
- Improved error messages to show actual MeTube responses
- Fixed context menu default setting to be enabled on first install

## 1.6.0 - 2025-11-09
- Added support for authentication via browser cookies (fixes SSO/reverse proxy auth issues)
- Replaced XMLHttpRequest with modern fetch() API
- Improved error handling with better error messages
- Added permissions for cookies and all URLs (required for fetch with credentials)

## 1.5.0 - 2025-04-16
- Added One-click mode, which automatically send the current page to MeTube instance when you click the extension icon (no popup, default values)
- Changed Auto Start option to true by default
- Improved some options description

## 1.4.2 - 2025-04-15
- Fixed download folder not properly passed to MeTube when used from popup
- Improved options readability

## 1.4.1 - 2025-01-16
- Added missing formats and quality types
- Added options for folder, autoStart and customNamePrefix

## 1.4.0 - 2024-04-27
- Added loading spinner when queueing, thanks to [@elwynelwyn](https://github.com/elwynelwyn)
- Added ability to configure custom headers, thanks to [@elwynelwyn](https://github.com/elwynelwyn)

## 1.3.4 - 2023-03-19

- Added missing format types: WAV, Opus, M4A, Thumbnail
- Improved UI to be easier on the eyes

## 1.3.3 - 2022-02-07

- Added default quality and format option, thanks to [@aYUSHc137](https://github.com/ayushc137)
- Added url input field in popup, thanks to [@aYUSHc137](https://github.com/ayushc137)
- Fixed context menu action not working

## 1.3.2 - 2021-12-12

- Fixed shouldShowContextMenu() return BUG, thanks to [@ncwhale](https://github.com/ncwhale)

## 1.3.1 - 2021-12-01

- Added context menu switch, thanks to [@ncwhale](https://github.com/ncwhale)
 
## 1.3 - 2021-11-27

- Added popup when clicking toolbar button for better verbosity
- Added option to select quality and format

## 1.2 - 2021-11-06

- Added option in addon preferences to open MeTube instance in new tab

## 1.0-1.1 - 2021-10-13

- Initial version
```

## File: `LICENSE`
```
Mozilla Public License Version 2.0
==================================

1. Definitions
--------------

1.1. "Contributor"
    means each individual or legal entity that creates, contributes to
    the creation of, or owns Covered Software.

1.2. "Contributor Version"
    means the combination of the Contributions of others (if any) used
    by a Contributor and that particular Contributor's Contribution.

1.3. "Contribution"
    means Covered Software of a particular Contributor.

1.4. "Covered Software"
    means Source Code Form to which the initial Contributor has attached
    the notice in Exhibit A, the Executable Form of such Source Code
    Form, and Modifications of such Source Code Form, in each case
    including portions thereof.

1.5. "Incompatible With Secondary Licenses"
    means

    (a) that the initial Contributor has attached the notice described
        in Exhibit B to the Covered Software; or

    (b) that the Covered Software was made available under the terms of
        version 1.1 or earlier of the License, but not also under the
        terms of a Secondary License.

1.6. "Executable Form"
    means any form of the work other than Source Code Form.

1.7. "Larger Work"
    means a work that combines Covered Software with other material, in
    a separate file or files, that is not Covered Software.

1.8. "License"
    means this document.

1.9. "Licensable"
    means having the right to grant, to the maximum extent possible,
    whether at the time of the initial grant or subsequently, any and
    all of the rights conveyed by this License.

1.10. "Modifications"
    means any of the following:

    (a) any file in Source Code Form that results from an addition to,
        deletion from, or modification of the contents of Covered
        Software; or

    (b) any new file in Source Code Form that contains any Covered
        Software.

1.11. "Patent Claims" of a Contributor
    means any patent claim(s), including without limitation, method,
    process, and apparatus claims, in any patent Licensable by such
    Contributor that would be infringed, but for the grant of the
    License, by the making, using, selling, offering for sale, having
    made, import, or transfer of either its Contributions or its
    Contributor Version.

1.12. "Secondary License"
    means either the GNU General Public License, Version 2.0, the GNU
    Lesser General Public License, Version 2.1, the GNU Affero General
    Public License, Version 3.0, or any later versions of those
    licenses.

1.13. "Source Code Form"
    means the form of the work preferred for making modifications.

1.14. "You" (or "Your")
    means an individual or a legal entity exercising rights under this
    License. For legal entities, "You" includes any entity that
    controls, is controlled by, or is under common control with You. For
    purposes of this definition, "control" means (a) the power, direct
    or indirect, to cause the direction or management of such entity,
    whether by contract or otherwise, or (b) ownership of more than
    fifty percent (50%) of the outstanding shares or beneficial
    ownership of such entity.

2. License Grants and Conditions
--------------------------------

2.1. Grants

Each Contributor hereby grants You a world-wide, royalty-free,
non-exclusive license:

(a) under intellectual property rights (other than patent or trademark)
    Licensable by such Contributor to use, reproduce, make available,
    modify, display, perform, distribute, and otherwise exploit its
    Contributions, either on an unmodified basis, with Modifications, or
    as part of a Larger Work; and

(b) under Patent Claims of such Contributor to make, use, sell, offer
    for sale, have made, import, and otherwise transfer either its
    Contributions or its Contributor Version.

2.2. Effective Date

The licenses granted in Section 2.1 with respect to any Contribution
become effective for each Contribution on the date the Contributor first
distributes such Contribution.

2.3. Limitations on Grant Scope

The licenses granted in this Section 2 are the only rights granted under
this License. No additional rights or licenses will be implied from the
distribution or licensing of Covered Software under this License.
Notwithstanding Section 2.1(b) above, no patent license is granted by a
Contributor:

(a) for any code that a Contributor has removed from Covered Software;
    or

(b) for infringements caused by: (i) Your and any other third party's
    modifications of Covered Software, or (ii) the combination of its
    Contributions with other software (except as part of its Contributor
    Version); or

(c) under Patent Claims infringed by Covered Software in the absence of
    its Contributions.

This License does not grant any rights in the trademarks, service marks,
or logos of any Contributor (except as may be necessary to comply with
the notice requirements in Section 3.4).

2.4. Subsequent Licenses

No Contributor makes additional grants as a result of Your choice to
distribute the Covered Software under a subsequent version of this
License (see Section 10.2) or under the terms of a Secondary License (if
permitted under the terms of Section 3.3).

2.5. Representation

Each Contributor represents that the Contributor believes its
Contributions are its original creation(s) or it has sufficient rights
to grant the rights to its Contributions conveyed by this License.

2.6. Fair Use

This License is not intended to limit any rights You have under
applicable copyright doctrines of fair use, fair dealing, or other
equivalents.

2.7. Conditions

Sections 3.1, 3.2, 3.3, and 3.4 are conditions of the licenses granted
in Section 2.1.

3. Responsibilities
-------------------

3.1. Distribution of Source Form

All distribution of Covered Software in Source Code Form, including any
Modifications that You create or to which You contribute, must be under
the terms of this License. You must inform recipients that the Source
Code Form of the Covered Software is governed by the terms of this
License, and how they can obtain a copy of this License. You may not
attempt to alter or restrict the recipients' rights in the Source Code
Form.

3.2. Distribution of Executable Form

If You distribute Covered Software in Executable Form then:

(a) such Covered Software must also be made available in Source Code
    Form, as described in Section 3.1, and You must inform recipients of
    the Executable Form how they can obtain a copy of such Source Code
    Form by reasonable means in a timely manner, at a charge no more
    than the cost of distribution to the recipient; and

(b) You may distribute such Executable Form under the terms of this
    License, or sublicense it under different terms, provided that the
    license for the Executable Form does not attempt to limit or alter
    the recipients' rights in the Source Code Form under this License.

3.3. Distribution of a Larger Work

You may create and distribute a Larger Work under terms of Your choice,
provided that You also comply with the requirements of this License for
the Covered Software. If the Larger Work is a combination of Covered
Software with a work governed by one or more Secondary Licenses, and the
Covered Software is not Incompatible With Secondary Licenses, this
License permits You to additionally distribute such Covered Software
under the terms of such Secondary License(s), so that the recipient of
the Larger Work may, at their option, further distribute the Covered
Software under the terms of either this License or such Secondary
License(s).

3.4. Notices

You may not remove or alter the substance of any license notices
(including copyright notices, patent notices, disclaimers of warranty,
or limitations of liability) contained within the Source Code Form of
the Covered Software, except that You may alter any license notices to
the extent required to remedy known factual inaccuracies.

3.5. Application of Additional Terms

You may choose to offer, and to charge a fee for, warranty, support,
indemnity or liability obligations to one or more recipients of Covered
Software. However, You may do so only on Your own behalf, and not on
behalf of any Contributor. You must make it absolutely clear that any
such warranty, support, indemnity, or liability obligation is offered by
You alone, and You hereby agree to indemnify every Contributor for any
liability incurred by such Contributor as a result of warranty, support,
indemnity or liability terms You offer. You may include additional
disclaimers of warranty and limitations of liability specific to any
jurisdiction.

4. Inability to Comply Due to Statute or Regulation
---------------------------------------------------

If it is impossible for You to comply with any of the terms of this
License with respect to some or all of the Covered Software due to
statute, judicial order, or regulation then You must: (a) comply with
the terms of this License to the maximum extent possible; and (b)
describe the limitations and the code they affect. Such description must
be placed in a text file included with all distributions of the Covered
Software under this License. Except to the extent prohibited by statute
or regulation, such description must be sufficiently detailed for a
recipient of ordinary skill to be able to understand it.

5. Termination
--------------

5.1. The rights granted under this License will terminate automatically
if You fail to comply with any of its terms. However, if You become
compliant, then the rights granted under this License from a particular
Contributor are reinstated (a) provisionally, unless and until such
Contributor explicitly and finally terminates Your grants, and (b) on an
ongoing basis, if such Contributor fails to notify You of the
non-compliance by some reasonable means prior to 60 days after You have
come back into compliance. Moreover, Your grants from a particular
Contributor are reinstated on an ongoing basis if such Contributor
notifies You of the non-compliance by some reasonable means, this is the
first time You have received notice of non-compliance with this License
from such Contributor, and You become compliant prior to 30 days after
Your receipt of the notice.

5.2. If You initiate litigation against any entity by asserting a patent
infringement claim (excluding declaratory judgment actions,
counter-claims, and cross-claims) alleging that a Contributor Version
directly or indirectly infringes any patent, then the rights granted to
You by any and all Contributors for the Covered Software under Section
2.1 of this License shall terminate.

5.3. In the event of termination under Sections 5.1 or 5.2 above, all
end user license agreements (excluding distributors and resellers) which
have been validly granted by You or Your distributors under this License
prior to termination shall survive termination.

************************************************************************
*                                                                      *
*  6. Disclaimer of Warranty                                           *
*  -------------------------                                           *
*                                                                      *
*  Covered Software is provided under this License on an "as is"       *
*  basis, without warranty of any kind, either expressed, implied, or  *
*  statutory, including, without limitation, warranties that the       *
*  Covered Software is free of defects, merchantable, fit for a        *
*  particular purpose or non-infringing. The entire risk as to the     *
*  quality and performance of the Covered Software is with You.        *
*  Should any Covered Software prove defective in any respect, You     *
*  (not any Contributor) assume the cost of any necessary servicing,   *
*  repair, or correction. This disclaimer of warranty constitutes an   *
*  essential part of this License. No use of any Covered Software is   *
*  authorized under this License except under this disclaimer.         *
*                                                                      *
************************************************************************

************************************************************************
*                                                                      *
*  7. Limitation of Liability                                          *
*  --------------------------                                          *
*                                                                      *
*  Under no circumstances and under no legal theory, whether tort      *
*  (including negligence), contract, or otherwise, shall any           *
*  Contributor, or anyone who distributes Covered Software as          *
*  permitted above, be liable to You for any direct, indirect,         *
*  special, incidental, or consequential damages of any character      *
*  including, without limitation, damages for lost profits, loss of    *
*  goodwill, work stoppage, computer failure or malfunction, or any    *
*  and all other commercial damages or losses, even if such party      *
*  shall have been informed of the possibility of such damages. This   *
*  limitation of liability shall not apply to liability for death or   *
*  personal injury resulting from such party's negligence to the       *
*  extent applicable law prohibits such limitation. Some               *
*  jurisdictions do not allow the exclusion or limitation of           *
*  incidental or consequential damages, so this exclusion and          *
*  limitation may not apply to You.                                    *
*                                                                      *
************************************************************************

8. Litigation
-------------

Any litigation relating to this License may be brought only in the
courts of a jurisdiction where the defendant maintains its principal
place of business and such litigation shall be governed by laws of that
jurisdiction, without reference to its conflict-of-law provisions.
Nothing in this Section shall prevent a party's ability to bring
cross-claims or counter-claims.

9. Miscellaneous
----------------

This License represents the complete agreement concerning the subject
matter hereof. If any provision of this License is held to be
unenforceable, such provision shall be reformed only to the extent
necessary to make it enforceable. Any law or regulation which provides
that the language of a contract shall be construed against the drafter
shall not be used to construe this License against a Contributor.

10. Versions of the License
---------------------------

10.1. New Versions

Mozilla Foundation is the license steward. Except as provided in Section
10.3, no one other than the license steward has the right to modify or
publish new versions of this License. Each version will be given a
distinguishing version number.

10.2. Effect of New Versions

You may distribute the Covered Software under the terms of the version
of the License under which You originally received the Covered Software,
or under the terms of any subsequent version published by the license
steward.

10.3. Modified Versions

If you create software not governed by this License, and you want to
create a new license for such software, you may create and use a
modified version of this License if you rename the license and remove
any references to the name of the license steward (except to note that
such modified license differs from this License).

10.4. Distributing Source Code Form that is Incompatible With Secondary
Licenses

If You choose to distribute Source Code Form that is Incompatible With
Secondary Licenses under the terms of this version of the License, the
notice described in Exhibit B of this License must be attached.

Exhibit A - Source Code Form License Notice
-------------------------------------------

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

If it is not possible or desirable to put the notice in a particular
file, then You may include the notice in a location (such as a LICENSE
file in a relevant directory) where a recipient would be likely to look
for such a notice.

You may add additional accurate notices of copyright ownership.

Exhibit B - "Incompatible With Secondary Licenses" Notice
---------------------------------------------------------

  This Source Code Form is "Incompatible With Secondary Licenses", as
  defined by the Mozilla Public License, v. 2.0.
```

## File: `README.md`
```markdown
# Firefox MeTube addon

[![Firefox Add-on](https://img.shields.io/amo/v/metube-downloader?label=Firefox%20Add-on)](https://addons.mozilla.org/en-US/firefox/addon/metube-downloader)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![GitHub issues](https://img.shields.io/github/issues/nanocortex/metube-firefox-addon)](https://github.com/nanocortex/metube-firefox-addon/issues)

Browser extension for queueing videos to your [MeTube](https://github.com/alexta69/metube) instance.

### Context Menu Integration
![Context menu on video links](https://github.com/nanocortex/metube-firefox-addon/blob/master/assets/scr_context_menu.png?raw=true)

### Popup Interface
![Extension popup with options](https://github.com/nanocortex/metube-firefox-addon/blob/master/assets/scr_button.png?raw=true)

## Features

- **One-Click Sending** - Send current page to MeTube with a single click or keyboard shortcut
- **Context Menu Integration** - Right-click on links to send them directly to MeTube
- **Keyboard Shortcuts** - Customizable keyboard shortcut (default: Ctrl+Shift+M)
- **SSO Authentication Support** - Works with SSO systems like Authentik, Authelia, and Keycloak
- **Custom Headers** - Add custom HTTP headers for authentication or other purposes
- **Playlist Control** - Strict Playlist Mode prevents unwanted full playlist downloads
- **Flexible Configuration** - Control quality, format, folder, auto-start, and more

## Installation

Install from [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/metube-downloader)

See the [CHANGELOG](CHANGELOG.md) for version history and release notes.

## Usage

> **Note**: This extension requires a running [MeTube](https://github.com/alexta69/metube) instance. MeTube is a self-hosted YouTube downloader with a web interface. If you don't have MeTube set up yet, visit the [MeTube project](https://github.com/alexta69/metube) for installation instructions.

### Basic Usage

1. Configure your MeTube instance URL in addon preferences (`about:addons` → MeTube Downloader → Options)
2. Navigate to any video page (YouTube, Vimeo, etc.)
3. Send to MeTube using one of these methods:
   - Click the extension icon in the toolbar
   - Use the keyboard shortcut `Ctrl+Shift+M` (or `Cmd+Shift+M` on Mac)
   - Right-click on a video link and select "Send to MeTube" (if context menu is enabled)

### Keyboard Shortcuts

The extension supports the following keyboard shortcut:

- **Ctrl+Shift+M** (Windows/Linux) or **Cmd+Shift+M** (Mac) - Send current page to MeTube

You can customize this shortcut in Firefox:
1. Navigate to `about:addons`
2. Click the gear icon ⚙️ at the top
3. Select "Manage Extension Shortcuts"
4. Find "MeTube Downloader" and customize the "Send current page to MeTube" shortcut

### Enabling SSO Support

If your MeTube instance is behind SSO authentication (e.g., Authentik, Authelia, Keycloak):

1. Open extension settings (`about:addons` → MeTube Downloader → Options)
2. Enter your MeTube instance URL
3. Check the **"Send cookies for authentication (SSO)"** checkbox
4. Read the privacy notice that appears explaining why `<all_urls>` permission is needed
5. Click **"Save Settings"** - Firefox will prompt you to allow access to all websites
6. Open your MeTube instance in a browser tab and log in through your SSO provider
7. The extension will now use your existing session cookies to authenticate requests

## Options

| Option | Description | Default |
|--------|-------------|---------|
| **MeTube Instance URL** | URL of your MeTube instance (e.g., `https://metube.example.com`) | `""` (empty) |
| **Default Quality** | Quality setting for downloads | `best` |
| **Default Format** | Format for downloads | `any` |
| **Default Folder** | Folder where downloaded files will be saved | `""` (empty) |
| **Custom Name Prefix** | Prefix added to downloaded file names | `""` (empty) |
| **Open in New Tab** | Open MeTube instance in new tab after adding to queue | `false` |
| **Show Context Menu** | Display context menu on supported sites | `true` |
| **Auto Start** | Automatically start downloads when ready | `true` |
| **One-Click Mode** | Send current page to MeTube with one click | `false` |
| **Strict Playlist Mode** | Only download playlists when URL explicitly points to one (prevents downloading YouTube Mixes when you only want the current video) | `false` |
| **Send Custom Headers** | Enable inclusion of custom headers when queueing | `false` |
| **Custom Headers** | Specify custom header names and values for authentication or other purposes | `[]` (empty) |

## Permissions

This extension requires the following permissions:

- **Access browser tabs** (`activeTab`) - To get the current tab's URL when you want to send it to MeTube.
- **Display context menu** (`menus`) - To show the right-click context menu option.
- **Store data** (`storage`) - To save your MeTube instance URL and preferences.

**Optional permissions (requested at runtime when SSO is enabled):**
- **Access all websites** (`<all_urls>`) - Only requested if you enable "Send cookies for authentication (SSO)" in settings. This permission is necessary because SSO authentication systems redirect to different domains (e.g., Authentik, Authelia, Keycloak) for login. The extension only uses this to follow authentication redirects and will only actually access your MeTube instance and authentication provider. If your MeTube instance doesn't require SSO authentication, you can leave this option disabled and no permission will be requested.
- **Access cookies** - Required for SSO mode to send authentication cookies to your MeTube instance.

## Troubleshooting

### Connection Issues

**Error: "MeTube instance url not configured"**
- Go to `about:addons` → MeTube Downloader → Options and enter your MeTube URL

**Error: "Connection failed" with HTTP URLs (e.g., `http://server:5510`)**
- Firefox HTTPS-Only Mode blocks HTTP requests from extensions ([Firefox bug #1685862](https://bugzilla.mozilla.org/show_bug.cgi?id=1685862))
- **Important**: Site exceptions do NOT work for extension requests - this is a known Firefox limitation
- **Workaround**: Use direct IP address instead of hostname (e.g., `http://192.168.1.100:5510` instead of `http://server.local:5510`)
  - Firefox has built-in HTTPS-Only Mode exemptions for local IP addresses
- **Solution 1**: Disable HTTPS-Only Mode entirely (Settings → Privacy & Security → HTTPS-Only Mode → "Don't enable")
- **Solution 2**: Use HTTPS with a reverse proxy

**Error: "Connection failed" with HTTPS URLs**
- **Self-signed certificate**: Visit your MeTube URL in a browser tab first and accept the security warning/certificate
- **CORS not configured**: MeTube needs proper CORS headers (usually configured via reverse proxy)
- **SSO/Authentication**: Enable "Send cookies for authentication (SSO)" in extension settings (see [Enabling SSO Support](#enabling-sso-support))

**Error: "Authentication failed. Your MeTube instance is redirecting to authentication"**
- You need to log in to your MeTube instance first
- Open your MeTube URL in a regular browser tab and log in through your SSO provider
- Then try using the extension again from that same tab

### Debugging and Viewing Logs

To view detailed error messages and logs:
1. Navigate to `about:debugging#/runtime/this-firefox`
2. Find "MeTube Downloader" and click "Inspect"
3. Go to the Console tab
4. Try sending a video to MeTube and check the console for error details

### Other Issues

**Context menu not appearing**
- Go to extension settings and enable "Show Context Menu"

**One-click mode not working**
- Verify "One-Click Mode" is enabled in settings
- The extension popup will be disabled when one-click mode is active

For other issues, please [create an issue on GitHub](https://github.com/nanocortex/metube-firefox-addon/issues).

## Roadmap

- [x] keyboard shortcuts
- [ ] new tab in popup with download history
- [ ] option to customize the list of sites where the context menu will appear
- [ ] enhance the user interface for settings (maybe in separate tab)
- [ ] dark/light mode theme support for popup and options pages
- [ ] Chrome/Edge browser port (cross-browser compatibility)
- [ ] mobile Firefox support (optimize UI for Firefox on Android)
- [ ] upgrade to Manifest V3
- [x] Github Actions for creating releases (maybe publish to Mozilla too?)

## Development

### Loading for Development
1. Navigate to `about:debugging#/runtime/this-firefox`
2. Click "Load Temporary Add-on"
3. Select `src/manifest.json` from this repository

## Support

Having issues? Check the [Troubleshooting](#troubleshooting) section above or [create an issue on GitHub](https://github.com/nanocortex/metube-firefox-addon/issues).

## Contributing

If you would like to contribute, please [create an issue](https://github.com/nanocortex/metube-firefox-addon/issues) or make a pull request.

Thanks to the following contributors for their work on this project:

-  [Whale Mo](https://github.com/ncwhale)
-  [Elwyn](https://github.com/elwynelwyn)
-  [Ayush Chaurasia](https://github.com/ayushc137)
-  [gmpbigsun](https://github.com/gmpbigsun)

## License

This project is licensed under the [Mozilla Public License Version 2.0](LICENSE).
```

## File: `package.sh`
```bash
#!/bin/sh

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
VERSION=$(grep -o '"version": "[^"]*"' ./src/manifest.json | cut -d'"' -f4)
VERSION_CLEAN=$(echo $VERSION | tr -d '.')

7z a -tzip metube_v${VERSION_CLEAN}_${TIMESTAMP}.zip ./src/*
```

## File: `release.sh`
```bash
#!/bin/sh

# Check if version parameter is provided
if [ -z "$1" ]; then
  echo "Usage: ./release.sh <version>"
  echo "Example: ./release.sh 1.6.1"
  exit 1
fi

NEW_VERSION=$1

# Validate version format (basic check)
if ! echo "$NEW_VERSION" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "Error: Invalid version format. Use semantic versioning (e.g., 1.6.1)"
  exit 1
fi

# Get current version from manifest.json
CURRENT_VERSION=$(grep -o '"version": "[^"]*"' ./src/manifest.json | cut -d'"' -f4)

if [ -z "$CURRENT_VERSION" ]; then
  echo "Error: Could not extract current version from manifest.json"
  exit 1
fi

echo "Current version: $CURRENT_VERSION"
echo "New version: $NEW_VERSION"
echo ""

# Check if there are uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
  echo "Error: You have uncommitted changes. Please commit or stash them first."
  git status --short
  exit 1
fi

# Check if tag already exists
if git rev-parse "v$NEW_VERSION" >/dev/null 2>&1; then
  echo "Error: Tag v$NEW_VERSION already exists"
  exit 1
fi

# Confirm with user
echo "This will:"
echo "  1. Update version in src/manifest.json to $NEW_VERSION"
echo "  2. Open CHANGELOG.md for you to add release notes"
echo "  3. Commit the changes"
echo "  4. Create and push tag v$NEW_VERSION"
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "Cancelled"
  exit 0
fi

# Update version in manifest.json
echo "Updating manifest.json..."
sed -i '' "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" ./src/manifest.json

# Verify the change
NEW_MANIFEST_VERSION=$(grep -o '"version": "[^"]*"' ./src/manifest.json | cut -d'"' -f4)
if [ "$NEW_MANIFEST_VERSION" != "$NEW_VERSION" ]; then
  echo "Error: Failed to update version in manifest.json"
  exit 1
fi

echo "Version updated successfully in manifest.json"

# Prepare CHANGELOG.md entry
CHANGELOG_DATE=$(date +"%Y-%m-%d")
CHANGELOG_ENTRY="## $NEW_VERSION - $CHANGELOG_DATE\n- \n"

# Check if CHANGELOG.md exists
if [ -f "CHANGELOG.md" ]; then
  # Add new entry after the first line (# Changelog)
  sed -i '' "2i\\
\\
$CHANGELOG_ENTRY
" CHANGELOG.md

  echo ""
  echo "CHANGELOG.md has been updated with a template entry."
  echo "Opening CHANGELOG.md for you to add release notes..."
  echo ""

  # Open CHANGELOG.md in default editor
  ${EDITOR:-vi} CHANGELOG.md

  echo ""
  read -p "Have you finished editing CHANGELOG.md? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled. Please edit CHANGELOG.md and commit manually."
    exit 1
  fi
else
  echo "Warning: CHANGELOG.md not found, skipping..."
fi

# Commit the version change
echo "Committing version change..."
git add ./src/manifest.json CHANGELOG.md
git commit -m "Bump version to $NEW_VERSION"

# Create and push tag
echo "Creating tag v$NEW_VERSION..."
git tag "v$NEW_VERSION"

echo "Pushing changes and tag to origin..."
git push origin master
git push origin "v$NEW_VERSION"

echo ""
echo "Done! Version $NEW_VERSION has been released."
echo "Check: https://github.com/nanocortex/metube-firefox-addon/actions"
```

## File: `src/background.js`
```javascript
let isRequestInProgress = false;

function onMenuCreated() {
  if (browser.runtime.lastError) {
    console.log("error creating item:" + browser.runtime.lastError);
  }

  syncContextMenu().then(() => {
    console.log("Context menu synced");
  });
}

async function syncContextMenu() {
  let showContextMenu = await shouldShowContextMenu();
  browser.menus.update("send-to-metube", {
    visible: showContextMenu,
  });
}

browser.browserAction.onClicked.addListener(async () => {
  const oneClickMode = await getOneClickMode();

  if (oneClickMode) {
    const url = await getCurrentUrl();
    const options = await getDefaultSendOptions();
    await sendToMeTube(url, options.quality, options.format, options.folder,
                       options.customNamePrefix, options.autoStart, options.strictPlaylistMode);
  }
});

browser.menus.create({
  id: "send-to-metube",
  title: "Send to MeTube",
  contexts: ["link"]
}, onMenuCreated);

async function showError(errorMessage) {
  console.error(`Error occurred: ${errorMessage}`)
  try {
    await browser.runtime.sendMessage({ command: 'errorOccurred', errorMessage: errorMessage });
  } catch (e) {
    console.log(`Popup closed, cannot display error message`);
  }
}

async function showSuccess() {
  console.log('Successfully sent to MeTube');
  try {
    await browser.runtime.sendMessage({ command: 'success' });
  } catch (e) {
    console.log('Popup closed, cannot display success message');
  }
}

async function getMeTubeUrl() {
  let item = await browser.storage.sync.get("url");
  return item.url;
}

async function shouldOpenInNewTab() {
  let item = await browser.storage.sync.get("openInNewTab");
  return item.openInNewTab;
}

async function shouldShowContextMenu() {
  let item = await browser.storage.sync.get("showContextMenu");
  return 'showContextMenu' in item ? item.showContextMenu : true;
}

async function shouldSendCustomHeaders() {
  let item = await browser.storage.sync.get("sendCustomHeaders");
  return item.sendCustomHeaders ?? false;
}

async function customHeaders() {
  let item = await browser.storage.sync.get("customHeaders");
  return item.customHeaders ?? [];
}

async function getOneClickMode() {
  let item = await browser.storage.sync.get("oneClickMode");
  return item.oneClickMode ?? false;
}

async function shouldUseCookieAuth() {
  let item = await browser.storage.sync.get("useCookieAuth");
  return item.useCookieAuth ?? false;
}

async function updateBrowserActionPopup() {
  const oneClickMode = await getOneClickMode();

  if (oneClickMode) {
    browser.browserAction.setPopup({ popup: "" });
  } else {
    browser.browserAction.setPopup({ popup: "popup/popup.html" });
  }
}

async function getDefaultSendOptions() {
  return {
    quality: await getDefaultQuality(),
    format: await getDefaultFormat(),
    folder: await getDefaultFolder(),
    customNamePrefix: await getDefaultCustomNamePrefix(),
    autoStart: await getDefaultAutoStart(),
    strictPlaylistMode: await getDefaultStrictPlaylistMode()
  };
}

async function sendToMeTube(itemUrl, quality, format, folder, customNamePrefix, autoStart, strictPlaylistMode) {
  if (isRequestInProgress) {
    console.log("Request already in progress, ignoring duplicate request");
    return;
  }

  isRequestInProgress = true;

  try {
    itemUrl = itemUrl || await getCurrentUrl();
    console.log(`Send to MeTube. Url: ${itemUrl}, quality: ${quality}, format: ${format}, folder: ${folder}, customNamePrefix: ${customNamePrefix}, autoStart: ${autoStart}, strictPlaylistMode: ${strictPlaylistMode}`);
    let meTubeUrl = await getMeTubeUrl();
    if (!meTubeUrl) {
      await showError('MeTube instance url not configured. Go to about:addons to configure.');
      return;
    }

    let url = new URL("add", meTubeUrl);

    const headers = {
      "Content-Type": "application/json"
    };

    const useCustomHeaders = await shouldSendCustomHeaders();
    if (useCustomHeaders) {
      const customHeadersList = await customHeaders();
      customHeadersList.forEach(header => {
        headers[header.name] = header.value;
      });
    }

    const useCookieAuth = await shouldUseCookieAuth();

    try {
      const response = await fetch(url.toString(), {
        method: "POST",
        credentials: useCookieAuth ? "include" : "omit",
        headers: headers,
        body: JSON.stringify({
          "url": itemUrl,
          "quality": quality,
          "format": format,
          "folder": folder,
          "custom_name_prefix": customNamePrefix,
          "auto_start": autoStart,
          "playlist_strict_mode": strictPlaylistMode
        })
      });

      if (response.ok) {
        await showSuccess();
        if (await shouldOpenInNewTab()) {
          await browser.tabs.create({ 'active': true, 'url': meTubeUrl });
        }
      } else {
        const contentType = response.headers.get('content-type');
        let errorMessage;

        if (contentType && contentType.includes('application/json')) {
          const errorData = await response.json();
          errorMessage = errorData.error || errorData.message || JSON.stringify(errorData);
        } else {
          errorMessage = await response.text();
        }

        if (errorMessage) {
          await showError(`MeTube error: ${errorMessage}`);
        } else {
          await showError(`MeTube error (HTTP ${response.status}): ${response.statusText}`);
        }
        console.error("Send to MeTube failed. MeTube url: " + url.toString() + ", itemUrl: " + itemUrl + ", status: " + response.status);
      }
    } catch (error) {
      if (error.message.includes('NetworkError') || error.message.includes('CORS')) {
        console.error("Network error details:", error, "MeTube URL:", meTubeUrl);

        if (meTubeUrl.startsWith('http://')) {
          await showError('Connection failed with HTTP URL. Common causes: 1) Firefox HTTPS-Only Mode (check about:debugging console for "HTTPS-Only Mode" messages), 2) CORS restrictions, 3) MeTube unreachable. If using HTTPS-Only Mode, you must disable it entirely - site exceptions don\'t work for extensions.');
        } else if (meTubeUrl.startsWith('https://')) {
          await showError('Connection failed with HTTPS URL. Common causes: 1) Self-signed/invalid certificate (visit MeTube URL in a tab first and accept it), 2) CORS not configured, 3) MeTube unreachable. Check about:debugging console for details.');
        } else {
          await showError('Connection failed. Check that MeTube URL is correct and reachable. View logs at about:debugging for details.');
        }
      } else {
        await showError(`Network error: ${error.message}. Check that MeTube URL is correct: ${meTubeUrl}`);
      }
      console.error("Network error:", error);
    }
  } finally {
    isRequestInProgress = false;
  }
}

function triggerSendWithLoading(url) {
  setTimeout(async () => {
    try {
      await browser.runtime.sendMessage({ command: 'showLoading' });
    } catch (error) {
      console.error("Failed to send showLoading message:", error);
    }

    const options = await getDefaultSendOptions();
    await sendToMeTube(url, options.quality, options.format, options.folder,
                       options.customNamePrefix, options.autoStart, options.strictPlaylistMode);
  }, 100);
}

async function sendWithLoadingIndicator(url) {
  browser.browserAction.setPopup({ popup: "popup/popup.html" });
  browser.browserAction.openPopup();
  triggerSendWithLoading(url);
}

browser.menus.onClicked.addListener(async function(info, tab) {
  if (info.menuItemId === "send-to-metube" && info.linkUrl) {
    await sendWithLoadingIndicator(info.linkUrl);
  }
});

browser.runtime.onMessage.addListener(async (message) => {
  if (message.command === "sendToMeTube") {
    let url = message.url || await getCurrentUrl();
    let quality = message.quality || 'best';
    let format = message.format || 'any';
    let folder = message.folder || await getDefaultFolder();
    let customNamePrefix = message.customNamePrefix || await getDefaultCustomNamePrefix();
    let autoStart = message.autoStart || await getDefaultAutoStart();
    let strictPlaylistMode = message.strictPlaylistMode || await getDefaultStrictPlaylistMode();
    await sendToMeTube(url, quality, format, folder, customNamePrefix, autoStart, strictPlaylistMode);
  } else if (message.command === "settingsUpdated") {
    await updateBrowserActionPopup();
  }

});


updateBrowserActionPopup();

browser.commands.onCommand.addListener(async (command) => {
  if (command === "send-to-metube") {
    browser.browserAction.setPopup({ popup: "popup/popup.html" });
    browser.browserAction.openPopup();

    const url = await getCurrentUrl();
    triggerSendWithLoading(url);
  }
});

// Listen for storage changes to update browser action popup
browser.storage.onChanged.addListener(async (changes) => {
  if ('oneClickMode' in changes) {
    await updateBrowserActionPopup();
  }
});
```

## File: `src/manifest.json`
```json
{
  "manifest_version": 2,
  "name": "MeTube Downloader",
  "version": "1.6.4",
  "description": "Queue download to your MeTube instance",
  "permissions": [
    "activeTab",
    "menus",
    "storage"
  ],
  "optional_permissions": [
    "<all_urls>",
    "cookies"
  ],
  "homepage_url": "https://github.com/nanocortex/metube-firefox-addon",
  "icons": {
    "48": "icons/icon-48.png"
  },
  "background": {
    "scripts": [
      "common/utils.js",
      "background.js"
    ]
  },
  "options_ui": {
    "page": "options/options.html",
    "browser_style": true
  },
  "browser_action": {
    "default_icon": {
      "19": "icons/icon-19.png",
      "38": "icons/icon-38.png"
    },
    "default_title": "Send to MeTube"
  },
  "commands": {
    "send-to-metube": {
      "suggested_key": {
        "default": "Ctrl+Shift+M"
      },
      "description": "Send current page to MeTube"
    }
  },
  "browser_specific_settings": {
    "gecko": {
      "id": "{6c6751df-7510-4e27-9637-9ae354c86f8c}"
    }
  }
}
```

## File: `src/common/common.css`
```css
.hidden {
  display: none;
}

.text-danger {
  color: tomato;
}

.text-success {
  color: green;
}
```

## File: `src/common/utils.js`
```javascript
async function getCurrentUrl() {
  let tabs = await browser.tabs.query({ currentWindow: true, active: true });
  return tabs[0].url;
}

async function getDefaultQuality() {
  let item = await browser.storage.sync.get("defaultQuality");
  return item.defaultQuality ?? 'best';
}

async function getDefaultFormat() {
  let item = await browser.storage.sync.get("defaultFormat");
  return item.defaultFormat ?? 'any';
}

async function getDefaultFolder() {
  let item = await browser.storage.sync.get("defaultFolder");
  return item.defaultFolder ?? '';
}

async function getDefaultCustomNamePrefix() {
  let item = await browser.storage.sync.get("defaultCustomNamePrefix");
  return item.defaultCustomNamePrefix ?? '';
}

async function getDefaultAutoStart() {
  let item = await browser.storage.sync.get("defaultAutoStart");
  return item.defaultAutoStart ?? true;
}

async function getDefaultStrictPlaylistMode() {
  let item = await browser.storage.sync.get("strictPlaylistMode");
  return item.strictPlaylistMode ?? false;
}

async function requestPermissionsForUrl(url, useCookieAuth) {
  try {
    const permissionRequest = {};

    if (useCookieAuth) {
      // For SSO, request <all_urls> to handle authentication redirects
      permissionRequest.origins = ["<all_urls>"];
      permissionRequest.permissions = ["cookies"];
    } else {
      // Without SSO, only request specific domain
      const urlObj = new URL(url);
      const origin = `${urlObj.protocol}//${urlObj.host}/*`;
      permissionRequest.origins = [origin];
    }

    return await browser.permissions.request(permissionRequest);
  } catch (error) {
    console.error("Error requesting permission:", error);
    return false;
  }
}
```

## File: `src/options/options.css`
```css
.section {
  border: 1px solid #ccc;
  padding: 0 1rem;
  margin-bottom: 1rem;
}

.inline-form-fields {
  display: flex;
  align-items: flex-end;
  gap: 0.5rem;
}

.inline-form-fields input {
  display: block;
}

.list-unstyled {
  list-style: none;
  padding: 0;
}

.header-pair {
  display: flex;
  gap: 0.5rem;
}

.header-pair code {
  border: 1px solid #ccc;
  background-color: #eee;
  padding: 0.25rem;
}

#saveSuccessMessage {
  margin-top: 0.5rem;
}

.field {
  margin-bottom: .75rem;
}

.field input[type="text"],
.field select {
  display: block;
  margin-top: 0.25rem;
}

#testConnectionMessage {
  margin-top: 0.25rem;
  font-size: 0.9em;
}
```

## File: `src/options/options.html`
```html
<!doctype html>

<html>
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="../common/common.css" />
    <link rel="stylesheet" href="options.css" />
  </head>

  <body>
    <form>
      <fieldset>
        <legend>Settings:</legend>
        <div class="field">
          <label for="url">MeTube instance url</label><br />
          <input type="text" id="url" placeholder="https://metube.example.com" />
          <div id="urlValidationMessage" class="text-danger"></div>
          <div id="testConnectionMessage"></div>
        </div>
        <div class="field">
          <label for="defaultQuality">Default quality:</label>
          <select name="defaultQuality" id="defaultQuality">
            <option value="best">Best</option>
            <option value="2160">2160p</option>
            <option value="1440">1440p</option>
            <option value="1080">1080p</option>
            <option value="720">720p</option>
            <option value="480">480p</option>
            <option value="360">360p</option>
            <option value="240">240p</option>
            <option value="worst">Worst</option>
            <option value="audio">Audio only</option>
          </select>
        </div>
        <div class="field">
          <label for="defaultFormat">Default format:</label>
          <select name="defaultFormat" id="defaultFormat">
            <option value="any">Any</option>
            <option value="mp4">MP4</option>
            <option value="m4a">M4A</option>
            <option value="mp3">MP3</option>
            <option value="opus">OPUS</option>
            <option value="wav">WAV</option>
            <option value="flac">FLAC</option>
            <option value="thumbnail">Thumbnail</option>
          </select>
        </div>
        <div class="field">
          <label for="defaultFolder">Default folder</label><br />
          <input type="text" id="defaultFolder" placeholder="" />
        </div>
        <div class="field">
          <label for="defaultCustomNamePrefix">Custom name prefix</label><br />
          <input type="text" id="defaultCustomNamePrefix" placeholder="" />
        </div>
        <div class="field">
          <input type="checkbox" id="openInNewTab" />
          <label for="openInNewTab">Open MeTube instance in new tab after adding to queue</label>
        </div>
        <div class="field">
          <input type="checkbox" id="showContextMenu" />
          <label for="showContextMenu">Show context menu in supported sites, e.g. YouTube, Vimeo, etc.</label>
        </div>
        <div class="field">
          <input type="checkbox" id="defaultAutoStart" />
          <label for="defaultAutoStart">Auto Start - automatically start the download when the file is ready</label>
        </div>
        <div class="field">
          <input type="checkbox" id="oneClickMode" />
          <label for="oneClickMode">One-click mode - automatically send the current page to MeTube instance when you click the extension icon (no popup, default values)</label>
        </div>
        <div class="field">
          <input type="checkbox" id="strictPlaylistMode" />
          <label for="strictPlaylistMode">Strict Playlist Mode - only download playlists when URL explicitly points to a playlist</label>
        </div>
        <div class="field">
          <input type="checkbox" id="useCookieAuth" />
          <label for="useCookieAuth">Send cookies for authentication (required for SSO/reverse proxy auth)</label>
          <div id="ssoWarning" class="hidden" style="margin-top: 0.5rem; padding: 0.5rem; background-color: #fff3cd; border: 1px solid #ffc107; border-radius: 4px;">
            <strong>⚠️ Privacy Notice:</strong> SSO mode requires access to all websites to follow authentication redirects. The extension will only access your MeTube instance and authentication provider. This permission is necessary because SSO systems can redirect to different domains for login.
          </div>
        </div>
        <div class="field">
          <input type="checkbox" id="sendCustomHeaders" />
          <label for="sendCustomHeaders">Send custom headers</label>
        </div>
        <section id="customHeadersSection" class="section hidden">
          <p>Custom headers which are included when queueing to MeTube instance.</p>
          <p>These can be used to provide credentials if your MeTube instance is behind a proxy or auth service.</p>
          <div class="inline-form-fields">
            <div>
              <label for="headerNameInput">Header name:</label>
              <input type="text" id="headerNameInput" placeholder="X-Foo-Header" />
            </div>
            <div>
              <label for="headerValueInput">Header value:</label>
              <input type="text" id="headerValueInput" placeholder="some-custom-value" />
            </div>
            <button type="button" id="addHeaderButton" aria-label="Add custom header">➕</button>
          </div>
          <div id="headerValidationMessage" class="text-danger"></div>
          <ul id="headersList" class="list-unstyled"></ul>
        </section>
        <button type="submit">Save Settings</button>
        <div id="saveSuccessMessage" class="text-success hidden"></div>
      </fieldset>
    </form>

    <script src="../common/utils.js"></script>
    <script src="options.js"></script>
  </body>
</html>
```

## File: `src/options/options.js`
```javascript
let connectionTested = false;

async function saveOptions(e) {
  e.preventDefault();

  let showContextMenu = document.querySelector("#showContextMenu").checked;
  let url = document.querySelector("#url").value.trim();
  let urlValidationMessageEl = document.getElementById("urlValidationMessage");

  if (!url) {
    urlValidationMessageEl.innerText = 'MeTube URL is required';
    return;
  }

  if (!url.startsWith('http://') && !url.startsWith('https://')) {
    urlValidationMessageEl.innerText = 'URL must start with http:// or https://';
    return;
  }

  try {
    new URL(url);
  } catch (error) {
    urlValidationMessageEl.innerText = 'Invalid URL format';
    return;
  }
  urlValidationMessageEl.innerText = '';

  let useCookieAuth = document.querySelector("#useCookieAuth").checked;

  // Request permissions if SSO is enabled
  if (useCookieAuth) {
    const granted = await requestPermissionsForUrl(url, useCookieAuth);
    if (!granted) {
      urlValidationMessageEl.innerText = 'Permission denied. Cannot enable SSO without permissions.';
      return;
    }
  }

  browser.storage.sync.set({
    url: url,
    defaultQuality: document.querySelector("#defaultQuality").value,
    defaultFormat: document.querySelector("#defaultFormat").value,
    openInNewTab: document.querySelector("#openInNewTab").checked,
    showContextMenu,
    useCookieAuth: document.querySelector("#useCookieAuth").checked,
    sendCustomHeaders: document.querySelector("#sendCustomHeaders").checked,
    customHeaders: Array.from(document.querySelectorAll('.header-pair')).map(el => ({ name: el.dataset.name, value: el.dataset.value })),
    defaultFolder: document.querySelector("#defaultFolder").value,
    defaultCustomNamePrefix: document.querySelector("#defaultCustomNamePrefix").value,
    defaultAutoStart: document.querySelector("#defaultAutoStart").checked,
    oneClickMode: document.querySelector("#oneClickMode").checked,
    strictPlaylistMode: document.querySelector("#strictPlaylistMode").checked,
  });

  browser.menus.update("send-to-metube", {
    visible: showContextMenu,
  });

  browser.runtime.sendMessage({ command: 'settingsUpdated' });

  const saveSuccessMessageEl = document.getElementById("saveSuccessMessage");
  saveSuccessMessageEl.innerText = '✓ Settings saved!';
  saveSuccessMessageEl.className = 'text-success';
  saveSuccessMessageEl.classList.remove("hidden");

  setTimeout(() => {
    saveSuccessMessageEl.classList.add("hidden");
  }, 3000);
}

function restoreOptions() {
  function onError(error) {
    console.log(`Error: ${error}`);
  }

  let getUrl = browser.storage.sync.get("url");
  getUrl.then(function(result) {
    document.querySelector("#url").value = result.url || "";
  }, onError);

  let getDefaultQuality = browser.storage.sync.get("defaultQuality");
  getDefaultQuality.then(function(result) {
    document.querySelector("#defaultQuality").value = result.defaultQuality || "best";
  }, onError);

  let getDefaultFormat = browser.storage.sync.get("defaultFormat");
  getDefaultFormat.then(function(result) {
    document.querySelector("#defaultFormat").value = result.defaultFormat || "any";
  }, onError);

  let getOpenInNewTab = browser.storage.sync.get("openInNewTab");
  getOpenInNewTab.then(function(result) {
    document.querySelector("#openInNewTab").checked = result.openInNewTab || false;
  }, onError);

  let showContextMenu = browser.storage.sync.get("showContextMenu");
  showContextMenu.then(function(result) {
    document.querySelector("#showContextMenu").checked = result.showContextMenu || true;
  }, onError);

  let sendCustomHeaders = browser.storage.sync.get("sendCustomHeaders");
  sendCustomHeaders.then(function(result) {
    document.querySelector("#sendCustomHeaders").checked = result.sendCustomHeaders;
    result.sendCustomHeaders ? showCustomHeadersSection() : hideCustomHeadersSection();
  });

  let customHeaders = browser.storage.sync.get("customHeaders");
  customHeaders.then(function(result) {
    result.customHeaders?.forEach(header => addCustomHeader(header));
  }, onError);

  let getDefaultFolder = browser.storage.sync.get("defaultFolder");
  getDefaultFolder.then(function(result) {
    document.querySelector("#defaultFolder").value = result.defaultFolder || "";
  }, onError);

  let getDefaultCustomNamePrefix = browser.storage.sync.get("defaultCustomNamePrefix");
  getDefaultCustomNamePrefix.then(function(result) {
    document.querySelector("#defaultCustomNamePrefix").value = result.defaultCustomNamePrefix || "";
  }, onError);

  let getDefaultAutoStart = browser.storage.sync.get("defaultAutoStart");
  getDefaultAutoStart.then(function(result) {
    document.querySelector("#defaultAutoStart").checked = result.defaultAutoStart || true;
  }, onError);

  let getOneClickMode = browser.storage.sync.get("oneClickMode");
  getOneClickMode.then(function(result) {
    document.querySelector("#oneClickMode").checked = result.oneClickMode || false;
  }, onError);

  let getStrictPlaylistMode = browser.storage.sync.get("strictPlaylistMode");
  getStrictPlaylistMode.then(function(result) {
    document.querySelector("#strictPlaylistMode").checked = result.strictPlaylistMode || false;
  }, onError);

  let getUseCookieAuth = browser.storage.sync.get("useCookieAuth");
  getUseCookieAuth.then(function(result) {
    const useCookieAuth = result.useCookieAuth || false;
    document.querySelector("#useCookieAuth").checked = useCookieAuth;
    // Show warning if SSO is already enabled
    if (useCookieAuth) {
      document.getElementById("ssoWarning").classList.remove("hidden");
    }
  }, onError);
}

function showCustomHeadersSection() {
  document.getElementById("customHeadersSection")?.classList.remove("hidden");
}

function hideCustomHeadersSection() {
  document.getElementById("customHeadersSection")?.classList.add("hidden");
}

function setupCustomHeadersSection() {
  const headerNameInput = document.getElementById("headerNameInput");
  const headerValueInput = document.getElementById("headerValueInput");
  const addHeaderButton = document.getElementById("addHeaderButton");
  const headerValidationMessageEl = document.getElementById("headerValidationMessage");

  document.getElementById("sendCustomHeaders").addEventListener("change", (event) => {
    event.target.checked ? showCustomHeadersSection() : hideCustomHeadersSection();
  });

  addHeaderButton.addEventListener("click", () => {
    const name = headerNameInput.value;
    const value = headerValueInput.value;

    let validationError = '';
    if (!name || !value) {
      validationError = 'Enter a header name and value';
    }

    headerValidationMessageEl.innerText = validationError;
    if (validationError) {
      return;
    }

    addCustomHeader({ name, value });

    headerNameInput.value = '';
    headerValueInput.value = '';
  });
}

function removeCustomHeader(header) {
  const headersList = document.getElementById('headersList');
  headersList.querySelector(`[data-name="${header.name}"]`)?.remove();
}

function addCustomHeader(header) {
  const headersList = document.getElementById('headersList');

  const listItem = document.createElement('li');
  listItem.classList.add('header-pair');
  listItem.dataset.name = header.name;
  listItem.dataset.value = header.value;

  const codeName = document.createElement('code');
  const codeValue = document.createElement('code');
  codeName.textContent = header.name;
  codeValue.textContent = header.value;

  listItem.append(codeName, codeValue);

  const removeBtn = document.createElement('button');
  removeBtn.type = 'button';
  removeBtn.setAttribute('aria-label', 'Remove custom header');
  removeBtn.innerText = '➖';
  removeBtn.addEventListener('click', () => removeCustomHeader(header));
  listItem.appendChild(removeBtn);

  headersList.appendChild(listItem);
}

document.addEventListener("DOMContentLoaded", setupCustomHeadersSection);
document.addEventListener("DOMContentLoaded", restoreOptions);
document.querySelector("form").addEventListener("submit", saveOptions);

document.getElementById("url").addEventListener("input", () => {
  connectionTested = false;
  document.getElementById("testConnectionMessage").innerText = '';
});

// Show/hide SSO warning
document.getElementById("useCookieAuth").addEventListener("change", (event) => {
  const ssoWarning = document.getElementById("ssoWarning");
  if (event.target.checked) {
    ssoWarning.classList.remove("hidden");
  } else {
    ssoWarning.classList.add("hidden");
  }
});
```

## File: `src/popup/popup.css`
```css
html,
body {
  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
  width: 300px;
  color: #CFD8DC;
  background: #263238;
}

#popup-content,
#error-content,
#success-content {
  text-align: center;
}

#popup-content div#options-row {
  display: flex;
  justify-content: space-between;
  margin-top: .75rem;
}

#popup-content div#options-row #quality-container {
  margin-right: .5rem;
}

label {
  color: #dedede;
  font-size: 12px;
  margin-bottom: .4rem !important;
  display: inline-block;
  text-align: left !important;
  font-weight: 600;
}

select {
  width: 100%;
  border: none;
  border-radius: 0.25em;
  padding: 0.4rem 0.75rem;
  border: solid 1px #455A64;
  background-color: #455A64;
  color: #CFD8DC;

}

#buttons-row {
  display: flex;
  justify-content: flex-end;
  margin-top: 1rem;
}

#buttons-row button {
  background-color: #0D47A1;
  border: 1px solid #0D47A1;
  border-radius: 6px;
  box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
  box-sizing: border-box;
  color: #fafafa;
  cursor: pointer;
  display: inline-block;
  font-size: .9em;
  font-weight: 700;
  line-height: 16px;
  min-height: 40px;
  outline: 0;
  padding: 12px 14px;
  text-align: center;
  touch-action: manipulation;
  vertical-align: middle;
  transition: all .1s ease;
  width: 100%;
  margin-bottom: .25rem;
}

#buttons-row button:hover,
#buttons-row button:active {
  transition: all .1s ease;
  opacity: .8;
}

#buttons-row button:active {
  opacity: .5;
}

.row {
  margin-top: .75rem;
}

input[type="text"] {
  width: 100%;
  font-size: 12px;
  box-sizing: border-box;
  border: 1px solid #455A64;
  background-color: #455A64;
  border-radius: .25em;
  padding: 0.4rem 0.75rem;
  color: #CFD8DC;
}

input::placeholder {
  color: #CFD8DC;
}

.send-to-metube {
  display: flex !important;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.spinner {
  width: 1rem;
  height: 1rem;
  border: 3px solid rgba(255, 255, 255, .3);
  border-radius: 50%;
  border-top-color: #fff;
  animation: spin 1s ease-in-out infinite;
  -webkit-animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to {
    -webkit-transform: rotate(360deg);
  }
}

@-webkit-keyframes spin {
  to {
    -webkit-transform: rotate(360deg);
  }
}


#history {
  font-size: 11px;
  text-align: left;
}

#history ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.validation-error {
  color: tomato;
  font-size: 0.85em;
  margin-top: 0.25rem;
}
```

## File: `src/popup/popup.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>MeTube extension popup</title>
    <link rel="stylesheet" href="../common/common.css" />
    <link rel="stylesheet" href="popup.css" />
  </head>

  <body>
    <div id="popup-content">
      <div class="row">
        <label for="urlInput">URL</label>
        <input id="urlInput" type="text" placeholder="URL" />
        <div id="urlValidationMessage" class="validation-error hidden"></div>
      </div>
      <div id="options-row">
        <div id="quality-container">
          <label for="quality">Quality</label>
          <select name="quality" id="quality">
            <option value="best">Best</option>
            <option value="2160">2160p</option>
            <option value="1440">1440p</option>
            <option value="1080">1080p</option>
            <option value="720">720p</option>
            <option value="480">480p</option>
            <option value="360">360p</option>
            <option value="240">240p</option>
            <option value="worst">Worst</option>
            <option value="audio">Audio only</option>
          </select>
        </div>
        <div id="format-container">
          <label for="format">Format</label>
          <select name="format" id="format">
            <option value="any">Any</option>
            <option value="mp4">MP4</option>
            <option value="m4a">M4A</option>
            <option value="mp3">MP3</option>
            <option value="opus">OPUS</option>
            <option value="wav">WAV</option>
            <option value="flac">FLAC</option>
            <option value="thumbnail">Thumbnail</option>
          </select>
        </div>
      </div>
      <div class="row">
        <label for="folder">Folder</label>
        <input id="folder" type="text" placeholder="Folder" />
      </div>
      <div class="row">
        <label for="customNamePrefix">Custom Name Prefix</label>
        <input id="customNamePrefix" type="text" placeholder="Custom Name Prefix" />
      </div>
      <div class="row">
        <input type="checkbox" id="autoStart" />
        <label for="autoStart">Auto Start</label>
      </div>
      <div class="row">
        <input type="checkbox" id="strictPlaylistMode" />
        <label for="strictPlaylistMode">Strict Playlist Mode</label>
      </div>
      <div id="buttons-row">
        <button id="sendToMeTube" class="send-to-metube">
          <span id="loadingSpinner" class="spinner hidden"></span>
          Send to MeTube
        </button>
      </div>
      <!-- <div id="history"> -->
      <!--   <span class="spinner"></span> -->
      <!-- </div> -->
    </div>
    <div id="error-content" class="hidden error-msg">
      <p>Error occurred. Check logs for more information.</p>
    </div>
    <div id="success-content" class="hidden success-msg">
      <p>Successfully sent to MeTube</p>
    </div>
    <script src="../common/utils.js"></script>
    <script src="popup.js"></script>
  </body>
</html>
```

## File: `src/popup/popup.js`
```javascript
function showValidationError(message) {
  const urlValidationMessageEl = document.getElementById('urlValidationMessage');
  urlValidationMessageEl.innerText = message;
  urlValidationMessageEl.classList.remove('hidden');
}

function hideValidationError() {
  const urlValidationMessageEl = document.getElementById('urlValidationMessage');
  urlValidationMessageEl.classList.add('hidden');
}

document.getElementById("sendToMeTube").addEventListener("click", async function() {
  let url = document.getElementById('urlInput').value;

  if (!url || url.trim() === '') {
    showValidationError('Please enter a URL');
    return;
  }

  if (url.indexOf("://") === -1) {
    showValidationError('Invalid URL format');
    return;
  }

  hideValidationError();
  showLoadingState();

  let quality = document.getElementById('quality').value;
  let format = document.getElementById('format').value;
  let folder = document.getElementById('folder').value;
  let customNamePrefix = document.getElementById('customNamePrefix').value;
  let autoStart = document.getElementById('autoStart').checked;
  let strictPlaylistMode = document.getElementById('strictPlaylistMode').checked;
  await browser.runtime.sendMessage({ command: 'sendToMeTube', quality: quality, format: format, url: url, folder: folder, customNamePrefix: customNamePrefix, autoStart: autoStart, strictPlaylistMode: strictPlaylistMode });
});

function showError(errorMessage) {
  document.querySelector("#popup-content").classList.add("hidden");
  document.querySelector("#success-content").classList.add("hidden");
  document.querySelector("#error-content").classList.remove("hidden");
  document.querySelector("#error-content p").textContent = errorMessage;
  console.error(`Failed to execute MeTube script: ${errorMessage}`);
}

function showSuccess() {
  document.querySelector("#popup-content").classList.add("hidden");
  document.querySelector("#error-content").classList.add("hidden");
  document.querySelector("#success-content").classList.remove("hidden");
}

function showLoadingState() {
  document.getElementById('loadingSpinner').classList.remove('hidden');
}

function hideLoadingState() {
  document.getElementById('loadingSpinner').classList.add('hidden');
}

browser.runtime.onMessage.addListener(async (message) => {
  if (message.command === "showLoading") {
    showLoadingState();
    return;
  }

  hideLoadingState();

  if (message.command === "errorOccurred") {
    showError(message.errorMessage);
  } else if (message.command === "success") {
    showSuccess();
    setTimeout(function() {
      window.close();
    }, 1500);
  }
  else if (message.command === "history") {
    // TODO: display download history (maybe in some separate tab?)
    // let history = JSON.parse(message.data);
    // let historyContainer = document.getElementById('history');
    // historyContainer.innerHTML = '<ul></ul>';
    //
    // let ul = historyContainer.querySelector('ul');
    //
    // let doneItems = history.done;
    //
    // for (let i = 0; i < doneItems.length; i++) {
    //   let item = doneItems[i];
    //   let li = document.createElement('li');
    //   li.textContent = item.title;
    //   ul.appendChild(li);
    // }
    //
    // console.log(history);
  }
});

addEventListener('DOMContentLoaded', async (event) => {
  let url = await getCurrentUrl();
  if (url && url.indexOf("://") === -1) url = "";
  document.getElementById('urlInput').value = url || "";
  document.getElementById('format').value = await getDefaultFormat() || "any";
  document.getElementById('quality').value = await getDefaultQuality() || "best";
  document.getElementById('folder').value = await getDefaultFolder() || "";
  document.getElementById('customNamePrefix').value = await getDefaultCustomNamePrefix() || "";
  document.getElementById('autoStart').checked = await getDefaultAutoStart() ?? true;
  document.getElementById('strictPlaylistMode').checked = await getDefaultStrictPlaylistMode() ?? false;

  //await fetchHistory();
});

async function fetchHistory() {
  return await browser.runtime.sendMessage({ command: 'fetchHistory' });
}
```

