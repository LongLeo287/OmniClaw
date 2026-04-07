---
id: pathway
type: knowledge
owner: OA_Triage
---
# pathway
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  <a href="https://pathway.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://pathway.com/logo-light.svg">
      <img src="https://pathway.com/logo-dark.svg">
    </picture>
  </a>
  <br /><br />
  <a href="https://trendshift.io/repositories/10388" target="_blank"><img src="https://trendshift.io/api/badge/repositories/10388" alt="pathwaycom%2Fpathway | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
  <br /><br />
</div>
<p align="center">
        <a href="https://github.com/pathwaycom/pathway/actions/workflows/ubuntu_test.yml">
        <img src="https://github.com/pathwaycom/pathway/actions/workflows/ubuntu_test.yml/badge.svg" alt="ubuntu"/>
        <br>
        <a href="https://github.com/pathwaycom/pathway/actions/workflows/release.yml">
        <img src="https://github.com/pathwaycom/pathway/actions/workflows/release.yml/badge.svg" alt="Last release"/></a>
        <a href="https://badge.fury.io/py/pathway"><img src="https://badge.fury.io/py/pathway.svg" alt="PyPI version" height="18"></a>
        <a href="https://badge.fury.io/py/pathway"><img src="https://static.pepy.tech/badge/pathway" alt="PyPI downloads" height="18"></a>
        <a href="https://github.com/pathwaycom/pathway/blob/main/LICENSE.txt">
        <img src="https://img.shields.io/badge/license-BSL-green" alt="License: BSL"/></a>
      <br>
        <a href="https://discord.gg/pathway">
        <img src="https://img.shields.io/discord/1042405378304004156?logo=discord"
            alt="chat on Discord"></a>
        <a href="https://twitter.com/intent/follow?screen_name=pathway_com">
        <img src="https://img.shields.io/twitter/follow/pathwaycom"
            alt="follow on Twitter"></a>
        <a href="https://linkedin.com/company/pathway">
        <img src="https://img.shields.io/badge/pathway-0077B5?style=social&logo=linkedin" alt="follow on LinkedIn"></a>
      <a href="https://github.com/dylanhogg/awesome-python/blob/main/README.md">
      <img src="https://awesome.re/badge.svg" alt="Awesome Python"></a>
      <a href="https://gurubase.io/g/pathway">
      <img src="https://img.shields.io/badge/Gurubase-Ask%20Pathway%20Guru-006BFF" alt="Pathway Guru"></a>
    <br>
    <a href="#getting-started">Getting Started</a> |
    <a href="#deployment">Deployment</a> |
    <a href="#resources">Documentation and Support</a> |
    <a href="https://pathway.com/blog/">Blog</a> |
    <a href="#license">License</a>

  
</p>

# Pathway<a id="pathway"> Live Data Framework</a>

