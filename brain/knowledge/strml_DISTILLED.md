---
id: strml
type: knowledge
owner: OA_Triage
---
# strml
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "strml.net",
  "version": "0.0.1",
  "description": "",
  "main": "app.js",
  "scripts": {
    "build": "webpack",
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "webpack serve --open",
    "watch": "webpack --progress --watch"
  },
  "author": "Samuel Reed <samuel.trace.reed@gmail.com> (http://strml.net/)",
  "license": "MIT",
  "devDependencies": {
    "@babel/core": "^7.14.0",
    "@babel/plugin-proposal-class-properties": "^7.13.0",
    "@babel/plugin-proposal-json-strings": "^7.13.8",
    "@babel/plugin-syntax-dynamic-import": "^7.8.3",
    "@babel/plugin-syntax-import-meta": "^7.10.4",
    "@babel/plugin-transform-runtime": "^7.13.15",
    "@babel/preset-env": "^7.14.1",
    "@babel/preset-flow": "^7.13.13",
    "babel-loader": "^8.2.2",
    "exports-loader": "^2.0.0",
    "raw-loader": "^4.0.2",
    "webpack": "^5.36.2",
    "webpack-cli": "^4.7.0",
    "webpack-dev-server": "^3.11.2"
  },
  "dependencies": {
    "@babel/runtime": "^7.14.0",
    "bluebird": "^3.7.2",
    "classlist-polyfill": "^1.0.1",
    "markdown": "^0.5.0",
    "mouse-wheel": "^1.0.2",
    "util": "^0.12.3"
  }
}

```

### File: README.md
```md
STRML.net
=========

