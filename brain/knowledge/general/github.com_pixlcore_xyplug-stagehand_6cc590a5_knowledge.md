---
id: github.com-pixlcore-xyplug-stagehand-6cc590a5-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.228529
---

# KNOWLEDGE EXTRACT: github.com_pixlcore_xyplug-stagehand_6cc590a5
> **Extracted on:** 2026-04-01 08:50:11
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519826/github.com_pixlcore_xyplug-stagehand_6cc590a5

---

## File: `.gitignore`
```
node_modules/
downloads/
work/
```

## File: `Dockerfile`
```
FROM node:22-bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libnss3 \
      libatk-bridge2.0-0 \
      libgtk-3-0 \
      libxss1 \
      libasound2 \
	  iproute2 \
	  tar \
	  gzip

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /app
COPY . .
RUN npm install

RUN npx playwright install-deps chromium
RUN npx playwright install chromium

RUN npm install -g @pixlcore/xyrun

RUN rm -rf /var/lib/apt/lists/*

CMD ["xyrun", "node", "index.js"]
```

## File: `LICENSE.md`
```markdown
# License

**The MIT License (MIT)**

*Copyright (c) 2025 Joseph Huckaby and PixlCore*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
<p align="center"><img src="https://raw.githubusercontent.com/pixlcore/xyplug-stagehand/refs/heads/main/logo.png" height="108" alt="Stagehand"/></p>
<h1 align="center">Stagehand Automation Plugin</h1>

A Stagehand event plugin for the [xyOps Workflow Automation System](https://xyops.io). This package provides an AI-powered browser automation framework for xyOps.  Using it you can drive a headless browser with simple English instructions, take actions, extract data, capture network requests, and even record a video of the whole session.

A headless Chromium is launched and automated locally in a Docker container.  This Plugin does not use any "cloud" browser environments.  Note that if you use any of the AI features, then you need to be careful with sensitive information, as they may be sent to the AI provider.  See below for discussion and mitigation techniques.

This Plugin relies heavily on the [Stagehand](https://github.com/browserbase/stagehand) and [Playwright](https://github.com/microsoft/playwright) libraries. See those repos for full documentation and low-level usage.

## Requirements

- **Docker**
	- This Plugin ships as a prebuilt Docker container, so your xyOps servers will need Docker installed for this to work.
- **AI Credentials**
	- If you intend to use any of the AI features, you will need an API Key for your chosen provider.

## Environment Variables

If you are going to use the AI features in Stagehand, create a [Secret Vault](https://xyops.io/docs/secrets) in xyOps and assign this Plugin to it.  Add your AI provider's API Key in a new variable named:

```
AI_API_KEY
```

Stagehand supports Google, OpenAI, Anthropic, xAI, DeepSeek, Perplexity, Azure, Ollama, or any other LLM model from the [Vercel AI SDK](https://sdk.vercel.ai/providers).

## Usage

### Script

The Plugin "Script" parameter is expected to be a list of instructions for the browser to perform, one per line.  It can be plain text or [JSON](#advanced).  This section will focus on the plain text format, which looks like this:

```
Navigate to https://mycompany.com/
Type "foo" into the Username text field.
Type "bar" into the Password text field.
Click the "Login" button.
Sleep for 3000
```

Each line should contain a simple instruction (i.e. one action).  For each line, the Plugin defaults to calling Stagehand [act()](https://docs.stagehand.dev/v3/basics/act) unless prefixed by a specific keyword.  See below for specific keywords.

### Perform Actions

The default behavior is to [act()](https://docs.stagehand.dev/v3/basics/act) (take action) on the instruction.  This expects commands such as:

| Action | Example instruction |
|--------|---------------------|
| Click | `click the button` |
| Fill | `fill the field with <value>` |
| Type | `type <text> into the search box` |
| Press | `press <key> in the search field` |
| Scroll | `scroll to <position>` |
| Select | `select <value> from the dropdown` |

### Browser Navigation

You can navigate to URLs at any time, by starting the line with the word "Navigate":

```
Navigate to https://news.ycombinator.com/
```

### Extract Data

To extract data from the page, begin the line with the word "Extract", and describe exactly what you want, including the desired output format.  Example:

```
Extract the first three article titles, in a JSON array.
```

The extraction results will be included in the Job output data, in an array called `extractions`.  Example output:

```json
{
	"extractions": [
		{
			"prompt": "Extract the first three article titles, in a JSON array.",
			"result": [
				"Same-day upstream Linux support for Snapdragon 8 Elite Gen 5",
				"Underrated reasons to be thankful V",
				"Physicists drive antihydrogen breakthrough at CERN"
			]
		}
	]
}
```

If you ask for JSON in the extraction prompt, and the extraction itself is valid JSON, it is parsed for you and included as an object/array in the "result" property.  Otherwise, it will be a text string.

This feature uses the Stagehand [extract()](https://docs.stagehand.dev/v3/basics/extract) function.

### Capture Network Requests

To capture network requests, including raw responses, include a line in your script starting with the word "Capture", followed by a URL (substring match).  Example:

```
Capture /y18.svg
```

Make sure you add your captures *before* you navigate to the page or take the action that will trigger the network request.  This command installs a "listener" on all network requests that match the URL you specify (which can be partial; it's a substring match).

For any matches, results will be included in the Job output data, in an array called `captures`.  Example output:

```json
{
	"captures": [
		{
			"url": "https://news.ycombinator.com/y18.svg",
			"status": 200,
			"headers": { "Content-Type": "image/svg" },
			"response": "<svg height=\\"18\\" viewBox=\\"4 4 188 188\\" width=\\"18\\" xmlns=\\"http://www.w3.org/2000/svg\\"><path d=\\"m4 4h188v188h-188z\\" fill=\\"#f60\\"/><path d=\\"m73.2521756 45.01 22.7478244 47.39130083 22.7478244-47.39130083h19.56569631l-34.32352071 64.48661468v41.49338532h-15.98v-41.49338532l-34.32352071-64.48661468z\\" fill=\\"#fff\\"/></svg>"
		}
	]
}
```

If the response appears to be JSON, it will be parsed and returned as an object/array.  Otherwise it will be a string, as shown above.  This should only be used for text-based resources, not binary ones.

### Evaluate JavaScript

To evaluate arbitrary JavaScript code in the browser (in the context of the current page), include a line in your script starting with the word "Evaluate", followed by the JavaScript code to run.  Example:

```
Evaluate 4 + 5
```

For any evaluations, results will be included in the Job output data, in an array called `evaluations`.  Example output:

```json
{
	"evaluations": [
		{
			"script": "4 + 5",
			"result": 9
		}
	]
}
```

### Sleep

To insert a sleep step for a specified duration, add a line in your script starting with the word "Sleep", followed by the number of milliseconds to sleep for  Example:

```
Sleep 5000
```

### Downloads

If you trigger any downloads during the browser session, they will be attached to the Job output as files.  These can be used in downstream jobs if connected via workflow or run action.

## Advanced

In addition to the simple text script format shown above, you can alternatively pass a JSON object as the script.  This allows you to specify advanced options and perform exact browser actions (i.e. not using AI).  Here is the format expected:

```json
{
	"steps": [
		{
			"type": "navigate",
			"url": "https://mycompany.com/"
		},
		{
			"type": "change",
			"selectors": ["aria/Username", "form > div:nth-of-type(1) input"],
			"value": "foo"
		},
		{
			"type": "change",
			"selectors": ["aria/Password", "form > div:nth-of-type(2) input"],
			"value": "bar"
		},
		{
			"type": "click",
			"selectors": ["aria/Login", "form > button"]
		}
	]
}
```

The `steps` property should be an array of objects.  Each object should have a `type` property, and other type-specific properties.  Here are the available types, and their required properties:

| Type | Params | Description |
|------|--------|-------------|
| `navigate` | `url` | Navigate to a new URL specified by `url`, and wait for the `load` event to fire. |
| `click` | `selectors` | Click on a target specified by whichever of the `selectors` matches first. |
| `doubleClick` | `selectors` | Double-click on a target specified by whichever of the `selectors` matches first. |
| `change` | `selectors`, `value` | Change a form field, specified by whichever of the `selectors` matches first, to the `value` value. |
| `keyDown` | `key` | Press down a specific key on the keyboard, specified by `key`. |
| `keyUp` | `key` | Release a specific key on the keyboard, specified by `key`. |
| `text` | `text` | Type in a string of `text`, just as if it was typed from the keyboard. |
| `evaluate` | `script` | Evaluate JavaScript code in the browser, in the context of the current page. |
| `sleep` | `duration` | Sleep for the specified amount of milliseconds in `duration`. |
| `waitFor` | `selectors` | Wait for any of the `selectors` to be visible. |
| `reload` | - | Reload the current page and wait for the `load` event to fire. |
| `capture` | `url` | Start a network capture for all requests matching URL or partial URL specified by `url`. |
| `action` | `prompt` | **(Uses AI)** Take action on the page using AI and a natural language prompt. |
| `extract` | `prompt` | **(Uses AI)** Extract content from the page using AI and a natural language prompt. |

### Advanced Capture

For the `capture` type, there are two optional properties you can set:

- If you set `download` to `true`, the raw response will be downloaded instead of included in the Job output data object.
- If you also set `pretty` to `true`, and the response is JSON format, it will be pretty-printed in the downloaded file.

These options are useful for capturing **large** amounts of data that you don't want passed around inside the job object, for memory and/or performance concerns, or if the response is binary.  Downloaded files are still attached to the job and passed to the next job via workflow or run action, as well as made available for viewing / downloading in the xyOps UI.

### Replay Chrome Recordings

The advanced JSON format described above is actually compatible with the [Chrome Dev Tools Recorder](https://developer.chrome.com/docs/devtools/recorder) feature, specifically its JSON export format.

To access the recorder, while in Chrome Dev Tools, press `Control+Shift+P` (Windows / Linux) or `Command+Shift+P` (Mac), and type "Recorder", then hit Enter.

When you finish a recording, while still on the detail view in Dev Tools, if you click the tiny little "Download" (downward-facing arrow) button in the toolbar, you can choose from a variety of formats.  Select "JSON", save the file, and then you can copy & paste (or just directly upload) the file into the xyOps Plugin Script Editor.

### Exit Steps

If your script has steps that must **always** be executed, even in the event of an error, include an `always` property and set it to `true`.  This feature can be used for situations like a logout sequence, which must be executed even if the other steps failed for whatever reason.  Example:

```json
{
	"type": "click",
	"selectors": [
		[ "aria/Logout" ]
	],
	"always": true
}
```

## Privacy

If you use any of the AI features, then the entire DOM tree of your visited pages are sent to the selected AI provider.  This may include sensitive information, especially if you type it into forms.  There are two ways to help mitigate this:

First, use the [Protect Sensitive Data](https://docs.stagehand.dev/v3/best-practices/prompting-best-practices#protect-sensitive-data) feature of Stagehand to use special placeholder macros for usernames, passwords, and other sensitive data.  Add these to your [Secret Vault](https://xyops.io/docs/secrets) and you can use the values via Stagehand's percent-wrapped syntax, e.g. `%USERNAME%`, `%PASSWORD%`, etc.  Also, set the "Verbose" selector to `0` to prevent these values from appearing in your job output.

The second thing you can do is run a local AI server in your infra, such as [Ollama](https://ollama.com/), and point to it via the "AI Base URL" parameter.  This will prevent all outbound requests, except of course the pages you navigate to, and perhaps some anonymous usage metrics broadcast by Chromium.

## Caching

### Browser Caching

To reduce browser network usage, and to retain things like cookies and user storage, you can utilize the built-in caching features of Chromium.  However, our Docker container is ephemeral and loses everything after each run (by design).  So, to retain the browser's user profile directory, you will need to create a volume bind so it shares a dir on the host.  This is not enabled by default for privacy concerns (i.e. leaking data outside the container).

To enable persistent browser caching, add this to your xyOps Plugin command, before the image name:

```
-v "$TMPDIR/xyplug-stagehand-profile:/app/profile"
```

### AI Caching

To reduce AI token usage, you can utilize the [Caching Actions](https://docs.stagehand.dev/v3/best-practices/caching) feature of Stagehand, which remembers the UI elements you target by storing a hash of the prompt.  However, our Docker container is ephemeral and loses everything after each run (by design).  So, to retain the cache directory, you will need to create a volume bind so it shares a dir on the host.  This is not enabled by default for privacy concerns (i.e. leaking data outside the container).

To enable persistent AI prompt caching, add this to your xyOps Plugin command, before the image name:

```
-v "$TMPDIR/xyplug-stagehand-ai-cache:/app/cache"
```

**Note:** If the website structure changes significantly, clear your cache directory to force fresh inference.

## Limitations

- Agent Mode: Stagehand's [Agent Mode](https://docs.stagehand.dev/v3/basics/agent) is currently not supported.
- Single-Page Only: Currently this plugin can only automate a single browser page / tab.
- Chromium Only: Currently this plugin only works with headless Chromium.

If there is enough interest we can add these features!  Let us know!

## Development

Here is how you can download the very latest dev build and install it manually:

```
git clone https://github.com/pixlcore/xyplug-stagehand.git
cd xyplug-stagehand
```

I highly recommend placing the following `.gitignore` file at the base of the project, if you plan on committing changes and sending pull requests:

```
.gitignore
/node_modules
```

## Testing

When invoked by xyOps the script expects JSON input via STDIN.  You can, however, fake this with a JSON file that you pipe into the script.  Example file:

```json
{
	"xy": 1,
	"params": {
		"ai_model_name": "google/gemini-2.5-flash",
		"ai_base_url": "",
		"ai_system_prompt": "",
		"ai_log_inference": true,
		"width": 1280,
		"height": 720,
		"video": "always",
		"verbose": 2,
		"aiTimeout": 60000,
		"domTimeout": 3000,
		"navTimeout": 30000,
		"script": "Navigate to https://news.ycombinator.com/\nExtract the first three article titles, in a JSON array."
	}
}
```

Example Dev setup:

```sh
# Build local docker image
docker build -t xyplug-stagehand-dev .