[Pathway](https://pathway.com) is a Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

Pathway comes with an **easy-to-use Python API**, allowing you to seamlessly integrate your favorite Python ML libraries.
Pathway code is versatile and robust: **you can use it in both development and production environments, handling both batch and streaming data effectively**.
The same code can be used for local development, CI/CD tests, running batch jobs, handling stream replays, and processing data streams.

Pathway is powered by a **scalable Rust engine** based on Differential Dataflow and performs incremental computation.
Your Pathway code, despite being written in Python, is run by the Rust engine, enabling multithreading, multiprocessing, and distributed computations.
All the pipeline is kept in memory and can be easily deployed with **Docker and Kubernetes**.

You can install Pathway with pip:
```
pip install -U pathway
```

For any questions, you will find the community and team behind the project [on Discord](https://discord.com/invite/pathway).

## Use-cases and templates

Ready to see what Pathway can do?

[Try one of our easy-to-run examples](https://pathway.com/developers/templates)!

Available in both notebook and docker formats, these ready-to-launch examples can be launched in just a few clicks. Pick one and start your hands-on experience with Pathway today!

### Event processing and real-time analytics pipelines
With its unified engine for batch and streaming and its full Python compatibility, Pathway makes data processing as easy as possible. It's the ideal solution for a wide range of data processing pipelines, including:

- [Showcase: Real-time ETL.](https://pathway.com/developers/templates/kafka-etl)
- [Showcase: Event-driven pipelines with alerting.](https://pathway.com/developers/templates/realtime-log-monitoring)
- [Showcase: Realtime analytics.](https://pathway.com/developers/templates/linear_regression_with_kafka)
- [Docs: Switch from batch to streaming.](https://pathway.com/developers/user-guide/connecting-to-data/switch-from-batch-to-streaming)



### AI Pipelines

Pathway provides dedicated LLM tooling to build live LLM and RAG pipelines. Wrappers for most common LLM services and utilities are included, making working with LLMs and RAGs pipelines incredibly easy. Check out our [LLM xpack documentation](https://pathway.com/developers/user-guide/llm-xpack/overview).

Don't hesitate to try one of our runnable examples featuring LLM tooling.
You can find such examples [here](https://pathway.com/developers/user-guide/llm-xpack/llm-examples).

  - [Template: Unstructured data to SQL on-the-fly.](https://pathway.com/developers/templates/unstructured-to-structured)
  - [Template: Private RAG with Ollama and Mistral AI](https://pathway.com/developers/templates/private-rag-ollama-mistral)
  - [Template: Adaptive RAG](https://pathway.com/developers/templates/adaptive-rag)
  - [Template: Multimodal RAG with gpt-4o](https://pathway.com/developers/templates/multimodal-rag)

## Features

- **A wide range of connectors**: Pathway comes with connectors that connect to external data sources such as Kafka, GDrive, PostgreSQL, or SharePoint. Its Airbyte connector allows you to connect to more than 300 different data sources. If the connector you want is not available, you can build your own custom connector using Pathway Python connector.
- **Stateless and stateful transformations**: Pathway supports stateful transformations such as joins, windowing, and sorting. It provides many transformations directly implemented in Rust. In addition to the provided transformation, you can use any Python function. You can implement your own or you can use any Python library to process your data.
- **Persistence**: Pathway provides persistence to save the state of the computation. This allows you to restart your pipeline after an update or a crash. Your pipelines are in good hands with Pathway!
- **Consistency**: Pathway handles the time for you, making sure all your computations are consistent. In particular, Pathway manages late and out-of-order points by updating its results whenever new (or late, in this case) data points come into the system. The free version of Pathway gives the "at least once" consistency while the enterprise version provides the "exactly once" consistency.
- **Scalable Rust engine**: with Pathway Rust engine, you are free from the usual limits imposed by Python. You can easily do multithreading, multiprocessing, and distributed computations.
- **LLM helpers**: Pathway provides an LLM extension with all the utilities to integrate LLMs with your data pipelines (LLM wrappers, parsers, embedders, splitters), including an in-memory real-time Vector Index, and integrations with LLamaIndex and LangChain. You can quickly build and deploy RAG applications with your live documents.


## Getting started<a id="getting-started"></a>

### Installation<a id="installation"></a>

Pathway requires Python 3.10 or above.

You can install the current release of Pathway using `pip`:

```
$ pip install -U pathway
```

⚠️ Pathway is available on MacOS and Linux. Users of other systems should run Pathway on a Virtual Machine.


### Example: computing the sum of positive values in real time.<a id="example"></a>

```python
import pathway as pw

# Define the schema of your data (Optional)
class InputSchema(pw.Schema):
  value: int

# Connect to your data using connectors
input_table = pw.io.csv.read(
  "./input/",
  schema=InputSchema
)

#Define your operations on the data
filtered_table = input_table.filter(input_table.value>=0)
result_table = filtered_table.reduce(
  sum_value = pw.reducers.sum(filtered_table.value)
)

# Load your results to external systems
pw.io.jsonlines.write(result_table, "output.jsonl")

# Run the computation
pw.run()
```

Run Pathway [in Google Colab](https://colab.research.google.com/drive/1aBIJ2HCng-YEUOMrr0qtj0NeZMEyRz55?usp=sharing).

You can find more examples [here](https://github.com/pathwaycom/pathway/tree/main/examples).


## Deployment<a id="deployment"></a>

### Locally<a id="running-pathway-locally"></a>

To use Pathway, you only need to import it:

```python
import pathway as pw
```

Now, you can easily create your processing pipeline, and let Pathway handle the updates. Once your pipeline is created, you can launch the computation on streaming data with a one-line command:

```python
pw.run()
```

You can then run your Pathway project (say, `main.py`) just like a normal Python script: `$ python main.py`.
Pathway comes with a monitoring dashboard that allows you to keep track of the number of messages sent by each connector and the latency of the system. The dashboard also includes log messages. 

<img src="https://d14l3brkh44201.cloudfront.net/pathway-dashboard.png" width="1326" alt="Pathway dashboard"/>

Alternatively, you can use the pathway'ish version:

```
$ pathway spawn python main.py
```

Pathway natively supports multithreading.
To launch your application with 3 threads, you can do as follows:
```
$ pathway spawn --threads 3 python main.py
```

To jumpstart a Pathway project, you can use our [cookiecutter template](https://github.com/pathwaycom/cookiecutter-pathway).


### Docker<a id="docker"></a>

You can easily run Pathway using docker.

#### Pathway image

You can use the [Pathway docker image](https://hub.docker.com/r/pathwaycom/pathway), using a Dockerfile:

```dockerfile
FROM pathwaycom/pathway:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-script.py" ]
```

You can then build and run the Docker image:

```console
docker build -t my-pathway-app .
docker run -it --rm --name my-pathway-app my-pathway-app
```

#### Run a single Python script

When dealing with single-file projects, creating a full-fledged `Dockerfile`
might seem unnecessary. In such scenarios, you can execute a
Python script directly using the Pathway Docker image. For example:

```console
docker run -it --rm --name my-pathway-app -v "$PWD":/app pathwaycom/pathway:latest python my-pathway-app.py
```

#### Python docker image

You can also use a standard Python image and install Pathway using pip with a Dockerfile:

```dockerfile
FROM --platform=linux/x86_64 python:3.10

RUN pip install -U pathway
COPY ./pathway-script.py pathway-script.py

CMD ["python", "-u", "pathway-script.py"]
```

### Kubernetes and cloud<a id="k8s"></a>

Docker containers are ideally suited for deployment on the cloud with Kubernetes.
If you want to scale your Pathway application, you may be interested in our Pathway for Enterprise.
Pathway for Enterprise is specially tailored towards end-to-end data processing and real time intelligent analytics.
It scales using distributed computing on the cloud and supports distributed Kubernetes deployment, with external persistence setup.

You can easily deploy Pathway using services like Render: see [how to deploy Pathway in a few clicks](https://pathway.com/developers/user-guide/deployment/render-deploy/).

If you are interested, don't hesitate to [contact us](mailto:contact@pathway.com) to learn more.

## Performance<a id="performance"></a>

Pathway is made to outperform state-of-the-art technologies designed for streaming and batch data processing tasks, including: Flink, Spark, and Kafka Streaming. It also makes it possible to implement a lot of algorithms/UDF's in streaming mode which are not readily supported by other streaming frameworks (especially: temporal joins, iterative graph algorithms, machine learning routines).

If you are curious, here are [some benchmarks to play with](https://github.com/pathwaycom/pathway-benchmarks).

<img src="https://github.com/pathwaycom/pathway-benchmarks/raw/main/images/bm-wordcount-lineplot.png" width="1326" alt="WordCount Graph"/>

## Documentation and Support<a id="resources"></a>

The entire documentation of Pathway is available at [pathway.com/developers/](https://pathway.com/developers/user-guide/introduction/welcome), including the [API Docs](https://pathway.com/developers/api-docs/pathway).

If you have any question, don't hesitate to [open an issue on GitHub](https://github.com/pathwaycom/pathway/issues), join us on [Discord](https://discord.com/invite/pathway), or send us an email at [contact@pathway.com](mailto:contact@pathway.com).



## 🤝 Featured Collaborations & Integrations

We build cutting-edge data processing pipelines and co-promote solutions that push the boundaries of what's possible with Python and streaming data.
Meet the people helping us shape the future of data engineering.

<div align="center">

| Project | Description |
| ------------ | ----------- |
| [Databento](https://databento.com/blog/option-greeks) | A simpler, faster way to get market data. |
| [LangChain](https://docs.langchain.com/oss/python/integrations/vectorstores/pathway) | LangChain is the platform for agent engineering. |
| [LlamaIndex](https://developers.llamaindex.ai/python/examples/retrievers/pathway_retriever/) | The developer-trusted framework for building context-aware AI agents. |
| [MinIO](https://www.min.io/) | MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | PaddleOCR is an industry-leading, production-ready OCR and document AI engine, offering end-to-end solutions from text extraction to intelligent document understanding. |
| [Redpanda](https://www.redpanda.com/blog/replace-kafka-redpanda-data-analysis-streaming) | Build, operate, and govern streaming and AI applications without the complexity of Kafka. |
</div>


## License<a id="license"></a>

Pathway is distributed on a [BSL 1.1 License](https://github.com/pathwaycom/pathway/blob/main/LICENSE.txt) which allows for unlimited non-commercial use, as well as use of the Pathway package [for most commercial purposes](https://pathway.com/license/), free of charge. Code in this repository automatically converts to Open Source (Apache 2.0 License) after 4 years. Some [public repos](https://github.com/pathwaycom) which are complementary to this one (examples, libraries, connectors, etc.) are licensed as Open Source, under the MIT license.


## Contribution guidelines<a id="contribution-guidelines"></a>

If you develop a library or connector which you would like to integ
... [TRUNCATED]
```

### File: examples\README.md
```md
# Pathway examples

This repository contains examples of data processing using [Pathway](https://pathway.com/developers/documentation/introduction/welcome), the Python-based programming framework for easy building of realtime and reactive data products.

For a quick start, here is a handpicked selection of examples that illustrate how Pathway can be used in your streaming projects:
- Working with live data streams in Jupyter (short version [GitHub](https://github.com/pathwaycom/pathway/blob/main/examples/notebooks/showcases/live-data-jupyter.ipynb) and [Colab](https://colab.research.google.com/github/pathwaycom/pathway/blob/main/examples/notebooks/showcases/live-data-jupyter.ipynb) | [long version GitHub](https://github.com/pathwaycom/pathway/tree/main/examples/projects/from_jupyter_to_deploy)).
- Realtime Server Log Monitoring with Pathway ([Filebeat+Slack version](https://github.com/pathwaycom/pathway/tree/main/examples/projects/realtime-log-monitoring/filebeat-pathway-slack) | [Logstash+Elastick version](https://github.com/pathwaycom/pathway/tree/main/examples/projects/realtime-log-monitoring/logstash-pathway-elastic)).
- Always up-to-date data indexing pipeline ([GitHub](https://github.com/pathwaycom/pathway/blob/main/examples/notebooks/showcases/live_vector_indexing_pipeline.ipynb) | [Colab](https://colab.research.google.com/github/pathwaycom/pathway/blob/main/examples/notebooks/showcases/live_vector_indexing_pipeline.ipynb)).
- Detecting suspicious user activity with Tumbling Window group-by ([GitHub](https://github.com/pathwaycom/pathway/blob/main/examples/notebooks/tutorials/suspicious_user_activity.ipynb) | [Colab](https://colab.research.google.com/github/pathwaycom/pathway/blob/main/examples/notebooks/tutorials/suspicious_user_activity.ipynb)).
- Build an LLM App with Pathway ([GitHub](https://github.com/pathwaycom/llm-app/tree/main)).
- Realtime Twitter Analysis App with Pathway ([GitHub](https://github.com/pathwaycom/pathway/tree/main/examples/projects/twitter)).
- Upsampling your Signal Processing Data: transforming multiple data streams ([GitHub](https://github.com/pathwaycom/pathway/blob/main/examples/notebooks/tutorials/upsampling.ipynb) | [Colab](https://colab.research.google.com/github/pathwaycom/pathway/blob/main/examples/notebooks/tutorials/upsampling.ipynb)).
- Computing PageRank ([GitHub](https://github.com/pathwaycom/pathway/blob/main/examples/notebooks/tutorials/pagerank.ipynb) | [Colab](https://colab.research.google.com/github/pathwaycom/pathway/blob/main/examples/notebooks/tutorials/pagerank.ipynb)).

Don't hesitate to look for help on [our website](pathway.com/developers/user-guide/development/get-help/) or directly on the [main repo of the Pathway package](https://github.com/pathwaycom/pathway).

```

### File: examples\projects\monitoring\README.md
```md
# Pathway Monitoring using OpenTelemetry Collector and Grafana Cloud

This example contains the necessary configuration files to set up an OpenTelemetry Collector instance using Docker Compose. It also includes an Grafana dashboard JSON file for visualizing the collected monitoring data.

## Contents

- [config.yaml](./config.yaml): OpenTelemetry Collector configuration file.
- [docker-compose.yaml](./docker-compose.yaml): Docker Compose file to set up the OpenTelemetry Collector.
- [grafana-dashboard.json](./grafana-dashboard.json): Example Grafana dashboard JSON file to import.
- [monitoring_demo.py](./monitoring_demo.py): Example Pathway pipeline to test monitoring.

## Getting Started

### Prerequisites

Ensure you have Docker and Docker Compose installed on your machine. For installation instructions, visit the [Docker website](https://www.docker.com/get-started/).

To send data to Grafana Cloud, you will need a free Grafana account. You can create one by visiting [Grafana Cloud](https://grafana.com/).

Make sure Pathway is installed in version 0.11.2 or higher:

```python
pip install -U pathway
```

### Configuration

Before starting the OpenTelemetry Collector, fill in the Loki, Prometheus, and Tempo credentials in the `docker-compose.yaml` file.

Credentials can be obtained by logging into [Grafana](https://grafana.com/). You will be redirected to the **My Account** page, where you can manage your tokens for specific Grafana services.

### Running the OpenTelemetry Collector

To start the OpenTelemetry Collector instance, run the following command:

```sh
OTLP_GRPC_PORT=<OTLP_GRPC_PORT> docker-compose up
```

If you wish to use the default port (4317), you can omit the OTLP_GRPC_PORT environment variable.

### Running pathway

Once the OpenTelemetry Collector instance is running, you can start your Pathway pipeline.

```python
import pathway as pw

pw.set_license_key(key="YOUR-KEY")
pw.set_monitoring_config(server_endpoint="http://localhost:<OTLP_GRPC_PORT>")

# your pipeline here...

pw.run()
```

You can also adjust the license key and monitoring endpoint in the [example script](./monitoring_demo.py) and run it with:

```bash
python monitoring_demo.py
```


## Grafana Dashboard

To visualize the collected telemetry data, you can import the provided Grafana dashboard JSON file. Follow these steps:

1. Open Grafana Cloud in your web browser.
2. Navigate to the Dashboards section.
3. Click on Import.
4. Upload the grafana-dashboard.json file.
5. Click Import to load the example dashboard.

Once you add the dashboard and run the script, you'll be able to see the first set of data on resource usage.
<img src="assets/monitoring_graph.png" alt="Explore trace graph" class="mx-auto" width="auto" height="auto"/>

```

### File: build.rs
```rs
// Copyright © 2026 Pathway

fn main() {
    println!("cargo:rerun-if-changed=build.rs");

    pyo3_build_config::add_extension_module_link_args();
}

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [Unreleased]

## [0.30.0] - 2026-03-24

### Added
- `pw.io.mongodb.read` connector, which reads data from a MongoDB collection. The connector first delivers a full snapshot of the collection and then, if the streaming mode is used, subscribes to the change stream to receive incremental updates in real time.
- `pw.io.postgres.read` connector, which reads data from a PostgreSQL table directly by parsing the Write-Ahead Log (WAL).
- `pw.io.postgres.write` and `pw.io.postgres.read` now support serialization/deserialization of `np.ndarray` (`int`/`float` elements), homogeneous `tuple` and `list` (via Postgres `ARRAY`; multidimensional rectangular arrays supported).
- `pw.io.airbyte.read` now accepts a `dependency_overrides` parameter, allowing users to pin specific versions of transitive dependencies (e.g. `airbyte-cdk`) installed into the connector's virtual environment. This unblocks connectors broken by upstream dependency changes without waiting for upstream fixes.

### Changed
- **BREAKING**: `pw.io.mongodb.write` and `pw.io.mongodb.read` now serialize and deserialize `np.ndarray` columns as nested BSON arrays that preserve the array's shape. Previously, all ndarrays were flattened to a single BSON array regardless of dimensionality, making it impossible to reconstruct the original shape on read-back. For 1-D arrays the representation is identical to before (`[1, 2, 3]`); only multi-dimensional arrays are affected.
- **BREAKING**: The dependencies for `pw.io.pyfilesystem.read` are no longer included in the default package installation. To install them, please use `pip install pathway[pyfilesystem]`.
- Asynchronous callback for `pw.io.python.write` is now available as `pw.io.OnChangeCallbackAsync`.
- `pw.run` and `pw.run_all` now have the `event_loop` parameter to support reusing async state across multiple graph runs.

### Fixed
- `pathway web-dashboard` now waits for the metrics database to be created instead of terminating instantly.

## [0.29.1] - 2026-02-16

### Added
- `pw.io.kafka.read` and `pw.io.kafka.write` connectors now support OAUTHBEARER authentication.
- `pw.io.mongodb.write` connector now supports an `output_table_type` parameter with two modes: `stream_of_changes` (default) and `snapshot`. In `snapshot` mode, the connector maintains the current state of the Pathway table in MongoDB using the `_id` field as the primary key, while `stream_of_changes` preserves the existing behavior by writing all events with `time` and `diff` flags to reflect transactional minibatches and the nature of each change.
- Workers can now automatically scale up or down based on pipeline load, using a configurable monitoring window. This feature requires persistence to be enabled and can be configured via `worker_scaling_enabled` and `workload_tracking_window_ms` in `pw.persistence.Config`. Please refer to the tutorial for more details.
- `pw.io.postgres.write` now properly supports TLS configuration via `sslmode` and `sslrootcert` connection string parameters.

### Changed
- `pw.xpacks.connectors.read` now retries initial connection requests.

## [0.29.0] - 2026-01-22

### Added
- Pathway Web Dashboard providing user-friendly interface for monitoring Pathway pipelines in real time with interactive graph plotting and latency/memory metrics.
- `pw.io.kafka.read` now includes message headers in the parsed metadata. The headers are available at the top level of the metadata in the `headers` array. Each element of the array is a pair consisting of a string header name and a base64-encoded header value. If the header is null, the corresponding value is also null.
- `pw.xpacks.llm.llms.BedrockChat` - Native AWS Bedrock chat integration using the Converse API. Supports Claude, Llama, Titan, Mistral, and other Bedrock models.
- `pw.xpacks.llm.embedders.BedrockEmbedder` - Native AWS Bedrock embedding integration supporting Amazon Titan and Cohere embedding models.

### Changed
- Most Python dependencies are now imported only if the related capabilities are used by a program.
- **BREAKING**: Output connectors no longer wrap string header values in double quotes when sending them to Kafka or NATS. The string values are forwarded as-is. The `None` value is handled differently: in Kafka, it is serialized as a header without a value, while in NATS it becomes the string `"None"`.

## [0.28.0] - 2026-01-08

### Added
- `pw.io.kafka.read` and `pw.io.redpanda.read` now allow each schema field to be specified as coming from either the message key or the message value.
- Connector groups now support the specification of an idle duration. When this is set, if a source does not provide any data for the specified period of time, it will be excluded from the group until it produces data again.
- It is now possible to assign priorities to sources within a connector group. When a priority is set, it ensures that at any moment, the source is not lagging behind any other source with a higher priority in terms of the tracked column.
- Connector groups can now be used in the multiprocess runs.

### Changed
- **BREAKING**: The `__str__` and `dumps` methods in `pw.Json` no longer enforce the result to be an ASCII string. This way, the behavior of `pw.debug.compute_and_print` is now consistent with other output connectors.
- The window functions now internally use deterministic UDFs, where possible.
- The detection logic for the append-only Python connectors has been improved, syntactic analysis has been put in place.

## [0.27.1] - 2025-12-08

### Added
- `pw.Table.filter_out_results_of_forgetting` method, allowing to revert the effects of forgetting at a later stage.

### Changed
- The MCP server `tool` method now allows to pass an optional `description`, default value ​​being kept as the handler's docstring.
- `pw.io.kafka.read` and `pw.io.redpanda.read` now create a `key` column storing the contents of the message keys.

## [0.27.0] - 2025-11-13

### Added
- JetStream extension is now supported in both NATS read and write connectors.
- The Iceberg connectors now support Glue as a catalog backend.
- New `Table.add_update_timestamp_utc` function for tracking update time of rows in the table

### Changed
- **BREAKING** The API for the Iceberg connectors has changed. The `catalog` parameter is now required in both `pw.io.iceberg.read` and `pw.io.iceberg.write`. This parameter can be either of type `pw.io.iceberg.RestCatalog` or `pw.io.iceberg.GlueCatalog`, and it must contain the connection parameters.
- **BREAKING** `paddlepaddle` is no longer a dependency of the Pathway package. The reason is that choosing a specific version for the hardware it will be run on is advantageous from the performance point of view. To install `paddlepaddle` follow instructions on https://www.paddlepaddle.org.cn/en/install/quick.
- `pw.xpacks.llm.question_answering.BaseRAGQuestionAnswerer` now supports document reranking. This enables two-stage retrieval where initial vector similarity search is followed by reranking to improve document relevance ordering.

### Fixed
- Endpoints created by `pw.io.http.rest_connector` now accept requests both with and without a trailing slash. For example, `/endpoint/` and `/endpoint` are now treated equivalently.
- Schemas that inherit from other schemas now automatically preserve all properties from their parent schemas.
- Fixed an issue where the persistence configuration failed when provided with a relative filesystem path.
- Fixed unique name autogeneration for the Python connectors.

## [0.26.4] - 2025-10-16

### Added
- New external integration with [Qdrant](https://qdrant.tech/).
- `pw.io.mysql.write` method for writing to MySQL. It supports two output table types: stream of changes and a realtime-updated data snapshot.

### Changed
- `pw.io.deltalake.read` now accepts the `start_from_timestamp_ms` parameter for non-append-only tables. In this case, the connector will replay the history of changes in the table version by version starting from the state of the table at the given timestamp. The differences between versions will be applied atomically.
- Asynchronous UDFs for connecting to API based llm and embedding models now have by default retry strategy set to `pw.udfs.ExponentialRetryStrategy()`
- `pw.io.postgres.write` method now supports two output table types: stream of changes and realtime-updated data snapshot. The output table type can be chosen with the `output_table_type` parameter.
- `pw.io.postgres.write_snapshot` method has been deprecated.

## [0.26.3] - 2025-10-03

### Added
- New parser `pathway.xpacks.llm.parsers.PaddleOCRParser` supporting parsing of PDF, PPTX and images.

## [0.26.2] - 2025-10-01

### Added
- `pw.io.gdrive.read` now supports the `"only_metadata"` format. When this format is used, the table will contain only metadata updates for the tracked directory, without reading object contents.
- Detailed metrics can now be exported to SQLite. Enable this feature using the environment variable `PATHWAY_DETAILED_METRICS_DIR` or via `pw.set_monitoring_config()`.
- `pw.io.kinesis.read` and `pw.io.kinesis.write` methods for reading from and writing to AWS Kinesis.

### Fixed
- A bug leading to potentially unbounded memory consumption that could occur in `Table.forget` and `Table.sort` operators during multi-worker runs has been fixed.
- Improved memory efficiency during cold starts by compacting intermediary structures and reducing retained memory after backfilling.

### Changed
- The frequency of background operator snapshot compression in data persistence is limited to the greater of the user-defined `snapshot_interval` or 30 minutes when S3 or Azure is used as the backend, in order to avoid frequent calls to potentially expensive operations.
- The Google Drive input connector performance has been improved, especially when handling directories with many nested subdirectories.
- The MCP server `tool` method now allows to pass the optional data `title`, `output_schema`, `annotations` and `meta` to inform the LLM client.
- Relaxed boto3 dependency to <2.0.0.

## [0.26.1] - 2025-08-28

### Added
- `pw.Table.forget` to remove old (in terms of event time) entries from the pipeline.
- `pw.Table.buffer`, a stateful buffering operator that delays entries until `time_column <= max(time_column) - threshold` condition is met.
- `pw.Table.ignore_late` to filter out old (in terms of event time) entries.
- Rows batching for async UDFs. It can be enabled with `max_batch_size` parameter.

### Changed
- `pw.io.subscribe` and `pw.io.python.write` now work with async callbacks.
- The `diff` column in tables automatically created by `pw.io.postgres.write` and `pw.io.postgres.write_snapshot` in `replace` and `create_if_not_exists` initialization modes now uses the `smallint` type.
- `optimize_transaction_log` option has been removed from `pw.io.deltalake.TableOptimizer`.

### Fixed
- `pw.io.postgres.write` and `pw.io.postgres.write_snapshot` now respect the type optionality defined in the Pathway table schema when creating a new PostgreSQL table. This applies to the `replace` and `create_if_not_exists` initialization modes.

## [0.26.0] - 2025-08-14

### Added
- `path_filter` parameter in `pw.io.s3.read` and `pw.io.minio.read` functions. It enables post-filtering of object paths using a wildcard pattern (`*`, `?`), allowing exclusion of paths that pass the main `path` filter but do not match `path_filter`.
- Input connectors now support backpressure control via `max_backlog_size`, allowing to limit the number of read events in processing per connector. This is useful when the data source emits a large initial burst followed by smaller, incremental updates.
- `pw.reducers.count_distinct` and `pw.reducers.count_distinct_approximate` to count the number of distinct elements in a table. The `pw.reducers.count_distinct_approximate` allows you to save memory by decreasing the accuracy. It is possible to control this tradeoff by using the `precision` parameter.
- `pw.Table.join` (and its variants) now has two additional parameters - `left_exactly_once` and `right_exactly_once`. If the elements from a side of a join should be joined exactly once, `*_exactly_once` parameter of the side can be set to `True`. Then after getting a match an entry will be removed from the join state and the memory consumption will be reduced.

### Changed
- Delta table compression logging has been improved: logs now include table names, and verbose messages have been streamlined while preserving details of important processing steps.
- Improved initialization speed of `pw.io.s3.read` and `pw.io.minio.read`.
- `pw.io.s3.read` and `pw.io.minio.read` now limit the number and the total size of objects to be predownloaded.
- **BREAKING** optimized the implementation of `pw.reducers.min`, `pw.reducers.max`, `pw.reducers.argmin`, `pw.reducers.argmax`, `pw.reducers.any` reducers for append-only tables. It is a breaking change for programs using operator persistence. The persisted state will have to be recomputed.
- **BREAKING** optimized the implementation of `pw.reducers.sum` reducer on `float` and `np.ndarray` columns. It is a breaking change for programs using operator persistence. The persisted state will have to be recomputed.
- **BREAKING** the implementation of data persistence has been optimized for the case of many small objects in filesystem and S3 connectors. It is a breaking change for programs using data persistence. The persisted state will have to be recomputed.
- **BREAKING** the data snapshot logic in persistence has been optimized for the case of big input snapshots. It is a breaking change for programs using data persistence. The persisted state will have to be recomputed.
- Improved precision of `pw.reducers.sum` on `float` columns by introducing Neumeier summation.

## [0.25.1] - 2025-07-24

### Added
- `pw.xpacks.llm.mcp_server.PathwayMcp` that allows serving `pw.xpacks.llm.document_store.DocumentStore` and `pw.xpacks.llm.question_answering` endpoints as MCP (Model Context Protocol) tools.
- `pw.io.dynamodb.write` method for writing to Dynamo DB.

## [0.25.0] - 2025-07-10

### Added
- `pw.io.questdb.write` method for writing to Quest DB.
- `pw.io.fs.read` now supports the `"only_metadata"` format. When this format is used, the table will contain only metadata updates for the tracked directory, without reading file contents.
- `pw.Table.to_stream` that transforms a table to a stream of changes from this table.
- `pw.Table.stream_to_table`, `pw.Table.from_streams` that transform a streams of changes to tables.
- `pw.Table.assert_append_only` that sets append_only property of a table and verifies at runtime if the condition is met.

### Changed
- **BREAKING** The Elasticsearch and BigQuery connectors have been moved to the Scale license tier. You can obtain the Scale tier license for fr
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Pathway Code of Conduct

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and our
community a harassment-free experience for everyone, regardless of age, body
size, disability, health condition, ethnicity, gender identity and expression, level of
experience, nationality, country of origin, personal appearance, race, religion, or sexual identity
and orientation, and any other criteria falling under discriminatory practices under the Law of France.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

*   Using welcoming and inclusive language.
*   Being respectful of differing viewpoints and experiences.
*   Gracefully accepting constructive criticism.
*   Focusing on what is best for the community.
*   Showing empathy towards other community members.

Examples of unacceptable behavior by participants include:

*   The use of sexualized language or imagery and unwelcome sexual attention or
    advances.
*   Trolling, insulting/derogatory comments, and personal or political attacks.
*   Public or private harassment.
*   Publishing others' private information, such as a physical or electronic
    address, without explicit permission.
*   Conduct which could reasonably be considered inappropriate for the forum in
    which it occurs.

All Pathway forums and spaces are meant for professional interactions, and any behavior which could reasonably be considered inappropriate in a professional setting is unacceptable.


## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.


## Scope

This Code of Conduct applies to all content on pathway.com, Pathway’s GitHub organization, or any other official Pathway web presence allowing for community interactions, as well as at all official Pathway events, whether offline or online.

The Code of Conduct also applies within project spaces and in public spaces whenever an individual is representing Pathway or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed or de facto representative at an online or offline event.


## Conflict Resolution

Conflicts in an open source project can take many forms, from someone having a bad day and using harsh and hurtful language in the issue queue, to more serious instances such as sexist/racist statements or threats of violence, and everything in between.

If the behavior is threatening or harassing, or for other reasons requires immediate escalation, please see below.

However, for the vast majority of issues, we aim to empower individuals to first resolve conflicts themselves, asking for help when needed, and only after that fails to escalate further. This approach gives people more control over the outcome of their dispute. 

If you are experiencing or witnessing conflict, we ask you to use the following escalation strategy to address the conflict:

1.  If you so wish and if you do not feel threatened or at risk of any form of personal abuse, address the perceived conflict directly with those involved, preferably in a real-time medium.
2.  If this fails, get a third party (e.g. a mutual friend, and/or someone with
    background on the issue, but not involved in the conflict) to intercede.
3.  If you are still unable to resolve the conflict, and you believe it rises to
    harassment or another code of conduct violation, report it.

Please note that if you are experiencing or witnessing a discriminatory practice that would be susceptible to be condemned by law, we ask you to directly escalate to 3. 

## Reporting Violations

Violations of the Code of Conduct can be reported to Pathway via email to code_of_conduct@pathway.com. Project maintainers will determine whether the Code of Conduct was violated, and will issue an appropriate sanction, possibly including a written warning or expulsion from the project, project sponsored spaces, or project forums. We ask that you make a good-faith effort to resolve your conflict via the conflict resolution policy before submitting a report.

Violations of the Code of Conduct can occur in any setting, even those unrelated to the project. We will only consider complaints about conduct that has occurred within one year of the report.


## Enforcement

If the Project maintainers receive a report alleging a violation of the Code of Conduct, the Project maintainers will notify the accused of the report, and provide them an opportunity to discuss the report before a sanction is issued. The Project maintainers will do their utmost to keep the reporter anonymous. If the act is ongoing (such as someone engaging in harassment), or involves a threat to anyone's safety (e.g. threats of violence), the Project maintainers may issue sanctions without notice.


## Attribution

This Code of Conduct is adapted from the Tensorflow Code of Conduct, and based on Contributor Covenant, version 1.4, available at https://contributor-covenant.org/version/1/4, and includes some aspects of the Geek Feminism Code of Conduct and the Drupal Code of Conduct.

```

### File: CONTRIBUTING.md
```md
# Contributing to Pathway

Welcome! This guide is intended to help developers that are new to the community
to make contributions to the Pathway project. Please be sure to also read our [code of conduct](CODE_OF_CONDUCT.md). We work hard to make this a welcoming community for all, and we're excited to have you on board!

## The basics:

* Use the [Issue Tracker](https://github.com/pathwaycom/pathway/issues) to
  report bugs, crashes, performance issues, etc... Please include as much detail
  as possible.

* [Discord](https://discord.com/invite/pathway) is our main gathering place - jump in and ask us anything!

* [Our forum](https://discord.com/channels/1042405378304004156/1044276516290314381) is a great
  venue to ask questions, start a design discussion, or post an RFC.

## Contributing Code

We are eager to build Pathway together with the community and are excited to have you here!

Important: Before you contribute any changes to our repositories (make a Pull Request) please get in touch with us and explain what you want to work on. You can do so by filing an issue, or asking us on Discord. That way you can get coding advice and speedier reviews. If you start to work on an issue before hearing back from a Pathway core team engineer there is a chance that we will not be able to accept your changes - something we all want to avoid!

We use a standard GitHub fork + pull request model for merging and reviewing
changes. New pull requests should be made against the main upstream branch.
After a pull request is opened it will be reviewed, and merged after
passing continuous integration tests and being accepted by a project or
sub-system maintainer.

We maintain a [Changelog](https://github.com/pathwaycom/pathway/blob/main/CHANGELOG.md) where all notable changes to this project are documented. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

We ask that developers sign our [contributor license
agreement](https://cla-assistant.io/pathwaycom/pathway). The
process of signing the CLA is automated, and you'll be prompted with instructions
the first time you submit a pull request to the project.

```

### File: LICENSE.txt
```txt
License:
    BSL 1.1
    
Licensor:
    NavAlgo SAS
    
Licensed Work:
    Pathway
    
    Releases of Pathway covered by this License contain a copy of this License
    as their license file, and are made available by the Licensor at
    pathway.com, github.com/pathwaycom/, and by way of other distribution
    channels.
    The Licensed Work is © 2024 NavAlgo SAS
    
Additional Use Grant:
    The Licensor grants you (the licensee) additional rights to the Licensed
    Work, whereby you are entitled to run the Licensed Work in production
    use, at no cost, subject to all of the following conditions: 
    (a) in a single installation of the Licensed Work you may run the Licensed
    Work on only one machine, physical or virtual, and without exceeding the
    number of worker threads and processes allowed by the configuration of the
    software runner of the distribution; and 
    (b) the additional right to use granted herein applies to the exclusion
    of use of the Licensed Work for a Stream Data Processing Service, as well
    as to the exclusion of use of any modified or derivative Licensed Work,
    in particular:
    - you may not move, change, disable, or circumvent any license key
    or resource limiting functionality that may be present in the software,
    and you may not remove or obscure any functionality in the software that
    is protected by the license key or circumvent resource limits,
    - you may not alter, remove, or obscure any licensing, copyright, or other
    notices of the licensor in the software; 
    (c) the production use of modified Licensed Work is permitted only where
    the modifications of the Licensed Work are indispensable to fix bugs or
    vulnerabilities which might otherwise alter the scope of functionalities
    of the Licensed Work, as described in API documentation available at
    https://pathway.com/developers/documentation/api-docs/pathway; and
    (d) this entire License including its Additional Use Grant shall remain
    in full force and effect for any use under this Additional Use Grant,
    thus covering the Licensed Work and also binding any and all users of
    the Licensed Work. 
    A “Stream Data Processing Service” is defined as any offering that allows
    third parties (other than your employees or individual contractors) to
    access the functionality of the Licensed Work by performing an action
    directly or indirectly that causes the deployment, creation, or change to
    the structure of a running computation graph of Pathway on any machine.
    For the sake of clarity, a Stream Data Processing Service would include
    providers of infrastructure services, such as cloud services, hosting
    services, data center services and similarly situated third parties
    (including affiliates of such entities) that would offer the Licensed
    Work, possibly in connection with a broader service offering, to their
    customers or subscribers.
 
Change Date:
    Change date is four years from the date of code merge into the main
    release branch of Pathway in the GitHub repo (and in no case earlier
    than July 20, 2027). Please see GitHub commit history for exact
    dates.
    
Change License:
    Apache License, Version 2.0, as published by the Apache Foundation.
    
    
The Licensor hereby grants you the right to copy, modify, create derivative
works, redistribute, and make non-production use of the Licensed Work. The
Licensor may make an Additional Use Grant, above, permitting limited 
production use.

Effective on the Change Date, or the fifth anniversary of the first publicly
available distribution of a specific version of the Licensed Work under this
License, whichever comes first, the Licensor hereby grants you rights under
the terms of the Change License, and the rights granted in the paragraph
above terminate.

If your use of the Licensed Work does not comply with the requirements
currently in effect as described in this License, you must purchase
a commercial license from the Licensor, its affiliated entities, or 
authorized resellers, or you must refrain from using the Licensed Work.
All copies of the original and modified Licensed Work, and derivative works
of the Licensed Work, are subject to this License. This License applies
separately for each version of the Licensed Work and the Change Date may
vary for each version of the Licensed Work released by Licensor.
You must conspicuously display this License on each original or modified
copy of the Licensed Work. If you receive the Licensed Work in original or
modified form from a third party, the terms and conditions set forth in this
License apply to your use of that work.

Any use of the Licensed Work in violation of this License will automatically
terminate your rights under this License for the current and all other
versions of the Licensed Work.

This License does not grant you any right in any trademark or logo of
Licensor or its affiliates (provided that you may use a trademark or logo of
Licensor as expressly required by this License). TO THE EXTENT PERMITTED BY
APPLICABLE LAW, THE LICENSED WORK IS PROVIDED ON AN “AS IS” BASIS. LICENSOR
HEREBY DISCLAIMS ALL WARRANTIES AND CONDITIONS, EXPRESS OR IMPLIED,
INCLUDING (WITHOUT LIMITATION) WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE, NON-INFRINGEMENT, AND TITLE.

```

### File: .github\pull_request_template.md
```md
### Introduction
To contribute code to the Pathway project, start by discussing your proposed changes on Discord or by filing an issue. 
Once approved, follow the fork + pull request model against the main branch, ensuring you've signed the contributor license agreement.

### Context
<!--- Why is this change required? What problem does it solve? -->

### How has this been tested?
<!--- Please describe in detail how you tested your changes. -->

### Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature or improvement (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)

### Related issue(s):
1. 
2.
3.

### Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're here to help! -->
- [ ] My code follows the code style of this project,
- [ ] My change requires a change to the documentation,
- [ ] I described the modification in the CHANGELOG.md file.
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
