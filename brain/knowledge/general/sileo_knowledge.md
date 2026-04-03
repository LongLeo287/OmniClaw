---
id: sileo-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.752643
---

# KNOWLEDGE EXTRACT: sileo
> **Extracted on:** 2026-03-30 17:53:21
> **Source:** sileo

---

## File: `.gitignore`
```
dist
node_modules
package-lock.json
```

## File: `bun.lock`
```
{
  "lockfileVersion": 1,
  "workspaces": {
    "": {
      "name": "sileo",
      "dependencies": {
        "motion": "^12.34.0",
      },
      "devDependencies": {
        "bunchee": "^6.9.4",
      },
      "peerDependencies": {
        "react": ">=18",
        "react-dom": ">=18",
      },
    },
  },
  "packages": {
    "@babel/code-frame": ["@babel/code-frame@7.29.0", "", { "dependencies": { "@babel/helper-validator-identifier": "^7.28.5", "js-tokens": "^4.0.0", "picocolors": "^1.1.1" } }, "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw=="],

    "@babel/helper-validator-identifier": ["@babel/helper-validator-identifier@7.28.5", "", {}, "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q=="],

    "@fastify/deepmerge": ["@fastify/deepmerge@1.3.0", "", {}, "sha512-J8TOSBq3SoZbDhM9+R/u77hP93gz/rajSA+K2kGyijPpORPWUXHUpTaleoj+92As0S9uPRP7Oi8IqMf0u+ro6A=="],

    "@jridgewell/sourcemap-codec": ["@jridgewell/sourcemap-codec@1.5.5", "", {}, "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og=="],

    "@rollup/plugin-commonjs": ["@rollup/plugin-commonjs@29.0.0", "", { "dependencies": { "@rollup/pluginutils": "^5.0.1", "commondir": "^1.0.1", "estree-walker": "^2.0.2", "fdir": "^6.2.0", "is-reference": "1.2.1", "magic-string": "^0.30.3", "picomatch": "^4.0.2" }, "peerDependencies": { "rollup": "^2.68.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-U2YHaxR2cU/yAiwKJtJRhnyLk7cifnQw0zUpISsocBDoHDJn+HTV74ABqnwr5bEgWUwFZC9oFL6wLe21lHu5eQ=="],

    "@rollup/plugin-json": ["@rollup/plugin-json@6.1.0", "", { "dependencies": { "@rollup/pluginutils": "^5.1.0" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-EGI2te5ENk1coGeADSIwZ7G2Q8CJS2sF120T7jLw4xFw9n7wIOXHo+kIYRAoVpJAN+kmqZSoO3Fp4JtoNF4ReA=="],

    "@rollup/plugin-node-resolve": ["@rollup/plugin-node-resolve@16.0.3", "", { "dependencies": { "@rollup/pluginutils": "^5.0.1", "@types/resolve": "1.20.2", "deepmerge": "^4.2.2", "is-module": "^1.0.0", "resolve": "^1.22.1" }, "peerDependencies": { "rollup": "^2.78.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-lUYM3UBGuM93CnMPG1YocWu7X802BrNF3jW2zny5gQyLQgRFJhV1Sq0Zi74+dh/6NBx1DxFC4b4GXg9wUCG5Qg=="],

    "@rollup/plugin-replace": ["@rollup/plugin-replace@6.0.3", "", { "dependencies": { "@rollup/pluginutils": "^5.0.1", "magic-string": "^0.30.3" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-J4RZarRvQAm5IF0/LwUUg+obsm+xZhYnbMXmXROyoSE1ATJe3oXSb9L5MMppdxP2ylNSjv6zFBwKYjcKMucVfA=="],

    "@rollup/plugin-wasm": ["@rollup/plugin-wasm@6.2.2", "", { "dependencies": { "@rollup/pluginutils": "^5.0.2" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-gpC4R1G9Ni92ZIRTexqbhX7U+9estZrbhP+9SRb0DW9xpB9g7j34r+J2hqrcW/lRI7dJaU84MxZM0Rt82tqYPQ=="],

    "@rollup/pluginutils": ["@rollup/pluginutils@5.3.0", "", { "dependencies": { "@types/estree": "^1.0.0", "estree-walker": "^2.0.2", "picomatch": "^4.0.2" }, "peerDependencies": { "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0" }, "optionalPeers": ["rollup"] }, "sha512-5EdhGZtnu3V88ces7s53hhfK5KSASnJZv8Lulpc04cWO3REESroJXg73DFsOmgbU2BhwV0E20bu2IDZb3VKW4Q=="],

    "@rollup/rollup-android-arm-eabi": ["@rollup/rollup-android-arm-eabi@4.57.1", "", { "os": "android", "cpu": "arm" }, "sha512-A6ehUVSiSaaliTxai040ZpZ2zTevHYbvu/lDoeAteHI8QnaosIzm4qwtezfRg1jOYaUmnzLX1AOD6Z+UJjtifg=="],

    "@rollup/rollup-android-arm64": ["@rollup/rollup-android-arm64@4.57.1", "", { "os": "android", "cpu": "arm64" }, "sha512-dQaAddCY9YgkFHZcFNS/606Exo8vcLHwArFZ7vxXq4rigo2bb494/xKMMwRRQW6ug7Js6yXmBZhSBRuBvCCQ3w=="],

    "@rollup/rollup-darwin-arm64": ["@rollup/rollup-darwin-arm64@4.57.1", "", { "os": "darwin", "cpu": "arm64" }, "sha512-crNPrwJOrRxagUYeMn/DZwqN88SDmwaJ8Cvi/TN1HnWBU7GwknckyosC2gd0IqYRsHDEnXf328o9/HC6OkPgOg=="],

    "@rollup/rollup-darwin-x64": ["@rollup/rollup-darwin-x64@4.57.1", "", { "os": "darwin", "cpu": "x64" }, "sha512-Ji8g8ChVbKrhFtig5QBV7iMaJrGtpHelkB3lsaKzadFBe58gmjfGXAOfI5FV0lYMH8wiqsxKQ1C9B0YTRXVy4w=="],

    "@rollup/rollup-freebsd-arm64": ["@rollup/rollup-freebsd-arm64@4.57.1", "", { "os": "freebsd", "cpu": "arm64" }, "sha512-R+/WwhsjmwodAcz65guCGFRkMb4gKWTcIeLy60JJQbXrJ97BOXHxnkPFrP+YwFlaS0m+uWJTstrUA9o+UchFug=="],

    "@rollup/rollup-freebsd-x64": ["@rollup/rollup-freebsd-x64@4.57.1", "", { "os": "freebsd", "cpu": "x64" }, "sha512-IEQTCHeiTOnAUC3IDQdzRAGj3jOAYNr9kBguI7MQAAZK3caezRrg0GxAb6Hchg4lxdZEI5Oq3iov/w/hnFWY9Q=="],

    "@rollup/rollup-linux-arm-gnueabihf": ["@rollup/rollup-linux-arm-gnueabihf@4.57.1", "", { "os": "linux", "cpu": "arm" }, "sha512-F8sWbhZ7tyuEfsmOxwc2giKDQzN3+kuBLPwwZGyVkLlKGdV1nvnNwYD0fKQ8+XS6hp9nY7B+ZeK01EBUE7aHaw=="],

    "@rollup/rollup-linux-arm-musleabihf": ["@rollup/rollup-linux-arm-musleabihf@4.57.1", "", { "os": "linux", "cpu": "arm" }, "sha512-rGfNUfn0GIeXtBP1wL5MnzSj98+PZe/AXaGBCRmT0ts80lU5CATYGxXukeTX39XBKsxzFpEeK+Mrp9faXOlmrw=="],

    "@rollup/rollup-linux-arm64-gnu": ["@rollup/rollup-linux-arm64-gnu@4.57.1", "", { "os": "linux", "cpu": "arm64" }, "sha512-MMtej3YHWeg/0klK2Qodf3yrNzz6CGjo2UntLvk2RSPlhzgLvYEB3frRvbEF2wRKh1Z2fDIg9KRPe1fawv7C+g=="],

    "@rollup/rollup-linux-arm64-musl": ["@rollup/rollup-linux-arm64-musl@4.57.1", "", { "os": "linux", "cpu": "arm64" }, "sha512-1a/qhaaOXhqXGpMFMET9VqwZakkljWHLmZOX48R0I/YLbhdxr1m4gtG1Hq7++VhVUmf+L3sTAf9op4JlhQ5u1Q=="],

    "@rollup/rollup-linux-loong64-gnu": ["@rollup/rollup-linux-loong64-gnu@4.57.1", "", { "os": "linux", "cpu": "none" }, "sha512-QWO6RQTZ/cqYtJMtxhkRkidoNGXc7ERPbZN7dVW5SdURuLeVU7lwKMpo18XdcmpWYd0qsP1bwKPf7DNSUinhvA=="],

    "@rollup/rollup-linux-loong64-musl": ["@rollup/rollup-linux-loong64-musl@4.57.1", "", { "os": "linux", "cpu": "none" }, "sha512-xpObYIf+8gprgWaPP32xiN5RVTi/s5FCR+XMXSKmhfoJjrpRAjCuuqQXyxUa/eJTdAE6eJ+KDKaoEqjZQxh3Gw=="],

    "@rollup/rollup-linux-ppc64-gnu": ["@rollup/rollup-linux-ppc64-gnu@4.57.1", "", { "os": "linux", "cpu": "ppc64" }, "sha512-4BrCgrpZo4hvzMDKRqEaW1zeecScDCR+2nZ86ATLhAoJ5FQ+lbHVD3ttKe74/c7tNT9c6F2viwB3ufwp01Oh2w=="],

    "@rollup/rollup-linux-ppc64-musl": ["@rollup/rollup-linux-ppc64-musl@4.57.1", "", { "os": "linux", "cpu": "ppc64" }, "sha512-NOlUuzesGauESAyEYFSe3QTUguL+lvrN1HtwEEsU2rOwdUDeTMJdO5dUYl/2hKf9jWydJrO9OL/XSSf65R5+Xw=="],

    "@rollup/rollup-linux-riscv64-gnu": ["@rollup/rollup-linux-riscv64-gnu@4.57.1", "", { "os": "linux", "cpu": "none" }, "sha512-ptA88htVp0AwUUqhVghwDIKlvJMD/fmL/wrQj99PRHFRAG6Z5nbWoWG4o81Nt9FT+IuqUQi+L31ZKAFeJ5Is+A=="],

    "@rollup/rollup-linux-riscv64-musl": ["@rollup/rollup-linux-riscv64-musl@4.57.1", "", { "os": "linux", "cpu": "none" }, "sha512-S51t7aMMTNdmAMPpBg7OOsTdn4tySRQvklmL3RpDRyknk87+Sp3xaumlatU+ppQ+5raY7sSTcC2beGgvhENfuw=="],

    "@rollup/rollup-linux-s390x-gnu": ["@rollup/rollup-linux-s390x-gnu@4.57.1", "", { "os": "linux", "cpu": "s390x" }, "sha512-Bl00OFnVFkL82FHbEqy3k5CUCKH6OEJL54KCyx2oqsmZnFTR8IoNqBF+mjQVcRCT5sB6yOvK8A37LNm/kPJiZg=="],

    "@rollup/rollup-linux-x64-gnu": ["@rollup/rollup-linux-x64-gnu@4.57.1", "", { "os": "linux", "cpu": "x64" }, "sha512-ABca4ceT4N+Tv/GtotnWAeXZUZuM/9AQyCyKYyKnpk4yoA7QIAuBt6Hkgpw8kActYlew2mvckXkvx0FfoInnLg=="],

    "@rollup/rollup-linux-x64-musl": ["@rollup/rollup-linux-x64-musl@4.57.1", "", { "os": "linux", "cpu": "x64" }, "sha512-HFps0JeGtuOR2convgRRkHCekD7j+gdAuXM+/i6kGzQtFhlCtQkpwtNzkNj6QhCDp7DRJ7+qC/1Vg2jt5iSOFw=="],

    "@rollup/rollup-openbsd-x64": ["@rollup/rollup-openbsd-x64@4.57.1", "", { "os": "openbsd", "cpu": "x64" }, "sha512-H+hXEv9gdVQuDTgnqD+SQffoWoc0Of59AStSzTEj/feWTBAnSfSD3+Dql1ZruJQxmykT/JVY0dE8Ka7z0DH1hw=="],

    "@rollup/rollup-openharmony-arm64": ["@rollup/rollup-openharmony-arm64@4.57.1", "", { "os": "none", "cpu": "arm64" }, "sha512-4wYoDpNg6o/oPximyc/NG+mYUejZrCU2q+2w6YZqrAs2UcNUChIZXjtafAiiZSUc7On8v5NyNj34Kzj/Ltk6dQ=="],

    "@rollup/rollup-win32-arm64-msvc": ["@rollup/rollup-win32-arm64-msvc@4.57.1", "", { "os": "win32", "cpu": "arm64" }, "sha512-O54mtsV/6LW3P8qdTcamQmuC990HDfR71lo44oZMZlXU4tzLrbvTii87Ni9opq60ds0YzuAlEr/GNwuNluZyMQ=="],

    "@rollup/rollup-win32-ia32-msvc": ["@rollup/rollup-win32-ia32-msvc@4.57.1", "", { "os": "win32", "cpu": "ia32" }, "sha512-P3dLS+IerxCT/7D2q2FYcRdWRl22dNbrbBEtxdWhXrfIMPP9lQhb5h4Du04mdl5Woq05jVCDPCMF7Ub0NAjIew=="],

    "@rollup/rollup-win32-x64-gnu": ["@rollup/rollup-win32-x64-gnu@4.57.1", "", { "os": "win32", "cpu": "x64" }, "sha512-VMBH2eOOaKGtIJYleXsi2B8CPVADrh+TyNxJ4mWPnKfLB/DBUmzW+5m1xUrcwWoMfSLagIRpjUFeW5CO5hyciQ=="],

    "@rollup/rollup-win32-x64-msvc": ["@rollup/rollup-win32-x64-msvc@4.57.1", "", { "os": "win32", "cpu": "x64" }, "sha512-mxRFDdHIWRxg3UfIIAwCm6NzvxG0jDX/wBN6KsQFTvKFqqg9vTrWUE68qEjHt19A5wwx5X5aUi2zuZT7YR0jrA=="],

    "@swc/core": ["@swc/core@1.15.11", "", { "dependencies": { "@swc/counter": "^0.1.3", "@swc/types": "^0.1.25" }, "optionalDependencies": { "@swc/core-darwin-arm64": "1.15.11", "@swc/core-darwin-x64": "1.15.11", "@swc/core-linux-arm-gnueabihf": "1.15.11", "@swc/core-linux-arm64-gnu": "1.15.11", "@swc/core-linux-arm64-musl": "1.15.11", "@swc/core-linux-x64-gnu": "1.15.11", "@swc/core-linux-x64-musl": "1.15.11", "@swc/core-win32-arm64-msvc": "1.15.11", "@swc/core-win32-ia32-msvc": "1.15.11", "@swc/core-win32-x64-msvc": "1.15.11" }, "peerDependencies": { "@swc/helpers": ">=0.5.17" }, "optionalPeers": ["@swc/helpers"] }, "sha512-iLmLTodbYxU39HhMPaMUooPwO/zqJWvsqkrXv1ZI38rMb048p6N7qtAtTp37sw9NzSrvH6oli8EdDygo09IZ/w=="],

    "@swc/core-darwin-arm64": ["@swc/core-darwin-arm64@1.15.11", "", { "os": "darwin", "cpu": "arm64" }, "sha512-QoIupRWVH8AF1TgxYyeA5nS18dtqMuxNwchjBIwJo3RdwLEFiJq6onOx9JAxHtuPwUkIVuU2Xbp+jCJ7Vzmgtg=="],

    "@swc/core-darwin-x64": ["@swc/core-darwin-x64@1.15.11", "", { "os": "darwin", "cpu": "x64" }, "sha512-S52Gu1QtPSfBYDiejlcfp9GlN+NjTZBRRNsz8PNwBgSE626/FUf2PcllVUix7jqkoMC+t0rS8t+2/aSWlMuQtA=="],

    "@swc/core-linux-arm-gnueabihf": ["@swc/core-linux-arm-gnueabihf@1.15.11", "", { "os": "linux", "cpu": "arm" }, "sha512-lXJs8oXo6Z4yCpimpQ8vPeCjkgoHu5NoMvmJZ8qxDyU99KVdg6KwU9H79vzrmB+HfH+dCZ7JGMqMF//f8Cfvdg=="],

    "@swc/core-linux-arm64-gnu": ["@swc/core-linux-arm64-gnu@1.15.11", "", { "os": "linux", "cpu": "arm64" }, "sha512-chRsz1K52/vj8Mfq/QOugVphlKPWlMh10V99qfH41hbGvwAU6xSPd681upO4bKiOr9+mRIZZW+EfJqY42ZzRyA=="],

    "@swc/core-linux-arm64-musl": ["@swc/core-linux-arm64-musl@1.15.11", "", { "os": "linux", "cpu": "arm64" }, "sha512-PYftgsTaGnfDK4m6/dty9ryK1FbLk+LosDJ/RJR2nkXGc8rd+WenXIlvHjWULiBVnS1RsjHHOXmTS4nDhe0v0w=="],

    "@swc/core-linux-x64-gnu": ["@swc/core-linux-x64-gnu@1.15.11", "", { "os": "linux", "cpu": "x64" }, "sha512-DKtnJKIHiZdARyTKiX7zdRjiDS1KihkQWatQiCHMv+zc2sfwb4Glrodx2VLOX4rsa92NLR0Sw8WLcPEMFY1szQ=="],

    "@swc/core-linux-x64-musl": ["@swc/core-linux-x64-musl@1.15.11", "", { "os": "linux", "cpu": "x64" }, "sha512-mUjjntHj4+8WBaiDe5UwRNHuEzLjIWBTSGTw0JT9+C9/Yyuh4KQqlcEQ3ro6GkHmBGXBFpGIj/o5VMyRWfVfWw=="],

    "@swc/core-win32-arm64-msvc": ["@swc/core-win32-arm64-msvc@1.15.11", "", { "os": "win32", "cpu": "arm64" }, "sha512-ZkNNG5zL49YpaFzfl6fskNOSxtcZ5uOYmWBkY4wVAvgbSAQzLRVBp+xArGWh2oXlY/WgL99zQSGTv7RI5E6nzA=="],

    "@swc/core-win32-ia32-msvc": ["@swc/core-win32-ia32-msvc@1.15.11", "", { "os": "win32", "cpu": "ia32" }, "sha512-6XnzORkZCQzvTQ6cPrU7iaT9+i145oLwnin8JrfsLG41wl26+5cNQ2XV3zcbrnFEV6esjOceom9YO1w9mGJByw=="],

    "@swc/core-win32-x64-msvc": ["@swc/core-win32-x64-msvc@1.15.11", "", { "os": "win32", "cpu": "x64" }, "sha512-IQ2n6af7XKLL6P1gIeZACskSxK8jWtoKpJWLZmdXTDj1MGzktUy4i+FvpdtxFmJWNavRWH1VmTr6kAubRDHeKw=="],

    "@swc/counter": ["@swc/counter@0.1.3", "", {}, "sha512-e2BR4lsJkkRlKZ/qCHPw9ZaSxc0MVUd7gtbtaB7aMvHeJVYe8sOB8DBZkP2DtISHGSku9sCK6T6cnY0CtXrOCQ=="],

    "@swc/helpers": ["@swc/helpers@0.5.18", "", { "dependencies": { "tslib": "^2.8.0" } }, "sha512-TXTnIcNJQEKwThMMqBXsZ4VGAza6bvN4pa41Rkqoio6QBKMvo+5lexeTMScGCIxtzgQJzElcvIltani+adC5PQ=="],

    "@swc/types": ["@swc/types@0.1.25", "", { "dependencies": { "@swc/counter": "^0.1.3" } }, "sha512-iAoY/qRhNH8a/hBvm3zKj9qQ4oc2+3w1unPJa2XvTK3XjeLXtzcCingVPw/9e5mn1+0yPqxcBGp9Jf0pkfMb1g=="],

    "@types/estree": ["@types/estree@1.0.8", "", {}, "sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w=="],

    "@types/resolve": ["@types/resolve@1.20.2", "", {}, "sha512-60BCwRFOZCQhDncwQdxxeOEEkbc5dIMccYLwbxsS4TUNeVECQ/pBJ0j09mrHOl/JJvpRPGwO9SvE4nR2Nb/a4Q=="],

    "ansi-regex": ["ansi-regex@5.0.1", "", {}, "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ=="],

    "ansi-styles": ["ansi-styles@4.3.0", "", { "dependencies": { "color-convert": "^2.0.1" } }, "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg=="],

    "bunchee": ["bunchee@6.9.4", "", { "dependencies": { "@rollup/plugin-commonjs": "^29.0.0", "@rollup/plugin-json": "^6.1.0", "@rollup/plugin-node-resolve": "^16.0.1", "@rollup/plugin-replace": "^6.0.2", "@rollup/plugin-wasm": "^6.2.2", "@rollup/pluginutils": "^5.1.4", "@swc/core": "^1.13.3", "@swc/helpers": "^0.5.17", "clean-css": "^5.3.3", "magic-string": "^0.30.17", "nanospinner": "^1.2.2", "picomatch": "^4.0.2", "pretty-bytes": "^5.6.0", "rollup": "^4.52.4", "rollup-plugin-dts": "^6.3.0", "rollup-plugin-swc3": "^0.11.1", "rollup-preserve-directives": "^1.1.3", "tinyglobby": "^0.2.14", "tslib": "^2.8.1", "yargs": "^17.7.2" }, "peerDependencies": { "typescript": "^4.1 || ^5.0" }, "optionalPeers": ["typescript"], "bin": { "bunchee": "dist/bin/cli.js" } }, "sha512-bwK6R+fVYbJp49elqL+L0ZYhEuaKraALVjuZLxb+eXcT1oCjPyQVBzYYG50o4fhzqdKyDSCk1mrJUvBSvlUULg=="],

    "clean-css": ["clean-css@5.3.3", "", { "dependencies": { "source-map": "~0.6.0" } }, "sha512-D5J+kHaVb/wKSFcyyV75uCn8fiY4sV38XJoe4CUyGQ+mOU/fMVYUdH1hJC+CJQ5uY3EnW27SbJYS4X8BiLrAFg=="],

    "cliui": ["cliui@8.0.1", "", { "dependencies": { "string-width": "^4.2.0", "strip-ansi": "^6.0.1", "wrap-ansi": "^7.0.0" } }, "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ=="],

    "color-convert": ["color-convert@2.0.1", "", { "dependencies": { "color-name": "~1.1.4" } }, "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ=="],

    "color-name": ["color-name@1.1.4", "", {}, "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA=="],

    "commondir": ["commondir@1.0.1", "", {}, "sha512-W9pAhw0ja1Edb5GVdIF1mjZw/ASI0AlShXM83UUGe2DVr5TdAPEA1OA8m/g8zWp9x6On7gqufY+FatDbC3MDQg=="],

    "deepmerge": ["deepmerge@4.3.1", "", {}, "sha512-3sUqbMEc77XqpdNO7FRyRog+eW3ph+GYCbj+rK+uYyRMuwsVy0rMiVtPn+QJlKFvWP/1PYpapqYn0Me2knFn+A=="],

    "emoji-regex": ["emoji-regex@8.0.0", "", {}, "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A=="],

    "escalade": ["escalade@3.2.0", "", {}, "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA=="],

    "estree-walker": ["estree-walker@2.0.2", "", {}, "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w=="],

    "fdir": ["fdir@6.5.0", "", { "peerDependencies": { "picomatch": "^3 || ^4" }, "optionalPeers": ["picomatch"] }, "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg=="],

    "framer-motion": ["framer-motion@12.34.0", "", { "dependencies": { "motion-dom": "^12.34.0", "motion-utils": "^12.29.2", "tslib": "^2.4.0" }, "peerDependencies": { "@emotion/is-prop-valid": "*", "react": "^18.0.0 || ^19.0.0", "react-dom": "^18.0.0 || ^19.0.0" }, "optionalPeers": ["@emotion/is-prop-valid", "react", "react-dom"] }, "sha512-+/H49owhzkzQyxtn7nZeF4kdH++I2FWrESQ184Zbcw5cEqNHYkE5yxWxcTLSj5lNx3NWdbIRy5FHqUvetD8FWg=="],

    "fsevents": ["fsevents@2.3.3", "", { "os": "darwin" }, "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw=="],

    "function-bind": ["function-bind@1.1.2", "", {}, "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA=="],

    "get-caller-file": ["get-caller-file@2.0.5", "", {}, "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg=="],

    "get-tsconfig": ["get-tsconfig@4.13.6", "", { "dependencies": { "resolve-pkg-maps": "^1.0.0" } }, "sha512-shZT/QMiSHc/YBLxxOkMtgSid5HFoauqCE3/exfsEcwg1WkeqjG+V40yBbBrsD+jW2HDXcs28xOfcbm2jI8Ddw=="],

    "hasown": ["hasown@2.0.2", "", { "dependencies": { "function-bind": "^1.1.2" } }, "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ=="],

    "is-core-module": ["is-core-module@2.16.1", "", { "dependencies": { "hasown": "^2.0.2" } }, "sha512-UfoeMA6fIJ8wTYFEUjelnaGI67v6+N7qXJEvQuIGa99l4xsCruSYOVSQ0uPANn4dAzm8lkYPaKLrrijLq7x23w=="],

    "is-fullwidth-code-point": ["is-fullwidth-code-point@3.0.0", "", {}, "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg=="],

    "is-module": ["is-module@1.0.0", "", {}, "sha512-51ypPSPCoTEIN9dy5Oy+h4pShgJmPCygKfyRCISBI+JoWT/2oJvK8QPxmwv7b/p239jXrm9M1mlQbyKJ5A152g=="],

    "is-reference": ["is-reference@1.2.1", "", { "dependencies": { "@types/estree": "*" } }, "sha512-U82MsXXiFIrjCK4otLT+o2NA2Cd2g5MLoOVXUZjIOhLurrRxpEXzI8O0KZHr3IjLvlAH1kTPYSuqer5T9ZVBKQ=="],

    "js-tokens": ["js-tokens@4.0.0", "", {}, "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ=="],

    "magic-string": ["magic-string@0.30.21", "", { "dependencies": { "@jridgewell/sourcemap-codec": "^1.5.5" } }, "sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ=="],

    "motion": ["motion@12.34.0", "", { "dependencies": { "framer-motion": "^12.34.0", "tslib": "^2.4.0" }, "peerDependencies": { "@emotion/is-prop-valid": "*", "react": "^18.0.0 || ^19.0.0", "react-dom": "^18.0.0 || ^19.0.0" }, "optionalPeers": ["@emotion/is-prop-valid", "react", "react-dom"] }, "sha512-01Sfa/zgsD/di8zA/uFW5Eb7/SPXoGyUfy+uMRMW5Spa8j0z/UbfQewAYvPMYFCXRlyD6e5aLHh76TxeeJD+RA=="],

    "motion-dom": ["motion-dom@12.34.0", "", { "dependencies": { "motion-utils": "^12.29.2" } }, "sha512-Lql3NuEcScRDxTAO6GgUsRHBZOWI/3fnMlkMcH5NftzcN37zJta+bpbMAV9px4Nj057TuvRooMK7QrzMCgtz6Q=="],

    "motion-utils": ["motion-utils@12.29.2", "", {}, "sha512-G3kc34H2cX2gI63RqU+cZq+zWRRPSsNIOjpdl9TN4AQwC4sgwYPl/Q/Obf/d53nOm569T0fYK+tcoSV50BWx8A=="],

    "nanospinner": ["nanospinner@1.2.2", "", { "dependencies": { "picocolors": "^1.1.1" } }, "sha512-Zt/AmG6qRU3e+WnzGGLuMCEAO/dAu45stNbHY223tUxldaDAeE+FxSPsd9Q+j+paejmm0ZbrNVs5Sraqy3dRxA=="],

    "path-parse": ["path-parse@1.0.7", "", {}, "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw=="],

    "picocolors": ["picocolors@1.1.1", "", {}, "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA=="],

    "picomatch": ["picomatch@4.0.3", "", {}, "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q=="],

    "pretty-bytes": ["pretty-bytes@5.6.0", "", {}, "sha512-FFw039TmrBqFK8ma/7OL3sDz/VytdtJr044/QUJtH0wK9lb9jLq9tJyIxUwtQJHwar2BqtiA4iCWSwo9JLkzFg=="],

    "react": ["react@19.2.4", "", {}, "sha512-9nfp2hYpCwOjAN+8TZFGhtWEwgvWHXqESH8qT89AT/lWklpLON22Lc8pEtnpsZz7VmawabSU0gCjnj8aC0euHQ=="],

    "react-dom": ["react-dom@19.2.4", "", { "dependencies": { "scheduler": "^0.27.0" }, "peerDependencies": { "react": "^19.2.4" } }, "sha512-AXJdLo8kgMbimY95O2aKQqsz2iWi9jMgKJhRBAxECE4IFxfcazB2LmzloIoibJI3C12IlY20+KFaLv+71bUJeQ=="],

    "require-directory": ["require-directory@2.1.1", "", {}, "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q=="],

    "resolve": ["resolve@1.22.11", "", { "dependencies": { "is-core-module": "^2.16.1", "path-parse": "^1.0.7", "supports-preserve-symlinks-flag": "^1.0.0" }, "bin": { "resolve": "bin/resolve" } }, "sha512-RfqAvLnMl313r7c9oclB1HhUEAezcpLjz95wFH4LVuhk9JF/r22qmVP9AMmOU4vMX7Q8pN8jwNg/CSpdFnMjTQ=="],

    "resolve-pkg-maps": ["resolve-pkg-maps@1.0.0", "", {}, "sha512-seS2Tj26TBVOC2NIc2rOe2y2ZO7efxITtLZcGSOnHHNOQ7CkiUBfw0Iw2ck6xkIhPwLhKNLS8BO+hEpngQlqzw=="],

    "rollup": ["rollup@4.57.1", "", { "dependencies": { "@types/estree": "1.0.8" }, "optionalDependencies": { "@rollup/rollup-android-arm-eabi": "4.57.1", "@rollup/rollup-android-arm64": "4.57.1", "@rollup/rollup-darwin-arm64": "4.57.1", "@rollup/rollup-darwin-x64": "4.57.1", "@rollup/rollup-freebsd-arm64": "4.57.1", "@rollup/rollup-freebsd-x64": "4.57.1", "@rollup/rollup-linux-arm-gnueabihf": "4.57.1", "@rollup/rollup-linux-arm-musleabihf": "4.57.1", "@rollup/rollup-linux-arm64-gnu": "4.57.1", "@rollup/rollup-linux-arm64-musl": "4.57.1", "@rollup/rollup-linux-loong64-gnu": "4.57.1", "@rollup/rollup-linux-loong64-musl": "4.57.1", "@rollup/rollup-linux-ppc64-gnu": "4.57.1", "@rollup/rollup-linux-ppc64-musl": "4.57.1", "@rollup/rollup-linux-riscv64-gnu": "4.57.1", "@rollup/rollup-linux-riscv64-musl": "4.57.1", "@rollup/rollup-linux-s390x-gnu": "4.57.1", "@rollup/rollup-linux-x64-gnu": "4.57.1", "@rollup/rollup-linux-x64-musl": "4.57.1", "@rollup/rollup-openbsd-x64": "4.57.1", "@rollup/rollup-openharmony-arm64": "4.57.1", "@rollup/rollup-win32-arm64-msvc": "4.57.1", "@rollup/rollup-win32-ia32-msvc": "4.57.1", "@rollup/rollup-win32-x64-gnu": "4.57.1", "@rollup/rollup-win32-x64-msvc": "4.57.1", "fsevents": "~2.3.2" }, "bin": { "rollup": "dist/bin/rollup" } }, "sha512-oQL6lgK3e2QZeQ7gcgIkS2YZPg5slw37hYufJ3edKlfQSGGm8ICoxswK15ntSzF/a8+h7ekRy7k7oWc3BQ7y8A=="],

    "rollup-plugin-dts": ["rollup-plugin-dts@6.3.0", "", { "dependencies": { "magic-string": "^0.30.21" }, "optionalDependencies": { "@babel/code-frame": "^7.27.1" }, "peerDependencies": { "rollup": "^3.29.4 || ^4", "typescript": "^4.5 || ^5.0" } }, "sha512-d0UrqxYd8KyZ6i3M2Nx7WOMy708qsV/7fTHMHxCMCBOAe3V/U7OMPu5GkX8hC+cmkHhzGnfeYongl1IgiooddA=="],

    "rollup-plugin-swc3": ["rollup-plugin-swc3@0.11.2", "", { "dependencies": { "@fastify/deepmerge": "^1.3.0", "@rollup/pluginutils": "^5.1.0", "get-tsconfig": "^4.7.3", "rollup-preserve-directives": "^1.1.1" }, "peerDependencies": { "@swc/core": ">=1.2.165", "rollup": "^2.0.0 || ^3.0.0 || ^4.0.0" } }, "sha512-o1ih9B806fV2wBSNk46T0cYfTF2eiiKmYXRpWw3K4j/Cp3tCAt10UCVsTqvUhGP58pcB3/GZcAVl5e7TCSKN6Q=="],

    "rollup-preserve-directives": ["rollup-preserve-directives@1.1.3", "", { "dependencies": { "magic-string": "^0.30.5" }, "peerDependencies": { "rollup": "^2.0.0 || ^3.0.0 || ^4.0.0" } }, "sha512-oXqxd6ZzkoQej8Qt0k+S/yvO2+S4CEVEVv2g85oL15o0cjAKTKEuo2MzyA8FcsBBXbtytBzBMFAbhvQg4YyPUQ=="],

    "scheduler": ["scheduler@0.27.0", "", {}, "sha512-eNv+WrVbKu1f3vbYJT/xtiF5syA5HPIMtf9IgY/nKg0sWqzAUEvqY/xm7OcZc/qafLx/iO9FgOmeSAp4v5ti/Q=="],

    "source-map": ["source-map@0.6.1", "", {}, "sha512-UjgapumWlbMhkBgzT7Ykc5YXUT46F0iKu8SGXq0bcwP5dz/h0Plj6enJqjz1Zbq2l5WaqYnrVbwWOWMyF3F47g=="],

    "string-width": ["string-width@4.2.3", "", { "dependencies": { "emoji-regex": "^8.0.0", "is-fullwidth-code-point": "^3.0.0", "strip-ansi": "^6.0.1" } }, "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g=="],

    "strip-ansi": ["strip-ansi@6.0.1", "", { "dependencies": { "ansi-regex": "^5.0.1" } }, "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A=="],

    "supports-preserve-symlinks-flag": ["supports-preserve-symlinks-flag@1.0.0", "", {}, "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w=="],

    "tinyglobby": ["tinyglobby@0.2.15", "", { "dependencies": { "fdir": "^6.5.0", "picomatch": "^4.0.3" } }, "sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ=="],

    "tslib": ["tslib@2.8.1", "", {}, "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w=="],

    "typescript": ["typescript@5.9.3", "", { "bin": { "tsc": "bin/tsc", "tsserver": "bin/tsserver" } }, "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw=="],

    "wrap-ansi": ["wrap-ansi@7.0.0", "", { "dependencies": { "ansi-styles": "^4.0.0", "string-width": "^4.1.0", "strip-ansi": "^6.0.0" } }, "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q=="],

    "y18n": ["y18n@5.0.8", "", {}, "sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA=="],

    "yargs": ["yargs@17.7.2", "", { "dependencies": { "cliui": "^8.0.1", "escalade": "^3.1.1", "get-caller-file": "^2.0.5", "require-directory": "^2.1.1", "string-width": "^4.2.3", "y18n": "^5.0.5", "yargs-parser": "^21.1.1" } }, "sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w=="],

    "yargs-parser": ["yargs-parser@21.1.1", "", {}, "sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw=="],
  }
}
```

