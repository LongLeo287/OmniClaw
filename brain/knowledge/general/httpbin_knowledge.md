---
id: httpbin-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.854666
---

# KNOWLEDGE EXTRACT: httpbin
> **Extracted on:** 2026-03-31 01:42:04
> **Source:** httpbin

---

## File: `.dockerignore`
```
Dockerfile
.git
```

## File: `.gitignore`
```
env/
build/
dist/
.eggs/
.workon
.epio-app
*.pyc
.tox
*.egg-info
*.swp
.vscode/
```

## File: `.travis.yml`
```yaml
dist: trusty
language: python

sudo: false
matrix:
    include:
        - python: 2.7
          env: TOXENV=py27
        - python: 3.6
          env: TOXENV=py36
        - python: 3.7
          env: TOXENV=py37
          dist: xenial
          sudo: true

install:
    - travis_retry pip install tox

script:
    - tox
```

## File: `app.json`
```json
{
  "name": "httpbin",
  "description": "HTTP Request & Response Service, written in Python + Flask.",
  "repository": "https://github.com/requests/httpbin",
  "website": "https://httpbin.org",
  "logo": "https://s3.amazonaws.com/f.cl.ly/items/333Y191Z2C0G2J3m3Y0b/httpbin.svg",
  "keywords": ["http", "rest", "API", "testing", "integration", "python", "flask"],
  "addons": "sentry"
}
```

## File: `AUTHORS`
```
HttpBin is written and maintained by Kenneth Reitz and
various contributors:

Development Lead
````````````````

- Kenneth Reitz <_@kennethreitz.com>


Patches and Suggestions
```````````````````````

