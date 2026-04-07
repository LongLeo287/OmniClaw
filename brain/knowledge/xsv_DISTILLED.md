---
id: xsv
type: knowledge
owner: OA_Triage
---
# xsv
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# `xsv` is now unmaintained

In lieu of `xsv`, I'd recommend either
[qsv](https://github.com/dathere/qsv)
or
[xan](https://github.com/medialab/xan).

-------------------------------------------------------------------------------


xsv is a command line program for indexing, slicing, analyzing, splitting
and joining CSV files. Commands should be simple, fast and composable:

1. Simple tasks should be easy.
2. Performance trade offs should be exposed in the CLI interface.
3. Composition should not come at the expense of performance.

This README contains information on how to
[install `xsv`](https://github.com/BurntSushi/xsv#installation), in addition to
a quick tour of several commands.

[![Linux build status](https://api.travis-ci.org/BurntSushi/xsv.svg)](https://travis-ci.org/BurntSushi/xsv)
[![Windows build status](https://ci.appveyor.com/api/projects/status/github/BurntSushi/xsv?svg=true)](https://ci.appveyor.com/project/BurntSushi/xsv)
[![](https://meritbadge.herokuapp.com/xsv)](https://crates.io/crates/xsv)

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org).


### Available commands

* **cat** - Concatenate CSV files by row or by column.
* **count** - Count the rows in a CSV file. (Instantaneous with an index.)
* **fixlengths** - Force a CSV file to have same-length records by either
  padding or truncating them.
* **flatten** - A flattened view of CSV records. Useful for viewing one record
  at a time. e.g., `xsv slice -i 5 data.csv | xsv flatten`.
* **fmt** - Reformat CSV data with different delimiters, record terminators
  or quoting rules. (Supports ASCII delimited data.)
* **frequency** - Build frequency tables of each column in CSV data. (Uses
  parallelism to go faster if an index is present.)
* **headers** - Show the headers of CSV data. Or show the intersection of all
  headers between many CSV files.
* **index** - Create an index for a CSV file. This is very quick and provides
  constant time indexing into the CSV file.
* **input** - Read CSV data with exotic quoting/escaping rules.
* **join** - Inner, outer and cross joins. Uses a simple hash index to make it
  fast.
* **partition** - Partition CSV data based on a column value.
* **sample** - Randomly draw rows from CSV data using reservoir sampling (i.e.,
  use memory proportional to the size of the sample).
* **reverse** - Reverse order of rows in CSV data.
* **search** - Run a regex over CSV data. Applies the regex to each field
  individually and shows only matching rows.
* **select** - Select or re-order columns from CSV data.
* **slice** - Slice rows from any part of a CSV file. When an index is present,
  this only has to parse the rows in the slice (instead of all rows leading up
  to the start of the slice).
* **sort** - Sort CSV data.
* **split** - Split one CSV file into many CSV files of N chunks.
* **stats** - Show basic types and statistics of each column in the CSV file.
  (i.e., mean, standard deviation, median, range, etc.)
* **table** - Show aligned output of any CSV data using
  [elastic tabstops](https://github.com/BurntSushi/tabwriter).


### A whirlwind tour

Let's say you're playing with some of the data from the
[Data Science Toolkit](https://github.com/petewarden/dstkdata), which contains
several CSV files. Maybe you're interested in the population counts of each
city in the world. So grab the data and start examining it:

```bash
$ curl -LO https://burntsushi.net/stuff/worldcitiespop.csv
$ xsv headers worldcitiespop.csv
1   Country
2   City
3   AccentCity
4   Region
5   Population
6   Latitude
7   Longitude
```

The next thing you might want to do is get an overview of the kind of data that
appears in each column. The `stats` command will do this for you:

```bash
$ xsv stats worldcitiespop.csv --everything | xsv table
field       type     min            max            min_length  max_length  mean          stddev         median     mode         cardinality
Country     Unicode  ad             zw             2           2                                                   cn           234
City        Unicode   bab el ahmar  Þykkvibaer     1           91                                                  san jose     2351892
AccentCity  Unicode   Bâb el Ahmar  ïn Bou Chella  1           91                                                  San Antonio  2375760
Region      Unicode  00             Z9             0           2                                        13         04           397
Population  Integer  7              31480498       0           8           47719.570634  302885.559204  10779                   28754
Latitude    Float    -54.933333     82.483333      1           12          27.188166     21.952614      32.497222  51.15        1038349
Longitude   Float    -179.983333    180            1           14          37.08886      63.22301       35.28      23.8         1167162
```

The `xsv table` command takes any CSV data and formats it into aligned columns
using [elastic tabstops](https://github.com/BurntSushi/tabwriter). You'll
notice that it even gets alignment right with respect to Unicode characters.

So, this command takes about 12 seconds to run on my machine, but we can speed
it up by creating an index and re-running the command:

```bash
$ xsv index worldcitiespop.csv
$ xsv stats worldcitiespop.csv --everything | xsv table
...
```

Which cuts it down to about 8 seconds on my machine. (And creating the index
takes less than 2 seconds.)

Notably, the same type of "statistics" command in another
[CSV command line toolkit](https://csvkit.readthedocs.io/)
takes about 2 minutes to produce similar statistics on the same data set.

Creating an index gives us more than just faster statistics gathering. It also
makes slice operations extremely fast because *only the sliced portion* has to
be parsed. For example, let's say you wanted to grab the last 10 records:

```bash
$ xsv count worldcitiespop.csv
3173958
$ xsv slice worldcitiespop.csv -s 3173948 | xsv table
Country  City               AccentCity         Region  Population  Latitude     Longitude
zw       zibalonkwe         Zibalonkwe         06                  -19.8333333  27.4666667
zw       zibunkululu        Zibunkululu        06                  -19.6666667  27.6166667
zw       ziga               Ziga               06                  -19.2166667  27.4833333
zw       zikamanas village  Zikamanas Village  00                  -18.2166667  27.95
zw       zimbabwe           Zimbabwe           07                  -20.2666667  30.9166667
zw       zimre park         Zimre Park         04                  -17.8661111  31.2136111
zw       ziyakamanas        Ziyakamanas        00                  -18.2166667  27.95
zw       zizalisari         Zizalisari         04                  -17.7588889  31.0105556
zw       zuzumba            Zuzumba            06                  -20.0333333  27.9333333
zw       zvishavane         Zvishavane         07      79876       -20.3333333  30.0333333
```

These commands are *instantaneous* because they run in time and memory
proportional to the size of the slice (which means they will scale to
arbitrarily large CSV data).

Switching gears a little bit, you might not always want to see every column in
the CSV data. In this case, maybe we only care about the country, city and
population. So let's take a look at 10 random rows:

```bash
$ xsv select Country,AccentCity,Population worldcitiespop.csv \
  | xsv sample 10 \
  | xsv table
Country  AccentCity       Population
cn       Guankoushang
za       Klipdrift
ma       Ouled Hammou
fr       Les Gravues
la       Ban Phadèng
de       Lüdenscheid      80045
qa       Umm ash Shubrum
bd       Panditgoan
us       Appleton
ua       Lukashenkivske
```

Whoops! It seems some cities don't have population counts. How pervasive is
that?

```bash
$ xsv frequency worldcitiespop.csv --limit 5
field,value,count
Country,cn,238985
Country,ru,215938
Country,id,176546
Country,us,141989
Country,ir,123872
City,san jose,328
City,san antonio,320
City,santa rosa,296
City,santa cruz,282
City,san juan,255
AccentCity,San Antonio,317
AccentCity,Santa Rosa,296
AccentCity,Santa Cruz,281
AccentCity,San Juan,254
AccentCity,San Miguel,254
Region,04,159916
Region,02,142158
Region,07,126867
Region,03,122161
Region,05,118441
Population,(NULL),3125978
Population,2310,12
Population,3097,11
Population,983,11
Population,2684,11
Latitude,51.15,777
Latitude,51.083333,772
Latitude,50.933333,769
Latitude,51.116667,769
Latitude,51.133333,767
Longitude,23.8,484
Longitude,23.2,477
Longitude,23.05,476
Longitude,25.3,474
Longitude,23.1,459
```

(The `xsv frequency` command builds a frequency table for each column in the
CSV data. This one only took 5 seconds.)

So it seems that most cities do not have a population count associated with
them at all. No matter—we can adjust our previous command so that it only
shows rows with a population count:

```bash
$ xsv search -s Population '[0-9]' worldcitiespop.csv \
  | xsv select Country,AccentCity,Population \
  | xsv sample 10 \
  | xsv table
Country  AccentCity       Population
es       Barañáin         22264
es       Puerto Real      36946
at       Moosburg         4602
hu       Hejobaba         1949
ru       Polyarnyye Zori  15092
gr       Kandíla          1245
is       Ólafsvík         992
hu       Decs             4210
bg       Sliven           94252
gb       Leatherhead      43544
```

Erk. Which country is `at`? No clue, but the Data Science Toolkit has a CSV
file called `countrynames.csv`. Let's grab it and do a join so we can see which
countries these are:

```bash
curl -LO https://gist.githubusercontent.com/anonymous/063cb470e56e64e98cf1/raw/98e2589b801f6ca3ff900b01a87fbb7452eb35c7/countrynames.csv
$ xsv headers countrynames.csv
1   Abbrev
2   Country
$ xsv join --no-case  Country sample.csv Abbrev countrynames.csv | xsv table
Country  AccentCity       Population  Abbrev  Country
es       Barañáin         22264       ES      Spain
es       Puerto Real      36946       ES      Spain
at       Moosburg         4602        AT      Austria
hu       Hejobaba         1949        HU      Hungary
ru       Polyarnyye Zori  15092       RU      Russian Federation | Russia
gr       Kandíla          1245        GR      Greece
is       Ólafsvík         992         IS      Iceland
hu       Decs             4210        HU      Hungary
bg       Sliven           94252       BG      Bulgaria
gb       Leatherhead      43544       GB      Great Britain | UK | England | Scotland | Wales | Northern Ireland | United Kingdom
```

Whoops, now we have two columns called `Country` and an `Abbrev` column that we
no longer need. This is easy to fix by re-ordering columns with the `xsv
select` command:

```bash
$ xsv join --no-case  Country sample.csv Abbrev countrynames.csv \
  | xsv select 'Country[1],AccentCity,Population' \
  | xsv table
Country                                                                              AccentCity       Population
Spain                                                                                Barañáin         22264
Spain                                                                                Puerto Real      36946
Austria                                                                              Moosburg         4602
Hungary                                                                              Hejobaba         1949
Russian Federation | Russia                                                          Polyarnyye Zori  15092
Greece                                                                               Kandíla          1245
Iceland                                                                              Ólafsvík         992
Hungary                                                                              Decs             4210
Bulgaria                                                                             Sliven           94252
Great Britain | UK | England | Scotland | Wales | Northern Ireland | United Kingdom  Leatherhead      43544
```

Perhaps we can do this with the original CSV data? Indeed we can—because
joins in `xsv` are fast.

```bash
$ xsv join --no-case Abbrev countrynames.csv Country worldcitiespop.csv \
  | xsv select '!Abbrev,Country[1]' \
  > worldcitiespop_countrynames.csv
$ xsv sample 10 worldcitiespop_countrynames.csv | xsv table
Country                      City                   AccentCity             Region  Population  Latitude    Longitude
Sri Lanka                    miriswatte             Miriswatte             36                  7.2333333   79.9
Romania                      livezile               Livezile               26      1985        44.512222   22.863333
Indonesia                    tawainalu              Tawainalu              22                  -4.0225     121.9273
Russian Federation | Russia  otar                   Otar                   45                  56.975278   48.305278
France                       le breuil-bois robert  le Breuil-Bois Robert  A8                  48.945567   1.717026
France                       lissac                 Lissac                 B1                  45.103094   1.464927
Albania                      lumalasi               Lumalasi               46                  40.6586111  20.7363889
China                        motzushih              Motzushih              11                  27.65       111.966667
Russian Federation | Russia  svakino                Svakino                69                  55.60211    34.559785
Romania                      tirgu pancesti         Tirgu Pancesti         38                  46.216667   27.1
```

The `!Abbrev,Country[1]` syntax means, "remove the `Abbrev` column and remove
the second occurrence of the `Country` column." Since we joined with
`countrynames.csv` first, the first `Country` name (fully expanded) is now
included in the CSV data.

This `xsv join` command takes about 7 seconds on my machine. The performance
comes from constructing a very simple hash index of one of the CSV data files
given. The `join` command does an inner join by default, but it also has left,
right and full outer join support too.


### Installation

Binaries for Windows, Linux and macOS are available [from Github](https://github.com/BurntSushi/xsv/releases/latest).

If you're a **macOS Homebrew** user, then you can install xsv
from homebrew-core:

```
$ brew install xsv
```

If you're a **macOS MacPorts** user, then you can install xsv
from the [official ports](https://www.macports.org/ports.php?by=name&substr=xsv):

```
$ sudo port install xsv
```

If you're a **Nix/NixOS** user, you can install xsv from nixpkgs:

```
$ nix-env -i xsv
```

Alternatively, you can compile from source by
[installing Cargo](https://crates.io/install)
([Rust's](https://www.rust-lang.org/) package manager)
and installing `xsv` using Cargo:

```bash
cargo install xsv
```

Compiling from this repository also works similarly:

```bash
git clone git://github.com/Burn
... [TRUNCATED]
```

### File: .zenodo.json
```json
{
  "language": "eng",
  "license": "MIT",
  "title": "xan, the CSV magician.",
  "upload_type": "software",
  "keywords": [
    "rust",
    "cli",
    "terminal",
    "data manipulation",
    "csv",
    "tsv"
  ],
  "creators": [
    {
      "orcid": "0000-0003-4916-8472",
      "affiliation": "médialab - Sciences Po",
      "name": "Guillaume Plique"
    },
    {
      "orcid": "0000-0003-4074-2976",
      "affiliation": "médialab - Sciences Po",
      "name": "Béatrice Mazoyer"
    },
    {
      "affiliation": "médialab - Sciences Po",
      "name": "Laura Miguel"
    },
    {
      "affiliation": "médialab - Sciences Po",
      "name": "César Pichon"
    },
    {
      "affiliation": "médialab - Sciences Po",
      "name": "Anna Charles"
    },
    {
      "affiliation": "médialab - Sciences Po",
      "name": "Julien Pontoire"
    },
    {
      "affiliation": "médialab - Sciences Po",
      "name": "Evan Chevalerias"
    }
  ],
  "access_right": "open",
  "description": "<p>A CSV-centric data manipulation CLI tool written in Rust.</p>"
}

```

### File: BENCHMARKS.md
```md
These are some very basic and unscientific benchmarks of various commands
provided by `xsv`. Please see below for more information.

These benchmarks were run with
[worldcitiespop_mil.csv](https://burntsushi.net/stuff/worldcitiespop_mil.csv),
which is a random 1,000,000 row subset of the world city population dataset
from the [Data Science Toolkit](https://github.com/petewarden/dstkdata).

These benchmarks were run on an Intel i7-6900K (8 CPUs, 16 threads) with 64GB
of memory.

```
count                   0.11 seconds   413.76  MB/sec
flatten                 4.54 seconds   10.02   MB/sec
flatten_condensed       4.45 seconds   10.22   MB/sec
frequency               1.82 seconds   25.00   MB/sec
index                   0.12 seconds   379.28  MB/sec
sample_10               0.18 seconds   252.85  MB/sec
sample_1000             0.18 seconds   252.85  MB/sec
sample_100000           0.29 seconds   156.94  MB/sec
search                  0.27 seconds   168.56  MB/sec
select                  0.14 seconds   325.09  MB/sec
search                  0.13 seconds   350.10  MB/sec
select                  0.13 seconds   350.10  MB/sec
sort                    2.18 seconds   20.87   MB/sec
slice_one_middle        0.08 seconds   568.92  MB/sec
slice_one_middle_index  0.01 seconds   4551.36 MB/sec
stats                   1.09 seconds   41.75   MB/sec
stats_index             0.15 seconds   303.42  MB/sec
stats_everything        1.94 seconds   23.46   MB/sec
stats_everything_index  0.93 seconds   48.93   MB/sec
```

### Details

The purpose of these benchmarks is to provide a rough ballpark estimate of how
fast each command is. My hope is that they can also catch significant
performance regressions.

The `count` command can be viewed as a sort of baseline of the fastest possible
command that parses every record in CSV data.

The benchmarks that end with `_index` are run with indexing enabled.

```

### File: CHANGELOG.md
```md
# Changelog

## 0.57.0 (provisional)

*Breaking*

* `xan select -n` will not error anymore on empty inputs and, generally, empty files should not trigger selection errors when using commands with `-n/--no-headers`.
* `xan heatmap -C/--cram` becomes a flag accepting either `auto`, `always` or `never`.
* Dropping `-C` short flag for `xan sort --cells` (it could be confused with `--columns` or `--check`).
* Completely overhauled how datetimes work in moonblade.
* `xan separate` will not trim splitted values with some modes by default anymore.
* Dropping `xan network --stats` in favor of `-f stats`.
* `-D` becomes short flag for `xan network --degrees` instead of `--disjoint-keys`.

*Features*

* Adding `xan matrix count` & `xan matrix adj`.
* Adding `front_coding` window function.
* Timestamp support with `xan plot -LT`.
* Adding `xan rename -n/--no-headers` support for `-p/--prefix` & `-x/--suffix`.
* Adding `xan from -f parquet` (requires the `parquet` feature).
* Adding `xan to latex`.
* Adding `xan top -L/--lexicographic`.
* Adding `xan heatmap` flags: `-w/--width`, `-F/--fill`, `-a/--align`, `-U/--unit`, `-Z/--show-normalized`, `-A/--ascii`, `-l/--label` & `-v/--values`.
* Adding new gradients to `xan heatmap`.
* Adding `range` & `repeat` moonblade functions.
* Adding `xan sort --columns`.
* Adding `xan view -T/--tee`.
* Adding `now`, `fractional_days`, `to_timezone`, `to_local_timezone`, `with_timezone`, `with_local_timezone`, `without_timezone`, `to_timestamp`, `to_timestamp_ms`, `from_timestamp`, `from_timestamp_ms`, `span`, `date` & `time` moonblade functions.
* Better type inference with `xan stats`, and the `type` & `types` aggregation functions, now including more types for temporal values (`zoned_datetime`, `datetime`, `date` & `time`).
* Adding `xan input -T/--tolerant`.
* Adding `xan separate --trim`.
* Adding `xan grep -B/--before-context & -A/--after-context`.
* Adding `xan network -f=components, -S/--simple, --union-find, --minify & --sample-size <n>`.

*Fixes*

* Fixing `xan separate` automatic column prefix extraction.
* Fixing `xan heatmap -n`.
* Fixing `xan heatmap --repeat-headers --cram always` not repeating x-axis legend.
* Fixing correctness of `xan plot -T` and increase resolution to microseconds.
* Fixing moonblade column-related functions returning incorrect results wrt `-n/--no-headers`.

*Performance*

* Improving performance of `xan complete`, `xan top`, `xan plot -T` & `xan hist`.
* Improving overall performance of `xan network`.
* Slightly optimizing `xan vocab` by allowing needless heap allocation & indirection.

*Quality of Life*

* Adding proper help to `xan heatmap`.

## 0.56.0

*Features*

* Adding `xan bisect`.
* Adding `xan flatten -N/--non-empty`.
* Adding the `soundex`, `refined_soundex` & `phonogram` moonblade functions for phonetic encoding.

*Fixes*

* Fixing `xan to (md|html) --no-headers`.
* Fixing `xan plot -R/--regression-line`.

*Quality of Life*

* Adding `xan to markdown` as an alias for `xan to md`.
* `xan flatten` & `xan view` will stop masquerading trimmed empty cells as empty.

## 0.55.0

*Breaking*

* Changing how `xan separate` generates default column names.
* `xan from -f=(json|ndjson|jsonl)` will now emit column in input order by default.
* Changing `xan to -B/--buffer-size` to `--sample-size` to harmonize flag names with `xan from`.

*Features*

* Adding the `xan complete` command.
* Adding an optional unit to `ceil`, `floor`, `round` & `trunc` moonblade function. E.g. floor to nearest decade: `floor(year, 10)`.
* Adding `basename` & `dirname` moonblade functions.
* Adding `parse_py_literal` moonblade functions. Useful to deal with files dubiously serialized using `pandas`.
* Adding `xan view --repeat-headers=(auto|always|never)`.
* Adding `xan view --reveal-whitespace=(auto|always|never)`.
* Adding `--color` support to `XAN_VIEW_ARGS`.
* Adding `xan from -f json --sample-size -1` to sample the whole file.
* Adding `xan from -f json --single-object`.
* Adding `xan from --sort-keys`.
* Adding `xan to (json|ndjson|jsonl) --sample-size -1` to sample the whole file.
* Adding `xan to (json|ndjson|jsonl) --strings` flag.
* Adding `xan separate --prefix`.
* Adding `xan heatmap -C` short flag for `--cram`.
* Adding `xan heatmap --repeat-headers`.
* Adding `rank`, `cume_dist`, `percent_rank` and `ntile` window functions.
* Adding `xan help --color`.

*Fixes*

* Fixing `xan select -ne` incorrectly emitting headers.

*Quality of Life*

* `xan view -p` will not print bottom header anymore by default.
* `xan view` will not reveal problematic whitespace if output is not colored anymore, by default.
* Better `xan hist` error messages and help.
* Testing more file name variants when searching for a `.gzi` index.

## 0.54.1

*Fixes*

* Fixing `xan freq --groupby` incorrectly unescaping group cells.
* Fixing help related to `xan pivot` & `xan unpivot`.
* Upgrading `simd-csv` to get safety fixes.
* Fixing evaluation of moonblade commands related to column indexing.

## 0.54.0

The **SIMD** update.

*Breaking*

* Bumping MSRV to `1.83.0`.
* Dropping `xan plot -Y/--add-series`. It is now possible to select multiple columns as `<y>` in  `xan plot <x> <y>` instead.
* Dropping the `-C/--force-colors` flag in `flatten`, `heatmap`, `hist`, `plot` and `view` in favor of the more standardized and flexible `--color=(auto|never|always)` flag.
* `xan join` will now automatically drop joined columns from one the files when it is obviously safe to do so.
* `xan behead` & `xan rename` do not normalize the output anymore to be as fast as possible.
* The new SIMD CSV parser might not deal with CSV irregular cases the same way `rust-csv` did. In any case, `xan input` will still continue to use `rust-csv`.
* `xan slice -B/--byte-offset` & `xan slice -A/--accumulate` are now mutually exclusive.
* `xan input` has been overhauled.
* Dropping `xan count --sample-size`.
* Overhauling `xan fixlengths` to accept streams by shifting default from double-pass read to buffering the whole stream into memory.
* `xan plot --x-scale log & --y-scale log` are now natural log. Use `log10` for the base10 log as before.
* Dropping `xan reverse -m/--in-memory` flag. Behavior is now automatically detected.
* Dropping `xan shuffle -m/--in-memory` flag. Loading the file into memory is now the default. The `xan shuffle -e/--external` flag has been added if
you want the old default behavior.
* `xan bins` now outputs `<empty>` values instead of `<nulls>`.
* Overhauling `xan bins`. The default is now to find nice boundaries for the bins. Use `-e/--exact` to revert to the old behavior. The default number of bins is now `10`, and won't use Freedman-Diaconis rule by default. A `-H/--heuristic` flag has been added if you want to automatically select a suitable number of bins.

*Features*

* Adding `xan flatten -F/--flatter`.
* `xan pivot` can now target multiple columns.
* Adding the `xan grep` command for fast but coarse filtering.
* Adding `xan search -f/--flag`.
* Adding `xan map -F/--filter`.
* `xan search -B/--breakdown` now consolidates the results when multiple patterns have a same name.
* Adding `xan flatten --row-separator`.
* Adding `xan flatten --csv`.
* Adding `xan headers --color`.
* Adding the `xan join <columns> <input1> <input2>` arity as a convenience when joined column names are the same in both inputs.
* Adding `xan join -D/--drop-key=(none|both|left|right)`.
* Adding `xan fuzzy-join -D/--drop-key=(none|both|left|right)`.
* Adding `xan plot -A/--aggregate`.
* Adding support for plural selection clauses in both `xan select -e` & `xan map` e.g. `xan map 'full_name.split(" ") as (first_name, last_name)`.
* Adding `xan search -P/--add-pattern`.
* Adding `xan groupby -M/--along-matrix`.
* Adding `xan groupby -T/--total`.
* Adding support for `.ndjson` & `.jsonl` files. Those are considered as headless TSV files with null byte quoting so you can easily use them with `xan` commands.
* Adding out-of-the-box support for `.vcf`, `.sam`, `.bed`, `.gtf` & `.gff2` files.
* Adding a `xan cat cols` alias to `xan cat columns`.
* Adding `zstd` support.
* Adding `earliest` & `latest` moonblade functions.
* Adding `xan dedup -f/--flag`.
* Adding `-k` short flag for `xan dedup --keep-duplicates`, and `-C` short flag for `xan dedup --choose`.
* Adding `xan fixlengths -H/--trust-header`.
* Adding `xan separate`.
* Adding full log scale support to `xan plot`.
* Adding `xan hist --scale`.
* `xan window` is now able to run total aggregations.
* Adding `thousands_sep`, `comma` and `significance` kwargs to `numfmt` moonblade function.

*Fixes*

* Fixing `xan dedup --check` bug where the first record was ignored.
* Fixing `xan hist -D` when a same date is found multiple times.
* Fixing `xan from -f xls` datetime conversion.
* Fixing `xan flatten` & `xan view` when column names contain line breaks.
* Fixing invalid argument parsing error being printed to stdout instead of stderr.
* Fixing `xan progress` SIGINT corrupting output.
* Fixing `xan enum -A/--accumulate`.
* Fixing `xan from -f tar` when tarball archive is not gzipped.
* Fixing `min` & `max` moonblade function when passing a list of numbers.
* Fixing `xan flatten -H` edge cases.
* Fixing commands requiring seekable streams accepting unindexed compressed files by error.
* Fixing `xan plot --count --y-scale log`.

*Performance*

* Wildly improving performance of most of `xan` commands by leveraging a novel SIMD CSV parser/writer.
* Improving performance of `xan from -f txt` & `xan from -f npy`.
* Improving memory footprint of hash-based commands (e.g. `frequency`, `groupby`, `dedup` etc.).
* Improving performance of `xan progress`, `xan range`, `xan enum`, `xan behead`, `xan rename`.

*Quality of Life*

* `xan parallel cat` now flushing more consistently.
* Better highlighting of problematic strings in `xan flatten`, `xan view` & `xan headers`.
* `xan parallel` will now generally stop as soon as an error is detected in a subprocess and cleanly report errors.
* Better argv parsing error UX in general.
* The `-p` flag will now avoid going further than 16 to avoid issues on server with many CPUs where hogging the resources is an issue and where using too much threads at once could hurt performance. The `-t` flag remain available to tweak the number of threads.
* `xan hist` will now dim bars having a `0` count so you can easily distinguish them from non-empty bars.

## 0.53.0

*Breaking*

* `xan partition` now normalizes filenames to lowercase to correctly deal with case-insensitive filesystems. `xan partition` also gets a related `-C/--case-sensitive` flag.

*Features*

* Adding `all` and `any` moonblade higher-order functions.
* Allowing moonblade `printf` function to be called with lists.
* Adding `-f/--evaluate-file` flag to `map`, `filter`, `flatmap` & `transform` commands.
* Adding `xan map -O/--overwrite`.

*Fixes*

* Fixing `xan top -T/--ties` edge case.
* Fixing broken pipe panics for some commands.
* Dropping remnant `dbg!` macro when reading files in reverse.
* `xan flatten -H` now correctly working on more data types.

*Performance*

* Using `jemallocator` for musl builds.

*Quality of Life*

* Better moonblade `printf` function error messages.

## 0.52.0

*Breaking*

* `xan search --count` will not emit rows with 0 matches anymore unless `--left` is used.

*Features*

* `xan transform` is now able to work on a selection of columns, rather than on a single column.
* Adding the `xan unpivot` command.
* Adding the `xan pivot` command.
* Adding `xan join --semi` & `xan join --anti` commands.
* Adding `xan slice --raw`.
* Adding default expression argument to `lead` & `lag` window functions.
* Adding `shlex_split`, `cmd` and `shell` moonblade functions.
* Adding `aarch64-apple-darwin` and `aarch64-unknown-linux-gnu` to CI builds.
* Adding `to_fixed` moonblade function.
* Adding decimal places optional argument to `ratio` & `percentage` aggregation functions.
* Adding `frac` & `dense_rank` aggregation functions to `xan window`.

*Fixes*

* Loosening `xan partition` sanitizer to allow hyphens, dashes and points.
* Fixing `xan parallel --progress` display.
* Fixing logic error in `xan search -B` when using without `--left`.
* Fixing `xan parallel cat` when working on file chunks with `-P` or `-H`.
* Fixing moonblade list/string slicing with some combinations of negatives indices.
* Fixing moonblade `split` function not using regex patterns properly.
* Fixing moonblade parsing wrt regex patterns and comments (using a regex pattern containing `#` was not possible).
* Fixing `lead` window aggregation function when working on any column that is not the first one.
* Fixing `xan view -S/--significance` being overzealous, especially wrt integers.

*Performance*

* Improving performance of `xan parallel` when working on file chunks.

*Quality of Life*

* `xan headers` now report more useful information when files have diverging headers.
* Better error messages for `read_json` and `parse_json` moonblade functions.
* `xan view -p` will not engage pager when input errored or is empty.
* `xan select -e & -f` become boolean flags instead of error-inducing invocation variants.

## 0.51.0

The **parallel** update.

*Breaking*

* Dropping undocumented `xan index` and related interactions (in `xan count`, `xan sample`, `xan slice` & `xan split --jobs`).
* Dropping now useless `coalesce` moonblade function.
* `xan split` now accepts its output directory as an optional flag.
* `xan partition` now accepts its output directory as an optional flag.
* `xan split -s` becomes `xan split -S` to avoid confusion with the `-s/--select` flag used everywhere else.
* Dropping useless `xan count --csv` flag.
* Dropping `xan freq -t/--threshold`. Use `xan freq | xan filter 'count >= n'` instead.
* Adding `xan slice -I/--indices` taking care of `xan slice -i` polymorphism taking multiple indices before.
* `xan parallel freq` now follows `xan freq` behavior regarding limits.
* Dropping `xan url-join` & `xan regex-join`. Both commands have been merged into a new `xan fuzzy-join` command using the `-u/--url-prefix` & `-r/--regex` flags respectively.
* `xan from --sheet` becomes `--sheet-name` and is no longer the default. `--sheet-index 0` becomes the default.
* Dropping `xan foreach`. It is not distinctive enough as you can use `xan map` for the same purpose and get useful information about the results of evaluated side effects or write to `/dev/null`.
* Renaming `xan agg --cols` to `xan agg --along-rows`.
* Changing `cell` placeholder to anonymous `_` value in `xan agg -R/--along-rows`.
* Dropping moonblade commands `-E/--errors` flags. A lot has changed since they were created. They will be reevaluated in the future if required. You can rely on the `try` & `warn` moonblade functions instead, for now.
* Dropping `xan select -A/--append`. Latest `xan map` is now actually equivalent to `xan select -eA`.
* Changing `xan map` to accept a selection expression able to create multiple columns at once rather than a 
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to `xan`

## How to release

1. Bump the version in `Cargo.toml`.
2. Drop `(provisional)` in `CHANGELOG.md`.
3. Commit `Bump <version>`.
4. Run `./scripts/release.sh`.

```

### File: ci\before_deploy.sh
```sh
# `before_deploy` phase: here we package the build artifacts

set -ex

. $(dirname $0)/utils.sh

# Generate artifacts for release
mk_artifacts() {
    cargo build --target $TARGET --release
}

mk_tarball() {
    # create a "staging" directory
    local td=$(mktempd)
    local out_dir=$(pwd)

    # TODO update this part to copy the artifacts that make sense for your project
    # NOTE All Cargo build artifacts will be under the 'target/$TARGET/{debug,release}'
    cp target/$TARGET/release/xsv $td

    pushd $td

    # release tarball will look like 'rust-everywhere-v1.2.3-x86_64-unknown-linux-gnu.tar.gz'
    tar czf $out_dir/${PROJECT_NAME}-${TRAVIS_TAG}-${TARGET}.tar.gz *

    popd
    rm -r $td
}

main() {
    mk_artifacts
    mk_tarball
}

main

```

### File: ci\install.sh
```sh
# `install` phase: install stuff needed for the `script` phase

set -ex

. $(dirname $0)/utils.sh

install_c_toolchain() {
    case $TARGET in
        aarch64-unknown-linux-gnu)
            sudo apt-get install -y --no-install-recommends \
                 gcc-aarch64-linux-gnu libc6-arm64-cross libc6-dev-arm64-cross
            ;;
        *)
            # For other targets, this is handled by addons.apt.packages in .travis.yml
            ;;
    esac
}

install_rustup() {
    curl https://sh.rustup.rs -sSf \
      | sh -s -- -y --default-toolchain=$TRAVIS_RUST_VERSION

    rustc -V
    cargo -V
}

install_standard_crates() {
    if [ $(host) != "$TARGET" ]; then
        rustup target add $TARGET
    fi
}

configure_cargo() {
    local prefix=$(gcc_prefix)

    if [ ! -z $prefix ]; then
        # information about the cross compiler
        ${prefix}gcc -v

        # tell cargo which linker to use for cross compilation
        mkdir -p .cargo
        cat >>.cargo/config <<EOF
[target.$TARGET]
linker = "${prefix}gcc"
EOF
    fi
}

main() {
    install_c_toolchain
    install_rustup
    install_standard_crates
    configure_cargo

    # TODO if you need to install extra stuff add it here
}

main

```

### File: ci\script.sh
```sh
# `script` phase: you usually build, test and generate docs in this phase

set -ex

. $(dirname $0)/utils.sh

# NOTE Workaround for rust-lang/rust#31907 - disable doc tests when cross compiling
# This has been fixed in the nightly channel but it would take a while to reach the other channels
disable_cross_doctests() {
    if [ $(host) != "$TARGET" ] && [ "$TRAVIS_RUST_VERSION" = "stable" ]; then
        if [ "$TRAVIS_OS_NAME" = "osx" ]; then
            brew install gnu-sed --default-names
        fi

        find src -name '*.rs' -type f | xargs sed -i -e 's:\(//.\s*```\):\1 ignore,:g'
    fi
}

# TODO modify this function as you see fit
# PROTIP Always pass `--target $TARGET` to cargo commands, this makes cargo output build artifacts
# to target/$TARGET/{debug,release} which can reduce the number of needed conditionals in the
# `before_deploy`/packaging phase
run_test_suite() {
    case $TARGET in
        # configure emulation for transparent execution of foreign binaries
        aarch64-unknown-linux-gnu)
            export QEMU_LD_PREFIX=/usr/aarch64-linux-gnu
            ;;
        arm*-unknown-linux-gnueabihf)
            export QEMU_LD_PREFIX=/usr/arm-linux-gnueabihf
            ;;
        *)
            ;;
    esac

    if [ ! -z "$QEMU_LD_PREFIX" ]; then
        # Run tests on a single thread when using QEMU user emulation
        export RUST_TEST_THREADS=1
    fi

    cargo build --target $TARGET --verbose
    cargo test --target $TARGET

    # sanity check the file type
    file target/$TARGET/debug/xsv
}

main() {
    disable_cross_doctests
    run_test_suite
}

main

```

### File: ci\utils.sh
```sh
mktempd() {
    echo $(mktemp -d 2>/dev/null || mktemp -d -t tmp)
}

host() {
    case "$TRAVIS_OS_NAME" in
        linux)
            echo x86_64-unknown-linux-gnu
            ;;
        osx)
            echo x86_64-apple-darwin
            ;;
    esac
}

gcc_prefix() {
    case "$TARGET" in
        aarch64-unknown-linux-gnu)
            echo aarch64-linux-gnu-
            ;;
        arm*-gnueabihf)
            echo arm-linux-gnueabihf-
            ;;
        *)
            return
            ;;
    esac
}

dobin() {
    [ -z $MAKE_DEB ] && die 'dobin: $MAKE_DEB not set'
    [ $# -lt 1 ] && die "dobin: at least one argument needed"

    local f prefix=$(gcc_prefix)
    for f in "$@"; do
        install -m0755 $f $dtd/debian/usr/bin/
        ${prefix}strip -s $dtd/debian/usr/bin/$(basename $f)
    done
}

architecture() {
    case $1 in
        x86_64-unknown-linux-gnu|x86_64-unknown-linux-musl)
            echo amd64
            ;;
        i686-unknown-linux-gnu|i686-unknown-linux-musl)
            echo i386
            ;;
        arm*-unknown-linux-gnueabihf)
            echo armhf
            ;;
        *)
            die "architecture: unexpected target $TARGET"
            ;;
    esac
}

```

### File: docs\LOVE_LETTER.md
```md
# A love letter to the CSV format

*Or why people pretending CSV is dead are wrong*

Every month or so, a new blog article declaring the near demise of CSV in favor of some "obviously superior" format ([parquet](https://parquet.apache.org/), newline-delimited JSON, [MessagePack](https://msgpack.org/) records etc.) find its ways to the reader's eyes. Sadly those articles often offer a very narrow and biased comparison and often fail to understand what makes CSV a seemingly unkillable staple of data serialization.

It is therefore my intention, through this article, to write a love letter to this data format, often criticized for the wrong reasons, even more so when it is somehow deemed "cool" to hate on it. My point is not, far from it, to say that CSV is a silver bullet but rather to shine a light on some of the format's sometimes overlooked strengths.

## 1. CSV is dead simple

The specification of CSV holds in its title: "comma separated values". Okay, it's a lie, but still, the specification holds in a tweet and can be explained to anybody in seconds: commas separate values, new lines separate rows. Now quote values containing commas and line breaks, double your quotes, and that's it. This is so simple you might even invent it yourself without knowing it already exists while learning how to program.

Of course it does not mean you should not use a dedicated CSV parser/writer because you *will* mess something up.

## 2. CSV is a collective idea

No one owns CSV. It has no real specification (yes, I know about the controversial ex-post [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180)), just a set of rules everyone kinda agrees to respect implicitly. It is, and will forever remain, an open and free collective idea.

## 3. CSV is text

Like JSON, YAML or XML, CSV is just plain text, that you are free to encode however you like. CSV is not a binary format, can be opened with any text editor and does not require any specialized program to be read. This means, by extension, that it can both be read and edited by humans directly, somehow.

## 4. CSV is streamable

CSV can be read row by row very easily without requiring more memory than what is needed to fit a single row. This also means that a trivial program that anyone can write is able to read gigabytes of CSV data with only some kilobytes of RAM.

By comparison, column-oriented data formats such as parquet are not able to stream files row by row without requiring you to jump here and there in the file or to buffer the memory cleverly so you don't tank read performance.

But of course, CSV is terrible if you are only interested in specific columns because you will indeed need to read all of a row only to access the part you are interested in.

Column-oriented data format are of course a very good fit for the dataframes mindset of R, pandas and such. But critics of CSV coming from this set of practices tend to only care about use-cases where everything is expected to fit into memory.

## 5. CSV can be appended to

It is trivial to add new rows at the end of a CSV file and it is very efficient to do so. Just open the file in append mode (`a+`) and get going.

Once again, column-oriented data formats cannot do this, or at least not in a straightforward manner. They can actually be regarded as on-disk dataframes, and like with dataframes, adding a column is very efficient while adding a new row really isn't.

## 6. CSV is dynamically typed

Please don't flee. Let me explain why this is sometimes a good thing. Sometimes when dealing with data, you might like to have some flexibility, especially across programming languages, when parsing serialized data.

Consider JavaScript, for instance, that is unable to represent 64 bits integers. Or what languages, frameworks and libraries consider as null values (don't get me started on pandas and null values). CSV lets you parse values as you see fit and is in fact dynamically typed. But this is as much of a strength as it can become a potential footgun if you are not careful.

Note also, but this might be hard to do with higher-level languages such as python and JavaScript, that you are not required to decode the text at all to process CSV cell values and that you can work directly on the binary representation of the text for performance reasons.

## 7. CSV is succinct

Having the headers written only once at the beginning of the file means the amount of formal repetition of the format is naturally very low. Consider a list of objects in JSON or the equivalent in XML and you will quickly see the cost of repeating keys everywhere. That does not mean JSON and XML will not compress very well, but few formats exhibit this level of natural conciseness.

What's more, strings are often already optimally represented and the overhead of the format itself (some commas and quotes here and there) is kept to a minimum. Of course, statically-typed numbers could be represented more concisely, but you will not save up an order of magnitude there neither.

## 8. Reverse CSV is still valid CSV

This one is not often realized by everyone but a reversed (byte by byte) CSV file, is still valid CSV. This is only made possible because of the genius idea to escape quotes by doubling them, which means escaping is a palindrome. It would not work if CSV used a backslash-based escaping scheme, as is most common when representing string literals.

But why should you care? Well, this means you can read very efficiently and very easily the last rows of a CSV file. Just feed the bytes of your file in reverse order to a CSV parser, then reverse the yielded rows and their cells' bytes and you are done (maybe read the header row before though).

This means you can very well use a CSV output as a way to efficiently resume an aborted process. You can indeed read and parse the last rows of a CSV file in constant time since you don't need to read the whole file but only to position yourself at the end of the file to buffer the bytes in reverse and feed them to the parser.

## 9. Excel hates CSV

It clearly means CSV must be doing something right.

Signed: [xan](https://github.com/medialab/xan#readme), the CSV magician

<!-- flaws about multiplexing, asv -->

```

### File: docs\NOTES.md
```md
# Misc Notes

## Regarding count-min sketch

Default params: `0.95p, 0.0001tol, ()`
```

### File: docs\PIPELINES.md
```md
# `xan` pipelines

Curated collection of unhinged `xan` pipelines.

## Summary

* [Paginating urls to download](#paginating-urls-to-download)
* [Making sure a crawler was logged in by reading files in parallel](#making-sure-a-crawler-was-logged-in-by-reading-files-in-parallel)
* [Parsing logs using `xan separate`](#parsing-logs-using-xan-separate)
* [Running subprocesses to extract raw text from PDF files](#running-subprocesses-to-extract-raw-text-from-pdf-files)
* [Matching multiple queries in a press articles corpus, in parallel](#matching-multiple-queries-in-a-press-articles-corpus-in-parallel)
* [Producing a heatmap of popularity profiles of top Twitter accounts](#producing-a-heatmap-of-popularity-profiles-of-top-twitter-accounts)

## Paginating urls to download

Let's say you want to download the latest 50 pages from [Hacker News](https://news.ycombinator.com). Fortunately our [`minet`](https://github.com/medialab/minet) tool knows how to efficiently download a bunch of urls fed through a CSV file.

The idea here is to generate CSV data out of thin air and to transform it into an url list to be fed to the `minet fetch` command:

```bash
xan range --start 1 50 --inclusive | \
xan select --evaluate '"https://news.ycombinator.com/?p=" ++ n as url' | \
minet fetch url --input -
```

The `xan range` command produces a CSV looking like this:

| n   |
| --- |
| 1   |
| 2   |
| 3   |
| 4   |
| 5   |
| ... |

Then the `xan select --evaluate` part uses the following expression to transform the file on the fly:

```python
# We append the content of the "n" column to the given url
"https://news.ycombinator.com/?p=" ++ n as url
```

This gives us:

| url                               |
| --------------------------------- |
| https://news.ycombinator.com/?p=1 |
| https://news.ycombinator.com/?p=2 |
| https://news.ycombinator.com/?p=3 |
| https://news.ycombinator.com/?p=4 |
| https://news.ycombinator.com/?p=5 |
| ...                               |

That is fit to be fed into `minet fetch`.

## Making sure a crawler was logged in by reading files in parallel

Let's say you crawled some media website and 1. wrote all the downloaded files into a directory (aptly named `downloaded`) and 2. produced a CSV report listing the downloaded files and their relative paths on disk.

Now you had to be logged in to retrieve the full text of crawled articles. Because you are a dilligent individual, you did not forget to use a proper authenticated cookie while crawling. But what if you messed up? Let's double check pages were crawled correctly.

Fortunately, the crawled media website shows your username on the top right section of each page when you are logged in, so you could easily check whether everything went smoothly by searching for an occurrence of your very specific username (`yomguithereal`) in every HTML file downloaded.

Let's do so with `xan`, in parallel, with a progress bar for flair (indeed, reading millions of HTML files tends to take some time):

```bash
xan progress crawl.csv | \
xan filter --parallel '"downloaded".pathjoin(path).read() | !contains(_, /yomguithereal/i)' | \
> not-crawled-correctly.csv
```

Here the `xan filter` command will know, thanks to the `--parallel` flag, how to use a suitable amount of threads to read and test files as fast as possible.

Now the following moonblade expression:

```perl
"downloaded".pathjoin(path).read() | !contains(_, /yomguithereal/i)
```

means: "join `downloaded` to each row's `path` column value, then read the content at the created full relative path, then check whether it does not contain an occurrence of the `/yomguithereal/i` case-insenstive regex".

## Parsing logs using `xan separate`

`xan separate` is a command able to "separate" a single CSV column into multiple ones through a variety of different methods. It boasts both a `-r/--regex` and `-c/--capture-groups` flags that let you give a regex pattern and create new columns based on its matched groups. It is therefore suitable to use it to parse logs.

See an example here of using a command to parse k8s access logs to structure them better and produce some quick time series:

```bash
xan from --from txt ~/Downloads/access.log.gz --column log | \
xan separate log -rc '- - \[([^\]]+)\] "([^"]+)" (\d+) \d+ "[^"]*" "([^"]+)"' \
  --keep \
  --into datetime,http_call,http_status,user_agent \ |
xan map --overwrite 'datetime.datetime("%d/%b/%Y:%H:%M:%S %z") as datetime, http_call.split(" ")[1] as url' \
> logs.csv
```

First we use the `xan from` command to convert our log lines into proper CSV data (log lines can contain commas or quotes for instance and those must be dealt with properly).

Then we apply our unwieldy regex to create some new columns given to the `--into` flag. The `--keep` flag is here because we want to keep the original log line in the result, so we can add further processing later on if needed.

Now, time in the logs is indicated using this atrocious format: `11/Jun/2025:05:48:49 +0000`, so we apply a `xan map` command to the result to convert it to something more appealing like ISO and we also extract the url from HTTP call at the same time. The `--overwrite` flag of the `map` command means we can replace any column from input having the same name in the output. Here it means we will replace the `datetime` column altogether and add a new one named `url`. This saves us a `xan transform` in addition to the `xan map`.

Now here is what a time series of all the logs look like:

```bash
# We use --ignore because some records don't have a time
# The --count flag means we don't have value for the y axis, we just
# want to count number of rows for each time slot
xan plot --line --time datetime --count logs.csv --ignore
```

![separate-log1](./img/pipelines/separate-log1.png)

But as with any access log, there is noise related to bots and people accessing stylesheets, scripts & images so let's focus on our website's homepage thusly:

```bash
# Searching exact matches for url "/", that is to say the homepage
xan search -s url --exact / logs.csv | xan plot -LT datetime --count
```

![separate-log2](./img/pipelines/separate-log2.png)

## Running subprocesses to extract raw text from PDF files

Ok, let's go wild: we have downloaded a long list of PDF reports from some UN subcommittee. We will attempt to use the `pdftotext` command on them to extract their raw text so we can do proper NLP down the line. But there is an issue: we are very bad at using the `xargs` or `parallel` commands and never remember how to write a proper bash loop.

Don't worry, `xan` is here for us:

```bash
xan filter 'http_status == 200 && col("path", 1).endswith(".pdf")' report-files.csv | \
xan map --parallel 'col("path", 1) | pjoin("files", _) | fmt("pdftotext {} -", _) | shell(_).trim() as text' | \
xan select ndoc,uid,title,lastModified,link,text | \
xan rename -s lastModified last_modified > report-files-with-raw-text.csv
```

Here `xan` was able to manage `pdftotext` subprocesses (using the `shell` moonblade function), in parallel, for each row of our CSV file listing the reports on disk, so we can add the extracted text in a new column. Pretty rad, no?

We need to use `col("path", 1)` in our expressions because of course there are two distinct columns with same name in our input CSV file.

We also use the `xan rename` command in the end because mixing camelCase and snake_case is an unforgivable fashion *faux-pas*.

## Matching multiple queries in a press articles corpus, in parallel

We have a corpus of several GBs of CSV files containing press articles from various French media outlets.

We need to match a bunch of regex patterns in each article to plot time series of the relevance of climate change-related concepts across time.

Here is our `queries.csv` file:

| name                 | pattern                                                      |
| -------------------- | ------------------------------------------------------------ |
| query_climatique     | \bclimatique                                                 |
| query_effet_de_serre | effet\s+de\s+serre\|couche\s+d[’']ozone                      |
| query_biodiversite   | \bbiodiversit[ée]                                            |
| query_transition     | transitions?\s+(?:[ée]cologique\|[ée]n[ée]rg[ée]tique)       |
| query_durable        | d[ée]veloppement\s+durable\|[ée]n[ée]rgies?\s+renouvelables? |

Here is our parallel `xan` pipeline:

```bash
xan parallel cat \
  --progress \
  --source-column media \
  --buffer-size -1 \
  --preprocess '
    map "date_published.ym().try() || `N/A` as month" |
    search --breakdown --regex --ignore-case -s headline,description,text
      --patterns queries.csv
      --pattern-column pattern
      --name-column name |
    groupby month --along-columns "query_*" "sum(_)" |
    sort -s month' \
  */articles.csv.gz | \
xan transform media '_.split("/")[0]' > $BASE_DIR/matches.csv
```

*Regarding `parallel cat`*

`xan parallel cat` consumes a bunch of CSV files (here everything matching `*/articles.csv.gz`), applies some sort of preprocessing on each file (as given to the `--preprocess` flag here) and redirect everything to the standard output.

<p align="center">
  <img src="https://i.redd.it/io23lob82pp61.jpg" alt="parallel cats" width="250px" />
</p>

The`--progress` flag means we want to display a progress bar, `--source-column` means we want to add a new column to the output tracking which file a row came from (here each CSV file is in fact the collection of all articles from one media, so it is important to remember from which file each row came from).

When running a `xan parallel cat` command, output rows are flushed regularly to stdout to avoid overflowing memory. This means however that the command must lock an access to stdout to serialize the result and avoid race conditions between threads. This ultimately means that output rows might be in some arbitrary order. Here, because we are using `xan search --breakdown`, we know beforehand that each media will only get one row per month in the output. We can therefore afford holding all breakdown rows per media before flushing them, in order to ensure that output order remains consistent (meaning that resulting rows per media are not interleaved in the output). To do so we use the `--buffer-size -1` flag.

*Regarding preprocessing*

Here is our preprocessing (the `xan` part can be omitted in a command fed to `--preprocess`):

```bash
map "date_published.ym().try() || `N/A` as month" |
search --breakdown --regex --ignore-case -s headline,description,text
  --patterns queries.csv
  --pattern-column pattern
  --name-column name |
groupby month --along-columns "query_*" "sum(_)" |
sort -s month
```

First we create a column by extracting the month from an article date, because we are going to use it for aggregating search results. For instance `2023-01-01T02:45:07+01:00` would become `2023-01`.

Then we apply the `search` command, feeding patterns from `queries.csv` using the `--patterns` flag. `--pattern-column` lets us tell which column of `queries.csv` contain the actual regex pattern, while `--name-column` indicates an associated name that will be used by the `--breakdown` flag to produce output columns.

Now let's consider the following file:

| group | text                   |
| ----- | ---------------------- |
| one   | the cat eats the mouse |
| one   | the sun is shining     |
| two   | a cat is nice          |

Using `search --breakdown` on it with patterns `the` and `cat` will produce the following result:

| group | text                   | the | cat |
| ----- | ---------------------- | --- | --- |
| one   | the cat eats the mouse | 2   | 1   |
| one   | the sun is shining     | 1   | 0   |
| two   | a cat is nice          | 0   | 1   |

We add one column per query and tally the number of their occurrences.

Now the `groupby --along-columns` part lets us run a same aggregation over a selection of columns. So the following command on our previous example:

```bash
groupby group --along-columns the,cat 'sum(_)'
```

Would produce the following result:

| group | the | cat |
| ----- | --- | --- |
| one   | 3   | 1   |
| two   | 0   | 1   |

Finally we use the `sort` command to make sure rows are sorted by month, and that's it (lol).

*Regarding the final transformation*

The last `xan transform` invocation is here to transform a file path into a proper media name. For instance `lemonde/articles.csv.gz` will become `lemonde`.

## Producing a heatmap of popularity profiles of top Twitter accounts

We have a CSV file of 3M tweets. We want to see a top 20 of most retweeted accounts and compare their popularity profiles in terms of number or retweets, replies and likes respectively.

Here is how to do that:

```bash
xan groupby user_screen_name 'mean(retweet_count) as rt, mean(reply_count) as rp, mean(like_count) as lk' tweets.csv | \
xan top rt --limit 20 | \
xan heatmap --size 2 --cram --gradient inferno --show-numbers
```

Here is the result:

![twitter-heatmap](./img/pipelines/twitter-heatmap.png)

We first use `xan groupby` to aggregate the data per Twitter user. We use short names for output columns such as `rt` or `lk` because it will fit easier in the legend of the resulting heatmap.

Then we rank Twitter users and keep the top 20 using `xan top`.

Finally we pipe everything into `xan heatmap` using the following flags:

* `--size 2` means we want our heatmap squares to be 2 characters tall
* `--cram` means we want to cram ou x-axis labels on top of the heatmap squares (they are short enough to fit, else they would get truncated)
* `--gradient inferno` means we want a stylish gradient for the colors because we are hipsters
* `--show-numbers` means we want to display numbers within the heatmap squares

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