## File: `package.json`
```json
{
	"name": "sileo",
	"version": "0.1.5",
	"description": "An opinionated, physics based toast notification library for react.",
	"license": "MIT",
	"repository": {
		"type": "git",
		"url": "https://github.com/hiaaryan/sileo.git"
	},
	"exports": {
		".": {
			"import": {
				"types": "./dist/index.d.mts",
				"default": "./dist/index.mjs"
			},
			"require": {
				"types": "./dist/index.d.ts",
				"default": "./dist/index.js"
			},
			"default": "./dist/index.js"
		},
		"./styles.css": "./dist/styles.css"
	},
	"main": "./dist/index.js",
	"types": "./dist/index.d.ts",
	"files": [
		"dist"
	],
	"scripts": {
		"build": "rm -rf dist && bunchee && cp src/styles.css dist/styles.css",
		"dev": "bunchee --watch"
	},
	"peerDependencies": {
		"react": ">=18",
		"react-dom": ">=18"
	},
	"devDependencies": {
		"bunchee": "^6.9.4"
	},
	"dependencies": {
		"motion": "^12.34.0"
	}
}
```

## File: `README.md`
```markdown
<div align="center">
  <h1>Sileo</h1>
  <p>An opinionated, physics-based toast component for React.</p>
  <p><a href="https://sileo.aaryan.design">Try Out</a> &nbsp; / &nbsp; <a href="https://sileo.aaryan.design/docs">Docs</a></p>
  <video src="https://github.com/user-attachments/assets/a292d310-9189-490a-9f9d-d0a1d09defce"></video>
</div>

### Installation

```bash
npm i sileo
```

### Getting Started

```tsx
import { sileo, Toaster } from "sileo";

