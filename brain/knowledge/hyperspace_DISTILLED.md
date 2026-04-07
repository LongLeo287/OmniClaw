---
id: hyperspace
type: knowledge
owner: OA_Triage
---
# hyperspace
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# [H] HyperspaceDB: The Spatial AI Engine

<div align="center">

[![Build Status](https://img.shields.io/github/actions/workflow/status/yarlabs/hyperspacedb/ci.yml?branch=main&style=for-the-badge)](https://github.com/yarlabs/hyperspacedb/actions)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/agpl-3.0)
[![Rust](https://img.shields.io/badge/Rust-Nightly-orange.svg?style=for-the-badge)](https://www.rust-lang.org/)
[![Commercial License](https://img.shields.io/badge/License-Commercial-purple.svg?style=for-the-badge)](COMMERCIAL_LICENSE.md)

**v3.0** | **The World's First Spatial AI Engine.**

[Why Spatial AI?](#-why-a-spatial-ai-engine) • [Use Cases](#-use-cases) • [Architecture](#-architecture) • [Benchmarks](#-performance-benchmarks) • [SDKs](#-sdks)

</div>

---

## 🌌 What is HyperspaceDB?

Traditional vector databases were built to search static PDF files for chatbots. **HyperspaceDB is built for Autonomous Agents, Robotics, and Continuous Learning.**

It is the world's first **Spatial AI Engine** — a mathematically advanced memory infrastructure that models information exactly how the physical world and human cognition are structured: as hierarchical, spatial, and dynamic graphs.

By combining **Hyperbolic Geometry (Poincaré & Lorentz models)**, **Lock-Free Concurrency**, and an **Edge-to-Cloud Serverless architecture**, HyperspaceDB allows machines to navigate massive semantic spaces in microseconds, using a fraction of the RAM required by traditional databases.

## 🧠 Why a Spatial AI Engine? (Beyond RAG)

AI is moving from text-in/text-out to autonomous action. Agents need *episodic memory* and *spatial reasoning*. HyperspaceDB provides the primitives to build it:

* **Fractal Knowledge Graphs:** Euclidean vectors fail at hierarchies. Our native Hyperbolic engine compresses massive trees (like codebases or taxonomies) into 64-dimensional spaces, reducing RAM usage by 50x without losing semantic context.
* **Continuous Reconsolidation:** AI agents need to "sleep" and organize memories. With our **Fast Upsert Path**, **CDC Event Streams**, and built-in **Riemannian Math SDK** (Fréchet mean, parallel transport), your agents can continuously shift and prune vectors dynamically.
* **Edge-to-Cloud & Offline-First:** Drones and humanoid robots can't wait for cloud latency. HyperspaceDB runs directly on Edge hardware, using a **Merkle Tree Delta Sync** protocol (`SyncHandshake`, `SyncPull`, `SyncPush`) to asynchronously handshake and sync episodic memory chunks with the Cloud when the network is available.
* **Serverless at Billion-Scale:** HyperspaceDB dynamically unloads idle logic to disk/S3, enabling you to host millions of vectors across thousands of tenants on a single commodity server, acting as the "Neon of Vector Search."

---

## 🚀 Core Pillars (v3.0)

<table>
  <tr>
    <td>⚙️ <b>Reflex-Level Speed</b></td>
    <td>Built on Nightly Rust. Our <b>ArcSwap Lock-Free architecture</b> and <code>f32</code> SIMD intrinsics deliver up to <b>12,000 Search QPS</b> and <b>60,000 Ingest QPS</b> on a single node.</td>
  </tr>
  <tr>
    <td>🧭 <b>Global Meta-Router</b></td>
    <td>Implements pure <b>Compute/Storage Separation</b>. The RAM-resident <code>MetaRouter</code> queries thousands of underlying HNSW fragments (chunks) in microseconds, pulling heavy data from NVMe/S3 via Paged Loading on the fly.</td>
  </tr>
  <tr>
    <td>🎓 <b>Cognitive Math Engine</b></td>
    <td>First-class HNSW support for Euclidean (L2/Cosine), <b>Poincaré Ball</b>, <b>Lorentz Hyperboloid</b> metrics, and <b>Wasserstein O(N) CFM</b>.
    * **Advanced Geometric Filters**: Added `InBall`, `InBox`, and `InCone` filters to the core engine and gRPC/REST APIs.
    * **Bitset-Based Pruning**: Implemented high-performance sequential filtering over spatial regions.
Execute spatial K-Means, Fréchet Mean, and Parallel Transport directly in the Native SDK. Evaluate datasets via <b>Gromov's Delta-Hyperbolicity</b>.</td>
  </tr>
  <tr>
    <td>📡 <b>Agentic Workflows</b></td>
    <td>Trigger <b>Memory Reconsolidation</b> via Flow Matching natively to shift paradigms. Connect CDC Streams via <code>subscribe_to_events</code> to trigger secondary models the millisecond a vector is stored.</td>
  </tr>
  <tr>
    <td>🧹 <b>Metadata-Driven Pruning</b></td>
    <td>Agents must forget to stay efficient. Use typed numeric Range Filters (<code>energy < 0.1</code>) inside a Hot Vacuum to automatically prune obsolete memories.</td>
  </tr>
  <tr>
    <td>📦 <b>LSM-Tree Storage</b></td>
    <td>Optimized for high-concurrency writes. Hot <b>MemTables</b> continuously flush into immutable <b>Fractal Segments</b> (<code>chunk_N.hyp</code>), enabling near-instant RAM reclamation and stable performance at billion-scale.</td>
  </tr>
  <tr>
    <td>☁️ <b>S3 Cloud Tiering</b></td>
    <td>Native <b>S3/MinIO</b> tiered storage integration. Seamlessly offload cold segments mapping Petabytes of vectors linearly without scaling local SSDs. <i>(Unlock via Cargo feature <code>s3-tiering</code> & <code>HS_STORAGE_BACKEND=s3</code>)</i>.</td>
  </tr>
</table>

## 🤖 Target Use Cases

1.  **Robotics & Autonomous Drones:** On-device semantic memory, Hierarchical SLAM, and offline-first edge synchronization.
2.  **Continuous Learning Systems (AGI):** Frameworks doing Riemannian optimization, memory reconsolidation, and Hausdorff-based graph pruning.
3.  **Enterprise Graph AI:** Merging relational logic with semantic proximity for massive multi-scale data analysis (Code ASTs, Medical Taxonomies).
4.  **High-Load RAG & SaaS:** Traditional search, but significantly cheaper to operate due to Serverless Idle Eviction and multi-tenant isolation.

---

## ⚡ 1 Million Vectors Benchmark (v3.0)
 
We pushed **HyperspaceDB v3.0** to the limit with a **1 Million Vector Dataset**.
The results define a new standard for performance and efficiency.

### 🏆 Hyperbolic Efficiency (Poincaré 64d)
When using the native **Hyperbolic (Poincaré)** metric, HyperspaceDB achieves unparalleled throughput by reducing dimensionality (64d) while preserving semantic structure achievable only with 1024d in Euclidean space.

| Metric | Result | vs Euclidean |
| :--- | :--- | :--- |
| **Throughput** | **156,587 QPS** ⚡ | **8.8x Faster** |
| **P99 Latency** | **2.47 ms** | **3.3x Lower** |
| **Disk Usage** | **687 MB** | **13x Smaller** |

### ⚔️ Euclidean Performance (1024d)
Even in standard Euclidean mode, HyperspaceDB outperforms competitors on standard hardware.

| Database       | Total Time (1M vectors) | Speedup Factor |
| :---           | :---                    | :---           |
| **HyperspaceDB** | **56.4s** ⚡             | **1x** |
| Milvus         | 88.7s                   | 1.6x slower    |
| Qdrant         | 629.4s (10m 29s)        | 11.1x slower   |
| Weaviate       | 2036.3s (33m 56s)       | 36.1x slower   |
 
### 📉 Zero Degradation Architecture
While other databases slow down as data grows, HyperspaceDB maintains consistent throughput.
* **Weaviate** degraded from 738 QPS -> 491 QPS (-33%).
* **Milvus** fluctuated between 6k and 11k QPS.
* **HyperspaceDB** held steady at **~156k QPS** (Hyperbolic) and **~17.8k QPS** (Euclidean).

### 💾 50% Less Disk Usage
Store more, pay less. HyperspaceDB's 1-bit quantization and efficient storage engine require half the disk space of Milvus for the exact same dataset.
 
* **HyperspaceDB:** 9.0 GB (Euclidean) / 0.7 GB (Hyperbolic)
* **Milvus:** 18.5 GB
 
> *Benchmark Config: 1M Vectors, 1024 Dimensions (Euclidean) vs 64 Dimensions (Hyperbolic), Batch Size 1000.*

---

## 🔒 Security

* **API Keys**: Secure endpoints with `HYPERSPACE_API_KEY` environment variable.
* **Header**: Clients must send `x-api-key: <key>`.
* **Zero-Knowledge**: Server stores only SHA-256 hash of the key in memory.

## 🤝 Federated Clustering & P2P Swarm (v3.0)
HyperspaceDB implements two distinct clustering architectures designed for both high availability in the Cloud and dynamic Edge-to-Edge discovery for robotics swarms.

### 1. Leader-Follower Replication (Cloud / High Availability)
* **Node Identity**: Each node generates a unique UUID (`node_id`) and maintains a Lamport logical clock.
* **Leader**: Handles Writes (Coordinator). Streams WAL events. Manages Cluster Topology.
* **Follower**: Read-Only replica. Can be promoted to Leader.

### 2. Edge-to-Edge Gossip Swarm (Robotics / Local-First)
Designed for robotic swarms without a central Leader. Uses raw UDP multicasting to form a decentralized, self-healing network.
* **Zero-Dependency**: Built on raw `tokio::net::UdpSocket` (no heavy libp2p dependencies).
* **Heartbeats**: Nodes broadcast state via UDP. Disconnected nodes are automatically evicted after a TTL interval.
* **Auto-Discovery**: Discover peers and instantly initiate a Delta Sync handshake to resolve diverging graphs.
* **Enable**: Set `HS_GOSSIP_PEERS` (e.g. `192.168.1.10:7946`) or `HS_GOSSIP_PORT` to join the swarm.

### Data Synchronization (Edge-to-Cloud Delta Sync)
HyperspaceDB uses a **256-bucket Merkle Tree** for efficient data drift detection, ideal for WASM/Edge targets updating offline:

* **Granular Hashing**: Each collection is partitioned into 256 buckets (by vector ID % 256)
* **XOR Rolling Hash**: Each bucket maintains an incremental hash of its vectors
* **Fast Diffing**: Compare bucket hashes to identify which partition is out of sync
* **Bandwidth Optimization**: Sync only affected buckets instead of full collection

#### WASM Sync Example
When your robot or web client comes back online, initiating a Sync is mathematically minimal:

```javascript
// 1. Handshake: Send local 256 bucket hashes
const { diffBuckets } = await client.syncHandshake(collection, localBuckets);

if (diffBuckets.length > 0) {
    // 2. Pull only the modified/missing buckets from Cloud
    const stream = client.syncPull(collection, diffBuckets);
    stream.on('data', (vectorData) => applyLocal(vectorData));
    
    // 3. Push local offline edits back to Cloud
    client.syncPush(localEditsQueue);
}
```

#### Digest API
```bash
# HTTP
GET /api/collections/{name}/digest

# gRPC
rpc GetDigest(DigestRequest) returns (DigestResponse)
```

Response includes:
- `logical_clock`: Lamport timestamp
- `state_hash`: Root hash (XOR of all buckets)
- `buckets`: Array of 256 bucket hashes
- `count`: Total vector count

### Cluster Topology API
View the logic state of the cluster via HTTP:

```bash
# Get Replication State
curl http://localhost:50050/api/cluster/status

# Get Decentralized Swarm Peers (Gossip)
curl http://localhost:50050/api/swarm/peers
```

```json
{
  "gossip_enabled": true,
  "peer_count": 2,
  "peers": [
    {
       "node_id": "e8...0e",
       "role": "Leader",
       "addr": "192.168.1.20:50050",
       "logical_clock": 42,
       "healthy": true
    }
  ]
}
```

### Starting a Cluster
```bash
# Start Leader
./hyperspace-server --port 50051 --role leader

# Start Follower
./hyperspace-server --port 50052 --role follower --leader http://127.0.0.1:50051
```


## 🕸️ WebAssembly (WASM) Support

HyperspaceDB can run directly in the browser via WebAssembly, enabling **Local-First AI** applications with zero network latency.

* **Zero Latency**: Search runs in-memory on the client.
* **Privacy**: Data never leaves the device.
* **Optimized**: Uses `RAMVectorStore` backend for browser environments.

👉 **[Read the WASM Documentation](docs/wasm.md)**

## ⚖️ Heterogeneous Tribunal Framework (Tribunal Router)

HyperspaceDB natively supports the confrontational model of LLM routing (Architect vs. Tribunal) directly on the vector graph.

Using the **Cognitive Math SDK** and the **Graph Traversal API**, the SDK calculates a **Geometric Trust Score** for any LLM claim by verifying the logical path length between concepts in the latent hyperbolic space.

If the geodesic distance (hops) between "Claim A" and "Claim B" on the graph is too large (or disconnected), the Trust Score drops to `0.0` (Hallucination).

```python
from hyperspace.agents import TribunalContext

tribunal = TribunalContext(client, collection_name="knowledge_graph")

# Evaluates structural graph distance between concepts. 
# 1.0 = Truth (Identical), 0.0 = Hallucination (Disconnected)
score = tribunal.evaluate_claim(concept_a_id=12, concept_b_id=45)
```

## 🧠 Hybrid Search (RRF)

Combine the power of Hyperbolic Embeddings with traditional Keyword Search.

```python
# Search for semantic similarity AND keyword match (e.g. "iphone")
results = client.search(
    vector=[0.1]*8, 
    top_k=5, 
    hybrid_query="iphone", 
    hybrid_alpha=0.3
)
```

## 📊 Quantization Modes

All quantization is configured per-collection at creation time via `HS_QUANTIZATION_LEVEL`:

| Mode | env value | Bits/dim | Compression | Best for |
|---|---|---|---|---|
| **SQ8 Anisotropic** | `scalar` (default) | 8 | 8x | Cosine/L2 — best recall at 1 byte/dim |
| **Binary (Hamming)** | `binary` | 1 | 64x | RAM-critical, 100M+ vectors |
| **Lorentz SQ8** | automatic | 8 | 8x | Lorentz metric (auto-selected) |
| **Zonal (MOND)** | `HS_ZONAL_QUANTIZATION=true` | mixed | ~30-40% | Hyperbolic with mixed density |
| **Full f64** | `none` | 64 | 1x | Research / debugging |

The default `scalar` mode uses a **ScaNN-inspired anisotropic loss** $L = \|e_\parallel\|^2 + t_w \cdot \|e_\perp\|^2$ ($t_w=10$), which penalizes directional error more than magnitude error, improving Recall@10 by **+5.3% (Cosine)** and **+3.8% (L2)** versus isotropic SQ8.

---

Each geometry has its own independent backend, now featuring **native support for Qwen3-Embedding (0.6B)** and **YAR v5** models:

| Provider | Description | Recommended For |
|---|---|---|
| **Local ONNX** | Any `.onnx` model from disk | Air-gapped / Edge |
| **HuggingFace** | Auto-download, cache, and chunk | High accuracy / Long context |
| **Remote API** | Mistral / OpenAI / Cohere / Voyage | Cloud API offload |

Example — Config for **Qwen3 (1024d)** and **YAR v5 (128d)**:
```env
HYPERSPACE_EMBED=true

# Cosine via Qwen3 (HuggingFace)
HS_EMBED_COSINE_PROVIDER=huggingface
HS_EMBED_COSINE_HF_MODEL_ID=onnx-community/Qwen3-Embedding-0.6B-ONNX
HS_EMBED_COSINE_DIM=1024
HS_EMBED_COSINE_CHUNK_SIZE=4096   # 32K context window

# Poincaré via YAR Labs v5
HS_EMBED_POINCARE_PROVIDER=huggingface
HS_EMBED_POINCARE_HF_MODEL_ID=YARlabs/v5_Embedding_0.5B
HS_EMBED_POINCARE_DIM=128
```

Direct Search from SDK:
```python
# Server-side text-to-vector search (v3.0.1)
results = client.search_text("Find similar robotics docs", top_k=5)
```

For details see [embeddings.md](docs/book/src/embeddings.md).

---

## 📉 Binary Quantization (1-bit)

Use `Binary` quantization mode to compress vectors by **32x-64x** (vs f32/f64).
Ideal for large-scale datasets where memory is the bottleneck.

---

## 🛠 Architecture

HyperspaceDB strictly follows a **Command-Query Separation (CQS)** pattern:

```mermaid
graph TD
    Client["Client (gRPC)"] -->|Insert| S["Server Service"]
    Cl
... [TRUNCATED]
```

### File: benchmarks\README.md
```md
# HyperspaceDB Benchmarks

> **⚠️ ATTENTION:** Don't take anyone's word for it, verify all numbers yourself! We provide the exact scripts used to generate our results so you can reproduce them on your own hardware.

## 1. Project Overview

This directory contains reproducible benchmark tooling for HyperspaceDB and other vector databases.
The main goal is to measure throughput, latency, and retrieval quality on the same datasets and query sets.

The project now includes:
- a **modular plugin-based runner** (`run_benchmark.py`) for scalable adapter growth (add you DB or custom metrics, if you want);

## 2. Core Functionalities

- Run benchmark against all supported databases at once.
- Run benchmark for only one database adapter.
- Add new database by creating one plugin file in `db_plugins/adapters/`.
- Reuse the same data preparation and metric logic across adapters.
- Compare legacy and modular reports to track metric parity.
- Run durability benchmark (`run_durability_benchmark.py`) independently.

## 3. Docs and Libraries

### Main references
- HuggingFace `datasets` for dataset loading.
- `vectordb-bench` for standardized benchmark cases.
- DB SDKs: `pymilvus`, `qdrant-client`, `chromadb`, Hyperspace Python SDK.
- `torch`, `transformers`, `peft` for embedding generation.

### Install
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e ../sdks/python
```

### Start DB stack
```bash
docker-compose up -d
```

## 4. Current File Structure (Snapshot)

```text
benchmarks/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── download_dataset.py
├── run_benchmark.py
├── run_durability_benchmark.py
├── plugin_runtime.py
├── db_plugins/
    ├── __init__.py
    ├── base.py
    ├── registry.py
    └── adapters/
        ├── __init__.py
        ├── chroma_plugin.py
        ├── hyperspace_plugin.py
        ├── milvus_plugin.py
        └── qdrant_plugin.py

```

## 5. Run Commands

### Benchmark runner
```bash
python3 run_benchmark.py hyper --case=Performance1024D1M
python3 run_benchmark.py --case=Performance1024D1M
python3 run_benchmark.py hyper
```

## 6. Benchmark Metrics

- Throughput (Insert/Search QPS)
- Latency (P50/P95/P99)
- Recall@10, MRR@10, NDCG@10
- System Recall@10 (vs exact brute-force)
- Concurrency profile (C1/C10/C30)
- **LSM-Tree Flush Latency**: Impact of WAL rotation on active search performance.
- **S3 Tiering Cold Latency**: First-access latency for chunks retrieved from cloud storage.
- **Cache Hit Ratio**: Effectiveness of the local `moka` LRU cache.
- Disk usage (Local vs Cloud breakdown).

```

### File: benchmarks\requirements.txt
```txt
pydantic<2.0.0
numpy>=1.26.0,<2.0.0
tqdm>=4.64.0
datasets>=2.8.0
vectordb-bench>=0.1.0
torch>=1.13.0
transformers>=4.25.0
peft>=0.2.0
sentence-transformers>=2.2.0
pymilvus>=2.3.0
qdrant-client>=1.7.0,<1.8.0
weaviate-client>=3.25.0,<4.0.0
chromadb>=0.4.0,<0.5.0
requests>=2.28.0
grpcio>=1.64.0
grpcio-tools>=1.64.0
protobuf>=5.29.0
h5py>=3.7.0
pandas>=2.0.0
pytest>=8.0.0
psycopg2-binary>=2.9.9
pgvector>=0.2.4

```

### File: tests\requirements.txt
```txt
grpcio>=1.50.0
grpcio-tools>=1.50.0
protobuf>=4.21.0
numpy>=1.20.0

```

### File: ARCHITECTURE.md
```md
# HyperspaceDB Architecture Guide

HyperspaceDB is a specialized vector database designed for high-performance hyperbolic embedding search. This document details its internal architecture, storage format, and indexing strategies.

---

## 🏗 System Overview

The system follows a strict **Command-Query Separation (CQS)** pattern, tailored for write-heavy ingestion and latency-sensitive search.

```mermaid
graph TD
    Client[Client (gRPC)] -->|Insert| S[Server Service]
    Client -->|Search| S
    
    subgraph LSM_Tree ["LSM-Tree Storage Engine"]
        S -->|1. Append| WAL[Active WAL]
        WAL -.->|Rotation| Chunk[Immutable Chunk]
        S -->|2. Search| MemT[MemTable (HNSW)]
        MemT -.->|Flush| Chunk
        Chunk -->|Tiering| S3[(S3 / Cloud)]
        Chunk -->|Search| Router{Meta-Router}
        Router -->|Route| Chunk
    end
    
    subgraph Read_Path ["Scatter-Gather Search"]
        S --> Searcher[Chunk Searcher]
        Searcher -->|Parallel mmap| Chunk
        S --> Merge[Result Merger]
    end

    subgraph Embedding_Engine ["Embedding Engine"]
        S -->|InsertText| EE[Embedding Service]
        EE -->|Chunking| ONNX[ONNX Backend]
        EE -->|Pooling| API[Cloud API Backend]
    end
```

---

## 🌌 Cosmological Architecture (The Design Philosophy)

HyperspaceDB relies on principles from modern cosmology to execute vector search dynamically. The database maps semantic dispersion to real physical properties:

1. **Multi-Geometric Routing (The Hubble Tension):**
   Upper layers of the HNSW graph utilize the **Klein projective model**, routing queries via cheap Euclidean chord distances (SIMD-optimized), while the bottom exact-search layer converts metrics back to the **Lorentz hyperboloid** for maximum-precision ranking.
2. **Anisotropic Quantization (The Axis of Evil):**
   Semantic vectors are concentrated along principal components (not cleanly isotropic). Our engine applies a weighted Vector Quantization function ($L \approx ||x||^2 ||e_{||}||^2 + h(x) ||e_{\perp}||^2$) to penalize unaligned orthogonal semantic shifts.
3. **Zonal Quantization (The MOND Hypothesis):**
   At the core of the hyperbolic disk, nodes correspond to broad semantic clusters requiring fewer bits of precision (`i8`/`f16`). Nearing the Euclidean horizon ($||x|| \to 1$), exact relationships demand extreme mapping in pure `f64`.
4. **Density Pruning (The $S_8$ Void Tension):**
   Akin to comic voids and clustered galaxies, HyperspaceDB performs Density-based Graph Pruning. Outlying vectors inherit restricted edge mappings, reducing RAM.
5. **Memory Reconsolidation (AI Sleep Mode):**
   Continuous Riemannian SGD pulls vectors towards an attractor state (e.g. Flow Matching) directly via `TriggerReconsolidation`, restructuring the graph dynamically without full re-indexing.
6. **Cross-Feature Matching (Wasserstein-1):**
   Instead of $O(N^3)$ generic OT, we execute an ultra-fast $O(N)$ 1D L1-CDF algorithm to compare distributions along feature axes directly inside the metric dispatch.

---

## 💾 Storage Layer (LSM-Tree Architecture)

HyperspaceDB 3.0 uses an **LSM-Tree** inspired architecture for vector search, optimized for high throughput and cloud tiering.

### 1. MemTable & WAL
New vectors are first appended to the **Write-Ahead Log (WAL)** and simultaneously indexed in an in-memory **HNSW MemTable**.
- **Rotation**: Once the WAL reaches `HS_WAL_SEGMENT_SIZE_MB`, it is rotated (frozen).
- **Flushing**: A background **Flush Worker** converts the frozen segment into a highly optimized, immutable **HNSW Chunk** (`.hyp`).
- **RAM Reclamation**: After the flush completes, the old MemTable is atomically swapped for a fresh one, freeing up significant memory.

### 2. Immutable Chunks (SSTables)
Data is stored in segmented `.hyp` files, each containing a subset of the collection.
- **Quantization**: Vectors are optionally quantized (e.g., `ScalarI8`), reducing size by 8x or more.
- **MMap**: Hot chunks are searched directly via memory-mapping, leveraging OS page cache.

### 3. S3 Cloud Tiering (hyperspace-tiering)
Cold chunks can be transparently offloaded to **S3-compatible storage**.
- **Local Cache**: A byte-weighted **LRU cache** manages local disk usage (`HS_MAX_LOCAL_CACHE_GB`).
- **Dynamic Fetch**: Chunks not present locally are automatically downloaded on-demand during search.

---

## 🕸 Indexing Layer (hyperspace-index)

### Metric Abstraction & HNSW
We use a Generic Metric system (`Metric<N>`) to support multiple geometries efficiently, dispatched at compile-time via Const Generics.

#### Cognitive Math & Tribunal Router
HyperspaceDB SDK includes a **Cognitive Math** engine built upon the HNSW graph that performs Phase-Locked Loop context tracking, Koopman extrapolations, and calculates LLM hallucination chaos via `local_entropy`. The **Heterogeneous Tribunal Framework** uses the Graph Traversal API to assign a "Geometric Trust Score" to any LLM claim by validating logical paths between ideas.

1.  **Hyperbolic Space (Poincaré Ball)**
    *   **Formula**: $ d(u, v) = \text{acosh}\left(1 + 2 \frac{||u-v||^2}{(1-||u||^2)(1-||v||^2)}\right) $
    *   **Optimization**: We utilize pre-computed normalization factors $\alpha$ and avoid `acosh` during graph traversal.
    *   **Constraint**: Vectors strictly inside unit ball ($||u|| < 1$).

2.  **Euclidean Space (Squared L2)**
    *   **Formula**: $ d(u, v) = \sum (u_i - v_i)^2 $
    *   **Optimization**: We use Squared L2 distance to avoid expensive `sqrt` calls.
    
3.  **Wasserstein-1 (Cross-Feature Matching / 1D CDF)**
    *   **Formula**: $ d(u, v) = \sum |CDF_u(i) - CDF_v(i)| $
    *   **Optimization**: O(N) evaluation instead of O(N^3) Sinkhorn, used for structural distribution matching.

*   **Locking**: The graph uses fine-grained `RwLock` per node layer, allowing concurrent searches and updates.

### Dynamic Configuration
Parameters `ef_search` (search depth) and `ef_construction` (build quality) are stored in `AtomicUsize` global config, allowing runtime tuning without restarts.

---

## ⚡️ Performance Traits

1.  **Async Indexing**: Client receives `OK` as soon as data hits the WAL. Indexing happens in the background.
2.  **Zero-Copy Read**: Search uses `mmap` to read quantized vectors directly from OS cache without heap allocation.
3.  **SIMD Acceleration**: Distance calculations use `std::simd` (Portable SIMD) for 4-8x speedup on supported CPUs (AVX2, Neon).

3.  **SIMD Acceleration**: Distance calculations use `std::simd` (Portable SIMD) for 4-8x speedup on supported CPUs (AVX2, Neon).

---

## 🏙 Multi-Tenancy (Since v2.0)

HyperspaceDB supports SaaS-style multi-tenancy natively.

-   **Namespace Isolation**: Collections are logical entities namespaced by `user_id`.
    -   Format: `{user_id}_{collection_name}`
    -   Example: `cust_123_vectors`, `cust_456_vectors`.
-   **Security**: API Requests require `x-hyperspace-user-id` header (injected by authenticating proxy or middleware).
-   **Resource Accounting**: Disk usage and vector counts are tracked per-user for billing.

## 🔁 Replication & Consistency (Since v2.0)

HyperspaceDB implements a hybrid replication model supporting both high-availability Cloud deployments and dynamic Edge swarms.

### 1. Leader-Follower Replication (WAL Anti-Entropy)
Used for stable cloud deployments. Maintains strict order.
1.  **Leader**: Accepts writes, appends to local WAL, and broadcasts replication stream.
2.  **Follower**: Connects to Leader via gRPC `Replicate()`, requests stream starting from its last persisted `logical_clock`.
3.  **Consistency**:
    -   **Logical Clocks**: Every WAL entry has a monotonic `logical_clock` ID.
    -   **Anti-Entropy**: Followers catch up by replaying missing entries from the Leader's stream.
    -   **Durability**: Followers persist their own WAL and snapshots entirely independently.

### 2. Edge-to-Edge Gossip Swarm
Used for robotics and Local-First AI where nodes are ephemeral and there is no central Leader.
1.  **UDP Heartbeats**: Nodes broadcast their presence and collection metadata summaries (`CollectionSummary`) every 5 seconds.
2.  **Network Discovery**: Nodes listen on `HS_GOSSIP_PORT` and construct a live registry of active peers. Stale peers are evicted after a 30-second TTL.
3.  **Merkle Delta Sync**: Upon discovery, nodes exchange 256-bucket XOR hashes. Only diverging partitions (buckets) are synchronized, making decentralized synchronization extremely bandwidth-efficient.

---

## 🔄 Lifecycle

1.  **Startup**: 
    - Load `index.snap` (Rkyv zero-copy deserialization).
    - Replay `wal.log` for any missing vectors.
2.  **Runtime**:
    - Serve read/write requests.
    - Background worker consumes indexing queue.
    - Snapshotter periodically saves graph state.
3.  **Shutdown**:
    - Stop accepting writes.
    - Drain indexing queue.
    - Save final snapshot.
    - Close file handles.

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0-rc.3] - 2026-03-24

### Added
* **Geometric Search & Spatial Studio (Sprint B / Spatial AI LTS)**:
    * **Advanced Geometric Filters**: Added `InBall`, `InBox`, and `InCone` filters to the core engine and gRPC/REST APIs.
    * **Bitset-Based Pruning**: Implemented high-performance sequential filtering over spatial regions.
    * **Spatial Studio Visuals**: Added Lasso selection and geometric region visualizers (Ball/Box/Cone) to the Poincaré Disk dashboard.
    * **SDK Parity**:
        * **Go**: Added `Search` with geometric filters support and `pb` regeneration.
        * **Python**: Added `filter_ball`, `filter_box`, `filter_cone` helpers to `HyperspaceClient`.
        * **TS**: Updated `search` options with geometric filter types and rebuilt SDK.
        * **C++**: Updated README with gRPC examples for geometric filtering.
    * **Documentation**: Full update of `api.md` and `math.md` with Geometric Search specifications.

### Fixed
* **Test Compatibility**: Fixed incorrect turbofish syntax in `hyperspace-core` unit tests.
* **Clippy compliance**: Resolved redundant `map_or` and documentation formatting warnings.

## [3.0.0-rc.2] - 2026-03-21

### Added
* **Finalized Embedding Pipeline (Sprint 12 / Final Release Candidate)**:
    * **New gRPC Endpoints**: Added `InsertText`, `Vectorize`, and `SearchText` RPCs for native server-side vectorization across all geometries.
    * **Native Model Support**:
        * **Qwen3-Embedding-0.6B**: First-class support for L2 and Cosine geometries (1024d, 32K context).
        * **YAR v5 Embedding**: Recommended models for Poincaré (128d) and Lorentz (129d) geometries.
    * **Advanced Text Handling**:
        * **Chunking & Overlap**: Added `HS_EMBED_<M>_CHUNK_SIZE` and `HS_EMBED_<M>_OVERLAP` to handle long text by vectorizing chunks and performing mean-pooling of resulting embeddings.
        * **HS_EMBED_<M>_HF_FILENAME**: Direct control over which file to load from a HuggingFace repository (e.g., `onnx/model.onnx`).
    * **SDK Parity**:
        * **Python**: Added `insert_text`, `vectorize`, `search_text`, and `search_multi_collection_text`.
        * **Rust**: Integrated `insert_text`, `vectorize`, and `search_text` into high-level `Client`.
        * **TS/Go/CPP/Dart**: Full API alignment for server-side embedding tasks.
    * **Integration Tests**: Added `benchmarks/test_all_embeddings.py` verifying 100% pass rate across L2, Cosine, Poincaré, and Lorentz with Qwen3 and YAR v5.

### Fixed
* **Clippy compliance**: Resolved redundant slicing and useless `as_ref()` warnings in the `hyperspace-embed` crate.
* **Documentation**: Updated all SDK READMEs and the official book with the finalized embedding API.

## [3.0.0-alpha.3] - 2026-03-05

### Added
* **SQ8 Anisotropic Quantization (Sprint 6.2 / 7.1)**:
    * Implemented ScaNN-inspired anisotropic loss function $L = \|e_\parallel\|^2 + t_w \cdot \|e_\perp\|^2$ ($t_w = 10$) in `QuantizedHyperVector::from_float()`.
    * Coordinate-descent refinement (±1 in i8-space) applied to all Cosine/L2/Euclidean collections by default. Lorentz uses `from_float_lorentz()` with dynamic-range scaling.
    * Expected Recall@10 improvement: Cosine **+5.3%**, L2 **+3.8%**, Lorentz **+2.4%** at 8x compression (1 byte/dim).
    * `HS_QUANTIZATION_LEVEL=scalar` (default) now enables Anisotropic SQ8 automatically. No code changes required for existing deployments.
    * `HS_ZONAL_QUANTIZATION=true` enables MOND-style zonal storage (`ZonalVector::Core(i8) / Boundary(f64)`), completely replacing the mmap store for nodes.
* **Per-Geometry Embedding System (Sprint 11.1)**:
    * Each of the four distance geometries (`l2`, `cosine`, `poincare`, `lorentz`) now has an independent, configurable embedding backend.
    * **Local ONNX provider**: Load any ONNX model + tokenizer from disk. Zero network at inference time. Configured via `HS_EMBED_<METRIC>_PROVIDER=local`.
    * **HuggingFace Hub provider**: Auto-downloads ONNX model and tokenizer on first startup, cached at `~/.cache/huggingface`. Configured via `HS_EMBED_<METRIC>_PROVIDER=huggingface` + `HS_EMBED_<METRIC>_HF_MODEL_ID`. Supports private/gated models via `HF_TOKEN`.
    * **Remote API providers**: `openai`, `cohere`, `mistral`, `voyage`, `openrouter`, `generic` (any OpenAI-compatible endpoint). Configured per-geometry via `HS_EMBED_<METRIC>_API_KEY` / `HS_EMBED_<METRIC>_EMBED_MODEL`.
    * **EmbedGeometry normalization**: `cosine`/`l2` → unit-normalize; `poincare` → clamp to unit ball; `lorentz` → pass-through (model enforces hyperboloid constraint).
    * **Configuration priority**: Per-metric vars (`HS_EMBED_<METRIC>_*`) → global fallback (`HYPERSPACE_EMBED_*`) → disabled.
    * **Client-side SDK embedders**: `LocalOnnxEmbedder` and `HuggingFaceEmbedder` available via `hyperspace-sdk` feature flags `local-onnx` / `huggingface`.

### Changed
* **Quantization documentation** (`docs/book/src/quantization.md`): Full rewrite. Mode table now includes SQ8 Anisotropic, Lorentz SQ8, Zonal (MOND). Decision guide updated. CLI `--mode` flags removed (never existed; all config via `HS_QUANTIZATION_LEVEL`).
* **Lorentz quantization documentation** (`docs/book/src/lorentz_quantization.md`): Added "Anisotropic Refinement for Lorentz SQ8" section with loss function, Rust pseudocode, and expected recall table.
* **Embeddings documentation** (`docs/book/src/embeddings.md`): Full rewrite. New: per-geometry architecture diagram, `EmbedGeometry` table, full `.env` example with all 4 geometries, SDK code examples in Rust/Python/TypeScript.

### Fixed
* **Documentation accuracy**: Removed non-existent `--mode binary/none` CLI flags from `quantization.md`. Corrected `HS_ZONAL_QUANTIZATION` env var description (it is a separate flag from `HS_QUANTIZATION_LEVEL`, not a value of it).

## [3.0.0-alpha.2] - 2026-03-03

### Added
* **Multi-Geometry Benchmark & SDK Sync (Sprint 10)**:
    * **Graph Diagnostics in SDK**: Added `gromov.rs` in `hyperspace_sdk` to analyze datasets client-side using Gromov's 4-point condition (delta-hyperbolicity) without loading the core DB. Recommends metric (`lorentz`, `poincare`, `cosine`, or `l2`).
    * **AI Sleep Mode / Memory Reconsolidation**: Added `MemoryReconsolidator` directly in `hyperspace_core` leveraging Riemannian SGD to pull vectors closer using Poincare geometry. Exposed via `TriggerReconsolidation` RPC.
    * **Multi-Geometry Search API**: Added `search_multi_collection` to perform parallel batched top-K queries against L2, Cosine, Poincare, and Lorentz metrics simultaneously.
    * **Wasserstein Metric**: Replaced heavy tensor dependency (`wass`) with a native, ultra-fast $O(N)$ 1D L1-CDF algorithm for Cross-Feature Matching (Wasserstein-1). Exposed via `search_wasserstein` in SDK and `use_wasserstein` flag in Proto.
    * **Dependency Pruning**: Removed heavy `hyperball`, `wass`, `ndarray`, and `skel` libraries from core to ensure Hyperspace DB remains lightweight and ultra-fast. Math operations (SGD, metric logic) replaced with custom inline $O(N)$ implementations.
    * **SDK Generation**: Regenerated protobufs spanning Python, TypeScript, Go, and C++ for synchronizing features (Wasserstein, Reconsolidation RPCs).

## [3.0.0-alpha.1] - 2026-02-23

### Added
* **LSM-Tree Vector Search Architecture (Sprint 1)**:
    * **MemTable & Flush Worker**: Active WAL segments now rotate and flush into immutable `HNSW` chunks. RAM is reclaimed by atomically swapping the hot index (MemTable) after flush.
    * **Global Meta-Router**: IVF-style routing layer that maps search queries to relevant immutable chunks via centroid-based pruning (200x faster than linear scan).
    * **Scatter-Gather Search Pipeline**: Read-path now queries the hot MemTable and multiple cold chunks in parallel using Rayon, merging results by distance.
* **Optional S3 Tiering (`hyperspace-tiering` crate)**:
    * **Cloud-Native Backend**: Cold chunks can now be offloaded to AWS S3, MinIO, or Ceph.
    * **LRU Disk Cache**: Byte-weighted cache (`moka`) manages local storage, automatically evicting cold chunks to S3 when `HS_MAX_LOCAL_CACHE_GB` is reached.
    * **Lazy Loading & Resilient I/O**: Automated S3 download on cache miss with exponential backoff and jitter-aware retries.
    * **Feature Gating**: All cloud dependencies are strictly optional via `s3-tiering` cargo feature, ensuring zero overhead for edge deployments.
* **Tiering Configuration**:
    * Added comprehensive S3 settings: `HS_STORAGE_BACKEND`, `HS_S3_BUCKET`, `HS_S3_REGION`, `HS_S3_ENDPOINT`, `HS_S3_MAX_RETRIES`, `HS_S3_UPLOAD_CONCURRENCY`.
* **Delta Sync Protocol (Task 2.1)**:
    * **Merkle Tree Bucket Sync**: Replaced linear replication with a O(1) lock-free 256-bucket XOR hash state tracker for granular structural diffing.
    * **Two-way gRPC Sync**: Added `SyncHandshake`, `SyncPull`, and `SyncPush` RPCs for efficient bilateral delta transfer (minimizing bandwidth to O(dirty_buckets)).
    * **HTTP Sync APIs**: Exposed `POST /api/collections/{name}/sync/handshake` and `/sync/pull` for WASM and REST clients.
    * **WASM Edge Sync**: Fully integrated synchronization into `hyperspace-wasm` (JS `.get_digest()`, `.apply_sync_vectors()`) with `IndexedDB` persistence for bucket hashes, enabling offline-first Edge-to-Cloud sync.
* **Peer-to-Peer (Edge-to-Edge) Gossip Swarm**:
    * **UDP Heartbeats**: Replaced centralized mesh logic with zero-dependency peer-to-peer UDP broadcasts. Nodes transmit state, role, and logical clocks (`tokio::net::UdpSocket`).
    * **Network Discovery**: `HS_GOSSIP_PEERS` enables dynamic cluster topologies without central coordinators. Stale peers are evicted via configurable `PEER_TTL` logic.
    * **Swarm Topology API**: `GET /api/swarm/peers` added for real-time visualization of the P2P Graph in the Dashboard.
* **Cognitive Math SDK & Heterogeneous Tribunal Framework**:
    * **Math Functions**: Implementations of `local_entropy`, `lyapunov_convergence`, `koopman_extrapolate` and `context_resonance` added to Python, TypeScript, Rust, and C++.
    * **Tribunal Router (`hyperspace.agents`)**: Added `TribunalContext` for evaluating LLM hallucination dynamically via geometric trust scores over the Graph Traversal API.
    * **Robotics Stack (ROS2)**: Initializing C++ and Go SDKs with gRPC pooling and Arena Serialization, alongside a ROS2 package `ros2_hyperspace_node` offering `NavigateToAttractor.srv`.

## [2.2.2] - 2026-02-19

### Added
* **Filtered search brute-force fallback**:
    * Added `HS_FILTER_BRUTEFORCE_THRESHOLD` routing: if filtered candidate bitmap is small, layer-0 performs exact brute-force scan instead of HNSW traversal.
    * Improves latency and recall stability on heavily filtered queries.
* **Hybrid search BM25 upgrade**:
    * Replaced token-overlap lexical scoring with BM25 (`idf`, document length normalization, per-document term frequency).
    * Added global lexical statistics in metadata index: token DF, per-document token length, term frequencies, and aggregate token length.
    * Hybrid lexical branch now respects the same filter constraints as vector search before RRF fusion.
* **GPU roadmap bootstrap in core**:
    * Added WGSL kernels for `L2`, `Cosine`, and `Poincare` batch distance.
    * Added reusable exact re-rank primitive (`rerank_topk_exact`) and CPU reference kernels.
* **GPU runtime dispatch (feature-gated)**:
    * Added `gpu-runtime` feature in `hyperspace-core` (`wgpu`, `pollster`, `bytemuck`).
    * `batch_distance_auto` now executes `L2/Cosine/Poincare/Lorentz` via `wgpu` when enabled, with safe CPU fallback (`GpuFallbackCpu`).
    * Added dedicated Lorentz float runtime kernel and connected `GpuMetric::Lorentz` in `kernel_for_metric`.
    * Added persistent GPU runtime cache (single device/pipeline initialization reused across requests).
    * Added GPU scratch-buffer reuse pool to reduce per-request buffer allocations in batch kernels.
    * Added conservative GPU offload thresholds: `HS_GPU_MIN_BATCH`, `HS_GPU_MIN_DIM`, `HS_GPU_MIN_WORK`.
* **Per-metric GPU controls**:
    * Added `HS_GPU_L2_ENABLED`, `HS_GPU_COSINE_ENABLED`, `HS_GPU_POINCARE_ENABLED`, `HS_GPU_LORENTZ_ENABLED`.
* **Benchmarking**:
    * Added `gpu_dispatch_bench` for CPU-reference vs auto-dispatch comparisons.
* **Batch Search runtime throughput**:
    * `search_batch` server handler now supports bounded per-query fan-out while preserving response order.
    * Added `HS_SEARCH_BATCH_INNER_CONCURRENCY` for deterministic load-scaling control.
* **Search re-rank integration**:
    * Added optional exact re-ranking in server search path via `HS_RERANK_ENABLED`.
    * Added `HS_RERANK_OVERSAMPLE` to control ANN candidate expansion before exact top-K ordering.
* **GPU runtime dispatch contract**:
    * Added `batch_distance_auto` and backend tags in core (`Cpu` / `GpuDispatchPlanned`).
    * Added `HS_GPU_BATCH_ENABLED` configuration toggle for batch kernel dispatch policy.

### Fixed
* **WGSL runtime parser compatibility**:
    * Fixed shader `Params` struct field separators for `wgpu` validation on Apple Silicon runtime path.


## [2.2.1] - 2026-02-17

### Added
* **Vacuum/Rebuild with pruning filter**:
    * `RebuildIndexRequest` now supports optional `filter_query` for metadata-driven forgetting.
    * Supported operators: `lt`, `lte`, `gt`, `gte`, `eq`, `ne`.
* **SDK Hyperbolic Math Utilities**:
    * Added `mobius_add`, `exp_map`, `log_map` in Python SDK.
    * Added `math` module with `mobius_add`, `exp_map`, `log_map` in Rust SDK.
* **Dashboard Graph Explorer activation**:
    * Enabled `/graph` route with working controls for neighbors and concept parents.
* **SDK math expansion**:
    * Added `parallel_transport` and `riemannian_gradient` to Python SDK.
    * Added `parallel_transport` and `riemannian_gradient` to Rust SDK.
    * Added `parallelTransport` and `riemannianGradient` to TypeScript SDK.
    * Added Fréchet mean utilities (`frechet_mean`/`frechetMean`) to Python, Rust, and TypeScript SDKs.
* **CDC SDK coverage**:
    * Added `subscribe_to_events` helpers to Python, TypeScript, and Rust SDKs.
* **Typed numeric filtering upgrade**:
    * Search `Range` filters now evaluate numeric values with `f64` semantics and support typed metadata numeric fields.
    * HTTP filter payloads now support decimal `gte/lte` thresholds.
    * gRPC `Range` extended with backward-compatible `gte_f64` / `lte_f64` fields for decimal thresholds.

### Changed
* **TS SDK upgrade**:
    * Added `rebuildIndex` and `rebuildIndexWithFilter`.
    * Added `HyperbolicMath` helpers in client package.
    * Updated npm package version to `2.2.1`.
* **SDK docs refresh**:
    * Updated TypeScript, Python, and Rust SDK README files for new API surface.
* **Fast 
... [TRUNCATED]
```

### File: COMMERCIAL_LICENSE.md
```md
COMMERCIAL LICENSE AGREEMENT FOR HYPERSPACEDB

This Commercial License Agreement (“Agreement”) is made between:

YARlabs (“Licensor”)  
Email: sglukhota@gmail.com

and the Licensee (“You”).

1. GRANT OF LICENSE
Licensor hereby grants You a non-exclusive, non-transferable, worldwide license to use, reproduce, modify, distribute, and sublicense HyperspaceDB under the terms of this Commercial License.

2. RIGHTS
You may:
a) Use HyperspaceDB in commercial, proprietary software, cloud or SaaS services;
b) Modify the code without obligation to publish the modified source;
c) Distribute modified or unmodified HyperspaceDB to end-customers under your own terms.

3. RESTRICTIONS
You may NOT:
a) Redistribute the original or modified code under any open source license (including AGPL) without separate consent from Licensor;
b) Remove or alter any copyright notices or trademark references;
c) Represent HyperspaceDB as your own product.

