---
id: telegram
type: knowledge
owner: OA_Triage
---
# telegram
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![](https://badge.mcpx.dev?type=server 'MCP Server')](https://github.com/punkpeye/awesome-mcp-servers?tab=readme-ov-file#communication)
[![](https://img.shields.io/badge/OS_Agnostic-Works_Everywhere-purple)](https://github.com/chaindead/telegram-mcp?tab=readme-ov-file#installation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fchaindead%2Ftelegram-mcp&label=Visitors&labelColor=%23d9e3f0&countColor=%23697689&style=flat&labelStyle=none)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fchaindead%2Ftelegram-mcp)

# Telegram MCP server

The server is a bridge between the Telegram API and the AI assistants and is based on the [Model Context Protocol](https://modelcontextprotocol.io).

> [!IMPORTANT]
> Ensure that you have read and understood the [Telegram API Terms of Service](https://core.telegram.org/api/terms) before using this server.
> Any misuse of the Telegram API may result in the suspension of your account.

## Table of Contents
- [What is MCP?](#what-is-mcp)
- [What does this server do?](#what-does-this-server-do)
  - [Capabilities](#capabilities)
  - [Prompt examples](#prompt-examples)
    - [Message Management](#message-management)
    - [Organization](#organization)
    - [Communication](#communication)
- [Installation](#installation)
  - [Homebrew](#homebrew)
  - [NPX](#npx)
  - [From Releases](#from-releases)
    - [MacOS](#macos)
    - [Linux](#linux)
    - [Windows](#windows)
  - [From Source](#from-source)
- [Configuration](#configuration)
  - [Authorization](#authorization)
  - [Client Configuration](#client-configuration)
  - [JSON Schema Version](#json-schema-version)
- [Star History](#star-history)

## What is MCP?

The Model Context Protocol (MCP) is a system that lets AI apps, like Claude Desktop or Cursor, connect to external tools and data sources. It gives a clear and safe way for AI assistants to work with local services and APIs while keeping the user in control.

## What does this server do?

### Capabilities

- [x] Get current account information (`tool: tg_me`)
- [x] List dialogs with optional unread filter (`tool: tg_dialogs`)
- [x] Mark dialog as read (`tool: tg_read`)
- [x] Retrieve messages from specific dialog (`tool: tg_dialog`)
- [x] Send draft messages to any dialog (`tool: tg_send`)

### Prompt examples

Here are some example prompts you can use with AI assistants:

#### Message Management
- "Check for any unread important messages in my Telegram"
- "Summarize all my unread Telegram messages"
- "Read and analyze my unread messages, prepare draft responses where needed"
- "Check non-critical unread messages and give me a brief overview"

#### Organization
- "Analyze my Telegram dialogs and suggest a folder structure"
- "Help me categorize my Telegram chats by importance"
- "Find all work-related conversations and suggest how to organize them"

#### Communication
- "Monitor specific chat for updates about [topic]"
- "Draft a polite response to the last message in [chat]"
- "Check if there are any unanswered questions in my chats"

## Installation

### Homebrew

You can install a binary release on macOS/Linux using brew:

```bash
# Install
brew install chaindead/tap/telegram-mcp

# Update
brew upgrade chaindead/tap/telegram-mcp
```

### NPX

You can run the latest version directly using npx (supports macOS, Linux, and Windows):

```bash
npx -y @chaindead/telegram-mcp
```

When using NPX, modify the standard commands and configuration as follows:

- [Authentication command](#authorization) becomes:
```bash
npx -y @chaindead/telegram-mcp auth ...
```

- [Claude MCP server configuration](#client-configuration) becomes:
```json
{
  "mcpServers": {
    "telegram": {
      "command": "npx",
      "args": ["-y", "@chaindead/telegram-mcp"],
      "env": {
        "TG_APP_ID": "<your-api-id>",
        "TG_API_HASH": "<your-api-hash>"
      }
    }
  }
}
```

For complete setup instructions, see [Authorization](#authorization) and [Client Configuration](#client-configuration).

### From Releases

#### MacOS

<details>

> **Note:** The commands below install to `/usr/local/bin`. To install elsewhere, replace `/usr/local/bin` with your preferred directory in your PATH.

First, download the archive for your architecture:

```bash
# For Intel Mac (x86_64)
curl -L -o telegram-mcp.tar.gz https://github.com/chaindead/telegram-mcp/releases/latest/download/telegram-mcp_Darwin_x86_64.tar.gz

# For Apple Silicon (M1/M2)
curl -L -o telegram-mcp.tar.gz https://github.com/chaindead/telegram-mcp/releases/latest/download/telegram-mcp_Darwin_arm64.tar.gz
```

Then install the binary:

```bash
# Extract the binary
sudo tar xzf telegram-mcp.tar.gz -C /usr/local/bin

# Make it executable
sudo chmod +x /usr/local/bin/telegram-mcp

# Clean up
rm telegram-mcp.tar.gz
```
</details>

#### Linux
<details>

> **Note:** The commands below install to `/usr/local/bin`. To install elsewhere, replace `/usr/local/bin` with your preferred directory in your PATH.

First, download the archive for your architecture:

```bash
# For x86_64 (64-bit)
curl -L -o telegram-mcp.tar.gz https://github.com/chaindead/telegram-mcp/releases/latest/download/telegram-mcp_Linux_x86_64.tar.gz

# For ARM64
curl -L -o telegram-mcp.tar.gz https://github.com/chaindead/telegram-mcp/releases/latest/download/telegram-mcp_Linux_arm64.tar.gz
```

Then install the binary:

```bash
# Extract the binary
sudo tar xzf telegram-mcp.tar.gz -C /usr/local/bin

# Make it executable
sudo chmod +x /usr/local/bin/telegram-mcp

# Clean up
rm telegram-mcp.tar.gz
```
</details>

#### Windows

<details>

#### Windows
1. Download the latest release for your architecture:
   - [Windows x64](https://github.com/chaindead/telegram-mcp/releases/latest/download/telegram-mcp_Windows_x86_64.zip)
   - [Windows ARM64](https://github.com/chaindead/telegram-mcp/releases/latest/download/telegram-mcp_Windows_arm64.zip)
2. Extract the `.zip` file
3. Add the extracted directory to your PATH or move `telegram-mcp.exe` to a directory in your PATH
</details>

### From Source

Requirements:
- Go 1.24 or later
- GOBIN in PATH

```bash
go install github.com/chaindead/telegram-mcp@latest
```

## Configuration

### Authorization

Before you can use the server, you need to connect to the Telegram API.

1. Get the API ID and hash from [Telegram API](https://my.telegram.org/auth)
2. Run the following command:
   > __Note:__
   > If you have 2FA enabled: add --password <2fa_password>

   >  __Note:__
   > If you want to override existing session: add --new

   ```bash
   telegram-mcp auth --app-id <your-api-id> --api-hash <your-api-hash> --phone <your-phone-number>
   ```

   📩 Enter the code you received from Telegram to connect to the API.

3. Done! Please give this project a ⭐️ to support its development.

### Client Configuration

Example of Configuring Claude Desktop to recognize the Telegram MCP server.

1. Open the Claude Desktop configuration file:
    - in MacOS, the configuration file is located at `~/Library/Application Support/Claude/claude_desktop_config.json`
    - in Windows, the configuration file is located at `%APPDATA%\Claude\claude_desktop_config.json`

   > __Note:__
   > You can also find claude_desktop_config.json inside the settings of Claude Desktop app

2. Add the server configuration
   
   for Claude desktop:
   ```json
    {
      "mcpServers": {
        "telegram": {
          "command": "telegram-mcp",
          "env": {
            "TG_APP_ID": "<your-app-id>",
            "TG_API_HASH": "<your-api-hash>",
            "PATH": "<path_to_telegram-mcp_binary_dir>",
            "HOME": "<path_to_your_home_directory"
          }
        }
      }
    }
   ```

   for Cursor:
    ```json
    {
      "mcpServers": {
        "telegram-mcp": {
          "command": "telegram-mcp",
          "env": {
            "TG_APP_ID": "<your-app-id>",
            "TG_API_HASH": "<your-api-hash>"
          }
        }
      }
    }
    ```

### JSON Schema Version

Some MCP clients (e.g. VS Code) do not support JSON Schema Draft 2020-12 and will reject tools that use it. You can override the JSON Schema version by setting the `--schema-version` flag or the `TG_SCHEMA_VERSION` environment variable.

Common values:
| Version | URL |
|---------|-----|
| Draft-07 (recommended for VS Code) | `https://json-schema.org/draft-07/schema#` |
| Draft 2020-12 (default) | `https://json-schema.org/draft/2020-12/schema` |

## Star History

<a href="https://www.star-history.com/#chaindead/telegram-mcp&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=chaindead/telegram-mcp&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=chaindead/telegram-mcp&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=chaindead/telegram-mcp&type=Date" />
 </picture>
</a>
```

### File: .golangci.yaml
```yaml
run:
  concurrency: 4
  timeout: 10m
  issues-exit-code: 2
  tests: true
  build-tags: []
  allow-parallel-runners: true
  allow-serial-runners: true
  go: '1.24'

output:
  formats:
    - format: colored-line-number
  print-issued-lines: true
  print-linter-name: true
  path-prefix: ""
  sort-results: true
  sort-order:
    - linter
    - severity
    - file
  show-stats: true

linters:
  enable:
    - errcheck
    - govet
    - gosimple
    - ineffassign
    - staticcheck
    - unused
    - asciicheck
    - bodyclose
    - canonicalheader
    - copyloopvar
    - dupl
    - errorlint
    - gocheckcompilerdirectives
    - gochecknoinits
    - gocognit
    - goconst
    - gocritic
    - gocyclo
    - gosec
    - grouper
    - inamedparam
    - lll
    - makezero
    - nestif
    - nilerr
    - nilnil
    - nlreturn
    - noctx
    - perfsprint
    - prealloc
    - revive
    - testifylint
    - whitespace
    - importas
    - wrapcheck
    - nolintlint

linters-settings:
  lll:
    line-length: 150

  wrapcheck:
    ignoreSigs:
      - github.com/pkg/errors.Wrap(
      - github.com/pkg/errors.Wrapf(
      - github.com/pkg/errors.New(
      - fmt.Errorf

  gocyclo:
    min-complexity: 15

  dupl:
    threshold: 100

issues:
  exclude-dirs-use-default: true
  exclude-files: []
  exclude-rules:
    - path: _test\.go
      linters:
        - gocyclo
        - errcheck
        - dupl
        - gosec
        - lll
    - path: internal/config/
      linters:
        - importas
    - path: cmd/.*\.go
      text: "exitAfterDefer"
      linters:
        - gocritic
    - text: "should be written without leading space as"
      linters: [nolintlint]

```

### File: .goreleaser.yaml
```yaml
version: 2

builds:
  - env:
      - CGO_ENABLED=0
    goos:
      - linux
      - windows
      - darwin
    goarch:
      - amd64
      - arm64
    main: .
    binary: telegram-mcp
    ldflags:
      - -s -w

archives:
  - name_template: >-
      {{ .ProjectName }}_
      {{- title .Os }}_
      {{- if eq .Arch "amd64" }}x86_64
      {{- else }}{{ .Arch }}{{ end }}
    format_overrides:
      - goos: windows
        formats: zip
    files: []

changelog:
  use: github
  sort: asc
  filters:
    exclude:
      - "^docs:"
      - typo
      - readme
    include:
      - "^feat:"

checksum:
  name_template: '{{ .ProjectName }}_{{ .Version }}_checksums.txt'
  algorithm: sha256

brews:
  - name: telegram-mcp
    homepage: "https://github.com/chaindead/telegram-mcp"
    description: "Telegram MCP server for AI assistants"
    license: "MIT"
    repository:
      owner: chaindead
      name: homebrew-tap
    install: |
      bin.install "telegram-mcp"
    test: |
      system "#{bin}/telegram-mcp", "--version"
    
```

### File: auth.go
```go
package main

import (
	"context"
	"encoding/json"
	"strconv"

	"github.com/chaindead/telegram-mcp/internal/tg"

	"github.com/rs/zerolog/log"
	"github.com/urfave/cli/v3"
)

func authCommand(_ context.Context, cmd *cli.Command) error {
	phone := cmd.String("phone")
	newSession := cmd.Bool("new")
	pass := cmd.String("password")
	appID := cmd.Root().Int("app-id")
	apiHash := cmd.Root().String("api-hash")
	sessionPath := cmd.Root().String("session")

	log.Info().
		Str("phone", phone).
		Str("api-hash", apiHash).
		Str("session", sessionPath).
		Int64("app-id", appID).
		Msg("Authenticate with Telegram")

	err := tg.Auth(phone, appID, apiHash, sessionPath, pass, newSession)
	if err != nil {
		log.Fatal().Err(err).Msg("Failed to authenticate with Telegram")
	}

	c := struct {
		Telegram struct {
			Command string `json:"command"`
			Env     struct {
				AppID   string `json:"TG_APP_ID"`
				APIHash string `json:"TG_API_HASH"`
			} `json:"env"`
		} `json:"telegram"`
	}{
		Telegram: struct {
			Command string `json:"command"`
			Env     struct {
				AppID   string `json:"TG_APP_ID"`
				APIHash string `json:"TG_API_HASH"`
			} `json:"env"`
		}{
			Command: "telegram-mcp",
			Env: struct {
				AppID   string `json:"TG_APP_ID"`
				APIHash string `json:"TG_API_HASH"`
			}{
				AppID:   strconv.FormatInt(appID, 10),
				APIHash: apiHash,
			},
		},
	}

	data, _ := json.MarshalIndent(c, "", "\t")
	log.Info().RawJSON("config", data).Msg("Successfully authenticated with Telegram")

	return nil
}

```

### File: main.go
```go
package main

import (
	"context"
	"os"
	"path/filepath"

	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/urfave/cli/v3"
)

const (
	dir = ".telegram-mcp"
)

func main() {
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})

	debugPath := os.Getenv("TG_DEBUG_LOG")
	if debugPath != "" {
		logFile, err := os.OpenFile(debugPath, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
		if err != nil {
			log.Fatal().Err(err).Msg("Failed to open debug log file")
		}

		log.Logger = log.Output(logFile)
		log.Info().Msgf("Enabling debug logging to %s", debugPath)
	}

	homeDir, err := os.UserHomeDir()
	if err != nil {
		log.Fatal().Err(err).Msg("Failed to get home dir")
	}

	configDir := filepath.Join(homeDir, dir)
	sesionPath := filepath.Join(configDir, "session.json")

	app := &cli.Command{
		Name:  "telegram-mcp",
		Usage: "Telegram MCP server",
		Flags: []cli.Flag{
			&cli.IntFlag{
				Name:     "app-id",
				Usage:    "Telegram App ID",
				Required: true,
				Sources:  cli.EnvVars("TG_APP_ID"),
			},
			&cli.StringFlag{
				Name:     "api-hash",
				Usage:    "Telegram API Hash",
				Required: true,
				Sources:  cli.EnvVars("TG_API_HASH"),
			},
			&cli.StringFlag{
				Name:    "session",
				Usage:   "Path to session file",
				Value:   sesionPath,
				Sources: cli.EnvVars("TG_SESSION_PATH"),
			},
			&cli.StringFlag{
				Name:    "schema-version",
				Usage:   "JSON Schema version URL (e.g. https://json-schema.org/draft-07/schema#)",
				Sources: cli.EnvVars("TG_SCHEMA_VERSION"),
			},
			&cli.BoolFlag{
				Name:        "dry",
				Usage:       "Test configuration",
				Local:       true,
				HideDefault: true,
			},
		},
		Commands: []*cli.Command{
			{
				Name:  "auth",
				Usage: "Authenticate with Telegram",
				Flags: []cli.Flag{
					&cli.StringFlag{
						Name:     "phone",
						Usage:    "Phone number to authenticate with",
						Required: true,
						Aliases:  []string{"p"},
					},
					&cli.StringFlag{
						Name:        "password",
						Usage:       "Password for 2FA if exists",
						HideDefault: true,
					},
					&cli.BoolFlag{
						Name:        "new",
						Usage:       "Remove old session and create new one",
						HideDefault: true,
					},
				},
				Action: authCommand,
			},
		},
		Action: serve,
	}

	if err := app.Run(context.Background(), os.Args); err != nil {
		log.Fatal().Msg(err.Error())
	}
}

```

### File: serve.go
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/chaindead/telegram-mcp/internal/tg"
	"github.com/invopop/jsonschema"

	mcp "github.com/metoro-io/mcp-golang"
	"github.com/metoro-io/mcp-golang/transport/stdio"
	"github.com/rs/zerolog/log"
	"github.com/urfave/cli/v3"
)

func serve(ctx context.Context, cmd *cli.Command) error {
	appID := cmd.Int("app-id")
	appHash := cmd.String("api-hash")
	sessionPath := cmd.String("session")
	dryRun := cmd.Bool("dry")

	if schemaURL := cmd.String("schema-version"); schemaURL != "" {
		jsonschema.Version = schemaURL
	}

	_, err := os.Stat(sessionPath)
	if err != nil {
		return fmt.Errorf("session file not found(%s): %w", sessionPath, err)
	}

	server := mcp.NewServer(stdio.NewStdioServerTransport())
	client := tg.New(int(appID), appHash, sessionPath)

	if dryRun {
		answer, err := client.GetMe(tg.EmptyArguments{})
		if err != nil {
			return fmt.Errorf("get user: %w", err)
		}

		data, err := json.MarshalIndent(answer, "", "  ")
		if err != nil {
			return fmt.Errorf("marshal: %w", err)
		}

		log.Info().RawJSON("answer", data).Msg("Check GetMe: OK")

		answer, err = client.GetDialogs(tg.DialogsArguments{Offset: "", OnlyUnread: true})
		if err != nil {
			return fmt.Errorf("get dialogs: %w", err)
		}

		log.Info().RawJSON("answer", []byte(answer.Content[0].TextContent.Text)).Msg("Check GetDialogs: OK")

		answer, err = client.GetHistory(tg.HistoryArguments{Name: os.Getenv("TG_TEST_USERNAME")})
		if err != nil {
			return fmt.Errorf("get nickname history: %w", err)
		}

		answer, err = client.GetHistory(tg.HistoryArguments{Name: "cht[4626931529]"})
		if err != nil {
			return fmt.Errorf("get chat history: %w", err)
		}

		answer, err = client.GetHistory(tg.HistoryArguments{Name: "chn[2225853048:8934705438195741763]"})
		if err != nil {
			return fmt.Errorf("get chan history: %w", err)
		}

		log.Info().RawJSON("answer", []byte(answer.Content[0].TextContent.Text)).Msg("Check GetHistory: OK")

		answer, err = client.SendDraft(tg.DraftArguments{Name: os.Getenv("TG_TEST_USERNAME"), Text: "test draft"})
		if err != nil {
			log.Err(err).Msg("Check SendDraft: FAIL")
		} else {
			log.Info().RawJSON("answer", []byte(answer.Content[0].TextContent.Text)).Msg("Check SendDraft: OK")
		}

		answer, err = client.ReadHistory(tg.ReadArguments{Name: os.Getenv("TG_TEST_USERNAME")})
		if err != nil {
			log.Err(err).Msg("Check ReadHistory: FAIL")
		} else {
			log.Info().RawJSON("answer", []byte(answer.Content[0].TextContent.Text)).Msg("Check ReadHistory: OK")
		}

		return nil
	}

	err = server.RegisterTool("tg_me", "Get current telegram account info", client.GetMe)
	if err != nil {
		return fmt.Errorf("register tool: %w", err)
	}

	err = server.RegisterTool("tg_dialogs", "Get list of telegram dialogs (chats, channels, users)", client.GetDialogs)
	if err != nil {
		return fmt.Errorf("register dialogs tool: %w", err)
	}

	err = server.RegisterTool("tg_dialog", "Get messages of telegram dialog", client.GetHistory)
	if err != nil {
		return fmt.Errorf("register dialogs tool: %w", err)
	}

	err = server.RegisterTool("tg_send", "Send draft message to dialog", client.SendDraft)
	if err != nil {
		return fmt.Errorf("register dialogs tool: %w", err)
	}

	err = server.RegisterTool("tg_read", "Mark dialog messages as read", client.ReadHistory)
	if err != nil {
		return fmt.Errorf("register read tool: %w", err)
	}

	if err := server.Serve(); err != nil {
		return fmt.Errorf("serve: %w", err)
	}

	<-ctx.Done()

	return nil
}

```

### File: cmd\test\main.go
```go
package main

import (
	"context"
	"os"
	"os/signal"
	"strconv"

	"github.com/chaindead/telegram-mcp/internal/tg"
	"github.com/pkg/errors"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
)

func main() {
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	log.Logger = log.Output(zerolog.ConsoleWriter{
		Out:        os.Stderr,
		TimeFormat: zerolog.TimeFormatUnix,
	})

	appIDStr, apiHash, sessionPath := os.Getenv("TG_APP_ID"), os.Getenv("TG_API_HASH"), os.Getenv("TG_SESSION_PATH")
	if appIDStr == "" {
		log.Fatal().Msg("TG_APP_ID is required")
	}
	if apiHash == "" {
		log.Fatal().Msg("TG_API_HASH is required")
	}
	if sessionPath == "" {
		log.Fatal().Msg("TG_SESSION_PATH is required")
	}

	appID, err := strconv.Atoi(appIDStr)
	if err != nil {
		log.Fatal().Err(err).Msg("TG_APP_ID app id")
	}

	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)
	defer cancel()

	client := tg.New(appID, apiHash, sessionPath).T()

	if err := client.Run(ctx, func(ctx context.Context) error {
		self, err := client.Self(ctx)
		if err != nil {
			return errors.Wrap(err, "get self")
		}

		log.Info().
			Str("first_name", self.FirstName).
			Str("last_name", self.LastName).
			Str("username", self.Username).
			Int64("id", self.ID).
			Msg("Logged in as")

		messages, err := getUnreadMessages(ctx, client)
		if err != nil {
			return errors.Wrap(err, "get unread messages")
		}

		for _, msg := range messages {
			log.Info().
				Int("id", msg.ID).
				Str("text", msg.Text).
				Time("date", msg.Date).
				Int64("from_id", msg.FromID).
				Str("from_name", msg.FromName).
				Str("chat_type", msg.ChatType).
				Str("chat_title", msg.ChatTitle).
				Msg("Unread message")
		}

		return nil
	}); err != nil {
		log.Fatal().Err(err).Msg("client error")
	}
}

```

### File: cmd\test\unread.go
```go
package main

import (
	"context"
	"sort"
	"time"

	"github.com/gotd/td/telegram"
	"github.com/gotd/td/tg"
	"github.com/pkg/errors"
	"github.com/rs/zerolog/log"
	cfg "github.com/spf13/pflag"
	"golang.org/x/time/rate"
)

const (
	defaultMessageLimit = 10
	maxDialogsLimit     = 100
	rateLimitPerSec     = 5
)

//nolint:gochecknoglobals // CLI flags must be global
var (
	messageLimit = cfg.Int("limit", defaultMessageLimit, "limit of unread messages to fetch")
)

//nolint:gochecknoglobals // Rate limiter should be global for consistent rate limiting across all functions
var telegramLimiter = rate.NewLimiter(rate.Limit(rateLimitPerSec), 1)

// UnreadMessage represents a simplified message structure
type UnreadMessage struct {
	ID        int
	Text      string
	Date      time.Time
	FromID    int64
	FromName  string
	ChatType  string
	ChatTitle string
}

// DialogWithUnread represents a dialog with its unread count and latest message ID
type DialogWithUnread struct {
	Dialog      *tg.Dialog
	UnreadCount int
	TopMessage  int
}

// getUnreadMessages fetches unread messages from different users
//
//nolint:gocognit,gocyclo // complexity is inherent to handling different types of Telegram messages and users
func getUnreadMessages(ctx context.Context, client *telegram.Client) ([]UnreadMessage, error) {
	if err := telegramLimiter.Wait(ctx); err != nil {
		return nil, errors.Wrap(err, "rate limiter wait")
	}

	api := client.API()
	dialogsClass, err := api.MessagesGetDialogs(ctx, &tg.MessagesGetDialogsRequest{
		OffsetPeer:    &tg.InputPeerEmpty{},
		OffsetDate:    0,
		OffsetID:      0,
		Limit:         maxDialogsLimit,
		Hash:          0,
		Flags:         0,
		ExcludePinned: false,
		FolderID:      0,
	})
	if err != nil {
		return nil, errors.Wrap(err, "get dialogs")
	}

	var dialogs *tg.MessagesDialogs
	switch d := dialogsClass.(type) {
	case *tg.MessagesDialogs:
		dialogs = d
	case *tg.MessagesDialogsSlice:
		dialogs = &tg.MessagesDialogs{
			Dialogs:  d.Dialogs,
			Messages: d.Messages,
			Chats:    d.Chats,
			Users:    d.Users,
		}
	default:
		return nil, errors.New("unexpected dialogs response type")
	}

	// Create a slice of dialogs with unread count
	dialogsWithUnread := make([]DialogWithUnread, 0, len(dialogs.Dialogs))
	for _, dialog := range dialogs.Dialogs {
		dialogItem, ok := dialog.(*tg.Dialog)
		if !ok {
			continue
		}

		if dialogItem.UnreadCount > 0 {
			dialogsWithUnread = append(dialogsWithUnread, DialogWithUnread{
				Dialog:      dialogItem,
				UnreadCount: dialogItem.UnreadCount,
				TopMessage:  dialogItem.TopMessage,
			})
		}
	}

	// Sort dialogs by TopMessage in descending order (newest first)
	sort.Slice(dialogsWithUnread, func(i, j int) bool {
		return dialogsWithUnread[i].TopMessage > dialogsWithUnread[j].TopMessage
	})

	// Map to store the latest message from each user
	userMessages := make(map[int64]UnreadMessage)
	processedCount := 0

	for _, dialogWithUnread := range dialogsWithUnread {
		dialogItem := dialogWithUnread.Dialog

		var inputPeer tg.InputPeerClass
		var chatType, chatTitle string
		var fromID int64
		var fromName string

		switch peer := dialogItem.Peer.(type) {
		case *tg.PeerUser:
			for _, userItem := range dialogs.Users {
				user, ok := userItem.(*tg.User)
				if !ok || user.ID != peer.UserID {
					continue
				}

				inputPeer = &tg.InputPeerUser{
					UserID:     user.ID,
					AccessHash: user.AccessHash,
				}
				chatType = "user"
				chatTitle = user.FirstName + " " + user.LastName
				fromID = user.ID
				fromName = chatTitle

				break
			}
		case *tg.PeerChat:
			inputPeer = &tg.InputPeerChat{
				ChatID: peer.ChatID,
			}
			chatType = "chat"
			for _, chatItem := range dialogs.Chats {
				chat, ok := chatItem.(*tg.Chat)
				if !ok || chat.ID != peer.ChatID {
					continue
				}

				chatTitle = chat.Title

				break
			}
		case *tg.PeerChannel:
			for _, channelItem := range dialogs.Chats {
				channel, ok := channelItem.(*tg.Channel)
				if !ok || channel.ID != peer.ChannelID {
					continue
				}

				inputPeer = &tg.InputPeerChannel{
					ChannelID:  channel.ID,
					AccessHash: channel.AccessHash,
				}
				chatType = "channel"
				chatTitle = channel.Title

				break
			}
		}

		if inputPeer == nil {
			continue
		}

		if err := telegramLimiter.Wait(ctx); err != nil {
			return nil, errors.Wrap(err, "rate limiter wait")
		}

		messagesClass, err := api.MessagesGetHistory(ctx, &tg.MessagesGetHistoryRequest{
			Peer:       inputPeer,
			OffsetID:   0,
			OffsetDate: 0,
			AddOffset:  0,
			Limit:      1, // We only need the latest message
			MaxID:      0,
			MinID:      0,
			Hash:       0,
		})
		if err != nil {
			log.Error().Err(err).Msg("failed to get messages")

			continue
		}

		var messages *tg.MessagesMessages
		switch m := messagesClass.(type) {
		case *tg.MessagesMessages:
			messages = m
		case *tg.MessagesMessagesSlice:
			messages = &tg.MessagesMessages{
				Messages: m.Messages,
				Chats:    m.Chats,
				Users:    m.Users,
			}
		case *tg.MessagesChannelMessages:
			messages = &tg.MessagesMessages{
				Messages: m.Messages,
				Chats:    m.Chats,
				Users:    m.Users,
			}
		default:
			log.Error().Msg("unexpected messages response type")

			continue
		}

		for _, msg := range messages.Messages {
			message, ok := msg.(*tg.Message)
			if !ok {
				continue
			}

			if message.Out {
				continue
			}

			if message.FromID != nil {
				if from, ok := message.FromID.(*tg.PeerUser); ok {
					for _, userItem := range messages.Users {
						user, ok := userItem.(*tg.User)
						if !ok || user.ID != from.UserID {
							continue
						}

						fromID = user.ID
						fromName = user.FirstName + " " + user.LastName

						break
					}
				}
			}

			unreadMsg := UnreadMessage{
				ID:        message.ID,
				Text:      message.Message,
				Date:      time.Unix(int64(message.Date), 0),
				FromID:    fromID,
				FromName:  fromName,
				ChatType:  chatType,
				ChatTitle: chatTitle,
			}

			// Only store if we haven't seen this user yet or if this message is newer
			if existingMsg, exists := userMessages[fromID]; !exists || unreadMsg.Date.After(existingMsg.Date) {
				userMessages[fromID] = unreadMsg
				processedCount++
			}

			break // We only need the latest message
		}

		if len(userMessages) >= *messageLimit {
			break
		}
	}

	// Convert map to slice and sort by date
	messages := make([]UnreadMessage, 0, len(userMessages))
	for _, msg := range userMessages {
		messages = append(messages, msg)
	}

	// Sort messages by date in descending order
	sort.Slice(messages, func(i, j int) bool {
		return messages[i].Date.After(messages[j].Date)
	})

	return messages, nil
}

```

