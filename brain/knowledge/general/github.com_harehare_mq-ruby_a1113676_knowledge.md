---
id: github.com-harehare-mq-ruby-a1113676-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.704061
---

# KNOWLEDGE EXTRACT: github.com_harehare_mq-ruby_a1113676
> **Extracted on:** 2026-04-01 07:55:47
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519276/github.com_harehare_mq-ruby_a1113676

---

## File: `.gitignore`
```
# Rust
/target/
Cargo.lock
**/*.rs.bk

# Ruby
*.gem
*.rbc
/.config
/coverage/
/InstalledFiles
/pkg/
/spec/reports/
/spec/examples.txt
/test/tmp/
/test/version_tmp/
/tmp/
.bundle/
lib/bundler/man/
vendor/bundle

# RSpec
.rspec_status

# Build artifacts
/lib/**/*.so
/lib/**/*.bundle
/ext/**/*.o
/ext/**/*.so
/ext/**/*.bundle
/ext/**/Makefile

# IDE
.idea/
.vscode/
*.swp
*.swo
*~
.DS_Store
```

## File: `.rspec`
```
--require spec_helper
--color
--format documentation
```

## File: `Cargo.toml`
```
[package]
authors = ["Takahiro Sato <harehare1110@gmail.com>"]
categories = ["command-line-utilities", "text-processing"]
description = "Ruby bindings for mq Markdown processing"
edition = "2024"
homepage = "https://mqlang.org/"
keywords = ["markdown", "jq", "query", "ruby"]
license = "MIT"
name = "mq-ruby"
publish = false
readme = "README.md"
repository = "https://github.com/harehare/mq"
version = "0.1.15"

[lib]
crate-type = ["cdylib"]
name = "mq_ruby"

[dependencies]
magnus = {version = "0.8"}
mq-lang = "0.5.24"
mq-markdown = "0.5.24"

```

## File: `Gemfile`
```
# frozen_string_literal: true

source "https://rubygems.org"

gemspec

gem "rake", "~> 13.0"
gem "rspec", "~> 3.0"
gem "rake-compiler", "~> 1.2"
gem "rb_sys", "~> 0.9"
```

## File: `Gemfile.lock`
```
PATH
  remote: .
  specs:
    mq-ruby (0.1.15)

GEM
  remote: https://rubygems.org/
  specs:
    diff-lcs (1.6.2)
    rake (13.3.1)
    rake-compiler (1.3.1)
      rake
    rake-compiler-dock (1.11.0)
    rb_sys (0.9.124)
      rake-compiler-dock (= 1.11.0)
    rspec (3.13.2)
      rspec-core (~> 3.13.0)
      rspec-expectations (~> 3.13.0)
      rspec-mocks (~> 3.13.0)
    rspec-core (3.13.6)
      rspec-support (~> 3.13.0)
    rspec-expectations (3.13.5)
      diff-lcs (>= 1.2.0, < 2.0)
      rspec-support (~> 3.13.0)
    rspec-mocks (3.13.7)
      diff-lcs (>= 1.2.0, < 2.0)
      rspec-support (~> 3.13.0)
    rspec-support (3.13.6)

PLATFORMS
  arm64-darwin-25
  ruby

DEPENDENCIES
  mq-ruby!
  rake (~> 13.0)
  rake-compiler (~> 1.2)
  rb_sys (~> 0.9)
  rspec (~> 3.0)

BUNDLED WITH
   2.6.9
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
<h1 align="center">mq-ruby</h1>

[![Gem Version](https://badge.fury.io/rb/mq-ruby.svg)](https://badge.fury.io/rb/mq-ruby)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ruby bindings for [mq](https://mqlang.org/), a jq-like command-line tool for processing Markdown.

## Ruby API

Once complete, the Ruby API will look like this:

```ruby
require 'mq'

# Basic usage
markdown = <<~MD
  # Main Title
  ## Section 1
  Some content here.
  ## Section 2
  More content.
MD

result = MQ.run('.h2', markdown)
result.values.each do |heading|
  puts heading
