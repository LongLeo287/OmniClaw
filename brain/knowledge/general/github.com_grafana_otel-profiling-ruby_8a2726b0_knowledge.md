---
id: github.com-grafana-otel-profiling-ruby-8a2726b0-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:04.406746
---

# KNOWLEDGE EXTRACT: github.com_grafana_otel-profiling-ruby_8a2726b0
> **Extracted on:** 2026-04-01 16:49:54
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525353/github.com_grafana_otel-profiling-ruby_8a2726b0

---

## File: `.gitignore`
```
.idea/
/.bundle/
/.yardoc
/_yardoc/
/coverage/
/doc/
/pkg/
/spec/reports/
/tmp/
/vendor/
Gemfile.lock
.ruby-version
.ruby-gemset
# rspec failure tracking
.rspec_status
```

## File: `.rspec`
```
--format documentation
--color
--require spec_helper
```

## File: `.rubocop.yml`
```yaml
AllCops:
  TargetRubyVersion: 2.6

Style/StringLiterals:
  Enabled: true
  EnforcedStyle: double_quotes

Style/StringLiteralsInInterpolation:
  Enabled: true
  EnforcedStyle: double_quotes

Layout/LineLength:
  Max: 120
```

## File: `Gemfile`
```
# frozen_string_literal: true

source "https://rubygems.org"

# Specify your gem's dependencies in pyroscope-otel.gemspec
gemspec

gem "rake", "~> 13.0"

gem "rspec", "~> 3.0"

gem "rubocop", "~> 0.80"
```

## File: `LICENSE.txt`
```
The MIT License (MIT)

Copyright (c) 2022 Tolya Korniltsev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `README.md`
```markdown
# Pyroscope::Otel

Pyroscope can integrate with distributed tracing systems supporting OpenTelemetry standard which allows you to link traces with the profiling data, and find specific lines of code related to a performance issue.