# Run with test file pipe, and index.js and downloads mapped to container
cat MY_TEST_FILE.json | docker run --rm -i --init --ipc=host -v "./downloads:/app/downloads" -v "./index.js:/app/index.js" -e AI_API_KEY="YOUR_AI_API_KEY_HERE" xyplug-stagehand-dev
```

## License

MIT
```

## File: `index.js`
```javascript
// Stagehand wrapper for xyOps
// Copyright (c) 2025 - 2026 PixlCore LLC
// MIT License

import { Stagehand } from "@browserbasehq/stagehand";
import { chromium } from "playwright-core";
import { z } from "zod";
import { globSync, unlinkSync, existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { basename } from 'node:path';

globalThis.AI_SDK_LOG_WARNINGS = false;

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
};

const app = {
	
	job: null,
	params: null,
	stagehand: null,
	browser: null,
	context: null,
	page: null,
	output: {},
	captures: [],
	steps: [],
	stepIdx: 0,
	
	async run() {
		// read in data from xyops
		const chunks = [];
		for await (const chunk of process.stdin) { chunks.push(chunk); }
		let job = this.job = JSON.parse( chunks.join('') );
		let params = this.params = job.params;
		
		// apply defaults and normalization on some params
		params.verbose = parseInt( params.verbose || 0 );
		params.width = parseInt( params.width || 1280 );
		params.height = parseInt( params.height || 720 );
		params.aiTimeout = parseInt( params.aiTimeout || 60000 );
		params.domTimeout = parseInt( params.domTimeout || 3000 );
		params.navTimeout = parseInt( params.navTimeout || 30000 );
		params.stepDelay = parseInt( params.stepDelay || 1000 );
		params.video = ('' + params.video).toLowerCase() || 'none';
		
		this.logVerbose("Job Parameters: " + JSON.stringify(params));
		
		// setup stagehand opts
		let sh_opts = {
			env: "LOCAL",
			model: {
				modelName: params.ai_model_name || 'google/gemini-2.5-flash',
				apiKey: process.env.AI_API_KEY || ''
			},
			verbose: params.verbose || 0,
			cacheDir: "cache",
			logInferenceToFile: params.ai_log_inference || false,
			domSettleTimeout: params.domTimeout,
			
			localBrowserLaunchOptions: {
				executablePath: globSync('/ms-playwright/chromium-*/chrome-*/chrome')[0],
				headless: true,
				viewport: { 
					width: params.width || 1280,
					height: params.height || 720
				},
				deviceScaleFactor: params.scale || 1.0, // Display scaling
				ignoreHTTPSErrors: params.ssl_cert_bypass || false, // Ignore certificate errors
				locale: params.locale || 'en-US', // Set browser language
				downloadsPath: './downloads', // Download directory
				acceptDownloads: true, // Allow downloads
				
				args: [
					// "--remote-debugging-port=9222",
					// "--remote-debugging-address=127.0.0.1",
					"--no-sandbox",
					"--disable-setuid-sandbox",
					"--disable-dev-shm-usage",
					"--disable-gpu",

					// Playwright usually adds these automatically; safe either way:
					"--disable-background-networking",
					"--no-first-run",
					"--no-default-browser-check",
					"--disable-features=TranslateUI",
				],
				
				// Optional: your own Chrome profile dir
				userDataDir: "./profile",
				// keep it between runs
				preserveUserDataDir: true,
			}
		};
		
		if (params.ai_base_url) {
			sh_opts.model.baseURL = params.ai_base_url;
		}
		if (params.ai_system_prompt) {
			sh_opts.systemPrompt = params.ai_system_prompt;
		}
		
		// make sure downloads dir exists
		if (!existsSync('downloads')) mkdirSync('downloads');
		
		// at vebose level 2, dump job data and env to downloads
		if (params.verbose >= 2) {
			writeFileSync( 'downloads/job.json', JSON.stringify(job, null, "\t") + "\n" );
			writeFileSync( 'downloads/env.json', JSON.stringify(process.env, null, "\t") + "\n" );
		}
		
		console.log(`🔵 Initializing Stagehand...`);
		this.logVerbose( "Stagehand Config: " + JSON.stringify(sh_opts) );
		
		// init stagehand
		let stagehand = this.stagehand = new Stagehand(sh_opts);
		await stagehand.init();
		
		// Connect Playwright to Stagehand's browser
		let browser = this.browser = await chromium.connectOverCDP({
			wsEndpoint: stagehand.connectURL(),
		});
		
		var ctx_opts = {};
		if (params.video != 'none') {
			ctx_opts.recordVideo = {
				dir: 'downloads',
				size: {
					width: params.width || 1280,
					height: params.height || 720
				},
			};
		}
		let context = this.context = await browser.newContext(ctx_opts);
		let page = this.page = await context.newPage();
		
		page.setDefaultTimeout( params.domTimeout );
		page.setDefaultNavigationTimeout( params.navTimeout );
		
		context.on("response", async (res) => {
			const url = res.url();
			const status = res.status();
			const headers = res.headers();
			
			this.logVerbose(`🌎 Network Request [${status}] ${url}`);
			
			let step = this.captures.find( (step) => {
				return !!url.includes( step.url );
			} );
			if (!step) return;
			
			if (!this.output.captures) this.output.captures = [];
			let capture = { url, status, headers };
			let data = null;
			
			console.log(`🟢 Request Captured [${res.status()}] ${url}`);
			
			try {
				const ct = headers["content-type"] || "";
				if (ct.includes("application/json")) {
					data = await res.json();
					this.logVerbose( "JSON Captured: " + JSON.stringify(data) );
				}
				else {
					data = await res.text();
					this.logVerbose( "Text Captured: " + data );
				}
			} 
			catch (e) {
				console.error("🛑 Error reading response body: ", e.message);
			}
			
			if (step.download) {
				// download as file
				var file = 'downloads/' + url.replace(/^\w+\:\/\/[^\/]+\//, '').replace(/\/$/, '').replace(/[^\w\-\.]+/g, '_').toLowerCase();
				
				if (!file.match(/\.\w+$/) && headers["content-type"] && headers["content-type"].match(/^\w+\/(\w+)/)) {
					file += '.' + RegExp.$1;
				}
				if (!file.match(/\.\w+$/)) {
					file += '.bin';
				}
				
				var payload = data;
				if (typeof(data) == 'object') {
					payload = step.pretty ? JSON.stringify(data, null, "\t") : JSON.stringify(data);
					payload += "\n";
				}
				
				// auto-increment file number if exists
				var file_num = 0;
				var orig_file = file;
				while (existsSync(file)) {
					file_num++;
					file = orig_file.replace( /(\.\w+)$/, '-' + file_num + '$1' );
				}
				
				writeFileSync( file, payload );
				capture.filename = basename(file);
			}
			else {
				// include in job data
				capture.response = data;
			}
			
			this.output.captures.push(capture);
		});
		
		await this.compileScript();
		if (!this.steps.length) throw new Error("Cannot run script: No steps found.");
		
		await this.runScript();
		await this.finish();
	},
	
	async compileScript() {
		// compile text script into JSON, if needed
		const params = this.params;
		
		// if script is already an object, we done
		if ((typeof(params.script) == 'object')) {
			this.steps = params.script.steps || [];
			return;
		}
		
		// if script is already json-text, just parse it
		if (params.script.trim().match(/^\{[\S\s]+\}$/)) {
			params.script = JSON.parse( params.script );
			this.steps = params.script.steps;
			return;
		}
		
		// parse as line-delimited instructions
		params.script.trim().split(/\n/).forEach( (line) => {
			line = line.trim();
			if (!line.match(/^\w/)) return; // ignore blanks and comments
			
			if (line.match(/^navigate\:?\s+(to\s+)?(\S+)$/i)) {
				this.steps.push({ type: 'navigate', url: RegExp.$2 });
			}
			else if (line.match(/^capture\:?\s+(\S+)$/i)) {
				this.steps.push({ type: 'capture', url: RegExp.$1 });
			}
			else if (line.match(/^extract\:?\s+/i)) {
				this.steps.push({ type: 'extract', prompt: line });
			}
			else if (line.match(/^evaluate\:?\s+(.+)$/i)) {
				this.steps.push({ type: 'evaluate', script: RegExp.$1 });
			}
			else if (line.match(/^sleep\:?\s+(for\s+)?(\d+)$/i)) {
				this.steps.push({ type: 'sleep', duration: parseInt(RegExp.$1) });
			}
			else {
				this.steps.push({ type: 'action', prompt: line });
			}
		} );
	},
	
	async runScript() {
		// here we go, run all steps
		try { 
			for (const step of this.steps) {
				await this.runStep(step);
			}
		}
		catch (err) {
			// a step failed, but the user may have "always" steps that must run no matter what
			// for e.g. a logout sequence
			var alwaysSteps = this.steps.filter( function(step) { return !!step.always } );
			if (alwaysSteps.length) {
				for (const step of alwaysSteps) {
					await this.runAlwaysStep(step);
				}
			}
			
			// throw original error regardless of always steps or their result
			throw err;
		}
	},
	
	getStepDescription(step) {
		// get step description text based on type and other props
		let desc = '';
		
		switch (step.type) {
			case 'navigate': desc = `Navigating to: ` + step.url; break;
			case 'capture': desc = `Capturing network requests for: ` + step.url; break;
			case 'action': desc = `Taking action: ` + step.prompt; break;
			case 'extract': desc = `Extracting data: ` + step.prompt; break;
			case 'setViewport': desc = `Setting viewport size: ` + step.width + 'x' + step.height; break;
			case 'click': desc = `Clicking on: ` + step.selectors.join(', '); break;
			case 'doubleClick': desc = `Double-clicking on: ` + step.selectors.join(', '); break;
			case 'change': desc = `Changing form element: ` + step.selectors.join(', ') + ` to: ` + step.value; break;
			case 'keyDown': desc = `Pressing key: ` + step.key; break;
			case 'keyUp': desc = `Releasing key: ` + step.key; break;
			case 'text': desc = `Typing text: ` + (step.text ?? step.value); break;
			case 'evaluate': desc = `Evaluating JavaScript: ` + step.script; break;
			case 'reload': desc = `Reloading page.`; break;
			case 'sleep': desc = `Sleeping for ${step.duration}ms.`; break;
			case 'waitFor': desc = `Waiting for: ` + step.selectors.join(', '); break;
		}
		
		return desc;
	},
	
	async runStep(step) {
		// run a single step
		let func = 'runStep_' + step.type;
		if (!this[func]) {
			// throw new Error("Unknown step type: " + step.type);
			this.logWarning( `Skipping unknown step type: ` + step.type );
			return;
		}
		
		const prefix = `🔵 Step ${ Math.floor(this.stepIdx + 1) }/${ this.steps.length }: `;
		console.log( prefix + this.getStepDescription(step) );
		
		await this[func](step);
		
		// update progress
		this.stepIdx++;
		if (this.job.xy) console.log( JSON.stringify({ xy:1, progress:this.stepIdx / this.steps.length }) );
		
		// sanity sleep between steps
		await sleep( this.params.stepDelay );
	},
	
	async runAlwaysStep(step) {
		// run a single step in "always" mode (e.g. a logout sequence)
		let func = 'runStep_' + step.type;
		if (!this[func]) {
			// throw new Error("Unknown step type: " + step.type);
			this.logWarning( `Skipping unknown step type: ` + step.type );
			return;
		}
		
		const prefix = `🟣 Exit Step: `;
		console.log( prefix + this.getStepDescription(step) );
		
		try { await this[func](step); }
		catch (err) {
			// step failed, but keep going anyway (always mode)
			this.logWarning( `Exit Step Failed: ` + err );
		}
		
		// sanity sleep between steps
		await sleep( this.params.stepDelay );
	},
	
	async runStep_navigate(step) {
		// nav to new url
		// step: { url, timeout?, waitUntil? }
		if (!step.url || (typeof(step.url) != 'string') || !step.url.match(/^\w+\:\/\/\S+$/)) {
			throw new Error("Navigate: Invalid URL: " + step.url);
		}
		
		await this.page.goto( step.url, { timeout: step.timeout || this.params.navTimeout, waitUntil: step.waitUntil || "load" } );
	},
	
	async runStep_reload(step) {
		// reload current page
		// step: { timeout?, waitUntil? }
		await this.page.reload({ timeout: step.timeout || this.params.navTimeout, waitUntil: step.waitUntil || 'load' });
	},
	
	async runStep_capture(step) {
		// add network capture
		// step: { url }
		if (!step.url || (typeof(step.url) != 'string')) {
			throw new Error("Capture: Invalid match: " + step.url);
		}
		this.captures.push( step );
	},
	
	async runStep_action(step) {
		// take action using AI
		// step: { prompt, timeout? }
		if (!step.prompt) throw new Error("Action: No prompt specified.");
		
		let result = await this.stagehand.act( step.prompt, { 
			variables: process.env, 
			timeout: step.timeout || this.params.aiTimeout,
			page: this.page 
		} );
		if (!result || !result.success) throw new Error("Action failed: " + result.actionDescription + ": " + result.message);
	},
	
	async runStep_extract(step) {
		// extract data using AI
		// step: { prompt, timeout? }
		if (!step.prompt) throw new Error("Extract: No prompt specified.");
		
		const result = await this.stagehand.extract( step.prompt, z.any(), { page: this.page, timeout: step.timeout || this.params.aiTimeout });
		if (!result) throw new Error("Extraction failed: " + step.prompt);
		
		if (!this.output.extractions) this.output.extractions = [];
		
		this.output.extractions.push({ 
			prompt: step.prompt,
			result: result
		});
	},
	
	async runStep_setViewport(step) {
		// change viewport size
		// step: { width, height }
		if (!step.width || !step.height) throw new Error("setViewPort: width and/or height missing.");
		
		await this.page.setViewportSize({ width, height });
	},
	
	async runStep_click(step) {
		// click the mouse on a target
		// step: { selectors, offsetX?, offsetY? }
		var locator = this.buildLocatorFromStep(step);
		
		const clickOptions = {
			timeout: this.params.domTimeout,
		};
		
		// DevTools uses offsetX/offsetY; Playwright uses position: { x, y }
		if (typeof step.offsetX === "number" && typeof step.offsetY === "number") {
			clickOptions.position = { x: step.offsetX, y: step.offsetY };
		}
		
		await locator.click(clickOptions);
	},
	
	async runStep_doubleClick(step) {
		// double-click the mouse on a target
		// step: { selectors, offsetX?, offsetY? }
		var locator = this.buildLocatorFromStep(step);
		
		const clickOptions = {
			timeout: this.params.domTimeout,
		};
		
		// DevTools uses offsetX/offsetY; Playwright uses position: { x, y }
		if (typeof step.offsetX === "number" && typeof step.offsetY === "number") {
			clickOptions.position = { x: step.offsetX, y: step.offsetY };
		}
		
		await locator.dblclick(clickOptions);
	},
	
	async runStep_change(step) {
		// change a form element's value
		// step: { selectors, value }
		var locator = this.buildLocatorFromStep(step);
		let value = step.value ?? "";
		
		// handle stagehand-style %placeholder% variables
		value = value.toString().replace( /\%(\w+)\%/g, function(m_all, m_g1) {
			if (!process.env[ m_g1 ]) throw new Error("Environment variable not found: " + m_g1);
			return process.env[ m_g1 ];
		} );
		
		await locator.fill(value, { timeout: this.params.domTimeout });
	},
	
	async runStep_keyDown(step) {
		// simulate pressing a key
		// step: { key }
		if (!step.key) throw new Error("keyDown: Missing key to hit.");
		
		await this.page.keyboard.down(step.key);
	},
	
	async runStep_keyUp(step) {
		// simulate releasing a key
		// step: { key }
		if (!step.key) throw new Error("keyUp: Missing key to release.");
		
		await this.page.keyboard.up(step.key);
	},
	
	async runStep_text(step) {
		// simulate typing a text string
		// step: { text }
		if (!step.text) throw new Error("Text: Missing text to enter.");
		
		let value = step.text ?? step.value;
		
		// handle stagehand-style %placeholder% variables
		value = value.toString().replace( /\%(\w+)\%/g, function(m_all, m_g1) {
			if (!process.env[ m_g1 ]) throw new Error("Environment variable not found: " + m_g1);
			return process.env[ m_g1 ];
		} );
		
		await this.page.keyboard.insertText( value );
	},
	
	async runStep_evaluate(step) {
		// run a JavaScript code snippet
		// step: { script }
		if (!step.script) throw new Error("Evaluate: Missing script code to execute.");
		
		let value = step.script;
		
		// handle stagehand-style %placeholder% variables
		value = value.toString().replace( /\%(\w+)\%/g, function(m_all, m_g1) {
			if (!process.env[ m_g1 ]) throw new Error("Environment variable not found: " + m_g1);
			return process.env[ m_g1 ];
		} );
		
		const result = await this.page.evaluate( value );
		
		if (!this.output.evaluations) this.output.evaluations = [];
		this.output.evaluations.push({
			script: step.script,
			result: result
		});
	},
	
	async runStep_sleep(step) {
		// sleep for the specified interval
		// step: { delay }
		if (!step.duration) throw new Error("Sleep: Missing duration (ms) to sleep for.");
		
		await sleep( step.duration );
	},
	
	async runStep_waitFor(step) {
		// wait for selectors to be visible
		// step: { selectors, state?, timeout? }
		var locator = this.buildLocatorFromStep(step);
		
		await locator.waitFor({
			state: step.state || 'visible',
			timeout: step.timeout || this.params.domTimeout
		});
	},
	
	/**
	 * Map a single raw Chrome selector string (e.g. "aria/Username")
	 * to a Playwright Locator.
	 */
	locatorFromSelector(rawSelector) {
		if (!rawSelector || typeof rawSelector !== "string") return null;
		let page = this.page;
		
		// Normalize 'pierce/' (Chrome's deep selector) by stripping the prefix.
		// We lose the shadow-boundary semantics, but in many apps it's still fine.
		if (rawSelector.startsWith("pierce/")) {
			rawSelector = rawSelector.slice("pierce/".length);
		}
		
		// 1) aria/ label → getByLabel (good for "Username", "Email Address", etc.)
		if (rawSelector.startsWith("aria/")) {
			const name = rawSelector.slice("aria/".length).trim();
			if (!name || name === "*") return null;
			return page.getByLabel(name);
		}
		
		// 2) text/ → getByText
		if (rawSelector.startsWith("text/")) {
			const text = rawSelector.slice("text/".length);
			// Chrome sometimes uses "text/*" as a wildcard; skip those
			if (!text || text === "*") return null;
			return page.getByText(text, { exact: false });
		}
		
		// 3) xpath/ or xpath// → locator('xpath=...')
		if (rawSelector.startsWith("xpath/")) {
			// Normalize xpath//... → //...
			const expr = rawSelector.replace(/^xpath\/+/, "//");
			return page.locator(`xpath=${expr}`);
		}
		
		// 4) explicit XPath looking selector (starts with // or (//)
		if (rawSelector.startsWith("//") || rawSelector.startsWith("(//")) {
			return page.locator(`xpath=${rawSelector}`);
		}
		
		// 5) Chrome CSS "pierce" selectors with >>>; Playwright uses >> for deep
		if (rawSelector.includes(">>>")) {
			const converted = rawSelector.replace(/>>>/g, ">>");
			return page.locator(converted);
		}
		
		// 6) catch-all: treat as CSS selector
		return page.locator(rawSelector);
	},

	/**
	 * Build a single Playwright Locator from a DevTools selector list:
	 *	 "selectors": [ ["aria/Email Address"], ["#LoginEmail"], ["xpath///*[@id=\"LoginEmail\"]"] ]
	 */
	buildLocatorFromStep(step) {
		if (!step.selectors || !Array.isArray(step.selectors)) {
			throw new Error(`Step of type '${step.type}' has no selectors`);
		}
		
		const locators = [];
		
		for (const selectorGroup of step.selectors) {
			if (selectorGroup.length === 0) continue;
			// DevTools uses an array of candidate strings per "group".
			// We’ll just take the first one in each group; FUTURE: get fancier here.
			const raw = Array.isArray(selectorGroup) ? selectorGroup[0] : selectorGroup;
			const loc = this.locatorFromSelector(raw);
			if (loc) locators.push(loc);
		}
		
		if (!locators.length) {
			throw new Error(`Could not build any locator for step type: ${step.type}`);
		}
		
		// Chain them with .or() so whichever resolves can be used.
		let combined = locators[0];
		for (let i = 1; i < locators.length; i++) {
			combined = combined.or(locators[i]);
		}
		
		// To avoid strict-mode multi-match errors, just take the first match
		return combined.first();
	},
	
	async archiveInferenceLog() {
		// if present, compress inference logs into archive in downloads dir
		if (!this.params || !this.params.ai_log_inference) return;
		if (!existsSync('inference_summary')) return;
		
		this.logVerbose( 
			execSync('/bin/tar zcf ./downloads/inference_summary.tar.gz ./inference_summary/*', { encoding: 'utf8' }) 
		);
	},
	
	async finish() {
		// finish up
		let params = this.params;
		
		// did we capture a video?
		let video_path = '';
		if (params.video != 'none') {
			video_path = await this.page.video().path();
		}
		
		// close things
		await this.context.close();
		await this.stagehand.close();
		
		// if user only wants video on error, delete it now
		if (video_path && (params.video != 'always')) {
			try { unlinkSync( video_path ); }
			catch (err) { this.logWarning(`Failed to delete video file: ` + err); }
		}
		
		// if user asked for logInferenceToFile, we need to tarball it up
		if (params.ai_log_inference) {
			await this.archiveInferenceLog();
		}
		
		console.log ( `✅ Completed all steps.` );
		
		// complete xyops job
		if (this.job.xy) console.log( JSON.stringify({ 
			xy: 1, 
			code: 0,
			description: 'Success',
			data: this.output, 
			files: [ 'downloads/*' ] 
		}) );
		
		// sanity exit after 1s (stagehand has trouble shutting down sometimes)
		var timer = setTimeout( function() { process.exit(0); }, 1000 );
		timer.unref();
	},
	
	logWarning(msg) {
		// only log if verbose mode is non-zero
		console.error(`🟠 Warning: ` + msg);
	},
	
	logVerbose(msg) {
		// only log if verbose mode is non-zero
		if (this.params.verbose) console.log(msg);
	}
	
}; // app

app.run().catch( async (err) => {
	// universal error catch
	console.error( `🛑 Error: ` + err, err );
	
	if (app.context) await app.context.close();
	if (app.stagehand) await app.stagehand.close();
	
	await app.archiveInferenceLog();
	
	if (app.job && app.job.xy) console.log( JSON.stringify({ 
		xy: 1, 
		code: 1, 
		description: '' + err,
		data: app.output, 
		files: [ 'downloads/*' ] 
	}) );
	
	process.exit(1);
});
```

