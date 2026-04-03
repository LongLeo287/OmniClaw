---
id: github.com-antlr-antlr4-tools-98133f3c-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:32.428973
---

# KNOWLEDGE EXTRACT: github.com_antlr_antlr4-tools_98133f3c
> **Extracted on:** 2026-04-01 13:47:31
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522630/github.com_antlr_antlr4-tools_98133f3c

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2022 Antlr Project

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
# antlr4-tools

Tools to run antlr4 w/o needing to install java or antlr4! The only requirement is Python3, which is typically installed on all developer machines on all operating systems. 
 
## Install

```bash
$ pip install antlr4-tools
```

That creates `antlr4` and `antlr4-parse` executables. On Windows, of course, this doesn't just work. You need to add the `...\local-packages\python38\scripts` dir to your `PATH`, which itself might require a fun reboot or perhaps reinstall of the OS. haha.

### Windows-specific issues

On Windows, the `pip` command doesn't just work---you need to add the `...\local-packages\python38\scripts` dir to your `PATH`, which itself might require a fun reboot.  If you use WSL on Windows, then the pip install will also properly at the scripts directly (if you run from bash shell).


1. Go to the Microsoft Store
2. Search in Microsoft Store for Python
3. Select the newest version of Python (3.10).
4. Click the "Get" button. Store installs python and pip at "c:\Users...\AppData\Local\Microsoft\WindowsApps\python.exe" and "c:\Users...\AppData\Local\Microsoft\WindowsApps\pip.exe", respectively. And, it updates the search path immediately with the install.
5. Open a "cmd" terminal.
6. You can now type "python" and "pip", and "pip install antlr4-tools". 7. Unfortunately, it does not add that to the search path.
7. Update the search path to contain `c:\Users...\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p8\LocalCache\local-packages\Python310\Scripts`. You may need to install MSYS2, then do a `find /c/ -name antlr4.exe 2> /dev/null` and enter that path.
8. Or, you can set up an alias to antlr4.exe on that path.

The good news is that the ANTLR4 Python tool downloads the ANTLR jar in a standard location, and you don't need to do that manually. It's also possible to go in a browser, go to python.org, and download the python package. But, it's likely you will need to update the path for antlr4.exe as before.

## First run will install Java and ANTLR

If needed, `antlr4` will download and install Java 11 and the latest ANTLR jar:

```bash
$ antlr4 
Downloading antlr4-4.11.1-complete.jar
ANTLR tool needs Java to run; install Java JRE 11 yes/no (default yes)? y
Installed Java in /Users/parrt/.jre/jdk-11.0.15+10-jre; remove that dir to uninstall
ANTLR Parser Generator  Version 4.11.1
 -o ___              specify output directory where all output is generated
 -lib ___            specify location of grammars, tokens files
...
```

To override the version of ANTLR jar used, you can pass a `-v <version>` argument or set `ANTLR4_TOOLS_ANTLR_VERSION` environment variable:

```bash
$ antlr4 -v 4.9.3
ANTLR Parser Generator  Version 4.9.3
 -o ___              specify output directory where all output is generated
 -lib ___            specify location of grammars, tokens files
...
$ ANTLR4_TOOLS_ANTLR_VERSION=4.10.1 antlr4
ANTLR Parser Generator  Version 4.10.1
 -o ___              specify output directory where all output is generated
 -lib ___            specify location of grammars, tokens files
...
```

## Running ANTLR tool on grammars

The `antlr4` command forwards all arguments (besides `-v` mentioned above) to the actual ANTLR tool command:

```bash
$ antlr4 JSON.g4 
$ ls JSON*.java
JSONBaseListener.java  JSONLexer.java         JSONListener.java      JSONParser.java
$ antlr4 -Dlanguage=Python3 -visitor JSON.g4
$ ls JSON*.py
JSONLexer.py     JSONListener.py  JSONParser.py    JSONVisitor.py
```

## Parsing using interpreter

The `antlr4-parse` command requires ANTLR 4.11 and above (but any version of ANTLR works for the plain `antlr4` command).  It accepts the same `-v` argument or environment variable to override the ANTLR jar version used.  (Note: `^D` means control-D and indicates "end of input" on Unix but use `^Z` on Windows.)

Let's play with a simple grammar:

```
grammar Expr;
prog:	expr EOF ;
expr:	expr ('*'|'/') expr
    |	expr ('+'|'-') expr
    |	INT
    |	'(' expr ')'
    ;
NEWLINE : [\r\n]+ -> skip;
INT     : [0-9]+ ;
```