export default function App() {
  return (
    <>
      <Toaster position="top-right" />
      <YourApp />
    </>
  );
}
```

For detailed docs, click here: https://sileo.aaryan.design
```

## File: `tsconfig.json`
```json
{
	"compilerOptions": {
		"target": "ES2017",
		"lib": ["dom", "dom.iterable", "esnext"],
		"strict": true,
		"esModuleInterop": true,
		"module": "esnext",
		"moduleResolution": "bundler",
		"jsx": "react-jsx",
		"declaration": true,
		"declarationMap": true,
		"sourceMap": true,
		"outDir": "dist",
		"skipLibCheck": true,
		"isolatedModules": true
	},
	"include": ["src"],
	"exclude": ["node_modules", "dist"]
}
```

## File: `src/constants.ts`
```typescript
/* --------------------------------- Layout --------------------------------- */

export const HEIGHT = 40;
export const WIDTH = 350;
export const DEFAULT_ROUNDNESS = 16;

/* --------------------------------- Timing --------------------------------- */

export const DURATION_MS = 600;
export const DURATION_S = DURATION_MS / 1000;

export const DEFAULT_TOAST_DURATION = 6000;
export const EXIT_DURATION = DEFAULT_TOAST_DURATION * 0.1;
export const AUTO_EXPAND_DELAY = DEFAULT_TOAST_DURATION * 0.025;
export const AUTO_COLLAPSE_DELAY = DEFAULT_TOAST_DURATION - 2000;

export const SPRING = {
	type: "spring" as const,
	bounce: 0.25,
	duration: DURATION_S,
};

/* --------------------------------- Render --------------------------------- */

export const BLUR_RATIO = 0.5;
export const PILL_PADDING = 10;
export const MIN_EXPAND_RATIO = 2.25;
export const SWAP_COLLAPSE_MS = 200;
export const HEADER_EXIT_MS = DURATION_MS * 0.7;
```