For full documentation, refer to our [docs](https://grafana.com/docs/pyroscope/latest/configure-client/trace-span-profiles/ruby-span-profiles/).

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'pyroscope-otel'
```

And then execute:

    $ bundle install

Or install it yourself as:

    $ gem install pyroscope-otel

## Usage

```ruby
Pyroscope.configure do |config|
  # Configure pyroscope as described https://pyroscope.io/docs/ruby/
end

OpenTelemetry::SDK.configure do |config|
  config.add_span_processor Pyroscope::Otel::SpanProcessor.new(
    "#{app_name}.cpu", # your app name with ".cpu" suffix, for example rideshare-ruby.cpu
    pyroscope_endpoint # link to your pyroscope server, for example "http://localhost:4040"
  )
  # Configure the rest of opentelemetry as described  https://github.com/open-telemetry/opentelemetry-ruby
end
```

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
```

## File: `Rakefile`
```
# frozen_string_literal: true

require "bundler/gem_tasks"
require "rspec/core/rake_task"

RSpec::Core::RakeTask.new(:spec)

require "rubocop/rake_task"

RuboCop::RakeTask.new

task default: %i[spec rubocop]
```

## File: `pyroscope-otel.gemspec`
```
# frozen_string_literal: true

require_relative "lib/pyroscope/otel/version"

Gem::Specification.new do |spec|
  spec.name          = "pyroscope-otel"
  spec.version       = Pyroscope::Otel::VERSION
  spec.authors       = ["Tolyan Korniltsev"]
  spec.email         = ["anatoly@pyroscope.io"]

  spec.summary       = "Pyroscope OTEL integration"
  spec.description   = "Pyroscope OTEL integration"
  spec.homepage      = "https://pyroscope.io/"
  spec.license       = "MIT"
  spec.required_ruby_version = Gem::Requirement.new(">= 2.6.0")

  # spec.metadata["allowed_push_host"] = "TODO: Set to 'http://mygemserver.com'"

  spec.metadata["homepage_uri"] = spec.homepage
  spec.metadata["source_code_uri"] = "https://github.com/pyroscope-io/otel-profiling-ruby"
  spec.metadata["changelog_uri"] = "https://github.com/pyroscope-io/otel-profiling-ruby/CHANGELOG.md"

  # Specify which files should be added to the gem when it is released.
  # The `git ls-files -z` loads the files in the RubyGem that have been added into git.
  spec.files = Dir.chdir(File.expand_path(__dir__)) do
    `git ls-files -z`.split("\x0").reject { |f| f.match(%r{\A(?:test|spec|features)/}) }
  end
  spec.bindir        = "exe"
  spec.executables   = spec.files.grep(%r{\Aexe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.add_dependency "opentelemetry-api", "~> 1.1"
  spec.add_dependency "pyroscope", ">= 0.5.1", "< 1.0"
end
```

## File: `lib/pyroscope/otel.rb`
```ruby
# frozen_string_literal: true

require "pyroscope"
# require_relative "otel/version"
require "uri"

module Pyroscope
  module Otel
    class Error < StandardError; end

    # SpanProcessor annotates otel spans with profile_id, profile urls,
    # baseline urls
    class SpanProcessor
      ZERO_SPAN_ID = [0, 0, 0, 0, 0, 0, 0, 0].pack("C*")
      # pyroscope app name, including ".cpu" suffix.
      attr_accessor :app_name
      # http address of pyroscope server for span links
      attr_accessor :pyroscope_endpoint

      # boolean flag option to annotate spans with profile attributes only on root spans.
      attr_accessor :root_span_only
      # boolean flag option to annotate pyroscope profiles with span name
      attr_accessor :add_span_name
      # boolean flag option to add profiler url to span attributes
      attr_accessor :add_url

      # @param [String] app_name - pyroscope app name, including ".cpu" suffix.
      # @param [String] pyroscope_endpoint - http address of pyroscope server for span links.
      def initialize(app_name,
                     pyroscope_endpoint)
        @app_name = app_name
        @pyroscope_endpoint = URI.parse(pyroscope_endpoint)
        @root_span_only = true
        @add_span_name = true
        @add_url = true
      end

      def on_start(span, parent_context)
        return if @root_span_only && !root_span?(span, parent_context)

        profile_id = profile_id(span)

        labels = { "profile_id": profile_id }
        labels["span"] = span.name if @add_span_name

        Pyroscope._add_tags(Pyroscope.thread_id, labels)

        annotate_span(profile_id, span)
      rescue StandardError => e
        OpenTelemetry.handle_error(exception: e, message: "unexpected error in span.on_start")
      end

      def on_finish(span)
        profile_id = span.attributes["pyroscope.profile.id"]
        return if profile_id.nil?

        labels = { "profile_id": profile_id }
        labels["span"] = span.name if @add_span_name
        Pyroscope._remove_tags(Pyroscope.thread_id, labels)
      end

      def force_flush(*)
        OpenTelemetry::SDK::Trace::Export::SUCCESS
      end

      def shutdown(*)
        OpenTelemetry::SDK::Trace::Export::SUCCESS
      end

      private

      def root_span?(parent, parent_context)
        return true if parent.parent_span_id == ZERO_SPAN_ID

        parent = OpenTelemetry::Trace.current_span(parent_context)
        return false if parent.nil?

        parent.context.remote?
      rescue StandardError => _e
        false
      end

      def annotate_span(profile_id, span)
        span.set_attribute("pyroscope.profile.id", profile_id)
        span.set_attribute("pyroscope.profile.url", profile_url(profile_id)) if @add_url
      end

      def profile_id(span)
        span.context.span_id.unpack1("H*")
      end

      def profile_url(profile_id)
        url = @pyroscope_endpoint.clone
        from = Time.now.to_i
        to = from + 60 * 60
        url.query = URI.encode_www_form({
                                          "query": query(profile_id),
                                          "from": from,
                                          "until": to
                                        })
        url.to_s
      end

      def query(profile_id)
        "#{app_name}{profile_id=\"#{profile_id}\"}"
      end
    end
  end
end
```

## File: `lib/pyroscope/otel/version.rb`
```ruby
# frozen_string_literal: true

module Pyroscope
  module Otel
    VERSION = "0.1.4"
  end
end
```

## File: `spec/spec_helper.rb`
```ruby
# frozen_string_literal: true

require "pyroscope/otel"

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

## File: `spec/pyroscope/otel_spec.rb`
```ruby
# frozen_string_literal: true

RSpec.describe Pyroscope::Otel do
  it "has a version number" do
    expect(Pyroscope::Otel::VERSION).not_to be nil
  end
end
```