To parse and get the parse tree in text form, use:

```bash
$ antlr4-parse Expr.g4 prog -tree
10+20*30
^D
(prog:1 (expr:2 (expr:3 10) + (expr:1 (expr:3 20) * (expr:3 30))) <EOF>)
```

Here's how to get the tokens and trace through the parse:

```bash
$ antlr4-parse Expr.g4 prog -tokens -trace
10+20*30
[@0,0:1='10',<INT>,1:0]
[@1,2:2='+',<'+'>,1:2]
[@2,3:4='20',<INT>,1:3]
[@3,5:5='*',<'*'>,1:5]
[@4,6:7='30',<INT>,1:6]
[@5,9:8='<EOF>',<EOF>,2:0]
enter   prog, LT(1)=10
enter   expr, LT(1)=10
consume [@0,0:1='10',<8>,1:0] rule expr
enter   expr, LT(1)=+
consume [@1,2:2='+',<3>,1:2] rule expr
enter   expr, LT(1)=20
consume [@2,3:4='20',<8>,1:3] rule expr
enter   expr, LT(1)=*
consume [@3,5:5='*',<1>,1:5] rule expr
enter   expr, LT(1)=30
consume [@4,6:7='30',<8>,1:6] rule expr
exit    expr, LT(1)=<EOF>
exit    expr, LT(1)=<EOF>
exit    expr, LT(1)=<EOF>
consume [@5,9:8='<EOF>',<-1>,2:0] rule prog
exit    prog, LT(1)=<EOF>
```

Here's how to get a visual tree view:

```bash
$ antlr4-parse Expr.g4 prog -gui
10+20*30
```

The following will pop up in a Java-based GUI window:

<img src="images/parse-tree.png" width="300">

On real grammars, it can be useful to get decision-making profiling info:

```bash
$ antlr4-parse JavaLexer.g4 JavaParser.g4 compilationUnit -profile dump.csv T.java
$ open /tmp/dump.csv 
$ head -5 /tmp/dump.csv 
Rule,Invocations,Time (ms),Total k,Max k,Ambiguities,DFA cache miss
compilationUnit:0,1,0.164791,1,1,0,1
compilationUnit:1,42,1.106583,42,1,0,2
compilationUnit:2,2,1.73675,2,1,0,2
compilationUnit:3,1,3.969,1,1,0,1
```

```

## File: `antlr4_tool_runner.py`
```python
import argparse
import os
import sys
import re
import subprocess
from shutil import which
from pathlib import Path
from urllib.request import urlopen
from urllib import error
import json

import jdk  # requires install-jdk package

mvn_repo: str
homedir: Path


def initialize_paths():
    global mvn_repo, homedir
    homedir = Path.home()
    mvn_repo = os.path.join(homedir, '.m2', 'repository', 'org', 'antlr', 'antlr4')


def latest_version():
    try:
        with urlopen("https://central.sonatype.com/solrsearch/select?q=a:antlr4-master+g:org.antlr",
                     timeout=10) as response:
            s = response.read().decode("UTF-8")
            searchResult = json.loads(s)['response']
            # searchResult = s.json()['response']
            antlr_info = searchResult['docs'][0]
            # print(json.dump(searchResult))
            latest = antlr_info['latestVersion']
            return latest
    except (error.URLError, error.HTTPError, TimeoutError):
        print("Could not get latest version number, attempting to fall back to latest downloaded version...")
        version_dirs = list(filter(lambda directory: re.match(r"[0-9]+\.[0-9]+\.[0-9]+", directory), os.listdir(mvn_repo)))
        version_dirs.sort(reverse=True)
        if len(version_dirs) == 0:
            raise FileNotFoundError("Could not find a previously downloaded antlr4 jar")
        else:
            latest_version_dir = version_dirs.pop()
            print(f"Found version '{latest_version_dir}', this version may be out of date")
            return latest_version_dir


def antlr4_jar(version):
    jar = os.path.join(mvn_repo, version, f'antlr4-{version}-complete.jar')
    if not os.path.exists(jar):
        return download_antlr4(jar, version)
    return jar