- Zbigniew Siciarz
- Andrey Petrov
- Lispython
- Kyle Conroy
- Flavio Percoco
- Radomir Stevanovic (http://github.com/randomir)
- Steven Honson
- Bob Carroll <bob.carroll@alum.rit.edu> @rcarz
- Cory Benfield (Lukasa) <cory@lukasa.co.uk>
- Matt Robenolt (https://github.com/mattrobenolt)
- Dave Challis (https://github.com/davechallis)
- Florian Bruhin (https://github.com/The-Compiler)
- Brett Randall (https://github.com/javabrett)
```

## File: `docker-compose.yml`
```yaml
version: '2'
services:
    httpbin:
      build: '.'
      ports:
        - '80:80'
```

## File: `Dockerfile`
```
FROM ubuntu:18.04

LABEL name="httpbin"
LABEL version="0.9.2"
LABEL description="A simple HTTP service."
LABEL org.kennethreitz.vendor="Kenneth Reitz"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update -y && apt install python3-pip git -y && pip3 install --no-cache-dir pipenv

ADD Pipfile Pipfile.lock /httpbin/
WORKDIR /httpbin
RUN /bin/bash -c "pip3 install --no-cache-dir -r <(pipenv lock -r)"

ADD . /httpbin
RUN pip3 install --no-cache-dir /httpbin

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "httpbin:app", "-k", "gevent"]
```

## File: `LICENSE`
```
ISC License

Copyright (c) 2017 Kenneth Reitz.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## File: `MANIFEST.in`
```
include httpbin/VERSION README.md LICENSE AUTHORS test_httpbin.py
recursive-include httpbin/templates *
recursive-include httpbin/static *
```

## File: `now.json`
```json
{
    "name": "httpbin",
    "regions": [
        "all"
    ],
    "alias": [
        "httpbin.org"
    ],
    "type": "docker"
}
```

## File: `Pipfile`
```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[packages]
gunicorn = "*"
decorator = "*"
brotlipy = "*"
gevent = "*"
Flask = "*"
meinheld = "*"
werkzeug = ">=0.14.1"
six = "*"
flasgger = "*"
pyyaml = {git = "https://github.com/yaml/pyyaml.git"}

[dev-packages]
rope = "*"
```

## File: `Procfile`
```
web: gunicorn httpbin:app -k gevent
```

## File: `README.md`
```markdown
# httpbin(1): HTTP Request & Response Service


A [Kenneth Reitz](http://kennethreitz.org/bitcoin) Project.

![ice cream](http://farm1.staticflickr.com/572/32514669683_4daf2ab7bc_k_d.jpg)

Run locally:
```sh
docker pull kennethreitz/httpbin
docker run -p 80:80 kennethreitz/httpbin
```

See http://httpbin.org for more information.

## Officially Deployed at:

- http://httpbin.org
- https://httpbin.org
- https://hub.docker.com/r/kennethreitz/httpbin/


## SEE ALSO

- http://requestb.in
- http://python-requests.org
- https://grpcb.in/

## Build Status

[![Build Status](https://travis-ci.org/requests/httpbin.svg?branch=master)](https://travis-ci.org/requests/httpbin)
```

## File: `runtime.txt`
```
python-3.6.5
```

## File: `setup.cfg`
```
[bdist_wheel]
universal = 1
```

## File: `setup.py`
```python
from setuptools import setup, find_packages
import os
import io


with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'httpbin', 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(
    name="httpbin",
    version=version,
    description="HTTP Request and Response Service",
    long_description="A simple HTTP Request & Response Service, written in Python + Flask.",

    # The project URL.
    url='https://github.com/requests/httpbin',

    # Author details
    author='Kenneth Reitz',
    author_email='me@kennethreitz.org',

    # Choose your license
    license='MIT',

    classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Intended Audience :: Developers',
         'Natural Language :: English',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3.6',
    ],
    test_suite="test_httpbin",
    packages=find_packages(),
    include_package_data = True, # include files listed in MANIFEST.in
    install_requires=[
        'Flask', 'MarkupSafe', 'decorator', 'itsdangerous', 'six', 'brotlipy',
        'raven[flask]', 'werkzeug>=0.14.1', 'gevent', 'flasgger'
    ],
)
```

## File: `test_httpbin.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import base64
import unittest
import contextlib
import six
import json
from werkzeug.http import parse_dict_header
from hashlib import md5, sha256, sha512
from six import BytesIO

import httpbin
from httpbin.helpers import parse_multi_value_header


@contextlib.contextmanager
def _setenv(key, value):
    """Context manager to set an environment variable temporarily."""
    old_value = os.environ.get(key, None)
    if value is None:
        os.environ.pop(key, None)
    else:
        os.environ[key] = value

    yield

    if old_value is None:
        os.environ.pop(key, None)
    else:
        os.environ[key] = value



def _string_to_base64(string):
    """Encodes string to utf-8 and then base64"""
    utf8_encoded = string.encode('utf-8')
    return base64.urlsafe_b64encode(utf8_encoded)

def _hash(data, algorithm):
    """Encode binary data according to specified algorithm, use MD5 by default"""
    if algorithm == 'SHA-256':
        return sha256(data).hexdigest()
    elif algorithm == 'SHA-512':
        return sha512(data).hexdigest()
    else:
        return md5(data).hexdigest()

def _make_digest_auth_header(username, password, method, uri, nonce,
                             realm=None, opaque=None, algorithm=None,
                             qop=None, cnonce=None, nc=None, body=None):
    """Compile a digest authentication header string.

    Arguments:
    - `nonce`: nonce string, received within "WWW-Authenticate" header
    - `realm`: realm string, received within "WWW-Authenticate" header
    - `opaque`: opaque string, received within "WWW-Authenticate" header
    - `algorithm`: type of hashing algorithm, used by the client
    - `qop`: type of quality-of-protection, used by the client
    - `cnonce`: client nonce, required if qop is "auth" or "auth-int"
    - `nc`: client nonce count, required if qop is "auth" or "auth-int"
    - `body`: body of the outgoing request (bytes), used if qop is "auth-int"
    """

    assert username
    assert password
    assert nonce
    assert method
    assert uri
    assert algorithm in ('MD5', 'SHA-256', 'SHA-512', None)

    a1 = ':'.join([username, realm or '', password])
    ha1 = _hash(a1.encode('utf-8'), algorithm)

    a2 = ':'.join([method, uri])
    if qop == 'auth-int':
        a2 = ':'.join([a2, _hash(body or b'', algorithm)])
    ha2 = _hash(a2.encode('utf-8'), algorithm)

    a3 = ':'.join([ha1, nonce])
    if qop in ('auth', 'auth-int'):
        assert cnonce
        assert nc
        a3 = ':'.join([a3, nc, cnonce, qop])

    a3 = ':'.join([a3, ha2])
    auth_response = _hash(a3.encode('utf-8'), algorithm)

    auth_header = \
        'Digest username="{0}", response="{1}", uri="{2}", nonce="{3}"'\
            .format(username, auth_response, uri, nonce)

    # 'realm' and 'opaque' should be returned unchanged, even if empty
    if realm != None:
        auth_header += ', realm="{0}"'.format(realm)
    if opaque != None:
        auth_header += ', opaque="{0}"'.format(opaque)

    if algorithm:
        auth_header += ', algorithm="{0}"'.format(algorithm)
    if cnonce:
        auth_header += ', cnonce="{0}"'.format(cnonce)
    if nc:
        auth_header += ', nc={0}'.format(nc)
    if qop:
        auth_header += ', qop={0}'.format(qop)

    return auth_header

class HttpbinTestCase(unittest.TestCase):
    """Httpbin tests"""

    def setUp(self):
        httpbin.app.debug = True
        self.app = httpbin.app.test_client()

    def test_index(self):   
        response = self.app.get('/', headers={'User-Agent': 'test'})
        self.assertEqual(response.status_code, 200)
 
    def get_data(self, response):
        if 'get_data' in dir(response):
            return response.get_data()
        else:
            return response.data

    def test_response_headers_simple(self):
        supported_verbs = ['get', 'post']
        for verb in supported_verbs:
            method = getattr(self.app, verb)
            response = method('/response-headers?animal=dog')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers.get_all('animal'), ['dog'])
            assert json.loads(response.data.decode('utf-8'))['animal'] == 'dog'

    def test_response_headers_multi(self):
        supported_verbs = ['get', 'post']
        for verb in supported_verbs:
            method = getattr(self.app, verb)
            response = method('/response-headers?animal=dog&animal=cat')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers.get_all('animal'), ['dog', 'cat'])
            assert json.loads(response.data.decode('utf-8'))['animal'] == ['dog', 'cat']

    def test_get(self):
        response = self.app.get('/get', headers={'User-Agent': 'test'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['args'], {})
        self.assertEqual(data['headers']['Host'], 'localhost')
        self.assertEqual(data['headers']['Content-Length'], '0')
        self.assertEqual(data['headers']['User-Agent'], 'test')
        # self.assertEqual(data['origin'], None)
        self.assertEqual(data['url'], 'http://localhost/get')
        self.assertTrue(response.data.endswith(b'\n'))

    def test_anything(self):
        response = self.app.get('/anything')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/anything/foo/bar')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['args'], {})
        self.assertEqual(data['headers']['Host'], 'localhost')
        self.assertEqual(data['headers']['Content-Length'], '0')
        self.assertEqual(data['url'], 'http://localhost/anything/foo/bar')
        self.assertEqual(data['method'], 'GET')
        self.assertTrue(response.data.endswith(b'\n'))

    def test_base64(self):
        greeting = u'Здравствуй, мир!'
        b64_encoded = _string_to_base64(greeting)
        response = self.app.get(b'/base64/' + b64_encoded)
        content = response.data.decode('utf-8')
        self.assertEqual(greeting, content)

    def test_post_binary(self):
        response = self.app.post('/post',
                                 data=b'\x01\x02\x03\x81\x82\x83',
                                 content_type='application/octet-stream')
        self.assertEqual(response.status_code, 200)

    def test_post_body_text(self):
        with open('httpbin/core.py') as f:
            response = self.app.post('/post', data={"file": f.read()})
        self.assertEqual(response.status_code, 200)

    def test_post_body_binary(self):
        response = self.app.post(
            '/post',
            data={"file": b'\x01\x02\x03\x81\x82\x83'})
        self.assertEqual(response.status_code, 200)

    def test_post_body_unicode(self):
        response = self.app.post('/post', data=u'оживлённым'.encode('utf-8'))
        self.assertEqual(json.loads(response.data.decode('utf-8'))['data'], u'оживлённым')

    def test_post_file_with_missing_content_type_header(self):
        # I built up the form data manually here because I couldn't find a way
        # to convince the werkzeug test client to send files without the
        # content-type of the file set.
        data = '--bound\r\nContent-Disposition: form-data; name="media"; '
        data += 'filename="test.bin"\r\n\r\n\xa5\xc6\n--bound--\r\n'
        response = self.app.post(
            '/post',
            content_type='multipart/form-data; boundary=bound',
            data=data,
        )
        self.assertEqual(response.status_code, 200)

    """
    This is currently a sort of negative-test.
    We validate that when running Flask-only server that
    Transfer-Encoding: chunked requests are unsupported and
    we return 501 Not Implemented
    """
    def test_post_chunked(self):
        data = '{"animal":"dog"}'
        response = self.app.post(
            '/post',
            content_type='application/json',
            headers=[('Transfer-Encoding', 'chunked')],
            data=data,
        )
        self.assertEqual(response.status_code, 501)
        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(json.loads(response.data.decode('utf-8'))['data'], '{"animal":"dog"}')
        #self.assertEqual(json.loads(response.data.decode('utf-8'))['json'], {"animal": "dog"})

    def test_set_cors_headers_after_request(self):
        response = self.app.get('/get')
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Origin'), '*'
        )

    def test_set_cors_credentials_headers_after_auth_request(self):
        response = self.app.get('/basic-auth/foo/bar')
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Credentials'), 'true'
        )

    def test_set_cors_headers_after_request_with_request_origin(self):
        response = self.app.get('/get', headers={'Origin': 'origin'})
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Origin'), 'origin'
        )

    def test_set_cors_headers_with_options_verb(self):
        response = self.app.open('/get', method='OPTIONS')
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Origin'), '*'
        )
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Credentials'), 'true'
        )
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Methods'),
            'GET, POST, PUT, DELETE, PATCH, OPTIONS'
        )
        self.assertEqual(
            response.headers.get('Access-Control-Max-Age'), '3600'
        )
        # FIXME should we add any extra headers?
        self.assertNotIn(
            'Access-Control-Allow-Headers', response.headers
        )
    def test_set_cors_allow_headers(self):
        response = self.app.open('/get', method='OPTIONS', headers={'Access-Control-Request-Headers': 'X-Test-Header'})
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Headers'), 'X-Test-Header'
        )

    def test_headers(self):
        headers = {
            "Accept": "*/*",
            "Host": "localhost:1234",
            "User-Agent": "curl/7.54.0",
            "Via": "bar"
        }
        response = self.app.get('/headers', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue({'Accept', 'Host', 'User-Agent'}.issubset(set(response.json['headers'].keys())))
        self.assertNotIn('Via', response.json)

    def test_headers_show_env(self):
        headers = {
            "Accept": "*/*",
            "Host": "localhost:1234",
            "User-Agent": "curl/7.54.0",
            "Via": "bar"
        }
        response = self.app.get('/headers?show_env=true', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue({'Accept', 'Host', 'User-Agent', 'Via'}.issubset(set(response.json['headers'].keys())))

    def test_user_agent(self):
        response = self.app.get(
            '/user-agent', headers={'User-Agent': 'test'}
        )
        self.assertIn('test', response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)

    def test_gzip(self):
        response = self.app.get('/gzip')
        self.assertEqual(response.status_code, 200)

    def test_brotli(self):
        response = self.app.get('/brotli')
        self.assertEqual(response.status_code, 200)

    def test_bearer_auth(self):
        token = 'abcd1234'
        response = self.app.get(
            '/bearer',
            headers={'Authorization': 'Bearer ' + token}
        )
        self.assertEqual(response.status_code, 200)
        assert json.loads(response.data.decode('utf-8'))['token'] == token

    def test_bearer_auth_with_wrong_authorization_type(self):
        """Sending an non-Bearer Authorization header to /bearer should return a 401"""
        auth_headers = (
            ('Authorization', 'Basic 1234abcd'),
            ('Authorization', ''),
            ('',  '')
        )
        for header in auth_headers:
            response = self.app.get(
                '/bearer',
                headers={header[0]: header[1]}
            )
            self.assertEqual(response.status_code, 401)

    def test_bearer_auth_with_missing_token(self):
        """Sending an 'Authorization: Bearer' header with no token to /bearer should return a 401"""
        response = self.app.get(
            '/bearer',
            headers={'Authorization': 'Bearer'}
        )
        self.assertEqual(response.status_code, 401)

    def test_digest_auth_with_wrong_password(self):
        auth_header = 'Digest username="user",realm="wrong",nonce="wrong",uri="/digest-auth/user/passwd/MD5",response="wrong",opaque="wrong"'
        response = self.app.get(
            '/digest-auth/auth/user/passwd/MD5',
            environ_base={
                # httpbin's digest auth implementation uses the remote addr to
                # build the nonce
                'REMOTE_ADDR': '127.0.0.1',
            },
            headers={
                'Authorization': auth_header,
            }
        )
        self.assertTrue('Digest' in response.headers.get('WWW-Authenticate'))
        self.assertEqual(response.status_code, 401)

    def test_digest_auth(self):
        """Test different combinations of digest auth parameters"""
        username = 'user'
        password = 'passwd'
        for qop in None, 'auth', 'auth-int',:
            for algorithm in None, 'MD5', 'SHA-256', 'SHA-512':
                for body in None, b'', b'request payload':
                    for stale_after in (None, 1, 4) if algorithm else (None,) :
                        self._test_digest_auth(username, password, qop, algorithm, body, stale_after)

    def test_digest_auth_with_wrong_authorization_type(self):
        """Sending an non-digest Authorization header to /digest-auth should return a 401"""
        auth_headers = (
            ('Authorization', 'Basic 1234abcd'),
            ('Authorization', ''),
            ('',  '')
        )
        for header in auth_headers:
            response = self.app.get(
                '/digest-auth/auth/myname/mysecret',
                headers={header[0]: header[1]}
            )
            self.assertEqual(response.status_code, 401)

    def _test_digest_auth(self, username, password, qop, algorithm=None, body=None, stale_after=None):
        uri = self._digest_auth_create_uri(username, password, qop, algorithm, stale_after)

        unauthorized_response = self._test_digest_auth_first_challenge(uri)

        header = unauthorized_response.headers.get('WWW-Authenticate')

        authorized_response, nonce = self._test_digest_response_for_auth_request(header, username, password, qop, uri, body)
        self.assertEqual(authorized_response.status_code, 200)

        if None == stale_after :
            return

        # test stale after scenerio
        self._digest_auth_stale_after_check(header, username, password, uri, body, qop, stale_after)

    def _test_digest_auth_first_challenge(self, uri):
        unauthorized_response = self.app.get(
            uri,
            environ_base={
                # digest auth uses the remote addr to build the nonce
                'REMOTE_ADDR': '127.0.0.1',
            }
        )
        # make sure it returns a 401
        self.assertEqual(unauthorized_response.status_code, 401)
        return unauthorized_response

    def _digest_auth_create_uri(self, username, password, qop, algorithm, stale_after):
        uri = '/digest-auth/{0}/{1}/{2}'.format(qop or 'wrong-qop', username, password)
        if algorithm:
            uri += '/' + algorithm
        if stale_after:
            uri += '/{0}'.format(stale_after)
        return uri

    def _digest_auth_stale_after_check(self, header, username, password, uri, body, qop, stale_after):
        for nc in range(2, stale_after + 1):
            authorized_response, nonce = self._test_digest_response_for_auth_request(header, username, password, qop, uri, \
                                                                              body, nc)
            self.assertEqual(authorized_response.status_code, 200)
        stale_response, nonce = self._test_digest_response_for_auth_request(header, username, password, qop, uri, \
                                                                     body, stale_after + 1)
        self.assertEqual(stale_response.status_code, 401)
        header = stale_response.headers.get('WWW-Authenticate')
        self.assertIn('stale=TRUE', header)

    def _test_digest_response_for_auth_request(self, header, username, password, qop, uri, body, nc=1, nonce=None):
        auth_type, auth_info = header.split(None, 1)
        self.assertEqual(auth_type, 'Digest')

        d = parse_dict_header(auth_info)

        nonce = nonce or d['nonce']
        realm = d['realm']
        opaque = d['opaque']
        if qop :
            self.assertIn(qop, [x.strip() for x in d['qop'].split(',')], 'Challenge should contains expected qop')
        algorithm = d['algorithm']

        cnonce, nc = (_hash(os.urandom(10), "MD5"), '{:08}'.format(nc)) if qop in ('auth', 'auth-int') else (None, None)

        auth_header = _make_digest_auth_header(
            username, password, 'GET', uri, nonce, realm, opaque, algorithm, qop, cnonce, nc, body)

        # make second request
        return self.app.get(
            uri,
            environ_base={
                # httpbin's digest auth implementation uses the remote addr to
                # build the nonce
                'REMOTE_ADDR': '127.0.0.1',
            },
            headers={
                'Authorization': auth_header,
            },
            data=body
        ), nonce

    def test_digest_auth_wrong_pass(self):
        """Test different combinations of digest auth parameters"""
        username = 'user'
        password = 'passwd'
        for qop in None, 'auth', 'auth-int',:
            for algorithm in None, 'MD5', 'SHA-256', 'SHA-512':
                for body in None, b'', b'request payload':
                    self._test_digest_auth_wrong_pass(username, password, qop, algorithm, body, 3)

    def _test_digest_auth_wrong_pass(self, username, password, qop, algorithm=None, body=None, stale_after=None):
        uri = self._digest_auth_create_uri(username, password, qop, algorithm, stale_after)
        unauthorized_response = self._test_digest_auth_first_challenge(uri)

        header = unauthorized_response.headers.get('WWW-Authenticate')

        wrong_pass_response, nonce = self._test_digest_response_for_auth_request(header, username, "wrongPassword", qop, uri, body)
        self.assertEqual(wrong_pass_response.status_code, 401)
        header = wrong_pass_response.headers.get('WWW-Authenticate')
        self.assertNotIn('stale=TRUE', header)

        reused_nonce_response, nonce =  self._test_digest_response_for_auth_request(header, username, password, qop, uri, \
                                                                              body, nonce=nonce)
        self.assertEqual(reused_nonce_response.status_code, 401)
        header = reused_nonce_response.headers.get('WWW-Authenticate')
        self.assertIn('stale=TRUE', header)

    def test_drip(self):
        response = self.app.get('/drip?numbytes=400&duration=2&delay=1')
        self.assertEqual(response.content_length, 400)
        self.assertEqual(len(self.get_data(response)), 400)
        self.assertEqual(response.status_code, 200)

    def test_drip_with_invalid_numbytes(self):
        for bad_num in -1, 0:
            uri = '/drip?numbytes={0}&duration=2&delay=1'.format(bad_num)
            response = self.app.get(uri)
            self.assertEqual(response.status_code, 400)

    def test_drip_with_custom_code(self):
        response = self.app.get('/drip?numbytes=400&duration=2&code=500')
        self.assertEqual(response.content_length, 400)
        self.assertEqual(len(self.get_data(response)), 400)
        self.assertEqual(response.status_code, 500)

    def test_get_bytes(self):
        response = self.app.get('/bytes/1024')
        self.assertEqual(len(self.get_data(response)), 1024)
        self.assertEqual(response.status_code, 200)

    def test_bytes_with_seed(self):
        response = self.app.get('/bytes/10?seed=0')
        # The RNG changed in python3, so even though we are
        # setting the seed, we can't expect the value to be the
        # same across both interpreters.
        if six.PY3:
            self.assertEqual(
                response.data, b'\xc5\xd7\x14\x84\xf8\xcf\x9b\xf4\xb7o'
            )
        else:
            self.assertEqual(
                response.data, b'\xd8\xc2kB\x82g\xc8Mz\x95'
            )

    def test_stream_bytes(self):
        response = self.app.get('/stream-bytes/1024')
        self.assertEqual(len(self.get_data(response)), 1024)
        self.assertEqual(response.status_code, 200)

    def test_stream_bytes_with_seed(self):
        response = self.app.get('/stream-bytes/10?seed=0')
        # The RNG changed in python3, so even though we are
        # setting the seed, we can't expect the value to be the
        # same across both interpreters.
        if six.PY3:
            self.assertEqual(
                response.data, b'\xc5\xd7\x14\x84\xf8\xcf\x9b\xf4\xb7o'
            )
        else:
            self.assertEqual(
                response.data, b'\xd8\xc2kB\x82g\xc8Mz\x95'
            )

    def test_delete_endpoint_returns_body(self):
        response = self.app.delete(
            '/delete',
            data={'name': 'kevin'},
            content_type='application/x-www-form-urlencoded'
        )
        form_data = json.loads(response.data.decode('utf-8'))['form']
        self.assertEqual(form_data, {'name': 'kevin'})

    def test_methods__to_status_endpoint(self):
        methods = [
            'GET',
            'HEAD',
            'POST',
            'PUT',
            'DELETE',
            'PATCH',
            'TRACE',
        ]
        for m in methods:
            response = self.app.open(path='/status/418', method=m)
            self.assertEqual(response.status_code, 418)

    def test_status_endpoint_invalid_code(self):
        response = self.app.get(path='/status/4!9')
        self.assertEqual(response.status_code, 400)

    def test_status_endpoint_invalid_codes(self):
        response = self.app.get(path='/status/200,402,foo')
        self.assertEqual(response.status_code, 400)

    def test_xml_endpoint(self):
        response = self.app.get(path='/xml')
        self.assertEqual(
            response.headers.get('Content-Type'), 'application/xml'
        )

    def test_x_forwarded_proto(self):
        response = self.app.get(path='/get', headers={
            'X-Forwarded-Proto':'https'
        })
        assert json.loads(response.data.decode('utf-8'))['url'].startswith('https://')

    def test_redirect_n_higher_than_1(self):
        response = self.app.get('/redirect/5')
        self.assertEqual(
            response.headers.get('Location'), '/relative-redirect/4'
        )

    def test_redirect_to_post(self):
        response = self.app.post('/redirect-to?url=/post&status_code=307',
                                 data=b'\x01\x02\x03\x81\x82\x83',
                                 content_type='application/octet-stream')
        self.assertEqual(response.status_code, 307)
        self.assertEqual(
            response.headers.get('Location'), '/post'
        )

    def test_redirect_absolute_param_n_higher_than_1(self):
        response = self.app.get('/redirect/5?absolute=true')
        self.assertEqual(
            response.headers.get('Location'), 'http://localhost/absolute-redirect/4'
        )

    def test_redirect_n_equals_to_1(self):
        response = self.app.get('/redirect/1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.headers.get('Location'), '/get'
        )

    def test_relative_redirect_n_equals_to_1(self):
        response = self.app.get('/relative-redirect/1')
        self.assertEqual(
            response.headers.get('Location'), '/get'
        )

    def test_relative_redirect_n_higher_than_1(self):
        response = self.app.get('/relative-redirect/7')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.headers.get('Location'), '/relative-redirect/6'
        )

    def test_absolute_redirect_n_higher_than_1(self):
        response = self.app.get('/absolute-redirect/5')
        self.assertEqual(
            response.headers.get('Location'), 'http://localhost/absolute-redirect/4'
        )

    def test_absolute_redirect_n_equals_to_1(self):
        response = self.app.get('/absolute-redirect/1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.headers.get('Location'), 'http://localhost/get'
        )

    def test_request_range(self):
        response1 = self.app.get('/range/1234')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.headers.get('ETag'), 'range1234')
        self.assertEqual(response1.headers.get('Content-range'), 'bytes 0-1233/1234')
        self.assertEqual(response1.headers.get('Accept-ranges'), 'bytes')
        self.assertEqual(len(self.get_data(response1)), 1234)

        response2 = self.app.get('/range/1234')
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.headers.get('ETag'), 'range1234')
        self.assertEqual(self.get_data(response1), self.get_data(response2))

    def test_request_range_with_parameters(self):
        response = self.app.get(
            '/range/100?duration=1.5&chunk_size=5',
            headers={ 'Range': 'bytes=10-24' }
        )

        self.assertEqual(response.status_code, 206)
        self.assertEqual(response.headers.get('ETag'), 'range100')
        self.assertEqual(response.headers.get('Content-range'), 'bytes 10-24/100')
        self.assertEqual(response.headers.get('Accept-ranges'), 'bytes')
        self.assertEqual(response.headers.get('Content-Length'), '15')
        self.assertEqual(self.get_data(response), 'klmnopqrstuvwxy'.encode('utf8'))

    def test_request_range_first_15_bytes(self):
        response = self.app.get(
            '/range/1000',
            headers={ 'Range': 'bytes=0-15' }
        )

        self.assertEqual(response.status_code, 206)
        self.assertEqual(response.headers.get('ETag'), 'range1000')
        self.assertEqual(self.get_data(response), 'abcdefghijklmnop'.encode('utf8'))
        self.assertEqual(response.headers.get('Content-range'), 'bytes 0-15/1000')

    def test_request_range_open_ended_last_6_bytes(self):
        response = self.app.get(
            '/range/26',
            headers={ 'Range': 'bytes=20-' }
        )

        self.assertEqual(response.status_code, 206)
        self.assertEqual(response.headers.get('ETag'), 'range26')
        self.assertEqual(self.get_data(response), 'uvwxyz'.encode('utf8'))
        self.assertEqual(response.headers.get('Content-range'), 'bytes 20-25/26')
        self.assertEqual(response.headers.get('Content-Length'), '6')

    def test_request_range_suffix(self):
        response = self.app.get(
            '/range/26',
            headers={ 'Range': 'bytes=-5' }
        )

        self.assertEqual(response.status_code, 206)
        self.assertEqual(response.headers.get('ETag'), 'range26')
        self.assertEqual(self.get_data(response), 'vwxyz'.encode('utf8'))
        self.assertEqual(response.headers.get('Content-range'), 'bytes 21-25/26')
        self.assertEqual(response.headers.get('Content-Length'), '5')

    def test_request_out_of_bounds(self):
        response = self.app.get(
            '/range/26',
            headers={ 'Range': 'bytes=10-5',
            }
        )

        self.assertEqual(response.status_code, 416)
        self.assertEqual(response.headers.get('ETag'), 'range26')
        self.assertEqual(len(self.get_data(response)), 0)
        self.assertEqual(response.headers.get('Content-range'), 'bytes */26')
        self.assertEqual(response.headers.get('Content-Length'), '0')

        response = self.app.get(
            '/range/26',
            headers={ 'Range': 'bytes=32-40',
            }
        )

        self.assertEqual(response.status_code, 416)
        response = self.app.get(
            '/range/26',
            headers={ 'Range': 'bytes=0-40',
            }
        )
        self.assertEqual(response.status_code, 416)

    def test_etag_if_none_match_matches(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-None-Match': 'abc' }
        )
        self.assertEqual(response.status_code, 304)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_etag_if_none_match_matches_list(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-None-Match': '"123", "abc"' }
        )
        self.assertEqual(response.status_code, 304)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_etag_if_none_match_matches_star(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-None-Match': '*' }
        )
        self.assertEqual(response.status_code, 304)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_etag_if_none_match_w_prefix(self):
        response = self.app.get(
            '/etag/c3piozzzz',
            headers={ 'If-None-Match': 'W/"xyzzy", W/"r2d2xxxx", W/"c3piozzzz"' }
        )
        self.assertEqual(response.status_code, 304)
        self.assertEqual(response.headers.get('ETag'), 'c3piozzzz')

    def test_etag_if_none_match_has_no_match(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-None-Match': '123' }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_etag_if_match_matches(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-Match': 'abc' }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_etag_if_match_matches_list(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-Match': '"123", "abc"' }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_etag_if_match_matches_star(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-Match': '*' }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_etag_if_match_has_no_match(self):
        response = self.app.get(
            '/etag/abc',
            headers={ 'If-Match': '123' }
        )
        self.assertEqual(response.status_code, 412)
        self.assertNotIn('ETag', response.headers)

    def test_etag_with_no_headers(self):
        response = self.app.get(
            '/etag/abc'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get('ETag'), 'abc')

    def test_parse_multi_value_header(self):
        self.assertEqual(parse_multi_value_header('xyzzy'), [ "xyzzy" ])
        self.assertEqual(parse_multi_value_header('"xyzzy"'), [ "xyzzy" ])
        self.assertEqual(parse_multi_value_header('W/"xyzzy"'), [ "xyzzy" ])
        self.assertEqual(parse_multi_value_header('"xyzzy", "r2d2xxxx", "c3piozzzz"'), [ "xyzzy", "r2d2xxxx", "c3piozzzz" ])
        self.assertEqual(parse_multi_value_header('W/"xyzzy", W/"r2d2xxxx", W/"c3piozzzz"'), [ "xyzzy", "r2d2xxxx", "c3piozzzz" ])
        self.assertEqual(parse_multi_value_header('*'), [ "*" ])

if __name__ == '__main__':
    unittest.main()
```

## File: `tox.ini`
```
[tox]
envlist = py27,py36,py37

[testenv]
commands=python test_httpbin.py

[testenv:release]
skipdist = true
usedevelop = false
deps =
    twine>=1.6.0
    wheel