end
# => ## Section 1
# => ## Section 2

# With options
options = MQ::Options.new
options.input_format = MQ::InputFormat::HTML

result = MQ.run('.h1', '<h1>Hello</h1><p>World</p>', options)
puts result.text  # => # Hello

# HTML to Markdown conversion
html = '<h1>Title</h1><p>Paragraph</p>'
markdown = MQ.html_to_markdown(html)
puts markdown  # => # Title\n\nParagraph
```

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Links

- [mq Website](https://mqlang.org/)
- [GitHub Repository](https://github.com/harehare/mq)
- [Command-line Tool](https://github.com/harehare/mq#installation)
```

## File: `Rakefile`
```
# frozen_string_literal: true

require "bundler/gem_tasks"
require "rspec/core/rake_task"
require "shellwords"

RSpec::Core::RakeTask.new(:spec)

task default: %i[compile spec]

desc "Compile the Rust extension"
task :compile do
  # Set up Ruby environment for linking
  require "rbconfig"

  profile = ENV.fetch("CARGO_PROFILE", "release")
  manifest_path = File.join(__dir__, "Cargo.toml")
  lib_dir = File.join(__dir__, "lib", "mq")
  FileUtils.mkdir_p(lib_dir)

  sh "cargo build --manifest-path #{manifest_path} --release"

  # Find the built library
  target_dir = File.join(__dir__, "target", profile)
  ext_name = RbConfig::CONFIG["DLEXT"]

  # Copy the library to lib/mq
  found = false
  Dir.glob(File.join(target_dir, "libmq_ruby.{so,dylib,dll}")).each do |lib|
    dest = File.join(lib_dir, "mq_ruby.#{ext_name}")
    FileUtils.cp(lib, dest)
    puts "Copied #{lib} to #{dest}"
    found = true
  end

  unless found
    warn "Warning: Could not find compiled library"
  end
end

desc "Clean build artifacts"
task :clean do
  sh "cargo clean --manifest-path #{__dir__}/Cargo.toml" rescue nil
  FileUtils.rm_f(Dir.glob("lib/mq/*.{so,dylib,dll,bundle}"))
end

task clobber: :clean

desc "Build the gem"
task build: :compile do
  sh "gem build mq-ruby.gemspec"
end

desc "Install the gem locally"
task install: :build do
  sh "gem install mq-ruby-0.5.9.gem"
end
```

## File: `build.rs`
```rust
use std::process::Command;

fn main() {
    // Get Ruby library directory
    let libdir = Command::new("ruby")
        .args(["-e", "puts RbConfig::CONFIG['libdir']"])
        .output()
        .expect("Failed to execute ruby command")
        .stdout;
    let libdir = String::from_utf8(libdir).unwrap().trim().to_string();

    // Get Ruby library name
    let libruby = Command::new("ruby")
        .args(["-e", "puts RbConfig::CONFIG['LIBRUBY']"])
        .output()
        .expect("Failed to execute ruby command")
        .stdout;
    let libruby = String::from_utf8(libruby).unwrap().trim().to_string();

    // Remove 'lib' prefix and '.dylib'/'.so' suffix to get the library name
    let lib_name = libruby.strip_prefix("lib").unwrap_or(&libruby);

    // Remove .dylib, .so, or .so.* (versioned shared library)
    let lib_name = if let Some(pos) = lib_name.find(".dylib") {
        &lib_name[..pos]
    } else if let Some(pos) = lib_name.find(".so") {
        &lib_name[..pos]
    } else {
        lib_name
    };

    // Output linker directives
    println!("cargo:rustc-link-search=native={}", libdir);
    println!("cargo:rustc-link-lib=dylib={}", lib_name);

    // Rerun if Ruby changes
    println!("cargo:rerun-if-env-changed=RUBY");
    println!("cargo:rerun-if-env-changed=RUBY_ROOT");
}
```

## File: `extconf.rb`
```ruby
# frozen_string_literal: true

require "mkmf"
require "rb_sys/mkmf"

create_rust_makefile("mq/mq_ruby")
```