[View Site](http://strml.net)

Building
--------

```bash
git clone git@github.com:STRML/strml.net.git
cd strml.net
npm install
npm run dev
# Open localhost:4003/index-dev.html in your browser
```

Building for Production
--------

```bash
npm run build
```

```

### File: app.js
```js
import 'classlist-polyfill';
import Promise from 'bluebird';
import Markdown from 'markdown';
const md = Markdown.markdown.toHTML;
import workText from 'raw-loader!./work.txt';
import pgpText from 'raw-loader!./pgp.txt';
import headerHTML from 'raw-loader!./header.html';
let styleText = [0, 1, 2, 3].map((i) => require('raw-loader!./styles' + i + '.css').default);
import preStyles from 'raw-loader!./prestyles.css';
import replaceURLs from './lib/replaceURLs';
import {default as writeChar, writeSimpleChar, handleChar} from './lib/writeChar';
import getPrefix from './lib/getPrefix';

// Vars that will help us get er done
const isDev = window.location.hostname === 'localhost';
const speed = isDev ? 0 : 16;
let style, styleEl, workEl, pgpEl, skipAnimationEl, pauseEl;
let animationSkipped = false, done = false, paused = false;
let browserPrefix;

// Wait for load to get started.
document.addEventListener("DOMContentLoaded", function() {
  getBrowserPrefix();
  populateHeader();
  getEls();
  createEventHandlers();
  startAnimation();
});

async function startAnimation() {
  try {
    await writeTo(styleEl, styleText[0], 0, speed, true, 1);
    await writeTo(workEl, workText, 0, speed, false, 1);
    await writeTo(styleEl, styleText[1], 0, speed, true, 1);
    createWorkBox();
    await Promise.delay(1000);
    await writeTo(styleEl, styleText[2], 0, speed, true, 1);
    await writeTo(pgpEl, pgpText, 0, speed, false, 32);
    await writeTo(styleEl, styleText[3], 0, speed, true, 1);
  }
  // Flow control straight from the ghettos of Milwaukee
  catch(e) {
    if (e.message === "SKIP IT") {
      surprisinglyShortAttentionSpan();
    } else {
      throw e;
    }
  }
}

// Skips all the animations.
async function surprisinglyShortAttentionSpan() {
  if (done) return;
  done = true;
  pgpEl.innerHTML = pgpText;
  let txt = styleText.join('\n');

  // The work-text animations are rough
  style.textContent = "#work-text * { " + browserPrefix + "transition: none; }";
  style.textContent += txt;
  let styleHTML = "";
  for(let i = 0; i < txt.length; i++) {
     styleHTML = handleChar(styleHTML, txt[i]);
  }
  styleEl.innerHTML = styleHTML;
  createWorkBox();

  // There's a bit of a scroll problem with this thing
  let start = Date.now();
  while(Date.now() - 1000 > start) {
    workEl.scrollTop = Infinity;
    styleEl.scrollTop = pgpEl.scrollTop = Infinity;
    await Promise.delay(16);
  }
}


/**
 * Helpers
 */

let endOfSentence = /[\.\?\!]\s$/;
let comma = /\D[\,]\s$/;
let endOfBlock = /[^\/]\n\n$/;

async function writeTo(el, message, index, interval, mirrorToStyle, charsPerInterval){
  if (animationSkipped) {
    // Lol who needs proper flow control
    throw new Error('SKIP IT');
  }
  // Write a character or multiple characters to the buffer.
  let chars = message.slice(index, index + charsPerInterval);
  index += charsPerInterval;

  // Ensure we stay scrolled to the bottom.
  el.scrollTop = el.scrollHeight;

  // If this is going to <style> it's more complex; otherwise, just write.
  if (mirrorToStyle) {
    writeChar(el, chars, style);
  } else {
    writeSimpleChar(el, chars);
  }

  // Schedule another write.
  if (index < message.length) {
    let thisInterval = interval;
    let thisSlice = message.slice(index - 2, index + 1);
    if (comma.test(thisSlice)) thisInterval = interval * 30;
    if (endOfBlock.test(thisSlice)) thisInterval = interval * 50;
    if (endOfSentence.test(thisSlice)) thisInterval = interval * 70;

    do {
      await Promise.delay(thisInterval);
    } while(paused);

    return writeTo(el, message, index, interval, mirrorToStyle, charsPerInterval);
  }
}

//
// Older versions of major browsers (like Android) still use prefixes. So we figure out what that prefix is
// and use it.
//
function getBrowserPrefix() {
  // Ghetto per-browser prefixing
  browserPrefix = getPrefix(); // could be empty string, which is fine
  styleText = styleText.map(function(text) {
    return text.replace(/-webkit-/g, browserPrefix);
  });
}

//
// Put els into the module scope.
//
function getEls() {
  // We're cheating a bit on styles.
  let preStyleEl = document.createElement('style');
  preStyleEl.textContent = preStyles;
  document.head.insertBefore(preStyleEl, document.getElementsByTagName('style')[0]);

  // El refs
  style = document.getElementById('style-tag');
  styleEl = document.getElementById('style-text');
  workEl = document.getElementById('work-text');
  pgpEl = document.getElementById('pgp-text');
  skipAnimationEl = document.getElementById('skip-animation');
  pauseEl = document.getElementById('pause-resume');
}

//
// Create links in header (now footer).
//
function populateHeader() {
  let header = document.getElementById('header');
  header.innerHTML = headerHTML;
}

//
// Create basic event handlers for user input.
//
function createEventHandlers() {
  // Mirror user edits back to the style element.
  styleEl.addEventListener('input', function() {
    style.textContent = styleEl.textContent;
  });

  // Skip anim on click to skipAnimation
  skipAnimationEl.addEventListener('click', function(e) {
    e.preventDefault();
    animationSkipped = true;
  });

  pauseEl.addEventListener('click', function(e) {
    e.preventDefault();
    if (paused) {
      pauseEl.textContent = "Pause ||";
      paused = false;
    } else {
      pauseEl.textContent = "Resume >>";
      paused = true;
    }
  });
}

//
// Fire a listener when scrolling the 'work' box.
//
function createWorkBox() {
  if (workEl.classList.contains('flipped')) return;
  workEl.innerHTML = '<div class="text">' + replaceURLs(workText) + '</div>' +
                     '<div class="md">' + replaceURLs(md(workText)) + '<div>';

  workEl.classList.add('flipped');
  workEl.scrollTop = 9999;

  // flippy floppy
  let flipping = 0;
  require('mouse-wheel')(workEl, async function(dx, dy) {
    if (flipping) return;
    let flipped = workEl.classList.contains('flipped');
    let half = (workEl.scrollHeight - workEl.clientHeight) / 2;
    let pastHalf = flipped ? workEl.scrollTop < half : workEl.scrollTop > half;

    // If we're past half, flip the el.
    if (pastHalf) {
      workEl.classList.toggle('flipped');
      flipping = true;
      await Promise.delay(500);
      workEl.scrollTop = flipped ? 0 : 9999;
      flipping = false;
    }

    // Scroll. If we've flipped, flip the scroll direction.
    workEl.scrollTop += (dy * (flipped ? -1 : 1));
  }, true);
}

```

### File: header.html
```html
<a href="#" id="pause-resume">Pause ||</a>
<a href="#" id="skip-animation">Skip Animation --></a>
<span style="float:right">
<a href="http://blog.strml.net">Blog</a>
<a href="https://www.bitmex.com">BitMEX</a>
<a href="https://securesha.re">SecureSha.re</a>
<a href="https://github.com/strml">GitHub</a>
<a href="https://github.com/STRML/strml.net/blob/master/app.js">View Source</a>
</span>

```

### File: index.html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>STRML: Projects and Work</title>
    <style id="style-tag"></style>
    <script src="dist/app.js"></script>
    <link rel="icon" type="image/png" sizes="32x32" href="/ico/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/ico/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/ico/favicon-16x16.png">
    <link rel="shortcut icon" href="/ico/favicon.ico" type="image/x-icon" />
  </head>
  <body spellcheck="false">
    <div id="content">
      <pre contenteditable id="style-text"></pre>
      <pre id="work-text"></pre>
      <pre id="pgp-text"></pre>
    </div>
    <div id="header"></div>
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-61551308-1', 'auto');
      ga('send', 'pageview');
    </script>
  </body>
</html>

```

### File: pgp.txt
```txt
## BEGIN samuel trace reed (ät) gmail com ##

-----BEGIN PGP PUBLIC KEY BLOCK-----

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
hjbIem327A==
=TEIf
-----END PGP PUBLIC KEY BLOCK-----


## END samuel trace reed (ät) gmail com ##
## BEGIN sam (ät) bitmex com ##

-----BEGIN PGP PUBLIC KEY BLOCK-----

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
... [TRUNCATED]
```

### File: prestyles.css
```css
/* I'm cheating a bit */

html, body {
  margin-top: 0;
  height: 100%;
  overflow: hidden;
}

pre {
  overflow: auto;
  max-height: 90%;
  width: 100%;
  border-radius: 1px; /* Prevents bad clipping in Chrome */
}

#content {
  position: absolute;
  top: 0; right: 0; left: 0; bottom: 20px;
}

#header {
  position: absolute;
  bottom: 0;
  height: 20px;
  left: 0;
  right: 0;
  padding: 0 10px;
}

a:after {
  content: '';
  padding-right: 5px;
  border-right-width: 1px;
  border-right-style: solid;
  border-color: inherit;
}

a:last-of-type:after {
  border: none;
}

```

### File: styles0.css
```css
/**
 *
 * Hey. My name's Samuel Reed. I'm a co-founder of BitMEX and frequent
 * open source contributor.
 *
 * I build interactive websites.
 *
 * How about some live coding?
 */

/**
 * Let's begin. We start by animating... well, everything.
 */

* {
  -webkit-transition: all 1s;
}

/**
 * That didn't do much. But you'll see.
 *
 * Black on white is really boring,
 * so let's do something about it.
 */

html {
  background: rgb(63, 82, 99);
}

/***
 * Hold on...
 */

pre, a {
  color: white;
}

/**
 * That's better. Sorry about your eyes.
 *
 * Working in this big empty space is tough.
 *
 * I'm going to make a nice area for us to work in.
 */

pre:not(:empty) {
  overflow: auto;
  background: rgb(48, 48, 48);
  border: 1px solid #ccc;
  max-height: 45vh;
  width: 49%;
  font-size: 14px;
  font-family: monospace;
  padding: 1vh 0.5vw;
  box-shadow: -4px 4px 2px 0 rgba(0,0,0,0.3);
  white-space: pre-wrap;
  outline: 0;
  margin: 1vh 0.5vw;
}

/**
 * Okay. We're going to start filling up the screen.
 * Let's get ready to do some work.
 */

#style-text {
  -webkit-transform: translateX(95%);
  position: absolute;
}

/**
 * This is good, but all the text is white!
 * Let's make it even more readable.
 */

.comment       { color: #857F6B; font-style: italic; }
.selector      { color: #E69F0F; }
.selector .key { color: #64D5EA; }
.key           { color: #64D5EA; }
.value         { color: #BE84F2; }
.value.px      { color: #F92772; }

/**
 * Now we're getting somewhere.
 * Time to get a little perspective.
 */

body {
  -webkit-perspective: 1000px;
}

#style-text {
  -webkit-transform: translateX(98.5%) rotateY(-10deg);
  -webkit-transform-origin: right;
  max-height: 93.1vh;
}

/**
 * So, let's talk projects. That's why you're here, right?
 * I can't imagine you'd come just to see the pretty colors.
 */

pre:not(#style-text) {
  -webkit-transform: rotateY(10deg);
  -webkit-transform-origin: left;
}

```

### File: styles1.css
```css

/**
 * That markdown on the left doesn't look great. Let's render it.
 */

#work-text.flipped {
  -webkit-transform: rotateX(0deg) rotateY(190deg) rotateZ(180deg);
}

#work-text .md {
  -webkit-transform: rotateY(190deg) rotateZ(180deg);
  margin-top: 800px;
}

/**
 * Alright. We're ready.
 *
 * 3...
 * 2...
 * 1...
 *
 * .
 * ....faked you out.
 *
 * Okay here we go!
 *
 */

```

### File: styles2.css
```css

/**
 * The text could use some tweaks.
 */

.md {
  font-family: "Helvetica Neue", Helvetica, sans-serif;
}

.md h1, .md h2, .md h3, .md h4, .md h5, .md h6 {
  display: inline-block;
  color: #ddd;
  border-bottom: 1px solid #ccc;
  padding-bottom: 5px;
}

.md li {
  margin: 5px 0;
}

.md h1, .md h2, .md h3, .md h4, .md h5, .md h6, .md ul, .md p {
  margin: 0px;
}

/**
 * That's better.
 *
 * If you want to contact me, use the PGP keys on the left.
 *
 * You know, if you're into that sort of thing.
 */

#pgp-text {
  font-size: 12px;
  color: #ada;
}

```

### File: styles3.css
```css

/**
 * We're almost done.
 */

 pre:hover{
   box-shadow: 0px 0px 40px 5px rgba(255,255,255,0.4);
 }

 #skip-animation, #pause-resume {
   display: none;
 }

/**
 * I hope you enjoyed this.
 *
 * Thanks to Jake Albaugh, who was the first (that I know of) to do
 * a page like this. Some of the autotyping and syntax highlighting
 * code is based off his work.
 *
 * See more of Jake's work at http://codepen.io/jakealbaugh/
 */

/**
 * By the way, you can edit this box. Try adding new CSS!
 *
 * For example,
 *
 * The property 'text-shadow' takes the parameters:
 * 'x', 'y', 'blur', 'color'.
 *
 * So if I wanted to mirror the values,
 * I could place a shadow 15px under it,
 * with a little blur for effect:
 */

.value {
  text-shadow: 0px 15px 1px white;
}

/**
 * Try it out! There's lots you can do.
 * Try playing with text sizes, shadows, animations, or just
 * break the page. I won't hold it against you.
 */



```

### File: webpack.config.js
```js
'use strict';
var webpack = require('webpack');
var path = require('path');

// Builds bundle usable inside <script>.
module.exports = {
  context: __dirname,
  mode: 'production',
  entry: {
    'app': './app.js'
  },
  output: {
    path: path.join(__dirname, "/dist"),
    filename: "[name].js",
    libraryTarget: "umd",
    library: "app",
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: {
          cacheDirectory: true,
        }
      }
    ]
  },
  resolve: {
    fallback: {
      util: require.resolve('util/')
    }
  },
  devServer: {
    contentBase: __dirname,
    publicPath: '/dist',
    compress: true,
    port: 4003,
  },
  optimization: {
    minimize: true
  },
};

```

### File: work.txt
```txt
STRML.net
=========

Samuel Reed
Co-Founder, BitMEX (The Bitcoin Mercantile Exchange)
Full-Stack / NodeJS / DevOps

Contact
-------

* sam at bitmex dot com
* samuel.trace.reed at gmail dot com
* STRML on irc.freenode.net
* @STRML_ on Twitter
* STRML#7665 on Discord

Projects
--------

* www.BitMEX.com
* www.Securesha.re
* www.Tixelated.com
* www.BrightestYoungThings.com
and of course...
* www.strml.net

Open Source
-----------

* Babel
* React-Grid-Layout
* React-LocalStorage
* React-Router-Component
* React-Resizable
* React-Draggable
* OpenBazaar
* JSXHint
* BTChip-Signing-Tools
* TextFit
* Imgur-to-GFYcat
* backbone.queryRouter
* backbone.layoutManager
* Mongoose-Filter-Denormalize

Photos
------

* [Party Rock is in the hou](/img/partyrock1.jpg)
  * [se tonight](/img/partyrock2.jpg)
```

### File: lib\getPrefix.js
```js
// @flow
export default function generatePrefix(): string {
  // Checking specifically for 'window.document' is for pseudo-browser server-side
  // environments that define 'window' as the global context.
  // E.g. React-rails (see https://github.com/reactjs/react-rails/pull/84)
  if (typeof window === 'undefined' || typeof window.document === 'undefined') return '';

  const prefixes = ['Moz', 'Webkit', 'O', 'ms'];
  const style = window.document.documentElement.style;

  if ('transform' in style) {
    return '';
  }

  for (let i = 0; i < prefixes.length; ++i) {
    if (prefixes[i] + 'Transform' in style) {
      return prefixes[i];
    }
  }
  return '';
}


```

### File: lib\replaceURLs.js
```js
const urlRegex = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w\-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w!\/]*))?)/g;

export default function createAnchors(message) {
  return regexReplace(message, urlRegex, function(match) {
    // Don't break <img src="http:..." /> or mailtos or other anchors
    if (/(src=|href=|mailto:)/.test(message.slice(message.indexOf(match) - 7).slice(0, 7))) return match;
    let href = match;
    if (match.slice(0, 4) !== 'http') href = 'http://' + href;
    return '<a href="' + href + '" target="_blank">' + match.replace('www.', '') + '</a>';
  });
};

// Simple regex replace function.
export function regexReplace(message, regex, replace) {
  const match = message.match(regex);
  if (match && match.length) {
    for (let i = 0; i < match.length; i++) {
      message = message.replace(match[i], (typeof replace === 'function' ? replace(match[i]) : replace));
    }
  }
  return message;
}

```

### File: lib\writeChar.js
```js
let styleBuffer = '';
const fullTextStorage = {};

export default function writeChar(el, char, style){
  // Grab text. We buffer it in storage so we don't have to read from the DOM every iteration.
  let fullText = fullTextStorage[el.id];
  if (!fullText) fullText = fullTextStorage[el.id] = el.innerHTML;

  fullText = handleChar(fullText, char);
  // But we still write to the DOM every iteration, which can be pretty slow.
  el.innerHTML = fullTextStorage[el.id] = fullText;

  // Buffer writes to the <style> element so we don't have to paint quite so much.
  styleBuffer += char;
  if (char === ';') {
    style.textContent += styleBuffer;
    styleBuffer = '';
  }
};

export function writeSimpleChar(el, char) {
  el.innerHTML += char;
};

let openComment = false;
const commentRegex = /(\/\*(?:[^](?!\/\*))*\*)$/;
const keyRegex = /([a-zA-Z- ^\n]*)$/;
const valueRegex = /([^:]*)$/;
const selectorRegex = /(.*)$/;
const pxRegex = /\dp/;
const pxRegex2 = /p$/;

export function handleChar(fullText, char) {
  if (openComment && char !== '/') {
    // Short-circuit during a comment so we don't highlight inside it.
    fullText += char;
  } else if (char === '/' && openComment === false) {
    openComment = true;
    fullText += char;
  } else if (char === '/' && fullText.slice(-1) === '*' && openComment === true) {
    openComment = false;
    // Unfortunately we can't just open a span and close it, because the browser will helpfully
    // 'fix' it for us, and we'll end up with a single-character span and an empty closing tag.
    fullText = fullText.replace(commentRegex, '<span class="comment">$1/</span>');
  } else if (char === ':') {
    fullText = fullText.replace(keyRegex, '<span class="key">$1</span>:');
  } else if (char === ';') {
    fullText = fullText.replace(valueRegex, '<span class="value">$1</span>;');
  } else if (char === '{') {
    fullText = fullText.replace(selectorRegex, '<span class="selector">$1</span>{');
  } else if (char === 'x' && pxRegex.test(fullText.slice(-2))) {
    fullText = fullText.replace(pxRegex2, '<span class="value px">px</span>');
  } else {
    fullText += char;
  }
  return fullText;
}

```

