---
id: github.com-harehare-mq-elixir-06fede4d-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.808430
---

# KNOWLEDGE EXTRACT: github.com_harehare_mq_elixir_06fede4d
> **Extracted on:** 2026-04-01 15:14:18
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524374/github.com_harehare_mq_elixir_06fede4d

---

## File: `.formatter.exs`
```
# Used by "mix format"
[
  inputs: ["{mix,.formatter}.exs", "{config,lib,test}/**/*.{ex,exs}"]
]
```

## File: `.gitignore`
```
# The directory Mix will write compiled artifacts to.
/_build/

# If you run "mix test --cover", coverage assets end up here.
/cover/

# The directory Mix downloads your dependencies sources to.
/deps/

# Where third-party dependencies like ExDoc output generated docs.
/doc/

# Temporary files, for example, from tests.
/tmp/

# If the VM crashes, it generates a dump, let's ignore it too.
erl_crash.dump

# Also ignore archive artifacts (built via "mix archive.build").
*.ez

# Ignore package tarball (built via "mix hex.build").
mq-*.tar

target

*.so

.claude/settings.local.json

.elixir_ls

.DS_Store
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-29

### Added
- Initial release of mq_elixir

[0.1.0]: https://github.com/harehare/mq_elixir/releases/tag/v0.1.0
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Takahiro Sato

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
# mq_elixir

Elixir bindings for [mq](https://mqlang.org/), a jq-like command-line tool for Markdown processing.

## Features

- Process markdown, MDX, HTML, and plain text
- Full mq query language support
- Multiple input and output format options
- Configurable rendering options
- Fast Rust-powered NIF implementation

## Installation

Add `mq` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:mq_elixir, "~> 0.1.0"}
  ]
end
```


## Usage

### Basic Query

```elixir
# Extract all H1 headings
{:ok, result} = Mq.run(".h1", "# Hello\n## World")
IO.inspect(result.values)  # ["# Hello"]
```

### Working with Results

```elixir
{:ok, result} = Mq.run(".h", "# H1\n## H2\n### H3")

# Access values
result.values  # ["# H1", "## H2", "### H3"]
result.text    # "# H1\n## H2\n### H3"

# Enumerate
Enum.each(result, fn heading -> IO.puts(heading) end)
```

## Documentation

