---
id: node-isdoc-pdf
type: knowledge
owner: OA_Triage
---
# node-isdoc-pdf
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "isdoc-pdf",
  "version": "0.1.2",
  "description": "Create ISDOC.PDF (PDF/A-3 with ISDOC attachment), create ISDOCX (ZIP archive with PDF and ISDOC) or extract ISDOC from PDF - Czechia's standard invoice format for data exchange",
  "author": "ΔO - David Obdržálek <david@deltazero.cz>",
  "license": "ISC",
  "keywords": [
    "isdoc",
    "isdocx",
    "isdoc-pdf",
    "pdf",
    "pdfa",
    "pdf/a",
    "pdf/a-3"
  ],
  "main": "index.js",
  "types": "index.d.ts",
  "scripts": {
    "pretest": "tsc",
    "test": "mocha tests --timeout 10000",
    "build": "tsc -b",
    "prepare": "npm run build"
  },
  "repository": "deltazero-cz/node-isdoc",
  "engines": {
    "node": ">=14.0.0"
  },
  "dependencies": {
    "@deltazero/isdoc": "^0.1.2",
    "jszip": "^3.10.1",
    "pdf-lib": "^1.17.1",
    "xsd-validator": "^1.1.0",
    "isdoc-pdf-bash": "git+https://github.com/deltazero-cz/isdoc-pdf.git"
  },
  "devDependencies": {
    "@types/chai": "^4.3.3",
    "@types/mocha": "^9.1.1",
    "@types/node": "^16.0.0",
    "chai": "^4.3.6",
    "mocha": "^10.0.0",
    "typescript": "latest"
  }
}

```

### File: README.md
```md
# ISDOC-PDF Node.js library

