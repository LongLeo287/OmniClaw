---
id: ollamamq-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:14.665017
---

# KNOWLEDGE EXTRACT: ollamamq
> **Extracted on:** 2026-03-30 17:49:54
> **Source:** ollamamq

---

## File: `.dockerignore`
```
# Git
.git
.gitignore

# Build outputs
target/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Documentation
*.md
demo.gif
demo-test.gif

# Test files
test_dispatcher.sh

# Docker files (not needed in image)
Dockerfile
docker-compose.yml
.dockerignore

# Logs
*.log
blocked_items.json

# CI/CD
.github/
.gitlab-ci.yml
```

## File: `.gitignore`
```
/target
ollamamq.log
blocked_items.json
```

## File: `Cargo.toml`
```
[package]
name = "ollamaMQ"
version = "0.2.4"
edition = "2024"
description = "High-performance Ollama proxy with per-user fair-share queuing, round-robin scheduling, and a real-time TUI dashboard."
license = "MIT"
authors = ["Chleba <chlebik@gmail.com>"]
repository = "https://github.com/Chleba/ollamaMQ"
homepage = "https://github.com/Chleba/ollamaMQ"

[dependencies]
axum = "0.8.8"
bytes = "1.11.1"
reqwest = { version = "0.13.2", default-features = false, features = ["json", "stream", "rustls"] }
tokio = { version = "1.49.0", features = ["full"] }
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
tracing-appender = "0.2"
ratatui = "0.29"
crossterm = "0.28"
tokio-stream = { version = "0.1.18", features = ["sync"] }
futures-util = "0.3.32"
clap = { version = "4.5", features = ["derive"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

## File: `demo-test.tape`
```
Output demo-test.gif

Set FontSize 11
Set Width 1200
Set Height 720

Type "./test_dispatcher.sh"

Enter

Sleep 16s
```

## File: `demo.tape`
```
Output demo.gif

Set FontSize 11
Set Width 1200
Set Height 720

Type "./ollamaMQ"

Enter

Sleep 3s
Type "?"
Sleep 5s

Type "jjjjjjjjjjjjjjj"
Type "kkkkkkk"

Type "?"

Type "b"
Sleep 1s
Type "j"
Sleep 1s
Type "b"
Sleep 1s
Type "j"

Type "l"
Type "j"
Type "j"

Sleep 2s

Type "l"
Type "j"
Type "B"

Sleep 2s

```

## File: `docker-compose.yml`
```yaml
services:
  # Optional: Uncomment if you want to run Ollama in Docker as well
  # ollama:
  #   image: ollama/ollama:latest
  #   container_name: ollama
  #   volumes:
  #     - ollama_data:/root/.ollama
  #   ports:
  #     - "11434:11434"
  #   restart: unless-stopped

  ollamamq:
    build: .
    image: chlebon/ollamamq:latest
    container_name: ollamamq
    ports:
      - "11435:11435"
    environment:
      # If using host Ollama on Linux:
      # 1. Ensure Ollama is listening on 0.0.0.0 (export OLLAMA_HOST=0.0.0.0)
      # 2. Use http://host.docker.internal:11434
      # If using the 'ollama' service above, use http://ollama:11434
      - OLLAMA_URL=http://host.docker.internal:11434
      - PORT=11435
      - TIMEOUT=300
      - RUST_LOG=info
    command: ["--no-tui"]
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:11435/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

# volumes:
#   ollama_data:
```

## File: `docker-entrypoint.sh`
```bash
#!/bin/sh
set -e

OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}"
PORT="${PORT:-11435}"
TIMEOUT="${TIMEOUT:-300}"

exec /app/ollamaMQ --port "$PORT" --ollama-url "$OLLAMA_URL" --timeout "$TIMEOUT" "$@"
```

## File: `Dockerfile`
```
# Build stage
FROM rust:alpine AS builder

# Add dependencies for building
RUN apk add --no-cache musl-dev llvm-dev clang pkgconfig openssl-dev

WORKDIR /build

# Create dummy project for caching dependencies
COPY Cargo.toml Cargo.lock ./
RUN mkdir src && echo "fn main() {}" > src/main.rs && cargo build --release && rm -rf src

# Copy source code
COPY src ./src

# Build the real binary
# Touch main.rs to ensure it's recompiled
RUN touch src/main.rs && cargo build --release

# Runtime stage
FROM alpine:3.20

WORKDIR /app

# Install ca-certificates and other runtime deps
RUN apk add --no-cache ca-certificates libgcc

# Copy the binary from builder
COPY --from=builder /build/target/release/ollamaMQ /app/ollamaMQ

# Copy entrypoint script
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Expose the default port
EXPOSE 11435

# Set entrypoint
ENTRYPOINT ["/app/docker-entrypoint.sh"]
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Chleba

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# ollamaMQ

