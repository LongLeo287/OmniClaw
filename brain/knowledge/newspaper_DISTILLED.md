---
id: newspaper
type: knowledge
owner: OA_Triage
---
# newspaper
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: requirements.txt
```txt
beautifulsoup4>=4.4.1
cssselect>=0.9.2
feedfinder2>=0.0.4
feedparser>=5.2.1
jieba3k>=0.35.1
lxml>=3.6.0
nltk>=3.2.1
Pillow>=3.3.0
pythainlp>=1.7.2
python-dateutil>=2.5.3
PyYAML>=3.11
requests>=2.10.0
tinysegmenter==0.3  # TODO(codelucas): Investigate making this >=0.3
tldextract>=2.0.1
```

### File: setup.py
```py
#!/bin/python2.7
# -*- coding: utf-8 -*-
"""
Lucas Ou-Yang 2014 -- http://codelucas.com
"""

import sys
import os
import codecs


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


packages = [
    'newspaper',
]


if sys.argv[-1] == 'publish':
    # PYPI now uses twine for package management.
    # For this to work you must first `$ pip3 install twine`
    os.system('python3 setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()


# This *must* run early. Please see this API limitation on our users:
# https://github.com/codelucas/newspaper/issues/155
if sys.version_info[0] == 2 and sys.argv[-1] not in ['publish', 'upload']:
    sys.exit('WARNING! You are attempting to install newspaper3k\'s '
             'python3 repository on python2. PLEASE RUN '
             '`$ pip3 install newspaper3k` for python3 or '
             '`$ pip install newspaper` for python2')


with open('requirements.txt') as f:
    required = f.read().splitlines()


with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='newspaper3k',
    version='0.3.0',
    description='Simplified python article discovery & extraction.',
    long_description=readme,
    author='Lucas Ou-Yang',
    author_email='lucasyangpersonal@gmail.com',
    url='https://github.com/codelucas/newspaper/',
    packages=packages,
    include_package_data=True,
    install_requires=required,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)

```

