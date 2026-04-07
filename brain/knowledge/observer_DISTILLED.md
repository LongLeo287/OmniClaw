---
id: observer
type: knowledge
owner: OA_Triage
---
# observer
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

# 👁️ Observer AI

[![Observer App Online](https://img.shields.io/badge/🌐_Try_Out-Online-blue?style=for-the-badge&color=4CAF50)](https://app.observer-ai.com/)
[![Download App](https://img.shields.io/badge/⬇️_Download-Latest_Release-blue?style=for-the-badge&color=2196F3)](https://github.com/Roy3838/Observer/releases/latest/)

 [Website](https://observer-ai.com) | [WebApp](https://app.observer-ai.com) | [YouTube](https://www.youtube.com/@Observer-AI) | [Tiktok](https://www.tiktok.com/@observerai) | [Twitter](https://x.com/AppObserverAI) | [Discord](https://discord.com/invite/wnBb7ZQDUC)

### *Local Micro-Agents That Observe, Log and React*

Build powerful micro-agents that observe your digital world, remember what matters, and react intelligently—all while keeping your data **100% private and secure**.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-success)](https://roy3838.github.io/observer-ai)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)




---

## 👁️ How Observer Agents Work

<div align="center">

<table>
<tr>
<td align="center" valign="top" width="33%">

### Sensors →

</td>
<td align="center" valign="top" width="33%">

### Models →

</td>
<td align="center" valign="top" width="33%">

### Tools

</td>
</tr>
<tr>
<td align="center" valign="middle" width="33%">

<img src="https://img.icons8.com/fluency/96/monitor.png" width="48" height="48" alt="Screen"/>
<img src="https://img.icons8.com/fluency/96/camera.png" width="48" height="48" alt="Camera"/>
<img src="https://img.icons8.com/fluency/96/microphone.png" width="48" height="48" alt="Mic"/>
<img src="https://img.icons8.com/fluency/96/speaker.png" width="48" height="48" alt="Audio"/>

<br><sub>Screen • Camera • Mic • Audio</sub>

</td>
<td align="center" valign="middle" width="33%">

<img src="https://img.icons8.com/fluency/96/brain.png" width="64" height="64" alt="AI Brain"/>

<br><sub>Local LLMs</sub>

</td>
<td align="center" valign="middle" width="33%">

<img src="https://cdn.simpleicons.org/whatsapp/25D366" width="40" height="40" alt="WhatsApp"/>
<img src="https://cdn.simpleicons.org/discord/5865F2" width="40" height="40" alt="Discord"/>
<img src="https://cdn.simpleicons.org/telegram/26A5E4" width="40" height="40" alt="Telegram"/>
<img src="https://cdn.simpleicons.org/iMessage/0084FF" width="40" height="40" alt="SMS"/>
<img src="https://img.icons8.com/fluency/96/note.png" width="40" height="40" alt="Memory"/>
<img src="https://img.icons8.com/fluency/96/code.png" width="40" height="40" alt="Code"/>

<br><sub>Messaging • Notifications • Recording • Memory • Code</sub>

</td>
</tr>
</table>

<br>

</div>

</div>

---

## 🤖 Base Agent Example 
Sends an email when the Observer logo is on screen

System Prompt (uses $SCREEN_64 for screen input)
```
You are an Observer agent, watch the screen and if you see the Observer logo say OBSERVER, if you don't, say CONTINUE. 
$SCREEN_64
```

Code using Email Tool if model identified an Observer logo
```javascript
if(response.includes("OBSERVER")){
  sendEmail("your@email.com", response, screen); //sends the screen as an attached image
}
```

---

## 🎯 What Observer AI Does Best

<table>
<tr>
<td width="50%" valign="top">

### 📊 **Intelligent Logging**

🧠 **Text & Visual Memory**

🎥 **Smart Screen Recording**

</td>
<td width="50%" valign="top">

### 🚨 **Powerful Notifications**

📧 **Email** • 💬 **Discord** • 📱 **Telegram**
📞 **SMS** • 💚 **WhatsApp** • **Pushover**  

</td>
</tr>
</table>


---

# 🏗️ Building Your Own Agent

Creating your own Observer AI consist of three things:

* SENSORS - input that your model will have
* MODELS - Small LLMs
* TOOLS - functions for your model to use

## Quick Start

1. Navigate to the Agent Dashboard and click "Create New Agent"
2. Fill in the "Configuration" tab with basic details (name, description, model, loop interval)
3. Give your model a system prompt and Sensors! The current Sensors that exist are:
   * **Screen OCR** ($SCREEN_OCR) Captures screen content as text via OCR
   * **Screenshot** ($SCREEN_64) Captures screen as an image for multimodal models
   * **Agent Memory** ($MEMORY or $MEMORY@agent_id) Accesses agents' stored information (defaults to current agent)
   * **Agent Image Memory** ($IMEMORY or $IMEMORY@agent_id) Accesses agents' stored images (defaults to current agent)
   * **Clipboard** ($CLIPBOARD) It pastes the clipboard contents 
   * **Microphone**\* ($MICROPHONE) Captures the microphone and adds a transcription
   * **Screen Audio**\* ($SCREEN_AUDIO) Captures the audio transcription of screen sharing a tab.
   * **All audio**\* ($ALL_AUDIO) Mixes the microphone and screen audio and provides a complete transcription of both (used for meetings).

\* Uses a whisper model with transformers.js

Agent Tools:
  * `getMemory(agentId?)*` – Retrieve stored memory 
  * `setMemory(agentId?, content)*` – Replace stored memory  
  * `appendMemory(agentId?, content)*` – Add to existing memory  
  * `getImageMemory(agentId?)*` - Retrieve images stored in memory 
  * `setImageMemory(agentId?, images)*` - Set images to memory
  * `appendImageMemory(agentId?, images)*` - Add images to memory
  * `startAgent(agentId?)*` – Starts an agent  
  * `stopAgent(agentId?)*` – Stops an agent
  * `time()` - Gets current time
  * `sleep(ms)` - Waits that ammount of miliseconds

`*` `agentId` is optional, deaults to agent running code

Notification Tools:
  * `sendDiscord(discord_webhook, message, images?, videos?)` - Directly sends a discord message to a server. 
  * `sendTelegram(chat_id, message, images?, videos?)` Sends a telegram message with the Observer bot. Get the chat_id messaging the bot @observer_notification_bot.
  * `sendEmail(email, message, images?, videos?)` - Sends an email
  * `sendPushover(user_token, message, images?, title?)` - Sends a pushover notification.
  * `call(phone_number, message)*` - Makes an automated phone call with text-to-speech message.
  * `sendWhatsapp(phone_number, message, videos?)*` - Sends a whatsapp message with the Observer bot.  
  * `sendSms(phone_number, message, images?, videos?)*` - Sends an SMS to a phone number. Due to A2P policy, blocked for US/Canada.
  * `notify(title, options)` – Send browser notification ⚠️IMPORTANT: Some browsers block notifications

`*` To activate, SMS or call +1 (863)208-5341 or whatsapp +1 (555)783-4727

Video Recording Tools: 
  * `startClip()` - Starts a recording of any video media and saves it to the recording Tab.
  * `stopClip()` - Stops an active recording
  * `markClip(label)` - Adds a label to any active recording that will be displayed in the recording Tab.
  * `getVideo()` - Returns array of videos on buffer.

App Tools:
  * `ask(question, title="Confirmation")` - Pops up a system confirmation dialog
  * `message(message, title="Agent Message")` - Pops up a system message
  * `system_notify(body, title="Observer AI")` - Sends a system notification
  * `overlay(body)` - Pushes a message to the overlay
  * `click('left'|'right')` - Triggers a mouse click at the current cursor position accepts either 'left' or 'right', defaults to left.
## Code Tab

The "Code" tab receives the following variables as context before running: 
* `response` - The model's response
* `agentId` - The id of the agent running the code
* `screen` - The screen if captured 
* `camera` - The camera if captured 
* `imemory` - The agent's current image in memory
* `images` - All images sent to the model 
* `prompt` - The model's prompt
* `microphone` - Trascription from the microphone in this loop
* `screenAudio` - Transcription from screen audio in this loop
* `allAudio` - Transcription from microphone and screen audio mixed in this loop

JavaScript agents run in the browser sandbox, making them ideal for passive monitoring and notifications:

```javascript
// Remove Think tags for deepseek model
const cleanedResponse = response.replace(/<think>[\s\S]*?<\/think>/g, '').trim();

// Get time
const time = time();

// Update memory with timestamp
appendMemory(`[${time}] ${cleanedResponse}`);

// Send to Telegram if the model mentions a word
if(response.includes("word")){
  sendTelegram(cleanedResponse, "12345678") // Example chat_id
}
```


# 🚀 Getting Started with Local Inference


There are a few ways to get Observer up and running with local inference. I recommend the Observer App. 

## Option 1: Just Install the Desktop App with any OpenAI compatible endpoint (Ollama, llama.cpp, vLLM)

Download the Official App:

[![Download App](https://img.shields.io/badge/⬇️_Download-Latest_Release-blue?style=for-the-badge&color=2196F3)](https://github.com/Roy3838/Observer/releases/latest/)

Download Ollama for the best compatibility. Observer can connect directly to any server that provides a `v1/chat/completions` endpoint.

### vLLM, llama.cpp, LMStudio etc: 
Set the `Custom Model Server URL` on the App to any OpenAI compatible endpoint if not using Ollama.

NOTE: Your browser app sends the request to `localhost:3838` which the ObserverApp proxies to your `Custom Model Server URL`, this is because of CORS. 


## Option 2: Full Docker Setup (Deprecated)

For Docker setup instructions, see [docker/DOCKER.md](docker/DOCKER.md).


### Setting Up Python (Jupyter Server) 

For Jupyter server setup instructions, see [app/JUPYTER.md](app/JUPYTER.md).


## Deploy & Share

Save your agent, test it from the dashboard, and upload to community to share with others!

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

Built with ❤️  by Roy Medina for the Observer AI Community
Special thanks to the Ollama team for being an awesome backbone to this project!

```

### File: api\requirements.txt
```txt
fastapi==0.103.1
uvicorn==0.23.2
httpx==0.24.1
pydantic==2.3.0

```

### File: app\package.json
```json
{
  "name": "@observer/webapp",
  "private": true,
  "version": "2.1.3",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview --port 8080 --host",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "format": "prettier --write .",
    "stage-cli": "cargo build --manifest-path ../cli/Cargo.toml --release && mkdir -p desktop/binaries && cp ../cli/target/release/observe desktop/binaries/observe-$(rustc -vV | sed -n 's/host: //p')",
    "desktop:dev": "pnpm stage-cli && cd desktop && cargo tauri dev",
    "desktop:build": "pnpm build && cd desktop && cargo tauri build",
    "ios:dev": "cd mobile && cargo tauri ios dev",
    "ios:build": "pnpm build && cd mobile && cargo tauri ios build",
    "android:dev": "cd mobile && cargo tauri android dev",
    "android:build": "pnpm build && cd mobile && cargo tauri android build"
  },
  "dependencies": {
    "@auth0/auth0-react": "^2.3.0",
    "@choochmeque/tauri-plugin-iap-api": "^0.7.0",
    "@codemirror/lang-javascript": "^6.2.3",
    "@codemirror/lang-python": "^6.1.7",
    "@codemirror/view": "^6.38.1",
    "@huggingface/transformers": "^3.5.2",
    "@jupyterlab/services": "^7.3.6",
    "@lexical/history": "^0.25.0",
    "@lexical/list": "^0.25.0",
    "@lexical/react": "^0.25.0",
    "@lexical/rich-text": "^0.25.0",
    "@lexical/selection": "^0.25.0",
    "@tauri-apps/api": "^2.6.0",
    "@tauri-apps/plugin-deep-link": "^2.4.6",
    "@tauri-apps/plugin-dialog": "^2.3.1",
    "@tauri-apps/plugin-http": "^2.5.7",
    "@tauri-apps/plugin-log": "^2",
    "@tauri-apps/plugin-notification": "^2.3.0",
    "@tauri-apps/plugin-opener": "^2.5.3",
    "@tauri-apps/plugin-os": "^2.3.2",
    "@tauri-apps/plugin-shell": "^2.3.0",
    "@tauri-apps/plugin-updater": "^2.9.0",
    "@tinymce/tinymce-react": "^6.0.0",
    "@types/react-syntax-highlighter": "^15.5.13",
    "@uiw/codemirror-theme-vscode": "^4.24.0",
    "@uiw/react-codemirror": "^4.23.8",
    "@xenova/transformers": "^2.17.2",
    "date-fns": "^4.1.0",
    "framer-motion": "^12.23.6",
    "fs": "^0.0.1-security",
    "idb": "^8.0.3",
    "js-yaml": "^4.1.0",
    "katex": "^0.16.19",
    "lexical": "^0.25.0",
    "lucide-react": "^0.476.0",
    "onnxruntime-web": "^1.22.0",
    "path": "^0.12.7",
    "qrcode.react": "^4.2.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-markdown": "^10.1.0",
    "react-player": "^2.16.0",
    "react-router-dom": "^6.30.1",
    "react-syntax-highlighter": "^15.6.1",
    "rehype-katex": "^7.0.1",
    "rehype-raw": "^7.0.0",
    "remark-gfm": "^4.0.1",
    "remark-math": "^6.0.0",
    "slate": "^0.123.0",
    "slate-history": "^0.113.1",
    "slate-react": "^0.123.0",
    "tauri-plugin-web-auth-api": "^1.0.0",
    "tesseract.js": "^6.0.0",
    "ts-node": "^10.9.2",
    "yaml": "^2.7.0"
  },
  "devDependencies": {
    "@tauri-apps/cli": "^2.6.2",
    "@types/dom-speech-recognition": "^0.0.6",
    "@types/js-yaml": "^4.0.9",
    "@types/node": "^20.17.10",
    "@types/react": "^18.2.55",
    "@types/react-dom": "^18.2.19",
    "@typescript-eslint/eslint-plugin": "^6.21.0",
    "@typescript-eslint/parser": "^6.21.0",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.17",
    "esbuild": "0.21.5",
    "eslint": "^8.56.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "postcss": "^8.4.35",
    "prettier": "^3.2.5",
    "rollup-plugin-visualizer": "^5.14.0",
    "tailwindcss": "^3.4.1",
    "typescript": "~5.3.3",
    "vite": "^5.1.0"
  }
}

```

### File: website\package.json
```json
{
  "name": "@observer/website",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "clsx": "^2.1.1",
    "lucide-react": "^0.525.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^7.13.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32",
    "tailwindcss": "^3.3.6",
    "typescript": "^5.2.2",
    "vite": "^5.0.8"
  }
}

```

### File: website\README.md
```md
# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default tseslint.config({
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```

- Replace `tseslint.configs.recommended` to `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked`
- Optionally add `...tseslint.configs.stylisticTypeChecked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and update the config:

```js
// eslint.config.js
import react from 'eslint-plugin-react'

export default tseslint.config({
  // Set the react version
  settings: { react: { version: '18.3' } },
  plugins: {
    // Add the react plugin
    react,
  },
  rules: {
    // other rules...
    // Enable its recommended rules
    ...react.configs.recommended.rules,
    ...react.configs['jsx-runtime'].rules,
  },
})
```

```

### File: build.sh
```sh
#!/bin/bash

echo "Building Observer..."
cd app

# Disable signing for local builds
unset TAURI_SIGNING_PRIVATE_KEY
unset TAURI_SIGNING_PRIVATE_KEY_PASSWORD

npm run tauri build -- --bundles deb

# Always try to run the binary if it exists
if [ -f "./src-tauri/target/release/app" ]; then
    echo "Running Observer..."
    ./src-tauri/target/release/app
else
    echo "Binary not found! Build may have failed completely."
    exit 1
fi
```

### File: get_download.sh
```sh
curl -s https://api.github.com/repos/Roy3838/Observer/releases | egrep 'download_count'  | cut '-d:' -f 2 | sed 's/,/+/' | xargs echo | xargs -I N echo N 0  | bc

```

### File: versionstrings.txt
```txt
# Version strings that need to be updated for releases

# Desktop app
app/desktop/tauri.conf.json                                    # "version": "X.X.X"

# Mobile app
app/mobile/tauri.conf.json                                     # "version": "X.X.X"

# iOS main app Info.plist
app/mobile/gen/apple/observer-mobile_iOS/Info.plist            # CFBundleShortVersionString, CFBundleVersion

# iOS extensions (must match parent app version)
app/mobile/extensions/ObserverBroadcast/Info.plist             # CFBundleShortVersionString, CFBundleVersion
app/mobile/gen/apple/broadcast/Info.plist                      # CFBundleShortVersionString, CFBundleVersion
app/mobile/gen/apple/broadcastSetupUI/Info.plist               # CFBundleShortVersionString

# Xcode project (MARKETING_VERSION for extensions)
app/mobile/gen/apple/observer-mobile.xcodeproj/project.pbxproj # MARKETING_VERSION (4 occurrences)

# Package.json
app/package.json                                               # "version": "X.X.X"

```

### File: api\api.py
```py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import argparse
import logging
import os
import socket
import subprocess
from pathlib import Path

# Import routers from our modules
from marketplace import marketplace_router
from compute import compute_router
from tools_router import tools_router
from payments import payments_router

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('api-server')

# modelo = randomforest()

# @app.post("/resultados")
# def enviar_resultados(datos):
#     resultados = modelo(datos)
#     return resultados

# Setup FastAPI app
app = FastAPI()

# Create temp images directory
TEMP_IMAGES_DIR = Path("temp_images")
TEMP_IMAGES_DIR.mkdir(exist_ok=True)

# Mount static files for serving images
app.mount("/temp-images", StaticFiles(directory="temp_images"), name="temp-images")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers - without prefixes to maintain original URL structure
app.include_router(marketplace_router)
# Mount compute router last since it has a catch-all route
app.include_router(compute_router)
# Mount twilio router
app.include_router(tools_router)
# Payments router
app.include_router(
    payments_router,
    prefix="/payments",
    tags=["Payments"]
)

# Root path to check if service is running
@app.get("/")
async def root():
    return {"status": "API server is running"}

# Generate SSL certificates
def prepare_certificates(cert_dir):
    """Prepare SSL certificates"""
    cert_path = Path(cert_dir) / "cert.pem"
    key_path = Path(cert_dir) / "key.pem"
    
    # Create certificate directory if it doesn't exist
    os.makedirs(cert_dir, exist_ok=True)
    
    # Check if we need to generate certificates
    if not cert_path.exists() or not key_path.exists():
        logger.info("Generating SSL certificates...")
        cmd = [
            "openssl", "req", "-x509", 
            "-newkey", "rsa:4096", 
            "-sha256", 
            "-days", "365", 
            "-nodes", 
            "-keyout", str(key_path), 
            "-out", str(cert_path),
            "-subj", "/CN=localhost"
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            logger.info(f"Certificates generated at {cert_dir}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to generate certificates: {e.stderr.decode() if hasattr(e, 'stderr') else str(e)}")
            raise RuntimeError("Failed to generate SSL certificates")
    else:
        logger.info(f"Using existing certificates from {cert_dir}")
        
    return cert_path, key_path

def get_local_ip():
    """Get the local IP address for network access"""
    try:
        # Create a socket that connects to an external server to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # We don't actually need to send data
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        logger.warning(f"Could not determine local IP: {e}")
        return "0.0.0.0"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Observer AI API Server")
    parser.add_argument("--port", type=int, default=8000, help="Port to run on")
    parser.add_argument("--cert-dir", default="./certs", help="Certificate directory")
    parser.add_argument("--cert-file", help="Path to certificate file (if not provided, self-signed will be used)")
    parser.add_argument("--key-file", help="Path to key file (if not provided, self-signed will be used)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--proxy-target", default="https://compute.observer-ai.com", help="Target service URL for proxy")
    
    args = parser.parse_args()
    
    if args.debug:
        logger.setLevel(logging.DEBUG)
        
    # Set target URL for compute proxy
    os.environ["AI_SERVICE_URL"] = args.proxy_target
    
    # Set up SSL
    if args.cert_file and args.key_file:
        # Use provided certificates
        cert_path = args.cert_file
        key_path = args.key_file
        logger.info(f"Using provided certificates: {cert_path}, {key_path}")
    else:
        # Self-sign certificates
        cert_path, key_path = prepare_certificates(args.cert_dir)
    
    # Get local IP for network access
    local_ip = get_local_ip()
    
    # Print server info
    print("\n\033[1m OBSERVER AI API SERVER \033[0m ready")
    print(f"  ➜  \033[36mLocal:   \033[0mhttps://localhost:{args.port}/")
    print(f"  ➜  \033[36mNetwork: \033[0mhttps://{local_ip}:{args.port}/")
    print(f"\n  Marketplace routes: https://localhost:{args.port}/agents")
    print(f"  Compute quota: https://localhost:{args.port}/quota")
    print(f"  Proxy forwarding to: {args.proxy_target}")
    
    # Run with SSL context
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=args.port,
        ssl_certfile=str(cert_path),
        ssl_keyfile=str(key_path)
    )

```

### File: api\api_handlers.py
```py
#!/usr/bin/env python3
import os
import json
from datetime import datetime
from pathlib import Path
import logging
import httpx # Import httpx here if base class needs it, or just in subclasses

logger = logging.getLogger("api_handlers")
# Basic logging setup if not configured elsewhere
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s')

# Global registry for API handlers
API_HANDLERS = {}

class HandlerError(Exception):
    """Custom exception for handler-specific errors."""
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.status_code = status_code

class ConfigError(HandlerError):
    """Error for configuration issues like missing API keys."""
    def __init__(self, message):
        super().__init__(message, status_code=500) # Internal server error as config is wrong

class BackendAPIError(HandlerError):
    """Error originating from the downstream AI API."""
    def __init__(self, message, status_code=502): # Bad Gateway by default
        super().__init__(message, status_code)


class BaseAPIHandler:
    """Base class for asynchronous API handlers."""
    def __init__(self, name):
        self.name = name
        self.models = []  # List of supported models { "name": "model-id", "parameters": "optional", ... }
        API_HANDLERS[name] = self
        logger.info("Registered API handler: '%s'", name)
        # Optional: Create a shared httpx client if needed across handlers (managing lifecycle is key)
        # self.http_client = httpx.AsyncClient(timeout=90.0) # Example

    def get_models(self):
        """Return the list of models supported by this handler."""
        return self.models

    async def handle_request(self, request_data: dict) -> dict:
        """
        Process the request asynchronously.
        Subclasses MUST override this method.

        Args:
            request_data: The parsed JSON request data (dictionary).

        Returns:
            A dictionary representing the successful JSON response payload.

        Raises:
            ConfigError: If configuration (like API key) is missing.
            BackendAPIError: If the downstream API call fails.
            ValueError: If the request_data is invalid.
            NotImplementedError: If the subclass doesn't implement this.
            Exception: For other unexpected errors.
        """
        raise NotImplementedError(f"Handler '{self.name}' must implement handle_request")

    # NOTE: log_conversation() method removed - now handled centrally in compute.py
    # This eliminates disk I/O during requests and ensures consistent logging across all handlers


# --- Import and Instantiate REWRITTEN Handlers ---
# Ensure these files contain the rewritten async versions below
from gemini_handler import GeminiAPIHandler
from gemini_pro_handler import GeminiProAPIHandler
from openrouter_handler import OpenRouterAPIHandler
from fireworks_handler import FireworksAPIHandler

# Instantiate and register the handlers.
# The __init__ method in BaseAPIHandler adds them to API_HANDLERS
gemini_handler = GeminiAPIHandler()
gemini_pro_handler = GeminiProAPIHandler()
fireworks_handler = FireworksAPIHandler()
openrouter_handler = OpenRouterAPIHandler()

logger.info("Initialized API Handlers. Available: %s", list(API_HANDLERS.keys()))
# --- End Handler Instantiation ---

```

### File: api\compute.py
```py
# compute.py

from fastapi import APIRouter, Request, HTTPException, status, Depends
from fastapi.responses import JSONResponse, StreamingResponse
import logging
import json
from collections import defaultdict
from datetime import datetime
from threading import Lock

# --- Local Imports ---
from auth import AuthUser
from admin_auth import get_admin_access
# Import the new, specific functions and the QUOTA_LIMITS dictionary
from quota_manager import increment_usage, get_usage_for_service, check_usage, QUOTA_LIMITS

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('compute_router')

# --- Observer AI Handler Integration ---
try:
    import api_handlers
    from api_handlers import HandlerError, ConfigError, BackendAPIError
    logger.info("Successfully imported api_handlers. Available handlers: %s", list(api_handlers.API_HANDLERS.keys()))
    HANDLERS_AVAILABLE = True
except ImportError as e:
    logger.error(f"Could not import api_handlers: {e}. Backend routing will not work.", exc_info=True)
    api_handlers, HandlerError, ConfigError, BackendAPIError, HANDLERS_AVAILABLE = (None, Exception, Exception, Exception, False)
# --- End Integration ---

compute_router = APIRouter()

# --- Metrics Logging System (Memory-Only) ---
# Similar to quota_manager.py pattern - all in memory
_conversation_metrics = []
_metrics_lock = Lock()

def log_conversation_metrics(user_id: str, prompt_text: str, response_text: str,
                           handler: str, model: str, status_code: int, image_count: int = 0,
                           time_to_first_token: float = None, chunks_per_second: float = None):
    """Log conversation metrics to memory (no disk I/O)."""
    with _metrics_lock:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "prompt": prompt_text[-500:] if prompt_text else "",  # See last 500 chars to look at requests for generated agents
            "response": response_text[:500] if response_text else "",
            "handler": handler,
            "model": model,
            "status_code": status_code,
            "image_count": image_count,
            "time_to_first_token": time_to_first_token,
            "chunks_per_second": chunks_per_second
        }
        _conversation_metrics.append(entry)
        
        # Keep only last 1000 entries to prevent memory bloat
        if len(_conversation_metrics) > 1000:
            _conversation_metrics.pop(0)

def get_all_conversation_metrics() -> list:
    """Get all conversation metrics (for admin endpoint)."""
    with _metrics_lock:
        return list(_conversation_metrics)  # Return copy

async def _log_streaming_response(stream_iterator, user_id: str, prompt_text: str,
                                 handler: str, model: str, image_count: int = 0):
    """
    Wrapper that logs complete streaming response with timing metrics.
    Accumulates content from OpenAI SSE chunks and logs when stream completes.
    """
    import time

    response_parts = []
    start_time = time.time()
    first_token_time = None
    total_chunks = 0

    try:
        async for chunk in stream_iterator:
            # Yield chunk immediately for streaming
            yield chunk

            # Parse chunk to extract content for logging
            if isinstance(chunk, (str, bytes)):
                chunk_str = chunk.decode() if isinstance(chunk, bytes) else chunk
                if chunk_str.startswith("data: ") and not chunk_str.startswith("data: [DONE]"):
                    try:
                        json_data = chunk_str[6:].strip()  # Remove "data: " prefix
                        if json_data:
                            chunk_json = json.loads(json_data)
                            choices = chunk_json.get("choices", [])
                            if choices and "delta" in choices[0]:
                                content = choices[0]["delta"].get("content")
                                if content:
                                    # Mark time to first token
                                    if first_token_time is None:
                                        first_token_time = time.time()
                                    response_parts.append(content)
                                    total_chunks += 1
                    except (json.JSONDecodeError, KeyError, IndexError):
                        # Skip malformed chunks
                        continue

        # Calculate timing metrics
        end_time = time.time()
        total_duration = end_time - start_time

        time_to_first_token_ms = None
        if first_token_time is not None:
            time_to_first_token_ms = round((first_token_time - start_time) * 1000, 2)

        chunks_per_second = None
        if total_chunks > 0 and total_duration > 0:
            chunks_per_second = round(total_chunks / total_duration, 2)

        # Log complete response when stream finishes
        complete_response = ''.join(response_parts)
        log_conversation_metrics(
            user_id=user_id,
            prompt_text=prompt_text,
            response_text=complete_response,
            handler=handler,
            model=model,
            status_code=200,
            image_count=image_count,
            time_to_first_token=time_to_first_token_ms,
            chunks_per_second=chunks_per_second
        )

    except Exception as e:
        # Log error if stream fails
        log_conversation_metrics(
            user_id=user_id,
            prompt_text=prompt_text,
            response_text=f"STREAM_ERROR: {str(e)}",
            handler=handler,
            model=model,
            status_code=500,
            image_count=image_count
        )

# --- API Routes ---

@compute_router.get("/admin/metrics", tags=["Admin"], summary="Get all conversation metrics")
async def get_all_metrics(is_admin: bool = Depends(get_admin_access)):
    """
    (Admin) Returns all conversation metrics including response times, models used, and error rates.
    Requires a valid X-Admin-Key header.
    """
    return get_all_conversation_metrics()

@compute_router.get("/quota", summary="Check remaining API credits for the authenticated user")
async def check_quota_endpoint(current_user: AuthUser): 
    """
    Returns the daily CHAT credit usage for the authenticated user.
    Requires a valid JWT. Pro users will show unlimited credits.
    """
    # Check if the user is a pro member
    if current_user.is_pro:
        return JSONResponse(content={"used": 0, "remaining": "unlimited", "limit": "unlimited", "pro_status": True})

    # Use the new specific function for the 'chat' service
    used = get_usage_for_service(current_user.id, "chat") # <-- Use current_user.id
    limit = QUOTA_LIMITS["chat"]
    remaining = max(0, limit - used)
    
    return JSONResponse(content={"used": used, "remaining": remaining, "limit": limit, "pro_status": False})


@compute_router.post("/v1/chat/completions", summary="Process chat completion requests")
async def handle_chat_completions_endpoint(request: Request, current_user: AuthUser):
    """
    Processes a chat completion request. Requires a valid JWT.
    Each call will consume one daily CHAT credit.
    """
    if not HANDLERS_AVAILABLE:
        raise HTTPException(status_code=503, detail="Backend LLM handlers are not available.")

    # --- NEW: Quota Check Logic ---
    # Check quota for both pro and free users (pro has higher limit as anti-abuse)
    if check_usage(current_user.id, "chat", current_user.is_pro):
        limit_type = "pro" if current_user.is_pro else "free"
        limit_value = 1000 if current_user.is_pro else QUOTA_LIMITS["chat"]
        logger.warning(f"Chat credit limit exceeded for {limit_type} user: {current_user.id} (Limit: {limit_value})")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"You have exceeded your daily chat quota. Please try again tomorrow."
        )
    
    # If within limit, increment the 'chat' usage.
    usage_count = increment_usage(current_user.id, "chat")
    user_type = "PRO" if current_user.is_pro else "free"
    logger.info(f"Processing chat request for {user_type} user: {current_user.id} (Daily chat request #{usage_count})")
    # --- END of Quota Logic ---

    # 4. Parse Request Data
    try:
        request_data = await request.json()
        model_name = request_data.get("model")
        if not model_name:
            raise HTTPException(status_code=400, detail="Request body must include a 'model' field.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON request body.")

    # 5. Find the appropriate handler
    selected_handler = next((h for h in api_handlers.API_HANDLERS.values() if model_name in [m["name"] for m in h.get_models()]), None)

    if not selected_handler:
        logger.warning(f"Request for unsupported model: {model_name}")
        raise HTTPException(status_code=404, detail=f"Model '{model_name}' is not found or supported.")

    # 6. Check pro access control
    model_info = next((m for m in selected_handler.get_models() if m["name"] == model_name), None)
    if model_info and model_info.get("pro", False) and not current_user.is_pro:
        logger.warning(f"Non-pro user {current_user.id} attempted to access pro model: {model_name}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Model '{model_name}' requires a pro subscription. Please upgrade to access premium models."
        )

    # 7. Execute handler logic with centralized metrics logging
    
    # Extract prompt info for logging
    messages = request_data.get("messages", [])
    prompt_text = ""
    image_count = 0
    
    if messages:
        last_message = messages[-1]
        content = last_message.get("content")
        if isinstance(content, str):
            prompt_text = content
        elif isinstance(content, list):
            # Handle multimodal content (text + images)
            text_parts = []
            for item in content:
                if isinstance(item, dict):
                    if item.get("type") == "text":
                        text_parts.append(item.get("text", ""))
                    elif item.get("type") == "image_url":
                        image_count += 1
            prompt_text = " ".join(text_parts)
            if image_count > 0:
                prompt_text += f" ({image_count} images)"
    
    try:
        response_payload = await selected_handler.handle_request(request_data)

        # Wrap StreamingResponse with logging (all requests are streaming)
        if hasattr(response_payload, '__class__') and response_payload.__class__.__name__ == 'StreamingResponse':
            return StreamingResponse(
                _log_streaming_response(
                    response_payload.body_iterator,
                    current_user.id,
                    prompt_text,
                    selected_handler.name,
                    model_name,
                    image_count
                ),
                media_type=response_payload.media_type,
                headers=response_payload.headers
            )

        # Fallback for non-streaming responses (shouldn't happen but defensive)
        return JSONResponse(content=response_payload)
        
    except (HandlerError, ConfigError, BackendAPIError) as e:
        status_code = getattr(e, 'status_code', 500)
        
        # Log error request metrics
        log_conversation_metrics(
            user_id=current_user.id,
            prompt_text=prompt_text,
            response_text=f"ERROR: {str(e)}",
            handler=selected_handler.name,
            model=model_name,
            status_code=status_code,
            image_count=image_count
        )
        
        logger.error(f"Handler error for model '{model_name}': {e}", exc_info=True)
        raise HTTPException(status_code=status_code, detail=str(e))
        
    except Exception as e:
        # Log unexpected error metrics
        log_conversation_metrics(
            user_id=current_user.id,
            prompt_text=prompt_text,
            response_text=f"INTERNAL_ERROR: {str(e)}",
            handler=selected_handler.name,
            model=model_name,
            status_code=500,
            image_count=image_count
        )
        
        logger.exception(f"Unexpected error processing request with handler {selected_handler.name}")
        raise HTTPException(status_code=500, detail="An internal server error occurred.")


@compute_router.get("/api/tags", summary="List available models (Ollama compatible format)")
async def list_tags_endpoint():
    if not HANDLERS_AVAILABLE:
         raise HTTPException(status_code=503, detail="Backend handlers are not available.")
    EXCLUDED = {"gemini-2.0-flash-lite"}

    ollama_models = []
    if api_handlers and api_handlers.API_HANDLERS:
        for handler in api_handlers.API_HANDLERS.values():
            try:
                for model_info in handler.get_models():
                     name = model_info.get("name", "")
                     if name in EXCLUDED:
                         continue
                     is_multimodal = model_info.get("multimodal", False)

                     model_entry = {
                          "name": model_info.get("name", "unknown"),
                          "model": model_info.get("name", "unknown"),
                          "size": model_info.get("size_bytes", 0),
                          "digest": model_info.get("digest", ""),
                          "details": {
                               "parameter_size": model_info.get("parameters", "N/A"),
                               "quantization_level": model_info.get("quantization", "N/A"),
                               "family": model_info.get("family", handler.name),
                               "format": model_info.get("format", "N/A"),
                               "multimodal": is_multimodal,
                               "pro": model_info.get("pro", False)
                          }
                     }
                     ollama_models.append(model_entry)
            except Exception as e:
                 logger.error(f"Failed to get tags from handler {handler.name}: {e}")
    else:
         logger.warning("/api/tags called but no handlers are loaded.")

    return JSONResponse(content={"models": ollama_models})

@compute_router.get("/v1/models", summary="List available models (OpenAI v1 compatible)")
async def list_models_v1_endpoint():
    """
    Provides an OpenAI-compatible /v1/models endpoint.

    This endpoint returns a list of available models in a standardized format,
    while also including custom 'parameter_size' and 'multimodal' fields
    that the Observer AI frontend uses for a richer
... [TRUNCATED]
```

### File: api\fireworks_handler.py
```py
#!/usr/bin/env python3
import os
import json
import logging
import httpx  # Use httpx for async requests
from fastapi.responses import StreamingResponse

# Import base class and custom exceptions
from api_handlers import BaseAPIHandler, ConfigError, BackendAPIError, HandlerError

logger = logging.getLogger("fireworks_handler")

class FireworksAPIHandler(BaseAPIHandler):
    """
    Asynchronous handler for Fireworks AI API requests using httpx,
    with mapping for user-friendly model names.
    """
    FIREWORKS_API_URL = "https://api.fireworks.ai/inference/v1/chat/completions"

    def __init__(self):
        super().__init__("fireworks")

        # --- Model Mapping ---
        # Dictionary mapping display names to actual model IDs and parameters
        self.model_map = {
            # Simple mapping with just two models
            "llama4-scout": {
                "model_id": "accounts/fireworks/models/llama4-scout-instruct-basic",
                "parameters": "109B",
                "multimodal": True
            },
            "llama4-maverick": {
                "model_id": "accounts/fireworks/models/llama4-maverick-instruct-basic",
                "parameters": "400B",
                "multimodal": True
            },
            "gpt-oss-120b": {
                "model_id": "accounts/fireworks/models/gpt-oss-120b",
                "parameters": "120B",
                "multimodal": False 
            },
        }

        # Define supported models for display using the pretty names from the map
        self.models = [
            {"name": display_name, "parameters": model_info.get("parameters", "N/A"),
            "multimodal": model_info.get("multimodal", False), "pro": True}
            for display_name, model_info in self.model_map.items()
        ]
        # --- End Model Mapping ---

        self.api_key = os.environ.get("FIREWORKS_API_KEY")
        if not self.api_key:
            logger.error("FIREWORKS_API_KEY environment variable not set. Fireworks handler will fail.")

        # Log the DISPLAY names that will be shown to the user
        logger.info("FireworksAPIHandler registered display models: %s", [m["name"] for m in self.models])

        # Base headers
        self.base_headers = {
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    async def handle_request(self, request_data: dict):
        """
        Process a /v1/chat/completions request asynchronously via Fireworks AI.
        Translates display model name to actual Fireworks model ID.
        Returns either dict (non-streaming) or StreamingResponse (streaming).
        """
        if not self.api_key:
            raise ConfigError("FIREWORKS_API_KEY is not configured on the server.")

        # --- Get Display Name and Translate to Actual Model ID ---
        display_model_name = request_data.get("model")
        if not display_model_name:
            raise ValueError("Request data must include a 'model' field (using the display name).")

        # Look up the display name in our map
        model_info = self.model_map.get(display_model_name)
        if not model_info:
            # If the display name isn't found, the model is unsupported by this mapping
            logger.warning(f"Received request for unmapped Fireworks model display name: {display_model_name}")
            raise ValueError(f"Model display name '{display_model_name}' is not recognized or supported.")

        actual_model_id = model_info.get("model_id")
        if not actual_model_id:
            # Should not happen if map is defined correctly, but good practice to check
            logger.error(f"Internal configuration error: Missing 'model_id' for display name '{display_model_name}' in model_map.")
            raise ConfigError(f"Internal mapping error for model '{display_model_name}'.")
        # --- End Translation ---

        # --- Prepare API Call ---
        # Create a copy of the request data to modify
        payload = request_data.copy()
        # Set the 'model' in the payload to the ACTUAL Fireworks ID
        payload["model"] = actual_model_id

        # Default values from the curl example
        if "max_tokens" not in payload:
            payload["max_tokens"] = 16384
        if "top_p" not in payload:
            payload["top_p"] = 1
        if "top_k" not in payload:
            payload["top_k"] = 40
        if "presence_penalty" not in payload:
            payload["presence_penalty"] = 0
        if "frequency_penalty" not in payload:
            payload["frequency_penalty"] = 0
        if "temperature" not in payload:
            payload["temperature"] = 0.6

        # Update headers (in case API key was missing during init)
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {self.api_key}"

        logger.info(f"Calling Fireworks API: display_model='{display_model_name}', actual_model='{actual_model_id}', streaming={payload.get('stream', False)}")

        # --- Check for streaming ---
        if payload.get("stream", False):
            return StreamingResponse(
                self._stream_fireworks_response(headers, payload, display_model_name, actual_model_id),
                media_type="text/event-stream"
            )

        # --- Make Non-Streaming API Call using httpx ---
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(self.FIREWORKS_API_URL, headers=headers, json=payload)
                response.raise_for_status()
                response_data = response.json()

        # --- Error Handling ---
        except httpx.RequestError as exc:
            logger.error(f"Fireworks API request failed (network/connection): {exc}")
            raise BackendAPIError(f"Could not connect to Fireworks API: {exc}", status_code=503) from exc
        except httpx.HTTPStatusError as exc:
            error_body = exc.response.text
            status_code = exc.response.status_code
            logger.error(f"Fireworks API returned error {status_code} for model {actual_model_id}: {error_body[:500]}")
            try:
                error_json = exc.response.json()
                message = error_json.get("error", {}).get("message", error_body)
            except json.JSONDecodeError:
                message = error_body
            raise BackendAPIError(f"Fireworks API Error ({status_code}): {message}", status_code=status_code) from exc
        except Exception as exc:
            logger.exception(f"An unexpected error occurred during Fireworks API call for model {actual_model_id}")
            raise HandlerError(f"Unexpected error processing Fireworks request: {exc}") from exc

        # --- Log Conversation (using display name for consistency) ---
        prompt_text = ""
        response_text = ""
        try:
            messages = request_data.get("messages", [])
            if messages and isinstance(messages[-1].get("content"), str):
                prompt_text = messages[-1].get("content", "")[:500]
            if 'choices' in response_data and response_data['choices']:
                choice = response_data['choices'][0]
                if 'message' in choice and 'content' in choice['message']:
                    response_text = choice['message']['content'][:500]
        except Exception as log_parse_err:
            logger.warning(f"Could not parse prompt/response for logging: {log_parse_err}")

        # --- Conversation logging now handled centrally in compute.py ---

        # --- Return Response ---
        # Replace actual ID with display name in response
        if "model" in response_data:
            response_data["model"] = display_model_name

        logger.info(f"Successfully processed Fireworks request for display model '{display_model_name}'.")
        return response_data

    async def _stream_fireworks_response(self, headers: dict, payload: dict, display_model_name: str, actual_model_id: str):
        """Stream SSE chunks from Fireworks API."""
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                async with client.stream("POST", self.FIREWORKS_API_URL, headers=headers, json=payload) as response:
                    response.raise_for_status()
                    async for line in response.aiter_lines():
                        if line.startswith("data: "):
                            # Replace actual model ID with display name in streaming chunks
                            chunk_data = line[6:]  # Remove "data: " prefix
                            if chunk_data != "[DONE]":
                                try:
                                    chunk_json = json.loads(chunk_data)
                                    if "model" in chunk_json:
                                        chunk_json["model"] = display_model_name
                                    yield f"data: {json.dumps(chunk_json)}\n\n"
                                except json.JSONDecodeError:
                                    # If we can't parse, just forward as-is
                                    yield f"data: {chunk_data}\n\n"
                            else:
                                yield f"data: {chunk_data}\n\n"
        except httpx.RequestError as exc:
            logger.error(f"Fireworks streaming API request failed: {exc}")
            yield f"data: {json.dumps({'error': f'Connection error: {exc}'})}\n\n"
        except httpx.HTTPStatusError as exc:
            error_body = exc.response.text
            logger.error(f"Fireworks streaming API error {exc.response.status_code}: {error_body[:500]}")
            yield f"data: {json.dumps({'error': f'API error ({exc.response.status_code}): {error_body}'})}\n\n"
        except Exception as exc:
            logger.exception(f"Unexpected error in Fireworks streaming for model {actual_model_id}")
            yield f"data: {json.dumps({'error': f'Unexpected error: {exc}'})}\n\n"

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