## File: `src/icons.tsx`
```tsx
import type { ReactNode, SVGProps } from "react";

const Icon = ({
	title,
	children,
	...props
}: SVGProps<SVGSVGElement> & { title: string; children: ReactNode }) => (
	<svg
		{...props}
		xmlns="http://www.w3.org/2000/svg"
		width="16"
		height="16"
		viewBox="0 0 24 24"
		fill="none"
		stroke="currentColor"
		strokeWidth="2"
		strokeLinecap="round"
		strokeLinejoin="round"
	>
		<title>{title}</title>
		{children}
	</svg>
);

export const ArrowRight = () => (
	<Icon title="Arrow Right">
		<path d="M5 12h14" />
		<path d="m12 5 7 7-7 7" />
	</Icon>
);

export const LifeBuoy = () => (
	<Icon title="Life Buoy">
		<circle cx="12" cy="12" r="10" />
		<path d="m4.93 4.93 4.24 4.24" />
		<path d="m14.83 9.17 4.24-4.24" />
		<path d="m14.83 14.83 4.24 4.24" />
		<path d="m9.17 14.83-4.24 4.24" />
		<circle cx="12" cy="12" r="4" />
	</Icon>
);

export const LoaderCircle = (props: SVGProps<SVGSVGElement>) => (
	<Icon title="Loader Circle" {...props}>
		<path d="M21 12a9 9 0 1 1-6.219-8.56" />
	</Icon>
);

export const X = () => (
	<Icon title="X">
		<path d="M18 6 6 18" />
		<path d="m6 6 12 12" />
	</Icon>
);

export const CircleAlert = () => (
	<Icon title="Circle Alert">
		<circle cx="12" cy="12" r="10" />
		<line x1="12" x2="12" y1="8" y2="12" />
		<line x1="12" x2="12.01" y1="16" y2="16" />
	</Icon>
);

export const Check = () => (
	<Icon title="Check">
		<path d="M20 6 9 17l-5-5" />
	</Icon>
);
```

## File: `src/index.ts`
```typescript
"use client";

import "./styles.css";

export { sileo, Toaster } from "./toast";
export type {
	SileoButton,
	SileoOptions,
	SileoPosition,
	SileoState,
	SileoStyles,
} from "./types";
```