### File: CHANGELOG.md
```md
# Change Log

## [0.1.7](https://github.com/codelucas/newspaper/tree/0.1.7) (2016-01-30)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.1.6...0.1.7)

**Closed issues:**

- ImportError: cannot import name 'Image' [\#183](https://github.com/codelucas/newspaper/issues/183)
- Won't let me import [\#182](https://github.com/codelucas/newspaper/issues/182)
- Install on Mac - El Capitan Failed - "Operation not permitted"  [\#181](https://github.com/codelucas/newspaper/issues/181)
- Downgrades to old versions of required packages upon installation [\#174](https://github.com/codelucas/newspaper/issues/174)
- Handling 404, 500, and other non-200 http response codes to prevent scraping error pages [\#142](https://github.com/codelucas/newspaper/issues/142)
- Libray downgrading in installation [\#138](https://github.com/codelucas/newspaper/issues/138)

**Merged pull requests:**

- Don't scrape error pages [\#190](https://github.com/codelucas/newspaper/pull/190) ([yprez](https://github.com/yprez))
- Added Hebrew stop words for language support [\#188](https://github.com/codelucas/newspaper/pull/188) ([alon7](https://github.com/alon7))
- Fix installation and build [\#187](https://github.com/codelucas/newspaper/pull/187) ([yprez](https://github.com/yprez))
- Fix installation docs [\#184](https://github.com/codelucas/newspaper/pull/184) ([yprez](https://github.com/yprez))
- Travis CI integration [\#180](https://github.com/codelucas/newspaper/pull/180) ([yprez](https://github.com/yprez))
- requirements.txt - Use minimal instead of exact versions [\#179](https://github.com/codelucas/newspaper/pull/179) ([yprez](https://github.com/yprez))
- Handle lxml raising ValueError on node.itertext\(\) - Python 3 [\#178](https://github.com/codelucas/newspaper/pull/178) ([yprez](https://github.com/yprez))
- Handle lxml raising ValueError on node.itertext\(\) [\#144](https://github.com/codelucas/newspaper/pull/144) ([yprez](https://github.com/yprez))
- Parse byline fix [\#132](https://github.com/codelucas/newspaper/pull/132) ([davecrumbacher](https://github.com/davecrumbacher))

## [0.1.6](https://github.com/codelucas/newspaper/tree/0.1.6) (2016-01-10)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.1.5...0.1.6)

**Closed issues:**

- Critical leak in newspaper.mthreading.Worker [\#177](https://github.com/codelucas/newspaper/issues/177)
- HTMLParseError [\#165](https://github.com/codelucas/newspaper/issues/165)
- Take local paths to .html files [\#153](https://github.com/codelucas/newspaper/issues/153)
- Wall Street Journal Full Text is not Correctly Scraped [\#150](https://github.com/codelucas/newspaper/issues/150)
- Article HTML Returning Null [\#131](https://github.com/codelucas/newspaper/issues/131)
- No articles [\#130](https://github.com/codelucas/newspaper/issues/130)
- Loading Pages that use heavy javascript [\#127](https://github.com/codelucas/newspaper/issues/127)
- Login handling for premium websites [\#126](https://github.com/codelucas/newspaper/issues/126)
- Installation of nltk is failing [\#121](https://github.com/codelucas/newspaper/issues/121)

**Merged pull requests:**

- Support urls with dots [\#176](https://github.com/codelucas/newspaper/pull/176) ([alexanderlukanin13](https://github.com/alexanderlukanin13))
- upgrade beautifulsoup4 to 4.4.1 for python 3.5 [\#171](https://github.com/codelucas/newspaper/pull/171) ([AlJohri](https://github.com/AlJohri))
- Updated requests version [\#170](https://github.com/codelucas/newspaper/pull/170) ([adrienthiery](https://github.com/adrienthiery))
- Turkish Language added [\#169](https://github.com/codelucas/newspaper/pull/169) ([muratcorlu](https://github.com/muratcorlu))
- Add macedonian stopwords [\#166](https://github.com/codelucas/newspaper/pull/166) ([dimitrovskif](https://github.com/dimitrovskif))
- Issue\#95 added graceful string concatenation [\#157](https://github.com/codelucas/newspaper/pull/157) ([surajssd](https://github.com/surajssd))
- fix for "jpeg error with PIL, Can't convert 'NoneType' object to str implicitly" [\#154](https://github.com/codelucas/newspaper/pull/154) ([hnykda](https://github.com/hnykda))
- bugfix in article.py, is\_valid\_body [\#149](https://github.com/codelucas/newspaper/pull/149) ([ms8r](https://github.com/ms8r))
- Fixed typo [\#139](https://github.com/codelucas/newspaper/pull/139) ([Eleonore9](https://github.com/Eleonore9))
- Correct link for the Python 3 branch [\#136](https://github.com/codelucas/newspaper/pull/136) ([jtpio](https://github.com/jtpio))
- Add python3-pip install step for Ubuntu [\#135](https://github.com/codelucas/newspaper/pull/135) ([irnc](https://github.com/irnc))

## [0.1.5](https://github.com/codelucas/newspaper/tree/0.1.5) (2015-03-04)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.1.4...0.1.5)

**Closed issues:**

- is there any kind of documentation on centos 7? [\#114](https://github.com/codelucas/newspaper/issues/114)
- Add extraction publishing date from article. [\#3](https://github.com/codelucas/newspaper/issues/3)

**Merged pull requests:**

- bumping nltk to 2.0.5 - see \#824 in nltk [\#125](https://github.com/codelucas/newspaper/pull/125) ([hexelon](https://github.com/hexelon))

## [0.1.4](https://github.com/codelucas/newspaper/tree/0.1.4) (2015-02-04)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.1.3...0.1.4)

**Closed issues:**

- Getting rate limiting issue? [\#116](https://github.com/codelucas/newspaper/issues/116)
- newspaper.build\( \) error [\#111](https://github.com/codelucas/newspaper/issues/111)
- Allow lists in Parser.clean\_article\_html\(\) [\#108](https://github.com/codelucas/newspaper/issues/108)

**Merged pull requests:**

- Fix incorrect log call while generating articles [\#115](https://github.com/codelucas/newspaper/pull/115) ([curita](https://github.com/curita))
- Allow lists in clean\_article\_html\(\) - fixes \#108 [\#112](https://github.com/codelucas/newspaper/pull/112) ([ecesena](https://github.com/ecesena))
- Fixed nodeToString\(\) to return valid HTML [\#110](https://github.com/codelucas/newspaper/pull/110) ([ecesena](https://github.com/ecesena))
- Fixed empty return in top\_meta\_image [\#109](https://github.com/codelucas/newspaper/pull/109) ([ecesena](https://github.com/ecesena))

## [0.1.3](https://github.com/codelucas/newspaper/tree/0.1.3) (2015-01-15)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.1.2...0.1.3)

**Implemented enhancements:**

- Fulltext extraction improvement \#1 [\#105](https://github.com/codelucas/newspaper/issues/105)

**Closed issues:**

- Tags h1 in article\_html - indented behavior? [\#107](https://github.com/codelucas/newspaper/issues/107)

**Merged pull requests:**

- Fulltext extraction improvement \#1 [\#106](https://github.com/codelucas/newspaper/pull/106) ([codelucas](https://github.com/codelucas))

## [0.1.2](https://github.com/codelucas/newspaper/tree/0.1.2) (2015-01-01)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.1.1...0.1.2)

**Closed issues:**

- Metatags on Vice.com [\#103](https://github.com/codelucas/newspaper/issues/103)
- Can't extract images from german newspapers [\#96](https://github.com/codelucas/newspaper/issues/96)
- article\_html misses many of the images [\#89](https://github.com/codelucas/newspaper/issues/89)

**Merged pull requests:**

- Integrate UnicodeDammit, deprecate parser\_class, deprecate encodeValue, refactor, scaffolding for more unit tests [\#104](https://github.com/codelucas/newspaper/pull/104) ([codelucas](https://github.com/codelucas))

## [0.1.1](https://github.com/codelucas/newspaper/tree/0.1.1) (2014-12-27)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.1.0...0.1.1)

**Closed issues:**

- UnicodeDecodeError: 'utf8' codec can't decode byte 0xcc [\#99](https://github.com/codelucas/newspaper/issues/99)
- TypeError: Can't convert 'bytes' object to str implicitly [\#98](https://github.com/codelucas/newspaper/issues/98)
- \[Parse lxml ERR\] Unicode strings with encoding declaration are not supported. Please use bytes input or XML fragments without declaration. [\#78](https://github.com/codelucas/newspaper/issues/78)
- UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 11: ordinal not in range\(128\) [\#77](https://github.com/codelucas/newspaper/issues/77)
- article.text  and keywords error [\#47](https://github.com/codelucas/newspaper/issues/47)

**Merged pull requests:**

- Huge bugfix to aid lxml DOM parsing + remove unhelpful and excess exception messages and added tracebacks to exception logging [\#102](https://github.com/codelucas/newspaper/pull/102) ([codelucas](https://github.com/codelucas))
- Decode bytestring returned from lxml's `toString` early on before sending it out to outer code [\#101](https://github.com/codelucas/newspaper/pull/101) ([codelucas](https://github.com/codelucas))
- Fixed \#78: Remove encoding tag because lxml won't accept it for unicode [\#97](https://github.com/codelucas/newspaper/pull/97) ([mhall1](https://github.com/mhall1))

## [0.1.0](https://github.com/codelucas/newspaper/tree/0.1.0) (2014-12-17)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.0.9...0.1.0)

## [0.0.9](https://github.com/codelucas/newspaper/tree/0.0.9) (2014-12-17)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.0.8...0.0.9)

**Closed issues:**

- object has no attribute clean Error when using parse method [\#90](https://github.com/codelucas/newspaper/issues/90)
- Questions [\#85](https://github.com/codelucas/newspaper/issues/85)
- \[nltk\_data\] Error loading brown: \<urlopen error \[Errno -2\] Name or \[nltk\_data\]     service not known\> [\#84](https://github.com/codelucas/newspaper/issues/84)
- newspaper unable to find embeded youtube video [\#82](https://github.com/codelucas/newspaper/issues/82)
- Bound for memory usage [\#81](https://github.com/codelucas/newspaper/issues/81)
- Hosted demo [\#80](https://github.com/codelucas/newspaper/issues/80)
- Having issues installing due to lxml [\#79](https://github.com/codelucas/newspaper/issues/79)
- Add a BeautifulSoup4 parser. [\#44](https://github.com/codelucas/newspaper/issues/44)
- python 3 support request [\#36](https://github.com/codelucas/newspaper/issues/36)

**Merged pull requests:**

- update jieba to 0.35 [\#94](https://github.com/codelucas/newspaper/pull/94) ([WingGao](https://github.com/WingGao))
- Parse was breaking in the method clean\_article\_html when keep\_article\_ht... [\#88](https://github.com/codelucas/newspaper/pull/88) ([phoenixwizard](https://github.com/phoenixwizard))
- split title with \_  [\#87](https://github.com/codelucas/newspaper/pull/87) ([deweydu](https://github.com/deweydu))
- Update to support python3 [\#86](https://github.com/codelucas/newspaper/pull/86) ([log0ymxm](https://github.com/log0ymxm))
- Added link to basic demo [\#83](https://github.com/codelucas/newspaper/pull/83) ([iwasrobbed](https://github.com/iwasrobbed))
- Add splitting of slash-separated titles [\#75](https://github.com/codelucas/newspaper/pull/75) ([igor-shevchenko](https://github.com/igor-shevchenko))

## [0.0.8](https://github.com/codelucas/newspaper/tree/0.0.8) (2014-10-13)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.0.7...0.0.8)

**Closed issues:**

- Parsing Raw HTML [\#74](https://github.com/codelucas/newspaper/issues/74)
- Can't install newspaper [\#72](https://github.com/codelucas/newspaper/issues/72)
- Refactor codebase so newspaper is actually pythonic [\#70](https://github.com/codelucas/newspaper/issues/70)
- Article.top\_node == Article.clean\_top\_node [\#65](https://github.com/codelucas/newspaper/issues/65)
- article.movies missing 'http:' [\#64](https://github.com/codelucas/newspaper/issues/64)
- KeyError when calling newspaper.languages\(\) [\#62](https://github.com/codelucas/newspaper/issues/62)
- Memoize Articles - Not Printing [\#61](https://github.com/codelucas/newspaper/issues/61)
- Add URL headers while building a "paper" [\#60](https://github.com/codelucas/newspaper/issues/60)
- AttributeError: 'module' object has no attribute 'build' [\#59](https://github.com/codelucas/newspaper/issues/59)
- Typo in newspaper.build argument "memoize\_articles" [\#58](https://github.com/codelucas/newspaper/issues/58)
- issue with stopwords-tr.txt [\#51](https://github.com/codelucas/newspaper/issues/51)
- Other language support.  [\#34](https://github.com/codelucas/newspaper/issues/34)
- Character encoding detection [\#2](https://github.com/codelucas/newspaper/issues/2)

**Merged pull requests:**

- Huge refactor: entire codebase in PEP8, imports alphabetized, bugfixes, core changes [\#71](https://github.com/codelucas/newspaper/pull/71) ([codelucas](https://github.com/codelucas))
- Meta tag extraction fixes [\#69](https://github.com/codelucas/newspaper/pull/69) ([karls](https://github.com/karls))
- Test suite improvements [\#68](https://github.com/codelucas/newspaper/pull/68) ([karls](https://github.com/karls))
- Test suite fixes [\#67](https://github.com/codelucas/newspaper/pull/67) ([karls](https://github.com/karls))
- Revert "Added published date to the extractor+article" [\#66](https://github.com/codelucas/newspaper/pull/66) ([codelucas](https://github.com/codelucas))
- Added published date to the extractor+article [\#63](https://github.com/codelucas/newspaper/pull/63) ([parhammmm](https://github.com/parhammmm))

## [0.0.7](https://github.com/codelucas/newspaper/tree/0.0.7) (2014-06-17)
[Full Changelog](https://github.com/codelucas/newspaper/compare/0.0.6...0.0.7)

**Closed issues:**

- no document on how to add language [\#57](https://github.com/codelucas/newspaper/issues/57)
- Retain \<a\> tags in top article node? [\#56](https://github.com/codelucas/newspaper/issues/56)
- DocumentCleaner is missing clean\_body\_classes [\#55](https://github.com/codelucas/newspaper/issues/55)
- You must download and parse an article before parsing it [\#52](https://github.com/codelucas/newspaper/issues/52)
- Not extracting UL LI text [\#50](https://github.com/codelucas/newspaper/issues/50)
- article does not release\_resources\(\) [\#42](https://github.com/codelucas/newspaper/issues/42)
- Doesn't work on http://www.le360.ma/fr [\#40](https://github.com/codelucas/newspaper/issues/40)
- How to assign html content without downloading it? [\#37](https://github.com/codelucas/newspaper/issues/37)
- Python venv only? [\#32](https://github.com/codelucas/newspaper/issues/32)
- .nlp\(\) could not work [\#27](https://github.com/codelucas/newspaper/issues/27)
- Doesn't work with Arabic news sites [\#23](https://github.com/codelucas/newspaper/issues/23)
- SyntaxError: invalid syntax [\#19](https://github.com/codelucas/newspaper/issues/19)
- Retain HTML markup for extracted article [\#18](https://github.com/codelucas/newspaper/issues/18)
- Portuguese is misspelled [\#14](https://github.com/codelucas/newspaper/issues/14)
- Multi-threading article downloads not working [\#12](https://git
... [TRUNCATED]
```