4. ATTRIBUTION
You agree to include visible attribution on your website or product documentation:
“Powered by HyperspaceDB (by YARlabs)”.

5. FEES
This License is subject to payment of commercial licensing fees as agreed by Licensor and Licensee.

6. TERM & TERMINATION
This License remains in effect until terminated. Licensor may terminate if You breach this Agreement.

7. WARRANTY DISCLAIMER
Software is provided “AS IS” without warranty of any kind.

8. GOVERNING LAW
This Agreement shall be governed by the laws of the Licensor’s jurisdiction.

Signature: ___________________     Date: ___________
```

### File: CONTRIBUTING.md
```md
# Contributing to HyperspaceDB

By submitting contributions to HyperspaceDB, you agree that
YARlabs may use your contributions under both the AGPLv3 license
and under commercial licenses.

This ensures that improvements contributed by the community
can be included in both open-source and commercial releases.

## 🛠 Development Setup

1.  **Toolchain**: Install Nightly Rust:
    ```bash
    rustup toolchain install nightly
    rustup default nightly
    ```
2.  **Helpers**: We use `just` for task management:
    ```bash
    cargo install just
    ```
3.  **Build**:
    ```bash
    just build
    ```

4.  **Python SDK**:
    ```bash
    cd sdks/python
    python3 -m venv venv
    source venv/bin/activate
    pip install grpcio-tools grpcio protobuf
    ./generate_protos.sh
    ```

