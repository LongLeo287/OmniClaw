---
id: oas
type: knowledge
owner: OA_Triage
---
# oas
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "license": "BSD-3-Clause",
  "devDependencies": {
    "@babel/runtime": "^7.12.5",
    "babel-preset-env": "^1.7.0",
    "eslint": "^7.8.1",
    "jsdoc-to-markdown": "^7.0.1",
    "lerna": "^4.0.0",
    "mocha": "^9.0.0",
    "should": "^13.2.1",
    "webpack": "^5.6.0",
    "webpack-bundle-analyzer": "^4.4.2",
    "webpack-cli": "^4.2.0",
    "yaml": "^1.10.0"
  },
  "name": "oas-kit",
  "description": "This is the mono-repo for swagger2openapi and related projects",
  "version": "5.3.0",
  "main": "index.js",
  "directories": {
    "test": "test"
  },
  "funding": "https://www.linode.com/?r=5734be467cc501b23267cf66d451bc339042ddfa",
  "scripts": {
    "test": "npx mocha",
    "lint": "npx eslint packages/*/*.js test/*.js",
    "webpack": "npx webpack",
    "webpack-converter": "npx webpack --config webpack.converter.js",
    "webpack-validator": "npx webpack --config webpack.validator.js",
    "webpack-reftools": "npx webpack --config webpack.reftools.js",
    "audits": "npx lerna exec --no-bail npm audit",
    "outdated": "npx lerna exec --no-bail npm outdated",
    "rescue": "npx lerna publish from-package"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/mermade/oas-kit.git"
  },
  "author": "Mike Ralphson",
  "bugs": {
    "url": "https://github.com/mermade/oas-kit/issues"
  },
  "homepage": "https://github.com/mermade/oas-kit#readme",
  "keywords": [
    "openapi",
    "oas",
    "swagger"
  ],
  "dependencies": {}
}

```

### File: README.md
```md
# OAS-Kit

This is the mono-repo for the following related projects

* [swagger2openapi](packages/swagger2openapi/README.md)
* [oas-validator](packages/oas-validator/README.md)
* [oas-linter](packages/oas-linter/README.md)
* [oas-resolver](packages/oas-resolver/README.md)
* [oas-schema-walker](packages/oas-schema-walker/README.md)
* [oas-kit-common](packages/oas-kit-common/README.md)
* [reftools](packages/reftools/README.md)

## Documentation

