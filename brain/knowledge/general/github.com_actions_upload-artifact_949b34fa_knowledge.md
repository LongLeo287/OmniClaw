---
id: github.com-actions-upload-artifact-949b34fa-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:27.735004
---

# KNOWLEDGE EXTRACT: github.com_actions_upload-artifact_949b34fa
> **Extracted on:** 2026-04-01 16:24:53
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525109/github.com_actions_upload-artifact_949b34fa

---

## File: `.gitattributes`
```
* text=auto eol=lf
.licenses/** -diff linguist-generated=true
```

## File: `.gitignore`
```
node_modules/
lib/
__tests__/_temp/
.DS_Store
```

## File: `.licensed.yml`
```yaml
sources:
  npm: true

# Force UTF-8 encoding
encoding: 'utf-8'

allowed:
  - apache-2.0
  - bsd-2-clause
  - bsd-3-clause
  - isc
  - mit
  - cc0-1.0
  - unlicense
  - 0bsd
  - blueoak-1.0.0

reviewed:
  npm:
  - fs.realpath
  - "@actions/http-client" # MIT
  - "@bufbuild/protobuf" # Apache-2.0
  - "@pkgjs/parseargs" # MIT
  - "@protobuf-ts/runtime" # Apache-2.0
  - argparse # Python-2.0
  - buffers # MIT
  - chainsaw # MIT
  - color-convert # MIT
  - ieee754 # BSD-3-Clause
  - lodash # MIT
  - mdurl # MIT
  - neo-async # MIT
  - package-json-from-dist # ISC
  - readable-stream # MIT
  - sax # ISC
  - source-map # BSD-3-Clause
  - string_decoder # MIT
  - traverse # MIT
  - tslib # 0BSD
  - uglify-js # BSD-2-Clause
  - wordwrap # MIT
```

## File: `.prettierignore`
```
dist/
lib/
node_modules/
```

## File: `.prettierrc.json`
```json
{
    "printWidth": 80,
    "tabWidth": 2,
    "useTabs": false,
    "semi": false,
    "singleQuote": true,
    "trailingComma": "none",
    "bracketSpacing": false,
    "arrowParens": "avoid",
    "parser": "typescript"
  }
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies within all project spaces, and it also applies when
an individual is representing the project or its community in public spaces.
Examples of representing a project or community include using an official
project e-mail address, posting via an official social media account, or acting
as an appointed representative at an online or offline event. Representation of
a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at opensource@github.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
```

## File: `CONTRIBUTING.md`
```markdown
## Contributing

[fork]: https://github.com/actions/upload-artifact/fork
[pr]: https://github.com/actions/upload-artifact/compare
[style]: https://github.com/styleguide/js
[code-of-conduct]: CODE_OF_CONDUCT.md

Hi there! We're thrilled that you'd like to contribute to this project. Your help is essential for keeping it great.

Contributions to this project are [released](https://help.github.com/articles/github-terms-of-service/#6-contributions-under-repository-license) to the public under the [project's open source license](LICENSE).

Please note that this project is released with a [Contributor Code of Conduct][code-of-conduct]. By participating in this project you agree to abide by its terms.

## Found a bug?

- **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/actions/upload-artifact/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/actions/upload-artifact/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or a **reproducable test case** demonstrating the expected behavior that is not occurring.
- If possible, use the relevant bug report templates to create the issue.

## What should I know before submitting a pull request or issue

The code related to `upload-artifact` is split between this repository and [actions/toolkit](https://github.com/actions/toolkit) where the `@actions/artifact` npm package is housed. The npm package contains the core functionality to interact with artifacts. Any extra functionality on top of interacting with the apis such as search is inside this repository.
Artifact related issues will be tracked in this repository so please do not open duplicate issues in `actions/toolkit`.

## Submitting a pull request

1. [Fork][fork] and clone the repository
2. Configure and install the dependencies: `npm install`
3. Make sure the tests pass on your machine: `npm run test`
4. Create a new branch: `git checkout -b my-branch-name`
5. Make your change, add tests, and make sure the tests still pass
6. Make sure your code is correctly formatted: `npm run format`
7. Make sure your code passes linting: `npm run lint`
8. Update `dist/index.js` using `npm run release`. This creates a single javascript file that is used as an entry-point for the action
7. Push to your fork and [submit a pull request][pr]
8. Pat your self on the back and wait for your pull request to be reviewed and merged.

Here are a few things you can do that will increase the likelihood of your pull request being accepted:

- Write tests.
- Keep your change as focused as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Licensed

This repository uses a tool called [Licensed](https://github.com/github/licensed) to verify third party dependencies. You may need to locally install licensed and run `licensed cache` to update the dependency cache if you install or update a production dependency. If licensed cache is unable to determine the dependency, you may need to modify the cache file yourself to put the correct license. You should still verify the dependency, licensed is a tool to help, but is not a substitute for human review of dependencies.

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)

Thanks! :heart: :heart: :heart:

GitHub Actions Team :octocat:
```

## File: `LICENSE`
```

The MIT License (MIT)

Copyright (c) 2018 GitHub, Inc. and contributors

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
# `@actions/upload-artifact`

> [!WARNING]
> actions/upload-artifact@v3 is scheduled for deprecation on **November 30, 2024**. [Learn more.](https://github.blog/changelog/2024-04-16-deprecation-notice-v3-of-the-artifact-actions/)
> Similarly, v1/v2 are scheduled for deprecation on **June 30, 2024**.
> Please update your workflow to use v4 of the artifact actions.
> This deprecation will not impact any existing versions of GitHub Enterprise Server being used by customers.

Upload [Actions Artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts) from your Workflow Runs. Internally powered by [@actions/artifact](https://github.com/actions/toolkit/tree/main/packages/artifact) package.

See also [download-artifact](https://github.com/actions/download-artifact).

- [`@actions/upload-artifact`](#actionsupload-artifact)
  - [v6 - What's new](#v6---whats-new)
  - [v4 - What's new](#v4---whats-new)
    - [Improvements](#improvements)
    - [Breaking Changes](#breaking-changes)
  - [Usage](#usage)
    - [Inputs](#inputs)
    - [Outputs](#outputs)
  - [Examples](#examples)
    - [Upload an Individual File](#upload-an-individual-file)
    - [Upload an Entire Directory](#upload-an-entire-directory)
    - [Upload using a Wildcard Pattern](#upload-using-a-wildcard-pattern)
    - [Upload using Multiple Paths and Exclusions](#upload-using-multiple-paths-and-exclusions)
    - [Altering compressions level (speed v. size)](#altering-compressions-level-speed-v-size)
    - [Customization if no files are found](#customization-if-no-files-are-found)
    - [(Not) Uploading to the same artifact](#not-uploading-to-the-same-artifact)
    - [Environment Variables and Tilde Expansion](#environment-variables-and-tilde-expansion)
    - [Retention Period](#retention-period)
    - [Using Outputs](#using-outputs)
      - [Example output between steps](#example-output-between-steps)
      - [Example output between jobs](#example-output-between-jobs)
    - [Overwriting an Artifact](#overwriting-an-artifact)
  - [Limitations](#limitations)
    - [Number of Artifacts](#number-of-artifacts)
    - [Zip archives](#zip-archives)
    - [Permission Loss](#permission-loss)
  - [Where does the upload go?](#where-does-the-upload-go)


## v6 - What's new

> [!IMPORTANT]
> actions/upload-artifact@v6 now runs on Node.js 24 (`runs.using: node24`) and requires a minimum Actions Runner version of 2.327.1. If you are using self-hosted runners, ensure they are updated before upgrading.

### Node.js 24

This release updates the runtime to Node.js 24. v5 had preliminary support for Node.js 24, however this action was by default still running on Node.js 20. Now this action by default will run on Node.js 24.

## v4 - What's new

> [!IMPORTANT]
> upload-artifact@v4+ is not currently supported on GitHub Enterprise Server (GHES) yet. If you are on GHES, you must use [v3](https://github.com/actions/upload-artifact/releases/tag/v3) (Node 16) or [v3-node20](https://github.com/actions/upload-artifact/releases/tag/v3-node20) (Node 20).

The release of upload-artifact@v4 and download-artifact@v4 are major changes to the backend architecture of Artifacts. They have numerous performance and behavioral improvements.

For more information, see the [`@actions/artifact`](https://github.com/actions/toolkit/tree/main/packages/artifact) documentation.

There is also a new sub-action, `actions/upload-artifact/merge`. For more info, check out that action's [README](../../../README.md).

### Improvements

1. Uploads are significantly faster, upwards of 90% improvement in worst case scenarios.
2. Once uploaded, an Artifact ID is returned and Artifacts are immediately available in the UI and [REST API](https://docs.github.com/en/rest/actions/artifacts). Previously, you would have to wait for the run to be completed before an ID was available or any APIs could be utilized.
3. The contents of an Artifact are uploaded together into an _immutable_ archive. They cannot be altered by subsequent jobs unless the Artifacts are deleted and recreated (where they will have a new ID). Both of these factors help reduce the possibility of accidentally corrupting Artifact files.
4. The compression level of an Artifact can be manually tweaked for speed or size reduction.

### Breaking Changes

1. On self hosted runners, additional [firewall rules](https://github.com/actions/toolkit/tree/main/packages/artifact#breaking-changes) may be required.
2. Uploading to the same named Artifact multiple times.

    Due to how Artifacts are created in this new version, it is no longer possible to upload to the same named Artifact multiple times. You must either split the uploads into multiple Artifacts with different names, or only upload once. Otherwise you _will_ encounter an error.

3. Limit of Artifacts for an individual job. Each job in a workflow run now has a limit of 500 artifacts.
4. With `v4.4` and later, hidden files are excluded by default.

For assistance with breaking changes, see [MIGRATION.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/hook_development/references/migration.md).

## Note

Thank you for your interest in this GitHub repo, however, right now we are not taking contributions. 

We continue to focus our resources on strategic areas that help our customers be successful while making developers' lives easier. While GitHub Actions remains a key part of this vision, we are allocating resources towards other areas of Actions and are not taking contributions to this repository at this time. The GitHub public roadmap is the best place to follow along for any updates on features we’re working on and what stage they’re in.

We are taking the following steps to better direct requests related to GitHub Actions, including:

1. We will be directing questions and support requests to our [Community Discussions area](https://github.com/orgs/community/discussions/categories/actions)

2. High Priority bugs can be reported through Community Discussions or you can report these to our support team https://support.github.com/contact/bug-report.

3. Security Issues should be handled as per our [security.md](SECURITY.md).

We will still provide security updates for this project and fix major breaking changes during this time.

You are welcome to still raise bugs in this repo.

## Usage

### Inputs

```yaml
- uses: actions/upload-artifact@v4
  with:
    # Name of the artifact to upload.
    # Optional. Default is 'artifact'
    name:

    # A file, directory or wildcard pattern that describes what to upload
    # Required.
    path:

    # The desired behavior if no files are found using the provided path.
    # Available Options:
    #   warn: Output a warning but do not fail the action
    #   error: Fail the action with an error message
    #   ignore: Do not output any warnings or errors, the action does not fail
    # Optional. Default is 'warn'
    if-no-files-found:

    # Duration after which artifact will expire in days. 0 means using default retention.
    # Minimum 1 day.
    # Maximum 90 days unless changed from the repository settings page.
    # Optional. Defaults to repository settings.
    retention-days:

    # The level of compression for Zlib to be applied to the artifact archive.
    # The value can range from 0 to 9.
    # For large files that are not easily compressed, a value of 0 is recommended for significantly faster uploads.
    # Optional. Default is '6'
    compression-level:

    # If true, an artifact with a matching name will be deleted before a new one is uploaded.
    # If false, the action will fail if an artifact for the given name already exists.
    # Does not fail if the artifact does not exist.
    # Optional. Default is 'false'
    overwrite:

    # Whether to include hidden files in the provided path in the artifact
    # The file contents of any hidden files in the path should be validated before
    # enabled this to avoid uploading sensitive information.
    # Optional. Default is 'false'
    include-hidden-files:
```

### Outputs

| Name | Description | Example |
| - | - | - |
| `artifact-id` | GitHub ID of an Artifact, can be used by the REST API | `1234` |
| `artifact-url` | URL to download an Artifact. Can be used in many scenarios such as linking to artifacts in issues or pull requests. Users must be logged-in in order for this URL to work. This URL is valid as long as the artifact has not expired or the artifact, run or repository have not been deleted | `https://github.com/example-org/example-repo/actions/runs/1/artifacts/1234` |
| `artifact-digest` | SHA-256 digest of an Artifact | 0fde654d4c6e659b45783a725dc92f1bfb0baa6c2de64b34e814dc206ff4aaaf |

## Examples

### Upload an Individual File

```yaml
steps:
- run: mkdir -p path/to/artifact
- run: echo hello > path/to/artifact/world.txt
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: path/to/artifact/world.txt
```

### Upload an Entire Directory

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: path/to/artifact/ # or path/to/artifact
```

### Upload using a Wildcard Pattern

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: path/**/[abc]rtifac?/*
```

### Upload using Multiple Paths and Exclusions

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: |
      path/output/bin/
      path/output/test-results
      !path/**/*.tmp
```

For supported wildcards along with behavior and documentation, see [@actions/glob](https://github.com/actions/toolkit/tree/main/packages/glob) which is used internally to search for files.

If a wildcard pattern is used, the path hierarchy will be preserved after the first wildcard pattern:

```
path/to/*/directory/foo?.txt =>
    ∟ path/to/some/directory/foo1.txt
    ∟ path/to/some/directory/foo2.txt
    ∟ path/to/other/directory/foo1.txt

would be flattened and uploaded as =>
    ∟ some/directory/foo1.txt
    ∟ some/directory/foo2.txt
    ∟ other/directory/foo1.txt
```

If multiple paths are provided as input, the least common ancestor of all the search paths will be used as the root directory of the artifact. Exclude paths do not affect the directory structure.

Relative and absolute file paths are both allowed. Relative paths are rooted against the current working directory. Paths that begin with a wildcard character should be quoted to avoid being interpreted as YAML aliases.

### Altering compressions level (speed v. size)

If you are uploading large or easily compressable data to your artifact, you may benefit from tweaking the compression level. By default, the compression level is `6`, the same as GNU Gzip.

The value can range from 0 to 9:
  - 0: No compression
  - 1: Best speed
  - 6: Default compression (same as GNU Gzip)
  - 9: Best compression

Higher levels will result in better compression, but will take longer to complete.
For large files that are not easily compressed, a value of `0` is recommended for significantly faster uploads.

For instance, if you are uploading random binary data, you can save a lot of time by opting out of compression completely, since it won't benefit:

```yaml
- name: Make a 1GB random binary file
  run: |
    dd if=/dev/urandom of=my-1gb-file bs=1M count=1000
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: my-1gb-file
    compression-level: 0 # no compression
```

But, if you are uploading data that is easily compressed (like plaintext, code, etc) you can save space and cost by having a higher compression level. But this will be heavier on the CPU therefore slower to upload:

```yaml
- name: Make a file with a lot of repeated text
  run: |
    for i in {1..100000}; do echo -n 'foobar' >> foobar.txt; done
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: foobar.txt
    compression-level: 9 # maximum compression
```

### Customization if no files are found

If a path (or paths), result in no files being found for the artifact, the action will succeed but print out a warning. In certain scenarios it may be desirable to fail the action or suppress the warning. The `if-no-files-found` option allows you to customize the behavior of the action if no files are found:

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: path/to/artifact/
    if-no-files-found: error # 'warn' or 'ignore' are also available, defaults to `warn`
```

### (Not) Uploading to the same artifact

Unlike earlier versions of `upload-artifact`, uploading to the same artifact via multiple jobs is _not_ supported with `v4`.

```yaml
- run: echo hi > world.txt
- uses: actions/upload-artifact@v4
  with:
    # implicitly named as 'artifact'
    path: world.txt

- run: echo howdy > extra-file.txt
- uses: actions/upload-artifact@v4
  with:
    # also implicitly named as 'artifact', will fail here!
    path: extra-file.txt
```

Artifact names must be unique since each created artifact is idempotent so multiple jobs cannot modify the same artifact.

In matrix scenarios, be careful to not accidentally upload to the same artifact, or else you will encounter conflict errors. It would be best to name the artifact _with_ a prefix or suffix from the matrix:

```yaml
jobs:
  upload:
    name: Generate Build Artifacts

    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        version: [a, b, c]

    runs-on: ${{ matrix.os }}

    steps:
    - name: Build
      run: ./some-script --version=${{ matrix.version }} > my-binary
    - name: Upload
      uses: actions/upload-artifact@v4
      with:
        name: binary-${{ matrix.os }}-${{ matrix.version }}
        path: my-binary
```

This will result in artifacts like: `binary-ubuntu-latest-a`, `binary-windows-latest-b`, and so on.

Previously the behavior _allowed_ for the artifact names to be the same which resulted in unexpected mutations and accidental corruption. Artifacts created by upload-artifact@v4 are immutable.

### Environment Variables and Tilde Expansion

You can use `~` in the path input as a substitute for `$HOME`. Basic tilde expansion is supported:

```yaml
  - run: |
      mkdir -p ~/new/artifact
      echo hello > ~/new/artifact/world.txt
  - uses: actions/upload-artifact@v4
    with:
      name: my-artifacts
      path: ~/new/**/*
```

Environment variables along with context expressions can also be used for input. For documentation see [context and expression syntax](https://help.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions):

```yaml
    env:
      name: my-artifact
    steps:
    - run: |
        mkdir -p ${{ github.workspace }}/artifact
        echo hello > ${{ github.workspace }}/artifact/world.txt
    - uses: actions/upload-artifact@v4
      with:
        name: ${{ env.name }}-name
        path: ${{ github.workspace }}/artifact/**/*
```

For environment variables created in other steps, make sure to use the `env` expression syntax

```yaml
    steps:
    - run: |
        mkdir testing
        echo "This is a file to upload" > testing/file.txt
        echo "artifactPath=testing/file.txt" >> $GITHUB_ENV
    - uses: actions/upload-artifact@v4
      with:
        name: artifact
        path: ${{ env.artifactPath }} # this will resolve to testing/file.txt at runtime
```

### Retention Period

Artifacts are retained for 90 days by default. You can specify a shorter retention period using the `retention-days` input:

```yaml
  - name: Create a file
    run: echo "I won't live long" > my_file.txt

  - name: Upload Artifact
    uses: actions/upload-artifact@v4
    with:
      name: my-artifact
      path: my_file.txt
      retention-days: 5
```

The retention period must be between 1 and 90 inclusive. For more information see [artifact and log retention policies](https://docs.github.com/en/free-pro-team@latest/actions/reference/usage-limits-billing-and-administration#artifact-and-log-retention-policy).

### Using Outputs

If an artifact upload is successful then an `artifact-id` output is available. This ID is a unique identifier that can be used with [Artifact REST APIs](https://docs.github.com/en/rest/actions/artifacts).

#### Example output between steps

```yml
    - uses: actions/upload-artifact@v4
      id: artifact-upload-step
      with:
        name: my-artifact
        path: path/to/artifact/content/

    - name: Output artifact ID
      run:  echo 'Artifact ID is ${{ steps.artifact-upload-step.outputs.artifact-id }}'
```

#### Example output between jobs

```yml
jobs:
  job1:
    runs-on: ubuntu-latest
    outputs:
      output1: ${{ steps.artifact-upload-step.outputs.artifact-id }}
    steps:
      - uses: actions/upload-artifact@v4
        id: artifact-upload-step
        with:
          name: my-artifact
          path: path/to/artifact/content/
  job2:
    runs-on: ubuntu-latest
    needs: job1
    steps:
      - env:
          OUTPUT1: ${{needs.job1.outputs.output1}}
        run: echo "Artifact ID from previous job is $OUTPUT1"
```

### Overwriting an Artifact

Although it's not possible to mutate an Artifact, can completely overwrite one. But do note that this will give the Artifact a new ID, the previous one will no longer exist:

```yaml
jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Create a file
        run: echo "hello world" > my-file.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: my-artifact # NOTE: same artifact name
          path: my-file.txt
  upload-again:
    needs: upload
    runs-on: ubuntu-latest
    steps:
      - name: Create a different file
        run: echo "goodbye world" > my-file.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: my-artifact # NOTE: same artifact name
          path: my-file.txt
          overwrite: true
```

### Uploading Hidden Files

By default, hidden files are ignored by this action to avoid unintentionally uploading sensitive information.

If you need to upload hidden files, you can use the `include-hidden-files` input.
Any files that contain sensitive information that should not be in the uploaded artifact can be excluded
using the `path`:

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    include-hidden-files: true
    path: |
      path/output/
      !path/output/.production.env
```

Hidden files are defined as any file beginning with `.` or files within folders beginning with `.`.
On Windows, files and directories with the hidden attribute are not considered hidden files unless
they have the `.` prefix.

## Limitations

### Number of Artifacts

Within an individual job, there is a limit of 500 artifacts that can be created for that job.