## File: `mq-ruby.gemspec`
```
# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name = "mq-ruby"
  spec.version = "0.1.15"
  spec.authors = ["Takahiro Sato"]

  spec.summary = "Ruby bindings for mq Markdown processing"
  spec.description = "mq is a jq-like command-line tool for Markdown processing. This gem provides Ruby bindings for mq."
  spec.homepage = "https://mqlang.org/"
  spec.license = "MIT"
  spec.required_ruby_version = ">= 3.0.0"

  spec.metadata["homepage_uri"] = spec.homepage
  spec.metadata["source_code_uri"] = "https://github.com/harehare/mq-ruby"
  spec.extensions = ["extconf.rb"]

  spec.files = Dir[
    "lib/**/*.rb",
    "ext/**/*.{rs,toml,rb}",
    "src/**/*.rs",
    "Cargo.toml",
    "Cargo.lock",
    "README.md",
    "CHANGELOG.md",
    "LICENSE"
  ]

  spec.require_paths = ["lib"]

  spec.add_development_dependency "rake", "~> 13.0"
  spec.add_development_dependency "rspec", "~> 3.0"
  spec.add_development_dependency "rake-compiler", "~> 1.2"
  spec.add_development_dependency "rb_sys", "~> 0.9"
end
```

## File: `lib/mq.rb`
```ruby
# frozen_string_literal: true

begin
  # Try to load the compiled extension
  RUBY_VERSION =~ /(\d+\.\d+)/
  require_relative "mq/#{Regexp.last_match(1)}/mq_ruby"
rescue LoadError
  require_relative "mq/mq_ruby"
end

module MQ
  class Error < StandardError; end

  # Options class for configuring mq queries
  class Options
    attr_accessor :input_format

    def initialize
      @input_format = nil
    end

    def to_h
      {
        input_format: @input_format,
      }.compact
    end
  end

  # Conversion options for HTML to Markdown conversion
  class ConversionOptions
    attr_accessor :extract_scripts_as_code_blocks, :generate_front_matter, :use_title_as_h1

    def initialize
      @extract_scripts_as_code_blocks = false
      @generate_front_matter = false
      @use_title_as_h1 = false
    end

    def to_h
      {
        extract_scripts_as_code_blocks: @extract_scripts_as_code_blocks,
        generate_front_matter: @generate_front_matter,
        use_title_as_h1: @use_title_as_h1
      }
    end
  end

  class << self
    # Run an mq query on the provided content
    #
    # @param code [String] The mq query string
    # @param content [String] The markdown/HTML/text content to process
    # @param options [Options, nil] Optional configuration options
    # @return [Result] The query results
    def run(code, content, options = nil)
      options_hash = options&.to_h
      _run(code, content, options_hash)
    end

    # Convert HTML to Markdown
    #
    # @param content [String] The HTML content to convert
    # @param options [ConversionOptions, nil] Optional conversion options
    # @return [String] The converted Markdown
    def html_to_markdown(content, options = nil)
      options_hash = options&.to_h
      _html_to_markdown(content, options_hash)
    end
  end
end
```