[ISDOC](https://isdoc.github.io/) is an XML Invoicing Standard for the Czech Republic.

This library can:
- extract ISDOC invoices from PDFs
- create ISDOC.PDF (PDF/A-3B with ISDOC attached)
- create IDDOCX archives (zips with PDF and ISDOC)

It also provides Node.js API for ISDOC format, see [node-isdoc](https://github.com/deltazero-cz/node-isdoc),
incl. XSD xchema validation.

### Installation

```shell
npm i isdoc-pdf
```

To create ISDOC.PDF (PDF/A-3B with ISDOC attached),
this package depends on Bash-like shell and Ghostscript,
see [isdoc-pdf (bash)](https://github.com/deltazero-cz/isdoc-pdf).

### Usage

Extract ISDOC from existing PDF

```js
import { hasISDOC, extractISDOC } from 'isdoc-pdf'

const plainInvoice = await fs.readFile('invoice.pdf'),
      isdocInvoice = await fs.readFile('invoice.isdoc.pdf')

await hasISDOC(plainInvoice)
// -> false

await hasISDOC(isdocInvoice)
// -> true

await extractISDOC(plainInvoice)
// -> null 

await extractISDOC(isdocInvoice)
// -> Invoice { DocumentType: number, ID: string, IssueDate: Date, ... }
```

Create ISDOC.PDF (attach ISDOC to PDF and convert into PDF/A-3)

```js
import { attachISDOC } from 'isdoc-pdf'

const invoice = await fs.readFile('invoice.pdf'),
      isdoc = await fs.readFile('invoice.isdoc')

const pdfa = await attachISDOC(invoice, isdoc)
// -> Buffer with PDF/A-3
```

Create ISDOC.PDF with a new Invoice

```js
import { Invoice, attachISDOC } from 'isdoc-pdf'

const isdoc = new Invoice({
  DocumentType: 1,
  ID: '2022123456',
  ... // see https://github.com/deltazero-cz/node-isdoc
})

const pdf = await fs.readFile('invoice.pdf')

const pdfa = await attachISDOC(pdf, isdoc)
// -> Buffer with PDF/A-3
```

Create IDDOCX archives (ZIP archives with PDF and ISDOC)

```js
import { createISDOCX } from 'isdoc-pdf'

const invoice = await fs.readFile('invoice.pdf'),
      isdoc = await fs.readFile('invoice.isdoc')

const isdocx = await createISDOCX(invoice, invoice)
// -> Buffer with ISDOCX (ZIP archive)
```

Create IDDOCX with a new Invoice

```js
import { Invoice, createISDOCX } from 'isdoc-pdf'

const isdoc = new Invoice({
  DocumentType: 1,
  ID: '2022123456',
  ... // see https://github.com/deltazero-cz/node-isdoc
})

const pdf = await fs.readFile('invoice.pdf')

const isdocx = await createISDOCX(pdf, isdoc)
// -> Buffer with ISDOCX (ZIP archive)
```

```

### File: index.ts
```ts
import Invoice, { InvoiceType } from '@deltazero/isdoc'
import extractISDOC, { hasISDOC } from './lib/extractISDOC'
import createISDOCX from './lib/createISDOCX'
import attachISDOC from './lib/attachISDOC'

export { Invoice, InvoiceType, createISDOCX, attachISDOC, extractISDOC, hasISDOC }

```

### File: package-lock.json
```json
{
  "name": "isdoc-pdf",
  "version": "0.1.2",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "isdoc-pdf",
      "version": "0.1.2",
      "license": "ISC",
      "dependencies": {
        "@deltazero/isdoc": "^0.1.2",
        "isdoc-pdf-bash": "git+https://github.com/deltazero-cz/isdoc-pdf.git",
        "jszip": "^3.10.1",
        "pdf-lib": "^1.17.1",
        "xsd-validator": "^1.1.0"
      },
      "devDependencies": {
        "@types/chai": "^4.3.3",
        "@types/mocha": "^9.1.1",
        "@types/node": "^16.0.0",
        "chai": "^4.3.6",
        "mocha": "^10.0.0",
        "typescript": "latest"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@deltazero/isdoc": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/@deltazero/isdoc/-/isdoc-0.1.2.tgz",
      "integrity": "sha512-IUlSrkz2CqAhNZ36mm2B2VQriAwkMIHRqb/FUccXBeIUkkiC5rTtxBPKPWKa2vD73zMgSWN4jWubKpf8qjG98A==",
      "dependencies": {
        "fast-xml-parser": "^4.2.4",
        "xsd-validator": "^1.1.0"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@mapbox/node-pre-gyp": {
      "version": "1.0.10",
      "resolved": "https://registry.npmjs.org/@mapbox/node-pre-gyp/-/node-pre-gyp-1.0.10.tgz",
      "integrity": "sha512-4ySo4CjzStuprMwk35H5pPbkymjv1SF3jGLj6rAHp/xT/RF7TL7bd9CTm1xDY49K2qF7jmR/g7k+SkLETP6opA==",
      "dependencies": {
        "detect-libc": "^2.0.0",
        "https-proxy-agent": "^5.0.0",
        "make-dir": "^3.1.0",
        "node-fetch": "^2.6.7",
        "nopt": "^5.0.0",
        "npmlog": "^5.0.1",
        "rimraf": "^3.0.2",
        "semver": "^7.3.5",
        "tar": "^6.1.11"
      },
      "bin": {
        "node-pre-gyp": "bin/node-pre-gyp"
      }
    },
    "node_modules/@pdf-lib/standard-fonts": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/@pdf-lib/standard-fonts/-/standard-fonts-1.0.0.tgz",
      "integrity": "sha512-hU30BK9IUN/su0Mn9VdlVKsWBS6GyhVfqjwl1FjZN4TxP6cCw0jP2w7V3Hf5uX7M0AZJ16vey9yE0ny7Sa59ZA==",
      "dependencies": {
        "pako": "^1.0.6"
      }
    },
    "node_modules/@pdf-lib/upng": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/@pdf-lib/upng/-/upng-1.0.1.tgz",
      "integrity": "sha512-dQK2FUMQtowVP00mtIksrlZhdFXQZPC+taih1q4CvPZ5vqdxR/LKBaFg0oAfzd1GlHZXXSPdQfzQnt+ViGvEIQ==",
      "dependencies": {
        "pako": "^1.0.10"
      }
    },
    "node_modules/@types/chai": {
      "version": "4.3.4",
      "resolved": "https://registry.npmjs.org/@types/chai/-/chai-4.3.4.tgz",
      "integrity": "sha512-KnRanxnpfpjUTqTCXslZSEdLfXExwgNxYPdiO2WGUj8+HDjFi8R3k5RVKPeSCzLjCcshCAtVO2QBbVuAV4kTnw==",
      "dev": true
    },
    "node_modules/@types/mocha": {
      "version": "9.1.1",
      "resolved": "https://registry.npmjs.org/@types/mocha/-/mocha-9.1.1.tgz",
      "integrity": "sha512-Z61JK7DKDtdKTWwLeElSEBcWGRLY8g95ic5FoQqI9CMx0ns/Ghep3B4DfcEimiKMvtamNVULVNKEsiwV3aQmXw==",
      "dev": true
    },
    "node_modules/@types/node": {
      "version": "16.18.12",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-16.18.12.tgz",
      "integrity": "sha512-vzLe5NaNMjIE3mcddFVGlAXN1LEWueUsMsOJWaT6wWMJGyljHAWHznqfnKUQWGzu7TLPrGvWdNAsvQYW+C0xtw==",
      "dev": true
    },
    "node_modules/abbrev": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz",
      "integrity": "sha512-nne9/IiQ/hzIhY6pdDnbBtz7DjPTKrY00P/zvPSm5pOFkl6xuGrGnXn/VtTNNfNtAfZ9/1RtehkszU9qcTii0Q=="
    },
    "node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/ansi-colors": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/ansi-colors/-/ansi-colors-4.1.1.tgz",
      "integrity": "sha512-JoX0apGbHaUJBNl6yF+p6JAFYZ666/hhCGKN5t9QFjbJQKUU/g8MNbFDbvfrgKXvI1QpZplPOnwIo99lX/AAmA==",
      "dev": true,
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "dev": true,
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/anymatch": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
      "integrity": "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==",
      "dev": true,
      "dependencies": {
        "normalize-path": "^3.0.0",
        "picomatch": "^2.0.4"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/aproba": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/aproba/-/aproba-2.0.0.tgz",
      "integrity": "sha512-lYe4Gx7QT+MKGbDsA+Z+he/Wtef0BiwDOlK/XkBrdfsh9J/jPPXbX0tE9x9cl27Tmu5gg3QUbUrQYa/y+KOHPQ=="
    },
    "node_modules/are-we-there-yet": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-2.0.0.tgz",
      "integrity": "sha512-Ci/qENmwHnsYo9xKIcUJN5LeDKdJ6R1Z1j9V/J5wyq8nh/mYPEpIKJbBZXtZjG04HiK7zV/p6Vs9952MrMeUIw==",
      "dependencies": {
        "delegates": "^1.0.0",
        "readable-stream": "^3.6.0"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/are-we-there-yet/node_modules/readable-stream": {
      "version": "3.6.2",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz",
      "integrity": "sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==",
      "dependencies": {
        "inherits": "^2.0.3",
        "string_decoder": "^1.1.1",
        "util-deprecate": "^1.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/argparse": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz",
      "integrity": "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==",
      "dev": true
    },
    "node_modules/assertion-error": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/assertion-error/-/assertion-error-1.1.0.tgz",
      "integrity": "sha512-jgsaNduz+ndvGyFt3uSuWqvy4lCnIJiovtouQN5JZHOKCS2QuhEdbcQHFhVksz2N2U9hXJo8odG7ETyWlEeuDw==",
      "dev": true,
      "engines": {
        "node": "*"
      }
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw=="
    },
    "node_modules/binary-extensions": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.2.0.tgz",
      "integrity": "sha512-jDctJ/IVQbZoJykoeHbhXpOlNBqGNcwXJKJog42E5HDPUwQTSdjCHdihjj0DlnheQ7blbT6dHOafNAiS8ooQKA==",
      "dev": true,
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/bindings": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/bindings/-/bindings-1.3.1.tgz",
      "integrity": "sha512-i47mqjF9UbjxJhxGf+pZ6kSxrnI3wBLlnGI2ArWJ4r0VrvDS7ZYXkprq/pLaBWYq4GM0r4zdHY+NNRqEMU7uew=="
    },
    "node_modules/brace-expansion": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.1.tgz",
      "integrity": "sha512-XnAIvQ8eM+kC6aULx6wuQiwVsnzsi9d3WxzV3FpWTGA19F621kwdbsAcFKXgKUHZWsy+mY6iL1sHTxWEFCytDA==",
      "dev": true,
      "dependencies": {
        "balanced-match": "^1.0.0"
      }
    },
    "node_modules/braces": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.2.tgz",
      "integrity": "sha512-b8um+L1RzM3WDSzvhm6gIz1yfTbBt6YTlcEKAvsmqCZZFw46z626lVj9j1yEPW33H5H+lBQpZMP1k8l+78Ha0A==",
      "dev": true,
      "dependencies": {
        "fill-range": "^7.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/browser-stdout": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/browser-stdout/-/browser-stdout-1.3.1.tgz",
      "integrity": "sha512-qhAVI1+Av2X7qelOfAIYwXONood6XlZE/fXaBSmW/T5SzLAmCgzi+eiWE7fUvbHaeNBQH13UftjpXxsfLkMpgw==",
      "dev": true
    },
    "node_modules/camelcase": {
      "version": "6.3.0",
      "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-6.3.0.tgz",
      "integrity": "sha512-Gmy6FhYlCY7uOElZUSbxo2UCDH8owEk996gkbrpsgGtrJLM3J7jGxl9Ic7Qwwj4ivOE5AWZWRMecDdF7hqGjFA==",
      "dev": true,
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/chai": {
      "version": "4.3.7",
      "resolved": "https://registry.npmjs.org/chai/-/chai-4.3.7.tgz",
      "integrity": "sha512-HLnAzZ2iupm25PlN0xFreAlBA5zaBSv3og0DdeGA4Ar6h6rJ3A0rolRUKJhSF2V10GZKDgWF/VmAEsNWjCRB+A==",
      "dev": true,
      "dependencies": {
        "assertion-error": "^1.1.0",
        "check-error": "^1.0.2",
        "deep-eql": "^4.1.2",
        "get-func-name": "^2.0.0",
        "loupe": "^2.3.1",
        "pathval": "^1.1.1",
        "type-detect": "^4.0.5"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/chalk": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz",
      "integrity": "sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==",
      "dev": true,
      "dependencies": {
        "ansi-styles": "^4.1.0",
        "supports-color": "^7.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/chalk/node_modules/supports-color": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz",
      "integrity": "sha512-qpCAvRl9stuOHveKsn7HncJRvv501qIacKzQlO/+Lwxc9+0q2wLyv4Dfvt80/DPn2pqOBsJdDiogXGR9+OvwRw==",
      "dev": true,
      "dependencies": {
        "has-flag": "^4.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/check-error": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/check-error/-/check-error-1.0.2.tgz",
      "integrity": "sha512-BrgHpW9NURQgzoNyjfq0Wu6VFO6D7IZEmJNdtgNqpzGG8RuNFHt2jQxWlAs4HMe119chBnv+34syEZtc6IhLtA==",
      "dev": true,
      "engines": {
        "node": "*"
      }
    },
    "node_modules/chokidar": {
      "version": "3.5.3",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.5.3.tgz",
      "integrity": "sha512-Dr3sfKRP6oTcjf2JmUmFJfeVMvXBdegxB0iVQ5eb2V10uFJUCAS8OByZdVAyVb8xXNz3GjjTgj9kLWsZTqE6kw==",
      "dev": true,
      "funding": [
        {
          "type": "individual",
          "url": "https://paulmillr.com/funding/"
        }
      ],
      "dependencies": {
        "anymatch": "~3.1.2",
        "braces": "~3.0.2",
        "glob-parent": "~5.1.2",
        "is-binary-path": "~2.1.0",
        "is-glob": "~4.0.1",
        "normalize-path": "~3.0.0",
        "readdirp": "~3.6.0"
      },
      "engines": {
        "node": ">= 8.10.0"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/chownr": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz",
      "integrity": "sha512-bIomtDF5KGpdogkLd9VspvFzk9KfpyyGlS8YFVZl7TGPBHL5snIOnxeshwVgPteQ9b4Eydl+pVbIyE1DcvCWgQ==",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/cliui": {
      "version": "7.0.4",
      "resolved": "https://registry.npmjs.org/cliui/-/cliui-7.0.4.tgz",
      "integrity": "sha512-OcRE68cOsVMXp1Yvonl/fzkQOyjLSu/8bhPDfQt0e0/Eb283TKP20Fs2MqoPsr9SwA595rRCA+QMzYc9nBP+JQ==",
      "dev": true,
      "dependencies": {
        "string-width": "^4.2.0",
        "strip-ansi": "^6.0.0",
        "wrap-ansi": "^7.0.0"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "dev": true,
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "dev": true
    },
    "node_modules/color-support": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/color-support/-/color-support-1.1.3.tgz",
      "integrity": "sha512-qiBjkpbMLO/HL68y+lh4q0/O1MZFj2RX6X/KmMa3+gJD3z+WwI1ZzDHysvqHGS3mP6mznPckpXmw1nI9cJjyRg==",
      "bin": {
        "color-support": "bin.js"
      }
    },
    "node_modules/concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg=="
    },
    "node_modules/console-control-strings": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz",
      "integrity": "sha512-ty/fTekppD2fIwRvnZAVdeOiGd1c7YXEixbgJTNzqcxJWKQnjJ/V1bNEEE6hygpM3WjwHFUVK6HTjWSzV4a8sQ=="
    },
    "node_modules/core-util-is": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz",
      "integrity": "sha512-ZQBvi1DcpJ4GDqanjucZ2Hj3wEO5pZDS89BWbkcrvdxksJorwUDDZamX9ldFkp9aw2lmBDLgkObEA4DWNJ9FYQ=="
    },
    "node_modules/debug": {
      "version": "4.3.4",
      "resolved": "https://registry.npmjs.org/
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "lib": ["es2020"],
    "module": "commonjs",
    "target": "es2020",
    "declaration": false,
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node"
  },

  "exclude": [
    "node_modules"
  ]
}

