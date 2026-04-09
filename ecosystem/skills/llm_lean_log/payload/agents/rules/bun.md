---
trigger: always_on
---

# Default to using Bun instead of Node.js

- Use `bun run <file>` instead of `node <file>` or `ts-node <file>`
- Use `bun i` instead of `npm install` or `yarn install` or `pnpm install`
- Use `bun run <script>` instead of `npm run <script>` or `yarn run <script>` or `pnpm run <script>`
- Use `bux` instead of `npx`.
- Bun automatically loads .env, so don't use dotenv.
