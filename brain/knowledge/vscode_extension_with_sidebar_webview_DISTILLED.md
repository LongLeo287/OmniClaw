---
id: vscode-extension-with-sidebar-webview
type: knowledge
owner: OA_Triage
---
# vscode-extension-with-sidebar-webview
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "vscode-webview-extension-with-react",
  "displayName": "vscode-webview-extension-with-react",
  "description": "Example of create webview",
  "publisher": "HuyQLuong",
  "version": "0.0.2",
  "engines": {
    "vscode": "^1.64.0"
  },
  "categories": [
    "Other"
  ],
  "activationEvents": [
    "onCommand:vscode-webview-extension-with-react.helloWorld",
    "onView:left-panel-webview"
  ],
  "main": "./dist/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "vscode-webview-extension-with-react.helloWorld",
        "title": "Hello World"
      }
    ],
    "viewsContainers": {
      "activitybar": [
        {
          "id": "webview",
          "title": "Example for webview",
          "icon": "./assets/extension-icon.png"
        }
      ]
    },
    "views": {
      "webview": [
        {
          "type": "webview",
          "id": "left-panel-webview",
          "name": "Webview",
          "icon": "src/assets/extension-icon.png"
        }
      ]
    }
  },
  "scripts": {
    "compile": "npm run tsc -p ./",
    "watch": "tsc -watch -p ./ && npm run compile",
    "vscode:package": "vsce package",
    "webpack": "rm -rf ./dist/* && webpack --mode development",
    "package": "rm -rf *.vsix && npm run webpack && vsce package"
  },
  "devDependencies": {
    "@types/glob": "^7.2.0",
    "@types/mocha": "^9.1.0",
    "@types/node": "14.x",
    "@types/vscode": "^1.64.0",
    "@typescript-eslint/eslint-plugin": "^5.12.1",
    "@typescript-eslint/parser": "^5.12.1",
    "@vscode/test-electron": "^2.1.2",
    "eslint": "^8.9.0",
    "glob": "^7.2.0",
    "mocha": "^9.2.1",
    "ts-loader": "^9.2.6",
    "typescript": "^4.5.5",
    "webpack": "^5.69.1",
    "webpack-cli": "^4.9.2"
  },
  "dependencies": {
    "@types/react-dom": "^17.0.11",
    "dotenv-webpack": "^7.1.0",
    "module-alias": "^2.2.2",
    "path": "^0.12.7",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "_moduleAliases": {
    "utils": "dist/utils",
    "providers": "dist/providers",
    "components": "dist/components",
    "constant": "dist/constant.js"
  }
}

```

### File: README.md
```md
# vscode-webview-extension-with-react README

vscode-webview-extension-with-react is a repo to illustrate how to register a webview using react to side bar of vscode when developing vscode extension
# 1. Create a webview to VScode extension side panel

- In `package.json` we need to register a view container to have a icon in side bar

        ```
            "viewsContainers": {
                "activitybar": [
                    {
                        "id": "webview",
                        "title": "Example for webview",
                        "icon": "./assets/extension-icon.png"
                    }
                ]
            },
            "views": {
                "webview": [
                    {
                        "type": "left-panel-webviews",
                        "id": "left-panel-webview",
                        "name": "Webview",
                        "icon": "src/assets/extension-icon.png"
                    }
                ]
            }
        ```
- Create a webview provider `LeftPanelWebview` which is implemented from `WebviewViewProvider`

    - Note that: 
        - We can assign data from extension to this webview such as `extensionPath` when create `LeftPanelWebview` class
        - `resolveWebviewView` will be the function calling first we open the webview
        - `_getHtmlForWebview` will be the function to render the webview from react
        - The script for the webview can be register in the `body` of webview

            ```
            	<script nonce="${nonce}" type="text/javascript" src="${constantUri}"></script>
				<script nonce="${nonce}" src="${scriptUri}"></script>
            ```

        - For styling, let add CSS file to `link` tag
            ```
                <link href="${styleUri}" rel="stylesheet">
            ```
- Declare `LeftPanelWebview` class and register Webview in `extension.ts`
    ```js
        const leftPanelWebViewProvider = new LeftPanelWebview(context?.extensionUri, {});
        let view = vscode.window.registerWebviewViewProvider(
            EXTENSION_CONSTANT.LEFT_PANEL_WEBVIEW_ID,
            leftPanelWebViewProvider,
        );
        context.subscriptions.push(view);
    ```

- Then you will have a webview in side panel !!

# 2. How to render react component in vscode and handle user action

- When calling Webview for the first time, `resolveWebviewView` will be called and expect to return the html file of the webview. We will use `ReactDOM.renderToString` to concat the react component into `body` tag of the html file. In that case, react component will be rendered.