`ollamaMQ` is a high-performance, asynchronous message queue dispatcher designed to sit in front of an [Ollama](https://ollama.ai/) API instance. It acts as a smart proxy that queues incoming requests from multiple users and dispatches them sequentially to the Ollama backend, preventing resource exhaustion and ensuring fair sharing of GPU/CPU resources.

![Rust](https://img.shields.io/badge/rust-2024-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Ollama](https://img.shields.io/badge/Ollama-Proxy-7ed321.svg)

## 🚀 Features

- **Per-User Queuing**: Each user (identified by the `X-User-ID` header) has their own FIFO queue.
- **Fair-Share Round-Robin Scheduling**: A background worker rotates through active users, processing one request at a time from each to prevent any single user from monopolizing the backend.
- **VIP Mode**: Assign absolute priority to a specific user (controllable via TUI).
- **Boost Mode**: Every 5th request is prioritized for a specific user (controllable via TUI).
- **Active Request Tracking**: Real-time monitoring of currently processing requests (marked with `▶` in the TUI).
- **Instant Blocking**: Drop all queued tasks immediately when a user or IP is blocked.
- **Full Streaming Support**: Proxies streaming responses from Ollama in real-time, maintaining per-user ordering while delivering tokens as they are generated.
- **Real-Time TUI Dashboard**: A built-in terminal interface powered by `ratatui` for monitoring queue depths, active users, and request throughput in real-time.
- **OpenAI Compatibility**: Supports standard OpenAI-compatible endpoints, making it easy to use with existing tools and libraries.
- **Async Architecture**: Built on `tokio` and `axum` for non-blocking I/O and high concurrency.

![ollamaMQ TUI Dashboard](demo.gif)

## 🛠️ Installation

Ensure you have [Rust](https://rustup.rs/) (2024 edition or later) and [Ollama](https://ollama.ai/) installed.

### Option 1: Install via Cargo (Recommended)

```bash
cargo install ollamaMQ
```

### Option 2: From Source

1. Clone the repository:

   ```bash
   git clone https://github.com/Chleba/ollamaMQ.git
   cd ollamaMQ
   ```

2. Build and install locally:
   ```bash
   cargo install --path .
   ```

## 🏃 Usage

### Docker Installation

#### Using Docker Compose (Recommended)

1. Ensure Docker and Docker Compose are installed.
2. Start your local Ollama instance (defaulting to `localhost:11434`).
3. Run:
   ```bash
   docker compose up -d
   ```

#### Using Docker CLI

First build the image from the local Dockerfile:

```bash
docker build -t chlebon/ollamamq .
```

Then run the container:

```bash
docker run -d \
  --name ollamamq \
  -p 11435:11435 \
  --restart unless-stopped \
  chlebon/ollamamq
```

### Command Line Arguments

`ollamaMQ` supports several options to configure the proxy:

- `-p, --port <PORT>`: Port to listen on (default: `11435`)
- `-o, --ollama-url <URL>`: Ollama server URL (default: `http://localhost:11434`)
- `-t, --timeout <SECONDS>`: Request timeout in seconds (default: `300`)
- `--no-tui`: Disable the interactive TUI dashboard (useful for Docker/CI)
- `-h, --help`: Print help message
- `-V, --version`: Print version information

**Example:**

```bash
ollamaMQ --port 8080 --ollama-url http://192.168.1.5:11434 --timeout 600 --no-tui
```

**Docker Example:**

```bash
docker run -d \
  --name ollamamq \
  -p 8080:8080 \
  chlebon/ollamamq --port 8080 --ollama-url http://192.168.1.5:11434 --timeout 600
```

### API Proxying

Point your LLM clients to the `ollamaMQ` port (`11435`) and include the `X-User-ID` header.

#### Supported Endpoints:

- `GET /health` (Internal health check)
- `GET /` (Ollama Native)
- `GET /api/tags` (Ollama Native)
- `GET /api/version" (Ollama Native)
- `POST /api/embed` (Ollama Native)
- `POST /api/generate` (Ollama Native)
- `POST /api/chat` (Ollama Native)
- `GET /v1/models` (OpenAI Compatible)
- `POST /v1/embeddings` (OpenAI Compatible)
- `POST /v1/chat/completions" (OpenAI Compatible)
- `POST /v1/completions` (OpenAI Compatible)

#### Example (cURL):

```bash
curl -X POST http://localhost:11435/api/chat \
  -H "X-User-ID: developer-1" \
  -d '{
    "model": "qwen3.5:35b",
    "messages": [{"role": "user", "content": "Explain quantum computing."}],
    "stream": true
  }'
```

### Dashboard Controls

The interactive TUI dashboard provides a live view of the dispatcher's state:

- **`j` / `k`** or **Arrows**: Navigate the user/blocked list.
- **`Tab`** or **`h` / `l`**: Switch between the Users and Blocked panels.
- **`p`**: Toggle **VIP** status for the selected user (absolute priority).
- **`b`**: Toggle **Boost** status for the selected user (prioritizes every 5th request).
- **`x`**: Block the selected user.
- **`X`**: Block the selected user's IP address.
- **`u`**: Unblock the selected user or IP (works in both panels).
- **`q`** or **Esc**: Exit the dashboard and stop the application.
- **`?`**: Toggle detailed help.

**Visual Indicators:**
- `★` (Magenta): **VIP User** (absolute priority).
- `⚡` (Yellow): **Boosted User** (every 5th request priority).
- `▶` (Cyan): Request is currently being processed/streamed.
- `●` (Green): User has requests waiting in the queue.
- `○` (Gray): User is idle (no active or queued requests).
- `✖` (Red): User or IP is blocked.

### Logging

Logs are automatically written to `ollamamq.log` in the current working directory. This keeps the terminal clear for the TUI dashboard while allowing you to monitor system events and debug backend communication.

## 🐳 Docker

### Docker Compose

The included `docker-compose.yml` provides a ready-to-use configuration:

```yaml
services:
  ollamamq:
    build: .
    image: chlebon/ollamamq:latest
    container_name: ollamamq
    ports:
      - "11435:11435"
    environment:
      - OLLAMA_URL=http://host.docker.internal:11434
      - PORT=11435
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped
```

**Note for Linux Users:**
When running in Docker on Linux to access a host-based Ollama:

1.  **Listen on all interfaces:** Ollama must be configured to listen on `0.0.0.0`. You can do this by setting `export OLLAMA_HOST=0.0.0.0` before starting the Ollama service (or editing the systemd unit file).
2.  **Firewall:** Ensure your firewall (e.g., `ufw`) allows traffic from the Docker bridge (usually `172.17.0.1/16`) to port `11434`.
3.  **Host Gateway:** The `extra_hosts` setting in `docker-compose.yml` maps `host.docker.internal` to your host's IP address.

### Dockerfile

The Dockerfile uses a multi-stage build:

- **Build stage**: Uses `rust:1.85-alpine` to compile the release binary
- **Runtime stage**: Uses `alpine:3.20` with only `ca-certificates` for a minimal footprint (~10MB)

### Environment Variables

| Variable     | Description                    | Default                  |
| ------------ | ------------------------------ | ------------------------ |
| `OLLAMA_URL` | URL of the Ollama server       | `http://localhost:11434` |
| `PORT`       | Port for ollamaMQ to listen on | `11435`                  |
| `TIMEOUT`    | Request timeout in seconds     | `300`                    |

### Connecting to Different Ollama Servers

#### Local Ollama (on host machine)

```bash
docker run -d \
  --name ollamamq \
  -p 11435:11435 \
  -e OLLAMA_URL=http://host.docker.internal:11434 \
  chlebon/ollamamq
```

#### Remote Ollama Server

```bash
docker run -d \
  --name ollamamq \
  -p 11435:11435 \
  -e OLLAMA_URL=https://ollama.example.com:11434 \
  chlebon/ollamamq
```

#### Custom Port on Same Server

```bash
docker run -d \
  --name ollamamq \
  -p 8080:8080 \
  -e OLLAMA_URL=http://host.docker.internal:11436 \
  -e PORT=8080 \
  chlebon/ollamamq
```

#### Ollama in Docker (different container)

```bash
docker run -d \
  --name ollamamq \
  --network ollama-network \
  -p 11435:11435 \
  -e OLLAMA_URL=http://ollama:11434 \
  chlebon/ollamamq
```

### Port Configuration

- **11435**: The proxy port that clients connect to (exposed by default)
- **11434**: The Ollama server port (internal, not exposed)

To change the proxy port, use the `PORT` environment variable:

```bash
docker run -d \
  --name ollamamq \
  -p 8080:8080 \
  -e PORT=8080 \
  chlebon/ollamamq
```

## 🏗️ Architecture

- **`src/main.rs`**: Entry point, HTTP server initialization, and TUI lifecycle management.
- **`src/dispatcher.rs`**: Core logic for queuing, round-robin scheduling, and Ollama proxying.
- **`src/tui.rs`**: Implementation of the terminal-based monitoring dashboard.

### Request Flow

1. Client sends a request to one of the supported endpoints with `X-User-ID`.
2. `ollamaMQ` pushes the request into a user-specific queue.
3. The background worker selects the next user in rotation and pops a task.
4. The task is forwarded to the Ollama backend (`localhost:11434`).
5. The response is streamed back to the client in real-time through an async channel, keeping the worker occupied until the generation is complete.

## 📦 Publishing to Docker Hub

To publish a new version of `ollamaMQ` to Docker Hub, follow these steps:

1. **Update Version**: Update the version number in `Cargo.toml`.
2. **Build and Tag**:

   ```bash
   # Build the image for the current version
   docker build -t chlebon/ollamamq:v0.2.4 .
   
   # Tag it as latest
   docker tag chlebon/ollamamq:v0.2.4 chlebon/ollamamq:latest
   ```

3. **Push to Hub**:

   ```bash
   # Log in to Docker Hub (if not already logged in)
   docker login
   
   # Push the versioned tag
   docker push chlebon/ollamamq:v0.2.4
   
   # Push the latest tag
   docker push chlebon/ollamamq:latest
   ```

## 🧪 Development

### Stress Testing

You can use the provided `test_dispatcher.sh` script to simulate multiple users and verify the dispatcher's behavior under load:

```bash
./test_dispatcher.sh
```

![ollamaMQ Stress Test](demo-test.gif)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if applicable).
```

## File: `test_dispatcher.sh`
```bash
#!/bin/bash

# Configuration
BASE_URL="${BASE_URL:-http://localhost:11435}"
MODEL="${MODEL:-qwen3.5:35b}"
ENDPOINTS=("/api/generate" "/api/chat" "/v1/chat/completions" "/v1/completions")

# Expanded list of 50 users to thoroughly test scrolling and high load
USERS=(
    "alice" "bob" "charlie" "david" "eve" 
    "frank" "grace" "heidi" "ivan" "judy" 
    "kevin" "laura" "mike" "nancy" "oscar"
    "peggy" "quinn" "ralph" "steve" "trent"
    "ursula" "victor" "walter" "xenia" "yvonne"
    "zelda" "arthur" "beatrice" "clarence" "dorothy"
    "edward" "florence" "george" "harriet" "isaac"
    "jane" "kurt" "lily" "marvin" "nellie"
    "owen" "pearl" "quintin" "rose" "samuel"
    "tessa" "ulysses" "vera" "william" "yasmin"
)

echo "🚀 Starting 50-User Stress Test for ollamaMQ..."
echo "Target Base: $BASE_URL"
echo "Endpoints: ${ENDPOINTS[*]}"
echo "Total Potential Users: ${#USERS[@]}"
echo "----------------------------------------"

# Function to send a request
send_request() {
    local user=$1
    local id=$2
    local endpoint=${ENDPOINTS[$RANDOM % ${#ENDPOINTS[@]}]}
    local url="${BASE_URL}${endpoint}"
    
    local payload=""
    if [[ "$endpoint" == "/api/chat" || "$endpoint" == "/v1/chat/completions" ]]; then
        payload="{\"model\": \"$MODEL\", \"messages\": [{\"role\": \"user\", \"content\": \"Req $id\"}], \"stream\": false}"
    else
        payload="{\"model\": \"$MODEL\", \"prompt\": \"Req $id\", \"stream\": false}"
    fi

    # Send request and capture HTTP status code + response
    response=$(curl -s -X POST "$url" \
        -H "X-User-ID: $user" \
        -H "Content-Type: application/json" \
        -d "$payload")
    status_code=$? # Note: we'll use curl exit code or check response for 200

    if [ -n "$response" ]; then
        echo "✅ [SUCCESS] User: $user | Endp: $endpoint | Res: ${response:0:100}"
    else
        echo "❌ [FAILED] User: $user | Endp: $endpoint | Req: $id"
    fi
}

# Function to simulate a client disconnecting early
send_and_cancel() {
    local user=$1
    local id=$2
    local endpoint=${ENDPOINTS[$RANDOM % ${#ENDPOINTS[@]}]}
    local url="${BASE_URL}${endpoint}"
    
    echo "🏃 [CANCEL TEST] User: $user | Req: $id (Will disconnect early)"
    
    # Start curl in background, wait a tiny bit, then kill it
    curl -s -X POST "$url" \
        -H "X-User-ID: $user" \
        -H "Content-Type: application/json" \
        -d "{\"model\": \"${MODEL}\", \"prompt\": \"Canceled request $id\"}" > /dev/null &
    
    local curl_pid=$!
    # Sleep slightly less than the dispatcher's 500ms artificial delay to test 'is_closed' check,
    # or slightly more to test 'tokio::select' abortion during backend call.
    sleep 0.3
    kill $curl_pid 2>/dev/null
}

# Function to send a request with an image (multimodal llava test)
send_image_request() {
    local user=$1
    local id=$2
    local url="${BASE_URL}/api/generate"
    
    # Base64 encoded tiny 1x1 red pixel PNG
    local b64_pixel="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    
    echo "🖼️ [IMAGE TEST] User: $user | Req: $id (Sending multimodal request to ${MODEL})"
    
    # Send request and capture HTTP status code
    response=$(curl -s -X POST "$url" \
        -H "X-User-ID: $user" \
        -H "Content-Type: application/json" \
        -d "{\"model\": \"${MODEL}\", \"prompt\": \"What is in this image?\", \"images\": [\"$b64_pixel\"], \"stream\": false}")

    if [ -n "$response" ]; then
        echo "✅ [SUCCESS] User: $user | Endpoint: IMAGE | Res: ${response:0:100}"
    else
        echo "❌ [FAILED] User: $user | Req: $id"
    fi
}

# Check if dispatcher is reachable (using /health)
if ! curl -s -o /dev/null "${BASE_URL}/health" --max-time 2; then
    echo "❌ Error: Dispatcher is not reachable at ${BASE_URL}"
    echo "   Please run 'docker compose up' or 'cargo run' in another terminal first."
    exit 1
fi

total_dispatched=0

echo "📡 Dispatching randomized requests in the background..."
for user in "${USERS[@]}"; do
    # Randomize number of requests between 1 and 12
    num_reqs=$((1 + RANDOM % 12))
    total_dispatched=$((total_dispatched + num_reqs))
    
    echo "👤 User: $user -> Sending $num_reqs requests..."
    
    for ((i=1; i<=num_reqs; i++)); do
        # 10% chance to simulate a client cancellation
        # 5% chance to send an image request
        # 85% chance for a normal request
        rand=$((RANDOM % 100))
        if [ $rand -lt 10 ]; then
            send_and_cancel "$user" "$i"
        elif [ $rand -lt 15 ]; then
            send_image_request "$user" "$i" &
        else
            send_request "$user" "$i" &
        fi
    done
    
    # Small sleep between user bursts to stagger the incoming load
    sleep 0.1
done

echo "----------------------------------------"
echo "⏳ Total of $total_dispatched requests dispatched across ${#USERS[@]} users."
echo "⏳ Waiting for all tasks to complete... (Watch the TUI!)"

# Wait for all background processes to finish
wait

echo "----------------------------------------"
echo "🏁 High-load stress test completed."
```

## File: `src/dispatcher.rs`
```rust
use axum::{
    body::{Body, Bytes},
    extract::{ConnectInfo, State},
    http::{HeaderMap, Method, StatusCode},
    response::IntoResponse,
};
use futures_util::StreamExt;
use serde::{Deserialize, Serialize};
use std::{
    collections::{HashMap, HashSet, VecDeque},
    fs,
    net::{IpAddr, SocketAddr},
    sync::{Arc, Mutex},
};
use tokio::sync::{Notify, mpsc};
use tokio_stream::wrappers::ReceiverStream;
use tracing::{info, warn};

const BLOCKED_FILE: &str = "blocked_items.json";

#[derive(Serialize, Deserialize, Default)]
struct BlockedConfig {
    ips: HashSet<IpAddr>,
    users: HashSet<String>,
}

pub struct Task {
    pub method: Method,
    pub path: String,
    pub body: Bytes,
    pub responder: mpsc::Sender<Result<Bytes, reqwest::Error>>,
}

pub struct AppState {
    pub queues: Mutex<HashMap<String, VecDeque<Task>>>,
    pub processing_counts: Mutex<HashMap<String, usize>>,
    pub processed_counts: Mutex<HashMap<String, usize>>,
    pub dropped_counts: Mutex<HashMap<String, usize>>,
    pub user_ips: Mutex<HashMap<String, IpAddr>>,
    pub blocked_ips: Mutex<HashSet<IpAddr>>,
    pub blocked_users: Mutex<HashSet<String>>,
    pub vip_user: Mutex<Option<String>>,
    pub boost_user: Mutex<Option<String>>,
    pub global_counter: Mutex<usize>,
    pub notify: Notify,
    pub ollama_url: String,
    pub timeout: u64,
}

impl AppState {
    pub fn new(ollama_url: String, timeout: u64) -> Self {
        let (blocked_ips, blocked_users) = Self::load_blocked_items();
        Self {
            queues: Mutex::new(HashMap::new()),
            processing_counts: Mutex::new(HashMap::new()),
            processed_counts: Mutex::new(HashMap::new()),
            dropped_counts: Mutex::new(HashMap::new()),
            user_ips: Mutex::new(HashMap::new()),
            blocked_ips: Mutex::new(blocked_ips),
            blocked_users: Mutex::new(blocked_users),
            vip_user: Mutex::new(None),
            boost_user: Mutex::new(None),
            global_counter: Mutex::new(0),
            notify: Notify::new(),
            ollama_url,
            timeout,
        }
    }

    fn load_blocked_items() -> (HashSet<IpAddr>, HashSet<String>) {
        if let Ok(content) = fs::read_to_string(BLOCKED_FILE)
            && let Ok(config) = serde_json::from_str::<BlockedConfig>(&content)
        {
            return (config.ips, config.users);
        }
        (HashSet::new(), HashSet::new())
    }

    fn save_blocked_items(&self) {
        let config = BlockedConfig {
            ips: self.blocked_ips.lock().unwrap().clone(),
            users: self.blocked_users.lock().unwrap().clone(),
        };
        if let Ok(content) = serde_json::to_string_pretty(&config) {
            let _ = fs::write(BLOCKED_FILE, content);
        }
    }

    pub fn block_ip(&self, ip: IpAddr) {
        {
            let mut ips = self.blocked_ips.lock().unwrap();
            ips.insert(ip);
        }
        self.save_blocked_items();
        warn!("IP blocked: {}", ip);
    }

    pub fn block_user(&self, user_id: String) {
        {
            let mut users = self.blocked_users.lock().unwrap();
            users.insert(user_id.clone());
        }
        self.save_blocked_items();
        warn!("User blocked: {}", user_id);
    }

    #[allow(dead_code)]
    pub fn unblock_ip(&self, ip: IpAddr) {
        {
            let mut ips = self.blocked_ips.lock().unwrap();
            ips.remove(&ip);
        }
        self.save_blocked_items();
        info!("IP unblocked: {}", ip);
    }

    #[allow(dead_code)]
    pub fn unblock_user(&self, user_id: &str) {
        {
            let mut users = self.blocked_users.lock().unwrap();
            users.remove(user_id);
        }
        self.save_blocked_items();
        info!("User unblocked: {}", user_id);
    }

    pub fn is_ip_blocked(&self, ip: &IpAddr) -> bool {
        self.blocked_ips.lock().unwrap().contains(ip)
    }

    pub fn is_user_blocked(&self, user_id: &str) -> bool {
        self.blocked_users.lock().unwrap().contains(user_id)
    }
}

pub async fn run_worker(state: Arc<AppState>) {
    // 5-minute timeout for backend requests
    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(state.timeout))
        .build()
        .unwrap();
    let mut current_idx = 0;

    loop {
        let task_opt = {
            let mut queues = state.queues.lock().unwrap();
            let vip = state.vip_user.lock().unwrap().clone();
            let boost = state.boost_user.lock().unwrap().clone();
            let mut counter = state.global_counter.lock().unwrap();

            // 1. Check VIP first (Absolute priority)
            let mut target_user = None;
            if let Some(vip_id) = &vip {
                if queues.get(vip_id).map_or(false, |q| !q.is_empty()) {
                    target_user = Some(vip_id.clone());
                }
            }

            // 2. Check Boost (Every 5th request)
            if target_user.is_none() && (*counter + 1) % 5 == 0 {
                if let Some(boost_id) = &boost {
                    if queues.get(boost_id).map_or(false, |q| !q.is_empty()) {
                        target_user = Some(boost_id.clone());
                    }
                }
            }

            // 3. Fallback to Round-Robin
            if target_user.is_none() {
                let mut active_users: Vec<String> = queues
                    .iter()
                    .filter(|(_, q)| !q.is_empty())
                    .map(|(k, _)| k.clone())
                    .collect();
                active_users.sort();

                if !active_users.is_empty() {
                    if current_idx >= active_users.len() {
                        current_idx = 0;
                    }
                    target_user = Some(active_users[current_idx].clone());
                    current_idx += 1;
                }
            }

            match target_user {
                Some(user_id) => {
                    let task = queues.get_mut(&user_id).unwrap().pop_front().unwrap();
                    *counter += 1;
                    Some((user_id, task))
                }
                None => None,
            }
        };

        match task_opt {
            Some((user_id, task)) => {
                // Check if user or IP was blocked after the task was queued
                let is_blocked = {
                    let user_ips = state.user_ips.lock().unwrap();
                    let blocked_ips = state.blocked_ips.lock().unwrap();
                    let blocked_users = state.blocked_users.lock().unwrap();

                    let user_blocked = blocked_users.contains(&user_id);
                    let ip_blocked = user_ips
                        .get(&user_id)
                        .map(|ip| blocked_ips.contains(ip))
                        .unwrap_or(false);

                    user_blocked || ip_blocked
                };

                if is_blocked {
                    info!("Dropping queued task for blocked user/IP: {}", user_id);
                    let mut dropped = state.dropped_counts.lock().unwrap();
                    *dropped.entry(user_id).or_insert(0) += 1;
                    continue;
                }

                // Check if client is still connected before processing
                if task.responder.is_closed() {
                    info!("Skipping task for user {} - client disconnected", user_id);
                    let mut dropped = state.dropped_counts.lock().unwrap();
                    *dropped.entry(user_id).or_insert(0) += 1;
                    continue;
                }

                {
                    let mut processing = state.processing_counts.lock().unwrap();
                    *processing.entry(user_id.clone()).or_insert(0) += 1;
                }

                let url = format!("{}{}", state.ollama_url, task.path);
                let body_str = if !task.body.is_empty() {
                    String::from_utf8_lossy(&task.body).trim().to_string()
                } else {
                    "EMPTY".to_string()
                };

                // info!(
                //     "OUTGOING REQUEST to Ollama:\nMethod: {}\nURL: {}\nUser: {}\nBody: {}",
                //     task.method, url, user_id, body_str
                // );

                let res_fut = match task.method {
                    Method::POST => client.post(url).body(task.body),
                    Method::GET => client.get(url),
                    _ => continue,
                }
                .send();

                tokio::select! {
                    res = res_fut => {
                        match res {
                            Ok(response) => {
                                let mut stream = response.bytes_stream();
                                let mut client_disconnected = false;
                                let mut first_chunk = true;

                                while let Some(chunk_res) = stream.next().await {
                                    let chunk = match chunk_res {
                                        Ok(c) => c,
                                        Err(e) => {
                                            info!("Error reading from backend: {}", e);
                                            break;
                                        }
                                    };

                                    if first_chunk {
                                        let content = String::from_utf8_lossy(&chunk);
                                        // info!("Response for user {}: {}", user_id, content.trim());
                                        first_chunk = false;
                                    }

                                    if task.responder.send(Ok(chunk)).await.is_err() {
                                        info!("Client disconnected during streaming for user {}", user_id);
                                        client_disconnected = true;
                                        break;
                                    }
                                }

                                if client_disconnected {
                                    let mut dropped = state.dropped_counts.lock().unwrap();
                                    *dropped.entry(user_id.clone()).or_insert(0) += 1;
                                } else {
                                    info!("Request {} for user {} completed", task.path, user_id);
                                    let mut counts = state.processed_counts.lock().unwrap();
                                    *counts.entry(user_id.clone()).or_insert(0) += 1;
                                }
                            }
                            Err(e) => {
                                info!("Request {} for user {} failed: {}", task.path, user_id, e);
                                let _ = task.responder.send(Err(e)).await;
                                let mut dropped = state.dropped_counts.lock().unwrap();
                                *dropped.entry(user_id.clone()).or_insert(0) += 1;
                            }
                        }
                    }
                    _ = task.responder.closed() => {
                        info!("Client disconnected while waiting for backend response for user {}", user_id);
                        let mut dropped = state.dropped_counts.lock().unwrap();
                        *dropped.entry(user_id.clone()).or_insert(0) += 1;
                    }
                }

                {
                    let mut processing = state.processing_counts.lock().unwrap();
                    if let Some(count) = processing.get_mut(&user_id) {
                        *count = count.saturating_sub(1);
                    }
                }
            }
            None => {
                info!("Worker idle, waiting for tasks...");
                state.notify.notified().await;
            }
        }
    }
}

pub async fn proxy_handler(
    State(state): State<Arc<AppState>>,
    ConnectInfo(addr): ConnectInfo<SocketAddr>,
    method: Method,
    headers: HeaderMap,
    axum::extract::OriginalUri(uri): axum::extract::OriginalUri,
    body: Bytes,
) -> impl IntoResponse {
    let path = uri.path().to_string();
    let ip = addr.ip();
    let user_id = headers
        .get("X-User-ID")
        .and_then(|h| h.to_str().ok())
        .unwrap_or("anonymous")
        .to_string();

    let body_str = String::from_utf8_lossy(&body).trim().to_string();
    info!(
        "INCOMING REQUEST:\nMethod: {}\nURI: {}\nUser: {}\nIP: {}\nHeaders: {:?}\nBody: {}",
        method, uri, user_id, ip, headers, body_str
    );

    if state.is_ip_blocked(&ip) {
        warn!("Blocked request from IP: {} for user: {}", ip, user_id);
        return (StatusCode::FORBIDDEN, "IP blocked").into_response();
    }

    if state.is_user_blocked(&user_id) {
        warn!("Blocked request from user: {} (IP: {})", user_id, ip);
        return (StatusCode::FORBIDDEN, "User blocked").into_response();
    }

    {
        let mut ips = state.user_ips.lock().unwrap();
        ips.insert(user_id.clone(), ip);
    }

    let (tx, rx) = mpsc::channel(32);
    let task = Task {
        path,
        method,
        responder: tx,
        body,
    };

    {
        let mut queues = state.queues.lock().unwrap();
        queues
            .entry(user_id.clone())
            .or_insert_with(VecDeque::new)
            .push_back(task);
    }

    state.notify.notify_one();

    let stream = ReceiverStream::new(rx);
    Body::from_stream(stream).into_response()
}
```

## File: `src/main.rs`
```rust
use axum::{
    Router,
    routing::{get, post},
};
use clap::Parser;
use std::net::SocketAddr;
use std::sync::{Arc, Mutex};
use tokio::sync::Notify;
use tracing::info;
use tracing_subscriber::EnvFilter;

mod dispatcher;
mod tui;

use crate::dispatcher::{AppState, proxy_handler, run_worker};

use std::io::IsTerminal;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Port to listen on
    #[arg(short, long, default_value_t = 11435)]
    port: u16,

    /// Ollama server URL
    #[arg(short, long, default_value = "http://localhost:11434")]
    ollama_url: String,

    /// Request timeout in seconds
    #[arg(short, long, default_value_t = 300)]
    timeout: u64,

    /// Disable TUI dashboard
    #[arg(long)]
    no_tui: bool,
}

struct TuiState {
    visible: bool,
    toggle_notify: Arc<Notify>,
}

#[tokio::main]
async fn main() {
    let args = Args::parse();
    let ollama_url = args.ollama_url.trim_end_matches('/').to_string();

    // Determine if we should run TUI
    let use_tui = !args.no_tui && std::io::stdout().is_terminal();

    // Keep the guard alive for the duration of main
    let _guard: Option<tracing_appender::non_blocking::WorkerGuard>;

    if use_tui {
        let file_appender = tracing_appender::rolling::never(".", "ollamamq.log");
        let (non_blocking, g) = tracing_appender::non_blocking(file_appender);
        _guard = Some(g);

        tracing_subscriber::fmt()
            .with_writer(non_blocking)
            .with_ansi(false)
            .with_env_filter(
                EnvFilter::try_from_default_env().unwrap_or_else(|_| EnvFilter::new("info")),
            )
            .init();
    } else {
        _guard = None;
        tracing_subscriber::fmt()
            .with_env_filter(
                EnvFilter::try_from_default_env().unwrap_or_else(|_| EnvFilter::new("info")),
            )
            .init();
    }

    let state = Arc::new(AppState::new(ollama_url, args.timeout));

    let worker_state = state.clone();
    tokio::spawn(async move {
        run_worker(worker_state).await;
    });

    let app = Router::new()
        .route("/health", get(|| async { "OK" }))
        .route("/", get(proxy_handler))
        .route("/api/tags", get(proxy_handler))
        .route("/api/version", get(proxy_handler))
        .route("/api/embed", post(proxy_handler))
        .route("/api/generate", post(proxy_handler))
        .route("/api/chat", post(proxy_handler))
        .route("/v1/models", get(proxy_handler))
        .route("/v1/embeddings", post(proxy_handler))
        .route("/v1/chat/completions", post(proxy_handler))
        .route("/v1/completions", post(proxy_handler))
        .layer(axum::extract::DefaultBodyLimit::max(50 * 1024 * 1024))
        .with_state(state.clone());

    let addr = format!("0.0.0.0:{}", args.port);
    let listener = tokio::net::TcpListener::bind(&addr).await.unwrap();
    info!("Dispatcher running on http://{}", addr);

    if use_tui {
        let tui_state = Arc::new(Mutex::new(TuiState {
            visible: true,
            toggle_notify: Arc::new(Notify::new()),
        }));

        tokio::spawn(async move {
            axum::serve(
                listener,
                app.into_make_service_with_connect_info::<SocketAddr>(),
            )
            .await
            .unwrap();
        });

        // Run TUI on the main thread
        tui_loop(tui_state, state).await;
    } else {
        // Just run the server on the main thread
        axum::serve(
            listener,
            app.into_make_service_with_connect_info::<SocketAddr>(),
        )
        .await
        .unwrap();
    }
}

async fn tui_loop(tui_state: Arc<Mutex<TuiState>>, state: Arc<AppState>) {
    let mut dashboard = tui::TuiDashboard::new();
    let toggle_notify = Arc::new(tui_state.lock().unwrap().toggle_notify.clone());

    loop {
        let visible = {
            let tui_state = tui_state.lock().unwrap();
            tui_state.visible
        };

        if visible {
            match dashboard.run(&state) {
                Ok(continue_loop) => {
                    if !continue_loop {
                        return;
                    }
                }
                Err(e) => {
                    eprintln!("TUI error: {}", e);
                    return;
                }
            }
        } else {
            toggle_notify.notified().await;
        }
    }
}
```

## File: `src/tui.rs`
```rust
use crossterm::{
    ExecutableCommand,
    event::{self, Event, KeyCode, KeyEventKind},
    terminal::{EnterAlternateScreen, LeaveAlternateScreen, disable_raw_mode, enable_raw_mode},
};
use ratatui::{
    backend::CrosstermBackend,
    prelude::*,
    widgets::{Block, Borders, Cell, Paragraph, Row, Table, TableState},
};
use std::collections::{HashMap, HashSet};
use std::io;
use std::net::IpAddr;
use std::sync::Arc;

use crate::dispatcher::AppState;

#[derive(PartialEq)]
enum Panel {
    Users,
    Blocked,
}

struct StateSnapshot {
    queues_len: HashMap<String, usize>,
    processing_counts: HashMap<String, usize>,
    processed_counts: HashMap<String, usize>,
    dropped_counts: HashMap<String, usize>,
    user_ips: HashMap<String, IpAddr>,
    blocked_ips: HashSet<IpAddr>,
    blocked_users: HashSet<String>,
    vip_user: Option<String>,
    boost_user: Option<String>,
    user_ids: Vec<String>,
}

pub struct TuiDashboard {
    table_state: TableState,
    blocked_table_state: TableState,
    active_panel: Panel,
    show_help: bool,
}

impl TuiDashboard {
    pub fn new() -> Self {
        Self {
            table_state: TableState::default(),
            blocked_table_state: TableState::default(),
            active_panel: Panel::Users,
            show_help: false,
        }
    }

    fn capture_snapshot(&self, state: &Arc<AppState>) -> StateSnapshot {
        let queues_len: HashMap<String, usize> = {
            let q = state.queues.lock().unwrap();
            q.iter().map(|(k, v)| (k.clone(), v.len())).collect()
        };
        let processing_counts = state.processing_counts.lock().unwrap().clone();
        let processed_counts = state.processed_counts.lock().unwrap().clone();
        let dropped_counts = state.dropped_counts.lock().unwrap().clone();
        let user_ips = state.user_ips.lock().unwrap().clone();
        let blocked_ips = state.blocked_ips.lock().unwrap().clone();
        let blocked_users = state.blocked_users.lock().unwrap().clone();
        let vip_user = state.vip_user.lock().unwrap().clone();
        let boost_user = state.boost_user.lock().unwrap().clone();

        let mut user_ids: Vec<String> = queues_len.keys().cloned().collect();
        user_ids.sort_by(|a, b| {
            let a_q = queues_len.get(a).unwrap_or(&0) + processing_counts.get(a).unwrap_or(&0);
            let b_q = queues_len.get(b).unwrap_or(&0) + processing_counts.get(b).unwrap_or(&0);
            let a_total = processed_counts.get(a).unwrap_or(&0) + dropped_counts.get(a).unwrap_or(&0);
            let b_total = processed_counts.get(b).unwrap_or(&0) + dropped_counts.get(b).unwrap_or(&0);

            b_q.cmp(&a_q)
                .then_with(|| b_total.cmp(&a_total))
                .then_with(|| a.cmp(b))
        });

        StateSnapshot {
            queues_len,
            processing_counts,
            processed_counts,
            dropped_counts,
            user_ips,
            blocked_ips,
            blocked_users,
            vip_user,
            boost_user,
            user_ids,
        }
    }

    pub fn run(&mut self, state: &Arc<AppState>) -> io::Result<bool> {
        enable_raw_mode()?;
        io::stdout().execute(EnterAlternateScreen)?;
        let mut terminal = Terminal::new(CrosstermBackend::new(io::stdout()))?;
        terminal.clear()?;

        loop {
            let snapshot = self.capture_snapshot(state);
            terminal.draw(|f| self.render(f, &snapshot))?;

            if event::poll(std::time::Duration::from_millis(100))? {
                if let Event::Key(key) = event::read()? {
                    if key.kind != KeyEventKind::Press {
                        continue;
                    }
                    match key.code {
                        KeyCode::Esc | KeyCode::Char('q') => {
                            io::stdout().execute(LeaveAlternateScreen)?;
                            disable_raw_mode()?;
                            terminal.show_cursor()?;
                            return Ok(false);
                        }
                        KeyCode::Char('?') => self.show_help = !self.show_help,
                        KeyCode::Tab | KeyCode::Char('l') | KeyCode::Char('h') => {
                            self.active_panel = match self.active_panel {
                                Panel::Users => Panel::Blocked,
                                Panel::Blocked => Panel::Users,
                            };
                        }
                        KeyCode::Char('p') => {
                            if self.active_panel == Panel::Users {
                                if let Some(i) = self.table_state.selected() {
                                    if i < snapshot.user_ids.len() {
                                        let user_id = snapshot.user_ids[i].clone();
                                        
                                        // 1. Handle VIP
                                        {
                                            let mut vip = state.vip_user.lock().unwrap();
                                            if vip.as_ref() == Some(&user_id) {
                                                *vip = None;
                                            } else {
                                                *vip = Some(user_id.clone());
                                            }
                                        }
                                        
                                        // 2. Clear Boost if we just set VIP
                                        {
                                            let mut boost = state.boost_user.lock().unwrap();
                                            if boost.as_ref() == Some(&user_id) {
                                                *boost = None;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        KeyCode::Char('b') => {
                            if self.active_panel == Panel::Users {
                                if let Some(i) = self.table_state.selected() {
                                    if i < snapshot.user_ids.len() {
                                        let user_id = snapshot.user_ids[i].clone();
                                        
                                        // 1. Handle Boost
                                        {
                                            let mut boost = state.boost_user.lock().unwrap();
                                            if boost.as_ref() == Some(&user_id) {
                                                *boost = None;
                                            } else {
                                                *boost = Some(user_id.clone());
                                            }
                                        }
                                        
                                        // 2. Clear VIP if we just set Boost
                                        {
                                            let mut vip = state.vip_user.lock().unwrap();
                                            if vip.as_ref() == Some(&user_id) {
                                                *vip = None;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        KeyCode::Char('x') => {
                            if self.active_panel == Panel::Users {
                                if let Some(i) = self.table_state.selected() {
                                    if i < snapshot.user_ids.len() {
                                        let user_id = snapshot.user_ids[i].clone();
                                        state.block_user(user_id);
                                    }
                                }
                            }
                        }
                        KeyCode::Char('X') => {
                            if self.active_panel == Panel::Users {
                                if let Some(i) = self.table_state.selected() {
                                    if i < snapshot.user_ids.len() {
                                        let user_id = &snapshot.user_ids[i];
                                        if let Some(ip) = snapshot.user_ips.get(user_id) {
                                            state.block_ip(*ip);
                                        }
                                    }
                                }
                            }
                        }
                        KeyCode::Char('u') => {
                            if self.active_panel == Panel::Blocked {
                                let selected = self.blocked_table_state.selected();
                                if let Some(i) = selected {
                                    let mut items = Vec::new();
                                    for ip in snapshot.blocked_ips.iter() {
                                        items.push(("IP", ip.to_string()));
                                    }
                                    for user in snapshot.blocked_users.iter() {
                                        items.push(("USER", user.clone()));
                                    }
                                    items.sort_by(|a, b| a.1.cmp(&b.1));

                                    if i < items.len() {
                                        let (kind, value) = &items[i];
                                        if *kind == "IP" {
                                            if let Ok(ip) = value.parse() {
                                                state.unblock_ip(ip);
                                            }
                                        } else {
                                            state.unblock_user(value);
                                        }
                                    }
                                }
                            } else if self.active_panel == Panel::Users {
                                if let Some(i) = self.table_state.selected() {
                                    if i < snapshot.user_ids.len() {
                                        let user_id = &snapshot.user_ids[i];
                                        state.unblock_user(user_id);
                                        if let Some(ip) = snapshot.user_ips.get(user_id) {
                                            state.unblock_ip(*ip);
                                        }
                                    }
                                }
                            }
                        }
                        KeyCode::Up | KeyCode::Char('k') => {
                            if self.active_panel == Panel::Users {
                                let i = self.table_state.selected().unwrap_or(0).saturating_sub(1);
                                self.table_state.select(Some(i));
                            } else {
                                let i = self.blocked_table_state.selected().unwrap_or(0).saturating_sub(1);
                                self.blocked_table_state.select(Some(i));
                            }
                        }
                        KeyCode::Down | KeyCode::Char('j') => {
                            if self.active_panel == Panel::Users {
                                let len = snapshot.user_ids.len();
                                if len > 0 {
                                    let i = self.table_state.selected().map(|s| (s + 1).min(len.saturating_sub(1))).unwrap_or(0);
                                    self.table_state.select(Some(i));
                                }
                            } else {
                                let len = snapshot.blocked_ips.len() + snapshot.blocked_users.len();
                                if len > 0 {
                                    let i = self.blocked_table_state.selected().map(|s| (s + 1).min(len.saturating_sub(1))).unwrap_or(0);
                                    self.blocked_table_state.select(Some(i));
                                }
                            }
                        }
                        _ => {}
                    }
                }
            }
        }
    }

    fn render(&mut self, f: &mut Frame, snapshot: &StateSnapshot) {
        if self.active_panel == Panel::Users {
            if snapshot.user_ids.is_empty() {
                self.table_state.select(None);
            } else if self.table_state.selected().is_none() {
                self.table_state.select(Some(0));
            }
        } else {
            let blocked_total = snapshot.blocked_ips.len() + snapshot.blocked_users.len();
            if blocked_total == 0 {
                self.blocked_table_state.select(None);
            } else if self.blocked_table_state.selected().is_none() {
                self.blocked_table_state.select(Some(0));
            }
        }

        let area = f.area();
        let main_chunks = Layout::default()
            .direction(Direction::Vertical)
            .constraints([
                Constraint::Length(3), // Stats
                Constraint::Min(0),    // Content
                Constraint::Length(3), // Help bar
                if self.show_help { Constraint::Length(12) } else { Constraint::Length(0) },
            ])
            .split(area);

        f.render_widget(self.render_stats(snapshot), main_chunks[0]);

        let content_chunks = Layout::default()
            .direction(Direction::Horizontal)
            .constraints([Constraint::Percentage(55), Constraint::Percentage(45)])
            .split(main_chunks[1]);

        f.render_stateful_widget(self.render_users(snapshot), content_chunks[0], &mut self.table_state);

        let right_chunks = Layout::default()
            .direction(Direction::Vertical)
            .constraints([Constraint::Percentage(60), Constraint::Percentage(40)])
            .split(content_chunks[1]);

        f.render_stateful_widget(self.render_queues(snapshot, right_chunks[0].width), right_chunks[0], &mut self.table_state);
        f.render_stateful_widget(self.render_blocked(snapshot), right_chunks[1], &mut self.blocked_table_state);

        f.render_widget(self.render_help(), main_chunks[2]);
        if self.show_help {
            f.render_widget(self.render_detailed_help(), main_chunks[3]);
        }
    }

    fn render_stats(&self, snapshot: &StateSnapshot) -> Paragraph<'static> {
        let total_queued: usize = snapshot.queues_len.values().sum();
        let total_processing: usize = snapshot.processing_counts.values().sum();
        let total_processed: usize = snapshot.processed_counts.values().sum();
        let total_dropped: usize = snapshot.dropped_counts.values().sum();

        let stats_line = vec![
            Span::styled(" ollamaMQ ", Style::default().fg(Color::Cyan).bold()),
            Span::raw(" | "),
            Span::styled("Panel: ", Style::default().fg(Color::White)),
            Span::styled(if self.active_panel == Panel::Users { "USERS" } else { "BLOCKED" }, Style::default().fg(Color::Yellow).bold()),
            Span::raw(" | "),
            Span::styled("VIP: ", Style::default().fg(Color::Magenta)),
            Span::styled(snapshot.vip_user.clone().unwrap_or_else(|| "None".to_string()), Style::default().fg(Color::Magenta).bold()),
            Span::raw(" | "),
            Span::styled("Boost: ", Style::default().fg(Color::Yellow)),
            Span::styled(snapshot.boost_user.clone().unwrap_or_else(|| "None".to_string()), Style::default().fg(Color::Yellow).bold()),
            Span::raw(" | "),
            Span::styled("Q: ", Style::default().fg(Color::Yellow)),
            Span::styled((total_queued + total_processing).to_string(), Style::default().fg(Color::Yellow).bold()),
            Span::raw(" | "),
            Span::styled("Done: ", Style::default().fg(Color::Green)),
            Span::styled(total_processed.to_string(), Style::default().fg(Color::Green).bold()),
            Span::raw(" | "),
            Span::styled("Drop: ", Style::default().fg(Color::Red)),
            Span::styled(total_dropped.to_string(), Style::default().fg(Color::Red).bold()),
        ];

        Paragraph::new(Line::from(stats_line)).block(Block::default().borders(Borders::ALL))
    }

    fn render_users(&self, snapshot: &StateSnapshot) -> Table<'static> {
        let rows: Vec<Row> = snapshot.user_ids.iter().map(|user| {
            let queue_len = snapshot.queues_len.get(user).unwrap_or(&0) + snapshot.processing_counts.get(user).unwrap_or(&0);
            let processed = snapshot.processed_counts.get(user).unwrap_or(&0);
            let dropped = snapshot.dropped_counts.get(user).unwrap_or(&0);
            let ip_str = snapshot.user_ips.get(user).map(|i| i.to_string()).unwrap_or_default();
            let is_blocked = snapshot.blocked_users.contains(user) || snapshot.user_ips.get(user).map_or(false, |ip| snapshot.blocked_ips.contains(ip));
            let is_vip = snapshot.vip_user.as_ref() == Some(user);
            let is_boost = snapshot.boost_user.as_ref() == Some(user);

            let (sym, style) = if is_blocked { ("✖ ", Style::default().fg(Color::Red)) }
                              else if is_vip { ("★ ", Style::default().fg(Color::Magenta)) }
                              else if is_boost { ("⚡", Style::default().fg(Color::Yellow)) }
                              else if *snapshot.processing_counts.get(user).unwrap_or(&0) > 0 { ("▶ ", Style::default().fg(Color::Cyan)) }
                              else if *snapshot.queues_len.get(user).unwrap_or(&0) > 0 { ("● ", Style::default().fg(Color::Green)) }
                              else { ("○ ", Style::default().fg(Color::DarkGray)) };

            let mut spans = vec![Span::styled(sym, style), Span::styled(user.clone(), if is_blocked { Style::default().fg(Color::Red).add_modifier(Modifier::CROSSED_OUT) } else if is_vip { Style::default().fg(Color::Magenta).bold() } else if is_boost { Style::default().fg(Color::Yellow).bold() } else { Style::default().fg(Color::White) })];
            if is_vip { spans.push(Span::styled(" [VIP]", Style::default().fg(Color::Magenta).bold())); }
            if is_boost { spans.push(Span::styled(" [BST]", Style::default().fg(Color::Yellow).bold())); }
            if is_blocked { spans.push(Span::styled(" [BLOCKED]", Style::default().fg(Color::Red).bold())); }

            Row::new(vec![Cell::from(Line::from(spans)), Cell::from(ip_str).style(Style::default().fg(Color::Cyan)), Cell::from(queue_len.to_string()), Cell::from(processed.to_string()), Cell::from(dropped.to_string())])
        }).collect();

        Table::new(rows, [Constraint::Percentage(45), Constraint::Percentage(25), Constraint::Percentage(10), Constraint::Percentage(10), Constraint::Percentage(10)])
            .header(Row::new(vec!["User ID", "Last IP", "Q", "Done", "Drop"]).style(Style::default().fg(Color::Yellow).bold()).bottom_margin(1))
            .row_highlight_style(Style::default().bg(Color::Rgb(40, 40, 40)).add_modifier(Modifier::BOLD))
            .highlight_symbol(">> ")
            .block(Block::default().title(" Active Users ").borders(Borders::ALL).border_style(if self.active_panel == Panel::Users { Style::default().fg(Color::Yellow) } else { Style::default().fg(Color::DarkGray) }))
    }

    fn render_queues(&self, snapshot: &StateSnapshot, available_width: u16) -> Table<'static> {
        let total_queued = snapshot.queues_len.values().sum::<usize>() + snapshot.processing_counts.values().sum::<usize>();
        let bar_max_width = ((available_width as f32) * 0.45) as usize;

        let rows: Vec<Row> = snapshot.user_ids.iter().map(|user| {
            let q_len = snapshot.queues_len.get(user).unwrap_or(&0) + snapshot.processing_counts.get(user).unwrap_or(&0);
            let bar_len = if q_len > 0 { ((q_len as f32 / 20.0).min(1.0) * bar_max_width as f32) as usize } else { 0 };
            let color = if snapshot.vip_user.as_ref() == Some(user) { Color::Magenta } else if snapshot.boost_user.as_ref() == Some(user) { Color::Yellow } else if *snapshot.processing_counts.get(user).unwrap_or(&0) > 0 { Color::Cyan } else { Color::Green };
            let bar = format!("{:<width$}", "⠿".repeat(bar_len), width = bar_max_width);
            let pct = if total_queued > 0 { (q_len as f64 / total_queued as f64) * 100.0 } else { 0.0 };
            Row::new(vec![Cell::from(user.clone()), Cell::from(bar).style(Style::default().fg(color)), Cell::from(format!("{} ({:.0}%)", q_len, pct)).style(Style::default().fg(color).bold())])
        }).collect();

        Table::new(rows, [Constraint::Percentage(30), Constraint::Percentage(45), Constraint::Percentage(25)])
            .header(Row::new(vec!["User ID", "Progress", "Num"]).style(Style::default().fg(Color::Yellow).bold()).bottom_margin(1))
            .row_highlight_style(Style::default().bg(Color::Rgb(40, 40, 40)).add_modifier(Modifier::BOLD))
            .highlight_symbol(">> ")
            .block(Block::default().title(" Queue Status ").borders(Borders::ALL))
    }

    fn render_blocked(&self, snapshot: &StateSnapshot) -> Table<'static> {
        let mut items = Vec::new();
        for ip in snapshot.blocked_ips.iter() { items.push(("IP", ip.to_string())); }
        for user in snapshot.blocked_users.iter() { items.push(("USER", user.clone())); }
        items.sort_by(|a, b| a.1.cmp(&b.1));

        let rows: Vec<Row> = items.iter().map(|(kind, val)| Row::new(vec![Cell::from(kind.to_string()).style(if *kind == "IP" { Style::default().fg(Color::Cyan) } else { Style::default().fg(Color::Magenta) }), Cell::from(val.clone())])).collect();

        Table::new(rows, [Constraint::Percentage(30), Constraint::Percentage(70)])
            .header(Row::new(vec!["Type", "Value"]).style(Style::default().fg(Color::Yellow).bold()).bottom_margin(1))
            .row_highlight_style(Style::default().bg(Color::Rgb(40, 40, 40)).add_modifier(Modifier::BOLD))
            .highlight_symbol(">> ")
            .block(Block::default().title(" Blocked Items ").borders(Borders::ALL).border_style(if self.active_panel == Panel::Blocked { Style::default().fg(Color::Yellow) } else { Style::default().fg(Color::DarkGray) }))
    }

    fn render_help(&self) -> Paragraph<'static> {
        Paragraph::new(" Tab: Switch | p: VIP | b: Boost | x: Block User | X: Block IP | u: Unblock | q: Quit")
            .block(Block::default().borders(Borders::ALL).title_bottom(Line::from(format!(" v{} ", env!("CARGO_PKG_VERSION"))).alignment(Alignment::Right)))
    }

    fn render_detailed_help(&self) -> Paragraph<'static> {
        Paragraph::new("\n  VIP: 'p' | BOOST: 'b' | BLOCK: 'x' (User) / 'X' (IP) | UNBLOCK: 'u'\n  PANELS: 'Tab' | QUIT: 'q' or 'Esc'\n\n  ★ VIP | ⚡ Boost | ✖ Blocked | ▶ Processing | ● Queued").block(Block::default().title(" Help ").borders(Borders::ALL)).style(Style::default().fg(Color::Gray))
    }
}
```

