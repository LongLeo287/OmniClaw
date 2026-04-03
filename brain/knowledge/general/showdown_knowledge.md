---
id: showdown-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.569264
---

# KNOWLEDGE EXTRACT: showdown
> **Extracted on:** 2026-03-30 22:54:17
> **Source:** showdown

---

## File: `.editorconfig`
```
[*.js]
indent_style = space
indent_size = 2
continuation_indent_size = 2
insert_final_newline = true
quote_type = single
space_after_anonymous_functions = true
space_after_control_statements = true
spaces_around_operators = true
trim_trailing_whitespace = true
spaces_in_brackets = false
curly_bracket_next_line = true
indent_brace_style = 1TBS
end_of_line = lf
charset = utf-8
```

## File: `.eslintrc.json`
```json
{
  "env": {
    "es6": true
  },
  "rules": {
    "indent": [2, 2, {"SwitchCase": 1, "VariableDeclarator": 2}],
    "curly": [2, "all"],
    "operator-linebreak": [2, "after"],
    "camelcase": [2, {"properties": "never"}],
    "quotes": [2, "single"],
    "no-multi-str": 2,
    "no-mixed-spaces-and-tabs": 2,
    "no-trailing-spaces": 2,
    "space-unary-ops": [2,
      {
        "nonwords": false,
        "overrides": {}
      }
    ],
    "brace-style": [2, "1tbs", {"allowSingleLine": true}],
    "keyword-spacing": [2, {}],
    "space-infix-ops": 2,
    "space-before-blocks": [2, "always"],
    "eol-last": 2,
    "space-before-function-paren": [2, "always"],
    "array-bracket-spacing": [2, "never", {"singleValue": false}],
    "space-in-parens": [2, "never"],
    "no-multiple-empty-lines": 2
  }
}
```

## File: `.gitattributes`
```
# Exports for git archive
/test export-ignore
.editorconfig export-ignore
.gitattributes export-ignore
.gitignore export-ignore
.eslintrc.json export-ignore
.jshintignore export-ignore
.jshintrc export-ignore
.travis.yml export-ignore
.appveyor.yml export-ignore
bower.json
Gruntfile.js export-ignore
performance.* export-ignore

# Line endings control
CHANGELOG.md text
CONTRIBUTING.md text
CREDITS.md text
license.txt text

# Force LF on js files
*.js text eol=lf

# Force binary mode on bin dir and dist fir
bin/* binary
dist/* binary
```

## File: `.gitignore`
```
.idea/
.build/
.DS_Store
node_modules
npm-debug.log
/*.test.*
*.log
```

## File: `.jshintignore`
```
Gruntfile.js
dist/**/*.js
build/**/*.js
src/options.js
bin/*
/karma.browserstack.js
```

## File: `.jshintrc`
```
{
  "node": true,
  "browser": true,
  "esnext": true,
  "bitwise": true,
  "camelcase": true,
  "curly": true,
  "eqeqeq": true,
  "immed": true,
  "indent": 2,
  "latedef": "nofunc",
  "newcap": true,
  "noarg": true,
  "quotmark": "single",
  "undef": false,
  "unused": true,
  "strict": false,
  "trailing": true,
  "smarttabs": true,
  "onevar": true,
  "globals": {
    "module": true,
    "define": true,
    "window": true,
    "document": true,
    "showdown": true
  }
}
```

## File: `bower.json`
```json
{
    "name": "showdown",
    "description": "A Markdown to HTML converter written in Javascript",
    "homepage": "https://github.com/showdownjs/showdown",
    "authors": [
      "Estevão Santos (https://github.com/tivie)",
      "Pascal Deschênes (https://github.com/pdeschen)"
    ],
    "main": ["dist/showdown.js"],
    "ignore": [
      ".editorconfig",
      ".gitattributes",
      ".gitignore",
      ".jscs.json",
      ".jshintignore",
      ".jshintrc",
      ".travis.yml",
      "Gruntfile.js",
      "package.json",
      "test/*"
    ],
    "repository": {
      "type": "git",
      "url": "https://github.com/showdownjs/showdown.git"
    },
    "keywords": [
      "markdown",
      "md",
      "mdown"
    ],
    "license": "https://github.com/showdownjs/showdown/blob/master/license.txt"
}
```

## File: `CHANGELOG.md`
```markdown
## [2.1.0](https://github.com/showdownjs/showdown/compare/2.0.0...2.1.0) (2022-04-21)

* refactor(cli)!: Remove support for "extra options" and add -c flag, closes [#916](https://github.com/showdownjs/showdown/issues/916)


### Bug Fixes

* **cli:** cli displays the correct version number ([8b48882](https://github.com/showdownjs/showdown/commit/8b48882))


### BREAKING CHANGES

* the CLI no longer accepts "extra options". Instead you should pass the `-c` flag. To update:

before:
```
showdown makehtml -i foo.md -o bar.html --strikethrough --emoji
```

after:
```
showdown makehtml -i foo.md -o bar.html -c strikethrough -c emoji
```

<a name="2.0.0"></a>
# [2.0.0](https://github.com/showdownjs/showdown/compare/1.9.1...2.0.0) (2022-02-15)

### Breaking Changes
* Supported Node Versions were set to match the [node release schedule](https://nodejs.org/en/about/releases/) which at the time of writing includes Node 12.x, 14.x, 16.x and 17.x
* The `yargs` dependecy was updated to `^17.2.1` to mitigate a security issue.
* The Showdown Licesnse has been changed from  BSD-3-Clause to MIT

### Bug Fixes

* allow escaping of colons ([25c4420](https://github.com/showdownjs/showdown/commit/25c4420))
* reduce npm package size  ([35730b7](https://github.com/showdownjs/showdown/commit/35730b7)), closes [#619](https://github.com/showdownjs/showdown/issues/619)

### Features

* Added `ellipsis` option to configure if the ellipsis unicode character is used or not. ( Thanks @VladimirV99 )
* Added a default security policy. Please report security issues to the issues tab on GitHub.


<a name="1.9.1"></a>
## [1.9.1](https://github.com/showdownjs/showdown/compare/1.9.0...1.9.1) (2019-11-02)


### Bug Fixes

* **openLinksInNewWindow:** add rel="noopener noreferrer" to links ([1cd281f](https://github.com/showdownjs/showdown/commit/1cd281f)), closes [#670](https://github.com/showdownjs/showdown/issues/670)

<a name="1.0.0"></a>
# [1.9.0](https://github.com/showdownjs/showdown/compare/1.8.7...1.9.0) (2018-11-10)

Version 1.9.0 introduces a new feature, the Markdown to HTML converter. This feature is still experimental and is a partial backport of the new Reverse Converter planned for version 2.0.
### Bug Fixes

* **italicsAndBold:** fix issue with consecutive spans ([#608](https://github.com/showdownjs/showdown/issues/608)) ([5c0d67e](https://github.com/showdownjs/showdown/commit/5c0d67e)), closes [#544](https://github.com/showdownjs/showdown/issues/544)
* **underline:** fix issue with consecutive spans ([81edc70](https://github.com/showdownjs/showdown/commit/81edc70))

### Features

* **converter.makeMarkdown:** [EXPERIMENTAL] add an HTML to MD converter ([e4b0e69](https://github.com/showdownjs/showdown/commit/e4b0e69)), closes [#388](https://github.com/showdownjs/showdown/issues/388) [#233](https://github.com/showdownjs/showdown/issues/233)

<a name="1.8.7"></a>
# [1.8.7](https://github.com/showdownjs/showdown/compare/1.8.6...1.8.7) (2018-10-16)

### Bug Fixes

* **emojis:** fix emoji excessive size ([4aca41c](https://github.com/showdownjs/showdown/commit/4aca41c))
* **gfm-codeblocks:** add support for spaces before language declaration ([24bf7b1](https://github.com/showdownjs/showdown/commit/24bf7b1)), closes [#569](https://github.com/showdownjs/showdown/issues/569)
leading space no longer breaks gfm codeblocks ([828c32f](https://github.com/showdownjs/showdown/commit/828c32f)), closes [#523](https://github.com/showdownjs/showdown/issues/523)

* **images:** fix js error when using image references ([980e702](https://github.com/showdownjs/showdown/commit/980e702)), closes [#585](https://github.com/showdownjs/showdown/issues/585)
* **literalMidWordAsterisks:** now parses single characters enclosed by * correctly ([fe70e45](https://github.com/showdownjs/showdown/commit/fe70e45)), closes [#478](https://github.com/showdownjs/showdown/issues/478)
* **mentions:** allow for usernames with dot, underscore and dash ([dfeb1e2](https://github.com/showdownjs/showdown/commit/dfeb1e2)), closes [#574](https://github.com/showdownjs/showdown/issues/574)
* **nbsp:** fix replacing of nbsp with regular spaces ([8bc1f42](https://github.com/showdownjs/showdown/commit/8bc1f42))

<a name="1.8.6"></a>
# [1.8.6](https://github.com/showdownjs/showdown/compare/1.8.5...1.8.6) (2017-12-22)

### Features

* **splitAdjacentBlockquotes:** add option to split adjacent blockquote blocks ([da328f2](https://github.com/showdownjs/showdown/commit/da328f2)), closes [#477](https://github.com/showdownjs/showdown/issues/477)



<a name="1.8.5"></a>
# [1.8.5](https://github.com/showdownjs/showdown/compare/1.8.4...1.8.5) (2017-12-10)


### Features

* **completeHTMLDocument:** add option to output a complete HTML document ([a8427c9](https://github.com/showdownjs/showdown/commit/a8427c9))
* **metadata:** add support for embedded metadata ([63d949f](https://github.com/showdownjs/showdown/commit/63d949f)), closes [#260](https://github.com/showdownjs/showdown/issues/260)



<a name="1.8.4"></a>
## [1.8.4](https://github.com/showdownjs/showdown/compare/1.8.3...1.8.4) (2017-12-05)


### Bug Fixes

* **tables:** raw html inside code tags in tables no longer breaks tables ([4ef4c5e](https://github.com/showdownjs/showdown/commit/4ef4c5e)), closes [#471](https://github.com/showdownjs/showdown/issues/471)



<a name="1.8.3"></a>
## [1.8.3](https://github.com/showdownjs/showdown/compare/1.8.2...1.8.3) (2017-11-28)


### Bug Fixes

* **literalMidWordAsterisks:** no longer treats colon as alphanumeric char ([21194c8](https://github.com/showdownjs/showdown/commit/21194c8)), closes [#461](https://github.com/showdownjs/showdown/issues/461)
* **spanGamut:** code spans are hashed after parsing ([f4f63c5](https://github.com/showdownjs/showdown/commit/f4f63c5)), closes [#464](https://github.com/showdownjs/showdown/issues/464)
* **tables:** pipe character in code spans no longer breaks table ([0c933a0](https://github.com/showdownjs/showdown/commit/0c933a0)), closes [#465](https://github.com/showdownjs/showdown/issues/465)



<a name="1.8.2"></a>
## [1.8.2](https://github.com/showdownjs/showdown/compare/1.8.1...1.8.2) (2017-11-11)


### Bug Fixes

* **fenced codeblocks:** add tilde as fenced code block delimiter ([c956ede](https://github.com/showdownjs/showdown/commit/c956ede)), closes [#456](https://github.com/showdownjs/showdown/issues/456)
* **openLinksInNewWindow:** hash links are not affected by the option ([11936ec](https://github.com/showdownjs/showdown/commit/11936ec)), closes [#457](https://github.com/showdownjs/showdown/issues/457)



<a name="1.8.1"></a>
## [1.8.1](https://github.com/showdownjs/showdown/compare/1.8.0...1.8.1) (2017-11-01)


### Dependencies update

* **package:** update yargs to version 10.0.3 ([#447](https://github.com/showdownjs/showdown/issues/447)) ([906b26d](https://github.com/showdownjs/showdown/commit/906b26d))

### Bug Fixes

* **CDNjs:** bump version to fix version mismatch with CDNjs ([#452](https://github.com/showdownjs/showdown/issues/452))


<a name="1.8.0"></a>
# [1.8.0](https://github.com/showdownjs/showdown/compare/1.7.6...1.8.0) (2017-10-24)

### NOTICE

Don't use the CDNjs version of this release. See issue [#452](https://github.com/showdownjs/showdown/issues/452) for more details.


### Bug Fixes

* **autolinks:** prevent _ and * to be parsed in links ([61929bb](https://github.com/showdownjs/showdown/commit/61929bb)), closes [#444](https://github.com/showdownjs/showdown/issues/444)


### Features

* **ellipsis:** add auto-ellipsis support ([25f1978](https://github.com/showdownjs/showdown/commit/25f1978))

  - *Example:*
    
      input
    
      ```md
      this is an ellipsis...
      ```
        
      output
    
      ```html
      <p>this is an ellipsis…</p>
      ```

* **emoji:** add emoji support through option `emoji`([5b8f1d3](https://github.com/showdownjs/showdown/commit/5b8f1d3)), closes [#448](https://github.com/showdownjs/showdown/issues/448)

  - *Usage:*
    
      ```js
      var conv = new showdown.Converter({emoji: true});
      ```      
    
  - *Example:*
    
      input
    
      ```md
      this is a smile :smile: emoji
      ```
        
      output
    
      ```html
      <p>this is a smile 😄 emoji</p>
      ```
    
* **start ordered lists at an arbitrary number:** add support for defining the first item number of ordered lists ([9cdc35e](https://github.com/showdownjs/showdown/commit/9cdc35e)), closes [#377](https://github.com/showdownjs/showdown/issues/377)

  - *Example:*
    
      input

       ```md
       3. foo
       4. bar
       5. baz
       ```

      output
    
      ```html
      <ol start="3">
        <li>foo</li>
        <li>bar</li>
        <li>baz</li>
      </ol>
      ```

* **underline:** add EXPERIMENTAL support for underline ([084b819](https://github.com/showdownjs/showdown/commit/084b819)), closes [#450](https://github.com/showdownjs/showdown/issues/450)

  - *Usage:*
    
      ```js
      var conv = new showdown.Converter({underline: true});
      ```
    
  - *Example:*
    
      input
    
      ```md
      this is __underlined__ and this is ___also underlined___
      ```
        
      output
    
      ```html
      <p>this is <u>underlined</u> and this is <u>also underlined</u></p>
      ```
	
  - *Note:*	With this option enabled, underscore no longer parses as `<em>` or `<strong>`	  
			
### BREAKING CHANGES

* start ordered lists at an arbitrary number: Since showdown now supports starting ordered lists at an arbitrary number, 
list output may differ.



<a name="1.7.6"></a>
## [1.7.6](https://github.com/showdownjs/showdown/compare/1.7.5...1.7.6) (2017-10-06)


### Bug Fixes

* **tables:** tables are properly rendered when followed by a single linebreak and a list ([d88b095](https://github.com/showdownjs/showdown/commit/d88b095)), closes [#443](https://github.com/showdownjs/showdown/issues/443)
* **tables:** trailing spaces no longer prevent table parsing ([66bdd21](https://github.com/showdownjs/showdown/commit/66bdd21)), closes [#442](https://github.com/showdownjs/showdown/issues/442)



<a name="1.7.5"></a>
## [1.7.5](https://github.com/showdownjs/showdown/compare/1.7.4...1.7.5) (2017-10-02)


### Bug Fixes

* **html-comments:** changed regex to prevent malformed long comment to freeze showdown ([3efcd10](https://github.com/showdownjs/showdown/commit/3efcd10)), closes [#439](https://github.com/showdownjs/showdown/issues/439)



<a name="1.7.4"></a>
## [1.7.4](https://github.com/showdownjs/showdown/compare/1.7.3...1.7.4) (2017-09-08)


### Bug Fixes

* **helper.isArray:** replace a.constructor === Array with Array.isArray ([466a2eb](https://github.com/showdownjs/showdown/commit/466a2eb)), closes [#425](https://github.com/showdownjs/showdown/issues/425)
* **loader:** allow AMD loader to be used within Node env  ([ff24bdb](https://github.com/showdownjs/showdown/commit/ff24bdb))


### Features

* **base64-wrapping:** support for wrapping base64 strings ([8c593a4](https://github.com/showdownjs/showdown/commit/8c593a4)), closes [#429](https://github.com/showdownjs/showdown/issues/429)



<a name="1.7.3"></a>
## [1.7.3](https://github.com/showdownjs/showdown/compare/1.7.2...1.7.3) (2017-08-23)


### Bug Fixes

* **github flavor:** add backslashEscapesHTMLTags to GFM flavor ([5284439](https://github.com/showdownjs/showdown/commit/5284439))
* **literalMidWordAsterisks:** option no longer treats punctuation as word character ([8f05be7](https://github.com/showdownjs/showdown/commit/8f05be7)), closes [#398](https://github.com/showdownjs/showdown/issues/398)
* **tables:** allow for one column table ([fef110c](https://github.com/showdownjs/showdown/commit/fef110cccb2d02b218183398d9baa0ae256a7283)), closes [#406](https://github.com/showdownjs/showdown/issues/406)

### Features

* **rawHeaderId:** Remove only spaces, ' and " from generated header ids ([1791cf0](https://github.com/showdownjs/showdown/commit/1791cf0)), closes [#409](https://github.com/showdownjs/showdown/issues/409)
* **rawPrefixHeaderId:** add option to prevent showdown from modifying the prefix ([ff26c08](https://github.com/showdownjs/showdown/commit/ff26c08)), closes [#409](https://github.com/showdownjs/showdown/issues/409)



<a name="1.7.2"></a>
## [1.7.2](https://github.com/showdownjs/showdown/compare/1.7.1...1.7.2) (2017-08-05)


### Bug Fixes

* **githubMentions:** githubMentions now works with openLinksInNewWindow options ([1194d88](https://github.com/showdownjs/showdown/commit/1194d88)), closes [#403](https://github.com/showdownjs/showdown/issues/403)
* **lists:** fix multi paragraph lists with sublists ([a2259c0](https://github.com/showdownjs/showdown/commit/a2259c0)), closes [#397](https://github.com/showdownjs/showdown/issues/397)
* **tablesHeaderId:** fix mismatch of option name ([51e4693](https://github.com/showdownjs/showdown/commit/51e4693)), closes [#412](https://github.com/showdownjs/showdown/issues/412)


### Features

* **backslashEscapesHTMLTags:** backslash escapes HTML tags ([5a5aff6](https://github.com/showdownjs/showdown/commit/5a5aff6)), closes [#374](https://github.com/showdownjs/showdown/issues/374)



<a name="1.7.1"></a>
## [1.7.1](https://github.com/showdownjs/showdown/compare/1.7.0...1.7.1) (2017-06-02)

Important HOTFIX

### Bug Fixes

* **HTML Parser:** fix nasty bug where malformed HTML would hang showdown ([6566c72](https://github.com/showdownjs/showdown/commit/6566c72)), closes [#393](https://github.com/showdownjs/showdown/issues/393)



<a name="1.7.0"></a>
## [1.7.0](https://github.com/showdownjs/showdown/compare/1.6.4...1.7.0) (2017-06-01)

(DEPRECATED)

### Bug Fixes

* **anchors:** fix issue with brackets in link URL ([7ba18dd](https://github.com/showdownjs/showdown/commit/7ba18dd)), closes [#390](https://github.com/showdownjs/showdown/issues/390)
* **excludeTrailingPunctuationFromURL:** add comma to punctuation list ([fa35fd5](https://github.com/showdownjs/showdown/commit/fa35fd5)), closes [#354](https://github.com/showdownjs/showdown/issues/354)
* **excludeTrailingPunctuationFromURLs:** fix weird character when this option with simplifiedAutoLinks ([71acff5](https://github.com/showdownjs/showdown/commit/71acff5)), closes [#378](https://github.com/showdownjs/showdown/issues/378)
* **HTML parsing:** fix HTML parsing issues with nested tags ([6fbc072](https://github.com/showdownjs/showdown/commit/6fbc072)), closes [#357](https://github.com/showdownjs/showdown/issues/357) [#387](https://github.com/showdownjs/showdown/issues/387)
* **openLinksInNewWindow:** encode _ to prevent clash with em ([813f832](https://github.com/showdownjs/showdown/commit/813f832)), closes [#379](https://github.com/showdownjs/showdown/issues/379)
* **package:** update yargs to version 7.0.1 ([#349](https://github.com/showdownjs/showdown/issues/349)) ([9308d7b](https://github.com/showdownjs/showdown/commit/9308d7b))
* **package:** update yargs to version 8.0.1 ([#385](https://github.com/showdownjs/showdown/issues/385)) ([5fd847b](https://github.com/showdownjs/showdown/commit/5fd847b))
* **simpleAutoLinks:** URLs with emphasis/strikethrough are parsed ([5c50675](https://github.com/showdownjs/showdown/commit/5c50675)), closes [#347](https://github.com/showdownjs/showdown/issues/347)
* **tables:** pipe char can now be escaped ([1ebc195](https://github.com/showdownjs/showdown/commit/1ebc195)), closes [#345](https://github.com/showdownjs/showdown/issues/345)
* **url parsing:** fix url edge case parsing in images and links ([30aa18c](https://github.com/showdownjs/showdown/commit/30aa18c))


### Features

* **customizeHeaderId:** add option for customizing header ids ([94c570a](https://github.com/showdownjs/showdown/commit/94c570a)), closes [#383](https://github.com/showdownjs/showdown/issues/383)
* **images:** add support for image's implicit reference syntax ([0c6c07b](https://github.com/showdownjs/showdown/commit/0c6c07b)), closes [#366](https://github.com/showdownjs/showdown/issues/366)
* **literalMidWordAsterisks:** add option for mid word asterisks ([5bec8f9](https://github.com/showdownjs/showdown/commit/5bec8f9))
* **openLinksInNewWindow:** add option to open all links in a new window ([50235d6](https://github.com/showdownjs/showdown/commit/50235d6)), closes [#362](https://github.com/showdownjs/showdown/issues/362) [#337](https://github.com/showdownjs/showdown/issues/337) [#249](https://github.com/showdownjs/showdown/issues/249) [#247](https://github.com/showdownjs/showdown/issues/247) [#222](https://github.com/showdownjs/showdown/issues/222)



<a name="1.6.4"></a>
## [1.6.4](https://github.com/showdownjs/showdown/compare/1.6.3...1.6.4) (2017-02-06)


### Bug Fixes

* **encodeAmpsAndAngles:** fix > and < encoding ([7f43b79](https://github.com/showdownjs/showdown/commit/7f43b79)), closes [#236](https://github.com/showdownjs/showdown/issues/236)
* **encodeEmail:** now produces valid emails ([605d8b7](https://github.com/showdownjs/showdown/commit/605d8b7)), closes [#340](https://github.com/showdownjs/showdown/issues/340)
* **flavor: github:** new version of github does not use prefix 'user-content' in headers ([368f0b6](https://github.com/showdownjs/showdown/commit/368f0b6))
* **hashCodeTags:** escape code tags ([41cb3f6](https://github.com/showdownjs/showdown/commit/41cb3f6)), closes [#339](https://github.com/showdownjs/showdown/issues/339)
* **italicsAndBold:** fix double emphasis edge case ([1832b7f](https://github.com/showdownjs/showdown/commit/1832b7f))
* **paragraph:** workaround QML bug ([f7a429e](https://github.com/showdownjs/showdown/commit/f7a429e)), closes [#246](https://github.com/showdownjs/showdown/issues/246) [#338](https://github.com/showdownjs/showdown/issues/338)
* **prefixHeaderId:** make `prefixHeaderId` string be parsed along the generated id ([f641a7d](https://github.com/showdownjs/showdown/commit/f641a7d))


### Features

* **flavor: ghost:** add Ghost flavor ([6374b5b](https://github.com/showdownjs/showdown/commit/6374b5b))
* **flavor: original:** add John Gruber's markdown flavor ([6374b5b](https://github.com/showdownjs/showdown/commit/6374b5b))



<a name="1.6.3"></a>
## [1.6.3](https://github.com/showdownjs/showdown/compare/1.6.2...1.6.3) (2017-01-30)


### Bug Fixes

* **codeSpans:** add - and = to escaped chars inside code spans ([4243a31](https://github.com/showdownjs/showdown/commit/4243a31))
* **italicsAndBold:** fix inconsistency in italicsAndBold parsing ([a4f05d4](https://github.com/showdownjs/showdown/commit/a4f05d4)), closes [#332](https://github.com/showdownjs/showdown/issues/332)
* **literalMidWordUnderscores:** fix inconsistent behavior of emphasis and strong with literalMidWordUndescores ([0292ae0](https://github.com/showdownjs/showdown/commit/0292ae0)), closes [#333](https://github.com/showdownjs/showdown/issues/333)
* **paragraphs:** fix empty lines generating empty paragraphs ([54bf744](https://github.com/showdownjs/showdown/commit/54bf744)), closes [#334](https://github.com/showdownjs/showdown/issues/334)
* **strikethrough:** fix strikethrough being wrongly parsed inside codeSpans ([169cbe8](https://github.com/showdownjs/showdown/commit/169cbe8))

### Features

* **events:** add events to all subparsers ([7d63a3e](https://github.com/showdownjs/showdown/commit/7d63a3e))



<a name="1.6.2"></a>
## [1.6.2](https://github.com/showdownjs/showdown/compare/1.6.1...1.6.2) (2017-01-29)


### Bug Fixes

* **escapeSpecialCharsWithinTagAttributes:** add ~ and = to escaped chars ([bfcc0e4](https://github.com/showdownjs/showdown/commit/bfcc0e4))
* **strikethrough:** allow escaping tilde char ([24d47d7](https://github.com/showdownjs/showdown/commit/24d47d7)), closes [#331](https://github.com/showdownjs/showdown/issues/331)

### Features

* **ghMentionsLink:** add ability to define the generated url in @mentions ([a4c24c9](https://github.com/showdownjs/showdown/commit/a4c24c9))



<a name="1.6.1"></a>
## [1.6.1](https://github.com/showdownjs/showdown/compare/1.6.0...1.6.1) (2017-01-28)


### Bug Fixes

* **simplifiedAutoLink:** fix missing spaces before and after email addresses ([5190b6a](https://github.com/showdownjs/showdown/commit/5190b6a)), closes [#330](https://github.com/showdownjs/showdown/issues/330)

### Features

* **encodeEmail:** add option to enable/disable mail obfuscation ([90c52b8](https://github.com/showdownjs/showdown/commit/90c52b8))

### Notes

This release also improves performance a bit (around 8%)



<a name="1.6.0"></a>
## [1.6.0](https://github.com/showdownjs/showdown/compare/1.5.5...1.6.0) (2017-01-09)


### Bug Fixes

* **ghCompatibleHeaderId:** improve the number of removed chars ([d499feb](https://github.com/showdownjs/showdown/commit/d499feb))
* **IE8:** fix for IE8 error on using isUndefined function ([561dc5f](https://github.com/showdownjs/showdown/commit/561dc5f)), closes [#280](https://github.com/showdownjs/showdown/issues/280)
* **options:** fix ghCompatibleHeaderId that was set as string instead of boolean ([de7c37e](https://github.com/showdownjs/showdown/commit/de7c37e))
* **simpleLineBreaks:** fix simpleLineBreaks option not working with non-ASCII chars and markdown delimiters ([b1c458a](https://github.com/showdownjs/showdown/commit/b1c458a)), closes [#318](https://github.com/showdownjs/showdown/issues/318) [#323](https://github.com/showdownjs/showdown/issues/323)

### Features

* **CLI:** add -q (quiet) and -m (mute) mode to CLI ([f3b86f0](https://github.com/showdownjs/showdown/commit/f3b86f0))
* **CLI:flavor:** add flavor option to CLI ([2d6cd1e](https://github.com/showdownjs/showdown/commit/2d6cd1e))
* **getFlavor:** add getFlavor method to showdown and Converter ([0eaf105](https://github.com/showdownjs/showdown/commit/0eaf105))
* **ghMentions:** add support for github's @mentions ([f2671c0](https://github.com/showdownjs/showdown/commit/f2671c0)), closes [#51](https://github.com/showdownjs/showdown/issues/51)

### BREAKING CHANGES:

* CLI tool now uses the same option defaults as showdown main library. This mean
  the default flavor is vanilla and ghCodeBlocks options is enabled by default.
    
    To update, add `--ghCodeBlocks="false"` to the command.


<a name="1.5.5"></a>
## [1.5.5](https://github.com/showdownjs/showdown/compare/1.5.4...1.5.5) (2016-12-30)

### Features

* **ghCompatibleHeaderId:** generate header ids compatible with github ([db97a90](https://github.com/showdownjs/showdown/commit/db97a90)), closes [#320](https://github.com/showdownjs/showdown/issues/320) [#321](https://github.com/showdownjs/showdown/issues/321)



<a name="1.5.4"></a>
## [1.5.4](https://github.com/showdownjs/showdown/compare/1.5.3...1.5.4) (2016-12-21)


### Bug Fixes

* **horizontal rule:** revert backwards incompatibility change ([113f5f6](https://github.com/showdownjs/showdown/commit/113f5f6)), closes [#317](https://github.com/showdownjs/showdown/issues/317)
* **simpleLineBreaks:** fix simpleLineBreak option breaking lists html ([ed4c33f](https://github.com/showdownjs/showdown/commit/ed4c33f)), closes [#316](https://github.com/showdownjs/showdown/issues/316)



<a name="1.5.3"></a>
## [1.5.3](https://github.com/showdownjs/showdown/compare/1.5.2...1.5.3) (2016-12-19)


### Bug Fixes

* parser slowness with certain inputs ([da8fb53](https://github.com/showdownjs/showdown/commit/da8fb53)), closes [#315](https://github.com/showdownjs/showdown/issues/315)

### Features

* **requireSpaceBeforeHeadingText:** option to make space between `#` and header text mandatory ([5d19877](https://github.com/showdownjs/showdown/commit/5d19877)), closes [#277](https://github.com/showdownjs/showdown/issues/277)



<a name="1.5.2"></a>
## [1.5.2](https://github.com/showdownjs/showdown/compare/1.5.1...1.5.2) (2016-12-17)


### Bug Fixes

* **listeners:** fix listeners typo ([f0d25b7](https://github.com/showdownjs/showdown/commit/f0d25b7)), closes [#290](https://github.com/showdownjs/showdown/issues/290)
* **lists:** lines with multiple dashes being parsed as multilists ([10b3410](https://github.com/showdownjs/showdown/commit/10b3410)), closes [#312](https://github.com/showdownjs/showdown/issues/312)
* **nbsp:** nbsp are replaced with simple spaces ([6e90f7c](https://github.com/showdownjs/showdown/commit/6e90f7c))



<a name="1.5.1"></a>
## [1.5.1](https://github.com/showdownjs/showdown/compare/1.5.0...1.5.1) (2016-12-01)


### Features

* **simpleLineBreaks:** option that parses linebreaks as <br />. This option enables linebreaks to always be treated as `<br />` tags 
  without needing to add spaces in front of the line, the same way GitHub does. ([0942b5e](https://github.com/showdownjs/showdown/commit/0942b5e)), closes [#206](https://github.com/showdownjs/showdown/issues/206)
* **excludeTrailingPunctuationFromURLs:** option that excludes trailing punctuation from auto linked URLs. ([d2fc2a0](https://github.com/showdownjs/showdown/commit/d2fc2a0)), closes [#266](https://github.com/showdownjs/showdown/issues/266) [#308](https://github.com/showdownjs/showdown/issues/308)



<a name="1.5.0"></a>
## [1.5.0](https://github.com/showdownjs/showdown/compare/1.4.4...1.5.0) (2016-11-11)


### Bug Fixes

* **lists:** enforce 4 space indentation in sublists ([d51be6e](https://github.com/showdownjs/showdown/commit/d51be6e))
* **lists:** fix sublists inconsistent behavior ([9cfe8b1](https://github.com/showdownjs/showdown/commit/9cfe8b1)), closes [#299](https://github.com/showdownjs/showdown/issues/299)

### Features

* **disableForced4SpacesIndentedSublists:** option that disables the requirement of indenting nested sublists by 4 spaces. The option is disabled by default ([0be39bc](https://github.com/showdownjs/showdown/commit/0be39bc))


### BREAKING CHANGES

* syntax for sublists is now more restrictive. Before, sublists SHOULD be indented by 4 spaces, but indenting at least 2 spaces would work. 
  Now, sublists MUST be indented 4 spaces or they won't work.

    With this input:
    ```md
    * one
      * two
        * three
    ```
    
    Before (output):
    ```html
    <ul>
      <li>one
        <ul>
          <li>two
            <ul><li>three</li></ul>
          <li>
        </ul>
      </li>
    <ul>
    ```
    
    After (output):
    ```html
    <ul>
      <li>one</li>
      <li>two
        <ul><li>three</li></ul>
      </li>
    </ul>
    ```
    
    To migrate either fix source md files or activate the option `disableForced4SpacesIndentedSublists`:
    ```md
    showdown.setOption('disableForced4SpacesIndentedSublists', true);
    ```


<a name="1.4.4"></a>
## [1.4.4](https://github.com/showdownjs/showdown/compare/1.4.3...1.4.4) (2016-11-02)


### Bug Fixes

* make some regexes a bit faster and make tab char equivalent to 4 spaces ([b7e7560](https://github.com/showdownjs/showdown/commit/b7e7560))
* **double linebreaks:** fix double linebreaks in html output ([f97e072](https://github.com/showdownjs/showdown/commit/f97e072)), closes [#291](https://github.com/showdownjs/showdown/issues/291)
* **lists linebreaks:** fix lists linebreaks in html output ([2b813cd](https://github.com/showdownjs/showdown/commit/2b813cd)), closes [#291](https://github.com/showdownjs/showdown/issues/291)
* **parser:** fix issue with comments inside nested code blocks ([799abea](https://github.com/showdownjs/showdown/commit/799abea)), closes [#288](https://github.com/showdownjs/showdown/issues/288)



<a name="1.4.3"></a>
## [1.4.3](https://github.com/showdownjs/showdown/compare/1.4.2...1.4.3) (2016-08-19)


### Bug Fixes

* **bower:** fix sourceMappingURL errors in bower by including source ([9b5a233](https://github.com/showdownjs/showdown/commit/9b5a233)), closes [#200](https://github.com/showdownjs/showdown/issues/200)
* **comments:** Fix html comment parser ([238726c](https://github.com/showdownjs/showdown/commit/238726c)), closes [#276](https://github.com/showdownjs/showdown/issues/276)
* **ie8 compatibility:** Improve ie8 compatibility ([984942e](https://github.com/showdownjs/showdown/commit/984942e)), closes [#275](https://github.com/showdownjs/showdown/issues/275) [#271](https://github.com/showdownjs/showdown/issues/271)
* **simplifiedAutoLink:** fix simplified autolink to match GFM behavior ([0cc55b0](https://github.com/showdownjs/showdown/commit/0cc55b0)), closes [#284](https://github.com/showdownjs/showdown/issues/284) [#285](https://github.com/showdownjs/showdown/issues/285)



<a name="1.4.2"></a>
## [1.4.2](https://github.com/showdownjs/showdown/compare/1.4.1...1.4.2) (2016-06-21)


### Bug Fixes

* **image-parser:** fix ref style imgs after inline style imgs not parsing correctly ([73206b0](https://github.com/showdownjs/showdown/commit/73206b0)), closes [#261](https://github.com/showdownjs/showdown/issues/261)
* **tables:** add check for undefined on text due to failing to parse tables ([6e30a48](https://github.com/showdownjs/showdown/commit/6e30a48)), author [stewartmckee](https://github.com/stewartmckee), closes [#257](https://github.com/showdownjs/showdown/pull/247)

### Features

* **smart-indent-fix:** fix for es6 indentation problems ([261f127](https://github.com/showdownjs/showdown/commit/261f127)), closes [#259](https://github.com/showdownjs/showdown/issues/259)



<a name="1.4.1"></a>
## [1.4.1](https://github.com/showdownjs/showdown/compare/1.4.0...1.4.1) (2016-05-17)


### Bug Fixes

* **tables:** fix table heading separators requiring 3 dashes instead of 2 ([ddaacfc](https://github.com/showdownjs/showdown/commit/ddaacfc)), closes [#256](https://github.com/showdownjs/showdown/issues/256)



<a name="1.4.0"></a>
## [1.4.0](https://github.com/showdownjs/showdown/compare/1.3.0...1.4.0) (2016-05-13)


### Bug Fixes

* **hashHTMLBlock:** fix issue with html breaking markdown parsing ([2746949](https://github.com/showdownjs/showdown/commit/2746949)), closes [#220](https://github.com/showdownjs/showdown/issues/220)
* **HTMLParser:** fix code tags parsing ([71a5873](https://github.com/showdownjs/showdown/commit/71a5873)), closes [#231](https://github.com/showdownjs/showdown/issues/231)
* **HTMLParser:** fix ghCodeBlocks being parsed inside code tags ([7d0436d](https://github.com/showdownjs/showdown/commit/7d0436d)), closes [#229](https://github.com/showdownjs/showdown/issues/229)
* **strikethrough:** Fix strikethrough issue with escaped chars ([5669317](https://github.com/showdownjs/showdown/commit/5669317)), closes [#214](https://github.com/showdownjs/showdown/issues/214)
* **tables:** fix tables to match github's md spec ([f58f014](https://github.com/showdownjs/showdown/commit/f58f014)), closes [#230](https://github.com/showdownjs/showdown/issues/230)

### Features

* **markdown="1":** enable parsing markdown inside HTML blocks ([c97f1dc](https://github.com/showdownjs/showdown/commit/c97f1dc)), closes [#178](https://github.com/showdownjs/showdown/issues/178)



<a name="1.3.0"></a>
## [1.3.0](https://github.com/showdownjs/showdown/compare/1.2.3...1.3.0) (2015-10-19)


### Bug Fixes

* **literalMidWordUnderscores:** fix different behavior with asterisks ([e86aea8](https://github.com/showdownjs/showdown/commit/e86aea8)), closes [#198](https://github.com/showdownjs/showdown/issues/198)
* **simpleautolink:** fix mail simpleAutoLink to ignore urls with @ symbol ([8ebb25e](https://github.com/showdownjs/showdown/commit/8ebb25e)), closes [#204](https://github.com/showdownjs/showdown/issues/204)

### Features

* **eventDispatcher:** add an event dispatcher to converter ([2734326](https://github.com/showdownjs/showdown/commit/2734326))
* **hashHTMLSpans:** add support for hashing span elements ([3097bd4](https://github.com/showdownjs/showdown/commit/3097bd4)), closes [#196](https://github.com/showdownjs/showdown/issues/196) [#175](https://github.com/showdownjs/showdown/issues/175)


<a name"1.2.3"></a>
## [1.2.3](https://github.com/showdownjs/showdown/compare/1.2.2...1.2.3) (2015-08-27)


### Bug Fixes

* **blockGamut:** fix for headings inside blockquotes ([3df70624](http://github.com/showdownjs/showdown/commit/3df70624), closes [#191](http://github.com/showdownjs/showdown/issues/191))
* **blockQuote:** fix 'github style codeblocks' not being parsed inside 'blockquote' ([ed2cf595](http://github.com/showdownjs/showdown/commit/ed2cf595), closes [#192](http://github.com/showdownjs/showdown/issues/192))
* **simpleAutoLinks:** fix emails being treated as simple urls ([7dc3fb1d](http://github.com/showdownjs/showdown/commit/7dc3fb1d), closes [#187](http://github.com/showdownjs/showdown/issues/187))
* **tables:** fix md tables being parsed inside indented code blocks. ([50256233](http://github.com/showdownjs/showdown/commit/50256233), closes [#193](http://github.com/showdownjs/showdown/issues/193))


<a name"1.2.2"></a>
## [1.2.2](https://github.com/showdownjs/showdown/compare/1.2.1...1.2.2) (2015-08-02)


### Bug Fixes

* **lists:** fix github code blocks not being parsed inside lists ([7720c88b](http://github.com/showdownjs/showdown/commit/7720c88b), closes [#142](http://github.com/showdownjs/showdown/issues/142), [#183](http://github.com/showdownjs/showdown/issues/183), [#184](http://github.com/showdownjs/showdown/issues/184))


<a name"1.2.1"></a>
## [1.2.1](https://github.com/showdownjs/showdown/compare/1.2.0...1.2.1) (2015-07-22)


### Features

* **smoothLivePreview:** fix weird effects due to parsing incomplete input ([62ba3733](http://github.com/showdownjs/showdown/commit/62ba3733))
* **subParsers/githubCodeBlock:** add extra language class to conform to html5 spec ([b7f5e32](http://github.com/showdownjs/showdown/commit/b7f5e32))


### Bug Fixes

* **tables:** 

  * fix undefined error in malformed tables ([6176977](http://github.com/showdownjs/showdown/commit/6176977))
  * add support for md span elements in table headers ([789dc18](http://github.com/showdownjs/showdown/commit/789dc18)), closes [#179](http://github.com/showdownjs/showdown/issues/179)
    
* **italicsAndBold:** 

    * fix broken em/strong tags when used with literalMidWordUnderscores ([7ee2017](http://github.com/showdownjs/showdown/commit/7ee2017)), closes [#179](http://github.com/showdownjs/showdown/issues/179)
    * fix underscores not being correctly parsed when used in conjunction with literalMidWordsUnderscores option ([c9e85f1](http://github.com/showdownjs/showdown/commit/c9e85f1))
    
* **codeSpans:** Fix issue with code html tags not being correctly escaped ([5f043ca](http://github.com/showdownjs/showdown/commit/5f043ca))

* **images:** fix alt attribute not being escaped correctly ([542194e](http://github.com/showdownjs/showdown/commit/542194e))


<a name"1.2.0"></a>
## [1.2.0](https://github.com/showdownjs/showdown/compare/1.1.0...1.2.0) (2015-07-13)

This release moves some of the most popular extensions (such as table-extension and github-extension) to core.
Also introduces a simple cli tool that you can use to quickly convert markdown files into html. 


### Bug Fixes

* **headerLevelStart:** fix for NaN error when specifying a non number as headerLevelStart param ([be72b487](http://github.com/showdownjs/showdown/commit/be72b487))


### Features

* **CLI:** simple cli tool (ALPHA) ([f6a33e40](http://github.com/showdownjs/showdown/commit/f6a33e40))
* **flavours:** add markdown presets/flavors ([7e55bceb](http://github.com/showdownjs/showdown/commit/7e55bceb), closes [#164](http://github.com/showdownjs/showdown/issues/164))
* **ghCodeBlocks:** add option to disable GH codeblocks ([c33f9888](http://github.com/showdownjs/showdown/commit/c33f9888))
* **literalMidWordUnderscores:**  add support for GFM literal midword underscores ([0c0cd7db](http://github.com/showdownjs/showdown/commit/0c0cd7db))
* **simplifiedAutoLink:** add support for GFM autolinks ([cff02372](http://github.com/showdownjs/showdown/commit/cff02372))
* **strikethrough:**  add support for GFM strikethrough ([43e9448d](http://github.com/showdownjs/showdown/commit/43e9448d))
* **tables:**  add support for GFM tables ([3a924e3c](http://github.com/showdownjs/showdown/commit/3a924e3c))
* **tasklists:** add support for GFM tasklists ([dc72403a](http://github.com/showdownjs/showdown/commit/dc72403a))


<a name"1.1.0"></a>
## [1.1.0](https://github.com/showdownjs/showdown/compare/1.0.2...1.1.0) (2015-06-18)


### Bug Fixes

* **converter.js:** add error if the passed constructor argument is not an object ([d86ed450](http://github.com/showdownjs/showdown/commit/d86ed450))
* **output modifiers:** fix for output modifiers running twice ([dcbdc61e](http://github.com/showdownjs/showdown/commit/dcbdc61e))


### Features

* **headerLevelStart:** add support for setting the header starting level ([b84ac67d](http://github.com/showdownjs/showdown/commit/b84ac67d), closes [#69](http://github.com/showdownjs/showdown/issues/69))
* **image dimensions:** add support for setting image dimensions within markdown syntax ([af82c2b6](http://github.com/showdownjs/showdown/commit/af82c2b6), closes [#143](http://github.com/showdownjs/showdown/issues/143))
* **noHeaderId:** add option to suppress automatic generation of ids in headers ([7ac893e9](http://github.com/showdownjs/showdown/commit/7ac893e9))
* **showdown.getDefaultOptions:** add method to retrieve default global options keypairs ([2de53a7d](http://github.com/showdownjs/showdown/commit/2de53a7d))


### Breaking Changes

* Deprecates `showdown.extensions` property. To migrate, extensions should use the new method `showdown.extension(<ext name>, <extension>)` to register.
  For more information on the new extension loading mechanism, please check the wiki pages.
  ([4ebd0caa](http://github.com/showdownjs/showdown/commit/4ebd0caa))


<a name"1.0.2"></a>
## [1.0.2](https://github.com/showdownjs/showdown/compare/1.0.1...1.0.2) (2015-05-28)

### Bug Fixes

* **Gruntfile.js** add missing comma in footer. This bug prevented concatenating other js scripts and libraries
  with showdown([5315508](http://github.com/showdownjs/showdown/commit/5315508). Credits to Alexandre Courtiol.


<a name"1.0.1"></a>
## [1.0.1](https://github.com/showdownjs/showdown/compare/1.0.0...1.0.1) (2015-05-27)


### Bug Fixes

* **bower.json:** update bower.json main attribute to point to dist directory ([bc3a092f](http://github.com/showdownjs/showdown/commit/bc3a092f))


<a name"1.0.0"></a>
## [1.0.0](https://github.com/showdownjs/showdown/compare/0.3.4...1.0.0) (2015-05-27)

### Release Information
This is a major code refactor with some big changes such as:
  - showdown.js file was split in several files, called sub-parsers. This should improve code maintainability.
  - angular integration was removed from core and move to its own repository, similar to what was done with extensions
  - A new extension registering system is on the "cooks" that should reduce errors when using extensions. The old mechanism
  is kept so old extensions should be compatible.

### Bug Fixes

* **extensions:** support for old extension loading mechanism ([95ed7c68](http://github.com/showdownjs/showdown/commit/95ed7c68))
* **helpers:** fix wrong function call 'escapeCharacters' due to old strayed code ([18ba4e75](http://github.com/showdownjs/showdown/commit/18ba4e75))
* **showdown.js:**
  - fix showdown extension loader ([a38c76d2](http://github.com/showdownjs/showdown/commit/a38c76d2)),
  closes [#50](http://github.com/showdownjs/showdown/issues/50),[#56](http://github.com/showdownjs/showdown/issues/56),
  [#104](http://github.com/showdownjs/showdown/issues/104), [#108](http://github.com/showdownjs/showdown/issues/108),
  [#109](http://github.com/showdownjs/showdown/issues/109), [#111](http://github.com/showdownjs/showdown/issues/111),
  [#118](http://github.com/showdownjs/showdown/issues/118), [#122](http://github.com/showdownjs/showdown/issues/122)
  - add unique id prefix and suffix to headers ([c367a4b9](http://github.com/showdownjs/showdown/commit/c367a4b9), closes [#81](http://github.com/showdownjs/showdown/issues/81), [#82](http://github.com/showdownjs/showdown/issues/82))
* **options.omitExtraWLInCodeBlocks:** fix for options.omitExtraWLInCodeBlocks only applying in gitHub flavoured code b ([e6f40e19](http://github.com/showdownjs/showdown/commit/e6f40e19))
* **showdown:** fix for options merging into globalOptions ([ddd6011d](http://github.com/showdownjs/showdown/commit/ddd6011d), closes [#153](http://github.com/showdownjs/showdown/issues/153))

### Features

* **registerExtension():** new extension loading mechanism. Now extensions can be registered using this function.
  The system, however, is not final and will probably be changed until the final version([0fd10cb] (http://github.com/showdownjs/showdown/commit/0fd10cb))
* **allowBlockIndents:** indented inline block elements can now be parsed as markdown ([f6326b84](http://github.com/showdownjs/showdown/commit/f6326b84))
* **omitExtraWLInCodeBlocks:**  add option to omit extra newline at the end of codeblocks ([141e3f5](http://github.com/showdownjs/showdown/commit/141e3f5))
* **prefixHeaderId:** add options to prefix header ids to prevent id clash ([141e3f5](http://github.com/showdownjs/showdown/commit/141e3f5))
* **Converter.options:** add getOption(), setOption() and getOptions() to Converter object ([db6f79b0](http://github.com/showdownjs/showdown/commit/db6f79b0))

### Breaking Changes
* **NAMESPACE:** showdown's namespace changed.

   To migrate your code you should update all references to `Showdown` with `showdown`.

* **Converter:** converter reference changed from `converter` to `Converter`.

   To migrate you should update all references to `Showdown.converter` with `showdown.Converter`

* **angular:** angular integration was removed from core and now lives in it's own [repository](http://github.com/showdownjs/angular/).

   If you're using angular integration, you should install ng-showdown. Ex: `bower install ng-showdown`

* **extensions:** showdown extensions were removed from core package and now live in their own repository. See the [project's github page](https://github.com/showdownjs) for available extensions
```

## File: `CONTRIBUTING.md`
```markdown
Contributing
============

If you wish to contribute please read the following quick guide.

# Issues (bug reporting)
Generally, bug reports should be in the following format:

 1. Description (Brief description of the problem)
 2. Input (input that is causing problems)
 3. Expected Output (Output that is expected)
 4. Actual Output (Actual showdown output)

ex:

**Description:**
Double asterisks do not parse as bold

**Input:**
    
    hello **world**!
     
**Expected output:**

    <p>hello <b>world</b>!

**Actual Output:**

    <p>hello **world**!</p>



# Want a Feature?
You can request a new feature by submitting an issue. If you would like to implement a new feature feel free to issue a
Pull Request.


# Pull requests (PRs)
PRs are awesome. However, before you submit your pull request consider the following guidelines:

 - Search GitHub for an open or closed Pull Request that relates to your submission. You don't want to duplicate effort.
 - When issuing PRs that change code, make your changes in a new git branch based on develop:

   ```bash
   git checkout -b my-fix-branch develop
   ```

 - Run the full test suite before submitting and make sure all tests pass (obviously =P).
 - Try to follow our [**coding style rules**](https://github.com/showdownjs/code-style/blob/master/README.md).
   Breaking them prevents the PR to pass the tests.
 - Refrain from fixing multiple issues in the same pull request. It's preferable to open multiple small PRs instead of one
   hard to review big one. Also, don't reuse old forks (or PRs) to fix new issues.
 - If the PR introduces a new feature or fixes an issue, please add the appropriate test case.
 - We use commit notes to generate the changelog. It's extremely helpful if your commit messages adhere to the
 [**AngularJS Git Commit Guidelines**](https://github.com/showdownjs/code-style/blob/master/README.md#commit-message-convention).
 - If we suggest changes then:
   - Make the required updates.
   - Re-run the Angular test suite to ensure tests are still passing.
   - Rebase your branch and force push to your GitHub repository (this will update your Pull Request):

   ```bash
   git rebase develop -i
   git push origin my-fix-branch -f
   ```
 - After your pull request is merged, you can safely delete your branch.

If you have time to contribute to this project, we feel obliged that you get credit for it.
These rules enable us to review your PR faster and will give you appropriate credit in your GitHub profile.
We thank you in advance for your contribution!


# Joining the team
We're looking for members to help maintaining Showdown.
Please see [this issue](https://github.com/showdownjs/showdown/issues/114) to express interest or comment on this note.
```

## File: `CREDITS.md`
```markdown
Credits
=======
  
  - Showdown v2
    * [Estevão Santos](https://github.com/tivie)
    * [SyntaxRules](https://github.com/SyntaxRules)

  - Showdown v1
    * [Estevão Santos](https://github.com/tivie)
    * [Pascal Deschênes](https://github.com/pdeschen)

  - Showdown v0
    * [Corey Innis](http://github.com/coreyti):<br/>
      Original GitHub project maintainer
    * [Remy Sharp](https://github.com/remy/):<br/>
      CommonJS-compatibility and more
    * [Konstantin Käfer](https://github.com/kkaefer/):<br/>
      CommonJS packaging
    * [Roger Braun](https://github.com/rogerbraun):<br/>
      Github-style code blocks
    * [Dominic Tarr](https://github.com/dominictarr):<br/>
      Documentation
    * [Cat Chen](https://github.com/CatChen):<br/>
      Export fix
    * [Titus Stone](https://github.com/tstone):<br/>
      Mocha tests, extension mechanism, and bug fixes
    * [Rob Sutherland](https://github.com/roberocity):<br/>
      The idea that lead to extensions
    * [Pavel Lang](https://github.com/langpavel):<br/>
      Code cleanup
    * [Ben Combee](https://github.com/unwiredben):<br/>
      Regex optimization
    * [Adam Backstrom](https://github.com/abackstrom):<br/>
      WebKit bugfix
    * [Pascal Deschênes](https://github.com/pdeschen):<br/>
      Grunt support, extension fixes + additions, packaging improvements, documentation
    * [Estevão Santos](https://github.com/tivie)<br/>
      Bug fixing and late maintainer
    * [Hannah Wolfe](https://github.com/ErisDS)<br/>
      Bug fixes
    * [Alexandre Courtiol](https://github.com/acourtiol)<br/>
      Bug fixes and build optimization
    * [Karthik Balakrishnan](https://github.com/torcellite)<br/>
      Support for table alignment
    * [rheber](https://github.com/rheber)<br/>
      Cli
      

  - Original Project
    * [John Gruber](http://daringfireball.net/projects/markdown/)<br/>
      Author of Markdown
    * [John Fraser](http://attacklab.net/)<br/>
      Author of Showdown
```

## File: `DONATIONS.md`
```markdown
We would like to thank everyone that contributed to this library. If you find our library useful and wish to donate as well, you can do so [through patreon](https://www.patreon.com/showdownjs) or directly [through paypal](https://www.paypal.me/tiviesantos)!! Your contribution will be greatly appreciated.

# Sponsors

## Platinum Supporters

## Gold Supporters

## Silver Supporters


# Patron Supporters

## Awesome Supporter

## Cool Supporter

## Supporter

 - Ricardo Jordão
 
 - Tiago Silva


---

# One Time Donors

- [**Learn on demand Systems**](http://www.learnondemandsystems.com/) (1000$)

- **Nothing AG** (25€)

    > Thank you for developing Showdown :)

- **Sam Huffman** (15$)

    > Thanks for the great work on showdown.js! I've been looking for a good solution to serve wiki-like text to a browser and render as
    HTML but nearly gave up after mixed success with wikitext. Your library gets me very close to where I want to be.

- **Maya Lekova** (10$)

    > Great work with the showdown library! I just used it and it worked exactly the way I expected 
      (given a complex inline HTML inside the Markdown, which renders fine with other viewers). 
      The other libraries I've tried (markdown-it and marked) produced a lot of bogus output. Y
      our library saved me at least half a day, thanks! Good luck :)

- **Lin Wang** (10$)

- **Walter Schnell** (10$)

- **ivanhjc** (5$)

- **Asbjørn Ulsberg** (5$)

    > Thanks for the ShowdownJS support!

- **Juan Marcelo Russo** (1$)
```

## File: `Gruntfile.js`
```javascript
/**
 * Created by Tivie on 12-11-2014.
 */

module.exports = function (grunt) {

  if (grunt.option('q') || grunt.option('quiet')) {
    require('quiet-grunt');
  }

  /**
   * Load common tasks for legacy and normal tests
   */
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-mocha-test');
  grunt.loadNpmTasks('grunt-endline');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  // Project configuration.
  var config = {
    pkg: grunt.file.readJSON('package.json'),

    concat: {
      dist: {
        options: {
          sourceMap: true,
          banner: ';/*! <%= pkg.name %> v <%= pkg.version %> - <%= grunt.template.today("dd-mm-yyyy") %> */\n(function(){\n',
          footer: '}).call(this);\n'
        },
        src: [
          'src/options.js',
          'src/showdown.js',
          'src/helpers.js',
          'src/subParsers/makehtml/*.js',
          'src/subParsers/makemarkdown/*.js',
          'src/converter.js',
          'src/loader.js'
        ],
        dest: 'dist/<%= pkg.name %>.js'
      },
      cli: {
        src: [
          'src/cli/cli.js'
        ],
        dest: 'bin/showdown.js'
      },
      test: {
        src: '<%= concat.dist.src %>',
        dest: '.build/<%= pkg.name %>.js',
        options: {
          sourceMap: false
        }
      }
    },

    clean: ['.build/'],

    uglify: {
      dist: {
        options: {
          sourceMap: true,
          banner: '/*! <%= pkg.name %> v <%= pkg.version %> - <%= grunt.template.today("dd-mm-yyyy") %> */'
        },
        files: {
          'dist/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
        }
      },
      cli: {
        options: {
          sourceMap: false,
          banner: '#!/usr/bin/env node'
        },
        files: {
          'bin/showdown.js': ['<%= concat.cli.dest %>']
        }
      }
    },

    endline: {
      dist: {
        files: {
          'dist/<%= pkg.name %>.js': 'dist/<%= pkg.name %>.js',
          'dist/<%= pkg.name %>.min.js': 'dist/<%= pkg.name %>.min.js'
        }
      }
    },

    jshint: {
      options: {
        jshintrc: '.jshintrc'
      },
      files: [
        'Gruntfile.js',
        'src/**/*.js',
        'test/**/*.js'
      ]
    },

    eslint: {
      options: {
        overrideConfigFile: '.eslintrc.json'
      },
      target: [
        'Gruntfile.js',
        'src/**/*.js',
        'test/**/*.js'
      ]
    },

    conventionalChangelog: {
      options: {
        changelogOpts: {
          preset: 'angular'
        }
      },
      release: {
        src: 'CHANGELOG.md'
      }
    },

    conventionalGithubReleaser: {
      release: {
        options: {
          auth: {
            type: 'oauth',
            token: process.env.GH_TOEKN
          },
          changelogOpts: {
            preset: 'angular'
          }
        }
      }
    },

    mochaTest: {
      functional: {
        src: 'test/functional/**/*.js',
        options: {
          timeout: 3000,
          ignoreLeaks: true,
          reporter: 'spec',
          require: ['test/bootstrap.js']
        }
      },
      unit: {
        src: 'test/unit/**/*.js',
        options: {
          timeout: 3000,
          ignoreLeaks: true,
          reporter: 'spec',
          require: ['test/bootstrap.js']
        }
      },
      single: {
        options: {
          timeout: 3000,
          ignoreLeaks: false,
          reporter: 'spec',
          require: ['test/bootstrap.js']
        }
      },
      cli: {
        src: 'test/unit/cli.js',
        options: {
          timeout: 3000,
          ignoreLeaks: false,
          reporter: 'spec',
          require: ['test/bootstrap.js']
        }
      }
    }
  };

  grunt.initConfig(config);

  /**
   * Generate Changelog
   */
  grunt.registerTask('generate-changelog', function () {
    'use strict';
    grunt.loadNpmTasks('grunt-conventional-changelog');
    grunt.loadNpmTasks('grunt-conventional-github-releaser');
    grunt.task.run('conventionalChangelog');
  });

  /**
   * Lint tasks
   */
  grunt.registerTask('lint', function () {
    'use strict';
    grunt.loadNpmTasks('grunt-eslint');
    grunt.task.run('jshint', 'eslint');
  });

  /**
   * Performance task
   */
  grunt.registerTask('performancejs', function () {
    'use strict';
    var perf = require('./test/performance/performance.js');
    perf.runTests();
    perf.generateLogs();
  });

  /**
   * Run a single test
   */
  grunt.registerTask('single-test', function (file) {
    'use strict';
    grunt.config.merge({
      mochaTest: {
        single: {
          src: file
        }
      }
    });

    grunt.task.run(['lint', 'concat:test', 'mochaTest:single', 'clean']);
  });

  /**
   * Tasks
   */
  grunt.registerTask('test', ['clean', 'lint', 'concat:test', 'mochaTest:unit', 'mochaTest:functional', 'clean']);
  grunt.registerTask('test-functional', ['concat:test', 'mochaTest:functional', 'clean']);
  grunt.registerTask('test-unit', ['concat:test', 'mochaTest:unit', 'clean']);
  grunt.registerTask('test-cli', ['clean', 'lint', 'concat:test', 'mochaTest:cli', 'clean']);

  grunt.registerTask('performance', ['concat:test', 'performancejs', 'clean']);
  grunt.registerTask('build', ['test', 'concat:dist', 'concat:cli', 'uglify:dist', 'uglify:cli', 'endline']);
  grunt.registerTask('build-without-test', ['concat:dist', 'uglify', 'endline']);
  grunt.registerTask('prep-release', ['build', 'performance', 'generate-changelog']);

  // Default task(s).
  grunt.registerTask('default', ['test']);
};
```

## File: `karma.browserstack.js`
```javascript
module.exports = function (config) {
  config.set({
    // global config of your BrowserStack account
    browserStack: {
      username: process.env.BROWSERSTACK_USERNAME,
      accessKey: process.env.BROWSERSTACK_ACCESSKEY,
      project: process.env.BROWSERSTACK_PROJECT_NAME || 'showdown',
      build: process.env.BROWSERSTACK_BUILD_NAME || require('./package.json').version,
      name: process.env.COMMIT_MSG || 'Unit Testing'
    },

    // define browsers
    customLaunchers: {
      bstack_chrome_windows: {
        base: 'BrowserStack',
        browser: 'chrome',
        browser_version: '49',
        os: 'Windows',
        os_version: '10'
      },
      bstack_firefox_windows: {
        base: 'BrowserStack',
        browser: 'firefox',
        browser_version: '44',
        os: 'Windows',
        os_version: '10'
      },
      bstack_edge_windows: {
        base: 'BrowserStack',
        browser: 'edge',
        browser_version: '15',
        os: 'Windows',
        os_version: '10'
      },
      bstack_ie11_windows: {
        base: 'BrowserStack',
        browser: 'ie',
        browser_version: '11',
        os: 'Windows',
        os_version: '10'
      },
      bstack_macos_safari: {
        base: 'BrowserStack',
        browser: 'safari',
        browser_version: '10.1',
        os: 'OS X',
        os_version: 'Sierra'
      },
      bstack_iphoneX: {
        base: 'BrowserStack',
        browser: 'safari',
        os: 'ios',
        os_version: '11.0',
        device: 'iPhone X',
        real_mobile: true
      },
      bstack_android: {
        base: 'BrowserStack',
        browser: 'chrome',
        os: 'android',
        os_version:'4.4',
        device: 'Samsung Galaxy Tab 4',
        realMobile: true
      }
    },

    browsers: ['bstack_chrome_windows', 'bstack_firefox_windows', 'bstack_ie11_windows', 'bstack_edge_windows', 'bstack_iphoneX', 'bstack_macos_safari', 'bstack_android'],
    frameworks: ['mocha', 'chai'],
    reporters: ['dots', 'BrowserStack'],
    files: [
      { pattern: '.build/showdown.js'},
      { pattern: 'src/options.js'},
      // tests
      { pattern: 'test/unit/showdown*.js' }
      //{ pattern: 'test/functional/showdown*.js' },
    ],
    singleRun: true,
    concurrency: Infinity
  });
};
```

## File: `karma.conf.js`
```javascript
module.exports = function (config) {
  config.set({
    client: {
      captureConsole: true
    },
    browserConsoleLogOptions: {
      level: 'log',
      format: '%b %T: %m',
      terminal: true
    },
    logLevel: config.LOG_LOG,
    frameworks: ['mocha', 'chai'],
    files: [
      { pattern: '.build/showdown.js'},
      { pattern: 'src/options.js'},
      // tests
      { pattern: 'test/unit/showdown*.js' },
      { pattern: 'test/functional/showdown*.js' },
    ],
    reporters: ['progress'],
    port: 9876,  // karma web server port
    colors: true,
    browsers: ['ChromeHeadless', 'FirefoxHeadless', 'jsdom'],
    autoWatch: false,
    singleRun: true, // Karma captures browsers, runs the tests and exits
    //concurrency: Infinity,
    customLaunchers: {
      'FirefoxHeadless': {
        base: 'Firefox',
        flags: [
          '-headless',
        ]
      }
    },
  });
};
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2018,2021 ShowdownJS

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `mkdocs.yml`
```yaml
site_name: Showdown documentation
site_description: Showdown is a JavaScript Markdown to HTML converter

theme:
  name: material
  logo: http://showdownjs.com/apple-touch-icon.png
  favicon: http://showdownjs.com/apple-touch-icon.png
  icon:
    repo: fontawesome/brands/github
  features:
    - navigation.tabs

markdown_extensions:
  - admonition
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true 
  - pymdownx.tasklist
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg

extra_css:
  - assets/extra.css 
  
repo_url: https://github.com/showdownjs/showdown
repo_name: showdownjs/showdown
site_dir: public

nav:
  - Home:
    - Introduction: index.md
    - Donations: donations.md
    - Credits: credits.md
  - Quickstart:
    - Quickstart: quickstart.md
    - Showdown's Markdown syntax: markdown-syntax.md
    - Compatibility: compatibility.md
  - Configuration:
    - Showdown options: configuration.md
    - Available options: available-options.md
    - Flavors: flavors.md
  - CLI: cli.md
  - Integrations: integrations.md
  - Extensions:
    - Overview: extensions.md
    - Create an extension: create-extension.md
    - List of known extensions: extensions-list.md 
  - Tutorials: tutorials/index.md
```

## File: `package.json`
```json
{
  "name": "showdown",
  "version": "3.0.0-alpha",
  "description": "A Markdown to HTML converter written in Javascript",
  "author": "Estevão Santos",
  "homepage": "http://showdownjs.com/",
  "keywords": [
    "markdown",
    "converter"
  ],
  "contributors": [
    "John Gruber",
    "John Fraser",
    "Corey Innis",
    "Remy Sharp",
    "Konstantin Käfer",
    "Roger Braun",
    "Dominic Tarr",
    "Cat Chen",
    "Titus Stone",
    "Rob Sutherland",
    "Pavel Lang",
    "Ben Combee",
    "Adam Backstrom",
    "Pascal Deschênes",
    "Estevão Santos"
  ],
  "funding": {
    "type": "individual",
    "url": "https://www.paypal.me/tiviesantos"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/showdownjs/showdown.git",
    "web": "https://github.com/showdownjs/showdown"
  },
  "license": "MIT",
  "main": "./dist/showdown.js",
  "scripts": {
    "test": "grunt test"
  },
  "bin": {
    "showdown": "bin/showdown.js"
  },
  "files": [
    "bin",
    "dist"
  ],
  "devDependencies": {
    "chai": "*",
    "chai-match": "*",
    "grunt": "^1.4.1",
    "grunt-contrib-clean": "^2.0.0",
    "grunt-contrib-concat": "^2.0.0",
    "grunt-contrib-jshint": "^3.1.0",
    "grunt-contrib-uglify": "^5.0.1",
    "grunt-conventional-changelog": "^6.1.0",
    "grunt-conventional-github-releaser": "^1.0.0",
    "grunt-endline": "^0.7.0",
    "grunt-eslint": "^24.0.0",
    "grunt-mocha-test": "^0.13.3",
    "grunt-simple-mocha": "^0.4.0",
    "karma": "^6.3.17",
    "karma-browserstack-launcher": "^1.6.0",
    "karma-chai": "^0.1.0",
    "karma-chrome-launcher": "^3.1.1",
    "karma-firefox-launcher": "^2.1.2",
    "karma-jsdom-launcher": "^12.0.0",
    "karma-mocha": "^2.0.1",
    "load-grunt-tasks": "^5.1.0",
    "performance-now": "^2.1.0",
    "quiet-grunt": "^0.2.0",
    "semver-sort": "^1.0.0",
    "sinon": "*",
    "source-map-support": "^0.5.21"
  },
  "dependencies": {
    "commander": "^9.0.0",
    "jsdom": "^19.0.0"
  },
  "overrides": {
    "minimist": "^1.2.6"
  }
}
```

## File: `performance.json`
```json
{"2.0.0":[{"suiteName":"Basic","cycles":50,"tests":[{"name":"Simple \"Hello World\"","time":0.5814020752906799,"maxTime":12.278934955596924,"minTime":0.15148591995239258},{"name":"performance.testfile.md","time":35.49076347827911,"maxTime":79.40457594394684,"minTime":29.04559099674225}]},{"suiteName":"subParsers","cycles":20,"tests":[{"name":"hashHTMLBlocks","time":4.561372250318527,"maxTime":7.806509017944336,"minTime":2.461485981941223},{"name":"anchors","time":2.9101044595241548,"maxTime":6.510464072227478,"minTime":1.055580973625183},{"name":"blockQuotes","time":4.141605257987976,"maxTime":19.022807955741882,"minTime":2.540547013282776},{"name":"codeBlocks","time":0.263570636510849,"maxTime":0.8583500385284424,"minTime":0.19387996196746826},{"name":"codeSpans","time":0.3651615560054779,"maxTime":1.4206420183181763,"minTime":0.27775895595550537},{"name":"detab","time":0.054944151639938356,"maxTime":0.11614596843719482,"minTime":0.04707300662994385},{"name":"encodeAmpsAndAngles","time":0.144669109582901,"maxTime":0.796051025390625,"minTime":0.09184098243713379},{"name":"encodeBackslashEscapes","time":0.08684400320053101,"maxTime":0.2664440870285034,"minTime":0.0629270076751709},{"name":"encodeCode","time":0.6048604607582092,"maxTime":1.1443489789962769,"minTime":0.5217140913009644},{"name":"escapeSpecialCharsWithinTagAttributes","time":0.2064647912979126,"maxTime":0.2871870994567871,"minTime":0.1843109130859375},{"name":"githubCodeBlocks","time":0.25113869905471803,"maxTime":1.0032700300216675,"minTime":0.19171404838562012},{"name":"hashBlock","time":0.038335990905761716,"maxTime":0.10441303253173828,"minTime":0.034361958503723145},{"name":"hashElement","time":0.0046201348304748535,"maxTime":0.05286991596221924,"minTime":0.0013968944549560547},{"name":"hashHTMLSpans","time":5.228999066352844,"maxTime":9.835397958755493,"minTime":4.239645004272461},{"name":"hashPreCodeTags","time":0.15527103543281556,"maxTime":0.7053269147872925,"minTime":0.11698400974273682},{"name":"headers","time":2.277534711360931,"maxTime":4.824635028839111,"minTime":1.6311440467834473},{"name":"horizontalRule","time":0.1592068076133728,"maxTime":0.27559399604797363,"minTime":0.14848291873931885},{"name":"images","time":0.15910540223121644,"maxTime":0.3903430700302124,"minTime":0.1241079568862915},{"name":"italicsAndBold","time":0.2797422528266907,"maxTime":0.7730040550231934,"minTime":0.21085107326507568},{"name":"lists","time":4.25269467830658,"maxTime":8.173315048217773,"minTime":3.1456509828567505},{"name":"outdent","time":0.18059219121932985,"maxTime":0.23801898956298828,"minTime":0.16182196140289307},{"name":"paragraphs","time":8.96755729317665,"maxTime":11.331398010253906,"minTime":7.8572129011154175},{"name":"spanGamut","time":2.985103452205658,"maxTime":4.162191033363342,"minTime":2.48593008518219},{"name":"strikethrough","time":0.006921297311782837,"maxTime":0.09889602661132812,"minTime":0.001326918601989746},{"name":"stripLinkDefinitions","time":1.9106478571891785,"maxTime":2.8545520305633545,"minTime":1.446552038192749},{"name":"tables","time":0.008185452222824097,"maxTime":0.12662196159362793,"minTime":0.0015370845794677734},{"name":"unescapeSpecialChars","time":0.013451296091079711,"maxTime":0.07347309589385986,"minTime":0.009706974029541016}]}]}
```

## File: `performance.log.md`
```markdown
# Performance Tests for showdown


## [version 2.0.0](https://github.com/showdownjs/showdown/tree/2.0.0)

### Test Suite: Basic (50 cycles)
| test | avgTime | max | min |
|:-----|--------:|----:|----:|
|Simple "Hello World"|0.581|12.279|0.151|
|performance.testfile.md|35.491|79.405|29.046|

### Test Suite: subParsers (20 cycles)
| test | avgTime | max | min |
|:-----|--------:|----:|----:|
|hashHTMLBlocks|4.561|7.807|2.461|
|anchors|2.910|6.510|1.056|
|blockQuotes|4.142|19.023|2.541|
|codeBlocks|0.264|0.858|0.194|
|codeSpans|0.365|1.421|0.278|
|detab|0.055|0.116|0.047|
|encodeAmpsAndAngles|0.145|0.796|0.092|
|encodeBackslashEscapes|0.087|0.266|0.063|
|encodeCode|0.605|1.144|0.522|
|escapeSpecialCharsWithinTagAttributes|0.206|0.287|0.184|
|githubCodeBlocks|0.251|1.003|0.192|
|hashBlock|0.038|0.104|0.034|
|hashElement|0.005|0.053|0.001|
|hashHTMLSpans|5.229|9.835|4.240|
|hashPreCodeTags|0.155|0.705|0.117|
|headers|2.278|4.825|1.631|
|horizontalRule|0.159|0.276|0.148|
|images|0.159|0.390|0.124|
|italicsAndBold|0.280|0.773|0.211|
|lists|4.253|8.173|3.146|
|outdent|0.181|0.238|0.162|
|paragraphs|8.968|11.331|7.857|
|spanGamut|2.985|4.162|2.486|
|strikethrough|0.007|0.099|0.001|
|stripLinkDefinitions|1.911|2.855|1.447|
|tables|0.008|0.127|0.002|
|unescapeSpecialChars|0.013|0.073|0.010|


```

## File: `README.md`
```markdown
![Showdown][sd-logo]

![Build Status: Linux](https://github.com/showdownjs/showdown/actions/workflows/node.linux.yml/badge.svg)
![Build Status: Windows](https://github.com/showdownjs/showdown/actions/workflows/node.win.yml/badge.svg)
[![Browserstack Tests](https://automate.browserstack.com/badge.svg?badge_key=VTIvTDNqWVdaTHljbS9RNmYrcTBiL0Uxc3dkRDhaN1dPaXpPb2VOc1B2VT0tLU1Ib09kVjVzMjhFcHExbWFSWlJEV3c9PQ==--1fb92e1730e4a00630d17d533822de6403ca65ec)](https://automate.browserstack.com/public-build/VTIvTDNqWVdaTHljbS9RNmYrcTBiL0Uxc3dkRDhaN1dPaXpPb2VOc1B2VT0tLU1Ib09kVjVzMjhFcHExbWFSWlJEV3c9PQ==--1fb92e1730e4a00630d17d533822de6403ca65ec)
[![npm version](https://badge.fury.io/js/showdown.svg)](http://badge.fury.io/js/showdown)
[![Bower version](https://badge.fury.io/bo/showdown.svg)](http://badge.fury.io/bo/showdown)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/tiviesantos)

------

Showdown is a JavaScript Markdown to HTML converter, based on the original works by John Gruber.
Showdown can be used client side (in the browser) or server side (with Node.js).

## Live DEMO



As you know, ShowdownJS is a free library and it will remain free forever. However, maintaining and improving the library costs time and money.

If you like our work and find our library useful, please donate through [PayPal](https://www.paypal.me/tiviesantos)! Your contribution will be greatly appreciated and help me continue to develop this awesome library.

## License

ShowdownJS v 2.0 is released under the MIT license.
Previous versions are released under BSD.

## Who uses Showdown (or a fork)

 - [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
 - [Meteor](https://www.meteor.com/)
 - [Stackexchange](http://stackexchange.com/) - forked as [PageDown](https://code.google.com/p/pagedown/)
 - [docular](https://github.com/Vertafore/docular)
 - [md-page](https://github.com/oscarmorrison/md-page)
 - [QCObjects](https://qcobjects.dev)
 - [and some others...](https://www.npmjs.com/browse/depended/showdown)

## Installation

### Download tarball

You can download the latest release tarball directly from [releases][releases].

### Bower

    bower install showdown

### npm (server-side)

    npm install showdown

### NuGet package

    PM> Install-Package showdownjs

The NuGet Packages can be found [here](https://www.nuget.org/packages/showdownjs/).

### CDN

You can also use one of several CDNs available: 

* jsDelivr

        https://cdn.jsdelivr.net/npm/showdown@<version tag>/dist/showdown.min.js

* cdnjs

        https://cdnjs.cloudflare.com/ajax/libs/showdown/<version tag>/showdown.min.js

* unpkg
       
        https://unpkg.com/showdown/dist/showdown.min.js

*Note*: replace `<version tag>` with an actual full length version you're interested in e.g. `1.9.0`
## Browser Compatibility

Showdown has been tested successfully with:

  * Firefox 1.5 and 2.0
  * Chrome 12.0
  * Internet Explorer 6 and 7
  * Safari 2.0.4
  * Opera 8.54 and 9.10
  * Netscape 8.1.2
  * Konqueror 3.5.4

In theory, Showdown will work in any browser that supports ECMA 262 3rd Edition (JavaScript 1.5).
The converter itself might even work in things that aren't web browsers, like Acrobat.  No promises.


## Node compatibility

Showdown is intended to work on any supported Node.js version (see the [Node.js releases schedule](https://nodejs.org/en/about/releases/). The code may work with previous versions of Node.js, but no accomidations are made to ensure it does. 


## Legacy version

If you're looking for showdown v<1.0.0, you can find it in the [**legacy branch**][legacy-branch].

## Changelog

You can check the full [changelog][changelog]

## Extended documentation
Check our [wiki pages][wiki] for examples and a more in-depth documentation.


## Quick Example

### Node

```js
var showdown  = require('showdown'),
    converter = new showdown.Converter(),
    text      = '# hello, markdown!',
    html      = converter.makeHtml(text);
```

### Browser

```js
var converter = new showdown.Converter(),
    text      = '# hello, markdown!',
    html      = converter.makeHtml(text);
```

### Output 

Both examples should output...

```html
    <h1 id="hellomarkdown">hello, markdown!</h1>
```

## Options

You can change some of showdown's default behavior through options. 

### Setting options

Options can be set:

#### Globally

Setting a "global" option affects all instances of showdown

```js
showdown.setOption('optionKey', 'value');
```

#### Locally
Setting a "local" option only affects the specified Converter object. 
Local options can be set:

 * **through the constructor**
    ```js
    var converter = new showdown.Converter({optionKey: 'value'});
    ```

 * **through the setOption() method**
    ```js
    var converter = new showdown.Converter();
    converter.setOption('optionKey', 'value');
    ```

### Getting an option

Showdown provides 2 methods (both local and global) to retrieve previous set options.

#### getOption()

```js
// Global
var myOption = showdown.getOption('optionKey');

//Local
var myOption = converter.getOption('optionKey');
```

#### getOptions()

```js
// Global
var showdownGlobalOptions = showdown.getOptions();

//Local
var thisConverterSpecificOptions = converter.getOptions();
```

### Retrieve the default options

You can get showdown's default options with:
```js
var defaultOptions = showdown.getDefaultOptions();
```

### Valid Options

 * **omitExtraWLInCodeBlocks**: (boolean) [default false] Omit the trailing newline in a code block. Ex:
   
    This:
    ```html
    <code><pre>var foo = 'bar';
    </pre></code>
    ```
    Becomes this:
    ```html
    <code><pre>var foo = 'bar';</pre></code>
    ```

 * **noHeaderId**: (boolean) [default false] Disable the automatic generation of header ids.
   Setting to true overrides **prefixHeaderId**

 * **customizedHeaderId**: (boolean) [default false] Use text in curly braces as header id. **(since v1.7.0)**
   Example:
   ```
   ## Sample header {real-id}     will use real-id as id
   ```

 * **ghCompatibleHeaderId**: (boolean) [default false] Generate header ids compatible with github style
   (spaces are replaced with dashes and a bunch of non alphanumeric chars are removed) **(since v1.5.5)**

 * **prefixHeaderId**: (string/boolean) [default false] Add a prefix to the generated header ids.
   Passing a string will prefix that string to the header id. Setting to `true` will add a generic 'section' prefix.

 * **rawPrefixHeaderId**: (boolean) [default false] Setting this option to true will prevent showdown from modifying the prefix.
   This might result in malformed IDs (if, for instance, the " char is used in the prefix).
   Has no effect if prefixHeaderId is set to false. **(since v 1.7.3)**

 * **rawHeaderId**: (boolean) [default false] Remove only spaces, ' and " from generated header ids (including prefixes),
    replacing them with dashes (-). WARNING: This might result in malformed ids **(since v1.7.3)**
 
 * **headerLevelStart**: (integer) [default 1] Set the header starting level. For instance, setting this to 3 means that

    ```md
    # foo
    ```
    will be parsed as 
    
    ```html
    <h3>foo</h3>
    ```

 * **parseImgDimensions**: (boolean) [default false] Enable support for setting image dimensions from within markdown syntax.
   Examples:
   ```
   ![foo](foo.jpg =100x80)     simple, assumes units are in px
   ![bar](bar.jpg =100x*)      sets the height to "auto"
   ![baz](baz.jpg =80%x5em)  Image with width of 80% and height of 5em
   ```

 * **simplifiedAutoLink**: (boolean) [default false] Turning this option on will enable automatic linking to urls.
   This means that:

   ```md
   some text www.google.com
   ```
   will be parsed as 
   ```html
   <p>some text <a href="www.google.com">www.google.com</a>
   ```
 
 * ~~**excludeTrailingPunctuationFromURLs**: (boolean) [default false] This option excludes trailing punctuation from autolinking urls.
   Punctuation excluded: `. !  ? ( )`. Only applies if **simplifiedAutoLink** option is set to `true`.~~
   
 * **literalMidWordUnderscores**: (boolean) [default false] Turning this on will stop showdown from interpreting
   underscores in the middle of words as `<em>` and `<strong>` and instead treat them as literal underscores.

   Example:
   
   ```md
   some text with__underscores__in middle
   ```
   will be parsed as
   ```html
   <p>some text with__underscores__in middle</p>
   ```

 * ~~**literalMidWordAsterisks**: (boolean) [default false] Turning this on will stop showdown from interpreting asterisks
   in the middle of words as `<em>` and `<strong>` and instead treat them as literal asterisks.~~
   
 * **strikethrough**: (boolean) [default false] Enable support for strikethrough syntax.
   `~~strikethrough~~` as `<del>strikethrough</del>`
   
 * **tables**: (boolean) [default false] Enable support for tables syntax. Example:
    
   ```md
   | h1    |    h2   |      h3 |
   |:------|:-------:|--------:|
   | 100   | [a][1]  | ![b][2] |
   | *foo* | **bar** | ~~baz~~ |
   ```
   
   See the wiki for more info

 * **tablesHeaderId**: (boolean) [default false] If enabled adds an id property to table headers tags.

 * **ghCodeBlocks**: (boolean) [default true] Enable support for GFM code block style.

 * **tasklists**: (boolean) [default false] Enable support for GFM tasklists. Example:
 
   ```md
    - [x] This task is done
    - [ ] This is still pending
   ```
 * **smoothLivePreview**: (boolean) [default false] Prevents weird effects in live previews due to incomplete input
 
 * **smartIndentationFix**: (boolean) [default false] Tries to smartly fix indentation problems related to es6 template
   strings in the midst of indented code.

 * **disableForced4SpacesIndentedSublists**: (boolean) [default false] Disables the requirement of indenting sublists
   by 4 spaces for them to be nested, effectively reverting to the old behavior where 2 or 3 spaces were enough.
   **(since v1.5.0)**
 
 * **simpleLineBreaks**: (boolean) [default false] Parses line breaks as `<br>`, without
   needing 2 spaces at the end of the line **(since v1.5.1)**
 
   ```md
   a line  
   wrapped in two
   ```
    
   turns into:
    
   ```html
   <p>a line<br>
   wrapped in two</p>
   ```

 * **requireSpaceBeforeHeadingText**: (boolean) [default false] Makes adding a space between `#` and the header text mandatory **(since v1.5.3)**
 
 * **ghMentions**: (boolean) [default false] Enables github @mentions, which link to the username mentioned **(since v1.6.0)**
 
 * **ghMentionsLink**: (string) [default `https://github.com/{u}`] Changes the link generated by @mentions.
   Showdown will replace `{u}` with the username. Only applies if ghMentions option is enabled.
   Example: `@tivie` with ghMentionsOption set to `//mysite.com/{u}/profile` will result in `<a href="//mysite.com/tivie/profile">@tivie</a>`
 
 * **encodeEmails**: (boolean) [default true] Enable e-mail addresses encoding through the use of Character Entities, transforming ASCII e-mail addresses into its equivalent decimal entities. (since v1.6.1)

   NOTE: Prior to version 1.6.1, emails would always be obfuscated through dec and hex encoding.

 * **openLinksInNewWindow**: (boolean) [default false] Open all links in new windows
   (by adding the attribute `target="_blank"` to `<a>` tags) **(since v1.7.0)**

 * **backslashEscapesHTMLTags**: (boolean) [default false] Support for HTML Tag escaping. ex: `\<div>foo\</div>` **(since v1.7.2)**

 * **emoji**: (boolean) [default false] Enable emoji support. Ex: `this is a :smile: emoji`
   For more info on available emojis, see https://github.com/showdownjs/showdown/wiki/Emojis **(since v.1.8.0)**

 * **underline**: (boolean) [default false] ***EXPERIMENTAL FEATURE*** Enable support for underline.
   Syntax is **double** or **triple** **underscores** ex: `__underlined word__`. With this option enabled, underscores are no longer parses into `<em>` and `<strong>`.

 * **ellipsis**: (boolean) [default true] Replaces three dots with the ellipsis unicode character.

 * **completeHTMLDocument**: (boolean) [default false] Outputs a complete html document,
   including `<html>`, `<head>` and `<body>` tags' instead of an HTML fragment. (since v.1.8.5)

 * **metadata**: (boolean) [default false] Enable support for document metadata (defined at the top of the document
   between `«««` and `»»»` or between `---` and `---`).  (since v.1.8.5)
   
   ```js
   var conv = new showdown.Converter({metadata: true});
   var html = conv.makeHtml(someMd);
   var metadata = conv.getMetadata(); // returns an object with the document metadata
   ```

 * **splitAdjacentBlockquotes**: (boolean) [default false] Split adjacent blockquote blocks.(since v.1.8.6)

 * **moreStyling**: (boolean) [default false] Adds some useful classes for css styling. (since v2.0.1)
    
    - Tasklists: Adds the class `task-list-item-complete` to completed tasks items in GFM tasklists.

**NOTE**: Please note that until **version 1.6.0**, all of these options are ***DISABLED*** by default in the cli tool.


## Flavors

You can also use flavors or presets to set the correct options automatically, so that showdown behaves like popular markdown flavors.

Currently, the following flavors are available:

 * original - original markdown flavor as in [John Gruber's spec](https://daringfireball.net/projects/markdown/)
 * vanilla  - showdown base flavor (as from v1.3.1)
 * github   - GFM (GitHub Flavored Markdown)


### Global
```javascript
showdown.setFlavor('github');
```

### Instance
```javascript
converter.setFlavor('github');
```


## CLI Tool

Showdown also comes bundled with a Command Line Interface tool. You can check the [CLI wiki page][cli-wiki] for more info

## Integration with AngularJS

ShowdownJS project also provides seamlessly integration with AngularJS via a "plugin".
Please visit https://github.com/showdownjs/ngShowdown for more information.

## Integration with TypeScript

If you're using TypeScript you maybe want to use the types from [DefinitelyTyped][definitely-typed]

## Integration with SystemJS/JSPM

Integration with SystemJS can be obtained via the third party ["system-md" plugin](https://github.com/guybedford/system-md).

## Integration with VueJS

To use ShowdownJS as a Vue component quickly, you can check [vue-showdown](https://vue-showdown.js.org/).

## XSS vulnerability

Showdown doesn't sanitize the input. This is by design since markdown relies on it to allow certain features to be correctly parsed into HTML.
This, however, means XSS injection is quite possible.

Please refer to the wiki article [Markdown's XSS Vulnerability (and how to mitigate it)][xss-wiki]
for more information.

## Extensions

Showdown allows additional functionality to be loaded via extensions. (you can find a list of known showdown extensions [here][ext-wiki])
You can also find a boilerplate, to create your own extensions in [this repository][boilerplate-repo]

### Client-side Extension Usage

```js
<script src="showdown.js" />
<script src="twitter-extension.js" />

var converter = new showdown.Converter({ extensions: ['twitter'] });
```

### Server-side Extension Usage

```js
var showdown    = require('showdown'),
    myExtension = require('myExtension'),
    converter = new showdown.Converter({ extensions: ['myExtension'] });
```

## Building

Building your clone of the repository is easy.
> Prerequesites: [Node.js](https://nodejs.org/) v12, [npm](https://www.npmjs.com/package/npm) and [npx](https://www.npmjs.com/package/npx) must be installed.

1. run `npm install`.
2. run `npx grunt build` (see [`Gruntfile.js`](/Gruntfile.js)). This command:

    1. Cleans the repo.
    2. Checks code quality ([JSHint](https://jshint.com/) and [ESLint](https://eslint.org/)).
    3. Runs tests.
    4. Creates the [distributable](/showdown.js) and [minified](/showdown.min.js) files in the [`dist`](/dist) folder.

## Tests

A suite of tests is available which require Node.js.  Once Node is installed, run the following command from
the project root to install the dependencies:

    npm install

Once installed the tests can be run from the project root using:

    npm test

New test cases can easily be added.  Create a markdown file (ending in `.md`) which contains the markdown to test.
Create a `.html` file of the exact same name.  It will automatically be tested when the tests are executed with `mocha`.

## Contributing

If you wish to contribute please read the following quick guide.

### Want a Feature?
You can request a new feature by submitting an issue. If you would like to implement a new feature feel free to issue a
Pull Request.


### Pull requests (PRs)
PRs are awesome. However, before you submit your pull request consider the following guidelines:

 - Search GitHub for an open or closed Pull Request that relates to your submission. You don't want to duplicate effort.
 - When issuing PRs that change code, make your changes in a new git branch based on **develop**:

   ```bash
   git checkout -b my-fix-branch develop
   ```

 - Run the full test suite before submitting and make sure all tests pass (obviously =P).
 - Try to follow our [**coding style rules**][coding-rules]. Breaking them prevents the PR to pass the tests.
 - Refrain from fixing multiple issues in the same pull request. It's preferable to open multiple small PRs instead of one
   hard to review big one.
 - If the PR introduces a new feature or fixes an issue, **please add the appropriate test case**.
 - We use [conventional commit][conventional-commits] notes to generate the changelog that follow the conventional changelog spec. It's extremely helpful if your commit messages adhere to these [Commit Guidelines][conventional-commits].
 - Don't forget to add your name to the [CREDITS.md](https://github.com/showdownjs/showdown/blob/master/CREDITS.md) file. We like to give credit were it's due.
 - If we suggest changes then:
     - Make the required updates.
     - Re-run the test suite to ensure tests are still passing.
     - Rebase your branch and force push to your GitHub repository (this will update your Pull Request):

     ```bash
     git rebase develop -i
     git push origin my-fix-branch -f
     ```
 - After your pull request is merged, you can safely delete your branch.

If you have time to contribute to this project, we feel obliged that you get credit for it.
These rules enable us to review your PR faster and will give you appropriate credit in your GitHub profile.
We thank you in advance for your contribution!

### Joining the team
We're looking for members to help maintaining Showdown.
Please see [this issue](https://github.com/showdownjs/showdown/issues/114) to express interest or comment on this note.

## Credits
Full credit list at https://github.com/showdownjs/showdown/blob/master/CREDITS.md

Showdown is powered by:<br/>
[![webstorm](https://www.jetbrains.com/webstorm/documentation/docs/logo_webstorm.png)](https://www.jetbrains.com/webstorm/)



[sd-logo]: https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png
[legacy-branch]: https://github.com/showdownjs/showdown/tree/legacy
[releases]: https://github.com/showdownjs/showdown/releases
[changelog]: https://github.com/showdownjs/showdown/blob/master/CHANGELOG.md
[wiki]: https://github.com/showdownjs/showdown/wiki
[cli-wiki]: https://github.com/showdownjs/showdown/wiki/CLI-tool
[definitely-typed]: https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/showdown
[xss-wiki]: https://github.com/showdownjs/showdown/wiki/Markdown's-XSS-Vulnerability-(and-how-to-mitigate-it)
[ext-wiki]: https://github.com/showdownjs/showdown/wiki/extensions
[coding-rules]: https://github.com/showdownjs/code-style/blob/master/README.md
[conventional-commits]: https://www.conventionalcommits.org/
[boilerplate-repo]: https://github.com/showdownjs/extension-boilerplate
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

Security fixes are addressed for the following versions of Showdown.

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.x.x   | :x: (Known security issue with yargs dependecy) |

Showdown targets the node.js versions targeted in the [node.js release schedule](https://nodejs.org/en/about/releases/). Our test suite follows this release schedule. Consequently, older versions of node may become unusable.

## Reporting a Vulnerability

To report a vulnerability, please add an issue to our main github page: https://github.com/showdownjs/showdown/issues
```

## File: `TASKS.TODO.md`
```markdown
# ROADMAP TO VERSION 3.0


## Options

- [ ] **ghCompatibleHeaderId** (removal)

    Will be removed and **will become the default behavior**.
    
- [ ] **customizedHeaderId** (removal)

    This option introduced non compliant syntax so it really belongs in an extension.
    The new **listener extension system** allows users to directly modify and customize
    the HTML and add any attributes they wish. 

- [ ] **rawPrefixHeaderId** (removal)

    This option will be superseeded by the option `rawHeaderId`. So basically activating `rawHeaderId` will make
    showdown only to replace spaces, ', ", > and < with dashes (-) from generated header ids, including prefixes.

- [X] **literalMidWordAsterisks** (removal)

    This option is weird, hard to maintain and really... makes little sense.

- [X] **excludeTrailingPunctuationFromURLs** (removal)

    This option will be removed and will be the default behavior from now on.

- [ ] **strikethrough** (change)

    Will be enabled by default

- [ ] **disableForced4SpacesIndentedSublists** (to think/postpone)

    This was only a temporary option for backwards compatibility reason. However, most flavours support lists indented
    with 2 spaces, so it puts us in a tight spot, specially since some markdown beautifiers out there insist in
    indenting lists with 2 spaces, probably in a misguided try to follow the CommonMark spec.
    
    The CommonMark spec is, IMHO, a bit confusing for users regarding this, since list sub-blocks (and lists) 
    are determined by the spaces from the start of the line and the first character after the list mark. And the proof
    are the MD beautifiers out there, which misinterpreted the spec and made a mess 
    
    Showdown syntax is actually easier (and fully compliant with the original spec): if you indent something 4 spaces,
    it becomes a sub-block. Since lists are blocks, you must indent it 4 spaces for it to become a sub-block.
    
    Regardless, we kinda have 2 solutions:
    
    - Drop support for 2 space indentation (and make a lot of users confused since GFM, CommonMark and others allow this)
    - Create a new list subparser that can be turned on with an option, like gfmListStyle
      (but postpones even more the alpha 3.0 release since the list subparser is probably the hardest thing to rewrite)
    
    Tough choices...

- [ ] **simpleLineBreaks** (change)

    Will be removed from Github Flavor since github only does this in comments (which is weird...)

- [ ] **openLinksInNewWindow** (removal)

    Will be removed in favor of the new listener extension, which will allow users to manipulate HTML tags attributes
    directly.
    
- [ ] Revamp the option system

    Revamp the option system so that it becomes more simple. Right now, it's really confusing. And option names are weird
    too. The idea is to pass options to the constructor under an option object, that can have hierarchical structure.
    Ex:
    
    ```js
    var conv = new showdown.Converter({ 
      options: { 
        links: {
          autoLinks: true
        },
        headings: {
          startLevel: 2
        }
      }
    });
    ``` 

## Legacy Code Removal
- [ ] Legacy extension support
        
    Old extensions that inject directly into extensions object property will no longer be supported
    
- [ ] HTML and OUTPUT extensions
    
    HTML and OTP extensions will be dropped in favor of Listener Extensions. We might even give them a new name
    
## Subparsers
- [X] **Anchors**: Revamp the anchors subparser so it calls strikethrough, bold, italic and underline directly
- [X] **autoLinks**: Fix some lingering bugs and issues with autolinks

## Priority Bugs
- [X] **#355**: *simplifiedAutoLink URLs inside parenthesis followed by another character are not parsed correctly*
- [X] **#534**: *Multiple parentheses () in url link is not parsed correctly*
- [ ] **#367**: *sublists rendering with 2 spaces* - related to disableForced4SpacesIndentedSublists option...
- [ ] **#537**: *master branch doesn't work in a web worker*

## CLI
- [ ] Refactor the CLI
- [ ] **#381**: *Support for src and dst directories in showdown cli*
- [X] **#584**: *Fails to read from stdin*
- [X] **#554**: *CLI not working with jsdom v10*

## Other stuff
- [X] Regexp rewrite for more performance oompf
- [X] Full unit testing
- [ ] Better error reporting

## Stuff that probably won't make it to v2.0
- [ ] **#486**: *A backslash at the end of the line is a hard line break*
- [ ] **#548**: *anchors and images of subParser are errors when they are specific strings*
- [ ] **#549**: *Strange parsing issue with `<pre><code>`*
- [ ] Rethink the global variable

## NEW Features

### Event system
- [X] Listener system revamp
- [ ] Standardize events for all event types
- [ ] Unit testing
- [ ] Functional testing

This should address:
- **#567**: Allow not making header ids lowercase
- **#540**: Add complete class to the tasklist list element

### MD to HTML conversion
- [X] Basic support
- [X] Basic functional testcase
- [ ] Advanced support for all showdown MD features
- [ ] Advanced functional testcase
- [ ] Unit testing

## Documentation (for v2.0)
- [ ] Options
- [ ] Extensions (and the new event system)
- [ ] Cookbook (with stuff for backwards compatibility, specially regarding removed options)

## Browser Testing

- [X] Implement unit tests in Karma
- [ ] Implement functional tests in Karma
- [ ] Integrate with browserstack
```

## File: `docs/available-options.md`
```markdown
!!! warning ""
    Starting from the version `1.6.0` and earlier, all the options are `disabled` by default in the cli tool.

### backslashEscapesHTMLTags

Support escaping of HTML tags.

* type: `boolean`
* default value: `false`
* introduced in: `1.7.2`

=== "input"
    
    ```html
    \<div>foo\</div>
    ```

=== "output (value is `true`)"

    ```html
    <p>&lt;div&gt;foo&lt;/div&gt;</p>
    ```

### completeHTMLDocument

Output a complete HTML document, including `<html>`, `<head>`, and `<body>` tags instead of an HTML fragment.

* type: `boolean`
* default value: `false`
* introduced in: `1.8.5`

### customizedHeaderId

Set custom ID for a heading.

!!! warning ""
    This option can be overridden with the [`noHeaderId`](#noheaderid) option.

* type: `boolean`
* default value: `false`
* introduced in: `1.7.0`

=== "code"

    ```html
    ## Sample heading {mycustomid}
    ```

=== "output"

    ```html
    <h1 id="mycustomid">This is a heading</h1>
    ```

!!! hint ""
    For better readability and human-friendliness of the heading IDs, it is also recommended to set the [`ghCompatibleHeaderId`](#ghcompatibleheaderid) option to `true`.

### disableForced4SpacesIndentedSublists

Disable the rule of 4 spaces to indent sub-lists. If enabled, this option effectively reverts to the old behavior where you can indent sub-lists with 2 or 3 spaces.

* type: `boolean`
* default value: `false`
* introduced in: `1.5.0`

=== "input"
    
    ```
    - one
      - two

    ...

    - one
        - two
    ```

=== "output (value is `false`)"

    ```html
    <ul>
    <li>one</li>
    <li>two</li>
    </ul>
    <p>...</p>
    <ul>
    <li>one
        <ul>
            <li>two</li>
        </ul>
    </li>
    </ul>
    ```

=== "output (value is `true`)"

    ```html
    <ul>
    <li>one
        <ul>
            <li>two</li>
        </ul>
    </li>
    </ul>
    <p>...</p>
    <ul>
    <li>one
        <ul>
            <li>two</li>
        </ul>
    </li>
    </ul>
    ```

### emoji

Enable emoji support. For more info on available emojis, see https://github.com/showdownjs/showdown/wiki/Emojis (since v.1.8.0)

* type: `boolean`
* default value: `false`
* introduced in: `1.8.0`

=== "input"
    
    ```
    this is a :smile: emoji
    ```

=== "output (value is `false`)"

    ```html
    <p>this is a :smile: emoji</p>
    ```

=== "output (value is `true`)"

    ```html
    <p>this is a 😄 emoji</p>
    ```

!!! hint "Full list of supported emojies"

    Check the [Showdown Wiki](https://github.com/showdownjs/showdown/wiki/Emojis#emoji-list) for a full list of supported emojies.    

### encodeEmails

Enable automatic obfuscation of email addresses. During this process, email addresses are encoded via Character Entities, transforming ASCII email addresses into their equivalent decimal entities.

* type: `boolean`
* default value: `false`
* introduced in: `1.6.1`

=== "input"
    
    ```
    <myself@example.com>
    ```

=== "output (value is `false`)"

    ```html
    <a href="mailto:myself@example.com">myself@example.com</a>
    ```

=== "output (value is `true`)"

    ```html
    <a href="&#109;&#97;&#105;&#108;t&#x6f;&#x3a;&#109;&#x79;s&#x65;&#x6c;&#102;&#64;&#x65;xa&#109;&#112;&#108;&#101;&#x2e;c&#x6f;&#109;">&#x6d;&#121;s&#101;&#108;f&#x40;&#x65;&#120;a&#x6d;&#x70;&#108;&#x65;&#x2e;&#99;&#x6f;&#109;</a>
    ```

### excludeTrailingPunctuationFromURLs

Exclude trailing punctuation from autolinked URLs: `.` `!` `?` `(` `)`

This option applies only to links generated by [`simplifiedAutoLink`](#simplifiedautolink).

* type: `boolean`
* default value: `false`
* introduced in: `1.5.1`

=== "input"
    
    ```
       check this link www.google.com.
    ```

=== "output (value is `false`)"

    ```html
    <p>check this link <a href="www.google.com">www.google.com.</a></p>
    ```

=== "output (value is `true`)"

    ```html
    <p>check this link <a href="www.google.com">www.google.com</a>.</p>
    ```

### ghCodeBlocks

Enable support for GFM code block style syntax (fenced codeblocks).

* type: `boolean`
* default value: `true`
* introduced in: `0.3.1`

=== "example"
    
    ```
     ```
     some code here
	 ```
    ```

### ghCompatibleHeaderId

Generate heading IDs compatible with GitHub style: spaces are replaced with dashes, and certain non-alphanumeric chars are removed.

!!! warning ""
    This option can be overridden with the [`noHeaderId`](#noheaderid) option.

* type: `boolean`
* default value: `false`
* introduced in: `1.5.5`

=== "input"
    
    ```
    # This is a heading with @#$%
    ```

=== "output (value is `false`)"

    ```html
    <h1 id="thisisaheading">This is a heading</h1>
    ```

=== "output (value is `true`)"

    ```html
    <h1 id="this-is-a-heading-with-">This is a heading with @#$%</h1>
    ```

### ghMentions

Enables support for GitHub `@mentions` that allows you to link to the GitHub profile page of the mentioned username.

* type: `boolean`
* default value: `false`
* introduced in: `1.6.0` 

=== "input"
    
    ```
    hello there @tivie
    ```

=== "output (value is `false`)"

    ```html
    <p>hello there @tivie</p>
    ```

=== "output (value is `true`)"

    ```html
    <p>hello there <a href="https://www.github.com/tivie">@tivie</a></p>
    ```

### ghMentionsLink

Specify where the link generated by `@mentions` should point to. Works only when [`ghMentions: true`](#ghmentions).

* type: `boolean`
* default value: `https://github.com/{u}`
* introduced in: `1.6.2`

=== "input"
    
    ```
    hello there @tivie
    ```

=== "output (value is `https://github.com/{u}`)"

    ```html
    <p>hello there <a href="https://www.github.com/tivie">@tivie</a></p>
    ```

=== "output (value is `http://mysite.com/{u}/profile`)"

    ```html
    <p>hello there <a href="//mysite.com/tivie/profile">@tivie</a></p>
    ```

### headerLevelStart

Set starting level for the heading tags.

* type: `integer`
* default value: `1`
* introduced in: `1.1.0`

=== "input"
    
    ```
    # This is a heading
    ```

=== "output (value is `1`)"

    ```html
    <h1>This is a heading</h1>
    ```

=== "output (value is `3`)"

    ```html
    <h3>This is a heading</h3>
    ```

### literalMidWordUnderscores

Treat underscores in the middle of words as literal characters.

Underscores allow you to specify the words that should be emphasized. However, in some cases, this may be unwanted behavior. With this option enabled, underscores in the middle of words will no longer be interpreted as `<em>` and `<strong>`, but as literal underscores.

* type: `boolean`
* default value: `false`
* introduced in: `1.2.0`

=== "input"
    
    ```
    some text with__underscores__in the middle
    ```

=== "output (value is `false`)"

    ```html
    <p>some text with<strong>underscores</strong>in the middle</p>
    ```

=== "output (value is `true`)"

    ```html
    <p>some text with__underscores__in the middle</p>
    ```

### metadata

Enable support for document metadata (front-matter). You can define metadata at the top of a document between `««« »»»` or `--- ---` symbols.

* type: `boolean`
* default value: `false`
* introduced in: `1.8.5`

=== "input"
    
    ```js
    let ref = `referenced value`;

    var markdown = `
    ---
    first: Lorem
    second: Ipsum
    ref_variable: ${ref}
    ---
    `

    var conv = new showdown.Converter({metadata: true});
    var html = conv.makeHtml(markdown);
    var metadata = conv.getMetadata();
    ```

=== "output (value is `true`)"

    ```js
    // console.log(metadata)
    {
        first: 'Lorem',
        second: 'Ipsum',
        ref_variable: 'referenced value'
    }
    ```

### noHeaderId

Disable automatic generation of heading IDs.

!!! warning ""
    Setting the option to `true` overrides the following options:
    
    * [`prefixHeaderId`](#prefixheaderid)
    * [`customizedHeaderId`](#customizedheaderid)
    * [`ghCompatibleHeaderId`](#ghcompatibleheaderid)

* type: `boolean`
* default value: `false`
* introduced in: `1.1.0`

=== "input"
    
    ```
    # This is a heading
    ```

=== "output (value is `false`)"

    ```html
    <h1 id="thisisaheading">This is a heading</h1>
    ```

=== "output (value is `true`)"

    ```html
    <h1>This is a heading</h1>
    ```

### omitExtraWLInCodeBlocks

Omit trailing newline in code blocks (which is set by default before the closing tag). This option affects both indented and fenced (gfm style) code blocks.

* type: `boolean`
* default value: `false`
* introduced in: `1.0.0`

=== "input"
    
    ```
        var foo = 'bar';
    ```

=== "output (value is `false`)"

    ```html
    <code><pre>var foo = 'bar';
    </pre></code>
    ```

=== "output (value is `true`)"

    ```html
    <code><pre>var foo = 'bar';</pre></code>
    ```

### openLinksInNewWindow

Open links in new windows.

* type: `boolean`
* default value: `false`
* introduced in: `1.7.0`

=== "input"
    
    ```
    [link](https://google.com)
    ```

=== "output (value is `false`)"

    ```html
    <a href="https://google.com">link</a>
    ```

=== "output (value is `true`)"

    ```html
    <a href="https://google.com" rel="noopener noreferrer" target="_blank">link</a>
    ```

### parseImgDimensions

Set image dimensions from within Markdown syntax.

* type: `boolean`
* default value: `false`
* introduced in: `1.1.0`

=== "example"
    
    ```
    ![foo](foo.jpg =100x80)   set width to 100px and height to 80px
    ![bar](bar.jpg =100x*)    set width to 100px and height to "auto"
    ![baz](baz.jpg =80%x5em)  set width to 80% and height to 5em
    ```

### prefixHeaderId

Add a prefix to the generated heading ID:

* Passing a string will add that string to the heading ID.
* Passing `true` will add a generic `section` prefix.

!!! warning ""
    This option can be overridden with the [`noHeaderId`](#noheaderid) option.

* type: `string / boolean`
* default value: `false`

=== "input"
    
    ```
    # This is a heading
    ```

=== "output (value is `false`)"

    ```html
    <h1 id="thisisaheading">This is a heading</h1>
    ```

=== "output (value is `true`)"

    ```html
    <h1 id="sectionthisisaheading">This is a heading</h1>
    ```

=== "output (value is `showdown`)"

     ```html
     <h1 id="showdownthisisaheading">This is a heading</h1>
     ```

### rawHeaderId

Replace ` ` (space), `'` (single quote), and `"` (double quote) with `-` (dash) in the generated heading IDs, including prefixes.

!!! danger ""
    **Use with caution** as it might result in malformed IDs.

* type:
* default value:
* introduced in: `1.7.3`

### rawPrefixHeaderId

Prevent Showndown from modifying the prefix. Works only when [`prefixHeaderId`](#prefixheaderid) is set to a string value.

!!! danger ""
    **Use with caution** as it might result in malformed IDs. For example, when the prefix contains special characters like `"` `\` `/` or others.

* type: `boolean`
* default value: `false`
* introduced in: `1.7.3`

### requireSpaceBeforeHeadingText

Require a space between a heading `#` and the heading text.

* type: `boolean`
* default value: `false`
* introduced in: `1.5.3`

=== "input"
    
    ```
    #heading
    ```

=== "output (value is `false`)"

    ```html
    <h1 id="heading">heading</h1>
    ```

=== "output (value is `true`)"

    ```html
    <p>#heading</p>
    ```

### simpleLineBreaks

Parse line breaks as `<br/>` in paragraphs (GitHub-style behavior).

* type: `boolean`
* default value: `false`
* introduced in: `1.5.1`

=== "input"
    
    ```
    a line
    wrapped in two
    ```

=== "output (value is `false`)"

    ```html
    <p>a line
    wrapped in two</p>
    ```

=== "output (value is `true`)"

    ```html
    <p>a line<br>
    wrapped in two</p>
    ```

### simplifiedAutoLink

Enable automatic linking for plain text URLs.

* type: `boolean`
* default value: `false`
* introduced in: `1.2.0`

=== "input"
    
    ```
    Lorem ipsum www.google.com
    ```

=== "output (value is `false`)"

    ```html
    <p>Lorem ipsum www.google.com</p>
    ```

=== "output (value is `true`)"

    ```html
    <p>Lorem ipsum <a href="www.google.com">www.google.com</a></p>
    ```

### smartIndentationFix

Resolve indentation problems related to ES6 template strings in the midst of indented code.

* type: `boolean`
* default value: `false`
* introduced in: `1.4.2`

### smoothLivePreview

Resolve an awkward effect when a paragraph is followed by a list. This effect appears on some circumstances, in live preview editors.

* type: `boolean`
* default value: `false`
* introduced in: `1.2.1`

!!! example "awkward effect"
    
    ![](http://i.imgur.com/YQ9iHTL.gif​)

### splitAdjacentBlockquotes

Split adjacent blockquote blocks.

* type: `boolean`
* default value: `false`
* introduced in: `1.8.6`

=== "input"
    
    ```
    > Quote #1
    >> Sub-quote 1

    > Quote #2
    >> Sub-quote 2
    ```

=== "output (value is `false`)"

    ```html
    <blockquote>
      <p>Quote #1</p>
      <blockquote>
        <p>Sub-quote 1</p>
      </blockquote>
      <p>Quote #2</p>
      <blockquote>
        <p>Sub-quote 2</p>
      </blockquote>
    </blockquote>
    ```

=== "output (value is `true`)"

    ```html
    <blockquote>
      <p>Quote #1</p>
      <blockquote>
        <p>Sub-quote 1</p>
      </blockquote>
    </blockquote>
    <blockquote>
      <p>Quote #2</p>
      <blockquote>
        <p>Sub-quote 2</p>
      </blockquote>
    </blockquote>    
    ```

### strikethrough

Enable support for strikethrough (`<del>`).

* type: `boolean`
* default value: `false`
* introduced in: `1.2.0`

=== "input"
    
    ```
    ~~strikethrough~~
    ```

=== "output (value is `true`)"

    ```html
    <del>strikethrough</del>
    ```

### tables

Enable support for tables syntax.

* type: `boolean`
* default value: `false`
* introduced in: `1.2.0`

=== "example"
    
    ```
    | h1    |    h2   |      h3 |
    |:------|:-------:|--------:|
    | 100   | [a][1]  | ![b][2] |
    | *foo* | **bar** | ~~baz~~ |
    ```

### tablesHeaderId

Generate automatic IDs for table headings. Works only when [`tables: true`](#tables).

* type: `boolean`
* default value: `false`
* introduced in: `1.2.0`

### tasklists

Enable support for GitHub style tasklists.

* type: `boolean`
* default value: `false`
* introduced in: `1.2.0`

=== "example"
    
    ```
     - [x] This task is done
     - [ ] This task is still pending
    ```

### underline

Enable support for underline. If enabled, underscores will no longer be parsed as `<em>` and `<strong>`.

* type: `boolean`
* default value: `false`
* status: `Experimental`

=== "example"
    
    ```
    __underlined word__     // double underscores

    ___underlined word___   // triple underscores
    ```
```

## File: `docs/cli.md`
```markdown
Showdown comes bundled with a Command-line interface (CLI) tool that allows you to run Showdown converter from the command line.

## Requirements

* [Node.js](https://nodejs.org/en/)

## Quick start guide

1. Check that Showdown CLI is accessible.

    * If you installed Showdown globally via `npm install showdown -g`, you can access the CLI tool help by typing `showdown -h` in the command line:

        === "input"

            ```sh
            showdown -h
            ```

        === "output"

            ```
            Usage: showdown <command> [options]

            CLI to Showdownjs markdown parser v3.0.0-alpha

            Options:
              -V, --version       output the version number
              -q, --quiet         Quiet mode. Only print errors
              -m, --mute          Mute mode. Does not print anything
              -h, --help          display help for command

            Commands:
              makehtml [options]  Converts markdown into html
              help [command]      display help for command
            ```

    * If you installed Showdown locally via `npm install showdown`, open the folder where Showdown is installed, and type `node ./bin/showdown.js -h` in the command line:

        === "input"

            ```sh
            node ./bin/showdown.js -h
            ```

        === "output"

            ```
            Usage: showdown <command> [options]

            CLI to Showdownjs markdown parser v3.0.0-alpha

            Options:
              -V, --version       output the version number
              -q, --quiet         Quiet mode. Only print errors
              -m, --mute          Mute mode. Does not print anything
              -h, --help          display help for command

            Commands:
              makehtml [options]  Converts markdown into html
              help [command]      display help for command
            ```

1. Use `makehtml` command to convert your document to HTML. For example:

    !!! example "Convert `foo.md` into `bar.html`"
        
        ```sh
        showdown makehtml -i foo.md -o bar.html
        ```

## Commands

### `makehtml`

Convert a Markdown input into HTML.

**Usage**

```sh
showdown makehtml [options]
```

#### Options

###### `-i / --input`

* Short format: `-i`
* Alias: `--input`
* Description: Input source. Usually a `.md` file. If omitted or empty, reads from `stdin`.
* Examples:

    !!! example ""

        ```sh
        // Read from stdin and output to stdout
        showdown makehtml -i

        // Read from the foo.md file and output to stdout
        showdown makehtml --input foo.md
        ```

###### `-o/--output`

* Short format: `-o`
* Alias: `--output`
* Description: Output target. Usually a `.html` file. If omitted or empty, writes to `stdout`.
* Example:

    !!! example ""

        ```sh
        // Read from the foo.md file and output to bar.html
        showdown makehtml -i foo.md -o bar.html
        ```

###### `-a/--append`

* Short format: `-a`
* Alias: `--append`
* Description: Append data to output instead of overwriting.
* Example: 

    !!! example ""

        ```sh
        showdown makehtml -a
        ```

###### `-u/--encoding`

* Short format: `-u`
* Alias: `--encoding`
* Description: Specify the input encoding.
* Example: 
    
    !!! example ""

        ```sh
        showdown makehtml -u UTF8
        ```

###### `-e/--extensions`

* Short format: `-e`
* Alias: `--extension`
* Description: Load the specified extension(s). Should be valid path(s) to Node-compatible extensions.
* Example:

    !!! example ""

        ```sh
        showdown makehtml -e ~/twitter.js -e ~/youtube.js
        ```

###### `-c/--config`

* Short format: `-c`
* Alias: `--config`
* Description: Enable or disable parser options.
* Introduced in: `2.0.1` (Breaking change. See the [`Extra options`](#extra-options) section below)
* Example: 

    !!! example ""

        ```sh
        showdown makehtml -i foo.md -o bar.html -c strikethrough
        showdown makehtml -i foo.md -o bar.html -c strikethrough -c emoji
        ```

## Extra options

Starting from the version `2.0.1`, CLI the format of passing extra options has changed. Please make the necessary changes to your code, if required.

=== "since `v2.0.1`"

    ```sh
    showdown makehtml -i foo.md -o bar.html -c strikethrough -c emoji
    ```

=== "before `v2.0.1`"

    ```sh
    showdown makehtml -i foo.md -o bar.html --strikethrough --emoji
    ```


You can specify any of the [supported options](available-options.md), and they will be passed to the converter.

The above commands are equivalent of doing:

```js
var conv = new showdown.Converter({strikethrough: true, emoji: true});
```

!!! warning ""
    In the CLI tool, all the extra options are **disabled** by default. This is the opposite of what is defined for node and browser, where some options, like `ghCodeBlocks` are enabled (for backward compatibility and historical reasons).
```

## File: `docs/compatibility.md`
```markdown
## Browsers

Showdown has been tested successfully with:

* <img src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/16/000000/external-firefox-a-free-and-open-source-web-browser-developed-by-the-mozilla-foundation-logo-color-tal-revivo.png"/> Firefox 1.5 and 2.0
* <img src="https://img.icons8.com/color/16/000000/chrome--v1.png"/> Chrome 12.0
* <img src="https://img.icons8.com/color/16/000000/internet-explorer.png"/> Internet Explorer 6 and 7
* <img src="https://img.icons8.com/color/16/000000/safari--v1.png"/> Safari 2.0.4
* <img src="https://img.icons8.com/color/16/000000/opera--v1.png"/> Opera 8.54 and 9.10
* <img src="https://img.icons8.com/color/16/000000/netscape.png"/> Netscape 8.1.2
* <img src="https://www.freepngimg.com/save/69063-konqueror-web-kde-manager-file-linux-browser/16x16"/> Konqueror 3.5.4

Generally, Showdown should work in any browser that supports ECMA 262 3<sup>rd</sup> Edition (JavaScript 1.5).

The converter might even work in things that aren't web browsers, like Acrobat. However, no promises.

## Node.js

Showdown is intended to work on any supported Node.js version (see the [Node.js releases schedule](https://nodejs.org/en/about/releases/).

Previous versions may also be supported, but no accomodations are made to ensure this.
```

## File: `docs/configuration.md`
```markdown
You can change Showdown's default behavior via options. 

## Set option

### Globally

Setting an option globally affects all Showdown instances.

```js
showdown.setOption('optionKey', 'value');
```

### Locally

Setting an option locally affects the specified Converter object only. You can set local options via:

=== "Constructor"

    ```js
    var converter = new showdown.Converter({optionKey: 'value'});
    ```

=== "setOption() method"

    ```js
    var converter = new showdown.Converter();
    converter.setOption('optionKey', 'value');
    ```

## Get option

Showdown provides both local and global methods to retrieve previously set options:

=== "getOption()"
    
    ```js
    // Global
    var myOption = showdown.getOption('optionKey');

    //Local
    var myOption = converter.getOption('optionKey');
    ```

=== "getOptions()"

    ```js
    // Global
    var showdownGlobalOptions = showdown.getOptions();

    //Local
    var thisConverterSpecificOptions = converter.getOptions();
    ```

### Get default options

You can get Showdown's default options with:

```js
var defaultOptions = showdown.getDefaultOptions();
```
```

## File: `docs/create-extension.md`
```markdown
A Showdown extension is a function that returns an array of language or outputs extensions (henceforth called "sub-extensions"). 

```js
var myext = function () {
  var myext1 = {
    type: 'lang',
    regex: /markdown/g,
    replace: 'showdown'
  };
  var myext2 = {
    /* extension code */
  };
  return [myext1, myext2];
}
```

Each sub-extension (`myext1` and `myext2` in the example above) should be an object that defines the behavior of the corresponding sub-extension.

## Sub-extension object properties

A sub-extension object should have a [`type` property](#type) that defines the type of the sub-extension, and either [`regex` and `replace` properties](#regex-and-replace) or a [`filter` property](#filter).

### Type

**Type** is a **required** property that defines the nature of the corresponding sub-extensions. It takes one of the two values:

* **`lang`**: language extension to add new Markdown syntax to Showdown.

    `lang` extensions have the **highest priority** in the subparser order, so they are called after [escaping and normalizing](#escape-and-normalization) the input text and before calling any other subparser (or extension).

    !!! example "When to use `lang` type"

        For example, if you want the `^^youtube http://www.youtube.com/watch?v=oHg5SJYRHA0` syntax to automatically be rendered as an embedded YouTube video.

* **`output`**: output extension (or modifier) to alter the HTML output generated by Showdown.
 
    `output` extensions have the **lowest priority** in the subparser order, so they are called right before the cleanup step and after calling all other subparsers.

    !!! example "When to use `output` type"

        For example, if you want the `<div class="header">` to become `<header>`.

### Regex and replace

`regex`/`replace` properties are similar to the Javascript's `string.replace` function and work the same way:

* `regex`: a `string` or a `RegExp` object.
    
    If `regex` is a `string`, it will automatically be assigned a `g` (global) modifier, that is, all matches of that string will be replaced.

* `replace` a `string` or a `function`.

    If `replace` is a `string`, you can use the `$1` syntax for group substitution, exactly as if it were making use of `string.replace`.

!!! example "Regex and replace example"

    In this example, all the occurrences of `markdown` will be replaced with `showndown`.

    ```js
    var myext = {
      type: 'lang',
      regex: /markdown/g,
      replace: 'showdown'
    };
    ```

### Filter

Alternately, if you'd like to have more control over the modification process, you can use `filter` property.

This property should be used as a function that acts as a callback. The callback should receive the following parameters:

1. `text`: the source text within the Showdown's engine.
1. `converter`: the full instance of the current Showdown's converter object.
1. `options`: the options used to initialize the converter

!!! warning ""
    The filter function **should return the transformed text**. If it doesn't, it will fail **silently** and return an empty output.

!!! example "Filter example"

    ```js
    var myext = {
      type: 'lang',
      filter: function (text, converter, options) {
        // ... do stuff to text ...
        return text;
      }
    };
    ```

!!! warning "Use `filter` with care"

    Although Filter extensions are more powerful, they have a few pitfalls that you should keep in mind before using them, especially regarding the `converter` parameter.

    Since the `converter` parameter passed to the filter function is the fully initialized instance, any change made to it will be propagated outside the scope of the filter function and will remain there until a new converter instance is created. So, **it is not recommended to make ANY change to the converter object**.

    Another aspect is that if you call the `converter` recursively, it will call your extension itself at some point. It may lead to infinite recursion in some circumstances, and it's up to you to prevent this. A simple solution is to place a kind of safeguard to disable your extension if it's called more than x times:

    ```js
    var x = 0;
    var myext = {
      type: 'lang',
      filter: function (text, converter) {
        if (x < 3) {
          ++x;
          someSubText = converter.makeHtml(someSubText);
        }
      } 
    };
    ```

## Register an extension


To let Showdown know what extensions are available, you need to register them in the Showdown global object.

To register an extension, call the `showdown.extension` function with two parameters: the first one is the extension name; the second one is the actual extension.

```js
showdown.extension('myext', myext);
```

## Test an extension

The Showdown test runner is configured to automatically test cases for extensions.

To add test cases for an extension:

1. Create a new folder under `./test/extensions` that matches with the name of the `.js` file in `./src/extensions`.
1. Place any test cases into the filter using the `md/html` format. These cases will automatically be executed when running tests.

## Additional information

### Escape and normalization

Showdown performs the following escape/normalization:

* Replaces `¨` (trema) with `¨T`
* Replaces `$` (dollar sign) with `¨D`
* Normalizes line endings (`\r`, `\r\n` are converted into `\n`)
* Uses `\r` as a char placeholder

!!! note ""
    This only applies to **language extensions** since these chars are unescaped before output extensions are run.

!!! warning ""
    
    Keep in mind that these modifications happen **before language extensions** are run, so if your extension relies on any of those chars, you have to make the appropriate adjustments.


### Implementation concerns

One of the concerns is maintaining both client-side and server-side compatibility. You can do this with a few lines of boilerplate code.:

```js
(function (extension) {
  if (typeof showdown !== 'undefined') {
    // global (browser or node.js global)
    extension(showdown);
  } else if (typeof define === 'function' && define.amd) {
    // AMD
    define(['showdown'], extension);
  } else if (typeof exports === 'object') {
    // Node, CommonJS-like
    module.exports = extension(require('showdown'));
  } else {
    // showdown was not found so an error is thrown
    throw Error('Could not find showdown library');
  }
}(function (showdown) {
  // loading extension into showdown
  showdown.extension('myext', function () {
    var myext = { /* ... actual extension code ... */ };
    return [myext];
  });
}));
```

In the code above, the extension definition is wrapped in a self-executing function to prevent pollution of the global scope. It has another benefit of creating several scope layers that can be useful for interaction between sub-extensions global-wise or local-wise.

It is also loaded conditionally to make it compatible with different loading mechanisms (such as browser, CommonJS, or AMD).
```

## File: `docs/credits.md`
```markdown
=== "v.2"

    * [Estevão Santos](https://github.com/tivie)
    * [SyntaxRules](https://github.com/SyntaxRules)

=== "v.1"

    * [Estevão Santos](https://github.com/tivie)
    * [Pascal Deschênes](https://github.com/pdeschen)

=== "v.0"

    * [Corey Innis](http://github.com/coreyti) - Original GitHub project maintainer
    * [Remy Sharp](https://github.com/remy/) - CommonJS-compatibility and more
    * [Konstantin Käfer](https://github.com/kkaefer/) - CommonJS packaging
    * [Roger Braun](https://github.com/rogerbraun) - GitHub-style code blocks
    * [Dominic Tarr](https://github.com/dominictarr) - Documentation
    * [Cat Chen](https://github.com/CatChen) - Export fix
    * [Titus Stone](https://github.com/tstone) - Mocha tests, extension mechanism, bug fixes
    * [Rob Sutherland](https://github.com/roberocity) - The idea that lead to extensions
    * [Pavel Lang](https://github.com/langpavel) - Code cleanup
    * [Ben Combee](https://github.com/unwiredben) - Regex optimization
    * [Adam Backstrom](https://github.com/abackstrom) - WebKit bug fixes
    * [Pascal Deschênes](https://github.com/pdeschen) - Grunt support, extension fixes + additions, packaging improvements, documentation
    * [Estevão Santos](https://github.com/tivie) - Bug fixes and late maintainer
    * [Hannah Wolfe](https://github.com/ErisDS) - Bug fixes
    * [Alexandre Courtiol](https://github.com/acourtiol) - Bug fixes and build optimization
    * [Karthik Balakrishnan](https://github.com/torcellite) - Support for table alignment
    * [rheber](https://github.com/rheber) - CLI
    

=== "Original Project"

    * [John Gruber](http://daringfireball.net/projects/markdown/) - Author of Markdown
    * [John Fraser](http://attacklab.net/) - Author of Showdown
```

## File: `docs/donations.md`
```markdown
ShowdownJS is a **free** library and it will remain **free forever**.

However, maintaining and improving the library costs time and money.

If you like our work and find it useful, please donate through [PayPal](https://www.paypal.me/tiviesantos).

:heart: :pray: Your contributions are greatly appreciated and will help us with the development of this awesome library.
```

## File: `docs/event_system.md`
```markdown
# Event System

## Introduction


## The Event Object


## Events

Events are raised when a subparser is run (or about to be run).
Within a subparser, the events always follow a certain order (sequence). For instance, **.before** events always run before **.captureStart**.
Each subparser raises several events sequentially:

 1. **.start**: **always runs** except it subparser is disabled

    Raised when the **subparser has started**, but no capturing or any modification to the text was done.
    
    **Always runs** (except if the subparser is deactivated through options).
    
    ***Properties***:
         
    | property | type      | access     | description                                                        |
    |----------|-----------|------------|--------------------------------------------------------------------|
    | input    | string    | read       | The full text that was passed to the subparser                     |
    | output   | string    | write      | The full text with modification that will be passed along the chain|
    | regexp   | null      |            |                                                                    |
    | matches  | null      |            |                                                                    |
    
    Usually you would want to use this event if you wish to change the input to the subparser
     
 2. **.captureStart**: *might not be run*;
 
     Raised when a regex match is found and a capture was successful. Some normalization and modification 
     of the regex captured groups might be performed.
     
     Might not be run if no regex match is found.
     
     ***Properties***:
     
     | property | type      | access     | description                                                        |
     |----------|-----------|------------|--------------------------------------------------------------------|
     | input    | string    | read       | The captured text                                                  |
     | output   | string    | write      | The text that will be passed to the subparser/other listeners      |
     | regexp   | RegExp    | readonly   | Regular Expression used to capture groups                          |
     | matches  | object    | read/write | Matches groups. Changes to this object are reflected in the output |
     
     Usually you would want to use this event if you wish to modify a certain subparser behavior.
     Exs: remove all title attributes from links; change indentation of code blocks; etc...
 
 3. **.captureEnd**: *might not be run*;
 
    Raised after the modifications to the captured text are done but before the replacement is introduced in the document.
    
    Might not be run if no regex match is found.
         
    ***Properties***:
    
    | property   | type      | access     | description                                                                    |
    |------------|-----------|------------|--------------------------------------------------------------------------------|
    | input      | string    | read       | The captured text                                                              |
    | output     | string    | write      | The text that will be passed to the subparser/other listeners                  |
    | regexp     | RegExp    | readonly   | Regular Expression used to capture groups                                      |
    | matches    | object    | read/write | Keypairs of matches groups. Changes to this object are reflected in the output |
    | attributes | object    | read/write | Attributes to add to the HTML output                                           |
 
 4. **.beforeHash**: *might not be run*;
 
    Raised before the output is hashed.
    
    Always run (except if the subparser was deactivated through options), even if no hashing is performed. 
    
    ***Properties***:
        
    | property | type       | access     | description                                                        |
    |----------|------------|------------|--------------------------------------------------------------------|
    | input    | string     | read       | The captured text                                                  |
    | output   | string     | write      | The text that will be passed to the subparser/other listeners      |
    | regexp   | null       |            |                                                                    |
    | matches  | null       |            |                                                                    |
 
    Usually you would want to use this event if you wish change the subparser output before it is hashed
 
 5. **.end**: *always runs*;
 
    Raised when the subparser has finished its work and is about to exit.
     
    Always runs (except if the subparser is deactivated through options).
    
    ***Properties***:
    
    | property | type      | access     | description                                                        |
    |----------|-----------|------------|--------------------------------------------------------------------|
    | input    | string    | read       | The partial/full text with the subparser modifications             |
    | output   | string    | write      | The text that will be passed to other subparsers                   |
    | regexp   | null      |            |                                                                    |
    | matches  | null      |            |                                                                    |
     
    Usually you would want to use this event if you wish change the subparser hashed output


### Special Events

There are some special events that are useful for *"positioning"* a listener extension in the main chain of events.
Usually these extensions introduce new syntax that, due to precedence 
These events are always guaranteed to be called, regardless of options or circumstances. 

 1. **.before_{subparserName}**: *always runs*
    
    Raised just before the **{subparserName} is about to be entered**.
    
    ***Properties***:
         
    | property | type      | access     | description                                                        |
    |----------|-----------|------------|--------------------------------------------------------------------|
    | input    | string    | read       | The full text that was passed to the subparser                     |
    | output   | string    | write      | The full text with modification that will be passed along the chain|
    | regexp   | null      |            |                                                                    |
    | matches  | null      |            |                                                                    |
    
 2. **.after**.{subparserName}: *always runs*;
 
    Raised when the **{subparserName} has exited** and before the next one is called.
    
    ***Properties***:
    
    | property | type      | access     | description                                                        |
    |----------|-----------|------------|--------------------------------------------------------------------|
    | input    | string    | read       | The partial/full text with the subparser modifications             |
    | output   | string    | write      | The text that will be passed to other subparsers                   |
    | regexp   | null      |            |                                                                    |
    | matches  | null      |            |                                                                    |

 
### Notes

 - There are 2 main differences between **before.{subparserName}** and **{subparserName}.start**.
   
     1. **before.{subparserName}** is always guaranteed to be called, even if the subparser is disabled, 
        while **{subparserName}.start** doesn't.
        
        ex: `makehtml.before.strikethrough` is always called even if the option `strikethrough` is false 
        
     2. **before.{subparserName}** is only raised once in a span context while **{subparserName}.start** is raised
        everytime **{subparserName}** is called.

    As a rule of thumb, 

## Events List
```

## File: `docs/extensions-list.md`
```markdown
## Official

* [twitter-extension][1] - Adds support of Twitter usernames and hastags
* [prettify-extension][2] - Adds [Google Prettify][3] hints to HTML output

## Community

* [showdown-icon][4] - Adds support of Glyphicon and font-awesome into Markdown
* [showdown-xss-filter][5] - Filters XSS, using leizongmin/js-xss
* [showdown-toc][6] - Adds Table of Contents
* [showdown-footnotes][7] - Adds simple footnotes
* [katex-latex][8] - Displays math using KaTeX and LaTeX or AsciiMath

!!! note ""
    If you have a Showdown extension you would like to add here, you can [raise an issue](https://github.com/showdownjs/showdown/issues).

[1]: https://github.com/showdownjs/twitter-extension
[2]: https://github.com/showdownjs/prettify-extension
[3]: https://github.com/googlearchive/code-prettify
[4]: https://github.com/dbtek/showdown-icon
[5]: https://github.com/VisionistInc/showdown-xss-filter
[6]: https://github.com/ravisorg/showdown-toc
[7]: https://github.com/Kriegslustig/showdown-footnotes
[8]: https://obedm503.github.io/showdown-katex
```

## File: `docs/extensions.md`
```markdown
Showdown allows you to load additional functionality via extensions. You can find a list of known Showdown extensions [here][ext-wiki].

You can also check the [boilerplate repo][boilerplate-repo], to create your own extension(s).

## Usage

=== "Server-side"

    ```js
    // Using a bundled extension
    var showdown = require('showdown');
    var converter = new showdown.Converter({ extensions: ['twitter'] });

    // Using a custom extension
    var mine = require('./custom-extensions/mine');
    var converter = new showdown.Converter({ extensions: ['twitter', mine] });
    ```

=== "Client-side"

    ```js
    <script src="src/showdown.js"></script>
    <script src="src/extensions/twitter.js"></script>
    <script>var converter = new showdown.Converter({ extensions: ['twitter'] });</script>
    ```

=== "CLI"

    In the CLI tool, use the [`-e` flag](/cli/#-e-extensions) to load an extension.

    ```sh
    showdown -e twitter -i foo.md -o bar.html
    ```

[ext-wiki]: https://github.com/showdownjs/showdown/wiki/extensions
[boilerplate-repo]: https://github.com/showdownjs/extension-boilerplate
```

## File: `docs/flavors.md`
```markdown
## Overview

You can use _flavors_ (or presets) to set the preferred options automatically. In this way, Showdown behaves like popular Markdown flavors.

Currently, the following flavors are available:

 * `original`: Original Markdown flavor as in [John Gruber's spec](https://daringfireball.net/projects/markdown/)
 * `vanilla`:  Showdown base flavor (v1.3.1 onwards)
 * `github`: [GitHub Flavored Markdown, or GFM](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## Set flavor

=== "Globally"

    ```js
    showdown.setFlavor('github');
    ```

=== "Locally"

    ```js
    converter.setFlavor('github');
    ```
```

## File: `docs/index.md`
```markdown
# Showdown documentation

![Showdown][sd-logo]

![Build Status: Linux](https://github.com/showdownjs/showdown/actions/workflows/node.linux.yml/badge.svg)
![Build Status: Windows](https://github.com/showdownjs/showdown/actions/workflows/node.win.yml/badge.svg)
[![npm version](https://badge.fury.io/js/showdown.svg)](http://badge.fury.io/js/showdown)
[![Bower version](https://badge.fury.io/bo/showdown.svg)](http://badge.fury.io/bo/showdown)
[![Join the chat at https://gitter.im/showdownjs/showdown](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/showdownjs/showdown?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/tiviesantos)

Showdown is a JavaScript Markdown to HTML converter, based on the original works by John Gruber.
Showdown can be used on the client-side (in the browser) or server-side (with Node.js).

----

## Live demo

<http://demo.showdownjs.com/>

## Who uses Showdown (or a fork)

* [Antmarky](https://github.com/bandantonio/antmarky)
* [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
* [Meteor](https://www.meteor.com/)
* [StackExchange](http://stackexchange.com/) - forked as [PageDown](https://code.google.com/p/pagedown/)
* [docular](https://github.com/Vertafore/docular)
* [md-page](https://github.com/oscarmorrison/md-page)
* [QCObjects](https://qcobjects.dev)
* [and some others](https://www.npmjs.com/browse/depended/showdown)

## Installation

To install Showdown, follow the instructions from the [Quickstart guide](quickstart.md).


## License

ShowdownJS v 2.0 is release under the MIT version.

Previous versions are release under BSD.

[sd-logo]: https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png
[wiki]: https://github.com/showdownjs/showdown/wiki
[cli-wiki]: https://github.com/showdownjs/showdown/wiki/CLI-tool
[definitely-typed]: https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/showdown
[xss-wiki]: https://github.com/showdownjs/showdown/wiki/Markdown's-XSS-Vulnerability-(and-how-to-mitigate-it)
[ext-wiki]: https://github.com/showdownjs/showdown/wiki/extensions
[coding-rules]: https://github.com/showdownjs/code-style/blob/master/README.md
[ng-commit-guide]: https://github.com/showdownjs/code-style/blob/master/README.md#commit-message-convention
[boilerplate-repo]: https://github.com/showdownjs/extension-boilerplate
```

## File: `docs/integrations.md`
```markdown
## AngularJS

ShowdownJS project provides seamless integration with AngularJS via a plugin.

Check [`ng-showdown`](https://github.com/showdownjs/ngShowdown) repository for more information.

## TypeScript

If you're using TypeScript, you may want to use the types from the [DefinitelyTyped][definitely-typed] repository.

## SystemJS/JSPM

To integrate ShowdownJS with SystemJS, you can use a third-party [system-md plugin](https://github.com/guybedford/system-md).

## Vue.js

To use ShowdownJS as a Vue component, you can check [vue-showdown](https://vue-showdown.js.org/).


[definitely-typed]: https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/showdown
```

## File: `docs/markdown-syntax.md`
```markdown
## Introduction

Showdown was created by John Fraser as a direct port of the original parser written by Markdown's creator, John Gruber.

Although Showdown has evolved since its inception, in "vanilla mode", it tries to follow the [original markdown spec][md-spec] (henceforth referred as vanilla) as much as possible. There are, however, a few important differences, mainly due to inconsistencies in the original spec, which Showdown addressed following the author's advice as stated in the [markdown's "official" newsletter][md-newsletter].

Showdown also supports opt-in features, that is, an "extra" syntax that is not defined in the original spec. Users can enable these features via options (All the new syntax elements are disabled by default).

This document provides a quick reference of the supported syntax and the differences in output from the original markdown.pl implementation.

## Paragraphs

Paragraphs in Showdown are **one or more lines of consecutive text** followed by one or more blank lines.

```md
On July 2, an alien mothership entered Earth's orbit and deployed several dozen 
saucer-shaped "destroyer" spacecraft, each 15 miles (24 km) wide.
    
On July 3, the Black Knights, a squadron of Marine Corps F/A-18 Hornets, 
participated in an assault on a destroyer near the city of Los Angeles.
```

The implication of the "one or more consecutive lines of text" is that Showdown supports 
"hard-wrapped" text paragraphs. It means the following examples produce the same output:

```md
A very long line of text
```

```md
A very
long line
of text
```

If you **do** want to add soft line breaks (which translate to `<br>` in HTML) to a paragraph, 
you can do so by adding 3 space characters to the end of the line.

You can also force every line break in paragraphs to translate to `<br>` (as Github does) by
enabling the option [**`simpleLineBreaks`**][simpleLineBreaks].

[simpleLineBreaks]: available-options.md#simplelinebreaks

## Headings

### Atx Style

You can create a heading by adding one or more `#` symbols before your heading text. The number of `#` determines the level of the heading. This is similar to [**atx style**][atx].

```md
# The 1st level heading (an <h1> tag)
## The 2nd level heading (an <h2> tag)
…
###### The 6th level heading (an <h6> tag)
```

The space between `#` and the heading text is not required but you can make it mandatory by enabling the option [**`requireSpaceBeforeHeadingText`**][requireSpaceBeforeHeadingText].

[requireSpaceBeforeHeadingText]: available-options.md#requirespacebeforeheadingtext

You can wrap the headings in `#`. Both leading and trailing `#` will be removed.

```md
## My Heading ##
```

If, for some reason, you need to keep a leading or trailing `#`, you can either add a space or escape it:

```md
# # My header # #

#\# My Header \# #
```

### Setext style

You can also use [**setext style**][setext] headings, although only two levels are available.

```md
This is an H1
=============
    
This is an H2
-------------
```

!!! warning ""
    There is an awkward effect when a paragraph is followed by a list. This effect appears on some circumstances, in live preview editors.

    ![awkward effect][]

    You can prevent this by enabling the option [**`smoothPreview`**][smoothlivepreview].

[smoothlivepreview]: available-options.md#smoothlivepreview

### Header IDs

Showdown automatically generates bookmark anchors in titles by adding an id property to a heading.

```md
# My cool header with ID
```

```html
<h1 id="mycoolheaderwithid">My cool header with ID</h1>
```

This behavior can be modified with options:

 - [**`noHeaderId`**][noHeaderId] disables automatic id generation; 
 - [**`ghCompatibleHeaderId`**][ghCompatibleHeaderId] generates header ids compatible with github style (spaces are replaced with dashes and a bunch of non alphanumeric chars are removed)
 - [**`prefixHeaderId`**][prefixHeaderId] adds a prefix to the generated header ids (either automatic or custom).
 - [**`headerLevelStart`**][headerLevelStart] sets the header starting level. For instance, setting this to 3 means that `# header` will be converted to `<h3>`.

Read the [README.md][readme] for more info

[noHeaderId]: available-options.md#noheaderid
[ghCompatibleHeaderId]: available-options.md#ghcompatibleheaderid
[prefixHeaderId]: available-options.md#prefixheaderid
[headerLevelStart]: available-options.md#headerlevelstart

## Blockquotes

You can indicate blockquotes with a `>`.

```md
In the words of Abraham Lincoln:
    
> Pardon my french
```

Blockquotes can have multiple paragraphs and can have other block elements inside.

```md
> A paragraph of text
>
> Another paragraph
>
> - A list
> - with items
```

## Bold and Italic

You can make text bold or italic.

```md
*This text will be italic*
**This text will be bold**
```

Both bold and italic can use either a `*` or an `_` around the text for styling. This allows you to combine both bold and italic if needed.

```md
**Everyone _must_ attend the meeting at 5 o'clock today.**
```

## Strikethrough

With the option [**`strikethrough`**][] enabled, Showdown supports strikethrough elements.
The syntax is the same as GFM, that is, by adding two tilde (`~~`) characters around
a word or groups of words.

```md
a ~~strikethrough~~ element
```

a <s>strikethrough</s> element

[strikethrough]: available-options.md#strikethrough

## Emojis

Since version 1.8.0, Showdown supports Github's emojis. A complete list of available emojis can be found [here][emoji list].

```md
this is a :smile: smile emoji
```

this is a :smile: smile emoji

## Code formatting

### Inline formats

Use single backticks (`) to format text in a special monospace format. Everything within the backticks appear as-is, with no other special formatting.

```md
Here's an idea: why don't we take `SuperiorProject` and turn it into `**Reasonable**Project`.
```

```html
<p>Here's an idea: why don't we take <code>SuperiorProject</code> and turn it into <code>**Reasonable**Project</code>.</p>
```

### Multiple lines

To create blocks of code you should indent it by four spaces.

```md
    this is a piece
    of
    code
```

If the option [**`ghCodeBlocks`**][ghCodeBlocks] is activated (which is by default), you can use triple backticks <code>```</code> to format text as its own distinct block.

    Check out this neat program I wrote:

    ```
    x = 0
    x = 2 + 2
    what is x
    ```

[ghCodeBlocks]: available-options.md#ghcodeblocks

## Lists

Showdown supports unordered (bulleted) and ordered (numbered) lists.

### Unordered lists

You can make an unordered list by preceding list items with either `*`, `-`, or `+`. Markers are interchangeable too.

```md
* Item
+ Item
- Item
```

### Ordered lists

You can make an ordered list by preceding list items with a number.

```md
1. Item 1
2. Item 2
3. Item 3
```

!!! earning ""
    The actual numbers you use to mark the list have no effect on the HTML output that Showdown produces. So you can use the same number in all items if you wish to. For example:

    ```md
    1. Item 1
    1. Item 2
    1. Item 3

    2. Item 1
    2. Item 2
    2. Item 3
    ```

### TaskLists (GFM Style)

Showdown supports GFM-styled takslists if the [**`tasklists`**][tasklists] option is enabled.

```md
 - [x] checked list item
 - [ ] unchecked list item
``` 

 - [x] checked list item
 - [ ] unchecked list item


[tasklists]: available-options.md#tasklists

### List syntax

List markers typically start at the left margin, but may be indented by up to three spaces. 

```md
* valid list item
   * this is valid too
   * this is too  
```

List markers must be followed by one or more spaces or a tab.

To make lists look nicer, you can wrap items with hanging indents:

```md
*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.
```

But if you want to be lazy, you don't have to :grin:

If one list item is separated by a blank line, Showdown will wrap all the list items in `<p>` tags in the HTML output.
So this input:

```md
* Bird

* Magic
* Johnson
```

results in:

```html
<ul>
<li><p>Bird</p></li>
<li><p>Magic</p></li>
<li><p>Johnson</p></li>
</ul>
```

This differs from other Markdown implementations such as GFM (GitHub) or CommonMark.  

### Nested blocks

List items may consist of multiple paragraphs. Each subsequent paragraph in a list item must be indented by either 4 spaces or one tab:

```md
1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.
```

This is valid for other block elements such as blockquotes:

```md
*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.
```

or even other lists.

### Nested lists

You can create nested lists by indenting list items by **four** spaces.

```md
1.  Item 1
    1. A corollary to the above item.
    2. Yet another point to consider.
2.  Item 2
    * A corollary that does not need to be ordered.
    * This is indented four spaces
    * You might want to consider making a new list.
3.  Item 3
```

This behavior is consistent with the original spec but differs from other implementations such as GFM or CommonMark. Prior to version 1.5, you just needed to indent two spaces for it to be considered a sublist.

You can disable the **four spaces requirement** with option [**`disableForced4SpacesIndentedSublists`**][disableForced4SpacesIndentedSublists]

To nest a third (or more) sublist level, you need to indent 4 extra spaces (or 1 extra tab) for each level:

```md
1.  level 1
    1.  Level 2
        *   Level 3
    2.  level 2
        1.  Level 3
1.  Level 1
```
[disableForced4SpacesIndentedSublists]: available-options.md#disableforced4spacesindentedsublists

### Nested code blocks

You can nest fenced codeblocks the same way you nest other block elements, by indenting by four spaces or a tab:

```md
1.  Some code:

    ```js
    var foo = 'bar';
    console.log(foo);
    ```
```

To put an *indented style* code block within a list item, the code block needs to be indented twice — 8 spaces or two tabs:

```md
1.  Some code:

        var foo = 'bar';
        console.log(foo);
```

## Links

### Simple

If you wrap a valid URL or email in `<>` it will be turned into a link whose text is the link itself.

```md
link to <http://www.google.com/>

this is my email <somedude@mail.com>
```

In the case of email addresses, Showdown also performs a bit of randomized decimal and hex entity-encoding to help obscure your address from address-harvesting spambots.
You can disable this obfuscation by setting [**`encodeEmails`**][encodeEmails] option to `false`.

With the option [**`simplifiedAutoLink`**][simplifiedAutoLink] enabled, Showdown will automagically turn every valid URL it finds in the text body into links without the need to wrap them in `<>`.

```md
link to http://www.google.com/

this is my email somedude@mail.com
```

[encodeEmails]: available-options.md#encodeemails
[simplifiedAutoLink]: available-options.md#simplifiedautolink

### Inline

You can create an inline link by wrapping link text in brackets `[ ]`, and then wrapping the link in parentheses `( )`.

For example, a hyperlink to `github.com/showdownjs/showdown`, with a link text that says, `Get Showdown!` will look as follows:

```
[Get Showdown!](https://github.com/showdownjs/showdown)
```

### Reference Style

You can also use the reference style, like this:

```md
this is a [link to google][1]

[1]: www.google.com
```

Showdown also supports implicit link references:

```md
this is a link to [google][]

[google]: www.google.com
```

## Images

In Markdown, the syntax for images is similar to that of links, supporting both inline and reference styles as well. The only difference in syntax for images is the leading exclamation mark before brackets: `![]`.

### Inline

Inline image syntax looks like this:

```md
![Alt text](url/to/image)

![Alt text](url/to/image "Optional title")
```

That is:

* An exclamation mark: `!`
* followed by a set of square brackets `[ ]` containing the alt attribute text for the image
* followed by a set of parentheses `( )` containing the URL or path to the image and an optional title attribute enclosed in double or single quotes.


### Reference Style

Reference-style image syntax looks like this:

```md
![Alt text][id]
```

Where `id` is the name of a defined image reference. Image references are defined using syntax identical to link references:

```md
[id]: url/to/image  "Optional title attribute"
```

Implicit references are also supported:

```md
![showdown logo][]

[showdown logo]: http://showdownjs.github.io/demo/img/editor.logo.white.png
```

### Image dimensions

When the option [**`parseImgDimensions`**][parseImgDimensions] is activated, you can define the image dimensions, like this:

```md
![Alt text](url/to/image =250x250 "Optional title")
```

or in reference style:

```md
![Alt text][id]

[id]: url/to/image =250x250
```

[parseImgDimensions]: available-options.md#parseimgdimensions

### Base64 encoded images

Showdown supports Base64 encoded images, both reference and inline style.

**Since version 1.7.4**, Showdown supports wrapping of base64 strings, which are usually extremely long lines of text.
You can add newlines arbitrarily, as long as they are added after the `,` character.

inline style

```md
![Alt text](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7l
jmRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAY
SURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=)
```

reference style

```md
![Alt text][id]

[id]:
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7l
jmRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7D
AcdvqGQAAAAYSURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=
```

!!! warning ""
    With reference-style base64 image sources, regardless of "wrapping", a double newline is **required** after the base64 string to separate them from a paragraph or other text block (but references can be adjacent):

    !!! example "Wrapped reference style"

        ```md
        ![Alt text][id]
        ![Alt text][id2]

        [id]:
        data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7l
        jmRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7D
        AcdvqGQAAAAYSURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=
        [id2]:
        data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7l
        jmRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7D
        AcdvqGQAAAAYSURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=


        this text needs to be separated from the references by 2 newlines
        ```

## Tables

Tables aren't part of the core Markdown spec, but they are part of GFM. You can enable them in Showdown via the option [**`tables`**][tables].

* Colons can be used to align columns.
* The outer pipes (`|`) are optional, matching GFM spec. 
* You don't need to make the raw Markdown line up prettily.
* You can use other Markdown syntax inside them.

```md
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| **col 3 is**  | right-aligned | $1600 |
| col 2 is      | *centered*    |   $12 |
| zebra stripes | ~~are neat~~  |    $1 |
```

[tables]: available-options.md#tables

## Mentions

Showdown supports GitHub mentions by enabling the option [**`ghMentions`**][mentions]. This will turn every `@username` into a link to their github profile.

```md
hey @tivie, check this out
```

Since version 1.6.2, you can customize the generated link in mentions with the option [**`ghMentionsLink`**][ghMentionsLink].

For example, setting this option to `http://mysite.com/{u}/profile`:

```html
<p>hey <a href="http://mysite.com/tivie/profile">@tivie</a>, check this out</p>
```

[mentions]: available-options.md#ghmentions
[ghMentionsLink]: available-options.md#ghmentionslink

## Handle HTML in markdown documents

Showdown, in most cases, leaves HTML tags untouched in the output document:

```md
some markdown **here**
<div>this is *not* **parsed**</div>
```

```html
<p>some markdown <strong>here</strong></p>
<div>this is *not* **parsed**</div>
```

However, the content of `<code>` and `<pre><code>` tags is always escaped.

```md
some markdown **here** with <code>foo & bar <baz></baz></code>
```

```html
<p>some markdown <strong>here</strong> with <code>foo &amp; bar &lt;baz&gt;&lt;/baz&gt;</code></p>
``` 

If you want to enable markdown parsing inside a specific HTML tag, you can use the html attribute **`markdown`**, **`markdown="1"`**, or **`data-markdown="1"`**.

```md
some markdown **here**
<div markdown="1">this is *not* **parsed**</div>
```

```html
<p>some markdown <strong>here</strong></p>
<div markdown="1"><p>this is <em>not</em> <strong>parsed</strong></p></div>
```

## Escape entities

### Escape markdown entities

Showdown allows you to use backslash (`\`) to escape characters that have special meaning in markdown's syntax and generate literal characters instead. For example, if you want to surround a word with literal underscores (instead of an HTML `<em>` tag), you can use backslashes before the underscores, like this:

```md
\_literal underscores\_
```

Showdown provides backslash escapes for the following characters:

```
\   backslash
`   backtick
*   asterisk
_   underscore
{}  curly braces
[]  square brackets
()  parentheses
#   hash mark
+   plus sign
-   minus sign (hyphen)
.   dot
!   exclamation mark
```

### Escape HTML tags

Since [version 1.7.2](https://github.com/showdownjs/showdown/tree/1.7.2), backslash escaping of HTML tags is supported when [**`backslashEscapesHTMLTags`**][backslashEscapesHTMLTags] option is enabled.

```md
\<div>a literal div\</div>
``` 

[backslashEscapesHTMLTags]: available-options.md#backslashescapeshtmltags

## Known differences and gotchas

In most cases, Showdown's output is identical to that of Perl Markdown v1.0.2b7. What follows is a list of all known deviations. Please file an issue if you find more.

* **Since version 1.4.0, Showdown supports the markdown="1" attribute**, but for older versions, this attribute is ignored. This means:

    ```md
    <div markdown="1">
          Markdown does *not* work in here.
    </div>
    ```

* You can only nest square brackets in link titles to a depth of two levels:

        [[fine]](http://www.github.com/)
        [[[broken]]](http://www.github.com/)

    If you need more, you can escape them with backslashes.

* A list is **single paragraph** if it has only **1 line break separating items** and it becomes **multi-paragraph if ANY of its items is separated by 2 line breaks**:

    ```md
    - foo

    - bar
    - baz
    ```

    becomes

    ```html
    <ul>
      <li><p>foo</p></li>
      <li><p>bar</p></li>
      <li><p>baz</p></li>
    </ul>
    ```

This new ruleset is based on the comments of Markdown's author John Gruber in the [Markdown discussion list][md-newsletter].

[md-spec]: http://daringfireball.net/projects/markdown/
[md-newsletter]: https://pairlist6.pair.net/mailman/listinfo/markdown-discuss
[atx]: http://www.aaronsw.com/2002/atx/intro
[setext]: https://en.wikipedia.org/wiki/Setext
[readme]: https://github.com/showdownjs/showdown/blob/master/README.md
[awkward effect]: http://i.imgur.com/YQ9iHTL.gif
[emoji list]: https://github.com/showdownjs/showdown/wiki/emojis
```

## File: `docs/quickstart.md`
```markdown
To quickstart with Showdown, install it as a package (for server-side) or include it to your browser (client-side) via CDN:

## Installation

### Server-side

=== "npm"

    ```
    npm install showdown
    ```

=== "bower"

    ```
    bower install showdown
    ```

=== "NuGet"

    ```
    PM> Install-Package showdownjs
    ```

    More information about the package you can find on the [NuGet website](https://www.nuget.org/packages/showdownjs/).

### Client-side

=== "jsDelivr"

    ```
    https://cdn.jsdelivr.net/npm/showdown@<version>/dist/showdown.min.js
    ```
    
    [Showndown page on jsDelivr](https://www.jsdelivr.com/package/npm/showdown)

=== "cdnjs"

    ```
    https://cdnjs.cloudflare.com/ajax/libs/showdown/<version>/showdown.min.js
    ```

    [Showndown page on cdnjs](https://cdnjs.com/libraries/showdown)

=== "unpkg"

    ```
    https://unpkg.com/showdown/dist/showdown.min.js
    ```

    [Showndown page on unpkg](https://unpkg.com/browse/showdown@latest/)

!!! note ""
    Replace `<version>` with an actual full length version you're interested in. For example, `2.0.3`.

## Usage

Once installed, you can use Showndown according to the chosen method:

### Server-side

!!! example "Node.js"

    === "code"

        ```js
        var showdown  = require('showdown'),
            converter = new showdown.Converter(),
            text      = '# hello, markdown!',
            html      = converter.makeHtml(text);
        ```
    
    === "output"

        ```html
        <h1 id="hellomarkdown">hello, markdown!</h1>
        ```

### Client-side

!!! example "Browser"

    === "code"

        ```js
        var converter = new showdown.Converter(),
            text      = '# hello, markdown!',
            html      = converter.makeHtml(text);
        ```

    === "output"

        ```html
        <h1 id="hellomarkdown">hello, markdown!</h1>
        ```

!!! warning "Potential XSS vulnerabilities"
    Showdown doesn't sanitize the input since Markdown relies on it to parse certain features correctly into HTML. As a result, this may lead to potential XSS injection vulnerabilities.

    Please refer to the [Markdown's XSS vulnerability](xss.md) page for more information.

## Other installation methods

### Tarball

You can download the latest tarball directly from [releases][releases].

## Previous versions

If you're looking for Showdown prior to version 1.0.0, you can find them in the [legacy branch][legacy-branch].

## Changelog

The full changelog is available [here][changelog].

[legacy-branch]: https://github.com/showdownjs/showdown/tree/legacy
[releases]: https://github.com/showdownjs/showdown/releases
[changelog]: https://github.com/showdownjs/showdown/blob/master/CHANGELOG.md
```

## File: `docs/xss.md`
```markdown
# Markdown's XSS vulnerability

## Introduction

Cross-Site Scripting (XSS) is a well-known technique to gain access to the private information of users on a website. The attacker injects spurious HTML content (a script) on the web page. This script can read the user’s cookies and do other malicious actions (like steal credentials). As a countermeasure, you should always filter user input for suspicious content. Showdown doesn’t include an XSS filter, so you must provide your own. But be careful in how you do it.

## Markdown is inherently unsafe

Markdown syntax allows the inclusion of arbitrary HTML. For example, below is a perfectly valid Markdown:

```md
This is a regular paragraph.

<table>
    <tr><td>Foo</td></tr>
</table>

This is another regular paragraph.
```

This means that an attacker could do something like this:

```md
This is a regular paragraph.

<script>alert('xss');</script>

This is another regular paragraph.
```

While `alert('xss');` is hardly problematic (maybe just annoying) a real-world scenario might be a lot worse. Obviously, you can easily prevent this kind of this straightforward attack. For example, you can define a whitelist for Showdown that will contain a limited set of allowed HTML tags. However, an attacker can easily circumvent this "defense".

## Whitelist / blacklist can't prevent XSS

Consider the following Markdown content:

```md
hello <a href="www.google.com">*you*</a>
```

As you can see, it's a link, nothing malicious about this. And `<a>` tags are pretty innocuous, right? Showdown should definitely allow them. But what if the content is slightly altered, like this:

```md
hello <a name="n" href="javascript:alert('xss')">*you*</a>
```

Now this is a lot more problematic. Once again, it's not that hard to filter Showdown's input to expunge problematic attributes (such as `href` in `<a>` tags) of scripting attacks. In fact, a regular HTML XSS prevention library should catch this kind of straightforward attack.

At this point you're probably thinking that the best way is to follow Stackoverflow's cue and disallow embedded HTML in Markdown. Unfortunately it's still not enough.

## Strip HTML tags is not enough

Consider the following Markdown input:

```md
[some text](javascript:alert('xss'))
```

Showdown will correctly parse this piece of Markdown input as:

```html
<a href="javascript:alert('xss')">some text</a>
```

In this case, it was Markdown's syntax itself to create the dangerous link. HTML XSS filter cannot catch this. And unless you start striping dangerous words like *javascript* (which would make this article extremely hard to write), there's nothing you can really do to filter XSS attacks from your input. Things get even harder when you tightly mix HTML with Markdown.

## Mixed HTML/Markdown XSS attack

Consider the following piece of Markdown:

```md
> hello <a name="n"
> href="javascript:alert('xss')">*you*</a>
```

If you apply an XSS filter to filter bad HTML in this Markdown input, the XSS filter, expecting HTML, will likely think the `<a>` tag ends with the first character on the second line and will leave the text snippet untouched. It will probably fail to see that the `href="javascript:…"` is part of the `<a>` element and leave it alone. But when Markdown converts this to HTML, you get this:

```html
<blockquote>
 <p>hello <a name="n"
 href="javascript:alert('xss')"><em>you</em></a></p>
</blockquote>
```

After parsing with Markdown, the first `>` on the second line disappears because it was the blockquote marker in the Markdown blockquote syntax. As a result, you’ve got a link containing an XSS attack!

Did Markdown generate the HTML? No, the HTML was already in plain sight in the input. The XSS filter couldn’t catch it because the input doesn’t follow HTML rules: it’s a mix of Markdown and HTML, and the filter doesn’t know a dime about Markdown.

## Mitigate XSS

So, is it all lost? Not really. The answer is not to filter the *input* but rather the *output*. After the *input* text is converted into full-fledged HTML, you can reliably apply the correct XSS filters to remove any dangerous or malicious content.

Also, client-side validations are not reliable. It should be a given, but in case you're wondering, you should (almost) never trust data sent by the client. If there's some critical operation you must perform on the data (such as XSS filtering), you should do it *SERVER-SIDE* not client-side.

HTML XSS filtering libraries are useful here since they prevent most of the attacks. However, you should not use them blindly: a library can't predict all the contexts and situations your application may face.

## Conclusion

Showdown tries to convert the input text as closely as possible, without any concerns for XSS attacks or malicious intent. So, the basic rules are:

* **removing HTML entities from Markdown does not prevent XSS**. Markdown syntax can generate XSS attacks.
* **XSS filtering should be done after Showdown has processed input, not before or during**. If you filter before, it will break some of Markdown’s features and will leave security holes.
* **perform the necessary filtering server-side, not client-side**. XSS filtering libraries are useful but should not be used blindly.

## Disclaimer

This page is based on the excellent article: ["Markdown and XSS"][1] by [Michel Fortin][2] 

[1]: https://michelf.ca/blog/2010/markdown-and-xss/
[2]: https://github.com/michelf
```

## File: `docs/assets/extra.css`
```css
:root {
  --md-primary-fg-color: rgb(196, 54, 39);
  --md-accent-fg-color: rgb(62, 139, 138);
}
```

## File: `docs/tutorials/add-default-class-to-html.md`
```markdown
# Add default class for each HTML element

Many people use CSS kits like Bootstrap, Semantic UI, or others that require default name classes for HTML elements:

```html
<h1 class="ui large header">1st Heading</h1>
<h2 class="ui medium header">2nd Heading</h2>
<ul class="ui list">
  <li class="ui item">first item</li>
  <li class="ui item">second item</li>
</ul>
```

Showdown does not support this out-of-the-box. But you can create an extension for this:

```js
const showdown = require('showdown');

const classMap = {
  h1: 'ui large header',
  h2: 'ui medium header',
  ul: 'ui list',
  li: 'ui item'
}

const bindings = Object.keys(classMap)
  .map(key => ({
    type: 'output',
    regex: new RegExp(`<${key}(.*)>`, 'g'),
    replace: `<${key} class="${classMap[key]}" $1>`
  }));

const conv = new showdown.Converter({
  extensions: [...bindings]
});

const text = `
# 1st Heading
## 2nd Heading

- first item
- second item
`;
```

With this extension, the output will be as follows:

```html
​​​​​<h1 class="ui large header">1st Heading</h1>​​​​​
​​​​​<h2 class="ui medium header">2nd Heading</h2>​​​​​
​​​​​<ul class="ui list">​​​​​
  ​​​​​<li class="ui item">first item</li>​​​​​
  ​​​​​<li class="ui item">second item</li>​​​​​
​​​​​</ul>​​​​​
```

## Credits

* Initial creator: [@zusamann](https://github.com/zusamann), [(original issue)](https://github.com/showdownjs/showdown/issues/376).
* Updated by [@Kameelridder](https://github.com/Kameelridder), [(original issue)](https://github.com/showdownjs/showdown/issues/509).
```

## File: `docs/tutorials/index.md`
```markdown
# Tutorials

* [Add default class for each HTML element](add-default-class-to-html.md)
* [Markdown editor with Showdown](markdown-editor-with-showdown.md)
* [Use language and output extensions on the same block](use-both-extension-types-together.md)
```

## File: `docs/tutorials/markdown-editor-with-showdown.md`
```markdown
# Markdown editor with Showdown

## Introduction

In this tutorial, you will create a simple in-browser Markdown editor using Showdown and some of its extensions. The purpose is to show how easy it is to include and configure Showdown in your project.

The fully working example you can see in [Fiddle][1].

## Step 1: Prepare project

1. Install [node.js](https://nodejs.org/en/).
1. Install project package management tool

    !!! info ""
        Showdown core library doesn't have any dependencies so the setup is pretty straightforward. However, you are strongly encouraged to use a package manager such as [**npm**](http://npmjs.com) or [**yarn**](https://yarnpkg.com) to manage project dependencies.

    To install package management tool:

    1. Create a directory called `showdown-editor` and recreate the following structure:

        ```
        showdown-editor
        ├── css
        │   └── style.css
        ├── js
        │   └── script.js
        └── index.html
        ```

    1. Initialize `package.json` file by running the following interactive console command:

        ```
        npm init -y
        ```

        This command creates `package.json` file in the root of the project folder, and populates the default content that you can change later if you wish.

## Step 2: Install Showdown

Inside the `showdown-editor` directory, run the following command:

```
npm install showdown --save
```

This command will install `showdown` inside the `node_modules` directory and save `showdown` as a dependency in the `package.json` file.

## Step 3: Update project files

Add the following content to the corresponding project files:

=== "index.html"

    ```html
    <!DOCTYPE HTML>
    <html>
    <head>
      <meta charset="UTF-8"/>
      <link rel="stylesheet" href="css/style.css"/>
    </head>
    <body>
      
      <textarea id="sourceTA" rows="10" cols="82">
    Showdown Tutorial
    =================

    This is a showdown tutorial. 

    Showdown supports a number of cool features, namely:

      - headers 
      - lists
      - and other stuff too
      
    It is also possible to include code:

        var foo = 'bar';
        
        var baz = {
          markdown: 'is great',
          showdown: 'is awesome'
        }

    Don't forget to check the [extensions wiki][1].

    [1]: https://github.com/showdownjs/showdown/wiki/extensions
      </textarea>
      <hr/>
      <button id="runBtn" onClick="run()">Convert</button>
      <hr/>
      <div id="targetDiv"></div>
      
      <script src="node_modules/showdown/dist/showdown.min.js"></script>
      <script src="js/script.js"></script>
    </body>
    </html>
    ```

    !!! warning ""
        Please note how Showdown and the script file are included to the `index.html` via the `script` tag at the bottom of the file.

=== "style.css"

    ```css
    #sourceTA {
      display: block;
    }
    #targetDiv {
      border: 1px dashed #333333;
      width: 600px;
      height: 400px;
    }
    ```

=== "script.js"

    ```js
    function run() {
      var text = document.getElementById('sourceTA').value,
      target = document.getElementById('targetDiv'),
      converter = new showdown.Converter(),
      html = converter.makeHtml(text);
      
      target.innerHTML = html;
    }
    ```

    The `script.js` file is simple: when the `runBtn` button is clicked, the script gets the text of the textarea, passes it through Showdown to convert the markdown text into HTML. The resulting HTML is then put inside the `targetDiv`, replacing the previous content.

## Step 4: Check the result

1. Open your `index.html` file. You should see your editor with prefilled markdown text in the text area.
1. Click `Convert` button. You show see the text to be converted to HTML:

    ![](../assets/markdown-editor.png)

The fully working example you can see in [Fiddle][1].

## Conclusion

Congratulations! :tada: You have successfully created a simple Markdown editor!

[1]: http://jsfiddle.net/tivie/6bnpptkb/
```

## File: `docs/tutorials/use-both-extension-types-together.md`
```markdown
# Use language and output extensions on the same block

## Overview

Showdown allows you to define and use any number of extensions that act on the same block. These extensions can be executed sequentially or at different moments.

This enables you to pre-parse/mark a block of text but defer any modifications for the last by using a combination of language and output extensions.

This is useful if you, for example, don't want Showdown to parse the contents of your new language construct.

## Example

Let's say you create an extension that captures everything between `%start%` and `%end%`. However, that content should not be modified by Showdown. Obviously, you can use `<pre>` tags but that is beside the point.

Although Showdown doesn't have any flag to prevent parsing the content of an extension, the same effect can be easily achieved by using lang and output extensions together.

!!! example ""
    The fully working example you can see in [Fiddle][1].

### Code

[Create your extensions](../create-extension.md) with the following content:

```js
showdown.extension('myExt', function() {
  var matches = [];
  return [
    { 
      type: 'lang',
      regex: /%start%([^]+?)%end%/gi,
      replace: function(s, match) { 
        matches.push(match);
        var n = matches.length - 1;
        return '%PLACEHOLDER' + n + '%';
      }
    },
    {
      type: 'output',
      filter: function (text) {
        for (var i=0; i< matches.length; ++i) {
          var pat = '<p>%PLACEHOLDER' + i + '% *<\/p>';
          text = text.replace(new RegExp(pat, 'gi'), matches[i]);
        }
        //reset array
        matches = [];
        return text;
      }
    }
  ]
});
```

In this example, you created a [`lang` extension](../create-extension.md#type) that:

1. Checks for the pseudo tags `%start%` and `%end%`.
1. Extracts everything in between the tags.
1. Saves the content between the tags in a variable.
1. Replaces the saved content with a placeholder to identify the exact position of the extracted text.

and an [`output` extension](../create-extension.md#type) that replaces the placeholder with the saved content, once Showdown is finished parsing.

[1]: http://jsfiddle.net/tivie/1rqr7xy8/
```

## File: `src/converter.js`
```javascript
/**
 * Created by Estevao on 31-05-2015.
 */

/**
 * Showdown Converter class
 * @class
 * @param {object} [converterOptions]
 * @returns {Converter}
 */
showdown.Converter = function (converterOptions) {
  'use strict';

  var
      /**
       * Options used by this converter
       * @private
       * @type {{}}
       */
      options = {},

      /**
       * Language extensions used by this converter
       * @private
       * @type {Array}
       */
      langExtensions = [],

      /**
       * Output modifiers extensions used by this converter
       * @private
       * @type {Array}
       */
      outputModifiers = [],

      /**
       * Event listeners
       * @private
       * @type {{}}
       */
      listeners = {},

      /**
       * The flavor set in this converter
       */
      setConvFlavor = setFlavor,

      /**
       * Metadata of the document
       * @type {{parsed: {}, raw: string, format: string}}
       */
      metadata = {
        parsed: {},
        raw: '',
        format: ''
      };

  _constructor();

  /**
   * Converter constructor
   * @private
   */
  function _constructor () {
    converterOptions = converterOptions || {};

    for (var gOpt in globalOptions) {
      if (globalOptions.hasOwnProperty(gOpt)) {
        options[gOpt] = globalOptions[gOpt];
      }
    }

    // Merge options
    if (typeof converterOptions === 'object') {
      for (var opt in converterOptions) {
        if (converterOptions.hasOwnProperty(opt)) {
          options[opt] = converterOptions[opt];
        }
      }
    } else {
      throw Error('Converter expects the passed parameter to be an object, but ' + typeof converterOptions +
      ' was passed instead.');
    }

    if (options.extensions) {
      showdown.helper.forEach(options.extensions, _parseExtension);
    }
  }

  /**
   * Parse extension
   * @param {*} ext
   * @param {string} [name='']
   * @private
   */
  function _parseExtension (ext, name) {

    name = name || null;
    // If it's a string, the extension was previously loaded
    if (showdown.helper.isString(ext)) {
      ext = showdown.helper.stdExtName(ext);
      name = ext;

      // LEGACY_SUPPORT CODE
      if (showdown.extensions[ext]) {
        console.warn('DEPRECATION WARNING: ' + ext + ' is an old extension that uses a deprecated loading method.' +
          'Please inform the developer that the extension should be updated!');
        legacyExtensionLoading(showdown.extensions[ext], ext);
        return;
        // END LEGACY SUPPORT CODE

      } else if (!showdown.helper.isUndefined(extensions[ext])) {
        ext = extensions[ext];

      } else {
        throw Error('Extension "' + ext + '" could not be loaded. It was either not found or is not a valid extension.');
      }
    }

    if (typeof ext === 'function') {
      ext = ext();
    }

    if (!showdown.helper.isArray(ext)) {
      ext = [ext];
    }

    var validExt = validate(ext, name);
    if (!validExt.valid) {
      throw Error(validExt.error);
    }

    for (var i = 0; i < ext.length; ++i) {
      switch (ext[i].type) {

        case 'lang':
          langExtensions.push(ext[i]);
          break;

        case 'output':
          outputModifiers.push(ext[i]);
          break;
      }
      if (ext[i].hasOwnProperty('listeners')) {
        for (var ln in ext[i].listeners) {
          if (ext[i].listeners.hasOwnProperty(ln)) {
            listen(ln, ext[i].listeners[ln]);
          }
        }
      }
    }

  }

  /**
   * LEGACY_SUPPORT
   * @param {*} ext
   * @param {string} name
   */
  function legacyExtensionLoading (ext, name) {
    if (typeof ext === 'function') {
      ext = ext(new showdown.Converter());
    }
    if (!showdown.helper.isArray(ext)) {
      ext = [ext];
    }
    var valid = validate(ext, name);

    if (!valid.valid) {
      throw Error(valid.error);
    }

    for (var i = 0; i < ext.length; ++i) {
      switch (ext[i].type) {
        case 'lang':
          langExtensions.push(ext[i]);
          break;
        case 'output':
          outputModifiers.push(ext[i]);
          break;
        default:// should never reach here
          throw Error('Extension loader error: Type unrecognized!!!');
      }
    }
  }

  /**
   * Listen to an event
   * @param {string} name
   * @param {function} callback
   */
  function listen (name, callback) {
    if (!showdown.helper.isString(name)) {
      throw Error('Invalid argument in converter.listen() method: name must be a string, but ' + typeof name + ' given');
    }

    if (typeof callback !== 'function') {
      throw Error('Invalid argument in converter.listen() method: callback must be a function, but ' + typeof callback + ' given');
    }
    name = name.toLowerCase();
    if (!listeners.hasOwnProperty(name)) {
      listeners[name] = [];
    }
    listeners[name].push(callback);
  }

  function rTrimInputText (text) {
    var rsp = text.match(/^\s*/)[0].length,
        rgx = new RegExp('^\\s{0,' + rsp + '}', 'gm');
    return text.replace(rgx, '');
  }

  /**
   *
   * @param {string} evtName Event name
   * @param {string} text Text
   * @param {{}} options Converter Options
   * @param {{}} globals Converter globals
   * @param {{}} [pParams] extra params for event
   * @returns showdown.helper.Event
   * @private
   */
  this._dispatch = function dispatch (evtName, text, options, globals, pParams) {
    evtName = evtName.toLowerCase();
    var params = pParams || {};
    params.converter = this;
    params.text = text;
    params.options = options;
    params.globals = globals;
    var event = new showdown.helper.Event(evtName, text, params);

    if (listeners.hasOwnProperty(evtName)) {
      for (var ei = 0; ei < listeners[evtName].length; ++ei) {
        var nText = listeners[evtName][ei](event);
        if (nText && typeof nText !== 'undefined') {
          event.setText(nText);
        }
      }
    }
    return event;
  };

  /**
   * Listen to an event
   * @param {string} name
   * @param {function} callback
   * @returns {showdown.Converter}
   */
  this.listen = function (name, callback) {
    listen(name, callback);
    return this;
  };

  /**
   * Converts a markdown string into HTML string
   * @param {string} text
   * @returns {*}
   */
  this.makeHtml = function (text) {
    //check if text is not falsy
    if (!text) {
      return text;
    }

    var globals = {
      gHtmlBlocks:     [],
      gHtmlMdBlocks:   [],
      gHtmlSpans:      [],
      gUrls:           {},
      gTitles:         {},
      gDimensions:     {},
      gListLevel:      0,
      hashLinkCounts:  {},
      langExtensions:  langExtensions,
      outputModifiers: outputModifiers,
      converter:       this,
      ghCodeBlocks:    [],
      metadata: {
        parsed: {},
        raw: '',
        format: ''
      }
    };

    // This lets us use ¨ trema as an escape char to avoid md5 hashes
    // The choice of character is arbitrary; anything that isn't
    // magic in Markdown will work.
    text = text.replace(/¨/g, '¨T');

    // Replace $ with ¨D
    // RegExp interprets $ as a special character
    // when it's in a replacement string
    text = text.replace(/\$/g, '¨D');

    // Standardize line endings
    text = text.replace(/\r\n/g, '\n'); // DOS to Unix
    text = text.replace(/\r/g, '\n'); // Mac to Unix

    // Stardardize line spaces
    text = text.replace(/\u00A0/g, '&nbsp;');

    if (options.smartIndentationFix) {
      text = rTrimInputText(text);
    }

    // Make sure text begins and ends with a couple of newlines:
    text = '\n\n' + text + '\n\n';

    // detab
    text = showdown.subParser('makehtml.detab')(text, options, globals);

    /**
     * Strip any lines consisting only of spaces and tabs.
     * This makes subsequent regexs easier to write, because we can
     * match consecutive blank lines with /\n+/ instead of something
     * contorted like /[ \t]*\n+/
     */
    text = text.replace(/^[ \t]+$/mg, '');

    //run languageExtensions
    showdown.helper.forEach(langExtensions, function (ext) {
      text = showdown.subParser('makehtml.runExtension')(ext, text, options, globals);
    });

    // run the sub parsers
    text = showdown.subParser('makehtml.metadata')(text, options, globals);
    text = showdown.subParser('makehtml.hashPreCodeTags')(text, options, globals);
    text = showdown.subParser('makehtml.githubCodeBlocks')(text, options, globals);
    text = showdown.subParser('makehtml.hashHTMLBlocks')(text, options, globals);
    text = showdown.subParser('makehtml.hashCodeTags')(text, options, globals);
    text = showdown.subParser('makehtml.stripLinkDefinitions')(text, options, globals);
    text = showdown.subParser('makehtml.blockGamut')(text, options, globals);
    text = showdown.subParser('makehtml.unhashHTMLSpans')(text, options, globals);
    text = showdown.subParser('makehtml.unescapeSpecialChars')(text, options, globals);

    // attacklab: Restore dollar signs
    text = text.replace(/¨D/g, '$$');

    // attacklab: Restore tremas
    text = text.replace(/¨T/g, '¨');

    // render a complete html document instead of a partial if the option is enabled
    text = showdown.subParser('makehtml.completeHTMLDocument')(text, options, globals);

    // Run output modifiers
    showdown.helper.forEach(outputModifiers, function (ext) {
      text = showdown.subParser('makehtml.runExtension')(ext, text, options, globals);
    });

    // update metadata
    metadata = globals.metadata;
    return text;
  };

  /**
   * Converts an HTML string into a markdown string
   * @param src
   * @returns {string}
   */
  this.makeMarkdown = function (src) {

    // replace \r\n with \n
    src = src.replace(/\r\n/g, '\n');
    src = src.replace(/\r/g, '\n'); // old macs

    // due to an edge case, we need to find this: > <
    // to prevent removing of non silent white spaces
    // ex: <em>this is</em> <strong>sparta</strong>
    src = src.replace(/>[ \t]+</, '>¨NBSP;<');

    var doc = showdown.helper.document.createElement('div');
    doc.innerHTML = src;

    var globals = {
      preList: substitutePreCodeTags(doc)
    };

    // remove all newlines and collapse spaces
    clean(doc);

    // some stuff, like accidental reference links must now be escaped
    // TODO
    // doc.innerHTML = doc.innerHTML.replace(/\[[\S\t ]]/);

    var nodes = doc.childNodes,
        mdDoc = '';

    for (var i = 0; i < nodes.length; i++) {
      mdDoc += showdown.subParser('makeMarkdown.node')(nodes[i], options, globals);
    }

    function clean (node) {
      for (var n = 0; n < node.childNodes.length; ++n) {
        var child = node.childNodes[n];
        if (child.nodeType === 3) {
          if (!/\S/.test(child.nodeValue) && !/^[ ]+$/.test(child.nodeValue)) {
            node.removeChild(child);
            --n;
          } else {
            child.nodeValue = child.nodeValue.split('\n').join(' ');
            child.nodeValue = child.nodeValue.replace(/(\s)+/g, '$1');
          }
        } else if (child.nodeType === 1) {
          clean(child);
        }
      }
    }

    // find all pre tags and replace contents with placeholder
    // we need this so that we can remove all indentation from html
    // to ease up parsing
    function substitutePreCodeTags (doc) {

      var pres = doc.querySelectorAll('pre'),
          presPH = [];

      for (var i = 0; i < pres.length; ++i) {

        if (pres[i].childElementCount === 1 && pres[i].firstChild.tagName.toLowerCase() === 'code') {
          var content = pres[i].firstChild.innerHTML.trim(),
              language = pres[i].firstChild.getAttribute('data-language') || '';

          // if data-language attribute is not defined, then we look for class language-*
          if (language === '') {
            var classes = pres[i].firstChild.className.split(' ');
            for (var c = 0; c < classes.length; ++c) {
              var matches = classes[c].match(/^language-(.+)$/);
              if (matches !== null) {
                language = matches[1];
                break;
              }
            }
          }

          // unescape html entities in content
          content = showdown.helper.unescapeHTMLEntities(content);

          presPH.push(content);
          pres[i].outerHTML = '<precode language="' + language + '" precodenum="' + i.toString() + '"></precode>';
        } else {
          presPH.push(pres[i].innerHTML);
          pres[i].innerHTML = '';
          pres[i].setAttribute('prenum', i.toString());
        }
      }
      return presPH;
    }

    return mdDoc;
  };

  /**
   * Set an option of this Converter instance
   * @param {string} key
   * @param {*} value
   */
  this.setOption = function (key, value) {
    options[key] = value;
  };

  /**
   * Get the option of this Converter instance
   * @param {string} key
   * @returns {*}
   */
  this.getOption = function (key) {
    return options[key];
  };

  /**
   * Get the options of this Converter instance
   * @returns {{}}
   */
  this.getOptions = function () {
    return options;
  };

  /**
   * Add extension to THIS converter
   * @param {{}} extension
   * @param {string} [name=null]
   */
  this.addExtension = function (extension, name) {
    name = name || null;
    _parseExtension(extension, name);
  };

  /**
   * Use a global registered extension with THIS converter
   * @param {string} extensionName Name of the previously registered extension
   */
  this.useExtension = function (extensionName) {
    _parseExtension(extensionName);
  };

  /**
   * Set the flavor THIS converter should use
   * @param {string} name
   */
  this.setFlavor = function (name) {
    if (!flavor.hasOwnProperty(name)) {
      throw Error(name + ' flavor was not found');
    }
    var preset = flavor[name];
    setConvFlavor = name;
    for (var option in preset) {
      if (preset.hasOwnProperty(option)) {
        options[option] = preset[option];
      }
    }
  };

  /**
   * Get the currently set flavor of this converter
   * @returns {string}
   */
  this.getFlavor = function () {
    return setConvFlavor;
  };

  /**
   * Remove an extension from THIS converter.
   * Note: This is a costly operation. It's better to initialize a new converter
   * and specify the extensions you wish to use
   * @param {Array} extension
   */
  this.removeExtension = function (extension) {
    if (!showdown.helper.isArray(extension)) {
      extension = [extension];
    }
    for (var a = 0; a < extension.length; ++a) {
      var ext = extension[a];
      for (var i = 0; i < langExtensions.length; ++i) {
        if (langExtensions[i] === ext) {
          langExtensions.splice(i, 1);
        }
      }
      for (var ii = 0; ii < outputModifiers.length; ++ii) {
        if (outputModifiers[ii] === ext) {
          outputModifiers.splice(ii, 1);
        }
      }
    }
  };

  /**
   * Get all extension of THIS converter
   * @returns {{language: Array, output: Array}}
   */
  this.getAllExtensions = function () {
    return {
      language: langExtensions,
      output: outputModifiers
    };
  };

  /**
   * Get the metadata of the previously parsed document
   * @param raw
   * @returns {string|{}}
   */
  this.getMetadata = function (raw) {
    if (raw) {
      return metadata.raw;
    } else {
      return metadata.parsed;
    }
  };

  /**
   * Get the metadata format of the previously parsed document
   * @returns {string}
   */
  this.getMetadataFormat = function () {
    return metadata.format;
  };

  /**
   * Private: set a single key, value metadata pair
   * @param {string} key
   * @param {string} value
   */
  this._setMetadataPair = function (key, value) {
    metadata.parsed[key] = value;
  };

  /**
   * Private: set metadata format
   * @param {string} format
   */
  this._setMetadataFormat = function (format) {
    metadata.format = format;
  };

  /**
   * Private: set metadata raw text
   * @param {string} raw
   */
  this._setMetadataRaw = function (raw) {
    metadata.raw = raw;
  };
};
```

## File: `src/helpers.js`
```javascript
/**
 * showdownjs helper functions
 */

if (!showdown.hasOwnProperty('helper')) {
  showdown.helper = {};
}

if (typeof this === 'undefined' && typeof window !== 'undefined') {
  showdown.helper.document = window.document;
} else {
  if (typeof this.document === 'undefined' && typeof this.window === 'undefined') {
    var jsdom = require('jsdom');
    this.window = new jsdom.JSDOM('', {}).window; // jshint ignore:line
  }
  showdown.helper.document = this.window.document;
}

/**
 * Check if var is string
 * @static
 * @param {string} a
 * @returns {boolean}
 */
showdown.helper.isString = function (a) {
  'use strict';
  return (typeof a === 'string' || a instanceof String);
};

/**
 * Check if var is a function
 * @static
 * @param {*} a
 * @returns {boolean}
 */
showdown.helper.isFunction = function (a) {
  'use strict';
  var getType = {};
  return a && getType.toString.call(a) === '[object Function]';
};

/**
 * isArray helper function
 * @static
 * @param {*} a
 * @returns {boolean}
 */
showdown.helper.isArray = function (a) {
  'use strict';
  let isArray;
  if (!Array.isArray) {
    isArray = function (arg) {
      return Object.prototype.toString.call(arg) === '[object Array]';
    };
  } else {
    isArray = Array.isArray;
  }
  return isArray(a);
};

/**
 * Check if value is undefined
 * @static
 * @param {*} value The value to check.
 * @returns {boolean} Returns `true` if `value` is `undefined`, else `false`.
 */
showdown.helper.isUndefined = function (value) {
  'use strict';
  return typeof value === 'undefined';
};

/**
 * ForEach helper function
 * Iterates over Arrays and Objects (own properties only)
 * @static
 * @param {*} obj
 * @param {function} callback Accepts 3 params: 1. value, 2. key, 3. the original array/object
 */
showdown.helper.forEach = function (obj, callback) {
  'use strict';
  // check if obj is defined
  if (showdown.helper.isUndefined(obj)) {
    throw new Error('obj param is required');
  }

  if (showdown.helper.isUndefined(callback)) {
    throw new Error('callback param is required');
  }

  if (!showdown.helper.isFunction(callback)) {
    throw new Error('callback param must be a function/closure');
  }

  if (typeof obj.forEach === 'function') {
    obj.forEach(callback);
  } else if (showdown.helper.isArray(obj)) {
    for (var i = 0; i < obj.length; i++) {
      callback(obj[i], i, obj);
    }
  } else if (typeof (obj) === 'object') {
    for (var prop in obj) {
      if (obj.hasOwnProperty(prop)) {
        callback(obj[prop], prop, obj);
      }
    }
  } else {
    throw new Error('obj does not seem to be an array or an iterable object');
  }
};

/**
 * Standardidize extension name
 * @static
 * @param {string} s extension name
 * @returns {string}
 */
showdown.helper.stdExtName = function (s) {
  'use strict';
  return s.replace(/[_?*+\/\\.^-]/g, '').replace(/\s/g, '').toLowerCase();
};

function escapeCharactersCallback (wholeMatch, m1) {
  'use strict';
  var charCodeToEscape = m1.charCodeAt(0);
  return '¨E' + charCodeToEscape + 'E';
}

/**
 * Callback used to escape characters when passing through String.replace
 * @static
 * @param {string} wholeMatch
 * @param {string} m1
 * @returns {string}
 */
showdown.helper.escapeCharactersCallback = escapeCharactersCallback;

/**
 * Escape characters in a string
 * @static
 * @param {string} text
 * @param {string} charsToEscape
 * @param {boolean} afterBackslash
 * @returns {string|void|*}
 */
showdown.helper.escapeCharacters = function (text, charsToEscape, afterBackslash) {
  'use strict';
  // First we have to escape the escape characters so that
  // we can build a character class out of them
  var regexString = '([' + charsToEscape.replace(/([\[\]\\])/g, '\\$1') + '])';

  if (afterBackslash) {
    regexString = '\\\\' + regexString;
  }

  var regex = new RegExp(regexString, 'g');
  text = text.replace(regex, escapeCharactersCallback);

  return text;
};

var rgxFindMatchPos = function (str, left, right, flags) {
  'use strict';
  var f = flags || '',
      g = f.indexOf('g') > -1,
      x = new RegExp(left + '|' + right, 'g' + f.replace(/g/g, '')),
      l = new RegExp(left, f.replace(/g/g, '')),
      pos = [],
      t, s, m, start, end;

  do {
    t = 0;
    while ((m = x.exec(str))) {
      if (l.test(m[0])) {
        if (!(t++)) {
          s = x.lastIndex;
          start = s - m[0].length;
        }
      } else if (t) {
        if (!--t) {
          end = m.index + m[0].length;
          var obj = {
            left: {start: start, end: s},
            match: {start: s, end: m.index},
            right: {start: m.index, end: end},
            wholeMatch: {start: start, end: end}
          };
          pos.push(obj);
          if (!g) {
            return pos;
          }
        }
      }
    }
  } while (t && (x.lastIndex = s));

  return pos;
};

/**
 * matchRecursiveRegExp
 *
 * (c) 2007 Steven Levithan <stevenlevithan.com>
 * MIT License
 *
 * Accepts a string to search, a left and right format delimiter
 * as regex patterns, and optional regex flags. Returns an array
 * of matches, allowing nested instances of left/right delimiters.
 * Use the "g" flag to return all matches, otherwise only the
 * first is returned. Be careful to ensure that the left and
 * right format delimiters produce mutually exclusive matches.
 * Backreferences are not supported within the right delimiter
 * due to how it is internally combined with the left delimiter.
 * When matching strings whose format delimiters are unbalanced
 * to the left or right, the output is intentionally as a
 * conventional regex library with recursion support would
 * produce, e.g. "<<x>" and "<x>>" both produce ["x"] when using
 * "<" and ">" as the delimiters (both strings contain a single,
 * balanced instance of "<x>").
 *
 * examples:
 * matchRecursiveRegExp("test", "\\(", "\\)")
 * returns: []
 * matchRecursiveRegExp("<t<<e>><s>>t<>", "<", ">", "g")
 * returns: ["t<<e>><s>", ""]
 * matchRecursiveRegExp("<div id=\"x\">test</div>", "<div\\b[^>]*>", "</div>", "gi")
 * returns: ["test"]
 */
showdown.helper.matchRecursiveRegExp = function (str, left, right, flags) {
  'use strict';

  var matchPos = rgxFindMatchPos (str, left, right, flags),
      results = [];

  for (var i = 0; i < matchPos.length; ++i) {
    results.push([
      str.slice(matchPos[i].wholeMatch.start, matchPos[i].wholeMatch.end),
      str.slice(matchPos[i].match.start, matchPos[i].match.end),
      str.slice(matchPos[i].left.start, matchPos[i].left.end),
      str.slice(matchPos[i].right.start, matchPos[i].right.end)
    ]);
  }
  return results;
};

/**
 *
 * @param {string} str
 * @param {string|function} replacement
 * @param {string} left
 * @param {string} right
 * @param {string} flags
 * @returns {string}
 */
showdown.helper.replaceRecursiveRegExp = function (str, replacement, left, right, flags) {
  'use strict';

  if (!showdown.helper.isFunction(replacement)) {
    var repStr = replacement;
    replacement = function () {
      return repStr;
    };
  }

  var matchPos = rgxFindMatchPos(str, left, right, flags),
      finalStr = str,
      lng = matchPos.length;

  if (lng > 0) {
    var bits = [];
    if (matchPos[0].wholeMatch.start !== 0) {
      bits.push(str.slice(0, matchPos[0].wholeMatch.start));
    }
    for (var i = 0; i < lng; ++i) {
      bits.push(
        replacement(
          str.slice(matchPos[i].wholeMatch.start, matchPos[i].wholeMatch.end),
          str.slice(matchPos[i].match.start, matchPos[i].match.end),
          str.slice(matchPos[i].left.start, matchPos[i].left.end),
          str.slice(matchPos[i].right.start, matchPos[i].right.end)
        )
      );
      if (i < lng - 1) {
        bits.push(str.slice(matchPos[i].wholeMatch.end, matchPos[i + 1].wholeMatch.start));
      }
    }
    if (matchPos[lng - 1].wholeMatch.end < str.length) {
      bits.push(str.slice(matchPos[lng - 1].wholeMatch.end));
    }
    finalStr = bits.join('');
  }
  return finalStr;
};

/**
 * Returns the index within the passed String object of the first occurrence of the specified regex,
 * starting the search at fromIndex. Returns -1 if the value is not found.
 *
 * @param {string} str string to search
 * @param {RegExp} regex Regular expression to search
 * @param {int} [fromIndex = 0] Index to start the search
 * @returns {Number}
 * @throws InvalidArgumentError
 */
showdown.helper.regexIndexOf = function (str, regex, fromIndex) {
  'use strict';
  if (!showdown.helper.isString(str)) {
    throw 'InvalidArgumentError: first parameter of showdown.helper.regexIndexOf function must be a string';
  }
  if (!(regex instanceof RegExp)) {
    throw 'InvalidArgumentError: second parameter of showdown.helper.regexIndexOf function must be an instance of RegExp';
  }
  var indexOf = str.substring(fromIndex || 0).search(regex);
  return (indexOf >= 0) ? (indexOf + (fromIndex || 0)) : indexOf;
};

/**
 * Splits the passed string object at the defined index, and returns an array composed of the two substrings
 * @param {string} str string to split
 * @param {int} index index to split string at
 * @returns {[string,string]}
 * @throws InvalidArgumentError
 */
showdown.helper.splitAtIndex = function (str, index) {
  'use strict';
  if (!showdown.helper.isString(str)) {
    throw 'InvalidArgumentError: first parameter of showdown.helper.regexIndexOf function must be a string';
  }
  return [str.substring(0, index), str.substring(index)];
};


/**
 * MurmurHash3's mixing function
 * https://stackoverflow.com/questions/521295/seeding-the-random-number-generator-in-javascript/47593316#47593316
 *
 * @param {string} string
 * @returns {Number}
 */
/*jshint bitwise: false*/
function xmur3 (str) {
  for (var i = 0, h = 1779033703 ^ str.length; i < str.length; i++) {
    h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
    h = h << 13 | h >>> 19;
  }
  return function () {
    h = Math.imul(h ^ h >>> 16, 2246822507);
    h = Math.imul(h ^ h >>> 13, 3266489909);
    return (h ^= h >>> 16) >>> 0;
  };
}

/**
 * Random Number Generator
 * https://stackoverflow.com/questions/521295/seeding-the-random-number-generator-in-javascript/47593316#47593316
 *
 * @param {Number} seed
 * @returns {Number}
 */
/*jshint bitwise: false*/
function mulberry32 (a) {
  return function () {
    var t = a += 0x6D2B79F5;
    t = Math.imul(t ^ t >>> 15, t | 1);
    t ^= t + Math.imul(t ^ t >>> 7, t | 61);
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}

/**
 * Obfuscate an e-mail address through the use of Character Entities,
 * transforming ASCII characters into their equivalent decimal or hex entities.
 *
 *
 * @param {string} mail
 * @returns {string}
 */
showdown.helper.encodeEmailAddress = function (mail) {
  'use strict';
  var encode = [
    function (ch) {
      return '&#' + ch.charCodeAt(0) + ';';
    },
    function (ch) {
      return '&#x' + ch.charCodeAt(0).toString(16) + ';';
    },
    function (ch) {
      return ch;
    }
  ];

  // RNG seeded with mail, so that we can get determined results for each email.
  var rand = mulberry32(xmur3(mail));

  mail = mail.replace(/./g, function (ch) {
    if (ch === '@') {
      // this *must* be encoded. I insist.
      ch = encode[Math.floor(rand() * 2)](ch);
    } else {
      var r = rand();
      // roughly 10% raw, 45% hex, 45% dec
      ch = (
        r > 0.9 ? encode[2](ch) : r > 0.45 ? encode[1](ch) : encode[0](ch)
      );
    }
    return ch;
  });

  return mail;
};

/**
 * String.prototype.repeat polyfill
 *
 * @param {string} str
 * @param {int} count
 * @returns {string}
 */
showdown.helper.repeat = function (str, count) {
  'use strict';
  // use built-in method if it's available
  if (!showdown.helper.isUndefined(String.prototype.repeat)) {
    return str.repeat(count);
  }
  str = '' + str;
  if (count < 0) {
    throw new RangeError('repeat count must be non-negative');
  }
  if (count === Infinity) {
    throw new RangeError('repeat count must be less than infinity');
  }
  count = Math.floor(count);
  if (str.length === 0 || count === 0) {
    return '';
  }
  // Ensuring count is a 31-bit integer allows us to heavily optimize the
  // main part. But anyway, most current (August 2014) browsers can't handle
  // strings 1 << 28 chars or longer, so:
  /*jshint bitwise: false*/
  if (str.length * count >= 1 << 28) {
    throw new RangeError('repeat count must not overflow maximum string size');
  }
  /*jshint bitwise: true*/
  var maxCount = str.length * count;
  count = Math.floor(Math.log(count) / Math.log(2));
  while (count) {
    str += str;
    count--;
  }
  str += str.substring(0, maxCount - str.length);
  return str;
};

/**
 * String.prototype.padEnd polyfill
 *
 * @param {string} str
 * @param {int} targetLength
 * @param {string} [padString]
 * @returns {string}
 */
showdown.helper.padEnd = function padEnd (str, targetLength, padString) {
  'use strict';
  /*jshint bitwise: false*/
  // eslint-disable-next-line space-infix-ops
  targetLength = targetLength>>0; //floor if number or convert non-number to 0;
  /*jshint bitwise: true*/
  padString = String(padString || ' ');
  if (str.length > targetLength) {
    return String(str);
  } else {
    targetLength = targetLength - str.length;
    if (targetLength > padString.length) {
      padString += showdown.helper.repeat(padString, targetLength / padString.length); //append to original to ensure we are longer than needed
    }
    return String(str) + padString.slice(0,targetLength);
  }
};

/**
 * Unescape HTML entities
 * @param txt
 * @returns {string}
 */
showdown.helper.unescapeHTMLEntities = function (txt) {
  'use strict';

  return txt
    .replace(/&quot;/g, '"')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&amp;/g, '&');
};

showdown.helper._hashHTMLSpan = function (html, globals) {
  return '¨C' + (globals.gHtmlSpans.push(html) - 1) + 'C';
};

/**
 * Prepends a base URL to relative paths.
 *
 * @param {string} baseUrl the base URL to prepend to a relative path
 * @param {string} url the path to modify, which may be relative
 * @returns {string} the full URL
 */
showdown.helper.applyBaseUrl = function (baseUrl, url) {
  // Only prepend if given a base URL and the path is not absolute.
  if (baseUrl && !this.isAbsolutePath(url)) {
    var urlResolve = require('url').resolve;
    url = urlResolve(baseUrl, url);
  }

  return url;
};

/**
 * Checks if the given path is absolute.
 *
 * @param {string} path the path to test for absolution
 * @returns {boolean} `true` if the given path is absolute, else `false`
 */
showdown.helper.isAbsolutePath = function (path) {
  // Absolute paths begin with '[protocol:]//' or '#' (anchors)
  return /(^([a-z]+:)?\/\/)|(^#)/i.test(path);
};

/**
 * Showdown's Event Object
 * @param {string} name Name of the event
 * @param {string} text Text
 * @param {{}} params optional. params of the event
 * @constructor
 */
showdown.helper.Event = function (name, text, params) {
  'use strict';

  var regexp = params.regexp || null;
  var matches = params.matches || {};
  var options = params.options || {};
  var converter = params.converter || null;
  var globals = params.globals || {};

  /**
   * Get the name of the event
   * @returns {string}
   */
  this.getName = function () {
    return name;
  };

  this.getEventName = function () {
    return name;
  };

  this._stopExecution = false;

  this.parsedText = params.parsedText || null;

  this.getRegexp = function () {
    return regexp;
  };

  this.getOptions = function () {
    return options;
  };

  this.getConverter = function () {
    return converter;
  };

  this.getGlobals = function () {
    return globals;
  };

  this.getCapturedText = function () {
    return text;
  };

  this.getText = function () {
    return text;
  };

  this.setText = function (newText) {
    text = newText;
  };

  this.getMatches = function () {
    return matches;
  };

  this.setMatches = function (newMatches) {
    matches = newMatches;
  };

  this.preventDefault = function (bool) {
    this._stopExecution = !bool;
  };
};

/**
 * POLYFILLS
 */
// use this instead of builtin is undefined for IE8 compatibility
if (typeof (console) === 'undefined') {
  console = {
    warn: function (msg) {
      'use strict';
      alert(msg);
    },
    log: function (msg) {
      'use strict';
      alert(msg);
    },
    error: function (msg) {
      'use strict';
      throw msg;
    }
  };
}

// Math.imul() polyfill
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/imul
if (!Math.imul) {
  Math.imul = function (opA, opB) {
    opB |= 0; // ensure that opB is an integer. opA will automatically be coerced.
    // floating points give us 53 bits of precision to work with plus 1 sign bit
    // automatically handled for our convienence:
    // 1. 0x003fffff /*opA & 0x000fffff*/ * 0x7fffffff /*opB*/ = 0x1fffff7fc00001
    //    0x1fffff7fc00001 < Number.MAX_SAFE_INTEGER /*0x1fffffffffffff*/
    var result = (opA & 0x003fffff) * opB;
    // 2. We can remove an integer coersion from the statement above because:
    //    0x1fffff7fc00001 + 0xffc00000 = 0x1fffffff800001
    //    0x1fffffff800001 < Number.MAX_SAFE_INTEGER /*0x1fffffffffffff*/
    if (opA & 0xffc00000 /*!== 0*/) {
      result += (opA & 0xffc00000) * opB | 0;
    }
    return result | 0;
  };
}

/**
 * Common regexes.
 * We declare some common regexes to improve performance
 */
showdown.helper.regexes = {
  asteriskDashTildeAndColon: /([*_:~])/g,
  asteriskDashAndTilde:      /([*_~])/g
};

/**
 * EMOJIS LIST
 */
showdown.helper.emojis = {
  '100': '\ud83d\udcaf',
  '1234': '\ud83d\udd22',
  '+1': '\ud83d\udc4d',
  '-1': '\ud83d\udc4e',
  '1st_place_medal': '\ud83e\udd47',
  '2nd_place_medal': '\ud83e\udd48',
  '3rd_place_medal': '\ud83e\udd49',
  '8ball': '\ud83c\udfb1',
  'a': '\ud83c\udd70\ufe0f',
  'ab': '\ud83c\udd8e',
  'abacus': '\ud83e\uddee',
  'abc': '\ud83d\udd24',
  'abcd': '\ud83d\udd21',
  'accept': '\ud83c\ude51',
  'adhesive_bandage': '\ud83e\ude79',
  'adult': '\ud83e\uddd1',
  'aerial_tramway': '\ud83d\udea1',
  'afghanistan': '\ud83c\udde6\ud83c\uddeb',
  'airplane': '\u2708\ufe0f',
  'aland_islands': '\ud83c\udde6\ud83c\uddfd',
  'alarm_clock': '\u23f0',
  'albania': '\ud83c\udde6\ud83c\uddf1',
  'alembic': '\u2697\ufe0f',
  'algeria': '\ud83c\udde9\ud83c\uddff',
  'alien': '\ud83d\udc7d',
  'ambulance': '\ud83d\ude91',
  'american_samoa': '\ud83c\udde6\ud83c\uddf8',
  'amphora': '\ud83c\udffa',
  'anchor': '\u2693',
  'andorra': '\ud83c\udde6\ud83c\udde9',
  'angel': '\ud83d\udc7c',
  'anger': '\ud83d\udca2',
  'angola': '\ud83c\udde6\ud83c\uddf4',
  'angry': '\ud83d\ude20',
  'anguilla': '\ud83c\udde6\ud83c\uddee',
  'anguished': '\ud83d\ude27',
  'ant': '\ud83d\udc1c',
  'antarctica': '\ud83c\udde6\ud83c\uddf6',
  'antigua_barbuda': '\ud83c\udde6\ud83c\uddec',
  'apple': '\ud83c\udf4e',
  'aquarius': '\u2652',
  'argentina': '\ud83c\udde6\ud83c\uddf7',
  'aries': '\u2648',
  'armenia': '\ud83c\udde6\ud83c\uddf2',
  'arrow_backward': '\u25c0\ufe0f',
  'arrow_double_down': '\u23ec',
  'arrow_double_up': '\u23eb',
  'arrow_down': '\u2b07\ufe0f',
  'arrow_down_small': '\ud83d\udd3d',
  'arrow_forward': '\u25b6\ufe0f',
  'arrow_heading_down': '\u2935\ufe0f',
  'arrow_heading_up': '\u2934\ufe0f',
  'arrow_left': '\u2b05\ufe0f',
  'arrow_lower_left': '\u2199\ufe0f',
  'arrow_lower_right': '\u2198\ufe0f',
  'arrow_right': '\u27a1\ufe0f',
  'arrow_right_hook': '\u21aa\ufe0f',
  'arrow_up': '\u2b06\ufe0f',
  'arrow_up_down': '\u2195\ufe0f',
  'arrow_up_small': '\ud83d\udd3c',
  'arrow_upper_left': '\u2196\ufe0f',
  'arrow_upper_right': '\u2197\ufe0f',
  'arrows_clockwise': '\ud83d\udd03',
  'arrows_counterclockwise': '\ud83d\udd04',
  'art': '\ud83c\udfa8',
  'articulated_lorry': '\ud83d\ude9b',
  'artificial_satellite': '\ud83d\udef0\ufe0f',
  'artist': '\ud83e\uddd1\u200d\ud83c\udfa8',
  'aruba': '\ud83c\udde6\ud83c\uddfc',
  'ascension_island': '\ud83c\udde6\ud83c\udde8',
  'asterisk': '*\ufe0f\u20e3',
  'astonished': '\ud83d\ude32',
  'astronaut': '\ud83e\uddd1\u200d\ud83d\ude80',
  'athletic_shoe': '\ud83d\udc5f',
  'atm': '\ud83c\udfe7',
  'atom_symbol': '\u269b\ufe0f',
  'australia': '\ud83c\udde6\ud83c\uddfa',
  'austria': '\ud83c\udde6\ud83c\uddf9',
  'auto_rickshaw': '\ud83d\udefa',
  'avocado': '\ud83e\udd51',
  'axe': '\ud83e\ude93',
  'azerbaijan': '\ud83c\udde6\ud83c\uddff',
  'b': '\ud83c\udd71\ufe0f',
  'baby': '\ud83d\udc76',
  'baby_bottle': '\ud83c\udf7c',
  'baby_chick': '\ud83d\udc24',
  'baby_symbol': '\ud83d\udebc',
  'back': '\ud83d\udd19',
  'bacon': '\ud83e\udd53',
  'badger': '\ud83e\udda1',
  'badminton': '\ud83c\udff8',
  'bagel': '\ud83e\udd6f',
  'baggage_claim': '\ud83d\udec4',
  'baguette_bread': '\ud83e\udd56',
  'bahamas': '\ud83c\udde7\ud83c\uddf8',
  'bahrain': '\ud83c\udde7\ud83c\udded',
  'balance_scale': '\u2696\ufe0f',
  'bald_man': '\ud83d\udc68\u200d\ud83e\uddb2',
  'bald_woman': '\ud83d\udc69\u200d\ud83e\uddb2',
  'ballet_shoes': '\ud83e\ude70',
  'balloon': '\ud83c\udf88',
  'ballot_box': '\ud83d\uddf3\ufe0f',
  'ballot_box_with_check': '\u2611\ufe0f',
  'bamboo': '\ud83c\udf8d',
  'banana': '\ud83c\udf4c',
  'bangbang': '\u203c\ufe0f',
  'bangladesh': '\ud83c\udde7\ud83c\udde9',
  'banjo': '\ud83e\ude95',
  'bank': '\ud83c\udfe6',
  'bar_chart': '\ud83d\udcca',
  'barbados': '\ud83c\udde7\ud83c\udde7',
  'barber': '\ud83d\udc88',
  'baseball': '\u26be',
  'basket': '\ud83e\uddfa',
  'basketball': '\ud83c\udfc0',
  'basketball_man': '\u26f9\ufe0f\u200d\u2642\ufe0f',
  'basketball_woman': '\u26f9\ufe0f\u200d\u2640\ufe0f',
  'bat': '\ud83e\udd87',
  'bath': '\ud83d\udec0',
  'bathtub': '\ud83d\udec1',
  'battery': '\ud83d\udd0b',
  'beach_umbrella': '\ud83c\udfd6\ufe0f',
  'bear': '\ud83d\udc3b',
  'bearded_person': '\ud83e\uddd4',
  'bed': '\ud83d\udecf\ufe0f',
  'bee': '\ud83d\udc1d',
  'beer': '\ud83c\udf7a',
  'beers': '\ud83c\udf7b',
  'beetle': '\ud83d\udc1e',
  'beginner': '\ud83d\udd30',
  'belarus': '\ud83c\udde7\ud83c\uddfe',
  'belgium': '\ud83c\udde7\ud83c\uddea',
  'belize': '\ud83c\udde7\ud83c\uddff',
  'bell': '\ud83d\udd14',
  'bellhop_bell': '\ud83d\udece\ufe0f',
  'benin': '\ud83c\udde7\ud83c\uddef',
  'bento': '\ud83c\udf71',
  'bermuda': '\ud83c\udde7\ud83c\uddf2',
  'beverage_box': '\ud83e\uddc3',
  'bhutan': '\ud83c\udde7\ud83c\uddf9',
  'bicyclist': '\ud83d\udeb4',
  'bike': '\ud83d\udeb2',
  'biking_man': '\ud83d\udeb4\u200d\u2642\ufe0f',
  'biking_woman': '\ud83d\udeb4\u200d\u2640\ufe0f',
  'bikini': '\ud83d\udc59',
  'billed_cap': '\ud83e\udde2',
  'biohazard': '\u2623\ufe0f',
  'bird': '\ud83d\udc26',
  'birthday': '\ud83c\udf82',
  'black_circle': '\u26ab',
  'black_flag': '\ud83c\udff4',
  'black_heart': '\ud83d\udda4',
  'black_joker': '\ud83c\udccf',
  'black_large_square': '\u2b1b',
  'black_medium_small_square': '\u25fe',
  'black_medium_square': '\u25fc\ufe0f',
  'black_nib': '\u2712\ufe0f',
  'black_small_square': '\u25aa\ufe0f',
  'black_square_button': '\ud83d\udd32',
  'blond_haired_man': '\ud83d\udc71\u200d\u2642\ufe0f',
  'blond_haired_person': '\ud83d\udc71',
  'blond_haired_woman': '\ud83d\udc71\u200d\u2640\ufe0f',
  'blonde_woman': '\ud83d\udc71\u200d\u2640\ufe0f',
  'blossom': '\ud83c\udf3c',
  'blowfish': '\ud83d\udc21',
  'blue_book': '\ud83d\udcd8',
  'blue_car': '\ud83d\ude99',
  'blue_heart': '\ud83d\udc99',
  'blue_square': '\ud83d\udfe6',
  'blush': '\ud83d\ude0a',
  'boar': '\ud83d\udc17',
  'boat': '\u26f5',
  'bolivia': '\ud83c\udde7\ud83c\uddf4',
  'bomb': '\ud83d\udca3',
  'bone': '\ud83e\uddb4',
  'book': '\ud83d\udcd6',
  'bookmark': '\ud83d\udd16',
  'bookmark_tabs': '\ud83d\udcd1',
  'books': '\ud83d\udcda',
  'boom': '\ud83d\udca5',
  'boot': '\ud83d\udc62',
  'bosnia_herzegovina': '\ud83c\udde7\ud83c\udde6',
  'botswana': '\ud83c\udde7\ud83c\uddfc',
  'bouncing_ball_man': '\u26f9\ufe0f\u200d\u2642\ufe0f',
  'bouncing_ball_person': '\u26f9\ufe0f',
  'bouncing_ball_woman': '\u26f9\ufe0f\u200d\u2640\ufe0f',
  'bouquet': '\ud83d\udc90',
  'bouvet_island': '\ud83c\udde7\ud83c\uddfb',
  'bow': '\ud83d\ude47',
  'bow_and_arrow': '\ud83c\udff9',
  'bowing_man': '\ud83d\ude47\u200d\u2642\ufe0f',
  'bowing_woman': '\ud83d\ude47\u200d\u2640\ufe0f',
  'bowl_with_spoon': '\ud83e\udd63',
  'bowling': '\ud83c\udfb3',
  'boxing_glove': '\ud83e\udd4a',
  'boy': '\ud83d\udc66',
  'brain': '\ud83e\udde0',
  'brazil': '\ud83c\udde7\ud83c\uddf7',
  'bread': '\ud83c\udf5e',
  'breast_feeding': '\ud83e\udd31',
  'bricks': '\ud83e\uddf1',
  'bride_with_veil': '\ud83d\udc70',
  'bridge_at_night': '\ud83c\udf09',
  'briefcase': '\ud83d\udcbc',
  'british_indian_ocean_territory': '\ud83c\uddee\ud83c\uddf4',
  'british_virgin_islands': '\ud83c\uddfb\ud83c\uddec',
  'broccoli': '\ud83e\udd66',
  'broken_heart': '\ud83d\udc94',
  'broom': '\ud83e\uddf9',
  'brown_circle': '\ud83d\udfe4',
  'brown_heart': '\ud83e\udd0e',
  'brown_square': '\ud83d\udfeb',
  'brunei': '\ud83c\udde7\ud83c\uddf3',
  'bug': '\ud83d\udc1b',
  'building_construction': '\ud83c\udfd7\ufe0f',
  'bulb': '\ud83d\udca1',
  'bulgaria': '\ud83c\udde7\ud83c\uddec',
  'bullettrain_front': '\ud83d\ude85',
  'bullettrain_side': '\ud83d\ude84',
  'burkina_faso': '\ud83c\udde7\ud83c\uddeb',
  'burrito': '\ud83c\udf2f',
  'burundi': '\ud83c\udde7\ud83c\uddee',
  'bus': '\ud83d\ude8c',
  'business_suit_levitating': '\ud83d\udd74\ufe0f',
  'busstop': '\ud83d\ude8f',
  'bust_in_silhouette': '\ud83d\udc64',
  'busts_in_silhouette': '\ud83d\udc65',
  'butter': '\ud83e\uddc8',
  'butterfly': '\ud83e\udd8b',
  'cactus': '\ud83c\udf35',
  'cake': '\ud83c\udf70',
  'calendar': '\ud83d\udcc6',
  'call_me_hand': '\ud83e\udd19',
  'calling': '\ud83d\udcf2',
  'cambodia': '\ud83c\uddf0\ud83c\udded',
  'camel': '\ud83d\udc2b',
  'camera': '\ud83d\udcf7',
  'camera_flash': '\ud83d\udcf8',
  'cameroon': '\ud83c\udde8\ud83c\uddf2',
  'camping': '\ud83c\udfd5\ufe0f',
  'canada': '\ud83c\udde8\ud83c\udde6',
  'canary_islands': '\ud83c\uddee\ud83c\udde8',
  'cancer': '\u264b',
  'candle': '\ud83d\udd6f\ufe0f',
  'candy': '\ud83c\udf6c',
  'canned_food': '\ud83e\udd6b',
  'canoe': '\ud83d\udef6',
  'cape_verde': '\ud83c\udde8\ud83c\uddfb',
  'capital_abcd': '\ud83d\udd20',
  'capricorn': '\u2651',
  'car': '\ud83d\ude97',
  'card_file_box': '\ud83d\uddc3\ufe0f',
  'card_index': '\ud83d\udcc7',
  'card_index_dividers': '\ud83d\uddc2\ufe0f',
  'caribbean_netherlands': '\ud83c\udde7\ud83c\uddf6',
  'carousel_horse': '\ud83c\udfa0',
  'carrot': '\ud83e\udd55',
  'cartwheeling': '\ud83e\udd38',
  'cat': '\ud83d\udc31',
  'cat2': '\ud83d\udc08',
  'cayman_islands': '\ud83c\uddf0\ud83c\uddfe',
  'cd': '\ud83d\udcbf',
  'central_african_republic': '\ud83c\udde8\ud83c\uddeb',
  'ceuta_melilla': '\ud83c\uddea\ud83c\udde6',
  'chad': '\ud83c\uddf9\ud83c\udde9',
  'chains': '\u26d3\ufe0f',
  'chair': '\ud83e\ude91',
  'champagne': '\ud83c\udf7e',
  'chart': '\ud83d\udcb9',
  'chart_with_downwards_trend': '\ud83d\udcc9',
  'chart_with_upwards_trend': '\ud83d\udcc8',
  'checkered_flag': '\ud83c\udfc1',
  'cheese': '\ud83e\uddc0',
  'cherries': '\ud83c\udf52',
  'cherry_blossom': '\ud83c\udf38',
  'chess_pawn': '\u265f\ufe0f',
  'chestnut': '\ud83c\udf30',
  'chicken': '\ud83d\udc14',
  'child': '\ud83e\uddd2',
  'children_crossing': '\ud83d\udeb8',
  'chile': '\ud83c\udde8\ud83c\uddf1',
  'chipmunk': '\ud83d\udc3f\ufe0f',
  'chocolate_bar': '\ud83c\udf6b',
  'chopsticks': '\ud83e\udd62',
  'christmas_island': '\ud83c\udde8\ud83c\uddfd',
  'christmas_tree': '\ud83c\udf84',
  'church': '\u26ea',
  'cinema': '\ud83c\udfa6',
  'circus_tent': '\ud83c\udfaa',
  'city_sunrise': '\ud83c\udf07',
  'city_sunset': '\ud83c\udf06',
  'cityscape': '\ud83c\udfd9\ufe0f',
  'cl': '\ud83c\udd91',
  'clamp': '\ud83d\udddc\ufe0f',
  'clap': '\ud83d\udc4f',
  'clapper': '\ud83c\udfac',
  'classical_building': '\ud83c\udfdb\ufe0f',
  'climbing': '\ud83e\uddd7',
  'climbing_man': '\ud83e\uddd7\u200d\u2642\ufe0f',
  'climbing_woman': '\ud83e\uddd7\u200d\u2640\ufe0f',
  'clinking_glasses': '\ud83e\udd42',
  'clipboard': '\ud83d\udccb',
  'clipperton_island': '\ud83c\udde8\ud83c\uddf5',
  'clock1': '\ud83d\udd50',
  'clock10': '\ud83d\udd59',
  'clock1030': '\ud83d\udd65',
  'clock11': '\ud83d\udd5a',
  'clock1130': '\ud83d\udd66',
  'clock12': '\ud83d\udd5b',
  'clock1230': '\ud83d\udd67',
  'clock130': '\ud83d\udd5c',
  'clock2': '\ud83d\udd51',
  'clock230': '\ud83d\udd5d',
  'clock3': '\ud83d\udd52',
  'clock330': '\ud83d\udd5e',
  'clock4': '\ud83d\udd53',
  'clock430': '\ud83d\udd5f',
  'clock5': '\ud83d\udd54',
  'clock530': '\ud83d\udd60',
  'clock6': '\ud83d\udd55',
  'clock630': '\ud83d\udd61',
  'clock7': '\ud83d\udd56',
  'clock730': '\ud83d\udd62',
  'clock8': '\ud83d\udd57',
  'clock830': '\ud83d\udd63',
  'clock9': '\ud83d\udd58',
  'clock930': '\ud83d\udd64',
  'closed_book': '\ud83d\udcd5',
  'closed_lock_with_key': '\ud83d\udd10',
  'closed_umbrella': '\ud83c\udf02',
  'cloud': '\u2601\ufe0f',
  'cloud_with_lightning': '\ud83c\udf29\ufe0f',
  'cloud_with_lightning_and_rain': '\u26c8\ufe0f',
  'cloud_with_rain': '\ud83c\udf27\ufe0f',
  'cloud_with_snow': '\ud83c\udf28\ufe0f',
  'clown_face': '\ud83e\udd21',
  'clubs': '\u2663\ufe0f',
  'cn': '\ud83c\udde8\ud83c\uddf3',
  'coat': '\ud83e\udde5',
  'cocktail': '\ud83c\udf78',
  'coconut': '\ud83e\udd65',
  'cocos_islands': '\ud83c\udde8\ud83c\udde8',
  'coffee': '\u2615',
  'coffin': '\u26b0\ufe0f',
  'cold_face': '\ud83e\udd76',
  'cold_sweat': '\ud83d\ude30',
  'collision': '\ud83d\udca5',
  'colombia': '\ud83c\udde8\ud83c\uddf4',
  'comet': '\u2604\ufe0f',
  'comoros': '\ud83c\uddf0\ud83c\uddf2',
  'compass': '\ud83e\udded',
  'computer': '\ud83d\udcbb',
  'computer_mouse': '\ud83d\uddb1\ufe0f',
  'confetti_ball': '\ud83c\udf8a',
  'confounded': '\ud83d\ude16',
  'confused': '\ud83d\ude15',
  'congo_brazzaville': '\ud83c\udde8\ud83c\uddec',
  'congo_kinshasa': '\ud83c\udde8\ud83c\udde9',
  'congratulations': '\u3297\ufe0f',
  'construction': '\ud83d\udea7',
  'construction_worker': '\ud83d\udc77',
  'construction_worker_man': '\ud83d\udc77\u200d\u2642\ufe0f',
  'construction_worker_woman': '\ud83d\udc77\u200d\u2640\ufe0f',
  'control_knobs': '\ud83c\udf9b\ufe0f',
  'convenience_store': '\ud83c\udfea',
  'cook': '\ud83e\uddd1\u200d\ud83c\udf73',
  'cook_islands': '\ud83c\udde8\ud83c\uddf0',
  'cookie': '\ud83c\udf6a',
  'cool': '\ud83c\udd92',
  'cop': '\ud83d\udc6e',
  'copyright': '\u00a9\ufe0f',
  'corn': '\ud83c\udf3d',
  'costa_rica': '\ud83c\udde8\ud83c\uddf7',
  'cote_divoire': '\ud83c\udde8\ud83c\uddee',
  'couch_and_lamp': '\ud83d\udecb\ufe0f',
  'couple': '\ud83d\udc6b',
  'couple_with_heart': '\ud83d\udc91',
  'couple_with_heart_man_man': '\ud83d\udc68\u200d\u2764\ufe0f\u200d\ud83d\udc68',
  'couple_with_heart_woman_man': '\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc68',
  'couple_with_heart_woman_woman': '\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc69',
  'couplekiss': '\ud83d\udc8f',
  'couplekiss_man_man': '\ud83d\udc68\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc68',
  'couplekiss_man_woman': '\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc68',
  'couplekiss_woman_woman': '\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc69',
  'cow': '\ud83d\udc2e',
  'cow2': '\ud83d\udc04',
  'cowboy_hat_face': '\ud83e\udd20',
  'crab': '\ud83e\udd80',
  'crayon': '\ud83d\udd8d\ufe0f',
  'credit_card': '\ud83d\udcb3',
  'crescent_moon': '\ud83c\udf19',
  'cricket': '\ud83e\udd97',
  'cricket_game': '\ud83c\udfcf',
  'croatia': '\ud83c\udded\ud83c\uddf7',
  'crocodile': '\ud83d\udc0a',
  'croissant': '\ud83e\udd50',
  'crossed_fingers': '\ud83e\udd1e',
  'crossed_flags': '\ud83c\udf8c',
  'crossed_swords': '\u2694\ufe0f',
  'crown': '\ud83d\udc51',
  'cry': '\ud83d\ude22',
  'crying_cat_face': '\ud83d\ude3f',
  'crystal_ball': '\ud83d\udd2e',
  'cuba': '\ud83c\udde8\ud83c\uddfa',
  'cucumber': '\ud83e\udd52',
  'cup_with_straw': '\ud83e\udd64',
  'cupcake': '\ud83e\uddc1',
  'cupid': '\ud83d\udc98',
  'curacao': '\ud83c\udde8\ud83c\uddfc',
  'curling_stone': '\ud83e\udd4c',
  'curly_haired_man': '\ud83d\udc68\u200d\ud83e\uddb1',
  'curly_haired_woman': '\ud83d\udc69\u200d\ud83e\uddb1',
  'curly_loop': '\u27b0',
  'currency_exchange': '\ud83d\udcb1',
  'curry': '\ud83c\udf5b',
  'cursing_face': '\ud83e\udd2c',
  'custard': '\ud83c\udf6e',
  'customs': '\ud83d\udec3',
  'cut_of_meat': '\ud83e\udd69',
  'cyclone': '\ud83c\udf00',
  'cyprus': '\ud83c\udde8\ud83c\uddfe',
  'czech_republic': '\ud83c\udde8\ud83c\uddff',
  'dagger': '\ud83d\udde1\ufe0f',
  'dancer': '\ud83d\udc83',
  'dancers': '\ud83d\udc6f',
  'dancing_men': '\ud83d\udc6f\u200d\u2642\ufe0f',
  'dancing_women': '\ud83d\udc6f\u200d\u2640\ufe0f',
  'dango': '\ud83c\udf61',
  'dark_sunglasses': '\ud83d\udd76\ufe0f',
  'dart': '\ud83c\udfaf',
  'dash': '\ud83d\udca8',
  'date': '\ud83d\udcc5',
  'de': '\ud83c\udde9\ud83c\uddea',
  'deaf_man': '\ud83e\uddcf\u200d\u2642\ufe0f',
  'deaf_person': '\ud83e\uddcf',
  'deaf_woman': '\ud83e\uddcf\u200d\u2640\ufe0f',
  'deciduous_tree': '\ud83c\udf33',
  'deer': '\ud83e\udd8c',
  'denmark': '\ud83c\udde9\ud83c\uddf0',
  'department_store': '\ud83c\udfec',
  'derelict_house': '\ud83c\udfda\ufe0f',
  'desert': '\ud83c\udfdc\ufe0f',
  'desert_island': '\ud83c\udfdd\ufe0f',
  'desktop_computer': '\ud83d\udda5\ufe0f',
  'detective': '\ud83d\udd75\ufe0f',
  'diamond_shape_with_a_dot_inside': '\ud83d\udca0',
  'diamonds': '\u2666\ufe0f',
  'diego_garcia': '\ud83c\udde9\ud83c\uddec',
  'disappointed': '\ud83d\ude1e',
  'disappointed_relieved': '\ud83d\ude25',
  'diving_mask': '\ud83e\udd3f',
  'diya_lamp': '\ud83e\ude94',
  'dizzy': '\ud83d\udcab',
  'dizzy_face': '\ud83d\ude35',
  'djibouti': '\ud83c\udde9\ud83c\uddef',
  'dna': '\ud83e\uddec',
  'do_not_litter': '\ud83d\udeaf',
  'dog': '\ud83d\udc36',
  'dog2': '\ud83d\udc15',
  'dollar': '\ud83d\udcb5',
  'dolls': '\ud83c\udf8e',
  'dolphin': '\ud83d\udc2c',
  'dominica': '\ud83c\udde9\ud83c\uddf2',
  'dominican_republic': '\ud83c\udde9\ud83c\uddf4',
  'door': '\ud83d\udeaa',
  'doughnut': '\ud83c\udf69',
  'dove': '\ud83d\udd4a\ufe0f',
  'dragon': '\ud83d\udc09',
  'dragon_face': '\ud83d\udc32',
  'dress': '\ud83d\udc57',
  'dromedary_camel': '\ud83d\udc2a',
  'drooling_face': '\ud83e\udd24',
  'drop_of_blood': '\ud83e\ude78',
  'droplet': '\ud83d\udca7',
  'drum': '\ud83e\udd41',
  'duck': '\ud83e\udd86',
  'dumpling': '\ud83e\udd5f',
  'dvd': '\ud83d\udcc0',
  'e-mail': '\ud83d\udce7',
  'eagle': '\ud83e\udd85',
  'ear': '\ud83d\udc42',
  'ear_of_rice': '\ud83c\udf3e',
  'ear_with_hearing_aid': '\ud83e\uddbb',
  'earth_africa': '\ud83c\udf0d',
  'earth_americas': '\ud83c\udf0e',
  'earth_asia': '\ud83c\udf0f',
  'ecuador': '\ud83c\uddea\ud83c\udde8',
  'egg': '\ud83e\udd5a',
  'eggplant': '\ud83c\udf46',
  'egypt': '\ud83c\uddea\ud83c\uddec',
  'eight': '8\ufe0f\u20e3',
  'eight_pointed_black_star': '\u2734\ufe0f',
  'eight_spoked_asterisk': '\u2733\ufe0f',
  'eject_button': '\u23cf\ufe0f',
  'el_salvador': '\ud83c\uddf8\ud83c\uddfb',
  'electric_plug': '\ud83d\udd0c',
  'elephant': '\ud83d\udc18',
  'elf': '\ud83e\udddd',
  'elf_man': '\ud83e\udddd\u200d\u2642\ufe0f',
  'elf_woman': '\ud83e\udddd\u200d\u2640\ufe0f',
  'email': '\u2709\ufe0f',
  'end': '\ud83d\udd1a',
  'england': '\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f',
  'envelope': '\u2709\ufe0f',
  'envelope_with_arrow': '\ud83d\udce9',
  'equatorial_guinea': '\ud83c\uddec\ud83c\uddf6',
  'eritrea': '\ud83c\uddea\ud83c\uddf7',
  'es': '\ud83c\uddea\ud83c\uddf8',
  'estonia': '\ud83c\uddea\ud83c\uddea',
  'ethiopia': '\ud83c\uddea\ud83c\uddf9',
  'eu': '\ud83c\uddea\ud83c\uddfa',
  'euro': '\ud83d\udcb6',
  'european_castle': '\ud83c\udff0',
  'european_post_office': '\ud83c\udfe4',
  'european_union': '\ud83c\uddea\ud83c\uddfa',
  'evergreen_tree': '\ud83c\udf32',
  'exclamation': '\u2757',
  'exploding_head': '\ud83e\udd2f',
  'expressionless': '\ud83d\ude11',
  'eye': '\ud83d\udc41\ufe0f',
  'eye_speech_bubble': '\ud83d\udc41\ufe0f\u200d\ud83d\udde8\ufe0f',
  'eyeglasses': '\ud83d\udc53',
  'eyes': '\ud83d\udc40',
  'face_with_head_bandage': '\ud83e\udd15',
  'face_with_thermometer': '\ud83e\udd12',
  'facepalm': '\ud83e\udd26',
  'facepunch': '\ud83d\udc4a',
  'factory': '\ud83c\udfed',
  'factory_worker': '\ud83e\uddd1\u200d\ud83c\udfed',
  'fairy': '\ud83e\uddda',
  'fairy_man': '\ud83e\uddda\u200d\u2642\ufe0f',
  'fairy_woman': '\ud83e\uddda\u200d\u2640\ufe0f',
  'falafel': '\ud83e\uddc6',
  'falkland_islands': '\ud83c\uddeb\ud83c\uddf0',
  'fallen_leaf': '\ud83c\udf42',
  'family': '\ud83d\udc6a',
  'family_man_boy': '\ud83d\udc68\u200d\ud83d\udc66',
  'family_man_boy_boy': '\ud83d\udc68\u200d\ud83d\udc66\u200d\ud83d\udc66',
  'family_man_girl': '\ud83d\udc68\u200d\ud83d\udc67',
  'family_man_girl_boy': '\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc66',
  'family_man_girl_girl': '\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc67',
  'family_man_man_boy': '\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc66',
  'family_man_man_boy_boy': '\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc66\u200d\ud83d\udc66',
  'family_man_man_girl': '\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc67',
  'family_man_man_girl_boy': '\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc66',
  'family_man_man_girl_girl': '\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc67',
  'family_man_woman_boy': '\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc66',
  'family_man_woman_boy_boy': '\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66',
  'family_man_woman_girl': '\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67',
  'family_man_woman_girl_boy': '\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc66',
  'family_man_woman_girl_girl': '\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc67',
  'family_woman_boy': '\ud83d\udc69\u200d\ud83d\udc66',
  'family_woman_boy_boy': '\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66',
  'family_woman_girl': '\ud83d\udc69\u200d\ud83d\udc67',
  'family_woman_girl_boy': '\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc66',
  'family_woman_girl_girl': '\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc67',
  'family_woman_woman_boy': '\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc66',
  'family_woman_woman_boy_boy': '\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66',
  'family_woman_woman_girl': '\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc67',
  'family_woman_woman_girl_boy': '\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc66',
  'family_woman_woman_girl_girl': '\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc67',
  'farmer': '\ud83e\uddd1\u200d\ud83c\udf3e',
  'faroe_islands': '\ud83c\uddeb\ud83c\uddf4',
  'fast_forward': '\u23e9',
  'fax': '\ud83d\udce0',
  'fearful': '\ud83d\ude28',
  'feet': '\ud83d\udc3e',
  'female_detective': '\ud83d\udd75\ufe0f\u200d\u2640\ufe0f',
  'female_sign': '\u2640\ufe0f',
  'ferris_wheel': '\ud83c\udfa1',
  'ferry': '\u26f4\ufe0f',
  'field_hockey': '\ud83c\udfd1',
  'fiji': '\ud83c\uddeb\ud83c\uddef',
  'file_cabinet': '\ud83d\uddc4\ufe0f',
  'file_folder': '\ud83d\udcc1',
  'film_projector': '\ud83d\udcfd\ufe0f',
  'film_strip': '\ud83c\udf9e\ufe0f',
  'finland': '\ud83c\uddeb\ud83c\uddee',
  'fire': '\ud83d\udd25',
  'fire_engine': '\ud83d\ude92',
  'fire_extinguisher': '\ud83e\uddef',
  'firecracker': '\ud83e\udde8',
  'firefighter': '\ud83e\uddd1\u200d\ud83d\ude92',
  'fireworks': '\ud83c\udf86',
  'first_quarter_moon': '\ud83c\udf13',
  'first_quarter_moon_with_face': '\ud83c\udf1b',
  'fish': '\ud83d\udc1f',
  'fish_cake': '\ud83c\udf65',
  'fishing_pole_and_fish': '\ud83c\udfa3',
  'fist': '\u270a',
  'fist_left': '\ud83e\udd1b',
  'fist_oncoming': '\ud83d\udc4a',
  'fist_raised': '\u270a',
  'fist_right': '\ud83e\udd1c',
  'five': '5\ufe0f\u20e3',
  'flags': '\ud83c\udf8f',
  'flamingo': '\ud83e\udda9',
  'flashlight': '\ud83d\udd26',
  'flat_shoe': '\ud83e\udd7f',
  'fleur_de_lis': '\u269c\ufe0f',
  'flight_arrival': '\ud83d\udeec',
  'flight_departure': '\ud83d\udeeb',
  'flipper': '\ud83d\udc2c',
  'floppy_disk': '\ud83d\udcbe',
  'flower_playing_cards': '\ud83c\udfb4',
  'flushed': '\ud83d\ude33',
  'flying_disc': '\ud83e\udd4f',
  'flying_saucer': '\ud83d\udef8',
  'fog': '\ud83c\udf2b\ufe0f',
  'foggy': '\ud83c\udf01',
  'foot': '\ud83e\uddb6',
  'football': '\ud83c\udfc8',
  'footprints': '\ud83d\udc63',
  'fork_and_knife': '\ud83c\udf74',
  'fortune_cookie': '\ud83e\udd60',
  'fountain': '\u26f2',
  'fountain_pen': '\ud83d\udd8b\ufe0f',
  'four': '4\ufe0f\u20e3',
  'four_leaf_clover': '\ud83c\udf40',
  'fox_face': '\ud83e\udd8a',
  'fr': '\ud83c\uddeb\ud83c\uddf7',
  'framed_picture': '\ud83d\uddbc\ufe0f',
  'free': '\ud83c\udd93',
  'french_guiana': '\ud83c\uddec\ud83c\uddeb',
  'french_polynesia': '\ud83c\uddf5\ud83c\uddeb',
  'french_southern_territories': '\ud83c\uddf9\ud83c\uddeb',
  'fried_egg': '\ud83c\udf73',
  'fried_shrimp': '\ud83c\udf64',
  'fries': '\ud83c\udf5f',
  'frog': '\ud83d\udc38',
  'frowning': '\ud83d\ude26',
  'frowning_face': '\u2639\ufe0f',
  'frowning_man': '\ud83d\ude4d\u200d\u2642\ufe0f',
  'frowning_person': '\ud83d\ude4d',
  'frowning_woman': '\ud83d\ude4d\u200d\u2640\ufe0f',
  'fu': '\ud83d\udd95',
  'fuelpump': '\u26fd',
  'full_moon': '\ud83c\udf15',
  'full_moon_with_face': '\ud83c\udf1d',
  'funeral_urn': '\u26b1\ufe0f',
  'gabon': '\ud83c\uddec\ud83c\udde6',
  'gambia': '\ud83c\uddec\ud83c\uddf2',
  'game_die': '\ud83c\udfb2',
  'garlic': '\ud83e\uddc4',
  'gb': '\ud83c\uddec\ud83c\udde7',
  'gear': '\u2699\ufe0f',
  'gem': '\ud83d\udc8e',
  'gemini': '\u264a',
  'genie': '\ud83e\uddde',
  'genie_man': '\ud83e\uddde\u200d\u2642\ufe0f',
  'genie_woman': '\ud83e\uddde\u200d\u2640\ufe0f',
  'georgia': '\ud83c\uddec\ud83c\uddea',
  'ghana': '\ud83c\uddec\ud83c\udded',
  'ghost': '\ud83d\udc7b',
  'gibraltar': '\ud83c\uddec\ud83c\uddee',
  'gift': '\ud83c\udf81',
  'gift_heart': '\ud83d\udc9d',
  'giraffe': '\ud83e\udd92',
  'girl': '\ud83d\udc67',
  'globe_with_meridians': '\ud83c\udf10',
  'gloves': '\ud83e\udde4',
  'goal_net': '\ud83e\udd45',
  'goat': '\ud83d\udc10',
  'goggles': '\ud83e\udd7d',
  'golf': '\u26f3',
  'golfing': '\ud83c\udfcc\ufe0f',
  'golfing_man': '\ud83c\udfcc\ufe0f\u200d\u2642\ufe0f',
  'golfing_woman': '\ud83c\udfcc\ufe0f\u200d\u2640\ufe0f',
  'gorilla': '\ud83e\udd8d',
  'grapes': '\ud83c\udf47',
  'greece': '\ud83c\uddec\ud83c\uddf7',
  'green_apple': '\ud83c\udf4f',
  'green_book': '\ud83d\udcd7',
  'green_circle': '\ud83d\udfe2',
  'green_heart': '\ud83d\udc9a',
  'green_salad': '\ud83e\udd57',
  'green_square': '\ud83d\udfe9',
  'greenland': '\ud83c\uddec\ud83c\uddf1',
  'grenada': '\ud83c\uddec\ud83c\udde9',
  'grey_exclamation': '\u2755',
  'grey_question': '\u2754',
  'grimacing': '\ud83d\ude2c',
  'grin': '\ud83d\ude01',
  'grinning': '\ud83d\ude00',
  'guadeloupe': '\ud83c\uddec\ud83c\uddf5',
  'guam': '\ud83c\uddec\ud83c\uddfa',
  'guard': '\ud83d\udc82',
  'guardsman': '\ud83d\udc82\u200d\u2642\ufe0f',
  'guardswoman': '\ud83d\udc82\u200d\u2640\ufe0f',
  'guatemala': '\ud83c\uddec\ud83c\uddf9',
  'guernsey': '\ud83c\uddec\ud83c\uddec',
  'guide_dog': '\ud83e\uddae',
  'guinea': '\ud83c\uddec\ud83c\uddf3',
  'guinea_bissau': '\ud83c\uddec\ud83c\uddfc',
  'guitar': '\ud83c\udfb8',
  'gun': '\ud83d\udd2b',
  'guyana': '\ud83c\uddec\ud83c\uddfe',
  'haircut': '\ud83d\udc87',
  'haircut_man': '\ud83d\udc87\u200d\u2642\ufe0f',
  'haircut_woman': '\ud83d\udc87\u200d\u2640\ufe0f',
  'haiti': '\ud83c\udded\ud83c\uddf9',
  'hamburger': '\ud83c\udf54',
  'hammer': '\ud83d\udd28',
  'hammer_and_pick': '\u2692\ufe0f',
  'hammer_and_wrench': '\ud83d\udee0\ufe0f',
  'hamster': '\ud83d\udc39',
  'hand': '\u270b',
  'hand_over_mouth': '\ud83e\udd2d',
  'handbag': '\ud83d\udc5c',
  'handball_person': '\ud83e\udd3e',
  'handshake': '\ud83e\udd1d',
  'hankey': '\ud83d\udca9',
  'hash': '#\ufe0f\u20e3',
  'hatched_chick': '\ud83d\udc25',
  'hatching_chick': '\ud83d\udc23',
  'headphones': '\ud83c\udfa7',
  'health_worker': '\ud83e\uddd1\u200d\u2695\ufe0f',
  'hear_no_evil': '\ud83d\ude49',
  'heard_mcdonald_islands': '\ud83c\udded\ud83c\uddf2',
  'heart': '\u2764\ufe0f',
  'heart_decoration': '\ud83d\udc9f',
  'heart_eyes': '\ud83d\ude0d',
  'heart_eyes_cat': '\ud83d\ude3b',
  'heartbeat': '\ud83d\udc93',
  'heartpulse': '\ud83d\udc97',
  'hearts': '\u2665\ufe0f',
  'heavy_check_mark': '\u2714\ufe0f',
  'heavy_division_sign': '\u2797',
  'heavy_dollar_sign': '\ud83d\udcb2',
  'heavy_exclamation_mark': '\u2757',
  'heavy_heart_exclamation': '\u2763\ufe0f',
  'heavy_minus_sign': '\u2796',
  'heavy_multiplication_x': '\u2716\ufe0f',
  'heavy_plus_sign': '\u2795',
  'hedgehog': '\ud83e\udd94',
  'helicopter': '\ud83d\ude81',
  'herb': '\ud83c\udf3f',
  'hibiscus': '\ud83c\udf3a',
  'high_brightness': '\ud83d\udd06',
  'high_heel': '\ud83d\udc60',
  'hiking_boot': '\ud83e\udd7e',
  'hindu_temple': '\ud83d\uded5',
  'hippopotamus': '\ud83e\udd9b',
  'hocho': '\ud83d\udd2a',
  'hole': '\ud83d\udd73\ufe0f',
  'honduras': '\ud83c\udded\ud83c\uddf3',
  'honey_pot': '\ud83c\udf6f',
  'honeybee': '\ud83d\udc1d',
  'hong_kong': '\ud83c\udded\ud83c\uddf0',
  'horse': '\ud83d\udc34',
  'horse_racing': '\ud83c\udfc7',
  'hospital': '\ud83c\udfe5',
  'hot_face': '\ud83e\udd75',
  'hot_pepper': '\ud83c\udf36\ufe0f',
  'hotdog': '\ud83c\udf2d',
  'hotel': '\ud83c\udfe8',
  'hotsprings': '\u2668\ufe0f',
  'hourglass': '\u231b',
  'hourglass_flowing_sand': '\u23f3',
  'house': '\ud83c\udfe0',
  'house_with_garden': '\ud83c\udfe1',
  'houses': '\ud83c\udfd8\ufe0f',
  'hugs': '\ud83e\udd17',
  'hungary': '\ud83c\udded\ud83c\uddfa',
  'hushed': '\ud83d\ude2f',
  'ice_cream': '\ud83c\udf68',
  'ice_cube': '\ud83e\uddca',
  'ice_hockey': '\ud83c\udfd2',
  'ice_skate': '\u26f8\ufe0f',
  'icecream': '\ud83c\udf66',
  'iceland': '\ud83c\uddee\ud83c\uddf8',
  'id': '\ud83c\udd94',
  'ideograph_advantage': '\ud83c\ude50',
  'imp': '\ud83d\udc7f',
  'inbox_tray': '\ud83d\udce5',
  'incoming_envelope': '\ud83d\udce8',
  'india': '\ud83c\uddee\ud83c\uddf3',
  'indonesia': '\ud83c\uddee\ud83c\udde9',
  'infinity': '\u267e\ufe0f',
  'information_desk_person': '\ud83d\udc81',
  'information_source': '\u2139\ufe0f',
  'innocent': '\ud83d\ude07',
  'interrobang': '\u2049\ufe0f',
  'iphone': '\ud83d\udcf1',
  'iran': '\ud83c\uddee\ud83c\uddf7',
  'iraq': '\ud83c\uddee\ud83c\uddf6',
  'ireland': '\ud83c\uddee\ud83c\uddea',
  'isle_of_man': '\ud83c\uddee\ud83c\uddf2',
  'israel': '\ud83c\uddee\ud83c\uddf1',
  'it': '\ud83c\uddee\ud83c\uddf9',
  'izakaya_lantern': '\ud83c\udfee',
  'jack_o_lantern': '\ud83c\udf83',
  'jamaica': '\ud83c\uddef\ud83c\uddf2',
  'japan': '\ud83d\uddfe',
  'japanese_castle': '\ud83c\udfef',
  'japanese_goblin': '\ud83d\udc7a',
  'japanese_ogre': '\ud83d\udc79',
  'jeans': '\ud83d\udc56',
  'jersey': '\ud83c\uddef\ud83c\uddea',
  'jigsaw': '\ud83e\udde9',
  'jordan': '\ud83c\uddef\ud83c\uddf4',
  'joy': '\ud83d\ude02',
  'joy_cat': '\ud83d\ude39',
  'joystick': '\ud83d\udd79\ufe0f',
  'jp': '\ud83c\uddef\ud83c\uddf5',
  'judge': '\ud83e\uddd1\u200d\u2696\ufe0f',
  'juggling_person': '\ud83e\udd39',
  'kaaba': '\ud83d\udd4b',
  'kangaroo': '\ud83e\udd98',
  'kazakhstan': '\ud83c\uddf0\ud83c\uddff',
  'kenya': '\ud83c\uddf0\ud83c\uddea',
  'key': '\ud83d\udd11',
  'keyboard': '\u2328\ufe0f',
  'keycap_ten': '\ud83d\udd1f',
  'kick_scooter': '\ud83d\udef4',
  'kimono': '\ud83d\udc58',
  'kiribati': '\ud83c\uddf0\ud83c\uddee',
  'kiss': '\ud83d\udc8b',
  'kissing': '\ud83d\ude17',
  'kissing_cat': '\ud83d\ude3d',
  'kissing_closed_eyes': '\ud83d\ude1a',
  'kissing_heart': '\ud83d\ude18',
  'kissing_smiling_eyes': '\ud83d\ude19',
  'kite': '\ud83e\ude81',
  'kiwi_fruit': '\ud83e\udd5d',
  'kneeling_man': '\ud83e\uddce\u200d\u2642\ufe0f',
  'kneeling_person': '\ud83e\uddce',
  'kneeling_woman': '\ud83e\uddce\u200d\u2640\ufe0f',
  'knife': '\ud83d\udd2a',
  'koala': '\ud83d\udc28',
  'koko': '\ud83c\ude01',
  'kosovo': '\ud83c\uddfd\ud83c\uddf0',
  'kr': '\ud83c\uddf0\ud83c\uddf7',
  'kuwait': '\ud83c\uddf0\ud83c\uddfc',
  'kyrgyzstan': '\ud83c\uddf0\ud83c\uddec',
  'lab_coat': '\ud83e\udd7c',
  'label': '\ud83c\udff7\ufe0f',
  'lacrosse': '\ud83e\udd4d',
  'lantern': '\ud83c\udfee',
  'laos': '\ud83c\uddf1\ud83c\udde6',
  'large_blue_circle': '\ud83d\udd35',
  'large_blue_diamond': '\ud83d\udd37',
  'large_orange_diamond': '\ud83d\udd36',
  'last_quarter_moon': '\ud83c\udf17',
  'last_quarter_moon_with_face': '\ud83c\udf1c',
  'latin_cross': '\u271d\ufe0f',
  'latvia': '\ud83c\uddf1\ud83c\uddfb',
  'laughing': '\ud83d\ude06',
  'leafy_green': '\ud83e\udd6c',
  'leaves': '\ud83c\udf43',
  'lebanon': '\ud83c\uddf1\ud83c\udde7',
  'ledger': '\ud83d\udcd2',
  'left_luggage': '\ud83d\udec5',
  'left_right_arrow': '\u2194\ufe0f',
  'left_speech_bubble': '\ud83d\udde8\ufe0f',
  'leftwards_arrow_with_hook': '\u21a9\ufe0f',
  'leg': '\ud83e\uddb5',
  'lemon': '\ud83c\udf4b',
  'leo': '\u264c',
  'leopard': '\ud83d\udc06',
  'lesotho': '\ud83c\uddf1\ud83c\uddf8',
  'level_slider': '\ud83c\udf9a\ufe0f',
  'liberia': '\ud83c\uddf1\ud83c\uddf7',
  'libra': '\u264e',
  'libya': '\ud83c\uddf1\ud83c\uddfe',
  'liechtenstein': '\ud83c\uddf1\ud83c\uddee',
  'light_rail': '\ud83d\ude88',
  'link': '\ud83d\udd17',
  'lion': '\ud83e\udd81',
  'lips': '\ud83d\udc44',
  'lipstick': '\ud83d\udc84',
  'lithuania': '\ud83c\uddf1\ud83c\uddf9',
  'lizard': '\ud83e\udd8e',
  'llama': '\ud83e\udd99',
  'lobster': '\ud83e\udd9e',
  'lock': '\ud83d\udd12',
  'lock_with_ink_pen': '\ud83d\udd0f',
  'lollipop': '\ud83c\udf6d',
  'loop': '\u27bf',
  'lotion_bottle': '\ud83e\uddf4',
  'lotus_position': '\ud83e\uddd8',
  'lotus_position_man': '\ud83e\uddd8\u200d\u2642\ufe0f',
  'lotus_position_woman': '\ud83e\uddd8\u200d\u2640\ufe0f',
  'loud_sound': '\ud83d\udd0a',
  'loudspeaker': '\ud83d\udce2',
  'love_hotel': '\ud83c\udfe9',
  'love_letter': '\ud83d\udc8c',
  'love_you_gesture': '\ud83e\udd1f',
  'low_brightness': '\ud83d\udd05',
  'luggage': '\ud83e\uddf3',
  'luxembourg': '\ud83c\uddf1\ud83c\uddfa',
  'lying_face': '\ud83e\udd25',
  'm': '\u24c2\ufe0f',
  'macau': '\ud83c\uddf2\ud83c\uddf4',
  'macedonia': '\ud83c\uddf2\ud83c\uddf0',
  'madagascar': '\ud83c\uddf2\ud83c\uddec',
  'mag': '\ud83d\udd0d',
  'mag_right': '\ud83d\udd0e',
  'mage': '\ud83e\uddd9',
  'mage_man': '\ud83e\uddd9\u200d\u2642\ufe0f',
  'mage_woman': '\ud83e\uddd9\u200d\u2640\ufe0f',
  'magnet': '\ud83e\uddf2',
  'mahjong': '\ud83c\udc04',
  'mailbox': '\ud83d\udceb',
  'mailbox_closed': '\ud83d\udcea',
  'mailbox_with_mail': '\ud83d\udcec',
  'mailbox_with_no_mail': '\ud83d\udced',
  'malawi': '\ud83c\uddf2\ud83c\uddfc',
  'malaysia': '\ud83c\uddf2\ud83c\uddfe',
  'maldives': '\ud83c\uddf2\ud83c\uddfb',
  'male_detective': '\ud83d\udd75\ufe0f\u200d\u2642\ufe0f',
  'male_sign': '\u2642\ufe0f',
  'mali': '\ud83c\uddf2\ud83c\uddf1',
  'malta': '\ud83c\uddf2\ud83c\uddf9',
  'man': '\ud83d\udc68',
  'man_artist': '\ud83d\udc68\u200d\ud83c\udfa8',
  'man_astronaut': '\ud83d\udc68\u200d\ud83d\ude80',
  'man_cartwheeling': '\ud83e\udd38\u200d\u2642\ufe0f',
  'man_cook': '\ud83d\udc68\u200d\ud83c\udf73',
  'man_dancing': '\ud83d\udd7a',
  'man_facepalming': '\ud83e\udd26\u200d\u2642\ufe0f',
  'man_factory_worker': '\ud83d\udc68\u200d\ud83c\udfed',
  'man_farmer': '\ud83d\udc68\u200d\ud83c\udf3e',
  'man_firefighter': '\ud83d\udc68\u200d\ud83d\ude92',
  'man_health_worker': '\ud83d\udc68\u200d\u2695\ufe0f',
  'man_in_manual_wheelchair': '\ud83d\udc68\u200d\ud83e\uddbd',
  'man_in_motorized_wheelchair': '\ud83d\udc68\u200d\ud83e\uddbc',
  'man_in_tuxedo': '\ud83e\udd35',
  'man_judge': '\ud83d\udc68\u200d\u2696\ufe0f',
  'man_juggling': '\ud83e\udd39\u200d\u2642\ufe0f',
  'man_mechanic': '\ud83d\udc68\u200d\ud83d\udd27',
  'man_office_worker': '\ud83d\udc68\u200d\ud83d\udcbc',
  'man_pilot': '\ud83d\udc68\u200d\u2708\ufe0f',
  'man_playing_handball': '\ud83e\udd3e\u200d\u2642\ufe0f',
  'man_playing_water_polo': '\ud83e\udd3d\u200d\u2642\ufe0f',
  'man_scientist': '\ud83d\udc68\u200d\ud83d\udd2c',
  'man_shrugging': '\ud83e\udd37\u200d\u2642\ufe0f',
  'man_singer': '\ud83d\udc68\u200d\ud83c\udfa4',
  'man_student': '\ud83d\udc68\u200d\ud83c\udf93',
  'man_teacher': '\ud83d\udc68\u200d\ud83c\udfeb',
  'man_technologist': '\ud83d\udc68\u200d\ud83d\udcbb',
  'man_with_gua_pi_mao': '\ud83d\udc72',
  'man_with_probing_cane': '\ud83d\udc68\u200d\ud83e\uddaf',
  'man_with_turban': '\ud83d\udc73\u200d\u2642\ufe0f',
  'mandarin': '\ud83c\udf4a',
  'mango': '\ud83e\udd6d',
  'mans_shoe': '\ud83d\udc5e',
  'mantelpiece_clock': '\ud83d\udd70\ufe0f',
  'manual_wheelchair': '\ud83e\uddbd',
  'maple_leaf': '\ud83c\udf41',
  'marshall_islands': '\ud83c\uddf2\ud83c\udded',
  'martial_arts_uniform': '\ud83e\udd4b',
  'martinique': '\ud83c\uddf2\ud83c\uddf6',
  'mask': '\ud83d\ude37',
  'massage': '\ud83d\udc86',
  'massage_man': '\ud83d\udc86\u200d\u2642\ufe0f',
  'massage_woman': '\ud83d\udc86\u200d\u2640\ufe0f',
  'mate': '\ud83e\uddc9',
  'mauritania': '\ud83c\uddf2\ud83c\uddf7',
  'mauritius': '\ud83c\uddf2\ud83c\uddfa',
  'mayotte': '\ud83c\uddfe\ud83c\uddf9',
  'meat_on_bone': '\ud83c\udf56',
  'mechanic': '\ud83e\uddd1\u200d\ud83d\udd27',
  'mechanical_arm': '\ud83e\uddbe',
  'mechanical_leg': '\ud83e\uddbf',
  'medal_military': '\ud83c\udf96\ufe0f',
  'medal_sports': '\ud83c\udfc5',
  'medical_symbol': '\u2695\ufe0f',
  'mega': '\ud83d\udce3',
  'melon': '\ud83c\udf48',
  'memo': '\ud83d\udcdd',
  'men_wrestling': '\ud83e\udd3c\u200d\u2642\ufe0f',
  'menorah': '\ud83d\udd4e',
  'mens': '\ud83d\udeb9',
  'mermaid': '\ud83e\udddc\u200d\u2640\ufe0f',
  'merman': '\ud83e\udddc\u200d\u2642\ufe0f',
  'merperson': '\ud83e\udddc',
  'metal': '\ud83e\udd18',
  'metro': '\ud83d\ude87',
  'mexico': '\ud83c\uddf2\ud83c\uddfd',
  'microbe': '\ud83e\udda0',
  'micronesia': '\ud83c\uddeb\ud83c\uddf2',
  'microphone': '\ud83c\udfa4',
  'microscope': '\ud83d\udd2c',
  'middle_finger': '\ud83d\udd95',
  'milk_glass': '\ud83e\udd5b',
  'milky_way': '\ud83c\udf0c',
  'minibus': '\ud83d\ude90',
  'minidisc': '\ud83d\udcbd',
  'mobile_phone_off': '\ud83d\udcf4',
  'moldova': '\ud83c\uddf2\ud83c\udde9',
  'monaco': '\ud83c\uddf2\ud83c\udde8',
  'money_mouth_face': '\ud83e\udd11',
  'money_with_wings': '\ud83d\udcb8',
  'moneybag': '\ud83d\udcb0',
  'mongolia': '\ud83c\uddf2\ud83c\uddf3',
  'monkey': '\ud83d\udc12',
  'monkey_face': '\ud83d\udc35',
  'monocle_face': '\ud83e\uddd0',
  'monorail': '\ud83d\ude9d',
  'montenegro': '\ud83c\uddf2\ud83c\uddea',
  'montserrat': '\ud83c\uddf2\ud83c\uddf8',
  'moon': '\ud83c\udf14',
  'moon_cake': '\ud83e\udd6e',
  'morocco': '\ud83c\uddf2\ud83c\udde6',
  'mortar_board': '\ud83c\udf93',
  'mosque': '\ud83d\udd4c',
  'mosquito': '\ud83e\udd9f',
  'motor_boat': '\ud83d\udee5\ufe0f',
  'motor_scooter': '\ud83d\udef5',
  'motorcycle': '\ud83c\udfcd\ufe0f',
  'motorized_wheelchair': '\ud83e\uddbc',
  'motorway': '\ud83d\udee3\ufe0f',
  'mount_fuji': '\ud83d\uddfb',
  'mountain': '\u26f0\ufe0f',
  'mountain_bicyclist': '\ud83d\udeb5',
  'mountain_biking_man': '\ud83d\udeb5\u200d\u2642\ufe0f',
  'mountain_biking_woman': '\ud83d\udeb5\u200d\u2640\ufe0f',
  'mountain_cableway': '\ud83d\udea0',
  'mountain_railway': '\ud83d\ude9e',
  'mountain_snow': '\ud83c\udfd4\ufe0f',
  'mouse': '\ud83d\udc2d',
  'mouse2': '\ud83d\udc01',
  'movie_camera': '\ud83c\udfa5',
  'moyai': '\ud83d\uddff',
  'mozambique': '\ud83c\uddf2\ud83c\uddff',
  'mrs_claus': '\ud83e\udd36',
  'muscle': '\ud83d\udcaa',
  'mushroom': '\ud83c\udf44',
  'musical_keyboard': '\ud83c\udfb9',
  'musical_note': '\ud83c\udfb5',
  'musical_score': '\ud83c\udfbc',
  'mute': '\ud83d\udd07',
  'myanmar': '\ud83c\uddf2\ud83c\uddf2',
  'nail_care': '\ud83d\udc85',
  'name_badge': '\ud83d\udcdb',
  'namibia': '\ud83c\uddf3\ud83c\udde6',
  'national_park': '\ud83c\udfde\ufe0f',
  'nauru': '\ud83c\uddf3\ud83c\uddf7',
  'nauseated_face': '\ud83e\udd22',
  'nazar_amulet': '\ud83e\uddff',
  'necktie': '\ud83d\udc54',
  'negative_squared_cross_mark': '\u274e',
  'nepal': '\ud83c\uddf3\ud83c\uddf5',
  'nerd_face': '\ud83e\udd13',
  'netherlands': '\ud83c\uddf3\ud83c\uddf1',
  'neutral_face': '\ud83d\ude10',
  'new': '\ud83c\udd95',
  'new_caledonia': '\ud83c\uddf3\ud83c\udde8',
  'new_moon': '\ud83c\udf11',
  'new_moon_with_face': '\ud83c\udf1a',
  'new_zealand': '\ud83c\uddf3\ud83c\uddff',
  'newspaper': '\ud83d\udcf0',
  'newspaper_roll': '\ud83d\uddde\ufe0f',
  'next_track_button': '\u23ed\ufe0f',
  'ng': '\ud83c\udd96',
  'ng_man': '\ud83d\ude45\u200d\u2642\ufe0f',
  'ng_woman': '\ud83d\ude45\u200d\u2640\ufe0f',
  'nicaragua': '\ud83c\uddf3\ud83c\uddee',
  'niger': '\ud83c\uddf3\ud83c\uddea',
  'nigeria': '\ud83c\uddf3\ud83c\uddec',
  'night_with_stars': '\ud83c\udf03',
  'nine': '9\ufe0f\u20e3',
  'niue': '\ud83c\uddf3\ud83c\uddfa',
  'no_bell': '\ud83d\udd15',
  'no_bicycles': '\ud83d\udeb3',
  'no_entry': '\u26d4',
  'no_entry_sign': '\ud83d\udeab',
  'no_good': '\ud83d\ude45',
  'no_good_man': '\ud83d\ude45\u200d\u2642\ufe0f',
  'no_good_woman': '\ud83d\ude45\u200d\u2640\ufe0f',
  'no_mobile_phones': '\ud83d\udcf5',
  'no_mouth': '\ud83d\ude36',
  'no_pedestrians': '\ud83d\udeb7',
  'no_smoking': '\ud83d\udead',
  'non-potable_water': '\ud83d\udeb1',
  'norfolk_island': '\ud83c\uddf3\ud83c\uddeb',
  'north_korea': '\ud83c\uddf0\ud83c\uddf5',
  'northern_mariana_islands': '\ud83c\uddf2\ud83c\uddf5',
  'norway': '\ud83c\uddf3\ud83c\uddf4',
  'nose': '\ud83d\udc43',
  'notebook': '\ud83d\udcd3',
  'notebook_with_decorative_cover': '\ud83d\udcd4',
  'notes': '\ud83c\udfb6',
  'nut_and_bolt': '\ud83d\udd29',
  'o': '\u2b55',
  'o2': '\ud83c\udd7e\ufe0f',
  'ocean': '\ud83c\udf0a',
  'octopus': '\ud83d\udc19',
  'oden': '\ud83c\udf62',
  'office': '\ud83c\udfe2',
  'office_worker': '\ud83e\uddd1\u200d\ud83d\udcbc',
  'oil_drum': '\ud83d\udee2\ufe0f',
  'ok': '\ud83c\udd97',
  'ok_hand': '\ud83d\udc4c',
  'ok_man': '\ud83d\ude46\u200d\u2642\ufe0f',
  'ok_person': '\ud83d\ude46',
  'ok_woman': '\ud83d\ude46\u200d\u2640\ufe0f',
  'old_key': '\ud83d\udddd\ufe0f',
  'older_adult': '\ud83e\uddd3',
  'older_man': '\ud83d\udc74',
  'older_woman': '\ud83d\udc75',
  'om': '\ud83d\udd49\ufe0f',
  'oman': '\ud83c\uddf4\ud83c\uddf2',
  'on': '\ud83d\udd1b',
  'oncoming_automobile': '\ud83d\ude98',
  'oncoming_bus': '\ud83d\ude8d',
  'oncoming_police_car': '\ud83d\ude94',
  'oncoming_taxi': '\ud83d\ude96',
  'one': '1\ufe0f\u20e3',
  'one_piece_swimsuit': '\ud83e\ude71',
  'onion': '\ud83e\uddc5',
  'open_book': '\ud83d\udcd6',
  'open_file_folder': '\ud83d\udcc2',
  'open_hands': '\ud83d\udc50',
  'open_mouth': '\ud83d\ude2e',
  'open_umbrella': '\u2602\ufe0f',
  'ophiuchus': '\u26ce',
  'orange': '\ud83c\udf4a',
  'orange_book': '\ud83d\udcd9',
  'orange_circle': '\ud83d\udfe0',
  'orange_heart': '\ud83e\udde1',
  'orange_square': '\ud83d\udfe7',
  'orangutan': '\ud83e\udda7',
  'orthodox_cross': '\u2626\ufe0f',
  'otter': '\ud83e\udda6',
  'outbox_tray': '\ud83d\udce4',
  'owl': '\ud83e\udd89',
  'ox': '\ud83d\udc02',
  'oyster': '\ud83e\uddaa',
  'package': '\ud83d\udce6',
  'page_facing_up': '\ud83d\udcc4',
  'page_with_curl': '\ud83d\udcc3',
  'pager': '\ud83d\udcdf',
  'paintbrush': '\ud83d\udd8c\ufe0f',
  'pakistan': '\ud83c\uddf5\ud83c\uddf0',
  'palau': '\ud83c\uddf5\ud83c\uddfc',
  'palestinian_territories': '\ud83c\uddf5\ud83c\uddf8',
  'palm_tree': '\ud83c\udf34',
  'palms_up_together': '\ud83e\udd32',
  'panama': '\ud83c\uddf5\ud83c\udde6',
  'pancakes': '\ud83e\udd5e',
  'panda_face': '\ud83d\udc3c',
  'paperclip': '\ud83d\udcce',
  'paperclips': '\ud83d\udd87\ufe0f',
  'papua_new_guinea': '\ud83c\uddf5\ud83c\uddec',
  'parachute': '\ud83e\ude82',
  'paraguay': '\ud83c\uddf5\ud83c\uddfe',
  'parasol_on_ground': '\u26f1\ufe0f',
  'parking': '\ud83c\udd7f\ufe0f',
  'parrot': '\ud83e\udd9c',
  'part_alternation_mark': '\u303d\ufe0f',
  'partly_sunny': '\u26c5',
  'partying_face': '\ud83e\udd73',
  'passenger_ship': '\ud83d\udef3\ufe0f',
  'passport_control': '\ud83d\udec2',
  'pause_button': '\u23f8\ufe0f',
  'paw_prints': '\ud83d\udc3e',
  'peace_symbol': '\u262e\ufe0f',
  'peach': '\ud83c\udf51',
  'peacock': '\ud83e\udd9a',
  'peanuts': '\ud83e\udd5c',
  'pear': '\ud83c\udf50',
  'pen': '\ud83d\udd8a\ufe0f',
  'pencil': '\ud83d\udcdd',
  'pencil2': '\u270f\ufe0f',
  'penguin': '\ud83d\udc27',
  'pensive': '\ud83d\ude14',
  'people_holding_hands': '\ud83e\uddd1\u200d\ud83e\udd1d\u200d\ud83e\uddd1',
  'performing_arts': '\ud83c\udfad',
  'persevere': '\ud83d\ude23',
  'person_bald': '\ud83e\uddd1\u200d\ud83e\uddb2',
  'person_curly_hair': '\ud83e\uddd1\u200d\ud83e\uddb1',
  'person_fencing': '\ud83e\udd3a',
  'person_in_manual_wheelchair': '\ud83e\uddd1\u200d\ud83e\uddbd',
  'person_in_motorized_wheelchair': '\ud83e\uddd1\u200d\ud83e\uddbc',
  'person_red_hair': '\ud83e\uddd1\u200d\ud83e\uddb0',
  'person_white_hair': '\ud83e\uddd1\u200d\ud83e\uddb3',
  'person_with_probing_cane': '\ud83e\uddd1\u200d\ud83e\uddaf',
  'person_with_turban': '\ud83d\udc73',
  'peru': '\ud83c\uddf5\ud83c\uddea',
  'petri_dish': '\ud83e\uddeb',
  'philippines': '\ud83c\uddf5\ud83c\udded',
  'phone': '\u260e\ufe0f',
  'pick': '\u26cf\ufe0f',
  'pie': '\ud83e\udd67',
  'pig': '\ud83d\udc37',
  'pig2': '\ud83d\udc16',
  'pig_nose': '\ud83d\udc3d',
  'pill': '\ud83d\udc8a',
  'pilot': '\ud83e\uddd1\u200d\u2708\ufe0f',
  'pinching_hand': '\ud83e\udd0f',
  'pineapple': '\ud83c\udf4d',
  'ping_pong': '\ud83c\udfd3',
  'pirate_flag': '\ud83c\udff4\u200d\u2620\ufe0f',
  'pisces': '\u2653',
  'pitcairn_islands': '\ud83c\uddf5\ud83c\uddf3',
  'pizza': '\ud83c\udf55',
  'place_of_worship': '\ud83d\uded0',
  'plate_with_cutlery': '\ud83c\udf7d\ufe0f',
  'play_or_pause_button': '\u23ef\ufe0f',
  'pleading_face': '\ud83e\udd7a',
  'point_down': '\ud83d\udc47',
  'point_left': '\ud83d\udc48',
  'point_right': '\ud83d\udc49',
  'point_up': '\u261d\ufe0f',
  'point_up_2': '\ud83d\udc46',
  'poland': '\ud83c\uddf5\ud83c\uddf1',
  'police_car': '\ud83d\ude93',
  'police_officer': '\ud83d\udc6e',
  'policeman': '\ud83d\udc6e\u200d\u2642\ufe0f',
  'policewoman': '\ud83d\udc6e\u200d\u2640\ufe0f',
  'poodle': '\ud83d\udc29',
  'poop': '\ud83d\udca9',
  'popcorn': '\ud83c\udf7f',
  'portugal': '\ud83c\uddf5\ud83c\uddf9',
  'post_office': '\ud83c\udfe3',
  'postal_horn': '\ud83d\udcef',
  'postbox': '\ud83d\udcee',
  'potable_water': '\ud83d\udeb0',
  'potato': '\ud83e\udd54',
  'pouch': '\ud83d\udc5d',
  'poultry_leg': '\ud83c\udf57',
  'pound': '\ud83d\udcb7',
  'pout': '\ud83d\ude21',
  'pouting_cat': '\ud83d\ude3e',
  'pouting_face': '\ud83d\ude4e',
  'pouting_man': '\ud83d\ude4e\u200d\u2642\ufe0f',
  'pouting_woman': '\ud83d\ude4e\u200d\u2640\ufe0f',
  'pray': '\ud83d\ude4f',
  'prayer_beads': '\ud83d\udcff',
  'pregnant_woman': '\ud83e\udd30',
  'pretzel': '\ud83e\udd68',
  'previous_track_button': '\u23ee\ufe0f',
  'prince': '\ud83e\udd34',
  'princess': '\ud83d\udc78',
  'printer': '\ud83d\udda8\ufe0f',
  'probing_cane': '\ud83e\uddaf',
  'puerto_rico': '\ud83c\uddf5\ud83c\uddf7',
  'punch': '\ud83d\udc4a',
  'purple_circle': '\ud83d\udfe3',
  'purple_heart': '\ud83d\udc9c',
  'purple_square': '\ud83d\udfea',
  'purse': '\ud83d\udc5b',
  'pushpin': '\ud83d\udccc',
  'put_litter_in_its_place': '\ud83d\udeae',
  'qatar': '\ud83c\uddf6\ud83c\udde6',
  'question': '\u2753',
  'rabbit': '\ud83d\udc30',
  'rabbit2': '\ud83d\udc07',
  'raccoon': '\ud83e\udd9d',
  'racehorse': '\ud83d\udc0e',
  'racing_car': '\ud83c\udfce\ufe0f',
  'radio': '\ud83d\udcfb',
  'radio_button': '\ud83d\udd18',
  'radioactive': '\u2622\ufe0f',
  'rage': '\ud83d\ude21',
  'railway_car': '\ud83d\ude83',
  'railway_track': '\ud83d\udee4\ufe0f',
  'rainbow': '\ud83c\udf08',
  'rainbow_flag': '\ud83c\udff3\ufe0f\u200d\ud83c\udf08',
  'raised_back_of_hand': '\ud83e\udd1a',
  'raised_eyebrow': '\ud83e\udd28',
  'raised_hand': '\u270b',
  'raised_hand_with_fingers_splayed': '\ud83d\udd90\ufe0f',
  'raised_hands': '\ud83d\ude4c',
  'raising_hand': '\ud83d\ude4b',
  'raising_hand_man': '\ud83d\ude4b\u200d\u2642\ufe0f',
  'raising_hand_woman': '\ud83d\ude4b\u200d\u2640\ufe0f',
  'ram': '\ud83d\udc0f',
  'ramen': '\ud83c\udf5c',
  'rat': '\ud83d\udc00',
  'razor': '\ud83e\ude92',
  'receipt': '\ud83e\uddfe',
  'record_button': '\u23fa\ufe0f',
  'recycle': '\u267b\ufe0f',
  'red_car': '\ud83d\ude97',
  'red_circle': '\ud83d\udd34',
  'red_envelope': '\ud83e\udde7',
  'red_haired_man': '\ud83d\udc68\u200d\ud83e\uddb0',
  'red_haired_woman': '\ud83d\udc69\u200d\ud83e\uddb0',
  'red_square': '\ud83d\udfe5',
  'registered': '\u00ae\ufe0f',
  'relaxed': '\u263a\ufe0f',
  'relieved': '\ud83d\ude0c',
  'reminder_ribbon': '\ud83c\udf97\ufe0f',
  'repeat': '\ud83d\udd01',
  'repeat_one': '\ud83d\udd02',
  'rescue_worker_helmet': '\u26d1\ufe0f',
  'restroom': '\ud83d\udebb',
  'reunion': '\ud83c\uddf7\ud83c\uddea',
  'revolving_hearts': '\ud83d\udc9e',
  'rewind': '\u23ea',
  'rhinoceros': '\ud83e\udd8f',
  'ribbon': '\ud83c\udf80',
  'rice': '\ud83c\udf5a',
  'rice_ball': '\ud83c\udf59',
  'rice_cracker': '\ud83c\udf58',
  'rice_scene': '\ud83c\udf91',
  'right_anger_bubble': '\ud83d\uddef\ufe0f',
  'ring': '\ud83d\udc8d',
  'ringed_planet': '\ud83e\ude90',
  'robot': '\ud83e\udd16',
  'rocket': '\ud83d\ude80',
  'rofl': '\ud83e\udd23',
  'roll_eyes': '\ud83d\ude44',
  'roll_of_paper': '\ud83e\uddfb',
  'roller_coaster': '\ud83c\udfa2',
  'romania': '\ud83c\uddf7\ud83c\uddf4',
  'rooster': '\ud83d\udc13',
  'rose': '\ud83c\udf39',
  'rosette': '\ud83c\udff5\ufe0f',
  'rotating_light': '\ud83d\udea8',
  'round_pushpin': '\ud83d\udccd',
  'rowboat': '\ud83d\udea3',
  'rowing_man': '\ud83d\udea3\u200d\u2642\ufe0f',
  'rowing_woman': '\ud83d\udea3\u200d\u2640\ufe0f',
  'ru': '\ud83c\uddf7\ud83c\uddfa',
  'rugby_football': '\ud83c\udfc9',
  'runner': '\ud83c\udfc3',
  'running': '\ud83c\udfc3',
  'running_man': '\ud83c\udfc3\u200d\u2642\ufe0f',
  'running_shirt_with_sash': '\ud83c\udfbd',
  'running_woman': '\ud83c\udfc3\u200d\u2640\ufe0f',
  'rwanda': '\ud83c\uddf7\ud83c\uddfc',
  'sa': '\ud83c\ude02\ufe0f',
  'safety_pin': '\ud83e\uddf7',
  'safety_vest': '\ud83e\uddba',
  'sagittarius': '\u2650',
  'sailboat': '\u26f5',
  'sake': '\ud83c\udf76',
  'salt': '\ud83e\uddc2',
  'samoa': '\ud83c\uddfc\ud83c\uddf8',
  'san_marino': '\ud83c\uddf8\ud83c\uddf2',
  'sandal': '\ud83d\udc61',
  'sandwich': '\ud83e\udd6a',
  'santa': '\ud83c\udf85',
  'sao_tome_principe': '\ud83c\uddf8\ud83c\uddf9',
  'sari': '\ud83e\udd7b',
  'sassy_man': '\ud83d\udc81\u200d\u2642\ufe0f',
  'sassy_woman': '\ud83d\udc81\u200d\u2640\ufe0f',
  'satellite': '\ud83d\udce1',
  'satisfied': '\ud83d\ude06',
  'saudi_arabia': '\ud83c\uddf8\ud83c\udde6',
  'sauna_man': '\ud83e\uddd6\u200d\u2642\ufe0f',
  'sauna_person': '\ud83e\uddd6',
  'sauna_woman': '\ud83e\uddd6\u200d\u2640\ufe0f',
  'sauropod': '\ud83e\udd95',
  'saxophone': '\ud83c\udfb7',
  'scarf': '\ud83e\udde3',
  'school': '\ud83c\udfeb',
  'school_satchel': '\ud83c\udf92',
  'scientist': '\ud83e\uddd1\u200d\ud83d\udd2c',
  'scissors': '\u2702\ufe0f',
  'scorpion': '\ud83e\udd82',
  'scorpius': '\u264f',
  'scotland': '\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc73\udb40\udc63\udb40\udc74\udb40\udc7f',
  'scream': '\ud83d\ude31',
  'scream_cat': '\ud83d\ude40',
  'scroll': '\ud83d\udcdc',
  'seat': '\ud83d\udcba',
  'secret': '\u3299\ufe0f',
  'see_no_evil': '\ud83d\ude48',
  'seedling': '\ud83c\udf31',
  'selfie': '\ud83e\udd33',
  'senegal': '\ud83c\uddf8\ud83c\uddf3',
  'serbia': '\ud83c\uddf7\ud83c\uddf8',
  'service_dog': '\ud83d\udc15\u200d\ud83e\uddba',
  'seven': '7\ufe0f\u20e3',
  'seychelles': '\ud83c\uddf8\ud83c\udde8',
  'shallow_pan_of_food': '\ud83e\udd58',
  'shamrock': '\u2618\ufe0f',
  'shark': '\ud83e\udd88',
  'shaved_ice': '\ud83c\udf67',
  'sheep': '\ud83d\udc11',
  'shell': '\ud83d\udc1a',
  'shield': '\ud83d\udee1\ufe0f',
  'shinto_shrine': '\u26e9\ufe0f',
  'ship': '\ud83d\udea2',
  'shirt': '\ud83d\udc55',
  'shit': '\ud83d\udca9',
  'shoe': '\ud83d\udc5e',
  'shopping': '\ud83d\udecd\ufe0f',
  'shopping_cart': '\ud83d\uded2',
  'shorts': '\ud83e\ude73',
  'shower': '\ud83d\udebf',
  'shrimp': '\ud83e\udd90',
  'shrug': '\ud83e\udd37',
  'shushing_face': '\ud83e\udd2b',
  'sierra_leone': '\ud83c\uddf8\ud83c\uddf1',
  'signal_strength': '\ud83d\udcf6',
  'singapore': '\ud83c\uddf8\ud83c\uddec',
  'singer': '\ud83e\uddd1\u200d\ud83c\udfa4',
  'sint_maarten': '\ud83c\uddf8\ud83c\uddfd',
  'six': '6\ufe0f\u20e3',
  'six_pointed_star': '\ud83d\udd2f',
  'skateboard': '\ud83d\udef9',
  'ski': '\ud83c\udfbf',
  'skier': '\u26f7\ufe0f',
  'skull': '\ud83d\udc80',
  'skull_and_crossbones': '\u2620\ufe0f',
  'skunk': '\ud83e\udda8',
  'sled': '\ud83d\udef7',
  'sleeping': '\ud83d\ude34',
  'sleeping_bed': '\ud83d\udecc',
  'sleepy': '\ud83d\ude2a',
  'slightly_frowning_face': '\ud83d\ude41',
  'slightly_smiling_face': '\ud83d\ude42',
  'slot_machine': '\ud83c\udfb0',
  'sloth': '\ud83e\udda5',
  'slovakia': '\ud83c\uddf8\ud83c\uddf0',
  'slovenia': '\ud83c\uddf8\ud83c\uddee',
  'small_airplane': '\ud83d\udee9\ufe0f',
  'small_blue_diamond': '\ud83d\udd39',
  'small_orange_diamond': '\ud83d\udd38',
  'small_red_triangle': '\ud83d\udd3a',
  'small_red_triangle_down': '\ud83d\udd3b',
  'smile': '\ud83d\ude04',
  'smile_cat': '\ud83d\ude38',
  'smiley': '\ud83d\ude03',
  'smiley_cat': '\ud83d\ude3a',
  'smiling_face_with_three_hearts': '\ud83e\udd70',
  'smiling_imp': '\ud83d\ude08',
  'smirk': '\ud83d\ude0f',
  'smirk_cat': '\ud83d\ude3c',
  'smoking': '\ud83d\udeac',
  'snail': '\ud83d\udc0c',
  'snake': '\ud83d\udc0d',
  'sneezing_face': '\ud83e\udd27',
  'snowboarder': '\ud83c\udfc2',
  'snowflake': '\u2744\ufe0f',
  'snowman': '\u26c4',
  'snowman_with_snow': '\u2603\ufe0f',
  'soap': '\ud83e\uddfc',
  'sob': '\ud83d\ude2d',
  'soccer': '\u26bd',
  'socks': '\ud83e\udde6',
  'softball': '\ud83e\udd4e',
  'solomon_islands': '\ud83c\uddf8\ud83c\udde7',
  'somalia': '\ud83c\uddf8\ud83c\uddf4',
  'soon': '\ud83d\udd1c',
  'sos': '\ud83c\udd98',
  'sound': '\ud83d\udd09',
  'south_africa': '\ud83c\uddff\ud83c\udde6',
  'south_georgia_south_sandwich_islands': '\ud83c\uddec\ud83c\uddf8',
  'south_sudan': '\ud83c\uddf8\ud83c\uddf8',
  'space_invader': '\ud83d\udc7e',
  'spades': '\u2660\ufe0f',
  'spaghetti': '\ud83c\udf5d',
  'sparkle': '\u2747\ufe0f',
  'sparkler': '\ud83c\udf87',
  'sparkles': '\u2728',
  'sparkling_heart': '\ud83d\udc96',
  'speak_no_evil': '\ud83d\ude4a',
  'speaker': '\ud83d\udd08',
  'speaking_head': '\ud83d\udde3\ufe0f',
  'speech_balloon': '\ud83d\udcac',
  'speedboat': '\ud83d\udea4',
  'spider': '\ud83d\udd77\ufe0f',
  'spider_web': '\ud83d\udd78\ufe0f',
  'spiral_calendar': '\ud83d\uddd3\ufe0f',
  'spiral_notepad': '\ud83d\uddd2\ufe0f',
  'sponge': '\ud83e\uddfd',
  'spoon': '\ud83e\udd44',
  'squid': '\ud83e\udd91',
  'sri_lanka': '\ud83c\uddf1\ud83c\uddf0',
  'st_barthelemy': '\ud83c\udde7\ud83c\uddf1',
  'st_helena': '\ud83c\uddf8\ud83c\udded',
  'st_kitts_nevis': '\ud83c\uddf0\ud83c\uddf3',
  'st_lucia': '\ud83c\uddf1\ud83c\udde8',
  'st_martin': '\ud83c\uddf2\ud83c\uddeb',
  'st_pierre_miquelon': '\ud83c\uddf5\ud83c\uddf2',
  'st_vincent_grenadines': '\ud83c\uddfb\ud83c\udde8',
  'stadium': '\ud83c\udfdf\ufe0f',
  'standing_man': '\ud83e\uddcd\u200d\u2642\ufe0f',
  'standing_person': '\ud83e\uddcd',
  'standing_woman': '\ud83e\uddcd\u200d\u2640\ufe0f',
  'star': '\u2b50',
  'star2': '\ud83c\udf1f',
  'star_and_crescent': '\u262a\ufe0f',
  'star_of_david': '\u2721\ufe0f',
  'star_struck': '\ud83e\udd29',
  'stars': '\ud83c\udf20',
  'station': '\ud83d\ude89',
  'statue_of_liberty': '\ud83d\uddfd',
  'steam_locomotive': '\ud83d\ude82',
  'stethoscope': '\ud83e\ude7a',
  'stew': '\ud83c\udf72',
  'stop_button': '\u23f9\ufe0f',
  'stop_sign': '\ud83d\uded1',
  'stopwatch': '\u23f1\ufe0f',
  'straight_ruler': '\ud83d\udccf',
  'strawberry': '\ud83c\udf53',
  'stuck_out_tongue': '\ud83d\ude1b',
  'stuck_out_tongue_closed_eyes': '\ud83d\ude1d',
  'stuck_out_tongue_winking_eye': '\ud83d\ude1c',
  'student': '\ud83e\uddd1\u200d\ud83c\udf93',
  'studio_microphone': '\ud83c\udf99\ufe0f',
  'stuffed_flatbread': '\ud83e\udd59',
  'sudan': '\ud83c\uddf8\ud83c\udde9',
  'sun_behind_large_cloud': '\ud83c\udf25\ufe0f',
  'sun_behind_rain_cloud': '\ud83c\udf26\ufe0f',
  'sun_behind_small_cloud': '\ud83c\udf24\ufe0f',
  'sun_with_face': '\ud83c\udf1e',
  'sunflower': '\ud83c\udf3b',
  'sunglasses': '\ud83d\ude0e',
  'sunny': '\u2600\ufe0f',
  'sunrise': '\ud83c\udf05',
  'sunrise_over_mountains': '\ud83c\udf04',
  'superhero': '\ud83e\uddb8',
  'superhero_man': '\ud83e\uddb8\u200d\u2642\ufe0f',
  'superhero_woman': '\ud83e\uddb8\u200d\u2640\ufe0f',
  'supervillain': '\ud83e\uddb9',
  'supervillain_man': '\ud83e\uddb9\u200d\u2642\ufe0f',
  'supervillain_woman': '\ud83e\uddb9\u200d\u2640\ufe0f',
  'surfer': '\ud83c\udfc4',
  'surfing_man': '\ud83c\udfc4\u200d\u2642\ufe0f',
  'surfing_woman': '\ud83c\udfc4\u200d\u2640\ufe0f',
  'suriname': '\ud83c\uddf8\ud83c\uddf7',
  'sushi': '\ud83c\udf63',
  'suspension_railway': '\ud83d\ude9f',
  'svalbard_jan_mayen': '\ud83c\uddf8\ud83c\uddef',
  'swan': '\ud83e\udda2',
  'swaziland': '\ud83c\uddf8\ud83c\uddff',
  'sweat': '\ud83d\ude13',
  'sweat_drops': '\ud83d\udca6',
  'sweat_smile': '\ud83d\ude05',
  'sweden': '\ud83c\uddf8\ud83c\uddea',
  'sweet_potato': '\ud83c\udf60',
  'swim_brief': '\ud83e\ude72',
  'swimmer': '\ud83c\udfca',
  'swimming_man': '\ud83c\udfca\u200d\u2642\ufe0f',
  'swimming_woman': '\ud83c\udfca\u200d\u2640\ufe0f',
  'switzerland': '\ud83c\udde8\ud83c\udded',
  'symbols': '\ud83d\udd23',
  'synagogue': '\ud83d\udd4d',
  'syria': '\ud83c\uddf8\ud83c\uddfe',
  'syringe': '\ud83d\udc89',
  't-rex': '\ud83e\udd96',
  'taco': '\ud83c\udf2e',
  'tada': '\ud83c\udf89',
  'taiwan': '\ud83c\uddf9\ud83c\uddfc',
  'tajikistan': '\ud83c\uddf9\ud83c\uddef',
  'takeout_box': '\ud83e\udd61',
  'tanabata_tree': '\ud83c\udf8b',
  'tangerine': '\ud83c\udf4a',
  'tanzania': '\ud83c\uddf9\ud83c\uddff',
  'taurus': '\u2649',
  'taxi': '\ud83d\ude95',
  'tea': '\ud83c\udf75',
  'teacher': '\ud83e\uddd1\u200d\ud83c\udfeb',
  'technologist': '\ud83e\uddd1\u200d\ud83d\udcbb',
  'teddy_bear': '\ud83e\uddf8',
  'telephone': '\u260e\ufe0f',
  'telephone_receiver': '\ud83d\udcde',
  'telescope': '\ud83d\udd2d',
  'tennis': '\ud83c\udfbe',
  'tent': '\u26fa',
  'test_tube': '\ud83e\uddea',
  'thailand': '\ud83c\uddf9\ud83c\udded',
  'thermometer': '\ud83c\udf21\ufe0f',
  'thinking': '\ud83e\udd14',
  'thought_balloon': '\ud83d\udcad',
  'thread': '\ud83e\uddf5',
  'three': '3\ufe0f\u20e3',
  'thumbsdown': '\ud83d\udc4e',
  'thumbsup': '\ud83d\udc4d',
  'ticket': '\ud83c\udfab',
  'tickets': '\ud83c\udf9f\ufe0f',
  'tiger': '\ud83d\udc2f',
  'tiger2': '\ud83d\udc05',
  'timer_clock': '\u23f2\ufe0f',
  'timor_leste': '\ud83c\uddf9\ud83c\uddf1',
  'tipping_hand_man': '\ud83d\udc81\u200d\u2642\ufe0f',
  'tipping_hand_person': '\ud83d\udc81',
  'tipping_hand_woman': '\ud83d\udc81\u200d\u2640\ufe0f',
  'tired_face': '\ud83d\ude2b',
  'tm': '\u2122\ufe0f',
  'togo': '\ud83c\uddf9\ud83c\uddec',
  'toilet': '\ud83d\udebd',
  'tokelau': '\ud83c\uddf9\ud83c\uddf0',
  'tokyo_tower': '\ud83d\uddfc',
  'tomato': '\ud83c\udf45',
  'tonga': '\ud83c\uddf9\ud83c\uddf4',
  'tongue': '\ud83d\udc45',
  'toolbox': '\ud83e\uddf0',
  'tooth': '\ud83e\uddb7',
  'top': '\ud83d\udd1d',
  'tophat': '\ud83c\udfa9',
  'tornado': '\ud83c\udf2a\ufe0f',
  'tr': '\ud83c\uddf9\ud83c\uddf7',
  'trackball': '\ud83d\uddb2\ufe0f',
  'tractor': '\ud83d\ude9c',
  'traffic_light': '\ud83d\udea5',
  'train': '\ud83d\ude8b',
  'train2': '\ud83d\ude86',
  'tram': '\ud83d\ude8a',
  'triangular_flag_on_post': '\ud83d\udea9',
  'triangular_ruler': '\ud83d\udcd0',
  'trident': '\ud83d\udd31',
  'trinidad_tobago': '\ud83c\uddf9\ud83c\uddf9',
  'tristan_da_cunha': '\ud83c\uddf9\ud83c\udde6',
  'triumph': '\ud83d\ude24',
  'trolleybus': '\ud83d\ude8e',
  'trophy': '\ud83c\udfc6',
  'tropical_drink': '\ud83c\udf79',
  'tropical_fish': '\ud83d\udc20',
  'truck': '\ud83d\ude9a',
  'trumpet': '\ud83c\udfba',
  'tshirt': '\ud83d\udc55',
  'tulip': '\ud83c\udf37',
  'tumbler_glass': '\ud83e\udd43',
  'tunisia': '\ud83c\uddf9\ud83c\uddf3',
  'turkey': '\ud83e\udd83',
  'turkmenistan': '\ud83c\uddf9\ud83c\uddf2',
  'turks_caicos_islands': '\ud83c\uddf9\ud83c\udde8',
  'turtle': '\ud83d\udc22',
  'tuvalu': '\ud83c\uddf9\ud83c\uddfb',
  'tv': '\ud83d\udcfa',
  'twisted_rightwards_arrows': '\ud83d\udd00',
  'two': '2\ufe0f\u20e3',
  'two_hearts': '\ud83d\udc95',
  'two_men_holding_hands': '\ud83d\udc6c',
  'two_women_holding_hands': '\ud83d\udc6d',
  'u5272': '\ud83c\ude39',
  'u5408': '\ud83c\ude34',
  'u55b6': '\ud83c\ude3a',
  'u6307': '\ud83c\ude2f',
  'u6708': '\ud83c\ude37\ufe0f',
  'u6709': '\ud83c\ude36',
  'u6e80': '\ud83c\ude35',
  'u7121': '\ud83c\ude1a',
  'u7533': '\ud83c\ude38',
  'u7981': '\ud83c\ude32',
  'u7a7a': '\ud83c\ude33',
  'uganda': '\ud83c\uddfa\ud83c\uddec',
  'uk': '\ud83c\uddec\ud83c\udde7',
  'ukraine': '\ud83c\uddfa\ud83c\udde6',
  'umbrella': '\u2614',
  'unamused': '\ud83d\ude12',
  'underage': '\ud83d\udd1e',
  'unicorn': '\ud83e\udd84',
  'united_arab_emirates': '\ud83c\udde6\ud83c\uddea',
  'united_nations': '\ud83c\uddfa\ud83c\uddf3',
  'unlock': '\ud83d\udd13',
  'up': '\ud83c\udd99',
  'upside_down_face': '\ud83d\ude43',
  'uruguay': '\ud83c\uddfa\ud83c\uddfe',
  'us': '\ud83c\uddfa\ud83c\uddf8',
  'us_outlying_islands': '\ud83c\uddfa\ud83c\uddf2',
  'us_virgin_islands': '\ud83c\uddfb\ud83c\uddee',
  'uzbekistan': '\ud83c\uddfa\ud83c\uddff',
  'v': '\u270c\ufe0f',
  'vampire': '\ud83e\udddb',
  'vampire_man': '\ud83e\udddb\u200d\u2642\ufe0f',
  'vampire_woman': '\ud83e\udddb\u200d\u2640\ufe0f',
  'vanuatu': '\ud83c\uddfb\ud83c\uddfa',
  'vatican_city': '\ud83c\uddfb\ud83c\udde6',
  'venezuela': '\ud83c\uddfb\ud83c\uddea',
  'vertical_traffic_light': '\ud83d\udea6',
  'vhs': '\ud83d\udcfc',
  'vibration_mode': '\ud83d\udcf3',
  'video_camera': '\ud83d\udcf9',
  'video_game': '\ud83c\udfae',
  'vietnam': '\ud83c\uddfb\ud83c\uddf3',
  'violin': '\ud83c\udfbb',
  'virgo': '\u264d',
  'volcano': '\ud83c\udf0b',
  'volleyball': '\ud83c\udfd0',
  'vomiting_face': '\ud83e\udd2e',
  'vs': '\ud83c\udd9a',
  'vulcan_salute': '\ud83d\udd96',
  'waffle': '\ud83e\uddc7',
  'wales': '\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc77\udb40\udc6c\udb40\udc73\udb40\udc7f',
  'walking': '\ud83d\udeb6',
  'walking_man': '\ud83d\udeb6\u200d\u2642\ufe0f',
  'walking_woman': '\ud83d\udeb6\u200d\u2640\ufe0f',
  'wallis_futuna': '\ud83c\uddfc\ud83c\uddeb',
  'waning_crescent_moon': '\ud83c\udf18',
  'waning_gibbous_moon': '\ud83c\udf16',
  'warning': '\u26a0\ufe0f',
  'wastebasket': '\ud83d\uddd1\ufe0f',
  'watch': '\u231a',
  'water_buffalo': '\ud83d\udc03',
  'water_polo': '\ud83e\udd3d',
  'watermelon': '\ud83c\udf49',
  'wave': '\ud83d\udc4b',
  'wavy_dash': '\u3030\ufe0f',
  'waxing_crescent_moon': '\ud83c\udf12',
  'waxing_gibbous_moon': '\ud83c\udf14',
  'wc': '\ud83d\udebe',
  'weary': '\ud83d\ude29',
  'wedding': '\ud83d\udc92',
  'weight_lifting': '\ud83c\udfcb\ufe0f',
  'weight_lifting_man': '\ud83c\udfcb\ufe0f\u200d\u2642\ufe0f',
  'weight_lifting_woman': '\ud83c\udfcb\ufe0f\u200d\u2640\ufe0f',
  'western_sahara': '\ud83c\uddea\ud83c\udded',
  'whale': '\ud83d\udc33',
  'whale2': '\ud83d\udc0b',
  'wheel_of_dharma': '\u2638\ufe0f',
  'wheelchair': '\u267f',
  'white_check_mark': '\u2705',
  'white_circle': '\u26aa',
  'white_flag': '\ud83c\udff3\ufe0f',
  'white_flower': '\ud83d\udcae',
  'white_haired_man': '\ud83d\udc68\u200d\ud83e\uddb3',
  'white_haired_woman': '\ud83d\udc69\u200d\ud83e\uddb3',
  'white_heart': '\ud83e\udd0d',
  'white_large_square': '\u2b1c',
  'white_medium_small_square': '\u25fd',
  'white_medium_square': '\u25fb\ufe0f',
  'white_small_square': '\u25ab\ufe0f',
  'white_square_button': '\ud83d\udd33',
  'wilted_flower': '\ud83e\udd40',
  'wind_chime': '\ud83c\udf90',
  'wind_face': '\ud83c\udf2c\ufe0f',
  'wine_glass': '\ud83c\udf77',
  'wink': '\ud83d\ude09',
  'wolf': '\ud83d\udc3a',
  'woman': '\ud83d\udc69',
  'woman_artist': '\ud83d\udc69\u200d\ud83c\udfa8',
  'woman_astronaut': '\ud83d\udc69\u200d\ud83d\ude80',
  'woman_cartwheeling': '\ud83e\udd38\u200d\u2640\ufe0f',
  'woman_cook': '\ud83d\udc69\u200d\ud83c\udf73',
  'woman_dancing': '\ud83d\udc83',
  'woman_facepalming': '\ud83e\udd26\u200d\u2640\ufe0f',
  'woman_factory_worker': '\ud83d\udc69\u200d\ud83c\udfed',
  'woman_farmer': '\ud83d\udc69\u200d\ud83c\udf3e',
  'woman_firefighter': '\ud83d\udc69\u200d\ud83d\ude92',
  'woman_health_worker': '\ud83d\udc69\u200d\u2695\ufe0f',
  'woman_in_manual_wheelchair': '\ud83d\udc69\u200d\ud83e\uddbd',
  'woman_in_motorized_wheelchair': '\ud83d\udc69\u200d\ud83e\uddbc',
  'woman_judge': '\ud83d\udc69\u200d\u2696\ufe0f',
  'woman_juggling': '\ud83e\udd39\u200d\u2640\ufe0f',
  'woman_mechanic': '\ud83d\udc69\u200d\ud83d\udd27',
  'woman_office_worker': '\ud83d\udc69\u200d\ud83d\udcbc',
  'woman_pilot': '\ud83d\udc69\u200d\u2708\ufe0f',
  'woman_playing_handball': '\ud83e\udd3e\u200d\u2640\ufe0f',
  'woman_playing_water_polo': '\ud83e\udd3d\u200d\u2640\ufe0f',
  'woman_scientist': '\ud83d\udc69\u200d\ud83d\udd2c',
  'woman_shrugging': '\ud83e\udd37\u200d\u2640\ufe0f',
  'woman_singer': '\ud83d\udc69\u200d\ud83c\udfa4',
  'woman_student': '\ud83d\udc69\u200d\ud83c\udf93',
  'woman_teacher': '\ud83d\udc69\u200d\ud83c\udfeb',
  'woman_technologist': '\ud83d\udc69\u200d\ud83d\udcbb',
  'woman_with_headscarf': '\ud83e\uddd5',
  'woman_with_probing_cane': '\ud83d\udc69\u200d\ud83e\uddaf',
  'woman_with_turban': '\ud83d\udc73\u200d\u2640\ufe0f',
  'womans_clothes': '\ud83d\udc5a',
  'womans_hat': '\ud83d\udc52',
  'women_wrestling': '\ud83e\udd3c\u200d\u2640\ufe0f',
  'womens': '\ud83d\udeba',
  'woozy_face': '\ud83e\udd74',
  'world_map': '\ud83d\uddfa\ufe0f',
  'worried': '\ud83d\ude1f',
  'wrench': '\ud83d\udd27',
  'wrestling': '\ud83e\udd3c',
  'writing_hand': '\u270d\ufe0f',
  'x': '\u274c',
  'yarn': '\ud83e\uddf6',
  'yawning_face': '\ud83e\udd71',
  'yellow_circle': '\ud83d\udfe1',
  'yellow_heart': '\ud83d\udc9b',
  'yellow_square': '\ud83d\udfe8',
  'yemen': '\ud83c\uddfe\ud83c\uddea',
  'yen': '\ud83d\udcb4',
  'yin_yang': '\u262f\ufe0f',
  'yo_yo': '\ud83e\ude80',
  'yum': '\ud83d\ude0b',
  'zambia': '\ud83c\uddff\ud83c\uddf2',
  'zany_face': '\ud83e\udd2a',
  'zap': '\u26a1',
  'zebra': '\ud83e\udd93',
  'zero': '0\ufe0f\u20e3',
  'zimbabwe': '\ud83c\uddff\ud83c\uddfc',
  'zipper_mouth_face': '\ud83e\udd10',
  'zombie': '\ud83e\udddf',
  'zombie_man': '\ud83e\udddf\u200d\u2642\ufe0f',
  'zombie_woman': '\ud83e\udddf\u200d\u2640\ufe0f',
  'zzz': '\ud83d\udca4',

  /* special emojis :P */
  'atom': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/atom.png?v8">',
  'basecamp': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/basecamp.png?v8">',
  'basecampy': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/basecampy.png?v8">',
  'bowtie': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/bowtie.png?v8">',
  'electron': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/electron.png?v8">',
  'feelsgood': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/feelsgood.png?v8">',
  'finnadie': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/finnadie.png?v8">',
  'goberserk': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/goberserk.png?v8">',
  'godmode': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/godmode.png?v8">',
  'hurtrealbad': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/hurtrealbad.png?v8">',
  'neckbeard': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/neckbeard.png?v8">',
  'octocat': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/octocat.png?v8">',
  'rage1': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/rage1.png?v8">',
  'rage2': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/rage2.png?v8">',
  'rage3': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/rage3.png?v8">',
  'rage4': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/rage4.png?v8">',
  'shipit': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/shipit.png?v8">',
  'suspect': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/suspect.png?v8">',
  'trollface': '<img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/trollface.png?v8">',
  'showdown': '<img width="20" height="20" align="absmiddle" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAS1BMVEX///8jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS3b1q3b1q3b1q3b1q3b1q3b1q3b1q3b1q0565CIAAAAGXRSTlMAQHCAYCCw/+DQwPCQUBAwoHCAEP+wwFBgS2fvBgAAAUZJREFUeAHs1cGy7BAUheFFsEDw/k97VTq3T6ge2EmdM+pvrP6Iwd74XV9Kb52xuMU4/uc1YNgZLFOeV8FGdhGrNk5SEgUyPxAEdj4LlMRDyhVAMVEa2M7TBSeVZAFPdqHgzSZJwPKgcLFLAooHDJo4EDCw4gAtBoJA5UFj4Ng5LOGLwVXZuoIlji/jeQHFk7+baHxrCjeUwB9+s88KndvlhcyBN5BSkYNQIVVb4pV+Npm7hhuKDs/uMP5KxT3WzSNNLIuuoDpMmuAVMruMSeDyQBi24DTr43LAY7ILA1QYaWkgfHzFthYYzg67SQsCbB8GhJUEGCtO9n0rSaCLxgJQjS/JSgMTg2eBDEHAJ+H350AsjYNYscrErgI2e/l+mdR967TCX/v6N0EhPECYCP0i+IAoYQOE8BogNhQMEMdrgAQWHaMAAGi5I5euoY9NAAAAAElFTkSuQmCC">'
};
```

## File: `src/loader.js`
```javascript
var root = this;

// AMD Loader
if (typeof define === 'function' && define.amd) {
  define(function () {
    'use strict';
    return showdown;
  });

// CommonJS/nodeJS Loader
} else if (typeof module !== 'undefined' && module.exports) {
  module.exports = showdown;

// Regular Browser loader
} else {
  root.showdown = showdown;
}
```

## File: `src/options.js`
```javascript
/**
 * Created by Tivie on 13-07-2015.
 */

function getDefaultOpts (simple) {
  'use strict';

  var defaultOptions = {
    omitExtraWLInCodeBlocks: {
      defaultValue: false,
      describe: 'Omit the default extra whiteline added to code blocks',
      type: 'boolean'
    },
    noHeaderId: {
      defaultValue: false,
      describe: 'Turn on/off generated header id',
      type: 'boolean'
    },
    prefixHeaderId: {
      defaultValue: false,
      describe: 'Add a prefix to the generated header ids. Passing a string will prefix that string to the header id. Setting to true will add a generic \'section-\' prefix',
      type: 'string'
    },
    rawPrefixHeaderId: {
      defaultValue: false,
      describe: 'Setting this option to true will prevent showdown from modifying the prefix. This might result in malformed IDs (if, for instance, the " char is used in the prefix)',
      type: 'boolean'
    },
    ghCompatibleHeaderId: {
      defaultValue: false,
      describe: 'Generate header ids compatible with github style (spaces are replaced with dashes, a bunch of non alphanumeric chars are removed)',
      type: 'boolean'
    },
    rawHeaderId: {
      defaultValue: false,
      describe: 'Remove only spaces, \' and " from generated header ids (including prefixes), replacing them with dashes (-). WARNING: This might result in malformed ids',
      type: 'boolean'
    },
    headerLevelStart: {
      defaultValue: false,
      describe: 'The header blocks level start',
      type: 'integer'
    },
    parseImgDimensions: {
      defaultValue: false,
      describe: 'Turn on/off image dimension parsing',
      type: 'boolean'
    },
    simplifiedAutoLink: {
      defaultValue: false,
      describe: 'Turn on/off GFM autolink style',
      type: 'boolean'
    },
    literalMidWordUnderscores: {
      defaultValue: false,
      describe: 'Parse midword underscores as literal underscores',
      type: 'boolean'
    },
    literalMidWordAsterisks: {
      defaultValue: false,
      describe: 'Parse midword asterisks as literal asterisks',
      type: 'boolean'
    },
    strikethrough: {
      defaultValue: false,
      describe: 'Turn on/off strikethrough support',
      type: 'boolean'
    },
    tables: {
      defaultValue: false,
      describe: 'Turn on/off tables support',
      type: 'boolean'
    },
    tablesHeaderId: {
      defaultValue: false,
      describe: 'Add an id to table headers',
      type: 'boolean'
    },
    ghCodeBlocks: {
      defaultValue: true,
      describe: 'Turn on/off GFM fenced code blocks support',
      type: 'boolean'
    },
    tasklists: {
      defaultValue: false,
      describe: 'Turn on/off GFM tasklist support',
      type: 'boolean'
    },
    smoothLivePreview: {
      defaultValue: false,
      describe: 'Prevents weird effects in live previews due to incomplete input',
      type: 'boolean'
    },
    smartIndentationFix: {
      defaultValue: false,
      describe: 'Tries to smartly fix indentation in es6 strings',
      type: 'boolean'
    },
    disableForced4SpacesIndentedSublists: {
      defaultValue: false,
      describe: 'Disables the requirement of indenting nested sublists by 4 spaces',
      type: 'boolean'
    },
    simpleLineBreaks: {
      defaultValue: false,
      describe: 'Parses simple line breaks as <br> (GFM Style)',
      type: 'boolean'
    },
    requireSpaceBeforeHeadingText: {
      defaultValue: false,
      describe: 'Makes adding a space between `#` and the header text mandatory (GFM Style)',
      type: 'boolean'
    },
    ghMentions: {
      defaultValue: false,
      describe: 'Enables github @mentions',
      type: 'boolean'
    },
    ghMentionsLink: {
      defaultValue: 'https://github.com/{u}',
      describe: 'Changes the link generated by @mentions. Only applies if ghMentions option is enabled.',
      type: 'string'
    },
    encodeEmails: {
      defaultValue: true,
      describe: 'Encode e-mail addresses through the use of Character Entities, transforming ASCII e-mail addresses into its equivalent decimal entities',
      type: 'boolean'
    },
    openLinksInNewWindow: {
      defaultValue: false,
      describe: 'Open all links in new windows',
      type: 'boolean'
    },
    backslashEscapesHTMLTags: {
      defaultValue: false,
      describe: 'Support for HTML Tag escaping. ex: \<div>foo\</div>',
      type: 'boolean'
    },
    emoji: {
      defaultValue: false,
      describe: 'Enable emoji support. Ex: `this is a :smile: emoji`',
      type: 'boolean'
    },
    underline: {
      defaultValue: false,
      describe: 'Enable support for underline. Syntax is double or triple underscores: `__underline word__`. With this option enabled, underscores no longer parses into `<em>` and `<strong>`',
      type: 'boolean'
    },
    ellipsis: {
      defaultValue: true,
      describe: 'Replaces three dots with the ellipsis unicode character',
      type: 'boolean'
    },
    completeHTMLDocument: {
      defaultValue: false,
      describe: 'Outputs a complete html document, including `<html>`, `<head>` and `<body>` tags',
      type: 'boolean'
    },
    metadata: {
      defaultValue: false,
      describe: 'Enable support for document metadata (defined at the top of the document between `«««` and `»»»` or between `---` and `---`).',
      type: 'boolean'
    },
    splitAdjacentBlockquotes: {
      defaultValue: false,
      describe: 'Split adjacent blockquote blocks',
      type: 'boolean'
    },
    moreStyling: {
      defaultValue: false,
      describe: 'Adds some useful styling css classes in the generated html',
      type: 'boolean'
    },
    relativePathBaseUrl: {
      defaultValue: false,
      describe: 'Prepends a base URL to relative paths',
      type: 'string'
    },
  };
  if (simple === false) {
    return JSON.parse(JSON.stringify(defaultOptions));
  }
  var ret = {};
  for (var opt in defaultOptions) {
    if (defaultOptions.hasOwnProperty(opt)) {
      ret[opt] = defaultOptions[opt].defaultValue;
    }
  }
  return ret;
}

function allOptionsOn () {
  'use strict';
  var options = getDefaultOpts(true),
      ret = {};
  for (var opt in options) {
    if (options.hasOwnProperty(opt)) {
      ret[opt] = true;
    }
  }
  return ret;
}
```

## File: `src/showdown.js`
```javascript
/**
 * Created by Tivie on 06-01-2015.
 */
// Private properties
var showdown = {},
    parsers = {},
    extensions = {},
    globalOptions = getDefaultOpts(true),
    setFlavor = 'vanilla',
    flavor = {
      github: {
        omitExtraWLInCodeBlocks:              true,
        simplifiedAutoLink:                   true,
        literalMidWordUnderscores:            true,
        strikethrough:                        true,
        tables:                               true,
        tablesHeaderId:                       true,
        ghCodeBlocks:                         true,
        tasklists:                            true,
        disableForced4SpacesIndentedSublists: true,
        simpleLineBreaks:                     true,
        requireSpaceBeforeHeadingText:        true,
        ghCompatibleHeaderId:                 true,
        ghMentions:                           true,
        backslashEscapesHTMLTags:             true,
        emoji:                                true,
        splitAdjacentBlockquotes:             true
      },
      original: {
        noHeaderId:                           true,
        ghCodeBlocks:                         false
      },
      ghost: {
        omitExtraWLInCodeBlocks:              true,
        parseImgDimensions:                   true,
        simplifiedAutoLink:                   true,
        literalMidWordUnderscores:            true,
        strikethrough:                        true,
        tables:                               true,
        tablesHeaderId:                       true,
        ghCodeBlocks:                         true,
        tasklists:                            true,
        smoothLivePreview:                    true,
        simpleLineBreaks:                     true,
        requireSpaceBeforeHeadingText:        true,
        ghMentions:                           false,
        encodeEmails:                         true
      },
      vanilla: getDefaultOpts(true),
      allOn: allOptionsOn()
    };

/**
 * helper namespace
 * @type {{}}
 */
showdown.helper = {};

/**
 * TODO LEGACY SUPPORT CODE
 * @type {{}}
 */
showdown.extensions = {};

/**
 * Set a global option
 * @static
 * @param {string} key
 * @param {*} value
 * @returns {showdown}
 */
showdown.setOption = function (key, value) {
  'use strict';
  globalOptions[key] = value;
  return this;
};

/**
 * Get a global option
 * @static
 * @param {string} key
 * @returns {*}
 */
showdown.getOption = function (key) {
  'use strict';
  return globalOptions[key];
};

/**
 * Get the global options
 * @static
 * @returns {{}}
 */
showdown.getOptions = function () {
  'use strict';
  return globalOptions;
};

/**
 * Reset global options to the default values
 * @static
 */
showdown.resetOptions = function () {
  'use strict';
  globalOptions = getDefaultOpts(true);
};

/**
 * Set the flavor showdown should use as default
 * @param {string} name
 */
showdown.setFlavor = function (name) {
  'use strict';
  if (!flavor.hasOwnProperty(name)) {
    throw Error(name + ' flavor was not found');
  }
  showdown.resetOptions();
  var preset = flavor[name];
  setFlavor = name;
  for (var option in preset) {
    if (preset.hasOwnProperty(option)) {
      globalOptions[option] = preset[option];
    }
  }
};

/**
 * Get the currently set flavor
 * @returns {string}
 */
showdown.getFlavor = function () {
  'use strict';
  return setFlavor;
};

/**
 * Get the options of a specified flavor. Returns undefined if the flavor was not found
 * @param {string} name Name of the flavor
 * @returns {{}|undefined}
 */
showdown.getFlavorOptions = function (name) {
  'use strict';
  if (flavor.hasOwnProperty(name)) {
    return flavor[name];
  }
};

/**
 * Get the default options
 * @static
 * @param {boolean} [simple=true]
 * @returns {{}}
 */
showdown.getDefaultOptions = function (simple) {
  'use strict';
  return getDefaultOpts(simple);
};

/**
 * Get or set a subParser
 *
 * subParser(name)       - Get a registered subParser
 * subParser(name, func) - Register a subParser
 * @static
 * @param {string} name
 * @param {function} [func]
 * @returns {*}
 */
showdown.subParser = function (name, func) {
  'use strict';
  if (showdown.helper.isString(name)) {
    if (typeof func !== 'undefined') {
      parsers[name] = func;
    } else {
      if (parsers.hasOwnProperty(name)) {
        return parsers[name];
      } else {
        throw Error('SubParser named ' + name + ' not registered!');
      }
    }
  } else {
    throw Error('showdown.subParser function first argument must be a string (the name of the subparser)');
  }
};

/**
 * Gets or registers an extension
 * @static
 * @param {string} name
 * @param {object|object[]|function=} ext
 * @returns {*}
 */
showdown.extension = function (name, ext) {
  'use strict';

  if (!showdown.helper.isString(name)) {
    throw Error('Extension \'name\' must be a string');
  }

  name = showdown.helper.stdExtName(name);

  // Getter
  if (showdown.helper.isUndefined(ext)) {
    if (!extensions.hasOwnProperty(name)) {
      throw Error('Extension named ' + name + ' is not registered!');
    }
    return extensions[name];

    // Setter
  } else {
    // Expand extension if it's wrapped in a function
    if (typeof ext === 'function') {
      ext = ext();
    }

    // Ensure extension is an array
    if (!showdown.helper.isArray(ext)) {
      ext = [ext];
    }

    var validExtension = validate(ext, name);

    if (validExtension.valid) {
      extensions[name] = ext;
    } else {
      throw Error(validExtension.error);
    }
  }
};

/**
 * Gets all extensions registered
 * @returns {{}}
 */
showdown.getAllExtensions = function () {
  'use strict';
  return extensions;
};

/**
 * Remove an extension
 * @param {string} name
 */
showdown.removeExtension = function (name) {
  'use strict';
  delete extensions[name];
};

/**
 * Removes all extensions
 */
showdown.resetExtensions = function () {
  'use strict';
  extensions = {};
};

/**
 * Validate extension
 * @param {array} extension
 * @param {string} name
 * @returns {{valid: boolean, error: string}}
 */
function validate (extension, name) {
  'use strict';

  var errMsg = (name) ? 'Error in ' + name + ' extension->' : 'Error in unnamed extension',
      ret = {
        valid: true,
        error: ''
      };

  if (!showdown.helper.isArray(extension)) {
    extension = [extension];
  }

  for (var i = 0; i < extension.length; ++i) {
    var baseMsg = errMsg + ' sub-extension ' + i + ': ',
        ext = extension[i];
    if (typeof ext !== 'object') {
      ret.valid = false;
      ret.error = baseMsg + 'must be an object, but ' + typeof ext + ' given';
      return ret;
    }

    if (!showdown.helper.isString(ext.type)) {
      ret.valid = false;
      ret.error = baseMsg + 'property "type" must be a string, but ' + typeof ext.type + ' given';
      return ret;
    }

    var type = ext.type = ext.type.toLowerCase();

    // normalize extension type
    if (type === 'language') {
      type = ext.type = 'lang';
    }

    if (type === 'html') {
      type = ext.type = 'output';
    }

    if (type !== 'lang' && type !== 'output' && type !== 'listener') {
      ret.valid = false;
      ret.error = baseMsg + 'type ' + type + ' is not recognized. Valid values: "lang/language", "output/html" or "listener"';
      return ret;
    }

    if (type === 'listener') {
      if (showdown.helper.isUndefined(ext.listeners)) {
        ret.valid = false;
        ret.error = baseMsg + '. Extensions of type "listener" must have a property called "listeners"';
        return ret;
      }
    } else {
      if (showdown.helper.isUndefined(ext.filter) && showdown.helper.isUndefined(ext.regex)) {
        ret.valid = false;
        ret.error = baseMsg + type + ' extensions must define either a "regex" property or a "filter" method';
        return ret;
      }
    }

    if (ext.listeners) {
      if (typeof ext.listeners !== 'object') {
        ret.valid = false;
        ret.error = baseMsg + '"listeners" property must be an object but ' + typeof ext.listeners + ' given';
        return ret;
      }
      for (var ln in ext.listeners) {
        if (ext.listeners.hasOwnProperty(ln)) {
          if (typeof ext.listeners[ln] !== 'function') {
            ret.valid = false;
            ret.error = baseMsg + '"listeners" property must be an hash of [event name]: [callback]. listeners.' + ln +
              ' must be a function but ' + typeof ext.listeners[ln] + ' given';
            return ret;
          }
        }
      }
    }

    if (ext.filter) {
      if (typeof ext.filter !== 'function') {
        ret.valid = false;
        ret.error = baseMsg + '"filter" must be a function, but ' + typeof ext.filter + ' given';
        return ret;
      }
    } else if (ext.regex) {
      if (showdown.helper.isString(ext.regex)) {
        ext.regex = new RegExp(ext.regex, 'g');
      }
      if (!(ext.regex instanceof RegExp)) {
        ret.valid = false;
        ret.error = baseMsg + '"regex" property must either be a string or a RegExp object, but ' + typeof ext.regex + ' given';
        return ret;
      }
      if (showdown.helper.isUndefined(ext.replace)) {
        ret.valid = false;
        ret.error = baseMsg + '"regex" extensions must implement a replace string or function';
        return ret;
      }
    }
  }
  return ret;
}

/**
 * Validate extension
 * @param {object} ext
 * @returns {boolean}
 */
showdown.validateExtension = function (ext) {
  'use strict';

  var validateExtension = validate(ext, null);
  if (!validateExtension.valid) {
    console.warn(validateExtension.error);
    return false;
  }
  return true;
};
```

## File: `src/cli/cli.js`
```javascript
/**
 * Created by tivie
 */
var fs = require('fs'),
    path = require('path'),
    Command = require('commander').Command,
    program = new Command(),
    path1 = path.resolve(__dirname + '/../dist/showdown.js'),
    path2 = path.resolve(__dirname + '/../../.build/showdown.js'),
    showdown,
    version;

// require shodown. We use conditional loading for each use case
if (fs.existsSync(path1)) {
  // production. File lives in bin directory
  showdown = require(path1);
  version = require(path.resolve(__dirname + '/../package.json')).version;
} else if (fs.existsSync(path2)) {
  // testing envo, uses the concatenated stuff for testing
  showdown = require(path2);
  version = require(path.resolve(__dirname + '/../../package.json')).version;
} else {
  // cold testing (manual) of cli.js in the src file. We load the dist file
  showdown = require('../../dist/showdown');
  version = require('../../package.json');
}


program
  .name('showdown')
  .description('CLI to Showdownjs markdown parser v' + version)
  .version(version)
  .usage('<command> [options]')
  .option('-q, --quiet', 'Quiet mode. Only print errors')
  .option('-m, --mute', 'Mute mode. Does not print anything');

program.command('makehtml')
  .description('Converts markdown into html')

  .addHelpText('after', '\n\nExamples:')
  .addHelpText('after', '  showdown makehtml -i                     Reads from stdin and outputs to stdout')
  .addHelpText('after', '  showdown makehtml -i foo.md -o bar.html  Reads \'foo.md\' and writes to \'bar.html\'')
  .addHelpText('after', '  showdown makehtml -i --flavor="github"   Parses stdin using GFM style')

  .addHelpText('after', '\nNote for windows users:')
  .addHelpText('after', 'When reading from stdin, use option -u to set the proper encoding or run `chcp 65001` prior to calling showdown cli to set the command line to utf-8')

  .option('-i, --input [file]', 'Input source. Usually a md file. If omitted or empty, reads from stdin. Windows users see note below.', true)
  .option('-o, --output [file]', 'Output target. Usually a html file. If omitted or empty, writes to stdout', true)
  .option('-u, --encoding <encoding>', 'Sets the input encoding', 'utf8')
  .option('-y, --output-encoding <encoding>', 'Sets the output encoding', 'utf8')
  .option('-a, --append', 'Append data to output instead of overwriting. Ignored if writing to stdout', false)
  .option('-e, --extensions <extensions...>', 'Load the specified extensions. Should be valid paths to node compatible extensions')
  .option('-p, --flavor <flavor>', 'Run with a predetermined flavor of options. Default is vanilla', 'vanilla')
  .option('-c, --config <config...>', 'Enables showdown makehtml parser config options. Overrides flavor')
  .option('--config-help', 'Shows configuration options for showdown parser')
  .action(makehtmlCommand);

program.parse();


//
// HELPER FUCNTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/**
 * Messenger helper object to the CLI
 * @param {string} writeMode
 * @param {boolean} supress
 * @param {boolean} mute
 * @constructor
 */
function Messenger (writeMode, supress, mute) {
  'use strict';
  writeMode = writeMode || 'stderr';
  supress = (!!supress || !!mute);
  mute = !!mute;
  this._print = (writeMode === 'stdout') ? console.log : console.error;

  this.errorExit = function (e) {
    if (!mute) {
      console.error('ERROR: ' + e.message);
      console.error('Run \'showdown <command> -h\' for help');
    }
    process.exit(1);
  };

  this.okExit = function () {
    if (!mute) {
      this._print('\n');
      this._print('DONE!');
    }
    process.exit(0);
  };

  this.printMsg = function (msg) {
    if (supress || mute || !msg) {
      return;
    }
    this._print(msg);
  };

  this.printError = function (msg) {
    if (mute) {
      return;
    }
    console.error(msg);
  };

}

/**
 * Helper function to show Showdown Options
 */
function showShowdownOptions () {
  'use strict';
  var showdownOptions = showdown.getDefaultOptions(false);
  console.log('\nshowdown makehtml config options:');
  // show showdown options
  for (var sopt in showdownOptions) {
    if (showdownOptions.hasOwnProperty(sopt)) {
      console.log('  ' + sopt + ':', '[default=' + showdownOptions[sopt].defaultValue + ']',showdownOptions[sopt].describe);
    }
  }
  console.log('\n\nExample: showdown makehtml -c openLinksInNewWindow ghMentions ghMentionsLink="https://google.com"');
}

/**
 * Helper function to parse showdown options
 * @param {{}} configOptions
 * @param {{}} defaultOptions
 * @returns {{}}
 */
function parseShowdownOptions (configOptions, defaultOptions) {
  'use strict';
  var shOpt = defaultOptions;

  // first prepare passed options
  if (configOptions) {
    for (var i = 0; i < configOptions.length; ++i) {
      var opt = configOptions[i],
          key = configOptions[i],
          val = true;
      if (/=/.test(opt)) {
        key = opt.split('=')[0];
        val = opt.split('=')[1];
      }
      shOpt[key] = val;
    }
  }
  return shOpt;
}

/**
 * Reads stdin
 * @returns {string}
 */
function readFromStdIn (encoding) {
  'use strict';
  /*
  // aparently checking the size of stdin is unreliable so we just won't test
  var size = fs.fstatSync(process.stdin.fd).size;
  if (size <= 0) {
    throw new Error('Could not read from stdin, reason: stdin is empty');
  }
  */
  encoding = encoding || 'utf8';
  try {
    return fs.readFileSync(process.stdin.fd, encoding).toString();
  } catch (e) {
    throw new Error('Could not read from stdin, reason: ' + e.message);
  }
}

/**
 * Reads from a file
 * @param {string} file Filepath to dile
 * @param {string} encoding Encoding of the file
 * @returns {Buffer}
 */
function readFromFile (file, encoding) {
  'use strict';
  try {
    return fs.readFileSync(file, encoding);
  } catch (err) {
    throw new Error('Could not read from file ' + file + ', reason: ' + err.message);
  }
}

/**
 * Writes to stdout
 * @param {string} html
 * @returns {boolean}
 */
function writeToStdOut (html) {
  'use strict';
  if (!process.stdout.write(html)) {
    throw new Error('Could not write to StdOut');
  }
}

/**
 * Writes to file
 * @param {string} html HTML to write
 * @param {string} file Filepath
 * @param {boolean} append If the result should be appended
 */
function writeToFile (html, file, append) {
  'use strict';
  // If a flag is passed, it means we should append instead of overwriting.
  // Only works with files, obviously
  var write = (append) ? fs.appendFileSync : fs.writeFileSync;
  try {
    write(file, html);
  } catch (err) {
    throw new Error('Could not write to file ' + file + ', readon: ' + err.message);
  }
}

/**
 * makehtml command
 * @param {{}} options
 * @param {Command} cmd
 */
function makehtmlCommand (options, cmd) {
  'use strict';

  // show configuration options for showdown helper if configHelp was passed
  if (options.configHelp) {
    showShowdownOptions();
    return;
  }

  var quiet = !!(cmd.parent._optionValues.quiet),
      mute = !!(cmd.parent._optionValues.mute),
      readMode = (!options.input || options.input === '' || options.input === true) ? 'stdin' : 'file',
      writeMode = (!options.output || options.output === '' || options.output === true) ? 'stdout' : 'file',
      msgMode = (writeMode === 'file') ? 'stdout' : 'stderr',
      // initiate Messenger helper, can maybe be replaced with commanderjs internal stuff
      messenger = new Messenger(msgMode, quiet, mute),
      defaultOptions = showdown.getDefaultOptions(true),
      md, html;

  // deal with flavor first since config flag overrides flavor individual options
  if (options.flavor) {
    messenger.printMsg('Enabling flavor ' + options.flavor + '...');
    defaultOptions = showdown.getFlavorOptions(options.flavor);
    if (!defaultOptions) {
      messenger.errorExit(new Error('Flavor ' + options.flavor + ' is not recognised'));
      return;
    }
    messenger.printMsg('OK!');
  }
  // store config options in the options.config as an object
  options.config = parseShowdownOptions(options.config, defaultOptions);

  // print enabled options
  for (var o in options.config) {
    if (options.config.hasOwnProperty(o) && options.config[o] === true) {
      messenger.printMsg('Enabling option ' + o);
    }
  }

  // initialize the converter
  messenger.printMsg('\nInitializing converter...');
  var converter;
  try {
    converter = new showdown.Converter(options.config);
  } catch (e) {
    messenger.errorExit(e);
    return;
  }
  messenger.printMsg('OK!');

  // load extensions
  if (options.extensions) {
    messenger.printMsg('\nLoading extensions...');
    for (var i = 0; i < options.extensions.length; ++i) {
      try {
        messenger.printMsg(options.extensions[i]);
        var ext = require(options.extensions[i]);
        converter.addExtension(ext, options.extensions[i]);
        messenger.printMsg(options.extensions[i] + ' loaded...');
      } catch (e) {
        messenger.printError('ERROR: Could not load extension ' + options.extensions[i] + '. Reason:');
        messenger.errorExit(e);
      }
    }
  }

  messenger.printMsg('...');
  // read the input
  messenger.printMsg('Reading data from ' + readMode + '...');

  if (readMode === 'stdin') {
    try {
      md = readFromStdIn(options.encoding);
    } catch (err) {
      messenger.errorExit(err);
      return;
    }
  } else {
    try {
      md = readFromFile(options.input, options.encoding);
    } catch (err) {
      messenger.errorExit(err);
      return;
    }
  }

  // process the input
  messenger.printMsg('Parsing markdown...');
  html = converter.makeHtml(md);

  // write the output
  messenger.printMsg('Writing data to ' + writeMode + '...');
  if (writeMode === 'stdout') {
    try {
      writeToStdOut(html);
    } catch (err) {
      messenger.errorExit(err);
      return;
    }
  } else {
    try {
      writeToFile(html, options.output, options.append);
    } catch (err) {
      messenger.errorExit(err);
      return;
    }
  }
  messenger.okExit();
}
```

## File: `src/subParsers/makehtml/blockGamut.js`
```javascript
/**
 * These are all the transformations that form block-level
 * tags like paragraphs, headers, and list items.
 */
showdown.subParser('makehtml.blockGamut', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.blockGamut.before', text, options, globals).getText();

  // we parse blockquotes first so that we can have headings and hrs
  // inside blockquotes
  text = showdown.subParser('makehtml.blockQuotes')(text, options, globals);
  text = showdown.subParser('makehtml.headers')(text, options, globals);

  // Do Horizontal Rules:
  text = showdown.subParser('makehtml.horizontalRule')(text, options, globals);

  text = showdown.subParser('makehtml.lists')(text, options, globals);
  text = showdown.subParser('makehtml.codeBlocks')(text, options, globals);
  text = showdown.subParser('makehtml.tables')(text, options, globals);

  // We already ran _HashHTMLBlocks() before, in Markdown(), but that
  // was to escape raw HTML in the original Markdown source. This time,
  // we're escaping the markup we've just created, so that we don't wrap
  // <p> tags around block-level tags.
  text = showdown.subParser('makehtml.hashHTMLBlocks')(text, options, globals);
  text = showdown.subParser('makehtml.paragraphs')(text, options, globals);

  text = globals.converter._dispatch('makehtml.blockGamut.after', text, options, globals).getText();

  return text;
});
```

## File: `src/subParsers/makehtml/blockQuotes.js`
```javascript
showdown.subParser('makehtml.blockQuotes', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.blockQuotes.before', text, options, globals).getText();

  // add a couple extra lines after the text and endtext mark
  text = text + '\n\n';

  var rgx = /(^ {0,3}>[ \t]?.+\n(.+\n)*\n*)+/gm;

  if (options.splitAdjacentBlockquotes) {
    rgx = /^ {0,3}>[\s\S]*?(?:\n\n)/gm;
  }

  text = text.replace(rgx, function (bq) {
    // attacklab: hack around Konqueror 3.5.4 bug:
    // "----------bug".replace(/^-/g,"") == "bug"
    bq = bq.replace(/^[ \t]*>[ \t]?/gm, ''); // trim one level of quoting

    // attacklab: clean up hack
    bq = bq.replace(/¨0/g, '');

    bq = bq.replace(/^[ \t]+$/gm, ''); // trim whitespace-only lines
    bq = showdown.subParser('makehtml.githubCodeBlocks')(bq, options, globals);
    bq = showdown.subParser('makehtml.blockGamut')(bq, options, globals); // recurse

    bq = bq.replace(/(^|\n)/g, '$1  ');
    // These leading spaces screw with <pre> content, so we need to fix that:
    bq = bq.replace(/(\s*<pre>[^\r]+?<\/pre>)/gm, function (wholeMatch, m1) {
      var pre = m1;
      // attacklab: hack around Konqueror 3.5.4 bug:
      pre = pre.replace(/^  /mg, '¨0');
      pre = pre.replace(/¨0/g, '');
      return pre;
    });

    return showdown.subParser('makehtml.hashBlock')('<blockquote>\n' + bq + '\n</blockquote>', options, globals);
  });

  text = globals.converter._dispatch('makehtml.blockQuotes.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/codeBlocks.js`
```javascript
/**
 * Process Markdown `<pre><code>` blocks.
 */
showdown.subParser('makehtml.codeBlocks', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.codeBlocks.before', text, options, globals).getText();

  // sentinel workarounds for lack of \A and \Z, safari\khtml bug
  text += '¨0';

  var pattern = /(?:\n\n|^)((?:(?:[ ]{4}|\t).*\n+)+)(\n*[ ]{0,3}[^ \t\n]|(?=¨0))/g;
  text = text.replace(pattern, function (wholeMatch, m1, m2) {
    var codeblock = m1,
        nextChar = m2,
        end = '\n';

    codeblock = showdown.subParser('makehtml.outdent')(codeblock, options, globals);
    codeblock = showdown.subParser('makehtml.encodeCode')(codeblock, options, globals);
    codeblock = showdown.subParser('makehtml.detab')(codeblock, options, globals);
    codeblock = codeblock.replace(/^\n+/g, ''); // trim leading newlines
    codeblock = codeblock.replace(/\n+$/g, ''); // trim trailing newlines

    if (options.omitExtraWLInCodeBlocks) {
      end = '';
    }

    codeblock = '<pre><code>' + codeblock + end + '</code></pre>';

    return showdown.subParser('makehtml.hashBlock')(codeblock, options, globals) + nextChar;
  });

  // strip sentinel
  text = text.replace(/¨0/, '');

  text = globals.converter._dispatch('makehtml.codeBlocks.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/codeSpans.js`
```javascript
/**
 *
 *   *  Backtick quotes are used for <code></code> spans.
 *
 *   *  You can use multiple backticks as the delimiters if you want to
 *     include literal backticks in the code span. So, this input:
 *
 *         Just type ``foo `bar` baz`` at the prompt.
 *
 *       Will translate to:
 *
 *         <p>Just type <code>foo `bar` baz</code> at the prompt.</p>
 *
 *    There's no arbitrary limit to the number of backticks you
 *    can use as delimters. If you need three consecutive backticks
 *    in your code, use four for delimiters, etc.
 *
 *  *  You can use spaces to get literal backticks at the edges:
 *
 *         ... type `` `bar` `` ...
 *
 *       Turns to:
 *
 *         ... type <code>`bar`</code> ...
 */
showdown.subParser('makehtml.codeSpans', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.codeSpans.before', text, options, globals).getText();

  if (typeof (text) === 'undefined') {
    text = '';
  }
  text = text.replace(/(^|[^\\])(`+)([^\r]*?[^`])\2(?!`)/gm,
    function (wholeMatch, m1, m2, m3) {
      var c = m3;
      c = c.replace(/^([ \t]*)/g, '');	// leading whitespace
      c = c.replace(/[ \t]*$/g, '');	// trailing whitespace
      c = showdown.subParser('makehtml.encodeCode')(c, options, globals);
      c = m1 + '<code>' + c + '</code>';
      c = showdown.subParser('makehtml.hashHTMLSpans')(c, options, globals);
      return c;
    }
  );

  text = globals.converter._dispatch('makehtml.codeSpans.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/completeHTMLDocument.js`
```javascript
/**
 * Create a full HTML document from the processed markdown
 */
showdown.subParser('makehtml.completeHTMLDocument', function (text, options, globals) {
  'use strict';

  if (!options.completeHTMLDocument) {
    return text;
  }

  text = globals.converter._dispatch('makehtml.completeHTMLDocument.before', text, options, globals).getText();

  var doctype = 'html',
      doctypeParsed = '<!DOCTYPE HTML>\n',
      title = '',
      charset = '<meta charset="utf-8">\n',
      lang = '',
      metadata = '';

  if (typeof globals.metadata.parsed.doctype !== 'undefined') {
    doctypeParsed = '<!DOCTYPE ' +  globals.metadata.parsed.doctype + '>\n';
    doctype = globals.metadata.parsed.doctype.toString().toLowerCase();
    if (doctype === 'html' || doctype === 'html5') {
      charset = '<meta charset="utf-8">';
    }
  }

  for (var meta in globals.metadata.parsed) {
    if (globals.metadata.parsed.hasOwnProperty(meta)) {
      switch (meta.toLowerCase()) {
        case 'doctype':
          break;

        case 'title':
          title = '<title>' +  globals.metadata.parsed.title + '</title>\n';
          break;

        case 'charset':
          if (doctype === 'html' || doctype === 'html5') {
            charset = '<meta charset="' + globals.metadata.parsed.charset + '">\n';
          } else {
            charset = '<meta name="charset" content="' + globals.metadata.parsed.charset + '">\n';
          }
          break;

        case 'language':
        case 'lang':
          lang = ' lang="' + globals.metadata.parsed[meta] + '"';
          metadata += '<meta name="' + meta + '" content="' + globals.metadata.parsed[meta] + '">\n';
          break;

        default:
          metadata += '<meta name="' + meta + '" content="' + globals.metadata.parsed[meta] + '">\n';
      }
    }
  }

  text = doctypeParsed + '<html' + lang + '>\n<head>\n' + title + charset + metadata + '</head>\n<body>\n' + text.trim() + '\n</body>\n</html>';

  text = globals.converter._dispatch('makehtml.completeHTMLDocument.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/detab.js`
```javascript
/**
 * Convert all tabs to spaces
 */
showdown.subParser('makehtml.detab', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.detab.before', text, options, globals).getText();

  // expand first n-1 tabs
  text = text.replace(/\t(?=\t)/g, '    '); // g_tab_width

  // replace the nth with two sentinels
  text = text.replace(/\t/g, '¨A¨B');

  // use the sentinel to anchor our regex so it doesn't explode
  text = text.replace(/¨B(.+?)¨A/g, function (wholeMatch, m1) {
    var leadingText = m1,
        numSpaces = 4 - leadingText.length % 4;  // g_tab_width

    // there *must* be a better way to do this:
    for (var i = 0; i < numSpaces; i++) {
      leadingText += ' ';
    }

    return leadingText;
  });

  // clean up sentinels
  text = text.replace(/¨A/g, '    ');  // g_tab_width
  text = text.replace(/¨B/g, '');

  text = globals.converter._dispatch('makehtml.detab.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/ellipsis.js`
```javascript
showdown.subParser('makehtml.ellipsis', function (text, options, globals) {
  'use strict';

  if (!options.ellipsis) {
    return text;
  }

  text = globals.converter._dispatch('makehtml.ellipsis.before', text, options, globals).getText();

  text = text.replace(/\.\.\./g, '…');

  text = globals.converter._dispatch('makehtml.ellipsis.after', text, options, globals).getText();

  return text;
});
```

## File: `src/subParsers/makehtml/emoji.js`
```javascript
/**
 * Turn emoji codes into emojis
 *
 * List of supported emojis: https://github.com/showdownjs/showdown/wiki/Emojis
 */
showdown.subParser('makehtml.emoji', function (text, options, globals) {
  'use strict';

  if (!options.emoji) {
    return text;
  }

  text = globals.converter._dispatch('makehtml.emoji.before', text, options, globals).getText();

  var emojiRgx = /:([\S]+?):/g;

  text = text.replace(emojiRgx, function (wm, emojiCode) {
    if (showdown.helper.emojis.hasOwnProperty(emojiCode)) {
      return showdown.helper.emojis[emojiCode];
    }
    return wm;
  });

  text = globals.converter._dispatch('makehtml.emoji.after', text, options, globals).getText();

  return text;
});
```

## File: `src/subParsers/makehtml/encodeAmpsAndAngles.js`
```javascript
/**
 * Smart processing for ampersands and angle brackets that need to be encoded.
 */
showdown.subParser('makehtml.encodeAmpsAndAngles', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.encodeAmpsAndAngles.before', text, options, globals).getText();

  // Ampersand-encoding based entirely on Nat Irons's Amputator MT plugin:
  // http://bumppo.net/projects/amputator/
  text = text.replace(/&(?!#?[xX]?(?:[0-9a-fA-F]+|\w+);)/g, '&amp;');

  // Encode naked <'s
  text = text.replace(/<(?![a-z\/?$!])/gi, '&lt;');

  // Encode <
  text = text.replace(/</g, '&lt;');

  // Encode >
  text = text.replace(/>/g, '&gt;');

  text = globals.converter._dispatch('makehtml.encodeAmpsAndAngles.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/encodeBackslashEscapes.js`
```javascript
/**
 * Returns the string, with after processing the following backslash escape sequences.
 *
 * attacklab: The polite way to do this is with the new escapeCharacters() function:
 *
 *    text = escapeCharacters(text,"\\",true);
 *    text = escapeCharacters(text,"`*_{}[]()>#+-.!",true);
 *
 * ...but we're sidestepping its use of the (slow) RegExp constructor
 * as an optimization for Firefox.  This function gets called a LOT.
 */
showdown.subParser('makehtml.encodeBackslashEscapes', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.encodeBackslashEscapes.before', text, options, globals).getText();

  text = text.replace(/\\(\\)/g, showdown.helper.escapeCharactersCallback);
  text = text.replace(/\\([`*_{}\[\]()>#+.!~=|:-])/g, showdown.helper.escapeCharactersCallback);

  text = globals.converter._dispatch('makehtml.encodeBackslashEscapes.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/encodeCode.js`
```javascript
/**
 * Encode/escape certain characters inside Markdown code runs.
 * The point is that in code, these characters are literals,
 * and lose their special Markdown meanings.
 */
showdown.subParser('makehtml.encodeCode', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.encodeCode.before', text, options, globals).getText();

  // Encode all ampersands; HTML entities are not
  // entities within a Markdown code span.
  text = text
    .replace(/&/g, '&amp;')
  // Do the angle bracket song and dance:
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
  // Now, escape characters that are magic in Markdown:
    .replace(/([*_{}\[\]\\=~-])/g, showdown.helper.escapeCharactersCallback);

  text = globals.converter._dispatch('makehtml.encodeCode.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/escapeSpecialCharsWithinTagAttributes.js`
```javascript
/**
 * Within tags -- meaning between < and > -- encode [\ ` * _ ~ =] so they
 * don't conflict with their use in Markdown for code, italics and strong.
 */
showdown.subParser('makehtml.escapeSpecialCharsWithinTagAttributes', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.escapeSpecialCharsWithinTagAttributes.before', text, options, globals).getText();

  // Build a regex to find HTML tags.
  var tags     = /<\/?[a-z\d_:-]+(?:[\s]+[\s\S]+?)?>/gi,
      comments = /<!(--(?:(?:[^>-]|-[^>])(?:[^-]|-[^-])*)--)>/gi;

  text = text.replace(tags, function (wholeMatch) {
    return wholeMatch
      .replace(/(.)<\/?code>(?=.)/g, '$1`')
      .replace(/([\\`*_~=|])/g, showdown.helper.escapeCharactersCallback);
  });

  text = text.replace(comments, function (wholeMatch) {
    return wholeMatch
      .replace(/([\\`*_~=|])/g, showdown.helper.escapeCharactersCallback);
  });

  text = globals.converter._dispatch('makehtml.escapeSpecialCharsWithinTagAttributes.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/githubCodeBlocks.js`
```javascript
/**
 * Handle github codeblocks prior to running HashHTML so that
 * HTML contained within the codeblock gets escaped properly
 * Example:
 * ```ruby
 *     def hello_world(x)
 *       puts "Hello, #{x}"
 *     end
 * ```
 */
showdown.subParser('makehtml.githubCodeBlocks', function (text, options, globals) {
  'use strict';

  // early exit if option is not enabled
  if (!options.ghCodeBlocks) {
    return text;
  }

  text = globals.converter._dispatch('makehtml.githubCodeBlocks.before', text, options, globals).getText();

  text += '¨0';

  text = text.replace(/(?:^|\n) {0,3}(```+|~~~+) *([^\n\t`~]*)\n([\s\S]*?)\n {0,3}\1/g, function (wholeMatch, delim, language, codeblock) {
    var end = (options.omitExtraWLInCodeBlocks) ? '' : '\n';

    // if the language has spaces followed by some other chars, according to the spec we should just ignore everything
    // after the first space
    language = language.trim().split(' ')[0];

    // First parse the github code block
    codeblock = showdown.subParser('makehtml.encodeCode')(codeblock, options, globals);
    codeblock = showdown.subParser('makehtml.detab')(codeblock, options, globals);
    codeblock = codeblock.replace(/^\n+/g, ''); // trim leading newlines
    codeblock = codeblock.replace(/\n+$/g, ''); // trim trailing whitespace

    codeblock = '<pre><code' + (language ? ' class="' + language + ' language-' + language + '"' : '') + '>' + codeblock + end + '</code></pre>';

    codeblock = showdown.subParser('makehtml.hashBlock')(codeblock, options, globals);

    // Since GHCodeblocks can be false positives, we need to
    // store the primitive text and the parsed text in a global var,
    // and then return a token
    return '\n\n¨G' + (globals.ghCodeBlocks.push({text: wholeMatch, codeblock: codeblock}) - 1) + 'G\n\n';
  });

  // attacklab: strip sentinel
  text = text.replace(/¨0/, '');

  return globals.converter._dispatch('makehtml.githubCodeBlocks.after', text, options, globals).getText();
});
```

## File: `src/subParsers/makehtml/hashBlock.js`
```javascript
showdown.subParser('makehtml.hashBlock', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.hashBlock.before', text, options, globals).getText();
  text = text.replace(/(^\n+|\n+$)/g, '');
  text = '\n\n¨K' + (globals.gHtmlBlocks.push(text) - 1) + 'K\n\n';
  text = globals.converter._dispatch('makehtml.hashBlock.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/hashCodeTags.js`
```javascript
/**
 * Hash and escape <code> elements that should not be parsed as markdown
 */
showdown.subParser('makehtml.hashCodeTags', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.hashCodeTags.before', text, options, globals).getText();

  var repFunc = function (wholeMatch, match, left, right) {
    var codeblock = left + showdown.subParser('makehtml.encodeCode')(match, options, globals) + right;
    return '¨C' + (globals.gHtmlSpans.push(codeblock) - 1) + 'C';
  };

  // Hash naked <code>
  text = showdown.helper.replaceRecursiveRegExp(text, repFunc, '<code\\b[^>]*>', '</code>', 'gim');

  text = globals.converter._dispatch('makehtml.hashCodeTags.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/hashElement.js`
```javascript
showdown.subParser('makehtml.hashElement', function (text, options, globals) {
  'use strict';

  return function (wholeMatch, m1) {
    var blockText = m1;

    // Undo double lines
    blockText = blockText.replace(/\n\n/g, '\n');
    blockText = blockText.replace(/^\n/, '');

    // strip trailing blank lines
    blockText = blockText.replace(/\n+$/g, '');

    // Replace the element text with a marker ("¨KxK" where x is its key)
    blockText = '\n\n¨K' + (globals.gHtmlBlocks.push(blockText) - 1) + 'K\n\n';

    return blockText;
  };
});
```

## File: `src/subParsers/makehtml/hashHTMLBlocks.js`
```javascript
showdown.subParser('makehtml.hashHTMLBlocks', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.hashHTMLBlocks.before', text, options, globals).getText();

  var blockTags = [
        'pre',
        'div',
        'h1',
        'h2',
        'h3',
        'h4',
        'h5',
        'h6',
        'blockquote',
        'table',
        'dl',
        'ol',
        'ul',
        'script',
        'noscript',
        'form',
        'fieldset',
        'iframe',
        'math',
        'style',
        'section',
        'header',
        'footer',
        'nav',
        'article',
        'aside',
        'address',
        'audio',
        'canvas',
        'figure',
        'hgroup',
        'output',
        'video',
        'details',
        'p'
      ],
      repFunc = function (wholeMatch, match, left, right) {
        var txt = wholeMatch;
        // check if this html element is marked as markdown
        // if so, it's contents should be parsed as markdown
        if (left.search(/\bmarkdown\b/) !== -1) {
          txt = left + globals.converter.makeHtml(match) + right;
        }
        return '\n\n¨K' + (globals.gHtmlBlocks.push(txt) - 1) + 'K\n\n';
      };

  if (options.backslashEscapesHTMLTags) {
    // encode backslash escaped HTML tags
    text = text.replace(/\\<(\/?[^>]+?)>/g, function (wm, inside) {
      return '&lt;' + inside + '&gt;';
    });
  }

  // hash HTML Blocks
  for (var i = 0; i < blockTags.length; ++i) {

    var opTagPos,
        rgx1     = new RegExp('^ {0,3}(<' + blockTags[i] + '\\b[^>]*>)', 'im'),
        patLeft  = '<' + blockTags[i] + '\\b[^>]*>',
        patRight = '</' + blockTags[i] + '>';
    // 1. Look for the first position of the first opening HTML tag in the text
    while ((opTagPos = showdown.helper.regexIndexOf(text, rgx1)) !== -1) {

      // if the HTML tag is \ escaped, we need to escape it and break


      //2. Split the text in that position
      var subTexts = showdown.helper.splitAtIndex(text, opTagPos),
          //3. Match recursively
          newSubText1 = showdown.helper.replaceRecursiveRegExp(subTexts[1], repFunc, patLeft, patRight, 'im');

      // prevent an infinite loop
      if (newSubText1 === subTexts[1]) {
        break;
      }
      text = subTexts[0].concat(newSubText1);
    }
  }
  // HR SPECIAL CASE
  text = text.replace(/(\n {0,3}(<(hr)\b([^<>])*?\/?>)[ \t]*(?=\n{2,}))/g,
    showdown.subParser('makehtml.hashElement')(text, options, globals));

  // Special case for standalone HTML comments
  text = showdown.helper.replaceRecursiveRegExp(text, function (txt) {
    return '\n\n¨K' + (globals.gHtmlBlocks.push(txt) - 1) + 'K\n\n';
  }, '^ {0,3}<!--', '-->', 'gm');

  // PHP and ASP-style processor instructions (<?...?> and <%...%>)
  text = text.replace(/\n\n( {0,3}<([?%])[^\r]*?\2>[ \t]*(?=\n{2,}))/g,
    showdown.subParser('makehtml.hashElement')(text, options, globals));

  text = globals.converter._dispatch('makehtml.hashHTMLBlocks.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/hashHTMLSpans.js`
```javascript
/**
 * Hash span elements that should not be parsed as markdown
 */
showdown.subParser('makehtml.hashHTMLSpans', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.hashHTMLSpans.before', text, options, globals).getText();

  // Hash Self Closing tags
  text = text.replace(/<[^>]+?\/>/gi, function (wm) {
    return showdown.helper._hashHTMLSpan(wm, globals);
  });

  // Hash tags without properties
  text = text.replace(/<([^>]+?)>[\s\S]*?<\/\1>/g, function (wm) {
    return showdown.helper._hashHTMLSpan(wm, globals);
  });

  // Hash tags with properties
  text = text.replace(/<([^>]+?)\s[^>]+?>[\s\S]*?<\/\1>/g, function (wm) {
    return showdown.helper._hashHTMLSpan(wm, globals);
  });

  // Hash self closing tags without />
  text = text.replace(/<[^>]+?>/gi, function (wm) {
    return showdown.helper._hashHTMLSpan(wm, globals);
  });

  text = globals.converter._dispatch('makehtml.hashHTMLSpans.after', text, options, globals).getText();
  return text;
});

/**
 * Unhash HTML spans
 */
showdown.subParser('makehtml.unhashHTMLSpans', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.unhashHTMLSpans.before', text, options, globals).getText();

  for (var i = 0; i < globals.gHtmlSpans.length; ++i) {
    var repText = globals.gHtmlSpans[i],
        // limiter to prevent infinite loop (assume 10 as limit for recurse)
        limit = 0;

    while (/¨C(\d+)C/.test(repText)) {
      var num = RegExp.$1;
      repText = repText.replace('¨C' + num + 'C', globals.gHtmlSpans[num]);
      if (limit === 10) {
        console.error('maximum nesting of 10 spans reached!!!');
        break;
      }
      ++limit;
    }
    text = text.replace('¨C' + i + 'C', repText);
  }

  text = globals.converter._dispatch('makehtml.unhashHTMLSpans.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/hashPreCodeTags.js`
```javascript
/**
 * Hash and escape <pre><code> elements that should not be parsed as markdown
 */
showdown.subParser('makehtml.hashPreCodeTags', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.hashPreCodeTags.before', text, options, globals).getText();

  var repFunc = function (wholeMatch, match, left, right) {
    // encode html entities
    var codeblock = left + showdown.subParser('makehtml.encodeCode')(match, options, globals) + right;
    return '\n\n¨G' + (globals.ghCodeBlocks.push({text: wholeMatch, codeblock: codeblock}) - 1) + 'G\n\n';
  };

  // Hash <pre><code>
  text = showdown.helper.replaceRecursiveRegExp(text, repFunc, '^ {0,3}<pre\\b[^>]*>\\s*<code\\b[^>]*>', '^ {0,3}</code>\\s*</pre>', 'gim');

  text = globals.converter._dispatch('makehtml.hashPreCodeTags.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/headers.js`
```javascript
showdown.subParser('makehtml.headers', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.headers.before', text, options, globals).getText();

  var headerLevelStart = (isNaN(parseInt(options.headerLevelStart))) ? 1 : parseInt(options.headerLevelStart),

      // Set text-style headers:
      //	Header 1
      //	========
      //
      //	Header 2
      //	--------
      //
      setextRegexH1 = (options.smoothLivePreview) ? /^(.+)[ \t]*\n={2,}[ \t]*\n+/gm : /^(.+)[ \t]*\n=+[ \t]*\n+/gm,
      setextRegexH2 = (options.smoothLivePreview) ? /^(.+)[ \t]*\n-{2,}[ \t]*\n+/gm : /^(.+)[ \t]*\n-+[ \t]*\n+/gm;

  text = text.replace(setextRegexH1, function (wholeMatch, m1) {

    var spanGamut = showdown.subParser('makehtml.spanGamut')(m1, options, globals),
        hID = (options.noHeaderId) ? '' : ' id="' + headerId(m1) + '"',
        hLevel = headerLevelStart,
        hashBlock = '<h' + hLevel + hID + '>' + spanGamut + '</h' + hLevel + '>';
    return showdown.subParser('makehtml.hashBlock')(hashBlock, options, globals);
  });

  text = text.replace(setextRegexH2, function (matchFound, m1) {
    var spanGamut = showdown.subParser('makehtml.spanGamut')(m1, options, globals),
        hID = (options.noHeaderId) ? '' : ' id="' + headerId(m1) + '"',
        hLevel = headerLevelStart + 1,
        hashBlock = '<h' + hLevel + hID + '>' + spanGamut + '</h' + hLevel + '>';
    return showdown.subParser('makehtml.hashBlock')(hashBlock, options, globals);
  });

  // atx-style headers:
  //  # Header 1
  //  ## Header 2
  //  ## Header 2 with closing hashes ##
  //  ...
  //  ###### Header 6
  //
  var atxStyle = (options.requireSpaceBeforeHeadingText) ? /^(#{1,6})[ \t]+(.+?)[ \t]*#*\n+/gm : /^(#{1,6})[ \t]*(.+?)[ \t]*#*\n+/gm;

  text = text.replace(atxStyle, function (wholeMatch, m1, m2) {
    var hText = m2;
    if (options.customizedHeaderId) {
      hText = m2.replace(/\s?{([^{]+?)}\s*$/, '');
    }

    var span = showdown.subParser('makehtml.spanGamut')(hText, options, globals),
        hID = (options.noHeaderId) ? '' : ' id="' + headerId(m2) + '"',
        hLevel = headerLevelStart - 1 + m1.length,
        header = '<h' + hLevel + hID + '>' + span + '</h' + hLevel + '>';

    return showdown.subParser('makehtml.hashBlock')(header, options, globals);
  });

  function headerId (m) {
    var title,
        prefix;

    // It is separate from other options to allow combining prefix and customized
    if (options.customizedHeaderId) {
      var match = m.match(/{([^{]+?)}\s*$/);
      if (match && match[1]) {
        m = match[1];
      }
    }

    title = m;

    // Prefix id to prevent causing inadvertent pre-existing style matches.
    if (showdown.helper.isString(options.prefixHeaderId)) {
      prefix = options.prefixHeaderId;
    } else if (options.prefixHeaderId === true) {
      prefix = 'section-';
    } else {
      prefix = '';
    }

    if (!options.rawPrefixHeaderId) {
      title = prefix + title;
    }

    if (options.ghCompatibleHeaderId) {
      title = title
        .replace(/ /g, '-')
        // replace previously escaped chars (&, ¨ and $)
        .replace(/&amp;/g, '')
        .replace(/¨T/g, '')
        .replace(/¨D/g, '')
        // replace rest of the chars (&~$ are repeated as they might have been escaped)
        // borrowed from github's redcarpet (some they should produce similar results)
        .replace(/[&+$,\/:;=?@"#{}|^¨~\[\]`\\*)(%.!'<>]/g, '')
        .toLowerCase();
    } else if (options.rawHeaderId) {
      title = title
        .replace(/ /g, '-')
        // replace previously escaped chars (&, ¨ and $)
        .replace(/&amp;/g, '&')
        .replace(/¨T/g, '¨')
        .replace(/¨D/g, '$')
        // replace " and '
        .replace(/["']/g, '-')
        .toLowerCase();
    } else {
      title = title
        .replace(/[^\w]/g, '')
        .toLowerCase();
    }

    if (options.rawPrefixHeaderId) {
      title = prefix + title;
    }

    if (globals.hashLinkCounts[title]) {
      title = title + '-' + (globals.hashLinkCounts[title]++);
    } else {
      globals.hashLinkCounts[title] = 1;
    }
    return title;
  }

  text = globals.converter._dispatch('makehtml.headers.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/horizontalRule.js`
```javascript
/**
 * Turn Markdown horizontal rule shortcuts into <hr /> tags.
 *
 * Any 3 or more unindented consecutive hyphens, asterisks or underscores with or without a space beetween them
 * in a single line is considered a horizontal rule
 */
showdown.subParser('makehtml.horizontalRule', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.horizontalRule.before', text, options, globals).getText();

  var key = showdown.subParser('makehtml.hashBlock')('<hr />', options, globals);
  text = text.replace(/^ {0,2}( ?-){3,}[ \t]*$/gm, key);
  text = text.replace(/^ {0,2}( ?\*){3,}[ \t]*$/gm, key);
  text = text.replace(/^ {0,2}( ?_){3,}[ \t]*$/gm, key);

  text = globals.converter._dispatch('makehtml.horizontalRule.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/images.js`
```javascript
/**
 * Turn Markdown image shortcuts into <img> tags.
 */
showdown.subParser('makehtml.images', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.images.before', text, options, globals).getText();

  var inlineRegExp      = /!\[([^\]]*?)][ \t]*()\([ \t]?<?([\S]+?(?:\([\S]*?\)[\S]*?)?)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*(?:(["'])([^"]*?)\6)?[ \t]?\)/g,
      crazyRegExp       = /!\[([^\]]*?)][ \t]*()\([ \t]?<([^>]*)>(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*(?:(?:(["'])([^"]*?)\6))?[ \t]?\)/g,
      base64RegExp      = /!\[([^\]]*?)][ \t]*()\([ \t]?<?(data:.+?\/.+?;base64,[A-Za-z0-9+/=\n]+?)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*(?:(["'])([^"]*?)\6)?[ \t]?\)/g,
      referenceRegExp   = /!\[([^\]]*?)] ?(?:\n *)?\[([\s\S]*?)]()()()()()/g,
      refShortcutRegExp = /!\[([^\[\]]+)]()()()()()/g;

  function writeImageTagBase64 (wholeMatch, altText, linkId, url, width, height, m5, title) {
    url = url.replace(/\s/g, '');
    return writeImageTag (wholeMatch, altText, linkId, url, width, height, m5, title);
  }

  function writeImageTagBaseUrl (wholeMatch, altText, linkId, url, width, height, m5, title) {
    url = showdown.helper.applyBaseUrl(options.relativePathBaseUrl, url);

    return writeImageTag (wholeMatch, altText, linkId, url, width, height, m5, title);
  }

  function writeImageTag (wholeMatch, altText, linkId, url, width, height, m5, title) {

    var gUrls   = globals.gUrls,
        gTitles = globals.gTitles,
        gDims   = globals.gDimensions;

    linkId = linkId.toLowerCase();

    if (!title) {
      title = '';
    }
    // Special case for explicit empty url
    if (wholeMatch.search(/\(<?\s*>? ?(['"].*['"])?\)$/m) > -1) {
      url = '';

    } else if (url === '' || url === null) {
      if (linkId === '' || linkId === null) {
        // lower-case and turn embedded newlines into spaces
        linkId = altText.toLowerCase().replace(/ ?\n/g, ' ');
      }
      url = '#' + linkId;

      if (!showdown.helper.isUndefined(gUrls[linkId])) {
        url = gUrls[linkId];
        if (!showdown.helper.isUndefined(gTitles[linkId])) {
          title = gTitles[linkId];
        }
        if (!showdown.helper.isUndefined(gDims[linkId])) {
          width = gDims[linkId].width;
          height = gDims[linkId].height;
        }
      } else {
        return wholeMatch;
      }
    }

    altText = altText
      .replace(/"/g, '&quot;')
    //altText = showdown.helper.escapeCharacters(altText, '*_', false);
      .replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);
    //url = showdown.helper.escapeCharacters(url, '*_', false);
    url = url.replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);
    var result = '<img src="' + url + '" alt="' + altText + '"';

    if (title && showdown.helper.isString(title)) {
      title = title
        .replace(/"/g, '&quot;')
      //title = showdown.helper.escapeCharacters(title, '*_', false);
        .replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);
      result += ' title="' + title + '"';
    }

    if (width && height) {
      width  = (width === '*') ? 'auto' : width;
      height = (height === '*') ? 'auto' : height;

      result += ' width="' + width + '"';
      result += ' height="' + height + '"';
    }

    result += ' />';

    return result;
  }

  // First, handle reference-style labeled images: ![alt text][id]
  text = text.replace(referenceRegExp, writeImageTag);

  // Next, handle inline images:  ![alt text](url =<width>x<height> "optional title")

  // base64 encoded images
  text = text.replace(base64RegExp, writeImageTagBase64);

  // cases with crazy urls like ./image/cat1).png
  text = text.replace(crazyRegExp, writeImageTagBaseUrl);

  // normal cases
  text = text.replace(inlineRegExp, writeImageTagBaseUrl);

  // handle reference-style shortcuts: ![img text]
  text = text.replace(refShortcutRegExp, writeImageTag);

  text = globals.converter._dispatch('makehtml.images.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/italicsAndBold.js`
```javascript
showdown.subParser('makehtml.italicsAndBold', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.italicsAndBold.before', text, options, globals).getText();

  // it's faster to have 3 separate regexes for each case than have just one
  // because of backtracing, in some cases, it could lead to an exponential effect
  // called "catastrophic backtrace". Ominous!

  function parseInside (txt, left, right) {
    return left + txt + right;
  }

  // Parse underscores
  if (options.literalMidWordUnderscores) {
    text = text.replace(/\b___(\S[\s\S]*?)___\b/g, function (wm, txt) {
      return parseInside (txt, '<strong><em>', '</em></strong>');
    });
    text = text.replace(/\b__(\S[\s\S]*?)__\b/g, function (wm, txt) {
      return parseInside (txt, '<strong>', '</strong>');
    });
    text = text.replace(/\b_(\S[\s\S]*?)_\b/g, function (wm, txt) {
      return parseInside (txt, '<em>', '</em>');
    });
  } else {
    text = text.replace(/___(\S[\s\S]*?)___/g, function (wm, m) {
      return (/\S$/.test(m)) ? parseInside (m, '<strong><em>', '</em></strong>') : wm;
    });
    text = text.replace(/__(\S[\s\S]*?)__/g, function (wm, m) {
      return (/\S$/.test(m)) ? parseInside (m, '<strong>', '</strong>') : wm;
    });
    text = text.replace(/_([^\s_][\s\S]*?)_/g, function (wm, m) {
      // !/^_[^_]/.test(m) - test if it doesn't start with __ (since it seems redundant, we removed it)
      return (/\S$/.test(m)) ? parseInside (m, '<em>', '</em>') : wm;
    });
  }

  // Now parse asterisks
  /*
  if (options.literalMidWordAsterisks) {
    text = text.replace(/([^*]|^)\B\*\*\*(\S[\s\S]+?)\*\*\*\B(?!\*)/g, function (wm, lead, txt) {
      return parseInside (txt, lead + '<strong><em>', '</em></strong>');
    });
    text = text.replace(/([^*]|^)\B\*\*(\S[\s\S]+?)\*\*\B(?!\*)/g, function (wm, lead, txt) {
      return parseInside (txt, lead + '<strong>', '</strong>');
    });
    text = text.replace(/([^*]|^)\B\*(\S[\s\S]+?)\*\B(?!\*)/g, function (wm, lead, txt) {
      return parseInside (txt, lead + '<em>', '</em>');
    });
  } else {
  */
  text = text.replace(/\*\*\*(\S[\s\S]*?)\*\*\*/g, function (wm, m) {
    return (/\S$/.test(m)) ? parseInside (m, '<strong><em>', '</em></strong>') : wm;
  });
  text = text.replace(/\*\*(\S[\s\S]*?)\*\*/g, function (wm, m) {
    return (/\S$/.test(m)) ? parseInside (m, '<strong>', '</strong>') : wm;
  });
  text = text.replace(/\*([^\s*][\s\S]*?)\*/g, function (wm, m) {
    // !/^\*[^*]/.test(m) - test if it doesn't start with ** (since it seems redundant, we removed it)
    return (/\S$/.test(m)) ? parseInside (m, '<em>', '</em>') : wm;
  });
  //}

  text = globals.converter._dispatch('makehtml.italicsAndBold.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/links.js`
```javascript
////
// makehtml/links.js
// Copyright (c) 2018 ShowdownJS
//
// Transforms MD links into `<a>` html anchors
//
// A link contains link text (the visible text), a link destination (the URI that is the link destination), and
// optionally a link title. There are two basic kinds of links in Markdown.
// In inline links the destination and title are given immediately after the link text.
// In reference links the destination and title are defined elsewhere in the document.
//
// ***Author:***
// - Estevão Soares dos Santos (Tivie) <https://github.com/tivie>
////

(function () {
  /**
   * Helper function: Wrapper function to pass as second replace parameter
   *
   * @param {RegExp} rgx
   * @param {string} evtRootName
   * @param {{}} options
   * @param {{}} globals
   * @returns {Function}
   */
  function replaceAnchorTagReference (rgx, evtRootName, options, globals, emptyCase) {
    emptyCase = !!emptyCase;
    return function (wholeMatch, text, id, url, m5, m6, title) {
      // bail we we find 2 newlines somewhere
      if (/\n\n/.test(wholeMatch)) {
        return wholeMatch;
      }

      var evt = createEvent(rgx, evtRootName + '.captureStart', wholeMatch, text, id, url, title, options, globals);
      return writeAnchorTag(evt, options, globals, emptyCase);
    };
  }

  function replaceAnchorTagBaseUrl (rgx, evtRootName, options, globals, emptyCase) {
    return function (wholeMatch, text, id, url, m5, m6, title) {
      url = showdown.helper.applyBaseUrl(options.relativePathBaseUrl, url);

      var evt = createEvent(rgx, evtRootName + '.captureStart', wholeMatch, text, id, url, title, options, globals);
      return writeAnchorTag(evt, options, globals, emptyCase);
    };
  }

  /**
   * TODO Normalize this
   * Helper function: Create a capture event
   * @param {RegExp} rgx
   * @param {String} evtName Event name
   * @param {String} wholeMatch
   * @param {String} text
   * @param {String} id
   * @param {String} url
   * @param {String} title
   * @param {{}} options
   * @param {{}} globals
   * @returns {showdown.helper.Event|*}
   */
  function createEvent (rgx, evtName, wholeMatch, text, id, url, title, options, globals) {
    return globals.converter._dispatch(evtName, wholeMatch, options, globals, {
      regexp: rgx,
      matches: {
        wholeMatch: wholeMatch,
        text: text,
        id: id,
        url: url,
        title: title
      }
    });
  }

  /**
   * Helper Function: Normalize and write an anchor tag based on passed parameters
   * @param evt
   * @param options
   * @param globals
   * @param {boolean} emptyCase
   * @returns {string}
   */
  function writeAnchorTag (evt, options, globals, emptyCase) {

    var wholeMatch = evt.getMatches().wholeMatch;
    var text = evt.getMatches().text;
    var id = evt.getMatches().id;
    var url = evt.getMatches().url;
    var title = evt.getMatches().title;
    var target = '';

    if (!title) {
      title = '';
    }
    id = (id) ? id.toLowerCase() : '';

    if (emptyCase) {
      url = '';
    } else if (!url) {
      if (!id) {
        // lower-case and turn embedded newlines into spaces
        id = text.toLowerCase().replace(/ ?\n/g, ' ');
      }
      url = '#' + id;

      if (!showdown.helper.isUndefined(globals.gUrls[id])) {
        url = globals.gUrls[id];
        if (!showdown.helper.isUndefined(globals.gTitles[id])) {
          title = globals.gTitles[id];
        }
      } else {
        return wholeMatch;
      }
    }
    //url = showdown.helper.escapeCharacters(url, '*_:~', false); // replaced line to improve performance
    url = url.replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);

    if (title !== '' && title !== null) {
      title = title.replace(/"/g, '&quot;');
      //title = showdown.helper.escapeCharacters(title, '*_', false); // replaced line to improve performance
      title = title.replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);
      title = ' title="' + title + '"';
    }

    // optionLinksInNewWindow only applies
    // to external links. Hash links (#) open in same page
    if (options.openLinksInNewWindow && !/^#/.test(url)) {
      // escaped _
      target = ' rel="noopener noreferrer" target="¨E95Eblank"';
    }

    // Text can be a markdown element, so we run through the appropriate parsers
    text = showdown.subParser('makehtml.codeSpans')(text, options, globals);
    text = showdown.subParser('makehtml.emoji')(text, options, globals);
    text = showdown.subParser('makehtml.underline')(text, options, globals);
    text = showdown.subParser('makehtml.italicsAndBold')(text, options, globals);
    text = showdown.subParser('makehtml.strikethrough')(text, options, globals);
    text = showdown.subParser('makehtml.ellipsis')(text, options, globals);
    text = showdown.subParser('makehtml.hashHTMLSpans')(text, options, globals);

    //evt = createEvent(rgx, evtRootName + '.captureEnd', wholeMatch, text, id, url, title, options, globals);

    var result = '<a href="' + url + '"' + title + target + '>' + text + '</a>';

    //evt = createEvent(rgx, evtRootName + '.beforeHash', wholeMatch, text, id, url, title, options, globals);

    result = showdown.subParser('makehtml.hashHTMLSpans')(result, options, globals);

    return result;
  }

  var evtRootName = 'makehtml.links';

  /**
   * Turn Markdown link shortcuts into XHTML <a> tags.
   */
  showdown.subParser('makehtml.links', function (text, options, globals) {

    text = globals.converter._dispatch(evtRootName + '.start', text, options, globals).getText();

    // 1. Handle reference-style links: [link text] [id]
    text = showdown.subParser('makehtml.links.reference')(text, options, globals);

    // 2. Handle inline-style links: [link text](url "optional title")
    text = showdown.subParser('makehtml.links.inline')(text, options, globals);

    // 3. Handle reference-style shortcuts: [link text]
    // These must come last in case there's a [link text][1] or [link text](/foo)
    text = showdown.subParser('makehtml.links.referenceShortcut')(text, options, globals);

    // 4. Handle angle brackets links -> `<http://example.com/>`
    // Must come after links, because you can use < and > delimiters in inline links like [this](<url>).
    text = showdown.subParser('makehtml.links.angleBrackets')(text, options, globals);

    // 5. Handle GithubMentions (if option is enabled)
    text = showdown.subParser('makehtml.links.ghMentions')(text, options, globals);

    // 6. Handle <a> tags and img tags
    text = text.replace(/<a\s[^>]*>[\s\S]*<\/a>/g, function (wholeMatch) {
      return showdown.helper._hashHTMLSpan(wholeMatch, globals);
    });

    text = text.replace(/<img\s[^>]*\/?>/g, function (wholeMatch) {
      return showdown.helper._hashHTMLSpan(wholeMatch, globals);
    });

    // 7. Handle naked links (if option is enabled)
    text = showdown.subParser('makehtml.links.naked')(text, options, globals);

    text = globals.converter._dispatch(evtRootName + '.end', text, options, globals).getText();
    return text;
  });

  /**
   * TODO WRITE THIS DOCUMENTATION
   */
  showdown.subParser('makehtml.links.inline', function (text, options, globals) {
    var evtRootName = evtRootName + '.inline';

    text = globals.converter._dispatch(evtRootName + '.start', text, options, globals).getText();

    // 1. Look for empty cases: []() and [empty]() and []("title")
    var rgxEmpty = /\[(.*?)]()()()()\(<? ?>? ?(?:["'](.*)["'])?\)/g;
    text = text.replace(rgxEmpty, replaceAnchorTagBaseUrl(rgxEmpty, evtRootName, options, globals, true));

    // 2. Look for cases with crazy urls like ./image/cat1).png
    var rgxCrazy = /\[((?:\[[^\]]*]|[^\[\]])*)]()\s?\([ \t]?<([^>]*)>(?:[ \t]*((["'])([^"]*?)\5))?[ \t]?\)/g;
    text = text.replace(rgxCrazy, replaceAnchorTagBaseUrl(rgxCrazy, evtRootName, options, globals));

    // 3. inline links with no title or titles wrapped in ' or ":
    // [text](url.com) || [text](<url.com>) || [text](url.com "title") || [text](<url.com> "title")
    //var rgx2 = /\[[ ]*[\s]?[ ]*([^\n\[\]]*?)[ ]*[\s]?[ ]*] ?()\(<?[ ]*[\s]?[ ]*([^\s'"]*)>?(?:[ ]*[\n]?[ ]*()(['"])(.*?)\5)?[ ]*[\s]?[ ]*\)/; // this regex is too slow!!!
    var rgx2 = /\[([\S ]*?)]\s?()\( *<?([^\s'"]*?(?:\([\S]*?\)[\S]*?)?)>?\s*(?:()(['"])(.*?)\5)? *\)/g;
    text = text.replace(rgx2, replaceAnchorTagBaseUrl(rgx2, evtRootName, options, globals));

    // 4. inline links with titles wrapped in (): [foo](bar.com (title))
    var rgx3 = /\[([\S ]*?)]\s?()\( *<?([^\s'"]*?(?:\([\S]*?\)[\S]*?)?)>?\s+()()\((.*?)\) *\)/g;
    text = text.replace(rgx3, replaceAnchorTagBaseUrl(rgx3, evtRootName, options, globals));

    text = globals.converter._dispatch(evtRootName + '.end', text, options, globals).getText();

    return text;
  });

  /**
   * TODO WRITE THIS DOCUMENTATION
   */
  showdown.subParser('makehtml.links.reference', function (text, options, globals) {
    var evtRootName = evtRootName + '.reference';

    text = globals.converter._dispatch(evtRootName + '.start', text, options, globals).getText();

    var rgx = /\[((?:\[[^\]]*]|[^\[\]])*)] ?(?:\n *)?\[(.*?)]()()()()/g;
    text = text.replace(rgx, replaceAnchorTagReference(rgx, evtRootName, options, globals));

    text = globals.converter._dispatch(evtRootName + '.end', text, options, globals).getText();

    return text;
  });

  /**
   * TODO WRITE THIS DOCUMENTATION
   */
  showdown.subParser('makehtml.links.referenceShortcut', function (text, options, globals) {
    var evtRootName = evtRootName + '.referenceShortcut';

    text = globals.converter._dispatch(evtRootName + '.start', text, options, globals).getText();

    var rgx = /\[([^\[\]]+)]()()()()()/g;
    text = text.replace(rgx, replaceAnchorTagReference(rgx, evtRootName, options, globals));

    text = globals.converter._dispatch(evtRootName + '.end', text, options, globals).getText();

    return text;
  });

  /**
   * TODO WRITE THIS DOCUMENTATION
   */
  showdown.subParser('makehtml.links.ghMentions', function (text, options, globals) {
    var evtRootName = evtRootName + 'ghMentions';

    if (!options.ghMentions) {
      return text;
    }

    text = globals.converter._dispatch(evtRootName + '.start', text, options, globals).getText();

    var rgx = /(^|\s)(\\)?(@([a-z\d]+(?:[a-z\d._-]+?[a-z\d]+)*))/gi;

    text = text.replace(rgx, function (wholeMatch, st, escape, mentions, username) {
      // bail if the mentions was escaped
      if (escape === '\\') {
        return st + mentions;
      }

      // check if options.ghMentionsLink is a string
      // TODO Validation should be done at initialization not at runtime
      if (!showdown.helper.isString(options.ghMentionsLink)) {
        throw new Error('ghMentionsLink option must be a string');
      }
      var url = options.ghMentionsLink.replace(/{u}/g, username);
      var evt = createEvent(rgx, evtRootName + '.captureStart', wholeMatch, mentions, null, url, null, options, globals);
      // captureEnd Event is triggered inside writeAnchorTag function
      return st + writeAnchorTag(evt, options, globals);
    });

    text = globals.converter._dispatch(evtRootName + '.end', text, options, globals).getText();

    return text;
  });

  /**
   * TODO WRITE THIS DOCUMENTATION
   */
  showdown.subParser('makehtml.links.angleBrackets', function (text, options, globals) {
    var evtRootName = 'makehtml.links.angleBrackets';

    text = globals.converter._dispatch(evtRootName + '.start', text, options, globals).getText();

    // 1. Parse links first
    var urlRgx  = /<(((?:https?|ftp):\/\/|www\.)[^'">\s]+)>/gi;
    text = text.replace(urlRgx, function (wholeMatch, url, urlStart) {
      var text = url;
      url = (urlStart === 'www.') ? 'http://' + url : url;
      var evt = createEvent(urlRgx, evtRootName + '.captureStart', wholeMatch, text, null, url, null, options, globals);
      return writeAnchorTag(evt, options, globals);
    });

    // 2. Then Mail Addresses
    var mailRgx = /<(?:mailto:)?([-.\w]+@[-a-z0-9]+(\.[-a-z0-9]+)*\.[a-z]+)>/gi;
    text = text.replace(mailRgx, function (wholeMatch, mail) {
      var url = 'mailto:';
      mail = showdown.subParser('makehtml.unescapeSpecialChars')(mail, options, globals);
      if (options.encodeEmails) {
        url = showdown.helper.encodeEmailAddress(url + mail);
        mail = showdown.helper.encodeEmailAddress(mail);
      } else {
        url = url + mail;
      }
      var evt = createEvent(mailRgx, evtRootName + '.captureStart', wholeMatch, mail, null, url, null, options, globals);
      return writeAnchorTag(evt, options, globals);
    });

    text = globals.converter._dispatch(evtRootName + '.end', text, options, globals).getText();
    return text;
  });

  /**
   * TODO MAKE THIS WORK (IT'S NOT ACTIVATED)
   * TODO WRITE THIS DOCUMENTATION
   */
  showdown.subParser('makehtml.links.naked', function (text, options, globals) {
    if (!options.simplifiedAutoLink) {
      return text;
    }

    var evtRootName = 'makehtml.links.naked';

    text = globals.converter._dispatch(evtRootName + '.start', text, options, globals).getText();

    // 2. Now we check for
    // we also include leading markdown magic chars [_*~] for cases like __https://www.google.com/foobar__
    var urlRgx = /([_*~]*?)(((?:https?|ftp):\/\/|www\.)[^\s<>"'`´.-][^\s<>"'`´]*?\.[a-z\d.]+[^\s<>"']*)\1/gi;
    text = text.replace(urlRgx, function (wholeMatch, leadingMDChars, url, urlPrefix) {

      // we now will start traversing the url from the front to back, looking for punctuation chars [_*~,;:.!?\)\]]
      var len = url.length;
      var suffix = '';
      for (var i = len - 1; i >= 0; --i) {
        var char = url.charAt(i);

        if (/[_*~,;:.!?]/.test(char)) {
          // it's a punctuation char
          // we remove it from the url
          url = url.slice(0, -1);
          // and prepend it to the suffix
          suffix = char + suffix;
        } else if (/\)/.test(char)) {
          var opPar = url.match(/\(/g) || [];
          var clPar = url.match(/\)/g);

          // it's a curved parenthesis so we need to check for "balance" (kinda)
          if (opPar.length < clPar.length) {
            // there are more closing Parenthesis than opening so chop it!!!!!
            url = url.slice(0, -1);
            // and prepend it to the suffix
            suffix = char + suffix;
          } else {
            // it's (kinda) balanced so our work is done
            break;
          }
        } else if (/]/.test(char)) {
          var opPar2 = url.match(/\[/g) || [];
          var clPar2 = url.match(/\]/g);
          // it's a squared parenthesis so we need to check for "balance" (kinda)
          if (opPar2.length < clPar2.length) {
            // there are more closing Parenthesis than opening so chop it!!!!!
            url = url.slice(0, -1);
            // and prepend it to the suffix
            suffix = char + suffix;
          } else {
            // it's (kinda) balanced so our work is done
            break;
          }
        } else {
          // it's not a punctuation or a parenthesis so our work is done
          break;
        }
      }

      // we copy the treated url to the text variable
      var text = url;
      // finally, if it's a www shortcut, we prepend http
      url = (urlPrefix === 'www.') ? 'http://' + url : url;

      // url part is done so let's take care of text now
      // we need to escape the text (because of links such as www.example.com/foo__bar__baz)
      text = text.replace(showdown.helper.regexes.asteriskDashTildeAndColon, showdown.helper.escapeCharactersCallback);

      // finally we dispatch the event
      var evt = createEvent(urlRgx, evtRootName + '.captureStart', wholeMatch, text, null, url, null, options, globals);

      // and return the link tag, with the leadingMDChars and  suffix. The leadingMDChars are added at the end too because
      // we consumed those characters in the regexp
      return leadingMDChars + writeAnchorTag(evt, options, globals) + suffix + leadingMDChars;
    });

    // 2. Then mails
    var mailRgx = /(^|\s)(?:mailto:)?([A-Za-z0-9!#$%&'*+-/=?^_`{|}~.]+@[-a-z0-9]+(\.[-a-z0-9]+)*\.[a-z]+)(?=$|\s)/gmi;
    text = text.replace(mailRgx, function (wholeMatch, leadingChar, mail) {
      var url = 'mailto:';
      mail = showdown.subParser('makehtml.unescapeSpecialChars')(mail, options, globals);
      if (options.encodeEmails) {
        url = showdown.helper.encodeEmailAddress(url + mail);
        mail = showdown.helper.encodeEmailAddress(mail);
      } else {
        url = url + mail;
      }
      var evt = createEvent(mailRgx, evtRootName + '.captureStart', wholeMatch, mail, null, url, null, options, globals);
      return leadingChar + writeAnchorTag(evt, options, globals);
    });


    text = globals.converter._dispatch(evtRootName + '.end', text, options, globals).getText();
    return text;
  });
})();
```

## File: `src/subParsers/makehtml/lists.js`
```javascript
/**
 * Form HTML ordered (numbered) and unordered (bulleted) lists.
 */
showdown.subParser('makehtml.lists', function (text, options, globals) {
  'use strict';

  /**
   * Process the contents of a single ordered or unordered list, splitting it
   * into individual list items.
   * @param {string} listStr
   * @param {boolean} trimTrailing
   * @returns {string}
   */
  function processListItems (listStr, trimTrailing) {
    // The $g_list_level global keeps track of when we're inside a list.
    // Each time we enter a list, we increment it; when we leave a list,
    // we decrement. If it's zero, we're not in a list anymore.
    //
    // We do this because when we're not inside a list, we want to treat
    // something like this:
    //
    //    I recommend upgrading to version
    //    8. Oops, now this line is treated
    //    as a sub-list.
    //
    // As a single paragraph, despite the fact that the second line starts
    // with a digit-period-space sequence.
    //
    // Whereas when we're inside a list (or sub-list), that line will be
    // treated as the start of a sub-list. What a kludge, huh? This is
    // an aspect of Markdown's syntax that's hard to parse perfectly
    // without resorting to mind-reading. Perhaps the solution is to
    // change the syntax rules such that sub-lists must start with a
    // starting cardinal number; e.g. "1." or "a.".
    globals.gListLevel++;

    // trim trailing blank lines:
    listStr = listStr.replace(/\n{2,}$/, '\n');

    // attacklab: add sentinel to emulate \z
    listStr += '¨0';

    var rgx = /(\n)?(^ {0,3})([*+-]|\d+[.])[ \t]+((\[([xX ])])?[ \t]*[^\r]+?(\n{1,2}))(?=\n*(¨0| {0,3}([*+-]|\d+[.])[ \t]+))/gm,
        isParagraphed = (/\n[ \t]*\n(?!¨0)/.test(listStr));

    // Since version 1.5, nesting sublists requires 4 spaces (or 1 tab) indentation,
    // which is a syntax breaking change
    // activating this option reverts to old behavior
    // This will be removed in version 2.0
    if (options.disableForced4SpacesIndentedSublists) {
      rgx = /(\n)?(^ {0,3})([*+-]|\d+[.])[ \t]+((\[([xX ])])?[ \t]*[^\r]+?(\n{1,2}))(?=\n*(¨0|\2([*+-]|\d+[.])[ \t]+))/gm;
    }

    listStr = listStr.replace(rgx, function (wholeMatch, m1, m2, m3, m4, taskbtn, checked) {
      checked = (checked && checked.trim() !== '');

      var item = showdown.subParser('makehtml.outdent')(m4, options, globals),
          bulletStyle = '';

      // Support for github tasklists
      if (taskbtn && options.tasklists) {

        // Style used for tasklist bullets
        bulletStyle = ' class="task-list-item';
        if (options.moreStyling) {bulletStyle +=  checked ? ' task-list-item-complete' : '';}
        bulletStyle += '" style="list-style-type: none;"';

        item = item.replace(/^[ \t]*\[([xX ])?]/m, function () {
          var otp = '<input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;"';
          if (checked) {
            otp += ' checked';
          }
          otp += '>';
          return otp;
        });
      }

      // ISSUE #312
      // This input: - - - a
      // causes trouble to the parser, since it interprets it as:
      // <ul><li><li><li>a</li></li></li></ul>
      // instead of:
      // <ul><li>- - a</li></ul>
      // So, to prevent it, we will put a marker (¨A)in the beginning of the line
      // Kind of hackish/monkey patching, but seems more effective than overcomplicating the list parser
      item = item.replace(/^([-*+]|\d\.)[ \t]+[\S\n ]*/g, function (wm2) {
        return '¨A' + wm2;
      });

      // SPECIAL CASE: a heading followed by a paragraph of text that is not separated by a double newline
      // or/nor indented. ex:
      //
      // - # foo
      // bar is great
      //
      // While this does now follow the spec per se, not allowing for this might cause confusion since
      // header blocks don't need double-newlines after
      if (/^#+.+\n.+/.test(item)) {
        item = item.replace(/^(#+.+)$/m, '$1\n');
      }

      // m1 - Leading line or
      // Has a double return (multi paragraph)
      if (m1 || (item.search(/\n{2,}/) > -1)) {
        item = showdown.subParser('makehtml.githubCodeBlocks')(item, options, globals);
        item = showdown.subParser('makehtml.blockQuotes')(item, options, globals);
        item = showdown.subParser('makehtml.headers')(item, options, globals);
        item = showdown.subParser('makehtml.lists')(item, options, globals);
        item = showdown.subParser('makehtml.codeBlocks')(item, options, globals);
        item = showdown.subParser('makehtml.tables')(item, options, globals);
        item = showdown.subParser('makehtml.hashHTMLBlocks')(item, options, globals);
        //item = showdown.subParser('makehtml.paragraphs')(item, options, globals);

        // TODO: This is a copy of the paragraph parser
        // This is a provisory fix for issue #494
        // For a permanente fix we need to rewrite the paragraph parser, passing the unhashify logic outside
        // so that we can call the paragraph parser without accidently unashifying previously parsed blocks

        // Strip leading and trailing lines:
        item = item.replace(/^\n+/g, '');
        item = item.replace(/\n+$/g, '');

        var grafs = item.split(/\n{2,}/g),
            grafsOut = [],
            end = grafs.length; // Wrap <p> tags

        for (var i = 0; i < end; i++) {
          var str = grafs[i];
          // if this is an HTML marker, copy it
          if (str.search(/¨([KG])(\d+)\1/g) >= 0) {
            grafsOut.push(str);

            // test for presence of characters to prevent empty lines being parsed
            // as paragraphs (resulting in undesired extra empty paragraphs)
          } else if (str.search(/\S/) >= 0) {
            str = showdown.subParser('makehtml.spanGamut')(str, options, globals);
            str = str.replace(/^([ \t]*)/g, '<p>');
            str += '</p>';
            grafsOut.push(str);
          }
        }
        item = grafsOut.join('\n');
        // Strip leading and trailing lines:
        item = item.replace(/^\n+/g, '');
        item = item.replace(/\n+$/g, '');

      } else {

        // Recursion for sub-lists:
        item = showdown.subParser('makehtml.lists')(item, options, globals);
        item = item.replace(/\n$/, ''); // chomp(item)
        item = showdown.subParser('makehtml.hashHTMLBlocks')(item, options, globals);

        // Colapse double linebreaks
        item = item.replace(/\n\n+/g, '\n\n');

        if (isParagraphed) {
          item = showdown.subParser('makehtml.paragraphs')(item, options, globals);
        } else {
          item = showdown.subParser('makehtml.spanGamut')(item, options, globals);
        }
      }

      // now we need to remove the marker (¨A)
      item = item.replace('¨A', '');
      // we can finally wrap the line in list item tags
      item =  '<li' + bulletStyle + '>' + item + '</li>\n';

      return item;
    });

    // attacklab: strip sentinel
    listStr = listStr.replace(/¨0/g, '');

    globals.gListLevel--;

    if (trimTrailing) {
      listStr = listStr.replace(/\s+$/, '');
    }

    return listStr;
  }

  function styleStartNumber (list, listType) {
    // check if ol and starts by a number different than 1
    if (listType === 'ol') {
      var res = list.match(/^ *(\d+)\./);
      if (res && res[1] !== '1') {
        return ' start="' + res[1] + '"';
      }
    }
    return '';
  }

  /**
   * Check and parse consecutive lists (better fix for issue #142)
   * @param {string} list
   * @param {string} listType
   * @param {boolean} trimTrailing
   * @returns {string}
   */
  function parseConsecutiveLists (list, listType, trimTrailing) {
    // check if we caught 2 or more consecutive lists by mistake
    // we use the counterRgx, meaning if listType is UL we look for OL and vice versa
    var olRgx = (options.disableForced4SpacesIndentedSublists) ? /^ ?\d+\.[ \t]/gm : /^ {0,3}\d+\.[ \t]/gm,
        ulRgx = (options.disableForced4SpacesIndentedSublists) ? /^ ?[*+-][ \t]/gm : /^ {0,3}[*+-][ \t]/gm,
        counterRxg = (listType === 'ul') ? olRgx : ulRgx,
        result = '';

    if (list.search(counterRxg) !== -1) {
      (function parseCL (txt) {
        var pos = txt.search(counterRxg),
            style = styleStartNumber(list, listType);
        if (pos !== -1) {
          // slice
          result += '\n\n<' + listType + style + '>\n' + processListItems(txt.slice(0, pos), !!trimTrailing) + '</' + listType + '>\n';

          // invert counterType and listType
          listType = (listType === 'ul') ? 'ol' : 'ul';
          counterRxg = (listType === 'ul') ? olRgx : ulRgx;

          //recurse
          parseCL(txt.slice(pos));
        } else {
          result += '\n\n<' + listType + style + '>\n' + processListItems(txt, !!trimTrailing) + '</' + listType + '>\n';
        }
      })(list);
    } else {
      var style = styleStartNumber(list, listType);
      result = '\n\n<' + listType + style + '>\n' + processListItems(list, !!trimTrailing) + '</' + listType + '>\n';
    }

    return result;
  }

  // Start of list parsing
  var subListRgx = /^(( {0,3}([*+-]|\d+[.])[ \t]+)[^\r]+?(¨0|\n{2,}(?=\S)(?![ \t]*(?:[*+-]|\d+[.])[ \t]+)))/gm;
  var mainListRgx = /(\n\n|^\n?)(( {0,3}([*+-]|\d+[.])[ \t]+)[^\r]+?(¨0|\n{2,}(?=\S)(?![ \t]*(?:[*+-]|\d+[.])[ \t]+)))/gm;

  text = globals.converter._dispatch('lists.before', text, options, globals).getText();
  // add sentinel to hack around khtml/safari bug:
  // http://bugs.webkit.org/show_bug.cgi?id=11231
  text += '¨0';

  if (globals.gListLevel) {
    text = text.replace(subListRgx, function (wholeMatch, list, m2) {
      var listType = (m2.search(/[*+-]/g) > -1) ? 'ul' : 'ol';
      return parseConsecutiveLists(list, listType, true);
    });
  } else {
    text = text.replace(mainListRgx, function (wholeMatch, m1, list, m3) {
      var listType = (m3.search(/[*+-]/g) > -1) ? 'ul' : 'ol';
      return parseConsecutiveLists(list, listType, false);
    });
  }

  // strip sentinel
  text = text.replace(/¨0/, '');
  text = globals.converter._dispatch('makehtml.lists.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/metadata.js`
```javascript
/**
 * Parse metadata at the top of the document
 */
showdown.subParser('makehtml.metadata', function (text, options, globals) {
  'use strict';

  if (!options.metadata) {
    return text;
  }

  text = globals.converter._dispatch('makehtml.metadata.before', text, options, globals).getText();

  function parseMetadataContents (content) {
    // raw is raw so it's not changed in any way
    globals.metadata.raw = content;

    // escape chars forbidden in html attributes
    // double quotes
    content = content
      // ampersand first
      .replace(/&/g, '&amp;')
      // double quotes
      .replace(/"/g, '&quot;');

    // Restore dollar signs and tremas
    content = content
      .replace(/¨D/g, '$$')
      .replace(/¨T/g, '¨');

    content = content.replace(/\n {4}/g, ' ');
    content.replace(/^([\S ]+): +([\s\S]+?)$/gm, function (wm, key, value) {
      globals.metadata.parsed[key] = value;
      return '';
    });
  }

  text = text.replace(/^\s*«««+\s*(\S*?)\n([\s\S]+?)\n»»»+\s*\n/, function (wholematch, format, content) {
    parseMetadataContents(content);
    return '¨M';
  });

  text = text.replace(/^\s*---+\s*(\S*?)\n([\s\S]+?)\n---+\s*\n/, function (wholematch, format, content) {
    if (format) {
      globals.metadata.format = format;
    }
    parseMetadataContents(content);
    return '¨M';
  });

  text = text.replace(/¨M/g, '');

  text = globals.converter._dispatch('makehtml.metadata.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/outdent.js`
```javascript
/**
 * Remove one level of line-leading tabs or spaces
 */
showdown.subParser('makehtml.outdent', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.outdent.before', text, options, globals).getText();

  // attacklab: hack around Konqueror 3.5.4 bug:
  // "----------bug".replace(/^-/g,"") == "bug"
  text = text.replace(/^(\t|[ ]{1,4})/gm, '¨0'); // attacklab: g_tab_width

  // attacklab: clean up hack
  text = text.replace(/¨0/g, '');

  text = globals.converter._dispatch('makehtml.outdent.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/paragraphs.js`
```javascript
/**
 *
 */
showdown.subParser('makehtml.paragraphs', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.paragraphs.before', text, options, globals).getText();
  // Strip leading and trailing lines:
  text = text.replace(/^\n+/g, '');
  text = text.replace(/\n+$/g, '');

  var grafs = text.split(/\n{2,}/g),
      grafsOut = [],
      end = grafs.length; // Wrap <p> tags

  for (var i = 0; i < end; i++) {
    var str = grafs[i];
    // if this is an HTML marker, copy it
    if (str.search(/¨(K|G)(\d+)\1/g) >= 0) {
      grafsOut.push(str);

    // test for presence of characters to prevent empty lines being parsed
    // as paragraphs (resulting in undesired extra empty paragraphs)
    } else if (str.search(/\S/) >= 0) {
      str = showdown.subParser('makehtml.spanGamut')(str, options, globals);
      str = str.replace(/^([ \t]*)/g, '<p>');
      str += '</p>';
      grafsOut.push(str);
    }
  }

  /** Unhashify HTML blocks */
  end = grafsOut.length;
  for (i = 0; i < end; i++) {
    var blockText = '',
        grafsOutIt = grafsOut[i],
        codeFlag = false;
    // if this is a marker for an html block...
    // use RegExp.test instead of string.search because of QML bug
    while (/¨(K|G)(\d+)\1/.test(grafsOutIt)) {
      var delim = RegExp.$1,
          num   = RegExp.$2;

      if (delim === 'K') {
        blockText = globals.gHtmlBlocks[num];
      } else {
        // we need to check if ghBlock is a false positive
        if (codeFlag) {
          // use encoded version of all text
          blockText = showdown.subParser('makehtml.encodeCode')(globals.ghCodeBlocks[num].text, options, globals);
        } else {
          blockText = globals.ghCodeBlocks[num].codeblock;
        }
      }
      blockText = blockText.replace(/\$/g, '$$$$'); // Escape any dollar signs

      grafsOutIt = grafsOutIt.replace(/(\n\n)?¨(K|G)\d+\2(\n\n)?/, blockText);
      // Check if grafsOutIt is a pre->code
      if (/^<pre\b[^>]*>\s*<code\b[^>]*>/.test(grafsOutIt)) {
        codeFlag = true;
      }
    }
    grafsOut[i] = grafsOutIt;
  }
  text = grafsOut.join('\n');
  // Strip leading and trailing lines:
  text = text.replace(/^\n+/g, '');
  text = text.replace(/\n+$/g, '');
  return globals.converter._dispatch('makehtml.paragraphs.after', text, options, globals).getText();
});
```

## File: `src/subParsers/makehtml/runExtension.js`
```javascript
/**
 * Run extension
 */
showdown.subParser('makehtml.runExtension', function (ext, text, options, globals) {
  'use strict';

  if (ext.filter) {
    text = ext.filter(text, globals.converter, options);

  } else if (ext.regex) {
    // TODO remove this when old extension loading mechanism is deprecated
    var re = ext.regex;
    if (!(re instanceof RegExp)) {
      re = new RegExp(re, 'g');
    }
    text = text.replace(re, ext.replace);
  }

  return text;
});
```

## File: `src/subParsers/makehtml/spanGamut.js`
```javascript
/**
 * These are all the transformations that occur *within* block-level
 * tags like paragraphs, headers, and list items.
 */
showdown.subParser('makehtml.spanGamut', function (text, options, globals) {
  'use strict';

  text = globals.converter._dispatch('makehtml.span.before', text, options, globals).getText();

  text = showdown.subParser('makehtml.codeSpans')(text, options, globals);
  text = showdown.subParser('makehtml.escapeSpecialCharsWithinTagAttributes')(text, options, globals);
  text = showdown.subParser('makehtml.encodeBackslashEscapes')(text, options, globals);

  // Process link and image tags. Images must come first,
  // because ![foo][f] looks like a link.
  text = showdown.subParser('makehtml.images')(text, options, globals);

  text = globals.converter._dispatch('smakehtml.links.before', text, options, globals).getText();
  text = showdown.subParser('makehtml.links')(text, options, globals);
  text = globals.converter._dispatch('smakehtml.links.after', text, options, globals).getText();

  //text = showdown.subParser('makehtml.autoLinks')(text, options, globals);
  //text = showdown.subParser('makehtml.simplifiedAutoLinks')(text, options, globals);
  text = showdown.subParser('makehtml.emoji')(text, options, globals);
  text = showdown.subParser('makehtml.underline')(text, options, globals);
  text = showdown.subParser('makehtml.italicsAndBold')(text, options, globals);
  text = showdown.subParser('makehtml.strikethrough')(text, options, globals);
  text = showdown.subParser('makehtml.ellipsis')(text, options, globals);

  // we need to hash HTML tags inside spans
  text = showdown.subParser('makehtml.hashHTMLSpans')(text, options, globals);

  // now we encode amps and angles
  text = showdown.subParser('makehtml.encodeAmpsAndAngles')(text, options, globals);

  // Do hard breaks
  if (options.simpleLineBreaks) {
    // GFM style hard breaks
    // only add line breaks if the text does not contain a block (special case for lists)
    if (!/\n\n¨K/.test(text)) {
      text = text.replace(/\n+/g, '<br />\n');
    }
  } else {
    // Vanilla hard breaks
    text = text.replace(/  +\n/g, '<br />\n');
  }

  text = globals.converter._dispatch('makehtml.spanGamut.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makehtml/strikethrough.js`
```javascript
showdown.subParser('makehtml.strikethrough', function (text, options, globals) {
  'use strict';

  if (options.strikethrough) {
    text = globals.converter._dispatch('makehtml.strikethrough.before', text, options, globals).getText();
    text = text.replace(/(?:~){2}([\s\S]+?)(?:~){2}/g, function (wm, txt) { return '<del>' + txt + '</del>'; });
    text = globals.converter._dispatch('makehtml.strikethrough.after', text, options, globals).getText();
  }

  return text;
});
```

## File: `src/subParsers/makehtml/stripLinkDefinitions.js`
```javascript
/**
 * Strips link definitions from text, stores the URLs and titles in
 * hash references.
 * Link defs are in the form: ^[id]: url "optional title"
 */
showdown.subParser('makehtml.stripLinkDefinitions', function (text, options, globals) {
  'use strict';

  var regex       = /^ {0,3}\[([^\]]+)]:[ \t]*\n?[ \t]*<?([^>\s]+)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*\n?[ \t]*(?:(\n*)["|'(](.+?)["|')][ \t]*)?(?:\n+|(?=¨0))/gm,
      base64Regex = /^ {0,3}\[([^\]]+)]:[ \t]*\n?[ \t]*<?(data:.+?\/.+?;base64,[A-Za-z0-9+/=\n]+?)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*\n?[ \t]*(?:(\n*)["|'(](.+?)["|')][ \t]*)?(?:\n\n|(?=¨0)|(?=\n\[))/gm;

  // attacklab: sentinel workarounds for lack of \A and \Z, safari\khtml bug
  text += '¨0';

  var replaceFunc = function (wholeMatch, linkId, url, width, height, blankLines, title) {

    // if there aren't two instances of linkId it must not be a reference link so back out
    linkId = linkId.toLowerCase();
    if (text.toLowerCase().split(linkId).length - 1 < 2) {
      return wholeMatch;
    }
    if (url.match(/^data:.+?\/.+?;base64,/)) {
      // remove newlines
      globals.gUrls[linkId] = url.replace(/\s/g, '');
    } else {
      url = showdown.helper.applyBaseUrl(options.relativePathBaseUrl, url);

      globals.gUrls[linkId] = showdown.subParser('makehtml.encodeAmpsAndAngles')(url, options, globals);  // Link IDs are case-insensitive
    }

    if (blankLines) {
      // Oops, found blank lines, so it's not a title.
      // Put back the parenthetical statement we stole.
      return blankLines + title;

    } else {
      if (title) {
        globals.gTitles[linkId] = title.replace(/"|'/g, '&quot;');
      }
      if (options.parseImgDimensions && width && height) {
        globals.gDimensions[linkId] = {
          width:  width,
          height: height
        };
      }
    }
    // Completely remove the definition from the text
    return '';
  };

  // first we try to find base64 link references
  text = text.replace(base64Regex, replaceFunc);

  text = text.replace(regex, replaceFunc);

  // attacklab: strip sentinel
  text = text.replace(/¨0/, '');

  return text;
});
```

## File: `src/subParsers/makehtml/tables.js`
```javascript
showdown.subParser('makehtml.tables', function (text, options, globals) {
  'use strict';

  if (!options.tables) {
    return text;
  }

  var tableRgx       = /^ {0,3}\|?.+\|.+\n {0,3}\|?[ \t]*:?[ \t]*[-=]{2,}[ \t]*:?[ \t]*\|[ \t]*:?[ \t]*[-=]{2,}[\s\S]+?(?:\n\n|¨0)/gm,
      //singeColTblRgx = /^ {0,3}\|.+\|\n {0,3}\|[ \t]*:?[ \t]*(?:[-=]){2,}[ \t]*:?[ \t]*\|[ \t]*\n(?: {0,3}\|.+\|\n)+(?:\n\n|¨0)/gm;
      singeColTblRgx = /^ {0,3}\|.+\|[ \t]*\n {0,3}\|[ \t]*:?[ \t]*[-=]{2,}[ \t]*:?[ \t]*\|[ \t]*\n( {0,3}\|.+\|[ \t]*\n)*(?:\n|¨0)/gm;

  function parseStyles (sLine) {
    if (/^:[ \t]*--*$/.test(sLine)) {
      return ' style="text-align:left;"';
    } else if (/^--*[ \t]*:[ \t]*$/.test(sLine)) {
      return ' style="text-align:right;"';
    } else if (/^:[ \t]*--*[ \t]*:$/.test(sLine)) {
      return ' style="text-align:center;"';
    } else {
      return '';
    }
  }

  function parseHeaders (header, style) {
    var id = '';
    header = header.trim();
    // support both tablesHeaderId and tableHeaderId due to error in documentation so we don't break backwards compatibility
    if (options.tablesHeaderId || options.tableHeaderId) {
      id = ' id="' + header.replace(/ /g, '_').toLowerCase() + '"';
    }
    header = showdown.subParser('makehtml.spanGamut')(header, options, globals);

    return '<th' + id + style + '>' + header + '</th>\n';
  }

  function parseCells (cell, style) {
    var subText = showdown.subParser('makehtml.spanGamut')(cell, options, globals);
    return '<td' + style + '>' + subText + '</td>\n';
  }

  function buildTable (headers, cells) {
    var tb = '<table>\n<thead>\n<tr>\n',
        tblLgn = headers.length;

    for (var i = 0; i < tblLgn; ++i) {
      tb += headers[i];
    }
    tb += '</tr>\n</thead>\n<tbody>\n';

    for (i = 0; i < cells.length; ++i) {
      tb += '<tr>\n';
      for (var ii = 0; ii < tblLgn; ++ii) {
        tb += cells[i][ii];
      }
      tb += '</tr>\n';
    }
    tb += '</tbody>\n</table>\n';
    return tb;
  }

  function parseTable (rawTable) {
    var i, tableLines = rawTable.split('\n');

    for (i = 0; i < tableLines.length; ++i) {
      // strip wrong first and last column if wrapped tables are used
      if (/^ {0,3}\|/.test(tableLines[i])) {
        tableLines[i] = tableLines[i].replace(/^ {0,3}\|/, '');
      }
      if (/\|[ \t]*$/.test(tableLines[i])) {
        tableLines[i] = tableLines[i].replace(/\|[ \t]*$/, '');
      }
      // parse code spans first, but we only support one line code spans

      tableLines[i] = showdown.subParser('makehtml.codeSpans')(tableLines[i], options, globals);
    }

    var rawHeaders = tableLines[0].split('|').map(function (s) { return s.trim();}),
        rawStyles = tableLines[1].split('|').map(function (s) { return s.trim();}),
        rawCells = [],
        headers = [],
        styles = [],
        cells = [];

    tableLines.shift();
    tableLines.shift();

    for (i = 0; i < tableLines.length; ++i) {
      if (tableLines[i].trim() === '') {
        continue;
      }
      rawCells.push(
        tableLines[i]
          .split('|')
          .map(function (s) {
            return s.trim();
          })
      );
    }

    if (rawHeaders.length < rawStyles.length) {
      return rawTable;
    }

    for (i = 0; i < rawStyles.length; ++i) {
      styles.push(parseStyles(rawStyles[i]));
    }

    for (i = 0; i < rawHeaders.length; ++i) {
      if (showdown.helper.isUndefined(styles[i])) {
        styles[i] = '';
      }
      headers.push(parseHeaders(rawHeaders[i], styles[i]));
    }

    for (i = 0; i < rawCells.length; ++i) {
      var row = [];
      for (var ii = 0; ii < headers.length; ++ii) {
        if (showdown.helper.isUndefined(rawCells[i][ii])) {

        }
        row.push(parseCells(rawCells[i][ii], styles[ii]));
      }
      cells.push(row);
    }

    return buildTable(headers, cells);
  }

  text = globals.converter._dispatch('makehtml.tables.before', text, options, globals).getText();

  // find escaped pipe characters
  text = text.replace(/\\(\|)/g, showdown.helper.escapeCharactersCallback);

  // parse multi column tables
  text = text.replace(tableRgx, parseTable);

  // parse one column tables
  text = text.replace(singeColTblRgx, parseTable);

  text = globals.converter._dispatch('makehtml.tables.after', text, options, globals).getText();

  return text;
});
```

## File: `src/subParsers/makehtml/underline.js`
```javascript
showdown.subParser('makehtml.underline', function (text, options, globals) {
  'use strict';

  if (!options.underline) {
    return text;
  }

  text = globals.converter._dispatch('makehtml.underline.before', text, options, globals).getText();

  if (options.literalMidWordUnderscores) {
    text = text.replace(/\b___(\S[\s\S]*?)___\b/g, function (wm, txt) {
      return '<u>' + txt + '</u>';
    });
    text = text.replace(/\b__(\S[\s\S]*?)__\b/g, function (wm, txt) {
      return '<u>' + txt + '</u>';
    });
  } else {
    text = text.replace(/___(\S[\s\S]*?)___/g, function (wm, m) {
      return (/\S$/.test(m)) ? '<u>' + m + '</u>' : wm;
    });
    text = text.replace(/__(\S[\s\S]*?)__/g, function (wm, m) {
      return (/\S$/.test(m)) ? '<u>' + m + '</u>' : wm;
    });
  }

  // escape remaining underscores to prevent them being parsed by italic and bold
  text = text.replace(/(_)/g, showdown.helper.escapeCharactersCallback);

  text = globals.converter._dispatch('makehtml.underline.after', text, options, globals).getText();

  return text;
});
```

## File: `src/subParsers/makehtml/unescapeSpecialChars.js`
```javascript
/**
 * Swap back in all the special characters we've hidden.
 */
showdown.subParser('makehtml.unescapeSpecialChars', function (text, options, globals) {
  'use strict';
  text = globals.converter._dispatch('makehtml.unescapeSpecialChars.before', text, options, globals).getText();

  text = text.replace(/¨E(\d+)E/g, function (wholeMatch, m1) {
    var charCodeToReplace = parseInt(m1);
    return String.fromCharCode(charCodeToReplace);
  });

  text = globals.converter._dispatch('makehtml.unescapeSpecialChars.after', text, options, globals).getText();
  return text;
});
```

## File: `src/subParsers/makemarkdown/blockquote.js`
```javascript
showdown.subParser('makeMarkdown.blockquote', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (node.hasChildNodes()) {
    var children = node.childNodes,
        childrenLength = children.length;

    for (var i = 0; i < childrenLength; ++i) {
      var innerTxt = showdown.subParser('makeMarkdown.node')(children[i], options, globals);

      if (innerTxt === '') {
        continue;
      }
      txt += innerTxt;
    }
  }
  // cleanup
  txt = txt.trim();
  txt = '> ' + txt.split('\n').join('\n> ');
  return txt;
});
```

## File: `src/subParsers/makemarkdown/break.js`
```javascript
showdown.subParser('makeMarkdown.break', function () {
  'use strict';

  return '  \n';
});
```

## File: `src/subParsers/makemarkdown/codeBlock.js`
```javascript
showdown.subParser('makeMarkdown.codeBlock', function (node, options, globals) {
  'use strict';

  var lang = node.getAttribute('language'),
      num  = node.getAttribute('precodenum');
  return '```' + lang + '\n' + globals.preList[num] + '\n```';
});
```

## File: `src/subParsers/makemarkdown/codeSpan.js`
```javascript
showdown.subParser('makeMarkdown.codeSpan', function (node) {
  'use strict';

  return '`' + node.innerHTML + '`';
});
```

## File: `src/subParsers/makemarkdown/emphasis.js`
```javascript
showdown.subParser('makeMarkdown.emphasis', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (node.hasChildNodes()) {
    txt += '*';
    var children = node.childNodes,
        childrenLength = children.length;
    for (var i = 0; i < childrenLength; ++i) {
      txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
    }
    txt += '*';
  }
  return txt;
});
```

## File: `src/subParsers/makemarkdown/header.js`
```javascript
showdown.subParser('makeMarkdown.header', function (node, options, globals, headerLevel) {
  'use strict';

  var headerMark = new Array(headerLevel + 1).join('#'),
      txt = '';

  if (node.hasChildNodes()) {
    txt = headerMark + ' ';
    var children = node.childNodes,
        childrenLength = children.length;

    for (var i = 0; i < childrenLength; ++i) {
      txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
    }
  }
  return txt;
});
```

## File: `src/subParsers/makemarkdown/hr.js`
```javascript
showdown.subParser('makeMarkdown.hr', function () {
  'use strict';

  return '---';
});
```

## File: `src/subParsers/makemarkdown/image.js`
```javascript
showdown.subParser('makeMarkdown.image', function (node) {
  'use strict';

  var txt = '';
  if (node.hasAttribute('src') && node.getAttribute('src') !== '') {
    txt += '![' + node.getAttribute('alt') + '](';
    txt += '<' + node.getAttribute('src') + '>';
    if (node.hasAttribute('width') && node.hasAttribute('height')) {
      var width = node.getAttribute('width');
      var height = node.getAttribute('height');
      txt += ' =' + (width === 'auto' ? '*' : width) + 'x' + (height === 'auto' ? '*' : height);
    }

    if (node.hasAttribute('title')) {
      txt += ' "' + node.getAttribute('title') + '"';
    }
    txt += ')';
  }
  return txt;
});
```

## File: `src/subParsers/makemarkdown/input.js`
```javascript
showdown.subParser('makeMarkdown.input', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (node.getAttribute('checked') !== null) {
    txt += '[x]';
  } else {
    txt += '[ ]';
  }
  var children = node.childNodes,
      childrenLength = children.length;
  for (var i = 0; i < childrenLength; ++i) {
    txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
  }
  return txt;
});
```

## File: `src/subParsers/makemarkdown/links.js`
```javascript
showdown.subParser('makeMarkdown.links', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (node.hasChildNodes() && node.hasAttribute('href')) {
    var children = node.childNodes,
        childrenLength = children.length;

    // special case for mentions
    // to simplify (and not make stuff really complicated) mentions will only work in this circumstance:
    // <a class="user-mention" href="https://github.com/user">@user</a>
    // that is, if there's a "user-mention" class and option ghMentions is true
    // otherwise is ignored
    var classes = node.getAttribute('class');
    if (options.ghMentions && /(?:^| )user-mention\b/.test(classes)) {
      for (var ii = 0; ii < childrenLength; ++ii) {
        txt += showdown.subParser('makeMarkdown.node')(children[ii], options, globals);
      }

    } else {
      txt = '[';
      for (var i = 0; i < childrenLength; ++i) {
        txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
      }
      txt += '](';
      txt += '<' + node.getAttribute('href') + '>';
      if (node.hasAttribute('title')) {
        txt += ' "' + node.getAttribute('title') + '"';
      }
      txt += ')';
    }


  }
  return txt;
});
```

## File: `src/subParsers/makemarkdown/list.js`
```javascript
showdown.subParser('makeMarkdown.list', function (node, options, globals, type) {
  'use strict';

  var txt = '';
  if (!node.hasChildNodes()) {
    return '';
  }
  var listItems       = node.childNodes,
      listItemsLenght = listItems.length,
      listNum = node.getAttribute('start') || 1;

  for (var i = 0; i < listItemsLenght; ++i) {
    if (typeof listItems[i].tagName === 'undefined' || listItems[i].tagName.toLowerCase() !== 'li') {
      continue;
    }

    // define the bullet to use in list
    var bullet = '';
    if (type === 'ol') {
      bullet = listNum.toString() + '. ';
    } else {
      bullet = '- ';
    }

    // parse list item
    txt += bullet + showdown.subParser('makeMarkdown.listItem')(listItems[i], options, globals);
    ++listNum;
  }

  return txt.trim();
});
```

## File: `src/subParsers/makemarkdown/listItem.js`
```javascript
showdown.subParser('makeMarkdown.listItem', function (node, options, globals) {
  'use strict';

  var listItemTxt = '';

  var children = node.childNodes,
      childrenLenght = children.length;

  for (var i = 0; i < childrenLenght; ++i) {
    listItemTxt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
  }
  // if it's only one liner, we need to add a newline at the end
  if (!/\n$/.test(listItemTxt)) {
    listItemTxt += '\n';
  } else {
    // it's multiparagraph, so we need to indent
    listItemTxt = listItemTxt
      .split('\n')
      .join('\n    ')
      .replace(/^ {4}$/gm, '')
      .replace(/\n\n+/g, '\n\n');
  }

  return listItemTxt;
});
```

## File: `src/subParsers/makemarkdown/node.js`
```javascript


showdown.subParser('makeMarkdown.node', function (node, options, globals, spansOnly) {
  'use strict';

  spansOnly = spansOnly || false;

  var txt = '';

  // edge case of text without wrapper paragraph
  if (node.nodeType === 3) {
    return showdown.subParser('makeMarkdown.txt')(node, options, globals);
  }

  // HTML comment
  if (node.nodeType === 8) {
    return '<!--' + node.data + '-->\n\n';
  }

  // process only node elements
  if (node.nodeType !== 1) {
    return '';
  }

  var tagName = node.tagName.toLowerCase();

  switch (tagName) {

    //
    // BLOCKS
    //
    case 'h1':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.header')(node, options, globals, 1) + '\n\n'; }
      break;
    case 'h2':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.header')(node, options, globals, 2) + '\n\n'; }
      break;
    case 'h3':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.header')(node, options, globals, 3) + '\n\n'; }
      break;
    case 'h4':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.header')(node, options, globals, 4) + '\n\n'; }
      break;
    case 'h5':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.header')(node, options, globals, 5) + '\n\n'; }
      break;
    case 'h6':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.header')(node, options, globals, 6) + '\n\n'; }
      break;

    case 'p':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.paragraph')(node, options, globals) + '\n\n'; }
      break;

    case 'blockquote':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.blockquote')(node, options, globals) + '\n\n'; }
      break;

    case 'hr':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.hr')(node, options, globals) + '\n\n'; }
      break;

    case 'ol':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.list')(node, options, globals, 'ol') + '\n\n'; }
      break;

    case 'ul':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.list')(node, options, globals, 'ul') + '\n\n'; }
      break;

    case 'precode':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.codeBlock')(node, options, globals) + '\n\n'; }
      break;

    case 'pre':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.pre')(node, options, globals) + '\n\n'; }
      break;

    case 'table':
      if (!spansOnly) { txt = showdown.subParser('makeMarkdown.table')(node, options, globals) + '\n\n'; }
      break;

    //
    // SPANS
    //
    case 'code':
      txt = showdown.subParser('makeMarkdown.codeSpan')(node, options, globals);
      break;

    case 'em':
    case 'i':
      txt = showdown.subParser('makeMarkdown.emphasis')(node, options, globals);
      break;

    case 'strong':
    case 'b':
      txt = showdown.subParser('makeMarkdown.strong')(node, options, globals);
      break;

    case 'del':
      txt = showdown.subParser('makeMarkdown.strikethrough')(node, options, globals);
      break;

    case 'a':
      txt = showdown.subParser('makeMarkdown.links')(node, options, globals);
      break;

    case 'img':
      txt = showdown.subParser('makeMarkdown.image')(node, options, globals);
      break;

    case 'br':
      txt = showdown.subParser('makeMarkdown.break')(node, options, globals);
      break;

    case 'input':
      txt = showdown.subParser('makeMarkdown.input')(node, options, globals);
      break;

    default:
      txt = node.outerHTML + '\n\n';
  }

  // common normalization
  // TODO eventually

  return txt;
});
```

## File: `src/subParsers/makemarkdown/paragraph.js`
```javascript
showdown.subParser('makeMarkdown.paragraph', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (node.hasChildNodes()) {
    var children = node.childNodes,
        childrenLength = children.length;
    for (var i = 0; i < childrenLength; ++i) {
      txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
    }
  }

  // some text normalization
  txt = txt.trim();

  return txt;
});
```

## File: `src/subParsers/makemarkdown/pre.js`
```javascript
showdown.subParser('makeMarkdown.pre', function (node, options, globals) {
  'use strict';

  var num  = node.getAttribute('prenum');
  return '<pre>' + globals.preList[num] + '</pre>';
});
```

## File: `src/subParsers/makemarkdown/strikethrough.js`
```javascript
showdown.subParser('makeMarkdown.strikethrough', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (node.hasChildNodes()) {
    txt += '~~';
    var children = node.childNodes,
        childrenLength = children.length;
    for (var i = 0; i < childrenLength; ++i) {
      txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
    }
    txt += '~~';
  }
  return txt;
});
```

## File: `src/subParsers/makemarkdown/strong.js`
```javascript
showdown.subParser('makeMarkdown.strong', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (node.hasChildNodes()) {
    txt += '**';
    var children = node.childNodes,
        childrenLength = children.length;
    for (var i = 0; i < childrenLength; ++i) {
      txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals);
    }
    txt += '**';
  }
  return txt;
});
```

## File: `src/subParsers/makemarkdown/table.js`
```javascript
showdown.subParser('makeMarkdown.table',
  /**
   *
   * @param {DocumentFragment} node
   * @param {{}} options
   * @param {{}} globals
   * @returns {string}
   */
  function (node, options, globals) {
    'use strict';

    var txt = '',
        tableArray = [[], []],
        headings,
        rows = [],
        colCount,
        i,
        ii;

    /**
     * @param {Element} tr
     */
    function iterateRow (tr) {
      var children = tr.childNodes,
          cols = [];
      // we need to iterate by order, since td and th can be used interchangeably and in any order
      // we will ignore malformed stuff, comments and floating text.
      for (var i = 0; i < children.length; ++i) {
        var childName = children[i].nodeName.toUpperCase();
        if (childName === 'TD' || childName === 'TH') {
          cols.push(children[i]);
        }
      }
      return cols;
    }


    // first lets look for <thead>
    // we will ignore thead without <tr> children
    // also, since markdown doesn't support tables with multiple heading rows, only the first one will be transformed
    // the rest will count as regular rows
    if (node.querySelectorAll(':scope>thead').length !== 0 && node.querySelectorAll(':scope>thead>tr').length !== 0) {
      var thead = node.querySelectorAll(':scope>thead>tr');

      // thead>tr can have td and th children
      for (i = 0; i < thead.length; ++i) {
        rows.push(iterateRow(thead[i]));
      }
    }

    // now let's look for tbody
    // we will ignore tbody without <tr> children
    if (node.querySelectorAll(':scope>tbody').length !== 0 && node.querySelectorAll(':scope>tbody>tr').length !== 0) {
      var tbody = node.querySelectorAll(':scope>tbody>tr');
      // tbody>tr can have td and th children, although th are not very screen reader friendly
      for (i = 0; i < tbody.length; ++i) {
        rows.push(iterateRow(tbody[i]));
      }
    }

    // now look for tfoot
    if (node.querySelectorAll(':scope>tfoot').length !== 0 && node.querySelectorAll(':scope>tfoot>tr').length !== 0) {
      var tfoot = node.querySelectorAll(':scope>tfoot>tr');
      // tfoot>tr can have td and th children, although th are not very screen reader friendly
      for (i = 0; i < tfoot.length; ++i) {
        rows.push(iterateRow(tfoot[i]));
      }
    }

    // lastly look for naked tr
    if (node.querySelectorAll(':scope>tr').length !== 0) {

      var tr = node.querySelectorAll(':scope>tr');
      // tfoot>tr can have td and th children, although th are not very screen reader friendly
      for (i = 0; i < tr.length; ++i) {
        rows.push(iterateRow(tr[i]));
      }
    }

    // TODO: implement <caption> in tables https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/caption
    // note: <colgroup> is ignored, since they are basically styling

    // we need now to account for cases of completely empty tables, like <table></table> or equivalent
    if (rows.length === 0) {
      // table is empty, return empty text
      return txt;
    }

    // count the first row. We need it to trim the table (if table rows have inconsistent number of columns)
    colCount = rows[0].length;

    // let's shift the first row as a heading
    headings = rows.shift();

    for (i = 0; i < headings.length; ++i) {
      var headContent = showdown.subParser('makeMarkdown.tableCell')(headings[i], globals),
          align = '---';

      if (headings[i].hasAttribute('style')) {
        var style = headings[i].getAttribute('style').toLowerCase().replace(/\s/g, '');
        switch (style) {
          case 'text-align:left;':
            align = ':---';
            break;
          case 'text-align:right;':
            align = '---:';
            break;
          case 'text-align:center;':
            align = ':---:';
            break;
        }
      }
      tableArray[0][i] = headContent.trim();
      tableArray[1][i] = align;
    }

    // now iterate through the rows and create the pseudo output (not pretty yet)
    for (i = 0; i < rows.length; ++i) {
      var r = tableArray.push([]) - 1;

      for (ii = 0; ii < colCount; ++ii) {
        var cellContent = ' ';
        if (typeof rows[i][ii] !== 'undefined') {
          // Note: if rows[i][ii] is undefined, it means the row has fewer elements than the header,
          // and empty content will be added
          cellContent = showdown.subParser('makeMarkdown.tableCell')(rows[i][ii], globals);
        }
        tableArray[r].push(cellContent);
      }
    }

    // now tidy up the output, aligning cells and stuff
    var cellSpacesCount = 3;
    for (i = 0; i < tableArray.length; ++i) {
      for (ii = 0; ii < tableArray[i].length; ++ii) {
        var strLen = tableArray[i][ii].length;
        if (strLen > cellSpacesCount) {
          cellSpacesCount = strLen;
        }
      }
    }

    for (i = 0; i < tableArray.length; ++i) {
      for (ii = 0; ii < tableArray[i].length; ++ii) {
        if (i === 1) {
          if (tableArray[i][ii].slice(-1) === ':') {
            tableArray[i][ii] = showdown.helper.padEnd(tableArray[i][ii].slice(0, -1), cellSpacesCount - 1, '-') + ':';
          } else {
            tableArray[i][ii] = showdown.helper.padEnd(tableArray[i][ii], cellSpacesCount, '-');
          }

        } else {
          tableArray[i][ii] = showdown.helper.padEnd(tableArray[i][ii], cellSpacesCount);
        }
      }
      txt += '| ' + tableArray[i].join(' | ') + ' |\n';
    }

    return txt.trim();
  }
);
```

## File: `src/subParsers/makemarkdown/tableCell.js`
```javascript
showdown.subParser('makeMarkdown.tableCell', function (node, options, globals) {
  'use strict';

  var txt = '';
  if (!node.hasChildNodes()) {
    return '';
  }
  var children = node.childNodes,
      childrenLength = children.length;

  for (var i = 0; i < childrenLength; ++i) {
    txt += showdown.subParser('makeMarkdown.node')(children[i], options, globals, true);
  }
  return txt.trim();
});
```

## File: `src/subParsers/makemarkdown/txt.js`
```javascript
showdown.subParser('makeMarkdown.txt', function (node) {
  'use strict';

  var txt = node.nodeValue;

  // multiple spaces are collapsed
  txt = txt.replace(/ +/g, ' ');

  // replace the custom ¨NBSP; with a space
  txt = txt.replace(/¨NBSP;/g, ' ');

  // ", <, > and & should replace escaped html entities
  txt = showdown.helper.unescapeHTMLEntities(txt);

  // escape markdown magic characters
  // emphasis, strong and strikethrough - can appear everywhere
  // we also escape pipe (|) because of tables
  // and escape ` because of code blocks and spans
  txt = txt.replace(/([*_~|`])/g, '\\$1');

  // escape > because of blockquotes
  txt = txt.replace(/^(\s*)>/g, '\\$1>');

  // hash character, only troublesome at the beginning of a line because of headers
  txt = txt.replace(/^#/gm, '\\#');

  // horizontal rules
  txt = txt.replace(/^(\s*)([-=]{3,})(\s*)$/, '$1\\$2$3');

  // dot, because of ordered lists, only troublesome at the beginning of a line when preceded by an integer
  txt = txt.replace(/^( {0,3}\d+)\./gm, '$1\\.');

  // +, * and -, at the beginning of a line becomes a list, so we need to escape them also (asterisk was already escaped)
  txt = txt.replace(/^( {0,3})([+-])/gm, '$1\\$2');

  // images and links, ] followed by ( is problematic, so we escape it
  txt = txt.replace(/]([\s]*)\(/g, '\\]$1\\(');

  // reference URIs must also be escaped
  txt = txt.replace(/^ {0,3}\[([\S \t]*?)]:/gm, '\\[$1]:');

  return txt;
});
```

## File: `test/bootstrap.js`
```javascript
//.webstorm.bootstrap.js
var chai = require('chai');
global.chai = chai;
global.expect = chai.expect;
global.showdown = require('../.build/showdown.js');
global.getDefaultOpts = require('./optionswp.js').getDefaultOpts;
```

## File: `test/optionswp.js`
```javascript
/* jshint ignore:start */
var fs = require('fs'),
    filedata;
filedata = fs.readFileSync('src/options.js', 'utf8');
eval(filedata);
module.exports = {
  getDefaultOpts: getDefaultOpts
};
/* jshint ignore:end */
```

## File: `test/performance.testfile.md`
```markdown

This is [an example][id] reference-style link.
This is [another] [foo] reference-style link.
This is [a third][bar] reference-style link.
This is [a fourth][4] reference-style link.

  [id]: http://example.com/  "Optional Title Here"
  [foo]: http://example.com/  (Optional Title Here)
  [bar]: http://example.com/  (Optional Title Here)
  [4]: <http://example.com/>
    "Optional Title Here"
  
 

<http://example.com/>
  
 
> a blockquote
    with a 4 space indented line (not code)

sep

> a blockquote

    with some code after
  
 
    > this is a pseudo blockquote
    > inside a code block

foo

    > this is another bq
    inside code
  
 
> ## This is a header.
>
> 1.   This is the first list item.
> 2.   This is the second list item.
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");
  
 
  
  > This is a multi line blockquote test
  >
  > With more than one line.
  
 

This is some HTML:

    <h1>Heading</h1>
  
 

This is a normal paragraph:

    This is a code block.
  
 

 *  Bird

 *  Magic
  
 
*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

text *with italic sentence* in middle

text __with bold sentence__ in middle

text with __bold text that
spans across multiple__ lines

underscored_word

doubleunderscore__word

asterix*word

doubleasterix**word

line with_underscored word

line with__doubleunderscored word

line with*asterixed word

line with**doubleasterixed word

some line_with_inner underscores

some line__with__inner double underscores

some line*with*inner asterixs

some line**with**inner double asterixs

another line with just _one underscore

another line with just __one double underscore

another line with just *one asterix

another line with just **one double asterix

a sentence with_underscore and another_underscore

a sentence with__doubleunderscore and another__doubleunderscore

a sentence with*asterix and another*asterix

a sentence with**doubleasterix and another**doubleasterix

escaped word\_with\_underscores

escaped word\_\_with\_\_double underscores

escaped word_\_with\__single italic underscore

escaped word\*with*asterixs

escaped word\*\*with\*\*asterixs

escaped word**\*with\***bold asterixs
  
 
It happened in 1986\. What a great season.
  
 

These should all be escaped:

\\

\`

\*

\_

\{

\}

\[

\]

\(

\)

\#

\+

\-

\.

\!
  
 
```
function MyFunc(a) {
    // ...
}
```

That is some code!
  
 
> Define a function in javascript:
>
> ```
> function MyFunc(a) {
>     var s = '`';
> }
> ```
>
>> And some nested quote
>>
>> ```html
>> <div>HTML!</div>
>> ```
  
 

Define a function in javascript:

```
function MyFunc(a) {
    var s = '`';
}
```

And some HTML

```html
<div>HTML!</div>
```
  
 
```
code can go here
this is rendered on a second line
```
  
 
# This is an H1 #
  
 
This is an H1
=============
  
 
# This is an H1
  
 
This is an H2
-------------
  
 
## This is an H2 ##
  
 
## This is an H2
  
 
### This is an H3 ###
  
 
### This is an H3
  
 
#### This is an H4
  
 
##### This is an H5
  
 
###### This is an H6
  
 

* * *

***

*****

- - -

---------------------------------------
  
 
<!-- a comment -->

<!-- a comment with *bogus* __markdown__ inside -->

words <!-- a comment --> words

<!-- comment --> words

   <!-- comment -->

    <!-- comment -->
  
 
  - list item 1

    ```html
    <a href="www.google.com">google</a>
    <div>
      <div>some div</div>
    </div>
    ```
  
 

These HTML5 tags should pass through just fine.

<section>hello</section>
<header>head</header>
<footer>footsies</footer>
<nav>navigation</nav>
<article>read me</article>
<aside>ignore me</aside>
<article>read
me</article>
<aside>
ignore me
</aside>

the end

<table class="test">
    <tr>
        <td>Foo</td>
    </tr>
    <tr>
        <td>Bar</td>
    </tr>
</table>

<table class="test">
    <thead>
        <tr>
            <td>Foo</td>
        </tr>
    </thead>
    <tr>
        <td>Bar</td>
    </tr>
    <tfoot>
        <tr>
            <td>Bar</td>
        </tr>
    </tfoot>
</table>

<audio class="podcastplayer" controls>
    <source src="foobar.mp3" type="audio/mp3" preload="none"></source>
    <source src="foobar.off" type="audio/ogg" preload="none"></source>
</audio>

<video src="foo.ogg">
    <track kind="subtitles" src="foo.en.vtt" srclang="en" label="English">
    <track kind="subtitles" src="foo.sv.vtt" srclang="sv" label="Svenska">
</video>

<address>My street</address>

<canvas id="canvas" width="300" height="300">
    Sorry, your browser doesn't support the &lt;canvas&gt; element.
</canvas>

<figure>
    <img src="mypic.png" alt="An awesome picture">
    <figcaption>Caption for the awesome picture</figcaption>
</figure>

<hgroup>
  <h1>Main title</h1>
  <h2>Secondary title</h2>
</hgroup>

<output name="result"></output>
  
 

![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")

![Alt text][id]

  [id]: url/to/image  "Optional title attribute"
  
 

Search the web at [Google][] or [Daring Fireball][].

  [Google]: http://google.com/
  [Daring Fireball]: http://daringfireball.net/
  
 

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.
  
 

Create a new `function`.

Use the backtick in MySQL syntax ``SELECT `column` FROM whatever``.

A single backtick in a code span: `` ` ``

A backtick-delimited string in a code span: `` `foo` ``

Please don't use any `<blink>` tags.

`&#8212;` is the decimal-encoded equivalent of `&mdash;`.
  
 

Hello.this\_is\_a\_variable
and.this.is.another_one
  
 

<style>
    p { line-height: 20px; }
</style>

An exciting sentence.
  
 

  > This is a multi line blockquote test

  > With more than one line.
  
 
<a href="foo">some text</a> words

<br> words
  
 
# some title

1. list item 1
2. list item 2

> some text in a blockquote

* another list item 1
* another list item 2
  
 
# some title

1. list item 1
2. list item 2

```
some code

and some other line of code
```

* another list item 1
* another list item 2
  
 
*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.
  
 
*   A list item with code:

        alert('Hello world!');
  
 
<code>some **code** yeah</code>

some <code>inline **code** block</code>

<code>some inline **code**</code> block

yo dawg <code start="true">some <code start="false">code</code> inception</code>

<div>some **div** yeah</div>
  
 

 1.  This is a major bullet point.

    That contains multiple paragraphs.

 2.  And another line
  
 

 - This line spans
 more than one line and is lazy
 - Similar to this line
  
 

  > This is a multi line blockquote test
  >
  > > And nesting!
  >
  > With more than one line.
  
 

 1.  Red
 1.  Green
 1.  Blue
  
 

 8.  Red
 1.  Green
 3.  Blue
  
 

 1.  Red
 2.  Green
 3.  Blue
  
 
 - foo
 
    - bazinga
    
    - yeah
 
 - bar
 
    1. damn
    
    2. so many paragraphs
 
 - baz
  
 
code inception

```
<pre><code>
<div>some html code inside code html tags inside a fenced code block</div>
</code></pre>
```
  
 
<pre>
<code>
foobar
</code>
</pre>

blabla

<pre nhaca="zulu"><code bla="bla">
foobar
</code>
</pre>

<pre><code>
<div>some html code</div>
</code></pre>
  
 

See my [About](/about/) page for details.
  
 
# Same Title

some text

# Same Title
  
 

Hello, world!
  
 

**important**

__important__

really **freaking**strong
  
 

 * Red
 * Green
 * Blue
  
 

 - Red
 - Green
 - Blue
  
 

 + Red
 + Green
 + Blue
  
 
There's an [episode](http://en.memory-alpha.org/wiki/Darmok_(episode)) of Star Trek: The Next Generation
  
 
# some title

Test **bold** and _italic_
  
 
![my image](./pic/pic1_50.png =100pxx20px)

![my image2][1]

[1]: ./pic/pic1_50.png =100pxx20px
  
 
foo.bar

www.foobar

www.foobar.com

http://foobar.com

https://www.foobar.com/baz?bazinga=nhecos;

<a href="http://www.google.com/">http://www.google.com</a>
  
 
this is a sentence_with_mid underscores

this is a sentence with just_one underscore

this _should be parsed_ as emphasis

this is double__underscore__mid word

this has just__one double underscore

this __should be parsed__ as bold

emphasis at _end of sentence_

_emphasis at_ line start

multi _line emphasis
yeah it is_ yeah
  
 
a ~~strikethrough~~ word

this should~~not be parsed

~~strike-through text~~
  
 
# my things

 -  foo
 - [] bar
 - [ ] baz
 - [x] bazinga

otherthings
  
 
# some markdown

blabla
<div>This is **not parsed**</div>
<div markdown="1">This is **parsed**</div>
<div>This is **not parsed**</div>
  
 
​pointer *ptr *thing

something _else _bla

something __else __bla
  
 
http://website.com/img@x2.jpg

http://website.com/img-x2.jpg

http://website.com/img@x2

http://website.com/img@.jpg
  
 
a simple
wrapped line
  
 
Your friend ~~[**test\***](www.google.com)~~ (~~[*@test*](www.google.com)~~) updated his/her description
  
 
      ## markdown doc
      
      you can use markdown for card documentation
        - foo
        - bar
  
 
this is a link to www.github.com

this is a link to <www.google.com>
  
 
1. One
2. Two
    - A
    - B
3. Three

> this has
> simple linebreaks

    testing
    some
    code

 1. paragraphed list

    this belongs
    to the first list item
    
 2. This text
    also

simple
text

 - a list
   item
 - another
   list item

simple
text

  - some item
 
    another
    paragraph
   
      - And
        now
     
        paragraph
        sublist
     
          - and
            even
       
            another
            one

 - foo

  
 
foo烫
bar

foo
bar
  
 
# some header

# some header with &+$,/:;=?@\"#{}|^~[]`\\*()%.!' chars

# another header > with < chars
  
 
**Nom :** aaaa
**Nom :** aaa
  
 
Just an example info@example.com ok?​
  
 
#Given

#When

#Then

foo
===

bar
---
  
 
http://en.wikipedia.org/wiki/Tourism_in_Germany
  
 
this email <foobar@example.com> should not be encoded
  
 
this is some text

```php
function thisThing() {
  echo "some weird formatted code!";
}
```

some other text
  
 
* foo
  * bar

...

* baz
  1. bazinga
  
 
url http://www.google.com.

url http://www.google.com!

url http://www.google.com? foo

url (http://www.google.com) bazinga
  
 
hello @tivie how are you?

this email foo@gmail.com is not parsed

this \@mentions is not parsed also
  
 
# header

#header
  
 
 1. One
 2. Two
    foo
    
    bar
    bazinga
    
    
    
    
    nhecos
    
 3. Three
    
    - foo
    
    - bar
     
 
| *foo* | **bar** | ~~baz~~ |
|-------|---------|---------|
| 100   | blabla  |  aaa    |
  
 
|key|value|
|--|--| 
|My Key|My Value|
  
 
| First Header  | Second Header |
| :------------ | :------------ |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
  
 
| First Header  | Second Header |
| ------------- | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
  
 
| First Header  | Second Header |
| ------------- | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
  
 
First Header  | Second Header|Third Header
------------- | -------------|---
Content Cell  | Content Cell|C
Content Cell  | Content Cell|C
  
 
| First Header  | Second Header | Third Header  | Fourth Header |
| :------------ |: ----------- :| ------------ :| ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  | Row 1 Cell 3  | Row 1 Cell 4  |
| Row 2 Cell 1  | Row 2 Cell 2  | Row 2 Cell 3  | Row 2 Cell 4  |
| Row 3 Cell 1  | Row 3 Cell 2  | Row 3 Cell 3  | Row 3 Cell 4  |
| Row 4 Cell 1  | Row 4 Cell 2  | Row 4 Cell 3  | Row 4 Cell 4  |
| Row 5 Cell 1  | Row 5 Cell 2  | Row 5 Cell 3  | Row 5 Cell 4  |
  
 
| First Header  | Second Header | Third Header  | Fourth Header |
| ------------- | ------------- | ------------  | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  | Row 1 Cell 3  | Row 1 Cell 4  |
| Row 2 Cell 1  | Row 2 Cell 2  | Row 2 Cell 3  | Row 2 Cell 4  |
| Row 3 Cell 1  | Row 3 Cell 2  | Row 3 Cell 3  | Row 3 Cell 4  |
| Row 4 Cell 1  | Row 4 Cell 2  | Row 4 Cell 3  | Row 4 Cell 4  |
| Row 5 Cell 1  | Row 5 Cell 2  | Row 5 Cell 3  | Row 5 Cell 4  |
  
 
| Left-Aligned  |    Center-Aligned    | Right-Aligned |
| :------------ |:--------------------:| -------------:|
| col 3 is      | some wordy paragraph |         $1600 |
| col 2 is      |       centered       |           $12 |
| zebra stripes |       are neat       |            $1 |
  
 
Table Test
============

section 1
------------

|header1    |header2    |header3|
|-----------|-----------|---------|
|Value1     |Value2     |Value3   |


section 2
-----------

|headerA    |headerB    |headerC|
|-----------|-----------|---------|
|ValueA     |ValueB     |ValueC   |
  
 
some text


    | Tables        | Are           | Cool  |
    | ------------- |:-------------:| -----:|
    | **col 3 is**  | right-aligned | $1600 |
    | col 2 is      | *centered*    |   $12 |
    | zebra stripes | ~~are neat~~  |    $1 |
  
 

### Stats


Status | AGENT1 | AGENT2 | AGENT3 | AGENT4 | AGENT5 | AGENT6 | AGENT7 | AGENT8 | AGENT9 | TOTAL |
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AGENT ERROR | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
APPROVED | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
  
 
| First Header  | Second Header |
| ============= | ============= |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
  
 
| First Header  | Second Header     |
| ------------- | ----------------- |
| **bold**      | ![img](foo.jpg)   |
| _italic_      | [link](bla.html)  |
| `some code`   | [google][1]       |
| <www.foo.com> | normal            |


  [1]: www.google.com
  
 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nisi est, 
ullamcorper euismod iaculis sed, tristique at neque. Nullam metus risus, 
malesuada vitae imperdiet ac, tincidunt eget lacus. Proin ullamcorper 
vulputate dictum. Vestibulum consequat ultricies nibh, sed tempus nisl mattis a.

| First Header  | Second Header |
| ------------- | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |

Phasellus ac porttitor quam. Integer cursus accumsan mauris nec interdum. 
Etiam iaculis urna vitae risus facilisis faucibus eu quis risus. Sed aliquet 
rutrum dictum. Vivamus pulvinar malesuada ultricies. Pellentesque in commodo 
nibh. Maecenas justo erat, sodales vel bibendum a, dignissim in orci. Duis 
blandit ornare mi non facilisis. Aliquam rutrum fringilla lacus in semper. 
Sed vel pretium lorem.
  
 
| First Header  | Second Header |
| ------------- | ------------- |
  
 
| First Header  | Second Header |
  
 
### Automatic Links

```
https://ghost.org
```

https://ghost.org

### Markdown Footnotes

```
The quick brown fox[^1] jumped over the lazy dog[^2].

[^1]: Foxes are red
[^2]: Dogs are usually not red
```

The quick brown fox[^1] jumped over the lazy dog[^2].


### Syntax Highlighting

    ```language-javascript
       [...]
    ```

Combined with [Prism.js](http://prismjs.com/) in the Ghost theme:

```language-javascript
// # Notifications API
// RESTful API for creating notifications
var Promise            = require('bluebird'),
    _                  = require('lodash'),
    canThis            = require('../permissions').canThis,
    errors             = require('../errors'),
    utils              = require('./utils'),

    // Holds the persistent notifications
    notificationsStore = [],
    // Holds the last used id
    notificationCounter = 0,
    notifications;
```
  
 
foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

_baz_bar_foo_

__baz_bar_foo__

___baz_bar_foo___

baz bar foo _baz_bar_foo foo bar baz_ and foo

foo\_bar\_baz foo\_bar\_baz\_bar\_foo \_foo\_bar baz\_bar\_ baz\_foo

`foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo`


    foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo


```html
foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
```

<pre>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</pre>

<pre><code class="language-html">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></pre>

<pre class="lang-html"><code class="language-html">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></pre>

<script>
var strike = "foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo";
var foo_bar_baz_bar_foo = "foo_bar_";
</script>

[foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo](http://myurl.com/foo_bar_baz_bar_foo)

<a href="http://myurl.com/foo_bar_baz_bar_foo" title="foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</a>

<img src="http://myurl.com/foo_bar_baz_bar_foo" alt="foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo">

foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
-----

### foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

1. foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
2. foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

> blockquote foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

* foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
* foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

-------

http://en.wikipedia.org/wiki/Tourism_in_Germany

[an example] [wiki]

Another [example][wiki] of a link

[wiki]: http://en.wikipedia.org/wiki/Tourism_in_Germany

<p><code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></p>

<!-- These two cases still have bad <ems> because showdown handles them incorrectly -->

<code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code>

![foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo](http://myurl.com/foo_bar_baz_bar_foo)

http://myurl.com/foo_bar_baz_bar_foo

<http://myurl.com/foo_bar_baz_bar_foo>

_italics_.

_italics_   .
  
 
escaped word\_with\_underscores

escaped word\_\_with\_\_double underscores

escaped word_\_with\__single italic underscore

escaped word\*with*asterixs

escaped word\*\*with\*\*asterixs

escaped word**\*with\***bold asterixs
  
 
* Item 1
* Item 2

1. Item 1
2. Item 2

- Item 1
- Item 2
  
 
2015-10-04
  
 
1. Hi, I am a thing

   ```sh
    
   $ git clone thing.git
   
   dfgdfg
   ```

1. I am another thing!

   ```sh
   
   $ git clone other-thing.git

   foobar
   ```
  
 
> a blockquote
# followed by an heading
  
 
Test pre in a list

- & <
- `& <`
    - & <
    - `& <`
        - & <
        - `& <`
            - & <
            - `& <`
  
 
Title 1
-------

<div></div>


# Title 2


<div>
</div>
  
 
<pre lang="no-highlight"><code>
foo

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

bar
</code></pre>

this is a long paragraph

this is another long paragraph

<pre lang="no-highlight"><code>```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```
</code></pre>
  
 
<pre lang="no-highlight"><code>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting.
But let's throw in a <b>tag</b>.
```
</code></pre>
  
 
<pre lang="no-highlight"><code>```python
var s;
```
</code></pre>

this is a long paragraph

<pre lang="no-highlight"><code>
```javascript
var s;
```
</code></pre>
  
 
![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) [sd-ref][sd-logo]

foo

[sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) ![sd-ref][sd-logo]

foo

![sd-ref][sd-logo] [sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

foo

[sd-ref][sd-logo] ![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

foo

[![sd-ref][sd-logo]](http://www.google.com/)

[sd-logo]: https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
  
 
![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) ![sd-ref][sd-logo]

foo

![sd-ref][sd-logo] ![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

[sd-logo]: https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
  
 
[sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) [sd-ref][sd-logo]

foo

[sd-ref][sd-logo] [sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

[sd-logo]: https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
  
 
* list item 1

    ```
    <parent>
    <child>child1</child>
    <!-- This is a comment -->
    <child>child2</child>
    <child>some text <!-- a comment --></child>
    </parent>
    ```

* list item 2

```
<parent>
<child>child1</child>
<!-- This is a comment -->
<child>child2</child>
<child>some text <!-- a comment --></child>
</parent>
```
  
 
 * one
 1. two

foo

  * one
  1. two

foo

   * one
   1. two

foo

   * one
     1. two

foo

 * one
 * two

foo

  * one
  * two

foo

   * one
   * two

foo

   * one
* two

foo

   * one
    * two
  
 
 * one long paragraph of
text
 1. two

foo

  * one long paragraph of
text
   1. two
  
 
* one
1. two

foo

* one
 1. two

foo

* one
  1. two

foo

* one
   1. two

foo

* uli one
* uli two

foo

* uli one
 * uli two

foo

* uli one
  * uli two

foo

* uli one
   * uli two
  
 
- - - a

a

+ - * - - + a

a

1. 2. 3. 4. 5.

a

1. 2. 3. 4. 5. a
  
 
- - - a

+ - * - - + a

1. 2. 3. 4. 5.

1. 2. 3. 4. 5. a
  
 
- - 
a


fooo


- - - aaaaa

   bbbbb
  
 
- - - - -- - - - - - - -- - - - - - - - - - -    - - - - - - - - -  abcd
  
 
   ---

   - - -
  
 
plain text link http://test.com/this_has/one.html with underscores

legit·word_with·1·underscore

a word_with_2underscores (gets em)
  
 
this is a underscore_test ![my cat](http://myserver.com/my_kitty.jpg)

another ![my cat](http://myserver.com/my_kitty.jpg) underscore_test bla
  
 
This is a first paragraph,
on multiple lines.
     
This is a second paragraph.
There are spaces in between the two.
  
 
This is a first paragraph,
on multiple lines.

This is a second paragraph
which has multiple lines too.
  
 
A first paragraph.



A second paragraph after 3 CR (carriage return).
  
 
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
     
A few spaces and a new long long long long long long long long long long long long long long long long paragraph on 1 line.
  
 
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
	
1 tab to separate them and a new long long long long long long long long long long long long long long long long paragraph on 1 line.
  
 
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.

A new long long long long long long long long long long long long long long long long paragraph on 1 line.
  
 
An ampersand & in the text flow is escaped as an html entity.
  
 
There is an [ampersand](http://validator.w3.org/check?uri=http://www.w3.org/&verbose=1) in the URI.
  
 
This is \*an asterisk which should stay as is.
  
 
This is * an asterisk which should stay as is.
  
 
\\   backslash
\`   backtick
\*   asterisk
\_   underscore
\{\}  curly braces
\[\]  square brackets
\(\)  parentheses
\#   hash mark
\+   plus sign
\-   minus sign (hyphen)
\.   dot
\!   exclamation mark
  
 
> # heading level 1
> 
> paragraph
  
 
>A blockquote with a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.

>and a second very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.
  
 
>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a blockquote.
  
 
> A blockquote
> on multiple lines
> like this.
  
 
>A blockquote 
>on multiple lines 
>like this. 
  
 
>A blockquote
>on multiple lines
>like this.
>
>But it has
>two paragraphs.
  
 
>A blockquote
>on multiple lines
>like this
  
 
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.
  
 
> This is the first level of quoting.
>
> > This is nested blockquote.
  
 
> This is the first level of quoting.
> > This is nested blockquote.
> Back to the first level.
  
 
> This is the first level of quoting.
> > This is nested blockquote.
  
 
	10 PRINT HELLO INFINITE
	20 GOTO 10
  
 
    10 PRINT < > &
    20 GOTO 10
  
 
    10 PRINT HELLO INFINITE
    20 GOTO 10
  
 
as*te*risks
  
 
*single asterisks*
  
 
_single underscores_
  
 
HTML entities are written using ampersand notation: &copy;
  
 
These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

  
 
These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

  
 
These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

  
 
This is an H1
=============
  
 
# This is an H1 #
  
 
 # This is an H1
   
 
# this is an h1 with two trailing spaces  
A new paragraph.
  
 
# This is an H1
  
 
This is an H2
-------------
  
 
## This is an H2 ##
  
 
## This is an H2
  
 
### This is an H3 ###
  
 
### This is an H3
  
 
#### This is an H4 ####
  
 
#### This is an H4
  
 
##### This is an H5 #####
  
 
##### This is an H5
  
 
###### This is an H6  ######
  
 
###### This is an H6
  
 
- - -
  
 
---
  
 
***
  
 
___
  
 
-------
  
 
![HTML5][h5]

[h5]: http://www.w3.org/html/logo/img/mark-word-icon.png "HTML5 for everyone"
  
 
![HTML5][h5]

[h5]: http://www.w3.org/html/logo/img/mark-word-icon.png
  
 
![HTML5](http://www.w3.org/html/logo/img/mark-word-icon.png "HTML5 logo for everyone")
  
 
![HTML5](http://www.w3.org/html/logo/img/mark-word-icon.png)
  
 
We love `<code> and &` for everything
  
 
``We love `code` for everything``
  
 
``We love `code` for everything``
  
 
A first sentence  
and a line break.
  
 
A first sentence     
and a line break.
  
 
This is an automatic link <http://www.w3.org/>
  
 
[W3C](http://www.w3.org/ "Discover w3c")
  
 
[W3C](http://www.w3.org/)
  
 
[World Wide Web Consortium][w3c]

[w3c]: <http://www.w3.org/>
  
 
[World Wide Web Consortium][]

[World Wide Web Consortium]: http://www.w3.org/
  
 
[w3c][]

[w3c]: http://www.w3.org/
  
 
[World Wide Web Consortium] [w3c]

[w3c]: http://www.w3.org/
  
 
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/
   "Discover W3C"
  
 
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ (Discover w3c)
  
 
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ 'Discover w3c'
  
 
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ "Discover w3c"
  
 
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/
  
 
*   a list containing a blockquote

    > this the blockquote in the list
  
 
*   a list containing a block of code

	    10 PRINT HELLO INFINITE
	    20 GOTO 10
  
 
*   This is a list item with two paragraphs. Lorem ipsum dolor
	sit amet, consectetuer adipiscing elit. Aliquam hendrerit
	mi posuere lectus.

	Vestibulum enim wisi, viverra nec, fringilla in, laoreet
	vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
	sit amet velit.

*   Suspendisse id sem consectetuer libero luctus adipiscing.
  
 
*   This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

*   Suspendisse id sem consectetuer libero luctus adipiscing.
  
 
1\. ordered list escape
  
 
1. 1

    - inner par list

2. 2
  
 
1. list item 1
8. list item 2
1. list item 3
  
 
1. list item 1
2. list item 2
3. list item 3
  
 
This is a paragraph
on multiple lines
with hard return.
  
 
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
  
 
 This is a paragraph with a trailing and leading space. 
  
 
This is a paragraph with 1 trailing tab.	
  
 
  This is a paragraph with 2 leading spaces.
  
 
   This is a paragraph with 3 leading spaces.
  
 
 This is a paragraph with 1 leading space.
  
 
This is a paragraph with a trailing space.   
 
as**te**risks
  
 
**double asterisks**
  
 
__double underscores__
  
 
* list item 1
* list item 2
* list item 3
  
 
- list item 1
- list item 2
- list item 3
  
 
 * list item 1
 * list item 2
 * list item 3
  
 
  * list item 1
  * list item 2
  * list item 3
  
 
   * list item 1
   * list item 2
   * list item 3
  
 
+ list item 1
+ list item 2
+ list item 3
  
 
* list item in paragraph

* another list item in paragraph
  
 
*   This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a list.
*   and yet another long long long long long long long long long long long long long long long long long long long long long long line.
  
 
*   This is a list item
    with the content on
    multiline and indented.
*   And this another list item
    with the same principle.
  
 
```

## File: `test/cli/basic.html`
```html
<h1 id="sometitle">some title</h1>
```

## File: `test/cli/basic.md`
```markdown
# some title
```

## File: `test/functional/makehtml/makehtml.bootstrap.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */

//jscs:disable requireCamelCaseOrUpperCaseIdentifiers
(function () {
  'use strict';

  require('source-map-support').install();
  require('chai').should();
  let fs = require('fs');

  function getTestSuite (dir) {
    return fs.readdirSync(dir)
      .filter(filter())
      .map(map(dir));
  }

  function getJsonTestSuite (file) {
    let json = JSON.parse(fs.readFileSync(file, 'utf8'));
    return mapJson(json, file);
  }

  function filter () {
    return function (file) {
      let ext = file.slice(-3);
      return (ext === '.md');
    };
  }

  function map (dir) {
    return function (file) {
      let oFile = 'file://' + process.cwd().replace(/\\/g, '/') + dir + file,
          name = file.replace('.md', ''),
          htmlPath = dir + name + '.html',
          html = fs.readFileSync(htmlPath, 'utf8'),
          mdPath = dir + name + '.md',
          md = fs.readFileSync(mdPath, 'utf8');

      return {
        name:     name,
        input:    md,
        expected: html,
        file: oFile
      };
    };
  }

  function mapJson (jsonArray, file) {
    let tcObj = {};
    for (let i = 0; i < jsonArray.length; ++i) {
      let section = jsonArray[i].section;
      let name = jsonArray[i].section + '_' + jsonArray[i].example;
      let md = jsonArray[i].markdown;
      let html = jsonArray[i].html;
      if (!tcObj.hasOwnProperty(section)) {
        tcObj[section] = [];
      }
      tcObj[section].push({
        name: name,
        input: md,
        expected: html,
        file: process.cwd().replace(/\\/g, '/') + file
      });
    }
    return tcObj;
  }


  function assertion (testCase, converter) {
    return function () {
      testCase.actual = converter.makeHtml(testCase.input);
      testCase = normalize(testCase);

      // Compare
      testCase.actual.should.equal(testCase.expected, testCase.file);
    };
  }

  //Normalize input/output
  function normalize (testCase) {

    // Normalize line returns
    testCase.expected = testCase.expected.replace(/(\r\n)|\n|\r/g, '\n');
    testCase.actual = testCase.actual.replace(/(\r\n)|\n|\r/g, '\n');

    // Ignore all leading/trailing whitespace
    testCase.expected = testCase.expected.split('\n').map(function (x) {
      return x.trim();
    }).join('\n');
    testCase.actual = testCase.actual.split('\n').map(function (x) {
      return x.trim();
    }).join('\n');

    // Remove extra lines
    testCase.expected = testCase.expected.trim();
    testCase.actual = testCase.actual.trim();

    //Beautify
    //testCase.expected = beautify(testCase.expected, beauOptions);
    //testCase.actual = beautify(testCase.actual, beauOptions);

    // Normalize line returns
    testCase.expected = testCase.expected.replace(/(\r\n)|\n|\r/g, '\n');
    testCase.actual = testCase.actual.replace(/(\r\n)|\n|\r/g, '\n');

    return testCase;
  }

  module.exports = {
    getTestSuite: getTestSuite,
    getJsonTestSuite: getJsonTestSuite,
    assertion: assertion,
    normalize: normalize,
    showdown: require('../../../.build/showdown.js')
  };
})();

```

## File: `test/functional/makehtml/testsuite.commonmark.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */

// jshint ignore: start
/*
var bootstrap = require('./makehtml.bootstrap.js'),
    converter = new bootstrap.showdown.Converter(),
    assertion = bootstrap.assertion,
    testsuite = bootstrap.getJsonTestSuite('test/functional/makehtml/cases/commonmark.testsuite.json');

describe('makeHtml() commonmark testsuite', function () {
  'use strict';

  for (var section in testsuite) {
    if (testsuite.hasOwnProperty(section)) {
      describe(section, function () {
        for (var i = 0; i < testsuite[section].length; ++i) {
          it(testsuite[section][i].name, assertion(testsuite[section][i], converter));
        }
      });
    }
  }
});
*/
```

## File: `test/functional/makehtml/testsuite.features.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */
var bootstrap = require('./makehtml.bootstrap.js'),
    showdown = bootstrap.showdown,
    assertion = bootstrap.assertion,
    testsuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/'),
    tableSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/tables/'),
    simplifiedAutoLinkSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/simplifiedAutoLink/'),
    openLinksInNewWindowSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/openLinksInNewWindow/'),
    disableForced4SpacesIndentedSublistsSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/disableForced4SpacesIndentedSublists/'),
    rawHeaderIdSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/rawHeaderId/'),
    rawPrefixHeaderIdSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/rawPrefixHeaderId/'),
    emojisSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/emojis/'),
    underlineSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/underline/'),
    ellipsisSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/ellipsis/'),
    literalMidWordUnderscoresSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/literalMidWordUnderscores/'),
    //literalMidWordAsterisksSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/literalMidWordAsterisks/'),
    completeHTMLOutputSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/completeHTMLOutput/'),
    metadataSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/metadata/'),
    splitAdjacentBlockquotesSuite = bootstrap.getTestSuite('test/functional/makehtml/cases/features/splitAdjacentBlockquotes/'),
    moreStyling = bootstrap.getTestSuite('test/functional/makehtml/cases/features/moreStyling/'),
    http = require('http'),
    https = require('https'),
    expect = require('chai').expect;

describe('makeHtml() features testsuite', function () {
  'use strict';

  describe('issues', function () {
    for (var i = 0; i < testsuite.length; ++i) {
      var converter;
      if (testsuite[i].name === '#143.support-image-dimensions') {
        converter = new showdown.Converter({parseImgDimensions: true});
      } else if (testsuite[i].name === '#69.header-level-start') {
        converter = new showdown.Converter({headerLevelStart: 3});
      } else if (testsuite[i].name === '#164.1.simple-autolink' || testsuite[i].name === '#204.certain-links-with-at-and-dot-break-url') {
        converter = new showdown.Converter({simplifiedAutoLink: true});
      } else if (testsuite[i].name === 'literalMidWordUnderscores') {
        converter = new showdown.Converter({literalMidWordUnderscores: true});
      } else if (testsuite[i].name === '#164.2.disallow-underscore-emphasis-mid-word') {
        converter = new showdown.Converter({literalMidWordUnderscores: true});
      } else if (testsuite[i].name === '#164.3.strikethrough' || testsuite[i].name === '#214.escaped-markdown-chars-break-strikethrough') {
        converter = new showdown.Converter({strikethrough: true});
      } else if (testsuite[i].name === 'disable-gh-codeblocks') {
        converter = new showdown.Converter({ghCodeBlocks: false});
      } else if (testsuite[i].name === '#164.4.tasklists') {
        converter = new showdown.Converter({tasklists: true});
      } else if (testsuite[i].name === '#198.literalMidWordUnderscores-changes-behavior-of-asterisk') {
        converter = new showdown.Converter({literalMidWordUnderscores: true});
      } else if (testsuite[i].name === '#259.es6-template-strings-indentation-issues') {
        converter = new showdown.Converter({smartIndentationFix: true});
      } else if (testsuite[i].name === '#284.simplifiedAutoLink-does-not-match-GFM-style') {
        converter = new showdown.Converter({simplifiedAutoLink: true});
      } else if (testsuite[i].name === 'disableForced4SpacesIndentedSublists') {
        converter = new showdown.Converter({disableForced4SpacesIndentedSublists: true});
      } else if (testsuite[i].name === '#206.treat-single-line-breaks-as-br') {
        converter = new showdown.Converter({simpleLineBreaks: true});
      } else if (testsuite[i].name === 'simpleLineBreaks2') {
        converter = new showdown.Converter({simpleLineBreaks: true});
      } else if (testsuite[i].name === '#316.new-simpleLineBreaks-option-breaks-lists') {
        converter = new showdown.Converter({simpleLineBreaks: true});
      } else if (testsuite[i].name === '#323.simpleLineBreaks-breaks-with-strong') {
        converter = new showdown.Converter({simpleLineBreaks: true});
      } else if (testsuite[i].name === '#318.simpleLineBreaks-does-not-work-with-chinese-characters') {
        converter = new showdown.Converter({simpleLineBreaks: true});
      } else if (testsuite[i].name === 'simpleLineBreaks-handle-html-pre') {
        converter = new showdown.Converter({simpleLineBreaks: true});
      } else if (testsuite[i].name === 'excludeTrailingPunctuationFromURLs-option') {
        converter = new showdown.Converter({simplifiedAutoLink: true});
      } else if (testsuite[i].name === 'requireSpaceBeforeHeadingText') {
        converter = new showdown.Converter({requireSpaceBeforeHeadingText: true});
      } else if (testsuite[i].name === '#320.github-compatible-generated-header-id') {
        converter = new showdown.Converter({ghCompatibleHeaderId: true});
      } else if (testsuite[i].name === 'ghMentions') {
        converter = new showdown.Converter({ghMentions: true});
      } else if (testsuite[i].name === 'disable-email-encoding') {
        converter = new showdown.Converter({encodeEmails: false});
      } else if (testsuite[i].name === '#330.simplifiedAutoLink-drops-character-before-and-after-linked-mail') {
        converter = new showdown.Converter({encodeEmails: false, simplifiedAutoLink: true});
      } else if (testsuite[i].name === '#331.allow-escaping-of-tilde') {
        converter = new showdown.Converter({strikethrough: true});
      } else if (testsuite[i].name === 'prefixHeaderId-simple') {
        converter = new showdown.Converter({prefixHeaderId: true});
      } else if (testsuite[i].name === 'prefixHeaderId-string') {
        converter = new showdown.Converter({prefixHeaderId: 'my-prefix-'});
      } else if (testsuite[i].name === 'prefixHeaderId-string-and-ghCompatibleHeaderId') {
        converter = new showdown.Converter({prefixHeaderId: 'my-prefix-', ghCompatibleHeaderId: true});
      } else if (testsuite[i].name === 'prefixHeaderId-string-and-ghCompatibleHeaderId2') {
        converter = new showdown.Converter({prefixHeaderId: 'my prefix ', ghCompatibleHeaderId: true});
      } else if (testsuite[i].name === 'simplifiedAutoLink') {
        converter = new showdown.Converter({simplifiedAutoLink: true, strikethrough: true});
      } else if (testsuite[i].name === 'customizedHeaderId-simple') {
        converter = new showdown.Converter({customizedHeaderId: true});
      } else if (testsuite[i].name === '#378.simplifiedAutoLinks-with-excludeTrailingPunctuationFromURLs') {
        converter = new showdown.Converter({simplifiedAutoLink: true});
      } else if (testsuite[i].name === '#374.escape-html-tags') {
        converter = new showdown.Converter({backslashEscapesHTMLTags: true});
      } else if (testsuite[i].name === '#379.openLinksInNewWindow-breaks-em-markdup') {
        converter = new showdown.Converter({openLinksInNewWindow: true});
      } else if (testsuite[i].name === '#355.simplifiedAutoLink-URLs-inside-parenthesis-followed-by-another-character-are-not-parsed-correctly') {
        converter = new showdown.Converter({simplifiedAutoLink: true});
      } else if (testsuite[i].name === '#709.allow-whitespaces-after-end-in-metadata') {
        converter = new showdown.Converter({metadata: true});
      } else if (testsuite[i].name === 'relativePathBaseUrl') {
        converter = new showdown.Converter({relativePathBaseUrl: 'http://my.site.com/'});
      } else {
        converter = new showdown.Converter();
      }
      it(testsuite[i].name.replace(/-/g, ' '), assertion(testsuite[i], converter));
    }
  });

  /** test Table Syntax Support **/
  describe('table support', function () {
    var converter,
        suite = tableSuite;
    for (var i = 0; i < suite.length; ++i) {
      if (suite[i].name === 'basic-with-header-ids') {
        converter = new showdown.Converter({tables: true, tablesHeaderId: true});
      } else if (suite[i].name === '#179.parse-md-in-table-ths') {
        converter = new showdown.Converter({tables: true, strikethrough: true});
      } else {
        converter = new showdown.Converter({tables: true});
      }
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test simplifiedAutoLink Support **/
  describe('simplifiedAutoLink support in', function () {
    var converter,
        suite = simplifiedAutoLinkSuite;
    for (var i = 0; i < suite.length; ++i) {
      if (suite[i].name === 'emphasis-and-strikethrough') {
        converter = new showdown.Converter({simplifiedAutoLink: true, strikethrough: true});
      } else if (suite[i].name === 'disallow-underscores') {
        converter = new showdown.Converter({literalMidWordUnderscores: true, simplifiedAutoLink: true});
      } else if (suite[i].name === 'disallow-asterisks') {
        converter = new showdown.Converter({literalMidWordAsterisks: true, simplifiedAutoLink: true});
      } else {
        converter = new showdown.Converter({simplifiedAutoLink: true});
      }
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test openLinksInNewWindow support **/
  describe('openLinksInNewWindow support in', function () {
    var converter,
        suite = openLinksInNewWindowSuite;
    for (var i = 0; i < suite.length; ++i) {
      if (suite[i].name === 'simplifiedAutoLink') {
        converter = new showdown.Converter({openLinksInNewWindow: true, simplifiedAutoLink: true});
      } else {
        converter = new showdown.Converter({openLinksInNewWindow: true});
      }
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test disableForced4SpacesIndentedSublists support **/
  describe('disableForced4SpacesIndentedSublists support in', function () {
    var converter,
        suite = disableForced4SpacesIndentedSublistsSuite;
    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({disableForced4SpacesIndentedSublists: true});
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test rawHeaderId support **/
  describe('rawHeaderId support', function () {
    var converter,
        suite = rawHeaderIdSuite;
    for (var i = 0; i < suite.length; ++i) {
      if (suite[i].name === 'with-prefixHeaderId') {
        converter = new showdown.Converter({rawHeaderId: true, prefixHeaderId: '/prefix/'});
      } else {
        converter = new showdown.Converter({rawHeaderId: true});
      }
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test rawPrefixHeaderId support **/
  describe('rawPrefixHeaderId support', function () {
    var converter,
        suite = rawPrefixHeaderIdSuite;
    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({rawPrefixHeaderId: true, prefixHeaderId: '/prefix/'});
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test emojis support **/
  describe('emojis support', function () {
    var converter,
        suite = emojisSuite,
        imgSrcRegexp = /<img[^>]+src=("https?:\/\/[^"]+"|'https?:\/\/[^']+')/g;

    function testImageUrlExists (imgUrl) {
      // Strip the quotes
      imgUrl = imgUrl.slice(1, -1);
      return function (done) {
        (imgUrl.startsWith('http://') ? http : https).get(imgUrl, function (res) {
          expect(res.statusCode).to.equal(200);
          // Make sure we get some data and that it's a png
          expect(parseInt(res.headers['content-length'], 10)).to.be.above(0);
          expect(res.headers['content-type']).to.equal('image/png');

          // Discard the data (but fetch it)
          res.on('data', function () {});

          res.on('end', function () {
            done();
          });
        }).on('error', function (e) {
          throw e;
        });
      };
    }

    for (var i = 0; i < suite.length; ++i) {
      if (suite[i].name === 'simplifiedautolinks') {
        converter = new showdown.Converter({emoji: true, simplifiedAutoLink: true});
      } else {
        converter = new showdown.Converter({emoji: true});
      }

      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));

      var imgUrl = imgSrcRegexp.exec(suite[i].expected);
      if (imgUrl) {
        it('should use a working emoji URL', testImageUrlExists(imgUrl[1]));
      }
    }
  });

  /** test underline support **/
  describe('underline support', function () {
    var converter,
        suite = underlineSuite;
    for (var i = 0; i < suite.length; ++i) {
      if (suite[i].name === 'simplifiedautolinks') {
        converter = new showdown.Converter({underline: true, simplifiedAutoLink: true});
      } else {
        converter = new showdown.Converter({underline: true});
      }
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test ellipsis option **/
  describe('ellipsis option', function () {
    var converter,
        suite = ellipsisSuite;
    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({ellipsis: false});
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test literalMidWordUnderscores option **/
  describe('literalMidWordUnderscores option', function () {
    var converter,
        suite = literalMidWordUnderscoresSuite;
    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({literalMidWordUnderscores: true});
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test literalMidWordAsterisks option **/
  /*
  describe('literalMidWordAsterisks option', function () {
    var converter,
        suite = literalMidWordAsterisksSuite;
    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({literalMidWordAsterisks: true});
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });
  */

  /** test completeHTMLDocument option **/
  describe('completeHTMLDocument option', function () {
    var converter,
        suite = completeHTMLOutputSuite;
    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({completeHTMLDocument: true});

      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test metadata option **/
  describe('metadata option', function () {
    var converter,
        suite = metadataSuite;

    for (var i = 0; i < suite.length; ++i) {
      if (suite[i].name === 'embeded-in-output' ||
        suite[i].name === 'embeded-two-consecutive-metadata-blocks' ||
        suite[i].name === 'embeded-two-consecutive-metadata-blocks-different-symbols') {
        converter = new showdown.Converter({metadata: true, completeHTMLDocument: true});
      } else if (suite[i].name === 'ignore-metadata') {
        converter = new showdown.Converter({metadata: false});
      } else {
        converter = new showdown.Converter({metadata: true});
      }
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test metadata option **/
  describe('splitAdjacentBlockquotes option', function () {
    var converter,
        suite = splitAdjacentBlockquotesSuite;

    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({splitAdjacentBlockquotes: true});
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

  /** test moreStyling option **/
  describe('moreStyling option', function () {
    var converter,
        suite = moreStyling;

    for (var i = 0; i < suite.length; ++i) {
      converter = new showdown.Converter({moreStyling: true, tasklists: true});
      it(suite[i].name.replace(/-/g, ' '), assertion(suite[i], converter));
    }
  });

});
```

## File: `test/functional/makehtml/testsuite.ghost.js`
```javascript
/**
 * Created by Estevao on 14-07-2015.
 */
var bootstrap = require('./makehtml.bootstrap.js'),
    converter = new bootstrap.showdown.Converter({
      strikethrough:             true,
      literalMidWordUnderscores: true,
      simplifiedAutoLink:        true,
      tables:                    true,
      parseImgDimensions:        true, //extra
      tasklists:                 true  //extra
    }),
    assertion = bootstrap.assertion,
    testsuite = bootstrap.getTestSuite('test/functional/makehtml/cases/ghost/');

//MD-Testsuite (borrowed from karlcow/markdown-testsuite)
describe('makeHtml() ghost testsuite', function () {
  'use strict';
  for (var i = 0; i < testsuite.length; ++i) {
    it(testsuite[i].name.replace(/-/g, ' '), assertion(testsuite[i], converter));
  }
});
```

## File: `test/functional/makehtml/testsuite.issues.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */
var bootstrap = require('./makehtml.bootstrap.js'),
    converter = new bootstrap.showdown.Converter(),
    assertion = bootstrap.assertion,
    testsuite = bootstrap.getTestSuite('test/functional/makehtml/cases/issues/');

describe('makeHtml() issues testsuite', function () {
  'use strict';
  for (var i = 0; i < testsuite.length; ++i) {
    it(testsuite[i].name.replace(/-/g, ' '), assertion(testsuite[i], converter));
  }
});
```

## File: `test/functional/makehtml/testsuite.karlcow.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */

var bootstrap = require('./makehtml.bootstrap.js'),
    converter = new bootstrap.showdown.Converter({noHeaderId: true}),
    assertion = bootstrap.assertion,
    testsuite = bootstrap.getTestSuite('test/functional/makehtml/cases/karlcow/');

//MD-Testsuite (borrowed from karlcow/markdown-testsuite)
describe('makeHtml() karlcow testsuite', function () {
  'use strict';
  for (var i = 0; i < testsuite.length; ++i) {
    it(testsuite[i].name.replace(/-/g, ' '), assertion(testsuite[i], converter));
  }
});
```

## File: `test/functional/makehtml/testsuite.standard.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */

var bootstrap = require('./makehtml.bootstrap.js'),
    converter = new bootstrap.showdown.Converter(),
    assertion = bootstrap.assertion,
    testsuite = bootstrap.getTestSuite('test/functional/makehtml/cases/standard/');

describe('makeHtml() standard testsuite', function () {
  'use strict';
  for (var i = 0; i < testsuite.length; ++i) {
    it(testsuite[i].name.replace(/-/g, ' '), assertion(testsuite[i], converter));
  }
});
```

## File: `test/functional/makehtml/cases/commonmark.testsuite.json`
```json
[
  {
    "end_line": 355,
    "section": "Tabs",
    "html": "<pre><code>foo\tbaz\t\tbim\n</code></pre>\n",
    "markdown": "\tfoo\tbaz\t\tbim\n",
    "example": 1,
    "start_line": 350
  },
  {
    "end_line": 362,
    "section": "Tabs",
    "html": "<pre><code>foo\tbaz\t\tbim\n</code></pre>\n",
    "markdown": "  \tfoo\tbaz\t\tbim\n",
    "example": 2,
    "start_line": 357
  },
  {
    "end_line": 371,
    "section": "Tabs",
    "html": "<pre><code>a\ta\nὐ\ta\n</code></pre>\n",
    "markdown": "    a\ta\n    ὐ\ta\n",
    "example": 3,
    "start_line": 364
  },
  {
    "end_line": 388,
    "section": "Tabs",
    "html": "<ul>\n<li>\n<p>foo</p>\n<p>bar</p>\n</li>\n</ul>\n",
    "markdown": "  - foo\n\n\tbar\n",
    "example": 4,
    "start_line": 377
  },
  {
    "end_line": 402,
    "section": "Tabs",
    "html": "<ul>\n<li>\n<p>foo</p>\n<pre><code>  bar\n</code></pre>\n</li>\n</ul>\n",
    "markdown": "- foo\n\n\t\tbar\n",
    "example": 5,
    "start_line": 390
  },
  {
    "end_line": 420,
    "section": "Tabs",
    "html": "<blockquote>\n<pre><code>  foo\n</code></pre>\n</blockquote>\n",
    "markdown": ">\t\tfoo\n",
    "example": 6,
    "start_line": 413
  },
  {
    "end_line": 431,
    "section": "Tabs",
    "html": "<ul>\n<li>\n<pre><code>  foo\n</code></pre>\n</li>\n</ul>\n",
    "markdown": "-\t\tfoo\n",
    "example": 7,
    "start_line": 422
  },
  {
    "end_line": 441,
    "section": "Tabs",
    "html": "<pre><code>foo\nbar\n</code></pre>\n",
    "markdown": "    foo\n\tbar\n",
    "example": 8,
    "start_line": 434
  },
  {
    "end_line": 459,
    "section": "Tabs",
    "html": "<ul>\n<li>foo\n<ul>\n<li>bar\n<ul>\n<li>baz</li>\n</ul>\n</li>\n</ul>\n</li>\n</ul>\n",
    "markdown": " - foo\n   - bar\n\t - baz\n",
    "example": 9,
    "start_line": 443
  },
  {
    "end_line": 465,
    "section": "Tabs",
    "html": "<h1>Foo</h1>\n",
    "markdown": "#\tFoo\n",
    "example": 10,
    "start_line": 461
  },
  {
    "end_line": 471,
    "section": "Tabs",
    "html": "<hr />\n",
    "markdown": "*\t*\t*\t\n",
    "example": 11,
    "start_line": 467
  },
  {
    "end_line": 502,
    "section": "Precedence",
    "html": "<ul>\n<li>`one</li>\n<li>two`</li>\n</ul>\n",
    "markdown": "- `one\n- two`\n",
    "example": 12,
    "start_line": 494
  },
  {
    "end_line": 541,
    "section": "Thematic breaks",
    "html": "<hr />\n<hr />\n<hr />\n",
    "markdown": "***\n\n---\n\n___\n\n",
    "example": 13,
    "start_line": 533
  },
  {
    "end_line": 550,
    "section": "Thematic breaks",
    "html": "<p>+++</p>\n",
    "markdown": "+++\n",
    "example": 14,
    "start_line": 546
  },
  {
    "end_line": 557,
    "section": "Thematic breaks",
    "html": "<p>===</p>\n",
    "markdown": "===\n",
    "example": 15,
    "start_line": 553
  },
  {
    "end_line": 570,
    "section": "Thematic breaks",
    "html": "<p>--\n**\n__</p>\n",
    "markdown": "--\n**\n__\n",
    "example": 16,
    "start_line": 562
  },
  {
    "end_line": 583,
    "section": "Thematic breaks",
    "html": "<hr />\n<hr />\n<hr />\n",
    "markdown": " ***\n  ***\n   ***\n",
    "example": 17,
    "start_line": 575
  },
  {
    "end_line": 593,
    "section": "Thematic breaks",
    "html": "<pre><code>***\n</code></pre>\n",
    "markdown": "    ***\n",
    "example": 18,
    "start_line": 588
  },
  {
    "end_line": 602,
    "section": "Thematic breaks",
    "html": "<p>Foo\n***</p>\n",
    "markdown": "Foo\n    ***\n",
    "example": 19,
    "start_line": 596
  },
  {
    "end_line": 611,
    "section": "Thematic breaks",
    "html": "<hr />\n",
    "markdown": "_____________________________________\n",
    "example": 20,
    "start_line": 607
  },
  {
    "end_line": 620,
    "section": "Thematic breaks",
    "html": "<hr />\n",
    "markdown": " - - -\n",
    "example": 21,
    "start_line": 616
  },
  {
    "end_line": 627,
    "section": "Thematic breaks",
    "html": "<hr />\n",
    "markdown": " **  * ** * ** * **\n",
    "example": 22,
    "start_line": 623
  },
  {
    "end_line": 634,
    "section": "Thematic breaks",
    "html": "<hr />\n",
    "markdown": "-     -      -      -\n",
    "example": 23,
    "start_line": 630
  },
  {
    "end_line": 643,
    "section": "Thematic breaks",
    "html": "<hr />\n",
    "markdown": "- - - -    \n",
    "example": 24,
    "start_line": 639
  },
  {
    "end_line": 658,
    "section": "Thematic breaks",
    "html": "<p>_ _ _ _ a</p>\n<p>a------</p>\n<p>---a---</p>\n",
    "markdown": "_ _ _ _ a\n\na------\n\n---a---\n",
    "example": 25,
    "start_line": 648
  },
  {
    "end_line": 668,
    "section": "Thematic breaks",
    "html": "<p><em>-</em></p>\n",
    "markdown": " *-*\n",
    "example": 26,
    "start_line": 664
  },
  {
    "end_line": 685,
    "section": "Thematic breaks",
    "html": "<ul>\n<li>foo</li>\n</ul>\n<hr />\n<ul>\n<li>bar</li>\n</ul>\n",
    "markdown": "- foo\n***\n- bar\n",
    "example": 27,
    "start_line": 673
  },
  {
    "end_line": 698,
    "section": "Thematic breaks",
    "html": "<p>Foo</p>\n<hr />\n<p>bar</p>\n",
    "markdown": "Foo\n***\nbar\n",
    "example": 28,
    "start_line": 690
  },
  {
    "end_line": 714,
    "section": "Thematic breaks",
    "html": "<h2>Foo</h2>\n<p>bar</p>\n",
    "markdown": "Foo\n---\nbar\n",
    "example": 29,
    "start_line": 707
  },
  {
    "end_line": 732,
    "section": "Thematic breaks",
    "html": "<ul>\n<li>Foo</li>\n</ul>\n<hr />\n<ul>\n<li>Bar</li>\n</ul>\n",
    "markdown": "* Foo\n* * *\n* Bar\n",
    "example": 30,
    "start_line": 720
  },
  {
    "end_line": 747,
    "section": "Thematic breaks",
    "html": "<ul>\n<li>Foo</li>\n<li>\n<hr />\n</li>\n</ul>\n",
    "markdown": "- Foo\n- * * *\n",
    "example": 31,
    "start_line": 737
  },
  {
    "end_line": 780,
    "section": "ATX headings",
    "html": "<h1>foo</h1>\n<h2>foo</h2>\n<h3>foo</h3>\n<h4>foo</h4>\n<h5>foo</h5>\n<h6>foo</h6>\n",
    "markdown": "# foo\n## foo\n### foo\n#### foo\n##### foo\n###### foo\n",
    "example": 32,
    "start_line": 766
  },
  {
    "end_line": 789,
    "section": "ATX headings",
    "html": "<p>####### foo</p>\n",
    "markdown": "####### foo\n",
    "example": 33,
    "start_line": 785
  },
  {
    "end_line": 807,
    "section": "ATX headings",
    "html": "<p>#5 bolt</p>\n<p>#hashtag</p>\n",
    "markdown": "#5 bolt\n\n#hashtag\n",
    "example": 34,
    "start_line": 800
  },
  {
    "end_line": 816,
    "section": "ATX headings",
    "html": "<p>## foo</p>\n",
    "markdown": "\\## foo\n",
    "example": 35,
    "start_line": 812
  },
  {
    "end_line": 825,
    "section": "ATX headings",
    "html": "<h1>foo <em>bar</em> *baz*</h1>\n",
    "markdown": "# foo *bar* \\*baz\\*\n",
    "example": 36,
    "start_line": 821
  },
  {
    "end_line": 834,
    "section": "ATX headings",
    "html": "<h1>foo</h1>\n",
    "markdown": "#                  foo                     \n",
    "example": 37,
    "start_line": 830
  },
  {
    "end_line": 847,
    "section": "ATX headings",
    "html": "<h3>foo</h3>\n<h2>foo</h2>\n<h1>foo</h1>\n",
    "markdown": " ### foo\n  ## foo\n   # foo\n",
    "example": 38,
    "start_line": 839
  },
  {
    "end_line": 857,
    "section": "ATX headings",
    "html": "<pre><code># foo\n</code></pre>\n",
    "markdown": "    # foo\n",
    "example": 39,
    "start_line": 852
  },
  {
    "end_line": 866,
    "section": "ATX headings",
    "html": "<p>foo\n# bar</p>\n",
    "markdown": "foo\n    # bar\n",
    "example": 40,
    "start_line": 860
  },
  {
    "end_line": 877,
    "section": "ATX headings",
    "html": "<h2>foo</h2>\n<h3>bar</h3>\n",
    "markdown": "## foo ##\n  ###   bar    ###\n",
    "example": 41,
    "start_line": 871
  },
  {
    "end_line": 888,
    "section": "ATX headings",
    "html": "<h1>foo</h1>\n<h5>foo</h5>\n",
    "markdown": "# foo ##################################\n##### foo ##\n",
    "example": 42,
    "start_line": 882
  },
  {
    "end_line": 897,
    "section": "ATX headings",
    "html": "<h3>foo</h3>\n",
    "markdown": "### foo ###     \n",
    "example": 43,
    "start_line": 893
  },
  {
    "end_line": 908,
    "section": "ATX headings",
    "html": "<h3>foo ### b</h3>\n",
    "markdown": "### foo ### b\n",
    "example": 44,
    "start_line": 904
  },
  {
    "end_line": 917,
    "section": "ATX headings",
    "html": "<h1>foo#</h1>\n",
    "markdown": "# foo#\n",
    "example": 45,
    "start_line": 913
  },
  {
    "end_line": 931,
    "section": "ATX headings",
    "html": "<h3>foo ###</h3>\n<h2>foo ###</h2>\n<h1>foo #</h1>\n",
    "markdown": "### foo \\###\n## foo #\\##\n# foo \\#\n",
    "example": 46,
    "start_line": 923
  },
  {
    "end_line": 945,
    "section": "ATX headings",
    "html": "<hr />\n<h2>foo</h2>\n<hr />\n",
    "markdown": "****\n## foo\n****\n",
    "example": 47,
    "start_line": 937
  },
  {
    "end_line": 956,
    "section": "ATX headings",
    "html": "<p>Foo bar</p>\n<h1>baz</h1>\n<p>Bar foo</p>\n",
    "markdown": "Foo bar\n# baz\nBar foo\n",
    "example": 48,
    "start_line": 948
  },
  {
    "end_line": 969,
    "section": "ATX headings",
    "html": "<h2></h2>\n<h1></h1>\n<h3></h3>\n",
    "markdown": "## \n#\n### ###\n",
    "example": 49,
    "start_line": 961
  },
  {
    "end_line": 1013,
    "section": "Setext headings",
    "html": "<h1>Foo <em>bar</em></h1>\n<h2>Foo <em>bar</em></h2>\n",
    "markdown": "Foo *bar*\n=========\n\nFoo *bar*\n---------\n",
    "example": 50,
    "start_line": 1004
  },
  {
    "end_line": 1025,
    "section": "Setext headings",
    "html": "<h1>Foo <em>bar\nbaz</em></h1>\n",
    "markdown": "Foo *bar\nbaz*\n====\n",
    "example": 51,
    "start_line": 1018
  },
  {
    "end_line": 1039,
    "section": "Setext headings",
    "html": "<h2>Foo</h2>\n<h1>Foo</h1>\n",
    "markdown": "Foo\n-------------------------\n\nFoo\n=\n",
    "example": 52,
    "start_line": 1030
  },
  {
    "end_line": 1058,
    "section": "Setext headings",
    "html": "<h2>Foo</h2>\n<h2>Foo</h2>\n<h1>Foo</h1>\n",
    "markdown": "   Foo\n---\n\n  Foo\n-----\n\n  Foo\n  ===\n",
    "example": 53,
    "start_line": 1045
  },
  {
    "end_line": 1076,
    "section": "Setext headings",
    "html": "<pre><code>Foo\n---\n\nFoo\n</code></pre>\n<hr />\n",
    "markdown": "    Foo\n    ---\n\n    Foo\n---\n",
    "example": 54,
    "start_line": 1063
  },
  {
    "end_line": 1087,
    "section": "Setext headings",
    "html": "<h2>Foo</h2>\n",
    "markdown": "Foo\n   ----      \n",
    "example": 55,
    "start_line": 1082
  },
  {
    "end_line": 1098,
    "section": "Setext headings",
    "html": "<p>Foo\n---</p>\n",
    "markdown": "Foo\n    ---\n",
    "example": 56,
    "start_line": 1092
  },
  {
    "end_line": 1114,
    "section": "Setext headings",
    "html": "<p>Foo\n= =</p>\n<p>Foo</p>\n<hr />\n",
    "markdown": "Foo\n= =\n\nFoo\n--- -\n",
    "example": 57,
    "start_line": 1103
  },
  {
    "end_line": 1124,
    "section": "Setext headings",
    "html": "<h2>Foo</h2>\n",
    "markdown": "Foo  \n-----\n",
    "example": 58,
    "start_line": 1119
  },
  {
    "end_line": 1134,
    "section": "Setext headings",
    "html": "<h2>Foo\\</h2>\n",
    "markdown": "Foo\\\n----\n",
    "example": 59,
    "start_line": 1129
  },
  {
    "end_line": 1153,
    "section": "Setext headings",
    "html": "<h2>`Foo</h2>\n<p>`</p>\n<h2>&lt;a title=&quot;a lot</h2>\n<p>of dashes&quot;/&gt;</p>\n",
    "markdown": "`Foo\n----\n`\n\n<a title=\"a lot\n---\nof dashes\"/>\n",
    "example": 60,
    "start_line": 1140
  },
  {
    "end_line": 1167,
    "section": "Setext headings",
    "html": "<blockquote>\n<p>Foo</p>\n</blockquote>\n<hr />\n",
    "markdown": "> Foo\n---\n",
    "example": 61,
    "start_line": 1159
  },
  {
    "end_line": 1180,
    "section": "Setext headings",
    "html": "<blockquote>\n<p>foo\nbar\n===</p>\n</blockquote>\n",
    "markdown": "> foo\nbar\n===\n",
    "example": 62,
    "start_line": 1170
  },
  {
    "end_line": 1191,
    "section": "Setext headings",
    "html": "<ul>\n<li>Foo</li>\n</ul>\n<hr />\n",
    "markdown": "- Foo\n---\n",
    "example": 63,
    "start_line": 1183
  },
  {
    "end_line": 1205,
    "section": "Setext headings",
    "html": "<h2>Foo\nBar</h2>\n",
    "markdown": "Foo\nBar\n---\n",
    "example": 64,
    "start_line": 1198
  },
  {
    "end_line": 1223,
    "section": "Setext headings",
    "html": "<hr />\n<h2>Foo</h2>\n<h2>Bar</h2>\n<p>Baz</p>\n",
    "markdown": "---\nFoo\n---\nBar\n---\nBaz\n",
    "example": 65,
    "start_line": 1211
  },
  {
    "end_line": 1233,
    "section": "Setext headings",
    "html": "<p>====</p>\n",
    "markdown": "\n====\n",
    "example": 66,
    "start_line": 1228
  },
  {
    "end_line": 1246,
    "section": "Setext headings",
    "html": "<hr />\n<hr />\n",
    "markdown": "---\n---\n",
    "example": 67,
    "start_line": 1240
  },
  {
    "end_line": 1257,
    "section": "Setext headings",
    "html": "<ul>\n<li>foo</li>\n</ul>\n<hr />\n",
    "markdown": "- foo\n-----\n",
    "example": 68,
    "start_line": 1249
  },
  {
    "end_line": 1267,
    "section": "Setext headings",
    "html": "<pre><code>foo\n</code></pre>\n<hr />\n",
    "markdown": "    foo\n---\n",
    "example": 69,
    "start_line": 1260
  },
  {
    "end_line": 1278,
    "section": "Setext headings",
    "html": "<blockquote>\n<p>foo</p>\n</blockquote>\n<hr />\n",
    "markdown": "> foo\n-----\n",
    "example": 70,
    "start_line": 1270
  },
  {
    "end_line": 1289,
    "section": "Setext headings",
    "html": "<h2>&gt; foo</h2>\n",
    "markdown": "\\> foo\n------\n",
    "example": 71,
    "start_line": 1284
  },
  {
    "end_line": 1325,
    "section": "Setext headings",
    "html": "<p>Foo</p>\n<h2>bar</h2>\n<p>baz</p>\n",
    "markdown": "Foo\n\nbar\n---\nbaz\n",
    "example": 72,
    "start_line": 1315
  },
  {
    "end_line": 1343,
    "section": "Setext headings",
    "html": "<p>Foo\nbar</p>\n<hr />\n<p>baz</p>\n",
    "markdown": "Foo\nbar\n\n---\n\nbaz\n",
    "example": 73,
    "start_line": 1331
  },
  {
    "end_line": 1359,
    "section": "Setext headings",
    "html": "<p>Foo\nbar</p>\n<hr />\n<p>baz</p>\n",
    "markdown": "Foo\nbar\n* * *\nbaz\n",
    "example": 74,
    "start_line": 1349
  },
  {
    "end_line": 1374,
    "section": "Setext headings",
    "html": "<p>Foo\nbar\n---\nbaz</p>\n",
    "markdown": "Foo\nbar\n\\---\nbaz\n",
    "example": 75,
    "start_line": 1364
  },
  {
    "end_line": 1399,
    "section": "Indented code blocks",
    "html": "<pre><code>a simple\n  indented code block\n</code></pre>\n",
    "markdown": "    a simple\n      indented code block\n",
    "example": 76,
    "start_line": 1392
  },
  {
    "end_line": 1417,
    "section": "Indented code blocks",
    "html": "<ul>\n<li>\n<p>foo</p>\n<p>bar</p>\n</li>\n</ul>\n",
    "markdown": "  - foo\n\n    bar\n",
    "example": 77,
    "start_line": 1406
  },
  {
    "end_line": 1433,
    "section": "Indented code blocks",
    "html": "<ol>\n<li>\n<p>foo</p>\n<ul>\n<li>bar</li>\n</ul>\n</li>\n</ol>\n",
    "markdown": "1.  foo\n\n    - bar\n",
    "example": 78,
    "start_line": 1420
  },
  {
    "end_line": 1451,
    "section": "Indented code blocks",
    "html": "<pre><code>&lt;a/&gt;\n*hi*\n\n- one\n</code></pre>\n",
    "markdown": "    <a/>\n    *hi*\n\n    - one\n",
    "example": 79,
    "start_line": 1440
  },
  {
    "end_line": 1473,
    "section": "Indented code blocks",
    "html": "<pre><code>chunk1\n\nchunk2\n\n\n\nchunk3\n</code></pre>\n",
    "markdown": "    chunk1\n\n    chunk2\n  \n \n \n    chunk3\n",
    "example": 80,
    "start_line": 1456
  },
  {
    "end_line": 1488,
    "section": "Indented code blocks",
    "html": "<pre><code>chunk1\n  \n  chunk2\n</code></pre>\n",
    "markdown": "    chunk1\n      \n      chunk2\n",
    "example": 81,
    "start_line": 1479
  },
  {
    "end_line": 1501,
    "section": "Indented code blocks",
    "html": "<p>Foo\nbar</p>\n",
    "markdown": "Foo\n    bar\n\n",
    "example": 82,
    "start_line": 1494
  },
  {
    "end_line": 1515,
    "section": "Indented code blocks",
    "html": "<pre><code>foo\n</code></pre>\n<p>bar</p>\n",
    "markdown": "    foo\nbar\n",
    "example": 83,
    "start_line": 1508
  },
  {
    "end_line": 1536,
    "section": "Indented code blocks",
    "html": "<h1>Heading</h1>\n<pre><code>foo\n</code></pre>\n<h2>Heading</h2>\n<pre><code>foo\n</code></pre>\n<hr />\n",
    "markdown": "# Heading\n    foo\nHeading\n------\n    foo\n----\n",
    "example": 84,
    "start_line": 1521
  },
  {
    "end_line": 1548,
    "section": "Indented code blocks",
    "html": "<pre><code>    foo\nbar\n</code></pre>\n",
    "markdown": "        foo\n    bar\n",
    "example": 85,
    "start_line": 1541
  },
  {
    "end_line": 1563,
    "section": "Indented code blocks",
    "html": "<pre><code>foo\n</code></pre>\n",
    "markdown": "\n    \n    foo\n    \n\n",
    "example": 86,
    "start_line": 1554
  },
  {
    "end_line": 1573,
    "section": "Indented code blocks",
    "html": "<pre><code>foo  \n</code></pre>\n",
    "markdown": "    foo  \n",
    "example": 87,
    "start_line": 1568
  },
  {
    "end_line": 1632,
    "section": "Fenced code blocks",
    "html": "<pre><code>&lt;\n &gt;\n</code></pre>\n",
    "markdown": "```\n<\n >\n```\n",
    "example": 88,
    "start_line": 1623
  },
  {
    "end_line": 1646,
    "section": "Fenced code blocks",
    "html": "<pre><code>&lt;\n &gt;\n</code></pre>\n",
    "markdown": "~~~\n<\n >\n~~~\n",
    "example": 89,
    "start_line": 1637
  },
  {
    "end_line": 1656,
    "section": "Fenced code blocks",
    "html": "<p><code>foo</code></p>\n",
    "markdown": "``\nfoo\n``\n",
    "example": 90,
    "start_line": 1650
  },
  {
    "end_line": 1670,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n~~~\n</code></pre>\n",
    "markdown": "```\naaa\n~~~\n```\n",
    "example": 91,
    "start_line": 1661
  },
  {
    "end_line": 1682,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n```\n</code></pre>\n",
    "markdown": "~~~\naaa\n```\n~~~\n",
    "example": 92,
    "start_line": 1673
  },
  {
    "end_line": 1696,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n```\n</code></pre>\n",
    "markdown": "````\naaa\n```\n``````\n",
    "example": 93,
    "start_line": 1687
  },
  {
    "end_line": 1708,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n~~~\n</code></pre>\n",
    "markdown": "~~~~\naaa\n~~~\n~~~~\n",
    "example": 94,
    "start_line": 1699
  },
  {
    "end_line": 1718,
    "section": "Fenced code blocks",
    "html": "<pre><code></code></pre>\n",
    "markdown": "```\n",
    "example": 95,
    "start_line": 1714
  },
  {
    "end_line": 1731,
    "section": "Fenced code blocks",
    "html": "<pre><code>\n```\naaa\n</code></pre>\n",
    "markdown": "`````\n\n```\naaa\n",
    "example": 96,
    "start_line": 1721
  },
  {
    "end_line": 1745,
    "section": "Fenced code blocks",
    "html": "<blockquote>\n<pre><code>aaa\n</code></pre>\n</blockquote>\n<p>bbb</p>\n",
    "markdown": "> ```\n> aaa\n\nbbb\n",
    "example": 97,
    "start_line": 1734
  },
  {
    "end_line": 1759,
    "section": "Fenced code blocks",
    "html": "<pre><code>\n  \n</code></pre>\n",
    "markdown": "```\n\n  \n```\n",
    "example": 98,
    "start_line": 1750
  },
  {
    "end_line": 1769,
    "section": "Fenced code blocks",
    "html": "<pre><code></code></pre>\n",
    "markdown": "```\n```\n",
    "example": 99,
    "start_line": 1764
  },
  {
    "end_line": 1785,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\naaa\n</code></pre>\n",
    "markdown": " ```\n aaa\naaa\n```\n",
    "example": 100,
    "start_line": 1776
  },
  {
    "end_line": 1799,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\naaa\naaa\n</code></pre>\n",
    "markdown": "  ```\naaa\n  aaa\naaa\n  ```\n",
    "example": 101,
    "start_line": 1788
  },
  {
    "end_line": 1813,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n aaa\naaa\n</code></pre>\n",
    "markdown": "   ```\n   aaa\n    aaa\n  aaa\n   ```\n",
    "example": 102,
    "start_line": 1802
  },
  {
    "end_line": 1827,
    "section": "Fenced code blocks",
    "html": "<pre><code>```\naaa\n```\n</code></pre>\n",
    "markdown": "    ```\n    aaa\n    ```\n",
    "example": 103,
    "start_line": 1818
  },
  {
    "end_line": 1840,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n</code></pre>\n",
    "markdown": "```\naaa\n  ```\n",
    "example": 104,
    "start_line": 1833
  },
  {
    "end_line": 1850,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n</code></pre>\n",
    "markdown": "   ```\naaa\n  ```\n",
    "example": 105,
    "start_line": 1843
  },
  {
    "end_line": 1863,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n    ```\n</code></pre>\n",
    "markdown": "```\naaa\n    ```\n",
    "example": 106,
    "start_line": 1855
  },
  {
    "end_line": 1875,
    "section": "Fenced code blocks",
    "html": "<p><code></code>\naaa</p>\n",
    "markdown": "``` ```\naaa\n",
    "example": 107,
    "start_line": 1869
  },
  {
    "end_line": 1886,
    "section": "Fenced code blocks",
    "html": "<pre><code>aaa\n~~~ ~~\n</code></pre>\n",
    "markdown": "~~~~~~\naaa\n~~~ ~~\n",
    "example": 108,
    "start_line": 1878
  },
  {
    "end_line": 1903,
    "section": "Fenced code blocks",
    "html": "<p>foo</p>\n<pre><code>bar\n</code></pre>\n<p>baz</p>\n",
    "markdown": "foo\n```\nbar\n```\nbaz\n",
    "example": 109,
    "start_line": 1892
  },
  {
    "end_line": 1921,
    "section": "Fenced code blocks",
    "html": "<h2>foo</h2>\n<pre><code>bar\n</code></pre>\n<h1>baz</h1>\n",
    "markdown": "foo\n---\n~~~\nbar\n~~~\n# baz\n",
    "example": 110,
    "start_line": 1909
  },
  {
    "end_line": 1940,
    "section": "Fenced code blocks",
    "html": "<pre><code class=\"language-ruby\">def foo(x)\n  return 3\nend\n</code></pre>\n",
    "markdown": "```ruby\ndef foo(x)\n  return 3\nend\n```\n",
    "example": 111,
    "start_line": 1929
  },
  {
    "end_line": 1954,
    "section": "Fenced code blocks",
    "html": "<pre><code class=\"language-ruby\">def foo(x)\n  return 3\nend\n</code></pre>\n",
    "markdown": "~~~~    ruby startline=3 $%@#$\ndef foo(x)\n  return 3\nend\n~~~~~~~\n",
    "example": 112,
    "start_line": 1943
  },
  {
    "end_line": 1962,
    "section": "Fenced code blocks",
    "html": "<pre><code class=\"language-;\"></code></pre>\n",
    "markdown": "````;\n````\n",
    "example": 113,
    "start_line": 1957
  },
  {
    "end_line": 1973,
    "section": "Fenced code blocks",
    "html": "<p><code>aa</code>\nfoo</p>\n",
    "markdown": "``` aa ```\nfoo\n",
    "example": 114,
    "start_line": 1967
  },
  {
    "end_line": 1985,
    "section": "Fenced code blocks",
    "html": "<pre><code>``` aaa\n</code></pre>\n",
    "markdown": "```\n``` aaa\n```\n",
    "example": 115,
    "start_line": 1978
  },
  {
    "end_line": 2070,
    "section": "HTML blocks",
    "html": "<table><tr><td>\n<pre>\n**Hello**,\n<p><em>world</em>.\n</pre></p>\n</td></tr></table>\n",
    "markdown": "<table><tr><td>\n<pre>\n**Hello**,\n\n_world_.\n</pre>\n</td></tr></table>\n",
    "example": 116,
    "start_line": 2055
  },
  {
    "end_line": 2103,
    "section": "HTML blocks",
    "html": "<table>\n  <tr>\n    <td>\n           hi\n    </td>\n  </tr>\n</table>\n<p>okay.</p>\n",
    "markdown": "<table>\n  <tr>\n    <td>\n           hi\n    </td>\n  </tr>\n</table>\n\nokay.\n",
    "example": 117,
    "start_line": 2084
  },
  {
    "end_line": 2114,
    "section": "HTML blocks",
    "html": " <div>\n  *hello*\n         <foo><a>\n",
    "markdown": " <div>\n  *hello*\n         <foo><a>\n",
    "example": 118,
    "start_line": 2106
  },
  {
    "end_line": 2125,
    "section": "HTML blocks",
    "html": "</div>\n*foo*\n",
    "markdown": "</div>\n*foo*\n",
    "example": 119,
    "start_line": 2119
  },
  {
    "end_line": 2140,
    "section": "HTML blocks",
    "html": "<DIV CLASS=\"foo\">\n<p><em>Markdown</em></p>\n</DIV>\n",
    "markdown": "<DIV CLASS=\"foo\">\n\n*Markdown*\n\n</DIV>\n",
    "example": 120,
    "start_line": 2130
  },
  {
    "end_line": 2154,
    "section": "HTML blocks",
    "html": "<div id=\"foo\"\n  class=\"bar\">\n</div>\n",
    "markdown": "<div id=\"foo\"\n  class=\"bar\">\n</div>\n",
    "example": 121,
    "start_line": 2146
  },
  {
    "end_line": 2165,
    "section": "HTML blocks",
    "html": "<div id=\"foo\" class=\"bar\n  baz\">\n</div>\n",
    "markdown": "<div id=\"foo\" class=\"bar\n  baz\">\n</div>\n",
    "example": 122,
    "start_line": 2157
  },
  {
    "end_line": 2178,
    "section": "HTML blocks",
    "html": "<div>\n*foo*\n<p><em>bar</em></p>\n",
    "markdown": "<div>\n*foo*\n\n*bar*\n",
    "example": 123,
    "start_line": 2169
  },
  {
    "end_line": 2191,
    "section": "HTML blocks",
    "html": "<div id=\"foo\"\n*hi*\n",
    "markdown": "<div id=\"foo\"\n*hi*\n",
    "example": 124,
    "start_line": 2185
  },
  {
    "end_line": 2200,
    "section": "HTML blocks",
    "html": "<div class\nfoo\n",
    "markdown": "<div class\nfoo\n",
    "example": 125,
    "start_line": 2194
  },
  {
    "end_line": 2212,
    "section": "HTML blocks",
    "html": "<div *???-&&&-<---\n*foo*\n",
    "markdown": "<div *???-&&&-<---\n*foo*\n",
    "example": 126,
    "start_line": 2206
  },
  {
    "end_line": 2222,
    "section": "HTML blocks",
    "html": "<div><a href=\"bar\">*foo*</a></div>\n",
    "markdown": "<div><a href=\"bar\">*foo*</a></div>\n",
    "example": 127,
    "start_line": 2218
  },
  {
    "end_line": 2233,
    "section": "HTML blocks",
    "html": "<table><tr><td>\nfoo\n</td></tr></table>\n",
    "markdown": "<table><tr><td>\nfoo\n</td></tr></table>\n",
    "example": 128,
    "start_line": 2225
  },
  {
    "end_line": 2252,
    "section": "HTML blocks",
    "html": "<div></div>\n``` c\nint x = 33;\n```\n",
    "markdown": "<div></div>\n``` c\nint x = 33;\n```\n",
    "example": 129,
    "start_line": 2242
  },
  {
    "end_line": 2267,
    "section": "HTML blocks",
    "html": "<a href=\"foo\">\n*bar*\n</a>\n",
    "markdown": "<a href=\"foo\">\n*bar*\n</a>\n",
    "example": 130,
    "start_line": 2259
  },
  {
    "end_line": 2280,
    "section": "HTML blocks",
    "html": "<Warning>\n*bar*\n</Warning>\n",
    "markdown": "<Warning>\n*bar*\n</Warning>\n",
    "example": 131,
    "start_line": 2272
  },
  {
    "end_line": 2291,
    "section": "HTML blocks",
    "html": "<i class=\"foo\">\n*bar*\n</i>\n",
    "markdown": "<i class=\"foo\">\n*bar*\n</i>\n",
    "example": 132,
    "start_line": 2283
  },
  {
    "end_line": 2300,
    "section": "HTML blocks",
    "html": "</ins>\n*bar*\n",
    "markdown": "</ins>\n*bar*\n",
    "example": 133,
    "start_line": 2294
  },
  {
    "end_line": 2317,
    "section": "HTML blocks",
    "html": "<del>\n*foo*\n</del>\n",
    "markdown": "<del>\n*foo*\n</del>\n",
    "example": 134,
    "start_line": 2309
  },
  {
    "end_line": 2334,
    "section": "HTML blocks",
    "html": "<del>\n<p><em>foo</em></p>\n</del>\n",
    "markdown": "<del>\n\n*foo*\n\n</del>\n",
    "example": 135,
    "start_line": 2324
  },
  {
    "end_line": 2346,
    "section": "HTML blocks",
    "html": "<p><del><em>foo</em></del></p>\n",
    "markdown": "<del>*foo*</del>\n",
    "example": 136,
    "start_line": 2342
  },
  {
    "end_line": 2374,
    "section": "HTML blocks",
    "html": "<pre language=\"haskell\"><code>\nimport Text.HTML.TagSoup\n\nmain :: IO ()\nmain = print $ parseTags tags\n</code></pre>\n<p>okay</p>\n",
    "markdown": "<pre language=\"haskell\"><code>\nimport Text.HTML.TagSoup\n\nmain :: IO ()\nmain = print $ parseTags tags\n</code></pre>\nokay\n",
    "example": 137,
    "start_line": 2358
  },
  {
    "end_line": 2393,
    "section": "HTML blocks",
    "html": "<script type=\"text/javascript\">\n// JavaScript example\n\ndocument.getElementById(\"demo\").innerHTML = \"Hello JavaScript!\";\n</script>\n<p>okay</p>\n",
    "markdown": "<script type=\"text/javascript\">\n// JavaScript example\n\ndocument.getElementById(\"demo\").innerHTML = \"Hello JavaScript!\";\n</script>\nokay\n",
    "example": 138,
    "start_line": 2379
  },
  {
    "end_line": 2414,
    "section": "HTML blocks",
    "html": "<style\n  type=\"text/css\">\nh1 {color:red;}\n\np {color:blue;}\n</style>\n<p>okay</p>\n",
    "markdown": "<style\n  type=\"text/css\">\nh1 {color:red;}\n\np {color:blue;}\n</style>\nokay\n",
    "example": 139,
    "start_line": 2398
  },
  {
    "end_line": 2431,
    "section": "HTML blocks",
    "html": "<style\n  type=\"text/css\">\n\nfoo\n",
    "markdown": "<style\n  type=\"text/css\">\n\nfoo\n",
    "example": 140,
    "start_line": 2421
  },
  {
    "end_line": 2445,
    "section": "HTML blocks",
    "html": "<blockquote>\n<div>\nfoo\n</blockquote>\n<p>bar</p>\n",
    "markdown": "> <div>\n> foo\n\nbar\n",
    "example": 141,
    "start_line": 2434
  },
  {
    "end_line": 2458,
    "section": "HTML blocks",
    "html": "<ul>\n<li>\n<div>\n</li>\n<li>foo</li>\n</ul>\n",
    "markdown": "- <div>\n- foo\n",
    "example": 142,
    "start_line": 2448
  },
  {
    "end_line": 2469,
    "section": "HTML blocks",
    "html": "<style>p{color:red;}</style>\n<p><em>foo</em></p>\n",
    "markdown": "<style>p{color:red;}</style>\n*foo*\n",
    "example": 143,
    "start_line": 2463
  },
  {
    "end_line": 2478,
    "section": "HTML blocks",
    "html": "<!-- foo -->*bar*\n<p><em>baz</em></p>\n",
    "markdown": "<!-- foo -->*bar*\n*baz*\n",
    "example": 144,
    "start_line": 2472
  },
  {
    "end_line": 2492,
    "section": "HTML blocks",
    "html": "<script>\nfoo\n</script>1. *bar*\n",
    "markdown": "<script>\nfoo\n</script>1. *bar*\n",
    "example": 145,
    "start_line": 2484
  },
  {
    "end_line": 2509,
    "section": "HTML blocks",
    "html": "<!-- Foo\n\nbar\n   baz -->\n<p>okay</p>\n",
    "markdown": "<!-- Foo\n\nbar\n   baz -->\nokay\n",
    "example": 146,
    "start_line": 2497
  },
  {
    "end_line": 2529,
    "section": "HTML blocks",
    "html": "<?php\n\n  echo '>';\n\n?>\n<p>okay</p>\n",
    "markdown": "<?php\n\n  echo '>';\n\n?>\nokay\n",
    "example": 147,
    "start_line": 2515
  },
  {
    "end_line": 2538,
    "section": "HTML blocks",
    "html": "<!DOCTYPE html>\n",
    "markdown": "<!DOCTYPE html>\n",
    "example": 148,
    "start_line": 2534
  },
  {
    "end_line": 2571,
    "section": "HTML blocks",
    "html": "<![CDATA[\nfunction matchwo(a,b)\n{\n  if (a < b && a < 0) then {\n    return 1;\n\n  } else {\n\n    return 0;\n  }\n}\n]]>\n<p>okay</p>\n",
    "markdown": "<![CDATA[\nfunction matchwo(a,b)\n{\n  if (a < b && a < 0) then {\n    return 1;\n\n  } else {\n\n    return 0;\n  }\n}\n]]>\nokay\n",
    "example": 149,
    "start_line": 2543
  },
  {
    "end_line": 2584,
    "section": "HTML blocks",
    "html": "  <!-- foo -->\n<pre><code>&lt;!-- foo --&gt;\n</code></pre>\n",
    "markdown": "  <!-- foo -->\n\n    <!-- foo -->\n",
    "example": 150,
    "start_line": 2576
  },
  {
    "end_line": 2595,
    "section": "HTML blocks",
    "html": "  <div>\n<pre><code>&lt;div&gt;\n</code></pre>\n",
    "markdown": "  <div>\n\n    <div>\n",
    "example": 151,
    "start_line": 2587
  },
  {
    "end_line": 2611,
    "section": "HTML blocks",
    "html": "<p>Foo</p>\n<div>\nbar\n</div>\n",
    "markdown": "Foo\n<div>\nbar\n</div>\n",
    "example": 152,
    "start_line": 2601
  },
  {
    "end_line": 2627,
    "section": "HTML blocks",
    "html": "<div>\nbar\n</div>\n*foo*\n",
    "markdown": "<div>\nbar\n</div>\n*foo*\n",
    "example": 153,
    "start_line": 2617
  },
  {
    "end_line": 2640,
    "section": "HTML blocks",
    "html": "<p>Foo\n<a href=\"bar\">\nbaz</p>\n",
    "markdown": "Foo\n<a href=\"bar\">\nbaz\n",
    "example": 154,
    "start_line": 2632
  },
  {
    "end_line": 2683,
    "section": "HTML blocks",
    "html": "<div>\n<p><em>Emphasized</em> text.</p>\n</div>\n",
    "markdown": "<div>\n\n*Emphasized* text.\n\n</div>\n",
    "example": 155,
    "start_line": 2673
  },
  {
    "end_line": 2694,
    "section": "HTML blocks",
    "html": "<div>\n*Emphasized* text.\n</div>\n",
    "markdown": "<div>\n*Emphasized* text.\n</div>\n",
    "example": 156,
    "start_line": 2686
  },
  {
    "end_line": 2728,
    "section": "HTML blocks",
    "html": "<table>\n<tr>\n<td>\nHi\n</td>\n</tr>\n</table>\n",
    "markdown": "<table>\n\n<tr>\n\n<td>\nHi\n</td>\n\n</tr>\n\n</table>\n",
    "example": 157,
    "start_line": 2708
  },
  {
    "end_line": 2756,
    "section": "HTML blocks",
    "html": "<table>\n  <tr>\n<pre><code>&lt;td&gt;\n  Hi\n&lt;/td&gt;\n</code></pre>\n  </tr>\n</table>\n",
    "markdown": "<table>\n\n  <tr>\n\n    <td>\n      Hi\n    </td>\n\n  </tr>\n\n</table>\n",
    "example": 158,
    "start_line": 2735
  },
  {
    "end_line": 2789,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/url\" title=\"title\">foo</a></p>\n",
    "markdown": "[foo]: /url \"title\"\n\n[foo]\n",
    "example": 159,
    "start_line": 2783
  },
  {
    "end_line": 2800,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/url\" title=\"the title\">foo</a></p>\n",
    "markdown": "   [foo]: \n      /url  \n           'the title'  \n\n[foo]\n",
    "example": 160,
    "start_line": 2792
  },
  {
    "end_line": 2809,
    "section": "Link reference definitions",
    "html": "<p><a href=\"my_(url)\" title=\"title (with parens)\">Foo*bar]</a></p>\n",
    "markdown": "[Foo*bar\\]]:my_(url) 'title (with parens)'\n\n[Foo*bar\\]]\n",
    "example": 161,
    "start_line": 2803
  },
  {
    "end_line": 2820,
    "section": "Link reference definitions",
    "html": "<p><a href=\"my%20url\" title=\"title\">Foo bar</a></p>\n",
    "markdown": "[Foo bar]:\n<my%20url>\n'title'\n\n[Foo bar]\n",
    "example": 162,
    "start_line": 2812
  },
  {
    "end_line": 2839,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/url\" title=\"\ntitle\nline1\nline2\n\">foo</a></p>\n",
    "markdown": "[foo]: /url '\ntitle\nline1\nline2\n'\n\n[foo]\n",
    "example": 163,
    "start_line": 2825
  },
  {
    "end_line": 2854,
    "section": "Link reference definitions",
    "html": "<p>[foo]: /url 'title</p>\n<p>with blank line'</p>\n<p>[foo]</p>\n",
    "markdown": "[foo]: /url 'title\n\nwith blank line'\n\n[foo]\n",
    "example": 164,
    "start_line": 2844
  },
  {
    "end_line": 2866,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/url\">foo</a></p>\n",
    "markdown": "[foo]:\n/url\n\n[foo]\n",
    "example": 165,
    "start_line": 2859
  },
  {
    "end_line": 2878,
    "section": "Link reference definitions",
    "html": "<p>[foo]:</p>\n<p>[foo]</p>\n",
    "markdown": "[foo]:\n\n[foo]\n",
    "example": 166,
    "start_line": 2871
  },
  {
    "end_line": 2890,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/url%5Cbar*baz\" title=\"foo&quot;bar\\baz\">foo</a></p>\n",
    "markdown": "[foo]: /url\\bar\\*baz \"foo\\\"bar\\baz\"\n\n[foo]\n",
    "example": 167,
    "start_line": 2884
  },
  {
    "end_line": 2901,
    "section": "Link reference definitions",
    "html": "<p><a href=\"url\">foo</a></p>\n",
    "markdown": "[foo]\n\n[foo]: url\n",
    "example": 168,
    "start_line": 2895
  },
  {
    "end_line": 2914,
    "section": "Link reference definitions",
    "html": "<p><a href=\"first\">foo</a></p>\n",
    "markdown": "[foo]\n\n[foo]: first\n[foo]: second\n",
    "example": 169,
    "start_line": 2907
  },
  {
    "end_line": 2926,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/url\">Foo</a></p>\n",
    "markdown": "[FOO]: /url\n\n[Foo]\n",
    "example": 170,
    "start_line": 2920
  },
  {
    "end_line": 2935,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/%CF%86%CE%BF%CF%85\">αγω</a></p>\n",
    "markdown": "[ΑΓΩ]: /φου\n\n[αγω]\n",
    "example": 171,
    "start_line": 2929
  },
  {
    "end_line": 2944,
    "section": "Link reference definitions",
    "html": "",
    "markdown": "[foo]: /url\n",
    "example": 172,
    "start_line": 2941
  },
  {
    "end_line": 2956,
    "section": "Link reference definitions",
    "html": "<p>bar</p>\n",
    "markdown": "[\nfoo\n]: /url\nbar\n",
    "example": 173,
    "start_line": 2949
  },
  {
    "end_line": 2966,
    "section": "Link reference definitions",
    "html": "<p>[foo]: /url &quot;title&quot; ok</p>\n",
    "markdown": "[foo]: /url \"title\" ok\n",
    "example": 174,
    "start_line": 2962
  },
  {
    "end_line": 2976,
    "section": "Link reference definitions",
    "html": "<p>&quot;title&quot; ok</p>\n",
    "markdown": "[foo]: /url\n\"title\" ok\n",
    "example": 175,
    "start_line": 2971
  },
  {
    "end_line": 2990,
    "section": "Link reference definitions",
    "html": "<pre><code>[foo]: /url &quot;title&quot;\n</code></pre>\n<p>[foo]</p>\n",
    "markdown": "    [foo]: /url \"title\"\n\n[foo]\n",
    "example": 176,
    "start_line": 2982
  },
  {
    "end_line": 3006,
    "section": "Link reference definitions",
    "html": "<pre><code>[foo]: /url\n</code></pre>\n<p>[foo]</p>\n",
    "markdown": "```\n[foo]: /url\n```\n\n[foo]\n",
    "example": 177,
    "start_line": 2996
  },
  {
    "end_line": 3020,
    "section": "Link reference definitions",
    "html": "<p>Foo\n[bar]: /baz</p>\n<p>[bar]</p>\n",
    "markdown": "Foo\n[bar]: /baz\n\n[bar]\n",
    "example": 178,
    "start_line": 3011
  },
  {
    "end_line": 3035,
    "section": "Link reference definitions",
    "html": "<h1><a href=\"/url\">Foo</a></h1>\n<blockquote>\n<p>bar</p>\n</blockquote>\n",
    "markdown": "# [Foo]\n[foo]: /url\n> bar\n",
    "example": 179,
    "start_line": 3026
  },
  {
    "end_line": 3054,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/foo-url\" title=\"foo\">foo</a>,\n<a href=\"/bar-url\" title=\"bar\">bar</a>,\n<a href=\"/baz-url\">baz</a></p>\n",
    "markdown": "[foo]: /foo-url \"foo\"\n[bar]: /bar-url\n  \"bar\"\n[baz]: /baz-url\n\n[foo],\n[bar],\n[baz]\n",
    "example": 180,
    "start_line": 3041
  },
  {
    "end_line": 3070,
    "section": "Link reference definitions",
    "html": "<p><a href=\"/url\">foo</a></p>\n<blockquote>\n</blockquote>\n",
    "markdown": "[foo]\n\n> [foo]: /url\n",
    "example": 181,
    "start_line": 3062
  },
  {
    "end_line": 3092,
    "section": "Paragraphs",
    "html": "<p>aaa</p>\n<p>bbb</p>\n",
    "markdown": "aaa\n\nbbb\n",
    "example": 182,
    "start_line": 3085
  },
  {
    "end_line": 3108,
    "section": "Paragraphs",
    "html": "<p>aaa\nbbb</p>\n<p>ccc\nddd</p>\n",
    "markdown": "aaa\nbbb\n\nccc\nddd\n",
    "example": 183,
    "start_line": 3097
  },
  {
    "end_line": 3121,
    "section": "Paragraphs",
    "html": "<p>aaa</p>\n<p>bbb</p>\n",
    "markdown": "aaa\n\n\nbbb\n",
    "example": 184,
    "start_line": 3113
  },
  {
    "end_line": 3132,
    "section": "Paragraphs",
    "html": "<p>aaa\nbbb</p>\n",
    "markdown": "  aaa\n bbb\n",
    "example": 185,
    "start_line": 3126
  },
  {
    "end_line": 3146,
    "section": "Paragraphs",
    "html": "<p>aaa\nbbb\nccc</p>\n",
    "markdown": "aaa\n             bbb\n                                       ccc\n",
    "example": 186,
    "start_line": 3138
  },
  {
    "end_line": 3158,
    "section": "Paragraphs",
    "html": "<p>aaa\nbbb</p>\n",
    "markdown": "   aaa\nbbb\n",
    "example": 187,
    "start_line": 3152
  },
  {
    "end_line": 3168,
    "section": "Paragraphs",
    "html": "<pre><code>aaa\n</code></pre>\n<p>bbb</p>\n",
    "markdown": "    aaa\nbbb\n",
    "example": 188,
    "start_line": 3161
  },
  {
    "end_line": 3181,
    "section": "Paragraphs",
    "html": "<p>aaa<br />\nbbb</p>\n",
    "markdown": "aaa     \nbbb     \n",
    "example": 189,
    "start_line": 3175
  },
  {
    "end_line": 3204,
    "section": "Blank lines",
    "html": "<p>aaa</p>\n<h1>aaa</h1>\n",
    "markdown": "  \n\naaa\n  \n\n# aaa\n\n  \n",
    "example": 190,
    "start_line": 3192
  },
  {
    "end_line": 3268,
    "section": "Block quotes",
    "html": "<blockquote>\n<h1>Foo</h1>\n<p>bar\nbaz</p>\n</blockquote>\n",
    "markdown": "> # Foo\n> bar\n> baz\n",
    "example": 191,
    "start_line": 3258
  },
  {
    "end_line": 3283,
    "section": "Block quotes",
    "html": "<blockquote>\n<h1>Foo</h1>\n<p>bar\nbaz</p>\n</blockquote>\n",
    "markdown": "># Foo\n>bar\n> baz\n",
    "example": 192,
    "start_line": 3273
  },
  {
    "end_line": 3298,
    "section": "Block quotes",
    "html": "<blockquote>\n<h1>Foo</h1>\n<p>bar\nbaz</p>\n</blockquote>\n",
    "markdown": "   > # Foo\n   > bar\n > baz\n",
    "example": 193,
    "start_line": 3288
  },
  {
    "end_line": 3312,
    "section": "Block quotes",
    "html": "<pre><code>&gt; # Foo\n&gt; bar\n&gt; baz\n</code></pre>\n",
    "markdown": "    > # Foo\n    > bar\n    > baz\n",
    "example": 194,
    "start_line": 3303
  },
  {
    "end_line": 3328,
    "section": "Block quotes",
    "html": "<blockquote>\n<h1>Foo</h1>\n<p>bar\nbaz</p>\n</blockquote>\n",
    "markdown": "> # Foo\n> bar\nbaz\n",
    "example": 195,
    "start_line": 3318
  },
  {
    "end_line": 3344,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>bar\nbaz\nfoo</p>\n</blockquote>\n",
    "markdown": "> bar\nbaz\n> foo\n",
    "example": 196,
    "start_line": 3334
  },
  {
    "end_line": 3366,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>foo</p>\n</blockquote>\n<hr />\n",
    "markdown": "> foo\n---\n",
    "example": 197,
    "start_line": 3358
  },
  {
    "end_line": 3390,
    "section": "Block quotes",
    "html": "<blockquote>\n<ul>\n<li>foo</li>\n</ul>\n</blockquote>\n<ul>\n<li>bar</li>\n</ul>\n",
    "markdown": "> - foo\n- bar\n",
    "example": 198,
    "start_line": 3378
  },
  {
    "end_line": 3406,
    "section": "Block quotes",
    "html": "<blockquote>\n<pre><code>foo\n</code></pre>\n</blockquote>\n<pre><code>bar\n</code></pre>\n",
    "markdown": ">     foo\n    bar\n",
    "example": 199,
    "start_line": 3396
  },
  {
    "end_line": 3419,
    "section": "Block quotes",
    "html": "<blockquote>\n<pre><code></code></pre>\n</blockquote>\n<p>foo</p>\n<pre><code></code></pre>\n",
    "markdown": "> ```\nfoo\n```\n",
    "example": 200,
    "start_line": 3409
  },
  {
    "end_line": 3433,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>foo\n- bar</p>\n</blockquote>\n",
    "markdown": "> foo\n    - bar\n",
    "example": 201,
    "start_line": 3425
  },
  {
    "end_line": 3454,
    "section": "Block quotes",
    "html": "<blockquote>\n</blockquote>\n",
    "markdown": ">\n",
    "example": 202,
    "start_line": 3449
  },
  {
    "end_line": 3464,
    "section": "Block quotes",
    "html": "<blockquote>\n</blockquote>\n",
    "markdown": ">\n>  \n> \n",
    "example": 203,
    "start_line": 3457
  },
  {
    "end_line": 3477,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>foo</p>\n</blockquote>\n",
    "markdown": ">\n> foo\n>  \n",
    "example": 204,
    "start_line": 3469
  },
  {
    "end_line": 3493,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>foo</p>\n</blockquote>\n<blockquote>\n<p>bar</p>\n</blockquote>\n",
    "markdown": "> foo\n\n> bar\n",
    "example": 205,
    "start_line": 3482
  },
  {
    "end_line": 3512,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>foo\nbar</p>\n</blockquote>\n",
    "markdown": "> foo\n> bar\n",
    "example": 206,
    "start_line": 3504
  },
  {
    "end_line": 3526,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>foo</p>\n<p>bar</p>\n</blockquote>\n",
    "markdown": "> foo\n>\n> bar\n",
    "example": 207,
    "start_line": 3517
  },
  {
    "end_line": 3539,
    "section": "Block quotes",
    "html": "<p>foo</p>\n<blockquote>\n<p>bar</p>\n</blockquote>\n",
    "markdown": "foo\n> bar\n",
    "example": 208,
    "start_line": 3531
  },
  {
    "end_line": 3557,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>aaa</p>\n</blockquote>\n<hr />\n<blockquote>\n<p>bbb</p>\n</blockquote>\n",
    "markdown": "> aaa\n***\n> bbb\n",
    "example": 209,
    "start_line": 3545
  },
  {
    "end_line": 3571,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>bar\nbaz</p>\n</blockquote>\n",
    "markdown": "> bar\nbaz\n",
    "example": 210,
    "start_line": 3563
  },
  {
    "end_line": 3583,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>bar</p>\n</blockquote>\n<p>baz</p>\n",
    "markdown": "> bar\n\nbaz\n",
    "example": 211,
    "start_line": 3574
  },
  {
    "end_line": 3595,
    "section": "Block quotes",
    "html": "<blockquote>\n<p>bar</p>\n</blockquote>\n<p>baz</p>\n",
    "markdown": "> bar\n>\nbaz\n",
    "example": 212,
    "start_line": 3586
  },
  {
    "end_line": 3614,
    "section": "Block quotes",
    "html": "<blockquote>\n<blockquote>\n<blockquote>\n<p>foo\nbar</p>\n</blockquote>\n</blockquote>\n</blockquote>\n",
    "markdown": "> > > foo\nbar\n",
    "example": 213,
    "start_line": 3602
  },
  {
    "end_line": 3631,
    "section": "Block quotes",
    "html": "<blockquote>\n<blockquote>\n<blockquote>\n<p>foo\nbar\nbaz</p>\n</blockquote>\n</blockquote>\n</blockquote>\n",
    "markdown": ">>> foo\n> bar\n>>baz\n",
    "example": 214,
    "start_line": 3617
  },
  {
    "end_line": 3651,
    "section": "Block quotes",
    "html": "<blockquote>\n<pre><code>code\n</code></pre>\n</blockquote>\n<blockquote>\n<p>not code</p>\n</blockquote>\n",
    "markdown": ">     code\n\n>    not code\n",
    "example": 215,
    "start_line": 3639
  },
  {
    "end_line": 3709,
    "section": "List items",
    "html": "<p>A paragraph\nwith two lines.</p>\n<pre><code>indented code\n</code></pre>\n<blockquote>\n<p>A block quote.</p>\n</blockquote>\n",
    "markdown": "A paragraph\nwith two lines.\n\n    indented code\n\n> A block quote.\n",
    "example": 216,
    "start_line": 3694
  },
  {
    "end_line": 3735,
    "section": "List items",
    "html": "<ol>\n<li>\n<p>A paragraph\nwith two lines.</p>\n<pre><code>indented code\n</code></pre>\n<blockquote>\n<p>A block quote.</p>\n</blockquote>\n</li>\n</ol>\n",
    "markdown": "1.  A paragraph\n    with two lines.\n\n        indented code\n\n    > A block quote.\n",
    "example": 217,
    "start_line": 3716
  },
  {
    "end_line": 3758,
    "section": "List items",
    "html": "<ul>\n<li>one</li>\n</ul>\n<p>two</p>\n",
    "markdown": "- one\n\n two\n",
    "example": 218,
    "start_line": 3749
  },
  {
    "end_line": 3772,
    "section": "List items",
    "html": "<ul>\n<li>\n<p>one</p>\n<p>two</p>\n</li>\n</ul>\n",
    "markdown": "- one\n\n  two\n",
    "example": 219,
    "start_line": 3761
  },
  {
    "end_line": 3785,
    "section": "List items",
    "html": "<ul>\n<li>one</li>\n</ul>\n<pre><code> two\n</code></pre>\n",
    "markdown": " -    one\n\n     two\n",
    "example": 220,
    "start_line": 3775
  },
  {
    "end_line": 3799,
    "section": "List items",
    "html": "<ul>\n<li>\n<p>one</p>\n<p>two</p>\n</li>\n</ul>\n",
    "markdown": " -    one\n\n      two\n",
    "example": 221,
    "start_line": 3788
  },
  {
    "end_line": 3825,
    "section": "List items",
    "html": "<blockquote>\n<blockquote>\n<ol>\n<li>\n<p>one</p>\n<p>two</p>\n</li>\n</ol>\n</blockquote>\n</blockquote>\n",
    "markdown": "   > > 1.  one\n>>\n>>     two\n",
    "example": 222,
    "start_line": 3810
  },
  {
    "end_line": 3850,
    "section": "List items",
    "html": "<blockquote>\n<blockquote>\n<ul>\n<li>one</li>\n</ul>\n<p>two</p>\n</blockquote>\n</blockquote>\n",
    "markdown": ">>- one\n>>\n  >  > two\n",
    "example": 223,
    "start_line": 3837
  },
  {
    "end_line": 3863,
    "section": "List items",
    "html": "<p>-one</p>\n<p>2.two</p>\n",
    "markdown": "-one\n\n2.two\n",
    "example": 224,
    "start_line": 3856
  },
  {
    "end_line": 3881,
    "section": "List items",
    "html": "<ul>\n<li>\n<p>foo</p>\n<p>bar</p>\n</li>\n</ul>\n",
    "markdown": "- foo\n\n\n  bar\n",
    "example": 225,
    "start_line": 3869
  },
  {
    "end_line": 3908,
    "section": "List items",
    "html": "<ol>\n<li>\n<p>foo</p>\n<pre><code>bar\n</code></pre>\n<p>baz</p>\n<blockquote>\n<p>bam</p>\n</blockquote>\n</li>\n</ol>\n",
    "markdown": "1.  foo\n\n    ```\n    bar\n    ```\n\n    baz\n\n    > bam\n",
    "example": 226,
    "start_line": 3886
  },
  {
    "end_line": 3932,
    "section": "List items",
    "html": "<ul>\n<li>\n<p>Foo</p>\n<pre><code>bar\n\n\nbaz\n</code></pre>\n</li>\n</ul>\n",
    "markdown": "- Foo\n\n      bar\n\n\n      baz\n",
    "example": 227,
    "start_line": 3914
  },
  {
    "end_line": 3942,
    "section": "List items",
    "html": "<ol start=\"123456789\">\n<li>ok</li>\n</ol>\n",
    "markdown": "123456789. ok\n",
    "example": 228,
    "start_line": 3936
  },
  {
    "end_line": 3949,
    "section": "List items",
    "html": "<p>1234567890. not ok</p>\n",
    "markdown": "1234567890. not ok\n",
    "example": 229,
    "start_line": 3945
  },
  {
    "end_line": 3960,
    "section": "List items",
    "html": "<ol start=\"0\">\n<li>ok</li>\n</ol>\n",
    "markdown": "0. ok\n",
    "example": 230,
    "start_line": 3954
  },
  {
    "end_line": 3969,
    "section": "List items",
    "html": "<ol start=\"3\">\n<li>ok</li>\n</ol>\n",
    "markdown": "003. ok\n",
    "example": 231,
    "start_line": 3963
  },
  {
    "end_line": 3978,
    "section": "List items",
    "html": "<p>-1. not ok</p>\n",
    "markdown": "-1. not ok\n",
    "example": 232,
    "start_line": 3974
  },
  {
    "end_line": 4010,
    "section": "List items",
    "html": "<ul>\n<li>\n<p>foo</p>\n<pre><code>bar\n</code></pre>\n</li>\n</ul>\n",
    "markdown": "- foo\n\n      bar\n",
    "example": 233,
    "start_line": 3998
  },
  {
    "end_line": 4027,
    "section": "List items",
    "html": "<ol start=\"10\">\n<li>\n<p>foo</p>\n<pre><code>bar\n</code></pre>\n</li>\n</ol>\n",
    "markdown": "  10.  foo\n\n           bar\n",
    "example": 234,
    "start_line": 4015
  },
  {
    "end_line": 4046,
    "section": "List items",
    "html": "<pre><code>indented code\n</code></pre>\n<p>paragraph</p>\n<pre><code>more code\n</code></pre>\n",
    "markdown": "    indented code\n\nparagraph\n\n    more code\n",
    "example": 235,
    "start_line": 4034
  },
  {
    "end_line": 4065,
    "section": "List items",
    "html": "<ol>\n<li>\n<pre><code>indented code\n</code></pre>\n<p>paragraph</p>\n<pre><code>more code\n</code></pre>\n</li>\n</ol>\n",
    "markdown": "1.     indented code\n\n   paragraph\n\n       more code\n",
    "example": 236,
    "start_line": 4049
  },
  {
    "end_line": 4087,
    "section": "List items",
    "html": "<ol>\n<li>\n<pre><code> indented code\n</code></pre>\n<p>paragraph</p>\n<pre><code>more code\n</code></pre>\n</li>\n</ol>\n",
    "markdown": "1.      indented code\n\n   paragraph\n\n       more code\n",
    "example": 237,
    "start_line": 4071
  },
  {
    "end_line": 4105,
    "section": "List items",
    "html": "<p>foo</p>\n<p>bar</p>\n",
    "markdown": "   foo\n\nbar\n",
    "example": 238,
    "start_line": 4098
  },
  {
    "end_line": 4117,
    "section": "List items",
    "html": "<ul>\n<li>foo</li>\n</ul>\n<p>bar</p>\n",
    "markdown": "-    foo\n\n  bar\n",
    "example": 239,
    "start_line": 4108
  },
  {
    "end_line": 4136,
    "section": "List items",
    "html": "<ul>\n<li>\n<p>foo</p>\n<p>bar</p>\n</li>\n</ul>\n",
    "markdown": "-  foo\n\n   bar\n",
    "example": 240,
    "start_line": 4125
  },
  {
    "end_line": 4174,
    "section": "List items",
    "html": "<ul>\n<li>foo</li>\n<li>\n<pre><code>bar\n</code></pre>\n</li>\n<li>\n<pre><code>baz\n</code></pre>\n</li>\n</ul>\n",
    "markdown": "-\n  foo\n-\n  ```\n  bar\n  ```\n-\n      baz\n",
    "example": 241,
    "start_line": 4153
  },
  {
    "end_line": 4186,
    "section": "List items",
    "html": "<ul>\n<li>foo</li>\n</ul>\n",
    "markdown": "-   \n  foo\n",
    "example": 242,
    "start_line": 4179
  },
  {
    "end_line": 4202,
    "section": "List items",
    "html": "<ul>\n<li></li>\n</ul>\n<p>foo</p>\n",
    "markdown": "-\n\n  foo\n",
    "example": 243,
    "start_line": 4193
  },
  {
    "end_line": 4217,
    "section": "List items",
    "html": "<ul>\n<li>foo</li>\n<li></li>\n<li>bar</li>\n</ul>\n",
    "markdown": "- foo\n-\n- bar\n",
    "example": 244,
    "start_line": 4207
  },
  {
    "end_line": 4232,
    "section": "List items",
    "html": "<ul>\n<li>foo</li>\n<li></li>\n<li>bar</li>\n</ul>\n",
    "markdown": "- foo\n-   \n- bar\n",
    "example": 245,
    "start_line": 4222
  },
  {
    "end_line": 4247,
    "section": "List items",
    "html": "<ol>\n<li>foo</li>\n<li></li>\n<li>bar</li>\n</ol>\n",
    "markdown": "1. foo\n2.\n3. bar\n",
    "example": 246,
    "start_line": 4237
  },
  {
    "end_line": 4258,
    "section": "List items",
    "html": "<ul>\n<li></li>\n</ul>\n",
    "markdown": "*\n",
    "example": 247,
    "start_line": 4252
  },
  {
    "end_line": 4273,
    "section": "List items",
    "html": "<p>foo\n*</p>\n<p>foo\n1.</p>\n",
    "markdown": "foo\n*\n\nfoo\n1.\n",
    "example": 248,
    "start_line": 4262
  },
  {
    "end_line": 4303,
    "section": "List items",
    "html": "<ol>\n<li>\n<p>A paragraph\nwith two lines.</p>\n<pre><code>indented code\n</code></pre>\n<blockquote>\n<p>A block quote.</p>\n</blockquote>\n</li>\n</ol>\n",
    "markdown": " 1.  A paragraph\n     with two lines.\n\n         indented code\n\n     > A block quote.\n",
    "example": 249,
    "start_line": 4284
  },
  {
    "end_line": 4327,
    "section": "List items",
    "html": "<ol>\n<li>\n<p>A paragraph\nwith two lines.</p>\n<pre><code>indented code\n</code></pre>\n<blockquote>\n<p>A block quote.</p>\n</blockquote>\n</li>\n</ol>\n",
    "markdown": "  1.  A paragraph\n      with two lines.\n\n          indented code\n\n      > A block quote.\n",
    "example": 250,
    "start_line": 4308
  },
  {
    "end_line": 4351,
    "section": "List items",
    "html": "<ol>\n<li>\n<p>A paragraph\nwith two lines.</p>\n<pre><code>indented code\n</code></pre>\n<blockquote>\n<p>A block quote.</p>\n</blockquote>\n</li>\n</ol>\n",
    "markdown": "   1.  A paragraph\n       with two lines.\n\n           indented code\n\n       > A block quote.\n",
    "example": 251,
    "start_line": 4332
  },
  {
    "end_line": 4371,
    "section": "List items",
    "html": "<pre><code>1.  A paragraph\n    with two lines.\n\n        indented code\n\n    &gt; A block quote.\n</code></pre>\n",
    "markdown": "    1.  A paragraph\n        with two lines.\n\n            indented code\n\n        > A block quote.\n",
    "example": 252,
    "start_line": 4356
  },
  {
    "end_line": 4405,
    "section": "List items",
    "html": "<ol>\n<li>\n<p>A paragraph\nwith two lines.</p>\n<pre><code>indented code\n</code></pre>\n<blockquote>\n<p>A block quote.</p>\n</blockquote>\n</li>\n</ol>\n",
    "markdown": "  1.  A paragraph\nwith two lines.\n\n          indented code\n\n      > A block quote.\n",
    "example": 253,
    "start_line": 4386
  },
  {
    "end_line": 4418,
    "section": "List items",
    "html": "<ol>\n<li>A paragraph\nwith two lines.</li>\n</ol>\n",
    "markdown": "  1.  A paragraph\n    with two lines.\n",
    "example": 254,
    "start_line": 4410
  },
  {
    "end_line": 4437,
    "section": "List items",
    "html": "<blockquote>\n<ol>\n<li>\n<blockquote>\n<p>Blockquote\ncontinued here.</p>\n</blockquote>\n</li>\n</ol>\n</blockquote>\n",
    "markdown": "> 1. > Blockquote\ncontinued here.\n",
    "example": 255,
    "start_line": 4423
  },
  {
    "end_line": 4454,
    "section": "List items",
    "html": "<blockquote>\n<ol>\n<li>\n<blockquote>\n<p>Blockquote\ncontinued here.</p>\n</blockquote>\n</li>\n</ol>\n</blockquote>\n",
    "markdown": "> 1. > Blockquote\n> continued here.\n",
    "example": 256,
    "start_line": 4440
  },
  {
    "end_line": 4488,
    "section": "List items",
    "html": "<ul>\n<li>foo\n<ul>\n<li>bar\n<ul>\n<li>baz\n<ul>\n<li>boo</li>\n</ul>\n</li>\n</ul>\n</li>\n</ul>\n</li>\n</ul>\n",
    "markdown": "- foo\n  - bar\n    - baz\n      - boo\n",
    "example": 257,
    "start_line": 4467
  },
  {
    "end_line": 4505,
    "section": "List items",
    "html": "<ul>\n<li>foo</li>\n<li>bar</li>\n<li>baz</li>\n<li>boo</li>\n</ul>\n",
    "markdown": "- foo\n - bar\n  - baz\n   - boo\n",
    "example": 258,
    "start_line": 4493
  },
  {
    "end_line": 4521,
    "section": "List items",
    "html": "<ol start=\"10\">\n<li>foo\n<ul>\n<li>bar</li>\n</ul>\n</li>\n</ol>\n",
    "markdown": "10) foo\n    - bar\n",
    "example": 259,
    "start_line": 4510
  },
  {
    "end_line": 4536,
    "section": "List items",
    "html": "<ol start=\"10\">\n<li>foo</li>\n</ol>\n<ul>\n<li>bar</li>\n</ul>\n",
    "markdown": "10) foo\n   - bar\n",
    "example": 260,
    "start_line": 4526
  },
  {
    "end_line": 4551,
    "section": "List items",
    "html": "<ul>\n<li>\n<ul>\n<li>foo</li>\n</ul>\n</li>\n</ul>\n",
    "markdown": "- - foo\n",
    "example": 261,
    "start_line": 4541
  },
  {
    "end_line": 4568,
    "section": "List items",
    "html": "<ol>\n<li>\n<ul>\n<li>\n<ol start=\"2\">\n<li>foo</li>\n</ol>\n</li>\n</ul>\n</li>\n</ol>\n",
    "markdown": "1. - 2. foo\n",
    "example": 262,
    "start_line": 4554
  },
  {
    "end_line": 4587,
    "section": "List items",
    "html": "<ul>\n<li>\n<h1>Foo</h1>\n</li>\n<li>\n<h2>Bar</h2>\nbaz</li>\n</ul>\n",
    "markdown": "- # Foo\n- Bar\n  ---\n  baz\n",
    "example": 263,
    "start_line": 4573
  },
  {
    "end_line": 4821,
    "section": "Lists",
    "html": "<ul>\n<li>foo</li>\n<li>bar</li>\n</ul>\n<ul>\n<li>baz</li>\n</ul>\n",
    "markdown": "- foo\n- bar\n+ baz\n",
    "example": 264,
    "start_line": 4809
  },
  {
    "end_line": 4836,
    "section": "Lists",
    "html": "<ol>\n<li>foo</li>\n<li>bar</li>\n</ol>\n<ol start=\"3\">\n<li>baz</li>\n</ol>\n",
    "markdown": "1. foo\n2. bar\n3) baz\n",
    "example": 265,
    "start_line": 4824
  },
  {
    "end_line": 4853,
    "section": "Lists",
    "html": "<p>Foo</p>\n<ul>\n<li>bar</li>\n<li>baz</li>\n</ul>\n",
    "markdown": "Foo\n- bar\n- baz\n",
    "example": 266,
    "start_line": 4843
  },
  {
    "end_line": 4926,
    "section": "Lists",
    "html": "<p>The number of windows in my house is\n14.  The number of doors is 6.</p>\n",
    "markdown": "The number of windows in my house is\n14.  The number of doors is 6.\n",
    "example": 267,
    "start_line": 4920
  },
  {
    "end_line": 4938,
    "section": "Lists",
    "html": "<p>The number of windows in my house is</p>\n<ol>\n<li>The number of doors is 6.</li>\n</ol>\n",
    "markdown": "The number of windows in my house is\n1.  The number of doors is 6.\n",
    "example": 268,
    "start_line": 4930
  },
  {
    "end_line": 4963,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>foo</p>\n</li>\n<li>\n<p>bar</p>\n</li>\n<li>\n<p>baz</p>\n</li>\n</ul>\n",
    "markdown": "- foo\n\n- bar\n\n\n- baz\n",
    "example": 269,
    "start_line": 4944
  },
  {
    "end_line": 4987,
    "section": "Lists",
    "html": "<ul>\n<li>foo\n<ul>\n<li>bar\n<ul>\n<li>\n<p>baz</p>\n<p>bim</p>\n</li>\n</ul>\n</li>\n</ul>\n</li>\n</ul>\n",
    "markdown": "- foo\n  - bar\n    - baz\n\n\n      bim\n",
    "example": 270,
    "start_line": 4965
  },
  {
    "end_line": 5013,
    "section": "Lists",
    "html": "<ul>\n<li>foo</li>\n<li>bar</li>\n</ul>\n<!-- -->\n<ul>\n<li>baz</li>\n<li>bim</li>\n</ul>\n",
    "markdown": "- foo\n- bar\n\n<!-- -->\n\n- baz\n- bim\n",
    "example": 271,
    "start_line": 4995
  },
  {
    "end_line": 5039,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>foo</p>\n<p>notcode</p>\n</li>\n<li>\n<p>foo</p>\n</li>\n</ul>\n<!-- -->\n<pre><code>code\n</code></pre>\n",
    "markdown": "-   foo\n\n    notcode\n\n-   foo\n\n<!-- -->\n\n    code\n",
    "example": 272,
    "start_line": 5016
  },
  {
    "end_line": 5069,
    "section": "Lists",
    "html": "<ul>\n<li>a</li>\n<li>b</li>\n<li>c</li>\n<li>d</li>\n<li>e</li>\n<li>f</li>\n<li>g</li>\n<li>h</li>\n<li>i</li>\n</ul>\n",
    "markdown": "- a\n - b\n  - c\n   - d\n    - e\n   - f\n  - g\n - h\n- i\n",
    "example": 273,
    "start_line": 5047
  },
  {
    "end_line": 5090,
    "section": "Lists",
    "html": "<ol>\n<li>\n<p>a</p>\n</li>\n<li>\n<p>b</p>\n</li>\n<li>\n<p>c</p>\n</li>\n</ol>\n",
    "markdown": "1. a\n\n  2. b\n\n    3. c\n",
    "example": 274,
    "start_line": 5072
  },
  {
    "end_line": 5113,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>a</p>\n</li>\n<li>\n<p>b</p>\n</li>\n<li>\n<p>c</p>\n</li>\n</ul>\n",
    "markdown": "- a\n- b\n\n- c\n",
    "example": 275,
    "start_line": 5096
  },
  {
    "end_line": 5133,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>a</p>\n</li>\n<li></li>\n<li>\n<p>c</p>\n</li>\n</ul>\n",
    "markdown": "* a\n*\n\n* c\n",
    "example": 276,
    "start_line": 5118
  },
  {
    "end_line": 5159,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>a</p>\n</li>\n<li>\n<p>b</p>\n<p>c</p>\n</li>\n<li>\n<p>d</p>\n</li>\n</ul>\n",
    "markdown": "- a\n- b\n\n  c\n- d\n",
    "example": 277,
    "start_line": 5140
  },
  {
    "end_line": 5180,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>a</p>\n</li>\n<li>\n<p>b</p>\n</li>\n<li>\n<p>d</p>\n</li>\n</ul>\n",
    "markdown": "- a\n- b\n\n  [ref]: /url\n- d\n",
    "example": 278,
    "start_line": 5162
  },
  {
    "end_line": 5204,
    "section": "Lists",
    "html": "<ul>\n<li>a</li>\n<li>\n<pre><code>b\n\n\n</code></pre>\n</li>\n<li>c</li>\n</ul>\n",
    "markdown": "- a\n- ```\n  b\n\n\n  ```\n- c\n",
    "example": 279,
    "start_line": 5185
  },
  {
    "end_line": 5229,
    "section": "Lists",
    "html": "<ul>\n<li>a\n<ul>\n<li>\n<p>b</p>\n<p>c</p>\n</li>\n</ul>\n</li>\n<li>d</li>\n</ul>\n",
    "markdown": "- a\n  - b\n\n    c\n- d\n",
    "example": 280,
    "start_line": 5211
  },
  {
    "end_line": 5249,
    "section": "Lists",
    "html": "<ul>\n<li>a\n<blockquote>\n<p>b</p>\n</blockquote>\n</li>\n<li>c</li>\n</ul>\n",
    "markdown": "* a\n  > b\n  >\n* c\n",
    "example": 281,
    "start_line": 5235
  },
  {
    "end_line": 5273,
    "section": "Lists",
    "html": "<ul>\n<li>a\n<blockquote>\n<p>b</p>\n</blockquote>\n<pre><code>c\n</code></pre>\n</li>\n<li>d</li>\n</ul>\n",
    "markdown": "- a\n  > b\n  ```\n  c\n  ```\n- d\n",
    "example": 282,
    "start_line": 5255
  },
  {
    "end_line": 5284,
    "section": "Lists",
    "html": "<ul>\n<li>a</li>\n</ul>\n",
    "markdown": "- a\n",
    "example": 283,
    "start_line": 5278
  },
  {
    "end_line": 5298,
    "section": "Lists",
    "html": "<ul>\n<li>a\n<ul>\n<li>b</li>\n</ul>\n</li>\n</ul>\n",
    "markdown": "- a\n  - b\n",
    "example": 284,
    "start_line": 5287
  },
  {
    "end_line": 5318,
    "section": "Lists",
    "html": "<ol>\n<li>\n<pre><code>foo\n</code></pre>\n<p>bar</p>\n</li>\n</ol>\n",
    "markdown": "1. ```\n   foo\n   ```\n\n   bar\n",
    "example": 285,
    "start_line": 5304
  },
  {
    "end_line": 5338,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>foo</p>\n<ul>\n<li>bar</li>\n</ul>\n<p>baz</p>\n</li>\n</ul>\n",
    "markdown": "* foo\n  * bar\n\n  baz\n",
    "example": 286,
    "start_line": 5323
  },
  {
    "end_line": 5366,
    "section": "Lists",
    "html": "<ul>\n<li>\n<p>a</p>\n<ul>\n<li>b</li>\n<li>c</li>\n</ul>\n</li>\n<li>\n<p>d</p>\n<ul>\n<li>e</li>\n<li>f</li>\n</ul>\n</li>\n</ul>\n",
    "markdown": "- a\n  - b\n  - c\n\n- d\n  - e\n  - f\n",
    "example": 287,
    "start_line": 5341
  },
  {
    "end_line": 5379,
    "section": "Inlines",
    "html": "<p><code>hi</code>lo`</p>\n",
    "markdown": "`hi`lo`\n",
    "example": 288,
    "start_line": 5375
  },
  {
    "end_line": 5393,
    "section": "Backslash escapes",
    "html": "<p>!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?@[\\]^_`{|}~</p>\n",
    "markdown": "\\!\\\"\\#\\$\\%\\&\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^\\_\\`\\{\\|\\}\\~\n",
    "example": 289,
    "start_line": 5389
  },
  {
    "end_line": 5403,
    "section": "Backslash escapes",
    "html": "<p>\\\t\\A\\a\\ \\3\\φ\\«</p>\n",
    "markdown": "\\\t\\A\\a\\ \\3\\φ\\«\n",
    "example": 290,
    "start_line": 5399
  },
  {
    "end_line": 5427,
    "section": "Backslash escapes",
    "html": "<p>*not emphasized*\n&lt;br/&gt; not a tag\n[not a link](/foo)\n`not code`\n1. not a list\n* not a list\n# not a heading\n[foo]: /url &quot;not a reference&quot;</p>\n",
    "markdown": "\\*not emphasized*\n\\<br/> not a tag\n\\[not a link](/foo)\n\\`not code`\n1\\. not a list\n\\* not a list\n\\# not a heading\n\\[foo]: /url \"not a reference\"\n",
    "example": 291,
    "start_line": 5409
  },
  {
    "end_line": 5436,
    "section": "Backslash escapes",
    "html": "<p>\\<em>emphasis</em></p>\n",
    "markdown": "\\\\*emphasis*\n",
    "example": 292,
    "start_line": 5432
  },
  {
    "end_line": 5447,
    "section": "Backslash escapes",
    "html": "<p>foo<br />\nbar</p>\n",
    "markdown": "foo\\\nbar\n",
    "example": 293,
    "start_line": 5441
  },
  {
    "end_line": 5457,
    "section": "Backslash escapes",
    "html": "<p><code>\\[\\`</code></p>\n",
    "markdown": "`` \\[\\` ``\n",
    "example": 294,
    "start_line": 5453
  },
  {
    "end_line": 5465,
    "section": "Backslash escapes",
    "html": "<pre><code>\\[\\]\n</code></pre>\n",
    "markdown": "    \\[\\]\n",
    "example": 295,
    "start_line": 5460
  },
  {
    "end_line": 5475,
    "section": "Backslash escapes",
    "html": "<pre><code>\\[\\]\n</code></pre>\n",
    "markdown": "~~~\n\\[\\]\n~~~\n",
    "example": 296,
    "start_line": 5468
  },
  {
    "end_line": 5482,
    "section": "Backslash escapes",
    "html": "<p><a href=\"http://example.com?find=%5C*\">http://example.com?find=\\*</a></p>\n",
    "markdown": "<http://example.com?find=\\*>\n",
    "example": 297,
    "start_line": 5478
  },
  {
    "end_line": 5489,
    "section": "Backslash escapes",
    "html": "<a href=\"/bar\\/)\">\n",
    "markdown": "<a href=\"/bar\\/)\">\n",
    "example": 298,
    "start_line": 5485
  },
  {
    "end_line": 5499,
    "section": "Backslash escapes",
    "html": "<p><a href=\"/bar*\" title=\"ti*tle\">foo</a></p>\n",
    "markdown": "[foo](/bar\\* \"ti\\*tle\")\n",
    "example": 299,
    "start_line": 5495
  },
  {
    "end_line": 5508,
    "section": "Backslash escapes",
    "html": "<p><a href=\"/bar*\" title=\"ti*tle\">foo</a></p>\n",
    "markdown": "[foo]\n\n[foo]: /bar\\* \"ti\\*tle\"\n",
    "example": 300,
    "start_line": 5502
  },
  {
    "end_line": 5518,
    "section": "Backslash escapes",
    "html": "<pre><code class=\"language-foo+bar\">foo\n</code></pre>\n",
    "markdown": "``` foo\\+bar\nfoo\n```\n",
    "example": 301,
    "start_line": 5511
  },
  {
    "end_line": 5546,
    "section": "Entity and numeric character references",
    "html": "<p>  &amp; © Æ Ď\n¾ ℋ ⅆ\n∲ ≧̸</p>\n",
    "markdown": "&nbsp; &amp; &copy; &AElig; &Dcaron;\n&frac34; &HilbertSpace; &DifferentialD;\n&ClockwiseContourIntegral; &ngE;\n",
    "example": 302,
    "start_line": 5538
  },
  {
    "end_line": 5561,
    "section": "Entity and numeric character references",
    "html": "<p># Ӓ Ϡ � �</p>\n",
    "markdown": "&#35; &#1234; &#992; &#98765432; &#0;\n",
    "example": 303,
    "start_line": 5557
  },
  {
    "end_line": 5574,
    "section": "Entity and numeric character references",
    "html": "<p>&quot; ആ ಫ</p>\n",
    "markdown": "&#X22; &#XD06; &#xcab;\n",
    "example": 304,
    "start_line": 5570
  },
  {
    "end_line": 5585,
    "section": "Entity and numeric character references",
    "html": "<p>&amp;nbsp &amp;x; &amp;#; &amp;#x;\n&amp;ThisIsNotDefined; &amp;hi?;</p>\n",
    "markdown": "&nbsp &x; &#; &#x;\n&ThisIsNotDefined; &hi?;\n",
    "example": 305,
    "start_line": 5579
  },
  {
    "end_line": 5596,
    "section": "Entity and numeric character references",
    "html": "<p>&amp;copy</p>\n",
    "markdown": "&copy\n",
    "example": 306,
    "start_line": 5592
  },
  {
    "end_line": 5606,
    "section": "Entity and numeric character references",
    "html": "<p>&amp;MadeUpEntity;</p>\n",
    "markdown": "&MadeUpEntity;\n",
    "example": 307,
    "start_line": 5602
  },
  {
    "end_line": 5617,
    "section": "Entity and numeric character references",
    "html": "<a href=\"&ouml;&ouml;.html\">\n",
    "markdown": "<a href=\"&ouml;&ouml;.html\">\n",
    "example": 308,
    "start_line": 5613
  },
  {
    "end_line": 5624,
    "section": "Entity and numeric character references",
    "html": "<p><a href=\"/f%C3%B6%C3%B6\" title=\"föö\">foo</a></p>\n",
    "markdown": "[foo](/f&ouml;&ouml; \"f&ouml;&ouml;\")\n",
    "example": 309,
    "start_line": 5620
  },
  {
    "end_line": 5633,
    "section": "Entity and numeric character references",
    "html": "<p><a href=\"/f%C3%B6%C3%B6\" title=\"föö\">foo</a></p>\n",
    "markdown": "[foo]\n\n[foo]: /f&ouml;&ouml; \"f&ouml;&ouml;\"\n",
    "example": 310,
    "start_line": 5627
  },
  {
    "end_line": 5643,
    "section": "Entity and numeric character references",
    "html": "<pre><code class=\"language-föö\">foo\n</code></pre>\n",
    "markdown": "``` f&ouml;&ouml;\nfoo\n```\n",
    "example": 311,
    "start_line": 5636
  },
  {
    "end_line": 5653,
    "section": "Entity and numeric character references",
    "html": "<p><code>f&amp;ouml;&amp;ouml;</code></p>\n",
    "markdown": "`f&ouml;&ouml;`\n",
    "example": 312,
    "start_line": 5649
  },
  {
    "end_line": 5661,
    "section": "Entity and numeric character references",
    "html": "<pre><code>f&amp;ouml;f&amp;ouml;\n</code></pre>\n",
    "markdown": "    f&ouml;f&ouml;\n",
    "example": 313,
    "start_line": 5656
  },
  {
    "end_line": 5682,
    "section": "Code spans",
    "html": "<p><code>foo</code></p>\n",
    "markdown": "`foo`\n",
    "example": 314,
    "start_line": 5678
  },
  {
    "end_line": 5692,
    "section": "Code spans",
    "html": "<p><code>foo ` bar</code></p>\n",
    "markdown": "`` foo ` bar  ``\n",
    "example": 315,
    "start_line": 5688
  },
  {
    "end_line": 5702,
    "section": "Code spans",
    "html": "<p><code>``</code></p>\n",
    "markdown": "` `` `\n",
    "example": 316,
    "start_line": 5698
  },
  {
    "end_line": 5713,
    "section": "Code spans",
    "html": "<p><code>foo</code></p>\n",
    "markdown": "``\nfoo\n``\n",
    "example": 317,
    "start_line": 5707
  },
  {
    "end_line": 5724,
    "section": "Code spans",
    "html": "<p><code>foo bar baz</code></p>\n",
    "markdown": "`foo   bar\n  baz`\n",
    "example": 318,
    "start_line": 5719
  },
  {
    "end_line": 5734,
    "section": "Code spans",
    "html": "<p><code>a  b</code></p>\n",
    "markdown": "`a  b`\n",
    "example": 319,
    "start_line": 5730
  },
  {
    "end_line": 5754,
    "section": "Code spans",
    "html": "<p><code>foo `` bar</code></p>\n",
    "markdown": "`foo `` bar`\n",
    "example": 320,
    "start_line": 5750
  },
  {
    "end_line": 5764,
    "section": "Code spans",
    "html": "<p><code>foo\\</code>bar`</p>\n",
    "markdown": "`foo\\`bar`\n",
    "example": 321,
    "start_line": 5760
  },
  {
    "end_line": 5780,
    "section": "Code spans",
    "html": "<p>*foo<code>*</code></p>\n",
    "markdown": "*foo`*`\n",
    "example": 322,
    "start_line": 5776
  },
  {
    "end_line": 5789,
    "section": "Code spans",
    "html": "<p>[not a <code>link](/foo</code>)</p>\n",
    "markdown": "[not a `link](/foo`)\n",
    "example": 323,
    "start_line": 5785
  },
  {
    "end_line": 5799,
    "section": "Code spans",
    "html": "<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>\n",
    "markdown": "`<a href=\"`\">`\n",
    "example": 324,
    "start_line": 5795
  },
  {
    "end_line": 5808,
    "section": "Code spans",
    "html": "<p><a href=\"`\">`</p>\n",
    "markdown": "<a href=\"`\">`\n",
    "example": 325,
    "start_line": 5804
  },
  {
    "end_line": 5817,
    "section": "Code spans",
    "html": "<p><code>&lt;http://foo.bar.</code>baz&gt;`</p>\n",
    "markdown": "`<http://foo.bar.`baz>`\n",
    "example": 326,
    "start_line": 5813
  },
  {
    "end_line": 5826,
    "section": "Code spans",
    "html": "<p><a href=\"http://foo.bar.%60baz\">http://foo.bar.`baz</a>`</p>\n",
    "markdown": "<http://foo.bar.`baz>`\n",
    "example": 327,
    "start_line": 5822
  },
  {
    "end_line": 5836,
    "section": "Code spans",
    "html": "<p>```foo``</p>\n",
    "markdown": "```foo``\n",
    "example": 328,
    "start_line": 5832
  },
  {
    "end_line": 5843,
    "section": "Code spans",
    "html": "<p>`foo</p>\n",
    "markdown": "`foo\n",
    "example": 329,
    "start_line": 5839
  },
  {
    "end_line": 5852,
    "section": "Code spans",
    "html": "<p>`foo<code>bar</code></p>\n",
    "markdown": "`foo``bar``\n",
    "example": 330,
    "start_line": 5848
  },
  {
    "end_line": 6065,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo bar</em></p>\n",
    "markdown": "*foo bar*\n",
    "example": 331,
    "start_line": 6061
  },
  {
    "end_line": 6075,
    "section": "Emphasis and strong emphasis",
    "html": "<p>a * foo bar*</p>\n",
    "markdown": "a * foo bar*\n",
    "example": 332,
    "start_line": 6071
  },
  {
    "end_line": 6086,
    "section": "Emphasis and strong emphasis",
    "html": "<p>a*&quot;foo&quot;*</p>\n",
    "markdown": "a*\"foo\"*\n",
    "example": 333,
    "start_line": 6082
  },
  {
    "end_line": 6095,
    "section": "Emphasis and strong emphasis",
    "html": "<p>* a *</p>\n",
    "markdown": "* a *\n",
    "example": 334,
    "start_line": 6091
  },
  {
    "end_line": 6104,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo<em>bar</em></p>\n",
    "markdown": "foo*bar*\n",
    "example": 335,
    "start_line": 6100
  },
  {
    "end_line": 6111,
    "section": "Emphasis and strong emphasis",
    "html": "<p>5<em>6</em>78</p>\n",
    "markdown": "5*6*78\n",
    "example": 336,
    "start_line": 6107
  },
  {
    "end_line": 6120,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo bar</em></p>\n",
    "markdown": "_foo bar_\n",
    "example": 337,
    "start_line": 6116
  },
  {
    "end_line": 6130,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_ foo bar_</p>\n",
    "markdown": "_ foo bar_\n",
    "example": 338,
    "start_line": 6126
  },
  {
    "end_line": 6140,
    "section": "Emphasis and strong emphasis",
    "html": "<p>a_&quot;foo&quot;_</p>\n",
    "markdown": "a_\"foo\"_\n",
    "example": 339,
    "start_line": 6136
  },
  {
    "end_line": 6149,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo_bar_</p>\n",
    "markdown": "foo_bar_\n",
    "example": 340,
    "start_line": 6145
  },
  {
    "end_line": 6156,
    "section": "Emphasis and strong emphasis",
    "html": "<p>5_6_78</p>\n",
    "markdown": "5_6_78\n",
    "example": 341,
    "start_line": 6152
  },
  {
    "end_line": 6163,
    "section": "Emphasis and strong emphasis",
    "html": "<p>пристаням_стремятся_</p>\n",
    "markdown": "пристаням_стремятся_\n",
    "example": 342,
    "start_line": 6159
  },
  {
    "end_line": 6173,
    "section": "Emphasis and strong emphasis",
    "html": "<p>aa_&quot;bb&quot;_cc</p>\n",
    "markdown": "aa_\"bb\"_cc\n",
    "example": 343,
    "start_line": 6169
  },
  {
    "end_line": 6184,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo-<em>(bar)</em></p>\n",
    "markdown": "foo-_(bar)_\n",
    "example": 344,
    "start_line": 6180
  },
  {
    "end_line": 6196,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_foo*</p>\n",
    "markdown": "_foo*\n",
    "example": 345,
    "start_line": 6192
  },
  {
    "end_line": 6206,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*foo bar *</p>\n",
    "markdown": "*foo bar *\n",
    "example": 346,
    "start_line": 6202
  },
  {
    "end_line": 6217,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*foo bar\n*</p>\n",
    "markdown": "*foo bar\n*\n",
    "example": 347,
    "start_line": 6211
  },
  {
    "end_line": 6228,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*(*foo)</p>\n",
    "markdown": "*(*foo)\n",
    "example": 348,
    "start_line": 6224
  },
  {
    "end_line": 6238,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>(<em>foo</em>)</em></p>\n",
    "markdown": "*(*foo*)*\n",
    "example": 349,
    "start_line": 6234
  },
  {
    "end_line": 6247,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo</em>bar</p>\n",
    "markdown": "*foo*bar\n",
    "example": 350,
    "start_line": 6243
  },
  {
    "end_line": 6260,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_foo bar _</p>\n",
    "markdown": "_foo bar _\n",
    "example": 351,
    "start_line": 6256
  },
  {
    "end_line": 6270,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_(_foo)</p>\n",
    "markdown": "_(_foo)\n",
    "example": 352,
    "start_line": 6266
  },
  {
    "end_line": 6279,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>(<em>foo</em>)</em></p>\n",
    "markdown": "_(_foo_)_\n",
    "example": 353,
    "start_line": 6275
  },
  {
    "end_line": 6288,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_foo_bar</p>\n",
    "markdown": "_foo_bar\n",
    "example": 354,
    "start_line": 6284
  },
  {
    "end_line": 6295,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_пристаням_стремятся</p>\n",
    "markdown": "_пристаням_стремятся\n",
    "example": 355,
    "start_line": 6291
  },
  {
    "end_line": 6302,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo_bar_baz</em></p>\n",
    "markdown": "_foo_bar_baz_\n",
    "example": 356,
    "start_line": 6298
  },
  {
    "end_line": 6313,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>(bar)</em>.</p>\n",
    "markdown": "_(bar)_.\n",
    "example": 357,
    "start_line": 6309
  },
  {
    "end_line": 6322,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo bar</strong></p>\n",
    "markdown": "**foo bar**\n",
    "example": 358,
    "start_line": 6318
  },
  {
    "end_line": 6332,
    "section": "Emphasis and strong emphasis",
    "html": "<p>** foo bar**</p>\n",
    "markdown": "** foo bar**\n",
    "example": 359,
    "start_line": 6328
  },
  {
    "end_line": 6343,
    "section": "Emphasis and strong emphasis",
    "html": "<p>a**&quot;foo&quot;**</p>\n",
    "markdown": "a**\"foo\"**\n",
    "example": 360,
    "start_line": 6339
  },
  {
    "end_line": 6352,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo<strong>bar</strong></p>\n",
    "markdown": "foo**bar**\n",
    "example": 361,
    "start_line": 6348
  },
  {
    "end_line": 6361,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo bar</strong></p>\n",
    "markdown": "__foo bar__\n",
    "example": 362,
    "start_line": 6357
  },
  {
    "end_line": 6371,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__ foo bar__</p>\n",
    "markdown": "__ foo bar__\n",
    "example": 363,
    "start_line": 6367
  },
  {
    "end_line": 6381,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__\nfoo bar__</p>\n",
    "markdown": "__\nfoo bar__\n",
    "example": 364,
    "start_line": 6375
  },
  {
    "end_line": 6391,
    "section": "Emphasis and strong emphasis",
    "html": "<p>a__&quot;foo&quot;__</p>\n",
    "markdown": "a__\"foo\"__\n",
    "example": 365,
    "start_line": 6387
  },
  {
    "end_line": 6400,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo__bar__</p>\n",
    "markdown": "foo__bar__\n",
    "example": 366,
    "start_line": 6396
  },
  {
    "end_line": 6407,
    "section": "Emphasis and strong emphasis",
    "html": "<p>5__6__78</p>\n",
    "markdown": "5__6__78\n",
    "example": 367,
    "start_line": 6403
  },
  {
    "end_line": 6414,
    "section": "Emphasis and strong emphasis",
    "html": "<p>пристаням__стремятся__</p>\n",
    "markdown": "пристаням__стремятся__\n",
    "example": 368,
    "start_line": 6410
  },
  {
    "end_line": 6421,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo, <strong>bar</strong>, baz</strong></p>\n",
    "markdown": "__foo, __bar__, baz__\n",
    "example": 369,
    "start_line": 6417
  },
  {
    "end_line": 6432,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo-<strong>(bar)</strong></p>\n",
    "markdown": "foo-__(bar)__\n",
    "example": 370,
    "start_line": 6428
  },
  {
    "end_line": 6445,
    "section": "Emphasis and strong emphasis",
    "html": "<p>**foo bar **</p>\n",
    "markdown": "**foo bar **\n",
    "example": 371,
    "start_line": 6441
  },
  {
    "end_line": 6458,
    "section": "Emphasis and strong emphasis",
    "html": "<p>**(**foo)</p>\n",
    "markdown": "**(**foo)\n",
    "example": 372,
    "start_line": 6454
  },
  {
    "end_line": 6468,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>(<strong>foo</strong>)</em></p>\n",
    "markdown": "*(**foo**)*\n",
    "example": 373,
    "start_line": 6464
  },
  {
    "end_line": 6477,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn.\n<em>Asclepias physocarpa</em>)</strong></p>\n",
    "markdown": "**Gomphocarpus (*Gomphocarpus physocarpus*, syn.\n*Asclepias physocarpa*)**\n",
    "example": 374,
    "start_line": 6471
  },
  {
    "end_line": 6484,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo &quot;<em>bar</em>&quot; foo</strong></p>\n",
    "markdown": "**foo \"*bar*\" foo**\n",
    "example": 375,
    "start_line": 6480
  },
  {
    "end_line": 6493,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo</strong>bar</p>\n",
    "markdown": "**foo**bar\n",
    "example": 376,
    "start_line": 6489
  },
  {
    "end_line": 6505,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__foo bar __</p>\n",
    "markdown": "__foo bar __\n",
    "example": 377,
    "start_line": 6501
  },
  {
    "end_line": 6515,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__(__foo)</p>\n",
    "markdown": "__(__foo)\n",
    "example": 378,
    "start_line": 6511
  },
  {
    "end_line": 6525,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>(<strong>foo</strong>)</em></p>\n",
    "markdown": "_(__foo__)_\n",
    "example": 379,
    "start_line": 6521
  },
  {
    "end_line": 6534,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__foo__bar</p>\n",
    "markdown": "__foo__bar\n",
    "example": 380,
    "start_line": 6530
  },
  {
    "end_line": 6541,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__пристаням__стремятся</p>\n",
    "markdown": "__пристаням__стремятся\n",
    "example": 381,
    "start_line": 6537
  },
  {
    "end_line": 6548,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo__bar__baz</strong></p>\n",
    "markdown": "__foo__bar__baz__\n",
    "example": 382,
    "start_line": 6544
  },
  {
    "end_line": 6559,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>(bar)</strong>.</p>\n",
    "markdown": "__(bar)__.\n",
    "example": 383,
    "start_line": 6555
  },
  {
    "end_line": 6571,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <a href=\"/url\">bar</a></em></p>\n",
    "markdown": "*foo [bar](/url)*\n",
    "example": 384,
    "start_line": 6567
  },
  {
    "end_line": 6580,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo\nbar</em></p>\n",
    "markdown": "*foo\nbar*\n",
    "example": 385,
    "start_line": 6574
  },
  {
    "end_line": 6590,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <strong>bar</strong> baz</em></p>\n",
    "markdown": "_foo __bar__ baz_\n",
    "example": 386,
    "start_line": 6586
  },
  {
    "end_line": 6597,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <em>bar</em> baz</em></p>\n",
    "markdown": "_foo _bar_ baz_\n",
    "example": 387,
    "start_line": 6593
  },
  {
    "end_line": 6604,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em><em>foo</em> bar</em></p>\n",
    "markdown": "__foo_ bar_\n",
    "example": 388,
    "start_line": 6600
  },
  {
    "end_line": 6611,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <em>bar</em></em></p>\n",
    "markdown": "*foo *bar**\n",
    "example": 389,
    "start_line": 6607
  },
  {
    "end_line": 6618,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <strong>bar</strong> baz</em></p>\n",
    "markdown": "*foo **bar** baz*\n",
    "example": 390,
    "start_line": 6614
  },
  {
    "end_line": 6624,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo<strong>bar</strong>baz</em></p>\n",
    "markdown": "*foo**bar**baz*\n",
    "example": 391,
    "start_line": 6620
  },
  {
    "end_line": 6649,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em><strong>foo</strong> bar</em></p>\n",
    "markdown": "***foo** bar*\n",
    "example": 392,
    "start_line": 6645
  },
  {
    "end_line": 6656,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <strong>bar</strong></em></p>\n",
    "markdown": "*foo **bar***\n",
    "example": 393,
    "start_line": 6652
  },
  {
    "end_line": 6663,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo<strong>bar</strong></em></p>\n",
    "markdown": "*foo**bar***\n",
    "example": 394,
    "start_line": 6659
  },
  {
    "end_line": 6672,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <strong>bar <em>baz</em> bim</strong> bop</em></p>\n",
    "markdown": "*foo **bar *baz* bim** bop*\n",
    "example": 395,
    "start_line": 6668
  },
  {
    "end_line": 6679,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <a href=\"/url\"><em>bar</em></a></em></p>\n",
    "markdown": "*foo [*bar*](/url)*\n",
    "example": 396,
    "start_line": 6675
  },
  {
    "end_line": 6688,
    "section": "Emphasis and strong emphasis",
    "html": "<p>** is not an empty emphasis</p>\n",
    "markdown": "** is not an empty emphasis\n",
    "example": 397,
    "start_line": 6684
  },
  {
    "end_line": 6695,
    "section": "Emphasis and strong emphasis",
    "html": "<p>**** is not an empty strong emphasis</p>\n",
    "markdown": "**** is not an empty strong emphasis\n",
    "example": 398,
    "start_line": 6691
  },
  {
    "end_line": 6708,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <a href=\"/url\">bar</a></strong></p>\n",
    "markdown": "**foo [bar](/url)**\n",
    "example": 399,
    "start_line": 6704
  },
  {
    "end_line": 6717,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo\nbar</strong></p>\n",
    "markdown": "**foo\nbar**\n",
    "example": 400,
    "start_line": 6711
  },
  {
    "end_line": 6727,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <em>bar</em> baz</strong></p>\n",
    "markdown": "__foo _bar_ baz__\n",
    "example": 401,
    "start_line": 6723
  },
  {
    "end_line": 6734,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <strong>bar</strong> baz</strong></p>\n",
    "markdown": "__foo __bar__ baz__\n",
    "example": 402,
    "start_line": 6730
  },
  {
    "end_line": 6741,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong><strong>foo</strong> bar</strong></p>\n",
    "markdown": "____foo__ bar__\n",
    "example": 403,
    "start_line": 6737
  },
  {
    "end_line": 6748,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <strong>bar</strong></strong></p>\n",
    "markdown": "**foo **bar****\n",
    "example": 404,
    "start_line": 6744
  },
  {
    "end_line": 6755,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <em>bar</em> baz</strong></p>\n",
    "markdown": "**foo *bar* baz**\n",
    "example": 405,
    "start_line": 6751
  },
  {
    "end_line": 6762,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo<em>bar</em>baz</strong></p>\n",
    "markdown": "**foo*bar*baz**\n",
    "example": 406,
    "start_line": 6758
  },
  {
    "end_line": 6769,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong><em>foo</em> bar</strong></p>\n",
    "markdown": "***foo* bar**\n",
    "example": 407,
    "start_line": 6765
  },
  {
    "end_line": 6776,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <em>bar</em></strong></p>\n",
    "markdown": "**foo *bar***\n",
    "example": 408,
    "start_line": 6772
  },
  {
    "end_line": 6787,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <em>bar <strong>baz</strong>\nbim</em> bop</strong></p>\n",
    "markdown": "**foo *bar **baz**\nbim* bop**\n",
    "example": 409,
    "start_line": 6781
  },
  {
    "end_line": 6794,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo <a href=\"/url\"><em>bar</em></a></strong></p>\n",
    "markdown": "**foo [*bar*](/url)**\n",
    "example": 410,
    "start_line": 6790
  },
  {
    "end_line": 6803,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__ is not an empty emphasis</p>\n",
    "markdown": "__ is not an empty emphasis\n",
    "example": 411,
    "start_line": 6799
  },
  {
    "end_line": 6810,
    "section": "Emphasis and strong emphasis",
    "html": "<p>____ is not an empty strong emphasis</p>\n",
    "markdown": "____ is not an empty strong emphasis\n",
    "example": 412,
    "start_line": 6806
  },
  {
    "end_line": 6820,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo ***</p>\n",
    "markdown": "foo ***\n",
    "example": 413,
    "start_line": 6816
  },
  {
    "end_line": 6827,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <em>*</em></p>\n",
    "markdown": "foo *\\**\n",
    "example": 414,
    "start_line": 6823
  },
  {
    "end_line": 6834,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <em>_</em></p>\n",
    "markdown": "foo *_*\n",
    "example": 415,
    "start_line": 6830
  },
  {
    "end_line": 6841,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo *****</p>\n",
    "markdown": "foo *****\n",
    "example": 416,
    "start_line": 6837
  },
  {
    "end_line": 6848,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <strong>*</strong></p>\n",
    "markdown": "foo **\\***\n",
    "example": 417,
    "start_line": 6844
  },
  {
    "end_line": 6855,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <strong>_</strong></p>\n",
    "markdown": "foo **_**\n",
    "example": 418,
    "start_line": 6851
  },
  {
    "end_line": 6866,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*<em>foo</em></p>\n",
    "markdown": "**foo*\n",
    "example": 419,
    "start_line": 6862
  },
  {
    "end_line": 6873,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo</em>*</p>\n",
    "markdown": "*foo**\n",
    "example": 420,
    "start_line": 6869
  },
  {
    "end_line": 6880,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*<strong>foo</strong></p>\n",
    "markdown": "***foo**\n",
    "example": 421,
    "start_line": 6876
  },
  {
    "end_line": 6887,
    "section": "Emphasis and strong emphasis",
    "html": "<p>***<em>foo</em></p>\n",
    "markdown": "****foo*\n",
    "example": 422,
    "start_line": 6883
  },
  {
    "end_line": 6894,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo</strong>*</p>\n",
    "markdown": "**foo***\n",
    "example": 423,
    "start_line": 6890
  },
  {
    "end_line": 6901,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo</em>***</p>\n",
    "markdown": "*foo****\n",
    "example": 424,
    "start_line": 6897
  },
  {
    "end_line": 6911,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo ___</p>\n",
    "markdown": "foo ___\n",
    "example": 425,
    "start_line": 6907
  },
  {
    "end_line": 6918,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <em>_</em></p>\n",
    "markdown": "foo _\\__\n",
    "example": 426,
    "start_line": 6914
  },
  {
    "end_line": 6925,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <em>*</em></p>\n",
    "markdown": "foo _*_\n",
    "example": 427,
    "start_line": 6921
  },
  {
    "end_line": 6932,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo _____</p>\n",
    "markdown": "foo _____\n",
    "example": 428,
    "start_line": 6928
  },
  {
    "end_line": 6939,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <strong>_</strong></p>\n",
    "markdown": "foo __\\___\n",
    "example": 429,
    "start_line": 6935
  },
  {
    "end_line": 6946,
    "section": "Emphasis and strong emphasis",
    "html": "<p>foo <strong>*</strong></p>\n",
    "markdown": "foo __*__\n",
    "example": 430,
    "start_line": 6942
  },
  {
    "end_line": 6953,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_<em>foo</em></p>\n",
    "markdown": "__foo_\n",
    "example": 431,
    "start_line": 6949
  },
  {
    "end_line": 6964,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo</em>_</p>\n",
    "markdown": "_foo__\n",
    "example": 432,
    "start_line": 6960
  },
  {
    "end_line": 6971,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_<strong>foo</strong></p>\n",
    "markdown": "___foo__\n",
    "example": 433,
    "start_line": 6967
  },
  {
    "end_line": 6978,
    "section": "Emphasis and strong emphasis",
    "html": "<p>___<em>foo</em></p>\n",
    "markdown": "____foo_\n",
    "example": 434,
    "start_line": 6974
  },
  {
    "end_line": 6985,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo</strong>_</p>\n",
    "markdown": "__foo___\n",
    "example": 435,
    "start_line": 6981
  },
  {
    "end_line": 6992,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo</em>___</p>\n",
    "markdown": "_foo____\n",
    "example": 436,
    "start_line": 6988
  },
  {
    "end_line": 7002,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo</strong></p>\n",
    "markdown": "**foo**\n",
    "example": 437,
    "start_line": 6998
  },
  {
    "end_line": 7009,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em><em>foo</em></em></p>\n",
    "markdown": "*_foo_*\n",
    "example": 438,
    "start_line": 7005
  },
  {
    "end_line": 7016,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong>foo</strong></p>\n",
    "markdown": "__foo__\n",
    "example": 439,
    "start_line": 7012
  },
  {
    "end_line": 7023,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em><em>foo</em></em></p>\n",
    "markdown": "_*foo*_\n",
    "example": 440,
    "start_line": 7019
  },
  {
    "end_line": 7033,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong><strong>foo</strong></strong></p>\n",
    "markdown": "****foo****\n",
    "example": 441,
    "start_line": 7029
  },
  {
    "end_line": 7040,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong><strong>foo</strong></strong></p>\n",
    "markdown": "____foo____\n",
    "example": 442,
    "start_line": 7036
  },
  {
    "end_line": 7051,
    "section": "Emphasis and strong emphasis",
    "html": "<p><strong><strong><strong>foo</strong></strong></strong></p>\n",
    "markdown": "******foo******\n",
    "example": 443,
    "start_line": 7047
  },
  {
    "end_line": 7060,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em><strong>foo</strong></em></p>\n",
    "markdown": "***foo***\n",
    "example": 444,
    "start_line": 7056
  },
  {
    "end_line": 7067,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em><strong><strong>foo</strong></strong></em></p>\n",
    "markdown": "_____foo_____\n",
    "example": 445,
    "start_line": 7063
  },
  {
    "end_line": 7076,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo _bar</em> baz_</p>\n",
    "markdown": "*foo _bar* baz_\n",
    "example": 446,
    "start_line": 7072
  },
  {
    "end_line": 7083,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>foo <strong>bar *baz bim</strong> bam</em></p>\n",
    "markdown": "*foo __bar *baz bim__ bam*\n",
    "example": 447,
    "start_line": 7079
  },
  {
    "end_line": 7092,
    "section": "Emphasis and strong emphasis",
    "html": "<p>**foo <strong>bar baz</strong></p>\n",
    "markdown": "**foo **bar baz**\n",
    "example": 448,
    "start_line": 7088
  },
  {
    "end_line": 7099,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*foo <em>bar baz</em></p>\n",
    "markdown": "*foo *bar baz*\n",
    "example": 449,
    "start_line": 7095
  },
  {
    "end_line": 7108,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*<a href=\"/url\">bar*</a></p>\n",
    "markdown": "*[bar*](/url)\n",
    "example": 450,
    "start_line": 7104
  },
  {
    "end_line": 7115,
    "section": "Emphasis and strong emphasis",
    "html": "<p>_foo <a href=\"/url\">bar_</a></p>\n",
    "markdown": "_foo [bar_](/url)\n",
    "example": 451,
    "start_line": 7111
  },
  {
    "end_line": 7122,
    "section": "Emphasis and strong emphasis",
    "html": "<p>*<img src=\"foo\" title=\"*\"/></p>\n",
    "markdown": "*<img src=\"foo\" title=\"*\"/>\n",
    "example": 452,
    "start_line": 7118
  },
  {
    "end_line": 7129,
    "section": "Emphasis and strong emphasis",
    "html": "<p>**<a href=\"**\"></p>\n",
    "markdown": "**<a href=\"**\">\n",
    "example": 453,
    "start_line": 7125
  },
  {
    "end_line": 7136,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__<a href=\"__\"></p>\n",
    "markdown": "__<a href=\"__\">\n",
    "example": 454,
    "start_line": 7132
  },
  {
    "end_line": 7143,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>a <code>*</code></em></p>\n",
    "markdown": "*a `*`*\n",
    "example": 455,
    "start_line": 7139
  },
  {
    "end_line": 7150,
    "section": "Emphasis and strong emphasis",
    "html": "<p><em>a <code>_</code></em></p>\n",
    "markdown": "_a `_`_\n",
    "example": 456,
    "start_line": 7146
  },
  {
    "end_line": 7157,
    "section": "Emphasis and strong emphasis",
    "html": "<p>**a<a href=\"http://foo.bar/?q=**\">http://foo.bar/?q=**</a></p>\n",
    "markdown": "**a<http://foo.bar/?q=**>\n",
    "example": 457,
    "start_line": 7153
  },
  {
    "end_line": 7164,
    "section": "Emphasis and strong emphasis",
    "html": "<p>__a<a href=\"http://foo.bar/?q=__\">http://foo.bar/?q=__</a></p>\n",
    "markdown": "__a<http://foo.bar/?q=__>\n",
    "example": 458,
    "start_line": 7160
  },
  {
    "end_line": 7245,
    "section": "Links",
    "html": "<p><a href=\"/uri\" title=\"title\">link</a></p>\n",
    "markdown": "[link](/uri \"title\")\n",
    "example": 459,
    "start_line": 7241
  },
  {
    "end_line": 7254,
    "section": "Links",
    "html": "<p><a href=\"/uri\">link</a></p>\n",
    "markdown": "[link](/uri)\n",
    "example": 460,
    "start_line": 7250
  },
  {
    "end_line": 7263,
    "section": "Links",
    "html": "<p><a href=\"\">link</a></p>\n",
    "markdown": "[link]()\n",
    "example": 461,
    "start_line": 7259
  },
  {
    "end_line": 7270,
    "section": "Links",
    "html": "<p><a href=\"\">link</a></p>\n",
    "markdown": "[link](<>)\n",
    "example": 462,
    "start_line": 7266
  },
  {
    "end_line": 7280,
    "section": "Links",
    "html": "<p>[link](/my uri)</p>\n",
    "markdown": "[link](/my uri)\n",
    "example": 463,
    "start_line": 7276
  },
  {
    "end_line": 7287,
    "section": "Links",
    "html": "<p>[link](&lt;/my uri&gt;)</p>\n",
    "markdown": "[link](</my uri>)\n",
    "example": 464,
    "start_line": 7283
  },
  {
    "end_line": 7296,
    "section": "Links",
    "html": "<p>[link](foo\nbar)</p>\n",
    "markdown": "[link](foo\nbar)\n",
    "example": 465,
    "start_line": 7290
  },
  {
    "end_line": 7305,
    "section": "Links",
    "html": "<p>[link](<foo\nbar>)</p>\n",
    "markdown": "[link](<foo\nbar>)\n",
    "example": 466,
    "start_line": 7299
  },
  {
    "end_line": 7313,
    "section": "Links",
    "html": "<p><a href=\"(foo)\">link</a></p>\n",
    "markdown": "[link](\\(foo\\))\n",
    "example": 467,
    "start_line": 7309
  },
  {
    "end_line": 7322,
    "section": "Links",
    "html": "<p><a href=\"foo(and(bar))\">link</a></p>\n",
    "markdown": "[link](foo(and(bar)))\n",
    "example": 468,
    "start_line": 7318
  },
  {
    "end_line": 7331,
    "section": "Links",
    "html": "<p><a href=\"foo(and(bar)\">link</a></p>\n",
    "markdown": "[link](foo\\(and\\(bar\\))\n",
    "example": 469,
    "start_line": 7327
  },
  {
    "end_line": 7338,
    "section": "Links",
    "html": "<p><a href=\"foo(and(bar)\">link</a></p>\n",
    "markdown": "[link](<foo(and(bar)>)\n",
    "example": 470,
    "start_line": 7334
  },
  {
    "end_line": 7348,
    "section": "Links",
    "html": "<p><a href=\"foo):\">link</a></p>\n",
    "markdown": "[link](foo\\)\\:)\n",
    "example": 471,
    "start_line": 7344
  },
  {
    "end_line": 7363,
    "section": "Links",
    "html": "<p><a href=\"#fragment\">link</a></p>\n<p><a href=\"http://example.com#fragment\">link</a></p>\n<p><a href=\"http://example.com?foo=3#frag\">link</a></p>\n",
    "markdown": "[link](#fragment)\n\n[link](http://example.com#fragment)\n\n[link](http://example.com?foo=3#frag)\n",
    "example": 472,
    "start_line": 7353
  },
  {
    "end_line": 7373,
    "section": "Links",
    "html": "<p><a href=\"foo%5Cbar\">link</a></p>\n",
    "markdown": "[link](foo\\bar)\n",
    "example": 473,
    "start_line": 7369
  },
  {
    "end_line": 7389,
    "section": "Links",
    "html": "<p><a href=\"foo%20b%C3%A4\">link</a></p>\n",
    "markdown": "[link](foo%20b&auml;)\n",
    "example": 474,
    "start_line": 7385
  },
  {
    "end_line": 7400,
    "section": "Links",
    "html": "<p><a href=\"%22title%22\">link</a></p>\n",
    "markdown": "[link](\"title\")\n",
    "example": 475,
    "start_line": 7396
  },
  {
    "end_line": 7413,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">link</a>\n<a href=\"/url\" title=\"title\">link</a>\n<a href=\"/url\" title=\"title\">link</a></p>\n",
    "markdown": "[link](/url \"title\")\n[link](/url 'title')\n[link](/url (title))\n",
    "example": 476,
    "start_line": 7405
  },
  {
    "end_line": 7423,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title &quot;&quot;\">link</a></p>\n",
    "markdown": "[link](/url \"title \\\"&quot;\")\n",
    "example": 477,
    "start_line": 7419
  },
  {
    "end_line": 7433,
    "section": "Links",
    "html": "<p><a href=\"/url%C2%A0%22title%22\">link</a></p>\n",
    "markdown": "[link](/url \"title\")\n",
    "example": 478,
    "start_line": 7429
  },
  {
    "end_line": 7442,
    "section": "Links",
    "html": "<p>[link](/url &quot;title &quot;and&quot; title&quot;)</p>\n",
    "markdown": "[link](/url \"title \"and\" title\")\n",
    "example": 479,
    "start_line": 7438
  },
  {
    "end_line": 7451,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title &quot;and&quot; title\">link</a></p>\n",
    "markdown": "[link](/url 'title \"and\" title')\n",
    "example": 480,
    "start_line": 7447
  },
  {
    "end_line": 7476,
    "section": "Links",
    "html": "<p><a href=\"/uri\" title=\"title\">link</a></p>\n",
    "markdown": "[link](   /uri\n  \"title\"  )\n",
    "example": 481,
    "start_line": 7471
  },
  {
    "end_line": 7486,
    "section": "Links",
    "html": "<p>[link] (/uri)</p>\n",
    "markdown": "[link] (/uri)\n",
    "example": 482,
    "start_line": 7482
  },
  {
    "end_line": 7496,
    "section": "Links",
    "html": "<p><a href=\"/uri\">link [foo [bar]]</a></p>\n",
    "markdown": "[link [foo [bar]]](/uri)\n",
    "example": 483,
    "start_line": 7492
  },
  {
    "end_line": 7503,
    "section": "Links",
    "html": "<p>[link] bar](/uri)</p>\n",
    "markdown": "[link] bar](/uri)\n",
    "example": 484,
    "start_line": 7499
  },
  {
    "end_line": 7510,
    "section": "Links",
    "html": "<p>[link <a href=\"/uri\">bar</a></p>\n",
    "markdown": "[link [bar](/uri)\n",
    "example": 485,
    "start_line": 7506
  },
  {
    "end_line": 7517,
    "section": "Links",
    "html": "<p><a href=\"/uri\">link [bar</a></p>\n",
    "markdown": "[link \\[bar](/uri)\n",
    "example": 486,
    "start_line": 7513
  },
  {
    "end_line": 7526,
    "section": "Links",
    "html": "<p><a href=\"/uri\">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>\n",
    "markdown": "[link *foo **bar** `#`*](/uri)\n",
    "example": 487,
    "start_line": 7522
  },
  {
    "end_line": 7533,
    "section": "Links",
    "html": "<p><a href=\"/uri\"><img src=\"moon.jpg\" alt=\"moon\" /></a></p>\n",
    "markdown": "[![moon](moon.jpg)](/uri)\n",
    "example": 488,
    "start_line": 7529
  },
  {
    "end_line": 7542,
    "section": "Links",
    "html": "<p>[foo <a href=\"/uri\">bar</a>](/uri)</p>\n",
    "markdown": "[foo [bar](/uri)](/uri)\n",
    "example": 489,
    "start_line": 7538
  },
  {
    "end_line": 7549,
    "section": "Links",
    "html": "<p>[foo <em>[bar <a href=\"/uri\">baz</a>](/uri)</em>](/uri)</p>\n",
    "markdown": "[foo *[bar [baz](/uri)](/uri)*](/uri)\n",
    "example": 490,
    "start_line": 7545
  },
  {
    "end_line": 7556,
    "section": "Links",
    "html": "<p><img src=\"uri3\" alt=\"[foo](uri2)\" /></p>\n",
    "markdown": "![[[foo](uri1)](uri2)](uri3)\n",
    "example": 491,
    "start_line": 7552
  },
  {
    "end_line": 7566,
    "section": "Links",
    "html": "<p>*<a href=\"/uri\">foo*</a></p>\n",
    "markdown": "*[foo*](/uri)\n",
    "example": 492,
    "start_line": 7562
  },
  {
    "end_line": 7573,
    "section": "Links",
    "html": "<p><a href=\"baz*\">foo *bar</a></p>\n",
    "markdown": "[foo *bar](baz*)\n",
    "example": 493,
    "start_line": 7569
  },
  {
    "end_line": 7583,
    "section": "Links",
    "html": "<p><em>foo [bar</em> baz]</p>\n",
    "markdown": "*foo [bar* baz]\n",
    "example": 494,
    "start_line": 7579
  },
  {
    "end_line": 7593,
    "section": "Links",
    "html": "<p>[foo <bar attr=\"](baz)\"></p>\n",
    "markdown": "[foo <bar attr=\"](baz)\">\n",
    "example": 495,
    "start_line": 7589
  },
  {
    "end_line": 7600,
    "section": "Links",
    "html": "<p>[foo<code>](/uri)</code></p>\n",
    "markdown": "[foo`](/uri)`\n",
    "example": 496,
    "start_line": 7596
  },
  {
    "end_line": 7607,
    "section": "Links",
    "html": "<p>[foo<a href=\"http://example.com/?search=%5D(uri)\">http://example.com/?search=](uri)</a></p>\n",
    "markdown": "[foo<http://example.com/?search=](uri)>\n",
    "example": 497,
    "start_line": 7603
  },
  {
    "end_line": 7647,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">foo</a></p>\n",
    "markdown": "[foo][bar]\n\n[bar]: /url \"title\"\n",
    "example": 498,
    "start_line": 7641
  },
  {
    "end_line": 7662,
    "section": "Links",
    "html": "<p><a href=\"/uri\">link [foo [bar]]</a></p>\n",
    "markdown": "[link [foo [bar]]][ref]\n\n[ref]: /uri\n",
    "example": 499,
    "start_line": 7656
  },
  {
    "end_line": 7671,
    "section": "Links",
    "html": "<p><a href=\"/uri\">link [bar</a></p>\n",
    "markdown": "[link \\[bar][ref]\n\n[ref]: /uri\n",
    "example": 500,
    "start_line": 7665
  },
  {
    "end_line": 7682,
    "section": "Links",
    "html": "<p><a href=\"/uri\">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>\n",
    "markdown": "[link *foo **bar** `#`*][ref]\n\n[ref]: /uri\n",
    "example": 501,
    "start_line": 7676
  },
  {
    "end_line": 7691,
    "section": "Links",
    "html": "<p><a href=\"/uri\"><img src=\"moon.jpg\" alt=\"moon\" /></a></p>\n",
    "markdown": "[![moon](moon.jpg)][ref]\n\n[ref]: /uri\n",
    "example": 502,
    "start_line": 7685
  },
  {
    "end_line": 7702,
    "section": "Links",
    "html": "<p>[foo <a href=\"/uri\">bar</a>]<a href=\"/uri\">ref</a></p>\n",
    "markdown": "[foo [bar](/uri)][ref]\n\n[ref]: /uri\n",
    "example": 503,
    "start_line": 7696
  },
  {
    "end_line": 7711,
    "section": "Links",
    "html": "<p>[foo <em>bar <a href=\"/uri\">baz</a></em>]<a href=\"/uri\">ref</a></p>\n",
    "markdown": "[foo *bar [baz][ref]*][ref]\n\n[ref]: /uri\n",
    "example": 504,
    "start_line": 7705
  },
  {
    "end_line": 7726,
    "section": "Links",
    "html": "<p>*<a href=\"/uri\">foo*</a></p>\n",
    "markdown": "*[foo*][ref]\n\n[ref]: /uri\n",
    "example": 505,
    "start_line": 7720
  },
  {
    "end_line": 7735,
    "section": "Links",
    "html": "<p><a href=\"/uri\">foo *bar</a></p>\n",
    "markdown": "[foo *bar][ref]\n\n[ref]: /uri\n",
    "example": 506,
    "start_line": 7729
  },
  {
    "end_line": 7747,
    "section": "Links",
    "html": "<p>[foo <bar attr=\"][ref]\"></p>\n",
    "markdown": "[foo <bar attr=\"][ref]\">\n\n[ref]: /uri\n",
    "example": 507,
    "start_line": 7741
  },
  {
    "end_line": 7756,
    "section": "Links",
    "html": "<p>[foo<code>][ref]</code></p>\n",
    "markdown": "[foo`][ref]`\n\n[ref]: /uri\n",
    "example": 508,
    "start_line": 7750
  },
  {
    "end_line": 7765,
    "section": "Links",
    "html": "<p>[foo<a href=\"http://example.com/?search=%5D%5Bref%5D\">http://example.com/?search=][ref]</a></p>\n",
    "markdown": "[foo<http://example.com/?search=][ref]>\n\n[ref]: /uri\n",
    "example": 509,
    "start_line": 7759
  },
  {
    "end_line": 7776,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">foo</a></p>\n",
    "markdown": "[foo][BaR]\n\n[bar]: /url \"title\"\n",
    "example": 510,
    "start_line": 7770
  },
  {
    "end_line": 7787,
    "section": "Links",
    "html": "<p><a href=\"/url\">Толпой</a> is a Russian word.</p>\n",
    "markdown": "[Толпой][Толпой] is a Russian word.\n\n[ТОЛПОЙ]: /url\n",
    "example": 511,
    "start_line": 7781
  },
  {
    "end_line": 7800,
    "section": "Links",
    "html": "<p><a href=\"/url\">Baz</a></p>\n",
    "markdown": "[Foo\n  bar]: /url\n\n[Baz][Foo bar]\n",
    "example": 512,
    "start_line": 7793
  },
  {
    "end_line": 7812,
    "section": "Links",
    "html": "<p>[foo] <a href=\"/url\" title=\"title\">bar</a></p>\n",
    "markdown": "[foo] [bar]\n\n[bar]: /url \"title\"\n",
    "example": 513,
    "start_line": 7806
  },
  {
    "end_line": 7823,
    "section": "Links",
    "html": "<p>[foo]\n<a href=\"/url\" title=\"title\">bar</a></p>\n",
    "markdown": "[foo]\n[bar]\n\n[bar]: /url \"title\"\n",
    "example": 514,
    "start_line": 7815
  },
  {
    "end_line": 7864,
    "section": "Links",
    "html": "<p><a href=\"/url1\">bar</a></p>\n",
    "markdown": "[foo]: /url1\n\n[foo]: /url2\n\n[bar][foo]\n",
    "example": 515,
    "start_line": 7856
  },
  {
    "end_line": 7877,
    "section": "Links",
    "html": "<p>[bar][foo!]</p>\n",
    "markdown": "[bar][foo\\!]\n\n[foo!]: /url\n",
    "example": 516,
    "start_line": 7871
  },
  {
    "end_line": 7890,
    "section": "Links",
    "html": "<p>[foo][ref[]</p>\n<p>[ref[]: /uri</p>\n",
    "markdown": "[foo][ref[]\n\n[ref[]: /uri\n",
    "example": 517,
    "start_line": 7883
  },
  {
    "end_line": 7900,
    "section": "Links",
    "html": "<p>[foo][ref[bar]]</p>\n<p>[ref[bar]]: /uri</p>\n",
    "markdown": "[foo][ref[bar]]\n\n[ref[bar]]: /uri\n",
    "example": 518,
    "start_line": 7893
  },
  {
    "end_line": 7910,
    "section": "Links",
    "html": "<p>[[[foo]]]</p>\n<p>[[[foo]]]: /url</p>\n",
    "markdown": "[[[foo]]]\n\n[[[foo]]]: /url\n",
    "example": 519,
    "start_line": 7903
  },
  {
    "end_line": 7919,
    "section": "Links",
    "html": "<p><a href=\"/uri\">foo</a></p>\n",
    "markdown": "[foo][ref\\[]\n\n[ref\\[]: /uri\n",
    "example": 520,
    "start_line": 7913
  },
  {
    "end_line": 7930,
    "section": "Links",
    "html": "<p><a href=\"/uri\">bar\\</a></p>\n",
    "markdown": "[bar\\\\]: /uri\n\n[bar\\\\]\n",
    "example": 521,
    "start_line": 7924
  },
  {
    "end_line": 7942,
    "section": "Links",
    "html": "<p>[]</p>\n<p>[]: /uri</p>\n",
    "markdown": "[]\n\n[]: /uri\n",
    "example": 522,
    "start_line": 7935
  },
  {
    "end_line": 7956,
    "section": "Links",
    "html": "<p>[\n]</p>\n<p>[\n]: /uri</p>\n",
    "markdown": "[\n ]\n\n[\n ]: /uri\n",
    "example": 523,
    "start_line": 7945
  },
  {
    "end_line": 7974,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">foo</a></p>\n",
    "markdown": "[foo][]\n\n[foo]: /url \"title\"\n",
    "example": 524,
    "start_line": 7968
  },
  {
    "end_line": 7983,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\"><em>foo</em> bar</a></p>\n",
    "markdown": "[*foo* bar][]\n\n[*foo* bar]: /url \"title\"\n",
    "example": 525,
    "start_line": 7977
  },
  {
    "end_line": 7994,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">Foo</a></p>\n",
    "markdown": "[Foo][]\n\n[foo]: /url \"title\"\n",
    "example": 526,
    "start_line": 7988
  },
  {
    "end_line": 8009,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">foo</a>\n[]</p>\n",
    "markdown": "[foo] \n[]\n\n[foo]: /url \"title\"\n",
    "example": 527,
    "start_line": 8001
  },
  {
    "end_line": 8027,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">foo</a></p>\n",
    "markdown": "[foo]\n\n[foo]: /url \"title\"\n",
    "example": 528,
    "start_line": 8021
  },
  {
    "end_line": 8036,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\"><em>foo</em> bar</a></p>\n",
    "markdown": "[*foo* bar]\n\n[*foo* bar]: /url \"title\"\n",
    "example": 529,
    "start_line": 8030
  },
  {
    "end_line": 8045,
    "section": "Links",
    "html": "<p>[<a href=\"/url\" title=\"title\"><em>foo</em> bar</a>]</p>\n",
    "markdown": "[[*foo* bar]]\n\n[*foo* bar]: /url \"title\"\n",
    "example": 530,
    "start_line": 8039
  },
  {
    "end_line": 8054,
    "section": "Links",
    "html": "<p>[[bar <a href=\"/url\">foo</a></p>\n",
    "markdown": "[[bar [foo]\n\n[foo]: /url\n",
    "example": 531,
    "start_line": 8048
  },
  {
    "end_line": 8065,
    "section": "Links",
    "html": "<p><a href=\"/url\" title=\"title\">Foo</a></p>\n",
    "markdown": "[Foo]\n\n[foo]: /url \"title\"\n",
    "example": 532,
    "start_line": 8059
  },
  {
    "end_line": 8076,
    "section": "Links",
    "html": "<p><a href=\"/url\">foo</a> bar</p>\n",
    "markdown": "[foo] bar\n\n[foo]: /url\n",
    "example": 533,
    "start_line": 8070
  },
  {
    "end_line": 8088,
    "section": "Links",
    "html": "<p>[foo]</p>\n",
    "markdown": "\\[foo]\n\n[foo]: /url \"title\"\n",
    "example": 534,
    "start_line": 8082
  },
  {
    "end_line": 8100,
    "section": "Links",
    "html": "<p>*<a href=\"/url\">foo*</a></p>\n",
    "markdown": "[foo*]: /url\n\n*[foo*]\n",
    "example": 535,
    "start_line": 8094
  },
  {
    "end_line": 8113,
    "section": "Links",
    "html": "<p><a href=\"/url2\">foo</a></p>\n",
    "markdown": "[foo][bar]\n\n[foo]: /url1\n[bar]: /url2\n",
    "example": 536,
    "start_line": 8106
  },
  {
    "end_line": 8121,
    "section": "Links",
    "html": "<p><a href=\"/url1\">foo</a></p>\n",
    "markdown": "[foo][]\n\n[foo]: /url1\n",
    "example": 537,
    "start_line": 8115
  },
  {
    "end_line": 8131,
    "section": "Links",
    "html": "<p><a href=\"\">foo</a></p>\n",
    "markdown": "[foo]()\n\n[foo]: /url1\n",
    "example": 538,
    "start_line": 8125
  },
  {
    "end_line": 8139,
    "section": "Links",
    "html": "<p><a href=\"/url1\">foo</a>(not a link)</p>\n",
    "markdown": "[foo](not a link)\n\n[foo]: /url1\n",
    "example": 539,
    "start_line": 8133
  },
  {
    "end_line": 8150,
    "section": "Links",
    "html": "<p>[foo]<a href=\"/url\">bar</a></p>\n",
    "markdown": "[foo][bar][baz]\n\n[baz]: /url\n",
    "example": 540,
    "start_line": 8144
  },
  {
    "end_line": 8163,
    "section": "Links",
    "html": "<p><a href=\"/url2\">foo</a><a href=\"/url1\">baz</a></p>\n",
    "markdown": "[foo][bar][baz]\n\n[baz]: /url1\n[bar]: /url2\n",
    "example": 541,
    "start_line": 8156
  },
  {
    "end_line": 8176,
    "section": "Links",
    "html": "<p>[foo]<a href=\"/url1\">bar</a></p>\n",
    "markdown": "[foo][bar][baz]\n\n[baz]: /url1\n[foo]: /url2\n",
    "example": 542,
    "start_line": 8169
  },
  {
    "end_line": 8196,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo\" title=\"title\" /></p>\n",
    "markdown": "![foo](/url \"title\")\n",
    "example": 543,
    "start_line": 8192
  },
  {
    "end_line": 8205,
    "section": "Images",
    "html": "<p><img src=\"train.jpg\" alt=\"foo bar\" title=\"train &amp; tracks\" /></p>\n",
    "markdown": "![foo *bar*]\n\n[foo *bar*]: train.jpg \"train & tracks\"\n",
    "example": 544,
    "start_line": 8199
  },
  {
    "end_line": 8212,
    "section": "Images",
    "html": "<p><img src=\"/url2\" alt=\"foo bar\" /></p>\n",
    "markdown": "![foo ![bar](/url)](/url2)\n",
    "example": 545,
    "start_line": 8208
  },
  {
    "end_line": 8219,
    "section": "Images",
    "html": "<p><img src=\"/url2\" alt=\"foo bar\" /></p>\n",
    "markdown": "![foo [bar](/url)](/url2)\n",
    "example": 546,
    "start_line": 8215
  },
  {
    "end_line": 8235,
    "section": "Images",
    "html": "<p><img src=\"train.jpg\" alt=\"foo bar\" title=\"train &amp; tracks\" /></p>\n",
    "markdown": "![foo *bar*][]\n\n[foo *bar*]: train.jpg \"train & tracks\"\n",
    "example": 547,
    "start_line": 8229
  },
  {
    "end_line": 8244,
    "section": "Images",
    "html": "<p><img src=\"train.jpg\" alt=\"foo bar\" title=\"train &amp; tracks\" /></p>\n",
    "markdown": "![foo *bar*][foobar]\n\n[FOOBAR]: train.jpg \"train & tracks\"\n",
    "example": 548,
    "start_line": 8238
  },
  {
    "end_line": 8251,
    "section": "Images",
    "html": "<p><img src=\"train.jpg\" alt=\"foo\" /></p>\n",
    "markdown": "![foo](train.jpg)\n",
    "example": 549,
    "start_line": 8247
  },
  {
    "end_line": 8258,
    "section": "Images",
    "html": "<p>My <img src=\"/path/to/train.jpg\" alt=\"foo bar\" title=\"title\" /></p>\n",
    "markdown": "My ![foo bar](/path/to/train.jpg  \"title\"   )\n",
    "example": 550,
    "start_line": 8254
  },
  {
    "end_line": 8265,
    "section": "Images",
    "html": "<p><img src=\"url\" alt=\"foo\" /></p>\n",
    "markdown": "![foo](<url>)\n",
    "example": 551,
    "start_line": 8261
  },
  {
    "end_line": 8272,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"\" /></p>\n",
    "markdown": "![](/url)\n",
    "example": 552,
    "start_line": 8268
  },
  {
    "end_line": 8283,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo\" /></p>\n",
    "markdown": "![foo][bar]\n\n[bar]: /url\n",
    "example": 553,
    "start_line": 8277
  },
  {
    "end_line": 8292,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo\" /></p>\n",
    "markdown": "![foo][bar]\n\n[BAR]: /url\n",
    "example": 554,
    "start_line": 8286
  },
  {
    "end_line": 8303,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo\" title=\"title\" /></p>\n",
    "markdown": "![foo][]\n\n[foo]: /url \"title\"\n",
    "example": 555,
    "start_line": 8297
  },
  {
    "end_line": 8312,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo bar\" title=\"title\" /></p>\n",
    "markdown": "![*foo* bar][]\n\n[*foo* bar]: /url \"title\"\n",
    "example": 556,
    "start_line": 8306
  },
  {
    "end_line": 8323,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"Foo\" title=\"title\" /></p>\n",
    "markdown": "![Foo][]\n\n[foo]: /url \"title\"\n",
    "example": 557,
    "start_line": 8317
  },
  {
    "end_line": 8337,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo\" title=\"title\" />\n[]</p>\n",
    "markdown": "![foo] \n[]\n\n[foo]: /url \"title\"\n",
    "example": 558,
    "start_line": 8329
  },
  {
    "end_line": 8348,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo\" title=\"title\" /></p>\n",
    "markdown": "![foo]\n\n[foo]: /url \"title\"\n",
    "example": 559,
    "start_line": 8342
  },
  {
    "end_line": 8357,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"foo bar\" title=\"title\" /></p>\n",
    "markdown": "![*foo* bar]\n\n[*foo* bar]: /url \"title\"\n",
    "example": 560,
    "start_line": 8351
  },
  {
    "end_line": 8369,
    "section": "Images",
    "html": "<p>![[foo]]</p>\n<p>[[foo]]: /url &quot;title&quot;</p>\n",
    "markdown": "![[foo]]\n\n[[foo]]: /url \"title\"\n",
    "example": 561,
    "start_line": 8362
  },
  {
    "end_line": 8380,
    "section": "Images",
    "html": "<p><img src=\"/url\" alt=\"Foo\" title=\"title\" /></p>\n",
    "markdown": "![Foo]\n\n[foo]: /url \"title\"\n",
    "example": 562,
    "start_line": 8374
  },
  {
    "end_line": 8392,
    "section": "Images",
    "html": "<p>![foo]</p>\n",
    "markdown": "!\\[foo]\n\n[foo]: /url \"title\"\n",
    "example": 563,
    "start_line": 8386
  },
  {
    "end_line": 8404,
    "section": "Images",
    "html": "<p>!<a href=\"/url\" title=\"title\">foo</a></p>\n",
    "markdown": "\\![foo]\n\n[foo]: /url \"title\"\n",
    "example": 564,
    "start_line": 8398
  },
  {
    "end_line": 8435,
    "section": "Autolinks",
    "html": "<p><a href=\"http://foo.bar.baz\">http://foo.bar.baz</a></p>\n",
    "markdown": "<http://foo.bar.baz>\n",
    "example": 565,
    "start_line": 8431
  },
  {
    "end_line": 8442,
    "section": "Autolinks",
    "html": "<p><a href=\"http://foo.bar.baz/test?q=hello&amp;id=22&amp;boolean\">http://foo.bar.baz/test?q=hello&amp;id=22&amp;boolean</a></p>\n",
    "markdown": "<http://foo.bar.baz/test?q=hello&id=22&boolean>\n",
    "example": 566,
    "start_line": 8438
  },
  {
    "end_line": 8449,
    "section": "Autolinks",
    "html": "<p><a href=\"irc://foo.bar:2233/baz\">irc://foo.bar:2233/baz</a></p>\n",
    "markdown": "<irc://foo.bar:2233/baz>\n",
    "example": 567,
    "start_line": 8445
  },
  {
    "end_line": 8458,
    "section": "Autolinks",
    "html": "<p><a href=\"MAILTO:FOO@BAR.BAZ\">MAILTO:FOO@BAR.BAZ</a></p>\n",
    "markdown": "<MAILTO:FOO@BAR.BAZ>\n",
    "example": 568,
    "start_line": 8454
  },
  {
    "end_line": 8470,
    "section": "Autolinks",
    "html": "<p><a href=\"a+b+c:d\">a+b+c:d</a></p>\n",
    "markdown": "<a+b+c:d>\n",
    "example": 569,
    "start_line": 8466
  },
  {
    "end_line": 8477,
    "section": "Autolinks",
    "html": "<p><a href=\"made-up-scheme://foo,bar\">made-up-scheme://foo,bar</a></p>\n",
    "markdown": "<made-up-scheme://foo,bar>\n",
    "example": 570,
    "start_line": 8473
  },
  {
    "end_line": 8484,
    "section": "Autolinks",
    "html": "<p><a href=\"http://../\">http://../</a></p>\n",
    "markdown": "<http://../>\n",
    "example": 571,
    "start_line": 8480
  },
  {
    "end_line": 8491,
    "section": "Autolinks",
    "html": "<p><a href=\"localhost:5001/foo\">localhost:5001/foo</a></p>\n",
    "markdown": "<localhost:5001/foo>\n",
    "example": 572,
    "start_line": 8487
  },
  {
    "end_line": 8500,
    "section": "Autolinks",
    "html": "<p>&lt;http://foo.bar/baz bim&gt;</p>\n",
    "markdown": "<http://foo.bar/baz bim>\n",
    "example": 573,
    "start_line": 8496
  },
  {
    "end_line": 8509,
    "section": "Autolinks",
    "html": "<p><a href=\"http://example.com/%5C%5B%5C\">http://example.com/\\[\\</a></p>\n",
    "markdown": "<http://example.com/\\[\\>\n",
    "example": 574,
    "start_line": 8505
  },
  {
    "end_line": 8531,
    "section": "Autolinks",
    "html": "<p><a href=\"mailto:foo@bar.example.com\">foo@bar.example.com</a></p>\n",
    "markdown": "<foo@bar.example.com>\n",
    "example": 575,
    "start_line": 8527
  },
  {
    "end_line": 8538,
    "section": "Autolinks",
    "html": "<p><a href=\"mailto:foo+special@Bar.baz-bar0.com\">foo+special@Bar.baz-bar0.com</a></p>\n",
    "markdown": "<foo+special@Bar.baz-bar0.com>\n",
    "example": 576,
    "start_line": 8534
  },
  {
    "end_line": 8547,
    "section": "Autolinks",
    "html": "<p>&lt;foo+@bar.example.com&gt;</p>\n",
    "markdown": "<foo\\+@bar.example.com>\n",
    "example": 577,
    "start_line": 8543
  },
  {
    "end_line": 8556,
    "section": "Autolinks",
    "html": "<p>&lt;&gt;</p>\n",
    "markdown": "<>\n",
    "example": 578,
    "start_line": 8552
  },
  {
    "end_line": 8563,
    "section": "Autolinks",
    "html": "<p>&lt; http://foo.bar &gt;</p>\n",
    "markdown": "< http://foo.bar >\n",
    "example": 579,
    "start_line": 8559
  },
  {
    "end_line": 8570,
    "section": "Autolinks",
    "html": "<p>&lt;m:abc&gt;</p>\n",
    "markdown": "<m:abc>\n",
    "example": 580,
    "start_line": 8566
  },
  {
    "end_line": 8577,
    "section": "Autolinks",
    "html": "<p>&lt;foo.bar.baz&gt;</p>\n",
    "markdown": "<foo.bar.baz>\n",
    "example": 581,
    "start_line": 8573
  },
  {
    "end_line": 8584,
    "section": "Autolinks",
    "html": "<p>http://example.com</p>\n",
    "markdown": "http://example.com\n",
    "example": 582,
    "start_line": 8580
  },
  {
    "end_line": 8591,
    "section": "Autolinks",
    "html": "<p>foo@bar.example.com</p>\n",
    "markdown": "foo@bar.example.com\n",
    "example": 583,
    "start_line": 8587
  },
  {
    "end_line": 8673,
    "section": "Raw HTML",
    "html": "<p><a><bab><c2c></p>\n",
    "markdown": "<a><bab><c2c>\n",
    "example": 584,
    "start_line": 8669
  },
  {
    "end_line": 8682,
    "section": "Raw HTML",
    "html": "<p><a/><b2/></p>\n",
    "markdown": "<a/><b2/>\n",
    "example": 585,
    "start_line": 8678
  },
  {
    "end_line": 8693,
    "section": "Raw HTML",
    "html": "<p><a  /><b2\ndata=\"foo\" ></p>\n",
    "markdown": "<a  /><b2\ndata=\"foo\" >\n",
    "example": 586,
    "start_line": 8687
  },
  {
    "end_line": 8704,
    "section": "Raw HTML",
    "html": "<p><a foo=\"bar\" bam = 'baz <em>\"</em>'\n_boolean zoop:33=zoop:33 /></p>\n",
    "markdown": "<a foo=\"bar\" bam = 'baz <em>\"</em>'\n_boolean zoop:33=zoop:33 />\n",
    "example": 587,
    "start_line": 8698
  },
  {
    "end_line": 8713,
    "section": "Raw HTML",
    "html": "<p>Foo <responsive-image src=\"foo.jpg\" /></p>\n",
    "markdown": "Foo <responsive-image src=\"foo.jpg\" />\n",
    "example": 588,
    "start_line": 8709
  },
  {
    "end_line": 8722,
    "section": "Raw HTML",
    "html": "<p>&lt;33&gt; &lt;__&gt;</p>\n",
    "markdown": "<33> <__>\n",
    "example": 589,
    "start_line": 8718
  },
  {
    "end_line": 8731,
    "section": "Raw HTML",
    "html": "<p>&lt;a h*#ref=&quot;hi&quot;&gt;</p>\n",
    "markdown": "<a h*#ref=\"hi\">\n",
    "example": 590,
    "start_line": 8727
  },
  {
    "end_line": 8740,
    "section": "Raw HTML",
    "html": "<p>&lt;a href=&quot;hi'&gt; &lt;a href=hi'&gt;</p>\n",
    "markdown": "<a href=\"hi'> <a href=hi'>\n",
    "example": 591,
    "start_line": 8736
  },
  {
    "end_line": 8751,
    "section": "Raw HTML",
    "html": "<p>&lt; a&gt;&lt;\nfoo&gt;&lt;bar/ &gt;</p>\n",
    "markdown": "< a><\nfoo><bar/ >\n",
    "example": 592,
    "start_line": 8745
  },
  {
    "end_line": 8760,
    "section": "Raw HTML",
    "html": "<p>&lt;a href='bar'title=title&gt;</p>\n",
    "markdown": "<a href='bar'title=title>\n",
    "example": 593,
    "start_line": 8756
  },
  {
    "end_line": 8769,
    "section": "Raw HTML",
    "html": "<p></a></foo ></p>\n",
    "markdown": "</a></foo >\n",
    "example": 594,
    "start_line": 8765
  },
  {
    "end_line": 8778,
    "section": "Raw HTML",
    "html": "<p>&lt;/a href=&quot;foo&quot;&gt;</p>\n",
    "markdown": "</a href=\"foo\">\n",
    "example": 595,
    "start_line": 8774
  },
  {
    "end_line": 8789,
    "section": "Raw HTML",
    "html": "<p>foo <!-- this is a\ncomment - with hyphen --></p>\n",
    "markdown": "foo <!-- this is a\ncomment - with hyphen -->\n",
    "example": 596,
    "start_line": 8783
  },
  {
    "end_line": 8796,
    "section": "Raw HTML",
    "html": "<p>foo &lt;!-- not a comment -- two hyphens --&gt;</p>\n",
    "markdown": "foo <!-- not a comment -- two hyphens -->\n",
    "example": 597,
    "start_line": 8792
  },
  {
    "end_line": 8808,
    "section": "Raw HTML",
    "html": "<p>foo &lt;!--&gt; foo --&gt;</p>\n<p>foo &lt;!-- foo---&gt;</p>\n",
    "markdown": "foo <!--> foo -->\n\nfoo <!-- foo--->\n",
    "example": 598,
    "start_line": 8801
  },
  {
    "end_line": 8817,
    "section": "Raw HTML",
    "html": "<p>foo <?php echo $a; ?></p>\n",
    "markdown": "foo <?php echo $a; ?>\n",
    "example": 599,
    "start_line": 8813
  },
  {
    "end_line": 8826,
    "section": "Raw HTML",
    "html": "<p>foo <!ELEMENT br EMPTY></p>\n",
    "markdown": "foo <!ELEMENT br EMPTY>\n",
    "example": 600,
    "start_line": 8822
  },
  {
    "end_line": 8835,
    "section": "Raw HTML",
    "html": "<p>foo <![CDATA[>&<]]></p>\n",
    "markdown": "foo <![CDATA[>&<]]>\n",
    "example": 601,
    "start_line": 8831
  },
  {
    "end_line": 8845,
    "section": "Raw HTML",
    "html": "<p>foo <a href=\"&ouml;\"></p>\n",
    "markdown": "foo <a href=\"&ouml;\">\n",
    "example": 602,
    "start_line": 8841
  },
  {
    "end_line": 8854,
    "section": "Raw HTML",
    "html": "<p>foo <a href=\"\\*\"></p>\n",
    "markdown": "foo <a href=\"\\*\">\n",
    "example": 603,
    "start_line": 8850
  },
  {
    "end_line": 8861,
    "section": "Raw HTML",
    "html": "<p>&lt;a href=&quot;&quot;&quot;&gt;</p>\n",
    "markdown": "<a href=\"\\\"\">\n",
    "example": 604,
    "start_line": 8857
  },
  {
    "end_line": 8877,
    "section": "Hard line breaks",
    "html": "<p>foo<br />\nbaz</p>\n",
    "markdown": "foo  \nbaz\n",
    "example": 605,
    "start_line": 8871
  },
  {
    "end_line": 8889,
    "section": "Hard line breaks",
    "html": "<p>foo<br />\nbaz</p>\n",
    "markdown": "foo\\\nbaz\n",
    "example": 606,
    "start_line": 8883
  },
  {
    "end_line": 8900,
    "section": "Hard line breaks",
    "html": "<p>foo<br />\nbaz</p>\n",
    "markdown": "foo       \nbaz\n",
    "example": 607,
    "start_line": 8894
  },
  {
    "end_line": 8911,
    "section": "Hard line breaks",
    "html": "<p>foo<br />\nbar</p>\n",
    "markdown": "foo  \n     bar\n",
    "example": 608,
    "start_line": 8905
  },
  {
    "end_line": 8920,
    "section": "Hard line breaks",
    "html": "<p>foo<br />\nbar</p>\n",
    "markdown": "foo\\\n     bar\n",
    "example": 609,
    "start_line": 8914
  },
  {
    "end_line": 8932,
    "section": "Hard line breaks",
    "html": "<p><em>foo<br />\nbar</em></p>\n",
    "markdown": "*foo  \nbar*\n",
    "example": 610,
    "start_line": 8926
  },
  {
    "end_line": 8941,
    "section": "Hard line breaks",
    "html": "<p><em>foo<br />\nbar</em></p>\n",
    "markdown": "*foo\\\nbar*\n",
    "example": 611,
    "start_line": 8935
  },
  {
    "end_line": 8951,
    "section": "Hard line breaks",
    "html": "<p><code>code span</code></p>\n",
    "markdown": "`code  \nspan`\n",
    "example": 612,
    "start_line": 8946
  },
  {
    "end_line": 8959,
    "section": "Hard line breaks",
    "html": "<p><code>code\\ span</code></p>\n",
    "markdown": "`code\\\nspan`\n",
    "example": 613,
    "start_line": 8954
  },
  {
    "end_line": 8970,
    "section": "Hard line breaks",
    "html": "<p><a href=\"foo  \nbar\"></p>\n",
    "markdown": "<a href=\"foo  \nbar\">\n",
    "example": 614,
    "start_line": 8964
  },
  {
    "end_line": 8979,
    "section": "Hard line breaks",
    "html": "<p><a href=\"foo\\\nbar\"></p>\n",
    "markdown": "<a href=\"foo\\\nbar\">\n",
    "example": 615,
    "start_line": 8973
  },
  {
    "end_line": 8990,
    "section": "Hard line breaks",
    "html": "<p>foo\\</p>\n",
    "markdown": "foo\\\n",
    "example": 616,
    "start_line": 8986
  },
  {
    "end_line": 8997,
    "section": "Hard line breaks",
    "html": "<p>foo</p>\n",
    "markdown": "foo  \n",
    "example": 617,
    "start_line": 8993
  },
  {
    "end_line": 9004,
    "section": "Hard line breaks",
    "html": "<h3>foo\\</h3>\n",
    "markdown": "### foo\\\n",
    "example": 618,
    "start_line": 9000
  },
  {
    "end_line": 9011,
    "section": "Hard line breaks",
    "html": "<h3>foo</h3>\n",
    "markdown": "### foo  \n",
    "example": 619,
    "start_line": 9007
  },
  {
    "end_line": 9028,
    "section": "Soft line breaks",
    "html": "<p>foo\nbaz</p>\n",
    "markdown": "foo\nbaz\n",
    "example": 620,
    "start_line": 9022
  },
  {
    "end_line": 9040,
    "section": "Soft line breaks",
    "html": "<p>foo\nbaz</p>\n",
    "markdown": "foo \n baz\n",
    "example": 621,
    "start_line": 9034
  },
  {
    "end_line": 9058,
    "section": "Textual content",
    "html": "<p>hello $.;'there</p>\n",
    "markdown": "hello $.;'there\n",
    "example": 622,
    "start_line": 9054
  },
  {
    "end_line": 9065,
    "section": "Textual content",
    "html": "<p>Foo χρῆν</p>\n",
    "markdown": "Foo χρῆν\n",
    "example": 623,
    "start_line": 9061
  },
  {
    "end_line": 9074,
    "section": "Textual content",
    "html": "<p>Multiple     spaces</p>\n",
    "markdown": "Multiple     spaces\n",
    "example": 624,
    "start_line": 9070
  }
]
```

## File: `test/functional/makehtml/cases/features/#143.support-image-dimensions.html`
```html
<p><img src="./pic/pic1_50.png" alt="my image" width="100px" height="20px" /></p>
<p><img src="./pic/pic1_50.png" alt="my image2" width="100px" height="20px" /></p>
```

## File: `test/functional/makehtml/cases/features/#143.support-image-dimensions.md`
```markdown
![my image](./pic/pic1_50.png =100pxx20px)

![my image2][1]

[1]: ./pic/pic1_50.png =100pxx20px
```

## File: `test/functional/makehtml/cases/features/#164.1.simple-autolink.html`
```html
<p>foo.bar</p>
<p>www.foobar</p>
<p><a href="http://www.foobar.com">www.foobar.com</a></p>
<p><a href="http://foobar.com">http://foobar.com</a></p>
<p><a href="https://www.foobar.com/baz?bazinga=nhecos">https://www.foobar.com/baz?bazinga=nhecos</a>;</p>
```

## File: `test/functional/makehtml/cases/features/#164.1.simple-autolink.md`
```markdown
foo.bar

www.foobar

www.foobar.com

http://foobar.com

https://www.foobar.com/baz?bazinga=nhecos;
```

## File: `test/functional/makehtml/cases/features/#164.2.disallow-underscore-emphasis-mid-word.html`
```html
<p>this is a sentence_with_mid underscores</p>
<p>this is a sentence with just_one underscore</p>
<p>this <em>should be parsed</em> as emphasis</p>
<p>this is double__underscore__mid word</p>
<p>this has just__one double underscore</p>
<p>this <strong>should be parsed</strong> as bold</p>
<p>emphasis at <em>end of sentence</em></p>
<p><em>emphasis at</em> line start</p>
<p>multi <em>line emphasis
yeah it is</em> yeah</p>
```

## File: `test/functional/makehtml/cases/features/#164.2.disallow-underscore-emphasis-mid-word.md`
```markdown
this is a sentence_with_mid underscores

this is a sentence with just_one underscore

this _should be parsed_ as emphasis

this is double__underscore__mid word

this has just__one double underscore

this __should be parsed__ as bold

emphasis at _end of sentence_

_emphasis at_ line start

multi _line emphasis
yeah it is_ yeah
```

## File: `test/functional/makehtml/cases/features/#164.3.strikethrough.html`
```html
<p>a <del>strikethrough</del> word</p>
<p>this should~~not be parsed</p>
<p><del>strike-through text</del></p>
<p><code>~~strikethough inside code span~~</code></p>
<p>escaped ~~strikethrough~~</p>
<p>escaped ~~strikethrough~~</p>
```

## File: `test/functional/makehtml/cases/features/#164.3.strikethrough.md`
```markdown
a ~~strikethrough~~ word

this should~~not be parsed

~~strike-through text~~

`~~strikethough inside code span~~`

escaped \~~strikethrough~~

escaped \~~strikethrough\~~
```

## File: `test/functional/makehtml/cases/features/#164.4.tasklists.html`
```html
<h1 id="mythings">my things</h1>
<ul>
    <li>foo</li>
    <li>[] bar</li>
    <li class="task-list-item" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;"> baz</li>
    <li class="task-list-item" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;" checked> bazinga</li>
    <li class="task-list-item" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;" checked> bazinga 2</li>
</ul>
<p>otherthings</p>
```

## File: `test/functional/makehtml/cases/features/#164.4.tasklists.md`
```markdown
# my things

 -  foo
 - [] bar
 - [ ] baz
 - [x] bazinga
 - [X] bazinga 2

otherthings
```

## File: `test/functional/makehtml/cases/features/#178.markdown-inside-html-does-not-parse.html`
```html
<h1 id="somemarkdown">some markdown</h1>
<p>blabla</p>
<div>This is **not parsed**</div>
<div markdown="1"><p>This is <strong>parsed</strong></p></div>
<div>This is **not parsed**</div>
```

## File: `test/functional/makehtml/cases/features/#178.markdown-inside-html-does-not-parse.md`
```markdown
# some markdown

blabla
<div>This is **not parsed**</div>
<div markdown="1">This is **parsed**</div>
<div>This is **not parsed**</div>
```

## File: `test/functional/makehtml/cases/features/#198.literalMidWordUnderscores-changes-behavior-of-asterisk.html`
```html
<p>foo *bar *baz</p>
<p>foo **bar **baz</p>
<p>foo _bar _baz</p>
<p>foo __bar __baz</p>
```

## File: `test/functional/makehtml/cases/features/#198.literalMidWordUnderscores-changes-behavior-of-asterisk.md`
```markdown
foo *bar *baz

foo **bar **baz

foo _bar _baz

foo __bar __baz
```

## File: `test/functional/makehtml/cases/features/#204.certain-links-with-at-and-dot-break-url.html`
```html
<p><a href="http://website.com/img@x2.jpg">http://website.com/img@x2.jpg</a></p>
<p><a href="http://website.com/img-x2.jpg">http://website.com/img-x2.jpg</a></p>
<p><a href="http://website.com/img@x2">http://website.com/img@x2</a></p>
<p><a href="http://website.com/img@.jpg">http://website.com/img@.jpg</a></p>
```

## File: `test/functional/makehtml/cases/features/#204.certain-links-with-at-and-dot-break-url.md`
```markdown
http://website.com/img@x2.jpg

http://website.com/img-x2.jpg

http://website.com/img@x2

http://website.com/img@.jpg
```

## File: `test/functional/makehtml/cases/features/#206.treat-single-line-breaks-as-br.html`
```html
<p>a simple<br />
wrapped line</p>
```

## File: `test/functional/makehtml/cases/features/#206.treat-single-line-breaks-as-br.md`
```markdown
a simple
wrapped line
```

## File: `test/functional/makehtml/cases/features/#214.escaped-markdown-chars-break-strikethrough.html`
```html
<p>Your friend <del><a href="www.google.com"><strong>test*</strong></a></del> (<del><a href="www.google.com"><em>@test</em></a></del>) updated his/her description</p>
```

## File: `test/functional/makehtml/cases/features/#214.escaped-markdown-chars-break-strikethrough.md`
```markdown
Your friend ~~[**test\***](www.google.com)~~ (~~[*@test*](www.google.com)~~) updated his/her description
```

## File: `test/functional/makehtml/cases/features/#259.es6-template-strings-indentation-issues.html`
```html
<h2 id="markdowndoc">markdown doc</h2>
<p>you can use markdown for card documentation</p>
<ul>
    <li>foo</li>
    <li>bar</li>
</ul>
```

## File: `test/functional/makehtml/cases/features/#259.es6-template-strings-indentation-issues.md`
```markdown
      ## markdown doc
      
      you can use markdown for card documentation
        - foo
        - bar
```

## File: `test/functional/makehtml/cases/features/#284.simplifiedAutoLink-does-not-match-GFM-style.html`
```html
<p>this is a link to <a href="http://www.github.com">www.github.com</a></p>
<p>this is a link to <a href="http://www.google.com">www.google.com</a></p>
```

## File: `test/functional/makehtml/cases/features/#284.simplifiedAutoLink-does-not-match-GFM-style.md`
```markdown
this is a link to www.github.com

this is a link to <www.google.com>
```

## File: `test/functional/makehtml/cases/features/#316.new-simpleLineBreaks-option-breaks-lists.html`
```html
<ol>
  <li>One</li>
  <li>Two<ul>
      <li>A</li>
      <li>B</li></ul></li>
  <li>Three</li>
</ol>
<blockquote>
  <p>this has<br />
    simple linebreaks</p>
</blockquote>
<pre><code>testing
some
code
</code></pre>
<ol>
  <li><p>paragraphed list</p>
    <p>this belongs<br />
      to the first list item</p></li>
  <li><p>This text<br />
    also</p></li>
</ol>
<p>simple<br />
  text</p>
<ul>
  <li>a list<br />
    item</li>
  <li>another<br />
    list item</li>
</ul>
<p>simple<br />
  text</p>
<ul>
  <li><p>some item</p>
    <p>another<br />
      paragraph</p>
    <ul>
      <li><p>And<br />
          now</p>
        <p>paragraph<br />
          sublist</p>
        <ul>
          <li><p>and<br />
              even</p>
              <p>another<br />
                one</p></li></ul></li></ul></li>
  <li><p>foo</p></li>
</ul>
```

## File: `test/functional/makehtml/cases/features/#316.new-simpleLineBreaks-option-breaks-lists.md`
```markdown
1. One
2. Two
    - A
    - B
3. Three

> this has
> simple linebreaks

    testing
    some
    code

 1. paragraphed list

    this belongs
    to the first list item
    
 2. This text
    also

simple
text

 - a list
   item
 - another
   list item

simple
text

  - some item
 
    another
    paragraph
   
      - And
        now
     
        paragraph
        sublist
     
          - and
            even
       
            another
            one

 - foo

```

## File: `test/functional/makehtml/cases/features/#318.simpleLineBreaks-does-not-work-with-chinese-characters.html`
```html
<p>foo烫<br />
bar</p>
<p>foo<br />
bar</p>
```

## File: `test/functional/makehtml/cases/features/#318.simpleLineBreaks-does-not-work-with-chinese-characters.md`
```markdown
foo烫
bar

foo
bar
```

## File: `test/functional/makehtml/cases/features/#320.github-compatible-generated-header-id.html`
```html
<h1 id="some-header">some header</h1>
<h1 id="some-header-with--chars">some header with &amp;+$,/:;=?@\"#{}|^~[]`\*()%.!' chars</h1>
<h1 id="another-header--with--chars">another header &gt; with &lt; chars</h1>
```

## File: `test/functional/makehtml/cases/features/#320.github-compatible-generated-header-id.md`
```markdown
# some header

# some header with &+$,/:;=?@\"#{}|^~[]`\\*()%.!' chars

# another header > with < chars
```

## File: `test/functional/makehtml/cases/features/#323.simpleLineBreaks-breaks-with-strong.html`
```html
<p><strong>Nom :</strong> aaaa<br />
<strong>Nom :</strong> aaa</p>
```

## File: `test/functional/makehtml/cases/features/#323.simpleLineBreaks-breaks-with-strong.md`
```markdown
**Nom :** aaaa
**Nom :** aaa
```

## File: `test/functional/makehtml/cases/features/#330.simplifiedAutoLink-drops-character-before-and-after-linked-mail.html`
```html
<p>Just an example <a href="mailto:info@example.com">info@example.com</a> ok?​</p>
```

## File: `test/functional/makehtml/cases/features/#330.simplifiedAutoLink-drops-character-before-and-after-linked-mail.md`
```markdown
Just an example info@example.com ok?​
```

## File: `test/functional/makehtml/cases/features/#331.allow-escaping-of-tilde.html`
```html
<p>~~test~~</p>
<p><del>test</del></p>
```

## File: `test/functional/makehtml/cases/features/#331.allow-escaping-of-tilde.md`
```markdown
\~~test~~

~~test~~
```

## File: `test/functional/makehtml/cases/features/#355.simplifiedAutoLink-URLs-inside-parenthesis-followed-by-another-character-are-not-parsed-correctly.html`
```html
<p>(<a href="https://www.google.com">https://www.google.com</a>)!</p>
```

## File: `test/functional/makehtml/cases/features/#355.simplifiedAutoLink-URLs-inside-parenthesis-followed-by-another-character-are-not-parsed-correctly.md`
```markdown
(https://www.google.com)!
```

## File: `test/functional/makehtml/cases/features/#374.escape-html-tags.html`
```html
<p>&lt;div&gt;foo&lt;/div&gt;</p>
```

## File: `test/functional/makehtml/cases/features/#374.escape-html-tags.md`
```markdown
\<div>foo\</div>
```

## File: `test/functional/makehtml/cases/features/#378.simplifiedAutoLinks-with-excludeTrailingPunctuationFromURLs.html`
```html
<p>Example <a href="http://example.com">http://example.com</a></p>
```

## File: `test/functional/makehtml/cases/features/#378.simplifiedAutoLinks-with-excludeTrailingPunctuationFromURLs.md`
```markdown
Example <http://example.com>
```

## File: `test/functional/makehtml/cases/features/#379.openLinksInNewWindow-breaks-em-markdup.html`
```html
<p>My <a href="http://example.com" rel="noopener noreferrer" target="_blank">link</a> is <em>important</em></p>
<p>My <a href="http://example.com" rel="noopener noreferrer" target="_blank">link</a> is <strong>important</strong></p>
```

## File: `test/functional/makehtml/cases/features/#379.openLinksInNewWindow-breaks-em-markdup.md`
```markdown
My [link](http://example.com) is _important_

My [link](http://example.com) is __important__
```

## File: `test/functional/makehtml/cases/features/#398.literalMidWordAsterisks-treats-non-word-characters-as-characters.html`
```html
<p>strippers, <strong>hitler</strong>, and stalin</p>
```

## File: `test/functional/makehtml/cases/features/#398.literalMidWordAsterisks-treats-non-word-characters-as-characters.md`
```markdown
strippers, **hitler**, and stalin
```

## File: `test/functional/makehtml/cases/features/#69.header-level-start.html`
```html
<h3 id="given">Given</h3>
<h3 id="when">When</h3>
<h3 id="then">Then</h3>
<h3 id="foo">foo</h3>
<h4 id="bar">bar</h4>
```

## File: `test/functional/makehtml/cases/features/#69.header-level-start.md`
```markdown
#Given

#When

#Then

foo
===

bar
---
```

## File: `test/functional/makehtml/cases/features/#709.allow-whitespaces-after-end-in-metadata.html`
```html
<p><strong>some</strong> markdown text</p>
<ul>
    <li>a list</li>
    <li>another list ---</li>
    <li>and stuff</li>
</ul>
<p>a paragraph --- with dashes</p>
<hr />
```

## File: `test/functional/makehtml/cases/features/#709.allow-whitespaces-after-end-in-metadata.md`
```markdown
---         

title: This is the document title
language: en
author: Tivie

---       
**some** markdown text

- a list
- another list ---
- and stuff

a paragraph --- with dashes

---
```

## File: `test/functional/makehtml/cases/features/customizedHeaderId-simple.html`
```html
<h1 id="simple">Просто заголовок</h1>
<h1 id="headerwithoutcurlybraces">Header without curly braces</h1>
<h1 id="cool">Headers with multiple braces {braces} {are}</h1>
<h1 id="withoutspace">Header</h1>
```

## File: `test/functional/makehtml/cases/features/customizedHeaderId-simple.md`
```markdown
# Просто заголовок {simple}
# Header without curly braces
# Headers with multiple braces {braces} {are} {cool}
# Header{withoutspace}
```

## File: `test/functional/makehtml/cases/features/disable-email-encoding.html`
```html
<p>this email <a href="mailto:foobar@example.com">foobar@example.com</a> should not be encoded</p>
```

## File: `test/functional/makehtml/cases/features/disable-email-encoding.md`
```markdown
this email <foobar@example.com> should not be encoded
```

## File: `test/functional/makehtml/cases/features/disable-gh-codeblocks.html`
```html
<p>this is some text</p>
<p><code>php
function thisThing() {
echo "some weird formatted code!";
}
</code></p>
<p>some other text</p>
```

## File: `test/functional/makehtml/cases/features/disable-gh-codeblocks.md`
```markdown
this is some text

```php
function thisThing() {
  echo "some weird formatted code!";
}
```

some other text
```

## File: `test/functional/makehtml/cases/features/disableForced4SpacesIndentedSublists.html`
```html
<ul>
  <li>foo<ul>
    <li>bar</li></ul></li>
</ul>
<hr />
<ul>
  <li>baz<ol>
    <li>bazinga</li></ol></li>
</ul>
```

## File: `test/functional/makehtml/cases/features/disableForced4SpacesIndentedSublists.md`
```markdown
* foo
  * bar

---

* baz
  1. bazinga
```

## File: `test/functional/makehtml/cases/features/excludeTrailingPunctuationFromURLs-option.html`
```html
<p>url <a href="http://www.google.com">http://www.google.com</a>.</p>
<p>url <a href="http://www.google.com">http://www.google.com</a>!</p>
<p>url <a href="http://www.google.com">http://www.google.com</a>? foo</p>
<p>url (<a href="http://www.google.com">http://www.google.com</a>) bazinga</p>
<p>url [<a href="http://www.google.com">http://www.google.com</a>] bazinga</p>
<p>url <a href="http://www.google.com">http://www.google.com</a>, bar</p>
```

## File: `test/functional/makehtml/cases/features/excludeTrailingPunctuationFromURLs-option.md`
```markdown
url http://www.google.com.

url http://www.google.com!

url http://www.google.com? foo

url (http://www.google.com) bazinga

url [http://www.google.com] bazinga

url http://www.google.com, bar
```

## File: `test/functional/makehtml/cases/features/ghMentions.html`
```html
<p>hello <a href="https://github.com/tivie">@tivie</a> how are you?</p>
<p>this email foo@gmail.com is not parsed</p>
<p>this @mentions is not parsed</p>
<p><a href="https://github.com/john.doe">@john.doe</a></p>
<p><a href="https://github.com/john-doe">@john-doe</a></p>
<p><a href="https://github.com/john_doe">@john_doe</a></p>
<p>@.johndoe</p>
<p>@_johndoe</p>
<p>@-johndoe</p>
<p><a href="https://github.com/johndoe">@johndoe</a>.</p>
<p><a href="https://github.com/johndoe">@johndoe</a>-</p>
<p><a href="https://github.com/johndoe">@johndoe</a>_</p>
```

## File: `test/functional/makehtml/cases/features/ghMentions.md`
```markdown
hello @tivie how are you?

this email foo@gmail.com is not parsed

this \@mentions is not parsed

@john.doe

@john-doe

@john_doe

@.johndoe

@_johndoe

@-johndoe

@johndoe.

@johndoe-

@johndoe_
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-simple.html`
```html
<h1 id="sectionfooheader">foo header</h1>
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-simple.md`
```markdown
# foo header
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-string-and-ghCompatibleHeaderId.html`
```html
<h1 id="my-prefix-foo-header">foo header</h1>
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-string-and-ghCompatibleHeaderId.md`
```markdown
# foo header
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-string-and-ghCompatibleHeaderId2.html`
```html
<h1 id="my-prefix-foo-header">foo header</h1>
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-string-and-ghCompatibleHeaderId2.md`
```markdown
# foo header
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-string.html`
```html
<h1 id="myprefixfooheader">foo header</h1>
```

## File: `test/functional/makehtml/cases/features/prefixHeaderId-string.md`
```markdown
# foo header
```

## File: `test/functional/makehtml/cases/features/relativePathBaseUrl.html`
```html
<p><a href="http://my.site.com/that_dude_mike.js">inline relative linky</a></p>
<p><a href="ftp://wikis.com/micky.txt">inline absolute linky</a></p>
<p><a href="http://my.site.com/painters/Michelangelo.html">global relative linky</a></p>
<p><a href="https://www.my-wikis-site.com/peeps/Michelangelo.html">global absolute linky</a></p>
<p><img src="http://my.site.com/mona-lisa.png" alt="inline relative image" /></p>
<p><img src="http://images.com/mona-lisa.png" alt="inline absolute image" /></p>
<p><img src="http://my.site.com/mona-lisa.png" alt="global relative image" /></p>
<p><img src="https://www.my-photo-site.com/mona-lisa.png" alt="global absolute image" /></p>
<p><a href="#holdin_it_down">just an anchor</a></p>
```

## File: `test/functional/makehtml/cases/features/relativePathBaseUrl.md`
```markdown
[inline relative linky](that_dude_mike.js)

[inline absolute linky](ftp://wikis.com/micky.txt)

[global relative linky][relative_linky]

[global absolute linky][absolute_linky]

![inline relative image](mona-lisa.png)

![inline absolute image](http://images.com/mona-lisa.png)

![global relative image][relative_image]

![global absolute image][absolute_image]

[just an anchor](#holdin_it_down)

[relative_linky]: painters/Michelangelo.html
[relative_image]: ./mona-lisa.png
[absolute_linky]: https://www.my-wikis-site.com/peeps/Michelangelo.html
[absolute_image]: https://www.my-photo-site.com/mona-lisa.png
```

## File: `test/functional/makehtml/cases/features/requireSpaceBeforeHeadingText.html`
```html
<h1 id="header">header</h1>
<p>#header</p>
```

## File: `test/functional/makehtml/cases/features/requireSpaceBeforeHeadingText.md`
```markdown
# header

#header
```

## File: `test/functional/makehtml/cases/features/simpleLineBreaks-handle-html-pre.html`
```html
<p>hmm</p>
<pre>
this is `a\_test` and this\_too and finally_this_is
</pre>
```

## File: `test/functional/makehtml/cases/features/simpleLineBreaks-handle-html-pre.md`
```markdown
hmm
<pre>
this is `a\_test` and this\_too and finally_this_is
</pre>
```

## File: `test/functional/makehtml/cases/features/simpleLineBreaks2.html`
```html
<ol>
    <li><p>One</p></li>
    <li><p>Two<br />
        foo</p>
        <p>bar<br />
        bazinga</p>
        <p>nhecos</p></li>
    <li><p>Three</p>
        <ul>
        <li><p>foo</p></li>
        <li><p>bar</p></li></ul></li>
</ol>
   
```

## File: `test/functional/makehtml/cases/features/simpleLineBreaks2.md`
```markdown
 1. One
 2. Two
    foo
    
    bar
    bazinga
    
    
    
    
    nhecos
    
 3. Three
    
    - foo
    
    - bar
   
```

## File: `test/functional/makehtml/cases/features/completeHTMLOutput/simple.html`
```html
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<p>This is a <strong>markdown</strong> file</p>
<p>Converted into a full HTML document</p>
<ul>
<li>this</li>
<li>is</li>
<li>awesome</li>
</ul>
</body>
</html>
```

## File: `test/functional/makehtml/cases/features/completeHTMLOutput/simple.md`
```markdown
This is a **markdown** file

Converted into a full HTML document

 - this
 - is
 - awesome
```

## File: `test/functional/makehtml/cases/features/ellipsis/ellipsis.html`
```html
<p>ellipsis in text...</p>
<p>…</p>
<ol>
    <li>foo...</li>
    <li>bar</li>
</ol>
<blockquote>
    <p>ellipsis in blockquote...</p>
</blockquote>
<pre><code>ellipsis in code...
</code></pre>
<pre><code>ellipsis in code...
</code></pre>
<h1 id="ellipsisinheader">ellipsis in header...</h1>
<p>1...</p>
<ol>
    <li>..</li>
</ol>
<p>1…</p>
<p><a href="https://gitlab.com/gitlab-org/gitlab-ce/compare/v11.5.4...v11.5.5" title="title">Link</a></p>
```

## File: `test/functional/makehtml/cases/features/ellipsis/ellipsis.md`
```markdown
ellipsis in text...

…

1. foo...
2. bar

> ellipsis in blockquote...

```
ellipsis in code...
```

    ellipsis in code...

# ellipsis in header...

1...

1. ..

1…

[Link](https://gitlab.com/gitlab-org/gitlab-ce/compare/v11.5.4...v11.5.5 "title")
```

## File: `test/functional/makehtml/cases/features/emojis/complex.html`
```html
<p>foo🍎bar</p>
<p>foo: apple :bar</p>
<p>:foo 🍎 bar:</p>
```

## File: `test/functional/makehtml/cases/features/emojis/complex.md`
```markdown
foo:apple:bar

foo: apple :bar

:foo :apple: bar:
```

## File: `test/functional/makehtml/cases/features/emojis/links.html`
```html
<p>this link <a href="http://www.example.com/some:apple:url">somelink</a></p>
<p>emoji <a href="http://www.example.com/some:apple:url">🍎</a></p>
<p><a href="http://www.example.com/some:apple:url">🍎</a></p>
<p><a href="http://www.example.com/some:apple:url">🍎</a></p>
```

## File: `test/functional/makehtml/cases/features/emojis/links.md`
```markdown
this link [somelink](http://www.example.com/some:apple:url)

emoji [:apple:](http://www.example.com/some:apple:url)

[:apple:][apple]

[:apple:][]


[apple]: http://www.example.com/some:apple:url
[:apple:]: http://www.example.com/some:apple:url
```

## File: `test/functional/makehtml/cases/features/emojis/simple.html`
```html
<p>🍎 and 💋</p>
<p>💋my🍎</p>
<p>👩‍❤️‍💋‍👨</p>
```

## File: `test/functional/makehtml/cases/features/emojis/simple.md`
```markdown
:apple: and :kiss:

:kiss:my:apple:

:couplekiss_man_woman:
```

## File: `test/functional/makehtml/cases/features/emojis/simplifiedautolinks.html`
```html
<p><a href="http://www.example.com/some:apple:url">http://www.example.com/some:apple:url</a></p>
```

## File: `test/functional/makehtml/cases/features/emojis/simplifiedautolinks.md`
```markdown
http://www.example.com/some:apple:url
```

## File: `test/functional/makehtml/cases/features/emojis/special.html`
```html
<p>this is showdown's emoji <img width="20" height="20" align="absmiddle" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAS1BMVEX///8jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS0jJS3b1q3b1q3b1q3b1q3b1q3b1q3b1q3b1q0565CIAAAAGXRSTlMAQHCAYCCw/+DQwPCQUBAwoHCAEP+wwFBgS2fvBgAAAUZJREFUeAHs1cGy7BAUheFFsEDw/k97VTq3T6ge2EmdM+pvrP6Iwd74XV9Kb52xuMU4/uc1YNgZLFOeV8FGdhGrNk5SEgUyPxAEdj4LlMRDyhVAMVEa2M7TBSeVZAFPdqHgzSZJwPKgcLFLAooHDJo4EDCw4gAtBoJA5UFj4Ng5LOGLwVXZuoIlji/jeQHFk7+baHxrCjeUwB9+s88KndvlhcyBN5BSkYNQIVVb4pV+Npm7hhuKDs/uMP5KxT3WzSNNLIuuoDpMmuAVMruMSeDyQBi24DTr43LAY7ILA1QYaWkgfHzFthYYzg67SQsCbB8GhJUEGCtO9n0rSaCLxgJQjS/JSgMTg2eBDEHAJ+H350AsjYNYscrErgI2e/l+mdR967TCX/v6N0EhPECYCP0i+IAoYQOE8BogNhQMEMdrgAQWHaMAAGi5I5euoY9NAAAAAElFTkSuQmCC"></p>
<p>and this is github's emoji <img width="20" height="20" align="absmiddle" src="https://github.githubassets.com/images/icons/emoji/octocat.png?v8"></p>
```

## File: `test/functional/makehtml/cases/features/emojis/special.md`
```markdown
this is showdown's emoji :showdown:

and this is github's emoji :octocat:
```

## File: `test/functional/makehtml/cases/features/literalMidWordAsterisks/basic.html`
```html
<p>this is a sentence*with*mid asterisks</p>
<p>this is a sentence**with**two mid asterisks</p>
<p>this is a sentence***with***three mid asterisks</p>
<p>this is double*asterisk*mid word with another**asterisk**word</p>
<p>this is double**asterisk**mid word with another**asterisk**word</p>
<p>this is double***asterisk***mid word with another***asterisk***word</p>
<p>this is double*asterisk**mid word with another***asterisk*word</p>
<p>this is double**asterisk*mid word with another***asterisk**word</p>
<p>this is a sentence with just*one asterisk</p>
<p>this is a sentence with just**one asterisk</p>
<p>this is a sentence with just***one asterisk</p>
<p>this is double**asterisk**mid word</p>
<p>this has just**one double asterisk</p>
<p>this has just***one triple asterisk</p>
<p>this <em>should be parsed</em> as emphasis</p>
<p>this <strong>should be parsed</strong> as bold</p>
<p>this <strong><em>should be parsed</em></strong> as bold and emphasis</p>
<p>emphasis at <em>end of sentence</em></p>
<p>bold at <strong>end of sentence</strong></p>
<p>bold and emphasis at <strong><em>end of sentence</em></strong></p>
<p><em>emphasis at</em> line start</p>
<p><strong>bold at</strong> line start</p>
<p><strong><em>bold and emphasis at</em></strong> line start</p>
<p>multi <em>line emphasis
yeah it is</em> yeah</p>
<p>multi <strong>line emphasis
yeah it is</strong> yeah</p>
<p>multi <strong><em>line emphasis
yeah it is</em></strong> yeah</p>
```

## File: `test/functional/makehtml/cases/features/literalMidWordAsterisks/basic.md`
```markdown
this is a sentence*with*mid asterisks

this is a sentence**with**two mid asterisks

this is a sentence***with***three mid asterisks

this is double*asterisk*mid word with another**asterisk**word

this is double**asterisk**mid word with another**asterisk**word

this is double***asterisk***mid word with another***asterisk***word

this is double*asterisk**mid word with another***asterisk*word

this is double**asterisk*mid word with another***asterisk**word

this is a sentence with just*one asterisk

this is a sentence with just**one asterisk

this is a sentence with just***one asterisk

this is double**asterisk**mid word

this has just**one double asterisk

this has just***one triple asterisk

this *should be parsed* as emphasis

this **should be parsed** as bold

this ***should be parsed*** as bold and emphasis

emphasis at *end of sentence*

bold at **end of sentence**

bold and emphasis at ***end of sentence***

*emphasis at* line start

**bold at** line start

***bold and emphasis at*** line start

multi *line emphasis
yeah it is* yeah


multi **line emphasis
yeah it is** yeah


multi ***line emphasis
yeah it is*** yeah
```

## File: `test/functional/makehtml/cases/features/literalMidWordAsterisks/punctation-test.html`
```html
<p><strong>Bold:</strong></p>
<p><strong>Bold</strong></p>
<p><strong>Bold</strong>:</p>
<ul>
    <li><strong>Bold</strong><ul>
        <li>Tier 2</li></ul></li>
</ul>
```

## File: `test/functional/makehtml/cases/features/literalMidWordAsterisks/punctation-test.md`
```markdown
**Bold:**

**Bold**

**Bold**:

- **Bold**
    - Tier 2
```

## File: `test/functional/makehtml/cases/features/literalMidWordUnderscores/basic.html`
```html
<p>some <em>foo</em> yeah</p>
<p>some <strong>foo</strong> yeah</p>
<p>some <strong><em>foo</em></strong> yeah</p>
<p>some word_foo_yeah</p>
<p>some word__foo__yeah</p>
<p>some word___foo___yeah</p>
<p>strippers, <em>hitler</em>, and stalin</p>
<p>strippers, <strong>hitler</strong>, and stalin</p>
<p>strippers, <strong><em>hitler</em></strong>, and stalin</p>
<p><strong><em>multiple</em></strong> italics and bolds in a <strong><em>paragraph</em></strong></p>
<p><strong>multiple</strong> bolds in a <strong>paragraph</strong></p>
<p><em>multiple</em> italics in a <em>paragraph</em></p>
```

## File: `test/functional/makehtml/cases/features/literalMidWordUnderscores/basic.md`
```markdown
some _foo_ yeah

some __foo__ yeah

some ___foo___ yeah

some word_foo_yeah

some word__foo__yeah

some word___foo___yeah

strippers, _hitler_, and stalin

strippers, __hitler__, and stalin

strippers, ___hitler___, and stalin

___multiple___ italics and bolds in a ___paragraph___

__multiple__ bolds in a __paragraph__

_multiple_ italics in a _paragraph_
```

## File: `test/functional/makehtml/cases/features/literalMidWordUnderscores/punctation-test.html`
```html
<p><strong>Bold:</strong></p>
<p><strong>Bold</strong></p>
<p><strong>Bold</strong>:</p>
<ul>
    <li><strong>Bold</strong><ul>
        <li>Tier 2</li></ul></li>
</ul>
```

## File: `test/functional/makehtml/cases/features/literalMidWordUnderscores/punctation-test.md`
```markdown
__Bold:__

__Bold__

__Bold__:

- __Bold__
    - Tier 2
```

## File: `test/functional/makehtml/cases/features/metadata/dashes-conflict.html`
```html
<p><strong>some</strong> markdown text</p>
<ul>
    <li>a list</li>
    <li>another list ---</li>
    <li>and stuff</li>
</ul>
<p>a paragraph --- with dashes</p>
<hr />
```

## File: `test/functional/makehtml/cases/features/metadata/dashes-conflict.md`
```markdown
---

title: This is the document title
language: en
author: Tivie

---
**some** markdown text

 - a list
 - another list ---
 - and stuff

a paragraph --- with dashes

---
```

## File: `test/functional/makehtml/cases/features/metadata/embeded-in-output.html`
```html
<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>This is the document title</title>
    <meta charset="utf-8">
    <meta name="language" content="en">
    <meta name="author" content="Tivie">
    <meta name="contributors" content="John, Mary, Steve">
    <meta name="description" content="This is a long text and so it spans on multiple lines. It must be indented, for showdown to parse it correctly. Markdown **such as bold** is not parsed and it will be rendered as plain text.">
    <meta name="date" content="01-01-2010">
    <meta name="keywords" content="foo, bar, baz">
</head>
<body>
<p><strong>some</strong> markdown text</p>
</body>
</html>
```

## File: `test/functional/makehtml/cases/features/metadata/embeded-in-output.md`
```markdown
«««
title: This is the document title
language: en
author: Tivie
contributors: John, Mary, Steve
description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown **such as bold** is not parsed
    and it will be rendered as plain text.
date: 01-01-2010
keywords: foo, bar, baz
»»»

**some** markdown text
```

## File: `test/functional/makehtml/cases/features/metadata/embeded-two-consecutive-metadata-blocks-different-symbols.html`
```html
<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>This is the document title</title>
    <meta charset="utf-8">
    <meta name="language" content="en">
    <meta name="author" content="Tivie">
    <meta name="contributors" content="John, Mary, Steve">
    <meta name="keywords" content="foo, bar, baz">
</head>
<body>
<hr />
<p>description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown <strong>such as bold</strong> is not parsed
    and it will be rendered as plain text.</p>
<h2 id="date01012010">date: 01-01-2010</h2>
<p><strong>some</strong> markdown text</p>
</body>
</html>
```

## File: `test/functional/makehtml/cases/features/metadata/embeded-two-consecutive-metadata-blocks-different-symbols.md`
```markdown
«««
title: This is the document title
language: en
author: Tivie
contributors: John, Mary, Steve
keywords: foo, bar, baz
»»»
---
description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown **such as bold** is not parsed
    and it will be rendered as plain text.
date: 01-01-2010
---

**some** markdown text
```

## File: `test/functional/makehtml/cases/features/metadata/embeded-two-consecutive-metadata-blocks.html`
```html
<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>This is the document title</title>
    <meta charset="utf-8">
    <meta name="language" content="en">
    <meta name="author" content="Tivie">
    <meta name="contributors" content="John, Mary, Steve">
    <meta name="keywords" content="foo, bar, baz">
</head>
<body>
<hr />
<p>description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown <strong>such as bold</strong> is not parsed
    and it will be rendered as plain text.</p>
<h2 id="date01012010">date: 01-01-2010</h2>
<p><strong>some</strong> markdown text</p>
</body>
</html>
```

## File: `test/functional/makehtml/cases/features/metadata/embeded-two-consecutive-metadata-blocks.md`
```markdown
---
title: This is the document title
language: en
author: Tivie
contributors: John, Mary, Steve
keywords: foo, bar, baz
---
---
description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown **such as bold** is not parsed
    and it will be rendered as plain text.
date: 01-01-2010
---

**some** markdown text
```

## File: `test/functional/makehtml/cases/features/metadata/ignore-metadata.html`
```html
<hr />
<p>title: This is the document title
language: en
author: Tivie
contributors: John, Mary, Steve
description: This is a long text and so it
spans on multiple lines.
It must be indented,
for showdown to parse it correctly.
Markdown <strong>such as bold</strong> is not parsed
and it will be rendered as plain text.
date: 01-01-2010
keywords: foo, bar, baz</p>
<hr />
<p><strong>some</strong> markdown text</p>
```

## File: `test/functional/makehtml/cases/features/metadata/ignore-metadata.md`
```markdown
---

title: This is the document title
language: en
author: Tivie
contributors: John, Mary, Steve
description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown **such as bold** is not parsed
    and it will be rendered as plain text.
date: 01-01-2010
keywords: foo, bar, baz

---

**some** markdown text
```

## File: `test/functional/makehtml/cases/features/metadata/simple-angled-for-method.html`
```html
<p>some <strong>text</strong></p>
```

## File: `test/functional/makehtml/cases/features/metadata/simple-angled-for-method.md`
```markdown
«««
foo: bar
baz: bazinga
»»»

some **text**
```

## File: `test/functional/makehtml/cases/features/metadata/simple-angled-quotes.html`
```html
<p><strong>some</strong> markdown text</p>
```

## File: `test/functional/makehtml/cases/features/metadata/simple-angled-quotes.md`
```markdown
«««
title: This is the document title
language: en
author: Tivie
contributors: John, Mary, Steve
description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown **such as bold** is not parsed
    and it will be rendered as plain text.
date: 01-01-2010
keywords: foo, bar, baz
»»»

**some** markdown text
```

## File: `test/functional/makehtml/cases/features/metadata/simple-three-dashes.html`
```html
<p><strong>some</strong> markdown text</p>
```

## File: `test/functional/makehtml/cases/features/metadata/simple-three-dashes.md`
```markdown
---
title: This is the document title
language: en
author: Tivie
contributors: John, Mary, Steve
description: This is a long text and so it
    spans on multiple lines.
    It must be indented,
    for showdown to parse it correctly.
    Markdown **such as bold** is not parsed
    and it will be rendered as plain text.
date: 01-01-2010
keywords: foo, bar, baz
---

**some** markdown text
```

## File: `test/functional/makehtml/cases/features/metadata/simple-with-format.html`
```html
<p><strong>some</strong> markdown text</p>
```

## File: `test/functional/makehtml/cases/features/metadata/simple-with-format.md`
```markdown
---YAML
foo: bar
baz:
 - bazinga
 - bling
 - blang
---

**some** markdown text
```

## File: `test/functional/makehtml/cases/features/moreStyling/tasklists-with-styling.html`
```html
<ul>
    <li class="task-list-item" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;"> test</li>
    <li class="task-list-item task-list-item-complete" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;" checked> testing complete</li>
</ul>
```

## File: `test/functional/makehtml/cases/features/moreStyling/tasklists-with-styling.md`
```markdown
- [ ] test
- [x] testing complete
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/hash-links-open-in-same-page.html`
```html
<p>this link is in the <a href="#same-page">same page</a></p>
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/hash-links-open-in-same-page.md`
```markdown
this link is in the [same page](#same-page)
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/simple-cases.html`
```html
<p><a href="www.google.com" rel="noopener noreferrer" target="_blank">foo</a></p>
<p>a link <a href="http://www.google.com" rel="noopener noreferrer" target="_blank">http://www.google.com</a></p>
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/simple-cases.md`
```markdown
[foo](www.google.com)

a link <http://www.google.com>
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/simple.html`
```html
<p><a href="www.google.com" rel="noopener noreferrer" target="_blank">foo</a></p>
<p>a link <a href="http://www.google.com" rel="noopener noreferrer" target="_blank">http://www.google.com</a></p>
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/simple.md`
```markdown
[foo](www.google.com)

a link <http://www.google.com>
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/simplifiedAutoLink.html`
```html
<p>this is <a href="http://www.google.com" rel="noopener noreferrer" target="_blank">http://www.google.com</a> autolink</p>
```

## File: `test/functional/makehtml/cases/features/openLinksInNewWindow/simplifiedAutoLink.md`
```markdown
this is http://www.google.com autolink
```

## File: `test/functional/makehtml/cases/features/rawHeaderId/simple.html`
```html
<h1 id="123-my#very/-strange-\header*`^ªº-_.,-yeah">123 My#very/ strange \header*`^ªº-_., yeah</h1>
```

## File: `test/functional/makehtml/cases/features/rawHeaderId/simple.md`
```markdown
# 123 My#very/ strange \header*`^ªº-_., yeah
```

## File: `test/functional/makehtml/cases/features/rawHeaderId/with-prefixHeaderId.html`
```html
<h1 id="/prefix/some-header">some header</h1>
<h1 id="/prefix/another-!-#$%&/()=?»@£§{[]}«--header">another !"#$%&amp;/()=?»@£§{[]}«' header</h1>
```

## File: `test/functional/makehtml/cases/features/rawHeaderId/with-prefixHeaderId.md`
```markdown
# some header

# another !"#$%&/()=?»@£§{[]}«' header
```

## File: `test/functional/makehtml/cases/features/rawPrefixHeaderId/simple-with-prefixHeaderId.html`
```html
<h1 id="/prefix/someheaderfoo">some header &amp;/) foo</h1>
```

## File: `test/functional/makehtml/cases/features/rawPrefixHeaderId/simple-with-prefixHeaderId.md`
```markdown
# some header &/) foo
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/autolinks-with-magic-chars.html`
```html
<p><a href="http://www.foobar.com/blegh#**foobar**bazinga">http://www.foobar.com/blegh#**foobar**bazinga</a></p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/autolinks-with-magic-chars.md`
```markdown
http://www.foobar.com/blegh#**foobar**bazinga
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/blockquote.html`
```html
<blockquote>
    <p><a href="http://www.google.com">http://www.google.com</a></p>
</blockquote>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/blockquote.md`
```markdown
> http://www.google.com
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/codespans.html`
```html
<p><code>http://www.gmail.com</code></p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/codespans.md`
```markdown
`http://www.gmail.com`
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/complete-test-case.html`
```html
<!-- SHOULD PASS -->
<p><a href="http://foo.com/blah_blah">http://foo.com/blah_blah</a></p>
<p><a href="http://foo.com/blah_blah/">http://foo.com/blah_blah/</a></p>
<p><a href="http://foo.com/blah_blah_(wikipedia)">http://foo.com/blah_blah_(wikipedia)</a></p>
<p><a href="http://foo.com/blah_blah_(wikipedia)_(again)">http://foo.com/blah_blah_(wikipedia)_(again)</a></p>
<p><a href="http://www.example.com/wpstyle/?p=364">http://www.example.com/wpstyle/?p=364</a></p>
<p><a href="https://www.example.com/foo/?bar=baz&inga=42&quux">https://www.example.com/foo/?bar=baz&inga=42&quux</a></p>
<p><a href="http://✪df.ws/123">http://✪df.ws/123</a></p>
<p><a href="http://userid:password@example.com:8080">http://userid:password@example.com:8080</a></p>
<p><a href="http://userid:password@example.com:8080/">http://userid:password@example.com:8080/</a></p>
<p><a href="http://userid@example.com">http://userid@example.com</a></p>
<p><a href="http://userid@example.com/">http://userid@example.com/</a></p>
<p><a href="http://userid@example.com:8080">http://userid@example.com:8080</a></p>
<p><a href="http://userid@example.com:8080/">http://userid@example.com:8080/</a></p>
<p><a href="http://userid:password@example.com">http://userid:password@example.com</a></p>
<p><a href="http://userid:password@example.com/">http://userid:password@example.com/</a></p>
<p><a href="http://142.42.1.1/">http://142.42.1.1/</a></p>
<p><a href="http://142.42.1.1:8080/">http://142.42.1.1:8080/</a></p>
<p><a href="http://➡.ws/䨹">http://➡.ws/䨹</a></p>
<p><a href="http://⌘.ws">http://⌘.ws</a></p>
<p><a href="http://⌘.ws/">http://⌘.ws/</a></p>
<p><a href="http://foo.com/blah_(wikipedia)#cite-1">http://foo.com/blah_(wikipedia)#cite-1</a></p>
<p><a href="http://foo.com/blah_(wikipedia)_blah#cite-1">http://foo.com/blah_(wikipedia)_blah#cite-1</a></p>
<p><a href="http://foo.com/unicode_(✪)_in_parens">http://foo.com/unicode_(✪)_in_parens</a></p>
<p><a href="http://foo.com/(something)?after=parens">http://foo.com/(something)?after=parens</a></p>
<p><a href="http://☺.damowmow.com/">http://☺.damowmow.com/</a></p>
<p><a href="http://code.google.com/events/#&product=browser">http://code.google.com/events/#&product=browser</a></p>
<p><a href="http://j.mp">http://j.mp</a></p>
<p><a href="ftp://foo.bar/baz">ftp://foo.bar/baz</a></p>
<p><a href="http://foo.bar/?q=Test%20URL-encoded%20stuff">http://foo.bar/?q=Test%20URL-encoded%20stuff</a></p>
<!-- http://مثال.إختبار -->
<!-- http://例子.测试 -->
<!-- http://उदाहरण.परीक्षा -->
<p><a href="http://1337.net">http://1337.net</a></p>
<p><a href="http://a.b-c.de">http://a.b-c.de</a></p>
<p><a href="http://223.255.255.254">http://223.255.255.254</a></p>
<p><a href="https://foo_bar.example.com/">https://foo_bar.example.com/</a></p>
<!-- WEIRD BUT SHOULD ALSO PASS -->
<p><a href="http://www.foo.bar./">http://www.foo.bar./</a></p>
<p><a href="http://a.b--c.de/">http://a.b--c.de/</a></p>
<!-- SHOULD PARTIALLY PASS -->
<p><a href="http://foo.bar/foo(bar)baz">http://foo.bar/foo(bar)baz</a> quux</p>
<p><a href="http://foo.bar?q=Spaces">http://foo.bar?q=Spaces</a> should be encoded</p>
<p>http://.<a href="http://www.foo.bar/">www.foo.bar/</a></p>
<p>http://.<a href="http://www.foo.bar./">www.foo.bar./</a></p>
<!-- THESE ARE INVALID IPS BUT WE WILL LET THEM PASS -->
<p><a href="http://10.1.1.1">http://10.1.1.1</a></p>
<p><a href="http://10.1.1.254">http://10.1.1.254</a></p>
<p><a href="http://0.0.0.0">http://0.0.0.0</a></p>
<p><a href="http://10.1.1.0">http://10.1.1.0</a></p>
<p><a href="http://10.1.1.255">http://10.1.1.255</a></p>
<p><a href="http://224.1.1.1">http://224.1.1.1</a></p>
<p><a href="http://1.1.1.1.1">http://1.1.1.1.1</a></p>
<p><a href="http://123.123.123">http://123.123.123</a></p>
<!-- SHOULD FAIL -->
<p>http://</p>
<p>http://.</p>
<p>http://..</p>
<p>http://../</p>
<p>http://?</p>
<p>http://??</p>
<p>http://??/</p>
<p>http://#</p>
<p>http://##</p>
<p>http://##/</p>
<p>//</p>
<p>//a</p>
<p>///a</p>
<p>///</p>
<p>http:///a</p>
<p>foo.com</p>
<p>rdar://1234</p>
<p>h://test</p>
<p>http:// shouldfail.com</p>
<p>:// should fail</p>
<p>http://-error-.invalid/</p>
<p>http://-a.b.co</p>
<p>http://3628126748</p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/complete-test-case.md`
```markdown
<!-- SHOULD PASS -->

http://foo.com/blah_blah

http://foo.com/blah_blah/

http://foo.com/blah_blah_(wikipedia)

http://foo.com/blah_blah_(wikipedia)_(again)

http://www.example.com/wpstyle/?p=364

https://www.example.com/foo/?bar=baz&inga=42&quux

http://✪df.ws/123

http://userid:password@example.com:8080

http://userid:password@example.com:8080/

http://userid@example.com

http://userid@example.com/

http://userid@example.com:8080

http://userid@example.com:8080/

http://userid:password@example.com

http://userid:password@example.com/

http://142.42.1.1/

http://142.42.1.1:8080/

http://➡.ws/䨹

http://⌘.ws

http://⌘.ws/

http://foo.com/blah_(wikipedia)#cite-1

http://foo.com/blah_(wikipedia)_blah#cite-1

http://foo.com/unicode_(✪)_in_parens

http://foo.com/(something)?after=parens

http://☺.damowmow.com/

http://code.google.com/events/#&product=browser

http://j.mp

ftp://foo.bar/baz

http://foo.bar/?q=Test%20URL-encoded%20stuff

<!-- http://مثال.إختبار -->

<!-- http://例子.测试 -->

<!-- http://उदाहरण.परीक्षा -->

http://1337.net

http://a.b-c.de

http://223.255.255.254

https://foo_bar.example.com/

<!-- WEIRD BUT SHOULD ALSO PASS -->

http://www.foo.bar./

http://a.b--c.de/

<!-- SHOULD PARTIALLY PASS -->

http://foo.bar/foo(bar)baz quux

http://foo.bar?q=Spaces should be encoded

http://.www.foo.bar/

http://.www.foo.bar./

<!-- THESE ARE INVALID IPS BUT WE WILL LET THEM PASS -->
http://10.1.1.1

http://10.1.1.254

http://0.0.0.0

http://10.1.1.0

http://10.1.1.255

http://224.1.1.1

http://1.1.1.1.1

http://123.123.123


<!-- SHOULD FAIL -->

http://

http://.

http://..

http://../

http://?

http://??

http://??/

http://#

http://##

http://##/

//

//a

///a

///

http:///a

foo.com

rdar://1234

h://test

http:// shouldfail.com

:// should fail

http://-error-.invalid/

http://-a.b.co

http://3628126748
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/disallow-underscores.html`
```html
<p><a href="http://en.wikipedia.org/wiki/Tourism_in_Germany">http://en.wikipedia.org/wiki/Tourism_in_Germany</a></p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/disallow-underscores.md`
```markdown
http://en.wikipedia.org/wiki/Tourism_in_Germany
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/does-not-parse-inside-a-tags.html`
```html
<p><a href="http://www.google.com">www.google.com</a></p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/does-not-parse-inside-a-tags.md`
```markdown
<a href="http://www.google.com">www.google.com</a>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/does-not-parse-inside-code.html`
```html
<pre><code>some code with
a link
www.google.com

and another link http://www.google.com
</code></pre>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/does-not-parse-inside-code.md`
```markdown
    some code with
    a link
    www.google.com
    
    and another link http://www.google.com
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/does-not-parse-reference-links.html`
```html
<p><img src="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png" alt="Showdown" /></p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/does-not-parse-reference-links.md`
```markdown
![Showdown][sd-logo]

[sd-logo]: https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/emphasis-and-strikethrough.html`
```html
<p><em><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></em></p>
<p><strong><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></strong></p>
<p><strong><em><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></em></strong></p>
<p><del><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></del></p>
<p><em><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></em></p>
<p><strong><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></strong></p>
<p><strong><em><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></em></strong></p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/emphasis-and-strikethrough.md`
```markdown
*http://www.google.com/foobar*

**http://www.google.com/foobar**

***http://www.google.com/foobar***

~~http://www.google.com/foobar~~

_http://www.google.com/foobar_

__http://www.google.com/foobar__

___http://www.google.com/foobar___
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/ordered-lists.html`
```html
<ol>
    <li><a href="http://www.google.com/listitem1">http://www.google.com/listitem1</a></li>
    <li><a href="http://www.google.com/listitem2">http://www.google.com/listitem2</a></li>
    <li><a href="http://www.google.com/listitem3">http://www.google.com/listitem3</a></li>
</ol>
<p>foo</p>
<ol>
    <li><p><a href="http://www.google.com/listitem1">http://www.google.com/listitem1</a></p></li>
    <li><p><a href="http://www.google.com/listitem2">http://www.google.com/listitem2</a></p></li>
    <li><p><a href="http://www.google.com/listitem3">http://www.google.com/listitem3</a></p></li>
</ol>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/ordered-lists.md`
```markdown
1. http://www.google.com/listitem1
2. http://www.google.com/listitem2
3. http://www.google.com/listitem3

foo

1. http://www.google.com/listitem1

2. http://www.google.com/listitem2

3. http://www.google.com/listitem3
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/text.html`
```html
<p><a href="http://www.google.com/foobar">http://www.google.com/foobar</a></p>
<p><a href="http://www.google.com/foobar">www.google.com/foobar</a></p>
<p><a href="ftp://user:password@host.com:port/path">ftp://user:password@host.com:port/path</a></p>
<p>this has some <a href="http://www.google.com/foobar">http://www.google.com/foobar</a> in text</p>
<p>this has some <a href="http://www.google.com/foobar">www.google.com/foobar</a> in text</p>
<p>this has some <a href="ftp://user:password@host.com:port/path">ftp://user:password@host.com:port/path</a> in text</p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/text.md`
```markdown
http://www.google.com/foobar

www.google.com/foobar

ftp://user:password@host.com:port/path

this has some http://www.google.com/foobar in text

this has some www.google.com/foobar in text

this has some ftp://user:password@host.com:port/path in text


```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/trailing-punctuation.html`
```html
<p><a href="http://www.google.com">http://www.google.com</a>!</p>
<p><a href="http://www.google.com">http://www.google.com</a>!!!!!!!!!!!!!!!!</p>
<p><a href="http://www.google.com/!!!!!!!!!!!!!!!!foobar">http://www.google.com/!!!!!!!!!!!!!!!!foobar</a></p>
<p><a href="http://www.google.com/">http://www.google.com/</a>!!!!!!!!!!!!!!!! foobar</p>
<p>(<a href="http://www.google.com/">http://www.google.com/</a>?!.)</p>
<p><a href="http://www.google.com/?!.(">http://www.google.com/?!.(</a></p>
<p><a href="http://www.google.com/a()">http://www.google.com/a()</a></p>
<p><a href="http://www.google.com/a?!.()">http://www.google.com/a?!.()</a></p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/trailing-punctuation.md`
```markdown
http://www.google.com!

http://www.google.com!!!!!!!!!!!!!!!!

http://www.google.com/!!!!!!!!!!!!!!!!foobar

http://www.google.com/!!!!!!!!!!!!!!!! foobar

(http://www.google.com/?!.)

http://www.google.com/?!.(

http://www.google.com/a()

http://www.google.com/a?!.()
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/unordered-lists.html`
```html
<ul>
 <li><a href="http://www.google.com/foo">http://www.google.com/foo</a></li>
 <li><a href="http://www.google.com/bar">http://www.google.com/bar</a></li>
 <li><a href="http://www.google.com/baz">http://www.google.com/baz</a></li>
</ul>
<p>a</p>
<ul>
 <li><p><a href="http://www.google.com/foo">http://www.google.com/foo</a></p></li>
 <li><p><a href="http://www.google.com/bar">http://www.google.com/bar</a></p></li>
 <li><p><a href="http://www.google.com/baz">http://www.google.com/baz</a></p></li>
</ul>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/unordered-lists.md`
```markdown
 - http://www.google.com/foo
 - http://www.google.com/bar
 - http://www.google.com/baz

a

 - http://www.google.com/foo

 - http://www.google.com/bar

 - http://www.google.com/baz
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/wrapping-parenthesis.html`
```html
<p>(<a href="https://www.google.com">https://www.google.com</a>)</p>
<p>(<a href="https://www.google.com">https://www.google.com</a>!?;)</p>
```

## File: `test/functional/makehtml/cases/features/simplifiedAutoLink/wrapping-parenthesis.md`
```markdown
(https://www.google.com)

(https://www.google.com!?;)


```

## File: `test/functional/makehtml/cases/features/splitAdjacentBlockquotes/basic.html`
```html
<blockquote>
    <h1 id="blockquote1">Block quote  1</h1>
    <p>This is my first block quote.</p>
</blockquote>
<blockquote>
    <h1 id="blockquote2">Block quote 2</h1>
    <p>This is my second block quote.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/features/splitAdjacentBlockquotes/basic.md`
```markdown
> # Block quote  1
>
> This is my first block quote.

> # Block quote 2
>
> This is my second block quote.
```

## File: `test/functional/makehtml/cases/features/splitAdjacentBlockquotes/multiline-paragraph.html`
```html
<blockquote>
<p>This is my second block quote
yeah
everythong is ok.</p>
</blockquote>
<p>This is not a blockquote</p>
```

## File: `test/functional/makehtml/cases/features/splitAdjacentBlockquotes/multiline-paragraph.md`
```markdown
> This is my second block quote
yeah
everythong is ok.

This is not a blockquote
```

## File: `test/functional/makehtml/cases/features/tables/#179.parse-md-in-table-ths.html`
```html
<table>
  <thead>
    <tr>
      <th><em>foo</em></th>
      <th><strong>bar</strong></th>
      <th><del>baz</del></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>100</td>
      <td>blabla</td>
      <td>aaa</td>
    </tr>
  </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/#179.parse-md-in-table-ths.md`
```markdown
| *foo* | **bar** | ~~baz~~ |
|-------|---------|---------|
| 100   | blabla  |  aaa    |
```

## File: `test/functional/makehtml/cases/features/tables/#256.table-header-separators-should-not-require-3-dashes.html`
```html
<table>
    <thead>
    <tr>
        <th>key</th>
        <th>value</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>My Key</td>
        <td>My Value</td>
    </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/#256.table-header-separators-should-not-require-3-dashes.md`
```markdown
|key|value|
|--|--| 
|My Key|My Value|
```

## File: `test/functional/makehtml/cases/features/tables/#345.escape-pipe-character.html`
```html
<table>
    <thead>
    <tr>
        <th>Operator</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>&amp;</td>
        <td>Logical AND</td>
    </tr>
    <tr>
        <td>&amp;&amp;</td>
        <td>Shortcut AND</td>
    </tr>
    <tr>
        <td>|</td>
        <td>Logical OR</td>
    </tr>
    <tr>
        <td>||</td>
        <td>Shortcut OR</td>
    </tr>
    <tr>
        <td>^</td>
        <td>Logical XOR</td>
    </tr>
  </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/#345.escape-pipe-character.md`
```markdown
| Operator | Description |
|----------|-------------|
| & | Logical AND |
| && | Shortcut AND |
| \| | Logical OR |
| \|\| | Shortcut OR |
| ^ | Logical XOR |
```

## File: `test/functional/makehtml/cases/features/tables/#406.does-not-render-one-column-tables.html`
```html
<table>
    <thead>
    <tr>
        <th>some header</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>some content</td>
    </tr>
    </tbody>
</table>
<table>
    <thead>
    <tr>
        <th>some header</th>
    </tr>
    </thead>
    <tbody>
    </tbody>
</table>
<table>
    <thead>
    <tr>
        <th>some header</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>some content</td>
    </tr>
    <tr>
        <td>some content</td>
    </tr>
    <tr>
        <td>some content</td>
    </tr>
    <tr>
        <td>some content</td>
    </tr>
    <tr>
        <td>some content</td>
    </tr>
    </tbody>
</table>
<table>
    <thead>
    <tr>
        <th style="text-align:left;">some header</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align:left;">some content</td>
    </tr>
    </tbody>
</table>
<table>
    <thead>
    <tr>
        <th style="text-align:right;">some header</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align:right;">some content</td>
    </tr>
    </tbody>
</table>
<table>
    <thead>
    <tr>
        <th style="text-align:center;">some header</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align:center;">some content</td>
    </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/#406.does-not-render-one-column-tables.md`
```markdown
|some header |
|------------|
|some content|

|some header |
|------------|

|some header |
|------------|
|some content|
|some content|
|some content|
|some content|
|some content|

|some header |
|:-----------|
|some content|

|some header |
|-----------:|
|some content|

|some header |
|:----------:|
|some content|
```

## File: `test/functional/makehtml/cases/features/tables/#442.trailing-spaces-break-one-column-tables.html`
```html
<table>
    <thead>
    <tr>
        <th style="text-align:left;">Single column</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align:left;">Row one</td>
    </tr>
    <tr>
        <td style="text-align:left;">Row two</td>
    </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/#442.trailing-spaces-break-one-column-tables.md`
```markdown
| Single column |  
|:--------------|   
|    Row one    |                                      
|    Row two    |               
```

## File: `test/functional/makehtml/cases/features/tables/#443.2.table-followed-by-list-does-not-parse-correctly.html`
```html
<table>
    <thead>
    <tr>
        <th>Tables</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><strong>col 3 is</strong></td>
    </tr>
    <tr>
        <td>col 2 is</td>
    </tr>
    <tr>
        <td>zebra stripes</td>
    </tr>
    </tbody>
</table>
<ol>
    <li>test</li>
</ol>
```

## File: `test/functional/makehtml/cases/features/tables/#443.2.table-followed-by-list-does-not-parse-correctly.md`
```markdown
| Tables        |
| ------------- |
| **col 3 is**  |
| col 2 is      |
| zebra stripes |

1. test
```

## File: `test/functional/makehtml/cases/features/tables/#443.table-followed-by-list-does-not-parse-correctly.html`
```html
<table>
<thead>
<tr>
    <th>Tables</th>
    <th style="text-align:center;">Are</th>
    <th style="text-align:right;">Cool</th>
</tr>
</thead>
<tbody>
<tr>
    <td><strong>col 3 is</strong></td>
    <td style="text-align:center;">right-aligned</td>
    <td style="text-align:right;">$1600</td>
</tr>
<tr>
    <td>col 2 is</td>
    <td style="text-align:center;"><em>centered</em></td>
    <td style="text-align:right;">$12</td>
</tr>
<tr>
    <td>zebra stripes</td>
    <td style="text-align:center;">are neat</td>
    <td style="text-align:right;">$1</td>
</tr>
</tbody>
</table>
<ol>
    <li>test</li>
</ol>
```

## File: `test/functional/makehtml/cases/features/tables/#443.table-followed-by-list-does-not-parse-correctly.md`
```markdown
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| **col 3 is**  | right-aligned | $1600 |
| col 2 is      | *centered*    |   $12 |
| zebra stripes | are neat      |    $1 |

1. test
```

## File: `test/functional/makehtml/cases/features/tables/#465.code-spans-with-pipes-break-table.html`
```html
<table>
    <thead>
    <tr>
        <th>PowerShell command</th>
        <th>Example</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Get-Service</td>
        <td><code>Get-Service | Stop-Service -WhatIf</code></td>
    </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/#465.code-spans-with-pipes-break-table.md`
```markdown
|PowerShell command|Example|
|--|--|
|Get-Service|`Get-Service | Stop-Service -WhatIf`|
```

## File: `test/functional/makehtml/cases/features/tables/#471.ol-is-not-rendered-correctly-inside-table.html`
```html
<table>
    <thead>
    <tr>
        <th style="text-align:right;">h1</th>
        <th style="text-align:left;">h2</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align:right;">asdf</td>
        <td style="text-align:left;">one <code>two &lt;ol&gt; three</code></td>
    </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/#471.ol-is-not-rendered-correctly-inside-table.md`
```markdown
|  h1     |  h2                  |
|--------:|:---------------------|
| asdf    | one `two <ol> three` |
```

## File: `test/functional/makehtml/cases/features/tables/basic-alignment.html`
```html
<table>
  <thead>
    <tr>
      <th style="text-align:left;">First Header</th>
      <th style="text-align:left;">Second Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left;">Row 1 Cell 1</td>
      <td style="text-align:left;">Row 1 Cell 2</td>
    </tr>
    <tr>
      <td style="text-align:left;">Row 2 Cell 1</td>
      <td style="text-align:left;">Row 2 Cell 2</td>
    </tr>
  </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/basic-alignment.md`
```markdown
| First Header  | Second Header |
| :------------ | :------------ |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
```

## File: `test/functional/makehtml/cases/features/tables/basic-with-header-ids.html`
```html
<table>
    <thead>
        <tr>
            <th id="first_header">First Header</th>
            <th id="second_header">Second Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 Cell 1</td>
            <td>Row 1 Cell 2</td>
        </tr>
        <tr>
            <td>Row 2 Cell 1</td>
            <td>Row 2 Cell 2</td>
        </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/basic-with-header-ids.md`
```markdown
| First Header  | Second Header |
| ------------- | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
```

## File: `test/functional/makehtml/cases/features/tables/basic.html`
```html
<table>
    <thead>
        <tr>
            <th>First Header</th>
            <th>Second Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 Cell 1</td>
            <td>Row 1 Cell 2</td>
        </tr>
        <tr>
            <td>Row 2 Cell 1</td>
            <td>Row 2 Cell 2</td>
        </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/basic.md`
```markdown
| First Header  | Second Header |
| ------------- | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
```

## File: `test/functional/makehtml/cases/features/tables/gh-style-tables.html`
```html
<table>
    <thead>
        <tr>
            <th>First Header</th>
            <th>Second Header</th>
            <th>Third Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Content Cell</td>
            <td>Content Cell</td>
            <td>C</td>
        </tr>
        <tr>
            <td>Content Cell</td>
            <td>Content Cell</td>
            <td>C</td>
        </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/gh-style-tables.md`
```markdown
First Header  | Second Header|Third Header
------------- | -------------|---
Content Cell  | Content Cell|C
Content Cell  | Content Cell|C
```

## File: `test/functional/makehtml/cases/features/tables/large-table-with-allignments.html`
```html
<table>
    <thead>
        <tr>
            <th style="text-align:left;">First Header</th>
            <th style="text-align:center;">Second Header</th>
            <th style="text-align:right;">Third Header</th>
            <th>Fourth Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left;">Row 1 Cell 1</td>
            <td style="text-align:center;">Row 1 Cell 2</td>
            <td style="text-align:right;">Row 1 Cell 3</td>
            <td>Row 1 Cell 4</td>
        </tr>
        <tr>
            <td style="text-align:left;">Row 2 Cell 1</td>
            <td style="text-align:center;">Row 2 Cell 2</td>
            <td style="text-align:right;">Row 2 Cell 3</td>
            <td>Row 2 Cell 4</td>
        </tr>
        <tr>
            <td style="text-align:left;">Row 3 Cell 1</td>
            <td style="text-align:center;">Row 3 Cell 2</td>
            <td style="text-align:right;">Row 3 Cell 3</td>
            <td>Row 3 Cell 4</td>
        </tr>
        <tr>
            <td style="text-align:left;">Row 4 Cell 1</td>
            <td style="text-align:center;">Row 4 Cell 2</td>
            <td style="text-align:right;">Row 4 Cell 3</td>
            <td>Row 4 Cell 4</td>
        </tr>
        <tr>
            <td style="text-align:left;">Row 5 Cell 1</td>
            <td style="text-align:center;">Row 5 Cell 2</td>
            <td style="text-align:right;">Row 5 Cell 3</td>
            <td>Row 5 Cell 4</td>
        </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/large-table-with-allignments.md`
```markdown
| First Header  | Second Header | Third Header  | Fourth Header |
| :------------ |: ----------- :| ------------ :| ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  | Row 1 Cell 3  | Row 1 Cell 4  |
| Row 2 Cell 1  | Row 2 Cell 2  | Row 2 Cell 3  | Row 2 Cell 4  |
| Row 3 Cell 1  | Row 3 Cell 2  | Row 3 Cell 3  | Row 3 Cell 4  |
| Row 4 Cell 1  | Row 4 Cell 2  | Row 4 Cell 3  | Row 4 Cell 4  |
| Row 5 Cell 1  | Row 5 Cell 2  | Row 5 Cell 3  | Row 5 Cell 4  |
```

## File: `test/functional/makehtml/cases/features/tables/large.html`
```html
<table>
    <thead>
        <tr>
            <th>First Header</th>
            <th>Second Header</th>
            <th>Third Header</th>
            <th>Fourth Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 Cell 1</td>
            <td>Row 1 Cell 2</td>
            <td>Row 1 Cell 3</td>
            <td>Row 1 Cell 4</td>
        </tr>
        <tr>
            <td>Row 2 Cell 1</td>
            <td>Row 2 Cell 2</td>
            <td>Row 2 Cell 3</td>
            <td>Row 2 Cell 4</td>
        </tr>
        <tr>
            <td>Row 3 Cell 1</td>
            <td>Row 3 Cell 2</td>
            <td>Row 3 Cell 3</td>
            <td>Row 3 Cell 4</td>
        </tr>
        <tr>
            <td>Row 4 Cell 1</td>
            <td>Row 4 Cell 2</td>
            <td>Row 4 Cell 3</td>
            <td>Row 4 Cell 4</td>
        </tr>
        <tr>
            <td>Row 5 Cell 1</td>
            <td>Row 5 Cell 2</td>
            <td>Row 5 Cell 3</td>
            <td>Row 5 Cell 4</td>
        </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/large.md`
```markdown
| First Header  | Second Header | Third Header  | Fourth Header |
| ------------- | ------------- | ------------  | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  | Row 1 Cell 3  | Row 1 Cell 4  |
| Row 2 Cell 1  | Row 2 Cell 2  | Row 2 Cell 3  | Row 2 Cell 4  |
| Row 3 Cell 1  | Row 3 Cell 2  | Row 3 Cell 3  | Row 3 Cell 4  |
| Row 4 Cell 1  | Row 4 Cell 2  | Row 4 Cell 3  | Row 4 Cell 4  |
| Row 5 Cell 1  | Row 5 Cell 2  | Row 5 Cell 3  | Row 5 Cell 4  |
```

## File: `test/functional/makehtml/cases/features/tables/mixed-alignment.html`
```html
<table>
  <thead>
    <tr>
      <th style="text-align:left;">Left-Aligned</th>
      <th style="text-align:center;">Center-Aligned</th>
      <th style="text-align:right;">Right-Aligned</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left;">col 3 is</td>
      <td style="text-align:center;">some wordy paragraph</td>
      <td style="text-align:right;">$1600</td>
    </tr>
    <tr>
      <td style="text-align:left;">col 2 is</td>
      <td style="text-align:center;">centered</td>
      <td style="text-align:right;">$12</td>
    </tr>
    <tr>
      <td style="text-align:left;">zebra stripes</td>
      <td style="text-align:center;">are neat</td>
      <td style="text-align:right;">$1</td>
    </tr>
  </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/mixed-alignment.md`
```markdown
| Left-Aligned  |    Center-Aligned    | Right-Aligned |
| :------------ |:--------------------:| -------------:|
| col 3 is      | some wordy paragraph |         $1600 |
| col 2 is      |       centered       |           $12 |
| zebra stripes |       are neat       |            $1 |
```

## File: `test/functional/makehtml/cases/features/tables/multiple-tables.html`
```html
<h1 id="tabletest">Table Test</h1>
<h2 id="section1">section 1</h2>
<table>
    <thead>
        <tr>
            <th>header1</th>
            <th>header2</th>
            <th>header3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Value1</td>
            <td>Value2</td>
            <td>Value3</td>
        </tr>
    </tbody>
</table>
<h2 id="section2">section 2</h2>
<table>
    <thead>
        <tr>
            <th>headerA</th>
            <th>headerB</th>
            <th>headerC</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ValueA</td>
            <td>ValueB</td>
            <td>ValueC</td>
        </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/multiple-tables.md`
```markdown
Table Test
============

section 1
------------

|header1    |header2    |header3|
|-----------|-----------|---------|
|Value1     |Value2     |Value3   |


section 2
-----------

|headerA    |headerB    |headerC|
|-----------|-----------|---------|
|ValueA     |ValueB     |ValueC   |
```

## File: `test/functional/makehtml/cases/features/tables/table-inside-codeblock.html`
```html
<p>some text</p>
<pre><code>| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| **col 3 is**  | right-aligned | $1600 |
| col 2 is      | *centered*    |   $12 |
| zebra stripes | ~~are neat~~  |    $1 |
</code></pre>
```

## File: `test/functional/makehtml/cases/features/tables/table-inside-codeblock.md`
```markdown
some text


    | Tables        | Are           | Cool  |
    | ------------- |:-------------:| -----:|
    | **col 3 is**  | right-aligned | $1600 |
    | col 2 is      | *centered*    |   $12 |
    | zebra stripes | ~~are neat~~  |    $1 |
```

## File: `test/functional/makehtml/cases/features/tables/table-without-leading-pipe.html`
```html

<h3 id="stats">Stats</h3>
<table>
<thead>
<tr>
<th>Status</th>
<th>AGENT1</th>
<th>AGENT2</th>
<th>AGENT3</th>
<th>AGENT4</th>
<th>AGENT5</th>
<th>AGENT6</th>
<th>AGENT7</th>
<th>AGENT8</th>
<th>AGENT9</th>
<th>TOTAL</th>
</tr>
</thead>
<tbody>
<tr>
<td>AGENT ERROR</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td></td>
</tr>
<tr>
<td>APPROVED</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td></td>
</tr>
</tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/table-without-leading-pipe.md`
```markdown

### Stats


Status | AGENT1 | AGENT2 | AGENT3 | AGENT4 | AGENT5 | AGENT6 | AGENT7 | AGENT8 | AGENT9 | TOTAL |
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AGENT ERROR | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
APPROVED | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
```

## File: `test/functional/makehtml/cases/features/tables/with-equals.html`
```html
<table>
    <thead>
        <tr>
            <th>First Header</th>
            <th>Second Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 Cell 1</td>
            <td>Row 1 Cell 2</td>
        </tr>
        <tr>
            <td>Row 2 Cell 1</td>
            <td>Row 2 Cell 2</td>
        </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/with-equals.md`
```markdown
| First Header  | Second Header |
| ============= | ============= |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |
```

## File: `test/functional/makehtml/cases/features/tables/with-span-elements.html`
```html
<table>
    <thead>
    <tr>
        <th>First Header</th>
        <th>Second Header</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><strong>bold</strong></td>
        <td><img src="foo.jpg" alt="img" /></td>
    </tr>
    <tr>
        <td><em>italic</em></td>
        <td><a href="bla.html">link</a></td>
    </tr>
    <tr>
        <td><code>some code</code></td>
        <td><a href="www.google.com">google</a></td>
    </tr>
    <tr>
        <td><a href="http://www.foo.com">www.foo.com</a></td>
        <td>normal</td>
    </tr>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/with-span-elements.md`
```markdown
| First Header  | Second Header     |
| ------------- | ----------------- |
| **bold**      | ![img](foo.jpg)   |
| _italic_      | [link](bla.html)  |
| `some code`   | [google][1]       |
| <www.foo.com> | normal            |


  [1]: www.google.com
```

## File: `test/functional/makehtml/cases/features/tables/with-surroundings.html`
```html
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nisi est, 
ullamcorper euismod iaculis sed, tristique at neque. Nullam metus risus, 
malesuada vitae imperdiet ac, tincidunt eget lacus. Proin ullamcorper 
vulputate dictum. Vestibulum consequat ultricies nibh, sed tempus nisl mattis a.</p>
<table>
    <thead>
        <tr>
            <th>First Header</th>
            <th>Second Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 Cell 1</td>
            <td>Row 1 Cell 2</td>
        </tr>
        <tr>
            <td>Row 2 Cell 1</td>
            <td>Row 2 Cell 2</td>
        </tr>
    </tbody>
</table>
<p>Phasellus ac porttitor quam. Integer cursus accumsan mauris nec interdum. 
Etiam iaculis urna vitae risus facilisis faucibus eu quis risus. Sed aliquet 
rutrum dictum. Vivamus pulvinar malesuada ultricies. Pellentesque in commodo 
nibh. Maecenas justo erat, sodales vel bibendum a, dignissim in orci. Duis 
blandit ornare mi non facilisis. Aliquam rutrum fringilla lacus in semper. 
Sed vel pretium lorem.</p>
```

## File: `test/functional/makehtml/cases/features/tables/with-surroundings.md`
```markdown
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nisi est, 
ullamcorper euismod iaculis sed, tristique at neque. Nullam metus risus, 
malesuada vitae imperdiet ac, tincidunt eget lacus. Proin ullamcorper 
vulputate dictum. Vestibulum consequat ultricies nibh, sed tempus nisl mattis a.

| First Header  | Second Header |
| ------------- | ------------- |
| Row 1 Cell 1  | Row 1 Cell 2  |
| Row 2 Cell 1  | Row 2 Cell 2  |

Phasellus ac porttitor quam. Integer cursus accumsan mauris nec interdum. 
Etiam iaculis urna vitae risus facilisis faucibus eu quis risus. Sed aliquet 
rutrum dictum. Vivamus pulvinar malesuada ultricies. Pellentesque in commodo 
nibh. Maecenas justo erat, sodales vel bibendum a, dignissim in orci. Duis 
blandit ornare mi non facilisis. Aliquam rutrum fringilla lacus in semper. 
Sed vel pretium lorem.
```

## File: `test/functional/makehtml/cases/features/tables/without-body.html`
```html
<table>
    <thead>
        <tr>
            <th>First Header</th>
            <th>Second Header</th>
        </tr>
    </thead>
    <tbody>
    </tbody>
</table>
```

## File: `test/functional/makehtml/cases/features/tables/without-body.md`
```markdown
| First Header  | Second Header |
| ------------- | ------------- |
```

## File: `test/functional/makehtml/cases/features/tables/without-header-delimiter.html`
```html
<p>| First Header  | Second Header |</p>
```

## File: `test/functional/makehtml/cases/features/tables/without-header-delimiter.md`
```markdown
| First Header  | Second Header |
```

## File: `test/functional/makehtml/cases/features/underline/fulltext.html`
```html
<h1 id="markdowntestadaptedfrombitbucket">Markdown test adapted from BitBucket</h1>
<p><a href="http://daringfireball.net/projects/markdown/">Markdown</a> for readmes is pretty popular.  So, I've given you a demo
    here of all the markup we support. In some cases, I copied the doc/examples entirely from the Fireball Markdown site. </p>
<p>I didn't duplicate all the Markdown doc everything tho. For the entire docs and a deeper explanation of Markdown, you still need to go to the <a href="http://daringfireball.net/projects/markdown/">Markdown</a> site.</p>
<p>You can also use <a href="https://confluence.atlassian.com/x/xTAvEw">Markdown mark up</a> in comments, issues, and commit messages.</p>
<p>On this page:</p>
<ul>
    <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-span-elements">Span Elements</a></p>
        <ul>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-emphasis">Emphasis</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-strikethrough">Strikethrough</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-preformatted-code">Preformatted code</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-links">Links</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-images">Images</a></p></li></ul></li>
    <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-block-elements">Block Elements</a></p>
        <ul>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-headings">Headings</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-paragraphs-and-blockquotes">Paragraphs and blockquotes</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-lists">Lists</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-tables">Tables</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-code-and-syntax-highlighting">Code and Syntax highlighting</a></p></li>
            <li><p><a href="https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-horizontal-rules">Horizontal rules</a></p></li></ul></li>
</ul>
<hr />
<h1 id="spanelements">Span Elements</h1>
<p>These elements occur within a line of text.  So, for example font changes or links.</p>
<h2 id="emphasis">Emphasis</h2>
<p>Markdown treats * (asterisk) as emphasis markers. </p>
<p><em>single asterisks</em>
    <strong>double asterisks</strong></p>
<p>All are created from this:</p>
<pre><code>*single asterisks*

**double asterisks**
</code></pre>
<h2 id="underlineexperimental">Underline [experimental]</h2>
<p><u>double underscores</u></p>
<p><u>triple underscores</u></p>
<p>All are created from this:</p>
<pre><code>__double underscores__

___triple underscores___
</code></pre>
<p>You must use the same character must be used to open and close an emphasis span. Emphasis can be used in the mi<em>dd</em>le of a word.</p>
<pre><code>Emphasis can be used in the mi*dd*le of a word.
</code></pre>
<p>But if you surround an * or _ with spaces, it will be treated as a literal asterisk or underscore.</p>
<p>To produce a literal asterisk or underscore at a position where it would otherwise be used as an emphasis delimiter, you can backslash escape it:</p>
<pre><code>\*this text is surrounded by literal asterisks\*
</code></pre>
<h2 id="strikethrough">Strikethrough</h2>
<p>Markdown's Markdown parser supports strikethrough by wrapping text in <code>~~</code>:</p>
<p>~~text that has been struckthrough~~</p>
<p>is created from:</p>
<pre><code>~~text that has been struckthrough~~
</code></pre>
<h2 id="preformattedcode">Preformatted code</h2>
<p>To indicate a span of code, wrap it with <code>`</code> (backtick). Unlike a pre-formatted code block, a code span indicates code within a normal paragraph. For example:</p>
<p>Use the <code>printf()</code> function.</p>
<p>is produced from:</p>
<pre><code>Use the `printf()` function.
</code></pre>
<p>To include a literal backtick character within a code span, you can use multiple backticks as the opening and closing delimiters:</p>
<p><code>There is a literal backtick (`) here.</code>    </p>
<h2 id="links">Links</h2>
<p>Markdown supports inline and reference links. In both styles, the link text is delimited by [square brackets]. To create an inline link, use this syntax:</p>
<pre><code>[ Text for the link ](URL)
</code></pre>
<p>So an inline link to <a href="http://www.yahoo.com">Yahoo</a> looks like this:</p>
<pre><code>So an inline link to [Yahoo](http://www.yahoo.com) looks like this:
</code></pre>
<p>Reference-style links use a second set of square brackets, inside which you place a label of your choosing to identify the link:</p>
<pre><code>This is [an example][id] reference-style link.
</code></pre>
<p>Which gives you a link like this:</p>
<p>This is <a href="http://example.com/" title="Optional Title Here">an example</a> reference-style link.</p>
<p>Elsewhere in the document, usually at the bottom of the file, you define your link label on a line by itself:</p>
<pre><code>[id]: http://example.com/  "Optional Title Here"
</code></pre>
<p>Links can get pretty fancy, so if you want the long form version, visit the
    official <a href="http://daringfireball.net/projects/markdown/">Markdown</a> docs.</p>
<h2 id="images">Images</h2>
<p>Markdown uses an image syntax that is intended to resemble the syntax for links, allowing for two styles: inline and reference. Images appear like this:</p>
<p><img src="http://www.addictedtoibiza.com/wp-content/uploads/2012/12/example.png" alt="Alt text" /></p>
<pre><code>![Alt text](http://www.addictedtoibiza.com/wp-content/uploads/2012/12/example.png)

![Alt text](http://www.addictedtoibiza.com/wp-content/uploads/2012/12/example.png "Optional title")
</code></pre>
<hr />
<h1 id="blockelements">Block Elements</h1>
<p>These are elements that are a single or multiple lines in length</p>
<h2 id="headings">Headings</h2>
<p>You can create Atx-style headings by prefixing with a # (hash mark)</p>
<h1 id="heading1markupheading1">Heading 1 markup  <code># Heading 1</code></h1>
<h1 id=""> </h1>
<h2 id="heading2markupheading2">Heading 2 markup  <code>## Heading 2</code></h2>
<h2 id="-1"> </h2>
<h3 id="heading3markupheading3">Heading 3 markup   <code>### Heading 3</code></h3>
<h3 id="-2"> </h3>
<h4 id="heading4markupheading4">Heading 4 markup  <code>#### Heading 4</code></h4>
<h4 id="-3"> </h4>
<h5 id="heading5markupheading5">Heading 5 markup  <code>##### Heading 5</code></h5>
<h5 id="-4"> </h5>
<h6 id="heading6markupheading6">Heading 6 markup  <code>###### Heading 6</code></h6>
<h6 id="-5"> </h6>
<p>You can also create Setext-style headings which have two levels.</p>
<h1 id="level1markupuseanequalsignequalsign">Level 1 markup use an equal sign = (equal sign) </h1>
<pre><code> Level 1 markup use an equal sign = (equal sign)        
 ==============================
</code></pre>
<h2 id="level2markupusesdashes">Level 2 markup uses - (dashes) </h2>
<pre><code>Level 2 markup uses - (dashes) 
-------------
</code></pre>
<h2 id="paragraphsandblockquotes">PARAGRAPHS and BLOCKQUOTES</h2>
<p>A paragraph is one or more consecutive lines of text separated by one or more
    blank lines. A blank line contains nothing but spaces or tabs. Do not indent
    normal paragraphs with spaces or tabs. New lines/carriage returns within paragraphs require two spaces at the end of the preceding line.</p>
<p>This is one paragraph.</p>
<p>This is a second.</p>
<pre><code>This is one paragraph.

This is a second.
</code></pre>
<p>Markdown uses email-style &gt; (greater than) characters for blockquoting. If youâ€™re familiar with quoting passages of text in an email message, then you know how to create a blockquote in Markdown. It looks best if you hard wrap the text and put a &gt; before every line:</p>
<blockquote>
    <p>This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
        consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.</p>
    <p>Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
        id sem consectetuer libero luctus adipiscing.</p>
</blockquote>
<pre><code>&gt; This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
&gt; consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
&gt; 
&gt; Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
&gt; id sem consectetuer libero luctus adipiscing.
</code></pre>
<p>Blockquotes can be nested (i.e. a blockquote-in-a-blockquote):</p>
<blockquote>
    <p>This is the first level of quoting.</p>
    <blockquote>
        <p>This is nested blockquote.</p>
    </blockquote>
    <p>Back to the first level.</p>
</blockquote>
<pre><code>&gt; This is the first level of quoting.
&gt;
&gt; &gt; This is nested blockquote.
&gt;
&gt; Back to the first level.
</code></pre>
<p>Blockquotes can contain other Markdown elements, including headers, lists, and code blocks:</p>
<blockquote>
    <h2 id="thisisaheader">This is a header.</h2>
    <ol>
        <li>This is the first list item.</li>
        <li>This is the second list item.</li>
    </ol>
    <p>Here's some example code:</p>
    <pre><code>return shell_exec("echo $input | $markdown_script");
</code></pre>
</blockquote>
<pre><code>&gt; ## This is a header.
&gt; 
&gt; 1.   This is the first list item.
&gt; 2.   This is the second list item.
&gt; 
&gt; Here's some example code:
&gt; 
&gt;     return shell_exec("echo $input | $markdown_script");
</code></pre>
<h2 id="lists">Lists</h2>
<p>Markdown supports ordered (numbered) and unordered (bulleted) lists.  List markers typically start at the left margin, but may be indented by up to three spaces. List markers must be followed by one or more spaces or a tab.</p>
<p>Form bulleted lists with any of * (asterisk), + (plus), or - (dash). You can one or any or mix of these to form a list:</p>
<ul>
    <li><p>Red </p></li>
    <li><p>Green </p></li>
    <li><p>Blue</p>
        <pre><code>* Red
+ Green
- Blue
</code></pre></li>
</ul>
<p>Ordered lists require a numeric character followed by a . (period).</p>
<ol>
    <li><p>Item one</p></li>
    <li><p>Item two </p></li>
    <li><p>Item three</p>
        <pre><code>1. Item one
1. Item two 
1. Item three
</code></pre></li>
</ol>
<p>Notice the actual value of the number doesn't matter in the list result. However, for readability better to use this markup:</p>
<pre><code>    1. Item one
    2. Item two 
    3. Item three
</code></pre>
<p>Lists can be embedded in lists. List items may consist of multiple paragraphs. Each subsequent paragraph in a list item must be indented by either 4 spaces or one tab:</p>
<ul>
    <li><p>Red </p></li>
    <li><p>Green </p>
        <ul>
            <li>dark  green </li>
            <li>lime    </li></ul></li>
    <li><p>Blue        </p>
        <ol>
            <li><p>Item one</p>
                <ol>
                    <li>subitem 1 </li>
                    <li>subitem 2</li></ol></li>
            <li><p>Item two </p>
                <p>This is is a first paragraph. </p>
                <ul>
                    <li>Green </li>
                    <li>Blue</li></ul>
                <p>This is a second paragraph.</p></li>
            <li><p>Item three</p></li></ol></li>
</ul>
<p>The code for these embedded lists or paragraphs is:</p>
<pre><code>        * Red 
        + Green 
            * dark  green 
            * lime    
        - Blue        
            1. Item one
                1. subitem 1
                1. subitem 2
            1. Item two 

                This is is a first paragraph. 

                * Green 
                * Blue

                This is a second paragraph.

            1. Item three
</code></pre>
<p>You can also embed blockquotes in a list.</p>
<ul>
    <li>Green</li>
</ul>
<blockquote>
    <p>What is this?  It is embedded blockquote.  Mix 'em and match 'em.</p>
    <ul>
        <li>Blue</li>
        <li>Red</li>
    </ul>
</blockquote>
<pre><code>    * Green
    &gt; What is this?  It is embedded blockquote.  Mix 'em and match 'em.
    * Blue
    * Red
</code></pre>
<p>You can also embed code blocks in a list.</p>
<ul>
    <li><p>Green</p>
        <p>Try this code:</p>
        <pre><code>This is an embedded code block.
</code></pre>
        <p>Then this:</p>
        <pre><code>More code!
</code></pre></li>
    <li><p>Blue</p></li>
    <li><p>Red</p>
        <pre><code>* Green

    Try this code:

        This is an embedded code block.

    Then this:

        More code!

* Blue
* Red
</code></pre></li>
</ul>
<h2 id="tables">Tables</h2>
<p>Markdown does not support <code>&lt;html&gt;</code> so you need to use the - (dash) and the | (pipe) symbols to construct a table. The first line contains column headers. Separate columns with the pipe symbol.</p>
<p>The  second line must be a mandatory separator line between the headers and the content. Subsequent lines are table rows. Columns are always separated by the pipe (|) character.  For example this table:</p>
<p>First Header  | Second Header
    ------------- | -------------
    Content Cell  | Content Cell
    Content Cell  | Content Cell</p>
<p>Comes from this code:</p>
<pre><code>First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
</code></pre>
<p>You can only put simple lines in a table.</p>
<p>You can specify alignment for each column by adding colons to separator lines. A colon at the left of the separator line, left-aligns the column. A colon on the right, right-aligns the column. Add colons to both sides to center the column is center-aligned.</p>
<p>Right     | Left   | Center
    ---------:| :----- |:-----:
    Computer  |  $1600 | one
    Phone     |    $12 | three
    Pipe      |     $1 | eleven</p>
<pre><code>Right     | Left   | Center 
---------:| :----- |:-----:
Computer  |  $1600 | one
Phone     |    $12 | three
Pipe      |     $1 | eleven
</code></pre>
<p>You can apply inline formatting (span-level changes such as fonts or links) to the content of each cell using regular Markdown syntax:</p>
<p>| Function name | Description                    |
    | ------------- | ------------------------------ |
    | <code>help()</code>      | Display the <u>help</u> window.   |
    | <code>destroy()</code>   | <strong>Destroy your computer!</strong>     |</p>
<pre><code>| Function name | Description                    |
| ------------- | ------------------------------ |
| `help()`      | Display the __help__ window.   |
| `destroy()`   | **Destroy your computer!**     |
</code></pre>
<ul>
    <li>-  -</li>
</ul>
<h2 id="codeandsyntaxhighlighting">Code and Syntax highlighting</h2>
<p>Pre-formatted code blocks are used for writing about programming or markup source code. Rather than forming normal paragraphs, the code block linesare interpreted literally.  Markdown wraps a code block in both <code>&lt;pre&gt;</code> and <code>&lt;code&gt;</code> tags.</p>
<p>To produce a code block in Markdown, indent every line of the block by at least 4 spaces or 1 tab. For :</p>
<p>This is a normal paragraph:</p>
<pre><code>This is a code block.
</code></pre>
<p>The code reveals the indentation.</p>
<pre><code>    This is a normal paragraph:

        This is a code block.
</code></pre>
<p>A code block continues until it reaches a line that is not indented (or the end of the page).</p>
<p>Within a code block, &amp; (ampersands) and < > (angle brackets) are automatically converted into HTML entities. This makes it very easy to include example HTML source code using Markdown â€” just paste it and indent it. Markdown will handle the hassle of encoding the ampersands and angle brackets. For example, this:</p>
<p>Here is an example of AppleScript:</p>
<pre><code>&lt;p&gt;Here is an example of AppleScript:&lt;/p&gt;
</code></pre>
<p>To produce a code block in Markdown, simply indent every line of the block by at least 4 spaces or 1 tab. For example, given this input:</p>
<p>You can also highlight snippets of text (Markdown uses the excellent <a href="http://pygments.org/">Pygments</a> library) to allow you to use code highlighting  Here's an example of some Python code:</p>
<pre><code>#!python
#
def wiki_rocks(text): formatter = lambda t: "funky"+t return formatter(text)         
</code></pre>
<p>To do this, do not indent the block. Start the block with <code>```</code> three ticks. Then, provide the comment with the type of syntax you are using.  There is a <a href="http://pygments.org/docs/lexers/">the vast library of Pygment lexers</a>. Markdown accepts the 'short name' or the 'mimetype' of anything in there.</p>
<p>You can also use a fence style for code.</p>
<pre><code>This is a code block, fenced-style
</code></pre>
<p>Which you create with this code:</p>
<pre><code>```
This is a code block, fenced-style
```
</code></pre>
<p>See <a href="http://michelf.ca/projects/php-markdown/extra/">Michel Fortin's blog</a> to try out more examples of this coding style. Not everything he demos is guaranteed to work though.</p>
<hr />
<h1 id="horizontalrules">Horizontal Rules</h1>
<p>You can produce a horizontal line with any of the following codes:</p>
<pre><code>* * *

***

*****

- - - -

-----------------------
</code></pre>
<p>The output looks like this:</p>
<hr />
<hr />
<hr />
<hr />
<hr />
<hr />
```

## File: `test/functional/makehtml/cases/features/underline/fulltext.md`
```markdown
Markdown test adapted from BitBucket
====================

[Markdown][fireball] for readmes is pretty popular.  So, I've given you a demo
here of all the markup we support. In some cases, I copied the doc/examples entirely from the Fireball Markdown site. 

I didn't duplicate all the Markdown doc everything tho. For the entire docs and a deeper explanation of Markdown, you still need to go to the [Markdown][fireball] site.

You can also use [Markdown mark up][BBmarkup] in comments, issues, and commit messages.

On this page:


* [Span Elements](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-span-elements)
    * [Emphasis](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-emphasis)

    * [Strikethrough](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-strikethrough)
    
    * [Preformatted code](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-preformatted-code)

    * [Links](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-links)

    * [Images](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-images)

* [Block Elements](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-block-elements)
    * [Headings](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-headings)

    * [Paragraphs and blockquotes](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-paragraphs-and-blockquotes)

    * [Lists](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-lists)

    * [Tables](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-tables)

    * [Code and Syntax highlighting](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-code-and-syntax-highlighting)

    * [Horizontal rules](https://Markdown.org/tutorials/markdowndemo/overview#markdown-header-horizontal-rules)

- - -

# Span Elements

These elements occur within a line of text.  So, for example font changes or links.

 
## Emphasis

Markdown treats * (asterisk) as emphasis markers. 

*single asterisks*
**double asterisks**

All are created from this:

    *single asterisks*

    **double asterisks**


## Underline [experimental]


__double underscores__

___triple underscores___


All are created from this:


    __double underscores__

    ___triple underscores___


You must use the same character must be used to open and close an emphasis span. Emphasis can be used in the mi*dd*le of a word.

    Emphasis can be used in the mi*dd*le of a word.

But if you surround an * or _ with spaces, it will be treated as a literal asterisk or underscore.

To produce a literal asterisk or underscore at a position where it would otherwise be used as an emphasis delimiter, you can backslash escape it:

    \*this text is surrounded by literal asterisks\*

## Strikethrough

Markdown's Markdown parser supports strikethrough by wrapping text in `~~`:

~~text that has been struckthrough~~

is created from:

    ~~text that has been struckthrough~~

## Preformatted code

To indicate a span of code, wrap it with `` ` `` (backtick). Unlike a pre-formatted code block, a code span indicates code within a normal paragraph. For example:

Use the `printf()` function.

is produced from:

    Use the `printf()` function.
    
To include a literal backtick character within a code span, you can use multiple backticks as the opening and closing delimiters:

``There is a literal backtick (`) here.``    


## Links

Markdown supports inline and reference links. In both styles, the link text is delimited by [square brackets]. To create an inline link, use this syntax:

    [ Text for the link ](URL)

So an inline link to [Yahoo](http://www.yahoo.com) looks like this:

    So an inline link to [Yahoo](http://www.yahoo.com) looks like this:

Reference-style links use a second set of square brackets, inside which you place a label of your choosing to identify the link:

    This is [an example][id] reference-style link.
    
Which gives you a link like this:

This is [an example][id] reference-style link.
    
Elsewhere in the document, usually at the bottom of the file, you define your link label on a line by itself:

    [id]: http://example.com/  "Optional Title Here"
    
Links can get pretty fancy, so if you want the long form version, visit the 
 official [Markdown][fireball] docs.


## Images

Markdown uses an image syntax that is intended to resemble the syntax for links, allowing for two styles: inline and reference. Images appear like this:

![Alt text](http://www.addictedtoibiza.com/wp-content/uploads/2012/12/example.png)



    ![Alt text](http://www.addictedtoibiza.com/wp-content/uploads/2012/12/example.png)

    ![Alt text](http://www.addictedtoibiza.com/wp-content/uploads/2012/12/example.png "Optional title")
    
- - -
# Block Elements

These are elements that are a single or multiple lines in length



## Headings
You can create Atx-style headings by prefixing with a # (hash mark)

# Heading 1 markup  `# Heading 1`
# 
## Heading 2 markup  `## Heading 2`
## 
### Heading 3 markup   `### Heading 3`
### 
#### Heading 4 markup  `#### Heading 4`
#### 
##### Heading 5 markup  `##### Heading 5`
##### 
###### Heading 6 markup  `###### Heading 6`
###### 
You can also create Setext-style headings which have two levels.

Level 1 markup use an equal sign = (equal sign) 
==============================


     Level 1 markup use an equal sign = (equal sign)        
     ==============================
     
Level 2 markup uses - (dashes) 
-------------


    Level 2 markup uses - (dashes) 
    -------------




## PARAGRAPHS and BLOCKQUOTES


A paragraph is one or more consecutive lines of text separated by one or more
blank lines. A blank line contains nothing but spaces or tabs. Do not indent
normal paragraphs with spaces or tabs. New lines/carriage returns within paragraphs require two spaces at the end of the preceding line.

This is one paragraph.

This is a second.

    This is one paragraph.

    This is a second.

Markdown uses email-style > (greater than) characters for blockquoting. If youâ€™re familiar with quoting passages of text in an email message, then you know how to create a blockquote in Markdown. It looks best if you hard wrap the text and put a > before every line:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.


    > This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
    > consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    > 
    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
    > id sem consectetuer libero luctus adipiscing.
    
Blockquotes can be nested (i.e. a blockquote-in-a-blockquote):

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

    > This is the first level of quoting.
    >
    > > This is nested blockquote.
    >
    > Back to the first level.

Blockquotes can contain other Markdown elements, including headers, lists, and code blocks:

> ## This is a header.
> 
> 1.   This is the first list item.
> 2.   This is the second list item.
> 
> Here's some example code:
> 
>     return shell_exec("echo $input | $markdown_script");


    > ## This is a header.
    > 
    > 1.   This is the first list item.
    > 2.   This is the second list item.
    > 
    > Here's some example code:
    > 
    >     return shell_exec("echo $input | $markdown_script");
    



## Lists

Markdown supports ordered (numbered) and unordered (bulleted) lists.  List markers typically start at the left margin, but may be indented by up to three spaces. List markers must be followed by one or more spaces or a tab.

Form bulleted lists with any of * (asterisk), + (plus), or - (dash). You can one or any or mix of these to form a list:

* Red 
+ Green 
- Blue


        * Red
        + Green
        - Blue
    
Ordered lists require a numeric character followed by a . (period).

1. Item one
1. Item two 
1. Item three

        1. Item one
        1. Item two 
        1. Item three
    
Notice the actual value of the number doesn't matter in the list result. However, for readability better to use this markup:

        1. Item one
        2. Item two 
        3. Item three
        
Lists can be embedded in lists. List items may consist of multiple paragraphs. Each subsequent paragraph in a list item must be indented by either 4 spaces or one tab:

* Red 
+ Green 
    * dark  green 
    * lime    
- Blue        
    1. Item one
        1. subitem 1 
        1. subitem 2
    1. Item two 
    
        This is is a first paragraph. 
        
        * Green 
        * Blue
        
        This is a second paragraph.
        
    1. Item three
    
The code for these embedded lists or paragraphs is:

            * Red 
            + Green 
                * dark  green 
                * lime    
            - Blue        
                1. Item one
                    1. subitem 1
                    1. subitem 2
                1. Item two 
    
                    This is is a first paragraph. 
        
                    * Green 
                    * Blue
        
                    This is a second paragraph.
        
                1. Item three

You can also embed blockquotes in a list.

* Green
> What is this?  It is embedded blockquote.  Mix 'em and match 'em.
* Blue
* Red

        * Green
        > What is this?  It is embedded blockquote.  Mix 'em and match 'em.
        * Blue
        * Red



You can also embed code blocks in a list.

* Green

    Try this code:

        This is an embedded code block.

    Then this:

        More code!

* Blue
* Red

        * Green

            Try this code:

                This is an embedded code block.

            Then this:

                More code!

        * Blue
        * Red


## Tables



Markdown does not support `<html>` so you need to use the - (dash) and the | (pipe) symbols to construct a table. The first line contains column headers. Separate columns with the pipe symbol.

The  second line must be a mandatory separator line between the headers and the content. Subsequent lines are table rows. Columns are always separated by the pipe (|) character.  For example this table:

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

Comes from this code:

    First Header  | Second Header
    ------------- | -------------
    Content Cell  | Content Cell
    Content Cell  | Content Cell
    
    
You can only put simple lines in a table.

You can specify alignment for each column by adding colons to separator lines. A colon at the left of the separator line, left-aligns the column. A colon on the right, right-aligns the column. Add colons to both sides to center the column is center-aligned.

Right     | Left   | Center 
---------:| :----- |:-----:
Computer  |  $1600 | one
Phone     |    $12 | three
Pipe      |     $1 | eleven

    Right     | Left   | Center 
    ---------:| :----- |:-----:
    Computer  |  $1600 | one
    Phone     |    $12 | three
    Pipe      |     $1 | eleven


You can apply inline formatting (span-level changes such as fonts or links) to the content of each cell using regular Markdown syntax:


| Function name | Description                    |
| ------------- | ------------------------------ |
| `help()`      | Display the __help__ window.   |
| `destroy()`   | **Destroy your computer!**     |

    | Function name | Description                    |
    | ------------- | ------------------------------ |
    | `help()`      | Display the __help__ window.   |
    | `destroy()`   | **Destroy your computer!**     |




- -  -


## Code and Syntax highlighting


Pre-formatted code blocks are used for writing about programming or markup source code. Rather than forming normal paragraphs, the code block linesare interpreted literally.  Markdown wraps a code block in both `<pre>` and `<code>` tags.

To produce a code block in Markdown, indent every line of the block by at least 4 spaces or 1 tab. For :

This is a normal paragraph:

    This is a code block.

The code reveals the indentation.

        This is a normal paragraph:

            This is a code block.

A code block continues until it reaches a line that is not indented (or the end of the page).

Within a code block, & (ampersands) and < > (angle brackets) are automatically converted into HTML entities. This makes it very easy to include example HTML source code using Markdown â€” just paste it and indent it. Markdown will handle the hassle of encoding the ampersands and angle brackets. For example, this:

<p>Here is an example of AppleScript:</p>

    <p>Here is an example of AppleScript:</p>

To produce a code block in Markdown, simply indent every line of the block by at least 4 spaces or 1 tab. For example, given this input:


You can also highlight snippets of text (Markdown uses the excellent [Pygments][] library) to allow you to use code highlighting  Here's an example of some Python code:

```
#!python
#
def wiki_rocks(text): formatter = lambda t: "funky"+t return formatter(text)         
```

To do this, do not indent the block. Start the block with ` ``` ` three ticks. Then, provide the comment with the type of syntax you are using.  There is a [the vast library of Pygment lexers][lexers]. Markdown accepts the 'short name' or the 'mimetype' of anything in there.

You can also use a fence style for code.

```
This is a code block, fenced-style
```

Which you create with this code:

    ```
    This is a code block, fenced-style
    ```
    
See [Michel Fortin's blog][extra] to try out more examples of this coding style. Not everything he demos is guaranteed to work though.


- - -

# Horizontal Rules

You can produce a horizontal line with any of the following codes:

    * * *

    ***

    *****

    - - - -

    -----------------------
    
The output looks like this:

* * *

***

*****

- - - 

-----------------------

- - -



[lexers]: http://pygments.org/docs/lexers/
[fireball]: http://daringfireball.net/projects/markdown/ 
[Pygments]: http://pygments.org/ 
[Extra]: http://michelf.ca/projects/php-markdown/extra/
[id]: http://example.com/  "Optional Title Here"
[BBmarkup]: https://confluence.atlassian.com/x/xTAvEw
```

## File: `test/functional/makehtml/cases/features/underline/simple.html`
```html
<p>this is <u>underlined</u> word</p>
<p><u>an underlined sentence</u></p>
<p><u>three underscores are fine</u></p>
<p>_single_ underscores are left alone</p>
<p><u>multiple</u> underlines in a <u>paragraph</u></p>
```

## File: `test/functional/makehtml/cases/features/underline/simple.md`
```markdown
this is __underlined__ word

__an underlined sentence__

___three underscores are fine___

_single_ underscores are left alone

__multiple__ underlines in a __paragraph__
```

## File: `test/functional/makehtml/cases/ghost/markdown-magic.html`
```html
<h3 id="automaticlinks">Automatic Links</h3>
<pre><code>https://ghost.org
</code></pre>
<p><a href="https://ghost.org">https://ghost.org</a></p>
<h3 id="markdownfootnotes">Markdown Footnotes</h3>
<pre><code>The quick brown fox[^1] jumped over the lazy dog[^2].

    [^1]: Foxes are red
    [^2]: Dogs are usually not red
</code></pre>
<p>The quick brown fox[^1] jumped over the lazy dog[^2].</p>
<h3 id="syntaxhighlighting">Syntax Highlighting</h3>
<pre><code>```language-javascript
    [...]
    ```
</code></pre>
<p>Combined with <a href="http://prismjs.com/">Prism.js</a> in the Ghost theme:</p>
<pre><code class="language-javascript language-language-javascript">// # Notifications API
// RESTful API for creating notifications
var Promise            = require('bluebird'),
_                  = require('lodash'),
canThis            = require('../permissions').canThis,
errors             = require('../errors'),
utils              = require('./utils'),

// Holds the persistent notifications
notificationsStore = [],
// Holds the last used id
notificationCounter = 0,
notifications;
</code></pre>
```

## File: `test/functional/makehtml/cases/ghost/markdown-magic.md`
```markdown
### Automatic Links

```
https://ghost.org
```

https://ghost.org

### Markdown Footnotes

```
The quick brown fox[^1] jumped over the lazy dog[^2].

[^1]: Foxes are red
[^2]: Dogs are usually not red
```

The quick brown fox[^1] jumped over the lazy dog[^2].


### Syntax Highlighting

    ```language-javascript
       [...]
    ```

Combined with [Prism.js](http://prismjs.com/) in the Ghost theme:

```language-javascript
// # Notifications API
// RESTful API for creating notifications
var Promise            = require('bluebird'),
    _                  = require('lodash'),
    canThis            = require('../permissions').canThis,
    errors             = require('../errors'),
    utils              = require('./utils'),

    // Holds the persistent notifications
    notificationsStore = [],
    // Holds the last used id
    notificationCounter = 0,
    notifications;
```
```

## File: `test/functional/makehtml/cases/ghost/underscore.html`
```html
<p>foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</p>
<p><em>baz_bar_foo</em></p>
<p><strong>baz_bar_foo</strong></p>
<p><strong><em>baz_bar_foo</em></strong></p>
<p>baz bar foo <em>baz_bar_foo foo bar baz</em> and foo</p>
<p>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</p>
<p><code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></p>
<pre><code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
</code></pre>
<pre><code class="html language-html">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
</code></pre>
<pre>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</pre>
<pre><code class="language-html">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></pre>
<pre class="lang-html"><code class="language-html">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></pre>
<script>
    var strike = "foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo";
    var foo_bar_baz_bar_foo = "foo_bar_";
</script>
<p><a href="http://myurl.com/foo_bar_baz_bar_foo">foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</a></p>
<p><a href="http://myurl.com/foo_bar_baz_bar_foo" title="foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</a></p>
<p><img src="http://myurl.com/foo_bar_baz_bar_foo" alt="foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo"></p>
<h2 id="foo_bar_bazfoo_bar_baz_bar_foo_foo_barbaz_bar_baz_foo">foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</h2>
<h3 id="foo_bar_bazfoo_bar_baz_bar_foo_foo_barbaz_bar_baz_foo-1">foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</h3>
<ol>
<li>foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</li>
<li>foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</li>
</ol>
<blockquote>
<p>blockquote foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</p>
</blockquote>
<ul>
<li>foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</li>
<li>foo_bar_baz foo_bar_baz_bar_foo <em>foo_bar baz_bar</em> baz_foo</li>
</ul>
<hr />
<p><a href="http://en.wikipedia.org/wiki/Tourism_in_Germany">http://en.wikipedia.org/wiki/Tourism_in_Germany</a></p>
<p><a href="http://en.wikipedia.org/wiki/Tourism_in_Germany">an example</a></p>
<p>Another <a href="http://en.wikipedia.org/wiki/Tourism_in_Germany">example</a> of a link</p>
<p><code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></p>
<!-- These two cases still have bad <ems> because showdown handles them incorrectly -->
<p><code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></p>
<p><img src="http://myurl.com/foo_bar_baz_bar_foo" alt="foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo" /></p>
<p><a href="http://myurl.com/foo_bar_baz_bar_foo">http://myurl.com/foo_bar_baz_bar_foo</a></p>
<p><a href="http://myurl.com/foo_bar_baz_bar_foo">http://myurl.com/foo_bar_baz_bar_foo</a></p>
<p><em>italics</em>.</p>
<p><em>italics</em>   .</p>
```

## File: `test/functional/makehtml/cases/ghost/underscore.md`
```markdown
foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

_baz_bar_foo_

__baz_bar_foo__

___baz_bar_foo___

baz bar foo _baz_bar_foo foo bar baz_ and foo

foo\_bar\_baz foo\_bar\_baz\_bar\_foo \_foo\_bar baz\_bar\_ baz\_foo

`foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo`


    foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo


```html
foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
```

<pre>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</pre>

<pre><code class="language-html">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></pre>

<pre class="lang-html"><code class="language-html">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></pre>

<script>
var strike = "foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo";
var foo_bar_baz_bar_foo = "foo_bar_";
</script>

[foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo](http://myurl.com/foo_bar_baz_bar_foo)

<a href="http://myurl.com/foo_bar_baz_bar_foo" title="foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo">foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</a>

<img src="http://myurl.com/foo_bar_baz_bar_foo" alt="foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo">

foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
-----

### foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

1. foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
2. foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

> blockquote foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

* foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo
* foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo

-------

http://en.wikipedia.org/wiki/Tourism_in_Germany

[an example] [wiki]

Another [example][wiki] of a link

[wiki]: http://en.wikipedia.org/wiki/Tourism_in_Germany

<p><code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code></p>

<!-- These two cases still have bad <ems> because showdown handles them incorrectly -->

<code>foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo</code>

![foo_bar_baz foo_bar_baz_bar_foo _foo_bar baz_bar_ baz_foo](http://myurl.com/foo_bar_baz_bar_foo)

http://myurl.com/foo_bar_baz_bar_foo

<http://myurl.com/foo_bar_baz_bar_foo>

_italics_.

_italics_   .
```

## File: `test/functional/makehtml/cases/issues/#107.inner-underscore-parse-to-block.html`
```html
<p>escaped word_with_underscores</p>
<p>escaped word__with__double underscores</p>
<p>escaped word<em>_with_</em>single italic underscore</p>
<p>escaped word*with*asterixs</p>
<p>escaped word**with**asterixs</p>
<p>escaped word<strong>*with*</strong>bold asterixs</p>
```

## File: `test/functional/makehtml/cases/issues/#107.inner-underscore-parse-to-block.md`
```markdown
escaped word\_with\_underscores

escaped word\_\_with\_\_double underscores

escaped word_\_with\__single italic underscore

escaped word\*with*asterixs

escaped word\*\*with\*\*asterixs

escaped word**\*with\***bold asterixs
```

## File: `test/functional/makehtml/cases/issues/#142.odd-behaviour-for-multiple-consecutive-lists.html`
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
</ol>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
```

## File: `test/functional/makehtml/cases/issues/#142.odd-behaviour-for-multiple-consecutive-lists.md`
```markdown
* Item 1
* Item 2

1. Item 1
2. Item 2

- Item 1
- Item 2
```

## File: `test/functional/makehtml/cases/issues/#150.hyphens-are-getting-removed.html`
```html
<p>2015-10-04</p>
```

## File: `test/functional/makehtml/cases/issues/#150.hyphens-are-getting-removed.md`
```markdown
2015-10-04
```

## File: `test/functional/makehtml/cases/issues/#183.gh-code-blocks-within-lists-do-not-render-properly.html`
```html
<ol>
<li><p>Hi, I am a thing</p>
<pre><code class="sh language-sh">$ git clone thing.git

dfgdfg
</code></pre></li>
<li><p>I am another thing!</p>
<pre><code class="sh language-sh">$ git clone other-thing.git

foobar
</code></pre></li>
</ol>
```

## File: `test/functional/makehtml/cases/issues/#183.gh-code-blocks-within-lists-do-not-render-properly.md`
```markdown
1. Hi, I am a thing

    ```sh
    
    $ git clone thing.git
   
    dfgdfg
    ```

1. I am another thing!

    ```sh
   
    $ git clone other-thing.git

    foobar
    ```
```

## File: `test/functional/makehtml/cases/issues/#191.blockquote-followed-by-an-heading.html`
```html
<blockquote>
    <p>a blockquote</p>
    <h1 id="followedbyanheading">followed by an heading</h1>
</blockquote>
```

## File: `test/functional/makehtml/cases/issues/#191.blockquote-followed-by-an-heading.md`
```markdown
> a blockquote
# followed by an heading
```

## File: `test/functional/makehtml/cases/issues/#196.entity-in-code-block-in-nested-list.html`
```html
<p>Test pre in a list</p>
<ul>
    <li>&amp; &lt;</li>
    <li><code>&amp; &lt;</code><ul>
        <li>&amp; &lt;</li>
        <li><code>&amp; &lt;</code><ul>
            <li>&amp; &lt;</li>
            <li><code>&amp; &lt;</code><ul>
                <li>&amp; &lt;</li>
                <li><code>&amp; &lt;</code></li></ul></li></ul></li></ul></li>
</ul>
```

## File: `test/functional/makehtml/cases/issues/#196.entity-in-code-block-in-nested-list.md`
```markdown
Test pre in a list

- & <
- `& <`
    - & <
    - `& <`
        - & <
        - `& <`
            - & <
            - `& <`
```

## File: `test/functional/makehtml/cases/issues/#220.html-breaks-markdown-parsing.html`
```html
<h2 id="title1">Title 1</h2>
<div></div>
<h1 id="title2">Title 2</h1>
<div>
</div>
```

## File: `test/functional/makehtml/cases/issues/#220.html-breaks-markdown-parsing.md`
```markdown
Title 1
-------

<div></div>


# Title 2


<div>
</div>
```

## File: `test/functional/makehtml/cases/issues/#229.2.code-being-parsed-inside-HTML-code-tags.html`
```html
<pre lang="no-highlight"><code>
foo

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

bar
</code></pre>
<p>this is a long paragraph</p>
<p>this is another long paragraph</p>
<pre lang="no-highlight"><code>```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#229.2.code-being-parsed-inside-HTML-code-tags.md`
```markdown
<pre lang="no-highlight"><code>
foo

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

bar
</code></pre>

this is a long paragraph

this is another long paragraph

<pre lang="no-highlight"><code>```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#229.code-being-parsed-inside-HTML-code-tags.html`
```html
<pre lang="no-highlight"><code>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting.
But let's throw in a &lt;b&gt;tag&lt;/b&gt;.
```
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#229.code-being-parsed-inside-HTML-code-tags.md`
```markdown
<pre lang="no-highlight"><code>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting.
But let's throw in a <b>tag</b>.
```
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#230.paragraphs-are-ignored-between-code-tags.html`
```html
<pre lang="no-highlight"><code>```python
var s;
```
</code></pre>
<p>this is a long paragraph</p>
<pre lang="no-highlight"><code>
```javascript
var s;
```
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#230.paragraphs-are-ignored-between-code-tags.md`
```markdown
<pre lang="no-highlight"><code>```python
var s;
```
</code></pre>

this is a long paragraph

<pre lang="no-highlight"><code>
```javascript
var s;
```
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#236.wrong-lt-parsing-when-attached-to-word.html`
```html
<p>this should be <parsed></parsed></p>
<p>this should be <parsed></p>
<p>this should be <parsed/></p>
<p>this should&gt; appear</p>
<p>this text &lt;should appear</p>
```

## File: `test/functional/makehtml/cases/issues/#236.wrong-lt-parsing-when-attached-to-word.md`
```markdown
this should be <parsed></parsed>

this should be <parsed>

this should be <parsed/>

this should> appear

this text <should appear
```

## File: `test/functional/makehtml/cases/issues/#261.mix-images-with-links.html`
```html
<p><img src="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png" alt="sd-inline" /> <a href="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png">sd-ref</a></p>
<p>foo</p>
<p><a href="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png">sd-inline</a> <img src="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="sd-ref" /></p>
<p>foo</p>
<p><img src="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="sd-ref" /> <a href="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png">sd-inline</a></p>
<p>foo</p>
<p><a href="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png">sd-ref</a> <img src="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png" alt="sd-inline" /></p>
<p>foo</p>
<p><a href="http://www.google.com/"><img src="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="sd-ref" /></a></p>
```

## File: `test/functional/makehtml/cases/issues/#261.mix-images-with-links.md`
```markdown
![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) [sd-ref][sd-logo]

foo

[sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) ![sd-ref][sd-logo]

foo

![sd-ref][sd-logo] [sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

foo

[sd-ref][sd-logo] ![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

foo

[![sd-ref][sd-logo]](http://www.google.com/)

[sd-logo]: https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
```

## File: `test/functional/makehtml/cases/issues/#261.reference-style-image-after-inline-style-image-does-not-work-correctely.html`
```html
<p><img src="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png" alt="sd-inline" /> <img src="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="sd-ref" /></p>
<p>foo</p>
<p><img src="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="sd-ref" /> <img src="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png" alt="sd-inline" /></p>
```

## File: `test/functional/makehtml/cases/issues/#261.reference-style-image-after-inline-style-image-does-not-work-correctely.md`
```markdown
![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) ![sd-ref][sd-logo]

foo

![sd-ref][sd-logo] ![sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

[sd-logo]: https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
```

## File: `test/functional/makehtml/cases/issues/#261.reference-style-link-after-inline-style-link-does-not-work-correctely.html`
```html
<p><a href="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png">sd-inline</a> <a href="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png">sd-ref</a></p>
<p>foo</p>
<p><a href="https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png">sd-ref</a> <a href="https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png">sd-inline</a></p>
```

## File: `test/functional/makehtml/cases/issues/#261.reference-style-link-after-inline-style-link-does-not-work-correctely.md`
```markdown
[sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png) [sd-ref][sd-logo]

foo

[sd-ref][sd-logo] [sd-inline](https://raw.githubusercontent.com/showdownjs/logo/master/dist/logo.readme.png)

[sd-logo]: https://www.google.pt/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
```

## File: `test/functional/makehtml/cases/issues/#288.code-blocks-containing-xml-comments-are-not-converted-correctly-when-nested-in-list-items.html`
```html
<ul>
<li><p>list item 1</p>
<pre><code>&lt;parent&gt;
&lt;child&gt;child1&lt;/child&gt;
&lt;!-- This is a comment --&gt;
&lt;child&gt;child2&lt;/child&gt;
&lt;child&gt;some text &lt;!-- a comment --&gt;&lt;/child&gt;
&lt;/parent&gt;
</code></pre></li>
<li><p>list item 2</p></li>
</ul>
<pre><code>&lt;parent&gt;
&lt;child&gt;child1&lt;/child&gt;
&lt;!-- This is a comment --&gt;
&lt;child&gt;child2&lt;/child&gt;
&lt;child&gt;some text &lt;!-- a comment --&gt;&lt;/child&gt;
&lt;/parent&gt;
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#288.code-blocks-containing-xml-comments-are-not-converted-correctly-when-nested-in-list-items.md`
```markdown
* list item 1

    ```
    <parent>
    <child>child1</child>
    <!-- This is a comment -->
    <child>child2</child>
    <child>some text <!-- a comment --></child>
    </parent>
    ```

* list item 2

```
<parent>
<child>child1</child>
<!-- This is a comment -->
<child>child2</child>
<child>some text <!-- a comment --></child>
</parent>
```
```

## File: `test/functional/makehtml/cases/issues/#299.nested-ordered-unordered-list-inconsistent-behavior-2.html`
```html
<ul>
    <li>one</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>one</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>one</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>one<ol>
        <li>two</li></ol></li>
</ul>
<p>foo</p>
<ul>
    <li>one</li>
    <li>two</li>
</ul>
<p>foo</p>
<ul>
    <li>one</li>
    <li>two</li>
</ul>
<p>foo</p>
<ul>
    <li>one</li>
    <li>two</li>
</ul>
<p>foo</p>
<ul>
    <li>one</li>
    <li>two</li>
</ul>
<p>foo</p>
<ul>
    <li>one<ul>
        <li>two</li></ul></li>
</ul>
```

## File: `test/functional/makehtml/cases/issues/#299.nested-ordered-unordered-list-inconsistent-behavior-2.md`
```markdown
 * one
 1. two

foo

  * one
  1. two

foo

   * one
   1. two

foo

   * one
     1. two

foo

 * one
 * two

foo

  * one
  * two

foo

   * one
   * two

foo

   * one
* two

foo

   * one
    * two
```

## File: `test/functional/makehtml/cases/issues/#299.nested-ordered-unordered-list-inconsistent-behavior-3.html`
```html
<ul>
    <li>one long paragraph of
text</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>one long paragraph of
text</li>
</ul>
<ol>
    <li>two</li>
</ol>
```

## File: `test/functional/makehtml/cases/issues/#299.nested-ordered-unordered-list-inconsistent-behavior-3.md`
```markdown
 * one long paragraph of
text
 1. two

foo

  * one long paragraph of
text
   1. two
```

## File: `test/functional/makehtml/cases/issues/#299.nested-ordered-unordered-list-inconsistent-behavior.html`
```html
<ul>
    <li>one</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>one</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>one</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>one</li>
</ul>
<ol>
    <li>two</li>
</ol>
<p>foo</p>
<ul>
    <li>uli one</li>
    <li>uli two</li>
</ul>
<p>foo</p>
<ul>
    <li>uli one</li>
    <li>uli two</li>
</ul>
<p>foo</p>
<ul>
    <li>uli one</li>
    <li>uli two</li>
</ul>
<p>foo</p>
<ul>
    <li>uli one</li>
    <li>uli two</li>
</ul>
```

## File: `test/functional/makehtml/cases/issues/#299.nested-ordered-unordered-list-inconsistent-behavior.md`
```markdown
* one
1. two

foo

* one
 1. two

foo

* one
  1. two

foo

* one
   1. two

foo

* uli one
* uli two

foo

* uli one
 * uli two

foo

* uli one
  * uli two

foo

* uli one
   * uli two
```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char.html`
```html
<ul>
<li>- - a</li>
</ul>
<p>a</p>
<ul>
<li>- * - - + a</li>
</ul>
<p>a</p>
<ol>
<li>2. 3. 4. 5.</li>
</ol>
<p>a</p>
<ol>
<li>2. 3. 4. 5. a</li>
</ol>
```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char.md`
```markdown
- - - a

a

+ - * - - + a

a

1. 2. 3. 4. 5.

a

1. 2. 3. 4. 5. a
```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char2.html`
```html
<ul>
<li><p>- - a</p></li>
<li><p>- * - - + a</p></li>
</ul>
<ol>
<li><p>2. 3. 4. 5.</p></li>
<li><p>2. 3. 4. 5. a</p></li>
</ol>
```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char2.md`
```markdown
- - - a

+ - * - - + a

1. 2. 3. 4. 5.

1. 2. 3. 4. 5. a
```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char3.html`
```html
<ul>
<li>-
a</li>
</ul>
<p>fooo</p>
<ul>
<li><p>- - aaaaa</p>
<p>bbbbb</p></li>
</ul>

```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char3.md`
```markdown
- - 
a


fooo


- - - aaaaa

   bbbbb
```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char4.html`
```html
<ul>
<li>- - - -- - - - - - - -- - - - - - - - - - -    - - - - - - - - -  abcd</li>
</ul>
```

## File: `test/functional/makehtml/cases/issues/#312.spaced-dashes-followed-by-char4.md`
```markdown
- - - - -- - - - - - - -- - - - - - - - - - -    - - - - - - - - -  abcd
```

## File: `test/functional/makehtml/cases/issues/#317.spaces-before-hr.html`
```html
<hr />
<hr />
```

## File: `test/functional/makehtml/cases/issues/#317.spaces-before-hr.md`
```markdown
   ---

   - - -
```

## File: `test/functional/makehtml/cases/issues/#332.inconsistent-behavior-of-emphasis-and-strong.html`
```html
<p>foo *bar *baz</p>
<p>foo **bar **baz</p>
<p>foo ***bar ***baz</p>
<p>foo _bar _baz</p>
<p>foo __bar __baz</p>
<p>foo ___bar ___baz</p>
<p>foo *bar *baz *bazinga</p>
<p>foo **bar **baz **bazinga</p>
<p>foo ***bar ***baz ***bazinga</p>
<p>foo _bar _baz __bazinga</p>
<p>foo __bar __baz __bazinga</p>
<p>foo ___bar ___baz ___bazinga</p>
<p><em>f</em></p>
<p><strong>f</strong></p>
<p><em>f</em></p>
<p><strong>f</strong></p>
<p>foo **bar **baz <strong>bazinga bla</strong></p>
<p>foo <strong>bar **baz **bazinga bla</strong></p>
<p>foo <strong>**bar **baz **bazinga bla</strong></p>
<p>this is <strong><a href="//google.com/foo**bar">imbued link with strong</a></strong></p>
<p>this is <strong><a href="google.com/foo__bar">imbued link with strong</a></strong></p>
```

## File: `test/functional/makehtml/cases/issues/#332.inconsistent-behavior-of-emphasis-and-strong.md`
```markdown
foo *bar *baz

foo **bar **baz

foo ***bar ***baz

foo _bar _baz

foo __bar __baz

foo ___bar ___baz

foo *bar *baz *bazinga

foo **bar **baz **bazinga

foo ***bar ***baz ***bazinga

foo _bar _baz __bazinga

foo __bar __baz __bazinga

foo ___bar ___baz ___bazinga

*f*

**f**

_f_

__f__

foo **bar **baz **bazinga bla**

foo __bar **baz **bazinga bla__

foo __**bar **baz **bazinga bla__

this is **<a href="//google.com/foo**bar">imbued link with strong</a>**

this is __<a href="google.com/foo__bar">imbued link with strong</a>__
```

## File: `test/functional/makehtml/cases/issues/#345.no-escape-for-the-pipe-character.html`
```html
<p>this |</p>
```

## File: `test/functional/makehtml/cases/issues/#345.no-escape-for-the-pipe-character.md`
```markdown
this \|
```

## File: `test/functional/makehtml/cases/issues/#390.brackets-in-URL-break-images.html`
```html
<p>This is an <img src="./image/cat(1).png" alt="image" /></p>
<p>This is another <img src="./image/cat(1).png" alt="image" /></p>
<p><a href="http://example.com"><img src="./image/cat(1).png" alt="image link" /></a></p>
<p><a href="http://example.com"><img src="./image/cat1).png" alt="image link" /></a></p>
```

## File: `test/functional/makehtml/cases/issues/#390.brackets-in-URL-break-images.md`
```markdown
This is an ![image][]

[image]: ./image/cat(1).png

This is another ![image](./image/cat(1).png)

[![image link](./image/cat(1).png)](http://example.com)

[![image link](<./image/cat1).png>)](http://example.com)
```

## File: `test/functional/makehtml/cases/issues/#390.brackets-in-URL-break-links.html`
```html
<p>This is a <a href="https://en.wikipedia.org/wiki/Textile_(markup_language)" title="Textile">link</a>.</p>
<p>This is another <a href="https://en.wikipedia.org/wiki/Textile_(markup_language)" title="Textile">link2</a>.</p>
<p><a href="./image/cat1).png" title="title">link3</a></p>
<p><a href="https://en.wikipedia.org/wiki/Textile_(markup_language)" title="Textile">link4</a>(this should work)</p>
```

## File: `test/functional/makehtml/cases/issues/#390.brackets-in-URL-break-links.md`
```markdown
This is a [link][].

[link]: https://en.wikipedia.org/wiki/Textile_(markup_language) "Textile"

This is another [link2](https://en.wikipedia.org/wiki/Textile_(markup_language) "Textile").

[link3](<./image/cat1).png> "title")

[link4](https://en.wikipedia.org/wiki/Textile_(markup_language) "Textile")(this should work)
```

## File: `test/functional/makehtml/cases/issues/#393.showdown-hangs-with-malformed-html.html`
```html
<p><p>malformed<p></p>
```

## File: `test/functional/makehtml/cases/issues/#393.showdown-hangs-with-malformed-html.md`
```markdown
<p>malformed<p>
```

## File: `test/functional/makehtml/cases/issues/#397.unordered-list-strange-behavior.html`
```html
<ul>
    <li><p><strong>Customer</strong> – Opens the Customer List. Refer to the document “Customer Management”.</p>
        <ul>
            <li>Customer List</li>
            <li>New Customer</li>
            <li>Customer Prices</li>
            <li>Appointments</li></ul></li>
    <li><p><strong>Designer</strong> - Opens the Designer List. Refer to the document “Designer Commissions”.</p>
        <ul>
            <li>Designer List</li>
            <li>New Designer</li>
            <li>Designer Payment List</li>
            <li>New Designer Payment</li></ul></li>
</ul>
```

## File: `test/functional/makehtml/cases/issues/#397.unordered-list-strange-behavior.md`
```markdown
- **Customer** – Opens the Customer List. Refer to the document “Customer Management”.
    - Customer List
    - New Customer
    - Customer Prices
    - Appointments

- **Designer** - Opens the Designer List. Refer to the document “Designer Commissions”.
    - Designer List
    - New Designer
    - Designer Payment List
    - New Designer Payment
```

## File: `test/functional/makehtml/cases/issues/#429.multiline-base64-image-support.html`
```html
<p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7ljmRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYSURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=" alt="foo" /></p>
<p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7ljmRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYSURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=" alt="bar" /></p>

```

## File: `test/functional/makehtml/cases/issues/#429.multiline-base64-image-support.md`
```markdown
![foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7ljmRAAAAAXNSR0IArs4c6QAAAARnQU1BAA
Cxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYSURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=)

![bar][]


[bar]:
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7ljmRAAAAAXNSR0IArs4c6QAAAARnQU1BAA
Cxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYSURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=
```

## File: `test/functional/makehtml/cases/issues/#467.header-ids-for-subheadings.html`
```html
<h2 id="headeridinh2">header id in h2</h2>
<h3 id="headeridinh3">header id in h3</h3>
<h4 id="headeridinh4">header id in h4</h4>
<h5 id="headeridinh5">header id in h5</h5>
<h6 id="headeridinh6">header id in h6</h6>
```

## File: `test/functional/makehtml/cases/issues/#467.header-ids-for-subheadings.md`
```markdown
## header id in h2

### header id in h3

#### header id in h4

##### header id in h5

###### header id in h6
```

## File: `test/functional/makehtml/cases/issues/#494.enumerated-code-blocks-are-partially-escaped-when-including-empy-lines-between-code-2.html`
```html
<pre><code>public static void main(String[] args) {

    for (int i = 0; i &lt; 10 &amp;&amp; true; i++) {
    
        System.out.println("Hello World");
    }

    // stuff here is affected as well &lt;&gt;&amp;&amp;%
}
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#494.enumerated-code-blocks-are-partially-escaped-when-including-empy-lines-between-code-2.md`
```markdown
```
public static void main(String[] args) {

    for (int i = 0; i < 10 && true; i++) {

        System.out.println("Hello World");
    }

    // stuff here is affected as well <>&&%
}
```
```

## File: `test/functional/makehtml/cases/issues/#494.enumerated-code-blocks-are-partially-escaped-when-including-empy-lines-between-code.html`
```html
<ol>
    <li><p>Code block as part of list</p>
<pre><code>public static void main(String[] args) {

    for (int i = 0; i &lt; 10 &amp;&amp; true; i++) {
    
        System.out.println("Hello World");
    }

    // stuff here is affected as well &lt;&gt;&amp;&amp;%
}
</code></pre></li>
</ol>
```

## File: `test/functional/makehtml/cases/issues/#494.enumerated-code-blocks-are-partially-escaped-when-including-empy-lines-between-code.md`
```markdown
1. Code block as part of list

    ```
    public static void main(String[] args) {

        for (int i = 0; i < 10 && true; i++) {

            System.out.println("Hello World");
        }

        // stuff here is affected as well <>&&%
    }
    ```
```

## File: `test/functional/makehtml/cases/issues/#495.headings-different-behavior-in-paragraphs-and-lists.html`
```html
<ul>
  <li>Increase the number of water changes.</li>
  <li><h1 id="proteinskimmers">Protein skimmers:</h1>
    <p>This remove dissolved</p></li>
  <li><h1 id="chemicalfiltermedia">Chemical filter media:</h1>
    <p>When placed in your filter</p></li>
<li>#</li>
<li>something</li>
<li>#
  something</li>
<li># something</li>
</ul>
```

## File: `test/functional/makehtml/cases/issues/#495.headings-different-behavior-in-paragraphs-and-lists.md`
```markdown
- Increase the number of water changes.
- # Protein skimmers:
  This remove dissolved
- # Chemical filter media:
  When placed in your filter
- #
- something
- #
something
- \# something
```

## File: `test/functional/makehtml/cases/issues/#510.specific-string-gets-removed-from-text.html`
```html
<p>[^1]:a</p>
<p>[^1]:a</p>
```

## File: `test/functional/makehtml/cases/issues/#510.specific-string-gets-removed-from-text.md`
```markdown
\[^1]:a

[^1]\:a
```

## File: `test/functional/makehtml/cases/issues/#523.leading-space-breaks-gfm-code-blocks.html`
```html
<pre><code class="javascript language-javascript">var test = test;
function foo() {
  return 'bar';
}
</code></pre>
<pre><code class="javascript language-javascript">var test = test;
function foo() {
  return 'bar';
}
</code></pre>
<pre><code class="javascript language-javascript">var test = test;
function foo() {
  return 'bar';
}
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#523.leading-space-breaks-gfm-code-blocks.md`
```markdown
 ```javascript
var test = test;
function foo() {
  return 'bar';
}
 ```

  ```javascript
var test = test;
function foo() {
  return 'bar';
}
  ```

   ```javascript
var test = test;
function foo() {
  return 'bar';
}
   ```
```

## File: `test/functional/makehtml/cases/issues/#585.error-when-using-image-references.html`
```html
<p>[<img src="http://example.com/foo.png" alt="the-image" />]</p>
```

## File: `test/functional/makehtml/cases/issues/#585.error-when-using-image-references.md`
```markdown
[![the-image]]

[the-image]: http://example.com/foo.png
```

## File: `test/functional/makehtml/cases/issues/#697.space-between-inline-elements.html`
```html
<p><em>one</em> <em>two</em> <em>three</em></p>
```

## File: `test/functional/makehtml/cases/issues/#697.space-between-inline-elements.md`
```markdown
*one* *two* *three*
```

## File: `test/functional/makehtml/cases/issues/#83.parsed-text-links-with-underscores.html`
```html
<p>plain text link http://test.com/this_has/one.html with underscores</p>
<p>legit·word_with·1·underscore</p>
<p>a word<em>with</em>2underscores (gets em)</p>
```

## File: `test/functional/makehtml/cases/issues/#83.parsed-text-links-with-underscores.md`
```markdown
plain text link http://test.com/this_has/one.html with underscores

legit·word_with·1·underscore

a word_with_2underscores (gets em)
```

## File: `test/functional/makehtml/cases/issues/#856.gfm-codeblock-with-language-with-spaces.html`
```html
<pre><code class="json language-json">{
    "custom": true
}
</code></pre>
<pre><code class="json language-json">{
    "custom": false
}
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/#856.gfm-codeblock-with-language-with-spaces.md`
```markdown
```json custom data
{
    "custom": true
}
```

```json custom data
{
    "custom": false
}
```
```

## File: `test/functional/makehtml/cases/issues/#96.underscores-in-links.html`
```html
<p>this is a underscore_test <img src="http://myserver.com/my_kitty.jpg" alt="my cat" /></p>
<p>another <img src="http://myserver.com/my_kitty.jpg" alt="my cat" /> underscore_test bla</p>
```

## File: `test/functional/makehtml/cases/issues/#96.underscores-in-links.md`
```markdown
this is a underscore_test ![my cat](http://myserver.com/my_kitty.jpg)

another ![my cat](http://myserver.com/my_kitty.jpg) underscore_test bla
```

## File: `test/functional/makehtml/cases/issues/crazy-urls.html`
```html
<p><img src="images(1)/cat(1).png" alt="my cat" /></p>
<p><a href="images(1)/cat(1).png">my cat</a></p>
<p><img src="some.com/crazy url with spaces" alt="foo" /></p>
<p><img src="some.com/crazy url with spaces" alt="foo" title="title" /></p>
<p><a href="some.com/crazy url with spaces">foo</a></p>
<p><a href="some.com/crazy url with spaces" title="title">foo</a></p>
<p><img src="" alt="empty" /></p>
<p><a href="">empty</a></p>
<p><img src="" alt="empty" title="title" /></p>
<p><a href="" title="title">empty</a></p>
<p><img src="" alt="empty" /></p>
<p><a href="">empty</a></p>
<p><img src="" alt="empty" title="title" /></p>
<p><a href="" title="title">empty</a></p>
<p><a href="">empty</a></p>
<p><a href="" title="title">empty</a></p>
<p><a href=""></a></p>
<p><a href=""></a></p>
<p><a href="" title="title"></a></p>
```

## File: `test/functional/makehtml/cases/issues/crazy-urls.md`
```markdown
![my cat](<images(1)/cat(1).png>)

[my cat](<images(1)/cat(1).png>)

![foo](<some.com/crazy url with spaces>)

![foo](<some.com/crazy url with spaces> "title")

[foo](<some.com/crazy url with spaces>)

[foo](<some.com/crazy url with spaces> "title")

![empty](<>)

[empty](<>)

![empty](<> "title")

[empty](<> "title")

![empty](< >)

[empty](< >)

![empty](< > "title")

[empty](< > "title")

[empty]()

[empty]("title")

[]()

[](<>)

[]("title")
```

## File: `test/functional/makehtml/cases/issues/deeply-nested-HTML-blocks.html`
```html
<div>
  <div>
    <div>
      <div>
        text
      </div>
      <div>
        text
      </div>
    </div>
  </div>
</div>
```

## File: `test/functional/makehtml/cases/issues/deeply-nested-HTML-blocks.md`
```markdown
<div>
  <div>
    <div>
      <div>
        text
      </div>
      <div>
        text
      </div>
    </div>
  </div>
</div>
```

## File: `test/functional/makehtml/cases/issues/handle-html-pre.html`
```html
<p>hmm</p>
<pre>
this is `a\_test` and this\_too and finally_this_is
</pre>
```

## File: `test/functional/makehtml/cases/issues/handle-html-pre.md`
```markdown
hmm
<pre>
this is `a\_test` and this\_too and finally_this_is
</pre>
```

## File: `test/functional/makehtml/cases/issues/one-line-HTML-input.html`
```html
<div><div>a</div><div>b</div></div>
<pre><code>&lt;div&gt;**foobar**&lt;/div&gt;
</code></pre>
```

## File: `test/functional/makehtml/cases/issues/one-line-HTML-input.md`
```markdown
<div><div>a</div><div>b</div></div>

    <div>**foobar**</div>
```

## File: `test/functional/makehtml/cases/issues/reference-link-impostors.html`
```html
<p>[We] are going to show [you]: sunshine!</p>
<p>[x]: take out the garbage<br />
[ ]: bring up the coal</p>
```

## File: `test/functional/makehtml/cases/issues/reference-link-impostors.md`
```markdown
[We] are going to show [you]: sunshine!

[x]: take out the garbage  
[ ]: bring up the coal
```

## File: `test/functional/makehtml/cases/issues/URLs-with-multiple-parenthesis.html`
```html
<p><a href="./images(1)/cat(1).png">link</a></p>
<p><a href="./images(1)/cat(1).png" title="title">link</a></p>
<p><img src="./images(1)/cat(1).png" alt="image" /></p>
<p><img src="./images(1)/cat(1).png" alt="image" title="title" /></p>
<p><img src="./images(1)/cat(1).png" alt="image" title="title" width="800" height="600" /></p>
```

## File: `test/functional/makehtml/cases/issues/URLs-with-multiple-parenthesis.md`
```markdown
[link](<./images(1)/cat(1).png>)

[link](<./images(1)/cat(1).png> "title")

![image](<./images(1)/cat(1).png>)

![image](<./images(1)/cat(1).png> "title")

![image](<./images(1)/cat(1).png> =800x600 "title")
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-hard-return-spaces.html`
```html
<p>This is a first paragraph,
on multiple lines.</p>
<p>This is a second paragraph.
There are spaces in between the two.</p>
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-hard-return-spaces.md`
```markdown
This is a first paragraph,
on multiple lines.
     
This is a second paragraph.
There are spaces in between the two.
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-hard-return.html`
```html
<p>This is a first paragraph,
on multiple lines.</p>
<p>This is a second paragraph
which has multiple lines too.</p>
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-hard-return.md`
```markdown
This is a first paragraph,
on multiple lines.

This is a second paragraph
which has multiple lines too.
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line-returns.html`
```html
<p>A first paragraph.</p>
<p>A second paragraph after 3 CR (carriage return).</p>
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line-returns.md`
```markdown
A first paragraph.



A second paragraph after 3 CR (carriage return).
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line-spaces.html`
```html
<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>
<p>A few spaces and a new long long long long long long long long long long long long long long long long paragraph on 1 line.</p>
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line-spaces.md`
```markdown
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
     
A few spaces and a new long long long long long long long long long long long long long long long long paragraph on 1 line.
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line-tab.html`
```html
<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>
<p>1 tab to separate them and a new long long long long long long long long long long long long long long long long paragraph on 1 line.</p>
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line-tab.md`
```markdown
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
	
1 tab to separate them and a new long long long long long long long long long long long long long long long long paragraph on 1 line.
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line.html`
```html
<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>
<p>A new long long long long long long long long long long long long long long long long paragraph on 1 line.</p>
```

## File: `test/functional/makehtml/cases/karlcow/2-paragraphs-line.md`
```markdown
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.

A new long long long long long long long long long long long long long long long long paragraph on 1 line.
```

## File: `test/functional/makehtml/cases/karlcow/ampersand-text-flow.html`
```html
<p>An ampersand &amp; in the text flow is escaped as an html entity.</p>
```

## File: `test/functional/makehtml/cases/karlcow/ampersand-text-flow.md`
```markdown
An ampersand & in the text flow is escaped as an html entity.
```

## File: `test/functional/makehtml/cases/karlcow/ampersand-uri.html`
```html
<p>There is an <a href="http://validator.w3.org/check?uri=http://www.w3.org/&verbose=1">ampersand</a> in the URI.</p>
```

## File: `test/functional/makehtml/cases/karlcow/ampersand-uri.md`
```markdown
There is an [ampersand](http://validator.w3.org/check?uri=http://www.w3.org/&verbose=1) in the URI.
```

## File: `test/functional/makehtml/cases/karlcow/asterisk-near-text.html`
```html
<p>This is *an asterisk which should stay as is.</p>
```

## File: `test/functional/makehtml/cases/karlcow/asterisk-near-text.md`
```markdown
This is \*an asterisk which should stay as is.
```

## File: `test/functional/makehtml/cases/karlcow/asterisk.html`
```html
<p>This is * an asterisk which should stay as is.</p>
```

## File: `test/functional/makehtml/cases/karlcow/asterisk.md`
```markdown
This is * an asterisk which should stay as is.
```

## File: `test/functional/makehtml/cases/karlcow/backslash-escape.html`
```html
<p>\   backslash
`   backtick
*   asterisk
_   underscore
{}  curly braces
[]  square brackets
()  parentheses
#   hash mark
+   plus sign
-   minus sign (hyphen)
.   dot
!   exclamation mark</p>
```

## File: `test/functional/makehtml/cases/karlcow/backslash-escape.md`
```markdown
\\   backslash
\`   backtick
\*   asterisk
\_   underscore
\{\}  curly braces
\[\]  square brackets
\(\)  parentheses
\#   hash mark
\+   plus sign
\-   minus sign (hyphen)
\.   dot
\!   exclamation mark
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-added-markup.html`
```html
<blockquote>
<h1>heading level 1</h1>
<p>paragraph</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-added-markup.md`
```markdown
> # heading level 1
> 
> paragraph
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-line-2-paragraphs.html`
```html
<blockquote>
<p>A blockquote with a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.</p>
<p>and a second very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-line-2-paragraphs.md`
```markdown
>A blockquote with a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.

>and a second very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-line.html`
```html
<blockquote>
<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a blockquote.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-line.md`
```markdown
>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a blockquote.
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline-1-space-begin.html`
```html
<blockquote>
<p>A blockquote
on multiple lines
like this.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline-1-space-begin.md`
```markdown
> A blockquote
> on multiple lines
> like this.
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline-1-space-end.html`
```html
<blockquote>
<p>A blockquote 
on multiple lines 
like this. </p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline-1-space-end.md`
```markdown
>A blockquote 
>on multiple lines 
>like this. 
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline-2-paragraphs.html`
```html
<blockquote>
<p>A blockquote
on multiple lines
like this.</p>
<p>But it has
two paragraphs.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline-2-paragraphs.md`
```markdown
>A blockquote
>on multiple lines
>like this.
>
>But it has
>two paragraphs.
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline.html`
```html
<blockquote>
<p>A blockquote
on multiple lines
like this</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-multiline.md`
```markdown
>A blockquote
>on multiple lines
>like this
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested-multiplereturn-level1.html`
```html
<blockquote>
<p>This is the first level of quoting.</p>
<blockquote>
<p>This is nested blockquote.</p>
</blockquote>
<p>Back to the first level.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested-multiplereturn-level1.md`
```markdown
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested-multiplereturn.html`
```html
<blockquote>
<p>This is the first level of quoting.</p>
<blockquote>
<p>This is nested blockquote.</p>
</blockquote>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested-multiplereturn.md`
```markdown
> This is the first level of quoting.
>
> > This is nested blockquote.
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested-return-level1.html`
```html
<blockquote>
<p>This is the first level of quoting.</p>
<blockquote>
<p>This is nested blockquote.
Back to the first level.</p>
</blockquote>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested-return-level1.md`
```markdown
> This is the first level of quoting.
> > This is nested blockquote.
> Back to the first level.
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested.html`
```html
<blockquote>
<p>This is the first level of quoting.</p>
<blockquote>
<p>This is nested blockquote.</p>
</blockquote>
</blockquote>
```

## File: `test/functional/makehtml/cases/karlcow/blockquote-nested.md`
```markdown
> This is the first level of quoting.
> > This is nested blockquote.
```

## File: `test/functional/makehtml/cases/karlcow/code-1-tab.html`
```html
<pre><code>10 PRINT HELLO INFINITE
20 GOTO 10
</code></pre>
```

## File: `test/functional/makehtml/cases/karlcow/code-1-tab.md`
```markdown
	10 PRINT HELLO INFINITE
	20 GOTO 10
```

## File: `test/functional/makehtml/cases/karlcow/code-4-spaces-escaping.html`
```html
<pre><code>10 PRINT &lt; &gt; &amp;
20 GOTO 10
</code></pre>
```

## File: `test/functional/makehtml/cases/karlcow/code-4-spaces-escaping.md`
```markdown
    10 PRINT < > &
    20 GOTO 10
```

## File: `test/functional/makehtml/cases/karlcow/code-4-spaces.html`
```html
<pre><code>10 PRINT HELLO INFINITE
20 GOTO 10
</code></pre>
```

## File: `test/functional/makehtml/cases/karlcow/code-4-spaces.md`
```markdown
    10 PRINT HELLO INFINITE
    20 GOTO 10
```

## File: `test/functional/makehtml/cases/karlcow/em-middle-word.html`
```html
<p>as<em>te</em>risks</p>
```

## File: `test/functional/makehtml/cases/karlcow/em-middle-word.md`
```markdown
as*te*risks
```

## File: `test/functional/makehtml/cases/karlcow/em-star.html`
```html
<p><em>single asterisks</em></p>
```

## File: `test/functional/makehtml/cases/karlcow/em-star.md`
```markdown
*single asterisks*
```

## File: `test/functional/makehtml/cases/karlcow/em-underscore.html`
```html
<p><em>single underscores</em></p>
```

## File: `test/functional/makehtml/cases/karlcow/em-underscore.md`
```markdown
_single underscores_
```

## File: `test/functional/makehtml/cases/karlcow/entities-text-flow.html`
```html
<p>HTML entities are written using ampersand notation: &copy;</p>
```

## File: `test/functional/makehtml/cases/karlcow/entities-text-flow.md`
```markdown
HTML entities are written using ampersand notation: &copy;
```

## File: `test/functional/makehtml/cases/karlcow/EOL-CR+LF.html`
```html
<p>These lines all end with end of line (EOL) sequences.</p>
<p>Seriously, they really do.</p>
<p>If you don't believe me: HEX EDIT!</p>
```

## File: `test/functional/makehtml/cases/karlcow/EOL-CR+LF.md`
```markdown
These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

```

## File: `test/functional/makehtml/cases/karlcow/EOL-CR.html`
```html
<p>These lines all end with end of line (EOL) sequences.</p>
<p>Seriously, they really do.</p>
<p>If you don't believe me: HEX EDIT!</p>
```

## File: `test/functional/makehtml/cases/karlcow/EOL-CR.md`
```markdown
These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

```

## File: `test/functional/makehtml/cases/karlcow/EOL-LF.html`
```html
<p>These lines all end with end of line (EOL) sequences.</p>
<p>Seriously, they really do.</p>
<p>If you don't believe me: HEX EDIT!</p>
```

## File: `test/functional/makehtml/cases/karlcow/EOL-LF.md`
```markdown
These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

```

## File: `test/functional/makehtml/cases/karlcow/header-level1-equal-underlined.html`
```html
<h1>This is an H1</h1>
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-equal-underlined.md`
```markdown
This is an H1
=============
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign-closed.html`
```html
<h1>This is an H1</h1>
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign-closed.md`
```markdown
# This is an H1 #
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign-trailing-1-space.html`
```html
<p># This is an H1</p>
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign-trailing-1-space.md`
```markdown
 # This is an H1
 
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign-trailing-2-spaces.html`
```html
<h1>this is an h1 with two trailing spaces</h1>
<p>A new paragraph.</p>
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign-trailing-2-spaces.md`
```markdown
# this is an h1 with two trailing spaces  
A new paragraph.
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign.html`
```html
<h1>This is an H1</h1>
```

## File: `test/functional/makehtml/cases/karlcow/header-level1-hash-sign.md`
```markdown
# This is an H1
```

## File: `test/functional/makehtml/cases/karlcow/header-level2-dash-underlined.html`
```html
<h2>This is an H2</h2>
```

## File: `test/functional/makehtml/cases/karlcow/header-level2-dash-underlined.md`
```markdown
This is an H2
-------------
```

## File: `test/functional/makehtml/cases/karlcow/header-level2-hash-sign-closed.html`
```html
<h2>This is an H2</h2>
```

## File: `test/functional/makehtml/cases/karlcow/header-level2-hash-sign-closed.md`
```markdown
## This is an H2 ##
```

## File: `test/functional/makehtml/cases/karlcow/header-level2-hash-sign.html`
```html
<h2>This is an H2</h2>
```

## File: `test/functional/makehtml/cases/karlcow/header-level2-hash-sign.md`
```markdown
## This is an H2
```

## File: `test/functional/makehtml/cases/karlcow/header-level3-hash-sign-closed.html`
```html
<h3>This is an H3</h3>
```

## File: `test/functional/makehtml/cases/karlcow/header-level3-hash-sign-closed.md`
```markdown
### This is an H3 ###
```

## File: `test/functional/makehtml/cases/karlcow/header-level3-hash-sign.html`
```html
<h3>This is an H3</h3>
```

## File: `test/functional/makehtml/cases/karlcow/header-level3-hash-sign.md`
```markdown
### This is an H3
```

## File: `test/functional/makehtml/cases/karlcow/header-level4-hash-sign-closed.html`
```html
<h4>This is an H4</h4>
```

## File: `test/functional/makehtml/cases/karlcow/header-level4-hash-sign-closed.md`
```markdown
#### This is an H4 ####
```

## File: `test/functional/makehtml/cases/karlcow/header-level4-hash-sign.html`
```html
<h4>This is an H4</h4>
```

## File: `test/functional/makehtml/cases/karlcow/header-level4-hash-sign.md`
```markdown
#### This is an H4
```

## File: `test/functional/makehtml/cases/karlcow/header-level5-hash-sign-closed.html`
```html
<h5>This is an H5</h5>
```

## File: `test/functional/makehtml/cases/karlcow/header-level5-hash-sign-closed.md`
```markdown
##### This is an H5 #####
```

## File: `test/functional/makehtml/cases/karlcow/header-level5-hash-sign.html`
```html
<h5>This is an H5</h5>
```

## File: `test/functional/makehtml/cases/karlcow/header-level5-hash-sign.md`
```markdown
##### This is an H5
```

## File: `test/functional/makehtml/cases/karlcow/header-level6-hash-sign-closed.html`
```html
<h6>This is an H6</h6>
```

## File: `test/functional/makehtml/cases/karlcow/header-level6-hash-sign-closed.md`
```markdown
###### This is an H6  ######
```

## File: `test/functional/makehtml/cases/karlcow/header-level6-hash-sign.html`
```html
<h6>This is an H6</h6>
```

## File: `test/functional/makehtml/cases/karlcow/header-level6-hash-sign.md`
```markdown
###### This is an H6
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-dashes-spaces.html`
```html
<hr />
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-dashes-spaces.md`
```markdown
- - -
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-dashes.html`
```html
<hr />
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-dashes.md`
```markdown
---
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-stars.html`
```html
<hr />
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-stars.md`
```markdown
***
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-underscores.html`
```html
<hr />
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-3-underscores.md`
```markdown
___
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-7-dashes.html`
```html
<hr />
```

## File: `test/functional/makehtml/cases/karlcow/horizontal-rule-7-dashes.md`
```markdown
-------
```

## File: `test/functional/makehtml/cases/karlcow/img-idref-title.html`
```html
<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" title="HTML5 for everyone" /></p>
```

## File: `test/functional/makehtml/cases/karlcow/img-idref-title.md`
```markdown
![HTML5][h5]

[h5]: http://www.w3.org/html/logo/img/mark-word-icon.png "HTML5 for everyone"
```

## File: `test/functional/makehtml/cases/karlcow/img-idref.html`
```html
<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" /></p>
```

## File: `test/functional/makehtml/cases/karlcow/img-idref.md`
```markdown
![HTML5][h5]

[h5]: http://www.w3.org/html/logo/img/mark-word-icon.png
```

## File: `test/functional/makehtml/cases/karlcow/img-title.html`
```html
<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" title="HTML5 logo for everyone" /></p>
```

## File: `test/functional/makehtml/cases/karlcow/img-title.md`
```markdown
![HTML5](http://www.w3.org/html/logo/img/mark-word-icon.png "HTML5 logo for everyone")
```

## File: `test/functional/makehtml/cases/karlcow/img.html`
```html
<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" /></p>
```

## File: `test/functional/makehtml/cases/karlcow/img.md`
```markdown
![HTML5](http://www.w3.org/html/logo/img/mark-word-icon.png)
```

## File: `test/functional/makehtml/cases/karlcow/inline-code-escaping-entities.html`
```html
<p>We love <code>&lt;code&gt; and &amp;</code> for everything</p>
```

## File: `test/functional/makehtml/cases/karlcow/inline-code-escaping-entities.md`
```markdown
We love `<code> and &` for everything
```

## File: `test/functional/makehtml/cases/karlcow/inline-code-with-visible-backtick.html`
```html
<p><code>We love `code` for everything</code></p>
```

## File: `test/functional/makehtml/cases/karlcow/inline-code-with-visible-backtick.md`
```markdown
``We love `code` for everything``
```

## File: `test/functional/makehtml/cases/karlcow/inline-code.html`
```html
<p><code>We love `code` for everything</code></p>
```

## File: `test/functional/makehtml/cases/karlcow/inline-code.md`
```markdown
``We love `code` for everything``
```

## File: `test/functional/makehtml/cases/karlcow/line-break-2-spaces.html`
```html
<p>A first sentence<br />
and a line break.</p>
```

## File: `test/functional/makehtml/cases/karlcow/line-break-2-spaces.md`
```markdown
A first sentence  
and a line break.
```

## File: `test/functional/makehtml/cases/karlcow/line-break-5-spaces.html`
```html
<p>A first sentence<br />
and a line break.</p>
```

## File: `test/functional/makehtml/cases/karlcow/line-break-5-spaces.md`
```markdown
A first sentence     
and a line break.
```

## File: `test/functional/makehtml/cases/karlcow/link-automatic.html`
```html
<p>This is an automatic link <a href="http://www.w3.org/">http://www.w3.org/</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-automatic.md`
```markdown
This is an automatic link <http://www.w3.org/>
```

## File: `test/functional/makehtml/cases/karlcow/link-bracket-paranthesis-title.html`
```html
<p><a href="http://www.w3.org/" title="Discover w3c">W3C</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-bracket-paranthesis-title.md`
```markdown
[W3C](http://www.w3.org/ "Discover w3c")
```

## File: `test/functional/makehtml/cases/karlcow/link-bracket-paranthesis.html`
```html
<p><a href="http://www.w3.org/">W3C</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-bracket-paranthesis.md`
```markdown
[W3C](http://www.w3.org/)
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-angle-bracket.html`
```html
<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-angle-bracket.md`
```markdown
[World Wide Web Consortium][w3c]

[w3c]: <http://www.w3.org/>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-implicit-spaces.html`
```html
<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-implicit-spaces.md`
```markdown
[World Wide Web Consortium][]

[World Wide Web Consortium]: http://www.w3.org/
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-implicit.html`
```html
<p><a href="http://www.w3.org/">w3c</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-implicit.md`
```markdown
[w3c][]

[w3c]: http://www.w3.org/
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-space.html`
```html
<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-space.md`
```markdown
[World Wide Web Consortium] [w3c]

[w3c]: http://www.w3.org/
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title-next-line.html`
```html
<p><a href="http://www.w3.org/" title="Discover W3C">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title-next-line.md`
```markdown
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/
   "Discover W3C"
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title-paranthesis.html`
```html
<p><a href="http://www.w3.org/" title="Discover w3c">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title-paranthesis.md`
```markdown
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ (Discover w3c)
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title-single-quote.html`
```html
<p><a href="http://www.w3.org/" title="Discover w3c">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title-single-quote.md`
```markdown
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ 'Discover w3c'
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title.html`
```html
<p><a href="http://www.w3.org/" title="Discover w3c">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref-title.md`
```markdown
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ "Discover w3c"
```

## File: `test/functional/makehtml/cases/karlcow/link-idref.html`
```html
<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>
```

## File: `test/functional/makehtml/cases/karlcow/link-idref.md`
```markdown
[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/
```

## File: `test/functional/makehtml/cases/karlcow/list-blockquote.html`
```html
<ul>
<li><p>a list containing a blockquote</p>
<blockquote>
<p>this the blockquote in the list</p>
</blockquote></li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/list-blockquote.md`
```markdown
*   a list containing a blockquote

    > this the blockquote in the list
```

## File: `test/functional/makehtml/cases/karlcow/list-code.html`
```html
<ul>
    <li><p>a list containing a block of code</p>
        <pre><code>10 PRINT HELLO INFINITE
20 GOTO 10
</code></pre></li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/list-code.md`
```markdown
*   a list containing a block of code

	    10 PRINT HELLO INFINITE
	    20 GOTO 10
```

## File: `test/functional/makehtml/cases/karlcow/list-multiparagraphs-tab.html`
```html
<ul>
<li><p>This is a list item with two paragraphs. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit. Aliquam hendrerit
mi posuere lectus.</p>
<p>Vestibulum enim wisi, viverra nec, fringilla in, laoreet
vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
sit amet velit.</p></li>
<li><p>Suspendisse id sem consectetuer libero luctus adipiscing.</p></li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/list-multiparagraphs-tab.md`
```markdown
*   This is a list item with two paragraphs. Lorem ipsum dolor
	sit amet, consectetuer adipiscing elit. Aliquam hendrerit
	mi posuere lectus.

	Vestibulum enim wisi, viverra nec, fringilla in, laoreet
	vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
	sit amet velit.

*   Suspendisse id sem consectetuer libero luctus adipiscing.
```

## File: `test/functional/makehtml/cases/karlcow/list-multiparagraphs.html`
```html
<ul>
<li><p>This is a list item with two paragraphs. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit. Aliquam hendrerit
mi posuere lectus.</p>
<p>Vestibulum enim wisi, viverra nec, fringilla in, laoreet
vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
sit amet velit.</p></li>
<li><p>Suspendisse id sem consectetuer libero luctus adipiscing.</p></li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/list-multiparagraphs.md`
```markdown
*   This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

*   Suspendisse id sem consectetuer libero luctus adipiscing.
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-escaped.html`
```html
<p>1. ordered list escape</p>
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-escaped.md`
```markdown
1\. ordered list escape
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-inner-par-list.html`
```html
<ol>
  <li><p>1</p>
    <ul>
      <li>inner par list</li></ul></li>
  <li><p>2</p></li>
</ol>
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-inner-par-list.md`
```markdown
1. 1

    - inner par list

2. 2
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-items-random-number.html`
```html
<ol>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ol>
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-items-random-number.md`
```markdown
1. list item 1
8. list item 2
1. list item 3
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-items.html`
```html
<ol>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ol>
```

## File: `test/functional/makehtml/cases/karlcow/ordered-list-items.md`
```markdown
1. list item 1
2. list item 2
3. list item 3
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-hard-return.html`
```html
<p>This is a paragraph
on multiple lines
with hard return.</p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-hard-return.md`
```markdown
This is a paragraph
on multiple lines
with hard return.
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-line.html`
```html
<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-line.md`
```markdown
This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-trailing-leading-spaces.html`
```html
<p>This is a paragraph with a trailing and leading space. </p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-trailing-leading-spaces.md`
```markdown
 This is a paragraph with a trailing and leading space. 
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-trailing-tab.html`
```html
<p>This is a paragraph with 1 trailing tab.    </p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraph-trailing-tab.md`
```markdown
This is a paragraph with 1 trailing tab.	
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-2-leading-spaces.html`
```html
<p>This is a paragraph with 2 leading spaces.</p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-2-leading-spaces.md`
```markdown
  This is a paragraph with 2 leading spaces.
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-3-leading-spaces.html`
```html
<p>This is a paragraph with 3 leading spaces.</p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-3-leading-spaces.md`
```markdown
   This is a paragraph with 3 leading spaces.
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-leading-space.html`
```html
<p>This is a paragraph with 1 leading space.</p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-leading-space.md`
```markdown
 This is a paragraph with 1 leading space.
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-trailing-spaces.html`
```html
<p>This is a paragraph with a trailing space. </p>
```

## File: `test/functional/makehtml/cases/karlcow/paragraphs-trailing-spaces.md`
```markdown
This is a paragraph with a trailing space. 
```

## File: `test/functional/makehtml/cases/karlcow/strong-middle-word.html`
```html
<p>as<strong>te</strong>risks</p>
```

## File: `test/functional/makehtml/cases/karlcow/strong-middle-word.md`
```markdown
as**te**risks
```

## File: `test/functional/makehtml/cases/karlcow/strong-star.html`
```html
<p><strong>double asterisks</strong></p>
```

## File: `test/functional/makehtml/cases/karlcow/strong-star.md`
```markdown
**double asterisks**
```

## File: `test/functional/makehtml/cases/karlcow/strong-underscore.html`
```html
<p><strong>double underscores</strong></p>
```

## File: `test/functional/makehtml/cases/karlcow/strong-underscore.md`
```markdown
__double underscores__
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-asterisk.html`
```html
<ul>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-asterisk.md`
```markdown
* list item 1
* list item 2
* list item 3
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-dashsign.html`
```html
<ul>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-dashsign.md`
```markdown
- list item 1
- list item 2
- list item 3
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-leading-1space.html`
```html
<ul>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-leading-1space.md`
```markdown
 * list item 1
 * list item 2
 * list item 3
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-leading-2spaces.html`
```html
<ul>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-leading-2spaces.md`
```markdown
  * list item 1
  * list item 2
  * list item 3
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-leading-3spaces.html`
```html
<ul>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-leading-3spaces.md`
```markdown
   * list item 1
   * list item 2
   * list item 3
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-plussign.html`
```html
<ul>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-items-plussign.md`
```markdown
+ list item 1
+ list item 2
+ list item 3
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-paragraphs.html`
```html
<ul>
<li><p>list item in paragraph</p></li>
<li><p>another list item in paragraph</p></li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-paragraphs.md`
```markdown
* list item in paragraph

* another list item in paragraph
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-unindented-content.html`
```html
<ul>
<li>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a list.</li>
<li>and yet another long long long long long long long long long long long long long long long long long long long long long long line.</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-unindented-content.md`
```markdown
*   This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a list.
*   and yet another long long long long long long long long long long long long long long long long long long long long long long line.
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-with-indented-content.html`
```html
<ul>
<li>This is a list item
with the content on
multiline and indented.</li>
<li>And this another list item
with the same principle.</li>
</ul>
```

## File: `test/functional/makehtml/cases/karlcow/unordered-list-with-indented-content.md`
```markdown
*   This is a list item
    with the content on
    multiline and indented.
*   And this another list item
    with the same principle.
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-fragments.html`
```html
<p><a href="#Declare">Declare options</a></p>
<p><a href="#Declare%20current%20operation%20options">Declare options</a></p>
<p><a href="#Declare current operation options">Declare options</a></p>
<p><a href="https://spec.commonmark.org/0.30/#example-500">Common Mark Example</a></p>
<p><a href="spec.commonmark.org/0.30/#example-500">Common Mark Example</a></p>
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-fragments.md`
```markdown
[Declare options](#Declare)

[Declare options](#Declare%20current%20operation%20options)

[Declare options](<#Declare current operation options>)

[Common Mark Example](https://spec.commonmark.org/0.30/#example-500)

[Common Mark Example](spec.commonmark.org/0.30/#example-500)
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-javacript-identifiers.html`
```html
<p>Reserved Keywords found at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar</p>
<p><a href="">break</a></p>
<p><a href="">case</a></p>
<p><a href="">catch</a></p>
<p><a href="">class</a></p>
<p><a href="">const</a></p>
<p><a href="">continue</a></p>
<p><a href="">debugger</a></p>
<p><a href="">default</a></p>
<p><a href="">delete</a></p>
<p><a href="">do</a></p>
<p><a href="">else</a></p>
<p><a href="">export</a></p>
<p><a href="">extends</a></p>
<p><a href="">finally</a></p>
<p><a href="">for</a></p>
<p><a href="">function</a></p>
<p><a href="">if</a></p>
<p><a href="">import</a></p>
<p><a href="">in</a></p>
<p><a href="">instanceof</a></p>
<p><a href="">new</a></p>
<p><a href="">return</a></p>
<p><a href="">super</a></p>
<p><a href="">switch</a></p>
<p><a href="">this</a></p>
<p><a href="">throw</a></p>
<p><a href="">try</a></p>
<p><a href="">typeof</a></p>
<p><a href="">var</a></p>
<p><a href="">void</a></p>
<p><a href="">while</a></p>
<p><a href="">with</a></p>
<p><a href="">yield</a></p>
<p><a href="">enum</a></p>
<p><a href="">implements</a></p>
<p><a href="">interface</a></p>
<p><a href="">let</a></p>
<p><a href="">package</a></p>
<p><a href="">private</a></p>
<p><a href="">protected</a></p>
<p><a href="">public</a></p>
<p><a href="">static</a></p>
<p><a href="">yield</a></p>
<p><a href="">await</a></p>
<p><a href="">abstract</a></p>
<p><a href="">boolean</a></p>
<p><a href="">byte</a></p>
<p><a href="">char</a></p>
<p><a href="">double</a></p>
<p><a href="">final</a></p>
<p><a href="">float</a></p>
<p><a href="">goto</a></p>
<p><a href="">int</a></p>
<p><a href="">long</a></p>
<p><a href="">native</a></p>
<p><a href="">short</a></p>
<p><a href="">synchronized</a></p>
<p><a href="">throws</a></p>
<p><a href="">transient</a></p>
<p><a href="">volatile</a></p>
<p><a href="">null</a></p>
<p><a href="">true</a></p>
<p><a href="">false</a></p>
<p><a href="">arguments</a></p>
<p><a href="">get</a></p>
<p><a href="">set</a></p>
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-javacript-identifiers.md`
```markdown
Reserved Keywords found at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar

[break]()

[case]()

[catch]()

[class]()

[const]()

[continue]()

[debugger]()

[default]()

[delete]()

[do]()

[else]()

[export]()

[extends]()

[finally]()

[for]()

[function]()

[if]()

[import]()

[in]()

[instanceof]()

[new]()

[return]()

[super]()

[switch]()

[this]()

[throw]()

[try]()

[typeof]()

[var]()

[void]()

[while]()

[with]()

[yield]()

[enum]()

[implements]()

[interface]()

[let]()

[package]()

[private]()

[protected]()

[public]()

[static]()

[yield]()

[await]()

[abstract]()

[boolean]()

[byte]()

[char]()

[double]()

[final]()

[float]()

[goto]()

[int]()

[long]()

[native]()

[short]()

[synchronized]()

[throws]()

[transient]()

[volatile]()

[null]()

[true]()

[false]()

[arguments]()

[get]()

[set]()
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-no-protocols.html`
```html
<p><a href="/uri">link</a></p>
<p><a href="http://example.com/">link</a></p>
<p><a href="http://example.com">link</a></p>
<p><a href="https://example.com">link</a></p>
<p><a href="https://example.com/">link</a></p>
<p><a href="example.com">link</a></p>
<p><a href="www.example.com">link</a></p>
<p><a href="file://example.com">link</a></p>
<p><a href="file://www.example.com">link</a></p>
<p><a href="example.jpg">link</a></p>
<p><a href="example.io">link</a></p>
<p><a href="http://baidu.com" title="百度">百度</a></p>
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-no-protocols.md`
```markdown
[link](/uri)

[link](http://example.com/)

[link](http://example.com)

[link](https://example.com)

[link](https://example.com/)

[link](example.com)

[link](www.example.com)

[link](file://example.com)

[link](file://www.example.com)

[link](example.jpg)

[link](example.io)

[百度](http://baidu.com "百度")
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-object-property-names.html`
```html
<p>Object property names found at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object</p>
<p><a href="">assign</a></p>
<p><a href="">create</a></p>
<p><a href="">defineProperty</a></p>
<p><a href="">defineProperties</a></p>
<p><a href="">entries</a></p>
<p><a href="">freeze</a></p>
<p><a href="">fromEntries</a></p>
<p><a href="">getOwnPropertyDescriptor</a></p>
<p><a href="">getOwnPropertyDescriptors</a></p>
<p><a href="">getOwnPropertyNames</a></p>
<p><a href="">getOwnPropertySymbols</a></p>
<p><a href="">getPrototypeOf</a></p>
<p><a href="">is</a></p>
<p><a href="">isExtensible</a></p>
<p><a href="">isFrozen</a></p>
<p><a href="">isSealed</a></p>
<p><a href="">keys</a></p>
<p><a href="">preventExtensions</a></p>
<p><a href="">seal</a></p>
<p><a href="">setPrototypeOf</a></p>
<p><a href="">values</a></p>
<p><a href="">prototype.constructor</a></p>
<p><a href="">prototype.<strong>proto</strong></a></p>
<p><a href="">prototype.<strong>defineGetter</strong></a></p>
<p><a href="">prototype.<strong>defineSetter</strong></a></p>
<p><a href="">prototype.<strong>lookupGetter</strong></a></p>
<p><a href="">prototype.<strong>lookupSetter</strong></a></p>
<p><a href="">prototype.hasOwnProperty</a></p>
<p><a href="">prototype.isPrototypeOf</a></p>
<p><a href="">prototype.propertyIsEnumerable</a></p>
<p><a href="">prototype.toLocaleString</a></p>
<p><a href="">prototype.toString</a></p>
<p><a href="">prototype.valueOf</a></p>
<p><a href="">constructor</a></p>
<p><a href=""><strong>proto</strong></a></p>
<p><a href=""><strong>defineGetter</strong></a></p>
<p><a href=""><strong>defineSetter</strong></a></p>
<p><a href=""><strong>lookupGetter</strong></a></p>
<p><a href=""><strong>lookupSetter</strong></a></p>
<p><a href="">hasOwnProperty</a></p>
<p><a href="">isPrototypeOf</a></p>
<p><a href="">propertyIsEnumerable</a></p>
<p><a href="">toLocaleString</a></p>
<p><a href="">toString</a></p>
<p><a href="">valueOf</a></p>
```

## File: `test/functional/makehtml/cases/standard/anchors-allow-object-property-names.md`
```markdown
Object property names found at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object

[assign]()

[create]()

[defineProperty]()

[defineProperties]()

[entries]()

[freeze]()

[fromEntries]()

[getOwnPropertyDescriptor]()

[getOwnPropertyDescriptors]()

[getOwnPropertyNames]()

[getOwnPropertySymbols]()

[getPrototypeOf]()

[is]()

[isExtensible]()

[isFrozen]()

[isSealed]()

[keys]()

[preventExtensions]()

[seal]()

[setPrototypeOf]()

[values]()

[prototype.constructor]()

[prototype.__proto__]()

[prototype.__defineGetter__]()

[prototype.__defineSetter__]()

[prototype.__lookupGetter__]()

[prototype.__lookupSetter__]()

[prototype.hasOwnProperty]()

[prototype.isPrototypeOf]()

[prototype.propertyIsEnumerable]()

[prototype.toLocaleString]()

[prototype.toString]()

[prototype.valueOf]()

[constructor]()

[__proto__]()

[__defineGetter__]()

[__defineSetter__]()

[__lookupGetter__]()

[__lookupSetter__]()

[hasOwnProperty]()

[isPrototypeOf]()

[propertyIsEnumerable]()

[toLocaleString]()

[toString]()

[valueOf]()
```

## File: `test/functional/makehtml/cases/standard/anchors-by-reference.html`
```html
<p>This is <a href="http://example.com/" title="Optional Title Here">an example</a> reference-style link.
  This is <a href="http://example.com/" title="Optional Title Here">another</a> reference-style link.
  This is <a href="http://example.com/" title="Optional Title Here">a third</a> reference-style link.
  This is <a href="http://example.com/" title="Optional Title Here">a fourth</a> reference-style link.</p>
```

## File: `test/functional/makehtml/cases/standard/anchors-by-reference.md`
```markdown

This is [an example][id] reference-style link.
This is [another] [foo] reference-style link.
This is [a third][bar] reference-style link.
This is [a fourth][4] reference-style link.

  [id]: http://example.com/  "Optional Title Here"
  [foo]: http://example.com/  (Optional Title Here)
  [bar]: http://example.com/  (Optional Title Here)
  [4]: <http://example.com/>
    "Optional Title Here"
```

## File: `test/functional/makehtml/cases/standard/anchors-followed-by-brakets.html`
```html
<p>This is a <a href="https://en.wikipedia.org/wiki/Textile">link</a> (some other text)</p>
<p>This is a <a href="https://en.wikipedia.org/wiki/Textile_(markup">link</a> (some other text)</p>
<p>This is a <a href="https://en.wikipedia.org/wiki/Textile_(markup_language)">link</a> (some other text)</p>
<p>This is a <a href="https://en.wikipedia.org/wiki/Textile_(markup_language)/foo">link</a> (some other text)</p>
```

## File: `test/functional/makehtml/cases/standard/anchors-followed-by-brakets.md`
```markdown
This is a [link](https://en.wikipedia.org/wiki/Textile) (some other text)

This is a [link](https://en.wikipedia.org/wiki/Textile_(markup) (some other text)

This is a [link](https://en.wikipedia.org/wiki/Textile_(markup_language)) (some other text)

This is a [link](https://en.wikipedia.org/wiki/Textile_(markup_language)/foo) (some other text)
```

## File: `test/functional/makehtml/cases/standard/automatic-anchors.html`
```html
<p><a href="http://example.com/">http://example.com/</a></p>
```

## File: `test/functional/makehtml/cases/standard/automatic-anchors.md`
```markdown

<http://example.com/>
```

## File: `test/functional/makehtml/cases/standard/blockquote-followed-by-code.html`
```html
<blockquote>
    <p>a blockquote
with a 4 space indented line (not code)</p>
</blockquote>
<p>sep</p>
<blockquote>
    <p>a blockquote</p>
</blockquote>
<pre><code>with some code after
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/blockquote-followed-by-code.md`
```markdown
> a blockquote
    with a 4 space indented line (not code)

sep

> a blockquote

    with some code after
```

## File: `test/functional/makehtml/cases/standard/blockquote-inside-code.html`
```html
<pre><code>&gt; this is a pseudo blockquote
    &gt; inside a code block
</code></pre>
<p>foo</p>
<pre><code>&gt; this is another bq
    inside code
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/blockquote-inside-code.md`
```markdown
    > this is a pseudo blockquote
    > inside a code block

foo

    > this is another bq
    inside code
```

## File: `test/functional/makehtml/cases/standard/blockquote-nested-markdown.html`
```html
<blockquote>
  <h2 id="thisisaheader">This is a header.</h2>
  <ol>
    <li>This is the first list item.</li>
    <li>This is the second list item.</li>
  </ol>
  <p>Here's some example code:</p>
    <pre><code>return shell_exec("echo $input | $markdown_script");
    </code></pre>
</blockquote>
```

## File: `test/functional/makehtml/cases/standard/blockquote-nested-markdown.md`
```markdown
> ## This is a header.
>
> 1.   This is the first list item.
> 2.   This is the second list item.
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");
```

## File: `test/functional/makehtml/cases/standard/blockquote.html`
```html
<blockquote>
  <p>This is a multi line blockquote test</p>
  <p>With more than one line.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/standard/blockquote.md`
```markdown
  
  > This is a multi line blockquote test
  >
  > With more than one line.
```

## File: `test/functional/makehtml/cases/standard/code-block-html-escape.html`
```html
<p>This is some HTML:</p>
<pre><code>&lt;h1&gt;Heading&lt;/h1&gt;
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/code-block-html-escape.md`
```markdown

This is some HTML:

    <h1>Heading</h1>
```

## File: `test/functional/makehtml/cases/standard/code-block-with-special-chars.html`
```html
<pre><code>//**this** code _has_ special chars
var arr = ['foo', 'bar', 'baz'];
function () {
    return 'foo';
}
\n
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/code-block-with-special-chars.md`
```markdown
    //**this** code _has_ special chars
    var arr = ['foo', 'bar', 'baz'];
    function () {
        return 'foo';
    }
    \n
```

## File: `test/functional/makehtml/cases/standard/code-block.html`
```html
<p>This is a normal paragraph:</p>
<pre><code>This is a code block.
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/code-block.md`
```markdown

This is a normal paragraph:

    This is a code block.
```

## File: `test/functional/makehtml/cases/standard/double-emphasis.html`
```html
<p>a <strong><em>strong and em</em></strong> thingy</p>
<p>bar<strong><em>bazinga</em></strong>bar</p>
<p>a <strong><em>strong and em</em></strong> thingy</p>
<p>bar<strong><em>bazinga</em></strong>bar</p>
```

## File: `test/functional/makehtml/cases/standard/double-emphasis.md`
```markdown
a ___strong and em___ thingy

bar___bazinga___bar

a ***strong and em*** thingy

bar***bazinga***bar
```

## File: `test/functional/makehtml/cases/standard/doubline-list.html`
```html
<ul>
  <li><p>Bird</p></li>
  <li><p>Magic</p></li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/doubline-list.md`
```markdown

 *  Bird

 *  Magic
```

## File: `test/functional/makehtml/cases/standard/ellipsis.html`
```html
<p>ellipsis in text…</p>
<p>…</p>
<ol>
    <li>foo…</li>
    <li>bar</li>
</ol>
<blockquote>
    <p>ellipsis in blockquote…</p>
</blockquote>
<pre><code>ellipsis in code...
</code></pre>
<pre><code>ellipsis in code...
</code></pre>
<h1 id="ellipsisinheader">ellipsis in header…</h1>
<p>1…</p>
<ol>
    <li>..</li>
</ol>
<p>1…</p>
<p><a href="https://gitlab.com/gitlab-org/gitlab-ce/compare/v11.5.4...v11.5.5" title="title">Link</a></p>
```

## File: `test/functional/makehtml/cases/standard/ellipsis.md`
```markdown
ellipsis in text...

...

1. foo...
2. bar

> ellipsis in blockquote...

```
ellipsis in code...
```

    ellipsis in code...

# ellipsis in header...

1...

1. ..

1...

[Link](https://gitlab.com/gitlab-org/gitlab-ce/compare/v11.5.4...v11.5.5 "title")
```

## File: `test/functional/makehtml/cases/standard/emphasis-inside-inline-code.html`
```html
<p>some text <code>**foo**</code></p>
```

## File: `test/functional/makehtml/cases/standard/emphasis-inside-inline-code.md`
```markdown
some text `**foo**`
```

## File: `test/functional/makehtml/cases/standard/emphasis.html`
```html
<p><em>single asterisks</em></p>
<p><em>single underscores</em></p>
<p><strong>double asterisks</strong></p>
<p><strong>double underscores</strong></p>
<p>text <em>with italic sentence</em> in middle</p>
<p>text <strong>with bold sentence</strong> in middle</p>
<p>text with <strong>bold text that
  spans across multiple</strong> lines</p>
<p>underscored_word</p>
<p>doubleunderscore__word</p>
<p>asterix*word</p>
<p>doubleasterix**word</p>
<p>line with_underscored word</p>
<p>line with__doubleunderscored word</p>
<p>line with*asterixed word</p>
<p>line with**doubleasterixed word</p>
<p>some line<em>with</em>inner underscores</p>
<p>some line<strong>with</strong>inner double underscores</p>
<p>some line<em>with</em>inner asterixs</p>
<p>some line<strong>with</strong>inner double asterixs</p>
<p>another line with just _one underscore</p>
<p>another line with just __one double underscore</p>
<p>another line with just *one asterix</p>
<p>another line with just **one double asterix</p>
<p>a sentence with<em>underscore and another</em>underscore</p>
<p>a sentence with<strong>doubleunderscore and another</strong>doubleunderscore</p>
<p>a sentence with<em>asterix and another</em>asterix</p>
<p>a sentence with<strong>doubleasterix and another</strong>doubleasterix</p>
<p>escaped word_with_underscores</p>
<p>escaped word__with__double underscores</p>
<p>escaped word<em>_with_</em>single italic underscore</p>
<p>escaped word*with*asterixs</p>
<p>escaped word**with**asterixs</p>
<p>escaped word<strong>*with*</strong>bold asterixs</p>
<p>foo<strong>bar</strong>baz</p>
<p>foo<strong>bar</strong>baz</p>
<p>this is <strong><a href="//google.com">imbued link with strong</a></strong></p>
<p>this is <strong><a href="//google.com">imbued link with strong</a></strong></p>
<p>this link has underscore <a href="http://www.google.com/some_link">some_link</a></p>
<p><strong><em>multiple</em></strong> italics and bolds with underscores in a <strong><em>paragraph</em></strong></p>
<p><strong><em>multiple</em></strong> italics and bolds with asterisks in a <strong><em>paragraph</em></strong></p>
<p><strong>multiple</strong> bolds with underscores in a <strong>paragraph</strong></p>
<p><strong>multiple</strong> bolds with asterisks in a <strong>paragraph</strong></p>
<p><em>multiple</em> italics with underscores in a <em>paragraph</em></p>
<p><em>multiple</em> italics with asterisks in a <em>paragraph</em></p>
```

## File: `test/functional/makehtml/cases/standard/emphasis.md`
```markdown
*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

text *with italic sentence* in middle

text __with bold sentence__ in middle

text with __bold text that
spans across multiple__ lines

underscored_word

doubleunderscore__word

asterix*word

doubleasterix**word

line with_underscored word

line with__doubleunderscored word

line with*asterixed word

line with**doubleasterixed word

some line_with_inner underscores

some line__with__inner double underscores

some line*with*inner asterixs

some line**with**inner double asterixs

another line with just _one underscore

another line with just __one double underscore

another line with just *one asterix

another line with just **one double asterix

a sentence with_underscore and another_underscore

a sentence with__doubleunderscore and another__doubleunderscore

a sentence with*asterix and another*asterix

a sentence with**doubleasterix and another**doubleasterix

escaped word\_with\_underscores

escaped word\_\_with\_\_double underscores

escaped word_\_with\__single italic underscore

escaped word\*with*asterixs

escaped word\*\*with\*\*asterixs

escaped word**\*with\***bold asterixs

foo**bar**baz

foo__bar__baz

this is **<a href="//google.com">imbued link with strong</a>**

this is __<a href="//google.com">imbued link with strong</a>__

this link has underscore [some_link](http://www.google.com/some_link)

___multiple___ italics and bolds with underscores in a ___paragraph___

***multiple*** italics and bolds with asterisks in a ***paragraph***

__multiple__ bolds with underscores in a __paragraph__

**multiple** bolds with asterisks in a **paragraph**

_multiple_ italics with underscores in a _paragraph_

_multiple_ italics with asterisks in a _paragraph_
```

## File: `test/functional/makehtml/cases/standard/encodeHTMLCodeTags.html`
```html
<p>this is code <code>some &lt;span&gt;text&lt;/span&gt;</code> yeah!</p>
<pre><code>
&lt;div&gt;foo&lt;/div&gt;
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/encodeHTMLCodeTags.md`
```markdown
this is code <code>some <span>text</span></code> yeah!

<pre><code>
<div>foo</div>
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/escaped-number-period.html`
```html
<p>It happened in 1986. What a great season.</p>
```

## File: `test/functional/makehtml/cases/standard/escaped-number-period.md`
```markdown
It happened in 1986\. What a great season.
```

## File: `test/functional/makehtml/cases/standard/escaping.html`
```html
<p>These should all be escaped:</p>
<p>\</p>
<p>`</p>
<p>*</p>
<p>_</p>
<p>{</p>
<p>}</p>
<p>[</p>
<p>]</p>
<p>(</p>
<p>)</p>
<p>#</p>
<p>+</p>
<p>-</p>
<p>.</p>
<p>!</p>
```

## File: `test/functional/makehtml/cases/standard/escaping.md`
```markdown

These should all be escaped:

\\

\`

\*

\_

\{

\}

\[

\]

\(

\)

\#

\+

\-

\.

\!
```

## File: `test/functional/makehtml/cases/standard/github-style-at-start.html`
```html
<pre><code>function MyFunc(a) {
  // ...
  }
</code></pre>
<p>That is some code!</p>
```

## File: `test/functional/makehtml/cases/standard/github-style-at-start.md`
```markdown
```
function MyFunc(a) {
    // ...
}
```

That is some code!
```

## File: `test/functional/makehtml/cases/standard/github-style-codeblock-inside-quote.html`
```html
<blockquote>
<p>Define a function in javascript:</p>
<pre><code>function MyFunc(a) {
  var s = '`';
  }
</code></pre>
<blockquote>
<p>And some nested quote</p>
<pre><code class="html language-html">&lt;div&gt;HTML!&lt;/div&gt;
</code></pre>
</blockquote>
</blockquote>
```

## File: `test/functional/makehtml/cases/standard/github-style-codeblock-inside-quote.md`
```markdown
> Define a function in javascript:
>
> ```
> function MyFunc(a) {
>     var s = '`';
> }
> ```
>
>> And some nested quote
>>
>> ```html
>> <div>HTML!</div>
>> ```
```

## File: `test/functional/makehtml/cases/standard/github-style-codeblock.html`
```html
<p>Define a function in javascript:</p>
<pre><code>function MyFunc(a) {
  var s = '`';
  }
</code></pre>
<p>And some HTML</p>
<pre><code class="html language-html">&lt;div&gt;HTML!&lt;/div&gt;
</code></pre>
<p>And some CSS with spaces before the language declaration</p>
<pre><code class="css language-css">body {
font-size: 1.5em;
}
</code></pre>
<p>Use more than 3 backticks</p>
<pre><code>some code
</code></pre>
<p>Use tilde as delimiter</p>
<pre><code>another piece of code
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/github-style-codeblock.md`
```markdown

Define a function in javascript:

```
function MyFunc(a) {
    var s = '`';
}
```

And some HTML

```html
<div>HTML!</div>
```

And some CSS with spaces before the language declaration

```    css
body {
    font-size: 1.5em;
}
```

Use more than 3 backticks

`````
some code
`````

Use tilde as delimiter

~~~
another piece of code
~~~
```

## File: `test/functional/makehtml/cases/standard/github-style-linebreaks.html`
```html
<pre><code>code can go here
  this is rendered on a second line
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/github-style-linebreaks.md`
```markdown
```
code can go here
this is rendered on a second line
```
```

## File: `test/functional/makehtml/cases/standard/h1-with-double-hash.html`
```html
<h1 id="thisisanh1">This is an H1</h1>
```

## File: `test/functional/makehtml/cases/standard/h1-with-double-hash.md`
```markdown
# This is an H1 #
```

## File: `test/functional/makehtml/cases/standard/h1-with-equals.html`
```html
<h1 id="thisisanh1">This is an H1</h1>
```

## File: `test/functional/makehtml/cases/standard/h1-with-equals.md`
```markdown
This is an H1
=============
```

## File: `test/functional/makehtml/cases/standard/h1-with-single-hash.html`
```html
<h1 id="thisisanh1">This is an H1</h1>
```

## File: `test/functional/makehtml/cases/standard/h1-with-single-hash.md`
```markdown
# This is an H1
```

## File: `test/functional/makehtml/cases/standard/h2-with-dashes.html`
```html
<h2 id="thisisanh2">This is an H2</h2>
```

## File: `test/functional/makehtml/cases/standard/h2-with-dashes.md`
```markdown
This is an H2
-------------
```

## File: `test/functional/makehtml/cases/standard/h2-with-double-hash.html`
```html
<h2 id="thisisanh2">This is an H2</h2>
```

## File: `test/functional/makehtml/cases/standard/h2-with-double-hash.md`
```markdown
## This is an H2 ##
```

## File: `test/functional/makehtml/cases/standard/h2-with-single-hash.html`
```html
<h2 id="thisisanh2">This is an H2</h2>
```

## File: `test/functional/makehtml/cases/standard/h2-with-single-hash.md`
```markdown
## This is an H2
```

## File: `test/functional/makehtml/cases/standard/h3-with-double-hash.html`
```html
<h3 id="thisisanh3">This is an H3</h3>
```

## File: `test/functional/makehtml/cases/standard/h3-with-double-hash.md`
```markdown
### This is an H3 ###
```

## File: `test/functional/makehtml/cases/standard/h3-with-single-hash.html`
```html
<h3 id="thisisanh3">This is an H3</h3>
```

## File: `test/functional/makehtml/cases/standard/h3-with-single-hash.md`
```markdown
### This is an H3
```

## File: `test/functional/makehtml/cases/standard/h4-with-single-hash.html`
```html
<h4 id="thisisanh4">This is an H4</h4>
```

## File: `test/functional/makehtml/cases/standard/h4-with-single-hash.md`
```markdown
#### This is an H4
```

## File: `test/functional/makehtml/cases/standard/h5-with-single-hash.html`
```html
<h5 id="thisisanh5">This is an H5</h5>
```

## File: `test/functional/makehtml/cases/standard/h5-with-single-hash.md`
```markdown
##### This is an H5
```

## File: `test/functional/makehtml/cases/standard/h6-with-single-hash.html`
```html
<h6 id="thisisanh6">This is an H6</h6>
```

## File: `test/functional/makehtml/cases/standard/h6-with-single-hash.md`
```markdown
###### This is an H6
```

## File: `test/functional/makehtml/cases/standard/horizontal-rules.html`
```html
<hr />
<hr />
<hr />
<hr />
<hr />
```

## File: `test/functional/makehtml/cases/standard/horizontal-rules.md`
```markdown

* * *

***

*****

- - -

---------------------------------------
```

## File: `test/functional/makehtml/cases/standard/html-comments.html`
```html
<!-- a comment -->
<!-- a comment with *bogus* __markdown__ inside -->
<p>words <!-- a comment --> words</p>
<!-- comment -->
<p>words</p>
   <!-- comment -->
<pre><code>&lt;!-- comment --&gt;
</code></pre>
<p>&lt;!----------------------------------------------------------------------------------------------------------------------------------------------------</p>
<!-------------------------------------------------------------------->
```

## File: `test/functional/makehtml/cases/standard/html-comments.md`
```markdown
<!-- a comment -->

<!-- a comment with *bogus* __markdown__ inside -->

words <!-- a comment --> words

<!-- comment --> words

   <!-- comment -->

    <!-- comment -->

<!----------------------------------------------------------------------------------------------------------------------------------------------------

<!-------------------------------------------------------------------->
```

## File: `test/functional/makehtml/cases/standard/html-inside-listed-code.html`
```html
<ul>
    <li><p>list item 1</p>
<pre><code class="html language-html">&lt;a href="www.google.com"&gt;google&lt;/a&gt;
&lt;div&gt;
&lt;div&gt;some div&lt;/div&gt;
&lt;/div&gt;
</code></pre></li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/html-inside-listed-code.md`
```markdown
  - list item 1

    ```html
    <a href="www.google.com">google</a>
    <div>
      <div>some div</div>
    </div>
    ```
```

## File: `test/functional/makehtml/cases/standard/html5-strutural-tags.html`
```html
<p>These HTML5 tags should pass through just fine.</p>
<section>hello</section>
<header>head</header>
<footer>footsies</footer>
<nav>navigation</nav>
<article>read me</article>
<aside>ignore me</aside>
<article>read
  me</article>
<aside>
  ignore me
</aside>
<p>the end</p>
<table class="test">
  <tr>
    <td>Foo</td>
  </tr>
  <tr>
    <td>Bar</td>
  </tr>
</table>
<table class="test">
  <thead>
  <tr>
    <td>Foo</td>
  </tr>
  </thead>
  <tr>
    <td>Bar</td>
  </tr>
  <tfoot>
  <tr>
    <td>Bar</td>
  </tr>
  </tfoot>
</table>
<audio class="podcastplayer" controls>
  <source src="foobar.mp3" type="audio/mp3" preload="none"></source>
  <source src="foobar.off" type="audio/ogg" preload="none"></source>
</audio>
<video src="foo.ogg">
  <track kind="subtitles" src="foo.en.vtt" srclang="en" label="English">
  <track kind="subtitles" src="foo.sv.vtt" srclang="sv" label="Svenska">
</video>
<address>My street</address>
<canvas id="canvas" width="300" height="300">
  Sorry, your browser doesn't support the &lt;canvas&gt; element.
</canvas>
<figure>
  <img src="mypic.png" alt="An awesome picture">
  <figcaption>Caption for the awesome picture</figcaption>
</figure>
<hgroup>
  <h1>Main title</h1>
  <h2>Secondary title</h2>
</hgroup>
<output name="result"></output>
<details>
  <summary>Summarise me</summary>
  <p>Explain the details</p>
</details>
```

## File: `test/functional/makehtml/cases/standard/html5-strutural-tags.md`
```markdown
These HTML5 tags should pass through just fine.

<section>hello</section>
<header>head</header>
<footer>footsies</footer>
<nav>navigation</nav>
<article>read me</article>
<aside>ignore me</aside>
<article>read
me</article>
<aside>
ignore me
</aside>

the end

<table class="test">
    <tr>
        <td>Foo</td>
    </tr>
    <tr>
        <td>Bar</td>
    </tr>
</table>

<table class="test">
    <thead>
        <tr>
            <td>Foo</td>
        </tr>
    </thead>
    <tr>
        <td>Bar</td>
    </tr>
    <tfoot>
        <tr>
            <td>Bar</td>
        </tr>
    </tfoot>
</table>

<audio class="podcastplayer" controls>
    <source src="foobar.mp3" type="audio/mp3" preload="none"></source>
    <source src="foobar.off" type="audio/ogg" preload="none"></source>
</audio>

<video src="foo.ogg">
    <track kind="subtitles" src="foo.en.vtt" srclang="en" label="English">
    <track kind="subtitles" src="foo.sv.vtt" srclang="sv" label="Svenska">
</video>

<address>My street</address>

<canvas id="canvas" width="300" height="300">
    Sorry, your browser doesn't support the &lt;canvas&gt; element.
</canvas>

<figure>
    <img src="mypic.png" alt="An awesome picture">
    <figcaption>Caption for the awesome picture</figcaption>
</figure>

<hgroup>
  <h1>Main title</h1>
  <h2>Secondary title</h2>
</hgroup>

<output name="result"></output>

<details>
  <summary>Summarise me</summary>
  <p>Explain the details</p>
</details>
```

## File: `test/functional/makehtml/cases/standard/images-followed-by-brackets.html`
```html
<p><img src="./image/cat1.png" alt="image link" />(some text between brackets)</p>
<p><img src="./image/cat(1).png" alt="image link" />(some text between brackets)</p>
```

## File: `test/functional/makehtml/cases/standard/images-followed-by-brackets.md`
```markdown
![image link](<./image/cat1.png>)(some text between brackets)

![image link](<./image/cat(1).png>)(some text between brackets)
```

## File: `test/functional/makehtml/cases/standard/images.html`
```html
<p><img src="/path/to/img.jpg" alt="Alt text" /></p>
<p><img src="/path/to/img.jpg" alt="Alt text" title="Optional title" /></p>
<p><img src="url/to/image.jpg" alt="Alt text" title="Optional title attribute" /></p>
<p><img src="url/to/image2.jpg" alt="My Image" title="Optional title attribute" /></p>
<p>![leave me alone]</p>
<p>![leave me alone][]</p>
```

## File: `test/functional/makehtml/cases/standard/images.md`
```markdown
![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")

![Alt text][id]

![My Image]

![leave me alone]

![leave me alone][]

  [id]: url/to/image.jpg  "Optional title attribute"
  [My Image]: url/to/image2.jpg "Optional title attribute"
```

## File: `test/functional/makehtml/cases/standard/implicit-anchors.html`
```html
<p>Search the web at <a href="http://google.com/">Google</a> or <a href="http://daringfireball.net/">Daring Fireball</a>.</p>
<p>Search the web at <a href="http://google.com/">Google</a> or <a href="http://daringfireball.net/">Daring Fireball</a>.</p>
```

## File: `test/functional/makehtml/cases/standard/implicit-anchors.md`
```markdown
Search the web at [Google][] or [Daring Fireball][].

Search the web at [Google] or [Daring Fireball].


  [Google]: http://google.com/
  [Daring Fireball]: http://daringfireball.net/
```

## File: `test/functional/makehtml/cases/standard/inline-anchors.html`
```html
<p>This is <a href="http://example.com/" title="Title">an example</a> inline link.</p>
<p><a href="http://example.net/">This link</a> has no title attribute.</p>
```

## File: `test/functional/makehtml/cases/standard/inline-anchors.md`
```markdown
This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.
```

## File: `test/functional/makehtml/cases/standard/inline-code.html`
```html
<p>Create a new <code>function</code>.</p>
<p>Use the backtick in MySQL syntax <code>SELECT `column` FROM whatever</code>.</p>
<p>A single backtick in a code span: <code>`</code></p>
<p>A backtick-delimited string in a code span: <code>`foo`</code></p>
<p>Please don't use any <code>&lt;blink&gt;</code> tags.</p>
<p><code>&amp;#8212;</code> is the decimal-encoded equivalent of <code>&amp;mdash;</code>.</p>
<p>this <code>inline **code** has ___magic___</code> chars</p>
```

## File: `test/functional/makehtml/cases/standard/inline-code.md`
```markdown
Create a new `function`.

Use the backtick in MySQL syntax ``SELECT `column` FROM whatever``.

A single backtick in a code span: `` ` ``

A backtick-delimited string in a code span: `` `foo` ``

Please don't use any `<blink>` tags.

`&#8212;` is the decimal-encoded equivalent of `&mdash;`.

this `inline **code** has ___magic___` chars
```

## File: `test/functional/makehtml/cases/standard/inline-escaped-chars.html`
```html
<p>Hello.this_is_a_variable
  and.this.is.another_one</p>
```

## File: `test/functional/makehtml/cases/standard/inline-escaped-chars.md`
```markdown
Hello.this\_is\_a\_variable
and.this.is.another_one
```

## File: `test/functional/makehtml/cases/standard/inline-style-tag.html`
```html
<style>
  p { line-height: 20px; }
</style>
<p>An exciting sentence.</p>
```

## File: `test/functional/makehtml/cases/standard/inline-style-tag.md`
```markdown
<style>
    p { line-height: 20px; }
</style>

An exciting sentence.
```

## File: `test/functional/makehtml/cases/standard/lazy-blockquote.html`
```html
<blockquote>
  <p>This is a multi line blockquote test</p>
  <p>With more than one line.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/standard/lazy-blockquote.md`
```markdown
  > This is a multi line blockquote test

  > With more than one line.
```

## File: `test/functional/makehtml/cases/standard/line-starts-with-html.html`
```html
<p><a href="foo">some text</a> words</p>
<p><br> words</p>
```

## File: `test/functional/makehtml/cases/standard/line-starts-with-html.md`
```markdown
<a href="foo">some text</a> words

<br> words
```

## File: `test/functional/makehtml/cases/standard/list-followed-by-blockquote.html`
```html
<h1 id="sometitle">some title</h1>
<ol>
    <li>list item 1</li>
    <li>list item 2</li>
</ol>
<blockquote>
    <p>some text in a blockquote</p>
</blockquote>
<ul>
    <li>another list item 1</li>
    <li>another list item 2</li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/list-followed-by-blockquote.md`
```markdown
# some title

1. list item 1
2. list item 2

> some text in a blockquote

* another list item 1
* another list item 2
```

## File: `test/functional/makehtml/cases/standard/list-followed-by-ghcode.html`
```html
<h1 id="sometitle">some title</h1>
<ol>
    <li>list item 1</li>
    <li>list item 2</li>
</ol>
<pre><code>some code

    and some other line of code
</code></pre>
<ul>
    <li>another list item 1</li>
    <li>another list item 2</li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/list-followed-by-ghcode.md`
```markdown
# some title

1. list item 1
2. list item 2

```
some code

and some other line of code
```

* another list item 1
* another list item 2
```

## File: `test/functional/makehtml/cases/standard/list-with-blockquote.html`
```html
<ul>
  <li><p>A list item with a blockquote:</p>
    <blockquote>
      <p>This is a blockquote
        inside a list item.</p>
    </blockquote></li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/list-with-blockquote.md`
```markdown
*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.
```

## File: `test/functional/makehtml/cases/standard/list-with-code.html`
```html
<ul>
  <li><p>A list item with code:</p>
    <pre><code>alert('Hello world!');
    </code></pre></li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/list-with-code.md`
```markdown
*   A list item with code:

        alert('Hello world!');
```

## File: `test/functional/makehtml/cases/standard/literal-html-tags.html`
```html
<p><code>some **code** yeah</code></p>
<p>some <code>inline **code** block</code></p>
<p><code>some inline **code**</code> block</p>
<p>yo dawg <code start="true">some &lt;code start="false"&gt;code&lt;/code&gt; inception</code></p>
<div>some **div** yeah</div>
```

## File: `test/functional/makehtml/cases/standard/literal-html-tags.md`
```markdown
<code>some **code** yeah</code>

some <code>inline **code** block</code>

<code>some inline **code**</code> block

yo dawg <code start="true">some <code start="false">code</code> inception</code>

<div>some **div** yeah</div>
```

## File: `test/functional/makehtml/cases/standard/multi-paragraph-list.html`
```html
<ol>
  <li><p>This is a major bullet point.</p>
    <p>That contains multiple paragraphs.</p></li>
  <li><p>And another line</p></li>
</ol>
```

## File: `test/functional/makehtml/cases/standard/multi-paragraph-list.md`
```markdown
 1.  This is a major bullet point.

    That contains multiple paragraphs.

 2.  And another line
```

## File: `test/functional/makehtml/cases/standard/multiline-unordered-list.html`
```html
<ul>
  <li>This line spans
    more than one line and is lazy</li>
  <li>Similar to this line</li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/multiline-unordered-list.md`
```markdown
 - This line spans
 more than one line and is lazy
 - Similar to this line
```

## File: `test/functional/makehtml/cases/standard/nested-blockquote.html`
```html
<blockquote>
  <p>This is a multi line blockquote test</p>
  <blockquote>
    <p>And nesting!</p>
  </blockquote>
  <p>With more than one line.</p>
</blockquote>
```

## File: `test/functional/makehtml/cases/standard/nested-blockquote.md`
```markdown
  > This is a multi line blockquote test
  >
  > > And nesting!
  >
  > With more than one line.
```

## File: `test/functional/makehtml/cases/standard/nested-gh-codeblocks.html`
```html
<pre><code>1. some code idented 4 spaces

    ```
    var foobar = 'foo';
    ```

2. another line
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/nested-gh-codeblocks.md`
```markdown
```
1. some code idented 4 spaces

    ```
    var foobar = 'foo';
    ```

2. another line
```
```

## File: `test/functional/makehtml/cases/standard/ordered-list-same-number.html`
```html
<ol>
  <li>Red</li>
  <li>Green</li>
  <li>Blue</li>
</ol>
```

## File: `test/functional/makehtml/cases/standard/ordered-list-same-number.md`
```markdown
 1.  Red
 1.  Green
 1.  Blue
```

## File: `test/functional/makehtml/cases/standard/ordered-list-starting-number.html`
```html
<ol start="5">
    <li>foo</li>
    <li>bar</li>
    <li>baz</li>
</ol>
<hr />
<ol start="3">
    <li>a</li>
    <li>b</li>
    <li>c</li>
    <li>d</li>
</ol>
```

## File: `test/functional/makehtml/cases/standard/ordered-list-starting-number.md`
```markdown
5. foo
6. bar
7. baz

---

3.  a
2.  b
7.  c
23. d
```

## File: `test/functional/makehtml/cases/standard/ordered-list-wrong-numbers.html`
```html
<ol>
  <li>Red</li>
  <li>Green</li>
  <li>Blue</li>
</ol>
```

## File: `test/functional/makehtml/cases/standard/ordered-list-wrong-numbers.md`
```markdown
 1.  Red
 1.  Green
 1.  Blue
```

## File: `test/functional/makehtml/cases/standard/ordered-list.html`
```html
<ol>
  <li>Red</li>
  <li>Green</li>
  <li>Blue</li>
</ol>
```

## File: `test/functional/makehtml/cases/standard/ordered-list.md`
```markdown
 1.  Red
 2.  Green
 3.  Blue
```

## File: `test/functional/makehtml/cases/standard/paragraphed-list-with-sublists.html`
```html
<ul>
  <li><p>foo</p>
    <ul>
      <li><p>bazinga</p></li>
      <li><p>yeah</p></li></ul></li>
  <li><p>bar</p>
    <ol>
      <li><p>damn</p></li>
      <li><p>so many paragraphs</p></li></ol></li>
  <li><p>baz</p></li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/paragraphed-list-with-sublists.md`
```markdown
 - foo
 
    - bazinga
    
    - yeah
 
 - bar
 
    1. damn
    
    2. so many paragraphs
 
 - baz
```

## File: `test/functional/makehtml/cases/standard/pre-code-tags-inside-code-block.html`
```html
<p>code inception</p>
<pre><code>&lt;pre&gt;&lt;code&gt;
&lt;div&gt;some html code inside code html tags inside a fenced code block&lt;/div&gt;
&lt;/code&gt;&lt;/pre&gt;
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/pre-code-tags-inside-code-block.md`
```markdown
code inception

```
<pre><code>
<div>some html code inside code html tags inside a fenced code block</div>
</code></pre>
```
```

## File: `test/functional/makehtml/cases/standard/pre-code-tags.html`
```html
<pre>
<code>
foobar
</code>
</pre>
<p>blabla</p>
<pre nhaca="zulu"><code bla="bla">
foobar
</code>
</pre>
<pre><code>
&lt;div&gt;some html code&lt;/div&gt;
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/pre-code-tags.md`
```markdown
<pre>
<code>
foobar
</code>
</pre>

blabla

<pre nhaca="zulu"><code bla="bla">
foobar
</code>
</pre>

<pre><code>
<div>some html code</div>
</code></pre>
```

## File: `test/functional/makehtml/cases/standard/relative-anchors.html`
```html
<p>See my <a href="/about/">About</a> page for details.</p>
```

## File: `test/functional/makehtml/cases/standard/relative-anchors.md`
```markdown
See my [About](/about/) page for details.
```

## File: `test/functional/makehtml/cases/standard/repeated-headers.html`
```html
<h1 id="sametitle">Same Title</h1>
<p>some text</p>
<h1 id="sametitle-1">Same Title</h1>
```

## File: `test/functional/makehtml/cases/standard/repeated-headers.md`
```markdown
# Same Title

some text

# Same Title
```

## File: `test/functional/makehtml/cases/standard/simple-paragraph.html`
```html
<p>Hello, world!</p>
```

## File: `test/functional/makehtml/cases/standard/simple-paragraph.md`
```markdown
Hello, world!
```

## File: `test/functional/makehtml/cases/standard/strip-references.md`
```markdown
[1]: http://www.google.co.uk

[http://www.google.co.uk]: http://www.google.co.uk





[1]: http://dsurl.stuff/something.jpg

[1]:http://www.google.co.uk

 [1]:http://www.google.co.uk
```

## File: `test/functional/makehtml/cases/standard/strong.html`
```html
<p><strong>important</strong></p>
<p><strong>important</strong></p>
<p>really <strong>freaking</strong>strong</p>
```

## File: `test/functional/makehtml/cases/standard/strong.md`
```markdown
**important**

__important__

really **freaking**strong
```

## File: `test/functional/makehtml/cases/standard/unordered-list-asterisk.html`
```html
<ul>
  <li>Red</li>
  <li>Green</li>
  <li>Blue</li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/unordered-list-asterisk.md`
```markdown
 * Red
 * Green
 * Blue
```

## File: `test/functional/makehtml/cases/standard/unordered-list-minus.html`
```html
<ul>
  <li>Red</li>
  <li>Green</li>
  <li>Blue</li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/unordered-list-minus.md`
```markdown
 - Red
 - Green
 - Blue
```

## File: `test/functional/makehtml/cases/standard/unordered-list-plus.html`
```html
<ul>
  <li>Red</li>
  <li>Green</li>
  <li>Blue</li>
</ul>
```

## File: `test/functional/makehtml/cases/standard/unordered-list-plus.md`
```markdown
 + Red
 + Green
 + Blue
```

## File: `test/functional/makehtml/cases/standard/url-with-parenthesis.html`
```html
<p>There's an <a href="http://en.memory-alpha.org/wiki/Darmok_(episode)">episode</a> of Star Trek: The Next Generation</p>
```

## File: `test/functional/makehtml/cases/standard/url-with-parenthesis.md`
```markdown
There's an [episode](http://en.memory-alpha.org/wiki/Darmok_(episode)) of Star Trek: The Next Generation
```

## File: `test/functional/makemarkdown/makemarkdown.bootstrap.js`
```javascript
/**
 * Created by Estevao on 22-12-2017.
 */

//jscs:disable requireCamelCaseOrUpperCaseIdentifiers
(function () {
  'use strict';

  require('source-map-support').install();
  require('chai').should();
  var fs = require('fs');

  function getTestSuite (dir) {
    return fs.readdirSync(dir)
      .filter(filter())
      .map(map(dir));
  }

  function filter () {
    return function (file) {
      var ext = file.slice(-3);
      return (ext === '.md');
    };
  }

  function map (dir) {
    return function (file) {
      var name = file.replace('.md', ''),
          htmlPath = dir + name + '.html',
          html = fs.readFileSync(htmlPath, 'utf8'),
          mdPath = dir + name + '.md',
          md = fs.readFileSync(mdPath, 'utf8');

      return {
        name:     name,
        input:    html,
        expected: md
      };
    };
  }

  function assertion (testCase, converter) {
    return function () {
      testCase.actual = converter.makeMarkdown(testCase.input);
      testCase = normalize(testCase);

      // Compare
      testCase.actual.should.equal(testCase.expected);
    };
  }

  //Normalize input/output
  function normalize (testCase) {

    // Normalize line returns
    testCase.expected = testCase.expected.replace(/(\r\n)|\n|\r/g, '\n');
    testCase.actual = testCase.actual.replace(/(\r\n)|\n|\r/g, '\n');

    // Remove extra lines
    testCase.expected = testCase.expected.replace(/^\n+/, '').replace(/\n+$/, '');
    testCase.actual = testCase.actual.replace(/^\n+/, '').replace(/\n+$/, '');

    return testCase;
  }

  module.exports = {
    getTestSuite: getTestSuite,
    assertion: assertion,
    normalize: normalize,
    showdown: require('../../../.build/showdown.js')
  };
})();

```

## File: `test/functional/makemarkdown/testsuite.features.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */
var bootstrap = require('./makemarkdown.bootstrap.js'),
    showdown = bootstrap.showdown,
    assertion = bootstrap.assertion,
    issues = bootstrap.getTestSuite('test/functional/makemarkdown/cases/features/issues/'),
    ghMentions = bootstrap.getTestSuite('test/functional/makemarkdown/cases/features/ghMentions/');

describe('makeMarkdown() features testsuite', function () {
  'use strict';

  describe('issues', function () {
    for (var i = 0; i < issues.length; ++i) {
      var converter;
      if (issues[i].name === '#164.4.tasklists') {
        converter = new showdown.Converter({tasklists: true});
      } else {
        converter = new showdown.Converter();
      }
      it(issues[i].name.replace(/-/g, ' '), assertion(issues[i], converter));
    }
  });

  describe('ghMentions', function () {
    var converter = new showdown.Converter({ ghMentions: true });
    for (var i = 0; i < ghMentions.length; ++i) {
      it(ghMentions[i].name.replace(/-/g, ' '), assertion(ghMentions[i], converter));
    }
  });
});
```

## File: `test/functional/makemarkdown/testsuite.standard.js`
```javascript
/**
 * Created by Estevao on 08-06-2015.
 */

var bootstrap = require('./makemarkdown.bootstrap.js'),
    converter = new bootstrap.showdown.Converter(),
    assertion = bootstrap.assertion,
    testsuite = bootstrap.getTestSuite('test/functional/makemarkdown/cases/standard/');

describe('makeMarkdown() standard testsuite', function () {
  'use strict';
  for (var i = 0; i < testsuite.length; ++i) {
    it(testsuite[i].name.replace(/-/g, ' '), assertion(testsuite[i], converter));
  }
});
```

## File: `test/functional/makemarkdown/cases/features/ghMentions/github.html`
```html
<p><a class="bazinga user-mention foo bar baz" href="https://github.com/tivie">@tivie</a></p>
<p><a class="not-user-mention" href="https://www.google.com">@something</a></p>
```

## File: `test/functional/makemarkdown/cases/features/ghMentions/github.md`
```markdown
@tivie

[@something](<https://www.google.com>)
```

## File: `test/functional/makemarkdown/cases/features/issues/tasklists.html`
```html
<h1 id="mythings">my things</h1>
<ul>
    <li>foo</li>
    <li class="task-list-item" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;"> bar</li>
    <li class="task-list-item" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;"> baz</li>
    <li class="task-list-item" style="list-style-type: none;"><input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;" checked> bazinga</li>
</ul>
<p>otherthings</p>
```

## File: `test/functional/makemarkdown/cases/features/issues/tasklists.md`
```markdown
# my things

- foo
- [ ] bar
- [ ] baz
- [x] bazinga

otherthings
```

## File: `test/functional/makemarkdown/cases/standard/anchors-relative.html`
```html
<p>See my <a href="/about/">About</a> page for details.</p>
```

## File: `test/functional/makemarkdown/cases/standard/anchors-relative.md`
```markdown
See my [About](</about/>) page for details.
```

## File: `test/functional/makemarkdown/cases/standard/anchors.html`
```html
<p>This is <a href="http://example.com/" title="Title">an example</a> inline link.</p>
<p><a href="http://example.net/">This link</a> has no title attribute.</p>
```

## File: `test/functional/makemarkdown/cases/standard/anchors.md`
```markdown
This is [an example](<http://example.com/> "Title") inline link.

[This link](<http://example.net/>) has no title attribute.
```

## File: `test/functional/makemarkdown/cases/standard/blockquote-followed-by-code.html`
```html
<blockquote>
    <p>a blockquote
with a 4 space indented line (not code)</p>
</blockquote>
<p>sep</p>
<blockquote>
    <p>a blockquote</p>
</blockquote>
<pre><code>with some code after</code></pre>
```

## File: `test/functional/makemarkdown/cases/standard/blockquote-followed-by-code.md`
```markdown
> a blockquote with a 4 space indented line (not code)

sep

> a blockquote

```
with some code after
```
```

## File: `test/functional/makemarkdown/cases/standard/blockquote-nested-markdown.html`
```html
<blockquote>
  <h2 id="thisisaheader">This is a header.</h2>
  <ol>
    <li>This is the first list item.</li>
    <li>This is the second list item.</li>
  </ol>
  <p>Here's some example code:</p>
    <pre><code>return shell_exec("echo $input | $markdown_script");
    </code></pre>
</blockquote>
```

## File: `test/functional/makemarkdown/cases/standard/blockquote-nested-markdown.md`
```markdown
> ## This is a header.
> 
> 1. This is the first list item.
> 2. This is the second list item.
> 
> Here's some example code:
> 
> ```
> return shell_exec("echo $input | $markdown_script");
> ```
```

## File: `test/functional/makemarkdown/cases/standard/blockquote.html`
```html
<blockquote>
<p>This is a multi line blockquote test</p>
<p>With more than one line.</p>
</blockquote>
```

## File: `test/functional/makemarkdown/cases/standard/blockquote.md`
```markdown
> This is a multi line blockquote test
> 
> With more than one line.
```

## File: `test/functional/makemarkdown/cases/standard/breaks.html`
```html
first line<br />and the second
```

## File: `test/functional/makemarkdown/cases/standard/breaks.md`
```markdown
first line  
and the second 
```

## File: `test/functional/makemarkdown/cases/standard/emphasis-double.html`
```html
<p>a <strong><em>strong and em</em></strong> thingy</p>
<p>bar<strong><em>bazinga</em></strong>bar</p>
```

## File: `test/functional/makemarkdown/cases/standard/emphasis-double.md`
```markdown
a ***strong and em*** thingy

bar***bazinga***bar
```

## File: `test/functional/makemarkdown/cases/standard/emphasis-inside-inline-code.html`
```html
<p>some text <code>**foo**</code></p>
```

## File: `test/functional/makemarkdown/cases/standard/emphasis-inside-inline-code.md`
```markdown
some text `**foo**`
```

## File: `test/functional/makemarkdown/cases/standard/emphasis.html`
```html
<p><em>single asterisks</em></p>
<p><em>single underscores</em></p>
<p><strong>double asterisks</strong></p>
<p><strong>double underscores</strong></p>
<p>text <em>with italic sentence</em> in middle</p>
<p>text <strong>with bold sentence</strong> in middle</p>
<p>text with <strong>bold text that
  spans across multiple</strong> lines</p>
<p>underscored_word</p>
<p>doubleunderscore__word</p>
<p>asterix*word</p>
<p>doubleasterix**word</p>
<p>line with_underscored word</p>
<p>line with__doubleunderscored word</p>
<p>line with*asterixed word</p>
<p>line with**doubleasterixed word</p>
<p>some line<em>with</em>inner underscores</p>
<p>some line<strong>with</strong>inner double underscores</p>
<p>some line<em>with</em>inner asterixs</p>
<p>some line<strong>with</strong>inner double asterixs</p>
<p>another line with just _one underscore</p>
<p>another line with just __one double underscore</p>
<p>another line with just *one asterix</p>
<p>another line with just **one double asterix</p>
<p>a sentence with<em>underscore and another</em>underscore</p>
<p>a sentence with<strong>doubleunderscore and another</strong>doubleunderscore</p>
<p>a sentence with<em>asterix and another</em>asterix</p>
<p>a sentence with<strong>doubleasterix and another</strong>doubleasterix</p>
<p>escaped word_with_underscores</p>
<p>escaped word__with__double underscores</p>
<p>escaped word<em>_with_</em>single italic underscore</p>
<p>escaped word*with*asterixs</p>
<p>escaped word**with**asterixs</p>
<p>escaped word<strong>*with*</strong>bold asterixs</p>
<p>foo<strong>bar</strong>baz</p>
<p>foo<strong>bar</strong>baz</p>
<p>this is <strong><a href="//google.com">imbued link with strong</a></strong></p>
```

## File: `test/functional/makemarkdown/cases/standard/emphasis.md`
```markdown
*single asterisks*

*single underscores*

**double asterisks**

**double underscores**

text *with italic sentence* in middle

text **with bold sentence** in middle

text with **bold text that spans across multiple** lines

underscored\_word

doubleunderscore\_\_word

asterix\*word

doubleasterix\*\*word

line with\_underscored word

line with\_\_doubleunderscored word

line with\*asterixed word

line with\*\*doubleasterixed word

some line*with*inner underscores

some line**with**inner double underscores

some line*with*inner asterixs

some line**with**inner double asterixs

another line with just \_one underscore

another line with just \_\_one double underscore

another line with just \*one asterix

another line with just \*\*one double asterix

a sentence with*underscore and another*underscore

a sentence with**doubleunderscore and another**doubleunderscore

a sentence with*asterix and another*asterix

a sentence with**doubleasterix and another**doubleasterix

escaped word\_with\_underscores

escaped word\_\_with\_\_double underscores

escaped word*\_with\_*single italic underscore

escaped word\*with\*asterixs

escaped word\*\*with\*\*asterixs

escaped word**\*with\***bold asterixs

foo**bar**baz

foo**bar**baz

this is **[imbued link with strong](<//google.com>)**
```

## File: `test/functional/makemarkdown/cases/standard/escaping-html-entities.html`
```html
<p>a &quot;quoted&quot; string</p>
<p>duarte&amp;companhia</p>
<p>1 &lt; 2</p>
<p>2 &gt; 1</p>
```

## File: `test/functional/makemarkdown/cases/standard/escaping-html-entities.md`
```markdown
a "quoted" string

duarte&companhia

1 < 2

2 > 1
```

## File: `test/functional/makemarkdown/cases/standard/escaping.html`
```html
<p>[a false reference]: must be escaped</p>
<p> - a list item</p>
<p>*</p>
<p>~</p>
<p>|</p>
<p>[a faux](link)</p>
<p># at start</p>
<p>in the # middle is ok</p>
<p>> at start</p>
<p>in the middle > is ok</p>
<p>---</p>
<p>1. must be escaped</p>
<p>but. this should not</p>
<p>. nor this</p>
<p>or this.</p>
<p>    4 spaces at the beginning of line are removed</p>
<p>multiple spaces    are colapsed to 1</p>
```

## File: `test/functional/makemarkdown/cases/standard/escaping.md`
```markdown
\[a false reference]: must be escaped

\- a list item

\*

\~

\|

[a faux\]\(link)

\# at start

in the # middle is ok

\> at start

in the middle > is ok

\---

1\. must be escaped

but. this should not

. nor this

or this.

4 spaces at the beginning of line are removed

multiple spaces are colapsed to 1
```

## File: `test/functional/makemarkdown/cases/standard/github-style-at-start.html`
```html
<pre><code>
function MyFunc(a) {
  // ...
}
</code></pre>
<p>That is some code!</p>
```

## File: `test/functional/makemarkdown/cases/standard/github-style-at-start.md`
```markdown
```
function MyFunc(a) {
  // ...
}
```

That is some code!
```

## File: `test/functional/makemarkdown/cases/standard/github-style-codeblock-inside-quote.html`
```html
<blockquote>
<p>Define a function in javascript:</p>
<pre><code>
function MyFunc(a) {
    var s = '`';
}
</code></pre>
<blockquote>
<p>And some nested quote</p>
<pre><code class="html language-html">&lt;div&gt;HTML!&lt;/div&gt;
</code></pre>
</blockquote>
</blockquote>
```

## File: `test/functional/makemarkdown/cases/standard/github-style-codeblock-inside-quote.md`
```markdown
> Define a function in javascript:
> 
> ```
> function MyFunc(a) {
>     var s = '`';
> }
> ```
> 
> > And some nested quote
> > 
> > ```html
> > <div>HTML!</div>
> > ```
```

## File: `test/functional/makemarkdown/cases/standard/github-style-codeblock.html`
```html
<p>Define a function in javascript:</p>
<pre><code>function MyFunc(a) {
    var s = '`';
}
</code></pre>
<p>And some HTML</p>
<pre><code class="html language-html">&lt;div&gt;HTML!&lt;/div&gt;
</code></pre>
<pre><code data-language="javascript">
function foo() {
    return 'bar';
}
</code></pre>
```

## File: `test/functional/makemarkdown/cases/standard/github-style-codeblock.md`
```markdown

Define a function in javascript:

```
function MyFunc(a) {
    var s = '`';
}
```

And some HTML

```html
<div>HTML!</div>
```

```javascript
function foo() {
    return 'bar';
}
```
```

## File: `test/functional/makemarkdown/cases/standard/github-style-linebreaks.html`
```html
<pre><code>code can go here
this is rendered on a second line
</code></pre>
```

## File: `test/functional/makemarkdown/cases/standard/github-style-linebreaks.md`
```markdown
```
code can go here
this is rendered on a second line
```
```

## File: `test/functional/makemarkdown/cases/standard/h1-with-single-hash.html`
```html
<h1 id="thisisanh1">This is an H1</h1>
```

## File: `test/functional/makemarkdown/cases/standard/h1-with-single-hash.md`
```markdown
# This is an H1
```

## File: `test/functional/makemarkdown/cases/standard/h2-with-single-hash.html`
```html
<h2 id="thisisanh2">This is an H2</h2>
```

## File: `test/functional/makemarkdown/cases/standard/h2-with-single-hash.md`
```markdown
## This is an H2
```

## File: `test/functional/makemarkdown/cases/standard/h3-with-single-hash.html`
```html
<h3 id="thisisanh3">This is an H3</h3>
```

## File: `test/functional/makemarkdown/cases/standard/h3-with-single-hash.md`
```markdown
### This is an H3
```

## File: `test/functional/makemarkdown/cases/standard/h4-with-single-hash.html`
```html
<h4 id="thisisanh4">This is an H4</h4>
```

## File: `test/functional/makemarkdown/cases/standard/h4-with-single-hash.md`
```markdown
#### This is an H4
```

## File: `test/functional/makemarkdown/cases/standard/h5-with-single-hash.html`
```html
<h5 id="thisisanh5">This is an H5</h5>
```

## File: `test/functional/makemarkdown/cases/standard/h5-with-single-hash.md`
```markdown
##### This is an H5
```

## File: `test/functional/makemarkdown/cases/standard/h6-with-single-hash.html`
```html
<h6 id="thisisanh6">This is an H6</h6>
```

## File: `test/functional/makemarkdown/cases/standard/h6-with-single-hash.md`
```markdown
###### This is an H6
```

## File: `test/functional/makemarkdown/cases/standard/horizontal-rules.html`
```html
<hr />
<hr>
```

## File: `test/functional/makemarkdown/cases/standard/horizontal-rules.md`
```markdown
---

---
```

## File: `test/functional/makemarkdown/cases/standard/html-comments.html`
```html
<!-- a comment -->
<!-- a comment with *bogus* __markdown__ inside -->
<!-- comment -->
<p>words</p>
   <!-- comment -->
<pre><code>&lt;!-- comment --&gt;
</code></pre>
<p>&lt;!----------------------------------------------------------------------------------------------------------------------------------------------------</p>
<!-------------------------------------------------------------------->
```

## File: `test/functional/makemarkdown/cases/standard/html-comments.md`
```markdown
<!-- a comment -->

<!-- a comment with *bogus* __markdown__ inside -->

<!-- comment -->

words

<!-- comment -->

```
<!-- comment -->
```

<!----------------------------------------------------------------------------------------------------------------------------------------------------

<!-------------------------------------------------------------------->
```

## File: `test/functional/makemarkdown/cases/standard/html.html`
```html
<div>
    some text
</div>

<span>an inline element</span>

<div>
    <span>a span inside a div</span>
</div>

```

## File: `test/functional/makemarkdown/cases/standard/html.md`
```markdown
<div> some text </div>

<span>an inline element</span>

<div><span>a span inside a div</span></div>

```

## File: `test/functional/makemarkdown/cases/standard/html5-strutural-tags.html`
```html
<p>These HTML5 tags should pass through just fine.</p>
<section>hello</section>
<header>head</header>
<footer>footsies</footer>
<nav>navigation</nav>
<article>read me</article>
<aside>ignore me</aside>
<article>read
  me</article>
<aside>
  ignore me
</aside>
<p>the end</p>
<audio class="podcastplayer" controls>
  <source src="foobar.mp3" type="audio/mp3" preload="none"></source>
  <source src="foobar.off" type="audio/ogg" preload="none"></source>
</audio>
<video src="foo.ogg">
  <track kind="subtitles" src="foo.en.vtt" srclang="en" label="English">
  <track kind="subtitles" src="foo.sv.vtt" srclang="sv" label="Svenska">
</video>
<address>My street</address>
<canvas id="canvas" width="300" height="300">
  Sorry, your browser doesn't support the &lt;canvas&gt; element.
</canvas>
<figure>
  <img src="mypic.png" alt="An awesome picture">
  <figcaption>Caption for the awesome picture</figcaption>
</figure>
<hgroup>
  <h1>Main title</h1>
  <h2>Secondary title</h2>
</hgroup>
<output name="result"></output>
<details>
  <summary>Summarise me</summary>
  <p>Explain the details</p>
</details>
```

## File: `test/functional/makemarkdown/cases/standard/html5-strutural-tags.md`
```markdown
These HTML5 tags should pass through just fine.

<section>hello</section>

<header>head</header>

<footer>footsies</footer>

<nav>navigation</nav>

<article>read me</article>

<aside>ignore me</aside>

<article>read me</article>

<aside> ignore me </aside>

the end

<audio class="podcastplayer" controls=""><source src="foobar.mp3" type="audio/mp3" preload="none"><source src="foobar.off" type="audio/ogg" preload="none"></audio>

<video src="foo.ogg"><track kind="subtitles" src="foo.en.vtt" srclang="en" label="English"><track kind="subtitles" src="foo.sv.vtt" srclang="sv" label="Svenska"></video>

<address>My street</address>

<canvas id="canvas" width="300" height="300"> Sorry, your browser doesn't support the &lt;canvas&gt; element. </canvas>

<figure><img src="mypic.png" alt="An awesome picture"><figcaption>Caption for the awesome picture</figcaption></figure>

<hgroup><h1>Main title</h1><h2>Secondary title</h2></hgroup>

<output name="result"></output>

<details><summary>Summarise me</summary><p>Explain the details</p></details>
```

## File: `test/functional/makemarkdown/cases/standard/images-followed-by-brackets.html`
```html
<p><img src="./image/cat1.png" alt="image link" />(some text between brackets)</p>
<p><img src="./image/cat(1).png" alt="image link" />(some text between brackets)</p>
```

## File: `test/functional/makemarkdown/cases/standard/images-followed-by-brackets.md`
```markdown
![image link](<./image/cat1.png>)(some text between brackets)

![image link](<./image/cat(1).png>)(some text between brackets)
```

## File: `test/functional/makemarkdown/cases/standard/images.html`
```html
<p><img src="/path/to/img.jpg" alt="Alt text" /></p>
<p><img src="/path/to/img.jpg" alt="Alt text" title="Optional title" /></p>
<p><img src="url/to/image.jpg" alt="Alt text" title="Optional title attribute" /></p>
<p><img src="url/to/image2.jpg" alt="My Image" title="Optional title attribute" /></p>
<p>![leave me alone]</p>
<p>![leave me alone][]</p>
```

## File: `test/functional/makemarkdown/cases/standard/images.md`
```markdown
![Alt text](</path/to/img.jpg>)

![Alt text](</path/to/img.jpg> "Optional title")

![Alt text](<url/to/image.jpg> "Optional title attribute")

![My Image](<url/to/image2.jpg> "Optional title attribute")

![leave me alone]

![leave me alone][]
```

## File: `test/functional/makemarkdown/cases/standard/list-doubleline.html`
```html
<ul>
  <li><p>Bird</p></li>
  <li><p>Magic</p></li>
</ul>
```

## File: `test/functional/makemarkdown/cases/standard/list-doubleline.md`
```markdown
- Bird

- Magic
```

## File: `test/functional/makemarkdown/cases/standard/list-followed-by-blockquote.html`
```html
<h1 id="sometitle">some title</h1>
<ol>
    <li>list item 1</li>
    <li>list item 2</li>
</ol>
<blockquote>
    <p>some text in a blockquote</p>
</blockquote>
<ul>
    <li>another list item 1</li>
    <li>another list item 2</li>
</ul>
```

## File: `test/functional/makemarkdown/cases/standard/list-followed-by-blockquote.md`
```markdown
# some title

1. list item 1
2. list item 2

> some text in a blockquote

- another list item 1
- another list item 2
```

## File: `test/functional/makemarkdown/cases/standard/list-followed-by-ghcode.html`
```html
<h1 id="sometitle">some title</h1>
<ol>
    <li>list item 1</li>
    <li>list item 2</li>
</ol>
<pre><code>some code

and some other line of code
</code></pre>
<ul>
    <li>another list item 1</li>
    <li>another list item 2</li>
</ul>
```

## File: `test/functional/makemarkdown/cases/standard/list-followed-by-ghcode.md`
```markdown
# some title

1. list item 1
2. list item 2

```
some code

and some other line of code
```

- another list item 1
- another list item 2
```

## File: `test/functional/makemarkdown/cases/standard/list-with-blockquote.html`
```html
<ul>
  <li><p>A list item with a blockquote:</p>
    <blockquote>
      <p>This is a blockquote
        inside a list item.</p>
    </blockquote></li>
</ul>
```

## File: `test/functional/makemarkdown/cases/standard/list-with-blockquote.md`
```markdown
- A list item with a blockquote:

    > This is a blockquote inside a list item.
```

## File: `test/functional/makemarkdown/cases/standard/list-with-code.html`
```html
<ul>
  <li><p>A list item with code:</p>
    <pre><code>alert('Hello world!');
    </code></pre></li>
</ul>
```

## File: `test/functional/makemarkdown/cases/standard/list-with-code.md`
```markdown
- A list item with code:

    ```
    alert('Hello world!');
    ```
```

## File: `test/functional/makemarkdown/cases/standard/multi-paragraph-list.html`
```html
<ol>
  <li><p>This is a major bullet point.</p>
    <p>That contains multiple paragraphs.</p></li>
  <li><p>And another line</p></li>
</ol>
```

## File: `test/functional/makemarkdown/cases/standard/multi-paragraph-list.md`
```markdown
1. This is a major bullet point.

    That contains multiple paragraphs.

2. And another line
```

## File: `test/functional/makemarkdown/cases/standard/nested-gh-codeblocks.html`
```html
<pre><code>1. some code idented 4 spaces

    ```
    var foobar = 'foo';
    ```

2. another line
</code></pre>
```

## File: `test/functional/makemarkdown/cases/standard/nested-gh-codeblocks.md`
```markdown
```
1. some code idented 4 spaces

    ```
    var foobar = 'foo';
    ```

2. another line
```
```

## File: `test/functional/makemarkdown/cases/standard/ordered-list-starting-number.html`
```html
<ol start="5">
    <li>foo</li>
    <li>bar</li>
    <li>baz</li>
</ol>
```

## File: `test/functional/makemarkdown/cases/standard/ordered-list-starting-number.md`
```markdown
5. foo
6. bar
7. baz

```

## File: `test/functional/makemarkdown/cases/standard/ordered-list.html`
```html
<ol>
  <li>Red</li>
  <li>Green</li>
  <li>Blue</li>
</ol>
```

## File: `test/functional/makemarkdown/cases/standard/ordered-list.md`
```markdown
1. Red
2. Green
3. Blue
```

## File: `test/functional/makemarkdown/cases/standard/paragraph-simple.html`
```html
<p>Hello, world!</p>
```

## File: `test/functional/makemarkdown/cases/standard/paragraph-simple.md`
```markdown
Hello, world!
```

## File: `test/functional/makemarkdown/cases/standard/paragraphed-list-with-sublists.html`
```html
<ul>
  <li><p>foo</p>
    <ul>
      <li><p>bazinga</p></li>
      <li><p>yeah</p></li></ul></li>
  <li><p>bar</p>
    <ol>
      <li><p>damn</p></li>
      <li><p>so many paragraphs</p></li></ol></li>
  <li><p>baz</p></li>
</ul>
```

## File: `test/functional/makemarkdown/cases/standard/paragraphed-list-with-sublists.md`
```markdown
- foo

    - bazinga

    - yeah

- bar

    1. damn

    2. so many paragraphs

- baz
```

## File: `test/functional/makemarkdown/cases/standard/table-complex.html`
```html
<table>
    <caption>some table</caption>
    <colgroup>
        <col span="2" style="background-color:red">
        <col style="background-color:yellow">
    </colgroup>
    <thead>
        <tr>
            <th scope="col">head 1</th>
            <th scope="col">head 2</th>
            <th scope="col">head 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>row 1: col 1</td>
            <td>row 1: col 2</td>
            <td>row 1: col 3</td>
        </tr>
        <tr>
            <td>row 2: col 1</td>
            <td>row 2: col 2</td>
            <td>row 2: col 3</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>footer 1</td>
            <td>footer 2</td>
            <td>footer 3</td>
        </tr>
        <tr>
            <td>footer 4</td>
            <td>footer 5</td>
            <td>footer 6</td>
        </tr>
    </tfoot>
</table>

```

## File: `test/functional/makemarkdown/cases/standard/table-complex.md`
```markdown
| head 1       | head 2       | head 3       |
| ------------ | ------------ | ------------ |
| row 1: col 1 | row 1: col 2 | row 1: col 3 |
| row 2: col 1 | row 2: col 2 | row 2: col 3 |
| footer 1     | footer 2     | footer 3     |
| footer 4     | footer 5     | footer 6     |
```

## File: `test/functional/makemarkdown/cases/standard/table-header-only.html`
```html
<table>
    <thead>
        <tr>
            <th>foo</th>
            <th>bar</th>
        </tr>
    </thead>
</table>
```

## File: `test/functional/makemarkdown/cases/standard/table-header-only.md`
```markdown
| foo | bar |
| --- | --- |
```

## File: `test/functional/makemarkdown/cases/standard/table-mix-malformed.html`
```html
<table></table>

<table>
  <caption>some stuff</caption>
</table>

```

## File: `test/functional/makemarkdown/cases/standard/table-no-header.html`
```html
<table>
  <thead>
    <tr>
      <td></td>
      <td></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>foo</td>
      <td>bar</td>
    </tr>
    <tr>
      <td>barista</td>
      <td>yes</td>
    </tr>
  </tbody>
</table>
```

## File: `test/functional/makemarkdown/cases/standard/table-no-header.md`
```markdown
|         |         |
| ------- | ------- |
| foo     | bar     |
| barista | yes     |
```

## File: `test/functional/makemarkdown/cases/standard/table-simple.html`
```html
<table>
    <tr>
        <td>head 1</td>
        <td>head 2</td>
        <td>head 3</td>
    </tr>
    <tr>
        <td>row 1: col 1</td>
        <td>row 1: col 2</td>
        <td>row 1: col 3</td>
    </tr>
    <tr>
        <td>row 2: col 1</td>
        <td>row 2: col 2</td>
        <td>row 2: col 3</td>
    </tr>
</table>
```

## File: `test/functional/makemarkdown/cases/standard/table-simple.md`
```markdown
| head 1       | head 2       | head 3       |
| ------------ | ------------ | ------------ |
| row 1: col 1 | row 1: col 2 | row 1: col 3 |
| row 2: col 1 | row 2: col 2 | row 2: col 3 |
```

## File: `test/mocks/mock-extension.js`
```javascript
var showdown = require('../../.build/showdown.js');

var ext = {
  type: 'lang',
  regex: /foo/g,
  replace: 'bar'
};

showdown.extension('mockextension', function () {
  'use strict';
  return [ext];
});

module.exports = ext;
```

## File: `test/performance/performance.js`
```javascript
/**
 * Created by Tivie on 21/12/2016.
 */
'use strict';
var fs = require('fs'),
    showdown = require('../../.build/showdown.js'),
    converter = new showdown.Converter(),
    pkg = require('../../package.json'),
    performance = require('./lib/performance.lib.js');

performance.setLibraryName(pkg.name);
performance.setVersion(pkg.version);
performance.setGithubLink('https://github.com/showdownjs/showdown/tree/');

var globals = {
      gHtmlBlocks:     [],
      gHtmlMdBlocks:   [],
      gHtmlSpans:      [],
      gUrls:           {},
      gTitles:         {},
      gDimensions:     {},
      gListLevel:      0,
      hashLinkCounts:  {},
      langExtensions:  [],
      outputModifiers: [],
      converter:       converter,
      ghCodeBlocks:    []
    },
    options = showdown.getOptions();

function runTests () {
  var testMDFile = fs.readFileSync('test/performance.testfile.md', 'utf8');
  new performance.Suite('Basic')
    .setOption('cycles', 50)
    .add('Simple "Hello World"', function () {
      converter.makeHtml('*Hello* **World**!');
    })
    .add('performance.testfile.md', {
      prepare: function () {
        return testMDFile;
      },
      test: function (mdText) {
        converter.makeHtml(mdText);
      }
    });
  new performance.Suite('subParsers')
    .setOption('cycles', 20)
    .add('hashHTMLBlocks', function () {
      showdown.subParser('makehtml.hashHTMLBlocks')(testMDFile, options, globals);
    })
    .add('anchors', function () {
      showdown.subParser('makehtml.links')(testMDFile, options, globals);
    })
    .add('blockQuotes', function () {
      showdown.subParser('makehtml.blockQuotes')(testMDFile, options, globals);
    })
    .add('codeBlocks', function () {
      showdown.subParser('makehtml.codeBlocks')(testMDFile, options, globals);
    })
    .add('codeSpans', function () {
      showdown.subParser('makehtml.codeSpans')(testMDFile, options, globals);
    })
    .add('detab', function () {
      showdown.subParser('makehtml.detab')(testMDFile, options, globals);
    })
    .add('encodeAmpsAndAngles', function () {
      showdown.subParser('makehtml.encodeAmpsAndAngles')(testMDFile, options, globals);
    })
    .add('encodeBackslashEscapes', function () {
      showdown.subParser('makehtml.encodeBackslashEscapes')(testMDFile, options, globals);
    })
    .add('encodeCode', function () {
      showdown.subParser('makehtml.encodeCode')(testMDFile, options, globals);
    })
    .add('escapeSpecialCharsWithinTagAttributes', function () {
      showdown.subParser('makehtml.escapeSpecialCharsWithinTagAttributes')(testMDFile, options, globals);
    })
    .add('githubCodeBlocks', function () {
      showdown.subParser('makehtml.githubCodeBlocks')(testMDFile, options, globals);
    })
    .add('hashBlock', function () {
      showdown.subParser('makehtml.hashBlock')(testMDFile, options, globals);
    })
    .add('hashElement', function () {
      showdown.subParser('makehtml.hashElement')(testMDFile, options, globals);
    })
    .add('hashHTMLSpans', function () {
      showdown.subParser('makehtml.hashHTMLSpans')(testMDFile, options, globals);
    })
    .add('hashPreCodeTags', function () {
      showdown.subParser('makehtml.hashPreCodeTags')(testMDFile, options, globals);
    })
    .add('headers', function () {
      showdown.subParser('makehtml.headers')(testMDFile, options, globals);
    })
    .add('horizontalRule', function () {
      showdown.subParser('makehtml.horizontalRule')(testMDFile, options, globals);
    })
    .add('images', function () {
      showdown.subParser('makehtml.images')(testMDFile, options, globals);
    })
    .add('italicsAndBold', function () {
      showdown.subParser('makehtml.italicsAndBold')(testMDFile, options, globals);
    })
    .add('lists', function () {
      showdown.subParser('makehtml.lists')(testMDFile, options, globals);
    })
    .add('outdent', function () {
      showdown.subParser('makehtml.outdent')(testMDFile, options, globals);
    })
    .add('paragraphs', function () {
      showdown.subParser('makehtml.paragraphs')(testMDFile, options, globals);
    })
    .add('spanGamut', function () {
      showdown.subParser('makehtml.spanGamut')(testMDFile, options, globals);
    })
    .add('strikethrough', function () {
      showdown.subParser('makehtml.strikethrough')(testMDFile, options, globals);
    })
    .add('stripLinkDefinitions', function () {
      showdown.subParser('makehtml.stripLinkDefinitions')(testMDFile, options, globals);
    })
    .add('tables', function () {
      showdown.subParser('makehtml.tables')(testMDFile, options, globals);
    })
    .add('unescapeSpecialChars', function () {
      showdown.subParser('makehtml.unescapeSpecialChars')(testMDFile, options, globals);
    });
}

function generateLogs () {
  performance.generateLog(null, null, true);
}

module.exports = {
  runTests: runTests,
  generateLogs: generateLogs
};
```

## File: `test/performance/lib/performance.lib.js`
```javascript
/**
 * Created by Tivie on 21/12/2016.
 */
'use strict';
var now = require('performance-now'),
    fs = require('fs'),
    semverSort = require('semver-sort'),
    performance = {
      version: '',
      libraryName: '',
      MDFile: 'performance.log.md',
      logFile: 'performance.json',
      testSuites: [],
      silent: false,
      githubLink: ''
    };

performance.setVersion = function (version) {
  performance.version = version;
};

performance.setLibraryName = function (name) {
  performance.libraryName = name;
};

performance.setGithubLink = function (url) {
  performance.githubLink = url;
};

performance.generateLog = function (filename, MDFilename, asTable) {
  filename = filename || performance.logFile;
  MDFilename = MDFilename || performance.MDFile;
  asTable = !!asTable;

  fs.closeSync(fs.openSync(filename, 'a'));

  var json = fs.readFileSync(filename),
      jsonParsed;

  try {
    jsonParsed = JSON.parse(json);
  } catch (err) {
    jsonParsed = {};
  }

  var jData = [];

  for (var i = 0; i < performance.testSuites.length; ++i) {
    // Suite
    var suiteName = performance.testSuites[i].getSuiteName(),
        cycles = performance.testSuites[i].getOption('cycles'),
        subJData = {
          suiteName: suiteName,
          cycles: cycles,
          tests: []
        },
        testSuite = performance.testSuites[i].getTests();
    //make sure tests have ran first
    if (!performance.testSuites[i].hasRun()) {
      performance.testSuites[i].run();
    }

    // loop through tests
    for (var ii = 0; ii < testSuite.length; ++ii) {
      // Test
      var test = testSuite[ii];
      subJData.tests.push({
        name: test.name,
        time: test.time,
        maxTime: test.maxTime,
        minTime: test.minTime
      });
    }
    jData.push(subJData);
  }
  jsonParsed[performance.version] = jData;

  //Sort jsonParsed
  var versions = [];
  for (var version in jsonParsed) {
    if (jsonParsed.hasOwnProperty(version)) {
      versions.push(version);
    }
  }

  semverSort.desc(versions);

  var finalJsonObj = {};

  for (i = 0; i < versions.length; ++i) {
    if (jsonParsed.hasOwnProperty(versions[i])) {
      finalJsonObj[versions[i]] = jsonParsed[versions[i]];
    }
  }

  fs.writeFileSync(filename, JSON.stringify(finalJsonObj));

  generateMD(MDFilename, finalJsonObj, asTable);
};

function generateMD (filename, obj, asTable) {
  fs.closeSync(fs.openSync(filename, 'w'));
  asTable = !!asTable;

  // generate MD
  var otp = '# Performance Tests for ' + performance.libraryName + '\n\n\n';

  for (var version in obj) {
    if (obj.hasOwnProperty(version)) {
      otp += '## [version ' + version + '](' + performance.githubLink + version + ')\n\n';
      var testSuite = obj[version];
      for (var i = 0; i < testSuite.length; ++i) {
        otp += '### Test Suite: ' + testSuite[i].suiteName + ' (' + testSuite[i].cycles + ' cycles)\n';
        var tests = testSuite[i].tests;
        if (asTable) {
          otp += '| test | avgTime | max | min |\n';
          otp += '|:-----|--------:|----:|----:|\n';
        }
        for (var ii = 0; ii < tests.length; ++ii) {
          var time = parseFloat(tests[ii].time).toFixed(3),
              maxTime = parseFloat(tests[ii].maxTime).toFixed(3),
              minTime = parseFloat(tests[ii].minTime).toFixed(3);
          if (asTable) {
            otp += '|' + tests[ii].name + '|' + time + '|' + maxTime + '|' + minTime + '|\n';
          } else {
            otp += ' - **' + tests[ii].name + ':** took ' + time + 'ms (*max: ' + maxTime + 'ms; min: ' + minTime + 'ms*)\n';
          }
        }
        otp += '\n';
      }
      otp += '\n';
    }
  }
  fs.writeFileSync(filename, otp);
}

performance.Suite = function (name) {
  var suiteName = name || '',
      tests = [],
      hasRunFlag = false,
      options = {
        cycles: 20
      };

  this.setOption = function (key, val) {
    options[key] = val;
    return this;
  };

  this.getOption = function (key) {
    return options[key];
  };

  this.add = function (name, obj) {
    if (typeof obj === 'function') {
      obj = {
        prepare: function () {},
        test: obj,
        teardown: function () {}
      };
    }

    if (!obj.hasOwnProperty('test')) {
      throw 'obj must have a property called test';
    }

    if (typeof obj.test !== 'function') {
      throw 'obj test property must be a function';
    }

    if (!obj.hasOwnProperty('prepare')) {
      obj.prepare = function () {};
    }

    if (!obj.hasOwnProperty('teardown')) {
      obj.teardown = function () {};
    }

    if (typeof obj.prepare !== 'function') {
      throw 'obj prepare property must be a function';
    }

    if (typeof obj.teardown !== 'function') {
      throw 'obj teardown property must be a function';
    }

    tests.push({
      name: name,
      obj: obj,
      time: 0,
      maxTime: 0,
      minTime: 0
    });
    return this;
  };

  this.run = function run () {
    var nn = options.cycles;
    console.log('running tests: ' + nn + ' cycles each.');
    for (var i = 0; i < tests.length; ++i) {
      var times = [],
          passVar = tests[i].obj.prepare();
      for (var ii = 0; ii < nn; ++ii) {
        var before = now();
        tests[i].obj.test(passVar);
        var after = now();
        times.push(after - before);
      }
      var total = times.reduce(function (a, b) {return a + b;}, 0);
      tests[i].time = total / options.cycles;
      tests[i].minTime = Math.min.apply(null, times);
      tests[i].maxTime = Math.max.apply(null, times);
      if (!options.silent) {
        console.log(tests[i].name + ' took an average of ' + tests[i].time + 'ms (min: ' + tests[i].minTime + 'ms; max: ' + tests[i].maxTime + 'ms');
      }
    }
    hasRunFlag = true;
    return this;
  };

  this.hasRun = function () {
    return hasRunFlag;
  };

  this.getSuiteName = function () {
    return suiteName;
  };

  this.getTests = function () {
    return tests;
  };

  performance.testSuites.push(this);
};

module.exports = performance;
```

## File: `test/unit/cli.js`
```javascript
var fs = require('fs'),
    path = require('path'),
    chai = require('chai'),
    expect = chai.expect,
    chaiMatch = require('chai-match'),
    execSync = require('child_process').execSync,
    spawnSync = require('child_process').spawnSync,
    cmd = 'node src/cli/cli.js',
    packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));

require('sinon');
chai.should();
chai.use(chaiMatch);

/**
 * Spawns a CLI process synchrously
 * @param {string|null} command
 * @param {string[]} args
 * @param {{}} [options]
 * @returns {{output: *, stdout: string, stderr: string, status: number}}
 */
function spawnCLI (command, args, options) {
  'use strict';
  var nargs = ['src/cli/cli.js'];
  if (command) { nargs.push(command);}
  args = nargs.concat(args);
  var otp = spawnSync('node', args, options),
      stdout = otp.stdout.toString(),
      stderr = otp.stderr.toString(),
      output = otp.output[0],
      status = otp.status;

  return {stdout: stdout, stderr: stderr, output: output, status: status};
}

describe('showdown cli', function () {
  'use strict';

  describe('without commands', function () {

    it('should display help if no commands are specified', function () {
      var proc = spawnCLI(null, [], {});
      proc.status.should.equal(1);
      proc.stderr.should.contain('CLI to Showdownjs markdown parser');
      proc.stderr.should.contain('Usage:');
      proc.stderr.should.contain('Options:');
      proc.stderr.should.contain('Commands:');
      proc.stdout.should.equal('');
    });

    describe('-h', function () {
      it('should display help', function () {
        var proc = spawnCLI(null, ['-h'], {});
        proc.status.should.equal(0);
        proc.stdout.should.contain('CLI to Showdownjs markdown parser');
        proc.stdout.should.contain('Usage:');
        proc.stdout.should.contain('Options:');
        proc.stdout.should.contain('Commands:');
        proc.stderr.should.equal('');
      });
    });

    describe('-v', function () {
      it('should display version', function () {
        let proc = spawnCLI(null, ['-V'], {}),
            verRegex = /^(\d{1,2}\.\d{1,3}\.\d{1,3}(?:-(alpha)|(beta)|(rc-\d{1,2})))?/;
        proc.status.should.equal(0);
        proc.stdout.should.match(verRegex);
        proc.stdout.should.match(verRegex).and.capture(0).equals(packageJson.version);
        proc.stderr.should.equal('');
      });
    });
  });

  describe('makehtml command', function () {

    describe('makehtml without flags', function () {
      it('should read from stdin and output to stdout', function () {
        var proc = spawnCLI('makehtml', [], {
          input: '**foo**',
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stdout.should.equal('<p><strong>foo</strong></p>');
        proc.stderr.should.not.equal('');
      });
    });

    describe('makehtml -p', function () {

      it('should enable a flavor', function () {
        var proc = spawnCLI('makehtml', ['-p', 'github'], {
          input: 'this is a :smile:', // test the emoji option as a proxy
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stderr.should.contain('Enabling flavor github...');
        proc.stdout.should.equal('<p>this is a 😄</p>');
        //'Here in London'.should.match(/(here|there) in (\w+)/i).and.capture(1).equals('London');
      });

      it('should give an error if a flavor is not recognised', function () {
        var proc = spawnCLI('makehtml', ['-p', 'foobar'], {
          input: '**foo**',
          encoding: 'utf-8'
        });
        proc.status.should.equal(1);
      });
    });

    describe('makehtml -c', function () {
      it('should not parse emoji if config option is not passed', function () {
        var proc = spawnCLI('makehtml', [], {
          input: 'this is a :smile:',
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stderr.should.not.contain('Enabling option emoji');
        proc.stdout.should.equal('<p>this is a :smile:</p>');
      });

      it('should enable a showdown option', function () {
        var proc = spawnCLI('makehtml', ['-c', 'emoji'], {
          input: 'this is a :smile:',
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stderr.should.contain('Enabling option emoji');
        proc.stdout.should.equal('<p>this is a 😄</p>');
      });

      it('should ignore unrecognized options', function () {
        var proc = spawnCLI('makehtml', ['-c', 'foobar'], {
          input: 'foo',
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stderr.should.contain('Enabling option foobar');
        proc.stdout.should.equal('<p>foo</p>');
      });

    });

    describe('makehtml -m', function () {

      it('should mute information', function () {
        var proc = spawnCLI('makehtml', ['-m', '-i'], {input: '**foo**'});
        proc.status.should.equal(0);
        expect(proc.output).to.be.null; // jshint ignore:line
        proc.stdout.should.equal('<p><strong>foo</strong></p>');
        proc.stderr.should.equal('');
      });

      it('should mute everything, even errors', function () {
        var proc = spawnCLI('makehtml', ['-m', '-i']);
        //proc.status.should.equal(0);
        expect(proc.output).to.be.null; // jshint ignore:line
        proc.stdout.should.equal('');
        proc.stderr.should.equal('');
      });

      it('should not mute parsed html', function () {
        var proc = spawnCLI('makehtml', ['-m', '-i'], {
          input: '**foo**',
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stdout.should.equal('<p><strong>foo</strong></p>');
        proc.stderr.should.equal('');
      });
    });

    describe('makehtml -q', function () {

      it('should not display information', function () {
        var proc = spawnCLI('makehtml', ['-q', '-i'], {input: '**foo**'});
        proc.status.should.equal(0);
        expect(proc.output).to.be.null; // jshint ignore:line
        proc.stdout.should.equal('<p><strong>foo</strong></p>');
        proc.stderr.should.match(/^\s*DONE!\s*$/);
      });

      it('should display errors', function () {
        var proc = spawnCLI('makehtml', ['-q', '-i', '-e', 'foo'], {input: 'f'});
        proc.status.should.equal(1);
        expect(proc.output).to.be.null; // jshint ignore:line
        proc.stdout.should.equal('');
        proc.stderr.should.match(/^ERROR:/);
      });

      it('should not mute parsed html', function () {
        var proc = spawnCLI('makehtml', ['-q', '-i'], {
          input: '**foo**',
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stdout.should.equal('<p><strong>foo</strong></p>');
        proc.stderr.should.match(/^\s*DONE!\s*$/);
      });
    });

    describe('makehtml -i -o', function () {
      it('should read from stdin and output to stdout', function () {
        var proc = spawnCLI('makehtml', ['-i', '-o'], {
          input: '**foo**',
          encoding: 'utf-8'
        });
        proc.status.should.equal(0);
        proc.stdout.should.equal('<p><strong>foo</strong></p>');
        proc.stderr.should.not.equal('');
      });
    });

    describe('makehtml -i <file> -o', function () {
      it('should read from a file and output to stdout', function () {
        var expectedOtp = fs.readFileSync('test/cli/basic.html', 'utf8').toString().trim(),
            proc = spawnCLI('makehtml', ['-i', 'test/cli/basic.md'], {encoding: 'utf-8'});

        proc.status.should.equal(0);
        proc.stdout.should.equal(expectedOtp);
        proc.stderr.should.not.equal('');
      });
    });

    describe('makehtml -i -o <file>', function () {
      it('should read from stdin and output to a file', function () {
        execSync(cmd + ' makehtml -m -i -o .build/io1.html', {
          encoding: 'utf8',
          input: '**foo**'
        });
        var otp = fs.readFileSync('.build/io1.html', 'utf8').toString().trim(),
            expectedOtp = '<p><strong>foo</strong></p>';

        otp.trim().should.equal(expectedOtp);
      });
    });

    describe('makehtml -i <file> -o <file>', function () {
      it('should read from a file and output to a file', function () {
        var expectedOtp = fs.readFileSync('test/cli/basic.html', 'utf8').toString().trim(),
            proc = spawnCLI('makehtml', ['-i', 'test/cli/basic.md', '-o', '.build/io2.html'], {encoding: 'utf-8'}),
            otp = fs.readFileSync('.build/io2.html', 'utf8').toString().trim();

        otp.trim().should.equal(expectedOtp);
        proc.stdout.should.not.equal(expectedOtp);
        proc.stderr.should.equal('');
        proc.status.should.equal(0);
      });
    });

    describe('makehtml -a', function () {
      it('should read from stdin and append to a file', function () {
        fs.writeFileSync('.build/io3.html', '<p>foo</p>');

        var expectedOtp = '<p>foo</p><p><strong>foo</strong></p>',
            proc = spawnCLI('makehtml', ['-i', '-o', '.build/io3.html', '-a'], {
              encoding: 'utf8',
              input: '**foo**'
            }),
            otp = fs.readFileSync('.build/io3.html', 'utf8').toString().trim();

        proc.status.should.equal(0);
        otp.trim().should.equal(expectedOtp);
        // since the output is to a file, messages are logged to stdout
        proc.stdout.should.not.equal(expectedOtp);
        // stderr should be empty
        proc.stderr.should.equal('');
      });

      it('should ignore -a flag if -o <file> is missing', function () {

        var expectedOtp = '<p><strong>foo</strong></p>',
            proc = spawnCLI('makehtml', ['-a'], {encoding: 'utf8', input: '**foo**'});
        proc.status.should.equal(0);
        proc.stderr.should.not.equal('');
        proc.stdout.should.equal(expectedOtp);
      });
    });

    describe('makehtml -e', function () {
      it('should load the extension', function () {
        var expectedOtp = '<p><strong>bar</strong></p>',
            extPath = path.resolve(__dirname + '/../mocks/mock-extension.js'),
            proc = spawnCLI('makehtml', ['-i', '-o', '-e', extPath], {
              encoding: 'utf8',
              input: '**foo**'
            });
        proc.status.should.equal(0, 'Process exited with error state');
        proc.stdout.trim().should.equal(expectedOtp);
      });
    });

  });
});
```

## File: `test/unit/showdown.Converter.js`
```javascript
/**
 * Created by Estevao on 31-05-2015.
 */
//let showdown = require('../../.build/showdown.js') || require('showdown');
chai.should();


describe('showdown.Converter', function () {
  'use strict';

  describe('option methods', function () {
    let converter = new showdown.Converter();

    it('setOption() should set option foo=baz', function () {
      converter.setOption('foo', 'baz');
    });

    it('getOption() should get option foo to equal baz', function () {
      converter.getOption('foo').should.equal('baz');
    });

    it('getOptions() should contain foo=baz', function () {
      let options = converter.getOptions();
      options.should.have.ownProperty('foo');
      options.foo.should.equal('baz');
    });
  });

  describe('metadata methods', function () {
    let converter = new showdown.Converter();

    it('_setMetadataPair() should set foo to bar', function () {
      converter._setMetadataPair('foo', 'bar');
      converter.getMetadata().should.eql({foo: 'bar'});
    });

    it('_setMetadata should set metadata to {baz: bazinga}', function () {
      converter._setMetadataRaw('{baz: bazinga}');
      converter.getMetadata(true).should.eql('{baz: bazinga}');
    });
  });

  describe('converter.setFlavor()', function () {

    /**
     * Test setFlavor('github')
     */
    describe('github', function () {
      let converter = new showdown.Converter(),
          ghOpts = showdown.getFlavorOptions('github');

      converter.setFlavor('github');

      for (let opt in ghOpts) {
        if (ghOpts.hasOwnProperty(opt)) {
          check(opt, ghOpts[opt]);
        }
      }
      function check (key, val) {
        it('should set ' + key + ' to ' + val, function () {
          converter.getOption(key).should.equal(val);
        });
      }
    });
  });

  describe('getFlavor method', function () {

    // reset showdown
    showdown.setFlavor('vanilla');

    describe('flavor', function () {
      it('should be vanilla by default', function () {
        let converter = new showdown.Converter();
        converter.getFlavor().should.equal('vanilla');
      });

      it('should be changed if global option is changed', function () {
        showdown.setFlavor('github');
        let converter = new showdown.Converter();
        converter.getFlavor().should.equal('github');
        showdown.setFlavor('vanilla');
      });

      it('should not be changed if converter is initialized before global change', function () {
        let converter = new showdown.Converter();
        showdown.setFlavor('github');
        converter.getFlavor().should.equal('vanilla');
        showdown.setFlavor('vanilla');
      });
    });
  });

  describe('extension methods', function () {
    let extObjMock = {
          type: 'lang',
          filter: function () {}
        },
        extObjFunc = function () {
          return extObjMock;
        };

    it('addExtension() should add an extension Object', function () {
      let converter = new showdown.Converter();
      converter.addExtension(extObjMock);
      converter.getAllExtensions().language.should.contain(extObjMock);
    });

    it('addExtension() should unwrap an extension wrapped in a function', function () {
      let converter = new showdown.Converter();

      converter.addExtension(extObjFunc);
      converter.getAllExtensions().language.should.contain(extObjMock);
    });

    it('useExtension() should use a previous registered extension in showdown', function () {
      showdown.extension('foo', extObjMock);
      let converter = new showdown.Converter();

      converter.useExtension('foo');
      converter.getAllExtensions().language.should.contain(extObjMock);
      showdown.resetExtensions();
    });

    it('removeExtension() should remove an added extension', function () {
      let converter = new showdown.Converter();
      converter.addExtension(extObjMock);

      converter.removeExtension(extObjMock);
      converter.getAllExtensions().language.should.not.contain(extObjMock);
    });
  });

  describe('events', function () {
    let events = [
      'makehtml.anchors',
      'makehtml.autoLinks',
      'makehtml.blockGamut',
      'makehtml.blockQuotes',
      'makehtml.codeBlocks',
      'makehtml.codeSpans',
      'makehtml.githubCodeBlocks',
      'makehtml.headers',
      'makehtml.images',
      'makehtml.italicsAndBold',
      'makehtml.lists',
      'makehtml.paragraph',
      'makehtml.spanGamut'
      //'strikeThrough',
      //'tables'
    ];

    for (let i = 0; i < events.length; ++i) {
      runListener(events[i] + '.before');
      runListener(events[i] + '.after');
    }

    function runListener (name) {
      it('should listen to ' + name, function () {
        let converter = new showdown.Converter();
        converter.listen(name, function (event) {
          let evtName = event.getName();
          let text = event.getCapturedText();
          evtName.should.equal(name.toLowerCase());
          text.should.match(/^[\s\S]*foo[\s\S]*$/);
          return text;
        })
          .makeHtml('foo');
      });
    }
  });
});
```

## File: `test/unit/showdown.Converter.makeHtml.js`
```javascript
/**
 * Created by Tivie on 15-01-2015.
 */
//let showdown = require('../../.build/showdown.js') || require('showdown');
chai.should();


describe('showdown.Converter', function () {
  'use strict';

  describe('Converter.options extensions', function () {
    let runCount;
    showdown.extension('testext', function () {
      return [{
        type: 'output',
        filter: function (text) {
          runCount = runCount + 1;
          return text;
        }
      }];
    });

    let converter = new showdown.Converter({extensions: ['testext']});

    it('output extensions should run once', function () {
      runCount = 0;
      converter.makeHtml('# testext');
      runCount.should.equal(1);
    });
  });

  describe('makeHtml() with option omitExtraWLInCodeBlocks', function () {
    let converter = new showdown.Converter({omitExtraWLInCodeBlocks: true}),
        text = 'var foo = bar;',
        html = converter.makeHtml('    ' + text);
    it('should omit extra line after code tag', function () {
      let expectedHtml = '<pre><code>' + text + '</code></pre>';
      html.should.equal(expectedHtml);
    });
  });

  describe('makeHtml() with option prefixHeaderId', function () {
    let converter = new showdown.Converter(),
        text = 'foo header';

    it('should prefix header id with "section"', function () {
      converter.setOption('prefixHeaderId', true);
      let html = converter.makeHtml('# ' + text),
          expectedHtml = '<h1 id="sectionfooheader">' + text + '</h1>';
      html.should.equal(expectedHtml);
    });

    it('should prefix header id with custom string', function () {
      converter.setOption('prefixHeaderId', 'blabla');
      let html = converter.makeHtml('# ' + text),
          expectedHtml = '<h1 id="blablafooheader">' + text + '</h1>';
      html.should.equal(expectedHtml);
    });
  });

  describe('makeHtml() with option metadata', function () {
    let converter = new showdown.Converter(),
        text1 =
          '---SIMPLE\n' +
          'foo: bar\n' +
          'baz: bazinga\n' +
          '---\n',
        text2 =
          '---TIVIE\n' +
          'a: b\n' +
          'c: 123\n' +
          '---\n';

    it('should correctly set metadata', function () {
      converter.setOption('metadata', true);

      let expectedHtml = '',
          expectedObj = {foo: 'bar', baz: 'bazinga'},
          expectedRaw = 'foo: bar\nbaz: bazinga',
          expectedFormat = 'SIMPLE';
      converter.makeHtml(text1).should.equal(expectedHtml);
      converter.getMetadata().should.eql(expectedObj);
      converter.getMetadata(true).should.equal(expectedRaw);
      converter.getMetadataFormat().should.equal(expectedFormat);
    });

    it('consecutive calls should reset metadata', function () {
      converter.makeHtml(text2);
      let expectedObj = {a: 'b', c: '123'},
          expectedRaw = 'a: b\nc: 123',
          expectedFormat = 'TIVIE';
      converter.getMetadata().should.eql(expectedObj);
      converter.getMetadata(true).should.equal(expectedRaw);
      converter.getMetadataFormat().should.equal(expectedFormat);
    });
  });
});
```

## File: `test/unit/showdown.Converter.makeMarkdown.js`
```javascript
/**
 * Created by Estevao on 15-01-2015.
 */
//let showdown = require('../../.build/showdown.js') || require('showdown');
chai.should();

describe('showdown.Converter', function () {
  'use strict';


  describe('makeMarkdown()', function () {
    let converter = new showdown.Converter();

    it('should parse a simple html string', function () {
      let html = '<a href="/somefoo.html">a link</a>\n';
      let md   = '[a link](</somefoo.html>)';

      converter.makeMarkdown(html).should.equal(md);
    });

  });
});
```

## File: `test/unit/showdown.helpers.js`
```javascript
/**
 * Created by Tivie on 27/01/2017.
 */
chai.should();
/*jshint expr: true*/
/*jshint -W053 */
/*jshint -W010 */
/*jshint -W009 */

describe('encodeEmailAddress()', function () {
  'use strict';
  let encoder = showdown.helper.encodeEmailAddress,
      email = 'foobar@example.com',
      encodedEmail = encoder(email),
      encodedEmail2 = encoder(email);

  it('should encode email', function () {
    encodedEmail.should.not.equal(email);
  });

  it('should encode email determinated', function () {
    encodedEmail.should.equal(encodedEmail2);
  });

  it('should decode to original email', function () {
    let decodedEmail = encodedEmail.replace(/&#(.+?);/g, function (wm, cc) {
      if (cc.charAt(0) === 'x') {
        //hex
        return String.fromCharCode('0' + cc);
      } else {
        //dec
        return String.fromCharCode(cc);
      }
    });
    decodedEmail.should.equal(email);
  });
});

describe('isString()', function () {
  'use strict';
  let isString = showdown.helper.isString;

  it('should return true for new String Object', function () {
    isString(new String('some string')).should.be.true;
  });

  it('should return true for String Object', function () {
    isString(String('some string')).should.be.true;
  });

  it('should return true for string literal', function () {
    isString('some string').should.be.true;
  });

  it('should return false for integers', function () {
    isString(5).should.be.false;
  });

  it('should return false for random objects', function () {
    isString({foo: 'bar'}).should.be.false;
  });

  it('should return false for arrays', function () {
    isString(['bar']).should.be.false;
  });
});

describe('isFunction()', function () {
  'use strict';
  let isFunction = showdown.helper.isFunction;

  it('should return true for closures', function () {
    isFunction(function () {}).should.be.true;
  });

  it('should return true for defined functions', function () {
    function foo () {}
    isFunction(foo).should.be.true;
  });

  it('should return true for function letiables', function () {
    let bar = function () {};
    isFunction(bar).should.be.true;
  });

  it('should return false for hash objects', function () {
    isFunction({}).should.be.false;
  });

  it('should return false for objects', function () {
    isFunction(new Object ()).should.be.false;
  });

  it('should return false for string primitives', function () {
    isFunction('foo').should.be.false;
  });
});

describe('isArray()', function () {
  'use strict';
  let isArray = showdown.helper.isArray;

  it('should return true for short syntax arrays', function () {
    isArray([]).should.be.true;
  });

  it('should return true for array objects', function () {
    let myArr = new Array();
    isArray(myArr).should.be.true;
  });

  it('should return false for functions', function () {
    isArray(function () {}).should.be.false;
    function baz () {}
    isArray(baz).should.be.false;
  });

  it('should return false for objects', function () {
    isArray({}).should.be.false;
    isArray(new Object ()).should.be.false;
  });

  it('should return false for strings', function () {
    isArray('foo').should.be.false;
    isArray(new String('foo')).should.be.false;
  });
});

describe('isUndefined()', function () {
  'use strict';
  let isUndefined = showdown.helper.isUndefined;

  it('should return true if nothing is passed', function () {
    isUndefined().should.be.true;
  });

  it('should return true if a letiable is initialized but not defined', function () {
    let myVar;
    isUndefined(myVar).should.be.true;
  });

  it('should return false for null', function () {
    isUndefined(null).should.be.false;
  });

  it('should return false for 0', function () {
    isUndefined(0).should.be.false;
  });

  it('should return false for empty string', function () {
    isUndefined('').should.be.false;
  });

  it('should return false for empty booleans false or true', function () {
    isUndefined(false).should.be.false;
    isUndefined(true).should.be.false;
  });

  it('should return false for anything not undefined', function () {
    isUndefined('foo').should.be.false;
    isUndefined(2).should.be.false;
    isUndefined({}).should.be.false;
  });
});

describe('stdExtName()', function () {
  'use strict';
  let stdExtName = showdown.helper.stdExtName;

  it('should remove certain chars', function () {
    let str = 'bla_-  \nbla';
    //[_?*+\/\\.^-]
    stdExtName(str).should.not.match(/[_?*+\/\\.^-]/g);
  });
  it('should make everything lowercase', function () {
    let str = 'BLABLA';
    //[_?*+\/\\.^-]
    stdExtName(str).should.equal('blabla');
  });
});

describe('forEach()', function () {
  'use strict';
  let forEach = showdown.helper.forEach;

  it('should throw an error if first parameter is undefined', function () {
    (function () {forEach();}).should.throw('obj param is required');
  });

  it('should throw an error if second parameter is undefined', function () {
    (function () {forEach([]);}).should.throw('callback param is required');
  });

  it('should throw an error if second parameter is not a function', function () {
    (function () {forEach([], 'foo');}).should.throw('callback param must be a function/closure');
  });

  it('should throw an error if first parameter is not an object or an array', function () {
    (function () {forEach('foo', function () {});}).should.throw('obj does not seem to be an array or an iterable object');
  });

  it('should not throw even if object is empty', function () {
    (function () {forEach({}, function () {});}).should.not.throw();
  });

  it('should iterate array items', function () {
    let myArray = ['banana', 'orange', 'grape'];
    forEach(myArray, function (val, key, obj) {
      key.should.be.a('number');
      (key % 1).should.equal(0);
      val.should.equal(myArray[key]);
      obj.should.equal(myArray);
    });
  });

  it('should iterate over object properties', function () {
    let myObj = {foo: 'banana', bar: 'orange', baz: 'grape'};
    forEach(myObj, function (val, key, obj) {
      myObj.should.have.ownProperty(key);
      val.should.equal(myObj[key]);
      obj.should.equal(myObj);
    });
  });

  it('should iterate only over object own properties', function () {
    let Obj1 = {foo: 'banana'},
        myObj = Object.create(Obj1);
    myObj.bar = 'orange';
    myObj.baz = 'grape';

    myObj.should.have.ownProperty('bar');
    myObj.should.have.ownProperty('baz');
    myObj.should.not.have.ownProperty('foo');

    forEach(myObj, function (val, key) {
      key.should.not.equal('foo');
    });
  });
});

describe('matchRecursiveRegExp()', function () {
  'use strict';

  let rRegExp = showdown.helper.matchRecursiveRegExp;

  it('should match nested elements', function () {
    let result = rRegExp('<div><div>a</div></div>', '<div\\b[^>]*>', '</div>', 'gim');
    result.should.deep.equal([['<div><div>a</div></div>', '<div>a</div>', '<div>', '</div>']]);
  });

});

describe('repeat()', function () {
  'use strict';
  it('work produce the same output as String.prototype.repeat()', function () {
    if (typeof String.prototype.repeat !== 'undefined') {
      let str = 'foo',
          expected = str.repeat(100),
          actual = showdown.helper.repeat(str, 100);
      expected.should.equal(actual);
    }
  });
});
```

## File: `test/unit/showdown.js`
```javascript
/**
 * Created by Tivie on 27/01/2017.
 */
//let showdown = require('../../.build/showdown.js') || require('showdown');

describe('showdown.options', function () {
  'use strict';

  describe('setOption() and getOption()', function () {
    it('should set option foo=bar', function () {
      showdown.setOption('foo', 'bar');
      showdown.getOption('foo').should.equal('bar');
      showdown.resetOptions();
      (typeof showdown.getOption('foo')).should.equal('undefined');
    });
  });

  describe('getDefaultOptions()', function () {
    it('should get default options', function () {
      let opts = getDefaultOpts(true);
      expect(showdown.getDefaultOptions()).to.be.eql(opts);
    });
  });
});

describe('showdown.extension()', function () {
  'use strict';

  let extObjMock = {
        type: 'lang',
        filter: function () {}
      },
      extObjFunc = function () {
        return extObjMock;
      };

  /*
  // very flimsy test
  describe('file loading', function () {

    beforeEach(function () {
      this.extension = require('../mocks/mock-extension');
    });

    it('should register an extension from a file', function () {
      showdown.extension('mockextension').should.be.an('array');
      showdown.extension('mockextension').should.eql([this.extension]);
    });

    afterEach(function () {
      showdown.resetExtensions();
    });

  });
  */

  describe('objects', function () {
    it('should register an extension object', function () {
      showdown.extension('foo', extObjMock);
      showdown.extension('foo').should.eql([extObjMock]);
    });

    it('should register an extension function', function () {
      showdown.extension('bar', extObjFunc);
      showdown.extension('bar').should.eql([extObjMock]);
    });

    it('should register a listener extension', function () {
      showdown.extension('baz', {
        type: 'listener',
        listeners: {
          foo: function (name, txt) {
            return txt;
          }
        }
      });
    });

    it('should refuse to register a generic object', function () {
      let fn = function () {
        showdown.extension('foo', {});
      };
      expect(fn).to.throw();
    });

    it('should refuse to register an extension with invalid type', function () {
      let fn = function () {
        showdown.extension('foo', {
          type: 'foo'
        });
      };
      expect(fn).to.throw(/type .+? is not recognized\. Valid values: "lang\/language", "output\/html" or "listener"/);
    });

    it('should refuse to register an extension without regex or filter', function () {
      let fn = function () {
        showdown.extension('foo', {
          type: 'lang'
        });
      };
      expect(fn).to.throw(/extensions must define either a "regex" property or a "filter" method/);
    });

    it('should refuse to register a listener extension without a listeners property', function () {
      let fn = function () {
        showdown.extension('foo', {
          type: 'listener'
        });
      };
      expect(fn).to.throw(/Extensions of type "listener" must have a property called "listeners"/);
    });

    afterEach(function () {
      showdown.resetExtensions();
    });

  });

});

describe('showdown.getAllExtensions()', function () {
  'use strict';
  let extObjMock = {
    type: 'lang',
    filter: function () {}
  };

  it('should return all extensions', function () {
    showdown.extension('bar', extObjMock);
    showdown.getAllExtensions().should.eql({bar: [extObjMock]});
  });
});

describe('showdown.setFlavor()', function () {
  'use strict';
  it('should set flavor to github', function () {
    showdown.setFlavor('github');
    showdown.getFlavor().should.equal('github');
    showdown.setFlavor('vanilla');
  });

  it('should set options correctly', function () {
    showdown.setFlavor('github');
    let ghOpts = showdown.getFlavorOptions('github'),
        shOpts = showdown.getOptions();
    for (let opt in ghOpts) {
      if (ghOpts.hasOwnProperty(opt)) {
        shOpts.should.have.property(opt);
        shOpts[opt].should.equal(ghOpts[opt]);
      }
    }
    showdown.setFlavor('vanilla');
  });

  it('should switch between flavors correctly', function () {
    showdown.setFlavor('github');
    let ghOpts = showdown.getFlavorOptions('github'),
        shOpts = showdown.getOptions(),
        dfOpts = showdown.getDefaultOptions();
    for (let opt in dfOpts) {
      if (ghOpts.hasOwnProperty(opt)) {
        shOpts[opt].should.equal(ghOpts[opt]);
      } else {
        shOpts[opt].should.equal(dfOpts[opt]);
      }
    }
    showdown.setFlavor('original');
    let orOpts = showdown.getFlavorOptions('original');
    shOpts = showdown.getOptions();
    for (let opt in dfOpts) {
      if (orOpts.hasOwnProperty(opt)) {
        shOpts[opt].should.equal(orOpts[opt]);
      } else {
        shOpts[opt].should.equal(dfOpts[opt]);
      }
    }
    showdown.setFlavor('vanilla');
  });
});
```

