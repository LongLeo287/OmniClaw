---
id: github.com-pixlcore-xyplug-bluesky-bc26320d-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.215361
---

# KNOWLEDGE EXTRACT: github.com_pixlcore_xyplug-bluesky_bc26320d
> **Extracted on:** 2026-04-01 14:59:51
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524212/github.com_pixlcore_xyplug-bluesky_bc26320d

---

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
<p align="center"><img src="logo.png" height="128" alt="Bluesky"/></p>
<h1 align="center">Bluesky Social Plugin</h1>

Bluesky event plugin for the [xyOps Workflow Automation System](https://xyops.io). This plugin is a pure Node.js implementation and talks directly to the Bluesky XRPC endpoints.

## Quick Start

Get your Bluesky app password at: https://bsky.app/settings/app-passwords

You will need the following environment variables (recommend storing them in a secret vault):

| Environment Variable | Description |
|----------------------|-------------|
| `BLUESKY_IDENTIFIER` | Your Bluesky identifier, e.g. `your-handle.bsky.social`. |
| `BLUESKY_APP_PASSWORD` | Your Bluesky App Password, which you can obtain [here](https://bsky.app/settings/app-passwords). |
| `BLUESKY_SERVICE_URL` | Optional service URL (defaults to `https://bsky.social`). |

## Requirements

- `npx`
- `git`

## What this plugin does

- Authenticates to Bluesky.
- Reads posts, profiles, followers, and timelines.
- Sends posts, images, and videos.
- Likes, reposts, follows, and mutes users.
- Returns the Bluesky API response as job output data.

### File Inputs

For `send_image`, `send_images`, and `send_video`, pass files into the xyOps job.

## Tools

All tools are selected via the Toolset parameter in `xyops.json`. When a tool is selected, its fields are flattened into `params` at the top level.

Notes on common fields:
- `cursor` is an opaque pagination token returned by Bluesky. Treat it as a string and pass it back verbatim to fetch the next page. Leave it empty for the first page.
- `limit` is the maximum number of items to return. Where applicable, Bluesky accepts `1-100`. If you leave it empty or `0`, the server default is used (often 50).

### Check Auth Status

Check if the current session is authenticated.  No parameters are used.

### Get Profile

Get a user profile. If you omit the handle, the authenticated user is used.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | No | Handle or DID to fetch (e.g. `user.bsky.social` or `did:plc:...`). | Current user |

### Get Follows

Get users followed by an account.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | No | Handle or DID to fetch follows for. | Current user |
| `limit` | number | No | Max results to return (1-100). | 50 |
| `cursor` | text | No | Pagination cursor returned from a previous call. | - |

### Get Followers

Get users who follow an account.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | No | Handle or DID to fetch followers for. | Current user |
| `limit` | number | No | Max results to return (1-100). | 50 |
| `cursor` | text | No | Pagination cursor returned from a previous call. | - |

### Like Post

Like a post. Requires the target post URI and CID (both are returned by Bluesky APIs).

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `uri` | text | Yes | Post URI to like (e.g. `at://did:.../app.bsky.feed.post/...`). | - |
| `cid` | text | Yes | Post CID to like. | - |

### Unlike Post

Unlike a previously liked post. Use the `like_uri` from the `like_post` response.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `like_uri` | text | Yes | Like record URI to delete. | - |

### Send Post

Send a text post. Optional fields allow replies, embeds, languages, and facets.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `text` | textarea | Yes | Text content of the post. | - |
| `profile_identify` | text | No | Handle or DID to post as. If omitted, uses the authenticated user. | Current user |
| `reply_to` | json | No | Reply reference with `root` and `parent` objects containing `uri` and `cid`. | - |
| `embed` | json | No | Raw Bluesky embed object (external link, record, or media). | - |
| `langs` | json | No | List of BCP-47 language codes (e.g. `["en"]`). | `["en"]` |
| `facets` | json | No | Rich-text facets (mentions, links, hashtags). | - |

### Repost

Repost another user's post.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `uri` | text | Yes | Post URI to repost. | - |
| `cid` | text | Yes | Post CID to repost. | - |

### Unrepost

Remove a repost you previously created. Use the `repost_uri` from the `repost` response.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `repost_uri` | text | Yes | Repost record URI to delete. | - |

### Get Likes

Get likes for a post.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `uri` | text | Yes | Post URI to query. | - |
| `cid` | text | No | Optional CID for the post. | - |
| `limit` | number | No | Max results to return (1-100). | 50 |
| `cursor` | text | No | Pagination cursor returned from a previous call. | - |

### Get Reposted By

Get users who reposted a post.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `uri` | text | Yes | Post URI to query. | - |
| `cid` | text | No | Optional CID for the post. | - |
| `limit` | number | No | Max results to return (1-100). | 50 |
| `cursor` | text | No | Pagination cursor returned from a previous call. | - |

### Get Post

Get a specific post by record key and author.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `post_rkey` | text | Yes | Record key of the post (last segment of the `at://` URI). | - |
| `profile_identify` | text | No | Handle or DID of the post author. | Current user |
| `cid` | text | No | Optional CID of the post. | - |

### Get Posts

Get multiple posts by their URIs.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `uris` | json | Yes | Array of post URIs to retrieve. | - |

### Get Timeline

Get posts from your home timeline.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `algorithm` | text | No | Optional timeline algorithm ID. Leave empty for the default timeline. | Default algorithm |
| `cursor` | text | No | Pagination cursor returned from a previous call (opaque string). | - |
| `limit` | number | No | Max results to return (1-100). | Server default |

### Get Author Feed

Get posts from a specific user (or the authenticated user if omitted).

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `actor` | text | No | Handle or DID of the user. | Current user |
| `cursor` | text | No | Pagination cursor returned from a previous call. | - |
| `filter` | text | No | Optional filter for post types (per Bluesky API). | - |
| `limit` | number | No | Max results to return (1-100). | Server default |
| `include_pins` | checkbox | No | Include pinned posts when available. | false |

### Get Post Thread

Get a full conversation thread for a post.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `uri` | text | Yes | Post URI to fetch the thread for. | - |
| `depth` | number | No | How many reply levels to include. Use `0` or empty for server default. | Server default |
| `parent_height` | number | No | How many parent posts to include. Use `0` or empty for server default. | Server default |

### Resolve Handle

Resolve a handle to a DID.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | Yes | Handle to resolve (e.g. `user.bsky.social`). | - |

### Mute User

Mute a user by handle or DID.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `actor` | text | Yes | Handle or DID of the user to mute. | - |

### Unmute User

Unmute a previously muted user.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `actor` | text | Yes | Handle or DID of the user to unmute. | - |

### Unfollow User

Unfollow a user. Use the `follow_uri` from `follow_user`.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `follow_uri` | text | Yes | Follow record URI to delete. | - |

### Send Image

Send a post with a single image. The image file is taken from the job input (first file in `input.files`).

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `text` | text | Yes | Text content of the post. | - |
| `image_alt` | text | Yes | Alt text description for the image. | - |
| `profile_identify` | text | No | Handle or DID to post as. | Current user |
| `reply_to` | json | No | Reply reference with `root` and `parent` objects containing `uri` and `cid`. | - |
| `langs` | json | No | List of BCP-47 language codes. | `["en"]` |
| `facets` | json | No | Rich-text facets (mentions, links, hashtags). | - |

### Send Images

Send a post with multiple images (up to 4). Images are taken from the job input files in order.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `text` | text | Yes | Text content of the post. | - |
| `image_alts` | json | No | Array of alt-text strings, one per image. | Empty strings |
| `profile_identify` | text | No | Handle or DID to post as. | Current user |
| `reply_to` | json | No | Reply reference with `root` and `parent` objects containing `uri` and `cid`. | - |
| `langs` | json | No | List of BCP-47 language codes. | `["en"]` |
| `facets` | json | No | Rich-text facets (mentions, links, hashtags). | - |

### Send Video

Send a post with a video. The video file is taken from the job input (first file in `input.files`).

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `text` | text | Yes | Text content of the post. | - |
| `video_alt` | text | No | Alt text description for the video. | - |
| `profile_identify` | text | No | Handle or DID to post as. | Current user |
| `reply_to` | json | No | Reply reference with `root` and `parent` objects containing `uri` and `cid`. | - |
| `langs` | json | No | List of BCP-47 language codes. | `["en"]` |
| `facets` | json | No | Rich-text facets (mentions, links, hashtags). | - |

### Delete Post

Delete a post created by the authenticated user.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `uri` | text | Yes | Post URI to delete. | - |

### Follow User

Follow a user by handle. The handle is resolved to a DID automatically.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | Yes | Handle to follow (e.g. `user.bsky.social`). | - |

## Testing

When invoked by xyOps the script expects JSON input via STDIN. You can also test locally by piping a JSON file into the command.

Example input JSON:

```json
{
	"params": {
		"tool": "get_timeline",
		"limit": 1
	}
}
```

Example command:

```sh
export BLUESKY_IDENTIFIER="your-handle.bsky.social"
export BLUESKY_APP_PASSWORD="your-app-password"

cat MYFILE.json | node index.js
```

## Data Collection

This plugin does not collect or transmit any metrics or user data beyond the Bluesky API calls you request.

## License

MIT
```

## File: `index.js`
```javascript
#!/usr/bin/env node

// xyOps Event Plugin for Bluesky Social (pure Node.js + fetch)
// Author: Joseph Huckaby (PixlCore), MIT License

'use strict';

const fs = require('fs');
const path = require('path');

const DEFAULT_SERVICE_URL = 'https://bsky.social';
const IMAGE_EXTS = new Map([
	['.jpg', 'image/jpeg'],
	['.jpeg', 'image/jpeg'],
	['.png', 'image/png'],
	['.gif', 'image/gif'],
	['.webp', 'image/webp']
]);
const VIDEO_EXTS = new Map([
	['.mp4', 'video/mp4'],
	['.mov', 'video/quicktime'],
	['.webm', 'video/webm']
]);

function writeXY(message) {
	process.stdout.write(JSON.stringify(message) + "\n");
}

function fail(code, description) {
	writeXY({ xy: 1, code, description });
	process.exit(0);
}

async function readJob() {
	const chunks = [];
	for await (const chunk of process.stdin) chunks.push(chunk);
	const raw = chunks.join('');
	if (!raw) return {};
	return JSON.parse(raw);
}

function normalizeServiceUrl(url) {
	return (url || DEFAULT_SERVICE_URL).replace(/\/+$/, '');
}

function getMimeType(filename) {
	const ext = path.extname(filename).toLowerCase();
	return IMAGE_EXTS.get(ext) || VIDEO_EXTS.get(ext) || 'application/octet-stream';
}

function parseAtUri(uri) {
	const match = uri.match(/^at:\/\/([^/]+)\/([^/]+)\/([^/]+)$/);
	if (!match) {
		throw new Error(`Invalid at:// URI: ${uri}`);
	}
	return { repo: match[1], collection: match[2], rkey: match[3] };
}

async function createSession(serviceUrl, identifier, password) {
	const res = await fetch(`${serviceUrl}/xrpc/com.atproto.server.createSession`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ identifier, password })
	});
	const text = await res.text();
	let data = null;
	try { data = text ? JSON.parse(text) : null; }
	catch (err) { data = { raw: text }; }
	if (!res.ok) {
		throw new Error(`Auth failed (${res.status}): ${text || res.statusText}`);
	}
	return data;
}