commands =
    python setup.py sdist bdist_wheel
    twine upload --skip-existing dist/*
```

## File: `httpbin/core.py`
```python
# -*- coding: utf-8 -*-

"""
httpbin.core
~~~~~~~~~~~~

This module provides the core HttpBin experience.
"""

import base64
import json
import os
import random
import time
import uuid
import argparse

from flask import (
    Flask,
    Response,
    request,
    render_template,
    redirect,
    jsonify as flask_jsonify,
    make_response,
    url_for,
    abort,
)
from six.moves import range as xrange
from werkzeug.datastructures import WWWAuthenticate, MultiDict
from werkzeug.http import http_date
from werkzeug.wrappers import BaseResponse
from werkzeug.http import parse_authorization_header
from flasgger import Swagger, NO_SANITIZER

from . import filters
from .helpers import (
    get_headers,
    status_code,
    get_dict,
    get_request_range,
    check_basic_auth,
    check_digest_auth,
    secure_cookie,
    H,
    ROBOT_TXT,
    ANGRY_ASCII,
    parse_multi_value_header,
    next_stale_after_value,
    digest_challenge_response,
)
from .utils import weighted_choice
from .structures import CaseInsensitiveDict

with open(
    os.path.join(os.path.realpath(os.path.dirname(__file__)), "VERSION")
) as version_file:
    version = version_file.read().strip()

ENV_COOKIES = (
    "_gauges_unique",
    "_gauges_unique_year",
    "_gauges_unique_month",
    "_gauges_unique_day",
    "_gauges_unique_hour",
    "__utmz",
    "__utma",
    "__utmb",
)


def jsonify(*args, **kwargs):
    response = flask_jsonify(*args, **kwargs)
    if not response.data.endswith(b"\n"):
        response.data += b"\n"
    return response


# Prevent WSGI from correcting the casing of the Location header
BaseResponse.autocorrect_location_header = False

# Find the correct template folder when running from a different location
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

app = Flask(__name__, template_folder=tmpl_dir)
app.debug = bool(os.environ.get("DEBUG"))
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

app.add_template_global("HTTPBIN_TRACKING" in os.environ, name="tracking_enabled")

app.config["SWAGGER"] = {"title": "httpbin.org", "uiversion": 3}

template = {
    "swagger": "2.0",
    "info": {
        "title": "httpbin.org",
        "description": (
            "A simple HTTP Request & Response Service."
            "<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>"
        ),
        "contact": {
            "responsibleOrganization": "Kenneth Reitz",
            "responsibleDeveloper": "Kenneth Reitz",
            "email": "me@kennethreitz.org",
            "url": "https://kennethreitz.org",
        },
        # "termsOfService": "http://me.com/terms",
        "version": version,
    },
    "host": "httpbin.org",  # overrides localhost:5000
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["https"],
    "protocol": "https",
    "tags": [
        {
            "name": "HTTP Methods",
            "description": "Testing different HTTP verbs",
            # 'externalDocs': {'description': 'Learn more', 'url': 'https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html'}
        },
        {"name": "Auth", "description": "Auth methods"},
        {
            "name": "Status codes",
            "description": "Generates responses with given status code",
        },
        {"name": "Request inspection", "description": "Inspect the request data"},
        {
            "name": "Response inspection",
            "description": "Inspect the response data like caching and headers",
        },
        {
            "name": "Response formats",
            "description": "Returns responses in different data formats",
        },
        {"name": "Dynamic data", "description": "Generates random and dynamic data"},
        {"name": "Cookies", "description": "Creates, reads and deletes Cookies"},
        {"name": "Images", "description": "Returns different image formats"},
        {"name": "Redirects", "description": "Returns different redirect responses"},
        {
            "name": "Anything",
            "description": "Returns anything that is passed to request",
        },
    ],
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "spec",
            "route": "/spec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/",
}

swagger = Swagger(app, sanitizer=NO_SANITIZER, template=template, config=swagger_config)

# Set up Bugsnag exception tracking, if desired. To use Bugsnag, install the
# Bugsnag Python client with the command "pip install bugsnag", and set the
# environment variable BUGSNAG_API_KEY. You can also optionally set
# BUGSNAG_RELEASE_STAGE.
if os.environ.get("BUGSNAG_API_KEY") is not None:
    try:
        import bugsnag
        import bugsnag.flask

        release_stage = os.environ.get("BUGSNAG_RELEASE_STAGE") or "production"
        bugsnag.configure(
            api_key=os.environ.get("BUGSNAG_API_KEY"),
            project_root=os.path.dirname(os.path.abspath(__file__)),
            use_ssl=True,
            release_stage=release_stage,
            ignore_classes=["werkzeug.exceptions.NotFound"],
        )
        bugsnag.flask.handle_exceptions(app)
    except:
        app.logger.warning("Unable to initialize Bugsnag exception handling.")

# -----------
# Middlewares
# -----------
"""
https://github.com/kennethreitz/httpbin/issues/340
Adds a middleware to provide chunked request encoding support running under
gunicorn only.
Werkzeug required environ 'wsgi.input_terminated' to be set otherwise it
empties the input request stream.
- gunicorn seems to support input_terminated but does not add the environ,
  so we add it here.
- flask will hang and does not seem to properly terminate the request, so
  we explicitly deny chunked requests.
"""


@app.before_request
def before_request():
    if request.environ.get("HTTP_TRANSFER_ENCODING", "").lower() == "chunked":
        server = request.environ.get("SERVER_SOFTWARE", "")
        if server.lower().startswith("gunicorn/"):
            if "wsgi.input_terminated" in request.environ:
                app.logger.debug(
                    "environ wsgi.input_terminated already set, keeping: %s"
                    % request.environ["wsgi.input_terminated"]
                )
            else:
                request.environ["wsgi.input_terminated"] = 1
        else:
            abort(501, "Chunked requests are not supported for server %s" % server)


@app.after_request
def set_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "*")
    response.headers["Access-Control-Allow-Credentials"] = "true"

    if request.method == "OPTIONS":
        # Both of these headers are only used for the "preflight request"
        # http://www.w3.org/TR/cors/#access-control-allow-methods-response-header
        response.headers[
            "Access-Control-Allow-Methods"
        ] = "GET, POST, PUT, DELETE, PATCH, OPTIONS"
        response.headers["Access-Control-Max-Age"] = "3600"  # 1 hour cache
        if request.headers.get("Access-Control-Request-Headers") is not None:
            response.headers["Access-Control-Allow-Headers"] = request.headers[
                "Access-Control-Request-Headers"
            ]
    return response


# ------
# Routes
# ------


@app.route("/legacy")
def view_landing_page():
    """Generates Landing Page in legacy layout."""
    return render_template("index.html")


@app.route("/html")
def view_html_page():
    """Returns a simple HTML document.
    ---
    tags:
      - Response formats
    produces:
      - text/html
    responses:
      200:
        description: An HTML page.
    """

    return render_template("moby.html")


@app.route("/robots.txt")
def view_robots_page():
    """Returns some robots.txt rules.
    ---
    tags:
      - Response formats
    produces:
      - text/plain
    responses:
      200:
        description: Robots file
    """

    response = make_response()
    response.data = ROBOT_TXT
    response.content_type = "text/plain"
    return response


@app.route("/deny")
def view_deny_page():
    """Returns page denied by robots.txt rules.
    ---
    tags:
      - Response formats
    produces:
      - text/plain
    responses:
      200:
        description: Denied message
    """
    response = make_response()
    response.data = ANGRY_ASCII
    response.content_type = "text/plain"
    return response
    # return "YOU SHOULDN'T BE HERE"


@app.route("/ip")
def view_origin():
    """Returns the requester's IP Address.
    ---
    tags:
      - Request inspection
    produces:
      - application/json
    responses:
      200:
        description: The Requester's IP Address.
    """

    return jsonify(origin=request.headers.get("X-Forwarded-For", request.remote_addr))


@app.route("/uuid")
def view_uuid():
    """Return a UUID4.
    ---
    tags:
      - Dynamic data
    produces:
      - application/json
    responses:
      200:
        description: A UUID4.
    """

    return jsonify(uuid=str(uuid.uuid4()))


@app.route("/headers")
def view_headers():
    """Return the incoming request's HTTP headers.
    ---
    tags:
      - Request inspection
    produces:
      - application/json
    responses:
      200:
        description: The request's headers.
    """

    return jsonify(get_dict('headers'))


@app.route("/user-agent")
def view_user_agent():
    """Return the incoming requests's User-Agent header.
    ---
    tags:
      - Request inspection
    produces:
      - application/json
    responses:
      200:
        description: The request's User-Agent header.
    """

    headers = get_headers()

    return jsonify({"user-agent": headers["user-agent"]})


@app.route("/get", methods=("GET",))
def view_get():
    """The request's query parameters.
    ---
    tags:
      - HTTP Methods
    produces:
      - application/json
    responses:
      200:
        description: The request's query parameters.
    """

    return jsonify(get_dict("url", "args", "headers", "origin"))


@app.route("/anything", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE"])
@app.route(
    "/anything/<path:anything>",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE"],
)
def view_anything(anything=None):
    """Returns anything passed in request data.
    ---
    tags:
      - Anything
    produces:
      - application/json
    responses:
      200:
        description: Anything passed in request
    """

    return jsonify(
        get_dict(
            "url",
            "args",
            "headers",
            "origin",
            "method",
            "form",
            "data",
            "files",
            "json",
        )
    )


@app.route("/post", methods=("POST",))
def view_post():
    """The request's POST parameters.
    ---
    tags:
      - HTTP Methods
    produces:
      - application/json
    responses:
      200:
        description: The request's POST parameters.
    """

    return jsonify(
        get_dict("url", "args", "form", "data", "origin", "headers", "files", "json")
    )


@app.route("/put", methods=("PUT",))
def view_put():
    """The request's PUT parameters.
    ---
    tags:
      - HTTP Methods
    produces:
      - application/json
    responses:
      200:
        description: The request's PUT parameters.
    """

    return jsonify(
        get_dict("url", "args", "form", "data", "origin", "headers", "files", "json")
    )


@app.route("/patch", methods=("PATCH",))
def view_patch():
    """The request's PATCH parameters.
    ---
    tags:
      - HTTP Methods
    produces:
      - application/json
    responses:
      200:
        description: The request's PATCH parameters.
    """

    return jsonify(
        get_dict("url", "args", "form", "data", "origin", "headers", "files", "json")
    )


@app.route("/delete", methods=("DELETE",))
def view_delete():
    """The request's DELETE parameters.
    ---
    tags:
      - HTTP Methods
    produces:
      - application/json
    responses:
      200:
        description: The request's DELETE parameters.
    """

    return jsonify(
        get_dict("url", "args", "form", "data", "origin", "headers", "files", "json")
    )


@app.route("/gzip")
@filters.gzip
def view_gzip_encoded_content():
    """Returns GZip-encoded data.
    ---
    tags:
      - Response formats
    produces:
      - application/json
    responses:
      200:
        description: GZip-encoded data.
    """

    return jsonify(get_dict("origin", "headers", method=request.method, gzipped=True))


@app.route("/deflate")
@filters.deflate
def view_deflate_encoded_content():
    """Returns Deflate-encoded data.
    ---
    tags:
      - Response formats
    produces:
      - application/json
    responses:
      200:
        description: Defalte-encoded data.
    """

    return jsonify(get_dict("origin", "headers", method=request.method, deflated=True))


@app.route("/brotli")
@filters.brotli
def view_brotli_encoded_content():
    """Returns Brotli-encoded data.
    ---
    tags:
      - Response formats
    produces:
      - application/json
    responses:
      200:
        description: Brotli-encoded data.
    """

    return jsonify(get_dict("origin", "headers", method=request.method, brotli=True))


@app.route("/redirect/<int:n>")
def redirect_n_times(n):
    """302 Redirects n times.
    ---
    tags:
      - Redirects
    parameters:
      - in: path
        name: n
        type: int
    produces:
      - text/html
    responses:
      302:
        description: A redirection.
    """
    assert n > 0

    absolute = request.args.get("absolute", "false").lower() == "true"

    if n == 1:
        return redirect(url_for("view_get", _external=absolute))

    if absolute:
        return _redirect("absolute", n, True)
    else:
        return _redirect("relative", n, False)


def _redirect(kind, n, external):
    return redirect(
        url_for("{0}_redirect_n_times".format(kind), n=n - 1, _external=external)
    )


@app.route("/redirect-to", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE"])
def redirect_to():
    """302/3XX Redirects to the given URL.
    ---
    tags:
      - Redirects
    produces:
      - text/html
    get:
      parameters:
        - in: query
          name: url
          type: string
          required: true
        - in: query
          name: status_code
          type: int
    post:
      consumes:
        - application/x-www-form-urlencoded
      parameters:
        - in: formData
          name: url
          type: string
          required: true
        - in: formData
          name: status_code
          type: int
          required: false
    patch:
      consumes:
        - application/x-www-form-urlencoded
      parameters:
        - in: formData
          name: url
          type: string
          required: true
        - in: formData
          name: status_code
          type: int
          required: false
    put:
      consumes:
        - application/x-www-form-urlencoded
      parameters:
        - in: formData
          name: url
          type: string
          required: true
        - in: formData
          name: status_code
          type: int
          required: false
    responses:
      302:
        description: A redirection.
    """

    args_dict = request.args.items()
    args = CaseInsensitiveDict(args_dict)

    # We need to build the response manually and convert to UTF-8 to prevent
    # werkzeug from "fixing" the URL. This endpoint should set the Location
    # header to the exact string supplied.
    response = app.make_response("")
    response.status_code = 302
    if "status_code" in args:
        status_code = int(args["status_code"])
        if status_code >= 300 and status_code < 400:
            response.status_code = status_code
    response.headers["Location"] = args["url"].encode("utf-8")

    return response


@app.route("/relative-redirect/<int:n>")
def relative_redirect_n_times(n):
    """Relatively 302 Redirects n times.
    ---
    tags:
      - Redirects
    parameters:
      - in: path
        name: n
        type: int
    produces:
      - text/html
    responses:
      302:
        description: A redirection.
    """

    assert n > 0

    response = app.make_response("")
    response.status_code = 302

    if n == 1:
        response.headers["Location"] = url_for("view_get")
        return response

    response.headers["Location"] = url_for("relative_redirect_n_times", n=n - 1)
    return response


@app.route("/absolute-redirect/<int:n>")
def absolute_redirect_n_times(n):
    """Absolutely 302 Redirects n times.
    ---
    tags:
      - Redirects
    parameters:
      - in: path
        name: n
        type: int
    produces:
      - text/html
    responses:
      302:
        description: A redirection.
    """

    assert n > 0

    if n == 1:
        return redirect(url_for("view_get", _external=True))

    return _redirect("absolute", n, True)


@app.route("/stream/<int:n>")
def stream_n_messages(n):
    """Stream n JSON responses
    ---
    tags:
      - Dynamic data
    parameters:
      - in: path
        name: n
        type: int
    produces:
      - application/json
    responses:
      200:
        description: Streamed JSON responses.
    """
    response = get_dict("url", "args", "headers", "origin")
    n = min(n, 100)

    def generate_stream():
        for i in range(n):
            response["id"] = i
            yield json.dumps(response) + "\n"

    return Response(generate_stream(), headers={"Content-Type": "application/json"})


@app.route(
    "/status/<codes>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE"]
)
def view_status_code(codes):
    """Return status code or random status code if more than one are given
    ---
    tags:
      - Status codes
    parameters:
      - in: path
        name: codes
    produces:
      - text/plain
    responses:
      100:
        description: Informational responses
      200:
        description: Success
      300:
        description: Redirection
      400:
        description: Client Errors
      500:
        description: Server Errors
    """

    if "," not in codes:
        try:
            code = int(codes)
        except ValueError:
            return Response("Invalid status code", status=400)
        return status_code(code)

    choices = []
    for choice in codes.split(","):
        if ":" not in choice:
            code = choice
            weight = 1
        else:
            code, weight = choice.split(":")

        try:
            choices.append((int(code), float(weight)))
        except ValueError:
            return Response("Invalid status code", status=400)

    code = weighted_choice(choices)

    return status_code(code)


@app.route("/response-headers", methods=["GET", "POST"])
def response_headers():
    """Returns a set of response headers from the query string.
    ---
    tags:
      - Response inspection
    parameters:
      - in: query
        name: freeform
        explode: true
        allowEmptyValue: true
        schema:
          type: object
          additionalProperties:
            type: string
        style: form
    produces:
      - application/json
    responses:
      200:
        description: Response headers
    """
    # Pending swaggerUI update
    # https://github.com/swagger-api/swagger-ui/issues/3850
    headers = MultiDict(request.args.items(multi=True))
    response = jsonify(list(headers.lists()))

    while True:
        original_data = response.data
        d = {}
        for key in response.headers.keys():
            value = response.headers.get_all(key)
            if len(value) == 1:
                value = value[0]
            d[key] = value
        response = jsonify(d)
        for key, value in headers.items(multi=True):
            response.headers.add(key, value)
        response_has_changed = response.data != original_data
        if not response_has_changed:
            break
    return response


@app.route("/cookies")
def view_cookies(hide_env=True):
    """Returns cookie data.
    ---
    tags:
      - Cookies
    produces:
      - application/json
    responses:
      200:
        description: Set cookies.
    """

    cookies = dict(request.cookies.items())

    if hide_env and ("show_env" not in request.args):
        for key in ENV_COOKIES:
            try:
                del cookies[key]
            except KeyError:
                pass

    return jsonify(cookies=cookies)


@app.route("/forms/post")
def view_forms_post():
    """Simple HTML form."""

    return render_template("forms-post.html")


@app.route("/cookies/set/<name>/<value>")
def set_cookie(name, value):
    """Sets a cookie and redirects to cookie list.
    ---
    tags:
      - Cookies
    parameters:
      - in: path
        name: name
        type: string
      - in: path
        name: value
        type: string
    produces:
      - text/plain
    responses:
      200:
        description: Set cookies and redirects to cookie list.
    """

    r = app.make_response(redirect(url_for("view_cookies")))
    r.set_cookie(key=name, value=value, secure=secure_cookie())

    return r


@app.route("/cookies/set")
def set_cookies():
    """Sets cookie(s) as provided by the query string and redirects to cookie list.
    ---
    tags:
      - Cookies
    parameters:
      - in: query
        name: freeform
        explode: true
        allowEmptyValue: true
        schema:
          type: object
          additionalProperties:
            type: string
        style: form
    produces:
      - text/plain
    responses:
      200:
        description: Redirect to cookie list
    """

    cookies = dict(request.args.items())
    r = app.make_response(redirect(url_for("view_cookies")))
    for key, value in cookies.items():
        r.set_cookie(key=key, value=value, secure=secure_cookie())

    return r


@app.route("/cookies/delete")
def delete_cookies():
    """Deletes cookie(s) as provided by the query string and redirects to cookie list.
    ---
    tags:
      - Cookies
    parameters:
      - in: query
        name: freeform
        explode: true
        allowEmptyValue: true
        schema:
          type: object
          additionalProperties:
            type: string
        style: form
    produces:
      - text/plain
    responses:
      200:
        description: Redirect to cookie list
    """

    cookies = dict(request.args.items())
    r = app.make_response(redirect(url_for("view_cookies")))
    for key, value in cookies.items():
        r.delete_cookie(key=key)

    return r


@app.route("/basic-auth/<user>/<passwd>")
def basic_auth(user="user", passwd="passwd"):
    """Prompts the user for authorization using HTTP Basic Auth.
    ---
    tags:
      - Auth
    parameters:
      - in: path
        name: user
        type: string
      - in: path
        name: passwd
        type: string
    produces:
      - application/json
    responses:
      200:
        description: Sucessful authentication.
      401:
        description: Unsuccessful authentication.
    """

    if not check_basic_auth(user, passwd):
        return status_code(401)

    return jsonify(authenticated=True, user=user)


@app.route("/hidden-basic-auth/<user>/<passwd>")
def hidden_basic_auth(user="user", passwd="passwd"):
    """Prompts the user for authorization using HTTP Basic Auth.
    ---
    tags:
      - Auth
    parameters:
      - in: path
        name: user
        type: string
      - in: path
        name: passwd
        type: string
    produces:
      - application/json
    responses:
      200:
        description: Sucessful authentication.
      404:
        description: Unsuccessful authentication.
    """

    if not check_basic_auth(user, passwd):
        return status_code(404)
    return jsonify(authenticated=True, user=user)


@app.route("/bearer")
def bearer_auth():
    """Prompts the user for authorization using bearer authentication.
    ---
    tags:
      - Auth
    parameters:
      - in: header
        name: Authorization
        schema:
          type: string
    produces:
      - application/json
    responses:
      200:
        description: Sucessful authentication.
      401:
        description: Unsuccessful authentication.
    """
    authorization = request.headers.get("Authorization")
    if not (authorization and authorization.startswith("Bearer ")):
        response = app.make_response("")
        response.headers["WWW-Authenticate"] = "Bearer"
        response.status_code = 401
        return response
    slice_start = len("Bearer ")
    token = authorization[slice_start:]

    return jsonify(authenticated=True, token=token)


@app.route("/digest-auth/<qop>/<user>/<passwd>")
def digest_auth_md5(qop=None, user="user", passwd="passwd"):
    """Prompts the user for authorization using Digest Auth.
    ---
    tags:
      - Auth
    parameters:
      - in: path
        name: qop
        type: string
        description: auth or auth-int
      - in: path
        name: user
        type: string
      - in: path
        name: passwd
        type: string
    produces:
      - application/json
    responses:
      200:
        description: Sucessful authentication.
      401:
        description: Unsuccessful authentication.
    """
    return digest_auth(qop, user, passwd, "MD5", "never")


@app.route("/digest-auth/<qop>/<user>/<passwd>/<algorithm>")
def digest_auth_nostale(qop=None, user="user", passwd="passwd", algorithm="MD5"):
    """Prompts the user for authorization using Digest Auth + Algorithm.
    ---
    tags:
      - Auth
    parameters:
      - in: path
        name: qop
        type: string
        description: auth or auth-int
      - in: path
        name: user
        type: string
      - in: path
        name: passwd
        type: string
      - in: path
        name: algorithm
        type: string
        description: MD5, SHA-256, SHA-512
        default: MD5
    produces:
      - application/json
    responses:
      200:
        description: Sucessful authentication.
      401:
        description: Unsuccessful authentication.
    """
    return digest_auth(qop, user, passwd, algorithm, "never")


@app.route("/digest-auth/<qop>/<user>/<passwd>/<algorithm>/<stale_after>")
def digest_auth(
    qop=None, user="user", passwd="passwd", algorithm="MD5", stale_after="never"
):
    """Prompts the user for authorization using Digest Auth + Algorithm.
    allow settings the stale_after argument.
    ---
    tags:
      - Auth
    parameters:
      - in: path
        name: qop
        type: string
        description: auth or auth-int
      - in: path
        name: user
        type: string
      - in: path
        name: passwd
        type: string
      - in: path
        name: algorithm
        type: string
        description: MD5, SHA-256, SHA-512
        default: MD5
      - in: path
        name: stale_after
        type: string
        default: never
    produces:
      - application/json
    responses:
      200:
        description: Sucessful authentication.
      401:
        description: Unsuccessful authentication.
    """
    require_cookie_handling = request.args.get("require-cookie", "").lower() in (
        "1",
        "t",
        "true",
    )
    if algorithm not in ("MD5", "SHA-256", "SHA-512"):
        algorithm = "MD5"

    if qop not in ("auth", "auth-int"):
        qop = None

    authorization = request.headers.get("Authorization")
    credentials = None
    if authorization:
        credentials = parse_authorization_header(authorization)

    if (
        not authorization
        or not credentials
        or credentials.type.lower() != "digest"
        or (require_cookie_handling and "Cookie" not in request.headers)
    ):
        response = digest_challenge_response(app, qop, algorithm)
        response.set_cookie("stale_after", value=stale_after)
        response.set_cookie("fake", value="fake_value")
        return response

    if require_cookie_handling and request.cookies.get("fake") != "fake_value":
        response = jsonify({"errors": ["missing cookie set on challenge"]})
        response.set_cookie("fake", value="fake_value")
        response.status_code = 403
        return response

    current_nonce = credentials.get("nonce")

    stale_after_value = None
    if "stale_after" in request.cookies:
        stale_after_value = request.cookies.get("stale_after")

    if (
        "last_nonce" in request.cookies
        and current_nonce == request.cookies.get("last_nonce")
        or stale_after_value == "0"
    ):
        response = digest_challenge_response(app, qop, algorithm, True)
        response.set_cookie("stale_after", value=stale_after)
        response.set_cookie("last_nonce", value=current_nonce)
        response.set_cookie("fake", value="fake_value")
        return response

    if not check_digest_auth(user, passwd):
        response = digest_challenge_response(app, qop, algorithm, False)
        response.set_cookie("stale_after", value=stale_after)
        response.set_cookie("last_nonce", value=current_nonce)
        response.set_cookie("fake", value="fake_value")
        return response

    response = jsonify(authenticated=True, user=user)
    response.set_cookie("fake", value="fake_value")
    if stale_after_value:
        response.set_cookie(
            "stale_after", value=next_stale_after_value(stale_after_value)
        )

    return response


@app.route("/delay/<delay>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE"])
def delay_response(delay):
    """Returns a delayed response (max of 10 seconds).
    ---
    tags:
      - Dynamic data
    parameters:
      - in: path
        name: delay
        type: int
    produces:
      - application/json
    responses:
      200:
        description: A delayed response.
    """
    delay = min(float(delay), 10)

    time.sleep(delay)

    return jsonify(
        get_dict("url", "args", "form", "data", "origin", "headers", "files")
    )


@app.route("/drip")
def drip():
    """Drips data over a duration after an optional initial delay.
    ---
    tags:
      - Dynamic data
    parameters:
      - in: query
        name: duration
        type: number
        description: The amount of time (in seconds) over which to drip each byte
        default: 2
        required: false
      - in: query
        name: numbytes
        type: integer
        description: The number of bytes to respond with
        default: 10
        required: false
      - in: query
        name: code
        type: integer
        description: The response code that will be returned
        default: 200
        required: false
      - in: query
        name: delay
        type: number
        description: The amount of time (in seconds) to delay before responding
        default: 2
        required: false
    produces:
      - application/octet-stream
    responses:
      200:
        description: A dripped response.
    """
    args = CaseInsensitiveDict(request.args.items())
    duration = float(args.get("duration", 2))
    numbytes = min(int(args.get("numbytes", 10)), (10 * 1024 * 1024))  # set 10MB limit
    code = int(args.get("code", 200))

    if numbytes <= 0:
        response = Response("number of bytes must be positive", status=400)
        return response

    delay = float(args.get("delay", 0))
    if delay > 0:
        time.sleep(delay)

    pause = duration / numbytes

    def generate_bytes():
        for i in xrange(numbytes):
            yield b"*"
            time.sleep(pause)

    response = Response(
        generate_bytes(),
        headers={
            "Content-Type": "application/octet-stream",
            "Content-Length": str(numbytes),
        },
    )

    response.status_code = code

    return response


@app.route("/base64/<value>")
def decode_base64(value):
    """Decodes base64url-encoded string.
    ---
    tags:
      - Dynamic data
    parameters:
      - in: path
        name: value
        type: string
        default: SFRUUEJJTiBpcyBhd2Vzb21l
    produces:
      - text/html
    responses:
      200:
        description: Decoded base64 content.
    """
    encoded = value.encode("utf-8")  # base64 expects binary string as input
    try:
        return base64.urlsafe_b64decode(encoded).decode("utf-8")
    except:
        return "Incorrect Base64 data try: SFRUUEJJTiBpcyBhd2Vzb21l"


@app.route("/cache", methods=("GET",))
def cache():
    """Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.
    ---
    tags:
      - Response inspection
    parameters:
      - in: header
        name: If-Modified-Since
      - in: header
        name: If-None-Match
    produces:
      - application/json
    responses:
      200:
        description: Cached response
      304:
        description: Modified

    """
    is_conditional = request.headers.get("If-Modified-Since") or request.headers.get(
        "If-None-Match"
    )

    if is_conditional is None:
        response = view_get()
        response.headers["Last-Modified"] = http_date()
        response.headers["ETag"] = uuid.uuid4().hex
        return response
    else:
        return status_code(304)


@app.route("/etag/<etag>", methods=("GET",))
def etag(etag):
    """Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.
    ---
    tags:
      - Response inspection
    parameters:
      - in: header
        name: If-None-Match
      - in: header
        name: If-Match
    produces:
      - application/json
    responses:
      200:
        description: Normal response
      412:
        description: match

    """
    if_none_match = parse_multi_value_header(request.headers.get("If-None-Match"))
    if_match = parse_multi_value_header(request.headers.get("If-Match"))

    if if_none_match:
        if etag in if_none_match or "*" in if_none_match:
            response = status_code(304)
            response.headers["ETag"] = etag
            return response
    elif if_match:
        if etag not in if_match and "*" not in if_match:
            return status_code(412)

    # Special cases don't apply, return normal response
    response = view_get()
    response.headers["ETag"] = etag
    return response


@app.route("/cache/<int:value>")
def cache_control(value):
    """Sets a Cache-Control header for n seconds.
    ---
    tags:
      - Response inspection
    parameters:
      - in: path
        name: value
        type: integer
    produces:
      - application/json
    responses:
      200:
        description: Cache control set
    """
    response = view_get()
    response.headers["Cache-Control"] = "public, max-age={0}".format(value)
    return response


@app.route("/encoding/utf8")
def encoding():
    """Returns a UTF-8 encoded body.
    ---
    tags:
      - Response formats
    produces:
      - text/html
    responses:
      200:
        description: Encoded UTF-8 content.
    """

    return render_template("UTF-8-demo.txt")


@app.route("/bytes/<int:n>")
def random_bytes(n):
    """Returns n random bytes generated with given seed
    ---
    tags:
      - Dynamic data
    parameters:
      - in: path
        name: n
        type: int
    produces:
      - application/octet-stream
    responses:
      200:
        description: Bytes.
    """

    n = min(n, 100 * 1024)  # set 100KB limit

    params = CaseInsensitiveDict(request.args.items())
    if "seed" in params:
        random.seed(int(params["seed"]))

    response = make_response()

    # Note: can't just use os.urandom here because it ignores the seed
    response.data = bytearray(random.randint(0, 255) for i in range(n))
    response.content_type = "application/octet-stream"
    return response


@app.route("/stream-bytes/<int:n>")
def stream_random_bytes(n):
    """Streams n random bytes generated with given seed, at given chunk size per packet.
    ---
    tags:
      - Dynamic data
    parameters:
      - in: path
        name: n
        type: int
    produces:
      - application/octet-stream
    responses:
      200:
        description: Bytes.
    """
    n = min(n, 100 * 1024)  # set 100KB limit

    params = CaseInsensitiveDict(request.args.items())
    if "seed" in params:
        random.seed(int(params["seed"]))

    if "chunk_size" in params:
        chunk_size = max(1, int(params["chunk_size"]))
    else:
        chunk_size = 10 * 1024

    def generate_bytes():
        chunks = bytearray()

        for i in xrange(n):
            chunks.append(random.randint(0, 255))
            if len(chunks) == chunk_size:
                yield (bytes(chunks))
                chunks = bytearray()

        if chunks:
            yield (bytes(chunks))

    headers = {"Content-Type": "application/octet-stream"}

    return Response(generate_bytes(), headers=headers)


@app.route("/range/<int:numbytes>")
def range_request(numbytes):
    """Streams n random bytes generated with given seed, at given chunk size per packet.
    ---
    tags:
      - Dynamic data
    parameters:
      - in: path
        name: numbytes
        type: int
    produces:
      - application/octet-stream
    responses:
      200:
        description: Bytes.
    """

    if numbytes <= 0 or numbytes > (100 * 1024):
        response = Response(
            headers={"ETag": "range%d" % numbytes, "Accept-Ranges": "bytes"}
        )
        response.status_code = 404
        response.data = "number of bytes must be in the range (0, 102400]"
        return response

    params = CaseInsensitiveDict(request.args.items())
    if "chunk_size" in params:
        chunk_size = max(1, int(params["chunk_size"]))
    else:
        chunk_size = 10 * 1024

    duration = float(params.get("duration", 0))
    pause_per_byte = duration / numbytes

    request_headers = get_headers()
    first_byte_pos, last_byte_pos = get_request_range(request_headers, numbytes)
    range_length = (last_byte_pos + 1) - first_byte_pos

    if (
        first_byte_pos > last_byte_pos
        or first_byte_pos not in xrange(0, numbytes)
        or last_byte_pos not in xrange(0, numbytes)
    ):
        response = Response(
            headers={
                "ETag": "range%d" % numbytes,
                "Accept-Ranges": "bytes",
                "Content-Range": "bytes */%d" % numbytes,
                "Content-Length": "0",
            }
        )
        response.status_code = 416
        return response

    def generate_bytes():
        chunks = bytearray()

        for i in xrange(first_byte_pos, last_byte_pos + 1):

            # We don't want the resource to change across requests, so we need
            # to use a predictable data generation function
            chunks.append(ord("a") + (i % 26))
            if len(chunks) == chunk_size:
                yield (bytes(chunks))
                time.sleep(pause_per_byte * chunk_size)
                chunks = bytearray()

        if chunks:
            time.sleep(pause_per_byte * len(chunks))
            yield (bytes(chunks))

    content_range = "bytes %d-%d/%d" % (first_byte_pos, last_byte_pos, numbytes)
    response_headers = {
        "Content-Type": "application/octet-stream",
        "ETag": "range%d" % numbytes,
        "Accept-Ranges": "bytes",
        "Content-Length": str(range_length),
        "Content-Range": content_range,
    }

    response = Response(generate_bytes(), headers=response_headers)

    if (first_byte_pos == 0) and (last_byte_pos == (numbytes - 1)):
        response.status_code = 200
    else:
        response.status_code = 206

    return response