```
<body>
    ${
        
        ReactDOMServer.renderToString((
            <LeftPanel message={"Tutorial for Left Panel Webview in VSCode extension"}></LeftPanel>
        ))
    }
    <script nonce="${nonce}" type="text/javascript" src="${constantUri}"></script>
    <script nonce="${nonce}" src="${scriptUri}"></script>
</body>
```

- The weakness of this approach is the webview will only be a static html view. Because of this problem, we will need to embedded the script into html so that we can handle user action base on eventListener from DOM

- We can also handle user action in script and callback to our extension by using `vscode.postMessage` in script file and use `_view.webview.onDidReceiveMessage` to receive the message in webview components
    ```
    // Script file: Emit message
    vscode.postMessage({ 
                action: POST_MESSAGE_ACTION.SHOW_WARNING_LOG, 
                data: {
                    message: "You just clicked on the left panel webview button"
            }});
    ```

    ```
    this._view.webview.onDidReceiveMessage((message) => {
                switch (message.action){
                    case 'SHOW_WARNING_LOG':
                        window.showWarningMessage(message.data.message);
                        break;
                    default:
                        break;
                }
    });
    ```
- Using this way of communication between webview and extension, we also can create a message chanel between 2 separated webview in some complicated vscode extension


Reference url: https://medium.com/@luongquochuy1995/create-a-vs-code-left-panel-web-view-extension-using-react-e765fd901f64

**If you have any further question, feel free to contact luongquochuy1995@gmail.com**

```

### File: .eslintrc.json
```json
{
    "root": true,
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "ecmaVersion": 6,
        "sourceType": "module"
    },
    "plugins": [
        "@typescript-eslint"
    ],
    "rules": {
        "@typescript-eslint/naming-convention": "warn",
        "@typescript-eslint/semi": "warn",
        "curly": "warn",
        "eqeqeq": "warn",
        "no-throw-literal": "warn",
        "semi": "off"
    },
    "ignorePatterns": [
        "out",
        "dist",
        "**/*.d.ts"
    ]
}

```

### File: CHANGELOG.md
```md
# Change Log

All notable changes to the "vscode-webview-extension-with-react" extension will be documented in this file.

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.

## [Unreleased]

- Initial release
```

### File: tsconfig.json
```json
{
	"compilerOptions": {
		"module": "commonjs",
		"target": "es6",
		"outDir": "dist",
		"lib": [
			"es6",
			"dom"
		],
		"baseUrl": "./src",
		"sourceMap": true,
		"paths" : {
			"*": ["*"],
		},
		"strict": false,   /* enable all strict type-checking options */
		"jsx": "react-jsx",
		"noUnusedParameters": false,  /* Report errors on unused parameters. */
		"noEmitHelpers": true,
		"importHelpers": true,
	},
	"exclude": [
		"node_modules",
		".vscode-test"
	]
}

```

### File: vsc-extension-quickstart.md
```md
# Welcome to your VS Code Extension

## What's in the folder

* This folder contains all of the files necessary for your extension.
* `package.json` - this is the manifest file in which you declare your extension and command.
  * The sample plugin registers a command and defines its title and command name. With this information VS Code can show the command in the command palette. It doesn’t yet need to load the plugin.
* `src/extension.ts` - this is the main file where you will provide the implementation of your command.
  * The file exports one function, `activate`, which is called the very first time your extension is activated (in this case by executing the command). Inside the `activate` function we call `registerCommand`.
  * We pass the function containing the implementation of the command as the second parameter to `registerCommand`.

## Setup

* install the recommended extensions (amodio.tsl-problem-matcher and dbaeumer.vscode-eslint)


## Get up and running straight away