## File: `src/sileo.tsx`
```tsx
import { motion } from "motion/react";
import {
	type CSSProperties,
	type MouseEventHandler,
	memo,
	type ReactNode,
	type TransitionEventHandler,
	useCallback,
	useEffect,
	useLayoutEffect,
	useMemo,
	useRef,
	useState,
} from "react";
import {
	BLUR_RATIO,
	DEFAULT_ROUNDNESS,
	HEADER_EXIT_MS,
	HEIGHT,
	MIN_EXPAND_RATIO,
	PILL_PADDING,
	SPRING,
	SWAP_COLLAPSE_MS,
	WIDTH,
} from "./constants";
import {
	ArrowRight,
	Check,
	CircleAlert,
	LifeBuoy,
	LoaderCircle,
	X,
} from "./icons";
import "./styles.css";
import type { SileoButton, SileoState, SileoStyles } from "./types";

type State = SileoState;

interface View {
	title?: string;
	description?: ReactNode | string;
	state: State;
	icon?: ReactNode | null;
	styles?: SileoStyles;
	button?: SileoButton;
	fill: string;
}

interface SileoProps {
	id: string;
	fill?: string;
	state?: State;
	title?: string;
	description?: ReactNode | string;
	position?: "left" | "center" | "right";
	expand?: "top" | "bottom";
	className?: string;
	icon?: ReactNode | null;
	styles?: SileoStyles;
	button?: SileoButton;
	roundness?: number;
	exiting?: boolean;
	autoExpandDelayMs?: number;
	autoCollapseDelayMs?: number;
	canExpand?: boolean;
	interruptKey?: string;
	refreshKey?: string;
	onMouseEnter?: MouseEventHandler<HTMLButtonElement>;
	onMouseLeave?: MouseEventHandler<HTMLButtonElement>;
	onDismiss?: () => void;
}

/* ---------------------------------- Icons --------------------------------- */

const STATE_ICON: Record<State, ReactNode> = {
	success: <Check />,
	loading: <LoaderCircle data-sileo-icon="spin" aria-hidden="true" />,
	error: <X />,
	warning: <CircleAlert />,
	info: <LifeBuoy />,
	action: <ArrowRight />,
};

/* ----------------------------- Memoised Defs ------------------------------ */
const GooeyDefs = memo(function GooeyDefs({
	filterId,
	blur,
}: {
	filterId: string;
	blur: number;
}) {
	return (
		<defs>
			<filter
				id={filterId}
				x="-20%"
				y="-20%"
				width="140%"
				height="140%"
				colorInterpolationFilters="sRGB"
			>
				<feGaussianBlur in="SourceGraphic" stdDeviation={blur} result="blur" />
				<feColorMatrix
					in="blur"
					mode="matrix"
					values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -10"
					result="goo"
				/>
				<feComposite in="SourceGraphic" in2="goo" operator="atop" />
			</filter>
		</defs>
	);
});

/* ------------------------------- Component -------------------------------- */

export const Sileo = memo(function Sileo({
	id,
	fill = "#FFFFFF",
	state = "success",
	title = state,
	description,
	position = "left",
	expand = "bottom",
	className,
	icon,
	styles,
	button,
	roundness,
	exiting = false,
	autoExpandDelayMs,
	autoCollapseDelayMs,
	canExpand,
	interruptKey,
	refreshKey,
	onMouseEnter,
	onMouseLeave,
	onDismiss,
}: SileoProps) {
	const next: View = useMemo(
		() => ({ title, description, state, icon, styles, button, fill }),
		[title, description, state, icon, styles, button, fill],
	);

	const [view, setView] = useState<View>(next);
	const [applied, setApplied] = useState(refreshKey);
	const [isExpanded, setIsExpanded] = useState(false);
	const [ready, setReady] = useState(false);
	const [pillWidth, setPillWidth] = useState(0);
	const [contentHeight, setContentHeight] = useState(0);
	const hasDesc = Boolean(view.description) || Boolean(view.button);
	const isLoading = view.state === "loading";
	const open = hasDesc && isExpanded && !isLoading;
	const allowExpand = isLoading
		? false
		: (canExpand ?? (!interruptKey || interruptKey === id));

	const headerKey = `${view.state}-${view.title}`;
	const filterId = `sileo-gooey-${id}`;
	const resolvedRoundness = Math.max(0, roundness ?? DEFAULT_ROUNDNESS);
	const blur = resolvedRoundness * BLUR_RATIO;

	const headerRef = useRef<HTMLDivElement>(null);
	const contentRef = useRef<HTMLDivElement>(null);
	const headerExitRef = useRef<number | null>(null);
	const autoExpandRef = useRef<number | null>(null);
	const autoCollapseRef = useRef<number | null>(null);
	const swapTimerRef = useRef<number | null>(null);
	const lastRefreshKeyRef = useRef(refreshKey);
	const pendingRef = useRef<{ key?: string; payload: View } | null>(null);
	const [headerLayer, setHeaderLayer] = useState<{
		current: { key: string; view: View };
		prev: { key: string; view: View } | null;
	}>({ current: { key: headerKey, view }, prev: null });

	/* ------------------------------ Measurements ------------------------------ */

	const innerRef = useRef<HTMLDivElement>(null);

	const headerPadRef = useRef<number | null>(null);

	const pillRoRef = useRef<ResizeObserver | null>(null);
	const pillRafRef = useRef(0);
	const pillObservedRef = useRef<Element | null>(null);

	// biome-ignore lint/correctness/useExhaustiveDependencies: headerLayer.current.key is used to force a re-render
	useLayoutEffect(() => {
		const el = innerRef.current;
		const header = headerRef.current;
		if (!el || !header) return;
		if (headerPadRef.current === null) {
			const cs = getComputedStyle(header);
			headerPadRef.current =
				parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight);
		}
		const px = headerPadRef.current;
		const measure = () => {
			const w = el.scrollWidth + px + PILL_PADDING;
			if (w > PILL_PADDING) {
				setPillWidth((prev) => (prev === w ? prev : w));
			}
		};
		measure();

		if (!pillRoRef.current) {
			pillRoRef.current = new ResizeObserver(() => {
				cancelAnimationFrame(pillRafRef.current);
				pillRafRef.current = requestAnimationFrame(() => {
					const inner = innerRef.current;
					const pad = headerPadRef.current ?? 0;
					if (!inner) return;
					const w = inner.scrollWidth + pad + PILL_PADDING;
					if (w > PILL_PADDING) {
						setPillWidth((prev) => (prev === w ? prev : w));
					}
				});
			});
		}

		if (pillObservedRef.current !== el) {
			if (pillObservedRef.current) {
				pillRoRef.current.unobserve(pillObservedRef.current);
			}
			pillRoRef.current.observe(el);
			pillObservedRef.current = el;
		}
	}, [headerLayer.current.key]);

	useEffect(() => {
		return () => {
			cancelAnimationFrame(pillRafRef.current);
			pillRoRef.current?.disconnect();
		};
	}, []);

	useLayoutEffect(() => {
		if (!hasDesc) {
			setContentHeight(0);
			return;
		}
		const el = contentRef.current;
		if (!el) return;
		const measure = () => {
			const h = el.scrollHeight;
			setContentHeight((prev) => (prev === h ? prev : h));
		};
		measure();
		let rafId = 0;
		const ro = new ResizeObserver(() => {
			cancelAnimationFrame(rafId);
			rafId = requestAnimationFrame(measure);
		});
		ro.observe(el);
		return () => {
			cancelAnimationFrame(rafId);
			ro.disconnect();
		};
	}, [hasDesc]);

	useEffect(() => {
		const raf = requestAnimationFrame(() => setReady(true));
		return () => cancelAnimationFrame(raf);
	}, []);

	useLayoutEffect(() => {
		setHeaderLayer((state) => {
			if (state.current.key === headerKey) {
				if (state.current.view === view) return state;
				return { ...state, current: { key: headerKey, view } };
			}
			return {
				prev: state.current,
				current: { key: headerKey, view },
			};
		});
	}, [headerKey, view]);

	useEffect(() => {
		if (!headerLayer.prev) return;
		if (headerExitRef.current) {
			clearTimeout(headerExitRef.current);
		}
		headerExitRef.current = window.setTimeout(() => {
			headerExitRef.current = null;
			setHeaderLayer((state) => ({ ...state, prev: null }));
		}, HEADER_EXIT_MS);
		return () => {
			if (headerExitRef.current) {
				clearTimeout(headerExitRef.current);
				headerExitRef.current = null;
			}
		};
	}, [headerLayer.prev]);

	/* ----------------------------- Sync fill ---------------------------------- */

	useEffect(() => {
		setView((prev) => (prev.fill === fill ? prev : { ...prev, fill }));
	}, [fill]);

	/* ----------------------------- Refresh logic ------------------------------ */

	useEffect(() => {
		if (refreshKey === undefined) {
			setView(next);
			setApplied(undefined);
			pendingRef.current = null;
			lastRefreshKeyRef.current = refreshKey;
			return;
		}

		if (lastRefreshKeyRef.current === refreshKey) return;
		lastRefreshKeyRef.current = refreshKey;

		if (swapTimerRef.current) {
			clearTimeout(swapTimerRef.current);
			swapTimerRef.current = null;
		}

		if (open) {
			pendingRef.current = { key: refreshKey, payload: next };
			setIsExpanded(false);
			swapTimerRef.current = window.setTimeout(() => {
				swapTimerRef.current = null;
				const pending = pendingRef.current;
				if (!pending) return;
				setView(pending.payload);
				setApplied(pending.key);
				pendingRef.current = null;
			}, SWAP_COLLAPSE_MS);
		} else {
			pendingRef.current = null;
			setView(next);
			setApplied(refreshKey);
		}
	}, [open, refreshKey, next]);

	/* ----------------------------- Auto expand/collapse ----------------------- */

	// biome-ignore lint/correctness/useExhaustiveDependencies: applied is used to force a re-render
	useEffect(() => {
		if (!hasDesc) return;

		if (autoExpandRef.current) clearTimeout(autoExpandRef.current);
		if (autoCollapseRef.current) clearTimeout(autoCollapseRef.current);

		if (exiting || !allowExpand) {
			setIsExpanded(false);
			return;
		}

		if (autoExpandDelayMs == null && autoCollapseDelayMs == null) return;

		const expandDelay = autoExpandDelayMs ?? 0;
		const collapseDelay = autoCollapseDelayMs ?? 0;

		if (expandDelay > 0) {
			autoExpandRef.current = window.setTimeout(
				() => setIsExpanded(true),
				expandDelay,
			);
		} else {
			setIsExpanded(true);
		}

		if (collapseDelay > 0) {
			autoCollapseRef.current = window.setTimeout(
				() => setIsExpanded(false),
				collapseDelay,
			);
		}

		return () => {
			if (autoExpandRef.current) clearTimeout(autoExpandRef.current);
			if (autoCollapseRef.current) clearTimeout(autoCollapseRef.current);
		};
	}, [
		autoCollapseDelayMs,
		autoExpandDelayMs,
		hasDesc,
		allowExpand,
		exiting,
		applied,
	]);

	/* ------------------------------ Derived values ---------------------------- */

	const minExpanded = HEIGHT * MIN_EXPAND_RATIO;
	const rawExpanded = hasDesc
		? Math.max(minExpanded, HEIGHT + contentHeight)
		: minExpanded;

	const frozenExpandedRef = useRef(rawExpanded);
	if (open) {
		frozenExpandedRef.current = rawExpanded;
	}

	const expanded = open ? rawExpanded : frozenExpandedRef.current;
	const svgHeight = hasDesc ? Math.max(expanded, minExpanded) : HEIGHT;
	const expandedContent = Math.max(0, expanded - HEIGHT);
	const resolvedPillWidth = Math.max(pillWidth || HEIGHT, HEIGHT);
	const pillHeight = HEIGHT + blur * 3;

	const pillX =
		position === "right"
			? WIDTH - resolvedPillWidth
			: position === "center"
				? (WIDTH - resolvedPillWidth) / 2
				: 0;

	/* ------------------------------- Memoised animate targets ----------------- */

	const pillAnimate = useMemo(
		() => ({
			x: pillX,
			width: resolvedPillWidth,
			height: open ? pillHeight : HEIGHT,
		}),
		[pillX, resolvedPillWidth, open, pillHeight],
	);

	const bodyAnimate = useMemo(
		() => ({
			height: open ? expandedContent : 0,
			opacity: open ? 1 : 0,
		}),
		[open, expandedContent],
	);

	const bodyTransition = useMemo(
		() => (open ? SPRING : { ...SPRING, bounce: 0 }),
		[open],
	);

	const pillTransition = useMemo(
		() => (ready ? SPRING : { duration: 0 }),
		[ready],
	);

	const viewBox = `0 0 ${WIDTH} ${svgHeight}`;

	const canvasStyle = useMemo<CSSProperties>(
		() => ({ filter: `url(#${filterId})` }),
		[filterId],
	);

	/* ------------------------------- Inline styles ---------------------------- */

	const rootStyle = useMemo<CSSProperties & Record<string, string>>(
		() => ({
			"--_h": `${open ? expanded : HEIGHT}px`,
			"--_pw": `${resolvedPillWidth}px`,
			"--_px": `${pillX}px`,
			"--_ht": `translateY(${open ? (expand === "bottom" ? 3 : -3) : 0}px) scale(${open ? 0.9 : 1})`,
			"--_co": `${open ? 1 : 0}`,
		}),
		[open, expanded, resolvedPillWidth, pillX, expand],
	);

	/* -------------------------------- Handlers -------------------------------- */

	const handleEnter: MouseEventHandler<HTMLButtonElement> = useCallback(
		(e) => {
			onMouseEnter?.(e);
			if (hasDesc) setIsExpanded(true);
		},
		[hasDesc, onMouseEnter],
	);

	const handleLeave: MouseEventHandler<HTMLButtonElement> = useCallback(
		(e) => {
			onMouseLeave?.(e);
			setIsExpanded(false);
		},
		[onMouseLeave],
	);

	const handleTransitionEnd: TransitionEventHandler<HTMLButtonElement> =
		useCallback(
			(e) => {
				if (e.propertyName !== "height" && e.propertyName !== "transform")
					return;
				if (open) return;
				const pending = pendingRef.current;
				if (!pending) return;
				if (swapTimerRef.current) {
					clearTimeout(swapTimerRef.current);
					swapTimerRef.current = null;
				}
				setView(pending.payload);
				setApplied(pending.key);
				pendingRef.current = null;
			},
			[open],
		);

	/* -------------------------------- Swipe ----------------------------------- */

	const SWIPE_DISMISS = 30;
	const SWIPE_MAX = 20;
	const buttonRef = useRef<HTMLButtonElement>(null);
	const pointerStartRef = useRef<number | null>(null);
	const onDismissRef = useRef(onDismiss);
	onDismissRef.current = onDismiss;

	const swipeHandlersRef = useRef<{
		onMove: (e: PointerEvent) => void;
		onUp: (e: PointerEvent) => void;
	} | null>(null);

	if (!swipeHandlersRef.current) {
		const handlers = {
			onMove: (e: PointerEvent) => {
				const el = buttonRef.current;
				if (pointerStartRef.current === null || !el) return;
				const dy = e.clientY - pointerStartRef.current;
				const sign = dy > 0 ? 1 : -1;
				const clamped = Math.min(Math.abs(dy), SWIPE_MAX) * sign;
				el.style.transform = `translateY(${clamped}px)`;
			},
			onUp: (e: PointerEvent) => {
				const el = buttonRef.current;
				if (pointerStartRef.current === null || !el) return;
				const dy = e.clientY - pointerStartRef.current;
				pointerStartRef.current = null;
				el.style.transform = "";
				el.removeEventListener("pointermove", handlers.onMove);
				el.removeEventListener("pointerup", handlers.onUp);
				if (Math.abs(dy) > SWIPE_DISMISS) {
					onDismissRef.current?.();
				}
			},
		};
		swipeHandlersRef.current = handlers;
	}

	const handleButtonClick = useCallback(
		(e: React.MouseEvent) => {
			e.preventDefault();
			e.stopPropagation();
			view.button?.onClick();
		},
		[view.button],
	);

	const handlePointerDown = useCallback(
		(e: React.PointerEvent<HTMLButtonElement>) => {
			if (exiting || !onDismiss) return;
			const target = e.target as HTMLElement;
			if (target.closest("[data-sileo-button]")) return;
			pointerStartRef.current = e.clientY;
			e.currentTarget.setPointerCapture(e.pointerId);
			const el = buttonRef.current;
			const h = swipeHandlersRef.current;
			if (el && h) {
				el.addEventListener("pointermove", h.onMove, { passive: true });
				el.addEventListener("pointerup", h.onUp, { passive: true });
			}
		},
		[exiting, onDismiss],
	);

	/* --------------------------------- Render --------------------------------- */

	return (
		<button
			ref={buttonRef}
			type="button"
			data-sileo-toast
			data-ready={ready}
			data-expanded={open}
			data-exiting={exiting}
			data-edge={expand}
			data-position={position}
			data-state={view.state}
			className={className}
			style={rootStyle}
			onMouseEnter={handleEnter}
			onMouseLeave={handleLeave}
			onTransitionEnd={handleTransitionEnd}
			onPointerDown={handlePointerDown}
		>
			<div data-sileo-canvas data-edge={expand} style={canvasStyle}>
				<svg data-sileo-svg width={WIDTH} height={svgHeight} viewBox={viewBox}>
					<title>Sileo Notification</title>
					<GooeyDefs filterId={filterId} blur={blur} />
					<motion.rect
						data-sileo-pill
						rx={resolvedRoundness}
						ry={resolvedRoundness}
						fill={view.fill}
						initial={false}
						animate={pillAnimate}
						transition={pillTransition}
					/>
					<motion.rect
						data-sileo-body
						y={HEIGHT}
						width={WIDTH}
						rx={resolvedRoundness}
						ry={resolvedRoundness}
						fill={view.fill}
						initial={false}
						animate={bodyAnimate}
						transition={bodyTransition}
					/>
				</svg>
			</div>

			<div ref={headerRef} data-sileo-header data-edge={expand}>
				<div data-sileo-header-stack>
					<div
						ref={innerRef}
						key={headerLayer.current.key}
						data-sileo-header-inner
						data-layer="current"
					>
						<div
							data-sileo-badge
							data-state={headerLayer.current.view.state}
							className={headerLayer.current.view.styles?.badge}
						>
							{headerLayer.current.view.icon ??
								STATE_ICON[headerLayer.current.view.state]}
						</div>
						<span
							data-sileo-title
							data-state={headerLayer.current.view.state}
							className={headerLayer.current.view.styles?.title}
						>
							{headerLayer.current.view.title}
						</span>
					</div>
					{headerLayer.prev && (
						<div
							key={headerLayer.prev.key}
							data-sileo-header-inner
							data-layer="prev"
							data-exiting="true"
						>
							<div
								data-sileo-badge
								data-state={headerLayer.prev.view.state}
								className={headerLayer.prev.view.styles?.badge}
							>
								{headerLayer.prev.view.icon ??
									STATE_ICON[headerLayer.prev.view.state]}
							</div>
							<span
								data-sileo-title
								data-state={headerLayer.prev.view.state}
								className={headerLayer.prev.view.styles?.title}
							>
								{headerLayer.prev.view.title}
							</span>
						</div>
					)}
				</div>
			</div>

			{hasDesc && (
				<div data-sileo-content data-edge={expand} data-visible={open}>
					<div
						ref={contentRef}
						data-sileo-description
						className={view.styles?.description}
					>
						{view.description}
						{view.button && (
							// biome-ignore lint/a11y/useValidAnchor: cannot use button inside a button
							<a
								href="#"
								type="button"
								data-sileo-button
								data-state={view.state}
								className={view.styles?.button}
								onClick={handleButtonClick}
							>
								{view.button.title}
							</a>
						)}
					</div>
				</div>
			)}
		</button>
	);
});
```

## File: `src/styles.css`
```css
/* -------------------------------- Variables ------------------------------- */

