---
id: lazy
type: knowledge
owner: OA_Triage
---
# lazy
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "lazy-downloader",
  "version": "1.0.1",
  "description": "All-in-one media downloader CLI (Node.js)",
  "type": "module",
  "license": "MIT",
  "files": [
    "dist",
    "README.md",
    "LICENSE"
  ],
  "bin": {
    "lazy-down": "dist/cli.js"
  },
  "main": "./dist/index.js",
  "exports": "./dist/index.js",
  "engines": {
    "node": ">=20"
  },
  "scripts": {
    "build": "tsc -p tsconfig.json",
    "start": "node dist/cli.js",
    "test:help": "node dist/cli.js --help",
    "prepack": "npm run build"
  },
  "dependencies": {
    "playwright": "^1.54.2"
  },
  "devDependencies": {
    "@types/node": "^20.19.11",
    "typescript": "^5.9.2"
  }
}

```

### File: README.md
```md
# Dự án lazy Downloader 1.0.0

[![npm](https://img.shields.io/npm/v/lazy-downloader.svg)](https://www.npmjs.com/package/lazy-downloader)
[![Node](https://img.shields.io/node/v/lazy-downloader.svg)](https://www.npmjs.com/package/lazy-downloader)
[![License](https://img.shields.io/npm/l/lazy-downloader.svg)](https://www.npmjs.com/package/lazy-downloader)

`lazy-downloader` là CLI Node.js để parse URL và tải media trực tiếp từ nhiều nền tảng.

## Install

```bash
npm install -g lazy-downloader
npx playwright install chromium
```

## CLI

```bash
lazy-down "URL" -P downloads --all -o "%(title)s_%(idx)s.%(ext)s"
```

### Options (tóm tắt)

- `-P, --paths`: thư mục lưu
- `-o, --outtmpl`: output template
- `--all`: tải tất cả media
- `--headful`: mở browser UI
- `--no-unlock`: tắt unlock
- `--timeout`: timeout giây
- `--write-json`: ghi JSON cạnh file
- `--quiet`: tắt progress
- `--upload-url`: upload file lên endpoint thay vì trả local path
- `--upload-field`: tên field multipart (mặc định `file`)
- `--upload-token`: Bearer token cho endpoint upload
- `--remove-local-after-upload`: xóa file local sau khi upload thành công
- `--only-url`: chỉ lấy URL media, không lưu file local

## Upload Mode

```bash
lazy-down "URL" \
  --upload-url "http://localhost:8787/upload" \
  --upload-field "file" \
  --remove-local-after-upload
```

Khi bật upload mode, `paths[]` trong JSON sẽ là URL trả về từ server upload.

## Only URL Mode

```bash
lazy-down "URL" --only-url --all
```

Mode này không tải file xuống máy và không ghi vào thư mục `paths`.

## Library (Node.js)

```js
import { DownloadWorker } from "lazy-downloader";

const w = new DownloadWorker({ allMedias: true, outtmpl: "%(title)s_%(idx)s.%(ext)s" });
const res = await w.download("URL", "downloads");
console.log(res.paths);
```

## Progress Hooks

Hook nhận object trạng thái.

```js
import { DownloadWorker } from "lazy-downloader";

const hook = (d) => {
  if (d.status === "downloading") {
    console.log(d.filename, d.downloaded_bytes, d.total_bytes);
  } else if (d.status === "finished") {
    console.log("done", d.filename);
  }
};

const w = new DownloadWorker({ progressHooks: [hook] });
await w.download("URL", "downloads");
```

## Docs

- [CLI](docs/cli.md)
- [Output Template](docs/template.md)
- [JSON Response](docs/response.md)
- [Library API](docs/library.md)
- [Publish](docs/publish.md)

## License

MIT

```

### File: docs\README.md
```md
# Docs

- [CLI](cli.md)
- [Output Template](template.md)
- [JSON Response](response.md)
- [Library API](library.md)
- [Publish npm](publish.md)

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022", "DOM"],
    "strict": false,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "declaration": true,
    "sourceMap": false,
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src/**/*.ts"]
}

```

### File: docs\cli.md
```md
# CLI

## Install

```bash
npm install -g Lazy-downloader
npx playwright install chromium
```

## Usage

```bash
lazy-down "URL" -P downloads --all -o "%(title)s_%(idx)s.%(ext)s"
```

## Flags

| Flag | Ý nghĩa |
|---|---|
| `-P, --paths` | Thư mục lưu |
| `-o, --outtmpl` | Output template |
| `--all` | Download tất cả media |
| `--headful` | Browser có UI |
| `--no-unlock` | Tắt unlock |
| `--timeout` | Timeout (giây) |
| `--write-json` | Ghi JSON ra file |
| `--quiet` | Tắt progress |
| `--stdin` | Đọc URL từ stdin |

## Batch from stdin

```bash
type urls.txt | lazy-down --stdin -P downloads --all
```

```

### File: docs\library.md
```md
# Library API

## DownloadWorker

Các option thường dùng:

- `allMedias`
- `headful`
- `unlock`
- `timeoutSec`
- `outtmpl`
- `progressHooks`
- `writeJson`
- `jsonPretty`
- `printJson`

## Basic

```js
import { DownloadWorker } from "Lazy-downloader";

const w = new DownloadWorker({
  allMedias: true,
  outtmpl: "%(title)s_%(idx)s.%(ext)s"
});
const res = await w.download("URL", "downloads");
console.log(res.paths);
```

## Progress Hook payload

- `status`: `downloading` | `finished` | `error`
- `filename`
- `downloaded_bytes`
- `total_bytes`
- `elapsed`
- `speed`
- `eta`
- `info_dict`

```

### File: docs\publish.md
```md
# Publish (npm)

## Chuẩn bị

1) Tạo npm token (automation token khuyến nghị).
2) Thêm GitHub Secret:

- `NPM_TOKEN`

## Release theo tag

Workflow/pipeline có thể chạy khi push tag dạng `v*`.

```bash
git tag v0.1.0
git push origin v0.1.0
```

## Notes

- Version trong `package.json` phải khớp tag.
- Nếu trùng tên package, đổi `name`.

```

### File: docs\response.md
```md
# JSON Response

Response dùng để tích hợp automation.

## Full

```json
{
  "json": {},
  "medias": [],
  "parsed": [],
  "paths": [],
  "timeMs": 0
}
```

## Top-level

| Field | Type | Ý nghĩa |
|---|---|---|
| `json` | object | Metadata tổng hợp |
| `medias` | array | Media gốc |
| `parsed` | array | Media đã tải |
| `paths` | array[string] | File local |
| `timeMs` | number | ms |

## `json`

| Field | Type | Ý nghĩa |
|---|---|---|
| `url` | string | URL đầu vào |
| `source` | string | nguồn |
| `type` | string | `single`/`multiple` |
| `error` | boolean | lỗi |
| `title` | string | tiêu đề |
| `author` | string | tác giả |
| `thumbnail` | string | thumbnail |
| `id` | string | id |
| `pk` | string | threads pk |
| `unique_id` | string | tiktok username |
| `duration` | number | thời lượng |
| `like_count` | string/number | like |
| `time_end` | number | nội bộ |
| `medias` | array | media list |

## `medias[]`

| Field | Type | Ý nghĩa |
|---|---|---|
| `type` | string | image/video/audio |
| `url` | string | direct |
| `extension` | string | ext |
| `quality` | string | quality |
| `width` | number | w |
| `height` | number | h |
| `resolution` | string | WxH |
| `caption` | string | caption |
| `data_size` | number | bytes |
| `format_id` | string | format |
| `duration` | number | duration |
| `title` | string | tiêu đề tổng hợp |
| `author` | string | tác giả/owner |
| `source` | string | nguồn |
| `id` | string | media/post id |
| `unique_id` | string/null | username (nếu có) |
| `thumbnail` | string/null | thumbnail URL |
| `webpage_url` | string | URL đầu vào |

## `parsed[]`

| Field | Type | Ý nghĩa |
|---|---|---|
| `idx` | number | 1-based |
| `type` | string | type |
| `quality` | string | quality |
| `extension` | string | ext |
| `url` | string | direct |
| `savedPath` | string | local |
| `contentType` | string | mime |
| `width` | number/null | w |
| `height` | number/null | h |
| `resolution` | string/null | WxH |

## Compact

```json
{
  "paths": ["assets/cache/..."],
  "timeMs": 980
}
```

## Error (recommended)

```json
{
  "json": { "error": true, "message": "No medias in response" },
  "medias": [],
  "parsed": [],
  "paths": []
}
```

```

### File: docs\template.md
```md
# Output Template

Template tương tự `yt-dlp`:

```bash
-o "%(title)s_%(idx)s.%(ext)s"
```

## Keys

| Key | Ý nghĩa |
|---|---|
| `%(title)s` | Tiêu đề |
| `%(id)s` | ID nội dung |
| `%(source)s` | Nguồn (`tiktok`, `threads`, ...) |
| `%(idx)s` | Thứ tự media (1-based) |
| `%(ext)s` | Extension |
| `%(url)s` | URL đầu vào |
| `%(webpage_url)s` | URL trang |
| `%(media_url)s` | Direct media URL |

## Ví dụ

```bash
-o "%(source)s/%(title)s/%(idx)s.%(ext)s"
```

## Sanitize

- Loại ký tự không hợp lệ
- Giới hạn độ dài
- Tránh trùng tên bằng suffix `_1`, `_2`, ...

```

### File: src\auth-cache.ts
```ts
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

interface HostState {
  bearer?: { token: string; exp: number };
  cookie_tokens?: { csrf: string; api: string; exp: number };
  session_cookie?: { value: string; exp: number };
}

interface CacheState {
  hosts: Record<string, HostState>;
}

function nowSec(): number {
  return Math.floor(Date.now() / 1000);
}

export class AuthCacheStore {
  private readonly filePath: string;
  private state: CacheState = { hosts: {} };
  private loaded = false;

  constructor(filePath?: string | null) {
    const env = (process.env.AIO_DOWN_AUTH_CACHE || "").trim();
    this.filePath = filePath || env || path.join(os.homedir(), ".cache", "lazy-downloader", "auth-cache.json");
  }

  private load(): void {
    if (this.loaded) return;
    this.loaded = true;
    try {
      const raw = fs.readFileSync(this.filePath, "utf8");
      const obj = JSON.parse(raw) as CacheState;
      if (obj && typeof obj === "object" && obj.hosts && typeof obj.hosts === "object") {
        this.state = obj;
      }
    } catch {
      this.state = { hosts: {} };
    }
  }

  private save(): void {
    fs.mkdirSync(path.dirname(this.filePath), { recursive: true });
    const tmp = `${this.filePath}.tmp`;
    fs.writeFileSync(tmp, JSON.stringify(this.state, null, 2), "utf8");
    fs.renameSync(tmp, this.filePath);
  }

  private host(base: string): HostState {
    this.load();
    if (!this.state.hosts[base]) this.state.hosts[base] = {};
    return this.state.hosts[base];
  }

  getBearer(base: string): string {
    const b = this.host(base).bearer;
    if (!b) return "";
    if (!b.token || b.exp <= nowSec() + 10) return "";
    return b.token;
  }

  setBearer(base: string, token: string, expiresInSec: number): void {
    const t = String(token || "").trim();
    if (!t) return;
    this.host(base).bearer = { token: t, exp: nowSec() + Math.max(1, Number(expiresInSec) || 0) };
    this.save();
  }

  clearBearer(base: string): void {
    const h = this.host(base);
    if (h.bearer) {
      delete h.bearer;
      this.save();
    }
  }

  getCookieTokens(base: string): { csrf: string; api: string } {
    const c = this.host(base).cookie_tokens;
    if (!c) return { csrf: "", api: "" };
    if (!c.csrf || !c.api || c.exp <= nowSec() + 10) return { csrf: "", api: "" };
    return { csrf: c.csrf, api: c.api };
  }

  setCookieTokens(base: string, csrf: string, api: string, ttlSec = 86400): void {
    const x = String(csrf || "").trim();
    const y = String(api || "").trim();
    if (!x || !y) return;
    this.host(base).cookie_tokens = { csrf: x, api: y, exp: nowSec() + Math.max(60, Number(ttlSec) || 86400) };
    this.save();
  }

  getSessionCookie(base: string): string {
    const s = this.host(base).session_cookie;
    if (!s) return "";
    if (!s.value || s.exp <= nowSec() + 10) return "";
    return s.value;
  }

  setSessionCookie(base: string, value: string, ttlSec = 86400): void {
    const v = String(value || "").trim();
    if (!v) return;
    this.host(base).session_cookie = { value: v, exp: nowSec() + Math.max(60, Number(ttlSec) || 86400) };
    this.save();
  }
}

```

### File: src\cli.ts
```ts
#!/usr/bin/env node
import { DownloadWorker } from "./worker.js";
import { defaultProgressPrinter } from "./progress.js";

interface CliArgs {
  url: string;
  paths: string;
  outtmpl: string;
  all: boolean;
  headful: boolean;
  unlock: boolean;
  timeout: number;
  retries: number;
  outputFile: string;
  writeJson: boolean;
  noPretty: boolean;
  noPrintJson: boolean;
  quiet: boolean;
  stdin: boolean;
  help: boolean;
  uploadUrl: string;
  uploadField: string;
  uploadToken: string;
  removeLocalAfterUpload: boolean;
  onlyUrl: boolean;
}

function usage(): void {
  console.log(`Usage: lazy-down [url] [options]\n
Options:
  -P, --paths <dir>          Output directory (default: assets/cache)
  -o, --outtmpl <template>   Output template (default: %(title)s.%(ext)s)
  --all                      Download all medias
  --headful                  Run browser with UI
  --no-unlock                Disable unlock
  --timeout <sec>            Timeout in seconds (default: 60)
  --retries <n>              Max retries (default: 3)
  --output-file <prefix>     JSON output file prefix (default: lazy-downloaded)
  --write-json               Write JSON payload to file
  --no-pretty                Disable pretty JSON output in file
  --no-print-json            Disable printing JSON payload
  --quiet                    Disable progress output
  --stdin                    Read URLs from stdin (one per line)
  --upload-url <url>         Upload endpoint URL (multipart/form-data)
  --upload-field <name>      Multipart field name (default: file)
  --upload-token <token>     Bearer token for upload endpoint
  --remove-local-after-upload  Remove local file after upload succeeds
  --only-url                 Do not download/upload files, return media URLs only
  -h, --help                 Show help
`);
}

function parseArgs(argv: string[]): CliArgs {
  const out: CliArgs = {
    url: "",
    paths: "assets/cache",
    outtmpl: "%(title)s.%(ext)s",
    all: false,
    headful: false,
    unlock: true,
    timeout: 60,
    retries: 3,
    outputFile: "lazy-downloaded",
    writeJson: false,
    noPretty: false,
    noPrintJson: false,
    quiet: false,
    stdin: false,
    help: false,
    uploadUrl: "",
    uploadField: "file",
    uploadToken: "",
    removeLocalAfterUpload: false,
    onlyUrl: false
  };

  const args = [...argv];
  for (let i = 0; i < args.length; i += 1) {
    const a = args[i];
    const need = (): string => {
      i += 1;
      if (i >= args.length) throw new Error(`Missing value for ${a}`);
      return args[i];
    };

    if (a === "-h" || a === "--help") out.help = true;
    else if (a === "-P" || a === "--paths") out.paths = need();
    else if (a === "-o" || a === "--outtmpl") out.outtmpl = need();
    else if (a === "--all") out.all = true;
    else if (a === "--headful") out.headful = true;
    else if (a === "--no-unlock") out.unlock = false;
    else if (a === "--timeout") out.timeout = Number(need()) || out.timeout;
    else if (a === "--retries") out.retries = Number(need()) || out.retries;
    else if (a === "--output-file") out.outputFile = need();
    else if (a === "--write-json") out.writeJson = true;
    else if (a === "--no-pretty") out.noPretty = true;
    else if (a === "--no-print-json") out.noPrintJson = true;
    else if (a === "--quiet") out.quiet = true;
    else if (a === "--stdin") out.stdin = true;
    else if (a === "--upload-url") out.uploadUrl = need();
    else if (a === "--upload-field") out.uploadField = need();
    else if (a === "--upload-token") out.uploadToken = need();
    else if (a === "--remove-local-after-upload") out.removeLocalAfterUpload = true;
    else if (a === "--only-url") out.onlyUrl = true;
    else if (!a.startsWith("-") && !out.url) out.url = a;
    else throw new Error(`Unknown argument: ${a}`);
  }
  return out;
}

async function readStdinLines(): Promise<string[]> {
  const chunks: Buffer[] = [];
  for await (const c of process.stdin) chunks.push(c as Buffer);
  return Buffer.concat(chunks)
    .toString("utf8")
    .split(/\r?\n/)
    .map((x) => x.trim())
    .filter(Boolean);
}

async function runOne(worker: DownloadWorker, u: string, args: CliArgs): Promise<number> {
  const r = await worker.download(u, args.paths, true);
  if (args.noPrintJson) {
    console.log(JSON.stringify({ paths: r.paths, timeMs: r.timeMs, jsonPath: r.jsonPath }));
  }
  return 0;
}

async function main(): Promise<void> {
  let args: CliArgs;
  try {
    args = parseArgs(process.argv.slice(2));
  } catch (e: any) {
    console.error(String(e?.message || e));
    usage();
    process.exitCode = 1;
    return;
  }

  if (args.help) {
    usage();
    return;
  }

  const hooks = args.quiet ? [] : [defaultProgressPrinter()];
  const worker = new DownloadWorker({
    headful: args.headful,
    allMedias: args.all,
    unlock: args.unlock,
    timeoutSec: args.timeout,
    maxRetries: args.retries,
    outputFile: args.outputFile,
    writeJson: args.writeJson,
    jsonPretty: !args.noPretty,
    printJson: !args.noPrintJson,
    outtmpl: args.outtmpl,
    progressHooks: hooks,
    uploadUrl: args.uploadUrl,
    uploadField: args.uploadField,
    uploadToken: args.uploadToken,
    removeLocalAfterUpload: args.removeLocalAfterUpload,
    onlyUrl: args.onlyUrl
  });

  if (args.stdin) {
    const urls = await readStdinLines();
    let rc = 0;
    for (const u of urls) {
      try {
        await runOne(worker, u, args);
      } catch (e: any) {
        console.error(String(e?.message || e));
        rc = 2;
      }
    }
    process.exitCode = rc;
    return;
  }

  if (!args.url) {
    usage();
    process.exitCode = 1;
    return;
  }

  try {
    process.exitCode = await runOne(worker, args.url, args);
  } catch (e: any) {
    console.error(String(e?.message || e));
    process.exitCode = 2;
  }
}

main();

```

### File: src\endpoints.ts
```ts
export const BASE = "https://j2download.com";

export const Endpoints = {
  home: (): string => `${BASE}/`,
  api: (): string => `${BASE}/api`,
  autolink: (): string => `${BASE}/api/autolink`,
  authBootstrap: (): string => `${BASE}/api/auth/bootstrap`,
  authIssue: (): string => `${BASE}/api/auth/issue`
};

```

### File: src\index.ts
```ts
export { DownloadWorker } from "./worker.js";
export { AuthCacheStore } from "./auth-cache.js";
export { TemplateEngine } from "./template-engine.js";

```

### File: src\progress.ts
```ts
export interface ProgressPayload {
  status: "downloading" | "finished" | string;
  filename?: string;
  downloaded_bytes?: number;
  total_bytes?: number | null;
  elapsed?: number;
  eta?: number | null;
  speed?: number | null;
}

function human(n: number | null | undefined): string {
  if (n == null || Number.isNaN(Number(n))) return "NA";
  let x = Number(n);
  const units = ["B", "KiB", "MiB", "GiB", "TiB"];
  for (const u of units) {
    if (x < 1024) return `${x.toFixed(2)}${u}`;
    x /= 1024;
  }
  return `${x.toFixed(2)}PiB`;
}

export function defaultProgressPrinter(): (d: ProgressPayload) => void {
  let last = 0;
  return (d: ProgressPayload) => {
    const st = d?.status;
    const fn = d?.filename || "";
    const dl = d?.downloaded_bytes;
    const tt = d?.total_bytes;
    const sp = d?.speed;
    const eta = d?.eta;
    const now = Date.now();

    if (st === "downloading") {
      if (now - last < 200) return;
      last = now;
      let line: string;
      if (tt) {
        const pct = ((Number(dl || 0) / Number(tt)) * 100).toFixed(2).padStart(6, " ");
        line = `[download] ${pct}% of ${human(tt)} at ${human(sp ?? null)}/s ETA ${eta}s : ${fn}`;
      } else {
        line = `[download] ${human(dl ?? null)} at ${human(sp ?? null)}/s : ${fn}`;
      }
      process.stdout.write(`\r${line.slice(0, 180)}          `);
    } else if (st === "finished") {
      process.stdout.write(`\r[download] 100% of ${human(dl ?? null)} in ${Number(d?.elapsed || 0).toFixed(1)}s : ${fn}          \n`);
    }
  };
}

```

### File: src\template-engine.ts
```ts
import path from "node:path";

export class TemplateEngine {
  private readonly outtmpl: string;
  private readonly maxLen: number;

  constructor(outtmpl = "%(title)s.%(ext)s", maxLen = 240) {
    this.outtmpl = outtmpl || "%(id)s.%(ext)s";
    this.maxLen = Math.max(32, Number(maxLen) || 240);
  }

  private norm(s: string): string {
    return String(s || "")
      .replace(/\x00/g, "")
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^\x20-\x7E]/g, "")
      .trim()
      .replace(/[\\/:*?"<>|\r\n\t]+/g, "_")
      .replace(/\s+/g, " ")
      .trim();
  }

  private safeBase(s: string): string {
    let x = this.norm(s).replace(/^[ ._]+|[ ._]+$/g, "");
    x = x.replace(/\s+\./g, ".");
    if (!x) x = "download";
    if (x.length > this.maxLen) x = x.slice(0, this.maxLen).replace(/[ ._]+$/g, "");
    return x || "download";
  }

  private apply(tmpl: string, info: Record<string, unknown>): string {
    return tmpl.replace(/%\(([^)]+)\)s/g, (_m, k: string) => {
      const v = info?.[k];
      return v == null ? "" : String(v);
    });
  }

  resolve(info: Record<string, unknown>): string {
    const applied = this.apply(this.outtmpl, info);
    const unified = applied.split("/").join(path.sep).split("\\").join(path.sep);
    const parts = unified.split(path.sep).filter((p) => p && p !== "." && p !== "..");
    if (!parts.length) parts.push("download");
    parts[parts.length - 1] = this.safeBase(parts[parts.length - 1]);
    return path.join(...parts);
  }

  ensureExt(filePath: string, ext: string): string {
    const cleanExt = String(ext || "bin").replace(/^\.+/, "");
    const parsed = path.parse(filePath);
    const current = parsed.ext.replace(/^\./, "");
    if (current.toLowerCase() === cleanExt.toLowerCase()) return filePath;
    return path.join(parsed.dir, `${parsed.name}.${cleanExt}`);
  }
}

```

### File: src\worker.ts
```ts
import fs from "node:fs";
import fsp from "node:fs/promises";
import path from "node:path";
import { Readable } from "node:stream";
import { chromium } from "playwright";

import { BASE, Endpoints } from "./endpoints.js";
import { TemplateEngine } from "./template-engine.js";
import { AuthCacheStore } from "./auth-cache.js";

export interface DownloadOptions {
  headful?: boolean;
  allMedias?: boolean;
  unlock?: boolean;
  timeoutSec?: number;
  maxRetries?: number;
  outputFile?: string;
  writeJson?: boolean;
  jsonPretty?: boolean;
  printJson?: boolean;
  outtmpl?: string;
  progressHooks?: Array<(d: any) => void>;
  userAgent?: string;
  uploadUrl?: string;
  uploadField?: string;
  uploadToken?: string;
  removeLocalAfterUpload?: boolean;
  onlyUrl?: boolean;
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function nowMs(): number {
  return Date.now();
}

export class DownloadWorker {
  private readonly config: Required<DownloadOptions>;
  private readonly templater: TemplateEngine;
  private readonly authCache: AuthCacheStore;

  constructor(options: DownloadOptions = {}) {
    this.config = {
      headful: false,
      allMedias: false,
      unlock: true,
      timeoutSec: 60,
      maxRetries: 3,
      outputFile: "lazy-downloaded",
      writeJson: false,
      jsonPretty: true,
      printJson: true,
      outtmpl: "%(title)s.%(ext)s",
      progressHooks: [],
      userAgent:
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
      uploadUrl: "",
      uploadField: "file",
      uploadToken: "",
      removeLocalAfterUpload: false,
      onlyUrl: false,
      ...options
    };
    this.templater = new TemplateEngine(this.config.outtmpl);
    this.authCache = new AuthCacheStore();
  }

  private log(level: string, msg: string): void {
    const t = new Date().toTimeString().slice(0, 8);
    console.log(`${t} | ${level.toUpperCase()} | ${msg}`);
  }

  private hook(payload: any): void {
    for (const h of this.config.progressHooks || []) {
      try {
        h(payload);
      } catch {
        // ignore hook errors
      }
    }
  }

  private safeFileName(name: string): string {
    let s = String(name || "download").replace(/\x00/g, "");
    s = s.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    s = s.replace(/[^a-z0-9._-]+/g, "").replace(/[.]{2,}/g, ".").replace(/^[._-]+|[._-]+$/g, "");
    s = s.slice(0, 240);
    return s || "download";
  }

  private pickMedias(j: any): any[] {
    if (!j || typeof j !== "object") return [];
    if (Array.isArray(j.medias)) return j.medias.filter((m: any) => m && typeof m === "object" && m.url);
    if (j.data && typeof j.data === "object" && Array.isArray(j.data.medias)) {
      return j.data.medias.filter((m: any) => m && typeof m === "object" && m.url);
    }
    return [];
  }

  private pickId(j: any): string {
    const raw = j?.id || j?.pk || j?.url || String(nowMs());
    return String(raw).replace(/[^a-zA-Z0-9_-]+/g, "").slice(0, 64) || String(nowMs());
  }

  private pickSource(j: any): string {
    const s = String(j?.source || "media").toLowerCase().trim().replace(/[^a-z0-9]+/g, "");
    return s.slice(0, 24) || "media";
  }

  private pickTitle(j: any): string {
    const t = String(j?.title || j?.data?.title || "").trim();
    return t || this.pickId(j);
  }

  private pickAuthor(j: any): string {
    for (const k of ["author", "unique_id", "username", "user", "owner"]) {
      const v = j?.[k] ?? j?.data?.[k];
      if (v != null && String(v).trim()) return String(v).trim();
    }
    return "";
  }

  private pickDuration(j: any): number {
    const v = j?.duration ?? j?.data?.duration;
    if (typeof v === "number" && Number.isFinite(v)) return Math.floor(v);
    if (/^\d+$/.test(String(v || ""))) return Number(v);
    return 0;
  }

  private pickExtFromUrl(mediaUrl: string): string {
    try {
      const p = new URL(mediaUrl);
      const m = p.pathname.match(/\.([a-zA-Z0-9]{1,8})$/);
      if (!m) return "";
      return m[1].toLowerCase().replace(/[^a-z0-9]+/g, "");
    } catch {
      return "";
    }
  }

  private pickExtFromContentType(ct: string): string {
    const s = String(ct || "").split(";")[0].trim().toLowerCase();
    if (s.endsWith("jpeg")) return "jpg";
    if (s.endsWith("png")) return "png";
    if (s.endsWith("webp")) return "webp";
    if (s.endsWith("gif")) return "gif";
    if (s.endsWith("mp4")) return "mp4";
    if (s.endsWith("mpeg")) return "mp3";
    if (s.endsWith("aac")) return "aac";
    if (s.endsWith("ogg")) return "ogg";
    if (s.endsWith("audio/mp4")) return "m4a";
    return "";
  }

  private pickExt(media: any, mediaUrl: string, contentType = ""): string {
    const ext0 = String(media?.extension || "").toLowerCase().replace(/[^a-z0-9]+/g, "");
    if (ext0) return ext0;
    const ext1 = this.pickExtFromUrl(mediaUrl);
    if (ext1) return ext1;
    const ext2 = this.pickExtFromContentType(contentType);
    if (ext2) return ext2;
    return "bin";
  }

  private async ensureDir(dir: string): Promise<void> {
    await fsp.mkdir(dir, { recursive: true });
  }

  private async uniquePath(p: string): Promise<string> {
    try {
      await fsp.access(p);
    } catch {
      return p;
    }
    const d = path.dirname(p);
    const ext = path.extname(p);
    const base = path.basename(p, ext);
    for (let i = 1; i < 9999; i += 1) {
      const candidate = path.join(d, `${base}_${i}${ext}`);
      try {
        await fsp.access(candidate);
      } catch {
        return candidate;
      }
    }
    return path.join(d, `${base}_${Date.now()}${ext}`);
  }

  private needsMetaEnrich(title: string, author: string, sid: string, source: string): boolean {
    const src = String(source || "").toLowerCase();
    if (!["facebook", "threads", "instagram", "tiktok"].includes(src)) return false;
    const t = String(title || "").trim().toLowerCase();
    if (!author) return true;
    if (!t) return true;
    if (sid && t === String(sid).toLowerCase()) return true;
    return t.startsWith("http") || t.length < 4 || t === "tiktok";
  }

  private async fetchMetaFromWebpage(context: any, webpageUrl: string, source: string): Promise<{ title: string; author: string }> {
    const headers = { "user-agent": this.config.userAgent };
    let title = "";
    let author = "";

    const parseHtml = (html: string) => {
      const mTitle =
        html.match(/<meta[^>]+property=["']og:title["'][^>]+content=["']([^"']+)["']/i) ||
        html.match(/<meta[^>]+name=["']twitter:title["'][^>]+content=["']([^"']+)["']/i) ||
        html.match(/<title[^>]*>(.*?)<\/title>/is);
      const mAuthor =
        html.match(/<meta[^>]+name=["']author["'][^>]+content=["']([^"']+)["']/i) ||
        html.match(/<meta[^>]+property=["']article:author["'][^>]+content=["']([^"']+)["']/i);
      return {
        title: (mTitle?.[1] || "").replace(/\s+/g, " ").trim(),
        author: (mAuthor?.[1] || "").replace(/\s+/g, " ").trim()
      };
    };

    try {
      const r = await fetch(webpageUrl, { headers, redirect: "follow" });
      if (r.ok) {
        const html = await r.text();
        const parsed = parseHtml(html);
        title = parsed.title;
        author = parsed.author;
      }
    } catch {
      // ignore
    }

    // For tiktok: avoid slow page navigation; prefer fast HTML meta.
    if (source === "tiktok") {
      return { title, author };
    }

    if (title && author) return { title, author };

    let page: any;
    try {
      page = await context.newPage();
      await page.goto(webpageUrl, {
        waitUntil: "domcontentloaded",
        timeout: Math.min(20000, this.config.timeoutSec * 1000)
      });
      await page.waitForTimeout(600);
      if (!title) title = String(await page.title()).trim();
      if (!author) {
        const el = await page.$("meta[name='author']");
        if (el) author = String(await el.evaluate((x: any) => x.getAttribute("content") || "")).trim();
      }
      if (!author && title.includes("|")) author = title.split("|")[0].trim();
    } catch {
      // ignore
    } finally {
      if (page) await page.close().catch(() => {});
    }
    return { title, author };
  }

  private j2h(buf: Uint8Array, n: number): number {
    const imul = Math.imul;
    let a = (2783036115 + n) >>> 0;
    let h = (2134608921 ^ n) >>> 0;
    let i = (3572102818 + (n << 16)) >>> 0;
    for (let l = 0; l < n; l += 1) {
      a = (a ^ buf[l]) >>> 0;
      a = imul(a, 2654435769) >>> 0;
      a = ((a << 13) | (a >>> 19)) >>> 0;

      h = (h + a) >>> 0;
      h = imul(h, 1367130551) >>> 0;
      h = ((h << 17) | (h >>> 15)) >>> 0;

      i = (i ^ ((a + h) >>> 0)) >>> 0;
      i = imul(i, 1818371886) >>> 0;
      i = ((i << 11) | (i >>> 21)) >>> 0;

      a = (a + i) >>> 0;
    }
    a ^= a >>> 16;
    a = imul(a, 2246822507) >>> 0;
    a ^= a >>> 13;
    a = imul(a, 3266489909) >>> 0;
    a ^= a >>> 16;

    h ^= h >>> 16;
    h = imul(h, 3432918353) >>> 0;
    h ^= h >>> 13;
    h = imul(h, 461845907) >>> 0;
    h ^= h >>> 16;

    return (a ^ h ^ i) >>> 0;
  }

  private solvePow(challenge: string, difficulty: number): string {
    if (!challenge || !difficulty) return "";
    const shift = 32 - Number(difficulty) * 4;
    const prefix = new TextEncoder().encode(`${challenge}:`);
    for (let n = 0; n < 100000000; n += 1) {
      const suffix = new TextEncoder().encode(String(n));
      const buf = new Uint8Array(prefix.length + suffix.length);
      buf.set(prefix);
      buf.set(suffix, prefix.length);
      if ((this.j2h(buf, buf.length) >>> shift) === 0) return String(n);
    }
    return "";
  }

  private async autolinkWithCookie(context: any, url: string, csrf: string, apiToken: string): Promise<any | null> {
    const payload = { data: { url, unlock: Boolean(this.config.unlock) } };
    const resp = await context.request.post(Endpoints.autolink(), {
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
        Origin: BASE,
        Referer: Endpoints.home(),
        "User-Agent": this.config.userAgent,
        "x-csrf-token": csrf,
        Cookie: `api_token=${apiToken}; csrf_token=${csrf}`
      },
      data: payload,
      timeout: this.config.timeoutSec * 1000
    });
    if (resp.status() !== 200) return null;
    return await resp.json();
  }

  private async autolinkWithBearer(context: any, url: string, token: string): Promise<any | null> {
    const payload = { data: { url, unlock: Boolean(this.config.unlock) } };
    const resp = await context.request.post(Endpoints.autolink(), {
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
        Origin: BASE,
        Referer: Endpoints.home(),
        "User-Agent": this.config.userAgent,
        Authorization: `Bearer ${token}`
      },
      data: payload,
      timeout: this.config.timeoutSec * 1000
    });
    const txt = await resp.text();
    if (resp.status() !== 200) {
      if (resp.status() === 401) this.authCache.clearBearer(BASE);
      return null;
    }
    return JSON.parse(txt);
  }

  private async autolinkAuthFlow(context: any, targetUrl: string, skipHome = false): Promise<any> {
    const runHttp = async (): Promise<{ status: number; phase: string; text: string }> => {
      const b = await context.request.get(Endpoints.authBootstrap(), {
        timeout: this.config.timeoutSec * 1000,
        headers: {
          Accept: "application/json, text/plain, */*",
          Origin: BASE,
          Referer: Endpoints.home(),
          "User-Agent": this.config.userAgent
        }
      });
      const btxt = await b.text();
      if (b.status() !== 200) return { status: b.status(), phase: "bootstrap", text: btxt };
      const bj = JSON.parse(btxt || "{}");
      const nonce = String(bj.nonce || "").trim();
      if (!nonce) return { status: 500, phase: "bootstrap", text: "nonce_missing" };
      const solution = this.solvePow(String(bj.powChallenge || ""), Number(bj.powDifficulty || 0));

      const issueHeaders: Record<string, string> = {
        "X-Page-Nonce": nonce,
        Origin: BASE,
        Referer: Endpoints.home(),
        "User-Agent": this.config.userAgent,
        Accept: "application/json, text/plain, */*"
      };
      if (solution) issueHeaders["X-Pow-Solution"] = solution;

      const i = await context.request.post(Endpoints.authIssue(), {
        headers: issueHeaders,
        timeout: this.config.timeoutSec * 1000
      });
      const itxt = await i.text();
      if (i.status() !== 200) return { status: i.status(), phase: "issue", text: itxt };

      const ij = JSON.parse(itxt || "{}");
      const token = String(ij.accessToken || ij.token || ij?.data?.accessToken || "").trim();
      const expSec = Number(ij.expiresIn || ij?.data?.expiresIn || 180) || 180;
      if (!token) return { status: 500, phase: "issue", text: "token_missing" };
      this.authCache.setBearer(BASE, token, expSec);

      const r = await context.request.post(Endpoints.autolink(), {
        headers: {
          Accept: "application/json, text/plain, */*",
          "Content-Type": "application/json",
          Origin: BASE,
          Referer: Endpoints.home(),
          "User-Agent": this.config.userAgent,
          Authorization: `Bearer ${token}`
        },
        data: { data: { url: targetUrl, unlock: Boolean(this.config.unlock) } },
        timeout: this.config.timeoutSec * 1000
      });
      return { status: r.status(), phase: "autolink", text: await r.text() };
    };

    const session = this.authCache.getSessionCookie(BASE);
    if (session) {
      await context.addCookies([
        {
          name: "session",
          value: session,
          domain: "j2download.com",
          path: "/",
          secure: true,
          httpOnly: true,
          sameSite: "Lax"
        }
      ]);
    }

    let result = await runHttp();
    if (result.status === 401 && /session_required/i.test(result.text || "") && !skipHome) {
      const page = await context.newPage();
      try {
        await page.goto(Endpoints.home(), {
          waitUntil: "domcontentloaded",
          timeout: this.config.timeoutSec * 1000
        });
        await page.waitForTimeout(300);
      } finally {
        await page.close().catch(() => {});
      }
      const cookies = await context.cookies();
      const s = cookies.find((c: any) => c?.name === "session")?.value || "";
      if (s) this.authCache.setSessionCookie(BASE, s);
      result = await runHttp();
    }

    if (result.status !== 200) {
      throw new Error(`Autolink HTTP ${result.status} phase=${result.phase}: ${(result.text || "").slice(0, 300)}`);
    }
    return JSON.parse(result.text || "{}");
  }

  private async autolink(context: any, url: string, skipHome = false): Promise<any> {
    const cookies = await context.cookie
... [TRUNCATED]
```