Full documentation is available on [HexDocs](https://hexdocs.pm/mq_elixir).

For mq query language syntax, see the [official mq documentation](https://mqlang.org/).

## License

MIT License
```

## File: `mix.exs`
```
defmodule Mq.MixProject do
  use Mix.Project

  @version "0.1.11"
  @source_url "https://github.com/harehare/mq_elixir"

  def project do
    [
      app: :mq_elixir,
      version: @version,
      elixir: "~> 1.14",
      start_permanent: Mix.env() == :prod,
      deps: deps(),
      description: description(),
      package: package(),
      docs: docs(),
      test_coverage: [tool: ExCoveralls]
    ]
  end

  def cli do
    [
      preferred_envs: [
        coveralls: :test,
        "coveralls.detail": :test,
        "coveralls.post": :test,
        "coveralls.html": :test
      ]
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger]
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
    [
      {:rustler, "~> 0.37.0"},
      {:ex_doc, "~> 0.31", only: :dev, runtime: false},
      {:excoveralls, "~> 0.18", only: :test},
      {:credo, "~> 1.7", only: [:dev, :test], runtime: false},
      {:dialyxir, "~> 1.4", only: [:dev, :test], runtime: false}
    ]
  end

  defp description do
    """
    Elixir bindings for mq, a jq-like command-line tool for Markdown processing.
    Process markdown, MDX, HTML, and plain text using the mq query language.
    """
  end

  defp package do
    [
      name: "mq_elixir",
      files:
        ~w(lib native/mq_nif/src native/mq_nif/Cargo.toml native/mq_nif/Cargo.lock .formatter.exs mix.exs README.md LICENSE CHANGELOG.md),
      licenses: ["MIT"],
      links: %{
        "GitHub" => @source_url,
        "Documentation" => "https://mqlang.org/"
      },
      maintainers: ["Takahiro Sato"]
    ]
  end

  defp docs do
    [
      main: "Mq",
      source_ref: "v#{@version}",
      source_url: @source_url,
      extras: ["README.md", "CHANGELOG.md"]
    ]
  end
end
```

## File: `mix.lock`
```
%{
  "bunt": {:hex, :bunt, "1.0.0", "081c2c665f086849e6d57900292b3a161727ab40431219529f13c4ddcf3e7a44", [:mix], [], "hexpm", "dc5f86aa08a5f6fa6b8096f0735c4e76d54ae5c9fa2c143e5a1fc7c1cd9bb6b5"},
  "credo": {:hex, :credo, "1.7.15", "283da72eeb2fd3ccf7248f4941a0527efb97afa224bcdef30b4b580bc8258e1c", [:mix], [{:bunt, "~> 0.2.1 or ~> 1.0", [hex: :bunt, repo: "hexpm", optional: false]}, {:file_system, "~> 0.2 or ~> 1.0", [hex: :file_system, repo: "hexpm", optional: false]}, {:jason, "~> 1.0", [hex: :jason, repo: "hexpm", optional: false]}], "hexpm", "291e8645ea3fea7481829f1e1eb0881b8395db212821338e577a90bf225c5607"},
  "dialyxir": {:hex, :dialyxir, "1.4.7", "dda948fcee52962e4b6c5b4b16b2d8fa7d50d8645bbae8b8685c3f9ecb7f5f4d", [:mix], [{:erlex, ">= 0.2.8", [hex: :erlex, repo: "hexpm", optional: false]}], "hexpm", "b34527202e6eb8cee198efec110996c25c5898f43a4094df157f8d28f27d9efe"},
  "earmark_parser": {:hex, :earmark_parser, "1.4.44", "f20830dd6b5c77afe2b063777ddbbff09f9759396500cdbe7523efd58d7a339c", [:mix], [], "hexpm", "4778ac752b4701a5599215f7030989c989ffdc4f6df457c5f36938cc2d2a2750"},
  "erlex": {:hex, :erlex, "0.2.8", "cd8116f20f3c0afe376d1e8d1f0ae2452337729f68be016ea544a72f767d9c12", [:mix], [], "hexpm", "9d66ff9fedf69e49dc3fd12831e12a8a37b76f8651dd21cd45fcf5561a8a7590"},
  "ex_doc": {:hex, :ex_doc, "0.39.3", "519c6bc7e84a2918b737aec7ef48b96aa4698342927d080437f61395d361dcee", [:mix], [{:earmark_parser, "~> 1.4.44", [hex: :earmark_parser, repo: "hexpm", optional: false]}, {:makeup_c, ">= 0.1.0", [hex: :makeup_c, repo: "hexpm", optional: true]}, {:makeup_elixir, "~> 0.14 or ~> 1.0", [hex: :makeup_elixir, repo: "hexpm", optional: false]}, {:makeup_erlang, "~> 0.1 or ~> 1.0", [hex: :makeup_erlang, repo: "hexpm", optional: false]}, {:makeup_html, ">= 0.1.0", [hex: :makeup_html, repo: "hexpm", optional: true]}], "hexpm", "0590955cf7ad3b625780ee1c1ea627c28a78948c6c0a9b0322bd976a079996e1"},
  "excoveralls": {:hex, :excoveralls, "0.18.5", "e229d0a65982613332ec30f07940038fe451a2e5b29bce2a5022165f0c9b157e", [:mix], [{:castore, "~> 1.0", [hex: :castore, repo: "hexpm", optional: true]}, {:jason, "~> 1.0", [hex: :jason, repo: "hexpm", optional: false]}], "hexpm", "523fe8a15603f86d64852aab2abe8ddbd78e68579c8525ae765facc5eae01562"},
  "file_system": {:hex, :file_system, "1.1.1", "31864f4685b0148f25bd3fbef2b1228457c0c89024ad67f7a81a3ffbc0bbad3a", [:mix], [], "hexpm", "7a15ff97dfe526aeefb090a7a9d3d03aa907e100e262a0f8f7746b78f8f87a5d"},
  "finch": {:hex, :finch, "0.20.0", "5330aefb6b010f424dcbbc4615d914e9e3deae40095e73ab0c1bb0968933cadf", [:mix], [{:mime, "~> 1.0 or ~> 2.0", [hex: :mime, repo: "hexpm", optional: false]}, {:mint, "~> 1.6.2 or ~> 1.7", [hex: :mint, repo: "hexpm", optional: false]}, {:nimble_options, "~> 0.4 or ~> 1.0", [hex: :nimble_options, repo: "hexpm", optional: false]}, {:nimble_pool, "~> 1.1", [hex: :nimble_pool, repo: "hexpm", optional: false]}, {:telemetry, "~> 0.4 or ~> 1.0", [hex: :telemetry, repo: "hexpm", optional: false]}], "hexpm", "2658131a74d051aabfcba936093c903b8e89da9a1b63e430bee62045fa9b2ee2"},
  "hpax": {:hex, :hpax, "1.0.3", "ed67ef51ad4df91e75cc6a1494f851850c0bd98ebc0be6e81b026e765ee535aa", [:mix], [], "hexpm", "8eab6e1cfa8d5918c2ce4ba43588e894af35dbd8e91e6e55c817bca5847df34a"},
  "jason": {:hex, :jason, "1.4.4", "b9226785a9aa77b6857ca22832cffa5d5011a667207eb2a0ad56adb5db443b8a", [:mix], [{:decimal, "~> 1.0 or ~> 2.0", [hex: :decimal, repo: "hexpm", optional: true]}], "hexpm", "c5eb0cab91f094599f94d55bc63409236a8ec69a21a67814529e8d5f6cc90b3b"},
  "makeup": {:hex, :makeup, "1.2.1", "e90ac1c65589ef354378def3ba19d401e739ee7ee06fb47f94c687016e3713d1", [:mix], [{:nimble_parsec, "~> 1.4", [hex: :nimble_parsec, repo: "hexpm", optional: false]}], "hexpm", "d36484867b0bae0fea568d10131197a4c2e47056a6fbe84922bf6ba71c8d17ce"},
  "makeup_elixir": {:hex, :makeup_elixir, "1.0.1", "e928a4f984e795e41e3abd27bfc09f51db16ab8ba1aebdba2b3a575437efafc2", [:mix], [{:makeup, "~> 1.0", [hex: :makeup, repo: "hexpm", optional: false]}, {:nimble_parsec, "~> 1.2.3 or ~> 1.3", [hex: :nimble_parsec, repo: "hexpm", optional: false]}], "hexpm", "7284900d412a3e5cfd97fdaed4f5ed389b8f2b4cb49efc0eb3bd10e2febf9507"},
  "makeup_erlang": {:hex, :makeup_erlang, "1.0.2", "03e1804074b3aa64d5fad7aa64601ed0fb395337b982d9bcf04029d68d51b6a7", [:mix], [{:makeup, "~> 1.0", [hex: :makeup, repo: "hexpm", optional: false]}], "hexpm", "af33ff7ef368d5893e4a267933e7744e46ce3cf1f61e2dccf53a111ed3aa3727"},
  "mime": {:hex, :mime, "2.0.7", "b8d739037be7cd402aee1ba0306edfdef982687ee7e9859bee6198c1e7e2f128", [:mix], [], "hexpm", "6171188e399ee16023ffc5b76ce445eb6d9672e2e241d2df6050f3c771e80ccd"},
  "mint": {:hex, :mint, "1.7.1", "113fdb2b2f3b59e47c7955971854641c61f378549d73e829e1768de90fc1abf1", [:mix], [{:castore, "~> 0.1.0 or ~> 1.0", [hex: :castore, repo: "hexpm", optional: true]}, {:hpax, "~> 0.1.1 or ~> 0.2.0 or ~> 1.0", [hex: :hpax, repo: "hexpm", optional: false]}], "hexpm", "fceba0a4d0f24301ddee3024ae116df1c3f4bb7a563a731f45fdfeb9d39a231b"},
  "nimble_options": {:hex, :nimble_options, "1.1.1", "e3a492d54d85fc3fd7c5baf411d9d2852922f66e69476317787a7b2bb000a61b", [:mix], [], "hexpm", "821b2470ca9442c4b6984882fe9bb0389371b8ddec4d45a9504f00a66f650b44"},
  "nimble_parsec": {:hex, :nimble_parsec, "1.4.2", "8efba0122db06df95bfaa78f791344a89352ba04baedd3849593bfce4d0dc1c6", [:mix], [], "hexpm", "4b21398942dda052b403bbe1da991ccd03a053668d147d53fb8c4e0efe09c973"},
  "nimble_pool": {:hex, :nimble_pool, "1.1.0", "bf9c29fbdcba3564a8b800d1eeb5a3c58f36e1e11d7b7fb2e084a643f645f06b", [:mix], [], "hexpm", "af2e4e6b34197db81f7aad230c1118eac993acc0dae6bc83bac0126d4ae0813a"},
  "req": {:hex, :req, "0.5.16", "99ba6a36b014458e52a8b9a0543bfa752cb0344b2a9d756651db1281d4ba4450", [:mix], [{:brotli, "~> 0.3.1", [hex: :brotli, repo: "hexpm", optional: true]}, {:ezstd, "~> 1.0", [hex: :ezstd, repo: "hexpm", optional: true]}, {:finch, "~> 0.17", [hex: :finch, repo: "hexpm", optional: false]}, {:jason, "~> 1.0", [hex: :jason, repo: "hexpm", optional: false]}, {:mime, "~> 2.0.6 or ~> 2.1", [hex: :mime, repo: "hexpm", optional: false]}, {:nimble_csv, "~> 1.0", [hex: :nimble_csv, repo: "hexpm", optional: true]}, {:plug, "~> 1.0", [hex: :plug, repo: "hexpm", optional: true]}], "hexpm", "974a7a27982b9b791df84e8f6687d21483795882a7840e8309abdbe08bb06f09"},
  "rustler": {:hex, :rustler, "0.37.1", "721434020c7f6f8e1cdc57f44f75c490435b01de96384f8ccb96043f12e8a7e0", [:mix], [{:jason, "~> 1.0", [hex: :jason, repo: "hexpm", optional: false]}], "hexpm", "24547e9b8640cf00e6a2071acb710f3e12ce0346692e45098d84d45cdb54fd79"},
  "telemetry": {:hex, :telemetry, "1.3.0", "fedebbae410d715cf8e7062c96a1ef32ec22e764197f70cda73d82778d61e7a2", [:rebar3], [], "hexpm", "7015fc8919dbe63764f4b4b87a95b7c0996bd539e0d499be6ec9d7f3875b79e6"},
  "toml": {:hex, :toml, "0.7.0", "fbcd773caa937d0c7a02c301a1feea25612720ac3fa1ccb8bfd9d30d822911de", [:mix], [], "hexpm", "0690246a2478c1defd100b0c9b89b4ea280a22be9a7b313a8a058a2408a2fa70"},
}
```

## File: `lib/mq.ex`
```
defmodule Mq do
  @moduledoc """
  Elixir bindings for the mq markdown processing library.

  ## Features

  - Process markdown, MDX, HTML, and plain text
  - Full mq query language support
  - Multiple input and output format options
  - Configurable rendering options

  ## Installation

  Add `mq` to your list of dependencies in `mix.exs`:

      def deps do
        [
          {:mq, "~> 0.5.9"}
        ]
      end

  ## Usage

      # Basic heading extraction
      {:ok, result} = Mq.run(".h1", "# Hello\\n## World")
      IO.inspect(result.values)  # ["# Hello"]

      # With options
      options = %Mq.Options{input_format: :markdown}
      {:ok, result} = Mq.run(".h2", markdown_content, options)

      # HTML to Markdown conversion
      {:ok, markdown} = Mq.html_to_markdown("<h1>Hello</h1>")
  """

  alias Mq.{ConversionOptions, Native, Options, Result}

  @doc """
  Run an mq query on the provided content.

  ## Parameters

  - `code` - The mq query string
  - `content` - The markdown/HTML/text content to process
  - `options` - Optional configuration (defaults to `%Mq.Options{}`)

  ## Returns

  - `{:ok, %Mq.Result{}}` on success
  - `{:error, reason}` on failure

  ## Examples

      iex> Mq.run(".h1", "# Title\\n## Subtitle")
      {:ok, %Mq.Result{values: ["# Title"], text: "# Title"}}

      iex> options = %Mq.Options{input_format: :text}
      iex> {:ok, _result} = Mq.run("select(contains(\\"test\\"))", "line1\\ntest line\\nline3", options)
      {:ok, %Mq.Result{values: ["test line"], text: "test line"}}
  """
  @spec run(String.t(), String.t(), Options.t() | nil) ::
          {:ok, Result.t()} | {:error, String.t()}
  def run(code, content, options \\ nil) do
    opts = options || %Options{}

    case Native.run(code, content, Options.to_map(opts)) do
      {:ok, result_map} -> {:ok, Result.from_map(result_map)}
      {:error, _} = error -> error
    end
  end

  @doc """
  Convert HTML to Markdown.

  ## Parameters

  - `content` - The HTML content to convert
  - `options` - Optional conversion options

  ## Returns

  - `{:ok, markdown_string}` on success
  - `{:error, reason}` on failure

  ## Examples

      iex> Mq.html_to_markdown("<h1>Hello</h1><p>World</p>")
      {:ok, "# Hello\\n\\nWorld"}

      iex> html_content = "<html><head><title>Title</title></head><body><h1>Content</h1></body></html>"
      iex> opts = %Mq.ConversionOptions{use_title_as_h1: true}
      iex> {:ok, markdown} = Mq.html_to_markdown(html_content, opts)
      {:ok, markdown}
  """
  @spec html_to_markdown(String.t(), ConversionOptions.t() | nil) ::
          {:ok, String.t()} | {:error, String.t()}
  def html_to_markdown(content, options \\ nil) do
    opts = options || %ConversionOptions{}

    case Native.html_to_markdown(content, ConversionOptions.to_map(opts)) do
      result when is_binary(result) -> {:ok, result}
      {:error, _} = error -> error
    end
  end
end
```

## File: `lib/mq/conversion_options.ex`
```
defmodule Mq.ConversionOptions do
  @moduledoc """
  Options for HTML to Markdown conversion.

  ## Fields

  - `:extract_scripts_as_code_blocks` - Extract `<script>` tags as code blocks
  - `:generate_front_matter` - Generate YAML front matter from meta tags
  - `:use_title_as_h1` - Use `<title>` tag as H1 heading
  """

  @type t :: %__MODULE__{
          extract_scripts_as_code_blocks: boolean(),
          generate_front_matter: boolean(),
          use_title_as_h1: boolean()
        }

  defstruct extract_scripts_as_code_blocks: false,
            generate_front_matter: false,
            use_title_as_h1: false

  @doc """
  Convert ConversionOptions struct to a map for passing to NIF.
  """
  @spec to_map(t()) :: map()
  def to_map(%__MODULE__{} = opts) do
    Map.from_struct(opts)
  end
end
```

## File: `lib/mq/input_format.ex`
```
defmodule Mq.InputFormat do
  @moduledoc """
  Input format constants for mq queries.

  ## Available Formats

  - `:markdown` - Standard Markdown (default)
  - `:mdx` - Markdown with JSX
  - `:html` - HTML content
  - `:text` - Plain text (line-by-line processing)
  - `:raw` - Raw string input
  - `:null` - Null/empty input
  """

  @type t :: :markdown | :mdx | :html | :text | :raw | :null

  @doc """
  List all available input formats.
  """
  @spec all() :: [t(), ...]
  def all, do: [:markdown, :mdx, :html, :text, :raw, :null]

  @doc """
  Validate an input format.
  """
  @spec valid?(atom()) :: boolean()
  def valid?(format), do: format in all()
end
```

## File: `lib/mq/native.ex`
```
defmodule Mq.Native do
  @moduledoc false

  use Rustler,
    otp_app: :mq_elixir,
    crate: :mq_nif,
    path: "native/mq_nif"

  @doc false
  def run(_code, _content, _options), do: :erlang.nif_error(:nif_not_loaded)

  @doc false
  def html_to_markdown(_content, _options), do: :erlang.nif_error(:nif_not_loaded)
end
```

## File: `lib/mq/options.ex`
```
defmodule Mq.Options do
  @moduledoc """
  Configuration options for mq query execution.

  ## Fields

  - `:input_format` - Input format (`:markdown`, `:mdx`, `:text`, `:html`, `:raw`, `:null`)
  - `:list_style` - List marker style (`:dash`, `:plus`, `:star`)
  - `:link_title_style` - Link title quoting (`:double`, `:single`, `:paren`)
  - `:link_url_style` - Link URL wrapping (`:angle`, `:none`)
  """

  @type input_format :: :markdown | :mdx | :text | :html | :raw | :null
  @type list_style :: :dash | :plus | :star
  @type title_surround_style :: :double | :single | :paren
  @type url_surround_style :: :angle | :none

  @type t :: %__MODULE__{
          input_format: input_format() | nil,
          list_style: list_style() | nil,
          link_title_style: title_surround_style() | nil,
          link_url_style: url_surround_style() | nil
        }

  defstruct [
    :input_format,
    :list_style,
    :link_title_style,
    :link_url_style
  ]

  @doc """
  Convert Options struct to a map for passing to NIF.
  Filters out nil values.
  """
  @spec to_map(t()) :: map()
  def to_map(%__MODULE__{} = opts) do
    opts
    |> Map.from_struct()
    |> Enum.reject(fn {_k, v} -> is_nil(v) end)
    |> Map.new()
  end
end
```

## File: `lib/mq/result.ex`
```
defmodule Mq.Result do
  @moduledoc """
  Result of an mq query execution.

  ## Fields

  - `:values` - List of result values (strings)
  - `:text` - All values joined by newlines
  """

  @type t :: %__MODULE__{
          values: [String.t()],
          text: String.t()
        }

  defstruct values: [], text: ""

  @doc """
  Create a Result from a map returned by the NIF.
  """
  @spec from_map(map()) :: t()
  def from_map(%{values: values, text: text}) do
    %__MODULE__{values: values, text: text}
  end

  @doc """
  Get the number of values in the result.
  """
  @spec length(t()) :: non_neg_integer()
  def length(%__MODULE__{values: values}), do: Kernel.length(values)

  @doc """
  Check if the result is empty.
  """
  @spec empty?(t()) :: boolean()
  def empty?(%__MODULE__{values: values}), do: values == []
end

defimpl Enumerable, for: Mq.Result do
  def count(result), do: {:ok, Mq.Result.length(result)}

  def member?(result, value) do
    {:ok, value in result.values}
  end

  def reduce(%Mq.Result{values: values}, acc, fun) do
    Enum.reduce(values, acc, fun)
  end

  def slice(%Mq.Result{values: values}) do
    size = Kernel.length(values)

    {:ok, size,
     fn start, length, step -> values |> Enum.slice(start, length) |> Enum.take_every(step) end}
  end
end

defimpl String.Chars, for: Mq.Result do
  def to_string(result), do: result.text
end
```

## File: `native/mq_nif/Cargo.toml`
```
[package]
authors = ["Takahiro Sato <harehare1110@gmail.com>"]
description = "Elixir NIF bindings for mq Markdown processing"
edition = "2024"
license = "MIT"
name = "mq_nif"
version = "0.1.11"

[lib]
crate-type = ["cdylib"]
name = "mq_nif"

[dependencies]
mq-lang = {version = "0.5.24"}
mq-markdown = {version = "0.5.24"}
rustler = "0.37.0"

[profile.release]
codegen-units = 1
lto = true
```

## File: `native/mq_nif/src/atoms.rs`
```rust
rustler::atoms! {
    // Result atoms
    ok,
    error,

    // Result struct keys
    values,
    text,

    // Input format atoms
    markdown,
    mdx,
    html,
    raw,
    null,

    // Option keys
    input_format,
}
```

## File: `native/mq_nif/src/lib.rs`
```rust
mod atoms;
mod result;
mod value;

use std::collections::HashMap;

use result::MqResult;
use rustler::{Atom, Encoder, Env, Error, NifMap, Term};
use value::MqValue;

/// Input format for mq queries
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
enum InputFormat {
    #[default]
    Markdown,
    Mdx,
    Text,
    Html,
    Raw,
    Null,
}

/// Options for running mq queries
#[derive(Debug, Clone, Copy, Default)]
struct Options {
    input_format: InputFormat,
}

impl<'a> rustler::Decoder<'a> for Options {
    fn decode(term: Term<'a>) -> Result<Self, Error> {
        let map: HashMap<Atom, Atom> = term.decode()?;
        let input_format = map.get(&atoms::input_format()).cloned();

        Ok(Options {
            input_format: parse_input_format(input_format),
        })
    }
}

fn parse_input_format(atom: Option<Atom>) -> InputFormat {
    match atom {
        Some(a) => {
            if a == atoms::mdx() {
                InputFormat::Mdx
            } else if a == atoms::text() {
                InputFormat::Text
            } else if a == atoms::html() {
                InputFormat::Html
            } else if a == atoms::raw() {
                InputFormat::Raw
            } else if a == atoms::null() {
                InputFormat::Null
            } else {
                InputFormat::Markdown // Default for unknown atoms
            }
        }
        None => InputFormat::Markdown, // Default when no format specified
    }
}

/// Options for HTML to Markdown conversion
#[derive(Debug, Clone, Copy, NifMap, Default)]
struct ConversionOptions {
    extract_scripts_as_code_blocks: bool,
    generate_front_matter: bool,
    use_title_as_h1: bool,
}

/// Run an mq query on the provided content
#[rustler::nif]
fn run<'a>(
    env: Env<'a>,
    code: String,
    content: String,
    options: Term<'a>,
) -> Result<Term<'a>, Error> {
    // Parse options from Elixir map
    let opts: Options = options.decode().unwrap_or_default();
    // Create engine and load builtin modules
    let mut engine = mq_lang::DefaultEngine::default();
    engine.load_builtin_module();

    // Parse input based on format
    let input = match opts.input_format {
        InputFormat::Markdown => mq_lang::parse_markdown_input(&content),
        InputFormat::Mdx => mq_lang::parse_mdx_input(&content),
        InputFormat::Text => mq_lang::parse_text_input(&content),
        InputFormat::Html => mq_lang::parse_html_input(&content),
        InputFormat::Raw => Ok(mq_lang::raw_input(&content)),
        InputFormat::Null => Ok(mq_lang::null_input()),
    }
    .map_err(|e| Error::Term(Box::new(format!("Error parsing input: {}", e))))?;

    // Execute query
    let values = engine
        .eval(&code, input.into_iter())
        .map_err(|e| Error::Term(Box::new(format!("Error evaluating query: {}", e))))?;

    // Convert to MqResult
    let result = MqResult::new(values.into_iter().map(MqValue::from).collect());

    // Encode and return as {:ok, result}
    Ok((atoms::ok(), result).encode(env))
}