:root {
	--sileo-spring-easing: linear(
		0,
		0.002 0.6%,
		0.007 1.2%,
		0.015 1.8%,
		0.026 2.4%,
		0.041 3.1%,
		0.06 3.8%,
		0.108 5.3%,
		0.157 6.6%,
		0.214 8%,
		0.467 13.7%,
		0.577 16.3%,
		0.631 17.7%,
		0.682 19.1%,
		0.73 20.5%,
		0.771 21.8%,
		0.808 23.1%,
		0.844 24.5%,
		0.874 25.8%,
		0.903 27.2%,
		0.928 28.6%,
		0.952 30.1%,
		0.972 31.6%,
		0.988 33.1%,
		1.01 35.7%,
		1.025 38.5%,
		1.034 41.6%,
		1.038 45%,
		1.035 50.1%,
		1.012 64.2%,
		1.003 73%,
		0.999 83.7%,
		1
	);

	--sileo-duration: 600ms;
	--sileo-height: 40px;
	--sileo-width: 350px;

	--sileo-state-success: oklch(0.723 0.219 142.136);
	--sileo-state-loading: oklch(0.556 0 0);
	--sileo-state-error: oklch(0.637 0.237 25.331);
	--sileo-state-warning: oklch(0.795 0.184 86.047);
	--sileo-state-info: oklch(0.685 0.169 237.323);
	--sileo-state-action: oklch(0.623 0.214 259.815);
}

/* ---------------------------------- Toast --------------------------------- */

[data-sileo-toast] {
	position: relative;
	cursor: pointer;
	pointer-events: auto;
	touch-action: none;
	border: 0;
	background: transparent;
	padding: 0;
	width: var(--sileo-width);
	height: var(--_h, var(--sileo-height));
	opacity: 0;
	transform: translateZ(0) scale(0.95);
	transform-origin: center;
	contain: layout style;
	overflow: visible;
}

[data-sileo-toast][data-state="loading"] {
	cursor: default;
}

[data-sileo-toast][data-ready="true"] {
	opacity: 1;
	transform: translateZ(0) scale(1);
	transition:
		transform calc(var(--sileo-duration) * 0.66) var(--sileo-spring-easing),
		opacity calc(var(--sileo-duration) * 0.66) var(--sileo-spring-easing),
		margin-bottom calc(var(--sileo-duration) * 0.66) var(--sileo-spring-easing),
		margin-top calc(var(--sileo-duration) * 0.66) var(--sileo-spring-easing),
		height var(--sileo-duration) var(--sileo-spring-easing);
}

/* Entry animation direction */
[data-sileo-viewport][data-position^="top"]
	[data-sileo-toast]:not([data-ready="true"]) {
	transform: translateY(-6px) scale(0.95);
}

[data-sileo-viewport][data-position^="bottom"]
	[data-sileo-toast]:not([data-ready="true"]) {
	transform: translateY(6px) scale(0.95);
}

/* Exit */
[data-sileo-toast][data-ready="true"][data-exiting="true"] {
	opacity: 0;
	pointer-events: none;
}

[data-sileo-viewport][data-position^="top"]
	[data-sileo-toast][data-ready="true"][data-exiting="true"] {
	transform: translateY(-6px) scale(0.95);
}

[data-sileo-viewport][data-position^="bottom"]
	[data-sileo-toast][data-ready="true"][data-exiting="true"] {
	transform: translateY(6px) scale(0.95);
}

/* ------------------------------- SVG Canvas ------------------------------- */

[data-sileo-canvas] {
	position: absolute;
	left: 0;
	right: 0;
	pointer-events: none;
	transform: translateZ(0);
	contain: layout style;
	overflow: visible;
}

[data-sileo-canvas][data-edge="top"] {
	bottom: 0;
	transform: scaleY(-1) translateZ(0);
}

[data-sileo-canvas][data-edge="bottom"] {
	top: 0;
}

[data-sileo-svg] {
	overflow: visible;
}

/* --------------------------------- Shapes --------------------------------- */

/* --------------------------------- Header --------------------------------- */

[data-sileo-header] {
	position: absolute;
	z-index: 20;
	display: flex;
	align-items: center;
	padding: 0.5rem;
	height: var(--sileo-height);
	overflow: hidden;
	left: var(--_px, 0px);
	transform: var(--_ht);
	max-width: var(--_pw);
}

[data-sileo-toast][data-ready="true"] [data-sileo-header] {
	transition:
		transform var(--sileo-duration) var(--sileo-spring-easing),
		left var(--sileo-duration) var(--sileo-spring-easing),
		max-width var(--sileo-duration) var(--sileo-spring-easing);
}

[data-sileo-header][data-edge="top"] {
	bottom: 0;
}

[data-sileo-header][data-edge="bottom"] {
	top: 0;
}

/* Header inner morphing */
[data-sileo-header-stack] {
	position: relative;
	display: inline-flex;
	align-items: center;
	height: 100%;
}

[data-sileo-header-inner] {
	display: flex;
	align-items: center;
	gap: 0.5rem;
	white-space: nowrap;
	opacity: 1;
	filter: blur(0px);
	transform: translateZ(0);
}

