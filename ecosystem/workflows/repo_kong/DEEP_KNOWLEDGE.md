# Deep Matrix Profile: kong

# DEEP_KNOWLEDGE.md

## Kong Framework Analysis: AI-Assisted Binary Reverse Engineering

This report provides a deep architectural analysis of the Kong framework, focusing specifically on the `kong-ml` module. The framework is designed to automate the complex, signal-processing-heavy task of function boundary detection in stripped and obfuscated binaries by leveraging advanced Large Language Model (LLM) orchestration and deep learning techniques.

---

## 🧠 Architectural Overview: The Detection Pipeline

The system follows a highly modular, layered architecture, separating concerns into configuration management, model inference, signal processing, and binary analysis.

The primary workflow for function boundary detection (`XdaDetector::predict`) can be summarized as a four-stage pipeline:

1.  **Region Segmentation:** The input binary data is segmented into `AmbiguousRegion`s (e.g., gaps, optimized code).
2.  **Windowing (Signal Processing):** Each region is broken down into overlapping, fixed-size windows using a sliding window approach.
3.  **Inference (ML):** Each window is tokenized and passed through the pre-trained XDA Transformer model for sequence classification.
4.  **Post-processing (Signal Reconstruction):** Raw, overlapping predictions are merged (confidence averaging) and filtered to reconstruct coherent function boundaries (`FunctionBoundary`).

### Core Components Map

| Module | Responsibility | Key Functionality |
| :--- | :--- | :--- |
| `kong-ml/src/config.rs` | Model Configuration | Defines and serializes BERT-like model hyperparameters (`XdaConfig`). |
| `kong-ml/src/tokenizer.rs` | Data Preprocessing | Converts raw byte streams (`[u8]`) into token IDs (`[u32]`) suitable for Transformer input, handling special tokens (CLS, SEP, PAD). |
| `kong-ml/src/model.rs` | ML Core | Implements the `XdaModel`: a BERT Encoder stack followed by a custom classification head. |
| `kong-ml/src/detector.rs` | Algorithm Engine | Manages the sliding window paradigm, batch inference, and prediction merging/filtering. |
| `kong-ml/src/registry.rs` | System Management | Handles model lifecycle: loading weights (Safetensors), caching, and selecting the correct model for a given architecture (`Arch`). |
| `kong/*` | Orchestration/I/O | Manages LLM API interaction, CLI setup, and persistent configuration storage (SQLite). |

---

## 🔬 Deep Dive 1: The Machine Learning Pipeline (XDA Model)

The core intelligence resides in the `XdaModel`, which is a specialized adaptation of the BERT architecture for binary sequence classification.

### 1. Model Structure (`XdaModel`)

The model is composed of two main parts:

*   **Encoder:** A standard `BertModel` (Transformer Encoder). This component processes the input sequence of byte tokens, generating rich, contextualized embeddings for every input position.
*   **Classifier Head:** A custom, two-layer feed-forward network (`ClassifierHead`). This head takes the final hidden state vector from the encoder and maps it to the probability distribution over the defined labels (`num_labels`: 3).

### 2. Input Representation and Tokenization

The `ByteTokenizer` is critical for translating raw binary data into the format required by the Transformer:

*   **Input:** A slice of bytes (`&[u8]`).
*   **Encoding:** The process prepends a `[CLS]` token ID, appends a `[SEP]` token ID, and maps every byte value directly to a unique token ID.
*   **Padding/Masking:** The `encode` method handles sequence length constraints (`max_length`), padding the sequence with `[PAD]` tokens and generating a corresponding `attention_mask` to inform the model which tokens should be ignored during attention calculation.

### 3. Inference Mechanism

The `XdaModel::forward` method executes the inference:

$$
\text{Output} = \text{Classifier}(\text{BERT}(\text{Input IDs}, \text{Attention Mask}))
$$

The output is a tensor of logits, where each position corresponds to a probability distribution over the three labels:
1.  `non-func` (Background)
2.  `func_start` (Function Prologue)
3.  `func_body` (Function Body)

---

