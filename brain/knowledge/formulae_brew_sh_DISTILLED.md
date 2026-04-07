---
id: formulae.brew.sh
type: knowledge
owner: OA_Triage
---
# formulae.brew.sh
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Homebrew Formulae

[Homebrew Formulae](https://formulae.brew.sh) is an online package browser for [Homebrew](https://brew.sh).

It displays all packages in the [Homebrew/homebrew-core](https://github.com/Homebrew/homebrew-core) and [Homebrew/homebrew-cask](https://github.com/Homebrew/homebrew-cask). A [GitHub Action](https://github.com/Homebrew/formulae.brew.sh/blob/main/.github/workflows/tests.yml) is run periodically which pulls changes from each tap and deploys the site to GitHub Pages.

## JSON API

It also provides a JSON API for all packages (or individual packages) in each tap and their related analytics. This JSON data is used for the creation of the HTML resources on this site.

Currently available:

- List metadata for all formulae and casks
- Get metadata for each formula and cask
- List analytics events for all formulae and casks
- List analytics events for each formula and cask

Read more in the [JSON API documentation](https://formulae.brew.sh/docs/api/).

## Usage

Open <https://formulae.brew.sh/> in your web browser.

To instead run the site locally, run:

```bash
git clone https://github.com/Homebrew/formulae.brew.sh
cd formulae.brew.sh
brew generate-formula-api
brew generate-cask-api
brew generate-analytics-api
ruby script/generate-api-samples.rb
bundle install
bundle exec jekyll serve
```

## Search

Search is indexed by Algolia crawler at <https://crawler.algolia.com/admin/crawlers/26b9e6e2-bce4-4f42-9930-6b6ddf06cc9e/overview>.
This is only accessible by brew organisation members.

## License

Code is under the [BSD 2-clause "Simplified" License](LICENSE.txt).

```

### File: cask-font_index.html
```html
---
title: homebrew-cask
layout: default
permalink: /cask-font/
---
<p>This is a listing of all fonts available from the <a href="{{ site.taps.cask.remote }}">{{ site.taps.cask.repository }} tap</a> via the <a href="https://brew.sh">Homebrew</a> package manager for macOS.</p>

<h2><a href="{{ site.baseurl }}/api/cask.json"><code>/api/cask.json</code> (JSON API)</a></h2>

<table>
    {%- assign sorted_casks = site.data.cask | sort -%}
    {%- for cask in sorted_casks -%}
        {%- assign subfolder = cask[1].ruby_source_path | slice: 6, 4 -%}
        {%- if subfolder == "font" -%}
        <tr>
            {%- assign data_token = cask[0] -%}
            {%- assign token = cask[1].token -%}
            {%- include cask.html data_token=data_token token=token -%}
        </tr>
        {%- endif -%}
    {%- endfor -%}
</table>
<footer id="border-no-bottom">Last updated: {{ "today" | date: "%F %R" }}</footer>

```

### File: cask_index.html
```html
---
title: homebrew-cask
layout: default
permalink: /cask/
---
<p>This is a listing of all casks available from the <a href="{{ site.taps.cask.remote }}">{{ site.taps.cask.repository }} tap</a> via the <a href="https://brew.sh">Homebrew</a> package manager for macOS.</p>

<h2><a href="{{ site.baseurl }}/api/cask.json"><code>/api/cask.json</code> (JSON API)</a></h2>

<table>
    {%- assign sorted_casks = site.data.cask | sort -%}
    {%- for cask in sorted_casks -%}
        {%- assign subfolder = cask[1].ruby_source_path | slice: 6, 4 -%}
        {%- unless subfolder == "font" -%}
        <tr>
            {%- assign data_token = cask[0] -%}
            {%- assign token = cask[1].token -%}
            {%- include cask.html data_token=data_token token=token -%}
        </tr>
        {%- endunless -%}
    {%- endfor -%}
</table>
<footer id="border-no-bottom">Last updated: {{ "today" | date: "%F %R" }}</footer>

```

### File: formula_index.html
```html
---
title: homebrew-core
layout: default
permalink: /formula/
redirect_from: /formula-linux/
---
<p>This is a listing of all packages available from the <a href="{{ site.taps.core.remote }}">{{ site.taps.core.repository }} tap</a> via the <a href="https://brew.sh">Homebrew</a> package manager for macOS and Linux.</p>

<h2><a href="{{ site.baseurl }}/api/formula.json"><code>/api/formula.json</code> (JSON API)</a></h2>

<table>
    {%- assign sorted_formulae = site.data.formula | sort -%}
    {%- for formula in sorted_formulae -%}
    <tr>
        {%- assign data_fname = formula[0] -%}
        {%- assign fname = formula[1].name -%}
        {%- include formula.html data_fname=data_fname fname=fname -%}
    </tr>
    {%- endfor -%}
</table>
<footer id="border-no-bottom">Last updated: {{ "today" | date: "%F %R" }}</footer>

```

### File: index.html
```html
---
layout: default
---
<p><a href="{{ site.baseurl }}/">Homebrew Formulae</a> is an online package browser for <a href="https://brew.sh">Homebrew</a> – the macOS (and Linux) package manager. For more information on how to install and use Homebrew see <a href="https://brew.sh">our homepage</a>.</p>

<h2><a href="{{ site.baseurl }}/formula/">Browse all formulae</a></h2>
<h2><a href="{{ site.baseurl }}/cask/">Browse all casks</a> or
    <a href="{{ site.baseurl }}/cask-font/">cask&nbsp;fonts</a></h2>
<h2><a href="{{ site.baseurl }}/analytics/">Analytics data</a></h2>
<h2><a href="{{ site.baseurl }}/docs/api/">JSON API documentation</a></h2>

```

### File: LICENSE.txt
```txt
BSD 2-Clause License

Copyright (c) 2009-present, Homebrew contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```

### File: .github\ISSUE_TEMPLATE.md
```md
# Please fill out one of the templates on: https://github.com/Homebrew/formulae.brew.sh/issues/new/choose or we will close it without comment.

```

### File: analytics\index.md
```md
---
layout: page
redirect_from: /analytics-linux/
---
# Analytics Data

<table>
    <tr>
        <td>Formula Install Events</td>
        <td><a href="{{ site.baseurl }}/analytics/install/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/install/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/install/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Formula Install On Request Events</td>
        <td><a href="{{ site.baseurl }}/analytics/install-on-request/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/install-on-request/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/install-on-request/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Cask Install Events</td>
        <td><a href="{{ site.baseurl }}/analytics/cask-install/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/cask-install/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/cask-install/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Formula Build Error Events</td>
        <td><a href="{{ site.baseurl }}/analytics/build-error/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/build-error/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/build-error/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>OS Versions for Events</td>
        <td><a href="{{ site.baseurl }}/analytics/os-version/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/os-version/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/os-version/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Homebrew Developer Configuration for Events</td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-devcmdrun-developer/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-devcmdrun-developer/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-devcmdrun-developer/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>OS/Architecture/CI for Events</td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-os-arch-ci/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-os-arch-ci/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-os-arch-ci/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Homebrew Prefixes for Events</td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-prefixes/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-prefixes/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-prefixes/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Homebrew Versions for Events</td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-versions/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-versions/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/homebrew-versions/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Homebrew Command Events</td>
        <td><a href="{{ site.baseurl }}/analytics/brew-command-run/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/brew-command-run/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/brew-command-run/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Homebrew Command and Options Events</td>
        <td><a href="{{ site.baseurl }}/analytics/brew-command-run-options/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/brew-command-run-options/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/brew-command-run-options/365d/">365 days</a></td>
    </tr>
    <tr>
        <td>Homebrew Core Test Bot Events</td>
        <td><a href="{{ site.baseurl }}/analytics/brew-test-bot-test/30d/">30 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/brew-test-bot-test/90d/">90 days</a></td>
        <td><a href="{{ site.baseurl }}/analytics/brew-test-bot-test/365d/">365 days</a></td>
    </tr>
    <tr>
        <td><code>/api/analytics/install/homebrew-core/${DAYS}.json</code> (JSON API)</td>
        <td><a href="{{ site.baseurl }}/api/analytics/install/homebrew-core/30d.json">30 days</a></td>
        <td><a href="{{ site.baseurl }}/api/analytics/install/homebrew-core/90d.json">90 days</a></td>
        <td><a href="{{ site.baseurl }}/api/analytics/install/homebrew-core/365d.json">365 days</a></td>
    </tr>
    <tr>
        <td><code>/api/analytics/install-on-request/homebrew-core/${DAYS}.json</code> (JSON API)</td>
        <td><a href="{{ site.baseurl }}/api/analytics/install-on-request/homebrew-core/30d.json">30 days</a></td>
        <td><a href="{{ site.baseurl }}/api/analytics/install-on-request/homebrew-core/90d.json">90 days</a></td>
        <td><a href="{{ site.baseurl }}/api/analytics/install-on-request/homebrew-core/365d.json">365 days</a></td>
    </tr>
    <tr>
        <td><code>/api/analytics/cask-install/homebrew-cask/${DAYS}.json</code> (JSON API)</td>
        <td><a href="{{ site.baseurl }}/api/analytics/cask-install/homebrew-cask/30d.json">30 days</a></td>
        <td><a href="{{ site.baseurl }}/api/analytics/cask-install/homebrew-cask/90d.json">90 days</a></td>
        <td><a href="{{ site.baseurl }}/api/analytics/cask-install/homebrew-cask/365d.json">365 days</a></td>
    </tr>
    <tr>
        <td><code>/api/analytics/build-error/homebrew-core/${DAYS}.json</code> (JSON API)</td>
        <td><a href="{{ site.baseurl }}/api/analytics/build-error/homebrew-core/30d.json">30 days</a></td>
        <td></td>
        <td></td>
    </tr>
</table>

```

### File: api\cask.json
```json
---
---
[
{%- assign sorted_casks = site.data.cask | sort -%}
{% for cask in sorted_casks %}
  {{ cask[1] | jsonify }}
  {%- unless forloop.last -%}
  ,
  {%- endunless -%}
{% endfor %}
]

```

### File: api\formula.json
```json
---
---
[
{%- assign sorted_formulae = site.data.formula | sort -%}
{% for formula in sorted_formulae %}
  {{ formula[1] | jsonify }}
  {%- unless forloop.last -%}
  ,
  {%- endunless -%}
{% endfor %}
]

```

### File: docs\api.md
```md
---
layout: page
permalink: /docs/api/
redirect_from:
  - /api/
  - /docs/
---
# JSON API Documentation

## Metadata

### List metadata for all {{ site.taps.core.name }} formulae or {{ site.taps.cask.name }} casks

List the `brew info --json` output for all current {{ site.taps.core.fullname }} formulae or {{ site.taps.cask.fullname }} casks.

```console
curl https://formulae.brew.sh/api/formula.json
curl https://formulae.brew.sh/api/cask.json
```

**[Response](https://formulae.brew.sh/api/formula.json):**

{% include api-samples/formula.md %}

### Get formula metadata for a {{ site.taps.core.name }} formula

Get the `brew info --json --formula <formula>` output for a single, current {{ site.taps.core.fullname }} formula with extra keys containing analytics data and generation date.

```console
curl https://formulae.brew.sh/api/formula/${FORMULA}.json
```

**Variables:**

- `${FORMULA}`: the name of the formula, e.g. `wget`

**[Response](https://formulae.brew.sh/api/formula/wget.json):**

{% include api-samples/formula_wget.md %}

### Get cask metadata for a {{ site.taps.cask.name }} cask

Get the `brew info --json=v2 --cask <cask>` JSON output for a single, current {{ site.taps.cask.fullname }} cask with extra keys containing analytics data and generation date.

```console
curl https://formulae.brew.sh/api/cask/${CASK}.json
```

**Variables:**

- `${CASK}`: the name of the cask, e.g. `docker-desktop`

**[Response](https://formulae.brew.sh/api/cask/docker-desktop.json):**

{% include api-samples/cask_docker_desktop.md %}

## Analytics

### List one category of analytics events

List all analytics events for a specified category over a number of days, ordered by event frequency count. This is the data source for `brew info --analytics`.

```console
curl https://formulae.brew.sh/api/analytics/${CATEGORY}/${DAYS}.json
```

**Variables:**

- `${CATEGORY}`: the analytics event category, i.e.
  - `install`: the installation of all formulae
  - `install-on-request`: the requested installation of all formulae (i.e. not as a dependency of other formulae)
  - `build-error`: the installation failure of all formulae
- `${DAYS}`: the number of days of analytics events, i.e.
  - `30d`: 30 days
  - `90d`: 90 days
  - `365d`: 365 days

**[Response](https://formulae.brew.sh/api/analytics/install/30d.json):**

{% include api-samples/analytics_install_30d.md %}

### List analytics events for all {{ site.taps.core.name }} formulae

List all the {{ site.taps.core.fullname }} formulae's analytics events for a specified category over a number of days, grouped by formula name. This is the data source for `brew info --analytics --formula <formula>`.

```console
curl https://formulae.brew.sh/api/analytics/${CATEGORY}/homebrew-core/${DAYS}.json
```

**Variables:**

- `${CATEGORY}`: the analytics event category, i.e.
  - `install`: the installation of all {{ site.taps.core.repository }} formulae
  - `install-on-request`: the requested installation of all {{ site.taps.core.repository }} formulae (i.e. not as a dependency of other formulae)
  - `build-error`: the installation failure of all {{ site.taps.core.repository }} formulae
    - only `${DAYS}: 30d` (30 days) is available
- `${DAYS}`: the number of days of analytics events, i.e.
  - `30d`: 30 days
  - `90d`: 90 days
  - `365d`: 365 days

**[Response](https://formulae.brew.sh/api/analytics/install/homebrew-core/30d.json):**

{% include api-samples/analytics_install_homebrew_core_30d.md %}

### List analytics events for all {{ site.taps.cask.name }} casks

List all the {{ site.taps.cask.fullname }} cask's analytics events for the `cask-install` category over a number of days, grouped by cask token.
This is the data source for `brew info --analytics --cask <cask>`.

```console
curl https://formulae.brew.sh/api/analytics/cask-install/homebrew-cask/${DAYS}.json
```

**Variables:**

- `${DAYS}`: the number of days of analytics events, i.e.
  - `30d`: 30 days
  - `90d`: 90 days
  - `365d`: 365 days

**[Response](https://formulae.brew.sh/api/analytics/cask-install/homebrew-cask/30d.json):**

{% include api-samples/analytics_cask_install_homebrew_cask_30d.md %}

```

### File: docs\robots.txt
```txt
---
---
User-agent: *
Sitemap: {{ site.url }}/sitemap.xml

```

### File: includes\attribute.html
```html

<p>{{ include.key }}: <strong>{{ include.value | escape }}</strong></p>

```

### File: includes\cask.html
```html

        <td>
{%- assign include_cdata = site.data.cask[include.data_token] -%}
{%- unless include_cdata -%}
    {%- assign include_data_token = site.data.cask_canonical[include.token] | remove: "@" | remove: "." | replace: "+", "_" -%}
    {%- assign include_cdata = site.data.cask[include_data_token] -%}
{%- endunless -%}
{%- if include_cdata -%}
            <a href="{{ site.baseurl }}/cask/{{ include_cdata.token | uri_escape }}"
            {%- if include_cdata.disabled %} class="disabled" title="This cask has been disabled"
            {%- elsif include_cdata.deprecated %} class="deprecated" title="This cask has been deprecated"
            {%- endif -%}
            >{{ include_cdata.token | escape }}</a></td>
        <td>{{ include_cdata.version | truncate: 20 | escape }}</td>
        <td>{{ include_cdata.desc | escape }}</td>
        <td>{{ include_cdata.name.first | escape }}
{%- else -%}
            {{ include.token | escape }}</td>
        <td></td>
        <td></td>
        <td>
{%- endif -%}
        </td>

```

### File: includes\casks.html
```html
{%- if include.tokens.size > 0 %}
<p>{{ include.description }}:</p>
<table>
    {%- for include_token in include.tokens -%}
    <tr>
        {%- assign include_data_token = include_token | remove: "@" | remove: "." | replace: "+", "_" -%}
        {%- include cask.html data_token=include_data_token token=include_token -%}
    </tr>
    {%- endfor -%}
</table>
{%- endif -%}

```

### File: includes\formula.html
```html

        <td>
{%- assign include_fdata = site.data.formula[include.data_fname] -%}
{%- unless include_fdata -%}
    {%- assign include_data_fname = site.data.formula_canonical[include.fname] | remove: "@" | remove: "." | replace: "+", "_" -%}
    {%- assign include_fdata = site.data.formula[include_data_fname] -%}
{%- endunless -%}
{%- if include_fdata -%}
            <a href="{{ site.baseurl }}/formula/{{ include_fdata.name | uri_escape }}"
            {%- if include_fdata.disabled %} class="disabled" title="This formula has been disabled"
            {%- elsif include_fdata.deprecated %} class="deprecated" title="This formula has been deprecated"
            {%- endif -%}
            >{{ include_fdata.name | escape }}</a></td>
        <td>{{ include_fdata.versions.stable | truncate: 20 | escape }}</td>
        <td>{{ include_fdata.desc | escape }}
{%- else -%}
            {{ include.fname | escape }}</td>
        <td></td>
        <td>
{%- endif -%}
        </td>

```

### File: includes\formulae.html
```html
{%- if include.fnames.size > 0 %}
<p>{{ include.description }}:</p>
<table>
    {%- for include_fname in include.fnames -%}
    <tr>
        {%- assign include_data_fname = include_fname | remove: "@" | remove: "." | replace: "+", "_" -%}
        {%- include formula.html data_fname=include_data_fname fname=include_fname -%}
    </tr>
    {%- endfor -%}
</table>
{%- endif -%}

```

### File: includes\install_command.html
```html

<div class="install">
    <span class="label">Install command: </span>
    <div class="copyable">
        {%- highlight bash -%} brew install{{include.modifier}} {{include.item | escape}} {%- endhighlight -%}
    </div>
</div>

```

### File: includes\replacement.html
```html

<p class="recommended-replacement">Recommended replacement: <strong><a href="{{ site.baseurl }}/{{ include.r_type }}/{{ include.item | uri_escape }}">{{ include.item | escape }}</a></strong></p>

```

### File: layouts\analytics.html
```html
---
layout: base
---
{%- assign analytics_path = page.dir | split: "/" -%}
{%- assign analytics_path = analytics_path[1] -%}
{%- assign analytics_data = site.data[analytics_path][page.category][page.days] -%}
<h2>{{ page.category_pretty }} Events ({{ page.days | split: "d" | first }} days)</h2>

<h3><a href="{{ site.baseurl }}/api/{{ analytics_path }}/{{ page.category }}/{{ page.days }}.json"><code>/api/{{ analytics_path }}/{{ page.category }}/{{ page.days }}.json</code> (JSON API)</a></h3>

<h4>Start Date: {{ analytics_data.start_date }}</h4>
<h4>Total Events: {{ analytics_data.total_count }}</h4>

<table class="full-width">
    <tr>
        <th></th>
        <th>
{%- case page.category -%}
    {%- when "os-version" -%}
            Version
    {%- when "homebrew-devcmdrun-developer" -%}
            Configuration
    {%- when "homebrew-os-arch-ci" -%}
            Setup
    {%- when "homebrew-prefixes" -%}
            Prefix
    {%- when "homebrew-versions" -%}
            Version
    {%- when "brew-command-run" -%}
            Command
    {%- when "brew-command-run-options" -%}
            Command
    {%- when "brew-test-bot-test" -%}
            Command
    {%- when "cask-install" -%}
            Cask
    {%- else -%}
            Formula
{%- endcase -%}
        </th>
        <th>Events</th>
        <th>%</th>
    </tr>
{%- for item in analytics_data.items -%}
    <tr>
        <td class="number-data">#{{ item.number }}</td>
        <td>
    {%- case page.category -%}
        {%- when "os-version" -%}
                <code>{{ item.os_version | escape }}</code>
        {%- when "homebrew-devcmdrun-developer" -%}
                <code>{{ item.devcmdrun_developer | escape }}</code>
        {%- when "homebrew-os-arch-ci" -%}
                <code>{{ item.os_arch_ci | escape }}</code>
        {%- when "homebrew-prefixes" -%}
                <code>{{ item.prefix | escape }}</code>
        {%- when "homebrew-versions" -%}
                <code>{{ item.version | escape }}</code>
        {%- when "brew-command-run" -%}
                <code>{{ item.command_run | escape }}</code>
        {%- when "brew-command-run-options" -%}
                <code>{{ item.command_run_options | escape }}</code>
        {%- when "brew-test-bot-test" -%}
                <code>{{ item.test_bot_test | escape }}</code>
        {%- when "cask-install" -%}
            {%- assign data_token = item.cask | remove: "@" | remove: "." | replace: "+", "_" -%}
            {%- assign cdata = site.data.cask[data_token] -%}
            {%- if cdata and cdata.token == item.cask -%}
                <a href="{{ site.baseurl }}/cask/{{ item.cask | uri_escape }}"><code>{{ item.cask | escape }}</code></a>
            {%- else -%}
                <code>{{ item.cask | escape }}</code>
            {%- endif -%}
        {%- else -%}
            {%- assign fname = item.formula | split: " " | first -%}
            {%- assign data_fname = fname | remove: "@" | remove: "." | replace: "+", "_" -%}
            {%- assign fdata = site.data.formula[data_fname] -%}
            {%- if fdata and fdata.name == fname -%}
                <a href="{{ site.baseurl }}/formula/{{ fname | uri_escape }}"><code>{{ item.formula | escape }}</code></a>
            {%- else -%}
                <code>{{ item.formula | escape }}</code>
            {%- endif -%}
    {%- endcase -%}
        </td>
        <td class="number-data">{{ item.count }}</td>
        <td class="number-data">{{ item.percent }}%</td>
    </tr>
{%- endfor %}
</table>

```

### File: layouts\analytics_json.json
```json
---
---
{%- assign analytics_path = page.dir | split: "/" -%}
{%- assign analytics_path = analytics_path[2] -%}
{%- if page.homebrew-core -%}
  {%- assign analytics_data_source = "homebrew-core" -%}
{%- elsif page.homebrew-cask -%}
  {%- assign analytics_data_source = "homebrew-cask" -%}
{%- endif -%}
{%- assign days = page.name | remove: ".json" -%}
{%- if analytics_data_source -%}
  {%- assign json = site.data[analytics_path][page.category][analytics_data_source][days] -%}
{%- else -%}
  {%- assign json = site.data[analytics_path][page.category][days] -%}
{%- endif -%}
{{ json | jsonify }}

```

### File: layouts\cask.html
```html
---
layout: default
permalink: :title
---
{%- assign token = page.title -%}
{%- assign data_token = token | remove: "@" | remove: "." | replace: "+", "_" -%}
{%- assign c = site.data.cask[data_token] -%}
<h2
    {%- if c.disabled %} class="disabled" title="This cask has been disabled since {{ c.disable_date | escape }} because it {{ site.reasons.cask[c.disable_reason] | default: c.disable_reason | escape }}"
    {%- elsif c.deprecated %} class="deprecated" title="This cask has been deprecated{% if c.deprecation_date %} since {{ c.deprecation_date | escape }}{% endif %} because it {{ site.reasons.cask[c.deprecation_reason] | default: c.deprecation_reason | escape }}"
    {%- endif -%}
    >
    {{ c.token | escape }}
    {%- if c.disabled %} (disabled)
    {%- elsif c.deprecated %} (deprecated)
    {%- endif -%}
</h2>

{%- if c.deprecated == false and c.deprecation_date -%}
    {%- include attribute.html key="Deprecation date" value=c.deprecation_date -%}
{%- endif -%}
{%- if c.disabled == false and c.disable_date -%}
    {%- include attribute.html key="Disable date" value=c.disable_date -%}
{%- endif -%}

{%- if c.disable_replacement_formula -%}
    {%- include replacement.html item=c.disable_replacement_formula r_type="formula" -%}
{%- elsif c.disable_replacement_cask -%}
    {%- include replacement.html item=c.disable_replacement_cask r_type="cask" -%}
{%- elsif c.deprecation_replacement_formula -%}
    {%- include replacement.html item=c.deprecation_replacement_formula r_type="formula" -%}
{%- elsif c.deprecation_replacement_cask -%}
    {%- include replacement.html item=c.deprecation_replacement_cask r_type="cask" -%}
{%- endif -%}

{%- include install_command.html item=c.token modifier=" --cask" %}
<p class="names">Name{%- if c.name.size > 1 -%}s{%- endif -%}:
{%- for name in c.name %}
    <strong>{{ name | escape }}</strong>
    {%- unless forloop.last -%}, {% endunless %}
{%- endfor -%}
</p>
{%- if c.desc %}
<p class="desc">{{ c.desc | escape }}</p>
{%- endif %}
<p class="homepage"><a rel="nofollow" href="{{ c.homepage | escape }}">{{ c.homepage | escape }}</a></p>

<p>Development: <a rel="nofollow" href="https://github.com/Homebrew/homebrew-cask/pulls?q=sort:updated-desc+is:pr+{{ c.token | uri_escape }}+in:title">Pull requests</a></p>

<p>Cask JSON API: <a rel="alternate" type="application/json" href="{{ site.baseurl }}/api/cask/{{ c.token | uri_escape }}.json"><code>/api/cask/{{ c.token | escape }}.json</code></a></p>

<p>Cask code: <a rel="alternate" target="_blank" href="{{ site.taps.cask.remote }}/blob/{{ c.tap_git_head | url_encode }}/{{ c.ruby_source_path | uri_escape }}"><code>{{ c.token | escape }}.rb</code></a> on GitHub</p>

<p>Current version: <a rel="nofollow" href="{{ c.url | escape }}" title="Download for {{ c.token | escape }}">{{ c.version | escape }}</a></p>

{%- if c.old_tokens.size > 0 %}
<p class="oldnames">Former tokens:
    {%- for oldtoken in c.old_tokens %}
        <strong>{{ oldtoken | escape }}</strong>
        {%- unless forloop.last -%}, {% endunless -%}
    {%- endfor %}
</p>
{%- endif %}

{%- if c.depends_on.size > 0 -%}
    {%- include casks.html tokens=c.depends_on.cask description="Depends on casks" -%}
    {%- include formulae.html fnames=c.depends_on.formula description="Depends on formulae" -%}
    {%- assign requirements = "" -%}
    {%- if c.depends_on.macos -%}
        {%- capture requirements -%}
            macOS {% for x in c.depends_on.macos -%}
                {{ x.first | escape }} <strong>{{ c.depends_on.macos[x.first] | join: "</strong> / <strong>" }}</strong>
                {%- unless forloop.last %} and {% endunless -%}
            {%- endfor -%}
        {%- endcapture -%}
    {%- endif -%}
    {%- if c.depends_on.arch -%}
        {%- if requirements.size > 0 -%}
            {%- assign requirements = requirements | append: ", " -%}
        {%- endif -%}
        {%- capture requirements -%}
            {{ requirements }}{% for a in c.depends_on.arch -%}
                <strong>{{ a.type | capitalize }} {{ a.bits }}-bit</strong>
                {%- unless forloop.last %} or {% endunless -%}
            {%- endfor %} architecture
        {%- endcapture -%}
    {%- endif -%}
    {%- if requirements.size > 0 %}
<p>Requirements: {{ requirements }}</p>
    {%- endif -%}
{%- endif -%}

{%- if c.conflicts_with.size > 0 -%}
    {%- include casks.html tokens=c.conflicts_with.cask description="Conflicts with casks" -%}
{%- endif -%}

{%- if c.caveats -%}
{%- capture soft_indent %}
  {% endcapture -%}
{%- capture hard_indent %}
&nbsp;&nbsp;&nbsp;&nbsp;{% endcapture %}
<table class="full-width">
    <tr>
        <td>{{ c.caveats | escape | replace: soft_indent, hard_indent | strip | newline_to_br }}</td>
    </tr>
</table>
{%- endif %}

{%- if c.variations.size > 0 -%}

{%- assign arm64_variation_count = 0 -%}
{%- assign intel_variation_count = 0 -%}
{%- for variation in c.variations -%}
    {%- if variation[0] contains "arm64_" -%}
        {%- assign arm64_variation_count = arm64_variation_count | plus: 1 -%}
    {%- else -%}
        {%- assign intel_variation_count = intel_variation_count | plus: 1 -%}
    {%- endif -%}
{%- endfor %}

<p>Versions:</p>
<table class="full-width">
    {%- assign subsequent = false -%}
    {%- for variation in c.variations -%}
        {%- if variation[0] contains "arm64_" %}
        <tr>
            {%- unless subsequent -%}
            <th rowspan="{{ arm64_variation_count }}" scope="rowgroup">Apple Silicon</th>
            {%- endunless %}
            <td style="text-transform:capitalize;">
                {{ variation[0] | remove_first: "arm64_" | replace: "_", "&nbsp;" }}
                {%- assign subsequent = true -%}
            </td>
            <td>
                <a rel="nofollow" href="{{ variation[1].url | default: c.url | escape }}"
                   title="Download for {{ c.token | escape }} on {{ variation[0] }}">
                    {{ variation[1].version | default: c.version | escape }}
                </a>
            </td>
        </tr>
        {%- endif -%}
    {%- endfor %}
    <tr><th colspan="3"></th></tr>
    {%- assign subsequent = false -%}
    {%- for variation in c.variations -%}
        {%- unless variation[0] contains "arm64_" %}
        <tr>
            {%- unless subsequent -%}
            <th rowspan="{{ intel_variation_count }}" scope="rowgroup">Intel</th>
            {%- endunless %}
            <td style="text-transform:capitalize;">
                {{ variation[0] | replace: "x86_64", "64-bit" | replace: "_", "&nbsp;" }}
                {%- assign subsequent = true -%}
            </td>
            <td>
                <a rel="nofollow" href="{{ variation[1].url | default: c.url | escape }}"
                   title="Download for {{ c.token | escape }} on {{ variation[0] }}">
                    {{ variation[1].version | default: c.version | escape }}
                </a>
            </td>
        </tr>
        {%- endunless -%}
    {%- endfor -%}
</table>
{%- endif %}

<p>Analytics:</p>
<table>
{%- for interval in site.analytics.intervals -%}
    <tr>
        <th colspan="2">Installs ({{ interval.name }})</th>
    </tr>
    {%- for fa in site.data.analytics.cask-install.homebrew-cask[interval.path].formulae[token] -%}
    <tr>
        <td><code>{{ fa.cask | escape }}</code></td>
        <td class="number-data">{{ fa.count }}</td>
    </tr>
    {%- else -%}
    <tr>
        <td><code>{{ token | escape }}</code></td>
        <td class="number-data">0</td>
    </tr>
    {%- endfor -%}
{%- endfor %}
</table>

```

### File: layouts\cask_json.json
```json
---
---
{%- assign token = page.name | remove: ".json" -%}
{%- assign data_token = token | remove: "@" | remove: "." | replace: "+", "_" -%}
{%- assign cdata = site.data.cask[data_token] -%}
{

{%- for key_value in cdata -%}
  {{ key_value[0] | jsonify }}:{{ key_value[1] | jsonify }},
{%- endfor -%}

"analytics":{"install":{
{%- for interval in site.analytics.intervals -%}
  "{{ interval.path }}":{
  {%- for fa in site.data.analytics.cask-install.homebrew-cask[interval.path].formulae[token] -%}
    {{ fa.cask | jsonify }}:{{ fa.count | remove: "," | plus: 0 }}
    {%- unless forloop.last -%}
    ,
    {%- endunless -%}
  {%- else -%}
    {{ token | jsonify }}:0
  {%- endfor -%}
  }
  {%- unless forloop.last -%}
  ,
  {%- endunless -%}
{%- endfor -%}
}},
"generated_date":"{{ "today" | date: "%F" }}"}

```

### File: layouts\formula.html
```html
---
layout: default
permalink: :title
---
{%- assign fname = page.title -%}
{%- assign data_fname = fname | remove: "@" | remove: "." | replace: "+", "_" -%}
{%- assign f = site.data.formula[data_fname] -%}
<h2
    {%- if f.disabled %} class="disabled" title="This formula has been disabled since {{ f.disable_date | escape }} because it {{ site.reasons.formula[f.disable_reason] | default: f.disable_reason | escape }}"
    {%- elsif f.deprecated %} class="deprecated" title="This formula has been deprecated{% if f.deprecation_date %} since {{ f.deprecation_date | escape }}{% endif %} because it {{ site.reasons.formula[f.deprecation_reason] | default: f.deprecation_reason | escape }}"
    {%- endif -%}
    >
    {{ f.name | escape }}
    {%- if f.disabled %} (disabled)
    {%- elsif f.deprecated %} (deprecated)
    {%- endif -%}
</h2>

{%- if f.deprecated == false and f.deprecation_date -%}
    {%- include attribute.html key="Deprecation date" value=f.deprecation_date -%}
{%- endif -%}
{%- if f.disabled == false and f.disable_date -%}
    {%- include attribute.html key="Disable date" value=f.disable_date -%}
{%- endif -%}

{%- if f.disable_replacement_formula -%}
    {%- include replacement.html item=f.disable_replacement_formula r_type="formula" -%}
{%- elsif f.disable_replacement_cask -%}
    {%- include replacement.html item=f.disable_replacement_cask r_type="cask" -%}
{%- elsif f.deprecation_replacement_formula -%}
    {%- include replacement.html item=f.deprecation_replacement_formula r_type="formula" -%}
{%- elsif f.deprecation_replacement_cask -%}
    {%- include replacement.html item=f.deprecation_replacement_cask r_type="cask" -%}
{%- endif -%}

{%- include install_command.html item=f.name %}
{%- if f.aliases.size > 0 %}
<p class="aliases">Also known as:
    {%- for alias in f.aliases %}
        <strong>{{ alias | escape }}</strong>
        {%- unless forloop.last -%}, {% endunless -%}
    {%- endfor %}
</p>
{%- endif -%}
{%- if f.oldnames.size > 0 %}
<p class="oldnames">Formerly known as:
    {%- for oldname in f.oldnames %}
        <strong>{{ oldname | escape }}</strong>
        {%- unless forloop.last -%}, {% endunless -%}
    {%- endfor %}
</p>
{%- endif %}
<p class="desc">{{ f.desc | escape }}</p>
<p class="homepage"><a rel="nofollow" href="{{ f.homepage | escape }}">{{ f.homepage | escape }}</a></p>

{%- if f.license.size > 0 %}
<p>License:
    {%- for license in f.license %}
        <strong>{{ license | replace: "_", " " | escape }}</strong>
        {%- unless forloop.last -%}, {% endunless -%}
    {%- endfor %}
</p>
{%- endif %}

<p>Development: <a rel="nofollow" href="https://github.com/Homebrew/homebrew-core/pulls?q=sort:updated-desc+is:pr+{{ f.name | uri_escape }}+in:title">Pull requests</a></p>

<p>Formula JSON API: <a rel="alternate" type="application/json" href="{{ site.baseurl }}/api/formula/{{ f.name | uri_escape }}.json"><code>/api/formula/{{ f.name | escape }}.json</code></a></p>

<p>Formula code: <a rel="alternate" target="_blank" href="{{ site.taps.core.remote }}/blob/{{ f.tap_git_head | url_encode }}/{{ f.ruby_source_path | uri_escape }}"><code>{{ f.name | escape }}.rb</code></a> on GitHub</p>

<p>Bottle (binary package)
{%- assign bottles = false -%}
{%- if f.bottle_disabled %} not required, support provided for all supported Homebrew platforms.
{%- elsif f.bottle.stable %} installation support provided
    {%- if f.bottle.stable.files.all -%}.
    {%- else -%}
        {%- assign bottles = true %} for:
    {%- endif -%}
{%- else %} not available on this platform.
{%- endif -%}</p>

{%- if bottles -%}
    {%- assign arm64_bottle_count = 0 -%}
    {%- assign intel_bottle_count = 0 -%}
    {%- assign linux_bottle_count = 0 -%}
    {%- for b in f.bottle.stable.files -%}
        {%- if b[0] contains "arm64_" -%}
            {%- if b[0] contains "_linux" -%}
                {%- assign linux_bottle_count = linux_bottle_count | plus: 1 -%}
            {%- else -%}
                {%- assign arm64_bottle_count = arm64_bottle_count | plus: 1 -%}
            {%- endif -%}
        {%- elsif b[0] contains "_linux" -%}
            {%- assign linux_bottle_count = linux_bottle_count | plus: 1 -%}
        {%- else -%}
            {%- assign intel_bottle_count = intel_bottle_count | plus: 1 -%}
        {%- endif -%}
    {%- endfor %}
<table>
    {%- assign subsequent = false -%}
    {%- for b in f.bottle.stable.files -%}
        {%- if b[0] contains "arm64_" %}
            {%- if b[0] contains "_linux" -%}
                {%- continue -%}
            {%- endif -%}
        <tr>
            {%- unless subsequent -%}
            <th rowspan="{{ arm64_bottle_count }}" scope="rowgroup">macOS on<br>Apple Silicon</th>
            {%- endunless %}
            <td style="text-transform:capitalize;">
                {{ b[0] | remove_first: "arm64_" | replace: "_", "&nbsp;" }}
                {%- assign subsequent = true -%}
            </td>
            <td>✅</td>
        </tr>
        {%- endif -%}
    {%- endfor %}
    {%- if arm64_bottle_count > 0 and intel_bottle_count > 0 %}
    <tr><th colspan="3"></th></tr>
    {%- endif %}
    {%- assign subsequent = false -%}
    {%- for b in f.bottle.stable.files -%}
        {%- unless b[0] contains "arm64_" %}
            {%- if b[0] contains "_linux" -%}
                {%- continue -%}
            {%- endif -%}
        <tr>
            {%- unless subsequent -%}
            <th rowspan="{{ intel_bottle_count }}" scope="rowgroup">macOS on<br>Intel</th>
            {%- endunless %}
            <td style="text-transform:capitalize;">
                {{ b[0] | replace: "_", "&nbsp;" }}
                {%- assign subsequent = true -%}
            </td>
            <td>✅</td>
        </tr>
        {%- endunless -%}
    {%- endfor -%}
    {%- assign macos_bottle_count = arm64_bottle_count | plus: intel_bottle_count %}
    {%- if macos_bottle_count > 0 and linux_bottle_count > 0 %}
    <tr><th colspan="3"></th></tr>
    {%- endif %}
    {%- assign subsequent = false -%}
    {%- for b in f.bottle.stable.files -%}
        {%- if b[0] contains "_linux" %}
        <tr>
            {%- unless subsequent -%}
            <th rowspan="{{ linux_bottle_count }}" scope="rowgroup">Linux</th>
            {%- endunless %}
            <td>
                {{ b[0] | replace: "arm64", "ARM64" | replace: "_linux", "" }}
                {%- assign subsequent = true -%}
            </td>
            <td>✅</td>
        </tr>
        {%- endif -%}
    {%- endfor -%}
</table>
{%- endif %}

<p>Current versions:</p>
<table>
    <tr>
        <td><strong>stable</strong></td>
        <td>✅</td>
        <td>{{ f.versions.stable | escape }}</td>
    </tr>
{%- if f.versions.head %}
    <tr>
        <td><strong>head</strong></td>
        <td>⚡️</td>
        <td>{{ f.versions.head | escape }}</td>
    </tr>
{%- endif %}
</table>

{%- include formulae.html fnames=f.versioned_formulae description="Other versions" -%}

{%- if f.revision > 0 -%}
    {%- include attribute.html key="Revision" value=f.revision -%}
{%- endif -%}

{%- if f.keg_only %}
<p>Keg-only</p>
{%- endif -%}

{%- if f.options.size > 0 %}
<p>Options:</p>
<table>
    {%- for o in f.options -%}
    <tr>
        <td>{{ o.option | escape }}</td>
        <td>{{ o.description | escape }}</td>
    </tr>
    {%- endfor %}
</table>
{%- endif -%}

{%- include formulae.html fnames=f.dependencies description="Depends on" -%}
{%- include formulae.html fnames=f.recommended_dependencies description="Depends on recommended" -%}
{%- include formulae.html fnames=f.optional_dependencies description="Depends on optionally" -%}
{%- include formulae.html fnames=f.build_dependencies description="Depends on when building from source" -%}

{%- if f.requirements.size > 0 %}
<p>Requires:
    {%- for r in f.requirements %}
    <strong>
        {%- capture requirement -%}
            {%- case r.name -%}
                {%- when "arch" -%}
                    {{ r.version | escape }}
                {%- when "macos" or "maximum_macos" -%}
                    macOS
                {%- else -%}
                    {{ r.name | capitalize | escape }}
            {%- endcase -%}
        {%- endcapture -%}
        {%- if r.cask -%}
            {%- unless r.cask contains "/" -%}
                <a href="{{ site.baseurl }}/cask/{{ r.cask | uri_escape }}">{{ requirement }}</a>
            {%- else -%}
                {{ requirement }}
            {%- endunless -%}
        {%- else -%}
            {{ requirement }}
        {%- endif -%}
    </strong>
        {%- if r.version -%}
            {%- if r.name == "arch" %} architecture
            {%- elsif r.name contains "maximum" %} &lt;= {{ r.version | escape }}
            {%- else %} &gt;= {{ r.version | escape }}
            {%- endif -%}
        {%- endif -%}
        {%- for c in r.contexts -%}
            {%- if forloop.first %} ( {%- endif -%}
            {{ c | escape }}
            {%- unless forloop.last -%}, {% endunless -%}
            {%- if forloop.last -%} ) {%- endif -%}
        {%- endfor -%}
        {%- unless forloop.last -%}, {% endunless -%}
    {%- endfor %}
</p>
{%- endif -%}

{%- if f.conflicts_with.size > 0 %}
<p>Conflicts with:
    {%- for conflict in f.conflicts_with %}
        <strong><a href="{{ site.baseurl }}/formula/{{ conflict | uri_escape }}">{{ conflict | escape }}</a></strong>
        {%- unless forloop.last -%}, {% endunless -%}
    {%- endfor %}
</p>
{%- endif -%}

{%- if f.caveats -%}
{%- capture soft_indent %}
  {% endcapture -%}
{%- capture hard_indent %}
&nbsp;&nbsp;&nbsp;&nbsp;{% endcapture %}
<table class="full-width">
    <tr>
        <td>{{ f.caveats | escape | replace: soft_indent, hard_indent | strip | newline_to_br }}</td>
    </tr>
</table>
{%- endif -%}

<p>Analytics:</p>
<table>
{%- for interval in site.analytics.intervals -%}
  {%- for category in site.analytics.categories.formulae -%}
    {%- if forloop.parentloop.first == false and forloop.last -%}
        {%- break -%}
    {%- endif -%}
    <tr>
        <th colspan="2">{{ category.name }} ({{ interval.name }})</th>
    </tr>
    {%- for fa in site.data.analytics[category.path].homebrew-core[interval.path].formulae[fname] -%}
    <tr>
        <td><code>{{ fa.formula | escape }}</code></td>
        <td class="number-data">{{ fa.count }}</td>
    </tr>
    {%- else -%}
    <tr>
        <td><code>{{ fname | escape }}</code></td>
        <td class="number-data">0</td>
    </tr>
    {%- endfor -%}
  {%- endfor -%}
{%- endfor %}
</table>

```

### File: layouts\formula_json.json
```json
---
---
{%- assign fname = page.name | remove: ".json" -%}
{%- assign data_fname = fname | remove: "@" | remove: "." | replace: "+", "_" -%}
{%- assign fdata = site.data.formula[data_fname] -%}
{

{%- for key_value in fdata -%}
  {{ key_value[0] | jsonify }}:{{ key_value[1] | jsonify }},
{%- endfor -%}

"analytics":{
{%- for category in site.analytics.categories.formulae -%}
  "{{ category.path | replace: "-", "_" }}":{
  {%- for interval in site.analytics.intervals -%}
    "{{ interval.path }}":{
    {%- for fa in site.data.analytics[category.path].homebrew-core[interval.path].formulae[fname] -%}
      {{ fa.formula | jsonify }}:{{ fa.count | remove: "," | plus: 0 }}
      {%- unless forloop.last -%}
      ,
      {%- endunless -%}
    {%- else -%}
      {{ fname | jsonify }}:0
    {%- endfor -%}
    }
    {%- if category.path == "build-error" -%}
      {%- break -%}
    {%- endif -%}
    {%- unless forloop.last -%}
    ,
    {%- endunless -%}
  {%- endfor -%}
  }
  {%- unless forloop.last -%}
  ,
  {%- endunless -%}
{%- endfor -%}
},
"generated_date":"{{ "today" | date: "%F" }}"}

```

### File: .github\ISSUE_TEMPLATE\bug.md
```md
---
name: New issue for Reproducible Bug
about: "If you're sure it's reproducible and not just your machine: submit an issue so we can investigate."

---

# Please note we will close your issue without comment if you delete, do not read or do not fill out the issue checklist below and provide ALL the requested information. If you repeatedly fail to use the issue template, we will block you from ever submitting issues to Homebrew again.

- [ ] your issue is with the https://formulae.brew.sh website and not the (generated) contents of a given formula/cask page.

<!-- To help us debug your issue, please complete these sections: -->

## What you were trying to do (and why)

<!-- replace me -->

## What happened (include screenshots)

<!-- replace me -->

## What you expected to happen

<!-- replace me -->

```