@app.route("/links/<int:n>/<int:offset>")
def link_page(n, offset):
    """Generate a page containing n links to other pages which do the same.
    ---
    tags:
      - Dynamic data
    parameters:
      - in: path
        name: n
        type: int
      - in: path
        name: offset
        type: int
    produces:
      - text/html
    responses:
      200:
        description: HTML links.
    """
    n = min(max(1, n), 200)  # limit to between 1 and 200 links

    link = "<a href='{0}'>{1}</a> "

    html = ["<html><head><title>Links</title></head><body>"]
    for i in xrange(n):
        if i == offset:
            html.append("{0} ".format(i))
        else:
            html.append(link.format(url_for("link_page", n=n, offset=i), i))
    html.append("</body></html>")

    return "".join(html)


@app.route("/links/<int:n>")
def links(n):
    """Redirect to first links page."""
    return redirect(url_for("link_page", n=n, offset=0))


@app.route("/image")
def image():
    """Returns a simple image of the type suggest by the Accept header.
    ---
    tags:
      - Images
    produces:
      - image/webp
      - image/svg+xml
      - image/jpeg
      - image/png
      - image/*
    responses:
      200:
        description: An image.
    """

    headers = get_headers()
    if "accept" not in headers:
        return image_png()  # Default media type to png

    accept = headers["accept"].lower()

    if "image/webp" in accept:
        return image_webp()
    elif "image/svg+xml" in accept:
        return image_svg()
    elif "image/jpeg" in accept:
        return image_jpeg()
    elif "image/png" in accept or "image/*" in accept:
        return image_png()
    else:
        return status_code(406)  # Unsupported media type