```

### File: lib\attachISDOC.ts
```ts
import Invoice, {InvoiceType} from '@deltazero/isdoc'
import { PDFDocument } from 'pdf-lib'
import { hasISDOC } from './extractISDOC'
import { readFile, writeFile, stat, unlink } from 'fs/promises'
import { exec } from 'child_process'

export default async function attachISDOC(
    pdf: Buffer|PDFDocument,
    isdoc: string|Buffer|Invoice|InvoiceType
) : Promise<Buffer> {
  if (await hasISDOC(pdf))
    throw new Error('attachISDOC: This PDF Already Has an ISDOC Attachment')

  if (!(isdoc instanceof Invoice))
    isdoc = new Invoice(isdoc)

  if (pdf instanceof PDFDocument)
    pdf = Buffer.from(await pdf.save())

  const bin = __dirname + '/../node_modules/isdoc-pdf-bash/isdoc-pdf'
  await stat(bin)
    .catch(() => { throw new Error('attachISDOC: Cannot find [isdoc-pdf] executable') })

  const [[ inpdf ], [ inisdoc ], [ outpdf ]] = await Promise.all([ execute('mktemp'), execute('mktemp'), execute('mktemp') ])
  await Promise.all([
      writeFile(inpdf, pdf),
      writeFile(inisdoc, isdoc.toXML())
  ])

  await execute(`${bin} ${inpdf} ${inisdoc} ${outpdf}`)
  const result = await readFile(outpdf)

  // clean up
  await Promise.all([ unlink(inpdf), unlink(inisdoc), unlink(outpdf) ])

  return result
}

