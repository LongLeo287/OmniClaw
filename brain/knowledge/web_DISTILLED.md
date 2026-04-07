---
id: web
type: knowledge
owner: OA_Triage
---
# web
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "web-check",
  "type": "module",
  "version": "2.0.2",
  "homepage": "https://web-check.xyz",
  "scripts": {
    "start": "node server",
    "start-pm": "pm2 start server.js -i max",
    "build": "astro check && astro build",
    "dev:vercel": "PLATFORM='vercel' npx vercel dev",
    "dev:netlify": "PLATFORM='netlify' npx netlify dev",
    "dev:api": "DISABLE_GUI='true' PORT='3001' nodemon server",
    "dev:astro": "PUBLIC_API_ENDPOINT=http://localhost:3001/api astro dev",
    "dev": "concurrently -c magenta,cyan -n backend,frontend 'yarn dev:api' 'yarn dev:astro'"
  },
  "dependencies": {
    "@astrojs/check": "^0.5.10",
    "@astrojs/react": "^3.3.2",
    "@emotion/react": "^11.11.4",
    "@emotion/styled": "^11.11.5",
    "@fortawesome/fontawesome-svg-core": "^6.5.2",
    "@fortawesome/free-brands-svg-icons": "^6.5.2",
    "@fortawesome/free-regular-svg-icons": "^6.5.2",
    "@fortawesome/free-solid-svg-icons": "^6.5.2",
    "@fortawesome/svelte-fontawesome": "^0.2.2",
    "@types/react": "^18.3.1",
    "@types/react-dom": "^18.3.0",
    "astro": "^4.7.1",
    "axios": "^1.4.8",
    "cheerio": "^1.0.0-rc.12",
    "chrome-aws-lambda": "^10.1.0",
    "chromium": "^3.0.3",
    "connect-history-api-fallback": "^2.0.0",
    "cors": "^2.8.5",
    "csv-parser": "^3.0.0",
    "dotenv": "^16.4.5",
    "express": "^4.19.2",
    "express-rate-limit": "^7.2.0",
    "framer-motion": "^11.2.6",
    "got": "^14.2.1",
    "pm2": "^5.3.1",
    "psl": "^1.9.0",
    "puppeteer": "^22.8.0",
    "puppeteer-core": "^22.8.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-masonry-css": "^1.0.16",
    "react-router-dom": "^6.23.0",
    "react-simple-maps": "^3.0.0",
    "react-toastify": "^10.0.5",
    "recharts": "^2.12.6",
    "svelte": "^4.2.17",
    "traceroute": "^1.0.0",
    "typescript": "^5.4.5",
    "unzipper": "^0.11.5",
    "url-parse": "^1.5.10",
    "wappalyzer": "^6.10.65",
    "xml2js": "^0.6.2"
  },
  "devDependencies": {
    "@astrojs/cloudflare": "^10.2.5",
    "@astrojs/netlify": "^5.2.0",
    "@astrojs/node": "^8.2.5",
    "@astrojs/partytown": "^2.1.0",
    "@astrojs/sitemap": "^3.1.4",
    "@astrojs/svelte": "^5.4.0",
    "@astrojs/ts-plugin": "^1.6.1",
    "@astrojs/vercel": "^7.5.4",
    "concurrently": "^8.2.2",
    "nodemon": "^3.1.0",
    "sass": "^1.77.1"
  }
}

```

### File: .github\README.md
```md
<h1 align="center">Web-Check</h1>


<p align="center">
<img src="https://i.ibb.co/q1gZN2p/web-check-logo.png" width="96" /><br />
<b><i>Comprehensive, on-demand open source intelligence for any website</i></b>
<br />
<b>🌐 <a href="https://web-check.xyz/">web-check.xyz</a></b><br />

</p>

---
<p align="center">
  <sup>Kindly supported by:</sup><br>
<a href="https://terminaltrove.com/?utm_campaign=github&utm_medium=referral&utm_content=web-check&utm_source=wcgh">
  <img src="https://i.ibb.co/8jrrcZ0/IMG-7210.jpg" width="300" alt="Terminal Trove">
  <br>
  <strong>The $HOME of all things in the terminal.</strong>
</a>
<br>
<a href="https://terminaltrove.com/newsletter?utm_campaign=github&utm_medium=referral&utm_content=web-check&utm_source=wcgh">
  <sub>Find your next CLI / TUI tool and more at Terminal Trove,</sub>
  <br>
  <sup>Get updates on new tools on our newsletter.</sup>
</a>
</p>

<p align="center">
	<sup>Kindly supported by:</sup><br>
	<a href="https://go.warp.dev/web-check"><b>Warp</b>, built for coding with multiple AI agents</a><br><br>
	<a href="https://go.warp.dev/web-check"><img width="640" src="https://github.com/warpdotdev/brand-assets/blob/main/Github/Sponsor/Warp-Github-LG-02.png?raw=true" /></a>
</p>

---

#### Contents