## File: `spec/mq_spec.rb`
```ruby
# frozen_string_literal: true

require "spec_helper"

RSpec.describe MQ do
  describe ".run" do
    context "with basic markdown queries" do
      it "extracts h1 headings" do
        content = "# Hello World\n\n## Heading2\n\nText"
        result = MQ.run(".h1", content, nil)
        expect(result.values).to eq(["# Hello World"])
      end

      it "extracts h2 headings" do
        content = "# Hello World\n\n## Heading2\n\nText"
        result = MQ.run(".h2", content, nil)
        expect(result.values).to eq(["## Heading2"])
      end

      it "extracts multiple h2 headings" do
        content = "# Main Title\n\n## Heading2A\n\nText\n\n## Heading2B\n\nMore text"
        result = MQ.run(".h2", content, nil)
        expect(result.values).to eq(["## Heading2A", "## Heading2B"])
      end

      it "filters headings with select" do
        content = "# Product\n\n## Features\n\nText\n\n## Installation\n\nMore text"
        result = MQ.run('.h2 | select(contains("Feature"))', content, nil)
        expect(result.values).to eq(["## Features"])
      end

      it "extracts list items" do
        content = "# List\n\n- Item 1\n- Item 2\n- Item 3"
        result = MQ.run(".[]", content, nil)
        expect(result.values).to eq(["- Item 1", "- Item 2", "- Item 3"])
      end

      it "extracts code blocks" do
        content = "# Code\n\n```python\nprint('Hello')\n```"
        result = MQ.run(".code", content, nil)
        expect(result.values).to eq(["```python\nprint('Hello')\n```"])
      end
    end

    context "with different input formats" do
      it "processes TEXT format" do
        options = MQ::Options.new
        options.input_format = MQ::InputFormat::TEXT

        content = "Line 1\nLine 2\nLine 3"
        result = MQ.run('select(contains("2"))', content, options)
        expect(result.values).to eq(["Line 2"])
      end

      it "processes MDX format" do
        options = MQ::Options.new
        options.input_format = MQ::InputFormat::MDX

        content = "# MDX Content\n\n<Component />"
        result = MQ.run("select(is_mdx())", content, options)
        expect(result.values).to eq(["<Component />"])
      end

      it "processes HTML format" do
        options = MQ::Options.new
        options.input_format = MQ::InputFormat::HTML

        content = "<h1>Hello</h1><p>World</p>"
        result = MQ.run('select(contains("Hello"))', content, options)
        expect(result.values).to eq(["# Hello"])
      end
    end

    context "with invalid queries" do
      it "raises an error for invalid syntax" do
        expect {
          MQ.run(".invalid_selector!!!", "# Heading", nil)
        }.to raise_error(RuntimeError, /Error evaluating query/)
      end
    end
  end

  describe ".html_to_markdown" do
    it "converts HTML to Markdown" do
      html_content = "<h1>Hello World</h1><p>This is a <strong>test</strong>.</p>"
      expected_markdown = "# Hello World\n\nThis is a **test**."
      markdown = MQ.html_to_markdown(html_content, nil)
      expect(markdown.strip).to eq(expected_markdown)
    end

    it "converts HTML with options" do
      html_content = "<html><head><title>Page Title</title></head><body><h1>Content</h1></body></html>"

      options = MQ::ConversionOptions.new
      options.use_title_as_h1 = true

      markdown = MQ.html_to_markdown(html_content, options)
      expect(markdown).to include("# Page Title")
    end
  end

  describe MQ::Result do
    let(:content) { "# Title\n\n## Section 1\n\n## Section 2" }
    let(:result) { MQ.run(".h2", content, nil) }

    describe "#text" do
      it "returns text representation" do
        expect(result.text).to eq("## Section 1\n## Section 2")
      end
    end

    describe "#values" do
      it "returns array of values" do
        expect(result.values).to eq(["## Section 1", "## Section 2"])
      end
    end

    describe "#length" do
      it "returns the number of values" do
        expect(result.length).to eq(3)
      end
    end

    describe "#[]" do
      it "accesses values by index" do
        expect(result[1]).to eq("## Section 1")
        expect(result[2]).to eq("## Section 2")
      end

      it "raises error for out of range index" do
        expect { result[10] }.to raise_error
      end
    end

    describe "#each" do
      it "iterates over values" do
        values = []
        result.each { |v| values << v }
        expect(values).to eq(["", "## Section 1", "## Section 2"])
      end
    end
  end

  describe "InputFormat constants" do
    it "defines all input format constants" do
      expect(MQ::InputFormat::MARKDOWN).to eq(0)
      expect(MQ::InputFormat::MDX).to eq(1)
      expect(MQ::InputFormat::TEXT).to eq(2)
      expect(MQ::InputFormat::HTML).to eq(3)
      expect(MQ::InputFormat::RAW).to eq(4)
      expect(MQ::InputFormat::NULL).to eq(5)
    end
  end

  describe MQ::Options do
    it "can be instantiated with default values" do
      options = MQ::Options.new
      expect(options.input_format).to be_nil
    end

    it "allows setting input format" do
      options = MQ::Options.new
      options.input_format = MQ::InputFormat::TEXT
      expect(options.input_format).to eq(MQ::InputFormat::TEXT)
    end
  end

  describe MQ::ConversionOptions do
    it "can be instantiated with default values" do
      options = MQ::ConversionOptions.new
      expect(options.extract_scripts_as_code_blocks).to be false
      expect(options.generate_front_matter).to be false
      expect(options.use_title_as_h1).to be false
    end

    it "allows setting options" do
      options = MQ::ConversionOptions.new
      options.extract_scripts_as_code_blocks = true
      options.generate_front_matter = true
      options.use_title_as_h1 = true

      expect(options.extract_scripts_as_code_blocks).to be true
      expect(options.generate_front_matter).to be true
      expect(options.use_title_as_h1).to be true
    end
  end
end
```