5.  **TypeScript SDK**:
    ```bash
    cd sdks/ts
    npm install
    npm run build
    ```

## 🧪 Testing

We value stability. Please ensure all tests pass before submitting a PR:
```bash
cargo check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --lib
```

## 📜 Code Style

We follow standard Rust formatting:
```bash
cargo fmt --all
cargo clippy --all-features -- -D warnings
cargo clippy --tests --workspace -- -W clippy::pedantic
```

## 📐 Adding New Metrics

To implement a new metric:
1.  Implement `Metric<N>` trait in `crates/hyperspace-core/src/lib.rs`.
2.  Implement `distance`, `validate`, and quantized distance methods (`distance_quantized`, `distance_binary`).
3.  Register alias and instantiation logic in `crates/hyperspace-server/src/manager.rs`.
4.  Add unit/integration tests in `crates/hyperspace-core/src/tests.rs` and related crates.

## 🧠 Cognitive SDK Development

If you are contributing to the **Cognitive Math SDK** or the **Heterogeneous Tribunal Framework**:
1. Add core math to `crates/hyperspace-sdk/src/math.rs` in Rust.
2. Mirror the functionality to Python (`sdks/python/hyperspace/math.py`) and TypeScript (`sdks/ts/src/math.ts`).
3. If adding a new multi-agent evaluation metric (e.g. `evaluate_claim` for the Tribunal Router), ensure it leverages the Graph Traversal API efficiently and is added symmetrically across the `agents` module in all SDKs.