/// Convert HTML to Markdown
#[rustler::nif]
fn html_to_markdown(content: String, options: Term) -> Result<String, Error> {
    // Parse conversion options
    let opts: ConversionOptions = options.decode().unwrap_or_default();
    // Convert HTML to Markdown
    let markdown = mq_markdown::convert_html_to_markdown(
        &content,
        mq_markdown::ConversionOptions {
            extract_scripts_as_code_blocks: opts.extract_scripts_as_code_blocks,
            generate_front_matter: opts.generate_front_matter,
            use_title_as_h1: opts.use_title_as_h1,
        },
    )
    .map_err(|e| {
        Error::Term(Box::new(format!(
            "Error converting HTML to Markdown: {}",
            e
        )))
    })?;

    Ok(markdown)
}

rustler::init!("Elixir.Mq.Native");
```

## File: `native/mq_nif/src/result.rs`
```rust
use rustler::{Encoder, Env, Term};

use crate::{atoms, value::MqValue};

/// Result of an mq query execution
#[derive(Debug, Clone)]
pub struct MqResult {
    pub values: Vec<MqValue>,
}

impl MqResult {
    /// Create a new MqResult from a vector of values
    pub fn new(values: Vec<MqValue>) -> Self {
        Self { values }
    }

    /// Get the text representation of all values joined by newlines
    pub fn text(&self) -> String {
        self.values
            .iter()
            .filter(|v| !v.is_empty())
            .map(|v| v.text())
            .collect::<Vec<String>>()
            .join("\n")
    }

