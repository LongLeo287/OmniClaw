---
id: order
type: knowledge
owner: OA_Triage
---
# order
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "dependencies": {
    "google-closure-compiler": "^20210505.0.0",
    "md5": "^2.3.0",
    "sqlite": "^4.0.22",
    "sqlite3": "^5.0.2",
    "sqlite3-promisify": "^1.0.2"
  }
}

```

### File: README.md
```md
# Idris Full Stack DDD NodeJS example

## Order Taking Service

Idris version of Domain Modeling Made Functional Book.

 The [Domain Modeling Made Functional by Scott Wlaschin](https://www.amazon.co.uk/Domain-Modeling-Made-Functional-Domain-Driven/dp/1680502549)
introduces domain driven design and shows how well it fits to the world of functional programming via the lens of
the F# programming language. As Scott showed us that DDD is indeed a nice fit for functional programming,
questions arise naturally; could we push further the abstractions if we use a dependently typed programming language, like Idris?
Where are the sweet spots of depedent types in the world of everyday programming?
 Everyday programming needs to be focused on delivery, maintanability, reliability, and being correct.
The sad truth is that many applications needs to be more maintanable than correct.
Being correct is not a clear concept because its meaning changes as the software evolves.
In many cases, stakeholders only get a deeper understanding of the domain as the software solution/product evolves over time.
In this setting, depedent typed programming helps us achieve maintanability rather than being correct.
 In this repository I show a simple layered architecture and I show how to use simple dependent types
to draw explicit connections between the high level design of a service and its NodeJS deployed implementation.
Ideas and practices originated, but reshuffled from the [Type Driven Development with Idris by Edwin Brady](https://www.amazon.co.uk/Type-driven-Development-Idris-Edwin-Brady/dp/1617293024)
and the [Domain Modeling Made Functional by Scott Wlaschin](https://www.amazon.co.uk/Domain-Modeling-Made-Functional-Domain-Driven/dp/1680502549).
This architecture includes; An abstraction to talk about Bounded Context and Workflow, type safe description of a state transition system,
a free monad approach for domain implementation, and an actual implementation of the domain on NodeJS back-end.
 Because of dependent types, this architecture becomes explicit, rather than implicit, meaning that
connections between the high level design and the low level implementation are done via functions, changing
the code anywhere requires to think at the whole, as possible type errors propagates to top or to bottom.
 Idris could immensely benefit from simple FFIs for NodeJS libraries. The FFIs would grant access to thousands
of libraries from the NodeJS ecosystem almost for free. This approach would position Idris to be used even
in production settings and the Idris userbase could be bootstrapped, later the Idris version of these
libraries could be written.

Request: Please consider buying both of the books mentioned above. Boths are excellent resources for
further studying of the applied subject.

## Work In Progress parts:

- The documentation is still under development. Please come back regurarly to see what changed.
- Client needs lots of improvements.
- Better error Handling around workflow runners.
- Dependently driven testing needs to be implemented.

## Financial Support

<a href="https://www.patreon.com/AndOrP">
<img src="https://c5.patreon.com/external/logo/become_a_patron_button.png" width="150"/>
</a>

## Talk

<a href="https://youtu.be/QBj-4K-l-sg">Youtube</a>

## Notes

This project meant to be a blue-print, example for micro-services written in Idris. Its main focus is to reproduce
abstractions in dependently typed setting, that can be found in Scott Wlashin's book. The main focus is
around the dependently typed implementation of `BoundedContext`, but several other parts of the architecture
had to be worked on to be able to demostrate that Idris can host such solutions. Although during the implementation
many other problems were required to think about in the dependently typed setting. This repository can be
considered as a mine practices for dependently typed software development. Enjoy digging up those gems.

You may find the style of the explanations strange, maybe a bit chaotic, but if you follow path suggested
in the [READMAP.md](https://github.com/andorp/order-taking/blob/main/READMAP.md) you will learn many things about the Idris language. This style feels chaotic that could
be because I have a slight ADHD and I try to linarize the content here, but sometimes quickly the explanations
go deep. Although I believe a short explanation after every Idris snippet helps to view this reposity as
a hand-book for Idris development.

## High level overview

This repository contains more than just the `Idris` one to one translation of the `F#` code from the
Domain Modeling Made Functional book. I wanted to show how Idris can be used to interface with existing
`NodeJS` libraries. For that reason I added the following parts:

- FFI for NodeJS interfacing libraries
- Sketch of type-safe SQL library
- Minimal scaffolding of a NodeJS server
- Dependently typed framework for Bound-Context and Workflows
- State transition of the PlaceOrder example
- Free monadic DSL formalization of the PlaceOrder example
- One backend implementation of the operations of PlaceOrder DSL

See the [slides](https://github.com/andorp/order-taking/blob/main/SLIDES.md)

## Run

After setted up; start the microservice with `make start-opt`, start the client service `npm run dev`,
and open `localhost:5000` in a browser.

## Setup

### Server

 * Install Idris2 which version must match the one marketd the [VERSIONS](https://github.com/andorp/order-taking/blob/main/VERSIONS) file. OR
 * If you Idris2 release version installed, check out the corresponding tag from 0.4.0

For dependencies install `nodejs`, `npm` and packages:

```
npm install google-closure-compiler
npm install sqlite
npm install md5
```

To start the OrderTaking service, which will create the initial Sqlite DB and starts
the service on `127.0.0.1:3000`

```
make init-db
make start-opt
```

### Client

An example client can be found in the `client/svelte-client` directory. Follow the instructions
from its README.md

To run the client, call the following command:

```
cd client/svelte-client
npm run dev
```

Which starts the client in development mode, any changes in its code, will be picked up.

Important note, use the `g21` as product code on the client side for testing. The client
is very in pre-alpha state, best to open the developer console to see, what happens before and
after submitting the order. I will work on these details soon.

Have fun!

## ASCII ART

[ASCII ART](https://dot-to-ascii.ggerganov.com/)

```

### File: package-lock.json
```json
{
  "name": "order-taking",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "dependencies": {
        "google-closure-compiler": "^20210505.0.0",
        "md5": "^2.3.0",
        "sqlite": "^4.0.22",
        "sqlite3": "^5.0.2",
        "sqlite3-promisify": "^1.0.2"
      }
    },
    "node_modules/abbrev": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz",
      "integrity": "sha512-nne9/IiQ/hzIhY6pdDnbBtz7DjPTKrY00P/zvPSm5pOFkl6xuGrGnXn/VtTNNfNtAfZ9/1RtehkszU9qcTii0Q=="
    },
    "node_modules/ajv": {
      "version": "6.12.6",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz",
      "integrity": "sha512-j3fVLgvTo527anyYyJOGTYJbG+vnnQYvE0m5mmkc1TK+nxAppkCLMIL0aZ4dblVCNoGShhm+kzE4ZUykBoMg4g==",
      "optional": true,
      "dependencies": {
        "fast-deep-equal": "^3.1.1",
        "fast-json-stable-stringify": "^2.0.0",
        "json-schema-traverse": "^0.4.1",
        "uri-js": "^4.2.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/ansi-regex": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz",
      "integrity": "sha1-w7M6te42DYbg5ijwRorn7yfWVN8=",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/ansi-styles": {
      "version": "3.2.1",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz",
      "integrity": "sha512-VT0ZI6kZRdTh8YyJw3SMbYm/u+NqfsAxEpWO0Pf9sq8/e94WxxOpPKx9FR1FlyCtOVDNOQ+8ntlqFxiRc+r5qA==",
      "dependencies": {
        "color-convert": "^1.9.0"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/aproba": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz",
      "integrity": "sha512-Y9J6ZjXtoYh8RnXVCMOU/ttDmk1aBjunq9vO0ta5x85WDQiQfUF9sIPBITdbiiIVcBo03Hi3jMxigBtsddlXRw=="
    },
    "node_modules/are-we-there-yet": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.5.tgz",
      "integrity": "sha512-5hYdAkZlcG8tOLujVDTgCT+uPX0VnpAH28gWsLfzpXYm7wP6mp5Q/gYyR7YQ0cKVJcXJnl3j2kpBan13PtQf6w==",
      "dependencies": {
        "delegates": "^1.0.0",
        "readable-stream": "^2.0.6"
      }
    },
    "node_modules/asn1": {
      "version": "0.2.4",
      "resolved": "https://registry.npmjs.org/asn1/-/asn1-0.2.4.tgz",
      "integrity": "sha512-jxwzQpLQjSmWXgwaCZE9Nz+glAG01yF1QnWgbhGwHI5A6FRIEY6IVqtHhIepHqI7/kyEyQEagBC5mBEFlIYvdg==",
      "optional": true,
      "dependencies": {
        "safer-buffer": "~2.1.0"
      }
    },
    "node_modules/assert-plus": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz",
      "integrity": "sha1-8S4PPF13sLHN2RRpQuTpbB5N1SU=",
      "optional": true,
      "engines": {
        "node": ">=0.8"
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha1-x57Zf380y48robyXkLzDZkdLS3k=",
      "optional": true
    },
    "node_modules/aws-sign2": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz",
      "integrity": "sha1-tG6JCTSpWR8tL2+G1+ap8bP+dqg=",
      "optional": true,
      "engines": {
        "node": "*"
      }
    },
    "node_modules/aws4": {
      "version": "1.11.0",
      "resolved": "https://registry.npmjs.org/aws4/-/aws4-1.11.0.tgz",
      "integrity": "sha512-xh1Rl34h6Fi1DC2WWKfxUTVqRsNnr6LsKz2+hfwDxQJWmrx8+c7ylaqBMcHfl1U1r2dsifOvKX3LQuLNZ+XSvA==",
      "optional": true
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw=="
    },
    "node_modules/bcrypt-pbkdf": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz",
      "integrity": "sha1-pDAdOJtqQ/m2f/PKEaP2Y342Dp4=",
      "optional": true,
      "dependencies": {
        "tweetnacl": "^0.14.3"
      }
    },
    "node_modules/block-stream": {
      "version": "0.0.9",
      "resolved": "https://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz",
      "integrity": "sha1-E+v+d4oDIFz+A3UUgeu0szAMEmo=",
      "optional": true,
      "dependencies": {
        "inherits": "~2.0.0"
      },
      "engines": {
        "node": "0.4 || >=0.5.8"
      }
    },
    "node_modules/brace-expansion": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz",
      "integrity": "sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==",
      "dependencies": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "node_modules/caseless": {
      "version": "0.12.0",
      "resolved": "https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz",
      "integrity": "sha1-G2gcIf+EAzyCZUMJBolCDRhxUdw=",
      "optional": true
    },
    "node_modules/chalk": {
      "version": "2.4.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz",
      "integrity": "sha512-Mti+f9lpJNcwF4tWV8/OrTTtF1gZi+f8FqlyAdouralcFWFQWF2+NgCHShjkCb+IFBLq9buZwE1xckQU4peSuQ==",
      "dependencies": {
        "ansi-styles": "^3.2.1",
        "escape-string-regexp": "^1.0.5",
        "supports-color": "^5.3.0"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/charenc": {
      "version": "0.0.2",
      "resolved": "https://registry.npmjs.org/charenc/-/charenc-0.0.2.tgz",
      "integrity": "sha1-wKHS86cJLgN3S/qD8UwPxXkKhmc=",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/chownr": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/chownr/-/chownr-1.1.4.tgz",
      "integrity": "sha512-jJ0bqzaylmJtVnNgzTeSOs8DPavpbYgEr/b0YL8/2GO3xJEhInFmhKMUnEJQjZumK7KXGFhUy89PrsJWlakBVg=="
    },
    "node_modules/clone": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/clone/-/clone-2.1.2.tgz",
      "integrity": "sha1-G39Ln1kfHo+DZwQBYANFoCiHQ18=",
      "engines": {
        "node": ">=0.8"
      }
    },
    "node_modules/clone-buffer": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/clone-buffer/-/clone-buffer-1.0.0.tgz",
      "integrity": "sha1-4+JbIHrE5wGvch4staFnksrD3Fg=",
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/clone-stats": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/clone-stats/-/clone-stats-1.0.0.tgz",
      "integrity": "sha1-s3gt/4u1R04Yuba/D9/ngvh3doA="
    },
    "node_modules/cloneable-readable": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/cloneable-readable/-/cloneable-readable-1.1.3.tgz",
      "integrity": "sha512-2EF8zTQOxYq70Y4XKtorQupqF0m49MBz2/yf5Bj+MHjvpG3Hy7sImifnqD6UA+TKYxeSV+u6qqQPawN5UvnpKQ==",
      "dependencies": {
        "inherits": "^2.0.1",
        "process-nextick-args": "^2.0.0",
        "readable-stream": "^2.3.5"
      }
    },
    "node_modules/code-point-at": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz",
      "integrity": "sha1-DQcLTQQ6W+ozovGkDi7bPZpMz3c=",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/color-convert": {
      "version": "1.9.3",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz",
      "integrity": "sha512-QfAUtd+vFdAtFQcC8CCyYt1fYWxSqAiK2cSD6zDB8N3cpsEBAvRxp9zOGg6G/SHHJYAT88/az/IuDGALsNVbGg==",
      "dependencies": {
        "color-name": "1.1.3"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz",
      "integrity": "sha1-p9BVi9icQveV3UIyj3QIMcpTvCU="
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "optional": true,
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha1-2Klr13/Wjfd5OnMDajug1UBdR3s="
    },
    "node_modules/console-control-strings": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz",
      "integrity": "sha1-PXz0Rk22RG6mRL9LOVB/mFEAjo4="
    },
    "node_modules/core-util-is": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz",
      "integrity": "sha1-tf1UIgqivFq1eqtxQMlAdUUDwac="
    },
    "node_modules/crypt": {
      "version": "0.0.2",
      "resolved": "https://registry.npmjs.org/crypt/-/crypt-0.0.2.tgz",
      "integrity": "sha1-iNf/fsDfuG9xPch7u0LQRNPmxBs=",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/dashdash": {
      "version": "1.14.1",
      "resolved": "https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz",
      "integrity": "sha1-hTz6D3y+L+1d4gMmuN1YEDX24vA=",
      "optional": true,
      "dependencies": {
        "assert-plus": "^1.0.0"
      },
      "engines": {
        "node": ">=0.10"
      }
    },
    "node_modules/debug": {
      "version": "3.2.7",
      "resolved": "https://registry.npmjs.org/debug/-/debug-3.2.7.tgz",
      "integrity": "sha512-CFjzYYAi4ThfiQvizrFQevTTXHtnCqWfe7x1AhgEscTz6ZbLbfoLRLPugTQyBth6f8ZERVUSyWHFD/7Wu4t1XQ==",
      "dependencies": {
        "ms": "^2.1.1"
      }
    },
    "node_modules/deep-extend": {
      "version": "0.6.0",
      "resolved": "https://registry.npmjs.org/deep-extend/-/deep-extend-0.6.0.tgz",
      "integrity": "sha512-LOHxIOaPYdHlJRtCQfDIVZtfw/ufM8+rVj649RIHzcm/vGwQRXFt6OPqIFWsm2XEMrNIEtWR64sY1LEKD2vAOA==",
      "engines": {
        "node": ">=4.0.0"
      }
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha1-3zrhmayt+31ECqrgsp4icrJOxhk=",
      "optional": true,
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/delegates": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz",
      "integrity": "sha1-hMbhWbgZBP3KWaDvRM2HDTElD5o="
    },
    "node_modules/detect-libc": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-1.0.3.tgz",
      "integrity": "sha1-+hN8S9aY7fVc1c0CrFWfkaTEups=",
      "bin": {
        "detect-libc": "bin/detect-libc.js"
      },
      "engines": {
        "node": ">=0.10"
      }
    },
    "node_modules/ecc-jsbn": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz",
      "integrity": "sha1-OoOpBOVDUyh4dMVkt1SThoSamMk=",
      "optional": true,
      "dependencies": {
        "jsbn": "~0.1.0",
        "safer-buffer": "^2.1.0"
      }
    },
    "node_modules/escape-string-regexp": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz",
      "integrity": "sha1-G2HAViGQqN/2rjuyzwIAyhMLhtQ=",
      "engines": {
        "node": ">=0.8.0"
      }
    },
    "node_modules/extend": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
      "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==",
      "optional": true
    },
    "node_modules/extsprintf": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz",
      "integrity": "sha1-lpGEQOMEGnpBT4xS48V06zw+HgU=",
      "engines": [
        "node >=0.6.0"
      ],
      "optional": true
    },
    "node_modules/fast-deep-equal": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
      "integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==",
      "optional": true
    },
    "node_modules/fast-json-stable-stringify": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz",
      "integrity": "sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==",
      "optional": true
    },
    "node_modules/forever-agent": {
      "version": "0.6.1",
      "resolved": "https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz",
      "integrity": "sha1-+8cfDEGt6zf5bFd60e1C2P2sypE=",
      "optional": true,
      "engines": {
        "node": "*"
      }
    },
    "node_modules/form-data": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz",
      "integrity": "sha512-1lLKB2Mu3aGP1Q/2eCOx0fNbRMe7XdwktwOruhfqqd0rIJWwN4Dh+E3hrPSlDCXnSR7UtZ1N38rVXm+6+MEhJQ==",
      "optional": true,
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.6",
        "mime-types": "^2.1.12"
      },
      "engines": {
        "node": ">= 0.12"
      }
    },
    "node_modules/fs-minipass": {
      "version": "1.2.7",
      "resolved": "https://registry.npmjs.org/fs-minipass/-/fs-minipass-1.2.7.tgz",
      "integrity": "sha512-GWSSJGFy4e9GUeCcbIkED+bgAoFyj7XF1mV8rma3QW4NIqX9Kyx79N/PF61H5udOV3aY1IaMLs6pGbH71nlCTA==",
      "dependencies": {
        "minipass": "^2.6.0"
      }
    },
    "node_modules/fs.realpath": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
      "integrity": "sha1-FQStJSMVjKpA20onh8sBQRmU6k8="
    },
    "node_modules/fstream": {
      "version": "1.0.12",
      "resolved": "https://registry.npmjs.org/fstream/-/fstream-1.0.12.tgz",
      "integrity": "sha512-WvJ193OHa0GHPEL+AycEJgxvBEwyfRkN1vhjca23OaPVMCaLCXTd5qAu82AjTcgP1UJmytkOKb63Ypde7raDIg==",
      "optional": true,
      "dependencies": {
        "graceful-fs": "^4.1.2",
        "inherits": "~2.0.0",
        "mkdirp": ">=0.5 0",
        "rimraf": "2"
      },
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/gauge": {
      "version": "2.7.4",
      "resolved": "https://registry.npmjs.org/gauge/-/gauge-
... [TRUNCATED]
```

### File: READMAP.md
```md
# Reader's map

Disclaimer: The documentation is still in the making...

You may want to read the documentation from the modules in this order if you want to learn
Idris via examples.

- [Data.Result](https://github.com/andorp/order-taking/blob/main/src/Data/Result.idr)
- [Data.Form](https://github.com/andorp/order-taking/blob/main/src/Data/Form.idr)
- [Data.Between](https://github.com/andorp/order-taking/blob/main/src/Data/Between.idr)
- [Data.StringN](https://github.com/andorp/order-taking/blob/main/src/Data/StringN.idr)
- [Language.JSON.Schema](https://github.com/andorp/order-taking/blob/main/src/Language/JSON/Schema.idr)
- [Rango.BoundedContext.Workflow](https://github.com/andorp/order-taking/blob/main/src/Rango/BoundedContext/Workflow.idr)
- [Rango.BoundedContext.BoundedContext](https://github.com/andorp/order-taking/blob/main/src/Rango/BoundedContext/BoundedContext.idr)
- [Service.NodeJS.Date](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/Date.idr)
- [Service.NodeJS.Random](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/Random.idr)
- [Service.NodeJS.MD5](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/MD5.idr)
- [Service.NodeJS.Promise](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/Promise.idr)
- ...

You may want to read the documentation from the modules in this order if you want to learn
about the DDD solution and its implementation in Idris.

- TODO

```

### File: SLIDES.md
```md
# Slides

## High level overview

### Idealized view of software projects

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎  Software Project         ╎
╎                           ╎
╎ ┌───────────────────┐     ╎
╎ │   Requirements    │─┐   ╎
╎ └───────────────────┘ │   ╎
╎   │                   │   ╎
╎   ▼                   │   ╎
╎ ┌───────────────────┐ │   ╎
╎ │ Quality Assurance │ │   ╎
╎ └───────────────────┘ │   ╎
╎   │                   │   ╎
╎   ▼                   │   ╎
╎ ┌───────────────────┐ │   ╎
╎ │  Implementation   │◀┘   ╎
╎ └───────────────────┘     ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Semantic tower of a tipical software project

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎         Semantic Tower         ╎
╎                                ╎
╎ ┌────────────────────────────┐ ╎
╎ │       Design diagram       │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │      Detailed design       │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │ Data / Behavior definition │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │       Implementation       │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │         Libraries          │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │      Tech environment      │ ╎
╎ └────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Realization of a software project

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎             Real Software Project             ╎
╎                                               ╎
╎ ┌───────────────────────────────────────────┐ ╎
╎ │       Requirement docs, JIRA items        │ ╎
╎ └───────────────────────────────────────────┘ ╎
╎ ┌───────────────────────────────────────────┐ ╎
╎ │      Implemented data and behaviour       │ ╎
╎ └───────────────────────────────────────────┘ ╎
╎ ┌───────────────────────────────────────────┐ ╎
╎ │ Some kind tests; manual, unit, end-to-end │ ╎
╎ └───────────────────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```


### Realization of a software project including the semantic tower

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎                Real Software Project               ╎
╎                                                    ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │            Requirement docs, JIRA items        │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Design Diagram      │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Detailed Design     │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │ Data / Behavior definition │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │         Implemented data and behaviour         │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Tech environment     │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │    Some kind tests; manual, unit, end-to-end   │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │      Tech environment      │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Change request of any kind

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎          Semantic Tower         ╎
╎                                 ╎
╎ ┌─────────────────────────────┐ ╎
╎ │        Design diagram       │ ╎ ◀─ Change should propagate down
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │       Detailed design       │ ╎
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │  Data / Behavior definition │ ╎ ◀─ Change should propagate up and down
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │        Implementation       │ ╎
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │          Libraries          │ ╎
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │       Tech environment      │ ╎ ◀─ Change could tear down all the project,
╎ └─────────────────────────────┘ ╎    but definetly could destroy everything up
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘    to the behavioral definition.
```

### Change request in realized software project

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎                Real Software Project               ╎
╎                                                    ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │            Requirement docs, JIRA items        │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Design Diagram      │         │ ╎ ◀─ Change here indicates ... what?
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Detailed Design     │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │ Data / Behavior definition │         │ ╎ ◀─ Change here indicates ... what?
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │         Implemented data and behaviour         │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Tech environment     │         │ ╎ ◀─ Change here indicates ... what?
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │    Some kind tests; manual, unit, end-to-end   │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │      Tech environment      │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Domain Driven Design

Focuses on the **Data / Behavioral definition**. DDD models the software a collection of
bounded contextes that interact with each other.

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎                    Bounded Context                    ╎
╎                                                       ╎
╎                   ┌───────────────┐                   ╎
╎   ┌────────────── │    Command    │ ──────┐           ╎
╎   │               └───────────────┘       │           ╎
╎   │                 │                     │           ╎
╎   │                 │                     │           ╎
╎   ▼                 ▼                     ▼           ╎
╎ ┌───────────┐     ┌───────────────┐     ┌───────────┐ ╎
╎ │ Workflow  │     │    Workflow   │     │ Workflow  │ ╎
╎ └───────────┘     └───────────────┘     └───────────┘ ╎
╎   │                 │                     │           ╎
╎   │                 │                     │           ╎
╎   │                 ▼                     │           ╎
╎   │               ┌───────────────┐       │           ╎
╎   └─────────────▶ │     Event     │ ◀─────┘           ╎
╎                   └───────────────┘                   ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Behaviour described in workflows

For example

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐                                    
╎                                    ┌────────────────────────────┐ ╎
╎                                    │         OrderForm          │ ╎
╎                                    └────────────────────────────┘ ╎
╎                                      │                            ╎
╎                                      │ Validate Order             ╎
╎                                      ▼                            ╎
╎ ┌─────────────┐    Create valid    ┌============================┐ ╎
╎ │ ValidOrder  │   ◀─────────────── I           Order            I ╎
╎ └─────────────┘                    └============================┘ ╎
╎   │                                  │                            ╎
╎   │ Price                            │ Create invalid             ╎
╎   ▼                                  ▼                            ╎
╎ ┌─────────────┐                    ┌────────────────────────────┐ ╎
╎ │ PricedOrder │                    │        InvalidOrder        │ ╎
╎ └─────────────┘                    └────────────────────────────┘ ╎
╎   │                                  │                            ╎
╎   │                                  │ Queue                      ╎
╎   │                                  ▼                            ╎
╎   │                                ┌────────────────────────────┐ ╎
╎   │                                |     InvalidOrderQueued     │ ╎
╎   │                                └────────────────────────────┘ ╎
╎   │                                  │                            ╎
╎   │                                  │ Create invalid order info  ╎
╎   │                                  ▼                            ╎
╎   │  Create priced order info      ┌────────────────────────────┐ ╎
╎   └────────────────────────────▶   │         OrderInfo          │ ╎
╎                                    └────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Information flow

In a service implementation information is processed via information flow
from Request to Response. In the Bounded Context of DDD this workflow
looks like this:

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎      Request/Response flow in bounded context           ╎
╎                                                         ╎
╎            ┌─────────────────────┐                      ╎
╎            │       Request       │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │        JSON         │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │    Command Data     │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │       Command       │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │   Workflow Input    │                      ╎
╎            └─────────────────────┘                      ╎
╎                ▼                                        ╎
╎ ┌────┐       ┌─────────────────────┐       ┌──────────┐ ╎
╎ │ DB │ ───── │ Workflow Internals  │ ───── │ Services │ ╎
╎ └────┘       └─────────────────────┘       └──────────┘ ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │   Workflow Output   │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │        Event        │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │     Event Data      │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │        JSON         │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │      Response       │                      ╎
╎            └─────────────────────┘                      ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘

```

### The missing link in the semantic tower

Layers may depend on each other. With dependent types we can express this connection.
If layer n of the semantic tower is a function of layer n-1 than any change in
one layer, will propagate through the semantic tower.

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎         Semantic Tower         ╎
╎                                ╎
╎ ┌────────────────────────────┐ ╎
╎ │       Design diagram       │ ╎
╎ └─────────────────────
... [TRUNCATED]
```