## 📊 Adding Quantization Modes

To implement a new quantization mode:
1. Add a variant to `QuantizationMode` enum in `crates/hyperspace-core/src/lib.rs`.
2. Implement encoder in `crates/hyperspace-core/src/vector.rs` (see `QuantizedHyperVector::from_float()` for the SQ8 Anisotropic reference — it uses coordinate-descent refinement with an anisotropic loss $L = \|e_\parallel\|^2 + t_w \cdot \|e_\perp\|^2$).
3. Wire the new variant in `CollectionMetadata::quantization_mode()` in `crates/hyperspace-server/src/manager.rs`.
4. Update `HS_QUANTIZATION_LEVEL` docs in `docs/book/src/quantization.md`.

## 🤖 Adding Embedding Providers

To add a new embedding provider to the built-in service:
1. Implement the `Embedder` trait in `crates/hyperspace-embed/src/lib.rs`.
2. Add a new variant to `EmbedProvider` enum and wire it in `EmbedRouter::from_env()`.
3. Add corresponding `HS_EMBED_<METRIC>_PROVIDER=<name>` documentation to `docs/book/src/embeddings.md`.
4. If the provider requires a new Cargo dependency, gate it behind a feature flag.

## 🚀 Future Roadmap

We focus on building the **Universal Spatial Memory** for AI Agents.

