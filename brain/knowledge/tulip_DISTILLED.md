---
id: tulip
type: knowledge
owner: OA_Triage
---
# tulip
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# 🌷 Tulip

Tulip is a flow analyzer meant for use during Attack / Defence CTF competitions. It allows players to easily find some traffic related to their service and automatically generates python snippets to replicate attacks.

## Origins
Tulip was developed by Team Europe for use in the first International Cyber Security Challenge. The project is a fork of [flower](https://github.com/secgroup/flower), but it contains quite some changes:
* New front-end (typescript / react / tailwind)
* New ingestor code, based on gopacket
* IPv6 support
* Vastly improved filter and tagging system.
* Deep links for easy collaboration
* Added an http decoding pass for compressed data
* Synchronized with Suricata.
* Flow diffing
* Time and size-based plots for correlation.
* Linking HTTP sessions together based on cookies (Experimental*, disabled by default)
* PCAP-over-IP with BPF filtering support**

\* - to enable, add `-experimental` after `./assembler` in `docker-compose.yml`

\*\* - to enable, configure PCAP-over-IP server (e.g. [pcap-broker](https://github.com/fox-it/pcap-broker) as suggested in [PR 24](https://github.com/OpenAttackDefenseTools/tulip/pull/24)) and set `PCAP_OVER_IP` (and `BPF` if necessary) in `.env`

## Screenshots
![](./demo_images/demo1.png)
![](./demo_images/demo2.png)
![](./demo_images/demo3.png)

## Configuration
Before starting the stack, edit `services/api/configurations.py`:

```
vm_ip = "10.60.4.1"
services = [{"ip": vm_ip, "port": 18080, "name": "BIOMarkt"},
            {"ip": vm_ip, "port": 5555, "name": "SaaS"},
]
```

You can also edit this during the CTF, just rebuild the `api` service:
```
docker-compose up --build -d api
```

## Usage

The stack can be started with docker-compose, after creating an `.env` file. See `.env.example` as an example of how to configure your environment.
```
cp .env.example .env
# < Edit the .env file with your favourite text editor >
docker-compose up -d --build
```
To ingest traffic, it is recommended to create a shared bind mount with the docker-compose. One convenient way to set this up is as follows:
1. On the vulnbox, start a rotating packet sniffer (e.g. tcpdump, suricata, ...)
```bash
tcpdump -i eth0 -G 180 -w "traffic_%H:%M:%S.pcap" port 8080
```
2. Using rsync, copy complete captures to the machine running tulip (e.g. to /traffic)
```bash
rsync -avz -e ssh --progress root@10.0.0.2:/pcaps ./pcaps
```
3. Add a bind to the assembler service so it can read /traffic
   > (Just change `TRAFFIC_DIR_HOST` in `.env`)

The ingestor will use inotify to watch for new pcap's and suricata logs. No need to set a chron job.


## Suricata synchronization

### Run in Docker

Configure `SURICATA_DIR_HOST` in `.env`.

Create some rules (404 for testing):
```bash
. .env
mkdir -p ${SURICATA_DIR_HOST}/{etc,lib/rules,log}
echo 'alert tcp any any -> any any (msg: "404 Not Found"; http.stat_code; content:"404"; metadata: tag notfound; sid:4; rev: 1;)' >> ${SURICATA_DIR_HOST}/lib/rules/suricata.rules
```

After that run (default config for `eve.json` logging was good enough):

```bash
docker compose -f docker-compose-suricata.yml up -d --build
```

### Metadata
Tags are read from the metadata field of a rule. For example, here's a simple rule to detect a path traversal:
```
alert tcp any any -> any any (msg: "Path Traversal-../"; flow:to_server; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)
```
Once this rule is seen in traffic, the `path_traversal` tag will automatically be added to the filters in Tulip.

> [!NOTE]
>
> After editing Suricata rules (renaming or id change) please:
>
> Remove old logs: `rm ${SURICATA_DIR_HOST}/log/*` (otherwise old signatures will be repopulated).
>
> Restart Docker containers.
>
> If database was only restarted (not dropped), try cleaning tags/signatures manually.

### eve.json
Suricata alerts are read directly from the `eve.json` file. Because this file can get quite verbose when all extensions are enabled, it is recommended to strip the config down a fair bit. For example:
```yaml
# ...
  - eve-log:
      enabled: yes
      filetype: regular #regular|syslog|unix_dgram|unix_stream|redis
      filename: eve.json
      pcap-file: false
      community-id: false
      community-id-seed: 0
      types:
        - alert:
            metadata: yes
            # Enable the logging of tagged packets for rules using the
            # "tag" keyword.
            tagged-packets: yes
# ...
```

Sessions with matched alerts will be highlighted in the front-end and include which rule was matched.

# Security
Your Tulip instance will probably contain sensitive CTF information, like flags stolen from your machines. If you expose it to the internet and other people find it, you risk losing additional flags. It is recommended to host it on an internal network (for instance behind a VPN) or to put Tulip behind some form of authentication.

# Contributing
If you have an idea for a new feature, bug fixes, UX improvements, or other contributions, feel free to open a pull request or create an issue!      

# Credits
Tulip was written by [@RickdeJager](https://github.com/rickdejager) and [@Bazumo](https://github.com/bazumo), with additional help from [@Sijisu](https://github.com/sijisu). Thanks to our fellow Team Europe players and coaches for testing, feedback and suggestions. Finally, thanks to the team behind [flower](https://github.com/secgroup/flower) for opensourcing their tooling.

```

### File: frontend\package.json
```json
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "scripts": {
    "dev": "vite --host",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@heroicons/react": "^1.0.6",
    "@reduxjs/toolkit": "^1.8.5",
    "apexcharts": "^3.35.5",
    "buffer": "^6.0.3",
    "classnames": "^2.3.1",
    "color": "^4.2.3",
    "date-fns": "^2.28.0",
    "escape-string-regexp": "^5.0.0",
    "hexy": "^0.3.4",
    "http-parser-js": "^0.5.6",
    "react": "^18.0.0",
    "react-apexcharts": "^1.4.0",
    "react-diff-viewer": "^3.1.1",
    "react-dom": "^18.0.0",
    "react-hotkeys-hook": "^4.4.1",
    "react-redux": "^8.0.2",
    "react-router-dom": "^6.3.0",
    "react-virtuoso": "^2.12.1"
  },
  "devDependencies": {
    "@types/color": "^3.0.3",
    "@types/node": "^17.0.38",
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "@vitejs/plugin-react": "^1.3.0",
    "autoprefixer": "^10.4.7",
    "postcss": "^8.4.13",
    "prettier": "^2.6.2",
    "tailwindcss": "^3.0.24",
    "typescript": "^4.6.3",
    "vite": "^2.9.13"
  }
}

```

### File: services\README.md
```md
# Services



### General idea
We create pcap of N minutes on the virtual machine. We somehow download them, and use the `importer.py` script to analyze and import them into mongodb. The webapp does rest request to the webservices, that does query to mongodb.


### MongoDB structure
We use a single collection for all the pcaps
Each document will have:
```{
        "inx": //progressive flow index inside pcap
        "time": //start timestamp
        "duration": //end_time-start_time
        "src_ip": "127.0.0.1",
        "src_port": 1234 ,
        "dst_ip": "127.0.0.1",
        "dst_port": 1234,
        "contains_flag": //true if the importer have found that the flow contains a flag based on the env var regex
        "flow": [
            {
                "data": "...", // session data (capped at 15 MB)
                "from": "c" // "c" for client, "s" for server
                "time": //timestamp
            }, 
            ...
        ],

    }

```

# Services description
All the end-points return an object or an array of objects.

##### POST /query
Accept the following payload
```
    {
       flow.data: "regex on data field of flow",
       dst_ip: "1.2.3.4"
       dst_port: "1.2.3.4"
       time : {"$gte": from_millis,
               "$lt": to_millis}
    }

```
It returns an array of documents, WITHOUT the "flow" field

##### GET /services
Returns informations about all services. It is configurable on `configurations.py`

##### GET /flow/(flow_id)
Returns the all document with `flow_id` id, including the field `flow`

##### GET /star/(flow_id)/(0,1)
Set the flow favourite (1) or not (0)

##### POST /to_python_request/(tokenize)
convert the request to python syntax. Tokenize is used to toggle the auto-parsing of args.

##### GET /to_pwn/(id)
Convert the flow with the specified id in pwntools syntax

```

### File: services\api\requirements.txt
```txt
Flask_Cors
Flask
requests
gunicorn
python-dateutil
psycopg[binary,pool]

```

### File: dev.sh
```sh
#!/bin/bash

# Requires internet
# docker-compose -f docker-compose.yml.dev up

docker-compose up -d mongo
docker-compose up -d api

```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions
Please only report issues that are present in the latest commit on the master branch.

## Reporting a Vulnerability
As this is an A/D CTF tool, most people will not run long-term publicly reachable instances. As such, feel free to report security issues directly in the github issues tracker.  
  
 If you prefer an email contact, you can email `tulip-sec<at>bricked.tech`.

```

### File: start.sh
```sh
#!/bin/bash

source .env

if [ -n "$FLAGID_SCRAPE" ]; then
  docker-compose -f docker-compose-flagid.yml up;
else
  docker-compose up 
fi


```

### File: test.sh
```sh
#!/bin/bash

docker compose -f docker-compose-test.yml up --build

```

### File: .devcontainer\devcontainer.json
```json
// For format details, see https://aka.ms/devcontainer.json. For config options, see the README at:
// https://github.com/microsoft/vscode-dev-containers/tree/v0.234.0/containers/docker-existing-docker-compose
// If you want to run as a non-root user in the container, see .devcontainer/docker-compose.yml.
{
	"name": "Existing Docker Compose (Extend)",

	// Update the 'dockerComposeFile' list if you have more compose files or use different names.
	// The .devcontainer/docker-compose.yml file contains any overrides you need/want to make.
	"dockerComposeFile": [
		"../docker-compose.yml",
		"docker-compose.yml"
	],

	// The 'service' property is the name of the service for the container that VS Code should
	// use. Update this value and .devcontainer/docker-compose.yml to the real service name.
	"service": "flower-node",

	// The optional 'workspaceFolder' property is the path VS Code should open by default when
	// connected. This is typically a file mount in .devcontainer/docker-compose.yml
	"workspaceFolder": "/workspace",

	// Set *default* container specific settings.json values on container create.
	"settings": {},

	// Add the IDs of extensions you want installed when the container is created.
	"extensions": []

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Uncomment the next line if you want start specific services in your Docker Compose config.
	// "runServices": [],

	// Uncomment the next line if you want to keep your containers running after VS Code shuts down.
	// "shutdownAction": "none",

	// Uncomment the next line to run commands after the container is created - for example installing curl.
	// "postCreateCommand": "apt-get update && apt-get install -y curl",

	// Uncomment to connect as a non-root user if you've added one. See https://aka.ms/vscode-remote/containers/non-root.
	// "remoteUser": "vscode"
}

```

### File: frontend\index.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tulip</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### File: frontend\postcss.config.js
```js
module.exports = {
  plugins: {
    'tailwindcss/nesting': {},
    tailwindcss: {},
    autoprefixer: {},
  },
}

```

### File: frontend\tailwind.config.js
```js
module.exports = {
  content: [
    './src/**/*.tsx',

  ],
  presets: [],
  darkMode: 'media', // or 'class'
  theme: {
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1536px',
    },
    colors: ({ colors }) => ({
      inherit: colors.inherit,
      current: colors.current,
      transparent: colors.transparent,
      black: colors.black,
      white: colors.white,
      slate: colors.slate,
      gray: colors.gray,
      zinc: colors.zinc,
      neutral: colors.neutral,
      stone: colors.stone,
      red: colors.red,
      orange: colors.orange,
      amber: colors.amber,
      yellow: colors.yellow,
      lime: colors.lime,
      green: colors.green,
      emerald: colors.emerald,
      teal: colors.teal,
      cyan: colors.cyan,
      sky: colors.sky,
      blue: colors.blue,
      indigo: colors.indigo,
      violet: colors.violet,
      purple: colors.purple,
      fuchsia: colors.fuchsia,
      pink: colors.pink,
      rose: colors.rose,
    }),
    columns: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
      8: '8',
      9: '9',
      10: '10',
      11: '11',
      12: '12',
      '3xs': '16rem',
      '2xs': '18rem',
      xs: '20rem',
      sm: '24rem',
      md: '28rem',
      lg: '32rem',
      xl: '36rem',
      '2xl': '42rem',
      '3xl': '48rem',
      '4xl': '56rem',
      '5xl': '64rem',
      '6xl': '72rem',
      '7xl': '80rem',
    },
    spacing: {
      px: '1px',
      0: '0px',
      0.5: '0.125rem',
      1: '0.25rem',
      1.5: '0.375rem',
      2: '0.5rem',
      2.5: '0.625rem',
      3: '0.75rem',
      3.5: '0.875rem',
      4: '1rem',
      5: '1.25rem',
      6: '1.5rem',
      7: '1.75rem',
      8: '2rem',
      9: '2.25rem',
      10: '2.5rem',
      11: '2.75rem',
      12: '3rem',
      14: '3.5rem',
      16: '4rem',
      20: '5rem',
      24: '6rem',
      28: '7rem',
      32: '8rem',
      36: '9rem',
      40: '10rem',
      44: '11rem',
      48: '12rem',
      52: '13rem',
      56: '14rem',
      60: '15rem',
      64: '16rem',
      72: '18rem',
      80: '20rem',
      96: '24rem',
    },
    animation: {
      none: 'none',
      spin: 'spin 1s linear infinite',
      ping: 'ping 1s cubic-bezier(0, 0, 0.2, 1) infinite',
      pulse: 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      bounce: 'bounce 1s infinite',
    },
    aspectRatio: {
      auto: 'auto',
      square: '1 / 1',
      video: '16 / 9',
    },
    backdropBlur: ({ theme }) => theme('blur'),
    backdropBrightness: ({ theme }) => theme('brightness'),
    backdropContrast: ({ theme }) => theme('contrast'),
    backdropGrayscale: ({ theme }) => theme('grayscale'),
    backdropHueRotate: ({ theme }) => theme('hueRotate'),
    backdropInvert: ({ theme }) => theme('invert'),
    backdropOpacity: ({ theme }) => theme('opacity'),
    backdropSaturate: ({ theme }) => theme('saturate'),
    backdropSepia: ({ theme }) => theme('sepia'),
    backgroundColor: ({ theme }) => theme('colors'),
    backgroundImage: {
      none: 'none',
      'gradient-to-t': 'linear-gradient(to top, var(--tw-gradient-stops))',
      'gradient-to-tr': 'linear-gradient(to top right, var(--tw-gradient-stops))',
      'gradient-to-r': 'linear-gradient(to right, var(--tw-gradient-stops))',
      'gradient-to-br': 'linear-gradient(to bottom right, var(--tw-gradient-stops))',
      'gradient-to-b': 'linear-gradient(to bottom, var(--tw-gradient-stops))',
      'gradient-to-bl': 'linear-gradient(to bottom left, var(--tw-gradient-stops))',
      'gradient-to-l': 'linear-gradient(to left, var(--tw-gradient-stops))',
      'gradient-to-tl': 'linear-gradient(to top left, var(--tw-gradient-stops))',
    },
    backgroundOpacity: ({ theme }) => theme('opacity'),
    backgroundPosition: {
      bottom: 'bottom',
      center: 'center',
      left: 'left',
      'left-bottom': 'left bottom',
      'left-top': 'left top',
      right: 'right',
      'right-bottom': 'right bottom',
      'right-top': 'right top',
      top: 'top',
    },
    backgroundSize: {
      auto: 'auto',
      cover: 'cover',
      contain: 'contain',
    },
    blur: {
      0: '0',
      none: '0',
      sm: '4px',
      DEFAULT: '8px',
      md: '12px',
      lg: '16px',
      xl: '24px',
      '2xl': '40px',
      '3xl': '64px',
    },
    brightness: {
      0: '0',
      50: '.5',
      75: '.75',
      90: '.9',
      95: '.95',
      100: '1',
      105: '1.05',
      110: '1.1',
      125: '1.25',
      150: '1.5',
      200: '2',
    },
    borderColor: ({ theme }) => ({
      ...theme('colors'),
      DEFAULT: theme('colors.gray.200', 'currentColor'),
    }),
    borderOpacity: ({ theme }) => theme('opacity'),
    borderRadius: {
      none: '0px',
      sm: '0.125rem',
      DEFAULT: '0.25rem',
      md: '0.375rem',
      lg: '0.5rem',
      xl: '0.75rem',
      '2xl': '1rem',
      '3xl': '1.5rem',
      full: '9999px',
    },
    /*
    borderSpacing: ({ theme }) => ({
      ...theme('spacing'),
    }),
    */
    borderWidth: {
      DEFAULT: '1px',
      0: '0px',
      2: '2px',
      4: '4px',
      8: '8px',
    },
    boxShadow: {
      sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
      DEFAULT: '0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
      md: '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
      lg: '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
      xl: '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)',
      '2xl': '0 25px 50px -12px rgb(0 0 0 / 0.25)',
      inner: 'inset 0 2px 4px 0 rgb(0 0 0 / 0.05)',
      none: 'none',
    },
    boxShadowColor: ({ theme }) => theme('colors'),
    caretColor: ({ theme }) => theme('colors'),
    accentColor: ({ theme }) => ({
      ...theme('colors'),
      auto: 'auto',
    }),
    contrast: {
      0: '0',
      50: '.5',
      75: '.75',
      100: '1',
      125: '1.25',
      150: '1.5',
      200: '2',
    },
    container: {},
    content: {
      none: 'none',
    },
    cursor: {
      auto: 'auto',
      default: 'default',
      pointer: 'pointer',
      wait: 'wait',
      text: 'text',
      move: 'move',
      help: 'help',
      'not-allowed': 'not-allowed',
      none: 'none',
      'context-menu': 'context-menu',
      progress: 'progress',
      cell: 'cell',
      crosshair: 'crosshair',
      'vertical-text': 'vertical-text',
      alias: 'alias',
      copy: 'copy',
      'no-drop': 'no-drop',
      grab: 'grab',
      grabbing: 'grabbing',
      'all-scroll': 'all-scroll',
      'col-resize': 'col-resize',
      'row-resize': 'row-resize',
      'n-resize': 'n-resize',
      'e-resize': 'e-resize',
      's-resize': 's-resize',
      'w-resize': 'w-resize',
      'ne-resize': 'ne-resize',
      'nw-resize': 'nw-resize',
      'se-resize': 'se-resize',
      'sw-resize': 'sw-resize',
      'ew-resize': 'ew-resize',
      'ns-resize': 'ns-resize',
      'nesw-resize': 'nesw-resize',
      'nwse-resize': 'nwse-resize',
      'zoom-in': 'zoom-in',
      'zoom-out': 'zoom-out',
    },
    divideColor: ({ theme }) => theme('borderColor'),
    divideOpacity: ({ theme }) => theme('borderOpacity'),
    divideWidth: ({ theme }) => theme('borderWidth'),
    dropShadow: {
      sm: '0 1px 1px rgb(0 0 0 / 0.05)',
      DEFAULT: ['0 1px 2px rgb(0 0 0 / 0.1)', '0 1px 1px rgb(0 0 0 / 0.06)'],
      md: ['0 4px 3px rgb(0 0 0 / 0.07)', '0 2px 2px rgb(0 0 0 / 0.06)'],
      lg: ['0 10px 8px rgb(0 0 0 / 0.04)', '0 4px 3px rgb(0 0 0 / 0.1)'],
      xl: ['0 20px 13px rgb(0 0 0 / 0.03)', '0 8px 5px rgb(0 0 0 / 0.08)'],
      '2xl': '0 25px 25px rgb(0 0 0 / 0.15)',
      none: '0 0 #0000',
    },
    fill: ({ theme }) => theme('colors'),
    grayscale: {
      0: '0',
      DEFAULT: '100%',
    },
    hueRotate: {
      0: '0deg',
      15: '15deg',
      30: '30deg',
      60: '60deg',
      90: '90deg',
      180: '180deg',
    },
    invert: {
      0: '0',
      DEFAULT: '100%',
    },
    flex: {
      1: '1 1 0%',
      auto: '1 1 auto',
      initial: '0 1 auto',
      none: 'none',
    },
    flexBasis: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      '1/5': '20%',
      '2/5': '40%',
      '3/5': '60%',
      '4/5': '80%',
      '1/6': '16.666667%',
      '2/6': '33.333333%',
      '3/6': '50%',
      '4/6': '66.666667%',
      '5/6': '83.333333%',
      '1/12': '8.333333%',
      '2/12': '16.666667%',
      '3/12': '25%',
      '4/12': '33.333333%',
      '5/12': '41.666667%',
      '6/12': '50%',
      '7/12': '58.333333%',
      '8/12': '66.666667%',
      '9/12': '75%',
      '10/12': '83.333333%',
      '11/12': '91.666667%',
      full: '100%',
    }),
    flexGrow: {
      0: '0',
      DEFAULT: '1',
    },
    flexShrink: {
      0: '0',
      DEFAULT: '1',
    },
    fontFamily: {
      sans: [
        'Recursive',
        'ui-sans-serif',
        'system-ui',
        '-apple-system',
        'BlinkMacSystemFont',
        '"Segoe UI"',
        'Roboto',
        '"Helvetica Neue"',
        'Arial',
        '"Noto Sans"',
        'sans-serif',
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"',
        '"Noto Color Emoji"',
      ],
      serif: ['ui-serif', 'Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif']
    },
    fontSize: {
      xs: ['0.75rem', { lineHeight: '1rem' }],
      sm: ['0.875rem', { lineHeight: '1.25rem' }],
      base: ['1rem', { lineHeight: '1.5rem' }],
      lg: ['1.125rem', { lineHeight: '1.75rem' }],
      xl: ['1.25rem', { lineHeight: '1.75rem' }],
      '2xl': ['1.5rem', { lineHeight: '2rem' }],
      '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
      '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
      '5xl': ['3rem', { lineHeight: '1' }],
      '6xl': ['3.75rem', { lineHeight: '1' }],
      '7xl': ['4.5rem', { lineHeight: '1' }],
      '8xl': ['6rem', { lineHeight: '1' }],
      '9xl': ['8rem', { lineHeight: '1' }],
    },
    fontWeight: {
      thin: '100',
      extralight: '200',
      light: '300',
      normal: '400',
      medium: '500',
      semibold: '600',
      bold: '700',
      extrabold: '800',
      black: '900',
    },
    gap: ({ theme }) => theme('spacing'),
    gradientColorStops: ({ theme }) => theme('colors'),
    gridAutoColumns: {
      auto: 'auto',
      min: 'min-content',
      max: 'max-content',
      fr: 'minmax(0, 1fr)',
    },
    gridAutoRows: {
      auto: 'auto',
      min: 'min-content',
      max: 'max-content',
      fr: 'minmax(0, 1fr)',
    },
    gridColumn: {
      auto: 'auto',
      'span-1': 'span 1 / span 1',
      'span-2': 'span 2 / span 2',
      'span-3': 'span 3 / span 3',
      'span-4': 'span 4 / span 4',
      'span-5': 'span 5 / span 5',
      'span-6': 'span 6 / span 6',
      'span-7': 'span 7 / span 7',
      'span-8': 'span 8 / span 8',
      'span-9': 'span 9 / span 9',
      'span-10': 'span 10 / span 10',
      'span-11': 'span 11 / span 11',
      'span-12': 'span 12 / span 12',
      'span-full': '1 / -1',
    },
    gridColumnEnd: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
      8: '8',
      9: '9',
      10: '10',
      11: '11',
      12: '12',
      13: '13',
    },
    gridColumnStart: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
      8: '8',
      9: '9',
      10: '10',
      11: '11',
      12: '12',
      13: '13',
    },
    gridRow: {
      auto: 'auto',
      'span-1': 'span 1 / span 1',
      'span-2': 'span 2 / span 2',
      'span-3': 'span 3 / span 3',
      'span-4': 'span 4 / span 4',
      'span-5': 'span 5 / span 5',
      'span-6': 'span 6 / span 6',
      'span-full': '1 / -1',
    },
    gridRowStart: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
    },
    gridRowEnd: {
      auto: 'auto',
      1: '1',
      2: '2',
      3: '3',
      4: '4',
      5: '5',
      6: '6',
      7: '7',
    },
    gridTemplateColumns: {
      none: 'none',
      1: 'repeat(1, minmax(0, 1fr))',
      2: 'repeat(2, minmax(0, 1fr))',
      3: 'repeat(3, minmax(0, 1fr))',
      4: 'repeat(4, minmax(0, 1fr))',
      5: 'repeat(5, minmax(0, 1fr))',
      6: 'repeat(6, minmax(0, 1fr))',
      7: 'repeat(7, minmax(0, 1fr))',
      8: 'repeat(8, minmax(0, 1fr))',
      9: 'repeat(9, minmax(0, 1fr))',
      10: 'repeat(10, minmax(0, 1fr))',
      11: 'repeat(11, minmax(0, 1fr))',
      12: 'repeat(12, minmax(0, 1fr))',
    },
    gridTemplateRows: {
      none: 'none',
      1: 'repeat(1, minmax(0, 1fr))',
      2: 'repeat(2, minmax(0, 1fr))',
      3: 'repeat(3, minmax(0, 1fr))',
      4: 'repeat(4, minmax(0, 1fr))',
      5: 'repeat(5, minmax(0, 1fr))',
      6: 'repeat(6, minmax(0, 1fr))',
    },
    height: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      '1/5': '20%',
      '2/5': '40%',
      '3/5': '60%',
      '4/5': '80%',
      '1/6': '16.666667%',
      '2/6': '33.333333%',
      '3/6': '50%',
      '4/6': '66.666667%',
      '5/6': '83.333333%',
      full: '100%',
      screen: '100vh',
      min: 'min-content',
      max: 'max-content',
      fit: 'fit-content',
    }),
    inset: ({ theme }) => ({
      auto: 'auto',
      ...theme('spacing'),
      '1/2': '50%',
      '1/3': '33.333333%',
      '2/3': '66.666667%',
      '1/4': '25%',
      '2/4': '50%',
      '3/4': '75%',
      full: '100%',
    }),
    keyframes: {
      spin: {
        to: {
          transform: 'rotate(360deg)',
        },
      },
      ping: {
        '75%, 100%': {
          transform: 'scale(2)',
          opacity: '0',
        },
      },
      pulse: {
        '50%': {
          opacity: '.5',
        },
      },
      bounce: {
        '0%, 100%': {
          transform: 'translateY(-25%)',
          animationTimingFunction: 'cubic-bezier(0.8,0,1,1)',
        },
        '50%': {
          transform: 'none',
          animationTimingFunction: 'cubic-bezier(0,0,0.2,1)',
        },
      },
    },
    letterSpacing: {
      tighter: '-0.05em',
      tight: '-0.025em',
      normal: '0em',
      wide: '0.025em',
      wider: '0.05em',
      widest: '0.1em',
    },
    lineHeight: {
      none: '1',
      tight: '1.25',
      snug: '1.375',
      normal: '1.5',
      relaxed: '1.625',
      loose: '2',
      3: '.75rem',
      4: '1rem',
      5: '1.25rem',
      6: '1.5rem',
      7: '1.75rem',
      8: '2rem',
      9: '2.25rem',
      10: '2.5rem',
    },
    listStyleType: {
      none: 'none',
      disc: 'disc',
      
... [TRUNCATED]
```

### File: frontend\tsconfig.json
```json
{
  "compilerOptions": {
    "target": "es2020",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ESNext", "es2020"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": false,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}

```

### File: frontend\tsconfig.node.json
```json
{
  "compilerOptions": {
    "composite": true,
    "module": "esnext",
    "moduleResolution": "node"
  },
  "include": ["vite.config.ts"]
}

```

### File: frontend\vite.config.ts
```ts
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {


  const env = loadEnv(mode, process.cwd(), '')

  return ({
    plugins: [react()],
    build: {
      target: ['es2020']
    },
    server: {
      proxy: {
        '/api': {
          target: env["API_SERVER_ENDPOINT"] ?? "http://localhost:5000/",
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '')
        }
      }
    }
  })
})

```

### File: frontend\src\api.ts
```ts
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

import { API_BASE_PATH } from "./const";
import {
  Service,
  FullFlow,
  TickInfo,
  Flow,
  FlowsQuery,
  StatsQuery,
  Stats,
  TicksAttackInfo,
  TicksAttackQuery,
} from "./types";

function base64DecodeUnicode(str: string) : string {
  const text = atob(str);
  const bytes = new Uint8Array(text.length);
  for(let i = 0; i < text.length; i++)
    bytes[i] = text.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}

export const tulipApi = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: API_BASE_PATH }),
  endpoints: (builder) => ({
    getServices: builder.query<Service[], void>({
      query: () => "/services",
    }),
    getFlagRegex: builder.query<string, void>({
      query: () => "/flag_regex",
    }),
    getFlow: builder.query<FullFlow, string>({
      query: (id) => `/flow/${id}`,
      transformResponse: (flow: any): FullFlow => {
        const representations: any = {};

        for(const item of flow.items) {
          if(!(item.kind in representations))
            representations[item.kind] = { type: item.kind, flow: [] };
          representations[item.kind].flow.push({
            from: item.direction,
            data: base64DecodeUnicode(item.data),
            b64: item.data,
            time: new Date(item.time).getTime(),
          });
        }

        return {
          id: flow.id,
          src_port: flow.port_src,
          dst_port: flow.port_dst,
          src_ip: flow.ip_src,
          dst_ip: flow.ip_dst,
          time: new Date(flow.time).getTime(),
          duration: +(flow.duration * 1000).toFixed(0),
          num_packets: flow.packets_count,
          parent_id: flow.link_parent_id,
          child_id: flow.link_child_id,
          tags: flow.tags,
          flags: flow.flags,
          flagids: flow.flagids,
          filename: flow.pcap_name,
          service_tag: "",
          suricata: [],
          signatures: flow.signatures,
          flow: Object.values(representations),
        };
      },
    }),
    getFlows: builder.query<Flow[], FlowsQuery>({
      query: (query) => ({
        url: `/query`,
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: query,
      }),
      transformResponse: (response: Array<any>) => {
        return response.map((flow: any): Flow => ({
          id: flow.id,
          src_port: flow.port_src,
          dst_port: flow.port_dst,
          src_ip: flow.ip_src,
          dst_ip: flow.ip_dst,
          time: new Date(flow.time).getTime(),
          duration: +(flow.duration * 1000).toFixed(0),
          num_packets: flow.packets_count,
          parent_id: flow.link_parent_id,
          child_id: flow.link_child_id,
          tags: flow.tags,
          flags: flow.flags,
          flagids: flow.flagids,
          filename: flow.pcap_name,
          service_tag: "",
          suricata: [],
        }));
      },
    }),
    getStats: builder.query<Stats[], StatsQuery>({
      query: (query) => ({
        url: `/stats`,
        method: "GET",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        params: {
          service: query.service,
          tick_from: query.tick_from,
          tick_to: query.tick_to,
        }
      })
    }),
    getTags: builder.query<string[], void>({
      query: () => `/tags`,
    }),
    getTickInfo: builder.query<TickInfo, void>({
      query: () => `/tick_info`,
    }),
    getUnderAttack: builder.query<TicksAttackInfo, TicksAttackQuery>({
      query: (query) => ({
        url: '/under_attack',
        params: {
          from_tick: query.from_tick,
          to_tick: query.to_tick,
        }
      }),
    }),
    toPwnTools: builder.query<string, string>({
      query: (id) => ({ url: `/to_pwn/${id}`, responseHandler: "text" }),
    }),
    toSinglePythonRequest: builder.query<
      string,
      { body: string; id: string; item_index: number; tokenize: boolean }
    >({
      query: ({ body, id, item_index, tokenize }) => ({
        url: `/to_single_python_request?tokenize=${
          tokenize ? "1" : "0"
        }&id=${id}&index=${item_index}`,
        method: "POST",
        responseHandler: "text",
        headers: {
          "Content-Type": "text/plain;charset=UTF-8",
        },
        body,
      }),
    }),
    toFullPythonRequest: builder.query<string, string>({
      query: (id) => ({
        url: `/to_python_request/${id}`,
        responseHandler: "text",
      }),
    }),
    starFlow: builder.mutation<unknown, { id: string; star: boolean }>({
      query: ({ id, star }) => ({
        url: `/star`,
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: { id, star },
      }),
      // TODO: optimistic cache update

      async onQueryStarted({ id, star }, { dispatch, queryFulfilled }) {
        // `updateQueryData` requires the endpoint name and cache key arguments,
        // so it knows which piece of cache state to update
        const patchResult = dispatch(
          tulipApi.util.updateQueryData("getFlows", {service: "undefined", tags_include: [], tags_exclude:[]}, (flows) => {
            // The `flows` is Immer-wrapped and can be "mutated" like in createSlice
            const flow = flows.find((flow) => flow.id === id);
            if (flow) {
              if (star) {
                flow.tags.push("starred");
              } else {
                flow.tags = flow.tags.filter((tag) => tag != "starred");
              }
            }
          })
        );
        try {
          await queryFulfilled;
        } catch {
          patchResult.undo();
        }
      },
    }),
  }),
});

export const {
  useGetServicesQuery,
  useGetFlagRegexQuery,
  useGetFlowQuery,
  useGetFlowsQuery,
  useLazyGetFlowsQuery,
  useGetTagsQuery,
  useGetTickInfoQuery,
  useLazyToPwnToolsQuery,
  useLazyToFullPythonRequestQuery,
  useToSinglePythonRequestQuery,
  useStarFlowMutation,
  useGetStatsQuery,
  useGetUnderAttackQuery,
} = tulipApi;

```

### File: frontend\src\App.css
```css


/* Grid */
.grid-container {
  display: grid;
  grid-template-columns: 400px 1fr;
  grid-template-rows: 50px calc(100vh - 50px);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}

.flow-list-area {
  grid-area: 2 / 1 / 3 / 2;
  border-right: 1px solid rgba(0, 0, 0, 0.2);
  overflow: auto;
}

.flow-details-area {
  grid-area: 2 / 2 / 3 / 3;
  overflow-y: auto;
  overflow-x: auto;
}

.header-area {
  grid-area: 1 / 1 / 2 / 3;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

/* no need for footer
.footer-area {
  grid-area: 3 / 1 / 4 / 3;
}*/


/* Header */

.header {
  display: flex;
  align-items: center;
  height: 50px;
  @apply gap-3;

  input {
    @apply flex bg-gray-200 py-1 px-3 rounded-md;
  }

  .header-icon {
    @apply text-2xl pl-5 pr-2
  }
  
}

.text-mono {
  font-family: 'Recursive';
  --mono: "MONO" 1;
  font-variation-settings: var(--mono);
}


/* Loading state */
.sidebar-loading {
  background: #eee;
  background: linear-gradient(90deg, #ececec 8%, #f5f5f5 18%, #ececec 33%);
  border-radius: 5px;
  background-size: 200% 100%;
  animation: 3s shine linear infinite;
}

@keyframes shine {
  to {
    background-position-x: -400%;
  }
}
```

### File: frontend\src\const.ts
```ts
export const API_BASE_PATH = `${window.location.origin}/api`;

export const TEXT_FILTER_KEY = "text";
export const SERVICE_FILTER_KEY = "service";
export const START_FILTER_KEY = "start";
export const END_FILTER_KEY = "end";
export const FIRST_DIFF_KEY = "first";
export const SECOND_DIFF_KEY = "second";
export const REPR_ID_KEY = "reprid";
export const CORRELATION_MODE_KEY = "correlation";

export const SERVICE_REFETCH_INTERVAL_MS = 15000;
export const TICK_REFETCH_INTERVAL_MS = 10000;
export const FLOW_LIST_REFETCH_INTERVAL_MS = 30000;
export const UNDER_ATTACK_REFETCH_INTERVAL_MS = 30000;
export const MAX_LENGTH_FOR_HIGHLIGHT = 400000;

export const FORCE_REFETCH_ON_STAR = true;
```

### File: frontend\src\index.css
```css
@import url('https://fonts.googleapis.com/css2?family=Recursive:wght,MONO@300..800,0..1&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;
```

### File: frontend\src\tick.ts
```ts
import { useSearchParams } from "react-router-dom";

import {
  END_FILTER_KEY,
  START_FILTER_KEY,
  TICK_REFETCH_INTERVAL_MS,
} from "./const";
import { useGetTickInfoQuery } from "./api";

export function getTickStuff() {
  const { data: tickInfoData } = useGetTickInfoQuery(undefined, {
    pollingInterval: TICK_REFETCH_INTERVAL_MS,
  });
  const startDate = tickInfoData?.startDate ?? "1970-01-01T00:00:00Z";
  const tickLength = tickInfoData?.tickLength ?? 1000;
  const flagLifetime = tickInfoData?.flagLifetime ?? 0;
  const currentTick = unixTimeToTick(new Date().valueOf());

  function tickToUnixTime(tick: number): number {
    return new Date(startDate).valueOf() + tickLength * tick;;
  }

  function unixTimeToTick(unixTime: number): number {
    return Math.floor(
      (unixTime - new Date(startDate).valueOf()) / tickLength
    );
  }

  let [searchParams, setSearchParams] = useSearchParams();
  const startTimeParam = searchParams.get(START_FILTER_KEY);
  const endTimeParam = searchParams.get(END_FILTER_KEY);
  const startTimeParamUnix = startTimeParam === null ? undefined : parseInt(startTimeParam);
  const endTimeParamUnix = endTimeParam === null ? undefined : parseInt(endTimeParam);
  const startTickParam = startTimeParamUnix === undefined ? undefined : unixTimeToTick(startTimeParamUnix);
  const endTickParam = endTimeParamUnix === undefined ? undefined : unixTimeToTick(endTimeParamUnix);

  function setTimeParam(startTick: number | null, param: string) {
    if (startTick === null) {
      searchParams.delete(param);
    } else {
      searchParams.set(param, tickToUnixTime(startTick).toString());
    }
    setSearchParams(searchParams);
  }

  function setToLastnTicks(n: number) {
    const startTick = (currentTick ?? 0) - n;
    const endTick = (currentTick ?? 0) + 1; // to be sure
    setTimeParam(startTick, START_FILTER_KEY);
    setTimeParam(endTick, END_FILTER_KEY);
  }

  return {
    startDate,
    tickLength,
    flagLifetime,
    currentTick,
    tickToUnixTime,
    unixTimeToTick,
    startTickParam,
    endTickParam,
    setTimeParam,
    setToLastnTicks,
  }

}

```

### File: frontend\src\types.ts
```ts
export interface Flow {
  id: Id;
  src_port: number;
  dst_port: number;
  src_ip: string;
  dst_ip: string;
  time: number;
  duration: number;
  // TODO: Get this from backend instead of hacky workaround
  service_tag: string;
  num_packets: number;
  parent_id: Id;
  child_id: Id;
  tags: string[];
  flags: string[];
  flagids: string[];
  suricata: number[];
  filename: string;
}

export interface TickInfo {
  startDate: string;
  tickLength: number;
  flagLifetime: number;
}

export interface FullFlow extends Flow {
  signatures: Signature[];
  flow: FlowRepresentation[];
}

export type Id = string;

export interface FlowRepresentation {
  type: string;
  flow: FlowData[];
}

export interface FlowData {
  from: string;
  data: string;
  b64: string;
  time: number;
}

export interface Signature {
  id: number;
  message: string;
  action: string;
}

// TODO: pagination WTF
export interface FlowsQuery {
  // Text filter
  regex_insensitive?: string;
  // Service filter
  // TODO: Why not use service name here?
  service?: string;
  ip_dst?: string;
  port_dst?: number;
  time_from?: string;
  time_to?: string;
  tags_include?: string[];
  tags_exclude?: string[];
  tag_intersection_mode?: "AND" | "OR";
  flags?: string[];
  flagids?: string[];
}

export interface StatsQuery {
  service: string;
  tick_from: number;
  tick_to: number;
}

export interface Stats {
  [key: string]: number; // little hack to make typescript happy
  tick: number;
  tag_flag_in: number;
  tag_flag_out: number;
  tag_blocked: number;
  tag_suricata: number;
  tag_enemy: number;
  flag_in: number;
  flag_out: number;
};

export type Service = {
  ip: string;
  port: number;
  name: string;
};

export type TicksAttackInfo = Record<number, Record<string, number>>;

export interface TicksAttackQuery {
  from_tick: number;
  to_tick: number;
}

```

### File: frontend\src\vite-env.d.ts
```ts
/// <reference types="vite/client" />

```

### File: frontend\types\twin.d.ts
```ts
import 'twin.macro'
import styledImport, { CSSProp, css as cssImport } from 'styled-components'

// Type hack for babel macro

declare module 'twin.macro' {
    // The styled and css imports
    const styled: typeof styledImport
    const css: typeof cssImport
}

declare module 'react' {
    // The css prop
    interface HTMLAttributes<T> extends DOMAttributes<T> {
        css?: CSSProp
        tw?: string
    }
    // The inline svg css prop
    interface SVGProps<T> extends SVGProps<SVGSVGElement> {
        css?: CSSProp
        tw?: string
    }
}

// The 'as' prop on styled components
declare global {
    namespace JSX {
        interface IntrinsicAttributes<T> extends DOMAttributes<T> {
            as?: string | Element
        }
    }
}
```

### File: services\api\configurations.py
```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Flower.
#
# Copyright ©2018 Nicolò Mazzucato
# Copyright ©2018 Antonio Groza
# Copyright ©2018 Brunello Simone
# Copyright ©2018 Alessio Marotta
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# Flower is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Flower is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Flower.  If not, see <https://www.gnu.org/licenses/>.

import os
from pathlib import Path

traffic_dir = Path(os.getenv("TULIP_TRAFFIC_DIR", "/traffic"))
dump_pcaps_dir = Path(os.getenv("DUMP_PCAPS", "/traffic"))
tick_length = os.getenv("TICK_LENGTH", 2*60*1000)
flag_lifetime = os.getenv("FLAG_LIFETIME", 5)
start_date = os.getenv("TICK_START", "2018-06-27T13:00:00+02:00")
flag_regex = os.getenv("FLAG_REGEX", "[A-Z0-9]{31}=")
vm_ip = os.getenv("VM_IP", "10.10.3.1")
visualizer_url = os.getenv("VISUALIZER_URL", "http://127.0.0.1:1337")

vm_ip_1 = "10.60.2.1"
helper = '''
10.61.5.1:1237 CyberUni 4
10.61.5.1:1236 CyberUni 3
10.61.5.1:1235 CyberUni 1
10.61.5.1:1234 CyberUni 2
10.60.5.1:3003 ClosedSea 1
10.60.5.1:3004 ClosedSea 2
10.62.5.1:5000 Trademark
10.63.5.1:1337 RPN
'''

services = [{"ip": x.split(" ")[0].split(":")[0], "port": int(x.split(" ")[0].split(":")[1]), "name": " ".join(x.split(" ")[1:])} for x in helper.strip().split("\n")]
services += [{"ip": vm_ip_1, "port": -1, "name": "other"}]

```

### File: services\api\data2req.py
```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Flower.
#
# Copyright ©2018 Nicolò Mazzucato
# Copyright ©2018 Antonio Groza
# Copyright ©2018 Brunello Simone
# Copyright ©2018 Alessio Marotta
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# Flower is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Flower is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Flower.  If not, see <https://www.gnu.org/licenses/>.

from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
from jinja2 import Environment, BaseLoader
from io import BytesIO
import json

from database import FlowDetail

DISCARD_COOKIES = ["PHPSESSID", "wordpress_logged_in_", "session"]


HEADER_TEMPLATE = """import json
import os
import sys

import requests

HOST = os.getenv('TARGET_IP')
EXTRA = json.loads(os.getenv('TARGET_EXTRA', '[]'))
{% if use_requests_session %}
s = requests.Session()
{% endif -%}
"""

REQUEST_TEMPLATE = """
{{"s." if use_requests_session}}headers = {{headers}}
{% if data -%}
data = {{data}}
{% endif -%}
{{"res = " if print_info}}{{"s" if use_requests_session else "requests"}}.{{request_method}}(f"http://{HOST}:{{port}}" + {{request_path_repr}}{% if data %}, {{data_param_name}}=data{% endif %}{{ ", headers=headers" if not use_requests_session}})
{% if print_info -%}
print(res.text)
print(res.status_code, res.headers)
{% endif %}
"""


def render(template, **kwargs):
    return Environment(loader=BaseLoader()).from_string(template).render(kwargs)


# class to parse request informations
class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, raw_http_request: bytes):
        self.rfile = BytesIO(raw_http_request)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

        self.headers: dict[str, str]
        try:
            self.headers = dict(self.headers)
        except AttributeError:
            self.headers = {}

        # Data
        try:
            self.body = raw_http_request.split(b"\r\n\r\n", 1)[1].rstrip()
        except IndexError:
            self.body = None

    def send_error(self, code, message=None, explain=None):
        self.error_code = code
        self.error_message = message


def decode_http_request(raw_request: bytes, tokenize):
    request = HTTPRequest(raw_request)
    headers = {}
    blocked_headers = [
        "content-length",
        "accept-encoding",
        "connection",
        "accept",
        "host",
    ]
    content_type = ""
    data = None
    data_param_name = None

    for i in request.headers:
        normalized_header = i.lower()

        if normalized_header == "content-type":
            content_type = request.headers[i]
        if not normalized_header in blocked_headers:
            headers[i] = request.headers[i]

    # if tokenization is enabled and body is not empty, try to decode form body or JSON body
    if tokenize and request.body:
        # try to deserialize form data
        if content_type.startswith("application/x-www-form-urlencoded"):
            data_param_name = "data"
            data = {}
            body_dict = parse_qs(request.body.decode())
            for key, value in body_dict.items():
                if len(value) == 1:
                    data[key] = value[0]
                else:
                    data[key] = value

        # try to deserialize json
        if content_type.startswith("application/json"):
            data_param_name = "json"
            try:
                data = json.loads(request.body)
            except json.decoder.JSONDecodeError:
                pass

        # Forms with files are not yet implemented
        # # try to extract files
        # if content_type.startswith("multipart/form-data"):
        #     data_param_name = "files"
        #     data  = ...

        # Fallback to use raw text if nothing else worked out
        if data is None:
            data_param_name = "data"
            data = request.body

    return request, data, data_param_name, headers


# tokenize used for automatically fill data param of request
def convert_single_http_requests(
    flow: FlowDetail,
    item_index: int,
    tokenize: bool = True,
    use_requests_session: bool = False,
):
    if not flow.items:
        return "No data"

    request, data, data_param_name, headers = decode_http_request(
        flow.items[item_index].data, tokenize
    )
    if not request.path.startswith("/"):
        raise Exception("request path must start with / to be a valid HTTP request")
    request_path_repr = repr(request.path)
    request_method = validate_request_method(request.command)

    return render(
        HEADER_TEMPLATE,
        use_requests_session=use_requests_session,
        port=flow.port_dst,
    ) + render(
        REQUEST_TEMPLATE,
        headers=repr(headers),
        data=data,
        request_method=request_method,
        request_path_repr=request_path_repr,
        data_param_name=data_param_name,
        use_requests_session=use_requests_session,
        port=flow.port_dst,
        print_info=True,
    )


def convert_flow_to_http_requests(
    flow: FlowDetail, tokenize: bool = True, use_requests_session: bool = True
):
    port = flow.port_dst
    script = render(
        HEADER_TEMPLATE,
        use_requests_session=use_requests_session,
        port=port,
    )

    for item in flow.kind_items():
        if item.direction == "c":
            request, data, data_param_name, headers = decode_http_request(
                item.data, tokenize
            )
            request_method = validate_request_method(request.command)
            if not request.path.startswith("/"):
                raise Exception(
                    "request path must start with / to be a valid HTTP request"
                )
            request_path_repr = repr(request.path)

            script += render(
                REQUEST_TEMPLATE,
                headers=repr(headers),
                data=data,
                request_method=request_method,
                request_path_repr=request_path_repr,
                data_param_name=data_param_name,
                use_requests_session=use_requests_session,
                port=port,
                print_info=True,
            )
    return script


def validate_request_method(request_method: str):
    request_method = request_method.lower()
    if request_method not in [
        "delete",
        "get",
        "head",
        "options",
        "patch",
        "post",
        "put",
    ]:
        # Throw Exception for a bad method to prevent command inject via a nasty request method
        raise Exception(f"Invalid request method: {request_method}")
    return request_method

```

### File: services\api\database.py
```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations

import base64
import re
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import Any, Iterator, cast

import dateutil.parser
import psycopg
import psycopg_pool
from psycopg import sql
from psycopg.rows import class_row, dict_row

import configurations
from json_util import JsonFactory


@dataclass(slots=True, kw_only=True)
class FlowQuery:
    regex_insensitive: re.Pattern | None = None
    ip_src: IPv4Network | IPv6Network | None = None
    ip_dst: IPv4Network | IPv6Network | None = None
    port_src: int | None = None
    port_dst: int | None = None
    time_from: datetime | None = None
    time_to: datetime | None = None
    tags_include: list[str] = field(default_factory=list)
    tags_exclude: list[str] = field(default_factory=list)
    tag_intersection_and: bool = False
    limit: int = 1000


@dataclass(slots=True, kw_only=True)
class Flow:
    id: uuid.UUID
    time: datetime
    port_src: int
    port_dst: int
    ip_src: IPv4Address | IPv6Address
    ip_dst: IPv4Address | IPv6Address
    duration: timedelta
    pcap_id: uuid.UUID
    pcap_name: str
    link_parent_id: uuid.UUID
    link_child_id: uuid.UUID
    fingerprints: list[int]
    packets_count: int
    packets_size: int
    flags_in: int
    flags_out: int
    signatures: list[Signature]
    tags: list[str]
    flags: list[str]
    flagids: list[str]
    rank: int = 0


@dataclass(slots=True, kw_only=True)
class Signature:
    id: int
    message: str
    action: str


@dataclass(slots=True, kw_only=True)
class FlowItem(JsonFactory):
    id: uuid.UUID
    flow_id: uuid.UUID
    kind: str
    time: datetime
    direction: str
    data: bytes

    def to_json(self) -> Any:
        result = JsonFactory.to_json(self)
        result["data"] = base64.b64encode(result["data"]).decode("ascii")
        return result


@dataclass(slots=True, kw_only=True)
class FlowDetail(Flow):
    items: list[FlowItem] = field(default_factory=list)

    def kind_items(self, kind: str = "raw") -> list[FlowItem]:
        return [i for i in self.items if i.kind == kind]

    def item_data(self, kind: str = "raw") -> list[bytes]:
        return [i.data for i in self.kind_items(kind)]

    def collect_data(self, kind: str = "raw") -> bytes:
        return b"".join(self.item_data(kind))


@dataclass(slots=True, kw_only=True)
class StatsQuery:
    service: str | None = None
    tick_from: int | None = None
    tick_to: int | None = None


@dataclass(slots=True)
class Stats:
    tick: int
    flow_count: int = 0
    tag_flag_in: int = 0
    tag_flag_out: int = 0
    tag_blocked: int = 0
    tag_suricata: int = 0
    tag_enemy: int = 0
    flag_in: int = 0
    flag_out: int = 0


class Pool(psycopg_pool.ConnectionPool):
    def __init__(self, connection_string: str, *, open: bool = False, **kwargs) -> None:
        super().__init__(
            connection_string,
            open=open,
            connection_class=Connection,
            **kwargs,
        )

    @contextmanager
    def connection(self, timeout: float | None = None) -> Iterator[Connection]:
        with super().connection(timeout) as connection:
            yield cast(Connection, connection)


class Connection(psycopg.Connection):
    def flow_query(self, query: FlowQuery) -> list[Flow]:
        pre_select = sql.SQL(
            "WITH f AS (SELECT *, fid_rank_desc(id) AS rank FROM flow ORDER BY id DESC)"
        )
        conditions = [sql.SQL("true")]
        pre_conditions = [sql.SQL("true")]
        parameters = {}

        if query.ip_src:
            parameters["ip_src"] = query.ip_src
            conditions.append(sql.SQL("f.ip_src <<= %(ip_src)s"))
        if query.ip_dst:
            parameters["ip_dst"] = query.ip_dst
            conditions.append(sql.SQL("f.ip_dst <<= %(ip_dst)s"))

        if query.port_src:
            parameters["port_src"] = query.port_src
            conditions.append(sql.SQL("f.port_src = %(port_src)s"))
        if query.port_dst:
            parameters["port_dst"] = query.port_dst
            conditions.append(sql.SQL("f.port_dst = %(port_dst)s"))

        if query.time_from:
            parameters["time_from"] = query.time_from
            conditions.append(sql.SQL("f.id > fid_pack_low(%(time_from)s)"))
            pre_conditions.append(sql.SQL("flow_id > fid_pack_low(%(time_from)s)"))
        if query.time_to:
            parameters["time_to"] = query.time_to
            conditions.append(sql.SQL("f.id < fid_pack_high(%(time_to)s)"))
            pre_conditions.append(sql.SQL("flow_id < fid_pack_high(%(time_to)s)"))

        if query.tags_include:
            parameters["tags_include"] = query.tags_include
            if query.tag_intersection_and:
                conditions.append(sql.SQL("f.tags ?& %(tags_include)s"))
            else:
                conditions.append(sql.SQL("f.tags ?| %(tags_include)s"))
        if query.tags_exclude:
            parameters["tags_exclude"] = query.tags_exclude
            conditions.append(sql.SQL("NOT f.tags ?| %(tags_exclude)s"))

        if query.regex_insensitive:
            parameters["regex_insensitive"] = query.regex_insensitive.pattern
            text = """
                WITH fi AS (
                    SELECT flow_id, fid_rank_desc(flow_id) AS rank
                    FROM flow_index
                    WHERE text ~* %(regex_insensitive)s
                        AND {pre_conditions}
                    ORDER BY rank
                ), fd AS (
                    SELECT DISTINCT flow_id, rank
                    FROM fi
                ), f AS (
                    SELECT fl.*, fd.rank
                    FROM fd
                    LEFT JOIN flow AS fl
                        ON fl.id = fd.flow_id
                )
            """
            pre_select = sql.SQL(text).format(
                pre_conditions=sql.SQL(" AND ").join(pre_conditions)
            )

        text_query = """
            /*+
                IndexScan(flow_index)
                Set(enable_material false)
            */
            {pre_select}
            SELECT f.*, p.name AS pcap_name
            FROM f
            LEFT JOIN pcap AS p
                ON p.id = f.pcap_id
            WHERE {conditions}
            LIMIT {limit}
        """

        sql_query = sql.SQL(text_query).format(
            conditions=sql.SQL(" AND ").join(conditions),
            pre_select=pre_select,
            limit=query.limit,
        )

        with self.cursor(row_factory=class_row(Flow)) as cursor:
            flows = cursor.execute(sql_query, parameters).fetchall()

        # Filter out non-existing tags
        tags = self.tag_list()
        for flow in flows:
            flow.tags = list(filter(lambda t: t in flow.tags, tags))

        return list(sorted(flows, key=lambda f: f.rank))

    def flow_detail(self, id: uuid.UUID) -> FlowDetail | None:
        sql_query = """
            SELECT f.*, p.name AS pcap_name
            FROM flow AS f
            INNER JOIN pcap AS p
                ON p.id = f.pcap_id
            WHERE f.id = %(id)s
            ORDER BY id DESC
            LIMIT 2000
        """
        with self.cursor(row_factory=class_row(FlowDetail)) as cursor:
            flow = cursor.execute(sql_query, {"id": id}).fetchone()

        if flow is None:
            return None

        flow.items = self.flow_item_query(flow)

        # Filter out non-existing tags and sort the rest
        flow.tags = list(filter(lambda t: t in flow.tags, self.tag_list()))

        return flow

    def flow_item_query(self, flow: Flow) -> list[FlowItem]:
        sql_query = """
            SELECT fi.*
            FROM flow_item AS fi
            WHERE fi.flow_id = %(flow_id)s
                AND fi.id > fid_pack_low(%(time_start)s)
                AND fi.id < fid_pack_high(%(time_end)s)
        """

        parameters = {
            "flow_id": flow.id,
            "time_start": flow.time,
            "time_end": flow.time + flow.duration,
        }

        with self.cursor(row_factory=class_row(FlowItem)) as cursor:
            return cursor.execute(sql_query, parameters).fetchall()

    def flow_tag(self, flow_id: uuid.UUID, tag: str, apply: bool) -> None:
        if apply:
            sql_query = """
                UPDATE flow
                SET tags = jsonb_unique(tags || jsonb_build_array(%(tag)s::text))
                WHERE id = %(flow_id)s
            """
        else:
            sql_query = """
                UPDATE flow
                SET tags = tags - %(tag)s::text
                WHERE id = %(flow_id)s
            """

        self.execute(sql_query, {"flow_id": flow_id, "tag": tag})

    def stats_query(self, query: StatsQuery) -> dict[int, Stats]:
        now = datetime.now(tz=timezone.utc)
        tick_first = dateutil.parser.parse(configurations.start_date)
        tick_length = timedelta(milliseconds=int(configurations.tick_length))
        tick_current = ((now - tick_first) // tick_length) + 1
        tick_start = query.tick_from if query.tick_from else 0
        tick_end = query.tick_to if query.tick_to else tick_current
        time_start = tick_first + (tick_start * tick_length)
        time_end = tick_first + (tick_end * tick_length)

        stats: dict[int, Stats] = {i: Stats(i) for i in range(tick_start, tick_end)}

        parameters = {
            "tick_length": tick_length,
            "tick_first": tick_first,
            "time_start": time_start,
            "time_end": time_end,
        }

        sql_query = """
            SELECT tick_number_bucket(%(tick_first)s, %(tick_length)s, time) AS tick,
                count(id) AS count, sum(flags_in) AS flags_in, sum(flags_out) AS flags_out
            FROM flow AS f
            WHERE f.id > fid_pack_low(%(time_start)s)
                AND f.id < fid_pack_high(%(time_end)s)
            GROUP BY tick
        """
        with self.cursor(row_factory=dict_row) as cursor:
            for row in cursor.execute(sql_query, parameters):
                stats[row["tick"]].flow_count = row["count"]
                stats[row["tick"]].flag_in = row["flags_in"]
                stats[row["tick"]].flag_out = row["flags_out"]

        # TODO: Maybe count all tags? The query already selects the numbers
        sql_query = """
            SELECT tick_time_bucket(%(tick_first)s, %(tick_length)s, time) AS tick_start,
                tick_number_bucket(%(tick_first)s, %(tick_length)s, time) AS tick,
                t.name AS tag, count(f.id) AS count
            FROM flow AS f
            JOIN tag AS t
                ON f.tags ? t.name
            WHERE f.id > fid_pack_low(%(time_start)s)
                AND f.id < fid_pack_high(%(time_end)s)
            GROUP BY tick_start, tick, t.name
            ORDER BY tick ASC
        """
        with self.cursor(row_factory=dict_row) as cursor:
            for row in cursor.execute(sql_query, parameters):
                if row["tag"] == "flag-in":
                    stats[row["tick"]].tag_flag_in += row["count"]
                elif row["tag"] == "flag-out":
                    stats[row["tick"]].tag_flag_out += row["count"]
                elif row["tag"] == "blocked":
                    stats[row["tick"]].tag_blocked += row["count"]
                elif row["tag"] == "suricata":
                    stats[row["tick"]].tag_suricata += row["count"]
                elif row["tag"] == "enemy":
                    stats[row["tick"]].tag_enemy += row["count"]

        return stats

    def tag_list(self) -> list[str]:
        with self.cursor(row_factory=dict_row) as cursor:
            tags = cursor.execute("SELECT name FROM tag ORDER BY sort ASC").fetchall()
            return [t["name"] for t in tags]

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