* [Main site](https://mermade.github.io/oas-kit)
* [CHANGELOG](https://github.com/Mermade/oas-kit/blob/master/CHANGELOG.md#change-log)

## Online converter/validator

* [OpenAPI-webconverter](https://mermade.org.uk/openapi-converter)

## Supported Node.js versions

Any LTS version. It is **not** recommended to use Node.js 12.17.x,12.18.x or 12.19.x due to an [http2 bug](https://github.com/nodejs/node/issues/28001).

## Development

* clone the repository
* `npm i` in the top level directory
* `npx lerna bootstrap`

Please try and keep commits related to a single package or piece of functionality. Please review the
[CONTRIBUTING.md](CONTRIBUTING.md) for additional details.

## Supporting development

* [APIs.guru open-collective](https://opencollective.com/openapi-directory)
* [Linode VPS referral link](https://www.linode.com/?r=5734be467cc501b23267cf66d451bc339042ddfa)

```

### File: docs\README.md
```md
# OAS-Kit

This is the documentation site for OAS-Kit, a collection of packages which comprise an OpenAPI 2.0 to 3.0.x converter, a resolver, a validator, a schema-walker and a linter.

## Project READMEs

* [main README](https://github.com/Mermade/oas-kit/blob/master/README.md)
* [swagger2openapi README](https://github.com/Mermade/oas-kit/blob/master/packages/swagger2openapi/README.md)
* [oas-validator README](https://github.com/Mermade/oas-kit/blob/master/packages/oas-validator/README.md)
* [oas-resolver README](https://github.com/Mermade/oas-kit/blob/master/packages/oas-resolver/README.md)
* [oas-linter README](https://github.com/Mermade/oas-kit/blob/master/packages/oas-linter/README.md)
* [oas-schema-walker README](https://github.com/Mermade/oas-kit/blob/master/packages/oas-schema-walker/README.md)
* [reftools README](https://github.com/Mermade/oas-kit/blob/master/packages/reftools/README.md)

## Implementation documentation

* [Use in the browser](browser.md)
* [Specification extensions supported](extensions.md)
* [Details on de-resolution information](externals.md)
* [Details on custom protocol/scheme handlers](handlers.md)
* [Linter default rule descriptions](default-rules.md)
* [Linter rule DSL documentation](linter-rules.md)
* [The options object](options.md)

## OAS-Kit Wiki

* [Including contributed Linter rules](https://github.com/Mermade/oas-kit/wiki)

## TODO (help wanted)

* Documentation/example of custom resource filters

```

### File: .eslintrc.json
```json
{
    "env": {
        "es6": true,
        "node": true,
        "mocha": true
    },
    "extends": "eslint:recommended",
    "parserOptions": {
        "ecmaVersion": 2017
    },
    "rules": {
        "accessor-pairs": "error",
        "array-bracket-spacing": [
            "off",
            "never"
        ],
        "array-callback-return": "error",
        "arrow-body-style": "off",
        "arrow-parens": [
            "off",
            "as-needed"
        ],
        "arrow-spacing": [
            "error",
            {
                "after": true,
                "before": true
            }
        ],
        "block-scoped-var": "off",
        "block-spacing": "off",
        "brace-style": [
            "off",
            "stroustrup"
        ],
        "callback-return": "off",
        "camelcase": "off",
        "class-methods-use-this": "error",
        "comma-dangle": "error",
        "comma-spacing": "off",
        "comma-style": [
            "error",
            "last"
        ],
        "complexity": "off",
        "computed-property-spacing": [
            "error",
            "never"
        ],
        "consistent-return": "off",
        "consistent-this": "error",
        "curly": "off",
        "default-case": "error",
        "dot-location": [
            "off",
            "property"
        ],
        "dot-notation": [
            "error",
            {
                "allowKeywords": true
            }
        ],
        "eol-last": "error",
        "eqeqeq": "off",
        "func-call-spacing": "off",
        "func-name-matching": "off",
        "func-names": "off",
        "func-style": [
            "off",
            "declaration"
        ],
        "generator-star-spacing": "off",
        "global-require": "off",
        "guard-for-in": "off",
        "handle-callback-err": "off",
        "id-blacklist": "error",
        "id-length": "off",
        "id-match": "error",
        "indent": "off",
        "init-declarations": "off",
        "jsx-quotes": "error",
        "key-spacing": "off",
        "keyword-spacing": ["error", { "after": true }],
        "line-comment-position": "off",
        "linebreak-style": [
            "error",
            "unix"
        ],
        "lines-around-comment": "off",
        "lines-around-directive": "off",
        "max-depth": "off",
        "max-len": "off",
        "max-lines": "off",
        "max-nested-callbacks": "error",
        "max-params": "off",
        "max-statements": "off",
        "max-statements-per-line": "off",
        "multiline-ternary": [
            "off",
            "never"
        ],
        "new-parens": "error",
        "newline-after-var": "off",
        "newline-before-return": "off",
        "newline-per-chained-call": "off",
        "no-alert": "error",
        "no-array-constructor": "error",
        "no-async-promise-executor": "warn",
        "no-bitwise": "off",
        "no-caller": "error",
        "no-catch-shadow": "off",
        "no-confusing-arrow": "error",
        "no-console": "off",
        "no-continue": "off",
        "no-div-regex": "error",
        "no-duplicate-imports": "error",
        "no-else-return": "off",
        "no-empty": [
            "warn",
            {
                "allowEmptyCatch": true
            }
        ],
        "no-empty-function": "off",
        "no-eq-null": "error",
        "no-eval": "error",
        "no-extend-native": "off",
        "no-extra-bind": "error",
        "no-extra-label": "error",
        "no-extra-parens": "off",
        "no-floating-decimal": "error",
        "no-global-assign": "error",
        "no-implicit-globals": "error",
        "no-implied-eval": "error",
        "no-inline-comments": "off",
        "no-inner-declarations": [
            "error",
            "functions"
        ],
        "no-invalid-this": "off",
        "no-iterator": "error",
        "no-label-var": "error",
        "no-labels": "error",
        "no-lone-blocks": "error",
        "no-lonely-if": "off",
        "no-loop-func": "off",
        "no-magic-numbers": "off",
        "no-mixed-operators": "error",
        "no-mixed-requires": "error",
        "no-multi-spaces": "off",
        "no-multi-str": "error",
        "no-multiple-empty-lines": "error",
        "no-negated-condition": "error",
        "no-nested-ternary": "off",
        "no-new": "error",
        "no-new-func": "error",
        "no-new-object": "error",
        "no-new-require": "error",
        "no-new-wrappers": "error",
        "no-octal-escape": "error",
        "no-param-reassign": "off",
        "no-path-concat": "error",
        "no-plusplus": "off",
        "no-process-env": "off",
        "no-process-exit": "off",
        "no-proto": "error",
        "no-prototype-builtins": "error",
        "no-restricted-globals": "error",
        "no-restricted-imports": "error",
        "no-restricted-modules": "error",
        "no-restricted-properties": "error",
        "no-restricted-syntax": "error",
        "no-return-assign": "off",
        "no-script-url": "error",
        "no-self-compare": "error",
        "no-sequences": "error",
        "no-shadow": "off",
        "no-shadow-restricted-names": "error",
        "no-spaced-func": "off",
        "no-sync": "off",
        "no-tabs": "off",
        "no-template-curly-in-string": "error",
        "no-ternary": "off",
        "no-throw-literal": "error",
        "no-trailing-spaces": "error",
        "no-undef-init": "error",
        "no-undefined": "warn",
        "no-underscore-dangle": "off",
        "no-unmodified-loop-condition": "error",
        "no-unneeded-ternary": [
            "error",
            {
                "defaultAssignment": true
            }
        ],
        "no-unsafe-negation": "error",
        "no-unused-expressions": "error",
        "no-unused-vars": "off",
        "no-use-before-define": "off",
        "no-useless-call": "error",
        "no-useless-computed-key": "error",
        "no-useless-concat": "off",
        "no-useless-constructor": "error",
        "no-useless-escape": "off",
        "no-useless-rename": "error",
        "no-var": "off",
        "no-void": "error",
        "no-warning-comments": "off",
        "no-whitespace-before-property": "error",
        "no-with": "error",
        "object-curly-newline": "off",
        "object-curly-spacing": "off",
        "object-property-newline": [
            "off",
            {
                "allowMultiplePropertiesPerLine": true
            }
        ],
        "object-shorthand": "off",
        "one-var": "off",
        "one-var-declaration-per-line": "error",
        "operator-assignment": "off",
        "operator-linebreak": "off",
        "padded-blocks": "off",
        "prefer-arrow-callback": "off",
        "prefer-const": "off",
        "prefer-numeric-literals": "error",
        "prefer-reflect": "off",
        "prefer-rest-params": "error",
        "prefer-spread": "error",
        "prefer-template": "off",
        "quote-props": "off",
        "quotes": "off",
        "radix": "error",
        "require-jsdoc": "off",
        "require-yield": "off",
        "rest-spread-spacing": "off",
        "semi": "off",
        "semi-spacing": "off",
        "sort-imports": "error",
        "sort-keys": "off",
        "sort-vars": "error",
        "space-before-blocks": "off",
        "space-before-function-paren": "off",
        "space-in-parens": [
            "error",
            "never"
        ],
        "space-infix-ops": "off",
        "space-unary-ops": "error",
        "spaced-comment": "off",
        "strict": "error",
        "symbol-description": "error",
        "template-curly-spacing": "error",
        "unicode-bom": [
            "error",
            "never"
        ],
        "valid-jsdoc": "off",
        "vars-on-top": "off",
        "wrap-iife": "error",
        "wrap-regex": "off",
        "yield-star-spacing": "error",
        "yoda": [
            "error",
            "never"
        ]
    }
}

```

### File: CHANGELOG.md
```md
# Change Log

## swagger2openapi v7.0 and oas-validator v5.0

* remove use of `ajv` for fallback schema validation

## swagger2openapi v6.1.0 and oas-resolver v2.4.0

New properties on the `options` object:

* `fetch` - to override the built-in `fetch` function
* `fetchOptions` - additional options to be passed to the `fetch` function

## swagger2openapi v6.0.0 and oas-validator v4.0.0

* Converter will now error out if passed in input containing YAML anchors/aliases. To bypass this check, pass the `--anchors` option or set `options.anchors` to `true`.
* Validator method `validateSync` has now been renamed `validateInner` as it (still) returns a Promise or calls a given callback.

```

### File: CONTRIBUTING.md
```md
# Contributing

First of all, many thanks for considering making a contribution to this project.

# Submitting PRs

Please run the tests before submitting your pull request.

* `npm run lint`
* `npm test`

# Known issues
[GitHub search](https://github.com/Mermade/oas-kit/search?utf8=%E2%9C%93&q=fixme+language%3Ajavascript&type=)

```

### File: lerna.json
```json
{
  "packages": [
    "packages/*"
  ],
  "version": "independent"
}

```

### File: webpack.config.js
```js
'use strict';

const webpack = require('webpack');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
    mode: 'production',
    performance: { hints: false },
    plugins: [
      new BundleAnalyzerPlugin(),
      new webpack.NormalModuleReplacementPlugin(/node_modules.should/, resource => {
        const components = resource.request.split('/');
        for (let i=0;i<components.length;i++) {
            if (components[i].startsWith('oas-')) {
                components[i] = 'swagger2openapi';
            }
        }
		resource.request = components.join('/');
      }),
      new webpack.NormalModuleReplacementPlugin(/node_modules.yaml/, resource => {
        const components = resource.request.split('/');
        for (let i=0;i<components.length;i++) {
            if (components[i].startsWith('oas-')) {
                components[i] = 'swagger2openapi';
            }
        }
		resource.request = components.join('/');
      })
    ],
    optimization: {
        splitChunks: {
            cacheGroups: {
                commons: {
                    test: /[\\/]node_modules[\\/]/,
                    name: 'oas-lib',
                    chunks: 'all'
                }
            }
        }
    },
    resolve: {
      fallback: {
        fs: false
      }
    },
    entry: {
        converter: './packages/swagger2openapi/index.js',
        validator: './packages/oas-validator/index.js',
        resolver: './packages/oas-resolver/index.js',
        linter: './packages/oas-linter/index.js',
        walker: './packages/oas-schema-walker/index.js'
    },
    output: {
        filename: '[name].min.js'
    }
};

```

### File: webpack.converter.js
```js
'use strict';

const webpack = require('webpack');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
    mode: 'production',
    performance: { hints: false },
    plugins: [
      new BundleAnalyzerPlugin(),
      new webpack.NormalModuleReplacementPlugin(/node_modules.yaml/, resource => {
        const components = resource.request.split('/');
        for (let i=0;i<components.length;i++) {
            if (components[i].startsWith('oas-')) {
                components[i] = 'swagger2openapi';
            }
        }
		resource.request = components.join('/');
      })
    ],
    optimization: {
        splitChunks: {
            cacheGroups: {
                commons: {
                    test: /[\\/]node_modules[\\/]/,
                    name: 'converter-lib',
                    chunks: 'all'
                }
            }
        }
    },
    resolve: {
      fallback: {
        fs: false
      }
    },
    entry: {
        converterOnly: './packages/swagger2openapi/index.js'
    },
    output: {
        filename: '[name].min.js'
    }
};

```

### File: webpack.reftools.js
```js
'use strict';

const webpack = require('webpack');

module.exports = {
    mode: 'production',
    plugins: [
    ],
    resolve: {
      fallback: {
        fs: false
      }
    },
    entry: {
        recurse: './packages/reftools/lib/recurse.js',
        clone: './packages/reftools/lib/clone.js',
        deref: './packages/reftools/lib/dereference.js',
        reref: './packages/reftools/lib/reref.js'
    },
    output: {
        filename: '[name].min.js',
        libraryTarget: 'umd'
    }
};

```

### File: webpack.validator.js
```js
'use strict';

const webpack = require('webpack');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
    mode: 'production',
    performance: { hints: false },
    plugins: [
      new BundleAnalyzerPlugin(),
      new webpack.NormalModuleReplacementPlugin(/node_modules.should/, resource => {
        const components = resource.request.split('/');
        for (let i=0;i<components.length;i++) {
            if (components[i].match(/^oas-[rl]/)) {
                components[i] = 'oas-validator';
            }
        }
		resource.request = components.join('/');
      }),
      new webpack.NormalModuleReplacementPlugin(/node_modules.yaml/, resource => {
        const components = resource.request.split('/');
        for (let i=0;i<components.length;i++) {
            if (components[i].match(/^oas-[rl]/)) {
                components[i] = 'oas-validator';
            }
        }
		resource.request = components.join('/');
      })
    ],
    optimization: {
        splitChunks: {
            cacheGroups: {
                commons: {
                    test: /[\\/]node_modules[\\/]/,
                    name: 'validator-lib',
                    chunks: 'all'
                }
            }
        }
    },
    resolve: {
      fallback: {
        fs: false
      }
    },
    entry: {
        validatorOnly: './packages/oas-validator/index.js'
    },
    output: {
        filename: '[name].min.js'
    }
};

```

### File: .github\ISSUE_TEMPLATE.md
```md
<!--- Provide a general summary of the issue in the Title above -->

### Checklist

<!-- delete as appropriate -->

- [ ] Conversion: I have checked my source definition is valid OpenAPI 2.0
- [ ] Conversion: On valid OpenAPI 2.0 input, the conversion looks wrong
- [ ] Validation: I believe my source definition is valid OpenAPI 3.0.x but the validator complains
- [ ] Validation: I believe my source definition is invalid OpenAPI 3.0.x but the validator does not complain
- [ ] Linting issue
- [ ] Resolver issue

<!--
For validating OpenAPI 2.0 definitions, we recommend the [bigstickcarpet swagger validator](http://bigstickcarpet.com/swagger-parser/www/index.html)
-->

### Detailed Description
<!--- Provide a detailed description of the bug, change or feature you are reporting -->


#### Other stuff

<!-- Please also let us know how you found out about OAS-Kit, and what version you are running -->



```

### File: bin\jsdocToMarkdown.sh
```sh
#!/bin/sh

echo '# OAS-Schema-Walker' > packages/oas-schema-walker/README.md
echo '' >> echo '# OAS-Schema-Walker' > packages/oas-schema-walker/README.md
npx jsdoc-to-markdown packages/oas-schema-walker/index.js >> packages/oas-schema-walker/README.md

echo '# RefTools' > packages/reftools/README.md
echo '' >> packages/reftools/README.md
npx jsdoc-to-markdown packages/reftools/lib/*.js >> packages/reftools/README.md


```

### File: bin\setflags.sh
```sh
#!/bin/sh
if [ "$TRAVIS_NODE_VERSION" -eq "4" ] ; then 
  export nflags="--harmony"
fi
echo flags: $nflags

```

### File: bin\updateCoverage.sh
```sh
#!/bin/sh
cat coverage/lcov.info | node node_modules/coveralls/bin/coveralls.js

```

### File: docs\browser.md
```md
# Browser support

## Webpack v4

Many thanks to @RomanGotsiy for getting these sizes down somewhat.
Further size reductions were made by replacing `js-yaml` with `yaml` and
forcing `webpack` to deduplicate across packages, inspired by @mrin9.

```shell
$ npm run webpack
$ ls -lh dist
total 564K
-rw-r--r-- 1 mike mike  42K Jan  7 10:09 converter.min.js
-rw-r--r-- 1 mike mike 5.0K Jan  7 10:09 linter.min.js
-rw-r--r-- 1 mike mike 406K Jan  7 10:09 oas-lib.min.js
-rw-r--r-- 1 mike mike  13K Jan  7 10:09 resolver.min.js
-rw-r--r-- 1 mike mike  82K Jan  7 10:09 validator.min.js
-rw-r--r-- 1 mike mike 2.5K Jan  7 10:09 walker.min.js
```

The whole suite is therefore around 149K gzipped.

The converter only is:

```shell
-rw-r--r-- 1 mike mike 172K Jan  7 09:41 dist/converter-lib.min.js
-rw-r--r-- 1 mike mike  42K Jan  7 09:41 dist/converterOnly.min.js
```

And the validator only is:

```shell
-rw-r--r-- 1 mike mike 359K Jan  7 09:40 dist/validator-lib.min.js
-rw-r--r-- 1 mike mike  82K Jan  7 09:40 dist/validatorOnly.min.js
```

You can also build key parts of `reftools` into browser libraries by using `npm run webpack-reftools`.

## Browserify

Please see [api-spec-converter](https://github.com/LucyBot-Inc/api-spec-converter/) for setup or to use this [bundle](https://github.com/LucyBot-Inc/api-spec-converter/blob/master/dist/api-spec-converter.js).

Size: 8.45M

```

### File: docs\default-rules.md
```md
---

# OAS-Kit Default Linter Rules

<table class="table table-striped table-inverted">
  <thead>
    <tr>
      <td>Name</td>
      <td>OpenAPI Object</td>
      <td>Description</td>
    </tr>
  </thead>
  <tbody>
  {% for rule in site.data.defaultrules.default %}
  <tr>
    <td id="{{ rule.name }}">
      <a href="#{{ rule.name }}">{{ rule.name }}</a>
    </td>
    <td>
        {% if rule.object == "*" %}
        <em>everything</em>
        {% else %}
        <a href="https://spec.openapis.org/oas/v3.0.3.html#{{ rule.object }}-object">{{ rule.object }}</a>
        {% endif %}
    </td>
    <td>{{ rule.description }}</td>
  </tr>
  <!-- <tr>
    <td colspan=3>{{ rule.more | markdownify }}</td>
  </tr> -->
  {% endfor %}
  </tbody>
</table>


```

### File: docs\extensions.md
```md
# Specification (Vendor) Extensions

Specification Extension|Vendor|Conversion Performed
|---|---|---|
x-ms-paths|[Microsoft](https://github.com/Azure/autorest/tree/master/docs/extensions)|Treated as an analogue of the `openapi.paths` object
x-ms-skip-url-encoding|[Microsoft](https://github.com/Azure/autorest/tree/master/docs/extensions)|For query parameters, converted to `allowReserved:true`
x-ms-odata|[Microsoft](https://github.com/Azure/autorest/tree/master/docs/extensions)|References to `#/definitions/` are updated to `#/components/schemas`
x-ms-parameterized-host|[Microsoft](https://github.com/Azure/autorest/tree/master/docs/extensions)|Converted into server entry
x-amazon-apigateway-any-method|[Amazon](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html)|Treated as an analogue of the `operation Object`
x-servers|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|At root, path and operation, converted to `servers`
x-anyOf|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|Within schemas, converted to `anyOf`
x-oneOf|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|Within schemas, converted to `oneOf`
x-not|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|Within schemas, converted to `not`
x-required|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|Within schemas, concatenated with `required`
x-deprecated|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|Within parameters, converted to `deprecated`
x-links|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|At root and within responses, converted to `links`/`components/links`
x-callbacks|[swaggerplusplus](https://github.com/mermade/swaggerplusplus)|At root and within operations, converted to `callbacks`/`components/callbacks`
x-example|[apiary](https://help.apiary.io/api_101/swagger-extensions/#x-example)|Within parameters, converted to `example`

See also [APIMatic extensions](https://docs.apimatic.io/advanced/swagger-server-configuration-extensions/)

```

### File: docs\externals.md
```md
# Externals structure documentation

`options.externals` is an array of Objects containing the following properties:

Name|Type|Description
|---|---|---|
context|String|A JSON Pointer containing the path to the containing property which was resolved
$ref|String|The original `$ref` property
original|Object|The original Swagger 2.0 version of the resolved reference
updated|Object|The OpenAPI 3.0 version of the resolved reference
source|String|The resolved source of the external `$ref`

## Example

````json
[
  {
    "context": "#/paths/~1subscriptions~1{subscriptionId}~1providers~1Microsoft.Commerce~1RateCard/get/x-ms-examples/GetRateCard",
    "$ref": "../examples/GetRatecard.json",
    "source": "https://raw.githubusercontent.com/Azure/azure-rest-api-specs/2fb9a0b3b902335ff0b0033711c234431931ec9d/specification/commerce/resource-manager/Microsoft.Commerce/2015-06-01-preview/examples/GetRatecard.json",
    "original": {
      "title": "Get RateCard",
      "parameters": {
        "subscriptionId": "6d61cc05-8f8f-4916-b1b9-f1d9c25aae27",
        "api-version": "2015-06-01-preview",
        "$filter": "OfferDurableId eq 'MS-AZR-0003P' and Currency eq 'USD' and Locale eq 'en-US' and RegionInfo eq 'US'"
      },
      "responses": {
        "200": {
          "body": {
            "OfferTerms": [],
            "Meters": [
              {
                "EffectiveDate": "2017-09-01T00:00:00Z",
                "IncludedQuantity": 0,
                "MeterCategory": "Test Category",
                "MeterId": "1d7518e5-bc2f-4a93-9057-1b3047856645",
                "MeterName": "Test Meter",
                "MeterRates": {
                  "0": 1.99,
                  "100": 0.99
                },
                "MeterRegion": "US West",
                "MeterSubCategory": "Test Subcategory",
                "MeterTags": [
                  "Third Party"
                ],
                "Unit": "Hours"
              }
            ]
          }
        }
      }
    },
    "updated": {
      "title": "Get RateCard",
      "parameters": {
        "subscriptionId": "6d61cc05-8f8f-4916-b1b9-f1d9c25aae27",
        "api-version": "2015-06-01-preview",
        "$filter": "OfferDurableId eq 'MS-AZR-0003P' and Currency eq 'USD' and Locale eq 'en-US' and RegionInfo eq 'US'"
      },
      "responses": {
        "200": {
          "body": {
            "OfferTerms": [],
            "Meters": [
              {
                "EffectiveDate": "2017-09-01T00:00:00Z",
                "IncludedQuantity": 0,
                "MeterCategory": "Test Category",
                "MeterId": "1d7518e5-bc2f-4a93-9057-1b3047856645",
                "MeterName": "Test Meter",
                "MeterRates": {
                  "0": 1.99,
                  "100": 0.99
                },
                "MeterRegion": "US West",
                "MeterSubCategory": "Test Subcategory",
                "MeterTags": [
                  "Third Party"
                ],
                "Unit": "Hours"
              }
            ]
          }
        }
      }
    }
  }
]
````

```

### File: docs\handlers.md
```md
# Protocol/Scheme handlers

You can create your own protocol/[scheme](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml) 
handlers for external references. You can also override the default `http:`, `https:` and `file:` handlers if necessary.

Examples of custom scheme handlers might be `root:` or `parent:` for accessing the referring
parts of the definition, or a `ssh:` handler for secure retrieval.

## Example

```javascript
const util = require('util');
const converter = require('./index.js');

function cache(base,pointer,fragment,options) {
    if (options.verbose) console.log('Cache handler called',base,pointer,fragment);
    return new Promise(function(res,rej){
        res(...);
    });
}

converter.convertFile('./test.yaml',{
    handlers: { 'cache:': cache },
    resolve: true,
    source: './',
    verbose: true}, function(err,options){
        if (err) console.warn(util.inspect(err))
        else console.log(util.inspect(options.openapi));
    });
```

```

### File: docs\linter-rules.md
```md
# Linter rules format

## Rules file format

A rules file is a YAML (or JSON) formatted file, containing an object, with a `rules` property, which is an array of `rule` objects.

There is a `require` property (type `string`) at the top level, which is used for rule-set chaining.

The `url` property can be used as the base for looking up rule documentation, the `rule-name` value should be appended as a fragment-id. The `url` property may be overridden for individual rules.

### Example

```yaml
rules:
- name: parameter-description
  object: parameter
  description: parameter objects should have a description
  truthy: description
- name: parameter-name-regex
  object: parameter
  description: parameter names should match RFC6570
  pattern:
    property: name
    value: '^[A-Za-z0-9?_()]+$'
```

## Rule object format

|Property|Type|Required|Description|
|---|---|---|---|
|name|string|yes|The name/slug of the rule. Use hyphens. Used as the unique key. You can namespace your rules with any prefix and delimiter you wish, to avoid clashes with other people's and the built-in rules|
|description|string|recommended|An optional description for the rule|
|disabled|boolean|no|Set to `true` to temporarily disable a rule|
|enabled|boolean|deprecated|No longer used by `oas-linter`|
|object|string\|array|no|The object(s) to act upon, may be `*` for all objects. E.g. `parameter`|
|schema|o bject|no|A JSON Schema object used to validate the input object|
|truthy|string\|array|no|A property or list of properties which must be truthy (present with a non-false, non-null, non-empty value). Empty arrays are not considered truthy|
|alphabetical|object|no|Structure: `{ properties: string, keyedBy: string }`|
|if|object|no|An object containing a `property` key. If this is present, the property within `then.property` must be present with the value in the `then.value`. An optional `else.property` and `else.value` may be supplied|
|or|array|no|An array of property names, one or more of which must be present|
|maxLength|object|no|An object containing a `property` string name, and a `value` (integer). The length of the `property` value must not be longer than `value`|
|notContain|object|no|An object containing a `properties` array and a `value` or `pattern`. None of the `properties` must contain the `value` or match the `pattern`. Used with strings|
|notEndWith|object|no|An object containing a `property`, an optional `omit` prefix and a `value` string. The given `property` (once `omit` is removed) must not end with the given `value`. Used with strings|
|pattern|object|no|An object containing a `property` name, an optional `split` string which is used to split the value being tested into individual components, an optional `omit` string (which is chopped off the front of each component being tested), and a `value` regex property which is used to test all components of the property value being tested. If `startsWith` is present, the property must start with that string or the rule is skipped|
|properties|integer|no|The exact number of non-extension properties which must be present on the target object|
|skip|string|no|The name of a property in the `options` object. If this property is truthy, then the rule is skipped. E.g. `isCallback` can be used to skip rules for `operation` objects within `callback` objects, while still applying to top-level `operation` objects|
|url|string|no|An optional override of the top-level `url` property, just for this rule
|xor|array|no|An array of property names, only one of which must be present|

```

### File: docs\options.md
```md
# Options documentation

Parameter|Type|Input/Output|Description
|---|---|---|---|
agent|Object|Input|Optional http(s).Agent to be used when fetching resources
allScopes|Object|Internal|Cache of scopes by securityScheme for validation
anchors|Boolean|Input|Allow use of YAML anchors/aliases. May break things
cache|Object|Input|Optional cache of external resources
components|Boolean|Input|Command-line flag to indicate unresolve information should be displayed
context|Array|Output|The context stack of associated with errors in a validation step, you normally want the last entry only
debug|Boolean|Input|Flag to enable debug mode, adds specification-extensions
direct|Boolean|Input|Flag to indicate that only the converted OpenApi definition should be returned, not wrapped in options
encoding|String|Input|Encoding to use when reading/writing files
expectFailure|Boolean|Input|Flag to invert the status of a validation step
externalRef|Object|Internal|When `prevalidate` is true, holds the entire object representing an externally `$ref`d file
externalRefs|Object|Internal|Used to track resolved external references
externals|[Array](externals.md)|Output|Information required to unresolve a resolved definition back into its component parts
fail|Boolean|Input|Command-line flag used by `testRunner`
fatal|Boolean|Input|Treat ENOTFOUND and 404 errors as fatal during resolution, otherwise returns empty objects
file|String|Input|Used to pass filename back to `testRunner`
filters|Array\[function\]|Input|Input filters for the resolver (e.g. to convert JSON schema dialects)
fetch|function|Input|Used to override the internal `fetch` implementation
fetchOptions|Object|Input|Additional options to be passed to `fetch` calls
handlers|Object|Input|Map of additional [protocol/scheme handlers](handlers.md), must be functions which return a Promise
help|Boolean|Reserved|Command-line flag to display help
ignoreIOErrors|Boolean|Input|Set to `true` to ignore IO errors when resolving
indent|String|Input|Command-line flag to control JSON indenting
isCallback|Boolean|Input|Hint to the linter that we are within a `callback` object
laxDefaults|Boolean|Input|Flag to validation step to ignore default/type mismatches
laxurls|Boolean|Input|Flag to validation step to ignore empty URLs and # ? in paths
lint|Boolean|Input|Whether to lint the document during validation
linter|Function|Input|A linter plugin to use in place of the default linter
linterResults|Function|Input|A function to return the set of linter warnings
lintLimit|Integer|Input|Controls how many linter warnings are logged in verbose mode
lintSkip|Array|Input|A list of lint rule names which will not be tested
mediatype|Boolean|Input|Flag to validation step to check media-type strings against RFC pattern
metadata|Object|Output|Used by the validator, if `options.text` is a string, will have a property `lines` containing the number of lines in the input document. Has a property `count`, an Object keyed by the object-type within the document having values summarising the number of times that object appears in total.
nopatch|Boolean|Input|Command-line flag by `testRunner` to unset `patch`
openapi|Object|Output|The OpenApi 3.x definition returned from a conversion step
operationIds|Array[string]|Output|Used by validation to track uniqueness of operationIds
origin|Boolean\|String|Input|`true` or a URL, to indicate an `x-origin` extension should be added to the converted output
original|Object|Bi-directional|Used by `testRunner` to round-trip the original definition, set by non-object `ConvertXXX` methods
outfile|String|Input|The output file to write to
output|Boolean|Input|Internal flag to testRunner to write output openapi.yaml files
patch|Boolean|Input|Flag to fix-up minor errors in the source definition during conversion
patches|Integer|Output|Count of number of patches applied during conversion
preserveMiro|Boolean|Input|Flag to resolver as to whether to preserve old value of `$ref` in `x-miro`, default: `false`
prevalidate|Boolean|Input|Whether to validate each externally `$ref`d file separately
promise|Object|Internal|Object containing resolve and reject functions for the converter
quiet|Boolean|Input|Command-line flag used by `testRunner`
rbname|String|Input|The name of the vendor extension to use to preserve body parameter names (e.g. x-codegen-request-body-name)
refmap|Object|Internal|Used as a mapping between old and new `$ref`s
refSiblings|string|Input|Controls handling of `$ref` which has sibling properties. Valid values are `remove` (to remove such properties) which is the default outside `schema` objects,  `preserve` to keep the (incorrect) use of sibling properties, and `allOf`, to wrap the `$ref` and the remaining sibling properties in an `allOf`, which is the default/allowed only within `schema` objects
resolve|Boolean|Input|Flag to enable resolution of external `$ref`s
resolveInternal|Boolean|Input|Flag to enable resolution of internal `$ref`s. Also disables deduplication of `requestBodies`
resolver|Object|Internal|Used by the resolver to track outstanding resolutions
skip|Boolean|Reserved|Used by tools such as Speccy to skip linter rules
stop|Boolean|Input|Command-line flag used by `testRunner`
source|String|Input|The source filename or url of the definition, used by the resolver
sourceYaml|Boolean|Output|Flag set if the source string, URL or stream contained a YAML formatted definition
targetVersion|String|Input|Used to override the default target OpenAPI version of `3.0.0`
text|String|Both|If not already a truthy value, will be set to the input text of the conversion
throws|Boolean|Input|Used by tests only to indicate the fixture should throw an exception
url|String|Input|URL of the original definition, used when reading a file to create `x-origin` extension
valid|Boolean|Output|The result of a validation step
verbose|Boolean|Input|Increase verbosity, e.g. show HTTP GET requests
version|Boolean|Input|Command-line flag to show version information
warnings|Array|Output|Warnings generated by a validation step
warnOnly|Boolean|Input|Do not throw on non-patchable errors, add warning extensions
warnProperty|String|Input|Property name to use for warning extensions, default `x-s2o-warning`
whatwg|Boolean|Input|Ignored (enable WHATWG URL parsing in validation step, now the default)
yaml|Boolean|Input|Flag to write YAML, default JSON (overridden by --outfile filepath extension)

```

### File: test\http2.test.js
```js
'use strict';

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const https = require('https');
const http2 = require('http2');
const mime = require('mime-types');
const yaml = require('yaml');

const resolver = require('../packages/oas-resolver');

const tests = fs.readdirSync(path.join(__dirname,'http2')).filter(file => {
    return fs.statSync(path.join(__dirname, 'http2', file)).isDirectory() && file !== 'include';
});

const {
    HTTP2_HEADER_PATH,
    HTTP2_HEADER_METHOD,
    HTTP_STATUS_NOT_FOUND,
    HTTP_STATUS_INTERNAL_SERVER_ERROR
} = http2.constants;

const serverOptions = {
  key: fs.readFileSync(path.join(__dirname,'localhost.key')),
  cert: fs.readFileSync(path.join(__dirname,'localhost.cert'))
};
const server = http2.createSecureServer(serverOptions);
const serverRoot = path.join(__dirname,'http2');

const agent = new https.Agent({
  rejectUnauthorized: false
});

function respondToStreamError(err, stream) {
    console.warn(err);
    if (err.code === 'ENOENT') {
        stream.respond({ ":status": HTTP_STATUS_NOT_FOUND });
    } else {
        stream.respond({ ":status": HTTP_STATUS_INTERNAL_SERVER_ERROR });
    }
    stream.end();
}

server.on('stream', (stream, headers) => {
    const reqPath = headers[HTTP2_HEADER_PATH];
    const reqMethod = headers[HTTP2_HEADER_METHOD];

    const fullPath = path.join(serverRoot, reqPath);
    const responseMimeType = mime.lookup(fullPath);

    stream.respondWithFile(fullPath, {
        'content-type': responseMimeType
    }, {
        onError: (err) => respondToStreamError(err, stream)
    });
});

describe('HTTP2 tests', () => {

  before(function () {
    server.listen(8321);
  });

  after(function () {
    server.close();
  });

tests.forEach((test) => {
    describe(test, () => {
        it('should match expected output', (done) => {
            const inputSpec = path.join(__dirname, 'http2', test, 'input.yaml');
            const input = yaml.parse(fs.readFileSync(inputSpec,'utf8'),{schema:'core'});
            const output = yaml.parse(fs.readFileSync(path.join(__dirname, 'http2', test, 'output.yaml'),'utf8'),{schema:'core'});

            let options = { resolve: true, preserveMiro: false, source: inputSpec, agent, verbose: true };
            try {
                options = Object.assign({},options,yaml.parse(fs.readFileSync(path.join(__dirname, 'http2', test, 'options.yaml'),'utf8'),{schema:'core'}));
            }
            catch (ex) {}

            resolver.resolve(input, options.source, options)
            .then(function(result){
                assert.deepStrictEqual(result.openapi, output);
                return done();
            })
            .catch(function(err){
                return done(err);
            });
        });
    });
});
});

```

### File: test\resolver.test.js
```js
'use strict';

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const yaml = require('yaml');

const resolver = require('../packages/oas-resolver');

const tests = fs.readdirSync(path.join(__dirname,'resolver')).filter(file => {
    return fs.statSync(path.join(__dirname, 'resolver', file)).isDirectory() && file !== 'include';
});

describe('Resolver tests', () => {
tests.forEach((test) => {
    describe(test, () => {
        it('should match expected output', (done) => {
            const inputSpec = path.join(__dirname, 'resolver', test, 'input.yaml');
            const input = yaml.parse(fs.readFileSync(inputSpec,'utf8'),{schema:'core'});
            const output = yaml.parse(fs.readFileSync(path.join(__dirname, 'resolver', test, 'output.yaml'),'utf8'),{schema:'core'});

            let options = { resolve: true, preserveMiro: false, source: inputSpec };
            try {
                options = Object.assign({},options,yaml.parse(fs.readFileSync(path.join(__dirname, 'resolver', test, 'options.yaml'),'utf8'),{schema:'core'}));
            }
            catch (ex) {}

            resolver.resolve(input, options.source, options)
            .then(function(result){
                assert.deepStrictEqual(result.openapi, output);
                return done();
            })
            .catch(function(err){
                return done(err);
            });
        });
    });
});
});

```

### File: test\s2o.test.js
```js
'use strict';

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const yaml = require('yaml');

const swagger2openapi = require('../packages/swagger2openapi/index.js');

const doPrivate = (!process.env.SKIP_PRIVATE);

const tests = fs.readdirSync(path.join(__dirname,'s2o-test')).filter(file => {
    return fs.statSync(path.join(__dirname, 's2o-test', file)).isDirectory() && file !== 'include' && (!file.startsWith('_') || doPrivate);
});

describe('Converter tests', () => {
tests.forEach((test) => {
    describe(test, () => {
        it('should match expected output', (done) => {
            const swagger = yaml.parse(fs.readFileSync(path.join(__dirname, 's2o-test', test, 'swagger.yaml'),'utf8'),{schema:'core'});
            const openapi = yaml.parse(fs.readFileSync(path.join(__dirname, 's2o-test', test, 'openapi.yaml'),'utf8'),{schema:'core'});

            let options = {};
            options.source = path.join(__dirname, 's2o-test', test, 'swagger.yaml');
            try {
                options = Object.assign({},options,yaml.parse(fs.readFileSync(path.join(__dirname, 's2o-test', test, 'options.yaml'),'utf8'),{schema:'core'}));
            }
            catch (ex) {}

            swagger2openapi.convertObj(swagger, options, (err, result) => {
                if (err && !options.throws) return done(err);
                if (!err && options.throws) return done(new Error('Test should have thrown an exception'));

                if (!options.throws) assert.deepStrictEqual(result.openapi, openapi);

                return done();
            });
        });
    });
});
});

```

### File: test\testclone.js
```js
'use strict';
const should = require('should');
const clone = require('../packages/reftools/lib/clone.js');

const input = { container: { child: { value: true } } };

describe('clone',function(){
    describe('nop',function(){
        it('should preserve the input object unchanged',function(){
            let output = clone.nop(input);
            output.should.equal(input);
        });
    });
    describe('simple',function(){
        it('should produce a deep clone of a given object',function(){
            let output = clone.clone(input);
            output.should.have.type('object');
            output.should.not.equal(input);
            output.should.deepEqual(input);
            output.container.should.not.equal(input.container);
            output.container.child.should.not.equal(input.container.child);
        });
    });
    describe('fast',function(){
        it('should produce a shallow clone of a given object',function(){
            let output = clone.fastClone(input);
            output.should.have.type('object');
            output.should.not.equal(input);
            output.should.deepEqual(input);
            output.container.should.equal(input.container);
        });
    });
    describe('shallow',function(){
        it('should produce a shallow clone of a given object',function(){
            let output = clone.shallowClone(input);
            output.should.have.type('object');
            output.should.not.equal(input);
            output.should.deepEqual(input);
            output.container.should.equal(input.container);
        });
    });
    describe('deep',function(){
        it('should produce a deep clone of a given object',function(){
            let output = clone.deepClone(input);
            output.should.have.type('object');
            output.should.not.equal(input);
            output.should.deepEqual(input);
            output.container.should.not.equal(input.container);
        });
    });
    describe('circular',function(){
        it('should produce a deep clone of a given object',function(){
            let output = clone.circularClone(input);
            output.should.have.type('object');
            output.should.not.equal(input);
            output.should.deepEqual(input);
            output.container.should.not.equal(input.container);
        });
    });
});

```

### File: test\testderef.js
```js
'use strict';
const should = require('should');
const deref = require('../packages/reftools/lib/dereference.js').dereference;

const input = JSON.parse(`
{
  "usage": {
    "one": {
      "$ref": "#/definitions/shared"
    },
    "two": {
      "$ref": "#/definitions/shared"
    }
  },
  "definitions": {
    "shared": {
      "container": "value"
    }
  }
}
`);

describe('dereference',function(){
    describe('simple',function(){
        it('should dereference an object with $refs',function(){
            let output = deref(input,{});
            output.usage.one.should.equal(input.definitions.shared);
            output.usage.two.should.equal(input.definitions.shared);
        });
    });
    describe('toplevel',function(){
        this.timeout(500);
        it('should dereference an object with a top level $ref',function(){
            const toplevel = JSON.parse(`
            {
                "$ref": "#/definitions/referee"
            }
            `);

            const lib = JSON.parse(`
            {
                "definitions": {
                    "referee": {
                        "data": 123
                    }
                }
            }
            `);

            let output = deref(toplevel,lib);
            output.data.should.equal(123);
        });
    });
    describe('oldref',function(){
        it('should annotate where references existed',function(){
            const anno = { top: { $ref: '#/definitions/shared' },
                definitions: { shared: { data: 123 } } };
            let output = deref(anno,{},{$ref:'$oldRef'});
            output.top.data.should.equal(123);
            output.top.$oldRef.should.equal('#/definitions/shared');
        });
    });
});

```

### File: test\testfindobj.js
```js
'use strict';

const findObj = require('../packages/reftools/lib/findObj.js').findObj;
const should = require('should');

const data = { a: { b: true } };

describe('findObj',function(){
    it('should not find missing object',function(){
        findObj(data,null).found.should.be.false();
    });
    it('should find itself',function(){
        findObj(data,data).found.should.be.true();
    });
    it('should find itself, path',function(){
        findObj(data,data).path.should.be.exactly('#/');
    });
    it('should find itself, parent',function(){
        should(findObj(data,data).parent).be.exactly(null);
    });
    it('should find child object',function(){
        findObj(data,data.a).found.should.be.true();
    });
    it('should find child object, path',function(){
        findObj(data,data.a).path.should.be.exactly('#/a');
    });
    it('should find child object, parent',function(){
        findObj(data,data.a).parent.should.be.exactly(data);
    });
    it('should find grandchild object',function(){
        findObj(data,data.a.b).found.should.be.true();
    });
    it('should not find similar object',function(){
        findObj(data,{ b: true }).found.should.be.false();
    });
});

```

### File: test\testflatten.js
```js
'use strict';
const should = require('should');
const flatten = require('../packages/reftools/lib/flatten.js').flatten;

const input = { container: { child: { value: true } }, sibling: { value: false } };

//depth,path,parent.pkey

describe('flatten',function(){
    describe('simple',function(){
        it('should flatten a simple nested object',function(){
            let output = flatten(input);

            output.should.be.an.Array();
            should(output.length).equal(5);

            output[0].name.should.equal('container');
            output[0].value.should.equal(input.container);
            output[0].depth.should.equal(0);
            output[0].path.should.equal('#/container');
            output[0].parent.should.equal(input);

            output[1].name.should.equal('child');
            output[1].value.should.equal(input.container.child);
            output[1].depth.should.equal(1);
            output[1].path.should.equal('#/container/child');
            output[1].parent.should.equal(input.container);

            output[2].name.should.equal('value');
            output[2].value.should.equal(true);
            output[2].depth.should.equal(2);
            output[2].path.should.equal('#/container/child/value');
            output[2].parent.should.equal(input.container.child);

            output[3].name.should.equal('sibling');
            output[3].value.should.equal(input.sibling);
            output[3].depth.should.equal(1);
            output[3].path.should.equal('#/sibling');
            output[3].parent.should.equal(input);

            output[4].name.should.equal('value');
            output[4].value.should.equal(false);
            output[4].depth.should.equal(2);
            output[4].path.should.equal('#/sibling/value');
            output[4].parent.should.equal(input.sibling);
        });
    });
    describe('filtered',function(){
        it('should flatten a simple nested object, filtering a property',function(){
            let output = flatten(input,function(entry){
                if ((entry.name !== 'child') && (entry.name !== 'sibling')) return entry;
            });

            output.should.be.an.Array();
            should(output.length).equal(3);

            output[0].name.should.equal('container');
            output[0].value.should.equal(input.container);
            output[0].depth.should.equal(0);
            output[0].path.should.equal('#/container');
            output[0].parent.should.equal(input);

            output[1].name.should.equal('value');
            output[1].value.should.equal(true);
            output[1].depth.should.equal(1);
            output[1].path.should.equal('#/container/child/value');
            output[1].parent.should.equal(input.container.child);

            output[2].name.should.equal('value');
            output[2].value.should.equal(false);
            output[2].depth.should.equal(0);
            output[2].path.should.equal('#/sibling/value');
            output[2].parent.should.equal(input.sibling);
        });
    });
});

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
