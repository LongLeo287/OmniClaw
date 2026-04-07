---
id: office
type: knowledge
owner: OA_Triage
---
# office
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "office-ui-fabric-core",
  "author": "Office UI Fabric Team",
  "version": "11.1.0",
  "description": "The front-end framework for building experiences for Office 365.",
  "license": "MIT",
  "scripts": {
    "test": "gulp",
    "start": "gulp watch",
    "build": "gulp"
  },
  "browserslist": [
    "last 1 version",
    "not dead"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/OfficeDev/Office-UI-Fabric-Core"
  },
  "private": false,
  "devDependencies": {
    "app-root-path": "^2.2.1",
    "colors": "^1.3.3",
    "csscomb": "^4.3.0",
    "del": "^1.2.1",
    "event-stream": "^4.0.1",
    "express": "^4.10.4",
    "fancy-log": "^1.3.3",
    "gulp": "^4.0.2",
    "gulp-autoprefixer": "^6.1.0",
    "gulp-changed": "^3.0.0",
    "gulp-clean-css": "^4.2.0",
    "gulp-connect": "^5.7.0",
    "gulp-cssbeautify": "^1.0.1",
    "gulp-data": "^1.2.0",
    "gulp-debug": "^3.0.0",
    "gulp-file-include": "^2.1.0",
    "gulp-header": "^2.0.9",
    "gulp-if": "^2.0.0",
    "gulp-nuget-pack": "^0.1.0",
    "gulp-plumber": "^1.0.1",
    "gulp-rename": "^1.2.2",
    "gulp-replace": "^0.5.4",
    "gulp-sass": "^4.0.2",
    "gulp-size": "^3.0.0",
    "gulp-template": "^5.0.0",
    "gulp-tslint": "^8.0.0",
    "gulp-typescript": "^5.0.1",
    "handlebars": ">=3.0.0",
    "jshint": "^2.10.2",
    "lintspaces": "^0.6.4",
    "log-symbols": "^3.0.0",
    "map-stream": "0.0.7",
    "merge-stream": "^1.0.0",
    "plugin-error": "^1.0.1",
    "require-dir": "^0.3.0",
    "tslint": "^5.0.0",
    "typescript": "^2.0.3",
    "walk-sync": "^0.3.0"
  }
}
```

### File: README.md
```md
# [Office UI Fabric Core](https://developer.microsoft.com/en-us/fabric)

##### The front-end framework for building experiences for Office and Office 365.

Fabric is a responsive, mobile-first collection of styles and tools designed to make it quick and simple for you to create web experiences using the Office Design Language.

**Latest version:** 11.0.1

## CONTENTS