function buildXrpcClient(serviceUrl, accessJwt) {
	return async function xrpc(method, nsid, options = {}) {
		const { params, body, headers, rawBody } = options;
		const url = new URL(`${serviceUrl}/xrpc/${nsid}`);
		if (params) {
			const search = new URLSearchParams();
			Object.keys(params).forEach((key) => {
				const value = params[key];
				if (value === undefined || value === null || value === '') return;
				if (Array.isArray(value)) {
					value.forEach((item) => search.append(key, item));
				}
				else {
					search.set(key, value);
				}
			});
			url.search = search.toString();
		}

		const requestHeaders = Object.assign({}, headers || {});
		if (accessJwt) requestHeaders.Authorization = `Bearer ${accessJwt}`;

		let payload = null;
		if (rawBody !== undefined) {
			payload = rawBody;
		}
		else if (body !== undefined) {
			requestHeaders['Content-Type'] = 'application/json';
			payload = JSON.stringify(body);
		}

		const res = await fetch(url, {
			method,
			headers: requestHeaders,
			body: payload
		});
		const text = await res.text();
		let data = null;
		try { data = text ? JSON.parse(text) : null; }
		catch (err) { data = { raw: text }; }
		if (!res.ok) {
			if (data.message) {
				var err = new Error(data.message);
				err.message = data.message;
				err.code = data.error || res.status;
				throw err;
			}
			else {
				const detail = text || res.statusText;
				throw new Error(`XRPC ${nsid} failed (${res.status}): ${detail}`);
			}
		}
		return data;
	};
}