@app.route("/image/png")
def image_png():
    """Returns a simple PNG image.
    ---
    tags:
      - Images
    produces:
      - image/png
    responses:
      200:
        description: A PNG image.
    """
    data = resource("images/pig_icon.png")
    return Response(data, headers={"Content-Type": "image/png"})


@app.route("/image/jpeg")
def image_jpeg():
    """Returns a simple JPEG image.
    ---
    tags:
      - Images
    produces:
      - image/jpeg
    responses:
      200:
        description: A JPEG image.
    """
    data = resource("images/jackal.jpg")
    return Response(data, headers={"Content-Type": "image/jpeg"})


@app.route("/image/webp")
def image_webp():
    """Returns a simple WEBP image.
    ---
    tags:
      - Images
    produces:
      - image/webp
    responses:
      200:
        description: A WEBP image.
    """
    data = resource("images/wolf_1.webp")
    return Response(data, headers={"Content-Type": "image/webp"})


@app.route("/image/svg")
def image_svg():
    """Returns a simple SVG image.
    ---
    tags:
      - Images
    produces:
      - image/svg+xml
    responses:
      200:
        description: An SVG image.
    """
    data = resource("images/svg_logo.svg")
    return Response(data, headers={"Content-Type": "image/svg+xml"})


def resource(filename):
    path = os.path.join(tmpl_dir, filename)
    with open(path, "rb") as f:
      return f.read()