### File: download_corpora.py
```py
# -*- coding: utf-8 -*-
"""
Downloads the necessary NLTK models and corpora required to support
all of newspaper's features. Modify for your own needs.
"""
import nltk

REQUIRED_CORPORA = [
    'brown',  # Required for FastNPExtractor
    'punkt',  # Required for WordTokenizer
    'maxent_treebank_pos_tagger',  # Required for NLTKTagger
    'movie_reviews',  # Required for NaiveBayesAnalyzer
    'wordnet',  # Required for lemmatization and Wordnet
    'stopwords'
]

def main():
    for each in REQUIRED_CORPORA:
        print(('Downloading "{0}"'.format(each)))
        nltk.download(each)
    print("Finished.")

if __name__ == '__main__':
    main()

```

### File: GOOSE-LICENSE.txt
```txt

                              Apache License
                        Version 2.0, January 2004
                     http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

   "License" shall mean the terms and conditions for use, reproduction,
   and distribution as defined by Sections 1 through 9 of this document.

   "Licensor" shall mean the copyright owner or entity authorized by
   the copyright owner that is granting the License.

   "Legal Entity" shall mean the union of the acting entity and all
   other entities that control, are controlled by, or are under common
   control with that entity. For the purposes of this definition,
   "control" means (i) the power, direct or indirect, to cause the
   direction or management of such entity, whether by contract or
   otherwise, or (ii) ownership of fifty percent (50%) or more of the
   outstanding shares, or (iii) beneficial ownership of such entity.

   "You" (or "Your") shall mean an individual or Legal Entity
   exercising permissions granted by this License.

   "Source" form shall mean the preferred form for making modifications,
   including but not limited to software source code, documentation
   source, and configuration files.

   "Object" form shall mean any form resulting from mechanical
   transformation or translation of a Source form, including but
   not limited to compiled object code, generated documentation,
   and conversions to other media types.

   "Work" shall mean the work of authorship, whether in Source or
   Object form, made available under the License, as indicated by a
   copyright notice that is included in or attached to the work
   (an example is provided in the Appendix below).

   "Derivative Works" shall mean any work, whether in Source or Object
   form, that is based on (or derived from) the Work and for which the
   editorial revisions, annotations, elaborations, or other modifications
   represent, as a whole, an original work of authorship. For the purposes
   of this License, Derivative Works shall not include works that remain
   separable from, or merely link (or bind by name) to the interfaces of,
   the Work and Derivative Works thereof.

   "Contribution" shall mean any work of authorship, including
   the original version of the Work and any modifications or additions
   to that Work or Derivative Works thereof, that is intentionally
   submitted to Licensor for inclusion in the Work by the copyright owner
   or by an individual or Legal Entity authorized to submit on behalf of
   the copyright owner. For the purposes of this definition, "submitted"
   means any form of electronic, verbal, or written communication sent
   to the Licensor or its representatives, including but not limited to
   communication on electronic mailing lists, source code control systems,
   and issue tracking systems that are managed by, or on behalf of, the
   Licensor for the purpose of discussing and improving the Work, but
   excluding communication that is conspicuously marked or otherwise
   designated in writing by the copyright owner as "Not a Contribution."

   "Contributor" shall mean Licensor and any individual or Legal Entity
   on behalf of whom a Contribution has been received by Licensor and
   subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of
   this License, each Contributor hereby grants to You a perpetual,
   worldwide, non-exclusive, no-charge, royalty-free, irrevocable
   copyright license to reproduce, prepare Derivative Works of,
   publicly display, publicly perform, sublicense, and distribute the
   Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of
   this License, each Contributor hereby grants to You a perpetual,
   worldwide, non-exclusive, no-charge, royalty-free, irrevocable
   (except as stated in this section) patent license to make, have made,
   use, offer to sell, sell, import, and otherwise transfer the Work,
   where such license applies only to those patent claims licensable
   by such Contributor that are necessarily infringed by their
   Contribution(s) alone or by combination of their Contribution(s)
   with the Work to which such Contribution(s) was submitted. If You
   institute patent litigation against any entity (including a
   cross-claim or counterclaim in a lawsuit) alleging that the Work
   or a Contribution incorporated within the Work constitutes direct
   or contributory patent infringement, then any patent licenses
   granted to You under this License for that Work shall terminate
   as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the
   Work or Derivative Works thereof in any medium, with or without
   modifications, and in Source or Object form, provided that You
   meet the following conditions:

   (a) You must give any other recipients of the Work or
       Derivative Works a copy of this License; and

   (b) You must cause any modified files to carry prominent notices
       stating that You changed the files; and

   (c) You must retain, in the Source form of any Derivative Works
       that You distribute, all copyright, patent, trademark, and
       attribution notices from the Source form of the Work,
       excluding those notices that do not pertain to any part of
       the Derivative Works; and

   (d) If the Work includes a "NOTICE" text file as part of its
       distribution, then any Derivative Works that You distribute must
       include a readable copy of the attribution notices contained
       within such NOTICE file, excluding those notices that do not
       pertain to any part of the Derivative Works, in at least one
       of the following places: within a NOTICE text file distributed
       as part of the Derivative Works; within the Source form or
       documentation, if provided along with the Derivative Works; or,
       within a display generated by the Derivative Works, if and
       wherever such third-party notices normally appear. The contents
       of the NOTICE file are for informational purposes only and
       do not modify the License. You may add Your own attribution
       notices within Derivative Works that You distribute, alongside
       or as an addendum to the NOTICE text from the Work, provided
       that such additional attribution notices cannot be construed
       as modifying the License.

   You may add Your own copyright statement to Your modifications and
   may provide additional or different license terms and conditions
   for use, reproduction, or distribution of Your modifications, or
   for any such Derivative Works as a whole, provided Your use,
   reproduction, and distribution of the Work otherwise complies with
   the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise,
   any Contribution intentionally submitted for inclusion in the Work
   by You to the Licensor shall be under the terms and conditions of
   this License, without any additional terms or conditions.
   Notwithstanding the above, nothing herein shall supersede or modify
   the terms of any separate license agreement you may have executed
   with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade
   names, trademarks, service marks, or product names of the Licensor,
   except as required for reasonable and customary use in describing the
   origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or
   agreed to in writing, Licensor provides the Work (and each
   Contributor provides its Contributions) on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
   implied, including, without limitation, any warranties or conditions
   of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
   PARTICULAR PURPOSE. You are solely responsible for determining the
   appropriateness of using or redistributing the Work and assume any
   risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory,
   whether in tort (including negligence), contract, or otherwise,
   unless required by applicable law (such as deliberate and grossly
   negligent acts) or agreed to in writing, shall any Contributor be
   liable to You for damages, including any direct, indirect, special,
   incidental, or consequential damages of any character arising as a
   result of this License or out of the use or inability to use the
   Work (including but not limited to damages for loss of goodwill,
   work stoppage, computer failure or malfunction, or any and all
   other commercial damages or losses), even if such Contributor
   has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing
   the Work or Derivative Works thereof, You may choose to offer,
   and charge a fee for, acceptance of support, warranty, indemnity,
   or other liability obligations and/or rights consistent with this
   License. However, in accepting such obligations, You may act only
   on Your own behalf and on Your sole responsibility, not on behalf
   of any other Contributor, and only if You agree to indemnify,
   defend, and hold each Contributor harmless for any liability
   incurred by, or claims asserted against, such Contributor by reason
   of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

APPENDIX: How to apply the Apache License to your work.

   To apply the Apache License to your work, attach the following
   boilerplate notice, with the fields enclosed by brackets "[]"
   replaced with your own identifying information. (Don't include
   the brackets!)  The text should be enclosed in the appropriate
   comment syntax for the file format. We also recommend that a
   file or class name and description of purpose be included on the
   same "printed page" as the copyright notice for easier
   identification within third-party archives.

Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

### File: docs\conf.py
```py
# -*- coding: utf-8 -*-
#
# newspaper documentation build configuration file, created by
# sphinx-quickstart on Sat Dec 21 22:26:51 2013.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