const execute = async (cmd: string, options: any = {}) : Promise<[string, string?]> =>
    new Promise((resolve, reject) =>
      exec(cmd, options, (e, stdout, stderr) => {
        if (e) return reject(e)
        resolve([stdout.toString().trim(), stderr?.toString().trim()])
      })
    )

```

### File: lib\createISDOCX.ts
```ts
import Invoice, { InvoiceType } from '@deltazero/isdoc'
import Zip from 'jszip'
import { hasISDOC } from './extractISDOC'

export default async function createISDOCX(
    pdf: Buffer,
    isdoc: string|Buffer|Invoice|InvoiceType,
    name ?: string
) {
  // noinspection SuspiciousTypeOfGuard
  if (!(pdf instanceof Buffer))
    throw new Error('createISDOCX: PDF Is Not an Instance of Buffer')

  if (await hasISDOC(pdf))
    throw new Error('createISDOCX: This PDF Already Has an ISDOC Attachment')

  if (!(isdoc instanceof Invoice))
    isdoc = new Invoice(isdoc)

  name ??= isdoc.ID?.replace(/[^\w.-]/gi, '_')
  if (!name)
    throw new Error('createISDOCX: File Name Is Not Set')

  const zip = new Zip()
  zip.file(name + '.pdf', pdf)
  zip.file(name + '.isdoc', isdoc.toXML())
  zip.file('manifest.xml', createManifest(name))

  return zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' })
}

export const createManifest = (name: string) : string =>
`<?xml version="1.0"?>
<manifest xmlns="http://isdoc.cz/namespace/2013/manifest">
  <maindocument filename="${name}.isdoc"/>
</manifest>
`