## File: `spec/spec_helper.rb`
```ruby
# frozen_string_literal: true

require "bundler/setup"

# Load the compiled extension
begin
  require "mq"
rescue LoadError
  # If the extension isn't built yet, provide a helpful message
  warn "WARNING: mq extension not loaded. Run 'rake compile' first."
end

RSpec.configure do |config|
  # Enable flags like --only-failures and --next-failure
  config.example_status_persistence_file_path = ".rspec_status"

  # Disable RSpec exposing methods globally on `Module` and `main`
  config.disable_monkey_patching!

  config.expect_with :rspec do |c|
    c.syntax = :expect
  end
end
```

## File: `src/lib.rs`
```rust
//! Ruby bindings for the mq markdown processing library.
//!
//! This crate provides Ruby bindings for mq, allowing Ruby applications to
//! process markdown, MDX, and HTML using the mq query language.

pub mod result;
pub mod value;

use magnus::{Error, RHash, Ruby, TryConvert, function, prelude::*};
use result::MQResult;
use value::InputFormat;

/// Main entry point for the Ruby extension
#[magnus::init]
fn init(ruby: &Ruby) -> Result<(), Error> {
    let mq_module = ruby.define_module("MQ")?;

    // Define input format constants
    InputFormat::define_constants(ruby, mq_module)?;

    // Define result class
    MQResult::define_class(ruby, mq_module)?;

    // Define module functions
    mq_module.define_singleton_method("_run", function!(run, 3))?;
    mq_module.define_singleton_method("_html_to_markdown", function!(html_to_markdown, 2))?;

    Ok(())
}

/// Run an mq query on the provided content
fn run(code: String, content: String, options_hash: Option<RHash>) -> Result<MQResult, Error> {
    let ruby = Ruby::get().unwrap();
    let mut engine = mq_lang::DefaultEngine::default();
    engine.load_builtin_module();

    // Parse options from hash
    let input_format = if let Some(opts) = options_hash {
        if let Some(val) = opts.get(ruby.to_symbol("input_format")) {
            let format_val: i32 = TryConvert::try_convert(val)?;
            InputFormat::from_i32(format_val)
        } else {
            InputFormat::Markdown
        }
    } else {
        InputFormat::Markdown
    };

    let input = match input_format {
        InputFormat::Markdown => mq_lang::parse_markdown_input(&content),
        InputFormat::Mdx => mq_lang::parse_mdx_input(&content),
        InputFormat::Text => mq_lang::parse_text_input(&content),
        InputFormat::Html => mq_lang::parse_html_input(&content),
        InputFormat::Raw => Ok(mq_lang::raw_input(&content)),
        InputFormat::Null => Ok(mq_lang::null_input()),
    }
    .map_err(|e| {
        Error::new(
            ruby.exception_runtime_error(),
            format!("Error parsing input: {}", e),
        )
    })?;

    engine
        .eval(&code, input.into_iter())
        .map(|values| MQResult::from(values.into_iter().map(Into::into).collect::<Vec<_>>()))
        .map_err(|e| {
            Error::new(
                ruby.exception_runtime_error(),
                format!("Error evaluating query: {}", e),
            )
        })
}

/// Convert HTML to Markdown
fn html_to_markdown(content: String, options_hash: Option<RHash>) -> Result<String, Error> {
    let ruby = Ruby::get().unwrap();
    let opts = if let Some(opts) = options_hash {
        let extract_scripts = get_bool_option(&ruby, &opts, "extract_scripts_as_code_blocks")?;
        let generate_front = get_bool_option(&ruby, &opts, "generate_front_matter")?;
        let use_title = get_bool_option(&ruby, &opts, "use_title_as_h1")?;

        mq_markdown::ConversionOptions {
            extract_scripts_as_code_blocks: extract_scripts,
            generate_front_matter: generate_front,
            use_title_as_h1: use_title,
        }
    } else {
        mq_markdown::ConversionOptions::default()
    };

    mq_markdown::convert_html_to_markdown(&content, opts).map_err(|e| {
        Error::new(
            ruby.exception_runtime_error(),
            format!("Error converting HTML to Markdown: {}", e),
        )
    })
}

fn get_bool_option(ruby: &Ruby, hash: &RHash, key: &str) -> Result<bool, Error> {
    if let Some(val) = hash.get(ruby.to_symbol(key)) {
        TryConvert::try_convert(val)
    } else {
        Ok(false)
    }
}
```