sys.path.append(os.path.abspath('_themes'))


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'newspaper'
copyright = '2013, <a href="http://codelucas.com">Lucas Ou-Yang</a>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.2'
# The full version, including alpha/beta/rc tags.
release = '0.0.2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

html_theme = 'kr'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index':    ['sidebarintro.html', 'sourcelink.html', 'searchbox.html'],
    '**':       ['sidebarlogo.html', 'localtoc.html', 'relations.html',
                 'sourcelink.html', 'searchbox.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'newspaperdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'newspaper.tex', 'newspaper Documentation',
   'Lucas Ou-Yang', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'newspaper', 'newspaper Documentation',
     ['Lucas Ou-Yang'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'newspaper', 'newspaper Documentation',
   'Lucas Ou-Yang', 'newspaper', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

```

### File: tests\benchmarks.py
```py
# -*- coding: utf-8 -*-
"""
Async IO vs multi-threading

Multi-thread:           5.9 secs (10 threads) for 100 requests
Async-IO with Gevent:   10.5 secs  for 100 requests
Single thread:          86.0 secs for 100 requests
"""
import sys
import logging
import queue
import os

from threading import activeCount
from threading import Thread
from http.cookiejar import CookieJar as cj
from .unit_tests import read_urls

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
log = logging.getLogger(__name__)

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PARENT_DIR, '..'))

