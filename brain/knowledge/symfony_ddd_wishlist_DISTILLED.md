---
id: symfony-ddd-wishlist
type: knowledge
owner: OA_Triage
---
# symfony-ddd-wishlist
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "wishlist",
  "version": "1.0.0",
  "description": "Wishlist DDD app",
  "main": "index.js",
  "directories": {
    "test": "tests"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "wishlist",
    "ddd",
    "symfony"
  ],
  "author": "Jan Iwanow <iwanow.jan@gmail.com> (http://janiwanow.com)",
  "license": "MIT",
  "dependencies": {
    "@symfony/webpack-encore": "^0.10.0",
    "url-search-params": "^0.7.1",
    "vue": "^2.4.2",
    "vue-loader": "^13.0.2",
    "vue-notifyjs": "^0.1.7",
    "vue-resource": "^1.3.4",
    "vue-router": "^2.7.0",
    "vue-template-compiler": "^2.4.2"
  },
  "devDependencies": {
    "node-sass": "^4.5.3",
    "sass-loader": "^6.0.6"
  }
}

```

### File: README.md
```md
[![](https://img.shields.io/packagist/dt/franzose/symfony-ddd-wishlist.svg)](https://packagist.org/packages/franzose/symfony-ddd-wishlist)
[![](https://travis-ci.org/franzose/symfony-ddd-wishlist.svg?branch=master)](https://travis-ci.org/franzose/symfony-ddd-wishlist)
[![](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist?branch=master)

[На русском](https://github.com/franzose/symfony-ddd-wishlist/blob/master/README_RUS.md)

Wishlist
========

*I'm still working on the project, so some things can be unimplemented yet.*

This repository serves as an implementation of DDD, domain driven design, with usage of Symfony 3, PostgreSQL, and Redis as a backend and Vue.js/Sass as a frontend. The project is heavily inspired by [DDD Cargo Sample in PHP](https://github.com/codeliner/php-ddd-cargo-sample).

The basis for the project is a fairly simple domain, a wish list. Each wish can have its own price, daily fee and a fund which is implemented as a list of deposits to the wish. Wish can be fulfilled and is fulfilled as soon as its fund has enough money. Mistaken deposits can be removed or transfered to another wish. Any wish can have surplus funds, so they can also be transfered to other wishes.

## Installation
Clone the repository and run the following commands to install all the dependencies and build frontend scripts and styles:
```bash
cd /path/to/webroot
git clone https://github.com/franzose/symfony-ddd-wishlist.git
cd symfony-ddd-wishlist
composer self-update
composer install
npm install
./node_modules/.bin/encore dev
```

### PostgreSQL, Redis, and PHP dev server
To simplify backend setup, the project uses a couple of Docker images (so you need to install Docker too) that you'll find in `docker-compose.yml.dist` file. Run the following commands to start PostgreSQL and Redis, and also fill the database with some data:

```bash
cp ./app/config/parameters.yml.dist ./app/config/parameters.yml
cp ./app/config/parameters_permanent.yml.dist ./app/config/parameters_permanent.yml
cp ./docker-compose.yml.dist ./docker-compose.yml
docker-compose up -d
php bin/console doctrine:fixtures:load --fixtures=/path/to/src/Infrastructure/Persistence/Doctrine/Fixture/LoadWishesData.php
php bin/console server:start
```

## Project structure
TODO: write about project structure

## Support
If you have any problems using the application, please open a Github issue. The same applies to any questions or feature requests.

## Contributions
Any contribution is appreciated. This application serves as an example implementation of the domain driven design. I'd be very glad of any kind of shares of this repository being it a tweet, a post, a link, or whatever.

## Tests
The application is covered by unit and functional tests. Functional tests use SQLite database. Before running tests, please copy PHPUnit's configuration file:

```bash
cp ./phpunit.xml.dist ./phpunit.xml
```

Then use the following command to run tests:

```bash
./vendor/bin/phpunit
```

```

### File: composer.json
```json
{
    "name": "franzose/symfony-ddd-wishlist",
    "license": "MIT",
    "type": "project",
    "keywords": ["symfony", "ddd", "vuejs", "wishlist", "sample app"],
    "description": "Wishlist, a sample application on Symfony 3 and Vue.js built with DDD in mind.",
    "autoload": {
        "psr-4": {
            "Wishlist\\": "src/"
        },
        "classmap": [
            "app/AppKernel.php",
            "app/AppCache.php"
        ]
    },
    "autoload-dev": {
        "psr-4": {
            "Wishlist\\Tests\\": "tests/"
        },
        "files": [
            "vendor/symfony/symfony/src/Symfony/Component/VarDumper/Resources/functions/dump.php"
        ]
    },
    "require": {
        "php": ">=7.1",
        "doctrine/doctrine-bundle": "^1.6",
        "doctrine/orm": "^2.5",
        "friendsofsymfony/jsrouting-bundle": "^1.6",
        "incenteev/composer-parameter-handler": "^2.0",
        "moneyphp/money": "^3.0",
        "ramsey/uuid": "^3.6",
        "ramsey/uuid-doctrine": "^1.4",
        "sensio/distribution-bundle": "^5.0.19",
        "sensio/framework-extra-bundle": "^3.0.2",
        "symfony/monolog-bundle": "^3.1.0",
        "symfony/polyfill-apcu": "^1.0",
        "symfony/swiftmailer-bundle": "^2.3.10",
        "symfony/symfony": "3.3.*",
        "twig/twig": "^1.0||^2.0",
        "webmozart/assert": "^1.2"
    },
    "require-dev": {
        "doctrine/doctrine-fixtures-bundle": "^2.3",
        "fzaninotto/faker": "^1.6",
        "liip/functional-test-bundle": "^1.8",
        "mockery/mockery": "^0.9.9",
        "phpunit/phpunit": "^6.2",
        "sensio/generator-bundle": "^3.0",
        "symfony/phpunit-bridge": "^3.0"
    },
    "scripts": {
        "symfony-scripts": [
            "Incenteev\\ParameterHandler\\ScriptHandler::buildParameters",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::buildBootstrap",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::clearCache",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installAssets",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installRequirementsFile",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::prepareDeploymentTarget"
        ],
        "post-install-cmd": [
            "@symfony-scripts"
        ],
        "post-update-cmd": [
            "@symfony-scripts"
        ]
    },
    "config": {
        "sort-packages": true
    },
    "extra": {
        "symfony-app-dir": "app",
        "symfony-bin-dir": "bin",
        "symfony-var-dir": "var",
        "symfony-web-dir": "web",
        "symfony-tests-dir": "tests",
        "symfony-assets-install": "relative",
        "incenteev-parameters": {
            "file": "app/config/parameters.yml"
        },
        "branch-alias": null
    }
}

```

### File: LICENSE.txt
```txt
The MIT License (MIT)

Copyright (c) 2017 Jan Iwanow

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

### File: npm-shrinkwrap.json
```json
{
  "name": "wishlist",
  "version": "1.0.0",
  "dependencies": {
    "@symfony/webpack-encore": {
      "version": "0.10.0",
      "from": "@symfony/webpack-encore@latest",
      "resolved": "https://registry.npmjs.org/@symfony/webpack-encore/-/webpack-encore-0.10.0.tgz"
    },
    "abbrev": {
      "version": "1.1.0",
      "from": "abbrev@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/abbrev/-/abbrev-1.1.0.tgz"
    },
    "accepts": {
      "version": "1.3.3",
      "from": "accepts@>=1.3.3 <1.4.0",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.3.tgz"
    },
    "acorn": {
      "version": "5.1.1",
      "from": "acorn@>=5.0.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/acorn/-/acorn-5.1.1.tgz"
    },
    "acorn-dynamic-import": {
      "version": "2.0.2",
      "from": "acorn-dynamic-import@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/acorn-dynamic-import/-/acorn-dynamic-import-2.0.2.tgz",
      "dependencies": {
        "acorn": {
          "version": "4.0.13",
          "from": "acorn@>=4.0.3 <5.0.0",
          "resolved": "https://registry.npmjs.org/acorn/-/acorn-4.0.13.tgz"
        }
      }
    },
    "adjust-sourcemap-loader": {
      "version": "1.1.0",
      "from": "adjust-sourcemap-loader@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/adjust-sourcemap-loader/-/adjust-sourcemap-loader-1.1.0.tgz",
      "dependencies": {
        "camelcase": {
          "version": "1.2.1",
          "from": "camelcase@>=1.2.1 <2.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-1.2.1.tgz"
        },
        "lodash.defaults": {
          "version": "3.1.2",
          "from": "lodash.defaults@>=3.1.2 <4.0.0",
          "resolved": "https://registry.npmjs.org/lodash.defaults/-/lodash.defaults-3.1.2.tgz",
          "dependencies": {
            "lodash.assign": {
              "version": "3.2.0",
              "from": "lodash.assign@>=3.0.0 <4.0.0",
              "resolved": "https://registry.npmjs.org/lodash.assign/-/lodash.assign-3.2.0.tgz"
            }
          }
        }
      }
    },
    "ajv": {
      "version": "5.2.2",
      "from": "ajv@>=5.0.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-5.2.2.tgz"
    },
    "ajv-keywords": {
      "version": "1.5.1",
      "from": "ajv-keywords@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-1.5.1.tgz"
    },
    "align-text": {
      "version": "0.1.4",
      "from": "align-text@>=0.1.3 <0.2.0",
      "resolved": "https://registry.npmjs.org/align-text/-/align-text-0.1.4.tgz"
    },
    "alphanum-sort": {
      "version": "1.0.2",
      "from": "alphanum-sort@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/alphanum-sort/-/alphanum-sort-1.0.2.tgz"
    },
    "amdefine": {
      "version": "1.0.1",
      "from": "amdefine@>=0.0.4",
      "resolved": "https://registry.npmjs.org/amdefine/-/amdefine-1.0.1.tgz"
    },
    "ansi-html": {
      "version": "0.0.7",
      "from": "ansi-html@0.0.7",
      "resolved": "https://registry.npmjs.org/ansi-html/-/ansi-html-0.0.7.tgz"
    },
    "ansi-regex": {
      "version": "2.1.1",
      "from": "ansi-regex@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz"
    },
    "ansi-styles": {
      "version": "2.2.1",
      "from": "ansi-styles@>=2.2.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz"
    },
    "anymatch": {
      "version": "1.3.0",
      "from": "anymatch@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-1.3.0.tgz"
    },
    "argparse": {
      "version": "1.0.9",
      "from": "argparse@>=1.0.7 <2.0.0",
      "resolved": "https://registry.npmjs.org/argparse/-/argparse-1.0.9.tgz"
    },
    "arr-diff": {
      "version": "2.0.0",
      "from": "arr-diff@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz"
    },
    "arr-flatten": {
      "version": "1.1.0",
      "from": "arr-flatten@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz"
    },
    "array-find-index": {
      "version": "1.0.2",
      "from": "array-find-index@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/array-find-index/-/array-find-index-1.0.2.tgz"
    },
    "array-flatten": {
      "version": "2.1.1",
      "from": "array-flatten@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-2.1.1.tgz"
    },
    "array-union": {
      "version": "1.0.2",
      "from": "array-union@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/array-union/-/array-union-1.0.2.tgz"
    },
    "array-uniq": {
      "version": "1.0.3",
      "from": "array-uniq@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/array-uniq/-/array-uniq-1.0.3.tgz"
    },
    "array-unique": {
      "version": "0.2.1",
      "from": "array-unique@>=0.2.1 <0.3.0",
      "resolved": "https://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz"
    },
    "arrify": {
      "version": "1.0.1",
      "from": "arrify@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/arrify/-/arrify-1.0.1.tgz"
    },
    "asn1.js": {
      "version": "4.9.1",
      "from": "asn1.js@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/asn1.js/-/asn1.js-4.9.1.tgz"
    },
    "assert": {
      "version": "1.4.1",
      "from": "assert@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/assert/-/assert-1.4.1.tgz"
    },
    "async": {
      "version": "2.5.0",
      "from": "async@>=2.1.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/async/-/async-2.5.0.tgz"
    },
    "async-each": {
      "version": "1.0.1",
      "from": "async-each@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/async-each/-/async-each-1.0.1.tgz"
    },
    "atob": {
      "version": "1.1.3",
      "from": "atob@>=1.1.0 <1.2.0",
      "resolved": "https://registry.npmjs.org/atob/-/atob-1.1.3.tgz"
    },
    "autoprefixer": {
      "version": "6.7.7",
      "from": "autoprefixer@>=6.3.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-6.7.7.tgz",
      "dependencies": {
        "browserslist": {
          "version": "1.7.7",
          "from": "browserslist@>=1.7.6 <2.0.0",
          "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-1.7.7.tgz"
        }
      }
    },
    "babel-code-frame": {
      "version": "6.22.0",
      "from": "babel-code-frame@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.22.0.tgz"
    },
    "babel-core": {
      "version": "6.25.0",
      "from": "babel-core@>=6.24.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-core/-/babel-core-6.25.0.tgz"
    },
    "babel-generator": {
      "version": "6.25.0",
      "from": "babel-generator@>=6.25.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-generator/-/babel-generator-6.25.0.tgz"
    },
    "babel-helper-builder-binary-assignment-operator-visitor": {
      "version": "6.24.1",
      "from": "babel-helper-builder-binary-assignment-operator-visitor@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-builder-binary-assignment-operator-visitor/-/babel-helper-builder-binary-assignment-operator-visitor-6.24.1.tgz"
    },
    "babel-helper-call-delegate": {
      "version": "6.24.1",
      "from": "babel-helper-call-delegate@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-call-delegate/-/babel-helper-call-delegate-6.24.1.tgz"
    },
    "babel-helper-define-map": {
      "version": "6.24.1",
      "from": "babel-helper-define-map@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-define-map/-/babel-helper-define-map-6.24.1.tgz"
    },
    "babel-helper-explode-assignable-expression": {
      "version": "6.24.1",
      "from": "babel-helper-explode-assignable-expression@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-explode-assignable-expression/-/babel-helper-explode-assignable-expression-6.24.1.tgz"
    },
    "babel-helper-function-name": {
      "version": "6.24.1",
      "from": "babel-helper-function-name@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-function-name/-/babel-helper-function-name-6.24.1.tgz"
    },
    "babel-helper-get-function-arity": {
      "version": "6.24.1",
      "from": "babel-helper-get-function-arity@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-get-function-arity/-/babel-helper-get-function-arity-6.24.1.tgz"
    },
    "babel-helper-hoist-variables": {
      "version": "6.24.1",
      "from": "babel-helper-hoist-variables@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-hoist-variables/-/babel-helper-hoist-variables-6.24.1.tgz"
    },
    "babel-helper-optimise-call-expression": {
      "version": "6.24.1",
      "from": "babel-helper-optimise-call-expression@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-optimise-call-expression/-/babel-helper-optimise-call-expression-6.24.1.tgz"
    },
    "babel-helper-regex": {
      "version": "6.24.1",
      "from": "babel-helper-regex@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-regex/-/babel-helper-regex-6.24.1.tgz"
    },
    "babel-helper-remap-async-to-generator": {
      "version": "6.24.1",
      "from": "babel-helper-remap-async-to-generator@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-remap-async-to-generator/-/babel-helper-remap-async-to-generator-6.24.1.tgz"
    },
    "babel-helper-replace-supers": {
      "version": "6.24.1",
      "from": "babel-helper-replace-supers@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-replace-supers/-/babel-helper-replace-supers-6.24.1.tgz"
    },
    "babel-helpers": {
      "version": "6.24.1",
      "from": "babel-helpers@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helpers/-/babel-helpers-6.24.1.tgz"
    },
    "babel-loader": {
      "version": "7.1.1",
      "from": "babel-loader@>=7.1.0 <8.0.0",
      "resolved": "https://registry.npmjs.org/babel-loader/-/babel-loader-7.1.1.tgz"
    },
    "babel-messages": {
      "version": "6.23.0",
      "from": "babel-messages@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz"
    },
    "babel-plugin-check-es2015-constants": {
      "version": "6.22.0",
      "from": "babel-plugin-check-es2015-constants@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-check-es2015-constants/-/babel-plugin-check-es2015-constants-6.22.0.tgz"
    },
    "babel-plugin-syntax-async-functions": {
      "version": "6.13.0",
      "from": "babel-plugin-syntax-async-functions@>=6.8.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-syntax-async-functions/-/babel-plugin-syntax-async-functions-6.13.0.tgz"
    },
    "babel-plugin-syntax-exponentiation-operator": {
      "version": "6.13.0",
      "from": "babel-plugin-syntax-exponentiation-operator@>=6.8.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-syntax-exponentiation-operator/-/babel-plugin-syntax-exponentiation-operator-6.13.0.tgz"
    },
    "babel-plugin-syntax-trailing-function-commas": {
      "version": "6.22.0",
      "from": "babel-plugin-syntax-trailing-function-commas@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-syntax-trailing-function-commas/-/babel-plugin-syntax-trailing-function-commas-6.22.0.tgz"
    },
    "babel-plugin-transform-async-to-generator": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-async-to-generator@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-async-to-generator/-/babel-plugin-transform-async-to-generator-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-arrow-functions": {
      "version": "6.22.0",
      "from": "babel-plugin-transform-es2015-arrow-functions@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-arrow-functions/-/babel-plugin-transform-es2015-arrow-functions-6.22.0.tgz"
    },
    "babel-plugin-transform-es2015-block-scoped-functions": {
      "version": "6.22.0",
      "from": "babel-plugin-transform-es2015-block-scoped-functions@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-block-scoped-functions/-/babel-plugin-transform-es2015-block-scoped-functions-6.22.0.tgz"
    },
    "babel-plugin-transform-es2015-block-scoping": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-block-scoping@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-block-scoping/-/babel-plugin-transform-es2015-block-scoping-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-classes": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-classes@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-classes/-/babel-plugin-transform-es2015-classes-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-computed-properties": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-computed-properties@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-computed-properties/-/babel-plugin-transform-es2015-computed-properties-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-destructuring": {
      "version": "6.23.0",
      "from": "babel-plugin-transform-es2015-destructuring@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-destructuring/-/babel-plugin-transform-es2015-destructuring-6.23.0.tgz"
    },
    "babel-plugin-transform-es2015-duplicate-keys": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-duplicate-keys@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-duplicate-keys/-/babel-plugin-transform-es2015-duplicate-keys-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-for-of": {
      "version": "6.23.0",
      "from": "babel-plugin-transform-es2015-for-of@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-for-of/-/babel-plugin-transform-es2015-for-of-6.23.0.tgz"
    },
    "babel-plugin-transform-es2015-function-name": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-function-name@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-function-name/-/babel-plugin-transform-es2015-function-name-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-literals": {
     
... [TRUNCATED]
```

### File: README_RUS.md
```md
[![](https://img.shields.io/packagist/dt/franzose/symfony-ddd-wishlist.svg)](https://packagist.org/packages/franzose/symfony-ddd-wishlist)
[![](https://travis-ci.org/franzose/symfony-ddd-wishlist.svg?branch=master)](https://travis-ci.org/franzose/symfony-ddd-wishlist)
[![](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist?branch=master)

[In English](https://github.com/franzose/symfony-ddd-wishlist/blob/master/README.md)

Wishlist
========

*Я всё еще работаю над проектом, поэтому некоторые вещи могут оставаться нереализованными.*

Этот репозиторий посвящен реализации предметно-ориентированного проектирования (DDD) с использованием Symfony 3, PostgreSQL и Redis для серверной части, а также Vue.js/SASS для фронтенда.

За основу проекта взята довольно простая предметная область — вишлист. Это список желаний, в который можно добавлять свои желания, а также их исполнять. Каждое желание имеет свою стоимость, размер ежедневного денежного вклада и копилку, выраженную набором вкладов в это желание. Чтобы исполнить желание, необходимо вложить в него достаточное количество денег. Ошибочные вклады можно удалять, либо перенаправлять на другие желания. У желаний могут быть излишки вкладов, которые также можно перенаправлять на другие желания.

## Установка
Склонируйте репозиторий и выполните следующие команды, чтобы установить все зависимости и собрать скрипты со стилями для фронтенда:
```bash
cd /path/to/webroot
git clone https://github.com/franzose/symfony-ddd-wishlist.git
cd symfony-ddd-wishlist
composer self-update
composer install
npm install
./node_modules/.bin/encore dev
```

### PostgreSQL, Redis и dev-сервер PHP
Для упрощения разворачивания базы данных и кеша в проекте используются образы Docker (так что его тоже придётся установить), указанные в файле `docker-compose.yml.dist`. Выполните следующие команды, чтобы запустить PostgreSQL и Redis, а также заполнить базу данных начальными данными:

```bash
cp ./app/config/parameters.yml.dist ./app/config/parameters.yml
cp ./app/config/parameters_permanent.yml.dist ./app/config/parameters_permanent.yml
cp ./docker-compose.yml.dist ./docker-compose.yml
docker-compose up -d
php bin/console doctrine:fixtures:load --fixtures=/path/to/src/Infrastructure/Persistence/Doctrine/Fixture/LoadWishesData.php
php bin/console server:start
```

## Структура проекта
TODO: написать про структуру проекта

## Поддержка
Если у вас возникли какие-либо проблемы в процессе использования данного приложения, пожалуйста напишите об этом в отдельной задаче. То же касается вопросов по реализации функциональности или запросов на добавление новых возможностей.

## Собственный вклад
Любой вклад ценен. Данное приложение служит одним из примеров реализации предметно-ориентированного проектирования. Хорошим или плохим, это уже не мне решать. Поэтому я был бы очень рад распространению информации об этом репозитории в широкие массы (<s>зараспространите среди жильцов вашего ЖЭКа, как вы это любите</s>).

## Тесты
Приложение покрыто юнит- и функциональными тестами. Для функциональных тестов используется база данных SQLite. Перед запуском тестов скопируйте конфигурационный файл-образец PHPUnit:

```bash
cp ./phpunit.xml.dist ./phpunit.xml
```

Затем, чтобы запустить тесты, используйте следующую команду:

```bash
./vendor/bin/phpunit
```

```

### File: webpack.config.js
```js
const Encore = require('@symfony/webpack-encore');

Encore
    .setOutputPath('web/assets/')
    .setPublicPath('/assets')
    .cleanupOutputBeforeBuild()
    .addEntry('app', './app/Resources/assets/js/app.js')
    .addStyleEntry('styles', './app/Resources/assets/scss/app.scss')
    .enableSassLoader()
    .enableVueLoader()
    .enableSourceMaps(!Encore.isProduction())
;

module.exports = Encore.getWebpackConfig();
```

### File: app\AppCache.php
```php
<?php

use Symfony\Bundle\FrameworkBundle\HttpCache\HttpCache;

class AppCache extends HttpCache
{
}

```

### File: app\AppKernel.php
```php
<?php

use Symfony\Component\HttpKernel\Kernel;
use Symfony\Component\Config\Loader\LoaderInterface;

class AppKernel extends Kernel
{
    public function registerBundles()
    {
        $bundles = [
            new Symfony\Bundle\FrameworkBundle\FrameworkBundle(),
            new Symfony\Bundle\SecurityBundle\SecurityBundle(),
            new Symfony\Bundle\TwigBundle\TwigBundle(),
            new Symfony\Bundle\MonologBundle\MonologBundle(),
            new Symfony\Bundle\SwiftmailerBundle\SwiftmailerBundle(),
            new Doctrine\Bundle\DoctrineBundle\DoctrineBundle(),
            new Sensio\Bundle\FrameworkExtraBundle\SensioFrameworkExtraBundle(),
            new FOS\JsRoutingBundle\FOSJsRoutingBundle(),
        ];

        $env = $this->getEnvironment();

        if (in_array($env, ['dev', 'test'], true)) {
            $bundles[] = new Symfony\Bundle\DebugBundle\DebugBundle();
            $bundles[] = new Symfony\Bundle\WebProfilerBundle\WebProfilerBundle();
            $bundles[] = new Sensio\Bundle\DistributionBundle\SensioDistributionBundle();

            if ('dev' === $env) {
                $bundles[] = new Sensio\Bundle\GeneratorBundle\SensioGeneratorBundle();
                $bundles[] = new Symfony\Bundle\WebServerBundle\WebServerBundle();
            }

            $bundles[] = new Doctrine\Bundle\FixturesBundle\DoctrineFixturesBundle();
            $bundles[] = new Liip\FunctionalTestBundle\LiipFunctionalTestBundle();
        }

        return $bundles;
    }

    public function getRootDir()
    {
        return __DIR__;
    }

    public function getCacheDir()
    {
        return dirname(__DIR__).'/var/cache/'.$this->getEnvironment();
    }

    public function getLogDir()
    {
        return dirname(__DIR__).'/var/logs';
    }

    public function registerContainerConfiguration(LoaderInterface $loader)
    {
        $loader->load($this->getRootDir().'/config/config_'.$this->getEnvironment().'.yml');
    }
}

```

### File: web\app.php
```php
<?php

use Symfony\Component\HttpFoundation\Request;

require __DIR__.'/../vendor/autoload.php';
if (PHP_VERSION_ID < 70000) {
    include_once __DIR__.'/../var/bootstrap.php.cache';
}

$kernel = new AppKernel('prod', false);
if (PHP_VERSION_ID < 70000) {
    $kernel->loadClassCache();
}
//$kernel = new AppCache($kernel);

// When using the HttpCache, you need to call the method in your front controller instead of relying on the configuration parameter
//Request::enableHttpMethodParameterOverride();
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);

```

### File: web\app_dev.php
```php
<?php

use Symfony\Component\Debug\Debug;
use Symfony\Component\HttpFoundation\Request;

// If you don't want to setup permissions the proper way, just uncomment the following PHP line
// read https://symfony.com/doc/current/setup.html#checking-symfony-application-configuration-and-setup
// for more information
//umask(0000);

// This check prevents access to debug front controllers that are deployed by accident to production servers.
// Feel free to remove this, extend it, or make something more sophisticated.
if (isset($_SERVER['HTTP_CLIENT_IP'])
    || isset($_SERVER['HTTP_X_FORWARDED_FOR'])
    || !(in_array(@$_SERVER['REMOTE_ADDR'], ['127.0.0.1', '::1'], true) || PHP_SAPI === 'cli-server')
) {
    header('HTTP/1.0 403 Forbidden');
    exit('You are not allowed to access this file. Check '.basename(__FILE__).' for more information.');
}

require __DIR__.'/../vendor/autoload.php';
Debug::enable();

$kernel = new AppKernel('dev', true);
if (PHP_VERSION_ID < 70000) {
    $kernel->loadClassCache();
}
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);

```

### File: web\config.php
```php
<?php

/*
 * ************** CAUTION **************
 *
 * DO NOT EDIT THIS FILE as it will be overridden by Composer as part of
 * the installation/update process. The original file resides in the
 * SensioDistributionBundle.
 *
 * ************** CAUTION **************
 */

if (!isset($_SERVER['HTTP_HOST'])) {
    exit("This script cannot be run from the CLI. Run it from a browser.\n");
}

if (!in_array(@$_SERVER['REMOTE_ADDR'], array(
    '127.0.0.1',
    '::1',
))) {
    header('HTTP/1.0 403 Forbidden');
    exit('This script is only accessible from localhost.');
}

require_once dirname(__FILE__).'/../var/SymfonyRequirements.php';

$symfonyRequirements = new SymfonyRequirements();

$majorProblems = $symfonyRequirements->getFailedRequirements();
$minorProblems = $symfonyRequirements->getFailedRecommendations();
$hasMajorProblems = (bool) count($majorProblems);
$hasMinorProblems = (bool) count($minorProblems);

?>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <meta name="robots" content="noindex,nofollow" />
        <title>Symfony Configuration Checker</title>
        <style>
            /* styles copied from symfony framework bundle */
            html {
                background: #eee;
            }
            body {
                font: 11px Verdana, Arial, sans-serif;
                color: #333;
            }
            .sf-reset, .sf-reset .block, .sf-reset #message {
                margin: auto;
            }
            img {
                border: 0;
            }
            .clear {
                clear: both;
                height: 0;
                font-size: 0;
                line-height: 0;
            }
            .clear-fix:after {
                content: "\0020";
                display: block;
                height: 0;
                clear: both;
                visibility: hidden;
            }
            .clear-fix {
                display: inline-block;
            }
            * html .clear-fix {
                height: 1%;
            }
            .clear-fix {
                display: block;
            }
            .header {
                padding: 30px 30px 20px 30px;
            }
            .header-logo {
                float: left;
            }
            .search {
                float: right;
                padding-top: 20px;
            }
            .search label {
                line-height: 28px;
                vertical-align: middle;
            }
            .search input {
                width: 195px;
                font-size: 12px;
                border: 1px solid #dadada;
                background: #fff url(data:image/gif;base64,R0lGODlhAQAFAKIAAPX19e/v7/39/fr6+urq6gAAAAAAAAAAACH5BAAAAAAALAAAAAABAAUAAAMESAEjCQA7) repeat-x left top;
                padding: 5px 6px;
                color: #565656;
            }
            .search input[type="search"] {
                -webkit-appearance: textfield;
            }
            #content {
                width: 970px;
                margin: 0 auto;
            }
            #content pre {
                white-space: normal;
                font-family: Arial, Helvetica, sans-serif;
            }

            /*
            Copyright (c) 2010, Yahoo! Inc. All rights reserved.
            Code licensed under the BSD License:
            http://developer.yahoo.com/yui/license.html
            version: 3.1.2
            build: 56
            */
            .sf-reset div,.sf-reset dl,.sf-reset dt,.sf-reset dd,.sf-reset ul,.sf-reset ol,.sf-reset li,.sf-reset h1,.sf-reset h2,.sf-reset h3,.sf-reset h4,.sf-reset h5,.sf-reset h6,.sf-reset pre,.sf-reset code,.sf-reset form,.sf-reset fieldset,.sf-reset legend,.sf-reset input,.sf-reset textarea,.sf-reset p,.sf-reset blockquote,.sf-reset th,.sf-reset td{margin:0;padding:0;}.sf-reset table{border-collapse:collapse;border-spacing:0;}.sf-reset fieldset,.sf-reset img{border:0;}.sf-reset address,.sf-reset caption,.sf-reset cite,.sf-reset code,.sf-reset dfn,.sf-reset em,.sf-reset strong,.sf-reset th,.sf-reset var{font-style:normal;font-weight:normal;}.sf-reset li{list-style:none;}.sf-reset caption,.sf-reset th{text-align:left;}.sf-reset h1,.sf-reset h2,.sf-reset h3,.sf-reset h4,.sf-reset h5,.sf-reset h6{font-size:100%;font-weight:normal;}.sf-reset q:before,.sf-reset q:after{content:'';}.sf-reset abbr,.sf-reset acronym{border:0;font-variant:normal;}.sf-reset sup{vertical-align:text-top;}.sf-reset sub{vertical-align:text-bottom;}.sf-reset input,.sf-reset textarea,.sf-reset select{font-family:inherit;font-size:inherit;font-weight:inherit;}.sf-reset input,.sf-reset textarea,.sf-reset select{font-size:100%;}.sf-reset legend{color:#000;}
            .sf-reset abbr {
                border-bottom: 1px dotted #000;
                cursor: help;
            }
            .sf-reset p {
                font-size: 14px;
                line-height: 20px;
                padding-bottom: 20px;
            }
            .sf-reset strong {
                color: #313131;
                font-weight: bold;
            }
            .sf-reset a {
                color: #6c6159;
            }
            .sf-reset a img {
                border: none;
            }
            .sf-reset a:hover {
                text-decoration: underline;
            }
            .sf-reset em {
                font-style: italic;
            }
            .sf-reset h2,
            .sf-reset h3 {
                font-weight: bold;
            }
            .sf-reset h1 {
                font-family: Georgia, "Times New Roman", Times, serif;
                font-size: 20px;
                color: #313131;
                word-wrap: break-word;
            }
            .sf-reset li {
                padding-bottom: 10px;
            }
            .sf-reset .block {
                -moz-border-radius: 16px;
                -webkit-border-radius: 16px;
                border-radius: 16px;
                margin-bottom: 20px;
                background-color: #FFFFFF;
                border: 1px solid #dfdfdf;
                padding: 40px 50px;
                word-break: break-all;
            }
            .sf-reset h2 {
                font-size: 16px;
                font-family: Arial, Helvetica, sans-serif;
            }
            .sf-reset li a {
                background: none;
                color: #868686;
                text-decoration: none;
            }
            .sf-reset li a:hover {
                background: none;
                color: #313131;
                text-decoration: underline;
            }
            .sf-reset ol {
                padding: 10px 0;
            }
            .sf-reset ol li {
                list-style: decimal;
                margin-left: 20px;
                padding: 2px;
                padding-bottom: 20px;
            }
            .sf-reset ol ol li {
                list-style-position: inside;
                margin-left: 0;
                white-space: nowrap;
                font-size: 12px;
                padding-bottom: 0;
            }
            .sf-reset li .selected {
                background-color: #ffd;
            }
            .sf-button {
                display: -moz-inline-box;
                display: inline-block;
                text-align: center;
                vertical-align: middle;
                border: 0;
                background: transparent none;
                text-transform: uppercase;
                cursor: pointer;
                font: bold 11px Arial, Helvetica, sans-serif;
            }
            .sf-button span {
                text-decoration: none;
                display: block;
                height: 28px;
                float: left;
            }
            .sf-button .border-l {
                text-decoration: none;
                display: block;
                height: 28px;
                float: left;
                padding: 0 0 0 7px;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAQtJREFUeNpiPHnyJAMakARiByDWYEGT8ADiYGVlZStubm5xlv///4MEQYoKZGRkQkRERLRYWVl5wYJQyXBZWdkwCQkJUxAHKgaWlAHSLqKiosb//v1DsYMFKGCvoqJiDmQzwXTAJYECulxcXNLoumCSoszMzDzoumDGghQwYZUECWIzkrAkSIIGOmlkLI10AiX//P379x8jIyMTNmPf/v79+ysLCwsvuiQoNi5//fr1Kch4dAyS3P/gwYMTQBP+wxwHw0xA4gkQ73v9+vUZdJ2w1Lf82bNn4iCHCQoKasHsZw4ODgbRIL8c+/Lly5M3b978Y2dn5wC6npkFLXnsAOKLjx49AmUHLYAAAwBoQubG016R5wAAAABJRU5ErkJggg==) no-repeat top left;
            }
            .sf-button .border-r {
                padding: 0 7px 0 0;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAR1JREFUeNpiPHnyZCMDA8MNID5gZmb2nAEJMH7//v3N169fX969e/cYkL8WqGAHXPLv37//QYzfv39/fvPmzbUnT56sAXInmJub/2H5/x8sx8DCwsIrISFhDmQyPX78+CmQXs70798/BmQsKipqBNTgdvz4cWkmkE5kDATMioqKZkCFdiwg1eiAi4tLGqhQF24nMmBmZuYEigth1QkEbEBxTlySYPvJkwSJ00AnjYylgU6gxB8g/oFVEphkvgLF32KNMmCCewYUv4qhEyj47+HDhyeBzIMYOoEp8CxQw56wsLAncJ1//vz5/P79+2svX74EJc2V4BT58+fPd8CE/QKYHMGJOiIiAp6oWW7evDkNSF8DZYfIyEiU7AAQYACJ2vxVdJW4eQAAAABJRU5ErkJggg==) right top no-repeat;
            }
            .sf-button .btn-bg {
                padding: 0 14px;
                color: #636363;
                line-height: 28px;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAcCAYAAACgXdXMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAClJREFUeNpiPnny5EKGf//+/Wf6//8/A4QAcrGzKCZwGc9sa2urBBBgAIbDUoYVp9lmAAAAAElFTkSuQmCC) repeat-x top left;
            }
            .sf-button:hover .border-l,
            .sf-button-selected .border-l {
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAR9JREFUeNpi/P//PwMyOHfunDqQSgNiexZkibNnzxYBqZa3HOs5v7PcYQBLnjlzhg1IbfzIdsTjA/t+ht9Mr8GKwZL//v3r+sB+0OMN+zqIEf8gFMvJkyd1gXTOa9YNDP//otrPAtSV/Jp9HfPff78Z0AEL0LUeXxivMfxD0wXTqfjj/2ugkf+wSrL9/YtpJEyS4S8WI5Ek/+GR/POPFjr//cenE6/kP9q4Fo/kr39/mdj+M/zFkGQCSj5i+ccPjLJ/GBgkuYOHQR1sNDpmAkb2LBmWwL///zKCIxwZM0VHR18G6p4uxeLLAA4tJMwEshiou1iMxXaHLGswA+t/YbhORuQUv2DBAnCifvxzI+enP3dQJUFg/vz5sOzgBBBgAPxX9j0YnH4JAAAAAElFTkSuQmCC) no-repeat top left;
            }
            .sf-button:hover .border-r,
            .sf-button-selected .border-r {
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAT5JREFUeNpiPHv27BkGBoaDQDzLyMjoJgMSYHrM3WX8hn1d0f///88DFRYhSzIuv2X5H8Rg/SfKIPDTkYH/l80OINffxMTkF9O/f/8ZQPgnwyuGl+wrGd6x7vf49+9fO9jYf3+Bkkj4NesmBqAV+SdPntQC6vzHgIz//gOawbqOGchOxtAJwp8Zr4F0e7D8/fuPAR38/P8eZIo0yz8skv8YvoIk+YE6/zNgAyD7sRqLkPzzjxY6/+HS+R+fTkZ8djLh08lCUCcuSWawJGbwMTGwg7zyBatX2Bj5QZKPsBrLzaICktzN8g/NWEYGZgYZjoC/wMiei5FMpFh8QPSU6Ojoy3Cd7EwiDBJsDgxiLNY7gLrKQGIsHAxSDHxAO2TZ/b8D+TVxcXF9MCtYtLiKLgDpfUDVsxITE1GyA0CAAQA2E/N8VuHyAAAAAABJRU5ErkJggg==) right top no-repeat;
            }
            .sf-button:hover .btn-bg,
            .sf-button-selected .btn-bg {
                color: #FFFFFF;
                text-shadow:0 1px 1px #6b9311;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAcCAIAAAAvP0KbAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAEFJREFUeNpiPnv2LNMdvlymf///M/37B8R/QfQ/MP33L4j+B6Qh7L9//sHpf2h8MA1V+w/KRjYLaDaLCU8vQIABAFO3TxZriO4yAAAAAElFTkSuQmCC) repeat-x top left;
            }

            /* styles copied from bundles/sensiodistribution/webconfigurator/css/install.css */
            body {
                font-size: 14px;
                font-family: "Lucida Sans Unicode", "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
            }
            .sf-reset h1.title {
                font-size: 45px;
                padding-bottom: 30px;
            }
            .sf-reset h2 {
                font-weight: bold;
                color: #FFFFFF;
                /* Font is reset to sans-serif (like body) */
                font-family: "Lucida Sans Unicode", "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
                margin-bottom: 10px;
                background-color: #aacd4e;
                padding: 2px 4px;
                display: inline-block;
                text-transform: uppercase;
            }
            .sf-reset ul a,
            .sf-reset ul a:hover {
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAICAYAAAAx8TU7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAFdJREFUeNpiYACBjjOhDEiACSggCKTLgXQ5TJARqhIkcReIKxgqTGYxwvV0nDEGkmeAOIwJySiQ4HsgvseIpGo3ELsCtZ9lRDIvDCiwhwHJPEFkJwEEGACq6hdnax8y1AAAAABJRU5ErkJggg==) no-repeat right 7px;
                padding-right: 10px;
            }
            .sf-reset ul, ol {
                padding-left: 20px;
            }
            .sf-reset li {
                padding-bottom: 18px;
            }
            .sf-reset ol li {
                list-style-type: decimal;
            }
            .sf-reset ul li {
                list-style-type: none;
            }
            .sf-reset .symfony-blocks-install {
                overflow: hidden;
            }
            .sf-reset .symfony-install-continue {
                font-size: 0.95em;
                padding-left: 0;
            }
            .sf-reset .symfony-install-continue li {
                padding-bottom: 10px;
            }
            .sf-reset .ok {
                color: #fff;
                font-family: "Lucida Sans Unicode", "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
                background-color: #6d6;
                padding: 10px;
                margin-bottom: 20px;
            }
            .sf-reset .ko {
                background-color: #d66;
            }
            .sf-reset p.help {
                padding: 12px 16px;
                word-break: break-word;
            }
            .version {
                text-align: right;
                font-size: 10px;
                margin-right: 20px;
            }
            .sf-reset a,
            .sf-reset li a {
                color: #08C;
                text-decoration: none;
            }
            .sf-reset a:hover,
            .sf-reset li a:hover {
                color: #08C;
                text-decoration: underline;
            }
            .sf-reset textarea {
                padding: 7px;
            }
        </style>
    </head>
    <body>
        <div id="content">
            <div class="header clear-fix">
                <div class="header-logo">
                    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALYAAAA+CAMAAACxzRGDAAAAUVBMVEX////Ly8yko6WLioxkYmVXVVkwLjLl5eWxsLJKSEzy8vJxcHLY2Ni+vb89Oz9XVVh+fH+Yl5n///+xsbLY2Nlxb3KkpKWXlph+fX+LiYy+vr/IZP61AAAAAXRSTlMAQObYZgAABRBJREFUeNrVmtuWoyAQRS1FEEQSzQU7//+hYxUiXsKQZLJWM+chsUloN+WhCuguYoKyY
... [TRUNCATED]
```

### File: web\robots.txt
```txt
# www.robotstxt.org/
# www.google.com/support/webmasters/bin/answer.py?hl=en&answer=156449

User-agent: *
Disallow:

```

### File: src\Application\Wishlist.php
```php
<?php

namespace Wishlist\Application;

use Money\Currency;
use Money\Money;
use Wishlist\Application\Assembler\ListWishDtoAssembler;
use Wishlist\Application\Dto\DepositDto;
use Wishlist\Application\Dto\NewWishDto;
use Wishlist\Domain\DepositId;
use Wishlist\Domain\Exception\InvalidIdentityException;
use Wishlist\Domain\Exception\WishNotFoundException;
use Wishlist\Domain\Expense;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishName;
use Wishlist\Domain\WishRepositoryInterface;

class Wishlist implements WishlistInterface
{
    private $wishes;
    private $currency;

    public function __construct(WishRepositoryInterface $wishes, Currency $currency)
    {
        $this->wishes = $wishes;
        $this->currency = $currency;
    }

    public function getWishesByPage(int $page, int $limit): array
    {
        $wishes = $this->wishes->slice($page * $limit, $limit);

        return (new ListWishDtoAssembler())->toArrayOfDto($wishes);
    }

    public function addNewWish(NewWishDto $dto): string
    {
        $wishId = WishId::next();
        $this->wishes->put($this->createWishFromIdAndDto($wishId, $dto));

        return $wishId->getId();
    }

    private function createWishFromIdAndDto(WishId $wishId, NewWishDto $dto): Wish
    {
        $wish = new Wish(
            $wishId,
            new WishName($dto->name),
            Expense::fromCurrencyAndScalars(
                $this->currency,
                $dto->price,
                $dto->fee,
                $dto->initialFund
            )
        );

        if ($dto->isPublished) {
            $wish->publish();
        }

        return $wish;
    }

    public function deposit(string $wishId, int $amount): DepositDto
    {
        $wish = $this->getWish($wishId);
        $deposit = $wish->deposit(new Money($amount, $this->currency));
        $this->wishes->put($wish);

        $dto = new DepositDto();
        $dto->depositId = $deposit->getId()->getId();
        $dto->amount = $deposit->getMoney()->getAmount();
        $dto->currency = $deposit->getMoney()->getCurrency();
        $dto->createdAt = $deposit->getDate()->format('d.m.Y H:i');

        return $dto;
    }

    public function withdraw(string $wishId, string $depositId): Money
    {
        $wish = $this->getWish($wishId);
        $wish->withdraw(DepositId::fromString($depositId));
        $this->wishes->put($wish);

        return $wish->getFund();
    }

    public function publish(string $wishId)
    {
        $wish = $this->getWish($wishId);
        $wish->publish();
        $this->wishes->put($wish);
    }

    public function unpublish(string $wishId)
    {
        $wish = $this->getWish($wishId);
        $wish->unpublish();
        $this->wishes->put($wish);
    }

    private function getWish(string $wishId): Wish
    {
        try {
            return $this->wishes->get(WishId::fromString($wishId));
        } catch (InvalidIdentityException $ex) {
            throw new WishNotFoundException($wishId);
        }
    }

    public function getTotalWishesNumber(): int
    {
        return $this->wishes->count();
    }
}

```

### File: src\Application\WishlistInterface.php
```php
<?php

namespace Wishlist\Application;

use Money\Money;
use Wishlist\Application\Dto\DepositDto;
use Wishlist\Application\Dto\NewWishDto;

interface WishlistInterface
{
    public function addNewWish(NewWishDto $dto): string;
    public function deposit(string $wishId, int $amount): DepositDto;
    public function withdraw(string $wishId, string $depositId): Money;
    public function publish(string $wishId);
    public function unpublish(string $wishId);
    public function getWishesByPage(int $page, int $limit): array;
    public function getTotalWishesNumber(): int;
}

```

### File: src\Domain\AbstractId.php
```php
<?php

namespace Wishlist\Domain;

use Ramsey\Uuid\Exception\InvalidUuidStringException;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;
use Wishlist\Domain\Exception\InvalidIdentityException;

abstract class AbstractId
{
    protected $id;

    private function __construct(UuidInterface $id)
    {
        $this->id = $id;
    }

    public static function fromString(string $id)
    {
        try {
            return new static(Uuid::fromString($id));
        } catch (InvalidUuidStringException $exception) {
            throw new InvalidIdentityException($id);
        }
    }

    public static function next()
    {
        return new static(Uuid::uuid4());
    }

    public function getId(): string
    {
        return $this->id->toString();
    }

    public function equalTo(AbstractId $id): bool
    {
        return $this->getId() === $id->getId() &&
               get_class($this) === get_class($id);
    }

    public function __toString(): string
    {
        return $this->getId();
    }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