[data-sileo-header-inner][data-layer="current"] {
	position: relative;
	z-index: 1;
	animation: sileo-header-enter var(--sileo-duration) var(--sileo-spring-easing)
		both;
}

[data-sileo-header-inner][data-layer="current"]:not(:only-child),
[data-sileo-header-inner][data-exiting="true"] {
	will-change: opacity, filter;
}

[data-sileo-header-inner][data-layer="prev"] {
	position: absolute;
	left: 0;
	top: 0;
	z-index: 0;
	pointer-events: none;
}

[data-sileo-header-inner][data-exiting="true"] {
	animation: sileo-header-exit calc(var(--sileo-duration) * 0.7) ease forwards;
}

/* ---------------------------------- Badge --------------------------------- */

[data-sileo-badge] {
	display: flex;
	height: 24px;
	width: 24px;
	flex-shrink: 0;
	align-items: center;
	justify-content: center;
	padding: 2px;
	box-sizing: border-box;
	border-radius: 9999px;
	color: var(--sileo-tone, currentColor);
	background-color: var(--sileo-tone-bg, transparent);
}

/* ---------------------------------- Title --------------------------------- */

[data-sileo-title] {
	font-size: 0.825rem;
	line-height: 1rem;
	font-weight: 500;
	text-transform: capitalize;
	color: var(--sileo-tone, currentColor);
}

/* ------------------------------ State Colors ------------------------------ */

:is([data-sileo-badge], [data-sileo-title], [data-sileo-button])[data-state] {
	--_c: var(--sileo-state-success);
}

:is(
		[data-sileo-badge],
		[data-sileo-title],
		[data-sileo-button]
	)[data-state="loading"] {
	--_c: var(--sileo-state-loading);
}

:is(
		[data-sileo-badge],
		[data-sileo-title],
		[data-sileo-button]
	)[data-state="error"] {
	--_c: var(--sileo-state-error);
}

:is(
		[data-sileo-badge],
		[data-sileo-title],
		[data-sileo-button]
	)[data-state="warning"] {
	--_c: var(--sileo-state-warning);
}

:is(
		[data-sileo-badge],
		[data-sileo-title],
		[data-sileo-button]
	)[data-state="info"] {
	--_c: var(--sileo-state-info);
}

:is(
		[data-sileo-badge],
		[data-sileo-title],
		[data-sileo-button]
	)[data-state="action"] {
	--_c: var(--sileo-state-action);
}

:is([data-sileo-badge], [data-sileo-title])[data-state] {
	--sileo-tone: var(--_c);
	--sileo-tone-bg: color-mix(in oklch, var(--_c) 20%, transparent);
}

/* --------------------------------- Content -------------------------------- */

[data-sileo-content] {
	position: absolute;
	left: 0;
	z-index: 10;
	width: 100%;
	pointer-events: none;
	opacity: var(--_co, 0);
}

[data-sileo-content]:not([data-visible="true"]) {
	content-visibility: hidden;
}

[data-sileo-toast][data-ready="true"] [data-sileo-content] {
	transition: opacity calc(var(--sileo-duration) * 0.08) ease
		calc(var(--sileo-duration) * 0.04);
}

[data-sileo-content][data-edge="top"] {
	top: 0;
}

[data-sileo-content][data-edge="bottom"] {
	top: var(--sileo-height);
}

[data-sileo-content][data-visible="true"] {
	pointer-events: auto;
}

[data-sileo-toast][data-ready="true"]
	[data-sileo-content][data-visible="true"] {
	transition: opacity calc(var(--sileo-duration) * 0.6) ease
		calc(var(--sileo-duration) * 0.3);
}

[data-sileo-description] {
	width: 100%;
	text-align: left;
	padding: 1rem;
	font-size: 0.875rem;
	line-height: 1.25rem;
	contain: layout style paint;
	content-visibility: auto;
}

/* --------------------------------- Button --------------------------------- */

[data-sileo-button] {
	display: flex;
	align-items: center;
	justify-content: center;
	height: 1.75rem;
	padding: 0 0.625rem;
	margin-top: 0.75rem;
	border-radius: 9999px;
	border: 0;
	font-size: 0.75rem;
	font-weight: 500;
	cursor: pointer;
	color: var(--sileo-btn-color, currentColor);
	background-color: var(--sileo-btn-bg, transparent);
	transition: background-color 150ms ease;
}

[data-sileo-button]:hover {
	background-color: var(--sileo-btn-bg-hover, transparent);
}

[data-sileo-button][data-state] {
	--sileo-btn-color: var(--_c);
	--sileo-btn-bg: color-mix(in oklch, var(--_c) 15%, transparent);
	--sileo-btn-bg-hover: color-mix(in oklch, var(--_c) 25%, transparent);
}

/* -------------------------------- Animations ------------------------------ */

[data-sileo-icon="spin"] {
	animation: sileo-spin 1s linear infinite;
}

@keyframes sileo-spin {
	to {
		transform: rotate(360deg);
	}
}

@keyframes sileo-header-enter {
	from {
		opacity: 0;
		filter: blur(6px);
	}
	to {
		opacity: 1;
		filter: blur(0px);
	}
}

@keyframes sileo-header-exit {
	from {
		opacity: 1;
		filter: blur(0px);
	}
	to {
		opacity: 0;
		filter: blur(6px);
	}
}

/* -------------------------------- Viewports ------------------------------- */

[data-sileo-viewport] {
	position: fixed;
	z-index: 50;
	display: flex;
	gap: 0.75rem;
	padding: 0.75rem;
	pointer-events: none;
	max-width: calc(100vw - 1.5rem);
	contain: layout style;
}

[data-sileo-viewport][data-position^="top"]
	[data-sileo-toast]:not([data-ready="true"]) {
	margin-bottom: calc(-1 * (var(--sileo-height) + 0.75rem));
}

[data-sileo-viewport][data-position^="bottom"]
	[data-sileo-toast]:not([data-ready="true"]) {
	margin-top: calc(-1 * (var(--sileo-height) + 0.75rem));
}

/* Vertical edge */
[data-sileo-viewport][data-position^="top"] {
	top: 0;
	flex-direction: column-reverse;
}

[data-sileo-viewport][data-position^="bottom"] {
	bottom: 0;
	flex-direction: column;
}

/* Horizontal alignment */
[data-sileo-viewport][data-position$="left"] {
	left: 0;
	align-items: flex-start;
}

[data-sileo-viewport][data-position$="right"] {
	right: 0;
	align-items: flex-end;
}

[data-sileo-viewport][data-position$="center"] {
	left: 50%;
	transform: translateX(-50%);
	align-items: center;
}

@media (prefers-reduced-motion: no-preference) {
	[data-sileo-toast][data-ready="true"]:hover,
	[data-sileo-toast][data-ready="true"][data-exiting="true"] {
		will-change: transform, opacity, height;
	}
}

@media (prefers-reduced-motion: reduce) {
	[data-sileo-viewport],
	[data-sileo-viewport] *,
	[data-sileo-viewport] *::before,
	[data-sileo-viewport] *::after {
		animation-duration: 0.01ms;
		animation-iteration-count: 1;
		transition-duration: 0.01ms;
	}
}

/* --------------------------------- Themes -------------------------------- */

[data-sileo-viewport][data-theme="dark"] [data-sileo-description] {
	color: rgba(0, 0, 0, 0.5);
}

[data-sileo-viewport][data-theme="light"] [data-sileo-description] {
	color: rgba(255, 255, 255, 0.5);
}
```

## File: `src/toast.tsx`
```tsx
import {
	type CSSProperties,
	type MouseEventHandler,
	type ReactNode,
	useCallback,
	useEffect,
	useMemo,
	useRef,
	useState,
} from "react";
import {
	AUTO_COLLAPSE_DELAY,
	AUTO_EXPAND_DELAY,
	DEFAULT_TOAST_DURATION,
	EXIT_DURATION,
} from "./constants";
import { Sileo } from "./sileo";
import type { SileoOptions, SileoPosition, SileoState } from "./types";

const pillAlign = (pos: SileoPosition) =>
	pos.includes("right") ? "right" : pos.includes("center") ? "center" : "left";
const expandDir = (pos: SileoPosition) =>
	pos.startsWith("top") ? ("bottom" as const) : ("top" as const);

/* ---------------------------------- Types --------------------------------- */

interface InternalSileoOptions extends SileoOptions {
	id?: string;
	state?: SileoState;
}

interface SileoItem extends InternalSileoOptions {
	id: string;
	instanceId: string;
	exiting?: boolean;
	autoExpandDelayMs?: number;
	autoCollapseDelayMs?: number;
}

type SileoOffsetValue = number | string;
type SileoOffsetConfig = Partial<
	Record<"top" | "right" | "bottom" | "left", SileoOffsetValue>
>;

export interface SileoToasterProps {
	children?: ReactNode;
	position?: SileoPosition;
	offset?: SileoOffsetValue | SileoOffsetConfig;
	options?: Partial<SileoOptions>;
	theme?: "light" | "dark" | "system";
}

/* ------------------------------ Global State ------------------------------ */

type SileoListener = (toasts: SileoItem[]) => void;

const store = {
	toasts: [] as SileoItem[],
	listeners: new Set<SileoListener>(),
	position: "top-right" as SileoPosition,
	options: undefined as Partial<SileoOptions> | undefined,

	emit() {
		for (const fn of this.listeners) fn(this.toasts);
	},

	update(fn: (prev: SileoItem[]) => SileoItem[]) {
		this.toasts = fn(this.toasts);
		this.emit();
	},
};