from newspaper.network import multithread_request, sync_request
from newspaper.utils import print_duration


@print_duration
def naive_run(urls):
    """no multithreading or async io
    """
    resps = []
    for url in urls:
        resps.append(sync_request(url))
    print(resps)


@print_duration
def mthread_run(urls):
    """download a bunch of urls via multithreading
    """
    reqs = multithread_request(urls)
    resps = [req.resp for req in reqs]


@print_duration
def asyncio_run(urls):
    """download a bunch of urls via async io
    """
    pass
    # rs = (grequests.request('GET', u, **req_kwargs) for u in urls)
    # responses = async_request(urls)
    # print(responses)


def benchmark():
    """multi-threading vs async-io vs regular
    """
    urls = read_urls(amount=1000)
    # naive_run(urls)
    mthread_run(urls)
    # asyncio_run(urls)


if __name__ == '__main__':
    benchmark()

```

### File: tests\unit_tests.py
```py
# -*- coding: utf-8 -*-
"""
All unit tests for the newspaper library should be contained in this file.
"""
import sys
import os
import unittest
import time
import traceback
import re
from collections import defaultdict, OrderedDict
import concurrent.futures

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')

# newspaper's unit tests are in their own separate module, so
# insert the parent directory manually to gain scope of the
# core module
sys.path.insert(0, PARENT_DIR)