* [What's included](#whats-included)
* [Get started](#get-started)
* [Learn more](#learn-more)
* [Contribute to Fabric](#contribute-to-fabric)
* [Licenses](#licenses)
* [Changelog](#changelog)

## What's included

This repository contains the core styles used across all aspects of Fabric including icons, type, fonts, colors, the grid, etc. This is a separate project from [Office UI Fabric React](https://github.com/OfficeDev/office-ui-fabric-react), which contains the React components.

## Get started

For a quick start, reference the latest release of Fabric from a CDN or add a copy to your project. See [get started](https://developer.microsoft.com/en-us/fabric#/get-started) on the [Office UI Fabric site](https://developer.microsoft.com/en-us/fabric) for full details on the most common ways to get started with the core along with a description of what's included.

If you'd like to get Fabric through a package manager such as Bower, npm, or NuGet, check out the [package manager docs](https://github.com/OfficeDev/office-ui-fabric-core/blob/master/ghdocs/PACKAGES.md).

Want to customize Fabric for your project? See [building Fabric](https://github.com/OfficeDev/Office-UI-Fabric/blob/master/ghdocs/BUILDING.md) to learn about the build process.

## Learn more

New to Fabric? Start with [the project's site](https://developer.microsoft.com/en-us/fabric) to understand its purpose and explore the full set of styles and components from [Office UI Fabric React](https://github.com/OfficeDev/office-ui-fabric-react).

When you're ready to create an Office Add-in with Fabric, take a look at the [Use Office UI Fabric with Office Add-ins on MSDN](https://msdn.microsoft.com/EN-US/library/office/mt450443.aspx) article.

## Contribute to Fabric

Bug reports, feature requests, and questions are posted on the [issue tracker](https://github.com/OfficeDev/Office-UI-Fabric-core/issues). For details on our contribution process and how we label issues, see our [contributing](https://github.com/OfficeDev/Office-UI-Fabric/blob/master/ghdocs/CONTRIBUTING.md) page.

## Licenses

All files in this GitHub repository are subject to the [MIT license](https://github.com/OfficeDev/office-ui-fabric-core/blob/master/LICENSE). This project also references fonts and icons from a CDN, which are subject to a separate [asset license](https://static2.sharepointonline.com/files/fabric/assets/license.txt).

## Changelog

We use [GitHub Releases](https://github.com/blog/1547-release-your-software) to manage our releases, including the changelog between every release. View a complete list of additions, fixes, and changes since 1.0 on the [releases](https://github.com/OfficeDev/Office-UI-Fabric/releases) page.

## Join the Microsoft 365 Developer Program

Join the [Microsoft 365 Developer Program](https://aka.ms/m365devprogram) to get resources and information to help you build solutions for the Microsoft 365 platform, including recommendations tailored to your areas of interest.

You might also qualify for a free developer subscription that's renewable for 90 days and comes configured with sample data; for details, see the [FAQ](https://learn.microsoft.com/office/developer-program/microsoft-365-developer-program-faq#who-qualifies-for-a-microsoft-365-e5-developer-subscription-).


---

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

```

### File: .csscomb.json
```json
{
    "remove-empty-rulesets": true,
    "always-semicolon": true,
    "color-case": "lower",
    "block-indent": "  ",
    "color-shorthand": false,
    "element-case": "lower",
    "eof-newline": true,
    "leading-zero": true,
    "quotes": "single",
    "space-before-colon": "",
    "space-after-colon": " ",
    "space-before-combinator": " ",
    "space-after-combinator": " ",
    "space-between-declarations": "\n",
    "space-before-opening-brace": " ",
    "space-after-opening-brace": "\n",
    "space-after-selector-delimiter": "\n",
    "space-before-selector-delimiter": "",
    "space-before-closing-brace": "\n",
    "strip-spaces": true,
    "tab-size": true,
    "unitless-zero": false,
    "vendor-prefix-align": true
}


```

### File: backup.html
```html

```

### File: bower.json
```json
{
  "name": "office-ui-fabric-core",
  "author": "Office UI Fabric Team",
  "version": "11.0.1",
  "description":
    "The front-end framework for building experiences for Office 365.",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/OfficeDev/Office-UI-Fabric-Core"
  },
  "main": "dist/css/fabric.css",
  "private": false,
  "ignore": [
    "node_modules",
    "bower_components",
    "*.sublime*",
    "typings",
    "ghdocs",
    "server",
    "gulp",
    ".travis.yml",
    ".sass-lint.yml",
    ".pullapprove.yml",
    ".htmllintrc",
    ".jshintrc",
    ".csscomb.json"
  ]
}

```

### File: gulpfile.js
```js
// Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license. See LICENSE in the project root for license information.
var gulp = require('gulp');
var Plugins = require('./gulp/modules/Plugins');
var Config = require('./gulp/modules/Config');
var ConsoleHelper = require('./gulp/modules/ConsoleHelper');
var Server = require('./gulp/modules/Server');
var Utilites = require('./gulp/modules/Utilities');
var ErrorHandling = require('./gulp/modules/ErrorHandling');

//////////////////////////
// BUILD TASKS
//////////////////////////

Plugins.requireDir('../../gulp');
var {buildMessagesFinished, buildMessagesServer, buildMessagesUpdated} = require('./gulp/BuildMessages');
var {documentationBuild,documentationNuke} = require('./gulp/Documentation');
var {fabricBuild, fabricNuke} = require('./gulp/FabricBuild');
var {setDebugMode} = require('./gulp/ConfigureEnvironment')
var {linting} = require('./gulp/Linting');
var {server} = require('./gulp/Server');

//////////////////////////
// MAIN BUILD
//////////////////////////
var build = gulp.parallel(documentationBuild, fabricBuild, linting);

//
// Local Server Configuration and Testing Website
// ----------------------------------------------------------------------------

Server.configServer(
   Config.port, // Port Number
   Config.projectURL, // URL To access the server
   Config.projectDirectory // Directory to serve up
);

// Config Paths
Server.serveSpecificPaths(Config.servePaths);

//
// Nuke Tasks
// ---------------------------------------------------------------------------
exports.nuke = gulp.parallel(fabricNuke, documentationNuke)

//
// Watch Tasks
// ----------------------------------------------------------------------------
function watchBuild(done) {
    gulp.watch(Config.paths.src + '/**/*', build);
    done();
};

exports.watch = gulp.series(build, server, watchBuild, buildMessagesServer);

//
// Debug Tasks
// ---------------------------------------------------------------------------
function watchDebugBuild(done) {
    gulp.watch(Config.paths.src + '/**/*', gulp.series(build, buildMessagesUpdated));
    done();
};

exports.watchDebug = gulp.series(setDebugMode, build, server, watchDebugBuild, buildMessagesServer);

//
// Check For errors
//
function checkAllErrors(done) {
    var returnFailedBuild = false;
     if (ErrorHandling.numberOfErrors() > 0) {
         ErrorHandling.generateError("------------------------------------------");
         ErrorHandling.generateBuildError("Errors in build, please fix and re build Fabric");
         ErrorHandling.showNumberOfErrors(ErrorHandling.numberOfErrors());
         ErrorHandling.generateError("------------------------------------------");
         ErrorHandling.generateBuildError("Exiting build");
         ErrorHandling.generateError("------------------------------------------");
         returnFailedBuild = true;
     }
          
     if (ErrorHandling.numberOfWarnings() > 0) {
         ErrorHandling.generateError("------------------------------------------");
         ErrorHandling.generateBuildError("Warnings in build, please fix and re build Fabric");
         ErrorHandling.showNumberOfWarnings(ErrorHandling.numberOfWarnings());
         ErrorHandling.generateError("------------------------------------------");
         ErrorHandling.generateBuildError("Exiting build");
         ErrorHandling.generateError("------------------------------------------");

         returnFailedBuild = true;
     }
     
     if (returnFailedBuild) {
        process.exit(1);
        done();
     } else {
        done();
     }
};


//
// Default Build
// ----------------------------------------------------------------------------
exports.default = gulp.series(build, checkAllErrors, buildMessagesFinished);

//
// Re-Build
// ----------------------------------------------------------------------------
exports.rebuild = gulp.series(build, buildMessagesFinished);

//
// Packaging tasks
// ----------------------------------------------------------------------------
exports.nugetPack = function(callback) {
    Plugins.nugetpack(Config.nugetConfig, Config.nugetPaths, callback);
};
```

### File: tslint.json
```json
{
  "rules": {
    "class-name": true,
    "comment-format": [true, "check-space"],
    "curly": true,
    "eofline": true,
    "forin": true,
    "indent": [true, "spaces"],
    "label-position": true,
    "label-undefined": true,
    "max-line-length": [true, 140],
    "member-access": true,
    "member-ordering": [true,
      "public-before-private",
      "static-before-instance",
      "variables-before-functions"
    ],
    "no-arg": true,
    "no-bitwise": true,
    "no-console": [true,
      "debug",
      "info",
      "time",
      "timeEnd",
      "trace"
    ],
    "no-construct": true,
    "no-debugger": true,
    "no-duplicate-key": true,
    "no-duplicate-variable": true,
    "no-empty": true,
    "no-eval": true,
    "no-inferrable-types": false,
    "no-shadowed-variable": true,
    "no-string-literal": true,
    "no-switch-case-fall-through": true,
    "no-trailing-whitespace": true,
    "no-unused-expression": true,
    "no-unused-variable": true,
    "no-unreachable": true,
    "no-use-before-declare": true,
    "no-var-keyword": true,
    "object-literal-sort-keys": false,
    "one-line": [true,
      "check-open-brace",
      "check-catch",
      "check-else",
      "check-finally",
      "check-whitespace"
    ],
    "quotemark": [true, "double", "avoid-escape"],
    "radix": true,
    "semicolon": true,
    "trailing-comma": [true, {
      "singleline": "never",
      "multiline": "never"
    }],
    "triple-equals": [true, "allow-null-check"],
    "typedef-whitespace": [true, {
      "call-signature": "nospace",
      "index-signature": "nospace",
      "parameter": "nospace",
      "property-declaration": "nospace",
      "variable-declaration": "nospace"
    }],
    "variable-name": false,
    "whitespace": [true,
      "check-branch",
      "check-decl",
      "check-operator",
      "check-separator",
      "check-type"
    ]
  }
}
```

### File: src\data\brand-icons.json
```json
[
  {
    "name": "access"
  },
  {
    "name": "excel"
  },
  {
    "name": "infopath"
  },
  {
    "name": "m365"
  },
  {
    "name": "office"
  },
  {
    "name": "onedrive"
  },
  {
    "name": "onenote"
  },
  {
    "name": "outlook"
  },
  {
    "name": "powerpoint"
  },
  {
    "name": "project"
  },
  {
    "name": "sharepoint"
  },
  {
    "name": "teams"
  },
  {
    "name": "visio"
  },
  {
    "name": "word"
  }
]

```

### File: src\data\colors.json
```json
[
  {
    "palette": "Neutral",
    "colors": [
      {
        "name": "Black",
        "hex": "#000000"
      },
      {
        "name": "Gray220",
        "hex": "#11100f"
      },
      {
        "name": "Gray210",
        "hex": "#161514"
      },
      {
        "name": "Gray200",
        "hex": "#1b1a19"
      },
      {
        "name": "Gray190",
        "hex": "#201f1e"
      },
      {
        "name": "Gray180",
        "hex": "#252423"
      },
      {
        "name": "Gray170",
        "hex": "#292827"
      },
      {
        "name": "Gray160",
        "hex": "#323130"
      },
      {
        "name": "Gray150",
        "hex": "#3b3a39"
      },
      {
        "name": "Gray140",
        "hex": "#484644"
      },
      {
        "name": "Gray130",
        "hex": "#605e5c"
      },
      {
        "name": "Gray120",
        "hex": "#797775"
      },
      {
        "name": "Gray110",
        "hex": "#8a8886"
      },
      {
        "name": "Gray100",
        "hex": "#979593"
      },
      {
        "name": "Gray90",
        "hex": "#a19f9d"
      },
      {
        "name": "Gray80",
        "hex": "#b3b0ad"
      },
      {
        "name": "Gray70",
        "hex": "#bebbb8"
      },
      {
        "name": "Gray60",
        "hex": "#c8c6c4"
      },
      {
        "name": "Gray50",
        "hex": "#d2d0ce"
      },
      {
        "name": "Gray40",
        "hex": "#e1dfdd"
      },
      {
        "name": "Gray30",
        "hex": "#edebe9"
      },
      {
        "name": "Gray20",
        "hex": "#f3f2f1"
      },
      {
        "name": "Gray10",
        "hex": "#faf9f8"
      },
      {
        "name": "White",
        "hex": "#ffffff"
      }
    ]
  },
  {
    "palette": "Communication",
    "colors": [
      {
        "name": "CommunicationShade30",
        "hex": "#004578"
      },
      {
        "name": "CommunicationShade20",
        "hex": "#005a9e"
      },
      {
        "name": "CommunicationShade10",
        "hex": "#106ebe"
      },
      {
        "name": "CommunicationPrimary",
        "hex": "#0078d4"
      },
      {
        "name": "communicationTint10",
        "hex": "#2b88d8"
      },
      {
        "name": "CommunicationTint20",
        "hex": "#c7e0f4"
      },
      {
        "name": "CommunicationTint30",
        "hex": "#deecf9"
      },
      {
        "name": "CommunicationTint40",
        "hex": "#eff6fc"
      }
    ]
  },
  {
    "palette": "Shared",
    "colors": [
      { "name": "SharedPinkRed10", "hex": "#750b1c" },
      { "name": "SharedRed20", "hex": "#a4262c" },
      { "name": "SharedRed10", "hex": "#d13438" },
      { "name": "SharedRedOrange20", "hex": "#603d30" },
      { "name": "SharedRedOrange10", "hex": "#da3b01" },
      { "name": "SharedOrange30", "hex": "#8e562e" },
      { "name": "SharedOrange20", "hex": "#ca5010" },
      { "name": "SharedOrange10", "hex": "#ffaa44" },
      { "name": "SharedYellow10", "hex": "#fce100" },
      { "name": "SharedOrangeYellow20", "hex": "#986f0b" },
      { "name": "SharedOrangeYellow10", "hex": "#c19c00" },
      { "name": "SharedYellowGreen10", "hex": "#8cbd18" },
      { "name": "SharedGreen20", "hex": "#0b6a0b" },
      { "name": "SharedGreen10", "hex": "#498205" },
      { "name": "SharedGreenCyan10", "hex": "#00ad56" },
      { "name": "SharedCyan40", "hex": "#005e50" },
      { "name": "SharedCyan30", "hex": "#005b70" },
      { "name": "SharedCyan20", "hex": "#038387" },
      { "name": "SharedCyan10", "hex": "#00b7c3" },
      { "name": "SharedCyanBlue20", "hex": "#004e8c" },
      { "name": "SharedCyanBlue10", "hex": "#0078d4" },
      { "name": "SharedBlue10", "hex": "#4f6bed" },
      { "name": "SharedBlueMagenta40", "hex": "#373277" },
      { "name": "SharedBlueMagenta30", "hex": "#5c2e91" },
      { "name": "SharedBlueMagenta20", "hex": "#8764b8" },
      { "name": "SharedBlueMagenta10", "hex": "#8378de" },
      { "name": "SharedMagenta20", "hex": "#881798" },
      { "name": "SharedMagenta10", "hex": "#c239b3" },
      { "name": "SharedMagentaPink20", "hex": "#9b0062" },
      { "name": "SharedMagentaPink10", "hex": "#e3008c" },
      { "name": "SharedGray40", "hex": "#393939" },
      { "name": "SharedGray30", "hex": "#7a7574" },
      { "name": "SharedGray20", "hex": "#69797e" },
      { "name": "SharedGray10", "hex": "#a0aeb2" }
    ]
  },
  {
    "palette": "Contrast",
    "colors": [
      {
        "name": "ContrastBlackDisabled",
        "hex": "#00ff00"
      },
      {
        "name": "ContrastWhiteDisabled",
        "hex": "#600000"
      },
      {
        "name": "ContrastBlackSelected",
        "hex": "#1aebff"
      },
      {
        "name": "ContrastWhiteSelected",
        "hex": "#37006e"
      }
    ]
  }
]

```

### File: src\data\depths.json
```json
[
  {
    "level": 0,
    "shadow": {
      "offsetX": 0,
      "offsetY": 0,
      "blurRadius": 0,
      "spreadRadius": 0,
      "color": "transparent",
      "opacity": 0
    },
    "border": {
      "color": "transparent",
      "width": "0px"
    }
  },
  {
    "level": 1,
    "shadow": {
      "offsetX": 0,
      "offsetY": 2,
      "blurRadius": 4,
      "spreadRadius": -0.75,
      "color": "#000000",
      "opacity": 0.1
    },
    "border": {
      "color": "#f3f2f1",
      "width": "1px"
    }
  },
  {
    "level": 2,
    "shadow": {
      "offsetX": 0,
      "offsetY": 4,
      "blurRadius": 8,
      "spreadRadius": -1,
      "color": "#000000",
      "opacity": 0.1
    },
    "border": {
      "color": "#f3f2f1",
      "width": "1px"
    }
  },
  {
    "level": 3,
    "shadow": {
      "offsetX": 0,
      "offsetY": 8,
      "blurRadius": 10,
      "spreadRadius": -2,
      "color": "#000000",
      "opacity": 0.1
    },
    "border": {
      "color": "#f3f2f1",
      "width": "1px"
    }
  },
  {
    "level": 4,
    "shadow": {
      "offsetX": 0,
      "offsetY": 16,
      "blurRadius": 18,
      "spreadRadius": -4,
      "color": "#000000",
      "opacity": 0.1
    },
    "border": {
      "color": "#f3f2f1",
      "width": "1px"
    }
  }
]

```

### File: src\data\file-type-icons.json
```json
[
  {
    "name": "accdb"
  },
  {
    "name": "archive"
  },
  {
    "name": "audio"
  },
  {
    "name": "code"
  },
  {
    "name": "csv"
  },
  {
    "name": "docset"
  },
  {
    "name": "docx"
  },
  {
    "name": "dotx"
  },
  {
    "name": "email"
  },
  {
    "name": "exe"
  },
  {
    "name": "folder"
  },
  {
    "name": "font"
  },
  {
    "name": "genericfile"
  },
  {
    "name": "html"
  },
  {
    "name": "link"
  },
  {
    "name": "listitem"
  },
  {
    "name": "model"
  },
  {
    "name": "mpp"
  },
  {
    "name": "mpt"
  },
  {
    "name": "one"
  },
  {
    "name": "onepkg"
  },
  {
    "name": "onetoc"
  },
  {
    "name": "pdf"
  },
  {
    "name": "photo"
  },
  {
    "name": "potx"
  },
  {
    "name": "ppsx"
  },
  {
    "name": "pptx"
  },
  {
    "name": "pub"
  },
  {
    "name": "rtf"
  },
  {
    "name": "sharedfolder"
  },
  {
    "name": "spo"
  },
  {
    "name": "sysfile"
  },
  {
    "name": "txt"
  },
  {
    "name": "vector"
  },
  {
    "name": "video"
  },
  {
    "name": "vsdx"
  },
  {
    "name": "vssx"
  },
  {
    "name": "vstx"
  },
  {
    "name": "xlsx"
  },
  {
    "name": "xls"
  },
  {
    "name": "xltx"
  },
  {
    "name": "xml"
  },
  {
    "name": "xsn"
  },
  {
    "name": "zip"
  }
]

```

### File: src\data\icons.json
```json
[
  { "name": "12PointStar", "unicode": "F505" },
  { "name": "6PointStar", "unicode": "F504" },
  { "name": "AADLogo", "unicode": "ED68" },
  { "name": "Accept", "unicode": "E8FB" },
  { "name": "AccessibiltyChecker", "unicode": "F835" },
  { "name": "AccessLogo", "unicode": "ED69" },
  { "name": "AccessLogoFill", "unicode": "F1DB" },
  { "name": "AccountActivity", "unicode": "EFF4" },
  { "name": "AccountBrowser", "unicode": "F652" },
  { "name": "AccountManagement", "unicode": "F55C" },
  { "name": "Accounts", "unicode": "E910" },
  { "name": "ActionCenter", "unicode": "E91C" },
  { "name": "ActivateOrders", "unicode": "EFE0" },
  { "name": "ActivityFeed", "unicode": "F056" },
  { "name": "Add", "unicode": "E710" },
  { "name": "AddBookmark", "unicode": "F5B7" },
  { "name": "AddEvent", "unicode": "EEB5" },
  { "name": "AddFavorite", "unicode": "F0C8" },
  { "name": "AddFavoriteFill", "unicode": "F0C9" },
  { "name": "AddFriend", "unicode": "E8FA" },
  { "name": "AddGroup", "unicode": "EE3D" },
  { "name": "AddHome", "unicode": "F17B" },
  { "name": "AddIn", "unicode": "F775" },
  { "name": "AddLink", "unicode": "E35E" },
  { "name": "AddNotes", "unicode": "EAE3" },
  { "name": "AddOnlineMeeting", "unicode": "ED8E" },
  { "name": "AddPhone", "unicode": "ED96" },
  { "name": "AddReaction", "unicode": "F85D" },
  { "name": "AddSpaceAfter", "unicode": "E3DF" },
  { "name": "AddSpaceBefore", "unicode": "E3DE" },
  { "name": "AddTo", "unicode": "ECC8" },
  { "name": "AddToShoppingList", "unicode": "EA9A" },
  { "name": "AddWork", "unicode": "F17C" },
  { "name": "Admin", "unicode": "E7EF" },
  { "name": "AdminALogo32", "unicode": "F4BA" },
  { "name": "AdminALogoFill32", "unicode": "F4BB" },
  { "name": "AdminALogoInverse32", "unicode": "ED6A" },
  { "name": "AdminCLogoInverse32", "unicode": "ED6B" },
  { "name": "AdminDLogoInverse32", "unicode": "ED6C" },
  { "name": "AdminELogoInverse32", "unicode": "ED6D" },
  { "name": "AdminLLogoInverse32", "unicode": "ED6E" },
  { "name": "AdminMLogoInverse32", "unicode": "ED6F" },
  { "name": "AdminOLogoInverse32", "unicode": "ED70" },
  { "name": "AdminPLogoInverse32", "unicode": "ED71" },
  { "name": "AdminSLogoInverse32", "unicode": "ED72" },
  { "name": "AdminYLogoInverse32", "unicode": "ED73" },
  { "name": "Airplane", "unicode": "E709" },
  { "name": "AirplaneSolid", "unicode": "EB4C" },
  { "name": "AirTickets", "unicode": "EF7A" },
  { "name": "AlarmClock", "unicode": "E919" },
  { "name": "Album", "unicode": "E7AB" },
  { "name": "AlbumRemove", "unicode": "EC62" },
  { "name": "AlertSettings", "unicode": "F8B6" },
  { "name": "AlertSolid", "unicode": "F331" },
  { "name": "AlignCenter", "unicode": "E8E3" },
  { "name": "AlignHorizontalCenter", "unicode": "F4F4" },
  { "name": "AlignHorizontalLeft", "unicode": "F4F3" },
  { "name": "AlignHorizontalRight", "unicode": "F4F5" },
  { "name": "AlignJustify", "unicode": "F51E" },
  { "name": "AlignLeft", "unicode": "E8E4" },
  { "name": "AlignRight", "unicode": "E8E2" },
  { "name": "AlignVerticalBottom", "unicode": "F4F8" },
  { "name": "AlignVerticalCenter", "unicode": "F4F7" },
  { "name": "AlignVerticalTop", "unicode": "F4F6" },
  { "name": "AllApps", "unicode": "E71D" },
  { "name": "AllAppsMirrored", "unicode": "EA40" },
  { "name": "AllCurrency", "unicode": "EAE4" },
  { "name": "AltText", "unicode": "E397" },
  { "name": "AnalyticsLogo", "unicode": "F1DE" },
  { "name": "AnalyticsQuery", "unicode": "F1DF" },
  { "name": "AnalyticsReport", "unicode": "F1E1" },
  { "name": "AnalyticsView", "unicode": "F5F1" },
  { "name": "AnchorLock", "unicode": "F511" },
  { "name": "Annotation", "unicode": "E924" },
  { "name": "AppIconDefault", "unicode": "ECAA" },
  { "name": "AppIconDefaultAdd", "unicode": "EFDA" },
  { "name": "AppIconDefaultList", "unicode": "EFDE" },
  { "name": "Archive", "unicode": "F03F" },
  { "name": "ArchiveUndo", "unicode": "E3A1" },
  { "name": "AreaChart", "unicode": "E9D2" },
  { "name": "ArrangeBringForward", "unicode": "F509" },
  { "name": "ArrangeBringToFront", "unicode": "F506" },
  { "name": "ArrangeByFrom", "unicode": "F678" },
  { "name": "ArrangeSendBackward", "unicode": "F508" },
  { "name": "ArrangeSendToBack", "unicode": "F507" },
  { "name": "Arrivals", "unicode": "EB34" },
  { "name": "ArrowDownRight8", "unicode": "EED5" },
  { "name": "ArrowDownRightMirrored8", "unicode": "EEF0" },
  { "name": "ArrowTallDownLeft", "unicode": "F2BF" },
  { "name": "ArrowTallDownRight", "unicode": "F2C0" },
  { "name": "ArrowTallUpLeft", "unicode": "F2BD" },
  { "name": "ArrowTallUpRight", "unicode": "F2BE" },
  { "name": "ArrowUpRight", "unicode": "F069" },
  { "name": "ArrowUpRight8", "unicode": "EED4" },
  { "name": "ArrowUpRightMirrored8", "unicode": "EEEF" },
  { "name": "Articles", "unicode": "EAC1" },
  { "name": "Ascending", "unicode": "EDC0" },
  { "name": "AspectRatio", "unicode": "E799" },
  { "name": "AssessmentGroup", "unicode": "F31A" },
  { "name": "AssessmentGroupTemplate", "unicode": "F2B1" },
  { "name": "AssetLibrary", "unicode": "EEB6" },
  { "name": "Assign", "unicode": "E9D3" },
  { "name": "Asterisk", "unicode": "EA38" },
  { "name": "AsteriskSolid", "unicode": "F34D" },
  { "name": "ATPLogo", "unicode": "EF85" },
  { "name": "Attach", "unicode": "E723" },
  { "name": "AustralianRules", "unicode": "EE70" },
  { "name": "AuthenticatorApp", "unicode": "F6B1" },
  { "name": "AutoDeploySettings", "unicode": "F3FA" },
  { "name": "AutoEnhanceOff", "unicode": "E78E" },
  { "name": "AutoEnhanceOn", "unicode": "E78D" },
  { "name": "AutoFillTemplate", "unicode": "F313" },
  { "name": "AutoFitContents", "unicode": "E3E8" },
  { "name": "AutoFitWindow", "unicode": "E3E9" },
  { "name": "AutoHeight", "unicode": "F512" },
  { "name": "AutomateFlow", "unicode": "E3F5" },
  { "name": "AutoRacing", "unicode": "EB24" },
  { "name": "AwayStatus", "unicode": "EE6A" },
  { "name": "AzureAPIManagement", "unicode": "F37F" },
  { "name": "AzureKeyVault", "unicode": "F3B4" },
  { "name": "AzureLogo", "unicode": "EB6A" },
  { "name": "AzureServiceEndpoint", "unicode": "F380" },
  { "name": "Back", "unicode": "E72B" },
  { "name": "BackgroundColor", "unicode": "F42B" },
  { "name": "Backlog", "unicode": "F2AC" },
  { "name": "BacklogBoard", "unicode": "F444" },
  { "name": "BacklogList", "unicode": "F6BF" },
  { "name": "BackToWindow", "unicode": "E73F" },
  { "name": "Badge", "unicode": "EC1B" },
  { "name": "Balloons", "unicode": "ED7E" },
  { "name": "Bank", "unicode": "E825" },
  { "name": "BankSolid", "unicode": "F34F" },
  { "name": "BarChart4", "unicode": "EAE7" },
  { "name": "BarChartHorizontal", "unicode": "E9EB" },
  { "name": "BarChartVertical", "unicode": "E9EC" },
  { "name": "BarChartVerticalEdit", "unicode": "F89D" },
  { "name": "BarChartVerticalFill", "unicode": "F830" },
  { "name": "BarChartVerticalFilter", "unicode": "F77E" },
  { "name": "BarChartVerticalFilterSolid", "unicode": "F77F" },
  { "name": "Baseball", "unicode": "EB20" },
  { "name": "BeerMug", "unicode": "F49E" },
  { "name": "BIDashboard", "unicode": "F543" },
  { "name": "BidiLtr", "unicode": "E9AA" },
  { "name": "BidiRtl", "unicode": "E9AB" },
  { "name": "BingLogo", "unicode": "EB6B" },
  { "name": "BirthdayCake", "unicode": "EF8D" },
  { "name": "BlockContact", "unicode": "E8F8" },
  { "name": "Blocked", "unicode": "E733" },
  { "name": "Blocked12", "unicode": "F62E" },
  { "name": "Blocked2", "unicode": "ECE4" },
  { "name": "Blocked2Solid", "unicode": "F737" },
  { "name": "BlockedSite", "unicode": "E72F" },
  { "name": "BlockedSiteSolid12", "unicode": "F70A" },
  { "name": "BlockedSolid", "unicode": "F531" },
  { "name": "Blog", "unicode": "F22B" },
  { "name": "BlowingSnow", "unicode": "E9C9" },
  { "name": "Blur", "unicode": "F28E" },
  { "name": "Boards", "unicode": "EF68" },
  { "name": "Bold", "unicode": "E8DD" },
  { "name": "BookAnswers", "unicode": "F8A4" },
  { "name": "BookingsLogo", "unicode": "EDC7" },
  { "name": "BookmarkReport", "unicode": "F76B" },
  { "name": "Bookmarks", "unicode": "E8A4" },
  { "name": "BookmarksMirrored", "unicode": "EA41" },
  { "name": "BorderDash", "unicode": "F50A" },
  { "name": "BorderDot", "unicode": "F50B" },
  { "name": "BoxAdditionSolid", "unicode": "F2D4" },
  { "name": "BoxCheckmarkSolid", "unicode": "F2D7" },
  { "name": "BoxMultiplySolid", "unicode": "F2D5" },
  { "name": "BoxPlaySolid", "unicode": "F2D6" },
  { "name": "BoxSubtractSolid", "unicode": "F2D3" },
  { "name": "BranchCommit", "unicode": "F293" },
  { "name": "BranchCompare", "unicode": "F294" },
  { "name": "BranchFork", "unicode": "F173" },
  { "name": "BranchFork2", "unicode": "F291" },
  { "name": "BranchLocked", "unicode": "F292" },
  { "name": "BranchMerge", "unicode": "F295" },
  { "name": "BranchPullRequest", "unicode": "F296" },
  { "name": "BranchSearch", "unicode": "F297" },
  { "name": "BranchShelveset", "unicode": "F298" },
  { "name": "Breadcrumb", "unicode": "EF8C" },
  { "name": "Breakfast", "unicode": "F49C" },
  { "name": "Brightness", "unicode": "E706" },
  { "name": "Broom", "unicode": "EA99" },
  { "name": "BrowserScreenShot", "unicode": "EBED" },
  { "name": "BrowserTab", "unicode": "F5D7" },
  { "name": "BrowserTabScreenshot", "unicode": "F5D8" },
  { "name": "Brunch", "unicode": "F49D" },
  { "name": "Brush", "unicode": "ECFF" },
  { "name": "BucketColor", "unicode": "F1B6" },
  { "name": "BucketColorFill", "unicode": "F1B7" },
  { "name": "BufferTimeAfter", "unicode": "F0D0" },
  { "name": "BufferTimeBefore", "unicode": "F0CF" },
  { "name": "BufferTimeBoth", "unicode": "F0D1" },
  { "name": "Bug", "unicode": "EBE8" },
  { "name": "BugBlock", "unicode": "E400" },
  { "name": "BugSolid", "unicode": "F335" },
  { "name": "BugSync", "unicode": "E3FF" },
  { "name": "Build", "unicode": "F28F" },
  { "name": "BuildDefinition", "unicode": "F6E9" },
  { "name": "BuildIssue", "unicode": "F319" },
  { "name": "BuildQueue", "unicode": "F24F" },
  { "name": "BuildQueueNew", "unicode": "F250" },
  { "name": "BulkUpload", "unicode": "F548" },
  { "name": "BulletedList", "unicode": "E8FD" },
  { "name": "BulletedList2", "unicode": "F2C7" },
  { "name": "BulletedList2Mirrored", "unicode": "F2C8" },
  { "name": "BulletedListBullet", "unicode": "F793" },
  { "name": "BulletedListBulletMirrored", "unicode": "F795" },
  { "name": "BulletedListMirrored", "unicode": "EA42" },
  { "name": "BulletedListText", "unicode": "F792" },
  { "name": "BulletedListTextMirrored", "unicode": "F794" },
  { "name": "BulletedTreeList", "unicode": "F84C" },
  { "name": "Bullseye", "unicode": "F272" },
  { "name": "BullseyeTarget", "unicode": "F5F0" },
  { "name": "BullseyeTargetEdit", "unicode": "E319" },
  { "name": "Bus", "unicode": "E806" },
  { "name": "BusinessCenterLogo", "unicode": "F4B2" },
  { "name": "BusinessHoursSign", "unicode": "F310" },
  { "name": "BusSolid", "unicode": "EB47" },
  { "name": "ButtonControl", "unicode": "F6C0" },
  { "name": "Cafe", "unicode": "EC32" },
  { "name": "Cake", "unicode": "ECA4" },
  { "name": "Calculator", "unicode": "E8EF" },
  { "name": "CalculatorAddition", "unicode": "E948" },
  { "name": "CalculatorDelta", "unicode": "E406" },
  { "name": "CalculatorEqualTo", "unicode": "E94E" },
  { "name": "CalculatorMultiply", "unicode": "E947" },
  { "name": "CalculatorNotEqualTo", "unicode": "F2D2" },
  { "name": "CalculatorPercentage", "unicode": "E94C" },
  { "name": "CalculatorSubtract", "unicode": "E949" },
  { "name": "Calendar", "unicode": "E787" },
  { "name": "CalendarAgenda", "unicode": "EE9A" },
  { "name": "CalendarDay", "unicode": "E8BF" },
  { "name": "CalendarMirrored", "unicode": "ED28" },
  { "name": "CalendarReply", "unicode": "E8F5" },
  { "name": "CalendarSettings", "unicode": "F558" },
  { "name": "CalendarSettingsMirrored", "unicode": "F559" },
  { "name": "CalendarWeek", "unicode": "E8C0" },
  { "name": "CalendarWorkWeek", "unicode": "EF51" },
  { "name": "CalendarYear", "unicode": "E371" },
  { "name": "Calories", "unicode": "ECAD" },
  { "name": "CaloriesAdd", "unicode": "F172" },
  { "name": "Camera", "unicode": "E722" },
  { "name": "CampaignTemplate", "unicode": "F811" },
  { "name": "Cancel", "unicode": "E711" },
  { "name": "CannedChat", "unicode": "F0F2" },
  { "name": "Car", "unicode": "E804" },
  { "name": "CaretBottomLeftCenter8", "unicode": "F365" },
  { "name": "CaretBottomLeftSolid8", "unicode": "F121" },
  { "name": "CaretBottomRightCenter8", "unicode": "F364" },
  { "name": "CaretBottomRightSolid8", "unicode": "F122" },
  { "name": "CaretDown8", "unicode": "EDD8" },
  { "name": "CaretDownSolid8", "unicode": "EDDC" },
  { "name": "CaretHollow", "unicode": "E817" },
  { "name": "CaretHollowMirrored", "unicode": "EA45" },
  { "name": "CaretLeft8", "unicode": "EDD5" },
  { "name": "CaretLeftSolid8", "unicode": "EDD9" },
  { "name": "CaretRight", "unicode": "F06B" },
  { "name": "CaretRight8", "unicode": "EDD6" },
  { "name": "CaretRightSolid8", "unicode": "EDDA" },
  { "name": "CaretSolid", "unicode": "E818" },
  { "name": "CaretSolid16", "unicode": "EE62" },
  { "name": "CaretSolidDown", "unicode": "F08E" },
  { "name": "CaretSolidLeft", "unicode": "F08D" },
  { "name": "CaretSolidMirrored", "unicode": "EA46" },
  { "name": "CaretSolidRight", "unicode": "F08F" },
  { "name": "CaretSolidUp", "unicode": "F090" },
  { "name": "CaretTopLeftCenter8", "unicode": "F367" },
  { "name": "CaretTopLeftSolid8", "unicode": "EF54" },
  { "name": "CaretTopRightCenter8", "unicode": "F366" },
  { "name": "CaretTopRightSolid8", "unicode": "EF55" },
  { "name": "CaretUp8", "unicode": "EDD7" },
  { "name": "CaretUpSolid8", "unicode": "EDDB" },
  { "name": "Cat", "unicode": "ED7F" },
  { "name": "CellPhone", "unicode": "E8EA" },
  { "name": "Certificate", "unicode": "EB95" },
  { "name": "CertifiedDatabase", "unicode": "F5BB" },
  { "name": "ChangeEntitlements", "unicode": "E310" },
  { "name": "Chart", "unicode": "E999" },
  { "name": "ChartSeries", "unicode": "F513" },
  { "name": "ChartTemplate", "unicode": "F812" },
  { "name": "ChartXAngle", "unicode": "F514" },
  { "name": "ChartYAngle", "unicode": "F515" },
  { "name": "Chat", "unicode": "E901" },
  { "name": "ChatBot", "unicode": "F08B" },
  { "name": "ChatInviteFriend", "unicode": "ECFE" },
  { "name": "ChatSolid", "unicode": "F344" },
  { "name": "Checkbox", "unicode": "E739" },
  { "name": "CheckboxComposite", "unicode": "E73A" },
  { "name": "CheckboxCompositeReversed", "unicode": "E73D" },
  { "name": "CheckboxFill", "unicode": "E73B" },
  { "name": "CheckboxIndeterminate", "unicode": "E73C" },
  { "name": "CheckedOutByOther12", "unicode": "F630" },
  { "name": "CheckedOutByYou12", "unicode": "F631" },
  { "name": "CheckList", "unicode": "E9D5" },
  { "name": "CheckListCheck", "unicode": "F7A9" },
  { "name": "CheckListCheckMirrored", "unicode": "F7AB" },
  { "name": "CheckListText", "unicode": "F7A8" },
  { "name": "CheckListTextMirrored", "unicode": "F7AA" },
  { "name": "CheckMark", "unicode": "E
... [TRUNCATED]
```

### File: src\data\type-sizes.json
```json
[
  {
    "size": 68
  },
  {
    "size": 42
  },
  {
    "size": 32
  },
  {
    "size": 28
  },
  {
    "size": 24
  },
  {
    "size": 20
  },
  {
    "size": 18
  },
  {
    "size": 16
  },
  {
    "size": 14
  },
  {
    "size": 12
  },
  {
    "size": 10
  }
]

```

### File: src\data\type-weights.json
```json
[
  {
    "name": "Regular",
    "weight": 400
  },
  {
    "name": "Semibold",
    "weight": 600
  },
  {
    "name": "Bold",
    "weight": 700
  }
]

```

### File: src\documentation\templates\documentation-template.html
```html
@@include('./modules/components/DocumentationPageHeader.html')
	<h1>Get Started</h1>
    <h2 id="quick-start">Quick start</h2>
    <p>The simplest way to get started is to add a copy of Fabric to your project.</p>
    <ol>
        <li>Download the source code zip file from the <a href="https://github.com/OfficeDev/Office-UI-Fabric/releases/latest">latest release on GitHub</a>.</li>
        <li>Unzip the file and copy the Fabric folder into your project.</li>
        <li>Add a reference to <code>fabric.css</code> in the <code>&lt;head&gt;</code> of your page. Make sure the path is correct.</li>
        <li>If you're using <a href="http://dev.office.com/fabric/components">components</a>, add a reference to <code>fabric.components.css</code> after the <code>fabric.css</code> reference.</li>
    </ol>

    <h3>Using Fabric icons and fonts</h3>
    <p>Now that your project references Fabric, you can apply <a href="/Typography">type styles</a> to any text element.</p>
    <pre><code class="hljs">&#x3C;span class=&#x22;ms-font-su ms-fontColor-themePrimary&#x22;&#x3E;Big blue text&#x3C;/span&#x3E;</code></pre>
    <p>To use icons, add an <code>&#x3C;i&#x3E;</code> element with the appropriate <a href="/Icons">icon classes</a>.</p>
    <pre><code class="hljs">&#x3C;i class=&#x22;ms-Icon ms-Icon--mail&#x22; aria-hidden=&#x22;true&#x22;&#x3E;&#x3C;/i&#x3E;</code></pre>
    <p>By default, icons inherit the text size and color of their parent. To override this, apply <a href="/Typography">type styles</a> directly to the icon.</p>
    <p aria-hidden="true">
         @@include('./modules/content/DownloadSVG.html')
    </p>

    <h3>Using components</h3>
    <p>To use Fabric components:</p>
    <ol>
        <li>Add <a href="http://dev.office.com/fabric/components">markup</a> to your pages using the appropriate classes.</li>
        <li>If the component requires JavaScript, you can use the sample JavaScript included in the <a href="https://github.com/OfficeDev/Office-UI-Fabric/releases/latest">latest release</a> on GitHub.</li>
        <li>Initialize the component JavaScript, and you’re all set! For an example that shows how to initialize the JavaScript, see the <a href="http://dev.office.com/fabric/components">components page</a>.</li>
    </ol>
    <p aria-hidden="true">
       @@include('./modules/content/ExampleUsageSVG.html')
    </p>
    <h2>Other ways to get Fabric</h2>
    <p>In addition to downloading a copy for your project, you can include Fabric via a CDN reference, by adding it through a package manager, or by building your own copy from the source code.</p>
    
    <h3 id="cdn">Reference the CDN</h3>
    <p>If you prefer to have your project's assets stored on an external server, Fabric is available from the apps for Office CDN. To use it, include the following references in the <code>&#x3C;head&#x3E;</code> of your page.</p>
    <pre><code class="hljs">&#x3C;link rel=&#x22;stylesheet&#x22; href=&#x22;https://appsforoffice.microsoft.com/fabric/2.2.0/fabric.min.css&#x22;&#x3E;
&#x3C;link rel=&#x22;stylesheet&#x22; href=&#x22;https://appsforoffice.microsoft.com/fabric/2.2.0/fabric.components.min.css&#x22;&#x3E;
</code></pre>
    <p>New versions of Fabric might not be available on the CDN right away. The following table lists the releases that are available now. To reference a specific version, update the version number in the URL to match the one you want.</p>
    <table class="docs-Table docs-Table--striped" style="width: 100%;">
        <tr>
            <th style="width: 80%;">Fabric Release</th>
            <th style="width: 20%;">Available on CDN</th>
        </tr>

        {{#each AvailableOnCDNModel.items}}
            {{> CDNRow this }}
        {{/each}}
    </table>

    <h3 id="package-managers">Package managers</h3>
    <p>Fabric is also available from a variety of package managers, including <a href="http://bower.io/">Bower</a>, <a href="https://www.npmjs.com/">npm</a>, and the <a href="https://www.nuget.org/">NuGet Package Manager</a>. You can quickly add Fabric as a package and stay up to date with the latest version.</p>

    <h4>Install with Bower</h4>
    <p>To install Fabric using Bower, run the following command:</p>
    <pre><code class="hljs">$ bower install office-ui-fabric</code></pre>

    <h4>Install with npm</h4>
    <p>To install Fabric using npm, run the following command:</p>
    <pre><code class="hljs">$ npm install office-ui-fabric</code></pre>

    <h4>Install with NuGet Package Manager</h4>
    <p>To install Fabric's NuGet package, run the following command in the <a href="http://docs.nuget.org/consume/package-manager-console">package manager console</a>:</p>
    <pre><code class="hljs">PM> Install-Package OfficeUIFabric</code></pre>
    
    <h3 id="build">Build from source</h3>
    <p>Fabric is easy to build and customize locally using gulp and a handful of tasks to watch and build specific parts of the toolkit. You can also use gulp to build and tweak demos and samples.</p>

    <p>For more information about how to build Fabric locally, including gulp tasks, check out <a href="https://github.com/OfficeDev/Office-UI-Fabric/blob/master/ghdocs/BUILDING.md">our instructions on GitHub</a>.</p>
@@include('./modules/components/DocumentationPageFooter.html')
```

### File: src\documentation\pages\Icons\index.html
```html
@@include('../../templates/modules/components/DocumentationPageHeader.html')
<div class="docs-Styles-section" id="icons">
  <h2>Icons</h2>
  <p>Fabric uses a custom font for its iconography. This font contains glyphs that you can scale, color, and style in any way. You can even flip them for right-to-left localization. To use the icons, combine the base ms-Icon class with a modifier class for the specific icon.</p>
  <pre><code class="hljs">&#x3C;i class=&#x22;ms-Icon ms-Icon--Mail&#x22; aria-hidden=&#x22;true&#x22;&#x3E;&#x3C;/i&#x3E;</code></pre>
  <p>Note the <code>aria-hidden</code> attribute, which prevents screen readers from reading the icon. In cases where meaning is conveyed only through the icon, such as an icon-only navigation bar, be sure to apply an aria-label to the button for accessibility.</p>
  <div class="docs-IconList clearfix">
    <ul>
      {{#each icons}}
        {{> IconPageItem this }}
      {{/each}}
    </ul>
  </div>
</div>
@@include('../../templates/modules/components/DocumentationPageFooter.html')

```

### File: src\documentation\templates\models\AccentColorsModel.json
```json
{
  "items": [
    {
      "name": "Yellow",
      "hex": "#FFB900",
      "fontClass": "ms-fontColor-yellow",
      "customNameColor": "ms-fontColor-black",
      "bgClass": "ms-bgColor-yellow",
      "borderClass": "ms-borderColor-yellow"
    },
    {
      "name": "Light Yellow",
      "hex": "#FFF100",
      "customNameColor": "ms-fontColor-black",
      "fontClass": "ms-fontColor-yellowLight",
      "bgClass": "ms-bgColor-yellowLight",
      "borderClass": "ms-borderColor-yellowLight"
    },
    {
      "name": "Orange",
      "hex": "#D83B01",
      "fontClass": "ms-fontColor-orange",
      "bgClass": "ms-bgColor-orange",
      "borderClass": "ms-borderColor-orange",
      "customNameColor": "ms-fontColor-black"
    },
    {
      "name": "Orange Light",
      "hex": "#EA4300",
      "fontClass": "ms-fontColor-orangeLight",
      "bgClass": "ms-bgColor-orangeLight",
      "borderClass": "ms-borderColor-orangeLight",
      "customNameColor": "ms-fontColor-black"
    },
    {
      "name": "Orange Lighter",
      "hex": "#FF8C00",
      "customNameColor": "ms-fontColor-black",
      "fontClass": "ms-fontColor-orangeLighter",
      "bgClass": "ms-bgColor-orangeLighter",
      "borderClass": "ms-borderColor-orangeLighter"
    },
    {
      "name": "Dark Red",
      "hex": "#A80000",
      "fontClass": "ms-fontColor-redDark",
      "bgClass": "ms-bgColor-redDark",
      "borderClass": "ms-borderColor-redDark"
    },
    {
      "name": "Red",
      "hex": "#E81123",
      "fontClass": "ms-fontColor-red",
      "bgClass": "ms-bgColor-red",
      "borderClass": "ms-borderColor-red"
    },
    {
      "name": "Magenta Light",
      "hex": "#E3008C",
      "fontClass": "ms-fontColor-magentaLight",
      "bgClass": "ms-bgColor-magentaLight",
      "borderClass": "ms-borderColor-magentaLight"
    },
    {
      "name": "Magenta",
      "hex": "#B4009E",
      "fontClass": "ms-fontColor-magenta",
      "bgClass": "ms-bgColor-magenta",
      "borderClass": "ms-borderColor-magenta"
    },
    {
      "name": "Dark Magenta",
      "hex": "#5C005C",
      "fontClass": "ms-fontColor-magentaDark",
      "bgClass": "ms-bgColor-magentaDark",
      "borderClass": "ms-borderColor-magentaDark"
    },
    {
      "name": "Light Purple",
      "hex": "#B4A0FF",
      "fontClass": "ms-fontColor-purpleLight",
      "bgClass": "ms-bgColor-purpleLight",
      "borderClass": "ms-borderColor-purpleLight",
      "customNameColor": "ms-fontColor-black"
    },
    {
      "name": "Purple",
      "hex": "#5C2D91",
      "fontClass": "ms-fontColor-purple",
      "bgClass": "ms-bgColor-purple",
      "borderClass": "ms-borderColor-purple"
    },
    {
      "name": "Dark Purple",
      "hex": "#32145A",
      "fontClass": "ms-fontColor-purpleDark",
      "bgClass": "ms-bgColor-purpleDark",
      "borderClass": "ms-borderColor-purpleDark"
    },
    {
      "name": "Light Blue",
      "hex": "#00BCF2",
      "fontClass": "ms-fontColor-blueLight",
      "bgClass": "ms-bgColor-blueLight",
      "borderClass": "ms-borderColor-blueLight",
      "customNameColor": "ms-fontColor-black"
    },
    {
      "name": "Mid Blue",
      "hex": "#00188F",
      "fontClass": "ms-fontColor-blueMid",
      "bgClass": "ms-bgColor-blueMid",
      "borderClass": "ms-borderColor-blueMid"
    },
    {
      "name": "Blue",
      "hex": "#0078d7",
      "fontClass": "ms-fontColor-blue",
      "bgClass": "ms-bgColor-blue",
      "borderClass": "ms-borderColor-blue"
    },
    {
      "name": "Dark Blue",
      "hex": "#002050",
      "fontClass": "ms-fontColor-blueDark",
      "bgClass": "ms-bgColor-blueDark",
      "borderClass": "ms-borderColor-blueDark"
    },
    {
      "name": "Light Teal",
      "hex": "#00B294",
      "fontClass": "ms-fontColor-tealLight",
      "bgClass": "ms-bgColor-tealLight",
      "borderClass": "ms-borderColor-tealLight",
      "customNameColor": "ms-fontColor-black"
    },
    {
      "name": "Teal",
      "hex": "#008272",
      "fontClass": "ms-fontColor-teal",
      "bgClass": "ms-bgColor-teal",
      "borderClass": "ms-borderColor-teal"
    },
    {
      "name": "Dark Teal",
      "hex": "#004B50",
      "fontClass": "ms-fontColor-tealDark",
      "bgClass": "ms-bgColor-tealDark",
      "borderClass": "ms-borderColor-tealDark"
    },
    {
      "name": "Light Green",
      "hex": "#BAD80A",
      "fontClass": "ms-fontColor-greenLight",
      "bgClass": "ms-bgColor-greenLight",
      "borderClass": "ms-borderColor-greenLight",
      "customNameColor": "ms-fontColor-black"
    },
    {
      "name": "Green",
      "hex": "#107C10",
      "fontClass": "ms-fontColor-green",
      "bgClass": "ms-bgColor-green",
      "borderClass": "ms-borderColor-green"
    },
    {
      "name": "Dark Green",
      "hex": "#004B1C",
      "fontClass": "ms-fontColor-greenDark",
      "bgClass": "ms-bgColor-greenDark",
      "borderClass": "ms-borderColor-greenDark"
    }
  ]
}
```

### File: src\documentation\templates\models\AnimationModel.json
```json
{
  "items": [
    {
      "class": "ms-slideRightIn10",
      "description": "Slide right 10px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideRightIn20",
      "description": "Slide right 20px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideRightIn40",
      "description": "Slide right 40px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideLeftIn10",
      "description": "Slide left 10px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideLeftIn20",
      "description": "Slide left 20px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideLeftIn40",
      "description": "Slide left 40px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideUpIn20",
      "description": "Slide up 20px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideUpIn10",
      "description": "Slide up 10px and fade in",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-slideDownIn20",
      "description": "Slide down 20px and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-slideDownIn10",
      "description": "Slide down 10px and fade in",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-slideRightOut40",
      "description": "Slide right 40px and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-slideLeftOut40",
      "description": "Slide left 40px and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-slideUpOut20",
      "description": "Slide up 20px and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-slideUpOut10",
      "description": "Slide up 10px and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-slideDownOut20",
      "description": "Slide down 20px and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-slideDownOut10",
      "description": "Slide down 10px and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-scaleUpIn100",
      "description": "Scale up to 100% and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-scaleDownIn100",
      "description": "Scale down to 100% and fade in",
      "bezier": "cubic-bezier(0.1, 0.9, 0.2, 1)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-scaleUpOut103",
      "description": "Scale up to 103% and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-scaleDownOut98",
      "description": "Scale down to 98% and fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-fadeIn100",
      "description": "Fade in",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-fadeIn200",
      "description": "Fade in",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.267s" 
    },
    {
      "class": "ms-fadeIn400",
      "description": "Fade in",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.367s" 
    },
    {
      "class": "ms-fadeIn500",
      "description": "Fade in",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.467s" 
    },
    {
      "class": "ms-fadeOut100",
      "description": "Fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.167s" 
    },
    {
      "class": "ms-fadeOut200",
      "description": "Fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.267s" 
    },
    {
      "class": "ms-fadeOut400",
      "description": "Fade out",
      "bezier": "cubic-bezier(0.1, 0.25, 0.75, 0.9)",
      "timing": "0.367s" 
    }
  ]
}
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