You may also be limited by Artifacts if you have exceeded your shared storage quota. Storage is calculated every 6-12 hours. See [the documentation](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#calculating-minute-and-storage-spending) for more info.

### Zip archives

When an Artifact is uploaded, all the files are assembled into an immutable Zip archive. There is currently no way to download artifacts in a format other than a Zip or to download individual artifact contents.

### Permission Loss

File permissions are not maintained during artifact upload. All directories will have `755` and all files will have `644`. For example, if you make a file executable using `chmod` and then upload that file, post-download the file is no longer guaranteed to be set as an executable.

If you must preserve permissions, you can `tar` all of your files together before artifact upload. Post download, the `tar` file will maintain file permissions and case sensitivity.

```yaml
- name: 'Tar files'
  run: tar -cvf my_files.tar /path/to/my/directory

- name: 'Upload Artifact'
  uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: my_files.tar
```

## Where does the upload go?

At the bottom of the workflow summary page, there is a dedicated section for artifacts. Here's a screenshot of something you might see:

<img src="https://github.com/user-attachments/assets/bcb7120f-f445-4a3e-9596-77f85f7e0af0" width="700" height="300">


There is a trashcan icon that can be used to delete the artifact. This icon will only appear for users who have write permissions to the repository.

The size of the artifact is denoted in bytes. The displayed artifact size denotes the size of the zip that `upload-artifact` creates during upload. The Digest column will display the SHA256 digest of the artifact being uploaded.
```

## File: `action.yml`
```yaml
name: 'Upload a Build Artifact'
description: 'Upload a build artifact that can be used by subsequent workflow steps'
author: 'GitHub'
inputs:
  name:
    description: 'Artifact name. If the `archive` input is `false`, the name of the file uploaded will be the artifact name.'
    default: 'artifact'
  path:
    description: 'A file, directory or wildcard pattern that describes what to upload.'
    required: true
  if-no-files-found:
    description: >
      The desired behavior if no files are found using the provided path.

      Available Options:
        warn: Output a warning but do not fail the action
        error: Fail the action with an error message
        ignore: Do not output any warnings or errors, the action does not fail
    default: 'warn'
  retention-days:
    description: >
      Duration after which artifact will expire in days. 0 means using default retention.

      Minimum 1 day.
      Maximum 90 days unless changed from the repository settings page.
  compression-level:
    description: >
      The level of compression for Zlib to be applied to the artifact archive.
      The value can range from 0 to 9:
      - 0: No compression
      - 1: Best speed
      - 6: Default compression (same as GNU Gzip)
      - 9: Best compression
      Higher levels will result in better compression, but will take longer to complete.
      For large files that are not easily compressed, a value of 0 is recommended for significantly faster uploads.
    default: '6'
  overwrite:
    description: >
      If true, an artifact with a matching name will be deleted before a new one is uploaded.
      If false, the action will fail if an artifact for the given name already exists.
      Does not fail if the artifact does not exist.
    default: 'false'
  include-hidden-files:
    description: >
      If true, hidden files will be included in the artifact.
      If false, hidden files will be excluded from the artifact.
    default: 'false'
  archive:
    description: >
      If true, the artifact will be archived (zipped) before uploading.
      If false, the artifact will be uploaded as-is without archiving.
      When `archive` is `false`, only a single file can be uploaded. The name of the file will be used as the artifact name (ignoring the `name` parameter).
    default: 'true'

outputs:
  artifact-id:
    description: >
      A unique identifier for the artifact that was just uploaded. Empty if the artifact upload failed.

      This ID can be used as input to other APIs to download, delete or get more information about an artifact: https://docs.github.com/en/rest/actions/artifacts
  artifact-url:
    description: >
      A download URL for the artifact that was just uploaded. Empty if the artifact upload failed.

      This download URL only works for requests Authenticated with GitHub. Anonymous downloads will be prompted to first login. 
      If an anonymous download URL is needed than a short time restricted URL can be generated using the download artifact API: https://docs.github.com/en/rest/actions/artifacts#download-an-artifact    

      This URL will be valid for as long as the artifact exists and the workflow run and repository exists. Once an artifact has expired this URL will no longer work.
      Common uses cases for such a download URL can be adding download links to artifacts in descriptions or comments on pull requests or issues.
  artifact-digest:
    description: >
      SHA-256 digest for the artifact that was just uploaded. Empty if the artifact upload failed.
runs:
  using: 'node24'
  main: 'dist/upload/index.js'
```

## File: `eslint.config.mjs`
```
import github from 'eslint-plugin-github'
import jest from 'eslint-plugin-jest'
import prettier from 'eslint-plugin-prettier/recommended'

const githubConfigs = github.getFlatConfigs()

export default [
  {
    ignores: ['**/node_modules/**', '**/lib/**', '**/dist/**']
  },
  githubConfigs.recommended,
  ...githubConfigs.typescript,
  prettier,
  {
    files: ['**/*.ts'],
    languageOptions: {
      parserOptions: {
        project: './tsconfig.eslint.json'
      }
    },
    rules: {
      'prettier/prettier': ['error', {endOfLine: 'auto'}],
      'eslint-comments/no-use': 'off',
      'github/no-then': 'off',
      'github/filenames-match-regex': 'off',
      'github/array-foreach': 'off',
      'import/no-namespace': 'off',
      'import/named': 'off',
      'import/no-unresolved': 'off',
      'i18n-text/no-en': 'off',
      'filenames/match-regex': 'off',
      'no-shadow': 'off',
      'no-unused-vars': 'off',
      'no-undef': 'off',
      camelcase: 'off',
      '@typescript-eslint/no-unused-vars': 'off',
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-shadow': 'off',
      '@typescript-eslint/array-type': 'off',
      '@typescript-eslint/no-require-imports': 'off'
    }
  },
  {
    files: ['**/__tests__/**/*.ts'],
    ...jest.configs['flat/recommended'],
    rules: {
      ...jest.configs['flat/recommended'].rules,
      'jest/expect-expect': 'off',
      'jest/no-conditional-expect': 'off'
    }
  }
]
```

## File: `jest.config.ts`
```typescript
export default {
  clearMocks: true,
  moduleFileExtensions: ['js', 'ts'],
  roots: ['<rootDir>'],
  testEnvironment: 'node',
  testMatch: ['**/*.test.ts'],
  transform: {
    '^.+\\.ts$': [
      'ts-jest',
      {
        useESM: true,
        diagnostics: {
          ignoreCodes: [151002]
        }
      }
    ]
  },
  extensionsToTreatAsEsm: ['.ts'],
  transformIgnorePatterns: ['node_modules/(?!(@actions)/)'],
  moduleNameMapper: {
    '^(\\.{1,2}/.*)\\.js$': '$1'
  },
  verbose: true
}
```

## File: `package.json`
```json
{
  "name": "upload-artifact",
  "version": "7.0.0",
  "description": "Upload an Actions Artifact in a workflow run",
  "type": "module",
  "main": "dist/upload/index.js",
  "scripts": {
    "build": "tsc",
    "release": "ncc build src/upload/index.ts -o dist/upload && ncc build src/merge/index.ts -o dist/merge",
    "check-all": "concurrently \"npm:format-check\" \"npm:lint\" \"npm:test\" \"npm:build\"",
    "format": "prettier --write **/*.ts",
    "format-check": "prettier --check **/*.ts",
    "lint": "eslint **/*.ts",
    "test": "node --experimental-vm-modules node_modules/jest/bin/jest.js --testTimeout 10000"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/actions/upload-artifact.git"
  },
  "keywords": [
    "Actions",
    "GitHub",
    "Artifacts",
    "Upload"
  ],
  "author": "GitHub",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/actions/upload-artifact/issues"
  },
  "homepage": "https://github.com/actions/upload-artifact#readme",
  "engines": {
    "node": ">=24"
  },
  "dependencies": {
    "@actions/artifact": "^6.2.0",
    "@actions/core": "^3.0.0",
    "@actions/github": "^9.0.0",
    "@actions/glob": "^0.6.1",
    "@actions/io": "^3.0.2",
    "minimatch": "^10.1.1"
  },
  "devDependencies": {
    "@types/jest": "^30.0.0",
    "@types/node": "^25.1.0",
    "@typescript-eslint/eslint-plugin": "^8.54.0",
    "@typescript-eslint/parser": "^8.54.0",
    "@vercel/ncc": "^0.38.4",
    "concurrently": "^9.2.1",
    "eslint": "^9.39.2",
    "eslint-plugin-github": "^6.0.0",
    "eslint-plugin-jest": "^29.12.1",
    "eslint-plugin-prettier": "^5.5.5",
    "jest": "^30.2.0",
    "prettier": "^3.8.1",
    "ts-jest": "^29.2.6",
    "ts-node": "^10.9.2",
    "typescript": "^5.3.3"
  },
  "overrides": {
    "uri-js": "npm:uri-js-replace@^1.0.1"
  }
}
```

## File: `tsconfig.eslint.json`
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "rootDir": "."
  },
  "include": ["src/**/*.ts", "__tests__/**/*.ts", "*.ts"],
  "exclude": ["node_modules", "lib", "dist"]
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "outDir": "./lib",
    "rootDir": "./src",
    "strict": true,
    "noImplicitAny": false,
    "moduleResolution": "NodeNext",
    "esModuleInterop": true
  },
  "exclude": ["node_modules", "**/*.test.ts", "jest.config.ts", "__tests__"]
}
```

## File: `__tests__/merge.test.ts`
```typescript
import {jest, describe, test, expect, beforeEach} from '@jest/globals'

// Mock @actions/github before importing modules that use it
jest.unstable_mockModule('@actions/github', () => ({
  context: {
    repo: {
      owner: 'actions',
      repo: 'toolkit'
    },
    runId: 123,
    serverUrl: 'https://github.com'
  },
  getOctokit: jest.fn()
}))

// Mock @actions/core
jest.unstable_mockModule('@actions/core', () => ({
  getInput: jest.fn(),
  getBooleanInput: jest.fn(),
  setOutput: jest.fn(),
  setFailed: jest.fn(),
  setSecret: jest.fn(),
  info: jest.fn(),
  warning: jest.fn(),
  debug: jest.fn(),
  error: jest.fn(),
  notice: jest.fn(),
  startGroup: jest.fn(),
  endGroup: jest.fn(),
  isDebug: jest.fn(() => false),
  getState: jest.fn(),
  saveState: jest.fn(),
  exportVariable: jest.fn(),
  addPath: jest.fn(),
  group: jest.fn((name: string, fn: () => Promise<unknown>) => fn()),
  toPlatformPath: jest.fn((p: string) => p),
  toWin32Path: jest.fn((p: string) => p),
  toPosixPath: jest.fn((p: string) => p)
}))

// Mock fs/promises
const actualFsPromises = await import('fs/promises')
jest.unstable_mockModule('fs/promises', () => ({
  ...actualFsPromises,
  mkdtemp: jest
    .fn<() => Promise<string>>()
    .mockResolvedValue('/tmp/merge-artifact'),
  rm: jest.fn<() => Promise<void>>().mockResolvedValue(undefined)
}))

// Mock shared search module
const mockFindFilesToUpload =
  jest.fn<() => Promise<{filesToUpload: string[]; rootDirectory: string}>>()
jest.unstable_mockModule('../src/shared/search.js', () => ({
  findFilesToUpload: mockFindFilesToUpload
}))

// Dynamic imports after mocking
const core = await import('@actions/core')
const artifact = await import('@actions/artifact')
const {run} = await import('../src/merge/merge-artifacts.js')
const {Inputs} = await import('../src/merge/constants.js')

const fixtures = {
  artifactName: 'my-merged-artifact',
  tmpDirectory: '/tmp/merge-artifact',
  filesToUpload: [
    '/some/artifact/path/file-a.txt',
    '/some/artifact/path/file-b.txt',
    '/some/artifact/path/file-c.txt'
  ],
  artifacts: [
    {
      name: 'my-artifact-a',
      id: 1,
      size: 100,
      createdAt: new Date('2024-01-01T00:00:00Z')
    },
    {
      name: 'my-artifact-b',
      id: 2,
      size: 100,
      createdAt: new Date('2024-01-01T00:00:00Z')
    },
    {
      name: 'my-artifact-c',
      id: 3,
      size: 100,
      createdAt: new Date('2024-01-01T00:00:00Z')
    }
  ]
}

const mockInputs = (
  overrides?: Partial<{[K in (typeof Inputs)[keyof typeof Inputs]]?: any}>
) => {
  const inputs: Record<string, any> = {
    [Inputs.Name]: 'my-merged-artifact',
    [Inputs.Pattern]: '*',
    [Inputs.SeparateDirectories]: false,
    [Inputs.RetentionDays]: 0,
    [Inputs.CompressionLevel]: 6,
    [Inputs.DeleteMerged]: false,
    ...overrides
  }

  ;(core.getInput as jest.Mock<typeof core.getInput>).mockImplementation(
    (name: string) => {
      return inputs[name]
    }
  )
  ;(
    core.getBooleanInput as jest.Mock<typeof core.getBooleanInput>
  ).mockImplementation((name: string) => {
    return inputs[name]
  })

  return inputs
}

describe('merge', () => {
  beforeEach(async () => {
    mockInputs()
    jest.clearAllMocks()

    jest
      .spyOn(artifact.default, 'listArtifacts')
      .mockResolvedValue({artifacts: fixtures.artifacts})

    jest.spyOn(artifact.default, 'downloadArtifact').mockResolvedValue({
      downloadPath: fixtures.tmpDirectory
    })

    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: fixtures.filesToUpload,
      rootDirectory: fixtures.tmpDirectory
    })

    jest.spyOn(artifact.default, 'uploadArtifact').mockResolvedValue({
      size: 123,
      id: 1337
    })

    jest
      .spyOn(artifact.default, 'deleteArtifact')
      .mockImplementation(async (artifactName: string) => {
        const found = fixtures.artifacts.find(a => a.name === artifactName)
        if (!found) throw new Error(`Artifact ${artifactName} not found`)
        return {id: found.id}
      })
  })

  test('merges artifacts', async () => {
    await run()

    for (const a of fixtures.artifacts) {
      expect(artifact.default.downloadArtifact).toHaveBeenCalledWith(a.id, {
        path: fixtures.tmpDirectory
      })
    }

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.tmpDirectory,
      {compressionLevel: 6}
    )
  })

  test('fails if no artifacts found', async () => {
    mockInputs({[Inputs.Pattern]: 'this-does-not-match'})

    await expect(run()).rejects.toThrow()

    expect(artifact.default.uploadArtifact).not.toHaveBeenCalled()
    expect(artifact.default.downloadArtifact).not.toHaveBeenCalled()
  })

  test('supports custom compression level', async () => {
    mockInputs({
      [Inputs.CompressionLevel]: 2
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.tmpDirectory,
      {compressionLevel: 2}
    )
  })

  test('supports custom retention days', async () => {
    mockInputs({
      [Inputs.RetentionDays]: 7
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.tmpDirectory,
      {retentionDays: 7, compressionLevel: 6}
    )
  })

  test('supports deleting artifacts after merge', async () => {
    mockInputs({
      [Inputs.DeleteMerged]: true
    })

    await run()

    for (const a of fixtures.artifacts) {
      expect(artifact.default.deleteArtifact).toHaveBeenCalledWith(a.name)
    }
  })
})
```