TEXT_FN = os.path.join(TEST_DIR, 'data', 'text')
HTML_FN = os.path.join(TEST_DIR, 'data', 'html')
URLS_FILE = os.path.join(TEST_DIR, 'data', 'fulltext_url_list.txt')

import newspaper
from newspaper import Article, fulltext, Source, ArticleException, news_pool
from newspaper.article import ArticleDownloadState
from newspaper.configuration import Configuration
from newspaper.urls import get_domain


def print_test(method):
    """
    Utility method for print verbalizing test suite, prints out
    time taken for test and functions name, and status
    """

    def run(*args, **kw):
        ts = time.time()
        print('\ttesting function %r' % method.__name__)
        method(*args, **kw)
        te = time.time()
        print('\t[OK] in %r %2.2f sec' % (method.__name__, te - ts))

    return run


def mock_resource_with(filename, resource_type):
    """
    Mocks an HTTP request by pulling text from a pre-downloaded file
    """
    VALID_RESOURCES = ['html', 'txt']
    if resource_type not in VALID_RESOURCES:
        raise Exception('Mocked resource must be one of: %s' %
                        ', '.join(VALID_RESOURCES))
    subfolder = 'text' if resource_type == 'txt' else 'html'
    resource_path = os.path.join(TEST_DIR, "data/%s/%s.%s" %
                                 (subfolder, filename, resource_type))
    with open(resource_path, 'r', encoding='utf-8') as f:
        return f.read()


def get_base_domain(url):
    """
    For example, the base url of uk.reuters.com => reuters.com
    """
    domain = get_domain(url)
    tld = '.'.join(domain.split('.')[-2:])
    if tld in ['co.uk', 'com.au', 'au.com']:  # edge cases
        end_chunks = domain.split('.')[-3:]
    else:
        end_chunks = domain.split('.')[-2:]
    base_domain = '.'.join(end_chunks)
    return base_domain


def check_url(*args, **kwargs):
    return ExhaustiveFullTextCase.check_url(*args, **kwargs)


@unittest.skipIf('fulltext' not in sys.argv, 'Skipping fulltext tests')
class ExhaustiveFullTextCase(unittest.TestCase):
    @staticmethod
    def check_url(args):
        """
        :param (basestr, basestr) url, res_filename:
        :return: (pubdate_failed, fulltext_failed)
        """
        url, res_filename = args
        pubdate_failed, fulltext_failed = False, False
        html = mock_resource_with(res_filename, 'html')
        try:
            a = Article(url)
            a.download(html)
            a.parse()
            if a.publish_date is None:
                pubdate_failed = True
        except Exception:
            print('<< URL: %s parse ERROR >>' % url)
            traceback.print_exc()
            pubdate_failed, fulltext_failed = True, True
        else:
            correct_text = mock_resource_with(res_filename, 'txt')
            if not (a.text == correct_text):
                # print('Diff: ', simplediff.diff(correct_text, a.text))
                # `correct_text` holds the reason of failure if failure
                print('%s -- %s -- %s' %
                      ('Fulltext failed',
                       res_filename, correct_text.strip()))
                fulltext_failed = True
                # TODO: assert statements are commented out for full-text
                # extraction tests because we are constantly tweaking the
                # algorithm and improving
                # assert a.text == correct_text
        return pubdate_failed, fulltext_failed

    @print_test
    def test_exhaustive(self):
        with open(URLS_FILE, 'r') as f:
            urls = [d.strip() for d in f.readlines() if d.strip()]

        domain_counters = {}

        def get_filename(url):
            domain = get_base_domain(url)
            domain_counters[domain] = domain_counters.get(domain, 0) + 1
            return '{}{}'.format(domain, domain_counters[domain])

        filenames = map(get_filename, urls)

        with concurrent.futures.ProcessPoolExecutor() as executor:
            test_results = list(executor.map(check_url, zip(urls, filenames)))

        total_pubdates_failed, total_fulltext_failed = \
            list(map(sum, zip(*test_results)))

        print('%s fulltext extractions failed out of %s' %
              (total_fulltext_failed, len(urls)))
        print('%s pubdate extractions failed out of %s' %
              (total_pubdates_failed, len(urls)))
        self.assertGreaterEqual(47, total_pubdates_failed)
        self.assertGreaterEqual(20, total_fulltext_failed)


