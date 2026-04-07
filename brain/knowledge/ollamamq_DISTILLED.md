---
id: ollamamq
type: knowledge
owner: OA_Triage
---
# ollamamq
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# ollamaMQ

`ollamaMQ` is a high-performance, asynchronous message queue dispatcher and load balancer designed to sit in front of one or more [Ollama](https://ollama.ai/) API instances. It acts as a smart proxy that queues incoming requests from multiple users and dispatches them in parallel to multiple Ollama backends using a fair-share round-robin scheduler with least-connections load balancing.

![Rust](https://img.shields.io/badge/rust-2024-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Ollama](https://img.shields.io/badge/Ollama-Proxy-7ed321.svg)

## 🚀 Features

- **Multi-Backend Load Balancing**: Distribute requests across multiple Ollama instances using a **Least Connections + Round Robin** strategy.
- **Parallel Processing**: Unlike basic proxies, `ollamaMQ` can process multiple requests simultaneously (one per available backend), significantly increasing throughput for multiple users.
- **Backend Health Checks**: Automatically monitors backend status every 10 seconds; offline instances are temporarily skipped and marked in the TUI.
- **Per-User Queuing**: Each user (identified by the `X-User-ID` header) has their own FIFO queue.
- **Fair-Share Scheduling**: Prevents any single user from monopolizing all available backends.
- **Transparent Header Forwarding**: Full support for all HTTP headers (including `X-User-ID`) passed to and from Ollama, ensuring compatibility with tools like **Claude Code**.
- **VIP & Boost Modes**: Absolute priority (VIP) or increased frequency (Boost) for specific users.
- **Real-Time TUI Dashboard**: Monitor backend health, active requests, queue depths, and throughput in real-time.
- **OpenAI Compatibility**: Supports standard OpenAI-compatible endpoints.
- **Async Architecture**: Built on `tokio` and `axum` for high concurrency.

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
- `-o, --ollama-urls <URL1,URL2>`: Comma-separated list of Ollama server URLs (default: `http://localhost:11434`)
- `-t, --timeout <SECONDS>`: Request timeout in seconds (default: `300`)
- `--no-tui`: Disable the interactive TUI dashboard (useful for Docker/CI)
- `--allow-all-routes`: Enable fallback proxy for non-standard endpoints
- `-h, --help`: Print help message
- `-V, --version`: Print version information

**Example:**

```bash
ollamaMQ --port 8080 --ollama-urls http://10.0.0.1:11434,http://10.0.0.2:11434 --timeout 600
```

**Docker Example:**

```bash
docker run -d \
  --name ollamamq \
  -p 8080:8080 \
  chlebon/ollamamq --port 8080 --ollama-urls http://192.168.1.5:11434 --timeout 600
```

### API Proxying

Point your LLM clients to the `ollamaMQ` port (`11435`) and include the `X-User-ID` header.

#### Supported Endpoints:

- `GET /health` (Internal health check)
- `GET /` (Ollama Status)
- `POST /api/generate`
- `POST /api/chat`
- `POST /api/embed`
- `POST /api/embeddings`
- `GET /api/tags`
- `POST /api/show`
- `POST /api/create`
- `POST /api/copy`
- `DELETE /api/delete`
- `POST /api/pull`
- `POST /api/push`
- `GET/HEAD/POST /api/blobs/{digest}`
- `GET /api/ps`
- `GET /api/version`
- `POST /v1/chat/completions` (OpenAI Compatible)
- `POST /v1/completions` (OpenAI Compatible)
- `POST /v1/embeddings` (OpenAI Compatible)
- `GET /v1/models` (OpenAI Compatible)
- `GET /v1/models/{model}` (OpenAI Compatible)


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
      - OLLAMA_URLS=http://host.docker.internal:11434
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

| Variable      | Description                    | Default                  |
| ------------- | ------------------------------ | ------------------------ |
| `OLLAMA_URLS` | URLs of the Ollama servers     | `http://localhost:11434` |
| `PORT`        | Port for ollamaMQ to listen on | `11435`                  |
| `TIMEOUT`     | Request timeout in seconds     | `300`                    |

### Connecting to Different Ollama Servers

#### Local Ollama (on host machine)

```bash
docker run -d \
  --name ollamamq \
  -p 11435:11435 \
  -e OLLAMA_URLS=http://host.docker.internal:11434 \
  chlebon/ollamamq
```

#### Remote Ollama Server

```bash
docker run -d \
  --name ollamamq \
  -p 11435:11435 \
  -e OLLAMA_URLS=https://ollama.example.com:11434 \
  chlebon/ollamamq
```

#### Custom Port on Same Server

```bash
docker run -d \
  --name ollamamq \
  -p 8080:8080 \
  -e OLLAMA_URLS=http://host.docker.internal:11436 \
  -e PORT=8080 \
  chlebon/ollamamq
```

#### Ollama in Docker (different container)

```bash
docker run -d \
  --name ollamamq \
  --network ollama-network \
  -p 11435:11435 \
  -e OLLAMA_URLS=http://ollama:11434 \
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

1. Client sends a request with `X-User-ID`.
2. `ollamaMQ` pushes the request into a user-specific queue.
3. The background worker checks for available backends (Online & not busy).
4. If a backend is free, the worker pops the next task (fair-share rotation) and **spawns a parallel task**.
5. The request is proxied to the selected Ollama backend.
6. The response is streamed back to the client in real-time, while the worker can immediately start another task on a different backend.

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

### File: docker-entrypoint.sh
```sh
#!/bin/sh
set -e

OLLAMA_URLS="${OLLAMA_URLS:-http://localhost:11434}"
PORT="${PORT:-11435}"
TIMEOUT="${TIMEOUT:-300}"

exec /app/ollamaMQ --port "$PORT" --ollama-urls "$OLLAMA_URLS" --timeout "$TIMEOUT" "$@"

```

### File: test_dispatcher.sh
```sh
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

### File: src\dispatcher.rs
```rs
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

pub enum ResponsePart {
    Status(StatusCode, HeaderMap),
    Chunk(Bytes),
    Error(reqwest::Error),
}

pub struct Task {
    pub method: Method,
    pub path: String,
    pub headers: HeaderMap,
    pub body: Bytes,
    pub responder: mpsc::Sender<ResponsePart>,
}

#[derive(Clone)]
pub struct BackendStatus {
    pub url: String,
    pub active_requests: usize,
    pub processed_count: usize,
    pub is_online: bool,
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
    pub backend_freed: Notify,
    pub backends: Mutex<Vec<BackendStatus>>,
    pub last_backend_idx: Mutex<usize>,
    pub timeout: u64,
}

impl AppState {
    pub fn new(ollama_urls: Vec<String>, timeout: u64) -> Self {
        let (blocked_ips, blocked_users) = Self::load_blocked_items();
        let backends = ollama_urls.into_iter()
            .map(|url| BackendStatus {
                url,
                active_requests: 0,
                processed_count: 0,
                is_online: true, // Default to true until first check
            })
            .collect();

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
            backend_freed: Notify::new(),
            backends: Mutex::new(backends),
            last_backend_idx: Mutex::new(0),
            timeout,
        }
    }

    fn load_blocked_items() -> (HashSet<IpAddr>, HashSet<String>) {
        if let Ok(content) = fs::read_to_string(BLOCKED_FILE) {
            if let Ok(config) = serde_json::from_str::<BlockedConfig>(&content) {
                return (config.ips, config.users);
            }
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
    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(state.timeout))
        .build()
        .unwrap();
    let mut current_idx = 0;

    // Background Health Check
    let health_state = state.clone();
    let health_client = client.clone();
    tokio::spawn(async move {
        loop {
            let backends_to_check: Vec<(usize, String)> = {
                let backends = health_state.backends.lock().unwrap();
                backends.iter().enumerate().map(|(i, b)| (i, b.url.clone())).collect()
            };

            for (idx, url) in backends_to_check {
                let check_url = format!("{}/api/tags", url);
                let is_online = health_client.get(&check_url).send().await.is_ok();
                
                let mut backends = health_state.backends.lock().unwrap();
                if backends[idx].is_online != is_online {
                    info!("Backend {} status changed to: {}", url, if is_online { "ONLINE" } else { "OFFLINE" });
                    backends[idx].is_online = is_online;
                }
            }
            tokio::time::sleep(std::time::Duration::from_secs(10)).await;
        }
    });

    loop {
        let selection_opt = {
            let mut queues = state.queues.lock().unwrap();
            let mut backends = state.backends.lock().unwrap();
            let mut last_idx = state.last_backend_idx.lock().unwrap();
            
            // 1. Find an available online backend (Limit: 1 request per backend)
            let online_indices: Vec<usize> = backends.iter()
                .enumerate()
                .filter(|(_, b)| b.is_online && b.active_requests < 1)
                .map(|(i, _)| i)
                .collect();

            if online_indices.is_empty() {
                None
            } else {
                let mut target_user = None;
                let vip = state.vip_user.lock().unwrap().clone();
                let boost = state.boost_user.lock().unwrap().clone();
                let mut counter = state.global_counter.lock().unwrap();

                let mut active_users: Vec<String> = queues.keys()
                    .filter(|u| !queues.get(*u).unwrap().is_empty())
                    .cloned()
                    .collect();

                if active_users.is_empty() {
                    None
                } else {
                    active_users.sort_by(|a, b| {
                        let a_total = state.processed_counts.lock().unwrap().get(a).cloned().unwrap_or(0);
                        let b_total = state.processed_counts.lock().unwrap().get(b).cloned().unwrap_or(0);
                        a_total.cmp(&b_total).then_with(|| a.cmp(b))
                    });

                    if let Some(ref v) = vip { if active_users.contains(v) { target_user = Some(v.clone()); } }
                    if target_user.is_none() {
                        if let Some(ref b) = boost {
                            if active_users.contains(b) && *counter % 2 == 0 { target_user = Some(b.clone()); }
                        }
                    }
                    if target_user.is_none() {
                        if current_idx >= active_users.len() { current_idx = 0; }
                        target_user = Some(active_users[current_idx].clone());
                        current_idx += 1;
                    }

                    match target_user {
                        Some(user_id) => {
                            let task = queues.get_mut(&user_id).unwrap().pop_front().unwrap();
                            *counter += 1;
                            
                            // Round-Robin among eligible backends with min connections
                            let min_conns = online_indices.iter().map(|&i| backends[i].active_requests).min().unwrap();
                            let candidates: Vec<usize> = online_indices.iter().cloned().filter(|&i| backends[i].active_requests == min_conns).collect();
                            let candidate_pos = candidates.iter().position(|&i| i > *last_idx).unwrap_or(0);
                            let selected_backend_idx = candidates[candidate_pos];
                            
                            *last_idx = selected_backend_idx;
                            backends[selected_backend_idx].active_requests += 1;
                            
                            Some((user_id, task, selected_backend_idx, backends[selected_backend_idx].url.clone()))
                        }
                        None => None
                    }
                }
            }
        };

        match selection_opt {
            Some((user_id, task, backend_idx, backend_url)) => {
                let state_clone = state.clone();
                let client_clone = client.clone();
                let url = format!("{}{}", backend_url, task.path);

                tokio::spawn(async move {
                    let is_blocked = {
                        let user_ips = state_clone.user_ips.lock().unwrap();
                        let blocked_ips = state_clone.blocked_ips.lock().unwrap();
                        let blocked_users = state_clone.blocked_users.lock().unwrap();
                        blocked_users.contains(&user_id) || user_ips.get(&user_id).map(|ip| blocked_ips.contains(ip)).unwrap_or(false)
                    };

                    if is_blocked || task.responder.is_closed() {
                        let mut dropped = state_clone.dropped_counts.lock().unwrap();
                        *dropped.entry(user_id.clone()).or_insert(0) += 1;
                    } else {
                        {
                            let mut processing = state_clone.processing_counts.lock().unwrap();
                            *processing.entry(user_id.clone()).or_insert(0) += 1;
                        }

                        let res_fut = client_clone.request(task.method, &url)
                            .headers(task.headers)
                            .body(task.body)
                            .send();

                        match res_fut.await {
                            Ok(response) => {
                                let status = response.status();
                                let mut headers = response.headers().clone();
                                headers.remove(axum::http::header::TRANSFER_ENCODING);
                                headers.remove(axum::http::header::CONTENT_LENGTH);

                                if task.responder.send(ResponsePart::Status(status, headers)).await.is_ok() {
                                    let mut stream = response.bytes_stream();
                                    let mut client_disconnected = false;
                                    while let Some(chunk_res) = stream.next().await {
                                        match chunk_res {
                                            Ok(chunk) => {
                                                if task.responder.send(ResponsePart::Chunk(chunk)).await.is_err() {
                                                    client_disconnected = true;
                                                    break;
                                                }
                                            }
                                            Err(_) => break,
                                        }
                                    }

                                    if !client_disconnected {
                                        let mut counts = state_clone.processed_counts.lock().unwrap();
                                        *counts.entry(user_id.clone()).or_insert(0) += 1;
                                    } else {
                                        let mut dropped = state_clone.dropped_counts.lock().unwrap();
                                        *dropped.entry(user_id.clone()).or_insert(0) += 1;
                                    }
                                }
                            }
                            Err(e) => {
                                let _ = task.responder.send(ResponsePart::Error(e)).await;
                                let mut dropped = state_clone.dropped_counts.lock().unwrap();
                                *dropped.entry(user_id.clone()).or_insert(0) += 1;
                            }
                        }

                        {
                            let mut processing = state_clone.processing_counts.lock().unwrap();
                            if let Some(count) = processing.get_mut(&user_id) { *count = count.saturating_sub(1); }
                        }
                    }

                    {
                        let mut backends = state_clone.backends.lock().unwrap();
                        backends[backend_idx].active_requests = backends[backend_idx].active_requests.saturating_sub(1);
                        backends[backend_idx].processed_count += 1;
                    }
                    state_clone.backend_freed.notify_one();
                });
            }
            None => {
                tokio::select! {
                    _ = state.notify.notified() => {},
                    _ = state.backend_freed.notified() => {},
                }
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

    if state.is_ip_blocked(&ip) {
        warn!("Blocked request from IP: {} for user: {}", ip, user_id);
        return (StatusCode::FORBIDDEN, "IP blocked").into_response();
    }

    if state.is_user_blocked(&user_id) {
        warn!("Blocked request from user: {} (IP: {})", user_id, ip);
        return (StatusCode:
... [TRUNCATED]
```

### File: src\main.rs
```rs
use axum::{
    Router,
    routing::{any, get, post},
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

    /// Ollama server URLs (comma-separated list)
    #[arg(short, long, value_delimiter = ',', default_value = "http://localhost:11434")]
    ollama_urls: Vec<String>,

    /// Request timeout in seconds
    #[arg(short, long, default_value_t = 300)]
    timeout: u64,

    /// Disable TUI dashboard
    #[arg(long)]
    no_tui: bool,

    /// Allow all routes (enable fallback proxy)
    #[arg(long, default_value_t = false)]
    allow_all_routes: bool,
}

struct TuiState {
    visible: bool,
    toggle_notify: Arc<Notify>,
}

#[tokio::main]
async fn main() {
    let args = Args::parse();
    let ollama_urls: Vec<String> = args.ollama_urls.iter()
        .map(|url| url.trim_end_matches('/').to_string())
        .collect();

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

    let state = Arc::new(AppState::new(ollama_urls, args.timeout));

    let worker_state = state.clone();
    tokio::spawn(async move {
        run_worker(worker_state).await;
    });

    let mut app = Router::new()
        .route("/health", get(|| async { "OK" }))
        // Ollama API Endpoints (Explicitly listed)
        .route("/", any(proxy_handler))
        .route("/api/generate", any(proxy_handler))
        .route("/api/chat", any(proxy_handler))
        .route("/api/embed", any(proxy_handler))
        .route("/api/embeddings", any(proxy_handler))
        .route("/api/tags", any(proxy_handler))
        .route("/api/show", any(proxy_handler))
        .route("/api/create", any(proxy_handler))
        .route("/api/copy", any(proxy_handler))
        .route("/api/delete", any(proxy_handler))
        .route("/api/pull", any(proxy_handler))
        .route("/api/push", any(proxy_handler))
        .route("/api/blobs/{digest}", any(proxy_handler))
        .route("/api/ps", any(proxy_handler))
        .route("/api/version", any(proxy_handler))
        // OpenAI Compatible Endpoints
        .route("/v1/chat/completions", any(proxy_handler))
        .route("/v1/completions", any(proxy_handler))
        .route("/v1/embeddings", any(proxy_handler))
        .route("/v1/models", any(proxy_handler))
        .route("/v1/models/{model}", any(proxy_handler));

    // Optional fallback
    if args.allow_all_routes {
        app = app.fallback(proxy_handler);
    }

    let app = app
        .layer(axum::extract::DefaultBodyLimit::max(1024 * 1024 * 1024)) // 1GB limit
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

### File: src\tui.rs
```rs
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

use crate::dispatcher::{AppState, BackendStatus};

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
    backends: Vec<BackendStatus>,
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
        let backends = state.backends.lock().unwrap().clone();

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
            backends,
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
            .constraints([
                Constraint::Percentage(25),
                Constraint::Percentage(40),
                Constraint::Percentage(35),
            ])
            .split(main_chunks[1]);

        f.render_widget(self.render_backends(snapshot), content_chunks[0]);
        f.render_stateful_widget(self.render_users(snapshot), content_chunks[1], &mut self.table_state);

        let right_chunks = Layout::default()
            .direction(Direction::Vertical)
            .constraints([Constraint::Percentage(60), Constraint::Percentage(40)])
            .split(content_chunks[2]);

        f.render_stateful_widget(self.render_queues(snapshot, right_chunks[0].width), right_chunks[0], &mut self.table_state);
        f.render_stateful_widget(self.render_blocked(snapshot), right_chunks[1], &mut self.blocked_table_state);

        f.render_widget(self.render_help(), main_chunks[2]);
        if self.show_help {
            f.render_widget(self.render_detailed_help(), main_chunks[3]);
        }
    }

    fn render_stats(&self, snapshot: &
... [TRUNCATED]
```