async function resolveHandle(xrpc, handle) {
	// Resolve a handle to a DID for follow/fetch operations.
	const data = await xrpc('GET', 'com.atproto.identity.resolveHandle', {
		params: { handle }
	});
	return data.did;
}

async function uploadBlob(xrpc, filename) {
	// Upload a local file to the repo blob endpoint.
	const mimeType = getMimeType(filename);
	const buffer = fs.readFileSync(filename);
	const data = await xrpc('POST', 'com.atproto.repo.uploadBlob', {
		headers: { 'Content-Type': mimeType },
		rawBody: buffer
	});
	return data.blob;
}

function coerceNumber(value, fallback) {
	if (value === undefined || value === null || value === '') return fallback;
	if (typeof value === 'number') return value;
	const parsed = parseInt(value, 10);
	return Number.isNaN(parsed) ? fallback : parsed;
}

function coerceOptionalPositive(value) {
	const number = coerceNumber(value, undefined);
	if (number === undefined || number <= 0) return undefined;
	return number;
}

(async function main() {
	if (!global.fetch) {
		fail('fetch', 'This plugin requires Node.js 18+ with the global fetch API.');
	}

	// Read job payload from STDIN.
	let job = {};
	try {
		job = await readJob();
	}
	catch (err) {
		fail('json', `Failed to parse JSON input: ${err.message || String(err)}`);
	}
	const params = job.params || {};
	const tool = params.tool;

	if (!tool || typeof tool !== 'string') {
		fail('params', "Required 'tool' parameter could not be found.");
	}

	const identifier = process.env.BLUESKY_IDENTIFIER;
	const password = process.env.BLUESKY_APP_PASSWORD;
	const serviceUrl = normalizeServiceUrl(process.env.BLUESKY_SERVICE_URL);

	if (!identifier) fail('env', "Required 'BLUESKY_IDENTIFIER' environment variable could not be found.");
	if (!password) fail('env', "Required 'BLUESKY_APP_PASSWORD' environment variable could not be found.");

	// Authenticate against the Bluesky service.
	let session = null;
	try {
		session = await createSession(serviceUrl, identifier, password);
	}
	catch (err) {
		fail('auth', err.message || String(err));
	}
	const xrpc = buildXrpcClient(serviceUrl, session.accessJwt);

	const ensureFiles = () => {
		if (!job.input || !job.input.files || !job.input.files.length) {
			throw new Error('No files were provided for job.');
		}
	};

	let result = null;
	try {
		// Route to the selected tool and collect results.
		switch (tool) {
			case 'check_auth_status': {
				result = {
					status: 'success',
					message: `Authenticated to ${serviceUrl}`,
					handle: session.handle,
					did: session.did
				};
				break;
			}

			case 'get_profile': {
				const handle = params.handle || session.handle;
				const profile = await xrpc('GET', 'app.bsky.actor.getProfile', {
					params: { actor: handle }
				});
				result = { status: 'success', profile };
				break;
			}

			case 'get_follows': {
				const handle = params.handle || session.handle;
				const limit = Math.max(1, Math.min(100, coerceNumber(params.limit, 50)));
				const follows = await xrpc('GET', 'app.bsky.graph.getFollows', {
					params: { actor: handle, limit, cursor: params.cursor }
				});
				result = { status: 'success', follows };
				break;
			}

			case 'get_followers': {
				const handle = params.handle || session.handle;
				const limit = Math.max(1, Math.min(100, coerceNumber(params.limit, 50)));
				const followers = await xrpc('GET', 'app.bsky.graph.getFollowers', {
					params: { actor: handle, limit, cursor: params.cursor }
				});
				result = { status: 'success', followers };
				break;
			}

			case 'like_post': {
				const record = {
					subject: { uri: params.uri, cid: params.cid },
					createdAt: new Date().toISOString()
				};
				const like = await xrpc('POST', 'com.atproto.repo.createRecord', {
					body: {
						repo: session.did,
						collection: 'app.bsky.feed.like',
						record
					}
				});
				result = {
					status: 'success',
					message: 'Post liked successfully',
					like_uri: like.uri,
					like_cid: like.cid
				};
				break;
			}

			case 'unlike_post': {
				const parsed = parseAtUri(params.like_uri);
				await xrpc('POST', 'com.atproto.repo.deleteRecord', {
					body: {
						repo: parsed.repo,
						collection: parsed.collection,
						rkey: parsed.rkey
					}
				});
				result = { status: 'success', message: 'Post unliked successfully' };
				break;
			}

			case 'send_post': {
				const record = {
					$type: 'app.bsky.feed.post',
					text: params.text,
					createdAt: new Date().toISOString()
				};
				if (params.reply_to && Object.keys(params.reply_to).length) record.reply = params.reply_to;
				if (params.embed && Object.keys(params.embed).length) record.embed = params.embed;
				record.langs = (params.langs && params.langs.length) ? params.langs : ['en'];
				if (params.facets && params.facets.length) record.facets = params.facets;

				const repoDid = params.profile_identify
					? (params.profile_identify.startsWith('did:') ? params.profile_identify : await resolveHandle(xrpc, params.profile_identify))
					: session.did;

				const post = await xrpc('POST', 'com.atproto.repo.createRecord', {
					body: {
						repo: repoDid,
						collection: 'app.bsky.feed.post',
						record
					}
				});
				result = {
					status: 'success',
					message: 'Post sent successfully',
					post_uri: post.uri,
					post_cid: post.cid
				};
				break;
			}

			case 'repost': {
				const record = {
					subject: { uri: params.uri, cid: params.cid },
					createdAt: new Date().toISOString()
				};
				const repost = await xrpc('POST', 'com.atproto.repo.createRecord', {
					body: {
						repo: session.did,
						collection: 'app.bsky.feed.repost',
						record
					}
				});
				result = {
					status: 'success',
					message: 'Post reposted successfully',
					repost_uri: repost.uri,
					repost_cid: repost.cid
				};
				break;
			}

			case 'unrepost': {
				const parsed = parseAtUri(params.repost_uri);
				await xrpc('POST', 'com.atproto.repo.deleteRecord', {
					body: {
						repo: parsed.repo,
						collection: parsed.collection,
						rkey: parsed.rkey
					}
				});
				result = { status: 'success', message: 'Repost removed successfully' };
				break;
			}

			case 'get_likes': {
				const limit = Math.max(1, Math.min(100, coerceNumber(params.limit, 50)));
				const likes = await xrpc('GET', 'app.bsky.feed.getLikes', {
					params: { uri: params.uri, cid: params.cid, limit, cursor: params.cursor }
				});
				result = { status: 'success', likes };
				break;
			}

			case 'get_reposted_by': {
				const limit = Math.max(1, Math.min(100, coerceNumber(params.limit, 50)));
				const reposts = await xrpc('GET', 'app.bsky.feed.getRepostedBy', {
					params: { uri: params.uri, cid: params.cid, limit, cursor: params.cursor }
				});
				result = { status: 'success', reposts };
				break;
			}

			case 'get_post': {
				const repoIdentify = params.profile_identify || session.did;
				const repoDid = repoIdentify.startsWith('did:') ? repoIdentify : await resolveHandle(xrpc, repoIdentify);
				const post = await xrpc('GET', 'com.atproto.repo.getRecord', {
					params: {
						repo: repoDid,
						collection: 'app.bsky.feed.post',
						rkey: params.post_rkey,
						cid: params.cid
					}
				});
				result = { status: 'success', post };
				break;
			}

			case 'get_posts': {
				const posts = await xrpc('GET', 'app.bsky.feed.getPosts', {
					params: { uris: params.uris }
				});
				result = { status: 'success', posts };
				break;
			}

			case 'get_timeline': {
				const timeline = await xrpc('GET', 'app.bsky.feed.getTimeline', {
					params: {
						algorithm: params.algorithm,
						cursor: params.cursor,
						limit: coerceOptionalPositive(params.limit)
					}
				});
				result = { status: 'success', timeline };
				break;
			}

			case 'get_author_feed': {
				const actor = params.actor || session.handle;
				const feed = await xrpc('GET', 'app.bsky.feed.getAuthorFeed', {
					params: {
						actor,
						cursor: params.cursor,
						filter: params.filter,
						limit: coerceOptionalPositive(params.limit),
						includePins: params.include_pins ? 'true' : undefined
					}
				});
				result = { status: 'success', feed };
				break;
			}

			case 'get_post_thread': {
				const thread = await xrpc('GET', 'app.bsky.feed.getPostThread', {
					params: {
						uri: params.uri,
						depth: coerceOptionalPositive(params.depth),
						parentHeight: coerceOptionalPositive(params.parent_height)
					}
				});
				result = { status: 'success', thread };
				break;
			}

			case 'resolve_handle': {
				const did = await resolveHandle(xrpc, params.handle);
				result = { status: 'success', handle: params.handle, did };
				break;
			}

			case 'mute_user': {
				await xrpc('POST', 'app.bsky.graph.muteActor', {
					body: { actor: params.actor }
				});
				result = { status: 'success', message: `Muted user ${params.actor}` };
				break;
			}

			case 'unmute_user': {
				await xrpc('POST', 'app.bsky.graph.unmuteActor', {
					body: { actor: params.actor }
				});
				result = { status: 'success', message: `Unmuted user ${params.actor}` };
				break;
			}

			case 'unfollow_user': {
				const parsed = parseAtUri(params.follow_uri);
				await xrpc('POST', 'com.atproto.repo.deleteRecord', {
					body: {
						repo: parsed.repo,
						collection: parsed.collection,
						rkey: parsed.rkey
					}
				});
				result = { status: 'success', message: 'Successfully unfollowed user' };
				break;
			}

			case 'send_image': {
				ensureFiles();
				const file = job.input.files[0].filename;
				const blob = await uploadBlob(xrpc, file);
				const record = {
					$type: 'app.bsky.feed.post',
					text: params.text,
					createdAt: new Date().toISOString(),
					embed: {
						$type: 'app.bsky.embed.images',
						images: [
							{ alt: params.image_alt || '', image: blob }
						]
					},
					langs: (params.langs && params.langs.length) ? params.langs : ['en']
				};
				if (params.reply_to && Object.keys(params.reply_to).length) record.reply = params.reply_to;
				if (params.facets && params.facets.length) record.facets = params.facets;

				const repoDid = params.profile_identify
					? (params.profile_identify.startsWith('did:') ? params.profile_identify : await resolveHandle(xrpc, params.profile_identify))
					: session.did;

				const post = await xrpc('POST', 'com.atproto.repo.createRecord', {
					body: {
						repo: repoDid,
						collection: 'app.bsky.feed.post',
						record
					}
				});
				result = {
					status: 'success',
					message: 'Post with image created successfully',
					post_uri: post.uri,
					post_cid: post.cid
				};
				break;
			}

			case 'send_images': {
				ensureFiles();
				const files = job.input.files.map((file) => file.filename).slice(0, 4);
				const blobs = [];
				for (const filename of files) {
					blobs.push(await uploadBlob(xrpc, filename));
				}

				const imageAlts = Array.isArray(params.image_alts) ? params.image_alts : [];
				const images = blobs.map((blob, idx) => ({
					alt: imageAlts[idx] || '',
					image: blob
				}));

				const record = {
					$type: 'app.bsky.feed.post',
					text: params.text,
					createdAt: new Date().toISOString(),
					embed: {
						$type: 'app.bsky.embed.images',
						images
					},
					langs: (params.langs && params.langs.length) ? params.langs : ['en']
				};
				if (params.reply_to && Object.keys(params.reply_to).length) record.reply = params.reply_to;
				if (params.facets && params.facets.length) record.facets = params.facets;

				const repoDid = params.profile_identify
					? (params.profile_identify.startsWith('did:') ? params.profile_identify : await resolveHandle(xrpc, params.profile_identify))
					: session.did;

				const post = await xrpc('POST', 'com.atproto.repo.createRecord', {
					body: {
						repo: repoDid,
						collection: 'app.bsky.feed.post',
						record
					}
				});
				result = {
					status: 'success',
					message: 'Post with images created successfully',
					post_uri: post.uri,
					post_cid: post.cid
				};
				break;
			}

			case 'send_video': {
				ensureFiles();
				const file = job.input.files[0].filename;
				const blob = await uploadBlob(xrpc, file);
				const record = {
					$type: 'app.bsky.feed.post',
					text: params.text,
					createdAt: new Date().toISOString(),
					embed: {
						$type: 'app.bsky.embed.video',
						video: blob,
						alt: params.video_alt || ''
					},
					langs: (params.langs && params.langs.length) ? params.langs : ['en']
				};
				if (params.reply_to && Object.keys(params.reply_to).length) record.reply = params.reply_to;
				if (params.facets && params.facets.length) record.facets = params.facets;

				const repoDid = params.profile_identify
					? (params.profile_identify.startsWith('did:') ? params.profile_identify : await resolveHandle(xrpc, params.profile_identify))
					: session.did;

				const post = await xrpc('POST', 'com.atproto.repo.createRecord', {
					body: {
						repo: repoDid,
						collection: 'app.bsky.feed.post',
						record
					}
				});
				result = {
					status: 'success',
					message: 'Post with video created successfully',
					post_uri: post.uri,
					post_cid: post.cid
				};
				break;
			}

			case 'delete_post': {
				const parsed = parseAtUri(params.uri);
				await xrpc('POST', 'com.atproto.repo.deleteRecord', {
					body: {
						repo: parsed.repo,
						collection: parsed.collection,
						rkey: parsed.rkey
					}
				});
				result = { status: 'success', message: 'Post deleted successfully' };
				break;
			}

			case 'follow_user': {
				const did = await resolveHandle(xrpc, params.handle);
				const record = {
					subject: did,
					createdAt: new Date().toISOString()
				};
				const follow = await xrpc('POST', 'com.atproto.repo.createRecord', {
					body: {
						repo: session.did,
						collection: 'app.bsky.graph.follow',
						record
					}
				});
				result = {
					status: 'success',
					message: `Now following ${params.handle}`,
					follow_uri: follow.uri,
					follow_cid: follow.cid
				};
				break;
			}

			default:
				throw new Error(`Unsupported tool: ${tool}`);
		} // switch tool
		
		writeXY({ xy: 1, code: 0, description: result.message || 'Success', data: result });
	}
	catch (err) {
		writeXY({ xy: 1, code: err.code || 1, description: err.message || String(err) });
	}
})();
```

## File: `package.json`
```json
{
	"name": "@pixlcore/xyplug-bluesky",
	"version": "1.0.7",
	"description": "A BlueSky Plugin for use in the xyOps workflow automation system.",
	"author": "Joseph Huckaby <jhuckaby@pixlcore.com>",
	"license": "MIT",
	"homepage": "https://github.com/pixlcore/xyplug-bluesky",
	"repository": {
		"type": "git",
		"url": "https://github.com/pixlcore/xyplug-bluesky"
	},
	"bugs": {
		"url": "https://github.com/pixlcore/xyplug-bluesky/issues"
	},
	"bin": {
		"xyplug-bluesky": "index.js"
	},
	"keywords": [
		"xyops",
		"bluesky",
		"social",
		"atproto"
	],
	"publishConfig": {
		"access": "public"
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
				"id": "pmjucch6qt8jan6t",
				"title": "Bluesky Social",
				"enabled": true,
				"type": "event",
				"command": "npx -y @pixlcore/xyplug-bluesky@1.0.7",
				"script": "",
				"groups": [],
				"format": "",
				"params": [
					{
						"id": "tool",
						"title": "Tool Select",
						"type": "toolset",
						"caption": "",
						"data": {
							"tools": [
								{
									"id": "check_auth_status",
									"title": "Check Auth Status",
									"description": "Check if the current session is authenticated.",
									"fields": []
								},
								{
									"id": "get_profile",
									"title": "Get Profile",
									"description": "Get a user profile.",
									"fields": [
										{
											"id": "handle",
											"title": "Handle",
											"type": "text",
											"value": "",
											"caption": "Optional handle to get profile for. If None, gets the authenticated user"
										}
									]
								},
								{
									"id": "get_follows",
									"title": "Get Follows",
									"description": "Get users followed by an account.",
									"fields": [
										{
											"id": "handle",
											"title": "Handle",
											"type": "text",
											"value": "",
											"caption": "Optional handle to get follows for. If None, gets the authenticated user"
										},
										{
											"id": "limit",
											"title": "Limit",
											"type": "text",
											"value": 50,
											"caption": "Maximum number of results to return (1-100)",
											"variant": "number"
										},
										{
											"id": "cursor",
											"title": "Cursor",
											"type": "text",
											"value": "",
											"caption": "Optional pagination cursor"
										}
									]
								},
								{
									"id": "get_followers",
									"title": "Get Followers",
									"description": "Get users who follow an account.",
									"fields": [
										{
											"id": "handle",
											"title": "Handle",
											"type": "text",
											"value": "",
											"caption": "Optional handle to get followers for. If None, gets the authenticated user"
										},
										{
											"id": "limit",
											"title": "Limit",
											"type": "text",
											"value": 50,
											"caption": "Maximum number of results to return (1-100)",
											"variant": "number"
										},
										{
											"id": "cursor",
											"title": "Cursor",
											"type": "text",
											"value": "",
											"caption": "Optional pagination cursor"
										}
									]
								},
								{
									"id": "like_post",
									"title": "Like Post",
									"description": "Like a post.",
									"fields": [
										{
											"id": "uri",
											"title": "URI",
											"type": "text",
											"value": "",
											"caption": "URI of the post to like",
											"required": true
										},
										{
											"id": "cid",
											"title": "CID",
											"type": "text",
											"value": "",
											"caption": "CID of the post to like",
											"required": true
										}
									]
								},
								{
									"id": "unlike_post",
									"title": "Unlike Post",
									"description": "Unlike a previously liked post.",
									"fields": [
										{
											"id": "like_uri",
											"title": "Like URI",
											"type": "text",
											"value": "",
											"caption": "URI of the like.",
											"required": true
										}
									]
								},
								{
									"id": "send_post",
									"title": "Send Post",
									"description": "Send a post to Bluesky.",
									"fields": [
										{
											"id": "text",
											"title": "Text",
											"type": "textarea",
											"value": "",
											"caption": "Text content of the post",
											"required": true
										},
										{
											"id": "profile_identify",
											"title": "Profile Identifier",
											"type": "text",
											"value": "",
											"caption": "Optional handle or DID. Where to send post. If not provided, sends to current profile"
										},
										{
											"id": "reply_to",
											"title": "Reply To",
											"type": "json",
											"value": {},
											"caption": "Optional reply reference with 'root' and 'parent' containing 'uri' and 'cid'"
										},
										{
											"id": "embed",
											"title": "Embed",
											"type": "json",
											"value": {},
											"caption": "Optional embed object (images, external links, records, or video)"
										},
										{
											"id": "langs",
											"title": "Languages",
											"type": "json",
											"value": [],
											"caption": "Optional list of language codes used in the post (defaults to ['en'])"
										},
										{
											"id": "facets",
											"title": "Facets",
											"type": "json",
											"value": [],
											"caption": "Optional list of rich text facets (mentions, links, etc.)"
										}
									]
								},
								{
									"id": "repost",
									"title": "Repost",
									"description": "Repost another user's post.",
									"fields": [
										{
											"id": "uri",
											"title": "URI",
											"type": "text",
											"value": "",
											"caption": "URI of the post to repost",
											"required": true
										},
										{
											"id": "cid",
											"title": "CID",
											"type": "text",
											"value": "",
											"caption": "CID of the post to repost",
											"required": true
										}
									]
								},
								{
									"id": "unrepost",
									"title": "Unrepost",
									"description": "Remove a repost of another user's post.",
									"fields": [
										{
											"id": "repost_uri",
											"title": "Repost URI",
											"type": "text",
											"value": "",
											"caption": "URI of the repost to remove",
											"required": true
										}
									]
								},
								{
									"id": "get_likes",
									"title": "Get Likes",
									"description": "Get likes for a post.",
									"fields": [
										{
											"id": "uri",
											"title": "URI",
											"type": "text",
											"value": "",
											"caption": "URI of the post to get likes for",
											"required": true
										},
										{
											"id": "cid",
											"title": "CID",
											"type": "text",
											"value": "",
											"caption": "Optional CID of the post (not strictly required)"
										},
										{
											"id": "limit",
											"title": "Limit",
											"type": "text",
											"value": 50,
											"caption": "Maximum number of results to return (1-100)",
											"variant": "number"
										},
										{
											"id": "cursor",
											"title": "Cursor",
											"type": "text",
											"value": "",
											"caption": "Optional pagination cursor"
										}
									]
								},
								{
									"id": "get_reposted_by",
									"title": "Get Reposted By",
									"description": "Get users who reposted a post.",
									"fields": [
										{
											"id": "uri",
											"title": "URI",
											"type": "text",
											"value": "",
											"caption": "URI of the post to get reposts for",
											"required": true
										},
										{
											"id": "cid",
											"title": "CID",
											"type": "text",
											"value": "",
											"caption": "Optional CID of the post (not strictly required)"
										},
										{
											"id": "limit",
											"title": "Limit",
											"type": "text",
											"value": 50,
											"caption": "Maximum number of results to return (1-100)",
											"variant": "number"
										},
										{
											"id": "cursor",
											"title": "Cursor",
											"type": "text",
											"value": "",
											"caption": "Optional pagination cursor"
										}
									]
								},
								{
									"id": "get_post",
									"title": "Get Post",
									"description": "Get a specific post.",
									"fields": [
										{
											"id": "post_rkey",
											"title": "Post Record Key",
											"type": "text",
											"value": "",
											"caption": "The record key of the post",
											"required": true
										},
										{
											"id": "profile_identify",
											"title": "Profile Identifier",
											"type": "text",
											"value": "",
											"caption": "Handle or DID of the post author"
										},
										{
											"id": "cid",
											"title": "CID",
											"type": "text",
											"value": "",
											"caption": "Optional CID of the post"
										}
									]
								},
								{
									"id": "get_posts",
									"title": "Get Posts",
									"description": "Get multiple posts by their URIs.",
									"fields": [
										{
											"id": "uris",
											"title": "URIs",
											"type": "json",
											"value": [],
											"caption": "List of post URIs to retrieve",
											"required": true
										}
									]
								},
								{
									"id": "get_timeline",
									"title": "Get Timeline",
									"description": "Get posts from your home timeline.",
									"fields": [
										{
											"id": "algorithm",
											"title": "Algorithm",
											"type": "text",
											"value": "",
											"caption": "Optional algorithm to use for timeline"
										},
										{
											"id": "cursor",
											"title": "Cursor",
											"type": "text",
											"value": "",
											"caption": "Optional pagination cursor"
										},
										{
											"id": "limit",
											"title": "Limit",
											"type": "text",
											"value": 0,
											"caption": "Maximum number of results to return",
											"variant": "number"
										}
									]
								},
								{
									"id": "get_author_feed",
									"title": "Get Author Feed",
									"description": "Get posts from a specific user.",
									"fields": [
										{
											"id": "actor",
											"title": "Actor",
											"type": "text",
											"value": "",
											"caption": "Handle or DID of the user",
											"required": false
										},
										{
											"id": "cursor",
											"title": "Cursor",
											"type": "text",
											"value": "",
											"caption": "Optional pagination cursor"
										},
										{
											"id": "filter",
											"title": "Filter",
											"type": "text",
											"value": "",
											"caption": "Optional filter for post types"
										},
										{
											"id": "limit",
											"title": "Limit",
											"type": "text",
											"value": 0,
											"caption": "Maximum number of results to return",
											"variant": "number"
										},
										{
											"id": "include_pins",
											"title": "Include Pins",
											"type": "checkbox",
											"value": false,
											"caption": "Whether to include pinned posts"
										}
									]
								},
								{
									"id": "get_post_thread",
									"title": "Get Post Thread",
									"description": "Get a full conversation thread.",
									"fields": [
										{
											"id": "uri",
											"title": "URI",
											"type": "text",
											"value": "",
											"caption": "URI of the post to get thread for",
											"required": true
										},
										{
											"id": "depth",
											"title": "Depth",
											"type": "text",
											"value": 0,
											"caption": "How many levels of replies to include",
											"variant": "number"
										},
										{
											"id": "parent_height",
											"title": "Parent Height",
											"type": "text",
											"value": 0,
											"caption": "How many parent posts to include",
											"variant": "number"
										}
									]
								},
								{
									"id": "resolve_handle",
									"title": "Resolve Handle",
									"description": "Resolve a handle to a DID.",
									"fields": [
										{
											"id": "handle",
											"title": "Handle",
											"type": "text",
											"value": "",
											"caption": "User handle to resolve (e.g. \"user.bsky.social\")",
											"required": true
										}
									]
								},
								{
									"id": "mute_user",
									"title": "Mute User",
									"description": "Mute a user.",
									"fields": [
										{
											"id": "actor",
											"title": "Actor",
											"type": "text",
											"value": "",
											"caption": "Handle or DID of the user to mute",
											"required": true
										}
									]
								},
								{
									"id": "unmute_user",
									"title": "Unmute User",
									"description": "Unmute a previously muted user.",
									"fields": [
										{
											"id": "actor",
											"title": "Actor",
											"type": "text",
											"value": "",
											"caption": "Handle or DID of the user to unmute",
											"required": true
										}
									]
								},
								{
									"id": "unfollow_user",
									"title": "Unfollow User",
									"description": "Unfollow a user.",
									"fields": [
										{
											"id": "follow_uri",
											"title": "Follow URI",
											"type": "text",
											"value": "",
											"caption": "URI of the follow record to delete",
											"required": true
										}
									]
								},
								{
									"id": "send_image",
									"title": "Send Image",
									"description": "Send a post with a single image.",
									"fields": [
										{
											"id": "text",
											"title": "Text",
											"type": "textarea",
											"value": "",
											"caption": "Text content of the post",
											"required": true
										},
										{
											"id": "image_alt",
											"title": "Image Alt",
											"type": "text",
											"value": "",
											"caption": "Alternative text description for the image",
											"required": true
										},
										{
											"id": "profile_identify",
											"title": "Profile Identifier",
											"type": "text",
											"value": "",
											"caption": "Optional handle or DID for the post author"
										},
										{
											"id": "reply_to",
											"title": "Reply To",
											"type": "json",
											"value": {},
											"caption": "Optional reply information dict with keys uri and cid"
										},
										{
											"id": "langs",
											"title": "Languages",
											"type": "json",
											"value": [],
											"caption": "Optional list of language codes"
										},
										{
											"id": "facets",
											"title": "Facets",
											"type": "json",
											"value": [],
											"caption": "Optional list of facets (mentions, links, etc.)"
										}
									]
								},
								{
									"id": "send_images",
									"title": "Send Images",
									"description": "Send a post with multiple images (up to 4).",
									"fields": [
										{
											"id": "text",
											"title": "Text",
											"type": "textarea",
											"value": "",
											"caption": "Text content of the post",
											"required": true
										},
										{
											"id": "image_alts",
											"title": "Image Alts",
											"type": "json",
											"value": [],
											"caption": "Optional list of alt text for each image"
										},
										{
											"id": "profile_identify",
											"title": "Profile Identifier",
											"type": "text",
											"value": "",
											"caption": "Optional handle or DID for the post author"
										},
										{
											"id": "reply_to",
											"title": "Reply To",
											"type": "json",
											"value": {},
											"caption": "Optional reply information dict with keys uri and cid"
										},
										{
											"id": "langs",
											"title": "Languages",
											"type": "json",
											"value": [],
											"caption": "Optional list of language codes"
										},
										{
											"id": "facets",
											"title": "Facets",
											"type": "json",
											"value": [],
											"caption": "Optional list of facets (mentions, links, etc.)"
										}
									]
								},
								{
									"id": "send_video",
									"title": "Send Video",
									"description": "Send a post with a video.",
									"fields": [
										{
											"id": "text",
											"title": "Text",
											"type": "textarea",
											"value": "",
											"caption": "Text content of the post",
											"required": true
										},
										{
											"id": "video_alt",
											"title": "Video Alt",
											"type": "text",
											"value": "",
											"caption": "Optional alternative text description for the video"
										},
										{
											"id": "profile_identify",
											"title": "Profile Identifier",
											"type": "text",
											"value": "",
											"caption": "Optional handle or DID for the post author"
										},
										{
											"id": "reply_to",
											"title": "Reply To",
											"type": "json",
											"value": {},
											"caption": "Optional reply information dict with keys uri and cid"
										},
										{
											"id": "langs",
											"title": "Languages",
											"type": "json",
											"value": [],
											"caption": "Optional list of language codes"
										},
										{
											"id": "facets",
											"title": "Facets",
											"type": "json",
											"value": [],
											"caption": "Optional list of facets (mentions, links, etc.)"
										}
									]
								},
								{
									"id": "delete_post",
									"title": "Delete Post",
									"description": "Delete a post created by the authenticated user.",
									"fields": [
										{
											"id": "uri",
											"title": "URI",
											"type": "text",
											"value": "",
											"caption": "URI of the post to delete",
											"required": true
										}
									]
								},
								{
									"id": "follow_user",
									"title": "Follow User",
									"description": "Follow a user.",
									"fields": [
										{
											"id": "handle",
											"title": "Handle",
											"type": "text",
											"value": "",
											"caption": "Handle of the user to follow",
											"required": true
										}
									]
								}
							]
						}
					}
				],
				"kill": "parent",
				"runner": false,
				"notes": "Access your Bluesky social profile, read your timeline, make posts, leave likes, and more.",
				"icon": "butterfly",
				"uid": "",
				"gid": ""
			}
		}
	]
}
```