class ArticleTestCase(unittest.TestCase):
    def setup_stage(self, stage_name):
        stages = OrderedDict([
            ('initial', lambda: None),
            ('download', lambda: self.article.download(
                mock_resource_with('cnn_article', 'html'))),
            ('parse', lambda: self.article.parse()),
            ('meta', lambda: None),  # Alias for nlp
            ('nlp', lambda: self.article.nlp())
        ])
        assert stage_name in stages
        for name, action in stages.items():
            if name == stage_name:
                break
            action()

    def setUp(self):
        """Called before the first test case of this unit begins
        """
        self.article = Article(
            url='http://www.cnn.com/2013/11/27/travel/weather-'
                'thanksgiving/index.html?iref=allsearch')

    @print_test
    def test_url(self):
        self.assertEqual(
            'http://www.cnn.com/2013/11/27/travel/weather-'
            'thanksgiving/index.html?iref=allsearch',
            self.article.url)

    @print_test
    def test_download_html(self):
        self.setup_stage('download')
        html = mock_resource_with('cnn_article', 'html')
        self.article.download(html)
        self.assertEqual(self.article.download_state, ArticleDownloadState.SUCCESS)
        self.assertEqual(self.article.download_exception_msg, None)
        self.assertEqual(75406, len(self.article.html))

    @print_test
    def test_meta_refresh_redirect(self):
        # TODO: We actually hit example.com in this unit test ... which is bad
        # Figure out how to mock an actual redirect
        config = Configuration()
        config.follow_meta_refresh = True
        article = Article(
            '', config=config)
        html = mock_resource_with('google_meta_refresh', 'html')
        article.download(input_html=html)
        article.parse()
        self.assertEqual(article.title, 'Example Domain')

    @print_test
    def test_meta_refresh_no_url_redirect(self):
        config = Configuration()
        config.follow_meta_refresh = True
        article = Article(
            '', config=config)
        html = mock_resource_with('ap_meta_refresh', 'html')
        article.download(input_html=html)
        article.parse()
        self.assertEqual(article.title, 'News from The Associated Press')

    @print_test
    def test_pre_download_parse(self):
        """Calling `parse()` before `download()` should yield an error
        """
        article = Article(self.article.url)
        self.assertRaises(ArticleException, article.parse)

    @print_test
    def test_parse_html(self):
        self.setup_stage('parse')

        AUTHORS = ['Chien-Ming Wang', 'Dana A. Ford', 'James S.A. Corey',
                   'Tom Watkins']
        TITLE = 'After storm, forecasters see smooth sailing for Thanksgiving'
        LEN_IMGS = 46
        META_LANG = 'en'
        META_SITE_NAME = 'CNN'

        self.article.parse()
        self.article.nlp()

        text = mock_resource_with('cnn', 'txt')
        self.assertEqual(text, self.article.text)
        self.assertEqual(text, fulltext(self.article.html))

        # NOTE: top_img extraction requires an internet connection
        # unlike the rest of this test file
        TOP_IMG = ('http://i2.cdn.turner.com/cnn/dam/assets/131129200805-'
                   '01-weather-1128-story-top.jpg')
        self.assertEqual(TOP_IMG, self.article.top_img)

        self.assertCountEqual(AUTHORS, self.article.authors)
        self.assertEqual(TITLE, self.article.title)
        self.assertEqual(LEN_IMGS, len(self.article.imgs))
        self.assertEqual(META_LANG, self.article.meta_lang)
        self.assertEqual(META_SITE_NAME, self.article.meta_site_name)
        self.assertEqual('2013-11-27 00:00:00', str(self.article.publish_date))

    @print_test
    def test_meta_type_extraction(self):
        self.setup_stage('meta')
        meta_type = self.article.extractor.get_meta_type(
            self.article.clean_doc)
        self.assertEqual('article', meta_type)

    @print_test
    def test_meta_extraction(self):
        self.setup_stage('meta')
        meta = self.article.extractor.get_meta_data(self.article.clean_doc)
        META_DATA = defaultdict(dict, {
            'medium': 'news',
            'googlebot': 'noarchive',
            'pubdate': '2013-11-27T08:36:32Z',
            'title': 'After storm, forecasters see smooth sailing for Thanksgiving - CNN.com',
            'og': {'site_name': 'CNN',
                   'description': 'A strong storm struck much of the eastern United States on Wednesday, complicating holiday plans for many of the 43 million Americans expected to travel.',
                   'title': 'After storm, forecasters see smooth sailing for Thanksgiving',
                   'url': 'http://www.cnn.com/2013/11/27/travel/weather-thanksgiving/index.html',
                   'image': 'http://i2.cdn.turner.com/cnn/dam/assets/131129200805-01-weather-1128-story-top.jpg',
                   'type': 'article'},
            'section': 'travel',
            'author': 'Dana A. Ford, James S.A. Corey, Chien-Ming Wang, and Tom Watkins, CNN',
            'robots': 'index,follow',
            'vr': {
                'canonical': 'http://edition.cnn.com/2013/11/27/travel/weather-thanksgiving/index.html'},
            'source': 'CNN',
            'fb': {'page_id': 18793419640, 'app_id': 80401312489},
            'keywords': 'winter storm,holiday travel,Thanksgiving storm,Thanksgiving winter storm',
            'article': {
                'publisher': 'https://www.facebook.com/cnninternational'},
            'lastmod': '2013-11-28T02:03:23Z',
            'twitter': {'site': {'identifier': '@CNNI', 'id': 2097571},
                        'card': 'summary',
                        'creator': {'identifier': '@cnntravel',
                                    'id': 174377718}},
            'viewport': 'width=1024',
            'news_keywords': 'winter storm,holiday travel,Thanksgiving storm,Thanksgiving winter storm'
        })

        self.assertDictEqual(META_DATA, meta)

        # if the value for a meta key is another dict, that dict ought to be
        # filled with keys and values
        dict_values = [v for v in list(meta.values()) if isinstance(v, dict)]
        self.assertTrue(all([len(d) > 0 for d in dict_values]))

        # there are exactly 5 top-level "og:type" type keys
        is_dict = lambda v: isinstance(v, dict)
        self.assertEqual(5, len([i for i in meta.values() if is_dict(i)]))

        # there are exactly 12 top-level "pubdate" type keys
        is_string = lambda v: isinstance(v, str)
        self.assertEqual(12, len([i for i in meta.values() if is_string(i)]))

    @print_test
    def test_pre_download_nlp(self):
        """Test running NLP algos before even downloading the article
        """
        self.setup_stage('initial')
        new_article = Article(self.article.url)
        self.assertRaises(ArticleException, new_article.nlp)

    @print_test
    def test_pre_parse_nlp(self):
        """Test running NLP algos before parsing the article
        """
        self.setup_stage('parse')
        self.assertRaises(ArticleException, self.article.nlp)

    @print_test
    def test_nlp_body(self):
        self.setup_stage('nlp')
        self.article.nlp()
        KEYWORDS = ['balloons', 'delays', 'flight', 'forecasters',
                    'good', 'sailing', 'smooth', 'storm', 'thanksgiving',
                    'travel', 'weather', 'winds', 'york']
        SUMMARY = mock_resource_with('cnn_summary', 'txt')
        self.assertEqual(SUMMARY, self.article.summary)
        self.assertCountEqual(KEYWORDS, self.article.keywords)