    /// Get the filtered values (non-empty)
    pub fn filtered_values(&self) -> Vec<String> {
        self.values
            .iter()
            .filter(|v| !v.is_empty())
            .map(|v| v.text())
            .collect()
    }
}

impl Encoder for MqResult {
    fn encode<'a>(&self, env: Env<'a>) -> Term<'a> {
        // Create an Elixir map with :values and :text keys
        let values_list = self.filtered_values();
        let text_string = self.text();

        // Build map manually using rustler's map_new
        let map = Term::map_new(env);
        let map = map
            .map_put(atoms::values().encode(env), values_list.encode(env))
            .expect("Failed to add values key");
        map.map_put(atoms::text().encode(env), text_string.encode(env))
            .expect("Failed to add text key")
    }
}
```

## File: `native/mq_nif/src/value.rs`
```rust
use rustler::{Encoder, Env, Term};
use std::collections::HashMap;

/// Value representation for mq results
#[derive(Debug, Clone)]
pub enum MqValue {
    Array(Vec<MqValue>),
    Dict(HashMap<String, MqValue>),
    Markdown { text: String },
}

impl MqValue {
    pub fn is_empty(&self) -> bool {
        match self {
            MqValue::Array(arr) => arr.is_empty(),
            MqValue::Dict(dict) => dict.is_empty(),
            MqValue::Markdown { text } => text.is_empty(),
        }
    }