### Phase 1: Ecosystem & Ubiquity (v1.x)
*The goal: Run everywhere RuVector runs, but faster and with better math.*

* **v1.1**: ✅ **Multi-Tenancy (Collections)**. Support for named Collections within a single instance. *Completed.*
* **v1.2**: ✅ **Web Dashboard & Euclidean Support**. Full management UI, L2 Metric support, and Presets. *Completed.*
* **v1.3**: ✅ **Universal TypeScript SDK**. Native bindings for Node.js, Deno, and Bun. *Completed.*
* **v1.4**: ✅ **WASM Core ("Edge Memory")**. Compiling `hyperspace-core` to WebAssembly to run directly in the browser (Local-First AI). Zero latency, zero network calls. *Core implementation ready.*

### Phase 2: Scale & Structure (v2.x)
*The goal: Serverless Economy and Cloud-Native Architecture.*

* **v2.0**: ✅ **Serverless Core**. Idle unloading, cold start, multi-tenancy, and Jemalloc tuning. *Completed.*
* **v2.1**: ✅ **Data-Plane Throughput Upgrade**. Batch search API, Lorentz metric integration, SDK/doc refresh. *Completed.*
* **v2.2**: ✅ **Hyperbolic Graph Traversal API** (planned). Graph-native traversal endpoints and neighborhood/cluster primitives (not fully implemented yet). *Completed.*
* **v2.3**: **Storage Tiering (S3/Blob)**. Automatic backup of idle collections to object storage.