class TestDownloadScheme(unittest.TestCase):
    @print_test
    def test_download_file_success(self):
        url = "file://" + os.path.join(HTML_FN, "cnn_article.html")
        article = Article(url=url)
        article.download()
        self.assertEqual(article.download_state, ArticleDownloadState.SUCCESS)
        self.assertEqual(article.download_exception_msg, None)
        self.assertEqual(75406, len(article.html))

    @print_test
    def test_download_file_failure(self):
        url = "file://" + os.path.join(HTML_FN, "does_not_exist.html")
        article = Article(url=url)
        article.download()
        self.assertEqual(0, len(article.html))
        self.assertEqual(article.download_state, ArticleDownloadState.FAILED_RESPONSE)
        self.assertEqual(article.download_exception_msg, "No such file or directory")


class ContentExtractorTestCase(unittest.TestCase):
    """Test specific element extraction cases"""

    def setUp(self):
        self.extractor = newspaper.extractors.ContentExtractor(Configuration())
        self.parser = newspaper.parsers.Parser

    def _get_title(self, html):
        doc = self.parser.fromstring(html)
        return self.extractor.get_title(doc)

    def test_get_title_basic(self):
        html = '<title>Test title</title>'
        self.assertEqual(self._get_title(html), 'Test title')

    def test_get_title_split(self):
        html = '<title>Test page » Test title</title>'
        self.assertEqual(self._get_title(html), 'Test title')

    def test_get_title_split_escaped(self):
        html = '<title>Test page &raquo; Test title</title>'
        self.assertEqual(self._get_title(html), 'Test title')

    def test_get_title_quotes(self):
        title = 'Test page and «something in quotes»'
        html = '<title>{}</title>'.format(title)
        self.assertEqual(self._get_title(html), title)

    def _get_canonical_link(self, article_url, html):
        doc = self.parser.fromstring(html)
        return self.extractor.get_canonical_link(article_url, doc)

    def test_get_canonical_link_rel_canonical(self):
        url = 'http://www.example.com/article.html'
        html = '<link rel="canonical" href="{}">'.format(url)
        self.assertEqual(self._get_canonical_link('', html), url)

    d
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