## File: `__tests__/search.test.ts`
```typescript
import {jest, describe, test, expect, beforeAll} from '@jest/globals'
import * as path from 'path'
import * as io from '@actions/io'
import {promises as fs} from 'fs'
import {fileURLToPath} from 'url'

// Mock @actions/core to suppress output during tests
jest.unstable_mockModule('@actions/core', () => ({
  getInput: jest.fn(),
  getBooleanInput: jest.fn(),
  setOutput: jest.fn(),
  setFailed: jest.fn(),
  setSecret: jest.fn(),
  info: jest.fn(),
  warning: jest.fn(),
  debug: jest.fn(),
  error: jest.fn(),
  notice: jest.fn(),
  startGroup: jest.fn(),
  endGroup: jest.fn(),
  isDebug: jest.fn(() => false),
  getState: jest.fn(),
  saveState: jest.fn(),
  exportVariable: jest.fn(),
  addPath: jest.fn(),
  group: jest.fn((name: string, fn: () => Promise<unknown>) => fn()),
  toPlatformPath: jest.fn((p: string) => p),
  toWin32Path: jest.fn((p: string) => p),
  toPosixPath: jest.fn((p: string) => p)
}))

const {findFilesToUpload} = await import('../src/shared/search.js')

const __dirname = path.dirname(fileURLToPath(import.meta.url))

const root = path.join(__dirname, '_temp', 'search')
const searchItem1Path = path.join(
  root,
  'folder-a',
  'folder-b',
  'folder-c',
  'search-item1.txt'
)
const searchItem2Path = path.join(root, 'folder-d', 'search-item2.txt')
const searchItem3Path = path.join(root, 'folder-d', 'search-item3.txt')
const searchItem4Path = path.join(root, 'folder-d', 'search-item4.txt')
const searchItem5Path = path.join(root, 'search-item5.txt')
const extraSearchItem1Path = path.join(
  root,
  'folder-a',
  'folder-b',
  'folder-c',
  'extraSearch-item1.txt'
)
const extraSearchItem2Path = path.join(
  root,
  'folder-d',
  'extraSearch-item2.txt'
)
const extraSearchItem3Path = path.join(
  root,
  'folder-f',
  'extraSearch-item3.txt'
)
const extraSearchItem4Path = path.join(
  root,
  'folder-h',
  'folder-i',
  'extraSearch-item4.txt'
)
const extraSearchItem5Path = path.join(
  root,
  'folder-h',
  'folder-i',
  'extraSearch-item5.txt'
)
const extraFileInFolderCPath = path.join(
  root,
  'folder-a',
  'folder-b',
  'folder-c',
  'extra-file-in-folder-c.txt'
)
const amazingFileInFolderHPath = path.join(root, 'folder-h', 'amazing-item.txt')
const lonelyFilePath = path.join(
  root,
  'folder-h',
  'folder-j',
  'folder-k',
  'lonely-file.txt'
)

const hiddenFile = path.join(root, '.hidden-file.txt')
const fileInHiddenFolderPath = path.join(
  root,
  '.hidden-folder',
  'folder-in-hidden-folder',
  'file.txt'
)
const fileInHiddenFolderInFolderA = path.join(
  root,
  'folder-a',
  '.hidden-folder-in-folder-a',
  'file.txt'
)

describe('Search', () => {
  beforeAll(async () => {
    // mock console.log to reduce noise
    jest.spyOn(console, 'log').mockImplementation(() => {})

    // clear temp directory
    await io.rmRF(root)
    await fs.mkdir(path.join(root, 'folder-a', 'folder-b', 'folder-c'), {
      recursive: true
    })
    await fs.mkdir(path.join(root, 'folder-a', 'folder-b', 'folder-e'), {
      recursive: true
    })
    await fs.mkdir(path.join(root, 'folder-d'), {
      recursive: true
    })
    await fs.mkdir(path.join(root, 'folder-f'), {
      recursive: true
    })
    await fs.mkdir(path.join(root, 'folder-g'), {
      recursive: true
    })
    await fs.mkdir(path.join(root, 'folder-h', 'folder-i'), {
      recursive: true
    })
    await fs.mkdir(path.join(root, 'folder-h', 'folder-j', 'folder-k'), {
      recursive: true
    })

    await fs.mkdir(
      path.join(root, '.hidden-folder', 'folder-in-hidden-folder'),
      {recursive: true}
    )
    await fs.mkdir(path.join(root, 'folder-a', '.hidden-folder-in-folder-a'), {
      recursive: true
    })

    await fs.writeFile(searchItem1Path, 'search item1 file')
    await fs.writeFile(searchItem2Path, 'search item2 file')
    await fs.writeFile(searchItem3Path, 'search item3 file')
    await fs.writeFile(searchItem4Path, 'search item4 file')
    await fs.writeFile(searchItem5Path, 'search item5 file')

    await fs.writeFile(extraSearchItem1Path, 'extraSearch item1 file')
    await fs.writeFile(extraSearchItem2Path, 'extraSearch item2 file')
    await fs.writeFile(extraSearchItem3Path, 'extraSearch item3 file')
    await fs.writeFile(extraSearchItem4Path, 'extraSearch item4 file')
    await fs.writeFile(extraSearchItem5Path, 'extraSearch item5 file')

    await fs.writeFile(extraFileInFolderCPath, 'extra file')

    await fs.writeFile(amazingFileInFolderHPath, 'amazing file')

    await fs.writeFile(lonelyFilePath, 'all by itself')

    await fs.writeFile(hiddenFile, 'hidden file')
    await fs.writeFile(fileInHiddenFolderPath, 'file in hidden directory')
    await fs.writeFile(fileInHiddenFolderInFolderA, 'file in hidden directory')
  })

  test('Single file search - Absolute Path', async () => {
    const searchResult = await findFilesToUpload(extraFileInFolderCPath)
    expect(searchResult.filesToUpload.length).toEqual(1)
    expect(searchResult.filesToUpload[0]).toEqual(extraFileInFolderCPath)
    expect(searchResult.rootDirectory).toEqual(
      path.join(root, 'folder-a', 'folder-b', 'folder-c')
    )
  })

  test('Single file search - Relative Path', async () => {
    const relativePath = path.join(
      '__tests__',
      '_temp',
      'search',
      'folder-a',
      'folder-b',
      'folder-c',
      'search-item1.txt'
    )

    const searchResult = await findFilesToUpload(relativePath)
    expect(searchResult.filesToUpload.length).toEqual(1)
    expect(searchResult.filesToUpload[0]).toEqual(searchItem1Path)
    expect(searchResult.rootDirectory).toEqual(
      path.join(root, 'folder-a', 'folder-b', 'folder-c')
    )
  })

  test('Single file using wildcard', async () => {
    const expectedRoot = path.join(root, 'folder-h')
    const searchPath = path.join(root, 'folder-h', '**/*lonely*')
    const searchResult = await findFilesToUpload(searchPath)
    expect(searchResult.filesToUpload.length).toEqual(1)
    expect(searchResult.filesToUpload[0]).toEqual(lonelyFilePath)
    expect(searchResult.rootDirectory).toEqual(expectedRoot)
  })

  test('Single file using directory', async () => {
    const searchPath = path.join(root, 'folder-h', 'folder-j')
    const searchResult = await findFilesToUpload(searchPath)
    expect(searchResult.filesToUpload.length).toEqual(1)
    expect(searchResult.filesToUpload[0]).toEqual(lonelyFilePath)
    expect(searchResult.rootDirectory).toEqual(searchPath)
  })

  test('Directory search - Absolute Path', async () => {
    const searchPath = path.join(root, 'folder-h')
    const searchResult = await findFilesToUpload(searchPath)
    expect(searchResult.filesToUpload.length).toEqual(4)

    expect(
      searchResult.filesToUpload.includes(amazingFileInFolderHPath)
    ).toEqual(true)
    expect(searchResult.filesToUpload.includes(extraSearchItem4Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem5Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(lonelyFilePath)).toEqual(true)

    expect(searchResult.rootDirectory).toEqual(searchPath)
  })

  test('Directory search - Relative Path', async () => {
    const searchPath = path.join('__tests__', '_temp', 'search', 'folder-h')
    const expectedRootDirectory = path.join(root, 'folder-h')
    const searchResult = await findFilesToUpload(searchPath)
    expect(searchResult.filesToUpload.length).toEqual(4)

    expect(
      searchResult.filesToUpload.includes(amazingFileInFolderHPath)
    ).toEqual(true)
    expect(searchResult.filesToUpload.includes(extraSearchItem4Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem5Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(lonelyFilePath)).toEqual(true)

    expect(searchResult.rootDirectory).toEqual(expectedRootDirectory)
  })

  test('Wildcard search - Absolute Path', async () => {
    const searchPath = path.join(root, '**/*[Ss]earch*')
    const searchResult = await findFilesToUpload(searchPath)
    expect(searchResult.filesToUpload.length).toEqual(10)

    expect(searchResult.filesToUpload.includes(searchItem1Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem2Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem3Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem4Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem5Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(extraSearchItem1Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem2Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem3Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem4Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem5Path)).toEqual(
      true
    )

    expect(searchResult.rootDirectory).toEqual(root)
  })

  test('Wildcard search - Relative Path', async () => {
    const searchPath = path.join(
      '__tests__',
      '_temp',
      'search',
      '**/*[Ss]earch*'
    )
    const searchResult = await findFilesToUpload(searchPath)
    expect(searchResult.filesToUpload.length).toEqual(10)

    expect(searchResult.filesToUpload.includes(searchItem1Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem2Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem3Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem4Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem5Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(extraSearchItem1Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem2Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem3Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem4Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem5Path)).toEqual(
      true
    )

    expect(searchResult.rootDirectory).toEqual(root)
  })

  test('Multi path search - root directory', async () => {
    const searchPath1 = path.join(root, 'folder-a')
    const searchPath2 = path.join(root, 'folder-d')

    const searchPaths = `${searchPath1}\n${searchPath2}`
    const searchResult = await findFilesToUpload(searchPaths)

    expect(searchResult.rootDirectory).toEqual(root)
    expect(searchResult.filesToUpload.length).toEqual(7)
    expect(searchResult.filesToUpload.includes(searchItem1Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem2Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem3Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem4Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(extraSearchItem1Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem2Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraFileInFolderCPath)).toEqual(
      true
    )
  })

  test('Multi path search - with exclude character', async () => {
    const searchPath1 = path.join(root, 'folder-a')
    const searchPath2 = path.join(root, 'folder-d')
    const searchPath3 = path.join(root, 'folder-a', 'folder-b', '**/extra*.txt')

    // negating the third search path
    const searchPaths = `${searchPath1}\n${searchPath2}\n!${searchPath3}`
    const searchResult = await findFilesToUpload(searchPaths)

    expect(searchResult.rootDirectory).toEqual(root)
    expect(searchResult.filesToUpload.length).toEqual(5)
    expect(searchResult.filesToUpload.includes(searchItem1Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem2Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem3Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(searchItem4Path)).toEqual(true)
    expect(searchResult.filesToUpload.includes(extraSearchItem2Path)).toEqual(
      true
    )
  })

  test('Multi path search - non root directory', async () => {
    const searchPath1 = path.join(root, 'folder-h', 'folder-i')
    const searchPath2 = path.join(root, 'folder-h', 'folder-j', 'folder-k')
    const searchPath3 = amazingFileInFolderHPath

    const searchPaths = [searchPath1, searchPath2, searchPath3].join('\n')
    const searchResult = await findFilesToUpload(searchPaths)

    expect(searchResult.rootDirectory).toEqual(path.join(root, 'folder-h'))
    expect(searchResult.filesToUpload.length).toEqual(4)
    expect(
      searchResult.filesToUpload.includes(amazingFileInFolderHPath)
    ).toEqual(true)
    expect(searchResult.filesToUpload.includes(extraSearchItem4Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(extraSearchItem5Path)).toEqual(
      true
    )
    expect(searchResult.filesToUpload.includes(lonelyFilePath)).toEqual(true)
  })

  test('Hidden files ignored by default', async () => {
    const searchPath = path.join(root, '**/*')
    const searchResult = await findFilesToUpload(searchPath)

    expect(searchResult.filesToUpload).not.toContain(hiddenFile)
    expect(searchResult.filesToUpload).not.toContain(fileInHiddenFolderPath)
    expect(searchResult.filesToUpload).not.toContain(
      fileInHiddenFolderInFolderA
    )
  })

  test('Hidden files included', async () => {
    const searchPath = path.join(root, '**/*')
    const searchResult = await findFilesToUpload(searchPath, true)

    expect(searchResult.filesToUpload).toContain(hiddenFile)
    expect(searchResult.filesToUpload).toContain(fileInHiddenFolderPath)
    expect(searchResult.filesToUpload).toContain(fileInHiddenFolderInFolderA)
  })
})
```