let idCounter = 0;
const generateId = () =>
	`${++idCounter}-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;

const timeoutKey = (t: SileoItem) => `${t.id}:${t.instanceId}`;

/* ------------------------------- Toast API -------------------------------- */

const dismissToast = (id: string) => {
	const item = store.toasts.find((t) => t.id === id);
	if (!item || item.exiting) return;

	store.update((prev) =>
		prev.map((t) => (t.id === id ? { ...t, exiting: true } : t)),
	);

	setTimeout(
		() => store.update((prev) => prev.filter((t) => t.id !== id)),
		EXIT_DURATION,
	);
};

const resolveAutopilot = (
	opts: InternalSileoOptions,
	duration: number | null,
): { expandDelayMs?: number; collapseDelayMs?: number } => {
	if (opts.autopilot === false || !duration || duration <= 0) return {};
	const cfg = typeof opts.autopilot === "object" ? opts.autopilot : undefined;
	const clamp = (v: number) => Math.min(duration, Math.max(0, v));
	return {
		expandDelayMs: clamp(cfg?.expand ?? AUTO_EXPAND_DELAY),
		collapseDelayMs: clamp(cfg?.collapse ?? AUTO_COLLAPSE_DELAY),
	};
};

const mergeOptions = (options: InternalSileoOptions) => ({
	...store.options,
	...options,
	styles: { ...store.options?.styles, ...options.styles },
});

const buildSileoItem = (
	merged: InternalSileoOptions,
	id: string,
	fallbackPosition?: SileoPosition,
): SileoItem => {
	const duration = merged.duration ?? DEFAULT_TOAST_DURATION;
	const auto = resolveAutopilot(merged, duration);
	return {
		...merged,
		id,
		instanceId: generateId(),
		position: merged.position ?? fallbackPosition ?? store.position,
		autoExpandDelayMs: auto.expandDelayMs,
		autoCollapseDelayMs: auto.collapseDelayMs,
	};
};

const createToast = (options: InternalSileoOptions) => {
	const live = store.toasts.filter((t) => !t.exiting);
	const merged = mergeOptions(options);

	const id = merged.id ?? "sileo-default";
	const prev = live.find((t) => t.id === id);
	const item = buildSileoItem(merged, id, prev?.position);

	if (prev) {
		store.update((p) => p.map((t) => (t.id === id ? item : t)));
	} else {
		store.update((p) => [...p.filter((t) => t.id !== id), item]);
	}
	return { id, duration: merged.duration ?? DEFAULT_TOAST_DURATION };
};

const updateToast = (id: string, options: InternalSileoOptions) => {
	const existing = store.toasts.find((t) => t.id === id);
	if (!existing) return;

	const item = buildSileoItem(mergeOptions(options), id, existing.position);
	store.update((prev) => prev.map((t) => (t.id === id ? item : t)));
};

export interface SileoPromiseOptions<T = unknown> {
	loading: SileoOptions;
	success: SileoOptions | ((data: T) => SileoOptions);
	error: SileoOptions | ((err: unknown) => SileoOptions);
	action?: SileoOptions | ((data: T) => SileoOptions);
	position?: SileoPosition;
}

export const sileo = {
	show: (opts: SileoOptions) => createToast({ ...opts, state: opts.type }).id,
	success: (opts: SileoOptions) =>
		createToast({ ...opts, state: "success" }).id,
	error: (opts: SileoOptions) => createToast({ ...opts, state: "error" }).id,
	warning: (opts: SileoOptions) =>
		createToast({ ...opts, state: "warning" }).id,
	info: (opts: SileoOptions) => createToast({ ...opts, state: "info" }).id,
	action: (opts: SileoOptions) => createToast({ ...opts, state: "action" }).id,

	promise: <T,>(
		promise: Promise<T> | (() => Promise<T>),
		opts: SileoPromiseOptions<T>,
	): Promise<T> => {
		const { id } = createToast({
			...opts.loading,
			state: "loading",
			duration: null,
			position: opts.position,
		});

		const p = typeof promise === "function" ? promise() : promise;

		p.then((data) => {
			if (opts.action) {
				const actionOpts =
					typeof opts.action === "function" ? opts.action(data) : opts.action;
				updateToast(id, { ...actionOpts, state: "action", id });
			} else {
				const successOpts =
					typeof opts.success === "function"
						? opts.success(data)
						: opts.success;
				updateToast(id, { ...successOpts, state: "success", id });
			}
		}).catch((err) => {
			const errorOpts =
				typeof opts.error === "function" ? opts.error(err) : opts.error;
			updateToast(id, { ...errorOpts, state: "error", id });
		});

		return p;
	},

	dismiss: dismissToast,

	clear: (position?: SileoPosition) =>
		store.update((prev) =>
			position ? prev.filter((t) => t.position !== position) : [],
		),
};

/* ------------------------------ Toaster Component ------------------------- */

const THEME_FILLS = {
	light: "#1a1a1a",
	dark: "#f2f2f2",
} as const;

function useResolvedTheme(
	theme: "light" | "dark" | "system" | undefined,
): "light" | "dark" {
	const [resolved, setResolved] = useState<"light" | "dark">(() => {
		if (theme === "light" || theme === "dark") return theme;
		if (typeof window === "undefined") return "light";
		return window.matchMedia("(prefers-color-scheme: dark)").matches
			? "dark"
			: "light";
	});

	useEffect(() => {
		if (theme === "light" || theme === "dark") {
			setResolved(theme);
			return;
		}
		const mq = window.matchMedia("(prefers-color-scheme: dark)");
		const handler = (e: MediaQueryListEvent) =>
			setResolved(e.matches ? "dark" : "light");
		setResolved(mq.matches ? "dark" : "light");
		mq.addEventListener("change", handler);
		return () => mq.removeEventListener("change", handler);
	}, [theme]);

	return resolved;
}

export function Toaster({
	children,
	position = "top-right",
	offset,
	options,
	theme,
}: SileoToasterProps) {
	const resolvedTheme = useResolvedTheme(theme);
	const [toasts, setToasts] = useState<SileoItem[]>(store.toasts);
	const [activeId, setActiveId] = useState<string>();

	const hoverRef = useRef(false);
	const timersRef = useRef(new Map<string, number>());
	const listRef = useRef(toasts);
	const latestRef = useRef<string | undefined>(undefined);
	const handlersCache = useRef(
		new Map<
			string,
			{
				enter: MouseEventHandler<HTMLButtonElement>;
				leave: MouseEventHandler<HTMLButtonElement>;
				dismiss: () => void;
			}
		>(),
	);

	useEffect(() => {
		store.position = position;
		store.options = options;
	}, [position, options]);

	const clearAllTimers = useCallback(() => {
		for (const t of timersRef.current.values()) clearTimeout(t);
		timersRef.current.clear();
	}, []);

	const schedule = useCallback((items: SileoItem[]) => {
		if (hoverRef.current) return;

		for (const item of items) {
			if (item.exiting) continue;
			const key = timeoutKey(item);
			if (timersRef.current.has(key)) continue;

			if (item.duration === null) continue;
			const dur = item.duration ?? DEFAULT_TOAST_DURATION;
			if (dur <= 0) continue;

			timersRef.current.set(
				key,
				window.setTimeout(() => dismissToast(item.id), dur),
			);
		}
	}, []);

	useEffect(() => {
		const listener: SileoListener = (next) => setToasts(next);
		store.listeners.add(listener);
		return () => {
			store.listeners.delete(listener);
			clearAllTimers();
		};
	}, [clearAllTimers]);

	useEffect(() => {
		listRef.current = toasts;

		const toastKeys = new Set(toasts.map(timeoutKey));
		const toastIds = new Set(toasts.map((t) => t.id));
		for (const [key, timer] of timersRef.current) {
			if (!toastKeys.has(key)) {
				clearTimeout(timer);
				timersRef.current.delete(key);
			}
		}
		for (const id of handlersCache.current.keys()) {
			if (!toastIds.has(id)) handlersCache.current.delete(id);
		}

		schedule(toasts);
	}, [toasts, schedule]);

	const handleMouseEnterRef =
		useRef<MouseEventHandler<HTMLButtonElement>>(null);
	const handleMouseLeaveRef =
		useRef<MouseEventHandler<HTMLButtonElement>>(null);

	handleMouseEnterRef.current = useCallback<
		MouseEventHandler<HTMLButtonElement>
	>(() => {
		if (hoverRef.current) return;
		hoverRef.current = true;
		clearAllTimers();
	}, [clearAllTimers]);

	handleMouseLeaveRef.current = useCallback<
		MouseEventHandler<HTMLButtonElement>
	>(() => {
		if (!hoverRef.current) return;
		hoverRef.current = false;
		schedule(listRef.current);
	}, [schedule]);

	const latest = useMemo(() => {
		for (let i = toasts.length - 1; i >= 0; i--) {
			if (!toasts[i].exiting) return toasts[i].id;
		}
		return undefined;
	}, [toasts]);

	useEffect(() => {
		latestRef.current = latest;
		setActiveId(latest);
	}, [latest]);

	const getHandlers = useCallback((toastId: string) => {
		let cached = handlersCache.current.get(toastId);
		if (cached) return cached;

		cached = {
			enter: ((e) => {
				setActiveId((prev) => (prev === toastId ? prev : toastId));
				handleMouseEnterRef.current?.(e);
			}) as MouseEventHandler<HTMLButtonElement>,
			leave: ((e) => {
				setActiveId((prev) =>
					prev === latestRef.current ? prev : latestRef.current,
				);
				handleMouseLeaveRef.current?.(e);
			}) as MouseEventHandler<HTMLButtonElement>,
			dismiss: () => dismissToast(toastId),
		};

		handlersCache.current.set(toastId, cached);
		return cached;
	}, []);

	const getViewportStyle = useCallback(
		(pos: SileoPosition): CSSProperties | undefined => {
			if (offset === undefined) return undefined;

			const o =
				typeof offset === "object"
					? offset
					: { top: offset, right: offset, bottom: offset, left: offset };

			const s: CSSProperties = {};
			const px = (v: SileoOffsetValue) =>
				typeof v === "number" ? `${v}px` : v;

			if (pos.startsWith("top") && o.top) s.top = px(o.top);
			if (pos.startsWith("bottom") && o.bottom) s.bottom = px(o.bottom);
			if (pos.endsWith("left") && o.left) s.left = px(o.left);
			if (pos.endsWith("right") && o.right) s.right = px(o.right);

			return s;
		},
		[offset],
	);

	const activePositions = useMemo(() => {
		const map = new Map<SileoPosition, SileoItem[]>();
		for (const t of toasts) {
			const pos = t.position ?? position;
			const arr = map.get(pos);
			if (arr) {
				arr.push(t);
			} else {
				map.set(pos, [t]);
			}
		}
		return map;
	}, [toasts, position]);

	return (
		<>
			{children}
			{Array.from(activePositions, ([pos, items]) => {
				const pill = pillAlign(pos);
				const expand = expandDir(pos);

				return (
					<section
						key={pos}
						data-sileo-viewport
						data-position={pos}
						data-theme={theme ? resolvedTheme : undefined}
						aria-live="polite"
						style={getViewportStyle(pos)}
					>
						{items.map((item) => {
							const h = getHandlers(item.id);
							return (
								<Sileo
									key={item.id}
									id={item.id}
									state={item.state}
									title={item.title}
									description={item.description}
									position={pill}
									expand={expand}
									icon={item.icon}
									fill={item.fill ?? (theme ? THEME_FILLS[resolvedTheme] : undefined)}
									styles={item.styles}
									button={item.button}
									roundness={item.roundness}
									exiting={item.exiting}
									autoExpandDelayMs={item.autoExpandDelayMs}
									autoCollapseDelayMs={item.autoCollapseDelayMs}
									refreshKey={item.instanceId}
									canExpand={activeId === undefined || activeId === item.id}
									onMouseEnter={h.enter}
									onMouseLeave={h.leave}
									onDismiss={h.dismiss}
								/>
							);
						})}
					</section>
				);
			})}
		</>
	);
}
```

## File: `src/types.ts`
```typescript
import type { ReactNode } from "react";

export type SileoState =
	| "success"
	| "loading"
	| "error"
	| "warning"
	| "info"
	| "action";

export interface SileoStyles {
	title?: string;
	description?: string;
	badge?: string;
	button?: string;
}

export interface SileoButton {
	title: string;
	onClick: () => void;
}

export const SILEO_POSITIONS = [
	"top-left",
	"top-center",
	"top-right",
	"bottom-left",
	"bottom-center",
	"bottom-right",
] as const;

export type SileoPosition = (typeof SILEO_POSITIONS)[number];

export interface SileoOptions {
	title?: string;
	description?: ReactNode | string;
	type?: SileoState;
	position?: SileoPosition;
	duration?: number | null;
	icon?: ReactNode | null;
	styles?: SileoStyles;
	fill?: string;
	roundness?: number;
	autopilot?: boolean | { expand?: number; collapse?: number };
	button?: SileoButton;
}
```