### Phase 3: Collective Intelligence (v3.x)
*The goal: Beyond storage. The "Digital Thalamus" realization.*

* **v3.0-alpha.1**: ✅ **Federated Swarm Protocol & Graph Diagnostics**. Connecting independent HyperspaceDB instances into a decentralized knowledge graph. Allows agents to "share memories" without centralized servers. Also added AI Sleep Mode / Memory Reconsolidation. *Completed.*
* **v3.0-alpha.2**: ✅ **Multi-Geometry Benchmark & SDK Sync**. Graph Diagnostics in SDK, Multi-Geometry Search API, Wasserstein metric (native O(N) 1D), dependency pruning. *Completed.*
* **v3.0-alpha.3**: ✅ **Anisotropic SQ8 & Per-Geometry Embedding System**. ScaNN-inspired coordinate-descent quantization for Cosine/L2 (+5.3% / +3.8% Recall@10). Full embedding service with Local ONNX, HuggingFace Hub, and 6 remote API providers. Documentation overhaul. *Completed.*
* **v3.0-LTS** *(planned)*: **Validation Layer & Batch ONNX Inference**. Strict NaN/Infinity filtering at gRPC ingress. Batch inference pipeline for `InsertBatch`. Gate Check: fuzzy testing with malformed vectors.
* **v3.1**: **Generative Memory**. Optional integration with LLMs to perform "Retrieval-Augmented Generation" directly inside the database query pipeline.

