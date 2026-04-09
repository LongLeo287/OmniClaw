---
trigger: always_on
---

# Common rules for LLM agent

When change codes, always run unit tests: `bun test`.
When change codes, always run TypeCheck: `bun tsc --noEmit`.

Whenever you finish a task or a request from developer, always log your work using the l-log bash command (llm-lean-log-cli package) with the following format:

`l-log add ./logs/chat.csv "<Task Name>" --tags="<tags>" --problem="<problem>" --solution="<solution>" --action="<action>" --files="<files>" --tech-stack="<tech>" --created-by-agent="<agent-name>"`

Note: `--last-commit-short-sha` is optional and will be auto-populated by the CLI if not provided.

Before run:

- Install the l-log CLI if not already installed: `bun add -g llm-lean-log-cli`.
- If need, run CLI help command: `l-log -h` for more information.
- log path: `./logs/chat.csv`.

## When use `console.log` / `console.warn` / `console.error`

Use `\n` to separate multiple lines of text if need.