* Press `F5` to open a new window with your extension loaded.
* Run your command from the command palette by pressing (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and typing `Hello World`.
* Set breakpoints in your code inside `src/extension.ts` to debug your extension.
* Find output from your extension in the debug console.

## Make changes

* You can relaunch the extension from the debug toolbar after changing code in `src/extension.ts`.
* You can also reload (`Ctrl+R` or `Cmd+R` on Mac) the VS Code window with your extension to load your changes.


## Explore the API

* You can open the full set of our API when you open the file `node_modules/@types/vscode/index.d.ts`.

## Run tests

* Open the debug viewlet (`Ctrl+Shift+D` or `Cmd+Shift+D` on Mac) and from the launch configuration dropdown pick `Extension Tests`.
* Press `F5` to run the tests in a new window with your extension loaded.
* See the output of the test result in the debug console.
* Make changes to `src/test/suite/extension.test.ts` or create new test files inside the `test/suite` folder.
  * The provided test runner will only consider files matching the name pattern `**.test.ts`.
  * You can create folders inside the `test` folder to structure your tests any way you want.

## Go further

* Reduce the extension size and improve the startup time by [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) on the VSCode extension marketplace.
* Automate builds by setting up [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

```

### File: webpack.config.js
```js
//@ts-check

'use strict';

const path = require('path');


/**@type {import('webpack').Configuration}*/
// @ts-ignore
const config = {

  target: 'node', // vscode extensions run in a Node.js-context 📖 -> https://webpack.js.org/configuration/node/

  entry: './src/extension.ts', // the entry point of this extension, 📖 -> https://webpack.js.org/configuration/entry-context/
  output: {
    // the bundle is stored in the 'dist' folder (check package.json), 📖 -> https://webpack.js.org/configuration/output/
    path: path.resolve(__dirname, 'dist'),
    filename: 'extension.js',
    libraryTarget: 'commonjs2',
    devtoolModuleFilenameTemplate: '../[resource-path]'
  },
  devtool: 'source-map',
  externals: {
    vscode: 'commonjs vscode' // the vscode-module is created on-the-fly and must be excluded. Add other modules that cannot be webpack'ed, 📖 -> https://webpack.js.org/configuration/externals/
  },
  resolve: {
    // support reading TypeScript and JavaScript files, 📖 -> https://github.com/TypeStrong/ts-loader
    extensions: ['.ts', '.js', '.tsx'],
    alias: {
      utils: path.resolve(__dirname, './src/utils.ts'),
      constant: path.resolve(__dirname, './src/constant.ts'),
      providers: path.resolve(__dirname, './src/providers/'),
      components: path.resolve(__dirname, './src/components/'),
    },
  },
  plugins: [
      // @ts-ignore
  ],
  module: {
    rules: [
      {
        test: /\.ts$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'ts-loader'
          }
        ]
      },
      {
        test: /\.tsx$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'ts-loader'
          }
        ]
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: [ 'style-loader', 'css-loader']
      }
    ]
  }
};
module.exports = config;

```

### File: script\constant.js
```js
const ELEMENT_IDS = {
    TRIGGER_MESSAGE_BUTTON: 'trigger-show-message-button'
};

const POST_MESSAGE_ACTION = {
    SHOW_WARNING_LOG: 'SHOW_WARNING_LOG'
}
```

### File: script\left-webview-provider.css
```css
.panel-wrapper {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.panel-info {
    font-size: 1.2rem;
    font-weight: bold;
    line-height: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 1rem;
    text-align: center;
}
```

### File: script\left-webview-provider.js
```js
(function () {
    const vscode = acquireVsCodeApi();
    document.getElementById(ELEMENT_IDS.TRIGGER_MESSAGE_BUTTON).addEventListener('click', ()=> {
        vscode.postMessage({ 
            action: POST_MESSAGE_ACTION.SHOW_WARNING_LOG, 
            data: {
                message: "You just clicked on the left panel webview button"
        }});
    });
}());
```

### File: src\constant.ts
```ts
const LEFT_PANEL_WEBVIEW_ID = 'left-panel-webview';

const ELEMENT_IDS = {
    TRIGGER_MESSAGE_BUTTON: 'trigger-show-message-button'
};

export const EXTENSION_CONSTANT = {
    LEFT_PANEL_WEBVIEW_ID,
    ELEMENT_IDS
};
```

### File: src\extension.ts
```ts
try {
	require("module-alias/register");
} catch (e) {
	console.log("module-alias import error !");
}
import * as vscode from "vscode";
import { EXTENSION_CONSTANT } from "constant";
import { LeftPanelWebview } from "providers/left-webview-provider";

export function activate(context: vscode.ExtensionContext) {
	let helloWorldCommand = vscode.commands.registerCommand(
		"vscode-webview-extension-with-react.helloWorld",
		() => {
			vscode.window.showInformationMessage(
				"Hello World from vscode-webview-extension-with-react!"
			);
		}
	);
	context.subscriptions.push(helloWorldCommand);

	// Register view
	const leftPanelWebViewProvider = new LeftPanelWebview(context?.extensionUri, {});
	let view = vscode.window.registerWebviewViewProvider(
		EXTENSION_CONSTANT.LEFT_PANEL_WEBVIEW_ID,
		leftPanelWebViewProvider,
	);
	context.subscriptions.push(view);

};

// this method is called when your extension is deactivated
export function deactivate() {}

```

### File: src\utils.ts
```ts
function getNonce() {
    let text = '';
    const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 32; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}

export const Utils = {
    getNonce,
};
```

### File: src\test\runTest.ts
```ts
import * as path from 'path';

import { runTests } from '@vscode/test-electron';

async function main() {
	try {
		// The folder containing the Extension Manifest package.json
		// Passed to `--extensionDevelopmentPath`
		const extensionDevelopmentPath = path.resolve(__dirname, '../../');

		// The path to test runner
		// Passed to --extensionTestsPath
		const extensionTestsPath = path.resolve(__dirname, './suite/index');

		// Download VS Code, unzip it and run the integration test
		await runTests({ extensionDevelopmentPath, extensionTestsPath });
	} catch (err) {
		console.error('Failed to run tests');
		process.exit(1);
	}
}

main();

```

