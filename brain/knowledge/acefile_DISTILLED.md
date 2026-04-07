---
id: acefile
type: knowledge
owner: OA_Triage
---
# acefile
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# acefile - read/test/extract ACE 1.0 and 2.0 archives in pure python
Copyright (C) 2017-2026, [Daniel Roethlisberger](//daniel.roe.ch/).  
https://www.roe.ch/acefile  


## Synopsis

    pip install acefile

    # python library
    import acefile
    with acefile.open('example.ace') as f:
        f.extractall()

    # unace utility
    acefile-unace -x example.ace


## Overview

This single-file, pure python 3, no-dependencies implementation is intended
to be used as a library, but also provides a stand-alone unace utility.
As mostly pure-python implementation, it is significantly slower than
native implementations, but more robust against vulnerabilities.

This implementation supports up to version 2.0 of the ACE archive format,
including the EXE, DELTA, PIC and SOUND modes of ACE 2.0, password protected
archives and multi-volume archives.  It does not support writing to archives.
It is an implementation from scratch, based on the 1998 document titled
"Technical information of the archiver ACE v1.2" by Marcel Lemke, using
unace 2.5 and WinAce 2.69 by Marcel Lemke as reference implementations.

For more information, API documentation, source code, packages and release
notifications, refer to:

- https://www.roe.ch/acefile
- https://apidoc.roe.ch/acefile
- https://github.com/droe/acefile
- https://pypi.python.org/pypi/acefile
- https://infosec.exchange/@droe


## Requirements

Python 3.  No other dependencies.


## Installation

    pip install acefile

The `acefile` package includes an optional `acebitstream` module that
implements the bit stream class in c, resulting in a 50% speedup.
It is automatically used wherever it builds cleanly, but is not required.


## Library usage examples

Extract all files in the archive, with directories, to current working dir:

    import acefile
    with acefile.open('example.ace') as f:
        f.extractall()

Walk all files in the archive and test each one of them:

    import acefile
    with acefile.open('example.ace') as f:
        for member in f:
            if member.is_dir():
                continue
            if f.test(member):
                print("CRC OK:     %s" % member.filename)
            else:
                print("CRC FAIL:   %s" % member.filename)

In-memory decompression of a specific archive member:

    import acefile
    import io

    filelike = io.BytesIO(b'\x73\x83\x31\x00\x00\x00\x90**ACE**\x14\x14' ...)
    with acefile.open(filelike) as f:
        data = f.read('example.txt')

Handle archives potentially containing large members in chunks to avoid fully
reading them into memory:

    import acefile

    with acefile.open('large.ace') as fi:
        with open('large.iso', 'wb') as fo:
            for block in fi.readblocks('large.iso'):
                fo.write(block)

Check the [API documentation](https://apidoc.roe.ch/acefile) for a complete
description of the API.


## Utility usage examples

Extract all files in the archive, with directories, to current working dir:

    acefile-unace -x example.ace

Test all files in the archive, verbosely:

    acefile-unace -tv example.ace

List archive contents, verbosely:

    acefile-unace -lv example.ace

Check usage for more functionality:

    acefile-unace -h


## Testing

This project uses docstrings for unit testing:

    ./acefile.py --doctest

This project uses pytest for integration testing, recursively looking for
corpora of ACE archives in `../acefile-testdata/` and
`../acefile-testdata-private/`.  The former is intended for a checkout of
[droe/acefile-testdata](https://github.com/droe/acefile-testdata).  The latter
is intended for a developer-local test corpus that might be impractically large
or contain data that cannot be redistributed.  Both are optional, the
integration tests are currently not useful without any test archives though.

    git clone https://github.com/droe/acefile-testdata.git ../acefile-testdata
    pytest -v


## Credits

Marcel Lemke for designing the ACE archive format and ACE compression and
decompression algorithms.


```

### File: requirements.txt
```txt
setuptools

```

### File: setup.py
```py
#!/usr/bin/env python3

from setuptools import setup, find_packages
from setuptools.extension import Extension
import re
import sys
import acefile

if 'sdist' in sys.argv:
    assert re.match(r'[0-9]+\.[0-9]+\.[0-9]+$', acefile.__version__)

title, desc = acefile.__doc__.strip().split('\n', 1)
desc = desc.strip()

def run_setup(with_optional_extensions):
    if with_optional_extensions:
        ext_modules=[Extension(
            "acebitstream", ["c/acebitstream_mod.c", "c/acebitstream.c"],
            define_macros=[(sys.byteorder.upper()+'_ENDIAN_SWAP', 1)]
        )]
    else:
        ext_modules=[]

    setup(
        name='acefile',
        version=acefile.__version__,
        description=title,
        long_description=desc,
        url=acefile.__url__,
        author=acefile.__author__,
        author_email=acefile.__email__,
        license=acefile.__license__,
        platforms=['all'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
            'Topic :: System :: Archiving :: Compression',
        ],
        keywords=['ace', 'unace', 'compression', 'decompression', 'archive'],
        py_modules=['acefile'],
        ext_modules=ext_modules,
        entry_points={
            'console_scripts': [
                'acefile-unace=acefile:unace',
            ],
        },
    )

try:
    run_setup(True)
except Exception as e:
    print('=' * 78)
    print(f'WARNING: Installation failed with {type(e).__name__}: {e}!')
    print('Retrying setup without C extensions enabled.')
    print('=' * 78)
    try:
        run_setup(False)
        print('=' * 78)
        print('WARNING: The optional C extensions failed to install!')
        print('The module will still be functional, but significantly slower.')
        print('=' * 78)
    except Exception as eprime:
        print('=' * 78)
        print(f'WARNING: Installation failed with {type(eprime).__name__}: {eprime}!')
        print('ERROR: Failed w/o C extensions too, issue likely unrelated to C.')
        print('=' * 78)
        raise


```

### File: acefile.py
```py
#!/usr/bin/env python3

# acefile - read/test/extract ACE 1.0 and 2.0 archives in pure python
# Copyright (C) 2017-2026, Daniel Roethlisberger <daniel@roe.ch>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# NOTE:  The ACE archive format and ACE compression and decompression
# algorithms have been designed by Marcel Lemke.  The above copyright
# notice and license does not constitute a claim of intellectual property
# over ACE technology beyond the copyright of this python implementation.

"""
Read/test/extract ACE 1.0 and 2.0 archives in pure python.

This single-file, pure python 3, no-dependencies implementation is intended
to be used as a library, but also provides a stand-alone unace utility.
As mostly pure-python implementation, it is significantly slower than
native implementations, but more robust against vulnerabilities.

This implementation supports up to version 2.0 of the ACE archive format,
including the EXE, DELTA, PIC and SOUND modes of ACE 2.0, password protected
archives and multi-volume archives.  It does not support writing to archives.
It is an implementation from scratch, based on the 1998 document titled
"Technical information of the archiver ACE v1.2" by Marcel Lemke, using
unace 2.5 and WinAce 2.69 by Marcel Lemke as reference implementations.

For more information, API documentation, source code, packages and release
notifications, refer to:

- https://www.roe.ch/acefile
- https://apidoc.roe.ch/acefile
- https://github.com/droe/acefile
- https://pypi.python.org/pypi/acefile
- https://infosec.exchange/@droe
"""

__version__     = '0.6.14'
__author__      = 'Daniel Roethlisberger'
__email__       = 'daniel@roe.ch'
__copyright__   = 'Copyright 2017-2026, Daniel Roethlisberger'
__credits__     = ['Marcel Lemke']
__license__     = 'BSD-2-Clause'
__url__         = 'https://www.roe.ch/acefile'



import array
import builtins
import ctypes
import datetime
import errno
import io
import math
import os
import platform
import re
import stat
import struct
import sys
import zlib



_ACEFILE_FORCE_ACEBITSTREAM = os.environ.get('ACEFILE_FORCE_ACEBITSTREAM', None)
if _ACEFILE_FORCE_ACEBITSTREAM == '1':
    import acebitstream
elif _ACEFILE_FORCE_ACEBITSTREAM == '0':
    acebitstream = None
else:
    try:
        import acebitstream
    except:
        acebitstream = None



# Very basic debugging facility; if set to True, exceptions raised during
# testing of archives will be raised and a minimal set of state information
# will be printed to stderr.
DEBUG = False



# Arbitrarily chosen buffer size to use for buffered file operations that
# have no obvious natural block size.
FILE_BLOCKSIZE = 131072
assert FILE_BLOCKSIZE % 4 == 0



if platform.system() == 'Windows':
    # BOOL WINAPI SetFileAttributes(
    #   _In_ LPCTSTR lpFileName,
    #   _In_ DWORD   dwFileAttributes
    # );
    try:
        SetFileAttributes = ctypes.windll.kernel32.SetFileAttributesW
    except:
        SetFileAttributes = None
    # BOOL WINAPI SetFileSecurity(
    #  _In_ LPCTSTR              lpFileName,
    #  _In_ SECURITY_INFORMATION SecurityInformation,
    #  _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor
    # );
    try:
        SetFileSecurity = ctypes.windll.advapi32.SetFileSecurityW
    except:
        SetFileSecurity = None
else:
    SetFileAttributes = None
    SetFileSecurity = None



def eprint(*args, **kwargs):
    """
    Print to stderr.
    """
    print(*args, file=sys.stderr, **kwargs)



# haklib.dt
def _dt_fromdos(dosdt):
    """
    Convert DOS format 32bit timestamp to datetime object.
    Timestamps with illegal values out of the allowed range are ignored and a
    datetime object representing 1980-01-01 00:00:00 is returned instead.
    https://msdn.microsoft.com/en-us/library/9kkf9tah.aspx

    >>> _dt_fromdos(0x4a5c48fd)
    datetime.datetime(2017, 2, 28, 9, 7, 58)
    >>> _dt_fromdos(0)
    datetime.datetime(1980, 1, 1, 0, 0)
    >>> _dt_fromdos(-1)
    datetime.datetime(1980, 1, 1, 0, 0)
    """
    try:
        return datetime.datetime(
                ((dosdt >> 25) & 0x7F) + 1980,
                 (dosdt >> 21) & 0x0F,
                 (dosdt >> 16) & 0x1F,
                 (dosdt >> 11) & 0x1F,
                 (dosdt >>  5) & 0x3F,
                ((dosdt      ) & 0x1F) * 2)
    except ValueError:
        return datetime.datetime(1980, 1, 1, 0, 0, 0)



# haklib.c
def c_div(q, d):
    """
    Arbitrary signed integer division with c behaviour.

    >>> (c_div(10, 3), c_div(-10, -3), c_div(-10, 3), c_div(10, -3))
    (3, 3, -3, -3)
    >>> c_div(-11, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError
    """
    s = int(math.copysign(1, q) * math.copysign(1, d))
    return s * int(abs(q) / abs(d))

def c_schar(i):
    """
    Convert arbitrary integer to c signed char type range as if casted in c.

    >>> c_schar(0x12345678)
    120
    >>> (c_schar(-128), c_schar(-129), c_schar(127), c_schar(128))
    (-128, 127, 127, -128)
    """
    return ((i + 128) % 256) - 128

def c_uchar(i):
    """
    Convert arbitrary integer to c unsigned char type range as if casted in c.

    >>> c_uchar(0x12345678)
    120
    >>> (c_uchar(-123), c_uchar(-1), c_uchar(255), c_uchar(256))
    (133, 255, 255, 0)
    """
    return i & 0xFF

def c_rot32(i, n):
    """
    Rotate *i* left by *n* bits within the uint32 value range.

    >>> c_rot32(0xF0000000, 4)
    15
    >>> c_rot32(0xF0, -4)
    15
    """
    if n < 0:
        n = 32 + n
    return (((i << n) & 0xFFFFFFFF) | (i >> (32 - n)))

def c_add32(a, b):
    """
    Add *a* and *b* within the uint32 value range.

    >>> c_add32(0xFFFFFFFF, 1)
    0
    >>> c_add32(0xFFFFFFFF, 0xFFFFFFFF)
    4294967294
    """
    return (a + b) & 0xFFFFFFFF

def c_sum32(*args):
    """
    Add all elements of *args* within the uint32 value range.

    >>> c_sum32(0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF)
    4294967293
    """
    return sum(args) & 0xFFFFFFFF



def asciibox(msg, title=None, minwidth=None):
    """
    Returns message string *msg* wrapped in a plain ASCII box.
    If *title* is given, add *title* in the top horizontal bar.
    Lines will be padded to the longest out of *minwidth* characters, the
    length of the longest line, or the length of the title plus six.
    Caller is responsible for ensuring a sensible line length in *msg*.
    """
    out = []
    lines = msg.splitlines()
    width = 0
    for line in lines:
        width = max(width, len(line))
    if minwidth != None:
        width = max(width, minwidth)
    if title != None:
        width = max(width, len(title) + 6)
    ftr = "+" + ("-" * (width + 2)) + "+"
    if title != None:
        hdr = ("+--[ %s ]--" % title) + ("-" * (width - 6 - len(title))) + "+"
    else:
        hdr = ftr
    fmt = "| %%-%is |" % width
    out.append(hdr)
    for line in msg.splitlines():
        out.append(fmt % line)
    out.append(ftr)
    return '\n'.join(out)



class FileSegmentIO:
    """
    Seekable file-like object that wraps and reads from seekable file-like
    object and fakes EOF when a read would extend beyond a defined boundary.

    >>> FileSegmentIO(io.BytesIO(b'0123456789'), 3, 4).read()
    b'3456'
    >>> f = FileSegmentIO(io.BytesIO(b'0123456789'), 3, 4)
    >>> f.seekable()
    True
    >>> f.seek(0)
    0
    >>> f.read(1)
    b'3'
    >>> f.seek(1, os.SEEK_CUR)
    2
    >>> f.read(1)
    b'5'
    >>> f.seek(0, os.SEEK_END)
    4
    >>> f.read(1)
    b''
    >>> f.seek(-1, os.SEEK_SET)
    Traceback (most recent call last):
        ...
    OSError
    >>> f.seek(1, os.SEEK_END)
    Traceback (most recent call last):
        ...
    OSError
    """
    def __init__(self, f, base, size):
        assert f.seekable()
        self.__file = f
        self.__base = base
        self.__eof = base + size
        self.__file.seek(self.__base)

    def seekable(self):
        return True

    def _tell(self):
        """
        Returns the current absolute position in the file and asserts that it
        lies within the defined file segment.
        """
        pos = self.__file.tell()
        assert pos >= self.__base and pos <= self.__eof
        return pos

    def tell(self):
        return self._tell() - self.__base

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            newpos = self.__base + offset
        elif whence == os.SEEK_CUR:
            newpos = self._tell() + offset
        elif whence == os.SEEK_END:
            newpos = self.__eof + offset
        if not (newpos >= self.__base and newpos <= self.__eof):
            raise OSError(errno.EINVAL, os.strerror(errno.EINVAL))
        self.__file.seek(newpos)
        return newpos - self.__base

    def read(self, n=None):
        pos = self._tell()
        if n == None:
            amount = self.__eof - pos
        else:
            amount = min(n, self.__eof - pos)
        if amount == 0:
            return b''
        return self.__file.read(amount)



class MultipleFilesIO:
    """
    Seekable file-like object that wraps and reads from multiple
    seekable lower-level file-like objects.

    >>> MultipleFilesIO((io.BytesIO(b'01234'), io.BytesIO(b'56789'))).read()
    b'0123456789'
    >>> f = MultipleFilesIO((io.BytesIO(b'01234'), io.BytesIO(b'56789')))
    >>> f.seekable()
    True
    >>> f.seek(0)
    0
    >>> f.read(1)
    b'0'
    >>> f.seek(1, os.SEEK_CUR)
    2
    >>> f.read(1)
    b'2'
    >>> f.seek(0, os.SEEK_END)
    10
    >>> f.read(1)
    b''
    >>> f.seek(-1, os.SEEK_SET)
    Traceback (most recent call last):
        ...
    OSError
    >>> f.seek(1, os.SEEK_END)
    Traceback (most recent call last):
        ...
    OSError
    """
    def __init__(self, files):
        assert len(files) > 0
        self.__files = files
        self.__sizes = []
        for f in files:
            f.seek(0, os.SEEK_END)
            self.__sizes.append(f.tell())
        self.__files[0].seek(0)
        self.__idx = 0
        self.__pos = 0
        self.__eof = sum(self.__sizes)

    def seekable(self):
        return True

    def tell(self):
        return self.__pos

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            newpos = offset
        elif whence == os.SEEK_CUR:
            newpos = self.__pos + offset
        elif whence == os.SEEK_END:
            newpos = self.__eof + offset
        if not (newpos >= 0 and newpos <= self.__eof):
            raise OSError(errno.EINVAL, os.strerror(errno.EINVAL))
        idx = 0
        relpos = newpos
        while relpos > self.__sizes[idx]:
            relpos -= self.__sizes[idx]
            idx += 1
        self.__files[idx].seek(relpos)
        self.__idx = idx
        return newpos

    def read(self, n=None):
        if n == None:
            n = self.__eof - self.__pos
        out = []
        have_size = 0
        while have_size < n:
            if self.__idx >= len(self.__files):
                break
            chunk = self.__files[self.__idx].read(n - have_size)
            if len(chunk) == 0:
                self.__idx += 1
                if self.__idx < len(self.__files):
                    self.__files[self.__idx].seek(0)
                continue
            out.append(chunk)
            self.__pos += len(chunk)
            have_size += len(chunk)
        return b''.join(out)



class EncryptedFileIO:
    """
    Non-seekable file-like object that reads from a lower-level seekable
    file-like object, and transparently decrypts the data stream using a
    decryption engine.  The decryption engine is assumed to support a
    decrypt() method and a blocksize property.  The underlying file-like
    object is expected to contain a multiple of blocksize bytes, if not,
    CorruptedArchiveError is raised.

    >>> EncryptedFileIO(io.BytesIO(b'7'*16), AceBlowfish(b'123456789')).read()
    b'\\t_\\xd0a}\\x1dh\\xdd>h\\xe7VJ*_\\xea'
    >>> EncryptedFileIO(io.BytesIO(b'7'*17), AceBlowfish(b'123456789')).read()
    Traceback (most recent call last):
        ...
    CorruptedArchiveError
    >>> f = EncryptedFileIO(io.BytesIO(b'7'*16), AceBlowfish(b'123456789'))
    >>> f.seekable()
    False
    """
    def __init__(self, f, engine):
        self.__file = f
        self.__file.seek(0, os.SEEK_END)
        self.__eof = self.__file.tell()
        self.__file.seek(0)
        self.__engine = engine
        self.__buffer = b''

    def seekable(self):
        return False

    def read(self, n=None):
        if n == None:
            n = self.__eof - (self.__file.tell() - len(self.__buffer))
        if n < len(self.__buffer):
            rbuf = self.__buffer[:n]
            self.__buffer = self.__buffer[n:]
            return rbuf
        want_bytes = n - len(self.__buffer)
        read_bytes = want_bytes
        blocksize = self.__engine.blocksize
        if want_bytes % blocksize:
            read_bytes += blocksize - (want_bytes % blocksize)
        buf = self.__file.read(read_bytes)
        if len(buf) % blocksize:
            raise CorruptedArchiveError("Truncated ciphertext block")
        buf = self.__engine.decrypt(buf)
        rbuf = self.__buffer + buf[:n]
        self.__buffer = buf[n:]
        return rbuf



class AceBlowfish:
    """
    Decryption engine for ACE Blowfish.

    >>> bf = AceBlowfish(b'123456789')
    >>> bf.blocksize
    8
    >>> bf.decrypt(b'\\xFF'*8)
    b'\\xb7wF@5.er'
    >>> bf.decrypt(b'\\xC7'*8)
    b'eE\\x05\\xc4\\xa5\\x85)\\xbc'
    >>> bf.decrypt(b'123')
    Traceback (most recent call last):
        ...
    AssertionError
    """

    SHA1_A = 0x67452301
    SHA1_B = 0xefcdab89
    SHA1_C = 0x98badcfe
    SHA1_D = 0x10325476
    SHA1_E = 0xc3d2e1f0

    BF_P = (
        0x243F6A88, 0x85A308D3, 0x13198A2E, 0x03707344,
        0xA4093822, 0x299F31D0, 0x082
... [TRUNCATED]
```

### File: LICENSE.md
```md
# License and copyright

## Copyright

Copyright (c) 2017-2026, Daniel Roethlisberger and contributors.
All rights reserved.
Licensed under the 2-clause BSD license contained herein.


## Contributions

By contributing to the software, the contributor releases their
contribution under the license and copyright terms herein.  While
contributors retain copyright to their contributions, they grant the
main copyright holder of the software the irrevocable, transferable
right to relicense the software as a whole or in part, including their
contributions, under different open source licenses than the one
contained herein.


## License

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


## Note

The ACE archive format and ACE compression and decompression
algorithms have been designed by Marcel Lemke.  The above copyright
notice and license does not constitute a claim of intellectual property
over ACE technology beyond the copyright of this python implementation.


```

### File: NEWS.md
```md
### acefile 0.6.14 2026-01-21

-   Experimental support for free-threaded Python.
-   Fix memory leak in acebitstream module.
-   Add pytest smoke tests and configure GitHub Actions CI for testing.
-   Remove deprecated setup.py features.


### acefile 0.6.13 2024-11-09

-   Rephrase setup failure notices for clarity.
-   Improve seekable conformance of internal file-like wrappers.
-   Minor maintainability and test improvements.


### acefile 0.6.12 2019-03-10

-   Fix an IndexError exception while decompressing corrupt archives, that also
    manifested for some encrypted ACE archives when using a wrong password
    (bug reported by Jonathan Leonard).
-   Parse all variants of recovery headers for dumping and diagnostics, but
    still ignore the actual recovery data (issue #11).
-   Expose the `--debug` option in the CLI usage information and make its
    output slightly more understandable.


### acefile 0.6.11 2019-02-26

-   Add unit test for WinRAR/unacev2.dll vulnerability CVE-2018-20250 to
    ensure and verify that acefile is not vulnerable.
-   Migrate to new PGP key 0xE1520675375F5E35 for release signing.


### acefile 0.6.10 2018-07-16

-   Fix reading archives from stdin in CLI on Windows.


### acefile 0.6.9 2018-05-16

-   Substantially improve filename sanitization to avoid absolute path
    overwrites, filenames containing reserved characters or matching reserved
    names.


### acefile 0.6.8 2018-01-01

-   Fix build of c extension on platforms without C99 support enabled by
    default (pull req #12, @joesecurity).


### acefile 0.6.7 2017-08-21

-   Make restoration of mtime/atime on extraction optional, default off, and
    add `-r` `--restore` arguments to CLI.
-   Parse NT security information from FILE headers when present and optionally
    restore file attributes and NT security information on extraction as far as
    the platform supports it (issue #4).


### acefile 0.6.6 2017-08-05

-   Restore mtime and atime on extraction of files (issue #7).
-   Add `-V` `--version` arguments to CLI (issue #8).


### acefile 0.6.5 2017-08-01

-   Remove ACE 2.0 PIC mode width multiple of planes restriction (issue #6).
-   Improve exception messages and CLI exception handling.
-   Add SIGINFO handler to CLI on platforms that support it.
-   Add 270 additional ACE archives to corpus of test archives.


### acefile 0.6.4 2017-07-26

-   Fix signedness of ACE 2.0 SOUND mode diff calculations (issue #5).
-   Add basic debugging facility: `acefile.DEBUG = True` and CLI `--debug`
    hidden option.


### acefile 0.6.3 2017-07-23

-   10% performance increase for larger archives by avoiding excessive LZ77
    dictionary truncations.
-   Improve error handling of acebitstream.BitStream.
-   Improve unit test integration and coverage; `setup.py test` now supported.


### acefile 0.6.2 2017-07-19

-   Library API: Export open instead of AceArchive on import * from acefile.
-   Add high-performance BitStream implementation as optional c extension,
    resulting in over 50% speed increase for LZ77 archives.


### acefile 0.6.1 2017-07-16

-   Truncate password to 50 bytes for 1:1 compatibility with official unace.
-   40% performance increase of LZ77 decompression by reading LZ77 symbols as
    needed instead of pre-loading whole blocks.
-   Extended API documentation with high-level file format description.


### acefile 0.6.0 2017-07-15

-   Library API overhaul towards a stable API:
    -   Add AceArchive.is_locked() for testing if an archive is locked.
    -   Add constants for compression types and quality.
    -   Replace AceArchive.mtime and AceMember.mtime with .datetime in order
        to avoid confusion as ACE does not have separate modification and
        creation times.
    -   Replace AceMember.orig_filename with AceMember.raw_filename and
        change type from str to bytes.
    -   Replace AceMember.params with decoded AceMember.dicsizebits and
        AceMember.dicsize, holding the decoded dictionary size as power of
        two and as effective number of literals, respectively.
    -   Replace UnknownMethodError with UnknownCompressionMethodError.
    -   Remove the AceFile alias of the AceArchive class.
    -   Remove AceArchive.open().
    -   Remove TruncatedArchiveError; CorruptedArchiveError is used instead.
-   Ensure all open files are closed on exceptions during object creation.
-   Roughly 10% performance increase by constructing non-standard ACE CRC-32
    from python standard library zlib.crc32 instead of using a pure python
    CRC implementation.
-   Show more metadata in CLI `--verbose` archive info and `--list`.
-   Generate API documentation.


### acefile 0.5.2 2017-07-03

-   Renamed AceFile to AceArchive, but AceFile is still available as an alias.
-   Hidden AceInfo class from the API, it is still there but not in __all__.
-   Added all exceptions to the API.
-   Improved filename sanitization.


### acefile 0.5.1 2017-07-02

-   Fix regression that broke extraction when directly writing the yielded
    chunks to files.


### acefile 0.5.0 2017-07-01

-   Add multi-volume archive support.
-   All optional function arguments in the library API must now be passed in
    keyword syntax, not as positional argument, to ensure future extensibility.
-   Added documentation files into PyPI package.
-   Renamed `--yes` to `--batch` in the CLI.


### acefile 0.4.3 2017-06-27

-   Search the first 1024 sectors of files for the main archive header by
    default, in line with the reference implementations.
-   Some performance improvement for all decompression modes.


### acefile 0.4.2 2017-06-25

-   Decode all currently known NT file attributes.
-   Avoid rare IndexError when decompressing malformed archives.
-   Handle archives with multiple different passwords gracefully in CLI.
-   Print comments in ASCII box with a title to improve clarity in CLI.


### acefile 0.4.1 2017-06-24

-   Allow passwords to be specified as str or bytes, not only str.


### acefile 0.4.0 2017-06-21

-   Add support for encrypted archives using 160-bit blowfish.
-   Fix division by zero when using the CLI to list an archive containing
    directory members.


### acefile 0.3.0 2017-06-18

-   Implement decompression of archive and file comments.
-   Fix exception in decompression of ACE 1.0 archives using compression
    method 1 (LZ77).


### acefile 0.2.1 2017-06-17

First public release.



```

### File: requirements-dev.txt
```txt
pytest
sphinx

```

