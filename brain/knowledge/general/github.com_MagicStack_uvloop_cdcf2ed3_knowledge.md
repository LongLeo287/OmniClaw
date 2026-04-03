---
id: github.com-magicstack-uvloop-cdcf2ed3-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:22.061141
---

# KNOWLEDGE EXTRACT: github.com_MagicStack_uvloop_cdcf2ed3
> **Extracted on:** 2026-04-01 13:00:35
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522200/github.com_MagicStack_uvloop_cdcf2ed3

---

## File: `.editorconfig`
```
root = true

[*]
trim_trailing_whitespace = true
insert_final_newline = true

[Makefile]
indent_style = tab

[*.{py,pyx,pxd,pxi,yml,h}]
indent_size = 4
indent_style = space
```

## File: `.flake8`
```
[flake8]
filename = *.py,*.pyi
ignore = E402,E731,D100,D101,D102,D103,D104,D105,W503,W504,E252
exclude = .git,__pycache__,build,dist,.eggs,postgres,vendor

per-file-ignores =
    *.pyx,*.pxd,*.pxi: E211, E222, E225, E226, E227, E999
    *.pyi: F401, F403, F405, F811, E127, E128, E203, E266, E301, E302, E305, E501, E701, E704, E741, B303, W503, W504
```

## File: `.gitignore`
```
*._*
*.pyc
*.pyo
*.ymlc
*.ymlc~
*.scssc
*.so
*~
.#*
.DS_Store
.project
.pydevproject
.settings
.idea
/.ropeproject
\#*#
/pub
/test*.py
/.local
/perf.data*
/config_local.yml
/build
__pycache__/
.d8_history
/*.egg
/*.egg-info
/dist
/.cache
docs/_build
uvloop/loop.*.pyd
/.pytest_cache/
/.mypy_cache/
/.vscode
/.eggs
/.venv*
/wheelhouse
/uvloop-dev
```

## File: `.gitmodules`
```
[submodule "vendor/libuv"]
	path = vendor/libuv
	url = https://github.com/libuv/libuv.git
```

## File: `LICENSE-APACHE`
```
Copyright (C) 2016-present the uvloop authors and contributors.

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

   Copyright (c) 2015-present MagicStack Inc.  http://magic.io

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

## File: `LICENSE-MIT`
```
The MIT License

Copyright (C) 2016-present the uvloop authors and contributors.

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

## File: `MANIFEST.in`
```
recursive-include docs *.py *.rst
recursive-include examples *.py
recursive-include tests *.py *.pem
recursive-include uvloop *.pyx *.pxd *.pxi *.py *.c *.h *.pyi py.typed
recursive-include vendor/libuv *
recursive-exclude vendor/libuv/.git *
recursive-exclude vendor/libuv/docs *
recursive-exclude vendor/libuv/img *
include LICENSE-MIT LICENSE-APACHE README.rst Makefile performance.png .flake8 mypy.ini
```

## File: `Makefile`
```
.PHONY: _default clean clean-libuv distclean compile debug docs test testinstalled release setup-build ci-clean


PYTHON ?= python
ROOT = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))


_default: compile


clean:
	rm -fr dist/ doc/_build/ *.egg-info uvloop/loop.*.pyd uvloop/loop_d.*.pyd
	rm -fr uvloop/*.c uvloop/*.html uvloop/*.so
	rm -fr uvloop/handles/*.html uvloop/includes/*.html
	find . -name '__pycache__' | xargs rm -rf


ci-clean: clean
	rm -fr build/lib.* build/temp.* build/libuv


clean-libuv:
	(cd vendor/libuv; git clean -dfX)


distclean: clean clean-libuv
	rm -fr build/


setup-build:
	$(PYTHON) setup.py build_ext --inplace --cython-always


compile: clean setup-build


debug: clean
	$(PYTHON) setup.py build_ext --inplace --debug \
		--cython-always \
		--cython-annotate \
		--cython-directives="linetrace=True" \
		--define UVLOOP_DEBUG,CYTHON_TRACE,CYTHON_TRACE_NOGIL


docs:
	$(PYTHON) setup.py build_ext --inplace build_sphinx


test:
	PYTHONASYNCIODEBUG=1 $(PYTHON) -m unittest discover -v tests
	$(PYTHON) -m unittest discover -v tests


testinstalled:
	cd "$${HOME}" && $(PYTHON) -m unittest discover -v $(ROOT)/tests
```

## File: `README.rst`
```
.. image:: https://img.shields.io/github/actions/workflow/status/MagicStack/uvloop/tests.yml?branch=master
    :target: https://github.com/MagicStack/uvloop/actions/workflows/tests.yml?query=branch%3Amaster

.. image:: https://img.shields.io/pypi/v/uvloop.svg
    :target: https://pypi.python.org/pypi/uvloop

.. image:: https://pepy.tech/badge/uvloop
    :target: https://pepy.tech/project/uvloop
    :alt: PyPI - Downloads


uvloop is a fast, drop-in replacement of the built-in asyncio
event loop.  uvloop is implemented in Cython and uses libuv
under the hood.

The project documentation can be found
`here <http://uvloop.readthedocs.org/>`_.  Please also check out the
`wiki <https://github.com/MagicStack/uvloop/wiki>`_.


Performance
-----------

uvloop makes asyncio 2-4x faster.

.. image:: https://raw.githubusercontent.com/MagicStack/uvloop/master/performance.png
    :target: http://magic.io/blog/uvloop-blazing-fast-python-networking/

The above chart shows the performance of an echo server with different
message sizes.  The *sockets* benchmark uses ``loop.sock_recv()`` and
``loop.sock_sendall()`` methods; the *streams* benchmark uses asyncio
high-level streams, created by the ``asyncio.start_server()`` function;
and the *protocol* benchmark uses ``loop.create_server()`` with a simple
echo protocol.  Read more about uvloop in a
`blog post <http://magic.io/blog/uvloop-blazing-fast-python-networking/>`_
about it.


Installation
------------

uvloop requires Python 3.8 or greater and is available on PyPI.
Use pip to install it::

    $ pip install uvloop

Note that it is highly recommended to **upgrade pip before** installing
uvloop with::

    $ pip install -U pip


Using uvloop
------------

As of uvloop 0.18, the preferred way of using it is via the
``uvloop.run()`` helper function:


.. code:: python

    import uvloop

    async def main():
        # Main entry-point.
        ...

    uvloop.run(main())

``uvloop.run()`` works by simply configuring ``asyncio.run()``
to use uvloop, passing all of the arguments to it, such as ``debug``,
e.g. ``uvloop.run(main(), debug=True)``.

With Python 3.11 and earlier the following alternative
snippet can be used:

.. code:: python

    import asyncio
    import sys

    import uvloop

    async def main():
        # Main entry-point.
        ...

    if sys.version_info >= (3, 11):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(main())
    else:
        uvloop.install()
        asyncio.run(main())


Building From Source
--------------------

To build uvloop, you'll need Python 3.8 or greater:

1. Clone the repository:

   .. code::

    $ git clone --recursive git@github.com:MagicStack/uvloop.git
    $ cd uvloop

2. Create a virtual environment and activate it:

   .. code::

    $ python3 -m venv uvloop-dev
    $ source uvloop-dev/bin/activate

3. Install development dependencies:

   ..  code::

    $ pip install -e .[dev]

4. Build and run tests:

   .. code::

    $ make
    $ make test


License
-------

uvloop is dual-licensed under MIT and Apache 2.0 licenses.
```

## File: `mypy.ini`
```
[mypy]
incremental = True
strict = True

[mypy-uvloop._testbase]
ignore_errors = True
```

## File: `pyproject.toml`
```
[project]
name = "uvloop"
description = "Fast implementation of asyncio event loop on top of libuv"
authors = [{name = "Yury Selivanov", email = "yury@magic.io"}]
requires-python = '>=3.8.1'
readme = "README.rst"
license = {text = "MIT License"}
dynamic = ["version"]
keywords = [
    "asyncio",
    "networking",
]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Framework :: AsyncIO",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: System :: Networking",
]

[project.urls]
github = "https://github.com/MagicStack/uvloop"

[project.optional-dependencies]
test = [
    # pycodestyle is a dependency of flake8, but it must be frozen because
    # their combination breaks too often
    # (example breakage: https://gitlab.com/pycqa/flake8/issues/427)
    'aiohttp>=3.10.5',
    'flake8~=6.1',
    'psutil',
    'pycodestyle~=2.11.0',
    'pyOpenSSL~=25.3.0',
    'mypy>=0.800',
]
dev = [
    'setuptools>=60',
    'Cython~=3.0',
]
docs = [
    'Sphinx~=4.1.2',
    'sphinxcontrib-asyncio~=0.3.0',
    'sphinx_rtd_theme~=0.5.2',
]

[build-system]
requires = [
    "setuptools>=60",
    "wheel",
    "Cython~=3.1",
]
build-backend = "setuptools.build_meta"

[tool.setuptools]
zip-safe = false
packages = ["uvloop"]

[tool.setuptools.exclude-package-data]
"*" = ["*.c", "*.h"]

[tool.cibuildwheel]
build-frontend = "build"
test-extras = "test"
test-command = "python -m unittest discover -v {project}/tests"

[tool.pytest.ini_options]
addopts = "--capture=no --assert=plain --strict-markers --tb=native --import-mode=importlib"
testpaths = "tests"
filterwarnings = "default"
```

## File: `setup.py`
```python
import sys

vi = sys.version_info
if vi < (3, 8):
    raise RuntimeError('uvloop requires Python 3.8 or greater')

if sys.platform in ('win32', 'cygwin', 'cli'):
    raise RuntimeError('uvloop does not support Windows at the moment')

import os
import os.path
import pathlib
import platform
import re
import shutil
import subprocess
import sys

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.sdist import sdist


CYTHON_DEPENDENCY = 'Cython~=3.0'
MACHINE = platform.machine()
MODULES_CFLAGS = [os.getenv('UVLOOP_OPT_CFLAGS', '-O2')]
_ROOT = pathlib.Path(__file__).parent
LIBUV_DIR = str(_ROOT / 'vendor' / 'libuv')
LIBUV_BUILD_DIR = str(_ROOT / 'build' / 'libuv-{}'.format(MACHINE))


def _libuv_build_env():
    env = os.environ.copy()

    cur_cflags = env.get('CFLAGS', '')
    if not re.search(r'-O\d', cur_cflags):
        cur_cflags += ' -O2'

    env['CFLAGS'] = (cur_cflags + ' -fPIC ' + env.get('ARCHFLAGS', ''))

    return env


def _libuv_autogen(env):
    if os.path.exists(os.path.join(LIBUV_DIR, 'configure')):
        # No need to use autogen, the configure script is there.
        return

    if not os.path.exists(os.path.join(LIBUV_DIR, 'autogen.sh')):
        raise RuntimeError(
            'the libuv submodule has not been checked out; '
            'try running "git submodule init; git submodule update"')

    subprocess.run(
        ['/bin/sh', 'autogen.sh'], cwd=LIBUV_DIR, env=env, check=True)


class uvloop_sdist(sdist):
    def run(self):
        # Make sure sdist archive contains configure
        # to avoid the dependency on autotools.
        _libuv_autogen(_libuv_build_env())
        super().run()


class uvloop_build_ext(build_ext):
    user_options = build_ext.user_options + [
        ('cython-always', None,
            'run cythonize() even if .c files are present'),
        ('cython-annotate', None,
            'Produce a colorized HTML version of the Cython source.'),
        ('cython-directives=', None,
            'Cythion compiler directives'),
        ('use-system-libuv', None,
            'Use the system provided libuv, instead of the bundled one'),
    ]

    boolean_options = build_ext.boolean_options + [
        'cython-always',
        'cython-annotate',
        'use-system-libuv',
    ]

    def initialize_options(self):
        super().initialize_options()
        self.use_system_libuv = False
        self.cython_always = False
        self.cython_annotate = None
        self.cython_directives = None

    def finalize_options(self):
        need_cythonize = self.cython_always
        cfiles = {}

        for extension in self.distribution.ext_modules:
            for i, sfile in enumerate(extension.sources):
                if sfile.endswith('.pyx'):
                    prefix, ext = os.path.splitext(sfile)
                    cfile = prefix + '.c'

                    if os.path.exists(cfile) and not self.cython_always:
                        extension.sources[i] = cfile
                    else:
                        if os.path.exists(cfile):
                            cfiles[cfile] = os.path.getmtime(cfile)
                        else:
                            cfiles[cfile] = 0
                        need_cythonize = True

        if need_cythonize:
            import pkg_resources

            # Double check Cython presence in case setup_requires
            # didn't go into effect (most likely because someone
            # imported Cython before setup_requires injected the
            # correct egg into sys.path.
            try:
                import Cython
            except ImportError:
                raise RuntimeError(
                    'please install {} to compile uvloop from source'.format(
                        CYTHON_DEPENDENCY))

            cython_dep = pkg_resources.Requirement.parse(CYTHON_DEPENDENCY)
            if Cython.__version__ not in cython_dep:
                raise RuntimeError(
                    'uvloop requires {}, got Cython=={}'.format(
                        CYTHON_DEPENDENCY, Cython.__version__
                    ))

            from Cython.Build import cythonize

            directives = {}
            if self.cython_directives:
                for directive in self.cython_directives.split(','):
                    k, _, v = directive.partition('=')
                    if v.lower() == 'false':
                        v = False
                    if v.lower() == 'true':
                        v = True

                    directives[k] = v
                self.cython_directives = directives

            self.distribution.ext_modules[:] = cythonize(
                self.distribution.ext_modules,
                compiler_directives=directives,
                annotate=self.cython_annotate,
                compile_time_env=dict(DEFAULT_FREELIST_SIZE=250),
                emit_linenums=self.debug)

        super().finalize_options()

    def build_libuv(self):
        env = _libuv_build_env()

        # Make sure configure and friends are present in case
        # we are building from a git checkout.
        _libuv_autogen(env)

        # Copy the libuv tree to build/ so that its build
        # products don't pollute sdist accidentally.
        if os.path.exists(LIBUV_BUILD_DIR):
            shutil.rmtree(LIBUV_BUILD_DIR)
        shutil.copytree(LIBUV_DIR, LIBUV_BUILD_DIR)

        # Sometimes pip fails to preserve the timestamps correctly,
        # in which case, make will try to run autotools again.
        subprocess.run(
            ['touch', 'configure.ac', 'aclocal.m4', 'configure',
             'Makefile.am', 'Makefile.in'],
            cwd=LIBUV_BUILD_DIR, env=env, check=True)

        if 'LIBUV_CONFIGURE_HOST' in env:
            cmd = ['./configure', '--host=' + env['LIBUV_CONFIGURE_HOST']]
        else:
            cmd = ['./configure']
        subprocess.run(
            cmd,
            cwd=LIBUV_BUILD_DIR, env=env, check=True)

        try:
            njobs = len(os.sched_getaffinity(0))
        except AttributeError:
            njobs = os.cpu_count()
        j_flag = '-j{}'.format(njobs or 1)
        c_flag = "CFLAGS={}".format(env['CFLAGS'])
        subprocess.run(
            ['make', j_flag, c_flag],
            cwd=LIBUV_BUILD_DIR, env=env, check=True)

    def build_extensions(self):
        if self.use_system_libuv:
            self.compiler.add_library('uv')

            if sys.platform == 'darwin' and \
                    os.path.exists('/opt/local/include'):
                # Support macports on Mac OS X.
                self.compiler.add_include_dir('/opt/local/include')
        else:
            libuv_lib = os.path.join(LIBUV_BUILD_DIR, '.libs', 'libuv.a')
            if not os.path.exists(libuv_lib):
                self.build_libuv()
            if not os.path.exists(libuv_lib):
                raise RuntimeError('failed to build libuv')

            self.extensions[-1].extra_objects.extend([libuv_lib])
            self.compiler.add_include_dir(os.path.join(LIBUV_DIR, 'include'))

        if sys.platform.startswith('linux'):
            self.compiler.add_library('rt')
        elif sys.platform.startswith(('freebsd', 'dragonfly')):
            self.compiler.add_library('kvm')
        elif sys.platform.startswith('sunos'):
            self.compiler.add_library('kstat')

        self.compiler.add_library('pthread')

        super().build_extensions()


with open(str(_ROOT / 'uvloop' / '_version.py')) as f:
    for line in f:
        if line.startswith('__version__ ='):
            _, _, version = line.partition('=')
            VERSION = version.strip(" \n'\"")
            break
    else:
        raise RuntimeError(
            'unable to read the version from uvloop/_version.py')


setup_requires = []

if not (_ROOT / 'uvloop' / 'loop.c').exists() or '--cython-always' in sys.argv:
    # No Cython output, require Cython to build.
    setup_requires.append(CYTHON_DEPENDENCY)


setup(
    version=VERSION,
    cmdclass={
        'sdist': uvloop_sdist,
        'build_ext': uvloop_build_ext
    },
    ext_modules=[
        Extension(
            "uvloop.loop",
            sources=[
                "uvloop/loop.pyx",
            ],
            extra_compile_args=MODULES_CFLAGS
        ),
    ],
    setup_requires=setup_requires,
)
```

## File: `docs/.gitignore`
```
_build
_static
_templates
```

## File: `docs/conf.py`
```python
#!/usr/bin/env python3

import alabaster
import os
import sys

sys.path.insert(0, os.path.abspath('..'))

version_file = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            'uvloop', '_version.py')

with open(version_file, 'r') as f:
    for line in f:
        if line.startswith('__version__ ='):
            _, _, version = line.partition('=')
            version = version.strip(" \n'\"")
            break
    else:
        raise RuntimeError(
            'unable to read the version from uvloop/_version.py')


# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'alabaster',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'uvloop'
copyright = '2016-present, MagicStack, Inc'
author = 'Yury Selivanov'
release = version
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'alabaster'
html_theme_options = {
    'description': 'uvloop is an ultra fast implementation of the '
                   'asyncio event loop on top of libuv.',
    'show_powered_by': False,
}
html_theme_path = [alabaster.get_path()]
html_title = 'uvloop Documentation'
html_short_title = 'uvloop'
html_static_path = []
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
htmlhelp_basename = 'uvloopdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

latex_documents = [
    (master_doc, 'uvloop.tex', 'uvloop Documentation',
     'Yury Selivanov', 'manual'),
]


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'uvloop', 'uvloop Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'uvloop', 'uvloop Documentation',
     author, 'uvloop', 'One line description of project.',
     'Miscellaneous'),
]
```

## File: `docs/index.rst`
```
.. image:: https://img.shields.io/github/actions/workflow/status/MagicStack/uvloop/tests.yml?branch=master
    :target: https://github.com/MagicStack/uvloop/actions/workflows/tests.yml?query=branch%3Amaster

.. image:: https://img.shields.io/pypi/status/uvloop.svg?maxAge=2592000?style=plastic
    :target: https://pypi.python.org/pypi/uvloop

.. image:: https://img.shields.io/github/stars/magicstack/uvloop.svg?style=social&label=GitHub
    :target: https://github.com/MagicStack/uvloop


uvloop
======

`uvloop` is a fast, drop-in replacement of the built-in asyncio event loop.
`uvloop` is released under the MIT license.

`uvloop` and asyncio, combined with the power of async/await in Python 3.7,
makes it easier than ever to write high-performance networking code in Python.

`uvloop` makes asyncio fast. In fact, it is at least 2x faster than nodejs,
gevent, as well as any other Python asynchronous framework. The performance of
uvloop-based asyncio is close to that of Go programs.

You can read more about uvloop in this
`blog post <http://magic.io/blog/uvloop-blazing-fast-python-networking/>`_.

Architecture
------------

The asyncio module, introduced by PEP 3156, is a collection of network
transports, protocols, and streams abstractions, with a pluggable event loop.
The event loop is the heart of asyncio. It provides APIs for:

- scheduling calls,
- transmitting data over the network,
- performing DNS queries,
- handling OS signals,
- convenient abstractions to create servers and connections,
- working with subprocesses asynchronously.

`uvloop` implements the :class:`asyncio.AbstractEventLoop` interface which
means that it provides a drop-in replacement of the asyncio event loop.

`uvloop` is written in Cython and is built on top of libuv.

libuv is a high performance, multiplatform asynchronous I/O library used by
nodejs. Because of how wide-spread and popular nodejs is, libuv is fast and
stable.

`uvloop` implements all asyncio event loop APIs. High-level Python objects
wrap low-level libuv structs and functions. Inheritance is used to keep the
code DRY and ensure that any manual memory management is in sync with libuv
primitives' lifespans.


Contents
--------

.. toctree::
   :maxdepth: 1

   user/index
   dev/index
```

## File: `docs/api/index.rst`
```
API
===

If you are looking for information on a specific function, class or method,
this part of the documentation is for you.


uvloop
------

.. autoclass:: uvloop.EventLoopPolicy
  :members:

.. autofunction:: uvloop.new_event_loop

.. autoclass:: uvloop.Loop
  :members:
  :undoc-members:
  :inherited-members:

```

## File: `docs/dev/index.rst`
```
Developers Guide
================

The project is hosted on `GitHub <https://github.com/MagicStack/uvloop>`_.
and uses `GitHub Actions <https://github.com/MagicStack/uvloop/actions>`_ for
Continuous Integration.

A goal for the `uvloop` project is to provide a drop in replacement for the
`asyncio` event loop. Any deviation from the behavior of the reference
`asyncio` event loop is considered a bug.

If you have found a bug or have an idea for an enhancement that would
improve the library, use the
`bug tracker <https://github.com/MagicStack/uvloop/issues>`_.


Get the source
--------------

.. code-block:: console

    $ git clone --recursive git@github.com:MagicStack/uvloop.git

The ``--recursive`` argument is important. It will fetch the ``libuv`` source
from the `libuv` Github repository.


Build
-----

To build `uvloop`, you'll need ``Cython`` and Python 3.8.

.. note::

    The best way to work on `uvloop` is to create a virtual env, so that
    you'll have Cython and Python commands pointing to the correct
    tools.

    .. code-block:: console

        $ python3 -m venv myvenv
        $ source myvenv/bin/activate

Install Cython if not already present.

.. code-block:: console

    $ pip install Cython


Build `uvloop` by running the ``make`` rule from the top level directory.

.. code-block:: console

    $ cd uvloop
    $ make


Test
----

The easiest method to run all of the unit tests is to run the ``make test``
rule from the top level directory. This runs the standard library
``unittest`` tool which discovers all the unit tests and runs them.
It actually runs them twice, once with the `PYTHONASYNCIODEBUG` enabled and
once without.

.. code-block:: console

    $ cd uvloop
    $ make test


Individual Tests
++++++++++++++++

Individual unit tests can be run using the standard library ``unittest``
or ``pytest`` package.

The easiest approach to ensure that ``uvloop`` can be found by Python is to
install the package using ``pip``:

.. code-block:: console

    $ cd uvloop
    $ pip install -e .

You can then run the unit tests individually from the tests directory using
``unittest``:

.. code-block:: console

    $ cd uvloop/tests
    $ python -m unittest test_tcp

or using ``pytest``:

.. code-block:: console

    $ cd uvloop/tests
    $ py.test -k test_signals_sigint_uvcode


Documentation
-------------

To rebuild the project documentation, developers should run the ``make docs``
rule from the top level directory. It performs a number of steps to create
a new set of `sphinx <http://sphinx-doc.org/>`_ html content.

This step requires Sphinx to be installed. Sphinx can be installed using
pip:

.. code-block:: console

    $ pip install sphinx

Once Sphinx is available you can make the documentation using:

.. code-block:: console

    $ make docs
```

## File: `docs/user/index.rst`
```
User Guide
==========

This section of the documentation provides information about how to use
uvloop.


Installation
------------

`uvloop` is available from PyPI. It requires Python 3.8.

Use pip to install it.

.. code-block:: console

    $ pip install uvloop


Using uvloop
------------

To make asyncio use the event loop provided by `uvloop`, you install the
`uvloop` event loop policy:

.. code-block:: python

    import asyncio
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


Alternatively, you can create an instance of the loop manually, using:

.. code-block:: python

    import asyncio
    import uvloop
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
```

## File: `examples/bench/echoclient.py`
```python
# Copied with minimal modifications from curio
# https://github.com/dabeaz/curio


import argparse
import concurrent.futures
import socket
import ssl
import time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--msize', default=1000, type=int,
                        help='message size in bytes')
    parser.add_argument('--mpr', default=1, type=int,
                        help='messages per request')
    parser.add_argument('--num', default=200000, type=int,
                        help='number of messages')
    parser.add_argument('--times', default=1, type=int,
                        help='number of times to run the test')
    parser.add_argument('--workers', default=3, type=int,
                        help='number of workers')
    parser.add_argument('--addr', default='127.0.0.1:25000', type=str,
                        help='address:port of echoserver')
    parser.add_argument('--ssl', default=False, action='store_true')
    args = parser.parse_args()

    client_context = None
    if args.ssl:
        print('with SSL')
        if hasattr(ssl, 'PROTOCOL_TLS'):
            client_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        else:
            client_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        if hasattr(client_context, 'check_hostname'):
            client_context.check_hostname = False
        client_context.verify_mode = ssl.CERT_NONE

    unix = False
    if args.addr.startswith('file:'):
        unix = True
        addr = args.addr[5:]
    else:
        addr = args.addr.split(':')
        addr[1] = int(addr[1])
        addr = tuple(addr)
    print('will connect to: {}'.format(addr))

    MSGSIZE = args.msize
    REQSIZE = MSGSIZE * args.mpr

    msg = b'x' * (MSGSIZE - 1) + b'\n'
    if args.mpr:
        msg *= args.mpr

    def run_test(n):
        print('Sending', NMESSAGES, 'messages')
        if args.mpr:
            n //= args.mpr

        if unix:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except (OSError, NameError):
            pass

        if client_context:
            sock = client_context.wrap_socket(sock)

        sock.connect(addr)

        while n > 0:
            sock.sendall(msg)
            nrecv = 0
            while nrecv < REQSIZE:
                resp = sock.recv(REQSIZE)
                if not resp:
                    raise SystemExit()
                nrecv += len(resp)
            n -= 1

    TIMES = args.times
    N = args.workers
    NMESSAGES = args.num
    start = time.time()
    for _ in range(TIMES):
        with concurrent.futures.ProcessPoolExecutor(max_workers=N) as e:
            for _ in range(N):
                e.submit(run_test, NMESSAGES)
    end = time.time()
    duration = end - start
    print(NMESSAGES * N * TIMES, 'in', duration)
    print(NMESSAGES * N * TIMES / duration, 'requests/sec')
```

## File: `examples/bench/echoserver.py`
```python
import argparse
import asyncio
import gc
import os.path
import pathlib
import socket
import ssl


PRINT = 0


async def echo_server(loop, address, unix):
    if unix:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    if PRINT:
        print('Server listening at', address)
    with sock:
        while True:
            client, addr = await loop.sock_accept(sock)
            if PRINT:
                print('Connection from', addr)
            loop.create_task(echo_client(loop, client))


async def echo_client(loop, client):
    try:
        client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    except (OSError, NameError):
        pass

    with client:
        while True:
            data = await loop.sock_recv(client, 1000000)
            if not data:
                break
            await loop.sock_sendall(client, data)
    if PRINT:
        print('Connection closed')


async def echo_client_streams(reader, writer):
    sock = writer.get_extra_info('socket')
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    except (OSError, NameError):
        pass
    if PRINT:
        print('Connection from', sock.getpeername())
    while True:
        data = await reader.read(1000000)
        if not data:
            break
        writer.write(data)
    if PRINT:
        print('Connection closed')
    writer.close()


class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def connection_lost(self, exc):
        self.transport = None

    def data_received(self, data):
        self.transport.write(data)


class EchoBufferedProtocol(asyncio.BufferedProtocol):
    def connection_made(self, transport):
        self.transport = transport
        # Here the buffer is intended to be copied, so that the outgoing buffer
        # won't be wrongly updated by next read
        self.buffer = bytearray(256 * 1024)

    def connection_lost(self, exc):
        self.transport = None

    def get_buffer(self, sizehint):
        return self.buffer

    def buffer_updated(self, nbytes):
        self.transport.write(self.buffer[:nbytes])


async def print_debug(loop):
    while True:
        print(chr(27) + "[2J")  # clear screen
        loop.print_debug_info()
        await asyncio.sleep(0.5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--uvloop', default=False, action='store_true')
    parser.add_argument('--streams', default=False, action='store_true')
    parser.add_argument('--proto', default=False, action='store_true')
    parser.add_argument('--addr', default='127.0.0.1:25000', type=str)
    parser.add_argument('--print', default=False, action='store_true')
    parser.add_argument('--ssl', default=False, action='store_true')
    parser.add_argument('--buffered', default=False, action='store_true')
    args = parser.parse_args()

    if args.uvloop:
        import uvloop
        loop = uvloop.new_event_loop()
        print('using UVLoop')
    else:
        loop = asyncio.new_event_loop()
        print('using asyncio loop')

    asyncio.set_event_loop(loop)
    loop.set_debug(False)

    if args.print:
        PRINT = 1

    if hasattr(loop, 'print_debug_info'):
        loop.create_task(print_debug(loop))
        PRINT = 0

    unix = False
    if args.addr.startswith('file:'):
        unix = True
        addr = args.addr[5:]
        if os.path.exists(addr):
            os.remove(addr)
    else:
        addr = args.addr.split(':')
        addr[1] = int(addr[1])
        addr = tuple(addr)

    print('serving on: {}'.format(addr))

    server_context = None
    if args.ssl:
        print('with SSL')
        if hasattr(ssl, 'PROTOCOL_TLS'):
            server_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        else:
            server_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        server_context.load_cert_chain(
            (pathlib.Path(__file__).parent.parent.parent /
                'tests' / 'certs' / 'ssl_cert.pem'),
            (pathlib.Path(__file__).parent.parent.parent /
                'tests' / 'certs' / 'ssl_key.pem'))
        if hasattr(server_context, 'check_hostname'):
            server_context.check_hostname = False
        server_context.verify_mode = ssl.CERT_NONE

    if args.streams:
        if args.proto:
            print('cannot use --stream and --proto simultaneously')
            exit(1)

        if args.buffered:
            print('cannot use --stream and --buffered simultaneously')
            exit(1)

        print('using asyncio/streams')
        if unix:
            coro = asyncio.start_unix_server(echo_client_streams,
                                             addr,
                                             ssl=server_context)
        else:
            coro = asyncio.start_server(echo_client_streams,
                                        *addr,
                                        ssl=server_context)
        srv = loop.run_until_complete(coro)
    elif args.proto:
        if args.streams:
            print('cannot use --stream and --proto simultaneously')
            exit(1)

        if args.buffered:
            print('using buffered protocol')
            protocol = EchoBufferedProtocol
        else:
            print('using simple protocol')
            protocol = EchoProtocol

        if unix:
            coro = loop.create_unix_server(protocol, addr,
                                           ssl=server_context)
        else:
            coro = loop.create_server(protocol, *addr,
                                      ssl=server_context)
        srv = loop.run_until_complete(coro)
    else:
        if args.ssl:
            print('cannot use SSL for loop.sock_* methods')
            exit(1)

        print('using sock_recv/sock_sendall')
        loop.create_task(echo_server(loop, addr, unix))
    try:
        loop.run_forever()
    finally:
        if hasattr(loop, 'print_debug_info'):
            gc.collect()
            print(chr(27) + "[2J")
            loop.print_debug_info()

        loop.close()
```

## File: `examples/bench/rlserver.py`
```python
import argparse
import asyncio
import gc
import os.path
import socket as stdsock


PRINT = 0


async def echo_client_streams(reader, writer):
    sock = writer.get_extra_info('socket')
    try:
        sock.setsockopt(
            stdsock.IPPROTO_TCP, stdsock.TCP_NODELAY, 1)
    except (OSError, NameError):
        pass
    if PRINT:
        print('Connection from', sock.getpeername())
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(data)
    if PRINT:
        print('Connection closed')
    writer.close()


async def print_debug(loop):
    while True:
        print(chr(27) + "[2J")  # clear screen
        loop.print_debug_info()
        await asyncio.sleep(0.5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--uvloop', default=False, action='store_true')
    parser.add_argument('--addr', default='127.0.0.1:25000', type=str)
    parser.add_argument('--print', default=False, action='store_true')
    args = parser.parse_args()

    if args.uvloop:
        import uvloop
        loop = uvloop.new_event_loop()
        print('using UVLoop')
    else:
        loop = asyncio.new_event_loop()
        print('using asyncio loop')

    asyncio.set_event_loop(loop)
    loop.set_debug(False)

    if args.print:
        PRINT = 1

    if hasattr(loop, 'print_debug_info'):
        loop.create_task(print_debug(loop))
        PRINT = 0

    unix = False
    if args.addr.startswith('file:'):
        unix = True
        addr = args.addr[5:]
        if os.path.exists(addr):
            os.remove(addr)
    else:
        addr = args.addr.split(':')
        addr[1] = int(addr[1])
        addr = tuple(addr)

    print('readline performance test')
    print('serving on: {}'.format(addr))

    print('using asyncio/streams')
    if unix:
        coro = asyncio.start_unix_server(echo_client_streams,
                                         addr, limit=256000)
    else:
        coro = asyncio.start_server(echo_client_streams,
                                    *addr, limit=256000)
    srv = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    finally:
        if hasattr(loop, 'print_debug_info'):
            gc.collect()
            print(chr(27) + "[2J")
            loop.print_debug_info()

        loop.close()
```

## File: `tests/__main__.py`
```python
import os.path
import sys
import unittest
import unittest.runner


def suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(os.path.dirname(__file__))
    return test_suite


if __name__ == '__main__':
    runner = unittest.runner.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
```

## File: `tests/test_aiohttp.py`
```python
try:
    import aiohttp
    import aiohttp.web
except ImportError:
    skip_tests = True
else:
    skip_tests = False

import asyncio
import sys
import unittest
import weakref

from uvloop import _testbase as tb


class _TestAioHTTP:

    def test_aiohttp_basic_1(self):

        PAYLOAD = '<h1>It Works!</h1>' * 10000

        async def on_request(request):
            return aiohttp.web.Response(text=PAYLOAD)

        asyncio.set_event_loop(self.loop)
        app = aiohttp.web.Application()
        app.router.add_get('/', on_request)

        runner = aiohttp.web.AppRunner(app)
        self.loop.run_until_complete(runner.setup())
        site = aiohttp.web.TCPSite(runner, '0.0.0.0', '0')
        self.loop.run_until_complete(site.start())
        port = site._server.sockets[0].getsockname()[1]

        async def test():
            # Make sure we're using the correct event loop.
            self.assertIs(asyncio.get_event_loop(), self.loop)

            for addr in (('localhost', port),
                         ('127.0.0.1', port)):
                async with aiohttp.ClientSession() as client:
                    async with client.get('http://{}:{}'.format(*addr)) as r:
                        self.assertEqual(r.status, 200)
                        result = await r.text()
                        self.assertEqual(result, PAYLOAD)

        self.loop.run_until_complete(test())
        self.loop.run_until_complete(runner.cleanup())

    def test_aiohttp_graceful_shutdown(self):
        if self.implementation == 'asyncio' and sys.version_info >= (3, 12, 0):
            # In Python 3.12.0, asyncio.Server.wait_closed() waits for all
            # existing connections to complete, before aiohttp sends
            # on_shutdown signals.
            # https://github.com/aio-libs/aiohttp/issues/7675#issuecomment-1752143748
            # https://github.com/python/cpython/pull/98582
            raise unittest.SkipTest('bug in aiohttp: #7675')

        async def websocket_handler(request):
            ws = aiohttp.web.WebSocketResponse()
            await ws.prepare(request)
            request.app['websockets'].add(ws)
            try:
                async for msg in ws:
                    await ws.send_str(msg.data)
            finally:
                request.app['websockets'].discard(ws)
            return ws

        async def on_shutdown(app):
            for ws in set(app['websockets']):
                await ws.close(
                    code=aiohttp.WSCloseCode.GOING_AWAY,
                    message='Server shutdown')

        asyncio.set_event_loop(self.loop)
        app = aiohttp.web.Application()
        app.router.add_get('/', websocket_handler)
        app.on_shutdown.append(on_shutdown)
        app['websockets'] = weakref.WeakSet()

        runner = aiohttp.web.AppRunner(app)
        self.loop.run_until_complete(runner.setup())
        site = aiohttp.web.TCPSite(
            runner,
            '0.0.0.0',
            0,
            # https://github.com/aio-libs/aiohttp/pull/7188
            shutdown_timeout=0.1,
        )
        self.loop.run_until_complete(site.start())
        port = site._server.sockets[0].getsockname()[1]

        async def client():
            async with aiohttp.ClientSession() as client:
                async with client.ws_connect(
                        'http://127.0.0.1:{}'.format(port)) as ws:
                    await ws.send_str("hello")
                    async for msg in ws:
                        assert msg.data == "hello"

        client_task = asyncio.ensure_future(client())

        async def stop():
            await asyncio.sleep(0.1)
            try:
                await asyncio.wait_for(runner.cleanup(), timeout=0.5)
            finally:
                try:
                    client_task.cancel()
                    await client_task
                except asyncio.CancelledError:
                    pass

        self.loop.run_until_complete(stop())


@unittest.skipIf(skip_tests, "no aiohttp module")
class Test_UV_AioHTTP(_TestAioHTTP, tb.UVTestCase):
    pass


@unittest.skipIf(skip_tests, "no aiohttp module")
class Test_AIO_AioHTTP(_TestAioHTTP, tb.AIOTestCase):
    pass
```

## File: `tests/test_base.py`
```python
import asyncio
import fcntl
import logging
import os
import random
import sys
import subprocess
import threading
import time
import uvloop
import unittest
import weakref

from unittest import mock
from uvloop._testbase import UVTestCase, AIOTestCase


class _TestBase:

    def test_close(self):
        self.assertFalse(self.loop._closed)
        self.assertFalse(self.loop.is_closed())
        self.loop.close()
        self.assertTrue(self.loop._closed)
        self.assertTrue(self.loop.is_closed())

        # it should be possible to call close() more than once
        self.loop.close()
        self.loop.close()

        # operation blocked when the loop is closed
        f = asyncio.Future()
        self.assertRaises(RuntimeError, self.loop.run_forever)
        self.assertRaises(RuntimeError, self.loop.run_until_complete, f)

    def test_handle_weakref(self):
        wd = weakref.WeakValueDictionary()
        h = self.loop.call_soon(lambda: None)
        wd['h'] = h  # Would fail without __weakref__ slot.

    def test_call_soon_1(self):
        calls = []

        def cb(inc):
            calls.append(inc)
            self.loop.stop()

        self.loop.call_soon(cb, 10)

        h = self.loop.call_soon(cb, 100)
        self.assertIn('.cb', repr(h))
        h.cancel()
        self.assertIn('cancelled', repr(h))

        self.loop.call_soon(cb, 1)

        self.loop.run_forever()

        self.assertEqual(calls, [10, 1])

    def test_call_soon_2(self):
        waiter = self.loop.create_future()
        waiter_r = weakref.ref(waiter)
        self.loop.call_soon(lambda f: f.set_result(None), waiter)
        self.loop.run_until_complete(waiter)
        del waiter
        self.assertIsNone(waiter_r())

    def test_call_soon_3(self):
        waiter = self.loop.create_future()
        waiter_r = weakref.ref(waiter)
        self.loop.call_soon(lambda f=waiter: f.set_result(None))
        self.loop.run_until_complete(waiter)
        del waiter
        self.assertIsNone(waiter_r())

    def test_call_soon_base_exc(self):
        def cb():
            raise KeyboardInterrupt()

        self.loop.call_soon(cb)

        with self.assertRaises(KeyboardInterrupt):
            self.loop.run_forever()

        self.assertFalse(self.loop.is_closed())

    def test_calls_debug_reporting(self):
        def run_test(debug, meth, stack_adj):
            context = None

            def handler(loop, ctx):
                nonlocal context
                context = ctx

            self.loop.set_debug(debug)
            self.loop.set_exception_handler(handler)

            def cb():
                1 / 0

            meth(cb)
            self.assertIsNone(context)
            self.loop.run_until_complete(asyncio.sleep(0.05))

            self.assertIs(type(context['exception']), ZeroDivisionError)
            self.assertTrue(context['message'].startswith(
                'Exception in callback'))

            if debug:
                tb = context['source_traceback']
                self.assertEqual(tb[-1 + stack_adj].name, 'run_test')
            else:
                self.assertFalse('source_traceback' in context)

            del context

        for debug in (True, False):
            for meth_name, meth, stack_adj in (
                ('call_soon',
                    self.loop.call_soon, 0),
                ('call_later',  # `-1` accounts for lambda
                    lambda *args: self.loop.call_later(0.01, *args), -1)
            ):
                with self.subTest(debug=debug, meth_name=meth_name):
                    run_test(debug, meth, stack_adj)

    def test_now_update(self):
        async def run():
            st = self.loop.time()
            time.sleep(0.05)
            return self.loop.time() - st

        delta = self.loop.run_until_complete(run())
        self.assertTrue(delta > 0.049 and delta < 0.6)

    def test_call_later_1(self):
        calls = []

        def cb(inc=10, stop=False):
            calls.append(inc)
            self.assertTrue(self.loop.is_running())
            if stop:
                self.loop.call_soon(self.loop.stop)

        self.loop.call_later(0.05, cb)

        # canceled right away
        h = self.loop.call_later(0.05, cb, 100, True)
        self.assertIn('.cb', repr(h))
        h.cancel()
        self.assertIn('cancelled', repr(h))

        self.loop.call_later(0.05, cb, 1, True)
        self.loop.call_later(1000, cb, 1000)  # shouldn't be called

        started = time.monotonic()
        self.loop.run_forever()
        finished = time.monotonic()

        self.assertEqual(calls, [10, 1])
        self.assertFalse(self.loop.is_running())

        self.assertLess(finished - started, 0.3)
        self.assertGreater(finished - started, 0.04)

    def test_call_later_2(self):
        # Test that loop.call_later triggers an update of
        # libuv cached time.

        async def main():
            await asyncio.sleep(0.001)
            time.sleep(0.01)
            await asyncio.sleep(0.01)

        started = time.monotonic()
        self.loop.run_until_complete(main())
        delta = time.monotonic() - started
        self.assertGreater(delta, 0.019)

    def test_call_later_3(self):
        # a memory leak regression test
        waiter = self.loop.create_future()
        waiter_r = weakref.ref(waiter)
        self.loop.call_later(0.01, lambda f: f.set_result(None), waiter)
        self.loop.run_until_complete(waiter)
        del waiter
        self.assertIsNone(waiter_r())

    def test_call_later_4(self):
        # a memory leak regression test
        waiter = self.loop.create_future()
        waiter_r = weakref.ref(waiter)
        self.loop.call_later(0.01, lambda f=waiter: f.set_result(None))
        self.loop.run_until_complete(waiter)
        del waiter
        self.assertIsNone(waiter_r())

    def test_call_later_negative(self):
        calls = []

        def cb(arg):
            calls.append(arg)
            self.loop.stop()

        self.loop.call_later(-1, cb, 'a')
        self.loop.run_forever()
        self.assertEqual(calls, ['a'])

    def test_call_later_rounding(self):
        # Refs #233, call_later() and call_at() shouldn't call cb early

        def cb():
            self.loop.stop()

        for i in range(8):
            self.loop.call_later(0.06 + 0.01, cb)  # 0.06999999999999999
            started = int(round(self.loop.time() * 1000))
            self.loop.run_forever()
            finished = int(round(self.loop.time() * 1000))
            self.assertGreaterEqual(finished - started, 69)

    def test_call_at(self):
        if (os.environ.get('TRAVIS_OS_NAME')
                or os.environ.get('GITHUB_WORKFLOW')):
            # Time seems to be really unpredictable on Travis.
            raise unittest.SkipTest('time is not monotonic on CI')

        i = 0

        def cb(inc):
            nonlocal i
            i += inc
            self.loop.stop()

        at = self.loop.time() + 0.05

        self.loop.call_at(at, cb, 100).cancel()
        self.loop.call_at(at, cb, 10)

        started = time.monotonic()
        self.loop.run_forever()
        finished = time.monotonic()

        self.assertEqual(i, 10)

        self.assertLess(finished - started, 0.07)
        self.assertGreater(finished - started, 0.045)

    def test_check_thread(self):
        def check_thread(loop, debug):
            def cb():
                pass

            loop.set_debug(debug)
            if debug:
                msg = ("Non-thread-safe operation invoked on an "
                       "event loop other than the current one")
                with self.assertRaisesRegex(RuntimeError, msg):
                    loop.call_soon(cb)
                with self.assertRaisesRegex(RuntimeError, msg):
                    loop.call_later(60, cb)
                with self.assertRaisesRegex(RuntimeError, msg):
                    loop.call_at(loop.time() + 60, cb)
            else:
                loop.call_soon(cb)
                loop.call_later(60, cb)
                loop.call_at(loop.time() + 60, cb)

        def check_in_thread(loop, event, debug, create_loop, fut):
            # wait until the event loop is running
            event.wait()

            try:
                if create_loop:
                    loop2 = self.new_loop()
                    try:
                        asyncio.set_event_loop(loop2)
                        check_thread(loop, debug)
                    finally:
                        asyncio.set_event_loop(None)
                        loop2.close()
                else:
                    check_thread(loop, debug)
            except Exception as exc:
                loop.call_soon_threadsafe(fut.set_exception, exc)
            else:
                loop.call_soon_threadsafe(fut.set_result, None)

        def test_thread(loop, debug, create_loop=False):
            event = threading.Event()
            fut = asyncio.Future(loop=loop)
            loop.call_soon(event.set)
            args = (loop, event, debug, create_loop, fut)
            thread = threading.Thread(target=check_in_thread, args=args)
            thread.start()
            loop.run_until_complete(fut)
            thread.join()

        # raise RuntimeError if the thread has no event loop
        test_thread(self.loop, True)

        # check disabled if debug mode is disabled
        test_thread(self.loop, False)

        # raise RuntimeError if the event loop of the thread is not the called
        # event loop
        test_thread(self.loop, True, create_loop=True)

        # check disabled if debug mode is disabled
        test_thread(self.loop, False, create_loop=True)

    def test_run_once_in_executor_plain(self):
        called = []

        def cb(arg):
            called.append(arg)

        async def runner():
            await self.loop.run_in_executor(None, cb, 'a')

        self.loop.run_until_complete(runner())

        self.assertEqual(called, ['a'])

    def test_set_debug(self):
        self.loop.set_debug(True)
        self.assertTrue(self.loop.get_debug())
        self.loop.set_debug(False)
        self.assertFalse(self.loop.get_debug())

    def test_run_until_complete_type_error(self):
        self.assertRaises(
            TypeError, self.loop.run_until_complete, 'blah')

    def test_run_until_complete_loop(self):
        task = asyncio.Future()
        other_loop = self.new_loop()
        self.addCleanup(other_loop.close)
        self.assertRaises(
            ValueError, other_loop.run_until_complete, task)

    def test_run_until_complete_error(self):
        async def foo():
            raise ValueError('aaa')
        with self.assertRaisesRegex(ValueError, 'aaa'):
            self.loop.run_until_complete(foo())

    def test_run_until_complete_loop_orphan_future_close_loop(self):
        async def foo(delay):
            await asyncio.sleep(delay)

        def throw():
            raise KeyboardInterrupt

        self.loop.call_soon(throw)
        try:
            self.loop.run_until_complete(foo(0.1))
        except KeyboardInterrupt:
            pass

        # This call fails if run_until_complete does not clean up
        # done-callback for the previous future.
        self.loop.run_until_complete(foo(0.2))

    def test_run_until_complete_keyboard_interrupt(self):
        # Issue #336: run_until_complete() must not schedule a pending
        # call to stop() if the future raised a KeyboardInterrupt
        async def raise_keyboard_interrupt():
            raise KeyboardInterrupt

        self.loop._process_events = mock.Mock()

        with self.assertRaises(KeyboardInterrupt):
            self.loop.run_until_complete(raise_keyboard_interrupt())

        def func():
            self.loop.stop()
            func.called = True

        func.called = False
        self.loop.call_later(0.01, func)
        self.loop.run_forever()
        self.assertTrue(func.called)

    def test_debug_slow_callbacks(self):
        logger = logging.getLogger('asyncio')
        self.loop.set_debug(True)
        self.loop.slow_callback_duration = 0.2
        self.loop.call_soon(lambda: time.sleep(0.3))

        with mock.patch.object(logger, 'warning') as log:
            self.loop.run_until_complete(asyncio.sleep(0))

        self.assertEqual(log.call_count, 1)
        # format message
        msg = log.call_args[0][0] % log.call_args[0][1:]

        self.assertIn('Executing <Handle', msg)
        self.assertIn('test_debug_slow_callbacks', msg)

    def test_debug_slow_timer_callbacks(self):
        logger = logging.getLogger('asyncio')
        self.loop.set_debug(True)
        self.loop.slow_callback_duration = 0.2
        self.loop.call_later(0.01, lambda: time.sleep(0.3))

        with mock.patch.object(logger, 'warning') as log:
            self.loop.run_until_complete(asyncio.sleep(0.02))

        self.assertEqual(log.call_count, 1)
        # format message
        msg = log.call_args[0][0] % log.call_args[0][1:]

        self.assertIn('Executing <TimerHandle', msg)
        self.assertIn('test_debug_slow_timer_callbacks', msg)

    def test_debug_slow_task_callbacks(self):
        logger = logging.getLogger('asyncio')
        self.loop.set_debug(True)
        self.loop.slow_callback_duration = 0.2

        async def foo():
            time.sleep(0.3)

        with mock.patch.object(logger, 'warning') as log:
            self.loop.run_until_complete(foo())

        self.assertEqual(log.call_count, 1)
        # format message
        msg = log.call_args[0][0] % log.call_args[0][1:]

        self.assertIn('Executing <Task finished', msg)
        self.assertIn('test_debug_slow_task_callbacks', msg)

    def test_default_exc_handler_callback(self):
        self.loop.set_exception_handler(None)

        self.loop._process_events = mock.Mock()

        def zero_error(fut):
            fut.set_result(True)
            1 / 0

        logger = logging.getLogger('asyncio')

        # Test call_soon (events.Handle)
        with mock.patch.object(logger, 'error') as log:
            fut = asyncio.Future()
            self.loop.call_soon(zero_error, fut)
            fut.add_done_callback(lambda fut: self.loop.stop())
            self.loop.run_forever()
            log.assert_called_with(
                self.mock_pattern('Exception in callback.*zero'),
                exc_info=mock.ANY)

        # Test call_later (events.TimerHandle)
        with mock.patch.object(logger, 'error') as log:
            fut = asyncio.Future()
            self.loop.call_later(0.01, zero_error, fut)
            fut.add_done_callback(lambda fut: self.loop.stop())
            self.loop.run_forever()
            log.assert_called_with(
                self.mock_pattern('Exception in callback.*zero'),
                exc_info=mock.ANY)

    def test_set_exc_handler_custom(self):
        self.loop.set_exception_handler(None)
        logger = logging.getLogger('asyncio')

        def run_loop():
            def zero_error():
                self.loop.stop()
                1 / 0
            self.loop.call_soon(zero_error)
            self.loop.run_forever()

        errors = []

        def handler(loop, exc):
            errors.append(exc)

        self.loop.set_debug(True)

        self.assertIsNone(self.loop.get_exception_handler())
        self.loop.set_exception_handler(handler)
        if hasattr(self.loop, 'get_exception_handler'):
            self.assertIs(self.loop.get_exception_handler(), handler)
        run_loop()
        self.assertEqual(len(errors), 1)
        self.assertRegex(errors[-1]['message'],
                         'Exception in callback.*zero_error')

        self.loop.set_exception_handler(None)
        with mock.patch.object(logger, 'error') as log:
            run_loop()
            log.assert_called_with(
                self.mock_pattern('Exception in callback.*zero'),
                exc_info=mock.ANY)

        self.assertEqual(len(errors), 1)

    def test_set_exc_handler_broken(self):
        logger = logging.getLogger('asyncio')

        def run_loop():
            def zero_error():
                self.loop.stop()
                1 / 0
            self.loop.call_soon(zero_error)
            self.loop.run_forever()

        def handler(loop, context):
            raise AttributeError('spam')

        self.loop._process_events = mock.Mock()

        self.loop.set_exception_handler(handler)

        with mock.patch.object(logger, 'error') as log:
            run_loop()
            log.assert_called_with(
                self.mock_pattern('Unhandled error in exception handler'),
                exc_info=mock.ANY)

    def test_set_task_factory_invalid(self):
        with self.assertRaisesRegex(
                TypeError,
                'task factory must be a callable or None'):

            self.loop.set_task_factory(1)

        self.assertIsNone(self.loop.get_task_factory())

    def test_set_task_factory(self):
        self.loop._process_events = mock.Mock()

        class MyTask(asyncio.Task):
            pass

        async def coro():
            pass

        factory = lambda loop, coro, **kwargs: MyTask(
            coro, loop=loop, **kwargs
        )

        self.assertIsNone(self.loop.get_task_factory())
        self.loop.set_task_factory(factory)
        self.assertIs(self.loop.get_task_factory(), factory)

        task = self.loop.create_task(coro())
        self.assertTrue(isinstance(task, MyTask))
        self.loop.run_until_complete(task)

        self.loop.set_task_factory(None)
        self.assertIsNone(self.loop.get_task_factory())

        task = self.loop.create_task(coro())
        self.assertTrue(isinstance(task, asyncio.Task))
        self.assertFalse(isinstance(task, MyTask))
        self.loop.run_until_complete(task)

    def test_set_task_name(self):
        self.loop._process_events = mock.Mock()

        result = None

        class MyTask(asyncio.Task):
            def set_name(self, name):
                nonlocal result
                result = name + "!"

            def get_name(self):
                return result

        async def coro():
            pass

        def factory(loop, coro, **kwargs):
            task = MyTask(coro, loop=loop, **kwargs)
            # Python moved the responsibility to set the name to the Task
            # class constructor, so MyTask.set_name is never called by
            # Python's create_task.  Compensate for that here.
            if self.is_asyncio_loop() and "name" in kwargs:
                task.set_name(kwargs["name"])
            return task

        self.assertIsNone(self.loop.get_task_factory())
        task = self.loop.create_task(coro(), name="mytask")
        self.assertFalse(isinstance(task, MyTask))
        self.assertEqual(task.get_name(), "mytask")
        self.loop.run_until_complete(task)

        self.loop.set_task_factory(factory)
        self.assertIs(self.loop.get_task_factory(), factory)

        task = self.loop.create_task(coro(), name="mytask")
        self.assertTrue(isinstance(task, MyTask))
        self.assertEqual(result, "mytask!")
        self.assertEqual(task.get_name(), "mytask!")
        self.loop.run_until_complete(task)

        self.loop.set_task_factory(None)
        self.assertIsNone(self.loop.get_task_factory())

    def test_shutdown_asyncgens_01(self):
        finalized = list()

        if not hasattr(self.loop, 'shutdown_asyncgens'):
            raise unittest.SkipTest()

        async def waiter(timeout, finalized):
            try:
                await asyncio.sleep(timeout)
                yield 1
            finally:
                await asyncio.sleep(0)
                finalized.append(1)

        async def wait():
            async for _ in waiter(1, finalized):
                pass

        t1 = self.loop.create_task(wait())
        t2 = self.loop.create_task(wait())

        self.loop.run_until_complete(asyncio.sleep(0.1))

        t1.cancel()
        t2.cancel()
        self.loop.run_until_complete(self.loop.shutdown_asyncgens())
        self.assertEqual(finalized, [1, 1])

        for t in {t1, t2}:
            try:
                self.loop.run_until_complete(t)
            except asyncio.CancelledError:
                pass

    def test_shutdown_asyncgens_02(self):
        if not hasattr(self.loop, 'shutdown_asyncgens'):
            raise unittest.SkipTest()

        logged = 0

        def logger(loop, context):
            nonlocal logged
            expected = 'an error occurred during closing of asynchronous'
            if expected in context['message']:
                self.assertIn('asyncgen', context)
                logged += 1

        async def waiter(timeout):
            try:
                await asyncio.sleep(timeout)
                yield 1
            finally:
                1 / 0

        async def wait():
            async for _ in waiter(1):
                pass

        t = self.loop.create_task(wait())
        self.loop.run_until_complete(asyncio.sleep(0.1))

        self.loop.set_exception_handler(logger)
        self.loop.run_until_complete(self.loop.shutdown_asyncgens())

        self.assertEqual(logged, 1)

        # Silence warnings
        t.cancel()
        self.loop.run_until_complete(asyncio.sleep(0.1))

    def test_shutdown_asyncgens_03(self):
        if not hasattr(self.loop, 'shutdown_asyncgens'):
            raise unittest.SkipTest()

        async def waiter():
            yield 1
            yield 2

        async def foo():
            # We specifically want to hit _asyncgen_finalizer_hook
            # method.
            await waiter().asend(None)

        self.loop.run_until_complete(foo())
        self.loop.run_until_complete(asyncio.sleep(0.01))

    def test_inf_wait_for(self):
        async def foo():
            await asyncio.sleep(0.1)
            return 123
        res = self.loop.run_until_complete(
            asyncio.wait_for(foo(), timeout=float('inf')))
        self.assertEqual(res, 123)

    def test_shutdown_default_executor(self):
        if not hasattr(self.loop, "shutdown_default_executor"):
            raise unittest.SkipTest()

        async def foo():
            await self.loop.run_in_executor(None, time.sleep, .1)

        self.loop.run_until_complete(foo())
        self.loop.run_until_complete(
            self.loop.shutdown_default_executor())

    def test_call_soon_threadsafe_safety(self):
        ITERATIONS = 4096
        counter = [0]

        def cb():
            counter[0] += 1
            if counter[0] < ITERATIONS - 512:
                h = self.loop.call_later(0.01, lambda: None)
                self.loop.call_later(
                    0.0005 + random.random() * 0.0005, h.cancel
                )

        def scheduler():
            loop = self.loop
            for i in range(ITERATIONS):
                if loop.is_running():
                    loop.call_soon_threadsafe(cb)
                time.sleep(0.001)
            loop.call_soon_threadsafe(loop.stop)

        thread = threading.Thread(target=scheduler)

        self.loop.call_soon(thread.start)
        self.loop.run_forever()
        thread.join()
        self.assertEqual(counter[0], ITERATIONS)

    def test_freethreading(self):
        if not hasattr(sys, "_is_gil_enabled"):
            raise unittest.SkipTest("No sys._is_gil_enabled()")
        if os.cpu_count() < 2:
            raise unittest.SkipTest("Flaky on single CPU machines")
        prog = """\
import asyncio
import os
import sys
import threading
import time


counter = 0


def job(barrier):
    global counter
    barrier.wait()
    start_time = time.monotonic()
    rv = 0
    while time.monotonic() - start_time < 1:
        for _i in range(10**4):
            counter += 1
            rv += 1
    return rv


async def main():
    if sys._is_gil_enabled():
        print("{impl} turned on GIL")
        return False
    loop = asyncio.get_running_loop()
    n_jobs = os.cpu_count()
    barrier = threading.Barrier(n_jobs)
    fs = [loop.run_in_executor(None, job, barrier) for _ in range(n_jobs)]
    result = sum(await asyncio.gather(*fs))
    if counter == result:
        print("Expected race condition did not happen")
        return False
    return True


if __name__ == "__main__":
    if sys._is_gil_enabled():
        print("Not running with GIL disabled")
        sys.exit(2)

    import {impl}

    if not {impl}.run(main()):
        sys.exit(1)
"""
        result = subprocess.run(
            [sys.executable, '-c', prog.format(impl=self.implementation)],
            stdout=subprocess.PIPE,
            text=True,
        )
        if result.returncode == 2:
            raise unittest.SkipTest(result.stdout.strip())
        elif result.returncode != 0:
            self.fail(result.stdout.strip())


class TestBaseUV(_TestBase, UVTestCase):

    def test_loop_create_future(self):
        fut = self.loop.create_future()
        self.assertTrue(isinstance(fut, asyncio.Future))
        self.assertIs(fut._loop, self.loop)
        fut.cancel()

    def test_loop_call_soon_handle_cancelled(self):
        cb = lambda: False  # NoQA
        handle = self.loop.call_soon(cb)
        self.assertFalse(handle.cancelled())
        handle.cancel()
        self.assertTrue(handle.cancelled())

        handle = self.loop.call_soon(cb)
        self.assertFalse(handle.cancelled())
        self.run_loop_briefly()
        self.assertFalse(handle.cancelled())

    def test_loop_call_later_handle_cancelled(self):
        cb = lambda: False  # NoQA
        handle = self.loop.call_later(0.01, cb)
        self.assertFalse(handle.cancelled())
        handle.cancel()
        self.assertTrue(handle.cancelled())

        handle = self.loop.call_later(0.01, cb)
        self.assertFalse(handle.cancelled())
        self.run_loop_briefly(delay=0.05)
        self.assertFalse(handle.cancelled())

    def test_loop_std_files_cloexec(self):
        # See https://github.com/MagicStack/uvloop/issues/40 for details.
        for fd in {0, 1, 2}:
            flags = fcntl.fcntl(fd, fcntl.F_GETFD)
            self.assertFalse(flags & fcntl.FD_CLOEXEC)

    def test_default_exc_handler_broken(self):
        logger = logging.getLogger('asyncio')
        _context = None

        class Loop(uvloop.Loop):

            _selector = mock.Mock()
            _process_events = mock.Mock()

            def default_exception_handler(self, context):
                nonlocal _context
                _context = context
                # Simulates custom buggy "default_exception_handler"
                raise ValueError('spam')

        loop = Loop()
        self.addCleanup(loop.close)
        self.addCleanup(lambda: asyncio.set_event_loop(None))

        asyncio.set_event_loop(loop)

        def run_loop():
            def zero_error():
                loop.stop()
                1 / 0
            loop.call_soon(zero_error)
            loop.run_forever()

        with mock.patch.object(logger, 'error') as log:
            run_loop()
            log.assert_called_with(
                'Exception in default exception handler',
                exc_info=True)

        def custom_handler(loop, context):
            raise ValueError('ham')

        _context = None
        loop.set_exception_handler(custom_handler)
        with mock.patch.object(logger, 'error') as log:
            run_loop()
            log.assert_called_with(
                self.mock_pattern('Exception in default exception.*'
                                  'while handling.*in custom'),
                exc_info=True)

            # Check that original context was passed to default
            # exception handler.
            self.assertIn('context', _context)
            self.assertIs(type(_context['context']['exception']),
                          ZeroDivisionError)

    def test_big_call_later_timeout(self):
        OK, NOT_OK = 0, 0

        async def sleep(delay_name, delay):
            nonlocal OK, NOT_OK
            try:
                await asyncio.sleep(delay)
            except asyncio.CancelledError:
                OK += 1
            except Exception:
                NOT_OK += 1

        async def main():
            tests = [
                sleep("infinity", float("inf")),
                sleep("sys.maxsize", float(sys.maxsize)),
                sleep("sys.maxsize", sys.maxsize),
                sleep("2**55", 2**55),
                sleep("2**54", 2**54),
            ]
            tasks = [self.loop.create_task(test) for test in tests]
            await asyncio.sleep(0.1)
            for task in tasks:
                task.cancel()
                await task

        self.loop.run_until_complete(main())

        self.assertEqual(OK, 5)
        self.assertEqual(NOT_OK, 0)

    def test_loop_call_later_handle_when(self):
        cb = lambda: False  # NoQA
        delay = 1.0
        loop_t = self.loop.time()
        handle = self.loop.call_later(delay, cb)
        self.assertAlmostEqual(handle.when(), loop_t + delay, places=2)
        handle.cancel()
        self.assertTrue(handle.cancelled())
        self.assertAlmostEqual(handle.when(), loop_t + delay, places=2)

    def test_loop_call_later_handle_when_after_fired(self):
        fut = self.loop.create_future()
        handle = self.loop.call_later(0.05, fut.set_result, None)
        when = handle.when()
        self.loop.run_until_complete(fut)
        self.assertEqual(handle.when(), when)


class TestBaseAIO(_TestBase, AIOTestCase):
    pass


class TestPolicy(unittest.TestCase):

    def test_uvloop_policy(self):
        try:
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
            loop = asyncio.new_event_loop()
            try:
                self.assertIsInstance(loop, uvloop.Loop)
            finally:
                loop.close()
        finally:
            asyncio.set_event_loop_policy(None)

    @unittest.skipUnless(hasattr(asyncio, '_get_running_loop'),
                         'No asyncio._get_running_loop')
    def test_running_loop_within_a_loop(self):
        async def runner(loop):
            loop.run_forever()

        try:
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

            loop = asyncio.new_event_loop()
            outer_loop = asyncio.new_event_loop()

            try:
                with self.assertRaisesRegex(RuntimeError,
                                            'while another loop is running'):
                    outer_loop.run_until_complete(runner(loop))
            finally:
                loop.close()
                outer_loop.close()

        finally:
            asyncio.set_event_loop_policy(None)

    @unittest.skipUnless(hasattr(asyncio, '_get_running_loop'),
                         'No asyncio._get_running_loop')
    def test_get_event_loop_returns_running_loop(self):
        class Policy(asyncio.DefaultEventLoopPolicy):
            def get_event_loop(self):
                raise NotImplementedError

        loop = None

        old_policy = asyncio.get_event_loop_policy()
        try:
            asyncio.set_event_loop_policy(Policy())
            loop = uvloop.new_event_loop()
            self.assertIs(asyncio._get_running_loop(), None)

            async def func():
                self.assertIs(asyncio.get_event_loop(), loop)
                self.assertIs(asyncio._get_running_loop(), loop)

            loop.run_until_complete(func())
        finally:
            asyncio.set_event_loop_policy(old_policy)
            if loop is not None:
                loop.close()

        self.assertIs(asyncio._get_running_loop(), None)
```

## File: `tests/test_context.py`
```python
import asyncio
import contextvars
import decimal
import itertools
import random
import socket
import ssl
import sys
import tempfile
import unittest
import weakref

from uvloop import _testbase as tb


class _BaseProtocol(asyncio.BaseProtocol):
    def __init__(self, cvar, *, loop=None):
        self.cvar = cvar
        self.transport = None
        self.connection_made_fut = asyncio.Future(loop=loop)
        self.buffered_ctx = None
        self.data_received_fut = asyncio.Future(loop=loop)
        self.eof_received_fut = asyncio.Future(loop=loop)
        self.pause_writing_fut = asyncio.Future(loop=loop)
        self.resume_writing_fut = asyncio.Future(loop=loop)
        self.pipe_ctx = {0, 1, 2}
        self.pipe_connection_lost_fut = asyncio.Future(loop=loop)
        self.process_exited_fut = asyncio.Future(loop=loop)
        self.error_received_fut = asyncio.Future(loop=loop)
        self.connection_lost_ctx = None
        self.done = asyncio.Future(loop=loop)

    def connection_made(self, transport):
        self.transport = transport
        self.connection_made_fut.set_result(self.cvar.get())

    def connection_lost(self, exc):
        self.connection_lost_ctx = self.cvar.get()
        if exc is None:
            self.done.set_result(None)
        else:
            self.done.set_exception(exc)

    def eof_received(self):
        self.eof_received_fut.set_result(self.cvar.get())

    def pause_writing(self):
        self.pause_writing_fut.set_result(self.cvar.get())

    def resume_writing(self):
        self.resume_writing_fut.set_result(self.cvar.get())


class _Protocol(_BaseProtocol, asyncio.Protocol):
    def data_received(self, data):
        self.data_received_fut.set_result(self.cvar.get())


class _BufferedProtocol(_BaseProtocol, asyncio.BufferedProtocol):
    def get_buffer(self, sizehint):
        if self.buffered_ctx is None:
            self.buffered_ctx = self.cvar.get()
        elif self.cvar.get() != self.buffered_ctx:
            self.data_received_fut.set_exception(ValueError("{} != {}".format(
                self.buffered_ctx, self.cvar.get(),
            )))
        return bytearray(65536)

    def buffer_updated(self, nbytes):
        if not self.data_received_fut.done():
            if self.cvar.get() == self.buffered_ctx:
                self.data_received_fut.set_result(self.cvar.get())
            else:
                self.data_received_fut.set_exception(
                    ValueError("{} != {}".format(
                        self.buffered_ctx, self.cvar.get(),
                    ))
                )


class _DatagramProtocol(_BaseProtocol, asyncio.DatagramProtocol):
    def datagram_received(self, data, addr):
        self.data_received_fut.set_result(self.cvar.get())

    def error_received(self, exc):
        self.error_received_fut.set_result(self.cvar.get())


class _SubprocessProtocol(_BaseProtocol, asyncio.SubprocessProtocol):
    def pipe_data_received(self, fd, data):
        self.data_received_fut.set_result(self.cvar.get())

    def pipe_connection_lost(self, fd, exc):
        self.pipe_ctx.remove(fd)
        val = self.cvar.get()
        self.pipe_ctx.add(val)
        if not any(isinstance(x, int) for x in self.pipe_ctx):
            if len(self.pipe_ctx) == 1:
                self.pipe_connection_lost_fut.set_result(val)
            else:
                self.pipe_connection_lost_fut.set_exception(
                    AssertionError(str(list(self.pipe_ctx))))

    def process_exited(self):
        self.process_exited_fut.set_result(self.cvar.get())


class _SSLSocketOverSSL:
    # because wrap_socket() doesn't work correctly on
    # SSLSocket, we have to do the 2nd level SSL manually

    def __init__(self, ssl_sock, ctx, **kwargs):
        self.sock = ssl_sock
        self.incoming = ssl.MemoryBIO()
        self.outgoing = ssl.MemoryBIO()
        self.sslobj = ctx.wrap_bio(
            self.incoming, self.outgoing, **kwargs)
        self.do(self.sslobj.do_handshake)

    def do(self, func, *args):
        while True:
            try:
                rv = func(*args)
                break
            except ssl.SSLWantReadError:
                if self.outgoing.pending:
                    self.sock.send(self.outgoing.read())
                self.incoming.write(self.sock.recv(65536))
        if self.outgoing.pending:
            self.sock.send(self.outgoing.read())
        return rv

    def send(self, data):
        self.do(self.sslobj.write, data)

    def unwrap(self):
        self.do(self.sslobj.unwrap)

    def close(self):
        self.sock.unwrap()
        self.sock.close()


class _ContextBaseTests(tb.SSLTestCase):

    ONLYCERT = tb._cert_fullname(__file__, 'ssl_cert.pem')
    ONLYKEY = tb._cert_fullname(__file__, 'ssl_key.pem')

    def test_task_decimal_context(self):
        async def fractions(t, precision, x, y):
            with decimal.localcontext() as ctx:
                ctx.prec = precision
                a = decimal.Decimal(x) / decimal.Decimal(y)
                await asyncio.sleep(t)
                b = decimal.Decimal(x) / decimal.Decimal(y ** 2)
                return a, b

        async def main():
            r1, r2 = await asyncio.gather(
                fractions(0.1, 3, 1, 3), fractions(0.2, 6, 1, 3))

            return r1, r2

        r1, r2 = self.loop.run_until_complete(main())

        self.assertEqual(str(r1[0]), '0.333')
        self.assertEqual(str(r1[1]), '0.111')

        self.assertEqual(str(r2[0]), '0.333333')
        self.assertEqual(str(r2[1]), '0.111111')

    def test_task_context_1(self):
        cvar = contextvars.ContextVar('cvar', default='nope')

        async def sub():
            await asyncio.sleep(0.01)
            self.assertEqual(cvar.get(), 'nope')
            cvar.set('something else')

        async def main():
            self.assertEqual(cvar.get(), 'nope')
            subtask = self.loop.create_task(sub())
            cvar.set('yes')
            self.assertEqual(cvar.get(), 'yes')
            await subtask
            self.assertEqual(cvar.get(), 'yes')

        task = self.loop.create_task(main())
        self.loop.run_until_complete(task)

    def test_task_context_2(self):
        cvar = contextvars.ContextVar('cvar', default='nope')

        async def main():
            def fut_on_done(fut):
                # This change must not pollute the context
                # of the "main()" task.
                cvar.set('something else')

            self.assertEqual(cvar.get(), 'nope')

            for j in range(2):
                fut = self.loop.create_future()
                fut.add_done_callback(fut_on_done)
                cvar.set('yes{}'.format(j))
                self.loop.call_soon(fut.set_result, None)
                await fut
                self.assertEqual(cvar.get(), 'yes{}'.format(j))

                for i in range(3):
                    # Test that task passed its context to add_done_callback:
                    cvar.set('yes{}-{}'.format(i, j))
                    await asyncio.sleep(0.001)
                    self.assertEqual(cvar.get(), 'yes{}-{}'.format(i, j))

        task = self.loop.create_task(main())
        self.loop.run_until_complete(task)

        self.assertEqual(cvar.get(), 'nope')

    def test_task_context_3(self):
        cvar = contextvars.ContextVar('cvar', default=-1)

        # Run 100 Tasks in parallel, each modifying cvar.

        async def sub(num):
            for i in range(10):
                cvar.set(num + i)
                await asyncio.sleep(random.uniform(0.001, 0.05))
                self.assertEqual(cvar.get(), num + i)

        async def main():
            tasks = []
            for i in range(100):
                task = self.loop.create_task(sub(random.randint(0, 10)))
                tasks.append(task)

            await asyncio.gather(*tasks, return_exceptions=True)

        self.loop.run_until_complete(main())

        self.assertEqual(cvar.get(), -1)

    def test_task_context_4(self):
        cvar = contextvars.ContextVar('cvar', default='nope')

        class TrackMe:
            pass
        tracked = TrackMe()
        ref = weakref.ref(tracked)

        async def sub():
            cvar.set(tracked)  # NoQA
            self.loop.call_soon(lambda: None)

        async def main():
            await self.loop.create_task(sub())
            await asyncio.sleep(0.01)

        task = self.loop.create_task(main())
        self.loop.run_until_complete(task)

        del tracked
        self.assertIsNone(ref())

    def _run_test(self, method, **switches):
        switches.setdefault('use_tcp', 'both')
        use_ssl = switches.setdefault('use_ssl', 'no') in {'yes', 'both'}
        names = ['factory']
        options = [(_Protocol, _BufferedProtocol)]
        for k, v in switches.items():
            if v == 'yes':
                options.append((True,))
            elif v == 'no':
                options.append((False,))
            elif v == 'both':
                options.append((True, False))
            else:
                raise ValueError(f"Illegal {k}={v}, can only be yes/no/both")
            names.append(k)

        for combo in itertools.product(*options):
            values = dict(zip(names, combo))
            with self.subTest(**values):
                cvar = contextvars.ContextVar('cvar', default='outer')
                values['proto'] = values.pop('factory')(cvar, loop=self.loop)

                async def test():
                    self.assertEqual(cvar.get(), 'outer')
                    cvar.set('inner')
                    tmp_dir = tempfile.TemporaryDirectory()
                    if use_ssl:
                        values['sslctx'] = self._create_server_ssl_context(
                            self.ONLYCERT, self.ONLYKEY)
                        values['client_sslctx'] = \
                            self._create_client_ssl_context()
                    else:
                        values['sslctx'] = values['client_sslctx'] = None

                    if values['use_tcp']:
                        values['addr'] = ('127.0.0.1', tb.find_free_port())
                        values['family'] = socket.AF_INET
                    else:
                        values['addr'] = tmp_dir.name + '/test.sock'
                        values['family'] = socket.AF_UNIX

                    try:
                        await method(cvar=cvar, **values)
                    finally:
                        tmp_dir.cleanup()

                self.loop.run_until_complete(test())

    def _run_server_test(self, method, async_sock=False, **switches):
        async def test(sslctx, client_sslctx, addr, family, **values):
            if values['use_tcp']:
                srv = await self.loop.create_server(
                    lambda: values['proto'], *addr, ssl=sslctx)
            else:
                srv = await self.loop.create_unix_server(
                    lambda: values['proto'], addr, ssl=sslctx)
            s = socket.socket(family)

            if async_sock:
                s.setblocking(False)
                await self.loop.sock_connect(s, addr)
            else:
                await self.loop.run_in_executor(
                    None, s.connect, addr)
                if values['use_ssl']:
                    values['ssl_sock'] = await self.loop.run_in_executor(
                        None, client_sslctx.wrap_socket, s)

            try:
                await method(s=s, **values)
            finally:
                if values['use_ssl']:
                    values['ssl_sock'].close()
                s.close()
                srv.close()
                await srv.wait_closed()
        return self._run_test(test, **switches)

    def test_create_server_protocol_factory_context(self):
        async def test(cvar, proto, use_tcp, family, addr, **_):
            factory_called_future = self.loop.create_future()

            def factory():
                try:
                    self.assertEqual(cvar.get(), 'inner')
                except Exception as e:
                    factory_called_future.set_exception(e)
                else:
                    factory_called_future.set_result(None)

                return proto

            if use_tcp:
                srv = await self.loop.create_server(factory, *addr)
            else:
                srv = await self.loop.create_unix_server(factory, addr)
            s = socket.socket(family)
            with s:
                s.setblocking(False)
                await self.loop.sock_connect(s, addr)

            try:
                await factory_called_future
            finally:
                srv.close()
                await proto.done
                await srv.wait_closed()

        self._run_test(test)

    def test_create_server_connection_protocol(self):
        async def test(proto, s, **_):
            inner = await proto.connection_made_fut
            self.assertEqual(inner, "inner")

            await self.loop.sock_sendall(s, b'data')
            inner = await proto.data_received_fut
            self.assertEqual(inner, "inner")

            s.shutdown(socket.SHUT_WR)
            inner = await proto.eof_received_fut
            self.assertEqual(inner, "inner")

            s.close()
            await proto.done
            self.assertEqual(proto.connection_lost_ctx, "inner")

        self._run_server_test(test, async_sock=True)

    def test_create_ssl_server_connection_protocol(self):
        async def test(cvar, proto, ssl_sock, **_):
            def resume_reading(transport):
                cvar.set("resume_reading")
                transport.resume_reading()

            try:
                inner = await proto.connection_made_fut
                self.assertEqual(inner, "inner")

                await self.loop.run_in_executor(None, ssl_sock.send, b'data')
                inner = await proto.data_received_fut
                self.assertEqual(inner, "inner")

                if self.implementation != 'asyncio':
                    # this seems to be a bug in asyncio
                    proto.data_received_fut = self.loop.create_future()
                    proto.transport.pause_reading()
                    await self.loop.run_in_executor(None,
                                                    ssl_sock.send, b'data')
                    self.loop.call_soon(resume_reading, proto.transport)
                    inner = await proto.data_received_fut
                    self.assertEqual(inner, "inner")

                    await self.loop.run_in_executor(None, ssl_sock.unwrap)
                else:
                    ssl_sock.shutdown(socket.SHUT_WR)
                inner = await proto.eof_received_fut
                self.assertEqual(inner, "inner")

                await self.loop.run_in_executor(None, ssl_sock.close)
                await proto.done
                self.assertEqual(proto.connection_lost_ctx, "inner")
            finally:
                if self.implementation == 'asyncio':
                    # mute resource warning in asyncio
                    proto.transport.close()

        self._run_server_test(test, use_ssl='yes')

    def test_create_server_manual_connection_lost(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest('this seems to be a bug in asyncio')

        async def test(proto, cvar, **_):
            def close():
                cvar.set('closing')
                proto.transport.close()

            inner = await proto.connection_made_fut
            self.assertEqual(inner, "inner")

            self.loop.call_soon(close)

            await proto.done
            self.assertEqual(proto.connection_lost_ctx, "inner")

        self._run_server_test(test, async_sock=True)

    def test_create_ssl_server_manual_connection_lost(self):
        if self.implementation == 'asyncio' and sys.version_info >= (3, 11, 0):
            # TODO(fantix): fix for 3.11
            raise unittest.SkipTest('should pass on 3.11')

        async def test(proto, cvar, ssl_sock, **_):
            def close():
                cvar.set('closing')
                proto.transport.close()

            inner = await proto.connection_made_fut
            self.assertEqual(inner, "inner")

            if self.implementation == 'asyncio':
                self.loop.call_soon(close)
            else:
                # asyncio doesn't have the flushing phase

                # put the incoming data on-hold
                proto.transport.pause_reading()
                # send data
                await self.loop.run_in_executor(None,
                                                ssl_sock.send, b'hello')
                # schedule a proactive transport close which will trigger
                # the flushing process to retrieve the remaining data
                self.loop.call_soon(close)
                # turn off the reading lock now (this also schedules a
                # resume operation after transport.close, therefore it
                # won't affect our test)
                proto.transport.resume_reading()

            await asyncio.sleep(0)
            await self.loop.run_in_executor(None, ssl_sock.unwrap)
            await proto.done
            self.assertEqual(proto.connection_lost_ctx, "inner")
            self.assertFalse(proto.data_received_fut.done())

        self._run_server_test(test, use_ssl='yes')

    def test_create_connection_protocol(self):
        async def test(cvar, proto, addr, sslctx, client_sslctx, family,
                       use_sock, use_ssl, use_tcp):
            ss = socket.socket(family)
            ss.bind(addr)
            ss.listen(1)

            def accept():
                sock, _ = ss.accept()
                if use_ssl:
                    sock = sslctx.wrap_socket(sock, server_side=True)
                return sock

            async def write_over():
                cvar.set("write_over")
                count = 0
                if use_ssl:
                    proto.transport.set_write_buffer_limits(high=256, low=128)
                    while not proto.transport.get_write_buffer_size():
                        proto.transport.write(b'q' * 16384)
                        count += 1
                else:
                    proto.transport.set_write_buffer_limits(high=256, low=128)
                    while not proto.transport.get_write_buffer_size():
                        proto.transport.write(b'q' * 16384)
                        count += 1
                return count

            s = self.loop.run_in_executor(None, accept)

            try:
                method = ('create_connection' if use_tcp
                          else 'create_unix_connection')
                params = {}
                if use_sock:
                    cs = socket.socket(family)
                    cs.connect(addr)
                    params['sock'] = cs
                    if use_ssl:
                        params['server_hostname'] = '127.0.0.1'
                elif use_tcp:
                    params['host'] = addr[0]
                    params['port'] = addr[1]
                else:
                    params['path'] = addr
                    if use_ssl:
                        params['server_hostname'] = '127.0.0.1'
                if use_ssl:
                    params['ssl'] = client_sslctx
                await getattr(self.loop, method)(lambda: proto, **params)
                s = await s

                inner = await proto.connection_made_fut
                self.assertEqual(inner, "inner")

                await self.loop.run_in_executor(None, s.send, b'data')
                inner = await proto.data_received_fut
                self.assertEqual(inner, "inner")

                if self.implementation != 'asyncio':
                    # asyncio bug
                    count = await self.loop.create_task(write_over())
                    inner = await proto.pause_writing_fut
                    self.assertEqual(inner, "inner")

                    for i in range(count):
                        await self.loop.run_in_executor(None, s.recv, 16384)
                    inner = await proto.resume_writing_fut
                    self.assertEqual(inner, "inner")

                if use_ssl and self.implementation != 'asyncio':
                    await self.loop.run_in_executor(None, s.unwrap)
                else:
                    s.shutdown(socket.SHUT_WR)
                inner = await proto.eof_received_fut
                self.assertEqual(inner, "inner")

                s.close()
                await proto.done
                self.assertEqual(proto.connection_lost_ctx, "inner")
            finally:
                ss.close()
                proto.transport.close()

        self._run_test(test, use_sock='both', use_ssl='both')

    def test_start_tls(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest('this seems to be a bug in asyncio')

        async def test(cvar, proto, addr, sslctx, client_sslctx, family,
                       ssl_over_ssl, use_tcp, **_):
            ss = socket.socket(family)
            ss.bind(addr)
            ss.listen(1)

            def accept():
                sock, _ = ss.accept()
                sock = sslctx.wrap_socket(sock, server_side=True)
                if ssl_over_ssl:
                    sock = _SSLSocketOverSSL(sock, sslctx, server_side=True)
                return sock

            s = self.loop.run_in_executor(None, accept)
            transport = None

            try:
                if use_tcp:
                    await self.loop.create_connection(lambda: proto, *addr)
                else:
                    await self.loop.create_unix_connection(lambda: proto, addr)
                inner = await proto.connection_made_fut
                self.assertEqual(inner, "inner")

                cvar.set('start_tls')
                transport = await self.loop.start_tls(
                    proto.transport, proto, client_sslctx,
                    server_hostname='127.0.0.1',
                )

                if ssl_over_ssl:
                    cvar.set('start_tls_over_tls')
                    transport = await self.loop.start_tls(
                        transport, proto, client_sslctx,
                        server_hostname='127.0.0.1',
                    )

                s = await s

                await self.loop.run_in_executor(None, s.send, b'data')
                inner = await proto.data_received_fut
                self.assertEqual(inner, "inner")

                await self.loop.run_in_executor(None, s.unwrap)
                inner = await proto.eof_received_fut
                self.assertEqual(inner, "inner")

                s.close()
                await proto.done
                self.assertEqual(proto.connection_lost_ctx, "inner")
            finally:
                ss.close()
                if transport:
                    transport.close()

        self._run_test(test, use_ssl='yes', ssl_over_ssl='both')

    def test_connect_accepted_socket(self):
        async def test(proto, addr, family, sslctx, client_sslctx,
                       use_ssl, **_):
            ss = socket.socket(family)
            ss.bind(addr)
            ss.listen(1)
            s = self.loop.run_in_executor(None, ss.accept)
            cs = socket.socket(family)
            cs.connect(addr)
            s, _ = await s

            try:
                if use_ssl:
                    cs = self.loop.run_in_executor(
                        None, client_sslctx.wrap_socket, cs)
                    await self.loop.connect_accepted_socket(lambda: proto, s,
                                                            ssl=sslctx)
                    cs = await cs
                else:
                    await self.loop.connect_accepted_socket(lambda: proto, s)

                inner = await proto.connection_made_fut
                self.assertEqual(inner, "inner")

                await self.loop.run_in_executor(None, cs.send, b'data')
                inner = await proto.data_received_fut
                self.assertEqual(inner, "inner")

                if use_ssl and self.implementation != 'asyncio':
                    await self.loop.run_in_executor(None, cs.unwrap)
                else:
                    cs.shutdown(socket.SHUT_WR)
                inner = await proto.eof_received_fut
                self.assertEqual(inner, "inner")

                cs.close()
                await proto.done
                self.assertEqual(proto.connection_lost_ctx, "inner")
            finally:
                proto.transport.close()
                ss.close()

        self._run_test(test, use_ssl='both')

    def test_subprocess_protocol(self):
        cvar = contextvars.ContextVar('cvar', default='outer')
        proto = _SubprocessProtocol(cvar, loop=self.loop)

        async def test():
            self.assertEqual(cvar.get(), 'outer')
            cvar.set('inner')
            await self.loop.subprocess_exec(
                lambda: proto, sys.executable, b'-c',
                b';'.join((b'import sys',
                           b'data = sys.stdin.buffer.read()',
                           b'sys.stdout.buffer.write(data)')))

            try:
                inner = await proto.connection_made_fut
                self.assertEqual(inner, "inner")

                proto.transport.get_pipe_transport(0).write(b'data')
                proto.transport.get_pipe_transport(0).write_eof()
                inner = await proto.data_received_fut
                self.assertEqual(inner, "inner")

                inner = await proto.pipe_connection_lost_fut
                self.assertEqual(inner, "inner")

                inner = await proto.process_exited_fut
                if self.implementation != 'asyncio':
                    # bug in asyncio
                    self.assertEqual(inner, "inner")

                await proto.done
                if self.implementation != 'asyncio':
                    # bug in asyncio
                    self.assertEqual(proto.connection_lost_ctx, "inner")
            finally:
                proto.transport.close()

        self.loop.run_until_complete(test())

    def test_datagram_protocol(self):
        cvar = contextvars.ContextVar('cvar', default='outer')
        proto = _DatagramProtocol(cvar, loop=self.loop)
        server_addr = ('127.0.0.1', 8888)
        client_addr = ('127.0.0.1', 0)

        async def run():
            self.assertEqual(cvar.get(), 'outer')
            cvar.set('inner')

            def close():
                cvar.set('closing')
                proto.transport.close()

            try:
                await self.loop.create_datagram_endpoint(
                    lambda: proto, local_addr=server_addr)
                inner = await proto.connection_made_fut
                self.assertEqual(inner, "inner")

                s = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
                s.bind(client_addr)
                s.sendto(b'data', server_addr)
                inner = await proto.data_received_fut
                self.assertEqual(inner, "inner")

                self.loop.call_soon(close)
                await proto.done
                if self.implementation != 'asyncio':
                    # bug in asyncio
                    self.assertEqual(proto.connection_lost_ctx, "inner")
            finally:
                proto.transport.close()
                s.close()
                # let transports close
                await asyncio.sleep(0.1)

        self.loop.run_until_complete(run())


class Test_UV_Context(_ContextBaseTests, tb.UVTestCase):
    pass


class Test_AIO_Context(_ContextBaseTests, tb.AIOTestCase):
    pass
```

## File: `tests/test_cython.py`
```python
import asyncio

from uvloop._testbase import UVTestCase


class TestCythonIntegration(UVTestCase):

    def test_cython_coro_is_coroutine(self):
        from uvloop.loop import _test_coroutine_1
        from asyncio.coroutines import _format_coroutine

        coro = _test_coroutine_1()

        coro_fmt = _format_coroutine(coro)
        self.assertTrue(
            coro_fmt.startswith('_test_coroutine_1() done')
            or coro_fmt.startswith('_test_coroutine_1() running')
        )
        self.assertEqual(_test_coroutine_1.__qualname__, '_test_coroutine_1')
        self.assertEqual(_test_coroutine_1.__name__, '_test_coroutine_1')
        self.assertTrue(asyncio.iscoroutine(coro))
        fut = asyncio.ensure_future(coro)
        self.assertTrue(isinstance(fut, asyncio.Future))
        self.assertTrue(isinstance(fut, asyncio.Task))
        fut.cancel()

        with self.assertRaises(asyncio.CancelledError):
            self.loop.run_until_complete(fut)

        try:
            _format_coroutine(coro)  # This line checks against Cython segfault
        except TypeError:
            # TODO: Fix Cython to not reset __name__/__qualname__ to None
            pass
        coro.close()
```

## File: `tests/test_dealloc.py`
```python
import asyncio
import subprocess
import sys

from uvloop import _testbase as tb


class TestDealloc(tb.UVTestCase):

    def test_dealloc_1(self):
        # Somewhere between Cython 0.25.2 and 0.26.0 uvloop programs
        # started to trigger the following output:
        #
        #    $ python prog.py
        #    Error in sys.excepthook:
        #
        #    Original exception was:
        #
        # Upon some debugging, it appeared that Handle.__dealloc__ was
        # called at a time where some CPython objects become non-functional,
        # and any exception in __dealloc__ caused CPython to output the
        # above.
        #
        # This regression test starts an event loop in debug mode,
        # lets it run for a brief period of time, and exits the program.
        # This will trigger Handle.__dealloc__, CallbackHandle.__dealloc__,
        # and Loop.__dealloc__ methods.  The test will fail if they produce
        # any unwanted output.

        async def test():
            prog = '''\
import uvloop

async def foo():
    return 42

def main():
    loop = uvloop.new_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(foo())
    # Do not close the loop on purpose: let __dealloc__ methods run.

if __name__ == '__main__':
    main()
            '''

            cmd = sys.executable
            proc = await asyncio.create_subprocess_exec(
                cmd, b'-W', b'ignore', b'-c', prog,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            await proc.wait()
            out = await proc.stdout.read()
            err = await proc.stderr.read()

            return out, err

        out, err = self.loop.run_until_complete(test())
        self.assertEqual(out, b'', 'stdout is not empty')
        self.assertEqual(err, b'', 'stderr is not empty')
```

## File: `tests/test_dns.py`
```python
import asyncio
import socket
import unittest

from uvloop import _testbase as tb


def patched_getaddrinfo(*args, **kwargs):
    # corrected socket.getaddrinfo() behavior: ai_canonname always follows the
    # flag AI_CANONNAME, even if `host` is an IP
    rv = []
    result = socket.getaddrinfo(*args, **kwargs)
    first = True
    for af, sk, proto, canon_name, addr in result:
        if kwargs.get('flags', 0) & socket.AI_CANONNAME:
            if not canon_name and first:
                first = False
                canon_name = args[0]
                if not isinstance(canon_name, str):
                    canon_name = canon_name.decode('ascii')
        elif canon_name:
            canon_name = ''
        rv.append((af, sk, proto, canon_name, addr))
    return rv


class BaseTestDNS:

    def _test_getaddrinfo(self, *args, _patch=False, _sorted=False, **kwargs):
        err = None
        try:
            if _patch:
                a1 = patched_getaddrinfo(*args, **kwargs)
            else:
                a1 = socket.getaddrinfo(*args, **kwargs)
        except (socket.gaierror, UnicodeError) as ex:
            err = ex

        try:
            a2 = self.loop.run_until_complete(
                self.loop.getaddrinfo(*args, **kwargs))
        except (socket.gaierror, UnicodeError) as ex:
            if err is not None:
                self.assertEqual(ex.args, err.args)
            else:
                ex.__context__ = err
                raise ex
        except OSError as ex:
            ex.__context__ = err
            raise ex
        else:
            if err is not None:
                raise err

            if _sorted:
                if kwargs.get('flags', 0) & socket.AI_CANONNAME and a1 and a2:
                    # The API doesn't guarantee the ai_canonname value if
                    # multiple results are returned, but both implementations
                    # must return the same value for the first result.
                    self.assertEqual(a1[0][3], a2[0][3])
                    a1 = [(af, sk, pr, addr) for af, sk, pr, _, addr in a1]
                    a2 = [(af, sk, pr, addr) for af, sk, pr, _, addr in a2]

                self.assertEqual(sorted(a1), sorted(a2))
            else:
                self.assertEqual(a1, a2)

    def _test_getnameinfo(self, *args, **kwargs):
        err = None
        try:
            a1 = socket.getnameinfo(*args, **kwargs)
        except Exception as ex:
            err = ex

        try:
            a2 = self.loop.run_until_complete(
                self.loop.getnameinfo(*args, **kwargs))
        except Exception as ex:
            if err is not None:
                if ex.__class__ is not err.__class__:
                    print(ex, err)
                self.assertIs(ex.__class__, err.__class__)
                self.assertEqual(ex.args, err.args)
            else:
                raise
        else:
            if err is not None:
                raise err

            self.assertEqual(a1, a2)

    def test_getaddrinfo_1(self):
        self._test_getaddrinfo('example.com', 80, _sorted=True)
        self._test_getaddrinfo('example.com', 80, type=socket.SOCK_STREAM,
                               _sorted=True)

    def test_getaddrinfo_2(self):
        self._test_getaddrinfo('example.com', 80, flags=socket.AI_CANONNAME,
                               _sorted=True)

    def test_getaddrinfo_3(self):
        self._test_getaddrinfo('a' + '1' * 50 + '.wat', 800)

    def test_getaddrinfo_4(self):
        self._test_getaddrinfo('example.com', 80, family=-1)
        self._test_getaddrinfo('example.com', 80, type=socket.SOCK_STREAM,
                               family=-1)

    def test_getaddrinfo_5(self):
        self._test_getaddrinfo('example.com', '80', _sorted=True)
        self._test_getaddrinfo('example.com', '80', type=socket.SOCK_STREAM,
                               _sorted=True)

    def test_getaddrinfo_6(self):
        self._test_getaddrinfo(b'example.com', b'80', _sorted=True)
        self._test_getaddrinfo(b'example.com', b'80', type=socket.SOCK_STREAM,
                               _sorted=True)

    def test_getaddrinfo_7(self):
        self._test_getaddrinfo(None, 0)
        self._test_getaddrinfo(None, 0, type=socket.SOCK_STREAM)

    def test_getaddrinfo_8(self):
        self._test_getaddrinfo('', 0)
        self._test_getaddrinfo('', 0, type=socket.SOCK_STREAM)

    def test_getaddrinfo_9(self):
        self._test_getaddrinfo(b'', 0)
        self._test_getaddrinfo(b'', 0, type=socket.SOCK_STREAM)

    def test_getaddrinfo_10(self):
        self._test_getaddrinfo(None, None)
        self._test_getaddrinfo(None, None, type=socket.SOCK_STREAM)

    def test_getaddrinfo_11(self):
        self._test_getaddrinfo(b'example.com', '80', _sorted=True)
        self._test_getaddrinfo(b'example.com', '80', type=socket.SOCK_STREAM,
                               _sorted=True)

    def test_getaddrinfo_12(self):
        # musl always returns ai_canonname but we don't
        patch = self.implementation != 'asyncio'

        self._test_getaddrinfo('127.0.0.1', '80')
        self._test_getaddrinfo('127.0.0.1', '80', type=socket.SOCK_STREAM,
                               _patch=patch)

    def test_getaddrinfo_13(self):
        # musl always returns ai_canonname but we don't
        patch = self.implementation != 'asyncio'

        self._test_getaddrinfo(b'127.0.0.1', b'80')
        self._test_getaddrinfo(b'127.0.0.1', b'80', type=socket.SOCK_STREAM,
                               _patch=patch)

    def test_getaddrinfo_14(self):
        # musl always returns ai_canonname but we don't
        patch = self.implementation != 'asyncio'

        self._test_getaddrinfo(b'127.0.0.1', b'http')
        self._test_getaddrinfo(b'127.0.0.1', b'http', type=socket.SOCK_STREAM,
                               _patch=patch)

    def test_getaddrinfo_15(self):
        # musl always returns ai_canonname but we don't
        patch = self.implementation != 'asyncio'

        self._test_getaddrinfo('127.0.0.1', 'http')
        self._test_getaddrinfo('127.0.0.1', 'http', type=socket.SOCK_STREAM,
                               _patch=patch)

    def test_getaddrinfo_16(self):
        self._test_getaddrinfo('localhost', 'http')
        self._test_getaddrinfo('localhost', 'http', type=socket.SOCK_STREAM)

    def test_getaddrinfo_17(self):
        self._test_getaddrinfo(b'localhost', 'http')
        self._test_getaddrinfo(b'localhost', 'http', type=socket.SOCK_STREAM)

    def test_getaddrinfo_18(self):
        self._test_getaddrinfo('localhost', b'http')
        self._test_getaddrinfo('localhost', b'http', type=socket.SOCK_STREAM)

    def test_getaddrinfo_19(self):
        # musl always returns ai_canonname while macOS never return for IPs,
        # but we strictly follow the docs to use the AI_CANONNAME flag in a
        # shortcut __static_getaddrinfo_pyaddr()
        patch = self.implementation != 'asyncio'

        self._test_getaddrinfo('::1', 80)
        self._test_getaddrinfo('::1', 80, type=socket.SOCK_STREAM,
                               _patch=patch)
        self._test_getaddrinfo('::1', 80, type=socket.SOCK_STREAM,
                               flags=socket.AI_CANONNAME, _patch=patch)

    def test_getaddrinfo_20(self):
        # musl always returns ai_canonname while macOS never return for IPs,
        # but we strictly follow the docs to use the AI_CANONNAME flag in a
        # shortcut __static_getaddrinfo_pyaddr()
        patch = self.implementation != 'asyncio'

        self._test_getaddrinfo('127.0.0.1', 80)
        self._test_getaddrinfo('127.0.0.1', 80, type=socket.SOCK_STREAM,
                               _patch=patch)
        self._test_getaddrinfo('127.0.0.1', 80, type=socket.SOCK_STREAM,
                               flags=socket.AI_CANONNAME, _patch=patch)

    # https://github.com/libuv/libuv/security/advisories/GHSA-f74f-cvh7-c6q6
    # See also: https://github.com/MagicStack/uvloop/pull/600
    def test_getaddrinfo_21(self):
        payload = f'0x{"0" * 246}7f000001.example.com'.encode('ascii')
        self._test_getaddrinfo(payload, 80)
        self._test_getaddrinfo(payload, 80, type=socket.SOCK_STREAM)

    def test_getaddrinfo_22(self):
        payload = f'0x{"0" * 246}7f000001.example.com'
        self._test_getaddrinfo(payload, 80)
        self._test_getaddrinfo(payload, 80, type=socket.SOCK_STREAM)

    def test_getaddrinfo_broadcast(self):
        self._test_getaddrinfo('<broadcast>', 80)
        self._test_getaddrinfo('<broadcast>', 80, type=socket.SOCK_STREAM)

    ######

    def test_getnameinfo_1(self):
        self._test_getnameinfo(('127.0.0.1', 80), 0)

    def test_getnameinfo_2(self):
        self._test_getnameinfo(('127.0.0.1', 80, 1231231231213), 0)

    def test_getnameinfo_3(self):
        self._test_getnameinfo(('127.0.0.1', 80, 0, 0), 0)

    def test_getnameinfo_4(self):
        self._test_getnameinfo(('::1', 80), 0)

    def test_getnameinfo_5(self):
        self._test_getnameinfo(('localhost', 8080), 0)


class Test_UV_DNS(BaseTestDNS, tb.UVTestCase):

    def test_getaddrinfo_close_loop(self):
        # Test that we can close the loop with a running
        # DNS query.

        try:
            # Check that we have internet connection
            socket.getaddrinfo('example.com', 80)
        except socket.error:
            raise unittest.SkipTest

        async def run():
            fut = self.loop.create_task(
                self.loop.getaddrinfo('example.com', 80))
            await asyncio.sleep(0)
            fut.cancel()
            self.loop.stop()

        try:
            self.loop.run_until_complete(run())
        finally:
            self.loop.close()


class Test_AIO_DNS(BaseTestDNS, tb.AIOTestCase):
    pass
```

## File: `tests/test_executors.py`
```python
import asyncio
import concurrent.futures
import multiprocessing
import unittest

from uvloop import _testbase as tb


def fib(n):
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)


class _TestExecutors:

    def run_pool_test(self, pool_factory):
        async def run():
            pool = pool_factory()
            with pool:
                coros = []
                for i in range(0, 10):
                    coros.append(self.loop.run_in_executor(pool, fib, i))
                res = await asyncio.gather(*coros)
            self.assertEqual(res, fib10)
            await asyncio.sleep(0.01)

        fib10 = [fib(i) for i in range(10)]
        self.loop.run_until_complete(run())

    @unittest.skipIf(
        multiprocessing.get_start_method(False) == 'spawn',
        'no need to test on macOS where spawn is used instead of fork')
    def test_executors_process_pool_01(self):
        self.run_pool_test(concurrent.futures.ProcessPoolExecutor)

    def test_executors_process_pool_02(self):
        self.run_pool_test(concurrent.futures.ThreadPoolExecutor)


class TestUVExecutors(_TestExecutors, tb.UVTestCase):
    pass


class TestAIOExecutors(_TestExecutors, tb.AIOTestCase):
    pass
```

## File: `tests/test_fs_event.py`
```python
import asyncio
import contextlib
import os.path
import tempfile

from uvloop import _testbase as tb
from uvloop.loop import FileSystemEvent


class Test_UV_FS_Event(tb.UVTestCase):
    def setUp(self):
        super().setUp()
        self.exit_stack = contextlib.ExitStack()
        self.tmp_dir = self.exit_stack.enter_context(
            tempfile.TemporaryDirectory()
        )

    def tearDown(self):
        self.exit_stack.close()
        super().tearDown()

    def test_fs_event_change(self):
        change_event_count = 0
        filename = "fs_event_change.txt"
        path = os.path.join(self.tmp_dir, filename)
        q = asyncio.Queue()

        with open(path, 'wt') as f:
            async def file_writer():
                while True:
                    f.write('hello uvloop\n')
                    f.flush()
                    x = await q.get()
                    if x is None:
                        return

            def event_cb(ev_fname: bytes, evt: FileSystemEvent):
                nonlocal change_event_count
                self.assertEqual(ev_fname, filename.encode())
                self.assertEqual(evt, FileSystemEvent.CHANGE)
                change_event_count += 1
                if change_event_count < 4:
                    q.put_nowait(0)
                else:
                    q.put_nowait(None)

            h = self.loop._monitor_fs(path, event_cb)
            self.loop.run_until_complete(
                asyncio.sleep(0.1)  # let monitor start
            )
            self.assertFalse(h.cancelled())

            self.loop.run_until_complete(asyncio.wait_for(file_writer(), 4))
            h.cancel()
            self.assertTrue(h.cancelled())

        self.assertEqual(change_event_count, 4)

    def test_fs_event_rename(self):
        orig_name = "hello_fs_event.txt"
        new_name = "hello_fs_event_rename.txt"
        changed_set = {orig_name, new_name}
        event = asyncio.Event()

        async def file_renamer():
            os.rename(os.path.join(self.tmp_dir, orig_name),
                      os.path.join(self.tmp_dir, new_name))
            await event.wait()

        def event_cb(ev_fname: bytes, evt: FileSystemEvent):
            ev_fname = ev_fname.decode()
            self.assertEqual(evt, FileSystemEvent.RENAME)
            changed_set.discard(ev_fname)
            if len(changed_set) == 0:
                event.set()

        with open(os.path.join(self.tmp_dir, orig_name), 'wt') as f:
            f.write('hello!')
        h = self.loop._monitor_fs(self.tmp_dir, event_cb)
        self.loop.run_until_complete(asyncio.sleep(0.5))  # let monitor start
        self.assertFalse(h.cancelled())

        self.loop.run_until_complete(asyncio.wait_for(file_renamer(), 4))
        h.cancel()
        self.assertTrue(h.cancelled())

        self.assertEqual(len(changed_set), 0)
```

## File: `tests/test_libuv_api.py`
```python
from uvloop import _testbase as tb
from uvloop.loop import libuv_get_loop_t_ptr, libuv_get_version
from uvloop.loop import _testhelper_unwrap_capsuled_pointer as unwrap


class Test_UV_libuv(tb.UVTestCase):
    def test_libuv_get_loop_t_ptr(self):
        loop1 = self.new_loop()
        cap1 = libuv_get_loop_t_ptr(loop1)
        cap2 = libuv_get_loop_t_ptr(loop1)

        loop2 = self.new_loop()
        cap3 = libuv_get_loop_t_ptr(loop2)

        try:
            self.assertEqual(unwrap(cap1), unwrap(cap2))
            self.assertNotEqual(unwrap(cap1), unwrap(cap3))
        finally:
            loop1.close()
            loop2.close()

    def test_libuv_get_version(self):
        self.assertGreater(libuv_get_version(), 0)
```

## File: `tests/test_pipes.py`
```python
import asyncio
import io
import os
import socket

from uvloop import _testbase as tb


# All tests are copied from asyncio (mostly as-is)


class MyReadPipeProto(asyncio.Protocol):
    done = None

    def __init__(self, loop=None):
        self.state = ['INITIAL']
        self.nbytes = 0
        self.transport = None
        if loop is not None:
            self.done = asyncio.Future(loop=loop)

    def connection_made(self, transport):
        self.transport = transport
        assert self.state == ['INITIAL'], self.state
        self.state.append('CONNECTED')

    def data_received(self, data):
        assert self.state == ['INITIAL', 'CONNECTED'], self.state
        self.nbytes += len(data)

    def eof_received(self):
        assert self.state == ['INITIAL', 'CONNECTED'], self.state
        self.state.append('EOF')

    def connection_lost(self, exc):
        if 'EOF' not in self.state:
            self.state.append('EOF')  # It is okay if EOF is missed.
        assert self.state == ['INITIAL', 'CONNECTED', 'EOF'], self.state
        self.state.append('CLOSED')
        if self.done:
            self.done.set_result(None)


class MyWritePipeProto(asyncio.BaseProtocol):
    done = None
    paused = False

    def __init__(self, loop=None):
        self.state = 'INITIAL'
        self.transport = None
        if loop is not None:
            self.done = asyncio.Future(loop=loop)

    def connection_made(self, transport):
        self.transport = transport
        assert self.state == 'INITIAL', self.state
        self.state = 'CONNECTED'

    def connection_lost(self, exc):
        assert self.state == 'CONNECTED', self.state
        self.state = 'CLOSED'
        if self.done:
            self.done.set_result(None)

    def pause_writing(self):
        self.paused = True

    def resume_writing(self):
        self.paused = False


class _BasePipeTest:
    def test_read_pipe(self):
        proto = MyReadPipeProto(loop=self.loop)

        rpipe, wpipe = os.pipe()
        pipeobj = io.open(rpipe, 'rb', 1024)

        async def connect():
            t, p = await self.loop.connect_read_pipe(
                lambda: proto, pipeobj)
            self.assertIs(p, proto)
            self.assertIs(t, proto.transport)
            self.assertEqual(['INITIAL', 'CONNECTED'], proto.state)
            self.assertEqual(0, proto.nbytes)

        self.loop.run_until_complete(connect())

        os.write(wpipe, b'1')
        tb.run_until(self.loop, lambda: proto.nbytes >= 1)
        self.assertEqual(1, proto.nbytes)

        os.write(wpipe, b'2345')
        tb.run_until(self.loop, lambda: proto.nbytes >= 5)
        self.assertEqual(['INITIAL', 'CONNECTED'], proto.state)
        self.assertEqual(5, proto.nbytes)

        os.close(wpipe)
        self.loop.run_until_complete(proto.done)
        self.assertEqual(
            ['INITIAL', 'CONNECTED', 'EOF', 'CLOSED'], proto.state)
        # extra info is available
        self.assertIsNotNone(proto.transport.get_extra_info('pipe'))

    def test_read_pty_output(self):
        proto = MyReadPipeProto(loop=self.loop)

        master, slave = os.openpty()
        master_read_obj = io.open(master, 'rb', 0)

        async def connect():
            t, p = await self.loop.connect_read_pipe(
                lambda: proto, master_read_obj)
            self.assertIs(p, proto)
            self.assertIs(t, proto.transport)
            self.assertEqual(['INITIAL', 'CONNECTED'], proto.state)
            self.assertEqual(0, proto.nbytes)

        self.loop.run_until_complete(connect())

        os.write(slave, b'1')
        tb.run_until(self.loop, lambda: proto.nbytes)
        self.assertEqual(1, proto.nbytes)

        os.write(slave, b'2345')
        tb.run_until(self.loop, lambda: proto.nbytes >= 5)
        self.assertEqual(['INITIAL', 'CONNECTED'], proto.state)
        self.assertEqual(5, proto.nbytes)

        # On Linux, transport raises EIO when slave is closed --
        # ignore it.
        self.loop.set_exception_handler(lambda loop, ctx: None)
        os.close(slave)
        proto.transport.close()
        self.loop.run_until_complete(proto.done)

        self.assertEqual(
            ['INITIAL', 'CONNECTED', 'EOF', 'CLOSED'], proto.state)
        # extra info is available
        self.assertIsNotNone(proto.transport.get_extra_info('pipe'))

    def test_write_pipe(self):
        rpipe, wpipe = os.pipe()
        os.set_blocking(rpipe, False)
        pipeobj = io.open(wpipe, 'wb', 1024)

        proto = MyWritePipeProto(loop=self.loop)
        connect = self.loop.connect_write_pipe(lambda: proto, pipeobj)
        transport, p = self.loop.run_until_complete(connect)
        self.assertIs(p, proto)
        self.assertIs(transport, proto.transport)
        self.assertEqual('CONNECTED', proto.state)

        transport.write(b'1')

        data = bytearray()

        def reader(data):
            try:
                chunk = os.read(rpipe, 1024)
            except BlockingIOError:
                return len(data)
            data += chunk
            return len(data)

        tb.run_until(self.loop, lambda: reader(data) >= 1)
        self.assertEqual(b'1', data)

        transport.write(b'2345')
        tb.run_until(self.loop, lambda: reader(data) >= 5)
        self.assertEqual(b'12345', data)
        self.assertEqual('CONNECTED', proto.state)

        os.close(rpipe)

        # extra info is available
        self.assertIsNotNone(proto.transport.get_extra_info('pipe'))

        # close connection
        proto.transport.close()
        self.loop.run_until_complete(proto.done)
        self.assertEqual('CLOSED', proto.state)

    def test_write_pipe_disconnect_on_close(self):
        rsock, wsock = socket.socketpair()
        rsock.setblocking(False)

        pipeobj = io.open(wsock.detach(), 'wb', 1024)

        proto = MyWritePipeProto(loop=self.loop)
        connect = self.loop.connect_write_pipe(lambda: proto, pipeobj)
        transport, p = self.loop.run_until_complete(connect)
        self.assertIs(p, proto)
        self.assertIs(transport, proto.transport)
        self.assertEqual('CONNECTED', proto.state)

        transport.write(b'1')
        data = self.loop.run_until_complete(self.loop.sock_recv(rsock, 1024))
        self.assertEqual(b'1', data)

        rsock.close()

        self.loop.run_until_complete(proto.done)
        self.assertEqual('CLOSED', proto.state)

    def test_write_pty(self):
        master, slave = os.openpty()
        os.set_blocking(master, False)

        slave_write_obj = io.open(slave, 'wb', 0)

        proto = MyWritePipeProto(loop=self.loop)
        connect = self.loop.connect_write_pipe(lambda: proto, slave_write_obj)
        transport, p = self.loop.run_until_complete(connect)
        self.assertIs(p, proto)
        self.assertIs(transport, proto.transport)
        self.assertEqual('CONNECTED', proto.state)

        transport.write(b'1')

        data = bytearray()

        def reader(data):
            try:
                chunk = os.read(master, 1024)
            except BlockingIOError:
                return len(data)
            data += chunk
            return len(data)

        tb.run_until(self.loop, lambda: reader(data) >= 1,
                     timeout=10)
        self.assertEqual(b'1', data)

        transport.write(b'2345')
        tb.run_until(self.loop, lambda: reader(data) >= 5,
                     timeout=10)
        self.assertEqual(b'12345', data)
        self.assertEqual('CONNECTED', proto.state)

        os.close(master)

        # extra info is available
        self.assertIsNotNone(proto.transport.get_extra_info('pipe'))

        # close connection
        proto.transport.close()
        self.loop.run_until_complete(proto.done)
        self.assertEqual('CLOSED', proto.state)

    def test_write_buffer_full(self):
        rpipe, wpipe = os.pipe()
        pipeobj = io.open(wpipe, 'wb', 1024)

        proto = MyWritePipeProto(loop=self.loop)
        connect = self.loop.connect_write_pipe(lambda: proto, pipeobj)
        transport, p = self.loop.run_until_complete(connect)
        self.assertIs(p, proto)
        self.assertIs(transport, proto.transport)
        self.assertEqual('CONNECTED', proto.state)

        for i in range(32):
            transport.write(b'x' * 32768)
            if proto.paused:
                transport.write(b'x' * 32768)
                break
        else:
            self.fail("Didn't reach a full buffer")

        os.close(rpipe)
        self.loop.run_until_complete(asyncio.wait_for(proto.done, 1))
        self.assertEqual('CLOSED', proto.state)


class Test_UV_Pipes(_BasePipeTest, tb.UVTestCase):
    pass


class Test_AIO_Pipes(_BasePipeTest, tb.AIOTestCase):
    pass
```

## File: `tests/test_process.py`
```python
import asyncio
import contextlib
import gc
import os
import pathlib
import signal
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest

import psutil

from uvloop import _testbase as tb


class _RedirectFD(contextlib.AbstractContextManager):
    def __init__(self, old_file, new_file):
        self._old_fd = old_file.fileno()
        self._old_fd_save = os.dup(self._old_fd)
        self._new_fd = new_file.fileno()

    def __enter__(self):
        os.dup2(self._new_fd, self._old_fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.dup2(self._old_fd_save, self._old_fd)
        os.close(self._old_fd_save)


class _TestProcess:
    def get_num_fds(self):
        return psutil.Process(os.getpid()).num_fds()

    def test_process_env_1(self):
        async def test():
            cmd = 'echo $FOO$BAR'
            env = {'FOO': 'sp', 'BAR': 'am'}
            proc = await asyncio.create_subprocess_shell(
                cmd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            out, _ = await proc.communicate()
            self.assertEqual(out, b'spam\n')
            self.assertEqual(proc.returncode, 0)

        self.loop.run_until_complete(test())

    def test_process_env_2(self):
        async def test():
            cmd = 'env'
            env = {}  # empty environment
            proc = await asyncio.create_subprocess_exec(
                cmd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            out, _ = await proc.communicate()
            self.assertEqual(out, b'')
            self.assertEqual(proc.returncode, 0)

        self.loop.run_until_complete(test())

    def test_process_cwd_1(self):
        async def test():
            cmd = 'pwd'
            env = {}
            cwd = '/'
            proc = await asyncio.create_subprocess_shell(
                cmd,
                cwd=cwd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            out, _ = await proc.communicate()
            self.assertEqual(out, b'/\n')
            self.assertEqual(proc.returncode, 0)

        self.loop.run_until_complete(test())

    @unittest.skipUnless(hasattr(os, 'fspath'), 'no os.fspath()')
    def test_process_cwd_2(self):
        async def test():
            cmd = 'pwd'
            env = {}
            cwd = pathlib.Path('/')
            proc = await asyncio.create_subprocess_shell(
                cmd,
                cwd=cwd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            out, _ = await proc.communicate()
            self.assertEqual(out, b'/\n')
            self.assertEqual(proc.returncode, 0)

        self.loop.run_until_complete(test())

    def test_process_preexec_fn_1(self):
        # Copied from CPython/test_suprocess.py

        # DISCLAIMER: Setting environment variables is *not* a good use
        # of a preexec_fn.  This is merely a test.

        async def test():
            cmd = sys.executable
            proc = await asyncio.create_subprocess_exec(
                cmd, b'-W', b'ignore', '-c',
                'import os,sys;sys.stdout.write(os.getenv("FRUIT"))',
                stdout=subprocess.PIPE,
                preexec_fn=lambda: os.putenv("FRUIT", "apple"))

            out, _ = await proc.communicate()
            self.assertEqual(out, b'apple')
            self.assertEqual(proc.returncode, 0)

        self.loop.run_until_complete(test())

    def test_process_preexec_fn_2(self):
        # Copied from CPython/test_suprocess.py

        def raise_it():
            raise ValueError("spam")

        async def test():
            cmd = sys.executable
            proc = await asyncio.create_subprocess_exec(
                cmd, b'-W', b'ignore', '-c', 'import time; time.sleep(10)',
                preexec_fn=raise_it)

            await proc.communicate()

        started = time.time()
        try:
            self.loop.run_until_complete(test())
        except subprocess.SubprocessError as ex:
            self.assertIn('preexec_fn', ex.args[0])
            if ex.__cause__ is not None:
                # uvloop will set __cause__
                self.assertIs(type(ex.__cause__), ValueError)
                self.assertEqual(ex.__cause__.args[0], 'spam')
        else:
            self.fail(
                'exception in preexec_fn did not propagate to the parent')

        if time.time() - started > 5:
            self.fail(
                'exception in preexec_fn did not kill the child process')

    def test_process_executable_1(self):
        async def test():
            proc = await asyncio.create_subprocess_exec(
                b'doesnotexist', b'-W', b'ignore', b'-c', b'print("spam")',
                executable=sys.executable,
                stdout=subprocess.PIPE)

            out, err = await proc.communicate()
            self.assertEqual(out, b'spam\n')

        self.loop.run_until_complete(test())

    def test_process_executable_2(self):
        async def test():
            proc = await asyncio.create_subprocess_exec(
                pathlib.Path(sys.executable),
                b'-W', b'ignore', b'-c', b'print("spam")',
                stdout=subprocess.PIPE)

            out, err = await proc.communicate()
            self.assertEqual(out, b'spam\n')

        self.loop.run_until_complete(test())

    def test_process_pid_1(self):
        async def test():
            prog = '''\
import os
print(os.getpid())
            '''

            cmd = sys.executable
            proc = await asyncio.create_subprocess_exec(
                cmd, b'-W', b'ignore', b'-c', prog,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE)

            pid = proc.pid
            expected_result = '{}\n'.format(pid).encode()

            out, err = await proc.communicate()
            self.assertEqual(out, expected_result)

        self.loop.run_until_complete(test())

    def test_process_send_signal_1(self):
        async def test():
            prog = '''\
import signal

def handler(signum, frame):
    if signum == signal.SIGUSR1:
        print('WORLD')

signal.signal(signal.SIGUSR1, handler)
a = input()
print(a)
a = input()
print(a)
exit(11)
            '''

            cmd = sys.executable
            proc = await asyncio.create_subprocess_exec(
                cmd, b'-W', b'ignore', b'-c', prog,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            proc.stdin.write(b'HELLO\n')
            await proc.stdin.drain()

            self.assertEqual(await proc.stdout.readline(), b'HELLO\n')

            proc.send_signal(signal.SIGUSR1)

            proc.stdin.write(b'!\n')
            await proc.stdin.drain()

            self.assertEqual(await proc.stdout.readline(), b'WORLD\n')
            self.assertEqual(await proc.stdout.readline(), b'!\n')
            self.assertEqual(await proc.wait(), 11)

        self.loop.run_until_complete(test())

    def test_process_streams_basic_1(self):
        async def test():

            prog = '''\
import sys
while True:
    a = input()
    if a == 'stop':
        exit(20)
    elif a == 'stderr':
        print('OUCH', file=sys.stderr)
    else:
        print('>' + a + '<')
            '''

            cmd = sys.executable
            proc = await asyncio.create_subprocess_exec(
                cmd, b'-W', b'ignore', b'-c', prog,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            self.assertGreater(proc.pid, 0)
            self.assertIs(proc.returncode, None)

            transp = proc._transport
            with self.assertRaises(NotImplementedError):
                # stdin is WriteTransport
                transp.get_pipe_transport(0).pause_reading()
            with self.assertRaises((NotImplementedError, AttributeError)):
                # stdout is ReadTransport
                transp.get_pipe_transport(1).write(b'wat')

            proc.stdin.write(b'foobar\n')
            await proc.stdin.drain()
            out = await proc.stdout.readline()
            self.assertEqual(out, b'>foobar<\n')

            proc.stdin.write(b'stderr\n')
            await proc.stdin.drain()
            out = await proc.stderr.readline()
            self.assertEqual(out, b'OUCH\n')

            proc.stdin.write(b'stop\n')
            await proc.stdin.drain()

            exitcode = await proc.wait()
            self.assertEqual(exitcode, 20)

        self.loop.run_until_complete(test())

    def test_process_streams_stderr_to_stdout(self):
        async def test():
            prog = '''\
import sys
print('out', flush=True)
print('err', file=sys.stderr, flush=True)
            '''

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', prog,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)

            out, err = await proc.communicate()
            self.assertIsNone(err)
            self.assertEqual(out, b'out\nerr\n')

        self.loop.run_until_complete(test())

    def test_process_streams_devnull(self):
        async def test():
            prog = '''\
import sys
print('out', flush=True)
print('err', file=sys.stderr, flush=True)
            '''

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', prog,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)

            out, err = await proc.communicate()
            self.assertIsNone(err)
            self.assertIsNone(out)

        self.loop.run_until_complete(test())

    def test_process_streams_pass_fds(self):
        async def test():
            prog = '''\
import sys, os
assert sys.argv[1] == '--'
inherited = int(sys.argv[2])
non_inherited = int(sys.argv[3])

os.fstat(inherited)

try:
    os.fstat(non_inherited)
except:
    pass
else:
    raise RuntimeError()

print("OK")
            '''

            with tempfile.TemporaryFile() as inherited, \
                    tempfile.TemporaryFile() as non_inherited:

                proc = await asyncio.create_subprocess_exec(
                    sys.executable, b'-W', b'ignore', b'-c', prog, '--',
                    str(inherited.fileno()),
                    str(non_inherited.fileno()),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    pass_fds=(inherited.fileno(),))

                out, err = await proc.communicate()
                self.assertEqual(err, b'')
                self.assertEqual(out, b'OK\n')

        self.loop.run_until_complete(test())

    def test_subprocess_fd_leak_1(self):
        async def main(n):
            for i in range(n):
                try:
                    await asyncio.create_subprocess_exec(
                        'nonexistant',
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
                except FileNotFoundError:
                    pass
                await asyncio.sleep(0)

        self.loop.run_until_complete(main(10))
        num_fd_1 = self.get_num_fds()
        self.loop.run_until_complete(main(10))
        num_fd_2 = self.get_num_fds()

        self.assertEqual(num_fd_1, num_fd_2)

    def test_subprocess_fd_leak_2(self):
        async def main(n):
            for i in range(n):
                try:
                    p = await asyncio.create_subprocess_exec(
                        'ls',
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
                finally:
                    await p.wait()
                await asyncio.sleep(0)

        self.loop.run_until_complete(main(10))
        num_fd_1 = self.get_num_fds()
        self.loop.run_until_complete(main(10))
        num_fd_2 = self.get_num_fds()

        self.assertEqual(num_fd_1, num_fd_2)

    def test_subprocess_invalid_stdin(self):
        fd = None
        for tryfd in range(10000, 1000, -1):
            try:
                tryfd = os.dup(tryfd)
            except OSError:
                fd = tryfd
                break
            else:
                os.close(tryfd)
        else:
            self.fail('could not find a free FD')

        async def main():
            with self.assertRaises(OSError):
                await asyncio.create_subprocess_exec(
                    'ls',
                    stdin=fd)

            with self.assertRaises(OSError):
                await asyncio.create_subprocess_exec(
                    'ls',
                    stdout=fd)

            with self.assertRaises(OSError):
                await asyncio.create_subprocess_exec(
                    'ls',
                    stderr=fd)

        self.loop.run_until_complete(main())

    def test_process_streams_redirect(self):
        async def test():
            prog = bR'''
import sys
print('out', flush=True)
print('err', file=sys.stderr, flush=True)
            '''

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', prog)

            out, err = await proc.communicate()
            self.assertIsNone(out)
            self.assertIsNone(err)

        with tempfile.NamedTemporaryFile('w') as stdout:
            with tempfile.NamedTemporaryFile('w') as stderr:
                with _RedirectFD(sys.stdout, stdout):
                    with _RedirectFD(sys.stderr, stderr):
                        self.loop.run_until_complete(test())

                stdout.flush()
                stderr.flush()

                with open(stdout.name, 'rb') as so:
                    self.assertEqual(so.read(), b'out\n')

                with open(stderr.name, 'rb') as se:
                    self.assertEqual(se.read(), b'err\n')


class _AsyncioTests:

    # Program blocking
    PROGRAM_BLOCKED = [sys.executable, b'-W', b'ignore',
                       b'-c', b'import time; time.sleep(3600)']

    # Program copying input to output
    PROGRAM_CAT = [
        sys.executable, b'-c',
        b';'.join((b'import sys',
                   b'data = sys.stdin.buffer.read()',
                   b'sys.stdout.buffer.write(data)'))]

    PROGRAM_ERROR = [
        sys.executable, b'-W', b'ignore', b'-c', b'1/0'
    ]

    def test_stdin_not_inheritable(self):
        # asyncio issue #209: stdin must not be inheritable, otherwise
        # the Process.communicate() hangs
        async def len_message(message):
            code = 'import sys; data = sys.stdin.read(); print(len(data))'
            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', code,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                close_fds=False)
            stdout, stderr = await proc.communicate(message)
            exitcode = await proc.wait()
            return (stdout, exitcode)

        output, exitcode = self.loop.run_until_complete(len_message(b'abc'))
        self.assertEqual(output.rstrip(), b'3')
        self.assertEqual(exitcode, 0)

    def test_stdin_stdout_pipe(self):
        args = self.PROGRAM_CAT

        async def run(data):
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE)

            # feed data
            proc.stdin.write(data)
            await proc.stdin.drain()
            proc.stdin.close()

            # get output and exitcode
            data = await proc.stdout.read()
            exitcode = await proc.wait()
            return (exitcode, data)

        task = run(b'some data')
        task = asyncio.wait_for(task, 60.0)
        exitcode, stdout = self.loop.run_until_complete(task)
        self.assertEqual(exitcode, 0)
        self.assertEqual(stdout, b'some data')

    def test_stdin_stdout_file(self):
        args = self.PROGRAM_CAT

        async def run(data, stdout):
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdin=subprocess.PIPE,
                stdout=stdout)

            # feed data
            proc.stdin.write(data)
            await proc.stdin.drain()
            proc.stdin.close()

            exitcode = await proc.wait()
            return exitcode

        with tempfile.TemporaryFile('w+b') as new_stdout:
            task = run(b'some data', new_stdout)
            task = asyncio.wait_for(task, 60.0)
            exitcode = self.loop.run_until_complete(task)
            self.assertEqual(exitcode, 0)

            new_stdout.seek(0)
            self.assertEqual(new_stdout.read(), b'some data')

    def test_stdin_stderr_file(self):
        args = self.PROGRAM_ERROR

        async def run(stderr):
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdin=subprocess.PIPE,
                stderr=stderr)

            exitcode = await proc.wait()
            return exitcode

        with tempfile.TemporaryFile('w+b') as new_stderr:
            task = run(new_stderr)
            task = asyncio.wait_for(task, 60.0)
            exitcode = self.loop.run_until_complete(task)
            self.assertEqual(exitcode, 1)

            new_stderr.seek(0)
            self.assertIn(b'ZeroDivisionError', new_stderr.read())

    def test_communicate(self):
        args = self.PROGRAM_CAT

        async def run(data):
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE)
            stdout, stderr = await proc.communicate(data)
            return proc.returncode, stdout

        task = run(b'some data')
        task = asyncio.wait_for(task, 60.0)
        exitcode, stdout = self.loop.run_until_complete(task)
        self.assertEqual(exitcode, 0)
        self.assertEqual(stdout, b'some data')

    def test_start_new_session(self):
        # start the new process in a new session
        create = asyncio.create_subprocess_shell('exit 8',
                                                 start_new_session=True)
        proc = self.loop.run_until_complete(create)
        exitcode = self.loop.run_until_complete(proc.wait())
        self.assertEqual(exitcode, 8)

    def test_shell(self):
        create = asyncio.create_subprocess_shell('exit 7')
        proc = self.loop.run_until_complete(create)
        exitcode = self.loop.run_until_complete(proc.wait())
        self.assertEqual(exitcode, 7)

    def test_kill(self):
        args = self.PROGRAM_BLOCKED
        create = asyncio.create_subprocess_exec(*args)
        proc = self.loop.run_until_complete(create)
        proc.kill()
        returncode = self.loop.run_until_complete(proc.wait())
        self.assertEqual(-signal.SIGKILL, returncode)

    def test_terminate(self):
        args = self.PROGRAM_BLOCKED
        create = asyncio.create_subprocess_exec(*args)
        proc = self.loop.run_until_complete(create)
        proc.terminate()
        returncode = self.loop.run_until_complete(proc.wait())
        self.assertEqual(-signal.SIGTERM, returncode)

    def test_send_signal(self):
        code = 'import time; print("sleeping", flush=True); time.sleep(3600)'
        args = [sys.executable, b'-W', b'ignore', b'-c', code]
        create = asyncio.create_subprocess_exec(*args,
                                                stdout=subprocess.PIPE)
        proc = self.loop.run_until_complete(create)

        async def send_signal(proc):
            # basic synchronization to wait until the program is sleeping
            line = await proc.stdout.readline()
            self.assertEqual(line, b'sleeping\n')

            proc.send_signal(signal.SIGHUP)
            returncode = (await proc.wait())
            return returncode

        returncode = self.loop.run_until_complete(send_signal(proc))
        self.assertEqual(-signal.SIGHUP, returncode)

    def test_cancel_process_wait(self):
        # Issue #23140: cancel Process.wait()

        async def cancel_wait():
            proc = await asyncio.create_subprocess_exec(
                *self.PROGRAM_BLOCKED)

            # Create an internal future waiting on the process exit
            task = self.loop.create_task(proc.wait())
            self.loop.call_soon(task.cancel)
            try:
                await task
            except asyncio.CancelledError:
                pass

            # Cancel the future
            task.cancel()

            # Kill the process and wait until it is done
            proc.kill()
            await proc.wait()

        self.loop.run_until_complete(cancel_wait())

    def test_cancel_make_subprocess_transport_exec(self):
        async def cancel_make_transport():
            coro = asyncio.create_subprocess_exec(*self.PROGRAM_BLOCKED)
            task = self.loop.create_task(coro)

            self.loop.call_soon(task.cancel)
            try:
                await task
            except asyncio.CancelledError:
                pass

            # Give the process handler some time to close itself
            await asyncio.sleep(0.3)
            gc.collect()

        # ignore the log:
        # "Exception during subprocess creation, kill the subprocess"
        with tb.disable_logger():
            self.loop.run_until_complete(cancel_make_transport())

    def test_cancel_post_init(self):
        if sys.version_info >= (3, 13) and self.implementation == 'asyncio':
            # https://github.com/python/cpython/issues/103847#issuecomment-3736561321
            # This test started to flake on CPython 3.13 and later,
            # so we skip it for asyncio tests until the issue is resolved.
            self.skipTest('flaky test on CPython 3.13+')

        async def cancel_make_transport():
            coro = self.loop.subprocess_exec(asyncio.SubprocessProtocol,
                                             *self.PROGRAM_BLOCKED)
            task = self.loop.create_task(coro)

            self.loop.call_soon(task.cancel)
            try:
                await task
            except asyncio.CancelledError:
                pass

            # Give the process handler some time to close itself
            await asyncio.sleep(0.3)
            gc.collect()

        # ignore the log:
        # "Exception during subprocess creation, kill the subprocess"
        with tb.disable_logger():
            self.loop.run_until_complete(cancel_make_transport())
            tb.run_briefly(self.loop)

    def test_close_gets_process_closed(self):

        loop = self.loop

        class Protocol(asyncio.SubprocessProtocol):

            def __init__(self):
                self.closed = loop.create_future()

            def connection_lost(self, exc):
                self.closed.set_result(1)

        async def test_subprocess():
            transport, protocol = await loop.subprocess_exec(
                Protocol, *self.PROGRAM_BLOCKED)
            pid = transport.get_pid()
            transport.close()
            self.assertIsNone(transport.get_returncode())
            await protocol.closed
            self.assertIsNotNone(transport.get_returncode())
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)

        loop.run_until_complete(test_subprocess())

    def test_communicate_large_stdout_65536(self):
        self._test_communicate_large_stdout(65536)

    def test_communicate_large_stdout_65537(self):
        self._test_communicate_large_stdout(65537)

    def test_communicate_large_stdout_1000000(self):
        self._test_communicate_large_stdout(1000000)

    def _test_communicate_large_stdout(self, size):
        async def copy_stdin_to_stdout(stdin):
            # See https://github.com/MagicStack/uvloop/issues/363
            # A program that copies stdin to stdout character by character
            code = ('import sys, shutil; '
                    'shutil.copyfileobj(sys.stdin, sys.stdout, 1)')
            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', code,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            stdout, _stderr = await asyncio.wait_for(proc.communicate(stdin),
                                                     60.0)
            return stdout

        stdin = b'x' * size
        stdout = self.loop.run_until_complete(copy_stdin_to_stdout(stdin))
        self.assertEqual(stdout, stdin)

    def test_write_huge_stdin_8192(self):
        self._test_write_huge_stdin(8192)

    def test_write_huge_stdin_8193(self):
        self._test_write_huge_stdin(8193)

    def test_write_huge_stdin_219263(self):
        self._test_write_huge_stdin(219263)

    def test_write_huge_stdin_219264(self):
        self._test_write_huge_stdin(219264)

    def _test_write_huge_stdin(self, buf_size):
        code = '''
import sys
n = 0
while True:
    line = sys.stdin.readline()
    if not line:
        print("unexpected EOF", file=sys.stderr)
        break
    if line == "END\\n":
        break
    n+=1
print(n)'''
        num_lines = buf_size - len(b"END\n")
        args = [sys.executable, b'-W', b'ignore', b'-c', code]

        async def test():
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stdin=asyncio.subprocess.PIPE)
            data = b"\n" * num_lines + b"END\n"
            self.assertEqual(len(data), buf_size)
            proc.stdin.write(data)
            await asyncio.wait_for(proc.stdin.drain(), timeout=5.0)
            try:
                await asyncio.wait_for(proc.wait(), timeout=5.0)
            except asyncio.TimeoutError:
                proc.kill()
                proc.stdin.close()
                await proc.wait()
                raise
            out = await proc.stdout.read()
            self.assertEqual(int(out), num_lines)

        self.loop.run_until_complete(test())


class Test_UV_Process(_TestProcess, tb.UVTestCase):
    def test_process_double_close(self):
        script = textwrap.dedent("""
            import os
            import sys
            from unittest import mock

            import asyncio

            pipes = []
            original_os_pipe = os.pipe
            def log_pipes():
                pipe = original_os_pipe()
                pipes.append(pipe)
                return pipe

            dups = []
            original_os_dup = os.dup
            def log_dups(*args, **kwargs):
                dup = original_os_dup(*args, **kwargs)
                dups.append(dup)
                return dup

            with mock.patch(
                "os.close", wraps=os.close
            ) as os_close, mock.patch(
                "os.pipe", new=log_pipes
            ), mock.patch(
                "os.dup", new=log_dups
            ):
                import uvloop


            async def test():
                proc = await asyncio.create_subprocess_exec(
                    sys.executable, "-c", "pass"
                )
                await proc.communicate()

            uvloop.run(test())

            stdin, stdout, stderr = dups
            (r, w), = pipes
            assert os_close.mock_calls == [
                mock.call(w),
                mock.call(r),
                mock.call(stderr),
                mock.call(stdout),
                mock.call(stdin),
            ]
        """)
        subprocess.run([sys.executable, '-c', script], check=True)


class Test_AIO_Process(_TestProcess, tb.AIOTestCase):
    pass


class TestAsyncio_UV_Process(_AsyncioTests, tb.UVTestCase):
    pass


class TestAsyncio_AIO_Process(_AsyncioTests, tb.AIOTestCase):
    pass


class Test_UV_Process_Delayed(tb.UVTestCase):

    class TestProto:
        def __init__(self):
            self.lost = 0
            self.stages = []

        def connection_made(self, transport):
            self.stages.append(('CM', transport))

        def pipe_data_received(self, fd, data):
            if fd == 1:
                self.stages.append(('STDOUT', data))

        def pipe_connection_lost(self, fd, exc):
            if fd == 1:
                self.stages.append(('STDOUT', 'LOST'))

        def process_exited(self):
            self.stages.append('PROC_EXIT')

        def connection_lost(self, exc):
            self.stages.append(('CL', self.lost, exc))
            self.lost += 1

    async def run_sub(self, **kwargs):
        return await self.loop.subprocess_shell(
            lambda: self.TestProto(),
            'echo 1',
            **kwargs)

    def test_process_delayed_stdio__paused__stdin_pipe(self):
        transport, proto = self.loop.run_until_complete(
            self.run_sub(
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                __uvloop_sleep_after_fork=True))
        self.assertIsNot(transport, None)
        self.assertEqual(transport.get_returncode(), 0)
        self.assertEqual(
            set(proto.stages),
            {
                ('CM', transport),
                'PROC_EXIT',
                ('STDOUT', b'1\n'),
                ('STDOUT', 'LOST'),
                ('CL', 0, None)
            })

    def test_process_delayed_stdio__paused__no_stdin(self):
        transport, proto = self.loop.run_until_complete(
            self.run_sub(
                stdin=None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                __uvloop_sleep_after_fork=True))
        self.assertIsNot(transport, None)
        self.assertEqual(transport.get_returncode(), 0)
        self.assertEqual(
            set(proto.stages),
            {
                ('CM', transport),
                'PROC_EXIT',
                ('STDOUT', b'1\n'),
                ('STDOUT', 'LOST'),
                ('CL', 0, None)
            })

    def test_process_delayed_stdio__not_paused__no_stdin(self):
        if ((os.environ.get('TRAVIS_OS_NAME')
                or os.environ.get('GITHUB_WORKFLOW'))
                and sys.platform == 'darwin'):
            # Randomly crashes on Travis, can't reproduce locally.
            raise unittest.SkipTest()

        transport, proto = self.loop.run_until_complete(
            self.run_sub(
                stdin=None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE))
        self.loop.run_until_complete(transport._wait())
        self.assertEqual(transport.get_returncode(), 0)
        self.assertIsNot(transport, None)
        self.assertEqual(
            set(proto.stages),
            {
                ('CM', transport),
                'PROC_EXIT',
                ('STDOUT', b'1\n'),
                ('STDOUT', 'LOST'),
                ('CL', 0, None)
            })
```

## File: `tests/test_process_spawning.py`
```python
import asyncio
import ctypes.util
import logging
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from unittest import TestCase

import uvloop


class ProcessSpawningTestCollection(TestCase):

    def test_spawning_external_process(self):
        """Test spawning external process (using `popen` system call) that
        cause loop freeze."""

        async def run(loop):
            event = asyncio.Event()

            dummy_workers = [simulate_loop_activity(loop, event)
                             for _ in range(5)]
            spawn_worker = spawn_external_process(loop, event)
            done, pending = await asyncio.wait([
                asyncio.ensure_future(fut)
                for fut in ([spawn_worker] + dummy_workers)
            ])
            exceptions = [result.exception()
                          for result in done if result.exception()]
            if exceptions:
                raise exceptions[0]

            return True

        async def simulate_loop_activity(loop, done_event):
            """Simulate loop activity by busy waiting for event."""
            while True:
                try:
                    await asyncio.wait_for(done_event.wait(), timeout=0.1)
                except asyncio.TimeoutError:
                    pass

                if done_event.is_set():
                    return None

        async def spawn_external_process(loop, event):
            executor = ThreadPoolExecutor()
            try:
                call = loop.run_in_executor(executor, spawn_process)
                await asyncio.wait_for(call, timeout=3600)
            finally:
                event.set()
                executor.shutdown(wait=False)
            return True

        BUFFER_LENGTH = 1025
        BufferType = ctypes.c_char * (BUFFER_LENGTH - 1)

        def run_echo(popen, fread, pclose):
            fd = popen('echo test'.encode('ASCII'), 'r'.encode('ASCII'))
            try:
                while True:
                    buffer = BufferType()
                    data = ctypes.c_void_p(ctypes.addressof(buffer))

                    # -> this call will freeze whole loop in case of bug
                    read = fread(data, 1, BUFFER_LENGTH, fd)
                    if not read:
                        break
            except Exception:
                logging.getLogger().exception('read error')
                raise
            finally:
                pclose(fd)

        def spawn_process():
            """Spawn external process via `popen` system call."""

            stdio = ctypes.CDLL(ctypes.util.find_library('c'))

            # popen system call
            popen = stdio.popen
            popen.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
            popen.restype = ctypes.c_void_p

            # pclose system call
            pclose = stdio.pclose
            pclose.argtypes = (ctypes.c_void_p,)
            pclose.restype = ctypes.c_int

            # fread system call
            fread = stdio.fread
            fread.argtypes = (ctypes.c_void_p, ctypes.c_size_t,
                              ctypes.c_size_t, ctypes.c_void_p)
            fread.restype = ctypes.c_size_t

            for iteration in range(1000):
                t = Thread(target=run_echo,
                           args=(popen, fread, pclose),
                           daemon=True)
                t.start()
                t.join(timeout=10.0)
                if t.is_alive():
                    raise Exception('process freeze detected at {}'
                                    .format(iteration))

            return True

        loop = uvloop.new_event_loop()
        proc = loop.run_until_complete(run(loop))
        self.assertTrue(proc)
```

## File: `tests/test_regr1.py`
```python
import asyncio
import queue
import multiprocessing
import signal
import threading
import unittest

import uvloop

from uvloop import _testbase as tb


class EchoServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        transport.write(b'z')


class EchoClientProtocol(asyncio.Protocol):

    def __init__(self, loop):
        self.loop = loop

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.transport.close()

    def connection_lost(self, exc):
        self.loop.stop()


class FailedTestError(BaseException):
    pass


def run_server(quin, qout):
    server_loop = None

    def server_thread():
        nonlocal server_loop
        loop = server_loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)
        coro = loop.create_server(EchoServerProtocol, '127.0.0.1', 0)
        server = loop.run_until_complete(coro)
        addr = server.sockets[0].getsockname()
        qout.put(addr)
        loop.run_forever()
        server.close()
        loop.run_until_complete(server.wait_closed())
        try:
            loop.close()
        except Exception as exc:
            print(exc)
        qout.put('stopped')

    thread = threading.Thread(target=server_thread, daemon=True)
    thread.start()

    quin.get()
    server_loop.call_soon_threadsafe(server_loop.stop)
    thread.join(1)


class TestIssue39Regr(tb.UVTestCase):
    """See https://github.com/MagicStack/uvloop/issues/39 for details.

    Original code to reproduce the bug is by Jim Fulton.
    """

    def on_alarm(self, sig, fr):
        if self.running:
            raise FailedTestError

    def run_test(self):
        for i in range(10):
            for threaded in [True, False]:
                if threaded:
                    qin, qout = queue.Queue(), queue.Queue()
                    threading.Thread(
                        target=run_server,
                        args=(qin, qout),
                        daemon=True).start()
                else:
                    qin = multiprocessing.Queue()
                    qout = multiprocessing.Queue()
                    multiprocessing.Process(
                        target=run_server,
                        args=(qin, qout),
                        daemon=True).start()

                addr = qout.get()
                loop = self.new_loop()
                asyncio.set_event_loop(loop)
                loop.create_task(
                    loop.create_connection(
                        lambda: EchoClientProtocol(loop),
                        host=addr[0], port=addr[1]))
                loop.run_forever()
                loop.close()
                qin.put('stop')
                qout.get()

    @unittest.skipIf(
        multiprocessing.get_start_method(False) == 'spawn',
        'no need to test on macOS where spawn is used instead of fork')
    def test_issue39_regression(self):
        signal.signal(signal.SIGALRM, self.on_alarm)
        signal.alarm(5)

        try:
            self.running = True
            self.run_test()
        except FailedTestError:
            self.fail('deadlocked in libuv')
        finally:
            self.running = False
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
```

## File: `tests/test_runner.py`
```python
import asyncio
import unittest
import uvloop


class TestSourceCode(unittest.TestCase):

    def test_uvloop_run_1(self):
        CNT = 0

        async def main():
            nonlocal CNT
            CNT += 1

            loop = asyncio.get_running_loop()

            self.assertTrue(isinstance(loop, uvloop.Loop))
            self.assertTrue(loop.get_debug())

            return 'done'

        result = uvloop.run(main(), debug=True)

        self.assertEqual(result, 'done')
        self.assertEqual(CNT, 1)

    def test_uvloop_run_2(self):

        async def main():
            pass

        coro = main()
        with self.assertRaisesRegex(TypeError, ' a non-uvloop event loop'):
            uvloop.run(
                coro,
                loop_factory=asyncio.DefaultEventLoopPolicy().new_event_loop,
            )

        coro.close()
```

## File: `tests/test_signals.py`
```python
import asyncio
import signal
import subprocess
import sys
import time

from uvloop import _testbase as tb

DELAY = 0.1


class _TestSignal:
    NEW_LOOP = None

    @tb.silence_long_exec_warning()
    def test_signals_sigint_pycode_stop(self):
        async def runner():
            PROG = R"""\
import asyncio
import uvloop
import time

from uvloop import _testbase as tb

async def worker():
    print('READY', flush=True)
    time.sleep(200)

@tb.silence_long_exec_warning()
def run():
    loop = """ + self.NEW_LOOP + """
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(worker())
    finally:
        loop.close()

run()
"""

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', PROG,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            await proc.stdout.readline()
            time.sleep(DELAY)
            proc.send_signal(signal.SIGINT)
            out, err = await proc.communicate()
            self.assertIn(b'KeyboardInterrupt', err)
            self.assertEqual(out, b'')

        self.loop.run_until_complete(runner())

    @tb.silence_long_exec_warning()
    def test_signals_sigint_pycode_continue(self):
        async def runner():
            PROG = R"""\
import asyncio
import uvloop
import time

from uvloop import _testbase as tb

async def worker():
    print('READY', flush=True)
    try:
        time.sleep(200)
    except KeyboardInterrupt:
        print("oups")
    await asyncio.sleep(0.5)
    print('done')

@tb.silence_long_exec_warning()
def run():
    loop = """ + self.NEW_LOOP + """
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(worker())
    finally:
        loop.close()

run()
"""

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', PROG,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            await proc.stdout.readline()
            time.sleep(DELAY)
            proc.send_signal(signal.SIGINT)
            out, err = await proc.communicate()
            self.assertEqual(err, b'')
            self.assertEqual(out, b'oups\ndone\n')

        self.loop.run_until_complete(runner())

    @tb.silence_long_exec_warning()
    def test_signals_sigint_uvcode(self):
        async def runner():
            PROG = R"""\
import asyncio
import uvloop

srv = None

async def worker():
    global srv
    cb = lambda *args: None
    srv = await asyncio.start_server(cb, '127.0.0.1', 0)
    print('READY', flush=True)

loop = """ + self.NEW_LOOP + """
asyncio.set_event_loop(loop)
loop.create_task(worker())
try:
    loop.run_forever()
finally:
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.close()
"""

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', PROG,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            await proc.stdout.readline()
            time.sleep(DELAY)
            proc.send_signal(signal.SIGINT)
            out, err = await proc.communicate()
            self.assertIn(b'KeyboardInterrupt', err)

        self.loop.run_until_complete(runner())

    @tb.silence_long_exec_warning()
    def test_signals_sigint_uvcode_two_loop_runs(self):
        async def runner():
            PROG = R"""\
import asyncio
import uvloop

srv = None

async def worker():
    global srv
    cb = lambda *args: None
    srv = await asyncio.start_server(cb, '127.0.0.1', 0)

loop = """ + self.NEW_LOOP + """
asyncio.set_event_loop(loop)
loop.run_until_complete(worker())
print('READY', flush=True)
try:
    loop.run_forever()
finally:
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.close()
"""

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', PROG,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            await proc.stdout.readline()
            time.sleep(DELAY)
            proc.send_signal(signal.SIGINT)
            out, err = await proc.communicate()
            self.assertIn(b'KeyboardInterrupt', err)

        self.loop.run_until_complete(runner())

    @tb.silence_long_exec_warning()
    def test_signals_sigint_and_custom_handler(self):
        async def runner():
            PROG = R"""\
import asyncio
import signal
import uvloop

srv = None

async def worker():
    global srv
    cb = lambda *args: None
    srv = await asyncio.start_server(cb, '127.0.0.1', 0)
    print('READY', flush=True)

def handler_sig(say):
    print(say, flush=True)
    exit()

def handler_hup(say):
    print(say, flush=True)

loop = """ + self.NEW_LOOP + """
loop.add_signal_handler(signal.SIGINT, handler_sig, '!s-int!')
loop.add_signal_handler(signal.SIGHUP, handler_hup, '!s-hup!')
asyncio.set_event_loop(loop)
loop.create_task(worker())
try:
    loop.run_forever()
finally:
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.close()
"""

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', PROG,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            await proc.stdout.readline()
            time.sleep(DELAY)
            proc.send_signal(signal.SIGHUP)
            time.sleep(DELAY)
            proc.send_signal(signal.SIGINT)
            out, err = await proc.communicate()
            self.assertEqual(err, b'')
            self.assertIn(b'!s-hup!', out)
            self.assertIn(b'!s-int!', out)

        self.loop.run_until_complete(runner())

    @tb.silence_long_exec_warning()
    def test_signals_and_custom_handler_1(self):
        async def runner():
            PROG = R"""\
import asyncio
import signal
import uvloop

srv = None

async def worker():
    global srv
    cb = lambda *args: None
    srv = await asyncio.start_server(cb, '127.0.0.1', 0)
    print('READY', flush=True)

def handler1():
    print("GOTIT", flush=True)

def handler2():
    assert loop.remove_signal_handler(signal.SIGUSR1)
    print("REMOVED", flush=True)

def handler_hup():
    exit()

loop = """ + self.NEW_LOOP + """
asyncio.set_event_loop(loop)
loop.add_signal_handler(signal.SIGUSR1, handler1)
loop.add_signal_handler(signal.SIGUSR2, handler2)
loop.add_signal_handler(signal.SIGHUP, handler_hup)
loop.create_task(worker())
try:
    loop.run_forever()
finally:
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.close()

"""

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', PROG,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            await proc.stdout.readline()

            time.sleep(DELAY)
            proc.send_signal(signal.SIGUSR1)
            time.sleep(DELAY)
            proc.send_signal(signal.SIGUSR1)
            time.sleep(DELAY)
            proc.send_signal(signal.SIGUSR2)
            time.sleep(DELAY)
            proc.send_signal(signal.SIGUSR1)
            time.sleep(DELAY)
            proc.send_signal(signal.SIGUSR1)
            time.sleep(DELAY)
            proc.send_signal(signal.SIGHUP)

            out, err = await proc.communicate()
            self.assertEqual(err, b'')
            self.assertEqual(b'GOTIT\nGOTIT\nREMOVED\n', out)

        self.loop.run_until_complete(runner())

    def test_signals_invalid_signal(self):
        with self.assertRaisesRegex(RuntimeError,
                                    'sig {} cannot be caught'.format(
                                        signal.SIGKILL)):

            self.loop.add_signal_handler(signal.SIGKILL, lambda *a: None)

    def test_signals_coro_callback(self):
        async def coro():
            pass
        with self.assertRaisesRegex(TypeError, 'coroutines cannot be used'):
            self.loop.add_signal_handler(signal.SIGHUP, coro)

    def test_signals_wakeup_fd_unchanged(self):
        async def runner():
            PROG = R"""\
import uvloop
import signal
import asyncio


def get_wakeup_fd():
    fd = signal.set_wakeup_fd(-1)
    signal.set_wakeup_fd(fd)
    return fd

async def f(): pass

fd0 = get_wakeup_fd()
loop = """ + self.NEW_LOOP + """
try:
    asyncio.set_event_loop(loop)
    loop.run_until_complete(f())
    fd1 = get_wakeup_fd()
finally:
    loop.close()

print(fd0 == fd1, flush=True)

"""

            proc = await asyncio.create_subprocess_exec(
                sys.executable, b'-W', b'ignore', b'-c', PROG,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

            out, err = await proc.communicate()
            self.assertEqual(err, b'')
            self.assertIn(b'True', out)

        self.loop.run_until_complete(runner())

    def test_signals_fork_in_thread(self):
        # Refs #452, when forked from a thread, the main-thread-only signal
        # operations failed thread ID checks because we didn't update
        # MAIN_THREAD_ID after fork. It's now a lazy value set when needed and
        # cleared after fork.
        PROG = R"""\
import asyncio
import multiprocessing
import signal
import sys
import threading
import uvloop

multiprocessing.set_start_method('fork')

def subprocess():
    loop = """ + self.NEW_LOOP + """
    loop.add_signal_handler(signal.SIGINT, lambda *a: None)

def run():
    loop = """ + self.NEW_LOOP + """
    loop.add_signal_handler(signal.SIGINT, lambda *a: None)
    p = multiprocessing.Process(target=subprocess)
    t = threading.Thread(target=p.start)
    t.start()
    t.join()
    p.join()
    sys.exit(p.exitcode)

run()
"""

        subprocess.check_call([
            sys.executable, b'-W', b'ignore', b'-c', PROG,
        ])


class Test_UV_Signals(_TestSignal, tb.UVTestCase):
    NEW_LOOP = 'uvloop.new_event_loop()'

    def test_signals_no_SIGCHLD(self):
        with self.assertRaisesRegex(RuntimeError,
                                    r"cannot add.*handler.*SIGCHLD"):

            self.loop.add_signal_handler(signal.SIGCHLD, lambda *a: None)


class Test_AIO_Signals(_TestSignal, tb.AIOTestCase):
    NEW_LOOP = 'asyncio.new_event_loop()'
```

## File: `tests/test_sockets.py`
```python
import asyncio
import pickle
import select
import socket
import sys
import time
import unittest

from uvloop import _testbase as tb


_SIZE = 1024 * 1024


class _TestSockets:

    async def recv_all(self, sock, nbytes):
        buf = b''
        while len(buf) < nbytes:
            buf += await self.loop.sock_recv(sock, nbytes - len(buf))
        return buf

    def test_socket_accept_recv_send(self):
        async def server():
            sock = socket.socket()
            sock.setblocking(False)

            with sock:
                sock.bind(('127.0.0.1', 0))
                sock.listen()

                fut = self.loop.run_in_executor(None, client,
                                                sock.getsockname())

                client_sock, _ = await self.loop.sock_accept(sock)

                with client_sock:
                    data = await self.recv_all(client_sock, _SIZE)
                    self.assertEqual(data, b'a' * _SIZE)

                await fut

        def client(addr):
            sock = socket.socket()
            with sock:
                sock.connect(addr)
                sock.sendall(b'a' * _SIZE)

        self.loop.run_until_complete(server())

    def test_socket_failed_connect(self):
        sock = socket.socket()
        with sock:
            sock.bind(('127.0.0.1', 0))
            addr = sock.getsockname()

        async def run():
            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                with self.assertRaises(ConnectionRefusedError):
                    await self.loop.sock_connect(sock, addr)

        self.loop.run_until_complete(run())

    @unittest.skipUnless(tb.has_IPv6, 'no IPv6')
    def test_socket_ipv6_addr(self):
        server_sock = socket.socket(socket.AF_INET6)
        with server_sock:
            server_sock.bind(('::1', 0))

            addr = server_sock.getsockname()  # tuple of 4 elements for IPv6

            async def run():
                sock = socket.socket(socket.AF_INET6)
                with sock:
                    sock.setblocking(False)
                    # Check that sock_connect accepts 4-element address tuple
                    # for IPv6 sockets.
                    f = self.loop.sock_connect(sock, addr)
                    try:
                        await asyncio.wait_for(f, timeout=0.1)
                    except (asyncio.TimeoutError, ConnectionRefusedError):
                        # TimeoutError is expected.
                        pass

            self.loop.run_until_complete(run())

    def test_socket_ipv4_nameaddr(self):
        async def run():
            sock = socket.socket(socket.AF_INET)
            with sock:
                sock.setblocking(False)
                await self.loop.sock_connect(sock, ('localhost', 0))

        with self.assertRaises(OSError):
            # Regression test: sock_connect(sock) wasn't calling
            # getaddrinfo() with `family=sock.family`, which resulted
            # in `socket.connect()` being called with an IPv6 address
            # for IPv4 sockets, which used to cause a TypeError.
            # Here we expect that that is fixed so we should get an
            # OSError instead.
            self.loop.run_until_complete(run())

    def test_socket_blocking_error(self):
        self.loop.set_debug(True)
        sock = socket.socket()

        with sock:
            with self.assertRaisesRegex(ValueError, 'must be non-blocking'):
                self.loop.run_until_complete(
                    self.loop.sock_recv(sock, 0))

            with self.assertRaisesRegex(ValueError, 'must be non-blocking'):
                self.loop.run_until_complete(
                    self.loop.sock_sendall(sock, b''))

            with self.assertRaisesRegex(ValueError, 'must be non-blocking'):
                self.loop.run_until_complete(
                    self.loop.sock_accept(sock))

            with self.assertRaisesRegex(ValueError, 'must be non-blocking'):
                self.loop.run_until_complete(
                    self.loop.sock_connect(sock, (b'', 0)))

    def test_socket_fileno(self):
        rsock, wsock = socket.socketpair()
        f = asyncio.Future(loop=self.loop)

        def reader():
            rsock.recv(100)
            # We are done: unregister the file descriptor
            self.loop.remove_reader(rsock)
            f.set_result(None)

        def writer():
            wsock.send(b'abc')
            self.loop.remove_writer(wsock)

        with rsock, wsock:
            self.loop.add_reader(rsock, reader)
            self.loop.add_writer(wsock, writer)
            self.loop.run_until_complete(f)

    def test_socket_sync_remove_and_immediately_close(self):
        # Test that it's OK to close the socket right after calling
        # `remove_reader`.
        sock = socket.socket()
        with sock:
            cb = lambda: None

            sock.bind(('127.0.0.1', 0))
            sock.listen(0)
            fd = sock.fileno()
            self.loop.add_reader(fd, cb)
            self.loop.run_until_complete(asyncio.sleep(0.01))
            self.loop.remove_reader(fd)
            sock.close()
            self.assertEqual(sock.fileno(), -1)
            self.loop.run_until_complete(asyncio.sleep(0.01))

    def test_sock_cancel_add_reader_race(self):
        if self.is_asyncio_loop() and sys.version_info[:2] == (3, 8):
            # asyncio 3.8.x has a regression; fixed in 3.9.0
            # tracked in https://bugs.python.org/issue30064
            raise unittest.SkipTest()

        srv_sock_conn = None

        async def server():
            nonlocal srv_sock_conn
            sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_server.setblocking(False)
            with sock_server:
                sock_server.bind(('127.0.0.1', 0))
                sock_server.listen()
                fut = asyncio.ensure_future(
                    client(sock_server.getsockname()))
                srv_sock_conn, _ = await self.loop.sock_accept(sock_server)
                srv_sock_conn.setsockopt(
                    socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                with srv_sock_conn:
                    await fut

        async def client(addr):
            sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_client.setblocking(False)
            with sock_client:
                await self.loop.sock_connect(sock_client, addr)
                _, pending_read_futs = await asyncio.wait(
                    [
                        asyncio.ensure_future(
                            self.loop.sock_recv(sock_client, 1)
                        )
                    ],
                    timeout=1,
                )

                async def send_server_data():
                    # Wait a little bit to let reader future cancel and
                    # schedule the removal of the reader callback.  Right after
                    # "rfut.cancel()" we will call "loop.sock_recv()", which
                    # will add a reader.  This will make a race between
                    # remove- and add-reader.
                    await asyncio.sleep(0.1)
                    await self.loop.sock_sendall(srv_sock_conn, b'1')
                self.loop.create_task(send_server_data())

                for rfut in pending_read_futs:
                    rfut.cancel()

                data = await self.loop.sock_recv(sock_client, 1)

                self.assertEqual(data, b'1')

        self.loop.run_until_complete(server())

    def test_sock_send_before_cancel(self):
        if self.is_asyncio_loop() and sys.version_info[:2] == (3, 8):
            # asyncio 3.8.x has a regression; fixed in 3.9.0
            # tracked in https://bugs.python.org/issue30064
            raise unittest.SkipTest()

        srv_sock_conn = None

        async def server():
            nonlocal srv_sock_conn
            sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_server.setblocking(False)
            with sock_server:
                sock_server.bind(('127.0.0.1', 0))
                sock_server.listen()
                fut = asyncio.ensure_future(
                    client(sock_server.getsockname()))
                srv_sock_conn, _ = await self.loop.sock_accept(sock_server)
                with srv_sock_conn:
                    await fut

        async def client(addr):
            await asyncio.sleep(0.01)
            sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_client.setblocking(False)
            with sock_client:
                await self.loop.sock_connect(sock_client, addr)
                _, pending_read_futs = await asyncio.wait(
                    [
                        asyncio.ensure_future(
                            self.loop.sock_recv(sock_client, 1)
                        )
                    ],
                    timeout=1,
                )

                # server can send the data in a random time, even before
                # the previous result future has cancelled.
                await self.loop.sock_sendall(srv_sock_conn, b'1')

                for rfut in pending_read_futs:
                    rfut.cancel()

                data = await self.loop.sock_recv(sock_client, 1)

                self.assertEqual(data, b'1')

        self.loop.run_until_complete(server())


class TestUVSockets(_TestSockets, tb.UVTestCase):

    @unittest.skipUnless(hasattr(select, 'epoll'), 'Linux only test')
    def test_socket_sync_remove(self):
        # See https://github.com/MagicStack/uvloop/issues/61 for details

        sock = socket.socket()
        epoll = select.epoll.fromfd(self.loop._get_backend_id())

        try:
            cb = lambda: None

            sock.bind(('127.0.0.1', 0))
            sock.listen(0)
            fd = sock.fileno()
            self.loop.add_reader(fd, cb)
            self.loop.run_until_complete(asyncio.sleep(0.01))
            self.loop.remove_reader(fd)
            with self.assertRaises(FileNotFoundError):
                epoll.modify(fd, 0)

        finally:
            sock.close()
            self.loop.close()
            epoll.close()

    def test_add_reader_or_writer_transport_fd(self):
        def assert_raises():
            return self.assertRaisesRegex(
                RuntimeError,
                r'File descriptor .* is used by transport')

        async def runner():
            tr, pr = await self.loop.create_connection(
                lambda: asyncio.Protocol(), sock=rsock)

            try:
                cb = lambda: None
                sock = tr.get_extra_info('socket')

                with assert_raises():
                    self.loop.add_reader(sock, cb)
                with assert_raises():
                    self.loop.add_reader(sock.fileno(), cb)

                with assert_raises():
                    self.loop.remove_reader(sock)
                with assert_raises():
                    self.loop.remove_reader(sock.fileno())

                with assert_raises():
                    self.loop.add_writer(sock, cb)
                with assert_raises():
                    self.loop.add_writer(sock.fileno(), cb)

                with assert_raises():
                    self.loop.remove_writer(sock)
                with assert_raises():
                    self.loop.remove_writer(sock.fileno())

            finally:
                tr.close()

        rsock, wsock = socket.socketpair()
        try:
            self.loop.run_until_complete(runner())
        finally:
            rsock.close()
            wsock.close()

    def test_pseudosocket(self):
        def assert_raises():
            return self.assertRaisesRegex(
                RuntimeError,
                r'File descriptor .* is used by transport')

        def test_pseudo(real_sock, pseudo_sock, *, is_dup=False):
            self.assertIn('AF_UNIX', repr(pseudo_sock))

            self.assertEqual(pseudo_sock.family, real_sock.family)
            self.assertEqual(pseudo_sock.proto, real_sock.proto)

            # Guard against SOCK_NONBLOCK bit in socket.type on Linux.
            self.assertEqual(pseudo_sock.type & 0xf, real_sock.type & 0xf)

            with self.assertRaises(TypeError):
                pickle.dumps(pseudo_sock)

            na_meths = {
                'accept', 'connect', 'connect_ex', 'bind', 'listen',
                'makefile', 'sendfile', 'close', 'detach', 'shutdown',
                'sendmsg_afalg', 'sendmsg', 'sendto', 'send', 'sendall',
                'recv_into', 'recvfrom_into', 'recvmsg_into', 'recvmsg',
                'recvfrom', 'recv'
            }
            for methname in na_meths:
                meth = getattr(pseudo_sock, methname)
                with self.assertRaisesRegex(
                        TypeError,
                        r'.*not support ' + methname + r'\(\) method'):
                    meth()

            eq_meths = {
                'getsockname', 'getpeername', 'get_inheritable', 'gettimeout'
            }
            for methname in eq_meths:
                pmeth = getattr(pseudo_sock, methname)
                rmeth = getattr(real_sock, methname)

                # Call 2x to check caching paths
                self.assertEqual(pmeth(), rmeth())
                self.assertEqual(pmeth(), rmeth())

            self.assertEqual(
                pseudo_sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR),
                0)

            if not is_dup:
                self.assertEqual(pseudo_sock.fileno(), real_sock.fileno())

                duped = pseudo_sock.dup()
                with duped:
                    test_pseudo(duped, pseudo_sock, is_dup=True)

            with self.assertRaises(TypeError):
                with pseudo_sock:
                    pass

        async def runner():
            tr, pr = await self.loop.create_connection(
                lambda: asyncio.Protocol(), sock=rsock)

            try:
                sock = tr.get_extra_info('socket')
                test_pseudo(rsock, sock)
            finally:
                tr.close()

        rsock, wsock = socket.socketpair()
        try:
            self.loop.run_until_complete(runner())
        finally:
            rsock.close()
            wsock.close()

    def test_socket_connect_and_close(self):
        def srv_gen(sock):
            sock.send(b'helo')

        async def client(sock, addr):
            f = asyncio.ensure_future(self.loop.sock_connect(sock, addr),
                                      loop=self.loop)
            self.loop.call_soon(sock.close)
            await f
            return 'ok'

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                r = self.loop.run_until_complete(client(sock, srv.addr))
                self.assertEqual(r, 'ok')

    def test_socket_recv_and_close(self):
        def srv_gen(sock):
            time.sleep(1.2)
            sock.send(b'helo')

        async def kill(sock):
            await asyncio.sleep(0.2)
            sock.close()

        async def client(sock, addr):
            await self.loop.sock_connect(sock, addr)

            f = asyncio.ensure_future(self.loop.sock_recv(sock, 10),
                                      loop=self.loop)
            self.loop.create_task(kill(sock))
            res = await f
            self.assertEqual(sock.fileno(), -1)
            return res

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                c = client(sock, srv.addr)
                w = asyncio.wait_for(c, timeout=5.0)
                r = self.loop.run_until_complete(w)
                self.assertEqual(r, b'helo')

    def test_socket_recv_into_and_close(self):
        def srv_gen(sock):
            time.sleep(1.2)
            sock.send(b'helo')

        async def kill(sock):
            await asyncio.sleep(0.2)
            sock.close()

        async def client(sock, addr):
            await self.loop.sock_connect(sock, addr)

            data = bytearray(10)
            with memoryview(data) as buf:
                f = asyncio.ensure_future(self.loop.sock_recv_into(sock, buf),
                                          loop=self.loop)
                self.loop.create_task(kill(sock))
                rcvd = await f
                data = data[:rcvd]
            self.assertEqual(sock.fileno(), -1)
            return bytes(data)

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                c = client(sock, srv.addr)
                w = asyncio.wait_for(c, timeout=5.0)
                r = self.loop.run_until_complete(w)
                self.assertEqual(r, b'helo')

    def test_socket_send_and_close(self):
        ok = False

        def srv_gen(sock):
            nonlocal ok
            b = sock.recv_all(2)
            if b == b'hi':
                ok = True
            sock.send(b'ii')

        async def client(sock, addr):
            await self.loop.sock_connect(sock, addr)

            s2 = sock.dup()  # Don't let it drop connection until `f` is done
            with s2:
                f = asyncio.ensure_future(self.loop.sock_sendall(sock, b'hi'),
                                          loop=self.loop)
                self.loop.call_soon(sock.close)
                await f

                return await self.loop.sock_recv(s2, 2)

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                r = self.loop.run_until_complete(client(sock, srv.addr))
                self.assertEqual(r, b'ii')

        self.assertTrue(ok)

    def test_socket_close_loop_and_close(self):
        class Abort(Exception):
            pass

        def srv_gen(sock):
            time.sleep(1.2)

        async def client(sock, addr):
            await self.loop.sock_connect(sock, addr)

            asyncio.ensure_future(self.loop.sock_recv(sock, 10),
                                  loop=self.loop)
            await asyncio.sleep(0.2)
            raise Abort

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)

                c = client(sock, srv.addr)
                w = asyncio.wait_for(c, timeout=5.0)
                try:
                    sock = self.loop.run_until_complete(w)
                except Abort:
                    pass

                # `loop` still owns `sock`, so closing `sock` shouldn't
                # do anything.
                sock.close()
                self.assertNotEqual(sock.fileno(), -1)

                # `loop.close()` should io-decref all sockets that the
                # loop owns, including our `sock`.
                self.loop.close()
                self.assertEqual(sock.fileno(), -1)

    def test_socket_close_remove_reader(self):
        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_reader(s, lambda: None)
            self.loop.remove_reader(s.fileno())
            s.close()
            self.assertEqual(s.fileno(), -1)

        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_reader(s.fileno(), lambda: None)
            self.loop.remove_reader(s)
            self.assertNotEqual(s.fileno(), -1)
            s.close()
            self.assertEqual(s.fileno(), -1)

    def test_socket_close_remove_writer(self):
        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_writer(s, lambda: None)
            self.loop.remove_writer(s.fileno())
            s.close()
            self.assertEqual(s.fileno(), -1)

        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_writer(s.fileno(), lambda: None)
            self.loop.remove_writer(s)
            self.assertNotEqual(s.fileno(), -1)
            s.close()
            self.assertEqual(s.fileno(), -1)

    def test_socket_cancel_sock_recv_1(self):
        def srv_gen(sock):
            time.sleep(1.2)
            sock.send(b'helo')

        async def kill(fut):
            await asyncio.sleep(0.2)
            fut.cancel()

        async def client(sock, addr):
            await self.loop.sock_connect(sock, addr)

            f = asyncio.ensure_future(self.loop.sock_recv(sock, 10),
                                      loop=self.loop)
            self.loop.create_task(kill(f))
            with self.assertRaises(asyncio.CancelledError):
                await f
            sock.close()
            self.assertEqual(sock.fileno(), -1)

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                c = client(sock, srv.addr)
                w = asyncio.wait_for(c, timeout=5.0)
                self.loop.run_until_complete(w)

    def test_socket_cancel_sock_recv_2(self):
        def srv_gen(sock):
            time.sleep(1.2)
            sock.send(b'helo')

        async def kill(fut):
            await asyncio.sleep(0.5)
            fut.cancel()

        async def recv(sock):
            fut = self.loop.create_task(self.loop.sock_recv(sock, 10))
            await asyncio.sleep(0.1)
            self.loop.remove_reader(sock)
            sock.close()
            try:
                await fut
            except asyncio.CancelledError:
                raise
            finally:
                sock.close()

        async def client(sock, addr):
            await self.loop.sock_connect(sock, addr)

            f = asyncio.ensure_future(recv(sock))
            self.loop.create_task(kill(f))
            with self.assertRaises(asyncio.CancelledError):
                await f
            sock.close()
            self.assertEqual(sock.fileno(), -1)

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                c = client(sock, srv.addr)
                w = asyncio.wait_for(c, timeout=5.0)
                self.loop.run_until_complete(w)

    def test_socket_cancel_sock_sendall(self):
        def srv_gen(sock):
            time.sleep(1.2)
            sock.recv_all(4)

        async def kill(fut):
            await asyncio.sleep(0.2)
            fut.cancel()

        async def client(sock, addr):
            await self.loop.sock_connect(sock, addr)

            f = asyncio.ensure_future(
                self.loop.sock_sendall(sock, b'helo' * (1024 * 1024 * 50)),
                loop=self.loop)
            self.loop.create_task(kill(f))
            with self.assertRaises(asyncio.CancelledError):
                await f
            sock.close()
            self.assertEqual(sock.fileno(), -1)

        # disable slow callback reporting for this test
        self.loop.slow_callback_duration = 1000.0

        with self.tcp_server(srv_gen) as srv:

            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                c = client(sock, srv.addr)
                w = asyncio.wait_for(c, timeout=5.0)
                self.loop.run_until_complete(w)

    def test_socket_close_many_add_readers(self):
        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_reader(s, lambda: None)
            self.loop.add_reader(s, lambda: None)
            self.loop.add_reader(s, lambda: None)
            self.loop.remove_reader(s.fileno())
            s.close()
            self.assertEqual(s.fileno(), -1)

        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_reader(s, lambda: None)
            self.loop.add_reader(s, lambda: None)
            self.loop.add_reader(s, lambda: None)
            self.loop.remove_reader(s)
            s.close()
            self.assertEqual(s.fileno(), -1)

    def test_socket_close_many_remove_writers(self):
        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_writer(s, lambda: None)
            self.loop.add_writer(s, lambda: None)
            self.loop.add_writer(s, lambda: None)
            self.loop.remove_writer(s.fileno())
            s.close()
            self.assertEqual(s.fileno(), -1)

        s = socket.socket()
        with s:
            s.setblocking(False)
            self.loop.add_writer(s, lambda: None)
            self.loop.add_writer(s, lambda: None)
            self.loop.add_writer(s, lambda: None)
            self.loop.remove_writer(s)
            s.close()
            self.assertEqual(s.fileno(), -1)


class TestAIOSockets(_TestSockets, tb.AIOTestCase):
    pass
```

## File: `tests/test_sourcecode.py`
```python
import os
import subprocess
import sys
import unittest


def find_uvloop_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestSourceCode(unittest.TestCase):

    def test_flake8(self):
        edgepath = find_uvloop_root()
        config_path = os.path.join(edgepath, '.flake8')
        if not os.path.exists(config_path):
            raise RuntimeError('could not locate .flake8 file')

        try:
            import flake8  # NoQA
        except ImportError:
            raise unittest.SkipTest('flake8 module is missing')

        for subdir in ['examples', 'uvloop', 'tests']:
            try:
                subprocess.run(
                    [sys.executable, '-m', 'flake8', '--config', config_path],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=os.path.join(edgepath, subdir))
            except subprocess.CalledProcessError as ex:
                output = ex.stdout.decode()
                output += '\n'
                output += ex.stderr.decode()
                raise AssertionError(
                    'flake8 validation failed: {}\n{}'.format(ex, output)
                ) from None

    def test_mypy(self):
        edgepath = find_uvloop_root()
        config_path = os.path.join(edgepath, 'mypy.ini')
        if not os.path.exists(config_path):
            raise RuntimeError('could not locate mypy.ini file')

        try:
            import mypy  # NoQA
        except ImportError:
            raise unittest.SkipTest('mypy module is missing')

        try:
            subprocess.run(
                [
                    sys.executable,
                    '-m',
                    'mypy',
                    '--config-file',
                    config_path,
                    'uvloop'
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=edgepath
            )
        except subprocess.CalledProcessError as ex:
            output = ex.stdout.decode()
            output += '\n'
            output += ex.stderr.decode()
            raise AssertionError(
                'mypy validation failed: {}\n{}'.format(ex, output)
            ) from None
```

## File: `tests/test_tcp.py`
```python
import asyncio
import asyncio.sslproto
import gc
import os
import select
import socket
import unittest.mock
import ssl
import sys
import threading
import time
import weakref

from OpenSSL import SSL as openssl_ssl
from uvloop import _testbase as tb


SSL_HANDSHAKE_TIMEOUT = 15.0


class MyBaseProto(asyncio.Protocol):
    connected = None
    done = None

    def __init__(self, loop=None):
        self.transport = None
        self.state = 'INITIAL'
        self.nbytes = 0
        if loop is not None:
            self.connected = asyncio.Future(loop=loop)
            self.done = asyncio.Future(loop=loop)

    def connection_made(self, transport):
        self.transport = transport
        assert self.state == 'INITIAL', self.state
        self.state = 'CONNECTED'
        if self.connected:
            self.connected.set_result(None)

    def data_received(self, data):
        assert self.state == 'CONNECTED', self.state
        self.nbytes += len(data)

    def eof_received(self):
        assert self.state == 'CONNECTED', self.state
        self.state = 'EOF'

    def connection_lost(self, exc):
        assert self.state in ('CONNECTED', 'EOF'), self.state
        self.state = 'CLOSED'
        if self.done:
            self.done.set_result(None)


class _TestTCP:
    def test_create_server_1(self):
        CNT = 0           # number of clients that were successful
        TOTAL_CNT = 25    # total number of clients that test will create
        TIMEOUT = 5.0     # timeout for this test

        A_DATA = b'A' * 1024 * 1024
        B_DATA = b'B' * 1024 * 1024

        async def handle_client(reader, writer):
            nonlocal CNT

            data = await reader.readexactly(len(A_DATA))
            self.assertEqual(data, A_DATA)
            writer.write(b'OK')

            data = await reader.readexactly(len(B_DATA))
            self.assertEqual(data, B_DATA)
            writer.writelines([b'S', b'P'])
            writer.write(bytearray(b'A'))
            writer.write(memoryview(b'M'))

            if self.implementation == 'uvloop':
                tr = writer.transport
                sock = tr.get_extra_info('socket')
                self.assertTrue(
                    sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))

            await writer.drain()
            writer.close()

            CNT += 1

        async def test_client(addr):
            sock = socket.socket()
            with sock:
                sock.setblocking(False)
                await self.loop.sock_connect(sock, addr)

                await self.loop.sock_sendall(sock, A_DATA)

                buf = b''
                while len(buf) != 2:
                    buf += await self.loop.sock_recv(sock, 1)
                self.assertEqual(buf, b'OK')

                await self.loop.sock_sendall(sock, B_DATA)

                buf = b''
                while len(buf) != 4:
                    buf += await self.loop.sock_recv(sock, 1)
                self.assertEqual(buf, b'SPAM')

            self.assertEqual(sock.fileno(), -1)
            self.assertEqual(sock._io_refs, 0)
            self.assertTrue(sock._closed)

        async def start_server():
            nonlocal CNT
            CNT = 0

            srv = await asyncio.start_server(
                handle_client,
                ('127.0.0.1', 'localhost'), 0,
                family=socket.AF_INET)

            srv_socks = srv.sockets
            self.assertTrue(srv_socks)
            self.assertTrue(srv.is_serving())

            addr = srv_socks[0].getsockname()

            tasks = []
            for _ in range(TOTAL_CNT):
                tasks.append(test_client(addr))

            await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

            self.loop.call_soon(srv.close)
            await srv.wait_closed()

            if (
                self.implementation == 'asyncio'
                and sys.version_info[:3] >= (3, 12, 0)
            ):
                # asyncio regression in 3.12 -- wait_closed()
                # doesn't wait for `close()` to actually complete.
                # https://github.com/python/cpython/issues/79033
                await asyncio.sleep(1)

            # Check that the server cleaned-up proxy-sockets
            for srv_sock in srv_socks:
                self.assertEqual(srv_sock.fileno(), -1)

            self.assertFalse(srv.is_serving())

        async def start_server_sock():
            nonlocal CNT
            CNT = 0

            sock = socket.socket()
            sock.bind(('127.0.0.1', 0))
            addr = sock.getsockname()

            srv = await asyncio.start_server(
                handle_client,
                None, None,
                family=socket.AF_INET,
                sock=sock)

            self.assertIs(srv.get_loop(), self.loop)

            srv_socks = srv.sockets
            self.assertTrue(srv_socks)
            self.assertTrue(srv.is_serving())

            tasks = []
            for _ in range(TOTAL_CNT):
                tasks.append(test_client(addr))

            await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

            srv.close()
            await srv.wait_closed()

            if (
                self.implementation == 'asyncio'
                and sys.version_info[:3] >= (3, 12, 0)
            ):
                # asyncio regression in 3.12 -- wait_closed()
                # doesn't wait for `close()` to actually complete.
                # https://github.com/python/cpython/issues/79033
                await asyncio.sleep(1)

            # Check that the server cleaned-up proxy-sockets
            for srv_sock in srv_socks:
                self.assertEqual(srv_sock.fileno(), -1)

            self.assertFalse(srv.is_serving())

        self.loop.run_until_complete(start_server())
        self.assertEqual(CNT, TOTAL_CNT)

        self.loop.run_until_complete(start_server_sock())
        self.assertEqual(CNT, TOTAL_CNT)

    def test_create_server_2(self):
        with self.assertRaisesRegex(ValueError, 'nor sock were specified'):
            self.loop.run_until_complete(self.loop.create_server(object))

    def test_create_server_3(self):
        ''' check ephemeral port can be used '''

        async def start_server_ephemeral_ports():

            for port_sentinel in [0, None]:
                srv = await self.loop.create_server(
                    asyncio.Protocol,
                    '127.0.0.1', port_sentinel,
                    family=socket.AF_INET)

                srv_socks = srv.sockets
                self.assertTrue(srv_socks)
                self.assertTrue(srv.is_serving())

                host, port = srv_socks[0].getsockname()
                self.assertNotEqual(0, port)

                self.loop.call_soon(srv.close)
                await srv.wait_closed()

                if (
                    self.implementation == 'asyncio'
                    and sys.version_info[:3] >= (3, 12, 0)
                ):
                    # asyncio regression in 3.12 -- wait_closed()
                    # doesn't wait for `close()` to actually complete.
                    # https://github.com/python/cpython/issues/79033
                    await asyncio.sleep(1)

                # Check that the server cleaned-up proxy-sockets
                for srv_sock in srv_socks:
                    self.assertEqual(srv_sock.fileno(), -1)

                self.assertFalse(srv.is_serving())

        self.loop.run_until_complete(start_server_ephemeral_ports())

    def test_create_server_4(self):
        sock = socket.socket()
        sock.bind(('127.0.0.1', 0))

        with sock:
            addr = sock.getsockname()

            with self.assertRaisesRegex(OSError,
                                        r"error while attempting.*\('127.*:"
                                        r"( \[errno \d+\])? address"
                                        r"( already)? in use"):

                self.loop.run_until_complete(
                    self.loop.create_server(object, *addr))

    def test_create_server_5(self):
        # Test that create_server sets the TCP_IPV6ONLY flag,
        # so it can bind to ipv4 and ipv6 addresses
        # simultaneously.

        port = tb.find_free_port()

        async def runner():
            srv = await self.loop.create_server(
                asyncio.Protocol,
                None, port)

            srv.close()
            await srv.wait_closed()

        self.loop.run_until_complete(runner())

    def test_create_server_6(self):
        if not hasattr(socket, 'SO_REUSEPORT'):
            raise unittest.SkipTest(
                'The system does not support SO_REUSEPORT')

        port = tb.find_free_port()

        async def runner():
            srv1 = await self.loop.create_server(
                asyncio.Protocol,
                None, port,
                reuse_port=True)

            srv2 = await self.loop.create_server(
                asyncio.Protocol,
                None, port,
                reuse_port=True)

            srv1.close()
            srv2.close()

            await srv1.wait_closed()
            await srv2.wait_closed()

        self.loop.run_until_complete(runner())

    def test_create_server_7(self):
        # Test that create_server() stores a hard ref to the server object
        # somewhere in the loop.  In asyncio it so happens that
        # loop.sock_accept() has a reference to the server object so it
        # never gets GCed.

        class Proto(asyncio.Protocol):
            def connection_made(self, tr):
                self.tr = tr
                self.tr.write(b'hello')

        async def test():
            port = tb.find_free_port()
            srv = await self.loop.create_server(Proto, '127.0.0.1', port)
            wsrv = weakref.ref(srv)
            del srv

            gc.collect()
            gc.collect()
            gc.collect()

            s = socket.socket(socket.AF_INET)
            with s:
                s.setblocking(False)
                await self.loop.sock_connect(s, ('127.0.0.1', port))
                d = await self.loop.sock_recv(s, 100)
                self.assertEqual(d, b'hello')

            srv = wsrv()
            srv.close()
            await srv.wait_closed()
            del srv

            # Let all transports shutdown.
            await asyncio.sleep(0.1)

            gc.collect()
            gc.collect()
            gc.collect()

            self.assertIsNone(wsrv())

        self.loop.run_until_complete(test())

    def test_create_server_8(self):
        with self.assertRaisesRegex(
                ValueError, 'ssl_handshake_timeout is only meaningful'):
            self.loop.run_until_complete(
                self.loop.create_server(
                    lambda: None, host='::', port=0,
                    ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT))

    def test_create_server_9(self):
        async def handle_client(reader, writer):
            pass

        async def start_server():
            srv = await asyncio.start_server(
                handle_client,
                '127.0.0.1', 0,
                family=socket.AF_INET,
                start_serving=False)

            await srv.start_serving()
            self.assertTrue(srv.is_serving())

            # call start_serving again
            await srv.start_serving()
            self.assertTrue(srv.is_serving())

            srv.close()
            await srv.wait_closed()
            self.assertFalse(srv.is_serving())

        self.loop.run_until_complete(start_server())

    def test_create_server_10(self):
        async def handle_client(reader, writer):
            pass

        async def start_server():
            srv = await asyncio.start_server(
                handle_client,
                '127.0.0.1', 0,
                family=socket.AF_INET,
                start_serving=False)

            async with srv:
                fut = asyncio.ensure_future(srv.serve_forever())
                await asyncio.sleep(0)
                self.assertTrue(srv.is_serving())

                fut.cancel()
                with self.assertRaises(asyncio.CancelledError):
                    await fut
                self.assertFalse(srv.is_serving())

        self.loop.run_until_complete(start_server())

    def test_create_connection_open_con_addr(self):
        async def client(addr):
            reader, writer = await asyncio.open_connection(*addr)

            writer.write(b'AAAA')
            self.assertEqual(await reader.readexactly(2), b'OK')

            re = r'(a bytes-like object)|(must be byte-ish)'
            if sys.version_info >= (3, 13, 9):
                re += r'|(must be a bytes, bytearray, or memoryview object)'
            with self.assertRaisesRegex(TypeError, re):
                writer.write('AAAA')

            writer.write(b'BBBB')
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            if self.implementation == 'uvloop':
                tr = writer.transport
                sock = tr.get_extra_info('socket')
                self.assertTrue(
                    sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))

            writer.close()
            await self.wait_closed(writer)

        self._test_create_connection_1(client)

    def test_create_connection_open_con_sock(self):
        async def client(addr):
            sock = socket.socket()
            sock.connect(addr)
            reader, writer = await asyncio.open_connection(sock=sock)

            writer.write(b'AAAA')
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(b'BBBB')
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            if self.implementation == 'uvloop':
                tr = writer.transport
                sock = tr.get_extra_info('socket')
                self.assertTrue(
                    sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))

            writer.close()
            await self.wait_closed(writer)

        self._test_create_connection_1(client)

    def _test_create_connection_1(self, client):
        CNT = 0
        TOTAL_CNT = 100

        def server(sock):
            data = sock.recv_all(4)
            self.assertEqual(data, b'AAAA')
            sock.send(b'OK')

            data = sock.recv_all(4)
            self.assertEqual(data, b'BBBB')
            sock.send(b'SPAM')

        async def client_wrapper(addr):
            await client(addr)
            nonlocal CNT
            CNT += 1

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.tcp_server(server,
                                 max_clients=TOTAL_CNT,
                                 backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(asyncio.gather(*tasks))

            self.assertEqual(CNT, TOTAL_CNT)

        run(client_wrapper)

    def test_create_connection_2(self):
        sock = socket.socket()
        with sock:
            sock.bind(('127.0.0.1', 0))
            addr = sock.getsockname()

        async def client():
            reader, writer = await asyncio.open_connection(*addr)
            writer.close()
            await self.wait_closed(writer)

        async def runner():
            with self.assertRaises(ConnectionRefusedError):
                await client()

        self.loop.run_until_complete(runner())

    def test_create_connection_3(self):
        CNT = 0
        TOTAL_CNT = 100

        def server(sock):
            data = sock.recv_all(4)
            self.assertEqual(data, b'AAAA')
            sock.close()

        async def client(addr):
            reader, writer = await asyncio.open_connection(*addr)

            writer.write(b'AAAA')

            with self.assertRaises(asyncio.IncompleteReadError):
                await reader.readexactly(10)

            writer.close()
            await self.wait_closed(writer)

            nonlocal CNT
            CNT += 1

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.tcp_server(server,
                                 max_clients=TOTAL_CNT,
                                 backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(asyncio.gather(*tasks))

            self.assertEqual(CNT, TOTAL_CNT)

        run(client)

    def test_create_connection_4(self):
        sock = socket.socket()
        sock.close()

        async def client():
            reader, writer = await asyncio.open_connection(sock=sock)
            writer.close()
            await self.wait_closed(writer)

        async def runner():
            with self.assertRaisesRegex(OSError, 'Bad file'):
                await client()

        self.loop.run_until_complete(runner())

    def test_create_connection_5(self):
        def server(sock):
            try:
                data = sock.recv_all(4)
            except ConnectionError:
                return
            self.assertEqual(data, b'AAAA')
            sock.send(b'OK')

        async def client(addr):
            fut = asyncio.ensure_future(
                self.loop.create_connection(asyncio.Protocol, *addr))
            await asyncio.sleep(0)
            fut.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await fut

        with self.tcp_server(server,
                             max_clients=1,
                             backlog=1) as srv:
            self.loop.run_until_complete(client(srv.addr))

    def test_create_connection_6(self):
        with self.assertRaisesRegex(
                ValueError, 'ssl_handshake_timeout is only meaningful'):
            self.loop.run_until_complete(
                self.loop.create_connection(
                    lambda: None, host='::', port=0,
                    ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT))

    def test_transport_shutdown(self):
        CNT = 0           # number of clients that were successful
        TOTAL_CNT = 100   # total number of clients that test will create
        TIMEOUT = 5.0     # timeout for this test

        async def handle_client(reader, writer):
            nonlocal CNT

            data = await reader.readexactly(4)
            self.assertEqual(data, b'AAAA')

            writer.write(b'OK')
            writer.write_eof()
            writer.write_eof()

            await writer.drain()
            writer.close()

            CNT += 1

        async def test_client(addr):
            reader, writer = await asyncio.open_connection(*addr)

            writer.write(b'AAAA')
            data = await reader.readexactly(2)
            self.assertEqual(data, b'OK')

            writer.close()
            await self.wait_closed(writer)

        async def start_server():
            nonlocal CNT
            CNT = 0

            srv = await asyncio.start_server(
                handle_client,
                '127.0.0.1', 0,
                family=socket.AF_INET)

            srv_socks = srv.sockets
            self.assertTrue(srv_socks)

            addr = srv_socks[0].getsockname()

            tasks = []
            for _ in range(TOTAL_CNT):
                tasks.append(test_client(addr))

            await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

            srv.close()
            await srv.wait_closed()

        self.loop.run_until_complete(start_server())
        self.assertEqual(CNT, TOTAL_CNT)

    def test_tcp_handle_exception_in_connection_made(self):
        # Test that if connection_made raises an exception,
        # 'create_connection' still returns.

        # Silence error logging
        self.loop.set_exception_handler(lambda *args: None)

        fut = asyncio.Future()
        connection_lost_called = asyncio.Future()

        async def server(reader, writer):
            try:
                await reader.read()
            finally:
                writer.close()

        class Proto(asyncio.Protocol):
            def connection_made(self, tr):
                1 / 0

            def connection_lost(self, exc):
                connection_lost_called.set_result(exc)

        srv = self.loop.run_until_complete(asyncio.start_server(
            server,
            '127.0.0.1', 0,
            family=socket.AF_INET))

        async def runner():
            tr, pr = await asyncio.wait_for(
                self.loop.create_connection(
                    Proto, *srv.sockets[0].getsockname()),
                timeout=1.0)
            fut.set_result(None)
            tr.close()

        self.loop.run_until_complete(runner())
        srv.close()
        self.loop.run_until_complete(srv.wait_closed())
        self.loop.run_until_complete(fut)

        self.assertIsNone(
            self.loop.run_until_complete(connection_lost_called))

    def test_resume_writing_write_different_transport(self):
        loop = self.loop

        class P1(asyncio.Protocol):
            def __init__(self, t2):
                self.t2 = t2
                self.paused = False
                self.waiter = loop.create_future()

            def data_received(self, data):
                self.waiter.set_result(data)

            def pause_writing(self):
                self.paused = True

            def resume_writing(self):
                self.paused = False
                self.t2.write(b'hello')

        s1, s2 = socket.socketpair()
        s1.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024)
        s2.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)

        async def _test(t1, p1, t2):
            t1.set_write_buffer_limits(1024, 1023)

            # fill s1 up first
            t2.pause_reading()
            while not p1.paused:
                t1.write(b' ' * 1024)

            # trigger resume_writing() in _exec_queued_writes() with tight loop
            t2.resume_reading()
            while p1.paused:
                t1.write(b' ')
                await asyncio.sleep(0)

            # t2.write() in p1.resume_writing() should work fine
            data = await asyncio.wait_for(p1.waiter, 5)
            self.assertEqual(data, b'hello')

        async def test():
            t2, _ = await loop.create_connection(asyncio.Protocol, sock=s2)
            t1, p1 = await loop.create_connection(lambda: P1(t2), sock=s1)
            try:
                await _test(t1, p1, t2)
            finally:
                t1.close()
                t2.close()

        with s1, s2:
            loop.run_until_complete(test())


class Test_UV_TCP(_TestTCP, tb.UVTestCase):

    def test_create_server_buffered_1(self):
        SIZE = 123123
        eof = False
        fut = asyncio.Future()

        class Proto(asyncio.BaseProtocol):
            def connection_made(self, tr):
                self.tr = tr
                self.recvd = b''
                self.data = bytearray(50)
                self.buf = memoryview(self.data)

            def get_buffer(self, sizehint):
                return self.buf

            def buffer_updated(self, nbytes):
                self.recvd += self.buf[:nbytes]
                if self.recvd == b'a' * SIZE:
                    self.tr.write(b'hello')

            def eof_received(self):
                nonlocal eof
                eof = True

            def connection_lost(self, exc):
                fut.set_result(exc)

        async def test():
            port = tb.find_free_port()
            srv = await self.loop.create_server(Proto, '127.0.0.1', port)

            s = socket.socket(socket.AF_INET)
            with s:
                s.setblocking(False)
                await self.loop.sock_connect(s, ('127.0.0.1', port))
                await self.loop.sock_sendall(s, b'a' * SIZE)
                d = await self.loop.sock_recv(s, 100)
                self.assertEqual(d, b'hello')

            srv.close()
            await srv.wait_closed()

        self.loop.run_until_complete(test())
        self.loop.run_until_complete(fut)
        self.assertTrue(eof)
        self.assertIsNone(fut.result())

    def test_create_server_buffered_2(self):
        class ProtoExc(asyncio.BaseProtocol):
            def __init__(self):
                self._lost_exc = None

            def get_buffer(self, sizehint):
                1 / 0

            def buffer_updated(self, nbytes):
                pass

            def connection_lost(self, exc):
                self._lost_exc = exc

            def eof_received(self):
                pass

        class ProtoZeroBuf1(asyncio.BaseProtocol):
            def __init__(self):
                self._lost_exc = None

            def get_buffer(self, sizehint):
                return bytearray(0)

            def buffer_updated(self, nbytes):
                pass

            def connection_lost(self, exc):
                self._lost_exc = exc

            def eof_received(self):
                pass

        class ProtoZeroBuf2(asyncio.BaseProtocol):
            def __init__(self):
                self._lost_exc = None

            def get_buffer(self, sizehint):
                return memoryview(bytearray(0))

            def buffer_updated(self, nbytes):
                pass

            def connection_lost(self, exc):
                self._lost_exc = exc

            def eof_received(self):
                pass

        class ProtoUpdatedError(asyncio.BaseProtocol):
            def __init__(self):
                self._lost_exc = None

            def get_buffer(self, sizehint):
                return memoryview(bytearray(100))

            def buffer_updated(self, nbytes):
                raise RuntimeError('oups')

            def connection_lost(self, exc):
                self._lost_exc = exc

            def eof_received(self):
                pass

        async def test(proto_factory, exc_type, exc_re):
            port = tb.find_free_port()
            proto = proto_factory()
            srv = await self.loop.create_server(
                lambda: proto, '127.0.0.1', port)

            try:
                s = socket.socket(socket.AF_INET)
                with s:
                    s.setblocking(False)
                    await self.loop.sock_connect(s, ('127.0.0.1', port))
                    await self.loop.sock_sendall(s, b'a')
                    d = await self.loop.sock_recv(s, 100)
                    if not d:
                        raise ConnectionResetError
            except ConnectionResetError:
                pass
            else:
                self.fail("server didn't abort the connection")
                return
            finally:
                srv.close()
                await srv.wait_closed()

            if proto._lost_exc is None:
                self.fail("connection_lost() was not called")
                return

            with self.assertRaisesRegex(exc_type, exc_re):
                raise proto._lost_exc

        self.loop.set_exception_handler(lambda loop, ctx: None)

        self.loop.run_until_complete(
            test(ProtoExc, RuntimeError, 'unhandled error .* get_buffer'))

        self.loop.run_until_complete(
            test(ProtoZeroBuf1, RuntimeError, 'unhandled error .* get_buffer'))

        self.loop.run_until_complete(
            test(ProtoZeroBuf2, RuntimeError, 'unhandled error .* get_buffer'))

        self.loop.run_until_complete(
            test(ProtoUpdatedError, RuntimeError, r'^oups$'))

    def test_transport_get_extra_info(self):
        # This tests is only for uvloop.  asyncio should pass it
        # too in Python 3.6.

        fut = asyncio.Future()

        async def handle_client(reader, writer):
            with self.assertRaises(asyncio.IncompleteReadError):
                await reader.readexactly(4)
            writer.close()

            # Previously, when we used socket.fromfd to create a socket
            # for UVTransports (to make get_extra_info() work), a duplicate
            # of the socket was created, preventing UVTransport from being
            # properly closed.
            # This test ensures that server handle will receive an EOF
            # and finish the request.
            fut.set_result(None)

        async def test_client(addr):
            t, p = await self.loop.create_connection(
                lambda: asyncio.Protocol(), *addr)

            if hasattr(t, 'get_protocol'):
                p2 = asyncio.Protocol()
                self.assertIs(t.get_protocol(), p)
                t.set_protocol(p2)
                self.assertIs(t.get_protocol(), p2)
                t.set_protocol(p)

            self.assertFalse(t._paused)
            self.assertTrue(t.is_reading())
            t.pause_reading()
            t.pause_reading()  # Check that it's OK to call it 2nd time.
            self.assertTrue(t._paused)
            self.assertFalse(t.is_reading())
            t.resume_reading()
            t.resume_reading()  # Check that it's OK to call it 2nd time.
            self.assertFalse(t._paused)
            self.assertTrue(t.is_reading())

            sock = t.get_extra_info('socket')
            self.assertIs(sock, t.get_extra_info('socket'))
            sockname = sock.getsockname()
            peername = sock.getpeername()

            with self.assertRaisesRegex(RuntimeError, 'is used by transport'):
                self.loop.add_writer(sock.fileno(), lambda: None)
            with self.assertRaisesRegex(RuntimeError, 'is used by transport'):
                self.loop.remove_writer(sock.fileno())
            with self.assertRaisesRegex(RuntimeError, 'is used by transport'):
                self.loop.add_reader(sock.fileno(), lambda: None)
            with self.assertRaisesRegex(RuntimeError, 'is used by transport'):
                self.loop.remove_reader(sock.fileno())

            self.assertEqual(t.get_extra_info('sockname'),
                             sockname)
            self.assertEqual(t.get_extra_info('peername'),
                             peername)

            t.write(b'OK')  # We want server to fail.

            self.assertFalse(t._closing)
            t.abort()
            self.assertTrue(t._closing)

            self.assertFalse(t.is_reading())
            # Check that pause_reading and resume_reading don't raise
            # errors if called after the transport is closed.
            t.pause_reading()
            t.resume_reading()

            await fut

            # Test that peername and sockname are available after
            # the transport is closed.
            self.assertEqual(t.get_extra_info('peername'),
                             peername)
            self.assertEqual(t.get_extra_info('sockname'),
                             sockname)

        async def start_server():
            srv = await asyncio.start_server(
                handle_client,
                '127.0.0.1', 0,
                family=socket.AF_INET)

            addr = srv.sockets[0].getsockname()
            await test_client(addr)

            srv.close()
            await srv.wait_closed()

        self.loop.run_until_complete(start_server())

    def test_create_server_float_backlog(self):
        # asyncio spits out a warning we cannot suppress

        async def runner(bl):
            await self.loop.create_server(
                asyncio.Protocol,
                None, 0, backlog=bl)

        for bl in (1.1, '1'):
            with self.subTest(backlog=bl):
                with self.assertRaisesRegex(TypeError, 'integer'):
                    self.loop.run_until_complete(runner(bl))

    def test_many_small_writes(self):
        N = 10000
        TOTAL = 0

        fut = self.loop.create_future()

        async def server(reader, writer):
            nonlocal TOTAL
            while True:
                d = await reader.read(10000)
                if not d:
                    break
                TOTAL += len(d)
            fut.set_result(True)
            writer.close()

        async def run():
            srv = await asyncio.start_server(
                server,
                '127.0.0.1', 0,
                family=socket.AF_INET)

            addr = srv.sockets[0].getsockname()
            r, w = await asyncio.open_connection(*addr)

            DATA = b'x' * 102400

            # Test _StreamWriteContext with short sequences of writes
            w.write(DATA)
            await w.drain()
            for _ in range(3):
                w.write(DATA)
            await w.drain()
            for _ in range(10):
                w.write(DATA)
            await w.drain()

            for _ in range(N):
                w.write(DATA)

                try:
                    w.write('a')
                except TypeError:
                    pass

            await w.drain()
            for _ in range(N):
                w.write(DATA)
                await w.drain()

            w.close()
            await fut
            await self.wait_closed(w)

            srv.close()
            await srv.wait_closed()

            self.assertEqual(TOTAL, N * 2 * len(DATA) + 14 * len(DATA))

        self.loop.run_until_complete(run())

    def test_tcp_handle_abort_in_connection_made(self):
        async def server(reader, writer):
            try:
                await reader.read()
            finally:
                writer.close()

        class Proto(asyncio.Protocol):
            def connection_made(self, tr):
                tr.abort()

        srv = self.loop.run_until_complete(asyncio.start_server(
            server,
            '127.0.0.1', 0,
            family=socket.AF_INET))

        async def runner():
            tr, pr = await asyncio.wait_for(
                self.loop.create_connection(
                    Proto, *srv.sockets[0].getsockname()),
                timeout=1.0)

            # Asyncio would return a closed socket, which we
            # can't do: the transport was aborted, hence there
            # is no FD to attach a socket to (to make
            # get_extra_info() work).
            self.assertIsNone(tr.get_extra_info('socket'))
            tr.close()

        self.loop.run_until_complete(runner())
        srv.close()
        self.loop.run_until_complete(srv.wait_closed())

    def test_connect_accepted_socket_ssl_args(self):
        with self.assertRaisesRegex(
                ValueError, 'ssl_handshake_timeout is only meaningful'):
            with socket.socket() as s:
                self.loop.run_until_complete(
                    self.loop.connect_accepted_socket(
                        (lambda: None),
                        s,
                        ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT
                    )
                )

    def test_connect_accepted_socket(self, server_ssl=None, client_ssl=None):
        loop = self.loop

        class MyProto(MyBaseProto):

            def connection_lost(self, exc):
                super().connection_lost(exc)
                loop.call_soon(loop.stop)

            def data_received(self, data):
                super().data_received(data)
                self.transport.write(expected_response)

        lsock = socket.socket(socket.AF_INET)
        lsock.bind(('127.0.0.1', 0))
        lsock.listen(1)
        addr = lsock.getsockname()

        message = b'test data'
        response = None
        expected_response = b'roger'

        def client():
            nonlocal response
            try:
                csock = socket.socket(socket.AF_INET)
                if client_ssl is not None:
                    csock = client_ssl.wrap_socket(csock)
                csock.connect(addr)
                csock.sendall(message)
                response = csock.recv(99)
                csock.close()
            except Exception as exc:
                print(
                    "Failure in client thread in test_connect_accepted_socket",
                    exc)

        thread = threading.Thread(target=client, daemon=True)
        thread.start()

        conn, _ = lsock.accept()
        proto = MyProto(loop=loop)
        proto.loop = loop

        extras = {}
        if server_ssl:
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

        f = loop.create_task(
            loop.connect_accepted_socket(
                (lambda: proto), conn, ssl=server_ssl,
                **extras))
        loop.run_forever()
        conn.close()
        lsock.close()

        thread.join(1)
        self.assertFalse(thread.is_alive())
        self.assertEqual(proto.state, 'CLOSED')
        self.assertEqual(proto.nbytes, len(message))
        self.assertEqual(response, expected_response)
        tr, _ = f.result()

        if server_ssl:
            self.assertIn('SSL', tr.__class__.__name__)

        tr.close()
        # let it close
        self.loop.run_until_complete(asyncio.sleep(0.1))

    @unittest.skipUnless(hasattr(socket, 'AF_UNIX'), 'no Unix sockets')
    def test_create_connection_wrong_sock(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with sock:
            coro = self.loop.create_connection(MyBaseProto, sock=sock)
            with self.assertRaisesRegex(ValueError,
                                        'A Stream Socket was expected'):
                self.loop.run_until_complete(coro)

    @unittest.skipUnless(hasattr(socket, 'AF_UNIX'), 'no Unix sockets')
    def test_create_server_wrong_sock(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with sock:
            coro = self.loop.create_server(MyBaseProto, sock=sock)
            with self.assertRaisesRegex(ValueError,
                                        'A Stream Socket was expected'):
                self.loop.run_until_complete(coro)

    @unittest.skipUnless(hasattr(socket, 'SOCK_NONBLOCK'),
                         'no socket.SOCK_NONBLOCK (linux only)')
    def test_create_server_stream_bittype(self):
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
        with sock:
            coro = self.loop.create_server(lambda: None, sock=sock)
            srv = self.loop.run_until_complete(coro)
            srv.close()
            self.loop.run_until_complete(srv.wait_closed())

    def test_flowcontrol_mixin_set_write_limits(self):
        async def client(addr):
            paused = False

            class Protocol(asyncio.Protocol):
                def pause_writing(self):
                    nonlocal paused
                    paused = True

                def resume_writing(self):
                    nonlocal paused
                    paused = False

            t, p = await self.loop.create_connection(Protocol, *addr)

            t.write(b'q' * 512)
            t.set_write_buffer_limits(low=16385)
            self.assertEqual(t.get_write_buffer_limits(), (16385, 65540))

            with self.assertRaisesRegex(ValueError, 'high.*must be >= low'):
                t.set_write_buffer_limits(high=0, low=1)

            t.set_write_buffer_limits(high=1024, low=128)
            self.assertEqual(t.get_write_buffer_limits(), (128, 1024))

            t.set_write_buffer_limits(high=256, low=128)
            self.assertEqual(t.get_write_buffer_limits(), (128, 256))

            t.close()

        with self.tcp_server(lambda sock: sock.recv_all(1),
                             max_clients=1,
                             backlog=1) as srv:
            self.loop.run_until_complete(client(srv.addr))


class Test_AIO_TCP(_TestTCP, tb.AIOTestCase):
    pass


class _TestSSL(tb.SSLTestCase):

    ONLYCERT = tb._cert_fullname(__file__, 'ssl_cert.pem')
    ONLYKEY = tb._cert_fullname(__file__, 'ssl_key.pem')

    PAYLOAD_SIZE = 1024 * 100
    TIMEOUT = 60

    def test_create_server_ssl_1(self):
        CNT = 0           # number of clients that were successful
        TOTAL_CNT = 25    # total number of clients that test will create
        TIMEOUT = 20.0    # timeout for this test

        A_DATA = b'A' * 1024 * 1024
        B_DATA = b'B' * 1024 * 1024

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()

        clients = []

        async def handle_client(reader, writer):
            nonlocal CNT

            data = await reader.readexactly(len(A_DATA))
            self.assertEqual(data, A_DATA)
            writer.write(b'OK')

            data = await reader.readexactly(len(B_DATA))
            self.assertEqual(data, B_DATA)
            writer.writelines([b'SP', bytearray(b'A'), memoryview(b'M')])

            await writer.drain()
            writer.close()

            CNT += 1

        async def test_client(addr):
            fut = asyncio.Future()

            def prog(sock):
                try:
                    sock.starttls(client_sslctx)
                    sock.connect(addr)
                    sock.send(A_DATA)

                    data = sock.recv_all(2)
                    self.assertEqual(data, b'OK')

                    sock.send(B_DATA)
                    data = sock.recv_all(4)
                    self.assertEqual(data, b'SPAM')

                    sock.close()

                except Exception as ex:
                    self.loop.call_soon_threadsafe(fut.set_exception, ex)
                else:
                    self.loop.call_soon_threadsafe(fut.set_result, None)

            client = self.tcp_client(prog)
            client.start()
            clients.append(client)

            await fut

        async def start_server():
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

            srv = await asyncio.start_server(
                handle_client,
                '127.0.0.1', 0,
                family=socket.AF_INET,
                ssl=sslctx,
                **extras)

            try:
                srv_socks = srv.sockets
                self.assertTrue(srv_socks)

                addr = srv_socks[0].getsockname()

                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(test_client(addr))

                await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

            finally:
                self.loop.call_soon(srv.close)
                await srv.wait_closed()

        with self._silence_eof_received_warning():
            self.loop.run_until_complete(start_server())

        self.assertEqual(CNT, TOTAL_CNT)

        for client in clients:
            client.stop()

    def test_create_connection_ssl_1(self):
        if self.implementation == 'asyncio':
            # Don't crash on asyncio errors
            self.loop.set_exception_handler(None)

        CNT = 0
        TOTAL_CNT = 25

        A_DATA = b'A' * 1024 * 1024
        B_DATA = b'B' * 1024 * 1024

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()

        def server(sock):
            sock.starttls(
                sslctx,
                server_side=True)

            data = sock.recv_all(len(A_DATA))
            self.assertEqual(data, A_DATA)
            sock.send(b'OK')

            data = sock.recv_all(len(B_DATA))
            self.assertEqual(data, B_DATA)
            sock.send(b'SPAM')

            sock.close()

        async def client(addr):
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='',
                **extras)

            writer.write(A_DATA)
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(B_DATA)
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            nonlocal CNT
            CNT += 1

            writer.close()
            await self.wait_closed(writer)

        async def client_sock(addr):
            sock = socket.socket()
            sock.connect(addr)
            reader, writer = await asyncio.open_connection(
                sock=sock,
                ssl=client_sslctx,
                server_hostname='')

            writer.write(A_DATA)
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(B_DATA)
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            nonlocal CNT
            CNT += 1

            writer.close()
            await self.wait_closed(writer)
            sock.close()

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.tcp_server(server,
                                 max_clients=TOTAL_CNT,
                                 backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(asyncio.gather(*tasks))

            self.assertEqual(CNT, TOTAL_CNT)

        with self._silence_eof_received_warning():
            run(client)

        with self._silence_eof_received_warning():
            run(client_sock)

    def test_create_connection_ssl_slow_handshake(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        client_sslctx = self._create_client_ssl_context()

        # silence error logger
        self.loop.set_exception_handler(lambda *args: None)

        def server(sock):
            try:
                sock.recv_all(1024 * 1024)
            except ConnectionAbortedError:
                pass
            finally:
                sock.close()

        async def client(addr):
            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='',
                ssl_handshake_timeout=1.0)
            writer.close()
            await self.wait_closed(writer)

        with self.tcp_server(server,
                             max_clients=1,
                             backlog=1) as srv:

            with self.assertRaisesRegex(
                    ConnectionAbortedError,
                    r'SSL handshake.*is taking longer'):

                self.loop.run_until_complete(client(srv.addr))

    def test_create_connection_ssl_failed_certificate(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        # silence error logger
        self.loop.set_exception_handler(lambda *args: None)

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context(disable_verify=False)

        def server(sock):
            try:
                sock.starttls(
                    sslctx,
                    server_side=True)
                sock.connect()
            except (ssl.SSLError, OSError):
                pass
            finally:
                sock.close()

        async def client(addr):
            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='',
                ssl_handshake_timeout=1.0)
            writer.close()
            await self.wait_closed(writer)

        with self.tcp_server(server,
                             max_clients=1,
                             backlog=1) as srv:

            with self.assertRaises(ssl.SSLCertVerificationError):
                self.loop.run_until_complete(client(srv.addr))

    def test_start_tls_wrong_args(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        async def main():
            with self.assertRaisesRegex(TypeError, 'SSLContext, got'):
                await self.loop.start_tls(None, None, None)

            sslctx = self._create_server_ssl_context(
                self.ONLYCERT, self.ONLYKEY)
            with self.assertRaisesRegex(TypeError, 'is not supported'):
                await self.loop.start_tls(None, None, sslctx)

        self.loop.run_until_complete(main())

    def test_ssl_handshake_timeout(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        # bpo-29970: Check that a connection is aborted if handshake is not
        # completed in timeout period, instead of remaining open indefinitely
        client_sslctx = self._create_client_ssl_context()

        # silence error logger
        messages = []
        self.loop.set_exception_handler(lambda loop, ctx: messages.append(ctx))

        server_side_aborted = False

        def server(sock):
            nonlocal server_side_aborted
            try:
                sock.recv_all(1024 * 1024)
            except ConnectionAbortedError:
                server_side_aborted = True
            finally:
                sock.close()

        async def client(addr):
            await asyncio.wait_for(
                self.loop.create_connection(
                    asyncio.Protocol,
                    *addr,
                    ssl=client_sslctx,
                    server_hostname='',
                    ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT
                ),
                0.5
            )

        with self.tcp_server(server,
                             max_clients=1,
                             backlog=1) as srv:

            with self.assertRaises(asyncio.TimeoutError):
                self.loop.run_until_complete(client(srv.addr))

        self.assertTrue(server_side_aborted)

        # Python issue #23197: cancelling a handshake must not raise an
        # exception or log an error, even if the handshake failed
        self.assertEqual(messages, [])

    def test_ssl_handshake_connection_lost(self):
        # #246: make sure that no connection_lost() is called before
        # connection_made() is called first

        client_sslctx = self._create_client_ssl_context()

        # silence error logger
        self.loop.set_exception_handler(lambda loop, ctx: None)

        connection_made_called = False
        connection_lost_called = False

        def server(sock):
            sock.recv(1024)
            # break the connection during handshake
            sock.close()

        class ClientProto(asyncio.Protocol):
            def connection_made(self, transport):
                nonlocal connection_made_called
                connection_made_called = True

            def connection_lost(self, exc):
                nonlocal connection_lost_called
                connection_lost_called = True

        async def client(addr):
            await self.loop.create_connection(
                ClientProto,
                *addr,
                ssl=client_sslctx,
                server_hostname=''),

        with self.tcp_server(server,
                             max_clients=1,
                             backlog=1) as srv:

            with self.assertRaises(ConnectionResetError):
                self.loop.run_until_complete(client(srv.addr))

        if connection_lost_called:
            if connection_made_called:
                self.fail("unexpected call to connection_lost()")
            else:
                self.fail("unexpected call to connection_lost() without"
                          "calling connection_made()")
        elif connection_made_called:
            self.fail("unexpected call to connection_made()")

    def test_ssl_connect_accepted_socket(self):
        if hasattr(ssl, 'PROTOCOL_TLS_SERVER'):
            server_proto = ssl.PROTOCOL_TLS_SERVER
            client_proto = ssl.PROTOCOL_TLS_CLIENT
        else:
            if hasattr(ssl, 'PROTOCOL_TLS'):
                client_proto = server_proto = ssl.PROTOCOL_TLS
            else:
                client_proto = server_proto = ssl.PROTOCOL_SSLv23

        server_context = ssl.SSLContext(server_proto)
        server_context.load_cert_chain(self.ONLYCERT, self.ONLYKEY)
        if hasattr(server_context, 'check_hostname'):
            server_context.check_hostname = False
        server_context.verify_mode = ssl.CERT_NONE

        client_context = ssl.SSLContext(client_proto)
        if hasattr(server_context, 'check_hostname'):
            client_context.check_hostname = False
        client_context.verify_mode = ssl.CERT_NONE

        Test_UV_TCP.test_connect_accepted_socket(
            self, server_context, client_context)

    def test_start_tls_client_corrupted_ssl(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        self.loop.set_exception_handler(lambda loop, ctx: None)

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()

        def server(sock):
            orig_sock = sock.dup()
            try:
                sock.starttls(
                    sslctx,
                    server_side=True)
                sock.sendall(b'A\n')
                sock.recv_all(1)
                orig_sock.send(b'please corrupt the SSL connection')
            except ssl.SSLError:
                pass
            finally:
                sock.close()
                orig_sock.close()

        async def client(addr):
            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='')

            self.assertEqual(await reader.readline(), b'A\n')
            writer.write(b'B')
            with self.assertRaises(ssl.SSLError):
                await reader.readline()
            writer.close()
            try:
                await self.wait_closed(writer)
            except ssl.SSLError:
                pass
            return 'OK'

        with self.tcp_server(server,
                             max_clients=1,
                             backlog=1) as srv:

            res = self.loop.run_until_complete(client(srv.addr))

        self.assertEqual(res, 'OK')

    def test_start_tls_client_reg_proto_1(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        HELLO_MSG = b'1' * self.PAYLOAD_SIZE

        server_context = self._create_server_ssl_context(
            self.ONLYCERT, self.ONLYKEY)
        client_context = self._create_client_ssl_context()

        def serve(sock):
            sock.settimeout(self.TIMEOUT)

            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            sock.starttls(server_context, server_side=True)

            sock.sendall(b'O')
            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            sock.unwrap()
            sock.close()

        class ClientProto(asyncio.Protocol):
            def __init__(self, on_data, on_eof):
                self.on_data = on_data
                self.on_eof = on_eof
                self.con_made_cnt = 0

            def connection_made(proto, tr):
                proto.con_made_cnt += 1
                # Ensure connection_made gets called only once.
                self.assertEqual(proto.con_made_cnt, 1)

            def data_received(self, data):
                self.on_data.set_result(data)

            def eof_received(self):
                self.on_eof.set_result(True)

        async def client(addr):
            await asyncio.sleep(0.5)

            on_data = self.loop.create_future()
            on_eof = self.loop.create_future()

            tr, proto = await self.loop.create_connection(
                lambda: ClientProto(on_data, on_eof), *addr)

            tr.write(HELLO_MSG)
            new_tr = await self.loop.start_tls(tr, proto, client_context)

            self.assertEqual(await on_data, b'O')
            new_tr.write(HELLO_MSG)
            await on_eof

            new_tr.close()

        with self.tcp_server(serve, timeout=self.TIMEOUT) as srv:
            self.loop.run_until_complete(
                asyncio.wait_for(client(srv.addr), timeout=10))

    def test_create_connection_memory_leak(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        HELLO_MSG = b'1' * self.PAYLOAD_SIZE

        server_context = self._create_server_ssl_context(
            self.ONLYCERT, self.ONLYKEY)
        client_context = self._create_client_ssl_context()

        def serve(sock):
            sock.settimeout(self.TIMEOUT)

            sock.starttls(server_context, server_side=True)

            sock.sendall(b'O')
            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            sock.unwrap()
            sock.close()

        class ClientProto(asyncio.Protocol):
            def __init__(self, on_data, on_eof):
                self.on_data = on_data
                self.on_eof = on_eof
                self.con_made_cnt = 0

            def connection_made(proto, tr):
                # XXX: We assume user stores the transport in protocol
                proto.tr = tr
                proto.con_made_cnt += 1
                # Ensure connection_made gets called only once.
                self.assertEqual(proto.con_made_cnt, 1)

            def data_received(self, data):
                self.on_data.set_result(data)

            def eof_received(self):
                self.on_eof.set_result(True)

        async def client(addr):
            await asyncio.sleep(0.5)

            on_data = self.loop.create_future()
            on_eof = self.loop.create_future()

            tr, proto = await self.loop.create_connection(
                lambda: ClientProto(on_data, on_eof), *addr,
                ssl=client_context)

            self.assertEqual(await on_data, b'O')
            tr.write(HELLO_MSG)
            await on_eof

            tr.close()

        with self.tcp_server(serve, timeout=self.TIMEOUT) as srv:
            self.loop.run_until_complete(
                asyncio.wait_for(client(srv.addr), timeout=10))

        # No garbage is left for SSL client from loop.create_connection, even
        # if user stores the SSLTransport in corresponding protocol instance
        client_context = weakref.ref(client_context)
        self.assertIsNone(client_context())

    def test_start_tls_client_buf_proto_1(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        HELLO_MSG = b'1' * self.PAYLOAD_SIZE

        server_context = self._create_server_ssl_context(
            self.ONLYCERT, self.ONLYKEY)
        client_context = self._create_client_ssl_context()

        client_con_made_calls = 0

        def serve(sock):
            sock.settimeout(self.TIMEOUT)

            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            sock.starttls(server_context, server_side=True)

            sock.sendall(b'O')
            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            sock.sendall(b'2')
            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            sock.unwrap()
            sock.close()

        class ClientProtoFirst(asyncio.BaseProtocol):
            def __init__(self, on_data):
                self.on_data = on_data
                self.buf = bytearray(1)

            def connection_made(self, tr):
                nonlocal client_con_made_calls
                client_con_made_calls += 1

            def get_buffer(self, sizehint):
                return self.buf

            def buffer_updated(self, nsize):
                assert nsize == 1
                self.on_data.set_result(bytes(self.buf[:nsize]))

            def eof_received(self):
                pass

        class ClientProtoSecond(asyncio.Protocol):
            def __init__(self, on_data, on_eof):
                self.on_data = on_data
                self.on_eof = on_eof
                self.con_made_cnt = 0

            def connection_made(self, tr):
                nonlocal client_con_made_calls
                client_con_made_calls += 1

            def data_received(self, data):
                self.on_data.set_result(data)

            def eof_received(self):
                self.on_eof.set_result(True)

        async def client(addr):
            await asyncio.sleep(0.5)

            on_data1 = self.loop.create_future()
            on_data2 = self.loop.create_future()
            on_eof = self.loop.create_future()

            tr, proto = await self.loop.create_connection(
                lambda: ClientProtoFirst(on_data1), *addr)

            tr.write(HELLO_MSG)
            new_tr = await self.loop.start_tls(tr, proto, client_context)

            self.assertEqual(await on_data1, b'O')
            new_tr.write(HELLO_MSG)

            new_tr.set_protocol(ClientProtoSecond(on_data2, on_eof))
            self.assertEqual(await on_data2, b'2')
            new_tr.write(HELLO_MSG)
            await on_eof

            new_tr.close()

            # connection_made() should be called only once -- when
            # we establish connection for the first time. Start TLS
            # doesn't call connection_made() on application protocols.
            self.assertEqual(client_con_made_calls, 1)

        with self.tcp_server(serve, timeout=self.TIMEOUT) as srv:
            self.loop.run_until_complete(
                asyncio.wait_for(client(srv.addr),
                                 timeout=self.TIMEOUT))

    def test_start_tls_slow_client_cancel(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        HELLO_MSG = b'1' * self.PAYLOAD_SIZE

        client_context = self._create_client_ssl_context()
        server_waits_on_handshake = self.loop.create_future()

        def serve(sock):
            sock.settimeout(self.TIMEOUT)

            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            try:
                self.loop.call_soon_threadsafe(
                    server_waits_on_handshake.set_result, None)
                data = sock.recv_all(1024 * 1024)
            except ConnectionAbortedError:
                pass
            finally:
                sock.close()

        class ClientProto(asyncio.Protocol):
            def __init__(self, on_data, on_eof):
                self.on_data = on_data
                self.on_eof = on_eof
                self.con_made_cnt = 0

            def connection_made(proto, tr):
                proto.con_made_cnt += 1
                # Ensure connection_made gets called only once.
                self.assertEqual(proto.con_made_cnt, 1)

            def data_received(self, data):
                self.on_data.set_result(data)

            def eof_received(self):
                self.on_eof.set_result(True)

        async def client(addr):
            await asyncio.sleep(0.5)

            on_data = self.loop.create_future()
            on_eof = self.loop.create_future()

            tr, proto = await self.loop.create_connection(
                lambda: ClientProto(on_data, on_eof), *addr)

            tr.write(HELLO_MSG)

            await server_waits_on_handshake

            with self.assertRaises(asyncio.TimeoutError):
                await asyncio.wait_for(
                    self.loop.start_tls(tr, proto, client_context),
                    0.5)

        with self.tcp_server(serve, timeout=self.TIMEOUT) as srv:
            self.loop.run_until_complete(
                asyncio.wait_for(client(srv.addr), timeout=10))

    def test_start_tls_server_1(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        HELLO_MSG = b'1' * self.PAYLOAD_SIZE

        server_context = self._create_server_ssl_context(
            self.ONLYCERT, self.ONLYKEY)
        client_context = self._create_client_ssl_context()

        def client(sock, addr):
            sock.settimeout(self.TIMEOUT)

            sock.connect(addr)
            data = sock.recv_all(len(HELLO_MSG))
            self.assertEqual(len(data), len(HELLO_MSG))

            sock.starttls(client_context)
            sock.sendall(HELLO_MSG)

            sock.unwrap()
            sock.close()

        class ServerProto(asyncio.Protocol):
            def __init__(self, on_con, on_eof, on_con_lost):
                self.on_con = on_con
                self.on_eof = on_eof
                self.on_con_lost = on_con_lost
                self.data = b''

            def connection_made(self, tr):
                self.on_con.set_result(tr)

            def data_received(self, data):
                self.data += data

            def eof_received(self):
                self.on_eof.set_result(1)

            def connection_lost(self, exc):
                if exc is None:
                    self.on_con_lost.set_result(None)
                else:
                    self.on_con_lost.set_exception(exc)

        async def main(proto, on_con, on_eof, on_con_lost):
            tr = await on_con
            tr.write(HELLO_MSG)

            self.assertEqual(proto.data, b'')

            new_tr = await self.loop.start_tls(
                tr, proto, server_context,
                server_side=True,
                ssl_handshake_timeout=self.TIMEOUT)

            await on_eof
            await on_con_lost
            self.assertEqual(proto.data, HELLO_MSG)
            new_tr.close()

        async def run_main():
            on_con = self.loop.create_future()
            on_eof = self.loop.create_future()
            on_con_lost = self.loop.create_future()
            proto = ServerProto(on_con, on_eof, on_con_lost)

            server = await self.loop.create_server(
                lambda: proto, '127.0.0.1', 0)
            addr = server.sockets[0].getsockname()

            with self.tcp_client(lambda sock: client(sock, addr),
                                 timeout=self.TIMEOUT):
                await asyncio.wait_for(
                    main(proto, on_con, on_eof, on_con_lost),
                    timeout=self.TIMEOUT)

            server.close()
            await server.wait_closed()

        self.loop.run_until_complete(run_main())

    def test_create_server_ssl_over_ssl(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest('asyncio does not support SSL over SSL')

        CNT = 0           # number of clients that were successful
        TOTAL_CNT = 25    # total number of clients that test will create
        TIMEOUT = 60.0    # timeout for this test

        A_DATA = b'A' * 1024 * 1024
        B_DATA = b'B' * 1024 * 1024

        sslctx_1 = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx_1 = self._create_client_ssl_context()
        sslctx_2 = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx_2 = self._create_client_ssl_context()

        clients = []

        async def handle_client(reader, writer):
            nonlocal CNT

            data = await reader.readexactly(len(A_DATA))
            self.assertEqual(data, A_DATA)
            writer.write(b'OK')

            data = await reader.readexactly(len(B_DATA))
            self.assertEqual(data, B_DATA)
            writer.writelines([b'SP', bytearray(b'A'), memoryview(b'M')])

            await writer.drain()
            writer.close()

            CNT += 1

        class ServerProtocol(asyncio.StreamReaderProtocol):
            def connection_made(self, transport):
                super_ = super()
                transport.pause_reading()
                fut = self._loop.create_task(self._loop.start_tls(
                    transport, self, sslctx_2, server_side=True))

                def cb(_):
                    try:
                        tr = fut.result()
                    except Exception as ex:
                        super_.connection_lost(ex)
                    else:
                        super_.connection_made(tr)
                fut.add_done_callback(cb)

        def server_protocol_factory():
            reader = asyncio.StreamReader()
            protocol = ServerProtocol(reader, handle_client)
            return protocol

        async def test_client(addr):
            fut = asyncio.Future()

            def prog(sock):
                try:
                    sock.connect(addr)
                    sock.starttls(client_sslctx_1)

                    # because wrap_socket() doesn't work correctly on
                    # SSLSocket, we have to do the 2nd level SSL manually
                    incoming = ssl.MemoryBIO()
                    outgoing = ssl.MemoryBIO()
                    sslobj = client_sslctx_2.wrap_bio(incoming, outgoing)

                    def do(func, *args):
                        while True:
                            try:
                                rv = func(*args)
                                break
                            except ssl.SSLWantReadError:
                                if outgoing.pending:
                                    sock.send(outgoing.read())
                                incoming.write(sock.recv(65536))
                        if outgoing.pending:
                            sock.send(outgoing.read())
                        return rv

                    do(sslobj.do_handshake)

                    do(sslobj.write, A_DATA)
                    data = do(sslobj.read, 2)
                    self.assertEqual(data, b'OK')

                    do(sslobj.write, B_DATA)
                    data = b''
                    while True:
                        chunk = do(sslobj.read, 4)
                        if not chunk:
                            break
                        data += chunk
                    self.assertEqual(data, b'SPAM')

                    do(sslobj.unwrap)
                    sock.close()

                except Exception as ex:
                    self.loop.call_soon_threadsafe(fut.set_exception, ex)
                    sock.close()
                else:
                    self.loop.call_soon_threadsafe(fut.set_result, None)

            client = self.tcp_client(prog)
            client.start()
            clients.append(client)

            await fut

        async def start_server():
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

            srv = await self.loop.create_server(
                server_protocol_factory,
                '127.0.0.1', 0,
                family=socket.AF_INET,
                ssl=sslctx_1,
                **extras)

            try:
                srv_socks = srv.sockets
                self.assertTrue(srv_socks)

                addr = srv_socks[0].getsockname()

                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(test_client(addr))

                await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

            finally:
                self.loop.call_soon(srv.close)
                await srv.wait_closed()

        with self._silence_eof_received_warning():
            self.loop.run_until_complete(start_server())

        self.assertEqual(CNT, TOTAL_CNT)

        for client in clients:
            client.stop()

    def test_renegotiation(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest('asyncio does not support renegotiation')

        CNT = 0
        TOTAL_CNT = 25

        A_DATA = b'A' * 1024 * 1024
        B_DATA = b'B' * 1024 * 1024

        sslctx = openssl_ssl.Context(openssl_ssl.TLSv1_2_METHOD)
        if hasattr(openssl_ssl, 'OP_NO_SSLV2'):
            sslctx.set_options(openssl_ssl.OP_NO_SSLV2)
        sslctx.use_privatekey_file(self.ONLYKEY)
        sslctx.use_certificate_chain_file(self.ONLYCERT)
        client_sslctx = self._create_client_ssl_context()
        client_sslctx.maximum_version = ssl.TLSVersion.TLSv1_2

        def server(sock):
            conn = openssl_ssl.Connection(sslctx, sock)
            conn.set_accept_state()

            data = b''
            while len(data) < len(A_DATA):
                try:
                    chunk = conn.recv(len(A_DATA) - len(data))
                    if not chunk:
                        break
                    data += chunk
                except openssl_ssl.WantReadError:
                    pass
            self.assertEqual(data, A_DATA)
            conn.renegotiate()
            if conn.renegotiate_pending():
                conn.send(b'OK')
            else:
                conn.send(b'ER')

            data = b''
            while len(data) < len(B_DATA):
                try:
                    chunk = conn.recv(len(B_DATA) - len(data))
                    if not chunk:
                        break
                    data += chunk
                except openssl_ssl.WantReadError:
                    pass
            self.assertEqual(data, B_DATA)
            if conn.renegotiate_pending():
                conn.send(b'ERRO')
            else:
                conn.send(b'SPAM')

            conn.shutdown()

        async def client(addr):
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='',
                **extras)

            writer.write(A_DATA)
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(B_DATA)
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            nonlocal CNT
            CNT += 1

            writer.close()
            await self.wait_closed(writer)

        async def client_sock(addr):
            sock = socket.socket()
            sock.connect(addr)
            reader, writer = await asyncio.open_connection(
                sock=sock,
                ssl=client_sslctx,
                server_hostname='')

            writer.write(A_DATA)
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(B_DATA)
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            nonlocal CNT
            CNT += 1

            writer.close()
            await self.wait_closed(writer)
            sock.close()

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.tcp_server(server,
                                 max_clients=TOTAL_CNT,
                                 backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(
                    asyncio.gather(*tasks))

            self.assertEqual(CNT, TOTAL_CNT)

        with self._silence_eof_received_warning():
            run(client)

        with self._silence_eof_received_warning():
            run(client_sock)

    def test_shutdown_timeout(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        CNT = 0           # number of clients that were successful
        TOTAL_CNT = 25    # total number of clients that test will create
        TIMEOUT = 10.0    # timeout for this test

        A_DATA = b'A' * 1024 * 1024

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()

        clients = []

        async def handle_client(reader, writer):
            nonlocal CNT

            data = await reader.readexactly(len(A_DATA))
            self.assertEqual(data, A_DATA)
            writer.write(b'OK')
            await writer.drain()
            writer.close()
            with self.assertRaisesRegex(asyncio.TimeoutError,
                                        'SSL shutdown timed out'):
                await reader.read()
            CNT += 1

        async def test_client(addr):
            fut = asyncio.Future()

            def prog(sock):
                try:
                    sock.starttls(client_sslctx)
                    sock.connect(addr)
                    sock.send(A_DATA)

                    data = sock.recv_all(2)
                    self.assertEqual(data, b'OK')

                    data = sock.recv(1024)
                    self.assertEqual(data, b'')

                    fd = sock.detach()
                    try:
                        select.select([fd], [], [], 3)
                    finally:
                        os.close(fd)

                except Exception as ex:
                    self.loop.call_soon_threadsafe(fut.set_exception, ex)
                else:
                    self.loop.call_soon_threadsafe(fut.set_result, None)

            client = self.tcp_client(prog)
            client.start()
            clients.append(client)

            await fut

        async def start_server():
            extras = {'ssl_handshake_timeout': SSL_HANDSHAKE_TIMEOUT}
            if self.implementation != 'asyncio':  # or self.PY38
                extras['ssl_shutdown_timeout'] = 0.5

            srv = await asyncio.start_server(
                handle_client,
                '127.0.0.1', 0,
                family=socket.AF_INET,
                ssl=sslctx,
                **extras)

            try:
                srv_socks = srv.sockets
                self.assertTrue(srv_socks)

                addr = srv_socks[0].getsockname()

                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(test_client(addr))

                await asyncio.wait_for(
                    asyncio.gather(*tasks),
                    TIMEOUT)

            finally:
                self.loop.call_soon(srv.close)
                await srv.wait_closed()

        with self._silence_eof_received_warning():
            self.loop.run_until_complete(start_server())

        self.assertEqual(CNT, TOTAL_CNT)

        for client in clients:
            client.stop()

    def test_shutdown_cleanly(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        CNT = 0
        TOTAL_CNT = 25

        A_DATA = b'A' * 1024 * 1024

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()

        def server(sock):
            sock.starttls(
                sslctx,
                server_side=True)

            data = sock.recv_all(len(A_DATA))
            self.assertEqual(data, A_DATA)
            sock.send(b'OK')

            sock.unwrap()

            sock.close()

        async def client(addr):
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='',
                **extras)

            writer.write(A_DATA)
            self.assertEqual(await reader.readexactly(2), b'OK')

            self.assertEqual(await reader.read(), b'')

            nonlocal CNT
            CNT += 1

            writer.close()
            await self.wait_closed(writer)

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.tcp_server(server,
                                 max_clients=TOTAL_CNT,
                                 backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(
                    asyncio.gather(*tasks))

            self.assertEqual(CNT, TOTAL_CNT)

        with self._silence_eof_received_warning():
            run(client)

    def test_write_to_closed_transport(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()
        future = None

        def server(sock):
            sock.starttls(sslctx, server_side=True)
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()

        def unwrap_server(sock):
            sock.starttls(sslctx, server_side=True)
            while True:
                try:
                    sock.unwrap()
                    break
                except ssl.SSLError as ex:
                    # Since OpenSSL 1.1.1, it raises "application data after
                    # close notify"
                    # Python < 3.8:
                    if ex.reason == 'KRB5_S_INIT':
                        break
                    # Python >= 3.8:
                    if ex.reason == 'APPLICATION_DATA_AFTER_CLOSE_NOTIFY':
                        break
                    raise ex
                except OSError as ex:
                    # OpenSSL < 1.1.1
                    if ex.errno != 0:
                        raise
            sock.close()

        async def client(addr):
            nonlocal future
            future = self.loop.create_future()

            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='')
            writer.write(b'I AM WRITING NOWHERE1' * 100)

            try:
                data = await reader.read()
                self.assertEqual(data, b'')
            except (ConnectionResetError, BrokenPipeError):
                pass

            for i in range(25):
                writer.write(b'I AM WRITING NOWHERE2' * 100)

            self.assertEqual(
                writer.transport.get_write_buffer_size(), 0)

            await future

            writer.close()
            await self.wait_closed(writer)

        def run(meth):
            def wrapper(sock):
                try:
                    meth(sock)
                except Exception as ex:
                    self.loop.call_soon_threadsafe(future.set_exception, ex)
                else:
                    self.loop.call_soon_threadsafe(future.set_result, None)
            return wrapper

        with self._silence_eof_received_warning():
            with self.tcp_server(run(server)) as srv:
                self.loop.run_until_complete(client(srv.addr))

            with self.tcp_server(run(unwrap_server)) as srv:
                self.loop.run_until_complete(client(srv.addr))

    def test_flush_before_shutdown(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        CHUNK = 1024 * 128
        SIZE = 32

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        sslctx_openssl = openssl_ssl.Context(openssl_ssl.TLSv1_2_METHOD)
        if hasattr(openssl_ssl, 'OP_NO_SSLV2'):
            sslctx_openssl.set_options(openssl_ssl.OP_NO_SSLV2)
        sslctx_openssl.use_privatekey_file(self.ONLYKEY)
        sslctx_openssl.use_certificate_chain_file(self.ONLYCERT)
        client_sslctx = self._create_client_ssl_context()
        client_sslctx.maximum_version = ssl.TLSVersion.TLSv1_2

        future = None

        def server(sock):
            sock.starttls(sslctx, server_side=True)
            self.assertEqual(sock.recv_all(4), b'ping')
            sock.send(b'pong')
            time.sleep(0.5)  # hopefully stuck the TCP buffer
            data = sock.recv_all(CHUNK * SIZE)
            self.assertEqual(len(data), CHUNK * SIZE)
            sock.close()

        def run(meth):
            def wrapper(sock):
                try:
                    meth(sock)
                except Exception as ex:
                    self.loop.call_soon_threadsafe(future.set_exception, ex)
                else:
                    self.loop.call_soon_threadsafe(future.set_result, None)
            return wrapper

        async def client(addr):
            nonlocal future
            future = self.loop.create_future()
            reader, writer = await asyncio.open_connection(
                *addr,
                ssl=client_sslctx,
                server_hostname='')
            sslprotocol = writer.get_extra_info('uvloop.sslproto')
            writer.write(b'ping')
            data = await reader.readexactly(4)
            self.assertEqual(data, b'pong')

            sslprotocol.pause_writing()
            for _ in range(SIZE):
                writer.write(b'x' * CHUNK)

            writer.close()
            sslprotocol.resume_writing()

            await self.wait_closed(writer)
            try:
                data = await reader.read()
                self.assertEqual(data, b'')
            except ConnectionResetError:
                pass
            await future

        with self.tcp_server(run(server)) as srv:
            self.loop.run_until_complete(client(srv.addr))

    def test_remote_shutdown_receives_trailing_data(self):
        if sys.platform == 'linux' and sys.version_info < (3, 11):
            # TODO: started hanging and needs to be diagnosed.
            raise unittest.SkipTest()

        CHUNK = 1024 * 16
        SIZE = 8
        count = 0

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()
        future = None
        filled = threading.Lock()
        eof_received = threading.Lock()

        def server(sock):
            incoming = ssl.MemoryBIO()
            outgoing = ssl.MemoryBIO()
            sslobj = sslctx.wrap_bio(incoming, outgoing, server_side=True)

            while True:
                try:
                    sslobj.do_handshake()
                except ssl.SSLWantReadError:
                    if outgoing.pending:
                        sock.send(outgoing.read())
                    incoming.write(sock.recv(16384))
                else:
                    if outgoing.pending:
                        sock.send(outgoing.read())
                    break

            while True:
                try:
                    data = sslobj.read(4)
                except ssl.SSLWantReadError:
                    incoming.write(sock.recv(16384))
                else:
                    break

            self.assertEqual(data, b'ping')
            sslobj.write(b'pong')
            sock.send(outgoing.read())

            data_len = 0

            with filled:
                # trigger peer's resume_writing()
                incoming.write(sock.recv(65536 * 4))
                while True:
                    try:
                        chunk = len(sslobj.read(16384))
                        data_len += chunk
                    except ssl.SSLWantReadError:
                        break

                # send close_notify but don't wait for response
                with self.assertRaises(ssl.SSLWantReadError):
                    sslobj.unwrap()
                sock.send(outgoing.read())

            with eof_received:
                # should receive all data
                while True:
                    try:
                        chunk = len(sslobj.read(16384))
                        data_len += chunk
                    except ssl.SSLWantReadError:
                        incoming.write(sock.recv(16384))
                        if not incoming.pending:
                            # EOF received
                            break
                    except ssl.SSLZeroReturnError:
                        break

            self.assertEqual(data_len, CHUNK * count)

            if self.implementation == 'uvloop':
                # Verify that close_notify is received. asyncio is currently
                # not guaranteed to send close_notify before dropping off
                sslobj.unwrap()

            sock.close()

        async def client(addr):
            nonlocal future, count
            future = self.loop.create_future()

            with eof_received:
                with filled:
                    reader, writer = await asyncio.open_connection(
                        *addr,
                        ssl=client_sslctx,
                        server_hostname='')
                    writer.write(b'ping')
                    data = await reader.readexactly(4)
                    self.assertEqual(data, b'pong')

                    count = 0
                    try:
                        while True:
                            writer.write(b'x' * CHUNK)
                            count += 1
                            await asyncio.wait_for(
                                asyncio.ensure_future(writer.drain()), 0.5)
                    except asyncio.TimeoutError:
                        # fill write backlog in a hacky way for uvloop
                        if self.implementation == 'uvloop':
                            for _ in range(SIZE):
                                writer.transport._test__append_write_backlog(
                                    b'x' * CHUNK)
                                count += 1

                data = await reader.read()
                self.assertEqual(data, b'')

            await future

            writer.close()
            await self.wait_closed(writer)

        def run(meth):
            def wrapper(sock):
                try:
                    meth(sock)
                except Exception as ex:
                    self.loop.call_soon_threadsafe(future.set_exception, ex)
                else:
                    self.loop.call_soon_threadsafe(future.set_result, None)
            return wrapper

        with self.tcp_server(run(server)) as srv:
            self.loop.run_until_complete(client(srv.addr))

    def test_connect_timeout_warning(self):
        s = socket.socket(socket.AF_INET)
        s.bind(('127.0.0.1', 0))
        addr = s.getsockname()

        async def test():
            try:
                await asyncio.wait_for(
                    self.loop.create_connection(asyncio.Protocol,
                                                *addr, ssl=True),
                    0.1)
            except (ConnectionRefusedError, asyncio.TimeoutError):
                pass
            else:
                self.fail('TimeoutError is not raised')

        with s:
            try:
                with self.assertWarns(ResourceWarning) as cm:
                    self.loop.run_until_complete(test())
                    gc.collect()
                    gc.collect()
                    gc.collect()
            except AssertionError as e:
                self.assertEqual(str(e), 'ResourceWarning not triggered')
            else:
                self.fail('Unexpected ResourceWarning: {}'.format(cm.warning))

    def test_handshake_timeout_handler_leak(self):
        if self.implementation == 'asyncio':
            # Okay this turns out to be an issue for asyncio.sslproto too
            raise unittest.SkipTest()

        s = socket.socket(socket.AF_INET)
        s.bind(('127.0.0.1', 0))
        s.listen(1)
        addr = s.getsockname()

        async def test(ctx):
            try:
                await asyncio.wait_for(
                    self.loop.create_connection(asyncio.Protocol, *addr,
                                                ssl=ctx),
                    0.1)
            except (ConnectionRefusedError, asyncio.TimeoutError):
                pass
            else:
                self.fail('TimeoutError is not raised')

        with s:
            ctx = ssl.create_default_context()
            self.loop.run_until_complete(test(ctx))
            ctx = weakref.ref(ctx)

        # SSLProtocol should be DECREF to 0
        self.assertIsNone(ctx())

    def test_shutdown_timeout_handler_leak(self):
        loop = self.loop

        def server(sock):
            sslctx = self._create_server_ssl_context(self.ONLYCERT,
                                                     self.ONLYKEY)
            sock = sslctx.wrap_socket(sock, server_side=True)
            sock.recv(32)
            sock.close()

        class Protocol(asyncio.Protocol):
            def __init__(self):
                self.fut = asyncio.Future(loop=loop)

            def connection_lost(self, exc):
                self.fut.set_result(None)

        async def client(addr, ctx):
            tr, pr = await loop.create_connection(Protocol, *addr, ssl=ctx)
            tr.close()
            await pr.fut

        with self.tcp_server(server) as srv:
            ctx = self._create_client_ssl_context()
            loop.run_until_complete(client(srv.addr, ctx))
            ctx = weakref.ref(ctx)

        if self.implementation == 'asyncio':
            # asyncio has no shutdown timeout, but it ends up with a circular
            # reference loop - not ideal (introduces gc glitches), but at least
            # not leaking
            gc.collect()
            gc.collect()
            gc.collect()

        # SSLProtocol should be DECREF to 0
        self.assertIsNone(ctx())

    def test_shutdown_timeout_handler_not_set(self):
        if self.implementation == 'asyncio':
            # asyncio doesn't call SSL eof_received() so we can't run this test
            raise unittest.SkipTest()

        loop = self.loop
        extra = None

        def server(sock):
            sslctx = self._create_server_ssl_context(self.ONLYCERT,
                                                     self.ONLYKEY)
            sock = sslctx.wrap_socket(sock, server_side=True)
            sock.send(b'hello')
            assert sock.recv(1024) == b'world'
            sock.send(b'extra bytes')
            # sending EOF here
            sock.shutdown(socket.SHUT_WR)
            # make sure we have enough time to reproduce the issue
            self.assertEqual(sock.recv(1024), b'')
            sock.close()

        class Protocol(asyncio.Protocol):
            def __init__(self):
                self.fut = asyncio.Future(loop=loop)
                self.transport = None

            def connection_made(self, transport):
                self.transport = transport

            def data_received(self, data):
                if data == b'hello':
                    self.transport.write(b'world')
                    # pause reading would make incoming data stay in the sslobj
                    self.transport.pause_reading()
                else:
                    nonlocal extra
                    extra = data

            def connection_lost(self, exc):
                if exc is None:
                    self.fut.set_result(None)
                else:
                    self.fut.set_exception(exc)

            def eof_received(self):
                self.transport.resume_reading()

        async def client(addr):
            ctx = self._create_client_ssl_context()
            tr, pr = await loop.create_connection(Protocol, *addr, ssl=ctx)
            await pr.fut
            tr.close()
            # extra data received after transport.close() should be ignored
            self.assertIsNone(extra)

        with self.tcp_server(server) as srv:
            loop.run_until_complete(client(srv.addr))

    def test_shutdown_while_pause_reading(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        loop = self.loop
        conn_made = loop.create_future()
        eof_recvd = loop.create_future()
        conn_lost = loop.create_future()
        data_recv = False

        def server(sock):
            sslctx = self._create_server_ssl_context(self.ONLYCERT,
                                                     self.ONLYKEY)
            incoming = ssl.MemoryBIO()
            outgoing = ssl.MemoryBIO()
            sslobj = sslctx.wrap_bio(incoming, outgoing, server_side=True)

            while True:
                try:
                    sslobj.do_handshake()
                    sslobj.write(b'trailing data')
                    break
                except ssl.SSLWantReadError:
                    if outgoing.pending:
                        sock.send(outgoing.read())
                    incoming.write(sock.recv(16384))
            if outgoing.pending:
                sock.send(outgoing.read())

            while True:
                try:
                    self.assertEqual(sslobj.read(), b'')  # close_notify
                    break
                except ssl.SSLWantReadError:
                    incoming.write(sock.recv(16384))

            while True:
                try:
                    sslobj.unwrap()
                except ssl.SSLWantReadError:
                    if outgoing.pending:
                        sock.send(outgoing.read())
                    incoming.write(sock.recv(16384))
                else:
                    if outgoing.pending:
                        sock.send(outgoing.read())
                    break

            self.assertEqual(sock.recv(16384), b'')  # socket closed

        class Protocol(asyncio.Protocol):
            def connection_made(self, transport):
                conn_made.set_result(None)

            def data_received(self, data):
                nonlocal data_recv
                data_recv = True

            def eof_received(self):
                eof_recvd.set_result(None)

            def connection_lost(self, exc):
                if exc is None:
                    conn_lost.set_result(None)
                else:
                    conn_lost.set_exception(exc)

        async def client(addr):
            ctx = self._create_client_ssl_context()
            tr, _ = await loop.create_connection(Protocol, *addr, ssl=ctx)
            await conn_made
            self.assertFalse(data_recv)

            tr.pause_reading()
            tr.close()

            await asyncio.wait_for(eof_recvd, 10)
            await asyncio.wait_for(conn_lost, 10)

        with self.tcp_server(server) as srv:
            loop.run_until_complete(client(srv.addr))

    def test_bpo_39951_discard_trailing_data(self):
        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()
        future = None
        close_notify = threading.Lock()

        def server(sock):
            incoming = ssl.MemoryBIO()
            outgoing = ssl.MemoryBIO()
            sslobj = sslctx.wrap_bio(incoming, outgoing, server_side=True)

            while True:
                try:
                    sslobj.do_handshake()
                except ssl.SSLWantReadError:
                    if outgoing.pending:
                        sock.send(outgoing.read())
                    incoming.write(sock.recv(16384))
                else:
                    if outgoing.pending:
                        sock.send(outgoing.read())
                    break

            while True:
                try:
                    data = sslobj.read(4)
                except ssl.SSLWantReadError:
                    incoming.write(sock.recv(16384))
                else:
                    break

            self.assertEqual(data, b'ping')
            sslobj.write(b'pong')
            sock.send(outgoing.read())

            with close_notify:
                sslobj.write(b'trailing')
                sock.send(outgoing.read())
                time.sleep(0.5)  # allow time for the client to receive

            incoming.write(sock.recv(16384))
            sslobj.unwrap()
            sock.send(outgoing.read())
            sock.close()

        async def client(addr):
            nonlocal future
            future = self.loop.create_future()

            with close_notify:
                reader, writer = await asyncio.open_connection(
                    *addr,
                    ssl=client_sslctx,
                    server_hostname='')
                writer.write(b'ping')
                data = await reader.readexactly(4)
                self.assertEqual(data, b'pong')

                writer.close()

            try:
                await self.wait_closed(writer)
            except ssl.SSLError as e:
                if self.implementation == 'asyncio' and \
                        'application data after close notify' in str(e):
                    raise unittest.SkipTest('bpo-39951')
                raise
            await future

        def run(meth):
            def wrapper(sock):
                try:
                    meth(sock)
                except Exception as ex:
                    self.loop.call_soon_threadsafe(future.set_exception, ex)
                else:
                    self.loop.call_soon_threadsafe(future.set_result, None)
            return wrapper

        with self.tcp_server(run(server)) as srv:
            self.loop.run_until_complete(client(srv.addr))

    def test_first_data_after_wakeup(self):
        if self.implementation == 'asyncio':
            raise unittest.SkipTest()

        server_context = self._create_server_ssl_context(
            self.ONLYCERT, self.ONLYKEY)
        client_context = self._create_client_ssl_context()
        loop = self.loop
        this = self
        fut = self.loop.create_future()

        def client(sock, addr):
            try:
                sock.connect(addr)

                incoming = ssl.MemoryBIO()
                outgoing = ssl.MemoryBIO()
                sslobj = client_context.wrap_bio(incoming, outgoing)

                # Do handshake manually so that we could collect the last piece
                while True:
                    try:
                        sslobj.do_handshake()
                        break
                    except ssl.SSLWantReadError:
                        if outgoing.pending:
                            sock.send(outgoing.read())
                        incoming.write(sock.recv(65536))

                # Send the first data together with the last handshake payload
                sslobj.write(b'hello')
                sock.send(outgoing.read())

                while True:
                    try:
                        incoming.write(sock.recv(65536))
                        self.assertEqual(sslobj.read(1024), b'hello')
                        break
                    except ssl.SSLWantReadError:
                        pass

                sock.close()

            except Exception as ex:
                loop.call_soon_threadsafe(fut.set_exception, ex)
                sock.close()
            else:
                loop.call_soon_threadsafe(fut.set_result, None)

        class EchoProto(asyncio.Protocol):
            def connection_made(self, tr):
                self.tr = tr
                # manually run the coroutine, in order to avoid accidental data
                coro = loop.start_tls(
                    tr, self, server_context,
                    server_side=True,
                    ssl_handshake_timeout=this.TIMEOUT,
                )
                waiter = coro.send(None)

                def tls_started(_):
                    try:
                        coro.send(None)
                    except StopIteration as e:
                        # update self.tr to SSL transport as soon as we know it
                        self.tr = e.value

                waiter.add_done_callback(tls_started)

            def data_received(self, data):
                # This is a dumb protocol that writes back whatever it receives
                # regardless of whether self.tr is SSL or not
                self.tr.write(data)

        async def run_main():
            proto = EchoProto()

            server = await self.loop.create_server(
                lambda: proto, '127.0.0.1', 0)
            addr = server.sockets[0].getsockname()

            with self.tcp_client(lambda sock: client(sock, addr),
                                 timeout=self.TIMEOUT):
                await asyncio.wait_for(fut, timeout=self.TIMEOUT)
                proto.tr.close()

            server.close()
            await server.wait_closed()

        self.loop.run_until_complete(run_main())


class Test_UV_TCPSSL(_TestSSL, tb.UVTestCase):
    pass


class Test_AIO_TCPSSL(_TestSSL, tb.AIOTestCase):
    pass
```

## File: `tests/test_testbase.py`
```python
import unittest

from uvloop import _testbase as tb


class TestBaseTest(unittest.TestCase):

    def test_duplicate_methods(self):
        with self.assertRaisesRegex(RuntimeError, 'duplicate test Foo.test_a'):

            class Foo(tb.BaseTestCase):
                def test_a(self):
                    pass

                def test_b(self):
                    pass

                def test_a(self):  # NOQA
                    pass

    def test_duplicate_methods_parent_1(self):
        class FooBase:
            def test_a(self):
                pass

        with self.assertRaisesRegex(RuntimeError,
                                    'duplicate test Foo.test_a.*'
                                    'defined in FooBase'):

            class Foo(FooBase, tb.BaseTestCase):
                def test_b(self):
                    pass

                def test_a(self):
                    pass

    def test_duplicate_methods_parent_2(self):
        class FooBase(tb.BaseTestCase):
            def test_a(self):
                pass

        with self.assertRaisesRegex(RuntimeError,
                                    'duplicate test Foo.test_a.*'
                                    'defined in FooBase'):

            class Foo(FooBase):
                def test_b(self):
                    pass

                def test_a(self):
                    pass
```

## File: `tests/test_udp.py`
```python
import asyncio
import os
import socket
import sys
import tempfile
import unittest
import uuid

from uvloop import _testbase as tb


class MyDatagramProto(asyncio.DatagramProtocol):
    done = None

    def __init__(self, loop=None):
        self.state = 'INITIAL'
        self.nbytes = 0
        if loop is not None:
            self.done = asyncio.Future(loop=loop)

    def connection_made(self, transport):
        self.transport = transport
        assert self.state == 'INITIAL', self.state
        self.state = 'INITIALIZED'

    def datagram_received(self, data, addr):
        assert self.state == 'INITIALIZED', self.state
        self.nbytes += len(data)

    def error_received(self, exc):
        assert self.state == 'INITIALIZED', self.state
        raise exc

    def connection_lost(self, exc):
        assert self.state == 'INITIALIZED', self.state
        self.state = 'CLOSED'
        if self.done:
            self.done.set_result(None)


class _TestUDP:

    def _test_create_datagram_endpoint_addrs(self, family, lc_addr):
        class TestMyDatagramProto(MyDatagramProto):
            def __init__(inner_self):
                super().__init__(loop=self.loop)

            def datagram_received(self, data, addr):
                super().datagram_received(data, addr)
                self.transport.sendto(b'resp:' + data, addr)

        coro = self.loop.create_datagram_endpoint(
            TestMyDatagramProto,
            local_addr=lc_addr,
            family=family)

        s_transport, server = self.loop.run_until_complete(coro)

        remote_addr = s_transport.get_extra_info('sockname')
        host, port, *_ = remote_addr

        self.assertIsInstance(server, TestMyDatagramProto)
        self.assertEqual('INITIALIZED', server.state)
        self.assertIs(server.transport, s_transport)

        extra = {}
        if hasattr(socket, 'SO_REUSEPORT'):
            extra['reuse_port'] = True

        coro = self.loop.create_datagram_endpoint(
            lambda: MyDatagramProto(loop=self.loop),
            family=family,
            remote_addr=(host, port),
            **extra)
        transport, client = self.loop.run_until_complete(coro)

        self.assertIsInstance(client, MyDatagramProto)
        self.assertEqual('INITIALIZED', client.state)
        self.assertIs(client.transport, transport)

        transport.sendto(b'xxx')
        tb.run_until(self.loop, lambda: server.nbytes)
        self.assertEqual(3, server.nbytes)
        tb.run_until(self.loop, lambda: client.nbytes)

        # received
        self.assertEqual(8, client.nbytes)

        # https://github.com/MagicStack/uvloop/issues/319
        # uvloop should behave the same as asyncio when given remote_addr
        transport.sendto(b'xxx', remote_addr)
        tb.run_until(
            self.loop, lambda: server.nbytes > 3 or client.done.done())
        self.assertEqual(6, server.nbytes)
        tb.run_until(self.loop, lambda: client.nbytes > 8)

        # received
        self.assertEqual(16, client.nbytes)

        # reject sendto with a different port
        with self.assertRaisesRegex(
            ValueError, "Invalid address.*" + repr(remote_addr)
        ):
            bad_addr = list(remote_addr)
            bad_addr[1] += 1
            bad_addr = tuple(bad_addr)
            transport.sendto(b"xxx", bad_addr)

        # reject sento with unresolved hostname
        if remote_addr[0] != lc_addr[0]:
            with self.assertRaisesRegex(
                ValueError, "Invalid address.*" + repr(remote_addr)
            ):
                bad_addr = list(remote_addr)
                bad_addr[0] = lc_addr[0]
                bad_addr = tuple(bad_addr)
                transport.sendto(b"xxx", bad_addr)

        # extra info is available
        self.assertIsNotNone(transport.get_extra_info('sockname'))

        # close connection
        transport.close()
        self.loop.run_until_complete(client.done)
        self.assertEqual('CLOSED', client.state)
        server.transport.close()
        self.loop.run_until_complete(server.done)

    def test_create_datagram_endpoint_addrs_ipv4(self):
        self._test_create_datagram_endpoint_addrs(
            socket.AF_INET, ('127.0.0.1', 0))

    def test_create_datagram_endpoint_addrs_ipv4_nameaddr(self):
        self._test_create_datagram_endpoint_addrs(
            socket.AF_INET, ('localhost', 0))

    def _test_create_datagram_endpoint_addrs_ipv6(self):
        self._test_create_datagram_endpoint_addrs(
            socket.AF_INET6, ('::1', 0))

    def test_create_datagram_endpoint_ipv6_family(self):
        class TestMyDatagramProto(MyDatagramProto):
            def __init__(inner_self):
                super().__init__(loop=self.loop)

            def datagram_received(self, data, addr):
                super().datagram_received(data, addr)
                self.transport.sendto(b'resp:' + data, addr)

        coro = self.loop.create_datagram_endpoint(
            TestMyDatagramProto, local_addr=None, family=socket.AF_INET6)
        s_transport = None
        try:
            s_transport, server = self.loop.run_until_complete(coro)
        finally:
            if s_transport:
                s_transport.close()
                # let it close
                self.loop.run_until_complete(
                    asyncio.sleep(0.1))

    def test_create_datagram_endpoint_sock(self):
        sock = None
        local_address = ('127.0.0.1', 0)
        infos = self.loop.run_until_complete(
            self.loop.getaddrinfo(
                *local_address, type=socket.SOCK_DGRAM))
        for family, type, proto, cname, address in infos:
            try:
                sock = socket.socket(family=family, type=type, proto=proto)
                sock.setblocking(False)
                sock.bind(address)
            except Exception:
                pass
            else:
                break
        else:
            assert False, 'Can not create socket.'

        with sock:
            f = self.loop.create_datagram_endpoint(
                lambda: MyDatagramProto(loop=self.loop), sock=sock)
            tr, pr = self.loop.run_until_complete(f)
            self.assertIsInstance(pr, MyDatagramProto)
            tr.close()
            self.loop.run_until_complete(pr.done)

    def test_create_datagram_endpoint_sock_unix_domain(self):

        class Proto(asyncio.DatagramProtocol):
            done = None

            def __init__(self, loop):
                self.state = 'INITIAL'
                self.addrs = set()
                self.done = asyncio.Future(loop=loop)
                self.data = b''

            def connection_made(self, transport):
                self.transport = transport
                assert self.state == 'INITIAL', self.state
                self.state = 'INITIALIZED'

            def datagram_received(self, data, addr):
                assert self.state == 'INITIALIZED', self.state
                self.addrs.add(addr)
                self.data += data
                if self.data == b'STOP' and not self.done.done():
                    self.done.set_result(True)

            def error_received(self, exc):
                assert self.state == 'INITIALIZED', self.state
                if not self.done.done():
                    self.done.set_exception(exc or RuntimeError())

            def connection_lost(self, exc):
                assert self.state == 'INITIALIZED', self.state
                self.state = 'CLOSED'
                if self.done and not self.done.done():
                    self.done.set_result(None)

        tmp_file = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        sock = socket.socket(socket.AF_UNIX, type=socket.SOCK_DGRAM)
        sock.bind(tmp_file)

        with sock:
            pr = Proto(loop=self.loop)
            f = self.loop.create_datagram_endpoint(
                lambda: pr, sock=sock)
            tr, pr_prime = self.loop.run_until_complete(f)
            self.assertIs(pr, pr_prime)

            tmp_file2 = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
            sock2 = socket.socket(socket.AF_UNIX, type=socket.SOCK_DGRAM)
            sock2.bind(tmp_file2)

            with sock2:
                f2 = self.loop.create_datagram_endpoint(
                    asyncio.DatagramProtocol, sock=sock2)
                tr2, pr2 = self.loop.run_until_complete(f2)

                tr2.sendto(b'STOP', tmp_file)

                self.loop.run_until_complete(pr.done)

                tr.close()
                tr2.close()

                # Let transports close
                self.loop.run_until_complete(asyncio.sleep(0.2))

                self.assertIn(tmp_file2, pr.addrs)

    def test_create_datagram_1(self):
        server_addr = ('127.0.0.1', 8888)
        client_addr = ('127.0.0.1', 0)

        async def run():
            server_transport, client_protocol = \
                await self.loop.create_datagram_endpoint(
                    asyncio.DatagramProtocol,
                    local_addr=server_addr)

            client_transport, client_conn = \
                await self.loop.create_datagram_endpoint(
                    asyncio.DatagramProtocol,
                    remote_addr=server_addr,
                    local_addr=client_addr)

            client_transport.close()
            server_transport.close()

            # let transports close
            await asyncio.sleep(0.1)

        self.loop.run_until_complete(run())

    def test_socketpair(self):
        peername = asyncio.Future(loop=self.loop)

        class Proto(MyDatagramProto):
            def datagram_received(self, data, addr):
                super().datagram_received(data, addr)
                peername.set_result(addr)

        s1, s2 = socket.socketpair(socket.AF_UNIX, socket.SOCK_DGRAM, 0)

        with s1, s2:
            f = self.loop.create_datagram_endpoint(
                lambda: Proto(loop=self.loop), sock=s1)
            tr, pr = self.loop.run_until_complete(f)
            self.assertIsInstance(pr, Proto)

            s2.send(b'hello, socketpair')
            addr = self.loop.run_until_complete(
                asyncio.wait_for(peername, 1))
            if sys.platform.startswith('linux'):
                self.assertEqual(addr, None)
            else:
                self.assertEqual(addr, '')
            self.assertEqual(pr.nbytes, 17)

            if not self.is_asyncio_loop():
                # asyncio doesn't support sendto(xx) on UDP sockets
                # https://git.io/Jfqbw
                data = b'from uvloop'
                tr.sendto(data)
                result = self.loop.run_until_complete(asyncio.wait_for(
                    self.loop.run_in_executor(None, s2.recv, 1024),
                    1))
                self.assertEqual(data, result)

            tr.close()
            self.loop.run_until_complete(pr.done)

    def _skip_create_datagram_endpoint_reuse_addr(self):
        if self.implementation == 'asyncio':
            if sys.version_info[:2] >= (3, 11):
                raise unittest.SkipTest()
            if (3, 8, 0) <= sys.version_info < (3, 8, 1):
                raise unittest.SkipTest()

    def test_create_datagram_endpoint_reuse_address_error(self):
        # bpo-37228: Ensure that explicit passing of `reuse_address=True`
        # raises an error, as it is not safe to use SO_REUSEADDR when using UDP

        self._skip_create_datagram_endpoint_reuse_addr()

        coro = self.loop.create_datagram_endpoint(
            lambda: MyDatagramProto(loop=self.loop),
            local_addr=('127.0.0.1', 0),
            reuse_address=True)

        with self.assertRaises(ValueError):
            self.loop.run_until_complete(coro)

    def test_create_datagram_endpoint_reuse_address_warning(self):
        # bpo-37228: Deprecate *reuse_address* parameter

        self._skip_create_datagram_endpoint_reuse_addr()

        coro = self.loop.create_datagram_endpoint(
            lambda: MyDatagramProto(loop=self.loop),
            local_addr=('127.0.0.1', 0),
            reuse_address=False)

        with self.assertWarns(DeprecationWarning):
            tr, pr = self.loop.run_until_complete(coro)

        tr.close()
        self.loop.run_until_complete(pr.done)


class Test_UV_UDP(_TestUDP, tb.UVTestCase):

    def test_create_datagram_endpoint_wrong_sock(self):
        sock = socket.socket(socket.AF_INET)
        with sock:
            coro = self.loop.create_datagram_endpoint(lambda: None, sock=sock)
            with self.assertRaisesRegex(ValueError,
                                        'A UDP Socket was expected'):
                self.loop.run_until_complete(coro)

    def test_udp_sendto_dns(self):
        coro = self.loop.create_datagram_endpoint(
            asyncio.DatagramProtocol,
            local_addr=('127.0.0.1', 0),
            family=socket.AF_INET)

        s_transport, server = self.loop.run_until_complete(coro)

        with self.assertRaisesRegex(ValueError, 'DNS lookup'):
            s_transport.sendto(b'aaaa', ('example.com', 80))

        with self.assertRaisesRegex(ValueError, 'socket family mismatch'):
            s_transport.sendto(b'aaaa', ('::1', 80))

        s_transport.close()
        self.loop.run_until_complete(asyncio.sleep(0.01))

    def test_udp_sendto_broadcast(self):
        coro = self.loop.create_datagram_endpoint(
            asyncio.DatagramProtocol,
            local_addr=('127.0.0.1', 0),
            family=socket.AF_INET)

        s_transport, server = self.loop.run_until_complete(coro)

        try:
            s_transport.sendto(b'aaaa', ('<broadcast>', 80))
        except ValueError as exc:
            raise AssertionError('sendto raises {}.'.format(exc))

        s_transport.close()
        self.loop.run_until_complete(asyncio.sleep(0.01))

    def test_send_after_close(self):
        coro = self.loop.create_datagram_endpoint(
            asyncio.DatagramProtocol,
            local_addr=('127.0.0.1', 0),
            family=socket.AF_INET)

        s_transport, _ = self.loop.run_until_complete(coro)

        s_transport.close()
        s_transport.sendto(b'aaaa', ('127.0.0.1', 80))
        self.loop.run_until_complete(asyncio.sleep(0.01))
        s_transport.sendto(b'aaaa', ('127.0.0.1', 80))

    @unittest.skipUnless(tb.has_IPv6, 'no IPv6')
    def test_create_datagram_endpoint_addrs_ipv6(self):
        self._test_create_datagram_endpoint_addrs_ipv6()


class Test_AIO_UDP(_TestUDP, tb.AIOTestCase):
    @unittest.skipUnless(tb.has_IPv6, 'no IPv6')
    def test_create_datagram_endpoint_addrs_ipv6(self):
        self._test_create_datagram_endpoint_addrs_ipv6()
```

## File: `tests/test_unix.py`
```python
import asyncio
import os
import pathlib
import socket
import tempfile
import time
import unittest
import sys

from uvloop import _testbase as tb


SSL_HANDSHAKE_TIMEOUT = 15.0


class _TestUnix:
    def test_create_unix_server_1(self):
        CNT = 0           # number of clients that were successful
        TOTAL_CNT = 100   # total number of clients that test will create
        TIMEOUT = 5.0     # timeout for this test

        async def handle_client(reader, writer):
            nonlocal CNT

            data = await reader.readexactly(4)
            self.assertEqual(data, b'AAAA')
            writer.write(b'OK')

            data = await reader.readexactly(4)
            self.assertEqual(data, b'BBBB')
            writer.write(b'SPAM')

            await writer.drain()
            writer.close()
            await self.wait_closed(writer)

            CNT += 1

        async def test_client(addr):
            sock = socket.socket(socket.AF_UNIX)
            with sock:
                sock.setblocking(False)
                await self.loop.sock_connect(sock, addr)

                await self.loop.sock_sendall(sock, b'AAAA')

                buf = b''
                while len(buf) != 2:
                    buf += await self.loop.sock_recv(sock, 1)
                self.assertEqual(buf, b'OK')

                await self.loop.sock_sendall(sock, b'BBBB')

                buf = b''
                while len(buf) != 4:
                    buf += await self.loop.sock_recv(sock, 1)
                self.assertEqual(buf, b'SPAM')

        async def start_server():
            nonlocal CNT
            CNT = 0

            with tempfile.TemporaryDirectory() as td:
                sock_name = os.path.join(td, 'sock')
                srv = await asyncio.start_unix_server(
                    handle_client,
                    sock_name)

                try:
                    srv_socks = srv.sockets
                    self.assertTrue(srv_socks)
                    self.assertTrue(srv.is_serving())

                    tasks = []
                    for _ in range(TOTAL_CNT):
                        tasks.append(test_client(sock_name))

                    await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

                finally:
                    self.loop.call_soon(srv.close)
                    await srv.wait_closed()

                    if (
                        self.implementation == 'asyncio'
                        and sys.version_info[:3] >= (3, 12, 0)
                    ):
                        # asyncio regression in 3.12 -- wait_closed()
                        # doesn't wait for `close()` to actually complete.
                        # https://github.com/python/cpython/issues/79033
                        await asyncio.sleep(1)

                    # Check that the server cleaned-up proxy-sockets
                    for srv_sock in srv_socks:
                        self.assertEqual(srv_sock.fileno(), -1)

                    self.assertFalse(srv.is_serving())

                if sys.version_info < (3, 13):
                    # asyncio doesn't cleanup the sock file under Python 3.13
                    self.assertTrue(os.path.exists(sock_name))
                else:
                    self.assertFalse(os.path.exists(sock_name))

        async def start_server_sock(start_server, is_unix_api=True):
            # is_unix_api indicates whether `start_server` is calling
            # `loop.create_unix_server()` or `loop.create_server()`,
            # because asyncio `loop.create_server()` doesn't cleanup
            # the socket file even if it's a UNIX socket.

            nonlocal CNT
            CNT = 0

            with tempfile.TemporaryDirectory() as td:
                sock_name = os.path.join(td, 'sock')
                sock = socket.socket(socket.AF_UNIX)
                sock.bind(sock_name)

                srv = await start_server(sock)

                try:
                    srv_socks = srv.sockets
                    self.assertTrue(srv_socks)
                    self.assertTrue(srv.is_serving())

                    tasks = []
                    for _ in range(TOTAL_CNT):
                        tasks.append(test_client(sock_name))

                    await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

                finally:
                    self.loop.call_soon(srv.close)
                    await srv.wait_closed()

                    if (
                        self.implementation == 'asyncio'
                        and sys.version_info[:3] >= (3, 12, 0)
                    ):
                        # asyncio regression in 3.12 -- wait_closed()
                        # doesn't wait for `close()` to actually complete.
                        # https://github.com/python/cpython/issues/79033
                        await asyncio.sleep(1)

                    # Check that the server cleaned-up proxy-sockets
                    for srv_sock in srv_socks:
                        self.assertEqual(srv_sock.fileno(), -1)

                    self.assertFalse(srv.is_serving())

                if sys.version_info < (3, 13) or not is_unix_api:
                    # asyncio doesn't cleanup the sock file under Python 3.13
                    self.assertTrue(os.path.exists(sock_name))
                else:
                    self.assertFalse(os.path.exists(sock_name))

        with self.subTest(func='start_unix_server(host, port)'):
            self.loop.run_until_complete(start_server())
            self.assertEqual(CNT, TOTAL_CNT)

        with self.subTest(func='start_unix_server(sock)'):
            self.loop.run_until_complete(start_server_sock(
                lambda sock: asyncio.start_unix_server(
                    handle_client,
                    None,
                    sock=sock)))
            self.assertEqual(CNT, TOTAL_CNT)

        with self.subTest(func='start_server(sock)'):
            self.loop.run_until_complete(start_server_sock(
                lambda sock: asyncio.start_server(
                    handle_client,
                    None, None,
                    sock=sock), is_unix_api=False))
            self.assertEqual(CNT, TOTAL_CNT)

    def test_create_unix_server_2(self):
        with tempfile.TemporaryDirectory() as td:
            sock_name = os.path.join(td, 'sock')
            with open(sock_name, 'wt') as f:
                f.write('x')

            with self.assertRaisesRegex(
                    OSError, "Address '{}' is already in use".format(
                        sock_name)):

                self.loop.run_until_complete(
                    self.loop.create_unix_server(object, sock_name))

    def test_create_unix_server_3(self):
        with self.assertRaisesRegex(
                ValueError, 'ssl_handshake_timeout is only meaningful'):
            self.loop.run_until_complete(
                self.loop.create_unix_server(
                    lambda: None, path='/tmp/a',
                    ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT))

    def test_create_unix_server_existing_path_sock(self):
        with self.unix_sock_name() as path:
            sock = socket.socket(socket.AF_UNIX)
            with sock:
                sock.bind(path)
                sock.listen(1)

            # Check that no error is raised -- `path` is removed.
            coro = self.loop.create_unix_server(lambda: None, path)
            srv = self.loop.run_until_complete(coro)
            srv.close()
            self.loop.run_until_complete(srv.wait_closed())

    def test_create_unix_connection_open_unix_con_addr(self):
        async def client(addr):
            reader, writer = await asyncio.open_unix_connection(addr)

            writer.write(b'AAAA')
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(b'BBBB')
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            writer.close()
            await self.wait_closed(writer)

        self._test_create_unix_connection_1(client)

    def test_create_unix_connection_open_unix_con_sock(self):
        async def client(addr):
            sock = socket.socket(socket.AF_UNIX)
            sock.connect(addr)
            reader, writer = await asyncio.open_unix_connection(sock=sock)

            writer.write(b'AAAA')
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(b'BBBB')
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            writer.close()
            await self.wait_closed(writer)

        self._test_create_unix_connection_1(client)

    def test_create_unix_connection_open_con_sock(self):
        async def client(addr):
            sock = socket.socket(socket.AF_UNIX)
            sock.connect(addr)
            reader, writer = await asyncio.open_connection(sock=sock)

            writer.write(b'AAAA')
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(b'BBBB')
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            writer.close()
            await self.wait_closed(writer)

        self._test_create_unix_connection_1(client)

    def _test_create_unix_connection_1(self, client):
        CNT = 0
        TOTAL_CNT = 100

        def server(sock):
            data = sock.recv_all(4)
            self.assertEqual(data, b'AAAA')
            sock.send(b'OK')

            data = sock.recv_all(4)
            self.assertEqual(data, b'BBBB')
            sock.send(b'SPAM')

        async def client_wrapper(addr):
            await client(addr)
            nonlocal CNT
            CNT += 1

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.unix_server(server,
                                  max_clients=TOTAL_CNT,
                                  backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(asyncio.gather(*tasks))

                # Give time for all transports to close.
                self.loop.run_until_complete(asyncio.sleep(0.1))

            self.assertEqual(CNT, TOTAL_CNT)

        run(client_wrapper)

    def test_create_unix_connection_2(self):
        with tempfile.NamedTemporaryFile() as tmp:
            path = tmp.name

        async def client():
            reader, writer = await asyncio.open_unix_connection(path)
            writer.close()
            await self.wait_closed(writer)

        async def runner():
            with self.assertRaises(FileNotFoundError):
                await client()

        self.loop.run_until_complete(runner())

    def test_create_unix_connection_3(self):
        CNT = 0
        TOTAL_CNT = 100

        def server(sock):
            data = sock.recv_all(4)
            self.assertEqual(data, b'AAAA')
            sock.close()

        async def client(addr):
            reader, writer = await asyncio.open_unix_connection(addr)

            sock = writer._transport.get_extra_info('socket')
            self.assertEqual(sock.family, socket.AF_UNIX)

            writer.write(b'AAAA')

            with self.assertRaises(asyncio.IncompleteReadError):
                await reader.readexactly(10)

            writer.close()
            await self.wait_closed(writer)

            nonlocal CNT
            CNT += 1

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.unix_server(server,
                                  max_clients=TOTAL_CNT,
                                  backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(asyncio.gather(*tasks))

            self.assertEqual(CNT, TOTAL_CNT)

        run(client)

    def test_create_unix_connection_4(self):
        sock = socket.socket(socket.AF_UNIX)
        sock.close()

        async def client():
            reader, writer = await asyncio.open_unix_connection(sock=sock)
            writer.close()
            await self.wait_closed(writer)

        async def runner():
            with self.assertRaisesRegex(OSError, 'Bad file'):
                await client()

        self.loop.run_until_complete(runner())

    def test_create_unix_connection_5(self):
        s1, s2 = socket.socketpair(socket.AF_UNIX)

        excs = []

        class Proto(asyncio.Protocol):
            def connection_lost(self, exc):
                excs.append(exc)

        proto = Proto()

        async def client():
            t, _ = await self.loop.create_unix_connection(
                lambda: proto,
                None,
                sock=s2)

            t.write(b'AAAAA')
            s1.close()
            t.write(b'AAAAA')
            await asyncio.sleep(0.1)

        self.loop.run_until_complete(client())

        self.assertEqual(len(excs), 1)
        self.assertIn(excs[0].__class__,
                      (BrokenPipeError, ConnectionResetError))

    def test_create_unix_connection_6(self):
        with self.assertRaisesRegex(
                ValueError, 'ssl_handshake_timeout is only meaningful'):
            self.loop.run_until_complete(
                self.loop.create_unix_connection(
                    lambda: None, path='/tmp/a',
                    ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT))


class Test_UV_Unix(_TestUnix, tb.UVTestCase):

    @unittest.skipUnless(hasattr(os, 'fspath'), 'no os.fspath()')
    def test_create_unix_connection_pathlib(self):
        async def run(addr):
            t, _ = await self.loop.create_unix_connection(
                asyncio.Protocol, addr)
            t.close()

        with self.unix_server(lambda sock: time.sleep(0.01)) as srv:
            addr = pathlib.Path(srv.addr)
            self.loop.run_until_complete(run(addr))

    @unittest.skipUnless(hasattr(os, 'fspath'), 'no os.fspath()')
    def test_create_unix_server_pathlib(self):
        with self.unix_sock_name() as srv_path:
            srv_path = pathlib.Path(srv_path)
            srv = self.loop.run_until_complete(
                self.loop.create_unix_server(asyncio.Protocol, srv_path))
            srv.close()
            self.loop.run_until_complete(srv.wait_closed())

    def test_transport_fromsock_get_extra_info(self):
        # This tests is only for uvloop.  asyncio should pass it
        # too in Python 3.6.

        async def test(sock):
            t, _ = await self.loop.create_unix_connection(
                asyncio.Protocol,
                sock=sock)

            sock = t.get_extra_info('socket')
            self.assertIs(t.get_extra_info('socket'), sock)

            with self.assertRaisesRegex(RuntimeError, 'is used by transport'):
                self.loop.add_writer(sock.fileno(), lambda: None)
            with self.assertRaisesRegex(RuntimeError, 'is used by transport'):
                self.loop.remove_writer(sock.fileno())

            t.close()

        s1, s2 = socket.socketpair(socket.AF_UNIX)
        with s1, s2:
            self.loop.run_until_complete(test(s1))

    def test_create_unix_server_path_dgram(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        with sock:
            coro = self.loop.create_unix_server(lambda: None,
                                                sock=sock)
            with self.assertRaisesRegex(ValueError,
                                        'A UNIX Domain Stream.*was expected'):
                self.loop.run_until_complete(coro)

    @unittest.skipUnless(hasattr(socket, 'SOCK_NONBLOCK'),
                         'no socket.SOCK_NONBLOCK (linux only)')
    def test_create_unix_server_path_stream_bittype(self):
        sock = socket.socket(
            socket.AF_UNIX, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
        with tempfile.NamedTemporaryFile() as file:
            fn = file.name
        with sock:
            sock.bind(fn)
            coro = self.loop.create_unix_server(lambda: None, path=None,
                                                sock=sock, cleanup_socket=True)
            srv = self.loop.run_until_complete(coro)
            srv.close()
            self.loop.run_until_complete(srv.wait_closed())

    @unittest.skipUnless(sys.platform.startswith('linux'), 'requires epoll')
    def test_epollhup(self):
        SIZE = 50
        eof = False
        done = False
        recvd = b''

        class Proto(asyncio.BaseProtocol):
            def connection_made(self, tr):
                tr.write(b'hello')
                self.data = bytearray(SIZE)
                self.buf = memoryview(self.data)

            def get_buffer(self, sizehint):
                return self.buf

            def buffer_updated(self, nbytes):
                nonlocal recvd
                recvd += self.buf[:nbytes]

            def eof_received(self):
                nonlocal eof
                eof = True

            def connection_lost(self, exc):
                nonlocal done
                done = exc

        async def test():
            with tempfile.TemporaryDirectory() as td:
                sock_name = os.path.join(td, 'sock')
                srv = await self.loop.create_unix_server(Proto, sock_name)

                s = socket.socket(socket.AF_UNIX)
                with s:
                    s.setblocking(False)
                    await self.loop.sock_connect(s, sock_name)
                    d = await self.loop.sock_recv(s, 100)
                    self.assertEqual(d, b'hello')

                    # IMPORTANT: overflow recv buffer and close immediately
                    await self.loop.sock_sendall(s, b'a' * (SIZE + 1))

                srv.close()
                await srv.wait_closed()

        self.loop.run_until_complete(test())
        self.assertTrue(eof)
        self.assertIsNone(done)
        self.assertEqual(recvd, b'a' * (SIZE + 1))


class Test_AIO_Unix(_TestUnix, tb.AIOTestCase):
    pass


class _TestSSL(tb.SSLTestCase):

    ONLYCERT = tb._cert_fullname(__file__, 'ssl_cert.pem')
    ONLYKEY = tb._cert_fullname(__file__, 'ssl_key.pem')

    def test_create_unix_server_ssl_1(self):
        CNT = 0           # number of clients that were successful
        TOTAL_CNT = 25    # total number of clients that test will create
        TIMEOUT = 10.0    # timeout for this test

        A_DATA = b'A' * 1024 * 1024
        B_DATA = b'B' * 1024 * 1024

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()

        clients = []

        async def handle_client(reader, writer):
            nonlocal CNT

            data = await reader.readexactly(len(A_DATA))
            self.assertEqual(data, A_DATA)
            writer.write(b'OK')

            data = await reader.readexactly(len(B_DATA))
            self.assertEqual(data, B_DATA)
            writer.writelines([b'SP', bytearray(b'A'), memoryview(b'M')])

            await writer.drain()
            writer.close()

            CNT += 1

        async def test_client(addr):
            fut = asyncio.Future(loop=self.loop)

            def prog(sock):
                try:
                    sock.starttls(client_sslctx)

                    sock.connect(addr)
                    sock.send(A_DATA)

                    data = sock.recv_all(2)
                    self.assertEqual(data, b'OK')

                    sock.send(B_DATA)
                    data = sock.recv_all(4)
                    self.assertEqual(data, b'SPAM')

                    sock.close()

                except Exception as ex:
                    self.loop.call_soon_threadsafe(
                        lambda ex=ex:
                            (fut.cancelled() or fut.set_exception(ex)))
                else:
                    self.loop.call_soon_threadsafe(
                        lambda: (fut.cancelled() or fut.set_result(None)))

            client = self.unix_client(prog)
            client.start()
            clients.append(client)

            await fut

        async def start_server():
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

            with tempfile.TemporaryDirectory() as td:
                sock_name = os.path.join(td, 'sock')

                srv = await asyncio.start_unix_server(
                    handle_client,
                    sock_name,
                    ssl=sslctx,
                    **extras)

                try:
                    tasks = []
                    for _ in range(TOTAL_CNT):
                        tasks.append(test_client(sock_name))

                    await asyncio.wait_for(asyncio.gather(*tasks), TIMEOUT)

                finally:
                    self.loop.call_soon(srv.close)
                    await srv.wait_closed()

        try:
            with self._silence_eof_received_warning():
                self.loop.run_until_complete(start_server())
        except asyncio.TimeoutError:
            if os.environ.get('TRAVIS_OS_NAME') == 'osx':
                # XXX: figure out why this fails on macOS on Travis
                raise unittest.SkipTest('unexplained error on Travis macOS')
            else:
                raise

        self.assertEqual(CNT, TOTAL_CNT)

        for client in clients:
            client.stop()

    def test_create_unix_connection_ssl_1(self):
        CNT = 0
        TOTAL_CNT = 25

        A_DATA = b'A' * 1024 * 1024
        B_DATA = b'B' * 1024 * 1024

        sslctx = self._create_server_ssl_context(self.ONLYCERT, self.ONLYKEY)
        client_sslctx = self._create_client_ssl_context()

        def server(sock):
            sock.starttls(sslctx, server_side=True)

            data = sock.recv_all(len(A_DATA))
            self.assertEqual(data, A_DATA)
            sock.send(b'OK')

            data = sock.recv_all(len(B_DATA))
            self.assertEqual(data, B_DATA)
            sock.send(b'SPAM')

            sock.close()

        async def client(addr):
            extras = dict(ssl_handshake_timeout=SSL_HANDSHAKE_TIMEOUT)

            reader, writer = await asyncio.open_unix_connection(
                addr,
                ssl=client_sslctx,
                server_hostname='',
                **extras)

            writer.write(A_DATA)
            self.assertEqual(await reader.readexactly(2), b'OK')

            writer.write(B_DATA)
            self.assertEqual(await reader.readexactly(4), b'SPAM')

            nonlocal CNT
            CNT += 1

            writer.close()
            await self.wait_closed(writer)

        def run(coro):
            nonlocal CNT
            CNT = 0

            with self.unix_server(server,
                                  max_clients=TOTAL_CNT,
                                  backlog=TOTAL_CNT) as srv:
                tasks = []
                for _ in range(TOTAL_CNT):
                    tasks.append(coro(srv.addr))

                self.loop.run_until_complete(asyncio.gather(*tasks))

            self.assertEqual(CNT, TOTAL_CNT)

        with self._silence_eof_received_warning():
            run(client)


class Test_UV_UnixSSL(_TestSSL, tb.UVTestCase):
    pass


class Test_AIO_UnixSSL(_TestSSL, tb.AIOTestCase):
    pass
```

## File: `tests/certs/ssl_cert.pem`
```
-----BEGIN CERTIFICATE-----
MIIF8TCCBFmgAwIBAgIJAMstgJlaaVJcMA0GCSqGSIb3DQEBCwUAME0xCzAJBgNV
BAYTAlhZMSYwJAYDVQQKDB1QeXRob24gU29mdHdhcmUgRm91bmRhdGlvbiBDQTEW
MBQGA1UEAwwNb3VyLWNhLXNlcnZlcjAeFw0xODA4MjkxNDIzMTZaFw0yODA3MDcx
NDIzMTZaMF8xCzAJBgNVBAYTAlhZMRcwFQYDVQQHDA5DYXN0bGUgQW50aHJheDEj
MCEGA1UECgwaUHl0aG9uIFNvZnR3YXJlIEZvdW5kYXRpb24xEjAQBgNVBAMMCWxv
Y2FsaG9zdDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBAJ8oLzdB739k
YxZiFukBFGIpyjqYkj0I015p/sDz1MT7DljcZLBLy7OqnkLpB5tnM8256DwdihPA
3zlnfEzTfr9DD0qFBW2H5cMCoz7X17koeRhzGDd3dkjUeBjXvR5qRosG8wM3lQug
U7AizY+3Azaj1yN3mZ9K5a20jr58Kqinz+Xxx6sb2JfYYff2neJbBahNm5id0AD2
pi/TthZqO5DURJYo+MdgZOcy+7jEjOJsLWZd3Yzq78iM07qDjbpIoVpENZCTHTWA
hX8LIqz0OBmh4weQpm4+plU7E4r4D82uauocWw8iyuznCTtABWO7n9fWySmf9QZC
WYxHAFpBQs6zUVqAD7nhFdTqpQ9bRiaEnjE4HiAccPW+MAoSxFnv/rNzEzI6b4zU
NspFMfg1aNVamdjxdpUZ1GG1Okf0yPJykqEX4PZl3La1Be2q7YZ1wydR523Xd+f3
EO4/g+imETSKn8gyCf6Rvib175L4r2WV1CXQH7gFwZYCod6WHYq5TQIDAQABo4IB
wDCCAbwwFAYDVR0RBA0wC4IJbG9jYWxob3N0MA4GA1UdDwEB/wQEAwIFoDAdBgNV
HSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIwADAdBgNVHQ4E
FgQUj+od4zNcABazi29rb9NMy7XLfFUwfQYDVR0jBHYwdIAU3b/K2ubRNLo3dSHK
b5oIKPI1tkihUaRPME0xCzAJBgNVBAYTAlhZMSYwJAYDVQQKDB1QeXRob24gU29m
dHdhcmUgRm91bmRhdGlvbiBDQTEWMBQGA1UEAwwNb3VyLWNhLXNlcnZlcoIJAMst
gJlaaVJbMIGDBggrBgEFBQcBAQR3MHUwPAYIKwYBBQUHMAKGMGh0dHA6Ly90ZXN0
Y2EucHl0aG9udGVzdC5uZXQvdGVzdGNhL3B5Y2FjZXJ0LmNlcjA1BggrBgEFBQcw
AYYpaHR0cDovL3Rlc3RjYS5weXRob250ZXN0Lm5ldC90ZXN0Y2Evb2NzcC8wQwYD
VR0fBDwwOjA4oDagNIYyaHR0cDovL3Rlc3RjYS5weXRob250ZXN0Lm5ldC90ZXN0
Y2EvcmV2b2NhdGlvbi5jcmwwDQYJKoZIhvcNAQELBQADggGBACf1jFkQ9MbnKAC/
uo17EwPxHKZfswZVpCK527LVRr33DN1DbrR5ZWchDCpV7kCOhZ+fR7sKKk22ZHSY
oH+u3PEu20J3GOB1iyY1aMNB7WvId3JvappdVWkC/VpUyFfLsGUDFuIPADmZZqCb
iJMX4loteTVfl1d4xK/1mV6Gq9MRrRqiDfpSELn+v53OM9mGspwW+NZ1CIrbCuW0
KxZ/tPkqn8PSd9fNZR70bB7rWbnwrl+kH8xKxLl6qdlrMmg74WWwhLeQxK7+9DdP
IaDenzqx5cwWBGY/C0HcQj0gPuy3lSs1V/q+f7Y6uspPWP51PgiJLIywXS75iRAr
+UFGTzwAtyfTZSQoFyMmMULqfk6T5HtoVMqfRvPvK+mFDLWEstU1NIB1K/CRI7gI
AY65ClTU+zRS/tlF8IA7tsFvgtEf8jsI9kamlidhS1gyeg4dWcVErV4aeTPB1AUv
StPYQkKNM+NjytWHl5tNuBoDNLsc0gI/WSPiI4CIY8LwomOoiw==
-----END CERTIFICATE-----
```

## File: `tests/certs/ssl_key.pem`
```
-----BEGIN PRIVATE KEY-----
MIIG/QIBADANBgkqhkiG9w0BAQEFAASCBucwggbjAgEAAoIBgQCfKC83Qe9/ZGMW
YhbpARRiKco6mJI9CNNeaf7A89TE+w5Y3GSwS8uzqp5C6QebZzPNueg8HYoTwN85
Z3xM036/Qw9KhQVth+XDAqM+19e5KHkYcxg3d3ZI1HgY170eakaLBvMDN5ULoFOw
Is2PtwM2o9cjd5mfSuWttI6+fCqop8/l8cerG9iX2GH39p3iWwWoTZuYndAA9qYv
07YWajuQ1ESWKPjHYGTnMvu4xIzibC1mXd2M6u/IjNO6g426SKFaRDWQkx01gIV/
CyKs9DgZoeMHkKZuPqZVOxOK+A/NrmrqHFsPIsrs5wk7QAVju5/X1skpn/UGQlmM
RwBaQULOs1FagA+54RXU6qUPW0YmhJ4xOB4gHHD1vjAKEsRZ7/6zcxMyOm+M1DbK
RTH4NWjVWpnY8XaVGdRhtTpH9MjycpKhF+D2Zdy2tQXtqu2GdcMnUedt13fn9xDu
P4PophE0ip/IMgn+kb4m9e+S+K9lldQl0B+4BcGWAqHelh2KuU0CAwEAAQKCAYEA
lKiWIYjmyRjdLKUGPTES9vWNvNmRjozV0RQ0LcoSbMMLDZkeO0UwyWqOVHUQ8+ib
jIcfEjeNJxI57oZopeHOO5vJhpNlFH+g7ltiW2qERqA1K88lSXm99Bzw6FNqhCRE
K8ub5N9fyfJA+P4o/xm0WK8EXk5yIUV17p/9zJJxzgKgv2jsVTi3QG2OZGvn4Oug
ByomMZEGHkBDzdxz8c/cP1Tlk1RFuwSgews178k2xq7AYSM/s0YmHi7b/RSvptX6
1v8P8kXNUe4AwTaNyrlvF2lwIadZ8h1hA7tCE2n44b7a7KfhAkwcbr1T59ioYh6P
zxsyPT678uD51dbtD/DXJCcoeeFOb8uzkR2KNcrnQzZpCJnRq4Gp5ybxwsxxuzpr
gz0gbNlhuWtE7EoSzmIK9t+WTS7IM2CvZymd6/OAh1Fuw6AQhSp64XRp3OfMMAAC
Ie2EPtKj4islWGT8VoUjuRYGmdRh4duAH1dkiAXOWA3R7y5a1/y/iE8KE8BtxocB
AoHBAM8aiURgpu1Fs0Oqz6izec7KSLL3l8hmW+MKUOfk/Ybng6FrTFsL5YtzR+Ap
wW4wwWnnIKEc1JLiZ7g8agRETK8hr5PwFXUn/GSWC0SMsazLJToySQS5LOV0tLzK
kJ3jtNU7tnlDGNkCHTHSoVL2T/8t+IkZI/h5Z6wjlYPvU2Iu0nVIXtiG+alv4A6M
Hrh9l5or4mjB6rGnVXeYohLkCm6s/W97ahVxLMcEdbsBo1prm2JqGnSoiR/tEFC/
QHQnbQKBwQDEu7kW0Yg9sZ89QtYtVQ1YpixFZORaUeRIRLnpEs1w7L1mCbOZ2Lj9
JHxsH05cYAc7HJfPwwxv3+3aGAIC/dfu4VSwEFtatAzUpzlhzKS5+HQCWB4JUNNU
MQ3+FwK2xQX4Ph8t+OzrFiYcK2g0An5UxWMa2HWIAWUOhnTOydAVsoH6yP31cVm4
0hxoABCwflaNLNGjRUyfBpLTAcNu/YtcE+KREy7YAAgXXrhRSO4XpLsSXwLnLT7/
YOkoBWDcTWECgcBPWnSUDZCIQ3efithMZJBciqd2Y2X19Dpq8O31HImD4jtOY0V7
cUB/wSkeHAGwjd/eCyA2e0x8B2IEdqmMfvr+86JJxekC3dJYXCFvH5WIhsH53YCa
3bT1KlWCLP9ib/g+58VQC0R/Cc9T4sfLePNH7D5ZkZd1wlbV30CPr+i8KwKay6MD
xhvtLx+jk07GE+E9wmjbCMo7TclyrLoVEOlqZMAqshgApT+p9eyCPetwXuDHwa3n
WxhHclcZCV7R4rUCgcAkdGSnxcvpIrDPOUNWwxvmAWTStw9ZbTNP8OxCNCm9cyDl
d4bAS1h8D/a+Uk7C70hnu7Sl2w7C7Eu2zhwRUdhhe3+l4GINPK/j99i6NqGPlGpq
xMlMEJ4YS768BqeKFpg0l85PRoEgTsphDeoROSUPsEPdBZ9BxIBlYKTkbKESZDGR
twzYHljx1n1NCDYPflmrb1KpXn4EOcObNghw2KqqNUUWfOeBPwBA1FxzM4BrAStp
DBINpGS4Dc0mjViVegECgcA3hTtm82XdxQXj9LQmb/E3lKx/7H87XIOeNMmvjYuZ
iS9wKrkF+u42vyoDxcKMCnxP5056wpdST4p56r+SBwVTHcc3lGBSGcMTIfwRXrj3
thOA2our2n4ouNIsYyTlcsQSzifwmpRmVMRPxl9fYVdEWUgB83FgHT0D9avvZnF9
t9OccnGJXShAIZIBADhVj/JwG4FbaX42NijD5PNpVLk1Y17OV0I576T9SfaQoBjJ
aH1M/zC4aVaS0DYB/Gxq7v8=
-----END PRIVATE KEY-----
```

## File: `uvloop/.gitignore`
```
*.c
*.html
```

## File: `uvloop/__init__.py`
```python
import asyncio as __asyncio
import typing as _typing
import sys as _sys
import warnings as _warnings

from . import includes as __includes  # NOQA
from .loop import Loop as __BaseLoop  # NOQA
from ._version import __version__  # NOQA


__all__: _typing.Tuple[str, ...] = ('new_event_loop', 'run')
_AbstractEventLoop = __asyncio.AbstractEventLoop


_T = _typing.TypeVar("_T")


class Loop(__BaseLoop, _AbstractEventLoop):  # type: ignore[misc]
    pass


def new_event_loop() -> Loop:
    """Return a new event loop."""
    return Loop()


if _typing.TYPE_CHECKING:
    def run(
        main: _typing.Coroutine[_typing.Any, _typing.Any, _T],
        *,
        loop_factory: _typing.Optional[
            _typing.Callable[[], Loop]
        ] = new_event_loop,
        debug: _typing.Optional[bool]=None,
    ) -> _T:
        """The preferred way of running a coroutine with uvloop."""
else:
    def run(main, *, loop_factory=new_event_loop, debug=None, **run_kwargs):
        """The preferred way of running a coroutine with uvloop."""

        async def wrapper():
            # If `loop_factory` is provided we want it to return
            # either uvloop.Loop or a subtype of it, assuming the user
            # is using `uvloop.run()` intentionally.
            loop = __asyncio._get_running_loop()
            if not isinstance(loop, Loop):
                raise TypeError('uvloop.run() uses a non-uvloop event loop')
            return await main

        vi = _sys.version_info[:2]

        if vi <= (3, 10):
            # Copied from python/cpython

            if __asyncio._get_running_loop() is not None:
                raise RuntimeError(
                    "asyncio.run() cannot be called from a running event loop")

            if not __asyncio.iscoroutine(main):
                raise ValueError(
                    "a coroutine was expected, got {!r}".format(main)
                )

            loop = loop_factory()
            try:
                __asyncio.set_event_loop(loop)
                if debug is not None:
                    loop.set_debug(debug)
                return loop.run_until_complete(wrapper())
            finally:
                try:
                    _cancel_all_tasks(loop)
                    loop.run_until_complete(loop.shutdown_asyncgens())
                    if hasattr(loop, 'shutdown_default_executor'):
                        loop.run_until_complete(
                            loop.shutdown_default_executor()
                        )
                finally:
                    __asyncio.set_event_loop(None)
                    loop.close()

        elif vi == (3, 11):
            if __asyncio._get_running_loop() is not None:
                raise RuntimeError(
                    "asyncio.run() cannot be called from a running event loop")

            with __asyncio.Runner(
                loop_factory=loop_factory,
                debug=debug,
                **run_kwargs
            ) as runner:
                return runner.run(wrapper())

        else:
            assert vi >= (3, 12)
            return __asyncio.run(
                wrapper(),
                loop_factory=loop_factory,
                debug=debug,
                **run_kwargs
            )


def _cancel_all_tasks(loop: _AbstractEventLoop) -> None:
    # Copied from python/cpython

    to_cancel = __asyncio.all_tasks(loop)
    if not to_cancel:
        return

    for task in to_cancel:
        task.cancel()

    loop.run_until_complete(
        __asyncio.gather(*to_cancel, return_exceptions=True)
    )

    for task in to_cancel:
        if task.cancelled():
            continue
        if task.exception() is not None:
            loop.call_exception_handler({
                'message': 'unhandled exception during asyncio.run() shutdown',
                'exception': task.exception(),
                'task': task,
            })


_deprecated_names = ('install', 'EventLoopPolicy')


if _sys.version_info[:2] < (3, 16):
    __all__ += _deprecated_names


def __getattr__(name: str) -> _typing.Any:
    if name not in _deprecated_names:
        raise AttributeError(f"module 'uvloop' has no attribute '{name}'")
    elif _sys.version_info[:2] >= (3, 16):
        raise AttributeError(
            f"module 'uvloop' has no attribute '{name}' "
            f"(it was removed in Python 3.16, use uvloop.run() instead)"
        )

    import threading

    def install() -> None:
        """A helper function to install uvloop policy.

        This function is deprecated and will be removed in Python 3.16.
        Use `uvloop.run()` instead.
        """
        if _sys.version_info[:2] >= (3, 12):
            _warnings.warn(
                'uvloop.install() is deprecated in favor of uvloop.run() '
                'starting with Python 3.12.',
                DeprecationWarning,
                stacklevel=1,
            )
        __asyncio.set_event_loop_policy(EventLoopPolicy())

    class EventLoopPolicy(
        # This is to avoid a mypy error about AbstractEventLoopPolicy
        getattr(__asyncio, 'AbstractEventLoopPolicy')  # type: ignore[misc]
    ):
        """Event loop policy for uvloop.

        This class is deprecated and will be removed in Python 3.16.
        Use `uvloop.run()` instead.

        >>> import asyncio
        >>> import uvloop
        >>> asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        >>> asyncio.get_event_loop()
        <uvloop.Loop running=False closed=False debug=False>
        """

        def _loop_factory(self) -> Loop:
            return new_event_loop()

        if _typing.TYPE_CHECKING:
            # EventLoopPolicy doesn't implement these, but since they are
            # marked as abstract in typeshed, we have to put them in so mypy
            # thinks the base methods are overridden. This is the same approach
            # taken for the Windows event loop policy classes in typeshed.
            def get_child_watcher(self) -> _typing.NoReturn:
                ...

            def set_child_watcher(
                self, watcher: _typing.Any
            ) -> _typing.NoReturn:
                ...

        class _Local(threading.local):
            _loop: _typing.Optional[_AbstractEventLoop] = None

        def __init__(self) -> None:
            self._local = self._Local()

        def get_event_loop(self) -> _AbstractEventLoop:
            """Get the event loop for the current context.

            Returns an instance of EventLoop or raises an exception.
            """
            if self._local._loop is None:
                raise RuntimeError(
                    'There is no current event loop in thread %r.'
                    % threading.current_thread().name
                )

            return self._local._loop

        def set_event_loop(
            self, loop: _typing.Optional[_AbstractEventLoop]
        ) -> None:
            """Set the event loop."""
            if loop is not None and not isinstance(loop, _AbstractEventLoop):
                raise TypeError(
                    f"loop must be an instance of AbstractEventLoop or None, "
                    f"not '{type(loop).__name__}'"
                )
            self._local._loop = loop

        def new_event_loop(self) -> Loop:
            """Create a new event loop.

            You must call set_event_loop() to make this the current event loop.
            """
            return self._loop_factory()

    globals()['install'] = install
    globals()['EventLoopPolicy'] = EventLoopPolicy
    return globals()[name]
```

## File: `uvloop/_noop.py`
```python
def noop() -> None:
    """Empty function to invoke CPython ceval loop."""
    return
```

## File: `uvloop/_testbase.py`
```python
"""Test utilities. Don't use outside of the uvloop project."""


import asyncio
import asyncio.events
import collections
import contextlib
import gc
import logging
import os
import pprint
import re
import select
import socket
import ssl
import sys
import tempfile
import threading
import time
import unittest
import uvloop


class MockPattern(str):
    def __eq__(self, other):
        return bool(re.search(str(self), other, re.S))


class TestCaseDict(collections.UserDict):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __setitem__(self, key, value):
        if key in self.data:
            raise RuntimeError('duplicate test {}.{}'.format(
                self.name, key))
        super().__setitem__(key, value)


class BaseTestCaseMeta(type):

    @classmethod
    def __prepare__(mcls, name, bases):
        return TestCaseDict(name)

    def __new__(mcls, name, bases, dct):
        for test_name in dct:
            if not test_name.startswith('test_'):
                continue
            for base in bases:
                if hasattr(base, test_name):
                    raise RuntimeError(
                        'duplicate test {}.{} (also defined in {} '
                        'parent class)'.format(
                            name, test_name, base.__name__))

        return super().__new__(mcls, name, bases, dict(dct))


class BaseTestCase(unittest.TestCase, metaclass=BaseTestCaseMeta):

    def new_loop(self):
        raise NotImplementedError

    def new_policy(self):
        raise NotImplementedError

    def mock_pattern(self, str):
        return MockPattern(str)

    async def wait_closed(self, obj):
        if not isinstance(obj, asyncio.StreamWriter):
            return
        try:
            await obj.wait_closed()
        except (BrokenPipeError, ConnectionError):
            pass

    def is_asyncio_loop(self):
        return type(self.loop).__module__.startswith('asyncio.')

    def run_loop_briefly(self, *, delay=0.01):
        self.loop.run_until_complete(asyncio.sleep(delay))

    def loop_exception_handler(self, loop, context):
        self.__unhandled_exceptions.append(context)
        self.loop.default_exception_handler(context)

    def setUp(self):
        self.loop = self.new_loop()
        asyncio.set_event_loop_policy(self.new_policy())
        asyncio.set_event_loop(self.loop)
        self._check_unclosed_resources_in_debug = True

        self.loop.set_exception_handler(self.loop_exception_handler)
        self.__unhandled_exceptions = []

    def tearDown(self):
        self.loop.close()

        if self.__unhandled_exceptions:
            print('Unexpected calls to loop.call_exception_handler():')
            pprint.pprint(self.__unhandled_exceptions)
            self.fail('unexpected calls to loop.call_exception_handler()')
            return

        if not self._check_unclosed_resources_in_debug:
            return

        # GC to show any resource warnings as the test completes
        gc.collect()
        gc.collect()
        gc.collect()

        if getattr(self.loop, '_debug_cc', False):
            gc.collect()
            gc.collect()
            gc.collect()

            self.assertEqual(
                self.loop._debug_uv_handles_total,
                self.loop._debug_uv_handles_freed,
                'not all uv_handle_t handles were freed')

            self.assertEqual(
                self.loop._debug_cb_handles_count, 0,
                'not all callbacks (call_soon) are GCed')

            self.assertEqual(
                self.loop._debug_cb_timer_handles_count, 0,
                'not all timer callbacks (call_later) are GCed')

            self.assertEqual(
                self.loop._debug_stream_write_ctx_cnt, 0,
                'not all stream write contexts are GCed')

            for h_name, h_cnt in self.loop._debug_handles_current.items():
                with self.subTest('Alive handle after test',
                                  handle_name=h_name):
                    self.assertEqual(
                        h_cnt, 0,
                        'alive {} after test'.format(h_name))

            for h_name, h_cnt in self.loop._debug_handles_total.items():
                with self.subTest('Total/closed handles',
                                  handle_name=h_name):
                    self.assertEqual(
                        h_cnt, self.loop._debug_handles_closed[h_name],
                        'total != closed for {}'.format(h_name))

        asyncio.set_event_loop(None)
        asyncio.set_event_loop_policy(None)
        self.loop = None

    def skip_unclosed_handles_check(self):
        self._check_unclosed_resources_in_debug = False

    def tcp_server(self, server_prog, *,
                   family=socket.AF_INET,
                   addr=None,
                   timeout=5,
                   backlog=1,
                   max_clients=10):

        if addr is None:
            if family == socket.AF_UNIX:
                with tempfile.NamedTemporaryFile() as tmp:
                    addr = tmp.name
            else:
                addr = ('127.0.0.1', 0)

        sock = socket.socket(family, socket.SOCK_STREAM)

        if timeout is None:
            raise RuntimeError('timeout is required')
        if timeout <= 0:
            raise RuntimeError('only blocking sockets are supported')
        sock.settimeout(timeout)

        try:
            sock.bind(addr)
            sock.listen(backlog)
        except OSError as ex:
            sock.close()
            raise ex

        return TestThreadedServer(
            self, sock, server_prog, timeout, max_clients)

    def tcp_client(self, client_prog,
                   family=socket.AF_INET,
                   timeout=10):

        sock = socket.socket(family, socket.SOCK_STREAM)

        if timeout is None:
            raise RuntimeError('timeout is required')
        if timeout <= 0:
            raise RuntimeError('only blocking sockets are supported')
        sock.settimeout(timeout)

        return TestThreadedClient(
            self, sock, client_prog, timeout)

    def unix_server(self, *args, **kwargs):
        return self.tcp_server(*args, family=socket.AF_UNIX, **kwargs)

    def unix_client(self, *args, **kwargs):
        return self.tcp_client(*args, family=socket.AF_UNIX, **kwargs)

    @contextlib.contextmanager
    def unix_sock_name(self):
        with tempfile.TemporaryDirectory() as td:
            fn = os.path.join(td, 'sock')
            try:
                yield fn
            finally:
                try:
                    os.unlink(fn)
                except OSError:
                    pass

    def _abort_socket_test(self, ex):
        try:
            self.loop.stop()
        finally:
            self.fail(ex)


def _cert_fullname(test_file_name, cert_file_name):
    fullname = os.path.abspath(os.path.join(
        os.path.dirname(test_file_name), 'certs', cert_file_name))
    assert os.path.isfile(fullname)
    return fullname


@contextlib.contextmanager
def silence_long_exec_warning():

    class Filter(logging.Filter):
        def filter(self, record):
            return not (record.msg.startswith('Executing') and
                        record.msg.endswith('seconds'))

    logger = logging.getLogger('asyncio')
    filter = Filter()
    logger.addFilter(filter)
    try:
        yield
    finally:
        logger.removeFilter(filter)


def find_free_port(start_from=50000):
    for port in range(start_from, start_from + 500):
        sock = socket.socket()
        with sock:
            try:
                sock.bind(('', port))
            except socket.error:
                continue
            else:
                return port
    raise RuntimeError('could not find a free port')


class SSLTestCase:

    def _create_server_ssl_context(self, certfile, keyfile=None):
        if hasattr(ssl, 'PROTOCOL_TLS_SERVER'):
            sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        elif hasattr(ssl, 'PROTOCOL_TLS'):
            sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS)
        else:
            sslcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        sslcontext.options |= ssl.OP_NO_SSLv2
        sslcontext.load_cert_chain(certfile, keyfile)
        return sslcontext

    def _create_client_ssl_context(self, *, disable_verify=True):
        sslcontext = ssl.create_default_context()
        sslcontext.check_hostname = False
        if disable_verify:
            sslcontext.verify_mode = ssl.CERT_NONE
        return sslcontext

    @contextlib.contextmanager
    def _silence_eof_received_warning(self):
        # TODO This warning has to be fixed in asyncio.
        logger = logging.getLogger('asyncio')
        filter = logging.Filter('has no effect when using ssl')
        logger.addFilter(filter)
        try:
            yield
        finally:
            logger.removeFilter(filter)


class UVTestCase(BaseTestCase):

    implementation = 'uvloop'

    def new_loop(self):
        return uvloop.new_event_loop()

    def new_policy(self):
        return uvloop.EventLoopPolicy()


class AIOTestCase(BaseTestCase):

    implementation = 'asyncio'

    def setUp(self):
        super().setUp()

        if sys.version_info < (3, 12):
            watcher = asyncio.SafeChildWatcher()
            watcher.attach_loop(self.loop)
            asyncio.set_child_watcher(watcher)

    def tearDown(self):
        if sys.version_info < (3, 12):
            asyncio.set_child_watcher(None)
        super().tearDown()

    def new_loop(self):
        return asyncio.new_event_loop()

    def new_policy(self):
        return asyncio.DefaultEventLoopPolicy()


def has_IPv6():
    server_sock = socket.socket(socket.AF_INET6)
    with server_sock:
        try:
            server_sock.bind(('::1', 0))
        except OSError:
            return False
        else:
            return True


has_IPv6 = has_IPv6()


###############################################################################
# Socket Testing Utilities
###############################################################################


class TestSocketWrapper:

    def __init__(self, sock):
        self.__sock = sock

    def recv_all(self, n):
        buf = b''
        while len(buf) < n:
            data = self.recv(n - len(buf))
            if data == b'':
                raise ConnectionAbortedError
            buf += data
        return buf

    def starttls(self, ssl_context, *,
                 server_side=False,
                 server_hostname=None,
                 do_handshake_on_connect=True):

        assert isinstance(ssl_context, ssl.SSLContext)

        ssl_sock = ssl_context.wrap_socket(
            self.__sock, server_side=server_side,
            server_hostname=server_hostname,
            do_handshake_on_connect=do_handshake_on_connect)

        if server_side:
            ssl_sock.do_handshake()

        self.__sock.close()
        self.__sock = ssl_sock

    def __getattr__(self, name):
        return getattr(self.__sock, name)

    def __repr__(self):
        return '<{} {!r}>'.format(type(self).__name__, self.__sock)


class SocketThread(threading.Thread):

    def stop(self):
        self._active = False
        self.join()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *exc):
        self.stop()


class TestThreadedClient(SocketThread):

    def __init__(self, test, sock, prog, timeout):
        threading.Thread.__init__(self, None, None, 'test-client')
        self.daemon = True

        self._timeout = timeout
        self._sock = sock
        self._active = True
        self._prog = prog
        self._test = test

    def run(self):
        try:
            self._prog(TestSocketWrapper(self._sock))
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as ex:
            self._test._abort_socket_test(ex)


class TestThreadedServer(SocketThread):

    def __init__(self, test, sock, prog, timeout, max_clients):
        threading.Thread.__init__(self, None, None, 'test-server')
        self.daemon = True

        self._clients = 0
        self._finished_clients = 0
        self._max_clients = max_clients
        self._timeout = timeout
        self._sock = sock
        self._active = True

        self._prog = prog

        self._s1, self._s2 = socket.socketpair()
        self._s1.setblocking(False)

        self._test = test

    def stop(self):
        try:
            if self._s2 and self._s2.fileno() != -1:
                try:
                    self._s2.send(b'stop')
                except OSError:
                    pass
        finally:
            super().stop()

    def run(self):
        try:
            with self._sock:
                self._sock.setblocking(0)
                self._run()
        finally:
            self._s1.close()
            self._s2.close()

    def _run(self):
        while self._active:
            if self._clients >= self._max_clients:
                return

            r, w, x = select.select(
                [self._sock, self._s1], [], [], self._timeout)

            if self._s1 in r:
                return

            if self._sock in r:
                try:
                    conn, addr = self._sock.accept()
                except BlockingIOError:
                    continue
                except socket.timeout:
                    if not self._active:
                        return
                    else:
                        raise
                else:
                    self._clients += 1
                    conn.settimeout(self._timeout)
                    try:
                        with conn:
                            self._handle_client(conn)
                    except (KeyboardInterrupt, SystemExit):
                        raise
                    except BaseException as ex:
                        self._active = False
                        try:
                            raise
                        finally:
                            self._test._abort_socket_test(ex)

    def _handle_client(self, sock):
        self._prog(TestSocketWrapper(sock))

    @property
    def addr(self):
        return self._sock.getsockname()


###############################################################################
# A few helpers from asyncio/tests/testutils.py
###############################################################################


def run_briefly(loop):
    async def once():
        pass
    gen = once()
    t = loop.create_task(gen)
    # Don't log a warning if the task is not done after run_until_complete().
    # It occurs if the loop is stopped or if a task raises a BaseException.
    t._log_destroy_pending = False
    try:
        loop.run_until_complete(t)
    finally:
        gen.close()


def run_until(loop, pred, timeout=30):
    deadline = time.time() + timeout
    while not pred():
        if timeout is not None:
            timeout = deadline - time.time()
            if timeout <= 0:
                raise asyncio.futures.TimeoutError()
        loop.run_until_complete(asyncio.tasks.sleep(0.001))


@contextlib.contextmanager
def disable_logger():
    """Context manager to disable asyncio logger.

    For example, it can be used to ignore warnings in debug mode.
    """
    old_level = asyncio.log.logger.level
    try:
        asyncio.log.logger.setLevel(logging.CRITICAL + 1)
        yield
    finally:
        asyncio.log.logger.setLevel(old_level)
```

## File: `uvloop/_version.py`
```python
# This file MUST NOT contain anything but the __version__ assignment.
#
# When making a release, change the value of __version__
# to an appropriate value, and open a pull request against
# the correct branch (master if making a new feature release).
# The commit message MUST contain a properly formatted release
# log, and the commit must be signed.
#
# The release automation will: build and test the packages for the
# supported platforms, publish the packages on PyPI, merge the PR
# to the target branch, create a Git tag pointing to the commit.

__version__ = '0.22.1'
```

## File: `uvloop/cbhandles.pxd`
```
cdef class Handle:
    cdef:
        Loop loop
        object context
        bint _cancelled

        str meth_name
        int cb_type
        void *callback
        object arg1, arg2, arg3, arg4

        object __weakref__

        readonly _source_traceback

    cdef inline _set_loop(self, Loop loop)
    cdef inline _set_context(self, object context)

    cdef inline _run(self)
    cdef _cancel(self)

    cdef _format_handle(self)


cdef class TimerHandle:
    cdef:
        object callback
        tuple args
        bint _cancelled
        UVTimer timer
        Loop loop
        object context
        tuple _debug_info
        object __weakref__
        object _when

    cdef _run(self)
    cdef _cancel(self)
    cdef inline _clear(self)
```

## File: `uvloop/cbhandles.pyx`
```
@cython.no_gc_clear
@cython.freelist(DEFAULT_FREELIST_SIZE)
cdef class Handle:
    def __cinit__(self):
        self._cancelled = 0
        self.cb_type = 0
        self._source_traceback = None

    cdef inline _set_loop(self, Loop loop):
        self.loop = loop
        if UVLOOP_DEBUG:
            system.__atomic_fetch_add(
                &loop._debug_cb_handles_total, 1, system.__ATOMIC_RELAXED)
            system.__atomic_fetch_add(
                &loop._debug_cb_handles_count, 1, system.__ATOMIC_RELAXED)
        if loop._debug:
            self._source_traceback = extract_stack()

    cdef inline _set_context(self, object context):
        if context is None:
            context = Context_CopyCurrent()
        self.context = context

    def __dealloc__(self):
        if UVLOOP_DEBUG and self.loop is not None:
            system.__atomic_fetch_sub(
                &self.loop._debug_cb_handles_count, 1, system.__ATOMIC_RELAXED)
        if self.loop is None:
            raise RuntimeError('Handle.loop is None in Handle.__dealloc__')

    def __init__(self):
        raise TypeError(
            '{} is not supposed to be instantiated from Python'.format(
                self.__class__.__name__))

    cdef inline _run(self):
        cdef:
            int cb_type
            object callback

        if self._cancelled:
            return

        cb_type = self.cb_type

        # Since _run is a cdef and there's no BoundMethod,
        # we guard 'self' manually (since the callback
        # might cause GC of the handle.)
        Py_INCREF(self)

        try:
            assert self.context is not None
            Context_Enter(self.context)

            if cb_type == 1:
                callback = self.arg1
                if callback is None:
                    raise RuntimeError(
                        'cannot run Handle; callback is not set')

                args = self.arg2

                if args is None:
                    callback()
                else:
                    callback(*args)

            elif cb_type == 2:
                (<method_t>self.callback)(self.arg1)

            elif cb_type == 3:
                (<method1_t>self.callback)(self.arg1, self.arg2)

            elif cb_type == 4:
                (<method2_t>self.callback)(self.arg1, self.arg2, self.arg3)

            elif cb_type == 5:
                (<method3_t>self.callback)(
                    self.arg1, self.arg2, self.arg3, self.arg4)

            else:
                raise RuntimeError('invalid Handle.cb_type: {}'.format(
                    cb_type))

        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as ex:
            if cb_type == 1:
                msg = 'Exception in callback {}'.format(callback)
            else:
                msg = 'Exception in callback {}'.format(self.meth_name)

            context = {
                'message': msg,
                'exception': ex,
                'handle': self,
            }

            if self._source_traceback is not None:
                context['source_traceback'] = self._source_traceback

            self.loop.call_exception_handler(context)

        finally:
            context = self.context
            Py_DECREF(self)
            Context_Exit(context)

    cdef _cancel(self):
        self._cancelled = 1
        self.callback = NULL
        self.arg1 = self.arg2 = self.arg3 = self.arg4 = None

    cdef _format_handle(self):
        # Mirrors `asyncio.base_events._format_handle`.
        if self.cb_type == 1 and self.arg1 is not None:
            cb = self.arg1
            if isinstance(getattr(cb, '__self__', None), aio_Task):
                try:
                    return repr(cb.__self__)
                except (AttributeError, TypeError, ValueError) as ex:
                    # Cython generates empty __code__ objects for coroutines
                    # that can crash asyncio.Task.__repr__ with an
                    # AttributeError etc.  Guard against that.
                    self.loop.call_exception_handler({
                        'message': 'exception in Task.__repr__',
                        'task': cb.__self__,
                        'exception': ex,
                        'handle': self,
                    })
        return repr(self)

    # Public API

    def __repr__(self):
        info = [self.__class__.__name__]

        if self._cancelled:
            info.append('cancelled')

        if self.cb_type == 1 and self.arg1 is not None:
            func = self.arg1
            # Cython can unset func.__qualname__/__name__, hence the checks.
            if hasattr(func, '__qualname__') and func.__qualname__:
                cb_name = func.__qualname__
            elif hasattr(func, '__name__') and func.__name__:
                cb_name = func.__name__
            else:
                cb_name = repr(func)

            info.append(cb_name)
        elif self.meth_name is not None:
            info.append(self.meth_name)

        if self._source_traceback is not None:
            frame = self._source_traceback[-1]
            info.append('created at {}:{}'.format(frame[0], frame[1]))

        return '<' + ' '.join(info) + '>'

    def cancel(self):
        self._cancel()

    def cancelled(self):
        return self._cancelled


@cython.no_gc_clear
@cython.freelist(DEFAULT_FREELIST_SIZE)
cdef class TimerHandle:
    def __cinit__(self, Loop loop, object callback, object args,
                  uint64_t delay, object context):

        self.loop = loop
        self.callback = callback
        self.args = args
        self._cancelled = 0

        if UVLOOP_DEBUG:
            system.__atomic_fetch_add(
                &self.loop._debug_cb_timer_handles_total, 1, system.__ATOMIC_RELAXED)
            system.__atomic_fetch_add(
                &self.loop._debug_cb_timer_handles_count, 1, system.__ATOMIC_RELAXED)

        if context is None:
            context = Context_CopyCurrent()
        self.context = context

        if loop._debug:
            self._debug_info = (
                format_callback_name(callback),
                extract_stack()
            )
        else:
            self._debug_info = None

        self.timer = UVTimer.new(
            loop, <method_t>self._run, self, delay)

        self.timer.start()
        self._when = self.timer.get_when() * 1e-3

        # Only add to loop._timers when `self.timer` is successfully created
        loop._timers.add(self)

    property _source_traceback:
        def __get__(self):
            if self._debug_info is not None:
                return self._debug_info[1]

    def __dealloc__(self):
        if UVLOOP_DEBUG:
            system.__atomic_fetch_sub(
                &self.loop._debug_cb_timer_handles_count, 1, system.__ATOMIC_RELAXED)
        if self.timer is not None:
            raise RuntimeError('active TimerHandle is deallacating')

    cdef _cancel(self):
        if self._cancelled == 1:
            return
        self._cancelled = 1
        self._clear()

    cdef inline _clear(self):
        if self.timer is None:
            return

        self.callback = None
        self.args = None

        try:
            self.loop._timers.remove(self)
        finally:
            self.timer._close()
            self.timer = None  # let the UVTimer handle GC

    cdef _run(self):
        if self._cancelled == 1:
            return
        if self.callback is None:
            raise RuntimeError('cannot run TimerHandle; callback is not set')

        callback = self.callback
        args = self.args

        # Since _run is a cdef and there's no BoundMethod,
        # we guard 'self' manually.
        Py_INCREF(self)

        if self.loop._debug:
            started = time_monotonic()
        try:
            assert self.context is not None
            Context_Enter(self.context)

            if args is not None:
                callback(*args)
            else:
                callback()
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as ex:
            context = {
                'message': 'Exception in callback {}'.format(callback),
                'exception': ex,
                'handle': self,
            }

            if self._debug_info is not None:
                context['source_traceback'] = self._debug_info[1]

            self.loop.call_exception_handler(context)
        else:
            if self.loop._debug:
                delta = time_monotonic() - started
                if delta > self.loop.slow_callback_duration:
                    aio_logger.warning(
                        'Executing %r took %.3f seconds',
                        self, delta)
        finally:
            context = self.context
            Py_DECREF(self)
            Context_Exit(context)
            self._clear()

    # Public API

    def __repr__(self):
        info = [self.__class__.__name__]

        if self._cancelled:
            info.append('cancelled')

        if self._debug_info is not None:
            callback_name = self._debug_info[0]
            source_traceback = self._debug_info[1]
        else:
            callback_name = None
            source_traceback = None

        if callback_name is not None:
            info.append(callback_name)
        elif self.callback is not None:
            info.append(format_callback_name(self.callback))

        if source_traceback is not None:
            frame = source_traceback[-1]
            info.append('created at {}:{}'.format(frame[0], frame[1]))

        return '<' + ' '.join(info) + '>'

    def cancelled(self):
        return self._cancelled

    def cancel(self):
        self._cancel()

    def when(self):
        return self._when


cdef format_callback_name(func):
    if hasattr(func, '__qualname__'):
        cb_name = getattr(func, '__qualname__')
    elif hasattr(func, '__name__'):
        cb_name = getattr(func, '__name__')
    else:
        cb_name = repr(func)
    return cb_name


cdef new_Handle(Loop loop, object callback, object args, object context):
    cdef Handle handle
    handle = Handle.__new__(Handle)
    handle._set_loop(loop)
    handle._set_context(context)

    handle.cb_type = 1

    handle.arg1 = callback
    handle.arg2 = args

    return handle


cdef new_MethodHandle(Loop loop, str name, method_t callback, object context,
                      object bound_to):
    cdef Handle handle
    handle = Handle.__new__(Handle)
    handle._set_loop(loop)
    handle._set_context(context)

    handle.cb_type = 2
    handle.meth_name = name

    handle.callback = <void*> callback
    handle.arg1 = bound_to

    return handle


cdef new_MethodHandle1(Loop loop, str name, method1_t callback, object context,
                       object bound_to, object arg):

    cdef Handle handle
    handle = Handle.__new__(Handle)
    handle._set_loop(loop)
    handle._set_context(context)

    handle.cb_type = 3
    handle.meth_name = name

    handle.callback = <void*> callback
    handle.arg1 = bound_to
    handle.arg2 = arg

    return handle


cdef new_MethodHandle2(Loop loop, str name, method2_t callback, object context,
                       object bound_to, object arg1, object arg2):

    cdef Handle handle
    handle = Handle.__new__(Handle)
    handle._set_loop(loop)
    handle._set_context(context)

    handle.cb_type = 4
    handle.meth_name = name

    handle.callback = <void*> callback
    handle.arg1 = bound_to
    handle.arg2 = arg1
    handle.arg3 = arg2

    return handle


cdef new_MethodHandle3(Loop loop, str name, method3_t callback, object context,
                       object bound_to, object arg1, object arg2, object arg3):

    cdef Handle handle
    handle = Handle.__new__(Handle)
    handle._set_loop(loop)
    handle._set_context(context)

    handle.cb_type = 5
    handle.meth_name = name

    handle.callback = <void*> callback
    handle.arg1 = bound_to
    handle.arg2 = arg1
    handle.arg3 = arg2
    handle.arg4 = arg3

    return handle


cdef extract_stack():
    """Replacement for traceback.extract_stack() that only does the
    necessary work for asyncio debug mode.
    """
    try:
        f = sys_getframe()
    # sys._getframe() might raise ValueError if being called without a frame, e.g.
    # from Cython or similar C extensions.
    except ValueError:
        return None
    if f is None:
        return

    try:
        stack = tb_StackSummary.extract(tb_walk_stack(f),
                                        limit=DEBUG_STACK_DEPTH,
                                        lookup_lines=False)
    finally:
        f = None

    stack.reverse()
    return stack
```

## File: `uvloop/dns.pyx`
```
cdef __port_to_int(port, proto):
    if type(port) is int:
        return port

    if port is None or port == '' or port == b'':
        return 0

    try:
        return int(port)
    except (ValueError, TypeError):
        pass

    if isinstance(port, bytes):
        port = port.decode()

    if isinstance(port, str) and proto is not None:
        if proto == uv.IPPROTO_TCP:
            return socket_getservbyname(port, 'tcp')
        elif proto == uv.IPPROTO_UDP:
            return socket_getservbyname(port, 'udp')

    raise OSError('service/proto not found')


cdef __convert_sockaddr_to_pyaddr(const system.sockaddr* addr):
    # Converts sockaddr structs into what Python socket
    # module can understand:
    #   - for IPv4 a tuple of (host, port)
    #   - for IPv6 a tuple of (host, port, flowinfo, scope_id)

    cdef:
        char buf[128]  # INET6_ADDRSTRLEN is usually 46
        int err
        system.sockaddr_in *addr4
        system.sockaddr_in6 *addr6
        system.sockaddr_un *addr_un

    if addr.sa_family == uv.AF_INET:
        addr4 = <system.sockaddr_in*>addr

        err = uv.uv_ip4_name(addr4, buf, sizeof(buf))
        if err < 0:
            raise convert_error(err)

        return (
            PyUnicode_FromString(buf),
            system.ntohs(addr4.sin_port)
        )

    elif addr.sa_family == uv.AF_INET6:
        addr6 = <system.sockaddr_in6*>addr

        err = uv.uv_ip6_name(addr6, buf, sizeof(buf))
        if err < 0:
            raise convert_error(err)

        return (
            PyUnicode_FromString(buf),
            system.ntohs(addr6.sin6_port),
            system.ntohl(addr6.sin6_flowinfo),
            addr6.sin6_scope_id
        )

    elif addr.sa_family == uv.AF_UNIX:
        addr_un = <system.sockaddr_un*>addr
        return system.MakeUnixSockPyAddr(addr_un)

    raise RuntimeError("cannot convert sockaddr into Python object")


@cython.freelist(DEFAULT_FREELIST_SIZE)
cdef class SockAddrHolder:
    cdef:
        int family
        system.sockaddr_storage addr
        Py_ssize_t addr_size


cdef LruCache sockaddrs = LruCache(maxsize=DNS_PYADDR_TO_SOCKADDR_CACHE_SIZE)


cdef __convert_pyaddr_to_sockaddr(int family, object addr,
                                  system.sockaddr* res):
    cdef:
        int err
        int addr_len
        int scope_id = 0
        int flowinfo = 0
        char *buf
        Py_ssize_t buflen
        SockAddrHolder ret

    ret = sockaddrs.get(addr, None)
    if ret is not None and ret.family == family:
        memcpy(res, &ret.addr, ret.addr_size)
        return

    ret = SockAddrHolder.__new__(SockAddrHolder)
    if family == uv.AF_INET:
        if not isinstance(addr, tuple):
            raise TypeError('AF_INET address must be tuple')
        if len(addr) != 2:
            raise ValueError('AF_INET address must be tuple of (host, port)')
        host, port = addr
        if isinstance(host, str):
            try:
                # idna codec is rather slow, so we try ascii first.
                host = host.encode('ascii')
            except UnicodeEncodeError:
                host = host.encode('idna')
        if not isinstance(host, (bytes, bytearray)):
            raise TypeError('host must be a string or bytes object')

        port = __port_to_int(port, None)

        ret.addr_size = sizeof(system.sockaddr_in)
        err = uv.uv_ip4_addr(host, <int>port, <system.sockaddr_in*>&ret.addr)
        if err < 0:
            raise convert_error(err)

    elif family == uv.AF_INET6:
        if not isinstance(addr, tuple):
            raise TypeError('AF_INET6 address must be tuple')

        addr_len = len(addr)
        if addr_len < 2 or addr_len > 4:
            raise ValueError(
                'AF_INET6 must be a tuple of 2-4 parameters: '
                '(host, port, flowinfo?, scope_id?)')

        host = addr[0]
        if isinstance(host, str):
            try:
                # idna codec is rather slow, so we try ascii first.
                host = host.encode('ascii')
            except UnicodeEncodeError:
                host = host.encode('idna')
        if not isinstance(host, (bytes, bytearray)):
            raise TypeError('host must be a string or bytes object')

        port = __port_to_int(addr[1], None)

        if addr_len > 2:
            flowinfo = addr[2]
        if addr_len > 3:
            scope_id = addr[3]

        ret.addr_size = sizeof(system.sockaddr_in6)

        err = uv.uv_ip6_addr(host, port, <system.sockaddr_in6*>&ret.addr)
        if err < 0:
            raise convert_error(err)

        (<system.sockaddr_in6*>&ret.addr).sin6_flowinfo = flowinfo
        (<system.sockaddr_in6*>&ret.addr).sin6_scope_id = scope_id

    elif family == uv.AF_UNIX:
        if isinstance(addr, str):
            addr = addr.encode(sys_getfilesystemencoding())
        elif not isinstance(addr, bytes):
            raise TypeError('AF_UNIX address must be a str or a bytes object')

        PyBytes_AsStringAndSize(addr, &buf, &buflen)
        if buflen > 107:
            raise ValueError(
                f'unix socket path {addr!r} is longer than 107 characters')

        ret.addr_size = sizeof(system.sockaddr_un)
        memset(&ret.addr, 0, sizeof(system.sockaddr_un))
        (<system.sockaddr_un*>&ret.addr).sun_family = uv.AF_UNIX
        memcpy((<system.sockaddr_un*>&ret.addr).sun_path, buf, buflen)

    else:
        raise ValueError(
            f'expected AF_INET, AF_INET6, or AF_UNIX family, got {family}')

    ret.family = family
    sockaddrs[addr] = ret
    memcpy(res, &ret.addr, ret.addr_size)


cdef __static_getaddrinfo(object host, object port,
                          int family, int type,
                          int proto,
                          system.sockaddr *addr):

    if proto not in {0, uv.IPPROTO_TCP, uv.IPPROTO_UDP}:
        return

    if _is_sock_stream(type):
        proto = uv.IPPROTO_TCP
    elif _is_sock_dgram(type):
        proto = uv.IPPROTO_UDP
    else:
        return

    try:
        port = __port_to_int(port, proto)
    except Exception:
        return

    hp = (host, port)
    if family == uv.AF_UNSPEC:
        try:
            __convert_pyaddr_to_sockaddr(uv.AF_INET, hp, addr)
        except Exception:
            pass
        else:
            return (uv.AF_INET, type, proto)

        try:
            __convert_pyaddr_to_sockaddr(uv.AF_INET6, hp, addr)
        except Exception:
            pass
        else:
            return (uv.AF_INET6, type, proto)

    else:
        try:
            __convert_pyaddr_to_sockaddr(family, hp, addr)
        except Exception:
            pass
        else:
            return (family, type, proto)


cdef __static_getaddrinfo_pyaddr(object host, object port,
                                 int family, int type,
                                 int proto, int flags):

    cdef:
        system.sockaddr_storage addr
        object triplet

    triplet = __static_getaddrinfo(
        host, port, family, type,
        proto, <system.sockaddr*>&addr)
    if triplet is None:
        return

    af, type, proto = triplet

    try:
        pyaddr = __convert_sockaddr_to_pyaddr(<system.sockaddr*>&addr)
    except Exception:
        return

    # When the host is an IP while type is one of TCP or UDP, different libc
    # implementations of getaddrinfo() behave differently:
    # 1. When AI_CANONNAME is set:
    #    * glibc: returns ai_canonname
    #    * musl: returns ai_canonname
    #    * macOS: returns an empty string for ai_canonname
    # 2. When AI_CANONNAME is NOT set:
    #    * glibc: returns an empty string for ai_canonname
    #    * musl: returns ai_canonname
    #    * macOS: returns an empty string for ai_canonname
    # At the same time, libuv and CPython both uses libc directly, even though
    # this different behavior is violating what is in the documentation.
    #
    # uvloop potentially should be a 100% drop-in replacement for asyncio,
    # doing whatever asyncio does, especially when the libc implementations are
    # also different in the same way. However, making our implementation to be
    # consistent with libc/CPython would be complex and hard to maintain
    # (including caching libc behaviors when flag is/not set), therefore we
    # decided to simply normalize the behavior in uvloop for this very marginal
    # case following the documentation, even though uvloop would behave
    # differently to asyncio on macOS and musl platforms, when again the host
    # is an IP and type is one of TCP or UDP.
    # All other cases are still asyncio-compatible.
    if flags & socket_AI_CANONNAME:
        if isinstance(host, str):
            canon_name = host
        else:
            canon_name = host.decode('ascii')
    else:
        canon_name = ''

    return (
        _intenum_converter(af, socket_AddressFamily),
        _intenum_converter(type, socket_SocketKind),
        proto,
        canon_name,
        pyaddr,
    )


@cython.freelist(DEFAULT_FREELIST_SIZE)
cdef class AddrInfo:
    cdef:
        system.addrinfo *data

    def __cinit__(self):
        self.data = NULL

    def __dealloc__(self):
        if self.data is not NULL:
            uv.uv_freeaddrinfo(self.data)  # returns void
            self.data = NULL

    cdef void set_data(self, system.addrinfo *data) noexcept:
        self.data = data

    cdef unpack(self):
        cdef:
            list result = []
            system.addrinfo *ptr

        if self.data is NULL:
            raise RuntimeError('AddrInfo.data is NULL')

        ptr = self.data
        while ptr != NULL:
            if ptr.ai_addr.sa_family in (uv.AF_INET, uv.AF_INET6):
                result.append((
                    _intenum_converter(ptr.ai_family, socket_AddressFamily),
                    _intenum_converter(ptr.ai_socktype, socket_SocketKind),
                    ptr.ai_protocol,
                    ('' if ptr.ai_canonname is NULL else
                        (<bytes>ptr.ai_canonname).decode()),
                    __convert_sockaddr_to_pyaddr(ptr.ai_addr)
                ))

            ptr = ptr.ai_next

        return result

    @staticmethod
    cdef int isinstance(object other):
        return type(other) is AddrInfo


cdef class AddrInfoRequest(UVRequest):
    cdef:
        system.addrinfo hints
        object callback
        uv.uv_getaddrinfo_t _req_data

    def __cinit__(self, Loop loop,
                  bytes host, bytes port,
                  int family, int type, int proto, int flags,
                  object callback):

        cdef:
            int err
            char *chost
            char *cport

        if host is None:
            chost = NULL
        elif host == b'' and sys.platform == 'darwin':
            # It seems `getaddrinfo("", ...)` on macOS is equivalent to
            # `getaddrinfo("localhost", ...)`. This is inconsistent with
            # libuv 1.48 which treats empty nodename as EINVAL.
            chost = <char*>'localhost'
        else:
            chost = <char*>host

        if port is None:
            cport = NULL
        else:
            cport = <char*>port

        memset(&self.hints, 0, sizeof(system.addrinfo))
        self.hints.ai_flags = flags
        self.hints.ai_family = family
        self.hints.ai_socktype = type
        self.hints.ai_protocol = proto

        self.request = <uv.uv_req_t*> &self._req_data
        self.callback = callback
        self.request.data = <void*>self

        err = uv.uv_getaddrinfo(loop.uvloop,
                                <uv.uv_getaddrinfo_t*>self.request,
                                __on_addrinfo_resolved,
                                chost,
                                cport,
                                &self.hints)

        if err < 0:
            self.on_done()
            try:
                if err == uv.UV_EINVAL:
                    # Convert UV_EINVAL to EAI_NONAME to match libc behavior
                    msg = system.gai_strerror(socket_EAI_NONAME).decode('utf-8')
                    ex = socket_gaierror(socket_EAI_NONAME, msg)
                else:
                    ex = convert_error(err)
            except Exception as ex:
                callback(ex)
            else:
                callback(ex)


cdef class NameInfoRequest(UVRequest):
    cdef:
        object callback
        uv.uv_getnameinfo_t _req_data

    def __cinit__(self, Loop loop, callback):
        self.request = <uv.uv_req_t*> &self._req_data
        self.callback = callback
        self.request.data = <void*>self

    cdef query(self, system.sockaddr *addr, int flags):
        cdef int err
        err = uv.uv_getnameinfo(self.loop.uvloop,
                                <uv.uv_getnameinfo_t*>self.request,
                                __on_nameinfo_resolved,
                                addr,
                                flags)
        if err < 0:
            self.on_done()
            self.callback(convert_error(err))


cdef _intenum_converter(value, enum_klass):
    try:
        return enum_klass(value)
    except ValueError:
        return value


cdef void __on_addrinfo_resolved(
    uv.uv_getaddrinfo_t *resolver,
    int status,
    system.addrinfo *res,
) noexcept with gil:

    if resolver.data is NULL:
        aio_logger.error(
            'AddrInfoRequest callback called with NULL resolver.data')
        return

    cdef:
        AddrInfoRequest request = <AddrInfoRequest> resolver.data
        Loop loop = request.loop
        object callback = request.callback
        AddrInfo ai

    try:
        if status < 0:
            callback(convert_error(status))
        else:
            ai = AddrInfo()
            ai.set_data(res)
            callback(ai)
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as ex:
        loop._handle_exception(ex)
    finally:
        request.on_done()


cdef void __on_nameinfo_resolved(
    uv.uv_getnameinfo_t* req,
    int status,
    const char* hostname,
    const char* service,
) noexcept with gil:
    cdef:
        NameInfoRequest request = <NameInfoRequest> req.data
        Loop loop = request.loop
        object callback = request.callback

    try:
        if status < 0:
            callback(convert_error(status))
        else:
            callback(((<bytes>hostname).decode(),
                      (<bytes>service).decode()))
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as ex:
        loop._handle_exception(ex)
    finally:
        request.on_done()
```

## File: `uvloop/errors.pyx`
```
cdef str __strerr(int errno):
    return strerror(errno).decode()


cdef __convert_python_error(int uverr):
    # XXX Won't work for Windows:
    # From libuv docs:
    #      Implementation detail: on Unix error codes are the
    #      negated errno (or -errno), while on Windows they
    #      are defined by libuv to arbitrary negative numbers.
    cdef int oserr = -uverr

    exc = OSError

    if uverr in (uv.UV_EACCES, uv.UV_EPERM):
        exc = PermissionError

    elif uverr in (uv.UV_EAGAIN, uv.UV_EALREADY):
        exc = BlockingIOError

    elif uverr in (uv.UV_EPIPE, uv.UV_ESHUTDOWN):
        exc = BrokenPipeError

    elif uverr == uv.UV_ECONNABORTED:
        exc = ConnectionAbortedError

    elif uverr == uv.UV_ECONNREFUSED:
        exc = ConnectionRefusedError

    elif uverr == uv.UV_ECONNRESET:
        exc = ConnectionResetError

    elif uverr == uv.UV_EEXIST:
        exc = FileExistsError

    elif uverr == uv.UV_ENOENT:
        exc = FileNotFoundError

    elif uverr == uv.UV_EINTR:
        exc = InterruptedError

    elif uverr == uv.UV_EISDIR:
        exc = IsADirectoryError

    elif uverr == uv.UV_ESRCH:
        exc = ProcessLookupError

    elif uverr == uv.UV_ETIMEDOUT:
        exc = TimeoutError

    return exc(oserr, __strerr(oserr))


cdef int __convert_socket_error(int uverr):
    cdef int sock_err = 0

    if uverr == uv.UV_EAI_ADDRFAMILY:
        sock_err = socket_EAI_ADDRFAMILY

    elif uverr == uv.UV_EAI_AGAIN:
        sock_err = socket_EAI_AGAIN

    elif uverr == uv.UV_EAI_BADFLAGS:
        sock_err = socket_EAI_BADFLAGS

    elif uverr == uv.UV_EAI_BADHINTS:
        sock_err = socket_EAI_BADHINTS

    elif uverr == uv.UV_EAI_CANCELED:
        sock_err = socket_EAI_CANCELED

    elif uverr == uv.UV_EAI_FAIL:
        sock_err = socket_EAI_FAIL

    elif uverr == uv.UV_EAI_FAMILY:
        sock_err = socket_EAI_FAMILY

    elif uverr == uv.UV_EAI_MEMORY:
        sock_err = socket_EAI_MEMORY

    elif uverr == uv.UV_EAI_NODATA:
        sock_err = socket_EAI_NODATA

    elif uverr == uv.UV_EAI_NONAME:
        sock_err = socket_EAI_NONAME

    elif uverr == uv.UV_EAI_OVERFLOW:
        sock_err = socket_EAI_OVERFLOW

    elif uverr == uv.UV_EAI_PROTOCOL:
        sock_err = socket_EAI_PROTOCOL

    elif uverr == uv.UV_EAI_SERVICE:
        sock_err = socket_EAI_SERVICE

    elif uverr == uv.UV_EAI_SOCKTYPE:
        sock_err = socket_EAI_SOCKTYPE

    return sock_err


cdef convert_error(int uverr):
    cdef int sock_err

    if uverr == uv.UV_ECANCELED:
        return aio_CancelledError()

    sock_err = __convert_socket_error(uverr)
    if sock_err:
        msg = system.gai_strerror(sock_err).decode('utf-8')
        return socket_gaierror(sock_err, msg)

    return __convert_python_error(uverr)
```

## File: `uvloop/loop.pxd`
```
# cython: language_level=3


from .includes cimport uv
from .includes cimport system

from libc.stdint cimport uint64_t, uint32_t, int64_t


include "includes/consts.pxi"


cdef extern from *:
    ctypedef int vint "volatile int"


cdef class UVHandle
cdef class UVSocketHandle(UVHandle)

cdef class UVAsync(UVHandle)
cdef class UVTimer(UVHandle)
cdef class UVIdle(UVHandle)

cdef class UVBaseTransport(UVSocketHandle)

ctypedef object (*method_t)(object)
ctypedef object (*method1_t)(object, object)
ctypedef object (*method2_t)(object, object, object)
ctypedef object (*method3_t)(object, object, object, object)


cdef class Loop:
    cdef:
        uv.uv_loop_t *uvloop

        bint _coroutine_debug_set
        int _coroutine_origin_tracking_saved_depth

        public slow_callback_duration

        readonly bint _closed
        bint _debug
        bint _running
        bint _stopping

        uint64_t _thread_id

        object _task_factory
        object _exception_handler
        object _default_executor
        object _ready
        set _queued_streams, _executing_streams

        set _servers

        object _transports
        set _processes
        dict _fd_to_reader_fileobj
        dict _fd_to_writer_fileobj
        dict _unix_server_sockets

        set _signals
        dict _signal_handlers
        object _ssock
        object _csock
        bint _listening_signals
        int _old_signal_wakeup_id

        set _timers
        dict _polls

        UVProcess active_process_handler

        UVAsync handler_async
        UVIdle handler_idle
        UVCheck handler_check__exec_writes

        object _last_error

        cdef object __weakref__

        object _asyncgens
        bint _asyncgens_shutdown_called

        bint _executor_shutdown_called

        char _recv_buffer[UV_STREAM_RECV_BUF_SIZE]
        bint _recv_buffer_in_use

        # DEBUG fields
        # True when compiled with DEBUG.
        # Used only in unittests.
        readonly bint _debug_cc

        readonly object _debug_handles_total
        readonly object _debug_handles_closed
        readonly object _debug_handles_current

        readonly uint64_t _debug_uv_handles_total
        readonly uint64_t _debug_uv_handles_freed

        readonly uint64_t _debug_cb_handles_total
        readonly uint64_t _debug_cb_handles_count
        readonly uint64_t _debug_cb_timer_handles_total
        readonly uint64_t _debug_cb_timer_handles_count

        readonly uint64_t _debug_stream_shutdown_errors_total
        readonly uint64_t _debug_stream_listen_errors_total

        readonly uint64_t _debug_stream_read_cb_total
        readonly uint64_t _debug_stream_read_cb_errors_total
        readonly uint64_t _debug_stream_read_eof_total
        readonly uint64_t _debug_stream_read_eof_cb_errors_total
        readonly uint64_t _debug_stream_read_errors_total

        readonly uint64_t _debug_stream_write_tries
        readonly uint64_t _debug_stream_write_errors_total
        readonly uint64_t _debug_stream_write_ctx_total
        readonly uint64_t _debug_stream_write_ctx_cnt
        readonly uint64_t _debug_stream_write_cb_errors_total

        readonly uint64_t _poll_read_events_total
        readonly uint64_t _poll_read_cb_errors_total
        readonly uint64_t _poll_write_events_total
        readonly uint64_t _poll_write_cb_errors_total

        readonly uint64_t _sock_try_write_total

        readonly uint64_t _debug_exception_handler_cnt

    cdef _init_debug_fields(self)

    cdef _on_wake(self)
    cdef _on_idle(self)

    cdef __run(self, uv.uv_run_mode)
    cdef _run(self, uv.uv_run_mode)

    cdef _close(self)
    cdef _stop(self, exc)
    cdef uint64_t _time(self)

    cdef inline _queue_write(self, UVStream stream)
    cdef _exec_queued_writes(self)

    cdef inline _call_soon(self, object callback, object args, object context)
    cdef inline _append_ready_handle(self, Handle handle)
    cdef inline _call_soon_handle(self, Handle handle)

    cdef _call_later(self, uint64_t delay, object callback, object args,
                     object context)

    cdef void _handle_exception(self, object ex)

    cdef inline _is_main_thread(self)

    cdef inline _new_future(self)
    cdef inline _check_signal(self, sig)
    cdef inline _check_closed(self)
    cdef inline _check_thread(self)

    cdef _getaddrinfo(self, object host, object port,
                      int family, int type,
                      int proto, int flags,
                      int unpack)

    cdef _getnameinfo(self, system.sockaddr *addr, int flags)

    cdef _track_transport(self, UVBaseTransport transport)
    cdef _fileobj_to_fd(self, fileobj)
    cdef _ensure_fd_no_transport(self, fd)

    cdef _track_process(self, UVProcess proc)
    cdef _untrack_process(self, UVProcess proc)

    cdef _add_reader(self, fd, Handle handle)
    cdef _has_reader(self, fd)
    cdef _remove_reader(self, fd)

    cdef _add_writer(self, fd, Handle handle)
    cdef _has_writer(self, fd)
    cdef _remove_writer(self, fd)

    cdef _sock_recv(self, fut, sock, n)
    cdef _sock_recv_into(self, fut, sock, buf)
    cdef _sock_sendall(self, fut, sock, data)
    cdef _sock_accept(self, fut, sock)

    cdef _sock_connect(self, sock, address)
    cdef _sock_connect_cb(self, fut, sock, address)

    cdef _sock_set_reuseport(self, int fd)

    cdef _setup_or_resume_signals(self)
    cdef _shutdown_signals(self)
    cdef _pause_signals(self)

    cdef _handle_signal(self, sig)
    cdef _read_from_self(self)
    cdef inline _ceval_process_signals(self)
    cdef _invoke_signals(self, bytes data)

    cdef _set_coroutine_debug(self, bint enabled)

    cdef _print_debug_info(self)


include "cbhandles.pxd"

include "handles/handle.pxd"
include "handles/async_.pxd"
include "handles/idle.pxd"
include "handles/check.pxd"
include "handles/timer.pxd"
include "handles/poll.pxd"
include "handles/basetransport.pxd"
include "handles/stream.pxd"
include "handles/streamserver.pxd"
include "handles/tcp.pxd"
include "handles/pipe.pxd"
include "handles/process.pxd"
include "handles/fsevent.pxd"

include "request.pxd"
include "sslproto.pxd"

include "handles/udp.pxd"

include "server.pxd"
```

## File: `uvloop/loop.pyi`
```
import asyncio
import ssl
import sys
from socket import AddressFamily, SocketKind, _Address, _RetAddress, socket
from typing import (
    IO,
    Any,
    Awaitable,
    Callable,
    Dict,
    Generator,
    List,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
    overload,
)

_T = TypeVar('_T')
_Context = Dict[str, Any]
_ExceptionHandler = Callable[[asyncio.AbstractEventLoop, _Context], Any]
_SSLContext = Union[bool, None, ssl.SSLContext]
_ProtocolT = TypeVar("_ProtocolT", bound=asyncio.BaseProtocol)

class Loop:
    def call_soon(
        self, callback: Callable[..., Any], *args: Any, context: Optional[Any] = ...
    ) -> asyncio.Handle: ...
    def call_soon_threadsafe(
        self, callback: Callable[..., Any], *args: Any, context: Optional[Any] = ...
    ) -> asyncio.Handle: ...
    def call_later(
        self, delay: float, callback: Callable[..., Any], *args: Any, context: Optional[Any] = ...
    ) -> asyncio.TimerHandle: ...
    def call_at(
        self, when: float, callback: Callable[..., Any], *args: Any, context: Optional[Any] = ...
    ) -> asyncio.TimerHandle: ...
    def time(self) -> float: ...
    def stop(self) -> None: ...
    def run_forever(self) -> None: ...
    def close(self) -> None: ...
    def get_debug(self) -> bool: ...
    def set_debug(self, enabled: bool) -> None: ...
    def is_running(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def create_future(self) -> asyncio.Future[Any]: ...
    def create_task(
        self,
        coro: Union[Awaitable[_T], Generator[Any, None, _T]],
        *,
        name: Optional[str] = ...,
    ) -> asyncio.Task[_T]: ...
    def set_task_factory(
        self,
        factory: Optional[
            Callable[[asyncio.AbstractEventLoop, Generator[Any, None, _T]], asyncio.Future[_T]]
        ],
    ) -> None: ...
    def get_task_factory(
        self,
    ) -> Optional[
        Callable[[asyncio.AbstractEventLoop, Generator[Any, None, _T]], asyncio.Future[_T]]
    ]: ...
    @overload
    def run_until_complete(self, future: Generator[Any, None, _T]) -> _T: ...
    @overload
    def run_until_complete(self, future: Awaitable[_T]) -> _T: ...
    async def getaddrinfo(
        self,
        host: Optional[Union[str, bytes]],
        port: Optional[Union[str, bytes, int]],
        *,
        family: int = ...,
        type: int = ...,
        proto: int = ...,
        flags: int = ...,
    ) -> List[
        Tuple[
            AddressFamily,
            SocketKind,
            int,
            str,
            Union[Tuple[str, int], Tuple[str, int, int, int]],
        ]
    ]: ...
    async def getnameinfo(
        self,
        sockaddr: Union[
            Tuple[str, int],
            Tuple[str, int, int],
            Tuple[str, int, int, int]
        ],
        flags: int = ...,
    ) -> Tuple[str, str]: ...
    async def start_tls(
        self,
        transport: asyncio.BaseTransport,
        protocol: asyncio.BaseProtocol,
        sslcontext: ssl.SSLContext,
        *,
        server_side: bool = ...,
        server_hostname: Optional[str] = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
    ) -> asyncio.BaseTransport: ...
    @overload
    async def create_server(
        self,
        protocol_factory: asyncio.events._ProtocolFactory,
        host: Optional[Union[str, Sequence[str]]] = ...,
        port: int = ...,
        *,
        family: int = ...,
        flags: int = ...,
        sock: None = ...,
        backlog: int = ...,
        ssl: _SSLContext = ...,
        reuse_address: Optional[bool] = ...,
        reuse_port: Optional[bool] = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
        start_serving: bool = ...,
    ) -> asyncio.AbstractServer: ...
    @overload
    async def create_server(
        self,
        protocol_factory: asyncio.events._ProtocolFactory,
        host: None = ...,
        port: None = ...,
        *,
        family: int = ...,
        flags: int = ...,
        sock: socket = ...,
        backlog: int = ...,
        ssl: _SSLContext = ...,
        reuse_address: Optional[bool] = ...,
        reuse_port: Optional[bool] = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
        start_serving: bool = ...,
    ) -> asyncio.AbstractServer: ...
    @overload
    async def create_connection(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        host: str = ...,
        port: int = ...,
        *,
        ssl: _SSLContext = ...,
        family: int = ...,
        proto: int = ...,
        flags: int = ...,
        sock: None = ...,
        local_addr: Optional[Tuple[str, int]] = ...,
        server_hostname: Optional[str] = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    @overload
    async def create_connection(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        host: None = ...,
        port: None = ...,
        *,
        ssl: _SSLContext = ...,
        family: int = ...,
        proto: int = ...,
        flags: int = ...,
        sock: socket,
        local_addr: None = ...,
        server_hostname: Optional[str] = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    async def create_unix_server(
        self,
        protocol_factory: asyncio.events._ProtocolFactory,
        path: Optional[str] = ...,
        *,
        backlog: int = ...,
        sock: Optional[socket] = ...,
        ssl: _SSLContext = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
        start_serving: bool = ...,
    ) -> asyncio.AbstractServer: ...
    async def create_unix_connection(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        path: Optional[str] = ...,
        *,
        ssl: _SSLContext = ...,
        sock: Optional[socket] = ...,
        server_hostname: Optional[str] = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    def default_exception_handler(self, context: _Context) -> None: ...
    def get_exception_handler(self) -> Optional[_ExceptionHandler]: ...
    def set_exception_handler(self, handler: Optional[_ExceptionHandler]) -> None: ...
    def call_exception_handler(self, context: _Context) -> None: ...
    def add_reader(self, fd: Any, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_reader(self, fd: Any) -> None: ...
    def add_writer(self, fd: Any, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_writer(self, fd: Any) -> None: ...
    async def sock_recv(self, sock: socket, nbytes: int) -> bytes: ...
    async def sock_recv_into(self, sock: socket, buf: bytearray) -> int: ...
    async def sock_sendall(self, sock: socket, data: bytes) -> None: ...
    async def sock_accept(self, sock: socket) -> Tuple[socket, _RetAddress]: ...
    async def sock_connect(self, sock: socket, address: _Address) -> None: ...
    async def sock_recvfrom(self, sock: socket, bufsize: int) -> bytes: ...
    async def sock_recvfrom_into(self, sock: socket, buf: bytearray, nbytes: int = ...) -> int: ...
    async def sock_sendto(self, sock: socket, data: bytes, address: _Address) -> None: ...
    async def connect_accepted_socket(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        sock: socket,
        *,
        ssl: _SSLContext = ...,
        ssl_handshake_timeout: Optional[float] = ...,
        ssl_shutdown_timeout: Optional[float] = ...,
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    async def run_in_executor(
        self, executor: Any, func: Callable[..., _T], *args: Any
    ) -> _T: ...
    def set_default_executor(self, executor: Any) -> None: ...
    async def subprocess_shell(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        cmd: Union[bytes, str],
        *,
        stdin: Any = ...,
        stdout: Any = ...,
        stderr: Any = ...,
        **kwargs: Any,
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    async def subprocess_exec(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        *args: Any,
        stdin: Any = ...,
        stdout: Any = ...,
        stderr: Any = ...,
        **kwargs: Any,
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    async def connect_read_pipe(
        self, protocol_factory: Callable[[], _ProtocolT], pipe: Any
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    async def connect_write_pipe(
        self, protocol_factory: Callable[[], _ProtocolT], pipe: Any
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    def add_signal_handler(
        self, sig: int, callback: Callable[..., Any], *args: Any
    ) -> None: ...
    def remove_signal_handler(self, sig: int) -> bool: ...
    async def create_datagram_endpoint(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        local_addr: Optional[Tuple[str, int]] = ...,
        remote_addr: Optional[Tuple[str, int]] = ...,
        *,
        family: int = ...,
        proto: int = ...,
        flags: int = ...,
        reuse_address: Optional[bool] = ...,
        reuse_port: Optional[bool] = ...,
        allow_broadcast: Optional[bool] = ...,
        sock: Optional[socket] = ...,
    ) -> tuple[asyncio.BaseProtocol, _ProtocolT]: ...
    async def shutdown_asyncgens(self) -> None: ...
    async def shutdown_default_executor(
        self,
        timeout: Optional[float] = ...,
    ) -> None: ...
    # Loop doesn't implement these, but since they are marked as abstract in typeshed,
    # we have to put them in so mypy thinks the base methods are overridden
    async def sendfile(
        self,
        transport: asyncio.BaseTransport,
        file: IO[bytes],
        offset: int = ...,
        count: Optional[int] = ...,
        *,
        fallback: bool = ...,
    ) -> int: ...
    async def sock_sendfile(
        self,
        sock: socket,
        file: IO[bytes],
        offset: int = ...,
        count: Optional[int] = ...,
        *,
        fallback: bool = ...
    ) -> int: ...
```

## File: `uvloop/loop.pyx`
```
# cython: language_level=3, embedsignature=True, freethreading_compatible=True

import asyncio
cimport cython

from .includes.debug cimport UVLOOP_DEBUG
from .includes cimport uv
from .includes cimport system
from .includes.python cimport (
    PY_VERSION_HEX,
    PyMem_RawMalloc, PyMem_RawFree,
    PyMem_RawCalloc, PyMem_RawRealloc,
    PyUnicode_EncodeFSDefault,
    PyErr_SetInterrupt,
    _Py_RestoreSignals,
    Context_CopyCurrent,
    Context_Enter,
    Context_Exit,
    PyMemoryView_FromMemory, PyBUF_WRITE,
    PyMemoryView_FromObject, PyMemoryView_Check,
    PyOS_AfterFork_Parent, PyOS_AfterFork_Child,
    PyOS_BeforeFork,
    PyUnicode_FromString
)
from .includes.flowcontrol cimport add_flowcontrol_defaults

from libc.stdint cimport uint64_t
from libc.string cimport memset, strerror, memcpy
from libc cimport errno

from cpython cimport PyObject
from cpython cimport PyErr_CheckSignals, PyErr_Occurred
from cpython cimport PyThread_get_thread_ident
from cpython cimport Py_INCREF, Py_DECREF, Py_XDECREF, Py_XINCREF
from cpython cimport (
    PyObject_GetBuffer, PyBuffer_Release, PyBUF_SIMPLE,
    Py_buffer, PyBytes_AsString, PyBytes_CheckExact,
    PyBytes_AsStringAndSize,
    Py_SIZE, PyBytes_AS_STRING, PyBUF_WRITABLE
)
from cpython.pycapsule cimport PyCapsule_New, PyCapsule_GetPointer

from . import _noop


include "includes/stdlib.pxi"

include "errors.pyx"

cdef:
    int PY39 = PY_VERSION_HEX >= 0x03090000
    int PY311 = PY_VERSION_HEX >= 0x030b0000
    int PY313 = PY_VERSION_HEX >= 0x030d0000
    uint64_t MAX_SLEEP = 3600 * 24 * 365 * 100


cdef _is_sock_stream(sock_type):
    if SOCK_NONBLOCK == -1:
        return sock_type == uv.SOCK_STREAM
    else:
        # Linux's socket.type is a bitmask that can include extra info
        # about socket (like SOCK_NONBLOCK bit), therefore we can't do simple
        # `sock_type == socket.SOCK_STREAM`, see
        # https://github.com/torvalds/linux/blob/v4.13/include/linux/net.h#L77
        # for more details.
        return (sock_type & 0xF) == uv.SOCK_STREAM


cdef _is_sock_dgram(sock_type):
    if SOCK_NONBLOCK == -1:
        return sock_type == uv.SOCK_DGRAM
    else:
        # Read the comment in `_is_sock_stream`.
        return (sock_type & 0xF) == uv.SOCK_DGRAM


cdef isfuture(obj):
    if aio_isfuture is None:
        return isinstance(obj, aio_Future)
    else:
        return aio_isfuture(obj)


cdef inline socket_inc_io_ref(sock):
    if isinstance(sock, socket_socket):
        sock._io_refs += 1


cdef inline socket_dec_io_ref(sock):
    if isinstance(sock, socket_socket):
        sock._decref_socketios()


cdef inline run_in_context(context, method):
    Context_Enter(context)
    try:
        return method()
    finally:
        Context_Exit(context)


cdef inline run_in_context1(context, method, arg):
    Context_Enter(context)
    try:
        return method(arg)
    finally:
        Context_Exit(context)


cdef inline run_in_context2(context, method, arg1, arg2):
    Context_Enter(context)
    try:
        return method(arg1, arg2)
    finally:
        Context_Exit(context)


# Used for deprecation and removal of `loop.create_datagram_endpoint()`'s
# *reuse_address* parameter
_unset = object()


@cython.no_gc_clear
cdef class Loop:
    def __cinit__(self):
        cdef int err

        # Install PyMem* memory allocators if they aren't installed yet.
        __install_pymem()

        # Install pthread_atfork handlers
        __install_atfork()

        self.uvloop = <uv.uv_loop_t*>PyMem_RawMalloc(sizeof(uv.uv_loop_t))
        if self.uvloop is NULL:
            raise MemoryError()

        self.slow_callback_duration = 0.1

        self._closed = 0
        self._debug = 0
        self._thread_id = 0
        self._running = 0
        self._stopping = 0

        self._transports = weakref_WeakValueDictionary()
        self._processes = set()

        # Used to keep a reference (and hence keep the fileobj alive)
        # for as long as its registered by add_reader or add_writer.
        # This is how the selector module and hence asyncio behaves.
        self._fd_to_reader_fileobj = {}
        self._fd_to_writer_fileobj = {}

        self._unix_server_sockets = {}

        self._timers = set()
        self._polls = {}

        self._recv_buffer_in_use = 0

        err = uv.uv_loop_init(self.uvloop)
        if err < 0:
            raise convert_error(err)
        self.uvloop.data = <void*> self

        self._init_debug_fields()

        self.active_process_handler = None

        self._last_error = None

        self._task_factory = None
        self._exception_handler = None
        self._default_executor = None

        self._queued_streams = set()
        self._executing_streams = set()
        self._ready = col_deque()

        self.handler_async = UVAsync.new(
            self, <method_t>self._on_wake, self)

        self.handler_idle = UVIdle.new(
            self,
            new_MethodHandle(
                self, "loop._on_idle", <method_t>self._on_idle, None, self))

        # Needed to call `UVStream._exec_write` for writes scheduled
        # during `Protocol.data_received`.
        self.handler_check__exec_writes = UVCheck.new(
            self,
            new_MethodHandle(
                self, "loop._exec_queued_writes",
                <method_t>self._exec_queued_writes, None, self))

        self._signals = set()
        self._ssock = self._csock = None
        self._signal_handlers = {}
        self._listening_signals = False
        self._old_signal_wakeup_id = -1

        self._coroutine_debug_set = False

        # A weak set of all asynchronous generators that are
        # being iterated by the loop.
        self._asyncgens = weakref_WeakSet()

        # Set to True when `loop.shutdown_asyncgens` is called.
        self._asyncgens_shutdown_called = False
        # Set to True when `loop.shutdown_default_executor` is called.
        self._executor_shutdown_called = False

        self._servers = set()

    cdef inline _is_main_thread(self):
        cdef uint64_t main_thread_id = system.MAIN_THREAD_ID
        if system.MAIN_THREAD_ID_SET == 0:
            main_thread_id = <uint64_t>threading_main_thread().ident
            system.setMainThreadID(main_thread_id)
        return main_thread_id == PyThread_get_thread_ident()

    def __init__(self):
        self.set_debug(
            sys_dev_mode or (not sys_ignore_environment
                             and bool(os_environ.get('PYTHONASYNCIODEBUG'))))

    def __dealloc__(self):
        if self._running == 1:
            raise RuntimeError('deallocating a running event loop!')
        if self._closed == 0:
            aio_logger.error("deallocating an open event loop")
            return
        PyMem_RawFree(self.uvloop)
        self.uvloop = NULL

    cdef _init_debug_fields(self):
        self._debug_cc = bool(UVLOOP_DEBUG)

        if UVLOOP_DEBUG:
            self._debug_handles_current = col_Counter()
            self._debug_handles_closed = col_Counter()
            self._debug_handles_total = col_Counter()
        else:
            self._debug_handles_current = None
            self._debug_handles_closed = None
            self._debug_handles_total = None

        self._debug_uv_handles_total = 0
        self._debug_uv_handles_freed = 0

        self._debug_stream_read_cb_total = 0
        self._debug_stream_read_eof_total = 0
        self._debug_stream_read_errors_total = 0
        self._debug_stream_read_cb_errors_total = 0
        self._debug_stream_read_eof_cb_errors_total = 0

        self._debug_stream_shutdown_errors_total = 0
        self._debug_stream_listen_errors_total = 0

        self._debug_stream_write_tries = 0
        self._debug_stream_write_errors_total = 0
        self._debug_stream_write_ctx_total = 0
        self._debug_stream_write_ctx_cnt = 0
        self._debug_stream_write_cb_errors_total = 0

        self._debug_cb_handles_total = 0
        self._debug_cb_handles_count = 0

        self._debug_cb_timer_handles_total = 0
        self._debug_cb_timer_handles_count = 0

        self._poll_read_events_total = 0
        self._poll_read_cb_errors_total = 0
        self._poll_write_events_total = 0
        self._poll_write_cb_errors_total = 0

        self._sock_try_write_total = 0

        self._debug_exception_handler_cnt = 0

    cdef _setup_or_resume_signals(self):
        if not self._is_main_thread():
            return

        if self._listening_signals:
            raise RuntimeError('signals handling has been already setup')

        if self._ssock is not None:
            raise RuntimeError('self-pipe exists before loop run')

        # Create a self-pipe and call set_signal_wakeup_fd() with one
        # of its ends.  This is needed so that libuv knows that it needs
        # to wakeup on ^C (no matter if the SIGINT handler is still the
        # standard Python's one or or user set their own.)

        self._ssock, self._csock = socket_socketpair()
        try:
            self._ssock.setblocking(False)
            self._csock.setblocking(False)

            fileno = self._csock.fileno()

            self._old_signal_wakeup_id = _set_signal_wakeup_fd(fileno)
        except Exception:
            # Out of all statements in the try block, only the
            # "_set_signal_wakeup_fd()" call can fail, but it shouldn't,
            # as we ensure that the current thread is the main thread.
            # Still, if something goes horribly wrong we want to clean up
            # the socket pair.
            self._ssock.close()
            self._csock.close()
            self._ssock = None
            self._csock = None
            raise

        self._add_reader(
            self._ssock,
            new_MethodHandle(
                self,
                "Loop._read_from_self",
                <method_t>self._read_from_self,
                None,
                self))

        self._listening_signals = True

    cdef _pause_signals(self):
        if not self._is_main_thread():
            if self._listening_signals:
                raise RuntimeError(
                    'cannot pause signals handling; no longer running in '
                    'the main thread')
            else:
                return

        if not self._listening_signals:
            raise RuntimeError('signals handling has not been setup')

        self._listening_signals = False

        _set_signal_wakeup_fd(self._old_signal_wakeup_id)

        self._remove_reader(self._ssock)
        self._ssock.close()
        self._csock.close()
        self._ssock = None
        self._csock = None

    cdef _shutdown_signals(self):
        if not self._is_main_thread():
            if self._signal_handlers:
                aio_logger.warning(
                    'cannot cleanup signal handlers: closing the event loop '
                    'in a non-main OS thread')
            return

        if self._listening_signals:
            raise RuntimeError(
                'cannot shutdown signals handling as it has not been paused')

        if self._ssock:
            raise RuntimeError(
                'self-pipe was not cleaned up after loop was run')

        for sig in list(self._signal_handlers):
            self.remove_signal_handler(sig)

    def __sighandler(self, signum, frame):
        self._signals.add(signum)

    cdef inline _ceval_process_signals(self):
        # Invoke CPython eval loop to let process signals.
        PyErr_CheckSignals()
        # Calling a pure-Python function will invoke
        # _PyEval_EvalFrameDefault which will process
        # pending signal callbacks.
        _noop.noop()  # Might raise ^C

    cdef _read_from_self(self):
        cdef bytes sigdata
        sigdata = b''
        while True:
            try:
                data = self._ssock.recv(65536)
                if not data:
                    break
                sigdata += data
            except InterruptedError:
                continue
            except BlockingIOError:
                break
        if sigdata:
            self._invoke_signals(sigdata)

    cdef _invoke_signals(self, bytes data):
        cdef set sigs

        self._ceval_process_signals()

        sigs = self._signals.copy()
        self._signals.clear()
        for signum in data:
            if not signum:
                # ignore null bytes written by set_wakeup_fd()
                continue
            sigs.discard(signum)
            self._handle_signal(signum)

        for signum in sigs:
            # Since not all signals are registered by add_signal_handler()
            # (for instance, we use the default SIGINT handler) not all
            # signals will trigger loop.__sighandler() callback.  Therefore
            # we combine two datasources: one is self-pipe, one is data
            # from __sighandler; this ensures that signals shouldn't be
            # lost even if set_wakeup_fd() couldn't write to the self-pipe.
            self._handle_signal(signum)

    cdef _handle_signal(self, sig):
        cdef Handle handle

        try:
            handle = <Handle>(self._signal_handlers[sig])
        except KeyError:
            handle = None

        if handle is None:
            self._ceval_process_signals()
            return

        if handle._cancelled:
            self.remove_signal_handler(sig)  # Remove it properly.
        else:
            self._append_ready_handle(handle)
            self.handler_async.send()

    cdef _on_wake(self):
        if ((len(self._ready) > 0 or self._stopping) and
                not self.handler_idle.running):
            self.handler_idle.start()

    cdef _on_idle(self):
        cdef:
            int i, ntodo
            object popleft = self._ready.popleft
            Handle handler

        ntodo = len(self._ready)
        if self._debug:
            for i from 0 <= i < ntodo:
                handler = <Handle> popleft()
                if handler._cancelled == 0:
                    try:
                        started = time_monotonic()
                        handler._run()
                    except BaseException as ex:
                        self._stop(ex)
                        return
                    else:
                        delta = time_monotonic() - started
                        if delta > self.slow_callback_duration:
                            aio_logger.warning(
                                'Executing %s took %.3f seconds',
                                handler._format_handle(), delta)

        else:
            for i from 0 <= i < ntodo:
                handler = <Handle> popleft()
                if handler._cancelled == 0:
                    try:
                        handler._run()
                    except BaseException as ex:
                        self._stop(ex)
                        return

        if len(self._queued_streams):
            self._exec_queued_writes()

        if len(self._ready) == 0 and self.handler_idle.running:
            self.handler_idle.stop()

        if self._stopping:
            uv.uv_stop(self.uvloop)  # void

    cdef _stop(self, exc):
        if exc is not None:
            self._last_error = exc
        if self._stopping == 1:
            return
        self._stopping = 1
        if not self.handler_idle.running:
            self.handler_idle.start()

    cdef __run(self, uv.uv_run_mode mode):
        # Although every UVHandle holds a reference to the loop,
        # we want to do everything to ensure that the loop will
        # never deallocate during the run -- so we do some
        # manual refs management.
        Py_INCREF(self)
        with nogil:
            err = uv.uv_run(self.uvloop, mode)
        Py_DECREF(self)

        if err < 0:
            raise convert_error(err)

    cdef _run(self, uv.uv_run_mode mode):
        cdef int err

        if self._closed == 1:
            raise RuntimeError('unable to start the loop; it was closed')

        if self._running == 1:
            raise RuntimeError('this event loop is already running.')

        if (aio_get_running_loop is not None and
                aio_get_running_loop() is not None):
            raise RuntimeError(
                'Cannot run the event loop while another loop is running')

        # reset _last_error
        self._last_error = None

        self._thread_id = PyThread_get_thread_ident()
        self._running = 1

        self.handler_check__exec_writes.start()
        self.handler_idle.start()

        self._setup_or_resume_signals()

        if aio_set_running_loop is not None:
            aio_set_running_loop(self)
        try:
            self.__run(mode)
        finally:
            if aio_set_running_loop is not None:
                aio_set_running_loop(None)

            self.handler_check__exec_writes.stop()
            self.handler_idle.stop()

            self._pause_signals()

            self._thread_id = 0
            self._running = 0
            self._stopping = 0

        if self._last_error is not None:
            # The loop was stopped with an error with 'loop._stop(error)' call
            raise self._last_error

    cdef _close(self):
        cdef int err

        if self._running == 1:
            raise RuntimeError("Cannot close a running event loop")

        if self._closed == 1:
            return

        self._closed = 1

        for cb_handle in self._ready:
            cb_handle.cancel()
        self._ready.clear()

        if self._polls:
            for poll_handle in self._polls.values():
                (<UVHandle>poll_handle)._close()

            self._polls.clear()

        if self._timers:
            for timer_cbhandle in tuple(self._timers):
                timer_cbhandle.cancel()

        # Close all remaining handles
        self.handler_async._close()
        self.handler_idle._close()
        self.handler_check__exec_writes._close()
        __close_all_handles(self)
        self._shutdown_signals()
        # During this run there should be no open handles,
        # so it should finish right away
        self.__run(uv.UV_RUN_DEFAULT)

        if self._fd_to_writer_fileobj:
            for fileobj in self._fd_to_writer_fileobj.values():
                socket_dec_io_ref(fileobj)
            self._fd_to_writer_fileobj.clear()

        if self._fd_to_reader_fileobj:
            for fileobj in self._fd_to_reader_fileobj.values():
                socket_dec_io_ref(fileobj)
            self._fd_to_reader_fileobj.clear()

        if self._timers:
            raise RuntimeError(
                f"new timers were queued during loop closing: {self._timers}")

        if self._polls:
            raise RuntimeError(
                f"new poll handles were queued during loop closing: "
                f"{self._polls}")

        if self._ready:
            raise RuntimeError(
                f"new callbacks were queued during loop closing: "
                f"{self._ready}")

        err = uv.uv_loop_close(self.uvloop)
        if err < 0:
            raise convert_error(err)

        self.handler_async = None
        self.handler_idle = None
        self.handler_check__exec_writes = None

        self._executor_shutdown_called = True
        executor = self._default_executor
        if executor is not None:
            self._default_executor = None
            executor.shutdown(wait=False)

    cdef uint64_t _time(self):
        # asyncio doesn't have a time cache, neither should uvloop.
        uv.uv_update_time(self.uvloop)  # void
        return uv.uv_now(self.uvloop)

    cdef inline _queue_write(self, UVStream stream):
        self._queued_streams.add(stream)
        if not self.handler_check__exec_writes.running:
            self.handler_check__exec_writes.start()

    cdef _exec_queued_writes(self):
        if len(self._queued_streams) == 0:
            if self.handler_check__exec_writes.running:
                self.handler_check__exec_writes.stop()
            return

        cdef:
            UVStream stream

        streams = self._queued_streams
        self._queued_streams = self._executing_streams
        self._executing_streams = streams
        try:
            for pystream in streams:
                stream = <UVStream>pystream
                stream._exec_write()
        finally:
            streams.clear()

        if self.handler_check__exec_writes.running:
            if len(self._queued_streams) == 0:
                self.handler_check__exec_writes.stop()

    cdef inline _call_soon(self, object callback, object args, object context):
        cdef Handle handle
        handle = new_Handle(self, callback, args, context)
        self._call_soon_handle(handle)
        return handle

    cdef inline _append_ready_handle(self, Handle handle):
        self._check_closed()
        self._ready.append(handle)

    cdef inline _call_soon_handle(self, Handle handle):
        self._append_ready_handle(handle)
        if not self.handler_idle.running:
            self.handler_idle.start()

    cdef _call_later(self, uint64_t delay, object callback, object args,
                     object context):
        return TimerHandle(self, callback, args, delay, context)

    cdef void _handle_exception(self, object ex):
        if isinstance(ex, Exception):
            self.call_exception_handler({'exception': ex})
        else:
            # BaseException
            self._last_error = ex
            # Exit ASAP
            self._stop(None)

    cdef inline _check_signal(self, sig):
        if not isinstance(sig, int):
            raise TypeError('sig must be an int, not {!r}'.format(sig))

        if not (1 <= sig < signal_NSIG):
            raise ValueError(
                'sig {} out of range(1, {})'.format(sig, signal_NSIG))

    cdef inline _check_closed(self):
        if self._closed == 1:
            raise RuntimeError('Event loop is closed')

    cdef inline _check_thread(self):
        if self._thread_id == 0:
            return

        cdef uint64_t thread_id
        thread_id = <uint64_t>PyThread_get_thread_ident()

        if thread_id != self._thread_id:
            raise RuntimeError(
                "Non-thread-safe operation invoked on an event loop other "
                "than the current one")

    cdef inline _new_future(self):
        return aio_Future(loop=self)

    cdef _track_transport(self, UVBaseTransport transport):
        self._transports[transport._fileno()] = transport

    cdef _track_process(self, UVProcess proc):
        self._processes.add(proc)

    cdef _untrack_process(self, UVProcess proc):
        self._processes.discard(proc)

    cdef _fileobj_to_fd(self, fileobj):
        """Return a file descriptor from a file object.

        Parameters:
        fileobj -- file object or file descriptor

        Returns:
        corresponding file descriptor

        Raises:
        ValueError if the object is invalid
        """
        # Copy of the `selectors._fileobj_to_fd()` function.
        if isinstance(fileobj, int):
            fd = fileobj
        else:
            try:
                fd = int(fileobj.fileno())
            except (AttributeError, TypeError, ValueError):
                raise ValueError("Invalid file object: "
                                 "{!r}".format(fileobj)) from None
        if fd < 0:
            raise ValueError("Invalid file descriptor: {}".format(fd))
        return fd

    cdef _ensure_fd_no_transport(self, fd):
        cdef UVBaseTransport tr
        try:
            tr = <UVBaseTransport>(self._transports[fd])
        except KeyError:
            pass
        else:
            if tr._is_alive():
                raise RuntimeError(
                    'File descriptor {!r} is used by transport {!r}'.format(
                        fd, tr))

    cdef _add_reader(self, fileobj, Handle handle):
        cdef:
            UVPoll poll

        self._check_closed()
        fd = self._fileobj_to_fd(fileobj)
        self._ensure_fd_no_transport(fd)

        try:
            poll = <UVPoll>(self._polls[fd])
        except KeyError:
            poll = UVPoll.new(self, fd)
            self._polls[fd] = poll

        poll.start_reading(handle)

        old_fileobj = self._fd_to_reader_fileobj.pop(fd, None)
        if old_fileobj is not None:
            socket_dec_io_ref(old_fileobj)

        self._fd_to_reader_fileobj[fd] = fileobj
        socket_inc_io_ref(fileobj)

    cdef _remove_reader(self, fileobj):
        cdef:
            UVPoll poll

        fd = self._fileobj_to_fd(fileobj)
        self._ensure_fd_no_transport(fd)

        mapped_fileobj = self._fd_to_reader_fileobj.pop(fd, None)
        if mapped_fileobj is not None:
            socket_dec_io_ref(mapped_fileobj)

        if self._closed == 1:
            return False

        try:
            poll = <UVPoll>(self._polls[fd])
        except KeyError:
            return False

        result = poll.stop_reading()
        if not poll.is_active():
            del self._polls[fd]
            poll._close()

        return result

    cdef _has_reader(self, fileobj):
        cdef:
            UVPoll poll

        self._check_closed()
        fd = self._fileobj_to_fd(fileobj)

        try:
            poll = <UVPoll>(self._polls[fd])
        except KeyError:
            return False

        return poll.is_reading()

    cdef _add_writer(self, fileobj, Handle handle):
        cdef:
            UVPoll poll

        self._check_closed()
        fd = self._fileobj_to_fd(fileobj)
        self._ensure_fd_no_transport(fd)

        try:
            poll = <UVPoll>(self._polls[fd])
        except KeyError:
            poll = UVPoll.new(self, fd)
            self._polls[fd] = poll

        poll.start_writing(handle)

        old_fileobj = self._fd_to_writer_fileobj.pop(fd, None)
        if old_fileobj is not None:
            socket_dec_io_ref(old_fileobj)

        self._fd_to_writer_fileobj[fd] = fileobj
        socket_inc_io_ref(fileobj)

    cdef _remove_writer(self, fileobj):
        cdef:
            UVPoll poll

        fd = self._fileobj_to_fd(fileobj)
        self._ensure_fd_no_transport(fd)

        mapped_fileobj = self._fd_to_writer_fileobj.pop(fd, None)
        if mapped_fileobj is not None:
            socket_dec_io_ref(mapped_fileobj)

        if self._closed == 1:
            return False

        try:
            poll = <UVPoll>(self._polls[fd])
        except KeyError:
            return False

        result = poll.stop_writing()
        if not poll.is_active():
            del self._polls[fd]
            poll._close()

        return result

    cdef _has_writer(self, fileobj):
        cdef:
            UVPoll poll

        self._check_closed()
        fd = self._fileobj_to_fd(fileobj)

        try:
            poll = <UVPoll>(self._polls[fd])
        except KeyError:
            return False

        return poll.is_writing()

    cdef _getaddrinfo(self, object host, object port,
                      int family, int type,
                      int proto, int flags,
                      int unpack):

        if isinstance(port, str):
            port = port.encode()
        elif isinstance(port, int):
            port = str(port).encode()
        if port is not None and not isinstance(port, bytes):
            raise TypeError('port must be a str, bytes or int')

        if isinstance(host, str):
            host = host.encode('idna')
        if host is not None:
            if not isinstance(host, bytes):
                raise TypeError('host must be a str or bytes')

        fut = self._new_future()

        def callback(result):
            if AddrInfo.isinstance(result):
                try:
                    if unpack == 0:
                        data = result
                    else:
                        data = (<AddrInfo>result).unpack()
                except (KeyboardInterrupt, SystemExit):
                    raise
                except BaseException as ex:
                    if not fut.cancelled():
                        fut.set_exception(ex)
                else:
                    if not fut.cancelled():
                        fut.set_result(data)
            else:
                if not fut.cancelled():
                    fut.set_exception(result)

        AddrInfoRequest(self, host, port, family, type, proto, flags, callback)
        return fut

    cdef _getnameinfo(self, system.sockaddr *addr, int flags):
        cdef NameInfoRequest nr
        fut = self._new_future()

        def callback(result):
            if isinstance(result, tuple):
                fut.set_result(result)
            else:
                fut.set_exception(result)

        nr = NameInfoRequest(self, callback)
        nr.query(addr, flags)
        return fut

    cdef _sock_recv(self, fut, sock, n):
        if UVLOOP_DEBUG:
            if fut.cancelled():
                # Shouldn't happen with _SyncSocketReaderFuture.
                raise RuntimeError(
                    f'_sock_recv is called on a cancelled Future')

            if not self._has_reader(sock):
                raise RuntimeError(
                    f'socket {sock!r} does not have a reader '
                    f'in the _sock_recv callback')

        try:
            data = sock.recv(n)
        except (BlockingIOError, InterruptedError):
            # No need to re-add the reader, let's just wait until
            # the poll handler calls this callback again.
            pass
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as exc:
            fut.set_exception(exc)
            self._remove_reader(sock)
        else:
            fut.set_result(data)
            self._remove_reader(sock)

    cdef _sock_recv_into(self, fut, sock, buf):
        if UVLOOP_DEBUG:
            if fut.cancelled():
                # Shouldn't happen with _SyncSocketReaderFuture.
                raise RuntimeError(
                    f'_sock_recv_into is called on a cancelled Future')

            if not self._has_reader(sock):
                raise RuntimeError(
                    f'socket {sock!r} does not have a reader '
                    f'in the _sock_recv_into callback')

        try:
            data = sock.recv_into(buf)
        except (BlockingIOError, InterruptedError):
            # No need to re-add the reader, let's just wait until
            # the poll handler calls this callback again.
            pass
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as exc:
            fut.set_exception(exc)
            self._remove_reader(sock)
        else:
            fut.set_result(data)
            self._remove_reader(sock)

    cdef _sock_sendall(self, fut, sock, data):
        cdef:
            Handle handle
            int n

        if UVLOOP_DEBUG:
            if fut.cancelled():
                # Shouldn't happen with _SyncSocketWriterFuture.
                raise RuntimeError(
                    f'_sock_sendall is called on a cancelled Future')

            if not self._has_writer(sock):
                raise RuntimeError(
                    f'socket {sock!r} does not have a writer '
                    f'in the _sock_sendall callback')

        try:
            n = sock.send(data)
        except (BlockingIOError, InterruptedError):
            # Try next time.
            return
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as exc:
            fut.set_exception(exc)
            self._remove_writer(sock)
            return

        self._remove_writer(sock)

        if n == len(data):
            fut.set_result(None)
        else:
            if n:
                if not isinstance(data, memoryview):
                    data = memoryview(data)
                data = data[n:]

            handle = new_MethodHandle3(
                self,
                "Loop._sock_sendall",
                <method3_t>self._sock_sendall,
                None,
                self,
                fut, sock, data)

            self._add_writer(sock, handle)

    cdef _sock_accept(self, fut, sock):
        try:
            conn, address = sock.accept()
            conn.setblocking(False)
        except (BlockingIOError, InterruptedError):
            # There is an active reader for _sock_accept, so
            # do nothing, it will be called again.
            pass
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as exc:
            fut.set_exception(exc)
            self._remove_reader(sock)
        else:
            fut.set_result((conn, address))
            self._remove_reader(sock)

    cdef _sock_connect(self, sock, address):
        cdef:
            Handle handle

        try:
            sock.connect(address)
        except (BlockingIOError, InterruptedError):
            pass
        else:
            return

        fut = _SyncSocketWriterFuture(sock, self)
        handle = new_MethodHandle3(
            self,
            "Loop._sock_connect",
            <method3_t>self._sock_connect_cb,
            None,
            self,
            fut, sock, address)

        self._add_writer(sock, handle)
        return fut

    cdef _sock_connect_cb(self, fut, sock, address):
        if UVLOOP_DEBUG:
            if fut.cancelled():
                # Shouldn't happen with _SyncSocketWriterFuture.
                raise RuntimeError(
                    f'_sock_connect_cb is called on a cancelled Future')

            if not self._has_writer(sock):
                raise RuntimeError(
                    f'socket {sock!r} does not have a writer '
                    f'in the _sock_connect_cb callback')

        try:
            err = sock.getsockopt(uv.SOL_SOCKET, uv.SO_ERROR)
            if err != 0:
                # Jump to any except clause below.
                raise OSError(err, 'Connect call failed %s' % (address,))
        except (BlockingIOError, InterruptedError):
            # socket is still registered, the callback will be retried later
            pass
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as exc:
            fut.set_exception(exc)
            self._remove_writer(sock)
        else:
            fut.set_result(None)
            self._remove_writer(sock)

    cdef _sock_set_reuseport(self, int fd):
        cdef:
            int err = 0
            int reuseport_flag = 1

        err = system.setsockopt(
            fd,
            uv.SOL_SOCKET,
            SO_REUSEPORT,
            <char*>&reuseport_flag,
            sizeof(reuseport_flag))

        if err < 0:
            raise convert_error(-errno.errno)

    cdef _set_coroutine_debug(self, bint enabled):
        enabled = bool(enabled)
        if self._coroutine_debug_set == enabled:
            return

        if enabled:
            self._coroutine_origin_tracking_saved_depth = (
                sys.get_coroutine_origin_tracking_depth())
            sys.set_coroutine_origin_tracking_depth(
                DEBUG_STACK_DEPTH)
        else:
            sys.set_coroutine_origin_tracking_depth(
                self._coroutine_origin_tracking_saved_depth)

        self._coroutine_debug_set = enabled

    def _get_backend_id(self):
        """This method is used by uvloop tests and is not part of the API."""
        return uv.uv_backend_fd(self.uvloop)

    cdef _print_debug_info(self):
        cdef:
            int err
            uv.uv_rusage_t rusage

        err = uv.uv_getrusage(&rusage)
        if err < 0:
            raise convert_error(err)

        # OS

        print('---- Process info: -----')
        print('Process memory:            {}'.format(rusage.ru_maxrss))
        print('Number of signals:         {}'.format(rusage.ru_nsignals))
        print('')

        # Loop

        print('--- Loop debug info: ---')
        print('Loop time:                 {}'.format(self.time()))
        print('Errors logged:             {}'.format(
            self._debug_exception_handler_cnt))
        print()
        print('Callback handles:          {: <8} | {}'.format(
            self._debug_cb_handles_count,
            self._debug_cb_handles_total))
        print('Timer handles:             {: <8} | {}'.format(
            self._debug_cb_timer_handles_count,
            self._debug_cb_timer_handles_total))
        print()

        print('                        alive  | closed  |')
        print('UVHandles               python | libuv   | total')
        print('                        objs   | handles |')
        print('-------------------------------+---------+---------')
        for name in sorted(self._debug_handles_total):
            print('    {: <18} {: >7} | {: >7} | {: >7}'.format(
                name,
                self._debug_handles_current[name],
                self._debug_handles_closed[name],
                self._debug_handles_total[name]))
        print()

        print('uv_handle_t (current: {}; freed: {}; total: {})'.format(
            self._debug_uv_handles_total - self._debug_uv_handles_freed,
            self._debug_uv_handles_freed,
            self._debug_uv_handles_total))
        print()

        print('--- Streams debug info: ---')
        print('Write errors:              {}'.format(
            self._debug_stream_write_errors_total))
        print('Write without poll:        {}'.format(
            self._debug_stream_write_tries))
        print('Write contexts:            {: <8} | {}'.format(
            self._debug_stream_write_ctx_cnt,
            self._debug_stream_write_ctx_total))
        print('Write failed callbacks:    {}'.format(
            self._debug_stream_write_cb_errors_total))
        print()
        print('Read errors:               {}'.format(
            self._debug_stream_read_errors_total))
        print('Read callbacks:            {}'.format(
            self._debug_stream_read_cb_total))
        print('Read failed callbacks:     {}'.format(
            self._debug_stream_read_cb_errors_total))
        print('Read EOFs:                 {}'.format(
            self._debug_stream_read_eof_total))
        print('Read EOF failed callbacks: {}'.format(
            self._debug_stream_read_eof_cb_errors_total))
        print()
        print('Listen errors:             {}'.format(
            self._debug_stream_listen_errors_total))
        print('Shutdown errors            {}'.format(
            self._debug_stream_shutdown_errors_total))
        print()

        print('--- Polls debug info: ---')
        print('Read events:               {}'.format(
            self._poll_read_events_total))
        print('Read callbacks failed:     {}'.format(
            self._poll_read_cb_errors_total))
        print('Write events:              {}'.format(
            self._poll_write_events_total))
        print('Write callbacks failed:    {}'.format(
            self._poll_write_cb_errors_total))
        print()

        print('--- Sock ops successful on 1st try: ---')
        print('Socket try-writes:         {}'.format(
            self._sock_try_write_total))

        print(flush=True)

    property print_debug_info:
        def __get__(self):
            if UVLOOP_DEBUG:
                return lambda: self._print_debug_info()
            else:
                raise AttributeError('print_debug_info')

    # Public API

    def __repr__(self):
        return '<{}.{} running={} closed={} debug={}>'.format(
            self.__class__.__module__,
            self.__class__.__name__,
            self.is_running(),
            self.is_closed(),
            self.get_debug()
        )

    def call_soon(self, callback, *args, context=None):
        """Arrange for a callback to be called as soon as possible.

        This operates as a FIFO queue: callbacks are called in the
        order in which they are registered.  Each callback will be
        called exactly once.

        Any positional arguments after the callback will be passed to
        the callback when it is called.
        """
        if self._debug == 1:
            self._check_thread()
        if args:
            return self._call_soon(callback, args, context)
        else:
            return self._call_soon(callback, None, context)

    def call_soon_threadsafe(self, callback, *args, context=None):
        """Like call_soon(), but thread-safe."""
        if not args:
            args = None
        cdef Handle handle = new_Handle(self, callback, args, context)
        self._append_ready_handle(handle)  # deque append is atomic
        # libuv async handler is thread-safe while the idle handler is not -
        # we only set the async handler here, which will start the idle handler
        # in _on_wake() from the loop and eventually call the callback.
        self.handler_async.send()
        return handle

    def call_later(self, delay, callback, *args, context=None):
        """Arrange for a callback to be called at a given time.

        Return a Handle: an opaque object with a cancel() method that
        can be used to cancel the call.

        The delay can be an int or float, expressed in seconds.  It is
        always relative to the current time.

        Each callback will be called exactly once.  If two callbacks
        are scheduled for exactly the same time, it undefined which
        will be called first.

        Any positional arguments after the callback will be passed to
        the callback when it is called.
        """
        cdef uint64_t when

        self._check_closed()
        if self._debug == 1:
            self._check_thread()

        if delay < 0:
            delay = 0
        elif delay == py_inf or delay > MAX_SLEEP:
            # ~100 years sounds like a good approximation of
            # infinity for a Python application.
            delay = MAX_SLEEP

        when = <uint64_t>round(delay * 1000)
        if not args:
            args = None
        if when == 0:
            return self._call_soon(callback, args, context)
        else:
            return self._call_later(when, callback, args, context)

    def call_at(self, when, callback, *args, context=None):
        """Like call_later(), but uses an absolute time.

        Absolute time corresponds to the event loop's time() method.
        """
        return self.call_later(
            when - self.time(), callback, *args, context=context)

    def time(self):
        """Return the time according to the event loop's clock.

        This is a float expressed in seconds since an epoch, but the
        epoch, precision, accuracy and drift are unspecified and may
        differ per event loop.
        """
        return self._time() / 1000

    def stop(self):
        """Stop running the event loop.

        Every callback already scheduled will still run.  This simply informs
        run_forever to stop looping after a complete iteration.
        """
        self._call_soon_handle(
            new_MethodHandle1(
                self,
                "Loop._stop",
                <method1_t>self._stop,
                None,
                self,
                None))

    def run_forever(self):
        """Run the event loop until stop() is called."""
        self._check_closed()
        mode = uv.UV_RUN_DEFAULT
        if self._stopping:
            # loop.stop() was called right before loop.run_forever().
            # This is how asyncio loop behaves.
            mode = uv.UV_RUN_NOWAIT
        self._set_coroutine_debug(self._debug)
        old_agen_hooks = sys.get_asyncgen_hooks()
        sys.set_asyncgen_hooks(firstiter=self._asyncgen_firstiter_hook,
                               finalizer=self._asyncgen_finalizer_hook)
        try:
            self._run(mode)
        finally:
            self._set_coroutine_debug(False)
            sys.set_asyncgen_hooks(*old_agen_hooks)

    def close(self):
        """Close the event loop.

        The event loop must not be running.

        This is idempotent and irreversible.

        No other methods should be called after this one.
        """
        self._close()

    def get_debug(self):
        return bool(self._debug)

    def set_debug(self, enabled):
        self._debug = bool(enabled)
        if self.is_running():
             self.call_soon_threadsafe(self._set_coroutine_debug, self._debug)

    def is_running(self):
        """Return whether the event loop is currently running."""
        return bool(self._running)

    def is_closed(self):
        """Returns True if the event loop was closed."""
        return bool(self._closed)

    def create_future(self):
        """Create a Future object attached to the loop."""
        return self._new_future()

    def create_task(self, coro, *, name=None, context=None):
        """Schedule a coroutine object.

        Return a task object.

        If name is not None, task.set_name(name) will be called if the task
        object has the set_name attribute, true for default Task in CPython.

        An optional keyword-only context argument allows specifying a custom
        contextvars.Context for the coro to run in. The current context copy is
        created when no context is provided.
        """
        self._check_closed()
        if PY311:
            if self._task_factory is None:
                task = aio_Task(coro, loop=self, context=context)
            else:
                task = self._task_factory(self, coro, context=context)
        else:
            if context is None:
                if self._task_factory is None:
                    task = aio_Task(coro, loop=self)
                else:
                    task = self._task_factory(self, coro)
            else:
                if self._task_factory is None:
                    task = context.run(aio_Task, coro, self)
                else:
                    task = context.run(self._task_factory, self, coro)

        # copied from asyncio.tasks._set_task_name (bpo-34270)
        if name is not None:
            try:
                set_name = task.set_name
            except AttributeError:
                pass
            else:
                set_name(name)

        return task

    def set_task_factory(self, factory):
        """Set a task factory that will be used by loop.create_task().

        If factory is None the default task factory will be set.

        If factory is a callable, it should have a signature matching
        '(loop, coro)', where 'loop' will be a reference to the active
        event loop, 'coro' will be a coroutine object.  The callable
        must return a Future.
        """
        if factory is not None and not callable(factory):
            raise TypeError('task factory must be a callable or None')
        self._task_factory = factory

    def get_task_factory(self):
        """Return a task factory, or None if the default one is in use."""
        return self._task_factory

    def run_until_complete(self, future):
        """Run until the Future is done.

        If the argument is a coroutine, it is wrapped in a Task.

        WARNING: It would be disastrous to call run_until_complete()
        with the same coroutine twice -- it would wrap it in two
        different Tasks and that can't be good.

        Return the Future's result, or raise its exception.
        """
        self._check_closed()

        new_task = not isfuture(future)
        future = aio_ensure_future(future, loop=self)
        if new_task:
            # An exception is raised if the future didn't complete, so there
            # is no need to log the "destroy pending task" message
            future._log_destroy_pending = False

        def done_cb(fut):
            if not fut.cancelled():
                exc = fut.exception()
                if isinstance(exc, (SystemExit, KeyboardInterrupt)):
                    # Issue #336: run_forever() already finished,
                    # no need to stop it.
                    return
            self.stop()

        future.add_done_callback(done_cb)
        try:
            self.run_forever()
        except BaseException:
            if new_task and future.done() and not future.cancelled():
                # The coroutine raised a BaseException. Consume the exception
                # to not log a warning, the caller doesn't have access to the
                # local task.
                future.exception()
            raise
        finally:
            future.remove_done_callback(done_cb)
        if not future.done():
            raise RuntimeError('Event loop stopped before Future completed.')

        return future.result()

    @cython.iterable_coroutine
    async def getaddrinfo(self, object host, object port, *,
                          int family=0, int type=0, int proto=0, int flags=0):

        addr = __static_getaddrinfo_pyaddr(host, port, family,
                                           type, proto, flags)
        if addr is not None:
            return [addr]

        return await self._getaddrinfo(
            host, port, family, type, proto, flags, 1)

    @cython.iterable_coroutine
    async def getnameinfo(self, sockaddr, int flags=0):
        cdef:
            AddrInfo ai_cnt
            system.addrinfo *ai
            system.sockaddr_in6 *sin6

        if not isinstance(sockaddr, tuple):
            raise TypeError('getnameinfo() argument 1 must be a tuple')

        sl = len(sockaddr)

        if sl < 2 or sl > 4:
            raise ValueError('sockaddr must be a tuple of 2, 3 or 4 values')

        if sl > 2:
            flowinfo = sockaddr[2]
            if flowinfo < 0 or flowinfo > 0xfffff:
                raise OverflowError(
                    'getnameinfo(): flowinfo must be 0-1048575.')
        else:
            flowinfo = 0

        if sl > 3:
            scope_id = sockaddr[3]
            if scope_id < 0 or scope_id > 2 ** 32:
                raise OverflowError(
                    'getsockaddrarg: scope_id must be unsigned 32 bit integer')
        else:
            scope_id = 0

        ai_cnt = await self._getaddrinfo(
            sockaddr[0], sockaddr[1],
            uv.AF_UNSPEC,         # family
            uv.SOCK_DGRAM,        # type
            0,                    # proto
            uv.AI_NUMERICHOST,    # flags
            0)                    # unpack

        ai = ai_cnt.data

        if ai.ai_next:
            raise OSError("sockaddr resolved to multiple addresses")

        if ai.ai_family == uv.AF_INET:
            if sl > 2:
                raise OSError("IPv4 sockaddr must be 2 tuple")
        elif ai.ai_family == uv.AF_INET6:
            # Modify some fields in `ai`
            sin6 = <system.sockaddr_in6*> ai.ai_addr
            sin6.sin6_flowinfo = system.htonl(flowinfo)
            sin6.sin6_scope_id = scope_id

        return await self._getnameinfo(ai.ai_addr, flags)

    @cython.iterable_coroutine
    async def start_tls(self, transport, protocol, sslcontext, *,
                        server_side=False,
                        server_hostname=None,
                        ssl_handshake_timeout=None,
                        ssl_shutdown_timeout=None):
        """Upgrade transport to TLS.

        Return a new transport that *protocol* should start using
        immediately.
        """
        if not isinstance(sslcontext, ssl_SSLContext):
            raise TypeError(
                f'sslcontext is expected to be an instance of ssl.SSLContext, '
                f'got {sslcontext!r}')

        if isinstance(transport, (TCPTransport, UnixTransport)):
            context = (<UVStream>transport).context
        elif isinstance(transport, _SSLProtocolTransport):
            context = (<_SSLProtocolTransport>transport).context
        else:
            raise TypeError(
                f'transport {transport!r} is not supported by start_tls()')

        waiter = self._new_future()
        ssl_protocol = SSLProtocol(
            self, protocol, sslcontext, waiter,
            server_side, server_hostname,
            ssl_handshake_timeout=ssl_handshake_timeout,
            ssl_shutdown_timeout=ssl_shutdown_timeout,
            call_connection_made=False)

        # Pause early so that "ssl_protocol.data_received()" doesn't
        # have a chance to get called before "ssl_protocol.connection_made()".
        transport.pause_reading()

        transport.set_protocol(ssl_protocol)
        conmade_cb = self.call_soon(ssl_protocol.connection_made, transport,
                                    context=context)
        # transport.resume_reading() will use the right context
        # (transport.context) to call e.g. data_received()
        resume_cb = self.call_soon(transport.resume_reading)
        app_transport = ssl_protocol._get_app_transport(context)

        try:
            await waiter
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            app_transport.close()
            conmade_cb.cancel()
            resume_cb.cancel()
            raise

        return app_transport

    @cython.iterable_coroutine
    async def create_server(self, protocol_factory, host=None, port=None,
                            *,
                            int family=uv.AF_UNSPEC,
                            int flags=uv.AI_PASSIVE,
                            sock=None,
                            backlog=100,
                            ssl=None,
                            reuse_address=None,
                            reuse_port=None,
                            ssl_handshake_timeout=None,
                            ssl_shutdown_timeout=None,
                            start_serving=True):
        """A coroutine which creates a TCP server bound to host and port.

        The return value is a Server object which can be used to stop
        the service.

        If host is an empty string or None all interfaces are assumed
        and a list of multiple sockets will be returned (most likely
        one for IPv4 and another one for IPv6). The host parameter can also be
        a sequence (e.g. list) of hosts to bind to.

        family can be set to either AF_INET or AF_INET6 to force the
        socket to use IPv4 or IPv6. If not set it will be determined
        from host (defaults to AF_UNSPEC).

        flags is a bitmask for getaddrinfo().

        sock can optionally be specified in order to use a preexisting
        socket object.

        backlog is the maximum number of queued connections passed to
        listen() (defaults to 100).

        ssl can be set to an SSLContext to enable SSL over the
        accepted connections.

        reuse_address tells the kernel to reuse a local socket in
        TIME_WAIT state, without waiting for its natural timeout to
        expire. If not specified will automatically be set to True on
        UNIX.

        reuse_port tells the kernel to allow this endpoint to be bound to
        the same port as other existing endpoints are bound to, so long as
        they all set this flag when being created. This option is not
        supported on Windows.

        ssl_handshake_timeout is the time in seconds that an SSL server
        will wait for completion of the SSL handshake before aborting the
        connection. Default is 60s.

        ssl_shutdown_timeout is the time in seconds that an SSL server
        will wait for completion of the SSL shutdown before aborting the
        connection. Default is 30s.
        """
        cdef:
            TCPServer tcp
            system.addrinfo *addrinfo
            Server server

        if sock is not None and sock.family == uv.AF_UNIX:
            if host is not None or port is not None:
                raise ValueError(
                    'host/port and sock can not be specified at the same time')
            return await self.create_unix_server(
                protocol_factory, sock=sock, backlog=backlog, ssl=ssl,
                start_serving=start_serving,
                # asyncio won't clean up socket file using create_server() API
                cleanup_socket=False,
            )

        server = Server(self)

        if ssl is not None:
            if not isinstance(ssl, ssl_SSLContext):
                raise TypeError('ssl argument must be an SSLContext or None')
        else:
            if ssl_handshake_timeout is not None:
                raise ValueError(
                    'ssl_handshake_timeout is only meaningful with ssl')
            if ssl_shutdown_timeout is not None:
                raise ValueError(
                    'ssl_shutdown_timeout is only meaningful with ssl')

        if host is not None or port is not None:
            if sock is not None:
                raise ValueError(
                    'host/port and sock can not be specified at the same time')

            if reuse_address is None:
                reuse_address = os_name == 'posix' and sys_platform != 'cygwin'
            reuse_port = bool(reuse_port)
            if reuse_port and not has_SO_REUSEPORT:
                raise ValueError(
                    'reuse_port not supported by socket module')

            if host == '':
                hosts = [None]
            elif (isinstance(host, str) or not isinstance(host, col_Iterable)):
                hosts = [host]
            else:
                hosts = host

            fs = [self._getaddrinfo(host, port, family,
                                    uv.SOCK_STREAM, 0, flags,
                                    0) for host in hosts]

            infos = await aio_gather(*fs)

            completed = False
            sock = None
            try:
                for info in infos:
                    addrinfo = (<AddrInfo>info).data
                    while addrinfo != NULL:
                        if addrinfo.ai_family == uv.AF_UNSPEC:
                            raise RuntimeError('AF_UNSPEC in DNS results')

                        try:
                            sock = socket_socket(addrinfo.ai_family,
                                                 addrinfo.ai_socktype,
                                                 addrinfo.ai_protocol)
                        except socket_error:
                            # Assume it's a bad family/type/protocol
                            # combination.
                            if self._debug:
                                aio_logger.warning(
                                    'create_server() failed to create '
                                    'socket.socket(%r, %r, %r)',
                                    addrinfo.ai_family,
                                    addrinfo.ai_socktype,
                                    addrinfo.ai_protocol, exc_info=True)
                            addrinfo = addrinfo.ai_next
                            continue

                        if reuse_address:
                            sock.setsockopt(uv.SOL_SOCKET, uv.SO_REUSEADDR, 1)
                        if reuse_port:
                            sock.setsockopt(uv.SOL_SOCKET, SO_REUSEPORT, 1)
                        # Disable IPv4/IPv6 dual stack support (enabled by
                        # default on Linux) which makes a single socket
                        # listen on both address families.
                        if (addrinfo.ai_family == uv.AF_INET6 and
                                has_IPV6_V6ONLY):
                            sock.setsockopt(uv.IPPROTO_IPV6, IPV6_V6ONLY, 1)

                        pyaddr = __convert_sockaddr_to_pyaddr(addrinfo.ai_addr)
                        try:
                            sock.bind(pyaddr)
                        except OSError as err:
                            raise OSError(
                                err.errno, 'error while attempting '
                                'to bind on address %r: %s'
                                % (pyaddr, err.strerror.lower())) from None

                        tcp = TCPServer.new(self, protocol_factory, server,
                                            uv.AF_UNSPEC, backlog,
                                            ssl, ssl_handshake_timeout,
                                            ssl_shutdown_timeout)

                        try:
                            tcp._open(sock.fileno())
                        except (KeyboardInterrupt, SystemExit):
                            raise
                        except BaseException:
                            tcp._close()
                            raise

                        server._add_server(tcp)
                        sock.detach()
                        sock = None

                        addrinfo = addrinfo.ai_next

                completed = True
            finally:
                if not completed:
                    if sock is not None:
                        sock.close()
                    server.close()
        else:
            if sock is None:
                raise ValueError('Neither host/port nor sock were specified')
            if not _is_sock_stream(sock.type):
                raise ValueError(
                    'A Stream Socket was expected, got {!r}'.format(sock))

            # libuv will set the socket to non-blocking mode, but
            # we want Python socket object to notice that.
            sock.setblocking(False)

            tcp = TCPServer.new(self, protocol_factory, server,
                                uv.AF_UNSPEC, backlog,
                                ssl, ssl_handshake_timeout,
                                ssl_shutdown_timeout)

            try:
                tcp._open(sock.fileno())
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                tcp._close()
                raise

            tcp._attach_fileobj(sock)
            server._add_server(tcp)

        if start_serving:
            server._start_serving()

        server._ref()
        return server

    @cython.iterable_coroutine
    async def create_connection(self, protocol_factory, host=None, port=None,
                                *,
                                ssl=None,
                                family=0, proto=0, flags=0, sock=None,
                                local_addr=None, server_hostname=None,
                                ssl_handshake_timeout=None,
                                ssl_shutdown_timeout=None):
        """Connect to a TCP server.

        Create a streaming transport connection to a given Internet host and
        port: socket family AF_INET or socket.AF_INET6 depending on host (or
        family if specified), socket type SOCK_STREAM. protocol_factory must be
        a callable returning a protocol instance.

        This method is a coroutine which will try to establish the connection
        in the background.  When successful, the coroutine returns a
        (transport, protocol) pair.
        """
        cdef:
            AddrInfo ai_local = None
            AddrInfo ai_remote
            TCPTransport tr

            system.addrinfo *rai = NULL
            system.addrinfo *lai = NULL

            system.addrinfo *rai_iter = NULL
            system.addrinfo *lai_iter = NULL

            system.addrinfo rai_static
            system.sockaddr_storage rai_addr_static
            system.addrinfo lai_static
            system.sockaddr_storage lai_addr_static

            object app_protocol
            object app_transport
            object protocol
            object ssl_waiter

        if sock is not None and sock.family == uv.AF_UNIX:
            if host is not None or port is not None:
                raise ValueError(
                    'host/port and sock can not be specified at the same time')
            return await self.create_unix_connection(
                protocol_factory, None,
                sock=sock, ssl=ssl, server_hostname=server_hostname)

        app_protocol = protocol = protocol_factory()
        ssl_waiter = None
        context = Context_CopyCurrent()
        if ssl:
            if server_hostname is None:
                if not host:
                    raise ValueError('You must set server_hostname '
                                     'when using ssl without a host')
                server_hostname = host

            ssl_waiter = self._new_future()
            sslcontext = None if isinstance(ssl, bool) else ssl
            protocol = SSLProtocol(
                self, app_protocol, sslcontext, ssl_waiter,
                False, server_hostname,
                ssl_handshake_timeout=ssl_handshake_timeout,
                ssl_shutdown_timeout=ssl_shutdown_timeout)
        else:
            if server_hostname is not None:
                raise ValueError('server_hostname is only meaningful with ssl')
            if ssl_handshake_timeout is not None:
                raise ValueError(
                    'ssl_handshake_timeout is only meaningful with ssl')
            if ssl_shutdown_timeout is not None:
                raise ValueError(
                    'ssl_shutdown_timeout is only meaningful with ssl')

        if host is not None or port is not None:
            if sock is not None:
                raise ValueError(
                    'host/port and sock can not be specified at the same time')

            fs = []
            f1 = f2 = None

            addr = __static_getaddrinfo(
                host, port, family, uv.SOCK_STREAM,
                proto, <system.sockaddr*>&rai_addr_static)

            if addr is None:
                f1 = self._getaddrinfo(
                    host, port, family,
                    uv.SOCK_STREAM, proto, flags,
                    0)  # 0 == don't unpack

                fs.append(f1)
            else:
                rai_static.ai_addr = <system.sockaddr*>&rai_addr_static
                rai_static.ai_next = NULL
                rai = &rai_static

            if local_addr is not None:
                if not isinstance(local_addr, (tuple, list)) or \
                        len(local_addr) != 2:
                    raise ValueError(
                        'local_addr must be a tuple of host and port')

                addr = __static_getaddrinfo(
                    local_addr[0], local_addr[1],
                    family, uv.SOCK_STREAM,
                    proto, <system.sockaddr*>&lai_addr_static)
                if addr is None:
                    f2 = self._getaddrinfo(
                        local_addr[0], local_addr[1], family,
                        uv.SOCK_STREAM, proto, flags,
                        0)  # 0 == don't unpack

                    fs.append(f2)
                else:
                    lai_static.ai_addr = <system.sockaddr*>&lai_addr_static
                    lai_static.ai_next = NULL
                    lai = &lai_static

            if len(fs):
                await aio_wait(fs)

            if rai is NULL:
                ai_remote = f1.result()
                if ai_remote.data is NULL:
                    raise OSError('getaddrinfo() returned empty list')
                rai = ai_remote.data

            if lai is NULL and f2 is not None:
                ai_local = f2.result()
                if ai_local.data is NULL:
                    raise OSError(
                        'getaddrinfo() returned empty list for local_addr')
                lai = ai_local.data

            exceptions = []
            rai_iter = rai
            while rai_iter is not NULL:
                tr = None
                try:
                    waiter = self._new_future()
                    tr = TCPTransport.new(self, protocol, None, waiter,
                                          context)

                    if lai is not NULL:
                        lai_iter = lai
                        while lai_iter is not NULL:
                            try:
                                tr.bind(lai_iter.ai_addr)
                                break
                            except OSError as exc:
                                exceptions.append(exc)
                            lai_iter = lai_iter.ai_next
                        else:
                            tr._close()
                            tr = None

                            rai_iter = rai_iter.ai_next
                            continue

                    tr.connect(rai_iter.ai_addr)
                    await waiter

                except OSError as exc:
                    if tr is not None:
                        tr._close()
                        tr = None
                    exceptions.append(exc)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except BaseException:
                    if tr is not None:
                        tr._close()
                        tr = None
                    raise
                else:
                    break

                rai_iter = rai_iter.ai_next

            else:
                # If they all have the same str(), raise one.
                model = str(exceptions[0])
                if all(str(exc) == model for exc in exceptions):
                    raise exceptions[0]
                # Raise a combined exception so the user can see all
                # the various error messages.
                raise OSError('Multiple exceptions: {}'.format(
                    ', '.join(str(exc) for exc in exceptions)))
        else:
            if sock is None:
                raise ValueError(
                    'host and port was not specified and no sock specified')
            if not _is_sock_stream(sock.type):
                raise ValueError(
                    'A Stream Socket was expected, got {!r}'.format(sock))

            # libuv will set the socket to non-blocking mode, but
            # we want Python socket object to notice that.
            sock.setblocking(False)

            waiter = self._new_future()
            tr = TCPTransport.new(self, protocol, None, waiter, context)
            try:
                # libuv will make socket non-blocking
                tr._open(sock.fileno())
                tr._init_protocol()
                await waiter
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                # It's OK to call `_close()` here, as opposed to
                # `_force_close()` or `close()` as we want to terminate the
                # transport immediately.  The `waiter` can only be waken
                # up in `Transport._call_connection_made()`, and calling
                # `_close()` before it is fine.
                tr._close()
                raise

            tr._attach_fileobj(sock)

        if ssl:
            app_transport = protocol._get_app_transport(context)
            try:
                await ssl_waiter
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                app_transport.close()
                raise
            return app_transport, app_protocol
        else:
            return tr, protocol

    @cython.iterable_coroutine
    async def create_unix_server(self, protocol_factory, path=None,
                                 *, backlog=100, sock=None, ssl=None,
                                 ssl_handshake_timeout=None,
                                 ssl_shutdown_timeout=None,
                                 start_serving=True, cleanup_socket=PY313):
        """A coroutine which creates a UNIX Domain Socket server.

        The return value is a Server object, which can be used to stop
        the service.

        path is a str, representing a file systsem path to bind the
        server socket to.

        sock can optionally be specified in order to use a preexisting
        socket object.

        backlog is the maximum number of queued connections passed to
        listen() (defaults to 100).

        ssl can be set to an SSLContext to enable SSL over the
        accepted connections.

        ssl_handshake_timeout is the time in seconds that an SSL server
        will wait for completion of the SSL handshake before aborting the
        connection. Default is 60s.

        ssl_shutdown_timeout is the time in seconds that an SSL server
        will wait for completion of the SSL shutdown before aborting the
        connection. Default is 30s.

        If *cleanup_socket* is true then the Unix socket will automatically
        be removed from the filesystem when the server is closed, unless the
        socket has been replaced after the server has been created.
        This defaults to True on Python 3.13 and above, or False otherwise.
        """
        cdef:
            UnixServer pipe
            Server server = Server(self)

        if ssl is not None:
            if not isinstance(ssl, ssl_SSLContext):
                raise TypeError('ssl argument must be an SSLContext or None')
        else:
            if ssl_handshake_timeout is not None:
                raise ValueError(
                    'ssl_handshake_timeout is only meaningful with ssl')
            if ssl_shutdown_timeout is not None:
                raise ValueError(
                    'ssl_shutdown_timeout is only meaningful with ssl')

        if path is not None:
            if sock is not None:
                raise ValueError(
                    'path and sock can not be specified at the same time')
            orig_path = path

            path = os_fspath(path)

            if isinstance(path, str):
                path = PyUnicode_EncodeFSDefault(path)

            # Check for abstract socket.
            if path[0] != 0:
                try:
                    if stat_S_ISSOCK(os_stat(path).st_mode):
                        os_remove(path)
                except FileNotFoundError:
                    pass
                except OSError as err:
                    # Directory may have permissions only to create socket.
                    aio_logger.error(
                        'Unable to check or remove stale UNIX socket %r: %r',
                        orig_path, err)

            # We use Python sockets to create a UNIX server socket because
            # when UNIX sockets are created by libuv, libuv removes the path
            # they were bound to.  This is different from asyncio, which
            # doesn't cleanup the socket path.
            sock = socket_socket(uv.AF_UNIX)

            try:
                sock.bind(path)
            except OSError as exc:
                sock.close()
                if exc.errno == errno.EADDRINUSE:
                    # Let's improve the error message by adding
                    # with what exact address it occurs.
                    msg = 'Address {!r} is already in use'.format(orig_path)
                    raise OSError(errno.EADDRINUSE, msg) from None
                else:
                    raise
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                sock.close()
                raise

        else:
            if sock is None:
                raise ValueError(
                    'path was not specified, and no sock specified')

            if sock.family != uv.AF_UNIX or not _is_sock_stream(sock.type):
                raise ValueError(
                    'A UNIX Domain Stream Socket was expected, got {!r}'
                    .format(sock))

            # libuv will set the socket to non-blocking mode, but
            # we want Python socket object to notice that.
            sock.setblocking(False)

        if cleanup_socket:
            path = sock.getsockname()
            # Check for abstract socket. `str` and `bytes` paths are supported.
            if path[0] not in (0, '\x00'):
                try:
                    self._unix_server_sockets[sock] = os_stat(path).st_ino
                except FileNotFoundError:
                    pass

        pipe = UnixServer.new(
            self, protocol_factory, server, backlog,
            ssl, ssl_handshake_timeout, ssl_shutdown_timeout)

        try:
            pipe._open(sock.fileno())
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            pipe._close()
            sock.close()
            raise

        pipe._attach_fileobj(sock)
        server._add_server(pipe)

        if start_serving:
            server._start_serving()

        return server

    @cython.iterable_coroutine
    async def create_unix_connection(self, protocol_factory, path=None, *,
                                     ssl=None, sock=None,
                                     server_hostname=None,
                                     ssl_handshake_timeout=None,
                                     ssl_shutdown_timeout=None):

        cdef:
            UnixTransport tr
            object app_protocol
            object app_transport
            object protocol
            object ssl_waiter

        app_protocol = protocol = protocol_factory()
        ssl_waiter = None
        context = Context_CopyCurrent()
        if ssl:
            if server_hostname is None:
                raise ValueError('You must set server_hostname '
                                 'when using ssl without a host')

            ssl_waiter = self._new_future()
            sslcontext = None if isinstance(ssl, bool) else ssl
            protocol = SSLProtocol(
                self, app_protocol, sslcontext, ssl_waiter,
                False, server_hostname,
                ssl_handshake_timeout=ssl_handshake_timeout,
                ssl_shutdown_timeout=ssl_shutdown_timeout)
        else:
            if server_hostname is not None:
                raise ValueError('server_hostname is only meaningful with ssl')
            if ssl_handshake_timeout is not None:
                raise ValueError(
                    'ssl_handshake_timeout is only meaningful with ssl')
            if ssl_shutdown_timeout is not None:
                raise ValueError(
                    'ssl_shutdown_timeout is only meaningful with ssl')

        if path is not None:
            if sock is not None:
                raise ValueError(
                    'path and sock can not be specified at the same time')

            path = os_fspath(path)

            if isinstance(path, str):
                path = PyUnicode_EncodeFSDefault(path)

            waiter = self._new_future()
            tr = UnixTransport.new(self, protocol, None, waiter, context)
            tr.connect(path)
            try:
                await waiter
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                tr._close()
                raise

        else:
            if sock is None:
                raise ValueError('no path and sock were specified')

            if sock.family != uv.AF_UNIX or not _is_sock_stream(sock.type):
                raise ValueError(
                    'A UNIX Domain Stream Socket was expected, got {!r}'
                    .format(sock))

            # libuv will set the socket to non-blocking mode, but
            # we want Python socket object to notice that.
            sock.setblocking(False)

            waiter = self._new_future()
            tr = UnixTransport.new(self, protocol, None, waiter, context)
            try:
                tr._open(sock.fileno())
                tr._init_protocol()
                await waiter
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                tr._close()
                raise

            tr._attach_fileobj(sock)

        if ssl:
            app_transport = protocol._get_app_transport(Context_CopyCurrent())
            try:
                await ssl_waiter
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                app_transport.close()
                raise
            return app_transport, app_protocol
        else:
            return tr, protocol

    def default_exception_handler(self, context):
        """Default exception handler.

        This is called when an exception occurs and no exception
        handler is set, and can be called by a custom exception
        handler that wants to defer to the default behavior.

        The context parameter has the same meaning as in
        `call_exception_handler()`.
        """
        message = context.get('message')
        if not message:
            message = 'Unhandled exception in event loop'

        exception = context.get('exception')
        if exception is not None:
            exc_info = (type(exception), exception, exception.__traceback__)
        else:
            exc_info = False

        log_lines = [message]
        for key in sorted(context):
            if key in {'message', 'exception'}:
                continue
            value = context[key]
            if key == 'source_traceback':
                tb = ''.join(tb_format_list(value))
                value = 'Object created at (most recent call last):\n'
                value += tb.rstrip()
            else:
                try:
                    value = repr(value)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except BaseException as ex:
                    value = ('Exception in __repr__ {!r}; '
                             'value type: {!r}'.format(ex, type(value)))
            log_lines.append('{}: {}'.format(key, value))

        aio_logger.error('\n'.join(log_lines), exc_info=exc_info)

    def get_exception_handler(self):
        """Return an exception handler, or None if the default one is in use.
        """
        return self._exception_handler

    def set_exception_handler(self, handler):
        """Set handler as the new event loop exception handler.

        If handler is None, the default exception handler will
        be set.

        If handler is a callable object, it should have a
        signature matching '(loop, context)', where 'loop'
        will be a reference to the active event loop, 'context'
        will be a dict object (see `call_exception_handler()`
        documentation for details about context).
        """
        if handler is not None and not callable(handler):
            raise TypeError('A callable object or None is expected, '
                            'got {!r}'.format(handler))
        self._exception_handler = handler

    def call_exception_handler(self, context):
        """Call the current event loop's exception handler.

        The context argument is a dict containing the following keys:

        - 'message': Error message;
        - 'exception' (optional): Exception object;
        - 'future' (optional): Future instance;
        - 'handle' (optional): Handle instance;
        - 'protocol' (optional): Protocol instance;
        - 'transport' (optional): Transport instance;
        - 'socket' (optional): Socket instance.

        New keys maybe introduced in the future.

        Note: do not overload this method in an event loop subclass.
        For custom exception handling, use the
        `set_exception_handler()` method.
        """
        if UVLOOP_DEBUG:
            self._debug_exception_handler_cnt += 1

        if self._exception_handler is None:
            try:
                self.default_exception_handler(context)
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                # Second protection layer for unexpected errors
                # in the default implementation, as well as for subclassed
                # event loops with overloaded "default_exception_handler".
                aio_logger.error('Exception in default exception handler',
                                 exc_info=True)
        else:
            try:
                self._exception_handler(self, context)
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException as exc:
                # Exception in the user set custom exception handler.
                try:
                    # Let's try default handler.
                    self.default_exception_handler({
                        'message': 'Unhandled error in exception handler',
                        'exception': exc,
                        'context': context,
                    })
                except (KeyboardInterrupt, SystemExit):
                    raise
                except BaseException:
                    # Guard 'default_exception_handler' in case it is
                    # overloaded.
                    aio_logger.error('Exception in default exception handler '
                                     'while handling an unexpected error '
                                     'in custom exception handler',
                                     exc_info=True)

    def add_reader(self, fileobj, callback, *args):
        """Add a reader callback."""
        if len(args) == 0:
            args = None
        self._add_reader(fileobj, new_Handle(self, callback, args, None))

    def remove_reader(self, fileobj):
        """Remove a reader callback."""
        self._remove_reader(fileobj)

    def add_writer(self, fileobj, callback, *args):
        """Add a writer callback.."""
        if len(args) == 0:
            args = None
        self._add_writer(fileobj, new_Handle(self, callback, args, None))

    def remove_writer(self, fileobj):
        """Remove a writer callback."""
        self._remove_writer(fileobj)

    @cython.iterable_coroutine
    async def sock_recv(self, sock, n):
        """Receive data from the socket.

        The return value is a bytes object representing the data received.
        The maximum amount of data to be received at once is specified by
        nbytes.

        This method is a coroutine.
        """
        cdef:
            Handle handle

        if self._debug and sock.gettimeout() != 0:
            raise ValueError("the socket must be non-blocking")

        fut = _SyncSocketReaderFuture(sock, self)
        handle = new_MethodHandle3(
            self,
            "Loop._sock_recv",
            <method3_t>self._sock_recv,
            None,
            self,
            fut, sock, n)

        self._add_reader(sock, handle)
        return await fut

    @cython.iterable_coroutine
    async def sock_recv_into(self, sock, buf):
        """Receive data from the socket.

        The received data is written into *buf* (a writable buffer).
        The return value is the number of bytes written.

        This method is a coroutine.
        """
        cdef:
            Handle handle

        if self._debug and sock.gettimeout() != 0:
            raise ValueError("the socket must be non-blocking")

        fut = _SyncSocketReaderFuture(sock, self)
        handle = new_MethodHandle3(
            self,
            "Loop._sock_recv_into",
            <method3_t>self._sock_recv_into,
            None,
            self,
            fut, sock, buf)

        self._add_reader(sock, handle)
        return await fut

    @cython.iterable_coroutine
    async def sock_sendall(self, sock, data):
        """Send data to the socket.

        The socket must be connected to a remote socket. This method continues
        to send data from data until either all data has been sent or an
        error occurs. None is returned on success. On error, an exception is
        raised, and there is no way to determine how much data, if any, was
        successfully processed by the receiving end of the connection.

        This method is a coroutine.
        """
        cdef:
            Handle handle
            ssize_t n

        if self._debug and sock.gettimeout() != 0:
            raise ValueError("the socket must be non-blocking")

        if not data:
            return

        socket_inc_io_ref(sock)
        try:
            try:
                n = sock.send(data)
            except (BlockingIOError, InterruptedError):
                pass
            else:
                if UVLOOP_DEBUG:
                    # This can be a partial success, i.e. only part
                    # of the data was sent
                    self._sock_try_write_total += 1

                if n == len(data):
                    return
                if not isinstance(data, memoryview):
                    data = memoryview(data)
                data = data[n:]

            fut = _SyncSocketWriterFuture(sock, self)
            handle = new_MethodHandle3(
                self,
                "Loop._sock_sendall",
                <method3_t>self._sock_sendall,
                None,
                self,
                fut, sock, data)

            self._add_writer(sock, handle)
            return await fut
        finally:
            socket_dec_io_ref(sock)

    @cython.iterable_coroutine
    async def sock_accept(self, sock):
        """Accept a connection.

        The socket must be bound to an address and listening for connections.
        The return value is a pair (conn, address) where conn is a new socket
        object usable to send and receive data on the connection, and address
        is the address bound to the socket on the other end of the connection.

        This method is a coroutine.
        """
        cdef:
            Handle handle

        if self._debug and sock.gettimeout() != 0:
            raise ValueError("the socket must be non-blocking")

        fut = _SyncSocketReaderFuture(sock, self)
        handle = new_MethodHandle2(
            self,
            "Loop._sock_accept",
            <method2_t>self._sock_accept,
            None,
            self,
            fut, sock)

        self._add_reader(sock, handle)
        return await fut

    @cython.iterable_coroutine
    async def sock_connect(self, sock, address):
        """Connect to a remote socket at address.

        This method is a coroutine.
        """
        if self._debug and sock.gettimeout() != 0:
            raise ValueError("the socket must be non-blocking")

        socket_inc_io_ref(sock)
        try:
            if sock.family == uv.AF_UNIX:
                fut = self._sock_connect(sock, address)
            else:
                addrs = await self.getaddrinfo(
                    *address[:2], family=sock.family)

                _, _, _, _, address = addrs[0]
                fut = self._sock_connect(sock, address)
            if fut is not None:
                await fut
        finally:
            socket_dec_io_ref(sock)

    @cython.iterable_coroutine
    async def sock_recvfrom(self, sock, bufsize):
        raise NotImplementedError

    @cython.iterable_coroutine
    async def sock_recvfrom_into(self, sock, buf, nbytes=0):
        raise NotImplementedError

    @cython.iterable_coroutine
    async def sock_sendto(self, sock, data, address):
        raise NotImplementedError

    @cython.iterable_coroutine
    async def connect_accepted_socket(self, protocol_factory, sock, *,
                                      ssl=None,
                                      ssl_handshake_timeout=None,
                                      ssl_shutdown_timeout=None):
        """Handle an accepted connection.

        This is used by servers that accept connections outside of
        asyncio but that use asyncio to handle connections.

        This method is a coroutine.  When completed, the coroutine
        returns a (transport, protocol) pair.
        """

        cdef:
            UVStream transport = None

        if ssl is not None:
            if not isinstance(ssl, ssl_SSLContext):
                raise TypeError('ssl argument must be an SSLContext or None')
        else:
            if ssl_handshake_timeout is not None:
                raise ValueError(
                    'ssl_handshake_timeout is only meaningful with ssl')
            if ssl_shutdown_timeout is not None:
                raise ValueError(
                    'ssl_shutdown_timeout is only meaningful with ssl')

        if not _is_sock_stream(sock.type):
            raise ValueError(
                'A Stream Socket was expected, got {!r}'.format(sock))

        app_protocol = protocol_factory()
        waiter = self._new_future()
        transport_waiter = None
        context = Context_CopyCurrent()

        if ssl is None:
            protocol = app_protocol
            transport_waiter = waiter
        else:
            protocol = SSLProtocol(
                self, app_protocol, ssl, waiter,
                server_side=True,
                server_hostname=None,
                ssl_handshake_timeout=ssl_handshake_timeout,
                ssl_shutdown_timeout=ssl_shutdown_timeout)
            transport_waiter = None

        if sock.family == uv.AF_UNIX:
            transport = <UVStream>UnixTransport.new(
                self, protocol, None, transport_waiter, context)
        elif sock.family in (uv.AF_INET, uv.AF_INET6):
            transport = <UVStream>TCPTransport.new(
                self, protocol, None, transport_waiter, context)

        if transport is None:
            raise ValueError(
                'invalid socket family, expected AF_UNIX, AF_INET or AF_INET6')

        transport._open(sock.fileno())
        transport._init_protocol()
        transport._attach_fileobj(sock)

        if ssl:
            app_transport = protocol._get_app_transport(context)
            try:
                await waiter
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                app_transport.close()
                raise
            return app_transport, protocol
        else:
            try:
                await waiter
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException:
                transport._close()
                raise
            return transport, protocol

    def run_in_executor(self, executor, func, *args):
        if aio_iscoroutine(func) or inspect_iscoroutinefunction(func):
            raise TypeError("coroutines cannot be used with run_in_executor()")

        self._check_closed()

        if executor is None:
            executor = self._default_executor
            # Only check when the default executor is being used
            self._check_default_executor()
            if executor is None:
                executor = cc_ThreadPoolExecutor()
                self._default_executor = executor

        return aio_wrap_future(executor.submit(func, *args), loop=self)

    def set_default_executor(self, executor):
        self._default_executor = executor

    @cython.iterable_coroutine
    async def __subprocess_run(self, protocol_factory, args,
                               stdin=subprocess_PIPE,
                               stdout=subprocess_PIPE,
                               stderr=subprocess_PIPE,
                               universal_newlines=False,
                               shell=True,
                               bufsize=0,
                               preexec_fn=None,
                               close_fds=None,
                               cwd=None,
                               env=None,
                               startupinfo=None,
                               creationflags=0,
                               restore_signals=True,
                               start_new_session=False,
                               executable=None,
                               pass_fds=(),
                               **kwargs):

        # TODO: Implement close_fds (might not be very important in
        # Python 3.5, since all FDs aren't inheritable by default.)

        cdef:
            int debug_flags = 0

        if universal_newlines:
            raise ValueError("universal_newlines must be False")
        if bufsize != 0:
            raise ValueError("bufsize must be 0")
        if startupinfo is not None:
            raise ValueError('startupinfo is not supported')
        if creationflags != 0:
            raise ValueError('creationflags is not supported')

        if executable is not None:
            args[0] = executable

        # For tests only! Do not use in your code. Ever.
        if kwargs.pop("__uvloop_sleep_after_fork", False):
            debug_flags |= __PROCESS_DEBUG_SLEEP_AFTER_FORK
        if kwargs:
            raise ValueError(
                'unexpected kwargs: {}'.format(', '.join(kwargs.keys())))

        waiter = self._new_future()
        protocol = protocol_factory()
        proc = UVProcessTransport.new(self, protocol,
                                      args, env, cwd, start_new_session,
                                      stdin, stdout, stderr, pass_fds,
                                      waiter,
                                      debug_flags,
                                      preexec_fn,
                                      restore_signals)

        try:
            await waiter
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            proc.close()
            raise

        return proc, protocol

    @cython.iterable_coroutine
    async def subprocess_shell(self, protocol_factory, cmd, *,
                               shell=True,
                               **kwargs):

        if not shell:
            raise ValueError("shell must be True")

        args = [cmd]
        if shell:
            args = [b'/bin/sh', b'-c'] + args

        return await self.__subprocess_run(protocol_factory, args, shell=True,
                                           **kwargs)

    @cython.iterable_coroutine
    async def subprocess_exec(self, protocol_factory, program, *args,
                              shell=False, **kwargs):

        if shell:
            raise ValueError("shell must be False")

        args = list((program,) + args)

        return await self.__subprocess_run(protocol_factory, args, shell=False,
                                           **kwargs)

    @cython.iterable_coroutine
    async def connect_read_pipe(self, proto_factory, pipe):
        """Register read pipe in event loop. Set the pipe to non-blocking mode.

        protocol_factory should instantiate object with Protocol interface.
        pipe is a file-like object.
        Return pair (transport, protocol), where transport supports the
        ReadTransport interface."""
        cdef:
            ReadUnixTransport transp

        waiter = self._new_future()
        proto = proto_factory()
        transp = ReadUnixTransport.new(self, proto, None, waiter)
        transp._add_extra_info('pipe', pipe)
        try:
            transp._open(pipe.fileno())
            transp._init_protocol()
            await waiter
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            transp._close()
            raise
        transp._attach_fileobj(pipe)
        return transp, proto

    @cython.iterable_coroutine
    async def connect_write_pipe(self, proto_factory, pipe):
        """Register write pipe in event loop.

        protocol_factory should instantiate object with BaseProtocol interface.
        Pipe is file-like object already switched to nonblocking.
        Return pair (transport, protocol), where transport support
        WriteTransport interface."""
        cdef:
            WriteUnixTransport transp

        waiter = self._new_future()
        proto = proto_factory()
        transp = WriteUnixTransport.new(self, proto, None, waiter)
        transp._add_extra_info('pipe', pipe)
        try:
            transp._open(pipe.fileno())
            transp._init_protocol()
            await waiter
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            transp._close()
            raise
        transp._attach_fileobj(pipe)
        return transp, proto

    def add_signal_handler(self, sig, callback, *args):
        """Add a handler for a signal.  UNIX only.

        Raise ValueError if the signal number is invalid or uncatchable.
        Raise RuntimeError if there is a problem setting up the handler.
        """
        cdef:
            Handle h

        if not self._is_main_thread():
            raise ValueError(
                'add_signal_handler() can only be called from '
                'the main thread')

        if (aio_iscoroutine(callback)
                or inspect_iscoroutinefunction(callback)):
            raise TypeError(
                "coroutines cannot be used with add_signal_handler()")

        if sig == uv.SIGCHLD:
            if (hasattr(callback, '__self__') and
                    isinstance(callback.__self__, aio_AbstractChildWatcher)):

                warnings_warn(
                    "!!! asyncio is trying to install its ChildWatcher for "
                    "SIGCHLD signal !!!\n\nThis is probably because a uvloop "
                    "instance is used with asyncio.set_event_loop(). "
                    "The correct way to use uvloop is to install its policy: "
                    "`asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())`"
                    "\n\n", RuntimeWarning, source=self)

                # TODO: ideally we should always raise an error here,
                # but that would be a backwards incompatible change,
                # because we recommended using "asyncio.set_event_loop()"
                # in our README.  Need to start a deprecation period
                # at some point to turn this warning into an error.
                return

            raise RuntimeError(
                'cannot add a signal handler for SIGCHLD: it is used '
                'by the event loop to track subprocesses')

        self._check_signal(sig)
        self._check_closed()

        h = new_Handle(self, callback, args or None, None)
        self._signal_handlers[sig] = h

        try:
            # Register a dummy signal handler to ask Python to write the signal
            # number in the wakeup file descriptor.
            signal_signal(sig, self.__sighandler)

            # Set SA_RESTART to limit EINTR occurrences.
            signal_siginterrupt(sig, False)
        except OSError as exc:
            del self._signal_handlers[sig]
            if not self._signal_handlers:
                try:
                    signal_set_wakeup_fd(-1)
                except (ValueError, OSError) as nexc:
                    aio_logger.info('set_wakeup_fd(-1) failed: %s', nexc)

            if exc.errno == errno_EINVAL:
                raise RuntimeError('sig {} cannot be caught'.format(sig))
            else:
                raise

    def remove_signal_handler(self, sig):
        """Remove a handler for a signal.  UNIX only.

        Return True if a signal handler was removed, False if not.
        """

        if not self._is_main_thread():
            raise ValueError(
                'remove_signal_handler() can only be called from '
                'the main thread')

        self._check_signal(sig)

        if not self._listening_signals:
            return False

        try:
            del self._signal_handlers[sig]
        except KeyError:
            return False

        if sig == uv.SIGINT:
            handler = signal_default_int_handler
        else:
            handler = signal_SIG_DFL

        try:
            signal_signal(sig, handler)
        except OSError as exc:
            if exc.errno == errno_EINVAL:
                raise RuntimeError('sig {} cannot be caught'.format(sig))
            else:
                raise

        return True

    @cython.iterable_coroutine
    async def create_datagram_endpoint(self, protocol_factory,
                                       local_addr=None, remote_addr=None, *,
                                       family=0, proto=0, flags=0,
                                       reuse_address=_unset, reuse_port=None,
                                       allow_broadcast=None, sock=None):
        """A coroutine which creates a datagram endpoint.

        This method will try to establish the endpoint in the background.
        When successful, the coroutine returns a (transport, protocol) pair.

        protocol_factory must be a callable returning a protocol instance.

        socket family AF_INET or socket.AF_INET6 depending on host (or
        family if specified), socket type SOCK_DGRAM.

        reuse_port tells the kernel to allow this endpoint to be bound to
        the same port as other existing endpoints are bound to, so long as
        they all set this flag when being created. This option is not
        supported on Windows and some UNIX's. If the
        :py:data:`~socket.SO_REUSEPORT` constant is not defined then this
        capability is unsupported.

        allow_broadcast tells the kernel to allow this endpoint to send
        messages to the broadcast address.

        sock can optionally be specified in order to use a preexisting
        socket object.
        """
        cdef:
            UDPTransport udp = None
            system.addrinfo * lai
            system.addrinfo * rai

        if sock is not None:
            if not _is_sock_dgram(sock.type):
                raise ValueError(
                    'A UDP Socket was expected, got {!r}'.format(sock))
            if (local_addr or remote_addr or
                    family or proto or flags or
                    reuse_port or allow_broadcast):
                # show the problematic kwargs in exception msg
                opts = dict(local_addr=local_addr, remote_addr=remote_addr,
                            family=family, proto=proto, flags=flags,
                            reuse_address=reuse_address, reuse_port=reuse_port,
                            allow_broadcast=allow_broadcast)
                problems = ', '.join(
                    '{}={}'.format(k, v) for k, v in opts.items() if v)
                raise ValueError(
                    'socket modifier keyword arguments can not be used '
                    'when sock is specified. ({})'.format(problems))
            sock.setblocking(False)
            udp = UDPTransport.__new__(UDPTransport)
            udp._init(self, uv.AF_UNSPEC)
            udp.open(sock.family, sock.fileno())
            udp._attach_fileobj(sock)
        else:
            if reuse_address is not _unset:
                if reuse_address:
                    raise ValueError("Passing `reuse_address=True` is no "
                                     "longer supported, as the usage of "
                                     "SO_REUSEPORT in UDP poses a significant "
                                     "security concern.")
                else:
                    warnings_warn("The *reuse_address* parameter has been "
                                  "deprecated as of 0.15.", DeprecationWarning,
                                  stacklevel=2)
            reuse_port = bool(reuse_port)
            if reuse_port and not has_SO_REUSEPORT:
                raise ValueError(
                    'reuse_port not supported by socket module')

            lads = None
            if local_addr is not None:
                if (not isinstance(local_addr, (tuple, list)) or
                        len(local_addr) != 2):
                    raise TypeError(
                        'local_addr must be a tuple of (host, port)')
                lads = await self._getaddrinfo(
                    local_addr[0], local_addr[1],
                    family, uv.SOCK_DGRAM, proto, flags,
                    0)

            rads = None
            if remote_addr is not None:
                if (not isinstance(remote_addr, (tuple, list)) or
                        len(remote_addr) != 2):
                    raise TypeError(
                        'remote_addr must be a tuple of (host, port)')
                rads = await self._getaddrinfo(
                    remote_addr[0], remote_addr[1],
                    family, uv.SOCK_DGRAM, proto, flags,
                    0)

            excs = []
            if lads is None:
                if rads is not None:
                    udp = UDPTransport.__new__(UDPTransport)
                    rai = (<AddrInfo>rads).data
                    udp._init(self, rai.ai_family)
                    udp._connect(rai.ai_addr, rai.ai_addrlen)
                    udp._set_address(rai)
                else:
                    if family not in (uv.AF_INET, uv.AF_INET6):
                        raise ValueError('unexpected address family')
                    udp = UDPTransport.__new__(UDPTransport)
                    udp._init(self, family)

                if reuse_port:
                    self._sock_set_reuseport(udp._fileno())

            else:
                lai = (<AddrInfo>lads).data
                while lai is not NULL:
                    try:
                        udp = UDPTransport.__new__(UDPTransport)
                        udp._init(self, lai.ai_family)
                        if reuse_port:
                            self._sock_set_reuseport(udp._fileno())
                        udp._bind(lai.ai_addr)
                    except (KeyboardInterrupt, SystemExit):
                        raise
                    except BaseException as ex:
                        lai = lai.ai_next
                        excs.append(ex)
                        continue
                    else:
                        break
                else:
                    ctx = None
                    if len(excs):
                        ctx = excs[0]
                    raise OSError('could not bind to local_addr {}'.format(
                        local_addr)) from ctx

                if rads is not None:
                    rai = (<AddrInfo>rads).data
                    while rai is not NULL:
                        if rai.ai_family != lai.ai_family:
                            rai = rai.ai_next
                            continue
                        if rai.ai_protocol != lai.ai_protocol:
                            rai = rai.ai_next
                            continue
                        udp._connect(rai.ai_addr, rai.ai_addrlen)
                        udp._set_address(rai)
                        break
                    else:
                        raise OSError(
                            'could not bind to remote_addr {}'.format(
                                remote_addr))

        if allow_broadcast:
            udp._set_broadcast(1)

        protocol = protocol_factory()
        waiter = self._new_future()
        assert udp is not None
        udp._set_protocol(protocol)
        udp._set_waiter(waiter)
        udp._init_protocol()

        await waiter
        return udp, protocol

    def _monitor_fs(self, path: str, callback) -> asyncio.Handle:
        cdef:
            UVFSEvent fs_handle
            char* c_str_path

        self._check_closed()
        fs_handle = UVFSEvent.new(self, callback, None)
        p_bytes = path.encode('UTF-8')
        c_str_path = p_bytes
        flags = 0
        fs_handle.start(c_str_path, flags)
        return fs_handle

    def _check_default_executor(self):
        if self._executor_shutdown_called:
            raise RuntimeError('Executor shutdown has been called')

    def _asyncgen_finalizer_hook(self, agen):
        self._asyncgens.discard(agen)
        if not self.is_closed():
            self.call_soon_threadsafe(self.create_task, agen.aclose())

    def _asyncgen_firstiter_hook(self, agen):
        if self._asyncgens_shutdown_called:
            warnings_warn(
                "asynchronous generator {!r} was scheduled after "
                "loop.shutdown_asyncgens() call".format(agen),
                ResourceWarning, source=self)

        self._asyncgens.add(agen)

    @cython.iterable_coroutine
    async def shutdown_asyncgens(self):
        """Shutdown all active asynchronous generators."""
        self._asyncgens_shutdown_called = True

        if not len(self._asyncgens):
            return

        closing_agens = list(self._asyncgens)
        self._asyncgens.clear()

        shutdown_coro = aio_gather(
            *[ag.aclose() for ag in closing_agens],
            return_exceptions=True)

        results = await shutdown_coro
        for result, agen in zip(results, closing_agens):
            if isinstance(result, Exception):
                self.call_exception_handler({
                    'message': 'an error occurred during closing of '
                               'asynchronous generator {!r}'.format(agen),
                    'exception': result,
                    'asyncgen': agen
                })

    @cython.iterable_coroutine
    async def shutdown_default_executor(self, timeout=None):
        """Schedule the shutdown of the default executor.

        The timeout parameter specifies the amount of time the executor will
        be given to finish joining. The default value is None, which means
        that the executor will be given an unlimited amount of time.
        """
        self._executor_shutdown_called = True
        if self._default_executor is None:
            return
        future = self.create_future()
        thread = threading_Thread(target=self._do_shutdown, args=(future,))
        thread.start()
        try:
            await future
        finally:
            thread.join(timeout)

        if thread.is_alive():
            warnings_warn(
                "The executor did not finishing joining "
                f"its threads within {timeout} seconds.",
                RuntimeWarning,
                stacklevel=2
            )
            self._default_executor.shutdown(wait=False)

    def _do_shutdown(self, future):
        try:
            self._default_executor.shutdown(wait=True)
            self.call_soon_threadsafe(future.set_result, None)
        except Exception as ex:
            self.call_soon_threadsafe(future.set_exception, ex)


# Expose pointer for integration with other C-extensions
def libuv_get_loop_t_ptr(loop):
    return PyCapsule_New(<void *>(<Loop>loop).uvloop, NULL, NULL)


def libuv_get_version():
    return uv.uv_version()


def _testhelper_unwrap_capsuled_pointer(obj):
    return <uint64_t>PyCapsule_GetPointer(obj, NULL)


cdef void __loop_alloc_buffer(
    uv.uv_handle_t* uvhandle,
    size_t suggested_size,
    uv.uv_buf_t* buf
) noexcept with gil:
    cdef:
        Loop loop = (<UVHandle>uvhandle.data)._loop

    if loop._recv_buffer_in_use == 1:
        buf.len = 0
        exc = RuntimeError('concurrent allocations')
        loop._handle_exception(exc)
        return

    loop._recv_buffer_in_use = 1
    buf.base = loop._recv_buffer
    buf.len = sizeof(loop._recv_buffer)


cdef inline void __loop_free_buffer(Loop loop):
    loop._recv_buffer_in_use = 0


class _SyncSocketReaderFuture(aio_Future):

    def __init__(self, sock, loop):
        aio_Future.__init__(self, loop=loop)
        self.__sock = sock
        self.__loop = loop

    def __remove_reader(self):
        if self.__sock is not None and self.__sock.fileno() != -1:
            self.__loop.remove_reader(self.__sock)
            self.__sock = None

    if PY39:
        def cancel(self, msg=None):
            self.__remove_reader()
            aio_Future.cancel(self, msg=msg)

    else:
        def cancel(self):
            self.__remove_reader()
            aio_Future.cancel(self)


class _SyncSocketWriterFuture(aio_Future):

    def __init__(self, sock, loop):
        aio_Future.__init__(self, loop=loop)
        self.__sock = sock
        self.__loop = loop

    def __remove_writer(self):
        if self.__sock is not None and self.__sock.fileno() != -1:
            self.__loop.remove_writer(self.__sock)
            self.__sock = None

    if PY39:
        def cancel(self, msg=None):
            self.__remove_writer()
            aio_Future.cancel(self, msg=msg)

    else:
        def cancel(self):
            self.__remove_writer()
            aio_Future.cancel(self)


include "cbhandles.pyx"
include "pseudosock.pyx"
include "lru.pyx"

include "handles/handle.pyx"
include "handles/async_.pyx"
include "handles/idle.pyx"
include "handles/check.pyx"
include "handles/timer.pyx"
include "handles/poll.pyx"
include "handles/basetransport.pyx"
include "handles/stream.pyx"
include "handles/streamserver.pyx"
include "handles/tcp.pyx"
include "handles/pipe.pyx"
include "handles/process.pyx"
include "handles/fsevent.pyx"

include "request.pyx"
include "dns.pyx"
include "sslproto.pyx"

include "handles/udp.pyx"

include "server.pyx"


# Used in UVProcess
cdef vint __atfork_installed = 0
cdef vint __forking = 0
cdef Loop __forking_loop = None


cdef void __get_fork_handler() noexcept nogil:
    with gil:
        if (__forking and __forking_loop is not None and
                __forking_loop.active_process_handler is not None):
            __forking_loop.active_process_handler._after_fork()

cdef __install_atfork():
    global __atfork_installed

    if __atfork_installed:
        return
    __atfork_installed = 1

    cdef int err

    err = system.pthread_atfork(NULL, NULL, &system.handleAtFork)
    if err:
        __atfork_installed = 0
        raise convert_error(-err)


# Install PyMem* memory allocators
cdef vint __mem_installed = 0
cdef __install_pymem():
    global __mem_installed
    if __mem_installed:
        return
    __mem_installed = 1

    cdef int err
    err = uv.uv_replace_allocator(<uv.uv_malloc_func>PyMem_RawMalloc,
                                  <uv.uv_realloc_func>PyMem_RawRealloc,
                                  <uv.uv_calloc_func>PyMem_RawCalloc,
                                  <uv.uv_free_func>PyMem_RawFree)
    if err < 0:
        __mem_installed = 0
        raise convert_error(err)


cdef _set_signal_wakeup_fd(fd):
    if fd >= 0:
        return signal_set_wakeup_fd(fd, warn_on_full_buffer=False)
    else:
        return signal_set_wakeup_fd(fd)


# Helpers for tests

@cython.iterable_coroutine
async def _test_coroutine_1():
    return 42
```

## File: `uvloop/lru.pyx`
```
cdef object _LRU_MARKER = object()


@cython.final
cdef class LruCache:

    cdef:
        object _dict
        int _maxsize
        object _dict_move_to_end
        object _dict_get

    # We use an OrderedDict for LRU implementation.  Operations:
    #
    # * We use a simple `__setitem__` to push a new entry:
    #       `entries[key] = new_entry`
    #   That will push `new_entry` to the *end* of the entries dict.
    #
    # * When we have a cache hit, we call
    #       `entries.move_to_end(key, last=True)`
    #   to move the entry to the *end* of the entries dict.
    #
    # * When we need to remove entries to maintain `max_size`, we call
    #       `entries.popitem(last=False)`
    #   to remove an entry from the *beginning* of the entries dict.
    #
    # So new entries and hits are always promoted to the end of the
    # entries dict, whereas the unused one will group in the
    # beginning of it.

    def __init__(self, *, maxsize):
        if maxsize <= 0:
            raise ValueError(
                f'maxsize is expected to be greater than 0, got {maxsize}')

        self._dict = col_OrderedDict()
        self._dict_move_to_end = self._dict.move_to_end
        self._dict_get = self._dict.get
        self._maxsize = maxsize

    cdef get(self, key, default):
        o = self._dict_get(key, _LRU_MARKER)
        if o is _LRU_MARKER:
            return default
        self._dict_move_to_end(key)  # last=True
        return o

    cdef inline needs_cleanup(self):
        return len(self._dict) > self._maxsize

    cdef inline cleanup_one(self):
        k, _ = self._dict.popitem(last=False)
        return k

    def __getitem__(self, key):
        o = self._dict[key]
        self._dict_move_to_end(key)  # last=True
        return o

    def __setitem__(self, key, o):
        if key in self._dict:
            self._dict[key] = o
            self._dict_move_to_end(key)  # last=True
        else:
            self._dict[key] = o
        while self.needs_cleanup():
            self.cleanup_one()

    def __delitem__(self, key):
        del self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)
```

## File: `uvloop/pseudosock.pyx`
```
cdef class PseudoSocket:
    cdef:
        int _family
        int _type
        int _proto
        int _fd
        object _peername
        object _sockname

    def __init__(self, int family, int type, int proto, int fd):
        self._family = family
        self._type = type
        self._proto = proto
        self._fd = fd
        self._peername = None
        self._sockname = None

    cdef _na(self, what):
        raise TypeError('transport sockets do not support {}'.format(what))

    cdef _make_sock(self):
        return socket_socket(self._family, self._type, self._proto, self._fd)

    property family:
        def __get__(self):
            try:
                return socket_AddressFamily(self._family)
            except ValueError:
                return self._family

    property type:
        def __get__(self):
            try:
                return socket_SocketKind(self._type)
            except ValueError:
                return self._type

    property proto:
        def __get__(self):
            return self._proto

    def __repr__(self):
        s = ("<uvloop.PseudoSocket fd={}, family={!s}, "
             "type={!s}, proto={}").format(self.fileno(), self.family.name,
                                           self.type.name, self.proto)

        if self._fd != -1:
            try:
                laddr = self.getsockname()
                if laddr:
                    s += ", laddr=%s" % str(laddr)
            except socket_error:
                pass
            try:
                raddr = self.getpeername()
                if raddr:
                    s += ", raddr=%s" % str(raddr)
            except socket_error:
                pass
        s += '>'
        return s

    def __getstate__(self):
        raise TypeError("Cannot serialize socket object")

    def fileno(self):
        return self._fd

    def dup(self):
        fd = os_dup(self._fd)
        sock = socket_socket(self._family, self._type, self._proto, fileno=fd)
        sock.settimeout(0)
        return sock

    def get_inheritable(self):
        return os_get_inheritable(self._fd)

    def set_inheritable(self):
        os_set_inheritable(self._fd)

    def ioctl(self, *args, **kwargs):
        pass

    def getsockopt(self, *args, **kwargs):
        sock = self._make_sock()
        try:
            return sock.getsockopt(*args, **kwargs)
        finally:
            sock.detach()

    def setsockopt(self, *args, **kwargs):
        sock = self._make_sock()
        try:
            return sock.setsockopt(*args, **kwargs)
        finally:
            sock.detach()

    def getpeername(self):
        if self._peername is not None:
            return self._peername

        sock = self._make_sock()
        try:
            self._peername = sock.getpeername()
            return self._peername
        finally:
            sock.detach()

    def getsockname(self):
        if self._sockname is not None:
            return self._sockname

        sock = self._make_sock()
        try:
            self._sockname = sock.getsockname()
            return self._sockname
        finally:
            sock.detach()

    def share(self, process_id):
        sock = self._make_sock()
        try:
            return sock.share(process_id)
        finally:
            sock.detach()

    def accept(self):
        self._na('accept() method')

    def connect(self, *args):
        self._na('connect() method')

    def connect_ex(self, *args):
        self._na('connect_ex() method')

    def bind(self, *args):
        self._na('bind() method')

    def listen(self, *args, **kwargs):
        self._na('listen() method')

    def makefile(self):
        self._na('makefile() method')

    def sendfile(self, *args, **kwargs):
        self._na('sendfile() method')

    def close(self):
        self._na('close() method')

    def detach(self):
        self._na('detach() method')

    def shutdown(self, *args):
        self._na('shutdown() method')

    def sendmsg_afalg(self, *args, **kwargs):
        self._na('sendmsg_afalg() method')

    def sendmsg(self):
        self._na('sendmsg() method')

    def sendto(self, *args, **kwargs):
        self._na('sendto() method')

    def send(self, *args, **kwargs):
        self._na('send() method')

    def sendall(self, *args, **kwargs):
        self._na('sendall() method')

    def recv_into(self, *args, **kwargs):
        self._na('recv_into() method')

    def recvfrom_into(self, *args, **kwargs):
        self._na('recvfrom_into() method')

    def recvmsg_into(self, *args, **kwargs):
        self._na('recvmsg_into() method')

    def recvmsg(self, *args, **kwargs):
        self._na('recvmsg() method')

    def recvfrom(self, *args, **kwargs):
        self._na('recvfrom() method')

    def recv(self, *args, **kwargs):
        self._na('recv() method')

    def settimeout(self, value):
        if value == 0:
            return
        raise ValueError(
            'settimeout(): only 0 timeout is allowed on transport sockets')

    def gettimeout(self):
        return 0

    def setblocking(self, flag):
        if not flag:
            return
        raise ValueError(
            'setblocking(): transport sockets cannot be blocking')

    def __enter__(self):
        self._na('context manager protocol')

    def __exit__(self, *err):
        self._na('context manager protocol')
```

## File: `uvloop/request.pxd`
```
cdef class UVRequest:
    cdef:
        uv.uv_req_t *request
        bint done
        Loop loop

    cdef on_done(self)
    cdef cancel(self)
```

## File: `uvloop/request.pyx`
```
cdef class UVRequest:
    """A base class for all libuv requests (uv_getaddrinfo_t, etc).

    Important: it's a responsibility of the subclass to call the
    "on_done" method in the request's callback.

    If "on_done" isn't called, the request object will never die.
    """

    def __cinit__(self, Loop loop, *_):
        self.request = NULL
        self.loop = loop
        self.done = 0
        Py_INCREF(self)

    cdef on_done(self):
        self.done = 1
        Py_DECREF(self)

    cdef cancel(self):
        # Most requests are implemented using a threadpool.  It's only
        # possible to cancel a request when it's still in a threadpool's
        # queue.  Once it's started to execute, we have to wait until
        # it finishes and calls its callback (and callback *must* call
        # UVRequest.on_done).

        cdef int err

        if self.done == 1:
            return

        if UVLOOP_DEBUG:
            if self.request is NULL:
                raise RuntimeError(
                    '{}.cancel: .request is NULL'.format(
                        self.__class__.__name__))

            if self.request.data is NULL:
                raise RuntimeError(
                    '{}.cancel: .request.data is NULL'.format(
                        self.__class__.__name__))

            if <UVRequest>self.request.data is not self:
                raise RuntimeError(
                    '{}.cancel: .request.data is not UVRequest'.format(
                        self.__class__.__name__))

        # We only can cancel pending requests.  Let's try.
        err = uv.uv_cancel(self.request)
        if err < 0:
            if err == uv.UV_EBUSY:
                # Can't close the request -- it's executing (see the first
                # comment).  Loop will have to wait until the callback
                # fires.
                pass
            elif err == uv.UV_EINVAL:
                # From libuv docs:
                #
                #     Only cancellation of uv_fs_t, uv_getaddrinfo_t,
                #     uv_getnameinfo_t and uv_work_t requests is currently
                #     supported.
                return
            else:
                ex = convert_error(err)
                self.loop._handle_exception(ex)
```

## File: `uvloop/server.pxd`
```
cdef class Server:
    cdef:
        list _servers
        list _waiters
        int _active_count
        Loop _loop
        bint _serving
        object _serving_forever_fut
        object __weakref__

    cdef _add_server(self, UVStreamServer srv)
    cdef _start_serving(self)
    cdef _wakeup(self)

    cdef _attach(self)
    cdef _detach(self)

    cdef _ref(self)
    cdef _unref(self)
```

## File: `uvloop/server.pyx`
```
import asyncio


cdef class Server:
    def __cinit__(self, Loop loop):
        self._loop = loop
        self._servers = []
        self._waiters = []
        self._active_count = 0
        self._serving_forever_fut = None

    cdef _add_server(self, UVStreamServer srv):
        self._servers.append(srv)

    cdef _start_serving(self):
        if self._serving:
            return

        self._serving = 1
        for server in self._servers:
            (<UVStreamServer>server).listen()

    cdef _wakeup(self):
        cdef list waiters

        waiters = self._waiters
        self._waiters = None
        for waiter in waiters:
            if not waiter.done():
                waiter.set_result(waiter)

    cdef _attach(self):
        assert self._servers is not None
        self._active_count += 1

    cdef _detach(self):
        assert self._active_count > 0
        self._active_count -= 1
        if self._active_count == 0 and self._servers is None:
            self._wakeup()

    cdef _ref(self):
        # Keep the server object alive while it's not explicitly closed.
        self._loop._servers.add(self)

    cdef _unref(self):
        self._loop._servers.discard(self)

    # Public API

    @cython.iterable_coroutine
    async def __aenter__(self):
        return self

    @cython.iterable_coroutine
    async def __aexit__(self, *exc):
        self.close()
        await self.wait_closed()

    def __repr__(self):
        return '<%s sockets=%r>' % (self.__class__.__name__, self.sockets)

    def get_loop(self):
        return self._loop

    @cython.iterable_coroutine
    async def wait_closed(self):
        # Do not remove `self._servers is None` below
        # because close() method only closes server sockets
        # and existing client connections are left open.
        if self._servers is None or self._waiters is None:
            return
        waiter = self._loop._new_future()
        self._waiters.append(waiter)
        await waiter

    def close(self):
        cdef list servers

        if self._servers is None:
            return

        try:
            servers = self._servers
            self._servers = None
            self._serving = 0

            for server in servers:
                (<UVStreamServer>server)._close()

            if self._active_count == 0:
                self._wakeup()
        finally:
            self._unref()

    def is_serving(self):
        return self._serving

    @cython.iterable_coroutine
    async def start_serving(self):
        self._start_serving()

    @cython.iterable_coroutine
    async def serve_forever(self):
        if self._serving_forever_fut is not None:
            raise RuntimeError(
                f'server {self!r} is already being awaited on serve_forever()')
        if self._servers is None:
            raise RuntimeError(f'server {self!r} is closed')

        self._start_serving()
        self._serving_forever_fut = self._loop.create_future()

        try:
            await self._serving_forever_fut
        except asyncio.CancelledError:
            try:
                self.close()
                await self.wait_closed()
            finally:
                raise
        finally:
            self._serving_forever_fut = None

    property sockets:
        def __get__(self):
            cdef list sockets = []

            # Guard against `self._servers is None`
            if self._servers:
                for server in self._servers:
                    sockets.append(
                        (<UVStreamServer>server)._get_socket()
                    )

            return sockets
```

## File: `uvloop/sslproto.pxd`
```
cdef enum SSLProtocolState:
    UNWRAPPED = 0
    DO_HANDSHAKE = 1
    WRAPPED = 2
    FLUSHING = 3
    SHUTDOWN = 4


cdef enum AppProtocolState:
    # This tracks the state of app protocol (https://git.io/fj59P):
    #
    #     INIT -cm-> CON_MADE [-dr*->] [-er-> EOF?] -cl-> CON_LOST
    #
    # * cm: connection_made()
    # * dr: data_received()
    # * er: eof_received()
    # * cl: connection_lost()

    STATE_INIT = 0
    STATE_CON_MADE = 1
    STATE_EOF = 2
    STATE_CON_LOST = 3


cdef class _SSLProtocolTransport:
    cdef:
        Loop _loop
        SSLProtocol _ssl_protocol
        bint _closed
        object context


cdef class SSLProtocol:
    cdef:
        bint _server_side
        str _server_hostname
        object _sslcontext

        object _extra

        object _write_backlog
        size_t _write_buffer_size

        object _waiter
        Loop _loop
        _SSLProtocolTransport _app_transport
        bint _app_transport_created

        object _transport
        object _ssl_handshake_timeout
        object _ssl_shutdown_timeout

        object _sslobj
        object _sslobj_read
        object _sslobj_write
        object _sslobj_pending
        object _incoming
        object _incoming_write
        object _outgoing
        object _outgoing_read
        char* _ssl_buffer
        size_t _ssl_buffer_len
        SSLProtocolState _state
        size_t _conn_lost
        AppProtocolState _app_state

        bint _ssl_writing_paused
        bint _app_reading_paused

        size_t _incoming_high_water
        size_t _incoming_low_water
        bint _ssl_reading_paused

        bint _app_writing_paused
        size_t _outgoing_high_water
        size_t _outgoing_low_water

        object _app_protocol
        bint _app_protocol_is_buffer
        object _app_protocol_get_buffer
        object _app_protocol_buffer_updated

        object _handshake_start_time
        object _handshake_timeout_handle
        object _shutdown_timeout_handle

    # Instead of doing python calls, c methods *_impl are called directly
    # from stream.pyx

    cdef inline get_buffer_impl(self, size_t n, char** buf, size_t* buf_size)
    cdef inline buffer_updated_impl(self, size_t nbytes)

    cdef inline _set_app_protocol(self, app_protocol)
    cdef inline _wakeup_waiter(self, exc=*)
    cdef inline _get_extra_info(self, name, default=*)
    cdef inline _set_state(self, SSLProtocolState new_state)

    # Handshake flow

    cdef inline _start_handshake(self)
    cdef inline _check_handshake_timeout(self)
    cdef inline _do_handshake(self)
    cdef inline _on_handshake_complete(self, handshake_exc)

    # Shutdown flow

    cdef inline _start_shutdown(self, object context=*)
    cdef inline _check_shutdown_timeout(self)
    cdef inline _do_read_into_void(self, object context)
    cdef inline _do_flush(self, object context=*)
    cdef inline _do_shutdown(self, object context=*)
    cdef inline _on_shutdown_complete(self, shutdown_exc)
    cdef inline _abort(self, exc)

    # Outgoing flow

    cdef inline _write_appdata(self, list_of_data, object context)
    cdef inline _do_write(self)
    cdef inline _process_outgoing(self)

    # Incoming flow

    cdef inline _do_read(self)
    cdef inline _do_read__buffered(self)
    cdef inline _do_read__copied(self)
    cdef inline _call_eof_received(self, object context=*)

    # Flow control for writes from APP socket

    cdef inline _control_app_writing(self, object context=*)
    cdef inline size_t _get_write_buffer_size(self)
    cdef inline _set_write_buffer_limits(self, high=*, low=*)

    # Flow control for reads to APP socket

    cdef inline _pause_reading(self)
    cdef inline _resume_reading(self, object context)

    # Flow control for reads from SSL socket

    cdef inline _control_ssl_reading(self)
    cdef inline _set_read_buffer_limits(self, high=*, low=*)
    cdef inline size_t _get_read_buffer_size(self)
    cdef inline _fatal_error(self, exc, message=*)
```

## File: `uvloop/sslproto.pyx`
```
cdef _create_transport_context(server_side, server_hostname):
    if server_side:
        raise ValueError('Server side SSL needs a valid SSLContext')

    # Client side may pass ssl=True to use a default
    # context; in that case the sslcontext passed is None.
    # The default is secure for client connections.
    # Python 3.4+: use up-to-date strong settings.
    sslcontext = ssl_create_default_context()
    if not server_hostname:
        sslcontext.check_hostname = False
    return sslcontext


cdef class _SSLProtocolTransport:

    # TODO:
    # _sendfile_compatible = constants._SendfileMode.FALLBACK

    def __cinit__(self, Loop loop, ssl_protocol, context):
        self._loop = loop
        # SSLProtocol instance
        self._ssl_protocol = ssl_protocol
        self._closed = False
        if context is None:
            context = Context_CopyCurrent()
        self.context = context

    def get_extra_info(self, name, default=None):
        """Get optional transport information."""
        return self._ssl_protocol._get_extra_info(name, default)

    def set_protocol(self, protocol):
        self._ssl_protocol._set_app_protocol(protocol)

    def get_protocol(self):
        return self._ssl_protocol._app_protocol

    def is_closing(self):
        return self._closed

    def close(self):
        """Close the transport.

        Buffered data will be flushed asynchronously.  No more data
        will be received.  After all buffered data is flushed, the
        protocol's connection_lost() method will (eventually) called
        with None as its argument.
        """
        self._closed = True
        self._ssl_protocol._start_shutdown(self.context.copy())

    def __dealloc__(self):
        if not self._closed:
            self._closed = True
            warnings_warn(
                "unclosed transport <uvloop.loop._SSLProtocolTransport "
                "object>", ResourceWarning)

    def is_reading(self):
        return not self._ssl_protocol._app_reading_paused

    def pause_reading(self):
        """Pause the receiving end.

        No data will be passed to the protocol's data_received()
        method until resume_reading() is called.
        """
        self._ssl_protocol._pause_reading()

    def resume_reading(self):
        """Resume the receiving end.

        Data received will once again be passed to the protocol's
        data_received() method.
        """
        self._ssl_protocol._resume_reading(self.context.copy())

    def set_write_buffer_limits(self, high=None, low=None):
        """Set the high- and low-water limits for write flow control.

        These two values control when to call the protocol's
        pause_writing() and resume_writing() methods.  If specified,
        the low-water limit must be less than or equal to the
        high-water limit.  Neither value can be negative.

        The defaults are implementation-specific.  If only the
        high-water limit is given, the low-water limit defaults to an
        implementation-specific value less than or equal to the
        high-water limit.  Setting high to zero forces low to zero as
        well, and causes pause_writing() to be called whenever the
        buffer becomes non-empty.  Setting low to zero causes
        resume_writing() to be called only once the buffer is empty.
        Use of zero for either limit is generally sub-optimal as it
        reduces opportunities for doing I/O and computation
        concurrently.
        """
        self._ssl_protocol._set_write_buffer_limits(high, low)
        self._ssl_protocol._control_app_writing(self.context.copy())

    def get_write_buffer_limits(self):
        return (self._ssl_protocol._outgoing_low_water,
                self._ssl_protocol._outgoing_high_water)

    def get_write_buffer_size(self):
        """Return the current size of the write buffers."""
        return self._ssl_protocol._get_write_buffer_size()

    def set_read_buffer_limits(self, high=None, low=None):
        """Set the high- and low-water limits for read flow control.

        These two values control when to call the upstream transport's
        pause_reading() and resume_reading() methods.  If specified,
        the low-water limit must be less than or equal to the
        high-water limit.  Neither value can be negative.

        The defaults are implementation-specific.  If only the
        high-water limit is given, the low-water limit defaults to an
        implementation-specific value less than or equal to the
        high-water limit.  Setting high to zero forces low to zero as
        well, and causes pause_reading() to be called whenever the
        buffer becomes non-empty.  Setting low to zero causes
        resume_reading() to be called only once the buffer is empty.
        Use of zero for either limit is generally sub-optimal as it
        reduces opportunities for doing I/O and computation
        concurrently.
        """
        self._ssl_protocol._set_read_buffer_limits(high, low)
        self._ssl_protocol._control_ssl_reading()

    def get_read_buffer_limits(self):
        return (self._ssl_protocol._incoming_low_water,
                self._ssl_protocol._incoming_high_water)

    def get_read_buffer_size(self):
        """Return the current size of the read buffer."""
        return self._ssl_protocol._get_read_buffer_size()

    @property
    def _protocol_paused(self):
        # Required for sendfile fallback pause_writing/resume_writing logic
        return self._ssl_protocol._app_writing_paused

    def write(self, data):
        """Write some data bytes to the transport.

        This does not block; it buffers the data and arranges for it
        to be sent out asynchronously.
        """
        if not isinstance(data, (bytes, bytearray, memoryview)):
            raise TypeError(f"data: expecting a bytes-like instance, "
                            f"got {type(data).__name__}")
        if not data:
            return
        self._ssl_protocol._write_appdata((data,), self.context.copy())

    def writelines(self, list_of_data):
        """Write a list (or any iterable) of data bytes to the transport.

        The default implementation concatenates the arguments and
        calls write() on the result.
        """
        self._ssl_protocol._write_appdata(list_of_data, self.context.copy())

    def write_eof(self):
        """Close the write end after flushing buffered data.

        This raises :exc:`NotImplementedError` right now.
        """
        raise NotImplementedError

    def can_write_eof(self):
        """Return True if this transport supports write_eof(), False if not."""
        return False

    def abort(self):
        """Close the transport immediately.

        Buffered data will be lost.  No more data will be received.
        The protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        self._force_close(None)

    def _force_close(self, exc):
        self._closed = True
        self._ssl_protocol._abort(exc)

    def _test__append_write_backlog(self, data):
        # for test only
        self._ssl_protocol._write_backlog.append(data)
        self._ssl_protocol._write_buffer_size += len(data)


cdef class SSLProtocol:
    """SSL protocol.

    Implementation of SSL on top of a socket using incoming and outgoing
    buffers which are ssl.MemoryBIO objects.
    """

    def __cinit__(self, *args, **kwargs):
        self._ssl_buffer_len = SSL_READ_MAX_SIZE
        self._ssl_buffer = <char*>PyMem_RawMalloc(self._ssl_buffer_len)
        if not self._ssl_buffer:
            raise MemoryError()

    def __dealloc__(self):
        PyMem_RawFree(self._ssl_buffer)
        self._ssl_buffer = NULL
        self._ssl_buffer_len = 0

    def __init__(self, loop, app_protocol, sslcontext, waiter,
                 server_side=False, server_hostname=None,
                 call_connection_made=True,
                 ssl_handshake_timeout=None,
                 ssl_shutdown_timeout=None):
        if ssl_handshake_timeout is None:
            ssl_handshake_timeout = SSL_HANDSHAKE_TIMEOUT
        elif ssl_handshake_timeout <= 0:
            raise ValueError(
                f"ssl_handshake_timeout should be a positive number, "
                f"got {ssl_handshake_timeout}")
        if ssl_shutdown_timeout is None:
            ssl_shutdown_timeout = SSL_SHUTDOWN_TIMEOUT
        elif ssl_shutdown_timeout <= 0:
            raise ValueError(
                f"ssl_shutdown_timeout should be a positive number, "
                f"got {ssl_shutdown_timeout}")

        if not sslcontext:
            sslcontext = _create_transport_context(
                server_side, server_hostname)

        self._server_side = server_side
        if server_hostname and not server_side:
            self._server_hostname = server_hostname
        else:
            self._server_hostname = None
        self._sslcontext = sslcontext
        # SSL-specific extra info. More info are set when the handshake
        # completes.
        self._extra = dict(sslcontext=sslcontext)

        # App data write buffering
        self._write_backlog = col_deque()
        self._write_buffer_size = 0

        self._waiter = waiter
        self._loop = loop
        self._set_app_protocol(app_protocol)
        self._app_transport = None
        self._app_transport_created = False
        # transport, ex: SelectorSocketTransport
        self._transport = None
        self._ssl_handshake_timeout = ssl_handshake_timeout
        self._ssl_shutdown_timeout = ssl_shutdown_timeout
        # SSL and state machine
        self._sslobj = None
        self._incoming = ssl_MemoryBIO()
        self._incoming_write = self._incoming.write
        self._outgoing = ssl_MemoryBIO()
        self._outgoing_read = self._outgoing.read
        self._state = UNWRAPPED
        self._conn_lost = 0  # Set when connection_lost called
        if call_connection_made:
            self._app_state = STATE_INIT
        else:
            self._app_state = STATE_CON_MADE

        # Flow Control

        self._ssl_writing_paused = False

        self._app_reading_paused = False

        self._ssl_reading_paused = False
        self._incoming_high_water = 0
        self._incoming_low_water = 0
        self._set_read_buffer_limits()

        self._app_writing_paused = False
        self._outgoing_high_water = 0
        self._outgoing_low_water = 0
        self._set_write_buffer_limits()

    cdef _set_app_protocol(self, app_protocol):
        self._app_protocol = app_protocol
        if (hasattr(app_protocol, 'get_buffer') and
                not isinstance(app_protocol, aio_Protocol)):
            self._app_protocol_get_buffer = app_protocol.get_buffer
            self._app_protocol_buffer_updated = app_protocol.buffer_updated
            self._app_protocol_is_buffer = True
        else:
            self._app_protocol_is_buffer = False

    cdef _wakeup_waiter(self, exc=None):
        if self._waiter is None:
            return
        if not self._waiter.cancelled():
            if exc is not None:
                self._waiter.set_exception(exc)
            else:
                self._waiter.set_result(None)
        self._waiter = None

    def _get_app_transport(self, context=None):
        if self._app_transport is None:
            if self._app_transport_created:
                raise RuntimeError('Creating _SSLProtocolTransport twice')
            self._app_transport = _SSLProtocolTransport(self._loop, self,
                                                        context)
            self._app_transport_created = True
        return self._app_transport

    def connection_made(self, transport):
        """Called when the low-level connection is made.

        Start the SSL handshake.
        """
        self._transport = transport
        self._start_handshake()

    def connection_lost(self, exc):
        """Called when the low-level connection is lost or closed.

        The argument is an exception object or None (the latter
        meaning a regular EOF is received or the connection was
        aborted or closed).
        """
        self._write_backlog.clear()
        self._outgoing_read()
        self._conn_lost += 1

        # Just mark the app transport as closed so that its __dealloc__
        # doesn't complain.
        if self._app_transport is not None:
            self._app_transport._closed = True

        if self._state != DO_HANDSHAKE:
            if self._app_state == STATE_CON_MADE or \
                    self._app_state == STATE_EOF:
                self._app_state = STATE_CON_LOST
                self._loop.call_soon(self._app_protocol.connection_lost, exc)
        self._set_state(UNWRAPPED)
        self._transport = None
        self._app_transport = None
        self._app_protocol = None
        self._wakeup_waiter(exc)

        if self._shutdown_timeout_handle:
            self._shutdown_timeout_handle.cancel()
            self._shutdown_timeout_handle = None
        if self._handshake_timeout_handle:
            self._handshake_timeout_handle.cancel()
            self._handshake_timeout_handle = None

    cdef get_buffer_impl(self, size_t n, char** buf, size_t* buf_size):
        cdef size_t want = n
        if want > SSL_READ_MAX_SIZE:
            want = SSL_READ_MAX_SIZE
        if self._ssl_buffer_len < want:
            self._ssl_buffer = <char*>PyMem_RawRealloc(self._ssl_buffer, want)
            if not self._ssl_buffer:
                raise MemoryError()
            self._ssl_buffer_len = want

        buf[0] = self._ssl_buffer
        buf_size[0] = self._ssl_buffer_len

    cdef buffer_updated_impl(self, size_t nbytes):
        self._incoming_write(PyMemoryView_FromMemory(
            self._ssl_buffer, nbytes, PyBUF_WRITE))

        if self._state == DO_HANDSHAKE:
            self._do_handshake()

        elif self._state == WRAPPED:
            self._do_read()

        elif self._state == FLUSHING:
            self._do_flush()

        elif self._state == SHUTDOWN:
            self._do_shutdown()

    def get_buffer(self, size_t n):
        # This pure python call is still used by some very peculiar test cases
        cdef:
            char* buf
            size_t buf_size

        self.get_buffer_impl(n, &buf, &buf_size)
        return PyMemoryView_FromMemory(buf, buf_size, PyBUF_WRITE)

    def buffer_updated(self, size_t nbytes):
        self.buffer_updated_impl(nbytes)

    def eof_received(self):
        """Called when the other end of the low-level stream
        is half-closed.

        If this returns a false value (including None), the transport
        will close itself.  If it returns a true value, closing the
        transport is up to the protocol.
        """
        try:
            if self._loop.get_debug():
                aio_logger.debug("%r received EOF", self)

            if self._state == DO_HANDSHAKE:
                self._on_handshake_complete(ConnectionResetError)

            elif self._state == WRAPPED or self._state == FLUSHING:
                # We treat a low-level EOF as a critical situation similar to a
                # broken connection - just send whatever is in the buffer and
                # close. No application level eof_received() is called -
                # because we don't want the user to think that this is a
                # graceful shutdown triggered by SSL "close_notify".
                self._set_state(SHUTDOWN)
                self._on_shutdown_complete(None)

            elif self._state == SHUTDOWN:
                self._on_shutdown_complete(None)

        except Exception:
            self._transport.close()
            raise

    cdef _get_extra_info(self, name, default=None):
        if name == 'uvloop.sslproto':
            return self
        elif name in self._extra:
            return self._extra[name]
        elif self._transport is not None:
            return self._transport.get_extra_info(name, default)
        else:
            return default

    cdef _set_state(self, SSLProtocolState new_state):
        cdef bint allowed = False

        if new_state == UNWRAPPED:
            allowed = True

        elif self._state == UNWRAPPED and new_state == DO_HANDSHAKE:
            allowed = True

        elif self._state == DO_HANDSHAKE and new_state == WRAPPED:
            allowed = True

        elif self._state == WRAPPED and new_state == FLUSHING:
            allowed = True

        elif self._state == WRAPPED and new_state == SHUTDOWN:
            allowed = True

        elif self._state == FLUSHING and new_state == SHUTDOWN:
            allowed = True

        if allowed:
            self._state = new_state

        else:
            raise RuntimeError(
                'cannot switch state from {} to {}'.format(
                    self._state, new_state))

    # Handshake flow

    cdef _start_handshake(self):
        if self._loop.get_debug():
            aio_logger.debug("%r starts SSL handshake", self)
            self._handshake_start_time = self._loop.time()
        else:
            self._handshake_start_time = None

        self._set_state(DO_HANDSHAKE)

        # start handshake timeout count down
        self._handshake_timeout_handle = \
            self._loop.call_later(self._ssl_handshake_timeout,
                                  lambda: self._check_handshake_timeout())

        try:
            self._sslobj = self._sslcontext.wrap_bio(
                self._incoming, self._outgoing,
                server_side=self._server_side,
                server_hostname=self._server_hostname)
            self._sslobj_read = self._sslobj.read
            self._sslobj_write = self._sslobj.write
            self._sslobj_pending = self._sslobj.pending
        except Exception as ex:
            self._on_handshake_complete(ex)
        else:
            self._do_handshake()

    cdef _check_handshake_timeout(self):
        if self._state == DO_HANDSHAKE:
            msg = (
                f"SSL handshake is taking longer than "
                f"{self._ssl_handshake_timeout} seconds: "
                f"aborting the connection"
            )
            self._fatal_error(ConnectionAbortedError(msg))

    cdef _do_handshake(self):
        try:
            self._sslobj.do_handshake()
        except ssl_SSLAgainErrors as exc:
            self._process_outgoing()
        except ssl_SSLError as exc:
            self._on_handshake_complete(exc)
        else:
            self._on_handshake_complete(None)

    cdef _on_handshake_complete(self, handshake_exc):
        if self._handshake_timeout_handle is not None:
            self._handshake_timeout_handle.cancel()
            self._handshake_timeout_handle = None

        sslobj = self._sslobj
        try:
            if handshake_exc is None:
                self._set_state(WRAPPED)
            else:
                raise handshake_exc

            peercert = sslobj.getpeercert()
        except Exception as exc:
            self._set_state(UNWRAPPED)
            if isinstance(exc, ssl_CertificateError):
                msg = 'SSL handshake failed on verifying the certificate'
            else:
                msg = 'SSL handshake failed'
            self._fatal_error(exc, msg)
            self._wakeup_waiter(exc)
            return

        if self._loop.get_debug():
            dt = self._loop.time() - self._handshake_start_time
            aio_logger.debug("%r: SSL handshake took %.1f ms", self, dt * 1e3)

        # Add extra info that becomes available after handshake.
        self._extra.update(peercert=peercert,
                           cipher=sslobj.cipher(),
                           compression=sslobj.compression(),
                           ssl_object=sslobj)
        if self._app_state == STATE_INIT:
            self._app_state = STATE_CON_MADE
            self._app_protocol.connection_made(self._get_app_transport())
        self._wakeup_waiter()

        # We should wakeup user code before sending the first data below. In
        # case of `start_tls()`, the user can only get the SSLTransport in the
        # wakeup callback, because `connection_made()` is not called again.
        # We should schedule the first data later than the wakeup callback so
        # that the user get a chance to e.g. check ALPN with the transport
        # before having to handle the first data.
        self._loop._call_soon_handle(
            new_MethodHandle(self._loop,
                             "SSLProtocol._do_read",
                             <method_t> self._do_read,
                             None,  # current context is good
                             self))

    # Shutdown flow

    cdef _start_shutdown(self, object context=None):
        if self._state in (FLUSHING, SHUTDOWN, UNWRAPPED):
            return
        # we don't need the context for _abort or the timeout, because
        # TCP transport._force_close() should be able to call
        # connection_lost() in the right context
        if self._app_transport is not None:
            self._app_transport._closed = True
        if self._state == DO_HANDSHAKE:
            self._abort(None)
        else:
            self._set_state(FLUSHING)
            self._shutdown_timeout_handle = \
                self._loop.call_later(self._ssl_shutdown_timeout,
                                      lambda: self._check_shutdown_timeout())
            self._do_flush(context)

    cdef _check_shutdown_timeout(self):
        if self._state in (FLUSHING, SHUTDOWN):
            self._transport._force_close(
                aio_TimeoutError('SSL shutdown timed out'))

    cdef _do_read_into_void(self, object context):
        """Consume and discard incoming application data.

        If close_notify is received for the first time, call eof_received.
        """
        cdef:
            bint close_notify = False
        try:
            while True:
                if not self._sslobj_read(SSL_READ_MAX_SIZE):
                    close_notify = True
                    break
        except ssl_SSLAgainErrors as exc:
            pass
        except ssl_SSLZeroReturnError:
            close_notify = True
        if close_notify:
            self._call_eof_received(context)

    cdef _do_flush(self, object context=None):
        """Flush the write backlog, discarding new data received.

        We don't send close_notify in FLUSHING because we still want to send
        the remaining data over SSL, even if we received a close_notify. Also,
        no application-level resume_writing() or pause_writing() will be called
        in FLUSHING, as we could fully manage the flow control internally.
        """
        try:
            self._do_read_into_void(context)
            self._do_write()
            self._process_outgoing()
            self._control_ssl_reading()
        except Exception as ex:
            self._on_shutdown_complete(ex)
        else:
            if not self._get_write_buffer_size():
                self._set_state(SHUTDOWN)
                self._do_shutdown(context)

    cdef _do_shutdown(self, object context=None):
        """Send close_notify and wait for the same from the peer."""
        try:
            # we must skip all application data (if any) before unwrap
            self._do_read_into_void(context)
            try:
                self._sslobj.unwrap()
            except ssl_SSLAgainErrors as exc:
                self._process_outgoing()
            else:
                self._process_outgoing()
                if not self._get_write_buffer_size():
                    self._on_shutdown_complete(None)
        except Exception as ex:
            self._on_shutdown_complete(ex)

    cdef _on_shutdown_complete(self, shutdown_exc):
        if self._shutdown_timeout_handle is not None:
            self._shutdown_timeout_handle.cancel()
            self._shutdown_timeout_handle = None

        # we don't need the context here because TCP transport.close() should
        # be able to call connection_made() in the right context
        if shutdown_exc:
            self._fatal_error(shutdown_exc, 'Error occurred during shutdown')
        else:
            self._transport.close()

    cdef _abort(self, exc):
        self._set_state(UNWRAPPED)
        if self._transport is not None:
            self._transport._force_close(exc)

    # Outgoing flow

    cdef _write_appdata(self, list_of_data, object context):
        if self._state in (FLUSHING, SHUTDOWN, UNWRAPPED):
            if self._conn_lost >= LOG_THRESHOLD_FOR_CONNLOST_WRITES:
                aio_logger.warning('SSL connection is closed')
            self._conn_lost += 1
            return

        for data in list_of_data:
            self._write_backlog.append(data)
            self._write_buffer_size += len(data)

        try:
            if self._state == WRAPPED:
                self._do_write()
                self._process_outgoing()
                self._control_app_writing(context)

        except Exception as ex:
            self._fatal_error(ex, 'Fatal error on SSL protocol')

    cdef _do_write(self):
        """Do SSL write, consumes write backlog and fills outgoing BIO."""
        cdef size_t data_len, count
        try:
            while self._write_backlog:
                data = self._write_backlog[0]
                count = self._sslobj_write(data)
                data_len = len(data)
                if count < data_len:
                    if not PyMemoryView_Check(data):
                        data = PyMemoryView_FromObject(data)
                    self._write_backlog[0] = data[count:]
                    self._write_buffer_size -= count
                else:
                    del self._write_backlog[0]
                    self._write_buffer_size -= data_len
        except ssl_SSLAgainErrors as exc:
            pass

    cdef _process_outgoing(self):
        """Send bytes from the outgoing BIO."""
        if not self._ssl_writing_paused:
            data = self._outgoing_read()
            if len(data):
                if isinstance(self._transport, UVStream):
                    (<UVStream>self._transport).write(data)
                else:
                    self._transport.write(data)

    # Incoming flow

    cdef _do_read(self):
        if self._state != WRAPPED:
            return
        try:
            if not self._app_reading_paused:
                if self._app_protocol_is_buffer:
                    self._do_read__buffered()
                else:
                    self._do_read__copied()
                if self._write_backlog:
                    self._do_write()
                self._process_outgoing()
                self._control_app_writing()
            self._control_ssl_reading()
        except Exception as ex:
            self._fatal_error(ex, 'Fatal error on SSL protocol')

    cdef _do_read__buffered(self):
        cdef:
            Py_ssize_t total_pending = (<Py_ssize_t>self._incoming.pending
                                        + <Py_ssize_t>self._sslobj_pending())
            # Ask for a little extra in case when decrypted data is bigger
            # than original
            object app_buffer = self._app_protocol_get_buffer(
                total_pending + 256)
            Py_ssize_t app_buffer_size = len(app_buffer)

        if app_buffer_size == 0:
            return

        cdef:
            Py_ssize_t last_bytes_read = -1
            Py_ssize_t total_bytes_read = 0
            Py_buffer pybuf
            bint pybuf_initialized = False

        try:
            # SSLObject.read may not return all available data in one go.
            # We have to keep calling read until it throw SSLWantReadError.
            # However, throwing SSLWantReadError is very expensive even in
            # the master trunk of cpython.
            # See https://github.com/python/cpython/issues/123954

            # One way to reduce reliance on SSLWantReadError is to check
            # self._incoming.pending > 0 and SSLObject.pending() > 0.
            # SSLObject.read may still throw SSLWantReadError even when
            # self._incoming.pending > 0 and SSLObject.pending() == 0,
            # but this should happen relatively rarely, only when ssl frame
            # is partially received.

            # This optimization works really well especially for peers
            # exchanging small messages and wanting to have minimal latency.

            # self._incoming.pending means how much data hasn't
            # been processed by ssl yet (read: "still encrypted"). The final
            # unencrypted data size maybe different.

            # self._sslobj.pending() means how much data has been already
            # decrypted and can be directly read with SSLObject.read.

            # Run test_create_server_ssl_over_ssl to reproduce different cases
            # for this method.
            while total_pending > 0:
                if total_bytes_read > 0:
                    if not pybuf_initialized:
                        PyObject_GetBuffer(app_buffer, &pybuf, PyBUF_WRITABLE)
                        pybuf_initialized = True

                    app_buffer = PyMemoryView_FromMemory(
                        (<char*>pybuf.buf) + total_bytes_read,
                        app_buffer_size - total_bytes_read,
                        PyBUF_WRITE)

                last_bytes_read = <Py_ssize_t>self._sslobj_read(
                    app_buffer_size - total_bytes_read, app_buffer)
                total_bytes_read += last_bytes_read

                if last_bytes_read == 0:
                    break

                # User buffer may not fit all available data.
                if total_bytes_read == app_buffer_size:
                    self._loop._call_soon_handle(
                        new_MethodHandle(self._loop,
                                         "SSLProtocol._do_read",
                                         <method_t> self._do_read,
                                         None,  # current context is good
                                         self))
                    break

                total_pending = (<Py_ssize_t>self._incoming.pending +
                                 <Py_ssize_t>self._sslobj_pending())
        except ssl_SSLAgainErrors as exc:
            pass
        finally:
            if pybuf_initialized:
                PyBuffer_Release(&pybuf)

        if total_bytes_read > 0:
            self._app_protocol_buffer_updated(total_bytes_read)

        # SSLObject.read() may return 0 instead of throwing SSLWantReadError
        # This indicates that we reached EOF
        if last_bytes_read == 0:
            # close_notify
            self._call_eof_received()
            self._start_shutdown()

    cdef _do_read__copied(self):
        cdef:
            list data
            bytes first, chunk = b'1'
            bint zero = True, one = False

        try:
            while (<Py_ssize_t>self._incoming.pending > 0 or
                   <Py_ssize_t>self._sslobj_pending() > 0):
                chunk = self._sslobj_read(SSL_READ_MAX_SIZE)
                if not chunk:
                    break
                if zero:
                    zero = False
                    one = True
                    first = chunk
                elif one:
                    one = False
                    data = [first, chunk]
                else:
                    data.append(chunk)
        except ssl_SSLAgainErrors as exc:
            pass
        if one:
            self._app_protocol.data_received(first)
        elif not zero:
            self._app_protocol.data_received(b''.join(data))
        if not chunk:
            # close_notify
            self._call_eof_received()
            self._start_shutdown()

    cdef _call_eof_received(self, object context=None):
        if self._app_state == STATE_CON_MADE:
            self._app_state = STATE_EOF
            try:
                if context is None:
                    # If the caller didn't provide a context, we assume the
                    # caller is already in the right context, which is usually
                    # inside the upstream callbacks like buffer_updated()
                    keep_open = self._app_protocol.eof_received()
                else:
                    keep_open = run_in_context(
                        context, self._app_protocol.eof_received,
                    )
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException as ex:
                self._fatal_error(ex, 'Error calling eof_received()')
            else:
                if keep_open:
                    aio_logger.warning('returning true from eof_received() '
                                       'has no effect when using ssl')

    # Flow control for writes from APP socket

    cdef _control_app_writing(self, object context=None):
        cdef size_t size = self._get_write_buffer_size()
        if size >= self._outgoing_high_water and not self._app_writing_paused:
            self._app_writing_paused = True
            try:
                if context is None:
                    # If the caller didn't provide a context, we assume the
                    # caller is already in the right context, which is usually
                    # inside the upstream callbacks like buffer_updated()
                    self._app_protocol.pause_writing()
                else:
                    run_in_context(context, self._app_protocol.pause_writing)
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException as exc:
                self._loop.call_exception_handler({
                    'message': 'protocol.pause_writing() failed',
                    'exception': exc,
                    'transport': self._app_transport,
                    'protocol': self,
                })
        elif size <= self._outgoing_low_water and self._app_writing_paused:
            self._app_writing_paused = False
            try:
                if context is None:
                    # If the caller didn't provide a context, we assume the
                    # caller is already in the right context, which is usually
                    # inside the upstream callbacks like resume_writing()
                    self._app_protocol.resume_writing()
                else:
                    run_in_context(context, self._app_protocol.resume_writing)
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException as exc:
                self._loop.call_exception_handler({
                    'message': 'protocol.resume_writing() failed',
                    'exception': exc,
                    'transport': self._app_transport,
                    'protocol': self,
                })

    cdef size_t _get_write_buffer_size(self):
        return self._outgoing.pending + self._write_buffer_size

    cdef _set_write_buffer_limits(self, high=None, low=None):
        high, low = add_flowcontrol_defaults(
            high, low, FLOW_CONTROL_HIGH_WATER_SSL_WRITE)
        self._outgoing_high_water = high
        self._outgoing_low_water = low

    # Flow control for reads to APP socket

    cdef _pause_reading(self):
        self._app_reading_paused = True

    cdef _resume_reading(self, object context):
        if self._app_reading_paused:
            self._app_reading_paused = False
            if self._state == WRAPPED:
                self._loop._call_soon_handle(
                    new_MethodHandle(self._loop,
                                     "SSLProtocol._do_read",
                                     <method_t>self._do_read,
                                     context,
                                     self))

    # Flow control for reads from SSL socket

    cdef _control_ssl_reading(self):
        cdef size_t size = self._get_read_buffer_size()
        if size >= self._incoming_high_water and not self._ssl_reading_paused:
            self._ssl_reading_paused = True
            self._transport.pause_reading()
        elif size <= self._incoming_low_water and self._ssl_reading_paused:
            self._ssl_reading_paused = False
            self._transport.resume_reading()

    cdef _set_read_buffer_limits(self, high=None, low=None):
        high, low = add_flowcontrol_defaults(
            high, low, FLOW_CONTROL_HIGH_WATER_SSL_READ)
        self._incoming_high_water = high
        self._incoming_low_water = low

    cdef size_t _get_read_buffer_size(self):
        return self._incoming.pending

    # Flow control for writes to SSL socket

    def pause_writing(self):
        """Called when the low-level transport's buffer goes over
        the high-water mark.
        """
        assert not self._ssl_writing_paused
        self._ssl_writing_paused = True

    def resume_writing(self):
        """Called when the low-level transport's buffer drains below
        the low-water mark.
        """
        assert self._ssl_writing_paused
        self._ssl_writing_paused = False

        if self._state == WRAPPED:
            self._process_outgoing()
            self._control_app_writing()

        elif self._state == FLUSHING:
            self._do_flush()

        elif self._state == SHUTDOWN:
            self._do_shutdown()

    cdef _fatal_error(self, exc, message='Fatal error on transport'):
        if self._app_transport:
            self._app_transport._force_close(exc)
        elif self._transport:
            self._transport._force_close(exc)

        if isinstance(exc, OSError):
            if self._loop.get_debug():
                aio_logger.debug("%r: %s", self, message, exc_info=True)
        elif not isinstance(exc, aio_CancelledError):
            self._loop.call_exception_handler({
                'message': message,
                'exception': exc,
                'transport': self._transport,
                'protocol': self,
            })
```

## File: `uvloop/handles/async_.pxd`
```
cdef class UVAsync(UVHandle):
    cdef:
        method_t callback
        object ctx

    cdef _init(self, Loop loop, method_t callback, object ctx)

    cdef send(self)

    @staticmethod
    cdef UVAsync new(Loop loop, method_t callback, object ctx)
```

## File: `uvloop/handles/async_.pyx`
```
@cython.no_gc_clear
cdef class UVAsync(UVHandle):
    cdef _init(self, Loop loop, method_t callback, object ctx):
        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*>PyMem_RawMalloc(sizeof(uv.uv_async_t))
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        err = uv.uv_async_init(self._loop.uvloop,
                               <uv.uv_async_t*>self._handle,
                               __uvasync_callback)
        if err < 0:
            self._abort_init()
            raise convert_error(err)

        self._finish_init()

        self.callback = callback
        self.ctx = ctx

    cdef send(self):
        cdef int err

        self._ensure_alive()

        err = uv.uv_async_send(<uv.uv_async_t*>self._handle)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return

    @staticmethod
    cdef UVAsync new(Loop loop, method_t callback, object ctx):
        cdef UVAsync handle
        handle = UVAsync.__new__(UVAsync)
        handle._init(loop, callback, ctx)
        return handle


cdef void __uvasync_callback(
    uv.uv_async_t* handle,
) noexcept with gil:
    if __ensure_handle_data(<uv.uv_handle_t*>handle, "UVAsync callback") == 0:
        return

    cdef:
        UVAsync async_ = <UVAsync> handle.data
        method_t cb = async_.callback
    try:
        cb(async_.ctx)
    except BaseException as ex:
        async_._error(ex, False)
```

## File: `uvloop/handles/basetransport.pxd`
```
cdef class UVBaseTransport(UVSocketHandle):

    cdef:
        readonly bint _closing

        bint _protocol_connected
        bint _protocol_paused
        object _protocol_data_received
        size_t _high_water
        size_t _low_water

        object _protocol
        Server _server
        object _waiter

        dict _extra_info

        uint32_t _conn_lost

        object __weakref__

    # All "inline" methods are final

    cdef inline _maybe_pause_protocol(self)
    cdef inline _maybe_resume_protocol(self)

    cdef inline _schedule_call_connection_made(self)
    cdef inline _schedule_call_connection_lost(self, exc)

    cdef _wakeup_waiter(self)
    cdef _call_connection_made(self)
    cdef _call_connection_lost(self, exc)

    # Overloads of UVHandle methods:
    cdef _fatal_error(self, exc, throw, reason=?)
    cdef _close(self)

    cdef inline _set_server(self, Server server)
    cdef inline _set_waiter(self, object waiter)

    cdef _set_protocol(self, object protocol)
    cdef _clear_protocol(self)

    cdef inline _init_protocol(self)
    cdef inline _add_extra_info(self, str name, object obj)

    # === overloads ===

    cdef _new_socket(self)
    cdef size_t _get_write_buffer_size(self)

    cdef bint _is_reading(self)
    cdef _start_reading(self)
    cdef _stop_reading(self)
```

## File: `uvloop/handles/basetransport.pyx`
```
cdef class UVBaseTransport(UVSocketHandle):

    def __cinit__(self):
        # Flow control
        self._high_water = FLOW_CONTROL_HIGH_WATER * 1024
        self._low_water = FLOW_CONTROL_HIGH_WATER // 4

        self._protocol = None
        self._protocol_connected = 0
        self._protocol_paused = 0
        self._protocol_data_received = None

        self._server = None
        self._waiter = None
        self._extra_info = None

        self._conn_lost = 0

        self._closing = 0

    cdef size_t _get_write_buffer_size(self):
        return 0

    cdef inline _schedule_call_connection_made(self):
        self._loop._call_soon_handle(
            new_MethodHandle(self._loop,
                             "UVTransport._call_connection_made",
                             <method_t>self._call_connection_made,
                             self.context,
                             self))

    cdef inline _schedule_call_connection_lost(self, exc):
        self._loop._call_soon_handle(
            new_MethodHandle1(self._loop,
                              "UVTransport._call_connection_lost",
                              <method1_t>self._call_connection_lost,
                              self.context,
                              self, exc))

    cdef _fatal_error(self, exc, throw, reason=None):
        # Overload UVHandle._fatal_error

        self._force_close(exc)

        if not isinstance(exc, OSError):

            if throw or self._loop is None:
                raise exc

            msg = f'Fatal error on transport {self.__class__.__name__}'
            if reason is not None:
                msg = f'{msg} ({reason})'

            self._loop.call_exception_handler({
                'message': msg,
                'exception': exc,
                'transport': self,
                'protocol': self._protocol,
            })

    cdef inline _maybe_pause_protocol(self):
        cdef:
            size_t size = self._get_write_buffer_size()

        if size <= self._high_water:
            return

        if not self._protocol_paused:
            self._protocol_paused = 1
            try:
                # _maybe_pause_protocol() is always triggered from user-calls,
                # so we must copy the context to avoid entering context twice
                run_in_context(
                    self.context.copy(), self._protocol.pause_writing,
                )
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException as exc:
                self._loop.call_exception_handler({
                    'message': 'protocol.pause_writing() failed',
                    'exception': exc,
                    'transport': self,
                    'protocol': self._protocol,
                })

    cdef inline _maybe_resume_protocol(self):
        cdef:
            size_t size = self._get_write_buffer_size()

        if self._protocol_paused and size <= self._low_water:
            self._protocol_paused = 0
            try:
                # We're copying the context to avoid entering context twice,
                # even though it's not always necessary to copy - it's easier
                # to copy here than passing down a copied context.
                run_in_context(
                    self.context.copy(), self._protocol.resume_writing,
                )
            except (KeyboardInterrupt, SystemExit):
                raise
            except BaseException as exc:
                self._loop.call_exception_handler({
                    'message': 'protocol.resume_writing() failed',
                    'exception': exc,
                    'transport': self,
                    'protocol': self._protocol,
                })

    cdef _wakeup_waiter(self):
        if self._waiter is not None:
            if not self._waiter.cancelled():
                if not self._is_alive():
                    self._waiter.set_exception(
                        RuntimeError(
                            'closed Transport handle and unset waiter'))
                else:
                    self._waiter.set_result(True)
            self._waiter = None

    cdef _call_connection_made(self):
        if self._protocol is None:
            raise RuntimeError(
                'protocol is not set, cannot call connection_made()')

        # We use `_is_alive()` and not `_closing`, because we call
        # `transport._close()` in `loop.create_connection()` if an
        # exception happens during `await waiter`.
        if not self._is_alive():
            # A connection waiter can be cancelled between
            # 'await loop.create_connection()' and
            # `_schedule_call_connection_made` and
            # the actual `_call_connection_made`.
            self._wakeup_waiter()
            return

        # Set _protocol_connected to 1 before calling "connection_made":
        # if transport is aborted or closed, "connection_lost" will
        # still be scheduled.
        self._protocol_connected = 1

        try:
            self._protocol.connection_made(self)
        except BaseException:
            self._wakeup_waiter()
            raise

        if not self._is_alive():
            # This might happen when "transport.abort()" is called
            # from "Protocol.connection_made".
            self._wakeup_waiter()
            return

        self._start_reading()
        self._wakeup_waiter()

    cdef _call_connection_lost(self, exc):
        if self._waiter is not None:
            if not self._waiter.done():
                self._waiter.set_exception(exc)
            self._waiter = None

        if self._closed:
            # The handle is closed -- likely, _call_connection_lost
            # was already called before.
            return

        try:
            if self._protocol_connected:
                self._protocol.connection_lost(exc)
        finally:
            self._clear_protocol()

            self._close()

            server = self._server
            if server is not None:
                (<Server>server)._detach()
                self._server = None

    cdef inline _set_server(self, Server server):
        self._server = server
        (<Server>server)._attach()

    cdef inline _set_waiter(self, object waiter):
        if waiter is not None and not isfuture(waiter):
            raise TypeError(
                f'invalid waiter object {waiter!r}, expected asyncio.Future')

        self._waiter = waiter

    cdef _set_protocol(self, object protocol):
        self._protocol = protocol
        # Store a reference to the bound method directly
        try:
            self._protocol_data_received = protocol.data_received
        except AttributeError:
            pass

    cdef _clear_protocol(self):
        self._protocol = None
        self._protocol_data_received = None

    cdef inline _init_protocol(self):
        self._loop._track_transport(self)
        if self._protocol is None:
            raise RuntimeError('invalid _init_protocol call')
        self._schedule_call_connection_made()

    cdef inline _add_extra_info(self, str name, object obj):
        if self._extra_info is None:
            self._extra_info = {}
        self._extra_info[name] = obj

    cdef bint _is_reading(self):
        raise NotImplementedError

    cdef _start_reading(self):
        raise NotImplementedError

    cdef _stop_reading(self):
        raise NotImplementedError

    # === Public API ===

    property _paused:
        # Used by SSLProto.  Might be removed in the future.
        def __get__(self):
            return bool(not self._is_reading())

    def get_protocol(self):
        return self._protocol

    def set_protocol(self, protocol):
        self._set_protocol(protocol)
        if self._is_reading():
            self._stop_reading()
            self._start_reading()

    def _force_close(self, exc):
        # Used by SSLProto.  Might be removed in the future.
        if self._conn_lost or self._closed:
            return
        if not self._closing:
            self._closing = 1
            self._stop_reading()
        self._conn_lost += 1
        self._schedule_call_connection_lost(exc)

    def abort(self):
        self._force_close(None)

    def close(self):
        if self._closing or self._closed:
            return

        self._closing = 1
        self._stop_reading()

        if not self._get_write_buffer_size():
            # The write buffer is empty
            self._conn_lost += 1
            self._schedule_call_connection_lost(None)

    def is_closing(self):
        return self._closing

    def get_write_buffer_size(self):
        return self._get_write_buffer_size()

    def set_write_buffer_limits(self, high=None, low=None):
        self._ensure_alive()

        self._high_water, self._low_water = add_flowcontrol_defaults(
            high, low, FLOW_CONTROL_HIGH_WATER)

        self._maybe_pause_protocol()

    def get_write_buffer_limits(self):
        return (self._low_water, self._high_water)

    def get_extra_info(self, name, default=None):
        if self._extra_info is not None and name in self._extra_info:
            return self._extra_info[name]
        if name == 'socket':
            return self._get_socket()
        if name == 'sockname':
            return self._get_socket().getsockname()
        if name == 'peername':
            try:
                return self._get_socket().getpeername()
            except socket_error:
                return default
        return default
```

## File: `uvloop/handles/check.pxd`
```
cdef class UVCheck(UVHandle):
    cdef:
        Handle h
        bint running

    # All "inline" methods are final

    cdef _init(self, Loop loop, Handle h)

    cdef inline stop(self)
    cdef inline start(self)

    @staticmethod
    cdef UVCheck new(Loop loop, Handle h)
```

## File: `uvloop/handles/check.pyx`
```
@cython.no_gc_clear
cdef class UVCheck(UVHandle):
    cdef _init(self, Loop loop, Handle h):
        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*>PyMem_RawMalloc(sizeof(uv.uv_check_t))
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        err = uv.uv_check_init(self._loop.uvloop, <uv.uv_check_t*>self._handle)
        if err < 0:
            self._abort_init()
            raise convert_error(err)

        self._finish_init()

        self.h = h
        self.running = 0

    cdef inline stop(self):
        cdef int err

        if not self._is_alive():
            self.running = 0
            return

        if self.running == 1:
            err = uv.uv_check_stop(<uv.uv_check_t*>self._handle)
            self.running = 0
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return

    cdef inline start(self):
        cdef int err

        self._ensure_alive()

        if self.running == 0:
            err = uv.uv_check_start(<uv.uv_check_t*>self._handle,
                                    cb_check_callback)
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return
            self.running = 1

    @staticmethod
    cdef UVCheck new(Loop loop, Handle h):
        cdef UVCheck handle
        handle = UVCheck.__new__(UVCheck)
        handle._init(loop, h)
        return handle


cdef void cb_check_callback(
    uv.uv_check_t* handle,
) noexcept with gil:
    if __ensure_handle_data(<uv.uv_handle_t*>handle, "UVCheck callback") == 0:
        return

    cdef:
        UVCheck check = <UVCheck> handle.data
        Handle h = check.h
    try:
        h._run()
    except BaseException as ex:
        check._error(ex, False)
```

## File: `uvloop/handles/fsevent.pxd`
```
cdef class UVFSEvent(UVHandle):
    cdef:
        object callback
        bint running

    cdef _init(self, Loop loop, object callback, object context)
    cdef _close(self)
    cdef start(self, char* path, int flags)
    cdef stop(self)

    @staticmethod
    cdef UVFSEvent new(Loop loop, object callback, object context)
```

## File: `uvloop/handles/fsevent.pyx`
```
import enum


class FileSystemEvent(enum.IntEnum):
    RENAME = uv.UV_RENAME
    CHANGE = uv.UV_CHANGE
    RENAME_CHANGE = RENAME | CHANGE


@cython.no_gc_clear
cdef class UVFSEvent(UVHandle):
    cdef _init(self, Loop loop, object callback, object context):
        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*>PyMem_RawMalloc(
            sizeof(uv.uv_fs_event_t)
        )
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        err = uv.uv_fs_event_init(
            self._loop.uvloop, <uv.uv_fs_event_t*>self._handle
        )
        if err < 0:
            self._abort_init()
            raise convert_error(err)

        self._finish_init()

        self.running = 0
        self.callback = callback
        if context is None:
            context = Context_CopyCurrent()
        self.context = context

    cdef start(self, char* path, int flags):
        cdef int err

        self._ensure_alive()

        if self.running == 0:
            err = uv.uv_fs_event_start(
                <uv.uv_fs_event_t*>self._handle,
                __uvfsevent_callback,
                path,
                flags,
            )
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return
            self.running = 1

    cdef stop(self):
        cdef int err

        if not self._is_alive():
            self.running = 0
            return

        if self.running == 1:
            err = uv.uv_fs_event_stop(<uv.uv_fs_event_t*>self._handle)
            self.running = 0
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return

    cdef _close(self):
        try:
            self.stop()
        finally:
            UVHandle._close(<UVHandle>self)

    def cancel(self):
        self._close()

    def cancelled(self):
        return self.running == 0

    @staticmethod
    cdef UVFSEvent new(Loop loop, object callback, object context):
        cdef UVFSEvent handle
        handle = UVFSEvent.__new__(UVFSEvent)
        handle._init(loop, callback, context)
        return handle


cdef void __uvfsevent_callback(
    uv.uv_fs_event_t* handle,
    const char *filename,
    int events,
    int status,
) noexcept with gil:
    if __ensure_handle_data(
        <uv.uv_handle_t*>handle, "UVFSEvent callback"
    ) == 0:
        return

    cdef:
        UVFSEvent fs_event = <UVFSEvent> handle.data
        Handle h

    try:
        h = new_Handle(
            fs_event._loop,
            fs_event.callback,
            (filename, FileSystemEvent(events)),
            fs_event.context,
        )
        h._run()
    except BaseException as ex:
        fs_event._error(ex, False)
```

## File: `uvloop/handles/handle.pxd`
```
cdef class UVHandle:
    cdef:
        uv.uv_handle_t *_handle
        Loop _loop
        readonly _source_traceback
        bint _closed
        bint _inited
        object context

        # Added to enable current UDPTransport implementation,
        # which doesn't use libuv handles.
        bint _has_handle

    # All "inline" methods are final

    cdef inline _start_init(self, Loop loop)
    cdef inline _abort_init(self)
    cdef inline _finish_init(self)

    cdef inline bint _is_alive(self)
    cdef inline _ensure_alive(self)

    cdef _error(self, exc, throw)
    cdef _fatal_error(self, exc, throw, reason=?)

    cdef _warn_unclosed(self)

    cdef _free(self)
    cdef _close(self)


cdef class UVSocketHandle(UVHandle):
    cdef:
        # Points to a Python file-object that should be closed
        # when the transport is closing.  Used by pipes.  This
        # should probably be refactored somehow.
        object _fileobj
        object __cached_socket

    # All "inline" methods are final

    cdef _fileno(self)

    cdef _new_socket(self)
    cdef inline _get_socket(self)
    cdef inline _attach_fileobj(self, object file)

    cdef _open(self, int sockfd)
```

## File: `uvloop/handles/handle.pyx`
```
cdef class UVHandle:
    """A base class for all libuv handles.

    Automatically manages memory deallocation and closing.

    Important:

       1. call "_ensure_alive()" before calling any libuv functions on
          your handles.

       2. call "__ensure_handle_data" in *all* libuv handle callbacks.
    """

    def __cinit__(self):
        self._closed = 0
        self._inited = 0
        self._has_handle = 1
        self._handle = NULL
        self._loop = None
        self._source_traceback = None

    def __init__(self):
        raise TypeError(
            '{} is not supposed to be instantiated from Python'.format(
                self.__class__.__name__))

    def __dealloc__(self):
        if UVLOOP_DEBUG:
            if self._loop is not None:
                if self._inited:
                    self._loop._debug_handles_current.subtract([
                        self.__class__.__name__])
            else:
                # No "@cython.no_gc_clear" decorator on this UVHandle
                raise RuntimeError(
                    '{} without @no_gc_clear; loop was set to None by GC'
                    .format(self.__class__.__name__))

        if self._handle is NULL:
            return

        # -> When we're at this point, something is wrong <-

        if self._handle.loop is NULL:
            # The handle wasn't initialized with "uv_{handle}_init"
            self._closed = 1
            self._free()
            raise RuntimeError(
                '{} is open in __dealloc__ with loop set to NULL'
                .format(self.__class__.__name__))

        if self._closed:
            # So _handle is not NULL and self._closed == 1?
            raise RuntimeError(
                '{}.__dealloc__: _handle is NULL, _closed == 1'.format(
                    self.__class__.__name__))

        # The handle is dealloced while open.  Let's try to close it.
        # Situations when this is possible include unhandled exceptions,
        # errors during Handle.__cinit__/__init__ etc.
        if self._inited:
            self._handle.data = NULL
            uv.uv_close(self._handle, __uv_close_handle_cb)  # void; no errors
            self._handle = NULL
            self._warn_unclosed()
        else:
            # The handle was allocated, but not initialized
            self._closed = 1
            self._free()

    cdef _free(self):
        if self._handle == NULL:
            return

        if UVLOOP_DEBUG and self._inited:
            self._loop._debug_uv_handles_freed += 1

        PyMem_RawFree(self._handle)
        self._handle = NULL

    cdef _warn_unclosed(self):
        if self._source_traceback is not None:
            try:
                tb = ''.join(tb_format_list(self._source_traceback))
                tb = 'object created at (most recent call last):\n{}'.format(
                    tb.rstrip())
            except Exception as ex:
                msg = (
                    'unclosed resource {!r}; could not serialize '
                    'debug traceback: {}: {}'
                ).format(self, type(ex).__name__, ex)
            else:
                msg = 'unclosed resource {!r}; {}'.format(self, tb)
        else:
            msg = 'unclosed resource {!r}'.format(self)
        warnings_warn(msg, ResourceWarning)

    cdef inline _abort_init(self):
        if self._handle is not NULL:
            self._free()

        try:
            if UVLOOP_DEBUG:
                name = self.__class__.__name__
                if self._inited:
                    raise RuntimeError(
                        '_abort_init: {}._inited is set'.format(name))
                if self._closed:
                    raise RuntimeError(
                        '_abort_init: {}._closed is set'.format(name))
        finally:
            self._closed = 1

    cdef inline _finish_init(self):
        self._inited = 1
        if self._has_handle == 1:
            self._handle.data = <void*>self
        if self._loop._debug:
            self._source_traceback = extract_stack()
        if UVLOOP_DEBUG:
            cls_name = self.__class__.__name__
            self._loop._debug_uv_handles_total += 1
            self._loop._debug_handles_total.update([cls_name])
            self._loop._debug_handles_current.update([cls_name])

    cdef inline _start_init(self, Loop loop):
        if UVLOOP_DEBUG:
            if self._loop is not None:
                raise RuntimeError(
                    '{}._start_init can only be called once'.format(
                        self.__class__.__name__))

        self._loop = loop

    cdef inline bint _is_alive(self):
        cdef bint res
        res = self._closed != 1 and self._inited == 1
        if UVLOOP_DEBUG:
            if res and self._has_handle == 1:
                name = self.__class__.__name__
                if self._handle is NULL:
                    raise RuntimeError(
                        '{} is alive, but _handle is NULL'.format(name))
                if self._loop is None:
                    raise RuntimeError(
                        '{} is alive, but _loop is None'.format(name))
                if self._handle.loop is not self._loop.uvloop:
                    raise RuntimeError(
                        '{} is alive, but _handle.loop is not '
                        'initialized'.format(name))
                if self._handle.data is not <void*>self:
                    raise RuntimeError(
                        '{} is alive, but _handle.data is not '
                        'initialized'.format(name))
        return res

    cdef inline _ensure_alive(self):
        if not self._is_alive():
            raise RuntimeError(
                'unable to perform operation on {!r}; '
                'the handler is closed'.format(self))

    cdef _fatal_error(self, exc, throw, reason=None):
        # Fatal error means an error that was returned by the
        # underlying libuv handle function.  We usually can't
        # recover from that, hence we just close the handle.
        self._close()

        if throw or self._loop is None:
            raise exc
        else:
            self._loop._handle_exception(exc)

    cdef _error(self, exc, throw):
        # A non-fatal error is usually an error that was caught
        # by the handler, but was originated in the client code
        # (not in libuv).  In this case we either want to simply
        # raise or log it.
        if throw or self._loop is None:
            raise exc
        else:
            self._loop._handle_exception(exc)

    cdef _close(self):
        if self._closed == 1:
            return

        self._closed = 1

        if self._handle is NULL:
            return

        if UVLOOP_DEBUG:
            if self._handle.data is NULL:
                raise RuntimeError(
                    '{}._close: _handle.data is NULL'.format(
                        self.__class__.__name__))

            if <object>self._handle.data is not self:
                raise RuntimeError(
                    '{}._close: _handle.data is not UVHandle/self'.format(
                        self.__class__.__name__))

            if uv.uv_is_closing(self._handle):
                raise RuntimeError(
                    '{}._close: uv_is_closing() is true'.format(
                        self.__class__.__name__))

        # We want the handle wrapper (UVHandle) to stay alive until
        # the closing callback fires.
        Py_INCREF(self)
        uv.uv_close(self._handle, __uv_close_handle_cb)  # void; no errors

    def __repr__(self):
        return '<{} closed={} {:#x}>'.format(
            self.__class__.__name__,
            self._closed,
            id(self))


cdef class UVSocketHandle(UVHandle):

    def __cinit__(self):
        self._fileobj = None
        self.__cached_socket = None

    cdef _fileno(self):
        cdef:
            int fd
            int err

        self._ensure_alive()
        err = uv.uv_fileno(self._handle, <uv.uv_os_fd_t*>&fd)
        if err < 0:
            raise convert_error(err)

        return fd

    cdef _new_socket(self):
        raise NotImplementedError

    cdef inline _get_socket(self):
        if self.__cached_socket is not None:
            return self.__cached_socket

        if not self._is_alive():
            return None

        self.__cached_socket = self._new_socket()
        if UVLOOP_DEBUG:
            # We don't "dup" for the "__cached_socket".
            assert self.__cached_socket.fileno() == self._fileno()
        return self.__cached_socket

    cdef inline _attach_fileobj(self, object file):
        # When we create a TCP/PIPE/etc connection/server based on
        # a Python file object, we need to close the file object when
        # the uv handle is closed.
        socket_inc_io_ref(file)
        self._fileobj = file

    cdef _close(self):
        if self.__cached_socket is not None:
            (<PseudoSocket>self.__cached_socket)._fd = -1

        UVHandle._close(self)

        try:
            # This code will only run for transports created from
            # Python sockets, i.e. with `loop.create_server(sock=sock)` etc.
            if self._fileobj is not None:
                if isinstance(self._fileobj, socket_socket):
                    # Detaching the socket object is the ideal solution:
                    # * libuv will actually close the FD;
                    # * detach() call will reset FD for the Python socket
                    #   object, which means that it won't be closed 2nd time
                    #   when the socket object is GCed.
                    #
                    # No need to call `socket_dec_io_ref()`, as
                    # `socket.detach()` ignores `socket._io_refs`.
                    self._fileobj.detach()
                else:
                    try:
                        # `socket.close()` will raise an EBADF because libuv
                        # has already closed the underlying FD.
                        self._fileobj.close()
                    except OSError as ex:
                        if ex.errno != errno_EBADF:
                            raise
        except Exception as ex:
            self._loop.call_exception_handler({
                'exception': ex,
                'transport': self,
                'message': f'could not close attached file object '
                           f'{self._fileobj!r}',
            })
        finally:
            self._fileobj = None

    cdef _open(self, int sockfd):
        raise NotImplementedError


cdef inline bint __ensure_handle_data(uv.uv_handle_t* handle,
                                      const char* handle_ctx):

    cdef Loop loop

    if UVLOOP_DEBUG:
        if handle.loop is NULL:
            raise RuntimeError(
                'handle.loop is NULL in __ensure_handle_data')

        if handle.loop.data is NULL:
            raise RuntimeError(
                'handle.loop.data is NULL in __ensure_handle_data')

    if handle.data is NULL:
        loop = <Loop>handle.loop.data
        loop.call_exception_handler({
            'message': '{} called with handle.data == NULL'.format(
                handle_ctx.decode('latin-1'))
        })
        return 0

    if handle.data is NULL:
        # The underlying UVHandle object was GCed with an open uv_handle_t.
        loop = <Loop>handle.loop.data
        loop.call_exception_handler({
            'message': '{} called after destroying the UVHandle'.format(
                handle_ctx.decode('latin-1'))
        })
        return 0

    return 1


cdef void __uv_close_handle_cb(uv.uv_handle_t* handle) noexcept with gil:
    cdef UVHandle h

    if handle.data is NULL:
        # The original UVHandle is long dead. Just free the mem of
        # the uv_handle_t* handler.

        if UVLOOP_DEBUG:
            if handle.loop == NULL or handle.loop.data == NULL:
                raise RuntimeError(
                    '__uv_close_handle_cb: handle.loop is invalid')
            (<Loop>handle.loop.data)._debug_uv_handles_freed += 1

        PyMem_RawFree(handle)
    else:
        h = <UVHandle>handle.data
        try:
            if UVLOOP_DEBUG:
                if not h._has_handle:
                    raise RuntimeError(
                        'has_handle=0 in __uv_close_handle_cb')
                h._loop._debug_handles_closed.update([
                    h.__class__.__name__])
            h._free()
        finally:
            Py_DECREF(h)  # Was INCREFed in UVHandle._close


cdef void __close_all_handles(Loop loop) noexcept:
    uv.uv_walk(loop.uvloop,
               __uv_walk_close_all_handles_cb,
               <void*>loop)  # void


cdef void __uv_walk_close_all_handles_cb(
    uv.uv_handle_t* handle,
    void* arg,
) noexcept with gil:

    cdef:
        Loop loop = <Loop>arg
        UVHandle h

    if uv.uv_is_closing(handle):
        # The handle is closed or is closing.
        return

    if handle.data is NULL:
        # This shouldn't happen. Ever.
        loop.call_exception_handler({
            'message': 'handle.data is NULL in __close_all_handles_cb'
        })
        return

    h = <UVHandle>handle.data
    if not h._closed:
        h._warn_unclosed()
        h._close()
```

## File: `uvloop/handles/idle.pxd`
```
cdef class UVIdle(UVHandle):
    cdef:
        Handle h
        bint running

    # All "inline" methods are final

    cdef _init(self, Loop loop, Handle h)

    cdef inline stop(self)
    cdef inline start(self)

    @staticmethod
    cdef UVIdle new(Loop loop, Handle h)
```

## File: `uvloop/handles/idle.pyx`
```
@cython.no_gc_clear
cdef class UVIdle(UVHandle):
    cdef _init(self, Loop loop, Handle h):
        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*>PyMem_RawMalloc(sizeof(uv.uv_idle_t))
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        err = uv.uv_idle_init(self._loop.uvloop, <uv.uv_idle_t*>self._handle)
        if err < 0:
            self._abort_init()
            raise convert_error(err)

        self._finish_init()

        self.h = h
        self.running = 0

    cdef inline stop(self):
        cdef int err

        if not self._is_alive():
            self.running = 0
            return

        if self.running == 1:
            err = uv.uv_idle_stop(<uv.uv_idle_t*>self._handle)
            self.running = 0
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return

    cdef inline start(self):
        cdef int err

        self._ensure_alive()

        if self.running == 0:
            err = uv.uv_idle_start(<uv.uv_idle_t*>self._handle,
                                   cb_idle_callback)
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return
            self.running = 1

    @staticmethod
    cdef UVIdle new(Loop loop, Handle h):
        cdef UVIdle handle
        handle = UVIdle.__new__(UVIdle)
        handle._init(loop, h)
        return handle


cdef void cb_idle_callback(
    uv.uv_idle_t* handle,
) noexcept with gil:
    if __ensure_handle_data(<uv.uv_handle_t*>handle, "UVIdle callback") == 0:
        return

    cdef:
        UVIdle idle = <UVIdle> handle.data
        Handle h = idle.h
    try:
        h._run()
    except BaseException as ex:
        idle._error(ex, False)
```

## File: `uvloop/handles/pipe.pxd`
```
cdef class UnixServer(UVStreamServer):

    cdef bind(self, str path)

    @staticmethod
    cdef UnixServer new(Loop loop, object protocol_factory, Server server,
                        object backlog,
                        object ssl,
                        object ssl_handshake_timeout,
                        object ssl_shutdown_timeout)


cdef class UnixTransport(UVStream):

    @staticmethod
    cdef UnixTransport new(Loop loop, object protocol, Server server,
                           object waiter, object context)

    cdef connect(self, char* addr)


cdef class ReadUnixTransport(UVStream):

    @staticmethod
    cdef ReadUnixTransport new(Loop loop, object protocol, Server server,
                               object waiter)


cdef class WriteUnixTransport(UVStream):

    @staticmethod
    cdef WriteUnixTransport new(Loop loop, object protocol, Server server,
                                object waiter)
```

## File: `uvloop/handles/pipe.pyx`
```
cdef __pipe_init_uv_handle(UVStream handle, Loop loop):
    cdef int err

    handle._handle = <uv.uv_handle_t*>PyMem_RawMalloc(sizeof(uv.uv_pipe_t))
    if handle._handle is NULL:
        handle._abort_init()
        raise MemoryError()

    # Initialize pipe handle with ipc=0.
    # ipc=1 means that libuv will use recvmsg/sendmsg
    # instead of recv/send.
    err = uv.uv_pipe_init(handle._loop.uvloop,
                          <uv.uv_pipe_t*>handle._handle,
                          0)
    # UV_HANDLE_READABLE allows calling uv_read_start() on this pipe
    # even if it is O_WRONLY, see also #317, libuv/libuv#2058
    handle._handle.flags |= uv.UV_INTERNAL_HANDLE_READABLE
    if err < 0:
        handle._abort_init()
        raise convert_error(err)

    handle._finish_init()


cdef __pipe_open(UVStream handle, int fd):
    cdef int err
    err = uv.uv_pipe_open(<uv.uv_pipe_t *>handle._handle,
                          <uv.uv_os_fd_t>fd)
    if err < 0:
        exc = convert_error(err)
        raise exc


cdef __pipe_get_socket(UVSocketHandle handle):
    fileno = handle._fileno()
    return PseudoSocket(uv.AF_UNIX, uv.SOCK_STREAM, 0, fileno)


@cython.no_gc_clear
cdef class UnixServer(UVStreamServer):

    @staticmethod
    cdef UnixServer new(Loop loop, object protocol_factory, Server server,
                        object backlog,
                        object ssl,
                        object ssl_handshake_timeout,
                        object ssl_shutdown_timeout):

        cdef UnixServer handle
        handle = UnixServer.__new__(UnixServer)
        handle._init(loop, protocol_factory, server, backlog,
                     ssl, ssl_handshake_timeout, ssl_shutdown_timeout)
        __pipe_init_uv_handle(<UVStream>handle, loop)
        return handle

    cdef _new_socket(self):
        return __pipe_get_socket(<UVSocketHandle>self)

    cdef _open(self, int sockfd):
        self._ensure_alive()
        __pipe_open(<UVStream>self, sockfd)
        self._mark_as_open()

    cdef bind(self, str path):
        cdef int err
        self._ensure_alive()
        err = uv.uv_pipe_bind(<uv.uv_pipe_t *>self._handle,
                              path.encode())
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return

        self._mark_as_open()

    cdef UVStream _make_new_transport(self, object protocol, object waiter,
                                      object context):
        cdef UnixTransport tr
        tr = UnixTransport.new(self._loop, protocol, self._server, waiter,
                               context)
        return <UVStream>tr

    cdef _close(self):
        sock = self._fileobj
        if sock is not None and sock in self._loop._unix_server_sockets:
            path = sock.getsockname()
        else:
            path = None

        UVStreamServer._close(self)

        if path is not None:
            prev_ino = self._loop._unix_server_sockets[sock]
            del self._loop._unix_server_sockets[sock]
            try:
                if os_stat(path).st_ino == prev_ino:
                    os_unlink(path)
            except FileNotFoundError:
                pass
            except OSError as err:
                aio_logger.error('Unable to clean up listening UNIX socket '
                                 '%r: %r', path, err)


@cython.no_gc_clear
cdef class UnixTransport(UVStream):

    @staticmethod
    cdef UnixTransport new(Loop loop, object protocol, Server server,
                           object waiter, object context):

        cdef UnixTransport handle
        handle = UnixTransport.__new__(UnixTransport)
        handle._init(loop, protocol, server, waiter, context)
        __pipe_init_uv_handle(<UVStream>handle, loop)
        return handle

    cdef _new_socket(self):
        return __pipe_get_socket(<UVSocketHandle>self)

    cdef _open(self, int sockfd):
        __pipe_open(<UVStream>self, sockfd)

    cdef connect(self, char* addr):
        cdef _PipeConnectRequest req
        req = _PipeConnectRequest(self._loop, self)
        req.connect(addr)


@cython.no_gc_clear
cdef class ReadUnixTransport(UVStream):

    @staticmethod
    cdef ReadUnixTransport new(Loop loop, object protocol, Server server,
                               object waiter):
        cdef ReadUnixTransport handle
        handle = ReadUnixTransport.__new__(ReadUnixTransport)
        # This is only used in connect_read_pipe() and subprocess_shell/exec()
        # directly, we could simply copy the current context.
        handle._init(loop, protocol, server, waiter, Context_CopyCurrent())
        __pipe_init_uv_handle(<UVStream>handle, loop)
        return handle

    cdef _new_socket(self):
        return __pipe_get_socket(<UVSocketHandle>self)

    cdef _open(self, int sockfd):
        __pipe_open(<UVStream>self, sockfd)

    def get_write_buffer_limits(self):
        raise NotImplementedError

    def set_write_buffer_limits(self, high=None, low=None):
        raise NotImplementedError

    def get_write_buffer_size(self):
        raise NotImplementedError

    def write(self, data):
        raise NotImplementedError

    def writelines(self, list_of_data):
        raise NotImplementedError

    def write_eof(self):
        raise NotImplementedError

    def can_write_eof(self):
        raise NotImplementedError

    def abort(self):
        raise NotImplementedError


@cython.no_gc_clear
cdef class WriteUnixTransport(UVStream):

    @staticmethod
    cdef WriteUnixTransport new(Loop loop, object protocol, Server server,
                                object waiter):
        cdef WriteUnixTransport handle
        handle = WriteUnixTransport.__new__(WriteUnixTransport)

        # We listen for read events on write-end of the pipe. When
        # the read-end is close, the uv_stream_t.read callback will
        # receive an error -- we want to silence that error, and just
        # close the transport.
        handle._close_on_read_error()

        # This is only used in connect_write_pipe() and subprocess_shell/exec()
        # directly, we could simply copy the current context.
        handle._init(loop, protocol, server, waiter, Context_CopyCurrent())
        __pipe_init_uv_handle(<UVStream>handle, loop)
        return handle

    cdef _new_socket(self):
        return __pipe_get_socket(<UVSocketHandle>self)

    cdef _open(self, int sockfd):
        __pipe_open(<UVStream>self, sockfd)

    def pause_reading(self):
        raise NotImplementedError

    def resume_reading(self):
        raise NotImplementedError


cdef class _PipeConnectRequest(UVRequest):
    cdef:
        UnixTransport transport
        uv.uv_connect_t _req_data

    def __cinit__(self, loop, transport):
        self.request = <uv.uv_req_t*> &self._req_data
        self.request.data = <void*>self
        self.transport = transport

    cdef connect(self, char* addr):
        # uv_pipe_connect returns void
        uv.uv_pipe_connect(<uv.uv_connect_t*>self.request,
                           <uv.uv_pipe_t*>self.transport._handle,
                           addr,
                           __pipe_connect_callback)

cdef void __pipe_connect_callback(
    uv.uv_connect_t* req,
    int status,
) noexcept with gil:
    cdef:
        _PipeConnectRequest wrapper
        UnixTransport transport

    wrapper = <_PipeConnectRequest> req.data
    transport = wrapper.transport

    if status < 0:
        exc = convert_error(status)
    else:
        exc = None

    try:
        transport._on_connect(exc)
    except BaseException as ex:
        wrapper.transport._fatal_error(ex, False)
    finally:
        wrapper.on_done()
```

## File: `uvloop/handles/poll.pxd`
```
cdef class UVPoll(UVHandle):
    cdef:
        int fd
        Handle reading_handle
        Handle writing_handle

    cdef _init(self, Loop loop, int fd)
    cdef _close(self)

    cdef inline _poll_start(self, int flags)
    cdef inline _poll_stop(self)

    cdef int is_active(self) noexcept

    cdef is_reading(self)
    cdef is_writing(self)

    cdef start_reading(self, Handle callback)
    cdef start_writing(self, Handle callback)
    cdef stop_reading(self)
    cdef stop_writing(self)
    cdef stop(self)

    @staticmethod
    cdef UVPoll new(Loop loop, int fd)
```

## File: `uvloop/handles/poll.pyx`
```
@cython.no_gc_clear
cdef class UVPoll(UVHandle):
    cdef _init(self, Loop loop, int fd):
        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*>PyMem_RawMalloc(sizeof(uv.uv_poll_t))
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        err = uv.uv_poll_init(self._loop.uvloop,
                              <uv.uv_poll_t *>self._handle, fd)
        if err < 0:
            self._abort_init()
            raise convert_error(err)

        self._finish_init()

        self.fd = fd
        self.reading_handle = None
        self.writing_handle = None

    @staticmethod
    cdef UVPoll new(Loop loop, int fd):
        cdef UVPoll handle
        handle = UVPoll.__new__(UVPoll)
        handle._init(loop, fd)
        return handle

    cdef int is_active(self) noexcept:
        return (self.reading_handle is not None or
                self.writing_handle is not None)

    cdef inline _poll_start(self, int flags):
        cdef int err

        self._ensure_alive()

        err = uv.uv_poll_start(
            <uv.uv_poll_t*>self._handle,
            flags,
            __on_uvpoll_event)

        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return

    cdef inline _poll_stop(self):
        cdef int err

        if not self._is_alive():
            return

        err = uv.uv_poll_stop(<uv.uv_poll_t*>self._handle)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return

        cdef:
            int backend_id
            system.epoll_event dummy_event

        if system.PLATFORM_IS_LINUX:
            # libuv doesn't remove the FD from epoll immediately
            # after uv_poll_stop or uv_poll_close, causing hard
            # to debug issue with dup-ed file descriptors causing
            # CPU burn in epoll/epoll_ctl:
            #    https://github.com/MagicStack/uvloop/issues/61
            #
            # It's safe though to manually call epoll_ctl here,
            # after calling uv_poll_stop.

            backend_id = uv.uv_backend_fd(self._loop.uvloop)
            if backend_id != -1:
                memset(&dummy_event, 0, sizeof(dummy_event))
                system.epoll_ctl(
                    backend_id,
                    system.EPOLL_CTL_DEL,
                    self.fd,
                    &dummy_event)  # ignore errors

    cdef is_reading(self):
        return self._is_alive() and self.reading_handle is not None

    cdef is_writing(self):
        return self._is_alive() and self.writing_handle is not None

    cdef start_reading(self, Handle callback):
        cdef:
            int mask = 0

        if self.reading_handle is None:
            # not reading right now, setup the handle

            mask = uv.UV_READABLE
            if self.writing_handle is not None:
                # are we writing right now?
                mask |= uv.UV_WRITABLE

            self._poll_start(mask)
        else:
            self.reading_handle._cancel()

        self.reading_handle = callback

    cdef start_writing(self, Handle callback):
        cdef:
            int mask = 0

        if self.writing_handle is None:
            # not writing right now, setup the handle

            mask = uv.UV_WRITABLE
            if self.reading_handle is not None:
                # are we reading right now?
                mask |= uv.UV_READABLE

            self._poll_start(mask)
        else:
            self.writing_handle._cancel()

        self.writing_handle = callback

    cdef stop_reading(self):
        if self.reading_handle is None:
            return False

        self.reading_handle._cancel()
        self.reading_handle = None

        if self.writing_handle is None:
            self.stop()
        else:
            self._poll_start(uv.UV_WRITABLE)

        return True

    cdef stop_writing(self):
        if self.writing_handle is None:
            return False

        self.writing_handle._cancel()
        self.writing_handle = None

        if self.reading_handle is None:
            self.stop()
        else:
            self._poll_start(uv.UV_READABLE)

        return True

    cdef stop(self):
        if self.reading_handle is not None:
            self.reading_handle._cancel()
            self.reading_handle = None

        if self.writing_handle is not None:
            self.writing_handle._cancel()
            self.writing_handle = None

        self._poll_stop()

    cdef _close(self):
        if self.is_active():
            self.stop()

        UVHandle._close(<UVHandle>self)

    cdef _fatal_error(self, exc, throw, reason=None):
        try:
            if self.reading_handle is not None:
                try:
                    self.reading_handle._run()
                except BaseException as ex:
                    self._loop._handle_exception(ex)
                self.reading_handle = None

            if self.writing_handle is not None:
                try:
                    self.writing_handle._run()
                except BaseException as ex:
                    self._loop._handle_exception(ex)
                self.writing_handle = None

        finally:
            self._close()


cdef void __on_uvpoll_event(
    uv.uv_poll_t* handle,
    int status,
    int events,
) noexcept with gil:

    if __ensure_handle_data(<uv.uv_handle_t*>handle, "UVPoll callback") == 0:
        return

    cdef:
        UVPoll poll = <UVPoll> handle.data

    if status < 0:
        exc = convert_error(status)
        poll._fatal_error(exc, False)
        return

    if ((events & (uv.UV_READABLE | uv.UV_DISCONNECT)) and
            poll.reading_handle is not None):

        try:
            if UVLOOP_DEBUG:
                poll._loop._poll_read_events_total += 1
            poll.reading_handle._run()
        except BaseException as ex:
            if UVLOOP_DEBUG:
                poll._loop._poll_read_cb_errors_total += 1
            poll._error(ex, False)
            # continue code execution

    if ((events & (uv.UV_WRITABLE | uv.UV_DISCONNECT)) and
            poll.writing_handle is not None):

        try:
            if UVLOOP_DEBUG:
                poll._loop._poll_write_events_total += 1
            poll.writing_handle._run()
        except BaseException as ex:
            if UVLOOP_DEBUG:
                poll._loop._poll_write_cb_errors_total += 1
            poll._error(ex, False)
```

## File: `uvloop/handles/process.pxd`
```
cdef class UVProcess(UVHandle):
    cdef:
        object _returncode
        object _pid

        object _errpipe_read
        object _errpipe_write
        object _preexec_fn
        bint _restore_signals

        list _fds_to_close

        # Attributes used to compose uv_process_options_t:
        uv.uv_process_options_t options
        uv.uv_stdio_container_t[3] iocnt
        list __env
        char **uv_opt_env
        list __args
        char **uv_opt_args
        char *uv_opt_file
        bytes __cwd

    cdef _close_process_handle(self)

    cdef _init(self, Loop loop, list args, dict env, cwd,
               start_new_session,
               _stdin, _stdout, _stderr, pass_fds,
               debug_flags, preexec_fn, restore_signals)

    cdef _after_fork(self)

    cdef char** __to_cstring_array(self, list arr)
    cdef _init_args(self, list args)
    cdef _init_env(self, dict env)
    cdef _init_files(self, _stdin, _stdout, _stderr)
    cdef _init_options(self, list args, dict env, cwd, start_new_session,
                       _stdin, _stdout, _stderr, bint force_fork)

    cdef _close_after_spawn(self, int fd)

    cdef _on_exit(self, int64_t exit_status, int term_signal)
    cdef _kill(self, int signum)


cdef class UVProcessTransport(UVProcess):
    cdef:
        list _exit_waiters
        list _init_futs
        bint _stdio_ready
        list _pending_calls
        object _protocol
        bint _finished

        WriteUnixTransport _stdin
        ReadUnixTransport _stdout
        ReadUnixTransport _stderr

        object stdin_proto
        object stdout_proto
        object stderr_proto

    cdef _file_redirect_stdio(self, int fd)
    cdef _file_devnull(self)
    cdef _file_inpipe(self)
    cdef _file_outpipe(self)

    cdef _check_proc(self)
    cdef _pipe_connection_lost(self, int fd, exc)
    cdef _pipe_data_received(self, int fd, data)

    cdef _call_connection_made(self, waiter)
    cdef _try_finish(self)

    @staticmethod
    cdef UVProcessTransport new(Loop loop, protocol, args, env, cwd,
                                start_new_session,
                                _stdin, _stdout, _stderr, pass_fds,
                                waiter,
                                debug_flags,
                                preexec_fn, restore_signals)
```

## File: `uvloop/handles/process.pyx`
```
@cython.no_gc_clear
cdef class UVProcess(UVHandle):
    """Abstract class; wrapper over uv_process_t handle."""

    def __cinit__(self):
        self.uv_opt_env = NULL
        self.uv_opt_args = NULL
        self._returncode = None
        self._pid = None
        self._fds_to_close = list()
        self._preexec_fn = None
        self._restore_signals = True
        self.context = Context_CopyCurrent()

    cdef _close_process_handle(self):
        # XXX: This is a workaround for a libuv bug:
        # - https://github.com/libuv/libuv/issues/1933
        # - https://github.com/libuv/libuv/pull/551
        if self._handle is NULL:
            return
        self._handle.data = NULL
        uv.uv_close(self._handle, __uv_close_process_handle_cb)
        self._handle = NULL  # close callback will free() the memory

    cdef _init(self, Loop loop, list args, dict env,
               cwd, start_new_session,
               _stdin, _stdout, _stderr,  # std* can be defined as macros in C
               pass_fds, debug_flags, preexec_fn, restore_signals):

        global __forking
        global __forking_loop
        global __forkHandler

        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*>PyMem_RawMalloc(
            sizeof(uv.uv_process_t))
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        # Too early to call _finish_init, but still a lot of work to do.
        # Let's set handle.data to NULL, so in case something goes wrong,
        # callbacks have a chance to avoid casting *something* into UVHandle.
        self._handle.data = NULL

        force_fork = False
        if system.PLATFORM_IS_APPLE and not (
            preexec_fn is None
            and not pass_fds
        ):
            # see _execute_child() in CPython/subprocess.py
            force_fork = True

        try:
            self._init_options(args, env, cwd, start_new_session,
                               _stdin, _stdout, _stderr, force_fork)

            restore_inheritable = set()
            if pass_fds:
                for fd in pass_fds:
                    if not os_get_inheritable(fd):
                        restore_inheritable.add(fd)
                        os_set_inheritable(fd, True)
        except Exception:
            self._abort_init()
            raise

        if __forking or loop.active_process_handler is not None:
            # Our pthread_atfork handlers won't work correctly when
            # another loop is forking in another thread (even though
            # GIL should help us to avoid that.)
            self._abort_init()
            raise RuntimeError(
                'Racing with another loop to spawn a process.')

        self._errpipe_read, self._errpipe_write = os_pipe()
        fds_to_close = self._fds_to_close
        self._fds_to_close = None
        fds_to_close.append(self._errpipe_read)
        # add the write pipe last so we can close it early
        fds_to_close.append(self._errpipe_write)
        try:
            os_set_inheritable(self._errpipe_write, True)

            self._preexec_fn = preexec_fn
            self._restore_signals = restore_signals

            loop.active_process_handler = self
            __forking = 1
            __forking_loop = loop
            system.setForkHandler(<system.OnForkHandler>&__get_fork_handler)

            PyOS_BeforeFork()

            err = uv.uv_spawn(loop.uvloop,
                              <uv.uv_process_t*>self._handle,
                              &self.options)

            __forking = 0
            __forking_loop = None
            system.resetForkHandler()
            loop.active_process_handler = None

            PyOS_AfterFork_Parent()

            if err < 0:
                self._close_process_handle()
                self._abort_init()
                raise convert_error(err)

            self._finish_init()

            # close the write pipe early
            os_close(fds_to_close.pop())

            if preexec_fn is not None:
                errpipe_data = bytearray()
                while True:
                    # XXX: This is a blocking code that has to be
                    # rewritten (using loop.connect_read_pipe() or
                    # otherwise.)
                    part = os_read(self._errpipe_read, 50000)
                    errpipe_data += part
                    if not part or len(errpipe_data) > 50000:
                        break

        finally:
            while fds_to_close:
                os_close(fds_to_close.pop())

            for fd in restore_inheritable:
                os_set_inheritable(fd, False)

        # asyncio caches the PID in BaseSubprocessTransport,
        # so that the transport knows what the PID was even
        # after the process is finished.
        self._pid = (<uv.uv_process_t*>self._handle).pid

        # Track the process handle (create a strong ref to it)
        # to guarantee that __dealloc__ doesn't happen in an
        # uncontrolled fashion.  We want to wait until the process
        # exits and libuv calls __uvprocess_on_exit_callback,
        # which will call `UVProcess._close()`, which will, in turn,
        # untrack this handle.
        self._loop._track_process(self)

        if debug_flags & __PROCESS_DEBUG_SLEEP_AFTER_FORK:
            time_sleep(1)

        if preexec_fn is not None and errpipe_data:
            # preexec_fn has raised an exception.  The child
            # process must be dead now.
            try:
                exc_name, exc_msg = errpipe_data.split(b':', 1)
                exc_name = exc_name.decode()
                exc_msg = exc_msg.decode()
            except Exception:
                self._close()
                raise subprocess_SubprocessError(
                    'Bad exception data from child: {!r}'.format(
                        errpipe_data))
            exc_cls = getattr(__builtins__, exc_name,
                              subprocess_SubprocessError)

            exc = subprocess_SubprocessError(
                'Exception occurred in preexec_fn.')
            exc.__cause__ = exc_cls(exc_msg)
            self._close()
            raise exc

    cdef _after_fork(self):
        # See CPython/_posixsubprocess.c for details
        cdef int err

        if self._restore_signals:
            _Py_RestoreSignals()

        PyOS_AfterFork_Child()

        err = uv.uv_loop_fork(self._loop.uvloop)
        if err < 0:
            raise convert_error(err)

        if self._preexec_fn is not None:
            try:
                gc_disable()
                self._preexec_fn()
            except BaseException as ex:
                try:
                    with open(self._errpipe_write, 'wb') as f:
                        f.write(str(ex.__class__.__name__).encode())
                        f.write(b':')
                        f.write(str(ex.args[0]).encode())
                finally:
                    system._exit(255)
                    return
            else:
                os_close(self._errpipe_write)
        else:
            os_close(self._errpipe_write)

    cdef _close_after_spawn(self, int fd):
        if self._fds_to_close is None:
            raise RuntimeError(
                'UVProcess._close_after_spawn called after uv_spawn')
        self._fds_to_close.append(fd)

    def __dealloc__(self):
        if self.uv_opt_env is not NULL:
            PyMem_RawFree(self.uv_opt_env)
            self.uv_opt_env = NULL

        if self.uv_opt_args is not NULL:
            PyMem_RawFree(self.uv_opt_args)
            self.uv_opt_args = NULL

    cdef char** __to_cstring_array(self, list arr):
        cdef:
            int i
            ssize_t arr_len = len(arr)
            bytes el

            char **ret

        ret = <char **>PyMem_RawMalloc((arr_len + 1) * sizeof(char *))
        if ret is NULL:
            raise MemoryError()

        for i in range(arr_len):
            el = arr[i]
            # NB: PyBytes_AsString doesn't copy the data;
            # we have to be careful when the "arr" is GCed,
            # and it shouldn't be ever mutated.
            ret[i] = PyBytes_AsString(el)

        ret[arr_len] = NULL
        return ret

    cdef _init_options(self, list args, dict env, cwd, start_new_session,
                       _stdin, _stdout, _stderr, bint force_fork):

        memset(&self.options, 0, sizeof(uv.uv_process_options_t))

        self._init_env(env)
        self.options.env = self.uv_opt_env

        self._init_args(args)
        self.options.file = self.uv_opt_file
        self.options.args = self.uv_opt_args

        if start_new_session:
            self.options.flags |= uv.UV_PROCESS_DETACHED

        if force_fork:
            # This is a hack to work around the change in libuv 1.44:
            #    > macos: use posix_spawn instead of fork
            # where Python subprocess options like preexec_fn are
            # crippled. CPython only uses posix_spawn under a pretty
            # strict list of conditions (see subprocess.py), and falls
            # back to using fork() otherwise. We'd like to simulate such
            # behavior with libuv, but unfortunately libuv doesn't
            # provide explicit API to choose such implementation detail.
            # Based on current (libuv 1.46) behavior, setting
            # UV_PROCESS_SETUID or UV_PROCESS_SETGID would reliably make
            # libuv fallback to use fork, so let's just use it for now.
            self.options.flags |= uv.UV_PROCESS_SETUID
            self.options.uid = uv.getuid()

        if cwd is not None:
            cwd = os_fspath(cwd)

            if isinstance(cwd, str):
                cwd = PyUnicode_EncodeFSDefault(cwd)
            if not isinstance(cwd, bytes):
                raise ValueError('cwd must be a str or bytes object')

            self.__cwd = cwd
            self.options.cwd = PyBytes_AsString(self.__cwd)

        self.options.exit_cb = &__uvprocess_on_exit_callback

        self._init_files(_stdin, _stdout, _stderr)

    cdef _init_args(self, list args):
        cdef:
            bytes path
            int an = len(args)

        if an < 1:
            raise ValueError('cannot spawn a process: args are empty')

        self.__args = args.copy()
        for i in range(an):
            arg = os_fspath(args[i])
            if isinstance(arg, str):
                self.__args[i] = PyUnicode_EncodeFSDefault(arg)
            elif not isinstance(arg, bytes):
                raise TypeError('all args must be str or bytes')

        path = self.__args[0]
        self.uv_opt_file = PyBytes_AsString(path)
        self.uv_opt_args = self.__to_cstring_array(self.__args)

    cdef _init_env(self, dict env):
        if env is not None:
            self.__env = list()
            for key in env:
                val = env[key]

                if isinstance(key, str):
                    key = PyUnicode_EncodeFSDefault(key)
                elif not isinstance(key, bytes):
                    raise TypeError(
                        'all environment vars must be bytes or str')

                if isinstance(val, str):
                    val = PyUnicode_EncodeFSDefault(val)
                elif not isinstance(val, bytes):
                    raise TypeError(
                        'all environment values must be bytes or str')

                self.__env.append(key + b'=' + val)

            self.uv_opt_env = self.__to_cstring_array(self.__env)
        else:
            self.__env = None

    cdef _init_files(self, _stdin, _stdout, _stderr):
        self.options.stdio_count = 0

    cdef _kill(self, int signum):
        cdef int err
        self._ensure_alive()
        err = uv.uv_process_kill(<uv.uv_process_t*>self._handle, signum)
        if err < 0:
            raise convert_error(err)

    cdef _on_exit(self, int64_t exit_status, int term_signal):
        if term_signal:
            # From Python docs:
            #    A negative value -N indicates that the child was
            #    terminated by signal N (POSIX only).
            self._returncode = -term_signal
        else:
            self._returncode = exit_status

        self._close()

    cdef _close(self):
        try:
            if self._loop is not None:
                self._loop._untrack_process(self)
        finally:
            UVHandle._close(self)


DEF _CALL_PIPE_DATA_RECEIVED = 0
DEF _CALL_PIPE_CONNECTION_LOST = 1
DEF _CALL_PROCESS_EXITED = 2
DEF _CALL_CONNECTION_LOST = 3


@cython.no_gc_clear
cdef class UVProcessTransport(UVProcess):
    def __cinit__(self):
        self._exit_waiters = []
        self._protocol = None

        self._init_futs = []
        self._pending_calls = []
        self._stdio_ready = 0

        self._stdin = self._stdout = self._stderr = None
        self.stdin_proto = self.stdout_proto = self.stderr_proto = None

        self._finished = 0

    cdef _on_exit(self, int64_t exit_status, int term_signal):
        UVProcess._on_exit(self, exit_status, term_signal)

        if self._stdio_ready:
            self._loop.call_soon(self._protocol.process_exited,
                                 context=self.context)
        else:
            self._pending_calls.append((_CALL_PROCESS_EXITED, None, None))

        self._try_finish()

        for waiter in self._exit_waiters:
            if not waiter.cancelled():
                waiter.set_result(self._returncode)
        self._exit_waiters.clear()

        self._close()

    cdef _check_proc(self):
        if not self._is_alive() or self._returncode is not None:
            raise ProcessLookupError()

    cdef _pipe_connection_lost(self, int fd, exc):
        if self._stdio_ready:
            self._loop.call_soon(self._protocol.pipe_connection_lost, fd, exc,
                                 context=self.context)
            self._try_finish()
        else:
            self._pending_calls.append((_CALL_PIPE_CONNECTION_LOST, fd, exc))

    cdef _pipe_data_received(self, int fd, data):
        if self._stdio_ready:
            self._loop.call_soon(self._protocol.pipe_data_received, fd, data,
                                 context=self.context)
        else:
            self._pending_calls.append((_CALL_PIPE_DATA_RECEIVED, fd, data))

    cdef _file_redirect_stdio(self, int fd):
        fd = os_dup(fd)
        os_set_inheritable(fd, True)
        self._close_after_spawn(fd)
        return fd

    cdef _file_devnull(self):
        dn = os_open(os_devnull, os_O_RDWR)
        os_set_inheritable(dn, True)
        self._close_after_spawn(dn)
        return dn

    cdef _file_outpipe(self):
        r, w = __socketpair()
        os_set_inheritable(w, True)
        self._close_after_spawn(w)
        return r, w

    cdef _file_inpipe(self):
        r, w = __socketpair()
        os_set_inheritable(r, True)
        self._close_after_spawn(r)
        return r, w

    cdef _init_files(self, _stdin, _stdout, _stderr):
        cdef uv.uv_stdio_container_t *iocnt

        UVProcess._init_files(self, _stdin, _stdout, _stderr)

        io = [None, None, None]

        self.options.stdio_count = 3
        self.options.stdio = self.iocnt

        if _stdin is not None:
            if _stdin == subprocess_PIPE:
                r, w = self._file_inpipe()
                io[0] = r

                self.stdin_proto = WriteSubprocessPipeProto(self, 0)
                waiter = self._loop._new_future()
                self._stdin = WriteUnixTransport.new(
                    self._loop, self.stdin_proto, None, waiter)
                self._init_futs.append(waiter)
                self._stdin._open(w)
                self._stdin._init_protocol()
            elif _stdin == subprocess_DEVNULL:
                io[0] = self._file_devnull()
            elif _stdout == subprocess_STDOUT:
                raise ValueError(
                    'subprocess.STDOUT is supported only by stderr parameter')
            else:
                io[0] = self._file_redirect_stdio(_stdin)
        else:
            io[0] = self._file_redirect_stdio(0)

        if _stdout is not None:
            if _stdout == subprocess_PIPE:
                # We can't use UV_CREATE_PIPE here, since 'stderr' might be
                # set to 'subprocess.STDOUT', and there is no way to
                # emulate that functionality with libuv high-level
                # streams API. Therefore, we create pipes for stdout and
                # stderr manually.

                r, w = self._file_outpipe()
                io[1] = w

                self.stdout_proto = ReadSubprocessPipeProto(self, 1)
                waiter = self._loop._new_future()
                self._stdout = ReadUnixTransport.new(
                    self._loop, self.stdout_proto, None, waiter)
                self._init_futs.append(waiter)
                self._stdout._open(r)
                self._stdout._init_protocol()
            elif _stdout == subprocess_DEVNULL:
                io[1] = self._file_devnull()
            elif _stdout == subprocess_STDOUT:
                raise ValueError(
                    'subprocess.STDOUT is supported only by stderr parameter')
            else:
                io[1] = self._file_redirect_stdio(_stdout)
        else:
            io[1] = self._file_redirect_stdio(1)

        if _stderr is not None:
            if _stderr == subprocess_PIPE:
                r, w = self._file_outpipe()
                io[2] = w

                self.stderr_proto = ReadSubprocessPipeProto(self, 2)
                waiter = self._loop._new_future()
                self._stderr = ReadUnixTransport.new(
                    self._loop, self.stderr_proto, None, waiter)
                self._init_futs.append(waiter)
                self._stderr._open(r)
                self._stderr._init_protocol()
            elif _stderr == subprocess_STDOUT:
                if io[1] is None:
                    # shouldn't ever happen
                    raise RuntimeError('cannot apply subprocess.STDOUT')

                io[2] = self._file_redirect_stdio(io[1])
            elif _stderr == subprocess_DEVNULL:
                io[2] = self._file_devnull()
            else:
                io[2] = self._file_redirect_stdio(_stderr)
        else:
            io[2] = self._file_redirect_stdio(2)

        assert len(io) == 3
        for idx in range(3):
            iocnt = &self.iocnt[idx]
            if io[idx] is not None:
                iocnt.flags = uv.UV_INHERIT_FD
                iocnt.data.fd = io[idx]
            else:
                iocnt.flags = uv.UV_IGNORE

    cdef _call_connection_made(self, waiter):
        try:
            # we're always called in the right context, so just call the user's
            self._protocol.connection_made(self)
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException as ex:
            if waiter is not None and not waiter.cancelled():
                waiter.set_exception(ex)
            else:
                raise
        else:
            if waiter is not None and not waiter.cancelled():
                waiter.set_result(True)

        self._stdio_ready = 1
        if self._pending_calls:
            pending_calls = self._pending_calls.copy()
            self._pending_calls.clear()
            for (type, fd, arg) in pending_calls:
                if type == _CALL_PIPE_CONNECTION_LOST:
                    self._pipe_connection_lost(fd, arg)
                elif type == _CALL_PIPE_DATA_RECEIVED:
                    self._pipe_data_received(fd, arg)
                elif type == _CALL_PROCESS_EXITED:
                    self._loop.call_soon(self._protocol.process_exited)
                elif type == _CALL_CONNECTION_LOST:
                    self._loop.call_soon(self._protocol.connection_lost, None)

    cdef _try_finish(self):
        if self._returncode is None or self._finished:
            return

        if ((self.stdin_proto is None or self.stdin_proto.disconnected) and
                (self.stdout_proto is None or
                    self.stdout_proto.disconnected) and
                (self.stderr_proto is None or
                    self.stderr_proto.disconnected)):

            self._finished = 1

            if self._stdio_ready:
                # copy self.context for simplicity
                self._loop.call_soon(self._protocol.connection_lost, None,
                                     context=self.context)
            else:
                self._pending_calls.append((_CALL_CONNECTION_LOST, None, None))

    def __stdio_inited(self, waiter, stdio_fut):
        exc = stdio_fut.exception()
        if exc is not None:
            if waiter is None:
                raise exc
            else:
                waiter.set_exception(exc)
        else:
            self._loop._call_soon_handle(
                new_MethodHandle1(self._loop,
                                  "UVProcessTransport._call_connection_made",
                                  <method1_t>self._call_connection_made,
                                  None,  # means to copy the current context
                                  self, waiter))

    @staticmethod
    cdef UVProcessTransport new(Loop loop, protocol, args, env,
                                cwd, start_new_session,
                                _stdin, _stdout, _stderr, pass_fds,
                                waiter,
                                debug_flags,
                                preexec_fn,
                                restore_signals):

        cdef UVProcessTransport handle
        handle = UVProcessTransport.__new__(UVProcessTransport)
        handle._protocol = protocol
        handle._init(loop, args, env, cwd, start_new_session,
                     __process_convert_fileno(_stdin),
                     __process_convert_fileno(_stdout),
                     __process_convert_fileno(_stderr),
                     pass_fds,
                     debug_flags,
                     preexec_fn,
                     restore_signals)

        if handle._init_futs:
            handle._stdio_ready = 0
            init_fut = aio_gather(*handle._init_futs)
            # add_done_callback will copy the current context and run the
            # callback within the context
            init_fut.add_done_callback(
                ft_partial(handle.__stdio_inited, waiter))
        else:
            handle._stdio_ready = 1
            loop._call_soon_handle(
                new_MethodHandle1(loop,
                                  "UVProcessTransport._call_connection_made",
                                  <method1_t>handle._call_connection_made,
                                  None,  # means to copy the current context
                                  handle, waiter))

        return handle

    def get_protocol(self):
        return self._protocol

    def set_protocol(self, protocol):
        self._protocol = protocol

    def get_pid(self):
        return self._pid

    def get_returncode(self):
        return self._returncode

    def get_pipe_transport(self, fd):
        if fd == 0:
            return self._stdin
        elif fd == 1:
            return self._stdout
        elif fd == 2:
            return self._stderr

    def terminate(self):
        self._check_proc()
        self._kill(uv.SIGTERM)

    def kill(self):
        self._check_proc()
        self._kill(uv.SIGKILL)

    def send_signal(self, int signal):
        self._check_proc()
        self._kill(signal)

    def is_closing(self):
        return self._closed

    def close(self):
        if self._returncode is None:
            self._kill(uv.SIGKILL)

        if self._stdin is not None:
            self._stdin.close()
        if self._stdout is not None:
            self._stdout.close()
        if self._stderr is not None:
            self._stderr.close()

        if self._returncode is not None:
            # The process is dead, just close the UV handle.
            #
            # (If "self._returncode is None", the process should have been
            # killed already and we're just waiting for a SIGCHLD; after
            # which the transport will be GC'ed and the uvhandle will be
            # closed in UVHandle.__dealloc__.)
            self._close()

    def get_extra_info(self, name, default=None):
        return default

    def _wait(self):
        fut = self._loop._new_future()
        if self._returncode is not None:
            fut.set_result(self._returncode)
            return fut

        self._exit_waiters.append(fut)
        return fut


class WriteSubprocessPipeProto(aio_BaseProtocol):

    def __init__(self, proc, fd):
        if UVLOOP_DEBUG:
            if type(proc) is not UVProcessTransport:
                raise TypeError
            if not isinstance(fd, int):
                raise TypeError
        self.proc = proc
        self.fd = fd
        self.pipe = None
        self.disconnected = False

    def connection_made(self, transport):
        self.pipe = transport

    def __repr__(self):
        return ('<%s fd=%s pipe=%r>'
                % (self.__class__.__name__, self.fd, self.pipe))

    def connection_lost(self, exc):
        self.disconnected = True
        (<UVProcessTransport>self.proc)._pipe_connection_lost(self.fd, exc)
        self.proc = None

    def pause_writing(self):
        (<UVProcessTransport>self.proc)._protocol.pause_writing()

    def resume_writing(self):
        (<UVProcessTransport>self.proc)._protocol.resume_writing()


class ReadSubprocessPipeProto(WriteSubprocessPipeProto,
                              aio_Protocol):

    def data_received(self, data):
        (<UVProcessTransport>self.proc)._pipe_data_received(self.fd, data)


cdef __process_convert_fileno(object obj):
    if obj is None or isinstance(obj, int):
        return obj

    fileno = obj.fileno()
    if not isinstance(fileno, int):
        raise TypeError(
            '{!r}.fileno() returned non-integer'.format(obj))
    return fileno


cdef void __uvprocess_on_exit_callback(
    uv.uv_process_t *handle,
    int64_t exit_status,
    int term_signal,
) noexcept with gil:

    if __ensure_handle_data(<uv.uv_handle_t*>handle,
                            "UVProcess exit callback") == 0:
        return

    cdef UVProcess proc = <UVProcess> handle.data
    try:
        proc._on_exit(exit_status, term_signal)
    except BaseException as ex:
        proc._error(ex, False)


cdef __socketpair():
    cdef:
        int fds[2]
        int err

    err = system.socketpair(uv.AF_UNIX, uv.SOCK_STREAM, 0, fds)
    if err:
        exc = convert_error(-err)
        raise exc

    os_set_inheritable(fds[0], False)
    os_set_inheritable(fds[1], False)

    return fds[0], fds[1]


cdef void __uv_close_process_handle_cb(
    uv.uv_handle_t* handle
) noexcept with gil:
    PyMem_RawFree(handle)
```

## File: `uvloop/handles/stream.pxd`
```
cdef enum ProtocolType:
    SIMPLE = 0          # User Protocol doesn't support asyncio.BufferedProtocol
    BUFFERED = 1        # User Protocol supports asyncio.BufferedProtocol
    SSL_PROTOCOL = 2    # Our own SSLProtocol


cdef class UVStream(UVBaseTransport):
    cdef:
        uv.uv_shutdown_t _shutdown_req
        bint __shutting_down
        bint __reading
        bint __read_error_close

        ProtocolType __protocol_type
        object _protocol_get_buffer
        object _protocol_buffer_updated

        bint _eof
        list _buffer
        size_t _buffer_size

        Py_buffer _read_pybuf
        bint _read_pybuf_acquired

    cpdef write(self, object buf)

    # All "inline" methods are final

    cdef inline _init(self, Loop loop, object protocol, Server server,
                      object waiter, object context)


    cdef inline _shutdown(self)
    cdef inline _accept(self, UVStream server)

    cdef inline _close_on_read_error(self)

    cdef inline __reading_started(self)
    cdef inline __reading_stopped(self)

    # The user API write() and writelines() firstly call _buffer_write() to
    # buffer up user data chunks, potentially multiple times in writelines(),
    # and then call _initiate_write() to start writing either immediately or in
    # the next iteration (loop._queue_write()).
    cdef inline _buffer_write(self, object data)
    cdef inline _initiate_write(self)

    # _exec_write() is the method that does the actual send, and _try_write()
    # is a fast-path used in _exec_write() to send a single chunk.
    cdef inline bint _exec_write(self) except -1
    cdef inline Py_ssize_t _try_write(self, object data) except -2

    cdef _close(self)

    cdef inline _on_accept(self)
    cdef inline _on_eof(self)
    cdef inline _on_write(self)
    cdef inline _on_connect(self, object exc)
```

## File: `uvloop/handles/stream.pyx`
```
cdef enum:
    __PREALLOCED_BUFS = 4


@cython.no_gc_clear
@cython.freelist(DEFAULT_FREELIST_SIZE)
cdef class _StreamWriteContext:
    # used to hold additional write request information for uv_write

    cdef:
        uv.uv_write_t   req

        list            buffers

        uv.uv_buf_t     uv_bufs_sml[__PREALLOCED_BUFS]
        Py_buffer       py_bufs_sml[__PREALLOCED_BUFS]
        bint            py_bufs_sml_inuse

        uv.uv_buf_t*    uv_bufs
        Py_buffer*      py_bufs
        size_t          py_bufs_len

        uv.uv_buf_t*    uv_bufs_start
        size_t          uv_bufs_len

        UVStream        stream

        bint            closed

    cdef free_bufs(self):
        cdef size_t i

        if self.uv_bufs is not NULL:
            PyMem_RawFree(self.uv_bufs)
            self.uv_bufs = NULL
            if UVLOOP_DEBUG:
                if self.py_bufs_sml_inuse:
                    raise RuntimeError(
                        '_StreamWriteContext.close: uv_bufs != NULL and '
                        'py_bufs_sml_inuse is True')

        if self.py_bufs is not NULL:
            for i from 0 <= i < self.py_bufs_len:
                PyBuffer_Release(&self.py_bufs[i])
            PyMem_RawFree(self.py_bufs)
            self.py_bufs = NULL
            if UVLOOP_DEBUG:
                if self.py_bufs_sml_inuse:
                    raise RuntimeError(
                        '_StreamWriteContext.close: py_bufs != NULL and '
                        'py_bufs_sml_inuse is True')

        if self.py_bufs_sml_inuse:
            for i from 0 <= i < self.py_bufs_len:
                PyBuffer_Release(&self.py_bufs_sml[i])
            self.py_bufs_sml_inuse = 0

        self.py_bufs_len = 0
        self.buffers = None

    cdef close(self):
        if self.closed:
            return
        self.closed = 1
        self.free_bufs()
        Py_DECREF(self)

    cdef advance_uv_buf(self, size_t sent):
        # Advance the pointer to first uv_buf and the
        # pointer to first byte in that buffer.
        #
        # We do this after a "uv_try_write" call, which
        # sometimes sends only a portion of data.
        # We then call "advance_uv_buf" on the write
        # context, and reuse it in a "uv_write" call.

        cdef:
            uv.uv_buf_t* buf
            size_t idx

        for idx from 0 <= idx < self.uv_bufs_len:
            buf = &self.uv_bufs_start[idx]
            if buf.len > sent:
                buf.len -= sent
                buf.base = buf.base + sent
                self.uv_bufs_start = buf
                self.uv_bufs_len -= idx
                return
            else:
                sent -= self.uv_bufs_start[idx].len

            if UVLOOP_DEBUG:
                if sent < 0:
                    raise RuntimeError('fatal: sent < 0 in advance_uv_buf')

        raise RuntimeError('fatal: Could not advance _StreamWriteContext')

    @staticmethod
    cdef _StreamWriteContext new(UVStream stream, list buffers):
        cdef:
            _StreamWriteContext ctx
            int uv_bufs_idx = 0
            size_t py_bufs_len = 0
            int i

            Py_buffer* p_pybufs
            uv.uv_buf_t* p_uvbufs

        ctx = _StreamWriteContext.__new__(_StreamWriteContext)
        ctx.stream = None
        ctx.closed = 1
        ctx.py_bufs_len = 0
        ctx.py_bufs_sml_inuse = 0
        ctx.uv_bufs = NULL
        ctx.py_bufs = NULL
        ctx.buffers = buffers
        ctx.stream = stream

        if len(buffers) <= __PREALLOCED_BUFS:
            # We've got a small number of buffers to write, don't
            # need to use malloc.
            ctx.py_bufs_sml_inuse = 1
            p_pybufs = <Py_buffer*>&ctx.py_bufs_sml
            p_uvbufs = <uv.uv_buf_t*>&ctx.uv_bufs_sml

        else:
            for buf in buffers:
                if UVLOOP_DEBUG:
                    if not isinstance(buf, (bytes, bytearray, memoryview)):
                        raise RuntimeError(
                            'invalid data in writebuf: an instance of '
                            'bytes, bytearray or memoryview was expected, '
                            'got {}'.format(type(buf)))

                if not PyBytes_CheckExact(buf):
                    py_bufs_len += 1

            if py_bufs_len > 0:
                ctx.py_bufs = <Py_buffer*>PyMem_RawMalloc(
                    py_bufs_len * sizeof(Py_buffer))
                if ctx.py_bufs is NULL:
                    raise MemoryError()

            ctx.uv_bufs = <uv.uv_buf_t*>PyMem_RawMalloc(
                len(buffers) * sizeof(uv.uv_buf_t))
            if ctx.uv_bufs is NULL:
                raise MemoryError()

            p_pybufs = ctx.py_bufs
            p_uvbufs = ctx.uv_bufs

        py_bufs_len = 0
        for buf in buffers:
            if PyBytes_CheckExact(buf):
                # We can only use this hack for bytes since it's
                # immutable.  For everything else it is only safe to
                # use buffer protocol.
                p_uvbufs[uv_bufs_idx].base = PyBytes_AS_STRING(buf)
                p_uvbufs[uv_bufs_idx].len = Py_SIZE(buf)

            else:
                try:
                    PyObject_GetBuffer(
                        buf, &p_pybufs[py_bufs_len], PyBUF_SIMPLE)
                except Exception:
                    # This shouldn't ever happen, as `UVStream._buffer_write`
                    # casts non-bytes objects to `memoryviews`.
                    ctx.py_bufs_len = py_bufs_len
                    ctx.free_bufs()
                    raise

                p_uvbufs[uv_bufs_idx].base = <char*>p_pybufs[py_bufs_len].buf
                p_uvbufs[uv_bufs_idx].len = p_pybufs[py_bufs_len].len

                py_bufs_len += 1

            uv_bufs_idx += 1

        ctx.uv_bufs_start = p_uvbufs
        ctx.uv_bufs_len = uv_bufs_idx

        ctx.py_bufs_len = py_bufs_len
        ctx.req.data = <void*> ctx

        if UVLOOP_DEBUG:
            stream._loop._debug_stream_write_ctx_total += 1
            stream._loop._debug_stream_write_ctx_cnt += 1

        # Do incref after everything else is done.
        # Under no circumstances we want `ctx` to be GCed while
        # libuv is still working with `ctx.uv_bufs`.
        Py_INCREF(ctx)
        ctx.closed = 0
        return ctx

    def __dealloc__(self):
        if not self.closed:
            # Because we do an INCREF in _StreamWriteContext.new,
            # __dealloc__ shouldn't ever happen with `self.closed == 1`
            raise RuntimeError(
                'open _StreamWriteContext is being deallocated')

        if UVLOOP_DEBUG:
            if self.stream is not None:
                self.stream._loop._debug_stream_write_ctx_cnt -= 1
                self.stream = None


@cython.no_gc_clear
cdef class UVStream(UVBaseTransport):

    def __cinit__(self):
        self.__shutting_down = 0
        self.__reading = 0
        self.__read_error_close = 0

        self.__protocol_type = ProtocolType.SIMPLE
        self._protocol_get_buffer = None
        self._protocol_buffer_updated = None

        self._eof = 0
        self._buffer = []
        self._buffer_size = 0

        self._read_pybuf_acquired = False

    cdef _set_protocol(self, object protocol):
        if protocol is None:
            raise TypeError('protocol is required')

        UVBaseTransport._set_protocol(self, protocol)

        if isinstance(protocol, SSLProtocol):
            self.__protocol_type = ProtocolType.SSL_PROTOCOL
        elif (hasattr(protocol, 'get_buffer') and
                not isinstance(protocol, aio_Protocol)):
            try:
                self._protocol_get_buffer = protocol.get_buffer
                self._protocol_buffer_updated = protocol.buffer_updated
                self.__protocol_type = ProtocolType.BUFFERED
            except AttributeError:
                pass
        else:
            self.__protocol_type = ProtocolType.SIMPLE

    cdef _clear_protocol(self):
        UVBaseTransport._clear_protocol(self)
        self._protocol_get_buffer = None
        self._protocol_buffer_updated = None
        self.__protocol_type = ProtocolType.SIMPLE

    cdef inline _shutdown(self):
        cdef int err

        if self.__shutting_down:
            return
        self.__shutting_down = 1

        self._ensure_alive()

        self._shutdown_req.data = <void*> self
        err = uv.uv_shutdown(&self._shutdown_req,
                             <uv.uv_stream_t*> self._handle,
                             __uv_stream_on_shutdown)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return

    cdef inline _accept(self, UVStream server):
        cdef int err
        self._ensure_alive()

        err = uv.uv_accept(<uv.uv_stream_t*>server._handle,
                           <uv.uv_stream_t*>self._handle)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return

        self._on_accept()

    cdef inline _close_on_read_error(self):
        self.__read_error_close = 1

    cdef bint _is_reading(self):
        return self.__reading

    cdef _start_reading(self):
        cdef int err

        if self._closing:
            return

        self._ensure_alive()

        if self.__reading:
            return

        if self.__protocol_type == ProtocolType.SIMPLE:
            err = uv.uv_read_start(<uv.uv_stream_t*>self._handle,
                                   __loop_alloc_buffer,
                                   __uv_stream_on_read)
        else:
            err = uv.uv_read_start(<uv.uv_stream_t *> self._handle,
                                   __uv_stream_buffered_alloc,
                                   __uv_stream_buffered_on_read)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return
        else:
            # UVStream must live until the read callback is called
            self.__reading_started()

    cdef inline __reading_started(self):
        if self.__reading:
            return
        self.__reading = 1
        Py_INCREF(self)

    cdef inline __reading_stopped(self):
        if not self.__reading:
            return
        self.__reading = 0
        Py_DECREF(self)

    cdef _stop_reading(self):
        cdef int err

        if not self.__reading:
            return

        self._ensure_alive()

        # From libuv docs:
        #    This function is idempotent and may be safely
        #    called on a stopped stream.
        err = uv.uv_read_stop(<uv.uv_stream_t*>self._handle)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return
        else:
            self.__reading_stopped()

    cdef inline Py_ssize_t _try_write(self, object data) except -2:
        # Returns number of bytes written.
        # -1 - in case of fatal errors
        cdef:
            Py_ssize_t written
            bint used_buf = 0
            Py_buffer py_buf
            void* buf
            Py_ssize_t blen
            int saved_errno
            int fd

        if (<uv.uv_stream_t*>self._handle).write_queue_size != 0:
            raise RuntimeError(
                'UVStream._try_write called with data in uv buffers')

        if PyBytes_CheckExact(data):
            # We can only use this hack for bytes since it's
            # immutable.  For everything else it is only safe to
            # use buffer protocol.
            buf = <void*>PyBytes_AS_STRING(data)
            blen = Py_SIZE(data)
        else:
            PyObject_GetBuffer(data, &py_buf, PyBUF_SIMPLE)
            used_buf = 1
            buf = py_buf.buf
            blen = py_buf.len

        if blen == 0:
            if used_buf:
                PyBuffer_Release(&py_buf)
            # Empty data, do nothing.
            return 0

        fd = self._fileno()
        # Use `unistd.h/write` directly, it's faster than
        # uv_try_write -- less layers of code.  The error
        # checking logic is copied from libuv.
        written = system.write(fd, buf, blen)
        while written == -1 and (
                errno.errno == errno.EINTR or
                (system.PLATFORM_IS_APPLE and
                    errno.errno == errno.EPROTOTYPE)):
            # From libuv code (unix/stream.c):
            #   Due to a possible kernel bug at least in OS X 10.10 "Yosemite",
            #   EPROTOTYPE can be returned while trying to write to a socket
            #   that is shutting down. If we retry the write, we should get
            #   the expected EPIPE instead.
            written = system.write(fd, buf, blen)
        saved_errno = errno.errno

        if used_buf:
            PyBuffer_Release(&py_buf)

        if written < 0:
            if saved_errno in (errno.EAGAIN, system.EWOULDBLOCK):
                return 0
            else:
                exc = convert_error(-saved_errno)
                self._fatal_error(exc, True)
                return -1

        if UVLOOP_DEBUG:
            self._loop._debug_stream_write_tries += 1

        return written

    cdef inline _buffer_write(self, object data):
        cdef Py_ssize_t dlen

        if not PyBytes_CheckExact(data):
            data = memoryview(data).cast('b')

        dlen = len(data)
        if not dlen:
            return

        self._buffer_size += dlen
        self._buffer.append(data)

    cdef inline _initiate_write(self):
        cdef bint all_sent

        if (not self._protocol_paused and
            (<uv.uv_stream_t*>self._handle).write_queue_size == 0):
            # Fast-path.  If:
            #   - the protocol isn't yet paused,
            #   - there is no data in libuv buffers for this stream,
            #
            # Then:
            #   - Try to write all buffered data right now.
            all_sent = self._exec_write()
            if UVLOOP_DEBUG:
                if self._buffer_size != 0 or self._buffer:
                    raise RuntimeError(
                        '_buffer_size is not 0 after a successful _exec_write')

            # There is no need to call `_queue_write` anymore,
            # as `uv_write` should be called already.

            if not all_sent:
                # If not all of the data was sent successfully,
                # we might need to pause the protocol.
                self._maybe_pause_protocol()

        elif self._buffer_size > 0:
            self._maybe_pause_protocol()
            self._loop._queue_write(self)

    cdef inline bint _exec_write(self) except -1:
        # Returns True if all data from self._buffers has been sent,
        # False - otherwise
        cdef:
            int err
            Py_ssize_t buf_len
            Py_ssize_t sent
            _StreamWriteContext ctx = None

        if self._closed:
            # If the handle is closed, just return, it's too
            # late to do anything.
            return False

        buf_len = len(self._buffer)
        if not buf_len:
            return True

        if (<uv.uv_stream_t*>self._handle).write_queue_size == 0:
            # libuv internal write buffers for this stream are empty.
            if buf_len == 1:
                # If we only have one piece of data to send, let's
                # use our fast implementation of try_write.
                data = self._buffer[0]
                sent = self._try_write(data)

                if sent == len(data):
                    # The most likely and latency sensitive outcome goes first,
                    # all data was successfully written.
                    self._buffer_size = 0
                    self._buffer.clear()
                    # on_write will call "maybe_resume_protocol".
                    self._on_write()
                    return True

                elif sent > 0:
                    if PyBytes_CheckExact(data):
                        # Cast bytes to memoryview to avoid copying
                        # data that wasn't sent.
                        data = memoryview(data)
                    data = data[sent:]

                    self._buffer_size -= sent
                    self._buffer[0] = data

                elif sent == -1:
                    # A `self._fatal_error` was called.
                    # It might not raise an exception under some
                    # conditions.
                    self._buffer_size = 0
                    self._buffer.clear()
                    if not self._closing:
                        # This should never happen.
                        raise RuntimeError(
                            'stream is open after UVStream._try_write '
                            'returned None')
                    return False

                # At this point it's either data was sent partially,
                # or an EAGAIN has happened.

            else:
                ctx = _StreamWriteContext.new(self, self._buffer)

                err = uv.uv_try_write(<uv.uv_stream_t*>self._handle,
                                      ctx.uv_bufs_start,
                                      ctx.uv_bufs_len)

                if err > 0:
                    # Some data was successfully sent.

                    if <size_t>err == self._buffer_size:
                        # Everything was sent.
                        ctx.close()
                        self._buffer.clear()
                        self._buffer_size = 0
                        # on_write will call "maybe_resume_protocol".
                        self._on_write()
                        return True

                    try:
                        # Advance pointers to uv_bufs in `ctx`,
                        # we will reuse it soon for a uv_write
                        # call.
                        ctx.advance_uv_buf(<ssize_t>err)
                    except Exception as ex:  # This should never happen.
                        # Let's try to close the `ctx` anyways.
                        ctx.close()
                        self._fatal_error(ex, True)
                        self._buffer.clear()
                        self._buffer_size = 0
                        return False

                elif err != uv.UV_EAGAIN:
                    ctx.close()
                    exc = convert_error(err)
                    self._fatal_error(exc, True)
                    self._buffer.clear()
                    self._buffer_size = 0
                    return False

                # fall through

        if ctx is None:
            ctx = _StreamWriteContext.new(self, self._buffer)

        err = uv.uv_write(&ctx.req,
                          <uv.uv_stream_t*>self._handle,
                          ctx.uv_bufs_start,
                          ctx.uv_bufs_len,
                          __uv_stream_on_write)

        self._buffer_size = 0
        # Can't use `_buffer.clear()` here: `ctx` holds a reference to
        # the `_buffer`.
        self._buffer = []

        if err < 0:
            # close write context
            ctx.close()

            exc = convert_error(err)
            self._fatal_error(exc, True)
            return False

        self._maybe_resume_protocol()
        return False

    cdef size_t _get_write_buffer_size(self):
        if self._handle is NULL:
            return 0
        return ((<uv.uv_stream_t*>self._handle).write_queue_size +
                self._buffer_size)

    cdef _close(self):
        try:
            if self._read_pybuf_acquired:
                # Should never happen. libuv always calls uv_alloc/uv_read
                # in pairs.
                self._loop.call_exception_handler({
                    'transport': self,
                    'message': 'XXX: an allocated buffer in transport._close()'
                })
                self._read_pybuf_acquired = 0
                PyBuffer_Release(&self._read_pybuf)

            self._stop_reading()
        finally:
            UVSocketHandle._close(<UVHandle>self)

    cdef inline _on_accept(self):
        # Ultimately called by __uv_stream_on_listen.
        self._init_protocol()

    cdef inline _on_eof(self):
        # Any exception raised here will be caught in
        # __uv_stream_on_read.

        try:
            meth = self._protocol.eof_received
        except AttributeError:
            keep_open = False
        else:
            keep_open = run_in_context(self.context, meth)

        if keep_open:
            # We're keeping the connection open so the
            # protocol can write more, but we still can't
            # receive more, so remove the reader callback.
            self._stop_reading()
        else:
            self.close()

    cdef inline _on_write(self):
        self._maybe_resume_protocol()
        if not self._get_write_buffer_size():
            if self._closing:
                self._schedule_call_connection_lost(None)
            elif self._eof:
                self._shutdown()

    cdef inline _init(self, Loop loop, object protocol, Server server,
                      object waiter, object context):
        self.context = context
        self._set_protocol(protocol)
        self._start_init(loop)

        if server is not None:
            self._set_server(server)

        if waiter is not None:
            self._set_waiter(waiter)

    cdef inline _on_connect(self, object exc):
        # Called from __tcp_connect_callback (tcp.pyx) and
        # __pipe_connect_callback (pipe.pyx).
        if exc is None:
            self._init_protocol()
        else:
            if self._waiter is None:
                self._fatal_error(exc, False, "connect failed")
            elif self._waiter.cancelled():
                # Connect call was cancelled; just close the transport
                # silently.
                self._close()
            elif self._waiter.done():
                self._fatal_error(exc, False, "connect failed")
            else:
                self._waiter.set_exception(exc)
                self._close()

    # === Public API ===

    def __repr__(self):
        return '<{} closed={} reading={} {:#x}>'.format(
            self.__class__.__name__,
            self._closed,
            self.__reading,
            id(self))

    cpdef write(self, object buf):
        self._ensure_alive()

        if self._eof:
            raise RuntimeError('Cannot call write() after write_eof()')
        if not buf:
            return
        if self._conn_lost:
            self._conn_lost += 1
            return
        self._buffer_write(buf)
        self._initiate_write()

    def writelines(self, bufs):
        self._ensure_alive()

        if self._eof:
            raise RuntimeError('Cannot call writelines() after write_eof()')
        if self._conn_lost:
            self._conn_lost += 1
            return
        for buf in bufs:
            self._buffer_write(buf)
        self._initiate_write()

    def write_eof(self):
        self._ensure_alive()

        if self._eof:
            return

        self._eof = 1
        if not self._get_write_buffer_size():
            self._shutdown()

    def can_write_eof(self):
        return True

    def is_reading(self):
        return self._is_reading()

    def pause_reading(self):
        if self._closing or not self._is_reading():
            return
        self._stop_reading()

    def resume_reading(self):
        if self._is_reading() or self._closing:
            return
        self._start_reading()


cdef void __uv_stream_on_shutdown(uv.uv_shutdown_t* req,
                                  int status) noexcept with gil:

    # callback for uv_shutdown

    if req.data is NULL:
        aio_logger.error(
            'UVStream.shutdown callback called with NULL req.data, status=%r',
            status)
        return

    cdef UVStream stream = <UVStream> req.data

    if status < 0 and status != uv.UV_ECANCELED:
        # From libuv source code:
        #     The ECANCELED error code is a lie, the shutdown(2) syscall is a
        #     fait accompli at this point. Maybe we should revisit this in
        #     v0.11.  A possible reason for leaving it unchanged is that it
        #     informs the callee that the handle has been destroyed.

        if UVLOOP_DEBUG:
            stream._loop._debug_stream_shutdown_errors_total += 1

        exc = convert_error(status)
        stream._fatal_error(
            exc, False, "error status in uv_stream_t.shutdown callback")
        return


cdef inline bint __uv_stream_on_read_common(
    UVStream sc,
    Loop loop,
    ssize_t nread,
):
    if sc._closed:
        # The stream was closed, there is no reason to
        # do any work now.
        sc.__reading_stopped()  # Just in case.
        return True

    if nread == uv.UV_EOF:
        # From libuv docs:
        #     The callee is responsible for stopping closing the stream
        #     when an error happens by calling uv_read_stop() or uv_close().
        #     Trying to read from the stream again is undefined.
        try:
            if UVLOOP_DEBUG:
                loop._debug_stream_read_eof_total += 1

            sc._stop_reading()
            sc._on_eof()
        except BaseException as ex:
            if UVLOOP_DEBUG:
                loop._debug_stream_read_eof_cb_errors_total += 1

            sc._fatal_error(ex, False)
        finally:
            return True

    if nread == 0:
        # From libuv docs:
        #     nread might be 0, which does not indicate an error or EOF.
        #     This is equivalent to EAGAIN or EWOULDBLOCK under read(2).
        return True

    if nread < 0:
        # From libuv docs:
        #     The callee is responsible for stopping closing the stream
        #     when an error happens by calling uv_read_stop() or uv_close().
        #     Trying to read from the stream again is undefined.
        #
        # Therefore, we're closing the stream.  Since "UVHandle._close()"
        # doesn't raise exceptions unless uvloop is built with DEBUG=1,
        # we don't need try...finally here.

        if UVLOOP_DEBUG:
            loop._debug_stream_read_errors_total += 1

        if sc.__read_error_close:
            # Used for getting notified when a pipe is closed.
            # See WriteUnixTransport for the explanation.
            sc._on_eof()
            return True

        exc = convert_error(nread)
        sc._fatal_error(
            exc, False, "error status in uv_stream_t.read callback")
        return True

    return False


cdef inline void __uv_stream_on_read_impl(
    uv.uv_stream_t* stream,
    ssize_t nread,
    const uv.uv_buf_t* buf,
):
    cdef:
        UVStream sc = <UVStream>stream.data
        Loop loop = sc._loop

    # It's OK to free the buffer early, since nothing will
    # be able to touch it until this method is done.
    __loop_free_buffer(loop)

    if __uv_stream_on_read_common(sc, loop, nread):
        return

    try:
        if UVLOOP_DEBUG:
            loop._debug_stream_read_cb_total += 1

        run_in_context1(
            sc.context,
            sc._protocol_data_received,
            loop._recv_buffer[:nread],
        )
    except BaseException as exc:
        if UVLOOP_DEBUG:
            loop._debug_stream_read_cb_errors_total += 1

        sc._fatal_error(exc, False)


cdef inline void __uv_stream_on_write_impl(
    uv.uv_write_t* req,
    int status,
):
    cdef:
        _StreamWriteContext ctx = <_StreamWriteContext> req.data
        UVStream stream = <UVStream>ctx.stream

    ctx.close()

    if stream._closed:
        # The stream was closed, there is nothing to do.
        # Even if there is an error, like EPIPE, there
        # is no reason to report it.
        return

    if status < 0:
        if UVLOOP_DEBUG:
            stream._loop._debug_stream_write_errors_total += 1

        exc = convert_error(status)
        stream._fatal_error(
            exc, False, "error status in uv_stream_t.write callback")
        return

    try:
        stream._on_write()
    except BaseException as exc:
        if UVLOOP_DEBUG:
            stream._loop._debug_stream_write_cb_errors_total += 1

        stream._fatal_error(exc, False)


cdef void __uv_stream_on_read(
    uv.uv_stream_t* stream,
    ssize_t nread,
    const uv.uv_buf_t* buf,
) noexcept with gil:

    if __ensure_handle_data(<uv.uv_handle_t*>stream,
                            "UVStream read callback") == 0:
        return

    # Don't need try-finally, __uv_stream_on_read_impl is void
    __uv_stream_on_read_impl(stream, nread, buf)


cdef void __uv_stream_on_write(
    uv.uv_write_t* req,
    int status,
) noexcept with gil:

    if UVLOOP_DEBUG:
        if req.data is NULL:
            aio_logger.error(
                'UVStream.write callback called with NULL req.data, status=%r',
                status)
            return

    # Don't need try-finally, __uv_stream_on_write_impl is void
    __uv_stream_on_write_impl(req, status)


cdef void __uv_stream_buffered_alloc(
    uv.uv_handle_t* stream,
    size_t suggested_size,
    uv.uv_buf_t* uvbuf,
) noexcept with gil:

    if __ensure_handle_data(<uv.uv_handle_t*>stream,
                            "UVStream alloc buffer callback") == 0:
        return

    cdef UVStream sc = <UVStream>stream.data

    # Fast pass for our own SSLProtocol
    # avoid python calls, memoryviews, context enter/exit, etc
    if sc.__protocol_type == ProtocolType.SSL_PROTOCOL:
        try:
            (<SSLProtocol>sc._protocol).get_buffer_impl(
                suggested_size, &uvbuf.base, &uvbuf.len)
            return
        except BaseException as exc:
            # Can't call 'sc._fatal_error' or 'sc._close', libuv will SF.
            # We'll do it later in __uv_stream_buffered_on_read when we
            # receive UV_ENOBUFS.
            uvbuf.len = 0
            uvbuf.base = NULL
            return

    cdef:
        Py_buffer* pybuf = &sc._read_pybuf
        int got_buf = 0

    if sc._read_pybuf_acquired:
        uvbuf.len = 0
        uvbuf.base = NULL
        return

    sc._read_pybuf_acquired = 0
    try:
        buf = run_in_context1(
            sc.context,
            sc._protocol_get_buffer,
            suggested_size,
        )
        PyObject_GetBuffer(buf, pybuf, PyBUF_WRITABLE)
        got_buf = 1
    except BaseException as exc:
        # Can't call 'sc._fatal_error' or 'sc._close', libuv will SF.
        # We'll do it later in __uv_stream_buffered_on_read when we
        # receive UV_ENOBUFS.
        uvbuf.len = 0
        uvbuf.base = NULL
        return

    if not pybuf.len:
        uvbuf.len = 0
        uvbuf.base = NULL
        if got_buf:
            PyBuffer_Release(pybuf)
        return

    sc._read_pybuf_acquired = 1
    uvbuf.base = <char*>pybuf.buf
    uvbuf.len = pybuf.len


cdef void __uv_stream_buffered_on_read(
    uv.uv_stream_t* stream,
    ssize_t nread,
    const uv.uv_buf_t* buf,
) noexcept with gil:

    if __ensure_handle_data(<uv.uv_handle_t*>stream,
                            "UVStream buffered read callback") == 0:
        return

    cdef:
        UVStream sc = <UVStream>stream.data
        Loop loop = sc._loop
        Py_buffer* pybuf = &sc._read_pybuf

    if nread == uv.UV_ENOBUFS:
        sc._fatal_error(
            RuntimeError(
                'unhandled error (or an empty buffer) in get_buffer()'),
            False)
        return

    try:
        # When our own SSLProtocol is used, we get buffer pointer directly,
        # through SSLProtocol.get_buffer_impl, not through Py_Buffer interface.
        # Therefore sc._read_pybuf_acquired is always False for SSLProtocol.
        if (nread > 0 and
            sc.__protocol_type == ProtocolType.BUFFERED and
            not sc._read_pybuf_acquired):
            # From libuv docs:
            #     nread is > 0 if there is data available or < 0 on error. When
            #     we’ve reached EOF, nread will be set to UV_EOF. When
            #     nread < 0, the buf parameter might not point to a valid
            #     buffer; in that case buf.len and buf.base are both set to 0.
            raise RuntimeError(
                f'no python buffer is allocated in on_read; nread={nread}')

        if nread == 0:
            # From libuv docs:
            #     nread might be 0, which does not indicate an error or EOF.
            #     This is equivalent to EAGAIN or EWOULDBLOCK under read(2).
            return

        if __uv_stream_on_read_common(sc, loop, nread):
            return

        if UVLOOP_DEBUG:
            loop._debug_stream_read_cb_total += 1

        if sc.__protocol_type == ProtocolType.SSL_PROTOCOL:
            Context_Enter(sc.context)
            try:
                (<SSLProtocol>sc._protocol).buffer_updated_impl(nread)
            finally:
                Context_Exit(sc.context)
        else:
            run_in_context1(sc.context, sc._protocol_buffer_updated, nread)
    except BaseException as exc:
        if UVLOOP_DEBUG:
            loop._debug_stream_read_cb_errors_total += 1

        sc._fatal_error(exc, False)
    finally:
        if sc._read_pybuf_acquired:
            sc._read_pybuf_acquired = 0
            PyBuffer_Release(pybuf)
```

## File: `uvloop/handles/streamserver.pxd`
```
cdef class UVStreamServer(UVSocketHandle):
    cdef:
        int backlog
        object ssl
        object ssl_handshake_timeout
        object ssl_shutdown_timeout
        object protocol_factory
        bint opened
        Server _server

    # All "inline" methods are final

    cdef inline _init(self, Loop loop, object protocol_factory,
                      Server server,
                      object backlog,
                      object ssl,
                      object ssl_handshake_timeout,
                      object ssl_shutdown_timeout)

    cdef inline _mark_as_open(self)

    cdef inline listen(self)
    cdef inline _on_listen(self)

    cdef UVStream _make_new_transport(self, object protocol, object waiter,
                                      object context)
```

## File: `uvloop/handles/streamserver.pyx`
```
@cython.no_gc_clear
cdef class UVStreamServer(UVSocketHandle):

    def __cinit__(self):
        self.opened = 0
        self._server = None
        self.ssl = None
        self.ssl_handshake_timeout = None
        self.ssl_shutdown_timeout = None
        self.protocol_factory = None

    cdef inline _init(self, Loop loop, object protocol_factory,
                      Server server,
                      object backlog,
                      object ssl,
                      object ssl_handshake_timeout,
                      object ssl_shutdown_timeout):

        if not isinstance(backlog, int):
            # Don't allow floats
            raise TypeError('integer argument expected, got {}'.format(
                type(backlog).__name__))

        if ssl is not None:
            if not isinstance(ssl, ssl_SSLContext):
                raise TypeError(
                    'ssl is expected to be None or an instance of '
                    'ssl.SSLContext, got {!r}'.format(ssl))
        else:
            if ssl_handshake_timeout is not None:
                raise ValueError(
                    'ssl_handshake_timeout is only meaningful with ssl')
            if ssl_shutdown_timeout is not None:
                raise ValueError(
                    'ssl_shutdown_timeout is only meaningful with ssl')

        self.backlog = backlog
        self.ssl = ssl
        self.ssl_handshake_timeout = ssl_handshake_timeout
        self.ssl_shutdown_timeout = ssl_shutdown_timeout

        self._start_init(loop)
        self.protocol_factory = protocol_factory
        self._server = server

    cdef inline listen(self):
        cdef int err
        self._ensure_alive()

        if self.protocol_factory is None:
            raise RuntimeError('unable to listen(); no protocol_factory')

        if self.opened != 1:
            raise RuntimeError('unopened TCPServer')

        self.context = Context_CopyCurrent()

        err = uv.uv_listen(<uv.uv_stream_t*> self._handle,
                           self.backlog,
                           __uv_streamserver_on_listen)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return

    cdef inline _on_listen(self):
        cdef UVStream client

        protocol = run_in_context(self.context, self.protocol_factory)

        if self.ssl is None:
            client = self._make_new_transport(protocol, None, self.context)

        else:
            waiter = self._loop._new_future()

            ssl_protocol = SSLProtocol(
                self._loop, protocol, self.ssl,
                waiter,
                server_side=True,
                server_hostname=None,
                ssl_handshake_timeout=self.ssl_handshake_timeout,
                ssl_shutdown_timeout=self.ssl_shutdown_timeout)

            client = self._make_new_transport(ssl_protocol, None, self.context)

            waiter.add_done_callback(
                ft_partial(self.__on_ssl_connected, client))

        client._accept(<UVStream>self)

    cdef _fatal_error(self, exc, throw, reason=None):
        # Overload UVHandle._fatal_error

        self._close()

        if not isinstance(exc, OSError):

            if throw or self._loop is None:
                raise exc

            msg = f'Fatal error on server {self.__class__.__name__}'
            if reason is not None:
                msg = f'{msg} ({reason})'

            self._loop.call_exception_handler({
                'message': msg,
                'exception': exc,
            })

    cdef inline _mark_as_open(self):
        self.opened = 1

    cdef UVStream _make_new_transport(self, object protocol, object waiter,
                                      object context):
        raise NotImplementedError

    def __on_ssl_connected(self, transport, fut):
        exc = fut.exception()
        if exc is not None:
            transport._force_close(exc)


cdef void __uv_streamserver_on_listen(
    uv.uv_stream_t* handle,
    int status,
) noexcept with gil:

    # callback for uv_listen

    if __ensure_handle_data(<uv.uv_handle_t*>handle,
                            "UVStream listen callback") == 0:
        return

    cdef:
        UVStreamServer stream = <UVStreamServer> handle.data

    if status < 0:
        if UVLOOP_DEBUG:
            stream._loop._debug_stream_listen_errors_total += 1

        exc = convert_error(status)
        stream._fatal_error(
            exc, False, "error status in uv_stream_t.listen callback")
        return

    try:
        stream._on_listen()
    except BaseException as exc:
        stream._error(exc, False)
```

## File: `uvloop/handles/tcp.pxd`
```
cdef class TCPServer(UVStreamServer):
    cdef bind(self, system.sockaddr* addr, unsigned int flags=*)

    @staticmethod
    cdef TCPServer new(Loop loop, object protocol_factory, Server server,
                       unsigned int flags,
                       object backlog,
                       object ssl,
                       object ssl_handshake_timeout,
                       object ssl_shutdown_timeout)


cdef class TCPTransport(UVStream):
    cdef:
        bint __peername_set
        bint __sockname_set
        system.sockaddr_storage __peername
        system.sockaddr_storage __sockname

    cdef bind(self, system.sockaddr* addr, unsigned int flags=*)
    cdef connect(self, system.sockaddr* addr)
    cdef _set_nodelay(self)

    @staticmethod
    cdef TCPTransport new(Loop loop, object protocol, Server server,
                          object waiter, object context)
```

## File: `uvloop/handles/tcp.pyx`
```
cdef __tcp_init_uv_handle(UVStream handle, Loop loop, unsigned int flags):
    cdef int err

    handle._handle = <uv.uv_handle_t*>PyMem_RawMalloc(sizeof(uv.uv_tcp_t))
    if handle._handle is NULL:
        handle._abort_init()
        raise MemoryError()

    err = uv.uv_tcp_init_ex(handle._loop.uvloop,
                            <uv.uv_tcp_t*>handle._handle,
                            flags)
    if err < 0:
        handle._abort_init()
        raise convert_error(err)

    handle._finish_init()


cdef __tcp_bind(UVStream handle, system.sockaddr* addr, unsigned int flags):
    cdef int err
    err = uv.uv_tcp_bind(<uv.uv_tcp_t *>handle._handle,
                         addr, flags)
    if err < 0:
        exc = convert_error(err)
        raise exc


cdef __tcp_open(UVStream handle, int sockfd):
    cdef int err
    err = uv.uv_tcp_open(<uv.uv_tcp_t *>handle._handle,
                         <uv.uv_os_sock_t>sockfd)
    if err < 0:
        exc = convert_error(err)
        raise exc


cdef __tcp_get_socket(UVSocketHandle handle):
    cdef:
        int buf_len = sizeof(system.sockaddr_storage)
        int fileno
        int err
        system.sockaddr_storage buf

    fileno = handle._fileno()

    err = uv.uv_tcp_getsockname(<uv.uv_tcp_t*>handle._handle,
                                <system.sockaddr*>&buf,
                                &buf_len)
    if err < 0:
        raise convert_error(err)

    return PseudoSocket(buf.ss_family, uv.SOCK_STREAM, 0, fileno)


@cython.no_gc_clear
cdef class TCPServer(UVStreamServer):

    @staticmethod
    cdef TCPServer new(Loop loop, object protocol_factory, Server server,
                       unsigned int flags,
                       object backlog,
                       object ssl,
                       object ssl_handshake_timeout,
                       object ssl_shutdown_timeout):

        cdef TCPServer handle
        handle = TCPServer.__new__(TCPServer)
        handle._init(loop, protocol_factory, server, backlog,
                     ssl, ssl_handshake_timeout, ssl_shutdown_timeout)
        __tcp_init_uv_handle(<UVStream>handle, loop, flags)
        return handle

    cdef _new_socket(self):
        return __tcp_get_socket(<UVSocketHandle>self)

    cdef _open(self, int sockfd):
        self._ensure_alive()
        try:
            __tcp_open(<UVStream>self, sockfd)
        except Exception as exc:
            self._fatal_error(exc, True)
        else:
            self._mark_as_open()

    cdef bind(self, system.sockaddr* addr, unsigned int flags=0):
        self._ensure_alive()
        try:
            __tcp_bind(<UVStream>self, addr, flags)
        except Exception as exc:
            self._fatal_error(exc, True)
        else:
            self._mark_as_open()

    cdef UVStream _make_new_transport(self, object protocol, object waiter,
                                      object context):
        cdef TCPTransport tr
        tr = TCPTransport.new(self._loop, protocol, self._server, waiter,
                              context)
        return <UVStream>tr


@cython.no_gc_clear
cdef class TCPTransport(UVStream):

    @staticmethod
    cdef TCPTransport new(Loop loop, object protocol, Server server,
                          object waiter, object context):

        cdef TCPTransport handle
        handle = TCPTransport.__new__(TCPTransport)
        handle._init(loop, protocol, server, waiter, context)
        __tcp_init_uv_handle(<UVStream>handle, loop, uv.AF_UNSPEC)
        handle.__peername_set = 0
        handle.__sockname_set = 0
        handle._set_nodelay()
        return handle

    cdef _set_nodelay(self):
        cdef int err
        self._ensure_alive()
        err = uv.uv_tcp_nodelay(<uv.uv_tcp_t*>self._handle, 1)
        if err < 0:
            raise convert_error(err)

    cdef _call_connection_made(self):
        # asyncio saves peername & sockname when transports are instantiated,
        # so that they're accessible even after the transport is closed.
        # We are doing the same thing here, except that we create Python
        # objects lazily, on request in get_extra_info()

        cdef:
            int err
            int buf_len

        buf_len = sizeof(system.sockaddr_storage)
        err = uv.uv_tcp_getsockname(<uv.uv_tcp_t*>self._handle,
                                    <system.sockaddr*>&self.__sockname,
                                    &buf_len)
        if err >= 0:
            # Ignore errors, this is an optional thing.
            # If something serious is going on, the transport
            # will crash later (in roughly the same way how
            # an asyncio transport would.)
            self.__sockname_set = 1

        buf_len = sizeof(system.sockaddr_storage)
        err = uv.uv_tcp_getpeername(<uv.uv_tcp_t*>self._handle,
                                    <system.sockaddr*>&self.__peername,
                                    &buf_len)
        if err >= 0:
            # Same as few lines above -- we don't really care
            # about error case here.
            self.__peername_set = 1

        UVBaseTransport._call_connection_made(self)

    def get_extra_info(self, name, default=None):
        if name == 'sockname':
            if self.__sockname_set:
                return __convert_sockaddr_to_pyaddr(
                    <system.sockaddr*>&self.__sockname)
        elif name == 'peername':
            if self.__peername_set:
                return __convert_sockaddr_to_pyaddr(
                    <system.sockaddr*>&self.__peername)
        return super().get_extra_info(name, default)

    cdef _new_socket(self):
        return __tcp_get_socket(<UVSocketHandle>self)

    cdef bind(self, system.sockaddr* addr, unsigned int flags=0):
        self._ensure_alive()
        __tcp_bind(<UVStream>self, addr, flags)

    cdef _open(self, int sockfd):
        self._ensure_alive()
        __tcp_open(<UVStream>self, sockfd)

    cdef connect(self, system.sockaddr* addr):
        cdef _TCPConnectRequest req
        req = _TCPConnectRequest(self._loop, self)
        req.connect(addr)


cdef class _TCPConnectRequest(UVRequest):
    cdef:
        TCPTransport transport
        uv.uv_connect_t _req_data

    def __cinit__(self, loop, transport):
        self.request = <uv.uv_req_t*>&self._req_data
        self.request.data = <void*>self
        self.transport = transport

    cdef connect(self, system.sockaddr* addr):
        cdef int err
        err = uv.uv_tcp_connect(<uv.uv_connect_t*>self.request,
                                <uv.uv_tcp_t*>self.transport._handle,
                                addr,
                                __tcp_connect_callback)
        if err < 0:
            exc = convert_error(err)
            self.on_done()
            raise exc


cdef void __tcp_connect_callback(
    uv.uv_connect_t* req,
    int status,
) noexcept with gil:
    cdef:
        _TCPConnectRequest wrapper
        TCPTransport transport

    wrapper = <_TCPConnectRequest> req.data
    transport = wrapper.transport

    if status < 0:
        exc = convert_error(status)
    else:
        exc = None

    try:
        transport._on_connect(exc)
    except BaseException as ex:
        wrapper.transport._fatal_error(ex, False)
    finally:
        wrapper.on_done()
```

## File: `uvloop/handles/timer.pxd`
```
cdef class UVTimer(UVHandle):
    cdef:
        method_t callback
        object ctx
        bint running
        uint64_t timeout
        uint64_t start_t

    cdef _init(self, Loop loop, method_t callback, object ctx,
               uint64_t timeout)

    cdef stop(self)
    cdef start(self)
    cdef get_when(self)

    @staticmethod
    cdef UVTimer new(Loop loop, method_t callback, object ctx,
                     uint64_t timeout)
```

## File: `uvloop/handles/timer.pyx`
```
@cython.no_gc_clear
cdef class UVTimer(UVHandle):
    cdef _init(self, Loop loop, method_t callback, object ctx,
               uint64_t timeout):

        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*> PyMem_RawMalloc(sizeof(uv.uv_timer_t))
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        err = uv.uv_timer_init(self._loop.uvloop, <uv.uv_timer_t*>self._handle)
        if err < 0:
            self._abort_init()
            raise convert_error(err)

        self._finish_init()

        self.callback = callback
        self.ctx = ctx
        self.running = 0
        self.timeout = timeout
        self.start_t = 0

    cdef stop(self):
        cdef int err

        if not self._is_alive():
            self.running = 0
            return

        if self.running == 1:
            err = uv.uv_timer_stop(<uv.uv_timer_t*>self._handle)
            self.running = 0
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return

    cdef start(self):
        cdef int err

        self._ensure_alive()

        if self.running == 0:
            # Update libuv internal time.
            uv.uv_update_time(self._loop.uvloop)  # void
            self.start_t = uv.uv_now(self._loop.uvloop)

            err = uv.uv_timer_start(<uv.uv_timer_t*>self._handle,
                                    __uvtimer_callback,
                                    self.timeout, 0)
            if err < 0:
                exc = convert_error(err)
                self._fatal_error(exc, True)
                return
            self.running = 1

    cdef get_when(self):
        return self.start_t + self.timeout

    @staticmethod
    cdef UVTimer new(Loop loop, method_t callback, object ctx,
                     uint64_t timeout):

        cdef UVTimer handle
        handle = UVTimer.__new__(UVTimer)
        handle._init(loop, callback, ctx, timeout)
        return handle


cdef void __uvtimer_callback(
    uv.uv_timer_t* handle,
) noexcept with gil:
    if __ensure_handle_data(<uv.uv_handle_t*>handle, "UVTimer callback") == 0:
        return

    cdef:
        UVTimer timer = <UVTimer> handle.data
        method_t cb = timer.callback

    timer.running = 0
    try:
        cb(timer.ctx)
    except BaseException as ex:
        timer._error(ex, False)
```

## File: `uvloop/handles/udp.pxd`
```
cdef class UDPTransport(UVBaseTransport):
    cdef:
        bint __receiving
        int _family
        object _address

    cdef _init(self, Loop loop, unsigned int family)
    cdef _set_address(self, system.addrinfo *addr)

    cdef _connect(self, system.sockaddr* addr, size_t addr_len)

    cdef _bind(self, system.sockaddr* addr)
    cdef open(self, int family, int sockfd)
    cdef _set_broadcast(self, bint on)

    cdef inline __receiving_started(self)
    cdef inline __receiving_stopped(self)

    cdef _send(self, object data, object addr)

    cdef _on_receive(self, bytes data, object exc, object addr)
    cdef _on_sent(self, object exc, object context=*)
```

## File: `uvloop/handles/udp.pyx`
```
@cython.no_gc_clear
@cython.freelist(DEFAULT_FREELIST_SIZE)
cdef class _UDPSendContext:
    # used to hold additional write request information for uv_write

    cdef:
        uv.uv_udp_send_t   req

        uv.uv_buf_t     uv_buf
        Py_buffer       py_buf

        UDPTransport    udp

        bint            closed

    cdef close(self):
        if self.closed:
            return

        self.closed = 1
        PyBuffer_Release(&self.py_buf)  # void
        self.req.data = NULL
        self.uv_buf.base = NULL
        Py_DECREF(self)
        self.udp = None

    @staticmethod
    cdef _UDPSendContext new(UDPTransport udp, object data):
        cdef _UDPSendContext ctx
        ctx = _UDPSendContext.__new__(_UDPSendContext)
        ctx.udp = None
        ctx.closed = 1

        ctx.req.data = <void*> ctx
        Py_INCREF(ctx)

        PyObject_GetBuffer(data, &ctx.py_buf, PyBUF_SIMPLE)
        ctx.uv_buf.base = <char*>ctx.py_buf.buf
        ctx.uv_buf.len = ctx.py_buf.len
        ctx.udp = udp

        ctx.closed = 0
        return ctx

    def __dealloc__(self):
        if UVLOOP_DEBUG:
            if not self.closed:
                raise RuntimeError(
                    'open _UDPSendContext is being deallocated')
        self.udp = None


@cython.no_gc_clear
cdef class UDPTransport(UVBaseTransport):
    def __cinit__(self):
        self._family = uv.AF_UNSPEC
        self.__receiving = 0
        self._address = None
        self.context = Context_CopyCurrent()

    cdef _init(self, Loop loop, unsigned int family):
        cdef int err

        self._start_init(loop)

        self._handle = <uv.uv_handle_t*>PyMem_RawMalloc(sizeof(uv.uv_udp_t))
        if self._handle is NULL:
            self._abort_init()
            raise MemoryError()

        err = uv.uv_udp_init_ex(loop.uvloop,
                                <uv.uv_udp_t*>self._handle,
                                family)
        if err < 0:
            self._abort_init()
            raise convert_error(err)

        if family in (uv.AF_INET, uv.AF_INET6):
            self._family = family

        self._finish_init()

    cdef _set_address(self, system.addrinfo *addr):
        self._address = __convert_sockaddr_to_pyaddr(addr.ai_addr)

    cdef _connect(self, system.sockaddr* addr, size_t addr_len):
        cdef int err
        err = uv.uv_udp_connect(<uv.uv_udp_t*>self._handle, addr)
        if err < 0:
            exc = convert_error(err)
            raise exc

    cdef open(self, int family, int sockfd):
        if family in (uv.AF_INET, uv.AF_INET6, uv.AF_UNIX):
            self._family = family
        else:
            raise ValueError(
                'cannot open a UDP handle, invalid family {}'.format(family))

        cdef int err
        err = uv.uv_udp_open(<uv.uv_udp_t*>self._handle,
                             <uv.uv_os_sock_t>sockfd)

        if err < 0:
            exc = convert_error(err)
            raise exc

    cdef _bind(self, system.sockaddr* addr):
        cdef:
            int err
            int flags = 0

        self._ensure_alive()

        err = uv.uv_udp_bind(<uv.uv_udp_t*>self._handle, addr, flags)
        if err < 0:
            exc = convert_error(err)
            raise exc

    cdef _set_broadcast(self, bint on):
        cdef int err

        self._ensure_alive()

        err = uv.uv_udp_set_broadcast(<uv.uv_udp_t*>self._handle, on)
        if err < 0:
            exc = convert_error(err)
            raise exc

    cdef size_t _get_write_buffer_size(self):
        if self._handle is NULL:
            return 0
        return (<uv.uv_udp_t*>self._handle).send_queue_size

    cdef bint _is_reading(self):
        return self.__receiving

    cdef _start_reading(self):
        cdef int err

        if self.__receiving:
            return

        self._ensure_alive()

        err = uv.uv_udp_recv_start(<uv.uv_udp_t*>self._handle,
                                   __loop_alloc_buffer,
                                   __uv_udp_on_receive)

        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return
        else:
            # UDPTransport must live until the read callback is called
            self.__receiving_started()

    cdef _stop_reading(self):
        cdef int err

        if not self.__receiving:
            return

        self._ensure_alive()

        err = uv.uv_udp_recv_stop(<uv.uv_udp_t*>self._handle)
        if err < 0:
            exc = convert_error(err)
            self._fatal_error(exc, True)
            return
        else:
            self.__receiving_stopped()

    cdef inline __receiving_started(self):
        if self.__receiving:
            return
        self.__receiving = 1
        Py_INCREF(self)

    cdef inline __receiving_stopped(self):
        if not self.__receiving:
            return
        self.__receiving = 0
        Py_DECREF(self)

    cdef _new_socket(self):
        if self._family not in (uv.AF_INET, uv.AF_INET6, uv.AF_UNIX):
            raise RuntimeError(
                'UDPTransport.family is undefined; '
                'cannot create python socket')

        fileno = self._fileno()
        return PseudoSocket(self._family, uv.SOCK_DGRAM, 0, fileno)

    cdef _send(self, object data, object addr):
        cdef:
            _UDPSendContext ctx
            system.sockaddr_storage saddr_st
            system.sockaddr *saddr
            Py_buffer       try_pybuf
            uv.uv_buf_t     try_uvbuf

        self._ensure_alive()

        if self._family not in (uv.AF_INET, uv.AF_INET6, uv.AF_UNIX):
            raise RuntimeError('UDPTransport.family is undefined; cannot send')

        if addr is None:
            saddr = NULL
        else:
            # resolve special hostname <broadcast> to the broadcast address before use
            if self._family == uv.AF_INET and addr[0] == '<broadcast>':
                addr = (b'255.255.255.255', addr[1])

            try:
                __convert_pyaddr_to_sockaddr(self._family, addr,
                                             <system.sockaddr*>&saddr_st)
            except (ValueError, TypeError):
                raise
            except Exception:
                raise ValueError(
                    f'{addr!r}: socket family mismatch or '
                    f'a DNS lookup is required')
            saddr = <system.sockaddr*>(&saddr_st)

        if self._get_write_buffer_size() == 0:
            PyObject_GetBuffer(data, &try_pybuf, PyBUF_SIMPLE)
            try_uvbuf.base = <char*>try_pybuf.buf
            try_uvbuf.len = try_pybuf.len
            err = uv.uv_udp_try_send(<uv.uv_udp_t*>self._handle,
                                     &try_uvbuf,
                                     1,
                                     saddr)
            PyBuffer_Release(&try_pybuf)
        else:
            err = uv.UV_EAGAIN

        if err == uv.UV_EAGAIN:
            ctx = _UDPSendContext.new(self, data)
            err = uv.uv_udp_send(&ctx.req,
                                 <uv.uv_udp_t*>self._handle,
                                 &ctx.uv_buf,
                                 1,
                                 saddr,
                                 __uv_udp_on_send)

            if err < 0:
                ctx.close()

                exc = convert_error(err)
                if isinstance(exc, OSError):
                    run_in_context1(self.context.copy(), self._protocol.error_received, exc)
                else:
                    self._fatal_error(exc, True)
            else:
                self._maybe_pause_protocol()

        else:
            self._on_sent(convert_error(err) if err < 0 else None, self.context.copy())

    cdef _on_receive(self, bytes data, object exc, object addr):
        if exc is None:
            run_in_context2(
                self.context, self._protocol.datagram_received, data, addr,
            )
        else:
            run_in_context1(self.context, self._protocol.error_received, exc)

    cdef _on_sent(self, object exc, object context=None):
        if exc is not None:
            if isinstance(exc, OSError):
                if context is None:
                    context = self.context
                run_in_context1(context, self._protocol.error_received, exc)
            else:
                self._fatal_error(
                    exc, False, 'Fatal write error on datagram transport')

        self._maybe_resume_protocol()
        if not self._get_write_buffer_size():
            if self._closing:
                self._schedule_call_connection_lost(None)

    # === Public API ===

    def sendto(self, data, addr=None):
        if not data:
            # Replicating asyncio logic here.
            return

        if self._address:
            if addr not in (None, self._address):
                # Replicating asyncio logic here.
                raise ValueError(
                    'Invalid address: must be None or %s' % (self._address,))

            # Instead of setting addr to self._address below like what asyncio
            # does, we depend on previous uv_udp_connect() to set the address
            addr = None

        if self._conn_lost:
            # Replicating asyncio logic here.
            if self._conn_lost >= LOG_THRESHOLD_FOR_CONNLOST_WRITES:
                aio_logger.warning('socket.send() raised exception.')
            self._conn_lost += 1
            return

        self._send(data, addr)


cdef void __uv_udp_on_receive(
    uv.uv_udp_t* handle,
    ssize_t nread,
    const uv.uv_buf_t* buf,
    const system.sockaddr* addr,
    unsigned flags
) noexcept with gil:

    if __ensure_handle_data(<uv.uv_handle_t*>handle,
                            "UDPTransport receive callback") == 0:
        return

    cdef:
        UDPTransport udp = <UDPTransport>handle.data
        Loop loop = udp._loop
        bytes data
        object pyaddr

    # It's OK to free the buffer early, since nothing will
    # be able to touch it until this method is done.
    __loop_free_buffer(loop)

    if udp._closed:
        # The handle was closed, there is no reason to
        # do any work now.
        udp.__receiving_stopped()  # Just in case.
        return

    if addr is NULL and nread == 0:
        # From libuv docs:
        #      addr: struct sockaddr* containing the address
        #      of the sender. Can be NULL. Valid for the duration
        #      of the callback only.
        #      [...]
        #      The receive callback will be called with
        #      nread == 0 and addr == NULL when there is
        #      nothing to read, and with nread == 0 and
        #      addr != NULL when an empty UDP packet is
        #      received.
        return

    if addr is NULL:
        pyaddr = None
    elif addr.sa_family == uv.AF_UNSPEC:
        # https://github.com/MagicStack/uvloop/issues/304
        if system.PLATFORM_IS_LINUX:
            pyaddr = None
        else:
            pyaddr = ''
    else:
        try:
            pyaddr = __convert_sockaddr_to_pyaddr(addr)
        except BaseException as exc:
            udp._error(exc, False)
            return

    if nread < 0:
        exc = convert_error(nread)
        udp._on_receive(None, exc, pyaddr)
        return

    if nread == 0:
        data = b''
    else:
        data = loop._recv_buffer[:nread]

    try:
        udp._on_receive(data, None, pyaddr)
    except BaseException as exc:
        udp._error(exc, False)


cdef void __uv_udp_on_send(
    uv.uv_udp_send_t* req,
    int status,
) noexcept with gil:

    if req.data is NULL:
        # Shouldn't happen as:
        #    - _UDPSendContext does an extra INCREF in its 'init()'
        #    - _UDPSendContext holds a ref to the relevant UDPTransport
        aio_logger.error(
            'UVStream.write callback called with NULL req.data, status=%r',
            status)
        return

    cdef:
        _UDPSendContext ctx = <_UDPSendContext> req.data
        UDPTransport udp = <UDPTransport>ctx.udp

    ctx.close()

    if status < 0:
        exc = convert_error(status)
        print(exc)
    else:
        exc = None

    try:
        udp._on_sent(exc)
    except BaseException as exc:
        udp._error(exc, False)
```

## File: `uvloop/includes/__init__.py`
```python
# flake8: noqa

# These have to be synced with the stdlib.pxi
import asyncio
import collections
import concurrent.futures
import errno
import functools
import gc
import inspect
import itertools
import os
import signal
import socket
import subprocess
import ssl
import stat
import sys
import threading
import traceback
import time
import warnings
import weakref
```

## File: `uvloop/includes/compat.h`
```c
#include <errno.h>
#include <stddef.h>
#include <signal.h>
#include <sys/socket.h>
#include <sys/un.h>
#include "Python.h"
#include "uv.h"


#ifndef EWOULDBLOCK
#define EWOULDBLOCK EAGAIN
#endif

#ifdef __APPLE__
#define PLATFORM_IS_APPLE 1
#else
#define PLATFORM_IS_APPLE 0
#endif


#ifdef __linux__
#  define PLATFORM_IS_LINUX 1
#  include <sys/epoll.h>
#else
#  define PLATFORM_IS_LINUX 0
#  define EPOLL_CTL_DEL 2
struct epoll_event {};
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event) {
    return 0;
};
#endif


PyObject *
MakeUnixSockPyAddr(struct sockaddr_un *addr)
{
    if (addr->sun_family != AF_UNIX) {
        PyErr_SetString(
            PyExc_ValueError, "a UNIX socket addr was expected");
        return NULL;
    }

#ifdef __linux__
    int addrlen = sizeof (struct sockaddr_un);
    size_t linuxaddrlen = addrlen - offsetof(struct sockaddr_un, sun_path);
    if (linuxaddrlen > 0 && addr->sun_path[0] == 0) {
        return PyBytes_FromStringAndSize(addr->sun_path, linuxaddrlen);
    }
    else
#endif /* linux */
    {
        /* regular NULL-terminated string */
        return PyUnicode_DecodeFSDefault(addr->sun_path);
    }
}


#if PY_VERSION_HEX < 0x03070100

PyObject * Context_CopyCurrent(void) {
    return (PyObject *)PyContext_CopyCurrent();
};

int Context_Enter(PyObject *ctx) {
    return PyContext_Enter((PyContext *)ctx);
}

int Context_Exit(PyObject *ctx) {
    return PyContext_Exit((PyContext *)ctx);
}

#else

PyObject * Context_CopyCurrent(void) {
    return PyContext_CopyCurrent();
};

int Context_Enter(PyObject *ctx) {
    return PyContext_Enter(ctx);
}

int Context_Exit(PyObject *ctx) {
    return PyContext_Exit(ctx);
}

#endif

/* inlined from cpython/Modules/signalmodule.c
 * https://github.com/python/cpython/blob/v3.13.0a6/Modules/signalmodule.c#L1931-L1951
 * private _Py_RestoreSignals has been moved to CPython internals in Python 3.13
 * https://github.com/python/cpython/pull/106400 */

void
_Py_RestoreSignals(void)
{
#ifdef SIGPIPE
    PyOS_setsig(SIGPIPE, SIG_DFL);
#endif
#ifdef SIGXFZ
    PyOS_setsig(SIGXFZ, SIG_DFL);
#endif
#ifdef SIGXFSZ
    PyOS_setsig(SIGXFSZ, SIG_DFL);
#endif
}
```

## File: `uvloop/includes/consts.pxi`
```
cdef enum:
    UV_STREAM_RECV_BUF_SIZE = 256000  # 250kb

    FLOW_CONTROL_HIGH_WATER = 64  # KiB
    FLOW_CONTROL_HIGH_WATER_SSL_READ = 256  # KiB
    FLOW_CONTROL_HIGH_WATER_SSL_WRITE = 512  # KiB

    DEFAULT_FREELIST_SIZE = 250
    DNS_PYADDR_TO_SOCKADDR_CACHE_SIZE = 2048

    DEBUG_STACK_DEPTH = 10


    __PROCESS_DEBUG_SLEEP_AFTER_FORK = 1


    LOG_THRESHOLD_FOR_CONNLOST_WRITES = 5
    SSL_READ_MAX_SIZE = 256 * 1024


cdef extern from *:
    '''
    // Number of seconds to wait for SSL handshake to complete
    // The default timeout matches that of Nginx.
    #define SSL_HANDSHAKE_TIMEOUT 60.0

    // Number of seconds to wait for SSL shutdown to complete
    // The default timeout mimics lingering_time
    #define SSL_SHUTDOWN_TIMEOUT 30.0
    '''

    const float SSL_HANDSHAKE_TIMEOUT
    const float SSL_SHUTDOWN_TIMEOUT
```

## File: `uvloop/includes/debug.h`
```c
#ifndef UVLOOP_DEBUG
#define UVLOOP_DEBUG 0
#endif
```

## File: `uvloop/includes/debug.pxd`
```
cdef extern from "includes/debug.h":

    cdef int UVLOOP_DEBUG
```

## File: `uvloop/includes/flowcontrol.pxd`
```
# flake8: noqa


cdef inline add_flowcontrol_defaults(high, low, int kb):
    cdef int h, l
    if high is None:
        if low is None:
            h = kb * 1024
        else:
            l = low
            h = 4 * l
    else:
        h = high
    if low is None:
        l = h // 4
    else:
        l = low

    if not h >= l >= 0:
        raise ValueError('high (%r) must be >= low (%r) must be >= 0' %
                         (h, l))

    return h, l
```

## File: `uvloop/includes/fork_handler.h`
```c
#ifndef UVLOOP_FORK_HANDLER_H_
#define UVLOOP_FORK_HANDLER_H_

volatile uint64_t MAIN_THREAD_ID = 0;
volatile int8_t MAIN_THREAD_ID_SET = 0;

typedef void (*OnForkHandler)(void);

OnForkHandler __forkHandler = NULL;

/* Auxiliary function to call global fork handler if defined.

Note: Fork handler needs to be in C (not cython) otherwise it would require
GIL to be present, but some forks can exec non-python processes.
*/
void handleAtFork(void) {
    // Reset the MAIN_THREAD_ID on fork, because the main thread ID is not
    // always the same after fork, especially when forked from within a thread.
    MAIN_THREAD_ID_SET = 0;

    if (__forkHandler != NULL) {
        __forkHandler();
    }
}


void setForkHandler(OnForkHandler handler)
{
    __forkHandler = handler;
}


void resetForkHandler(void)
{
    __forkHandler = NULL;
}

void setMainThreadID(uint64_t id) {
    MAIN_THREAD_ID = id;
    MAIN_THREAD_ID_SET = 1;
}
#endif
```

## File: `uvloop/includes/python.pxd`
```
cdef extern from "Python.h":
    int PY_VERSION_HEX

    unicode PyUnicode_FromString(const char *)

    void* PyMem_RawMalloc(size_t n) nogil
    void* PyMem_RawRealloc(void *p, size_t n) nogil
    void* PyMem_RawCalloc(size_t nelem, size_t elsize) nogil
    void PyMem_RawFree(void *p) nogil

    object PyUnicode_EncodeFSDefault(object)
    void PyErr_SetInterrupt() nogil

    object PyMemoryView_FromMemory(char *mem, ssize_t size, int flags)
    object PyMemoryView_FromObject(object obj)
    int PyMemoryView_Check(object obj)

    cdef enum:
        PyBUF_WRITE


cdef extern from "includes/compat.h":
    object Context_CopyCurrent()
    int Context_Enter(object) except -1
    int Context_Exit(object) except -1

    void PyOS_BeforeFork()
    void PyOS_AfterFork_Parent()
    void PyOS_AfterFork_Child()

    void _Py_RestoreSignals()
```

## File: `uvloop/includes/stdlib.pxi`
```
# flake8: noqa


import asyncio, asyncio.log, asyncio.base_events, \
       asyncio.sslproto, asyncio.coroutines, \
       asyncio.futures, asyncio.transports
import collections.abc
import concurrent.futures
import errno
import functools
import gc
import inspect
import itertools
import os
import signal
import socket
import subprocess
import ssl
import stat
import sys
import threading
import traceback
import time
import warnings
import weakref


cdef aio_get_event_loop = asyncio.get_event_loop
cdef aio_CancelledError = asyncio.CancelledError
cdef aio_InvalidStateError = asyncio.InvalidStateError
cdef aio_TimeoutError = asyncio.TimeoutError
cdef aio_Future = asyncio.Future
cdef aio_Task = asyncio.Task
cdef aio_ensure_future = asyncio.ensure_future
cdef aio_gather = asyncio.gather
cdef aio_wait = asyncio.wait
cdef aio_wrap_future = asyncio.wrap_future
cdef aio_logger = asyncio.log.logger
cdef aio_iscoroutine = asyncio.iscoroutine
cdef aio_BaseProtocol = asyncio.BaseProtocol
cdef aio_Protocol = asyncio.Protocol
cdef aio_isfuture = getattr(asyncio, 'isfuture', None)
cdef aio_get_running_loop = getattr(asyncio, '_get_running_loop', None)
cdef aio_set_running_loop = getattr(asyncio, '_set_running_loop', None)
cdef aio_debug_wrapper = getattr(asyncio.coroutines, 'debug_wrapper', None)
cdef aio_AbstractChildWatcher = getattr(asyncio, "AbstractChildWatcher", ())
cdef aio_Transport = asyncio.Transport
cdef aio_FlowControlMixin = asyncio.transports._FlowControlMixin

cdef col_deque = collections.deque
cdef col_Iterable = collections.abc.Iterable
cdef col_Counter = collections.Counter
cdef col_OrderedDict = collections.OrderedDict

cdef cc_ThreadPoolExecutor = concurrent.futures.ThreadPoolExecutor
cdef cc_Future = concurrent.futures.Future

cdef errno_EBADF = errno.EBADF
cdef errno_EINVAL = errno.EINVAL

cdef ft_partial = functools.partial

cdef gc_disable = gc.disable

cdef iter_chain = itertools.chain
cdef inspect_isgenerator = inspect.isgenerator
cdef inspect_iscoroutinefunction = inspect.iscoroutinefunction

cdef int has_IPV6_V6ONLY = hasattr(socket, 'IPV6_V6ONLY')
cdef int IPV6_V6ONLY = getattr(socket, 'IPV6_V6ONLY', -1)
cdef int has_SO_REUSEPORT = hasattr(socket, 'SO_REUSEPORT')
cdef int SO_REUSEPORT = getattr(socket, 'SO_REUSEPORT', 0)
cdef int SO_BROADCAST = getattr(socket, 'SO_BROADCAST')
cdef int SOCK_NONBLOCK = getattr(socket, 'SOCK_NONBLOCK', -1)
cdef int socket_AI_CANONNAME = getattr(socket, 'AI_CANONNAME')

cdef socket_gaierror = socket.gaierror
cdef socket_error = socket.error
cdef socket_timeout = socket.timeout
cdef socket_socket = socket.socket
cdef socket_socketpair = socket.socketpair
cdef socket_getservbyname = socket.getservbyname
cdef socket_AddressFamily = socket.AddressFamily
cdef socket_SocketKind = socket.SocketKind

cdef int socket_EAI_ADDRFAMILY = getattr(socket, 'EAI_ADDRFAMILY', -1)
cdef int socket_EAI_AGAIN      = getattr(socket, 'EAI_AGAIN', -1)
cdef int socket_EAI_BADFLAGS   = getattr(socket, 'EAI_BADFLAGS', -1)
cdef int socket_EAI_BADHINTS   = getattr(socket, 'EAI_BADHINTS', -1)
cdef int socket_EAI_CANCELED   = getattr(socket, 'EAI_CANCELED', -1)
cdef int socket_EAI_FAIL       = getattr(socket, 'EAI_FAIL', -1)
cdef int socket_EAI_FAMILY     = getattr(socket, 'EAI_FAMILY', -1)
cdef int socket_EAI_MEMORY     = getattr(socket, 'EAI_MEMORY', -1)
cdef int socket_EAI_NODATA     = getattr(socket, 'EAI_NODATA', -1)
cdef int socket_EAI_NONAME     = getattr(socket, 'EAI_NONAME', -1)
cdef int socket_EAI_OVERFLOW   = getattr(socket, 'EAI_OVERFLOW', -1)
cdef int socket_EAI_PROTOCOL   = getattr(socket, 'EAI_PROTOCOL', -1)
cdef int socket_EAI_SERVICE    = getattr(socket, 'EAI_SERVICE', -1)
cdef int socket_EAI_SOCKTYPE   = getattr(socket, 'EAI_SOCKTYPE', -1)


cdef str os_name = os.name
cdef os_environ = os.environ
cdef os_dup = os.dup
cdef os_set_inheritable = os.set_inheritable
cdef os_get_inheritable = os.get_inheritable
cdef os_close = os.close
cdef os_open = os.open
cdef os_devnull = os.devnull
cdef os_O_RDWR = os.O_RDWR
cdef os_pipe = os.pipe
cdef os_read = os.read
cdef os_remove = os.remove
cdef os_stat = os.stat
cdef os_unlink = os.unlink
cdef os_fspath = os.fspath

cdef stat_S_ISSOCK = stat.S_ISSOCK

cdef sys_ignore_environment = sys.flags.ignore_environment
cdef sys_dev_mode = sys.flags.dev_mode
cdef sys_exc_info = sys.exc_info
cdef sys_set_coroutine_wrapper = getattr(sys, 'set_coroutine_wrapper', None)
cdef sys_get_coroutine_wrapper = getattr(sys, 'get_coroutine_wrapper', None)
cdef sys_getframe = sys._getframe
cdef sys_version_info = sys.version_info
cdef sys_getfilesystemencoding = sys.getfilesystemencoding
cdef str sys_platform = sys.platform

cdef ssl_SSLContext = ssl.SSLContext
cdef ssl_MemoryBIO = ssl.MemoryBIO
cdef ssl_create_default_context = ssl.create_default_context
cdef ssl_SSLError = ssl.SSLError
cdef ssl_SSLAgainErrors = (ssl.SSLWantReadError, ssl.SSLSyscallError)
cdef ssl_SSLZeroReturnError = ssl.SSLZeroReturnError
cdef ssl_CertificateError = ssl.CertificateError
cdef int ssl_SSL_ERROR_WANT_READ = ssl.SSL_ERROR_WANT_READ
cdef int ssl_SSL_ERROR_WANT_WRITE = ssl.SSL_ERROR_WANT_WRITE
cdef int ssl_SSL_ERROR_SYSCALL = ssl.SSL_ERROR_SYSCALL

cdef threading_Thread = threading.Thread
cdef threading_main_thread = threading.main_thread

cdef int subprocess_PIPE = subprocess.PIPE
cdef int subprocess_STDOUT = subprocess.STDOUT
cdef int subprocess_DEVNULL = subprocess.DEVNULL
cdef subprocess_SubprocessError = subprocess.SubprocessError

cdef int signal_NSIG = signal.NSIG
cdef signal_signal = signal.signal
cdef signal_siginterrupt = signal.siginterrupt
cdef signal_set_wakeup_fd = signal.set_wakeup_fd
cdef signal_default_int_handler = signal.default_int_handler
cdef signal_SIG_DFL = signal.SIG_DFL

cdef time_sleep = time.sleep
cdef time_monotonic = time.monotonic

cdef tb_StackSummary = traceback.StackSummary
cdef tb_walk_stack = traceback.walk_stack
cdef tb_format_list = traceback.format_list

cdef warnings_warn = warnings.warn

cdef weakref_WeakValueDictionary = weakref.WeakValueDictionary
cdef weakref_WeakSet = weakref.WeakSet

cdef py_inf = float('inf')


# Cython doesn't clean-up imported objects properly in Py3 mode,
# so we delete refs to all modules manually (except sys)
del asyncio, concurrent, collections, errno
del functools, inspect, itertools, socket, os, threading
del signal, subprocess, ssl
del time, traceback, warnings, weakref
```

## File: `uvloop/includes/system.pxd`
```
from libc.stdint cimport int8_t, uint64_t

cdef extern from "arpa/inet.h" nogil:

    int ntohl(int)
    int htonl(int)
    int ntohs(int)


cdef extern from "sys/socket.h" nogil:

    struct sockaddr:
        unsigned short sa_family
        char           sa_data[14]

    struct addrinfo:
        int            ai_flags
        int            ai_family
        int            ai_socktype
        int            ai_protocol
        size_t         ai_addrlen
        sockaddr*      ai_addr
        char*          ai_canonname
        addrinfo*      ai_next

    struct sockaddr_in:
        unsigned short sin_family
        unsigned short sin_port
        # ...

    struct sockaddr_in6:
        unsigned short sin6_family
        unsigned short sin6_port
        unsigned long  sin6_flowinfo
        # ...
        unsigned long  sin6_scope_id

    struct sockaddr_storage:
        unsigned short ss_family
        # ...

    const char *gai_strerror(int errcode)

    int socketpair(int domain, int type, int protocol, int socket_vector[2])

    int setsockopt(int socket, int level, int option_name,
                   const void *option_value, int option_len)


cdef extern from "sys/un.h" nogil:

    struct sockaddr_un:
        unsigned short sun_family
        char*          sun_path
        # ...


cdef extern from "unistd.h" nogil:

    ssize_t write(int fd, const void *buf, size_t count)
    void _exit(int status)


cdef extern from "pthread.h":

    int pthread_atfork(
        void (*prepare)(),
        void (*parent)(),
        void (*child)())


cdef extern from "includes/compat.h" nogil:

    cdef int EWOULDBLOCK

    cdef int PLATFORM_IS_APPLE
    cdef int PLATFORM_IS_LINUX

    struct epoll_event:
        # We don't use the fields
        pass

    int EPOLL_CTL_DEL
    int epoll_ctl(int epfd, int op, int fd, epoll_event *event)
    object MakeUnixSockPyAddr(sockaddr_un *addr)


cdef extern from "includes/fork_handler.h":

    uint64_t MAIN_THREAD_ID
    int8_t MAIN_THREAD_ID_SET
    ctypedef void (*OnForkHandler)()
    void handleAtFork()
    void setForkHandler(OnForkHandler handler)
    void resetForkHandler()
    void setMainThreadID(uint64_t id)


cdef extern from * nogil:
    uint64_t __atomic_fetch_add(uint64_t *ptr, uint64_t val, int memorder)
    uint64_t __atomic_fetch_sub(uint64_t *ptr, uint64_t val, int memorder)

    cdef enum:
        __ATOMIC_RELAXED
```

## File: `uvloop/includes/uv.pxd`
```
from libc.stdint cimport uint16_t, uint32_t, uint64_t, int64_t
from posix.types cimport gid_t, uid_t
from posix.unistd cimport getuid

from . cimport system

# This is an internal enum UV_HANDLE_READABLE from uv-common.h, used only by
# handles/pipe.pyx to temporarily workaround a libuv issue libuv/libuv#2058,
# before there is a proper fix in libuv. In short, libuv disallowed feeding a
# write-only pipe to uv_read_start(), which was needed by uvloop to detect a
# broken pipe without having to send anything on the write-only end. We're
# setting UV_HANDLE_READABLE on pipe_t to workaround this limitation
# temporarily, please see also #317.
cdef enum:
    UV_INTERNAL_HANDLE_READABLE = 0x00004000

cdef extern from "uv.h" nogil:
    cdef int UV_TCP_IPV6ONLY

    cdef int UV_EACCES
    cdef int UV_EAGAIN
    cdef int UV_EALREADY
    cdef int UV_EBUSY
    cdef int UV_ECONNABORTED
    cdef int UV_ECONNREFUSED
    cdef int UV_ECONNRESET
    cdef int UV_ECANCELED
    cdef int UV_EEXIST
    cdef int UV_EINTR
    cdef int UV_EINVAL
    cdef int UV_EISDIR
    cdef int UV_ENOENT
    cdef int UV_EOF
    cdef int UV_EPERM
    cdef int UV_EPIPE
    cdef int UV_ESHUTDOWN
    cdef int UV_ESRCH
    cdef int UV_ETIMEDOUT
    cdef int UV_EBADF
    cdef int UV_ENOBUFS

    cdef int UV_EAI_ADDRFAMILY
    cdef int UV_EAI_AGAIN
    cdef int UV_EAI_BADFLAGS
    cdef int UV_EAI_BADHINTS
    cdef int UV_EAI_CANCELED
    cdef int UV_EAI_FAIL
    cdef int UV_EAI_FAMILY
    cdef int UV_EAI_MEMORY
    cdef int UV_EAI_NODATA
    cdef int UV_EAI_NONAME
    cdef int UV_EAI_OVERFLOW
    cdef int UV_EAI_PROTOCOL
    cdef int UV_EAI_SERVICE
    cdef int UV_EAI_SOCKTYPE

    cdef int SOL_SOCKET
    cdef int SO_ERROR
    cdef int SO_REUSEADDR
    # use has_SO_REUSEPORT and SO_REUSEPORT in stdlib.pxi instead
    cdef int AF_INET
    cdef int AF_INET6
    cdef int AF_UNIX
    cdef int AF_UNSPEC
    cdef int AI_PASSIVE
    cdef int AI_NUMERICHOST
    cdef int INET6_ADDRSTRLEN
    cdef int IPPROTO_IPV6
    cdef int SOCK_STREAM
    cdef int SOCK_DGRAM
    cdef int IPPROTO_TCP
    cdef int IPPROTO_UDP

    cdef int SIGINT
    cdef int SIGHUP
    cdef int SIGCHLD
    cdef int SIGKILL
    cdef int SIGTERM

    ctypedef int uv_os_sock_t
    ctypedef int uv_file
    ctypedef int uv_os_fd_t

    ctypedef struct uv_buf_t:
        char* base
        size_t len

    ctypedef struct uv_loop_t:
        void* data
        # ...

    ctypedef struct uv_handle_t:
        void* data
        uv_loop_t* loop
        unsigned int flags
        # ...

    ctypedef struct uv_idle_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_check_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_signal_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_async_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_timer_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_stream_t:
        void* data
        size_t write_queue_size
        uv_loop_t* loop
        # ...

    ctypedef struct uv_tcp_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_pipe_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_udp_t:
        void* data
        uv_loop_t* loop
        size_t send_queue_size
        size_t send_queue_count
        # ...

    ctypedef struct uv_udp_send_t:
        void* data
        uv_udp_t* handle

    ctypedef struct uv_poll_t:
        void* data
        uv_loop_t* loop
        # ...

    ctypedef struct uv_req_t:
        # Only cancellation of uv_fs_t, uv_getaddrinfo_t,
        # uv_getnameinfo_t and uv_work_t requests is
        # currently supported.
        void* data
        uv_req_type type
        # ...

    ctypedef struct uv_connect_t:
        void* data

    ctypedef struct uv_getaddrinfo_t:
        void* data
        # ...

    ctypedef struct uv_getnameinfo_t:
        void* data
        # ...

    ctypedef struct uv_write_t:
        void* data
        # ...

    ctypedef struct uv_shutdown_t:
        void* data
        # ...

    ctypedef struct uv_process_t:
        void* data
        int pid
        # ...

    ctypedef struct uv_fs_event_t:
        void* data
        # ...

    ctypedef enum uv_req_type:
        UV_UNKNOWN_REQ = 0,
        UV_REQ,
        UV_CONNECT,
        UV_WRITE,
        UV_SHUTDOWN,
        UV_UDP_SEND,
        UV_FS,
        UV_WORK,
        UV_GETADDRINFO,
        UV_GETNAMEINFO,
        UV_REQ_TYPE_PRIVATE,
        UV_REQ_TYPE_MAX

    ctypedef enum uv_run_mode:
        UV_RUN_DEFAULT = 0,
        UV_RUN_ONCE,
        UV_RUN_NOWAIT

    ctypedef enum uv_poll_event:
        UV_READABLE = 1,
        UV_WRITABLE = 2,
        UV_DISCONNECT = 4

    ctypedef enum uv_udp_flags:
        UV_UDP_IPV6ONLY = 1,
        UV_UDP_PARTIAL = 2

    ctypedef enum uv_membership:
        UV_LEAVE_GROUP = 0,
        UV_JOIN_GROUP

    cdef enum uv_fs_event:
        UV_RENAME = 1,
        UV_CHANGE = 2

    const char* uv_strerror(int err)
    const char* uv_err_name(int err)

    ctypedef void (*uv_walk_cb)(uv_handle_t* handle, void* arg) with gil

    ctypedef void (*uv_close_cb)(uv_handle_t* handle) with gil
    ctypedef void (*uv_idle_cb)(uv_idle_t* handle) with gil
    ctypedef void (*uv_check_cb)(uv_check_t* handle) with gil
    ctypedef void (*uv_signal_cb)(uv_signal_t* handle, int signum) with gil
    ctypedef void (*uv_async_cb)(uv_async_t* handle) with gil
    ctypedef void (*uv_timer_cb)(uv_timer_t* handle) with gil
    ctypedef void (*uv_connection_cb)(uv_stream_t* server, int status) with gil
    ctypedef void (*uv_alloc_cb)(uv_handle_t* handle,
                                 size_t suggested_size,
                                 uv_buf_t* buf) with gil
    ctypedef void (*uv_read_cb)(uv_stream_t* stream,
                                ssize_t nread,
                                const uv_buf_t* buf) with gil
    ctypedef void (*uv_write_cb)(uv_write_t* req, int status) with gil
    ctypedef void (*uv_getaddrinfo_cb)(uv_getaddrinfo_t* req,
                                       int status,
                                       system.addrinfo* res) with gil
    ctypedef void (*uv_getnameinfo_cb)(uv_getnameinfo_t* req,
                                       int status,
                                       const char* hostname,
                                       const char* service) with gil
    ctypedef void (*uv_shutdown_cb)(uv_shutdown_t* req, int status) with gil
    ctypedef void (*uv_poll_cb)(uv_poll_t* handle,
                                int status, int events) with gil

    ctypedef void (*uv_connect_cb)(uv_connect_t* req, int status) with gil

    ctypedef void (*uv_udp_send_cb)(uv_udp_send_t* req, int status) with gil
    ctypedef void (*uv_udp_recv_cb)(uv_udp_t* handle,
                                    ssize_t nread,
                                    const uv_buf_t* buf,
                                    const system.sockaddr* addr,
                                    unsigned flags) with gil
    ctypedef void (*uv_fs_event_cb)(uv_fs_event_t* handle,
                                    const char *filename,
                                    int events,
                                    int status) with gil

    # Generic request functions
    int uv_cancel(uv_req_t* req)

    # Generic handler functions
    int uv_is_active(const uv_handle_t* handle)
    void uv_close(uv_handle_t* handle, uv_close_cb close_cb)
    int uv_is_closing(const uv_handle_t* handle)
    int uv_fileno(const uv_handle_t* handle, uv_os_fd_t* fd)
    void uv_walk(uv_loop_t* loop, uv_walk_cb walk_cb, void* arg)

    # Loop functions
    int uv_loop_init(uv_loop_t* loop)
    int uv_loop_close(uv_loop_t* loop)
    int uv_loop_alive(uv_loop_t* loop)
    int uv_loop_fork(uv_loop_t* loop)
    uv_os_fd_t uv_backend_fd(uv_loop_t* loop)

    void uv_update_time(uv_loop_t* loop)
    uint64_t uv_now(const uv_loop_t*)

    int uv_run(uv_loop_t*, uv_run_mode mode) nogil
    void uv_stop(uv_loop_t*)

    # Idle handler
    int uv_idle_init(uv_loop_t*, uv_idle_t* idle)
    int uv_idle_start(uv_idle_t* idle, uv_idle_cb cb)
    int uv_idle_stop(uv_idle_t* idle)

    # Check handler
    int uv_check_init(uv_loop_t*, uv_check_t* idle)
    int uv_check_start(uv_check_t* check, uv_check_cb cb)
    int uv_check_stop(uv_check_t* check)

    # Signal handler
    int uv_signal_init(uv_loop_t* loop, uv_signal_t* handle)
    int uv_signal_start(uv_signal_t* handle,
                        uv_signal_cb signal_cb,
                        int signum)
    int uv_signal_stop(uv_signal_t* handle)

    # Async handler
    int uv_async_init(uv_loop_t*,
                      uv_async_t* async_,
                      uv_async_cb async_cb)
    int uv_async_send(uv_async_t* async_)

    # Timer handler
    int uv_timer_init(uv_loop_t*, uv_timer_t* handle)
    int uv_timer_start(uv_timer_t* handle,
                       uv_timer_cb cb,
                       uint64_t timeout,
                       uint64_t repeat)
    int uv_timer_stop(uv_timer_t* handle)

    # DNS
    int uv_getaddrinfo(uv_loop_t* loop,
                       uv_getaddrinfo_t* req,
                       uv_getaddrinfo_cb getaddrinfo_cb,
                       const char* node,
                       const char* service,
                       const system.addrinfo* hints)

    void uv_freeaddrinfo(system.addrinfo* ai)

    int uv_getnameinfo(uv_loop_t* loop,
                       uv_getnameinfo_t* req,
                       uv_getnameinfo_cb getnameinfo_cb,
                       const system.sockaddr* addr,
                       int flags)

    int uv_ip4_name(const system.sockaddr_in* src, char* dst, size_t size)
    int uv_ip6_name(const system.sockaddr_in6* src, char* dst, size_t size)

    # Streams

    int uv_listen(uv_stream_t* stream, int backlog, uv_connection_cb cb)
    int uv_accept(uv_stream_t* server, uv_stream_t* client)
    int uv_read_start(uv_stream_t* stream,
                      uv_alloc_cb alloc_cb,
                      uv_read_cb read_cb)
    int uv_read_stop(uv_stream_t*)
    int uv_write(uv_write_t* req, uv_stream_t* handle,
                 uv_buf_t bufs[], unsigned int nbufs, uv_write_cb cb)

    int uv_try_write(uv_stream_t* handle, uv_buf_t bufs[], unsigned int nbufs)

    int uv_shutdown(uv_shutdown_t* req, uv_stream_t* handle, uv_shutdown_cb cb)

    int uv_is_readable(const uv_stream_t* handle)
    int uv_is_writable(const uv_stream_t* handle)

    # TCP

    int uv_tcp_init_ex(uv_loop_t*, uv_tcp_t* handle, unsigned int flags)
    int uv_tcp_nodelay(uv_tcp_t* handle, int enable)
    int uv_tcp_keepalive(uv_tcp_t* handle, int enable, unsigned int delay)
    int uv_tcp_open(uv_tcp_t* handle, uv_os_sock_t sock)
    int uv_tcp_bind(uv_tcp_t* handle, system.sockaddr* addr,
                    unsigned int flags)

    int uv_tcp_getsockname(const uv_tcp_t* handle, system.sockaddr* name,
                           int* namelen)
    int uv_tcp_getpeername(const uv_tcp_t* handle, system.sockaddr* name,
                           int* namelen)

    int uv_tcp_connect(uv_connect_t* req, uv_tcp_t* handle,
                       const system.sockaddr* addr, uv_connect_cb cb)

    # Pipes

    int uv_pipe_init(uv_loop_t* loop, uv_pipe_t* handle, int ipc)
    int uv_pipe_open(uv_pipe_t* handle, uv_os_fd_t file)
    int uv_pipe_bind(uv_pipe_t* handle, const char* name)

    void uv_pipe_connect(uv_connect_t* req, uv_pipe_t* handle,
                         const char* name, uv_connect_cb cb)

    # UDP

    int uv_udp_init_ex(uv_loop_t* loop, uv_udp_t* handle, unsigned int flags)
    int uv_udp_connect(uv_udp_t* handle, const system.sockaddr* addr)
    int uv_udp_open(uv_udp_t* handle, uv_os_sock_t sock)
    int uv_udp_bind(uv_udp_t* handle, const system.sockaddr* addr,
                    unsigned int flags)
    int uv_udp_send(uv_udp_send_t* req, uv_udp_t* handle,
                    const uv_buf_t bufs[], unsigned int nbufs,
                    const system.sockaddr* addr, uv_udp_send_cb send_cb)
    int uv_udp_try_send(uv_udp_t* handle,
                        const uv_buf_t bufs[], unsigned int nbufs,
                        const system.sockaddr* addr)
    int uv_udp_recv_start(uv_udp_t* handle, uv_alloc_cb alloc_cb,
                          uv_udp_recv_cb recv_cb)
    int uv_udp_recv_stop(uv_udp_t* handle)
    int uv_udp_set_broadcast(uv_udp_t* handle, int on)

    # Polling

    int uv_poll_init(uv_loop_t* loop, uv_poll_t* handle, int fd)
    int uv_poll_init_socket(uv_loop_t* loop, uv_poll_t* handle,
                            uv_os_sock_t socket)
    int uv_poll_start(uv_poll_t* handle, int events, uv_poll_cb cb)
    int uv_poll_stop(uv_poll_t* poll)

    # FS Event

    int uv_fs_event_init(uv_loop_t *loop, uv_fs_event_t *handle)
    int uv_fs_event_start(uv_fs_event_t *handle, uv_fs_event_cb cb,
                          const char *path, unsigned int flags)
    int uv_fs_event_stop(uv_fs_event_t *handle)

    # Misc

    ctypedef struct uv_timeval_t:
        long tv_sec
        long tv_usec

    ctypedef struct uv_rusage_t:
        uv_timeval_t ru_utime   # user CPU time used
        uv_timeval_t ru_stime   # system CPU time used
        uint64_t ru_maxrss      # maximum resident set size
        uint64_t ru_ixrss       # integral shared memory size
        uint64_t ru_idrss       # integral unshared data size
        uint64_t ru_isrss       # integral unshared stack size
        uint64_t ru_minflt      # page reclaims (soft page faults)
        uint64_t ru_majflt      # page faults (hard page faults)
        uint64_t ru_nswap       # swaps
        uint64_t ru_inblock     # block input operations
        uint64_t ru_oublock     # block output operations
        uint64_t ru_msgsnd      # IPC messages sent
        uint64_t ru_msgrcv      # IPC messages received
        uint64_t ru_nsignals    # signals received
        uint64_t ru_nvcsw       # voluntary context switches
        uint64_t ru_nivcsw      # involuntary context switches

    int uv_getrusage(uv_rusage_t* rusage)

    int uv_ip4_addr(const char* ip, int port, system.sockaddr_in* addr)
    int uv_ip6_addr(const char* ip, int port, system.sockaddr_in6* addr)

    # Memory Allocation

    ctypedef void* (*uv_malloc_func)(size_t size)
    ctypedef void* (*uv_realloc_func)(void* ptr, size_t size)
    ctypedef void* (*uv_calloc_func)(size_t count, size_t size)
    ctypedef void (*uv_free_func)(void* ptr)

    int uv_replace_allocator(uv_malloc_func malloc_func,
                             uv_realloc_func realloc_func,
                             uv_calloc_func calloc_func,
                             uv_free_func free_func)

    # Process

    ctypedef void (*uv_exit_cb)(uv_process_t*, int64_t exit_status,
                                int term_signal) with gil

    ctypedef enum uv_process_flags:
        UV_PROCESS_SETUID = 1,
        UV_PROCESS_SETGID = 2,
        UV_PROCESS_WINDOWS_VERBATIM_ARGUMENTS = 4,
        UV_PROCESS_DETACHED = 8,
        UV_PROCESS_WINDOWS_HIDE = 16

    ctypedef enum uv_stdio_flags:
        UV_IGNORE = 0x00,
        UV_CREATE_PIPE = 0x01,
        UV_INHERIT_FD = 0x02,
        UV_INHERIT_STREAM = 0x04,
        UV_READABLE_PIPE = 0x10,
        UV_WRITABLE_PIPE = 0x20

    ctypedef union uv_stdio_container_data_u:
        uv_stream_t* stream
        int fd

    ctypedef struct uv_stdio_container_t:
        uv_stdio_flags flags
        uv_stdio_container_data_u data

    ctypedef struct uv_process_options_t:
        uv_exit_cb exit_cb
        char* file
        char** args
        char** env
        char* cwd
        unsigned int flags
        int stdio_count
        uv_stdio_container_t* stdio
        uid_t uid
        gid_t gid

    int uv_spawn(uv_loop_t* loop, uv_process_t* handle,
                 const uv_process_options_t* options)

    int uv_process_kill(uv_process_t* handle, int signum)

    unsigned int uv_version()
```

