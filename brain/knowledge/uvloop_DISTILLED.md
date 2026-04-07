---
id: uvloop
type: knowledge
owner: OA_Triage
---
# uvloop
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: setup.py
```py
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

### File: .github\ISSUE_TEMPLATE.md
```md
<!--
Thanks for wanting to report an issue you've found in uvloop. Please fill in
the template below.

It will be much easier for us to fix the issue if a test case that reproduces
the problem is provided, with clear instructions on how to run it.

Thank you!
-->

* **uvloop version**:
* **Python version**:
* **Platform**:
* **Can you reproduce the bug with `PYTHONASYNCIODEBUG` in env?**:
* **Does uvloop behave differently from vanilla asyncio? How?**:

<!-- Enter your issue details below this comment. -->

```

### File: .github\release_log.py
```py
#!/usr/bin/env python3


import argparse
import json
import requests
import re


BASE_URL = 'https://api.github.com/repos/magicstack/uvloop/compare'


def main():
    parser = argparse.ArgumentParser(
        description='Generate release log.')
    parser.add_argument('--to', dest='to_hash', default='master', type=str)
    parser.add_argument('--from', dest='from_hash', type=str)
    args = parser.parse_args()

    r = requests.get(f'{BASE_URL}/{args.from_hash}...{args.to_hash}')
    data = json.loads(r.text)

    for commit in data['commits']:
        message = commit['commit']['message']
        first_line = message.partition('\n\n')[0]
        if commit.get('author'):
            username = '@{}'.format(commit['author']['login'])
        else:
            username = commit['commit']['author']['name']
        sha = commit["sha"][:8]

        m = re.search(r'\#(?P<num>\d+)\b', message)
        if m:
            issue_num = m.group('num')
        else:
            issue_num = None

        print(f'* {first_line}')
        print(f'  (by {username} in {sha}', end='')
        if issue_num:
            print(f' for #{issue_num})')
        else:
            print(')')
        print()


if __name__ == '__main__':
    main()

```

### File: docs\conf.py
```py
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

### File: tests\test_aiohttp.py
```py
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

### File: tests\test_base.py
```py
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
            def z
... [TRUNCATED]
```

### File: tests\test_context.py
```py
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
               
... [TRUNCATED]
```

### File: tests\test_cython.py
```py
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

### File: tests\test_dealloc.py
```py
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

### File: tests\test_dns.py
```py
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