## File: `src/result.rs`
```rust
use crate::value::MQValue;
use magnus::{DataTypeFunctions, Error, RModule, Ruby, TypedData, Value, method, prelude::*};

/// Result of an mq query execution
#[derive(Debug, Clone, TypedData)]
#[magnus(class = "MQ::Result", free_immediately, mark)]
pub struct MQResult {
    pub values: Vec<MQValue>,
}

impl DataTypeFunctions for MQResult {}

impl MQResult {
    /// Define the MQResult class in Ruby
    pub fn define_class(ruby: &Ruby, mq_module: RModule) -> Result<(), Error> {
        let class = mq_module.define_class("Result", ruby.class_object())?;
        class.define_method("text", method!(MQResult::text, 0))?;
        class.define_method("values", method!(MQResult::values_as_strings, 0))?;
        class.define_method("length", method!(MQResult::len, 0))?;
        class.define_method("[]", method!(MQResult::get_at, 1))?;
        class.define_method("each", method!(MQResult::each, 0))?;
        Ok(())
    }

    /// Get the text representation of all values joined by newlines
    pub fn text(&self) -> String {
        self.values
            .iter()
            .filter_map(|value| {
                if value.is_empty() {
                    None
                } else {
                    Some(value.text())
                }
            })
            .collect::<Vec<String>>()
            .join("\n")
    }

    /// Get an array of text values
    pub fn values_as_strings(&self) -> Vec<String> {
        self.values
            .iter()
            .filter_map(|value| {
                if value.is_empty() {
                    None
                } else {
                    Some(value.text())
                }
            })
            .collect()
    }

    /// Get the number of values
    pub fn len(&self) -> usize {
        self.values.len()
    }

    /// Check if the result is empty
    pub fn is_empty(&self) -> bool {
        self.values.is_empty()
    }

    /// Access a value by index (for Ruby)
    fn get_at(&self, idx: usize) -> Result<String, Error> {
        if idx < self.values.len() {
            Ok(self.values[idx].text())
        } else {
            let ruby = Ruby::get().unwrap();
            Err(Error::new(
                ruby.exception_runtime_error(),
                format!(
                    "Index {} out of range for MQResult with length {}",
                    idx,
                    self.len()
                ),
            ))
        }
    }

    /// Iterator for Ruby each method
    fn each(&self) -> Result<Value, Error> {
        let ruby = Ruby::get().unwrap();
        let block = ruby.block_proc()?;

        for value in &self.values {
            let text = value.text();
            block.call::<(String,), Value>((text,))?;
        }

        Ok(ruby.qnil().as_value())
    }
}

impl From<Vec<MQValue>> for MQResult {
    fn from(values: Vec<MQValue>) -> Self {
        Self { values }
    }
}
```