    pub fn text(&self) -> String {
        match self {
            MqValue::Array(arr) => arr
                .iter()
                .map(|v| v.text())
                .collect::<Vec<String>>()
                .join("\n"),
            MqValue::Dict(dict) => dict
                .iter()
                .map(|(k, v)| format!("{}: {}", k, v.text()))
                .collect::<Vec<String>>()
                .join("\n"),
            MqValue::Markdown { text } => text.clone(),
        }
    }
}

impl Encoder for MqValue {
    fn encode<'a>(&self, env: Env<'a>) -> Term<'a> {
        match self {
            MqValue::Array(arr) => arr.encode(env),
            MqValue::Dict(dict) => dict.encode(env),
            MqValue::Markdown { text } => {
                // Return string for simple cases
                text.encode(env)
            }
        }
    }
}

impl From<mq_lang::RuntimeValue> for MqValue {
    fn from(value: mq_lang::RuntimeValue) -> Self {
        match value {
            mq_lang::RuntimeValue::Array(arr) => {
                MqValue::Array(arr.into_iter().map(|v| v.into()).collect())
            }
            mq_lang::RuntimeValue::Dict(map) => MqValue::Dict(
                map.into_iter()
                    .map(|(k, v)| (k.as_str().to_string(), v.into()))
                    .collect(),
            ),
            mq_lang::RuntimeValue::Markdown(node, _) => MqValue::Markdown {
                text: node.to_string(),
            },
            mq_lang::RuntimeValue::String(s) => MqValue::Markdown { text: s },
            mq_lang::RuntimeValue::Symbol(sym) => MqValue::Markdown {
                text: sym.as_str().to_string(),
            },
            mq_lang::RuntimeValue::Number(n) => MqValue::Markdown {
                text: n.to_string(),
            },
            mq_lang::RuntimeValue::Boolean(b) => MqValue::Markdown {
                text: b.to_string(),
            },
            mq_lang::RuntimeValue::Function(..)
            | mq_lang::RuntimeValue::NativeFunction(..)
            | mq_lang::RuntimeValue::Module(..)
            | mq_lang::RuntimeValue::Ast(_)
            | mq_lang::RuntimeValue::None => MqValue::Markdown {
                text: String::new(),
            },
        }
    }
}
```

## File: `test/mq_test.exs`
```
defmodule MqTest do
  use ExUnit.Case, async: true
  doctest Mq

  describe "run/3" do
    test "extracts h1 headings" do
      content = "# Hello World\n\n## Heading2\n\nText"
      assert {:ok, result} = Mq.run(".h1", content)
      assert result.values == ["# Hello World"]
      assert result.text == "# Hello World"
    end

    test "extracts h2 headings" do
      content = "# Hello World\n\n## Heading2\n\nText"
      assert {:ok, result} = Mq.run(".h2", content)
      assert result.values == ["## Heading2"]
    end

    test "extracts multiple h2 headings" do
      content = "# Main Title\n\n## Heading2A\n\nText\n\n## Heading2B\n\nMore text"
      assert {:ok, result} = Mq.run(".h2", content)
      assert result.values == ["## Heading2A", "## Heading2B"]
    end

    test "filters headings with select" do
      content = "# Product\n\n## Features\n\nText\n\n## Installation\n\nMore text"
      assert {:ok, result} = Mq.run(".h2 | select(contains(\"Feature\"))", content)
      assert result.values == ["## Features"]
    end

    test "extracts list items" do
      content = "# List\n\n- Item 1\n- Item 2\n- Item 3"
      assert {:ok, result} = Mq.run(".[]", content)
      assert result.values == ["- Item 1", "- Item 2", "- Item 3"]
    end

    test "extracts code blocks" do
      content = "# Code\n\n```python\nprint('Hello')\n```"
      assert {:ok, result} = Mq.run(".code", content)
      assert result.values == ["```python\nprint('Hello')\n```"]
    end
  end

  describe "run/3 with different input formats" do
    test "processes TEXT format" do
      options = %Mq.Options{input_format: :text}
      content = "Line 1\nLine 2\nLine 3"
      assert {:ok, result} = Mq.run("select(contains(\"2\"))", content, options)
      assert result.values == ["Line 2"]
    end

    test "processes MDX format" do
      options = %Mq.Options{input_format: :mdx}
      content = "# MDX Content\n\n<Component />"
      assert {:ok, result} = Mq.run("select(is_mdx())", content, options)
      assert result.values == ["<Component />"]
    end

    test "processes HTML format" do
      options = %Mq.Options{input_format: :html}
      content = "<h1>Hello</h1><p>World</p>"
      assert {:ok, result} = Mq.run("select(contains(\"Hello\"))", content, options)
      assert result.values == ["# Hello"]
    end
  end

  describe "run/3 with invalid queries" do
    test "returns error for invalid syntax" do
      assert {:error, reason} = Mq.run(".invalid_selector!!!", "# Heading")
      assert reason =~ "Error evaluating query"
    end
  end

  describe "html_to_markdown/2" do
    test "converts HTML to Markdown" do
      html_content = "<h1>Hello World</h1><p>This is a <strong>test</strong>.</p>"
      expected_markdown = "# Hello World\n\nThis is a **test**."
      assert {:ok, markdown} = Mq.html_to_markdown(html_content)
      assert String.trim(markdown) == expected_markdown
    end

    test "converts HTML with options" do
      html_content =
        "<html><head><title>Page Title</title></head><body><h1>Content</h1></body></html>"

      options = %Mq.ConversionOptions{use_title_as_h1: true}

      assert {:ok, markdown} = Mq.html_to_markdown(html_content, options)
      assert markdown =~ "# Page Title"
    end

    test "handles empty HTML" do
      assert {:ok, markdown} = Mq.html_to_markdown("")
      assert markdown == ""
    end
  end

  describe "Mq.Result" do
    test "implements Enumerable protocol" do
      {:ok, result} = Mq.run(".h", "# H1\n## H2\n### H3")

      assert Enum.count(result) == 3
      assert Enum.member?(result, "# H1")
      assert Enum.at(result, 0) == "# H1"
    end

    test "implements String.Chars protocol" do
      {:ok, result} = Mq.run(".h1", "# Title")
      assert to_string(result) == "# Title"
    end

    test "length/1 returns correct count" do
      {:ok, result} = Mq.run(".h", "# H1\n## H2")
      assert Mq.Result.length(result) == 2
    end

    test "empty?/1 checks for empty results" do
      {:ok, result} = Mq.run(".h1", "No headings here")
      assert Mq.Result.empty?(result)
    end
  end

  describe "Mq.Options" do
    test "to_map/1 converts struct to map" do
      options = %Mq.Options{input_format: :markdown}
      map = Mq.Options.to_map(options)

      assert map == %{input_format: :markdown}
    end

    test "to_map/1 removes nil values" do
      options = %Mq.Options{input_format: :markdown}
      map = Mq.Options.to_map(options)

      refute Map.has_key?(map, :list_style)
    end
  end

  describe "Mq.InputFormat" do
    test "all/0 returns all formats" do
      formats = Mq.InputFormat.all()
      assert :markdown in formats
      assert :mdx in formats
      assert length(formats) == 6
    end

    test "valid?/1 validates formats" do
      assert Mq.InputFormat.valid?(:markdown)
      refute Mq.InputFormat.valid?(:invalid)
    end
  end
end
```

## File: `test/test_helper.exs`
```
ExUnit.start()
```