- **[About](#about)**
  - [Screenshot](#screenshot)
  - [Live Demo](#live-demo)
  - [Mirror](#mirror)
  - [Features](#features)
- **[Usage](#usage)**
  - [Deployment](#deployment)
    - [Option#1: Netlify](#deploying---option-1-netlify)
    - [Option#2: Vercel](#deploying---option-2-vercel)
    - [Option#3: Docker](#deploying---option-3-docker)
    - [Option#4: Source](#deploying---option-4-from-source)
  - [Configuration Options](#configuring)
  - [Developer Setup](#developing)
- **[Community](#community)**
  - [Contributing](#contributing)
  - [Bugs](#reporting-bugs)
  - [Support](#supporting)
- **[License](#license)**

---

## About
Get an insight into the inner-workings of a given website: uncover potential attack vectors, analyse server architecture, view security configurations, and learn what technologies a site is using.

Currently the dashboard will show: IP info, SSL chain, DNS records, cookies, headers, domain info, search crawl rules, page map, server location, redirect ledger, open ports, traceroute, DNS security extensions, site performance, trackers, associated hostnames, carbon footprint. Stay tuned, as I'll add more soon!

The aim is to help you easily understand, optimize and secure your website.

### Screenshot

<details>
      <summary>Expand Screenshot</summary>

[![Screenshot](https://raw.githubusercontent.com/Lissy93/web-check/master/.github/screenshots/web-check-screenshot1.png)](https://web-check.as93.net/)
      
</details>

[![Screenshot](https://i.ibb.co/r0jXN6s/web-check.png)](https://github.com/Lissy93/web-check/tree/master/.github/screenshots)

### Live Demo
A hosted version can be accessed at: **[web-check.as93.net](https://web-check.as93.net)**

### Mirror
The source for this repo is mirrored to CodeBerg, available at: **[codeberg.org/alicia/web-check](https://codeberg.org/alicia/web-check)**

### Status


Build & Deploys: [![Netlify Status](https://api.netlify.com/api/v1/badges/c43453c1-5333-4df7-889b-c1d2b52183c0/deploy-status)](https://app.netlify.com/sites/web-check/deploys)
[![Vercel Status](https://therealsujitk-vercel-badge.vercel.app/?app=web-check-ten)](https://vercel.com/as93/web-check/)
[![🐳 Build + Publish Docker Image](https://github.com/Lissy93/web-check/actions/workflows/docker.yml/badge.svg)](https://github.com/Lissy93/web-check/actions/workflows/docker.yml)
[![🚀 Deploy to AWS](https://github.com/Lissy93/web-check/actions/workflows/deploy-aws.yml/badge.svg)](https://github.com/Lissy93/web-check/actions/workflows/deploy-aws.yml)
<br />
Repo Management & Miscellaneous: [![🪞 Mirror to Codeberg](https://github.com/Lissy93/web-check/actions/workflows/mirror.yml/badge.svg)](https://github.com/Lissy93/web-check/actions/workflows/mirror.yml)
[![💓 Inserts Contributors & Sponsors](https://github.com/Lissy93/web-check/actions/workflows/credits.yml/badge.svg)](https://github.com/Lissy93/web-check/actions/workflows/credits.yml)


### Features

<details open>
<summary><b>Click to expand / collapse section</b></summary>

<sup>**Note** _this list needs updating, many more jobs have been added since..._</sup>

The following section outlines the core features, and briefly explains why this data might be useful for you to know, as well as linking to further resources for learning more.

<details>
<summary><b>IP Info</b></summary>

###### Description
An IP address (Internet Protocol address) is a numerical label assigned to each device connected to a network / the internet. The IP associated with a given domain can be found by querying the Domain Name System (DNS) for the domain's A (address) record.

###### Use Cases
Finding the IP of a given server is the first step to conducting further investigations, as it allows us to probe the server for additional info. Including creating a detailed map of a target's network infrastructure, pinpointing the physical location of a server, identifying the hosting service, and even discovering other domains that are hosted on the same IP address.

###### Useful Links
- [Understanding IP Addresses](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking)
- [IP Addresses - Wiki](https://en.wikipedia.org/wiki/IP_address)
- [RFC-791 Internet Protocol](https://tools.ietf.org/html/rfc791)
- [whatismyipaddress.com](https://whatismyipaddress.com/)

</details>
<details>
<summary><b>SSL Chain</b></summary>

<img width="300" src="https://i.ibb.co/kB7LsV1/wc-ssl.png" align="right" />

###### Description
SSL certificates are digital certificates that authenticate the identity of a website or server, enable secure encrypted communication (HTTPS), and establish trust between clients and servers. A valid SSL certificate is required for a website to be able to use the HTTPS protocol, and encrypt user + site data in transit. SSL certificates are issued by Certificate Authorities (CAs), which are trusted third parties that verify the identity and legitimacy of the certificate holder.

###### Use Cases
SSL certificates not only provide the assurance that data transmission to and from the website is secure, but they also provide valuable OSINT data. Information from an SSL certificate can include the issuing authority, the domain name, its validity period, and sometimes even organization details. This can be useful for verifying the authenticity of a website, understanding its security setup, or even for discovering associated subdomains or other services.

###### Useful Links
- [TLS - Wiki](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [What is SSL (via Cloudflare learning)](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
- [RFC-8446 - TLS](https://tools.ietf.org/html/rfc8446)
- [SSL Checker](https://www.sslshopper.com/ssl-checker.html)

</details>
<details>
<summary><b>DNS Records</b></summary>

<img width="300" src="https://i.ibb.co/7Q1kMwM/wc-dns.png" align="right" />

###### Description
This task involves looking up the DNS records associated with a specific domain. DNS is a system that translates human-readable domain names into IP addresses that computers use to communicate. Various types of DNS records exist, including A (address), MX (mail exchange), NS (name server), CNAME (canonical name), and TXT (text), among others.

###### Use Cases
Extracting DNS records can provide a wealth of information in an OSINT investigation. For example, A and AAAA records can disclose IP addresses associated with a domain, potentially revealing the location of servers. MX records can give clues about a domain's email provider. TXT records are often used for various administrative purposes and can sometimes inadvertently leak internal information. Understanding a domain's DNS setup can also be useful in understanding how its online infrastructure is built and managed.

###### Useful Links
- [What are DNS records? (via Cloudflare learning)](https://www.cloudflare.com/learning/dns/dns-records/)
- [DNS Record Types](https://en.wikipedia.org/wiki/List_of_DNS_record_types)
- [RFC-1035 - DNS](https://tools.ietf.org/html/rfc1035)
- [DNS Lookup (via MxToolbox)](https://mxtoolbox.com/DNSLookup.aspx)

</details>
<details>
<summary><b>Cookies</b></summary>

<img width="300" src="https://i.ibb.co/TTQ6DtP/wc-cookies.png" align="right" />

###### Description
The Cookies task involves examining the HTTP cookies set by the target website. Cookies are small pieces of data stored on the user's computer by the web browser while browsing a website. They hold a modest amount of data specific to a particular client and website, such as site preferences, the state of the user's session, or tracking information.

###### Use Cases
Cookies can disclose information about how the website tracks and interacts with its users. For instance, session cookies can reveal how user sessions are managed, and tracking cookies can hint at what kind of tracking or analytics frameworks are being used. Additionally, examining cookie policies and practices can offer insights into the site's security settings and compliance with privacy regulations.

###### Useful Links
- [HTTP Cookie Docs (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [What are Cookies (via Cloudflare Learning)](https://www.cloudflare.com/learning/privacy/what-are-cookies/)
- [Testing for Cookie Attributes (OWASP)](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes)
- [RFC-6265 - Coolies](https://tools.ietf.org/html/rfc6265)

</details>
<details>
<summary><b>Crawl Rules</b></summary>

<img width="300" src="https://i.ibb.co/KwQCjPf/wc-robots.png" align="right" />

###### Description
Robots.txt is a file found (usually) at the root of a domain, and is used to implement the Robots Exclusion Protocol (REP) to indicate which pages should be ignored by which crawlers and bots. It's good practice to avoid search engine crawlers from over-loading your site, but should not be used to keep pages out of search results (use the noindex meta tag or header instead).

###### Use Cases
It's often useful to check the robots.txt file during an investigation, as it can sometimes disclose the directories and pages that the site owner doesn't want to be indexed, potentially because they contain sensitive information, or reveal the existence of otherwise hidden or unlinked directories. Additionally, understanding crawl rules may offer insights into a website's SEO strategies.

###### Useful Links
- [Google Search Docs - Robots.txt](https://developers.google.com/search/docs/advanced/robots/intro)
- [Learn about robots.txt (via Moz.com)](https://moz.com/learn/seo/robotstxt)
- [RFC-9309 -  Robots Exclusion Protocol](https://datatracker.ietf.org/doc/rfc9309/)
- [Robots.txt - wiki](https://en.wikipedia.org/wiki/Robots_exclusion_standard)

</details>
<details>
<summary><b>Headers</b></summary>

<img width="300" src="https://i.ibb.co/t3xcwP1/wc-headers.png" align="right" />

###### Description
The Headers task involves extracting and interpreting the HTTP headers sent by the target website during the request-response cycle. HTTP headers are key-value pairs sent at the start of an HTTP response, or before the actual data. Headers contain important directives for how to handle the data being transferred, including cache policies, content types, encoding, server information, security policies, and more.

###### Use Cases
Analyzing HTTP headers can provide significant insights in an OSINT investigation. Headers can reveal specific server configurations, chosen technologies, caching directives, and various security settings. This information can help to determine a website's underlying technology stack, server-side security measures, potential vulnerabilities, and general operational practices.

###### Useful Links
- [HTTP Headers - Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [RFC-7231 Section 7 - Headers](https://datatracker.ietf.org/doc/html/rfc7231#section-7)
- [List of header response fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)

</details>
<details>
<summary><b>Quality Metrics</b></summary>

<img width="300" src="https://i.ibb.co/Kqg8rx7/wc-quality.png" align="right" />

###### Description
Using Lighthouse, the Quality Metrics task measures the performance, accessibility, best practices, and SEO of the target website. This returns a simple checklist of 100 core metrics, along with a score for each category, to gauge the overall quality of a given site.

###### Use Cases
Useful for assessing a site's technical health, SEO issues, identify vulnerabilities, and ensure compliance with standards.

###### Useful Links
- [Lighthouse Docs](https://developer.chrome.com/docs/lighthouse/)
- [Google Page Speed Tools](https://developers.google.com/speed)
- [W3 Accessibility Tools](https://www.w3.org/WAI/test-evaluate/)
- [Google Search Console](https://search.google.com/search-console)
- [SEO Checker](https://www.seobility.net/en/seocheck/)
- [PWA Builder](https://www.pwabuilder.com/)

</details>
<details>
<summary><b>Server Location</b></summary>

<img width="300" src="https://i.ibb.co/cXH2hfR/wc-location.png" align="right" />

###### Description
The Server Location task determines the physical location of the server hosting a given website based on its IP address. This is done by looking up the IP in a location database, which maps the IP to a lat + long of known data centers and ISPs. From the latitude and longitude, it's then possible to show additional contextual info, like a pin on the map, along with address, flag, time zone, currency, etc.

###### Use Cases
Knowing the server location is a good first step in better understanding a website. For site owners this aids in optimizing content delivery, ensuring compliance with data residency requirements, and identifying potential latency issues that may impact user experience in specific geographical regions. And for security researcher, assess the risk posed by specific regions or jurisdictions regarding cyber threats and regulations.

###### Useful Links
- [IP Locator](https://geobytes.com/iplocator/)
- [Internet Geolocation - Wiki](https://en.wikipedia.org/wiki/Internet_geolocation)

</details>
<details>
<summary><b>Associated Hosts</b></summary>

<img width="300" src="https://i.ibb.co/25j1sT7/wc-hosts.png" align="right" />

###### Description
This task involves identifying and listing all domains and subdomains (hostnames) that are associated with the website's primary domain. This process often involves DNS enumeration to discover any linked domains and hostnames, as we
... [TRUNCATED]
```

### File: .github\screenshots\README.md
```md
![Screenshot](https://raw.githubusercontent.com/Lissy93/web-check/HEAD/.github/screenshots/web-check-screenshot3.png)

```

### File: chrome-extension-api.md
```md
---
id: chrome-extension-api
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:25.594584
---

# Chrome Extension API — Knowledge Base

## Description
Technical reference for Manifest V3 extension development, focusing on bookmarks, storage, and service worker best practices for the Smart Bookmark Manager.

## Manifest V3 Key Differences

### Service Worker (replaces background page)
```js
// manifest.json
"background": {
  "service_worker": "src/background/worker.js"
}
// NOT: "scripts": ["background.js"]
```

### Storage (use chrome.storage, not localStorage)
```js
// localStorage does NOT work in service workers
// Use chrome.storage.local instead
await chrome.storage.local.set({ key: value });
const data = await chrome.storage.local.get('key');
```

### Bookmarks API Quick Reference
```js
// Get full tree
const [tree] = await chrome.bookmarks.getTree();

// Root nodes
tree.children[0] = Bookmarks Bar (id: "1")
tree.children[1] = Other Bookmarks (id: "2")

// Create
await chrome.bookmarks.create({ parentId: "1", title, url });

// Listen for changes
chrome.bookmarks.onCreated.addListener((id, bookmark) => {});
chrome.bookmarks.onRemoved.addListener((id, removeInfo) => {});
chrome.bookmarks.onChanged.addListener((id, changeInfo) => {});
chrome.bookmarks.onMoved.addListener((id, moveInfo) => {});
```

### Favicon API
```js
// Get favicon URL
const favIconUrl = `chrome-extension://${chrome.runtime.id}/_favicon/?pageUrl=${encodeURIComponent(url)}&size=16`;
```

### Action API (popup trigger)
```js
// In popup.js - no special setup needed
// Extension icon click → opens popup.html automatically
```

## Common Pitfalls

1. **Service Worker sleep**: SW can be killed by Chrome. Don't rely on in-memory state.
2. **CSP restrictions**: No inline scripts, no remote scripts.
3. **localStorage**: Not shared between popup and SW. Use chrome.storage.
4. **Permissions**: Request minimal permissions to pass Chrome Web Store review.
5. **Async APIs**: Always use await/Promise, never callbacks for modern code.

## Debugging Tips
```
chrome://extensions/ → Enable Developer mode → Inspect popup
chrome://bookmarks/ → Test bookmark operations
Ctrl+Shift+J → Extension errors in console
```

```

### File: ki_2026_03_22_agent_browser2.md
```md
---
id: KI-2026-03-22-agent-browser2
source: https://github.com/vercel-labs/agent-browser
type: REFERENCE
domain: ['web', 'browser-agent']
dept: engineering
agents: ['web_intelligence']
stars: 1k
security_gate: PASS (community_vetted)
compatible_ai_os: True
created: 2026-03-22T23:02:23.338520
---

# Vercel Agent Browser

> Playwright-based browser control for AI agents (Node.js/TypeScript)

**Source:** [https://github.com/vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)  
**Stars:** 1k | **Type:** REFERENCE | **Dept:** engineering  
**OmniClaw Compatible:** ✅ Compatible

## Phase 3 Classification
- **knowledge_type:** `REFERENCE`
- **domains:** web, browser-agent
- **target_dept:** engineering
- **relevant_agents:** web_intelligence
- **security_gate:** PASS — community_vetted

## OmniClaw Notes
REFERENCE — JS only. Study alongside scrapling MCP for browser automation patterns.

## Integration
📖 KI entry only — no plugin clone needed

---
*Ingested: 2026-03-22T23:02:23.338520 via knowledge-ingest.md Phase 1-3*

```

### File: ki_2026_03_22_scrapling_tool.md
```md
---
id: KI-2026-03-22-scrapling-tool
source: https://github.com/D4Vinci/Scrapling
type: TOOL
domain: ['web', 'scraping']
dept: engineering
agents: []
stars: 3k
security_gate: PASS (community_vetted)
compatible_ai_os: True
created: 2026-03-22T23:02:23.338520
---

# Scrapling (see plugin)

> Already in plugins/scrapling/ — MCP server mode

**Source:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)  
**Stars:** 3k | **Type:** TOOL | **Dept:** engineering  
**OmniClaw Compatible:** ✅ Compatible

## Phase 3 Classification
- **knowledge_type:** `TOOL`
- **domains:** web, scraping
- **target_dept:** engineering
- **relevant_agents:** _(none assigned)_
- **security_gate:** PASS — community_vetted

## OmniClaw Notes
INSTALLED. MCP endpoint for Claude agents.

## Integration
📖 KI entry only — no plugin clone needed

---
*Ingested: 2026-03-22T23:02:23.338520 via knowledge-ingest.md Phase 1-3*

```

### File: server.js
```js

import fs from 'fs';
import path from 'path';
import cors from 'cors';
import dotenv from 'dotenv';
import express from 'express';
import rateLimit from 'express-rate-limit';
import historyApiFallback from 'connect-history-api-fallback';

// Load environment variables from .env file
dotenv.config();

// Create the Express app
const app = express();

const __filename = new URL(import.meta.url).pathname;
const __dirname = path.dirname(__filename);

const port = process.env.PORT || 3000; // The port to run the server on
const API_DIR = '/api'; // Name of the dir containing the lambda functions
const dirPath = path.join(__dirname, API_DIR); // Path to the lambda functions dir
const guiPath = path.join(__dirname, 'dist', 'client');
const placeholderFilePath = path.join(__dirname, 'public', 'placeholder.html');
const handlers = {}; // Will store list of API endpoints
process.env.WC_SERVER = 'true'; // Tells middleware to return in non-lambda mode

// Enable CORS
app.use(cors({
  origin: process.env.API_CORS_ORIGIN || '*',
}));

// Define max requests within each time frame
const limits = [
  { timeFrame: 10 * 60, max: 100, messageTime: '10 minutes' },
  { timeFrame: 60 * 60, max: 250, messageTime: '1 hour' },
  { timeFrame: 12 * 60 * 60, max: 500, messageTime: '12 hours' },
];

// Construct a message to be returned if the user has been rate-limited
const makeLimiterResponseMsg = (retryAfter) => {
  const why = 'This keeps the service running smoothly for everyone. '
  + 'You can get around these limits by running your own instance of Web Check.';
  return `You've been rate-limited, please try again in ${retryAfter} seconds.\n${why}`;
};

// Create rate limiters for each time frame
const limiters = limits.map(limit => rateLimit({
  windowMs: limit.timeFrame * 1000,
  max: limit.max,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: makeLimiterResponseMsg(limit.messageTime) }
}));

// If rate-limiting enabled, then apply the limiters to the /api endpoint
if (process.env.API_ENABLE_RATE_LIMIT === 'true') {
  app.use(API_DIR, limiters);
}

// Read and register each API function as an Express routes
fs.readdirSync(dirPath, { withFileTypes: true })
  .filter(dirent => dirent.isFile() && dirent.name.endsWith('.js'))
  .forEach(async dirent => {
    const routeName = dirent.name.split('.')[0];
    const route = `${API_DIR}/${routeName}`;
    // const handler = require(path.join(dirPath, dirent.name));

    const handlerModule = await import(path.join(dirPath, dirent.name));
    const handler = handlerModule.default || handlerModule;
    handlers[route] = handler;

    app.get(route, async (req, res) => {
      try {
        await handler(req, res);
      } catch (err) {
        res.status(500).json({ error: err.message });
      }
    });
  });

const renderPlaceholderPage = async (res, msgId, logs) => {
  const errorMessages = {
    notCompiled: 'Looks like the GUI app has not yet been compiled.<br />'
    + 'Run <code>yarn build</code> to continue, then restart the server.',
    notCompiledSsrHandler: 'Server-side rendering failed to initiate, as SSR handler not found.<br />'
    + 'This can be fixed by running <code>yarn build</code>, then restarting the server.<br />',
    disabledGui:  'Web-Check API is up and running!<br />Access the endpoints at '
    + `<a href="${API_DIR}"><code>${API_DIR}</code></a>`,
  };
  const logOutput = logs ? `<div class="logs"><code>${logs}</code></div>` : '';
  const errorMessage = (errorMessages[msgId] || 'An mystery error occurred.') + logOutput;
  const placeholderContent = await fs.promises.readFile(placeholderFilePath, 'utf-8');
  const htmlContent = placeholderContent.replace('<!-- CONTENT -->', errorMessage );
  res.status(500).send(htmlContent);
};

// Create a single API endpoint to execute all lambda functions
app.get(API_DIR, async (req, res) => {
  const results = {};
  const { url } = req.query;
  const maxExecutionTime = process.env.API_TIMEOUT_LIMIT || 20000;

  const executeHandler = async (handler, req) => {
    return new Promise(async (resolve, reject) => {
      try {
        const mockRes = {
          status: () => mockRes,
          json: (body) => resolve({ body }),
        };
        await handler({ ...req, query: { url } }, mockRes);
      } catch (err) {
        reject(err);
      }
    });
  };

  const timeout = (ms, jobName = null) => {
    return new Promise((_, reject) => {
      setTimeout(() => {
        reject(new Error(
          `Timed out after ${ms/1000} seconds${jobName ? `, when executing ${jobName}` : ''}`
        ));
      }, ms);
    });
  };

  const handlerPromises = Object.entries(handlers).map(async ([route, handler]) => {
    const routeName = route.replace(`${API_DIR}/`, '');

    try {
      const result = await Promise.race([
        executeHandler(handler, req, res),
        timeout(maxExecutionTime, routeName)
      ]);
      results[routeName] = result.body;
    } catch (err) {
      results[routeName] = { error: err.message };
    }
  });

  await Promise.all(handlerPromises);
  res.json(results);
});

// Skip the marketing homepage, for self-hosted users
app.use((req, res, next) => {
  if (req.path === '/' && process.env.BOSS_SERVER !== 'true' && !process.env.DISABLE_GUI) {
    req.url = '/check';
  }
  next();
});

// Serve up the GUI - if build dir exists, and GUI feature enabled
if (process.env.DISABLE_GUI && process.env.DISABLE_GUI !== 'false') {
  app.get('/', async (req, res) => {
    renderPlaceholderPage(res, 'disabledGui');
  });
} else if (!fs.existsSync(guiPath)) {
  app.get('/', async (req, res) => {
    renderPlaceholderPage(res, 'notCompiled');
  });
} else { // GUI enabled, and build files present, let's go!!
  app.use(express.static('dist/client/'));
  app.use(async (req, res, next) => {
    const ssrHandlerPath = path.join(__dirname, 'dist', 'server', 'entry.mjs');
    import(ssrHandlerPath).then(({ handler: ssrHandler }) => {
      ssrHandler(req, res, next);
    }).catch(async err => {
      renderPlaceholderPage(res, 'notCompiledSsrHandler', err.message);
    });
  });  
}

// Handle SPA routing
app.use(historyApiFallback({
  rewrites: [
    { from: new RegExp(`^${API_DIR}/.*$`), to: (context) => context.parsedUrl.path },
    { from: /^.*$/, to: '/index.html' }
  ]
}));

// Anything left unhandled (which isn't an API endpoint), return a 404
app.use((req, res, next) => {
  if (!req.path.startsWith(`${API_DIR}/`)) {
    res.status(404).sendFile(path.join(__dirname, 'public', 'error.html'));
  } else {
    next();
  }
});

// Print nice welcome message to user
const printMessage = () => {
  console.log(
    `\x1b[36m\n` +
    '    __      __   _         ___ _           _   \n' +
    '    \\ \\    / /__| |__ ___ / __| |_  ___ __| |__\n' +
    '     \\ \\/\\/ / -_) \'_ \\___| (__| \' \\/ -_) _| / /\n' +
    '      \\_/\\_/\\___|_.__/    \\___|_||_\\___\\__|_\\_\\\n' +
    `\x1b[0m\n`,
    `\x1b[1m\x1b[32m🚀 Web-Check is up and running at http://localhost:${port} \x1b[0m\n\n`,
    `\x1b[2m\x1b[36m🛟 For documentation and support, visit the GitHub repo: ` +
    `https://github.com/lissy93/web-check \n`,
    `💖 Found Web-Check useful? Consider sponsoring us on GitHub ` +
    `to help fund maintenance & development.\x1b[0m`
  );
};

// Create server
app.listen(port, () => {
  printMessage();
});


```

### File: svelte.config.js
```js
import { vitePreprocess } from '@astrojs/svelte';

export default {
	preprocess: vitePreprocess(),
}

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ES2020",
    "moduleResolution": "node",
    "allowImportingTsExtensions": true,
    "plugins": [
      {
        "name": "@astrojs/ts-plugin"
      },
    ],
    "lib": [
      "DOM",
      "DOM.Iterable",
      "ES2020"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "jsxImportSource": "react",
    "baseUrl": "src",
    "paths": {
      "@/*": ["*"],
      "@components/*": ["components/*"],
      "@layouts/*": ["layouts/*"],
      "@pages/*": ["pages/*"],
      "@styles/*": ["styles/*"],
      "@assets/*": ["assets/*"],
    }
  },
  "include": [
    "src"
  ]
}

```

### File: vercel.json
```json
{
  "version": 2,
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/$1.js"
    }
  ],
  "functions": {
    "api/*.js": {
      "maxDuration": 10
    }
  },
  "env": {
    "PLATFORM": "vercel",
    "CI": "false",
    "CHROME_PATH": "/usr/bin/chromium",
    "NODE_VERSION": "21.x",
    "GOOGLE_CLOUD_API_KEY": "",
    "BUILT_WITH_API_KEY": "",
    "REACT_APP_SHODAN_API_KEY": "",
    "REACT_APP_WHO_API_KEY": ""
  },
  "build": {
    "env": {
      "PLATFORM": "vercel"
    }
  }
}

```

### File: vite.config.js
```js
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [
    react({
      jsxImportSource: '@emotion/react',
      babel: {
        plugins: ['babel-plugin-styled-components'],
      },
    }),
  ],
});

```

### File: api\archives.js
```js
import axios from 'axios';
import middleware from './_common/middleware.js';

const convertTimestampToDate = (timestamp) => {
  const [year, month, day, hour, minute, second] = [
    timestamp.slice(0, 4),
    timestamp.slice(4, 6) - 1,
    timestamp.slice(6, 8),
    timestamp.slice(8, 10),
    timestamp.slice(10, 12),
    timestamp.slice(12, 14),
  ].map(num => parseInt(num, 10));

  return new Date(year, month, day, hour, minute, second);
}

const countPageChanges = (results) => {
  let prevDigest = null;
  return results.reduce((acc, curr) => {
    if (curr[2] !== prevDigest) {
      prevDigest = curr[2];
      return acc + 1;
    }
    return acc;
  }, -1);
}

const getAveragePageSize = (scans) => {
    const totalSize = scans.map(scan => parseInt(scan[3], 10)).reduce((sum, size) => sum + size, 0);
    return Math.round(totalSize / scans.length);
};

const getScanFrequency = (firstScan, lastScan, totalScans, changeCount) => {
  const formatToTwoDecimal = num => parseFloat(num.toFixed(2));

  const dayFactor = (lastScan - firstScan) / (1000 * 60 * 60 * 24);  
  const daysBetweenScans = formatToTwoDecimal(dayFactor / totalScans);
  const daysBetweenChanges = formatToTwoDecimal(dayFactor / changeCount);
  const scansPerDay = formatToTwoDecimal((totalScans - 1) / dayFactor);
  const changesPerDay = formatToTwoDecimal(changeCount / dayFactor);
  return {
    daysBetweenScans,
    daysBetweenChanges,
    scansPerDay,
    changesPerDay,
  };
};

const wayBackHandler = async (url) => {
  const cdxUrl = `https://web.archive.org/cdx/search/cdx?url=${url}&output=json&fl=timestamp,statuscode,digest,length,offset`;

  try {
    const { data } = await axios.get(cdxUrl);
    
    // Check there's data
    if (!data || !Array.isArray(data) || data.length <= 1) {
      return { skipped: 'Site has never before been archived via the Wayback Machine' };
    }

    // Remove the header row
    data.shift();

    // Process and return the results
    const firstScan = convertTimestampToDate(data[0][0]);
    const lastScan = convertTimestampToDate(data[data.length - 1][0]);
    const totalScans = data.length;
    const changeCount = countPageChanges(data);
    return {
      firstScan,
      lastScan,
      totalScans,
      changeCount,
      averagePageSize: getAveragePageSize(data),
      scanFrequency: getScanFrequency(firstScan, lastScan, totalScans, changeCount),
      scans: data,
      scanUrl: url,
    };
  } catch (err) {
    return { error: `Error fetching Wayback data: ${err.message}` };
  }
};

export const handler = middleware(wayBackHandler);
export default handler;

```

### File: api\block-lists.js
```js
import dns from 'dns';
import { URL } from 'url';
import middleware from './_common/middleware.js';

const DNS_SERVERS = [
  { name: 'AdGuard', ip: '176.103.130.130' },
  { name: 'AdGuard Family', ip: '176.103.130.132' },
  { name: 'CleanBrowsing Adult', ip: '185.228.168.10' },
  { name: 'CleanBrowsing Family', ip: '185.228.168.168' },
  { name: 'CleanBrowsing Security', ip: '185.228.168.9' },
  { name: 'CloudFlare', ip: '1.1.1.1' },
  { name: 'CloudFlare Family', ip: '1.1.1.3' },
  { name: 'Comodo Secure', ip: '8.26.56.26' },
  { name: 'Google DNS', ip: '8.8.8.8' },
  { name: 'Neustar Family', ip: '156.154.70.3' },
  { name: 'Neustar Protection', ip: '156.154.70.2' },
  { name: 'Norton Family', ip: '199.85.126.20' },
  { name: 'OpenDNS', ip: '208.67.222.222' },
  { name: 'OpenDNS Family', ip: '208.67.222.123' },
  { name: 'Quad9', ip: '9.9.9.9' },
  { name: 'Yandex Family', ip: '77.88.8.7' },
  { name: 'Yandex Safe', ip: '77.88.8.88' },
];
const knownBlockIPs = [
  '146.112.61.106', // OpenDNS
  '185.228.168.10', // CleanBrowsing
  '8.26.56.26',     // Comodo
  '9.9.9.9',        // Quad9
  '208.69.38.170',  // Some OpenDNS IPs
  '208.69.39.170',  // Some OpenDNS IPs
  '208.67.222.222', // OpenDNS
  '208.67.222.123', // OpenDNS FamilyShield
  '199.85.126.10',  // Norton
  '199.85.126.20',  // Norton Family
  '156.154.70.22',  // Neustar
  '77.88.8.7',      // Yandex
  '77.88.8.8',      // Yandex
  '::1',              // Localhost IPv6
  '2a02:6b8::feed:0ff', // Yandex DNS
  '2a02:6b8::feed:bad', // Yandex Safe
  '2a02:6b8::feed:a11', // Yandex Family
  '2620:119:35::35',    // OpenDNS
  '2620:119:53::53',    // OpenDNS FamilyShield
  '2606:4700:4700::1111', // Cloudflare
  '2606:4700:4700::1001', // Cloudflare
  '2001:4860:4860::8888', // Google DNS
  '2a0d:2a00:1::',        // AdGuard
  '2a0d:2a00:2::'         // AdGuard Family
];

const isDomainBlocked = async (domain, serverIP) => {
  return new Promise((resolve) => {
    dns.resolve4(domain, { server: serverIP }, (err, addresses) => {
      if (!err) {
        if (addresses.some(addr => knownBlockIPs.includes(addr))) {
          resolve(true);
          return;
        }
        resolve(false);
        return;
      }

      dns.resolve6(domain, { server: serverIP }, (err6, addresses6) => {
        if (!err6) {
          if (addresses6.some(addr => knownBlockIPs.includes(addr))) {
            resolve(true);
            return;
          }
          resolve(false);
          return;
        }
        if (err6.code === 'ENOTFOUND' || err6.code === 'SERVFAIL') {
          resolve(true);
        } else {
          resolve(false);
        }
      });
    });
  });
};

const checkDomainAgainstDnsServers = async (domain) => {
  let results = [];

  for (let server of DNS_SERVERS) {
    const isBlocked = await isDomainBlocked(domain, server.ip);
    results.push({
      server: server.name,
      serverIp: server.ip,
      isBlocked,
    });
  }

  return results;
};

export const blockListHandler = async (url) => {
  const domain = new URL(url).hostname;
  const results = await checkDomainAgainstDnsServers(domain);
  return { blocklists: results };
};

export const handler = middleware(blockListHandler);
export default handler;


```

### File: api\carbon.js
```js
import https from 'https';
import middleware from './_common/middleware.js';

const carbonHandler = async (url) => {

  // First, get the size of the website's HTML
  const getHtmlSize = (url) => new Promise((resolve, reject) => {
    https.get(url, res => {
      let data = '';
      res.on('data', chunk => {
        data += chunk;
      });
      res.on('end', () => {
        const sizeInBytes = Buffer.byteLength(data, 'utf8');
        resolve(sizeInBytes);
      });
    }).on('error', reject);
  });

  try {
    const sizeInBytes = await getHtmlSize(url);
    const apiUrl = `https://api.websitecarbon.com/data?bytes=${sizeInBytes}&green=0`;

    // Then use that size to get the carbon data
    const carbonData = await new Promise((resolve, reject) => {
      https.get(apiUrl, res => {
        let data = '';
        res.on('data', chunk => {
          data += chunk;
        });
        res.on('end', () => {
          // Check if response looks like HTML (e.g., Cloudflare challenge page)
          const trimmedData = data.trim();
          if (trimmedData.startsWith('<!DOCTYPE') || trimmedData.startsWith('<html') || trimmedData.startsWith('<')) {
            reject(new Error('WebsiteCarbon API returned HTML instead of JSON. This may be due to Cloudflare protection when running from a datacenter IP.'));
            return;
          }
          try {
            resolve(JSON.parse(data));
          } catch (parseError) {
            reject(new Error(`Failed to parse WebsiteCarbon API response as JSON: ${parseError.message}`));
          }
        });
      }).on('error', reject);
    });

    if (!carbonData.statistics || (carbonData.statistics.adjustedBytes === 0 && carbonData.statistics.energy === 0)) {
      return {
        statusCode: 200,
        body: JSON.stringify({ skipped: 'Not enough info to get carbon data' }),
      };
    }

    carbonData.scanUrl = url;
    return carbonData;
  } catch (error) {
    throw new Error(`Error: ${error.message}`);
  }
};

export const handler = middleware(carbonHandler);
export default handler;

```

### File: api\cookies.js
```js
import axios from 'axios';
import puppeteer from 'puppeteer';
import middleware from './_common/middleware.js';

const getPuppeteerCookies = async (url) => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  try {
    const page = await browser.newPage();
    const navigationPromise = page.goto(url, { waitUntil: 'networkidle2' });
        const timeoutPromise = new Promise((_, reject) => 
      setTimeout(() => reject(new Error('Puppeteer took too long!')), 3000)
    );
    await Promise.race([navigationPromise, timeoutPromise]);
    return await page.cookies();
  } finally {
    await browser.close();
  }
};

const cookieHandler = async (url) => {
  let headerCookies = null;
  let clientCookies = null;

  try {
    const response = await axios.get(url, {
      withCredentials: true,
      maxRedirects: 5,
    });
    headerCookies = response.headers['set-cookie'];
  } catch (error) {
    if (error.response) {
      return { error: `Request failed with status ${error.response.status}: ${error.message}` };
    } else if (error.request) {
      return { error: `No response received: ${error.message}` };
    } else {
      return { error: `Error setting up request: ${error.message}` };
    }
  }

  try {
    clientCookies = await getPuppeteerCookies(url);
  } catch (_) {
    clientCookies = null;
  }

  if (!headerCookies && (!clientCookies || clientCookies.length === 0)) {
    return { skipped: 'No cookies' };
  }

  return { headerCookies, clientCookies };
};

export const handler = middleware(cookieHandler);
export default handler;

```

### File: api\dns-server.js
```js
import { promises as dnsPromises, lookup } from 'dns';
import axios from 'axios';
import middleware from './_common/middleware.js';

const dnsHandler = async (url) => {
  try {
    const domain = url.replace(/^(?:https?:\/\/)?/i, "");
    const addresses = await dnsPromises.resolve4(domain);
    const results = await Promise.all(addresses.map(async (address) => {
      const hostname = await dnsPromises.reverse(address).catch(() => null);
      let dohDirectSupports = false;
      try {
        await axios.get(`https://${address}/dns-query`);
        dohDirectSupports = true;
      } catch (error) {
        dohDirectSupports = false;
      }
      return {
        address,
        hostname,
        dohDirectSupports,
      };
    }));

    // let dohMozillaSupport = false;
    // try {
    //   const mozillaList = await axios.get('https://firefox.settings.services.mozilla.com/v1/buckets/security-state/collections/onecrl/records');
    //   dohMozillaSupport = results.some(({ hostname }) => mozillaList.data.data.some(({ id }) => id.includes(hostname)));
    // } catch (error) {
    //   console.error(error);
    // }

    return {
      domain,
      dns: results,
      // dohMozillaSupport,
    };
  } catch (error) {
    throw new Error(`An error occurred while resolving DNS. ${error.message}`); // This will be caught and handled by the commonMiddleware
  }
};


export const handler = middleware(dnsHandler);
export default handler;


```

### File: api\dns.js
```js
import dns from 'dns';
import util from 'util';
import middleware from './_common/middleware.js';

const dnsHandler = async (url) => {
  let hostname = url;

  // Handle URLs by extracting hostname
  if (hostname.startsWith('http://') || hostname.startsWith('https://')) {
    hostname = new URL(hostname).hostname;
  }

  try {
    const lookupPromise = util.promisify(dns.lookup);
    const resolve4Promise = util.promisify(dns.resolve4);
    const resolve6Promise = util.promisify(dns.resolve6);
    const resolveMxPromise = util.promisify(dns.resolveMx);
    const resolveTxtPromise = util.promisify(dns.resolveTxt);
    const resolveNsPromise = util.promisify(dns.resolveNs);
    const resolveCnamePromise = util.promisify(dns.resolveCname);
    const resolveSoaPromise = util.promisify(dns.resolveSoa);
    const resolveSrvPromise = util.promisify(dns.resolveSrv);
    const resolvePtrPromise = util.promisify(dns.resolvePtr);

    const [a, aaaa, mx, txt, ns, cname, soa, srv, ptr] = await Promise.all([
      lookupPromise(hostname),
      resolve4Promise(hostname).catch(() => []), // A record
      resolve6Promise(hostname).catch(() => []), // AAAA record
      resolveMxPromise(hostname).catch(() => []), // MX record
      resolveTxtPromise(hostname).catch(() => []), // TXT record
      resolveNsPromise(hostname).catch(() => []), // NS record
      resolveCnamePromise(hostname).catch(() => []), // CNAME record
      resolveSoaPromise(hostname).catch(() => []), // SOA record
      resolveSrvPromise(hostname).catch(() => []), // SRV record
      resolvePtrPromise(hostname).catch(() => [])  // PTR record
    ]);

    return {
      A: a,
      AAAA: aaaa,
      MX: mx,
      TXT: txt,
      NS: ns,
      CNAME: cname,
      SOA: soa,
      SRV: srv,
      PTR: ptr
    };
  } catch (error) {
    throw new Error(error.message);
  }
};

export const handler = middleware(dnsHandler);
export default handler;

```

### File: api\dnssec.js
```js
import https from 'https';
import middleware from './_common/middleware.js';

const dnsSecHandler = async (domain) => {
  const dnsTypes = ['DNSKEY', 'DS', 'RRSIG'];
  const records = {};

  for (const type of dnsTypes) {
    const options = {
      hostname: 'dns.google',
      path: `/resolve?name=${encodeURIComponent(domain)}&type=${type}`,
      method: 'GET',
      headers: {
        'Accept': 'application/dns-json'
      }
    };

    try {
      const dnsResponse = await new Promise((resolve, reject) => {
        const req = https.request(options, res => {
          let data = '';
          
          res.on('data', chunk => {
            data += chunk;
          });

          res.on('end', () => {
            try {
              resolve(JSON.parse(data));
            } catch (error) {
              reject(new Error('Invalid JSON response'));
            }
          });

          res.on('error', error => {
            reject(error);
          });
        });

        req.end();
      });

      if (dnsResponse.Answer) {
        records[type] = { isFound: true, answer: dnsResponse.Answer, response: dnsResponse.Answer };
      } else {
        records[type] = { isFound: false, answer: null, response: dnsResponse };
      }
    } catch (error) {
      throw new Error(`Error fetching ${type} record: ${error.message}`); // This will be caught and handled by the commonMiddleware
    }
  }

  return records;
};

export const handler = middleware(dnsSecHandler);
export default handler;

```

### File: api\features.js
```js
import https from 'https';
import middleware from './_common/middleware.js';

const featuresHandler = async (url) => {
  const apiKey = process.env.BUILT_WITH_API_KEY;

  if (!url) {
    throw new Error('URL query parameter is required');
  }

  if (!apiKey) {
    throw new Error('Missing BuiltWith API key in environment variables');
  }

  const apiUrl = `https://api.builtwith.com/free1/api.json?KEY=${apiKey}&LOOKUP=${encodeURIComponent(url)}`;

  try {
    const response = await new Promise((resolve, reject) => {
      const req = https.get(apiUrl, res => {
        let data = '';

        res.on('data', chunk => {
          data += chunk;
        });

        res.on('end', () => {
          if (res.statusCode >= 200 && res.statusCode <= 299) {
            resolve(data);
          } else {
            reject(new Error(`Request failed with status code: ${res.statusCode}`));
          }
        });
      });

      req.on('error', error => {
        reject(error);
      });

      req.end();
    });

    return response;
  } catch (error) {
    throw new Error(`Error making request: ${error.message}`);
  }
};

export const handler = middleware(featuresHandler);
export default handler;

```

### File: api\firewall.js
```js
import axios from 'axios';
import middleware from './_common/middleware.js';

const hasWaf = (waf) => {
  return {
    hasWaf: true, waf,
  }
};

const firewallHandler = async (url) => {
  const fullUrl = url.startsWith('http') ? url : `http://${url}`;
  
  try {
    const response = await axios.get(fullUrl);

    const headers = response.headers;

    if (headers['server'] && headers['server'].includes('cloudflare')) {
      return hasWaf('Cloudflare');
    }

    if (headers['x-powered-by'] && headers['x-powered-by'].includes('AWS Lambda')) {
      return hasWaf('AWS WAF');
    }

    if (headers['server'] && headers['server'].includes('AkamaiGHost')) {
      return hasWaf('Akamai');
    }

    if (headers['server'] && headers['server'].includes('Sucuri')) {
      return hasWaf('Sucuri');
    }

    if (headers['server'] && headers['server'].includes('BarracudaWAF')) {
      return hasWaf('Barracuda WAF');
    }

    if (headers['server'] && (headers['server'].includes('F5 BIG-IP') || headers['server'].includes('BIG-IP'))) {
      return hasWaf('F5 BIG-IP');
    }

    if (headers['x-sucuri-id'] || headers['x-sucuri-cache']) {
      return hasWaf('Sucuri CloudProxy WAF');
    }

    if (headers['server'] && headers['server'].includes('FortiWeb')) {
      return hasWaf('Fortinet FortiWeb WAF');
    }

    if (headers['server'] && headers['server'].includes('Imperva')) {
      return hasWaf('Imperva SecureSphere WAF');
    }

    if (headers['x-protected-by'] && headers['x-protected-by'].includes('Sqreen')) {
      return hasWaf('Sqreen');
    }

    if (headers['x-waf-event-info']) {
      return hasWaf('Reblaze WAF');
    }

    if (headers['set-cookie'] && headers['set-cookie'].includes('_citrix_ns_id')) {
      return hasWaf('Citrix NetScaler');
    }

    if (headers['x-denied-reason'] || headers['x-wzws-requested-method']) {
      return hasWaf('WangZhanBao WAF');
    }

    if (headers['x-webcoment']) {
      return hasWaf('Webcoment Firewall');
    }

    if (headers['server'] && headers['server'].includes('Yundun')) {
      return hasWaf('Yundun WAF');
    }

    if (headers['x-yd-waf-info'] || headers['x-yd-info']) {
      return hasWaf('Yundun WAF');
    }

    if (headers['server'] && headers['server'].includes('Safe3WAF')) {
      return hasWaf('Safe3 Web Application Firewall');
    }

    if (headers['server'] && headers['server'].includes('NAXSI')) {
      return hasWaf('NAXSI WAF');
    }

    if (headers['x-datapower-transactionid']) {
      return hasWaf('IBM WebSphere DataPower');
    }

    if (headers['server'] && headers['server'].includes('QRATOR')) {
      return hasWaf('QRATOR WAF');
    }

    if (headers['server'] && headers['server'].includes('ddos-guard')) {
      return hasWaf('DDoS-Guard WAF');
    }

    return {
      hasWaf: false,
    }
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};

export const handler = middleware(firewallHandler);
export default handler;

```

### File: api\get-ip.js
```js
import dns from 'dns';
import middleware from './_common/middleware.js';

const lookupAsync = (address) => {
  return new Promise((resolve, reject) => {
    dns.lookup(address, (err, ip, family) => {
      if (err) {
        reject(err);
      } else {
        resolve({ ip, family });
      }
    });
  });
};

const ipHandler = async (url) => {
  const address = url.replaceAll('https://', '').replaceAll('http://', '');
  return await lookupAsync(address);
};


export const handler = middleware(ipHandler);
export default handler;

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
