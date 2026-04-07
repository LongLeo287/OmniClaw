---
id: react-enterprise-boilerplate
type: knowledge
owner: OA_Triage
---
# react-enterprise-boilerplate
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "react-enterprise-boilerplate",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@reduxjs/toolkit": "^1.9.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-redux": "^8.0.5"
  },
  "devDependencies": {
    "@types/react": "^18.0.28",
    "@types/react-dom": "^18.0.11",
    "@vitejs/plugin-react": "^3.1.0",
    "typescript": "^4.9.3",
    "vite": "^4.2.0"
  }
}

```

### File: readme.md
```md
# React Enterprise Boilerplate

A scalable and well-structured React + TypeScript project architecture
designed for enterprise-level applications.

------------------------------------------------------------------------

## 📁 Project Structure

<img src="./assets/standard.jpg" alt="QR Code ABBank" width="700" height="700">

    react-enterprise-boilerplate/
    │
    ├── public/                 # Static assets (favicon, static images, etc.)
    │
    ├── src/
    │   ├── assets/             # Images, fonts, icons, global styles
    │   ├── components/         # Reusable UI components (Button, Modal, Input...)
    │   ├── constant/           # Application-wide constants and enums
    │   ├── features/           # Business logic modules (feature-based structure)
    │   ├── hooks/              # Custom React hooks
    │   ├── layouts/            # Layout components (MainLayout, AuthLayout...)
    │   ├── pages/              # Page-level components mapped to routes
    │   ├── routes/             # Application routing configuration
    │   ├── store/              # Global state management (Redux/Zustand/etc.)
    │   │
    │   ├── App.tsx             # Root application component
    │   ├── App.css             # App-level styles
    │   ├── index.css           # Global styles
    │   ├── main.tsx            # Application entry point
    │   └── vite-env.d.ts       # Vite TypeScript definitions
    │
    ├── index.html              # Root HTML template
    ├── package.json            # Project dependencies and scripts
    ├── package-lock.json       # Dependency lock file
    ├── tsconfig.json           # TypeScript configuration
    ├── tsconfig.node.json      # Node-specific TypeScript configuration
    ├── vite.config.ts          # Vite configuration
    └── README.md               # Project documentation

------------------------------------------------------------------------

## 🧠 Architectural Principles

### 1️⃣ Separation of Concerns

Each folder has a clear responsibility: - UI components →
`components/` - Business logic → `features/` - Layout structure →
`layouts/` - Routing → `routes/` - Global state → `store/`

This ensures maintainability and scalability.

------------------------------------------------------------------------

### 2️⃣ Feature-Based Structure

Business logic is grouped by feature inside the `features/` directory.\
Each feature can contain: - components - services - hooks - slices (if
using Redux) - types - utils

Example:

    features/
    └── auth/
        ├── components/
        ├── services/
        ├── hooks/
        ├── auth.slice.ts
        └── types.ts

------------------------------------------------------------------------

### 3️⃣ Reusability & Composability

Shared UI components are placed inside `components/` to maximize reuse
across features.

------------------------------------------------------------------------

### 4️⃣ Scalable State Management

Global state is managed inside `store/`, allowing: - Centralized state
handling - Predictable data flow - Easy debugging

------------------------------------------------------------------------

## 🚀 Getting Started

### Install dependencies

``` bash
npm install
```

### Run development server

``` bash
npm run dev
```

### Build for production

``` bash
npm run build
```

------------------------------------------------------------------------

## 📦 Tech Stack

-   React
-   TypeScript
-   Vite
-   Modern State Management (Redux/Zustand)
-   Modular Architecture

------------------------------------------------------------------------

## 📌 Best Practices

-   Keep components small and reusable
-   Avoid business logic inside UI components
-   Organize code by feature when possible
-   Use TypeScript types consistently
-   Follow consistent naming conventions

------------------------------------------------------------------------

## 👨‍💻 Author

Code Web Không Khó

---
## 📚 Dạy Học Online

Bên cạnh tài liệu miễn phí, mình còn mở các khóa học online:

- **Lập trình web cơ bản → nâng cao**
- **Ứng dụng về AI và Automation**
- **Kỹ năng phỏng vấn & xây CV IT**

### Thông Tin Đăng Ký

- 🌐 Website: [https://codewebkhongkho.com](https://codewebkhongkho.com/portfolios)
- 📧 Email: nguyentientai10@gmail.com
- 📞 Zalo/Hotline: 0798805741

---

## 💖 Donate Ủng Hộ

Nếu bạn thấy các source hữu ích và muốn mình tiếp tục phát triển nội dung miễn phí, hãy ủng hộ mình bằng cách donate.  
Mình sẽ sử dụng kinh phí cho:

- 🌐 Server, domain, hosting
- 🛠️ Công cụ bản quyền (IDE, plugin…)
- 🎓 Học bổng, quà tặng cho cộng đồng

### QR Code Ngân Hàng

Quét QR để ủng hộ nhanh:

<img src="https://res.cloudinary.com/ecommerce2021/image/upload/v1760680573/abbank_yjbpat.jpg" alt="QR Code ABBank" width="300">


**QR Code ABBank**  
- Chủ tài khoản: Nguyễn Tiến Tài  
- Ngân hàng: NGAN HANG TMCP AN BINH  
- Số tài khoản: 1651002972052

---

## 📞 Liên Hệ

- 📚 Facebook Dạy Học: [Code Web Không Khó](https://www.facebook.com/codewebkhongkho)
- 📚 Tiktok Dạy Học: [@code.web.khng.kh](https://www.tiktok.com/@code.web.khng.kh)
- 💻 GitHub: [fdhhhdjd](https://github.com/fdhhhdjd)
- 📧 Email: [nguyentientai10@gmail.com](mailto:nguyentientai10@gmail.com)

Cảm ơn bạn đã quan tâm & chúc bạn học tập hiệu quả! Have a nice day <3!!

```

### File: src\components\readme.md
```md

```

### File: src\features\readme.md
```md

```

### File: src\pages\readme.md
```md

```

### File: src\routes\readme.md
```md

```

### File: src\store\readme.md
```md

```

### File: src\pages\dashboard\readme.md
```md

```

### File: index.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React + TS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### File: package-lock.json
```json
{
  "name": "react-enterprise-boilerplate",
  "version": "0.0.0",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "react-enterprise-boilerplate",
      "version": "0.0.0",
      "dependencies": {
        "@reduxjs/toolkit": "^1.9.3",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-redux": "^8.0.5"
      },
      "devDependencies": {
        "@types/react": "^18.0.28",
        "@types/react-dom": "^18.0.11",
        "@vitejs/plugin-react": "^3.1.0",
        "typescript": "^4.9.3",
        "vite": "^4.2.0"
      }
    },
    "node_modules/@ampproject/remapping": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/@ampproject/remapping/-/remapping-2.2.0.tgz",
      "integrity": "sha512-qRmjj8nj9qmLTQXXmaR1cck3UXSRMPrbsLJAasZpF+t3riI71BXed5ebIOYwQntykeZuhjsdweEc9BxH5Jc26w==",
      "dev": true,
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.1.0",
        "@jridgewell/trace-mapping": "^0.3.9"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.21.4.tgz",
      "integrity": "sha512-LYvhNKfwWSPpocw8GI7gpK2nq3HSDuEPC/uSYaALSJu9xjsalaaYFOq0Pwt5KmVqwEbZlDu81aLXwBOmD/Fv9g==",
      "dev": true,
      "dependencies": {
        "@babel/highlight": "^7.18.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.21.4.tgz",
      "integrity": "sha512-/DYyDpeCfaVinT40FPGdkkb+lYSKvsVuMjDAG7jPOWWiM1ibOaB9CXJAlc4d1QpP/U2q2P9jbrSlClKSErd55g==",
      "dev": true,
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.21.4.tgz",
      "integrity": "sha512-qt/YV149Jman/6AfmlxJ04LMIu8bMoyl3RB91yTFrxQmgbrSvQMy7cI8Q62FHx1t8wJ8B5fu0UDoLwHAhUo1QA==",
      "dev": true,
      "dependencies": {
        "@ampproject/remapping": "^2.2.0",
        "@babel/code-frame": "^7.21.4",
        "@babel/generator": "^7.21.4",
        "@babel/helper-compilation-targets": "^7.21.4",
        "@babel/helper-module-transforms": "^7.21.2",
        "@babel/helpers": "^7.21.0",
        "@babel/parser": "^7.21.4",
        "@babel/template": "^7.20.7",
        "@babel/traverse": "^7.21.4",
        "@babel/types": "^7.21.4",
        "convert-source-map": "^1.7.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.2",
        "semver": "^6.3.0"
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
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.21.4.tgz",
      "integrity": "sha512-NieM3pVIYW2SwGzKoqfPrQsf4xGs9M9AIG3ThppsSRmO+m7eQhmI6amajKMUeIO37wFfsvnvcxQFx6x6iqxDnA==",
      "dev": true,
      "dependencies": {
        "@babel/types": "^7.21.4",
        "@jridgewell/gen-mapping": "^0.3.2",
        "@jridgewell/trace-mapping": "^0.3.17",
        "jsesc": "^2.5.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/generator/node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.2.tgz",
      "integrity": "sha512-mh65xKQAzI6iBcFzwv28KVWSmCkdRBWoOh+bYQGW3+6OZvbbN3TqMGo5hqYxQniRcH9F2VZIoJCm4pa3BPDK/A==",
      "dev": true,
      "dependencies": {
        "@jridgewell/set-array": "^1.0.1",
        "@jridgewell/sourcemap-codec": "^1.4.10",
        "@jridgewell/trace-mapping": "^0.3.9"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.21.4.tgz",
      "integrity": "sha512-Fa0tTuOXZ1iL8IeDFUWCzjZcn+sJGd9RZdH9esYVjEejGmzf+FFYQpMi/kZUk2kPy/q1H3/GPw7np8qar/stfg==",
      "dev": true,
      "dependencies": {
        "@babel/compat-data": "^7.21.4",
        "@babel/helper-validator-option": "^7.21.0",
        "browserslist": "^4.21.3",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.0"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-environment-visitor": {
      "version": "7.18.9",
      "resolved": "https://registry.npmjs.org/@babel/helper-environment-visitor/-/helper-environment-visitor-7.18.9.tgz",
      "integrity": "sha512-3r/aACDJ3fhQ/EVgFy0hpj8oHyHpQc+LPtJoY9SzTThAsStm4Ptegq92vqKoE3vD706ZVFWITnMnxucw+S9Ipg==",
      "dev": true,
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-function-name": {
      "version": "7.21.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-function-name/-/helper-function-name-7.21.0.tgz",
      "integrity": "sha512-HfK1aMRanKHpxemaY2gqBmL04iAPOPRj7DxtNbiDOrJK+gdwkiNRVpCpUJYbUT+aZyemKN8brqTOxzCaG6ExRg==",
      "dev": true,
      "dependencies": {
        "@babel/template": "^7.20.7",
        "@babel/types": "^7.21.0"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-hoist-variables": {
      "version": "7.18.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-hoist-variables/-/helper-hoist-variables-7.18.6.tgz",
      "integrity": "sha512-UlJQPkFqFULIcyW5sbzgbkxn2FKRgwWiRexcuaR8RNJRy8+LLveqPjwZV/bwrLZCN0eUHD/x8D0heK1ozuoo6Q==",
      "dev": true,
      "dependencies": {
        "@babel/types": "^7.18.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.21.4.tgz",
      "integrity": "sha512-orajc5T2PsRYUN3ZryCEFeMDYwyw09c/pZeaQEZPH0MpKzSvn3e0uXsDBu3k03VI+9DBiRo+l22BfKTpKwa/Wg==",
      "dev": true,
      "dependencies": {
        "@babel/types": "^7.21.4"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.21.2",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.21.2.tgz",
      "integrity": "sha512-79yj2AR4U/Oqq/WOV7Lx6hUjau1Zfo4cI+JLAVYeMV5XIlbOhmjEk5ulbTc9fMpmlojzZHkUUxAiK+UKn+hNQQ==",
      "dev": true,
      "dependencies": {
        "@babel/helper-environment-visitor": "^7.18.9",
        "@babel/helper-module-imports": "^7.18.6",
        "@babel/helper-simple-access": "^7.20.2",
        "@babel/helper-split-export-declaration": "^7.18.6",
        "@babel/helper-validator-identifier": "^7.19.1",
        "@babel/template": "^7.20.7",
        "@babel/traverse": "^7.21.2",
        "@babel/types": "^7.21.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.20.2",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.20.2.tgz",
      "integrity": "sha512-8RvlJG2mj4huQ4pZ+rU9lqKi9ZKiRmuvGuM2HlWmkmgOhbs6zEAw6IEiJ5cQqGbDzGZOhwuOQNtZMi/ENLjZoQ==",
      "dev": true,
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-simple-access": {
      "version": "7.20.2",
      "resolved": "https://registry.npmjs.org/@babel/helper-simple-access/-/helper-simple-access-7.20.2.tgz",
      "integrity": "sha512-+0woI/WPq59IrqDYbVGfshjT5Dmk/nnbdpcF8SnMhhXObpTq2KNBdLFRFrkVdbDOyUmHBCxzm5FHV1rACIkIbA==",
      "dev": true,
      "dependencies": {
        "@babel/types": "^7.20.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-split-export-declaration": {
      "version": "7.18.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-split-export-declaration/-/helper-split-export-declaration-7.18.6.tgz",
      "integrity": "sha512-bde1etTx6ZyTmobl9LLMMQsaizFVZrquTEHOqKeQESMKo4PlObf+8+JA25ZsIpZhT/WEd39+vOdLXAFG/nELpA==",
      "dev": true,
      "dependencies": {
        "@babel/types": "^7.18.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.19.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.19.4.tgz",
      "integrity": "sha512-nHtDoQcuqFmwYNYPz3Rah5ph2p8PFeFCsZk9A/48dPc/rGocJ5J3hAAZ7pb76VWX3fZKu+uEr/FhH5jLx7umrw==",
      "dev": true,
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.19.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.19.1.tgz",
      "integrity": "sha512-awrNfaMtnHUr653GgGEs++LlAvW6w+DcPrOliSMXWCKo597CwL5Acf/wWdNkf/tfEQE3mjkeD1YOVZOUV/od1w==",
      "dev": true,
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.21.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.21.0.tgz",
      "integrity": "sha512-rmL/B8/f0mKS2baE9ZpyTcTavvEuWhTTW8amjzXNvYG4AwBsqTLikfXsEofsJEfKHf+HQVQbFOHy6o+4cnC/fQ==",
      "dev": true,
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.21.0",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.21.0.tgz",
      "integrity": "sha512-XXve0CBtOW0pd7MRzzmoyuSj0e3SEzj8pgyFxnTT1NJZL38BD1MK7yYrm8yefRPIDvNNe14xR4FdbHwpInD4rA==",
      "dev": true,
      "dependencies": {
        "@babel/template": "^7.20.7",
        "@babel/traverse": "^7.21.0",
        "@babel/types": "^7.21.0"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/highlight": {
      "version": "7.18.6",
      "resolved": "https://registry.npmjs.org/@babel/highlight/-/highlight-7.18.6.tgz",
      "integrity": "sha512-u7stbOuYjaPezCuLj29hNW1v64M2Md2qupEKP1fHc7WdOA3DgLh37suiSrZYY7haUB7iBeQZ9P1uiRF359do3g==",
      "dev": true,
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.18.6",
        "chalk": "^2.0.0",
        "js-tokens": "^4.0.0"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.21.4.tgz",
      "integrity": "sha512-alVJj7k7zIxqBZ7BTRhz0IqJFxW1VJbm6N8JbcYhQ186df9ZBPbZBmWSqAMXwHGsCJdYks7z/voa3ibiS5bCIw==",
      "dev": true,
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.21.0",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.21.0.tgz",
      "integrity": "sha512-f/Eq+79JEu+KUANFks9UZCcvydOOGMgF7jBrcwjHa5jTZD8JivnhCJYvmlhR/WTXBWonDExPoW0eO/CR4QJirA==",
      "dev": true,
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.20.2"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.19.6",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.19.6.tgz",
      "integrity": "sha512-RpAi004QyMNisst/pvSanoRdJ4q+jMCWyk9zdw/CyLB9j8RXEahodR6l2GyttDRyEVWZtbN+TpLiHJ3t34LbsQ==",
      "dev": true,
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.19.0"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.21.0",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.21.0.tgz",
      "integrity": "sha512-xwII0//EObnq89Ji5AKYQaRYiW/nZ3llSv29d49IuxPhKbtJoLP+9QUUZ4nVragQVtaVGeZrpB+ZtG/Pdy/POw==",
      "dependencies": {
        "regenerator-runtime": "^0.13.11"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.20.7",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.20.7.tgz",
      "integrity": "sha512-8SegXApWe6VoNw0r9JHpSteLKTpTiLZ4rMlGIm9JQ18KiCtyQiAMEazujAHrUS5flrcqYZa75ukev3P6QmUwUw==",
      "dev": true,
      "dependencies": {
        "@babel/code-frame": "^7.18.6",
        "@babel/parser": "^7.20.7",
        "@babel/types": "^7.20.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.21.4.tgz",
      "integrity": "sha512-eyKrRHKdyZxqDm+fV1iqL9UAHMoIg0nDaGqfIOd8rKH17m5snv7Gn4qgjBoFfLz9APvjFU/ICT00NVCv1Epp8Q==",
      "dev": true,
      "dependencies": {
        "@babel/code-frame": "^7.21.4",
        "@babel/generator": "^7.21.4",
        "@babel/helper-environment-visitor": "^7.18.9",
        "@babel/helper-function-name": "^7.21.0",
        "@babel/helper-hoist-variables": "^7.18.6",
        "@babel/helper-split-export-declaration": "^7.18.6",
        "@babel/parser": "^7.21.4",
        "@babel/types": "^7.21.4",
        "debug": "^4.1.0",
        "globals": "^11.1.0"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.21.4",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.21.4.tgz",
      "integrity": "sha512-rU2oY501qDxE8Pyo7i/Orqma4ziCOrby0/9mvbDUGEfvZjb279Nk9k19e2fiCxHbRRpY2ZyrgW1eq22mvmOIzA==",
      "dev": true,
      "dependencies": {
        "@babel/helper-string-parser": "^7.19.4",
        "@babel/helper-validator-identifier": "^7.19.1",
        "to-fast-properties": "^2.0.0"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.17.15",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.17.15.tgz",
      "integrity": "sha512-sRSOVlLawAktpMvDyJIkdLI/c/kdRTOqo8t6ImVxg8yT7LQDUYV5Rp2FKeEosLr6ZCja9UjYAzyRSxGteSJPYg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
      
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ESNext"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": false,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}

```

### File: tsconfig.node.json
```json
{
  "compilerOptions": {
    "composite": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}

```

### File: vite.config.ts
```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})

```

### File: src\App.css
```css
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}

```

### File: src\index.css
```css
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}

a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button {
    background-color: #f9f9f9;
  }
}

```

### File: src\vite-env.d.ts
```ts
/// <reference types="vite/client" />

```

### File: src\hooks\index.ts
```ts

```

### File: src\hooks\useFetch.ts
```ts

```

### File: src\hooks\useLocalStorage.ts
```ts

```

### File: src\routes\index.ts
```ts

```

### File: src\routes\routes.ts
```ts

```

### File: src\store\store.ts
```ts

```

### File: src\pages\dashboard\dashboardConstant.ts
```ts

```

### File: src\pages\dashboard\dashboardHooks.ts
```ts

```