def download_antlr4(jar, version):
    s = None
    try:
        with urlopen(f"https://repo1.maven.org/maven2/org/antlr/antlr4/{version}/antlr4-{version}-complete.jar",
                     timeout=60) as response:
            print(f"Downloading antlr4-{version}-complete.jar")
            os.makedirs(os.path.join(mvn_repo, version), exist_ok=True)
            s = response.read()
    except (error.URLError, error.HTTPError, TimeoutError):
        print(f"Could not find antlr4-{version}-complete.jar at maven.org")

    if s is None:
        return None
    with open(jar, "wb") as f:
        f.write(s)
    return jar


def find_bin_dir(install_dir):
    for root, dirs, files in os.walk(install_dir):
        if root.endswith("bin"):
            return root
    return None


def install_jre(java_version='11'):
    USER_DIR = os.path.expanduser("~")
    JRE_DIR = os.path.join(USER_DIR, ".jre")
    if os.path.exists(JRE_DIR):
        for f in os.listdir(JRE_DIR):
            if f.startswith(f"jdk-{java_version}"):
                install_dir = os.path.join(JRE_DIR, f)
                bindir = find_bin_dir(install_dir)
                java = os.path.join(bindir, 'java')
                return java

    r = input(f"ANTLR tool needs Java to run; install Java JRE 11 yes/no (default yes)? ")
    if r.strip().lower() not in {'yes', 'y', ''}:
        exit(1)
    install_dir = jdk.install(java_version, jre=True)
    print(f"Installed Java in {install_dir}; remove that dir to uninstall")
    bindir = find_bin_dir(install_dir)
    if bindir is None:
        print(f"Can't find bin/java in {install_dir}; installation failed")
        return None
    java = os.path.join(bindir, 'java')
    return java


def install_jre_and_antlr(version):
    jar = antlr4_jar(version)
    java = which("java")
    if java is None:
        java = install_jre()
    if jar is None or java is None:
        exit(1)
    CHECK_JRE_VERSION = False
    if CHECK_JRE_VERSION:
        p = subprocess.Popen([java, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode("UTF-8").split('\n')[0]
        print(f"Running {out}")
    return jar, java


def process_args():
    parser = argparse.ArgumentParser(
        add_help=False, usage="%(prog)s [-v VERSION] [%(prog)s options]"
    )
    # Note, that the space after `-v` is needed, so we don't pick up other arguments beginning with `v`, like `-visitor`
    parser.add_argument("-v ", dest="version", default=None)
    args, unparsed_args = parser.parse_known_args()

    return unparsed_args, (
            args.version or os.environ.get("ANTLR4_TOOLS_ANTLR_VERSION") or latest_version()
    )


def run_cli(entrypoint):
    initialize_paths()
    args, version = process_args()
    jar, java = install_jre_and_antlr(version)

    cp = subprocess.run([java, '-cp', jar, entrypoint] + args)
    sys.exit(cp.returncode)


def tool():
    """Entry point to run antlr4 tool itself"""
    run_cli('org.antlr.v4.Tool')


def interp():
    """Entry point to run antlr4 profiling using grammar and input file"""
    run_cli('org.antlr.v4.gui.Interpreter')


if __name__ == '__main__':
    interp()
```

## File: `developer-cert-of-origin.txt`
```
This repo uses the Linux Foundation's Developer
Certificate of Origin, DCO, version 1.1. See either
https://developercertificate.org/ or the text below.

Each commit requires a "signature", which is simple as
using `-s` (not `-S`) to the git commit command: 

git commit -s -m 'This is my commit message'

Github's pull request process enforces the sig and gives
instructions on how to fix any commits that lack the sig.
See https://github.com/apps/dco for more info.

----- https://developercertificate.org/ ------

Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

## File: `setup.py`
```python
from setuptools import setup, find_packages

# To RELEASE:
#
# $ pip install --upgrade build setuptools wheel twine  # update tools
# $ rm -rf dist build *.egg-info
# $ python -m build
# $ twine upload dist/*

v = '0.2.2'

setup(
    name='antlr4-tools',
    version=v,
    py_modules=['antlr4_tool_runner'],
    install_requires=[
        "install-jdk"
    ],
    url='http://www.antlr.org',
    license='MIT',
    author='Terence Parr',
    author_email='parrt@antlr.org',
    entry_points={'console_scripts': [
        'antlr4=antlr4_tool_runner:tool',
        'antlr4-parse=antlr4_tool_runner:interp'
    ]
    },
    description='Tools to run ANTLR4 tool and grammar interpreter/profiler',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Intended Audience :: Developers']
)
```