Join us in pushing the boundaries of hyperbolic vector search!

```

### File: DockerHub.md
```md
```markdown
# [H] HyperspaceDB

![Banner](https://img.shields.io/badge/Status-v1.0_Gold-00FFFF?style=for-the-badge)
![License](https://img.shields.io/badge/License-AGPL_v3-blue?style=for-the-badge)
![Size](https://img.shields.io/docker/image-size/yarlabs/hyperspacedb/latest?style=for-the-badge)

**The Spatial Memory for AI.**
HyperspaceDB is a high-performance, hyperbolic vector database written in Rust. It features 1-bit quantization, async replication, and native support for hierarchical datasets (Poincaré ball model).

---

## 🚀 Quick Reference

* **Maintained by:** [YARlabs](https://github.com/yarlabs)
* **Where to get help:** [GitHub Issues](https://github.com/yarlabs/hyperspace-db/issues), [Discord](https://discord.gg/hyperspace-db)
* **Supported architectures:** `linux/amd64`, `linux/arm64` (Apple Silicon compatible)

---

## 🐳 How to use this image

### 1. Start a single instance

To start the database and expose the gRPC port (50051):

```bash
docker run -d \
  --name hyperspace \
  -p 50051:50051 \
  glukhota/hyperspace-db:latest

```

### 2. Persisting Data (Critical)

By default, data is stored inside the container. To prevent data loss when the container is removed, you **must** mount a volume to `/data`.

```bash
docker run -d \
  --name hyperspace \
  -p 50051:50051 \
  -v $(pwd)/hs_data:/data \
  glukhota/hyperspace-db:latest