```

### File: lib\extractISDOC.ts
```ts
import PDFDocument from 'pdf-lib/cjs/api/PDFDocument'
import { PDFExtractAttachments } from './PDFAttachments'
import Invoice from '@deltazero/isdoc'

export default async function extractISDOC(pdf: Buffer|PDFDocument) : Promise<Invoice|null> {
  const document = !(pdf instanceof PDFDocument)
      ? await PDFDocument.load(pdf)
      : pdf

  const isdoc = PDFExtractAttachments(document)
      .find(r => r.name.match(/isdoc$/))
  if (!isdoc) return null

  return new Invoice(Buffer.from(isdoc.data))
}

export const hasISDOC = async (pdf: Buffer|PDFDocument) : Promise<boolean> => {
  const document = !(pdf instanceof PDFDocument)
      ? await PDFDocument.load(pdf)
      : pdf

  return !! PDFExtractAttachments(document).find(r => r.name.match(/isdoc$/))
}

```

### File: lib\PDFAttachments.ts
```ts
import {
  PDFDocument,
  PDFName,
  PDFDict,
  PDFArray,
  PDFHexString,
  PDFString,
  PDFStream,
  decodePDFRawStream,
  PDFRawStream,
} from 'pdf-lib'

export const PDFExtractAttachments = (pdfDoc: PDFDocument) => {
  const rawAttachments = PDFExtractRawAttachments(pdfDoc)
  return rawAttachments.map(({ fileName, fileSpec }) => {
    const stream = fileSpec
        .lookup(PDFName.of('EF'), PDFDict)
        .lookup(PDFName.of('F'), PDFStream) as PDFRawStream
    return {
      name: fileName.decodeText(),
      data: decodePDFRawStream(stream).decode(),
    }
  })
}

export const PDFExtractRawAttachments = (pdfDoc: PDFDocument) => {
  if (!pdfDoc.catalog.has(PDFName.of('Names'))) return []
  const Names = pdfDoc.catalog.lookup(PDFName.of('Names'), PDFDict)

  if (!Names.has(PDFName.of('EmbeddedFiles'))) return []
  let EmbeddedFiles = Names.lookup(PDFName.of('EmbeddedFiles'), PDFDict)

  if (!EmbeddedFiles.has(PDFName.of('Names')) && EmbeddedFiles.has(PDFName.of('Kids')))
    EmbeddedFiles = EmbeddedFiles.lookup(PDFName.of('Kids'), PDFArray).lookup(0) as PDFDict

  if (!EmbeddedFiles.has(PDFName.of('Names'))) return []
  const EFNames = EmbeddedFiles.lookup(PDFName.of('Names'), PDFArray)

  const rawAttachments = []
  for (let idx = 0, len = EFNames.size(); idx < len; idx += 2) {
    const fileName = EFNames.lookup(idx) as PDFHexString | PDFString
    const fileSpec = EFNames.lookup(idx + 1, PDFDict)
    rawAttachments.push({ fileName, fileSpec })
  }

  return rawAttachments
}