## File: `__tests__/upload.test.ts`
```typescript
import {jest, describe, test, expect, beforeEach} from '@jest/globals'

// Mock @actions/github before importing modules that use it
jest.unstable_mockModule('@actions/github', () => ({
  context: {
    repo: {
      owner: 'actions',
      repo: 'toolkit'
    },
    runId: 123,
    serverUrl: 'https://github.com'
  },
  getOctokit: jest.fn()
}))

// Mock @actions/core
jest.unstable_mockModule('@actions/core', () => ({
  getInput: jest.fn(),
  getBooleanInput: jest.fn(),
  setOutput: jest.fn(),
  setFailed: jest.fn(),
  setSecret: jest.fn(),
  info: jest.fn(),
  warning: jest.fn(),
  debug: jest.fn(),
  error: jest.fn(),
  notice: jest.fn(),
  startGroup: jest.fn(),
  endGroup: jest.fn(),
  isDebug: jest.fn(() => false),
  getState: jest.fn(),
  saveState: jest.fn(),
  exportVariable: jest.fn(),
  addPath: jest.fn(),
  group: jest.fn((name: string, fn: () => Promise<unknown>) => fn()),
  toPlatformPath: jest.fn((p: string) => p),
  toWin32Path: jest.fn((p: string) => p),
  toPosixPath: jest.fn((p: string) => p)
}))

// Mock shared search module
const mockFindFilesToUpload =
  jest.fn<() => Promise<{filesToUpload: string[]; rootDirectory: string}>>()
jest.unstable_mockModule('../src/shared/search.js', () => ({
  findFilesToUpload: mockFindFilesToUpload
}))

// Dynamic imports after mocking
const core = await import('@actions/core')
const github = await import('@actions/github')
const artifact = await import('@actions/artifact')
const {run} = await import('../src/upload/upload-artifact.js')
const {Inputs} = await import('../src/upload/constants.js')
const {ArtifactNotFoundError} = artifact

const fixtures = {
  artifactName: 'artifact-name',
  rootDirectory: '/some/artifact/path',
  filesToUpload: [
    '/some/artifact/path/file1.txt',
    '/some/artifact/path/file2.txt'
  ]
}

const mockInputs = (
  overrides?: Partial<{[K in (typeof Inputs)[keyof typeof Inputs]]?: any}>
) => {
  const inputs: Record<string, any> = {
    [Inputs.Name]: 'artifact-name',
    [Inputs.Path]: '/some/artifact/path',
    [Inputs.IfNoFilesFound]: 'warn',
    [Inputs.RetentionDays]: 0,
    [Inputs.CompressionLevel]: 6,
    [Inputs.Overwrite]: false,
    [Inputs.Archive]: true,
    ...overrides
  }

  ;(core.getInput as jest.Mock<typeof core.getInput>).mockImplementation(
    (name: string) => {
      return inputs[name]
    }
  )
  ;(
    core.getBooleanInput as jest.Mock<typeof core.getBooleanInput>
  ).mockImplementation((name: string) => {
    return inputs[name]
  })

  return inputs
}

describe('upload', () => {
  beforeEach(async () => {
    mockInputs()
    jest.clearAllMocks()

    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: fixtures.filesToUpload,
      rootDirectory: fixtures.rootDirectory
    })

    jest.spyOn(artifact.default, 'uploadArtifact').mockResolvedValue({
      size: 123,
      id: 1337,
      digest: 'facefeed'
    })
  })

  test('uploads a single file', async () => {
    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: [fixtures.filesToUpload[0]],
      rootDirectory: fixtures.rootDirectory
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      [fixtures.filesToUpload[0]],
      fixtures.rootDirectory,
      {compressionLevel: 6}
    )
  })

  test('uploads multiple files', async () => {
    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.rootDirectory,
      {compressionLevel: 6}
    )
  })

  test('sets outputs', async () => {
    await run()

    expect(core.setOutput).toHaveBeenCalledWith('artifact-id', 1337)
    expect(core.setOutput).toHaveBeenCalledWith('artifact-digest', 'facefeed')
    expect(core.setOutput).toHaveBeenCalledWith(
      'artifact-url',
      `${github.context.serverUrl}/${github.context.repo.owner}/${github.context.repo.repo}/actions/runs/${github.context.runId}/artifacts/${1337}`
    )
  })

  test('supports custom compression level', async () => {
    mockInputs({
      [Inputs.CompressionLevel]: 2
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.rootDirectory,
      {compressionLevel: 2}
    )
  })

  test('supports custom retention days', async () => {
    mockInputs({
      [Inputs.RetentionDays]: 7
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.rootDirectory,
      {retentionDays: 7, compressionLevel: 6}
    )
  })

  test('supports warn if-no-files-found', async () => {
    mockInputs({
      [Inputs.IfNoFilesFound]: 'warn'
    })

    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: [],
      rootDirectory: fixtures.rootDirectory
    })

    await run()

    expect(core.warning).toHaveBeenCalledWith(
      `No files were found with the provided path: ${fixtures.rootDirectory}. No artifacts will be uploaded.`
    )
  })

  test('supports error if-no-files-found', async () => {
    mockInputs({
      [Inputs.IfNoFilesFound]: 'error'
    })

    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: [],
      rootDirectory: fixtures.rootDirectory
    })

    await run()

    expect(core.setFailed).toHaveBeenCalledWith(
      `No files were found with the provided path: ${fixtures.rootDirectory}. No artifacts will be uploaded.`
    )
  })

  test('supports ignore if-no-files-found', async () => {
    mockInputs({
      [Inputs.IfNoFilesFound]: 'ignore'
    })

    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: [],
      rootDirectory: fixtures.rootDirectory
    })

    await run()

    expect(core.info).toHaveBeenCalledWith(
      `No files were found with the provided path: ${fixtures.rootDirectory}. No artifacts will be uploaded.`
    )
  })

  test('supports overwrite', async () => {
    mockInputs({
      [Inputs.Overwrite]: true
    })

    jest.spyOn(artifact.default, 'deleteArtifact').mockResolvedValue({
      id: 1337
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.rootDirectory,
      {compressionLevel: 6}
    )

    expect(artifact.default.deleteArtifact).toHaveBeenCalledWith(
      fixtures.artifactName
    )
  })

  test('supports overwrite and continues if not found', async () => {
    mockInputs({
      [Inputs.Overwrite]: true
    })

    jest
      .spyOn(artifact.default, 'deleteArtifact')
      .mockRejectedValue(new ArtifactNotFoundError('not found'))

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      fixtures.filesToUpload,
      fixtures.rootDirectory,
      {compressionLevel: 6}
    )

    expect(artifact.default.deleteArtifact).toHaveBeenCalledWith(
      fixtures.artifactName
    )
    expect(core.debug).toHaveBeenCalledWith(
      `Skipping deletion of '${fixtures.artifactName}', it does not exist`
    )
  })

  test('passes skipArchive when archive is false', async () => {
    mockInputs({
      [Inputs.Archive]: false
    })

    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: [fixtures.filesToUpload[0]],
      rootDirectory: fixtures.rootDirectory
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      [fixtures.filesToUpload[0]],
      fixtures.rootDirectory,
      {compressionLevel: 6, skipArchive: true}
    )
  })

  test('does not pass skipArchive when archive is true', async () => {
    mockInputs({
      [Inputs.Archive]: true
    })

    mockFindFilesToUpload.mockResolvedValue({
      filesToUpload: [fixtures.filesToUpload[0]],
      rootDirectory: fixtures.rootDirectory
    })

    await run()

    expect(artifact.default.uploadArtifact).toHaveBeenCalledWith(
      fixtures.artifactName,
      [fixtures.filesToUpload[0]],
      fixtures.rootDirectory,
      {compressionLevel: 6}
    )
  })

  test('fails when archive is false and multiple files are provided', async () => {
    mockInputs({
      [Inputs.Archive]: false
    })

    await run()

    expect(core.setFailed).toHaveBeenCalledWith(
      `When 'archive' is set to false, only a single file can be uploaded. Found ${fixtures.filesToUpload.length} files to upload.`
    )
    expect(artifact.default.uploadArtifact).not.toHaveBeenCalled()
  })
})
```