@app.route("/xml")
def xml():
    """Returns a simple XML document.
    ---
    tags:
      - Response formats
    produces:
      - application/xml
    responses:
      200:
        description: An XML document.
    """
    response = make_response(render_template("sample.xml"))
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route("/json")
def a_json_endpoint():
    """Returns a simple JSON document.
    ---
    tags:
      - Response formats
    produces:
      - application/json
    responses:
      200:
        description: An JSON document.
    """
    return flask_jsonify(
        slideshow={
            "title": "Sample Slide Show",
            "date": "date of publication",
            "author": "Yours Truly",
            "slides": [
                {"type": "all", "title": "Wake up to WonderWidgets!"},
                {
                    "type": "all",
                    "title": "Overview",
                    "items": [
                        "Why <em>WonderWidgets</em> are great",
                        "Who <em>buys</em> WonderWidgets",
                    ],
                },
            ],
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    app.run(port=args.port, host=args.host)
```

## File: `httpbin/filters.py`
```python
# -*- coding: utf-8 -*-

"""
httpbin.filters
~~~~~~~~~~~~~~~

This module provides response filter decorators.
"""

import gzip as gzip2
import zlib

import brotli as _brotli

from six import BytesIO
from decimal import Decimal
from time import time as now

from decorator import decorator
from flask import Flask, Response


app = Flask(__name__)


@decorator
def x_runtime(f, *args, **kwargs):
    """X-Runtime Flask Response Decorator."""

    _t0 = now()
    r = f(*args, **kwargs)
    _t1 = now()
    r.headers['X-Runtime'] = '{0}s'.format(Decimal(str(_t1 - _t0)))

    return r


@decorator
def gzip(f, *args, **kwargs):
    """GZip Flask Response Decorator."""

    data = f(*args, **kwargs)

    if isinstance(data, Response):
        content = data.data
    else:
        content = data

    gzip_buffer = BytesIO()
    gzip_file = gzip2.GzipFile(
        mode='wb',
        compresslevel=4,
        fileobj=gzip_buffer
    )
    gzip_file.write(content)
    gzip_file.close()

    gzip_data = gzip_buffer.getvalue()

    if isinstance(data, Response):
        data.data = gzip_data
        data.headers['Content-Encoding'] = 'gzip'
        data.headers['Content-Length'] = str(len(data.data))

        return data

    return gzip_data


@decorator
def deflate(f, *args, **kwargs):
    """Deflate Flask Response Decorator."""

    data = f(*args, **kwargs)

    if isinstance(data, Response):
        content = data.data
    else:
        content = data

    deflater = zlib.compressobj()
    deflated_data = deflater.compress(content)
    deflated_data += deflater.flush()

    if isinstance(data, Response):
        data.data = deflated_data
        data.headers['Content-Encoding'] = 'deflate'
        data.headers['Content-Length'] = str(len(data.data))

        return data

    return deflated_data


@decorator
def brotli(f, *args, **kwargs):
    """Brotli Flask Response Decorator"""

    data = f(*args, **kwargs)

    if isinstance(data, Response):
        content = data.data
    else:
        content = data

    deflated_data = _brotli.compress(content)

    if isinstance(data, Response):
        data.data = deflated_data
        data.headers['Content-Encoding'] = 'br'
        data.headers['Content-Length'] = str(len(data.data))

        return data

    return deflated_data
```

## File: `httpbin/helpers.py`
```python
# -*- coding: utf-8 -*-

"""
httpbin.helpers
~~~~~~~~~~~~~~~

This module provides helper functions for httpbin.
"""

import json
import base64
import re
import time
import os
from hashlib import md5, sha256, sha512
from werkzeug.http import parse_authorization_header
from werkzeug.datastructures import WWWAuthenticate

from flask import request, make_response
from six.moves.urllib.parse import urlparse, urlunparse


from .structures import CaseInsensitiveDict


ASCII_ART = """
    -=[ teapot ]=-

       _...._
     .'  _ _ `.
    | ."` ^ `". _,
    \_;`"---"`|//
      |       ;/
      \_     _/
        `\"\"\"`
"""

REDIRECT_LOCATION = '/redirect/1'

ENV_HEADERS = (
    'X-Varnish',
    'X-Request-Start',
    'X-Heroku-Queue-Depth',
    'X-Real-Ip',
    'X-Forwarded-Proto',
    'X-Forwarded-Protocol',
    'X-Forwarded-Ssl',
    'X-Heroku-Queue-Wait-Time',
    'X-Forwarded-For',
    'X-Heroku-Dynos-In-Use',
    'X-Forwarded-Protocol',
    'X-Forwarded-Port',
    'X-Request-Id',
    'Via',
    'Total-Route-Time',
    'Connect-Time'
)

ROBOT_TXT = """User-agent: *
Disallow: /deny
"""

ACCEPTED_MEDIA_TYPES = [
    'image/webp',
    'image/svg+xml',
    'image/jpeg',
    'image/png',
    'image/*'
]

ANGRY_ASCII ="""
          .-''''''-.
        .' _      _ '.
       /   O      O   \\
      :                :
      |                |
      :       __       :
       \  .-"`  `"-.  /
        '.          .'
          '-......-'
     YOU SHOULDN'T BE HERE
"""


def json_safe(string, content_type='application/octet-stream'):
    """Returns JSON-safe version of `string`.

    If `string` is a Unicode string or a valid UTF-8, it is returned unmodified,
    as it can safely be encoded to JSON string.

    If `string` contains raw/binary data, it is Base64-encoded, formatted and
    returned according to "data" URL scheme (RFC2397). Since JSON is not
    suitable for binary data, some additional encoding was necessary; "data"
    URL scheme was chosen for its simplicity.
    """
    try:
        string = string.decode('utf-8')
        json.dumps(string)
        return string
    except (ValueError, TypeError):
        return b''.join([
            b'data:',
            content_type.encode('utf-8'),
            b';base64,',
            base64.b64encode(string)
        ]).decode('utf-8')


def get_files():
    """Returns files dict from request context."""

    files = dict()

    for k, v in request.files.items():
        content_type = request.files[k].content_type or 'application/octet-stream'
        val = json_safe(v.read(), content_type)
        if files.get(k):
            if not isinstance(files[k], list):
                files[k] = [files[k]]
            files[k].append(val)
        else:
            files[k] = val

    return files


def get_headers(hide_env=True):
    """Returns headers dict from request context."""

    headers = dict(request.headers.items())

    if hide_env and ('show_env' not in request.args):
        for key in ENV_HEADERS:
            try:
                del headers[key]
            except KeyError:
                pass

    return CaseInsensitiveDict(headers.items())


def semiflatten(multi):
    """Convert a MutiDict into a regular dict. If there are more than one value
    for a key, the result will have a list of values for the key. Otherwise it
    will have the plain value."""
    if multi:
        result = multi.to_dict(flat=False)
        for k, v in result.items():
            if len(v) == 1:
                result[k] = v[0]
        return result
    else:
        return multi

def get_url(request):
    """
    Since we might be hosted behind a proxy, we need to check the
    X-Forwarded-Proto, X-Forwarded-Protocol, or X-Forwarded-SSL headers
    to find out what protocol was used to access us.
    """
    protocol = request.headers.get('X-Forwarded-Proto') or request.headers.get('X-Forwarded-Protocol')
    if protocol is None and request.headers.get('X-Forwarded-Ssl') == 'on':
        protocol = 'https'
    if protocol is None:
        return request.url
    url = list(urlparse(request.url))
    url[0] = protocol
    return urlunparse(url)


def get_dict(*keys, **extras):
    """Returns request dict of given keys."""

    _keys = ('url', 'args', 'form', 'data', 'origin', 'headers', 'files', 'json', 'method')

    assert all(map(_keys.__contains__, keys))
    data = request.data
    form = semiflatten(request.form)

    try:
        _json = json.loads(data.decode('utf-8'))
    except (ValueError, TypeError):
        _json = None

    d = dict(
        url=get_url(request),
        args=semiflatten(request.args),
        form=form,
        data=json_safe(data),
        origin=request.headers.get('X-Forwarded-For', request.remote_addr),
        headers=get_headers(),
        files=get_files(),
        json=_json,
        method=request.method,
    )

    out_d = dict()

    for key in keys:
        out_d[key] = d.get(key)

    out_d.update(extras)

    return out_d


def status_code(code):
    """Returns response object of given status code."""

    redirect = dict(headers=dict(location=REDIRECT_LOCATION))

    code_map = {
        301: redirect,
        302: redirect,
        303: redirect,
        304: dict(data=''),
        305: redirect,
        307: redirect,
        401: dict(headers={'WWW-Authenticate': 'Basic realm="Fake Realm"'}),
        402: dict(
            data='Fuck you, pay me!',
            headers={
                'x-more-info': 'http://vimeo.com/22053820'
            }
        ),
        406: dict(data=json.dumps({
                'message': 'Client did not request a supported media type.',
                'accept': ACCEPTED_MEDIA_TYPES
            }),
            headers={
                'Content-Type': 'application/json'
            }),
        407: dict(headers={'Proxy-Authenticate': 'Basic realm="Fake Realm"'}),
        418: dict(  # I'm a teapot!
            data=ASCII_ART,
            headers={
                'x-more-info': 'http://tools.ietf.org/html/rfc2324'
            }
        ),

    }

    r = make_response()
    r.status_code = code

    if code in code_map:

        m = code_map[code]

        if 'data' in m:
            r.data = m['data']
        if 'headers' in m:
            r.headers = m['headers']

    return r


def check_basic_auth(user, passwd):
    """Checks user authentication using HTTP Basic Auth."""

    auth = request.authorization
    return auth and auth.username == user and auth.password == passwd



# Digest auth helpers
# qop is a quality of protection

def H(data, algorithm):
    if algorithm == 'SHA-256':
        return sha256(data).hexdigest()
    elif algorithm == 'SHA-512':
        return sha512(data).hexdigest()
    else:
        return md5(data).hexdigest()


def HA1(realm, username, password, algorithm):
    """Create HA1 hash by realm, username, password

    HA1 = md5(A1) = MD5(username:realm:password)
    """
    if not realm:
        realm = u''
    return H(b":".join([username.encode('utf-8'),
                           realm.encode('utf-8'),
                           password.encode('utf-8')]), algorithm)


def HA2(credentials, request, algorithm):
    """Create HA2 md5 hash

    If the qop directive's value is "auth" or is unspecified, then HA2:
        HA2 = md5(A2) = MD5(method:digestURI)
    If the qop directive's value is "auth-int" , then HA2 is
        HA2 = md5(A2) = MD5(method:digestURI:MD5(entityBody))
    """
    if credentials.get("qop") == "auth" or credentials.get('qop') is None:
        return H(b":".join([request['method'].encode('utf-8'), request['uri'].encode('utf-8')]), algorithm)
    elif credentials.get("qop") == "auth-int":
        for k in 'method', 'uri', 'body':
            if k not in request:
                raise ValueError("%s required" % k)
        A2 = b":".join([request['method'].encode('utf-8'),
                        request['uri'].encode('utf-8'),
                        H(request['body'], algorithm).encode('utf-8')])
        return H(A2, algorithm)
    raise ValueError


def response(credentials, password, request):
    """Compile digest auth response

    If the qop directive's value is "auth" or "auth-int" , then compute the response as follows:
       RESPONSE = MD5(HA1:nonce:nonceCount:clienNonce:qop:HA2)
    Else if the qop directive is unspecified, then compute the response as follows:
       RESPONSE = MD5(HA1:nonce:HA2)

    Arguments:
    - `credentials`: credentials dict
    - `password`: request user password
    - `request`: request dict
    """
    response = None
    algorithm = credentials.get('algorithm')
    HA1_value = HA1(
        credentials.get('realm'),
        credentials.get('username'),
        password,
        algorithm
    )
    HA2_value = HA2(credentials, request, algorithm)
    if credentials.get('qop') is None:
        response = H(b":".join([
            HA1_value.encode('utf-8'),
            credentials.get('nonce', '').encode('utf-8'),
            HA2_value.encode('utf-8')
        ]), algorithm)
    elif credentials.get('qop') == 'auth' or credentials.get('qop') == 'auth-int':
        for k in 'nonce', 'nc', 'cnonce', 'qop':
            if k not in credentials:
                raise ValueError("%s required for response H" % k)
        response = H(b":".join([HA1_value.encode('utf-8'),
                               credentials.get('nonce').encode('utf-8'),
                               credentials.get('nc').encode('utf-8'),
                               credentials.get('cnonce').encode('utf-8'),
                               credentials.get('qop').encode('utf-8'),
                               HA2_value.encode('utf-8')]), algorithm)
    else:
        raise ValueError("qop value are wrong")

    return response


def check_digest_auth(user, passwd):
    """Check user authentication using HTTP Digest auth"""

    if request.headers.get('Authorization'):
        credentials = parse_authorization_header(request.headers.get('Authorization'))
        if not credentials:
            return
        request_uri = request.script_root + request.path
        if request.query_string:
            request_uri +=  '?' + request.query_string
        response_hash = response(credentials, passwd, dict(uri=request_uri,
                                                           body=request.data,
                                                           method=request.method))
        if credentials.get('response') == response_hash:
            return True
    return False

def secure_cookie():
    """Return true if cookie should have secure attribute"""
    return request.environ['wsgi.url_scheme'] == 'https'

def __parse_request_range(range_header_text):
    """ Return a tuple describing the byte range requested in a GET request
    If the range is open ended on the left or right side, then a value of None
    will be set.
    RFC7233: http://svn.tools.ietf.org/svn/wg/httpbis/specs/rfc7233.html#header.range
    Examples:
      Range : bytes=1024-
      Range : bytes=10-20
      Range : bytes=-999
    """

    left = None
    right = None

    if not range_header_text:
        return left, right

    range_header_text = range_header_text.strip()
    if not range_header_text.startswith('bytes'):
        return left, right

    components = range_header_text.split("=")
    if len(components) != 2:
        return left, right

    components = components[1].split("-")

    try:
        right = int(components[1])
    except:
        pass

    try:
        left = int(components[0])
    except:
        pass

    return left, right

def get_request_range(request_headers, upper_bound):
    first_byte_pos, last_byte_pos = __parse_request_range(request_headers['range'])

    if first_byte_pos is None and last_byte_pos is None:
        # Request full range
        first_byte_pos = 0
        last_byte_pos = upper_bound - 1
    elif first_byte_pos is None:
        # Request the last X bytes
        first_byte_pos = max(0, upper_bound - last_byte_pos)
        last_byte_pos = upper_bound - 1
    elif last_byte_pos is None:
        # Request the last X bytes
        last_byte_pos = upper_bound - 1

    return first_byte_pos, last_byte_pos

def parse_multi_value_header(header_str):
    """Break apart an HTTP header string that is potentially a quoted, comma separated list as used in entity headers in RFC2616."""
    parsed_parts = []
    if header_str:
        parts = header_str.split(',')
        for part in parts:
            match = re.search('\s*(W/)?\"?([^"]*)\"?\s*', part)
            if match is not None:
                parsed_parts.append(match.group(2))
    return parsed_parts


def next_stale_after_value(stale_after):
    try:
        stal_after_count = int(stale_after) - 1
        return str(stal_after_count)
    except ValueError:
        return 'never'


def digest_challenge_response(app, qop, algorithm, stale = False):
    response = app.make_response('')
    response.status_code = 401

    # RFC2616 Section4.2: HTTP headers are ASCII.  That means
    # request.remote_addr was originally ASCII, so I should be able to
    # encode it back to ascii.  Also, RFC2617 says about nonces: "The
    # contents of the nonce are implementation dependent"
    nonce = H(b''.join([
        getattr(request, 'remote_addr', u'').encode('ascii'),
        b':',
        str(time.time()).encode('ascii'),
        b':',
        os.urandom(10)
    ]), algorithm)
    opaque = H(os.urandom(10), algorithm)

    auth = WWWAuthenticate("digest")
    auth.set_digest('me@kennethreitz.com', nonce, opaque=opaque,
                    qop=('auth', 'auth-int') if qop is None else (qop,), algorithm=algorithm)
    auth.stale = stale
    response.headers['WWW-Authenticate'] = auth.to_header()
    return response
```

## File: `httpbin/structures.py`
```python
# -*- coding: utf-8 -*-

"""
httpbin.structures
~~~~~~~~~~~~~~~~~~~

Data structures that power httpbin.
"""


class CaseInsensitiveDict(dict):
    """Case-insensitive Dictionary for headers.

    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header.
    """

    def _lower_keys(self):
        return [k.lower() for k in self.keys()]

    def __contains__(self, key):
        return key.lower() in self._lower_keys()

    def __getitem__(self, key):
        # We allow fall-through here, so values default to None
        if key in self:
            return list(self.items())[self._lower_keys().index(key.lower())][1]
```

## File: `httpbin/utils.py`
```python
# -*- coding: utf-8 -*-

"""
httpbin.utils
~~~~~~~~~~~~~~~

Utility functions.
"""

import random
import bisect


def weighted_choice(choices):
    """Returns a value from choices chosen by weighted random selection

    choices should be a list of (value, weight) tuples.

    eg. weighted_choice([('val1', 5), ('val2', 0.3), ('val3', 1)])

    """
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.uniform(0, total)
    i = bisect.bisect(cum_weights, x)
    return values[i]
```

## File: `httpbin/VERSION`
```
0.9.2
```

## File: `httpbin/__init__.py`
```python
# -*- coding: utf-8 -*-

from .core import *
```

## File: `httpbin/templates/footer.html`
```html
<div class='swagger-ui'>
    <div class="wrapper">
        <section class="block col-12 block-desktop col-12-desktop">
            <div>

                <h2>Other Utilities</h2>

                <ul>
                    <li>
                        <a href="{{url_for('view_forms_post')}}">HTML form</a> that posts to /post /forms/post</li>
                </ul>

                <br />
                <br />
            </div>
        </section>
    </div>
</div>
```

## File: `httpbin/templates/forms-post.html`
```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
  <!-- Example form from HTML5 spec http://www.w3.org/TR/html5/forms.html#writing-a-form's-user-interface -->
  <form method="post" action="{{ url_for('view_post') }}">
   <p><label>Customer name: <input name="custname"></label></p>
   <p><label>Telephone: <input type=tel name="custtel"></label></p>
   <p><label>E-mail address: <input type=email name="custemail"></label></p>
   <fieldset>
    <legend> Pizza Size </legend>
    <p><label> <input type=radio name=size value="small"> Small </label></p>
    <p><label> <input type=radio name=size value="medium"> Medium </label></p>
    <p><label> <input type=radio name=size value="large"> Large </label></p>
   </fieldset>
   <fieldset>
    <legend> Pizza Toppings </legend>
    <p><label> <input type=checkbox name="topping" value="bacon"> Bacon </label></p>
    <p><label> <input type=checkbox name="topping" value="cheese"> Extra Cheese </label></p>
    <p><label> <input type=checkbox name="topping" value="onion"> Onion </label></p>
    <p><label> <input type=checkbox name="topping" value="mushroom"> Mushroom </label></p>
   </fieldset>
   <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900" name="delivery"></label></p>
   <p><label>Delivery instructions: <textarea name="comments"></textarea></label></p>
   <p><button>Submit order</button></p>
  </form>
  </body>
</html>
```

## File: `httpbin/templates/httpbin.1.html`
```html
<div class='mp'>
<h1>httpbin(1): HTTP Request &amp; Response Service</h1>
<p>Freely hosted in <a href="http://httpbin.org">HTTP</a>, <a href="https://httpbin.org">HTTPS</a>, &amp; <a href="http://eu.httpbin.org/">EU</a> flavors by <a href="http://kennethreitz.org/bitcoin">Kenneth Reitz</a> &amp; <a href="https://www.heroku.com/python">Heroku</a>.</p>

<h2 id="BONUSPOINTS">BONUSPOINTS</h2>

<ul>
<li><a href="https://now.httpbin.org/" data-bare-link="true"><code>now.httpbin.org</code></a> The current time, in a variety of formats.</li>
</ul>

<h2 id="ENDPOINTS">ENDPOINTS</h2>

<ul>
<li><a href="{{ url_for('view_landing_page') }}" data-bare-link="true"><code>/</code></a> This page.</li>
<li><a href="{{ url_for('view_origin') }}" data-bare-link="true"><code>/ip</code></a> Returns Origin IP.</li>
<li><a href="{{ url_for('view_uuid') }}" data-bare-link="true"><code>/uuid</code></a> Returns UUID4.</li>
<li><a href="{{ url_for('view_user_agent') }}" data-bare-link="true"><code>/user-agent</code></a> Returns user-agent.</li>
<li><a href="{{ url_for('view_headers') }}" data-bare-link="true"><code>/headers</code></a> Returns header dict.</li>
<li><a href="{{ url_for('view_get') }}" data-bare-link="true"><code>/get</code></a> Returns GET data.</li>
<li><code>/post</code> Returns POST data.</li>
<li><code>/patch</code> Returns PATCH data.</li>
<li><code>/put</code> Returns PUT data.</li>
<li><code>/delete</code> Returns DELETE data</li>
<li><a href="{{ url_for('view_anything') }}" data-bare-link="true"><code>/anything</code></a> Returns request data, including method used.</li>
<li><code>/anything/:anything</code> Returns request data, including the URL.</li>
<li><a href="{{ url_for('decode_base64', value='aGVsbG8gd29ybGQNCg==') }}"><code>/base64/:value</code></a> Decodes base64url-encoded string.</li>
<li><a href="{{ url_for('encoding') }}"><code>/encoding/utf8</code></a> Returns page containing UTF-8 data.</li>
<li><a href="{{ url_for('view_gzip_encoded_content') }}" data-bare-link="true"><code>/gzip</code></a> Returns gzip-encoded data.</li>
<li><a href="{{ url_for('view_deflate_encoded_content') }}" data-bare-link="true"><code>/deflate</code></a> Returns deflate-encoded data.</li>
<li><a href="{{ url_for('view_brotli_encoded_content') }}" data-bare-link="true"><code>/brotli</code></a> Returns brotli-encoded data.</li>
<li><a href="{{ url_for('view_status_code', codes='418') }}"><code>/status/:code</code></a> Returns given HTTP Status code.</li>
<li><a href="{{ url_for('response_headers', **{'Content-Type': 'text/plain; charset=UTF-8', 'Server': 'httpbin'}) }}"><code>/response-headers?key=val</code></a> Returns given response headers.</li>
<li><a href="{{ url_for('redirect_n_times', n=6) }}"><code>/redirect/:n</code></a> 302 Redirects <em>n</em> times.</li>
<li><a href="{{ url_for('redirect_to', url='http://example.com/') }}"><code>/redirect-to?url=foo</code></a> 302 Redirects to the <em>foo</em> URL.</li>
<li><a href="{{ url_for('redirect_to', url='http://example.com/', status_code=307) }}"><code>/redirect-to?url=foo&status_code=307</code></a> 307 Redirects to the <em>foo</em> URL.</li>
<li><a href="{{ url_for('relative_redirect_n_times', n=6) }}"><code>/relative-redirect/:n</code></a> 302 Relative redirects <em>n</em> times.</li>
<li><a href="{{ url_for('absolute_redirect_n_times', n=6) }}"><code>/absolute-redirect/:n</code></a> 302 Absolute redirects <em>n</em> times.</li>
<li><a href="{{ url_for('view_cookies') }}" data-bare-link="true"><code>/cookies</code></a> Returns cookie data.</li>
<li><a href="{{ url_for('set_cookies', k1='v1', k2='v2') }}"><code>/cookies/set?name=value</code></a> Sets one or more simple cookies.</li>
<li><a href="{{ url_for('delete_cookies', k1='', k2='') }}"><code>/cookies/delete?name</code></a> Deletes one or more simple cookies.</li>
<li><a href="{{ url_for('basic_auth', user='user', passwd='passwd') }}"><code>/basic-auth/:user/:passwd</code></a> Challenges HTTPBasic Auth.</li>
<li><a href="{{ url_for('hidden_basic_auth', user='user', passwd='passwd') }}"><code>/hidden-basic-auth/:user/:passwd</code></a> 404'd BasicAuth.</li>
<li><a href="{{ url_for('digest_auth', qop='auth', user='user', passwd='passwd', algorithm='MD5', stale_after='never') }}"><code>/digest-auth/:qop/:user/:passwd/:algorithm</code></a> Challenges HTTP Digest Auth.</li>
<li><a href="{{ url_for('digest_auth', qop='auth', user='user', passwd='passwd', algorithm='MD5', stale_after='never') }}"><code>/digest-auth/:qop/:user/:passwd</code></a> Challenges HTTP Digest Auth.</li>
<li><a href="{{ url_for('stream_n_messages', n=20) }}"><code>/stream/:n</code></a> Streams <em>min(n, 100)</em> lines.</li>
<li><a href="{{ url_for('delay_response', delay=3) }}"><code>/delay/:n</code></a> Delays responding for <em>min(n, 10)</em> seconds.</li>
<li><a href="{{ url_for('drip', numbytes=5, duration=5, code=200) }}"><code>/drip?numbytes=n&amp;duration=s&amp;delay=s&amp;code=code</code></a> Drips data over a duration after an optional initial delay, then (optionally) returns with the given status code.</li>
<li><a href="{{ url_for('range_request', numbytes=1024) }}"><code>/range/1024?duration=s&amp;chunk_size=code</code></a> Streams <em>n</em> bytes, and allows specifying a <em>Range</em> header to select a subset of the data. Accepts a <em>chunk_size</em> and request <em>duration</em> parameter.</li>
<li><a href="{{ url_for('view_html_page') }}" data-bare-link="true"><code>/html</code></a> Renders an HTML Page.</li>
<li><a href="{{ url_for('view_robots_page') }}" data-bare-link="true"><code>/robots.txt</code></a> Returns some robots.txt rules.</li>
<li><a href="{{ url_for('view_deny_page') }}" data-bare-link="true"><code>/deny</code></a> Denied by robots.txt file.</li>
<li><a href="{{ url_for('cache') }}" data-bare-link="true"><code>/cache</code></a> Returns 200 unless an If-Modified-Since or If-None-Match header is provided, when it returns a 304.</li>
<li><a href="{{ url_for('etag', etag='etag') }}"><code>/etag/:etag</code></a> Assumes the resource has the given etag and responds to If-None-Match header with a 200 or 304 and If-Match with a 200 or 412 as appropriate.</li>
<li><a href="{{ url_for('cache_control', value=60) }}"><code>/cache/:n</code></a> Sets a Cache-Control header for <em>n</em> seconds.</li>
<li><a href="{{ url_for('random_bytes', n=1024) }}"><code>/bytes/:n</code></a> Generates <em>n</em> random bytes of binary data, accepts optional <em>seed</em> integer parameter.</li>
<li><a href="{{ url_for('stream_random_bytes', n=1024) }}"><code>/stream-bytes/:n</code></a> Streams <em>n</em> random bytes of binary data in chunked encoding, accepts optional <em>seed</em> and <em>chunk_size</em> integer parameters.</li>
<li><a href="{{ url_for('links', n=10) }}"><code>/links/:n</code></a> Returns page containing <em>n</em> HTML links.</li>
<li><a href="{{ url_for('image') }}"><code>/image</code></a> Returns page containing an image based on sent Accept header.</li>
<li><a href="{{ url_for('image_png') }}"><code>/image/png</code></a> Returns a PNG image.</li>
<li><a href="{{ url_for('image_jpeg') }}"><code>/image/jpeg</code></a> Returns a JPEG image.</li>
<li><a href="{{ url_for('image_webp') }}"><code>/image/webp</code></a> Returns a WEBP image.</li>
<li><a href="{{ url_for('image_svg') }}"><code>/image/svg</code></a> Returns a SVG image.</li>
<li><a href="{{ url_for('view_forms_post') }}" data-bare-link="true"><code>/forms/post</code></a> HTML form that submits to <em>/post</em></li>
<li><a href="{{ url_for('xml') }}" data-bare-link="true"><code>/xml</code></a> Returns some XML</li>
</ul>

<h2 id="DESCRIPTION">DESCRIPTION</h2>

<p>Testing an HTTP Library can become difficult sometimes. <a href="http://requestb.in">RequestBin</a> is fantastic for testing POST requests, but doesn't let you control the response. This exists to cover all kinds of HTTP scenarios. Additional endpoints are being considered.</p>

<p>All endpoint responses are JSON-encoded.</p>

<h2 id="EXAMPLES">EXAMPLES</h2>

<h3 id="-curl-http-httpbin-org-ip">$ curl http://httpbin.org/ip</h3>

<pre><code>{"origin": "24.127.96.129"}
</code></pre>

<h3 id="-curl-http-httpbin-org-user-agent">$ curl http://httpbin.org/user-agent</h3>

<pre><code>{"user-agent": "curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3"}
</code></pre>

<h3 id="-curl-http-httpbin-org-get">$ curl http://httpbin.org/get</h3>

<pre><code>{
   "args": {},
   "headers": {
      "Accept": "*/*",
      "Connection": "close",
      "Content-Length": "",
      "Content-Type": "",
      "Host": "httpbin.org",
      "User-Agent": "curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3"
   },
   "origin": "24.127.96.129",
   "url": "http://httpbin.org/get"
}
</code></pre>

<h3 id="-curl-I-http-httpbin-org-status-418">$ curl -I http://httpbin.org/status/418</h3>

<pre><code>HTTP/1.1 418 I'M A TEAPOT
Server: nginx/0.7.67
Date: Mon, 13 Jun 2011 04:25:38 GMT
Connection: close
x-more-info: http://tools.ietf.org/html/rfc2324
Content-Length: 135
</code></pre>

<h3 id="-curl-https-httpbin-org-get-show_env-1">$ curl https://httpbin.org/get?show_env=1</h3>

<pre><code>{
  "headers": {
    "Content-Length": "",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "gzip,deflate,sdch",
    "X-Forwarded-Port": "443",
    "X-Forwarded-For": "109.60.101.240",
    "Host": "httpbin.org",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11",
    "X-Request-Start": "1350053933441",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Connection": "keep-alive",
    "X-Forwarded-Proto": "https",
    "Cookie": "_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1",
    "Content-Type": ""
  },
  "args": {
    "show_env": "1"
  },
  "origin": "109.60.101.240",
  "url": "http://httpbin.org/get?show_env=1"
}
</code></pre>

<h2 id="Installing-and-running-from-PyPI">Installing and running from PyPI</h2>

<p>You can install httpbin as a library from PyPI and run it as a WSGI app.  For example, using Gunicorn:</p>

<pre><code class="bash">$ pip install httpbin
$ gunicorn httpbin:app
</code></pre>


<h2 id="AUTHOR">AUTHOR</h2>

<p>A <a href="http://kennethreitz.com/">Kenneth Reitz</a> project.</p>
<p>BTC: <a href="https://www.kennethreitz.org/bitcoin"><code>1Me2iXTJ91FYZhrGvaGaRDCBtnZ4KdxCug</code></a></p>

<h2 id="SEE-ALSO">SEE ALSO</h2>

<p><a href="https://www.hurl.it">Hurl.it</a> - Make HTTP requests.</p>
<p><a href="http://requestb.in">RequestBin</a> - Inspect HTTP requests.</p>
<p><a href="http://python-requests.org" data-bare-link="true">http://python-requests.org</a></p>

</div>
```

## File: `httpbin/templates/index.html`
```html
<!DOCTYPE html>
<html>

<head>
  <meta http-equiv='content-type' value='text/html;charset=utf8'>
  <meta name='generator' value='Ronn/v0.7.3 (http://github.com/rtomayko/ronn/tree/0.7.3)'>
  <title>httpbin(1): HTTP Client Testing Service</title>
  <style type='text/css' media='all'>
    /* style: man */

    body#manpage {
      margin: 0;
    }

    .mp {
      max-width: 100ex;
      padding: 0 9ex 1ex 4ex;
    }

    .mp p,
    .mp pre,
    .mp ul,
    .mp ol,
    .mp dl {
      margin: 0 0 20px 0;
    }

    .mp h2 {
      margin: 10px 0 0 0;
    }

    .mp>p,
    .mp>pre,
    .mp>ul,
    .mp>ol,
    .mp>dl {
      margin-left: 8ex;
    }

    .mp h3 {
      margin: 0 0 0 4ex;
    }

    .mp dt {
      margin: 0;
      clear: left;
    }

    .mp dt.flush {
      float: left;
      width: 8ex;
    }

    .mp dd {
      margin: 0 0 0 9ex;
    }

    .mp h1,
    .mp h2,
    .mp h3,
    .mp h4 {
      clear: left;
    }

    .mp pre {
      margin-bottom: 20px;
    }

    .mp pre+h2,
    .mp pre+h3 {
      margin-top: 22px;
    }

    .mp h2+pre,
    .mp h3+pre {
      margin-top: 5px;
    }

    .mp img {
      display: block;
      margin: auto;
    }

    .mp h1.man-title {
      display: none;
    }

    .mp,
    .mp code,
    .mp pre,
    .mp tt,
    .mp kbd,
    .mp samp,
    .mp h3,
    .mp h4 {
      font-family: monospace;
      font-size: 14px;
      line-height: 1.42857142857143;
    }

    .mp h2 {
      font-size: 16px;
      line-height: 1.25;
    }

    .mp h1 {
      font-size: 20px;
      line-height: 2;
    }

    .mp {
      text-align: justify;
      background: #fff;
    }

    .mp,
    .mp code,
    .mp pre,
    .mp pre code,
    .mp tt,
    .mp kbd,
    .mp samp {
      color: #131211;
    }

    .mp h1,
    .mp h2,
    .mp h3,
    .mp h4 {
      color: #030201;
    }

    .mp u {
      text-decoration: underline;
    }

    .mp code,
    .mp strong,
    .mp b {
      font-weight: bold;
      color: #131211;
    }

    .mp em,
    .mp var {
      font-style: italic;
      color: #232221;
      text-decoration: none;
    }

    .mp a,
    .mp a:link,
    .mp a:hover,
    .mp a code,
    .mp a pre,
    .mp a tt,
    .mp a kbd,
    .mp a samp {
      color: #0000ff;
    }

    .mp b.man-ref {
      font-weight: normal;
      color: #434241;
    }

    .mp pre {
      padding: 0 4ex;
    }

    .mp pre code {
      font-weight: normal;
      color: #434241;
    }

    .mp h2+pre,
    h3+pre {
      padding-left: 0;
    }

    ol.man-decor,
    ol.man-decor li {
      margin: 3px 0 10px 0;
      padding: 0;
      float: left;
      width: 33%;
      list-style-type: none;
      text-transform: uppercase;
      color: #999;
      letter-spacing: 1px;
    }

    ol.man-decor {
      width: 100%;
    }

    ol.man-decor li.tl {
      text-align: left;
    }

    ol.man-decor li.tc {
      text-align: center;
      letter-spacing: 4px;
    }

    ol.man-decor li.tr {
      text-align: right;
      float: right;
    }
  </style>
  <style type='text/css' media='all'>
    /* style: 80c */

    .mp {
      max-width: 86ex
    }

    ul {
      list-style: None;
      margin-left: 1em !important
    }

    .man-navigation {
      left: 101ex
    }

    .scheme-container {
      display: none !important;
    }
  </style>
</head>

<body id='manpage'>
  <a href="https://github.com/requests/httpbin" class="github-corner" aria-label="View source on Github">
    <svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;"
      aria-hidden="true">
      <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
      <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"
        fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
      <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"
        fill="currentColor" class="octo-body"></path>
    </svg>
  </a>



  {% include 'httpbin.1.html' %} {% if tracking_enabled %} {% include 'trackingscripts.html' %} {% endif %}

</body>

</html>
```

## File: `httpbin/templates/moby.html`
```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
      <h1>Herman Melville - Moby-Dick</h1>

      <div>
        <p>
          Availing himself of the mild, summer-cool weather that now reigned in these latitudes, and in preparation for the peculiarly active pursuits shortly to be anticipated, Perth, the begrimed, blistered old blacksmith, had not removed his portable forge to the hold again, after concluding his contributory work for Ahab's leg, but still retained it on deck, fast lashed to ringbolts by the foremast; being now almost incessantly invoked by the headsmen, and harpooneers, and bowsmen to do some little job for them; altering, or repairing, or new shaping their various weapons and boat furniture. Often he would be surrounded by an eager circle, all waiting to be served; holding boat-spades, pike-heads, harpoons, and lances, and jealously watching his every sooty movement, as he toiled. Nevertheless, this old man's was a patient hammer wielded by a patient arm. No murmur, no impatience, no petulance did come from him. Silent, slow, and solemn; bowing over still further his chronically broken back, he toiled away, as if toil were life itself, and the heavy beating of his hammer the heavy beating of his heart. And so it was.—Most miserable! A peculiar walk in this old man, a certain slight but painful appearing yawing in his gait, had at an early period of the voyage excited the curiosity of the mariners. And to the importunity of their persisted questionings he had finally given in; and so it came to pass that every one now knew the shameful story of his wretched fate. Belated, and not innocently, one bitter winter's midnight, on the road running between two country towns, the blacksmith half-stupidly felt the deadly numbness stealing over him, and sought refuge in a leaning, dilapidated barn. The issue was, the loss of the extremities of both feet. Out of this revelation, part by part, at last came out the four acts of the gladness, and the one long, and as yet uncatastrophied fifth act of the grief of his life's drama. He was an old man, who, at the age of nearly sixty, had postponedly encountered that thing in sorrow's technicals called ruin. He had been an artisan of famed excellence, and with plenty to do; owned a house and garden; embraced a youthful, daughter-like, loving wife, and three blithe, ruddy children; every Sunday went to a cheerful-looking church, planted in a grove. But one night, under cover of darkness, and further concealed in a most cunning disguisement, a desperate burglar slid into his happy home, and robbed them all of everything. And darker yet to tell, the blacksmith himself did ignorantly conduct this burglar into his family's heart. It was the Bottle Conjuror! Upon the opening of that fatal cork, forth flew the fiend, and shrivelled up his home. Now, for prudent, most wise, and economic reasons, the blacksmith's shop was in the basement of his dwelling, but with a separate entrance to it; so that always had the young and loving healthy wife listened with no unhappy nervousness, but with vigorous pleasure, to the stout ringing of her young-armed old husband's hammer; whose reverberations, muffled by passing through the floors and walls, came up to her, not unsweetly, in her nursery; and so, to stout Labor's iron lullaby, the blacksmith's infants were rocked to slumber. Oh, woe on woe! Oh, Death, why canst thou not sometimes be timely? Hadst thou taken this old blacksmith to thyself ere his full ruin came upon him, then had the young widow had a delicious grief, and her orphans a truly venerable, legendary sire to dream of in their after years; and all of them a care-killing competency.
        </p>
      </div>
  </body>
</html>
```

## File: `httpbin/templates/sample.xml`
```xml
<?xml version='1.0' encoding='us-ascii'?>

<!--  A SAMPLE set of slides  -->

<slideshow 
    title="Sample Slide Show"
    date="Date of publication"
    author="Yours Truly"
    >

    <!-- TITLE SLIDE -->
    <slide type="all">
      <title>Wake up to WonderWidgets!</title>
    </slide>

    <!-- OVERVIEW -->
    <slide type="all">
        <title>Overview</title>
        <item>Why <em>WonderWidgets</em> are great</item>
        <item/>
        <item>Who <em>buys</em> WonderWidgets</item>
    </slide>

</slideshow>
```

## File: `httpbin/templates/trackingscripts.html`
```html
{#
	place tracking scripts (like Google Analytics) here
#}

<script type="text/javascript">
  var _gauges = _gauges || [];
  (function() {
    var t   = document.createElement('script');
    t.type  = 'text/javascript';
    t.async = true;
    t.id    = 'gauges-tracker';
    t.setAttribute('data-site-id', '58cb2e71c88d9043ac01d000');
    t.setAttribute('data-track-path', 'https://track.gaug.es/track.gif');
    t.src = 'https://d36ee2fcip1434.cloudfront.net/track.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(t, s);
  })();
</script>
```

## File: `httpbin/templates/UTF-8-demo.txt`
```
<h1>Unicode Demo</h1>

<p>Taken from <a
href="http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt">http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt</a></p>

<pre>

UTF-8 encoded sample plain-text file
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Markus Kuhn [ˈmaʳkʊs kuːn] <http://www.cl.cam.ac.uk/~mgk25/> — 2002-07-25


The ASCII compatible UTF-8 encoding used in this plain-text file
is defined in Unicode, ISO 10646-1, and RFC 2279.


Using Unicode/UTF-8, you can write in emails and source code things such as

Mathematics and sciences:

  ∮ E⋅da = Q,  n → ∞, ∑ f(i) = ∏ g(i),      ⎧⎡⎛┌─────┐⎞⎤⎫
                                            ⎪⎢⎜│a²+b³ ⎟⎥⎪
  ∀x∈ℝ: ⌈x⌉ = −⌊−x⌋, α ∧ ¬β = ¬(¬α ∨ β),    ⎪⎢⎜│───── ⎟⎥⎪
                                            ⎪⎢⎜⎷ c₈   ⎟⎥⎪
  ℕ ⊆ ℕ₀ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ,                   ⎨⎢⎜       ⎟⎥⎬
                                            ⎪⎢⎜ ∞     ⎟⎥⎪
  ⊥ < a ≠ b ≡ c ≤ d ≪ ⊤ ⇒ (⟦A⟧ ⇔ ⟪B⟫),      ⎪⎢⎜ ⎲     ⎟⎥⎪
                                            ⎪⎢⎜ ⎳aⁱ-bⁱ⎟⎥⎪
  2H₂ + O₂ ⇌ 2H₂O, R = 4.7 kΩ, ⌀ 200 mm     ⎩⎣⎝i=1    ⎠⎦⎭

Linguistics and dictionaries:

  ði ıntəˈnæʃənəl fəˈnɛtık əsoʊsiˈeıʃn
  Y [ˈʏpsilɔn], Yen [jɛn], Yoga [ˈjoːgɑ]

APL:

  ((V⍳V)=⍳⍴V)/V←,V    ⌷←⍳→⍴∆∇⊃‾⍎⍕⌈

Nicer typography in plain text files:

  ╔══════════════════════════════════════════╗
  ║                                          ║
  ║   • ‘single’ and “double” quotes         ║
  ║                                          ║
  ║   • Curly apostrophes: “We’ve been here” ║
  ║                                          ║
  ║   • Latin-1 apostrophe and accents: '´`  ║
  ║                                          ║
  ║   • ‚deutsche‘ „Anführungszeichen“       ║
  ║                                          ║
  ║   • †, ‡, ‰, •, 3–4, —, −5/+5, ™, …      ║
  ║                                          ║
  ║   • ASCII safety test: 1lI|, 0OD, 8B     ║
  ║                      ╭─────────╮         ║
  ║   • the euro symbol: │ 14.95 € │         ║
  ║                      ╰─────────╯         ║
  ╚══════════════════════════════════════════╝

Combining characters:

  STARGΛ̊TE SG-1, a = v̇ = r̈, a⃑ ⊥ b⃑

Greek (in Polytonic):

  The Greek anthem:

  Σὲ γνωρίζω ἀπὸ τὴν κόψη
  τοῦ σπαθιοῦ τὴν τρομερή,
  σὲ γνωρίζω ἀπὸ τὴν ὄψη
  ποὺ μὲ βία μετράει τὴ γῆ.

  ᾿Απ᾿ τὰ κόκκαλα βγαλμένη
  τῶν ῾Ελλήνων τὰ ἱερά
  καὶ σὰν πρῶτα ἀνδρειωμένη
  χαῖρε, ὦ χαῖρε, ᾿Ελευθεριά!

  From a speech of Demosthenes in the 4th century BC:

  Οὐχὶ ταὐτὰ παρίσταταί μοι γιγνώσκειν, ὦ ἄνδρες ᾿Αθηναῖοι,
  ὅταν τ᾿ εἰς τὰ πράγματα ἀποβλέψω καὶ ὅταν πρὸς τοὺς
  λόγους οὓς ἀκούω· τοὺς μὲν γὰρ λόγους περὶ τοῦ
  τιμωρήσασθαι Φίλιππον ὁρῶ γιγνομένους, τὰ δὲ πράγματ᾿
  εἰς τοῦτο προήκοντα,  ὥσθ᾿ ὅπως μὴ πεισόμεθ᾿ αὐτοὶ
  πρότερον κακῶς σκέψασθαι δέον. οὐδέν οὖν ἄλλο μοι δοκοῦσιν
  οἱ τὰ τοιαῦτα λέγοντες ἢ τὴν ὑπόθεσιν, περὶ ἧς βουλεύεσθαι,
  οὐχὶ τὴν οὖσαν παριστάντες ὑμῖν ἁμαρτάνειν. ἐγὼ δέ, ὅτι μέν
  ποτ᾿ ἐξῆν τῇ πόλει καὶ τὰ αὑτῆς ἔχειν ἀσφαλῶς καὶ Φίλιππον
  τιμωρήσασθαι, καὶ μάλ᾿ ἀκριβῶς οἶδα· ἐπ᾿ ἐμοῦ γάρ, οὐ πάλαι
  γέγονεν ταῦτ᾿ ἀμφότερα· νῦν μέντοι πέπεισμαι τοῦθ᾿ ἱκανὸν
  προλαβεῖν ἡμῖν εἶναι τὴν πρώτην, ὅπως τοὺς συμμάχους
  σώσομεν. ἐὰν γὰρ τοῦτο βεβαίως ὑπάρξῃ, τότε καὶ περὶ τοῦ
  τίνα τιμωρήσεταί τις καὶ ὃν τρόπον ἐξέσται σκοπεῖν· πρὶν δὲ
  τὴν ἀρχὴν ὀρθῶς ὑποθέσθαι, μάταιον ἡγοῦμαι περὶ τῆς
  τελευτῆς ὁντινοῦν ποιεῖσθαι λόγον.

  Δημοσθένους, Γ´ ᾿Ολυνθιακὸς

Georgian:

  From a Unicode conference invitation:

  გთხოვთ ახლავე გაიაროთ რეგისტრაცია Unicode-ის მეათე საერთაშორისო
  კონფერენციაზე დასასწრებად, რომელიც გაიმართება 10-12 მარტს,
  ქ. მაინცში, გერმანიაში. კონფერენცია შეჰკრებს ერთად მსოფლიოს
  ექსპერტებს ისეთ დარგებში როგორიცაა ინტერნეტი და Unicode-ი,
  ინტერნაციონალიზაცია და ლოკალიზაცია, Unicode-ის გამოყენება
  ოპერაციულ სისტემებსა, და გამოყენებით პროგრამებში, შრიფტებში,
  ტექსტების დამუშავებასა და მრავალენოვან კომპიუტერულ სისტემებში.

Russian:

  From a Unicode conference invitation:

  Зарегистрируйтесь сейчас на Десятую Международную Конференцию по
  Unicode, которая состоится 10-12 марта 1997 года в Майнце в Германии.
  Конференция соберет широкий круг экспертов по  вопросам глобального
  Интернета и Unicode, локализации и интернационализации, воплощению и
  применению Unicode в различных операционных системах и программных
  приложениях, шрифтах, верстке и многоязычных компьютерных системах.

Thai (UCS Level 2):

  Excerpt from a poetry on The Romance of The Three Kingdoms (a Chinese
  classic 'San Gua'):

  [----------------------------|------------------------]
    ๏ แผ่นดินฮั่นเสื่อมโทรมแสนสังเวช  พระปกเกศกองบู๊กู้ขึ้นใหม่
  สิบสองกษัตริย์ก่อนหน้าแลถัดไป       สององค์ไซร้โง่เขลาเบาปัญญา
    ทรงนับถือขันทีเป็นที่พึ่ง           บ้านเมืองจึงวิปริตเป็นนักหนา
  โฮจิ๋นเรียกทัพทั่วหัวเมืองมา         หมายจะฆ่ามดชั่วตัวสำคัญ
    เหมือนขับไสไล่เสือจากเคหา      รับหมาป่าเข้ามาเลยอาสัญ
  ฝ่ายอ้องอุ้นยุแยกให้แตกกัน          ใช้สาวนั้นเป็นชนวนชื่นชวนใจ
    พลันลิฉุยกุยกีกลับก่อเหตุ          ช่างอาเพศจริงหนาฟ้าร้องไห้
  ต้องรบราฆ่าฟันจนบรรลัย           ฤๅหาใครค้ำชูกู้บรรลังก์ ฯ

  (The above is a two-column text. If combining characters are handled
  correctly, the lines of the second column should be aligned with the
  | character above.)

Ethiopian:

  Proverbs in the Amharic language:

  ሰማይ አይታረስ ንጉሥ አይከሰስ።
  ብላ ካለኝ እንደአባቴ በቆመጠኝ።
  ጌጥ ያለቤቱ ቁምጥና ነው።
  ደሀ በሕልሙ ቅቤ ባይጠጣ ንጣት በገደለው።
  የአፍ ወለምታ በቅቤ አይታሽም።
  አይጥ በበላ ዳዋ ተመታ።
  ሲተረጉሙ ይደረግሙ።
  ቀስ በቀስ፥ ዕንቁላል በእግሩ ይሄዳል።
  ድር ቢያብር አንበሳ ያስር።
  ሰው እንደቤቱ እንጅ እንደ ጉረቤቱ አይተዳደርም።
  እግዜር የከፈተውን ጉሮሮ ሳይዘጋው አይድርም።
  የጎረቤት ሌባ፥ ቢያዩት ይስቅ ባያዩት ያጠልቅ።
  ሥራ ከመፍታት ልጄን ላፋታት።
  ዓባይ ማደሪያ የለው፥ ግንድ ይዞ ይዞራል።
  የእስላም አገሩ መካ የአሞራ አገሩ ዋርካ።
  ተንጋሎ ቢተፉ ተመልሶ ባፉ።
  ወዳጅህ ማር ቢሆን ጨርስህ አትላሰው።
  እግርህን በፍራሽህ ልክ ዘርጋ።

Runes:

  ᚻᛖ ᚳᚹᚫᚦ ᚦᚫᛏ ᚻᛖ ᛒᚢᛞᛖ ᚩᚾ ᚦᚫᛗ ᛚᚪᚾᛞᛖ ᚾᚩᚱᚦᚹᛖᚪᚱᛞᚢᛗ ᚹᛁᚦ ᚦᚪ ᚹᛖᛥᚫ

  (Old English, which transcribed into Latin reads 'He cwaeth that he
  bude thaem lande northweardum with tha Westsae.' and means 'He said
  that he lived in the northern land near the Western Sea.')

Braille:

  ⡌⠁⠧⠑ ⠼⠁⠒  ⡍⠜⠇⠑⠹⠰⠎ ⡣⠕⠌

  ⡍⠜⠇⠑⠹ ⠺⠁⠎ ⠙⠑⠁⠙⠒ ⠞⠕ ⠃⠑⠛⠔ ⠺⠊⠹⠲ ⡹⠻⠑ ⠊⠎ ⠝⠕ ⠙⠳⠃⠞
  ⠱⠁⠞⠑⠧⠻ ⠁⠃⠳⠞ ⠹⠁⠞⠲ ⡹⠑ ⠗⠑⠛⠊⠌⠻ ⠕⠋ ⠙⠊⠎ ⠃⠥⠗⠊⠁⠇ ⠺⠁⠎
  ⠎⠊⠛⠝⠫ ⠃⠹ ⠹⠑ ⠊⠇⠻⠛⠹⠍⠁⠝⠂ ⠹⠑ ⠊⠇⠻⠅⠂ ⠹⠑ ⠥⠝⠙⠻⠞⠁⠅⠻⠂
  ⠁⠝⠙ ⠹⠑ ⠡⠊⠑⠋ ⠍⠳⠗⠝⠻⠲ ⡎⠊⠗⠕⠕⠛⠑ ⠎⠊⠛⠝⠫ ⠊⠞⠲ ⡁⠝⠙
  ⡎⠊⠗⠕⠕⠛⠑⠰⠎ ⠝⠁⠍⠑ ⠺⠁⠎ ⠛⠕⠕⠙ ⠥⠏⠕⠝ ⠰⡡⠁⠝⠛⠑⠂ ⠋⠕⠗ ⠁⠝⠹⠹⠔⠛ ⠙⠑
  ⠡⠕⠎⠑ ⠞⠕ ⠏⠥⠞ ⠙⠊⠎ ⠙⠁⠝⠙ ⠞⠕⠲

  ⡕⠇⠙ ⡍⠜⠇⠑⠹ ⠺⠁⠎ ⠁⠎ ⠙⠑⠁⠙ ⠁⠎ ⠁ ⠙⠕⠕⠗⠤⠝⠁⠊⠇⠲

  ⡍⠔⠙⠖ ⡊ ⠙⠕⠝⠰⠞ ⠍⠑⠁⠝ ⠞⠕ ⠎⠁⠹ ⠹⠁⠞ ⡊ ⠅⠝⠪⠂ ⠕⠋ ⠍⠹
  ⠪⠝ ⠅⠝⠪⠇⠫⠛⠑⠂ ⠱⠁⠞ ⠹⠻⠑ ⠊⠎ ⠏⠜⠞⠊⠊⠥⠇⠜⠇⠹ ⠙⠑⠁⠙ ⠁⠃⠳⠞
  ⠁ ⠙⠕⠕⠗⠤⠝⠁⠊⠇⠲ ⡊ ⠍⠊⠣⠞ ⠙⠁⠧⠑ ⠃⠑⠲ ⠔⠊⠇⠔⠫⠂ ⠍⠹⠎⠑⠇⠋⠂ ⠞⠕
  ⠗⠑⠛⠜⠙ ⠁ ⠊⠕⠋⠋⠔⠤⠝⠁⠊⠇ ⠁⠎ ⠹⠑ ⠙⠑⠁⠙⠑⠌ ⠏⠊⠑⠊⠑ ⠕⠋ ⠊⠗⠕⠝⠍⠕⠝⠛⠻⠹
  ⠔ ⠹⠑ ⠞⠗⠁⠙⠑⠲ ⡃⠥⠞ ⠹⠑ ⠺⠊⠎⠙⠕⠍ ⠕⠋ ⠳⠗ ⠁⠝⠊⠑⠌⠕⠗⠎
  ⠊⠎ ⠔ ⠹⠑ ⠎⠊⠍⠊⠇⠑⠆ ⠁⠝⠙ ⠍⠹ ⠥⠝⠙⠁⠇⠇⠪⠫ ⠙⠁⠝⠙⠎
  ⠩⠁⠇⠇ ⠝⠕⠞ ⠙⠊⠌⠥⠗⠃ ⠊⠞⠂ ⠕⠗ ⠹⠑ ⡊⠳⠝⠞⠗⠹⠰⠎ ⠙⠕⠝⠑ ⠋⠕⠗⠲ ⡹⠳
  ⠺⠊⠇⠇ ⠹⠻⠑⠋⠕⠗⠑ ⠏⠻⠍⠊⠞ ⠍⠑ ⠞⠕ ⠗⠑⠏⠑⠁⠞⠂ ⠑⠍⠏⠙⠁⠞⠊⠊⠁⠇⠇⠹⠂ ⠹⠁⠞
  ⡍⠜⠇⠑⠹ ⠺⠁⠎ ⠁⠎ ⠙⠑⠁⠙ ⠁⠎ ⠁ ⠙⠕⠕⠗⠤⠝⠁⠊⠇⠲

  (The first couple of paragraphs of "A Christmas Carol" by Dickens)

Compact font selection example text:

  ABCDEFGHIJKLMNOPQRSTUVWXYZ /0123456789
  abcdefghijklmnopqrstuvwxyz £©µÀÆÖÞßéöÿ
  –—‘“”„†•…‰™œŠŸž€ ΑΒΓΔΩαβγδω АБВГДабвгд
  ∀∂∈ℝ∧∪≡∞ ↑↗↨↻⇣ ┐┼╔╘░►☺♀ ﬁ�⑀₂ἠḂӥẄɐː⍎אԱა

Greetings in various languages:

  Hello world, Καλημέρα κόσμε, コンニチハ

Box drawing alignment tests:                                          █
                                                                      ▉
  ╔══╦══╗  ┌──┬──┐  ╭──┬──╮  ╭──┬──╮  ┏━━┳━━┓  ┎┒┏┑   ╷  ╻ ┏┯┓ ┌┰┐    ▊ ╱╲╱╲╳╳╳
  ║┌─╨─┐║  │╔═╧═╗│  │╒═╪═╕│  │╓─╁─╖│  ┃┌─╂─┐┃  ┗╃╄┙  ╶┼╴╺╋╸┠┼┨ ┝╋┥    ▋ ╲╱╲╱╳╳╳
  ║│╲ ╱│║  │║   ║│  ││ │ ││  │║ ┃ ║│  ┃│ ╿ │┃  ┍╅╆┓   ╵  ╹ ┗┷┛ └┸┘    ▌ ╱╲╱╲╳╳╳
  ╠╡ ╳ ╞╣  ├╢   ╟┤  ├┼─┼─┼┤  ├╫─╂─╫┤  ┣┿╾┼╼┿┫  ┕┛┖┚     ┌┄┄┐ ╎ ┏┅┅┓ ┋ ▍ ╲╱╲╱╳╳╳
  ║│╱ ╲│║  │║   ║│  ││ │ ││  │║ ┃ ║│  ┃│ ╽ │┃  ░░▒▒▓▓██ ┊  ┆ ╎ ╏  ┇ ┋ ▎
  ║└─╥─┘║  │╚═╤═╝│  │╘═╪═╛│  │╙─╀─╜│  ┃└─╂─┘┃  ░░▒▒▓▓██ ┊  ┆ ╎ ╏  ┇ ┋ ▏
  ╚══╩══╝  └──┴──┘  ╰──┴──╯  ╰──┴──╯  ┗━━┻━━┛  ▗▄▖▛▀▜   └╌╌┘ ╎ ┗╍╍┛ ┋  ▁▂▃▄▅▆▇█
                                               ▝▀▘▙▄▟

</pre>
```

## File: `httpbin/templates/flasgger/index.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"
        rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="{{url_for('flasgger.static', filename='swagger-ui.css')}}">
    <link rel="icon" type="image/png" href="{{url_for('static', filename='favicon.ico')}}" sizes="64x64 32x32 16x16" />
    <style>
        html {
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }

        *,
        *:before,
        *:after {
            box-sizing: inherit;
        }

        body {
            margin: 0;
            background: #fafafa;
        }
    </style>
</head>

<body>
    <a href="https://github.com/requests/httpbin" class="github-corner" aria-label="View source on Github">
        <svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;"
            aria-hidden="true">
            <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
            <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"
                fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
            <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"
                fill="currentColor" class="octo-body"></path>
        </svg>
    </a>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="position:absolute;width:0;height:0">
        <defs>
            <symbol viewBox="0 0 20 20" id="unlocked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V6h2v-.801C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8z"></path>
            </symbol>

            <symbol viewBox="0 0 20 20" id="locked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8zM12 8H8V5.199C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="close">
                <path d="M14.348 14.849c-.469.469-1.229.469-1.697 0L10 11.819l-2.651 3.029c-.469.469-1.229.469-1.697 0-.469-.469-.469-1.229 0-1.697l2.758-3.15-2.759-3.152c-.469-.469-.469-1.228 0-1.697.469-.469 1.228-.469 1.697 0L10 8.183l2.651-3.031c.469-.469 1.228-.469 1.697 0 .469.469.469 1.229 0 1.697l-2.758 3.152 2.758 3.15c.469.469.469 1.229 0 1.698z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow">
                <path d="M13.25 10L6.109 2.58c-.268-.27-.268-.707 0-.979.268-.27.701-.27.969 0l7.83 7.908c.268.271.268.709 0 .979l-7.83 7.908c-.268.271-.701.27-.969 0-.268-.269-.268-.707 0-.979L13.25 10z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow-down">
                <path d="M17.418 6.109c.272-.268.709-.268.979 0s.271.701 0 .969l-7.908 7.83c-.27.268-.707.268-.979 0l-7.908-7.83c-.27-.268-.27-.701 0-.969.271-.268.709-.268.979 0L10 13.25l7.418-7.141z"
                />
            </symbol>


            <symbol viewBox="0 0 24 24" id="jump-to">
                <path d="M19 7v4H5.83l3.58-3.59L8 6l-6 6 6 6 1.41-1.41L5.83 13H21V7z" />
            </symbol>

            <symbol viewBox="0 0 24 24" id="expand">
                <path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z" />
            </symbol>

        </defs>
    </svg>


    <div id="swagger-ui">
        <div data-reactroot="" class="swagger-ui">
            <div>
                <div class="information-container wrapper">
                    <section class="block col-12">
                        <div class="info">
                            <hgroup class="main">
                                <h2 class="title">httpbin.org
                                    <small>
                                        <pre class="version">0.9.2</pre>
                                    </small>
                                </h2>
                                <pre class="base-url">[ Base URL: httpbin.org/ ]</pre>
                            </hgroup>
                            <div class="description">
                                <div class="markdown">
                                    <p>A simple HTTP Request &amp; Response Service.
                                        <br>
                                        <br>
                                        <b>Run locally: </b>
                                        <code>$ docker run -p 80:80 kennethreitz/httpbin</code>
                                    </p>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <a href="https://kennethreitz.org" target="_blank">the developer - Website</a>
                                </div>
                                <a href="mailto:me@kennethreitz.org">Send email to the developer</a>
                            </div>
                        </div>
                        <!-- ADDS THE LOADER SPINNER -->
                        <div class="loading-container">
                            <div class="loading"></div>
                        </div>

                    </section>
                </div>
            </div>
        </div>
    </div>


    <div class='swagger-ui'>
        <div class="wrapper">
            <section class="clear">
                <span style="float: right;">
                    [Powered by
                    <a target="_blank" href="https://github.com/rochacbruno/flasgger">Flasgger</a>]
                    <br>
                </span>
            </section>
        </div>
    </div>



    <script src="{{url_for('flasgger.static', filename='swagger-ui-bundle.js')}}"> </script>
    <script src="{{url_for('flasgger.static', filename='swagger-ui-standalone-preset.js')}}"> </script>
    <script src='{{url_for('flasgger.static', filename='')}}lib/jquery.min.js' type='text/javascript'></script>
    <script>

        window.onload = function () {
            {% if config.JWT_AUTH_URL_RULE %}
            // JWT token holder
            var jwt_token;
            {% endif %}

            fetch("{{ specs[0]['url'] }}")
                .then(function (response) {
                    response.json()
                        .then(function (json) {
                            var current_protocol = window.location.protocol.slice(0, -1);
                            if (json.schemes[0] != current_protocol) {
                                // Switches scheme to the current in use
                                var other_protocol = json.schemes[0];
                                json.schemes[0] = current_protocol;
                                json.schemes[1] = other_protocol;

                            }
                            json.host = window.location.host;  // sets the current host

                            const ui = SwaggerUIBundle({
                                spec: json,
                                validatorUrl: null,
                                dom_id: '#swagger-ui',
                                deepLinking: true,
                                jsonEditor: true,
                                docExpansion: "none",
                                apisSorter: "alpha",
                                //operationsSorter: "alpha",
                                presets: [
                                    SwaggerUIBundle.presets.apis,
                                    // yay ES6 modules ↘
                                    Array.isArray(SwaggerUIStandalonePreset) ? SwaggerUIStandalonePreset : SwaggerUIStandalonePreset.default
                                ],
                                plugins: [
                                    SwaggerUIBundle.plugins.DownloadUrl
                                ],
            {% if config.JWT_AUTH_URL_RULE %}
            requestInterceptor: function (request) {
                                if (jwt_token) {
                                    request.headers.Authorization = "Bearer " + jwt_token;
                                }

                                return request;
                            },
                            responseInterceptor: function (response) {
                                var tokenField = 'jwt-token';
                                var headers = response.headers;

                                if (headers.hasOwnProperty(tokenField)) {
                                    jwt_token = headers[tokenField];
                                }

                                return response;
                            },
            {% endif %}
            // layout: "StandaloneLayout"  // uncomment to enable the green top header
        })

        window.ui = ui

        // uncomment to rename the top brand if layout is enabled
        // $(".topbar-wrapper .link span").replaceWith("<span>httpbin</span>");
        })
    })
}
    </script> {% if tracking_enabled %} {% include 'trackingscripts.html' %} {% endif %} {% include 'footer.html' %}
</body>

</html>
```

