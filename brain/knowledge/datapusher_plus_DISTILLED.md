---
id: datapusher-plus
type: knowledge
owner: OA_Triage
---
# datapusher-plus
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[CKAN Service Provider]: https://github.com/ckan/ckan-service-provider
[Messytables]: https://github.com/okfn/messytables
[qsv]: https://github.com/dathere/qsv#qsv-ultra-fast-csv-data-wrangling-toolkit

# DataPusher+

> NOTE: v2 is a major revamp. Documentation is currently WIP.

DataPusher+ is a fork of [Datapusher](https://github.com/ckan/datapusher) that combines the speed and robustness of [ckanext-xloader](https://github.com/ckan/ckanext-xloader) with the data type guessing of Datapusher - [super-powered with the ability to infer, calculate & suggest metadata using Jinja2 formulas defined in the scheming configuration file](docs/dataset_schema.yaml).


https://github.com/user-attachments/assets/b2fc2c3a-d244-4d11-9cf3-8270f0e99162


The Formulas have access to not just the `package` and `resource` fields (in the same namespaces), it also has access to the following information in these additional namespaces that can be used in Jinja2 expressions:
* `dpps` - with the "s" for stats.<br/>Each field will have an extensive list of summary statistics (by default: 
type, is_ascii, sum, min/max, range, sort_order, sortiness, min_length, max_length, sum_length, avg_length, stddev_length, variance_length, cv_length, mean, sem, geometric_mean, harmonic_mean, stddev, variance, cv, nullcount, max_precision, sparsity, cardinality, uniqueness_ratio.) Check [here](https://github.com/dathere/qsv/wiki/Supplemental#stats-command-output-explanation) for all other available statistics.
* `dppf` - with the "f" for frequency table.<br/>Each field will have its frequency table available sorted in descending order the top N (configurable, default 10) values, with a corresponding count & percentage. "Other (COUNT)" will be used as a "basket" for other values with COUNT set to the count of other values beyond the top N. ID fields will be indicated by "<ALL_UNIQUE>" in the table.
* `dpp` - additional inferred/calculated metadata.<br/>
  * `ORIGINAL_FILE_SIZE` (bytes)
  * `PREVIEW_FILE_SIZE` (bytes)
  * `RECORD_COUNT` (int)
  * `PREVIEW_RECORD_COUNT` (int)
  * `IS_SORTED` (bool)
  * `DEDUPED` (bool)
  * `DUPE_COUNT` (int: -1 if there are no dupes)
  * Date/DateTime metadata<br/>
    DP+ can infer date/datetime columns - supporting 19 different formats. As it is a relatively expensive operation, it will only do so for candidate columns with names that fit a configurable pattern.
      * `DATE_FIELDS` - a list of inferred date columns
      * `NO_DATE_FIELDS` (bool)
      * `DATETIME_FIELDS` - a list of inferred datetime columns
      * `NO_DATETIME_FIELDS` (bool)
  * Latitude/Longitude metadata<br/>
    DP+ can infer the latitude and longitude columns based on the column's characteristics. A column is inferred to be a latitude/longitude column if:
      * its in a comma-separated priority-order list of lat/long name patterns
      * for latitude, if its of type "Float" with a range of -90.0 to 90.0, and
      * for longitude, if its a "Float" with a range of -180.0 to 180.0.
    * `LAT_FIELD` and `LON_FIELD` - the inferred lat/long columns
    * `NO_LAT_LONG_FIELDS` (bool)

Beyond the extensive list of built-in Jinja2 [filters](https://jinja.palletsprojects.com/en/stable/templates/#list-of-builtin-filters)/[functions](https://jinja.palletsprojects.com/en/stable/templates/#list-of-global-functions), DP+ also supports an extensive list of additional [custom filters/functions](https://github.com/dathere/datapusher-plus/blob/607e7c5e5d75c5dc7ac55d684522c7972bc33d1d/ckanext/datapusher_plus/jinja2_helpers.py#L171). Several of these helper functions make it trivially easy to calculate [DCAT 3](https://doi-do.github.io/dcat-us/) recommended, optional properties that would ordinarily be too painstaking to manually compile (e.g `dcat-us:GeographicBoundingBox`, `dcat:temporalResolution`, `dcat:startDate`, `dcat:endDate`, etc. ).

There are two Formula types that are indicated by adding these keywords to the scheming yaml file:
 * `formula` - the formula will be evaluated at resource creation/update time and the result is assigned to the corresponding package/resource field immediately.
 * `suggest_formula` - the formula will be evaluated at resource creation/update time and the result is stored in the `dpp_suggestions` package field as a compound JSON object. `dpp_suggestions` contains all the suggestion for both package and resource fields. This field is parsed to show "Suggestions" during metadata entry for the associated package/resource field using the Suggestion UI (indicated by a function symbol next to the metadata field name).

 Formulas that fail to evaluate will return with the `#ERROR!:` (reminiscent of Excel's `#VALUE!` function error) prefix followed by a detailed Jinja2 error message.

In addition, Datapusher+ is no longer a webservice, but a full-fledged CKAN extension. It drops usage of the deprecated [CKAN Service Provider][], with the unmaintained [Messytables] replaced by the blazing-fast [qsv] data-wrangling engine.

[TxGIO](https://geographic.texas.gov/)/[TWDB](https://www.twdb.texas.gov/) provided the use cases that informed and supported the development
of Datapusher+, specifically, to support a [Resource-first upload workflow](docs/RESOURCE_FIRST_WORKFLOW.md#Resource-first-Upload-Workflow).

For a more detailed overview, see the [CKAN Monthly Live Jan 2023 presentation](https://docs.google.com/presentation/d/e/2PACX-1vT0BfmrrtaEINRGg4UI_m7B02_X6HlFr4yN_DXmgX9goVtgu2DNmZjl-SowL9ZA2ibQhDjScRRJh95q/pub?start=false&loop=false&delayms=3000).

It features:

* **"Bullet-proof", ultra-fast data type inferencing with qsv**

  Unlike [Messytables][] which scans only the the first few rows to guess the type of
  a column, [qsv][] scans the entire table so its data type inferences are guaranteed[^1].

  Despite this, qsv is still exponentially faster even if it scans the whole file, not
  only inferring data types, it also calculates [summary statistics](https://github.com/dathere/qsv/blob/b0fbd0e575e2e80f57f94ce916438edf9dc32859/src/cmd/stats.rs#L2-L18) as well. For example,
  [scanning a 2.7 million row, 124MB CSV file for types and stats took 0.16 seconds](https://github.com/dathere/qsv/blob/master/docs/whirlwind_tour.md#a-whirlwind-tour)[^2].

  It is very fast as qsv is written in [Rust](https://www.rust-lang.org/), is multithreaded,
  and uses all kinds of [performance techniques](https://github.com/dathere/qsv/blob/master/docs/PERFORMANCE.md#performance-tuning)
  especially designed for data-wrangling.

* **Exponentially faster loading speed**

  Similar to xloader, we use PostgreSQL COPY to directly pipe the data into the datastore,
  short-circuiting the additional processing/transformation/API calls used by Datapusher Plus.

  But unlike xloader, we load everything using the proper data types and not as text, so there's
  no need to reload the data again after adjusting the Data Dictionary, as you would with xloader.

* **Far more Storage Efficient AND Performant Datastore with easier to compose SQL queries**

  As we create the Datastore tables using the most efficient PostgreSQL data type for each column
  using qsv's guaranteed type inferences - the Datastore is not only more storage efficient, it is
  also far more more performant for loading AND querying.
  
  With its "smartint" data type (with qsv inferring the most efficient integer data type for the range of
  values in the column); comprehensive date format inferencing (supporting [19 date formats](https://github.com/jqnatividad/belt/tree/main/dateparser#accepted-date-formats), with each
  format having several variants & with configurable DMY/MDY preference parsing) & auto-formatting dates to
  RFC3339 format so they are stored as Postgres timestamps; cardinality-aware, configurable auto-indexing;
  automatic sanitization of column names to valid PostgreSQL column identifiers; auto PostgreSQL vacuuming &
  analysis of resources after loading; and more - DP+ enables the Datastore to tap into PostgreSQL's full power.

  Configurable auto-aliasing of resources also makes it easier to compose SQL queries, as you can
  use more intuitive resource aliases instead of cryptic resource IDs.

* **Production-ready Robustness**

  In production, the number one source of support issues is Datapusher - primarily, because of
  data quality issues and Datapusher's inability to correctly infer data types, gracefully handle
  errors[^3], and provide the Data Publisher actionable information to correct the data.

  Datapusher+'s design directly addresses all these issues.

* **More informative datastore loading messages**

  Datapusher+ messages are designed to be more verbose and actionable, so the data publisher's
  user experience is far better and makes it possible to have a resource-first upload workflow.

* **Extended preprocessing with qsv**

  qsv is leveraged by Datapusher+ to:

  * create "Smarter" Data Dictionaries, with:
    * guaranteed data type inferences
    * optional ability to automatically choose the best integer PostgreSQL data type ("smartint") based on the range of the numeric column ([PostgreSQL's int, bigint and numeric types](https://www.postgresql.org/docs/12/datatype-numeric.html)) for optimal storage/indexing efficiency and SQL query performance.
    * sanitized column names (guaranteeing valid PostgreSQL column identifiers) while preserving the original column name as a label, which is used to label columns in DataTables_view.
    * an optional "summary stats" resource as an extension of the Data Dictionary, with comprehensive summary statistics for each column - sum, min/max/range, min/max length, mean, stddev, variance, nullcount, sparsity, quartiles, IQR, lower/upper fences, skewness, median, mode/s, antimode/s & cardinality.
  * convert Excel & OpenOffice/LibreOffice Calc (ODS) files to CSV, with the ability to choose which sheet to use by default (e.g. 0 is the first sheet, -1 is the last sheet, -2 the second to last sheet, etc.)
  * convert SHP and GeoJSON files to CSV, with optional geometry simplification.
  * decompress ZIP archives and insert the manifest as a CSV file with detailed metadata about the files in the archive. For ZIP archives with only one recognized file format, it can also automatically decompress the file and push that instead of the ZIP manifest into the Datastore.
  * convert various date formats ([19 date formats are recognized](https://github.com/jqnatividad/belt/tree/main/dateparser#accepted-date-formats) with each format having several variants; ~80 date format permutations in total) to a standard [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format
  * enable random access of a CSV by creating a CSV index - which also enables parallel processing of different parts of a CSV simultaneously (a major reason type inferencing and stats calculation is so fast)
  * instantaneously count the number of rows with a CSV index
  * validate if an uploaded CSV conforms to the [RFC-4180](https://datatracker.ietf.org/doc/html/rfc4180) standard
  * normalizes and transcodes CSV/TSV dialects into a standard UTF-8 encoded RFC-4180 CSV format
  * optionally create a preview subset, with the ability to only download the first `n` preview rows of a file, and not the entire file (e.g. only download first 1,000 rows of 3 gb CSV file - especially good for harvesting/cataloging external sites where you only want to harvest the metadata and a small sample of each file).
  * optionally create a preview subset from the end of a file (e.g. last 1,000 rows, good for time-series/sensor data)
  * auto-index columns based on its cardinality/format (unique indices created for columns with all unique values, auto-index columns whose cardinality is below a given threshold; auto-index date columns)
  * check for duplicates, and optionally deduplicate rows
  * optionally screen for Personally Identifiable Information (PII), with an option to "quarantine" the PII-candidate rows in a separate resource, while still creating the screened resource.
  * optional ability to specify a custom PII screening regex set, instead of the [default PII screening regex set](https://github.com/dathere/datapusher-plus/blob/master/default-pii-regexes.txt).

  Even with all these pre-processing tasks, qsv typically takes less than 5 seconds to finish all its analysis tasks, even for a 100mb CSV file.

  Future versions of Datapusher+ will further leverage qsv's 80+ commands to do additional
  preprocessing, data-wrangling and validation. The Roadmap is available [here](https://github.com/dathere/datapusher-plus/issues/5).
  Ideas, suggestions and your feedback are most welcome!

[^1]: [Why use qsv instead of a "proper" python data analysis library like pandas?](https://github.com/dathere/datapusher-plus/discussions/15)
[^2]: It takes 0.16 seconds with an index to run `qsv stats` against the [qsv whirlwind tour sample file](https://raw.githubusercontent.com/wiki/dathere/qsv/files/wcp.zip) on a Ryzen 4800H (8 physical/16 logical cores) with 32 gb memory and a 1 TB SSD.
Without an index, it takes 1.3 seconds.
[^3]: Imagine you have a 1M row CSV, and the last row has an invalid value for a numeric column (e.g. "N/A" instead of a number).
      After spending hours pushing the data very slowly, legacy datapusher will abort on the last row and the ENTIRE job is invalid.
      Ok, that's bad, but what makes it worse is that the old table has been deleted already, and Datapusher doesn't tell you what
      caused the job to fail! YIKES!!!!

## DRUF: Dataset Resource Upload First Workflow

DataPusher+ supports an optional **DRUF (Dataset Resource Upload First)** workflow that allows users to upload data files before creating dataset metadata. This resource-first approach is particularly useful for:

- **Data-driven workflows**: Where the structure and content of the data informs the metadata
- **Exploratory data publishing**: When you want to examine the data before writing descriptions
- **Simplified workflows**: Reducing the cognitive load of filling out metadata forms upfront

### How DRUF Works

When DRUF is enabled, the dataset creation workflow is modified:

1. **"Add Dataset" buttons** redirect to a resource upload page instead of the metadata form
2. **Temporary datasets** are automatically created with placeholder metadata
3. **Resource upload happens first**, allowing DataPusher+ to analyze the data
4. **Metadata forms** are enhanced with data-driven suggestions based on the uploaded content
5. **Form redirects** guide users through a logical resource-first workflow

### Enabling DRUF

- To enable DRUF you need [`DRUF compatable ckan version`](https://github.com/ckan/ckan/tree/7778-iformredirect) 
- You need to have scheming extension enabled and use the example DRUF compatable schema included in the dp+ extension.

Add the following configuration to your CKAN config file (e.g., `/etc/ckan/default/ckan.ini`):


```ini
# Enable DRUF (Dataset Resource Upload First) workflow
ck
... [TRUNCATED]
```

### File: requirements.txt
```txt
semver==3.0.4
datasize==1.0.0
jinja2>=3.1.4
fiona==1.10.1
pandas==2.2.3
shapely==2.1.0
pyproj>=3.7.1

```

### File: setup.py
```py
# -*- coding: utf-8 -*-

from setuptools import setup
setup(
    message_extractors={
        "ckanext": [
            ("**.py", "python", None),
            ("**.js", "javascript", None),
            ("**/templates/**.html", "ckan", None),
        ],
    },
)

```

### File: tests\README.md
```md

## Technical Reference



### Time Measurements
- All `time` values in the worker_analysis.csv are measured in **seconds**

### Data Quality Scoring Algorithm
Base score: 100, with penalties applied:
- Invalid CSV: -30 points
- Unsorted data: -10 points
- Unsafe headers: -5 points per unsafe header (max -25)
- Failed normalization: -20 points
- Failed analysis: -25 points
- UTF-8 encoding: +5 points
- `>1000 records: +5 points`

### Performance Anomaly Detection
- Uses statistical analysis (mean + 2 standard deviations)
- Identifies jobs with processing times significantly above normal
- Requires minimum 3 successful jobs for analysis


### CSV Output Schema

#### Primary Fields
| Column | Type | Description |
|--------|------|-------------|
| `timestamp` | String | Job start timestamp (YYYY-MM-DD HH:MM:SS) |
| `job_id` | String | UUID of the processing job |
| `file_name` | String | Name of the processed file |
| `status` | String | SUCCESS, ERROR, or INCOMPLETE |
| `qsv_version` | String | Version of QSV tool used |
| `file_format` | String | Detected file format (CSV, XLSX, etc.) |
| `encoding` | String | File character encoding |
| `normalized` | String | "Successful" or "Failed" |
| `valid_csv` | String | "TRUE" or "FALSE" |
| `sorted` | String | "TRUE", "FALSE", or "UNKNOWN" |
| `db_safe_headers` | String | Header safety status |
| `analysis` | String | "Successful" or "Failed" |
| `records` | Integer | Number of records detected |

#### Timing Fields (all in seconds)
| Column | Type | Description |
|--------|------|-------------|
| `total_time` | Float | Total processing time |
| `download_time` | Float | File download time |
| `analysis_time` | Float | Analysis phase time |
| `copying_time` | Float | Database copy time |
| `indexing_time` | Float | Index creation time |
| `formulae_time` | Float | Formula processing time |
| `metadata_time` | Float | Metadata update time |

```

### File: CHANGELOG.md
```md
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## What's Changed
* Update README with some fixes by @tino097 in https://github.com/dathere/datapusher-plus/pull/178
* Druf apr2025 by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/180
* Refactor upload log level by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/181
* feat: zip file support by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/182
* feat: shapefile support by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/183
* Refactor jobs py by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/184
* feat: make frequency limit configurable; move stats/freq copying to datastore from jobs.py to qsv_utils.py by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/185
* Lat lon columns inferencing for use in Formulas by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/188
* Configurable Date/Datetime inferencing and dataset stats by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/190
* refactor: move pii-screening to a separate module by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/191
* chore: add WIP geojson update by @rzmk in https://github.com/dathere/datapusher-plus/pull/186
* "smart" formula spatial functions by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/192
* Jobs cleanup by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/193
* Fix datastore upload log timestamps by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/194
* DCAT 3 formula helpers by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/195
* fix: tmp input was being wrongfully assigned  by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/197
* refactored SQL-enabled formulas by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/199
* auto unzip one file setting by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/200
* add LRU caches to potentially expensive Formula methods by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/201
* feat: add `dpp_suggestions.STATUS` to track formulae processing progress by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/202
* refactor dpp_suggestions.STATUS to sync with Suggestions UI by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/203
* Refactor: remove stats & freq  table save to datastore by @jqnatividad in https://github.com/dathere/datapusher-plus/pull/204

## New Contributors
* @rzmk made their first contribution in https://github.com/dathere/datapusher-plus/pull/186

**Full Changelog**: https://github.com/dathere/datapusher-plus/compare/2.0.0...2.1.0

## [2.0.0] - 2025-04-25

## 🎉 Data Resource Upload First (DRUF) Workflow is finally here! 🎉 
A workflow that flips the old CKAN traditional data ingestion on its head.
 * Instead of filling out the metadata first and then uploading the data, users upload data resources first 
 * In a few seconds, even for very large datasets, analysis and validation is done while precompiling statistical metadata
 * This precompiled metadata are then used by Metadata Formulae defined in the [scheming](https://github.com/ckan/ckanext-scheming?tab=readme-ov-file#ckanext-scheming) yaml files to either precompute other metadata fields (on both package & resource levels) or to offer metadata suggestions
 * Metadata Formulae use the same powerful Jinja2 template engine that powers CKAN's templating system.
 * It comes with an extensible library of Jinja2 filters/functions that can be used in Metadata Formulae ala Excel.

The DRUF reinvents CKAN data ingestion - by automatically calculating/suggesting "**Automagical Metadata**" - high-quality, high-resolution metadata that reflects and describes what's **INSIDE** the dataset (e.g. summary stats; frequency table; spatial extent, date range, outliers, etc. calculated with Metadata Formulae) in addition to metadata about the dataset **FILE** (e.g. last updated, size of the file, owner, format, license, etc - what's normally found in traditional data catalogs).

Future improvements planned:
- **Expanded Data Dictionary**

- **"entry-time" Metadata Formulae**
In addition to the two formula types (`formula` to set a metadata field directly during creation/update; and `suggestion_formula` to suggest values using the Bootstap Popover UI), we'll add the ability to allow Data Publishers to enter formulas while they're entering metadata - fully embracing the Excel formula UI/UX aesthetic.
- **DCAT3-optimized reference profiles**
Following implementation guidance for both [DCAT-US v3](https://doi-do.github.io/dcat-us/) and [DCAT-AP 3](https://semiceu.github.io/DCAT-AP/releases/3.0.0/) scheming profiles with Metadata Formulae to compute recommended and optional properties that allow publishers to more fully take advantage of DCAT3 features and improvements - metadata properties that are often too laborious to manually compile.
- **Co-Curator AI**
"Automagical metadata" is the perfect context for AI engines - as it summarizes even very large datasets in just a few kilobytes. It allows the Co-Curator[^1] to suggest tags, descriptions, links to related data sets and chat about the corpus WHILE the Data Publisher is curating the data.
- **Inline Data Validation**
Optional ability to [infer an initial JSON Schema validation file](https://github.com/dathere/qsv?tab=readme-ov-file#schema_deeplink), and then [validate future updates](https://github.com/dathere/qsv?tab=readme-ov-file#validate_deeplink) to the dataset using it, leveraging the same blazing-fast qsv engine (validating up to 340,000 records/per second[^2]). 
- **Customizable DRUF Data ingestion pipeline**
Currently, there are [numerous configuration settings](https://github.com/dathere/datapusher-plus/blob/main/ckanext/datapusher_plus/config.py) to fine-tune the DRUF data-ingestion pipeline. However, the built-in default pipeline can only be customized to a limit without customizing the code. We will expose hooks that CKAN operators can take advantage of to tailor their DRUF pipelines to meet their requirements, while preserving the ability to access the precompiled statistical metadata that DP+ maintains.
- **Dynamic loading of Formula filters/functions**
So users can share custom Jinja2 filters and functions they developed for their Metadata Formulae.
- **Inline Data Enrichment**
Data can be optionally enriched while it's being ingested from other reference datasets within the same CKAN instance or external sources (e.g. enriched against high value curated sources like the Census; geocoding, etc.)
- **and more!**
It took a while for us to bake 2.0.0, but we look forward to picking up the pace and co-innovating with the CKAN ecosystem.


> NOTE: To fully experience the DRUF workflow, you'll need to use [scheming dataset form pages](https://excess.org/scheming-formpages/) and apply some CKAN core changes. A detailed installation procedure will be published on the Wiki shortly.

[^1]: Inspired by the [Curator in Ready Player One](https://hero.fandom.com/wiki/Curator)
[^2]: `validate_index benchmark` -  https://qsv.dathere.com/benchmarks
---

### Added
* Data Resource Upload First (DRUF) Workflow
  * Enhanced resource validation for DRUF workflow
  * Formulas for precomputing metadata/metadata sugggestions
  * Spatial file support - supports GeoJSON and Shapefiles
* Support for CKAN 2.9 compatibility in CLI operations
* Enhanced error handling and logging for resource uploads

### Changed
* Updated CLI interface to work with CKAN 2.9
* Refactored resource upload process to support DRUF workflow
* Improved error messages and user feedback
* Enhanced configuration handling

### Fixed
* Various bug fixes and improvements for CKAN 2.9 compatibility
* Resource upload process reliability improvements

### Contributors
* @tino097
* @minhajuddin2510
* @jqnatividad

**Full Changelog**: https://github.com/dathere/datapusher-plus/compare/1.0.4...2.0.0

## [1.0.4] - 2025-01-15

## [1.0.3] - 2024-10-30

### Changed
* Ensure we are always using the same token setting for datapusher
* Fix iconv
* Fix the api_token config variable and fix for default views creation
* Migration added

### Contributors
* @tino097
* @avdata99

## [1.0.2] - 2024-09-16

### Changed
* Update README file for DP+ as extension
* Fix MANIFEST.in
* Migrate cli commands
* Fix init db command
* Config part
* Database migrations
* Update readme
* Fix yaml extension in MANIFEST.in
* Fix datefmt compatability with qsv in dev-v1.0
* Remove obsolete assets

### Contributors
* @Zharktas
* @tino097
* @pdelboca

## [1.0.1] - 2024-05-22

### Changed
* Replace http requests with actions
* Fix calling package action for resource

### Contributors
* @tino097

## [1.0.0] - 2024-05-06

### Added
* Convert the datapusher to work as plugin
* Feature db models
* Add migration script
* Rewrite resource URL if it differs from the defined ckan_url

### Changed
* Code cleanup
* Rewrite resource url
* Sync with master

### Contributors
* @jhbruhn
* @tino097
* @TomeCirun

## [0.16.4] - 2024-01-23

### Changed
* sync read buffer with buffer size of copyexpert

### Contributors
* @jqnatividad

## [0.16.3] - 2024-01-23

### Changed
* make COPY_READBUFFER_SIZE a configurable parameter

### Contributors
* @jqnatividad

## [0.16.2] - 2024-01-23

### Changed
* explicitly create a large read buffer when reading CSV when COPYing files to the datastore

## [0.16.1] - 2024-01-15

### Fixed
* fix utf8 encoding check, replacing NamedTemporaryFile approach, with Temporary Directory approach

### Note
* Requires `uchardet` for the encoding check (`apt-get install uchardet`)

## [0.16.0] - 2024-01-11

### Added
* Update README.md
* Use a temporary directory to manage temporary files
* Utf8 conversion
* import syntax and ckanserviceprovider version
* upgrade container qsv to 0.118.0
* Fixed init of index_elapsed in case auto_index is off

### Changed
* caught a missing variable

### Contributors
* @bzar
* @categulario
* @hjhornbeck
* @EricSoroos
* @minhajuddin2510

## [0.15.0] - 2023-06-26

### Fixed
* removed DOWNLOAD_PREVIEW_ONLY as its unreliable with CSVs and corrupted Excel files
* removed SUMMARY_STATS_WITH_PREVIEW, which doesn't make sense without DOWNLOAD_PREVIEW_ONLY

## [0.14.1] - 2023-06-26

### Changed
* made a mistake publishing 0.14.0, neglecting to bump setup version
* add a note about using glibc-2.31 version of qsv if the Linux distro running it has an older version of GNU C library (e.g. Ubuntu 18.04 and Debian 11)

## [0.14.0] - 2023-06-26

### Added
* More robust file format detection, also now prompts the user to specify the file format if it cannot infer it from the server's content-type header or the file's extension

### Changed
* Minimum QuickSilver version is now 0.108.0, which features a more robust and faster `input` command DP+ uses for transcoding and normalization of CSVs

### Fixed
* Fixed file format detection
* Removed SNIFF_DELIMITER setting which was causing DP+ to periodically sniff non-comma delimiters even if the file was using comma delimiters

## [0.13.2] - 2023-06-22

### Fixed
* Added `tzdata` dependency and missing `logging` import

### Contributors
* @minhajuddin2510

## [0.13.1] - 2023-06-22

### Changed
* Reordered imports for clarity
* Minor Download improvements to make streaming download more robust as we're doing streaming downloads when using preview rows by doing request in a with clause
* added vscode setting to use black formatter

### Fixed
* added missing dependencies for `pytz` and `python-dateutil`. These new dependencies are required because of the fix in 0.13.0 that checked if a resource's metadata has been modified, allowing a DP+ job even if the file hash has not changed (e.g. when the Data Dictionary data types are changed and the user wants the resource file re-pushed to use the new data types)

## [0.13.0] - 2023-06-16

### Added
* Add unsafe headers configuration settings. This allows DP+ to use an alternate unsafe prefix when sanitizing column names
* Add SNIFF_DELIMITER setting. This allows DP+ to automatically infer the delimiter used by a CSV file if its not a comma
* The inferred Data Dictionary now also has a "Unit" column. Note that you'll still need to modify your CKAN theme to expose the Unit field in the Data Dictionary tab

### Changed
* set minimum qsv version to 0.107.0

### Fixed
* Allow url parameters. This allows DP+ to process links with URL parameters. Just be sure to specify the resource format to one of the supported DP+ formats so it will be processed
* Properly handle when there is no timezone info when checking if a resource is updated

## [0.12.0] - 2023-05-19

### Changed
* Use single source of configuration
* Containerfile dependencies

### Fixed
* Don't crash when not given content-length header
* Use `--prefer-dmy` with `qsv` instead of `--prefer_dmy`
* Don't crash on missing original column name
* Allow reupload of file if resource metadata has changed
* Reset resource.preview_rows to False if existing resource falls below preview_rows threshold

### Contributors
* @bluepython508

## [0.11.0] - 2023-04-10

### Added
* Added link to datapusher-plus docker
* Added uninstallation procedure
* Added more comments in the main jobs.py process where all the main work is done
* Added details about what qsv analysis enables

### Changed
* Revamped documentation to streamline installation
* set config.py to more conservative defaults
* set minimum QSV version to 0.99.0

### Fixed
* Container packaging fixes
* Fix error handling in validate
* pinned ckanserviceprovider to 1.1.0 and APScheduler to 3.9.1.post1

### Contributors
* @Zharktas
* @EricSoroos
* @minhajuddin2510

## [0.10.1] - 2023-02-03

### Changed
* add separate AUTO_UNIQUE_INDEX setting
* improved Development Installation procedure
* improved Datapusher+ Configuration section, with heavily commented dot-env.template
* bumped qsv from 0.87.0 to 0.87.1, with improved safenames sanitizing
* added qsv version checks

## [0.9.0] - 2023-01-30

### Added
* Updated the readme to include locale installation
* Initial implementation of PII screening

### Contributors
* @jqnatividad
* @minhajuddin2510

## [0.8.0] - 2023-01-18

**More detailed release notes forthcoming...**

## [0.7.0] - 2023-01-17

### Fixed
* fix import of MutableMapping from collections.abc

### Contributors
* @ctrepka

## [0.6.0] - 2023-01-06

### Added
* validate excel file exported CSVs as well, as they can potentially be invalid CSVs (e.g. differing column counts per row)
* support negative values for PREVIEW_ROWS to start previewing from the end of a file (e.g. -1000 = last 1000 rows)
* if an Excel file is invalid or
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DataPusher+ is a CKAN extension (v2.0.0) for ultra-fast, robust data ingestion into CKAN's datastore. It replaces the legacy Datapusher webservice with a full CKAN extension that leverages [qsv](https://github.com/dathere/qsv) (a Rust-based CSV data-wrangling toolkit) for blazing-fast type inference and data analysis.

**Key differentiators:**
- Guaranteed data type inference by scanning entire files (not just first few rows)
- PostgreSQL COPY for direct data loading (no API overhead)
- Jinja2 formula system for metadata inference/suggestion (`formula` and `suggest_formula` in scheming YAML)
- DRUF (Dataset Resource Upload First) workflow support

## Build & Test Commands

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_unit.py

# Run with coverage
pytest --cov=ckanext/datapusher_plus tests/

# Debug with IPython
pytest --pdbcls=IPython.terminal.debugger:TerminalPdb tests/
```

## CKAN CLI Commands

```bash
# Resubmit all resources to datapusher
ckan -c /etc/ckan/default/ckan.ini datapusher_plus resubmit -y

# Submit specific package resources
ckan -c /etc/ckan/default/ckan.ini datapusher_plus submit {dataset_id}

# Database migrations
ckan -c /etc/ckan/default/ckan.ini db upgrade -p datapusher_plus
```

## Architecture

### Pipeline Stage Pattern (v2.0)

The refactored jobs module uses a modular stage-based pipeline in `ckanext/datapusher_plus/jobs/`:

```
pipeline.py          → Main orchestration, entry point (datapusher_plus_to_datastore)
context.py           → ProcessingContext state management across stages
stages/
  base.py            → Abstract BaseStage class
  download.py        → File download with retries, proxy support, timeout handling
  format_converter.py → Excel/ODS/Shapefile/GeoJSON/ZIP → CSV conversion
  validation.py      → RFC-4180 CSV validation, encoding detection/normalization
  analysis.py        → QSV-based type inference, summary stats, frequency tables
  database.py        → PostgreSQL COPY operations, smartint type selection
  indexing.py        → Auto-index creation based on cardinality/dates
  formula.py         → Jinja2 formula evaluation (package/resource metadata)
  metadata.py        → Datastore resource dict updates, dpp_suggestions
```

### Key Modules

- **plugin.py** — CKAN plugin entry point, implements IConfigurer, IConfigurable, IActions, IAuthFunctions, IPackageController, IResourceUrlChange, IResourceController, ITemplateHelpers, IBlueprint, IClick (+ IFormRedirect conditionally)
- **config.py** — ~50 configuration parameters (all `ckanext.datapusher_plus.*` settings)
- **config_declaration.yaml** — CKAN 2.10+ declarative config definitions
- **qsv_utils.py** — QSV CLI wrapper (stats, frequency, type inference, validation)
- **jinja2_helpers.py** — FormulaProcessor and custom filters/functions for metadata formulas
- **datastore_utils.py** — PostgreSQL datastore operations
- **spatial_helpers.py** — Shapefile/GeoJSON processing with geometry simplification
- **pii_screening.py** — PII detection with configurable regex patterns
- **helpers.py** — Template helpers for job status display in CKAN UI
- **cli.py** — CKAN CLI command implementations (resubmit, submit)
- **logging_utils.py** — Custom TRACE logging level (level 5)
- **interfaces.py** — `IDataPusher` interface for external plugin hooks
- **job_exceptions.py** — Custom exception hierarchy (`DataTooBigError`, `JobError`, `HTTPError`, etc.)
- **logic/action.py** — Actions: `datapusher_submit`, `datapusher_hook`, `datapusher_status`
- **logic/schema.py** — Validation schemas for action functions
- **logic/auth.py** — Authorization functions
- **views.py** — Flask blueprints for web endpoints
- **druf_view.py** — DRUF-specific view handling
- **jobs_legacy.py** — Legacy monolithic implementation (preserved for reference)

### Database Models (model/model.py)

- `Jobs` — Job tracking (job_id, status, data, error, timestamps)
- `Metadata` — Formula evaluation results storage
- `Logs` — Detailed processing logs
- `get_job_details()` — Helper function for retrieving job info

### Formula System

Formulas in scheming YAML have access to three namespaces:
- `dpps` — Summary statistics per field (type, min/max, cardinality, stddev, etc.)
- `dppf` — Frequency tables per field (top N values with counts)
- `dpp` — Inferred metadata (RECORD_COUNT, DATE_FIELDS, LAT_FIELD, LON_FIELD, etc.)

Formula types:
- `formula` — Evaluated and assigned to field immediately
- `suggest_formula` — Stored in `dpp_suggestions` field for UI suggestions

## Coding Conventions

- **Python 3.10+** — Uses `from __future__ import annotations` throughout
- **Import organization** — stdlib → third-party → CKAN → local; `import ckan.plugins as p`, `tk = p.toolkit`
- **Type hints** — Used throughout; `from typing import Any, Optional`, etc.
- **Docstrings** — Google-style
- **Naming** — snake_case functions, UPPERCASE constants, PascalCase classes
- **Logging** — Custom TRACE level (5) via `logging_utils.py`; f-string log messages; pipeline stages use `ProcessingContext.logger`
- **Error handling** — Custom exception hierarchy in `job_exceptions.py`
- **Linting** — Flake8 with E501 disabled (long lines allowed): `# flake8: noqa: E501`
- **CI** — `.github/workflows/main.yml` runs integration tests

## External Dependencies

- **Python 3.10, 3.11, 3.12, 3.13**
- **qsv v4.0.0+** — Must be installed at path specified by `ckanext.datapusher_plus.qsv_bin`
- **CKAN 2.10+** with ckanext-scheming
- **PostgreSQL** datastore
- **RQ (Redis Queue)** for background job processing

## Configuration Reference

Key settings in `ckan.ini` (see config.py and config_declaration.yaml for full list):
- `ckanext.datapusher_plus.qsv_bin` — Path to qsv binary
- `ckanext.datapusher_plus.formats` — Supported file formats
- `ckanext.datapusher_plus.preview_rows` — Number of preview rows (default: 1000)
- `ckanext.datapusher_plus.auto_index_threshold` — Cardinality threshold for auto-indexing
- `ckanext.datapusher_plus.prefer_dmy` — Date format preference (DMY vs MDY)
- `ckanext.datapusher_plus.enable_druf` — Enable DRUF workflow
- `ckanext.datapusher_plus.enable_form_redirect` — Enable IFormRedirect interface

```

### File: CONFIG.md
```md
# DataPusher Plus Configuration

## Optional Features

DataPusher Plus includes some optional features that can be enabled through configuration. These features are disabled by default to ensure compatibility with different CKAN versions.

### IFormRedirect Support

The IFormRedirect interface provides custom redirect behavior after dataset and resource form submissions. This interface is only available in certain CKAN branches and is not yet merged into the main CKAN codebase.

**Note**: IFormRedirect methods are only defined when this feature is enabled, keeping the plugin completely clean when disabled.

**Configuration:**
```ini
# Enable IFormRedirect functionality (default: false)
ckanext.datapusher_plus.enable_form_redirect = true
```

**What it does:**
- **Dynamically adds IFormRedirect methods** only when enabled
- Provides custom redirect URLs after dataset/resource creation or editing
- Redirects to dataset page after dataset metadata submission
- Redirects to resource view after resource editing
- Allows "add another resource" workflow
- **Works best with DRUF** for complete resource-first workflow

**Requirements:**
- CKAN version with IFormRedirect interface support
- If the interface is not available, the feature will be automatically disabled with a warning
- **Recommended**: Enable together with DRUF for optimal resource-first experience

### DRUF (Dataset Resource Upload First) Support

DRUF allows users to upload resources before creating the dataset metadata, providing a resource-first workflow.

**Configuration:**
```ini
# Enable DRUF functionality (default: false)  
ckanext.datapusher_plus.enable_druf = true
```

**What it does:**
- Adds a `/resource-first/new` endpoint
- Creates a temporary dataset and redirects to resource upload
- Useful for workflows where users want to upload data files first
- **Overrides templates**: Modifies "Add Dataset" buttons and form stages to support resource-first workflow

**Template Overrides:**
When DRUF is enabled, the following templates are overridden:
- `snippets/add_dataset.html`: Changes "Add Dataset" to redirect to resource upload
- `package/snippets/package_form.html`: Modifies form stages to show "Add data" first
- `scheming/package/snippets/package_form.html`: Modifies scheming form stages

**Requirements:**
- No special CKAN version requirements
- Works with standard CKAN installations
- Compatible with ckanext-scheming

## Example Configuration

Add these lines to your CKAN configuration file (e.g., `/etc/ckan/default/ckan.ini`):

```ini
# Enable DRUF (Dataset Resource Upload First) workflow
ckanext.datapusher_plus.enable_druf = true

# Enable IFormRedirect for better form redirects (recommended with DRUF)
ckanext.datapusher_plus.enable_form_redirect = true
```

**Recommended combinations:**
- **Standard mode**: Both disabled (default) - maintains standard CKAN behavior
- **Resource-first workflow**: Both enabled - complete resource-first experience
- **DRUF only**: Only `enable_druf = true` - resource-first without custom redirects

## Template Organization

DataPusher Plus uses a conditional template loading system to avoid conflicts when optional features are disabled:

- **Base templates** (`templates/`): Always loaded, provides standard DataPusher Plus functionality
- **DRUF templates** (`templates/druf/`): Only loaded when `enable_druf = true`, overrides default dataset creation workflow

This ensures that when DRUF is disabled, your CKAN installation maintains completely standard behavior without any template modifications.

## Backwards Compatibility

When these features are disabled (default), DataPusher Plus maintains full backwards compatibility with standard CKAN installations. The plugin will automatically detect if required interfaces are available and disable features gracefully if they are not supported.

## Logging

The plugin will log the status of these features:
- Info messages when features are successfully enabled
- Warning messages when features are configured but not available
- Debug messages for DRUF blueprint registration

Check your CKAN logs to verify the status of these optional features.

```

### File: default-pii-regexes.txt
```txt
(?x)(?:\d{3}-\d{2}-\d{4}) #SSN
(?x)5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4} #Mastercard
(?x)4\d{3}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4} #Visa
(?x)3[47][0-9]{13} #American Express
(?x)[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z\d]?){0,16} #IBAN
(?x)[\w\.=-]+@[\w\.-]+\.[\w]{2,3} #Email
(?x)(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4} #Phone

```

### File: requirements-dev.txt
```txt
httpretty==1.1.4
pytest
pytest-cov

```

### File: test_config.py
```py
#!/usr/bin/env python3
"""
Test script to verify DataPusher Plus conditional features
"""

import os
import sys

# Add CKAN to Python path (adjust as needed)
sys.path.insert(0, '/usr/lib/ckan/default/src/ckan')

def test_configuration():
    """Test the conditional loading of DataPusher Plus features"""
    
    print("=== DataPusher Plus Configuration Test ===\n")
    
    # Mock configuration scenarios
    test_configs = [
        {
            'name': 'All disabled (default)',
            'config': {}
        },
        {
            'name': 'DRUF enabled only',
            'config': {'ckanext.datapusher_plus.enable_druf': 'true'}
        },
        {
            'name': 'IFormRedirect enabled only',  
            'config': {'ckanext.datapusher_plus.enable_form_redirect': 'true'}
        },
        {
            'name': 'Both enabled',
            'config': {
                'ckanext.datapusher_plus.enable_druf': 'true',
                'ckanext.datapusher_plus.enable_form_redirect': 'true'
            }
        }
    ]
    
    try:
        # Import required modules
        from ckan.plugins import toolkit as tk
        
        for test in test_configs:
            print(f"Testing: {test['name']}")
            print(f"Config: {test['config']}")
            
            # Simulate configuration
            for key, value in test['config'].items():
                tk.config[key] = value
            
            # Test helper functions
            enable_druf = tk.asbool(tk.config.get('ckanext.datapusher_plus.enable_druf', False))
            enable_form_redirect = tk.asbool(tk.config.get('ckanext.datapusher_plus.enable_form_redirect', False))
            
            print(f"  DRUF enabled: {enable_druf}")
            print(f"  IFormRedirect enabled: {enable_form_redirect}")
            
            # Check template directory logic
            template_dirs = ['templates']
            if enable_druf:
                template_dirs.append('templates/druf')
            
            print(f"  Template directories: {template_dirs}")
            print()
            
            # Clear config for next test
            for key in test['config'].keys():
                tk.config.pop(key, None)
                
    except ImportError as e:
        print(f"Could not import CKAN modules: {e}")
        print("This is expected if running outside CKAN environment")
        return False
        
    return True

def check_template_structure():
    """Verify template directory structure"""
    
    print("=== Template Structure Check ===\n")
    
    base_dir = "/usr/lib/ckan/default/src/datapusher-plus/ckanext/datapusher_plus/templates"
    
    # Check expected directories
    expected_dirs = [
        "templates",
        "templates/druf", 
        "templates/druf/snippets",
        "templates/druf/package/snippets",
        "templates/druf/scheming/package/snippets"
    ]
    
    # Check expected files
    expected_files = [
        "templates/snippets/add_dataset.html",
        "templates/druf/snippets/add_dataset.html",
        "templates/package/snippets/package_form.html", 
        "templates/druf/package/snippets/package_form.html",
        "templates/scheming/package/snippets/package_form.html",
        "templates/druf/scheming/package/snippets/package_form.html"
    ]
    
    print("Checking directories:")
    for dir_path in expected_dirs:
        full_path = os.path.join(base_dir, dir_path.replace("templates/", ""))
        if dir_path == "templates":
            full_path = base_dir
        exists = os.path.exists(full_path)
        print(f"  {dir_path}: {'✓' if exists else '✗'}")
    
    print("\nChecking template files:")
    for file_path in expected_files:
        full_path = os.path.join(base_dir, file_path.replace("templates/", ""))
        if file_path.startswith("templates/") and not file_path.startswith("templates/druf"):
            full_path = os.path.join(base_dir, file_path[10:])  # Remove "templates/"
        exists = os.path.exists(full_path)
        print(f"  {file_path}: {'✓' if exists else '✗'}")
    
    print()

if __name__ == "__main__":
    print("DataPusher Plus Configuration and Template Test\n")
    
    check_template_structure()
    test_configuration()
    
    print("=== Summary ===")
    print("✓ Template structure organized for conditional loading")
    print("✓ Configuration options available for DRUF and IFormRedirect")
    print("✓ Backwards compatibility maintained when features disabled")
    print("\nTo enable features, add to your CKAN config:")
    print("  ckanext.datapusher_plus.enable_druf = true")
    print("  ckanext.datapusher_plus.enable_form_redirect = true")

```

### File: wsgi.py
```py
# Use this file for development, on a production setup (eg a CKAN production
# install) use deployment/datapusher.wsgi

import ckanserviceprovider.web as web

from datapusher.config import config

web.init()

import datapusher.jobs as jobs
# check whether jobs have been imported properly
assert(jobs.push_to_datastore)

web.app.run(config.get('HOST'), config.get('PORT'))

```

### File: docs\dataset_schema.yaml
```yaml
scheming_version: 2
dataset_type: dataset
about: >
  A reimplementation of the default CKAN dataset schema
  extended with DataPusher+ Jinja2 Formulas to make
  DCAT3 metadata generation easier!
about_url: https://github.com/dathere/datapusher-plus

dataset_fields:
  - field_name: title
    label: Title
    preset: title
    form_placeholder: eg. A descriptive title

  - field_name: name
    label: URL
    preset: dataset_slug
    form_placeholder: eg. my-dataset

  - field_name: notes
    label: Description
    form_snippet: markdown.html
    form_placeholder: eg. Some useful notes/blurb about the data
    # TODO: Add a suggestion formula that suggests an LLM-generated description
    # of the dataset based on the dataset's metadata, ALL the dataset's resources
    # and their statistical properties.

  - field_name: latitude_range
    label: Latitude Range
    # This is a suggestion formula that calculates the latitudinal range of the dataset.
    # It uses the inferred latitude field (dpp.LAT_FIELD) which is automatically detected
    # based on column name patterns and value ranges (-90 to 90 for latitude).
    # The formula calculates the difference between max and min values, which is
    # automatically computed by DataPusher+ using the qsv stats command.
    # The truncate_with_ellipsis filter is used to limit text length.
    suggestion_formula: >
      Latitudinal range {{dpps[dpp.LAT_FIELD].stats.max|float - dpps[dpp.LAT_FIELD].stats.min|float }}
      {{"the quick brown fox"|truncate_with_ellipsis(5)}}

  - field_name: spatial_extent
    label: Spatial Extent
    form_snippet: markdown.html
    # This suggestion formula generates a WKT (Well-Known Text) representation of the dataset's spatial extent.
    # It automatically uses the inferred latitude and longitude fields unless explicitly specified.
    # The spatial_extent_wkt() Jinja2 custom function creates a POLYGON that encompasses all data points.
    # By leveraging the extensive statistical info compiled by DP+ and the expressiveness
    # of Jinja2, we have a powerful, easily extensible Formula Language for DataPusher+!
    # Check out jinja2_helpers.py for more examples of custom Jinja2 filters and functions.
    suggestion_formula: "{{ spatial_extent_wkt() }}"

  - field_name: tag_string
    label: Tags
    preset: tag_string_autocomplete
    form_placeholder: eg. economy, mental health, government
    # TODO: Add a suggestion formula that suggests tags based on the dataset's metadata,
    # ALL the dataset's resources and their statistical properties. The tags
    # will be compiled at the same time the notes field above is derived using an LLM.

  - field_name: license_id
    label: License
    form_snippet: license.html
    help_text: License definitions and additional information can be found at http://opendefinition.org/

  - field_name: owner_org
    label: Organization
    preset: dataset_organization

  - field_name: url
    label: Source
    form_placeholder: http://example.com/dataset.json
    display_property: foaf:homepage
    display_snippet: link.html

  - field_name: version
    label: Version
    validators: ignore_missing unicode_safe package_version_validator
    form_placeholder: "1.0"

  - field_name: author
    label: Author
    form_placeholder: Joe Bloggs
    display_property: dc:creator

  - field_name: author_email
    label: Author Email
    form_placeholder: joe@example.com
    display_property: dc:creator
    display_snippet: email.html
    display_email_name_field: author

  - field_name: test_derived_field
    label: Test Derived Field
    # This is a DIRECT formula (not a suggestion) that sets the field's value at creation/update.
    # It combines the package author name (title-cased) with their email address.
    # The result is stored directly in the field rather than as a suggestion.
    formula: "Contact: {{package.author|title}} - Email: {{package.author_email}}"

  - field_name: maintainer
    label: Maintainer
    form_placeholder: Joe Bloggs
    display_property: dc:contributor

  - field_name: maintainer_email
    label: Maintainer Email
    form_placeholder: joe@example.com
    display_property: dc:contributor
    display_snippet: email.html
    display_email_name_field: maintainer

  # DP+ uses this field to store the suggestions it generates for the dataset
  # and its resources. It also has a STATUS field to track the progress of
  # formula processing, which is used by the Suggestion UI to indicate when
  # all suggestions have been processed.
  - field_name: dpp_suggestions
    label: DPP Suggestion
    preset: json_object

resource_fields:
  - field_name: url
    label: URL
    preset: resource_url_upload

  - field_name: name
    label: Name
    form_placeholder: eg. January 2011 Gold Prices

  - field_name: description
    label: Description
    form_snippet: markdown.html
    form_placeholder: Some useful notes about the data
    # TODO: Add a suggestion formula that suggests an LLM-generated description of the resource
    # based on the resource's metadata, the resource's data and its statistical properties.

  - field_name: format
    label: Format
    preset: resource_format_autocomplete

  - field_name: resource_spatial_extent
    label: Resource Spatial Extent
    form_snippet: markdown.html
    # This suggestion formula creates a WKT POLYGON representing the spatial extent of the dataset.
    # It uses the inferred latitude and longitude fields to calculate the bounding box.
    # The coordinates are ordered as: (min_lat, min_lon), (min_lat, max_lon),
    # (max_lat, max_lon), (max_lat, min_lon), (min_lat, min_lon).
    suggestion_formula: >
      POLYGON(({{dpps[dpp.LAT_FIELD].stats.min|float}}, {{dpps[dpp.LON_FIELD].stats.min|float}},
      {{dpps[dpp.LAT_FIELD].stats.max|float}}, {{dpps[dpp.LON_FIELD].stats.min|float}}, 
      {{dpps[dpp.LAT_FIELD].stats.max|float}}, {{dpps[dpp.LON_FIELD].stats.max|float}}, 
      {{dpps[dpp.LAT_FIELD].stats.min|float}}, {{dpps[dpp.LON_FIELD].stats.max|float}}, 
      {{dpps[dpp.LAT_FIELD].stats.min|float}}, {{dpps[dpp.LON_FIELD].stats.min|float}}))

  - field_name: frequency_info
    label: Frequency Info
    form_snippet: markdown.html
    # This suggestion formula uses get_frequency_top_values() to analyze the
    # frequency distribution of values in the "department" field. It returns
    # the top N most common values with their counts and percentages.
    suggestion_formula: '{{ get_frequency_top_values("department") }}'

  - field_name: temporal_resolution
    label: Temporal Resolution
    # This suggestion formula calculates the minimum time interval between dates in the dataset.
    # It automatically detects date columns based on configurable patterns.
    # Returns an ISO 8601 duration string (e.g., "P1D" for daily, "P1M" for monthly).
    # Requires datastore.sqlsearch.enabled to be true in CKAN config.
    # This is illustrative of how otherwise "expensive", hard-to-compile, optional
    # but recommended DCAT3 metadata can be computed on-demand using DP+ and Jinja2.
    suggestion_formula: "{{ temporal_resolution() }}"

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