## File: `brain/knowledge/docs_legacy/MIGRATION.md`
```markdown
# Migration

- [Migration](#migration)
  - [Multiple uploads to the same named Artifact](#multiple-uploads-to-the-same-named-artifact)
  - [Overwriting an Artifact](#overwriting-an-artifact)
  - [Merging multiple artifacts](#merging-multiple-artifacts)
  - [Hidden files](#hidden-files)

Several behavioral differences exist between Artifact actions `v3` and below vs `v4`. This document outlines common scenarios in `v3`, and how they would be handled in `v4`.

## Multiple uploads to the same named Artifact

In `v3`, Artifacts are _mutable_ so it's possible to write workflow scenarios where multiple jobs upload to the same Artifact like so:

```yaml
jobs:
  upload:
    strategy:
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.runs-on }}
    steps:
      - name: Create a File
        run: echo "hello from ${{ matrix.runs-on }}" > file-${{ matrix.runs-on }}.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v3
        with:
          name: my-artifact # NOTE: same artifact name
          path: file-${{ matrix.runs-on }}.txt
  download:
    needs: upload
    runs-on: ubuntu-latest
    steps:
      - name: Download All Artifacts
        uses: actions/download-artifact@v3
        with:
          name: my-artifact
          path: my-artifact
      - run: ls -R my-artifact
```

This results in a directory like so:

```
my-artifact/
  file-macos-latest.txt
  file-ubuntu-latest.txt
  file-windows-latest.txt
```

In v4, Artifacts are immutable (unless deleted). So you must change each of the uploaded Artifacts to have a different name and filter the downloads by name to achieve the same effect:

```diff
jobs:
  upload:
    strategy:
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.runs-on }}
    steps:
    - name: Create a File
      run: echo "hello from ${{ matrix.runs-on }}" > file-${{ matrix.runs-on }}.txt
    - name: Upload Artifact
-     uses: actions/upload-artifact@v3
+     uses: actions/upload-artifact@v4
      with:
-       name: my-artifact
+       name: my-artifact-${{ matrix.runs-on }}
        path: file-${{ matrix.runs-on }}.txt
  download:
    needs: upload
    runs-on: ubuntu-latest
    steps:
    - name: Download All Artifacts
-     uses: actions/download-artifact@v3
+     uses: actions/download-artifact@v4
      with:
-       name: my-artifact
        path: my-artifact
+       pattern: my-artifact-*
+       merge-multiple: true
    - run: ls -R my-artifact
```

In `v4`, the new `pattern:` input will filter the downloaded Artifacts to match the name specified. The new `merge-multiple:` input will support downloading multiple Artifacts to the same directory. If the files within the Artifacts have the same name, the last writer wins.

## Overwriting an Artifact

In `v3`, the contents of an Artifact were mutable so something like the following was possible:

```yaml
jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Create a file
        run: echo "hello world" > my-file.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v3
        with:
          name: my-artifact # NOTE: same artifact name
          path: my-file.txt
  upload-again:
    needs: upload
    runs-on: ubuntu-latest
    steps:
      - name: Create a different file
        run: echo "goodbye world" > my-file.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v3
        with:
          name: my-artifact # NOTE: same artifact name
          path: my-file.txt
```

The resulting `my-file.txt` in `my-artifact` will have "goodbye world" as the content.

In `v4`, Artifacts are immutable unless deleted. To achieve this same behavior, you can use `overwrite: true` to delete the Artifact before a new one is created:

```diff
jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Create a file
        run: echo "hello world" > my-file.txt
      - name: Upload Artifact
-       uses: actions/upload-artifact@v3
+       uses: actions/upload-artifact@v4
        with:
          name: my-artifact # NOTE: same artifact name
          path: my-file.txt
  upload-again:
    needs: upload
    runs-on: ubuntu-latest
    steps:
      - name: Create a different file
        run: echo "goodbye world" > my-file.txt
      - name: Upload Artifact
-       uses: actions/upload-artifact@v3
+       uses: actions/upload-artifact@v4
        with:
          name: my-artifact # NOTE: same artifact name
          path: my-file.txt
+         overwrite: true
```

Note that this will create an _entirely_ new Artifact, with a different ID from the previous.

## Merging multiple artifacts

In `v3`, multiple uploads from multiple jobs could be done to the same Artifact. This would result in a single archive, which could be useful for sending to upstream systems outside of Actions via API or UI downloads.

```yaml
jobs:
  upload:
    strategy:
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.runs-on }}
    steps:
      - name: Create a File
        run: echo "hello from ${{ matrix.runs-on }}" > file-${{ matrix.runs-on }}.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v3
        with:
          name: all-my-files # NOTE: same artifact name
          path: file-${{ matrix.runs-on }}.txt
```

The single `all-my-files` artifact would contain the following:

```
.
  ∟ file-ubuntu-latest.txt
  ∟ file-macos-latest.txt
  ∟ file-windows-latest.txt
```

To achieve the same in `v4` you can change it like so:

```diff
jobs:
  upload:
    strategy:
      matrix:
        runs-on: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.runs-on }}
    steps:
      - name: Create a File
        run: echo "hello from ${{ matrix.runs-on }}" > file-${{ matrix.runs-on }}.txt
      - name: Upload Artifact
-       uses: actions/upload-artifact@v3
+       uses: actions/upload-artifact@v4
        with:
-         name: all-my-files
+         name: my-artifact-${{ matrix.runs-on }}
          path: file-${{ matrix.runs-on }}.txt
+  merge:
+    runs-on: ubuntu-latest
+    needs: upload
+    steps:
+      - name: Merge Artifacts
+        uses: actions/upload-artifact/merge@v4
+        with:
+          name: all-my-files
+          pattern: my-artifact-*
```

Note that this will download all artifacts to a temporary directory and reupload them as a single artifact. For more information on inputs and other use cases for `actions/upload-artifact/merge@v4`, see [the action documentation](../../../README.md).

## Hidden Files

By default, hidden files are ignored by this action to avoid unintentionally uploading sensitive
information.

In versions of this action before v4.4.0, these hidden files were included by default.

If you need to upload hidden files, you can use the `include-hidden-files` input.

```yaml
jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Create a Hidden File
        run: echo "hello from a hidden file" > .hidden-file.txt
      - name: Upload Artifact
        uses: actions/upload-artifact@v3
        with:
          path: .hidden-file.txt
```


```diff
jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Create a Hidden File
        run: echo "hello from a hidden file" > .hidden-file.txt
      - name: Upload Artifact
-       uses: actions/upload-artifact@v3
+       uses: actions/upload-artifact@v4
        with:
          path: .hidden-file.txt
+         include-hidden-files: true
```
```

## File: `merge/README.md`
```markdown
# `@actions/upload-artifact/merge`

Merge multiple [Actions Artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts) in Workflow Runs. Internally powered by [@actions/artifact](https://github.com/actions/toolkit/tree/main/packages/artifact) package.

- [`@actions/upload-artifact/merge`](#actionsupload-artifactmerge)
  - [Usage](#usage)
    - [Inputs](#inputs)
    - [Outputs](#outputs)
  - [Examples](#examples)
    - [Combining all artifacts in a workflow run](#combining-all-artifacts-in-a-workflow-run)
    - [Prefix directories in merged artifact](#prefix-directories-in-merged-artifact)
    - [Deleting artifacts after merge](#deleting-artifacts-after-merge)
    - [Retention and Compression Level](#retention-and-compression-level)

## Usage

> [!IMPORTANT]
> upload-artifact/merge@v4+ is not currently supported on GHES.

Note: this actions can only merge artifacts created with actions/upload-artifact@v4+

This sub-action is a helper to merge multiple artifacts after they are created. To do so, it will download multiple artifacts to a temporary directory and reupload them as a single artifact.

For most cases, this may not be the most efficient solution. See [the migration docs](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/hook_development/references/migration.md#multiple-uploads-to-the-same-named-artifact) on how to download multiple artifacts to the same directory on a runner. This action should only be necessary for cases where multiple artifacts will need to be downloaded outside the runner environment, like downloads via the UI or REST API.

### Inputs

```yaml
- uses: actions/upload-artifact/merge@v4
  with:
    # The name of the artifact that the artifacts will be merged into
    # Optional. Default is 'merged-artifacts'
    name:

    # A glob pattern matching the artifacts that should be merged.
    # Optional. Default is '*'
    pattern:

    # If true, the artifacts will be merged into separate directories.
    # If false, the artifacts will be merged into the root of the destination.
    # Optional. Default is 'false'
    separate-directories:

    # If true, the artifacts that were merged will be deleted.
    # If false, the artifacts will still exist.
    # Optional. Default is 'false'
    delete-merged:

    # Duration after which artifact will expire in days. 0 means using default retention.
    # Minimum 1 day.
    # Maximum 90 days unless changed from the repository settings page.
    # Optional. Defaults to repository settings.
    retention-days:

    # The level of compression for Zlib to be applied to the artifact archive.
    # The value can range from 0 to 9.
    # For large files that are not easily compressed, a value of 0 is recommended for significantly faster uploads.
    # Optional. Default is '6'
    compression-level:
```

### Outputs

| Name | Description | Example |
| - | - | - |
| `artifact-id` | GitHub ID of an Artifact, can be used by the REST API | `1234` |
| `artifact-url` | URL to download an Artifact. Can be used in many scenarios such as linking to artifacts in issues or pull requests. Users must be logged-in in order for this URL to work. This URL is valid as long as the artifact has not expired or the artifact, run or repository have not been deleted | `https://github.com/example-org/example-repo/actions/runs/1/artifacts/1234` |
| `artifact-digest` | SHA-256 digest of an Artifact | 0fde654d4c6e659b45783a725dc92f1bfb0baa6c2de64b34e814dc206ff4aaaf |

## Examples

For each of these examples, assume we have a prior job matrix that generates three artifacts: `my-artifact-a`, `my-artifact-b` and `my-artifact-c`.

e.g.

```yaml
jobs:
  upload:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        foo: [a, b, c]

    steps:
      - name: Run a one-line script
        run: echo "hello from job ${{ matrix.foo }}" > file-${{ matrix.foo }}.txt
      - name: Upload
        uses: actions/upload-artifact@v4
        with:
          name: my-artifact-${{ matrix.foo }}
          path: file-${{ matrix.foo }}.txt
```

Each of the following examples will use the `needs: upload` as a prerequesite before any merging operations.

### Combining all artifacts in a workflow run

By default (with no inputs), calling this action will take all the artifacts in the workflow run and combined them into a single artifact called `merged-artifacts`:

```yaml
jobs:
  # ... <upload job> ...
  merge:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Merge Artifacts
        uses: actions/upload-artifact/merge@v4
```

This will result in an artifact called `merged-artifacts` with the following content:

```
.
  ∟ file-a.txt
  ∟ file-b.txt
  ∟ file-c.txt
```

To change the name of the artifact and filter on what artifacts are added, you can use the `name` and `pattern` inputs:

```yaml
jobs:
  # ... <upload job> ...
  merge:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Merge Artifacts
        uses: actions/upload-artifact/merge@v4
        with:
          name: my-amazing-merged-artifact
          pattern: my-artifact-*
```

### Prefix directories in merged artifact