## File: `package.json`
```json
{
	"name": "xyplug-stagehand",
	"type": "module",
	"version": "1.0.18",
	"private": true,
	"description": "A Stagehand Plugin for use in the xyOps workflow automation system.",
	"author": "Joseph Huckaby <jhuckaby@pixlcore.com>",
	"homepage": "https://github.com/pixlcore/xyplug-stagehand",
	"license": "MIT",
	"main": "index.js",
	"repository": {
		"type": "git",
		"url": "https://github.com/pixlcore/xyplug-stagehand"
	},
	"bugs": {
		"url": "https://github.com/pixlcore/xyplug-stagehand/issues"
	},
	"keywords": [
		"xyops",
		"stagehand",
		"playwright",
		"chromium"
	],
	"dependencies": {
		"@browserbasehq/stagehand": "3.0.3",
		"playwright-core": "1.56.1"
	}
}
```

## File: `xyops.json`
```json
{
	"type": "xypdf",
	"description": "xyOps Portable Data Object",
	"version": "1.0",
	"items": [
		{
			"type": "plugin",
			"data": {
				"id": "pmikpt744ub",
				"title": "Stagehand",
				"enabled": true,
				"type": "event",
				"command": "docker run -i --rm --init --ipc=host --name \"xyplug-stagehand-{{id}}\" ghcr.io/pixlcore/xyplug-stagehand:v1.0.18",
				"script": "",
				"groups": [],
				"format": "",
				"params": [
					{
						"id": "ai_model_name",
						"title": "AI Model Name",
						"type": "text",
						"caption": "Enter the AI provider and model name, separated by a slash.",
						"locked": false,
						"value": "google/gemini-2.5-flash",
						"variant": "text",
						"required": false
					},
					{
						"id": "ai_base_url",
						"title": "AI Base URL",
						"type": "text",
						"caption": "If using a custom endpoint for AI inference (e.g. Ollama), enter the URL here.",
						"locked": false,
						"value": "",
						"variant": "text",
						"required": false
					},
					{
						"id": "ai_log_inference",
						"title": "Log AI Inference",
						"type": "checkbox",
						"caption": "Optionally capture and attach all the AI inference summary logs (for debugging).",
						"locked": false,
						"value": false
					},
					{ 
						"id": "ssl_cert_bypass", 
						"type": "checkbox", 
						"title": "SSL Certificate Bypass", 
						"caption": "Optionally bypass SSL / TLS certificate validation when visiting websites.",
						"value": false
					},
					{
						"id": "width",
						"title": "Width",
						"type": "text",
						"caption": "Enter the desired browser window width in pixels.",
						"locked": false,
						"value": 1280,
						"variant": "number",
						"required": true
					},
					{
						"id": "height",
						"title": "Height",
						"type": "text",
						"caption": "Enter the desired browser window height in pixels.",
						"locked": false,
						"value": 720,
						"variant": "number",
						"required": true
					},
					{
						"id": "video",
						"title": "Capture Video",
						"type": "select",
						"caption": "Choose whether to capture and attach a video of the browser session always, only on error, or never.",
						"locked": false,
						"value": "Always, Error, None"
					},
					{
						"id": "verbose",
						"title": "Verbosity Level",
						"type": "select",
						"caption": "Select the verbosity level of the job output.  0 is quietest, 2 is loudest.\n",
						"locked": false,
						"value": "0, 1, 2"
					},
					{
						"id": "aiTimeout",
						"title": "AI Timeout",
						"type": "text",
						"caption": "Number of milliseconds to wait for AI to run an action.",
						"locked": false,
						"value": 60000,
						"variant": "number",
						"required": true
					},
					{
						"id": "domTimeout",
						"title": "DOM Timeout",
						"type": "text",
						"caption": "Number of milliseconds to wait for DOM selectors to locate their targets.",
						"locked": false,
						"value": 3000,
						"variant": "number",
						"required": true
					},
					{
						"id": "navTimeout",
						"title": "Navigation Timeout",
						"type": "text",
						"caption": "Number of milliseconds to wait for navigation events (page loads).",
						"locked": false,
						"value": 30000,
						"variant": "number",
						"required": true
					},
					{
						"id": "stepDelay",
						"title": "Step Delay",
						"type": "text",
						"caption": "Number of milliseconds to wait between steps, to help ensure stability.",
						"locked": false,
						"value": 1000,
						"variant": "number",
						"required": true
					},
					{
						"id": "script",
						"title": "Script",
						"type": "code",
						"caption": "Enter your list of instructions for the browser to perform, one per line.  It can be plain text or JSON.  See [xyplug-stagehand](https://github.com/pixlcore/xyplug-stagehand) for details.",
						"locked": false,
						"value": "Navigate to https://mycompany.com/\nType \"foo\" into the Username text field.\nType \"bar\" into the Password text field.\nClick the \"Login\" button.\nSleep for 3000",
						"required": true
					}
				],
				"kill": "parent",
				"notes": "A Stagehand event plugin for the xyOps Workflow Automation System. This package provides an AI-powered browser automation framework for xyOps.  Using it you can drive a headless browser with simple English instructions, take actions, extract data, capture network requests, and even record a video of the whole session.",
				"icon": "hand-back-right-outline",
				"uid": "",
				"gid": "",
				"runner": true
			}
		}
	]
}
```

