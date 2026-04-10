# Knowledge Dump for AtQ-Experiment

## File: firebase.json
```
{
  "hosting": {
    "site": "threeplabs",
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}

```

## File: index.html
```
<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>@Q</title>
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Google+Sans+Code:ital,wght@0,300..800;1,300..800&display=swap"
    rel="stylesheet">
</head>

<body>
  <div id="root"></div>
  <script type="module" src="/src/main.tsx"></script>
</body>

</html>
```

## File: package-lock.json
```
{
  "name": "vite-project",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "vite-project",
      "version": "0.0.0",
      "dependencies": {
        "@google/genai": "^1.24.0",
        "@radix-ui/themes": "^3.2.1",
        "@xyflow/react": "^12.8.6",
        "classnames": "^2.5.1",
        "esbuild-wasm": "^0.25.11",
        "firebase": "^12.4.0",
        "html-to-image": "^1.11.13",
        "lucide-react": "^0.545.0",
        "nanoid": "^5.1.6",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "zod": "^4.1.12"
      },
      "devDependencies": {
        "@paper-design/shaders-react": "^0.0.71",
        "@types/react": "^18.2.15",
        "@types/react-dom": "^18.2.7",
        "@vitejs/plugin-react": "^4.0.3",
        "sass": "^1.93.2",
        "typescript": "^5.0.2",
        "vite": "^4.4.5",
        "vite-plugin-node-polyfills": "^0.24.0",
        "vite-tsconfig-paths": "^5.1.4"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.27.1.tgz",
      "integrity": "sha512-cjQ7ZlQ0Mv3b47hABuTevyTuYN4i+loJKGeV9flcCgIK37cCXRh+L1bd3iBHlynerhQ7BhCkn2BPbQUL+rGqFg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.27.1",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.28.4.tgz",
      "integrity": "sha512-YsmSKC29MJwf0gF8Rjjrg5LQCmyh+j/nD8/eP7f+BeoQTKYqs9RoWbjGOdy0+1Ekr68RJZMUOPVQaQisnIo4Rw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.28.4.tgz",
      "integrity": "sha512-2BCOP7TN8M+gVDj7/ht3hsaO/B/n5oDbiAyyvnRlNOs+u1o+JWNYTQrmpuNp1/Wq2gcFrI01JAW+paEKDMx/CA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.3",
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-module-transforms": "^7.28.3",
        "@babel/helpers": "^7.28.4",
        "@babel/parser": "^7.28.4",
        "@babel/template": "^7.27.2",
        "@babel/traverse": "^7.28.4",
        "@babel/types": "^7.28.4",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.28.3.tgz",
      "integrity": "sha512-3lSpxGgvnmZznmBkCRnVREPUFJv2wrv9iAoFDvADJc0ypmdOxdUtcLeBgBJ6zE0PMeTKnxeQzyk0xTBq4Ep7zw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.3",
        "@babel/types": "^7.28.2",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.27.2",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.27.2.tgz",
      "integrity": "sha512-2+1thGUUWWjLTYTHZWK1n8Yga0ijBz1XAhUXcKy81rd5g6yh7hGqMp45v7cadSbEHc9G3OTv45SyneRN3ps4DQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.27.2",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.27.1.tgz",
      "integrity": "sha512-0gSFWUPNXNopqtIPQvlD5WgXYI5GY2kP2cCvoT8kczjbfcfuIljTbcWrulD1CIPIX2gt1wghbDy08yE1p+/r3w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.3.tgz",
      "integrity": "sha512-gytXUbs8k2sXS9PnQptz5o0QnpLL51SwASIORY6XaBKF88nsOT0Zw9szLqlSGQDP/4TljBAD5y98p2U1fqkdsw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1",
        "@babel/traverse": "^7.28.3"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.27.1.tgz",
      "integrity": "sha512-1gn1Up5YXka3YYAHGKpbideQ5Yjf1tDa9qYcgysz+cNCXukyLl6DjPXhD3VRwSb8c0J9tA4b2+rHEZtc6R0tlw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.27.1.tgz",
      "integrity": "sha512-D2hP9eA+Sqx1kBZgzxZh0y1trbuU+JoDkiEwqhQ36nodYqJwyEIhPSdMNd7lOm/4io72luTPWH20Yda0xOuUow==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
      "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.28.4.tgz",
      "integrity": "sha512-HFN59MmQXGHVyYadKLVumYsA9dBFun/ldYxipEjzA4196jpLZd8UjEEBLkbEkvfYreDqJhZxYAWFPtrfhNpj4w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.27.2",
        "@babel/types": "^7.28.4"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.28.4.tgz",
      "integrity": "sha512-yZbBqeM6TkpP9du/I2pUZnJsRMGGvOuIrhjzC1AwHwW+6he4mni6Bp/m8ijn0iOuZuPI2BfkCoSRunpyjnrQKg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.4"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.27.1.tgz",
      "integrity": "sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.27.1.tgz",
      "integrity": "sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.27.2",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.27.2.tgz",
      "integrity": "sha512-LPDZ85aEJyYSd18/DkjNh4/y1ntkE5KwUHWTiqgRxruuZL2F1yuHligVHLvcHY2vMHXttKFpJn6LwfI7cw7ODw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/parser": "^7.27.2",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.28.4.tgz",
      "integrity": "sha512-YEzuboP2qvQavAcjgQNVgsvHIDv6ZpwXvcvjmyySP2DIMuByS/6ioU5G9pYrWHM6T2YDfc7xga9iNzYOs12CFQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.3",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.28.4",
        "@babel/template": "^7.27.2",
        "@babel/types": "^7.28.4",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.28.4.tgz",
      "integrity": "sha512-bkFqkLhh3pMBUQQkpVgWDWq/lqzc2678eUyDlTBhRqhCHFguYYGM0Efga7tYk4TogG/3x0EEl66/OQ+WGbWB/Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.18.20.tgz",
      "integrity": "sha512-fyi7TDI/ijKKNZTUJAQqiG5T7YjJXgnzkURqmGj13C6dCqckZBLdl4h7bkhHt/t0WP+zO9/zwroDvANaOqO5Sw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.18.20.tgz",
      "integrity": "sha512-Nz4rJcchGDtENV0eMKUNa6L12zz2zBDXuhj/Vjh18zGqB44Bi7MBMSXjgunJgjRhCmKOjnPuZp4Mb6OKqtMHLQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.18.20.tgz",
      "integrity": "sha512-8GDdlePJA8D6zlZYJV/jnrRAi6rOiNaCC/JclcXpB+KIuvfBN4owLtgzY2bsxnx666XjJx2kDPUmnTtR8qKQUg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.18.20.tgz",
      "integrity": "sha512-bxRHW5kHU38zS2lPTPOyuyTm+S+eobPUnTNkdJEfAddYgEcll4xkT8DB9d2008DtTbl7uJag2HuE5NZAZgnNEA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.18.20.tgz",
      "integrity": "sha512-pc5gxlMDxzm513qPGbCbDukOdsGtKhfxD1zJKXjCCcU7ju50O7MeAZ8c4krSJcOIJGFR+qx21yMMVYwiQvyTyQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.18.20.tgz",
      "integrity": "sha512-yqDQHy4QHevpMAaxhhIwYPMv1NECwOvIpGCZkECn8w2WFHXjEwrBn3CeNIYsibZ/iZEUemj++M26W3cNR5h+Tw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.18.20.tgz",
      "integrity": "sha512-tgWRPPuQsd3RmBZwarGVHZQvtzfEBOreNuxEMKFcd5DaDn2PbBxfwLcj4+aenoh7ctXcbXmOQIn8HI6mCSw5MQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.18.20.tgz",
      "integrity": "sha512-/5bHkMWnq1EgKr1V+Ybz3s1hWXok7mDFUMQ4cG10AfW3wL02PSZi5kFpYKrptDsgb2WAJIvRcDm+qIvXf/apvg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.18.20.tgz",
      "integrity": "sha512-2YbscF+UL7SQAVIpnWvYwM+3LskyDmPhe31pE7/aoTMFKKzIc9lLbyGUpmmb8a8AixOL61sQ/mFh3jEjHYFvdA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.18.20.tgz",
      "integrity": "sha512-P4etWwq6IsReT0E1KHU40bOnzMHoH73aXp96Fs8TIT6z9Hu8G6+0SHSw9i2isWrD2nbx2qo5yUqACgdfVGx7TA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.18.20.tgz",
      "integrity": "sha512-nXW8nqBTrOpDLPgPY9uV+/1DjxoQ7DoB2N8eocyq8I9XuqJ7BiAMDMf9n1xZM9TgW0J8zrquIb/A7s3BJv7rjg==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.18.20.tgz",
      "integrity": "sha512-d5NeaXZcHp8PzYy5VnXV3VSd2D328Zb+9dEq5HE6bw6+N86JVPExrA6O68OPwobntbNJ0pzCpUFZTo3w0GyetQ==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.18.20.tgz",
      "integrity": "sha512-WHPyeScRNcmANnLQkq6AfyXRFr5D6N2sKgkFo2FqguP44Nw2eyDlbTdZwd9GYk98DZG9QItIiTlFLHJHjxP3FA==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.18.20.tgz",
      "integrity": "sha512-WSxo6h5ecI5XH34KC7w5veNnKkju3zBRLEQNY7mv5mtBmrP/MjNBCAlsM2u5hDBlS3NGcTQpoBvRzqBcRtpq1A==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.18.20.tgz",
      "integrity": "sha512-+8231GMs3mAEth6Ja1iK0a1sQ3ohfcpzpRLH8uuc5/KVDFneH6jtAJLFGafpzpMRO6DzJ6AvXKze9LfFMrIHVQ==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.18.20.tgz",
      "integrity": "sha512-UYqiqemphJcNsFEskc73jQ7B9jgwjWrSayxawS6UVFZGWrAAtkzjxSqnoclCXxWtfwLdzU+vTpcNYhpn43uP1w==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.18.20.tgz",
      "integrity": "sha512-iO1c++VP6xUBUmltHZoMtCUdPlnPGdBom6IrO4gyKPFFVBKioIImVooR5I83nTew5UOYrk3gIJhbZh8X44y06A==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.18.20.tgz",
      "integrity": "sha512-e5e4YSsuQfX4cxcygw/UCPIEP6wbIL+se3sxPdCiMbFLBWu0eiZOJ7WoD+ptCLrmjZBK1Wk7I6D/I3NglUGOxg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.18.20.tgz",
      "integrity": "sha512-kDbFRFp0YpTQVVrqUd5FTYmWo45zGaXe0X8E1G/LKFC0v8x0vWrhOWSLITcCn63lmZIxfOMXtCfti/RxN/0wnQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.18.20.tgz",
      "integrity": "sha512-ddYFR6ItYgoaq4v4JmQQaAI5s7npztfV4Ag6NrhiaW0RrnOXqBkgwZLofVTlq1daVTQNhtI5oieTvkRPfZrePg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.18.20.tgz",
      "integrity": "sha512-Wv7QBi3ID/rROT08SABTS7eV4hX26sVduqDOTe1MvGMjNd3EjOz4b7zeexIR62GTIEKrfJXKL9LFxTYgkyeu7g==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.18.20.tgz",
      "integrity": "sha512-kTdfRcSiDfQca/y9QIkng02avJ+NCaQvrMejlsB3RRv5sE9rRoeBPISaZpKxHELzRxZyLvNts1P27W3wV+8geQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@firebase/ai": {
      "version": "2.4.0",
      "resolved": "https://registry.npmjs.org/@firebase/ai/-/ai-2.4.0.tgz",
      "integrity": "sha512-YilG6AJ/nYpCKtxZyvEzBRAQv5bU+2tBOKX4Ps0rNNSdxN39aT37kGhjATbk1kq1z5Lq7mkWglw/ajAF3lOWUg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app-check-interop-types": "0.3.3",
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x",
        "@firebase/app-types": "0.x"
      }
    },
    "node_modules/@firebase/analytics": {
      "version": "0.10.19",
      "resolved": "https://registry.npmjs.org/@firebase/analytics/-/analytics-0.10.19.tgz",
      "integrity": "sha512-3wU676fh60gaiVYQEEXsbGS4HbF2XsiBphyvvqDbtC1U4/dO4coshbYktcCHq+HFaGIK07iHOh4pME0hEq1fcg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/installations": "0.6.19",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/analytics-compat": {
      "version": "0.2.25",
      "resolved": "https://registry.npmjs.org/@firebase/analytics-compat/-/analytics-compat-0.2.25.tgz",
      "integrity": "sha512-fdzoaG0BEKbqksRDhmf4JoyZf16Wosrl0Y7tbZtJyVDOOwziE0vrFjmZuTdviL0yhak+Nco6rMsUUbkbD+qb6Q==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/analytics": "0.10.19",
        "@firebase/analytics-types": "0.8.3",
        "@firebase/component": "0.7.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/analytics-types": {
      "version": "0.8.3",
      "resolved": "https://registry.npmjs.org/@firebase/analytics-types/-/analytics-types-0.8.3.tgz",
      "integrity": "sha512-VrIp/d8iq2g501qO46uGz3hjbDb8xzYMrbu8Tp0ovzIzrvJZ2fvmj649gTjge/b7cCCcjT0H37g1gVtlNhnkbg==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/app": {
      "version": "0.14.4",
      "resolved": "https://registry.npmjs.org/@firebase/app/-/app-0.14.4.tgz",
      "integrity": "sha512-pUxEGmR+uu21OG/icAovjlu1fcYJzyVhhT0rsCrn+zi+nHtrS43Bp9KPn9KGa4NMspCUE++nkyiqziuIvJdwzw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "idb": "7.1.1",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@firebase/app-check": {
      "version": "0.11.0",
      "resolved": "https://registry.npmjs.org/@firebase/app-check/-/app-check-0.11.0.tgz",
      "integrity": "sha512-XAvALQayUMBJo58U/rxW02IhsesaxxfWVmVkauZvGEz3vOAjMEQnzFlyblqkc2iAaO82uJ2ZVyZv9XzPfxjJ6w==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/app-check-compat": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@firebase/app-check-compat/-/app-check-compat-0.4.0.tgz",
      "integrity": "sha512-UfK2Q8RJNjYM/8MFORltZRG9lJj11k0nW84rrffiKvcJxLf1jf6IEjCIkCamykHE73C6BwqhVfhIBs69GXQV0g==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app-check": "0.11.0",
        "@firebase/app-check-types": "0.5.3",
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/app-check-interop-types": {
      "version": "0.3.3",
      "resolved": "https://registry.npmjs.org/@firebase/app-check-interop-types/-/app-check-interop-types-0.3.3.tgz",
      "integrity": "sha512-gAlxfPLT2j8bTI/qfe3ahl2I2YcBQ8cFIBdhAQA4I2f3TndcO+22YizyGYuttLHPQEpWkhmpFW60VCFEPg4g5A==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/app-check-types": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/@firebase/app-check-types/-/app-check-types-0.5.3.tgz",
      "integrity": "sha512-hyl5rKSj0QmwPdsAxrI5x1otDlByQ7bvNvVt8G/XPO2CSwE++rmSVf3VEhaeOR4J8ZFaF0Z0NDSmLejPweZ3ng==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/app-compat": {
      "version": "0.5.4",
      "resolved": "https://registry.npmjs.org/@firebase/app-compat/-/app-compat-0.5.4.tgz",
      "integrity": "sha512-T7ifGmb+awJEcp542Ek4HtNfBxcBrnuk1ggUdqyFEdsXHdq7+wVlhvE6YukTL7NS8hIkEfL7TMAPx/uCNqt30g==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app": "0.14.4",
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@firebase/app-types": {
      "version": "0.9.3",
      "resolved": "https://registry.npmjs.org/@firebase/app-types/-/app-types-0.9.3.tgz",
      "integrity": "sha512-kRVpIl4vVGJ4baogMDINbyrIOtOxqhkZQg4jTq3l8Lw6WSk0xfpEYzezFu+Kl4ve4fbPl79dvwRtaFqAC/ucCw==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/auth-compat": {
      "version": "0.6.0",
      "resolved": "https://registry.npmjs.org/@firebase/auth-compat/-/auth-compat-0.6.0.tgz",
      "integrity": "sha512-J0lGSxXlG/lYVi45wbpPhcWiWUMXevY4fvLZsN1GHh+po7TZVng+figdHBVhFheaiipU8HZyc7ljw1jNojM2nw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/auth": "1.11.0",
        "@firebase/auth-types": "0.13.0",
        "@firebase/component": "0.7.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/auth-compat/node_modules/@firebase/auth": {
      "version": "1.11.0",
      "resolved": "https://registry.npmjs.org/@firebase/auth/-/auth-1.11.0.tgz",
      "integrity": "sha512-5j7+ua93X+IRcJ1oMDTClTo85l7Xe40WSkoJ+shzPrX7OISlVWLdE1mKC57PSD+/LfAbdhJmvKixINBw2ESK6w==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x",
        "@react-native-async-storage/async-storage": "^1.18.1"
      },
      "peerDependenciesMeta": {
        "@react-native-async-storage/async-storage": {
          "optional": true
        }
      }
    },
    "node_modules/@firebase/auth-interop-types": {
      "version": "0.2.4",
      "resolved": "https://registry.npmjs.org/@firebase/auth-interop-types/-/auth-interop-types-0.2.4.tgz",
      "integrity": "sha512-JPgcXKCuO+CWqGDnigBtvo09HeBs5u/Ktc2GaFj2m01hLarbxthLNm7Fk8iOP1aqAtXV+fnnGj7U28xmk7IwVA==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/auth-types": {
      "version": "0.13.0",
      "resolved": "https://registry.npmjs.org/@firebase/auth-types/-/auth-types-0.13.0.tgz",
      "integrity": "sha512-S/PuIjni0AQRLF+l9ck0YpsMOdE8GO2KU6ubmBB7P+7TJUCQDa3R1dlgYm9UzGbbePMZsp0xzB93f2b/CgxMOg==",
      "license": "Apache-2.0",
      "peerDependencies": {
        "@firebase/app-types": "0.x",
        "@firebase/util": "1.x"
      }
    },
    "node_modules/@firebase/component": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/@firebase/component/-/component-0.7.0.tgz",
      "integrity": "sha512-wR9En2A+WESUHexjmRHkqtaVH94WLNKt6rmeqZhSLBybg4Wyf0Umk04SZsS6sBq4102ZsDBFwoqMqJYj2IoDSg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@firebase/data-connect": {
      "version": "0.3.11",
      "resolved": "https://registry.npmjs.org/@firebase/data-connect/-/data-connect-0.3.11.tgz",
      "integrity": "sha512-G258eLzAD6im9Bsw+Qm1Z+P4x0PGNQ45yeUuuqe5M9B1rn0RJvvsQCRHXgE52Z+n9+WX1OJd/crcuunvOGc7Vw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/auth-interop-types": "0.2.4",
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/database": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@firebase/database/-/database-1.1.0.tgz",
      "integrity": "sha512-gM6MJFae3pTyNLoc9VcJNuaUDej0ctdjn3cVtILo3D5lpp0dmUHHLFN/pUKe7ImyeB1KAvRlEYxvIHNF04Filg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app-check-interop-types": "0.3.3",
        "@firebase/auth-interop-types": "0.2.4",
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "faye-websocket": "0.11.4",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@firebase/database-compat": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/@firebase/database-compat/-/database-compat-2.1.0.tgz",
      "integrity": "sha512-8nYc43RqxScsePVd1qe1xxvWNf0OBnbwHxmXJ7MHSuuTVYFO3eLyLW3PiCKJ9fHnmIz4p4LbieXwz+qtr9PZDg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/database": "1.1.0",
        "@firebase/database-types": "1.0.16",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@firebase/database-types": {
      "version": "1.0.16",
      "resolved": "https://registry.npmjs.org/@firebase/database-types/-/database-types-1.0.16.tgz",
      "integrity": "sha512-xkQLQfU5De7+SPhEGAXFBnDryUWhhlFXelEg2YeZOQMCdoe7dL64DDAd77SQsR+6uoXIZY5MB4y/inCs4GTfcw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app-types": "0.9.3",
        "@firebase/util": "1.13.0"
      }
    },
    "node_modules/@firebase/firestore": {
      "version": "4.9.2",
      "resolved": "https://registry.npmjs.org/@firebase/firestore/-/firestore-4.9.2.tgz",
      "integrity": "sha512-iuA5+nVr/IV/Thm0Luoqf2mERUvK9g791FZpUJV1ZGXO6RL2/i/WFJUj5ZTVXy5pRjpWYO+ZzPcReNrlilmztA==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "@firebase/webchannel-wrapper": "1.0.5",
        "@grpc/grpc-js": "~1.9.0",
        "@grpc/proto-loader": "^0.7.8",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/firestore-compat": {
      "version": "0.4.2",
      "resolved": "https://registry.npmjs.org/@firebase/firestore-compat/-/firestore-compat-0.4.2.tgz",
      "integrity": "sha512-cy7ov6SpFBx+PHwFdOOjbI7kH00uNKmIFurAn560WiPCZXy9EMnil1SOG7VF4hHZKdenC+AHtL4r3fNpirpm0w==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/firestore": "4.9.2",
        "@firebase/firestore-types": "3.0.3",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/firestore-types": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@firebase/firestore-types/-/firestore-types-3.0.3.tgz",
      "integrity": "sha512-hD2jGdiWRxB/eZWF89xcK9gF8wvENDJkzpVFb4aGkzfEaKxVRD1kjz1t1Wj8VZEp2LCB53Yx1zD8mrhQu87R6Q==",
      "license": "Apache-2.0",
      "peerDependencies": {
        "@firebase/app-types": "0.x",
        "@firebase/util": "1.x"
      }
    },
    "node_modules/@firebase/functions": {
      "version": "0.13.1",
      "resolved": "https://registry.npmjs.org/@firebase/functions/-/functions-0.13.1.tgz",
      "integrity": "sha512-sUeWSb0rw5T+6wuV2o9XNmh9yHxjFI9zVGFnjFi+n7drTEWpl7ZTz1nROgGrSu472r+LAaj+2YaSicD4R8wfbw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app-check-interop-types": "0.3.3",
        "@firebase/auth-interop-types": "0.2.4",
        "@firebase/component": "0.7.0",
        "@firebase/messaging-interop-types": "0.2.3",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/functions-compat": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/@firebase/functions-compat/-/functions-compat-0.4.1.tgz",
      "integrity": "sha512-AxxUBXKuPrWaVNQ8o1cG1GaCAtXT8a0eaTDfqgS5VsRYLAR0ALcfqDLwo/QyijZj1w8Qf8n3Qrfy/+Im245hOQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/functions": "0.13.1",
        "@firebase/functions-types": "0.6.3",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/functions-types": {
      "version": "0.6.3",
      "resolved": "https://registry.npmjs.org/@firebase/functions-types/-/functions-types-0.6.3.tgz",
      "integrity": "sha512-EZoDKQLUHFKNx6VLipQwrSMh01A1SaL3Wg6Hpi//x6/fJ6Ee4hrAeswK99I5Ht8roiniKHw4iO0B1Oxj5I4plg==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/installations": {
      "version": "0.6.19",
      "resolved": "https://registry.npmjs.org/@firebase/installations/-/installations-0.6.19.tgz",
      "integrity": "sha512-nGDmiwKLI1lerhwfwSHvMR9RZuIH5/8E3kgUWnVRqqL7kGVSktjLTWEMva7oh5yxQ3zXfIlIwJwMcaM5bK5j8Q==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/util": "1.13.0",
        "idb": "7.1.1",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/installations-compat": {
      "version": "0.2.19",
      "resolved": "https://registry.npmjs.org/@firebase/installations-compat/-/installations-compat-0.2.19.tgz",
      "integrity": "sha512-khfzIY3EI5LePePo7vT19/VEIH1E3iYsHknI/6ek9T8QCozAZshWT9CjlwOzZrKvTHMeNcbpo/VSOSIWDSjWdQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/installations": "0.6.19",
        "@firebase/installations-types": "0.5.3",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/installations-types": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/@firebase/installations-types/-/installations-types-0.5.3.tgz",
      "integrity": "sha512-2FJI7gkLqIE0iYsNQ1P751lO3hER+Umykel+TkLwHj6plzWVxqvfclPUZhcKFVQObqloEBTmpi2Ozn7EkCABAA==",
      "license": "Apache-2.0",
      "peerDependencies": {
        "@firebase/app-types": "0.x"
      }
    },
    "node_modules/@firebase/logger": {
      "version": "0.5.0",
      "resolved": "https://registry.npmjs.org/@firebase/logger/-/logger-0.5.0.tgz",
      "integrity": "sha512-cGskaAvkrnh42b3BA3doDWeBmuHFO/Mx5A83rbRDYakPjO9bJtRL3dX7javzc2Rr/JHZf4HlterTW2lUkfeN4g==",
      "license": "Apache-2.0",
      "dependencies": {
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@firebase/messaging": {
      "version": "0.12.23",
      "resolved": "https://registry.npmjs.org/@firebase/messaging/-/messaging-0.12.23.tgz",
      "integrity": "sha512-cfuzv47XxqW4HH/OcR5rM+AlQd1xL/VhuaeW/wzMW1LFrsFcTn0GND/hak1vkQc2th8UisBcrkVcQAnOnKwYxg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/installations": "0.6.19",
        "@firebase/messaging-interop-types": "0.2.3",
        "@firebase/util": "1.13.0",
        "idb": "7.1.1",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/messaging-compat": {
      "version": "0.2.23",
      "resolved": "https://registry.npmjs.org/@firebase/messaging-compat/-/messaging-compat-0.2.23.tgz",
      "integrity": "sha512-SN857v/kBUvlQ9X/UjAqBoQ2FEaL1ZozpnmL1ByTe57iXkmnVVFm9KqAsTfmf+OEwWI4kJJe9NObtN/w22lUgg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/messaging": "0.12.23",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/messaging-interop-types": {
      "version": "0.2.3",
      "resolved": "https://registry.npmjs.org/@firebase/messaging-interop-types/-/messaging-interop-types-0.2.3.tgz",
      "integrity": "sha512-xfzFaJpzcmtDjycpDeCUj0Ge10ATFi/VHVIvEEjDNc3hodVBQADZ7BWQU7CuFpjSHE+eLuBI13z5F/9xOoGX8Q==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/performance": {
      "version": "0.7.9",
      "resolved": "https://registry.npmjs.org/@firebase/performance/-/performance-0.7.9.tgz",
      "integrity": "sha512-UzybENl1EdM2I1sjYm74xGt/0JzRnU/0VmfMAKo2LSpHJzaj77FCLZXmYQ4oOuE+Pxtt8Wy2BVJEENiZkaZAzQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/installations": "0.6.19",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0",
        "web-vitals": "^4.2.4"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/performance-compat": {
      "version": "0.2.22",
      "resolved": "https://registry.npmjs.org/@firebase/performance-compat/-/performance-compat-0.2.22.tgz",
      "integrity": "sha512-xLKxaSAl/FVi10wDX/CHIYEUP13jXUjinL+UaNXT9ByIvxII5Ne5150mx6IgM8G6Q3V+sPiw9C8/kygkyHUVxg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/performance": "0.7.9",
        "@firebase/performance-types": "0.2.3",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/performance-types": {
      "version": "0.2.3",
      "resolved": "https://registry.npmjs.org/@firebase/performance-types/-/performance-types-0.2.3.tgz",
      "integrity": "sha512-IgkyTz6QZVPAq8GSkLYJvwSLr3LS9+V6vNPQr0x4YozZJiLF5jYixj0amDtATf1X0EtYHqoPO48a9ija8GocxQ==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/remote-config": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/@firebase/remote-config/-/remote-config-0.7.0.tgz",
      "integrity": "sha512-dX95X6WlW7QlgNd7aaGdjAIZUiQkgWgNS+aKNu4Wv92H1T8Ue/NDUjZHd9xb8fHxLXIHNZeco9/qbZzr500MjQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/installations": "0.6.19",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/remote-config-compat": {
      "version": "0.2.20",
      "resolved": "https://registry.npmjs.org/@firebase/remote-config-compat/-/remote-config-compat-0.2.20.tgz",
      "integrity": "sha512-P/ULS9vU35EL9maG7xp66uljkZgcPMQOxLj3Zx2F289baTKSInE6+YIkgHEi1TwHoddC/AFePXPpshPlEFkbgg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/remote-config": "0.7.0",
        "@firebase/remote-config-types": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/remote-config-types": {
      "version": "0.5.0",
      "resolved": "https://registry.npmjs.org/@firebase/remote-config-types/-/remote-config-types-0.5.0.tgz",
      "integrity": "sha512-vI3bqLoF14L/GchtgayMiFpZJF+Ao3uR8WCde0XpYNkSokDpAKca2DxvcfeZv7lZUqkUwQPL2wD83d3vQ4vvrg==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/storage": {
      "version": "0.14.0",
      "resolved": "https://registry.npmjs.org/@firebase/storage/-/storage-0.14.0.tgz",
      "integrity": "sha512-xWWbb15o6/pWEw8H01UQ1dC5U3rf8QTAzOChYyCpafV6Xki7KVp3Yaw2nSklUwHEziSWE9KoZJS7iYeyqWnYFA==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x"
      }
    },
    "node_modules/@firebase/storage-compat": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@firebase/storage-compat/-/storage-compat-0.4.0.tgz",
      "integrity": "sha512-vDzhgGczr1OfcOy285YAPur5pWDEvD67w4thyeCUh6Ys0izN9fNYtA1MJERmNBfqjqu0lg0FM5GLbw0Il21M+g==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/storage": "0.14.0",
        "@firebase/storage-types": "0.8.3",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app-compat": "0.x"
      }
    },
    "node_modules/@firebase/storage-types": {
      "version": "0.8.3",
      "resolved": "https://registry.npmjs.org/@firebase/storage-types/-/storage-types-0.8.3.tgz",
      "integrity": "sha512-+Muk7g9uwngTpd8xn9OdF/D48uiQ7I1Fae7ULsWPuKoCH3HU7bfFPhxtJYzyhjdniowhuDpQcfPmuNRAqZEfvg==",
      "license": "Apache-2.0",
      "peerDependencies": {
        "@firebase/app-types": "0.x",
        "@firebase/util": "1.x"
      }
    },
    "node_modules/@firebase/util": {
      "version": "1.13.0",
      "resolved": "https://registry.npmjs.org/@firebase/util/-/util-1.13.0.tgz",
      "integrity": "sha512-0AZUyYUfpMNcztR5l09izHwXkZpghLgCUaAGjtMwXnCg3bj4ml5VgiwqOMOxJ+Nw4qN/zJAaOQBcJ7KGkWStqQ==",
      "hasInstallScript": true,
      "license": "Apache-2.0",
      "dependencies": {
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@firebase/webchannel-wrapper": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/@firebase/webchannel-wrapper/-/webchannel-wrapper-1.0.5.tgz",
      "integrity": "sha512-+uGNN7rkfn41HLO0vekTFhTxk61eKa8mTpRGLO0QSqlQdKvIoGAvLp3ppdVIWbTGYJWM6Kp0iN+PjMIOcnVqTw==",
      "license": "Apache-2.0"
    },
    "node_modules/@floating-ui/core": {
      "version": "1.7.3",
      "resolved": "https://registry.npmjs.org/@floating-ui/core/-/core-1.7.3.tgz",
      "integrity": "sha512-sGnvb5dmrJaKEZ+LDIpguvdX3bDlEllmv4/ClQ9awcmCZrlx5jQyyMWFM5kBI+EyNOCDDiKk8il0zeuX3Zlg/w==",
      "license": "MIT",
      "dependencies": {
        "@floating-ui/utils": "^0.2.10"
      }
    },
    "node_modules/@floating-ui/dom": {
      "version": "1.7.4",
      "resolved": "https://registry.npmjs.org/@floating-ui/dom/-/dom-1.7.4.tgz",
      "integrity": "sha512-OOchDgh4F2CchOX94cRVqhvy7b3AFb+/rQXyswmzmGakRfkMgoWVjfnLWkRirfLEfuD4ysVW16eXzwt3jHIzKA==",
      "license": "MIT",
      "dependencies": {
        "@floating-ui/core": "^1.7.3",
        "@floating-ui/utils": "^0.2.10"
      }
    },
    "node_modules/@floating-ui/react-dom": {
      "version": "2.1.6",
      "resolved": "https://registry.npmjs.org/@floating-ui/react-dom/-/react-dom-2.1.6.tgz",
      "integrity": "sha512-4JX6rEatQEvlmgU80wZyq9RT96HZJa88q8hp0pBd+LrczeDI4o6uA2M+uvxngVHo4Ihr8uibXxH6+70zhAFrVw==",
      "license": "MIT",
      "dependencies": {
        "@floating-ui/dom": "^1.7.4"
      },
      "peerDependencies": {
        "react": ">=16.8.0",
        "react-dom": ">=16.8.0"
      }
    },
    "node_modules/@floating-ui/utils": {
      "version": "0.2.10",
      "resolved": "https://registry.npmjs.org/@floating-ui/utils/-/utils-0.2.10.tgz",
      "integrity": "sha512-aGTxbpbg8/b5JfU1HXSrbH3wXZuLPJcNEcZQFMxLs3oSzgtVu6nFPkbbGGUvBcUjKV2YyB9Wxxabo+HEH9tcRQ==",
      "license": "MIT"
    },
    "node_modules/@google/genai": {
      "version": "1.24.0",
      "resolved": "https://registry.npmjs.org/@google/genai/-/genai-1.24.0.tgz",
      "integrity": "sha512-e3jZF9Dx3dDaDCzygdMuYByHI2xJZ0PaD3r2fRgHZe2IOwBnmJ/Tu5Lt/nefTCxqr1ZnbcbQK9T13d8U/9UMWg==",
      "license": "Apache-2.0",
      "dependencies": {
        "google-auth-library": "^9.14.2",
        "ws": "^8.18.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@modelcontextprotocol/sdk": "^1.11.4"
      },
      "peerDependenciesMeta": {
        "@modelcontextprotocol/sdk": {
          "optional": true
        }
      }
    },
    "node_modules/@grpc/grpc-js": {
      "version": "1.9.15",
      "resolved": "https://registry.npmjs.org/@grpc/grpc-js/-/grpc-js-1.9.15.tgz",
      "integrity": "sha512-nqE7Hc0AzI+euzUwDAy0aY5hCp10r734gMGRdU+qOPX0XSceI2ULrcXB5U2xSc5VkWwalCj4M7GzCAygZl2KoQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@grpc/proto-loader": "^0.7.8",
        "@types/node": ">=12.12.47"
      },
      "engines": {
        "node": "^8.13.0 || >=10.10.0"
      }
    },
    "node_modules/@grpc/proto-loader": {
      "version": "0.7.15",
      "resolved": "https://registry.npmjs.org/@grpc/proto-loader/-/proto-loader-0.7.15.tgz",
      "integrity": "sha512-tMXdRCfYVixjuFK+Hk0Q1s38gV9zDiDJfWL3h1rv4Qc39oILCu1TRTDt7+fGUI8K4G1Fj125Hx/ru3azECWTyQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "lodash.camelcase": "^4.3.0",
        "long": "^5.0.0",
        "protobufjs": "^7.2.5",
        "yargs": "^17.7.2"
      },
      "bin": {
        "proto-loader-gen-types": "build/bin/proto-loader-gen-types.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/@grpc/proto-loader/node_modules/cliui": {
      "version": "8.0.1",
      "resolved": "https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz",
      "integrity": "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==",
      "license": "ISC",
      "dependencies": {
        "string-width": "^4.2.0",
        "strip-ansi": "^6.0.1",
        "wrap-ansi": "^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@grpc/proto-loader/node_modules/long": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/long/-/long-5.3.2.tgz",
      "integrity": "sha512-mNAgZ1GmyNhD7AuqnTG3/VQ26o760+ZYBPKjPvugO8+nLbYfX6TVpJPseBvopbdY+qpZ/lKUnmEc1LeZYS3QAA==",
      "license": "Apache-2.0"
    },
    "node_modules/@grpc/proto-loader/node_modules/yargs": {
      "version": "17.7.2",
      "resolved": "https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz",
      "integrity": "sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w==",
      "license": "MIT",
      "dependencies": {
        "cliui": "^8.0.1",
        "escalade": "^3.1.1",
        "get-caller-file": "^2.0.5",
        "require-directory": "^2.1.1",
        "string-width": "^4.2.3",
        "y18n": "^5.0.5",
        "yargs-parser": "^21.1.1"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@grpc/proto-loader/node_modules/yargs-parser": {
      "version": "21.1.1",
      "resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz",
      "integrity": "sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/remapping": {
      "version": "2.3.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/remapping/-/remapping-2.3.5.tgz",
      "integrity": "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@paper-design/shaders": {
      "version": "0.0.71",
      "resolved": "https://registry.npmjs.org/@paper-design/shaders/-/shaders-0.0.71.tgz",
      "integrity": "sha512-brCt05YxxyjBrhnE3l1wJJHcFXsM8aE4lmpd9TMQp+p0dMU3F+OWkJZL9m/RC1Tt7om5xr0Wg7d0HYm+b9NYZA==",
      "dev": true,
      "license": "SEE LICENSE IN https://github.com/paper-design/shaders/blob/main/LICENSE"
    },
    "node_modules/@paper-design/shaders-react": {
      "version": "0.0.71",
      "resolved": "https://registry.npmjs.org/@paper-design/shaders-react/-/shaders-react-0.0.71.tgz",
      "integrity": "sha512-kTqjIlyZcpkwqJie+3ldEDscTtx1oOi8eRBD5QgWKI21GaNn/SSg26092M5zzqr3e8dVANv0ktS2ICSjbMFKbw==",
      "dev": true,
      "license": "SEE LICENSE IN https://github.com/paper-design/shaders/blob/main/LICENSE",
      "dependencies": {
        "@paper-design/shaders": "0.0.71"
      },
      "peerDependencies": {
        "@types/react": "^18 || ^19",
        "react": "^18 || ^19"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@parcel/watcher": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher/-/watcher-2.5.1.tgz",
      "integrity": "sha512-dfUnCxiN9H4ap84DvD2ubjw+3vUNpstxa0TneY/Paat8a3R4uQZDLSvWjmznAY/DoahqTHl9V46HF/Zs3F29pg==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "detect-libc": "^1.0.3",
        "is-glob": "^4.0.3",
        "micromatch": "^4.0.5",
        "node-addon-api": "^7.0.0"
      },
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      },
      "optionalDependencies": {
        "@parcel/watcher-android-arm64": "2.5.1",
        "@parcel/watcher-darwin-arm64": "2.5.1",
        "@parcel/watcher-darwin-x64": "2.5.1",
        "@parcel/watcher-freebsd-x64": "2.5.1",
        "@parcel/watcher-linux-arm-glibc": "2.5.1",
        "@parcel/watcher-linux-arm-musl": "2.5.1",
        "@parcel/watcher-linux-arm64-glibc": "2.5.1",
        "@parcel/watcher-linux-arm64-musl": "2.5.1",
        "@parcel/watcher-linux-x64-glibc": "2.5.1",
        "@parcel/watcher-linux-x64-musl": "2.5.1",
        "@parcel/watcher-win32-arm64": "2.5.1",
        "@parcel/watcher-win32-ia32": "2.5.1",
        "@parcel/watcher-win32-x64": "2.5.1"
      }
    },
    "node_modules/@parcel/watcher-android-arm64": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-android-arm64/-/watcher-android-arm64-2.5.1.tgz",
      "integrity": "sha512-KF8+j9nNbUN8vzOFDpRMsaKBHZ/mcjEjMToVMJOhTozkDonQFFrRcfdLWn6yWKCmJKmdVxSgHiYvTCef4/qcBA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-darwin-arm64": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-darwin-arm64/-/watcher-darwin-arm64-2.5.1.tgz",
      "integrity": "sha512-eAzPv5osDmZyBhou8PoF4i6RQXAfeKL9tjb3QzYuccXFMQU0ruIc/POh30ePnaOyD1UXdlKguHBmsTs53tVoPw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-darwin-x64": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-darwin-x64/-/watcher-darwin-x64-2.5.1.tgz",
      "integrity": "sha512-1ZXDthrnNmwv10A0/3AJNZ9JGlzrF82i3gNQcWOzd7nJ8aj+ILyW1MTxVk35Db0u91oD5Nlk9MBiujMlwmeXZg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-freebsd-x64": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-freebsd-x64/-/watcher-freebsd-x64-2.5.1.tgz",
      "integrity": "sha512-SI4eljM7Flp9yPuKi8W0ird8TI/JK6CSxju3NojVI6BjHsTyK7zxA9urjVjEKJ5MBYC+bLmMcbAWlZ+rFkLpJQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-linux-arm-glibc": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-linux-arm-glibc/-/watcher-linux-arm-glibc-2.5.1.tgz",
      "integrity": "sha512-RCdZlEyTs8geyBkkcnPWvtXLY44BCeZKmGYRtSgtwwnHR4dxfHRG3gR99XdMEdQ7KeiDdasJwwvNSF5jKtDwdA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-linux-arm-musl": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-linux-arm-musl/-/watcher-linux-arm-musl-2.5.1.tgz",
      "integrity": "sha512-6E+m/Mm1t1yhB8X412stiKFG3XykmgdIOqhjWj+VL8oHkKABfu/gjFj8DvLrYVHSBNC+/u5PeNrujiSQ1zwd1Q==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-linux-arm64-glibc": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-linux-arm64-glibc/-/watcher-linux-arm64-glibc-2.5.1.tgz",
      "integrity": "sha512-LrGp+f02yU3BN9A+DGuY3v3bmnFUggAITBGriZHUREfNEzZh/GO06FF5u2kx8x+GBEUYfyTGamol4j3m9ANe8w==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-linux-arm64-musl": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-linux-arm64-musl/-/watcher-linux-arm64-musl-2.5.1.tgz",
      "integrity": "sha512-cFOjABi92pMYRXS7AcQv9/M1YuKRw8SZniCDw0ssQb/noPkRzA+HBDkwmyOJYp5wXcsTrhxO0zq1U11cK9jsFg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-linux-x64-glibc": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-linux-x64-glibc/-/watcher-linux-x64-glibc-2.5.1.tgz",
      "integrity": "sha512-GcESn8NZySmfwlTsIur+49yDqSny2IhPeZfXunQi48DMugKeZ7uy1FX83pO0X22sHntJ4Ub+9k34XQCX+oHt2A==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-linux-x64-musl": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-linux-x64-musl/-/watcher-linux-x64-musl-2.5.1.tgz",
      "integrity": "sha512-n0E2EQbatQ3bXhcH2D1XIAANAcTZkQICBPVaxMeaCVBtOpBZpWJuf7LwyWPSBDITb7In8mqQgJ7gH8CILCURXg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-win32-arm64": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-win32-arm64/-/watcher-win32-arm64-2.5.1.tgz",
      "integrity": "sha512-RFzklRvmc3PkjKjry3hLF9wD7ppR4AKcWNzH7kXR7GUe0Igb3Nz8fyPwtZCSquGrhU5HhUNDr/mKBqj7tqA2Vw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-win32-ia32": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-win32-ia32/-/watcher-win32-ia32-2.5.1.tgz",
      "integrity": "sha512-c2KkcVN+NJmuA7CGlaGD1qJh1cLfDnQsHjE89E60vUEMlqduHGCdCLJCID5geFVM0dOtA3ZiIO8BoEQmzQVfpQ==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@parcel/watcher-win32-x64": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/@parcel/watcher-win32-x64/-/watcher-win32-x64-2.5.1.tgz",
      "integrity": "sha512-9lHBdJITeNR++EvSQVUcaZoWupyHfXe1jZvGZ06O/5MflPcuPLtEphScIBL+AiCWBO46tDSHzWyD0uDmmZqsgA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 10.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/@protobufjs/aspromise": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/aspromise/-/aspromise-1.1.2.tgz",
      "integrity": "sha512-j+gKExEuLmKwvz3OgROXtrJ2UG2x8Ch2YZUxahh+s1F2HZ+wAceUNLkvy6zKCPVRkU++ZWQrdxsUeQXmcg4uoQ==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/base64": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/base64/-/base64-1.1.2.tgz",
      "integrity": "sha512-AZkcAA5vnN/v4PDqKyMR5lx7hZttPDgClv83E//FMNhR2TMcLUhfRUBHCmSl0oi9zMgDDqRUJkSxO3wm85+XLg==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/codegen": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/@protobufjs/codegen/-/codegen-2.0.4.tgz",
      "integrity": "sha512-YyFaikqM5sH0ziFZCN3xDC7zeGaB/d0IUb9CATugHWbd1FRFwWwt4ld4OYMPWu5a3Xe01mGAULCdqhMlPl29Jg==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/eventemitter": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/eventemitter/-/eventemitter-1.1.0.tgz",
      "integrity": "sha512-j9ednRT81vYJ9OfVuXG6ERSTdEL1xVsNgqpkxMsbIabzSo3goCjDIveeGv5d03om39ML71RdmrGNjG5SReBP/Q==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/fetch": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/fetch/-/fetch-1.1.0.tgz",
      "integrity": "sha512-lljVXpqXebpsijW71PZaCYeIcE5on1w5DlQy5WH6GLbFryLUrBD4932W/E2BSpfRJWseIL4v/KPgBFxDOIdKpQ==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "@protobufjs/aspromise": "^1.1.1",
        "@protobufjs/inquire": "^1.1.0"
      }
    },
    "node_modules/@protobufjs/float": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/float/-/float-1.0.2.tgz",
      "integrity": "sha512-Ddb+kVXlXst9d+R9PfTIxh1EdNkgoRe5tOX6t01f1lYWOvJnSPDBlG241QLzcyPdoNTsblLUdujGSE4RzrTZGQ==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/inquire": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/inquire/-/inquire-1.1.0.tgz",
      "integrity": "sha512-kdSefcPdruJiFMVSbn801t4vFK7KB/5gd2fYvrxhuJYg8ILrmn9SKSX2tZdV6V+ksulWqS7aXjBcRXl3wHoD9Q==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/path": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/path/-/path-1.1.2.tgz",
      "integrity": "sha512-6JOcJ5Tm08dOHAbdR3GrvP+yUUfkjG5ePsHYczMFLq3ZmMkAD98cDgcT2iA1lJ9NVwFd4tH/iSSoe44YWkltEA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/pool": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/pool/-/pool-1.1.0.tgz",
      "integrity": "sha512-0kELaGSIDBKvcgS4zkjz1PeddatrjYcmMWOlAuAPwAeccUrPHdUqo/J6LiymHHEiJT5NrF1UVwxY14f+fy4WQw==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/utf8": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/utf8/-/utf8-1.1.0.tgz",
      "integrity": "sha512-Vvn3zZrhQZkkBE8LSuW3em98c0FwgO4nxzv6OdSxPKJIEKY2bGbHn+mhGIPerzI4twdxaP8/0+06HBpwf345Lw==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@radix-ui/colors": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/@radix-ui/colors/-/colors-3.0.0.tgz",
      "integrity": "sha512-FUOsGBkHrYJwCSEtWRCIfQbZG7q1e6DgxCIOe1SUQzDe/7rXXeA47s8yCn6fuTNQAj1Zq4oTFi9Yjp3wzElcxg==",
      "license": "MIT"
    },
    "node_modules/@radix-ui/number": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/number/-/number-1.1.1.tgz",
      "integrity": "sha512-MkKCwxlXTgz6CFoJx3pCwn07GKp36+aZyu/u2Ln2VrA5DcdyCZkASEDBTd8x5whTQQL5CiYf4prXKLcgQdv29g==",
      "license": "MIT"
    },
    "node_modules/@radix-ui/primitive": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/@radix-ui/primitive/-/primitive-1.1.3.tgz",
      "integrity": "sha512-JTF99U/6XIjCBo0wqkU5sK10glYe27MRRsfwoiq5zzOEZLHU3A3KCMa5X/azekYRCJ0HlwI0crAXS/5dEHTzDg==",
      "license": "MIT"
    },
    "node_modules/@radix-ui/react-accessible-icon": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-accessible-icon/-/react-accessible-icon-1.1.7.tgz",
      "integrity": "sha512-XM+E4WXl0OqUJFovy6GjmxxFyx9opfCAIUku4dlKRd5YEPqt4kALOkQOp0Of6reHuUkJuiPBEc5k0o4z4lTC8A==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-visually-hidden": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-accordion": {
      "version": "1.2.12",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-accordion/-/react-accordion-1.2.12.tgz",
      "integrity": "sha512-T4nygeh9YE9dLRPhAHSeOZi7HBXo+0kYIPJXayZfvWOWA0+n3dESrZbjfDPUABkUNym6Hd+f2IR113To8D2GPA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collapsible": "1.1.12",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-alert-dialog": {
      "version": "1.1.15",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-alert-dialog/-/react-alert-dialog-1.1.15.tgz",
      "integrity": "sha512-oTVLkEw5GpdRe29BqJ0LSDFWI3qu0vR1M0mUkOQWDIUnY/QIkLpgDMWuKxP94c2NAC2LGcgVhG1ImF3jkZ5wXw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-dialog": "1.1.15",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-arrow": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-arrow/-/react-arrow-1.1.7.tgz",
      "integrity": "sha512-F+M1tLhO+mlQaOWspE8Wstg+z6PwxwRd8oQ8IXceWz92kfAmalTRf0EjrouQeo7QssEPfCn05B4Ihs1K9WQ/7w==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-aspect-ratio": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-aspect-ratio/-/react-aspect-ratio-1.1.7.tgz",
      "integrity": "sha512-Yq6lvO9HQyPwev1onK1daHCHqXVLzPhSVjmsNjCa2Zcxy2f7uJD2itDtxknv6FzAKCwD1qQkeVDmX/cev13n/g==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-avatar": {
      "version": "1.1.10",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-avatar/-/react-avatar-1.1.10.tgz",
      "integrity": "sha512-V8piFfWapM5OmNCXTzVQY+E1rDa53zY+MQ4Y7356v4fFz6vqCyUtIz2rUD44ZEdwg78/jKmMJHj07+C/Z/rcog==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-is-hydrated": "0.1.0",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-checkbox": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-checkbox/-/react-checkbox-1.3.3.tgz",
      "integrity": "sha512-wBbpv+NQftHDdG86Qc0pIyXk5IR3tM8Vd0nWLKDcX8nNn4nXFOFwsKuqw2okA/1D/mpaAkmuyndrPJTYDNZtFw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-previous": "1.1.1",
        "@radix-ui/react-use-size": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-collapsible": {
      "version": "1.1.12",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-collapsible/-/react-collapsible-1.1.12.tgz",
      "integrity": "sha512-Uu+mSh4agx2ib1uIGPP4/CKNULyajb3p92LsVXmH2EHVMTfZWpll88XJ0j4W0z3f8NK1eYl1+Mf/szHPmcHzyA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-collection": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-collection/-/react-collection-1.1.7.tgz",
      "integrity": "sha512-Fh9rGN0MoI4ZFUNyfFVNU4y9LUz93u9/0K+yLgA2bwRojxM8JU1DyvvMBabnZPBgMWREAJvU2jjVzq+LrFUglw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-compose-refs": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-compose-refs/-/react-compose-refs-1.1.2.tgz",
      "integrity": "sha512-z4eqJvfiNnFMHIIvXP3CY57y2WJs5g2v3X0zm9mEJkrkNv4rDxu+sg9Jh8EkXyeqBkB7SOcboo9dMVqhyrACIg==",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-context": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-context/-/react-context-1.1.2.tgz",
      "integrity": "sha512-jCi/QKUM2r1Ju5a3J64TH2A5SpKAgh0LpknyqdQ4m6DCV0xJ2HG1xARRwNGPQfi1SLdLWZ1OJz6F4OMBBNiGJA==",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-context-menu": {
      "version": "2.2.16",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-context-menu/-/react-context-menu-2.2.16.tgz",
      "integrity": "sha512-O8morBEW+HsVG28gYDZPTrT9UUovQUlJue5YO836tiTJhuIWBm/zQHc7j388sHWtdH/xUZurK9olD2+pcqx5ww==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-menu": "2.1.16",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-dialog": {
      "version": "1.1.15",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-dialog/-/react-dialog-1.1.15.tgz",
      "integrity": "sha512-TCglVRtzlffRNxRMEyR36DGBLJpeusFcgMVD9PZEzAKnUs1lKCgX5u9BmC2Yg+LL9MgZDugFFs1Vl+Jp4t/PGw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-focus-guards": "1.1.3",
        "@radix-ui/react-focus-scope": "1.1.7",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "aria-hidden": "^1.2.4",
        "react-remove-scroll": "^2.6.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-direction": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-direction/-/react-direction-1.1.1.tgz",
      "integrity": "sha512-1UEWRX6jnOA2y4H5WczZ44gOOjTEmlqv1uNW4GAJEO5+bauCBhv8snY65Iw5/VOS/ghKN9gr2KjnLKxrsvoMVw==",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-dismissable-layer": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-dismissable-layer/-/react-dismissable-layer-1.1.11.tgz",
      "integrity": "sha512-Nqcp+t5cTB8BinFkZgXiMJniQH0PsUt2k51FUhbdfeKvc4ACcG2uQniY/8+h1Yv6Kza4Q7lD7PQV0z0oicE0Mg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-escape-keydown": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-dropdown-menu": {
      "version": "2.1.16",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-dropdown-menu/-/react-dropdown-menu-2.1.16.tgz",
      "integrity": "sha512-1PLGQEynI/3OX/ftV54COn+3Sud/Mn8vALg2rWnBLnRaGtJDduNW/22XjlGgPdpcIbiQxjKtb7BkcjP00nqfJw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-menu": "2.1.16",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-focus-guards": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-focus-guards/-/react-focus-guards-1.1.3.tgz",
      "integrity": "sha512-0rFg/Rj2Q62NCm62jZw0QX7a3sz6QCQU0LpZdNrJX8byRGaGVTqbrW9jAoIAHyMQqsNpeZ81YgSizOt5WXq0Pw==",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-focus-scope": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-focus-scope/-/react-focus-scope-1.1.7.tgz",
      "integrity": "sha512-t2ODlkXBQyn7jkl6TNaw/MtVEVvIGelJDCG41Okq/KwUsJBwQ4XVZsHAVUkK4mBv3ewiAS3PGuUWuY2BoK4ZUw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-form": {
      "version": "0.1.8",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-form/-/react-form-0.1.8.tgz",
      "integrity": "sha512-QM70k4Zwjttifr5a4sZFts9fn8FzHYvQ5PiB19O2HsYibaHSVt9fH9rzB0XZo/YcM+b7t/p7lYCT/F5eOeF5yQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-label": "2.1.7",
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-hover-card": {
      "version": "1.1.15",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-hover-card/-/react-hover-card-1.1.15.tgz",
      "integrity": "sha512-qgTkjNT1CfKMoP0rcasmlH2r1DAiYicWsDsufxl940sT2wHNEWWv6FMWIQXWhVdmC1d/HYfbhQx60KYyAtKxjg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-popper": "1.2.8",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-id": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-id/-/react-id-1.1.1.tgz",
      "integrity": "sha512-kGkGegYIdQsOb4XjsfM97rXsiHaBwco+hFI66oO4s9LU+PLAC5oJ7khdOVFxkhsmlbpUqDAvXw11CluXP+jkHg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-label": {
      "version": "2.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-label/-/react-label-2.1.7.tgz",
      "integrity": "sha512-YT1GqPSL8kJn20djelMX7/cTRp/Y9w5IZHvfxQTVHrOqa2yMl7i/UfMqKRU5V7mEyKTrUVgJXhNQPVCG8PBLoQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-menu": {
      "version": "2.1.16",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-menu/-/react-menu-2.1.16.tgz",
      "integrity": "sha512-72F2T+PLlphrqLcAotYPp0uJMr5SjP5SL01wfEspJbru5Zs5vQaSHb4VB3ZMJPimgHHCHG7gMOeOB9H3Hdmtxg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-focus-guards": "1.1.3",
        "@radix-ui/react-focus-scope": "1.1.7",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-popper": "1.2.8",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-slot": "1.2.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "aria-hidden": "^1.2.4",
        "react-remove-scroll": "^2.6.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-menubar": {
      "version": "1.1.16",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-menubar/-/react-menubar-1.1.16.tgz",
      "integrity": "sha512-EB1FktTz5xRRi2Er974AUQZWg2yVBb1yjip38/lgwtCVRd3a+maUoGHN/xs9Yv8SY8QwbSEb+YrxGadVWbEutA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-menu": "2.1.16",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-navigation-menu": {
      "version": "1.2.14",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-navigation-menu/-/react-navigation-menu-1.2.14.tgz",
      "integrity": "sha512-YB9mTFQvCOAQMHU+C/jVl96WmuWeltyUEpRJJky51huhds5W2FQr1J8D/16sQlf0ozxkPK8uF3niQMdUwZPv5w==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-layout-effect": "1.1.1",
        "@radix-ui/react-use-previous": "1.1.1",
        "@radix-ui/react-visually-hidden": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-one-time-password-field": {
      "version": "0.1.8",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-one-time-password-field/-/react-one-time-password-field-0.1.8.tgz",
      "integrity": "sha512-ycS4rbwURavDPVjCb5iS3aG4lURFDILi6sKI/WITUMZ13gMmn/xGjpLoqBAalhJaDk8I3UbCM5GzKHrnzwHbvg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/number": "1.1.1",
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-effect-event": "0.0.2",
        "@radix-ui/react-use-is-hydrated": "0.1.0",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-password-toggle-field": {
      "version": "0.1.3",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-password-toggle-field/-/react-password-toggle-field-0.1.3.tgz",
      "integrity": "sha512-/UuCrDBWravcaMix4TdT+qlNdVwOM1Nck9kWx/vafXsdfj1ChfhOdfi3cy9SGBpWgTXwYCuboT/oYpJy3clqfw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-effect-event": "0.0.2",
        "@radix-ui/react-use-is-hydrated": "0.1.0"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-popover": {
      "version": "1.1.15",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-popover/-/react-popover-1.1.15.tgz",
      "integrity": "sha512-kr0X2+6Yy/vJzLYJUPCZEc8SfQcf+1COFoAqauJm74umQhta9M7lNJHP7QQS3vkvcGLQUbWpMzwrXYwrYztHKA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-focus-guards": "1.1.3",
        "@radix-ui/react-focus-scope": "1.1.7",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-popper": "1.2.8",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "aria-hidden": "^1.2.4",
        "react-remove-scroll": "^2.6.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-popper": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-popper/-/react-popper-1.2.8.tgz",
      "integrity": "sha512-0NJQ4LFFUuWkE7Oxf0htBKS6zLkkjBH+hM1uk7Ng705ReR8m/uelduy1DBo0PyBXPKVnBA6YBlU94MBGXrSBCw==",
      "license": "MIT",
      "dependencies": {
        "@floating-ui/react-dom": "^2.0.0",
        "@radix-ui/react-arrow": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-layout-effect": "1.1.1",
        "@radix-ui/react-use-rect": "1.1.1",
        "@radix-ui/react-use-size": "1.1.1",
        "@radix-ui/rect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-portal": {
      "version": "1.1.9",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-portal/-/react-portal-1.1.9.tgz",
      "integrity": "sha512-bpIxvq03if6UNwXZ+HTK71JLh4APvnXntDc6XOX8UVq4XQOVl7lwok0AvIl+b8zgCw3fSaVTZMpAPPagXbKmHQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-presence": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-presence/-/react-presence-1.1.5.tgz",
      "integrity": "sha512-/jfEwNDdQVBCNvjkGit4h6pMOzq8bHkopq458dPt2lMjx+eBQUohZNG9A7DtO/O5ukSbxuaNGXMjHicgwy6rQQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-primitive": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-primitive/-/react-primitive-2.1.3.tgz",
      "integrity": "sha512-m9gTwRkhy2lvCPe6QJp4d3G1TYEUHn/FzJUtq9MjH46an1wJU+GdoGC5VLof8RX8Ft/DlpshApkhswDLZzHIcQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-slot": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-progress": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-progress/-/react-progress-1.1.7.tgz",
      "integrity": "sha512-vPdg/tF6YC/ynuBIJlk1mm7Le0VgW6ub6J2UWnTQ7/D23KXcPI1qy+0vBkgKgd38RCMJavBXpB83HPNFMTb0Fg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-radio-group": {
      "version": "1.3.8",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-radio-group/-/react-radio-group-1.3.8.tgz",
      "integrity": "sha512-VBKYIYImA5zsxACdisNQ3BjCBfmbGH3kQlnFVqlWU4tXwjy7cGX8ta80BcrO+WJXIn5iBylEH3K6ZTlee//lgQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-previous": "1.1.1",
        "@radix-ui/react-use-size": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-roving-focus": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-roving-focus/-/react-roving-focus-1.1.11.tgz",
      "integrity": "sha512-7A6S9jSgm/S+7MdtNDSb+IU859vQqJ/QAtcYQcfFC6W8RS4IxIZDldLR0xqCFZ6DCyrQLjLPsxtTNch5jVA4lA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-scroll-area": {
      "version": "1.2.10",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-scroll-area/-/react-scroll-area-1.2.10.tgz",
      "integrity": "sha512-tAXIa1g3sM5CGpVT0uIbUx/U3Gs5N8T52IICuCtObaos1S8fzsrPXG5WObkQN3S6NVl6wKgPhAIiBGbWnvc97A==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/number": "1.1.1",
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-select": {
      "version": "2.2.6",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-select/-/react-select-2.2.6.tgz",
      "integrity": "sha512-I30RydO+bnn2PQztvo25tswPH+wFBjehVGtmagkU78yMdwTwVf12wnAOF+AeP8S2N8xD+5UPbGhkUfPyvT+mwQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/number": "1.1.1",
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-focus-guards": "1.1.3",
        "@radix-ui/react-focus-scope": "1.1.7",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-popper": "1.2.8",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-layout-effect": "1.1.1",
        "@radix-ui/react-use-previous": "1.1.1",
        "@radix-ui/react-visually-hidden": "1.2.3",
        "aria-hidden": "^1.2.4",
        "react-remove-scroll": "^2.6.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-separator": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-separator/-/react-separator-1.1.7.tgz",
      "integrity": "sha512-0HEb8R9E8A+jZjvmFCy/J4xhbXy3TV+9XSnGJ3KvTtjlIUy/YQ/p6UYZvi7YbeoeXdyU9+Y3scizK6hkY37baA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-slider": {
      "version": "1.3.6",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-slider/-/react-slider-1.3.6.tgz",
      "integrity": "sha512-JPYb1GuM1bxfjMRlNLE+BcmBC8onfCi60Blk7OBqi2MLTFdS+8401U4uFjnwkOr49BLmXxLC6JHkvAsx5OJvHw==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/number": "1.1.1",
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-layout-effect": "1.1.1",
        "@radix-ui/react-use-previous": "1.1.1",
        "@radix-ui/react-use-size": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-slot": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-slot/-/react-slot-1.2.3.tgz",
      "integrity": "sha512-aeNmHnBxbi2St0au6VBVC7JXFlhLlOnvIIlePNniyUNAClzmtAUEY8/pBiK3iHjufOlwA+c20/8jngo7xcrg8A==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-compose-refs": "1.1.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-switch": {
      "version": "1.2.6",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-switch/-/react-switch-1.2.6.tgz",
      "integrity": "sha512-bByzr1+ep1zk4VubeEVViV592vu2lHE2BZY5OnzehZqOOgogN80+mNtCqPkhn2gklJqOpxWgPoYTSnhBCqpOXQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-previous": "1.1.1",
        "@radix-ui/react-use-size": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-tabs": {
      "version": "1.1.13",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-tabs/-/react-tabs-1.1.13.tgz",
      "integrity": "sha512-7xdcatg7/U+7+Udyoj2zodtI9H/IIopqo+YOIcZOq1nJwXWBZ9p8xiu5llXlekDbZkca79a/fozEYQXIA4sW6A==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-toast": {
      "version": "1.2.15",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-toast/-/react-toast-1.2.15.tgz",
      "integrity": "sha512-3OSz3TacUWy4WtOXV38DggwxoqJK4+eDkNMl5Z/MJZaoUPaP4/9lf81xXMe1I2ReTAptverZUpbPY4wWwWyL5g==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-layout-effect": "1.1.1",
        "@radix-ui/react-visually-hidden": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-toggle": {
      "version": "1.1.10",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-toggle/-/react-toggle-1.1.10.tgz",
      "integrity": "sha512-lS1odchhFTeZv3xwHH31YPObmJn8gOg7Lq12inrr0+BH/l3Tsq32VfjqH1oh80ARM3mlkfMic15n0kg4sD1poQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-toggle-group": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-toggle-group/-/react-toggle-group-1.1.11.tgz",
      "integrity": "sha512-5umnS0T8JQzQT6HbPyO7Hh9dgd82NmS36DQr+X/YJ9ctFNCiiQd6IJAYYZ33LUwm8M+taCz5t2ui29fHZc4Y6Q==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-toggle": "1.1.10",
        "@radix-ui/react-use-controllable-state": "1.2.2"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-toolbar": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-toolbar/-/react-toolbar-1.1.11.tgz",
      "integrity": "sha512-4ol06/1bLoFu1nwUqzdD4Y5RZ9oDdKeiHIsntug54Hcr1pgaHiPqHFEaXI1IFP/EsOfROQZ8Mig9VTIRza6Tjg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-separator": "1.1.7",
        "@radix-ui/react-toggle-group": "1.1.11"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-tooltip": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-tooltip/-/react-tooltip-1.2.8.tgz",
      "integrity": "sha512-tY7sVt1yL9ozIxvmbtN5qtmH2krXcBCfjEiCgKGLqunJHvgvZG2Pcl2oQ3kbcZARb1BGEHdkLzcYGO8ynVlieg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-id": "1.1.1",
        "@radix-ui/react-popper": "1.2.8",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-slot": "1.2.3",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-visually-hidden": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-callback-ref": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-callback-ref/-/react-use-callback-ref-1.1.1.tgz",
      "integrity": "sha512-FkBMwD+qbGQeMu1cOHnuGB6x4yzPjho8ap5WtbEJ26umhgqVXbhekKUQO+hZEL1vU92a3wHwdp0HAcqAUF5iDg==",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-controllable-state": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-controllable-state/-/react-use-controllable-state-1.2.2.tgz",
      "integrity": "sha512-BjasUjixPFdS+NKkypcyyN5Pmg83Olst0+c6vGov0diwTEo6mgdqVR6hxcEgFuh4QrAs7Rc+9KuGJ9TVCj0Zzg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-use-effect-event": "0.0.2",
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-effect-event": {
      "version": "0.0.2",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-effect-event/-/react-use-effect-event-0.0.2.tgz",
      "integrity": "sha512-Qp8WbZOBe+blgpuUT+lw2xheLP8q0oatc9UpmiemEICxGvFLYmHm9QowVZGHtJlGbS6A6yJ3iViad/2cVjnOiA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-escape-keydown": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-escape-keydown/-/react-use-escape-keydown-1.1.1.tgz",
      "integrity": "sha512-Il0+boE7w/XebUHyBjroE+DbByORGR9KKmITzbR7MyQ4akpORYP/ZmbhAr0DG7RmmBqoOnZdy2QlvajJ2QA59g==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-use-callback-ref": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-is-hydrated": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-is-hydrated/-/react-use-is-hydrated-0.1.0.tgz",
      "integrity": "sha512-U+UORVEq+cTnRIaostJv9AGdV3G6Y+zbVd+12e18jQ5A3c0xL03IhnHuiU4UV69wolOQp5GfR58NW/EgdQhwOA==",
      "license": "MIT",
      "dependencies": {
        "use-sync-external-store": "^1.5.0"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-layout-effect": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-layout-effect/-/react-use-layout-effect-1.1.1.tgz",
      "integrity": "sha512-RbJRS4UWQFkzHTTwVymMTUv8EqYhOp8dOOviLj2ugtTiXRaRQS7GLGxZTLL1jWhMeoSCf5zmcZkqTl9IiYfXcQ==",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-previous": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-previous/-/react-use-previous-1.1.1.tgz",
      "integrity": "sha512-2dHfToCj/pzca2Ck724OZ5L0EVrr3eHRNsG/b3xQJLA2hZpVCS99bLAX+hm1IHXDEnzU6by5z/5MIY794/a8NQ==",
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-rect": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-rect/-/react-use-rect-1.1.1.tgz",
      "integrity": "sha512-QTYuDesS0VtuHNNvMh+CjlKJ4LJickCMUAqjlE3+j8w+RlRpwyX3apEQKGFzbZGdo7XNG1tXa+bQqIE7HIXT2w==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/rect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-use-size": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-use-size/-/react-use-size-1.1.1.tgz",
      "integrity": "sha512-ewrXRDTAqAXlkl6t/fkXWNAhFX9I+CkKlw6zjEwk86RSPKwZr3xpBRso655aqYafwtnbpHLj6toFzmd6xdVptQ==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-use-layout-effect": "1.1.1"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/react-visually-hidden": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/@radix-ui/react-visually-hidden/-/react-visually-hidden-1.2.3.tgz",
      "integrity": "sha512-pzJq12tEaaIhqjbzpCuv/OypJY/BPavOofm+dbab+MHLajy277+1lLm6JFcGgF5eskJ6mquGirhXY2GD/8u8Ug==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/react-primitive": "2.1.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@radix-ui/rect": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/rect/-/rect-1.1.1.tgz",
      "integrity": "sha512-HPwpGIzkl28mWyZqG52jiqDJ12waP11Pa1lGoiyUkIEuMLBP0oeK/C89esbXrxsky5we7dfd8U58nm0SgAWpVw==",
      "license": "MIT"
    },
    "node_modules/@radix-ui/themes": {
      "version": "3.2.1",
      "resolved": "https://registry.npmjs.org/@radix-ui/themes/-/themes-3.2.1.tgz",
      "integrity": "sha512-WJL2YKAGItkunwm3O4cLTFKCGJTfAfF6Hmq7f5bCo1ggqC9qJQ/wfg/25AAN72aoEM1yqXZQ+pslsw48AFR0Xg==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/colors": "^3.0.0",
        "classnames": "^2.3.2",
        "radix-ui": "^1.1.3",
        "react-remove-scroll-bar": "^2.3.8"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/@rolldown/pluginutils": {
      "version": "1.0.0-beta.27",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.0-beta.27.tgz",
      "integrity": "sha512-+d0F4MKMCbeVUJwG96uQ4SgAznZNSq93I3V+9NHA4OpvqG8mRCpGdKmK8l/dl02h2CCDHwW2FqilnTyDcAnqjA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@rollup/plugin-inject": {
      "version": "5.0.5",
      "resolved": "https://registry.npmjs.org/@rollup/plugin-inject/-/plugin-inject-5.0.5.tgz",
      "integrity": "sha512-2+DEJbNBoPROPkgTDNe8/1YXWcqxbN5DTjASVIOx8HS+pITXushyNiBV56RB08zuptzz8gT3YfkqriTBVycepg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/pluginutils": "^5.0.1",
        "estree-walker": "^2.0.2",
        "magic-string": "^0.30.3"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/pluginutils": {
      "version": "5.3.0",
      "resolved": "https://registry.npmjs.org/@rollup/pluginutils/-/pluginutils-5.3.0.tgz",
      "integrity": "sha512-5EdhGZtnu3V88ces7s53hhfK5KSASnJZv8Lulpc04cWO3REESroJXg73DFsOmgbU2BhwV0E20bu2IDZb3VKW4Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "^1.0.0",
        "estree-walker": "^2.0.2",
        "picomatch": "^4.0.2"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "rollup": "^1.20.0||^2.0.0||^3.0.0||^4.0.0"
      },
      "peerDependenciesMeta": {
        "rollup": {
          "optional": true
        }
      }
    },
    "node_modules/@rollup/pluginutils/node_modules/picomatch": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz",
      "integrity": "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/@types/babel__core": {
      "version": "7.20.5",
      "resolved": "https://registry.npmjs.org/@types/babel__core/-/babel__core-7.20.5.tgz",
      "integrity": "sha512-qoQprZvz5wQFJwMDqeseRXWv3rqMvhgpbXFfVyWhbx9X47POIA6i/+dXefEmZKoAgOaTdaIgNSMqMIU61yRyzA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.20.7",
        "@babel/types": "^7.20.7",
        "@types/babel__generator": "*",
        "@types/babel__template": "*",
        "@types/babel__traverse": "*"
      }
    },
    "node_modules/@types/babel__generator": {
      "version": "7.27.0",
      "resolved": "https://registry.npmjs.org/@types/babel__generator/-/babel__generator-7.27.0.tgz",
      "integrity": "sha512-ufFd2Xi92OAVPYsy+P4n7/U7e68fex0+Ee8gSG9KX7eo084CWiQ4sdxktvdl0bOPupXtVJPY19zk6EwWqUQ8lg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__template": {
      "version": "7.4.4",
      "resolved": "https://registry.npmjs.org/@types/babel__template/-/babel__template-7.4.4.tgz",
      "integrity": "sha512-h/NUaSyG5EyxBIp8YRxo4RMe2/qQgvyowRwVMzhYhBCONbW8PUsg4lkFMrhgZhUe5z3L3MiLDuvyJ/CaPa2A8A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.1.0",
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__traverse": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@types/babel__traverse/-/babel__traverse-7.28.0.tgz",
      "integrity": "sha512-8PvcXf70gTDZBgt9ptxJ8elBeBjcLOAcOtoO/mPJjtji1+CdGbHgm77om1GrsPxsiE+uXIpNSK64UYaIwQXd4Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.2"
      }
    },
    "node_modules/@types/d3-color": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/@types/d3-color/-/d3-color-3.1.3.tgz",
      "integrity": "sha512-iO90scth9WAbmgv7ogoq57O9YpKmFBbmoEoCHDB2xMBY0+/KVrqAaCDyCE16dUspeOvIxFFRI+0sEtqDqy2b4A==",
      "license": "MIT"
    },
    "node_modules/@types/d3-drag": {
      "version": "3.0.7",
      "resolved": "https://registry.npmjs.org/@types/d3-drag/-/d3-drag-3.0.7.tgz",
      "integrity": "sha512-HE3jVKlzU9AaMazNufooRJ5ZpWmLIoc90A37WU2JMmeq28w1FQqCZswHZ3xR+SuxYftzHq6WU6KJHvqxKzTxxQ==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-selection": "*"
      }
    },
    "node_modules/@types/d3-interpolate": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-3.0.4.tgz",
      "integrity": "sha512-mgLPETlrpVV1YRJIglr4Ez47g7Yxjl1lj7YKsiMCb27VJH9W8NVM6Bb9d8kkpG/uAQS5AmbA48q2IAolKKo1MA==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-color": "*"
      }
    },
    "node_modules/@types/d3-selection": {
      "version": "3.0.11",
      "resolved": "https://registry.npmjs.org/@types/d3-selection/-/d3-selection-3.0.11.tgz",
      "integrity": "sha512-bhAXu23DJWsrI45xafYpkQ4NtcKMwWnAC/vKrd2l+nxMFuvOT3XMYTIj2opv8vq8AO5Yh7Qac/nSeP/3zjTK0w==",
      "license": "MIT"
    },
    "node_modules/@types/d3-transition": {
      "version": "3.0.9",
      "resolved": "https://registry.npmjs.org/@types/d3-transition/-/d3-transition-3.0.9.tgz",
      "integrity": "sha512-uZS5shfxzO3rGlu0cC3bjmMFKsXv+SmZZcgp0KD22ts4uGXp5EVYGzu/0YdwZeKmddhcAccYtREJKkPfXkZuCg==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-selection": "*"
      }
    },
    "node_modules/@types/d3-zoom": {
      "version": "3.0.8",
      "resolved": "https://registry.npmjs.org/@types/d3-zoom/-/d3-zoom-3.0.8.tgz",
      "integrity": "sha512-iqMC4/YlFCSlO8+2Ii1GGGliCAY4XdeG748w5vQUbevlbDu0zSjH/+jojorQVBK/se0j6DUFNPBGSqD3YWYnDw==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-interpolate": "*",
        "@types/d3-selection": "*"
      }
    },
    "node_modules/@types/estree": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.8.tgz",
      "integrity": "sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/node": {
      "version": "24.7.2",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-24.7.2.tgz",
      "integrity": "sha512-/NbVmcGTP+lj5oa4yiYxxeBjRivKQ5Ns1eSZeB99ExsEQ6rX5XYU1Zy/gGxY/ilqtD4Etx9mKyrPxZRetiahhA==",
      "license": "MIT",
      "dependencies": {
        "undici-types": "~7.14.0"
      }
    },
    "node_modules/@types/prop-types": {
      "version": "15.7.15",
      "resolved": "https://registry.npmjs.org/@types/prop-types/-/prop-types-15.7.15.tgz",
      "integrity": "sha512-F6bEyamV9jKGAFBEmlQnesRPGOQqS2+Uwi0Em15xenOxHaf2hv6L8YCVn3rPdPJOiJfPiCnLIRyvwVaqMY3MIw==",
      "devOptional": true,
      "license": "MIT"
    },
    "node_modules/@types/react": {
      "version": "18.3.26",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-18.3.26.tgz",
      "integrity": "sha512-RFA/bURkcKzx/X9oumPG9Vp3D3JUgus/d0b67KB0t5S/raciymilkOa66olh78MUI92QLbEJevO7rvqU/kjwKA==",
      "devOptional": true,
      "license": "MIT",
      "dependencies": {
        "@types/prop-types": "*",
        "csstype": "^3.0.2"
      }
    },
    "node_modules/@types/react-dom": {
      "version": "18.3.7",
      "resolved": "https://registry.npmjs.org/@types/react-dom/-/react-dom-18.3.7.tgz",
      "integrity": "sha512-MEe3UeoENYVFXzoXEWsvcpg6ZvlrFNlOQ7EOsvhI3CfAXwzPfO8Qwuxd40nepsYKqyyVQnTdEfv68q91yLcKrQ==",
      "devOptional": true,
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "^18.0.0"
      }
    },
    "node_modules/@vitejs/plugin-react": {
      "version": "4.7.0",
      "resolved": "https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-4.7.0.tgz",
      "integrity": "sha512-gUu9hwfWvvEDBBmgtAowQCojwZmJ5mcLn3aufeCsitijs3+f2NsrPtlAWIR6OPiqljl96GVCUbLe0HyqIpVaoA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/core": "^7.28.0",
        "@babel/plugin-transform-react-jsx-self": "^7.27.1",
        "@babel/plugin-transform-react-jsx-source": "^7.27.1",
        "@rolldown/pluginutils": "1.0.0-beta.27",
        "@types/babel__core": "^7.20.5",
        "react-refresh": "^0.17.0"
      },
      "engines": {
        "node": "^14.18.0 || >=16.0.0"
      },
      "peerDependencies": {
        "vite": "^4.2.0 || ^5.0.0 || ^6.0.0 || ^7.0.0"
      }
    },
    "node_modules/@xyflow/react": {
      "version": "12.8.6",
      "resolved": "https://registry.npmjs.org/@xyflow/react/-/react-12.8.6.tgz",
      "integrity": "sha512-SksAm2m4ySupjChphMmzvm55djtgMDPr+eovPDdTnyGvShf73cvydfoBfWDFllooIQ4IaiUL5yfxHRwU0c37EA==",
      "license": "MIT",
      "dependencies": {
        "@xyflow/system": "0.0.70",
        "classcat": "^5.0.3",
        "zustand": "^4.4.0"
      },
      "peerDependencies": {
        "react": ">=17",
        "react-dom": ">=17"
      }
    },
    "node_modules/@xyflow/system": {
      "version": "0.0.70",
      "resolved": "https://registry.npmjs.org/@xyflow/system/-/system-0.0.70.tgz",
      "integrity": "sha512-PpC//u9zxdjj0tfTSmZrg3+sRbTz6kop/Amky44U2Dl51sxzDTIUfXMwETOYpmr2dqICWXBIJwXL2a9QWtX2XA==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-drag": "^3.0.7",
        "@types/d3-interpolate": "^3.0.4",
        "@types/d3-selection": "^3.0.10",
        "@types/d3-transition": "^3.0.8",
        "@types/d3-zoom": "^3.0.8",
        "d3-drag": "^3.0.0",
        "d3-interpolate": "^3.0.1",
        "d3-selection": "^3.0.0",
        "d3-zoom": "^3.0.0"
      }
    },
    "node_modules/agent-base": {
      "version": "7.1.4",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-7.1.4.tgz",
      "integrity": "sha512-MnA+YT8fwfJPgBx3m60MNqakm30XOkyIoH1y6huTQvC0PwZG7ki8NacLBcrPbNoo8vEZy7Jpuk7+jMO+CUovTQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 14"
      }
    },
    "node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "license": "MIT",
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
    "node_modules/aria-hidden": {
      "version": "1.2.6",
      "resolved": "https://registry.npmjs.org/aria-hidden/-/aria-hidden-1.2.6.tgz",
      "integrity": "sha512-ik3ZgC9dY/lYVVM++OISsaYDeg1tb0VtP5uL3ouh1koGOaUMDPpbFIei4JkFimWUFPn90sbMNMXQAIVOlnYKJA==",
      "license": "MIT",
      "dependencies": {
        "tslib": "^2.0.0"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/asn1.js": {
      "version": "4.10.1",
      "resolved": "https://registry.npmjs.org/asn1.js/-/asn1.js-4.10.1.tgz",
      "integrity": "sha512-p32cOF5q0Zqs9uBiONKYLm6BClCoBCM5O9JfeUSlnQLBTxYdTK+pW+nXflm8UkKd2UYlEbYz5qEi0JuZR9ckSw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bn.js": "^4.0.0",
        "inherits": "^2.0.1",
        "minimalistic-assert": "^1.0.0"
      }
    },
    "node_modules/asn1.js/node_modules/bn.js": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.12.2.tgz",
      "integrity": "sha512-n4DSx829VRTRByMRGdjQ9iqsN0Bh4OolPsFnaZBLcbi8iXcB+kJ9s7EnRt4wILZNV3kPLHkRVfOc/HvhC3ovDw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/assert": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/assert/-/assert-2.1.0.tgz",
      "integrity": "sha512-eLHpSK/Y4nhMJ07gDaAzoX/XAKS8PSaojml3M0DM4JpV1LAi5JOJ/p6H/XWrl8L+DzVEvVCW1z3vWAaB9oTsQw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.2",
        "is-nan": "^1.3.2",
        "object-is": "^1.1.5",
        "object.assign": "^4.1.4",
        "util": "^0.12.5"
      }
    },
    "node_modules/available-typed-arrays": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/available-typed-arrays/-/available-typed-arrays-1.0.7.tgz",
      "integrity": "sha512-wvUjBtSGN7+7SjNpq/9M2Tg350UZD3q62IFZLbRAR1bSMlCo1ZaeW+BJ+D090e4hIIZLBcTDWe4Mh4jvUDajzQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "possible-typed-array-names": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/baseline-browser-mapping": {
      "version": "2.8.16",
      "resolved": "https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.8.16.tgz",
      "integrity": "sha512-OMu3BGQ4E7P1ErFsIPpbJh0qvDudM/UuJeHgkAvfWe+0HFJCXh+t/l8L6fVLR55RI/UbKrVLnAXZSVwd9ysWYw==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "baseline-browser-mapping": "dist/cli.js"
      }
    },
    "node_modules/bignumber.js": {
      "version": "9.3.1",
      "resolved": "https://registry.npmjs.org/bignumber.js/-/bignumber.js-9.3.1.tgz",
      "integrity": "sha512-Ko0uX15oIUS7wJ3Rb30Fs6SkVbLmPBAKdlm7q9+ak9bbIeFf0MwuBsQV6z7+X768/cHsfg+WlysDWJcmthjsjQ==",
      "license": "MIT",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/bn.js": {
      "version": "5.2.2",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-5.2.2.tgz",
      "integrity": "sha512-v2YAxEmKaBLahNwE1mjp4WON6huMNeuDvagFZW+ASCuA/ku0bXR9hSMw0XpiqMoA3+rmnyck/tPRSFQkoC9Cuw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/brorand": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/brorand/-/brorand-1.1.0.tgz",
      "integrity": "sha512-cKV8tMCEpQs4hK/ik71d6LrPOnpkpGBR0wzxqr68g2m/LB2GxVYQroAjMJZRVM1Y4BCjCKc3vAamxSzOY2RP+w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/browser-resolve": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/browser-resolve/-/browser-resolve-2.0.0.tgz",
      "integrity": "sha512-7sWsQlYL2rGLy2IWm8WL8DCTJvYLc/qlOnsakDac87SOoCd16WLsaAMdCiAqsTNHIe+SXfaqyxyo6THoWqs8WQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "resolve": "^1.17.0"
      }
    },
    "node_modules/browserify-aes": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/browserify-aes/-/browserify-aes-1.2.0.tgz",
      "integrity": "sha512-+7CHXqGuspUn/Sl5aO7Ea0xWGAtETPXNSAjHo48JfLdPWcMng33Xe4znFvQweqc/uzk5zSOI3H52CYnjCfb5hA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "buffer-xor": "^1.0.3",
        "cipher-base": "^1.0.0",
        "create-hash": "^1.1.0",
        "evp_bytestokey": "^1.0.3",
        "inherits": "^2.0.1",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/browserify-cipher": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/browserify-cipher/-/browserify-cipher-1.0.1.tgz",
      "integrity": "sha512-sPhkz0ARKbf4rRQt2hTpAHqn47X3llLkUGn+xEJzLjwY8LRs2p0v7ljvI5EyoRO/mexrNunNECisZs+gw2zz1w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "browserify-aes": "^1.0.4",
        "browserify-des": "^1.0.0",
        "evp_bytestokey": "^1.0.0"
      }
    },
    "node_modules/browserify-des": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/browserify-des/-/browserify-des-1.0.2.tgz",
      "integrity": "sha512-BioO1xf3hFwz4kc6iBhI3ieDFompMhrMlnDFC4/0/vd5MokpuAc3R+LYbwTA9A5Yc9pq9UYPqffKpW2ObuwX5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "cipher-base": "^1.0.1",
        "des.js": "^1.0.0",
        "inherits": "^2.0.1",
        "safe-buffer": "^5.1.2"
      }
    },
    "node_modules/browserify-rsa": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/browserify-rsa/-/browserify-rsa-4.1.1.tgz",
      "integrity": "sha512-YBjSAiTqM04ZVei6sXighu679a3SqWORA3qZTEqZImnlkDIFtKc6pNutpjyZ8RJTjQtuYfeetkxM11GwoYXMIQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bn.js": "^5.2.1",
        "randombytes": "^2.1.0",
        "safe-buffer": "^5.2.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/browserify-sign": {
      "version": "4.2.5",
      "resolved": "https://registry.npmjs.org/browserify-sign/-/browserify-sign-4.2.5.tgz",
      "integrity": "sha512-C2AUdAJg6rlM2W5QMp2Q4KGQMVBwR1lIimTsUnutJ8bMpW5B52pGpR2gEnNBNwijumDo5FojQ0L9JrXA8m4YEw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "bn.js": "^5.2.2",
        "browserify-rsa": "^4.1.1",
        "create-hash": "^1.2.0",
        "create-hmac": "^1.1.7",
        "elliptic": "^6.6.1",
        "inherits": "^2.0.4",
        "parse-asn1": "^5.1.9",
        "readable-stream": "^2.3.8",
        "safe-buffer": "^5.2.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/browserify-sign/node_modules/isarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
      "integrity": "sha512-VLghIWNM6ELQzo7zwmcg0NmTVyWKYjvIeM83yjp0wRDTmUnrM678fQbcKBo6n2CJEF0szoG//ytg+TKla89ALQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/browserify-sign/node_modules/readable-stream": {
      "version": "2.3.8",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz",
      "integrity": "sha512-8p0AUk4XODgIewSi0l8Epjs+EVnWiK7NoDIEGU0HhE7+ZyY8D1IMY7odu5lRrFXGg71L15KG8QrPmum45RTtdA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "core-util-is": "~1.0.0",
        "inherits": "~2.0.3",
        "isarray": "~1.0.0",
        "process-nextick-args": "~2.0.0",
        "safe-buffer": "~5.1.1",
        "string_decoder": "~1.1.1",
        "util-deprecate": "~1.0.1"
      }
    },
    "node_modules/browserify-sign/node_modules/readable-stream/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/browserify-sign/node_modules/string_decoder": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz",
      "integrity": "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "~5.1.0"
      }
    },
    "node_modules/browserify-sign/node_modules/string_decoder/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/browserify-zlib": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/browserify-zlib/-/browserify-zlib-0.2.0.tgz",
      "integrity": "sha512-Z942RysHXmJrhqk88FmKBVq/v5tqmSkDz7p54G/MGyjMnCFFnC79XWNbg+Vta8W6Wb2qtSZTSxIGkJrRpCFEiA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "pako": "~1.0.5"
      }
    },
    "node_modules/browserslist": {
      "version": "4.26.3",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.26.3.tgz",
      "integrity": "sha512-lAUU+02RFBuCKQPj/P6NgjlbCnLBMp4UtgTx7vNHd3XSIJF87s9a5rA3aH2yw3GS9DqZAUbOtZdCCiZeVRqt0w==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "baseline-browser-mapping": "^2.8.9",
        "caniuse-lite": "^1.0.30001746",
        "electron-to-chromium": "^1.5.227",
        "node-releases": "^2.0.21",
        "update-browserslist-db": "^1.1.3"
      },
      "bin": {
        "browserslist": "cli.js"
      },
      "engines": {
        "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
      }
    },
    "node_modules/buffer": {
      "version": "5.7.1",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz",
      "integrity": "sha512-EHcyIPBQ4BSGlvjB16k5KgAJ27CIsHY/2JBmCRReo48y9rQ3MaUzWX3KVlBa4U7MyX02HdVj0K7C3WaB3ju7FQ==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "base64-js": "^1.3.1",
        "ieee754": "^1.1.13"
      }
    },
    "node_modules/buffer-equal-constant-time": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/buffer-equal-constant-time/-/buffer-equal-constant-time-1.0.1.tgz",
      "integrity": "sha512-zRpUiDwd/xk6ADqPMATG8vc9VPrkck7T07OIx0gnjmJAnHnTVXNQG3vfvWNuiZIkwu9KrKdA1iJKfsfTVxE6NA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/buffer-xor": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/buffer-xor/-/buffer-xor-1.0.3.tgz",
      "integrity": "sha512-571s0T7nZWK6vB67HI5dyUF7wXiNcfaPPPTl6zYCNApANjIvYJTg7hlud/+cJpdAhS7dVzqMLmfhfHR3rAcOjQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/builtin-status-codes": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/builtin-status-codes/-/builtin-status-codes-3.0.0.tgz",
      "integrity": "sha512-HpGFw18DgFWlncDfjTa2rcQ4W88O1mC8e8yZ2AvQY5KDaktSTwo+KRf6nHK6FRI5FyRyb/5T6+TSxfP7QyGsmQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/call-bind": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/call-bind/-/call-bind-1.0.8.tgz",
      "integrity": "sha512-oKlSFMcMwpUg2ednkhQ454wfWiU/ul3CkJe/PEHcTKuiX6RpbehUiFMXu13HalGZxfUwCQzZG747YXBn1im9ww==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.0",
        "es-define-property": "^1.0.0",
        "get-intrinsic": "^1.2.4",
        "set-function-length": "^1.2.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/caniuse-lite": {
      "version": "1.0.30001750",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001750.tgz",
      "integrity": "sha512-cuom0g5sdX6rw00qOoLNSFCJ9/mYIsuSOA+yzpDw8eopiFqcVwQvZHqov0vmEighRxX++cfC0Vg1G+1Iy/mSpQ==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "CC-BY-4.0"
    },
    "node_modules/chokidar": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-4.0.3.tgz",
      "integrity": "sha512-Qgzu8kfBvo+cA4962jnP1KkS6Dop5NS6g7R5LFYJr4b8Ub94PPQXUksCw9PvXoeXPRRddRNC5C1JQUR2SMGtnA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "readdirp": "^4.0.1"
      },
      "engines": {
        "node": ">= 14.16.0"
      },
      "funding": {
        "url": "https://paulmillr.com/funding/"
      }
    },
    "node_modules/cipher-base": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/cipher-base/-/cipher-base-1.0.7.tgz",
      "integrity": "sha512-Mz9QMT5fJe7bKI7MH31UilT5cEK5EHHRCccw/YRFsRY47AuNgaV6HY3rscp0/I4Q+tTW/5zoqpSeRRI54TkDWA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.4",
        "safe-buffer": "^5.2.1",
        "to-buffer": "^1.2.2"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/classcat": {
      "version": "5.0.5",
      "resolved": "https://registry.npmjs.org/classcat/-/classcat-5.0.5.tgz",
      "integrity": "sha512-JhZUT7JFcQy/EzW605k/ktHtncoo9vnyW/2GspNYwFlN1C/WmjuV/xtS04e9SOkL2sTdw0VAZ2UGCcQ9lR6p6w==",
      "license": "MIT"
    },
    "node_modules/classnames": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/classnames/-/classnames-2.5.1.tgz",
      "integrity": "sha512-saHYOzhIQs6wy2sVxTM6bUDsQO4F50V9RQ22qBpEdCW+I+/Wmke2HOl6lS6dTpdxVhb88/I6+Hs+438c3lfUow==",
      "license": "MIT"
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "license": "MIT",
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
      "license": "MIT"
    },
    "node_modules/console-browserify": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/console-browserify/-/console-browserify-1.2.0.tgz",
      "integrity": "sha512-ZMkYO/LkF17QvCPqM0gxw8yUzigAOZOSWSHg91FH6orS7vcEj5dVZTidN2fQ14yBSdg97RqhSNwLUXInd52OTA==",
      "dev": true
    },
    "node_modules/constants-browserify": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/constants-browserify/-/constants-browserify-1.0.0.tgz",
      "integrity": "sha512-xFxOwqIzR/e1k1gLiWEophSCMqXcwVHIH7akf7b/vxcUeGunlj3hvZaaqxwHsTgn+IndtkQJgSztIDWeumWJDQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/convert-source-map": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz",
      "integrity": "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/core-util-is": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz",
      "integrity": "sha512-ZQBvi1DcpJ4GDqanjucZ2Hj3wEO5pZDS89BWbkcrvdxksJorwUDDZamX9ldFkp9aw2lmBDLgkObEA4DWNJ9FYQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/create-ecdh": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/create-ecdh/-/create-ecdh-4.0.4.tgz",
      "integrity": "sha512-mf+TCx8wWc9VpuxfP2ht0iSISLZnt0JgWlrOKZiNqyUZWnjIaCIVNQArMHnCZKfEYRg6IM7A+NeJoN8gf/Ws0A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bn.js": "^4.1.0",
        "elliptic": "^6.5.3"
      }
    },
    "node_modules/create-ecdh/node_modules/bn.js": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.12.2.tgz",
      "integrity": "sha512-n4DSx829VRTRByMRGdjQ9iqsN0Bh4OolPsFnaZBLcbi8iXcB+kJ9s7EnRt4wILZNV3kPLHkRVfOc/HvhC3ovDw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/create-hash": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/create-hash/-/create-hash-1.2.0.tgz",
      "integrity": "sha512-z00bCGNHDG8mHAkP7CtT1qVu+bFQUPjYq/4Iv3C3kWjTFV10zIjfSoeqXo9Asws8gwSHDGj/hl2u4OGIjapeCg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "cipher-base": "^1.0.1",
        "inherits": "^2.0.1",
        "md5.js": "^1.3.4",
        "ripemd160": "^2.0.1",
        "sha.js": "^2.4.0"
      }
    },
    "node_modules/create-hmac": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/create-hmac/-/create-hmac-1.1.7.tgz",
      "integrity": "sha512-MJG9liiZ+ogc4TzUwuvbER1JRdgvUFSB5+VR/g5h82fGaIRWMWddtKBHi7/sVhfjQZ6SehlyhvQYrcYkaUIpLg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "cipher-base": "^1.0.3",
        "create-hash": "^1.1.0",
        "inherits": "^2.0.1",
        "ripemd160": "^2.0.0",
        "safe-buffer": "^5.0.1",
        "sha.js": "^2.4.8"
      }
    },
    "node_modules/create-require": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/create-require/-/create-require-1.1.1.tgz",
      "integrity": "sha512-dcKFX3jn0MpIaXjisoRvexIJVEKzaq7z2rZKxf+MSr9TkdmHmsU4m2lcLojrj/FHl8mk5VxMmYA+ftRkP/3oKQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/crypto-browserify": {
      "version": "3.12.1",
      "resolved": "https://registry.npmjs.org/crypto-browserify/-/crypto-browserify-3.12.1.tgz",
      "integrity": "sha512-r4ESw/IlusD17lgQi1O20Fa3qNnsckR126TdUuBgAu7GBYSIPvdNyONd3Zrxh0xCwA4+6w/TDArBPsMvhur+KQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "browserify-cipher": "^1.0.1",
        "browserify-sign": "^4.2.3",
        "create-ecdh": "^4.0.4",
        "create-hash": "^1.2.0",
        "create-hmac": "^1.1.7",
        "diffie-hellman": "^5.0.3",
        "hash-base": "~3.0.4",
        "inherits": "^2.0.4",
        "pbkdf2": "^3.1.2",
        "public-encrypt": "^4.0.3",
        "randombytes": "^2.1.0",
        "randomfill": "^1.0.4"
      },
      "engines": {
        "node": ">= 0.10"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/csstype": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.1.3.tgz",
      "integrity": "sha512-M1uQkMl8rQK/szD0LNhtqxIPLpimGm8sOBwU7lLnCpSbTyY3yeU1Vc7l4KT5zT4s/yOxHH5O7tIuuLOCnLADRw==",
      "devOptional": true,
      "license": "MIT"
    },
    "node_modules/d3-color": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-color/-/d3-color-3.1.0.tgz",
      "integrity": "sha512-zg/chbXyeBtMQ1LbD/WSoW2DpC3I0mpmPdW+ynRTj/x2DAWYrIY7qeZIHidozwV24m4iavr15lNwIwLxRmOxhA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-dispatch": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-dispatch/-/d3-dispatch-3.0.1.tgz",
      "integrity": "sha512-rzUyPU/S7rwUflMyLc1ETDeBj0NRuHKKAcvukozwhshr6g6c5d8zh4c2gQjY2bZ0dXeGLWc1PF174P2tVvKhfg==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-drag": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/d3-drag/-/d3-drag-3.0.0.tgz",
      "integrity": "sha512-pWbUJLdETVA8lQNJecMxoXfH6x+mO2UQo8rSmZ+QqxcbyA3hfeprFgIT//HW2nlHChWeIIMwS2Fq+gEARkhTkg==",
      "license": "ISC",
      "dependencies": {
        "d3-dispatch": "1 - 3",
        "d3-selection": "3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-ease": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-ease/-/d3-ease-3.0.1.tgz",
      "integrity": "sha512-wR/XK3D3XcLIZwpbvQwQ5fK+8Ykds1ip7A2Txe0yxncXSdq1L9skcG7blcedkOX+ZcgxGAmLX1FrRGbADwzi0w==",
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-interpolate": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-interpolate/-/d3-interpolate-3.0.1.tgz",
      "integrity": "sha512-3bYs1rOD33uo8aqJfKP3JWPAibgw8Zm2+L9vBKEHJ2Rg+viTR7o5Mmv5mZcieN+FRYaAOWX5SJATX6k1PWz72g==",
      "license": "ISC",
      "dependencies": {
        "d3-color": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-selection": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/d3-selection/-/d3-selection-3.0.0.tgz",
      "integrity": "sha512-fmTRWbNMmsmWq6xJV8D19U/gw/bwrHfNXxrIN+HfZgnzqTHp9jOmKMhsTUjXOJnZOdZY9Q28y4yebKzqDKlxlQ==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-timer": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-timer/-/d3-timer-3.0.1.tgz",
      "integrity": "sha512-ndfJ/JxxMd3nw31uyKoY2naivF+r29V+Lc0svZxe1JvvIRmi8hUsrMvdOwgS1o6uBHmiz91geQ0ylPP0aj1VUA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-transition": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-transition/-/d3-transition-3.0.1.tgz",
      "integrity": "sha512-ApKvfjsSR6tg06xrL434C0WydLr7JewBB3V+/39RMHsaXTOG0zmt/OAXeng5M5LBm0ojmxJrpomQVZ1aPvBL4w==",
      "license": "ISC",
      "dependencies": {
        "d3-color": "1 - 3",
        "d3-dispatch": "1 - 3",
        "d3-ease": "1 - 3",
        "d3-interpolate": "1 - 3",
        "d3-timer": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      },
      "peerDependencies": {
        "d3-selection": "2 - 3"
      }
    },
    "node_modules/d3-zoom": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/d3-zoom/-/d3-zoom-3.0.0.tgz",
      "integrity": "sha512-b8AmV3kfQaqWAuacbPuNbL6vahnOJflOhexLzMMNLga62+/nh0JzvJ0aO/5a5MVgUFGS7Hu1P9P03o3fJkDCyw==",
      "license": "ISC",
      "dependencies": {
        "d3-dispatch": "1 - 3",
        "d3-drag": "2 - 3",
        "d3-interpolate": "1 - 3",
        "d3-selection": "2 - 3",
        "d3-transition": "2 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/define-data-property": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/define-data-property/-/define-data-property-1.1.4.tgz",
      "integrity": "sha512-rBMvIzlpA8v6E+SJZoo++HAYqsLrkg7MSfIinMPFhmkorw7X+dOXVJQs+QT69zGkzMyfDnIMN2Wid1+NbL3T+A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-define-property": "^1.0.0",
        "es-errors": "^1.3.0",
        "gopd": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/define-properties": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/define-properties/-/define-properties-1.2.1.tgz",
      "integrity": "sha512-8QmQKqEASLd5nx0U1B1okLElbUuuttJ/AnYmRXbbbGDWh6uS208EjD4Xqq/I9wK7u0v6O08XhTWnt5XtEbR6Dg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "define-data-property": "^1.0.1",
        "has-property-descriptors": "^1.0.0",
        "object-keys": "^1.1.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/des.js": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/des.js/-/des.js-1.1.0.tgz",
      "integrity": "sha512-r17GxjhUCjSRy8aiJpr8/UadFIzMzJGexI3Nmz4ADi9LYSFx4gTBp80+NaX/YsXWWLhpZ7v/v/ubEc/bCNfKwg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.1",
        "minimalistic-assert": "^1.0.0"
      }
    },
    "node_modules/detect-libc": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-1.0.3.tgz",
      "integrity": "sha512-pGjwhsmsp4kL2RTz08wcOlGN83otlqHeD/Z5T8GXZB+/YcpQ/dgo+lbU8ZsGxV0HIvqqxo9l7mqYwyYMD9bKDg==",
      "dev": true,
      "license": "Apache-2.0",
      "optional": true,
      "bin": {
        "detect-libc": "bin/detect-libc.js"
      },
      "engines": {
        "node": ">=0.10"
      }
    },
    "node_modules/detect-node-es": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/detect-node-es/-/detect-node-es-1.1.0.tgz",
      "integrity": "sha512-ypdmJU/TbBby2Dxibuv7ZLW3Bs1QEmM7nHjEANfohJLvE0XVujisn1qPJcZxg+qDucsr+bP6fLD1rPS3AhJ7EQ==",
      "license": "MIT"
    },
    "node_modules/diffie-hellman": {
      "version": "5.0.3",
      "resolved": "https://registry.npmjs.org/diffie-hellman/-/diffie-hellman-5.0.3.tgz",
      "integrity": "sha512-kqag/Nl+f3GwyK25fhUMYj81BUOrZ9IuJsjIcDE5icNM9FJHAVm3VcUDxdLPoQtTuUylWm6ZIknYJwwaPxsUzg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bn.js": "^4.1.0",
        "miller-rabin": "^4.0.0",
        "randombytes": "^2.0.0"
      }
    },
    "node_modules/diffie-hellman/node_modules/bn.js": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.12.2.tgz",
      "integrity": "sha512-n4DSx829VRTRByMRGdjQ9iqsN0Bh4OolPsFnaZBLcbi8iXcB+kJ9s7EnRt4wILZNV3kPLHkRVfOc/HvhC3ovDw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/domain-browser": {
      "version": "4.22.0",
      "resolved": "https://registry.npmjs.org/domain-browser/-/domain-browser-4.22.0.tgz",
      "integrity": "sha512-IGBwjF7tNk3cwypFNH/7bfzBcgSCbaMOD3GsaY1AU/JRrnHnYgEM0+9kQt52iZxjNsjBtJYtao146V+f8jFZNw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://bevry.me/fund"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/ecdsa-sig-formatter": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/ecdsa-sig-formatter/-/ecdsa-sig-formatter-1.0.11.tgz",
      "integrity": "sha512-nagl3RYrbNv6kQkeJIpt6NJZy8twLB/2vtz6yN9Z4vRKHN4/QZJIEbqohALSgwKdnksuY3k5Addp5lg8sVoVcQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/electron-to-chromium": {
      "version": "1.5.234",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.234.tgz",
      "integrity": "sha512-RXfEp2x+VRYn8jbKfQlRImzoJU01kyDvVPBmG39eU2iuRVhuS6vQNocB8J0/8GrIMLnPzgz4eW6WiRnJkTuNWg==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/elliptic": {
      "version": "6.6.1",
      "resolved": "https://registry.npmjs.org/elliptic/-/elliptic-6.6.1.tgz",
      "integrity": "sha512-RaddvvMatK2LJHqFJ+YA4WysVN5Ita9E35botqIYspQ4TkRAlCicdzKOjlyv/1Za5RyTNn7di//eEV0uTAfe3g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bn.js": "^4.11.9",
        "brorand": "^1.1.0",
        "hash.js": "^1.0.0",
        "hmac-drbg": "^1.0.1",
        "inherits": "^2.0.4",
        "minimalistic-assert": "^1.0.1",
        "minimalistic-crypto-utils": "^1.0.1"
      }
    },
    "node_modules/elliptic/node_modules/bn.js": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.12.2.tgz",
      "integrity": "sha512-n4DSx829VRTRByMRGdjQ9iqsN0Bh4OolPsFnaZBLcbi8iXcB+kJ9s7EnRt4wILZNV3kPLHkRVfOc/HvhC3ovDw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "license": "MIT"
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
      "integrity": "sha512-FGgH2h8zKNim9ljj7dankFPcICIK9Cp5bm+c2gQSYePhpaG5+esrLODihIorn+Pe6FGJzWhXQotPv73jTaldXA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/esbuild": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.18.20.tgz",
      "integrity": "sha512-ceqxoedUrcayh7Y7ZX6NdbbDzGROiyVBgC4PriJThBKSVPWnnFHZAkfI1lJT8QFkOwH4qOS2SJkS4wvpGl8BpA==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "bin": {
        "esbuild": "bin/esbuild"
      },
      "engines": {
        "node": ">=12"
      },
      "optionalDependencies": {
        "@esbuild/android-arm": "0.18.20",
        "@esbuild/android-arm64": "0.18.20",
        "@esbuild/android-x64": "0.18.20",
        "@esbuild/darwin-arm64": "0.18.20",
        "@esbuild/darwin-x64": "0.18.20",
        "@esbuild/freebsd-arm64": "0.18.20",
        "@esbuild/freebsd-x64": "0.18.20",
        "@esbuild/linux-arm": "0.18.20",
        "@esbuild/linux-arm64": "0.18.20",
        "@esbuild/linux-ia32": "0.18.20",
        "@esbuild/linux-loong64": "0.18.20",
        "@esbuild/linux-mips64el": "0.18.20",
        "@esbuild/linux-ppc64": "0.18.20",
        "@esbuild/linux-riscv64": "0.18.20",
        "@esbuild/linux-s390x": "0.18.20",
        "@esbuild/linux-x64": "0.18.20",
        "@esbuild/netbsd-x64": "0.18.20",
        "@esbuild/openbsd-x64": "0.18.20",
        "@esbuild/sunos-x64": "0.18.20",
        "@esbuild/win32-arm64": "0.18.20",
        "@esbuild/win32-ia32": "0.18.20",
        "@esbuild/win32-x64": "0.18.20"
      }
    },
    "node_modules/esbuild-wasm": {
      "version": "0.25.11",
      "resolved": "https://registry.npmjs.org/esbuild-wasm/-/esbuild-wasm-0.25.11.tgz",
      "integrity": "sha512-60gllbYFIRGzB6KALBB5Va9Wy3VeCi2U0NgmM7r+TFnRgzeEyoCn2D7fhacW2zWbd7MUeTKLDE7RlfYGBQ00bw==",
      "license": "MIT",
      "bin": {
        "esbuild": "bin/esbuild"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/estree-walker": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/estree-walker/-/estree-walker-2.0.2.tgz",
      "integrity": "sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/events": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/events/-/events-3.3.0.tgz",
      "integrity": "sha512-mQw+2fkQbALzQ7V0MY0IqdnXNOeTtP4r0lN9z7AAawCXgqea7bDii20AYrIBrFd/Hx0M2Ocz6S111CaFkUcb0Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.8.x"
      }
    },
    "node_modules/evp_bytestokey": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/evp_bytestokey/-/evp_bytestokey-1.0.3.tgz",
      "integrity": "sha512-/f2Go4TognH/KvCISP7OUsHn85hT9nUkxxA9BEWxFn+Oj9o8ZNLm/40hdlgSLyuOimsrTKLUMEorQexp/aPQeA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "md5.js": "^1.3.4",
        "safe-buffer": "^5.1.1"
      }
    },
    "node_modules/extend": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
      "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==",
      "license": "MIT"
    },
    "node_modules/faye-websocket": {
      "version": "0.11.4",
      "resolved": "https://registry.npmjs.org/faye-websocket/-/faye-websocket-0.11.4.tgz",
      "integrity": "sha512-CzbClwlXAuiRQAlUyfqPgvPoNKTckTPGfwZV4ZdAhVcP2lh9KUxJg2b5GkE7XbjKQ3YJnQ9z6D9ntLAlB+tP8g==",
      "license": "Apache-2.0",
      "dependencies": {
        "websocket-driver": ">=0.5.1"
      },
      "engines": {
        "node": ">=0.8.0"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/find-up": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz",
      "integrity": "sha512-78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "locate-path": "^6.0.0",
        "path-exists": "^4.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/firebase": {
      "version": "12.4.0",
      "resolved": "https://registry.npmjs.org/firebase/-/firebase-12.4.0.tgz",
      "integrity": "sha512-/chNgDQ6ppPPGOQO4jctxOa/5JeQxuhaxA7Y90K0I+n/wPfoO8mRveedhVUdo7ExLcWUivnnow/ouSLYSI5Icw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/ai": "2.4.0",
        "@firebase/analytics": "0.10.19",
        "@firebase/analytics-compat": "0.2.25",
        "@firebase/app": "0.14.4",
        "@firebase/app-check": "0.11.0",
        "@firebase/app-check-compat": "0.4.0",
        "@firebase/app-compat": "0.5.4",
        "@firebase/app-types": "0.9.3",
        "@firebase/auth": "1.11.0",
        "@firebase/auth-compat": "0.6.0",
        "@firebase/data-connect": "0.3.11",
        "@firebase/database": "1.1.0",
        "@firebase/database-compat": "2.1.0",
        "@firebase/firestore": "4.9.2",
        "@firebase/firestore-compat": "0.4.2",
        "@firebase/functions": "0.13.1",
        "@firebase/functions-compat": "0.4.1",
        "@firebase/installations": "0.6.19",
        "@firebase/installations-compat": "0.2.19",
        "@firebase/messaging": "0.12.23",
        "@firebase/messaging-compat": "0.2.23",
        "@firebase/performance": "0.7.9",
        "@firebase/performance-compat": "0.2.22",
        "@firebase/remote-config": "0.7.0",
        "@firebase/remote-config-compat": "0.2.20",
        "@firebase/storage": "0.14.0",
        "@firebase/storage-compat": "0.4.0",
        "@firebase/util": "1.13.0"
      }
    },
    "node_modules/firebase/node_modules/@firebase/auth": {
      "version": "1.11.0",
      "resolved": "https://registry.npmjs.org/@firebase/auth/-/auth-1.11.0.tgz",
      "integrity": "sha512-5j7+ua93X+IRcJ1oMDTClTo85l7Xe40WSkoJ+shzPrX7OISlVWLdE1mKC57PSD+/LfAbdhJmvKixINBw2ESK6w==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.7.0",
        "@firebase/logger": "0.5.0",
        "@firebase/util": "1.13.0",
        "tslib": "^2.1.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@firebase/app": "0.x",
        "@react-native-async-storage/async-storage": "^1.18.1"
      },
      "peerDependenciesMeta": {
        "@react-native-async-storage/async-storage": {
          "optional": true
        }
      }
    },
    "node_modules/for-each": {
      "version": "0.3.5",
      "resolved": "https://registry.npmjs.org/for-each/-/for-each-0.3.5.tgz",
      "integrity": "sha512-dKx12eRCVIzqCxFGplyFKJMPvLEWgmNtUrpTiJIR5u97zEhRG8ySrtboPHZXx7daLxQVrl643cTzbab2tkQjxg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-callable": "^1.2.7"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gaxios": {
      "version": "6.7.1",
      "resolved": "https://registry.npmjs.org/gaxios/-/gaxios-6.7.1.tgz",
      "integrity": "sha512-LDODD4TMYx7XXdpwxAVRAIAuB0bzv0s+ywFonY46k126qzQHT9ygyoa9tncmOiQmmDrik65UYsEkv3lbfqQ3yQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "extend": "^3.0.2",
        "https-proxy-agent": "^7.0.1",
        "is-stream": "^2.0.0",
        "node-fetch": "^2.6.9",
        "uuid": "^9.0.1"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/gcp-metadata": {
      "version": "6.1.1",
      "resolved": "https://registry.npmjs.org/gcp-metadata/-/gcp-metadata-6.1.1.tgz",
      "integrity": "sha512-a4tiq7E0/5fTjxPAaH4jpjkSv/uCaU2p5KC6HVGrvl0cDjA8iBZv4vv1gyzlmK0ZUKqwpOyQMKzZQe3lTit77A==",
      "license": "Apache-2.0",
      "dependencies": {
        "gaxios": "^6.1.1",
        "google-logging-utils": "^0.0.2",
        "json-bigint": "^1.0.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/generator-function": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/generator-function/-/generator-function-2.0.1.tgz",
      "integrity": "sha512-SFdFmIJi+ybC0vjlHN0ZGVGHc3lgE0DxPAT0djjVg+kjOnSqclqmj0KQ7ykTOLP6YxoqOvuAODGdcHJn+43q3g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/gensync": {
      "version": "1.0.0-beta.2",
      "resolved": "https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz",
      "integrity": "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/get-caller-file": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz",
      "integrity": "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==",
      "license": "ISC",
      "engines": {
        "node": "6.* || 8.* || >= 10.*"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-nonce": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-nonce/-/get-nonce-1.0.1.tgz",
      "integrity": "sha512-FJhYRoDaiatfEkUK8HKlicmu/3SGFD51q3itKDGoSTysQJBnfOcxU5GxnhE1E6soB76MbT0MBtnKJuXyAx+96Q==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/globrex": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/globrex/-/globrex-0.1.2.tgz",
      "integrity": "sha512-uHJgbwAMwNFf5mLst7IWLNg14x1CkeqglJb/K3doi4dw6q2IvAAmM/Y81kevy83wP+Sst+nutFTYOGg3d1lsxg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/google-auth-library": {
      "version": "9.15.1",
      "resolved": "https://registry.npmjs.org/google-auth-library/-/google-auth-library-9.15.1.tgz",
      "integrity": "sha512-Jb6Z0+nvECVz+2lzSMt9u98UsoakXxA2HGHMCxh+so3n90XgYWkq5dur19JAJV7ONiJY22yBTyJB1TSkvPq9Ng==",
      "license": "Apache-2.0",
      "dependencies": {
        "base64-js": "^1.3.0",
        "ecdsa-sig-formatter": "^1.0.11",
        "gaxios": "^6.1.1",
        "gcp-metadata": "^6.1.0",
        "gtoken": "^7.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/google-logging-utils": {
      "version": "0.0.2",
      "resolved": "https://registry.npmjs.org/google-logging-utils/-/google-logging-utils-0.0.2.tgz",
      "integrity": "sha512-NEgUnEcBiP5HrPzufUkBzJOD/Sxsco3rLNo1F1TNf7ieU8ryUzBhqba8r756CjLX7rn3fHl6iLEwPYuqpoKgQQ==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gtoken": {
      "version": "7.1.0",
      "resolved": "https://registry.npmjs.org/gtoken/-/gtoken-7.1.0.tgz",
      "integrity": "sha512-pCcEwRi+TKpMlxAQObHDQ56KawURgyAf6jtIY046fJ5tIv3zDe/LEIubckAO8fj6JnAxLdmWkUfNyulQ2iKdEw==",
      "license": "MIT",
      "dependencies": {
        "gaxios": "^6.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/has-property-descriptors": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.2.tgz",
      "integrity": "sha512-55JNKuIW+vq4Ke1BjOTjM2YctQIvCT7GFzHwmfZPGo5wnrgkid0YQtnAleFSqumZm4az3n2BS+erby5ipJdgrg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-define-property": "^1.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-tostringtag": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
      "integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "has-symbols": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hash-base": {
      "version": "3.0.5",
      "resolved": "https://registry.npmjs.org/hash-base/-/hash-base-3.0.5.tgz",
      "integrity": "sha512-vXm0l45VbcHEVlTCzs8M+s0VeYsB2lnlAaThoLKGXr3bE/VWDOelNUnycUPEhKEaXARL2TEFjBOyUiM6+55KBg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.4",
        "safe-buffer": "^5.2.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/hash.js": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/hash.js/-/hash.js-1.1.7.tgz",
      "integrity": "sha512-taOaskGt4z4SOANNseOviYDvjEJinIkRgmp7LbKP2YTTmVxWBl87s/uzK9r+44BclBSp2X7K1hqeNfz9JbBeXA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.3",
        "minimalistic-assert": "^1.0.1"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz",
      "integrity": "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/hmac-drbg": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/hmac-drbg/-/hmac-drbg-1.0.1.tgz",
      "integrity": "sha512-Tti3gMqLdZfhOQY1Mzf/AanLiqh1WTiJgEj26ZuYQ9fbkLomzGchCws4FyrSd4VkpBfiNhaE1On+lOz894jvXg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hash.js": "^1.0.3",
        "minimalistic-assert": "^1.0.0",
        "minimalistic-crypto-utils": "^1.0.1"
      }
    },
    "node_modules/html-to-image": {
      "version": "1.11.13",
      "resolved": "https://registry.npmjs.org/html-to-image/-/html-to-image-1.11.13.tgz",
      "integrity": "sha512-cuOPoI7WApyhBElTTb9oqsawRvZ0rHhaHwghRLlTuffoD1B2aDemlCruLeZrUIIdvG7gs9xeELEPm6PhuASqrg==",
      "license": "MIT"
    },
    "node_modules/http-parser-js": {
      "version": "0.5.10",
      "resolved": "https://registry.npmjs.org/http-parser-js/-/http-parser-js-0.5.10.tgz",
      "integrity": "sha512-Pysuw9XpUq5dVc/2SMHpuTY01RFl8fttgcyunjL7eEMhGM3cI4eOmiCycJDVCo/7O7ClfQD3SaI6ftDzqOXYMA==",
      "license": "MIT"
    },
    "node_modules/https-browserify": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/https-browserify/-/https-browserify-1.0.0.tgz",
      "integrity": "sha512-J+FkSdyD+0mA0N+81tMotaRMfSL9SGi+xpD3T6YApKsc3bGSXJlfXri3VyFOeYkfLRQisDk1W+jIFFKBeUBbBg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/https-proxy-agent": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-7.0.6.tgz",
      "integrity": "sha512-vK9P5/iUfdl95AI+JVyUuIcVtd4ofvtrOr3HNtM2yxC9bnMbEdp3x01OhQNnjb8IJYi38VlTE3mBXwcfvywuSw==",
      "license": "MIT",
      "dependencies": {
        "agent-base": "^7.1.2",
        "debug": "4"
      },
      "engines": {
        "node": ">= 14"
      }
    },
    "node_modules/idb": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/idb/-/idb-7.1.1.tgz",
      "integrity": "sha512-gchesWBzyvGHRO9W8tzUWFDycow5gwjvFKfyV9FF32Y7F50yZMp7mP+T2mJIWFx49zicqyC4uefHM17o6xKIVQ==",
      "license": "ISC"
    },
    "node_modules/ieee754": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz",
      "integrity": "sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "BSD-3-Clause"
    },
    "node_modules/immutable": {
      "version": "5.1.4",
      "resolved": "https://registry.npmjs.org/immutable/-/immutable-5.1.4.tgz",
      "integrity": "sha512-p6u1bG3YSnINT5RQmx/yRZBpenIl30kVxkTLDyHLIMk0gict704Q9n+thfDI7lTRm9vXdDYutVzXhzcThxTnXA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/is-arguments": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/is-arguments/-/is-arguments-1.2.0.tgz",
      "integrity": "sha512-7bVbi0huj/wrIAOzb8U1aszg9kdi3KN/CyU19CTI7tAoZYEZoL9yCDXpbXN+uPsuWnP02cyug1gleqq+TU+YCA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "has-tostringtag": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-callable": {
      "version": "1.2.7",
      "resolved": "https://registry.npmjs.org/is-callable/-/is-callable-1.2.7.tgz",
      "integrity": "sha512-1BC0BVFhS/p0qtw6enp8e+8OD0UrK0oFLztSjNzhcKA3WDuJxxAPXzPuPtKkjEY9UUoEWlX/8fgKeu2S8i9JTA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-core-module": {
      "version": "2.16.1",
      "resolved": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.1.tgz",
      "integrity": "sha512-UfoeMA6fIJ8wTYFEUjelnaGI67v6+N7qXJEvQuIGa99l4xsCruSYOVSQ0uPANn4dAzm8lkYPaKLrrijLq7x23w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-fullwidth-code-point": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
      "integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-generator-function": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/is-generator-function/-/is-generator-function-1.1.2.tgz",
      "integrity": "sha512-upqt1SkGkODW9tsGNG5mtXTXtECizwtS2kA161M+gJPc1xdb/Ax629af6YrTwcOeQHbewrPNlE5Dx7kzvXTizA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.4",
        "generator-function": "^2.0.0",
        "get-proto": "^1.0.1",
        "has-tostringtag": "^1.0.2",
        "safe-regex-test": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-nan": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/is-nan/-/is-nan-1.3.2.tgz",
      "integrity": "sha512-E+zBKpQ2t6MEo1VsonYmluk9NxGrbzpeeLC2xIViuO2EjU2xsXsBPwTr3Ykv9l08UYEVEdWeRZNouaZqF6RN0w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.0",
        "define-properties": "^1.1.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/is-regex": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/is-regex/-/is-regex-1.2.1.tgz",
      "integrity": "sha512-MjYsKHO5O7mCsmRGxWcLWheFqN9DJ/2TmngvjKXihe6efViPqc274+Fx/4fYj/r03+ESvBdTXK0V6tA3rgez1g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "gopd": "^1.2.0",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-stream": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-2.0.1.tgz",
      "integrity": "sha512-hFoiJiTl63nn+kstHGBtewWSKnQLpyb155KHheA1l39uvtO9nWIop1p3udqPcUd/xbF1VLMO4n7OI6p7RbngDg==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/is-typed-array": {
      "version": "1.1.15",
      "resolved": "https://registry.npmjs.org/is-typed-array/-/is-typed-array-1.1.15.tgz",
      "integrity": "sha512-p3EcsicXjit7SaskXHs1hA91QxgTw46Fv6EFKKGS5DRFLD8yKnohjF3hxoju94b/OcMZoQukzpPpBE9uLVKzgQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "which-typed-array": "^1.1.16"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/isarray": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-2.0.5.tgz",
      "integrity": "sha512-xHjhDr3cNBK0BzdUJSPXZntQUx/mwMS5Rw4A7lPJ90XGAO6ISP/ePDNuo0vhqOZU+UD5JoodwCAAoZQd3FeAKw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/isomorphic-timers-promises": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/isomorphic-timers-promises/-/isomorphic-timers-promises-1.0.1.tgz",
      "integrity": "sha512-u4sej9B1LPSxTGKB/HiuzvEQnXH0ECYkSVQU39koSwmFAxhlEAFl9RdTvLv4TOTQUgBS5O3O5fwUxk6byBZ+IQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/js-tokens": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
      "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
      "license": "MIT"
    },
    "node_modules/jsesc": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
      "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jsesc": "bin/jsesc"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/json-bigint": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/json-bigint/-/json-bigint-1.0.0.tgz",
      "integrity": "sha512-SiPv/8VpZuWbvLSMtTDU8hEfrZWg/mH/nV/b4o0CYbSxu1UIQPLdwKOCIyLQX+VIPO5vrLX3i8qtqFyhdPSUSQ==",
      "license": "MIT",
      "dependencies": {
        "bignumber.js": "^9.0.0"
      }
    },
    "node_modules/json5": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/json5/-/json5-2.2.3.tgz",
      "integrity": "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "json5": "lib/cli.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/jwa": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/jwa/-/jwa-2.0.1.tgz",
      "integrity": "sha512-hRF04fqJIP8Abbkq5NKGN0Bbr3JxlQ+qhZufXVr0DvujKy93ZCbXZMHDL4EOtodSbCWxOqR8MS1tXA5hwqCXDg==",
      "license": "MIT",
      "dependencies": {
        "buffer-equal-constant-time": "^1.0.1",
        "ecdsa-sig-formatter": "1.0.11",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/jws": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/jws/-/jws-4.0.0.tgz",
      "integrity": "sha512-KDncfTmOZoOMTFG4mBlG0qUIOlc03fmzH+ru6RgYVZhPkyiy/92Owlt/8UEN+a4TXR1FQetfIpJE8ApdvdVxTg==",
      "license": "MIT",
      "dependencies": {
        "jwa": "^2.0.0",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/locate-path": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz",
      "integrity": "sha512-iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "p-locate": "^5.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/lodash.camelcase": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-4.3.0.tgz",
      "integrity": "sha512-TwuEnCnxbc3rAvhf/LbG7tJUDzhqXyFnv3dtzLOPgCG/hODL7WFnsbwktkD7yUV0RrreP/l1PALq/YSg6VvjlA==",
      "license": "MIT"
    },
    "node_modules/loose-envify": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz",
      "integrity": "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==",
      "license": "MIT",
      "dependencies": {
        "js-tokens": "^3.0.0 || ^4.0.0"
      },
      "bin": {
        "loose-envify": "cli.js"
      }
    },
    "node_modules/lru-cache": {
      "version": "5.1.1",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz",
      "integrity": "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^3.0.2"
      }
    },
    "node_modules/lucide-react": {
      "version": "0.545.0",
      "resolved": "https://registry.npmjs.org/lucide-react/-/lucide-react-0.545.0.tgz",
      "integrity": "sha512-7r1/yUuflQDSt4f1bpn5ZAocyIxcTyVyBBChSVtBKn5M+392cPmI5YJMWOJKk/HUWGm5wg83chlAZtCcGbEZtw==",
      "license": "ISC",
      "peerDependencies": {
        "react": "^16.5.1 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/magic-string": {
      "version": "0.30.19",
      "resolved": "https://registry.npmjs.org/magic-string/-/magic-string-0.30.19.tgz",
      "integrity": "sha512-2N21sPY9Ws53PZvsEpVtNuSW+ScYbQdp4b9qUaL+9QkHUrGFKo56Lg9Emg5s9V/qrtNBmiR01sYhUOwu3H+VOw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.5"
      }
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/md5.js": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/md5.js/-/md5.js-1.3.5.tgz",
      "integrity": "sha512-xitP+WxNPcTTOgnTJcrhM0xvdPepipPSf3I8EIpGKeFLjt3PlJLIDG3u8EX53ZIubkb+5U2+3rELYpEhHhzdkg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hash-base": "^3.0.0",
        "inherits": "^2.0.1",
        "safe-buffer": "^5.1.2"
      }
    },
    "node_modules/micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      },
      "engines": {
        "node": ">=8.6"
      }
    },
    "node_modules/miller-rabin": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/miller-rabin/-/miller-rabin-4.0.1.tgz",
      "integrity": "sha512-115fLhvZVqWwHPbClyntxEVfVDfl9DLLTuJvq3g2O/Oxi8AiNouAHvDSzHS0viUJc+V5vm3eq91Xwqn9dp4jRA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bn.js": "^4.0.0",
        "brorand": "^1.0.1"
      },
      "bin": {
        "miller-rabin": "bin/miller-rabin"
      }
    },
    "node_modules/miller-rabin/node_modules/bn.js": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.12.2.tgz",
      "integrity": "sha512-n4DSx829VRTRByMRGdjQ9iqsN0Bh4OolPsFnaZBLcbi8iXcB+kJ9s7EnRt4wILZNV3kPLHkRVfOc/HvhC3ovDw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/minimalistic-assert": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/minimalistic-assert/-/minimalistic-assert-1.0.1.tgz",
      "integrity": "sha512-UtJcAD4yEaGtjPezWuO9wC4nwUnVH/8/Im3yEHQP4b67cXlD/Qr9hdITCU1xDbSEXg2XKNaP8jsReV7vQd00/A==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/minimalistic-crypto-utils": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/minimalistic-crypto-utils/-/minimalistic-crypto-utils-1.0.1.tgz",
      "integrity": "sha512-JIYlbt6g8i5jKfJ3xz7rF0LXmv2TkDxBLUkiBeZ7bAx4GnnNMr8xFpGnOxn6GhTEHx3SjRrZEoU+j04prX1ktg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/nanoid": {
      "version": "5.1.6",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-5.1.6.tgz",
      "integrity": "sha512-c7+7RQ+dMB5dPwwCp4ee1/iV/q2P6aK1mTZcfr1BTuVlyW9hJYiMPybJCcnBlQtuSmTIWNeazm/zqNoZSSElBg==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.js"
      },
      "engines": {
        "node": "^18 || >=20"
      }
    },
    "node_modules/node-addon-api": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/node-addon-api/-/node-addon-api-7.1.1.tgz",
      "integrity": "sha512-5m3bsyrjFWE1xf7nz7YXdN4udnVtXK6/Yfgn5qnahL6bCkf2yKt4k3nuTKAtT4r3IG8JNR2ncsIMdZuAzJjHQQ==",
      "dev": true,
      "license": "MIT",
      "optional": true
    },
    "node_modules/node-fetch": {
      "version": "2.6.13",
      "resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-2.6.13.tgz",
      "integrity": "sha512-StxNAxh15zr77QvvkmveSQ8uCQ4+v5FkvNTj0OESmiHu+VRi/gXArXtkWMElOsOUNLtUEvI4yS+rdtOHZTwlQA==",
      "license": "MIT",
      "dependencies": {
        "whatwg-url": "^5.0.0"
      },
      "engines": {
        "node": "4.x || >=6.0.0"
      },
      "peerDependencies": {
        "encoding": "^0.1.0"
      },
      "peerDependenciesMeta": {
        "encoding": {
          "optional": true
        }
      }
    },
    "node_modules/node-releases": {
      "version": "2.0.23",
      "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.23.tgz",
      "integrity": "sha512-cCmFDMSm26S6tQSDpBCg/NR8NENrVPhAJSf+XbxBG4rPFaaonlEoE9wHQmun+cls499TQGSb7ZyPBRlzgKfpeg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/node-stdlib-browser": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/node-stdlib-browser/-/node-stdlib-browser-1.3.1.tgz",
      "integrity": "sha512-X75ZN8DCLftGM5iKwoYLA3rjnrAEs97MkzvSd4q2746Tgpg8b8XWiBGiBG4ZpgcAqBgtgPHTiAc8ZMCvZuikDw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "assert": "^2.0.0",
        "browser-resolve": "^2.0.0",
        "browserify-zlib": "^0.2.0",
        "buffer": "^5.7.1",
        "console-browserify": "^1.1.0",
        "constants-browserify": "^1.0.0",
        "create-require": "^1.1.1",
        "crypto-browserify": "^3.12.1",
        "domain-browser": "4.22.0",
        "events": "^3.0.0",
        "https-browserify": "^1.0.0",
        "isomorphic-timers-promises": "^1.0.1",
        "os-browserify": "^0.3.0",
        "path-browserify": "^1.0.1",
        "pkg-dir": "^5.0.0",
        "process": "^0.11.10",
        "punycode": "^1.4.1",
        "querystring-es3": "^0.2.1",
        "readable-stream": "^3.6.0",
        "stream-browserify": "^3.0.0",
        "stream-http": "^3.2.0",
        "string_decoder": "^1.0.0",
        "timers-browserify": "^2.0.4",
        "tty-browserify": "0.0.1",
        "url": "^0.11.4",
        "util": "^0.12.4",
        "vm-browserify": "^1.0.1"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/object-inspect": {
      "version": "1.13.4",
      "resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz",
      "integrity": "sha512-W67iLl4J2EXEGTbfeHCffrjDfitvLANg0UlX3wFUUSTx92KXRFegMHUVgSqE+wvhAbi4WqjGg9czysTV2Epbew==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/object-is": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/object-is/-/object-is-1.1.6.tgz",
      "integrity": "sha512-F8cZ+KfGlSGi09lJT7/Nd6KJZ9ygtvYC0/UYYLI9nmQKLMnydpB9yvbv9K1uSkEu7FU9vYPmVwLg328tX+ot3Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.7",
        "define-properties": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/object-keys": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz",
      "integrity": "sha512-NuAESUOUMrlIXOfHKzD6bpPu3tYt3xvjNdRIQ+FeT0lNb4K8WR70CaDxhuNguS2XG+GjkyMwOzsN5ZktImfhLA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/object.assign": {
      "version": "4.1.7",
      "resolved": "https://registry.npmjs.org/object.assign/-/object.assign-4.1.7.tgz",
      "integrity": "sha512-nK28WOo+QIjBkDduTINE4JkF/UJJKyf2EJxvJKfblDpyg0Q+pkOHNTL0Qwy6NP6FhE/EnzV73BxxqcJaXY9anw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.3",
        "define-properties": "^1.2.1",
        "es-object-atoms": "^1.0.0",
        "has-symbols": "^1.1.0",
        "object-keys": "^1.1.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/os-browserify": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/os-browserify/-/os-browserify-0.3.0.tgz",
      "integrity": "sha512-gjcpUc3clBf9+210TRaDWbf+rZZZEshZ+DlXMRCeAjp0xhTrnQsKHypIy1J3d5hKdUzj69t708EHtU8P6bUn0A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/p-limit": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz",
      "integrity": "sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "yocto-queue": "^0.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/p-locate": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz",
      "integrity": "sha512-LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "p-limit": "^3.0.2"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/pako": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/pako/-/pako-1.0.11.tgz",
      "integrity": "sha512-4hLB8Py4zZce5s4yd9XzopqwVv/yGNhV1Bl8NTmCq1763HeK2+EwVTv+leGeL13Dnh2wfbqowVPXCIO0z4taYw==",
      "dev": true,
      "license": "(MIT AND Zlib)"
    },
    "node_modules/parse-asn1": {
      "version": "5.1.9",
      "resolved": "https://registry.npmjs.org/parse-asn1/-/parse-asn1-5.1.9.tgz",
      "integrity": "sha512-fIYNuZ/HastSb80baGOuPRo1O9cf4baWw5WsAp7dBuUzeTD/BoaG8sVTdlPFksBE2lF21dN+A1AnrpIjSWqHHg==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "asn1.js": "^4.10.1",
        "browserify-aes": "^1.2.0",
        "evp_bytestokey": "^1.0.3",
        "pbkdf2": "^3.1.5",
        "safe-buffer": "^5.2.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/path-browserify": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-browserify/-/path-browserify-1.0.1.tgz",
      "integrity": "sha512-b7uo2UCUOYZcnF/3ID0lulOJi/bafxa1xPe7ZPsammBSpjSWQkjNxlt635YGS2MiR9GjvuXCtz2emr3jbsz98g==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/path-exists": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz",
      "integrity": "sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/path-parse": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
      "integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/pbkdf2": {
      "version": "3.1.5",
      "resolved": "https://registry.npmjs.org/pbkdf2/-/pbkdf2-3.1.5.tgz",
      "integrity": "sha512-Q3CG/cYvCO1ye4QKkuH7EXxs3VC/rI1/trd+qX2+PolbaKG0H+bgcZzrTt96mMyRtejk+JMCiLUn3y29W8qmFQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "create-hash": "^1.2.0",
        "create-hmac": "^1.1.7",
        "ripemd160": "^2.0.3",
        "safe-buffer": "^5.2.1",
        "sha.js": "^2.4.12",
        "to-buffer": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/picocolors": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
      "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/picomatch": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
      "integrity": "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=8.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/pkg-dir": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/pkg-dir/-/pkg-dir-5.0.0.tgz",
      "integrity": "sha512-NPE8TDbzl/3YQYY7CSS228s3g2ollTFnc+Qi3tqmqJp9Vg2ovUpixcJEo2HJScN2Ez+kEaal6y70c0ehqJBJeA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "find-up": "^5.0.0"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/possible-typed-array-names": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/possible-typed-array-names/-/possible-typed-array-names-1.1.0.tgz",
      "integrity": "sha512-/+5VFTchJDoVj3bhoqi6UeymcD00DAwb1nJwamzPvHEszJ4FpF6SNNbUbOS8yI56qHzdV8eK0qEfOSiodkTdxg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/postcss": {
      "version": "8.5.6",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.6.tgz",
      "integrity": "sha512-3Ybi1tAuwAP9s0r1UQ2J4n5Y0G05bJkpUIO0/bI9MhwmD70S5aTWbXGBwxHrelT+XM1k6dM0pk+SwNkpTRN7Pg==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/postcss"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "nanoid": "^3.3.11",
        "picocolors": "^1.1.1",
        "source-map-js": "^1.2.1"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      }
    },
    "node_modules/postcss/node_modules/nanoid": {
      "version": "3.3.11",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.11.tgz",
      "integrity": "sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.cjs"
      },
      "engines": {
        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
      }
    },
    "node_modules/process": {
      "version": "0.11.10",
      "resolved": "https://registry.npmjs.org/process/-/process-0.11.10.tgz",
      "integrity": "sha512-cdGef/drWFoydD1JsMzuFf8100nZl+GT+yacc2bEced5f9Rjk4z+WtFUTBu9PhOi9j/jfmBPu0mMEY4wIdAF8A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.6.0"
      }
    },
    "node_modules/process-nextick-args": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz",
      "integrity": "sha512-3ouUOpQhtgrbOa17J7+uxOTpITYWaGP7/AhoR3+A+/1e9skrzelGi/dXzEYyvbxubEF6Wn2ypscTKiKJFFn1ag==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/protobufjs": {
      "version": "7.5.4",
      "resolved": "https://registry.npmjs.org/protobufjs/-/protobufjs-7.5.4.tgz",
      "integrity": "sha512-CvexbZtbov6jW2eXAvLukXjXUW1TzFaivC46BpWc/3BpcCysb5Vffu+B3XHMm8lVEuy2Mm4XGex8hBSg1yapPg==",
      "hasInstallScript": true,
      "license": "BSD-3-Clause",
      "dependencies": {
        "@protobufjs/aspromise": "^1.1.2",
        "@protobufjs/base64": "^1.1.2",
        "@protobufjs/codegen": "^2.0.4",
        "@protobufjs/eventemitter": "^1.1.0",
        "@protobufjs/fetch": "^1.1.0",
        "@protobufjs/float": "^1.0.2",
        "@protobufjs/inquire": "^1.1.0",
        "@protobufjs/path": "^1.1.2",
        "@protobufjs/pool": "^1.1.0",
        "@protobufjs/utf8": "^1.1.0",
        "@types/node": ">=13.7.0",
        "long": "^5.0.0"
      },
      "engines": {
        "node": ">=12.0.0"
      }
    },
    "node_modules/protobufjs/node_modules/long": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/long/-/long-5.3.2.tgz",
      "integrity": "sha512-mNAgZ1GmyNhD7AuqnTG3/VQ26o760+ZYBPKjPvugO8+nLbYfX6TVpJPseBvopbdY+qpZ/lKUnmEc1LeZYS3QAA==",
      "license": "Apache-2.0"
    },
    "node_modules/public-encrypt": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/public-encrypt/-/public-encrypt-4.0.3.tgz",
      "integrity": "sha512-zVpa8oKZSz5bTMTFClc1fQOnyyEzpl5ozpi1B5YcvBrdohMjH2rfsBtyXcuNuwjsDIXmBYlF2N5FlJYhR29t8Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "bn.js": "^4.1.0",
        "browserify-rsa": "^4.0.0",
        "create-hash": "^1.1.0",
        "parse-asn1": "^5.0.0",
        "randombytes": "^2.0.1",
        "safe-buffer": "^5.1.2"
      }
    },
    "node_modules/public-encrypt/node_modules/bn.js": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.12.2.tgz",
      "integrity": "sha512-n4DSx829VRTRByMRGdjQ9iqsN0Bh4OolPsFnaZBLcbi8iXcB+kJ9s7EnRt4wILZNV3kPLHkRVfOc/HvhC3ovDw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/punycode": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz",
      "integrity": "sha512-jmYNElW7yvO7TV33CjSmvSiE2yco3bV2czu/OzDKdMNVZQWfxCblURLhf+47syQRBntjfLdd/H0egrzIG+oaFQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/qs": {
      "version": "6.14.0",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.14.0.tgz",
      "integrity": "sha512-YWWTjgABSKcvs/nWBi9PycY/JiPJqOD4JA6o9Sej2AtvSGarXxKC3OQSk4pAarbdQlKAh5D4FCQkJNkW+GAn3w==",
      "dev": true,
      "license": "BSD-3-Clause",
      "dependencies": {
        "side-channel": "^1.1.0"
      },
      "engines": {
        "node": ">=0.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/querystring-es3": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/querystring-es3/-/querystring-es3-0.2.1.tgz",
      "integrity": "sha512-773xhDQnZBMFobEiztv8LIl70ch5MSF/jUQVlhwFyBILqq96anmoctVIYz+ZRp0qbCKATTn6ev02M3r7Ga5vqA==",
      "dev": true,
      "engines": {
        "node": ">=0.4.x"
      }
    },
    "node_modules/radix-ui": {
      "version": "1.4.3",
      "resolved": "https://registry.npmjs.org/radix-ui/-/radix-ui-1.4.3.tgz",
      "integrity": "sha512-aWizCQiyeAenIdUbqEpXgRA1ya65P13NKn/W8rWkcN0OPkRDxdBVLWnIEDsS2RpwCK2nobI7oMUSmexzTDyAmA==",
      "license": "MIT",
      "dependencies": {
        "@radix-ui/primitive": "1.1.3",
        "@radix-ui/react-accessible-icon": "1.1.7",
        "@radix-ui/react-accordion": "1.2.12",
        "@radix-ui/react-alert-dialog": "1.1.15",
        "@radix-ui/react-arrow": "1.1.7",
        "@radix-ui/react-aspect-ratio": "1.1.7",
        "@radix-ui/react-avatar": "1.1.10",
        "@radix-ui/react-checkbox": "1.3.3",
        "@radix-ui/react-collapsible": "1.1.12",
        "@radix-ui/react-collection": "1.1.7",
        "@radix-ui/react-compose-refs": "1.1.2",
        "@radix-ui/react-context": "1.1.2",
        "@radix-ui/react-context-menu": "2.2.16",
        "@radix-ui/react-dialog": "1.1.15",
        "@radix-ui/react-direction": "1.1.1",
        "@radix-ui/react-dismissable-layer": "1.1.11",
        "@radix-ui/react-dropdown-menu": "2.1.16",
        "@radix-ui/react-focus-guards": "1.1.3",
        "@radix-ui/react-focus-scope": "1.1.7",
        "@radix-ui/react-form": "0.1.8",
        "@radix-ui/react-hover-card": "1.1.15",
        "@radix-ui/react-label": "2.1.7",
        "@radix-ui/react-menu": "2.1.16",
        "@radix-ui/react-menubar": "1.1.16",
        "@radix-ui/react-navigation-menu": "1.2.14",
        "@radix-ui/react-one-time-password-field": "0.1.8",
        "@radix-ui/react-password-toggle-field": "0.1.3",
        "@radix-ui/react-popover": "1.1.15",
        "@radix-ui/react-popper": "1.2.8",
        "@radix-ui/react-portal": "1.1.9",
        "@radix-ui/react-presence": "1.1.5",
        "@radix-ui/react-primitive": "2.1.3",
        "@radix-ui/react-progress": "1.1.7",
        "@radix-ui/react-radio-group": "1.3.8",
        "@radix-ui/react-roving-focus": "1.1.11",
        "@radix-ui/react-scroll-area": "1.2.10",
        "@radix-ui/react-select": "2.2.6",
        "@radix-ui/react-separator": "1.1.7",
        "@radix-ui/react-slider": "1.3.6",
        "@radix-ui/react-slot": "1.2.3",
        "@radix-ui/react-switch": "1.2.6",
        "@radix-ui/react-tabs": "1.1.13",
        "@radix-ui/react-toast": "1.2.15",
        "@radix-ui/react-toggle": "1.1.10",
        "@radix-ui/react-toggle-group": "1.1.11",
        "@radix-ui/react-toolbar": "1.1.11",
        "@radix-ui/react-tooltip": "1.2.8",
        "@radix-ui/react-use-callback-ref": "1.1.1",
        "@radix-ui/react-use-controllable-state": "1.2.2",
        "@radix-ui/react-use-effect-event": "0.0.2",
        "@radix-ui/react-use-escape-keydown": "1.1.1",
        "@radix-ui/react-use-is-hydrated": "0.1.0",
        "@radix-ui/react-use-layout-effect": "1.1.1",
        "@radix-ui/react-use-size": "1.1.1",
        "@radix-ui/react-visually-hidden": "1.2.3"
      },
      "peerDependencies": {
        "@types/react": "*",
        "@types/react-dom": "*",
        "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
        "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "@types/react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/randombytes": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/randombytes/-/randombytes-2.1.0.tgz",
      "integrity": "sha512-vYl3iOX+4CKUWuxGi9Ukhie6fsqXqS9FE2Zaic4tNFD2N2QQaXOMFbuKK4QmDHC0JO6B1Zp41J0LpT0oR68amQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "^5.1.0"
      }
    },
    "node_modules/randomfill": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/randomfill/-/randomfill-1.0.4.tgz",
      "integrity": "sha512-87lcbR8+MhcWcUiQ+9e+Rwx8MyR2P7qnt15ynUlbm3TU/fjbgz4GsvfSUDTemtCCtVCqb4ZcEFlyPNTh9bBTLw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "randombytes": "^2.0.5",
        "safe-buffer": "^5.1.0"
      }
    },
    "node_modules/react": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
      "integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-dom": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
      "integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0",
        "scheduler": "^0.23.2"
      },
      "peerDependencies": {
        "react": "^18.3.1"
      }
    },
    "node_modules/react-refresh": {
      "version": "0.17.0",
      "resolved": "https://registry.npmjs.org/react-refresh/-/react-refresh-0.17.0.tgz",
      "integrity": "sha512-z6F7K9bV85EfseRCp2bzrpyQ0Gkw1uLoCel9XBVWPg/TjRj94SkJzUTGfOa4bs7iJvBWtQG0Wq7wnI0syw3EBQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-remove-scroll": {
      "version": "2.7.1",
      "resolved": "https://registry.npmjs.org/react-remove-scroll/-/react-remove-scroll-2.7.1.tgz",
      "integrity": "sha512-HpMh8+oahmIdOuS5aFKKY6Pyog+FNaZV/XyJOq7b4YFwsFHe5yYfdbIalI4k3vU2nSDql7YskmUseHsRrJqIPA==",
      "license": "MIT",
      "dependencies": {
        "react-remove-scroll-bar": "^2.3.7",
        "react-style-singleton": "^2.2.3",
        "tslib": "^2.1.0",
        "use-callback-ref": "^1.3.3",
        "use-sidecar": "^1.1.3"
      },
      "engines": {
        "node": ">=10"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/react-remove-scroll-bar": {
      "version": "2.3.8",
      "resolved": "https://registry.npmjs.org/react-remove-scroll-bar/-/react-remove-scroll-bar-2.3.8.tgz",
      "integrity": "sha512-9r+yi9+mgU33AKcj6IbT9oRCO78WriSj6t/cF8DWBZJ9aOGPOTEDvdUDz1FwKim7QXWwmHqtdHnRJfhAxEG46Q==",
      "license": "MIT",
      "dependencies": {
        "react-style-singleton": "^2.2.2",
        "tslib": "^2.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/react-style-singleton": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/react-style-singleton/-/react-style-singleton-2.2.3.tgz",
      "integrity": "sha512-b6jSvxvVnyptAiLjbkWLE/lOnR4lfTtDAl+eUC7RZy+QQWc6wRzIV2CE6xBuMmDxc2qIihtDCZD5NPOFl7fRBQ==",
      "license": "MIT",
      "dependencies": {
        "get-nonce": "^1.0.0",
        "tslib": "^2.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/readable-stream": {
      "version": "3.6.2",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz",
      "integrity": "sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.3",
        "string_decoder": "^1.1.1",
        "util-deprecate": "^1.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/readdirp": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-4.1.2.tgz",
      "integrity": "sha512-GDhwkLfywWL2s6vEjyhri+eXmfH6j1L7JE27WhqLeYzoh/A3DBaYGEj2H/HFZCn/kMfim73FXxEJTw06WtxQwg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 14.18.0"
      },
      "funding": {
        "type": "individual",
        "url": "https://paulmillr.com/funding/"
      }
    },
    "node_modules/require-directory": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz",
      "integrity": "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/resolve": {
      "version": "1.22.11",
      "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.22.11.tgz",
      "integrity": "sha512-RfqAvLnMl313r7c9oclB1HhUEAezcpLjz95wFH4LVuhk9JF/r22qmVP9AMmOU4vMX7Q8pN8jwNg/CSpdFnMjTQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-core-module": "^2.16.1",
        "path-parse": "^1.0.7",
        "supports-preserve-symlinks-flag": "^1.0.0"
      },
      "bin": {
        "resolve": "bin/resolve"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/ripemd160": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/ripemd160/-/ripemd160-2.0.3.tgz",
      "integrity": "sha512-5Di9UC0+8h1L6ZD2d7awM7E/T4uA1fJRlx6zk/NvdCCVEoAnFqvHmCuNeIKoCeIixBX/q8uM+6ycDvF8woqosA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hash-base": "^3.1.2",
        "inherits": "^2.0.4"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/ripemd160/node_modules/hash-base": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/hash-base/-/hash-base-3.1.2.tgz",
      "integrity": "sha512-Bb33KbowVTIj5s7Ked1OsqHUeCpz//tPwR+E2zJgJKo9Z5XolZ9b6bdUgjmYlwnWhoOQKoTd1TYToZGn5mAYOg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.4",
        "readable-stream": "^2.3.8",
        "safe-buffer": "^5.2.1",
        "to-buffer": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/ripemd160/node_modules/isarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
      "integrity": "sha512-VLghIWNM6ELQzo7zwmcg0NmTVyWKYjvIeM83yjp0wRDTmUnrM678fQbcKBo6n2CJEF0szoG//ytg+TKla89ALQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/ripemd160/node_modules/readable-stream": {
      "version": "2.3.8",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz",
      "integrity": "sha512-8p0AUk4XODgIewSi0l8Epjs+EVnWiK7NoDIEGU0HhE7+ZyY8D1IMY7odu5lRrFXGg71L15KG8QrPmum45RTtdA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "core-util-is": "~1.0.0",
        "inherits": "~2.0.3",
        "isarray": "~1.0.0",
        "process-nextick-args": "~2.0.0",
        "safe-buffer": "~5.1.1",
        "string_decoder": "~1.1.1",
        "util-deprecate": "~1.0.1"
      }
    },
    "node_modules/ripemd160/node_modules/readable-stream/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/ripemd160/node_modules/string_decoder": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz",
      "integrity": "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "~5.1.0"
      }
    },
    "node_modules/ripemd160/node_modules/string_decoder/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/rollup": {
      "version": "3.29.5",
      "resolved": "https://registry.npmjs.org/rollup/-/rollup-3.29.5.tgz",
      "integrity": "sha512-GVsDdsbJzzy4S/v3dqWPJ7EfvZJfCHiDqe80IyrF59LYuP+e6U1LJoUqeuqRbwAWoMNoXivMNeNAOf5E22VA1w==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "rollup": "dist/bin/rollup"
      },
      "engines": {
        "node": ">=14.18.0",
        "npm": ">=8.0.0"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/safe-buffer": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
      "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/safe-regex-test": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/safe-regex-test/-/safe-regex-test-1.1.0.tgz",
      "integrity": "sha512-x/+Cz4YrimQxQccJf5mKEbIa1NzeCRNI5Ecl/ekmlYaampdNLPalVyIcCZNNH3MvmqBugV5TMYZXv0ljslUlaw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "is-regex": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/sass": {
      "version": "1.93.2",
      "resolved": "https://registry.npmjs.org/sass/-/sass-1.93.2.tgz",
      "integrity": "sha512-t+YPtOQHpGW1QWsh1CHQ5cPIr9lbbGZLZnbihP/D/qZj/yuV68m8qarcV17nvkOX81BCrvzAlq2klCQFZghyTg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "chokidar": "^4.0.0",
        "immutable": "^5.0.2",
        "source-map-js": ">=0.6.2 <2.0.0"
      },
      "bin": {
        "sass": "sass.js"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "optionalDependencies": {
        "@parcel/watcher": "^2.4.1"
      }
    },
    "node_modules/scheduler": {
      "version": "0.23.2",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
      "integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0"
      }
    },
    "node_modules/semver": {
      "version": "6.3.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.1.tgz",
      "integrity": "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/set-function-length": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/set-function-length/-/set-function-length-1.2.2.tgz",
      "integrity": "sha512-pgRc4hJ4/sNjWCSS9AmnS40x3bNMDTknHgL5UaMBTMyJnU90EgWh1Rz+MC9eFu4BuN/UwZjKQuY/1v3rM7HMfg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "define-data-property": "^1.1.4",
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2",
        "get-intrinsic": "^1.2.4",
        "gopd": "^1.0.1",
        "has-property-descriptors": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/setimmediate": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz",
      "integrity": "sha512-MATJdZp8sLqDl/68LfQmbP8zKPLQNV6BIZoIgrscFDQ+RsvK/BxeDQOgyxKKoh0y/8h3BqVFnCqQ/gd+reiIXA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/sha.js": {
      "version": "2.4.12",
      "resolved": "https://registry.npmjs.org/sha.js/-/sha.js-2.4.12.tgz",
      "integrity": "sha512-8LzC5+bvI45BjpfXU8V5fdU2mfeKiQe1D1gIMn7XUlF3OTUrpdJpPPH4EMAnF0DsHHdSZqCdSss5qCmJKuiO3w==",
      "dev": true,
      "license": "(MIT AND BSD-3-Clause)",
      "dependencies": {
        "inherits": "^2.0.4",
        "safe-buffer": "^5.2.1",
        "to-buffer": "^1.2.0"
      },
      "bin": {
        "sha.js": "bin.js"
      },
      "engines": {
        "node": ">= 0.10"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz",
      "integrity": "sha512-ZX99e6tRweoUXqR+VBrslhda51Nh5MTQwou5tnUDgbtyM0dBgmhEDtWGP/xbKn6hqfPRHujUNwz5fy/wbbhnpw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3",
        "side-channel-list": "^1.0.0",
        "side-channel-map": "^1.0.1",
        "side-channel-weakmap": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-list": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.0.tgz",
      "integrity": "sha512-FCLHtRD/gnpCiCHEiJLOwdmFP+wzCmDEkc9y7NsYxeF4u7Btsn1ZuwgwJGxImImHicJArLP4R0yX4c2KCrMrTA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-map": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz",
      "integrity": "sha512-VCjCNfgMsby3tTdo02nbjtM/ewra6jPHmpThenkTYh8pG9ucZ/1P8So4u4FGBek/BjpOVsDCMoLA/iuBKIFXRA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-weakmap": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz",
      "integrity": "sha512-WPS/HvHQTYnHisLo9McqBHOJk2FkHO/tlpvldyrnem4aeQp4hai3gythswg6p01oSoTl58rcpiFAjF2br2Ak2A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3",
        "side-channel-map": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/source-map-js": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
      "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
      "dev": true,
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/stream-browserify": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/stream-browserify/-/stream-browserify-3.0.0.tgz",
      "integrity": "sha512-H73RAHsVBapbim0tU2JwwOiXUj+fikfiaoYAKHF3VJfA0pe2BCzkhAHBlLG6REzE+2WNZcxOXjK7lkso+9euLA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "~2.0.4",
        "readable-stream": "^3.5.0"
      }
    },
    "node_modules/stream-http": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/stream-http/-/stream-http-3.2.0.tgz",
      "integrity": "sha512-Oq1bLqisTyK3TSCXpPbT4sdeYNdmyZJv1LxpEm2vu1ZhK89kSE5YXwZc3cWk0MagGaKriBh9mCFbVGtO+vY29A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "builtin-status-codes": "^3.0.0",
        "inherits": "^2.0.4",
        "readable-stream": "^3.6.0",
        "xtend": "^4.0.2"
      }
    },
    "node_modules/string_decoder": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz",
      "integrity": "sha512-hkRX8U1WjJFd8LsDJ2yQ/wWWxaopEsABU1XfkM8A+j0+85JAGppt16cr1Whg6KIbb4okU6Mql6BOj+uup/wKeA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "~5.2.0"
      }
    },
    "node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/supports-preserve-symlinks-flag": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
      "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/timers-browserify": {
      "version": "2.0.12",
      "resolved": "https://registry.npmjs.org/timers-browserify/-/timers-browserify-2.0.12.tgz",
      "integrity": "sha512-9phl76Cqm6FhSX9Xe1ZUAMLtm1BLkKj2Qd5ApyWkXzsMRaA7dgr81kf4wJmQf/hAvg8EEyJxDo3du/0KlhPiKQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "setimmediate": "^1.0.4"
      },
      "engines": {
        "node": ">=0.6.0"
      }
    },
    "node_modules/to-buffer": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/to-buffer/-/to-buffer-1.2.2.tgz",
      "integrity": "sha512-db0E3UJjcFhpDhAF4tLo03oli3pwl3dbnzXOUIlRKrp+ldk/VUxzpWYZENsw2SZiuBjHAk7DfB0VU7NKdpb6sw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "isarray": "^2.0.5",
        "safe-buffer": "^5.2.1",
        "typed-array-buffer": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    },
    "node_modules/tr46": {
      "version": "0.0.3",
      "resolved": "https://registry.npmjs.org/tr46/-/tr46-0.0.3.tgz",
      "integrity": "sha512-N3WMsuqV66lT30CrXNbEjx4GEwlow3v6rr4mCcv6prnfwhS01rkgyFdjPNBYd9br7LpXV1+Emh01fHnq2Gdgrw==",
      "license": "MIT"
    },
    "node_modules/tsconfck": {
      "version": "3.1.6",
      "resolved": "https://registry.npmjs.org/tsconfck/-/tsconfck-3.1.6.tgz",
      "integrity": "sha512-ks6Vjr/jEw0P1gmOVwutM3B7fWxoWBL2KRDb1JfqGVawBmO5UsvmWOQFGHBPl5yxYz4eERr19E6L7NMv+Fej4w==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "tsconfck": "bin/tsconfck.js"
      },
      "engines": {
        "node": "^18 || >=20"
      },
      "peerDependencies": {
        "typescript": "^5.0.0"
      },
      "peerDependenciesMeta": {
        "typescript": {
          "optional": true
        }
      }
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "license": "0BSD"
    },
    "node_modules/tty-browserify": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/tty-browserify/-/tty-browserify-0.0.1.tgz",
      "integrity": "sha512-C3TaO7K81YvjCgQH9Q1S3R3P3BtN3RIM8n+OvX4il1K1zgE8ZhI0op7kClgkxtutIE8hQrcrHBXvIheqKUUCxw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/typed-array-buffer": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/typed-array-buffer/-/typed-array-buffer-1.0.3.tgz",
      "integrity": "sha512-nAYYwfY3qnzX30IkA6AQZjVbtK6duGontcQm1WSG1MD94YLqK0515GNApXkoxKOWMusVssAHWLh9SeaoefYFGw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "es-errors": "^1.3.0",
        "is-typed-array": "^1.1.14"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/typescript": {
      "version": "5.9.3",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
      "integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/undici-types": {
      "version": "7.14.0",
      "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-7.14.0.tgz",
      "integrity": "sha512-QQiYxHuyZ9gQUIrmPo3IA+hUl4KYk8uSA7cHrcKd/l3p1OTpZcM0Tbp9x7FAtXdAYhlasd60ncPpgu6ihG6TOA==",
      "license": "MIT"
    },
    "node_modules/update-browserslist-db": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.1.3.tgz",
      "integrity": "sha512-UxhIZQ+QInVdunkDAaiazvvT/+fXL5Osr0JZlJulepYu6Jd7qJtDZjlur0emRlT71EN3ScPoE7gvsuIKKNavKw==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "escalade": "^3.2.0",
        "picocolors": "^1.1.1"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/url": {
      "version": "0.11.4",
      "resolved": "https://registry.npmjs.org/url/-/url-0.11.4.tgz",
      "integrity": "sha512-oCwdVC7mTuWiPyjLUz/COz5TLk6wgp0RCsN+wHZ2Ekneac9w8uuV0njcbbie2ME+Vs+d6duwmYuR3HgQXs1fOg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "punycode": "^1.4.1",
        "qs": "^6.12.3"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/use-callback-ref": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/use-callback-ref/-/use-callback-ref-1.3.3.tgz",
      "integrity": "sha512-jQL3lRnocaFtu3V00JToYz/4QkNWswxijDaCVNZRiRTO3HQDLsdu1ZtmIUvV4yPp+rvWm5j0y0TG/S61cuijTg==",
      "license": "MIT",
      "dependencies": {
        "tslib": "^2.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/use-sidecar": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/use-sidecar/-/use-sidecar-1.1.3.tgz",
      "integrity": "sha512-Fedw0aZvkhynoPYlA5WXrMCAMm+nSWdZt6lzJQ7Ok8S6Q+VsHmHpRWndVRJ8Be0ZbkfPc5LRYH+5XrzXcEeLRQ==",
      "license": "MIT",
      "dependencies": {
        "detect-node-es": "^1.1.0",
        "tslib": "^2.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "peerDependencies": {
        "@types/react": "*",
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        }
      }
    },
    "node_modules/use-sync-external-store": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/use-sync-external-store/-/use-sync-external-store-1.6.0.tgz",
      "integrity": "sha512-Pp6GSwGP/NrPIrxVFAIkOQeyw8lFenOHijQWkUTrDvrF4ALqylP2C/KCkeS9dpUM3KvYRQhna5vt7IL95+ZQ9w==",
      "license": "MIT",
      "peerDependencies": {
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/util": {
      "version": "0.12.5",
      "resolved": "https://registry.npmjs.org/util/-/util-0.12.5.tgz",
      "integrity": "sha512-kZf/K6hEIrWHI6XqOFUiiMa+79wE/D8Q+NCNAWclkyg3b4d2k7s0QGepNjiABc+aR3N1PAyHL7p6UcLY6LmrnA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.3",
        "is-arguments": "^1.0.4",
        "is-generator-function": "^1.0.7",
        "is-typed-array": "^1.1.3",
        "which-typed-array": "^1.1.2"
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/uuid": {
      "version": "9.0.1",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-9.0.1.tgz",
      "integrity": "sha512-b+1eJOlsR9K8HJpow9Ok3fiWOWSIcIzXodvv0rQjVoOVNpWMpxf1wZNpt4y9h10odCNrqnYp1OBzRktckBe3sA==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "license": "MIT",
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    },
    "node_modules/vite": {
      "version": "4.5.14",
      "resolved": "https://registry.npmjs.org/vite/-/vite-4.5.14.tgz",
      "integrity": "sha512-+v57oAaoYNnO3hIu5Z/tJRZjq5aHM2zDve9YZ8HngVHbhk66RStobhb1sqPMIPEleV6cNKYK4eGrAbE9Ulbl2g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "esbuild": "^0.18.10",
        "postcss": "^8.4.27",
        "rollup": "^3.27.1"
      },
      "bin": {
        "vite": "bin/vite.js"
      },
      "engines": {
        "node": "^14.18.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/vitejs/vite?sponsor=1"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.2"
      },
      "peerDependencies": {
        "@types/node": ">= 14",
        "less": "*",
        "lightningcss": "^1.21.0",
        "sass": "*",
        "stylus": "*",
        "sugarss": "*",
        "terser": "^5.4.0"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        },
        "less": {
          "optional": true
        },
        "lightningcss": {
          "optional": true
        },
        "sass": {
          "optional": true
        },
        "stylus": {
          "optional": true
        },
        "sugarss": {
          "optional": true
        },
        "terser": {
          "optional": true
        }
      }
    },
    "node_modules/vite-plugin-node-polyfills": {
      "version": "0.24.0",
      "resolved": "https://registry.npmjs.org/vite-plugin-node-polyfills/-/vite-plugin-node-polyfills-0.24.0.tgz",
      "integrity": "sha512-GA9QKLH+vIM8NPaGA+o2t8PDfFUl32J8rUp1zQfMKVJQiNkOX4unE51tR6ppl6iKw5yOrDAdSH7r/UIFLCVhLw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rollup/plugin-inject": "^5.0.5",
        "node-stdlib-browser": "^1.2.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/davidmyersdev"
      },
      "peerDependencies": {
        "vite": "^2.0.0 || ^3.0.0 || ^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0"
      }
    },
    "node_modules/vite-tsconfig-paths": {
      "version": "5.1.4",
      "resolved": "https://registry.npmjs.org/vite-tsconfig-paths/-/vite-tsconfig-paths-5.1.4.tgz",
      "integrity": "sha512-cYj0LRuLV2c2sMqhqhGpaO3LretdtMn/BVX4cPLanIZuwwrkVl+lK84E/miEXkCHWXuq65rhNN4rXsBcOB3S4w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "debug": "^4.1.1",
        "globrex": "^0.1.2",
        "tsconfck": "^3.0.3"
      },
      "peerDependencies": {
        "vite": "*"
      },
      "peerDependenciesMeta": {
        "vite": {
          "optional": true
        }
      }
    },
    "node_modules/vm-browserify": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vm-browserify/-/vm-browserify-1.1.2.tgz",
      "integrity": "sha512-2ham8XPWTONajOR0ohOKOHXkm3+gaBmGut3SRuu75xLd/RRaY6vqgh8NBYYk7+RW3u5AtzPQZG8F10LHkl0lAQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/web-vitals": {
      "version": "4.2.4",
      "resolved": "https://registry.npmjs.org/web-vitals/-/web-vitals-4.2.4.tgz",
      "integrity": "sha512-r4DIlprAGwJ7YM11VZp4R884m0Vmgr6EAKe3P+kO0PPj3Unqyvv59rczf6UiGcb9Z8QxZVcqKNwv/g0WNdWwsw==",
      "license": "Apache-2.0"
    },
    "node_modules/webidl-conversions": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-3.0.1.tgz",
      "integrity": "sha512-2JAn3z8AR6rjK8Sm8orRC0h/bcl/DqL7tRPdGZ4I1CjdF+EaMLmYxBHyXuKL849eucPFhvBoxMsflfOb8kxaeQ==",
      "license": "BSD-2-Clause"
    },
    "node_modules/websocket-driver": {
      "version": "0.7.4",
      "resolved": "https://registry.npmjs.org/websocket-driver/-/websocket-driver-0.7.4.tgz",
      "integrity": "sha512-b17KeDIQVjvb0ssuSDF2cYXSg2iztliJ4B9WdsuB6J952qCPKmnVq4DyW5motImXHDC1cBT/1UezrJVsKw5zjg==",
      "license": "Apache-2.0",
      "dependencies": {
        "http-parser-js": ">=0.5.1",
        "safe-buffer": ">=5.1.0",
        "websocket-extensions": ">=0.1.1"
      },
      "engines": {
        "node": ">=0.8.0"
      }
    },
    "node_modules/websocket-extensions": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/websocket-extensions/-/websocket-extensions-0.1.4.tgz",
      "integrity": "sha512-OqedPIGOfsDlo31UNwYbCFMSaO9m9G/0faIHj5/dZFDMFqPTcx6UwqyOy3COEaEOg/9VsGIpdqn62W5KhoKSpg==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=0.8.0"
      }
    },
    "node_modules/whatwg-url": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/whatwg-url/-/whatwg-url-5.0.0.tgz",
      "integrity": "sha512-saE57nupxk6v3HY35+jzBwYa0rKSy0XR8JSxZPwgLr7ys0IBzhGviA1/TUGJLmSVqs8pb9AnvICXEuOHLprYTw==",
      "license": "MIT",
      "dependencies": {
        "tr46": "~0.0.3",
        "webidl-conversions": "^3.0.0"
      }
    },
    "node_modules/which-typed-array": {
      "version": "1.1.19",
      "resolved": "https://registry.npmjs.org/which-typed-array/-/which-typed-array-1.1.19.tgz",
      "integrity": "sha512-rEvr90Bck4WZt9HHFC4DJMsjvu7x+r6bImz0/BrbWb7A2djJ8hnZMrWnHo9F8ssv0OMErasDhftrfROTyqSDrw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "available-typed-arrays": "^1.0.7",
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.4",
        "for-each": "^0.3.5",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-tostringtag": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/wrap-ansi": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
      "integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^4.0.0",
        "string-width": "^4.1.0",
        "strip-ansi": "^6.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
      }
    },
    "node_modules/ws": {
      "version": "8.18.3",
      "resolved": "https://registry.npmjs.org/ws/-/ws-8.18.3.tgz",
      "integrity": "sha512-PEIGCY5tSlUt50cqyMXfCzX+oOPqN0vuGqWzbcJ2xvnkzkq46oOpz7dQaTDBdfICb4N14+GARUDw2XV2N4tvzg==",
      "license": "MIT",
      "engines": {
        "node": ">=10.0.0"
      },
      "peerDependencies": {
        "bufferutil": "^4.0.1",
        "utf-8-validate": ">=5.0.2"
      },
      "peerDependenciesMeta": {
        "bufferutil": {
          "optional": true
        },
        "utf-8-validate": {
          "optional": true
        }
      }
    },
    "node_modules/xtend": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz",
      "integrity": "sha512-LKYU1iAXJXUgAXn9URjiu+MWhyUXHsvfp7mcuYm9dSUKK0/CjtrUwFAxD82/mCWbtLsGjFIad0wIsod4zrTAEQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.4"
      }
    },
    "node_modules/y18n": {
      "version": "5.0.8",
      "resolved": "https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz",
      "integrity": "sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==",
      "license": "ISC",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/yallist": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz",
      "integrity": "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/yocto-queue": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz",
      "integrity": "sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/zod": {
      "version": "4.1.12",
      "resolved": "https://registry.npmjs.org/zod/-/zod-4.1.12.tgz",
      "integrity": "sha512-JInaHOamG8pt5+Ey8kGmdcAcg3OL9reK8ltczgHTAwNhMys/6ThXHityHxVV2p3fkw/c+MAvBHFVYHFZDmjMCQ==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/colinhacks"
      }
    },
    "node_modules/zustand": {
      "version": "4.5.7",
      "resolved": "https://registry.npmjs.org/zustand/-/zustand-4.5.7.tgz",
      "integrity": "sha512-CHOUy7mu3lbD6o6LJLfllpjkzhHXSBlX8B9+qPddUsIfeF5S/UZ5q0kmCsnRqT1UHFQZchNFDDzMbQsuesHWlw==",
      "license": "MIT",
      "dependencies": {
        "use-sync-external-store": "^1.2.2"
      },
      "engines": {
        "node": ">=12.7.0"
      },
      "peerDependencies": {
        "@types/react": ">=16.8",
        "immer": ">=9.0.6",
        "react": ">=16.8"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "immer": {
          "optional": true
        },
        "react": {
          "optional": true
        }
      }
    }
  }
}

```

## File: package.json
```
{
  "name": "atq-experiment",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "deploy": "npm run build && firebase hosting:channel:deploy -e 30d ss",
    "preview": "vite preview"
  },
  "dependencies": {
    "@google/genai": "^1.24.0",
    "@radix-ui/themes": "^3.2.1",
    "@xyflow/react": "^12.8.6",
    "classnames": "^2.5.1",
    "esbuild-wasm": "^0.25.11",
    "firebase": "^12.4.0",
    "html-to-image": "^1.11.13",
    "lucide-react": "^0.545.0",
    "nanoid": "^5.1.6",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "zod": "^4.1.12"
  },
  "devDependencies": {
    "@paper-design/shaders-react": "^0.0.71",
    "@types/react": "^18.2.15",
    "@types/react-dom": "^18.2.7",
    "@vitejs/plugin-react": "^4.0.3",
    "sass": "^1.93.2",
    "typescript": "^5.0.2",
    "vite": "^4.4.5",
    "vite-plugin-node-polyfills": "^0.24.0",
    "vite-tsconfig-paths": "^5.1.4"
  }
}
```

## File: README.md
```
# @Q Experiment

A prototype-level platform for on-the-fly team collaboration tools

👉 [**Read the article**](https://labs.google/code/experiments/atq)

## Building locally

1. Create a Firebase project with Realtime Database and Auth enabled

2. Make a `.env` file at the root, as a copy of [`.env.example`](./.env.example), filling out the necessary field(s)

3. Install dependencies and start the Vite server:
    ```bash
    $ npm install
    $ npm run dev
    ```

## Technical components

- **Realtime multiplayer** - powered by [Firebase Realtime Database](https://firebase.google.com/docs/database) and Auth.
- **On-the-fly app generation** - simplified coding agent powered by Gemini, along with an in-browser runtime powered by [`esbuild-wasm`](https://www.npmjs.com/package/esbuild-wasm) and inspired by [JSNotebook](https://github.com/tschoffelen/jsnotebook).

```

## File: tsconfig.json
```
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"],
  "exclude": ["**/*.example.tsx"],
  "references": [{ "path": "./tsconfig.node.json" }]
}

```

## File: tsconfig.node.json
```
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}

```

## File: vite.config.ts
```
import react from "@vitejs/plugin-react";
import path from "path";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";
import { nodePolyfills } from 'vite-plugin-node-polyfills'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), tsconfigPaths(), nodePolyfills()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
});

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_AtQ-Experiment_223720



================================================
FILE: firebase.json
================================================
{
  "hosting": {
    "site": "threeplabs",
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}


================================================
FILE: package-lock.json
================================================
{
  "name": "vite-project",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "vite-project",
      "version": "0.0.0",
      "dependencies": {
        "@google/genai": "^1.24.0",
        "@radix-ui/themes": "^3.2.1",
        "@xyflow/react": "^12.8.6",
        "classnames": "^2.5.1",
        "esbuild-wasm": "^0.25.11",
        "firebase": "^12.4.0",
        "html-to-image": "^1.11.13",
        "lucide-react": "^0.545.0",
        "nanoid": "^5.1.6",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "zod": "^4.1.12"
      },
      "devDependencies": {
        "@paper-design/shaders-react": "^0.0.71",
        "@types/react": "^18.2.15",
        "@types/react-dom": "^18.2.7",
        "@vitejs/plugin-react": "^4.0.3",
        "sass": "^1.93.2",
        "typescript": "^5.0.2",
        "vite": "^4.4.5",
        "vite-plugin-node-polyfills": "^0.24.0",
        "vite-tsconfig-paths": "^5.1.4"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.27.1.tgz",
      "integrity": "sha512-cjQ7ZlQ0Mv3b47hABuTevyTuYN4i+loJKGeV9flcCgIK37cCXRh+L1bd3iBHlynerhQ7BhCkn2BPbQUL+rGqFg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.27.1",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.28.4.tgz",
      "integrity": "sha512-YsmSKC29MJwf0gF8Rjjrg5LQCmyh+j/nD8/eP7f+BeoQTKYqs9RoWbjGOdy0+1Ekr68RJZMUOPVQaQisnIo4Rw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.28.4.tgz",
      "integrity": "sha512-2BCOP7TN8M+gVDj7/ht3hsaO/B/n5oDbiAyyvnRlNOs+u1o+JWNYTQrmpuNp1/Wq2gcFrI01JAW+paEKDMx/CA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.3",
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-module-transforms": "^7.28.3",
        "@babel/helpers": "^7.28.4",
        "@babel/parser": "^7.28.4",
        "@babel/template": "^7.27.2",
        "@babel/traverse": "^7.28.4",
        "@babel/types": "^7.28.4",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.28.3.tgz",
      "integrity": "sha512-3lSpxGgvnmZznmBkCRnVREPUFJv2wrv9iAoFDvADJc0ypmdOxdUtcLeBgBJ6zE0PMeTKnxeQzyk0xTBq4Ep7zw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.3",
        "@babel/types": "^7.28.2",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.27.2",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.27.2.tgz",
      "integrity": "sha512-2+1thGUUWWjLTYTHZWK1n8Yga0ijBz1XAhUXcKy81rd5g6yh7hGqMp45v7cadSbEHc9G3OTv45SyneRN3ps4DQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.27.2",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.27.1.tgz",
      "integrity": "sha512-0gSFWUPNXNopqtIPQvlD5WgXYI5GY2kP2cCvoT8kczjbfcfuIljTbcWrulD1CIPIX2gt1wghbDy08yE1p+/r3w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babe

================================================
FILE: package.json
================================================
{
  "name": "atq-experiment",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "deploy": "npm run build && firebase hosting:channel:deploy -e 30d ss",
    "preview": "vite preview"
  },
  "dependencies": {
    "@google/genai": "^1.24.0",
    "@radix-ui/themes": "^3.2.1",
    "@xyflow/react": "^12.8.6",
    "classnames": "^2.5.1",
    "esbuild-wasm": "^0.25.11",
    "firebase": "^12.4.0",
    "html-to-image": "^1.11.13",
    "lucide-react": "^0.545.0",
    "nanoid": "^5.1.6",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "zod": "^4.1.12"
  },
  "devDependencies": {
    "@paper-design/shaders-react": "^0.0.71",
    "@types/react": "^18.2.15",
    "@types/react-dom": "^18.2.7",
    "@vitejs/plugin-react": "^4.0.3",
    "sass": "^1.93.2",
    "typescript": "^5.0.2",
    "vite": "^4.4.5",
    "vite-plugin-node-polyfills": "^0.24.0",
    "vite-tsconfig-paths": "^5.1.4"
  }
}

================================================
FILE: README.md
================================================
# @Q Experiment

A prototype-level platform for on-the-fly team collaboration tools

👉 [**Read the article**](https://labs.google/code/experiments/atq)

## Building locally

1. Create a Firebase project with Realtime Database and Auth enabled

2. Make a `.env` file at the root, as a copy of [`.env.example`](./.env.example), filling out the necessary field(s)

3. Install dependencies and start the Vite server:
    ```bash
    $ npm install
    $ npm run dev
    ```

## Technical components

- **Realtime multiplayer** - powered by [Firebase Realtime Database](https://firebase.google.com/docs/database) and Auth.
- **On-the-fly app generation** - simplified coding agent powered by Gemini, along with an in-browser runtime powered by [`esbuild-wasm`](https://www.npmjs.com/package/esbuild-wasm) and inspired by [JSNotebook](https://github.com/tschoffelen/jsnotebook).


================================================
FILE: tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"],
  "exclude": ["**/*.example.tsx"],
  "references": [{ "path": "./tsconfig.node.json" }]
}


================================================
FILE: tsconfig.node.json
================================================
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}


================================================
FILE: vite.config.ts
================================================
import react from "@vitejs/plugin-react";
import path from "path";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";
import { nodePolyfills } from 'vite-plugin-node-polyfills'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), tsconfigPaths(), nodePolyfills()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
});


================================================
FILE: chat-integration\apps-script\appsscript.json
================================================
{
  "timeZone": "America/New_York",
  "dependencies": {},
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8",
  "addOns": {
    "common": {
      "name": "Q (Quartermaster)"
    },
    "chat": {}
  },
  "oauthScopes": [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/script.external_request"
  ]
}

================================================
FILE: chat-integration\functions\firebase.json
================================================
{
  "functions": [
    {
      "source": ".",
      "codebase": "default",
      "disallowLegacyRuntimeConfig": true,
      "ignore": [
        "node_modules",
        ".git",
        "firebase-debug.log",
        "firebase-debug.*.log",
        "*.local"
      ],
      "predeploy": ["npm --prefix \"$RESOURCE_DIR\" run build"]
    }
  ]
}


================================================
FILE: chat-integration\functions\package-lock.json
================================================
{
  "name": "atq-chat-integration",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "atq-chat-integration",
      "dependencies": {
        "firebase-admin": "^12.6.0",
        "firebase-functions": "^6.0.1"
      },
      "devDependencies": {
        "@google/genai": "^1.34.0",
        "nanoid": "^5.1.6",
        "tsdown": "^0.18.3",
        "typescript": "^5.7.3",
        "zod": "^4.2.1"
      },
      "engines": {
        "node": "22"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.28.5.tgz",
      "integrity": "sha512-3EwLFhZ38J4VyIP6WNtt2kUdW9dokXA9Cr4IVIFHuCpZ3H8/YFOl5JjZHisrn1fATPBmKKqXzDFvh9fUwHz6CQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.5",
        "@babel/types": "^7.28.5",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.28.5.tgz",
      "integrity": "sha512-KKBU1VGYR7ORr3At5HAtUQ+TV3SzRCXmA/8OdDZiLDBIZxVyzXuztPjfLd3BV1PRAQGCMWWSHYhL0F8d5uHBDQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.5"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.28.5.tgz",
      "integrity": "sha512-qQ5m48eI/MFLQ5PxQj4PFaprjyCTLI37ElWMmNs0K8Lk3dVeOdNpB3ks8jc7yM5CDmVC73eMVk/trk3fgmrUpA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@emnapi/core": {
      "version": "1.7.1",
      "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.7.1.tgz",
      "integrity": "sha512-o1uhUASyo921r2XtHYOHy7gdkGLge8ghBEQHMWmyJFoXlpU58kIrhhN3w26lpQb6dspetweapMn2CSNwQ8I4wg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/wasi-threads": "1.1.0",
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.7.1",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.7.1.tgz",
      "integrity": "sha512-PVtJr5CmLwYAU9PZDMITZoR5iAOShYREoR45EyyLrbntV50mdePTgUn4AmOw90Ifcj+x2kRjdzr1HP3RrNiHGA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/wasi-threads": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.1.0.tgz",
      "integrity": "sha512-WI0DdZ8xFSbgMjR1sFsKABJ/C5OnRrjT06JXbZKexJGrDuPTzZdDYfFlsgcCXCyf+suG5QU2e/y1Wo2V/OapLQ==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@fastify/busboy": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/@fastify/busboy/-/busboy-3.2.0.tgz",
      "integrity": "sha512-m9FVDXU3GT2ITSe0UaMA5rU3QkfC/UXtCU8y0gSN/GugTqtVldOBWIB5V6V3sbmenVZUIpU6f+mPEO2+m5iTaA==",
      "license": "MIT"
    },
    "node_modules/@firebase/app-check-interop-types": {
      "version": "0.3.2",
      "resolved": "https://registry.npmjs.org/@firebase/app-check-interop-types/-/app-check-interop-types-0.3.2.tgz",
      "integrity": "sha512-LMs47Vinv2HBMZi49C09dJxp0QT5LwDzFaVGf/+ITHe3BlIhUiLNttkATSXplc89A2lAaeTqjgqVkiRfUGyQiQ==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/app-types": {
      "version": "0.9.2",
      "resolved": "https://registry.npmjs.org/@firebase/app-types/-/app-types-0.9.2.tgz",
      "integrity": "sha

================================================
FILE: chat-integration\functions\package.json
================================================
{
  "name": "atq-chat-integration",
  "scripts": {
    "build": "tsdown",
    "dev": "tsdown -w",
    "serve": "npm run build && firebase emulators:start --only functions",
    "shell": "npm run build && firebase functions:shell",
    "start": "npm run shell",
    "deploy": "firebase deploy --only functions",
    "logs": "firebase functions:log"
  },
  "engines": {
    "node": "22"
  },
  "main": "lib/index.js",
  "dependencies": {
    "firebase-admin": "^12.6.0",
    "firebase-functions": "^6.0.1"
  },
  "devDependencies": {
    "@google/genai": "^1.34.0",
    "nanoid": "^5.1.6",
    "zod": "^4.2.1",
    "tsdown": "^0.18.3",
    "typescript": "^5.7.3"
  },
  "private": true
}


================================================
FILE: chat-integration\functions\tsconfig.json
================================================
{
  "compilerOptions": {
    "module": "NodeNext",
    "esModuleInterop": true,
    "moduleResolution": "nodenext",
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "outDir": "lib",
    "sourceMap": true,
    "strict": true,
    "allowArbitraryExtensions": true,
    "target": "es2017"
  },
  "compileOnSave": true,
  "include": [
    "src"
  ]
}


================================================
FILE: chat-integration\functions\tsdown.config.ts
================================================
import { defineConfig } from "tsdown";

export default defineConfig({
  format: ["cjs"],
  target: ["es2022"],
  envFile: ".env",
  clean: true,
  minify: false,
  outDir: "lib",
  fixedExtension: false,
  entry: ["./src/index.ts"],
  platform: "node",
});


================================================
FILE: chat-integration\functions\src\index.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { initializeApp } from "firebase-admin/app";
import { getDatabase } from "firebase-admin/database";
import { setGlobalOptions } from "firebase-functions";
import { onRequest } from "firebase-functions/https";
import * as logger from "firebase-functions/logger";
import { ai } from "./miniapp-generator/ai";
import { generateMiniApp } from "./miniapp-generator/miniapp-generator";
import { generateTitle } from "./miniapp-generator/title-generator";
import { generateId } from "./util";

setGlobalOptions({ maxInstances: 10 });

if (!process.env.TSDOWN_FIREBASE_DATABASE_URL) {
  throw new Error("TSDOWN_FIREBASE_DATABASE_URL is not set");
}

const app = initializeApp({
  databaseURL: process.env.TSDOWN_FIREBASE_DATABASE_URL,
});
const db = getDatabase(app);

async function putSharedSoftDocument(id: string, data: any) {
  await db.ref(`sharedsoft/docs/${id}`).set(data);
}

export const generateSharedSoftDocument = onRequest(
  async (request, response) => {
    if (request.method !== "POST") {
      response.status(405).send("Method not allowed");
      return;
    }

    const { prompt } = request.body || "";
    if (!prompt) {
      response.status(400).send("Missing `prompt` param");
      return;
    }

    let id = generateId();

    logger.info(`[${id}] Generating code asynchronously...`);
    await putSharedSoftDocument(id, {
      content: {
        prompt,
        status: "generating",
      },
    });
    let [appCode, title] = await Promise.all([
      generateMiniApp(ai, prompt),
      generateTitle(ai, prompt),
    ]);
    logger.info(`[${id}] Generated app code!`);
    await putSharedSoftDocument(id, {
      metadata: {
        title,
      },
      content: {
        prompt,
        status: "generated",
        code: appCode,
      },
    });

    response.status(200).send(
      JSON.stringify({
        prompt,
        title,
        id,
      }) + "\n"
    );
  }
);


================================================
FILE: chat-integration\functions\src\util.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { customAlphabet } from "nanoid";

export const generateId = () =>
  customAlphabet(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    10
  )();


================================================
FILE: chat-integration\functions\src\miniapp-generator\ai.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";

export const ai = new GoogleGenAI({
  apiKey: process.env.TSDOWN_GEMINI_API_KEY,
});


================================================
FILE: chat-integration\functions\src\miniapp-generator\counter.example.txt
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { MinusIcon, PlusIcon } from "npm:lucide-react";
import { useSyncedState, useLoggedInUser } from "$";

export default function App() {
  const [count, setCount] = useSyncedState("counter", 0);
  const { name, color } = useLoggedInUser();

  return (
    <div className="flex flex-col items-center justify-center h-screen space-y-4">
      <div>
        Hello, <span style={{ color }}>{name}</span>
      </div>
      <div className="text-8xl text-bold text-green-600">{count}</div>
      <div className="flex gap-1">
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-full"
          onClick={() => setCount(count - 1)}
        >
          <MinusIcon />
        </button>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-full"
          onClick={() => setCount(count + 1)}
        >
          <PlusIcon />
        </button>
      </div>
    </div>
  );
}


================================================
FILE: chat-integration\functions\src\miniapp-generator\fileTypes.d.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

declare module "*.txt" {
  const content: string;
  export default content;
}

================================================
FILE: chat-integration\functions\src\miniapp-generator\host-types.txt
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export type User = { name: string; color: string };

/**
 * Example:
 * ```ts
 * import { useSyncedState } from '$';
 *
 * function MyComponent() {
 *   const [value, setValue] = useSyncedState("value", 15);
 *   return <>The value is {value}</>;
 * }
 * ```
 */
export type useSyncedState = (
  stateKey: string,
  defaultValue: any
) => [any, (newValue: any) => void];

/**
 * Example:
 * ```ts
 * import { useLoggedInUser } from '$';
 *
 * function MyComponent() {
 *   const { name, color } = useLoggedInUser();
 *   return <>You are <span style={{ color }}>{name}</span></>;
 * }
 * ```
 */
export type useLoggedInUser = () => User;

/**
 * Calls AI, returning an async generator that yields content chunks as they arrive. Example:
 * ```ts
 * import { generateContentStream } from '$';
 * async function callAI() {
 *   let request = {
 *     contents: [
 *       {
 *         role: 'user',
 *         parts: [
 *           { text: "Hello there" }
 *         ]
 *       }
 *     ]
 *   };
 *   let result = "";
 *   for await (let chunk of generateContentStream(request)) {
 *     result += chunk;
 *     console.log("Received chunk:", chunk);
 *   }
 *   console.log("Final result:", result);
 * }
 * ```
 */
export type generateContentStream = (
  messages: Array<{ role: "user" | "model"; text: string }>
) => AsyncIterable<string>;


================================================
FILE: chat-integration\functions\src\miniapp-generator\miniapp-generator.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";
import appExampleCounterSource from "./counter.example.txt";
import hostApiTypesSource from "./host-types.txt";

const INSTRUCTIONS = `
You are a helpful assistant that generates code for React "mini apps"
based on a user's prompt. These mini apps are designed to be collaborative (several
users may be using them at once) and sync in real-time using a provided host API.

The generated app should be a single React component in TypeScript that uses functional
components and hooks. The app should be self-contained and not rely on any external
APIs or services.

The app should use Tailwind CSS for styling.

The types for the host API are as follows:

\`\`\`ts
${hostApiTypesSource}
\`\`\`

These APIs are available from the "$", e.g.:

\`\`\`
import { useSyncedState, useLoggedInUser } from "$";
\`\`\`

You can also import packages from npm as needed, using the "npm:" prefix. For example,
to use lucide-react icons, you can import them like so:

\`\`\`ts
import { PlusIcon } from "npm:lucide-react";
\`\`\`

If you need something from React, you can import it from "react", DO NOT prefix it with "npm:".

Here are some examples of prompts and the corresponding app code you should generate:

Prompt: "A simple counter."
App Code:

\`\`\`tsx
${appExampleCounterSource}
\`\`\`
`;

export async function generateMiniApp(
  ai: GoogleGenAI,
  prompt: string,
): Promise<string> {
  let result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    config: {
      systemInstruction: INSTRUCTIONS,
      thinkingConfig: {
        includeThoughts: false,
        thinkingBudget: 1024,
      },
    },
    contents: `
Generate a React mini-app for the following prompt:\n\n
"${prompt}"\n\n
Respond with only the code and nothing else, optionally wrapped in triple backticks.
`,
  });
  let appCode = result.text?.trim() || "";
  appCode = appCode
    .replace(/^\n*```\w*\n/, "")
    .replace(/\n*```\n*$/, "")
    .trim();
  return appCode;
}


================================================
FILE: chat-integration\functions\src\miniapp-generator\title-generator.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";

export async function generateTitle(ai: GoogleGenAI, prompt: string) {
  let result = await ai.models.generateContent({
    model: "gemini-2.5-flash-lite",
    config: {
      systemInstruction: `
            You are great at creating short, catchy titles for app ideas based on
            a brief description of the app's purpose. Given the description below,
            respond with a short title (4 words or less) that captures the essence
            of the app idea. Do not include any additional text or explanation.`
        .replace(/\s+/g, " ")
        .trim(),
    },
    contents: `
          Here is my prompt for an app idea:
          
          ${prompt}
          
          Now give me a short, catchy title for this app idea.`,
  });
  return result.text?.trim();
}


================================================
FILE: src\firebase-config.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

let config: object = {};
try {
  config = JSON.parse(import.meta.env.VITE_FIREBASE_CONFIG);
} catch (e) {
  throw new Error(
    'Must provide FIREBASE_CONFIG as a JSON object (with keys "projectId", "apiKey", etc) in .env',
  );
}
export const FIREBASE_CONFIG = config;


================================================
FILE: src\firebase.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";
import { getFunctions } from "firebase/functions";
import { FIREBASE_CONFIG } from "./firebase-config";

export const app = initializeApp(FIREBASE_CONFIG);
export const db = getDatabase(app);
export const auth = getAuth(app);
export const storage = getStorage(app);
export const functions = getFunctions(app);

================================================
FILE: src\vite-env.d.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

/// <reference types="vite/client" />


================================================
FILE: src\ai\index.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { usePrefsContext } from "@/util/PrefsProvider";
import { GoogleGenAI } from "@google/genai";
import { useMemo } from "react";

export function useGeminiApi() {
  const { prefs } = usePrefsContext();
  return useMemo(() => {
    return new GoogleGenAI({
      apiKey: prefs.geminiApiKey || "FAKE_INVALID_KEY",
      httpOptions: { apiVersion: "v1alpha" },
    });
  }, [prefs.geminiApiKey]);
}


================================================
FILE: src\ai\nano-banana.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { MEDIA_ROOT_PATH } from "@/document/model-and-db";
import { storage } from "@/firebase";
import { GoogleGenAI } from "@google/genai";
import {
  getDownloadURL,
  ref as storageRef,
  uploadBytes,
} from "firebase/storage";

export async function generateImage(
  ai: GoogleGenAI,
  { prompt }: { prompt: string },
): Promise<string> {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image-preview",
    contents: prompt,
  });

  for (const part of response.candidates?.[0].content?.parts || []) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data || "";
      return `data:image/png;base64,${imageData}`;
    }
  }

  throw new Error("No images were generated");
}

export async function saveImage(
  imageDataUrl: string,
  idPath?: string,
): Promise<string> {
  idPath = idPath ?? crypto.randomUUID();
  let storagePath = `${MEDIA_ROOT_PATH}/${idPath}.png`;
  let res = await uploadBytes(
    storageRef(storage, storagePath),
    await fetch(imageDataUrl).then((r) => r.blob()),
  );
  return await getDownloadURL(res.ref);
}


================================================
FILE: src\ai\tools.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import z from "zod";

export type Tool<T> = {
  name: string;
  description: string;
  parameters: z.ZodType<T>;
  run(args: T): Promise<string> | string;
};

export function makeTool<T>(tool: Tool<T>): Tool<T> {
  return tool;
}


================================================
FILE: src\collab\user-colors.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { hashString } from "@/util/hash";
import * as COLORS from "@radix-ui/colors";
import { UserInfo } from "firebase/auth";

const USER_COLORS: (keyof typeof COLORS)[] = [
  "red",
  "pink",
  "purple",
  "indigo",
  "cyan",
  "green",
  "amber",
];

export function globalColorForUser(user: Partial<UserInfo>) {
  let userStr = user.displayName || user.email || user.uid || "Guest";
  let hue = USER_COLORS[hashString(userStr) % USER_COLORS.length];
  return (COLORS[hue] as any)[hue + "9"];
}


================================================
FILE: src\document\model-and-db.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export const APP_ROOT_PATH = "sharedsoft";
export const DOC_ROOT_PATH = `${APP_ROOT_PATH}/docs`;
export const USERINFO_ROOT_PATH = `${APP_ROOT_PATH}/userinfo`;
export const MEDIA_ROOT_PATH = `${APP_ROOT_PATH}/media`;

export type PresenceAppData = {
  canvasCursorPos: { x: number; y: number } | null;
};

export type DocMetadata = {
  creatorUid?: string;
  title?: string;
};

export type AppUserInfo = {
  docs: Record<string, DocMetadata>;
};

export const UNTITLED_DOC_TITLE = "Untitled";


================================================
FILE: src\document\util.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { customAlphabet } from "nanoid";

export const generateId = () =>
  customAlphabet(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    10
  )();


================================================
FILE: src\miniapp\bundler.ts
================================================
// Borrowed heavily from https://github.com/tschoffelen/jsnotebook/blob/main/lib/bundler/index.ts
import * as esbuild from "esbuild-wasm";
import wasmURL from "esbuild-wasm/esbuild.wasm?url";

interface BundledResult {
  output: string;
  error: string;
  npmExternals?: string[];
}

let loaded = false;
let isLoading = false;

export async function loadEsbuild() {
  if (loaded) {
    return;
  }

  if (isLoading) {
    return new Promise((resolve) => {
      const interval = setInterval(() => {
        if (!isLoading) {
          clearInterval(interval);
          resolve("");
        }
      }, 100);
    });
  }

  isLoading = true;

  try {
    await esbuild.initialize({
      worker: true,
      wasmURL,
    });
    loaded = true;
  } catch (error) {
    if (!String(error).includes("more than once")) {
      console.warn("Error initializing ESBuild", error);
    }
  }
  isLoading = false;
}

export async function esBundle(
  modules: Record<string, string>
): Promise<BundledResult> {
  await loadEsbuild();
  try {
    let npmExternals: string[] = [];
    const result = await esbuild.build({
      entryPoints: ["index.ts"],
      bundle: true,
      minify: false,
      format: "esm",
      platform: "node",
      write: false,
      jsx: "automatic",
      external: ["react", "react-dom", "npm:*"],
      plugins: [
        loaderPlugin(modules, (pkgName) => {
          if (!npmExternals.includes(pkgName)) {
            npmExternals.push(pkgName);
          }
        }),
      ],
      define: {
        global: "window",
      },
    });
    return {
      output: result.outputFiles[0].text,
      npmExternals,
      error: "",
    };
  } catch (error) {
    return {
      output: "",
      error: String((error as any)?.message || error),
    };
  }
}

function loaderPlugin(
  modules: Record<string, string>,
  onRequestExternalPackage?: (pkgName: string) => void
): esbuild.Plugin {
  return {
    name: "fetch-plugin",
    setup(build: esbuild.PluginBuild) {
      // handle root entry file of user input
      build.onResolve({ filter: /^(\w+\.ts)$/ }, ({ path }) => {
        return { path, namespace: "app" };
      });

      // handle other modules in the list
      build.onResolve({ filter: /^.+$/ }, ({ path }) => {
        if (modules[path]) return { path, namespace: "app" };
      });

      // handle other modules in the list
      build.onResolve({ filter: /^npm:(.+)$/ }, ({ path }) => {
        onRequestExternalPackage?.(path.replace(/^npm:/, ""));
        return undefined;
      });

      // handle local modules
      build.onResolve({ filter: /\.\/(.+)$/ }, ({ path }) => {
        return { path: path.replace(/^\.\//, "") + ".ts", namespace: "app" };
      });

      // handle root user input code
      build.onLoad({ filter: /^.*$/ }, ({ path }) => {
        if (!modules[path]) throw new Error("Module not provided: " + path);
        return {
          loader: "tsx",
          contents: modules[path],
        };
      });
    },
  };
}


================================================
FILE: src\miniapp\compiler.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { esBundle, loadEsbuild } from "./bundler";
import hostApi from "./host-api?raw";

const REACT_VERSION = "19.1.0";

export async function compileMiniApp(appCode: string): Promise<string> {
  await loadEsbuild();
  const {
    output: jsBundle,
    npmExternals,
    error,
  } = await esBundle({
    "index.ts": `
import React, {useState} from "react";
import ReactDOM from "react-dom/client";
import App from './app';
import {MiniAppWrapper} from '$';

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <MiniAppWrapper>
      <App />
    </MiniAppWrapper>
  </React.StrictMode>
);

`,
    "app.ts": appCode,
    $: hostApi,
  });
  if (error) throw error;

  // const code = `window.codeRunner = async function () { \n${output}\n }`;
  // iframe.current?.contentWindow?.postMessage({ id, code }, "*");
  return assembleHtml({ jsBundle, npmExternals });
}

function importFor(pkg: string) {
  if (pkg === "lucide-react") {
    // lots of breakages with lucide 1.0
    pkg = "lucide-react@0.577.0";
  }
  return `https://esm.sh/${pkg}`;
}

function assembleHtml({
  jsBundle,
  npmExternals,
}: {
  jsBundle: string;
  npmExternals?: string[];
}) {
  return `
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body>
  <div id="root"></div>
  <script type="importmap">
    {
      "imports": ${JSON.stringify(
        {
          ...Object.fromEntries(
            npmExternals?.map((pkg) => [`npm:${pkg}`, importFor(pkg)]) || [],
          ),
          react: `https://esm.sh/react@${REACT_VERSION}`,
          "react/jsx-runtime": `https://esm.sh/react@${REACT_VERSION}/jsx-runtime`,
          "react-dom/": `https://esm.sh/react-dom@${REACT_VERSION}/`,
        },
        null,
        2,
      )}
    }
  </script>
  <style type="text/tailwindcss">
    @layer base {
      button:not([disabled]),
      [role="button"]:not([disabled]) {
        @apply cursor-pointer;
      }
    }
  </style>
  <script type="module">
${jsBundle}
  </script>
</body>
</html>
`;
}


================================================
FILE: src\miniapp\host-protocol.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GenerateContentParameters } from "@google/genai";

export type AppToHostMessage = ProtocolToUnion<AppToHostProtocol>;
export type AppToHostProtocol = {
  ready: {};
  updateState: { stateKey: string; valueJson: string };
  mouseMove: { x: number; y: number };
  aiGenerateContent: { requestId: string; gcr: GenerateContentParameters };
  aiGenerateImage: { requestId: string; prompt: string };
};

export type HostToAppMessage = ProtocolToUnion<HostToAppProtocol>;
export type HostToAppProtocol = {
  initialize: {
    user: { color: string; name: string };
    syncedState: Record<string, any>;
  };
  updateState: { stateKey: string; valueJson: string };
  aiGenerateContentResponse: { requestId: string } & (
    | { chunk: string }
    | { error: string }
    | { done: true }
  );
  aiGenerateImageResponse: { requestId: string } & (
    | { imageUrl: string }
    | { error: string }
  );
};

// type helpers
type Prettify<T> = { [K in keyof T]: T[K] } & {};
type ProtocolToUnion<T extends Record<string, Record<string, any>>> = Prettify<
  {
    [K in keyof T]: T[K] & {
      type: K;
    };
  }[keyof T]
>;


================================================
FILE: src\miniapp\host-types.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export type User = { name: string; color: string };

/**
 * Example:
 * ```ts
 * import { useSyncedState } from '$';
 *
 * function MyComponent() {
 *   const [value, setValue] = useSyncedState("value", 15);
 *   return <>The value is {value}</>;
 * }
 * ```
 */
export type useSyncedState = (
  stateKey: string,
  defaultValue: any,
) => [any, (newValue: any) => void];

/**
 * Example:
 * ```ts
 * import { useLoggedInUser } from '$';
 *
 * function MyComponent() {
 *   const { name, color } = useLoggedInUser();
 *   return <>You are <span style={{ color }}>{name}</span></>;
 * }
 * ```
 */
export type useLoggedInUser = () => User;

/**
 * Calls AI, returning an async generator that yields content chunks as they arrive. Example:
 * ```ts
 * import { generateContentStream } from '$';
 * async function callAI() {
 *   let request = {
 *     contents: [
 *       {
 *         role: 'user',
 *         parts: [
 *           { text: "Hello there" }
 *         ]
 *       }
 *     ]
 *   };
 *   let result = "";
 *   for await (let chunk of generateContentStream(request)) {
 *     result += chunk;
 *     console.log("Received chunk:", chunk);
 *   }
 *   console.log("Final result:", result);
 * }
 * ```
 */
export type generateContentStream = (
  messages: Array<{ role: "user" | "model"; text: string }>,
) => AsyncIterable<string>;

/**
 * Example:
 * ```ts
 * import { generateImage } from '$';
 * async function createImage() {
 *   let imageUrl = await generateImage("A picture of a banana wearing hat");
 *   console.log("Final result:", imageUrl);
 * }
 * ```
 */
export type generateImage = (prompt: string) => Promise<string>;


================================================
FILE: src\miniapp\README.md
================================================
Mini apps are:

- A single React + Tailwind JSX file that exports a default component
- Use a fixed "harness" consisting of a static HTML file and default Tailwind config
- Compiled entirely in the browser with esbuild-wasm


================================================
FILE: src\miniapp-generator\miniapp-generator.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";
import hostApiTypesSource from "../miniapp/host-types?raw";
import appExampleCounterSource from "./counter.example?raw";

const INSTRUCTIONS = `
You are a helpful assistant that generates code for React "mini apps"
based on a user's prompt. These mini apps are designed to be collaborative (several
users may be using them at once) and sync in real-time using a provided host API.

The generated app should be a single React component in TypeScript that uses functional
components and hooks. The app should be self-contained and not rely on any external
APIs or services.

The app should use Tailwind CSS for styling.

The types for the host API are as follows:

\`\`\`ts
${hostApiTypesSource}
\`\`\`

These APIs are available from the "$", e.g.:

\`\`\`
import { useSyncedState, useLoggedInUser } from "$";
\`\`\`

You can also import packages from npm as needed, using the "npm:" prefix. For example,
to use lucide-react icons, you can import them like so:

\`\`\`ts
import { PlusIcon } from "npm:lucide-react";
\`\`\`

If you need something from React, you can import it from "react", DO NOT prefix it with "npm:".

Here are some examples of prompts and the corresponding app code you should generate:

Prompt: "A simple counter."
App Code:

\`\`\`tsx
${appExampleCounterSource}
\`\`\`
`;

export async function generateMiniApp(
  ai: GoogleGenAI,
  prompt: string,
): Promise<string> {
  await new Promise((resolve) => setTimeout(resolve, 1000));
  let result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    config: {
      systemInstruction: INSTRUCTIONS,
      thinkingConfig: {
        includeThoughts: false,
        thinkingBudget: 1024,
      },
    },
    contents: `
Generate a React mini-app for the following prompt:\n\n
"${prompt}"\n\n
Respond with only the code and nothing else, optionally wrapped in triple backticks.
`,
  });
  let appCode = result.text?.trim() || "";
  appCode = appCode
    .replace(/^\n*```\w*\n/, "")
    .replace(/\n*```\n*$/, "")
    .trim();
  return appCode;
}

export async function updateMiniApp(
  ai: GoogleGenAI,
  existingCode: string,
  prompt: string,
): Promise<string> {
  await new Promise((resolve) => setTimeout(resolve, 1000));
  let result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    config: {
      systemInstruction: INSTRUCTIONS,
      thinkingConfig: {
        includeThoughts: false,
        thinkingBudget: 1024,
      },
    },
    contents: `
${existingCode}
---
Update the mini-app above with the following instructions:\n\n
"${prompt}"\n\n
Respond with only the code and nothing else, optionally wrapped in triple backticks.
`,
  });
  let appCode = result.text?.trim() || "";
  appCode = appCode
    .replace(/^\n*```\w*\n/, "")
    .replace(/\n*```\n*$/, "")
    .trim();
  return appCode;
}


================================================
FILE: src\miniapp-generator\title-generator.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";

export async function generateTitle(ai: GoogleGenAI, prompt: string) {
  let result = await ai.models.generateContent({
    model: "gemini-2.5-flash-lite",
    config: {
      systemInstruction: `
            You are great at creating short, catchy titles for app ideas based on
            a brief description of the app's purpose. Given the description below,
            respond with a short title (4 words or less) that captures the essence
            of the app idea. Do not include any additional text or explanation.`
        .replace(/\s+/g, " ")
        .trim(),
    },
    contents: `
Here is my prompt for an app idea:

${prompt}

Now give me a short, catchy title for this app idea.`,
  });
  return result.text?.trim();
}


================================================
FILE: src\util\hash.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

// FNV-1a implementation
export function hashString(str: string) {
  let hash = 2166136261 >>> 0;
  for (let i = 0; i < str.length; i++) {
    hash ^= str.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}


================================================
FILE: src\util\primitives-util.ts
================================================
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export function stripUndefined<T>(obj: T): T {
  return JSON.parse(JSON.stringify(obj));
}
```

## File: chat-integration\apps-script\appsscript.json
```
{
  "timeZone": "America/New_York",
  "dependencies": {},
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8",
  "addOns": {
    "common": {
      "name": "Q (Quartermaster)"
    },
    "chat": {}
  },
  "oauthScopes": [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/script.external_request"
  ]
}
```

## File: chat-integration\functions\firebase.json
```
{
  "functions": [
    {
      "source": ".",
      "codebase": "default",
      "disallowLegacyRuntimeConfig": true,
      "ignore": [
        "node_modules",
        ".git",
        "firebase-debug.log",
        "firebase-debug.*.log",
        "*.local"
      ],
      "predeploy": ["npm --prefix \"$RESOURCE_DIR\" run build"]
    }
  ]
}

```

## File: chat-integration\functions\package-lock.json
```
{
  "name": "atq-chat-integration",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "atq-chat-integration",
      "dependencies": {
        "firebase-admin": "^12.6.0",
        "firebase-functions": "^6.0.1"
      },
      "devDependencies": {
        "@google/genai": "^1.34.0",
        "nanoid": "^5.1.6",
        "tsdown": "^0.18.3",
        "typescript": "^5.7.3",
        "zod": "^4.2.1"
      },
      "engines": {
        "node": "22"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.28.5.tgz",
      "integrity": "sha512-3EwLFhZ38J4VyIP6WNtt2kUdW9dokXA9Cr4IVIFHuCpZ3H8/YFOl5JjZHisrn1fATPBmKKqXzDFvh9fUwHz6CQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.5",
        "@babel/types": "^7.28.5",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.28.5.tgz",
      "integrity": "sha512-KKBU1VGYR7ORr3At5HAtUQ+TV3SzRCXmA/8OdDZiLDBIZxVyzXuztPjfLd3BV1PRAQGCMWWSHYhL0F8d5uHBDQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.5"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.28.5.tgz",
      "integrity": "sha512-qQ5m48eI/MFLQ5PxQj4PFaprjyCTLI37ElWMmNs0K8Lk3dVeOdNpB3ks8jc7yM5CDmVC73eMVk/trk3fgmrUpA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@emnapi/core": {
      "version": "1.7.1",
      "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.7.1.tgz",
      "integrity": "sha512-o1uhUASyo921r2XtHYOHy7gdkGLge8ghBEQHMWmyJFoXlpU58kIrhhN3w26lpQb6dspetweapMn2CSNwQ8I4wg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/wasi-threads": "1.1.0",
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.7.1",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.7.1.tgz",
      "integrity": "sha512-PVtJr5CmLwYAU9PZDMITZoR5iAOShYREoR45EyyLrbntV50mdePTgUn4AmOw90Ifcj+x2kRjdzr1HP3RrNiHGA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/wasi-threads": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.1.0.tgz",
      "integrity": "sha512-WI0DdZ8xFSbgMjR1sFsKABJ/C5OnRrjT06JXbZKexJGrDuPTzZdDYfFlsgcCXCyf+suG5QU2e/y1Wo2V/OapLQ==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@fastify/busboy": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/@fastify/busboy/-/busboy-3.2.0.tgz",
      "integrity": "sha512-m9FVDXU3GT2ITSe0UaMA5rU3QkfC/UXtCU8y0gSN/GugTqtVldOBWIB5V6V3sbmenVZUIpU6f+mPEO2+m5iTaA==",
      "license": "MIT"
    },
    "node_modules/@firebase/app-check-interop-types": {
      "version": "0.3.2",
      "resolved": "https://registry.npmjs.org/@firebase/app-check-interop-types/-/app-check-interop-types-0.3.2.tgz",
      "integrity": "sha512-LMs47Vinv2HBMZi49C09dJxp0QT5LwDzFaVGf/+ITHe3BlIhUiLNttkATSXplc89A2lAaeTqjgqVkiRfUGyQiQ==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/app-types": {
      "version": "0.9.2",
      "resolved": "https://registry.npmjs.org/@firebase/app-types/-/app-types-0.9.2.tgz",
      "integrity": "sha512-oMEZ1TDlBz479lmABwWsWjzHwheQKiAgnuKxE0pz0IXCVx7/rtlkx1fQ6GfgK24WCrxDKMplZrT50Kh04iMbXQ==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/auth-interop-types": {
      "version": "0.2.3",
      "resolved": "https://registry.npmjs.org/@firebase/auth-interop-types/-/auth-interop-types-0.2.3.tgz",
      "integrity": "sha512-Fc9wuJGgxoxQeavybiuwgyi+0rssr76b+nHpj+eGhXFYAdudMWyfBHvFL/I5fEHniUM/UQdFzi9VXJK2iZF7FQ==",
      "license": "Apache-2.0"
    },
    "node_modules/@firebase/component": {
      "version": "0.6.9",
      "resolved": "https://registry.npmjs.org/@firebase/component/-/component-0.6.9.tgz",
      "integrity": "sha512-gm8EUEJE/fEac86AvHn8Z/QW8BvR56TBw3hMW0O838J/1mThYQXAIQBgUv75EqlCZfdawpWLrKt1uXvp9ciK3Q==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/util": "1.10.0",
        "tslib": "^2.1.0"
      }
    },
    "node_modules/@firebase/database": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/@firebase/database/-/database-1.0.8.tgz",
      "integrity": "sha512-dzXALZeBI1U5TXt6619cv0+tgEhJiwlUtQ55WNZY7vGAjv7Q1QioV969iYwt1AQQ0ovHnEW0YW9TiBfefLvErg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app-check-interop-types": "0.3.2",
        "@firebase/auth-interop-types": "0.2.3",
        "@firebase/component": "0.6.9",
        "@firebase/logger": "0.4.2",
        "@firebase/util": "1.10.0",
        "faye-websocket": "0.11.4",
        "tslib": "^2.1.0"
      }
    },
    "node_modules/@firebase/database-compat": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/@firebase/database-compat/-/database-compat-1.0.8.tgz",
      "integrity": "sha512-OpeWZoPE3sGIRPBKYnW9wLad25RaWbGyk7fFQe4xnJQKRzlynWeFBSRRAoLE2Old01WXwskUiucNqUUVlFsceg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/component": "0.6.9",
        "@firebase/database": "1.0.8",
        "@firebase/database-types": "1.0.5",
        "@firebase/logger": "0.4.2",
        "@firebase/util": "1.10.0",
        "tslib": "^2.1.0"
      }
    },
    "node_modules/@firebase/database-types": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/@firebase/database-types/-/database-types-1.0.5.tgz",
      "integrity": "sha512-fTlqCNwFYyq/C6W7AJ5OCuq5CeZuBEsEwptnVxlNPkWCo5cTTyukzAHRSO/jaQcItz33FfYrrFk1SJofcu2AaQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@firebase/app-types": "0.9.2",
        "@firebase/util": "1.10.0"
      }
    },
    "node_modules/@firebase/logger": {
      "version": "0.4.2",
      "resolved": "https://registry.npmjs.org/@firebase/logger/-/logger-0.4.2.tgz",
      "integrity": "sha512-Q1VuA5M1Gjqrwom6I6NUU4lQXdo9IAQieXlujeHZWvRt1b7qQ0KwBaNAjgxG27jgF9/mUwsNmO8ptBCGVYhB0A==",
      "license": "Apache-2.0",
      "dependencies": {
        "tslib": "^2.1.0"
      }
    },
    "node_modules/@firebase/util": {
      "version": "1.10.0",
      "resolved": "https://registry.npmjs.org/@firebase/util/-/util-1.10.0.tgz",
      "integrity": "sha512-xKtx4A668icQqoANRxyDLBLz51TAbDP9KRfpbKGxiCAW346d0BeJe5vN6/hKxxmWwnZ0mautyv39JxviwwQMOQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "tslib": "^2.1.0"
      }
    },
    "node_modules/@google-cloud/firestore": {
      "version": "7.11.6",
      "resolved": "https://registry.npmjs.org/@google-cloud/firestore/-/firestore-7.11.6.tgz",
      "integrity": "sha512-EW/O8ktzwLfyWBOsNuhRoMi8lrC3clHM5LVFhGvO1HCsLozCOOXRAlHrYBoE6HL42Sc8yYMuCb2XqcnJ4OOEpw==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "@opentelemetry/api": "^1.3.0",
        "fast-deep-equal": "^3.1.1",
        "functional-red-black-tree": "^1.0.1",
        "google-gax": "^4.3.3",
        "protobufjs": "^7.2.6"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@google-cloud/paginator": {
      "version": "5.0.2",
      "resolved": "https://registry.npmjs.org/@google-cloud/paginator/-/paginator-5.0.2.tgz",
      "integrity": "sha512-DJS3s0OVH4zFDB1PzjxAsHqJT6sKVbRwwML0ZBP9PbU7Yebtu/7SWMRzvO2J3nUi9pRNITCfu4LJeooM2w4pjg==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "arrify": "^2.0.0",
        "extend": "^3.0.2"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@google-cloud/projectify": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/projectify/-/projectify-4.0.0.tgz",
      "integrity": "sha512-MmaX6HeSvyPbWGwFq7mXdo0uQZLGBYCwziiLIGq5JVX+/bdI3SAq6bP98trV5eTWfLuvsMcIC1YJOF2vfteLFA==",
      "license": "Apache-2.0",
      "optional": true,
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@google-cloud/promisify": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/promisify/-/promisify-4.0.0.tgz",
      "integrity": "sha512-Orxzlfb9c67A15cq2JQEyVc7wEsmFBmHjZWZYQMUyJ1qivXyMwdyNOs9odi79hze+2zqdTtu1E19IM/FtqZ10g==",
      "license": "Apache-2.0",
      "optional": true,
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/@google-cloud/storage": {
      "version": "7.18.0",
      "resolved": "https://registry.npmjs.org/@google-cloud/storage/-/storage-7.18.0.tgz",
      "integrity": "sha512-r3ZwDMiz4nwW6R922Z1pwpePxyRwE5GdevYX63hRmAQUkUQJcBH/79EnQPDv5cOv1mFBgevdNWQfi3tie3dHrQ==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "@google-cloud/paginator": "^5.0.0",
        "@google-cloud/projectify": "^4.0.0",
        "@google-cloud/promisify": "<4.1.0",
        "abort-controller": "^3.0.0",
        "async-retry": "^1.3.3",
        "duplexify": "^4.1.3",
        "fast-xml-parser": "^4.4.1",
        "gaxios": "^6.0.2",
        "google-auth-library": "^9.6.3",
        "html-entities": "^2.5.2",
        "mime": "^3.0.0",
        "p-limit": "^3.0.1",
        "retry-request": "^7.0.0",
        "teeny-request": "^9.0.0",
        "uuid": "^8.0.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/@google-cloud/storage/node_modules/uuid": {
      "version": "8.3.2",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-8.3.2.tgz",
      "integrity": "sha512-+NYs2QeMWy+GWFOEm9xnn6HCDp0l7QBD7ml8zLUmJ+93Q5NF0NocErnwkTkXVFNiX3/fpC6afS8Dhb/gz7R7eg==",
      "license": "MIT",
      "optional": true,
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    },
    "node_modules/@google/genai": {
      "version": "1.34.0",
      "resolved": "https://registry.npmjs.org/@google/genai/-/genai-1.34.0.tgz",
      "integrity": "sha512-vu53UMPvjmb7PGzlYu6Tzxso8Dfhn+a7eQFaS2uNemVtDZKwzSpJ5+ikqBbXplF7RGB1STcVDqCkPvquiwb2sw==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "google-auth-library": "^10.3.0",
        "ws": "^8.18.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "@modelcontextprotocol/sdk": "^1.24.0"
      },
      "peerDependenciesMeta": {
        "@modelcontextprotocol/sdk": {
          "optional": true
        }
      }
    },
    "node_modules/@google/genai/node_modules/gaxios": {
      "version": "7.1.3",
      "resolved": "https://registry.npmjs.org/gaxios/-/gaxios-7.1.3.tgz",
      "integrity": "sha512-YGGyuEdVIjqxkxVH1pUTMY/XtmmsApXrCVv5EU25iX6inEPbV+VakJfLealkBtJN69AQmh1eGOdCl9Sm1UP6XQ==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "extend": "^3.0.2",
        "https-proxy-agent": "^7.0.1",
        "node-fetch": "^3.3.2",
        "rimraf": "^5.0.1"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google/genai/node_modules/gcp-metadata": {
      "version": "8.1.2",
      "resolved": "https://registry.npmjs.org/gcp-metadata/-/gcp-metadata-8.1.2.tgz",
      "integrity": "sha512-zV/5HKTfCeKWnxG0Dmrw51hEWFGfcF2xiXqcA3+J90WDuP0SvoiSO5ORvcBsifmx/FoIjgQN3oNOGaQ5PhLFkg==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "gaxios": "^7.0.0",
        "google-logging-utils": "^1.0.0",
        "json-bigint": "^1.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google/genai/node_modules/google-auth-library": {
      "version": "10.5.0",
      "resolved": "https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.5.0.tgz",
      "integrity": "sha512-7ABviyMOlX5hIVD60YOfHw4/CxOfBhyduaYB+wbFWCWoni4N7SLcV46hrVRktuBbZjFC9ONyqamZITN7q3n32w==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "base64-js": "^1.3.0",
        "ecdsa-sig-formatter": "^1.0.11",
        "gaxios": "^7.0.0",
        "gcp-metadata": "^8.0.0",
        "google-logging-utils": "^1.0.0",
        "gtoken": "^8.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google/genai/node_modules/google-logging-utils": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/google-logging-utils/-/google-logging-utils-1.1.3.tgz",
      "integrity": "sha512-eAmLkjDjAFCVXg7A1unxHsLf961m6y17QFqXqAXGj/gVkKFrEICfStRfwUlGNfeCEjNRa32JEWOUTlYXPyyKvA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/@google/genai/node_modules/gtoken": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/gtoken/-/gtoken-8.0.0.tgz",
      "integrity": "sha512-+CqsMbHPiSTdtSO14O51eMNlrp9N79gmeqmXeouJOhfucAedHw9noVe/n5uJk3tbKE6a+6ZCQg3RPhVhHByAIw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "gaxios": "^7.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@google/genai/node_modules/node-fetch": {
      "version": "3.3.2",
      "resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-3.3.2.tgz",
      "integrity": "sha512-dRB78srN/l6gqWulah9SrxeYnxeddIG30+GOqK/9OlLVyLg3HPnr6SqOWTWOXKRwC2eGYCkZ59NNuSgvSrpgOA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "data-uri-to-buffer": "^4.0.0",
        "fetch-blob": "^3.1.4",
        "formdata-polyfill": "^4.0.10"
      },
      "engines": {
        "node": "^12.20.0 || ^14.13.1 || >=16.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/node-fetch"
      }
    },
    "node_modules/@grpc/grpc-js": {
      "version": "1.14.3",
      "resolved": "https://registry.npmjs.org/@grpc/grpc-js/-/grpc-js-1.14.3.tgz",
      "integrity": "sha512-Iq8QQQ/7X3Sac15oB6p0FmUg/klxQvXLeileoqrTRGJYLV+/9tubbr9ipz0GKHjmXVsgFPo/+W+2cA8eNcR+XA==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "@grpc/proto-loader": "^0.8.0",
        "@js-sdsl/ordered-map": "^4.4.2"
      },
      "engines": {
        "node": ">=12.10.0"
      }
    },
    "node_modules/@grpc/grpc-js/node_modules/@grpc/proto-loader": {
      "version": "0.8.0",
      "resolved": "https://registry.npmjs.org/@grpc/proto-loader/-/proto-loader-0.8.0.tgz",
      "integrity": "sha512-rc1hOQtjIWGxcxpb9aHAfLpIctjEnsDehj0DAiVfBlmT84uvR0uUtN2hEi/ecvWVjXUGf5qPF4qEgiLOx1YIMQ==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "lodash.camelcase": "^4.3.0",
        "long": "^5.0.0",
        "protobufjs": "^7.5.3",
        "yargs": "^17.7.2"
      },
      "bin": {
        "proto-loader-gen-types": "build/bin/proto-loader-gen-types.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/@grpc/proto-loader": {
      "version": "0.7.15",
      "resolved": "https://registry.npmjs.org/@grpc/proto-loader/-/proto-loader-0.7.15.tgz",
      "integrity": "sha512-tMXdRCfYVixjuFK+Hk0Q1s38gV9zDiDJfWL3h1rv4Qc39oILCu1TRTDt7+fGUI8K4G1Fj125Hx/ru3azECWTyQ==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "lodash.camelcase": "^4.3.0",
        "long": "^5.0.0",
        "protobufjs": "^7.2.5",
        "yargs": "^17.7.2"
      },
      "bin": {
        "proto-loader-gen-types": "build/bin/proto-loader-gen-types.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/@isaacs/cliui": {
      "version": "8.0.2",
      "resolved": "https://registry.npmjs.org/@isaacs/cliui/-/cliui-8.0.2.tgz",
      "integrity": "sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "string-width": "^5.1.2",
        "string-width-cjs": "npm:string-width@^4.2.0",
        "strip-ansi": "^7.0.1",
        "strip-ansi-cjs": "npm:strip-ansi@^6.0.1",
        "wrap-ansi": "^8.1.0",
        "wrap-ansi-cjs": "npm:wrap-ansi@^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@js-sdsl/ordered-map": {
      "version": "4.4.2",
      "resolved": "https://registry.npmjs.org/@js-sdsl/ordered-map/-/ordered-map-4.4.2.tgz",
      "integrity": "sha512-iUKgm52T8HOE/makSxjqoWhe95ZJA1/G1sYsGev2JDKUSS14KAgg1LHb+Ba+IPow0xflbnSkOsZcO08C7w1gYw==",
      "license": "MIT",
      "optional": true,
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/js-sdsl"
      }
    },
    "node_modules/@opentelemetry/api": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@opentelemetry/api/-/api-1.9.0.tgz",
      "integrity": "sha512-3giAOQvZiH5F9bMlMiv8+GSPMeqg0dbaeo58/0SlA9sxSqZhnUtxzX9/2FzyhS9sWQf5S0GJE0AKBrFqjpeYcg==",
      "license": "Apache-2.0",
      "optional": true,
      "engines": {
        "node": ">=8.0.0"
      }
    },
    "node_modules/@oxc-project/types": {
      "version": "0.103.0",
      "resolved": "https://registry.npmjs.org/@oxc-project/types/-/types-0.103.0.tgz",
      "integrity": "sha512-bkiYX5kaXWwUessFRSoXFkGIQTmc6dLGdxuRTrC+h8PSnIdZyuXHHlLAeTmOue5Br/a0/a7dHH0Gca6eXn9MKg==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/Boshen"
      }
    },
    "node_modules/@pkgjs/parseargs": {
      "version": "0.11.0",
      "resolved": "https://registry.npmjs.org/@pkgjs/parseargs/-/parseargs-0.11.0.tgz",
      "integrity": "sha512-+1VkjdD0QBLPodGrJUeqarH8VAIvQODIbwh9XpP5Syisf7YoQgsJKPNFoqqLQlu+VQ/tVSshMR6loPMn8U+dPg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/@pkgr/core": {
      "version": "0.2.9",
      "resolved": "https://registry.npmjs.org/@pkgr/core/-/core-0.2.9.tgz",
      "integrity": "sha512-QNqXyfVS2wm9hweSYD2O7F0G06uurj9kZ96TRQE5Y9hU7+tgdZwIkbAKc5Ocy1HxEY2kuDQa6cQ1WRs/O5LFKA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "peer": true,
      "engines": {
        "node": "^12.20.0 || ^14.18.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/pkgr"
      }
    },
    "node_modules/@protobufjs/aspromise": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/aspromise/-/aspromise-1.1.2.tgz",
      "integrity": "sha512-j+gKExEuLmKwvz3OgROXtrJ2UG2x8Ch2YZUxahh+s1F2HZ+wAceUNLkvy6zKCPVRkU++ZWQrdxsUeQXmcg4uoQ==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/base64": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/base64/-/base64-1.1.2.tgz",
      "integrity": "sha512-AZkcAA5vnN/v4PDqKyMR5lx7hZttPDgClv83E//FMNhR2TMcLUhfRUBHCmSl0oi9zMgDDqRUJkSxO3wm85+XLg==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/codegen": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/@protobufjs/codegen/-/codegen-2.0.4.tgz",
      "integrity": "sha512-YyFaikqM5sH0ziFZCN3xDC7zeGaB/d0IUb9CATugHWbd1FRFwWwt4ld4OYMPWu5a3Xe01mGAULCdqhMlPl29Jg==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/eventemitter": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/eventemitter/-/eventemitter-1.1.0.tgz",
      "integrity": "sha512-j9ednRT81vYJ9OfVuXG6ERSTdEL1xVsNgqpkxMsbIabzSo3goCjDIveeGv5d03om39ML71RdmrGNjG5SReBP/Q==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/fetch": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/fetch/-/fetch-1.1.0.tgz",
      "integrity": "sha512-lljVXpqXebpsijW71PZaCYeIcE5on1w5DlQy5WH6GLbFryLUrBD4932W/E2BSpfRJWseIL4v/KPgBFxDOIdKpQ==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "@protobufjs/aspromise": "^1.1.1",
        "@protobufjs/inquire": "^1.1.0"
      }
    },
    "node_modules/@protobufjs/float": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/float/-/float-1.0.2.tgz",
      "integrity": "sha512-Ddb+kVXlXst9d+R9PfTIxh1EdNkgoRe5tOX6t01f1lYWOvJnSPDBlG241QLzcyPdoNTsblLUdujGSE4RzrTZGQ==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/inquire": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/inquire/-/inquire-1.1.0.tgz",
      "integrity": "sha512-kdSefcPdruJiFMVSbn801t4vFK7KB/5gd2fYvrxhuJYg8ILrmn9SKSX2tZdV6V+ksulWqS7aXjBcRXl3wHoD9Q==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/path": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/path/-/path-1.1.2.tgz",
      "integrity": "sha512-6JOcJ5Tm08dOHAbdR3GrvP+yUUfkjG5ePsHYczMFLq3ZmMkAD98cDgcT2iA1lJ9NVwFd4tH/iSSoe44YWkltEA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/pool": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/pool/-/pool-1.1.0.tgz",
      "integrity": "sha512-0kELaGSIDBKvcgS4zkjz1PeddatrjYcmMWOlAuAPwAeccUrPHdUqo/J6LiymHHEiJT5NrF1UVwxY14f+fy4WQw==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@protobufjs/utf8": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/utf8/-/utf8-1.1.0.tgz",
      "integrity": "sha512-Vvn3zZrhQZkkBE8LSuW3em98c0FwgO4nxzv6OdSxPKJIEKY2bGbHn+mhGIPerzI4twdxaP8/0+06HBpwf345Lw==",
      "license": "BSD-3-Clause"
    },
    "node_modules/@quansync/fs": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/@quansync/fs/-/fs-1.0.0.tgz",
      "integrity": "sha512-4TJ3DFtlf1L5LDMaM6CanJ/0lckGNtJcMjQ1NAV6zDmA0tEHKZtxNKin8EgPaVX1YzljbxckyT2tJrpQKAtngQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "quansync": "^1.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sxzz"
      }
    },
    "node_modules/@rolldown/binding-android-arm64": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-android-arm64/-/binding-android-arm64-1.0.0-beta.57.tgz",
      "integrity": "sha512-GoOVDy8bjw9z1K30Oo803nSzXJS/vWhFijFsW3kzvZCO8IZwFnNa6pGctmbbJstKl3Fv6UBwyjJQN6msejW0IQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-arm64": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-arm64/-/binding-darwin-arm64-1.0.0-beta.57.tgz",
      "integrity": "sha512-9c4FOhRGpl+PX7zBK5p17c5efpF9aSpTPgyigv57hXf5NjQUaJOOiejPLAtFiKNBIfm5Uu6yFkvLKzOafNvlTw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-x64": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-x64/-/binding-darwin-x64-1.0.0-beta.57.tgz",
      "integrity": "sha512-6RsB8Qy4LnGqNGJJC/8uWeLWGOvbRL/KG5aJ8XXpSEupg/KQtlBEiFaYU/Ma5Usj1s+bt3ItkqZYAI50kSplBA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-freebsd-x64": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-freebsd-x64/-/binding-freebsd-x64-1.0.0-beta.57.tgz",
      "integrity": "sha512-uA9kG7+MYkHTbqwv67Tx+5GV5YcKd33HCJIi0311iYBd25yuwyIqvJfBdt1VVB8tdOlyTb9cPAgfCki8nhwTQg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm-gnueabihf": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm-gnueabihf/-/binding-linux-arm-gnueabihf-1.0.0-beta.57.tgz",
      "integrity": "sha512-3KkS0cHsllT2T+Te+VZMKHNw6FPQihYsQh+8J4jkzwgvAQpbsbXmrqhkw3YU/QGRrD8qgcOvBr6z5y6Jid+rmw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-gnu": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-gnu/-/binding-linux-arm64-gnu-1.0.0-beta.57.tgz",
      "integrity": "sha512-A3/wu1RgsHhqP3rVH2+sM81bpk+Qd2XaHTl8LtX5/1LNR7QVBFBCpAoiXwjTdGnI5cMdBVi7Z1pi52euW760Fw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-musl": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-musl/-/binding-linux-arm64-musl-1.0.0-beta.57.tgz",
      "integrity": "sha512-d0kIVezTQtazpyWjiJIn5to8JlwfKITDqwsFv0Xc6s31N16CD2PC/Pl2OtKgS7n8WLOJbfqgIp5ixYzTAxCqMg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-gnu": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-gnu/-/binding-linux-x64-gnu-1.0.0-beta.57.tgz",
      "integrity": "sha512-E199LPijo98yrLjPCmETx8EF43sZf9t3guSrLee/ej1rCCc3zDVTR4xFfN9BRAapGVl7/8hYqbbiQPTkv73kUg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-musl": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-musl/-/binding-linux-x64-musl-1.0.0-beta.57.tgz",
      "integrity": "sha512-++EQDpk/UJ33kY/BNsh7A7/P1sr/jbMuQ8cE554ZIy+tCUWCivo9zfyjDUoiMdnxqX6HLJEqqGnbGQOvzm2OMQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-openharmony-arm64": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-openharmony-arm64/-/binding-openharmony-arm64-1.0.0-beta.57.tgz",
      "integrity": "sha512-voDEBcNqxbUv/GeXKFtxXVWA+H45P/8Dec4Ii/SbyJyGvCqV1j+nNHfnFUIiRQ2Q40DwPe/djvgYBs9PpETiMA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-wasm32-wasi": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-wasm32-wasi/-/binding-wasm32-wasi-1.0.0-beta.57.tgz",
      "integrity": "sha512-bRhcF7NLlCnpkzLVlVhrDEd0KH22VbTPkPTbMjlYvqhSmarxNIq5vtlQS8qmV7LkPKHrNLWyJW/V/sOyFba26Q==",
      "cpu": [
        "wasm32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@napi-rs/wasm-runtime": "^1.1.0"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@rolldown/binding-wasm32-wasi/node_modules/@napi-rs/wasm-runtime": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@napi-rs/wasm-runtime/-/wasm-runtime-1.1.0.tgz",
      "integrity": "sha512-Fq6DJW+Bb5jaWE69/qOE0D1TUN9+6uWhCeZpdnSBk14pjLcCWR7Q8n49PTSPHazM37JqrsdpEthXy2xn6jWWiA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/core": "^1.7.1",
        "@emnapi/runtime": "^1.7.1",
        "@tybys/wasm-util": "^0.10.1"
      }
    },
    "node_modules/@rolldown/binding-win32-arm64-msvc": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-arm64-msvc/-/binding-win32-arm64-msvc-1.0.0-beta.57.tgz",
      "integrity": "sha512-rnDVGRks2FQ2hgJ2g15pHtfxqkGFGjJQUDWzYznEkE8Ra2+Vag9OffxdbJMZqBWXHVM0iS4dv8qSiEn7bO+n1Q==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-win32-x64-msvc": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-x64-msvc/-/binding-win32-x64-msvc-1.0.0-beta.57.tgz",
      "integrity": "sha512-OqIUyNid1M4xTj6VRXp/Lht/qIP8fo25QyAZlCP+p6D2ATCEhyW4ZIFLnC9zAGN/HMbXoCzvwfa8Jjg/8J4YEg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/pluginutils": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.0-beta.57.tgz",
      "integrity": "sha512-aQNelgx14tGA+n2tNSa9x6/jeoCL9fkDeCei7nOKnHx0fEFRRMu5ReiITo+zZD5TzWDGGRjbSYCs93IfRIyTuQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@tootallnate/once": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/@tootallnate/once/-/once-2.0.0.tgz",
      "integrity": "sha512-XCuKFP5PS55gnMVu3dty8KPatLqUoy/ZYzDzAGCQ8JNFCkLXzmI7vNHCR+XpbZaMWQK/vQubr7PkYq8g470J/A==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">= 10"
      }
    },
    "node_modules/@tybys/wasm-util": {
      "version": "0.10.1",
      "resolved": "https://registry.npmjs.org/@tybys/wasm-util/-/wasm-util-0.10.1.tgz",
      "integrity": "sha512-9tTaPJLSiejZKx+Bmog4uSubteqTvFrVrURwkmHixBo0G4seD0zUxp98E1DzUBJxLQ3NPwXrGKDiVjwx/DpPsg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@types/body-parser": {
      "version": "1.19.6",
      "resolved": "https://registry.npmjs.org/@types/body-parser/-/body-parser-1.19.6.tgz",
      "integrity": "sha512-HLFeCYgz89uk22N5Qg3dvGvsv46B8GLvKKo1zKG4NybA8U2DiEO3w9lqGg29t/tfLRJpJ6iQxnVw4OnB7MoM9g==",
      "license": "MIT",
      "dependencies": {
        "@types/connect": "*",
        "@types/node": "*"
      }
    },
    "node_modules/@types/caseless": {
      "version": "0.12.5",
      "resolved": "https://registry.npmjs.org/@types/caseless/-/caseless-0.12.5.tgz",
      "integrity": "sha512-hWtVTC2q7hc7xZ/RLbxapMvDMgUnDvKvMOpKal4DrMyfGBUfB1oKaZlIRr6mJL+If3bAP6sV/QneGzF6tJjZDg==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/@types/connect": {
      "version": "3.4.38",
      "resolved": "https://registry.npmjs.org/@types/connect/-/connect-3.4.38.tgz",
      "integrity": "sha512-K6uROf1LD88uDQqJCktA4yzL1YYAK6NgfsI0v/mTgyPKWsX1CnJ0XPSDhViejru1GcRkLWb8RlzFYJRqGUbaug==",
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/cors": {
      "version": "2.8.19",
      "resolved": "https://registry.npmjs.org/@types/cors/-/cors-2.8.19.tgz",
      "integrity": "sha512-mFNylyeyqN93lfe/9CSxOGREz8cpzAhH+E93xJ4xWQf62V8sQ/24reV2nyzUWM6H6Xji+GGHpkbLe7pVoUEskg==",
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/express": {
      "version": "4.17.25",
      "resolved": "https://registry.npmjs.org/@types/express/-/express-4.17.25.tgz",
      "integrity": "sha512-dVd04UKsfpINUnK0yBoYHDF3xu7xVH4BuDotC/xGuycx4CgbP48X/KF/586bcObxT0HENHXEU8Nqtu6NR+eKhw==",
      "license": "MIT",
      "dependencies": {
        "@types/body-parser": "*",
        "@types/express-serve-static-core": "^4.17.33",
        "@types/qs": "*",
        "@types/serve-static": "^1"
      }
    },
    "node_modules/@types/express-serve-static-core": {
      "version": "4.19.7",
      "resolved": "https://registry.npmjs.org/@types/express-serve-static-core/-/express-serve-static-core-4.19.7.tgz",
      "integrity": "sha512-FvPtiIf1LfhzsaIXhv/PHan/2FeQBbtBDtfX2QfvPxdUelMDEckK08SM6nqo1MIZY3RUlfA+HV8+hFUSio78qg==",
      "license": "MIT",
      "dependencies": {
        "@types/node": "*",
        "@types/qs": "*",
        "@types/range-parser": "*",
        "@types/send": "*"
      }
    },
    "node_modules/@types/http-errors": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@types/http-errors/-/http-errors-2.0.5.tgz",
      "integrity": "sha512-r8Tayk8HJnX0FztbZN7oVqGccWgw98T/0neJphO91KkmOzug1KkofZURD4UaD5uH8AqcFLfdPErnBod0u71/qg==",
      "license": "MIT"
    },
    "node_modules/@types/jsonwebtoken": {
      "version": "9.0.10",
      "resolved": "https://registry.npmjs.org/@types/jsonwebtoken/-/jsonwebtoken-9.0.10.tgz",
      "integrity": "sha512-asx5hIG9Qmf/1oStypjanR7iKTv0gXQ1Ov/jfrX6kS/EO0OFni8orbmGCn0672NHR3kXHwpAwR+B368ZGN/2rA==",
      "license": "MIT",
      "dependencies": {
        "@types/ms": "*",
        "@types/node": "*"
      }
    },
    "node_modules/@types/long": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/@types/long/-/long-4.0.2.tgz",
      "integrity": "sha512-MqTGEo5bj5t157U6fA/BiDynNkn0YknVdh48CMPkTSpFTVmvao5UQmm7uEF6xBEo7qIMAlY/JSleYaE6VOdpaA==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/@types/mime": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/@types/mime/-/mime-1.3.5.tgz",
      "integrity": "sha512-/pyBZWSLD2n0dcHE3hq8s8ZvcETHtEuF+3E7XVt0Ig2nvsVQXdghHVcEkIWjy9A0wKfTn97a/PSDYohKIlnP/w==",
      "license": "MIT"
    },
    "node_modules/@types/ms": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/@types/ms/-/ms-2.1.0.tgz",
      "integrity": "sha512-GsCCIZDE/p3i96vtEqx+7dBUGXrc7zeSK3wwPHIaRThS+9OhWIXRqzs4d6k1SVU8g91DrNRWxWUGhp5KXQb2VA==",
      "license": "MIT"
    },
    "node_modules/@types/node": {
      "version": "22.19.3",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-22.19.3.tgz",
      "integrity": "sha512-1N9SBnWYOJTrNZCdh/yJE+t910Y128BoyY+zBLWhL3r0TYzlTmFdXrPwHL9DyFZmlEXNQQolTZh3KHV31QDhyA==",
      "license": "MIT",
      "dependencies": {
        "undici-types": "~6.21.0"
      }
    },
    "node_modules/@types/qs": {
      "version": "6.14.0",
      "resolved": "https://registry.npmjs.org/@types/qs/-/qs-6.14.0.tgz",
      "integrity": "sha512-eOunJqu0K1923aExK6y8p6fsihYEn/BYuQ4g0CxAAgFc4b/ZLN4CrsRZ55srTdqoiLzU2B2evC+apEIxprEzkQ==",
      "license": "MIT"
    },
    "node_modules/@types/range-parser": {
      "version": "1.2.7",
      "resolved": "https://registry.npmjs.org/@types/range-parser/-/range-parser-1.2.7.tgz",
      "integrity": "sha512-hKormJbkJqzQGhziax5PItDUTMAM9uE2XXQmM37dyd4hVM+5aVl7oVxMVUiVQn2oCQFN/LKCZdvSM0pFRqbSmQ==",
      "license": "MIT"
    },
    "node_modules/@types/request": {
      "version": "2.48.13",
      "resolved": "https://registry.npmjs.org/@types/request/-/request-2.48.13.tgz",
      "integrity": "sha512-FGJ6udDNUCjd19pp0Q3iTiDkwhYup7J8hpMW9c4k53NrccQFFWKRho6hvtPPEhnXWKvukfwAlB6DbDz4yhH5Gg==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@types/caseless": "*",
        "@types/node": "*",
        "@types/tough-cookie": "*",
        "form-data": "^2.5.5"
      }
    },
    "node_modules/@types/send": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/@types/send/-/send-1.2.1.tgz",
      "integrity": "sha512-arsCikDvlU99zl1g69TcAB3mzZPpxgw0UQnaHeC1Nwb015xp8bknZv5rIfri9xTOcMuaVgvabfIRA7PSZVuZIQ==",
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/serve-static": {
      "version": "1.15.10",
      "resolved": "https://registry.npmjs.org/@types/serve-static/-/serve-static-1.15.10.tgz",
      "integrity": "sha512-tRs1dB+g8Itk72rlSI2ZrW6vZg0YrLI81iQSTkMmOqnqCaNr/8Ek4VwWcN5vZgCYWbg/JJSGBlUaYGAOP73qBw==",
      "license": "MIT",
      "dependencies": {
        "@types/http-errors": "*",
        "@types/node": "*",
        "@types/send": "<1"
      }
    },
    "node_modules/@types/serve-static/node_modules/@types/send": {
      "version": "0.17.6",
      "resolved": "https://registry.npmjs.org/@types/send/-/send-0.17.6.tgz",
      "integrity": "sha512-Uqt8rPBE8SY0RK8JB1EzVOIZ32uqy8HwdxCnoCOsYrvnswqmFZ/k+9Ikidlk/ImhsdvBsloHbAlewb2IEBV/Og==",
      "license": "MIT",
      "dependencies": {
        "@types/mime": "^1",
        "@types/node": "*"
      }
    },
    "node_modules/@types/tough-cookie": {
      "version": "4.0.5",
      "resolved": "https://registry.npmjs.org/@types/tough-cookie/-/tough-cookie-4.0.5.tgz",
      "integrity": "sha512-/Ad8+nIOV7Rl++6f1BdKxFSMgmoqEoYbHRpPcx3JEfv8VRsQe9Z4mCXeJBzxs7mbHY/XOZZuXlRNfhpVPbs6ZA==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/abort-controller": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/abort-controller/-/abort-controller-3.0.0.tgz",
      "integrity": "sha512-h8lQ8tacZYnR3vNQTgibj+tODHI5/+l06Au2Pcriv/Gmet0eaj4TwWH41sO9wnHDiQsEj19q0drzdWdeAHtweg==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "event-target-shim": "^5.0.0"
      },
      "engines": {
        "node": ">=6.5"
      }
    },
    "node_modules/accepts": {
      "version": "1.3.8",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.8.tgz",
      "integrity": "sha512-PYAthTa2m2VKxuvSD3DPC/Gy+U+sOA1LAuT8mkmRuvw+NACSaeXEQ+NHcVF7rONl6qcaxV3Uuemwawk+7+SJLw==",
      "license": "MIT",
      "dependencies": {
        "mime-types": "~2.1.34",
        "negotiator": "0.6.3"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/agent-base": {
      "version": "7.1.4",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-7.1.4.tgz",
      "integrity": "sha512-MnA+YT8fwfJPgBx3m60MNqakm30XOkyIoH1y6huTQvC0PwZG7ki8NacLBcrPbNoo8vEZy7Jpuk7+jMO+CUovTQ==",
      "devOptional": true,
      "license": "MIT",
      "engines": {
        "node": ">= 14"
      }
    },
    "node_modules/ansi-regex": {
      "version": "6.2.2",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.2.2.tgz",
      "integrity": "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-regex?sponsor=1"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "devOptional": true,
      "license": "MIT",
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
    "node_modules/ansis": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/ansis/-/ansis-4.2.0.tgz",
      "integrity": "sha512-HqZ5rWlFjGiV0tDm3UxxgNRqsOTniqoKZu0pIAfh7TZQMGuZK+hH0drySty0si0QXj1ieop4+SkSfPZBPPkHig==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha512-PCVAQswWemu6UdxsDFFX/+gVeYqKAod3D3UVm91jHwynguOwAvYPhx8nNlM++NqRcK6CxxpUafjmhIdKiHibqg==",
      "license": "MIT"
    },
    "node_modules/arrify": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/arrify/-/arrify-2.0.1.tgz",
      "integrity": "sha512-3duEwti880xqi4eAMN8AyR4a0ByT90zoYdLlevfrvU43vb0YZwZVfxOgxWrLXXXpyugL0hNZc9G6BiB5B3nUug==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ast-kit": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/ast-kit/-/ast-kit-2.2.0.tgz",
      "integrity": "sha512-m1Q/RaVOnTp9JxPX+F+Zn7IcLYMzM8kZofDImfsKZd8MbR+ikdOzTeztStWqfrqIxZnYWryyI9ePm3NGjnZgGw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.5",
        "pathe": "^2.0.3"
      },
      "engines": {
        "node": ">=20.19.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sxzz"
      }
    },
    "node_modules/async-retry": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/async-retry/-/async-retry-1.3.3.tgz",
      "integrity": "sha512-wfr/jstw9xNi/0teMHrRW7dsz3Lt5ARhYNZ2ewpadnhaIp5mbALhOAP+EAdsC7t4Z6wqsDVv9+W6gm1Dk9mEyw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "retry": "0.13.1"
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "devOptional": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/bignumber.js": {
      "version": "9.3.1",
      "resolved": "https://registry.npmjs.org/bignumber.js/-/bignumber.js-9.3.1.tgz",
      "integrity": "sha512-Ko0uX15oIUS7wJ3Rb30Fs6SkVbLmPBAKdlm7q9+ak9bbIeFf0MwuBsQV6z7+X768/cHsfg+WlysDWJcmthjsjQ==",
      "devOptional": true,
      "license": "MIT",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/birpc": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/birpc/-/birpc-4.0.0.tgz",
      "integrity": "sha512-LShSxJP0KTmd101b6DRyGBj57LZxSDYWKitQNW/mi8GRMvZb078Uf9+pveax1DrVL89vm7mWe+TovdI/UDOuPw==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/antfu"
      }
    },
    "node_modules/body-parser": {
      "version": "1.20.4",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.20.4.tgz",
      "integrity": "sha512-ZTgYYLMOXY9qKU/57FAo8F+HA2dGX7bqGc71txDRC1rS4frdFI5R7NhluHxH6M0YItAP0sHB4uqAOcYKxO6uGA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "~3.1.2",
        "content-type": "~1.0.5",
        "debug": "2.6.9",
        "depd": "2.0.0",
        "destroy": "~1.2.0",
        "http-errors": "~2.0.1",
        "iconv-lite": "~0.4.24",
        "on-finished": "~2.4.1",
        "qs": "~6.14.0",
        "raw-body": "~2.5.3",
        "type-is": "~1.6.18",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8",
        "npm": "1.2.8000 || >= 1.4.16"
      }
    },
    "node_modules/brace-expansion": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.2.tgz",
      "integrity": "sha512-Jt0vHyM+jmUBqojB7E1NIYadt0vI0Qxjxd2TErW94wDz+E2LAm5vKMXXwg6ZZBTHPuUlDgQHKXvjGBdfcF1ZDQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^1.0.0"
      }
    },
    "node_modules/buffer-equal-constant-time": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/buffer-equal-constant-time/-/buffer-equal-constant-time-1.0.1.tgz",
      "integrity": "sha512-zRpUiDwd/xk6ADqPMATG8vc9VPrkck7T07OIx0gnjmJAnHnTVXNQG3vfvWNuiZIkwu9KrKdA1iJKfsfTVxE6NA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/bytes": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
      "integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/cac": {
      "version": "6.7.14",
      "resolved": "https://registry.npmjs.org/cac/-/cac-6.7.14.tgz",
      "integrity": "sha512-b6Ilus+c3RrdDk+JhLKUAQfzzgLEPy6wcXqS7f/xe1EETvsDP6GORG7SFuOs6cID5YkqchW/LXZbX5bc8j7ZcQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/cliui": {
      "version": "8.0.1",
      "resolved": "https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz",
      "integrity": "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==",
      "license": "ISC",
      "optional": true,
      "dependencies": {
        "string-width": "^4.2.0",
        "strip-ansi": "^6.0.1",
        "wrap-ansi": "^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/cliui/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/cliui/node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/cliui/node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/cliui/node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/cliui/node_modules/wrap-ansi": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
      "integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "ansi-styles": "^4.0.0",
        "string-width": "^4.1.0",
        "strip-ansi": "^6.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "devOptional": true,
      "license": "MIT",
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
      "devOptional": true,
      "license": "MIT"
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/content-disposition": {
      "version": "0.5.4",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.4.tgz",
      "integrity": "sha512-FveZTNuGw04cxlAiWbzi6zTAL/lhehaWbTtgluJh4/E95DqMwTmha3KZN1aAWA8cFIhHzMZUvLevkw5Rqk+tSQ==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "5.2.1"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/content-type": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
      "integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz",
      "integrity": "sha512-yki5XnKuf750l50uGTllt6kKILY4nQ1eNIQatoXEByZ5dWgnKqbnqmTrBE5B4N7lrMJKQ2ytWMiTO2o0v6Ew/w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie-signature": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.7.tgz",
      "integrity": "sha512-NXdYc3dLr47pBkpUCHtKSwIOQXLVn8dZEuywboCOJY/osA0wFSLlSawr3KN8qXJEyX66FcONTH8EIlVuK0yyFA==",
      "license": "MIT"
    },
    "node_modules/cors": {
      "version": "2.8.5",
      "resolved": "https://registry.npmjs.org/cors/-/cors-2.8.5.tgz",
      "integrity": "sha512-KIHbLJqu73RGr/hnbrO9uBeixNGuvSQjul/jdFvS/KFSIH1hWVd1ng7zOHx+YrEfInLG7q4n6GHQ9cDtxv/P6g==",
      "license": "MIT",
      "dependencies": {
        "object-assign": "^4",
        "vary": "^1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/cross-spawn": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
      "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/data-uri-to-buffer": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/data-uri-to-buffer/-/data-uri-to-buffer-4.0.1.tgz",
      "integrity": "sha512-0R9ikRb668HB7QDxT1vkpuUBtqc53YyAwMwGeUFKRojY/NWKvdZ+9UYtRfGmhqNbRkTSVpMbmyhXipFFv2cb/A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 12"
      }
    },
    "node_modules/debug": {
      "version": "2.6.9",
      "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
      "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
      "license": "MIT",
      "dependencies": {
        "ms": "2.0.0"
      }
    },
    "node_modules/defu": {
      "version": "6.1.4",
      "resolved": "https://registry.npmjs.org/defu/-/defu-6.1.4.tgz",
      "integrity": "sha512-mEQCMmwJu317oSz8CwdIOdwf3xMif1ttiM8LTufzc3g6kR+9Pe236twL8j3IYT1F7GfRgGcW6MWxzZjLIkuHIg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/depd": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
      "integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/destroy": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.2.0.tgz",
      "integrity": "sha512-2sJGJTaXIIaR1w4iJSNoN0hnMY7Gpc/n8D4qSCJw8QqFWXf7cuAgnEHxBpweaVcPevC2l3KpjYCx3NypQQgaJg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8",
        "npm": "1.2.8000 || >= 1.4.16"
      }
    },
    "node_modules/dts-resolver": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/dts-resolver/-/dts-resolver-2.1.3.tgz",
      "integrity": "sha512-bihc7jPC90VrosXNzK0LTE2cuLP6jr0Ro8jk+kMugHReJVLIpHz/xadeq3MhuwyO4TD4OA3L1Q8pBBFRc08Tsw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=20.19.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sxzz"
      },
      "peerDependencies": {
        "oxc-resolver": ">=11.0.0"
      },
      "peerDependenciesMeta": {
        "oxc-resolver": {
          "optional": true
        }
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/duplexify": {
      "version": "4.1.3",
      "resolved": "https://registry.npmjs.org/duplexify/-/duplexify-4.1.3.tgz",
      "integrity": "sha512-M3BmBhwJRZsSx38lZyhE53Csddgzl5R7xGJNk7CVddZD6CcmwMCH8J+7AprIrQKH7TonKxaCjcv27Qmf+sQ+oA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "end-of-stream": "^1.4.1",
        "inherits": "^2.0.3",
        "readable-stream": "^3.1.1",
        "stream-shift": "^1.0.2"
      }
    },
    "node_modules/eastasianwidth": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/eastasianwidth/-/eastasianwidth-0.2.0.tgz",
      "integrity": "sha512-I88TYZWc9XiYHRQ4/3c5rjjfgkjhLyW2luGIheGERbNQ6OY7yTybanSpDXZa8y7VUP9YmDcYa+eyq4ca7iLqWA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/ecdsa-sig-formatter": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/ecdsa-sig-formatter/-/ecdsa-sig-formatter-1.0.11.tgz",
      "integrity": "sha512-nagl3RYrbNv6kQkeJIpt6NJZy8twLB/2vtz6yN9Z4vRKHN4/QZJIEbqohALSgwKdnksuY3k5Addp5lg8sVoVcQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
      "license": "MIT"
    },
    "node_modules/emoji-regex": {
      "version": "9.2.2",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-9.2.2.tgz",
      "integrity": "sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/empathic": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/empathic/-/empathic-2.0.0.tgz",
      "integrity": "sha512-i6UzDscO/XfAcNYD75CfICkmfLedpyPDdozrLMmQc5ORaQcdMoc21OnlEylMIqI7U8eniKrPMxxtj8k0vhmJhA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/encodeurl": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
      "integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/end-of-stream": {
      "version": "1.4.5",
      "resolved": "https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.5.tgz",
      "integrity": "sha512-ooEGc6HP26xXq/N+GCGOT0JKCLDGrq2bQUZrQ7gyrJiZANJ/8YDTxTpQBXGMn+WbIQXNVpyWymm7KYVICQnyOg==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "once": "^1.4.0"
      }
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
      "integrity": "sha512-FGgH2h8zKNim9ljj7dankFPcICIK9Cp5bm+c2gQSYePhpaG5+esrLODihIorn+Pe6FGJzWhXQotPv73jTaldXA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-set-tostringtag": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
      "integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow==",
      "license": "MIT"
    },
    "node_modules/etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/event-target-shim": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/event-target-shim/-/event-target-shim-5.0.1.tgz",
      "integrity": "sha512-i/2XbnSz/uxRCU6+NdVJgKWDTM427+MqYbkQzD321DuCQJUqOuJKIA0IM2+W2xtYHdKOmZ4dR6fExsd4SXL+WQ==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/express": {
      "version": "4.22.1",
      "resolved": "https://registry.npmjs.org/express/-/express-4.22.1.tgz",
      "integrity": "sha512-F2X8g9P1X7uCPZMA3MVf9wcTqlyNp7IhH5qPCI0izhaOIYXaW9L535tGA3qmjRzpH+bZczqq7hVKxTR4NWnu+g==",
      "license": "MIT",
      "dependencies": {
        "accepts": "~1.3.8",
        "array-flatten": "1.1.1",
        "body-parser": "~1.20.3",
        "content-disposition": "~0.5.4",
        "content-type": "~1.0.4",
        "cookie": "~0.7.1",
        "cookie-signature": "~1.0.6",
        "debug": "2.6.9",
        "depd": "2.0.0",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "~1.3.1",
        "fresh": "~0.5.2",
        "http-errors": "~2.0.0",
        "merge-descriptors": "1.0.3",
        "methods": "~1.1.2",
        "on-finished": "~2.4.1",
        "parseurl": "~1.3.3",
        "path-to-regexp": "~0.1.12",
        "proxy-addr": "~2.0.7",
        "qs": "~6.14.0",
        "range-parser": "~1.2.1",
        "safe-buffer": "5.2.1",
        "send": "~0.19.0",
        "serve-static": "~1.16.2",
        "setprototypeof": "1.2.0",
        "statuses": "~2.0.1",
        "type-is": "~1.6.18",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
      },
      "engines": {
        "node": ">= 0.10.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/extend": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
      "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==",
      "devOptional": true,
      "license": "MIT"
    },
    "node_modules/farmhash-modern": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/farmhash-modern/-/farmhash-modern-1.1.0.tgz",
      "integrity": "sha512-6ypT4XfgqJk/F3Yuv4SX26I3doUjt0GTG4a+JgWxXQpxXzTBq8fPUeGHfcYMMDPHJHm3yPOSjaeBwBGAHWXCdA==",
      "license": "MIT",
      "engines": {
        "node": ">=18.0.0"
      }
    },
    "node_modules/fast-deep-equal": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
      "integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/fast-xml-parser": {
      "version": "4.5.3",
      "resolved": "https://registry.npmjs.org/fast-xml-parser/-/fast-xml-parser-4.5.3.tgz",
      "integrity": "sha512-RKihhV+SHsIUGXObeVy9AXiBbFwkVk7Syp8XgwN5U3JV416+Gwp/GO9i0JYKmikykgz/UHRrrV4ROuZEo/T0ig==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/NaturalIntelligence"
        }
      ],
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "strnum": "^1.1.1"
      },
      "bin": {
        "fxparser": "src/cli/cli.js"
      }
    },
    "node_modules/faye-websocket": {
      "version": "0.11.4",
      "resolved": "https://registry.npmjs.org/faye-websocket/-/faye-websocket-0.11.4.tgz",
      "integrity": "sha512-CzbClwlXAuiRQAlUyfqPgvPoNKTckTPGfwZV4ZdAhVcP2lh9KUxJg2b5GkE7XbjKQ3YJnQ9z6D9ntLAlB+tP8g==",
      "license": "Apache-2.0",
      "dependencies": {
        "websocket-driver": ">=0.5.1"
      },
      "engines": {
        "node": ">=0.8.0"
      }
    },
    "node_modules/fetch-blob": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/fetch-blob/-/fetch-blob-3.2.0.tgz",
      "integrity": "sha512-7yAQpD2UMJzLi1Dqv7qFYnPbaPx7ZfFK6PiIxQ4PfkGPyNyl2Ugx+a/umUonmKqjhM4DnfbMvdX6otXq83soQQ==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/jimmywarting"
        },
        {
          "type": "paypal",
          "url": "https://paypal.me/jimmywarting"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "node-domexception": "^1.0.0",
        "web-streams-polyfill": "^3.0.3"
      },
      "engines": {
        "node": "^12.20 || >= 14.13"
      }
    },
    "node_modules/finalhandler": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.3.2.tgz",
      "integrity": "sha512-aA4RyPcd3badbdABGDuTXCMTtOneUCAYH/gxoYRTZlIJdF0YPWuGqiAsIrhNnnqdXGswYk6dGujem4w80UJFhg==",
      "license": "MIT",
      "dependencies": {
        "debug": "2.6.9",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "on-finished": "~2.4.1",
        "parseurl": "~1.3.3",
        "statuses": "~2.0.2",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/firebase-admin": {
      "version": "12.7.0",
      "resolved": "https://registry.npmjs.org/firebase-admin/-/firebase-admin-12.7.0.tgz",
      "integrity": "sha512-raFIrOyTqREbyXsNkSHyciQLfv8AUZazehPaQS1lZBSCDYW74FYXU0nQZa3qHI4K+hawohlDbywZ4+qce9YNxA==",
      "license": "Apache-2.0",
      "dependencies": {
        "@fastify/busboy": "^3.0.0",
        "@firebase/database-compat": "1.0.8",
        "@firebase/database-types": "1.0.5",
        "@types/node": "^22.0.1",
        "farmhash-modern": "^1.1.0",
        "jsonwebtoken": "^9.0.0",
        "jwks-rsa": "^3.1.0",
        "node-forge": "^1.3.1",
        "uuid": "^10.0.0"
      },
      "engines": {
        "node": ">=14"
      },
      "optionalDependencies": {
        "@google-cloud/firestore": "^7.7.0",
        "@google-cloud/storage": "^7.7.0"
      }
    },
    "node_modules/firebase-functions": {
      "version": "6.6.0",
      "resolved": "https://registry.npmjs.org/firebase-functions/-/firebase-functions-6.6.0.tgz",
      "integrity": "sha512-wwfo6JF+N7HUExVs5gUFgkgVGHDEog9O+qtouh7IuJWk8TBQ+KwXEgRiXbatSj7EbTu3/yYnHuzh3XExbfF6wQ==",
      "license": "MIT",
      "dependencies": {
        "@types/cors": "^2.8.5",
        "@types/express": "^4.17.21",
        "cors": "^2.8.5",
        "express": "^4.21.0",
        "protobufjs": "^7.2.2"
      },
      "bin": {
        "firebase-functions": "lib/bin/firebase-functions.js"
      },
      "engines": {
        "node": ">=14.10.0"
      },
      "peerDependencies": {
        "firebase-admin": "^11.10.0 || ^12.0.0 || ^13.0.0"
      }
    },
    "node_modules/foreground-child": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/foreground-child/-/foreground-child-3.3.1.tgz",
      "integrity": "sha512-gIXjKqtFuWEgzFRJA9WCQeSJLZDjgJUOMCMzxtvFq/37KojM1BFGufqsCy0r4qSQmYLsZYMeyRqzIWOMup03sw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "cross-spawn": "^7.0.6",
        "signal-exit": "^4.0.1"
      },
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/form-data": {
      "version": "2.5.5",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-2.5.5.tgz",
      "integrity": "sha512-jqdObeR2rxZZbPSGL+3VckHMYtu+f9//KXBsVny6JSX/pa38Fy+bGjuG8eW/H6USNQWhLi8Num++cU2yOCNz4A==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.8",
        "es-set-tostringtag": "^2.1.0",
        "hasown": "^2.0.2",
        "mime-types": "^2.1.35",
        "safe-buffer": "^5.2.1"
      },
      "engines": {
        "node": ">= 0.12"
      }
    },
    "node_modules/formdata-polyfill": {
      "version": "4.0.10",
      "resolved": "https://registry.npmjs.org/formdata-polyfill/-/formdata-polyfill-4.0.10.tgz",
      "integrity": "sha512-buewHzMvYL29jdeQTVILecSaZKnt/RJWjoZCF5OW60Z67/GmSLBkOFM7qh1PI3zFNtJbaZL5eQu1vLfazOwj4g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fetch-blob": "^3.1.2"
      },
      "engines": {
        "node": ">=12.20.0"
      }
    },
    "node_modules/forwarded": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz",
      "integrity": "sha512-buRG0fpBtRHSTCOASe6hD258tEubFoRLb4ZNA6NxMVHNw2gOcwHo9wyablzMzOA5z9xA9L1KNjk/Nt6MT9aYow==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/fresh": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
      "integrity": "sha512-zJ2mQYM18rEFOudeV4GShTGIQ7RbzA7ozbU9I/XBpm7kqgMywgmylMwXHxZJmkVoYkna9d2pVXVXPdYTP9ej8Q==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/functional-red-black-tree": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/functional-red-black-tree/-/functional-red-black-tree-1.0.1.tgz",
      "integrity": "sha512-dsKNQNdj6xA3T+QlADDA7mOSlX0qiMINjn0cgr+eGHGsbSHzTabcIogz2+p/iqP1Xs6EP/sS2SbqH+brGTbq0g==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/gaxios": {
      "version": "6.7.1",
      "resolved": "https://registry.npmjs.org/gaxios/-/gaxios-6.7.1.tgz",
      "integrity": "sha512-LDODD4TMYx7XXdpwxAVRAIAuB0bzv0s+ywFonY46k126qzQHT9ygyoa9tncmOiQmmDrik65UYsEkv3lbfqQ3yQ==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "extend": "^3.0.2",
        "https-proxy-agent": "^7.0.1",
        "is-stream": "^2.0.0",
        "node-fetch": "^2.6.9",
        "uuid": "^9.0.1"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/gaxios/node_modules/uuid": {
      "version": "9.0.1",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-9.0.1.tgz",
      "integrity": "sha512-b+1eJOlsR9K8HJpow9Ok3fiWOWSIcIzXodvv0rQjVoOVNpWMpxf1wZNpt4y9h10odCNrqnYp1OBzRktckBe3sA==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "license": "MIT",
      "optional": true,
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    },
    "node_modules/gcp-metadata": {
      "version": "6.1.1",
      "resolved": "https://registry.npmjs.org/gcp-metadata/-/gcp-metadata-6.1.1.tgz",
      "integrity": "sha512-a4tiq7E0/5fTjxPAaH4jpjkSv/uCaU2p5KC6HVGrvl0cDjA8iBZv4vv1gyzlmK0ZUKqwpOyQMKzZQe3lTit77A==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "gaxios": "^6.1.1",
        "google-logging-utils": "^0.0.2",
        "json-bigint": "^1.0.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/get-caller-file": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz",
      "integrity": "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==",
      "license": "ISC",
      "optional": true,
      "engines": {
        "node": "6.* || 8.* || >= 10.*"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/get-tsconfig": {
      "version": "4.13.0",
      "resolved": "https://registry.npmjs.org/get-tsconfig/-/get-tsconfig-4.13.0.tgz",
      "integrity": "sha512-1VKTZJCwBrvbd+Wn3AOgQP/2Av+TfTCOlE4AcRJE72W1ksZXbAx8PPBR9RzgTeSPzlPMHrbANMH3LbltH73wxQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "resolve-pkg-maps": "^1.0.0"
      },
      "funding": {
        "url": "https://github.com/privatenumber/get-tsconfig?sponsor=1"
      }
    },
    "node_modules/glob": {
      "version": "10.5.0",
      "resolved": "https://registry.npmjs.org/glob/-/glob-10.5.0.tgz",
      "integrity": "sha512-DfXN8DfhJ7NH3Oe7cFmu3NCu1wKbkReJ8TorzSAFbSKrlNaQSKfIzqYqVY8zlbs2NLBbWpRiU52GX2PbaBVNkg==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "foreground-child": "^3.1.0",
        "jackspeak": "^3.1.2",
        "minimatch": "^9.0.4",
        "minipass": "^7.1.2",
        "package-json-from-dist": "^1.0.0",
        "path-scurry": "^1.11.1"
      },
      "bin": {
        "glob": "dist/esm/bin.mjs"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/google-auth-library": {
      "version": "9.15.1",
      "resolved": "https://registry.npmjs.org/google-auth-library/-/google-auth-library-9.15.1.tgz",
      "integrity": "sha512-Jb6Z0+nvECVz+2lzSMt9u98UsoakXxA2HGHMCxh+so3n90XgYWkq5dur19JAJV7ONiJY22yBTyJB1TSkvPq9Ng==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "base64-js": "^1.3.0",
        "ecdsa-sig-formatter": "^1.0.11",
        "gaxios": "^6.1.1",
        "gcp-metadata": "^6.1.0",
        "gtoken": "^7.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/google-gax": {
      "version": "4.6.1",
      "resolved": "https://registry.npmjs.org/google-gax/-/google-gax-4.6.1.tgz",
      "integrity": "sha512-V6eky/xz2mcKfAd1Ioxyd6nmA61gao3n01C+YeuIwu3vzM9EDR6wcVzMSIbLMDXWeoi9SHYctXuKYC5uJUT3eQ==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "@grpc/grpc-js": "^1.10.9",
        "@grpc/proto-loader": "^0.7.13",
        "@types/long": "^4.0.0",
        "abort-controller": "^3.0.0",
        "duplexify": "^4.0.0",
        "google-auth-library": "^9.3.0",
        "node-fetch": "^2.7.0",
        "object-hash": "^3.0.0",
        "proto3-json-serializer": "^2.0.2",
        "protobufjs": "^7.3.2",
        "retry-request": "^7.0.0",
        "uuid": "^9.0.1"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/google-gax/node_modules/uuid": {
      "version": "9.0.1",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-9.0.1.tgz",
      "integrity": "sha512-b+1eJOlsR9K8HJpow9Ok3fiWOWSIcIzXodvv0rQjVoOVNpWMpxf1wZNpt4y9h10odCNrqnYp1OBzRktckBe3sA==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "license": "MIT",
      "optional": true,
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    },
    "node_modules/google-logging-utils": {
      "version": "0.0.2",
      "resolved": "https://registry.npmjs.org/google-logging-utils/-/google-logging-utils-0.0.2.tgz",
      "integrity": "sha512-NEgUnEcBiP5HrPzufUkBzJOD/Sxsco3rLNo1F1TNf7ieU8ryUzBhqba8r756CjLX7rn3fHl6iLEwPYuqpoKgQQ==",
      "license": "Apache-2.0",
      "optional": true,
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gtoken": {
      "version": "7.1.0",
      "resolved": "https://registry.npmjs.org/gtoken/-/gtoken-7.1.0.tgz",
      "integrity": "sha512-pCcEwRi+TKpMlxAQObHDQ56KawURgyAf6jtIY046fJ5tIv3zDe/LEIubckAO8fj6JnAxLdmWkUfNyulQ2iKdEw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "gaxios": "^6.0.0",
        "jws": "^4.0.0"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-tostringtag": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
      "integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "has-symbols": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz",
      "integrity": "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ==",
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/hookable": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/hookable/-/hookable-6.0.1.tgz",
      "integrity": "sha512-uKGyY8BuzN/a5gvzvA+3FVWo0+wUjgtfSdnmjtrOVwQCZPHpHDH2WRO3VZSOeluYrHoDCiXFffZXs8Dj1ULWtw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/html-entities": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/html-entities/-/html-entities-2.6.0.tgz",
      "integrity": "sha512-kig+rMn/QOVRvr7c86gQ8lWXq+Hkv6CbAH1hLu+RG338StTpE8Z0b44SDVaqVu7HGKf27frdmUYEs9hTUX/cLQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/mdevils"
        },
        {
          "type": "patreon",
          "url": "https://patreon.com/mdevils"
        }
      ],
      "license": "MIT",
      "optional": true
    },
    "node_modules/http-errors": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-2.0.1.tgz",
      "integrity": "sha512-4FbRdAX+bSdmo4AUFuS0WNiPz8NgFt+r8ThgNWmlrjQjt1Q7ZR9+zTlce2859x4KSXrwIsaeTqDoKQmtP8pLmQ==",
      "license": "MIT",
      "dependencies": {
        "depd": "~2.0.0",
        "inherits": "~2.0.4",
        "setprototypeof": "~1.2.0",
        "statuses": "~2.0.2",
        "toidentifier": "~1.0.1"
      },
      "engines": {
        "node": ">= 0.8"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/http-parser-js": {
      "version": "0.5.10",
      "resolved": "https://registry.npmjs.org/http-parser-js/-/http-parser-js-0.5.10.tgz",
      "integrity": "sha512-Pysuw9XpUq5dVc/2SMHpuTY01RFl8fttgcyunjL7eEMhGM3cI4eOmiCycJDVCo/7O7ClfQD3SaI6ftDzqOXYMA==",
      "license": "MIT"
    },
    "node_modules/http-proxy-agent": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-5.0.0.tgz",
      "integrity": "sha512-n2hY8YdoRE1i7r6M0w9DIw5GgZN0G25P8zLCRQ8rjXtTU3vsNFBI/vWK/UIeE6g5MUUz6avwAPXmL6Fy9D/90w==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@tootallnate/once": "2",
        "agent-base": "6",
        "debug": "4"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/http-proxy-agent/node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/http-proxy-agent/node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/http-proxy-agent/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/https-proxy-agent": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-7.0.6.tgz",
      "integrity": "sha512-vK9P5/iUfdl95AI+JVyUuIcVtd4ofvtrOr3HNtM2yxC9bnMbEdp3x01OhQNnjb8IJYi38VlTE3mBXwcfvywuSw==",
      "devOptional": true,
      "license": "MIT",
      "dependencies": {
        "agent-base": "^7.1.2",
        "debug": "4"
      },
      "engines": {
        "node": ">= 14"
      }
    },
    "node_modules/https-proxy-agent/node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "devOptional": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/https-proxy-agent/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "devOptional": true,
      "license": "MIT"
    },
    "node_modules/iconv-lite": {
      "version": "0.4.24",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
      "integrity": "sha512-v3MXnZAcvnywkTUEZomIActle7RXXeedOR31wwl7VlyoXO4Qi9arvSenNQWne1TcRwhCL1HwLI21bEqdpj8/rA==",
      "license": "MIT",
      "dependencies": {
        "safer-buffer": ">= 2.1.2 < 3"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/import-without-cache": {
      "version": "0.2.5",
      "resolved": "https://registry.npmjs.org/import-without-cache/-/import-without-cache-0.2.5.tgz",
      "integrity": "sha512-B6Lc2s6yApwnD2/pMzFh/d5AVjdsDXjgkeJ766FmFuJELIGHNycKRj+l3A39yZPM4CchqNCB4RITEAYB1KUM6A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=20.19.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sxzz"
      }
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "license": "ISC"
    },
    "node_modules/ipaddr.js": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
      "integrity": "sha512-0KI/607xoxSToH7GjN1FfSbLoU0+btTicjsQSWQlh/hZykN8KpmMf7uYwPW3R+akZ6R/w18ZlXSHBYXiYUPO3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/is-fullwidth-code-point": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
      "integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
      "devOptional": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-stream": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-2.0.1.tgz",
      "integrity": "sha512-hFoiJiTl63nn+kstHGBtewWSKnQLpyb155KHheA1l39uvtO9nWIop1p3udqPcUd/xbF1VLMO4n7OI6p7RbngDg==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/isexe": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz",
      "integrity": "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/jackspeak": {
      "version": "3.4.3",
      "resolved": "https://registry.npmjs.org/jackspeak/-/jackspeak-3.4.3.tgz",
      "integrity": "sha512-OGlZQpz2yfahA/Rd1Y8Cd9SIEsqvXkLVoSw/cgwhnhFMDbsQFeZYoJJ7bIZBS9BcamUW96asq/npPWugM+RQBw==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "dependencies": {
        "@isaacs/cliui": "^8.0.2"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      },
      "optionalDependencies": {
        "@pkgjs/parseargs": "^0.11.0"
      }
    },
    "node_modules/jose": {
      "version": "4.15.9",
      "resolved": "https://registry.npmjs.org/jose/-/jose-4.15.9.tgz",
      "integrity": "sha512-1vUQX+IdDMVPj4k8kOxgUqlcK518yluMuGZwqlr44FS1ppZB/5GWh4rZG89erpOBOJjU/OBsnCVFfapsRz6nEA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/panva"
      }
    },
    "node_modules/jsesc": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
      "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jsesc": "bin/jsesc"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/json-bigint": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/json-bigint/-/json-bigint-1.0.0.tgz",
      "integrity": "sha512-SiPv/8VpZuWbvLSMtTDU8hEfrZWg/mH/nV/b4o0CYbSxu1UIQPLdwKOCIyLQX+VIPO5vrLX3i8qtqFyhdPSUSQ==",
      "devOptional": true,
      "license": "MIT",
      "dependencies": {
        "bignumber.js": "^9.0.0"
      }
    },
    "node_modules/jsonwebtoken": {
      "version": "9.0.3",
      "resolved": "https://registry.npmjs.org/jsonwebtoken/-/jsonwebtoken-9.0.3.tgz",
      "integrity": "sha512-MT/xP0CrubFRNLNKvxJ2BYfy53Zkm++5bX9dtuPbqAeQpTVe0MQTFhao8+Cp//EmJp244xt6Drw/GVEGCUj40g==",
      "license": "MIT",
      "dependencies": {
        "jws": "^4.0.1",
        "lodash.includes": "^4.3.0",
        "lodash.isboolean": "^3.0.3",
        "lodash.isinteger": "^4.0.4",
        "lodash.isnumber": "^3.0.3",
        "lodash.isplainobject": "^4.0.6",
        "lodash.isstring": "^4.0.1",
        "lodash.once": "^4.0.0",
        "ms": "^2.1.1",
        "semver": "^7.5.4"
      },
      "engines": {
        "node": ">=12",
        "npm": ">=6"
      }
    },
    "node_modules/jsonwebtoken/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/jsonwebtoken/node_modules/semver": {
      "version": "7.7.3",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.7.3.tgz",
      "integrity": "sha512-SdsKMrI9TdgjdweUSR9MweHA4EJ8YxHn8DFaDisvhVlUOe4BF1tLD7GAj0lIqWVl+dPb/rExr0Btby5loQm20Q==",
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/jwa": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/jwa/-/jwa-2.0.1.tgz",
      "integrity": "sha512-hRF04fqJIP8Abbkq5NKGN0Bbr3JxlQ+qhZufXVr0DvujKy93ZCbXZMHDL4EOtodSbCWxOqR8MS1tXA5hwqCXDg==",
      "license": "MIT",
      "dependencies": {
        "buffer-equal-constant-time": "^1.0.1",
        "ecdsa-sig-formatter": "1.0.11",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/jwks-rsa": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/jwks-rsa/-/jwks-rsa-3.2.0.tgz",
      "integrity": "sha512-PwchfHcQK/5PSydeKCs1ylNym0w/SSv8a62DgHJ//7x2ZclCoinlsjAfDxAAbpoTPybOum/Jgy+vkvMmKz89Ww==",
      "license": "MIT",
      "dependencies": {
        "@types/express": "^4.17.20",
        "@types/jsonwebtoken": "^9.0.4",
        "debug": "^4.3.4",
        "jose": "^4.15.4",
        "limiter": "^1.1.5",
        "lru-memoizer": "^2.2.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/jwks-rsa/node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/jwks-rsa/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/jws": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/jws/-/jws-4.0.1.tgz",
      "integrity": "sha512-EKI/M/yqPncGUUh44xz0PxSidXFr/+r0pA70+gIYhjv+et7yxM+s29Y+VGDkovRofQem0fs7Uvf4+YmAdyRduA==",
      "license": "MIT",
      "dependencies": {
        "jwa": "^2.0.1",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/limiter": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/limiter/-/limiter-1.1.5.tgz",
      "integrity": "sha512-FWWMIEOxz3GwUI4Ts/IvgVy6LPvoMPgjMdQ185nN6psJyBJ4yOpzqm695/h5umdLJg2vW3GR5iG11MAkR2AzJA=="
    },
    "node_modules/lodash.camelcase": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-4.3.0.tgz",
      "integrity": "sha512-TwuEnCnxbc3rAvhf/LbG7tJUDzhqXyFnv3dtzLOPgCG/hODL7WFnsbwktkD7yUV0RrreP/l1PALq/YSg6VvjlA==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/lodash.clonedeep": {
      "version": "4.5.0",
      "resolved": "https://registry.npmjs.org/lodash.clonedeep/-/lodash.clonedeep-4.5.0.tgz",
      "integrity": "sha512-H5ZhCF25riFd9uB5UCkVKo61m3S/xZk1x4wA6yp/L3RFP6Z/eHH1ymQcGLo7J3GMPfm0V/7m1tryHuGVxpqEBQ==",
      "license": "MIT"
    },
    "node_modules/lodash.includes": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/lodash.includes/-/lodash.includes-4.3.0.tgz",
      "integrity": "sha512-W3Bx6mdkRTGtlJISOvVD/lbqjTlPPUDTMnlXZFnVwi9NKJ6tiAk6LVdlhZMm17VZisqhKcgzpO5Wz91PCt5b0w==",
      "license": "MIT"
    },
    "node_modules/lodash.isboolean": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/lodash.isboolean/-/lodash.isboolean-3.0.3.tgz",
      "integrity": "sha512-Bz5mupy2SVbPHURB98VAcw+aHh4vRV5IPNhILUCsOzRmsTmSQ17jIuqopAentWoehktxGd9e/hbIXq980/1QJg==",
      "license": "MIT"
    },
    "node_modules/lodash.isinteger": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/lodash.isinteger/-/lodash.isinteger-4.0.4.tgz",
      "integrity": "sha512-DBwtEWN2caHQ9/imiNeEA5ys1JoRtRfY3d7V9wkqtbycnAmTvRRmbHKDV4a0EYc678/dia0jrte4tjYwVBaZUA==",
      "license": "MIT"
    },
    "node_modules/lodash.isnumber": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/lodash.isnumber/-/lodash.isnumber-3.0.3.tgz",
      "integrity": "sha512-QYqzpfwO3/CWf3XP+Z+tkQsfaLL/EnUlXWVkIk5FUPc4sBdTehEqZONuyRt2P67PXAk+NXmTBcc97zw9t1FQrw==",
      "license": "MIT"
    },
    "node_modules/lodash.isplainobject": {
      "version": "4.0.6",
      "resolved": "https://registry.npmjs.org/lodash.isplainobject/-/lodash.isplainobject-4.0.6.tgz",
      "integrity": "sha512-oSXzaWypCMHkPC3NvBEaPHf0KsA5mvPrOPgQWDsbg8n7orZ290M0BmC/jgRZ4vcJ6DTAhjrsSYgdsW/F+MFOBA==",
      "license": "MIT"
    },
    "node_modules/lodash.isstring": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/lodash.isstring/-/lodash.isstring-4.0.1.tgz",
      "integrity": "sha512-0wJxfxH1wgO3GrbuP+dTTk7op+6L41QCXbGINEmD+ny/G/eCqGzxyCsh7159S+mgDDcoarnBw6PC1PS5+wUGgw==",
      "license": "MIT"
    },
    "node_modules/lodash.once": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/lodash.once/-/lodash.once-4.1.1.tgz",
      "integrity": "sha512-Sb487aTOCr9drQVL8pIxOzVhafOjZN9UU54hiN8PU3uAiSV7lx1yYNpbNmex2PK6dSJoNTSJUUswT651yww3Mg==",
      "license": "MIT"
    },
    "node_modules/long": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/long/-/long-5.3.2.tgz",
      "integrity": "sha512-mNAgZ1GmyNhD7AuqnTG3/VQ26o760+ZYBPKjPvugO8+nLbYfX6TVpJPseBvopbdY+qpZ/lKUnmEc1LeZYS3QAA==",
      "license": "Apache-2.0"
    },
    "node_modules/lru-memoizer": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/lru-memoizer/-/lru-memoizer-2.3.0.tgz",
      "integrity": "sha512-GXn7gyHAMhO13WSKrIiNfztwxodVsP8IoZ3XfrJV4yH2x0/OeTO/FIaAHTY5YekdGgW94njfuKmyyt1E0mR6Ug==",
      "license": "MIT",
      "dependencies": {
        "lodash.clonedeep": "^4.5.0",
        "lru-cache": "6.0.0"
      }
    },
    "node_modules/lru-memoizer/node_modules/lru-cache": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz",
      "integrity": "sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==",
      "license": "ISC",
      "dependencies": {
        "yallist": "^4.0.0"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/lru-memoizer/node_modules/yallist": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz",
      "integrity": "sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==",
      "license": "ISC"
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/media-typer": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
      "integrity": "sha512-dq+qelQ9akHpcOl/gUVRTxVIOkAJ1wR3QAvb4RsVjS8oVoFjDGTc679wJYmUmknUF5HwMLOgb5O+a3KxfWapPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/merge-descriptors": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.3.tgz",
      "integrity": "sha512-gaNvAS7TZ897/rVaZ0nMtAyxNyi/pdbjbAwUpFQpN70GqnVfOiXpeUUMKRBmzXaSQ8DdTX4/0ms62r2K+hE6mQ==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/methods": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
      "integrity": "sha512-iclAHeNqNm68zFtnZ0e+1L2yUIdvzNoauKU4WBA3VvH/vPFieF7qfRlwUZU+DA9P9bPXIS90ulxoUoCH23sV2w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/mime/-/mime-3.0.0.tgz",
      "integrity": "sha512-jSCU7/VB1loIWBZe14aEYHU/+1UMEHoaO7qxCOVJOw9GgH72VAWppxNcjU+x9a2k3GSIBXNKxXQFqRvvZ7vr3A==",
      "license": "MIT",
      "optional": true,
      "bin": {
        "mime": "cli.js"
      },
      "engines": {
        "node": ">=10.0.0"
      }
    },
    "node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/minimatch": {
      "version": "9.0.5",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-9.0.5.tgz",
      "integrity": "sha512-G6T0ZX48xgozx7587koeX9Ys2NYy6Gmv//P89sEte9V9whIapMNF4idKxnW2QtCcLiTWlb/wfCabAtAFWhhBow==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "brace-expansion": "^2.0.1"
      },
      "engines": {
        "node": ">=16 || 14 >=14.17"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/minipass": {
      "version": "7.1.2",
      "resolved": "https://registry.npmjs.org/minipass/-/minipass-7.1.2.tgz",
      "integrity": "sha512-qOOzS1cBTWYF4BH8fVePDBOO9iptMnGUEZwNc/cMWnTV2nVLZ7VoNWEPHkYczZA0pdoA7dl6e7FL659nX9S2aw==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": ">=16 || 14 >=14.17"
      }
    },
    "node_modules/ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
      "license": "MIT"
    },
    "node_modules/nanoid": {
      "version": "5.1.6",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-5.1.6.tgz",
      "integrity": "sha512-c7+7RQ+dMB5dPwwCp4ee1/iV/q2P6aK1mTZcfr1BTuVlyW9hJYiMPybJCcnBlQtuSmTIWNeazm/zqNoZSSElBg==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.js"
      },
      "engines": {
        "node": "^18 || >=20"
      }
    },
    "node_modules/negotiator": {
      "version": "0.6.3",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz",
      "integrity": "sha512-+EUsqGPLsM+j/zdChZjsnX51g4XrHFOIXwfnCVPGlQk/k5giakcKsuxCObBRu6DSm9opw/O6slWbJdghQM4bBg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/node-domexception": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/node-domexception/-/node-domexception-1.0.0.tgz",
      "integrity": "sha512-/jKZoMpw0F8GRwl4/eLROPA3cfcXtLApP0QzLmUT/HuPCZWyB7IY9ZrMeKw2O/nFIqPQB3PVM9aYm0F312AXDQ==",
      "deprecated": "Use your platform's native DOMException instead",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/jimmywarting"
        },
        {
          "type": "github",
          "url": "https://paypal.me/jimmywarting"
        }
      ],
      "license": "MIT",
      "engines": {
        "node": ">=10.5.0"
      }
    },
    "node_modules/node-fetch": {
      "version": "2.7.0",
      "resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-2.7.0.tgz",
      "integrity": "sha512-c4FRfUm/dbcWZ7U+1Wq0AwCyFL+3nt2bEw05wfxSz+DWpWsitgmSgYmy2dQdWyKC1694ELPqMs/YzUSNozLt8A==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "whatwg-url": "^5.0.0"
      },
      "engines": {
        "node": "4.x || >=6.0.0"
      },
      "peerDependencies": {
        "encoding": "^0.1.0"
      },
      "peerDependenciesMeta": {
        "encoding": {
          "optional": true
        }
      }
    },
    "node_modules/node-forge": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/node-forge/-/node-forge-1.3.3.tgz",
      "integrity": "sha512-rLvcdSyRCyouf6jcOIPe/BgwG/d7hKjzMKOas33/pHEr6gbq18IK9zV7DiPvzsz0oBJPme6qr6H6kGZuI9/DZg==",
      "license": "(BSD-3-Clause OR GPL-2.0)",
      "engines": {
        "node": ">= 6.13.0"
      }
    },
    "node_modules/object-assign": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
      "integrity": "sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/object-hash": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/object-hash/-/object-hash-3.0.0.tgz",
      "integrity": "sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/object-inspect": {
      "version": "1.13.4",
      "resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz",
      "integrity": "sha512-W67iLl4J2EXEGTbfeHCffrjDfitvLANg0UlX3wFUUSTx92KXRFegMHUVgSqE+wvhAbi4WqjGg9czysTV2Epbew==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/obug": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/obug/-/obug-2.1.1.tgz",
      "integrity": "sha512-uTqF9MuPraAQ+IsnPf366RG4cP9RtUi7MLO1N3KEc+wb0a6yKpeL0lmk2IB1jY5KHPAlTc6T/JRdC/YqxHNwkQ==",
      "dev": true,
      "funding": [
        "https://github.com/sponsors/sxzz",
        "https://opencollective.com/debug"
      ],
      "license": "MIT"
    },
    "node_modules/on-finished": {
      "version": "2.4.1",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.4.1.tgz",
      "integrity": "sha512-oVlzkg3ENAhCk2zdv7IJwd/QUD4z2RxRwpkcGY8psCVcCYZNq4wYnVWALHM+brtuJjePWiYF/ClmuDr8Ch5+kg==",
      "license": "MIT",
      "dependencies": {
        "ee-first": "1.1.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==",
      "license": "ISC",
      "optional": true,
      "dependencies": {
        "wrappy": "1"
      }
    },
    "node_modules/p-limit": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz",
      "integrity": "sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "yocto-queue": "^0.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/package-json-from-dist": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/package-json-from-dist/-/package-json-from-dist-1.0.1.tgz",
      "integrity": "sha512-UEZIS3/by4OC8vL3P2dTXRETpebLI2NiI5vIrjaD/5UtrkFX/tNbwjTSRAGC/+7CAo2pIcBaRgWmcBBHcsaCIw==",
      "dev": true,
      "license": "BlueOak-1.0.0"
    },
    "node_modules/parseurl": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
      "integrity": "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/path-key": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz",
      "integrity": "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/path-scurry": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/path-scurry/-/path-scurry-1.11.1.tgz",
      "integrity": "sha512-Xa4Nw17FS9ApQFJ9umLiJS4orGjm7ZzwUrwamcGQuHSzDyth9boKDaycYdDcZDuqYATXw4HFXgaqWTctW/v1HA==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "dependencies": {
        "lru-cache": "^10.2.0",
        "minipass": "^5.0.0 || ^6.0.2 || ^7.0.0"
      },
      "engines": {
        "node": ">=16 || 14 >=14.18"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/path-scurry/node_modules/lru-cache": {
      "version": "10.4.3",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-10.4.3.tgz",
      "integrity": "sha512-JNAzZcXrCt42VGLuYz0zfAzDfAvJWW6AfYlDBQyDV5DClI2m5sAmK+OIO7s59XfsRsWHp02jAJrRadPRGTt6SQ==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/path-to-regexp": {
      "version": "0.1.12",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.12.tgz",
      "integrity": "sha512-RA1GjUVMnvYFxuqovrEqZoxxW5NUZqbwKtYz/Tt7nXerk0LbLblQmrsgdeOxV5SFHf0UDggjS/bSeOZwt1pmEQ==",
      "license": "MIT"
    },
    "node_modules/pathe": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/pathe/-/pathe-2.0.3.tgz",
      "integrity": "sha512-WUjGcAqP1gQacoQe+OBJsFA7Ld4DyXuUIjZ5cc75cLHvJ7dtNsTugphxIADwspS+AraAUePCKrSVtPLFj/F88w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/proto3-json-serializer": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/proto3-json-serializer/-/proto3-json-serializer-2.0.2.tgz",
      "integrity": "sha512-SAzp/O4Yh02jGdRc+uIrGoe87dkN/XtwxfZ4ZyafJHymd79ozp5VG5nyZ7ygqPM5+cpLDjjGnYFUkngonyDPOQ==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "protobufjs": "^7.2.5"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/protobufjs": {
      "version": "7.5.4",
      "resolved": "https://registry.npmjs.org/protobufjs/-/protobufjs-7.5.4.tgz",
      "integrity": "sha512-CvexbZtbov6jW2eXAvLukXjXUW1TzFaivC46BpWc/3BpcCysb5Vffu+B3XHMm8lVEuy2Mm4XGex8hBSg1yapPg==",
      "hasInstallScript": true,
      "license": "BSD-3-Clause",
      "dependencies": {
        "@protobufjs/aspromise": "^1.1.2",
        "@protobufjs/base64": "^1.1.2",
        "@protobufjs/codegen": "^2.0.4",
        "@protobufjs/eventemitter": "^1.1.0",
        "@protobufjs/fetch": "^1.1.0",
        "@protobufjs/float": "^1.0.2",
        "@protobufjs/inquire": "^1.1.0",
        "@protobufjs/path": "^1.1.2",
        "@protobufjs/pool": "^1.1.0",
        "@protobufjs/utf8": "^1.1.0",
        "@types/node": ">=13.7.0",
        "long": "^5.0.0"
      },
      "engines": {
        "node": ">=12.0.0"
      }
    },
    "node_modules/proxy-addr": {
      "version": "2.0.7",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.7.tgz",
      "integrity": "sha512-llQsMLSUDUPT44jdrU/O37qlnifitDP+ZwrmmZcoSKyLKvtZxpyV0n2/bD/N4tBAAZ/gJEdZU7KMraoK1+XYAg==",
      "license": "MIT",
      "dependencies": {
        "forwarded": "0.2.0",
        "ipaddr.js": "1.9.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/qs": {
      "version": "6.14.0",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.14.0.tgz",
      "integrity": "sha512-YWWTjgABSKcvs/nWBi9PycY/JiPJqOD4JA6o9Sej2AtvSGarXxKC3OQSk4pAarbdQlKAh5D4FCQkJNkW+GAn3w==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "side-channel": "^1.1.0"
      },
      "engines": {
        "node": ">=0.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/quansync": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/quansync/-/quansync-1.0.0.tgz",
      "integrity": "sha512-5xZacEEufv3HSTPQuchrvV6soaiACMFnq1H8wkVioctoH3TRha9Sz66lOxRwPK/qZj7HPiSveih9yAyh98gvqA==",
      "dev": true,
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/antfu"
        },
        {
          "type": "individual",
          "url": "https://github.com/sponsors/sxzz"
        }
      ],
      "license": "MIT"
    },
    "node_modules/range-parser": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz",
      "integrity": "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/raw-body": {
      "version": "2.5.3",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.5.3.tgz",
      "integrity": "sha512-s4VSOf6yN0rvbRZGxs8Om5CWj6seneMwK3oDb4lWDH0UPhWcxwOWw5+qk24bxq87szX1ydrwylIOp2uG1ojUpA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "~3.1.2",
        "http-errors": "~2.0.1",
        "iconv-lite": "~0.4.24",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/readable-stream": {
      "version": "3.6.2",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz",
      "integrity": "sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "inherits": "^2.0.3",
        "string_decoder": "^1.1.1",
        "util-deprecate": "^1.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/require-directory": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz",
      "integrity": "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/resolve-pkg-maps": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/resolve-pkg-maps/-/resolve-pkg-maps-1.0.0.tgz",
      "integrity": "sha512-seS2Tj26TBVOC2NIc2rOe2y2ZO7efxITtLZcGSOnHHNOQ7CkiUBfw0Iw2ck6xkIhPwLhKNLS8BO+hEpngQlqzw==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/privatenumber/resolve-pkg-maps?sponsor=1"
      }
    },
    "node_modules/retry": {
      "version": "0.13.1",
      "resolved": "https://registry.npmjs.org/retry/-/retry-0.13.1.tgz",
      "integrity": "sha512-XQBQ3I8W1Cge0Seh+6gjj03LbmRFWuoszgK9ooCpwYIrhhoO80pfq4cUkU5DkknwfOfFteRwlZ56PYOGYyFWdg==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">= 4"
      }
    },
    "node_modules/retry-request": {
      "version": "7.0.2",
      "resolved": "https://registry.npmjs.org/retry-request/-/retry-request-7.0.2.tgz",
      "integrity": "sha512-dUOvLMJ0/JJYEn8NrpOaGNE7X3vpI5XlZS/u0ANjqtcZVKnIxP7IgCFwrKTxENw29emmwug53awKtaMm4i9g5w==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@types/request": "^2.48.8",
        "extend": "^3.0.2",
        "teeny-request": "^9.0.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/rimraf": {
      "version": "5.0.10",
      "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-5.0.10.tgz",
      "integrity": "sha512-l0OE8wL34P4nJH/H2ffoaniAokM2qSmrtXHmlpvYr5AVVX8msAyW0l8NVJFDxlSK4u3Uh/f41cQheDVdnYijwQ==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "glob": "^10.3.7"
      },
      "bin": {
        "rimraf": "dist/esm/bin.mjs"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/rolldown": {
      "version": "1.0.0-beta.57",
      "resolved": "https://registry.npmjs.org/rolldown/-/rolldown-1.0.0-beta.57.tgz",
      "integrity": "sha512-lMMxcNN71GMsSko8RyeTaFoATHkCh4IWU7pYF73ziMYjhHZWfVesC6GQ+iaJCvZmVjvgSks9Ks1aaqEkBd8udg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@oxc-project/types": "=0.103.0",
        "@rolldown/pluginutils": "1.0.0-beta.57"
      },
      "bin": {
        "rolldown": "bin/cli.mjs"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "optionalDependencies": {
        "@rolldown/binding-android-arm64": "1.0.0-beta.57",
        "@rolldown/binding-darwin-arm64": "1.0.0-beta.57",
        "@rolldown/binding-darwin-x64": "1.0.0-beta.57",
        "@rolldown/binding-freebsd-x64": "1.0.0-beta.57",
        "@rolldown/binding-linux-arm-gnueabihf": "1.0.0-beta.57",
        "@rolldown/binding-linux-arm64-gnu": "1.0.0-beta.57",
        "@rolldown/binding-linux-arm64-musl": "1.0.0-beta.57",
        "@rolldown/binding-linux-x64-gnu": "1.0.0-beta.57",
        "@rolldown/binding-linux-x64-musl": "1.0.0-beta.57",
        "@rolldown/binding-openharmony-arm64": "1.0.0-beta.57",
        "@rolldown/binding-wasm32-wasi": "1.0.0-beta.57",
        "@rolldown/binding-win32-arm64-msvc": "1.0.0-beta.57",
        "@rolldown/binding-win32-x64-msvc": "1.0.0-beta.57"
      }
    },
    "node_modules/rolldown-plugin-dts": {
      "version": "0.20.0",
      "resolved": "https://registry.npmjs.org/rolldown-plugin-dts/-/rolldown-plugin-dts-0.20.0.tgz",
      "integrity": "sha512-cLAY1kN2ilTYMfZcFlGWbXnu6Nb+8uwUBsi+Mjbh4uIx7IN8uMOmJ7RxrrRgPsO4H7eSz3E+JwGoL1gyugiyUA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/generator": "^7.28.5",
        "@babel/parser": "^7.28.5",
        "@babel/types": "^7.28.5",
        "ast-kit": "^2.2.0",
        "birpc": "^4.0.0",
        "dts-resolver": "^2.1.3",
        "get-tsconfig": "^4.13.0",
        "obug": "^2.1.1"
      },
      "engines": {
        "node": ">=20.19.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sxzz"
      },
      "peerDependencies": {
        "@ts-macro/tsc": "^0.3.6",
        "@typescript/native-preview": ">=7.0.0-dev.20250601.1",
        "rolldown": "^1.0.0-beta.57",
        "typescript": "^5.0.0",
        "vue-tsc": "~3.2.0"
      },
      "peerDependenciesMeta": {
        "@ts-macro/tsc": {
          "optional": true
        },
        "@typescript/native-preview": {
          "optional": true
        },
        "typescript": {
          "optional": true
        },
        "vue-tsc": {
          "optional": true
        }
      }
    },
    "node_modules/safe-buffer": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
      "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==",
      "license": "MIT"
    },
    "node_modules/send": {
      "version": "0.19.2",
      "resolved": "https://registry.npmjs.org/send/-/send-0.19.2.tgz",
      "integrity": "sha512-VMbMxbDeehAxpOtWJXlcUS5E8iXh6QmN+BkRX1GARS3wRaXEEgzCcB10gTQazO42tpNIya8xIyNx8fll1OFPrg==",
      "license": "MIT",
      "dependencies": {
        "debug": "2.6.9",
        "depd": "2.0.0",
        "destroy": "1.2.0",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "fresh": "~0.5.2",
        "http-errors": "~2.0.1",
        "mime": "1.6.0",
        "ms": "2.1.3",
        "on-finished": "~2.4.1",
        "range-parser": "~1.2.1",
        "statuses": "~2.0.2"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/send/node_modules/mime": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.6.0.tgz",
      "integrity": "sha512-x0Vn8spI+wuJ1O6S7gnbaQg8Pxh4NNHb7KSINmEWKiPE4RKOplvijn+NkmYmmRgP68mc70j2EbeTFRsrswaQeg==",
      "license": "MIT",
      "bin": {
        "mime": "cli.js"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/send/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/serve-static": {
      "version": "1.16.3",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.16.3.tgz",
      "integrity": "sha512-x0RTqQel6g5SY7Lg6ZreMmsOzncHFU7nhnRWkKgWuMTu5NN0DR5oruckMqRvacAN9d5w6ARnRBXl9xhDCgfMeA==",
      "license": "MIT",
      "dependencies": {
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "parseurl": "~1.3.3",
        "send": "~0.19.1"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/setprototypeof": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz",
      "integrity": "sha512-E5LDX7Wrp85Kil5bhZv46j8jOeboKq5JMmYM3gVGdGH8xFpPWXUMsNrlODCrkoxMEeNi/XZIwuRvY4XNwYMJpw==",
      "license": "ISC"
    },
    "node_modules/shebang-command": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz",
      "integrity": "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "shebang-regex": "^3.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/shebang-regex": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz",
      "integrity": "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/side-channel": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz",
      "integrity": "sha512-ZX99e6tRweoUXqR+VBrslhda51Nh5MTQwou5tnUDgbtyM0dBgmhEDtWGP/xbKn6hqfPRHujUNwz5fy/wbbhnpw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3",
        "side-channel-list": "^1.0.0",
        "side-channel-map": "^1.0.1",
        "side-channel-weakmap": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-list": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.0.tgz",
      "integrity": "sha512-FCLHtRD/gnpCiCHEiJLOwdmFP+wzCmDEkc9y7NsYxeF4u7Btsn1ZuwgwJGxImImHicJArLP4R0yX4c2KCrMrTA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-map": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz",
      "integrity": "sha512-VCjCNfgMsby3tTdo02nbjtM/ewra6jPHmpThenkTYh8pG9ucZ/1P8So4u4FGBek/BjpOVsDCMoLA/iuBKIFXRA==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-weakmap": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz",
      "integrity": "sha512-WPS/HvHQTYnHisLo9McqBHOJk2FkHO/tlpvldyrnem4aeQp4hai3gythswg6p01oSoTl58rcpiFAjF2br2Ak2A==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3",
        "side-channel-map": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/signal-exit": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-4.1.0.tgz",
      "integrity": "sha512-bzyZ1e88w9O1iNJbKnOlvYTrWPDl46O1bG0D3XInv+9tkPrxrN8jUUTiFlDkkmKWgn1M6CfIA13SuGqOa9Korw==",
      "dev": true,
      "license": "ISC",
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/statuses": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-2.0.2.tgz",
      "integrity": "sha512-DvEy55V3DB7uknRo+4iOGT5fP1slR8wQohVdknigZPMpMstaKJQWhwiYBACJE3Ul2pTnATihhBYnRhZQHGBiRw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/stream-events": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/stream-events/-/stream-events-1.0.5.tgz",
      "integrity": "sha512-E1GUzBSgvct8Jsb3v2X15pjzN1tYebtbLaMg+eBOUOAxgbLoSbT2NS91ckc5lJD1KfLjId+jXJRgo0qnV5Nerg==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "stubs": "^3.0.0"
      }
    },
    "node_modules/stream-shift": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.3.tgz",
      "integrity": "sha512-76ORR0DO1o1hlKwTbi/DM3EXWGf3ZJYO8cXX5RJwnul2DEg2oyoZyjLNoQM8WsvZiFKCRfC1O0J7iCvie3RZmQ==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/string_decoder": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz",
      "integrity": "sha512-hkRX8U1WjJFd8LsDJ2yQ/wWWxaopEsABU1XfkM8A+j0+85JAGppt16cr1Whg6KIbb4okU6Mql6BOj+uup/wKeA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "safe-buffer": "~5.2.0"
      }
    },
    "node_modules/string-width": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-5.1.2.tgz",
      "integrity": "sha512-HnLOCR3vjcY8beoNLtcjZ5/nxn2afmME6lhrDrebokqMap+XbeW8n9TXpPDOqdGK5qcI3oT0GKTW6wC7EMiVqA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "eastasianwidth": "^0.2.0",
        "emoji-regex": "^9.2.2",
        "strip-ansi": "^7.0.1"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/string-width-cjs": {
      "name": "string-width",
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/string-width-cjs/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/string-width-cjs/node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/string-width-cjs/node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strip-ansi": {
      "version": "7.1.2",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-7.1.2.tgz",
      "integrity": "sha512-gmBGslpoQJtgnMAvOVqGZpEz9dyoKTCzy2nfz/n8aIFhN/jCE/rCmcxabB6jOOHV+0WNnylOxaxBQPSvcWklhA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^6.0.1"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/strip-ansi?sponsor=1"
      }
    },
    "node_modules/strip-ansi-cjs": {
      "name": "strip-ansi",
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strip-ansi-cjs/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/strnum": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/strnum/-/strnum-1.1.2.tgz",
      "integrity": "sha512-vrN+B7DBIoTTZjnPNewwhx6cBA/H+IS7rfW68n7XxC1y7uoiGQBxaKzqucGUgavX15dJgiGztLJ8vxuEzwqBdA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/NaturalIntelligence"
        }
      ],
      "license": "MIT",
      "optional": true
    },
    "node_modules/stubs": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/stubs/-/stubs-3.0.0.tgz",
      "integrity": "sha512-PdHt7hHUJKxvTCgbKX9C1V/ftOcjJQgz8BZwNfV5c4B6dcGqlpelTbJ999jBGZ2jYiPAwcX5dP6oBwVlBlUbxw==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/synckit": {
      "version": "0.11.11",
      "resolved": "https://registry.npmjs.org/synckit/-/synckit-0.11.11.tgz",
      "integrity": "sha512-MeQTA1r0litLUf0Rp/iisCaL8761lKAZHaimlbGK4j0HysC4PLfqygQj9srcs0m2RdtDYnF8UuYyKpbjHYp7Jw==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "peer": true,
      "dependencies": {
        "@pkgr/core": "^0.2.9"
      },
      "engines": {
        "node": "^14.18.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/synckit"
      }
    },
    "node_modules/teeny-request": {
      "version": "9.0.0",
      "resolved": "https://registry.npmjs.org/teeny-request/-/teeny-request-9.0.0.tgz",
      "integrity": "sha512-resvxdc6Mgb7YEThw6G6bExlXKkv6+YbuzGg9xuXxSgxJF7Ozs+o8Y9+2R3sArdWdW8nOokoQb1yrpFB0pQK2g==",
      "license": "Apache-2.0",
      "optional": true,
      "dependencies": {
        "http-proxy-agent": "^5.0.0",
        "https-proxy-agent": "^5.0.0",
        "node-fetch": "^2.6.9",
        "stream-events": "^1.0.5",
        "uuid": "^9.0.0"
      },
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/teeny-request/node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/teeny-request/node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/teeny-request/node_modules/https-proxy-agent": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.1.tgz",
      "integrity": "sha512-dFcAjpTQFgoLMzC2VwU+C/CbS7uRL0lWmxDITmqm7C+7F0Odmj6s9l6alZc6AELXhrnggM2CeWSXHGOdX2YtwA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "agent-base": "6",
        "debug": "4"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/teeny-request/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/teeny-request/node_modules/uuid": {
      "version": "9.0.1",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-9.0.1.tgz",
      "integrity": "sha512-b+1eJOlsR9K8HJpow9Ok3fiWOWSIcIzXodvv0rQjVoOVNpWMpxf1wZNpt4y9h10odCNrqnYp1OBzRktckBe3sA==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "license": "MIT",
      "optional": true,
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    },
    "node_modules/tinyexec": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/tinyexec/-/tinyexec-1.0.2.tgz",
      "integrity": "sha512-W/KYk+NFhkmsYpuHq5JykngiOCnxeVL8v8dFnqxSD8qEEdRfXk1SDM6JzNqcERbcGYj9tMrDQBYV9cjgnunFIg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/tinyglobby": {
      "version": "0.2.15",
      "resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.15.tgz",
      "integrity": "sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fdir": "^6.5.0",
        "picomatch": "^4.0.3"
      },
      "engines": {
        "node": ">=12.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/SuperchupuDev"
      }
    },
    "node_modules/tinyglobby/node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/tinyglobby/node_modules/picomatch": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz",
      "integrity": "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/toidentifier": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz",
      "integrity": "sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA==",
      "license": "MIT",
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/tr46": {
      "version": "0.0.3",
      "resolved": "https://registry.npmjs.org/tr46/-/tr46-0.0.3.tgz",
      "integrity": "sha512-N3WMsuqV66lT30CrXNbEjx4GEwlow3v6rr4mCcv6prnfwhS01rkgyFdjPNBYd9br7LpXV1+Emh01fHnq2Gdgrw==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/tree-kill": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/tree-kill/-/tree-kill-1.2.2.tgz",
      "integrity": "sha512-L0Orpi8qGpRG//Nd+H90vFB+3iHnue1zSSGmNOOCh1GLJ7rUKVwV2HvijphGQS2UmhUZewS9VgvxYIdgr+fG1A==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "tree-kill": "cli.js"
      }
    },
    "node_modules/tsdown": {
      "version": "0.18.3",
      "resolved": "https://registry.npmjs.org/tsdown/-/tsdown-0.18.3.tgz",
      "integrity": "sha512-OVFzktKDTglFAUh/WO8WamBUbZoBlJ9m7NgZZrVyIKe32BfXBeRZ+soFFpuOGVP8g8OU4tOLOpTyPTELWvcTFw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansis": "^4.2.0",
        "cac": "^6.7.14",
        "defu": "^6.1.4",
        "empathic": "^2.0.0",
        "hookable": "^6.0.1",
        "import-without-cache": "^0.2.5",
        "obug": "^2.1.1",
        "picomatch": "^4.0.3",
        "rolldown": "1.0.0-beta.57",
        "rolldown-plugin-dts": "^0.20.0",
        "semver": "^7.7.3",
        "tinyexec": "^1.0.2",
        "tinyglobby": "^0.2.15",
        "tree-kill": "^1.2.2",
        "unconfig-core": "^7.4.2",
        "unrun": "^0.2.21"
      },
      "bin": {
        "tsdown": "dist/run.mjs"
      },
      "engines": {
        "node": ">=20.19.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sxzz"
      },
      "peerDependencies": {
        "@arethetypeswrong/core": "^0.18.1",
        "@vitejs/devtools": "*",
        "publint": "^0.3.0",
        "typescript": "^5.0.0",
        "unplugin-lightningcss": "^0.4.0",
        "unplugin-unused": "^0.5.0"
      },
      "peerDependenciesMeta": {
        "@arethetypeswrong/core": {
          "optional": true
        },
        "@vitejs/devtools": {
          "optional": true
        },
        "publint": {
          "optional": true
        },
        "typescript": {
          "optional": true
        },
        "unplugin-lightningcss": {
          "optional": true
        },
        "unplugin-unused": {
          "optional": true
        }
      }
    },
    "node_modules/tsdown/node_modules/picomatch": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz",
      "integrity": "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/tsdown/node_modules/semver": {
      "version": "7.7.3",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.7.3.tgz",
      "integrity": "sha512-SdsKMrI9TdgjdweUSR9MweHA4EJ8YxHn8DFaDisvhVlUOe4BF1tLD7GAj0lIqWVl+dPb/rExr0Btby5loQm20Q==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "license": "0BSD"
    },
    "node_modules/type-is": {
      "version": "1.6.18",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
      "integrity": "sha512-TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J2do2Jr3Kym598JVdEksuzPQCnlFPW4ky9Q+iA+ma9BGm06XQBy8g==",
      "license": "MIT",
      "dependencies": {
        "media-typer": "0.3.0",
        "mime-types": "~2.1.24"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/typescript": {
      "version": "5.9.3",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
      "integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/unconfig-core": {
      "version": "7.4.2",
      "resolved": "https://registry.npmjs.org/unconfig-core/-/unconfig-core-7.4.2.tgz",
      "integrity": "sha512-VgPCvLWugINbXvMQDf8Jh0mlbvNjNC6eSUziHsBCMpxR05OPrNrvDnyatdMjRgcHaaNsCqz+wjNXxNw1kRLHUg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@quansync/fs": "^1.0.0",
        "quansync": "^1.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/antfu"
      }
    },
    "node_modules/undici-types": {
      "version": "6.21.0",
      "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-6.21.0.tgz",
      "integrity": "sha512-iwDZqg0QAGrg9Rav5H4n0M64c3mkR59cJ6wQp+7C4nI0gsmExaedaYLNO44eT4AtBBwjbTiGPMlt2Md0T9H9JQ==",
      "license": "MIT"
    },
    "node_modules/unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha512-pjy2bYhSsufwWlKwPc+l3cN7+wuJlK6uz0YdJEOlQDbl6jo/YlPi4mb8agUkVC8BF7V8NuzeyPNqRksA3hztKQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/unrun": {
      "version": "0.2.21",
      "resolved": "https://registry.npmjs.org/unrun/-/unrun-0.2.21.tgz",
      "integrity": "sha512-VuwI4YKtwBpDvM7hCEop2Im/ezS82dliqJpkh9pvS6ve8HcUsBDvESHxMmUfImXR03GkmfdDynyrh/pUJnlguw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "rolldown": "1.0.0-beta.57"
      },
      "bin": {
        "unrun": "dist/cli.mjs"
      },
      "engines": {
        "node": ">=20.19.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/Gugustinette"
      },
      "peerDependencies": {
        "synckit": "^0.11.11"
      },
      "peerDependenciesMeta": {
        "synckit": {
          "optional": true
        }
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/utils-merge": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
      "integrity": "sha512-pMZTvIkT1d+TFGvDOqodOclx0QWkkgi6Tdoa8gC8ffGAAqz9pzPTZWAybbsHHoED/ztMtkv/VoYTYyShUn81hA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4.0"
      }
    },
    "node_modules/uuid": {
      "version": "10.0.0",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-10.0.0.tgz",
      "integrity": "sha512-8XkAphELsDnEGrDxUOHB3RGvXz6TeuYSGEZBOjtTtPm2lwhGBjLgOzLHB63IUWfBpNucQjND6d3AOudO+H3RWQ==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "license": "MIT",
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    },
    "node_modules/vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha512-BNGbWLfd0eUPabhkXUVm0j8uuvREyTh5ovRa/dyow/BqAbZJyC+5fU+IzQOzmAKzYqYRAISoRhdQr3eIZ/PXqg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/web-streams-polyfill": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/web-streams-polyfill/-/web-streams-polyfill-3.3.3.tgz",
      "integrity": "sha512-d2JWLCivmZYTSIoge9MsgFCZrt571BikcWGYkjC1khllbTeDlGqZ2D8vD8E/lJa8WGWbb7Plm8/XJYV7IJHZZw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/webidl-conversions": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-3.0.1.tgz",
      "integrity": "sha512-2JAn3z8AR6rjK8Sm8orRC0h/bcl/DqL7tRPdGZ4I1CjdF+EaMLmYxBHyXuKL849eucPFhvBoxMsflfOb8kxaeQ==",
      "license": "BSD-2-Clause",
      "optional": true
    },
    "node_modules/websocket-driver": {
      "version": "0.7.4",
      "resolved": "https://registry.npmjs.org/websocket-driver/-/websocket-driver-0.7.4.tgz",
      "integrity": "sha512-b17KeDIQVjvb0ssuSDF2cYXSg2iztliJ4B9WdsuB6J952qCPKmnVq4DyW5motImXHDC1cBT/1UezrJVsKw5zjg==",
      "license": "Apache-2.0",
      "dependencies": {
        "http-parser-js": ">=0.5.1",
        "safe-buffer": ">=5.1.0",
        "websocket-extensions": ">=0.1.1"
      },
      "engines": {
        "node": ">=0.8.0"
      }
    },
    "node_modules/websocket-extensions": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/websocket-extensions/-/websocket-extensions-0.1.4.tgz",
      "integrity": "sha512-OqedPIGOfsDlo31UNwYbCFMSaO9m9G/0faIHj5/dZFDMFqPTcx6UwqyOy3COEaEOg/9VsGIpdqn62W5KhoKSpg==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=0.8.0"
      }
    },
    "node_modules/whatwg-url": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/whatwg-url/-/whatwg-url-5.0.0.tgz",
      "integrity": "sha512-saE57nupxk6v3HY35+jzBwYa0rKSy0XR8JSxZPwgLr7ys0IBzhGviA1/TUGJLmSVqs8pb9AnvICXEuOHLprYTw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tr46": "~0.0.3",
        "webidl-conversions": "^3.0.0"
      }
    },
    "node_modules/which": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/which/-/which-2.0.2.tgz",
      "integrity": "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "isexe": "^2.0.0"
      },
      "bin": {
        "node-which": "bin/node-which"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/wrap-ansi": {
      "version": "8.1.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-8.1.0.tgz",
      "integrity": "sha512-si7QWI6zUMq56bESFvagtmzMdGOtoxfR+Sez11Mobfc7tm+VkUckk9bW2UeffTGVUbOksxmSw0AA2gs8g71NCQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^6.1.0",
        "string-width": "^5.0.1",
        "strip-ansi": "^7.0.1"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
      }
    },
    "node_modules/wrap-ansi-cjs": {
      "name": "wrap-ansi",
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
      "integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^4.0.0",
        "string-width": "^4.1.0",
        "strip-ansi": "^6.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
      }
    },
    "node_modules/wrap-ansi-cjs/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/wrap-ansi-cjs/node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/wrap-ansi-cjs/node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/wrap-ansi-cjs/node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/wrap-ansi/node_modules/ansi-styles": {
      "version": "6.2.3",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-6.2.3.tgz",
      "integrity": "sha512-4Dj6M28JB+oAH8kFkTLUo+a2jwOFkuqb3yucU0CANcRRUbxS0cP0nZYCGjcc3BNXwRIsUVmDGgzawme7zvJHvg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
      "license": "ISC",
      "optional": true
    },
    "node_modules/ws": {
      "version": "8.18.3",
      "resolved": "https://registry.npmjs.org/ws/-/ws-8.18.3.tgz",
      "integrity": "sha512-PEIGCY5tSlUt50cqyMXfCzX+oOPqN0vuGqWzbcJ2xvnkzkq46oOpz7dQaTDBdfICb4N14+GARUDw2XV2N4tvzg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10.0.0"
      },
      "peerDependencies": {
        "bufferutil": "^4.0.1",
        "utf-8-validate": ">=5.0.2"
      },
      "peerDependenciesMeta": {
        "bufferutil": {
          "optional": true
        },
        "utf-8-validate": {
          "optional": true
        }
      }
    },
    "node_modules/y18n": {
      "version": "5.0.8",
      "resolved": "https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz",
      "integrity": "sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==",
      "license": "ISC",
      "optional": true,
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/yargs": {
      "version": "17.7.2",
      "resolved": "https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz",
      "integrity": "sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "cliui": "^8.0.1",
        "escalade": "^3.1.1",
        "get-caller-file": "^2.0.5",
        "require-directory": "^2.1.1",
        "string-width": "^4.2.3",
        "y18n": "^5.0.5",
        "yargs-parser": "^21.1.1"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/yargs-parser": {
      "version": "21.1.1",
      "resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz",
      "integrity": "sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==",
      "license": "ISC",
      "optional": true,
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/yargs/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/yargs/node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/yargs/node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/yargs/node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/yocto-queue": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz",
      "integrity": "sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==",
      "license": "MIT",
      "optional": true,
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/zod": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/zod/-/zod-4.2.1.tgz",
      "integrity": "sha512-0wZ1IRqGGhMP76gLqz8EyfBXKk0J2qo2+H3fi4mcUP/KtTocoX08nmIAHl1Z2kJIZbZee8KOpBCSNPRgauucjw==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/colinhacks"
      }
    }
  }
}

```

## File: chat-integration\functions\package.json
```
{
  "name": "atq-chat-integration",
  "scripts": {
    "build": "tsdown",
    "dev": "tsdown -w",
    "serve": "npm run build && firebase emulators:start --only functions",
    "shell": "npm run build && firebase functions:shell",
    "start": "npm run shell",
    "deploy": "firebase deploy --only functions",
    "logs": "firebase functions:log"
  },
  "engines": {
    "node": "22"
  },
  "main": "lib/index.js",
  "dependencies": {
    "firebase-admin": "^12.6.0",
    "firebase-functions": "^6.0.1"
  },
  "devDependencies": {
    "@google/genai": "^1.34.0",
    "nanoid": "^5.1.6",
    "zod": "^4.2.1",
    "tsdown": "^0.18.3",
    "typescript": "^5.7.3"
  },
  "private": true
}

```

## File: chat-integration\functions\tsconfig.json
```
{
  "compilerOptions": {
    "module": "NodeNext",
    "esModuleInterop": true,
    "moduleResolution": "nodenext",
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "outDir": "lib",
    "sourceMap": true,
    "strict": true,
    "allowArbitraryExtensions": true,
    "target": "es2017"
  },
  "compileOnSave": true,
  "include": [
    "src"
  ]
}

```

## File: chat-integration\functions\tsdown.config.ts
```
import { defineConfig } from "tsdown";

export default defineConfig({
  format: ["cjs"],
  target: ["es2022"],
  envFile: ".env",
  clean: true,
  minify: false,
  outDir: "lib",
  fixedExtension: false,
  entry: ["./src/index.ts"],
  platform: "node",
});

```

## File: chat-integration\functions\src\index.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { initializeApp } from "firebase-admin/app";
import { getDatabase } from "firebase-admin/database";
import { setGlobalOptions } from "firebase-functions";
import { onRequest } from "firebase-functions/https";
import * as logger from "firebase-functions/logger";
import { ai } from "./miniapp-generator/ai";
import { generateMiniApp } from "./miniapp-generator/miniapp-generator";
import { generateTitle } from "./miniapp-generator/title-generator";
import { generateId } from "./util";

setGlobalOptions({ maxInstances: 10 });

if (!process.env.TSDOWN_FIREBASE_DATABASE_URL) {
  throw new Error("TSDOWN_FIREBASE_DATABASE_URL is not set");
}

const app = initializeApp({
  databaseURL: process.env.TSDOWN_FIREBASE_DATABASE_URL,
});
const db = getDatabase(app);

async function putSharedSoftDocument(id: string, data: any) {
  await db.ref(`sharedsoft/docs/${id}`).set(data);
}

export const generateSharedSoftDocument = onRequest(
  async (request, response) => {
    if (request.method !== "POST") {
      response.status(405).send("Method not allowed");
      return;
    }

    const { prompt } = request.body || "";
    if (!prompt) {
      response.status(400).send("Missing `prompt` param");
      return;
    }

    let id = generateId();

    logger.info(`[${id}] Generating code asynchronously...`);
    await putSharedSoftDocument(id, {
      content: {
        prompt,
        status: "generating",
      },
    });
    let [appCode, title] = await Promise.all([
      generateMiniApp(ai, prompt),
      generateTitle(ai, prompt),
    ]);
    logger.info(`[${id}] Generated app code!`);
    await putSharedSoftDocument(id, {
      metadata: {
        title,
      },
      content: {
        prompt,
        status: "generated",
        code: appCode,
      },
    });

    response.status(200).send(
      JSON.stringify({
        prompt,
        title,
        id,
      }) + "\n"
    );
  }
);

```

## File: chat-integration\functions\src\util.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { customAlphabet } from "nanoid";

export const generateId = () =>
  customAlphabet(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    10
  )();

```

## File: chat-integration\functions\src\miniapp-generator\ai.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";

export const ai = new GoogleGenAI({
  apiKey: process.env.TSDOWN_GEMINI_API_KEY,
});

```

## File: chat-integration\functions\src\miniapp-generator\counter.example.txt
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { MinusIcon, PlusIcon } from "npm:lucide-react";
import { useSyncedState, useLoggedInUser } from "$";

export default function App() {
  const [count, setCount] = useSyncedState("counter", 0);
  const { name, color } = useLoggedInUser();

  return (
    <div className="flex flex-col items-center justify-center h-screen space-y-4">
      <div>
        Hello, <span style={{ color }}>{name}</span>
      </div>
      <div className="text-8xl text-bold text-green-600">{count}</div>
      <div className="flex gap-1">
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-full"
          onClick={() => setCount(count - 1)}
        >
          <MinusIcon />
        </button>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-full"
          onClick={() => setCount(count + 1)}
        >
          <PlusIcon />
        </button>
      </div>
    </div>
  );
}

```

## File: chat-integration\functions\src\miniapp-generator\fileTypes.d.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

declare module "*.txt" {
  const content: string;
  export default content;
}
```

## File: chat-integration\functions\src\miniapp-generator\host-types.txt
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export type User = { name: string; color: string };

/**
 * Example:
 * ```ts
 * import { useSyncedState } from '$';
 *
 * function MyComponent() {
 *   const [value, setValue] = useSyncedState("value", 15);
 *   return <>The value is {value}</>;
 * }
 * ```
 */
export type useSyncedState = (
  stateKey: string,
  defaultValue: any
) => [any, (newValue: any) => void];

/**
 * Example:
 * ```ts
 * import { useLoggedInUser } from '$';
 *
 * function MyComponent() {
 *   const { name, color } = useLoggedInUser();
 *   return <>You are <span style={{ color }}>{name}</span></>;
 * }
 * ```
 */
export type useLoggedInUser = () => User;

/**
 * Calls AI, returning an async generator that yields content chunks as they arrive. Example:
 * ```ts
 * import { generateContentStream } from '$';
 * async function callAI() {
 *   let request = {
 *     contents: [
 *       {
 *         role: 'user',
 *         parts: [
 *           { text: "Hello there" }
 *         ]
 *       }
 *     ]
 *   };
 *   let result = "";
 *   for await (let chunk of generateContentStream(request)) {
 *     result += chunk;
 *     console.log("Received chunk:", chunk);
 *   }
 *   console.log("Final result:", result);
 * }
 * ```
 */
export type generateContentStream = (
  messages: Array<{ role: "user" | "model"; text: string }>
) => AsyncIterable<string>;

```

## File: chat-integration\functions\src\miniapp-generator\miniapp-generator.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";
import appExampleCounterSource from "./counter.example.txt";
import hostApiTypesSource from "./host-types.txt";

const INSTRUCTIONS = `
You are a helpful assistant that generates code for React "mini apps"
based on a user's prompt. These mini apps are designed to be collaborative (several
users may be using them at once) and sync in real-time using a provided host API.

The generated app should be a single React component in TypeScript that uses functional
components and hooks. The app should be self-contained and not rely on any external
APIs or services.

The app should use Tailwind CSS for styling.

The types for the host API are as follows:

\`\`\`ts
${hostApiTypesSource}
\`\`\`

These APIs are available from the "$", e.g.:

\`\`\`
import { useSyncedState, useLoggedInUser } from "$";
\`\`\`

You can also import packages from npm as needed, using the "npm:" prefix. For example,
to use lucide-react icons, you can import them like so:

\`\`\`ts
import { PlusIcon } from "npm:lucide-react";
\`\`\`

If you need something from React, you can import it from "react", DO NOT prefix it with "npm:".

Here are some examples of prompts and the corresponding app code you should generate:

Prompt: "A simple counter."
App Code:

\`\`\`tsx
${appExampleCounterSource}
\`\`\`
`;

export async function generateMiniApp(
  ai: GoogleGenAI,
  prompt: string,
): Promise<string> {
  let result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    config: {
      systemInstruction: INSTRUCTIONS,
      thinkingConfig: {
        includeThoughts: false,
        thinkingBudget: 1024,
      },
    },
    contents: `
Generate a React mini-app for the following prompt:\n\n
"${prompt}"\n\n
Respond with only the code and nothing else, optionally wrapped in triple backticks.
`,
  });
  let appCode = result.text?.trim() || "";
  appCode = appCode
    .replace(/^\n*```\w*\n/, "")
    .replace(/\n*```\n*$/, "")
    .trim();
  return appCode;
}

```

## File: chat-integration\functions\src\miniapp-generator\title-generator.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";

export async function generateTitle(ai: GoogleGenAI, prompt: string) {
  let result = await ai.models.generateContent({
    model: "gemini-2.5-flash-lite",
    config: {
      systemInstruction: `
            You are great at creating short, catchy titles for app ideas based on
            a brief description of the app's purpose. Given the description below,
            respond with a short title (4 words or less) that captures the essence
            of the app idea. Do not include any additional text or explanation.`
        .replace(/\s+/g, " ")
        .trim(),
    },
    contents: `
          Here is my prompt for an app idea:
          
          ${prompt}
          
          Now give me a short, catchy title for this app idea.`,
  });
  return result.text?.trim();
}

```

## File: src\firebase-config.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

let config: object = {};
try {
  config = JSON.parse(import.meta.env.VITE_FIREBASE_CONFIG);
} catch (e) {
  throw new Error(
    'Must provide FIREBASE_CONFIG as a JSON object (with keys "projectId", "apiKey", etc) in .env',
  );
}
export const FIREBASE_CONFIG = config;

```

## File: src\firebase.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";
import { getFunctions } from "firebase/functions";
import { FIREBASE_CONFIG } from "./firebase-config";

export const app = initializeApp(FIREBASE_CONFIG);
export const db = getDatabase(app);
export const auth = getAuth(app);
export const storage = getStorage(app);
export const functions = getFunctions(app);
```

## File: src\vite-env.d.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

/// <reference types="vite/client" />

```

## File: src\ai\index.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { usePrefsContext } from "@/util/PrefsProvider";
import { GoogleGenAI } from "@google/genai";
import { useMemo } from "react";

export function useGeminiApi() {
  const { prefs } = usePrefsContext();
  return useMemo(() => {
    return new GoogleGenAI({
      apiKey: prefs.geminiApiKey || "FAKE_INVALID_KEY",
      httpOptions: { apiVersion: "v1alpha" },
    });
  }, [prefs.geminiApiKey]);
}

```

## File: src\ai\nano-banana.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { MEDIA_ROOT_PATH } from "@/document/model-and-db";
import { storage } from "@/firebase";
import { GoogleGenAI } from "@google/genai";
import {
  getDownloadURL,
  ref as storageRef,
  uploadBytes,
} from "firebase/storage";

export async function generateImage(
  ai: GoogleGenAI,
  { prompt }: { prompt: string },
): Promise<string> {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image-preview",
    contents: prompt,
  });

  for (const part of response.candidates?.[0].content?.parts || []) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data || "";
      return `data:image/png;base64,${imageData}`;
    }
  }

  throw new Error("No images were generated");
}

export async function saveImage(
  imageDataUrl: string,
  idPath?: string,
): Promise<string> {
  idPath = idPath ?? crypto.randomUUID();
  let storagePath = `${MEDIA_ROOT_PATH}/${idPath}.png`;
  let res = await uploadBytes(
    storageRef(storage, storagePath),
    await fetch(imageDataUrl).then((r) => r.blob()),
  );
  return await getDownloadURL(res.ref);
}

```

## File: src\ai\tools.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import z from "zod";

export type Tool<T> = {
  name: string;
  description: string;
  parameters: z.ZodType<T>;
  run(args: T): Promise<string> | string;
};

export function makeTool<T>(tool: Tool<T>): Tool<T> {
  return tool;
}

```

## File: src\collab\user-colors.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { hashString } from "@/util/hash";
import * as COLORS from "@radix-ui/colors";
import { UserInfo } from "firebase/auth";

const USER_COLORS: (keyof typeof COLORS)[] = [
  "red",
  "pink",
  "purple",
  "indigo",
  "cyan",
  "green",
  "amber",
];

export function globalColorForUser(user: Partial<UserInfo>) {
  let userStr = user.displayName || user.email || user.uid || "Guest";
  let hue = USER_COLORS[hashString(userStr) % USER_COLORS.length];
  return (COLORS[hue] as any)[hue + "9"];
}

```

## File: src\document\model-and-db.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export const APP_ROOT_PATH = "sharedsoft";
export const DOC_ROOT_PATH = `${APP_ROOT_PATH}/docs`;
export const USERINFO_ROOT_PATH = `${APP_ROOT_PATH}/userinfo`;
export const MEDIA_ROOT_PATH = `${APP_ROOT_PATH}/media`;

export type PresenceAppData = {
  canvasCursorPos: { x: number; y: number } | null;
};

export type DocMetadata = {
  creatorUid?: string;
  title?: string;
};

export type AppUserInfo = {
  docs: Record<string, DocMetadata>;
};

export const UNTITLED_DOC_TITLE = "Untitled";

```

## File: src\document\util.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { customAlphabet } from "nanoid";

export const generateId = () =>
  customAlphabet(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    10
  )();

```

## File: src\miniapp\bundler.ts
```
// Borrowed heavily from https://github.com/tschoffelen/jsnotebook/blob/main/lib/bundler/index.ts
import * as esbuild from "esbuild-wasm";
import wasmURL from "esbuild-wasm/esbuild.wasm?url";

interface BundledResult {
  output: string;
  error: string;
  npmExternals?: string[];
}

let loaded = false;
let isLoading = false;

export async function loadEsbuild() {
  if (loaded) {
    return;
  }

  if (isLoading) {
    return new Promise((resolve) => {
      const interval = setInterval(() => {
        if (!isLoading) {
          clearInterval(interval);
          resolve("");
        }
      }, 100);
    });
  }

  isLoading = true;

  try {
    await esbuild.initialize({
      worker: true,
      wasmURL,
    });
    loaded = true;
  } catch (error) {
    if (!String(error).includes("more than once")) {
      console.warn("Error initializing ESBuild", error);
    }
  }
  isLoading = false;
}

export async function esBundle(
  modules: Record<string, string>
): Promise<BundledResult> {
  await loadEsbuild();
  try {
    let npmExternals: string[] = [];
    const result = await esbuild.build({
      entryPoints: ["index.ts"],
      bundle: true,
      minify: false,
      format: "esm",
      platform: "node",
      write: false,
      jsx: "automatic",
      external: ["react", "react-dom", "npm:*"],
      plugins: [
        loaderPlugin(modules, (pkgName) => {
          if (!npmExternals.includes(pkgName)) {
            npmExternals.push(pkgName);
          }
        }),
      ],
      define: {
        global: "window",
      },
    });
    return {
      output: result.outputFiles[0].text,
      npmExternals,
      error: "",
    };
  } catch (error) {
    return {
      output: "",
      error: String((error as any)?.message || error),
    };
  }
}

function loaderPlugin(
  modules: Record<string, string>,
  onRequestExternalPackage?: (pkgName: string) => void
): esbuild.Plugin {
  return {
    name: "fetch-plugin",
    setup(build: esbuild.PluginBuild) {
      // handle root entry file of user input
      build.onResolve({ filter: /^(\w+\.ts)$/ }, ({ path }) => {
        return { path, namespace: "app" };
      });

      // handle other modules in the list
      build.onResolve({ filter: /^.+$/ }, ({ path }) => {
        if (modules[path]) return { path, namespace: "app" };
      });

      // handle other modules in the list
      build.onResolve({ filter: /^npm:(.+)$/ }, ({ path }) => {
        onRequestExternalPackage?.(path.replace(/^npm:/, ""));
        return undefined;
      });

      // handle local modules
      build.onResolve({ filter: /\.\/(.+)$/ }, ({ path }) => {
        return { path: path.replace(/^\.\//, "") + ".ts", namespace: "app" };
      });

      // handle root user input code
      build.onLoad({ filter: /^.*$/ }, ({ path }) => {
        if (!modules[path]) throw new Error("Module not provided: " + path);
        return {
          loader: "tsx",
          contents: modules[path],
        };
      });
    },
  };
}

```

## File: src\miniapp\compiler.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { esBundle, loadEsbuild } from "./bundler";
import hostApi from "./host-api?raw";

const REACT_VERSION = "19.1.0";

export async function compileMiniApp(appCode: string): Promise<string> {
  await loadEsbuild();
  const {
    output: jsBundle,
    npmExternals,
    error,
  } = await esBundle({
    "index.ts": `
import React, {useState} from "react";
import ReactDOM from "react-dom/client";
import App from './app';
import {MiniAppWrapper} from '$';

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <MiniAppWrapper>
      <App />
    </MiniAppWrapper>
  </React.StrictMode>
);

`,
    "app.ts": appCode,
    $: hostApi,
  });
  if (error) throw error;

  // const code = `window.codeRunner = async function () { \n${output}\n }`;
  // iframe.current?.contentWindow?.postMessage({ id, code }, "*");
  return assembleHtml({ jsBundle, npmExternals });
}

function importFor(pkg: string) {
  if (pkg === "lucide-react") {
    // lots of breakages with lucide 1.0
    pkg = "lucide-react@0.577.0";
  }
  return `https://esm.sh/${pkg}`;
}

function assembleHtml({
  jsBundle,
  npmExternals,
}: {
  jsBundle: string;
  npmExternals?: string[];
}) {
  return `
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body>
  <div id="root"></div>
  <script type="importmap">
    {
      "imports": ${JSON.stringify(
        {
          ...Object.fromEntries(
            npmExternals?.map((pkg) => [`npm:${pkg}`, importFor(pkg)]) || [],
          ),
          react: `https://esm.sh/react@${REACT_VERSION}`,
          "react/jsx-runtime": `https://esm.sh/react@${REACT_VERSION}/jsx-runtime`,
          "react-dom/": `https://esm.sh/react-dom@${REACT_VERSION}/`,
        },
        null,
        2,
      )}
    }
  </script>
  <style type="text/tailwindcss">
    @layer base {
      button:not([disabled]),
      [role="button"]:not([disabled]) {
        @apply cursor-pointer;
      }
    }
  </style>
  <script type="module">
${jsBundle}
  </script>
</body>
</html>
`;
}

```

## File: src\miniapp\host-protocol.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GenerateContentParameters } from "@google/genai";

export type AppToHostMessage = ProtocolToUnion<AppToHostProtocol>;
export type AppToHostProtocol = {
  ready: {};
  updateState: { stateKey: string; valueJson: string };
  mouseMove: { x: number; y: number };
  aiGenerateContent: { requestId: string; gcr: GenerateContentParameters };
  aiGenerateImage: { requestId: string; prompt: string };
};

export type HostToAppMessage = ProtocolToUnion<HostToAppProtocol>;
export type HostToAppProtocol = {
  initialize: {
    user: { color: string; name: string };
    syncedState: Record<string, any>;
  };
  updateState: { stateKey: string; valueJson: string };
  aiGenerateContentResponse: { requestId: string } & (
    | { chunk: string }
    | { error: string }
    | { done: true }
  );
  aiGenerateImageResponse: { requestId: string } & (
    | { imageUrl: string }
    | { error: string }
  );
};

// type helpers
type Prettify<T> = { [K in keyof T]: T[K] } & {};
type ProtocolToUnion<T extends Record<string, Record<string, any>>> = Prettify<
  {
    [K in keyof T]: T[K] & {
      type: K;
    };
  }[keyof T]
>;

```

## File: src\miniapp\host-types.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export type User = { name: string; color: string };

/**
 * Example:
 * ```ts
 * import { useSyncedState } from '$';
 *
 * function MyComponent() {
 *   const [value, setValue] = useSyncedState("value", 15);
 *   return <>The value is {value}</>;
 * }
 * ```
 */
export type useSyncedState = (
  stateKey: string,
  defaultValue: any,
) => [any, (newValue: any) => void];

/**
 * Example:
 * ```ts
 * import { useLoggedInUser } from '$';
 *
 * function MyComponent() {
 *   const { name, color } = useLoggedInUser();
 *   return <>You are <span style={{ color }}>{name}</span></>;
 * }
 * ```
 */
export type useLoggedInUser = () => User;

/**
 * Calls AI, returning an async generator that yields content chunks as they arrive. Example:
 * ```ts
 * import { generateContentStream } from '$';
 * async function callAI() {
 *   let request = {
 *     contents: [
 *       {
 *         role: 'user',
 *         parts: [
 *           { text: "Hello there" }
 *         ]
 *       }
 *     ]
 *   };
 *   let result = "";
 *   for await (let chunk of generateContentStream(request)) {
 *     result += chunk;
 *     console.log("Received chunk:", chunk);
 *   }
 *   console.log("Final result:", result);
 * }
 * ```
 */
export type generateContentStream = (
  messages: Array<{ role: "user" | "model"; text: string }>,
) => AsyncIterable<string>;

/**
 * Example:
 * ```ts
 * import { generateImage } from '$';
 * async function createImage() {
 *   let imageUrl = await generateImage("A picture of a banana wearing hat");
 *   console.log("Final result:", imageUrl);
 * }
 * ```
 */
export type generateImage = (prompt: string) => Promise<string>;

```

## File: src\miniapp\README.md
```
Mini apps are:

- A single React + Tailwind JSX file that exports a default component
- Use a fixed "harness" consisting of a static HTML file and default Tailwind config
- Compiled entirely in the browser with esbuild-wasm

```

## File: src\miniapp-generator\miniapp-generator.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";
import hostApiTypesSource from "../miniapp/host-types?raw";
import appExampleCounterSource from "./counter.example?raw";

const INSTRUCTIONS = `
You are a helpful assistant that generates code for React "mini apps"
based on a user's prompt. These mini apps are designed to be collaborative (several
users may be using them at once) and sync in real-time using a provided host API.

The generated app should be a single React component in TypeScript that uses functional
components and hooks. The app should be self-contained and not rely on any external
APIs or services.

The app should use Tailwind CSS for styling.

The types for the host API are as follows:

\`\`\`ts
${hostApiTypesSource}
\`\`\`

These APIs are available from the "$", e.g.:

\`\`\`
import { useSyncedState, useLoggedInUser } from "$";
\`\`\`

You can also import packages from npm as needed, using the "npm:" prefix. For example,
to use lucide-react icons, you can import them like so:

\`\`\`ts
import { PlusIcon } from "npm:lucide-react";
\`\`\`

If you need something from React, you can import it from "react", DO NOT prefix it with "npm:".

Here are some examples of prompts and the corresponding app code you should generate:

Prompt: "A simple counter."
App Code:

\`\`\`tsx
${appExampleCounterSource}
\`\`\`
`;

export async function generateMiniApp(
  ai: GoogleGenAI,
  prompt: string,
): Promise<string> {
  await new Promise((resolve) => setTimeout(resolve, 1000));
  let result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    config: {
      systemInstruction: INSTRUCTIONS,
      thinkingConfig: {
        includeThoughts: false,
        thinkingBudget: 1024,
      },
    },
    contents: `
Generate a React mini-app for the following prompt:\n\n
"${prompt}"\n\n
Respond with only the code and nothing else, optionally wrapped in triple backticks.
`,
  });
  let appCode = result.text?.trim() || "";
  appCode = appCode
    .replace(/^\n*```\w*\n/, "")
    .replace(/\n*```\n*$/, "")
    .trim();
  return appCode;
}

export async function updateMiniApp(
  ai: GoogleGenAI,
  existingCode: string,
  prompt: string,
): Promise<string> {
  await new Promise((resolve) => setTimeout(resolve, 1000));
  let result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    config: {
      systemInstruction: INSTRUCTIONS,
      thinkingConfig: {
        includeThoughts: false,
        thinkingBudget: 1024,
      },
    },
    contents: `
${existingCode}
---
Update the mini-app above with the following instructions:\n\n
"${prompt}"\n\n
Respond with only the code and nothing else, optionally wrapped in triple backticks.
`,
  });
  let appCode = result.text?.trim() || "";
  appCode = appCode
    .replace(/^\n*```\w*\n/, "")
    .replace(/\n*```\n*$/, "")
    .trim();
  return appCode;
}

```

## File: src\miniapp-generator\title-generator.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { GoogleGenAI } from "@google/genai";

export async function generateTitle(ai: GoogleGenAI, prompt: string) {
  let result = await ai.models.generateContent({
    model: "gemini-2.5-flash-lite",
    config: {
      systemInstruction: `
            You are great at creating short, catchy titles for app ideas based on
            a brief description of the app's purpose. Given the description below,
            respond with a short title (4 words or less) that captures the essence
            of the app idea. Do not include any additional text or explanation.`
        .replace(/\s+/g, " ")
        .trim(),
    },
    contents: `
Here is my prompt for an app idea:

${prompt}

Now give me a short, catchy title for this app idea.`,
  });
  return result.text?.trim();
}

```

## File: src\util\hash.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

// FNV-1a implementation
export function hashString(str: string) {
  let hash = 2166136261 >>> 0;
  for (let i = 0; i < str.length; i++) {
    hash ^= str.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}

```

## File: src\util\primitives-util.ts
```
/**
 * @license
 * Copyright 2026 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export function stripUndefined<T>(obj: T): T {
  return JSON.parse(JSON.stringify(obj));
}
```