To prevent overwriting files in artifacts that may have the same name, you can use the `separate-directories` to prefix the extracted files with directories (named after the original artifact):

```yaml
jobs:
  # ... <upload job> ...
  merge:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Merge Artifacts
        uses: actions/upload-artifact/merge@v4
        with:
          separate-directories: true
```

This will result in the following artifact structure:

```
.
  ∟ my-artifact-a
    ∟ file-a.txt
  ∟ my-artifact-b
    ∟ file-b.txt
  ∟ my-artifact-c
    ∟ file-c.txt
```

### Deleting artifacts after merge

After merge, the old artifacts may no longer be required. To automatically delete them after they are merged into a new artifact, you can use `delete-merged` like so:

```yaml
jobs:
  # ... <upload job> ...
  merge:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Merge Artifacts
        uses: actions/upload-artifact/merge@v4
        with:
          delete-merged: true
```

After this runs, the matching artifact (`my-artifact-a`, `my-artifact-b` and `my-artifact-c`) will be merged.

### Retention and Compression Level

Similar to actions/upload-artifact, both [`retention-days`](../../../README.md#retention-period) and [`compression-level`](../../../README.md#altering-compressions-level-speed-v-size) are supported:

```yaml
jobs:
  # ... <upload job> ...
  merge:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Merge Artifacts
        uses: actions/upload-artifact/merge@v4
        with:
          retention-days: 1
          compression-level: 9
```
```

## File: `merge/action.yml`
```yaml
name: 'Merge Build Artifacts'
description: 'Merge one or more build Artifacts'
author: 'GitHub'
inputs:
  name:
    description: 'The name of the artifact that the artifacts will be merged into.'
    required: true
    default: 'merged-artifacts'
  pattern:
    description: 'A glob pattern matching the artifact names that should be merged.'
    default: '*'
  separate-directories:
    description: 'When multiple artifacts are matched, this changes the behavior of how they are merged in the archive.
      If true, the matched artifacts will be extracted into individual named directories within the specified path.
      If false, the matched artifacts will combined in the same directory.'
    default: 'false'
  retention-days:
    description: >
      Duration after which artifact will expire in days. 0 means using default retention.

      Minimum 1 day.
      Maximum 90 days unless changed from the repository settings page.
  compression-level:
    description: >
      The level of compression for Zlib to be applied to the artifact archive.
      The value can range from 0 to 9:
      - 0: No compression
      - 1: Best speed
      - 6: Default compression (same as GNU Gzip)
      - 9: Best compression
      Higher levels will result in better compression, but will take longer to complete.
      For large files that are not easily compressed, a value of 0 is recommended for significantly faster uploads.
    default: '6'
  delete-merged:
    description: >
      If true, the artifacts that were merged will be deleted.
      If false, the artifacts will still exist.
    default: 'false'
  include-hidden-files:
    description: >
      If true, hidden files will be included in the merged artifact.
      If false, hidden files will be excluded from the merged artifact.
    default: 'false'

outputs:
  artifact-id:
    description: >
      A unique identifier for the artifact that was just uploaded. Empty if the artifact upload failed.

      This ID can be used as input to other APIs to download, delete or get more information about an artifact: https://docs.github.com/en/rest/actions/artifacts
  artifact-url:
    description: >
      A download URL for the artifact that was just uploaded. Empty if the artifact upload failed.

      This download URL only works for requests Authenticated with GitHub. Anonymous downloads will be prompted to first login. 
      If an anonymous download URL is needed than a short time restricted URL can be generated using the download artifact API: https://docs.github.com/en/rest/actions/artifacts#download-an-artifact    

      This URL will be valid for as long as the artifact exists and the workflow run and repository exists. Once an artifact has expired this URL will no longer work.
      Common uses cases for such a download URL can be adding download links to artifacts in descriptions or comments on pull requests or issues.
  artifact-digest:
    description: >
      SHA-256 digest for the artifact that was just uploaded. Empty if the artifact upload failed.
runs:
  using: 'node24'
  main: '../dist/merge/index.js'
```

## File: `src/merge/constants.ts`
```typescript
/* eslint-disable no-unused-vars */
export enum Inputs {
  Name = 'name',
  Pattern = 'pattern',
  SeparateDirectories = 'separate-directories',
  RetentionDays = 'retention-days',
  CompressionLevel = 'compression-level',
  DeleteMerged = 'delete-merged',
  IncludeHiddenFiles = 'include-hidden-files'
}
```

## File: `src/merge/index.ts`
```typescript
import * as core from '@actions/core'
import {run} from './merge-artifacts.js'

run().catch(error => {
  core.setFailed((error as Error).message)
})
```

## File: `src/merge/input-helper.ts`
```typescript
import * as core from '@actions/core'
import {Inputs} from './constants.js'
import {MergeInputs} from './merge-inputs.js'

/**
 * Helper to get all the inputs for the action
 */
export function getInputs(): MergeInputs {
  const name = core.getInput(Inputs.Name, {required: true})
  const pattern = core.getInput(Inputs.Pattern, {required: true})
  const separateDirectories = core.getBooleanInput(Inputs.SeparateDirectories)
  const deleteMerged = core.getBooleanInput(Inputs.DeleteMerged)
  const includeHiddenFiles = core.getBooleanInput(Inputs.IncludeHiddenFiles)

  const inputs = {
    name,
    pattern,
    separateDirectories,
    deleteMerged,
    retentionDays: 0,
    compressionLevel: 6,
    includeHiddenFiles
  } as MergeInputs

  const retentionDaysStr = core.getInput(Inputs.RetentionDays)
  if (retentionDaysStr) {
    inputs.retentionDays = parseInt(retentionDaysStr)
    if (isNaN(inputs.retentionDays)) {
      core.setFailed('Invalid retention-days')
    }
  }

  const compressionLevelStr = core.getInput(Inputs.CompressionLevel)
  if (compressionLevelStr) {
    inputs.compressionLevel = parseInt(compressionLevelStr)
    if (isNaN(inputs.compressionLevel)) {
      core.setFailed('Invalid compression-level')
    }

    if (inputs.compressionLevel < 0 || inputs.compressionLevel > 9) {
      core.setFailed('Invalid compression-level. Valid values are 0-9')
    }
  }

  return inputs
}
```

## File: `src/merge/merge-artifacts.ts`
```typescript
import * as path from 'path'
import {mkdtemp, rm} from 'fs/promises'
import * as core from '@actions/core'
import {Minimatch} from 'minimatch'
import artifactClient, {UploadArtifactOptions} from '@actions/artifact'
import {getInputs} from './input-helper.js'
import {uploadArtifact} from '../shared/upload-artifact.js'
import {findFilesToUpload} from '../shared/search.js'

const PARALLEL_DOWNLOADS = 5

export const chunk = <T>(arr: T[], n: number): T[][] =>
  arr.reduce((acc, cur, i) => {
    const index = Math.floor(i / n)
    acc[index] = [...(acc[index] || []), cur]
    return acc
  }, [] as T[][])

export async function run(): Promise<void> {
  const inputs = getInputs()
  const tmpDir = await mkdtemp('merge-artifact')

  const listArtifactResponse = await artifactClient.listArtifacts({
    latest: true
  })
  const matcher = new Minimatch(inputs.pattern)
  const artifacts = listArtifactResponse.artifacts.filter(artifact =>
    matcher.match(artifact.name)
  )
  core.debug(
    `Filtered from ${listArtifactResponse.artifacts.length} to ${artifacts.length} artifacts`
  )

  if (artifacts.length === 0) {
    throw new Error(`No artifacts found matching pattern '${inputs.pattern}'`)
  }

  core.info(`Preparing to download the following artifacts:`)
  artifacts.forEach(artifact => {
    core.info(`- ${artifact.name} (ID: ${artifact.id}, Size: ${artifact.size})`)
  })

  const downloadPromises = artifacts.map(artifact =>
    artifactClient.downloadArtifact(artifact.id, {
      path: inputs.separateDirectories
        ? path.join(tmpDir, artifact.name)
        : tmpDir
    })
  )

  const chunkedPromises = chunk(downloadPromises, PARALLEL_DOWNLOADS)
  for (const chunk of chunkedPromises) {
    await Promise.all(chunk)
  }

  const options: UploadArtifactOptions = {}
  if (inputs.retentionDays) {
    options.retentionDays = inputs.retentionDays
  }

  if (typeof inputs.compressionLevel !== 'undefined') {
    options.compressionLevel = inputs.compressionLevel
  }

  const searchResult = await findFilesToUpload(
    tmpDir,
    inputs.includeHiddenFiles
  )

  await uploadArtifact(
    inputs.name,
    searchResult.filesToUpload,
    searchResult.rootDirectory,
    options
  )

  core.info(
    `The ${artifacts.length} artifact(s) have been successfully merged!`
  )

  if (inputs.deleteMerged) {
    const deletePromises = artifacts.map(artifact =>
      artifactClient.deleteArtifact(artifact.name)
    )
    await Promise.all(deletePromises)
    core.info(`The ${artifacts.length} artifact(s) have been deleted`)
  }

  try {
    await rm(tmpDir, {recursive: true})
  } catch (error) {
    core.warning(
      `Unable to remove temporary directory: ${(error as Error).message}`
    )
  }
}
```

## File: `src/merge/merge-inputs.ts`
```typescript
export interface MergeInputs {
  /**
   * The name of the artifact that the artifacts will be merged into
   */
  name: string

  /**
   * A glob pattern matching the artifacts that should be merged.
   */
  pattern: string

  /**
   * Duration after which artifact will expire in days
   */
  retentionDays: number

  /**
   * The level of compression for Zlib to be applied to the artifact archive.
   */
  compressionLevel?: number

  /**
   * If true, the artifacts that were merged will be deleted.
   * If false, the artifacts will still exist.
   */
  deleteMerged: boolean

  /**
   * If true, the artifacts will be merged into separate directories.
   * If false, the artifacts will be merged into the root of the destination.
   */
  separateDirectories: boolean

  /**
   * Whether or not to include hidden files in the artifact
   */
  includeHiddenFiles: boolean
}
```

## File: `src/shared/search.ts`
```typescript
import * as glob from '@actions/glob'
import * as path from 'path'
import {debug, info} from '@actions/core'
import {stat} from 'fs'
import {dirname} from 'path'
import {promisify} from 'util'
const stats = promisify(stat)

export interface SearchResult {
  filesToUpload: string[]
  rootDirectory: string
}

function getDefaultGlobOptions(includeHiddenFiles: boolean): glob.GlobOptions {
  return {
    followSymbolicLinks: true,
    implicitDescendants: true,
    omitBrokenSymbolicLinks: true,
    excludeHiddenFiles: !includeHiddenFiles
  }
}

/**
 * If multiple paths are specific, the least common ancestor (LCA) of the search paths is used as
 * the delimiter to control the directory structure for the artifact. This function returns the LCA
 * when given an array of search paths
 *
 * Example 1: The patterns `/foo/` and `/bar/` returns `/`
 *
 * Example 2: The patterns `~/foo/bar/*` and `~/foo/voo/two/*` and `~/foo/mo/` returns `~/foo`
 */
function getMultiPathLCA(searchPaths: string[]): string {
  if (searchPaths.length < 2) {
    throw new Error('At least two search paths must be provided')
  }

  const commonPaths = new Array<string>()
  const splitPaths = new Array<string[]>()
  let smallestPathLength = Number.MAX_SAFE_INTEGER

  // split each of the search paths using the platform specific separator
  for (const searchPath of searchPaths) {
    debug(`Using search path ${searchPath}`)

    const splitSearchPath = path.normalize(searchPath).split(path.sep)

    // keep track of the smallest path length so that we don't accidentally later go out of bounds
    smallestPathLength = Math.min(smallestPathLength, splitSearchPath.length)
    splitPaths.push(splitSearchPath)
  }

  // on Unix-like file systems, the file separator exists at the beginning of the file path, make sure to preserve it
  if (searchPaths[0].startsWith(path.sep)) {
    commonPaths.push(path.sep)
  }

  let splitIndex = 0
  // function to check if the paths are the same at a specific index
  function isPathTheSame(): boolean {
    const compare = splitPaths[0][splitIndex]
    for (let i = 1; i < splitPaths.length; i++) {
      if (compare !== splitPaths[i][splitIndex]) {
        // a non-common index has been reached
        return false
      }
    }
    return true
  }

  // loop over all the search paths until there is a non-common ancestor or we go out of bounds
  while (splitIndex < smallestPathLength) {
    if (!isPathTheSame()) {
      break
    }
    // if all are the same, add to the end result & increment the index
    commonPaths.push(splitPaths[0][splitIndex])
    splitIndex++
  }
  return path.join(...commonPaths)
}

export async function findFilesToUpload(
  searchPath: string,
  includeHiddenFiles?: boolean
): Promise<SearchResult> {
  const searchResults: string[] = []
  const globber = await glob.create(
    searchPath,
    getDefaultGlobOptions(includeHiddenFiles || false)
  )
  const rawSearchResults: string[] = await globber.glob()

  /*
    Files are saved with case insensitivity. Uploading both a.txt and A.txt will files to be overwritten
    Detect any files that could be overwritten for user awareness
  */
  const set = new Set<string>()

  /*
    Directories will be rejected if attempted to be uploaded. This includes just empty
    directories so filter any directories out from the raw search results
  */
  for (const searchResult of rawSearchResults) {
    const fileStats = await stats(searchResult)
    // isDirectory() returns false for symlinks if using fs.lstat(), make sure to use fs.stat() instead
    if (!fileStats.isDirectory()) {
      debug(`File:${searchResult} was found using the provided searchPath`)
      searchResults.push(searchResult)

      // detect any files that would be overwritten because of case insensitivity
      if (set.has(searchResult.toLowerCase())) {
        info(
          `Uploads are case insensitive: ${searchResult} was detected that it will be overwritten by another file with the same path`
        )
      } else {
        set.add(searchResult.toLowerCase())
      }
    } else {
      debug(
        `Removing ${searchResult} from rawSearchResults because it is a directory`
      )
    }
  }

  // Calculate the root directory for the artifact using the search paths that were utilized
  const searchPaths: string[] = globber.getSearchPaths()

  if (searchPaths.length > 1) {
    info(
      `Multiple search paths detected. Calculating the least common ancestor of all paths`
    )
    const lcaSearchPath = getMultiPathLCA(searchPaths)
    info(
      `The least common ancestor is ${lcaSearchPath}. This will be the root directory of the artifact`
    )

    return {
      filesToUpload: searchResults,
      rootDirectory: lcaSearchPath
    }
  }

  /*
    Special case for a single file artifact that is uploaded without a directory or wildcard pattern. The directory structure is
    not preserved and the root directory will be the single files parent directory
  */
  if (searchResults.length === 1 && searchPaths[0] === searchResults[0]) {
    return {
      filesToUpload: searchResults,
      rootDirectory: dirname(searchResults[0])
    }
  }

  return {
    filesToUpload: searchResults,
    rootDirectory: searchPaths[0]
  }
}
```

## File: `src/shared/upload-artifact.ts`
```typescript
import * as core from '@actions/core'
import * as github from '@actions/github'
import artifact, {UploadArtifactOptions} from '@actions/artifact'

export async function uploadArtifact(
  artifactName: string,
  filesToUpload: string[],
  rootDirectory: string,
  options: UploadArtifactOptions
) {
  const uploadResponse = await artifact.uploadArtifact(
    artifactName,
    filesToUpload,
    rootDirectory,
    options
  )

  core.info(
    `Artifact ${artifactName} has been successfully uploaded! Final size is ${uploadResponse.size} bytes. Artifact ID is ${uploadResponse.id}`
  )
  core.setOutput('artifact-id', uploadResponse.id)
  core.setOutput('artifact-digest', uploadResponse.digest)

  const repository = github.context.repo
  const artifactURL = `${github.context.serverUrl}/${repository.owner}/${repository.repo}/actions/runs/${github.context.runId}/artifacts/${uploadResponse.id}`

  core.info(`Artifact download URL: ${artifactURL}`)
  core.setOutput('artifact-url', artifactURL)
}
```

## File: `src/upload/constants.ts`
```typescript
/* eslint-disable no-unused-vars */
export enum Inputs {
  Name = 'name',
  Path = 'path',
  IfNoFilesFound = 'if-no-files-found',
  RetentionDays = 'retention-days',
  CompressionLevel = 'compression-level',
  Overwrite = 'overwrite',
  IncludeHiddenFiles = 'include-hidden-files',
  Archive = 'archive'
}

export enum NoFileOptions {
  /**
   * Default. Output a warning but do not fail the action
   */
  warn = 'warn',

  /**
   * Fail the action with an error message
   */
  error = 'error',

  /**
   * Do not output any warnings or errors, the action does not fail
   */
  ignore = 'ignore'
}
```

## File: `src/upload/index.ts`
```typescript
import * as core from '@actions/core'
import {run} from './upload-artifact.js'

run().catch(error => {
  core.setFailed((error as Error).message)
})
```

## File: `src/upload/input-helper.ts`
```typescript
import * as core from '@actions/core'
import {Inputs, NoFileOptions} from './constants.js'
import {UploadInputs} from './upload-inputs.js'

/**
 * Helper to get all the inputs for the action
 */
export function getInputs(): UploadInputs {
  const name = core.getInput(Inputs.Name)
  const path = core.getInput(Inputs.Path, {required: true})
  const overwrite = core.getBooleanInput(Inputs.Overwrite)
  const includeHiddenFiles = core.getBooleanInput(Inputs.IncludeHiddenFiles)
  const archive = core.getBooleanInput(Inputs.Archive)

  const ifNoFilesFound = core.getInput(Inputs.IfNoFilesFound)
  const noFileBehavior: NoFileOptions = NoFileOptions[ifNoFilesFound]

  if (!noFileBehavior) {
    core.setFailed(
      `Unrecognized ${
        Inputs.IfNoFilesFound
      } input. Provided: ${ifNoFilesFound}. Available options: ${Object.keys(
        NoFileOptions
      )}`
    )
  }

  const inputs = {
    artifactName: name,
    searchPath: path,
    ifNoFilesFound: noFileBehavior,
    overwrite: overwrite,
    includeHiddenFiles: includeHiddenFiles,
    archive: archive
  } as UploadInputs

  const retentionDaysStr = core.getInput(Inputs.RetentionDays)
  if (retentionDaysStr) {
    inputs.retentionDays = parseInt(retentionDaysStr)
    if (isNaN(inputs.retentionDays)) {
      core.setFailed('Invalid retention-days')
    }
  }

  const compressionLevelStr = core.getInput(Inputs.CompressionLevel)
  if (compressionLevelStr) {
    inputs.compressionLevel = parseInt(compressionLevelStr)
    if (isNaN(inputs.compressionLevel)) {
      core.setFailed('Invalid compression-level')
    }

    if (inputs.compressionLevel < 0 || inputs.compressionLevel > 9) {
      core.setFailed('Invalid compression-level. Valid values are 0-9')
    }
  }

  return inputs
}
```

## File: `src/upload/upload-artifact.ts`
```typescript
import * as core from '@actions/core'
import artifact, {
  UploadArtifactOptions,
  ArtifactNotFoundError
} from '@actions/artifact'
import {findFilesToUpload} from '../shared/search.js'
import {getInputs} from './input-helper.js'
import {NoFileOptions} from './constants.js'
import {uploadArtifact} from '../shared/upload-artifact.js'

async function deleteArtifactIfExists(artifactName: string): Promise<void> {
  try {
    await artifact.deleteArtifact(artifactName)
  } catch (error) {
    if (error instanceof ArtifactNotFoundError) {
      core.debug(`Skipping deletion of '${artifactName}', it does not exist`)
      return
    }

    // Best effort, we don't want to fail the action if this fails
    core.debug(`Unable to delete artifact: ${(error as Error).message}`)
  }
}

export async function run(): Promise<void> {
  const inputs = getInputs()
  const searchResult = await findFilesToUpload(
    inputs.searchPath,
    inputs.includeHiddenFiles
  )
  if (searchResult.filesToUpload.length === 0) {
    // No files were found, different use cases warrant different types of behavior if nothing is found
    switch (inputs.ifNoFilesFound) {
      case NoFileOptions.warn: {
        core.warning(
          `No files were found with the provided path: ${inputs.searchPath}. No artifacts will be uploaded.`
        )
        break
      }
      case NoFileOptions.error: {
        core.setFailed(
          `No files were found with the provided path: ${inputs.searchPath}. No artifacts will be uploaded.`
        )
        break
      }
      case NoFileOptions.ignore: {
        core.info(
          `No files were found with the provided path: ${inputs.searchPath}. No artifacts will be uploaded.`
        )
        break
      }
    }
  } else {
    const s = searchResult.filesToUpload.length === 1 ? '' : 's'
    core.info(
      `With the provided path, there will be ${searchResult.filesToUpload.length} file${s} uploaded`
    )
    core.debug(`Root artifact directory is ${searchResult.rootDirectory}`)

    // Validate that only a single file is uploaded when archive is false
    if (!inputs.archive && searchResult.filesToUpload.length > 1) {
      core.setFailed(
        `When 'archive' is set to false, only a single file can be uploaded. Found ${searchResult.filesToUpload.length} files to upload.`
      )
      return
    }

    if (inputs.overwrite) {
      await deleteArtifactIfExists(inputs.artifactName)
    }

    const options: UploadArtifactOptions = {}
    if (inputs.retentionDays) {
      options.retentionDays = inputs.retentionDays
    }

    if (typeof inputs.compressionLevel !== 'undefined') {
      options.compressionLevel = inputs.compressionLevel
    }

    if (!inputs.archive) {
      options.skipArchive = true
    }

    await uploadArtifact(
      inputs.artifactName,
      searchResult.filesToUpload,
      searchResult.rootDirectory,
      options
    )
  }
}
```

## File: `src/upload/upload-inputs.ts`
```typescript
import {NoFileOptions} from './constants.js'

export interface UploadInputs {
  /**
   * The name of the artifact that will be uploaded
   */
  artifactName: string

  /**
   * The search path used to describe what to upload as part of the artifact
   */
  searchPath: string

  /**
   * The desired behavior if no files are found with the provided search path
   */
  ifNoFilesFound: NoFileOptions

  /**
   * Duration after which artifact will expire in days
   */
  retentionDays: number

  /**
   * The level of compression for Zlib to be applied to the artifact archive.
   */
  compressionLevel?: number

  /**
   * Whether or not to replace an existing artifact with the same name
   */
  overwrite: boolean

  /**
   * Whether or not to include hidden files in the artifact
   */
  includeHiddenFiles: boolean

  /**
   * Whether or not to archive (zip) the artifact before uploading.
   * When false, only a single file can be uploaded.
   */
  archive: boolean
}
```