```

### File: lib\schemaISDOC.ts
```ts
export default `<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://isdoc.cz/namespace/2013" xmlns:isdoc="http://isdoc.cz/namespace/2013" targetNamespace="http://isdoc.cz/namespace/2013" elementFormDefault="qualified" version="6.0.2" xml:lang="cs">
  <xs:group name="Signature">
    <xs:sequence>
      <xs:any namespace="http://www.w3.org/2000/09/xmldsig#" processContents="lax"/>
    </xs:sequence>
  </xs:group>

  <xs:simpleType name="VersionType">
    <xs:restriction base="xs:string">
      <xs:pattern value="[0-9]+\\.[0-9]+(\\.[0-9]+)?"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="DocumentTypeType">
    <xs:restriction base="xs:integer">
      <xs:enumeration value="1">
        </xs:enumeration>
      <xs:enumeration value="2">
        </xs:enumeration>
      <xs:enumeration value="3">
        </xs:enumeration>
      <xs:enumeration value="4">
        </xs:enumeration>
      <xs:enumeration value="5">
        </xs:enumeration>
      <xs:enumeration value="6">
        </xs:enumeration>
      <xs:enumeration value="7">
        </xs:enumeration>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="SubDocumentTypeType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="SubDocumentTypeOriginType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>
  
  <xs:simpleType name="TargetConsolidatorType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ClientOnTargetConsolidatorType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>
  
  <xs:simpleType name="ClientBankAccountType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="IDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ID36Type">
    <xs:restriction base="IDType">
      <xs:maxLength value="36"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="UUIDType">
    <xs:restriction base="xs:string">
      <xs:pattern value="[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="IDSchemeType">
    <xs:restriction base="xs:anyURI"/>
  </xs:simpleType>

  <xs:simpleType name="IssuingSystemType">
    <xs:restriction base="xs:string">
      <xs:maxLength value="80"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="IssueDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="TaxPointDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="VATApplicableType">
    <xs:restriction base="BooleanType"/>
  </xs:simpleType>

  <xs:complexType name="NoteType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="languageID" type="xs:language" use="optional">
          </xs:attribute>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:complexType name="OrderReferencesType">
    <xs:sequence>
      <xs:element name="OrderReference" type="OrderReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="OrderReferenceType">
    <xs:sequence>
      <xs:element name="SalesOrderID" type="SalesOrderIDType">
        </xs:element>
      <xs:element name="ExternalOrderID" type="IDType" minOccurs="0">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="ExternalOrderIssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
      <xs:element name="ISDS_ID" type="ISDS_IDType" minOccurs="0">
        </xs:element>
      <xs:element name="FileReference" type="FileReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="ReferenceNumber" type="ReferenceNumberType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="OrderLineReferenceType">
    <xs:sequence>
      <xs:element name="LineID" type="LineIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:simpleType name="SalesOrderIDType">
    <xs:restriction base="IDType"/>
  </xs:simpleType>

  <xs:simpleType name="LineIDType">
    <xs:restriction base="IDType"/>
  </xs:simpleType>

  <xs:simpleType name="ParagraphIDType">
    <xs:restriction base="IDType"/>
  </xs:simpleType>

  <xs:complexType name="DeliveryNoteReferencesType">
    <xs:sequence>
      <xs:element name="DeliveryNoteReference" type="DeliveryNoteReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="DeliveryNoteReferenceType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="DeliveryNoteLineReferenceType">
    <xs:sequence>
      <xs:element name="LineID" type="LineIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:complexType name="ContractReferencesType">
    <xs:sequence>
      <xs:element name="ContractReference" type="ContractReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="ContractReferenceType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType">
        </xs:element>
      <xs:choice minOccurs="0">
        <xs:element name="LastValidDate" type="LastValidDateType">
          </xs:element>
        <xs:element name="LastValidDateUnbounded" type="LastValidDateUnboundedType">
          </xs:element>
      </xs:choice>
      <xs:element name="ISDS_ID" type="ISDS_IDType" minOccurs="0">
        </xs:element>
      <xs:element name="FileReference" type="FileReferenceType" minOccurs="0">
        </xs:element>
      <xs:element name="ReferenceNumber" type="ReferenceNumberType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="ContractLineReferenceType">
    <xs:sequence>
      <xs:element name="ParagraphID" type="ParagraphIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:simpleType name="LastValidDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:complexType name="LastValidDateUnboundedType">
    </xs:complexType>

  <xs:simpleType name="CurrRateType">
    <xs:restriction base="xs:decimal"/>
  </xs:simpleType>

  <xs:simpleType name="RefCurrRateType">
    <xs:restriction base="xs:decimal"/>
  </xs:simpleType>

  <xs:complexType name="OriginalDocumentReferencesType">
    <xs:sequence>
      <xs:element name="OriginalDocumentReference" type="OriginalDocumentReferenceType" maxOccurs="unbounded">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="OriginalDocumentReferenceType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="IssueDate" type="IssueDateType" minOccurs="0">
        </xs:element>
      <xs:element name="UUID" type="UUIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="IdAttribute"/>
  </xs:complexType>

  <xs:complexType name="OriginalDocumentLineReferenceType">
    <xs:sequence>
      <xs:element name="LineID" type="LineIDType" minOccurs="0">
        </xs:element>
    </xs:sequence>
    <xs:attributeGroup ref="RefAttribute"/>
  </xs:complexType>

  <xs:complexType name="SupplementsListType">
    <xs:sequence>
      <xs:element maxOccurs="unbounded" name="Supplement" type="SupplementType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="SupplementType">
    <xs:sequence>
      <xs:element name="Filename" type="FilenameType">
        </xs:element>
      <xs:element name="DigestMethod" type="DigestMethodType">
        </xs:element>
      <xs:element name="DigestValue" type="DigestValueType">
        </xs:element>
    </xs:sequence>
    <xs:attribute name="preview" type="BooleanType">
      </xs:attribute>
  </xs:complexType>

  <xs:simpleType name="FilenameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="DigestMethodType">
    <xs:attribute name="Algorithm" use="required" type="xs:anyURI">
      </xs:attribute>
  </xs:complexType>

  <xs:simpleType name="DigestValueType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="BooleanType">
    <xs:restriction base="xs:boolean">
      <xs:pattern value="true|false"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="ExtensionsType">
    <xs:sequence>
      <xs:any minOccurs="1" maxOccurs="unbounded" namespace="##other" processContents="lax"/>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AccountingSupplierPartyType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PartyType">
    <xs:sequence>
      <xs:element name="PartyIdentification" type="PartyIdentificationType">
        </xs:element>
      <xs:element name="PartyName" type="PartyNameType">
        </xs:element>
      <xs:element name="PostalAddress" type="PostalAddressType">
        </xs:element>
      <xs:element name="PartyTaxScheme" type="PartyTaxSchemeType" minOccurs="0" maxOccurs="unbounded">
        </xs:element>
      <xs:element minOccurs="0" name="RegisterIdentification" type="RegisterIdentificationType">
        </xs:element>
      <xs:element name="Contact" type="ContactType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PartyIdentificationType">
    <xs:sequence>
      <xs:element name="UserID" type="UserIDType" minOccurs="0">
        </xs:element>
      <xs:element name="CatalogFirmIdentification" type="CatalogFirmIdentificationType" minOccurs="0">
        </xs:element>
      <xs:element name="ID" type="IDType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="UserIDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="CatalogFirmIdentificationType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="PartyNameType">
    <xs:sequence>
      <xs:element name="Name" type="NameType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="NameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="PostalAddressType">
    <xs:sequence>
      <xs:element name="StreetName" type="StreetNameType">
        </xs:element>
      <xs:element name="BuildingNumber" type="BuildingNumberType">
        </xs:element>
      <xs:element name="CityName" type="CityNameType">
        </xs:element>
      <xs:element name="PostalZone" type="PostalZoneType">
        </xs:element>
      <xs:element name="Country" type="CountryType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="StreetNameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="BuildingNumberType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="CityNameType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="PostalZoneType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="CountryType">
    <xs:sequence>
      <xs:element name="IdentificationCode" type="IdentificationCodeType">
        </xs:element>
      <xs:element name="Name" type="NameType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="IdentificationCodeType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="PartyTaxSchemeType">
    <xs:sequence>
      <xs:element name="CompanyID" type="CompanyIDType">
        </xs:element>
      <xs:element name="TaxScheme" type="TaxSchemeType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="CompanyIDType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="TaxSchemeType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="RegisterIdentificationType">
    <xs:choice>
      <xs:sequence>
        <xs:element name="RegisterKeptAt" type="RegisterKeptAtType">
          </xs:element>
        <xs:element name="RegisterFileRef" type="RegisterFileRefType">
          </xs:element>
        <xs:element name="RegisterDate" type="RegisterDateType">
          </xs:element>
      </xs:sequence>
      <xs:element name="Preformatted" type="PreformattedType">
        </xs:element>
    </xs:choice>
  </xs:complexType>

  <xs:simpleType name="RegisterKeptAtType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="RegisterFileRefType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="RegisterDateType">
    <xs:restriction base="xs:date"/>
  </xs:simpleType>

  <xs:simpleType name="PreformattedType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="ContactType">
    <xs:sequence>
      <xs:element name="Name" type="NameType" minOccurs="0">
        </xs:element>
      <xs:element name="Telephone" type="TelephoneType" minOccurs="0">
        </xs:element>
      <xs:element name="ElectronicMail" type="ElectronicMailType" minOccurs="0">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="TelephoneType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:simpleType name="ElectronicMailType">
    <xs:restriction base="xs:string"/>
  </xs:simpleType>

  <xs:complexType name="SellerSupplierPartyType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AccountingCustomerPartyType">
    <xs:sequence>
      <xs:element name="Party" type="PartyType">
        </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AnonymousCustomerPartyType">
    <xs:sequence>
      <xs:element name="ID" type="IDType">
        </xs:element>
      <xs:element name="IDScheme" type="IDSchemeType">
        </xs:element>
    </xs
... [TRUNCATED]
```

