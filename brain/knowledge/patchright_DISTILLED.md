---
id: patchright
type: knowledge
owner: OA_Triage
---
# patchright
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "scripts": {
        "patch": "tsx patchright_driver_patch.ts",
        "typecheck": "tsc --noEmit",
        "format:check": "bash -c 'biome check --line-width=320 --formatter-enabled=false --diagnostic-level=error ${@:-patchright_driver_patch.ts driver_patches/}' --",
        "format:fix": "tsx utils/format-indentation.ts",
        "format": "bash -c 'npm run format:fix -- ${@} && npm run format:check -- ${@}' --"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.10",
        "@types/node": "^25.5.0",
        "glob": "^13.0.6",
        "prettier": "^3.0.0",
        "ts-morph": "^27.0.2",
        "tsx": "^4.21.0",
        "typescript": "^6.0.2",
        "yaml": "^2.7.0"
    },
    "type": "module"
}

```

### File: README.md
```md
<h1 align="center">
    🎭 Patchright
</h1>


<p align="center">
    <a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/License-Apache%202.0-green">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Based%20on-Playwright-goldenrod">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Driver-Patched-blue">
    </a>
    <a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright/releases/latest">
        <img alt="Patchright Version" src="https://img.shields.io/github/v/release/Kaliiiiiiiiii-Vinyzu/patchright?display_name=release&label=Version">
    </a>
<br/>
    <a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python">
        <img src="https://img.shields.io/badge/Package-Python-seagreen">
    </a>
    <a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python/releases">
        <img alt="Python Downloads" src="https://img.shields.io/pepy/dt/patchright?color=red&label=Python%20Downloads">
    </a>
    <a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-nodejs">
        <img src="https://img.shields.io/badge/Package-NodeJS-seagreen">
    </a>
    <a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-nodejs/releases">
        <img alt="NodeJS Downloads" src="https://img.shields.io/npm/d18m/patchright?color=red&label=NodeJS%20Downloads">
    </a>
    <a href="https://github.com/DevEnterpriseSoftware/patchright-dotnet">
        <img src="https://img.shields.io/badge/Package-.Net-seagreen">
    </a>
    <a href="https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-nodejs/releases">
        <img alt=".Net Downloads" src="https://img.shields.io/nuget/dt/Patchright?label=.Net%20Downloads">
    </a>
<br/>
    <img src="https://img.shields.io/github/actions/workflow/status/Kaliiiiiiiiii-Vinyzu/patchright/patchright_tests.yml?label=Patchright%20Driver%20Tests">
    <img src="https://img.shields.io/github/actions/workflow/status/Kaliiiiiiiiii-Vinyzu/patchright-python/patchright_tests.yml?label=Patchright%20Python%20Tests">
    <img src="https://img.shields.io/github/actions/workflow/status/DevEnterpriseSoftware/patchright-dotnet/patchright_test.yml?label=Patchright%20.Net%20Tests">
</p>

#### Patchright is a patched and undetected version of the Playwright Testing and Automation Framework. </br> It can be used as a drop-in replacement for Playwright.