## File: `src/value.rs`
```rust
use magnus::{Error, Module, RModule, Ruby};
use std::{collections::HashMap, fmt};

#[derive(Debug, Clone, Copy, PartialEq, Default)]
pub enum InputFormat {
    #[default]
    Markdown,
    Mdx,
    Text,
    Html,
    Raw,
    Null,
}

impl InputFormat {
    pub fn define_constants(ruby: &Ruby, mq_module: RModule) -> Result<(), Error> {
        let class = ruby.define_class("InputFormat", ruby.class_object())?;
        mq_module.const_set("InputFormat", class)?;
        class.const_set("MARKDOWN", 0)?;
        class.const_set("MDX", 1)?;
        class.const_set("TEXT", 2)?;
        class.const_set("HTML", 3)?;
        class.const_set("RAW", 4)?;
        class.const_set("NULL", 5)?;
        Ok(())
    }

    pub fn from_i32(val: i32) -> Self {
        match val {
            0 => InputFormat::Markdown,
            1 => InputFormat::Mdx,
            2 => InputFormat::Text,
            3 => InputFormat::Html,
            4 => InputFormat::Raw,
            5 => InputFormat::Null,
            _ => InputFormat::Markdown, // Default
        }
    }
}

#[derive(Debug, Clone)]
pub enum MQValue {
    Array { value: Vec<MQValue> },
    Dict { value: HashMap<String, MQValue> },
    Markdown { value: String },
}

impl fmt::Display for MQValue {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            MQValue::Array { value } => write!(
                f,
                "{}",
                value
                    .iter()
                    .map(|val| val.text())
                    .collect::<Vec<String>>()
                    .join("\n")
            ),
            MQValue::Dict { value } => write!(
                f,
                "{}",
                value
                    .iter()
                    .map(|(k, v)| format!("{}: {}", k, v.text()))
                    .collect::<Vec<String>>()
                    .join("\n")
            ),
            MQValue::Markdown { value } => write!(f, "{}", value),
        }
    }
}

impl MQValue {
    pub fn text(&self) -> String {
        self.to_string()
    }

    pub fn is_empty(&self) -> bool {
        match self {
            MQValue::Array { value } => value.is_empty(),
            MQValue::Dict { value } => value.is_empty(),
            MQValue::Markdown { value } => value.is_empty(),
        }
    }
}

impl From<mq_lang::RuntimeValue> for MQValue {
    fn from(value: mq_lang::RuntimeValue) -> Self {
        match value {
            mq_lang::RuntimeValue::Array(arr) => MQValue::Array {
                value: arr.into_iter().map(|v| v.into()).collect(),
            },
            mq_lang::RuntimeValue::Dict(map) => MQValue::Dict {
                value: map
                    .into_iter()
                    .map(|(k, v)| (k.as_str(), v.into()))
                    .collect(),
            },
            mq_lang::RuntimeValue::Markdown(node, _) => MQValue::Markdown {
                value: node.to_string(),
            },
            mq_lang::RuntimeValue::String(s) => MQValue::Markdown { value: s },
            mq_lang::RuntimeValue::Symbol(i) => MQValue::Markdown { value: i.as_str() },
            mq_lang::RuntimeValue::Number(n) => MQValue::Markdown {
                value: n.to_string(),
            },
            mq_lang::RuntimeValue::Boolean(b) => MQValue::Markdown {
                value: b.to_string(),
            },
            mq_lang::RuntimeValue::Function(..)
            | mq_lang::RuntimeValue::NativeFunction(..)
            | mq_lang::RuntimeValue::Module(..) => MQValue::Markdown {
                value: "".to_string(),
            },
            mq_lang::RuntimeValue::Ast(_) => MQValue::Markdown {
                value: "".to_string(),
            },
            mq_lang::RuntimeValue::None => MQValue::Markdown {
                value: "".to_string(),
            },
        }
    }
}
```