### File: tests\index.ts
```ts
import { Invoice, InvoiceType, attachISDOC, extractISDOC, hasISDOC } from '..'
import { readFileSync, writeFileSync } from 'fs'
import { before } from 'mocha'
import { expect } from 'chai'
import createISDOCX from '../lib/createISDOCX'
import Zip from 'jszip'

const test0 = readFileSync(__dirname + '/test000.pdf'),
      test1 = readFileSync(__dirname + '/test001.isdoc.pdf'),
      test2 = readFileSync(__dirname + '/test002.isdoc.pdf'),
      invoice = readFileSync(__dirname + '/invoice.isdoc'),
      template = {
        DocumentType: 'invoice',
        ID: 1,
        IssuingSystem: 'ΔO Delta Zero',
        IssueDate: new Date(),
        TaxPointDate: new Date(),
        VATApplicable: true,
        AccountingSupplierParty: {
          Party: {
            PartyIdentification: {ID: '12345678'},
            PartyName: {Name: 'Test s.r.o.'},
            PostalAddress: {
              StreetName: 'Dodavatelská',
              BuildingNumber: '1',
              CityName: 'Dodavatelov',
              PostalZone: '12345',
              Country: {IdentificationCode: 'CZ', Name: ''}
            },
            PartyTaxScheme: {
              CompanyID: 'CZ12345678',
              TaxScheme: 'VAT'
            },
            Contact: {
              Telephone: '222111000',
              ElectronicMail: 'dodavatel@posta.cz'
            }
          }
        },
        AccountingCustomerParty: {
          Party: {
            PartyIdentification: {ID: '12345678'},
            PartyName: {Name: 'Test s.r.o.'},
            PostalAddress: {
              StreetName: 'Dodavatelská',
              BuildingNumber: '1',
              CityName: 'Dodavatelov',
              PostalZone: '12345',
              Country: {IdentificationCode: 'CZ', Name: ''}
            },
            PartyTaxScheme: {
              CompanyID: 'CZ12345678',
              TaxScheme: 'VAT'
            },
            Contact: {
              Telephone: '222111000',
              ElectronicMail: 'dodavatel@posta.cz'
            }
          }
        },
        InvoiceLines: {
          InvoiceLine: [
            {
              ID: '10001',
              InvoicedQuantity: 1,
              LineExtensionAmount: 100,
              LineExtensionAmountTaxInclusive: 121,
              LineExtensionTaxAmount: 21,
              UnitPrice: 100,
              UnitPriceTaxInclusive: 121,
              ClassifiedTaxCategory: {Percent: 21, VATCalculationMethod: 0, VATApplicable: true},
              Item: {Description: 'Zboží 10001'}
            },
          ]
        },
        TaxTotal: {
          TaxSubTotal: {
            TaxableAmount: 100,
            TaxAmount: 21,
            TaxInclusiveAmount: 121,
            AlreadyClaimedTaxableAmount: 0,
            AlreadyClaimedTaxAmount: 0,
            AlreadyClaimedTaxInclusiveAmount: 0,
            DifferenceTaxableAmount: 100,
            DifferenceTaxAmount: 21,
            DifferenceTaxInclusiveAmount: 121,
            TaxCategory: {
              Percent: 21,
              VATApplicable: true,
            }
          },
          TaxAmount: 21
        },
        LegalMonetaryTotal: {
          TaxExclusiveAmount: 5500,
          TaxInclusiveAmount: 6655,
          AlreadyClaimedTaxExclusiveAmount: 0,
          AlreadyClaimedTaxInclusiveAmount: 0,
          DifferenceTaxExclusiveAmount: 5500,
          DifferenceTaxInclusiveAmount: 6655,
          PayableRoundingAmount: 0,
          PaidDepositsAmount: 0,
          PayableAmount: 6655
        },
        PaymentMeans: {
          Payment: {
            PaidAmount: 6655,
            PaymentMeansCode: 42,
            Details: {
              PaymentDueDate: new Date(),
              ID: 1234567890,
              BankCode: 1234,
              Name: 'BANKA',
              IBAN: '',
              BIC: '',
              VariableSymbol: 10111,
              ConstantSymbol: '',
              SpecificSymbol: ''
            }
          }
        }
      }

describe('Extracting ISDOCs', () => {
  it ('test000.pdf -> false', async () => {
    expect(await hasISDOC(test0)).to.be.false
  })

  it ('test001.isdoc.pdf -> true', async () => {
    expect(await hasISDOC(test1)).to.be.true
    const isdoc = await extractISDOC(test1)
    expect(isdoc).to.be.instanceof(Invoice)
    expect(isdoc?.ID).to.be.eq('FV-1/2021')
    expect(isdoc?.UUID).to.be.eq('AEC4791C-4BA1-451E-A1DC-2BF634B1C29D')
    expect(isdoc?.['$_version']).to.be.eq('6.0.2')
  })

  it ('test002.isdoc.pdf -> true', async () => {
    expect(await hasISDOC(test2)).to.be.true
    const isdoc = await extractISDOC(test2)
    expect(isdoc).to.be.instanceof(Invoice)
    expect(isdoc?.ID).to.be.eq('FV-2/2021')
    expect(isdoc?.UUID).to.be.eq('A34D00BF-FFB3-445B-BA1F-C5764B89409E')
    expect(isdoc?.['$_version']).to.be.eq('6.0.2')
  })
})

describe('Attaching ISDOC', () => {
  it ('test000.pdf -> test000.isdoc.pdf', async () => {
    const test0isdoc = await attachISDOC(test0, template as InvoiceType)
    expect(test0isdoc).to.be.instanceof(Buffer)
    writeFileSync(__dirname + '/test000.isdoc.pdf', test0isdoc)
  })

  it ('test000.isdoc.pdf is valid', async () => {
    const test0i = readFileSync(__dirname + '/test000.isdoc.pdf')
    expect(await hasISDOC(test0i)).to.be.true

    const isdoc = await extractISDOC(test0i)
    expect(isdoc).to.be.instanceof(Invoice)
    expect(isdoc?.ID?.toString()).to.be.eq('1')
    expect(isdoc?.UUID).to.be.match(/[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}/)
    expect(isdoc?.['$_version']).to.be.eq('6.0.1')
  })

  it ('test001.isdoc.pdf -> throws that it already has one', async () => {
    expect(await attachISDOC(test1, invoice).catch(e => e.message)).to.be.include('This PDF Already Has an ISDOC Attachment')
  })
})

describe('Creating ISDOCX archive', () => {
  it ('test000.pdf + invoice.isdoc -> test000.isdox', async () => {
    const isdocx = await createISDOCX(test0, invoice)
    expect(isdocx).to.be.instanceof(Buffer)
    writeFileSync(__dirname + '/test000.isdocx', isdocx)
  })

  it ('test001.isdoc.pdf + invoice.isdoc -> throws ', async () => {
    expect(await createISDOCX(test1, invoice).catch(e => e.message)).to.be.include('This PDF Already Has an ISDOC Attachment')
  })
})

describe('Validating created ISDOCX archive', () => {
  let zip : Zip

  before(async () => {
    zip = await new Zip().loadAsync(readFileSync(__dirname + '/test000.isdocx'))
  })

  it ('test000.isdox is readable', async () => {
    expect(zip.files).to.be.an('object')
    expect(Object.keys(zip.files)).to.be.an('Array')
  })

  it ('test000.isdox has 3 files', async () => {
    expect(Object.keys(zip.files).length).to.be.eq(3)
  })

  it ('test000.isdox has a .pdf', async () => {
    expect(Object.keys(zip.files).find(r => r.match(/\.pdf$/i))).to.be.a('string')
  })

  it ('test000.isdox has a .isdoc', async () => {
    expect(Object.keys(zip.files).find(r => r.match(/\.isdoc$/i))).to.be.a('string')
  })

  it ('test000.isdox has a valid .isdoc', async () => {
    const name = Object.keys(zip.files).find(r => r.match(/\.isdoc$/i)) as string,
          file = await zip.file(name)?.async('nodebuffer'),
          isdoc = new Invoice(file)
    expect(isdoc?.['$_version']).to.be.eq('6.0.1')
  })

  it ('test000.isdox has a manifest.xml', async () => {
    expect(Object.keys(zip.files).find(r => r.toLowerCase() === 'manifest.xml')).to.be.a('string')
  })
})

// describe('Clean Up', () => {
//   it ('Clean Up', () => {
//     expect((() => {
//       rmSync(__dirname + '/test000.isdoc.pdf')
//       rmSync(__dirname + '/test000.isdocx')
//       return true
//     })()).not.to.throw
//   })
// })

```