## ⚙️ Deep Dive 2: Binary Signal Processing and Detection

The `XdaDetector` implements the complex signal processing required to transform sparse, overlapping ML predictions into continuous, meaningful function boundaries.

### 1. The Sliding Window Paradigm (`create_windows`)

Since function characteristics are local and continuous, the detector cannot process the entire region at once. It employs a **Sliding Window** technique:

*   **Window Size:** Fixed at 512 bytes (`window_size`).
*   **Stride:** Fixed at 256 bytes (`stride`).
*   **Mechanism:** The input byte array is sampled repeatedly, starting at `offset` and advancing by `stride`. This ensures that the analysis overlaps significantly, allowing the model to capture context that spans across the window boundaries.
*   **Padding Handling:** The implementation explicitly handles the end-of-region scenario, padding the final window with null bytes (`0`) if its length is less than `window_size`, ensuring the model receives a consistent input shape.

### 2. Batch Inference (`run_batch`)

The detector processes all generated windows in a single batch call to the `XdaModel`. This is a crucial optimization, leveraging GPU parallelism (via `candle_core::Tensor`) to minimize I/O and maximize throughput.

### 3. Prediction Merging and Boundary Extraction (The Core Algorithm)

This is the most sophisticated step, converting discrete window predictions into continuous boundaries:

*   **Prediction Structure:** Each window yields a sequence of labels and confidence scores.
*   **Merging (`merge_predictions`):** Because windows overlap, the same byte address may be predicted multiple times. The detector resolves this redundancy by **averaging the confidence scores** for overlapping addresses. This stabilizes the prediction and reduces noise.
*   **Boundary Extraction (`extract_boundaries`):** The merged confidence scores are analyzed sequentially. A function boundary is defined by a sustained sequence of high-confidence labels (e.g., a transition from `non-func` $\rightarrow$ `func_start` $\rightarrow$ `func_body` $\rightarrow$ `non-func`). The detector uses these transitions and the `confidence_threshold` to define the final `FunctionBoundary` objects, providing robust start and end addresses.

---

## 🏛️ Deep Dive 3: System Infrastructure and Modularity

### 1. Model Registry (`ModelRegistry`)

The `ModelRegistry` acts as the system's state manager and factory pattern implementation.

*   **Caching:** It enforces persistence by mapping architectures (`Arch`) to specific cache paths (`weights_path`, `config_path`). This prevents redundant downloading and initialization.
*   **Loading:** The `load_detector` method encapsulates the entire initialization sequence:
    1.  Check existence (`has_model`).
    2.  Load configuration (`XdaConfig::from_json`).
    3.  Load weights using `VarBuilder::from_mmaped_safetensors` (efficient memory mapping).
    4.  Instantiate `XdaModel` and subsequently `XdaDetector`.

### 2. Configuration and Environment Management

*   **`kong-types`:** Defines the canonical data structures (`AmbiguousRegion`, `FunctionBoundary`, `Arch`), ensuring type safety across the entire pipeline.
*   **`kong-ml/src/config.rs`:** Provides a clean interface for managing the ML model's hyperparameters, decoupling the model definition from the runtime logic.
*   **`kong/db.py`:** Implements a simple SQLite persistence layer for global framework settings (e.g., default LLM provider, setup status), demonstrating robust state management for a CLI tool.

---

## 🚀 Summary of Key Technical Patterns

1.  **Transformer-Based Sequence Classification:** Utilizing BERT for contextual feature extraction on raw binary data.
2.  **Sliding Window Signal Processing:** Applying a fixed-stride, fixed-window approach to analyze continuous, high-dimensional data streams (binary code).
3.  **Averaging Consensus Filtering:** Implementing a confidence-based merging strategy to resolve prediction conflicts arising from window overlap, significantly improving prediction stability.
4.  **Factory/Registry Pattern:** Using `ModelRegistry` to manage the complex, multi-step initialization and loading of architecture-specific ML models.
5.  **Modular Separation of Concerns:** Strict separation between configuration, tokenization, model definition, and algorithmic execution ensures maintainability and scalability.