```

### 3. Using Docker Compose

The easiest way to run HyperspaceDB in production or development.

```yaml
services:
  hyperspace:
    image: glukhota/hyperspace-db:latest
    container_name: hyperspace
    restart: unless-stopped
    ports:
      - "50051:50051"
    volumes:
      - ./data:/data
    environment:
      - RUST_LOG=info
      - HS_PORT=50051

```

---

## ⚙️ Configuration

HyperspaceDB is configured via environment variables passed to the container.

| Variable | Default | Description |
| --- | --- | --- |
| `HS_PORT` | `50051` | The gRPC listening port. |
| `HS_DATA_DIR` | `/data` | Path inside the container for storing segments and WAL. |
| `RUST_LOG` | `info` | Log verbosity (`error`, `warn`, `info`, `debug`, `trace`). |
| `HS_API_KEY` | *(None)* | If set, enables SHA-256 authentication for all requests. |
| `HS_DIMENSION` | `1024` | Vector dimensionality (e.g. 1024, 768, 8). Must match compilation. |
| `HS_DISTANCE_METRIC` | `poincare` | Distance metric (`poincare`, `cosine`, etc). |
| `HS_QUANTIZATION_LEVEL` | `scalar` | Compression level: `none`, `scalar` (i8), `binary` (1-bit). |
| `HS_HNSW_EF_CONSTRUCT` | `100` | HNSW Index construction quality (50-500). |
| `HS_HNSW_EF_SEARCH` | `10` | HNSW Search beam width (10-500). |

---

## 🏷 Image Variants

### `glukhota/hyperspace-db:latest`

This is the defacto image. It contains the latest stable release of the database. Use this for most use cases.

### `glukhota/hyperspace-db:1.0.0`

Specific version tags. Use these in production to ensure immutability and prevent unexpected updates.

---

## 🔒 License

HyperspaceDB is licensed under a dual-license model:

1. **Open Source (AGPLv3):** Free for open source projects.
2. **Commercial:** Required for proprietary/closed-source products.

View full license details on [GitHub](https://github.com/yarlabs/hyperspace-db/blob/main/LICENSE).

```

---
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