> [!NOTE]  
> This repository serves the Patchright Driver. To use Patchright, check out the [Python Package](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python), the [NodeJS Package](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-nodejs) or the _community-driven_ [.Net Package](https://github.com/DevEnterpriseSoftware/patchright-dotnet/)

> [!IMPORTANT]  
> Patchright only patches CHROMIUM based browsers. Firefox and Webkit are not supported.

---

<details open>
    <summary><h3>Sponsors</h1></summary>

<sup>Want to Sponsor this Project? [Contact Me](https://discordapp.com/users/935224495126487150)!</sup>

</br>

<img width="500" alt="proxylayer" src="https://github.com/user-attachments/assets/d1c5f849-5cb0-4aff-b48c-530bda2ee03f" />

Running Patchright? Your proxy layer can decide whether you scale — or get blocked.

#### [ProxyEmpire](https://proxyempire.io/?ref=patchright&utm_source=patchright) delivers:

- 🌍 30M+ Residential IPs (170+ countries)
- 📱 4G/5G Mobile Proxies
- 🔄 Rotating & Sticky Sessions + Unlimited Concurrent Sessions
- 🎯 Precise geo-targeting
- HTTP, HTTPS & SOCKS5 Support

<sup>Built for scraping, automation, and high-stealth workflows.</sup>

<span style="font-size:3em;"> 🔥 **Special Offer**: Use code **Patchright30** to get **30% recurring discount** (not just first month). </span>

<sup>Upgrade your proxies. Reduce bans. Scale properly.</sup>

</details>

---

## Patches

### [Runtime.enable](https://vanilla.aslushnikov.com/?Runtime.enable) Leak
This is the biggest Patch Patchright uses. To avoid detection by this leak, patchright avoids using [Runtime.enable](https://vanilla.aslushnikov.com/?Runtime.enable) by executing Javascript in (isolated) ExecutionContexts.

### [Console.enable](https://vanilla.aslushnikov.com/?Console.enable) Leak
Patchright patches this leak by disabling the Console API all together. This means, console functionality will not work in Patchright. If you really need the console, you might be better off using Javascript loggers, although they also can be easily detected.

### Command Flags Leaks
Patchright tweaks the Playwright Default Args to avoid detection by Command Flag Leaks. This (most importantly) affects:
- `--disable-blink-features=AutomationControlled` (added) to avoid navigator.webdriver detection.
- `--enable-automation` (removed) to avoid navigator.webdriver detection.
- `--disable-popup-blocking` (removed) to avoid popup crashing.
- `--disable-component-update` (removed) to avoid detection as a Stealth Driver.
- `--disable-default-apps` (removed) to enable default apps.
- `--disable-extensions` (removed) to enable extensions

### General Leaks
Patchright patches some general leaks in the Playwright codebase. This mainly includes poor setups and obvious detection points.

### Closed Shadow Roots
Patchright is able to interact with elements in Closed Shadow Roots. Just use normal locators and Patchright will do the rest.
<br/>
Patchright is now also able to use XPaths in Closed Shadow Roots.

---

## Stealth

With the right setup, Patchright currently is considered undetectable.
Patchright passes:
- [Brotector](https://kaliiiiiiiiii.github.io/brotector/) ✅ (with [CDP-Patches](https://github.com/Kaliiiiiiiiii-Vinyzu/CDP-Patches/))
- [Cloudflare](https://cloudflare.com/) ✅
- [Kasada](https://www.kasada.io/) ✅
- [Akamai](https://www.akamai.com/products/bot-manager/) ✅
- [Shape/F5](https://www.f5.com/) ✅
- [Bet365](https://bet365.com/) ✅
- [Datadome](https://datadome.co/products/bot-protection/) ✅
- [Fingerprint.com](https://fingerprint.com/products/bot-detection/) ✅
- [CreepJS](https://abrahamjuliot.github.io/creepjs/) ✅
- [Sannysoft](https://bot.sannysoft.com/) ✅
- [Incolumitas](https://bot.incolumitas.com/) ✅
- [IPHey](https://iphey.com/) ✅
- [Browserscan](https://browserscan.net/) ✅
- [Pixelscan](https://pixelscan.net/) ✅

---

## Bugs
#### Even though we have spent a lot of time to make Patchright as stable as possible, bugs may still occur. If you encounter any bugs, please report them in the [Issues](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright/issues).
#### Patchright is now tested against the Playwright Tests after every release. See [here](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python/actions/workflows/patchright_tests.yml)

> [!WARNING]  
> Patchright passes most, but not all the Playwright tests. Some bugs are considered impossible to solve, some are just not relevant. See the list of bugs and their explanation [here](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright/issues/30).

#### Based on the Playwright Tests, we concluded that its highly unlikely that you will be affected by these bugs in regular usecases.

<details>
    <summary><b>Init Script Shenanigans</b></summary>

### Explanation
To be able to use InitScripts without [Runtime.enable](https://vanilla.aslushnikov.com/?Runtime.enable), Patchright uses Playwright Routes to inject JavaScript into HTML requests.

### Bugs
Playwright Routes may cause some bugs in other parts of your code. Patchright InitScripts won't cause any bugs that wouldn't be caused by normal Playwright Routes. </br> If you want any of these bugs fixed, you'll have to contact the Playwright team.

### Leaks
Patchright InitScripts can be detected by Timing Attacks. However, no antibot currently checks for this kind of Timing Attack and they probably won't for a good amount of time. </br> We consider them not to be a big risk of detection.

</details>

---

### TODO
- [x] Implement Option to choose Execution Context (Main/Isolated).
- [x] Fix Fixable Bugs.
- [x] Implement .patch Updater to easily show Patchright's patches.
- [x] Setup Automated Testing on new Release.
- [x] Implement Patchright on .NET.
- [ ] Implement Patchright on Java.

---

## Development

Deployment of new Patchright versions are automatic, but bugs due to Playwright codebase changes may occur. Fixes for these bugs might take a few days to be released. 

---

## Support our work

If you choose to support our work, please contact [@vinyzu](https://discord.com/users/935224495126487150) or [@steve_abcdef](https://discord.com/users/936292409426477066) on Discord.

---

## Copyright and License
© [Vinyzu](https://github.com/Vinyzu/)

Patchright is licensed [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)

[Some Parts](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright/blob/10c5a090e9a1dcd2107c253d65b3d8b27d0670a9/driver_patches/framesPatch.ts#L156-L171) of the Codebase are inspired by [Driverless](https://github.com/kaliiiiiiiiii/Selenium-Driverless).
Thanks to [Nick Webson](https://github.com/rebrowser/rebrowser-patches) for the idea of .patch-File Documentation.

---

## Disclaimer

This repository is provided for **educational purposes only**. \
No warranties are provided regarding accuracy, completeness, or suitability for any purpose. **Use at your own risk**—the authors and maintainers assume **no liability** for **any damages**, **legal issues**, or **warranty breaches** resulting from use, modification, or distribution of this code.\
**Any misuse or legal violations are the sole responsibility of the user**. 

---

## Authors

#### Active Maintainer: [Vinyzu](https://github.com/Vinyzu/) </br> Co-Maintainer: [Kaliiiiiiiiii](https://github.com/kaliiiiiiiiii/)

```

### File: modify_tests.js
```js
import fs from 'node:fs';
import path from 'node:path';
import { Project, Node, SyntaxKind } from 'ts-morph';

const repoRoot = process.cwd();
const playwrightRoot = path.join(repoRoot, 'playwright');
const testsRoot = path.join(playwrightRoot, 'tests');
const tsConfigPath = path.join(testsRoot, 'tsconfig.json');
const dryRun = process.env.MODIFY_TESTS_DRY_RUN === '1';

if (!fs.existsSync(playwrightRoot)) {
	console.error('[modify_tests] Missing playwright directory at', playwrightRoot);
	process.exit(1);
}
if (!fs.existsSync(tsConfigPath)) {
	console.error('[modify_tests] Missing tests tsconfig at', tsConfigPath);
	process.exit(1);
}

const TARGET_METHODS = new Set(['evaluate', 'evaluateHandle', 'evaluateAll']);

// Patchright limitation: init scripts don't run on about:blank/data: URLs.
// Keep this surgical and simple: rewrite only the known failing upstream tests.
function applyPatchrightWorkarounds(sourceFile, relativePath) {
	let text = sourceFile.getFullText();
	const original = text;

	const missingReplacements = [];
	const replaceAll = (from, to) => {
		if (text.includes(from))
			text = text.split(from).join(to);
	};
	const replaceOnce = (from, to) => {
		if (text.includes(from)) {
			text = text.replace(from, to);
			return true;
		}
		missingReplacements.push({ relativePath, from });
		return false;
	};

	if (relativePath === 'tests/library/browsercontext-add-init-script.spec.ts') {
		replaceOnce(
			"it('should work without navigation, after all bindings', async ({ context }) => {",
			"it('should work without navigation, after all bindings', async ({ context, server }) => {"
		);
		replaceOnce(
			"it('should work without navigation in popup', async ({ context }) => {",
			"it('should work without navigation in popup', async ({ context, server }) => {"
		);
		replaceOnce(
			"it('init script should run only once in popup', async ({ context }) => {",
			"it('init script should run only once in popup', async ({ context, server }) => {"
		);

		replaceOnce(
			"  const page = await context.newPage();\n\n  expect(await page.evaluate(() => (window as any)['temp'], undefined, false)).toBe(123);",
			"  const page = await context.newPage();\n  await page.goto(server.EMPTY_PAGE);\n\n  expect(await page.evaluate(() => (window as any)['temp'], undefined, false)).toBe(123);"
		);

		// In Patchright, bindings might not be available at document start; don't throw before setting temp.
		replaceOnce(
			"  await context.addInitScript(() => {\n    (window as any)['woof']('hey');\n    (window as any)['temp'] = 123;\n  });",
			"  await context.addInitScript(() => {\n    const retry = () => {\n      const fn = (window as any)['woof'];\n      if (typeof fn === 'function') fn('hey');\n      else setTimeout(retry, 0);\n    };\n    retry();\n    (window as any)['temp'] = 123;\n  });"
		);

		replaceOnce(
			"  const page = await context.newPage();\n  const [popup] = await Promise.all([",
			"  const page = await context.newPage();\n  await page.goto(server.EMPTY_PAGE);\n  const [popup] = await Promise.all(["
		);
		replaceOnce(
			"    page.evaluate(() => (window as any)['win'] = window.open(), undefined, false),",
			"    page.evaluate(url => (window as any)['win'] = window.open(url), server.EMPTY_PAGE, false),"
		);
		replaceOnce(
			"  ]);\n  expect(await popup.evaluate(() => (window as any)['temp'], undefined, false)).toBe(123);",
			"  ]);\n  await popup.waitForLoadState();\n  expect(await popup.evaluate(() => (window as any)['temp'], undefined, false)).toBe(123);"
		);

		replaceOnce(
			"    page.evaluate(() => window.open('about:blank'), undefined, false),",
			"    page.evaluate(url => window.open(url), server.EMPTY_PAGE, false),"
		);
		replaceOnce(
			"  ]);\n  expect(await popup.evaluate('callCount', undefined, false)).toEqual(1);",
			"  ]);\n  await popup.waitForLoadState();\n  expect(await popup.evaluate('callCount', undefined, false)).toEqual(1);"
		);
	}

	if (relativePath === 'tests/library/page-clock.spec.ts') {
		replaceAll("await page.goto('data:text/html,');", 'await page.goto(server.EMPTY_PAGE);');
		replaceAll(
			"page.evaluate(() => window.open('about:blank'), undefined, false),",
			"page.evaluate(url => window.open(url), server.EMPTY_PAGE, false),"
		);
		replaceAll(
			"]);\n    const popupTime = await popup.evaluate(() => Date.now(), undefined, false);",
			"]);\n    await popup.waitForLoadState();\n    const popupTime = await popup.evaluate(() => Date.now(), undefined, false);"
		);

		// Ensure tests in this file that now use server have it in fixtures.
		text = text.replace(/async \(\{([^}]*)\}\) => \{/g, (match, inside) => {
			if (!inside.includes('page') || inside.includes('server'))
				return match;
			const next = inside.trim().length ? `${inside.trim()}, server` : 'server';
			return `async ({ ${next} }) => {`;
		});

		replaceOnce(
			"const waitForDone = page.waitForEvent('console', msg => msg.text() === 'done');",
			"const waitForDone = page.waitForFunction(() => (window as any).__pw_done);"
		);
		replaceOnce(
			"console.log('done');",
			"window.__pw_done = true; console.log('done');"
		);
	}

	if (relativePath === 'tests/library/emulation-focus.spec.ts') {
		// Patchright's modify_tests.js only adds isolatedContext=false to evaluate calls with
		// inline arrow/function expressions. These tests pass function references (identifiers)
		// like evaluate(clickCounter) which are skipped by the safety check. Add the main-world
		// flag so window/self properties are visible to subsequent reads.

		// Test: should not affect mouse event target page
		replaceOnce(
			"page.evaluate(clickCounter),\n    page2.evaluate(clickCounter),",
			"page.evaluate(clickCounter, undefined, false),\n    page2.evaluate(clickCounter, undefined, false),"
		);

		// Test: should change focused iframe
		replaceOnce(
			"frame1.evaluate(logger),\n    frame2.evaluate(logger),",
			"frame1.evaluate(logger, undefined, false),\n    frame2.evaluate(logger, undefined, false),"
		);
	}

	if (relativePath === 'tests/library/hit-target.spec.ts') {
		// Patchright runs $eval in the utility/isolated world. These tests set window properties
		// from $eval callbacks, then read them from the main world via evaluate(..., false).
		// Convert $eval('button', ...) to evaluate(() => { querySelector + ... }, undefined, false).

		// Test: should block click when mousedown fails
		replaceOnce(
			"await page.$eval('button', button => {\n    button.addEventListener('mousemove', () => {\n      button.style.marginLeft = '100px';\n    });\n\n    const allEvents = [];\n    (window as any).allEvents = allEvents;\n    for (const name of ['mousemove', 'mousedown', 'mouseup', 'click', 'dblclick', 'auxclick', 'contextmenu', 'pointerdown', 'pointerup'])\n      button.addEventListener(name, e => allEvents.push(e.type));\n  });",
			"await page.evaluate(() => {\n    const button = document.querySelector('button')!;\n    button.addEventListener('mousemove', () => {\n      button.style.marginLeft = '100px';\n    });\n\n    const allEvents = [];\n    (window as any).allEvents = allEvents;\n    for (const name of ['mousemove', 'mousedown', 'mouseup', 'click', 'dblclick', 'auxclick', 'contextmenu', 'pointerdown', 'pointerup'])\n      button.addEventListener(name, e => allEvents.push(e.type));\n  }, undefined, false);"
		);

		// Test: should click when element detaches in mousedown
		replaceOnce(
			"await page.$eval('button', button => {\n    button.addEventListener('mousedown', () => {\n      (window as any).result = 'Mousedown';\n      button.remove();\n    });\n  });",
			"await page.evaluate(() => {\n    const button = document.querySelector('button')!;\n    button.addEventListener('mousedown', () => {\n      (window as any).result = 'Mousedown';\n      button.remove();\n    });\n  }, undefined, false);"
		);

		// Test: should block all events when hit target is wrong and element detaches
		replaceOnce(
			"await page.$eval('button', button => {\n    const blocker = document.createElement('div');",
			"await page.evaluate(() => {\n    const button = document.querySelector('button')!;\n    const blocker = document.createElement('div');"
		);
		replaceOnce(
			"      blocker.addEventListener(name, e => allEvents.push(e.type));\n    }\n  });",
			"      blocker.addEventListener(name, e => allEvents.push(e.type));\n    }\n  }, undefined, false);"
		);

		// Test: should not block programmatic events
		replaceOnce(
			"await page.$eval('button', button => {\n    button.addEventListener('mousemove', () => {\n      button.style.marginLeft = '100px';\n      button.dispatchEvent(new MouseEvent('click'));\n    });\n\n    const allEvents = [];\n    (window as any).allEvents = allEvents;\n    button.addEventListener('click', e => {\n      if (!e.isTrusted)\n        allEvents.push(e.type);\n    });\n  });",
			"await page.evaluate(() => {\n    const button = document.querySelector('button')!;\n    button.addEventListener('mousemove', () => {\n      button.style.marginLeft = '100px';\n      button.dispatchEvent(new MouseEvent('click'));\n    });\n\n    const allEvents = [];\n    (window as any).allEvents = allEvents;\n    button.addEventListener('click', e => {\n      if (!e.isTrusted)\n        allEvents.push(e.type);\n    });\n  }, undefined, false);"
		);
	}

	if (relativePath === 'tests/library/popup.spec.ts') {
		replaceOnce(
			"  const injected = await page.evaluate(() => {\n    const win = window.open('about:blank');\n    return win['injected'];\n  }, undefined, false);",
			"  const injected = await page.evaluate(async url => {\n    const win = window.open(url);\n    await new Promise(f => win.onload = f);\n    return win['injected'];\n  }, server.EMPTY_PAGE, false);"
		);
		replaceOnce(
			"  await Promise.all([\n    page.waitForEvent('popup'),\n    page.evaluate(async () => {\n      const win = window.open('about:blank');\n      win['add'](9, 4);\n      win.close();\n    }, undefined, false),\n  ]);",
			"  const [popup] = await Promise.all([\n    page.waitForEvent('popup'),\n    page.evaluate(url => window.open(url), server.EMPTY_PAGE, false),\n  ]);\n  await popup.waitForLoadState();\n  await Promise.all([\n    popup.waitForEvent('close'),\n    popup.evaluate(() => { window['add'](9, 4); window.close(); }, undefined, false),\n  ]);"
		);
	}

	if (missingReplacements.length) {
		console.error(`[modify_tests] Failed to apply expected modifications for ${relativePath}`);
		for (const { from } of missingReplacements)
			console.error(`  - Missing replacement: ${from}`);
		if (!dryRun)
			console.error(`[modify_tests] Continuing despite ${missingReplacements.length} missing replacement(s) due to upstream test drift.`);
	}

	if (text !== original) {
		sourceFile.replaceWithText(text);
		return true;
	}
	return false;
}

const FIXME_TARGETS = {
	'tests/page/page-basic.spec.ts': new Map([
		['has navigator.webdriver set to true', 'Patchright intentionally disables automation fingerprinting.'],
		['page.press should work for Enter', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
	]),
	'tests/page/page-network-response.spec.ts': new Map([
		['should report if request was fromServiceWorker', 'Patchright routing/injection changes service-worker attribution semantics.'],
	]),
	'tests/page/page-event-request.spec.ts': new Map([
		['should report requests and responses handled by service worker', 'Patchright routing/injection changes service-worker attribution semantics.'],
		['should report requests and responses handled by service worker with routing', 'Patchright routing/injection changes service-worker attribution semantics.'],
		['should report navigation requests and responses handled by service worker', 'Patchright routing/injection changes service-worker attribution semantics.'],
		['should report navigation requests and responses handled by service worker with routing', 'Patchright routing/injection changes service-worker attribution semantics.'],
	]),
	'tests/page/interception.spec.ts': new Map([
		['should intercept after a service worker', 'Patchright routing order differs after service-worker interception.'],
		['should intercept network activity from worker', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['should intercept worker requests when enabled after worker creation', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['should intercept network activity from worker 2', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
	]),
	'tests/page/jshandle-to-string.spec.ts': new Map([
		['should beautifully render sparse arrays', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
	]),
	'tests/page/page-click.spec.ts': new Map([
		['should click offscreen buttons', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['ensure events are dispatched in the individual tasks', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
	]),
	'tests/page/page-history.spec.ts': new Map([
		['page.goBack should work for file urls', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['regression test for issue 20791', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
	]),
	'tests/page/page-listeners.spec.ts': new Map([
		['should not throw with ignoreErrors', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['should wait', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['wait should throw', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
	]),
	'tests/page/page-screenshot.spec.ts': new Map([
		['should trigger particular events for css transitions', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['should trigger particular events for INfinite css animation', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['should trigger particular events for finite css animation', 'Known Patchright bug: Console CDP domain is disabled, so console events/messages are not reliably available.'],
		['should wait for fonts to load', 'Known Patchright divergence: page.screenshot does not reliably block on webfonts, so the expected timeout/message is not deterministic.'],
	]),
	'tests/page/page-wait-for-function.spec.ts': new Map([
		['should work when resolved right before execution co
... [TRUNCATED]
```

### File: patchright_driver_patch.ts
```ts
import fs from "node:fs/promises";
import { IndentationText, Project } from "ts-morph";
import YAML from "yaml";

import * as patches from "./driver_patches/index.ts";

const project = new Project({
	manipulationSettings: {
		indentationText: IndentationText.TwoSpaces,
	},
});

// patchright-driver-patch: start
// NOTE: Workflows append everything after this marker into patchright-nodejs patch script.

// ------------------------
// server/browserContext.ts
// ------------------------
patches.patchBrowserContext(project);

// ---------------------------
// server/chromium/chromium.ts
// ---------------------------
patches.patchChromium(project);

// -----------------------------------
// server/chromium/chromiumSwitches.ts
// -----------------------------------
patches.patchChromiumSwitches(project);

// ----------------------------
// server/chromium/crBrowser.ts
// ----------------------------
patches.patchCRBrowser(project);

// -----------------------------
// server/chromium/crDevTools.ts
// -----------------------------
patches.patchCRDevTools(project);

// -----------------------------------
// server/chromium/crNetworkManager.ts
// -----------------------------------
patches.patchCRNetworkManager(project);

// -----------------------------
// server/chromium/crCoverage.ts
// -----------------------------
patches.patchCRCoverage(project);

// ----------------------------------
// server/chromium/crServiceWorker.ts
// ----------------------------------
patches.patchCRServiceWorker(project);

// ----------------
// server/frames.ts
// ----------------
patches.patchFrames(project);

// -------------------------
// server/frameSelectors.ts
// -------------------------
patches.patchFrameSelectors(project);

// -------------------------
// server/chromium/crPage.ts
// -------------------------
patches.patchCRPage(project);

// --------------
// server/page.ts
// --------------
patches.patchPage(project);

// ---------------------------
// server/utils/expectUtils.ts
// ---------------------------
patches.patchExpectUtils(project);

// ---------------------------------------------
// utils/isomorphic/utilityScriptSerializers.ts
// --------------------------------------------
patches.patchUtilityScriptSerializers(project);

// ---------------------
// server/pageBinding.ts
// ---------------------
patches.patchPageBinding(project);

// ---------------
// server/clock.ts
// --------------
patches.patchClock(project);

// ----------------------
// Patchright CLI Aliases
// ----------------------
patches.patchCliAlias(project);

// --------------------
// server/javascript.ts
// --------------------
patches.patchJavascript(project);

// -------------------
// server/launchApp.ts
// -------------------
patches.patchLaunchApp(project);

// -------------------------------------
// server/dispatchers/frameDispatcher.ts
// -------------------------------------
patches.patchFrameDispatcher(project);

// ----------------------------------------------
// server/dispatchers/browserContextDispatcher.ts
// ----------------------------------------------
patches.patchBrowserContextDispatcher(project);

// ----------------------------------------
// server/dispatchers/jsHandleDispatcher.ts
// ----------------------------------------
patches.patchJSHandleDispatcher(project);

// ------------------------------------
// server/dispatchers/pageDispatcher.ts
// ------------------------------------
patches.patchPageDispatcher(project);

// -----------------------------------
// injected/src/xpathSelectorEngine.ts
// -----------------------------------
patches.patchXPathSelectorEngine(project);

// -------------------------
// recorder/src/recorder.tsx
// -------------------------
patches.patchRecorder(project);

// -----------------------
// server/screenshotter.ts
// -----------------------
patches.patchScreenshotter(project);

// ------------------------------------
// server/trace/recorder/snapshotter.ts
// ------------------------------------
patches.patchSnapshotter(project);

// --------------------------------------------
// server/trace/recorder/snapshotterInjected.ts
// --------------------------------------------
patches.patchSnapshotterInjected(project);

// --------------------------------
// server/trace/recorder/tracing.ts
// --------------------------------
patches.patchTracing(project);

// -------------------------
// protocol/protocol.yml
// -------------------------
const protocol = YAML.parse(await fs.readFile("packages/protocol/src/protocol.yml", "utf8"));

// isolatedContext parameters
for (const type of ["Frame", "JSHandle", "Worker"]) {
	const commands = protocol[type].commands;
	commands.evaluateExpression.parameters.isolatedContext = "boolean?";
	commands.evaluateExpressionHandle.parameters.isolatedContext = "boolean?";
}
protocol.Frame.commands.evalOnSelectorAll.parameters.isolatedContext = "boolean?";

// focusControl parameter
protocol.ContextOptions.properties.focusControl = "boolean?";

await fs.writeFile("packages/protocol/src/protocol.yml", YAML.stringify(protocol));

// Save the changes without reformatting
project.saveSync();

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "allowImportingTsExtensions": true,
    "allowJs": true,
    "checkJs": false,
    "verbatimModuleSyntax": true,
    "strict": true,
    "skipLibCheck": true,
    "noEmit": true
  },
  "include": [
    "patchright_driver_patch.ts",
    "driver_patches/**/*.ts",
    "driver_patches/**/*.js",
    "utils/**/*.ts"
  ]
}
```

### File: utils\check_patch_impact.ts
```ts
import fs from "node:fs/promises";
import path from "node:path";
import YAML from "yaml";
import { Project, ScriptKind, SyntaxKind, type Node } from "ts-morph";
import { extractPatchedSymbols, type PatchedSymbolKind, type PatchedSymbolRecord } from "./extract_patched_symbols.ts";

type ChangeType = "signature_changed" | "body_changed" | "symbol_removed" | "symbol_added" | "unchanged";

type SymbolImpactRow = PatchedSymbolRecord & {
  changeType: ChangeType;
  diffLine: number | null;
  diffSide: "L" | "R" | null;
  diffSnippet: string;
};

type CompareApiFile = {
  filename: string;
  status?: string;
  patch?: string;
};

type ParsedArgs = {
  oldVersion: string;
  newVersion: string;
  reportPath: string;
  summaryPath: string;
  diffPath: string;
};

type DiffParsedLine = {
  raw: string;
  side: "L" | "R" | "C";
  oldLine: number | null;
  newLine: number | null;
};

type DiffHunk = {
  lines: DiffParsedLine[];
};

type ParsedPatch = {
  hunks: DiffHunk[];
  additions: Array<{ line: number; text: string }>;
  deletions: Array<{ line: number; text: string }>;
};

const RELEVANT_PATH_PREFIXES = [
  "packages/playwright-core/src/server/",
  "packages/playwright-core/src/utils/isomorphic/",
  "packages/playwright-core/src/injected/src/",
  "packages/injected/src/",
  "packages/playwright-core/src/server/dispatchers/",
  "packages/playwright-core/src/recorder/src/",
  "packages/recorder/src/",
  "packages/protocol/src/",
];

function parseArgs(argv: string[]): ParsedArgs {
  const args: ParsedArgs = {
    oldVersion: "",
    newVersion: "",
    reportPath: "report.json",
    summaryPath: "step_summary.md",
    diffPath: "affected_diff.patch",
  };

  for (let i = 2; i < argv.length; i += 1) {
    const arg = argv[i];
    const value = argv[i + 1];
    if (!value) continue;

    if (arg === "--old-version") {
      args.oldVersion = value;
      i += 1;
      continue;
    }
    if (arg === "--new-version") {
      args.newVersion = value;
      i += 1;
      continue;
    }
    if (arg === "--report") {
      args.reportPath = value;
      i += 1;
      continue;
    }
    if (arg === "--summary") {
      args.summaryPath = value;
      i += 1;
      continue;
    }
    if (arg === "--diff") {
      args.diffPath = value;
      i += 1;
      continue;
    }
  }

  if (!args.oldVersion || !args.newVersion) {
    throw new Error("Both --old-version and --new-version are required");
  }

  return args;
}

function normalizeVersion(version: string): string {
  return version.startsWith("v") ? version.slice(1) : version;
}

function toTag(version: string): string {
  return version.startsWith("v") ? version : `v${version}`;
}

function isRelevantPath(filePath: string): boolean {
  return RELEVANT_PATH_PREFIXES.some((prefix) => filePath.startsWith(prefix));
}

function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function escapeUnderscore(value: string): string {
  return value.replaceAll("_", "\\_");
}

function colorTextToken(value: string, color: string): string {
  return `\${\\color{${color}}\\text{${escapeUnderscore(value)}}}$`;
}

function changeTypeColor(changeType: ChangeType): string {
  if (changeType === "signature_changed") return "brown";
  if (changeType === "symbol_removed") return "brown";
  if (changeType === "symbol_added") return "orange";
  return "orange";
}

function kindColor(kind: PatchedSymbolKind): string {
  return kind === "class" ? "green" : "lime";
}

function getDeclSignatureText(node: Node): string {
  if (node.getKind() === SyntaxKind.FunctionDeclaration) {
    const functionNode = node.asKindOrThrow(SyntaxKind.FunctionDeclaration);
    const name = functionNode.getName() ?? "";
    const params = functionNode.getParameters().map((param) => {
      const rest = param.isRestParameter() ? "..." : "";
      const typeNode = param.getTypeNode();
      const type = typeNode ? `: ${typeNode.getText()}` : "";
      const optional = param.isOptional() ? "?" : "";
      return `${rest}${param.getName()}${optional}${type}`;
    });
    const returnTypeNode = functionNode.getReturnTypeNode();
    const returnType = returnTypeNode ? `: ${returnTypeNode.getText()}` : "";
    return `${name}(${params.join(",")})${returnType}`;
  }

  if (node.getKind() === SyntaxKind.MethodDeclaration) {
    const methodNode = node.asKindOrThrow(SyntaxKind.MethodDeclaration);
    const name = methodNode.getName() ?? "";
    const params = methodNode.getParameters().map((param) => {
      const rest = param.isRestParameter() ? "..." : "";
      const typeNode = param.getTypeNode();
      const type = typeNode ? `: ${typeNode.getText()}` : "";
      const optional = param.isOptional() ? "?" : "";
      return `${rest}${param.getName()}${optional}${type}`;
    });
    const returnTypeNode = methodNode.getReturnTypeNode();
    const returnType = returnTypeNode ? `: ${returnTypeNode.getText()}` : "";
    return `${name}(${params.join(",")})${returnType}`;
  }

  return node.getText();
}

function buildSourceFile(project: Project, filePath: string, text: string) {
  const extension = path.extname(filePath).toLowerCase();
  const scriptKind = extension === ".ts" || extension === ".tsx"
    ? ScriptKind.TS
    : extension === ".js" || extension === ".jsx"
      ? ScriptKind.JS
      : ScriptKind.TS;

  const virtualPath = `/virtual/${filePath.replaceAll("/", "_")}`;
  const existing = project.getSourceFile(virtualPath);
  if (existing) existing.delete();

  return project.createSourceFile(virtualPath, text, { scriptKind, overwrite: true });
}

function findNodesByKindAndSymbol(sourceFile: ReturnType<Project["createSourceFile"]> | null, kind: PatchedSymbolKind, symbol: string): Node[] {
  if (!sourceFile) return [];

  if (kind === "class") return sourceFile.getClasses().filter((node) => node.getName() === symbol);
  if (kind === "function") return sourceFile.getFunctions().filter((node) => node.getName() === symbol);

  if (kind === "method") {
    return sourceFile.getDescendantsOfKind(SyntaxKind.MethodDeclaration).filter((node) => node.getName() === symbol);
  }

  if (kind === "property") {
    return sourceFile.getDescendantsOfKind(SyntaxKind.PropertyDeclaration).filter((node) => node.getName() === symbol);
  }

  if (kind === "parameter") {
    return sourceFile.getDescendantsOfKind(SyntaxKind.Parameter).filter((node) => node.getName() === symbol);
  }

  return [];
}

function getDeclarationRangeForNode(node: Node): { start: number; end: number } {
  const start = node.getStartLineNumber();

  if (node.getKind() === SyntaxKind.MethodDeclaration) {
    const methodNode = node.asKindOrThrow(SyntaxKind.MethodDeclaration);
    const body = methodNode.getBody();
    const end = body ? Math.max(start, body.getStartLineNumber() - 1) : methodNode.getEndLineNumber();
    return { start, end };
  }

  if (node.getKind() === SyntaxKind.FunctionDeclaration) {
    const fnNode = node.asKindOrThrow(SyntaxKind.FunctionDeclaration);
    const body = fnNode.getBody();
    const end = body ? Math.max(start, body.getStartLineNumber() - 1) : fnNode.getEndLineNumber();
    return { start, end };
  }

  return { start, end: node.getEndLineNumber() };
}

function getBodyRangeForNode(node: Node): { start: number; end: number } | null {
  if (node.getKind() === SyntaxKind.MethodDeclaration) {
    const methodNode = node.asKindOrThrow(SyntaxKind.MethodDeclaration);
    const body = methodNode.getBody();
    if (!body) return null;
    return { start: body.getStartLineNumber(), end: body.getEndLineNumber() };
  }

  if (node.getKind() === SyntaxKind.FunctionDeclaration) {
    const fnNode = node.asKindOrThrow(SyntaxKind.FunctionDeclaration);
    const body = fnNode.getBody();
    if (!body) return null;
    return { start: body.getStartLineNumber(), end: body.getEndLineNumber() };
  }

  return { start: node.getStartLineNumber(), end: node.getEndLineNumber() };
}

function lineInRange(line: number, range: { start: number; end: number } | null): boolean {
  if (!range) return false;
  return line >= range.start && line <= range.end;
}

function yamlPathExists(protocolDocument: unknown, dotPath: string): boolean {
  const pathParts = dotPath.split(".");
  let current: unknown = protocolDocument;
  for (const part of pathParts) {
    if (current == null || typeof current !== "object" || !(part in (current as Record<string, unknown>))) {
      return false;
    }
    current = (current as Record<string, unknown>)[part];
  }
  return true;
}

function parsePatch(patchText: string): ParsedPatch {
  const additions: Array<{ line: number; text: string }> = [];
  const deletions: Array<{ line: number; text: string }> = [];
  const hunks: DiffHunk[] = [];
  let currentHunk: DiffHunk | null = null;

  let oldLine = 0;
  let newLine = 0;

  for (const rawLine of patchText.split("\n")) {
    const hunkMatch = rawLine.match(/^@@\s+-(\d+)(?:,\d+)?\s+\+(\d+)(?:,\d+)?\s+@@/);
    if (hunkMatch) {
      currentHunk = { lines: [] };
      hunks.push(currentHunk);
      oldLine = Number.parseInt(hunkMatch[1], 10);
      newLine = Number.parseInt(hunkMatch[2], 10);
      continue;
    }

    if (!currentHunk) continue;

    if (rawLine.startsWith("+")) {
      currentHunk.lines.push({ raw: rawLine, side: "R", oldLine: null, newLine });
      additions.push({ line: newLine, text: rawLine.slice(1) });
      newLine += 1;
      continue;
    }

    if (rawLine.startsWith("-")) {
      currentHunk.lines.push({ raw: rawLine, side: "L", oldLine, newLine: null });
      deletions.push({ line: oldLine, text: rawLine.slice(1) });
      oldLine += 1;
      continue;
    }

    if (rawLine.startsWith(" ")) {
      currentHunk.lines.push({ raw: rawLine, side: "C", oldLine, newLine });
      oldLine += 1;
      newLine += 1;
      continue;
    }

    if (rawLine.startsWith("\\")) {
      currentHunk.lines.push({ raw: rawLine, side: "C", oldLine: null, newLine: null });
    }
  }

  return { hunks, additions, deletions };
}

function diffSnippetForAnchor(parsedPatch: ParsedPatch, side: "L" | "R" | null, line: number | null): string {
  const allChangedLines = parsedPatch.hunks.flatMap((hunk) => hunk.lines.filter((diffLine) => diffLine.side !== "C"));
  if (allChangedLines.length === 0) return " No diff hunk available.";

  let targetHunk: DiffHunk | null = null;
  let targetIndex = -1;

  for (const hunk of parsedPatch.hunks) {
    for (let i = 0; i < hunk.lines.length; i += 1) {
      const diffLine = hunk.lines[i];
      if (side === "R" && line != null && diffLine.side === "R" && diffLine.newLine === line) {
        targetHunk = hunk;
        targetIndex = i;
        break;
      }
      if (side === "L" && line != null && diffLine.side === "L" && diffLine.oldLine === line) {
        targetHunk = hunk;
        targetIndex = i;
        break;
      }
    }
    if (targetHunk) break;
  }

  if (!targetHunk) {
    targetHunk = parsedPatch.hunks.find((hunk) => hunk.lines.some((diffLine) => diffLine.side !== "C")) ?? null;
    if (!targetHunk) return " No diff hunk available.";
    targetIndex = targetHunk.lines.findIndex((diffLine) => diffLine.side !== "C");
  }

  if (targetIndex < 0) return " No diff hunk available.";

  let leftChanged = targetIndex;
  while (leftChanged > 0 && targetHunk.lines[leftChanged - 1].side !== "C") leftChanged -= 1;

  let rightChanged = targetIndex;
  while (rightChanged < targetHunk.lines.length - 1 && targetHunk.lines[rightChanged + 1].side !== "C") rightChanged += 1;

  const start = Math.max(0, leftChanged - 3);
  const end = Math.min(targetHunk.lines.length - 1, rightChanged + 3);

  return targetHunk.lines.slice(start, end + 1).map((diffLine) => diffLine.raw).join("\n");
}

function diffSnippetForAnchorWithContext(parsedPatch: ParsedPatch, side: "L" | "R" | null, line: number | null, contextLines: number): string {
  const allChangedLines = parsedPatch.hunks.flatMap((hunk) => hunk.lines.filter((diffLine) => diffLine.side !== "C"));
  if (allChangedLines.length === 0) return " No diff hunk available.";

  let targetHunk: DiffHunk | null = null;
  let targetIndex = -1;

  for (const hunk of parsedPatch.hunks) {
    for (let i = 0; i < hunk.lines.length; i += 1) {
      const diffLine = hunk.lines[i];
      if (side === "R" && line != null && diffLine.side === "R" && diffLine.newLine === line) {
        targetHunk = hunk;
        targetIndex = i;
        break;
      }
      if (side === "L" && line != null && diffLine.side === "L" && diffLine.oldLine === line) {
        targetHunk = hunk;
        targetIndex = i;
        break;
      }
    }
    if (targetHunk) break;
  }

  if (!targetHunk) {
    targetHunk = parsedPatch.hunks.find((hunk) => hunk.lines.some((diffLine) => diffLine.side !== "C")) ?? null;
    if (!targetHunk) return " No diff hunk available.";
    targetIndex = targetHunk.lines.findIndex((diffLine) => diffLine.side !== "C");
  }

  if (targetIndex < 0) return " No diff hunk available.";

  let leftChanged = targetIndex;
  while (leftChanged > 0 && targetHunk.lines[leftChanged - 1].side !== "C") leftChanged -= 1;

  let rightChanged = targetIndex;
  while (rightChanged < targetHunk.lines.length - 1 && targetHunk.lines[rightChanged + 1].side !== "C") rightChanged += 1;

  const start = Math.max(0, leftChanged - contextLines);
  const end = Math.min(targetHunk.lines.length - 1, rightChanged + contextLines);
  return targetHunk.lines.slice(start, end + 1).map((diffLine) => diffLine.raw).join("\n");
}

function normalizeLineEndings(text: string): string[] {
  return text.replace(/\r\n/g, "\n").split("\n");
}

function lineDiff(oldLines: string[], newLines: string[]): Array<{ kind: " " | "+" | "-"; text: string }> {
  const m = oldLines.length;
  const n = newLines.length;
  const dp: number[][] = Array.from({ length: m + 1 }, () => Array<number>(n + 1).fill(0));

  for (let i = m - 1; i >= 0; i -= 1) {
    for (let j = n - 1; j >= 0; j -= 1) {
      if (oldLines[i] === newLines[j]) dp[i][j] = dp[i + 1][j + 1] + 1;
      else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }

  const out: Array<{ kind: " " | "+" | "-"; text: string }> = [];
  let i = 0;
  let j = 0;
  while (i < m && j < n) {
    if (oldLines[i] === newLines[j]) {
      out.push({ kind: " ", text: oldLines[i] });
      i += 1;
      j += 1;
      continue;
    }

    if (dp[i + 1][j] >= dp[i][j + 1]) {
      out.push({ kind: "-", text: oldLines[i] });
      i += 1;
    } else {
      out.push({ kind: "+", text: newLines[j] });
      j += 1;
    }
  }

  while (i < m) {
    out.push({ kind: "-", text: oldLines[i] });
    i += 1;
  }
  while (j < n) {
    out.push({ kind: "+", text: newLines[j] });
    j += 1;
  }

  return out;
}

function getNodeBodyText(node: Node | null): string | null {
  if (!node) return null;
  if (node.getKind() === SyntaxKind.MethodDeclaration) {
    const methodNode = node.asKindOrThrow(SyntaxKind.MethodDeclaration);
    return methodNode.getBody()?.getText() ?? null;
  }
  if (node
... [TRUNCATED]
```

### File: utils\extract_patched_symbols.ts
```ts
import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { Project, ScriptKind, SyntaxKind, type Node } from "ts-morph";

export type PatchedSymbolKind =
  | "class"
  | "method"
  | "property"
  | "function"
  | "parameter"
  | "protocol_param"
  | "protocol_property";

export type PatchedSymbolRecord = {
  symbol: string;
  kind: PatchedSymbolKind;
  playwrightFile: string;
  patchFile: string;
  patchFileLineStart: number | null;
  patchFileLineEnd: number | null;
  playwrightFileLineStart: number | null;
  playwrightFileLineEnd: number | null;
};

type ExtractOptions = {
  newVersionTag?: string;
  githubToken?: string;
};

type ParsedArgs = {
  outputPath: string | null;
  newVersionTag: string | null;
};

type ExtractEvent = {
  callName: string;
  value: string;
  index: number;
  lineStart: number;
  lineEnd: number;
};

const ROOT_DIR = process.cwd();
const DRIVER_PATCHES_DIR = path.join(ROOT_DIR, "driver_patches");

const SOURCE_FILE_CALLS = new Set(["getSourceFileOrThrow", "addSourceFileAtPath"]);
const SYMBOL_CALL_TO_KIND = new Map<string, PatchedSymbolKind>([
  ["getClassOrThrow", "class"],
  ["getClass", "class"],
  ["getMethodOrThrow", "method"],
  ["getMethod", "method"],
  ["getPropertyOrThrow", "property"],
  ["getProperty", "property"],
  ["getFunctionOrThrow", "function"],
  ["getFunction", "function"],
  ["getParameterOrThrow", "parameter"],
  ["getParameter", "parameter"],
]);

const TARGET_CALL_REGEX = /\b(getSourceFileOrThrow|addSourceFileAtPath|getClassOrThrow|getClass|getMethodOrThrow|getMethod|getPropertyOrThrow|getProperty|getFunctionOrThrow|getFunction|getParameterOrThrow|getParameter)\(\s*(["'`])([^"'`]+)\2\s*\)/g;

const PROTOCOL_SYMBOLS: PatchedSymbolRecord[] = [
  {
    symbol: "Frame.evaluateExpression.parameters.isolatedContext",
    kind: "protocol_param",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
  {
    symbol: "Frame.evaluateExpressionHandle.parameters.isolatedContext",
    kind: "protocol_param",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
  {
    symbol: "JSHandle.evaluateExpression.parameters.isolatedContext",
    kind: "protocol_param",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
  {
    symbol: "JSHandle.evaluateExpressionHandle.parameters.isolatedContext",
    kind: "protocol_param",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
  {
    symbol: "Worker.evaluateExpression.parameters.isolatedContext",
    kind: "protocol_param",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
  {
    symbol: "Worker.evaluateExpressionHandle.parameters.isolatedContext",
    kind: "protocol_param",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
  {
    symbol: "Frame.evalOnSelectorAll.parameters.isolatedContext",
    kind: "protocol_param",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
  {
    symbol: "ContextOptions.properties.focusControl",
    kind: "protocol_property",
    playwrightFile: "packages/protocol/src/protocol.yml",
    patchFile: "patchright_driver_patch.ts",
    patchFileLineStart: null,
    patchFileLineEnd: null,
    playwrightFileLineStart: null,
    playwrightFileLineEnd: null,
  },
];

function parseArgs(argv: string[]): ParsedArgs {
  const args: ParsedArgs = { outputPath: null, newVersionTag: null };
  for (let i = 2; i < argv.length; i += 1) {
    const arg = argv[i];
    if ((arg === "--output" || arg === "-o") && argv[i + 1]) {
      args.outputPath = argv[i + 1];
      i += 1;
      continue;
    }
    if (arg === "--new-version" && argv[i + 1]) {
      const version = argv[i + 1];
      args.newVersionTag = version.startsWith("v") ? version : `v${version}`;
      i += 1;
    }
  }
  return args;
}

function toRelativePosix(filePath: string): string {
  const rel = path.relative(ROOT_DIR, filePath);
  return rel.split(path.sep).join("/");
}

function computeLineStarts(text: string): number[] {
  const starts = [0];
  for (let i = 0; i < text.length; i += 1) {
    if (text[i] === "\n") starts.push(i + 1);
  }
  return starts;
}

function lineFromIndex(lineStarts: number[], index: number): number {
  let low = 0;
  let high = lineStarts.length - 1;
  let answer = 0;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (lineStarts[mid] <= index) {
      answer = mid;
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return answer + 1;
}

function lineRangeForIndex(lineStarts: number[], startIndex: number, length: number): { start: number; end: number } {
  const start = lineFromIndex(lineStarts, startIndex);
  const endIndex = Math.max(startIndex, startIndex + Math.max(0, length - 1));
  const end = lineFromIndex(lineStarts, endIndex);
  return { start, end };
}

function buildSourceFile(project: Project, filePath: string, text: string) {
  const extension = path.extname(filePath).toLowerCase();
  const scriptKind = extension === ".ts" || extension === ".tsx"
    ? ScriptKind.TS
    : extension === ".js" || extension === ".jsx"
      ? ScriptKind.JS
      : ScriptKind.TS;

  const virtualPath = `/virtual/${filePath.replaceAll("/", "_")}`;
  const existing = project.getSourceFile(virtualPath);
  if (existing) existing.delete();
  return project.createSourceFile(virtualPath, text, { scriptKind, overwrite: true });
}

function findNodesByKindAndSymbol(sourceFile: ReturnType<Project["createSourceFile"]> | null, kind: PatchedSymbolKind, symbol: string): Node[] {
  if (!sourceFile) return [];

  if (kind === "class") return sourceFile.getClasses().filter((node) => node.getName() === symbol);
  if (kind === "function") return sourceFile.getFunctions().filter((node) => node.getName() === symbol);

  if (kind === "method") {
    return sourceFile.getDescendantsOfKind(SyntaxKind.MethodDeclaration).filter((node) => node.getName() === symbol);
  }

  if (kind === "property") {
    return sourceFile.getDescendantsOfKind(SyntaxKind.PropertyDeclaration).filter((node) => node.getName() === symbol);
  }

  if (kind === "parameter") {
    return sourceFile.getDescendantsOfKind(SyntaxKind.Parameter).filter((node) => node.getName() === symbol);
  }

  return [];
}

function getSymbolBodyRange(node: Node): { start: number; end: number } {
  if (node.getKind() === SyntaxKind.MethodDeclaration) {
    const methodNode = node.asKindOrThrow(SyntaxKind.MethodDeclaration);
    const body = methodNode.getBody();
    if (body) return { start: methodNode.getStartLineNumber(), end: body.getEndLineNumber() };
    return { start: methodNode.getStartLineNumber(), end: methodNode.getEndLineNumber() };
  }

  if (node.getKind() === SyntaxKind.FunctionDeclaration) {
    const fnNode = node.asKindOrThrow(SyntaxKind.FunctionDeclaration);
    const body = fnNode.getBody();
    if (body) return { start: fnNode.getStartLineNumber(), end: body.getEndLineNumber() };
    return { start: fnNode.getStartLineNumber(), end: fnNode.getEndLineNumber() };
  }

  if (node.getKind() === SyntaxKind.ClassDeclaration) {
    const classNode = node.asKindOrThrow(SyntaxKind.ClassDeclaration);
    return { start: classNode.getStartLineNumber(), end: classNode.getEndLineNumber() };
  }

  return { start: node.getStartLineNumber(), end: node.getEndLineNumber() };
}

async function fetchRawFile(tag: string, filePath: string, token: string): Promise<string | null> {
  const url = `https://raw.githubusercontent.com/microsoft/playwright/${tag}/${filePath}`;
  const response = await fetch(url, {
    headers: {
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      "User-Agent": "patchright-extract-patched-symbols",
    },
  });

  if (response.status === 404) return null;
  if (!response.ok) throw new Error(`Failed to fetch ${filePath} at ${tag}: HTTP ${response.status}`);
  return response.text();
}

export async function extractPatchedSymbols(options: ExtractOptions = {}): Promise<PatchedSymbolRecord[]> {
  const entries = await fs.readdir(DRIVER_PATCHES_DIR, { withFileTypes: true });

  const patchFiles = entries
    .filter((entry) => entry.isFile())
    .map((entry) => entry.name)
    .filter((name) => name.endsWith(".ts"))
    .filter((name) => name !== "index.ts");

  const records: PatchedSymbolRecord[] = [];

  for (const patchFile of patchFiles) {
    const absolutePatchPath = path.join(DRIVER_PATCHES_DIR, patchFile);
    const content = await fs.readFile(absolutePatchPath, "utf8");
    const lineStarts = computeLineStarts(content);

    const events: ExtractEvent[] = [];
    for (const match of content.matchAll(TARGET_CALL_REGEX)) {
      const callName = match[1];
      const value = match[3];
      const index = match.index ?? 0;
      const range = lineRangeForIndex(lineStarts, index, match[0].length);
      events.push({ callName, value, index, lineStart: range.start, lineEnd: range.end });
    }

    events.sort((a, b) => a.index - b.index);

    let currentPlaywrightFile: string | null = null;
    for (const event of events) {
      if (SOURCE_FILE_CALLS.has(event.callName)) {
        currentPlaywrightFile = event.value;
        continue;
      }

      const kind = SYMBOL_CALL_TO_KIND.get(event.callName);
      if (!kind || !currentPlaywrightFile) continue;

      records.push({
        symbol: event.value,
        kind,
        playwrightFile: currentPlaywrightFile,
        patchFile,
        patchFileLineStart: event.lineStart,
        patchFileLineEnd: event.lineEnd,
        playwrightFileLineStart: null,
        playwrightFileLineEnd: null,
      });
    }
  }

  records.push(...PROTOCOL_SYMBOLS);

  const deduped: PatchedSymbolRecord[] = [];
  const seen = new Set<string>();
  for (const record of records) {
    const key = `${record.symbol}::${record.kind}::${record.playwrightFile}::${record.patchFile}`;
    if (seen.has(key)) continue;
    seen.add(key);
    deduped.push(record);
  }

  deduped.sort((a, b) => {
    if (a.playwrightFile !== b.playwrightFile) return a.playwrightFile.localeCompare(b.playwrightFile);
    if (a.patchFile !== b.patchFile) return a.patchFile.localeCompare(b.patchFile);
    if (a.kind !== b.kind) return a.kind.localeCompare(b.kind);
    return a.symbol.localeCompare(b.symbol);
  });

  if (options.newVersionTag) {
    const project = new Project({ useInMemoryFileSystem: true });
    const token = options.githubToken ?? "";
    const fileTexts = new Map<string, string | null>();
    const uniqueFiles = [...new Set(deduped.map((record) => record.playwrightFile))];

    for (const playwrightFile of uniqueFiles) {
      if (playwrightFile === "packages/protocol/src/protocol.yml") {
        fileTexts.set(playwrightFile, null);
        continue;
      }
      fileTexts.set(playwrightFile, await fetchRawFile(options.newVersionTag, playwrightFile, token));
    }

    for (const record of deduped) {
      if (record.kind === "protocol_param" || record.kind === "protocol_property") continue;
      const text = fileTexts.get(record.playwrightFile);
      if (!text) continue;

      const sourceFile = buildSourceFile(project, record.playwrightFile, text);
      const nodes = findNodesByKindAndSymbol(sourceFile, record.kind, record.symbol);
      const node = nodes[0];
      if (!node) continue;

      const range = getSymbolBodyRange(node);
      record.playwrightFileLineStart = range.start;
      record.playwrightFileLineEnd = range.end;
    }
  }

  return deduped;
}

async function main(): Promise<void> {
  const args = parseArgs(process.argv);
  const symbols = await extractPatchedSymbols({
    newVersionTag: args.newVersionTag ?? undefined,
    githubToken: process.env.GITHUB_TOKEN || process.env.GH_TOKEN || "",
  });
  const json = `${JSON.stringify(symbols, null, 2)}\n`;

  if (args.outputPath) {
    const absOut = path.resolve(ROOT_DIR, args.outputPath);
    await fs.mkdir(path.dirname(absOut), { recursive: true });
    await fs.writeFile(absOut, json, "utf8");
    console.log(`Wrote ${symbols.length} symbol records to ${toRelativePosix(absOut)}`);
    return;
  }

  process.stdout.write(json);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch((error: unknown) => {
    console.error(error instanceof Error ? error.stack : error);
    process.exitCode = 1;
  });
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
